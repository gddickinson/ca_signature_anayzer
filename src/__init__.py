"""
Ca²⁺ Signature Analyzer
========================

A comprehensive toolkit for analyzing plant calcium signaling dynamics
using information theory and biophysical modeling.

Modules:
--------
- signature_database: Manage and analyze Ca²⁺ signature data
- biophysical_model: ODE-based simulation of Ca²⁺ dynamics
- decoder_model: CDPK and other decoder activation models
- information_theory: Calculate mutual information and channel capacity
- visualization: Plotting and visualization tools
- utils: Utility functions and helpers

Author: George (2025)
License: MIT
"""

__version__ = "1.0.0"
__author__ = "George"

from . import signature_database
from . import biophysical_model
from . import decoder_model
from . import information_theory
from . import visualization
from . import utils

__all__ = [
    'signature_database',
    'biophysical_model', 
    'decoder_model',
    'information_theory',
    'visualization',
    'utils'
]
