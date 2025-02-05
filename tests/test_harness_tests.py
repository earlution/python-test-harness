import unittest
from src.test_harness import TestHarness
from io import StringIO
import sys

class TestTestHarness(unittest.TestCase):
    def setUp(self):
        self.harness = TestHarness()
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_successful_test(self):
        def dummy_func(x):
            return x + 1
        
        result = self.harness.run_test(dummy_func, [1], 2, "Test add one")
        self.assertTrue(result)
        self.assertEqual(self.harness.passed_tests, 1)
        self.assertEqual(self.harness.failed_tests, 0)

    def test_failed_test(self):
        def dummy_func(x):
            return x + 1
        
        result = self.harness.run_test(dummy_func, [1], 3, "Test add one")
        self.assertFalse(result)
        self.assertEqual(self.harness.passed_tests, 0)
        self.assertEqual(self.harness.failed_tests, 1)

    def test_exception_handling(self):
        def dummy_func(x):
            raise ValueError("Test error")
        
        result = self.harness.run_test(dummy_func, [1], None, "Test exception")
        self.assertFalse(result)
        self.assertEqual(self.harness.passed_tests, 0)
        self.assertEqual(self.harness.failed_tests, 1)

    def test_test_suite(self):
        def dummy_func(x):
            return x + 1
        
        test_cases = [
            ([1], 2, "Test case 1"),
            ([2], 3, "Test case 2"),
            ([3], 4, "Test case 3")
        ]
        
        self.harness.run_test_suite(dummy_func, test_cases)
        self.assertEqual(self.harness.total_tests, 3)
        self.assertEqual(self.harness.passed_tests, 3)
        self.assertEqual(self.harness.failed_tests, 0)

if __name__ == '__main__':
    unittest.main()