import os

import keyring
import pytest


@pytest.fixture
def flickr_api_key():
    keyring.set_password("flickr_api", "key", os.environ["FLICKR_API_KEY"])
    yield
    keyring.delete_password("flickr_api", "key")
