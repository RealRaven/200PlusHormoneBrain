"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.anterior_nuclear_group.anterodorsal_nucleus
Anatomical Role:
    The right anterodorsal nucleus (AD). The smallest of the three right
    anterior thalamic nuclei, situated at the dorsal-anterior pole of
    the right anterior nuclear group. Like its left counterpart, it
    contains HEAD-DIRECTION CELLS: neurons whose firing is tuned to the
    animal's directional heading, analogous to the head-direction cells
    of the right lateral mammillary nucleus
    (hypothalamus/mammillary_bodies/right/ § Functional Mode).

    See ../../../../left/anterior_nuclear_group/anterodorsal_nucleus/
    __init__.py for the full anatomical description, the head-direction
    cell framing, the presubicular/subicular input list, the
    retrosplenial/postsubicular output list, and the Alzheimer's
    clinical fact.

    Reproduced distinctions (apply equally on the right):
    - AD vs. AM and AV (intra-group): right AD is the head-direction
      relay; right AM and AV are episodic-memory relays. All three are
      Papez relays, but AD specializes in spatial orientation. Do not
      treat them as interchangeable.
    - AD vs. RIGHT LATERAL MAMMILLARY NUCLEUS (head-direction parallel):
      the right LM contains head-direction cells and projects to the
      right AD via the right mammillothalamic tract. The two are the
      right-sided diencephalic head-direction hubs, connected via the
      tract. Distinct nodes; do not merge.
    - AD vs. RIGHT ANTERIOR HYPOTHALAMIC NUCLEUS: the right AD is the
      head-direction relay in the anterior thalamus; the right AHN
      (hypothalamus/anterior/medial_area/right/anterior_hypothalamic_
      nucleus/) is the parasympathetic/thermoregulatory hub. Distinct;
      do not merge.

Functional Mode:
    Same as ../../../../left/anterior_nuclear_group/anterodorsal_nucleus/:
    head-direction relay (the anchor); Papez memory relay (secondary;
    shared with AM and AV). No documented functional asymmetry between
    left and right AD. Do not fabricate one.
    The Alzheimer's clinical fact applies on the right identically: the
    right anterior thalamic nuclei (including the right AD) are among
    the earliest brain regions affected in Alzheimer's disease;
    anterior thalamic atrophy is an established early biomarker.
    See ../../../../left/anterior_nuclear_group/anterodorsal_nucleus/
    § Functional Mode for the full description.

Hormonal Modulation:
    Same as ../../../../left/anterior_nuclear_group/anterodorsal_
    nucleus/. Minimal; the AD is a head-direction relay, modulated by
    cholinergic and monoaminergic arousal inputs, not a principal target
    of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/anterior_nuclear_group/anterodorsal_
    nucleus/. Reads short_term (head-direction buffer), episodic
    (spatial context), temporal_sequence_learning (supporting);
    writes nothing directly (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right AD fragment. The AD is a head-direction relay; the model
    prompt does not need an anterodorsal-nucleus block. The relevant
    spatial and memory state is carried by the right mammillary bodies'
    fragment and the right retrosplenial cortex. Same deliberate
    absence as on the left. See ../../../../left/anterior_nuclear_
    group/anterodorsal_nucleus/ § Model Integration.

Right-specific reciprocal connections to enforce in Stage 4:

    Head-direction sub-pathway (the anchor):
    - ← hypothalamus/mammillary_bodies/right (via the right
      mammillothalamic tract; HEAD-DIRECTION SUB-PATHWAY from the
      right lateral mammillary nucleus's head-direction cells to the
      right AD; THE DEFERRED EDGE CLOSED ON THE RIGHT; the right
      mammillary leaf declares this edge from its side).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/hippocampus/right/presubiculum
      (presubicular head-direction input; right-side).
    - ← telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/hippocampus/right/subiculum (subicular
      spatial-context input; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      retrosplenial_cortex (retrosplenial head-direction target;
      right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/*
      (postsubicular / parietal head-direction target; right-side).

    Papez circuit (secondary; shared with AM and AV):
    - ← hypothalamus/mammillary_bodies/right (via the right
      mammillothalamic tract; Papez memory relay; same tract as the
      head-direction sub-pathway).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate and retrosplenial_cortex (Papez cortical
      relay; right-side).

    Intra-group:
    - ↔ ../anteroventral_nucleus/ (right AV; distinct specializations;
      do not merge).
    - ↔ ../anteromedial_nucleus/ (right AM; distinct from AD's
      head-direction role; do not merge).

    - ↔ ../../../../left/anterior_nuclear_group/anterodorsal_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/anterior_nuclear_group/
      anterodorsal_nucleus/. Not a full leaf. Do not duplicate.
    - HEAD-DIRECTION SUB-EDGE CLOSED ON THE RIGHT: with this file, the
      LM → AD head-direction sub-pathway of the mammillary → anterior
      thalamus deferred edge is fully closed on BOTH hemispheres. The
      full Papez circuit (both the memory and head-direction aspects)
      is now documented on both sides.
    - THE AD's HEAD-DIRECTION ROLE IS DISTINCT from AM/AV's memory
      role on the right identically. Do not flatten to "memory relay."
    - The right LM ↔ right AD parallel is reproduced in abbreviated
      form; the full parallel framing is in
      ../../../../left/anterior_nuclear_group/anterodorsal_nucleus/.
    - The right AD vs. right AHN trap is reproduced in abbreviated
      form; the full group-level trap is in
      ../../../__init__.py (right anterior nuclear group).
    - The Alzheimer's clinical fact applies on the right identically:
      right anterior thalamic (including right AD) atrophy is an
      established early biomarker of Alzheimer's disease.
    - NO FRAGMENT: same as the whole thalamus. The right AD is a relay,
      not a state-emitter.
    - The three clinical anchors of the anterior nuclear group are
      distributed by nucleus: right AD = Alzheimer's; right AM =
      episodic memory impairment (secondary); right AV = thalamic
      Korsakoff (the dominant memory relay's lesion fact). Each leaf
      carries its own; this delta references the AD's.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/anterior_nuclear_group/anterodorsal_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/anterior_nuclear_
      group/.
"""