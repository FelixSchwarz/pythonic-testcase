# -*- coding: UTF-8 -*-
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2011, 2015 Felix Schwarz <felix.schwarz@oss.schwarz.eu>

from __future__ import absolute_import, unicode_literals, print_function

from datetime import datetime, timedelta
from unittest import TestCase

from pythonic_testcase import assert_equals, assert_almost_equals, assert_raises
from .util import exception_message


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

