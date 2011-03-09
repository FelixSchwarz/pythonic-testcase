# -*- coding: UTF-8 -*-
#
# The MIT License
# 
# Copyright (c) 2011 Felix Schwarz <felix.schwarz@oss.schwarz.eu>
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

from pythonic_testcase import assert_equals, assert_false, assert_raises, assert_true
from tests.assert_raises_test import exception_message


class AssertTrueTest(TestCase):
    
    def test_passes_if_value_is_true(self):
        assert_true(True)
    
    def assert_fail(self, value, message=None):
        return assert_raises(AssertionError, lambda: assert_true(value, message=message))
        
    def test_fails_if_value_is_not_true(self):
        self.assert_fail(False)
        self.assert_fail('')
        self.assert_fail([])
        self.assert_fail(dict())
    
    def test_fails_with_sensible_default_error_message(self):
        # using a string here on purpose so we can check that repr is used in 
        # exception message
        e = self.assert_fail('bar')
        assert_equals("True != 'bar'", exception_message(e))
    
    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail('bar', message='Foo')
        assert_equals("True != 'bar': Foo", exception_message(e))


class AssertFalseTest(TestCase):
    
    def test_passes_if_value_is_false(self):
        assert_false(False)
    
    def assert_fail(self, value, message=None):
        return assert_raises(AssertionError, lambda: assert_false(value, message=message))
        
    def test_fails_if_value_is_not_false(self):
        self.assert_fail(True)
        self.assert_fail('')
        self.assert_fail([])
        self.assert_fail(dict())
    
    def test_fails_with_sensible_default_error_message(self):
        # using a string here on purpose so we can check that repr is used in 
        # exception message
        e = self.assert_fail('bar')
        assert_equals("False != 'bar'", exception_message(e))
    
    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail('bar', message='Foo')
        assert_equals("False != 'bar': Foo", exception_message(e))

