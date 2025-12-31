#!/usr/bin/env python3
"""
Quick launcher for Ca²⁺ Signature Analyzer GUI.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

if __name__ == "__main__":
    try:
        from src.gui_app import main
        main()
    except ImportError as e:
        print("Error: Missing dependencies.")
        print("Please install required packages:")
        print("  pip install -r requirements.txt")
        print(f"\nDetails: {e}")
        sys.exit(1)
