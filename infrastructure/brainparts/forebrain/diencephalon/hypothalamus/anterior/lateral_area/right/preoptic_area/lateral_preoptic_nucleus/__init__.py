"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.right.preoptic_area.lateral_preoptic_nucleus
Anatomical Role:
    Right hemisphere of the lateral preoptic nucleus (LPO). Same
    sleep-active GABAergic/galaninergic populations as ../left/ (VLPO
    and MnPO sleep-active neurons, VLPO-adjacent), mirrored to the right
    hemisphere. See ../left/__init__.py for the full anatomical
    description, the sleep-switch framing, and the reciprocal inhibition
    of every major arousal system.

    Reproduced critical warning (applies equally on the right):
    PREOPTIC NAMING COLLISION — this node is the LATERAL preoptic
    nucleus, distinct from
    medial_area/right/preoptic_area/medial_preoptic_nucleus/ (the MEDIAL
    preoptic nucleus, MPN, involved in maternal behavior, sexual
    behavior, and GnRH regulation). Do not merge.

    Reproduced naming disambiguation (applies equally on the right):
    MnPO — the "median preoptic nucleus" referenced here is the
    sleep-active population in the ventrolateral preoptic region, NOT
    the "median preoptic nucleus" that appears in the medial preoptic
    area's GnRH circuitry. Two different structures share the acronym;
    the tree distinguishes them by location.

Functional Mode:
    Same as ../left/. Sleep promotion via reciprocal inhibition of every
    major arousal system (TMN, LC, raphe, LDT/PPN, orexin neurons),
    sleep consolidation (VLPO), sleep onset (MnPO), thermoregulation,
    and adenosine integration. No documented functional asymmetry
    between left and right LPO. Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. Adenosine ↑ LPO activity; GABA/galanin promote
    LPO output; PGD2 ↑ sleep; estradiol withdrawal ↑ thermal
    disruption; orexin ↓ LPO activity; SCN circadian gating. See
    ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (sleep pressure, thermal state),
    temporal_sequence_learning (circadian sleep window), episodic
    (sleep history), emotional_valence (stress suppression of sleep).
    Writes no stored content directly. See ../left/__init__.py
    § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No hemisphere-specific prompt fragment. The sleep-state fragment
    (sleep drive, adenosine pressure, sleep-wake mode, thermal state,
    arousal-system suppression, and the guardrail against treating
    high sleep drive as impairment) is emitted once at the left/ level
    and represents the bilateral LPO. Emitting a separate right-side
    fragment would double-count the sleep signal. See
    ../left/__init__.py § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:
    - → hindbrain/.../tuberomammillary_nucleus (LPO → TMN; inhibitory;
      right-side projection; TMN is midline-adjacent — verify).
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus
      (LPO → LC; inhibitory; right-side projection; LC is
      midline-adjacent — verify).
    - → midbrain/tegmentum/dorsal_raphe_nucleus (LPO → raphe;
      inhibitory; raphe is midline).
    - → midbrain/tegmentum/laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (LPO → LDT/PPN; inhibitory; both are
      midline-adjacent — verify).
    - → hypothalamus/anterior/lateral_area/right/
      anterior_part_of_lateral_nucleus (LPO → orexin neurons;
      inhibitory; reciprocal sleep-wake switch; right-side).
    - ← hypothalamus/anterior/lateral_area/right/
      anterior_part_of_lateral_nucleus (orexin → LPO; inhibitory;
      reciprocal antagonism; right-side).
    - ← hypothalamus/anterior/medial_area/right/
      suprachiasmatic_nucleus (SCN → LPO; circadian sleep gating;
      right SCN is midline-adjacent — verify).
    - ← hypothalamus/anterior/medial_area/right/supraoptic_nucleus and
      paraventricular_nucleus (CRH/stress → LPO; stress-induced
      insomnia; right-side).
    - ↔ hypothalamus/anterior/lateral_area/right/
      periventricular_preoptic_nucleus/ (adjacent sleep-active
      population; continuity edge, not duplicate-structure warning;
      right-side).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - Both naming traps (preoptic collision, MnPO disambiguation) are
      reproduced above because they are structural traps that apply on
      both hemispheres. The full anatomical, functional, hormonal, and
      memory content is referenced rather than duplicated.
    - No hemisphere-specific fragment: the left-side sleep fragment is
      bilateral. Same convention as habenular_nuclei/right/ and the
      other deltas in this subtree.
    - Midline targets (TMN, LC, raphe, LDT, PPN, SCN) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree.
    - The mutual-inhibition edge with orexin neurons is bilateral; both
      directions are listed here so the reciprocal edge resolves on
      the right side. The left-side edge is in ../left/__init__.py.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/lateral_area/right/
      preoptic_area/.
"""