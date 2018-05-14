"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import ts_code.nsfg as nsfg
import ts_code.thinkstats2 as thinkstats2

def read_FemResp(dct_file = 'ts_code/2002FemResp.dct',
              dat_file = 'ts_code/2002FemResp.dat.gz'):
  dct = thinkstats2.ReadStataDct(dct_file)
  df = dct.ReadFixedWidth(dat_file, compression='gzip')
  return df

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
