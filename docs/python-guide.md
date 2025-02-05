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

# Create test harness
harness = TestHarness()

# Define test cases
test_cases = [
    ([1, 2], 3, "Simple addition"),
    ([0, 0], 0, "Zero addition"),
    ([-1, 1], 0, "Negative numbers")
]

# Run the tests
harness.run_test_suite(add_numbers, test_cases)
```

## Running Tests

You can run tests in several ways:

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

### Method 3: Import in Another Script
```python
# your_tests.py
from test_harness import TestHarness
from your_module import your_function

harness = TestHarness()
harness.run_test_suite(your_function, test_cases)
```

## Examples

See the [examples](../examples/python/) directory for more detailed examples.

## Command-Line Interface

For batch testing, you can use the command-line interface:

```bash
python -m test_harness tests_file.py
```

## Best Practices

1. Keep test cases in a separate file from your main code
2. Use descriptive test names
3. Test edge cases and normal cases
4. Group related tests together
5. Use meaningful variable names

## Troubleshooting

Common issues and solutions:

1. ImportError:
   - Ensure test_harness.py is in your Python path
   - Check you're in the correct directory

2. Test failures:
   - Check input types match expected types
   - Verify expected outputs
   - Look for off-by-one errors

3. Syntax errors:
   - Verify test case format: ([inputs], expected_output, "name")
   - Check for missing commas or brackets

## For Teachers

### Classroom Setup
1. Install Python on all machines
2. Copy test_harness.py to a shared location
3. Prepare example scripts

### Teaching Tips
1. Start with simple functions
2. Build up to more complex examples
3. Use pair programming exercises
4. Encourage students to write their own test cases

## Next Steps

- Explore the [examples](../examples/python/)
- Read the [full documentation](../docs/)
- Try the [exercises](../examples/python/exercises/)