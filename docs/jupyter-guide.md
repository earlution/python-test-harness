# Jupyter Implementation Guide

This guide covers using the test harness in a Jupyter environment for an enhanced interactive experience.

## Prerequisites

Ensure you have:
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- IPython

See the [Jupyter setup guide](jupyter-setup.md) for installation instructions.

## Getting Started

1. Start Jupyter:
```bash
jupyter notebook
```

2. Navigate to the `notebooks` directory
3. Open `test_harness_tutorial.ipynb`

## Using the Interactive Tutorial

The tutorial notebook contains:
1. Introduction to testing concepts
2. Live code examples
3. Interactive exercises
4. Challenge problems

### Running Cells

- Click a cell and press Shift+Enter to run it
- Run cells in order from top to bottom
- Wait for each cell to finish before running the next

### Modifying Code

- Double-click any code cell to edit
- Try changing values and running tests
- Add new test cases
- Create your own functions

## Classroom Usage

### Teacher Setup
1. Install Jupyter on teaching machine
2. Prepare the notebook environment
3. Test all examples beforehand

### Student Setup
1. Copy notebook files to student machines
2. Ensure Jupyter is installed and configured
3. Test notebook access

### Teaching Approaches

1. **Guided Learning**
   - Walk through notebook together
   - Students follow along
   - Stop for exercises

2. **Independent Learning**
   - Students work at their own pace
   - Teacher available for help
   - Check progress at checkpoints

3. **Pair Programming**
   - Students work in pairs
   - Take turns writing tests
   - Review each other's work

## Alternative Setups

### Google Colab
If local Jupyter installation isn't possible:
1. Upload notebooks to Google Colab
2. Share links with students
3. Students can run in browser

### MyBinder
For a consistent environment:
1. Create Binder configuration
2. Share Binder link
3. Students run in browser

## Troubleshooting

Common Jupyter issues:

1. Kernel Problems
   - Restart kernel
   - Run all cells again
   - Check for error messages

2. Package Installation
   - Use pip in notebook
   - Check package versions
   - Verify imports

3. Cell Execution
   - Run cells in order
   - Check for missing variables
   - Look for skipped cells

## Advanced Features

### Magic Commands
```python
%run test_harness.py
%matplotlib inline
%autoreload 2
```

### Debugging
```python
%debug
from IPython.core.debugger import set_trace
```

## Resources

- [Example Notebooks](../notebooks/)
- [Exercise Solutions](../notebooks/solutions/)
- [Advanced Topics](../notebooks/advanced/)

## Next Steps

1. Complete the tutorial notebook
2. Try the exercises
3. Create your own test cases
4. Explore advanced features