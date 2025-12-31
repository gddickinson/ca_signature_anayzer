"""
Main GUI Application
====================

Tabbed GUI interface for Ca²⁺ signature analysis.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from signature_database import SignatureDatabase, CalciumSignature, create_example_database
from biophysical_model import CalciumDynamicsModel, ModelParameters
from decoder_model import DecoderPanel, CDPKLibrary
from information_theory import (InformationAnalyzer, PathwayInformationFlow, 
                                SignatureDiscriminability)
from visualization import SignaturePlotter, IntegratedReport
import utils


class CaSignatureAnalyzerGUI:
    """Main GUI application for Ca²⁺ signature analysis."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ca²⁺ Signature Analyzer v1.0")
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
        
        # Create tabs
        self.create_database_tab()
        self.create_simulation_tab()
        self.create_decoder_tab()
        self.create_information_tab()
        self.create_visualization_tab()
    
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
    
    # Callback methods
    
    def load_database(self):
        """Load database from CSV file."""
        filename = filedialog.askopenfilename(
            title="Load Signature Database",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if filename:
            try:
                self.database = SignatureDatabase()
                self.database.load_from_csv(filename)
                self.status_var.set(f"Loaded {len(self.database)} signatures from {Path(filename).name}")
                self.update_database_display()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load database:\n{str(e)}")
    
    def save_database(self):
        """Save database to CSV file."""
        if len(self.database) == 0:
            messagebox.showwarning("Warning", "Database is empty")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save Signature Database",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if filename:
            try:
                self.database.save_to_csv(filename)
                self.status_var.set(f"Saved {len(self.database)} signatures to {Path(filename).name}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save database:\n{str(e)}")
    
    def load_example_data(self):
        """Load example database."""
        self.database = create_example_database()
        self.status_var.set(f"Loaded {len(self.database)} example signatures")
        self.update_database_display()
        messagebox.showinfo("Success", "Example database loaded successfully!")
    
    def update_database_display(self):
        """Update database text display."""
        self.db_text.delete(1.0, tk.END)
        
        if len(self.database) == 0:
            self.db_text.insert(tk.END, "Database is empty. Load example data or add signatures.")
            return
        
        # Show summary
        stats = self.database.get_summary_statistics()
        self.db_text.insert(tk.END, "=== DATABASE SUMMARY ===\n\n")
        for key, value in stats.items():
            self.db_text.insert(tk.END, f"{key}: {value}\n")
        
        self.db_text.insert(tk.END, "\n=== SIGNATURES ===\n\n")
        
        # Show signatures
        df = self.database.to_dataframe()
        self.db_text.insert(tk.END, df.to_string())
    
    def show_database_stats(self):
        """Show detailed database statistics."""
        if len(self.database) == 0:
            messagebox.showwarning("Warning", "Database is empty")
            return
        
        stats = self.database.get_summary_statistics()
        
        msg = "DATABASE STATISTICS\n\n"
        for key, value in stats.items():
            msg += f"{key}: {value}\n"
        
        messagebox.showinfo("Database Statistics", msg)
    
    def add_signature_simple(self):
        """Add signature with simple form."""
        try:
            sig_id = self.sig_id_var.get()
            stimulus = self.sig_stimulus_var.get()
            peak = float(self.sig_peak_var.get())
            
            if not sig_id or not stimulus:
                messagebox.showwarning("Warning", "Please fill in ID and Stimulus")
                return
            
            sig = CalciumSignature(
                signature_id=sig_id,
                species="Arabidopsis thaliana",
                cell_type="unknown",
                stimulus=stimulus,
                peak_amplitude=peak
            )
            
            self.database.add_signature(sig)
            self.update_database_display()
            self.status_var.set(f"Added signature: {sig_id}")
            
            # Clear form
            self.sig_id_var.set("")
            self.sig_stimulus_var.set("")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add signature:\n{str(e)}")
    
    def run_simulation(self):
        """Run biophysical model simulation."""
        try:
            stimulus = self.stimulus_var.get()
            duration = float(self.duration_var.get())
            intensity = float(self.intensity_var.get())
            
            self.status_var.set("Running simulation...")
            self.root.update()
            
            # Run simulation
            t, sol = self.model.simulate(stimulus, duration=duration, intensity=intensity)
            ca_cyt = sol[:, 0]
            
            # Extract features
            features = self.model.extract_signature_features(t, ca_cyt)
            
            # Store results
            self.last_simulation = {
                't': t,
                'ca_cyt': ca_cyt,
                'stimulus': stimulus,
                'features': features
            }
            
            # Plot
            self.sim_figure.clear()
            ax = self.sim_figure.add_subplot(111)
            ax.plot(t, ca_cyt / 1000, 'b-', linewidth=1.5)
            ax.set_xlabel('Time (s)', fontsize=12)
            ax.set_ylabel('[Ca²⁺] (μM)', fontsize=12)
            ax.set_title(f'{stimulus} Signature', fontweight='bold')
            ax.grid(True, alpha=0.3)
            self.sim_figure.tight_layout()
            self.sim_canvas.draw()
            
            # Display features
            self.sim_results_text.delete(1.0, tk.END)
            self.sim_results_text.insert(tk.END, "SIGNATURE FEATURES:\n\n")
            for key, value in features.items():
                if value is not None and not (isinstance(value, float) and np.isnan(value)):
                    self.sim_results_text.insert(tk.END, f"{key}: {value:.2f}\n")
            
            self.status_var.set("Simulation complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"Simulation failed:\n{str(e)}")
            self.status_var.set("Simulation failed")
    
    def save_simulation_to_db(self):
        """Save last simulation to database."""
        if self.last_simulation is None:
            messagebox.showwarning("Warning", "No simulation to save. Run a simulation first.")
            return
        
        try:
            features = self.last_simulation['features']
            stimulus = self.last_simulation['stimulus']
            
            # Generate unique ID
            sig_id = f"{stimulus}_{len(self.database)+1}"
            
            sig = CalciumSignature(
                signature_id=sig_id,
                species="Arabidopsis thaliana (simulated)",
                cell_type="model",
                stimulus=stimulus,
                baseline_ca=features['baseline_ca'],
                peak_amplitude=features['peak_amplitude'],
                rise_time=features['rise_time'] if not np.isnan(features['rise_time']) else 0,
                decay_tau=features['decay_tau'] if not np.isnan(features['decay_tau']) else 0,
                duration=features['duration'],
                latency=features['latency'] if not np.isnan(features['latency']) else 0,
                oscillatory=features['oscillatory'],
                frequency=features['frequency']
            )
            
            self.database.add_signature(sig)
            self.update_database_display()
            self.status_var.set(f"Saved simulation as: {sig_id}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save simulation:\n{str(e)}")
    
    def analyze_decoders(self):
        """Analyze all signatures with decoder panel."""
        if len(self.database) == 0:
            messagebox.showwarning("Warning", "Database is empty")
            return
        
        try:
            self.status_var.set("Analyzing decoders...")
            self.root.update()
            
            # For demonstration, analyze first few signatures
            results_text = "DECODER ANALYSIS RESULTS:\n\n"
            
            for i, sig in enumerate(self.database.signatures[:5]):  # Limit to 5 for speed
                results_text += f"\n--- {sig.signature_id} ({sig.stimulus}) ---\n"
                
                # Simulate Ca2+ trace for this signature
                t, sol = self.model.simulate(sig.stimulus, duration=sig.duration, intensity=1.0)
                ca_trace = sol[:, 0]
                
                # Analyze with decoder panel
                responses = self.decoder_panel.analyze_signature(t, ca_trace)
                
                # Show top 3 responding decoders
                sorted_decoders = sorted(responses.items(), 
                                       key=lambda x: x[1]['integrated_activation'],
                                       reverse=True)
                
                results_text += "Top 3 Responding CDPKs:\n"
                for name, resp in sorted_decoders[:3]:
                    results_text += f"  {name}: {resp['integrated_activation']:.1f}\n"
            
            self.decoder_results_text.delete(1.0, tk.END)
            self.decoder_results_text.insert(tk.END, results_text)
            
            self.status_var.set("Decoder analysis complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"Decoder analysis failed:\n{str(e)}")
            self.status_var.set("Analysis failed")
    
    def show_dose_response(self):
        """Show CDPK dose-response curves."""
        self.decoder_figure.clear()
        
        ca_range = np.logspace(1, 4, 100)  # 10 nM to 10 μM
        
        ax = self.decoder_figure.add_subplot(111)
        
        for decoder in self.decoder_panel.decoders:
            activation = [decoder.steady_state_activation(ca) for ca in ca_range]
            label = f"{decoder.params.name} (Kd={decoder.params.K_d:.0f} nM)"
            ax.semilogx(ca_range, activation, label=label, linewidth=2)
        
        ax.set_xlabel('[Ca²⁺] (nM)', fontsize=12)
        ax.set_ylabel('Fractional Activation', fontsize=12)
        ax.set_title('CDPK Ca²⁺ Dose-Response Curves', fontsize=14, fontweight='bold')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_ylim([0, 1.05])
        
        self.decoder_figure.tight_layout()
        self.decoder_canvas.draw()
    
    def generate_decoder_heatmap(self):
        """Generate decoder response heatmap."""
        if len(self.database) == 0:
            messagebox.showwarning("Warning", "Database is empty")
            return
        
        try:
            self.status_var.set("Generating heatmap...")
            self.root.update()
            
            # Simulate signatures and get decoder responses
            t_list = []
            ca_list = []
            labels = []
            
            for sig in self.database.signatures[:10]:  # Limit to 10
                t, sol = self.model.simulate(sig.stimulus, duration=300, intensity=1.0)
                t_list.append(t)
                ca_list.append(sol[:, 0])
                labels.append(sig.stimulus)
            
            # Get response matrix
            matrix = self.decoder_panel.get_response_matrix(t_list, ca_list)
            
            # Plot heatmap
            SignaturePlotter.plot_decoder_heatmap(
                matrix,
                self.decoder_panel.names,
                labels,
                output_path=str(self.output_dir / "decoder_heatmap.png")
            )
            
            messagebox.showinfo("Success", f"Heatmap saved to {self.output_dir / 'decoder_heatmap.png'}")
            self.status_var.set("Heatmap generated")
            
        except Exception as e:
            messagebox.showerror("Error", f"Heatmap generation failed:\n{str(e)}")
            self.status_var.set("Heatmap failed")
    
    def calculate_mutual_information(self):
        """Calculate mutual information for signatures."""
        if len(self.database) < 5:
            messagebox.showwarning("Warning", "Need at least 5 signatures for MI analysis")
            return
        
        try:
            self.status_var.set("Calculating mutual information...")
            self.root.update()
            
            # Get features and labels
            features = self.database.get_feature_matrix()
            stimuli = [sig.stimulus for sig in self.database.signatures]
            
            # Encode stimuli as integers
            unique_stimuli = list(set(stimuli))
            labels = np.array([unique_stimuli.index(s) for s in stimuli])
            
            # Calculate capacity
            metrics = InformationAnalyzer.estimate_signature_capacity(features, labels)
            
            # Display results
            self.info_results_text.delete(1.0, tk.END)
            self.info_results_text.insert(tk.END, "INFORMATION METRICS:\n\n")
            
            for key, value in metrics.items():
                if key != 'mi_per_feature':
                    self.info_results_text.insert(tk.END, f"{key}: {value:.3f}\n")
            
            self.status_var.set("MI calculation complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"MI calculation failed:\n{str(e)}")
            self.status_var.set("MI calculation failed")
    
    def test_classification(self):
        """Test signature classification accuracy."""
        if len(self.database) < 10:
            messagebox.showwarning("Warning", "Need at least 10 signatures for classification")
            return
        
        try:
            self.status_var.set("Testing classification...")
            self.root.update()
            
            # Get features and labels
            features = self.database.get_feature_matrix()
            stimuli = [sig.stimulus for sig in self.database.signatures]
            
            # Test classification
            results = SignatureDiscriminability.classification_accuracy(
                features, np.array(stimuli), classifier='random_forest'
            )
            
            # Display results
            self.info_results_text.delete(1.0, tk.END)
            self.info_results_text.insert(tk.END, "CLASSIFICATION RESULTS:\n\n")
            self.info_results_text.insert(tk.END, f"Accuracy: {results['accuracy_mean']:.3f} ± {results['accuracy_std']:.3f}\n")
            self.info_results_text.insert(tk.END, f"Information: {results['information_bits']:.3f} / {results['max_information_bits']:.3f} bits\n")
            self.info_results_text.insert(tk.END, f"N classes: {results['n_classes']}\n")
            self.info_results_text.insert(tk.END, f"N samples: {results['n_samples']}\n")
            
            # Plot confusion matrix
            self.info_figure.clear()
            ax = self.info_figure.add_subplot(111)
            
            import seaborn as sns
            conf_matrix = results['confusion_matrix']
            sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', ax=ax)
            ax.set_xlabel('Predicted', fontsize=12)
            ax.set_ylabel('True', fontsize=12)
            ax.set_title('Confusion Matrix', fontweight='bold')
            
            self.info_figure.tight_layout()
            self.info_canvas.draw()
            
            self.status_var.set("Classification complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"Classification failed:\n{str(e)}")
            self.status_var.set("Classification failed")
    
    def analyze_information_flow(self):
        """Analyze information flow through pathway."""
        if len(self.database) < 5:
            messagebox.showwarning("Warning", "Need at least 5 signatures")
            return
        
        try:
            self.status_var.set("Analyzing information flow...")
            self.root.update()
            
            # Create pathway
            pathway = PathwayInformationFlow()
            
            # Get signatures
            stimuli = np.array([sig.stimulus for sig in self.database.signatures])
            features = self.database.get_feature_matrix()
            
            # Simulate decoder responses
            decoder_responses = []
            for sig in self.database.signatures:
                t, sol = self.model.simulate(sig.stimulus, duration=300)
                responses = self.decoder_panel.analyze_signature(t, sol[:, 0])
                integrated = [r['integrated_activation'] for r in responses.values()]
                decoder_responses.append(integrated)
            decoder_responses = np.array(decoder_responses)
            
            # Add stages
            pathway.add_stage("Stimulus", stimuli.reshape(-1, 1))
            pathway.add_stage("Ca_Signature", features)
            pathway.add_stage("CDPK_Response", decoder_responses)
            
            # Calculate flow
            flow = pathway.calculate_flow()
            
            # Display
            self.info_results_text.delete(1.0, tk.END)
            self.info_results_text.insert(tk.END, "INFORMATION FLOW:\n\n")
            for key, value in flow.items():
                self.info_results_text.insert(tk.END, f"{key}: {value:.3f} bits\n")
            
            # Plot
            SignaturePlotter.plot_information_flow(
                flow,
                output_path=str(self.output_dir / "information_flow.png")
            )
            
            self.status_var.set("Information flow analysis complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"Information flow analysis failed:\n{str(e)}")
            self.status_var.set("Analysis failed")
    
    def generate_umap(self):
        """Generate UMAP projection."""
        if len(self.database) < 5:
            messagebox.showwarning("Warning", "Need at least 5 signatures for UMAP")
            return
        
        try:
            self.status_var.set("Generating UMAP...")
            self.root.update()
            
            features = self.database.get_feature_matrix()
            stimuli = np.array([sig.stimulus for sig in self.database.signatures])
            
            SignaturePlotter.plot_umap_projection(
                features,
                stimuli,
                output_path=str(self.output_dir / "umap_projection.png")
            )
            
            messagebox.showinfo("Success", f"UMAP saved to {self.output_dir / 'umap_projection.png'}")
            self.status_var.set("UMAP complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"UMAP failed:\n{str(e)}")
            self.status_var.set("UMAP failed")
    
    def plot_signature_comparison(self):
        """Plot signature comparison."""
        if len(self.database) == 0:
            messagebox.showwarning("Warning", "Database is empty")
            return
        
        try:
            self.status_var.set("Generating comparison plot...")
            self.root.update()
            
            # Simulate first few signatures
            t_list = []
            ca_list = []
            labels = []
            
            for sig in self.database.signatures[:5]:
                t, sol = self.model.simulate(sig.stimulus, duration=300)
                t_list.append(t)
                ca_list.append(sol[:, 0])
                labels.append(f"{sig.signature_id} ({sig.stimulus})")
            
            SignaturePlotter.plot_signature_comparison(
                t_list, ca_list, labels,
                output_path=str(self.output_dir / "signature_comparison.png")
            )
            
            messagebox.showinfo("Success", f"Comparison saved to {self.output_dir / 'signature_comparison.png'}")
            self.status_var.set("Comparison complete")
            
        except Exception as e:
            messagebox.showerror("Error", f"Comparison failed:\n{str(e)}")
            self.status_var.set("Comparison failed")
    
    def generate_full_report(self):
        """Generate comprehensive HTML report."""
        if len(self.database) == 0:
            messagebox.showwarning("Warning", "Database is empty")
            return
        
        try:
            self.status_var.set("Generating full report...")
            self.root.update()
            
            report = IntegratedReport(str(self.output_dir))
            
            # Generate all analyses
            # (This is placeholder - in full version would run all analyses)
            
            messagebox.showinfo("Info", "Full report generation not yet implemented.\nPlease run individual analyses and save figures.")
            self.status_var.set("Ready")
            
        except Exception as e:
            messagebox.showerror("Error", f"Report generation failed:\n{str(e)}")
    
    def export_to_csv(self):
        """Export database to CSV."""
        self.save_database()
    
    def save_all_figures(self):
        """Save all generated figures."""
        messagebox.showinfo("Info", f"Figures are automatically saved to:\n{self.output_dir.absolute()}")
    
    def show_about(self):
        """Show about dialog."""
        about_text = """Ca²⁺ Signature Analyzer v1.0

A comprehensive toolkit for analyzing plant calcium signaling dynamics using information theory and biophysical modeling.

Features:
- Signature database management
- Biophysical Ca²⁺ dynamics simulation
- CDPK decoder analysis
- Information theory calculations
- Comprehensive visualizations

Author: George (2025)
License: MIT"""
        
        messagebox.showinfo("About", about_text)


def main():
    """Main entry point."""
    root = tk.Tk()
    app = CaSignatureAnalyzerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
