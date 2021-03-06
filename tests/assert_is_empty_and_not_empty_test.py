# -*- coding: UTF-8 -*-
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2011, 2015 Felix Schwarz <felix.schwarz@oss.schwarz.eu>

from __future__ import absolute_import, unicode_literals, print_function

from unittest import TestCase

from pythonic_testcase import assert_equals, assert_is_empty, assert_is_not_empty, assert_raises
from .util import exception_message


class AssertIsEmptyTest(TestCase):
    def test_passes_if_value_is_empty(self):
        assert_is_empty('')
        assert_is_empty(())
        assert_is_empty([])
        assert_is_empty({})

    def assert_fail(self, value, message=None):
        return assert_raises(AssertionError, lambda: assert_is_empty(value, message=message))

    def test_fails_if_value_is_not_empty(self):
        self.assert_fail('foo')
        self.assert_fail([1])

    def test_can_consume_generator_if_necessary(self):
        def generator():
            for i in (1, 2, 3):
                yield i
        self.assert_fail(generator())

    def test_fails_with_sensible_default_error_message(self):
        # using a string here on purpose so we can check that repr is used in
        # exception message
        e = self.assert_fail('bar')
        assert_equals("%r is not empty (3 items)" % 'bar', exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail('bar', message='Foo')
        assert_equals("%r is not empty (3 items): Foo" % 'bar', exception_message(e))


class AssertIsNotEmptyTest(TestCase):
    def test_passes_if_value_is_not_empty(self):
        assert_is_not_empty((1,))
        assert_is_not_empty([1])
        assert_is_not_empty('foo')

    def assert_fail(self, value, message=None):
        return assert_raises(AssertionError, lambda: assert_is_not_empty(value, message=message))

    def test_fails_if_value_is_empty(self):
        self.assert_fail('')
        self.assert_fail(())
        self.assert_fail([])
        self.assert_fail({})

    def test_can_consume_generator_if_necessary(self):
        def generator():
            for i in (1, 2, 3):
                yield i
        assert_is_not_empty(generator())

    def test_fails_with_sensible_default_error_message(self):
        # using a string here on purpose so we can check that repr is used in
        # exception message
        e = self.assert_fail('')
        assert_equals("%r is empty" % '', exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail('', message='Foo')
        assert_equals("%r is empty: Foo" % '', exception_message(e))

