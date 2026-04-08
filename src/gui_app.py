"""
Main GUI Application
====================

Tabbed GUI interface for Ca2+ signature analysis.

This is the main entry point for the GUI. Tab construction and callback
logic are split into gui_tabs.py and gui_callbacks.py respectively to
keep each file under 500 lines.
"""

import tkinter as tk
from tkinter import ttk
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from signature_database import SignatureDatabase
from biophysical_model import CalciumDynamicsModel
from decoder_model import DecoderPanel

# Import tab construction mixins
from gui_tabs import (
    DatabaseTabMixin,
    SimulationTabMixin,
    DecoderTabMixin,
    InformationTabMixin,
    VisualizationTabMixin,
)

# Import callback mixins
from gui_callbacks import (
    DatabaseCallbacksMixin,
    SimulationCallbacksMixin,
    DecoderCallbacksMixin,
    InformationCallbacksMixin,
    VisualizationCallbacksMixin,
)


class CaSignatureAnalyzerGUI(
    DatabaseTabMixin,
    SimulationTabMixin,
    DecoderTabMixin,
    InformationTabMixin,
    VisualizationTabMixin,
    DatabaseCallbacksMixin,
    SimulationCallbacksMixin,
    DecoderCallbacksMixin,
    InformationCallbacksMixin,
    VisualizationCallbacksMixin,
):
    """Main GUI application for Ca2+ signature analysis."""

    def __init__(self, root):
        self.root = root
        self.root.title("Ca2+ Signature Analyzer v1.0")
        self.root.geometry("1200x800")

        # Initialize data structures
        self.database = SignatureDatabase()
        self.model = CalciumDynamicsModel()
        self.decoder_panel = DecoderPanel()

        # Output directory
        self.output_dir = Path("outputs")
        self.output_dir.mkdir(exist_ok=True)

        # Create GUI
        self.create_menu()
        self.create_notebook()

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_menu(self):
        """Create menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Database (CSV)", command=self.load_database)
        file_menu.add_command(label="Save Database (CSV)", command=self.save_database)
        file_menu.add_separator()
        file_menu.add_command(label="Load Example Data", command=self.load_example_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_notebook(self):
        """Create tabbed interface."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Create tabs (from mixin classes)
        self.create_database_tab()
        self.create_simulation_tab()
        self.create_decoder_tab()
        self.create_information_tab()
        self.create_visualization_tab()


def main():
    """Main entry point."""
    root = tk.Tk()
    app = CaSignatureAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
