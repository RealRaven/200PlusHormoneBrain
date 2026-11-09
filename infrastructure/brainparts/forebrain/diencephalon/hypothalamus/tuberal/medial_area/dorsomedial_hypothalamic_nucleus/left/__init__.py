"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.dorsomedial_hypothalamic_nucleus.left
Anatomical Role:
    The left dorsomedial hypothalamic nucleus (DMH). A small, densely
    packed nucleus in the left dorsomedial tuberal hypothalamus,
    situated dorsal to the left VMH and ventral to the left PVN. Its
    principal role is as the PRINCIPAL OUTPUT RELAY of the left
    suprachiasmatic nucleus (SCN) to five downstream circadian
    effectors:
        (1) Feeding rhythms (DMH → arcuate → feeding circuits).
        (2) Body temperature rhythms (DMH → preoptic thermoregulatory
            circuits).
        (3) Sleep-wake rhythms (DMH → LPO / TMN / orexin / LC / raphe).
        (4) Corticosterone rhythm (DMH → PVN → CRH → ACTH → cortisol).
        (5) Locomotor activity rhythms (DMH → basal forebrain and
            downstream motor circuits).
    The DMH is NOT the master clock (the SCN is); it is the principal
    neural RELAY between the SCN and the downstream circuits that
    express circadian rhythms in behavior and physiology.

    SECONDARY ROLES (documented but not the file's anchor):
        - Stress responses (DMH → PVN → CRH; acute stress activation).
        - Defensive behavior (DMH → PAG; defensive motor patterns).
        - Thermogenesis (DMH → brown adipose tissue activation;
          secondary to the VMH's thermogenic role).
        - Feeding (as a circadian-gated relay to the arcuate; secondary
          to the arcuate's first-order feeding populations).
    The DMH is therefore a relay with five primary outputs and four
    secondary roles; the anchor is "the principal output relay of the
    master circadian clock."

    THREE TRAPS (reproduced from the parent tuberal/medial_area/
    container and the DMH hub container; each resolves a specific
    conflation risk):

    - TRAP 4: VMH vs. DMH (adjacent-nuclei trap). The left VMH
      (tuberal/medial_area/left/ventromedial_nucleus/) and the left
      DMH are adjacent but functionally distinct. VMH = satiety,
      aggression, thermoregulation. DMH = circadian relay. Do not
      merge; do not treat as a pair of similar structures.

    - TRAP 5: DMH vs. posterior LHA (circadian-adjacent trap). The DMH
      projects ONTO the left posterior LHA segment 3
      (posterior/lateral_area/left/posterior_part_of_lateral_nucleus/)
      as the circadian-to-arousal gating pathway. The posterior LHA is
      a DOWNSTREAM TARGET SEGMENT, not the relay itself. Do not merge.

    - TRAP 6: DMH vs. SCN (relay-vs-clock trap). The left SCN
      (anterior/medial_area/left/suprachiasmatic_nucleus/) is the
      MASTER CLOCK; the left DMH is the PRINCIPAL OUTPUT RELAY. The DMH
      does not generate the ~24-hour rhythm; it transmits the SCN's
      rhythm. This is the most likely conflation (both are
      circadian-adjacent, both are in the hypothalamus, both are
      involved in circadian rhythms). Do not draft the DMH as if it
      were the clock.

Functional Mode:
    - Circadian relay (primary function): the left DMH receives direct
      projections from the left SCN and relays circadian timing to five
      downstream hypothalamic and extrahypothalamic targets:
        * Feeding rhythm relay (DMH → left arcuate; DMH → left LHA):
          produces the circadian rhythm of food intake (higher during
          the active phase). The DMH → arcuate projection gates
          NPY/AgRP and POMC/CART activity to the circadian active
          phase, producing the daily feeding rhythm.
        * Temperature rhythm relay (DMH → left preoptic area; DMH →
          left VMH): produces the circadian body temperature rhythm
          (lower at night, higher during the active phase). The DMH →
          preoptic projection gates thermoregulatory circuits to the
          circadian cycle.
        * Sleep-wake rhythm relay (DMH → left LPO; DMH → left TMN; DMH
          → left orexin neurons; DMH → left LC/raphe): produces the
          circadian gating of sleep onset and wake. The DMH → sleep-
          wake switch projections are the anatomical basis of the
          circadian sleep-wake cycle.
        * Corticosterone rhythm relay (DMH → left PVN → CRH → ACTH →
          cortisol): produces the circadian cortisol rhythm (morning
          peak). The DMH → PVN projection is the anatomical basis of
          the circadian gating of the HPA axis.
        * Locomotor activity rhythm relay (DMH → left basal forebrain
          → downstream motor circuits): produces the circadian rhythm
          of locomotor activity.
    - Stress response (secondary): the left DMH is activated by acute
      stress and contributes to the stress-axis response via
      projections to the left PVN. Secondary to the circadian relay
      role.
    - Defensive behavior (secondary): the left DMH contributes to
      defensive behavior via projections to the left PAG
      (periaqueductal gray; midline-adjacent). Secondary to the
      circadian relay role.
    - Thermogenesis (secondary): the left DMH contributes to
      brown-adipose-tissue thermogenesis, secondary to the left VMH's
      primary thermogenic role.
    - The DMH is therefore a RELAY, not an oscillator: it does not
      generate the ~24-hour rhythm itself; it transmits the SCN's
      rhythm to downstream effectors. Its functional identity is
      "the principal output relay of the master circadian clock."

Hormonal Modulation:
    - SCN input (SCN → DMH): the DMH's primary modulator. The SCN
      provides the circadian timing signal via vasopressin, VIP, and
      other SCN output transmitters.
    - Melatonin (from the pineal, indirect feedback): modulates DMH
      activity through SCN-dependent and SCN-independent pathways. The
      pineal → melatonin → SCN → DMH pathway is the feedback loop.
    - Glucocorticoids (cortisol): feed back on the DMH → PVN → HPA
      circadian gating; the DMH participates in the cortisol-rhythm
      loop.
    - Leptin (↑ DMH activity): the DMH integrates metabolic state with
      circadian timing; leptin's excitatory input is part of the
      feeding-rhythm relay.
    - Ghrelin (↑ DMH activity): the fasting signal also modulates DMH
      activity, contributing to the circadian-feeding coupling.
    - CRH (stress input): the DMH is activated by acute stress and
      contributes to the stress-axis response.
    - Direction summary: SCN → DMH (circadian timing; the primary
      input); melatonin ↓ (indirect; feedback); leptin ↑ and ghrelin
      ↑ (metabolic-coupling inputs); CRH ↑ (stress). These are the
      actionable directions.
    - The DMH is primarily a RELAY: it does not produce a major
      neuroendocrine output of its own; its outputs are neural
      projections to downstream circadian effectors.

Memory Interfaces:
    - Reads:
        * temporal_sequence_learning: the DMH's PRIMARY read. The DMH
          relays the SCN's circadian timing; it needs the temporal
          sequence that the SCN writes. (Note: the SCN is one of the
          few regions that WRITES to temporal_sequence_learning; the
          DMH is the reader that consumes it. This is the
          SCN-writes/DMH-reads relationship — the complementary
          memory pattern of the circadian relay.)
        * short_term: current circadian phase, stress state, and
          feeding state buffers. The DMH's downstream relays depend on
          these.
        * episodic: circadian-disruption history (jet lag, shift work,
          seasonal change), used to set circadian phase thresholds.
    - Writes: none directly. The DMH relays timing; it does not write
      stored content. The SCN writes to temporal_sequence_learning; the
      DMH reads it and relays the timing to downstream effectors.
    - The DMH has no other memory interfaces; do not invent them. It is
      a relay, not a stored-content region.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No independent prompt fragment. The DMH's contribution is
      UPSTREAM MODULATION of the SCN's circadian fragment. The SCN's
      fragment (emitted by
      anterior/medial_area/left/suprachiasmatic_nucleus/) carries the
      master phase and gating signals; the DMH relays them to
      downstream effectors.
    - AGGREGATION RULE (mandatory for the implementer): do NOT emit a
      separate DMH fragment. The DMH's downstream rhythms (feeding,
      temperature, sleep-wake, corticosterone) are documented in the
      downstream nuclei's fragments (arcuate feeding fragment,
      preoptic thermoregulatory fragment, sleep-wake switch fragments,
      PVN HPA fragment). The DMH supplies the circadian relay that
      gates them; it does not add its own circadian fragment. Emitting
      a DMH fragment would double-count the circadian signal already
      carried by the SCN and the downstream fragments.
    - The DMH is a RELAY: it does not emit a signal, it relays one.
      The model prompt does not need a DMH block.
    - Guardrails: the downstream fragments (feeding, thermoregulatory,
      sleep-wake, HPA) each carry their own "bias not impairment"
      clauses. The DMH does not add a new guardrail.
    - No multimodal input is consumed here; the DMH's contribution is
      via its downstream targets' text-only fragments.

Reciprocal Connections (left-side; the right side is in ../right/):

    Circadian relay — primary (SCN input, five downstream relays):
    - ← anterior/medial_area/left/suprachiasmatic_nucleus (SCN → DMH;
      THE DEFERRED CLOSURE — the SCN leaf declared "SCN → DMH; the DMH
      is the principal relay for SCN output to feeding, temperature,
      and arousal"; this leaf closes it; SCN is midline-adjacent —
      verify).
    - → tuberal/medial_area/left/arcuate_nucleus (DMH → arcuate;
      circadian-gated feeding rhythm relay; left-side).
    - → tuberal/lateral_area/left/tuberal_part_of_lateral_nucleus
      (DMH → tuberal LHA segment 2; circadian-to-feeding-arousal
      gating; left-side).
    - → posterior/lateral_area/left/posterior_part_of_lateral_nucleus
      (DMH → posterior LHA segment 3; circadian-to-arousal gating;
      left-side).
    - → anterior/medial_area/left/preoptic_area (DMH → preoptic;
      circadian body-temperature gating; left-side).
    - → lateral_area/left/preoptic_area/lateral_preoptic_nucleus
      (DMH → LPO; circadian sleep-onset gating; left-side).
    - → hypothalamus/tuber_cinereum/left/tuberomammillary_nucleus
      (DMH → TMN; circadian wake-gating; left-side).
    - → anterior/lateral_area/left/anterior_part_of_lateral_nucleus
      (DMH → orexin neurons; circadian arousal gating; left-side).
    - → anterior/medial_area/left/paraventricular_nucleus (DMH → PVN;
      circadian HPA gating; left-side).
    - → telencephalon/cerebral_hemispheres/left/subcortical/
      basal_forebrain (DMH → basal forebrain; circadian locomotor
      activity relay; left-side).

    Secondary roles:
    - → anterior/medial_area/left/paraventricular_nucleus (DMH → PVN;
      stress activation; secondary to the circadian HPA gating edge
      above; same target, different functional context).
    - → midbrain/tegmentum/periaqueductal_gray (DMH → PAG; defensive
      behavior motor patterns; PAG is midline-adjacent — verify).
    - → left brown adipose tissue sympathetic circuit (DMH →
      thermogenesis; secondary to the VMH's primary thermogenic role;
      the sympathetic preganglionic pathway is downstream of the
      dorsal motor nucleus — verify).

    Adjacency (not signaling):
    - ↔ tuberal/medial_area/left/ventromedial_nucleus (adjacent tuberal
      nuclei; VMH = satiety/aggression/thermoregulation; DMH =
      circadian relay; do not merge; the VMH reciprocates when
      drafted).

Notes:
    - Tier 1 full leaf (left). The full DMH content. right/ is a
      delta.
    - THE DEFERRED CLOSURE — SCN → DMH: this leaf closes the edge
      declared in anterior/medial_area/left/suprachiasmatic_nucleus/.
      It is the LAST remaining circadian closure in the entire
      hypothalamus subtree. After this leaf and its right delta, every
      circadian loop declared from pineal_gland/ through SCN →
      downstream is fully closed on both hemispheres.
    - The DMH is a RELAY, not an oscillator. Do not draft it as if it
      were the clock. Trap 6 is the most likely conflation.
    - THE THREE TRAPS reproduced in full above (VMH vs. DMH; DMH vs.
      posterior LHA; DMH vs. SCN). Trap 6 is the newest and most
      important; do not remove it.
    - The SCN-writes/DMH-reads memory pattern is the circadian relay's
      defining memory feature. The SCN is one of the few regions that
      WRITES to temporal_sequence_learning; the DMH is the reader
      that consumes it and relays the timing. This is a complementary
      pattern, not a duplicate; do not draft the DMH as writing to
      temporal_sequence_learning (the SCN writes; the DMH reads).
    - No independent fragment: the DMH is upstream modulation of the
      SCN's fragment. Stated explicitly in the Model Integration
      section.
    - The five primary relays (feeding, temperature, sleep-wake,
      corticosterone, locomotor activity) are the DMH's anchor content.
      The four secondary roles (stress, defensive, thermogenic,
      feeding-as-relay) are documented but not the anchor.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/02_* (HPA, CRH, cortisol), 04_* (satiety,
      leptin, ghrelin), 05_* (CRH-adjacent, PAG-adjacent), 10_*
      (circadian, SCN, melatonin); memory/stores/
      (temporal_sequence_learning, short_term, episodic); gateway/.
    - Connects upward to hypothalamus/tuberal/medial_area/
      dorsomedial_hypothalamic_nucleus/.
"""