from typing import Any, Callable, List, Union
import traceback
from datetime import datetime

class TestHarness:
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        
    def run_test(self, 
                 func: Callable, 
                 input_args: List[Any], 
                 expected_output: Any,
                 test_name: str = None) -> bool:
        """
        Run a single test case for the given function.
        
        Args:
            func: The function to test
            input_args: List of arguments to pass to the function
            expected_output: Expected return value from the function
            test_name: Optional name for the test case
            
        Returns:
            bool: True if test passed, False if failed
        """
        self.total_tests += 1
        test_id = test_name or f"Test #{self.total_tests}"
        
        try:
            actual_output = func(*input_args)
            
            if actual_output == expected_output:
                self.passed_tests += 1
                print(f"✓ {test_id} PASSED")
                print(f"  Input: {input_args}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual: {actual_output}\n")
                return True
            else:
                self.failed_tests += 1
                print(f"✗ {test_id} FAILED")
                print(f"  Input: {input_args}")
                print(f"  Expected: {expected_output}")
                print(f"  Actual: {actual_output}\n")
                return False
                
        except Exception as e:
            self.failed_tests += 1
            print(f"✗ {test_id} FAILED - Exception raised")
            print(f"  Input: {input_args}")
            print(f"  Expected: {expected_output}")
            print(f"  Error: {str(e)}")
            print(f"  Traceback: {traceback.format_exc()}\n")
            return False
            
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
        print(f"Starting test suite at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Testing function: {func.__name__}\n")
        
        for test_case in test_cases:
            if len(test_case) == 3:
                input_args, expected_output, test_name = test_case
            else:
                input_args, expected_output = test_case
                test_name = None
            self.run_test(func, input_args, expected_output, test_name)
            
        print("\nTest Suite Summary:")
        print(f"Total tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        print(f"Success rate: {(self.passed_tests/self.total_tests)*100:.2f}%")