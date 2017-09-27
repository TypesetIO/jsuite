import logging

logger = logging.getLogger('jsuite')

def of_type_in_body(etree, type):
  xpath_query = './body//%s' %(type)
  return len(etree.findall(xpath_query))

def of_type(etree, type):
  xpath_query = './/%s' %(type)
  return len(etree.findall(xpath_query))

def of_xpath(etree, xpath_query):
  return len(etree.findall(xpath_query))
