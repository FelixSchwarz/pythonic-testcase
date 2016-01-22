# -*- coding: UTF-8 -*-
#
# The MIT License
# 
# Copyright (c) 2016 Felix Schwarz <felix.schwarz@oss.schwarz.eu>
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


from pythonic_testcase import assert_raises, expect_failure, PythonicTestCase, _ExpectedFailure


class ExpectedFailureTest(PythonicTestCase):
    @expect_failure
    def test_failing_tests_marked_as_expected_failure_are_not_treated_as_errors(self):
        raise AssertionError('not yet fixed')

    def test_passing_tests_marked_as_expected_failure_are_treated_as_errors(self):
        @expect_failure
        def passing():
            pass

        with assert_raises(AssertionError, message='should treat passing tests as error'):
            passing()

    def test_tests_with_errors_marked_as_expected_failure_are_treated_as_errors(self):
        # This is actually a really important part of the "expected failure"
        # concept: The test code should not bit-rot due to API changes but
        # always exercise the exact problem.
        @expect_failure
        def error_test():
            raise ValueError('foobar')

        try:
            with assert_raises(ValueError, message='should treat errors (anything besides AssertionError) as error'):
                error_test()
        except _ExpectedFailure:
            # need to handle this exception explicitly as test runners (e.g.
            # nosetests on Python 2.7) can't tell which part of the code
            # (test code or the PythonicTestcase decorator) threw the exception.
            # This ensures our decorator really just catches AssertionError.
            self.fail('ValueError should cause errors')


if __name__ == '__main__':
    import unittest
    unittest.main()
