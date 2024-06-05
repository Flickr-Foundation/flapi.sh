import subprocess


def get_success_stdout(cmd: list[str]) -> bytes:
    """
    Run a command, check it returns a success status code, and return
    the bytes written to stdout.
    """
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()

    if proc.returncode != 0:
        print(f"stdout: {stdout}")
        print(f"stderr: {stderr}")

    assert proc.returncode == 0
    assert stderr == b""
    return stdout
