"""
Tests for the ``flapi`` script.
"""

import os

import pytest

from utils import get_failure_stderr, get_success_stdout


def test_no_method_is_error(flickr_api_key: None) -> None:
    """
    Calling ``flapi`` without an API method is an error.
    """
    stderr = get_failure_stderr(cmd=["flapi"])
    assert stderr.startswith(b"Usage: ")


@pytest.mark.skipif(
    os.environ.get("CI") != "true",
    reason="This requires a clean keychain with no Flickr API key",
)
def test_no_api_key_is_error() -> None:
    """
    Calling ``flapi`` if there's no API key in the keychain is an error.
    """
    stderr = get_failure_stderr(
        ["flapi", "flickr.profile.getProfile", "user_id=197130754@N07"]
    )
    assert b"Unable to get Flickr API key from system keychain!" in stderr


def test_can_call_an_api_without_parameters(flickr_api_key: None) -> None:
    """
    Call ``flapi`` with just an API method, and no parameters.
    """
    stdout = get_success_stdout(["flapi", "flickr.commons.getInstitutions"])

    assert b"http://flickr.com/photos/library_of_congress/" in stdout


def test_can_call_an_api_with_parameters(flickr_api_key: None) -> None:
    """
    Call ``flapi`` with an API method and parameters.
    """
    stdout = get_success_stdout(
        ["flapi", "flickr.profile.getProfile", "user_id=197130754@N07"]
    )

    assert b"Flickr Foundation" in stdout
