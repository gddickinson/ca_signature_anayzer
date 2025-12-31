# Installation Instructions

## System Requirements

- Python 3.7 or higher
- pip package manager
- 500 MB disk space
- 2 GB RAM (recommended)

## Step-by-Step Installation

### 1. Verify Python Installation

```bash
python3 --version
# Should show: Python 3.7.x or higher
```

If Python is not installed:
- **Linux/Mac**: Already installed or use package manager
- **Windows**: Download from https://www.python.org/downloads/

### 2. Install Dependencies

Navigate to the project directory:
```bash
cd ca_signature_analyzer
```

Install required packages:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install numpy scipy pandas matplotlib seaborn scikit-learn umap-learn
```

### 3. Verify Installation

Test if all modules can be imported:
```bash
python3 -c "import numpy, scipy, pandas, matplotlib, sklearn, umap; print('✓ All dependencies OK!')"
```

### 4. Test the Application

Run a quick test:
```bash
python3 src/signature_database.py
```

You should see:
```
Created database with 7 signatures
...
Saved to .../data/example_signatures.csv
```

### 5. Launch the GUI

```bash
python3 launch_gui.py
```

The GUI window should appear with 5 tabs.

## Troubleshooting

### Issue: "ModuleNotFoundError"

**Solution**: Install missing package
```bash
pip install <package_name>
```

### Issue: "tkinter not found"

**Solution**: Install tkinter (it should come with Python)
- **Ubuntu/Debian**: `sudo apt-get install python3-tk`
- **macOS**: Should be included with Python
- **Windows**: Reinstall Python with "tcl/tk" option checked

### Issue: UMAP installation fails

**Solution**: Install with specific version
```bash
pip install umap-learn==0.5.3
```

### Issue: Permission denied

**Solution**: Use user install
```bash
pip install --user -r requirements.txt
```

### Issue: Older Python version

**Solution**: Use virtual environment or update Python
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Platform-Specific Notes

### Linux
- Most distributions have Python 3 pre-installed
- May need to install python3-pip: `sudo apt-get install python3-pip`

### macOS  
- Use Homebrew Python for best compatibility: `brew install python`
- May need Xcode Command Line Tools: `xcode-select --install`

### Windows
- Download Python from python.org
- Check "Add Python to PATH" during installation
- Use Command Prompt or PowerShell

## Virtual Environment (Optional but Recommended)

Create isolated environment:
```bash
python3 -m venv ca_env
source ca_env/bin/activate  # On Windows: ca_env\Scripts\activate
pip install -r requirements.txt
```

Deactivate when done:
```bash
deactivate
```

## Verification Checklist

After installation, verify:

- [ ] Python 3.7+ installed
- [ ] All dependencies installed (run test command above)
- [ ] Example database can be created
- [ ] GUI launches without errors
- [ ] Can run standalone scripts

## Getting Started

Once installed:

1. Read QUICKSTART.md for a 10-minute introduction
2. Launch the GUI: `python3 launch_gui.py`
3. Load example data: File → Load Example Data
4. Explore the different tabs
5. Run your first simulation!

## Support

If you encounter issues:
1. Check Python version
2. Verify all dependencies are installed
3. Review error messages carefully
4. Check QUICKSTART.md and README.md for solutions

## Success!

You should now be ready to analyze Ca²⁺ signatures! 🎉
