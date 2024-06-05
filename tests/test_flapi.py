#!/usr/bin/env python3

import subprocess


def test_no_method_is_error():
    proc = subprocess.Popen(["./flapi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    assert proc.returncode == 1
    assert stdout == b""
    assert stderr.startswith(b"Usage: ")


def test_can_call_an_api():
    proc = subprocess.Popen(
        ["./flapi", "flickr.profile.getProfile", "user_id=197130754@N07"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()

    assert proc.returncode == 0
    assert b"Flickr Foundation" in stdout
    assert stderr == b""
