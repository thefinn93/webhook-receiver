#!/usr/bin/env python
from distutils.core import setup
from webhook_receiver import __version__

setup(name='webhook-receiver',
      version=__version__,
      description='Recieves webhooks and executes commands.',
      author='Finn Herzfeld',
      author_email='finn@finn.io',
      url='https://github.com/thefinn93/webhook-receiver',
      packages=['webhook_receiver'],
      install_requires=["flask>=0.12.2"])
