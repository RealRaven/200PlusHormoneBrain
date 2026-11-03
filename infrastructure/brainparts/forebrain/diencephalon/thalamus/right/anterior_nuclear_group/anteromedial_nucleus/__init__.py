"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.anterior_nuclear_group.anteromedial_nucleus
Anatomical Role:
    The right anteromedial nucleus (AM). The intermediate of the three
    right anterior thalamic nuclei, situated between the right
    anterodorsal (AD; head-direction) and the right anteroventral (AV;
    dominant memory relay) nuclei. Same Papez-circuit memory relay role
    as the left AM: it receives right mammillothalamic tract input from
    the right mammillary bodies and projects to the right cingulate and
    retrosplenial cortices.

    See ../../../../left/anterior_nuclear_group/anteromedial_nucleus/
    __init__.py for the full anatomical description, the
    secondary-Papez-relay framing, the vocalization-adjacent secondary
    role, and the honest "no AM-specific syndrome" framing.

    Reproduced distinctions (apply equally on the right):
    - AM vs. AD (intra-group): right AM is a memory relay; right AD is
      the head-direction relay. Different specializations. Do not
      merge.
    - AM vs. AV (intra-group): right AV is the DOMINANT memory relay
      (largest, densest mammillothalamic input); right AM is
      SECONDARY. Do not treat them as interchangeable memory relays.
    - AM vs. MEDIODORSAL NUCLEUS (MD; subtle): right AM is a
      Papez-circuit memory relay; right MD
      (../../../medial_nuclear_group/medial_dorsal_nucleus/) is a
      prefrontal relay. Different circuits; do not merge.
    - AM vs. ANTERIOR HYPOTHALAMIC NUCLEUS (group trap): right AM is
      the anterior thalamic memory relay; the right AHN
      (hypothalamus/anterior/medial_area/right/anterior_hypothalamic_
      nucleus/) is the parasympathetic/thermoregulatory hub. Distinct;
      do not merge.

Functional Mode:
    Same as ../../../../left/anterior_nuclear_group/anteromedial_
    nucleus/. Papez circuit memory relay (the anchor; secondary to the
    right AV); vocalization-adjacent / emotional memory (secondary;
    thinner evidence; do not overclaim).
    No documented functional asymmetry between left and right AM. Do
    not fabricate one.
    The clinical fact applies on the right identically: the right AM is
    part of the anterior thalamic amnesia system, but AM-SPECIFIC
    lesions are rare and AM-specific syndromes are not established. See
    ../../../../left/anterior_nuclear_group/anteromedial_nucleus/
    § Functional Mode.

Hormonal Modulation:
    Same as ../../../../left/anterior_nuclear_group/anteromedial_
    nucleus/. Minimal; cholinergic and monoaminergic arousal
    modulation; not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/anterior_nuclear_group/anteromedial_
    nucleus/. Reads episodic (relayed via the right mammillary bodies),
    short_term (memory buffer), temporal_sequence_learning (event
    order). Writes nothing directly (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right AM fragment. Same as ../../../../left/anterior_nuclear_
    group/anteromedial_nucleus/ and the whole thalamus: the AM is a
    relay, not a state-emitter. The model-relevant state is carried by
    the right mammillary bodies' fragment (with its confabulation
    guardrail) and the right cingulate's memory signals.

Right-specific reciprocal connections to enforce in Stage 4:

    Papez circuit memory relay (the anchor):
    - ← hypothalamus/mammillary_bodies/right (via the right
      mammillothalamic tract; Papez memory relay; THE DEFERRED
      MAMMILLARY → AM SUB-EDGE CLOSED ON THE RIGHT; the right
      mammillary leaf declares this edge from its side).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate (right AM → cingulate; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      retrosplenial_cortex (right AM → retrosplenial; right-side).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/hippocampus/right/subiculum (subicular
      input; right-side).

    Intra-group:
    - ↔ ../anterodorsal_nucleus/ (right AD; head-direction; distinct
      specialization; do not merge).
    - ↔ ../anteroventral_nucleus/ (right AV; dominant memory relay;
      AM is secondary; do not merge).

    - ↔ ../../../../left/anterior_nuclear_group/anteromedial_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/anterior_nuclear_group/
      anteromedial_nucleus/. Not a full leaf. Do not duplicate.
    - THE RIGHT MAMMILLARY → AM SUB-EDGE IS NOW CLOSED. Combined with
      the left AM leaf, the AM's side of the mammillothalamic deferred
      edge is fully declared on both hemispheres. With the AD pair
      also complete (both left leaf and right delta), the anterior
      nuclear group's mammillothalamic closures are:
        * AD (head-direction sub-pathway): both sides closed.
        * AM (memory sub-pathway): both sides closed (this file).
        * AV (dominant memory relay): still pending (the AV leaves).
    - AM vs. AV distinction reproduced: the right AV remains the
      DOMINANT memory relay; the right AM is SECONDARY. Do not treat
      them as interchangeable memory relays.
    - CLINICAL FACT (honest): AM-SPECIFIC lesions are rare and
      AM-specific syndromes are not established on the right either.
      Document the right AM as part of the anterior thalamic amnesia
      system, not as a standalone clinical entity. The right AV leaf
      will carry the full "thalamic Korsakoff" framing for the group's
      dominant memory relay.
    - The "vocalization-adjacent / emotional memory" secondary role is
      reproduced on the right with the same "thinner evidence; do not
      overclaim" caveat.
    - NO FRAGMENT: same as the whole thalamus. The right AM is a
      relay, not a state-emitter.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right mammillary bodies, right cingulate, right retrosplenial,
      right subiculum). The Stage 4 audit should not confuse
      right-side edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/anterior_nuclear_group/anteromedial_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/anterior_nuclear_
      group/.
"""