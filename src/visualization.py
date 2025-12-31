"""
Visualization Module
====================

Plotting and visualization tools for Ca²⁺ signature analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Optional, Tuple
from pathlib import Path
import pandas as pd


class SignaturePlotter:
    """Plotting tools for Ca²⁺ signatures."""
    
    @staticmethod
    def plot_signature_comparison(t_list: List[np.ndarray],
                                  ca_traces: List[np.ndarray],
                                  labels: List[str],
                                  output_path: Optional[str] = None,
                                  title: str = "Ca²⁺ Signature Comparison"):
        """
        Plot multiple Ca²⁺ signatures for comparison.
        
        Parameters
        ----------
        t_list : List[np.ndarray]
            List of time arrays
        ca_traces : List[np.ndarray]
            List of Ca²⁺ concentration traces
        labels : List[str]
            Labels for each trace
        output_path : Optional[str]
            Save path (if None, display instead)
        title : str
            Plot title
        """
        n_traces = len(ca_traces)
        
        fig, axes = plt.subplots(n_traces, 1, figsize=(12, 2*n_traces), 
                                sharex=True)
        
        if n_traces == 1:
            axes = [axes]
        
        for i, (t, ca, label) in enumerate(zip(t_list, ca_traces, labels)):
            axes[i].plot(t, ca / 1000, 'b-', linewidth=1.5)  # Convert to μM
            axes[i].set_ylabel('[Ca²⁺] (μM)', fontsize=10)
            axes[i].set_title(label, fontweight='bold', fontsize=11)
            axes[i].grid(True, alpha=0.3)
            axes[i].set_ylim(bottom=0)
        
        axes[-1].set_xlabel('Time (s)', fontsize=12)
        fig.suptitle(title, fontsize=14, fontweight='bold', y=0.995)
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    @staticmethod
    def plot_decoder_heatmap(decoder_matrix: np.ndarray,
                            decoder_names: List[str],
                            signature_labels: List[str],
                            output_path: Optional[str] = None,
                            title: str = "Decoder Response Matrix"):
        """
        Plot heatmap of decoder responses to signatures.
        
        Parameters
        ----------
        decoder_matrix : np.ndarray
            Matrix [n_decoders, n_signatures]
        decoder_names : List[str]
            Names of decoders
        signature_labels : List[str]
            Labels for signatures
        output_path : Optional[str]
            Save path
        title : str
            Plot title
        """
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Normalize each row for better visualization
        matrix_norm = decoder_matrix / (decoder_matrix.max(axis=1, keepdims=True) + 1e-10)
        
        sns.heatmap(matrix_norm, annot=False, cmap='viridis',
                   xticklabels=signature_labels,
                   yticklabels=decoder_names,
                   cbar_kws={'label': 'Normalized Activation'},
                   ax=ax)
        
        ax.set_xlabel('Signature', fontsize=12, fontweight='bold')
        ax.set_ylabel('Decoder', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    @staticmethod
    def plot_umap_projection(features: np.ndarray,
                            labels: np.ndarray,
                            output_path: Optional[str] = None,
                            title: str = "Ca²⁺ Signature Space (UMAP)"):
        """
        Plot UMAP projection of signature feature space.
        
        Parameters
        ----------
        features : np.ndarray
            Feature matrix [n_samples, n_features]
        labels : np.ndarray
            Labels for coloring
        output_path : Optional[str]
            Save path
        title : str
            Plot title
        """
        from umap import UMAP
        
        # Perform UMAP
        reducer = UMAP(n_components=2, random_state=42, min_dist=0.1)
        embedding = reducer.fit_transform(features)
        
        # Plot
        fig, ax = plt.subplots(figsize=(10, 8))
        
        unique_labels = np.unique(labels)
        colors = plt.cm.tab10(np.linspace(0, 1, len(unique_labels)))
        
        for i, label in enumerate(unique_labels):
            mask = labels == label
            ax.scatter(embedding[mask, 0], embedding[mask, 1],
                      c=[colors[i]], label=str(label), s=100, alpha=0.7,
                      edgecolors='black', linewidth=0.5)
        
        ax.set_xlabel('UMAP 1', fontsize=12, fontweight='bold')
        ax.set_ylabel('UMAP 2', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    @staticmethod
    def plot_information_flow(flow_dict: Dict[str, float],
                             output_path: Optional[str] = None,
                             title: str = "Information Flow Through Pathway"):
        """
        Plot information flow through signaling pathway.
        
        Parameters
        ----------
        flow_dict : Dict[str, float]
            Dictionary of stage transitions and MI values
        output_path : Optional[str]
            Save path
        title : str
            Plot title
        """
        # Extract stage transitions
        transitions = []
        mi_values = []
        
        for key, value in flow_dict.items():
            if '→' in key:
                transitions.append(key)
                mi_values.append(value)
        
        if len(transitions) == 0:
            print("No stage transitions found in flow_dict")
            return
        
        # Create bar plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        x_pos = np.arange(len(transitions))
        bars = ax.bar(x_pos, mi_values, color='steelblue', alpha=0.7,
                     edgecolor='black', linewidth=1.5)
        
        # Color bars by magnitude
        max_mi = max(mi_values)
        for i, (bar, mi) in enumerate(zip(bars, mi_values)):
            bar.set_color(plt.cm.viridis(mi / max_mi))
        
        ax.set_xticks(x_pos)
        ax.set_xticklabels(transitions, rotation=45, ha='right')
        ax.set_ylabel('Mutual Information (bits)', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for i, (x, y) in enumerate(zip(x_pos, mi_values)):
            ax.text(x, y, f'{y:.2f}', ha='center', va='bottom', 
                   fontweight='bold', fontsize=10)
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()
    
    @staticmethod
    def plot_confusion_matrix(conf_matrix: np.ndarray,
                             class_labels: List[str],
                             output_path: Optional[str] = None,
                             title: str = "Signature Classification Confusion Matrix"):
        """
        Plot confusion matrix for signature classification.
        
        Parameters
        ----------
        conf_matrix : np.ndarray
            Confusion matrix [n_classes, n_classes]
        class_labels : List[str]
            Class labels
        output_path : Optional[str]
            Save path
        title : str
            Plot title
        """
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Normalize by row (true labels)
        conf_matrix_norm = conf_matrix.astype(float) / conf_matrix.sum(axis=1, keepdims=True)
        
        sns.heatmap(conf_matrix_norm, annot=True, fmt='.2f', cmap='Blues',
                   xticklabels=class_labels,
                   yticklabels=class_labels,
                   cbar_kws={'label': 'Fraction'},
                   vmin=0, vmax=1,
                   ax=ax)
        
        ax.set_xlabel('Predicted Label', fontsize=12, fontweight='bold')
        ax.set_ylabel('True Label', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        
        if output_path:
            plt.savefig(output_path, dpi=150, bbox_inches='tight')
            plt.close()
        else:
            plt.show()


class IntegratedReport:
    """Generate comprehensive analysis report with multiple plots."""
    
    def __init__(self, output_dir: str = "outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)
        self.figures = []
    
    def add_figure(self, fig_name: str, fig_path: str):
        """Add figure to report."""
        self.figures.append({'name': fig_name, 'path': fig_path})
    
    def generate_html_report(self, title: str = "Ca²⁺ Signature Analysis Report"):
        """Generate HTML report with all figures."""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
        }}
        .figure {{
            background-color: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }}
        .timestamp {{
            color: #7f8c8d;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p class="timestamp">Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
"""
        
        for fig in self.figures:
            # Convert absolute path to relative
            rel_path = Path(fig['path']).name
            
            html += f"""
    <div class="figure">
        <h2>{fig['name']}</h2>
        <img src="{rel_path}" alt="{fig['name']}">
    </div>
"""
        
        html += """
</body>
</html>
"""
        
        # Save HTML
        report_path = self.output_dir / "analysis_report.html"
        with open(report_path, 'w') as f:
            f.write(html)
        
        print(f"HTML report saved to: {report_path}")
        return report_path


if __name__ == "__main__":
    # Test visualization functions
    print("Testing Visualization Module\n")
    
    # Test 1: Signature comparison
    print("Generating signature comparison plot...")
    t1 = np.linspace(0, 300, 1000)
    ca1 = 100 + 600 * (np.sin(2*np.pi*0.5*t1) + 1) / 2  # Oscillatory
    ca2 = 100 + 500 * np.exp(-t1/100)  # Exponential decay
    
    SignaturePlotter.plot_signature_comparison(
        [t1, t1],
        [ca1, ca2],
        ['Oscillatory (0.5 Hz)', 'Transient Spike'],
        output_path='/home/claude/ca_signature_analyzer/outputs/test_signatures.png'
    )
    print("  Saved to outputs/test_signatures.png\n")
    
    # Test 2: Decoder heatmap
    print("Generating decoder heatmap...")
    decoder_matrix = np.random.rand(10, 5) * 100
    decoder_names = [f'CDPK{i}' for i in range(1, 11)]
    signature_labels = ['ABA', 'NaCl', 'Touch', 'Pathogen', 'Cold']
    
    SignaturePlotter.plot_decoder_heatmap(
        decoder_matrix,
        decoder_names,
        signature_labels,
        output_path='/home/claude/ca_signature_analyzer/outputs/test_heatmap.png'
    )
    print("  Saved to outputs/test_heatmap.png\n")
    
    print("Visualization tests complete!")
