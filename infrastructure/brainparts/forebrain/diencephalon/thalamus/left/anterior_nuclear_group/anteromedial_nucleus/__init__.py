"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.anterior_nuclear_group.anteromedial_nucleus
Anatomical Role:
    The left anteromedial nucleus (AM). The intermediate of the three
    left anterior thalamic nuclei, situated between the left
    anterodorsal (AD; head-direction) and the left anteroventral (AV;
    dominant memory relay) nuclei. It is a Papez-circuit memory relay:
    it receives mammillothalamic tract input from the left mammillary
    bodies and projects to the left cingulate and retrosplenial
    cortices.

    Unlike the AD (head-direction specialized) and the AV (the
    dominant memory relay with the densest mammillothalamic input),
    the AM is a SECONDARY MEMORY RELAY: it contributes to the same
    Papez memory circuit as the AV, but with less dense
    mammillothalamic input and smaller overall size. The AM's
    contribution is real but secondary to the AV's.

    The AM also has a distinctive VOICING-ADJACENT role: some
    functional imaging studies associate the AM with vocalization-
    adjacent and emotional-memory-related activity, but the evidence
    is thinner than for the AV's memory role. Document as a
    "secondary" contribution; do not overclaim.

    DISTINCTIONS (critical):

    - AM vs. AD (intra-group): the AM is a memory relay; the AD is
      the head-direction relay. Both receive mammillothalamic input
      and project to retrosplenial cortex, but their functional
      specializations differ (memory vs. spatial orientation). Do
      not merge.

    - AM vs. AV (intra-group): both are memory relays; the AV is the
      DOMINANT one (largest, densest mammillothalamic input, the
      primary Papez memory relay). The AM is SECONDARY. Do not merge;
      do not treat them as interchangeable memory relays.

    - AM vs. MEDIODORSAL NUCLEUS (MD; subtle): the AM is a
      PAPEZ-circuit memory relay (hippocampus → mammillary bodies →
      AM → cingulate); the MD (thalamus/left/medial_nuclear_group/
      medial_dorsal_nucleus/) is a PREFRONTAL relay (amygdala/PFC →
      MD → PFC). Different circuits; different nuclei; do not merge.

    - AM vs. ANTERIOR HYPOTHALAMIC NUCLEUS (the standard group
      trap): the AM is the anterior thalamic memory relay; the left
      anterior hypothalamic nucleus
      (hypothalamus/anterior/medial_area/left/anterior_hypothalamic_
      nucleus/) is the parasympathetic/thermoregulatory hub. Both are
      "anterior"; both are diencephalic; distinct structures. Do not
      merge.

Functional Mode:
    - Papez circuit memory relay (the anchor role; secondary to AV):
        * The AM receives mammillothalamic tract input from the left
          mammillary bodies and projects to the left cingulate and
          retrosplenial cortices, continuing the Papez memory signal
          to its cortical targets.
        * Its contribution is secondary to the AV's: the AV carries
          the densest mammillothalamic input and is the dominant
          relay; the AM contributes to the same circuit with less
          dense input.
    - Vocalization-adjacent / emotional memory (secondary): some
      functional imaging studies associate the AM with
      vocalization-adjacent activity and emotional memory content.
      The evidence is thinner than for the AV's memory role; document
      as a secondary contribution; do not overclaim.
    - The AM is therefore a SECONDARY Papez memory relay: its role is
      real (it contributes to the memory circuit) but subordinate to
      the AV's dominant role.

    - CLINICAL FACT (the AM's clinical anchor): the AM is one of the
      anterior thalamic nuclei, and its lesion contributes to the
      broader anterior-thalamic-amnesia picture (see the AV leaf for
      the "thalamic Korsakoff" framing). AM-SPECIFIC lesions are RARE
      because the AM is rarely affected in isolation; its clinical
      contribution is documented as part of the anterior thalamic
      memory system, not as a distinct AM-specific syndrome. This is
      the honest epistemic stance: do not claim an AM-specific
      clinical syndrome that the literature does not establish.

Hormonal Modulation (minimal; the AM is a secondary memory relay):
    - The AM is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) arousal inputs contribute to the attentional gating
      of the memory relay. Document as arousal modulation, not
      endocrine modulators.
    - The AM is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * episodic: the left AM relays the hippocampal episodic
          signal from the left mammillary bodies to the left cingulate
          and retrosplenial cortices. The memory content flows through
          the AM; it READS the memory signal from the mammillothalamic
          tract.
        * short_term: the current memory buffer being relayed.
        * temporal_sequence_learning: temporal order of events within
          an episode, as relayed via the mammillary bodies.
    - Writes: none directly. The AM is a RELAY, not an encoder;
      re-encoding happens in the cingulate and retrosplenial cortices.
      Same discipline as the mammillary bodies and the AV.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No AM fragment. The AM is a secondary memory relay; the model
      prompt does not need an anteromedial-nucleus block because the
      memory signals it relays are already represented in the upstream
      (mammillary bodies) and downstream (cingulate) fragments. The
      mammillary memory-relay fragment (with its confabulation
      guardrail) and the cortical memory signals carry the
      model-relevant state.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence.
    - The AM's clinical contribution (part of the anterior thalamic
      amnesia picture) is documented for completeness, but is not a
      prompt field.

Reciprocal Connections (left-side; the right side is in
../../../../right/anterior_nuclear_group/anteromedial_nucleus/):

    Papez circuit memory relay (the anchor):
    - ← hypothalamus/mammillary_bodies/left (via the left
      mammillothalamic tract; Papez memory relay; the mammillary leaf
      declares this edge from its side; this leaf CLOSES the AM's
      side of the mammillary → anterior thalamus deferred edge).
    - → telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      anterior_cingulate (AM → cingulate; the Papez cortical relay).
    - → telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      retrosplenial_cortex (AM → retrosplenial; the Papez cortical
      relay).
    - ← telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/hippocampus/left/subiculum (subicular
      input; the Papez circuit's hippocampal-mammillary input
      reaches the AM both via the mammillary bodies and directly
      from the subiculum).

    Intra-group:
    - ↔ ../anterodorsal_nucleus/ (adjacent; AD is head-direction;
      distinct specialization; do not merge).
    - ↔ ../anteroventral_nucleus/ (adjacent; AV is the dominant
      memory relay; the AM is secondary to the AV; do not merge; the
      AV/AM division of labor is density-based, not circuit-based —
      both carry Papez memory).

Notes:
    - Tier 1 full leaf (left). The AM is the SECONDARY Papez memory
      relay: real contribution, subordinate to the AV's dominant role.
    - AM vs. AV DISTINCTION: the AV is the dominant memory relay (largest,
      densest mammillothalamic input, the primary Papez relay); the AM
      is secondary. Do not treat them as interchangeable memory relays.
    - AM vs. AD DISTINCTION: the AD is the head-direction relay; the AM
      is memory. Same tract (mammillothalamic), same cortical targets
      (cingulate + retrosplenial), different specializations. Do not
      merge.
    - THE MAMMILLARY → AM DEFERRED EDGE CLOSURE: the mammillary bodies
      leaf declared the mammillothalamic tract edge to the AV/AM/AD
      collectively. The AV leaf will close the AV's side; the AD leaf
      closed the AD's side; THIS leaf closes the AM's side. With the
      three left leaves plus their right deltas, all three nuclei's
      sides of the mammillothalamic deferred edge will be closed.
    - CLINICAL FACT: the AM is part of the anterior thalamic amnesia
      system, but AM-SPECIFIC lesions are rare and AM-specific
      syndromes are not established. Document honestly; do not
      invent an AM-specific syndrome. The AV leaf carries the full
      "thalamic Korsakoff" framing (the dominant memory relay's
      lesion fact); this leaf references it and documents the AM's
      role as part of the broader picture.
    - The AM's "vocalization-adjacent" and "emotional memory" roles are
      documented as secondary and the evidence is thinner than the
      AV's memory role. Do not overclaim.
    - NO FRAGMENT: same as the whole thalamus. The AM is a relay, not
      a state-emitter.
    - The AM's memory interfaces (reads episodic, short_term,
      temporal_sequence_learning) are the same as the AV's, but
      secondary to the AV's role in the circuit. The AV is the dominant
      memory relay; the AM contributes.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (episodic, short_term,
      temporal_sequence_learning); gateway/.
    - Connects upward to diencephalon/thalamus/left/anterior_nuclear_
      group/.
"""