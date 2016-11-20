import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from contextlib import contextmanager

import jsuite

@contextmanager
def fixture(fixture_path):
  dirname = os.path.dirname(__file__)
  f = open(os.path.join(dirname, 'fixtures', fixture_path + '.xml'))
  try:
    yield f
  finally:
    f.close()

