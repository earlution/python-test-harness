from typing import Any, Callable, List, Union, Optional
import traceback
from datetime import datetime
import sys
from enum import Enum

class TestResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    ERROR = "ERROR"

class TestHarness:
    """
    A test harness for educational purposes, designed to help students learn testing.
    
    Features:
    - Clear test output formatting
    - Detailed error messages
    - Support for test suites
    - Educational hints for failures
    """
    
    def __init__(self, show_hints: bool = True, use_colours: bool = True):
        """
        Initialize the test harness.
        
        Args:
            show_hints: Whether to show helpful hints for failed tests
            use_colours: Whether to use coloured output in the terminal
        """
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.error_tests = 0
        self.show_hints = show_hints
        self.use_colours = use_colours and sys.stdout.isatty()  # Only use colours if in terminal
        
    def _colorize(self, text: str, color_code: str) -> str:
        """Add colour to terminal output if enabled."""
        if self.use_colours:
            return f"\033[{color_code}m{text}\033[0m"
        return text
        
    def _validate_test_case(self, test_case: tuple) -> bool:
        """
        Validate the format of a test case.
        
        Returns:
            bool: True if valid, raises ValueError if invalid
        """
        if not isinstance(test_case, tuple):
            raise ValueError("Test case must be a tuple")
        
        if len(test_case) not in [2, 3]:
            raise ValueError("Test case must have 2 or 3 elements: (inputs, expected_output, [name])")
            
        inputs, expected = test_case[0], test_case[1]
        if not isinstance(inputs, list):
            raise ValueError("Test case inputs must be a list")
            
        return True
        
    def _generate_hint(self, func: Callable, inputs: List[Any], expected: Any, actual: Any) -> str:
        """Generate a helpful hint for a failed test."""
        hints = []
        
        # Type mismatch hint
        if type(actual) != type(expected):
            hints.append(f"The function returned a {type(actual).__name__}, "
                        f"but we expected a {type(expected).__name__}")
            
        # Number comparison hint
        if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            if actual < expected:
                hints.append(f"The result ({actual}) is too small")
            else:
                hints.append(f"The result ({actual}) is too large")
                
        # String comparison hint
        if isinstance(expected, str) and isinstance(actual, str):
            if len(actual) != len(expected):
                hints.append(f"The string lengths don't match: "
                           f"expected {len(expected)}, got {len(actual)}")
                
        return "\n  Hint: " + "; ".join(hints) if hints else ""

    def run_test(self, 
                 func: Callable, 
                 input_args: List[Any], 
                 expected_output: Any,
                 test_name: Optional[str] = None) -> TestResult:
        """
        Run a single test case for the given function.
        
        Args:
            func: The function to test
            input_args: List of arguments to pass to the function
            expected_output: Expected return value from the function
            test_name: Optional name for the test case
            
        Returns:
            TestResult: The result of the test (PASS, FAIL, or ERROR)
        """
        self.total_tests += 1
        test_id = test_name or f"Test #{self.total_tests}"
        
        try:
            actual_output = func(*input_args)
            
            if actual_output == expected_output:
                self.passed_tests += 1
                print(self._colorize(f"✓ {test_id} PASSED", "32"))  # Green
                print(f"  Input: {input_args}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual: {actual_output}\n")
                return TestResult.PASS
            else:
                self.failed_tests += 1
                print(self._colorize(f"✗ {test_id} FAILED", "31"))  # Red
                print(f"  Input: {input_args}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual: {actual_output}")
                if self.show_hints:
                    print(self._generate_hint(func, input_args, expected_output, actual_output))
                print()
                return TestResult.FAIL
                
        except Exception as e:
            self.error_tests += 1
            print(self._colorize(f"✗ {test_id} ERROR", "33"))  # Yellow
            print(f"  Input: {input_args}")
            print(f"  Expected: {expected_output}")
            print(f"  Error: {str(e)}")
            print(f"  Traceback: {traceback.format_exc()}\n")
            return TestResult.ERROR
            
    def run_test_suite(self, 
                       func: Callable, 
                       test_cases: List[tuple[List[Any], Any, Union[str, None]]]) -> None:
        """
        Run multiple test cases for the given function.
        
        Args:
            func: The function to test
            test_cases: List of tuples containing (input_args, expected_output, test_name)
                       where test_name is optional
        """
        if not test_cases:
            print(self._colorize("Warning: No test cases provided!", "33"))
            return
            
        print(f"Starting test suite at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Testing function: {func.__name__}\n")
        
        for test_case in test_cases:
            try:
                self._validate_test_case(test_case)
                if len(test_case) == 3:
                    input_args, expected_output, test_name = test_case
                else:
                    input_args, expected_output = test_case
                    test_name = None
                self.run_test(func, input_args, expected_output, test_name)
            except ValueError as e:
                print(self._colorize(f"Invalid test case format: {e}", "31"))
                continue
            
        # Print summary with colour
        print("\nTest Suite Summary:")
        print(f"Total tests: {self.total_tests}")
        if self.passed_tests:
            print(self._colorize(f"Passed: {self.passed_tests}", "32"))
        if self.failed_tests:
            print(self._colorize(f"Failed: {self.failed_tests}", "31"))
        if self.error_tests:
            print(self._colorize(f"Errors: {self.error_tests}", "33"))
        
        if self.total_tests > 0:
            success_rate = (self.passed_tests/self.total_tests)*100
            colour = "32" if success_rate == 100 else "33" if success_rate >= 50 else "31"
            print(self._colorize(f"Success rate: {success_rate:.2f}%", colour))


# Example usage
if __name__ == "__main__":
    def add_numbers(a: int, b: int) -> int:
        return a + b
        
    harness = TestHarness(show_hints=True, use_colours=True)
    
    test_cases = [
        ([1, 2], 3, "Simple addition"),
        ([0, 0], 0, "Zero addition"),
        ([2, 2], 5, "Failing test"),  # This will fail
        ([-1, 1], 0, "Negative numbers")
    ]
    
    harness.run_test_suite(add_numbers, test_cases)