import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.0'
PACKAGE_NAME = 'xml2pdf'
AUTHOR = 'Rickard Lundstedt'
AUTHOR_EMAIL = 'rickard.lundstedt@gmail.com'
URL = 'https://github.com/lundst1/xml2pdf'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'A simple script for converting XML to PDF-documents, using XSLT.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'lxml',
      'pdfkit',
      'argparse'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
