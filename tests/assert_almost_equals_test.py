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

from datetime import datetime, timedelta
from unittest import TestCase

from pythonic_testcase import assert_equals, assert_almost_equals, assert_raises
from tests.assert_raises_test import exception_message


class AssertAlmostEquals(TestCase):
    
    def test_passes_if_values_are_equal(self):
        assert_almost_equals(1, 1)
        assert_almost_equals('foo', 'foo')
    
    def test_fails_if_values_are_not_equal(self):
        self.assert_fail(2, ['foo'])
        self.assert_fail(2, 1)
    
    def test_passes_if_values_are_equal_within_max_delta(self):
        assert_almost_equals(1, 1, max_delta=1)
        assert_almost_equals(1, 2, max_delta=1)
        
        now = datetime.now()
        one_hour_ago = now - timedelta(hours=1)
        assert_almost_equals(now, one_hour_ago, max_delta=timedelta(hours=2))
    
    def test_fails_if_values_are_not_within_delta(self):
        self.assert_fail(1, 3, max_delta=1)
    
    def test_fails_with_sensible_default_error_message(self):
        e = self.assert_fail(2, 3)
        assert_equals('2 != 3', exception_message(e))
        e = self.assert_fail(2, 4, 1)
        assert_equals('2 != 4 +/- 1', exception_message(e))
    
    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail(1, 3, max_delta=1, message='Bar')
        assert_equals('1 != 3 +/- 1: Bar', exception_message(e))
    
    def assert_fail(self, expected, actual, max_delta=None, message=None):
        assertion = lambda: assert_almost_equals(expected, actual, max_delta=max_delta, message=message)
        return assert_raises(AssertionError, assertion)

