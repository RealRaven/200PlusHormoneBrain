"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.paraventricular_nucleus
Anatomical Role:
    Right hemisphere of the paraventricular nucleus (PVN). The same
    "three-in-one" nucleus documented in ../left/, mirrored to the right
    hemisphere:
        1. Parvocellular neurosecretory (CRH, TRH, somatostatin) —
           hypophyseal portal → anterior pituitary.
        2. Parvocellular preautonomic — brainstem and spinal autonomic
           targets.
        3. Magnocellular neurosecretory (oxytocin, vasopressin) —
           posterior pituitary axon terminals.
    See ../left/__init__.py for the full anatomical description, the
    sub-population framing, and the distinction from the thalamic
    paraventricular nucleus. Do not subdivide this leaf into
    parvocellular_endocrine/ etc.; the three sub-populations are
    documented within each hemisphere's file, not as tree children.

    Reproduced notes (apply equally on the right):
    - NO structural-identity trap: PVN is a single nucleus on both sides.
      Unlike the SON split or the LHA continuum, there is no
      "same structure split across compartments" issue. Do not invent
      one.
    - NO naming collision inside this tree: "paraventricular nucleus" is
      unambiguous as long as the thalamic paraventricular node is not
      added. If the thalamic PVT is later added under
      thalamus/*/midline_nuclear_group/paraventricular_nucleus/, this
      file must be disambiguated as the *hypothalamic* PVN; do not merge
      the two.

Functional Mode:
    Same as ../left/. HPA axis (CRH), HPT axis (TRH), growth axis
    (somatostatin), social/bonding (oxytocin), fluid/osmoregulation
    (vasopressin), autonomic control (parvo-autonomic), and stress
    integration across all three. No documented functional asymmetry
    between left and right PVN. Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. Outputs: CRH, TRH, somatostatin, oxytocin,
    vasopressin. Inputs/feedback: cortisol ↓ CRH, thyroid hormones ↓
    TRH, IGF-1 ↓ somatostatin, estradiol ↑ CRH/oxytocin (sex-dependent),
    leptin ↓ CRH/TRH, ghrelin ↑ CRH/↓ TRH, angiotensin II ↑ vasopressin,
    ANP ↓ vasopressin, cytokines ↑ CRH, monoamines and limbic input
    modulate CRH, SCN gates the morning cortisol peak. See
    ../left/__init__.py § Hormonal Modulation for the full list and
    directions.

Memory Interfaces:
    Same as ../left/. Reads short_term, episodic, emotional_valence,
    temporal_sequence_learning, reinforcement_value_based_learning.
    Writes emotional_valence indirectly via HPA-axis cortisol modulation
    of amygdala tagging. See ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragments. The five PVN fragments (HPA, HPT,
    growth, social/bonding, fluid/osmotic) are emitted once at the left/
    level and represent the bilateral PVN. The autonomic constituent is
    also aggregated at the anterior-division level. Emitting separate
    right-side fragments would double-count all five signals. See
    ../left/__init__.py § Model Integration.

    AGGREGATION RULES (mandatory, repeated because they apply
    identically on the right):
        * Osmotic fragment (5): aggregate with the right-side SON
          contributions (lateral_area/right/part_of_supraoptic_nucleus/
          and medial_area/right/supraoptic_nucleus/) before emission.
          Do not emit an independent un-aggregated right-side osmotic
          fragment.
        * Autonomic constituent (6): aggregate with the right-side AHN
          (anterior_hypothalamic_nucleus/) and preoptic contributions
          before emission. Do not emit an independent un-aggregated
          right-side autonomic fragment.

Right-specific reciprocal connections to enforce in Stage 4 (organized
by sub-population; do not duplicate the left-side edges in ../left/):

    Parvocellular endocrine (CRH, TRH, somatostatin):
    - → pituitary_gland/anterior (CRH, TRH, somatostatin via hypophyseal
      portal; the principal endocrine output edge; anterior pituitary is
      midline).
    - → median_eminence (parvocellular axon terminals; portal release
      site; midline).
    - ← hypothalamus/tuberal/medial_area/right/arcuate_nucleus (leptin,
      ghrelin, NPY/AgRP, POMC inputs; metabolic modulation of CRH and
      TRH; right-side).
    - ← brainstem/.../solitary_nucleus (NTS; visceral and cytokine
      inputs; NTS is midline-adjacent — verify).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/amygdala (stria terminalis and ventral
      amygdalofugal pathway; stress-reactive CRH activation; right-side).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/hippocampus (glucocorticoid feedback;
      hippocampal inhibition of CRH under normal feedback; right-side).
    - ← telencephalon/cerebral_hemispheres/right/cortex/frontal/cortex/
      prefrontal_cortex (executive control of stress reactivity;
      right-side).
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN; circadian gating of the morning cortisol peak; SCN is
      midline-adjacent — verify).

    Parvocellular autonomic:
    - → hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
      (NTS; reciprocal autonomic feedback; NTS is midline-adjacent —
      verify).
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; sympathetic modulation; RVLM
      is midline-adjacent — verify).
    - → hindbrain/myelencephalon/medulla_oblongata/cranial_nerve_nuclei/
      right/dorsal_motor_nucleus_vagus and right/nucleus_ambiguus
      (parasympathetic modulation; right-side).
    - → spinal_cord/gray_matter/right/lateral_horn (sympathetic
      preganglionic modulation; right-side).
    - ↔ hypothalamus/anterior/medial_area/right/
      anterior_hypothalamic_nucleus (autonomic co-regulation; right-side).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/amygdala (central nucleus; autonomic stress
      responses; right-side).

    Magnocellular:
    - → pituitary_gland/neurohypophysis (oxytocin, vasopressin via axon
      terminals; posterior pituitary output edge; midline).
    - ↔ hypothalamus/anterior/medial_area/right/supraoptic_nucleus (SON;
      magnocellular co-regulation; right-side).
    - ↔ hypothalamus/anterior/lateral_area/right/
      part_of_supraoptic_nucleus (lateral SON portion; magnocellular
      co-regulation; right-side).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      angiotensin II input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input; SFO
      is midline).

    Cross-cutting:
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → PVN autonomic and endocrine circadian gating; SCN is
      midline-adjacent — verify).
    - ↔ hypothalamus/anterior/lateral_area/right/preoptic_area/
      lateral_preoptic_nucleus (stress-induced insomnia; CRH and stress
      signaling modulates LPO sleep circuitry; right-side).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - This is the LONGEST delta in the tree (~15–20 right-side edges)
      because the PVN is the most connection-heavy nucleus. It is still
      a delta: no functional content duplicated, no fragments emitted,
      no hormonal inputs re-described. The length comes entirely from
      the reciprocal-edge list.
    - The three sub-populations are not tree children; do not create
      paraventricular_nucleus/parvocellular_endocrine/ or similar nodes
      on the right either. The sub-population framing is documented in
      ../left/ and referenced here.
    - No structural-identity trap and no naming collision to reproduce
      (the PVN is a single, unambiguously named nucleus on both sides).
      The "no trap" notes above are reproduced not because there is a
      trap, but because a contributor entering at the right/ level
      should not pattern-match and invent one.
    - Midline targets (anterior pituitary, median eminence, NTS, RVLM,
      neurohypophysis, OVLT, SFO, SCN) are flagged with "verify" so
      Stage 4 does not force a hemisphere split on structures that are
      not hemisphere-split in the tree. Amygdala, hippocampus, PFC,
      arcuate, AHN, SON (medial and lateral parts), LPO, DMV, nucleus
      ambiguus, and spinal lateral horn are all hemisphere-split and
      therefore require right-side targets explicitly.
    - The thalamic paraventricular nucleus (PVT) is not currently in the
      tree. If it is added later, this file must be disambiguated as
      the *hypothalamic* PVN. Do not merge.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/right/.
"""