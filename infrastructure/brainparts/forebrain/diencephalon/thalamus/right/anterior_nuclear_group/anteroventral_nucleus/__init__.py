"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.anterior_nuclear_group.anteroventral_nucleus
Anatomical Role:
    The right anteroventral nucleus (AV). The LARGEST of the three
    right anterior thalamic nuclei, situated at the ventral-anterior
    pole of the right anterior nuclear group. Same DOMINANT Papez
    memory relay role as the left AV: it receives the DENSEST
    mammillothalamic tract input from the right mammillary bodies,
    projects densely to the right cingulate and retrosplenial
    cortices, and carries the primary episodic-memory relay of the
    right anterior group.

    Among the three right anterior nuclei:
        - AD (smallest): head-direction relay (right presubicular
          input).
        - AM (intermediate): secondary Papez memory relay.
        - AV (largest; THIS LEAF): DOMINANT Papez memory relay.

    See ../../../../left/anterior_nuclear_group/anteroventral_
    nucleus/__init__.py for the full anatomical description, the
    dominance framing (AV largest, densest mammillothalamic input),
    the full Papez circuit diagram, and the full "thalamic Korsakoff"
    clinical framing.

    Reproduced distinctions (apply equally on the right):
    - AV vs. AM (intra-group): right AV is DOMINANT; right AM is
      SECONDARY. Density-based division, not circuit-based. Do not
      treat as interchangeable.
    - AV vs. AD (intra-group): right AV is memory; right AD is
      head-direction. Different specializations.
    - AV vs. MEDIODORSAL NUCLEUS (MD; subtle): right AV is the Papez
      circuit memory relay; right MD
      (../../../medial_nuclear_group/medial_dorsal_nucleus/) is the
      prefrontal relay. Different circuits; do not merge.
    - AV vs. ANTERIOR HYPOTHALAMIC NUCLEUS: right AV is the anterior
      thalamic memory relay; the right AHN
      (hypothalamus/anterior/medial_area/right/anterior_hypothalamic_
      nucleus/) is the parasympathetic/thermoregulatory hub. Distinct;
      do not merge.

Functional Mode:
    Same as ../../../../left/anterior_nuclear_group/anteroventral_
    nucleus/. Papez circuit memory relay (the anchor; the DOMINANT
    memory relay of the right group); episodic memory consolidation
    (the functional consequence); spatial memory (secondary).
    No documented functional asymmetry between left and right AV. Do
    not fabricate one.

    CLINICAL FACT — THALAMIC KORSAKOFF (the AV's defining clinical
    anchor): applies on the right identically. Lesions of the right
    anterior thalamic nuclei (including the right AV), or of the right
    mammillothalamic tract, produce anterograde amnesia often with
    confabulation — functionally identical to hypothalamic Korsakoff
    from right mammillary body lesions. Same syndrome, different
    anatomical site (one synapse downstream). The right mammillary
    bodies (hypothalamus/mammillary_bodies/right/) + the right
    mammillothalamic tract + the right AV together document the full
    right-sided Korsakoff circuit. See ../../../../left/anterior_
    nuclear_group/anteroventral_nucleus/ § Functional Mode for the
    full clinical description.

Hormonal Modulation:
    Same as ../../../../left/anterior_nuclear_group/anteroventral_
    nucleus/. Minimal; cholinergic (basal forebrain) and monoaminergic
    arousal inputs, with the basal forebrain cholinergic input
    particularly relevant to memory. Not a principal target of the 12
    endocrine axes.

Memory Interfaces:
    Same as ../../../../left/anterior_nuclear_group/anteroventral_
    nucleus/. Reads episodic (relayed via the right mammillary bodies
    and direct right subicular input), short_term (memory buffer),
    temporal_sequence_learning (event order). Writes nothing directly
    (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right AV fragment. Same as ../../../../left/anterior_nuclear_
    group/anteroventral_nucleus/ and the whole thalamus: the AV is a
    relay, not a state-emitter. The model-relevant state is carried by
    the right mammillary bodies' fragment (with its confabulation
    guardrail) and the right cingulate's memory signals.

Right-specific reciprocal connections to enforce in Stage 4:

    Papez circuit memory relay (the anchor; DOMINANT):
    - ← hypothalamus/mammillary_bodies/right (via the right
      mammillothalamic tract; Papez memory relay; DENSEST
      mammillothalamic input of the three right anterior nuclei; THE
      DEFERRED SUB-EDGE CLOSED ON THE RIGHT; the right mammillary
      leaf declares this edge from its side).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate (right AV → cingulate; dense; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      retrosplenial_cortex (right AV → retrosplenial; dense;
      right-side).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/hippocampus/right/subiculum (subicular
      input; second source of hippocampal memory signal; right-side).

    Intra-group:
    - ↔ ../anterodorsal_nucleus/ (right AD; head-direction; distinct
      specialization; do not merge).
    - ↔ ../anteromedial_nucleus/ (right AM; secondary memory relay;
      AV is dominant; do not merge).

    - ↔ ../../../../left/anterior_nuclear_group/anteroventral_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/anterior_nuclear_group/
      anteroventral_nucleus/. Not a full leaf. Do not duplicate.
    - THE RIGHT MAMMILLARY → AV SUB-EDGE IS NOW CLOSED. Combined with
      the left AV leaf, the AV's side of the mammillothalamic deferred
      edge is fully declared on both hemispheres.
    - THE ENTIRE MAMMILLOTHALAMIC DEFERRED EDGE IS NOW FULLY RESOLVED
      ON BOTH HEMISPHERES: all six sub-closures are complete:
        * LM head-direction → AD (left + right).
        * Mammillary memory → AM (left + right).
        * Mammillary memory → AV (left + right; this file closes the
          final one).
      The Papez circuit's mammillothalamic link is fully documented on
      both sides.
    - ENTIRE ANTERIOR NUCLEAR GROUP NOW COMPLETE: with this file, the
      anterior nuclear group is fully documented on both hemispheres:
        * Group containers (left + right delta).
        * AD pair (left leaf + right delta).
        * AM pair (left leaf + right delta).
        * AV pair (left leaf + right delta; this file).
      8 files total, all complete.
    - THALAMIC KORSAKOFF (the AV's defining clinical anchor) applies
      on the right identically: right anterior thalamic (including
      right AV) or right mammillothalamic tract lesions produce
      anterograde amnesia + confabulation, functionally identical to
      hypothalamic Korsakoff from right mammillary body lesions. The
      right AV completes the right-sided Korsakoff circuit
      documentation (right mammillary bodies + right mammillothalamic
      tract + right AV).
    - AV vs. AM DOMINANCE reproduced: right AV remains DOMINANT; right
      AM is SECONDARY. Density-based division, not circuit-based.
    - AV vs. AD DISTINCTION reproduced: right AV is memory; right AD
      is head-direction. Different specializations.
    - NO FRAGMENT: same as the whole thalamus. The right AV is a relay,
      not a state-emitter. The memory-failure guardrail is inherited
      from the right mammillary bodies' fragment.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right mammillary bodies, right cingulate, right retrosplenial,
      right subiculum). Stage 4 should not confuse right-side edges
      with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/anterior_nuclear_group/anteroventral_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/anterior_nuclear_
      group/.
"""