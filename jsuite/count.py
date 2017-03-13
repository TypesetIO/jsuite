import logging

logger = logging.getLogger('jsuite')

def of_type(etree, type):
  xpath_query = './body//%s' %(type)
  return len(etree.findall(xpath_query))