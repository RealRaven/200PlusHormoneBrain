"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.tuberal.medial_area.dorsomedial_hypothalamic_nucleus
Anatomical Role:
    The dorsomedial hypothalamic nucleus (DMH). A small, densely packed
    nucleus in the dorsomedial tuberal hypothalamus, situated dorsal to
    the ventromedial nucleus (VMH) and ventral to the dorsomedial
    aspect of the paraventricular nucleus. Its principal role is as the
    PRINCIPAL OUTPUT RELAY of the suprachiasmatic nucleus (SCN) to
    downstream circadian effectors:
        - Feeding rhythms.
        - Body temperature rhythms.
        - Sleep-wake rhythms.
        - Corticosterone rhythm (HPA circadian gating).
        - Locomotor activity rhythms.
    The DMH is NOT the master circadian clock (the SCN is); it is the
    principal neural RELAY between the SCN and the downstream circuits
    that express circadian rhythms in behavior and physiology.

    The DMH also contributes (secondary roles) to:
        - Stress responses (CRH-adjacent; DMH → PVN → HPA).
        - Defensive behavior (via projections to the PAG).
        - Thermogenesis (brown adipose tissue activation; secondary to
          the VMH's role).
        - Feeding (as a relay for SCN-gated feeding rhythms; secondary
          to the arcuate's first-order feeding populations).

    THREE TRAPS apply (reproduced from the parent tuberal/medial_area/
    container):

    - TRAP 4 (adjacent-nuclei trap): VMH vs. DMH. The ventromedial
      (VMH) and dorsomedial (DMH) nuclei are adjacent but functionally
      distinct. VMH = satiety, aggression, thermoregulation. DMH =
      circadian relay. Do not merge; do not treat as a pair of similar
      structures.

    - TRAP 5 (circadian-adjacent trap): DMH vs. posterior LHA. The DMH
      is the PRINCIPAL circadian relay (SCN → DMH → downstream); the
      posterior LHA segment 3 (posterior/lateral_area/left|right/
      posterior_part_of_lateral_nucleus/) is an orexin/MCH field
      segment that RECEIVES DMH input. Do not merge; the DMH is the
      relay, the posterior LHA is a downstream target segment.

    - TRAP 6 (relay-vs-clock trap): DMH vs. SCN. The SCN
      (anterior/medial_area/left|right/suprachiasmatic_nucleus/) is the
      MASTER CLOCK; the DMH is the PRINCIPAL OUTPUT RELAY. Do not draft
      the DMH as if it were the clock. The DMH leaf must reciprocate
      the SCN → DMH edge declared in the SCN leaf (the DEFERRED
      CLOSURE).

Functional Mode:
    - Circadian relay (primary function): the DMH receives direct
      projections from the SCN and relays circadian timing information
      to downstream hypothalamic and extrahypothalamic targets. The SCN
      → DMH projection is the anatomical basis for the circadian gating
      of feeding, body temperature, sleep-wake, corticosterone, and
      locomotor activity. The DMH is the single most important relay
      node for SCN output in the hypothalamus.
    - Feeding rhythm relay: the DMH relays SCN-gated circadian timing
      to feeding circuits (arcuate, LHA, PVN), producing the circadian
      rhythm of food intake (the "feeding rhythm"). The DMH → arcuate
      and DMH → LHA projections are the anatomical basis of this
      rhythm.
    - Temperature rhythm relay: the DMH relays SCN timing to
      thermoregulatory circuits (preoptic area, VMH), producing the
      circadian body temperature rhythm (lower at night, higher during
      the active phase).
    - Sleep-wake rhythm relay: the DMH relays SCN timing to the
      sleep-wake switch (LPO, TMN, orexin, LC, raphe), producing the
      circadian gating of sleep onset and wake.
    - Corticosterone rhythm relay: the DMH relays SCN timing to the
      PVN → CRH → ACTH → cortisol axis, producing the circadian
      cortisol rhythm (morning peak).
    - Stress and defensive behavior (secondary): the DMH contributes
      to acute stress responses and defensive behavior via projections
      to the PVN and the PAG. Secondary to the circadian relay role.
    - The DMH is therefore a RELAY, not an oscillator: it does not
      generate the ~24-hour rhythm itself; it transmits the SCN's
      rhythm to downstream effectors. Its functional identity is
      "the principal output relay of the master circadian clock."

Hormonal Modulation (container-level summary; full list in left/):
    - SCN input (SCN → DMH): the DMH's primary modulator. The SCN
      provides the circadian timing signal.
    - Melatonin (from the pineal, indirect feedback): modulates DMH
      activity through SCN-dependent and SCN-independent pathways.
    - Glucocorticoids (cortisol): feed back on DMH → PVN → HPA
      circadian gating; the DMH participates in the cortisol-rhythm
      loop.
    - Leptin (↑ DMH activity): the DMH integrates metabolic state
      with circadian timing; leptin's excitatory input is part of the
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

Memory Interfaces (container-level summary; full list in left/):
    - Reads: temporal_sequence_learning (the DMH's PRIMARY read — it
      relays SCN output and needs the circadian temporal sequence),
      short_term (current circadian phase, stress state, feeding
      state), episodic (circadian-disruption history, jet-lag
      history, shift-work history).
    - Writes: none directly. The DMH relays timing; it does not write
      stored content. (Note: the SCN writes to temporal_sequence_
      learning; the DMH reads it to relay.)
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - The container does not emit fragments itself. The DMH's
      contribution is a CONSTITUENT INPUT to the circadian aggregate
      that is emitted by the SCN:
        * The SCN's circadian fragment (emitted by
          anterior/medial_area/left|right/suprachiasmatic_nucleus/)
          carries the master phase and gating signals.
        * The DMH relays this timing to downstream effectors; its
          contribution is upstream modulation, not a separate
          fragment.
    - AGGREGATION RULE (mandatory): do NOT emit a separate DMH
      fragment. The DMH's downstream rhythms (feeding, temperature,
      sleep-wake, corticosterone) are documented in the downstream
      nuclei's fragments (arcuate feeding fragment, preoptic
      thermoregulatory fragment, sleep-wake switch fragments, PVN HPA
      fragment). The DMH supplies the circadian relay that gates them;
      it does not add its own circadian fragment.
    - Guardrails: the downstream fragments (feeding, thermoregulatory,
      sleep-wake, HPA) each carry their own "bias not impairment"
      clauses. The DMH does not add a new guardrail.

Children (one child pair — full leaf + delta):
    - left/    ★ FULL TIER 1 LEAF. The complete DMH content:
                 circadian relay role, the SCN → DMH → downstream
                 pathways (feeding, temperature, sleep-wake,
                 corticosterone, locomotor activity), the secondary
                 stress/defensive/thermogenic roles, all reciprocal
                 connections, and the DEFERRED CLOSURE of the SCN →
                 DMH edge.
    - right/   Delta mirror of left/, differing only in the right-side
                 reciprocal edges. No functional asymmetry documented.

Notes:
    - Tier 1 hub container. The full leaf lives in left/; right/ is a
      delta.
    - The DMH is marked ★ at the parent tuberal/medial_area/ and
      tuberal/ containers: it is the tertiary content hub of the
      tuberal division after the arcuate (★★) and VMH (★).
    - THREE TRAPS reproduced above (VMH-vs-DMH; DMH-vs-posterior-LHA;
      DMH-vs-SCN). All three apply to the DMH specifically. Do not
      omit any of them.
    - DEFERRED CLOSURE — SCN → DMH: this container names the deferred
      edge, and the left/ leaf closes it. The SCN leaf
      (anterior/medial_area/left|right/suprachiasmatic_nucleus/)
      declared "SCN → DMH; right-side split in right/" and "the DMH
      is the principal relay for SCN output to feeding, temperature,
      and arousal." The DMH leaf reciprocates this edge, closing the
      last remaining circadian loop deferred since the SCN pair.
    - The DMH is NOT the master clock; the SCN is. The DMH is the
      principal output relay. Do not draft the DMH as if it were the
      clock. This is Trap 6, and it is the most likely conflation
      (both are circadian-adjacent, both are in the hypothalamus, both
      are involved in circadian rhythms).
    - The DMH is NOT the posterior LHA segment 3. The DMH projects
      ONTO the posterior LHA (the DMH → posterior LHA arousal relay);
      the posterior LHA is a downstream target, not the relay itself.
    - The DMH is NOT the VMH. Adjacent but distinct (satiety/aggression/
      thermoregulation vs. circadian relay). Do not merge.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/04_* (satiety, leptin, ghrelin), 05_*
      (CRH-adjacent), 10_* (circadian, SCN, melatonin); memory/stores/
      (temporal_sequence_learning, short_term, episodic); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ anterior/medial_area/left|right/
          suprachiasmatic_nucleus (SCN → DMH; THE DEFERRED CLOSURE;
          SCN is midline-adjacent — verify).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ posterior/lateral_area/left|right/
          posterior_part_of_lateral_nucleus (DMH → posterior LHA;
          circadian-to-arousal gating; the posterior LHA reciprocates).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ tuberal/lateral_area/left|right/
          tuberal_part_of_lateral_nucleus (DMH → tuberal LHA;
          circadian-to-feeding-arousal gating; the tuberal LHA
          reciprocates).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ tuberal/medial_area/left|right/arcuate_nucleus
          (DMH → arcuate; circadian-gated feeding rhythm relay;
          adjacent tuberal nodes).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ anterior/medial_area/left|right/
          paraventricular_nucleus (DMH → PVN; circadian HPA gating
          and stress; the PVN reciprocates when drafted).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ anterior/medial_area/left|right/preoptic_area
          (DMH → preoptic; circadian body-temperature gating).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ lateral_area/left|right/preoptic_area/
          lateral_preoptic_nucleus (DMH → LPO; circadian sleep-onset
          gating).
        * tuberal/medial_area/left|right/dorsomedial_hypothalamic_
          nucleus ↔ midbrain/tegmentum/periaqueductal_gray (defensive
          behavior motor patterns; PAG is midline-adjacent — verify).
    - Connects upward to hypothalamus/tuberal/medial_area/.
"""