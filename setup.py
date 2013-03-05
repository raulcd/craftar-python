#!/usr/bin/python
#
#  (C) Catchoom Technologies S.L.
#  Licensed under the MIT license.
#  https://github.com/catchoom/catchoom-python/blob/master/LICENSE
#  All warranties and liabilities are disclaimed.

"""Catchoom Python Library
==========================

The Catchoom Python Library allows you to integrate
`Catchoom Image Recognition`_ in your applications and services.

This client library provides access to our APIs:

-  `Catchoom Recognition API` allows visual recognition against one of
   your collections of reference images specified using the
   collection token.
-  `Catchoom Management API` allows upload and management of
   collections of reference images. All requests must be
   authenticated using your management api key.

The library also provides tools for performing batch operations:

-  `catchoom\_search`, for image recognition.
-  `catchoom\_upload`, for batch upload of images.

To use our service you need a `Catchoom Recognition Service`_ account.

You can get our `code`_, check the `README`_ and file bugs in the
`issue tracker`_.

.. _Catchoom Recognition Service: https://crs.catchoom.com
.. _Catchoom Image Recognition: http://catchoom.com
.. _code: https://github.com/Catchoom/catchoom-python
.. _README: https://github.com/Catchoom/catchoom-python/blob/master/README.md
.. _issue tracker: https://github.com/Catchoom/catchoom-python/issues
"""
from distutils.core import setup


setup(name='catchoom',
      version='1.0.3',
      description="Catchoom Python Library",
      long_description=__doc__,
      license="MIT",
      keywords="catchoom image recognition",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: Information Technology",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet",
          "Topic :: Multimedia :: Graphics",
          "Topic :: Scientific/Engineering :: Image Recognition",
          "Topic :: Software Development",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Utilities",
      ],
      platforms=["any"],
      author='Catchoom',
      author_email='support@catchoom.com',
      maintainer='Catchoom',
      maintainer_email='support@catchoom.com',
      url='http://catchoom.com',
      bugtrack_url="https://github.com/Catchoom/catchoom-python/issues",
      packages=["catchoom"],
      scripts=['bin/catchoom_search', 'bin/catchoom_upload'],
      install_requires=["requests==1.1.0", "Pillow==1.7.8"]
      )
