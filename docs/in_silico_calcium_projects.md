# In Silico Research Projects: Plant Calcium Signaling
## Computational Studies for Publication-Ready Results

---

## PROJECT 1: Genome-Wide Discovery of Candidate Plant InsP₃ and cADPR Receptors Through Convergent Evolution Analysis

### Background and Rationale

The absence of canonical InsP₃ receptors (InsP₃Rs) and ryanodine receptors (RyRs) in plant genomes represents a fundamental paradox: robust functional evidence for InsP₃-induced and cADPR-induced Ca²⁺ release exists, yet no molecular entity has been identified. This suggests plants evolved **convergent solutions**—proteins that perform analogous functions through entirely different structural scaffolds.

Convergent evolution is well-documented in biology: dolphin and shark fins, bird and bat wings, camera eyes in vertebrates and cephalopods. At the molecular level, serine proteases evolved independently in multiple families (trypsin-like, subtilisin-like), all converging on the same catalytic triad mechanism despite different folds. Similarly, plants may have evolved Ca²⁺ channels with InsP₃/cADPR-binding capacity using protein families unrelated to animal receptors.

**Key insight**: Rather than searching for sequence homology (which has failed for 25 years), we should search for **functional convergence**—proteins with structural features that could plausibly bind InsP₃/cADPR and form Ca²⁺-permeable pores, even if they lack homology to known receptors.

This computational project will systematically identify candidate receptors by integrating:
1. Structural prediction (AlphaFold2/3)
2. Ligand binding pocket detection
3. Transmembrane topology analysis
4. Phylogenetic distribution patterns
5. Expression correlation with known Ca²⁺ signaling components

### Research Objectives

1. **Identify structural features required for InsP₃/cADPR binding** through analysis of animal receptors
2. **Screen plant proteomes** for proteins with convergent structural motifs
3. **Prioritize candidates** using multi-criteria scoring
4. **Generate testable predictions** for experimental validation

### Methodology

#### Phase 1: Defining the "Search Image" for Convergent Receptors

**1.1 Structural Analysis of Animal InsP₃Rs and RyRs**

**Data collection**:
- Download cryo-EM structures: InsP₃R (PDB: 3JAV, 6DLD), RyR1 (PDB: 5T15, 6JI8)
- Extract InsP₃ and cADPR binding domains
- Identify ATP/cAMP binding domain structures (potential evolutionary precursors)

**Binding pocket characterization**:
```python
# Using PyMOL and fpocket
# For each receptor structure:
1. Identify ligand binding residues (within 5Å of InsP3/cADPR)
2. Calculate pocket volume, depth, and hydrophobicity
3. Determine electrostatic potential distribution (for phosphate binding)
4. Extract pharmacophore: positions of key interactions
   - Positive patches for phosphate groups
   - Hydrophobic regions for adenine/ribose
```

**Key features to identify**:
- **InsP₃ binding**: Requires basic/aromatic cluster for 4,5-bisphosphate recognition (e.g., Arg-Lys pairs)
- **cADPR binding**: Requires pocket for cyclic ribose + adenine base (wider, more hydrophobic than InsP₃)
- **Ca²⁺ selectivity**: Acidic residues in pore-lining region (EEEE motif in CaV channels)

**Minimal receptor architecture**:
- Ligand binding domain (LBD): ~150-200 aa, can be N-terminal, C-terminal, or cytoplasmic loop
- Transmembrane domains: 4-6 spanning helices (tetramer would give 16-24 TM)
- Pore region: Re-entrant loop or TM helix with selectivity filter

**1.2 Comparative Structural Motif Analysis**

Screen for **structural motifs that could perform similar chemistry**:
- **Nucleotide-binding domains**: P-loop NTPases, PBP (periplasmic binding protein) folds, Rossmann folds
- **Inositol phosphate binding**: PH domains, FYVE domains, PX domains
- **Cation channels**: TRP-like, P2X-like, CNG-like (even though plants lack these, structural principles may be reused)

Create HMM (Hidden Markov Model) profiles for each domain type.

#### Phase 2: Plant Proteome Screening

**2.1 Candidate Gene Identification**

**Species selection**: 
- Arabidopsis thaliana (reference)
- Oryza sativa (monocot)
- Solanum lycopersicum (eudicot, solanaceae)
- Physcomitrella patens (moss, early land plant)
- Chlamydomonas reinhardtii (green alga, has canonical InsP₃R!)
- Cyanidioschyzon merolae (red alga)

**Filtering pipeline**:
```bash
# Step 1: Extract all genes encoding transmembrane proteins (≥2 TMDs)
tmhmm arabidopsis_proteome.faa > tmproteins.txt
# Yields ~8,000 proteins in Arabidopsis

# Step 2: Filter for predicted tonoplast/ER localization
TargetP 2.0 -> Keep "secretory pathway" predictions
# Reduces to ~3,000 proteins

# Step 3: Screen for potential ligand binding domains
hmmsearch --tblout results.txt nucleotide_binding_HMMs.hmm proteome.faa
hmmsearch --tblout results.txt inositol_binding_HMMs.hmm proteome.faa
# Identifies ~500 candidates
```

**2.2 AlphaFold2 Structure Prediction**

For all 500 candidates across 6 species (3,000 proteins total):
```python
# Use AlphaFold2 via ColabFold for batch prediction
# For each protein:
1. Generate structure with 5 models
2. Select highest pLDDT model
3. Predict multimers (dimers, tetramers) using AlphaFold-Multimer
   - Hypothesis: Functional channel may require oligomerization
```

**Quality filtering**:
- Retain only structures with pLDDT >70 in TM regions
- Verify membrane topology consistency with TMHMM predictions

**2.3 Binding Pocket Detection and Characterization**

```python
# For each predicted structure:
# Use fpocket 4.0 and P2Rank

# Score pockets for InsP3-binding potential:
def score_insp3_pocket(pocket):
    score = 0
    # 1. Sufficient volume (>200 Å³)
    if pocket.volume > 200: score += 2
    # 2. Positive electrostatic potential (for phosphates)
    if pocket.charge > +2: score += 3
    # 3. Presence of Arg/Lys within pocket
    basic_residues = count_residues(pocket, ['ARG','LYS'])
    score += min(basic_residues, 4)
    # 4. Aromatic residues (for inositol ring)
    aromatic = count_residues(pocket, ['PHE','TRP','TYR'])
    score += min(aromatic, 2)
    # 5. Accessibility from cytoplasm (not buried in membrane)
    if pocket.z_position > 15: score += 2
    return score

# Score pockets for cADPR-binding potential:
def score_cadpr_pocket(pocket):
    score = 0
    # Larger volume needed (cyclic structure)
    if pocket.volume > 300: score += 2
    # Less charge requirement (only pyrophosphate)
    if pocket.charge > 0: score += 2
    # Hydrophobic character for adenine
    hydrophobic = count_residues(pocket, ['ALA','VAL','LEU','ILE','PHE','TRP'])
    score += min(hydrophobic, 3)
    # H-bond donors for ribose hydroxyls
    hbond_donors = count_residues(pocket, ['SER','THR','ASN','GLN','HIS'])
    score += min(hbond_donors, 3)
    return score
```

**2.4 Docking Simulations**

For top 100 candidates (highest pocket scores):
```python
# Use AutoDock Vina or GNINA (CNN-based scoring)
# Prepare ligands:
ligands = ['InsP3', 'InsP4', 'cADPR', '8-Br-cADPR', 'NAADP']

# For each candidate protein:
for protein in top_candidates:
    for ligand in ligands:
        # Flexible docking
        results = dock(protein, ligand, 
                       exhaustiveness=32,
                       num_modes=20)
        # Score binding:
        if results.affinity < -7.0:  # kcal/mol
            candidate.priority = "HIGH"
```

**Specificity analysis**: 
- Does candidate bind InsP₃ but NOT InsP₄? (Critical specificity test)
- Does it bind cADPR but NOT NAD⁺? 
- Antagonist blocking: Does 8-NH₂-cADPR compete with cADPR?

#### Phase 3: Multi-Criteria Candidate Prioritization

**3.1 Phylogenetic Distribution Analysis**

```python
# For each candidate gene family:
# Build phylogenetic tree across plant species
# Key patterns to identify:

# Pattern 1: "Chlamydomonas Loss Pattern"
# Present in algae (where canonical InsP3R exists)
# Lost in land plants (when InsP3R was lost)
# Re-expanded in angiosperms
# -> Interpretation: Compensatory expansion to replace lost InsP3R

# Pattern 2: "Land Plant Innovation"
# Absent in algae
# Appeared in bryophytes
# Conserved in all land plants
# -> Interpretation: Novel solution evolved early in land plant evolution

# Pattern 3: "Angiosperm Specific"
# Absent in mosses/ferns
# Present only in flowering plants
# -> Interpretation: Recent innovation
```

**3.2 Expression Correlation Analysis**

Using public RNA-seq databases (EMBL-EBI Expression Atlas, GENEVESTIGATOR):

```python
# For each candidate:
# Extract expression across 1000+ conditions in Arabidopsis
# Calculate Pearson correlation with known Ca2+ signaling components:

reference_genes = [
    'TPC1',      # Vacuolar channel
    'CNGC2',     # Plasma membrane channel
    'CPK5',      # Ca2+ decoder
    'CPK6',      # Ca2+ decoder
    'CBL1',      # Ca2+ sensor
    'ACA8',      # Ca2+ pump
    'AtPLC2',    # InsP3 synthesis
]

# High positive correlation (r > 0.6) suggests functional relationship
# Co-expression in same stimuli (ABA, pathogens) supports role
```

**3.3 Subcellular Localization Prediction**

```python
# Combine multiple predictors:
predictors = {
    'DeepLoc2': deep_learning_based,
    'TargetP': signal_peptide_based,
    'Localizer': SVM_based,
    'YLoc': Bayesian_network
}

# Consensus prediction:
# For InsP3 receptor candidates: Require tonoplast/ER prediction
# For cADPR receptor candidates: Require vacuolar prediction
```

**3.4 Structural Similarity to Ion Channels**

```python
# Use Dali server or TM-align
# Compare candidate structures to known plant channels:
templates = [
    'TPC1_structure.pdb',     # Vacuolar SV channel
    'KAT1_structure.pdb',     # Shaker K+ channel
    'GLR3.4_model.pdb',       # Glutamate receptor
]

# High TM-score (>0.5) in TM region suggests channel architecture
```

**3.5 Integration: Multi-Criteria Scoring**

```python
def calculate_priority_score(candidate):
    score = 0
    
    # Structural features (max 30 points)
    score += candidate.pocket_score_InsP3  # 0-13 points
    score += candidate.pocket_score_cADPR  # 0-12 points
    score += candidate.docking_affinity / -1  # 7-10 points if < -7 kcal/mol
    
    # Evolutionary (max 20 points)
    if candidate.phylo_pattern == "Chlamy_loss": score += 10
    elif candidate.phylo_pattern == "Land_plant_innovation": score += 8
    score += candidate.copy_number_variation * 2  # Gene family expansion
    
    # Expression (max 20 points)
    score += min(candidate.correlation_with_Ca_genes * 20, 10)
    score += candidate.coexpression_stimulus_overlap * 10  # ABA/pathogen
    
    # Localization (max 15 points)
    if candidate.predicted_localization == "tonoplast": score += 10
    elif candidate.predicted_localization == "ER": score += 8
    if candidate.has_ER_retention_signal: score += 5
    
    # Structural topology (max 15 points)
    if candidate.TM_domains in range(4,8): score += 5
    if candidate.has_pore_loop: score += 5
    if candidate.TM_similarity_to_channels > 0.5: score += 5
    
    return score

# Rank all candidates
# Score >60/100 = "High priority for experimental testing"
# Score 40-60 = "Medium priority"
# Score <40 = "Low priority"
```

#### Phase 4: Detailed Characterization of Top Candidates

For the top 20 candidates (highest scores):

**4.1 Molecular Dynamics Simulations**

```python
# Embed predicted structure in lipid bilayer
# Using GROMACS with CHARMM36m forcefield

# Simulation protocol:
1. Build membrane system (POPC:POPE 3:1 for PM, POPC:POPI 2:1 for tonoplast)
2. Solvate with 150 mM KCl
3. Energy minimization
4. NVT equilibration (100 ps)
5. NPT equilibration (1 ns)
6. Production MD (100 ns × 3 replicates)

# Analyses:
- Verify stable membrane insertion
- Monitor pocket stability (RMSD of binding site residues)
- Calculate electrostatic potential along pore axis
- Identify potential Ca2+ binding sites (using DensityMap)
```

**4.2 Electrostatic Analysis for Ca²⁺ Permeation**

```python
# Using APBS (Adaptive Poisson-Boltzmann Solver)
# For each candidate with stable pore:

# Calculate electrostatic potential along pore axis
# Compare to known Ca2+ channels (CaV, TPC1)

# Metrics:
# 1. Central barrier height (should be <2 kBT for permeation)
# 2. Presence of negative electrostatic well (Ca2+ binding site)
# 3. Asymmetry of potential (directional flux)
```

**4.3 Ligand Binding Free Energy Calculations**

```python
# For top 10 candidates
# Using MM-PBSA or FEP (Free Energy Perturbation)

# Calculate ΔG_binding for:
# - InsP3
# - InsP4 (specificity control)
# - cADPR  
# - 8-NH2-cADPR (antagonist)

# Predictions:
# True receptor should show:
# ΔG(InsP3) < -7 kcal/mol
# ΔG(InsP4) > ΔG(InsP3) + 2 kcal/mol (specificity)
# ΔG(antagonist) competitive with agonist
```

**4.4 Functional Domain Architecture Prediction**

```python
# Using InterPro, Pfam, and AI-based domain prediction (ProteinCartography)

# For each candidate, identify:
# 1. Predicted regulatory domains (C-terminal, N-terminal)
# 2. Potential phosphorylation sites (kinase motifs)
# 3. Protein interaction motifs (PDZ, SH3, etc.)
# 4. Ca2+-binding EF hands (could provide Ca2+-induced Ca2+ release)

# Compare domain architecture between candidates and animal receptors
# Identify convergent regulatory mechanisms
```

#### Phase 5: Network Integration and Systems-Level Analysis

**5.1 Protein-Protein Interaction Prediction**

```python
# Using AlphaFold-Multimer
# Test interactions between top candidates and known Ca2+ signaling proteins:

interaction_partners = [
    'Calmodulin',
    'CPK5', 'CPK6',  # May directly regulate
    'TPC1',          # May form complexes
    'V-ATPase subunits',  # Co-localize at tonoplast
]

# Predict heteromeric complexes
# Score interface quality (pDockQ score)
# Hypothesis: True receptor may require accessory subunits
```

**5.2 Genetic Interaction Network Analysis**

```python
# Mine Arabidopsis genetic interaction databases:
# - AraNet v3 (functional gene networks)
# - STRING (protein-protein interaction predictions)

# For each candidate:
# 1. Extract predicted interaction partners
# 2. Check for enrichment of Ca2+ signaling genes
# 3. Identify shared synthetic lethal partners with known channels

# Statistical test:
# Hypergeometric test for enrichment of Gene Ontology term "calcium ion transport"
```

**5.3 Evolutionary Rate Analysis**

```python
# Calculate dN/dS ratios across plant phylogeny
# Using codeml (PAML package)

# Hypothesis: True receptor under strong purifying selection
# dN/dS << 1 indicates functional constraint

# Test for positive selection in specific lineages
# (might indicate adaptation to novel ligands/regulation)
```

### Expected Outcomes and Deliverables

**Primary Deliverable**: Ranked list of 20-50 high-confidence candidate InsP₃/cADPR receptors with:
- Predicted 3D structures
- Ligand binding predictions (affinities, poses)
- Phylogenetic distribution patterns
- Expression correlation profiles
- Testable experimental predictions

**Publication Structure**:

**Title**: "Computational Discovery of Candidate InsP₃ and cADPR Receptors in Plants Through Convergent Evolution Analysis"

**Main Figures**:
1. **Overview figure**: Animal receptor structures → extracted functional features → plant proteome screen workflow
2. **Candidate structures**: AlphaFold2 models of top 5 candidates with predicted ligand binding poses
3. **Phylogenetic distribution**: Presence/absence heatmap across plant species, expansion/contraction analysis
4. **Multi-criteria scoring**: Scatter plots showing pocket scores, docking affinities, expression correlations
5. **Predicted mechanisms**: Comparison of candidate channel architectures to known channels
6. **Validation roadmap**: Experimental tests to discriminate between candidates

**Supplementary Data**:
- Full ranked list of all candidates (Excel file)
- AlphaFold2 structures deposited to ModelArchive
- Binding site residues and pharmacophore models
- Expression correlation matrices
- Docking poses (PDB format)
- Python/R scripts for reproducibility

**Impact Metrics**:
- **Scientific impact**: Provides first systematic computational search for plant InsP₃/cADPR receptors
- **Experimental utility**: Reduces search space from ~30,000 genes to ~20 high-priority candidates
- **Cost savings**: Computational screening ($5K compute time) vs. experimental screening ($500K+ for genome-wide CRISPR)
- **Field advancement**: If even one candidate validates, resolves 35-year mystery

### Technical Requirements

**Computational Resources**:
- AlphaFold2 batch predictions: ~3,000 CPU-hours (Google Colab Pro or local GPU cluster)
- Molecular dynamics: ~50,000 CPU-hours (HPC cluster, or 500 GPU-hours)
- Docking simulations: ~1,000 CPU-hours
- **Total estimated cost**: $2,000-5,000 (cloud computing) or free (university HPC access)

**Software (all open-source)**:
- AlphaFold2, ColabFold
- PyMOL, VMD (visualization)
- fpocket, P2Rank (binding site detection)
- AutoDock Vina, GNINA (docking)
- GROMACS (molecular dynamics)
- APBS (electrostatics)
- BLAST, HMMER (sequence analysis)
- RAxML, IQ-TREE (phylogenetics)

**Data Sources (all public)**:
- Phytozome (plant genomes)
- Protein Data Bank (structures)
- EMBL-EBI Expression Atlas (RNA-seq)
- AraNet, STRING (networks)

**Timeline**: 6-9 months for complete analysis

### Novelty and Significance

**Methodological Innovation**:
- First application of convergent evolution principles to plant Ca²⁺ signaling
- Integration of structure prediction, ligand docking, and phylogenomics
- Establishes generalizable framework for finding "missing" plant proteins

**Biological Insight**:
- Tests hypothesis that plants evolved novel Ca²⁺ channel families
- Provides evolutionary perspective on plant signaling innovation
- May reveal whether different plant lineages solved problem independently

**Practical Impact**:
- Enables targeted experimental validation (vs. fishing expeditions)
- Predictions immediately testable with CRISPR and patch-clamp
- Success would transform plant Ca²⁺ signaling field

---

## PROJECT 2: Quantitative Modeling of Plant Ca²⁺ Signature Decoding and Information Transmission

### Background and Rationale

A fundamental question in cell signaling is how temporal patterns ("signatures") of second messengers encode stimulus-specific information. In Ca²⁺ signaling, different stimuli produce distinct patterns—single spikes, oscillations, sustained plateaus—that somehow specify different cellular responses. This "Ca²⁺ code" has been extensively studied in animals but remains poorly understood in plants.

Plants face a unique challenge: they achieve complex Ca²⁺ signaling with a **dramatically simplified toolkit** compared to animals. Animals have hundreds of channel types (voltage-gated, TRP, store-operated, glutamate, purinergic), while plants have ~60 channels across just a few families (GLRs, CNGCs, MCAs, Annexins). How do plants achieve equivalent signaling specificity with fewer components?

**Three competing hypotheses**:
1. **Reduced specificity**: Plants don't actually need as much information transmission
2. **Decoder multiplexing**: Expanded decoder families (34 CDPKs vs. 7 mammalian CaMKs) provide discrimination
3. **Enhanced temporal coding**: Plants use more sophisticated frequency/amplitude modulation

This project will use **computational modeling** and **information theory** to quantitatively assess these hypotheses and determine the **information-carrying capacity** of plant Ca²⁺ signatures.

### Research Objectives

1. **Construct biophysical models** of plant Ca²⁺ signature generation and decoding
2. **Calculate information transmission** from stimulus → Ca²⁺ signature → cellular output
3. **Compare plant vs. animal Ca²⁺ signaling capacity**
4. **Generate experimentally testable predictions** about signature discrimination

### Methodology

#### Phase 1: Compilation of Experimental Ca²⁺ Signature Database

**1.1 Literature Mining**

Systematically extract Ca²⁺ signature data from literature:
```python
# Search PubMed for plant Ca2+ imaging papers (2000-2025)
# Extract from papers:
# - Stimulus type
# - Cell type
# - Ca2+ reporter used
# - Signature features: amplitude, duration, frequency, latency

# Compile database structure:
signature_db = {
    'paper_ID': 'PMID_12345678',
    'species': 'Arabidopsis thaliana',
    'cell_type': 'guard_cell',
    'stimulus': 'ABA',
    'concentration': '10 uM',
    'baseline_Ca': '100 nM',
    'peak_amplitude': '800 nM',
    'rise_time': '15 s',
    'decay_time': '120 s',
    'oscillation_frequency': 'None',
    'duration': '600 s',
}
```

**Target signatures** (from literature):
- ABA-induced oscillations in guard cells (0.3-1 Hz)
- Pathogen-induced biphasic Ca²⁺ elevations
- NaCl-induced sustained plateau
- Mechanical touch-induced rapid spike
- Glutamate-induced long-distance waves
- Cold shock transients
- H₂O₂-induced oscillations

**Expected database size**: 200-300 distinct signatures across 20+ stimuli and 10+ cell types

**1.2 Signature Parameterization**

Define quantitative signature descriptors:
```python
class CalciumSignature:
    # Amplitude features
    peak_amplitude: float  # max [Ca2+] in nM
    baseline: float        # resting [Ca2+]
    fold_change: float     # peak/baseline
    
    # Temporal features  
    rise_time: float       # 10-90% rise time
    decay_tau: float       # exponential decay time constant
    duration: float        # time above half-max
    latency: float         # stimulus to response onset
    
    # Oscillation features
    frequency: float       # Hz (if oscillatory)
    duty_cycle: float      # fraction of time elevated
    spike_amplitude_CV: float  # variability between spikes
    
    # Spatial features (if available)
    wave_velocity: float   # μm/s
    spatial_range: float   # μm propagation distance
    
    # Statistical features
    noise_level: float     # std of baseline
    SNR: float            # signal/noise ratio
```

**1.3 Dimensionality Reduction and Clustering**

```python
# Use UMAP or t-SNE to visualize signature space
from umap import UMAP

# Features matrix: [n_signatures × n_features]
X = signature_database.to_numpy()

# Dimensionality reduction
embedding = UMAP(n_components=2, min_dist=0.1).fit_transform(X)

# Hierarchical clustering
from scipy.cluster.hierarchy import linkage, fcluster
Z = linkage(X, method='ward')
clusters = fcluster(Z, t=10, criterion='maxclust')

# Question: Do signatures cluster by stimulus type?
# If yes → signatures are discriminable
# If no → multiple stimuli produce similar signatures
```

#### Phase 2: Biophysical Modeling of Ca²⁺ Dynamics

**2.1 Single-Cell Ca²⁺ Dynamics Model**

Build ordinary differential equation (ODE) model of Ca²⁺ fluxes:

```python
# Modified from Dupont & Goldbeter (1993), adapted for plants

def calcium_dynamics(t, y, params, stimulus):
    Ca_cyt, Ca_ER, Ca_vac, IP3 = y
    
    # Ca2+ influx from apoplast (PM channels)
    J_PM_in = (params['GLR_activity'](stimulus, t) * 
               params['CNGC_activity'](stimulus, t))
    
    # Ca2+ release from ER (InsP3-induced)
    J_ER_release = (params['V_ER'] * IP3**params['n_IP3'] / 
                    (params['K_IP3']**params['n_IP3'] + IP3**params['n_IP3']) *
                    Ca_ER)
    
    # Ca2+ release from vacuole (NAADP, cADPR, voltage)
    J_vac_release = (params['V_vac'] * 
                     (1 / (1 + params['K_vac']/Ca_vac)))
    
    # Ca2+ pumps (ACA, ECA)
    J_PM_pump = params['V_pm_pump'] * Ca_cyt**2 / (params['K_pump']**2 + Ca_cyt**2)
    J_ER_pump = params['V_er_pump'] * Ca_cyt**2 / (params['K_pump']**2 + Ca_cyt**2)
    J_vac_pump = params['V_vac_pump'] * Ca_cyt**2 / (params['K_pump']**2 + Ca_cyt**2)
    
    # IP3 synthesis and degradation
    J_IP3_synth = params['PLC_activity'](stimulus, t)
    J_IP3_deg = params['k_IP3_deg'] * IP3
    
    # ODEs
    dCa_cyt = (J_PM_in + J_ER_release + J_vac_release - 
               J_PM_pump - J_ER_pump - J_vac_pump)
    dCa_ER = J_ER_pump - J_ER_release
    dCa_vac = J_vac_pump - J_vac_release
    dIP3 = J_IP3_synth - J_IP3_deg
    
    return [dCa_cyt, dCa_ER, dCa_vac, dIP3]
```

**Parameter estimation**:
- Fit to experimental signatures from database
- Use Latin Hypercube Sampling for parameter space exploration
- Bayesian inference (PyMC3) for uncertainty quantification

**Model outputs**: 
- Can model reproduce experimental signatures?
- What parameter combinations generate oscillations vs. spikes vs. plateaus?

**2.2 Ca²⁺ Decoder Models**

Model CDPK activation as function of Ca²⁺:
```python
def CDPK_activation(Ca, params):
    # Cooperative Ca2+ binding to EF hands (Hill equation)
    # Different CDPKs have different affinities
    
    K_d = params['K_d']      # Ca2+ dissociation constant (100 nM - 10 μM)
    n_Hill = params['n']      # Cooperativity (typically 2-4)
    k_on = params['k_on']     # Activation rate
    k_off = params['k_off']   # Deactivation rate
    
    # Fraction of activated CDPK
    f_active = Ca**n_Hill / (K_d**n_Hill + Ca**n_Hill)
    
    return f_active

# Model all 34 Arabidopsis CDPKs
CDPK_params = {
    'CPK1': {'K_d': 200e-9, 'n': 3.2, 'k_on': 1e8, 'k_off': 100},
    'CPK2': {'K_d': 150e-9, 'n': 2.8, 'k_on': 5e7, 'k_off': 80},
    # ... (obtain from literature or estimate from EF-hand sequences)
    'CPK34': {'K_d': 5e-6, 'n': 2.0, 'k_on': 1e7, 'k_off': 500},
}
```

**Temporal filtering**:
```python
def decoder_with_kinetics(Ca_timeseries, CDPK_params):
    # ODEs for CDPK activation/inactivation
    # Allows frequency decoding through kinetic filtering
    
    CDPK_active = np.zeros_like(Ca_timeseries)
    
    for i in range(1, len(Ca_timeseries)):
        dt = t[i] - t[i-1]
        Ca = Ca_timeseries[i]
        
        # Activation
        d_activation = (CDPK_params['k_on'] * Ca * (1 - CDPK_active[i-1]) -
                        CDPK_params['k_off'] * CDPK_active[i-1])
        
        CDPK_active[i] = CDPK_active[i-1] + d_activation * dt
        
    return CDPK_active

# Key insight: Different k_on/k_off allows different CDPKs 
# to respond to different frequency signatures
```

**2.3 Downstream Target Phosphorylation**

Model transcription factor phosphorylation:
```python
def target_phosphorylation(CDPK_active, phosphatase_activity):
    # Phosphorylation-dephosphorylation cycle
    # Creates additional temporal filtering
    
    k_phos = CDPK_active * params['k_cat']
    k_dephos = phosphatase_activity
    
    # Steady-state phosphorylation
    P_fraction = k_phos / (k_phos + k_dephos)
    
    return P_fraction

# Multiple phosphorylation sites create ultrasensitivity
# (Goldbeter-Koshland switch)
```

#### Phase 3: Information Theory Analysis

**3.1 Calculate Channel Capacity**

Information theory quantifies how much information flows from input (stimulus) to output (cellular response) through the Ca²⁺ signaling system.

```python
# Calculate mutual information I(Stimulus; Output)

# For discrete stimuli and outputs:
def mutual_information(stimuli, outputs):
    """
    stimuli: array of stimulus IDs [N_trials]
    outputs: array of output IDs [N_trials]
    """
    # Calculate p(stimulus), p(output), p(stimulus, output)
    p_s = np.bincount(stimuli) / len(stimuli)
    p_o = np.bincount(outputs) / len(outputs)
    p_so = np.histogram2d(stimuli, outputs)[0] / len(stimuli)
    
    # Mutual information
    MI = 0
    for s in range(len(p_s)):
        for o in range(len(p_o)):
            if p_so[s,o] > 0:
                MI += p_so[s,o] * np.log2(p_so[s,o] / (p_s[s] * p_o[o]))
    
    return MI  # bits

# For continuous variables:
from sklearn.feature_selection import mutual_info_regression
MI_continuous = mutual_info_regression(signatures, output_genes)
```

**3.2 Decompose Information Flow**

```python
# Decompose total information into stages:
# Stimulus → Ca2+ signature → Decoder activation → Target phosphorylation → Gene expression

# Stage 1: Stimulus → Ca2+ signature
I_stimulus_Ca = mutual_information(stimuli, Ca_signatures)

# Stage 2: Ca2+ signature → Decoder activation  
I_Ca_decoder = mutual_information(Ca_signatures, CDPK_activation)

# Stage 3: Decoder → Target phosphorylation
I_decoder_target = mutual_information(CDPK_activation, target_phos)

# Information loss at each stage
loss_stage1 = I_stimulus_Ca
loss_stage2 = I_stimulus_Ca - I_Ca_decoder
loss_stage3 = I_Ca_decoder - I_decoder_target

# Identifies bottleneck in information flow
```

**3.3 Assess Signature Discriminability**

```python
# Question: Can decoders reliably distinguish between different signatures?

# Approach: Train classifier on Ca2+ signatures to predict stimulus

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# Features: signature parameters (amplitude, frequency, etc.)
X = signature_features
y = stimulus_labels

clf = RandomForestClassifier(n_estimators=100)
accuracy = cross_val_score(clf, X, y, cv=5).mean()

# Classification accuracy → information transmission
# 90% accuracy for 10 stimuli → log2(10) × 0.9 = 2.99 bits transmitted
```

**3.4 Decoder Multiplexing Analysis**

```python
# Test hypothesis: Multiple CDPKs with different affinities enable discrimination

# Simulate responses of all 34 CDPKs to each signature
CDPK_response_matrix = np.zeros((34, n_signatures))

for i, signature in enumerate(signatures):
    Ca_trace = simulate_Ca_dynamics(signature)
    for j, CDPK in enumerate(all_CDPKs):
        CDPK_response_matrix[j, i] = integrate_CDPK_activation(Ca_trace, CDPK)

# Cluster analysis: Do different signatures activate different CDPK combinations?
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_projection = pca.fit_transform(CDPK_response_matrix.T)

# If different signatures are well-separated in CDPK activation space
# → Decoder multiplexing provides discrimination
```

#### Phase 4: Comparative Analysis with Animal Ca²⁺ Signaling

**4.1 Compile Animal Ca²⁺ Signature Database**

Extract comparable data from animal studies:
- Hippocampal neuron Ca²⁺ spikes (L-type, NMDA channels)
- T cell Ca²⁺ oscillations (ORAI, store-operated Ca²⁺ entry)
- β-cell Ca²⁺ bursts (voltage-gated Ca²⁺ channels)
- Oocyte Ca²⁺ waves (InsP₃R, RyR)

**4.2 Model Animal Ca²⁺ Decoding**

Build equivalent model with mammalian components:
- CaM (calmodulin) instead of CBL/CML
- CaMKII instead of CDPK
- Calcineurin phosphatase

**4.3 Quantitative Comparison**

```python
# Compare information transmission capacity

metrics = {
    'channel_diversity': len(unique_channels),
    'decoder_diversity': len(unique_decoders),
    'mutual_information': I(stimulus; output),
    'signature_classes': n_distinct_signatures,
    'discrimination_accuracy': classifier_accuracy,
}

# Statistical comparison
plant_metrics = calculate_metrics(plant_data)
animal_metrics = calculate_metrics(animal_data)

# Key questions:
# 1. Do plants transmit less information despite fewer channels?
# 2. Does CDPK expansion compensate for reduced channel diversity?
# 3. Are plant signatures more stereotyped or more diverse?
```

#### Phase 5: Predict Optimal Signature Design

**5.1 In Silico Signature Evolution**

```python
# Genetic algorithm to evolve optimal Ca2+ signatures for discrimination

# Genome: Ca2+ signature parameters [amplitude, frequency, duration, ...]
# Fitness: How well decoders can discriminate this signature from others

class SignatureGenome:
    genes = {
        'peak_amplitude': (100e-9, 5e-6),  # range in M
        'frequency': (0, 2),                # range in Hz
        'duty_cycle': (0.1, 0.9),
        'rise_time': (1, 60),               # seconds
        'duration': (10, 600),
    }
    
def fitness(signature, existing_signatures, decoder_model):
    # Simulate decoder responses
    response_vector = decoder_model.predict(signature)
    
    # Calculate Euclidean distance to existing signatures
    min_distance = min([euclidean(response_vector, 
                        decoder_model.predict(s)) 
                        for s in existing_signatures])
    
    # Fitness = how distinct from other signatures
    return min_distance

# Evolve new signatures
population = initialize_random_signatures(n=100)
for generation in range(1000):
    fitness_scores = [fitness(sig, population) for sig in population]
    selected = select_top(population, fitness_scores, n=50)
    offspring = crossover_and_mutate(selected)
    population = selected + offspring

# Output: What are the theoretical optimal signatures for discrimination?
```

**5.2 Information-Theoretic Constraints**

```python
# Calculate theoretical maximum information transmission

# Shannon-Hartley theorem for continuous signals
# C = W × log2(1 + SNR)
# where C = channel capacity (bits/s)
#       W = bandwidth (Hz)
#       SNR = signal-to-noise ratio

# For Ca2+ signatures:
bandwidth = 1 / (2 * min_rise_time)  # Nyquist limit
SNR = (signal_amplitude - baseline) / noise_std

capacity_max = bandwidth * np.log2(1 + SNR)

# Compare to actual measured information transmission
efficiency = I_measured / capacity_max

# Question: Are plants operating near theoretical limit?
```

### Expected Outcomes and Deliverables

**Primary Findings**:

1. **Quantification of plant Ca²⁺ signature diversity** 
   - Number of statistically distinct signature classes
   - Overlap between signatures from different stimuli

2. **Information transmission capacity**
   - Bits of information transmitted from stimulus → output
   - Comparison to animal systems

3. **Decoder multiplexing contribution**
   - Quantitative assessment of CDPK family expansion benefit
   - Identification of which CDPKs discriminate which signatures

4. **Predictions for experimental testing**
   - Signatures predicted to be discriminable vs. indiscriminable
   - Specific CDPK knockouts that should abolish discrimination
   - Synthetic signatures that should activate specific pathways

**Publication Structure**:

**Title**: "Information-Theoretic Analysis Reveals How Plants Achieve Signaling Specificity with a Simplified Ca²⁺ Toolkit"

**Main Figures**:
1. **Ca²⁺ signature atlas**: UMAP of all experimental signatures, clustered by stimulus type
2. **Biophysical model**: Model schematic + fit to experimental data
3. **Information flow**: Sankey diagram showing I(stimulus; Ca²⁺; decoder; output) with losses
4. **Decoder multiplexing**: Heatmap of CDPK activation across signatures
5. **Plant vs. animal comparison**: Information capacity, channel diversity, decoder diversity
6. **Predictions**: Synthetic signatures and expected outputs

**Supplementary**:
- Full signature database (CSV)
- Model code (Python notebooks)
- Parameter sensitivity analyses
- All information-theoretic calculations

**Impact**:
- **First quantitative framework** for plant Ca²⁺ signaling specificity
- **Resolves debate**: Do plants need fewer channels or use decoders differently?
- **Enables rational design**: Predicts signatures for synthetic biology applications
- **Evolutionary insight**: How did plants compensate for reduced channel diversity?

### Technical Requirements

**Computational Resources**:
- Modest requirements: Standard laptop or desktop
- Simulations parallelize easily (embarrassingly parallel)
- Total compute time: ~500 CPU-hours

**Software**:
- Python (NumPy, SciPy, scikit-learn, PyMC3)
- MATLAB alternative (for ODE solving)
- R (for statistical analyses)
- All open-source, free

**Data**:
- Literature-mined experimental data (manual curation required)
- Public databases: EMBL-EBI Expression Atlas, PlantTFDB

**Timeline**: 4-6 months

### Novelty and Significance

**Conceptual Advance**:
- First application of information theory to plant Ca²⁺ signaling
- Provides quantitative framework (vs. qualitative descriptions)
- Tests fundamental hypothesis about biological information processing

**Practical Applications**:
- Rational design of synthetic Ca²⁺ circuits for optogenetics
- Predicts which signals can be reliably distinguished
- Identifies decoder engineering targets

**Broader Impact**:
- Methodology applicable to other plant signaling systems (hormone, ROS, pH)
- Tests general principles of signaling network evolution
- Provides comparative evolutionary perspective

---

## PROJECT 3: Evolutionary Genomics of Plant Ca²⁺ Signaling Toolkit Across 1000+ Genomes

### Background and Rationale

Plant Ca²⁺ signaling exhibits a puzzling evolutionary pattern: **gain** of novel components (CDPKs, CBL-CIPK) and **loss** of ancestral ones (InsP₃R, RyR, voltage-gated Ca²⁺ channels). Understanding this evolutionary trajectory requires comparative genomic analysis across the plant phylogeny, from algae to flowering plants.

Recent sequencing initiatives provide unprecedented data:
- **1000 Plants Project** (OneKP): 1000+ plant transcriptomes
- **10KP**: 10,000+ plant genome assemblies
- Individual genome projects: 100+ high-quality plant genomes

This dataset enables testing **macro-evolutionary hypotheses**:
1. **When** were InsP₃R/RyR lost? Single event or multiple independent losses?
2. **What** was gained to compensate? Timing of CDPK/CBL-CIPK expansion?
3. **Why** the difference? Correlation with plant ecological/morphological traits?
4. **How** does toolkit complexity scale with organism complexity?

### Research Objectives

1. **Map presence/absence** of all Ca²⁺ signaling components across plant phylogeny
2. **Date evolutionary transitions** (origins, expansions, losses)
3. **Correlate toolkit changes** with plant traits (land colonization, vascularization, multicellularity)
4. **Identify lineage-specific innovations**
5. **Predict functional equivalence** through phylogenetic bracketing

### Methodology

#### Phase 1: Comprehensive Ca²⁺ Signaling Gene Identification

**1.1 Define Complete Gene Inventory**

Compile comprehensive list of Ca²⁺ signaling genes from Arabidopsis:

```python
Ca_signaling_genes = {
    # CHANNELS & TRANSPORTERS
    'GLR': 20,        # Glutamate receptor-like
    'CNGC': 20,       # Cyclic nucleotide-gated channels
    'MCA': 2,         # Mid1-complementing activity (mechanosensitive)
    'OSCA': 15,       # Hyperosmolality-gated calcium-permeable
    'TPC1': 1,        # Two-pore channel
    'Annexin': 8,     # Annexins (putative Ca2+ channels)
    'ACA': 10,        # Autoinhibited Ca2+-ATPase
    'ECA': 4,         # ER-type Ca2+-ATPase
    'CAX': 6,         # Cation/H+ exchangers
    
    # SENSORS & DECODERS
    'CDPK/CPK': 34,   # Calcium-dependent protein kinases
    'CML': 50,        # Calmodulin-like
    'CBL': 10,        # Calcineurin B-like
    'CIPK': 26,       # CBL-interacting protein kinases
    'CaM': 7,         # Calmodulin
    'CCaMK': 1,       # Ca2+/CaM-dependent kinase (legumes/bryophytes)
    
    # SYNTHESIS & METABOLISM
    'PLC': 9,         # Phospholipase C (makes InsP3)
    'ITPK': 4,        # Inositol polyphosphate kinases
    'VIH': 2,         # InsP8 synthesis
    'TIR': ~150,      # TIR domain NADases (make cADPR variants)
}

# Total: ~370 genes
```

**1.2 Sequence Database Construction**

```bash
# For each gene family, extract Arabidopsis sequences
# Use as queries for homolog search

# Example for GLRs:
# 1. Download Arabidopsis GLR protein sequences from TAIR
cat AtGLR*.faa > Arabidopsis_GLRs.faa

# 2. Create HMM profile
mafft --auto Arabidopsis_GLRs.faa > GLR_alignment.faa
hmmbuild GLR_profile.hmm GLR_alignment.faa
```

#### Phase 2: Genome-Wide Homolog Search Across Plant Phylogeny

**2.1 Species Selection Strategy**

Strategically sample across plant phylogeny:

```python
species_selection = {
    # ALGAE (outgroups)
    'Chlorophyta': [
        'Chlamydomonas reinhardtii',     # Model green alga - HAS InsP3R!
        'Volvox carteri',                 # Multicellular colonial
        'Ostreococcus tauri',            # Minimal genome
    ],
    'Rhodophyta': [
        'Cyanidioschyzon merolae',       # Red alga
        'Galdieria sulphuraria',
    ],
    
    # BASAL LAND PLANTS
    'Bryophytes': [
        'Physcomitrella patens',          # Model moss
        'Marchantia polymorpha',          # Liverwort
        'Sphagnum fallax',               # Peat moss
    ],
    
    # VASCULAR PLANTS
    'Lycophytes': [
        'Selaginella moellendorffii',    # Spike moss
    ],
    'Ferns': [
        'Azolla filiculoides',           # Water fern
        'Salvinia cucullata',
    ],
    'Gymnosperms': [
        'Picea abies',                   # Norway spruce
        'Pinus taeda',                   # Loblolly pine
        'Ginkgo biloba',
    ],
    
    # ANGIOSPERMS
    'Basal_angiosperms': [
        'Amborella trichopoda',          # Sister to all angiosperms
    ],
    'Monocots': [
        'Oryza sativa',                  # Rice
        'Zea mays',                      # Maize
        'Triticum aestivum',             # Wheat
        'Brachypodium distachyon',
        'Spirodela polyrhiza',           # Duckweed
    ],
    'Eudicots': [
        'Arabidopsis thaliana',          # Model reference
        'Solanum lycopersicum',          # Tomato
        'Medicago truncatula',           # Legume
        'Populus trichocarpa',           # Poplar
        'Vitis vinifera',                # Grape
        'Eucalyptus grandis',
    ],
}

# Total: 100-200 species spanning 1 billion years of evolution
```

**2.2 Homolog Detection Pipeline**

```bash
#!/bin/bash
# For each species and each gene family

for SPECIES in species_list.txt; do
    for FAMILY in Ca_gene_families.txt; do
        
        # 1. hmmsearch to find candidates
        hmmsearch --tblout ${SPECIES}_${FAMILY}.tbl \
                  --domtblout ${SPECIES}_${FAMILY}_dom.tbl \
                  -E 1e-5 \
                  ${FAMILY}_profile.hmm \
                  ${SPECIES}_proteome.faa
        
        # 2. Extract sequences
        grep -v "^#" ${SPECIES}_${FAMILY}.tbl | \
        awk '{print $1}' | \
        seqtk subseq ${SPECIES}_proteome.faa - > ${SPECIES}_${FAMILY}_candidates.faa
        
        # 3. Reciprocal BLAST back to Arabidopsis
        blastp -query ${SPECIES}_${FAMILY}_candidates.faa \
               -db Arabidopsis_proteome \
               -out ${SPECIES}_${FAMILY}_reciprocal.txt \
               -outfmt 6 \
               -max_target_seqs 1
        
        # 4. Keep only reciprocal best hits
        # Filter: ≥30% identity, ≥50% coverage
        python filter_rbh.py ${SPECIES}_${FAMILY}_reciprocal.txt \
                             --identity 30 \
                             --coverage 50
    done
done
```

**2.3 Phylogenetic Classification**

```python
# For each gene family, build phylogenetic tree
# Ensure sequences cluster correctly

# Example workflow for GLRs:
# 1. All GLR sequences from all species → MAFFT alignment
# 2. TrimAl to remove poorly aligned regions
# 3. IQ-TREE for maximum likelihood phylogeny
# 4. Classify into GLR subfamilies (GLR1, GLR2, GLR3)

from Bio import Phylo
from ete3 import Tree

# Parse tree
tree = Tree("GLR_phylogeny.nwk")

# Root with algal sequences
algal_GLRs = tree.get_leaves_by_name("Chlre_GLR*")
tree.set_outgroup(algal_GLRs[0])

# Identify orthogroups using TreeFam/OrthoFinder
orthogroups = identify_orthogroups(tree)

# For each species, count members in each orthogroup
GLR_counts = {}
for species in all_species:
    GLR_counts[species] = {
        'GLR1_subfamily': count_in_clade(species, 'GLR1'),
        'GLR2_subfamily': count_in_clade(species, 'GLR2'),
        'GLR3_subfamily': count_in_clade(species, 'GLR3'),
    }
```

#### Phase 3: Evolutionary Pattern Analysis

**3.1 Presence/Absence Matrix Construction**

```python
# Binary matrix: [species × gene families]
# 0 = absent, 1+ = present (with copy number)

import pandas as pd
import numpy as np

# Initialize matrix
species_list = [list of 200 species]
gene_families = [list of 50 gene families]

presence_matrix = pd.DataFrame(
    np.zeros((len(species_list), len(gene_families))),
    index=species_list,
    columns=gene_families
)

# Fill in counts
for species in species_list:
    for family in gene_families:
        presence_matrix.loc[species, family] = count_homologs(species, family)

# Convert to presence/absence
pa_matrix = (presence_matrix > 0).astype(int)
```

**3.2 Detection of Gene Gains and Losses**

```python
# Use Maximum Parsimony or Maximum Likelihood
# to infer gene gain/loss events on phylogeny

from ete3 import Tree
import scipy.stats

# Load species phylogeny
species_tree = Tree("plant_species_tree.nwk")

# For each gene family, reconstruct ancestral states
def infer_ancestral_states(pa_vector, tree):
    """
    pa_vector: presence/absence for extant species
    tree: species phylogenetic tree
    Returns: inferred states for all nodes
    """
    # Fitch parsimony algorithm
    # Or use COUNT software for ML inference with gene birth/death rates
    
    ancestral_states = fitch_algorithm(pa_vector, tree)
    return ancestral_states

# Identify transition events
def detect_transitions(ancestral_states, tree):
    gains = []
    losses = []
    
    for node in tree.traverse():
        if not node.is_leaf():
            parent_state = ancestral_states[node.up]
            child_state = ancestral_states[node]
            
            if parent_state == 0 and child_state == 1:
                gains.append(node.name)
            elif parent_state == 1 and child_state == 0:
                losses.append(node.name)
    
    return gains, losses

# Apply to InsP3R family
InsP3R_states = infer_ancestral_states(pa_matrix['InsP3R'], species_tree)
InsP3R_gains, InsP3R_losses = detect_transitions(InsP3R_states, species_tree)

print(f"InsP3R losses occurred at: {InsP3R_losses}")
# Expected: Loss in ancestor of land plants or early land plants
```

**3.3 Gene Family Expansion/Contraction Analysis**

```python
# CAFE (Computational Analysis of gene Family Evolution)
# Models gene family expansion as birth-death process

# Input: Gene counts + species tree
# Output: Significantly expanded/contracted families at each node

# Example:
# Did CDPKs expand significantly at land plant origin?

from scipy.stats import poisson

def test_expansion(counts_ancestor, counts_descendant, branch_length):
    """
    Likelihood ratio test for significant expansion
    """
    # Null: Constant birth-death rate
    lambda_null = np.mean(counts_descendant) / branch_length
    
    # Alternative: Different rates for this branch
    lambda_alt = counts_descendant / branch_length
    
    # Likelihood ratio
    LR = 2 * (loglik(lambda_alt) - loglik(lambda_null))
    p_value = chi2.sf(LR, df=1)
    
    return p_value < 0.05

# Test CDPK expansion
land_plant_ancestor_CDPKs = 10  # inferred
angiosperm_CDPKs = 34           # observed in Arabidopsis
branch_length = 450  # million years

is_expanded = test_expansion(10, 34, 450)
```

**3.4 Correlation with Plant Traits**

```python
# Test hypotheses linking Ca2+ toolkit to plant biology

# Trait database
trait_data = pd.DataFrame({
    'species': species_list,
    'multicellular': [1,1,1,...],        # binary
    'vascular': [0,0,1,1,...],          # binary
    'genome_size': [125, 450, 135,...], # Mbp
    'cell_types': [5, 8, 15, 40,...],   # estimated number
    'habitat': ['aquatic','terrestrial',...],
})

# Phylogenetic comparative methods
# Control for phylogenetic non-independence

from phylo_comparative import pgls

# Question: Does CDPK number correlate with cell type diversity?
model = pgls(
    formula='CDPK_count ~ cell_types',
    data=combined_data,
    tree=species_tree
)

# Question: Did toolkit complexity increase at land colonization?
land_plants = species_tree.get_common_ancestor(['Physcomitrella','Arabidopsis'])
aquatic_plants = species_tree.get_common_ancestor(['Chlamydomonas','Volvox'])

toolkit_size_land = np.mean([total_genes(sp) for sp in land_plants.get_leaves()])
toolkit_size_aquatic = np.mean([total_genes(sp) for sp in aquatic_plants.get_leaves()])

t_test = scipy.stats.ttest_ind(toolkit_size_land, toolkit_size_aquatic)
```

#### Phase 4: Detailed Analysis of Key Transitions

**4.1 The InsP₃R/RyR Loss Event**

```python
# Precisely date when InsP3R and RyR were lost

# Strategy: Examine basal land plant genomes
basal_species = [
    'Chlamydomonas',    # Alga - HAS InsP3R
    'Marchantia',       # Liverwort
    'Physcomitrella',   # Moss
    'Selaginella',      # Lycophyte
    'Azolla',           # Fern
]

InsP3R_presence = {}
for sp in basal_species:
    # Exhaustive search using:
    # 1. BLAST with animal InsP3R
    # 2. HMM with InsP3R domains
    # 3. Synteny analysis (check if genomic region conserved)
    
    InsP3R_presence[sp] = comprehensive_search(sp, 'InsP3R')

# Hypothesis: Lost in transition from algae → land plants
# Or lost independently in each land plant lineage?
# Distinguishable by phylogenetic pattern
```

**4.2 CDPK Origin and Expansion**

```python
# Reconstruct CDPK phylogeny across all plants

# Key questions:
# 1. Single origin or multiple?
# 2. When did kinase-CaM fusion occur?
# 3. Expansion timing relative to InsP3R loss?

# Build phylogeny
CDPK_tree = build_tree(all_CDPK_sequences)

# Root with outgroup (if exists in animals/fungi?)
# Actually, CDPKs are plant-specific! Need to root with sister group

# Identify expansion events
for node in CDPK_tree.iter_descendants():
    if len(node.get_leaves()) > 10:  # Large clade
        dating = estimate_node_age(node, species_tree)
        print(f"Major CDPK expansion at {dating} Mya")

# Correlation analysis
# Did CDPK expansion occur AFTER InsP3R loss?
# Time series analysis
```

**4.3 CBL-CIPK Network Assembly**

```python
# CBL-CIPK are rare outside land plants
# Trace their origin and co-expansion

# Build CBL and CIPK phylogenies
CBL_tree = build_tree(all_CBL_sequences)
CIPK_tree = build_tree(all_CIPK_sequences)

# Co-phylogeny analysis
# Do CBL and CIPK phylogenies match?
# Suggests co-evolution

from ete3 import TreeStyle
from tanglegram import draw_tanglegram

draw_tanglegram(CBL_tree, CIPK_tree, 
                associations=known_CBL_CIPK_interactions)

# Test: Did CBL and CIPK numbers expand in parallel?
correlation = np.corrcoef(CBL_counts, CIPK_counts)
# High correlation suggests coordinated evolution
```

#### Phase 5: Functional Prediction Through Phylogenetic Bracketing

**5.1 Identify Compensation Mechanisms**

```python
# Hypothesis: New genes appeared to replace lost functions

# For each lost gene (InsP3R, RyR), identify:
# 1. What new genes appeared around the same time?
# 2. Do they have compensatory expression patterns?

# Example:
InsP3R_loss_date = 450  # Mya (estimated)

# Find genes that:
# (a) Originated within ±50 My of InsP3R loss
# (b) Encode transmembrane proteins (potential channels)
# (c) Express in same tissues as InsP3R (in animals)

candidates = []
for gene in all_genes:
    origin_date = estimate_gene_age(gene)
    if abs(origin_date - InsP3R_loss_date) < 50:
        if has_TM_domains(gene):
            if expression_overlap(gene, animal_InsP3R):
                candidates.append(gene)

# These are prime candidates for functional replacement!
```

**5.2 Synteny Analysis**

```python
# Check if genes in same genomic region across species
# Can reveal compensatory evolution

from jcvi.compara.synteny import scan_break points

# Example: Is there a gene in land plants at the syntenic location
# where algae have InsP3R?

Chlamy_InsP3R_locus = 'chromosome_6:1234567-1245678'
Arabidopsis_syntenic_region = find_syntenic_region(
    Chlamy_InsP3R_locus,
    'Chlamydomonas',
    'Arabidopsis'
)

# What genes are there?
genes_in_region = extract_genes(Arabidopsis_syntenic_region)
# Might reveal functionally related genes
```

### Expected Outcomes and Deliverables

**Key Findings**:

1. **Comprehensive gene family catalog**
   - Presence/absence matrix for 50+ Ca²⁺ signaling families across 200 species
   - Copy number variation quantified

2. **Dated evolutionary transitions**
   - Precise timing of InsP₃R/RyR loss
   - CDPK/CBL-CIPK expansion events
   - Correlation with major plant evolutionary transitions

3. **Trait correlations**
   - Does toolkit complexity correlate with organism complexity?
   - Unique innovations in specific lineages (e.g., carnivorous plants, parasites)

4. **Candidate compensatory genes**
   - Genes that emerged to replace lost functions
   - Testable predictions for functional studies

**Publication Structure**:

**Title**: "Evolutionary Trajectory of Plant Ca²⁺ Signaling: Gene Losses, Compensatory Innovations, and Lineage-Specific Adaptations"

**Main Figures**:
1. **Phylogenetic overview**: Species tree with toolkit size, key transitions marked
2. **Presence/absence heatmap**: All gene families across all species
3. **Gene gain/loss events**: Mapped onto phylogeny with statistical support
4. **CDPK expansion analysis**: Copy number evolution through time
5. **Trait correlations**: Toolkit complexity vs. morphological/ecological traits
6. **Synteny analysis**: Genomic context of lost vs. gained genes

**Supplementary**:
- Full gene family alignments and trees
- Detailed orthogroup assignments
- All gene sequences (FASTA files)
- Scripts for reproducibility

**Impact**:
- **First comprehensive evolutionary view** of plant Ca²⁺ signaling
- **Resolves timing** of major transitions
- **Identifies candidate replacement genes** for experimental testing
- **Informs synthetic biology**: Which genes are "core" vs. "accessory"?

### Technical Requirements

**Computational Resources**:
- Phylogenetic analyses: CPU-intensive
- Estimated: 10,000-50,000 CPU-hours (HPC cluster)
- Storage: ~500 GB for all genomes and alignments

**Software** (all open-source):
- BLAST+, HMMER (homology search)
- MAFFT, MUSCLE (alignment)
- TrimAl (alignment trimming)
- IQ-TREE, RAxML (phylogenetics)
- CAFE (gene family evolution)
- OrthoFinder (orthogroup inference)
- COUNT (gain/loss inference)
- R packages: ape, phytools, geiger (phylogenetic comparative methods)

**Data Sources**:
- Phytozome (plant genomes)
- OneKP (plant transcriptomes)
- NCBI (individual genome projects)
- All publicly available

**Timeline**: 6-12 months

### Novelty and Significance

**Scientific Contribution**:
- First genome-scale evolutionary analysis of plant Ca²⁺ signaling
- Establishes timeline for major transitions
- Tests hypotheses about compensation mechanisms

**Practical Applications**:
- Identifies which components are essential (conserved) vs. dispensable
- Guides engineering: Use only conserved components for robust circuits
- Reveals lineage-specific innovations (potential unique biology)

**Broader Impact**:
- General framework for studying signaling evolution in plants
- Comparative perspective valuable for animal Ca²⁺ field
- Educational resource (gene family catalog)

---

## Summary Table: In Silico Project Comparison

| Project | Primary Methods | Compute Requirements | Timeline | Key Deliverable |
|---------|----------------|---------------------|----------|----------------|
| **1: Candidate Receptor Discovery** | AlphaFold2, molecular docking, MD simulations | High (GPU needed) | 6-9 months | Ranked list of 20-50 receptor candidates |
| **2: Information Theory Analysis** | ODE modeling, machine learning, information theory | Low (standard laptop) | 4-6 months | Quantification of signaling capacity |
| **3: Evolutionary Genomics** | Phylogenetics, comparative genomics, synteny | High (HPC cluster) | 6-12 months | Complete evolutionary history of toolkit |

All three projects are:
- **Independently publishable** in high-impact journals
- **Complementary**: Findings from one inform the others
- **Experimentally testable**: Generate concrete predictions
- **Open science**: All data and code can be made public
