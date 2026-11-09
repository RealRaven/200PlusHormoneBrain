"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.anterior_nuclear_group.anteroventral_nucleus
Anatomical Role:
    The left anteroventral nucleus (AV). The LARGEST of the three left
    anterior thalamic nuclei, situated at the ventral-anterior pole of
    the left anterior nuclear group, adjacent to the left
    anteromedial (AM) nucleus and to the left third ventricle. It is
    the DOMINANT MEMORY RELAY of the Papez circuit: it receives the
    DENSEST mammillothalamic tract input from the left mammillary
    bodies, projects densely to the left cingulate and retrosplenial
    cortices, and carries the primary episodic-memory relay of the
    group.

    Among the three anterior nuclei:
        - AD (smallest): head-direction relay (presubicular input).
        - AM (intermediate): secondary Papez memory relay (moderate
          mammillothalamic input).
        - AV (largest; THIS LEAF): DOMINANT Papez memory relay
          (densest mammillothalamic input; the primary memory relay of
          the anterior group).

    The AV is the anterior nuclear group's ANCHOR: it is the nucleus
    that gives the group its memory identity, the nucleus most
    consistently studied in the Papez circuit literature, and the
    nucleus that carries the group's defining clinical syndrome
    (thalamic Korsakoff).

    DISTINCTIONS (critical):

    - AV vs. AM (intra-group): both are memory relays; the AV is
      DOMINANT (largest, densest mammillothalamic input, the primary
      Papez memory relay); the AM is SECONDARY. Do not treat them as
      interchangeable; the AV is the anchor.

    - AV vs. AD (intra-group): the AV is the memory relay; the AD is
      the head-direction relay. Same tract (mammillothalamic), same
      cortical targets (cingulate + retrosplenial), different
      specializations. Do not merge.

    - AV vs. MEDIODORSAL NUCLEUS (MD; subtle): both are memory-related
      thalamic relays. The AV is the PAPEZ-circular memory relay
      (hippocampus → mammillary bodies → AV → cingulate); the MD
      (thalamus/left/medial_nuclear_group/medial_dorsal_nucleus/) is
      the PREFRONTAL relay (amygdala/PFC → MD → PFC). Different
      circuits; different nuclei; do not merge.

    - AV vs. ANTERIOR HYPOTHALAMIC NUCLEUS (the standard group trap):
      the AV is the anterior thalamic memory relay; the left anterior
      hypothalamic nucleus
      (hypothalamus/anterior/medial_area/left/anterior_hypothalamic_
      nucleus/) is the parasympathetic/thermoregulatory hub. Both are
      "anterior"; both are diencephalic; distinct structures. Do not
      merge.

Functional Mode:
    - Papez circuit memory relay (the AV's anchor; the group's
      dominant memory relay):
        * The AV receives the DENSEST mammillothalamic tract input
          from the left mammillary bodies (of the three anterior
          nuclei, the AV has the strongest mammillothalamic input).
        * The AV projects densely to the left cingulate cortex
          (anterior cingulate) and the left retrosplenial cortex —
          the Papez circuit's cortical targets.
        * The full Papez circuit through the AV:
            hippocampus → fornix → mammillary bodies →
            mammillothalamic tract → AV → cingulate cortex and
            retrosplenial cortex → parahippocampal gyrus → entorhinal
            cortex → hippocampus.
          The AV is the required thalamic relay: without it, the
          hippocampal-mammillary memory signal cannot reach the
          cingulate cortex, and episodic memory consolidation fails
          (see the clinical fact).
        * The AV also receives subicular input directly (in addition
          to the mammillary relay), giving it a second source of
          hippocampal memory signal.
    - Episodic memory consolidation (the functional consequence): the
      AV's relay is required for the consolidation of episodic memory
      — the process by which a short-term experience becomes a
      durable long-term memory. The AV is one of the nodes whose
      integrity is necessary for this consolidation.
    - Spatial memory (secondary): the AV contributes to spatial
      memory consolidation via the same Papez circuit, alongside its
      episodic memory role. The AD's head-direction role is spatial;
      the AV's role is memory (both episodic and spatial).
    - CLINICAL FACT (the AV's defining clinical anchor; THE GROUP'S
      DEFINING SYNDROME):
        * ANTERIOR THALAMIC AMNESIA / THALAMIC KORSAKOFF: lesions of
          the anterior thalamic nuclei (including the AV), or of the
          mammillothalamic tract that feeds them, produce
          ANTEROGRADE AMNESIA — the inability to form new episodic
          memories — often with CONFABULATION (the fabrication of
          plausible but false memories).
        * The syndrome is functionally IDENTICAL to hypothalamic
          Korsakoff (from mammillary body lesions): same clinical
          picture (anterograde amnesia + confabulation + preserved
          procedural memory), different anatomical site (one synapse
          downstream in the Papez circuit). The mammillary body is
          the hypothalamic site; the AV is the thalamic site; the
          mammillothalamic tract connects them. Lesions at any of the
          three sites produce the same syndrome.
        * The "thalamic Korsakoff" framing is the AV's specific
          clinical contribution to the group: the AV is the nucleus
          that carries the group's defining clinical signature.
        * This is the thalamic counterpart of the hypothalamic
          Korsakoff documented in the mammillary bodies leaf
          (hypothalamus/mammillary_bodies/left/ § Functional Mode).
          The two leaves together document the full Korsakoff circuit:
          mammillary bodies (hypothalamic site) + mammillothalamic
          tract + AV (thalamic site).
    - The AV is therefore the anterior nuclear group's MEMORY ANCHOR
      and CLINICAL ANCHOR: it is the dominant memory relay, and its
      lesion produces the group's defining syndrome (thalamic
      Korsakoff).

Hormonal Modulation (minimal; the AV is a memory relay):
    - The AV is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) arousal inputs contribute to the attentional gating
      of the memory relay. The cholinergic basal forebrain input is
      particularly relevant to memory (the basal forebrain cholinergic
      system is a memory-modulating system). Document as arousal and
      memory-modulatory input, not endocrine modulators.
    - The AV is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * episodic: the AV relays the hippocampal episodic signal from
          the left mammillary bodies to the left cingulate and
          retrosplenial cortices. The memory content flows through the
          AV; it READS the memory signal from the mammillothalamic
          tract.
        * short_term: the current memory buffer being relayed.
        * temporal_sequence_learning: temporal order of events within
          an episode, as relayed via the mammillary bodies.
        * episodic: the AV also receives direct subicular input, a
          second source of the hippocampal episodic signal.
    - Writes: none directly. The AV is a RELAY, not an encoder;
      re-encoding happens in the cingulate and retrosplenial cortices.
      Same discipline as the mammillary bodies and the AM.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No AV fragment. The AV is a memory relay; the model prompt does
      not need an anteroventral-nucleus block because the memory
      signals it relays are already represented in the upstream
      (mammillary bodies) and downstream (cingulate) fragments. The
      mammillary memory-relay fragment (with its confabulation
      guardrail) and the cortical memory signals carry the
      model-relevant state.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence.
    - The AV's clinical fact (thalamic Korsakoff) is documented for
      completeness, but is not a prompt field. The memory-failure
      guardrail for the thalamic relay is inherited from the
      mammillary bodies' fragment ("do not confabulate missing
      details"), not added here.

Reciprocal Connections (left-side; the right side is in
../../../../right/anterior_nuclear_group/anteroventral_nucleus/):

    Papez circuit memory relay (the anchor; DOMINANT):
    - ← hypothalamus/mammillary_bodies/left (via the left
      mammillothalamic tract; Papez memory relay; the DENSEST
      mammillothalamic input of the three anterior nuclei; THE
      DEFERRED SUB-EDGE CLOSED HERE — the final mammillothalamic
      sub-edge; the mammillary leaf declares this edge from its
      side).
    - → telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      anterior_cingulate (AV → cingulate; the Papez cortical relay;
      dense).
    - → telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      retrosplenial_cortex (AV → retrosplenial; the Papez cortical
      relay; dense).
    - ← telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/hippocampus/left/subiculum (subicular
      input; the second source of hippocampal memory signal).

    Intra-group:
    - ↔ ../anterodorsal_nucleus/ (adjacent; AD is the head-direction
      relay; distinct specialization; do not merge).
    - ↔ ../anteromedial_nucleus/ (adjacent; AM is the secondary
      memory relay; AV is dominant; do not merge; the AV/AM division
      of labor is density-based, not circuit-based — both carry Papez
      memory, but AV is dominant).

Notes:
    - Tier 1 full leaf (left). The ANCHOR of the anterior nuclear
      group: largest, dominant memory relay, clinical anchor
      (thalamic Korsakoff).
    - THE FINAL MAMMILLOTHALAMIC SUB-EDGE CLOSED: with this leaf, the
      mammillary → AV sub-edge of the mammillothalamic deferred edge
      is closed on the left. Combined with the AD and AM leaves
      (already closed), all three left-side sub-edges are now closed.
      The right AV delta will close the right-side AV sub-edge, and
      with it the entire anterior nuclear group's mammillothalamic
      deferred edge is fully resolved on both hemispheres.
    - THALAMIC KORSAKOFF (the AV's defining clinical anchor): the
      AV's clinical contribution is the thalamic counterpart of the
      hypothalamic Korsakoff (mammillary bodies). Together they
      document the full Korsakoff circuit: mammillary bodies
      (hypothalamic site) + mammillothalamic tract + AV (thalamic
      site). Document this; do not omit.
    - AV vs. AM DOMINANCE: the AV is the DOMINANT Papez relay; the AM
      is SECONDARY. The division of labor is density-based (AV has
      the densest mammillothalamic input), not circuit-based (both
      carry the same Papez memory signal). Do not treat them as
      interchangeable memory relays.
    - AV vs. AD DISTINCTION: the AV is the memory relay; the AD is
      the head-direction relay. Same tract, same cortical targets,
      different specializations. Do not merge.
    - The AV's "memory consolidation" role is the functional
      consequence of its relay role: the AV is required for episodic
      memory consolidation, and its loss produces thalamic Korsakoff.
      This is the AV's substantive contribution to the memory-circuit
      documentation.
    - NO FRAGMENT: same as the whole thalamus. The AV is a relay, not
      a state-emitter. The memory-failure guardrail (confabulation
      prevention) is inherited from the mammillary bodies' fragment,
      not added here.
    - The AV's dense mammillothalamic input is the structural basis of
      its dominant role: it is the largest nucleus with the strongest
      mammillothalamic input, which is why lesions of the mammillary
      bodies, the mammillothalamic tract, or the AV all produce the
      same Korsakoff syndrome.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (episodic, short_term,
      temporal_sequence_learning); gateway/.
    - Connects upward to diencephalon/thalamus/left/anterior_nuclear_
      group/.
"""