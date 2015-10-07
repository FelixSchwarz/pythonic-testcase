# -*- coding: UTF-8 -*-
#
# The MIT License
#
# Copyright (c) 2015 Felix Schwarz <felix.schwarz@oss.schwarz.eu>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# I believe the license above is permissible enough so you can actually
# use/relicense the code in any other project without license proliferation.
# I'm happy to relicense this code if necessary for inclusion in other free
# software projects.

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

