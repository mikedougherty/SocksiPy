#!/usr/bin/env python
import distutils.core

kw = {
    'name': "SocksiPy-digsby",
    'version': "1.0.1",
    'description': "A Python SOCKS and HTTP proxy module",
    'author': "Dan Haim",
    'author_email': "negativeiq@users.sourceforge.net",
    'url': "http://socksipy.sourceforge.net/",
    'license': "BSD",
    'py_modules': ['socks'],
}

distutils.core.setup(**kw)
