# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='sentry_now',
      version='0.1',
      description='Sentry on Openshift based on Python-2.7 Community Cartridge',
      author=u'José Moreira',
      author_email='zemanel@zemanel.eu',
      url='https://github.com/getsentry/sentry/',
      install_requires=[
          'sentry',
          'psycopg2',
      ],
     )
