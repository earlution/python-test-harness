# Jupyter Setup Guide

This guide will help you set up Jupyter Notebooks to use the test harness in an interactive environment.

## Prerequisites

Before starting, ensure you have:
- Python 3.8 or higher installed
- pip (Python package installer)
- Command line/terminal access

## Installation Steps

### 1. Install Jupyter

Choose one of these methods:

#### Method A: Using pip
```bash
python -m pip install jupyter
```

#### Method B: Using Anaconda (Recommended for beginners)
1. Download Anaconda from [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Install Anaconda following the installer prompts
3. Jupyter comes pre-installed with Anaconda

### 2. Verify Installation

```bash
jupyter notebook --version
```

You should see a version number displayed.

## Starting Jupyter

1. Open your terminal/command prompt
2. Navigate to your project directory:
```bash
cd path/to/python-test-harness
```
3. Start Jupyter:
```bash
jupyter notebook
```
4. Your default web browser should open automatically to the Jupyter dashboard

## Setting Up the Test Harness in Jupyter

1. In the Jupyter dashboard, navigate to the `notebooks` directory
2. Open `test_harness_tutorial.ipynb`
3. Run the first cell to verify everything is working

## Troubleshooting

### Common Issues

1. **Jupyter not found**
   ```bash
   pip install --upgrade jupyter
   ```

2. **Kernel not starting**
   - Try restarting Jupyter
   - Check Python installation

3. **Import errors**
   - Verify you're in the correct directory
   - Check Python path settings

4. **Browser not opening**
   - Copy the URL displayed in terminal
   - Paste into your browser manually

## School Network Considerations

### Standard Installation
If you have administrator access:
1. Follow the standard installation steps above
2. Test on one machine first
3. Document any specific network requirements

### Network Restrictions
If you have limited access:
1. Contact IT support for installation assistance
2. Consider alternative setups (see below)

### Alternative Setups

#### 1. Portable Installation
```bash
python -m pip install --user jupyter
```

#### 2. Google Colab
- No installation required
- Runs in browser
- Requires Google account

#### 3. Zero Configuration Options
- Use MyBinder
- Consider JupyterLite
- Use online Python notebooks

## For System Administrators

### Network Requirements
- Allow TCP port 8888 (default Jupyter port)
- Enable WebSocket connections
- Allow browser connections to localhost

### Security Considerations
- Configure authentication
- Set up SSL if required
- Consider JupyterHub for multi-user setup

### Mass Deployment
Consider:
1. Group Policy deployment
2. Shared network installation
3. Virtual environment setup

## Testing Your Installation

1. Create a new notebook:
   - Click 'New' → 'Python 3'
   - Enter and run this code:
```python
print("Hello, Jupyter!")
```

2. Test the test harness:
```python
from test_harness import TestHarness
harness = TestHarness()
print("Test harness imported successfully!")
```

## Support

If you encounter issues:
1. Check the [Jupyter documentation](https://jupyter.org/documentation)
2. Review our [troubleshooting guide](troubleshooting.md)
3. Create an issue on our GitHub repository

## Next Steps

After installation:
1. Complete the [Jupyter tutorial](jupyter-guide.md)
2. Try the example notebooks
3. Start creating your own test cases

## Updates and Maintenance

- Keep Jupyter updated:
```bash
pip install --upgrade jupyter
```

- Check for test harness updates on our GitHub repository
- Review release notes for any breaking changes