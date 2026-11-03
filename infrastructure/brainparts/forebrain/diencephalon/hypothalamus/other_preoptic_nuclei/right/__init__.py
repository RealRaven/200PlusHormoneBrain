"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.other_preoptic_nuclei.right
Anatomical Role:
    Right hemisphere of the "other preoptic nuclei" group. Same named
    nuclei documented in ../left/, mirrored to the right hemisphere,
    each documented WITHIN this file (not as further child nodes):
        - Anteroventral periventricular nucleus (AVPV): kisspeptin-
          expressing, female-larger, estrogen-positive-feedback relay.
        - Anterodorsal preoptic nucleus (ADP): small vasopressin-
          expressing nucleus; minor fluid/social contributor.
        - Striohypothalamic nucleus: poorly characterized.
        - Ventral preoptic area: poorly characterized.
        - Other small preoptic cell groups not classified under
          lateral_area or medial_area.
    See ../left/__init__.py for the full anatomical description, the
    AVPV anchor framing, and the honest documentation of the poorly
    characterized regions.

    Reproduced critical distinctions (all apply equally on the right):
    - PREOPTIC COLLISION: this file is NOT lateral_area/right/
      preoptic_area/ and NOT medial_area/right/preoptic_area/. It is
      the "other" preoptic group.
    - AVPV ↔ PeN: the AVPV is DISTINCT from the right periventricular
      preoptic nucleus (lateral_area/right/periventricular_preoptic_
      nucleus/) but they are adjacent kisspeptin populations that
      function as a continuum. CONTINUITY EDGE, not duplicate-
      structure warning. Do not merge.
    - AVPV-vs-PeN SPECIALIZATION: AVPV = estrogen POSITIVE feedback /
      surge; PeN = tonic drive / pulse frequency. Same anatomy
      (kisspeptin, periventricular), different jobs. Do not flatten
      into "the kisspeptin nucleus."
    - AVPV-vs-INAH-3 DIMORPHISM: AVPV is larger in females (estrogen-
      positive-feedback substrate); INAH-3 is larger in males (SDN-POA
      homologue). OPPOSITE dimorphisms in adjacent regions. Do not
      conflate.

Functional Mode:
    Same as ../left/. AVPV: estrogen positive feedback (the surge);
    sexual dimorphism (female-larger). ADP: vasopressin, minor fluid/
    social contributor. Striohypothalamic and ventral preoptic:
    poorly characterized, documented factually without overclaiming.
    No documented functional asymmetry between left and right AVPV or
    ADP. Do not fabricate one. See ../left/__init__.py § Functional
    Mode.

Hormonal Modulation:
    Same as ../left/. AVPV: estradiol ↑ (positive feedback → surge);
    SCN vasopressin ↑ gating (circadian window); progesterone
    facilitates the surge after estradiol priming; kisspeptin
    amplifies; GABA/glutamate intrinsic. ADP: outputs vasopressin;
    modulated by estradiol and osmotic input via OVLT/SFO. See
    ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. AVPV reads short_term (estradiol, circadian
    phase), episodic (surge history), emotional_valence (stress
    suppression), temporal_sequence_learning (SCN-gated surge
    timing). ADP reads short_term (osmotic state). No stored content
    writes. Striohypothalamic and ventral preoptic: no documented
    interfaces; do not invent. See ../left/__init__.py § Memory
    Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The AVPV contributes a CONSTITUENT
    INPUT to the anterior-division reproductive fragment, aggregated
    with the right PeN (lateral_area/right/periventricular_preoptic_
    nucleus/), right MPN (medial_area/right/preoptic_area/
    medial_preoptic_nucleus/), and right MnPO (medial_area/right/
    preoptic_area/median_preoptic_nucleus/) contributions. The ADP's
    vasopressin is upstream of the right SON/PVN fluid fragment. Do
    not emit right-side AVPV or ADP fragments; aggregate at the
    anterior-division level. See ../left/__init__.py § Model
    Integration for the mandatory aggregation rules. Those rules apply
    identically on the right.

Right-specific reciprocal connections to enforce in Stage 4
(organized by nucleus; do not duplicate the left-side edges in
../left/):

    AVPV (primary):
    - ↔ lateral_area/right/periventricular_preoptic_nucleus (PeN;
      AVPV/PeN CONTINUITY EDGE — kisspeptin continuum; not a
      duplicate-structure warning; this edge CLOSES the continuity on
      the right side, matching the left-side closure in ../left/).
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area/
      medial_preoptic_nucleus (MPN; adjacent preoptic GnRH-regulatory
      nodes; right-side).
    - ← hypothalamus/anterior/medial_area/right/
      suprachiasmatic_nucleus (SCN → AVPV; circadian gating of the LH
      surge; SCN is midline-adjacent — verify).
    - ↔ hypothalamus/tuberal/medial_area/right/arcuate_nucleus
      (kisspeptin KNDy input; the arcuate-to-AVPV kisspeptin network;
      right-side).
    - → preoptic GnRH neuron population (kisspeptin → GnRH neurons; the
      right-side reproductive output edge).
    - ↔ telencephalon/.../subcortical/medial_temporal_lobe/amygdala
      (reproductive/social context; right-side).

    ADP (secondary):
    - ↔ hypothalamus/anterior/medial_area/right/supraoptic_nucleus
      and paraventricular_nucleus (vasopressin co-regulation;
      right-side).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      osmotic input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input; SFO
      is midline).

    Striohypothalamic and ventral preoptic:
    - ↔ telencephalon/.../subcortical/basal_ganglia/striatum (striatal
      input; right-side; poorly characterized function).
    - ↔ lateral_area/right/preoptic_area/lateral_preoptic_nucleus
      (anatomical adjacency; keep distinct — different structures).

    Cross-cutting:
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area (sibling
      preoptic sub-container; adjacent preoptic circuits; right-side).
    - ↔ hypothalamus/anterior/lateral_area/right/preoptic_area
      (sibling preoptic sub-container; adjacent preoptic circuits;
      right-side).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - This is the AVPV CONTINUITY CLOSER on the right: the AVPV/PeN
      continuity edge was declared in lateral_area/right/
      periventricular_preoptic_nucleus/ and deferred to "when the AVPV
      is drafted." ../left/ closed it on the left; this file closes it
      on the right. Both hemispheres now declare the continuity edge
      to the Stage 4 audit.
    - All four traps (preoptic collision, AVPV/PeN continuity, AVPV/
      PeN specialization, AVPV-vs-INAH-3 dimorphism) are reproduced
      above because they are structural/naming traps that apply on
      both hemispheres. The full anatomical, functional, hormonal, and
      memory content is referenced rather than duplicated.
    - No independent fragment: AVPV → aggregated reproductive; ADP →
      upstream fluid. Same aggregation rules as ../left/ and the
      parent container.
    - Do not create AVPV/, ADP/, striohypothalamic_nucleus/, or
      ventral_preoptic_area/ as child nodes on the right either. They
      are documented WITHIN this file, same as ../left/.
    - The AVPV dimorphism (female-larger) is the OPPOSITE of the
      INAH-3 dimorphism (male-larger). Reproduced in abbreviated form
      above because it is the most likely conflation on the right.
    - The striohypothalamic and ventral preoptic regions are poorly
      characterized. Same honest stance as ../left/: document factually,
      do not invent functional roles.
    - Midline targets (SCN, OVLT, SFO) are flagged with "verify" so
      Stage 4 does not force a hemisphere split on structures that are
      not hemisphere-split in the tree. Right PeN, right MPN, right
      MnPO, right arcuate, right amygdala, right striatum, right
      supraoptic, right paraventricular, and right preoptic sub-
      containers are hemisphere-split and require right-side targets
      explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/other_preoptic_nuclei/.
"""