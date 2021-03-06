#!/usr/bin/env python
'''
The setup script for saltapi
'''
from distutils.core import setup

# pylint: disable-msg=W0122,E0602
exec(compile(open('saltapi/version.py').read(), 'saltapi/version.py', 'exec'))
VERSION = __version__
# pylint: enable-msg=W0122,E0602

NAME = 'salt-api'
DESC = ("Generic interface for providing external access APIs to Salt")

# Specify the test suite for < 2.7
try:
    import unittest2
except ImportError:
    pass

setup(
    name=NAME,
    version=VERSION,
    description=DESC,
    author='Thomas S Hatch',
    author_email='thatch@saltstack.com',
    url='http://saltstack.org',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Distributed Computing'],
    packages=['saltapi',
        'saltapi.netapi',
        'saltapi.netapi.rest_cherrypy',
        ],
    package_data={
        'saltapi.netapi.rest_cherrypy': ['tmpl/*']},
    data_files=[('share/man/man1',
        ['doc/man/salt-api.1']),
        ('share/man/man7',
        ['doc/man/salt-api.7'])],
    scripts=['scripts/salt-api'],
    test_suite='unittest2.collector' if 'unittest2' in locals() else None)
