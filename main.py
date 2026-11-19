#!/usr/bin/env python3
"""Copy the bundled front-page image to the make.fun output directory.

Standard library only, no network. Running it twice writes byte-identical
output because it copies the same bundled file every time.
"""
import hashlib
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)
    if os.path.getsize(destination) != os.path.getsize(source):
        raise RuntimeError(
            "copied entry.png size %d does not match bundled source size %d"
            % (os.path.getsize(destination), os.path.getsize(source))
        )
    digest = hashlib.sha256(open(destination, "rb").read()).hexdigest()
    print("wrote %s sha256=%s" % (destination, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
