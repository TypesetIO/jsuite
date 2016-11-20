from .context import jsuite, fixture

import unittest

class ContentSuite(unittest.TestCase):
  def test_body_text(self):
    with fixture('content/full-body') as f:
      doc = jsuite.from_file(f)
      content = jsuite.content.body_text(doc)
      control = "word word word Some text here to talk about things. Let's add some citations now. Linguistic aphorism 1 2 2 2 4 4 4 4"
      assert(content == control)