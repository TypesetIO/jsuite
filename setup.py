from distutils.core import setup

setup(
  name = 'jsuite',
  packages = ['jsuite'], # this must be the same as the name above
  version = '0.1.3',

  scripts=['bin/jsuite'],
  install_requires = [
    'lxml==3.6.4',
    'clint==0.5.1'
  ],

  description = 'Parsing and manipulation tools for JATS XML files.',
  author = 'Dipanjan Mukherjee',
  author_email = 'dipanjan.mu@gmail.com',
  url = 'https://github.com/schatten/jsuite', # use the URL to the github repo
  download_url = 'https://github.com/schatten/jsuite/tarball/0.1', # I'll explain this in a second
  keywords = ['xml', 'parsing', 'JATS', 'tools'], # arbitrary keywords
  classifiers = [],
)