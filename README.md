# Python Test Harness for Computer Science Education

A simple yet powerful test harness designed specifically for GCSE and A-Level Computer Science students in the UK. This tool helps students learn and practice test-driven development with clear, educational examples.

## Features

- Easy-to-use test framework for Python functions
- Detailed test output with clear pass/fail indicators
- Support for multiple test cases
- Comprehensive error handling and reporting
- Educational examples aligned with the UK Computer Science curriculum
- Available in both standard Python and Jupyter Notebook formats

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-test-harness.git
cd python-test-harness
```

2. No additional dependencies are required - the test harness uses only Python's standard library.

## Usage

### Basic Example

```python
from test_harness import TestHarness

# Create a function to test
def add_five(number):
    return number + 5

# Create test harness
harness = TestHarness()

# Define test cases
test_cases = [
    ([0], 5, "Adding five to zero"),
    ([10], 15, "Adding five to ten"),
    ([-3], 2, "Adding five to a negative number")
]

# Run the tests
harness.run_test_suite(add_five, test_cases)
```

### Test Case Format

Each test case consists of three elements:
1. Input arguments (in a list)
2. Expected output
3. Test name (optional)

Example: `([input], expected_output, "test name")`

## Educational Resources

This repository includes:

- `test_harness.py`: The main test harness code
- `examples.py`: Various example functions and tests
- `student_guide.md`: Detailed documentation for students
- `test_harness_tutorial.ipynb`: Interactive Jupyter Notebook tutorial
- Sample exercises and solutions

## For Teachers

The test harness is designed to support teaching of:
- Unit testing
- Test-driven development
- Code quality and reliability
- Debugging techniques
- Problem-solving skills

### Curriculum Alignment

The examples and exercises align with:
- GCSE Computer Science specifications
- A-Level Computer Science requirements
- Programming fundamentals
- Testing methodologies

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Guidelines for Contributing:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Licence

This project is licensed under the MIT Licence - see the [LICENCE](LICENCE) file for details.

## Acknowledgments

- Developed for UK Computer Science education
- Inspired by Python's unittest framework
- Created with input from Computer Science teachers

## Project Structure

```
python-test-harness/
│
├── src/
│   ├── test_harness.py
│   └── examples.py
│
├── docs/
│   ├── student_guide.md
│   └── teacher_guide.md
│
├── notebooks/
│   └── test_harness_tutorial.ipynb
│
├── examples/
│   ├── basic_examples.py
│   ├── gcse_examples.py
│   └── alevel_examples.py
│
├── tests/
│   └── test_harness_tests.py
│
├── README.md
├── LICENCE
└── .gitignore
```

## Contact

If you have any questions or suggestions, please open an issue on GitHub or contact the maintainers.

## Version History

- 1.0.0
    - Initial release
    - Basic test harness functionality
    - Educational documentation
    - Example suite
