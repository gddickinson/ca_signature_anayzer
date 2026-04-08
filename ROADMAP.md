# Ca2+ Signature Analyzer -- Roadmap

## Current State
A well-structured toolkit for analyzing plant calcium signaling using information theory and biophysical modeling. Clean `src/` package with six focused modules: `signature_database.py`, `biophysical_model.py`, `decoder_model.py`, `information_theory.py`, `visualization.py`, and `gui_app.py`. Has both GUI (Tkinter) and CLI interfaces (`run_simulation.py`, `analyze_database.py`). Dependencies listed in `requirements.txt`. Test directory exists but likely empty. Supports 7 stimulus types and 10 CDPK decoders.

## Short-term Improvements
- [x] Populate `tests/` with unit tests -- test `CalciumDynamicsModel.simulate()` against known ODE solutions, test `InformationAnalyzer` with synthetic data
- [x] Add input validation to `biophysical_model.py` -- reject negative durations, invalid stimulus types
- [ ] Add progress feedback for long-running simulations in `gui_app.py` (progress bars, cancel button)
- [ ] Validate CSV format on load in `SignatureDatabase` -- handle missing columns gracefully
- [ ] Add type hints to `decoder_model.py` (`CDPKDecoder`, `DecoderPanel`) and `information_theory.py`
- [ ] Add logging throughout `src/` modules instead of print statements

## Feature Enhancements
- [ ] Add parameter sensitivity analysis -- sweep model parameters and visualize effect on signatures
- [ ] Implement stochastic ODE solver option for more realistic noisy signatures
- [ ] Add experimental data import (CSV, Excel) for comparing model predictions with real recordings
- [ ] Support custom stimulus waveforms (arbitrary time series, not just predefined types)
- [ ] Add Bayesian inference for fitting model parameters to experimental data
- [ ] Implement pathway diagrams showing Ca2+ flux between compartments
- [ ] Add export to LaTeX-formatted tables for publication
- [ ] Create interactive Plotly-based visualizations as alternative to static matplotlib

## Long-term Vision
- [ ] Publish as a pip-installable package for the plant biology community
- [ ] Add multi-compartment models (cytosol, ER, vacuole, apoplast, nucleus)
- [ ] Implement spatial calcium wave modeling (1D/2D reaction-diffusion)
- [ ] Build a web application for collaborative signature analysis
- [ ] Integrate with CellML or SBML for model interoperability
- [ ] Add machine learning-based stimulus classification from raw Ca2+ traces

## Technical Debt
- [x] `gui_app.py` in `src/` is likely large -- split into separate tab modules
- [ ] `visualization.py` and `information_theory.py` may have circular import risks through shared data structures
- [ ] The `examples/` and `docs/` directories need content -- currently likely sparse
- [x] `launch_gui.py` at root is a thin wrapper -- consider making `gui_app.py` directly runnable
- [ ] No CI/CD pipeline or linting configuration
- [ ] Module self-tests (mentioned in README) should be converted to proper pytest fixtures
