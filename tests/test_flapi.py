"""
Tests for the ``flapi`` script.
"""

from collections.abc import Iterator

import keyring
import pytest

from utils import get_failure_stderr, get_success_stdout


def test_no_method_is_error() -> None:
    """
    Calling ``flapi`` without an API method is an error.
    """
    stderr = get_failure_stderr(cmd=["flapi"])
    assert stderr.startswith("Usage: ")


@pytest.fixture
def no_flickr_api_key() -> Iterator[None]:
    """
    Temporarily remove the Flickr API key from the system keychain.
    """
    stored_password = keyring.get_password("flickr_api", "key")

    if stored_password:
        keyring.delete_password("flickr_api", "key")
        yield
        keyring.set_password("flickr_api", "key", stored_password)

    assert keyring.get_password("flickr_api", "key") == stored_password


def test_no_api_key_is_error(no_flickr_api_key: None) -> None:
    """
    Calling ``flapi`` if there's no API key in the keychain is an error.
    """
    stderr = get_failure_stderr(
        ["flapi", "flickr.profile.getProfile", "user_id=197130754@N07"]
    )
    assert "Unable to get Flickr API key from system keychain!" in stderr


def test_can_call_an_api_without_parameters() -> None:
    """
    Call ``flapi`` with just an API method, and no parameters.
    """
    stdout = get_success_stdout(["flapi", "flickr.commons.getInstitutions"])

    assert "http://flickr.com/photos/library_of_congress/" in stdout


def test_can_call_an_api_with_parameters() -> None:
    """
    Call ``flapi`` with an API method and parameters.
    """
    stdout = get_success_stdout(
        ["flapi", "flickr.profile.getProfile", "user_id=197130754@N07"]
    )

    assert "Flickr Foundation" in stdout
