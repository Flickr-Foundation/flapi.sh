"""
Tests for the ``fluser`` script.
"""

import pytest

from utils import get_failure_stderr, get_success_stdout


@pytest.mark.parametrize(
    "argv",
    [
        "197130754@N07",
        "https://www.flickr.com/people/197130754@N07",
        "https://www.flickr.com/photos/flickrfoundation/",
        "https://www.flickr.com/photos/197130754@N07/53630778857/",
        "https://www.flickr.com/photos/flickrfoundation/53630778857/",
    ],
)
def test_fluser_handles_different_variants(argv: str) -> None:
    """
    Look up a user with ``fluser`` with different inputs.
    """
    stdout = get_success_stdout(["./fluser", argv])
    assert stdout == (
        b"NSID:     197130754@N07\n"
        b"username: Flickr Foundation\n"
        b"realname: Flickr Foundation\n"
        b"URL:      https://www.flickr.com/photos/flickrfoundation/\n"
    )


def test_no_input_is_error() -> None:
    """
    Calling ``fluser`` without any arguments is an error.
    """
    stderr = get_failure_stderr(cmd=["fluser"])
    assert stderr.startswith(b"Usage: ")


def test_too_many_input_is_error() -> None:
    """
    Calling ``fluser`` with more than one argument is an error.
    """
    stderr = get_failure_stderr(
        cmd=["fluser", "https://www.flickr.com/photos/197130754@N07", "197130754@N07"]
    )
    assert stderr.startswith(b"Usage: ")


def test_unrecognised_url_is_error() -> None:
    """
    Calling ``fluser`` with a non-Flickr.com URL is an error.
    """
    stderr = get_failure_stderr(["fluser", "https://example.com"])
    assert stderr == b"Unrecognised URL: https://example.com\n"
