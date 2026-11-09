"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.lateral_nuclear_group
Anatomical Role:
    The right lateral nuclear group of the thalamus. Same three nuclei
    on the lateral aspect of the right thalamus documented in
    ../../left/lateral_nuclear_group/:
        - lateral_dorsal_nucleus/ (LD): limbic-adjacent association;
          LD → right cingulate and retrosplenial. Least characterized.
        - lateral_posterior_nucleus/ (LP): parietal association;
          LP → right posterior parietal cortex. Second anchor.
        - pulvinar/ (★): visual association; pulvinar → right visual
          association cortices. The anchor nucleus of the group.

    See ../../left/lateral_nuclear_group/__init__.py for the full
    anatomical description, the higher-order association framing, the
    pulvinar vs. LP trap, the LD honesty, the pulvinar subregion
    breakdown, and the group's clinical anchor (pulvinar visual
    attention).

    Reproduced distinctions (apply equally on the right):
    - PULVINAR vs. LP (group's signature trap): right pulvinar =
      visual association; right LP = parietal association. Different
      cortical targets; do not merge.
    - LATERAL GROUP vs. ANTERIOR GROUP: right lateral group is
      cortico-cortical association; right anterior group
      (right/anterior_nuclear_group/) is Papez memory relay. Different
      circuits; do not merge.
    - LATERAL GROUP vs. VENTRAL GROUP: right lateral group relays
      cortico-cortical association; right ventral group
      (right/ventral_nuclear_group/) relays first-order sensory (VPL/
      VPM) and motor (VA/VL). Different relay types; do not merge.
    - LATERAL DORSAL vs. ANTERIOR NUCLEAR GROUP (subtle): the right LD
      projects to the right cingulate and retrosplenial (same cortical
      targets as the right anterior nuclei), but the right LD is a
      HIGHER-ORDER ASSOCIATION relay (cortical layer 5 driver), not a
      Papez memory relay (hippocampal/mammillary driver). Distinct
      circuits; do not merge.

Functional Mode:
    Same as ../../left/lateral_nuclear_group/. Visual association
    (pulvinar; anchor role); parietal association (LP; second role);
    limbic-adjacent association (LD; tertiary, least characterized).
    No documented functional asymmetry between left and right lateral
    nuclear groups. Do not fabricate one.

    CLINICAL FACT (the group's clinical anchor): right pulvinar lesions
    can produce VISUAL ATTENTIONAL DEFICITS (left hemifield spatial
    neglect-like symptoms; the contralateral hemifield to the right
    pulvinar lesion) and VISUAL ASSOCIATION DEFICITS (integration and
    salience impairments). Right LP lesions can produce
    PARIETAL-LIKE DEFICITS (left-sided spatial attention,
    visuomotor integration). Right LD lesions are rare in isolation.
    See ../../left/lateral_nuclear_group/ § Functional Mode for the
    full description.

Hormonal Modulation:
    Same as ../../left/lateral_nuclear_group/. Minimal; cholinergic
    and monoaminergic arousal modulation; not a principal target of
    the 12 endocrine axes.

Memory Interfaces:
    Same as ../../left/lateral_nuclear_group/. Reads episodic (via the
    right LD's limbic-adjacent role), semantic (via the right pulvinar
    and right LP's association loops), short_term (all three relay the
    current state of their cortical loops). Writes nothing directly
    (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right lateral group fragment. Same as ../../left/ and the whole
    thalamus: the lateral group is an association relay, not a
    state-emitter. The model-relevant state is carried by the right
    visual cortex, right parietal cortex, and right cingulate cortex.

Children (three children — all right-side deltas of their left
counterparts):
    - lateral_dorsal_nucleus/    Delta of ../../left/lateral_nuclear_
                                   group/lateral_dorsal_nucleus/.
                                   Right LD; limbic-adjacent.
    - lateral_posterior_nucleus/ Delta of ../../left/lateral_nuclear_
                                   group/lateral_posterior_nucleus/.
                                   Right LP; parietal association.
    - pulvinar/                  ★ Delta of ../../left/lateral_nuclear_
                                   group/pulvinar/. Right pulvinar;
                                   visual association; the anchor.

    Each of these three right nuclei is a DELTA of its left
    counterpart; no full right-side leaves are needed. The left side
    carries the substantive content; the right side records only
    right-side reciprocal edges and reproduces the traps.

Right-specific reciprocal connections to enforce in Stage 4:

    Visual association (pulvinar):
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/occipital/*
      (V2–V5, MT) and telencephalon/.../cortex/temporal/* (IT)
      (right pulvinar ↔ right visual association cortices;
      right-side).
    - ↔ right lateral_posterior_nucleus (intra-group: right pulvinar ↔
      right LP; the pulvinar projects to the LP as part of the
      parietal association circuit; distinct nuclei; do not merge).

    Parietal association (LP):
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/parietal/
      posterior_parietal_cortex (right LP ↔ right posterior parietal
      cortex; parietal association; right-side).

    Limbic-adjacent association (LD):
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate and retrosplenial_cortex (right LD →
      right cingulate + retrosplenial; higher-order limbic-adjacent
      association; right-side).

    - ↔ ../../left/lateral_nuclear_group/ (hemisphere counterpart; no
      functional asymmetry assumed; but see the clinical fact: the
      pulvinar and LP produce CONTRALATERAL effects, so the right and
      left hemispheres differ in the direction of the deficit — left
      lesion → right hemifield; right lesion → left hemifield — which
      is a real directional fact, not a functional asymmetry).

Notes:
    - Group-container delta of ../../left/lateral_nuclear_group/. Not a
      full container. Do not duplicate the left group's content.
    - THE PULVINAR vs. LP TRAP is reproduced in abbreviated form above;
      the full text is in ../../left/lateral_nuclear_group/ and
      ../../. A contributor entering at the right lateral group must
      see them.
    - DELTA-OF-A-DELTA CHAIN EXTENDS TO THIS GROUP: the three right
      nuclei (LD, LP, pulvinar) are each deltas of their left
      counterparts, same as every other thalamic right leaf.
    - THE CONTRALATERAL CLINICAL FACT: pulvinar and LP lesions produce
      CONTRALATERAL deficits (left pulvinar lesion → right hemifield
      neglect; right pulvinar lesion → left hemifield neglect). This
      is a DIRECTIONAL fact (contralateral projection), not a
      functional asymmetry of the nuclei themselves. The left and
      right leaves both document their respective clinical facts with
      the correct contralateral direction. Do not flatten to
      "pulvinar lesion causes neglect" without specifying the side.
    - THE LD HONESTY: the right LD is also the least characterized of
      the three right nuclei; document as "less well characterized"
      rather than inventing function.
    - THE LATERAL GROUP IS NOT A FIRST-ORDER SENSORY GROUP: same as
      the left. Right lateral group relays cortico-cortical
      association, not primary sensory input. Primary sensory relays
      are in the right ventral group (VPL/VPM) and right metathalamus
      (LGN/MGN).
    - THE PULVINAR IS ANCHOR on the right as well: largest, most
      studied, most visually salient, and the group's clinical
      anchor.
    - NO FRAGMENT: same as the whole thalamus. The right lateral group
      is a relay, not a state-emitter.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right visual association cortices, right posterior parietal
      cortex, right cingulate, right retrosplenial). Stage 4 should
      not confuse right-side edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/lateral_nuclear_group/ § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/.
"""