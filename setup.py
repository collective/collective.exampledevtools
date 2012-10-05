from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('docs/index.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.exampledevtools',
      version=version,
      description="This package is created for the Plone Conf 2012 talk, Essential Development Tools.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Kim Chee Leong, Goldmund, Wyldebeast & Wunderliebe',
      author_email='leong@gw20e.com',
      url='https://github.com/collective/collective.exampledevtools/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'five.grok',
      ],
      extras_require={
          'test': ['plone.app.testing'],
          'develop': [
              'Sphinx',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
