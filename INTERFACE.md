# Ca2+ Signature Analyzer -- Interface Map

## Package: `src/`

### `biophysical_model.py`
- `ModelParameters` -- ODE model parameters (channel conductances, pump activities, etc.)
- `CalciumDynamicsModel` -- ODE-based Ca2+ dynamics simulation
  - `simulate(stimulus_type, duration, dt, intensity)` -- run simulation (with input validation)
  - `extract_signature_features(t, ca_trace)` -- extract peak, rise time, decay tau, etc.
  - `VALID_STIMULI` -- class-level tuple of accepted stimulus names

### `decoder_model.py`
- `CDPKParameters` -- CDPK kinetic parameters (Kd, Hill coeff, rates)
- `CDPKLibrary` -- default library of 10 Arabidopsis CDPKs
- `CDPKDecoder` -- single CDPK activation model (steady-state + dynamic)
- `DecoderPanel` -- panel of multiple CDPKs; `analyze_signature()`, `get_response_matrix()`
- `PhosphorylationTarget` -- target protein phosphorylation dynamics

### `information_theory.py`
- `InformationAnalyzer` -- MI (discrete/continuous), entropy, channel capacity, signature capacity
- `PathwayInformationFlow` -- information flow between signaling stages
- `SignatureDiscriminability` -- pairwise discrimination, classification accuracy

### `signature_database.py`
- `CalciumSignature` -- single signature record
- `SignatureDatabase` -- collection with load/save CSV, feature matrix, summary stats

### `visualization.py`
- `SignaturePlotter` -- static plotting methods (heatmaps, UMAP, comparisons)
- `IntegratedReport` -- report generation

### `utils.py`
- Utility functions

### GUI (split across 3 files):
- `gui_app.py` -- main GUI class `CaSignatureAnalyzerGUI` (uses mixins), entry point `main()`
- `gui_tabs.py` -- tab construction mixins (Database, Simulation, Decoder, Information, Visualization)
- `gui_callbacks.py` -- callback method mixins for all GUI actions

## Entry Points
- `launch_gui.py` -- launches the GUI
- `run_simulation.py` -- CLI simulation runner
- `analyze_database.py` -- CLI database analysis

## Tests: `tests/`
- `test_biophysical_model.py` -- ODE model and feature extraction tests
- `test_information_theory.py` -- MI, entropy, classification tests
- `test_decoder_model.py` -- CDPK activation and decoder panel tests
