# Ca²⁺ Signature Analyzer - Quick Start Guide

## Installation (5 minutes)

1. **Check Python version** (must be 3.7+):
```bash
python3 --version
```

2. **Install dependencies**:
```bash
cd ca_signature_analyzer
pip install -r requirements.txt
```

3. **Verify installation**:
```bash
python3 -c "import numpy, scipy, pandas, matplotlib, sklearn; print('All dependencies OK!')"
```

## Quick Start Options

### Option 1: GUI Application (Recommended for Beginners)

Launch the graphical interface:
```bash
python3 launch_gui.py
```

**First Steps in GUI:**
1. Click "File" → "Load Example Data"
2. Go to "Simulate Signatures" tab
3. Click "Run Simulation"
4. Explore other tabs!

### Option 2: Command-Line Analysis

Run a complete analysis on example data:
```bash
python3 analyze_database.py
```

This will:
- Load example signatures
- Generate visualizations
- Calculate information metrics
- Save results to `outputs/analysis/`

View results:
```bash
ls -lh outputs/analysis/
```

### Option 3: Python Scripts

Run a single simulation:
```bash
python3 run_simulation.py --stimulus ABA --duration 600
```

View output:
```bash
cat outputs/simulation.csv | head -10
```

## Example Session (10 minutes)

### 1. Load and Explore Data

```python
from src.signature_database import create_example_database

# Load example data
db = create_example_database()
print(f"Loaded {len(db)} signatures")

# View statistics
stats = db.get_summary_statistics()
for key, value in stats.items():
    print(f"{key}: {value}")
```

### 2. Run a Simulation

```python
from src.biophysical_model import CalciumDynamicsModel

model = CalciumDynamicsModel()

# Simulate ABA response
t, sol = model.simulate('ABA', duration=600)
ca_cyt = sol[:, 0]  # Cytosolic Ca2+

# Extract signature features
features = model.extract_signature_features(t, ca_cyt)
print("\nSignature features:")
for key, value in features.items():
    if value is not None:
        print(f"  {key}: {value:.2f}")
```

### 3. Analyze with Decoders

```python
from src.decoder_model import DecoderPanel

# Create decoder panel (10 CDPKs)
panel = DecoderPanel()

# Analyze signature
responses = panel.analyze_signature(t, ca_cyt)

# Show top 3 responding CDPKs
sorted_cdpks = sorted(responses.items(), 
                     key=lambda x: x[1]['integrated_activation'],
                     reverse=True)

print("\nTop 3 responding CDPKs:")
for name, resp in sorted_cdpks[:3]:
    print(f"  {name}: {resp['integrated_activation']:.1f}")
```

### 4. Calculate Information Metrics

```python
from src.information_theory import SignatureDiscriminability
import numpy as np

# Get features and labels
features = db.get_feature_matrix()
labels = np.array([sig.stimulus for sig in db.signatures])

# Test classification
results = SignatureDiscriminability.classification_accuracy(
    features, labels, classifier='random_forest'
)

print(f"\nClassification accuracy: {results['accuracy_mean']:.3f}")
print(f"Information transmitted: {results['information_bits']:.3f} bits")
```

### 5. Generate Visualizations

```python
from src.visualization import SignaturePlotter

# UMAP projection
SignaturePlotter.plot_umap_projection(
    features, labels,
    output_path='outputs/my_umap.png'
)
print("UMAP saved to outputs/my_umap.png")
```

## Common Tasks

### Add a Custom Signature

```python
from src.signature_database import SignatureDatabase, CalciumSignature

db = SignatureDatabase()

custom_sig = CalciumSignature(
    signature_id="MY_SIG_001",
    species="Arabidopsis",
    cell_type="guard_cell",
    stimulus="drought",
    baseline_ca=100,
    peak_amplitude=900,
    rise_time=20,
    decay_tau=100,
    duration=400
)

db.add_signature(custom_sig)
db.save_to_csv("my_signatures.csv")
```

### Batch Simulations

```bash
# Simulate all stimulus types
for stim in ABA NaCl mechanical_touch flg22 cold_shock H2O2 glutamate; do
    python3 run_simulation.py --stimulus $stim --output outputs/${stim}.csv
done
```

### Custom Analysis Pipeline

```python
# 1. Load data
db = create_example_database()

# 2. Simulate signatures
model = CalciumDynamicsModel()
panel = DecoderPanel()

all_responses = []
for sig in db.signatures:
    t, sol = model.simulate(sig.stimulus, duration=300)
    responses = panel.analyze_signature(t, sol[:, 0])
    all_responses.append(responses)

# 3. Analyze and visualize
# ... your analysis here
```

## Output Files

All outputs are saved to the `outputs/` directory:

- **CSV files**: Time series data
- **PNG files**: Plots and visualizations  
- **JSON files**: Analysis results
- **HTML files**: Comprehensive reports

## Next Steps

1. Read the full README.md for detailed documentation
2. Explore the GUI tabs
3. Modify model parameters for your research
4. Add your own experimental data
5. Develop custom analysis scripts

## Getting Help

- Check README.md for detailed documentation
- Run module help: `python3 src/signature_database.py`
- View example workflows in README.md
- Check the `examples/` directory (when available)

## Tips

1. **Start with GUI**: Easiest way to understand the workflow
2. **Use example data**: Perfect for testing and learning
3. **Check outputs**: All results are saved automatically
4. **Experiment**: Try different stimuli and parameters
5. **Read docstrings**: All functions have detailed documentation

## Common Questions

**Q: Can I use my own data?**  
A: Yes! Create a CSV file with the same format as `data/example_signatures.csv`

**Q: How do I add more CDPKs?**  
A: Use the `CDPKParameters` class to define custom decoders

**Q: Can I run this on HPC?**  
A: Yes! Use the command-line scripts with your job scheduler

**Q: Where are results saved?**  
A: All outputs go to the `outputs/` directory by default

**Q: Can I modify the model?**  
A: Yes! Edit `src/biophysical_model.py` or create custom parameters

## Troubleshooting

**"Module not found" error**:
```bash
pip install -r requirements.txt
```

**GUI won't start**:
```bash
python3 -m tkinter  # Test if tkinter works
```

**UMAP error**:
```bash
pip install umap-learn
```

**Need more help?**  
See README.md or open an issue on GitHub.

---

**Ready to start analyzing Ca²⁺ signatures!** 🔬🌱
