"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.anterior_hypothalamic_nucleus
Anatomical Role:
    Right hemisphere of the anterior hypothalamic nucleus (AHN). Same
    small, densely packed nucleus as ../left/, mirrored to the right
    hemisphere. Principal hypothalamic controller of parasympathetic
    outflow, thermoregulation, cardiovascular control, and an
    osmoregulatory contribution. Same adjacency to the preoptic area,
    same distinction from it. See ../left/__init__.py for the full
    anatomical description and the functional framing.

Functional Mode:
    Same as ../left/. Parasympathetic outflow (via DMV, NA), thermo-
    regulation, cardiovascular control (via NTS, RVLM), osmoregulatory
    contribution (via SON/PVN projections), and a minor arousal-modulation
    role. No documented functional asymmetry between left and right AHN.
    Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. Angiotensin II ↑ AHN activity (volume depletion);
    ANP ↓ AHN activity; PGE2 ↑ thermoregulatory drive; estradiol
    withdrawal ↑ thermal disruption; thyroid hormones modulate the
    thermoregulatory set-point. The AHN is primarily an autonomic
    output nucleus, not a target of most of the 12 axes. See
    ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (autonomic tone, thermal state),
    episodic (thermoregulatory/autonomic event history),
    emotional_valence (stress-arousal context), temporal_sequence_learning
    (circadian autonomic tone). Writes no stored content directly. See
    ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The thermoregulatory/autonomic
    fragment emitted by ../left/ represents the bilateral AHN and is
    aggregated at the anterior-division level together with the preoptic
    contributions. Emitting a separate right-side fragment would
    double-count the autonomic/thermal signal. See ../left/__init__.py
    § Model Integration (AGGREGATION RULE).

Right-specific reciprocal connections to enforce in Stage 4:
    - → hindbrain/myelencephalon/medulla_oblongata/cranial_nerve_nuclei/
      right/dorsal_motor_nucleus_vagus (parasympathetic outflow;
      excitatory; right-side projection).
    - → hindbrain/myelencephalon/medulla_oblongata/cranial_nerve_nuclei/
      right/nucleus_ambiguus (parasympathetic outflow; excitatory;
      right-side projection).
    - → hindbrain/myelencephalon/medulla_oblongata/solitary_nucleus
      (NTS; reciprocal autonomic feedback; NTS is midline-adjacent —
      verify).
    - → hindbrain/myelencephalon/medulla_oblongata/
      rostral_ventrolateral_medulla (RVLM; inhibitory; reduces
      sympathetic outflow; RVLM is midline-adjacent — verify).
    - ← lamina_terminalis/vascular_organ_of_lamina_terminalis (OVLT;
      angiotensin II input; OVLT is midline).
    - ← hypothalamus/subfornical_organ (SFO; angiotensin II input; SFO
      is midline).
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN; circadian autonomic gating; right SCN is midline-adjacent —
      verify).
    - ↔ hypothalamus/anterior/medial_area/right/supraoptic_nucleus
      (osmoregulatory cross-talk; right-side).
    - ↔ hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (autonomic co-regulation; right-side).
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area
      (thermoregulatory co-regulation; distinct but interacting;
      right-side).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - NO structural-identity trap: AHN is a single nucleus on both
      sides. Nothing to reproduce.
    - NO naming collision: "anterior hypothalamic nucleus" is
      unambiguous. Nothing to reproduce.
    - No hemisphere-specific fragment: the left-side thermoregulatory/
      autonomic fragment is bilateral and aggregated at the
      anterior-division level. Same convention as habenular_nuclei/
      right/ and the other deltas in this subtree.
    - Midline targets (NTS, RVLM, OVLT, SFO, SCN) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/right/.
"""