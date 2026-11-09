"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.metathalamus
Anatomical Role:
    The right metathalamus. Same group of two first-order sensory relay
    nuclei at the CAUDAL pole of the right thalamus documented in
    ../../left/metathalamus/:
        - lateral_geniculate_body/ (LGN): the FIRST-ORDER VISUAL relay.
          Receives retinal input via the right optic tract; projects to
          the right primary visual cortex (V1) via the right optic
          radiation.
        - medial_geniculate_body/ (MGN): the FIRST-ORDER AUDITORY relay.
          Receives ascending auditory input from the right inferior
          colliculus; projects to the right primary auditory cortex
          (A1) via the right acoustic radiation.
    See ../../left/metathalamus/__init__.py for the full anatomical
    description, the two-nucleus framing, the six-layer LGN structure,
    the three-division MGN structure, the modality-specific clinical
    anchors, and the "metathalamus is the cleanest first-order sensory
    group" framing.

    Reproduced FOUR TRAPS (apply equally on the right):

    - TRAP 1: LGN vs. MGN (the group's signature trap). Both are
      "geniculate bodies," both in the metathalamus, both first-order
      sensory relays. But the right LGN is VISUAL (right retina →
      right LGN → right V1) and the right MGN is AUDITORY (right
      inferior colliculus → right MGN → right A1). Different
      modalities; do not merge.

    - TRAP 2: LGN vs. PULVINAR (the canonical cross-group
      first-order-vs-higher-order trap; declared from the pulvinar
      side in right/lateral_nuclear_group/pulvinar/; THIS CONTAINER
      IS THE CANONICAL DECLARATION FROM THE FIRST-ORDER SIDE for the
      right hemisphere). The right LGN is the FIRST-ORDER visual relay
      (retinal driver; right V1 target); the right pulvinar is the
      HIGHER-ORDER visual association relay (cortical layer 5 driver;
      right V2–V5/MT/IT target). Both are right thalamic visual
      relays, but of different ORDERS. Do not merge.

    - TRAP 3: MGN vs. HIGHER-ORDER AUDITORY CORTEX (the first-order
      vs. higher-order auditory trap). The right MGN's VENTRAL division
      is the canonical first-order auditory relay (right inferior
      colliculus driver; right A1 target); the right MGN's MEDIAL and
      DORSAL divisions contribute higher-order auditory and
      multisensory association. Do not treat all right MGN output as
      "primary auditory."

    - TRAP 4: METATHALAMUS vs. THALAMUS PROPER (name trap). The name
      "metathalamus" means "beyond the thalamus," but the right
      metathalamus is a SUBDIVISION OF the right thalamus at its
      caudal pole, not a structure beyond it. Do not move the
      metathalamus out of thalamus/right/ or treat it as a separate
      anatomical entity.

Functional Mode:
    Same as ../../left/metathalamus/. First-order visual relay (LGN;
    the anchor role); first-order auditory relay (MGN; the second
    role); first-order sensory relay pattern (the metathalamus's
    defining functional architecture). No documented functional
    asymmetry between left and right metathalamus. Do not fabricate
    one.

    CLINICAL FACTS (apply on the right identically, with
    CONTRALATERAL specification):
        * RIGHT LGN LESIONS: produce CONTRALATERAL HOMONYMOUS
          HEMIANOPIA — a RIGHT LGN lesion produces a LEFT homonymous
          hemianopia (loss of the LEFT visual hemifield in both eyes).
          The LEFT LGN lesion produces a RIGHT homonymous hemianopia
          (documented in ../../left/metathalamus/). The two leaves
          together document the full contralateral pattern with the
          correct direction on each side. This is the same pattern as
          the LP and pulvinar pairs — the contralateral direction is
          anatomically meaningful and must be stated explicitly. Do
          not flatten to "LGN lesion causes hemianopia" without
          specifying the side.
        * RIGHT MGN LESIONS: produce AUDITORY PROCESSING DEFICITS
          (typically subtle; the ascending auditory pathway is
          bilateral above the cochlear nuclei, so unilateral MGN
          lesions produce little or no hearing loss).
        * Right LGN is also affected in some right optic neuropathies
          (trans-synaptic degeneration from right retinal ganglion
          cell loss) and in some right thalamic strokes (right LGN in
          the right posterior cerebral artery territory).

Hormonal Modulation:
    Same as ../../left/metathalamus/. Minimal; cholinergic and
    monoaminergic arousal modulation of the LGN's and MGN's sensory
    relay gain. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../left/metathalamus/. Right LGN reads short_term
    (visual sensory buffer); right MGN reads short_term (auditory
    sensory buffer). Writes nothing directly (sensory relays, not
    memory structures). Thin interface; do not pad.

Model Integration (Gemma-4-E2B):
    No right metathalamus fragment. Same as ../../left/ and the whole
    thalamus: the metathalamus is a first-order sensory relay group,
    not a state-emitter. The visual and auditory sensory states are
    carried by the right V1 and right A1 upstream/downstream
    fragments.

Children (two children — all right-side deltas of their left
counterparts):
    - lateral_geniculate_body/   ★ Delta of ../../left/metathalamus/
                                  lateral_geniculate_body/. Right LGN;
                                  first-order visual relay.
    - medial_geniculate_body/    ★ Delta of ../../left/metathalamus/
                                  medial_geniculate_body/. Right MGN;
                                  first-order auditory relay.

    Each of these two right nuclei is a DELTA of its left counterpart;
    no full right-side leaves are needed. The left side carries the
    substantive content; the right side records only right-side
    reciprocal edges and reproduces the traps.

Right-specific reciprocal connections to enforce in Stage 4:

    First-order visual relay (right LGN):
    - ← right retina (via the right optic tract; the retina is NOT a
      tree node — document as a named external relay).
    - → telencephalon/cerebral_hemispheres/right/cortex/occipital/
      primary_visual_cortex (right V1; via the right optic
      radiation; right-side).

    First-order auditory relay (right MGN):
    - ← midbrain/.../inferior_colliculus (via the right brachium of
      the inferior colliculus; the inferior colliculus is
      midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/temporal/
      primary_auditory_cortex (right A1; via the right acoustic
      radiation; right-side).

    Intra-group:
    - ↔ ../lateral_geniculate_body/ (right LGN ↔ right MGN;
      anatomically adjacent within the right metathalamus; different
      modalities; do not merge).

    Cross-group:
    - ↔ ../../lateral_nuclear_group/pulvinar/ (right LGN ↔ right
      pulvinar; adjacent right thalamic visual relays; LGN =
      first-order; pulvinar = higher-order; distinct relay types; do
      not merge; the canonical first-order-vs-higher-order trap).

    - ↔ ../../left/metathalamus/ (hemisphere counterpart; no
      functional asymmetry assumed; but see the CONTRALATERAL clinical
      fact — right and left LGN lesions produce opposite-side
      hemianopias, which is a real directional fact, not a functional
      asymmetry of the nuclei themselves).

Notes:
    - Group-container delta of ../../left/metathalamus/. Not a full
      container. Do not duplicate the left group's content.
    - FOUR TRAPS reproduced in abbreviated form above; the full text
      is in ../../left/metathalamus/ and ../../__init__.py. A
      contributor entering at the right metathalamus must see them.
    - DELTA-OF-A-DELTA CHAIN EXTENDS TO THIS GROUP: the two right
      nuclei (LGN, MGN) are each deltas of their left counterparts,
      same as every other thalamic right leaf.
    - THE CONTRALATERAL CLINICAL FACT IS REVERSED ON THE RIGHT: a
      right LGN lesion produces LEFT homonymous hemianopia (the left
      LGN leaf documents the RIGHT homonymous hemianopia). This is
      the ONLY substantive content difference between the left and
      right metathalamus at the container level; the LGN right delta
      will carry the full clinical fact on the right.
    - THE METATHALAMUS IS A FIRST-ORDER SENSORY GROUP: same on the
      right. The right LGN and right MGN are canonical first-order
      relays, not higher-order association relays.
    - THE METATHALAMUS IS THE PATTERN FOR THE VENTRAL GROUP'S VPL/VPM:
      the right first-order sensory relay pattern established here
      will carry through to the right VPL/VPM (body/face
      somatosensory) when the ventral group is drafted on the right.
    - NO FRAGMENT: same as the whole thalamus. The right metathalamus
      is a relay group, not a state-emitter.
    - Midline targets (inferior colliculus) are flagged with "verify"
      so Stage 4 does not force a hemisphere split on structures that
      are not hemisphere-split in the tree. Right retina, right V1,
      right A1, right optic radiation, right acoustic radiation,
      right LGN, right MGN, and right pulvinar are hemisphere-split
      and require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/metathalamus/ § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/.
"""