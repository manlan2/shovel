#! /usr/bin/env python

try:
	from setuptools import setup
	extra = {
		'install_requires' : ['argparse']
	}
except ImportError:
	from distutils.core import setup
	extra = {
		'dependencies' : ['argparse']
	}

setup(name           = 'shovel',
	version          = '0.1.0',
	description      = 'Not Rake, but Shovel',
	long_description = 'Execute python functions as tasks',
	url              = 'http://github.com/seomoz/shovel',
	author           = 'Dan Lecocq',
	author_email     = 'dan@seomoz.org',
	keywords         = 'tasks, shovel, rake',
	packages         = ['shovel'],
	scripts          = ['bin/shovel'],
	classifiers      = [
		'Programming Language :: Python',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent'
	],
	**extra
)