"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.lateral_nuclear_group.lateral_posterior_nucleus
Anatomical Role:
    The right lateral posterior nucleus (LP). A medium-sized nucleus in
    the right lateral nuclear group, situated between the right lateral
    dorsal nucleus (LD) and the right pulvinar. Same PARIETAL
    ASSOCIATION relay role as the left LP: its driver input is primarily
    from the right parietal cortex (and from the right pulvinar), and
    its output is to the right posterior parietal cortex (areas 5, 7,
    and adjacent).

    See ../../../../left/lateral_nuclear_group/lateral_posterior_
    nucleus/__init__.py for the full anatomical description, the
    second-anchor framing, the four traps (LP vs. pulvinar; LP vs. LD;
    LP vs. VPL/VPM; LP vs. anterior group), the multisensory and
    parietal-hippocampal secondary roles, and the honest LP-specific
    syndrome stance.

    Reproduced distinctions (apply equally on the right):
    - LP vs. PULVINAR (group's signature trap): right LP = parietal
      association; right pulvinar = visual association. Different
      domains; do not merge.
    - LP vs. LD (intra-group): right LP = parietal association; right
      LD = limbic-adjacent association. Different domains; do not
      merge.
    - LP vs. VPL/VPM (subtle, new): both project to the parietal lobe,
      but the right LP is a HIGHER-ORDER PARIETAL ASSOCIATION relay
      (posterior parietal, areas 5/7, cortical layer 5 driver) while
      the right VPL/VPM (right/ventral_nuclear_group/ventral_posterior_
      nucleus/) are FIRST-ORDER SOMATOSENSORY relays (primary
      somatosensory S1, areas 3/1/2, peripheral driver). Different
      relay types; different cortical targets; do not merge.
    - LP vs. ANTERIOR NUCLEAR GROUP: right LP = parietal association
      relay; right anterior nuclei = Papez memory relays. Different
      circuits; do not merge.

Functional Mode:
    Same as ../../../../left/lateral_nuclear_group/lateral_posterior_
    nucleus/. Parietal association (the anchor: spatial attention,
    visuomotor integration, multisensory integration); parietal-
    hippocampal interaction (secondary). No documented functional
    asymmetry between left and right LP. Do not fabricate one.

    CLINICAL FACT (contralateral; reversed relative to the left leaf):
        * Right LP lesions can produce PARIETAL-LIKE DEFICITS, and
          the deficits are CONTRALATERAL — a RIGHT LP lesion produces
          LEFT hemifield deficits:
            - Left hemifield spatial attention deficits (left
              hemispatial neglect-like symptoms).
            - Left visuomotor integration deficits (optic
              ataxia-like symptoms).
            - Left multisensory integration deficits.
        * The left LP leaf documents the reverse: a LEFT LP lesion
          produces RIGHT hemifield deficits.
        * The two leaves together document the full contralateral
          pattern with the correct direction on each side. Do not
          flatten to "LP lesion causes parietal deficits" without
          specifying the side.
        * LP-SPECIFIC syndromes (isolated right LP lesion without
          adjacent thalamic involvement) are RARE. Document honestly;
          do not claim an LP-specific syndrome beyond the broader
          "parietal-like" picture.

Hormonal Modulation:
    Same as ../../../../left/lateral_nuclear_group/lateral_posterior_
    nucleus/. Minimal; cholinergic and monoaminergic arousal modulation;
    not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/lateral_nuclear_group/lateral_posterior_
    nucleus/. Reads short_term (parietal spatial-attention buffer),
    semantic (parietal semantic association), episodic (secondary;
    parietal-hippocampal-adjacent). Writes nothing directly (relay,
    not encoder).

Model Integration (Gemma-4-E2B):
    No right LP fragment. Same as ../../../../left/lateral_nuclear_
    group/lateral_posterior_nucleus/ and the whole thalamus: the LP is
    a higher-order parietal association relay; the model prompt does
    not need an LP block. The association state is carried by the
    right posterior parietal cortex.

Right-specific reciprocal connections to enforce in Stage 4:

    Parietal association (the anchor):
    - ← telencephalon/cerebral_hemispheres/right/cortex/parietal/
      posterior_parietal_cortex (cortical layer 5 input from the right
      posterior parietal cortex; the right LP's driver input;
      right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/
      posterior_parietal_cortex (right LP output to the right
      posterior parietal cortex; the higher-order parietal association
      loop; right-side).
    - ← ../pulvinar/ (right pulvinar → right LP; the pulvinar projects
      to the LP as part of the parietal association circuit;
      intra-group edge; right-side).

    Multisensory integration (secondary):
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/parietal/*
      (right parietal multisensory integration; the right LP relays
      the cortico-cortical association that supports it; right-side).

    Parietal-hippocampal interaction (secondary):
    - ↔ telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/hippocampus/right (hippocampal-adjacent
      input to the right LP; secondary contribution to spatial memory;
      right-side).
    - ↔ telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      retrosplenial_cortex (retrosplenial-adjacent projection;
      secondary contribution to spatial memory; right-side).

    Intra-group:
    - ↔ ../lateral_dorsal_nucleus/ (right LD; limbic-adjacent
      association; different domain; do not merge).
    - ↔ ../pulvinar/ (right pulvinar; visual association; different
      domain; do not merge).

    Distinction (not signaling; structural note):
    - ↔ ../../ventral_nuclear_group/ventral_posterior_nucleus (the
      right LP and right VPL both project to the parietal lobe, but the
      right LP targets POSTERIOR parietal association cortex (5/7)
      while right VPL targets PRIMARY somatosensory cortex (S1, 3/1/2);
      different relay types; do not merge).

    - ↔ ../../../../left/lateral_nuclear_group/lateral_posterior_
      nucleus/ (hemisphere counterpart; no functional asymmetry
      assumed; but see the contralateral clinical fact — the left and
      right LP lesions produce opposite-side deficits, which is a real
      directional fact, not a functional asymmetry of the nuclei
      themselves).

Notes:
    - Delta file of ../../../../left/lateral_nuclear_group/
      lateral_posterior_nucleus/. Not a full leaf. Do not duplicate.
    - THE LP vs. PULVINAR TRAP is reproduced in abbreviated form; the
      full text is in ../../../../left/lateral_nuclear_group/
      lateral_posterior_nucleus/ and ../../../__init__.py. A
      contributor entering at the right LP must see it.
    - THE LP vs. VPL/VPM TRAP (new, declared in the left LP leaf) is
      reproduced in abbreviated form. Same trap applies on the right:
      the right LP targets posterior parietal association cortex (5/7);
      the right VPL targets primary somatosensory cortex (S1, 3/1/2).
      Different relay types; different cortical targets.
    - THE CONTRALATERAL CLINICAL FACT IS REVERSED ON THE RIGHT: right LP
      lesion → LEFT hemifield deficits (left LP lesion → RIGHT hemifield
      deficits). This is the ONLY substantive content difference between
      the left and right LP leaves (same pattern as the STN right delta
      and the pulvinar right delta), and it is documented explicitly.
    - LP-SPECIFIC SYNDROME HONESTY: isolated right LP lesions are rare;
      no right-LP-specific syndrome is established. Do not claim one.
    - NO FRAGMENT: same as the whole thalamus. The right LP is a relay,
      not a state-emitter.
    - The right LP is NOT the right pulvinar (visual association), NOT
      the right LD (limbic-adjacent association), NOT the right VPL/VPM
      (first-order somatosensory), NOT the right anterior nuclei (Papez
      memory). The traps make these distinctions explicit on the right.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right posterior parietal cortex, right pulvinar, right
      hippocampus, right retrosplenial cortex, right VPL/VPM for the
      structural distinction). Stage 4 should not confuse right-side
      edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/lateral_nuclear_group/lateral_posterior_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/lateral_nuclear_
      group/.
"""