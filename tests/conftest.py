"""
pytest fixtures and utilities.
"""

from collections.abc import Iterator
import os

import keyring
import pytest


@pytest.fixture
def flickr_api_key() -> Iterator[None]:
    """
    In CI, store a copy of the Flickr API in the system keychain.

    The ``flapi`` script expects to gets its API key from the keychain;
    in CI the API key is stored in an env var, which we copy into the
    keychain for the duration of this test only.
    """
    if os.environ.get("CI") == "true":
        keyring.set_password("flickr_api", "key", os.environ["FLICKR_API_KEY"])
        yield
        keyring.delete_password("flickr_api", "key")
    else:
        yield
