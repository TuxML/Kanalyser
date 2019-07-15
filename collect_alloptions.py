#!/usr/bin/env python3

# make ARCH=x86 scriptconfig SCRIPT=../collect_alloptions.py (within Linux source code, and after applying a patch)


import kconfiglib
import sys
import pandas as pd 
# Autor Mathieu Acher


def collect_alloptions(input):
    kconf = kconfiglib.Kconfig(input)
    data_fill = []

    # Add new entries
    for sym in set(kconf.defined_syms):
        data_fill.append((
        sym.name,
        kconfiglib.TYPE_TO_STR[sym.orig_type].upper()))

    return data_fill

all_opts = collect_alloptions(sys.argv[1])
# print(len(all_opts))
DEFAULT_CSV_OUTPUT = 'alloptions-x64.csv'
pd.DataFrame(all_opts, columns=['option', 'type']).to_csv('alloptions-x64.csv', index=False)
