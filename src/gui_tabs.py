"""
GUI Tab Definitions
====================

Tab construction methods for the Ca2+ Signature Analyzer GUI.
Split out from gui_app.py to keep files under 500 lines.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DatabaseTabMixin:
    """Mixin providing database tab construction."""

    def create_database_tab(self):
        """Create database management tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Database")

        # Left panel: Controls
        left_panel = ttk.Frame(tab)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

        ttk.Label(left_panel, text="Signature Database",
                 font=('Arial', 12, 'bold')).pack(pady=5)

        ttk.Button(left_panel, text="Load Example Database",
                  command=self.load_example_data).pack(pady=5, fill=tk.X)

        ttk.Button(left_panel, text="View Statistics",
                  command=self.show_database_stats).pack(pady=5, fill=tk.X)

        ttk.Separator(left_panel, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)

        ttk.Label(left_panel, text="Add New Signature",
                 font=('Arial', 10, 'bold')).pack(pady=5)

        # Simple form for adding signatures
        form_frame = ttk.Frame(left_panel)
        form_frame.pack(fill=tk.X, pady=5)

        ttk.Label(form_frame, text="ID:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.sig_id_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.sig_id_var, width=20).grid(row=0, column=1, pady=2)

        ttk.Label(form_frame, text="Stimulus:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.sig_stimulus_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.sig_stimulus_var, width=20).grid(row=1, column=1, pady=2)

        ttk.Label(form_frame, text="Peak (nM):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.sig_peak_var = tk.StringVar(value="800")
        ttk.Entry(form_frame, textvariable=self.sig_peak_var, width=20).grid(row=2, column=1, pady=2)

        ttk.Button(left_panel, text="Add to Database",
                  command=self.add_signature_simple).pack(pady=5, fill=tk.X)

        # Right panel: Display
        right_panel = ttk.Frame(tab)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        ttk.Label(right_panel, text="Database Contents",
                 font=('Arial', 12, 'bold')).pack(pady=5)

        self.db_text = scrolledtext.ScrolledText(right_panel, width=80, height=30)
        self.db_text.pack(fill=tk.BOTH, expand=True)


class SimulationTabMixin:
    """Mixin providing simulation tab construction."""

    def create_simulation_tab(self):
        """Create simulation tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Simulate Signatures")

        # Left panel: Controls
        left_panel = ttk.Frame(tab)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        ttk.Label(left_panel, text="Biophysical Model",
                 font=('Arial', 12, 'bold')).pack(pady=5)

        # Stimulus selection
        ttk.Label(left_panel, text="Stimulus Type:").pack(pady=2)
        self.stimulus_var = tk.StringVar(value="ABA")
        stimulus_combo = ttk.Combobox(left_panel, textvariable=self.stimulus_var,
                                     values=['ABA', 'NaCl', 'mechanical_touch',
                                            'flg22', 'cold_shock', 'H2O2', 'glutamate'],
                                     state='readonly')
        stimulus_combo.pack(pady=5)

        # Duration
        ttk.Label(left_panel, text="Duration (s):").pack(pady=2)
        self.duration_var = tk.StringVar(value="600")
        ttk.Entry(left_panel, textvariable=self.duration_var).pack(pady=5)

        # Intensity
        ttk.Label(left_panel, text="Intensity:").pack(pady=2)
        self.intensity_var = tk.StringVar(value="1.0")
        ttk.Entry(left_panel, textvariable=self.intensity_var).pack(pady=5)

        # Run button
        ttk.Button(left_panel, text="Run Simulation",
                  command=self.run_simulation).pack(pady=20, fill=tk.X)

        # Save button
        ttk.Button(left_panel, text="Save to Database",
                  command=self.save_simulation_to_db).pack(pady=5, fill=tk.X)

        # Results display
        ttk.Separator(left_panel, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        ttk.Label(left_panel, text="Signature Features:",
                 font=('Arial', 10, 'bold')).pack(pady=5)

        self.sim_results_text = scrolledtext.ScrolledText(left_panel, width=35, height=15)
        self.sim_results_text.pack(fill=tk.BOTH, expand=True)

        # Right panel: Plot
        right_panel = ttk.Frame(tab)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.sim_figure = Figure(figsize=(8, 6))
        self.sim_canvas = FigureCanvasTkAgg(self.sim_figure, right_panel)
        self.sim_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Store simulation results
        self.last_simulation = None


class DecoderTabMixin:
    """Mixin providing decoder analysis tab construction."""

    def create_decoder_tab(self):
        """Create decoder analysis tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Decoder Analysis")

        # Left panel: Controls
        left_panel = ttk.Frame(tab)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        ttk.Label(left_panel, text="CDPK Decoder Panel",
                 font=('Arial', 12, 'bold')).pack(pady=5)

        ttk.Button(left_panel, text="Analyze All Signatures",
                  command=self.analyze_decoders).pack(pady=10, fill=tk.X)

        ttk.Button(left_panel, text="Show Dose-Response Curves",
                  command=self.show_dose_response).pack(pady=5, fill=tk.X)

        ttk.Button(left_panel, text="Generate Heatmap",
                  command=self.generate_decoder_heatmap).pack(pady=5, fill=tk.X)

        # Results
        ttk.Separator(left_panel, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        ttk.Label(left_panel, text="Analysis Results:",
                 font=('Arial', 10, 'bold')).pack(pady=5)

        self.decoder_results_text = scrolledtext.ScrolledText(left_panel, width=35, height=20)
        self.decoder_results_text.pack(fill=tk.BOTH, expand=True)

        # Right panel: Plot
        right_panel = ttk.Frame(tab)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.decoder_figure = Figure(figsize=(8, 6))
        self.decoder_canvas = FigureCanvasTkAgg(self.decoder_figure, right_panel)
        self.decoder_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


class InformationTabMixin:
    """Mixin providing information theory tab construction."""

    def create_information_tab(self):
        """Create information theory analysis tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Information Theory")

        # Left panel: Controls
        left_panel = ttk.Frame(tab)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        ttk.Label(left_panel, text="Information Analysis",
                 font=('Arial', 12, 'bold')).pack(pady=5)

        ttk.Button(left_panel, text="Calculate MI (Signatures)",
                  command=self.calculate_mutual_information).pack(pady=10, fill=tk.X)

        ttk.Button(left_panel, text="Test Classification",
                  command=self.test_classification).pack(pady=5, fill=tk.X)

        ttk.Button(left_panel, text="Analyze Information Flow",
                  command=self.analyze_information_flow).pack(pady=5, fill=tk.X)

        # Results
        ttk.Separator(left_panel, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        ttk.Label(left_panel, text="Information Metrics:",
                 font=('Arial', 10, 'bold')).pack(pady=5)

        self.info_results_text = scrolledtext.ScrolledText(left_panel, width=35, height=20)
        self.info_results_text.pack(fill=tk.BOTH, expand=True)

        # Right panel: Plot
        right_panel = ttk.Frame(tab)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.info_figure = Figure(figsize=(8, 6))
        self.info_canvas = FigureCanvasTkAgg(self.info_figure, right_panel)
        self.info_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


class VisualizationTabMixin:
    """Mixin providing visualization tab construction."""

    def create_visualization_tab(self):
        """Create comprehensive visualization tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Visualizations")

        # Left panel: Controls
        left_panel = ttk.Frame(tab)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        ttk.Label(left_panel, text="Generate Plots",
                 font=('Arial', 12, 'bold')).pack(pady=5)

        ttk.Button(left_panel, text="UMAP Projection",
                  command=self.generate_umap).pack(pady=5, fill=tk.X)

        ttk.Button(left_panel, text="Signature Comparison",
                  command=self.plot_signature_comparison).pack(pady=5, fill=tk.X)

        ttk.Button(left_panel, text="Generate Full Report",
                  command=self.generate_full_report).pack(pady=20, fill=tk.X)

        ttk.Separator(left_panel, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)

        ttk.Label(left_panel, text="Export Options:",
                 font=('Arial', 10, 'bold')).pack(pady=5)

        ttk.Button(left_panel, text="Export to CSV",
                  command=self.export_to_csv).pack(pady=5, fill=tk.X)

        ttk.Button(left_panel, text="Save All Figures",
                  command=self.save_all_figures).pack(pady=5, fill=tk.X)

        # Right panel: Plot
        right_panel = ttk.Frame(tab)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.vis_figure = Figure(figsize=(8, 6))
        self.vis_canvas = FigureCanvasTkAgg(self.vis_figure, right_panel)
        self.vis_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
