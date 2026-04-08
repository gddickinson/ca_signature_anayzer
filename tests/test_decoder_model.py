"""
Tests for src.decoder_model module.

Tests CDPK activation and decoder panel functionality.
"""

import pytest
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from decoder_model import (
    CDPKParameters, CDPKLibrary, CDPKDecoder, DecoderPanel,
    PhosphorylationTarget
)


class TestCDPKParameters:
    """Tests for CDPKParameters dataclass."""

    def test_valid_creation(self):
        params = CDPKParameters(name="test", K_d=100, n_Hill=2, k_on=1e7, k_off=10, k_cat=5)
        assert params.name == "test"

    def test_invalid_kd(self):
        with pytest.raises(AssertionError):
            CDPKParameters(name="bad", K_d=-1, n_Hill=2, k_on=1e7, k_off=10, k_cat=5)


class TestCDPKLibrary:
    """Tests for CDPKLibrary."""

    def test_default_cdpks(self):
        cdpks = CDPKLibrary.get_default_cdpks()
        assert len(cdpks) == 10
        names = [c.name for c in cdpks]
        assert "CPK1" in names
        assert "CPK5" in names


class TestCDPKDecoder:
    """Tests for CDPKDecoder."""

    def test_steady_state_zero_ca(self):
        params = CDPKParameters(name="test", K_d=100, n_Hill=2, k_on=1e7, k_off=10, k_cat=5)
        decoder = CDPKDecoder(params)
        activation = decoder.steady_state_activation(0.0)
        assert activation == pytest.approx(0.0)

    def test_steady_state_high_ca(self):
        params = CDPKParameters(name="test", K_d=100, n_Hill=2, k_on=1e7, k_off=10, k_cat=5)
        decoder = CDPKDecoder(params)
        activation = decoder.steady_state_activation(100000.0)  # Very high Ca
        assert activation == pytest.approx(1.0, abs=0.01)

    def test_steady_state_at_kd(self):
        """At Ca = K_d, activation should be 0.5 for Hill n=1."""
        params = CDPKParameters(name="test", K_d=100, n_Hill=1, k_on=1e7, k_off=10, k_cat=5)
        decoder = CDPKDecoder(params)
        activation = decoder.steady_state_activation(100.0)
        assert activation == pytest.approx(0.5, abs=0.01)

    def test_dynamic_activation_shape(self):
        params = CDPKParameters(name="test", K_d=100, n_Hill=2, k_on=1e7, k_off=10, k_cat=5)
        decoder = CDPKDecoder(params)
        t = np.linspace(0, 10, 100)
        ca = np.full_like(t, 200.0)
        activation = decoder.dynamic_activation(t, ca)
        assert activation.shape == t.shape
        assert np.all(activation >= 0)
        assert np.all(activation <= 1)


class TestDecoderPanel:
    """Tests for DecoderPanel."""

    def test_creation(self):
        panel = DecoderPanel()
        assert len(panel.decoders) == 10

    def test_analyze_signature(self):
        panel = DecoderPanel()
        t = np.linspace(0, 60, 600)
        ca = 100 + 500 * np.exp(-((t - 10)**2) / 20)
        responses = panel.analyze_signature(t, ca)
        assert len(responses) == 10
        for name, resp in responses.items():
            assert "peak_activation" in resp
            assert "integrated_activation" in resp


class TestPhosphorylationTarget:
    """Tests for PhosphorylationTarget."""

    def test_single_site(self):
        target = PhosphorylationTarget(n_sites=1, k_dephos=0.1)
        t = np.linspace(0, 30, 300)
        activation = np.ones_like(t) * 0.8  # Constant high activation
        phos = target.simulate_phosphorylation(t, activation)
        assert phos.shape == t.shape
        assert np.all(phos >= 0)
        assert np.all(phos <= 1)
        # Should reach steady state
        assert phos[-1] > 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
