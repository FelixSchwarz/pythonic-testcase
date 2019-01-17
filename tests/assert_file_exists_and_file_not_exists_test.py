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


class AssertFileExistsTest(TestCase):
    def setUp(self):
        super(AssertFileExistsTest, self).setUp()
        self.tempdir = tempfile.mkdtemp()
        self.path_foo = os.path.join(self.tempdir, 'foo')

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        super(AssertFileExistsTest, self).tearDown()

    def test_passes_if_file_exists(self):
        _create_file(self.path_foo)
        assert_file_exists(self.path_foo)

    def test_fails_if_path_does_not_exist(self):
        self.assert_fail(self.path_foo, message='file "%s" does not exist yet' % self.path_foo)
        _create_file(self.path_foo)
        assert_file_exists(self.path_foo)

    def test_fails_if_path_is_directory(self):
        dir_path = os.path.join(self.tempdir, 'some-directory')
        os.mkdir(dir_path)
        assert_path_exists(dir_path)
        self.assert_fail(dir_path)

    def assert_fail(self, path, message=None):
        with assert_raises(AssertionError, message=message) as exc_context:
            assert_file_exists(path, message=message)
        return exc_context.caught_exception

    def test_fails_with_sensible_default_error_message(self):
        e = self.assert_fail(self.path_foo)
        expected_msg = "file '%s' does not exist" % self.path_foo
        assert_equals(expected_msg, exception_message(e))

        os.mkdir(self.path_foo)
        e = self.assert_fail(self.path_foo)
        expected_msg = "'%s' is a directory" % self.path_foo
        assert_equals(expected_msg, exception_message(e))

    def test_can_specify_additional_custom_message(self):
        e = self.assert_fail(self.path_foo, message='Foo')
        expected_msg = "file '%s' does not exist: Foo" % self.path_foo
        assert_equals(expected_msg, exception_message(e))



class AssertFileNotExistsTest(TestCase):
    def setUp(self):
        super(AssertFileNotExistsTest, self).setUp()
        self.tempdir = tempfile.mkdtemp()
        self.path_foo = os.path.join(self.tempdir, 'foo')

    def tearDown(self):
        shutil.rmtree(self.tempdir)
        super(AssertFileNotExistsTest, self).tearDown()

    def test_passes_if_file_does_not_exist(self):
        assert_file_not_exists(self.path_foo)

    def assert_fail(self, path, message=None):
        with assert_raises(AssertionError, message=message) as exc_context:
            assert_file_not_exists(path, message=message)
        return exc_context.caught_exception

    def test_fails_if_file_exists(self):
        assert_file_not_exists(self.path_foo)
        _create_file(self.path_foo)
        self.assert_fail(self.path_foo, message='file "%s" exists' % self.path_foo)

    def test_passes_if_path_is_directory(self):
        os.mkdir(self.path_foo)
        assert_path_exists(self.path_foo)
        assert_file_not_exists(self.path_foo)

    def test_fails_with_sensible_default_error_message(self):
        _create_file(self.path_foo)
        e = self.assert_fail(self.path_foo)
        expected_msg = "file '%s' exists" % self.path_foo
        assert_equals(expected_msg, exception_message(e))

    def test_can_specify_additional_custom_message(self):
        _create_file(self.path_foo)
        e = self.assert_fail(self.path_foo, message='Foo')
        expected_msg = "file '%s' exists: Foo" % self.path_foo
        assert_equals(expected_msg, exception_message(e))


def _create_file(path):
    with open(path, 'wb') as fp:
        fp.write(b'')
