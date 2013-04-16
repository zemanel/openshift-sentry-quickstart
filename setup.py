# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='sentry_now',
      version='0.1',
      description='Sentry instance based on Python-2.7 Community Cartridge',
      author=u'José Moreira',
      author_email='zemanel@zemanel.eu',
      url='https://github.com/getsentry/sentry/',
      install_requires=[
          'sentry==5.4.5',
          'psycopg2',
          # testing
          'selenium==2.32.0',
          'flake8==2.0'
      ],
      )
