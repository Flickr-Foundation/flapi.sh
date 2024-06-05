#!/usr/bin/env python3

import subprocess

from utils import get_success_stdout


def test_no_method_is_error(flickr_api_key):
    proc = subprocess.Popen(["./flapi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    assert proc.returncode == 1
    assert stdout == b""
    assert stderr.startswith(b"Usage: ")


def test_no_api_key_is_error():
    proc = subprocess.Popen(["./flapi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    assert proc.returncode == 1
    assert stdout == b""
    assert b"Unable to get Flickr API key from system keychain!" in stderr


def test_can_call_an_api(flickr_api_key):
    stdout = get_success_stdout(
        ["./flapi", "flickr.profile.getProfile", "user_id=197130754@N07"]
    )

    assert b"Flickr Foundation" in stdout
