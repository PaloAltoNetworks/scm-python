"""
JWT Token Caching Tests for scm-python

Tests JWT token caching functionality to ensure tokens are properly:
- Loaded from config file when fresh
- Shared across multiple client instances
- Handled correctly when expired
"""

import json
import os
import pytest
import tempfile
import time
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch, Mock
import threading

from scm import Scm


class TestJWTCaching:
    """Test suite for JWT token caching functionality"""

    @pytest.fixture
    def temp_config_file(self):
        """Create a temporary config file for testing"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            config_path = f.name
        yield config_path
        # Cleanup
        try:
            os.unlink(config_path)
        except FileNotFoundError:
            pass

    @pytest.fixture
    def sample_config_fresh_token(self):
        """Sample config with fresh JWT token"""
        return {
            "client_id": "test-client-id",
            "client_secret": "test-client-secret",
            "host": "api.test.paloaltonetworks.com",
            "auth_url": "https://auth.test.paloaltonetworks.com",
            "protocol": "https",
            "scope": "tsg_id:123456789",
            "logging": "ERROR",
            "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.test_token",
            "jwt_expires_at": (datetime.now() + timedelta(minutes=15)).isoformat(),
            "jwt_lifetime": 900
        }

    @pytest.fixture
    def sample_config_expired_token(self):
        """Sample config with expired JWT token"""
        return {
            "client_id": "test-client-id",
            "client_secret": "test-client-secret",
            "host": "api.test.paloaltonetworks.com",
            "auth_url": "https://auth.test.paloaltonetworks.com",
            "protocol": "https",
            "scope": "tsg_id:123456789",
            "logging": "ERROR",
            "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.expired_token",
            "jwt_expires_at": (datetime.now() - timedelta(hours=1)).isoformat(),
            "jwt_lifetime": 900
        }

    def save_config_atomic(self, path: str, config: dict):
        """Save config using atomic write (temp file then rename)"""
        temp_path = path + '.tmp'
        with open(temp_path, 'w') as f:
            json.dump(config, f, indent=2)
        os.rename(temp_path, path)

    def test_load_fresh_token_from_config(self, temp_config_file, sample_config_fresh_token):
        """Test loading a fresh JWT from config file"""
        # Save config with fresh token
        self.save_config_atomic(temp_config_file, sample_config_fresh_token)

        # Mock OAuth2 session to verify it's not called
        with patch('scm.OAuth2Session') as mock_oauth:
            with patch.dict(os.environ, {'SCM_CONFIG_FILE': temp_config_file}):
                client = Scm()

            # Verify OAuth was NOT called (token loaded from cache)
            mock_oauth.assert_not_called()

            # Verify token was loaded
            assert client._access_token == sample_config_fresh_token["jwt"]
            assert client._access_token is not None

    def test_expired_token_fetches_new(self, temp_config_file, sample_config_expired_token):
        """Test that expired token triggers new token fetch"""
        # Save config with expired token
        self.save_config_atomic(temp_config_file, sample_config_expired_token)

        # Mock OAuth2 session to return new token
        mock_token_response = {
            "access_token": "new_fresh_token",
            "expires_in": 900
        }

        with patch('scm.OAuth2Session') as mock_oauth:
            mock_session = Mock()
            mock_session.fetch_token.return_value = mock_token_response
            mock_oauth.return_value = mock_session

            with patch.dict(os.environ, {'SCM_CONFIG_FILE': temp_config_file}):
                client = Scm()

            # Verify OAuth was called to get new token
            mock_oauth.assert_called()

            # Verify new token was set
            assert client._access_token == "new_fresh_token"

    def test_missing_jwt_fields_fetches_token(self, temp_config_file):
        """Test that missing JWT fields triggers token fetch"""
        config = {
            "client_id": "test-client-id",
            "client_secret": "test-client-secret",
            "host": "api.test.paloaltonetworks.com",
            "auth_url": "https://auth.test.paloaltonetworks.com",
            "protocol": "https",
            "scope": "tsg_id:123456789",
            "logging": "ERROR"
            # No JWT fields
        }
        self.save_config_atomic(temp_config_file, config)

        mock_token_response = {
            "access_token": "fetched_token",
            "expires_in": 900
        }

        with patch('scm.OAuth2Session') as mock_oauth:
            mock_session = Mock()
            mock_session.fetch_token.return_value = mock_token_response
            mock_oauth.return_value = mock_session

            with patch.dict(os.environ, {'SCM_CONFIG_FILE': temp_config_file}):
                client = Scm()

            # Verify token was fetched
            assert client._access_token == "fetched_token"

    def test_concurrent_clients_share_token(self, temp_config_file, sample_config_fresh_token):
        """Test that multiple concurrent clients can share cached token"""
        self.save_config_atomic(temp_config_file, sample_config_fresh_token)

        tokens = []
        errors = []

        def create_client():
            try:
                with patch('scm.OAuth2Session'):
                    with patch.dict(os.environ, {'SCM_CONFIG_FILE': temp_config_file}):
                        client = Scm()
                        tokens.append(client._access_token)
            except Exception as e:
                errors.append(e)

        # Create 5 concurrent clients
        threads = []
        for _ in range(5):
            t = threading.Thread(target=create_client)
            threads.append(t)
            t.start()

        # Wait for all to complete
        for t in threads:
            t.join()

        # Verify no errors
        assert len(errors) == 0, f"Errors occurred: {errors}"

        # Verify all clients got the same token
        assert len(tokens) == 5
        assert all(token == sample_config_fresh_token["jwt"] for token in tokens)

    def test_invalid_config_file_raises_error(self):
        """Test behavior with invalid JSON in config file"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            f.write("invalid json{{{")
            invalid_config_path = f.name

        try:
            with patch.dict(os.environ, {'SCM_CONFIG_FILE': invalid_config_path}):
                # Should raise ValueError due to missing credentials
                with pytest.raises(ValueError, match="client_id and client_secret"):
                    Scm()
        finally:
            os.unlink(invalid_config_path)

    def test_missing_config_file_without_env_vars(self, temp_config_file):
        """Test behavior when config file doesn't exist and no env vars"""
        # Use non-existent path
        nonexistent_path = temp_config_file + ".nonexistent"

        with patch.dict(os.environ, {'SCM_CONFIG_FILE': nonexistent_path}, clear=True):
            # Should raise ValueError due to missing credentials
            with pytest.raises(ValueError, match="client_id and client_secret"):
                Scm()

    def test_token_expiring_soon_is_refreshed(self, temp_config_file):
        """Test that token expiring within buffer time is refreshed"""
        # Create token expiring in 30 seconds (less than 60 second buffer)
        config = {
            "client_id": "test-client-id",
            "client_secret": "test-client-secret",
            "host": "api.test.paloaltonetworks.com",
            "auth_url": "https://auth.test.paloaltonetworks.com",
            "protocol": "https",
            "scope": "tsg_id:123456789",
            "logging": "ERROR",
            "jwt": "expiring_soon_token",
            "jwt_expires_at": (datetime.now() + timedelta(seconds=30)).isoformat(),
            "jwt_lifetime": 900
        }
        self.save_config_atomic(temp_config_file, config)

        mock_token_response = {
            "access_token": "refreshed_token",
            "expires_in": 900
        }

        with patch('scm.OAuth2Session') as mock_oauth:
            mock_session = Mock()
            mock_session.fetch_token.return_value = mock_token_response
            mock_oauth.return_value = mock_session

            with patch.dict(os.environ, {'SCM_CONFIG_FILE': temp_config_file}):
                client = Scm()

            # Should have fetched new token (token expiring soon)
            assert client._access_token == "refreshed_token"

    @pytest.mark.skipif(
        not (os.getenv("SCM_CLIENT_ID") and os.getenv("SCM_CLIENT_SECRET")),
        reason="Integration test requires SCM_CLIENT_ID and SCM_CLIENT_SECRET"
    )
    def test_integration_refresh_expired_token(self, temp_config_file):
        """Integration test: Refresh expired token with real credentials"""
        config = {
            "client_id": os.getenv("SCM_CLIENT_ID"),
            "client_secret": os.getenv("SCM_CLIENT_SECRET"),
            "host": os.getenv("SCM_HOST", "api.sase.paloaltonetworks.com"),
            "auth_url": os.getenv("SCM_AUTH_URL", "https://auth.apps.paloaltonetworks.com"),
            "protocol": "https",
            "scope": os.getenv("SCM_SCOPE", f"tsg_id:{os.getenv('SCM_TSG_ID', '000000000')}"),
            "logging": "ERROR",
            "jwt": "old_expired_token",
            "jwt_expires_at": (datetime.now() - timedelta(hours=1)).isoformat(),
            "jwt_lifetime": 900
        }
        self.save_config_atomic(temp_config_file, config)

        with patch.dict(os.environ, {'SCM_CONFIG_FILE': temp_config_file}):
            client = Scm()

        # Verify new token was fetched
        assert client._access_token != "old_expired_token"
        assert client._access_token is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
