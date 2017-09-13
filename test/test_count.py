# coding=utf-8
from .context import jsuite, fixture

import unittest

class CountSuite(unittest.TestCase):
  def test_count_figures_in_body(self):
    with fixture('count/4-figures') as f:
      doc = jsuite.from_file(f)
      count = jsuite.count.of_type_in_body(doc, 'fig')
      assert(count == 4)

  def test_count_figures(self):
    with fixture('count/4-figures') as f:
      doc = jsuite.from_file(f)
      count = jsuite.count.of_type(doc, 'fig')
      assert(count == 4)