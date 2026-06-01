# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/abhilashbha/Diabetes-Prediction-ML.git
cd Diabetes-Prediction-ML
```

## Step 2: Create Virtual Environment

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Step 4: Verify Installation

```bash
python -c "import pandas, numpy, sklearn, streamlit; print('All packages installed successfully!')"
```

## Step 5: Run the Application

### To run the main prediction script:
```bash
python diabetes_prediction.py
```

### To run the Streamlit web interface:
```bash
streamlit run app.py
```

The Streamlit dashboard will open in your default browser at `http://localhost:8501`

## Troubleshooting

### Issue: `pip: command not found`
- Ensure Python is installed: `python --version`
- Try `pip3` instead of `pip`

### Issue: Virtual environment not activating
- Check if venv is created: `ls venv` (macOS/Linux) or `dir venv` (Windows)
- Recreate it: `python -m venv venv`

### Issue: Module import errors
- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

## Development Setup

For contributing to the project:

```bash
# Install with development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov  # For testing
```

## Getting Help

If you encounter issues:
1. Check the README.md
2. Review the Issues section on GitHub
3. Open a new issue with detailed error messages

Happy analyzing! 🎉
