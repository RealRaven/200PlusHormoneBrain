"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.dorsomedial_hypothalamic_nucleus.right
Anatomical Role:
    Right dorsomedial hypothalamic nucleus (DMH). Same small, densely
    packed nucleus in the right dorsomedial tuberal hypothalamus
    documented in ../left/, with the same principal role as the
    PRINCIPAL OUTPUT RELAY of the right SCN to five downstream
    circadian effectors:
        (1) Feeding rhythms (DMH → arcuate).
        (2) Body temperature rhythms (DMH → preoptic area; DMH → VMH).
        (3) Sleep-wake rhythms (DMH → LPO; DMH → TMN; DMH → orexin
            neurons; DMH → LC/raphe).
        (4) Corticosterone rhythm (DMH → PVN → CRH → ACTH → cortisol).
        (5) Locomotor activity rhythms (DMH → basal forebrain).
    See ../left/__init__.py for the full anatomical description, the
    five-relay anchor, the four secondary roles, the complete
    hormonal-modulation list, and the SCN-writes/DMH-reads memory
    pattern.

    Reproduced THREE TRAPS (apply equally on the right):
    - TRAP 4: right VMH vs. right DMH (adjacent-nuclei trap; VMH =
      satiety/aggression/thermoregulation; DMH = circadian relay; do
      not merge).
    - TRAP 5: right DMH vs. right posterior LHA segment 3
      (circadian-adjacent trap; the DMH projects ONTO the posterior
      LHA as a downstream target, not the relay itself; do not merge).
    - TRAP 6: right DMH vs. right SCN (relay-vs-clock trap; the SCN
      is the master clock; the DMH is the principal output relay; the
      DMH does not generate the ~24-hour rhythm itself; do not draft
      the DMH as if it were the clock).

Functional Mode:
    Same as ../left/. Circadian relay (primary function); five
    downstream relays (feeding, temperature, sleep-wake, corticosterone,
    locomotor activity); four secondary roles (stress, defensive
    behavior, thermogenesis, feeding-as-relay). The DMH is a RELAY,
    not an oscillator. No documented functional asymmetry between left
    and right DMH. Do not fabricate one. See ../left/ § Functional
    Mode.

Hormonal Modulation:
    Same as ../left/. SCN → DMH (circadian timing; the primary input);
    melatonin ↓ (indirect feedback); leptin ↑ and ghrelin ↑
    (metabolic-coupling); CRH ↑ (stress). See ../left/ § Hormonal
    Modulation.

Memory Interfaces:
    Same as ../left/. Reads temporal_sequence_learning (the DMH's
    primary read — it relays the SCN's timing); short_term (circadian
    phase, stress, feeding state); episodic (circadian-disruption
    history). Writes nothing directly. The SCN-writes/DMH-reads pattern
    applies on the right identically: the right SCN writes to
    temporal_sequence_learning; the right DMH reads it and relays the
    timing. Do not draft the right DMH as writing. See ../left/
    § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No independent prompt fragment. The DMH's contribution is upstream
    modulation of the SCN's circadian fragment. The SCN's fragment
    (emitted by anterior/medial_area/right/suprachiasmatic_nucleus/)
    carries the master phase and gating signals; the DMH relays them to
    downstream effectors. AGGREGATION RULE (mandatory, applies
    identically on the right): do NOT emit a separate DMH fragment.
    The downstream rhythms (feeding, temperature, sleep-wake,
    corticosterone) are documented in the downstream nuclei's
    fragments; the DMH supplies the relay that gates them. See
    ../left/ § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:

    Circadian relay — primary (SCN input, five downstream relays):
    - ← anterior/medial_area/right/suprachiasmatic_nucleus (SCN → DMH;
      THE DEFERRED CLOSURE ON THE RIGHT; SCN is midline-adjacent —
      verify).
    - → tuberal/medial_area/right/arcuate_nucleus (DMH → arcuate;
      circadian-gated feeding rhythm relay; right-side).
    - → tuberal/lateral_area/right/tuberal_part_of_lateral_nucleus
      (DMH → tuberal LHA segment 2; circadian-to-feeding-arousal
      gating; right-side).
    - → posterior/lateral_area/right/posterior_part_of_lateral_nucleus
      (DMH → posterior LHA segment 3; circadian-to-arousal gating;
      right-side).
    - → anterior/medial_area/right/preoptic_area (DMH → preoptic;
      circadian body-temperature gating; right-side).
    - → lateral_area/right/preoptic_area/lateral_preoptic_nucleus
      (DMH → LPO; circadian sleep-onset gating; right-side).
    - → hypothalamus/tuber_cinereum/right/tuberomammillary_nucleus
      (DMH → TMN; circadian wake-gating; right-side).
    - → anterior/lateral_area/right/anterior_part_of_lateral_nucleus
      (DMH → orexin neurons; circadian arousal gating; right-side).
    - → anterior/medial_area/right/paraventricular_nucleus (DMH → PVN;
      circadian HPA gating; right-side).
    - → telencephalon/cerebral_hemispheres/right/subcortical/
      basal_forebrain (DMH → basal forebrain; circadian locomotor
      activity relay; right-side).

    Secondary roles:
    - → anterior/medial_area/right/paraventricular_nucleus (DMH → PVN;
      stress activation; same target as the HPA-gating edge above,
      different functional context).
    - → midbrain/tegmentum/periaqueductal_gray (DMH → PAG; defensive
      behavior motor patterns; PAG is midline-adjacent — verify).
    - → right brown adipose tissue sympathetic circuit (DMH →
      thermogenesis; secondary to the right VMH's primary thermogenic
      role; sympathetic preganglionic pathway downstream of the dorsal
      motor nucleus — verify).

    Adjacency (not signaling):
    - ↔ tuberal/medial_area/right/ventromedial_nucleus (adjacent tuberal
      nuclei; VMH = satiety/aggression/thermoregulation; DMH =
      circadian relay; do not merge).

    - ↔ ../left/ (hemisphere counterpart; no functional asymmetry
      assumed).

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - THE DEFERRED CLOSURE — SCN → DMH — IS NOW COMPLETE ON BOTH
      HEMISPHERES: the left leaf closed the left side; this delta
      closes the right side. The SCN → DMH edge that has been pending
      since anterior/medial_area/left/suprachiasmatic_nucleus/ was
      drafted is now fully resolved.
    - ALL CIRCADIAN LOOPS IN THE ENTIRE TREE ARE NOW CLOSED ON BOTH
      HEMISPHERES. The ten loops declared over the entire project
      (SCN → pineal, SCN → PVN → cortisol, SCN → PeN → LH surge,
      SCN → LPO → sleep, SCN → LHA → arousal, SCN → arcuate → feeding,
      SCN → DMH → five relays, SCN ↔ SCO, SCN → AHN → autonomic,
      pineal → SCN feedback) are all fully closed. This is the last
      circadian closure in the entire tree.
    - All three traps (VMH vs. DMH; DMH vs. posterior LHA; DMH vs.
      SCN) are reproduced in abbreviated form above; the full text is
      in ../left/ and the parent hub container. Trap 6 (relay-vs-clock)
      is the most important and applies equally on the right.
    - The DMH is a RELAY, not an oscillator. Do not draft it as if it
      were the clock. The right DMH relays the right SCN's rhythm; it
      does not generate it.
    - The SCN-writes/DMH-reads memory pattern applies on the right
      identically: the right SCN writes to temporal_sequence_learning;
      the right DMH reads it. Do not draft the right DMH as writing.
    - No independent fragment: the DMH is upstream modulation of the
      SCN's fragment. Same AGGREGATION RULE as ../left/.
    - Midline targets (SCN, PAG) are flagged with "verify" so Stage 4
      does not force a hemisphere split on structures that are not
      hemisphere-split in the tree. Right arcuate, right tuberal LHA,
      right posterior LHA, right preoptic area, right LPO, right TMN,
      right orexin neurons, right PVN, right basal forebrain, right
      VMH, and right brown adipose sympathetic circuit are
      hemisphere-split and require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see ../left/
      § Notes for the full list.
    - Connects upward to hypothalamus/tuberal/medial_area/
      dorsomedial_hypothalamic_nucleus/.
"""