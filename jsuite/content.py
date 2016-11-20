import logging

logger = logging.getLogger('jsuite')

def _text_content(node):
  return " ".join([x.strip() for x in node.itertext() if x.strip() is not ""])

def body_text(etree):
  """ Extracts text content from the body element of a JATS XML ElementTree 
  instance"""
  BODY_XPATH = '/article/body'
  query_set = etree.xpath(BODY_XPATH)

  if len(query_set) is 0:
    logger.warn('No body element found in article.')
    return None
  if len(query_set) is 1:
    return _text_content(query_set[0])
