# Copyright (c) 2024 Joshua Watt
#
# SPDX-License-Identifier: MIT

import subprocess
import sys


def test_help():
    subprocess.run(["spdx3-build-gen", "--help"], check=True)


def test_module():
    subprocess.run([sys.executable, "-m", "spdx3_build_gen", "--help"], check=True)
