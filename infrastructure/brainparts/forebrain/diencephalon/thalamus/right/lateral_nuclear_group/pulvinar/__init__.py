"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.lateral_nuclear_group.pulvinar
Anatomical Role:
    The right pulvinar. The LARGEST nucleus of the right lateral nuclear
    group and one of the largest nuclei in the entire right thalamus,
    forming the posterior pole of the right thalamus. Same VISUAL
    ASSOCIATION RELAY role as the left pulvinar: driver input from the
    right visual cortices (V1–V5, MT) and output to the right visual
    association cortices (V2–V5, MT, IT) and to the right parietal and
    temporal association cortices.

    THREE SUBREGIONS (documented WITHIN this leaf, not as child nodes;
    same convention as ../../../../left/lateral_nuclear_group/
    pulvinar/):
        - Lateral pulvinar: visual association (V1, V2, V4, MT → V2,
          V4, V5/MT, IT).
        - Medial pulvinar: multisensory / higher-order association
          (parietal + temporal + PFC → parietal + temporal + PFC).
        - Inferior pulvinar: motion / subcortical visual (superior
          colliculus + MT → MT).
    Do not create lateral_pulvinar/, medial_pulvinar/, or
    inferior_pulvinar/ as child nodes here either.

    Reproduced distinctions (apply equally on the right):
    - PULVINAR vs. LATERAL POSTERIOR (group's signature trap): right
      pulvinar = visual association; right LP = parietal association.
      Different domains; do not merge.
    - PULVINAR vs. LGN (subtle): the right LGN
      (right/metathalamus/lateral_geniculate_body/) is the FIRST-ORDER
      visual relay (retina → LGN → V1); the right pulvinar is the
      HIGHER-ORDER visual association relay (cortical layer 5 →
      pulvinar → visual association). Different relay types; do not
      merge.
    - PULVINAR vs. LD: right pulvinar = visual association; right LD
      = limbic-adjacent association. Different domains; do not merge.
    - PULVINAR vs. MGN: right pulvinar = visual HIGHER-ORDER relay;
      right MGN (right/metathalamus/medial_geniculate_body/) =
      auditory FIRST-ORDER relay. Different modalities; different
      relay types; do not merge.
    - PULVINAR vs. SUPERIOR COLLICULUS: the right superior colliculus
      is a midbrain visual-motor structure (orienting, saccades); the
      right pulvinar is a thalamic visual-association relay. Both are
      in the visual attention network; distinct structures; do not
      merge.

Functional Mode:
    Same as ../../../../left/lateral_nuclear_group/pulvinar/:
    visual association (the anchor); visual attention (spatial
    attention, distractor filtering, salience); visual-motor
    integration (secondary; especially inferior pulvinar); multisensory
    / higher-order association (medial pulvinar). No documented
    functional asymmetry between left and right pulvinar. Do not
    fabricate one.

    CLINICAL FACT (contralateral; reversed relative to the left leaf):
        * Right pulvinar lesions can produce VISUAL ATTENTIONAL
          DEFICITS, and the deficits are CONTRALATERAL — a RIGHT
          pulvinar lesion produces LEFT hemifield deficits:
            - LEFT hemifield spatial neglect-like symptoms.
            - LEFT hemifield visual salience deficits.
            - LEFT hemifield distractor filtering deficits.
        * The left pulvinar leaf documents the reverse: a LEFT
          pulvinar lesion produces RIGHT hemifield deficits.
        * The two leaves together document the full contralateral
          pattern with the correct direction on each side. Do not
          flatten to "pulvinar lesion causes neglect" without
          specifying the side.
        * The pulvinar's clinical anchor (contralateral visual
          neglect-like deficit) is ESTABLISHED on both hemispheres,
          unlike the LD's "no specific syndrome" or the LP's "rare in
          isolation."

Hormonal Modulation:
    Same as ../../../../left/lateral_nuclear_group/pulvinar/. Minimal;
    cholinergic and monoaminergic arousal modulation of the visual
    attention relay; not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/lateral_nuclear_group/pulvinar/. Reads
    semantic (visual object knowledge via IT/V4), short_term (visual
    attention buffer), episodic (secondary; pulvinar-hippocampal-
    adjacent). Writes nothing directly (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right pulvinar fragment. The pulvinar is a higher-order visual
    association relay; the model prompt does not need a pulvinar block.
    The visual-association state is carried by the right visual
    association cortex.

Right-specific reciprocal connections to enforce in Stage 4:

    Visual association (the anchor):
    - ← telencephalon/cerebral_hemispheres/right/cortex/occipital/*
      (V1–V5, MT; cortical layer 5 driver input; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/occipital/*
      (V2–V5, MT; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/temporal/*
      (IT; right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/*
      (posterior parietal; medial pulvinar projection; right-side).

    Intra-group:
    - → ../lateral_posterior_nucleus/ (right pulvinar → right LP;
      parietal association circuit; intra-group edge; right-side).
    - ↔ ../lateral_dorsal_nucleus/ (right LD; limbic-adjacent
      association; different domain; do not merge).

    Subcortical visual-motor (secondary; especially inferior pulvinar):
    - ↔ midbrain/.../superior_colliculus (right tecto-pulvinar-MT
      pathway; the superior colliculus is midline-adjacent — verify).

    Distinction (not signaling; structural note):
    - ↔ ../../metathalamus/lateral_geniculate_body (right LGN is the
      FIRST-ORDER visual relay; right pulvinar is the HIGHER-ORDER
      visual association relay; different relay types; do not merge).
    - ↔ ../../medial_nuclear_group/medial_dorsal_nucleus (the right
      medial pulvinar projects to the right prefrontal cortex
      alongside the right MD; distinct higher-order relays; do not
      merge).

    - ↔ ../../../../left/lateral_nuclear_group/pulvinar/ (hemisphere
      counterpart; no functional asymmetry assumed; but see the
      contralateral clinical fact — left and right pulvinar lesions
      produce opposite-side deficits, which is a real directional
      fact, not a functional asymmetry of the nuclei themselves).

Notes:
    - Delta file of ../../../../left/lateral_nuclear_group/pulvinar/.
      Not a full leaf. Do not duplicate.
    - THE FINAL FILE IN THE ENTIRE LATERAL NUCLEAR GROUP. With this
      file, the lateral nuclear group is complete: 2 containers + 3
      left leaves + 3 right deltas = 8 files.
    - THE PULVINAR vs. LP TRAP is reproduced in abbreviated form; the
      full text is in ../../../../left/lateral_nuclear_group/
      pulvinar/ and ../../../__init__.py. A contributor entering at the
      right pulvinar must see it.
    - THE PULVINAR vs. LGN TRAP (new, declared in the left pulvinar
      leaf) is reproduced in abbreviated form. The right LGN is the
      FIRST-ORDER visual relay; the right pulvinar is the HIGHER-ORDER
      visual association relay. Different relay types; do not merge.
    - THE CONTRALATERAL CLINICAL FACT IS REVERSED ON THE RIGHT: right
      pulvinar lesion → LEFT hemifield neglect-like deficit (left
      pulvinar lesion → RIGHT hemifield deficit). This is the ONLY
      substantive content difference between the left and right
      pulvinar leaves, matching the pattern of the STN pair and the
      LP pair.
    - THE PULVINAR'S CLINICAL ANCHOR IS ESTABLISHED on both
      hemispheres (the group's one established clinical anchor,
      unlike the LD's "no specific syndrome" and the LP's "rare in
      isolation").
    - THE THREE SUBREGIONS are documented WITHIN the leaf, not as
      child nodes, same as the left leaf. Do not create
      lateral_pulvinar/, medial_pulvinar/, or inferior_pulvinar/ as
      child nodes on the right either.
    - NO FRAGMENT: same as the whole thalamus. The right pulvinar is a
      relay, not a state-emitter.
    - The right pulvinar is NOT the right LP (parietal association),
      NOT the right LGN (first-order visual), NOT the right LD
      (limbic-adjacent), NOT the right MGN (first-order auditory),
      NOT the right superior colliculus (midbrain orienting). The
      traps make these distinctions explicit on the right.
    - Midline targets (superior colliculus) are flagged with "verify"
      so Stage 4 does not force a hemisphere split on structures that
      are not hemisphere-split in the tree. Right V1–V5, MT, IT,
      right parietal, right LP, right LD, right MD, right LGN, right
      MGN, and right prefrontal cortex are hemisphere-split and
      require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/lateral_nuclear_group/pulvinar/ § Notes for
      the full list.
    - Connects upward to diencephalon/thalamus/right/lateral_nuclear_
      group/.
"""