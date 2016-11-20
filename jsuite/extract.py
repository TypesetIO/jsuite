import logging

logger = logging.getLogger('jsuite')

def extract_title(etree):
  """ Extracts article title from a JATS XML ElementTree instance"""
  TITLE_XPATH = '/article/front/article-meta/title-group/article-title'
  query_set = etree.xpath(TITLE_XPATH)

  if len(query_set) is 0:
    return None
  elif len(query_set) is 1:
    return query_set[0].text
  else:
    logger.warn('Multiple article-title elements found')