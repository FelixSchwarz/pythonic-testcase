# -*- coding: UTF-8 -*-
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Felix Schwarz <felix.schwarz@oss.schwarz.eu>

from __future__ import absolute_import, unicode_literals, print_function

from datetime import datetime as DateTime, timedelta as TimeDelta
from unittest import TestCase

from pythonic_testcase import (assert_almost_now, assert_equals, assert_none,
    assert_raises, UTC)
from .util import exception_message


class AssertAlmostNowTest(TestCase):
    def test_passes_if_date_is_almost_now(self):
        now = DateTime.now()
        assert_almost_now(now)

        now = DateTime.now().replace(microsecond=0)
        assert_almost_now(now)

        now = DateTime.now() - TimeDelta(seconds=0.5)
        assert_almost_now(now)

    def test_fails_if_date_is_older_than_max_delta(self):
        a_few_seconds_ago = DateTime.now() - TimeDelta(seconds=30)
        self.assert_fail(a_few_seconds_ago)

        one_minute = TimeDelta(minutes=1)
        assert_almost_now(a_few_seconds_ago, max_delta=one_minute)
        yesterday = DateTime.now() - TimeDelta(days=1)
        self.assert_fail(yesterday, max_delta=one_minute)

    def test_can_use_plain_integer_for_max_delta(self):
        a_few_seconds_ago = DateTime.now() - TimeDelta(seconds=5)
        assert_almost_now(a_few_seconds_ago, max_delta=10)
        # check that this are really seconds (i.e. not "minutes"/"hours")
        one_minute_ago = DateTime.now() - TimeDelta(minutes=1)
        self.assert_fail(one_minute_ago, max_delta=10)

    def test_can_handle_timezone_aware_datetimes(self):
        datetime = DateTime.now(tz=UTC)
        assert_almost_now(datetime)

        a_few_seconds_ago = DateTime.now(tz=UTC) - TimeDelta(seconds=30)
        self.assert_fail(a_few_seconds_ago)

    def test_can_enforce_timezone_aware_checks(self):
        datetime = DateTime.now()
        assert_none(datetime.tzinfo)
        assert_almost_now(datetime)
        self.assert_fail(datetime, tz=UTC)

    def test_fails_with_sensible_default_error_message(self):
        a_few_seconds_ago = DateTime.now() - TimeDelta(seconds=30)
        e = self.assert_fail(a_few_seconds_ago)
        expected_msg = '%r is older than 1.0 seconds' % a_few_seconds_ago
        assert_equals(expected_msg, exception_message(e))

    def test_can_specify_additional_custom_message(self):
        a_few_seconds_ago = DateTime.now() - TimeDelta(seconds=30)
        e = self.assert_fail(a_few_seconds_ago, message='Foo')
        expected_msg = '%r is older than 1.0 seconds: Foo' % a_few_seconds_ago
        assert_equals(expected_msg, exception_message(e))

    # --- internal helpers ----------------------------------------------------
    def assert_fail(self, date, **kwargs):
        with assert_raises(AssertionError) as exc_context:
            assert_almost_now(date, **kwargs)
        return exc_context.caught_exception
