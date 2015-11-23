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

from pythonic_testcase import assert_raises
from tests.util import exception_message


class AssertRaisesTest(TestCase):
    # assert_raises is the basis of all testing. Therefore this test case must
    # not use any other helper method.
    
    def _good_callable(self):
        return lambda: None
    
    def test_fails_if_no_exception_was_raised(self):
        try:
            assert_raises(Exception, self._good_callable())
        except AssertionError:
            pass
        else:
            self.fail('No assertion raised')
    
    def _fail_with(self, exception):
        def failing_callable():
            raise exception
        return failing_callable
    
    def test_passes_if_callable_raised_exception(self):
        assert_raises(ValueError, self._fail_with(ValueError()))
        # also test for Python 2.6 specific "behavior"/bug where
        # Python 2.6 sometimes only passes a string (instead of
        # the exception instance) to the context manager
        # https://bugs.python.org/issue7853
        def raises_valueerror():
            from datetime import date
            # not sure how to reproduce the issue generically but
            # this date call triggers it at least.
            date(2000, 12, 50)
        assert_raises(ValueError, raises_valueerror)
    
    def test_returns_caught_exception_instance(self):
        expected_exception = ValueError('foobar')
        e = assert_raises(ValueError, self._fail_with(expected_exception))
        assert expected_exception == e
        assert id(expected_exception) == id(e)
    
    def test_callable_can_also_raise_assertion_error(self):
        expected_exception = AssertionError('foobar')
        e = assert_raises(AssertionError, self._fail_with(expected_exception))
        assert expected_exception == e
        assert id(expected_exception) == id(e)
    
    def test_passes_unexpected_exceptions(self):
        try:
            assert_raises(ValueError, self._fail_with(AssertionError()))
        except AssertionError:
            pass
        else:
            self.fail('Did not raise ValueError')
    
    def test_fails_with_sensible_default_error_message(self):
        try:
            assert_raises(ValueError, self._good_callable())
        except AssertionError as e:
            assert 'ValueError not raised!' == exception_message(e), repr(exception_message(e))
        else:
            self.fail('AssertionError not raised!')
    
    def test_can_specify_additional_custom_message(self):
        try:
            assert_raises(ValueError, self._good_callable(), message='Foo')
        except AssertionError as e:
            assert 'ValueError not raised! Foo' == exception_message(e), repr(exception_message(e))
        else:
            self.fail('AssertionError not raised!')

    def test_can_return_contextmanager(self):
        with assert_raises(ValueError):
            raise ValueError()

        try:
            with assert_raises(ValueError):
                raise AssertionError()
        except AssertionError:
            pass
        else:
            self.fail('Did not raise ValueError')

        try:
            with assert_raises(ValueError):
                pass
        except AssertionError:
            pass
        else:
            self.fail('No assertion raised')

