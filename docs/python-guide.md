# Python Implementation Guide

This guide covers using the test harness in a standard Python environment.

## Getting Started

1. Ensure Python 3.8 or higher is installed
2. Copy `test_harness.py` to your working directory
3. Import and use the test harness in your code

## Basic Usage

```python
from test_harness import TestHarness

# Create a function to test
def add_numbers(a, b):
    return a + b

# Create test harness with default settings
harness = TestHarness()

# Or create with specific settings
harness = TestHarness(
    show_hints=True,    # Show helpful hints for failed tests
    use_colours=True    # Use coloured output in terminal
)

# Define test cases
test_cases = [
    ([1, 2], 3, "Simple addition"),
    ([0, 0], 0, "Zero addition"),
    ([-1, 1], 0, "Negative numbers")
]

# Run the tests
harness.run_test_suite(add_numbers, test_cases)
```

## Test Output Features

### Coloured Output
The test harness uses colours to make results clear:
- Green (✓) for passed tests
- Red (✗) for failed tests
- Yellow (✗) for errors
- Coloured summary statistics

Example output:
```
✓ Simple addition PASSED
  Input: [1, 2]
  Expected: 3
  Actual: 3

✗ Division test FAILED
  Input: [10, 2]
  Expected: 6
  Actual: 5
  Hint: The result (5) is too small

Test Suite Summary:
Total tests: 2
Passed: 1
Failed: 1
Success rate: 50.00%
```

### Educational Hints
When tests fail, the harness provides helpful hints:
- Type mismatches: "Function returned a str, but we expected an int"
- Numeric comparisons: "The result is too small/large"
- String issues: "The string lengths don't match"

## Test Case Format

Each test case is a tuple with:
1. Input arguments (in a list)
2. Expected output
3. Test name (optional)

Examples:
```python
# Basic format
([inputs], expected_output)

# With test name
([inputs], expected_output, "test name")

# Multiple inputs
([input1, input2], expected_output, "test name")
```

## Running Tests

### Method 1: Direct Script Execution
```python
# test_script.py
if __name__ == "__main__":
    harness = TestHarness()
    harness.run_test_suite(your_function, test_cases)
```

Run with:
```bash
python test_script.py
```

### Method 2: Interactive Python Shell
```python
>>> from test_harness import TestHarness
>>> harness = TestHarness()
>>> harness.run_test_suite(your_function, test_cases)
```

## Best Practices

1. Test Case Design
   - Test normal cases
   - Test edge cases (0, empty, max values)
   - Test error cases
   - Use descriptive test names

2. Output Reading
   - Green means success
   - Red means logical failure
   - Yellow means runtime error
   - Read hints for guidance

3. Test Organisation
   - Group related tests together
   - Use clear test names
   - Test one concept per test

## For Teachers

### Classroom Setup
1. Configure colour preferences:
   ```python
   harness = TestHarness(
       use_colours=True,    # False for non-terminal environments
       show_hints=True      # True for beginners
   )
   ```

2. Hint Levels:
   - Use show_hints=True for beginners
   - Disable hints for advanced exercises

### Teaching Tips
1. Start with simple functions
2. Use hints to guide learning
3. Progress to more complex examples
4. Encourage students to write their own tests

## Troubleshooting

Common issues and solutions:

1. No Colours Showing
   - Check terminal support
   - Verify use_colours=True
   - Try in different terminal

2. Test Case Errors
   - Verify tuple format
   - Check input list syntax
   - Confirm expected output type

3. Hint Issues
   - Verify show_hints=True
   - Check function output types
   - Review expected values

## Next Steps

1. Try the [example scripts](../examples/python/)
2. Practice writing test cases
3. Explore advanced features
4. Create your own test scenarios