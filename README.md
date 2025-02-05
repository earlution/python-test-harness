# Python Test Harness for Computer Science Education

A simple yet powerful test harness designed specifically for GCSE and A-Level Computer Science students in the UK. This tool helps students learn and practice test-driven development with clear, educational examples.

## Quick Start

This project can be used in two ways:
1. **Python Only (Default)**: Standard Python implementation, works everywhere
2. **Jupyter Notebook (Optional)**: Enhanced interactive experience if Jupyter is available

Choose your preferred method:
- [Python Only Implementation](docs/python-guide.md)
- [Jupyter Notebook Implementation](docs/jupyter-guide.md)

## Features

- Easy-to-use test framework for Python functions
- Detailed test output with clear pass/fail indicators
- Support for multiple test cases
- Comprehensive error handling and reporting
- Educational examples aligned with the UK Computer Science curriculum
- Available in both standard Python and Jupyter Notebook formats

## Requirements

### Basic Requirements (Python Only)
- Python 3.8 or higher
- No additional dependencies required

### Optional Requirements (Jupyter Version)
- Jupyter Notebook/Lab
- IPython
- See [Jupyter setup guide](docs/jupyter_setup.md) for details

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-test-harness.git
cd python-test-harness
```

2. Choose your implementation:
   - For Python only: No additional setup needed
   - For Jupyter: Follow the [Jupyter setup guide](docs/jupyter_setup.md)

## Project Structure

```
python-test-harness/
│
├── src/                      # Core implementation
│   ├── test_harness.py      # Main test harness code
│   └── examples.py          # Example implementations
│
├── docs/                    # Documentation
│   ├── python-guide.md      # Guide for Python-only usage
│   ├── jupyter-guide.md     # Guide for Jupyter implementation
│   ├── jupyter-setup.md     # Jupyter setup instructions
│   └── examples.md          # Detailed examples for both approaches
│
├── notebooks/               # Optional Jupyter materials
│   └── test_harness_tutorial.ipynb
│
├── examples/                # Example code for both approaches
│   ├── python/             # Python-only examples
│   └── jupyter/            # Jupyter-specific examples
│
├── tests/                   # Unit tests
│   └── test_harness_tests.py
│
├── README.md
├── LICENCE
└── .gitignore
```

## Documentation

- [Python Implementation Guide](docs/python-guide.md)
- [Jupyter Implementation Guide](docs/jupyter-guide.md)
- [Example Usage](docs/examples.md)
- [Contributing Guidelines](docs/contributing.md)

## For Teachers

### Python-Only Environment
- Perfect for standard computer labs
- Works on any system with Python installed
- No additional setup required
- Command-line interface available

### Jupyter Environment (Optional)
- Interactive learning experience
- Real-time code execution
- Better for demonstrations
- Requires additional setup

## Contributing

Contributions are welcome! Please read our [Contributing Guidelines](docs/contributing.md) before submitting a Pull Request.

## Licence

This project is licensed under the MIT Licence - see the [LICENCE](LICENCE) file for details.