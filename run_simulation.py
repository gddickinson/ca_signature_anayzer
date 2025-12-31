#!/usr/bin/env python3
"""
Standalone script for running Ca²⁺ signature simulations.

Usage:
    python run_simulation.py --stimulus ABA --duration 600 --output simulation_results.csv
"""

import argparse
import sys
from pathlib import Path
import numpy as np
import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from biophysical_model import CalciumDynamicsModel, ModelParameters
from visualization import SignaturePlotter
import utils


def main():
    parser = argparse.ArgumentParser(description='Run Ca²⁺ signature simulation')
    
    parser.add_argument('--stimulus', type=str, default='ABA',
                       choices=['ABA', 'NaCl', 'mechanical_touch', 'flg22', 
                               'cold_shock', 'H2O2', 'glutamate'],
                       help='Stimulus type')
    parser.add_argument('--duration', type=float, default=600.0,
                       help='Simulation duration (seconds)')
    parser.add_argument('--intensity', type=float, default=1.0,
                       help='Stimulus intensity')
    parser.add_argument('--output', type=str, default='outputs/simulation.csv',
                       help='Output CSV file path')
    parser.add_argument('--plot', type=str, default='outputs/simulation.png',
                       help='Output plot file path')
    
    args = parser.parse_args()
    
    print(f"Running simulation: {args.stimulus}")
    print(f"  Duration: {args.duration}s")
    print(f"  Intensity: {args.intensity}")
    
    # Create model
    model = CalciumDynamicsModel()
    
    # Run simulation
    print("\nSimulating...")
    t, sol = model.simulate(args.stimulus, duration=args.duration, 
                           intensity=args.intensity)
    
    ca_cyt = sol[:, 0]
    ca_er = sol[:, 1]
    ca_vac = sol[:, 2]
    ip3 = sol[:, 3]
    
    # Extract features
    print("Extracting features...")
    features = model.extract_signature_features(t, ca_cyt)
    
    print("\nSignature Features:")
    for key, value in features.items():
        if value is not None and not (isinstance(value, float) and np.isnan(value)):
            print(f"  {key}: {value:.2f}")
    
    # Save results
    print(f"\nSaving results to {args.output}...")
    utils.ensure_directory(Path(args.output).parent)
    
    data = {
        'time_s': t,
        'Ca_cyt_nM': ca_cyt,
        'Ca_ER_nM': ca_er,
        'Ca_vac_nM': ca_vac,
        'IP3_nM': ip3
    }
    utils.export_to_csv(data, args.output)
    
    # Plot
    if args.plot:
        print(f"Generating plot: {args.plot}...")
        SignaturePlotter.plot_signature_comparison(
            [t], [ca_cyt],
            [f"{args.stimulus} (intensity={args.intensity})"],
            output_path=args.plot,
            title=f"Ca²⁺ Signature: {args.stimulus}"
        )
    
    print("\nComplete!")


if __name__ == "__main__":
    main()
