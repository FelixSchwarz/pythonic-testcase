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

from pythonic_testcase import assert_equals, assert_length, assert_raises
from tests.util import exception_message


class AssertLengthTest(TestCase):

    def test_passes_if_length_matches_actual(self):
        assert_length(0, [])
        assert_length(1, ['foo'])

    def assert_fail(self, expected, actual, message=None):
        return assert_raises(AssertionError, lambda: assert_length(expected, actual, message=message))

    def test_fails_if_length_does_not_match_equal(self):
        self.assert_fail(2, ['foo'])

    def test_fails_with_sensible_default_error_message(self):
        e = self.assert_fail(2, ['foo'])
        assert "2 != 1" == exception_message(e), repr(exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail(2, ['foo'], message='Bar')
        assert "2 != 1: Bar" == exception_message(e), repr(exception_message(e))


