"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.anterior_nuclear_group
Anatomical Role:
    The right anterior nuclear group of the thalamus. Same three nuclei
    at the anterior pole of the right thalamus documented in
    ../../left/anterior_nuclear_group/:
        - anterodorsal_nucleus/ (AD): head-direction relay; AD →
          right retrosplenial / postsubicular.
        - anteromedial_nucleus/ (AM): memory relay; AM → right
          cingulate and retrosplenial.
        - anteroventral_nucleus/ (AV): ★ the largest and dominant
          Papez relay; AV → right cingulate and retrosplenial.
    See ../../left/anterior_nuclear_group/__init__.py for the full
    anatomical description, the three-nucleus framing, the AD
    head-direction / AM-AV memory split, and the "thalamic Korsakoff"
    clinical fact.

    Reproduced distinctions (apply equally on the right):
    - ANTERIOR THALAMIC NUCLEI vs. ANTERIOR HYPOTHALAMIC NUCLEUS: the
      right anterior thalamic nuclei (AD, AM, AV) are the Papez circuit
      relay; the right anterior hypothalamic nucleus
      (hypothalamus/anterior/medial_area/right/anterior_hypothalamic_
      nucleus/) is the parasympathetic/thermoregulatory hub. Both are
      "anterior"; both are diencephalic; DISTINCT structures. Do not
      merge.
    - ANTERIOR NUCLEAR GROUP vs. MEDIODORSAL NUCLEUS: the right
      anterior group is the Papez relay (hippocampus → mammillary
      bodies → anterior thalamus → cingulate); the right MD (in
      right/medial_nuclear_group/medial_dorsal_nucleus/) is the
      prefrontal relay (amygdala/PFC → MD → PFC). Different circuits;
      do not merge.

Functional Mode:
    Same as ../../left/anterior_nuclear_group/. Papez circuit relay
    (the anchor role); head-direction (AD); episodic memory and
    spatial learning (AM, AV). The "thalamic Korsakoff" clinical fact
    (anterograde amnesia from anterior thalamic or mammillothalamic
    tract lesions) applies on the right identically. No documented
    functional asymmetry between left and right anterior nuclear
    groups. Do not fabricate one. See ../../left/
    anterior_nuclear_group/ § Functional Mode.

Hormonal Modulation:
    Same as ../../left/anterior_nuclear_group/. Minimal; the anterior
    group is a memory relay, modulated by cholinergic and monoaminergic
    arousal inputs, not a principal target of the 12 endocrine axes.
    See ../../left/anterior_nuclear_group/ § Hormonal Modulation.

Memory Interfaces:
    Same as ../../left/anterior_nuclear_group/. Reads episodic,
    short_term, temporal_sequence_learning (relayed via the right
    mammillary bodies); writes nothing directly (relay, not encoder).
    See ../../left/anterior_nuclear_group/ § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    No right anterior group fragment. Same as ../../left/ and the whole
    thalamus: the anterior group is a memory relay; the model-relevant
    state is carried by the right mammillary bodies' fragment (with its
    confabulation guardrail) and the right cingulate cortex's memory
    signals. See ../../left/anterior_nuclear_group/ § Model
    Integration.

Children (three children — all right-side deltas of their left
counterparts):
    - anterodorsal_nucleus/    Delta of ../../left/anterior_nuclear_
                                 group/anterodorsal_nucleus/. Right
                                 AD; head-direction relay.
    - anteromedial_nucleus/    Delta of ../../left/anterior_nuclear_
                                 group/anteromedial_nucleus/. Right
                                 AM; memory relay.
    - anteroventral_nucleus/   ★ Delta of ../../left/anterior_nuclear_
                                 group/anteroventral_nucleus/. Right
                                 AV; dominant Papez relay.

    Each of these three right nuclei is a DELTA of its left
    counterpart; no full right-side leaves are needed. The left side
    carries the substantive content (nucleus-specific anatomy, full
    clinical detail, complete reciprocal edge list); the right side
    records only right-side reciprocal edges and reproduces the traps.

Right-specific reciprocal connections to enforce in Stage 4:

    Papez circuit (the anchor):
    - ↔ hypothalamus/mammillary_bodies/right (mammillothalamic tract;
      THE DEFERRED EDGE CLOSED ON THE RIGHT; the right mammillary
      bodies leaf declares this edge from its side; the right AV and
      AM receive it; the right AD receives the LM head-direction
      sub-pathway).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate and retrosplenial_cortex (the Papez cortical
      relay; right-side).
    - ← telencephalon/.../subcortical/medial_temporal_lobe/hippocampus/
      right/subiculum and presubiculum (subicular/presubicular input;
      the AD's head-direction input is right presubicular).

    Head-direction (AD-specific):
    - ↔ hypothalamus/mammillary_bodies/right (via the mammillothalamic
      tract; head-direction sub-pathway from the right lateral
      mammillary nucleus).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      retrosplenial_cortex and telencephalon/.../cortex/parietal/*
      (postsubicular / retrosplenial; right-side).

    - ↔ ../../left/anterior_nuclear_group/ (hemisphere counterpart; no
      functional asymmetry assumed).

Notes:
    - Group-container delta of ../../left/anterior_nuclear_group/. Not a
      full container. Do not duplicate the left group's content.
    - THE MAMMILLARY BODIES → ANTERIOR THALAMUS DEFERRED EDGE IS NOW
      COMPLETE ON BOTH HEMISPHERES: the left group container declared
      it on the left; this right delta declares it on the right. The
      full Papez circuit's mammillothalamic link is now closed on both
      sides.
    - The two traps (anterior thalamic vs. anterior hypothalamic;
      anterior group vs. MD) are reproduced in abbreviated form above;
      the full text is in ../../left/anterior_nuclear_group/ and
      ../../. A contributor entering at the right anterior group must
      see them.
    - DELTA-OF-A-DELTA CHAIN EXTENDS TO THIS GROUP: the three right
      nuclei (AD, AM, AV) are each deltas of their left counterparts,
      same as every other thalamic right leaf. The chain is consistent
      with the LHA segments, the STN/VMH pairs, and the thalamus/right/
      container.
    - The AV is marked ★ on the right as well: it is the dominant Papez
      relay on the right, same as on the left.
    - NO FRAGMENT: same as the whole thalamus. The right anterior group
      is a relay, not a state-emitter.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right mammillary bodies, right cingulate, right retrosplenial,
      right subiculum, right presubiculum, right postsubicular, right
      parietal association). The Stage 4 audit should not confuse
      right-side edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/anterior_nuclear_group/ § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/.
"""