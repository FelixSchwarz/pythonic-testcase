# -*- coding: UTF-8 -*-
#
# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Felix Schwarz <felix.schwarz@oss.schwarz.eu>

from __future__ import absolute_import, unicode_literals, print_function

import os
import shutil
import tempfile
from unittest import TestCase

from pythonic_testcase import *
from .util import exception_message


class AssertPathExistsTest(TestCase):
    def setUp(self):
        super(AssertPathExistsTest, self).setUp()
        self.tempdir = tempfile.mkdtemp()
        self.path_foo = os.path.join(self.tempdir, 'foo')

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        super(AssertPathExistsTest, self).tearDown()

    def test_passes_if_path_exists(self):
        assert_path_exists(self.tempdir)
        os.mkdir(self.path_foo)
        assert_path_exists(self.path_foo)

    def assert_fail(self, path, message=None):
        with assert_raises(AssertionError, message=message) as exc_context:
            assert_path_exists(path, message=message)
        return exc_context.caught_exception

    def test_fails_if_path_does_not_exist(self):
        self.assert_fail(self.path_foo, message='path "%s" does not exist yet' % self.path_foo)
        os.mkdir(self.path_foo)
        assert_path_exists(self.path_foo)

    def test_fails_with_sensible_default_error_message(self):
        e = self.assert_fail(self.path_foo)
        expected_msg = "path '%s' does not exist" % self.path_foo
        assert_equals(expected_msg, exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail(self.path_foo, message='Foo')
        expected_msg = "path '%s' does not exist: Foo" % self.path_foo
        assert_equals(expected_msg, exception_message(e))


class AssertPathNotExistsTest(TestCase):
    def setUp(self):
        super(AssertPathNotExistsTest, self).setUp()
        self.tempdir = tempfile.mkdtemp()
        self.path_foo = os.path.join(self.tempdir, 'foo')

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        super(AssertPathNotExistsTest, self).tearDown()

    def test_passes_if_path_does_not_exist(self):
        assert_false(os.path.exists(self.path_foo))
        assert_path_not_exists(self.path_foo)

    def assert_fail(self, path, message=None):
        with assert_raises(AssertionError, message=message) as exc_context:
            assert_path_not_exists(path, message=message)
        return exc_context.caught_exception

    def test_fails_if_path_exists(self):
        assert_true(os.path.exists(self.tempdir))
        self.assert_fail(self.tempdir, message='path "%s" should not be present' % self.path_foo)

    def test_fails_with_sensible_default_error_message(self):
        e = self.assert_fail(self.tempdir)
        expected_msg = "path '%s' exists" % self.tempdir
        assert_equals(expected_msg, exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail(self.tempdir, message='Foo')
        expected_msg = "path '%s' exists: Foo" % self.tempdir
        assert_equals(expected_msg, exception_message(e))
