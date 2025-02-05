import unittest
from src.test_harness import TestHarness, TestResult
from io import StringIO
import sys

class TestTestHarness(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test method."""
        self.harness = TestHarness(show_hints=True, use_colours=False)  # Disable colours for testing
        self.captured_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_output

    def tearDown(self):
        """Clean up after each test method."""
        sys.stdout = self.original_stdout

    def test_successful_test(self):
        """Test that a successful test is handled correctly."""
        def dummy_func(x):
            return x + 1
        
        result = self.harness.run_test(dummy_func, [1], 2, "Test add one")
        self.assertEqual(result, TestResult.PASS)
        self.assertEqual(self.harness.passed_tests, 1)
        self.assertEqual(self.harness.failed_tests, 0)
        self.assertEqual(self.harness.error_tests, 0)

    def test_failed_test(self):
        """Test that a failed test is handled correctly."""
        def dummy_func(x):
            return x + 1
        
        result = self.harness.run_test(dummy_func, [1], 3, "Test add one")
        self.assertEqual(result, TestResult.FAIL)
        self.assertEqual(self.harness.passed_tests, 0)
        self.assertEqual(self.harness.failed_tests, 1)
        self.assertEqual(self.harness.error_tests, 0)
        
        # Check that hints are included in output
        output = self.captured_output.getvalue()
        self.assertIn("Hint:", output)

    def test_error_test(self):
        """Test that an error in the test is handled correctly."""
        def dummy_func(x):
            raise ValueError("Test error")
        
        result = self.harness.run_test(dummy_func, [1], None, "Test exception")
        self.assertEqual(result, TestResult.ERROR)
        self.assertEqual(self.harness.passed_tests, 0)
        self.assertEqual(self.harness.failed_tests, 0)
        self.assertEqual(self.harness.error_tests, 1)

    def test_test_suite(self):
        """Test that a test suite runs correctly."""
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
        self.assertEqual(self.harness.error_tests, 0)

    def test_empty_test_suite(self):
        """Test handling of empty test suite."""
        def dummy_func(x):
            return x
            
        self.harness.run_test_suite(dummy_func, [])
        output = self.captured_output.getvalue()
        self.assertIn("Warning: No test cases provided!", output)

    def test_invalid_test_case_format(self):
        """Test handling of invalid test case format."""
        def dummy_func(x):
            return x
            
        # Test with invalid tuple length
        test_cases = [
            ([1], 2, "name", "extra")  # Invalid: too many elements
        ]
        
        self.harness.run_test_suite(dummy_func, test_cases)
        output = self.captured_output.getvalue()
        self.assertIn("Invalid test case format", output)

    def test_hint_generation(self):
        """Test that appropriate hints are generated."""
        def dummy_func(x):
            return str(x)  # Returns string instead of int
            
        self.harness.run_test(dummy_func, [1], 1, "Type mismatch test")
        output = self.captured_output.getvalue()
        self.assertIn("function returned a str", output)
        self.assertIn("expected a int", output)

    def test_colour_disabled(self):
        """Test that colour output can be disabled."""
        harness = TestHarness(use_colours=False)
        output = harness._colorize("test", "32")
        self.assertEqual(output, "test")

    def test_different_types_hints(self):
        """Test hints for different types of mismatches."""
        def dummy_func(x):
            return x + 1
            
        # Test numeric comparison hint
        self.harness.run_test(dummy_func, [1], 3, "Numeric comparison")
        output = self.captured_output.getvalue()
        self.assertIn("too small", output)
        
        # Clear output for next test
        self.captured_output.truncate(0)
        self.captured_output.seek(0)
        
        # Test string length hint
        def string_func(x):
            return "ab"
            
        self.harness.run_test(string_func, ["x"], "abc", "String length")
        output = self.captured_output.getvalue()
        self.assertIn("string lengths don't match", output)

if __name__ == '__main__':
    unittest.main()