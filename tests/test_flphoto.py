"""
Tests for the ``flphoto`` script.
"""

from utils import get_failure_stderr, get_success_stdout


def test_no_method_is_error() -> None:
    """
    Calling ``flphoto`` without a photo ID is an error.
    """
    stderr = get_failure_stderr(cmd=["flphoto"])
    assert stderr.startswith("Usage: ")


def test_too_many_arguments_is_error() -> None:
    """
    Calling ``flphoto`` with more than one argument is an error.
    """
    stderr = get_failure_stderr(cmd=["flphoto"])
    assert stderr.startswith("Usage: ")


def test_can_look_up_a_photo_id() -> None:
    """
    Call ``flphoto`` with a photo ID.
    """
    stdout = get_success_stdout(cmd=["flphoto", "53630778857"])

    assert "https://www.flickr.com/photos/flickrfoundation/53630778857/" in stdout


def test_can_look_up_a_photo_url() -> None:
    """
    Call ``flphoto`` with a photo URL.
    """
    stdout = get_success_stdout(
        cmd=["flphoto", "https://www.flickr.com/photos/flickrfoundation/53630778857/"]
    )

    assert "https://www.flickr.com/photos/flickrfoundation/53630778857/" in stdout
