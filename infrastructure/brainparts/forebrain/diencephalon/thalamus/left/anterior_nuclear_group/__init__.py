"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.anterior_nuclear_group
Anatomical Role:
    The left anterior nuclear group of the thalamus. A small cluster of
    three nuclei situated at the anterior pole of the left thalamus,
    dorsal to the left hypothalamus and adjacent to the left third
    ventricle. It is the THALAMIC RELAY OF THE PAPEZ CIRCUIT and one of
    the three principal memory-related thalamic groups (along with the
    mediodorsal nucleus and the intralaminar group).

    The three nuclei:
        - anterodorsal_nucleus/ (AD): the smallest of the three.
          Contains HEAD-DIRECTION CELLS (like the lateral mammillary
          nucleus). Receives strong input from the left presubiculum
          and left subiculum; projects to the left retrosplenial
          cortex and the left postsubiculum. Implicated in spatial
          orientation and navigation.
        - anteromedial_nucleus/ (AM): receives mammillothalamic input
          and projects to the left cingulate cortex and left
          retrosplenial cortex. Contributes to episodic memory and
          spatial learning.
        - anteroventral_nucleus/ (AV): the LARGEST of the three.
          Receives strong mammillothalamic input; projects densely to
          the left cingulate cortex and left retrosplenial cortex.
          The principal Papez-circuit memory relay.

    All three receive input via the mammillothalamic tract from the
    left mammillary bodies (see
    hypothalamus/mammillary_bodies/left/ for the hypothalamic side of
    this edge). The three nuclei together relay the hippocampal-
    mammillary memory signal to the cingulate and retrosplenial
    cortices, completing the Papez circuit.

    DISTINCTIONS (critical):

    - ANTERIOR THALAMIC NUCLEI vs. ANTERIOR HYPOTHALAMIC NUCLEUS (the
      primary trap): the anterior thalamic nuclei (this group; AD, AM,
      AV) are the PAPEZ CIRCUIT RELAY in the thalamus. The anterior
      hypothalamic nucleus (hypothalamus/anterior/medial_area/left/
      anterior_hypothalamic_nucleus/) is the PARASYMPATHETIC AND
      THERMOREGULATORY HUB in the hypothalamus. Both are "anterior,"
      both are in the diencephalon — but they are DIFFERENT STRUCTURES
      with different functions. Do not merge; do not confuse the AD /
      AM / AV leaves with the AHN leaf.

    - ANTERIOR NUCLEAR GROUP vs. MEDIODORSAL NUCLEUS (a subtle
      distinction): both are memory-related thalamic relays. The
      anterior group is the PAPEZ CIRCUIT relay (hippocampus →
      mammillary bodies → anterior thalamus → cingulate); the
      mediodorsal nucleus is the PREFRONTAL relay (amygdala and
      prefrontal cortex → MD → PFC). Different circuits; different
      nuclei; do not merge.

Functional Mode:
    - Papez circuit relay (the anchor role): the anterior nuclear group
      is the thalamic relay of the Papez circuit — the classical
      circuit that supports episodic memory and spatial navigation:
        hippocampus → fornix → mammillary bodies → mammillothalamic
        tract → anterior thalamic nuclei (this group) → cingulate
        cortex and retrosplenial cortex → parahippocampal gyrus →
        entorhinal cortex → hippocampus.
      The anterior group is the REQUIRED thalamic relay: it receives
      the mammillothalamic memory signal from the mammillary bodies and
      relays it to the cingulate and retrosplenial cortices, where
      episodic re-encoding and spatial-context integration happen.
    - Head-direction (AD; the sub-function): the anterodorsal nucleus
      contains head-direction cells, analogous to the lateral
      mammillary nucleus's head-direction cells. The AD → retrosplenial
      / postsubicular pathway carries the head-direction signal,
      supporting spatial orientation.
    - Episodic memory and spatial learning (AM, AV): the anteromedial
      and anteroventral nuclei relay memory content from the
      mammillary bodies to the cingulate and retrosplenial cortices;
      they support episodic memory and spatial learning. The AV is the
      dominant relay (largest, densest mammillothalamic input).
    - Subcortical and cortical integration: the anterior group also
      receives subicular and presubicular inputs, and projects to
      multiple cortical targets (cingulate, retrosplenial,
      postsubicular), integrating the hippocampal-mammillary signal
      with cortical memory circuits.
    - CLINICAL FACT (the anterior group's defining clinical anchor):
      lesions of the anterior thalamic nuclei — or of the
      mammillothalamic tract that feeds them — produce ANTEROGRADE
      AMNESIA, sometimes with confabulation. This is functionally
      similar to Korsakoff syndrome (which is caused by mammillary body
      lesions, and by extension damages the anterior thalamic relay),
      and it is the anatomical proof that the anterior thalamic nuclei
      are a required memory relay, not just a waypoint. The anterior
      thalamic lesion is sometimes called the "thalamic Korsakoff" —
      same syndrome as the hypothalamic version, different anatomical
      site. Document this fact; it is the anterior group's clinical
      signature.

Hormonal Modulation (minimal; the anterior group is a memory relay):
    - The anterior nuclear group is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) inputs contribute to the arousal and attentional
      gating of the memory relay; these are the same ascending
      neuromodulators that modulate the whole thalamus. Document them
      as arousal modulation, not as endocrine modulators.
    - The anterior group is NOT a principal target of the 12 endocrine
      axes. Do not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * episodic: the left anterior group relays the hippocampal
          episodic signal from the left mammillary bodies to the
          left cingulate/retrosplenial cortices. The memory content
          flows through the anterior group; it READS the memory
          signal from the mammillothalamic tract.
        * short_term: the current memory buffer being relayed.
        * temporal_sequence_learning: temporal order of events within
          an episode, as relayed via the mammillary bodies.
    - Writes: none directly. The anterior group is a RELAY, not an
      encoder. It transmits the hippocampal-mammillary signal to the
      cingulate cortex; the actual re-encoding happens in the cortex.
      Same discipline as the mammillary bodies (relay, not encoder)
      and the thalamus generally (relay, not state-emitter).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No anterior group fragment. The anterior group is a memory relay;
      the model prompt does not need an anterior-thalamic block because
      the memory signals it relays are already represented in the
      upstream (mammillary bodies) and downstream (cingulate cortex)
      fragments. The mammillary memory-relay fragment (with its
      confabulation guardrail) and the cortical memory signals carry
      the model-relevant state.
    - AGGREGATION RULES: no fragments are emitted from this container
      or from the three nucleus leaves. Deliberate absence.
    - The anterior group's clinical fact (anterograde amnesia /
      "thalamic Korsakoff") is documented for completeness, but is
      not a prompt field.

Children (three children — three full leaves, no sub-containers):
    - anterodorsal_nucleus/    Tier 1 leaf. Head-direction relay; AD
                                 → retrosplenial / postsubicular.
                                 The smallest of the three but with a
                                 distinctive head-direction function.
    - anteromedial_nucleus/    Tier 1 leaf. Memory relay; AM →
                                 cingulate and retrosplenial.
    - anteroventral_nucleus/   ★ Tier 1 leaf. The largest and
                                 dominant Papez relay; AV →
                                 cingulate and retrosplenial. The
                                 anchor nucleus of the group.

    All three are full leaves (not deltas of each other): AD, AM, and
    AV are distinct nuclei with distinct projections and functions.
    The left/right pairs are the standard hemisphere-delta pattern.

Notes:
    - Group container. Names the three nuclei; defers functional
      content to the leaves (except for the container-level summary
      above).
    - CLOSES THE MAMMILLARY BODIES → ANTERIOR THALAMUS DEFERRED EDGE:
      the mammillary bodies leaf
      (hypothalamus/mammillary_bodies/left/) declared the
      mammillothalamic tract edge to the anterior thalamic nuclei. The
      anterior group's leaves (specifically AV and AM, and AD for the
      head-direction sub-pathway) close it on the anterior-thalamic
      side. This completes the Papez circuit's memory relay chain
      from the hypothalamic side.
    - ANTERIOR THALAMIC NUCLEI vs. ANTERIOR HYPOTHALAMIC NUCLEUS trap
      reproduced in full above. The two are easy to confuse (both
      "anterior," both diencephalic); the container makes the
      distinction explicit.
    - The ANTERIOR GROUP vs. MD distinction (both memory-related
      thalamic relays, different circuits) is also reproduced: the
      anterior group is the Papez relay; MD is the prefrontal relay.
    - The AD (head-direction) vs. AM/AV (memory) distinction is
      documented at the group level: the AD's function is structurally
      analogous to the lateral mammillary nucleus's head-direction
      cells, and the AD's leaf should reference the LM leaf's
      head-direction role. The AM/AV are the memory relays.
    - The AV is marked ★: it is the largest and dominant Papez relay
      and the anchor nucleus of the group. It is the natural first
      leaf to draft after the container.
    - CLINICAL FACT: anterior thalamic lesions (or mammillothalamic
      tract lesions) produce anterograde amnesia functionally similar
      to Korsakoff syndrome ("thalamic Korsakoff"). Documented at the
      group level; the AV leaf (as the dominant memory relay) should
      carry the full clinical detail.
    - NO FRAGMENT: same as the whole thalamus. The anterior group is a
      relay, not a state-emitter. The memory-relay state is carried by
      the mammillary bodies' fragment.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (episodic, short_term,
      temporal_sequence_learning); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * anterior_nuclear_group/left/anterodorsal_nucleus ↔
          hypothalamus/mammillary_bodies/left (via the mammillothalamic
          tract; head-direction sub-pathway; the LM's head-direction
          cells project to the AD via the mammillothalamic tract; the
          mammillary leaf declares this edge from its side).
        * anterior_nuclear_group/left/anterodorsal_nucleus ↔
          telencephalon/.../cortex/cingulate/retrosplenial_cortex and
          telencephalon/.../cortex/parietal/* (postsubicular /
          retrosplenial; head-direction cortical target).
        * anterior_nuclear_group/left/anteromedial_nucleus ↔
          hypothalamus/mammillary_bodies/left (via the
          mammillothalamic tract; Papez memory relay) and ↔
          telencephalon/.../cortex/cingulate (AM → cingulate).
        * anterior_nuclear_group/left/anteroventral_nucleus ↔
          hypothalamus/mammillary_bodies/left (via the
          mammillothalamic tract; the dominant Papez relay) and ↔
          telencephalon/.../cortex/cingulate and retrosplenial_cortex
          (AV → cingulate + retrosplenial).
        * anterior_nuclear_group/left ↔ telencephalon/.../subcortical/
          medial_temporal_lobe/hippocampus/left/subiculum and
          presubiculum (subicular/presubicular input to the anterior
          group; the AD's head-direction input is presubicular).
        * anterior_nuclear_group/left ↔ hypothalamus/mammillary_bodies/
          left (mammillothalamic tract; the deferred edge this group
          closes; both AD and AV/AM receive it).
    - Connects upward to diencephalon/thalamus/left/.
"""