"""Entry program for news-image-20261123.

The front page for Monday 23 November 2026 was rendered in the build
session and is stored beside this file as entry.png. This program only
copies that image to the grader's output directory and checks the copy
is a well-formed PNG of the expected size and hash. It performs a
byte-exact copy; no re-rendering happens here.

Usage: python3 main.py
Output: entry.png (1024x1024, 211,610 bytes) written to
$MAKEFUN_OUTPUT_DIR, or to <repo>/output when that variable is unset
or not writable. The program exits 0 only after the copy passes its
PNG-magic, size and sha256 checks.
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SHA256 = "b5bf967033272e4c60ac33e421a238a09a6547fad62ab18d34676e921d189d8c"
EXPECTED_SIZE = 211610


def repo_root():
    """Directory containing this file."""
    return os.path.dirname(os.path.abspath(__file__))


def output_dir():
    """Grader output directory.

    Uses $MAKEFUN_OUTPUT_DIR when it is set and writable, probed by
    creating and then removing a ".write-test" file inside it;
    otherwise falls back to <repo>/output, creating it if needed.
    """
    candidate = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if candidate:
        probe = os.path.join(candidate, ".write-test")
        try:
            with open(probe, "w") as handle:
                handle.write("ok")
            os.remove(probe)
            return candidate
        except OSError:
            pass
    fallback = os.path.join(repo_root(), "output")
    os.makedirs(fallback, exist_ok=True)
    return fallback


def main():
    """Copy entry.png to the output directory and verify the copy."""
    source = os.path.join(repo_root(), IMAGE_NAME)
    if not os.path.isfile(source):
        print("error: %s not found" % source, file=sys.stderr)
        return 1
    destination = os.path.join(output_dir(), IMAGE_NAME)
    shutil.copyfile(source, destination)
    with open(destination, "rb") as handle:
        data = handle.read()
    if not data.startswith(PNG_MAGIC):
        print("error: %s is not a PNG file" % destination, file=sys.stderr)
        return 1
    if len(data) != EXPECTED_SIZE:
        print("error: %s is %d bytes, expected %d"
              % (destination, len(data), EXPECTED_SIZE), file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("error: sha256 mismatch for %s" % destination, file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (destination, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
