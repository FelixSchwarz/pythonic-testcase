# -*- coding: UTF-8 -*-
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Felix Schwarz <felix.schwarz@oss.schwarz.eu>

from __future__ import absolute_import, unicode_literals, print_function

from unittest import TestCase

from pythonic_testcase import assert_equals, assert_is, assert_is_not, assert_raises
from .util import exception_message


class AssertIsTest(TestCase):
    def test_passes_if_value_is_identical(self):
        assert_is(False, False)
        assert_is(True, True)
        assert_is(None, None)

    def assert_fail(self, expr1, expr2, message=None):
        with assert_raises(AssertionError) as exc_context:
            assert_is(expr1, expr2, message=message)
        return exc_context.caught_exception

    def test_fails_if_value_is_not_identical(self):
        self.assert_fail(False, True, message='False is not True')
        self.assert_fail(False, 0, message='False is not 0')
        self.assert_fail(0, False, message='0 is not False')
        assert_equals(0, False, message='False should be "equal" to 0')

    def test_fails_with_sensible_default_error_message(self):
        # using a string here on purpose so we can check that repr is used in
        # exception message
        e = self.assert_fail('bar', True)
        assert_equals("'bar' is not True", exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail('bar', True, message='Foo')
        assert_equals("'bar' is not True: Foo", exception_message(e))


class AssertIsNotTest(TestCase):
    def test_passes_if_value_is_not_identical(self):
        assert_is_not(False, True)
        assert_is_not(0, False)
        assert_is_not('something', True)
        assert_is_not([], False)

    def assert_fail(self, expr1, expr2, message=None):
        with assert_raises(AssertionError) as exc_context:
            assert_is_not(expr1, expr2, message=message)
        return exc_context.caught_exception

    def test_fails_if_value_is_identical(self):
        self.assert_fail(True, True, message='True must not be True')

    def test_fails_with_sensible_default_error_message(self):
        e = self.assert_fail(True, True)
        assert_equals('True is identical to True', exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail(True, True, message='Foo')
        assert_equals('True is identical to True: Foo', exception_message(e))
