from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jsuite',
    version='0.5.0',

    description='Parsing and manipulation tools for JATS XML files.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/schatten/jsuite',

    # Author details
    author='Dipanjan Mukherjee',
    author_email='dipanjan.mu@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Markup :: XML',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='xml parsing JATS tools',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['jsuite'],

    install_requires=[
      'lxml==4.6.2',
      'clint==0.5.1'
    ],
    
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['nose'],
    }
)
