# -*- coding: UTF-8 -*-
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2015 Felix Schwarz <felix.schwarz@oss.schwarz.eu>

import sys


__all__ = ['basestring', 'exception_message', 'UPREFIX']

UPREFIX = 'u' if (sys.version_info < (3, 0)) else ''

try:
    basestring = basestring
except NameError:
    basestring = str

def exception_message(exception):
    if len(exception.args) == 0:
        return None
    return exception.args[0]

