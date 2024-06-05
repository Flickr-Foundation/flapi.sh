import pytest

from utils import get_success_stdout


@pytest.mark.parametrize(
    "argv",
    [
        "197130754@N07",
        "https://www.flickr.com/people/197130754@N07",
        "https://www.flickr.com/photos/flickrfoundation/",
    ],
)
def test_fluser_handles_different_variants(argv: str):
    stdout = get_success_stdout(["./fluser", argv])
    assert stdout == (
        b"NSID:     197130754@N07\n"
        b"username: Flickr Foundation\n"
        b"realname: Flickr Foundation\n"
        b"URL:      https://www.flickr.com/photos/flickrfoundation/\n"
    )
