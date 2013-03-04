#!/usr/bin/python
#
#  (C) Catchoom Technologies S.L.
#  Licensed under the MIT license.
#  https://github.com/catchoom/catchoom-python/blob/master/LICENSE
#  All warranties and liabilities are disclaimed.

from distutils.core import setup


setup(name='catchoom',
      version='1.0.1',
      description="Catchoom Python Library",
      long_description="Catchoom Python Library",
      license="MIT",
      platforms=["any"],
      author='Catchoom',
      author_email='support@catchoom.com',
      maintainer='Catchoom',
      maintainer_email='support@catchoom.com',
      url='https://github.com/catchoom/catchoom-python',
      packages=["catchoom"],
      scripts=['bin/catchoom_search', 'bin/catchoom_upload'],
      install_requires=["requests==1.1.0", "Pillow==1.7.8"]
      )
