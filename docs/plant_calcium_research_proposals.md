# Grant Research Proposals: Resolving Critical Questions in Plant Calcium Signaling

---

## PROPOSAL 1: Molecular Identification of the Plant InsP₃-Sensitive Ca²⁺ Release Channel

### Background and Significance

Despite 35 years of functional evidence for InsP₃-induced Ca²⁺ release (IICR) in plants—including electrophysiological recordings showing InsP₃-gated currents across vacuolar membranes and photorelease experiments demonstrating Ca²⁺ transients—no molecular entity responsible for this release has been identified. The absence of canonical InsP₃ receptor (InsP₃R) homologs in all sequenced plant genomes represents one of the most persistent enigmas in plant cell biology. This gap prevents understanding of how plants transduce phospholipase C activation into Ca²⁺ signals and limits biotechnological manipulation of stress responses.

Recent advances provide new opportunities: (1) High-resolution cryo-EM enables structure determination of low-abundance membrane proteins, (2) CRISPR-based genetic screens can systematically interrogate candidate genes, and (3) improved Ca²⁺ imaging with jGCaMP8 sensors enables high-throughput phenotyping of channel mutants.

### Central Hypothesis

Plants utilize a **novel, evolutionarily unrelated protein family** as functional InsP₃ receptors, potentially involving multi-protein complexes that assemble InsP₃-responsive Ca²⁺ conductances from components that individually lack homology to animal InsP₃Rs.

### Specific Aims

**Aim 1**: Identify candidate InsP₃-binding proteins through quantitative chemical proteomics
- Deploy InsP₃ photoaffinity probes with mass spectrometry to identify direct InsP₃-interacting proteins in Arabidopsis vacuolar membrane preparations
- Validate binding specificity through competition assays with InsP₃ analogs and heparin

**Aim 2**: Execute genome-wide CRISPR knockout screen for InsP₃-responsive Ca²⁺ release
- Generate arrayed Arabidopsis mutant library targeting all predicted transmembrane proteins (>3000 genes)
- Screen suspension cell protoplasts loaded with cytosolic jGCaMP8m for loss of InsP₃-induced Ca²⁺ transients
- Focus secondary screens on tonoplast-localized candidates

**Aim 3**: Reconstitute InsP₃-dependent Ca²⁺ conductance in heterologous systems
- Express top candidates in HEK293 cells and Xenopus oocytes
- Perform whole-cell patch-clamp recordings with InsP₃ in the pipette solution
- Test requirement for plant-specific accessory proteins through co-expression

**Aim 4**: Validate physiological function through knockout phenotyping
- Generate CRISPR null alleles in validated candidates
- Assess ABA-induced stomatal closure, pathogen defense responses, and pollen tube guidance
- Complement mutants with wild-type transgenes for rescue validation

### Research Approach and Methodology

#### 1.1 InsP₃ Photoaffinity Labeling and Proteomics

**Probe synthesis**: Synthesize biotinylated photoactivatable InsP₃ analogs with benzophenone crosslinker at the 2-position (retaining 4,5-bisphosphate critical for binding). Validate functional activity by testing Ca²⁺ release from Arabidopsis microsomes.

**Membrane preparation**: Isolate highly enriched vacuolar membranes from 500g Arabidopsis suspension cell culture using sucrose density gradient ultracentrifugation (validated by V-ATPase and TPC1 Western blots). Solubilize in 1% digitonin (preserves protein complexes better than harsh detergents).

**Crosslinking and enrichment**: Incubate membranes (10 mg protein) with 10 µM photoaffinity probe ± 1 mM unlabeled InsP₃ competitor for 30 min on ice. UV crosslink (365 nm, 15 min), quench unreacted probe, and enrich biotinylated proteins on streptavidin beads.

**Mass spectrometry**: Perform on-bead trypsin digestion followed by TMT labeling for quantitative comparison of +/− competitor samples. Analyze by LC-MS/MS (Orbitrap Fusion). Prioritize hits showing >5-fold enrichment in −competitor samples with multiple unique peptides.

**Validation**: Recombinantly express top 10 candidates as GST fusions, perform radioligand binding assays with [³H]InsP₃, determine Kd values, and test competition with heparin and non-bioactive InsP₄ isomers.

#### 1.2 Genome-Wide CRISPR Screen

**Library construction**: Design sgRNA library targeting 3,247 Arabidopsis genes encoding predicted transmembrane proteins (≥2 TMDs by TMHMM algorithm). Include 4 sgRNAs per gene plus 200 non-targeting controls. Clone into pRGEB32 vector with GFP reporter.

**Cell culture transformation**: Transform Arabidopsis PSB-D suspension cells (high transformation efficiency) via Agrobacterium. Select transformed pools with hygromycin, expand to 200 million cells ensuring 1000× library coverage.

**Ca²⁺ imaging screen**: 
- Generate protoplasts, load with jGCaMP8m via electroporation
- Distribute to 384-well plates (1000 cells/well)
- Automated confocal microscopy: baseline imaging → add 10 µM InsP₃ via microfluidics → record for 5 min at 2 Hz
- Classify wells as "hit" if <20% of WT Ca²⁺ response amplitude

**sgRNA identification**: Sort non-responding cells via FACS, extract genomic DNA, amplify sgRNA cassettes, and sequence on Illumina platform. Genes with ≥2 independent sgRNAs enriched in hit pool (>10-fold) advance to validation.

**Validation in stable lines**: Generate individual CRISPR knockouts for top 20 candidates, confirm at protein level, re-test InsP₃ responsiveness in patch-clamp experiments on isolated vacuoles.

#### 1.3 Electrophysiological Reconstitution

**Heterologous expression**: Clone candidates into pcDNA3.1 for mammalian expression with N-terminal FLAG tag. For multi-component hypothesis, co-transfect combinations of 2-3 proteins.

**Whole-cell patch-clamp (HEK293 cells)**:
- Bath: 140 mM NaCl, 5 mM KCl, 2 mM CaCl₂, 10 mM HEPES (pH 7.4)
- Pipette: 140 mM K-gluconate, 5 mM EGTA, 3.6 mM CaCl₂ (100 nM free Ca²⁺), 10 µM InsP₃
- Voltage-clamp at −60 mV, monitor for inward Ca²⁺ currents developing within 2-5 min
- Test InsP₃ dose-dependence (0.01-100 µM), heparin block (50 µg/ml), and Ca²⁺ dependence

**Two-electrode voltage clamp (Xenopus oocytes)**: 
- Inject cRNA (50 ng), incubate 3 days
- Microinject InsP₃ or caged InsP₃ directly into cytoplasm
- UV-uncage and monitor Ca²⁺-activated Cl⁻ currents as surrogate for InsP₃-induced Ca²⁺ release

**Single-channel recordings**: Excise vacuolar patches from protoplasts of candidate overexpression lines, apply InsP₃ to cytoplasmic face, characterize single-channel conductance, gating kinetics, and InsP₃ dose-response.

#### 1.4 In Planta Functional Validation

**CRISPR knockout generation**: Design CRISPR constructs targeting validated candidate(s), confirm homozygous null mutants by sequencing and Western blot.

**Phenotypic characterization**:
- **Stomatal assays**: Measure ABA-induced closure kinetics in epidermal peels with vs. without bath-applied InsP₃. Load guard cells with caged InsP₃, UV-uncage, measure aperture changes.
- **Pathogen immunity**: Challenge with *Pseudomonas syringae* pv. *maculicola*, quantify bacterial growth, measure Ca²⁺ signatures with GCaMP6s in response to flg22 PAMP.
- **Pollen tube guidance**: Cross mutant pollen onto WT pistils, score fertilization success rates, image Ca²⁺ oscillations during pollen tube growth.

**Complementation**: Transform null mutants with genomic candidate driven by native promoter, confirm restoration of InsP₃-induced Ca²⁺ release and rescued phenotypes.

### Expected Outcomes and Impact

**Deliverables**:
1. Molecular identity of plant InsP₃-responsive Ca²⁺ channel
2. Structural model via AlphaFold3 prediction or cryo-EM
3. Mechanistic understanding of InsP₃ gating in the absence of canonical receptor domains
4. Toolkit for engineering InsP₃ sensitivity in crops

**Broader impact**: Resolving this 35-year mystery will fundamentally transform understanding of plant signaling evolution and enable rational engineering of stress-responsive Ca²⁺ signatures in crops.

### Timeline: 4 years
- **Year 1**: Photoaffinity proteomics, CRISPR library construction and primary screen
- **Year 2**: Validation of top candidates, heterologous expression and electrophysiology
- **Year 3**: CRISPR mutant generation and phenotyping
- **Year 4**: Complementation, structural studies, publication

---

## PROPOSAL 2: Identification of the Plant cADPR Receptor and ADP-Ribosyl Cyclase

### Background and Significance

Cyclic ADP-ribose (cADPR) has been established as a Ca²⁺-mobilizing second messenger in plants for 30 years, with particularly well-defined roles in ABA signaling and immune responses. However, two fundamental molecular components remain unidentified: (1) the **cADPR receptor** mediating Ca²⁺ release and (2) the **ADP-ribosyl cyclase** synthesizing cADPR from NAD⁺. 

The recent discovery that plant TIR domains produce variant cADPR isomers (2'cADPR, 3'cADPR) partially addresses synthesis but raises new questions: Are TIR domains the sole source of cADPR for all physiological contexts, or does a canonical cyclase exist for non-immune functions? What protein mediates cADPR-induced Ca²⁺ release from the vacuole given the complete absence of ryanodine receptor (RyR) homologs in plant genomes?

### Central Hypotheses

**H1**: A novel, plant-specific protein family functions as cADPR receptor, possibly involving unique binding pocket architecture convergent with but structurally distinct from animal RyRs.

**H2**: Plants possess a non-TIR, canonical ADP-ribosyl cyclase for housekeeping cADPR production, distinct from immune-activated TIR domain NADases.

### Specific Aims

**Aim 1**: Identify cADPR-binding proteins via quantitative chemical proteomics
- Synthesize biotinylated cADPR affinity probes
- Enrich binding proteins from vacuolar membrane preparations
- Validate with cADPR competition and 8-NH₂-cADPR antagonist

**Aim 2**: Execute forward genetic screen for cADPR-insensitive mutants
- EMS mutagenesis of Arabidopsis line expressing vacuolar-targeted jGCaMP8
- Screen M2 seedlings for loss of cADPR-induced Ca²⁺ transients
- Map causative mutations via whole-genome sequencing

**Aim 3**: Identify ADP-ribosyl cyclase through activity-based protein profiling
- Synthesize mechanism-based NAD⁺ suicide substrate probes
- Enrich cyclase activity from cauliflower microsomes
- Purify to homogeneity via multi-step chromatography

**Aim 4**: Reconstitute cADPR-gated Ca²⁺ conductance and cyclase activity
- Heterologous expression and patch-clamp validation of receptor
- Biochemical characterization of recombinant cyclase

### Research Approach and Methodology

#### 2.1 cADPR Photoaffinity Proteomics

**Probe design**: Synthesize cADPR analogs with benzophenone photocrosslinker attached via linker at the N6-position of adenine (distal from proposed binding pocket) and biotin tag for enrichment. Generate 8-N₃-cADPR analog for competition control.

**Vacuolar membrane preparation**: Isolate tonoplast membranes from 1 kg red beet tap roots (high vacuolar content) using sucrose step gradient. Validate enrichment via V-ATPase activity assays and absence of ER markers (BiP/calreticulin Western blots).

**Crosslinking workflow**:
- Incubate membranes (20 mg) with 5 µM photoaffinity probe ± 500 µM unlabeled cADPR
- UV crosslink (365 nm, 20 min, 4°C)
- Solubilize in 2% digitonin, enrich on streptavidin beads
- Wash extensively, on-bead trypsin digest
- TMT multiplex labeling (6-plex): biological triplicates of +/− competitor
- LC-MS/MS on Orbitrap Eclipse

**Bioinformatic prioritization**: Focus on proteins showing:
- >10-fold enrichment in −competitor samples
- Predicted localization to tonoplast (signal peptide, no ER retention)
- Transmembrane domains (2-20 TMDs)
- No homology to known cADPR-binding proteins

**Validation**: Express top 15 candidates as MBP fusions in *E. coli*, purify, perform [³²P]cADPR binding assays (synthesize [³²P]cADPR from [³²P]NAD⁺ using Aplysia cyclase). Measure Kd, competition by 8-NH₂-cADPR antagonist.

#### 2.2 Forward Genetic Screen

**Transgenic line generation**: Transform Arabidopsis with DEX-inducible vacuolar-targeted jGCaMP8m (fused to AtTIP1;1 tonoplast aquaporin), driven by UBQ10 promoter. Select line with strong, uniform expression.

**EMS mutagenesis**: Treat 50,000 seeds with 0.3% EMS for 10 h, generate M1 plants, harvest M2 seeds (~500,000 individuals, representing ~99% genome saturation for recessive mutations).

**Microscopy screen setup**:
- Germinate M2 seedlings on MS agar in 6-well plates
- At 5-day stage, treat with 10 µM dexamethasone for 6h to induce sensor
- Mount whole seedlings in perfusion chamber on confocal microscope
- Automated imaging (Yokogawa CSU-W1 spinning disk): baseline 30s → perfuse 50 µM 8-Br-cADPR (membrane-permeable analog) → record 5 min
- Screen 2,000 seedlings/week (25 weeks required)

**Hit criteria**: Seedlings showing <25% of WT Ca²⁺ response amplitude. Re-test survivors with InsP₃ and NAADP to confirm specificity.

**Genetic mapping**:
- Cross hit plants to WT (parental line)
- F2 populations (500 plants) screened for recessive segregation
- Pool 50 mutant and 50 WT F2 individuals
- Whole-genome sequencing (Illumina NovaSeq, 30× coverage)
- SNP mapping via SHOREmap or NGM pipelines
- Identify causal mutations in linkage intervals

**Validation**: Test independent alleles via CRISPR knockout, perform allelism tests if multiple hits map to the same gene.

#### 2.3 Activity-Based ADP-Ribosyl Cyclase Profiling

**Mechanism-based probe synthesis**: Design NAD⁺ analog with C2'-fluorine substitution (mechanism-based inhibitor that covalently traps cyclase) and alkyne handle for click chemistry enrichment.

**Cyclase-enriched extract preparation**:
- Homogenize 5 kg cauliflower florets (established to have cyclase activity from thesis work)
- Differential centrifugation to obtain microsomal fraction
- Solubilize with 1% CHAPS detergent
- Enrich membrane proteins by ultracentrifugation

**Activity-based enrichment**:
- Incubate extract (100 mg protein) with 20 µM mechanism-based probe (1 h, 37°C)
- Click conjugation to biotin-azide (CuAAC chemistry)
- Streptavidin affinity purification
- Elute with formic acid, neutralize, concentrate

**Multi-dimensional chromatography purification**:
1. Anion exchange (Q-Sepharose): elute with 0-1 M NaCl gradient
2. Hydrophobic interaction (Phenyl-Sepharose)
3. Size exclusion (Superdex 200)
- Assay fractions with NGD→cGDPR fluorescence assay (λex=300nm, λem=410nm) established in thesis
- Track activity through purification, aim for single band on SDS-PAGE

**Mass spectrometry identification**: In-gel trypsin digest of final purified band, LC-MS/MS identification, confirm by Western blot with antibodies to identified protein.

**Recombinant validation**: Clone identified gene, express in *E. coli* or *Pichia*, purify, confirm NAD⁺→cADPR conversion by HPLC and mass spectrometry.

#### 2.4 Electrophysiological Reconstitution

**cADPR receptor validation**:
- Whole-vacuole patch-clamp on protoplasts from receptor candidate overexpression lines
- Bath (cytosolic face): 100 mM K-gluconate, 2 mM MgCl₂, 100 nM free Ca²⁺, 10 mM HEPES pH 7.2
- Pipette (luminal face): 100 mM K-gluconate, 1 mM CaCl₂
- Apply cADPR (0.1-100 µM) to cytosolic side
- Measure single-channel conductance, open probability, inhibition by 8-NH₂-cADPR and ruthenium red
- Compare to TPC1-mediated currents to ensure distinct identity

**Cyclase enzymatic characterization**:
- Determine Km and Vmax for NAD⁺ substrate (vary 10 µM - 10 mM)
- Test regulation by cGMP (established activator in other systems)
- Measure cADPR hydrolase activity (potential bifunctional enzyme)
- Assay NAADP synthesis from NADP + nicotinic acid

### Expected Outcomes and Impact

**Deliverables**:
1. Molecular identity of plant cADPR receptor
2. Identification of canonical plant ADP-ribosyl cyclase (if exists)
3. Comparative structural modeling with animal RyRs
4. Biochemical characterization of cyclase regulation

**Impact**: These discoveries will complete the cADPR signaling pathway in plants and reveal whether plants evolved convergent solutions to cADPR signaling or retained ancestral mechanisms distinct from animals.

### Timeline: 4 years
- **Year 1**: Proteomics and screen setup, initial genetic screen
- **Year 2**: Complete screen, genetic mapping, cyclase purification
- **Year 3**: Gene validation, heterologous expression
- **Year 4**: Structural and mechanistic studies

---

## PROPOSAL 3: Defining Physiological Roles of NAADP in Plant Signaling

### Background and Significance

NAADP was discovered as a Ca²⁺-mobilizing agent in higher plants in 2000 (Navazio et al., *PNAS*), mobilizing Ca²⁺ from ER stores with nanomolar potency. However, 25 years later, its physiological significance remains uncertain. In contrast to InsP₃ and cADPR—which have well-established roles in ABA signaling, immunity, and development—no specific biological function has been ascribed to NAADP in plants. This gap stems from three challenges: (1) inability to identify the NAADP receptor, (2) lack of specific pharmacological inhibitors, and (3) technical difficulties in measuring endogenous NAADP dynamics.

The discovery that plant TPC1 is NOT an NAADP receptor (unlike animal TPC1/2) eliminated the most obvious candidate. Meanwhile, TIR domain NADases generate cADPR isomers but not NAADP. Whether NAADP is a bona fide plant signaling molecule or a biochemical curiosity remains the fundamental question.

### Central Hypothesis

NAADP serves as a **specialized Ca²⁺ messenger for rapid, localized ER Ca²⁺ release** in specific developmental or stress contexts (e.g., tip growth, ER stress responses) that cannot be adequately served by vacuolar Ca²⁺ pools accessed by InsP₃/cADPR.

### Specific Aims

**Aim 1**: Develop tools to manipulate cellular NAADP levels
- Generate CRISPR knockouts of candidate NAADP synthesis/degradation pathways
- Create chemogenetic system for acute NAADP production

**Aim 2**: Measure endogenous NAADP dynamics during plant stress/development
- Develop ultrasensitive LC-MS/MS method for NAADP quantification
- Measure NAADP levels during ER stress, pathogen infection, pollen tube growth

**Aim 3**: Identify NAADP receptor via chemical genetic resistance screen
- Synthesize NAADP analogs with altered potency
- Screen for mutations conferring resistance to toxic NAADP analogs

**Aim 4**: Assess physiological consequences of NAADP pathway disruption
- Characterize phenotypes of NAADP synthesis knockouts
- Rescue experiments with exogenous NAADP delivery

### Research Approach and Methodology

#### 3.1 Genetic Manipulation of NAADP Pathways

**Candidate pathway identification**: Review literature on animal NAADP metabolism:
- **Synthesis**: In animals, CD38/CD157 ADP-ribosyl cyclases catalyze NADP + nicotinic acid → NAADP via base-exchange
- **Degradation**: NAADP is hydrolyzed by alkaline phosphatases and potentially specific NAADP phosphatases

**Plant enzyme identification**:
- Search Arabidopsis genome for genes encoding proteins with predicted ADP-ribosyl cyclase activity (despite no canonical CD38 homologs, may have convergent evolution)
- Identify all alkaline phosphatases and NUDIX hydrolases (potential degradation enzymes)

**CRISPR knockout strategy**: Generate double/triple knockouts of candidate synthesis genes to overcome redundancy. For degradation enzymes, generate dominant-negative versions with catalytic site mutations.

**Chemogenetic NAADP production**: Adapt rapamycin-inducible dimerization system:
- Express animal CD157 enzyme split into two inactive fragments
- Fuse fragments to FRB and FKBP domains
- Rapamycin addition induces dimerization → reconstitutes active cyclase → NAADP burst
- Validate by LC-MS/MS measurement of cellular NAADP levels

#### 3.2 Quantification of Endogenous NAADP

**Extraction protocol optimization**: Test multiple extraction methods (perchloric acid, TCA, formic acid) for NAADP recovery from plant tissue. Spike-in [¹⁵N₅]NAADP internal standard during homogenization.

**LC-MS/MS method development**:
- HILIC chromatography (ZIC-pHILIC column) for nucleotide separation
- Triple quadrupole MS in negative ion mode
- MRM transitions: NAADP m/z 744→408 (primary), 744→272 (confirmation)
- Limit of detection: 10 fmol (requiring ~100 mg fresh tissue)

**Biological sampling**: Measure NAADP in:
- **ER stress**: Tunicamycin-treated seedlings (1-24h time course)
- **Pathogen infection**: *Pseudomonas* infiltration (0-12h post-inoculation)
- **Pollen tubes**: Growing *Nicotiana tabacum* pollen in vitro
- **Osmotic stress**: Mannitol/NaCl treatment
- **ABA treatment**: Compare to established InsP₃/cADPR responses

**Spatial profiling**: Use MALDI-MSI (matrix-assisted laser desorption ionization mass spectrometry imaging) to map NAADP distribution in tissue sections (e.g., root tips, pollen tubes).

#### 3.3 Chemical Genetic Receptor Screen

**Rationale**: If NAADP has essential functions, analogs that constitutively activate the receptor should be toxic. Resistance mutations will identify the receptor.

**Analog synthesis**: Prepare NAADP derivatives modified at:
- Nicotinic acid moiety (pyridine ring substituents)
- Adenine base (2' or 8 position modifications)
- Phosphate groups (phosphonate mimetics)
Test analogs for Ca²⁺-releasing activity in microsome flux assays

**Toxicity screen**: Identify NAADP analog that inhibits seedling growth at 1-10 µM. For example, a super-agonist analog may cause chronic ER Ca²⁺ depletion → growth arrest.

**Resistance screen**:
- EMS mutagenesis of 100,000 seeds
- Germinate M2 on agar plates containing toxic NAADP analog
- Select survivors (expect ~100-500 based on typical mutation rates)
- Confirm resistance is recessive single-gene trait
- Map by whole-genome sequencing (as in Proposal 2)

**Validation**: Generate CRISPR knockouts of candidate receptor. Confirm loss of NAADP-induced Ca²⁺ release by patch-clamp on isolated ER microsomes or by ER-targeted GCaMP imaging.

#### 3.4 Phenotypic Analysis of NAADP Pathway Mutants

**Systematic phenotyping** of NAADP synthesis knockouts:

**Developmental screens**:
- Germination rates under stress
- Root growth and architecture
- Flowering time
- Pollen viability and tube growth rates
- Seed production

**Stress response assays**:
- **ER stress tolerance**: Tunicamycin/DTT sensitivity, measure unfolded protein response (UPR) marker gene expression (*BiP3*, *CNX1*)
- **Oxidative stress**: H₂O₂ or paraquat resistance
- **Pathogen resistance**: Challenge with *P. syringae*, *Botrytis cinerea*
- **Salt/drought stress**: Ion accumulation, stomatal responses

**Subcellular Ca²⁺ imaging**: Transform mutants with organelle-targeted GCaMPs:
- ER-targeted (ER-jGCaMP8s): Assess ER Ca²⁺ depletion kinetics during stress
- Cytosolic (jGCaMP8m): Measure ER→cytosol Ca²⁺ transfer
- Compare spatiotemporal Ca²⁺ signatures in WT vs. NAADP pathway mutants

**Rescue experiments**: 
- Microinject caged NAADP into mutant cells, UV-photorelease
- Express heterologous NAADP synthesis enzyme under inducible promoter
- Assess phenotype complementation

### Expected Outcomes and Impact

**Scenario A** (NAADP is physiologically important): 
- Mutants will show phenotypes in ER-centric processes (secretion, protein folding, ER stress)
- Specific biological function(s) will be identified
- NAADP receptor will be discovered

**Scenario B** (NAADP is not physiologically significant):
- Mutants will be indistinguishable from WT
- NAADP levels will be constitutively low across conditions
- This important negative result would close a 25-year question

Either outcome transforms understanding and redirects research effort appropriately.

### Timeline: 4 years
- **Year 1**: Tool development (CRISPR lines, MS method), baseline measurements
- **Year 2**: Chemical genetic screen, NAADP dynamics during stress
- **Year 3**: Receptor validation, phenotyping
- **Year 4**: Mechanistic studies, rescue experiments

---

## PROPOSAL 4: Decoding Ca²⁺ Signature Specificity with Systems Biology

### Background and Significance

A central paradigm in Ca²⁺ signaling posits that stimulus-specific information is encoded in the spatiotemporal dynamics of Ca²⁺ elevation—amplitude, frequency, duration, and subcellular location. Guard cells responding to ABA, pathogens, or CO₂ each generate distinct Ca²⁺ "signatures." Yet how these signatures are decoded into specific outputs remains largely mysterious. 

Plants achieve this with a **dramatically simpler toolkit** than animals: no voltage-gated Ca²⁺ channels, no InsP₃/ryanodine receptors, fewer channel types overall. This implies either (1) plants require less signaling specificity, or (2) plants achieve equivalent specificity through different mechanisms—combinatorial channel deployment, decoder multiplexing, or compartmentalization.

Recent technical advances enable this question to be addressed: optogenetic Ca²⁺ actuators allow imposing defined Ca²⁺ signatures, transcriptomics reveals downstream outputs, and computational modeling can test sufficiency of proposed decoding mechanisms.

### Central Hypothesis

Plant Ca²⁺ signature specificity emerges from **three-layer combinatorial encoding**: (1) differential channel deployment across cell types/organelles, (2) multiplex decoding by the expanded CDPKs/CBLs with distinct Ca²⁺ affinities, and (3) frequency/amplitude filtering through decoder-target phosphorylation-dephosphorylation cycles.

### Specific Aims

**Aim 1**: Systematically characterize Ca²⁺ signatures across stimuli and cell types
- High-throughput Ca²⁺ imaging of 20 stimuli × 5 cell types with subcellular resolution
- Define "signature space" using dimensionality reduction

**Aim 2**: Impose artificial Ca²⁺ signatures with optogenetic actuators
- Deploy ORAI-LiGluR system for programmable Ca²⁺ patterns
- Test sufficiency of signatures to trigger specific transcriptional outputs

**Aim 3**: Map Ca²⁺ decoder deployment and binding properties
- Single-cell RNA-seq atlas of sensor/decoder expression
- Measure Ca²⁺-binding affinities and activation kinetics for all 34 CDPKs

**Aim 4**: Computational modeling of signature-to-output transformation
- Build biophysical models of decoder activation
- Predict and test signature discrimination capacity

### Research Approach and Methodology

#### 4.1 Comprehensive Ca²⁺ Signature Atlas

**Reporter system**: Generate Arabidopsis stable lines expressing:
- Cytosolic: jGCaMP8m (fast kinetics, high sensitivity)
- ER: ER-LAR-GECO1 (low-affinity red sensor for high [Ca²⁺]ER)
- Vacuole: Vac-jGCaMP8s

**Multicellular imaging**: Use UBQ10 promoter for ubiquitous expression; image intact tissues with light-sheet microscopy (Zeiss Z.1) for 3D volumetric imaging.

**Stimulus panel** (applied via perfusion):
1. **Hormones**: ABA, auxin, brassinosteroids, jasmonate, salicylic acid
2. **PAMPs**: flg22, chitin, elf18
3. **Abiotic**: NaCl, mannitol, H₂O₂, cold shock, heat shock
4. **Mechanical**: touch, hypoosmotic shock
5. **Nutrients**: nitrate, phosphate depletion
6. **Light**: blue, red, far-red

**Cell type specificity**: Image in:
- Root epidermal cells
- Root hair cells  
- Guard cells
- Mesophyll cells
- Pollen tubes

**Image analysis pipeline**:
- Automated segmentation (CellPose neural network)
- Extract features for each cell: baseline [Ca²⁺], peak amplitude, rise time, decay time, oscillation frequency, oscillation duty cycle, wave propagation velocity
- Dimensionality reduction (UMAP) to visualize "signature space"
- Hierarchical clustering to identify signature classes

#### 4.2 Optogenetic Ca²⁺ Pattern Imposition

**Optogenetic system**: Deploy ORAI-LiGluR fusion (Kyung et al., *Nature Biotech*, 2015):
- Light-gated glutamate receptor (LiGluR) fused to ORAI Ca²⁺ channel
- Blue light (470 nm) opens channel → Ca²⁺ influx
- Kinetics allow generating oscillations up to 1 Hz

**Transgenic line**: Transform Arabidopsis with UBQ10::ORAI-LiGluR + cytosolic jRGECO1a (red Ca²⁺ sensor to avoid spectral overlap with blue stimulation light).

**Pattern generation**: Use digital micromirror device (DMD) for spatially patterned illumination:
- **Single spike**: 5s pulse
- **Oscillatory**: 0.1, 0.5, 1 Hz square wave for 10 min
- **Amplitude-modulated**: vary light intensity for low vs. high amplitude
- **Spatially restricted**: illuminate only guard cells in epidermis, measure transcriptional response in mesophyll

**Transcriptional readout**:
- Harvest tissue 30 min and 2h post-stimulation
- RNA-seq (3 biological replicates per pattern)
- Compare to RNA-seq from bona fide stimulus (e.g., ABA treatment)
- Assess overlap: does artificial "ABA-like" Ca²⁺ signature activate ABA-responsive genes (*RD29A*, *RAB18*, *KIN1*)?

**Key prediction**: If signatures encode specificity, then artificial imposition of an ABA-like Ca²⁺ signature should activate ABA-responsive genes even without ABA present.

#### 4.3 Decoder Atlas and Biophysical Properties

**Single-cell RNA-seq**: Perform on 5 cell types using protoplasting + FACS enrichment:
- Guard cells (GFP-marked by GC1 promoter)
- Root hairs (RHD6 promoter)
- Mesophyll (isolated from protoplasts)
- Root epidermal (non-hair)
- Pollen tubes

Sequence 5,000 cells per type (10× Genomics). Map expression of:
- Ca²⁺ channels (20 GLRs, 20 CNGCs, TPC1, MCAs, Annexins)
- Decoders (34 CDPKs, 10 CBLs, 26 CIPKs, 50 CMLs)
- Downstream targets (transcription factors, ion channels)

**Ca²⁺-binding measurements**: Recombinantly express all 34 CDPKs in *E. coli* as His-tagged fusions. Purify via Ni-NTA. Measure:
- **Ca²⁺ binding affinity**: Use isothermal titration calorimetry (ITC) to determine Kd for Ca²⁺ binding to EF-hand domain
- **Activation kinetics**: FRET-based kinase activity sensor (Campbell et al., *Nature Methods*, 2012). Mix with substrate peptide + ATP, trigger with rapid Ca²⁺ photorelease from caged Ca²⁺, measure phosphorylation kinetics (τ activation)

**Hypothesis**: CDPKs partition into low-affinity (Kd ~1-10 µM, respond to high-amplitude spikes) and high-affinity (Kd ~100-500 nM, respond to low-amplitude sustained elevations) groups, enabling amplitude decoding.

#### 4.4 Computational Modeling

**Model architecture**: Build ordinary differential equation (ODE) model:
```
d[Ca²⁺]/dt = Jin - Jout
Jin = Σ(channel activities)
Jout = Pumps + Buffers

d[CDPK*]/dt = kon[Ca²⁺]⁴[CDPK] - koff[CDPK*]
(cooperative binding, Hill coefficient ~4)

d[Target~P]/dt = kcat[CDPK*][Target] - kphos[Target~P]
```

**Parameter estimation**: 
- Use measured Ca²⁺-binding Kd values for CDPKs
- Fit channel conductances to match experimental Ca²⁺ signatures
- Estimate phosphatase rates from literature

**In silico experiments**:
1. Simulate 20 different Ca²⁺ input signatures
2. Calculate CDPK activation profiles (which CDPKs activate for each signature)
3. Calculate target phosphorylation states
4. Assess discrimination: Can model distinguish signatures based on output phosphorylation patterns?

**Information theory analysis**: Calculate mutual information I(Stimulus; Output) to quantify how much stimulus information is preserved through the Ca²⁺ → decoder → output transformation.

**Predictions to test experimentally**:
- Model may predict: "CDPK5 and CDPK6 cannot distinguish between salt and osmotic stress signatures"
- Test: Measure CDPK5/6 activation (using FRET reporters) during NaCl vs. mannitol
- Model may predict: "Oscillation frequency is decoded by CDPK21"
- Test: Express CDPK21 with calcium-insensitive mutant (EF-hand disabled), assess loss of frequency discrimination in transcriptional output

### Expected Outcomes and Impact

**Deliverables**:
1. Comprehensive atlas of plant Ca²⁺ signatures (publicly accessible database)
2. Proof-of-principle that artificial Ca²⁺ signatures are sufficient for transcriptional outputs
3. Biophysical decoder map (affinities, kinetics, expression patterns)
4. Quantitative model predicting signature decoding capacity

**Impact**: Transform Ca²⁺ signaling from qualitative phenomenon to quantitative, predictive framework. Enable rational design of synthetic Ca²⁺ circuits.

### Timeline: 4 years
- **Year 1**: Generate transgenic lines, Ca²⁺ signature imaging
- **Year 2**: Optogenetics, scRNA-seq atlas
- **Year 3**: Decoder biophysical measurements
- **Year 4**: Computational modeling, experimental validation

---

## PROPOSAL 5: Mechanisms of NLR Resistosome Ca²⁺ Channel Activation and Immune Specificity

### Background and Significance

The 2021 discovery that plant NLR immune receptors form pentameric Ca²⁺-permeable channels (resistosomes) upon pathogen detection revolutionized understanding of plant immunity. Within 24 hours of effector recognition, activated ZAR1, Sr35, and helper NRGs oligomerize into ring-shaped structures that insert into membranes and mediate Ca²⁺ influx, triggering hypersensitive cell death.

However, fundamental questions remain: (1) **How do resistosome channels specifically activate immune outputs rather than generic Ca²⁺ responses?** (2) What distinguishes the Ca²⁺ signature generated by resistosomes from other Ca²⁺-elevating stimuli? (3) Do different resistosomes generate distinct Ca²⁺ signatures for tailored immune responses?

### Central Hypothesis

Resistosome Ca²⁺ channels generate **ultra-localized, high-amplitude Ca²⁺ nanodomains** at the plasma membrane that specifically activate a subset of calcium decoders (CPK5/CPK6/CPK11) via proximity-based coupling, distinct from the global cytosolic Ca²⁺ elevations produced by other channels.

### Specific Aims

**Aim 1**: Characterize the spatiotemporal Ca²⁺ signature of resistosome activation
- Super-resolution Ca²⁺ imaging near activated resistosomes
- Compare ZAR1, Sr35, and NRG resistosome Ca²⁺ signatures

**Aim 2**: Identify Ca²⁺ decoders specifically coupled to resistosome channels
- Proximity labeling (TurboID) to identify proteins near activated resistosomes
- Test decoder specificity by swapping with non-immune Ca²⁺ channels

**Aim 3**: Determine structural basis of resistosome Ca²⁺ selectivity and gating
- Cryo-EM of activated resistosome embedded in lipid nanodiscs
- Mutagenesis of pore region, assess Ca²⁺ vs. monovalent cation selectivity

**Aim 4**: Engineer resistosomes with altered Ca²⁺ signatures for crop protection
- Generate constitutively active resistosome variants
- Test whether resistosome-mediated Ca²⁺ elevation is sufficient for immunity without cell death

### Research Approach and Methodology

#### 5.1 Super-Resolution Ca²⁺ Imaging of Resistosome Activation

**Challenge**: Resistosomes are ~120 Å diameter, generate localized Ca²⁺ nanodomains (<200 nm) that cannot be resolved by conventional confocal microscopy (diffraction limit ~250 nm).

**Solution**: Combine TIRF microscopy (Total Internal Reflection Fluorescence) with low-affinity Ca²⁺ sensors to visualize high [Ca²⁺] microdomains.

**Reporter system**: 
- Transform Arabidopsis with ZAR1 pathway (RKS1-ZAR1-ZED1)
- Co-express PM-targeted low-affinity GCaMP (OPAL-GCaMP6, Kd ~20 µM) + far-red Ca²⁺ sensor (FR-GECO1c, Kd ~400 nM) for dual imaging
- N-terminally tag ZAR1 with HaloTag for resistosome localization

**Experimental workflow**:
1. Generate protoplasts from transgenic leaves
2. Attach to coverslips coated with Cell-Tak
3. Add AvrAC effector (triggers ZAR1 oligomerization) + JF646 HaloTag ligand
4. TIRF imaging: 488 nm (GCaMP), 640 nm (FR-GECO), 730 nm (HaloTag-JF646)
5. Acquire at 50 Hz for 5 min post-activation

**Image analysis**:
- Segment ZAR1 puncta (resistosome locations)
- Measure Ca²⁺ sensor intensity in 500 nm radius around each resistosome
- Calculate local [Ca²⁺] using ratiometric FR-GECO/OPAL-GCaMP calibration
- Measure nanodomain spatial extent (FWHM) and temporal dynamics (rise time, decay kinetics)

**Comparative analysis**: Repeat with Sr35 resistosome (wheat → Nicotiana expression) and NRG1 helper resistosome. Hypothesis: Different resistosomes may generate quantitatively distinct Ca²⁺ signatures.

#### 5.2 Identification of Resistosome-Coupled Decoders

**Proximity labeling**: Use TurboID enzyme (ultrafast biotin ligase) fused to ZAR1 to label proteins within ~10 nm radius during resistosome activation.

**Experimental design**:
- Express ZAR1-TurboID (C-terminal fusion) in *N. benthamiana*
- Co-infiltrate with AvrAC effector
- At T=0 of resistosome activation, add 500 µM biotin to media
- Harvest tissue at 0.5, 5, 30 min
- Purify biotinylated proteins on streptavidin beads
- LC-MS/MS identification

**Expected enriched proteins**:
- RBOHD NADPH oxidase (known immune Ca²⁺ target)
- Specific CDPK isoforms (CPK5/6/11 are candidates based on immune function)
- PM-localized kinases and phospholipases

**Functional validation**: For top hits (e.g., CPK5):
1. Generate CPK5-ZAR1 fusion to force coupling
2. Express in *cpk5* knockout background
3. Measure immune output (ROS burst, defense gene expression)
4. Compare to WT ZAR1 (endogenous coupling)

**Channel-swapping experiment**: Test decoder specificity:
- Replace ZAR1 pore-forming domain with ORAI channel domain (also PM Ca²⁺ channel but non-immune)
- Trigger ORAI opening with store depletion
- Measure: Does this activate immune outputs or only generic Ca²⁺ responses?
- Prediction: Resistosome couples decoders via protein-protein interaction, not just local [Ca²⁺]

#### 5.3 Structural Basis of Resistosome Ca²⁺ Conductance

**Sample preparation for cryo-EM**:
- Express ZAR1/RKS1/PBL2 in *Sf9* insect cells (improved expression vs. plants)
- Trigger activation with AvrAC, purify resistosomes via size-exclusion chromatography
- Reconstitute into MSP1D1 lipid nanodiscs (POPC:POPE 3:1 mimicking PM composition)

**Cryo-EM imaging**:
- Vitrify on Quantifoil grids
- Image on Titan Krios (300 kV) with K3 detector
- Collect 10,000+ movies
- Process with cryoSPARC: Particle picking, 2D classification, 3D refinement
- Target resolution: <3 Å (achieved for ZAR1 in previous studies)

**Structure analysis**:
- Identify pore-lining residues using HOLE program
- Measure pore diameter at narrowest constriction
- Model Ca²⁺ binding sites using Rosetta
- Compare to CaV channels and TPC1 for mechanistic insights

**Functional mutagenesis**: Based on structure, mutate:
- Putative selectivity filter (negatively charged residues in pore)
- Proposed gating hinge (conserved Gly/Pro)
- Aromatic "lid" residues (might control opening)

**Electrophysiology**: Reconstitute mutant resistosomes into planar lipid bilayers. Apply voltage-clamp, measure:
- Single-channel conductance (expect ~40 pS for Ca²⁺)
- Ion selectivity (PCa/PNa ratio)
- Voltage-dependence (if any)
- Inhibition by Ca²⁺ channel blockers (Gd³⁺, La³⁺)

#### 5.4 Engineering Resistosomes for Crop Protection

**Rationale**: Resistosome activation causes cell death (hypersensitive response), limiting applications. Can we engineer resistosomes that trigger immunity without death?

**Strategy 1 - Tunable activation**:
- Insert estrogen-binding domain (EBD) into ZAR1 linker region
- Estradiol binding releases autoinhibition → resistosome formation
- Dose estradiol to achieve sub-lethal Ca²⁺ elevation

**Strategy 2 - Reduced conductance**:
- Engineer pore mutants with reduced Ca²⁺ flux
- Screen for variants that activate MAPK signaling (immunity) but not metacaspases (cell death)

**Crop transformation**:
- Express engineered resistosome in tomato (*S. lycopersicum*) via *Agrobacterium*
- Challenge with *Pseudomonas syringae* pv. *tomato*
- Measure: Bacterial growth, lesion size, plant survival, yield impact

**Key test**: Can we achieve broad-spectrum disease resistance without yield penalty from excessive cell death?

### Expected Outcomes and Impact

**Deliverables**:
1. High-resolution map of resistosome Ca²⁺ nanodomains
2. Identification of decoder proteins specifically coupled to resistosomes  
3. Atomic structure of Ca²⁺-conducting resistosome channel
4. Proof-of-concept engineered resistosome for crop protection

**Impact**: Provide mechanistic understanding of newest class of plant Ca²⁺ channels and develop new biotechnology platform for engineering disease-resistant crops.

### Timeline: 4 years
- **Year 1**: Establish imaging and TurboID proteomics
- **Year 2**: Structural biology, decoder validation
- **Year 3**: Mutagenesis and functional characterization
- **Year 4**: Crop engineering and field trials

---

## PROPOSAL 6: Engineering Ca²⁺ Signaling for Crop Stress Tolerance

### Background and Significance

Climate change intensifies abiotic stresses (drought, salinity, heat) that devastate global crop yields. Ca²⁺ signaling is central to plant stress perception and response, yet current crops rely on naturally evolved Ca²⁺ networks that may be suboptimal for agricultural environments. Rational engineering of Ca²⁺ signaling offers transformative potential but has been limited by incomplete mechanistic understanding.

Recent discoveries present new opportunities: (1) GLR desensitization mutants show altered systemic signaling (Shao et al., *Nature Plants*, 2024), (2) CRISPR enables precise channel modification, (3) CBL-CIPK networks can be rewired. This proposal aims to engineer enhanced stress tolerance through **targeted Ca²⁺ circuit modification**.

### Central Hypothesis

Strategic modification of Ca²⁺ signature generation (via GLR/CNGC variants) and decoding (via CDPK/CIPK optimization) can **improve stress tolerance without yield penalty** by tuning signal sensitivity, duration, and specificity.

### Specific Aims

**Aim 1**: Identify Ca²⁺ signaling modifications that enhance stress tolerance in Arabidopsis
- CRISPR library targeting Ca²⁺ signaling genes for gain-of-function
- High-throughput stress screens

**Aim 2**: Validate lead candidates in crop species (tomato, rice)
- CRISPR engineering of orthologous genes
- Field trial assessment of stress tolerance and yield

**Aim 3**: Develop combinatorial engineering strategies
- Stack multiple beneficial Ca²⁺ pathway modifications
- Optimize with machine learning prediction

**Aim 4**: Assess environmental safety and regulatory pathway
- Pollen flow, off-target assessment
- Prepare regulatory documentation for engineered lines

### Research Approach and Methodology

#### 6.1 CRISPR Gain-of-Function Library Screen

**Gene target selection** (200 genes):
- **Ca²⁺ channels**: All 20 GLRs, 20 CNGCs, MCAs, Annexins (45 genes)
- **Decoders**: 34 CDPKs, 10 CBLs, 26 CIPKs (70 genes)
- **Regulators**: PP2C phosphatases, ROPs, RBOH (20 genes)
- **Transporters**: CAXs, ACAs (15 genes)
- **Others**: PLC, TPC1, transcription factors (50 genes)

**CRISPR strategy**: Use activation-CRISPRa (dCas9-VP64) to upregulate target genes rather than knockout. Design 4 sgRNAs per gene targeting promoter region (-200 to -1 bp).

**Library transformation**: Transform Arabidopsis (Col-0) via floral dip, select T1 transformants (expect 50,000 lines for >95% library coverage).

**Stress screens**:

**Primary screen - Drought tolerance**:
- Germinate T2 seeds on soil, grow 2 weeks under normal watering
- Withhold water for 10 days (WT plants wilt severely)
- Re-water, score survival after 3 days
- Select survivors (expect ~2-5% hit rate)

**Secondary screens** on primary hits:
- **Salt tolerance**: 150 mM NaCl irrigation for 2 weeks, measure biomass
- **Heat tolerance**: 42°C for 4h daily × 5 days, measure photosynthetic efficiency (Fv/Fm)
- **Freezing tolerance**: −8°C for 2h after cold acclimation

**Genotyping**: Identify activated gene in survivors by PCR amplification of sgRNA cassette followed by Sanger sequencing.

**Validation**: Generate independent CRISPR lines (promoter replacement with strong 35S) for top 10 candidates. Confirm phenotype in T3 homozygous lines.

#### 6.2 Mechanistic Characterization of Lead Variants

**For each validated hit, perform**:

**Ca²⁺ signature analysis**:
- Transform with cytosolic jGCaMP8m
- Image Ca²⁺ responses to drought/salt/heat stress
- Quantify: Does overexpression alter signature amplitude, frequency, duration?

**Transcriptomics**:
- RNA-seq under stress (3h salt treatment)
- Compare stress-responsive gene expression vs. WT
- Hypothesis: Enhanced tolerance from earlier/stronger activation of adaptive transcriptional programs

**Physiological measurements**:
- **Stomatal conductance**: Measure closure kinetics in response to ABA/drought
- **ROS levels**: DAB staining, H₂O₂-specific fluorescent probe
- **Osmolyte accumulation**: Proline, soluble sugars
- **Ion homeostasis**: Na⁺/K⁺ ratio in salt stress

**Example prediction**: GLR3.3 overexpression may enhance systemic wound signaling (based on Toyota et al. 2018 findings). Test whether this improves systemic acquired acclimation to drought.

#### 6.3 Crop Translation

**Target crops**: 
- **Tomato** (*Solanum lycopersicum*): High-value crop, Agrobacterium-transformable
- **Rice** (*Oryza sativa*): Staple crop, salt-sensitive, well-established transformation

**Ortholog identification**: Use Arabidopsis hit as query for BLAST against tomato/rice genomes. Generate phylogenetic trees to identify true orthologs (not just top BLAST hit).

**CRISPR engineering**: Design sgRNAs using CHOPCHOP tool. Use tissue culture transformation:
- Tomato: Cotyledon explant transformation
- Rice: Callus transformation

**Targeting strategy based on Arabidopsis findings**:
- If CRISPRa worked: Use strong constitutive promoter (UBQ/ACTIN) to drive ortholog
- If desensitization mutant worked: CRISPR-edit specific residues (e.g., Ca²⁺-binding site in GLR)
- If decoder rewiring worked: Replace promoter with stress-inducible (RD29A)

**Field trials** (Years 3-4):
- Randomized block design with 4 replicates
- Treatments: Well-watered control, drought stress (50% reduction in irrigation), salt stress (irrigate with 100 mM NaCl)
- Measure: Biomass, fruit yield, water use efficiency, fruit quality parameters
- Perform across 2 seasons and 2 locations

**Critical assessment**: Is there a yield penalty under optimal conditions? Many stress tolerance modifications inadvertently reduce growth. Only variants showing neutral or positive yield under optimal conditions advance.

#### 6.4 Combinatorial Optimization

**Hypothesis**: Stacking multiple beneficial Ca²⁺ pathway modifications may provide additive or synergistic stress tolerance.

**Strategy**: 
- Cross top 3-5 Arabidopsis single-gene lines
- Generate all pairwise combinations (e.g., GLR3.3-OX × CPK21-OX)
- Assess stress tolerance

**Machine learning prediction**: 
- Train neural network on single-gene phenotyping data (input: gene identity + expression level; output: stress tolerance score)
- Predict optimal combinations
- Test top 10 predictions experimentally

**Potential synergies**:
- **Channel + decoder**: GLR overexpression + CPK that responds to GLR-generated Ca²⁺ signature
- **Synthesis + buffering**: Enhanced Ca²⁺ release (CNGC) + enhanced Ca²⁺ reuptake (ACA8) for faster signal termination and recovery
- **Perception + output**: HPCA1 (ROS sensor) + RBOHD (ROS producer) for positive feedback loop tuning

#### 6.5 Safety and Regulatory Assessment

**Environmental risk assessment**:

**Pollen flow**: 
- Measure pollen dispersal distances in field trials (bee traps, sticky traps)
- Model gene flow to related wild species (for tomato: wild *S. pimpinellifolium*)
- Mitigation: Use cytoplasmic male sterility if needed

**Off-target effects**:
- Whole-genome sequencing of engineered lines
- Confirm no off-target mutations at predicted sites (using in silico prediction)
- Compare transcriptome of engineered line vs. WT under 3 conditions (control, drought, salt)

**Allergenicity**: 
- Bioinformatic analysis of any new proteins (compare to AllergenOnline database)
- If protein modifications were made, test serum IgE binding

**Nutritional analysis**:
- Proximate analysis (protein, fat, carbohydrate, minerals)
- Vitamin content
- Anti-nutritional factors (e.g., trypsin inhibitors)

**Regulatory strategy**:
- USDA: "Am I Regulated?" inquiry for plants with CRISPRa or precise edits
- FDA: GRAS notification if going to market
- EPA: Not required if no pesticide properties
- Prepare regulatory dossier including molecular characterization, phenotypic data, safety assessments

### Expected Outcomes and Impact

**Deliverables**:
1. Catalog of Ca²⁺ signaling modifications that enhance stress tolerance
2. Mechanistic understanding of how modifications improve tolerance
3. Engineered crop varieties with field-validated stress tolerance
4. Regulatory-ready documentation for commercial deployment

**Impact**: 
- Provide climate-resilient crop varieties for sustainable agriculture
- Demonstrate Ca²⁺ signaling as a viable engineering target
- Reduce need for irrigation and chemical inputs

**Economic potential**: A 10-20% yield improvement in stress-prone regions could impact millions of farmers globally.

### Timeline: 5 years
- **Year 1**: CRISPR library screen in Arabidopsis
- **Year 2**: Mechanistic characterization, crop transformation
- **Year 3**: Field trials (season 1), regulatory prep
- **Year 4**: Field trials (season 2), combinatorial engineering
- **Year 5**: Data analysis, publication, regulatory submission

---

## Cross-Cutting Considerations for All Proposals

### Shared Technical Infrastructure Needs

1. **Imaging Core**: Confocal, light-sheet, TIRF, super-resolution microscopes
2. **Genomics Core**: Illumina sequencing, 10× Chromium for scRNA-seq
3. **Proteomics Core**: Orbitrap mass spectrometer, LC-MS/MS
4. **Structural Biology**: Cryo-EM facility (Proposals 2, 5)
5. **Plant Growth Facilities**: Controlled environment chambers, greenhouse, field sites

### Synergies Between Proposals

- **Proposals 1 & 2** share proteomics and electrophysiology approaches
- **Proposals 1, 2, 3** findings feed into **Proposal 4** modeling
- **Proposal 5** NLR findings inform **Proposal 4** decoder specificity
- **Proposal 6** benefits from molecular targets identified in **Proposals 1-5**

### Training Opportunities

Each proposal provides interdisciplinary training spanning:
- Molecular biology (CRISPR, cloning)
- Cell biology (microscopy, Ca²⁺ imaging)
- Biochemistry (protein purification, MS)
- Biophysics (electrophysiology, ITC)
- Computational biology (RNA-seq analysis, modeling)
- Plant physiology (stress tolerance, phenotyping)

### Open Science Commitment

All proposals commit to:
- Depositing plasmids to Addgene
- Sharing seed stocks via ABRC
- Posting preprints to bioRxiv
- Publishing in open-access journals where possible
- Making all sequencing data publicly available (GEO, SRA)
- Creating interactive data visualization portals for Ca²⁺ signature atlas (Proposal 4) and decoder atlas (Proposal 4)

---

## Summary

These six proposals collectively address the most pressing unsolved questions in plant calcium signaling, spanning from fundamental molecular identification to applied crop improvement. Success in any single proposal would represent a major advance; together, they offer a comprehensive roadmap to transform the field over the next 5 years.
