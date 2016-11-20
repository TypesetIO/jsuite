from lxml import etree

def from_string(str):
  return etree.fromstring(str)

def from_file(file_like):
  return etree.parse(file_like)

# Define public API
from . import extract, content