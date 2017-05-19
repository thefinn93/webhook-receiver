#!/usr/bin/env python
from distutils.core import setup

setup(name='webhook-receiver',
      version="0.1.0",
      description='Recieves webhooks and executes commands.',
      author='Finn Herzfeld',
      author_email='finn@finn.io',
      url='https://github.com/thefinn93/webhook-receiver',
      packages=['webhook_receiver'],
      install_requires=["flask"])
