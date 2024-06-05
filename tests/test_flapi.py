#!/usr/bin/env python3

import subprocess


def test_no_method_is_error():
    proc = subprocess.Popen(["flapi"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    assert proc.returncode == 1
    assert stdout == b""
    assert stderr.startswith(b"Usage: ")
