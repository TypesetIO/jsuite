# coding=utf-8
from .context import jsuite, fixture

import unittest

class ExtractSuite(unittest.TestCase):
  def test_article_title(self):
    with fixture('extract/single-title') as f:
      doc = jsuite.from_file(f)
      title = jsuite.extract.extract_title(doc)
      assert(title == 'Sample article title')

  def test_article_title_unicode(self):
    with fixture('extract/title-with-unicodes') as f:
        doc = jsuite.from_file(f)
        title = jsuite.extract.extract_title(doc)
        assert(title == u'Sample article title † ecolé Straßße')