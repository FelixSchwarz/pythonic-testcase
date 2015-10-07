# -*- coding: UTF-8 -*-
#
# The MIT License
# 
# Copyright (c) 2011, 2015 Felix Schwarz <felix.schwarz@oss.schwarz.eu>
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

from unittest import TestCase

from pythonic_testcase import assert_equals, assert_raises
from tests.util import exception_message


class AssertEqualsTest(TestCase):
    # assert_equals testing relies on assert_raises being correct, however it 
    # should not rely on any other helper method so assert_raises and 
    # assert_equals can provide the foundation for all other test methods
    
    def test_passes_if_values_are_equal(self):
        assert_equals(1, 1)
    
    def test_fails_if_values_are_not_equal(self):
        assert_raises(AssertionError, lambda: assert_equals(1, 2))
    
    def test_fails_with_sensible_default_error_message(self):
        # using a string here on purpose so we can check that repr is used in 
        # exception message
        e = assert_raises(AssertionError, lambda: assert_equals('foo', 'bar'))
        assert "'foo' != 'bar'" == exception_message(e), repr(exception_message(e))
    
    def test_can_specify_additional_custom_message(self):
        e = assert_raises(AssertionError, lambda: assert_equals(1, 2, message='foo'))
        assert "1 != 2: foo" == exception_message(e), repr(exception_message(e))

