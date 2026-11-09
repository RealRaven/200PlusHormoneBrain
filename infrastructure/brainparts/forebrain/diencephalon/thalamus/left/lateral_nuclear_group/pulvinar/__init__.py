"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.lateral_nuclear_group.pulvinar
Anatomical Role:
    The left pulvinar. The LARGEST nucleus of the left lateral nuclear
    group and one of the largest nuclei in the entire left thalamus,
    forming the posterior pole of the thalamus. It is a VISUAL
    ASSOCIATION RELAY: its driver input is primarily from the left
    visual cortices (V1–V5, MT) and its output is to the left visual
    association cortices (V2–V5, MT, IT) and to the parietal and
    temporal association cortices.

    THREE SUBREGIONS (documented WITHIN this leaf, not as child nodes):
        - Lateral pulvinar: the VISUAL subregion. Receives strong
          input from V1, V2, V4, and MT; projects primarily back to
          V2, V4, V5/MT, and IT. This is the subregion most directly
          involved in visual association and visual attention.
        - Medial pulvinar: the MULTISENSORY / ASSOCIATION subregion.
          Receives input from parietal and temporal association
          cortices, and from the superior colliculus and other
          subcortical structures; projects to the parietal and
          temporal association cortices and to the prefrontal cortex.
          This is the subregion most involved in higher-order
          multimodal association and in the "attention to
          behaviorally relevant stimuli" role.
        - Inferior pulvinar: the MOTION-ADJACENT subregion. Receives
          input from and projects to MT/V5 (the motion area); is
          adjacent to and functionally coupled with the motion
          pathway. The inferior pulvinar's role in motion processing
          and in the subcortical visual pathway (via the superior
          colliculus) is less established than the lateral pulvinar's
          visual-association role.
    Same convention as the habenula's LHb/MHb split and the PVN's
    three sub-populations: the subregions are content within a single
    leaf, not tree children. Do not create lateral_pulvinar/,
    medial_pulvinar/, or inferior_pulvinar/ as child nodes.

    DISTINCTIONS (critical):

    - PULVINAR vs. LATERAL POSTERIOR (the group's signature trap;
      reproduced from the group container): the pulvinar is the VISUAL
      association relay (V2–V5, MT, IT); the LP is the PARIETAL
      association relay (posterior parietal cortex, areas 5/7).
      Different cortical targets; different association domains. Do
      not merge; do not treat them as interchangeable higher-order
      relays.

    - PULVINAR vs. LGN (lateral geniculate nucleus; the FIRST-ORDER
      visual relay): the LGN (thalamus/left/metathalamus/
      lateral_geniculate_body/) is the FIRST-ORDER visual relay (retina
      → LGN → V1); the pulvinar is the HIGHER-ORDER visual association
      relay (visual cortex → pulvinar → visual association cortex). The
      two are the two visual thalamic relays — first-order (LGN) and
      higher-order (pulvinar). Different relay types; different driver
      inputs; different cortical targets; do not merge.

    - PULVINAR vs. LD (intra-group): the pulvinar is the visual
      association relay; the LD is the limbic-adjacent association
      relay. Different domains; do not merge.

    - PULVINAR vs. MEDIAL GENICULATE BODY (MGN; auditory first-order
      relay): the pulvinar is the visual HIGHER-ORDER relay; the MGN is
      the auditory FIRST-ORDER relay. Different modalities; different
      relay types; do not merge.

    - PULVINAR vs. SUPERIOR COLLICULUS (subcortical visual
      structure): the superior colliculus is a MIDBRAIN visual-motor
      structure (orienting, saccades); the pulvinar is a THALAMIC
      visual-association relay. Both are involved in visual attention,
      but the colliculus is a subcortical orienting hub and the
      pulvinar is a cortical-association relay. Distinct structures;
      do not merge.

Functional Mode:
    - Visual association (the pulvinar's anchor role):
        * The pulvinar is the thalamic relay of the visual association
          hierarchy: it receives cortical layer 5 driver input from
          the visual cortices (V1–V5, MT) and projects back to the
          visual association cortices (V2–V5, MT, IT). This is the
          thalamo-cortical loop that supports visual feature
          integration, object recognition, and visual scene analysis.
    - Visual attention (the pulvinar's most distinctive function):
        * The pulvinar is a KEY node in the visual attention network.
          It contributes to:
            - Spatial attention: shifting attention to locations in
              space (particularly the contralateral hemifield).
            - Distractor filtering: suppressing responses to
              behaviorally irrelevant visual stimuli (the pulvinar is
              part of the "attentional filter" that gates visual
              salience).
            - Visual salience: promoting the representation of
              behaviorally relevant stimuli at the expense of
              irrelevant ones.
        * The pulvinar's attention role is one of the most studied
          higher-order thalamic functions; it is the anatomical
          basis of the pulvinar's clinical signature (visual neglect
          from pulvinar lesions).
    - Visual-motor integration (secondary; especially the inferior
      pulvinar):
        * The inferior pulvinar, adjacent to MT/V5, contributes to
          motion processing and to the subcortical visual pathway
          (superior colliculus → pulvinar → MT); it is less studied
          than the lateral pulvinar's visual-association role.
    - Multisensory / higher-order association (medial pulvinar):
        * The medial pulvinar receives parietal, temporal, and
          prefrontal inputs and projects to those same regions; it
          contributes to multimodal association, attention to
          behaviorally relevant stimuli across modalities, and to
          the integration of visual information with parietal and
          temporal association.
    - The pulvinar is therefore the THALAMUS'S VISUAL ASSOCIATION
      RELAY and one of the thalamus's principal attention hubs. It is
      the natural counterpart, in the visual-association domain, to
      the LP's parietal-association role and the LD's limbic-adjacent
      role.

    - CLINICAL FACT (the pulvinar's defining clinical anchor;
      contralateral):
        * Pulvinar lesions can produce VISUAL ATTENTIONAL DEFICITS,
          particularly:
            - Contralateral spatial neglect-like symptoms (a LEFT
              pulvinar lesion produces RIGHT hemifield neglect-like
              deficits; a RIGHT pulvinar lesion produces LEFT
              hemifield neglect-like deficits — the contralateral
              specification is anatomically meaningful and must be
              stated explicitly).
            - Contralateral visual salience deficits (reduced
              response to behaviorally relevant stimuli in the
              affected hemifield).
            - Contralateral distractor filtering deficits (impaired
              suppression of irrelevant stimuli).
        * The pulvinar's clinical picture OVERLAPS with posterior
          parietal and superior colliculus lesions (all are in the
          visual attention network); the pulvinar's specific
          contribution is the THALAMIC relay component of that
          network.
        * The pulvinar is one of the thalamic nuclei whose lesions
          produce a specific cortical-like syndrome (visual neglect),
          making it a genuine clinical anchor (unlike the LD, which
          has no specific syndrome). Documented as established.

Hormonal Modulation (minimal; the pulvinar is a higher-order
association relay):
    - The pulvinar is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) arousal inputs contribute to the attentional gating
      of the visual-association relay. The pulvinar's attention role
      is modulated by these same ascending arousal systems.
    - The pulvinar is NOT a principal target of the 12 endocrine axes.
      Do not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * semantic: the pulvinar's visual association loops contribute
          to visual object knowledge (semantic visual representations)
          via the IT and V4 connections.
        * short_term: the current state of the pulvinar's visual
          attention buffer (the spatial attention state it is
          currently gating).
        * episodic: some pulvinar-hippocampal-adjacent contributions to
          episodic visual memory (secondary; the pulvinar's primary
          role is visual association, not memory).
    - Writes: none directly. The pulvinar is a RELAY: it transmits
      association signals between cortical areas; the memory content
      is stored in the cortex, not the thalamus.
    - The pulvinar's memory interfaces are THICKER than the LD's and LP's
      on the SEMANTIC dimension (visual object knowledge); thinner on
      the episodic dimension (the pulvinar is not a Papez-adjacent
      relay).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No pulvinar fragment. The pulvinar is a higher-order association
      relay; the model prompt does not need a pulvinar block because
      the association signals it relays are already represented in
      the upstream (visual cortex) and downstream (visual association
      cortex, parietal and temporal association) fragments. The
      cortex carries the visual-association state.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The pulvinar's clinical fact (contralateral visual neglect) is
      documented for completeness, but is not a prompt field.

Reciprocal Connections (left-side; the right side is in
../../../../right/lateral_nuclear_group/pulvinar/):

    Visual association (the anchor):
    - ← telencephalon/cerebral_hemispheres/left/cortex/occipital/*
      (V1–V5, MT; cortical layer 5 driver input from the left visual
      cortices).
    - → telencephalon/cerebral_hemispheres/left/cortex/occipital/*
      (V2–V5, MT; pulvinar output to the left visual association
      cortices).
    - → telencephalon/cerebral_hemispheres/left/cortex/temporal/*
      (IT; pulvinar output to the left inferior temporal association
      cortex; the object-recognition pathway).
    - → telencephalon/cerebral_hemispheres/left/cortex/parietal/*
      (posterior parietal; medial pulvinar projection to the left
      parietal association cortex).

    Intra-group:
    - → ../lateral_posterior_nucleus/ (left pulvinar → left LP; the
      pulvinar projects to the LP as part of the parietal association
      circuit; intra-group edge).
    - ↔ ../lateral_dorsal_nucleus/ (left LD; limbic-adjacent
      association relay; different domain; do not merge).

    Subcortical visual-motor (secondary; especially inferior pulvinar):
    - ↔ midbrain/.../superior_colliculus (the subcortical visual
      pathway; the inferior pulvinar receives from and projects to
      the superior colliculus as part of the tecto-pulvinar-MT
      pathway; the superior colliculus is midline-adjacent — verify).

    Distinction (not signaling; structural note):
    - ↔ ../../metathalamus/lateral_geniculate_body (the LGN is the
      FIRST-ORDER visual relay; the pulvinar is the HIGHER-ORDER
      visual association relay; different relay types; do not merge).
    - ↔ ../../medial_nuclear_group/medial_dorsal_nucleus (the
      medial pulvinar projects to the prefrontal cortex alongside the
      MD; the two are distinct higher-order relays; do not merge).

Notes:
    - Tier 1 full leaf (left). The LARGEST nucleus of the lateral
      group and the group's clinical anchor. The pulvinar's literature
      is heavier than the LD's and LP's; the leaf is correspondingly
      longer (~110 lines, vs. the LD's ~70 and the LP's ~85).
    - THE PULVINAR vs. LP TRAP is the group's signature trap; the
      pulvinar leaf enforces it from the pulvinar side, matching the
      LP leaf's enforcement from the LP side. Together they make the
      trap fully declared on both sides.
    - THE PULVINAR vs. LGN TRAP is a NEW trap declared in this leaf:
      the LGN is the FIRST-ORDER visual relay (retina → LGN → V1);
      the pulvinar is the HIGHER-ORDER visual association relay
      (cortical layer 5 → pulvinar → visual association). Both are
      thalamic visual relays, but of different orders. Do not merge.
    - THE THREE SUBREGIONS (lateral, medial, inferior) are documented
      WITHIN this leaf, not as child nodes. Same convention as the
      habenula's LHb/MHb, the PVN's sub-populations, and the
      mammillary bodies' MM/LM. Do not create lateral_pulvinar/,
      medial_pulvinar/, or inferior_pulvinar/ as child nodes.
    - CONTRAALTERAL CLINICAL FACT: left pulvinar lesion → RIGHT
      hemifield neglect-like deficits (the right pulvinar leaf's delta
      will document the reverse: right pulvinar lesion → LEFT
      hemifield deficits). The contralateral direction is stated
      explicitly; the right delta will state the reverse explicitly.
    - THE PULVINAR'S CLINICAL ANCHOR IS ESTABLISHED (unlike the LD's
      and LP's, which are "part of a broader picture" or "rare in
      isolation"). The pulvinar lesion produces a genuine
      visual-attention syndrome; this is the group's one established
      clinical anchor.
    - NO FRAGMENT: same as the whole thalamus. The pulvinar is a
      relay, not a state-emitter.
    - The pulvinar is NOT the LP (parietal association), NOT the LGN
      (first-order visual), NOT the LD (limbic-adjacent), NOT the MGN
      (first-order auditory), NOT the superior colliculus (midbrain
      orienting). The traps make these distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (semantic, short_term, episodic); gateway/.
    - Connects upward to diencephalon/thalamus/left/lateral_nuclear_
      group/.
"""