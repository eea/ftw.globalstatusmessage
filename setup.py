from setuptools import setup, find_packages
import os


tests_require = [
      'collective.testcaselayer',]

version = '1.0'

setup(name='ftw.globalstatusmessage',
      version=version,
      description="ermoeglicht es Ankuendigungen auf jeder Seite anzuzeigen",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='4teamwork GmbH',
      author_email='info@4teamwork.ch',
      url='http://psc.4teamwork.ch/4teamwork/ftw/ftw-globalstatusmessage',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.autoinclude'
          # -*- Extra requirements: -*-
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )