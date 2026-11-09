"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.ventral_nuclear_group.ventral_posterior_nucleus.ventral_posterior_medial_nucleus
Anatomical Role:
    The right ventral posterior medial nucleus (VPM). A first-order
    somatosensory AND taste relay in the right ventral nuclear group's
    ventral posterior sub-container. Same FACE + TASTE role as the left
    VPM: the thalamic relay of the right FACE's ascending somatosensory
    pathway (right trigeminothalamic tract) and of the right TASTE
    pathway (right parabrachial nucleus → right VPMpc → right gustatory
    cortex).

    The VPM's TWO MODALITIES (documented WITHIN this leaf, not as child
    nodes):
        - FACE somatosensory (principal VPM): right trigeminothalamic
          → right S1 face map.
        - TASTE (VPMpc; parvicellular subdivision): right parabrachial
          → right VPMpc → right gustatory cortex (anterior insula).
    Do not create vpm_face/, vpm_taste/, or vpm_pc/ as child nodes.

    See ../../../../../../left/ventral_nuclear_group/ventral_posterior_
    nucleus/ventral_posterior_medial_nucleus/__init__.py (now drafted —
    the source of truth for this delta) for the full anatomical
    description, the two-modality framing, the VPMpc framing, the
    somatotopic and taste-topographic organization, and the full
    clinical fact list.

    Reproduced distinctions (apply equally on the right):

    - VPL vs. VPM (SOMATOTOPIC-SPLIT trap; group signature): the right
      VPL (../ventral_posterior_lateral_nucleus/) is BODY somatosensory
      (right medial lemniscus + right spinothalamic); the right VPM is
      FACE somatosensory (right trigeminothalamic) + TASTE (right
      parabrachial → right VPMpc). Do not merge; SOMATOTOPIC split,
      not functional split; the VPM adds taste as a second modality.

    - VPM vs. VPMpc (somatosensory-vs-taste sub-trap): right VPM
      principal = FACE somatosensory; right VPMpc = TASTE. Two distinct
      modalities; VPMpc is a subregion, not a separate nucleus. Do not
      flatten the VPM as "purely face somatosensory."

    - VPL/VPM vs. LP (cross-group first-order vs. higher-order;
      canonical right-side first-order declaration is in the right VP
      sub-container): right VPL/VPM are FIRST-ORDER somatosensory
      relays (→ right S1); the right LP is a HIGHER-ORDER parietal
      association relay (→ right posterior parietal cortex). Do not
      merge.

    - VPL/VPM vs. Pf (cross-group first-order vs. nociceptive-
      affective; canonical right-side first-order declaration is in the
      right VP sub-container): right VPL/VPM carry the
      SENSORY-DISCRIMINATIVE dimension of pain; the right Pf carries
      the AFFECTIVE-MOTIVATIONAL dimension. Do not merge.

    - VPM vs. gustatory cortex: VPMpc is the THALAMIC taste relay; the
      gustatory cortex (right anterior insula) is the CORTICAL taste
      target. The VPMpc is the thalamic node, not the whole taste
      system.

Functional Mode:
    Same as the left VPM: first-order somatosensory relay for the FACE
    (right trigeminothalamic → right S1 face map); first-order taste
    relay for the mouth (right parabrachial → right VPMpc → right
    gustatory cortex). No documented functional asymmetry between left
    and right VPM. Do not fabricate one.

    CLINICAL FACTS (apply on the right identically, with CONTRALATERAL
    specification):
        * RIGHT VPM LESIONS → CONTRALATERAL (LEFT) FACE
          SOMATOSENSORY DEFICITS — LEFT facial hemianesthesia (loss of
          touch, pain, temperature on the LEFT side of the face). The
          LEFT VPM leaf documents the reverse: LEFT VPM lesion →
          RIGHT facial hemianesthesia. Together they are the SIXTH
          contralateral-clinical pair in the tree.
        * RIGHT VPMpc LESIONS → CONTRALATERAL (LEFT) TASTE DEFICITS —
          impaired recognition of tastes on the LEFT side of the
          tongue. Subtle, predominantly contralateral (the taste
          pathway is bilaterally represented); not overclaimed as
          complete unilateral ageusia.
        * RIGHT VPM LESIONS AND RIGHT PCA-TERRITORY STROKE: right
          thalamogeniculate branches of the right PCA supply the right
          VPM; right PCA infarcts can produce LEFT facial
          hemianesthesia with other right PCA-territory deficits.
        * VPM-SPECIFIC SYNDROMES are rare in isolation; the VPM's
          anchors are the CONTRALATERAL FACIAL HEMIANESTHESIA
          (established; primary) and the CONTRALATERAL TASTE DEFICITS
          (established; secondary; subtle).

Hormonal Modulation:
    Same as the left VPM: minimal; cholinergic and monoaminergic arousal
    modulation of the right VPM's and right VPMpc's sensory relay gain;
    right S1 and right gustatory corticothalamic feedback to right
    VPM/VPMpc. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as the left VPM: reads short_term (face somatosensory and
    taste buffer). Writes nothing directly (sensory relay, not memory
    structure). Thin interface; do not pad.

Model Integration (Gemma-4-E2B):
    No right VPM fragment. The VPM is a first-order somatosensory and
    taste relay; the model prompt does not need a VPM block. The
    somatosensory and gustatory cortical states are carried by right S1
    and the right gustatory cortex. Same deliberate absence as on the
    left.

Right-specific reciprocal connections to enforce in Stage 4:

    Face somatosensory pathway (the principal role):
    - ← brainstem/.../trigeminal_nuclei (right principal sensory and
      right spinal trigeminal nuclei → right VPM; the trigeminal nuclei
      are midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 face map; area 3b for face
      touch, area 1 for face pain/temperature).
    - ← telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 → right VPM;
      corticothalamic feedback).

    Taste pathway (VPMpc; the secondary role):
    - ← brainstem/.../parabrachial_nucleus (right parabrachial → right
      VPMpc; the parabrachial nucleus is midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/insular/
      primary_gustatory_cortex (right gustatory cortex; right anterior
      insula).
    - ← telencephalon/cerebral_hemispheres/right/cortex/insular/*
      (right gustatory and insular cortex → right VPMpc;
      corticothalamic feedback).

    Cross-group traps (documented as distinctions, not signaling):
    - right VPM vs. right VPL (somatotopic split; VPM also carries
      taste, VPL does not).
    - right VPM/VPL vs. right LP (first-order vs. higher-order).
    - right VPM/VPL vs. right Pf (sensory-discriminative vs.
      affective-motivational for pain).

    - ↔ ../../../../../../left/ventral_nuclear_group/ventral_posterior_
      nucleus/ventral_posterior_medial_nucleus/ (hemisphere counterpart;
      no functional asymmetry assumed; but see the CONTRALATERAL
      clinical facts — right and left VPM lesions produce opposite-side
      facial hemianesthesia and opposite-side taste deficits).

Notes:
    - Delta file of ../../../../../../left/ventral_nuclear_group/
      ventral_posterior_nucleus/ventral_posterior_medial_nucleus/ (now
      drafted — the source of truth). Not a full leaf. Do not
      duplicate.
    - THE VPM PAIR IS NOW COMPLETE: with the left VPM leaf drafted
      (prior turn), this delta's cross-references resolve and the pair
      is closed. The thalamus is fully documented on both hemispheres.
    - THE THALAMUS SUBTREE IS COMPLETE: ~54 files (anterior group 8,
      lateral group 8, medial group 20, metathalamus 6, reticular
      nucleus 2, ventral group 10), all documented on both hemispheres.
    - THE VPM IS A CHILD OF THE RIGHT VP SUB-CONTAINER (not a sibling
      of it). Same hierarchical parent pattern as the right VPL.
    - THE VPM's TWO MODALITIES (face somatosensory + taste) are
      documented WITHIN the left VPM leaf; this delta references them
      and reproduces the distinctions. Do not create vpm_face/,
      vpm_taste/, or vpm_pc/ as child nodes on the right either.
    - THE VPL vs. VPM (somatotopic split) and VPM vs. VPMpc
      (somatosensory vs. taste) traps are reproduced in abbreviated
      form; the full text is in the left VPM leaf.
    - THE VPL/VPM vs. LP and VPL/VPM vs. Pf cross-group traps are
      reproduced; the canonical right-side first-order declaration is in
      the right VP sub-container (drafted); this VPM delta enforces it
      at the leaf level.
    - THE CONTRALATERAL CLINICAL FACTS apply on the right with the
      correct direction: right VPM lesion → LEFT facial hemianesthesia;
      right VPMpc lesion → LEFT taste deficit (subtle, predominantly
      contralateral). The left and right VPM leaves document the
      opposite directions explicitly.
    - THE TASTE DEFICIT IS SUBTLE (predominantly contralateral; not
      complete unilateral ageusia). Documented honestly.
    - NO FRAGMENT: same as the whole thalamus. The right VPM is a
      relay, not a state-emitter.
    - The right VPM is NOT the right VPL, NOT the right LP, NOT the
      right Pf, NOT the gustatory cortex. The traps make these
      distinctions explicit on the right.
    - Midline targets (trigeminal nuclei, parabrachial nucleus) are
      flagged with "verify" so Stage 4 does not force a hemisphere
      split on structures that are not hemisphere-split in the tree.
      Right trigeminothalamic, right parabrachial, right S1, right
      gustatory cortex, right VPL, right LP, right Pf, and right VP
      sub-container are hemisphere-split and require right-side targets
      explicitly.
    - Vocabulary used above is defined in Stage 0 files; see the left
      VPM leaf § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/ventral_nuclear_
      group/ventral_posterior_nucleus/.
"""