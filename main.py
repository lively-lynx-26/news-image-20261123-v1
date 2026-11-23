"""Entry program for news-image-20261123.

The front page for Monday 23 November 2026 was rendered in the build
session (code-drawn text, scenes and map, PIL/DejaVu) and is stored
beside this file as entry.png. This program only copies that image to
the grader's output directory, then checks the copy is a well-formed
PNG of the expected size and hash. The copy is byte-exact: no pixels
are re-rendered here, so the shipped image is identical to the one
reviewed in the build session.

Usage: python3 main.py
Output: $MAKEFUN_OUTPUT_DIR/entry.png (falls back to <repo>/output
when the variable is unset, empty or unwritable).
"""

import hashlib
import os
import shutil
import sys

IMAGE_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SHA256 = "b5bf967033272e4c60ac33e421a238a09a6547fad62ab18d34676e921d189d8c"


def repo_root():
    return os.path.dirname(os.path.abspath(__file__))


def output_dir():
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if wanted:
        try:
            os.makedirs(wanted, exist_ok=True)
            probe = os.path.join(wanted, ".write-test")
            with open(probe, "wb") as handle:
                handle.write(b"ok")
            os.remove(probe)
            return wanted
        except OSError:
            pass
    fallback = os.path.join(repo_root(), "output")
    os.makedirs(fallback, exist_ok=True)
    return fallback


def main():
    src = os.path.join(repo_root(), IMAGE_NAME)
    if not os.path.isfile(src):
        print("missing source image: %s" % src, file=sys.stderr)
        return 1
    out_dir = output_dir()
    dst = os.path.join(out_dir, IMAGE_NAME)
    shutil.copyfile(src, dst)
    with open(dst, "rb") as handle:
        data = handle.read()
    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("entry.png sha256 mismatch: %s" % digest, file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (dst, len(data), digest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
