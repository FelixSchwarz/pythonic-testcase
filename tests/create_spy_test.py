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

from pythonic_testcase import create_spy, assert_raises, assert_equals

class CreateSpyTest(TestCase):
    
    def test_spy_knows_if_it_was_called(self):
        spy = create_spy()
        spy.assert_was_not_called()
        assert_raises(AssertionError, spy.assert_was_called)
        spy()
        assert_raises(AssertionError, spy.assert_was_not_called)
        spy.assert_was_called()
    
    def test_should_know_keyword_call_parameters(self):
        spy = create_spy()
        assert_raises(AssertionError, lambda: spy.assert_was_called_with())
        spy()
        spy.assert_was_called_with()
        spy(foo='bar')
        spy.assert_was_called_with(foo='bar')
        assert_raises(AssertionError, lambda: spy.assert_was_called_with())
        assert_raises(AssertionError, lambda: spy.assert_was_called_with('bar'))
        assert_raises(AssertionError, lambda: spy.assert_was_called_with(foo='bar', fnord='baz'))

    def test_should_know_positional_call_parameters(self):
        spy = create_spy()
        spy(23)
        spy.assert_was_called_with(23)
        assert_raises(AssertionError, lambda: spy.assert_was_called_with())
        assert_raises(AssertionError, lambda: spy.assert_was_called_with(23, 24))
        assert_raises(AssertionError, lambda: spy.assert_was_called_with(foo=23))
        assert_raises(AssertionError, lambda: spy.assert_was_called_with(23, fnord='baz'))
    
    def test_should_allow_mocking_return_value(self):
        spy = create_spy().and_return(23)
        assert_equals(23, spy())

    def test_should_reset(self):
        spy = create_spy().and_return(23)
        spy()
        spy.reset()
        spy.assert_was_not_called()
        assert_equals(None, spy())
