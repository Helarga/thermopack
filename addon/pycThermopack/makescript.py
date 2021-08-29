"""Simple script to copy the desired libthermopack.so file."""
#!/usr/bin/env python
from __future__ import print_function

import argparse
import os
import shutil
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('mode', type=str, help='optim or debug')

args = parser.parse_args()
mode = args.mode

# Glob to handle different OS suffixes
libthermo = list(
    Path('../../bin').glob(f'libthermopack_{mode}_gfortran*.*'))[0]

if not os.path.exists(libthermo):
    print(f'{libthermo}does not exist. Have you compiled thermopack?')
    sys.exit(1)

shutil.copy2(libthermo, './pyctp/libthermopack.so')
