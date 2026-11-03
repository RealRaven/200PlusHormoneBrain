"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.suprachiasmatic_nucleus
Anatomical Role:
    Right hemisphere of the suprachiasmatic nucleus (SCN). The same
    master circadian pacemaker documented in ../left/, mirrored to the
    right hemisphere: a small paired nucleus with an endogenous ~24.2-
    hour oscillator, entrained primarily by light via the
    retinohypothalamic tract, and containing core (VIP/GRP) and shell
    (AVP) sub-populations. See ../left/__init__.py for the full
    anatomical description and the core/shell framing.

    Core/shell organization is documented WITHIN this file's parent
    (../left/__init__.py), not as child nodes. Do not create
    scc/ or shell/ children on the right either.

    Reproduced notes (apply equally on the right):
    - NO structural-identity trap: SCN is a single nucleus on both
      sides. Unlike the SON split or the LHA continuum, there is no
      "same structure split across compartments" issue. Do not invent
      one.
    - NO naming collision: "suprachiasmatic nucleus" is unambiguous.

Functional Mode:
    Same as ../left/. Endogenous rhythm generation; light entrainment
    via RHT; master output to hypothalamic and brainstem targets (SCN
    → PVN, pineal, PeN, LPO, LHA, arcuate, DMH, AHN, SCO); humoral
    output. No documented functional asymmetry between left and right
    SCN. Do not fabricate one.

Hormonal Modulation:
    Same as ../left/. Light resets phase (primary); melatonin modulates
    phase and gating; serotonin modulates phase (non-photic); estradiol
    gates the LH-surge output; glucocorticoids feed back on phase;
    orexin, ghrelin, and leptin modulate SCN response to arousal/
    metabolic cues. See ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    Same as ../left/, with one reproduced emphasis:
    - The SCN WRITES to temporal_sequence_learning: it maintains an
      internal temporal model (phase state, photoperiod estimate)
      updated by experience. This is the SCN's defining memory
      interface — unusual for a hub leaf, which normally only reads
      memory. Do not omit this write on the right.
    - Reads: temporal_sequence_learning, short_term, episodic. See
      ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The SCN's circadian phase and
    gating fragment (early-morning / mid-day / afternoon / evening /
    night / late-night; entrained; photoperiod; LH-surge gate;
    sleep-onset gate; arousal gate) is emitted once at the left/ level
    and represents the bilateral SCN. Emitting a separate right-side
    fragment would double-count the phase signal. See
    ../left/__init__.py § Model Integration.

    Reproduced FRAGMENT RELATIONSHIP RULES (mandatory for the
    implementer, applying identically on the right):
        (1) The SCN carries the master phase and gating signals; the
            pineal fragment (epithalamus/pineal_gland/) carries the
            melatonin readout. Complementary — SCN = clock, pineal =
            hormonal readout. Do not merge; do not double-count phase.
        (2) The SCN does NOT emit its own cortisol, LH, sleep, or
            autonomic fragments. Those are emitted by their respective
            downstream targets (PVN, PeN, LPO, PVN/AHN), each of which
            references the SCN's phase/gating state internally.
        (3) The SCN fragment is ALWAYS emitted (circadian phase is
            always defined), even at baseline. It is the canonical
            always-on fragment.

Right-specific reciprocal connections to enforce in Stage 4 (organized
by functional loop; do not duplicate the left-side edges in ../left/):

    Entrainment (input):
    - ← retina (retinohypothalamic tract; ipRGCs; glutamatergic; the
      right retina is a paired structure — verify hemisphere-split).
    - ← midbrain/.../intergeniculate_leaflet (non-photic phase-shift
      input; not currently a tree node — document as named relay).
    - ← brainstem/.../dorsal_raphe_nucleus (serotonergic non-photic
      input; raphe is midline).

    Endocrine output loops:
    - → hypothalamus/anterior/medial_area/right/paraventricular_nucleus
      (SCN → PVN → CRH and autonomic outflow; the SCN → PVN edge is
      the gateway to the cortisol peak and autonomic rhythms;
      right-side).
    - → epithalamus/pineal_gland (SCN → PVN → spinal cord → SCG →
      pineal → melatonin; canonical circadian loop; indirect;
      midline-adjacent — verify).
    - → lateral_area/right/periventricular_preoptic_nucleus (SCN → PeN
      vasopressin; LH-surge gating; right-side).

    Sleep and arousal output loops:
    - → lateral_area/right/preoptic_area/lateral_preoptic_nucleus
      (SCN → LPO; sleep-onset gating; right-side).
    - → lateral_area/right/anterior_part_of_lateral_nucleus (SCN → LHA
      orexin/MCH neurons; arousal and feeding gating; right-side).
    - → hypothalamus/tuberal/medial_area/right/arcuate_nucleus (SCN →
      arcuate; feeding rhythm gating; right-side).
    - → hypothalamus/tuberal/medial_area/right/
      dorsomedial_hypothalamic_nucleus (SCN → DMH; the principal relay
      for SCN output to feeding, temperature, and arousal; right-side).

    Adjacent structural connections:
    - ↔ hypothalamus/anterior/medial_area/right/
      anterior_hypothalamic_nucleus (SCN → AHN; circadian autonomic
      gating; right-side).
    - ↔ hypothalamus/subcommissural_organ (SCO; adjacent; TGF-β and
      CSF-flow circadian output; SCO is midline).
    - ↔ epithalamus/pineal_gland (feedback from melatonin; MT1/MT2
      receptors).

    Feedback (input):
    - ← epithalamus/pineal_gland (melatonin feedback; MT1/MT2; the
      pineal → SCN edge closes the bidirectional loop).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/amygdala (emotional/arousal context;
      indirect; right-side).
    - ← hypothalamus/tuberal/medial_area/right/arcuate_nucleus
      (ghrelin, leptin, metabolic cues; circadian-metabolic coupling;
      right-side).

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - This is the LAST content-complex delta in the medial area. After
      it, only the SON pair remains in the medial area — both short
      and mechanical.
    - The ALWAYS-ON fragment rule and the SCN-PINEAL COMPLEMENTARY rule
      are reproduced above because they are the two relationships that
      most affect how the model prompt is built. Do not remove them:
      a contributor entering at right/ must see them.
    - The SCN WRITES to temporal_sequence_learning is reproduced above
      because it is the SCN's defining memory interface and the only
      write of this kind in the tree. Do not omit it on the right.
    - Core/shell organization is documented within ../left/; do not
      create scc/ or shell/ children on the right either.
    - NO structural-identity trap and NO naming collision to reproduce
      (the SCN is a single, unambiguously named nucleus on both sides).
      The "no trap" notes are reproduced because a contributor
      entering at the right/ level should not pattern-match from
      other files and invent one.
    - Midline targets (dorsal raphe, pineal, SCO) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree. The retina
      is a paired structure — verify; the intergeniculate leaflet is
      currently not a tree node and is documented as a named relay in
      the SCN files. Right PVN, right PeN, right LPO, right LHA, right
      arcuate, right DMH, right AHN, right amygdala, and right arcuate
      are hemisphere-split and require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to hypothalamus/anterior/medial_area/right/.
"""