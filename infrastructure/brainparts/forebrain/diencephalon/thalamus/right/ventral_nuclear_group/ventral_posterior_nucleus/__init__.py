"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.ventral_nuclear_group.ventral_posterior_nucleus.ventral_posterior_lateral_nucleus
Anatomical Role:
    The right ventral posterior lateral nucleus (VPL). A first-order
    somatosensory relay in the right ventral nuclear group's ventral
    posterior sub-container, situated lateral to the right VPM and
    posterior to the right VL. Same BODY SOMATOSENSORY RELAY role as
    the left VPL: the thalamic relay of the ascending somatosensory
    pathways for the BODY (right medial lemniscus + right spinothalamic
    → right S1 body map).

    See ../../../../../../left/ventral_nuclear_group/ventral_posterior_
    nucleus/ventral_posterior_lateral_nucleus/__init__.py (to be
    drafted next; the source of truth for this delta) for the full
    anatomical description, the two-driver framing (medial lemniscus
    + spinothalamic), the shell/core subregion distinction, and the
    full clinical fact list.

    Reproduced distinctions (apply equally on the right):

    - VPL vs. VPM (SOMATOTOPIC-SPLIT trap; group signature): the right
      VPL is the BODY somatosensory relay (right medial lemniscus +
      right spinothalamic → right S1 body map); the right VPM
      (../ventral_posterior_medial_nucleus/) is the FACE somatosensory
      relay (right trigeminothalamic) plus the TASTE relay (right
      parabrachial → right VPMpc). Both are first-order somatosensory
      relays; the VPL/VPM split is a SOMATOTOPIC SPLIT of one
      functional system, not a functional split. Do not merge.

    - VPL's TWO DRIVERS (medial lemniscus + spinothalamic): the right
      VPL receives BOTH the right medial lemniscus (fine touch,
      vibration, proprioception) AND the right spinothalamic tract
      (pain, temperature, crude touch). Two separate drivers
      converging on the right VPL; do not treat it as a single
      undifferentiated somatosensory relay.

    - VPL/VPM vs. LP (cross-group first-order vs. higher-order;
      declared from the LP side; canonical first-order side declared
      in the right VP sub-container): the right VPL/VPM are FIRST-ORDER
      somatosensory relays (peripheral driver → right S1); the right
      LP (right/lateral_nuclear_group/lateral_posterior_nucleus/) is a
      HIGHER-ORDER parietal association relay (cortical layer 5 driver
      → right posterior parietal cortex, areas 5/7). Different relay
      types; do not merge.

    - VPL/VPM vs. Pf (cross-group first-order vs. nociceptive-affective;
      declared from the Pf side; canonical first-order side declared
      in the right VP sub-container): the right VPL/VPM carry the
      SENSORY-DISCRIMINATIVE dimension of pain; the right Pf
      (right/medial_nuclear_group/parafascicular_nucleus/) carries the
      AFFECTIVE-MOTIVATIONAL dimension. Do not merge.

Functional Mode:
    Same as the left VPL: first-order somatosensory relay for the BODY
    (discriminative touch, vibration, proprioception, and the
    sensory-discriminative dimension of pain for the contralateral
    body). No documented functional asymmetry between left and right
    VPL. Do not fabricate one.

    CLINICAL FACTS (apply on the right identically, with CONTRALATERAL
    specification):
        * RIGHT VPL LESIONS: produce CONTRALATERAL (LEFT) BODY
          SOMATOSENSORY DEFICITS — LEFT body hemianesthesia (loss of
          touch, vibration, proprioception, pain, temperature on the
          LEFT side of the body). The LEFT VPL leaf documents the
          reverse: a LEFT VPL lesion produces RIGHT body hemianesthesia.
          The two leaves together document the full contralateral
          pattern with the correct direction on each side; this is the
          fifth contralateral-clinical pair in the tree.
        * RIGHT VPL LESIONS AND THALAMIC PAIN SYNDROME (Dejerine-Roussy):
          chronic LEFT-sided pain after a right thalamic stroke, often
          with hyperalgesia and allodynia. The thalamic pain syndrome
          applies on the right identically, producing LEFT-sided pain.
        * RIGHT VPL LESIONS AND RIGHT PCA-TERRITORY STROKE: the right
          VPL is supplied by the right posterior cerebral artery
          territory; right PCA infarcts can involve the VPL and produce
          the contralateral hemianesthesia, often with other
          PCA-territory deficits (hemianopia from right LGN, motor
          deficits from right VL/cerebral peduncle).
        * VPL-SPECIFIC SYNDROMES are rare in isolation (the VPL is
          rarely affected alone); the clinical picture is usually part
          of a broader right thalamic or right PCA syndrome. The
          right VPL's clinical anchor is the contralateral (LEFT) body
          hemianesthesia, plus thalamic pain syndrome as the second
          anchor.

Hormonal Modulation:
    Same as the left VPL: minimal; cholinergic and monoaminergic arousal
    modulation of the right VPL's sensory relay gain; right S1
    corticothalamic feedback to the right VPL. Not a principal target of
    the 12 endocrine axes.

Memory Interfaces:
    Same as the left VPL: reads short_term (somatosensory buffer).
    Writes nothing directly (sensory relay, not memory structure). Thin
    interface; do not pad.

Model Integration (Gemma-4-E2B):
    No right VPL fragment. The VPL is a first-order somatosensory relay;
    the model prompt does not need a VPL block because the somatosensory
    signals it relays are already represented in the upstream (right
    body periphery) and downstream (right S1 body map) fragments. Same
    deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Body somatosensory pathway (the anchor):
    - ← spinal cord + brainstem (right medial lemniscus; fine touch,
      vibration, proprioception; right dorsal column pathway).
    - ← spinal cord + brainstem (right spinothalamic tract; pain,
      temperature, crude touch; right anterolateral pathway).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 body map; the VPL's
      principal cortical output; the right postcentral gyrus body
      representation).
    - ← telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 → right VPL;
      corticothalamic feedback; right-side).

    Cross-group traps (documented as distinctions, not signaling):
    - right VPL vs. right VPM (somatotopic split; different body maps).
    - right VPL/VPM vs. right LP (first-order vs. higher-order).
    - right VPL/VPM vs. right Pf (sensory-discriminative vs.
      affective-motivational for pain).

    - ↔ ../../../../../../left/ventral_nuclear_group/ventral_posterior_
      nucleus/ventral_posterior_lateral_nucleus/ (hemisphere
      counterpart; no functional asymmetry assumed; but see the
      CONTRALATERAL clinical facts — right and left VPL lesions produce
      opposite-side hemianesthesia; right VPL lesion → LEFT body
      hemianesthesia; left VPL lesion → RIGHT body hemianesthesia).

Notes:
    - Delta file of ../../../../../../left/ventral_nuclear_group/
      ventral_posterior_nucleus/ventral_posterior_lateral_nucleus/
      (to be drafted next; the source of truth). Not a full leaf. Do
      not duplicate.
    - THIS RIGHT VPL DELTA IS DRAFTED BEFORE ITS LEFT PARENT, following
      the pattern of the right VL delta and the right VP sub-container
      delta. Once the left VPL leaf is drafted, the pair is closed.
    - THE RIGHT VPL IS A CHILD OF THE RIGHT VP SUB-CONTAINER, not a
      sibling of it. This is the only genuine hierarchical sub-container
      pattern in the thalamus; the right VPL and right VPM are both
      children of right/ventral_nuclear_group/ventral_posterior_
      nucleus/.
    - THE VPL vs. VPM (somatotopic split) and VPL's TWO DRIVERS traps
      are reproduced in abbreviated form; the full text will be in the
      left VPL leaf (to be drafted).
    - THE VPL/VPM vs. LP and VPL/VPM vs. Pf cross-group traps are
      reproduced in abbreviated form; the canonical right-side
      first-order declaration is in the right VP sub-container (already
      drafted); this VPL delta enforces it at the leaf level.
    - THE CONTRALATERAL CLINICAL FACTS apply on the right with the
      correct direction: right VPL lesion → LEFT body hemianesthesia;
      right VPL lesion → LEFT-sided thalamic pain syndrome. The right
      and left VPL leaves document the opposite directions explicitly;
      do not flatten.
    - THALAMIC PAIN SYNDROME (Dejerine-Roussy) is the VPL's second
      clinical anchor (after the hemianesthesia); it applies on the
      right identically, producing LEFT-sided chronic pain after a
      right thalamic stroke. Document it; do not omit.
    - NO FRAGMENT: same as the whole thalamus. The right VPL is a
      relay, not a state-emitter.
    - The right VPL is NOT the right VPM (face + taste), NOT the right
      LP (higher-order parietal association), NOT the right Pf
      (nociceptive-affective). The traps make these distinctions
      explicit on the right.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right medial lemniscus, right spinothalamic, right S1, right
      VPM, right LP, right Pf, right VP sub-container). Stage 4 should
      not confuse right-side edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see the left
      VPL leaf (to be drafted) § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/ventral_nuclear_
      group/ventral_posterior_nucleus/.
"""