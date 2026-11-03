"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.anterior_nuclear_group.anterodorsal_nucleus
Anatomical Role:
    The left anterodorsal nucleus (AD). The smallest of the three left
    anterior thalamic nuclei, situated at the dorsal-anterior pole of
    the left anterior nuclear group. It contains HEAD-DIRECTION CELLS:
    neurons whose firing is tuned to the animal's directional heading,
    analogous to the head-direction cells of the left lateral
    mammillary nucleus (hypothalamus/mammillary_bodies/left/ §
    Functional Mode).

    Unlike the AM and AV (which are primarily episodic-memory relays),
    the AD is primarily a HEAD-DIRECTION / SPATIAL ORIENTATION relay:
        - Head-direction cells encode the current directional heading.
        - The AD receives strong presubicular input (the presubiculum
          is a head-direction-processing region).
        - The AD projects to the left retrosplenial cortex and the
          left postsubiculum, which continue the head-direction signal
          to the spatial navigation circuits.

    The AD also participates in the Papez circuit's memory relay (via
    the mammillothalamic tract from the left mammillary bodies), but
    its distinctive contribution is the head-direction signal.

    DISTINCTIONS (critical):

    - AD vs. AM and AV (intra-group distinction): AD is the
      head-direction relay; AM and AV are episodic-memory relays. All
      three are Papez circuit relays, but AD specializes in spatial
      orientation and AM/AV in memory content. Do not treat them as
      interchangeable; the AD leaf's "head-direction" framing is
      distinct from the AM/AV "memory" framing.

    - AD vs. LEFT LATERAL MAMMILLARY NUCLEUS (the head-direction
      parallel): the left lateral mammillary nucleus (LM) contains
      head-direction cells and projects to the AD via the
      mammillothalamic tract. The LM → AD projection is the
      subcortical-to-thalamic head-direction relay. The AD continues
      this signal to the retrosplenial and postsubicular cortices. The
      AD and LM are the two head-direction hubs in the diencephalon;
      they are distinct nodes at different anatomical sites (LM in the
      mammillary bodies, AD in the anterior thalamus), connected via
      the mammillothalamic tract. Do not merge.

    - AD vs. ANTERIOR HYPOTHALAMIC NUCLEUS (the standard group trap):
      the AD (this leaf) is the head-direction relay in the anterior
      thalamus; the left anterior hypothalamic nucleus
      (hypothalamus/anterior/medial_area/left/anterior_hypothalamic_
      nucleus/) is the parasympathetic/thermoregulatory hub in the
      hypothalamus. Both are "anterior"; both are diencephalic; distinct
      structures. Do not merge.

Functional Mode:
    - Head-direction relay (the AD's anchor role):
        * Head-direction cells: the AD contains neurons whose firing
          rate is tuned to the animal's directional heading (typically
          in the horizontal plane). The population as a whole encodes
          the full 360° of directional heading.
        * Input from the presubiculum and subiculum: the presubiculum
          is a head-direction-processing region; the subiculum
          provides spatial context. These inputs give the AD its
          head-direction signal.
        * Output to the retrosplenial cortex and postsubiculum: the
          AD → retrosplenial / postsubicular pathway continues the
          head-direction signal to the cortical spatial navigation
          circuits (retrosplenial cortex is a key hub for spatial
          orientation and navigation).
    - Papez circuit memory relay (secondary for the AD): the AD also
      receives mammillothalamic tract input from the left mammillary
      bodies and participates in the Papez circuit's memory relay.
      This role is shared with the AM and AV; the AD's distinctive
      contribution remains the head-direction signal.
    - The AD is therefore the head-direction sub-relay of the Papez
      circuit: its position in the circuit is the same as the AM/AV
      (mammillothalamic input → retrosplenial output), but its
      functional specialization is spatial orientation rather than
      memory content.

    - CLINICAL FACT (the AD's defining clinical anchor): the anterior
      thalamic nuclei (including the AD) are among the earliest brain
      regions affected in Alzheimer's disease. Anterior thalamic
      atrophy — including AD involvement — is an established early
      biomarker of Alzheimer's, and its disruption contributes to the
      spatial disorientation and episodic memory impairment that
      characterize the disease. This is a disease-specific
      contribution distinct from the "thalamic Korsakoff" lesion
      fact that the AV carries; the AD's clinical anchor is
      Alzheimer's-related anterior thalamic degeneration.

Hormonal Modulation (minimal; the AD is a head-direction relay):
    - The AD is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) inputs contribute to the arousal and attentional
      gating of the head-direction relay. These are the same ascending
      neuromodulators that modulate the whole thalamus; document as
      arousal modulation, not endocrine modulators.
    - The AD is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * short_term: the current head-direction buffer (the AD's
          head-direction signal is a short-term spatial state).
        * episodic: the spatial context of the current episode; the
          AD's head-direction signal is integrated with episodic
          memory by the retrosplenial cortex.
        * temporal_sequence_learning: the temporal order of
          spatial-orientation events (the AD's head-direction signal
          is temporally continuous, not event-indexed; document as a
          supporting read).
    - Writes: none directly. The AD is a RELAY: it transmits the
      head-direction signal to the retrosplenial cortex; the
      spatial-context integration happens in the cortical targets.
    - The AD is therefore a head-direction-relay node: it reads the
      short-term spatial context and relays it; it does not write
      stored content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No AD fragment. The AD is a head-direction relay; the model
      prompt does not need an anterodorsal-nucleus block because the
      spatial-orientation signal is not a discrete state the language
      model should be conditioned on. The relevant spatial and memory
      state is carried by the upstream (lateral mammillary nucleus,
      via the mammillary bodies' fragment) and downstream
      (retrosplenial cortex) nodes.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence.
    - The AD's clinical fact (Alzheimer's-related anterior thalamic
      degeneration) is documented for completeness, but is not a
      prompt field.

Reciprocal Connections (left-side; the right side is in
../../../../right/anterior_nuclear_group/anterodorsal_nucleus/):

    Head-direction sub-pathway (the anchor):
    - ← hypothalamus/mammillary_bodies/left (via the mammillothalamic
      tract; the HEAD-DIRECTION SUB-PATHWAY from the left lateral
      mammillary nucleus's head-direction cells to the left AD; the
      mammillary leaf declares this edge from its side; THE DEFERRED
      EDGE CLOSED HERE).
    - ← telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/hippocampus/left/presubiculum (presubicular
      head-direction input; the presubiculum's head-direction cells
      project to the AD).
    - ← telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/hippocampus/left/subiculum (subicular
      spatial-context input).
    - → telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      retrosplenial_cortex (retrosplenial head-direction target; the
      retrosplenial cortex is a key hub for spatial orientation).
    - → telencephalon/cerebral_hemispheres/left/cortex/parietal/*
      (postsubicular / parietal head-direction target; the
      postsubicular continuation of the head-direction signal).

    Papez circuit (secondary; shared with AM and AV):
    - ← hypothalamus/mammillary_bodies/left (via the mammillothalamic
      tract; Papez memory relay; the same mammillothalamic edge
      carries both head-direction and memory signals from the
      mammillary bodies).
    - → telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      anterior_cingulate and retrosplenial_cortex (Papez cortical
      relay; shared with AM and AV).

    Intra-group:
    - ↔ ../anteroventral_nucleus/ (adjacent anterior thalamic nuclei;
      AV is the dominant memory relay; AD is the head-direction relay;
      distinct specializations within the same group; do not merge).
    - ↔ ../anteromedial_nucleus/ (adjacent anterior thalamic nuclei;
      AM is the secondary memory relay; distinct from AD's
      head-direction role; do not merge).

Notes:
    - Tier 1 full leaf (left). The smallest of the three anterior
      thalamic nuclei but the one with the most distinct
      specialization (head-direction).
    - THE AD's HEAD-DIRECTION ROLE IS DISTINCT FROM AM/AV's MEMORY
      ROLE: all three are Papez relays, but AD specializes in spatial
      orientation. The leaf's "head-direction" framing is deliberate
      and should not be flattened to "memory relay."
    - THE LM → AD HEAD-DIRECTION SUB-EDGE CLOSURE: this leaf closes
      the head-direction sub-pathway of the mammillary → anterior
      thalamus deferred edge. The mammillary bodies leaf declared the
      full mammillothalamic edge; this leaf declares the AD's
      head-direction specialization of that edge.
    - AD vs. LM parallel: the AD's head-direction role is functionally
      analogous to the left lateral mammillary nucleus's head-direction
      cells. Both are head-direction hubs; both are in the diencephalon;
      they are connected via the mammillothalamic tract. Document the
      parallel; do not merge.
    - AD vs. ANTERIOR HYPOTHALAMIC NUCLEUS trap reproduced in
      abbreviated form; the full group-level trap is in
      ../../__init__.py.
    - CLINICAL FACT (Alzheimer's): the anterior thalamic nuclei
      (including the AD) are among the earliest brain regions affected
      in Alzheimer's disease; anterior thalamic atrophy is an
      established early biomarker. This is the AD's disease-specific
      contribution, distinct from the AV's "thalamic Korsakoff" lesion
      fact. Both facts belong to the anterior nuclear group; each
      leaf carries its own.
    - NO FRAGMENT: same as the whole thalamus. The AD is a relay, not
      a state-emitter.
    - The AD's memory interfaces (reads episodic, short_term,
      temporal_sequence_learning) are for its role in the Papez
      circuit's memory relay, not for head-direction. The AD's
      head-direction role uses the short_term read (spatial buffer)
      and does not have a distinct memory interface.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (episodic, short_term,
      temporal_sequence_learning); gateway/.
    - Connects upward to diencephalon/thalamus/left/anterior_nuclear_
      group/.
"""