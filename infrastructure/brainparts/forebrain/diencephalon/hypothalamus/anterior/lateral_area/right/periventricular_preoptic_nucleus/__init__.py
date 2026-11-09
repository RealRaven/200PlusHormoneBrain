"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.lateral_area.right.periventricular_preoptic_nucleus
Anatomical Role:
    Right hemisphere of the periventricular preoptic nucleus (PeN). The
    same tri-modal population documented in ../left/, mirrored to the
    right hemisphere: kisspeptin/GnRH-regulatory neurons, sleep-promoting
    GABAergic/galaninergic neurons, and thermoregulatory neurons. See
    ../left/__init__.py for the full anatomical description and the
    tri-modal framing.

    Reproduced naming note (applies equally on the right):
    DISTINCTION FROM AVPV — this node is the periventricular preoptic
    nucleus, adjacent to but distinct from the anteroventral
    periventricular nucleus (AVPV). The literature often groups them as
    "AVPV/PeN"; this tree treats them as separate nodes. When the AVPV is
    drafted, both files must declare a reciprocal continuity edge — not
    a duplicate-structure warning. Adjacent kisspeptin populations, not
    one split nucleus.

Functional Mode:
    Same as ../left/. GnRH pulse generation (basal), GnRH surge generation
    (estrogen positive feedback, SCN-gated), sleep promotion via inhibition
    of histaminergic and brainstem arousal centers, and thermoregulation.
    No documented functional asymmetry between left and right PeN. Do not
    fabricate one.

Hormonal Modulation:
    Same as ../left/. Estradiol ↑ KP activity (surge); SCN vasopressin ↑
    gating (time-locked); PGE2 ↑ heat-loss; GABA ↑ sleep. See
    ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (estradiol, circadian phase, sleep
    pressure), temporal_sequence_learning (SCN-gated time-of-day),
    episodic (cycle/sleep history), emotional_valence (stress suppression
    of GnRH). Writes no stored content directly. See ../left/__init__.py
    § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No hemisphere-specific prompt fragment. The PeN fragment (reproductive
    mode, estradiol feedback, GnRH pulse state, circadian gate, sleep
    drive, thermal state) is emitted once at the left/ level and
    represents the bilateral nucleus. Emitting a separate right-side
    fragment would double-count the reproductive/sleep/thermal signal.
    See ../left/__init__.py § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:
    - → preoptic GnRH neuron population (KP → GnRH; excitatory;
      right-side projection).
    - ← hypothalamus/anterior/medial_area/right/suprachiasmatic_nucleus
      (SCN → PeN vasopressinergic input; circadian gating; right SCN
      is midline-adjacent — verify).
    - ↔ hypothalamus/tuberal/medial_area/right/arcuate_nucleus (KNDy
      kisspeptin population; reciprocal kisspeptin network; right-side).
    - → hindbrain/metencephalon/pons/tegmentum/locus_coeruleus
      (PeN → LC; inhibitory; sleep promotion; LC is midline-adjacent —
      verify).
    - → hindbrain/.../tuberomammillary_nucleus (PeN → TMN; inhibitory;
      sleep promotion; TMN is midline-adjacent — verify).
    - → brainstem cholinergic arousal centers (PeN → LDT/PPN;
      inhibitory; sleep promotion; both are midline-adjacent — verify).
    - ↔ hypothalamus/anterior/medial_area/right/preoptic_area (adjacent
      thermoregulatory and sleep circuitry; right-side).
    - ↔ anteroventral periventricular nucleus right-side portion (AVPV;
      adjacent kisspeptin population; continuity edge, not
      duplicate-structure warning).
    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - No structural-identity warning to reproduce: unlike the supraoptic
      split or the LHA continuum, PeN is a single nucleus on both sides.
      The AVPV relationship is a continuity edge, not a split-structure
      trap. Do not invent a structural warning for this file.
    - No hemisphere-specific fragment: the left-side fragment is
      bilateral. Same convention as habenular_nuclei/right/ and the other
      deltas in this subtree.
    - Midline targets (SCN, LC, TMN, LDT, PPN, AVPV) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on structures
      that are not hemisphere-split in the tree.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/lateral_area/right/.
"""