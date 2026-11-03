"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.ventral_nuclear_group.ventral_posterior_nucleus.ventral_posterior_medial_nucleus
Anatomical Role:
    The right ventral posterior medial nucleus (VPM). A first-order
    somatosensory AND taste relay in the right ventral nuclear group's
    ventral posterior sub-container, situated medial to the right VPL
    and posterior to the right VL. Same FACE + TASTE role as the left
    VPM: the thalamic relay of the right FACE's ascending somatosensory
    pathway (right trigeminothalamic tract) and of the right TASTE
    pathway (right parabrachial nucleus → right VPMpc → right gustatory
    cortex).

    The VPM's TWO MODALITIES (documented WITHIN this leaf, not as child
    nodes):
        - FACE somatosensory (principal VPM, especially the
          parvocellular-adjacent but non-VPMpc portions): receives the
          right trigeminothalamic tract (face and head somatosensation);
          projects to the right S1 face map (postcentral gyrus face
          area).
        - TASTE (VPMpc; the parvicellular subdivision): receives taste
          input from the right parabrachial nucleus; projects to the
          right gustatory cortex (anterior insula). The VPMpc carries
          the taste pathway.
    Same convention as the LGN's six layers, the MGN's three
    divisions, the pulvinar's three subregions, the MD's three
    subdivisions, the VA's subdivisions, the VL's VIM subnucleus, and
    the VPL's shell/core distinction: the VPM's two modalities and its
    VPMpc subdivision are documented within this leaf, not as tree
    children. Do not create vpm_face/, vpm_taste/, or vpm_pc/ as child
    nodes.

    See ../../../../../../left/ventral_nuclear_group/ventral_posterior_
    nucleus/ventral_posterior_medial_nucleus/__init__.py (to be drafted
    next; the source of truth for this delta) for the full anatomical
    description, the two-modality framing, the VPMpc taste sub-nucleus
    framing, and the full clinical fact list.

    Reproduced distinctions (apply equally on the right):

    - VPL vs. VPM (SOMATOTOPIC-SPLIT trap; group signature): the right
      VPL (../ventral_posterior_lateral_nucleus/) is the BODY
      somatosensory relay (right medial lemniscus + right
      spinothalamic → right S1 body map); the right VPM is the FACE
      somatosensory relay (right trigeminothalamic) plus the TASTE
      relay (right parabrachial → right VPMpc → right gustatory
      cortex). Both are first-order somatosensory relays (at least for
      their somatosensory components); the VPL/VPM split is a
      SOMATOTOPIC SPLIT (body vs. face), not a functional split. Do
      not merge.

    - VPM vs. VPMpc (the somatosensory-vs-taste sub-trap; the VPM's
      distinctive intra-nucleus split): the VPM's principal
      (somatosensory) portion carries FACE somatosensation; the VPM's
      parvicellular subdivision (VPMpc) carries TASTE. The two
      modalities are distinct; the VPMpc is a subregion of the VPM,
      not a separate nucleus; the taste pathway is distinct from the
      face somatosensory pathway. Do not flatten the VPM as "purely
      face somatosensory."

    - VPL/VPM vs. LP (cross-group first-order vs. higher-order;
      declared from the LP side; canonical first-order side declared
      in the right VP sub-container): the right VPL/VPM are FIRST-ORDER
      somatosensory relays (peripheral driver → right S1); the right LP
      (right/lateral_nuclear_group/lateral_posterior_nucleus/) is a
      HIGHER-ORDER parietal association relay. Different relay types;
      do not merge.

    - VPL/VPM vs. Pf (cross-group first-order vs. nociceptive-affective;
      declared from the Pf side; canonical first-order side declared
      in the right VP sub-container): the right VPL/VPM carry the
      SENSORY-DISCRIMINATIVE dimension of pain; the right Pf carries
      the AFFECTIVE-MOTIVATIONAL dimension. Do not merge.

    - VPM vs. VPL's TWO DRIVERS (subtle): the right VPL receives TWO
      drivers (medial lemniscus + spinothalamic) for the body; the
      right VPM receives TWO modalities (face somatosensory + taste)
      for the face and mouth. The VPL's two drivers are two
      somatosensory submodalities; the VPM's two modalities are
      different modalities. Do not conflate the "two drivers" (VPL)
      with the "two modalities" (VPM).

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
          LEFT VPM leaf documents the reverse: a LEFT VPM lesion
          produces RIGHT facial hemianesthesia. The two leaves
          together document the full contralateral pattern; this is
          the SIXTH contralateral-clinical pair in the tree.
        * RIGHT VPMpc LESIONS → CONTRALATERAL (LEFT) TASTE DEFICITS —
          impaired recognition of tastes on the LEFT side of the
          tongue (the anterior two-thirds of the tongue, which is
          innervated by the chorda tympani / facial nerve and
          bilaterally represented; unilateral VPMpc lesions typically
          produce SUBTLE taste deficits, and the deficit is
          predominantly contralateral). Documented honestly; not
          overclaimed as complete unilateral ageusia.
        * RIGHT VPM LESIONS AND RIGHT PCA-TERRITORY STROKE: the right
          VPM is supplied by the right thalamogeniculate branches of
          the right posterior cerebral artery; right PCA infarcts can
          involve the VPM and produce the contralateral facial
          hemianesthesia, often with other right PCA-territory
          deficits.
        * VPM-SPECIFIC SYNDROMES are rare in isolation; the VPM's
          clinical anchors are the CONTRALATERAL FACIAL HEMIANESTHESIA
          (established; the primary anchor) and the CONTRALATERAL
          TASTE DEFICITS (established, though typically subtle). The
          VPM's clinical anchors are STRONGER than the VA's
          (investigational) but SUBTLER than the VPL's (which has the
          additional thalamic pain syndrome).

Hormonal Modulation:
    Same as the left VPM: minimal; cholinergic and monoaminergic arousal
    modulation of the right VPM's sensory relay gain; right S1
    corticothalamic feedback to the right VPM. Not a principal target of
    the 12 endocrine axes.

Memory Interfaces:
    Same as the left VPM: reads short_term (face somatosensory and
    taste buffer). Writes nothing directly (sensory relay, not memory
    structure). Thin interface; do not pad.

Model Integration (Gemma-4-E2B):
    No right VPM fragment. The VPM is a first-order somatosensory and
    taste relay; the model prompt does not need a VPM block because the
    face somatosensory and taste signals it relays are already
    represented in the upstream (right face periphery, right taste
    receptors) and downstream (right S1 face map, right gustatory
    cortex) fragments. Same deliberate absence as on the left.

Right-specific reciprocal connections to enforce in Stage 4:

    Face somatosensory pathway (the principal role):
    - ← brainstem (right trigeminothalamic tract; from the right
      principal sensory and spinal trigeminal nuclei; face and head
      somatosensation; the trigeminal nuclei are midline-adjacent but
      the right trigeminothalamic projection is to the right VPM —
      verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 face map; the right VPM's
      principal cortical output; the right postcentral gyrus face
      representation; area 3b for face touch, area 1 for face pain).
    - ← telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 → right VPM;
      corticothalamic feedback; right-side).

    Taste pathway (VPMpc; the secondary role):
    - ← brainstem/.../parabrachial_nucleus (right parabrachial nucleus
      → right VPMpc; taste input; the parabrachial nucleus is
      midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/insular/
      primary_gustatory_cortex (right gustatory cortex in the right
      anterior insula; the right VPMpc's principal cortical output;
      the taste pathway's cortical target).
    - ← telencephalon/cerebral_hemispheres/right/cortex/insular/*
      (right gustatory and insular cortex → right VPMpc;
      corticothalamic feedback; right-side).

    Cross-group traps (documented as distinctions, not signaling):
    - right VPM vs. right VPL (somatotopic split; different body maps;
      the VPM also carries taste, the VPL does not).
    - right VPM/VPL vs. right LP (first-order vs. higher-order).
    - right VPM/VPL vs. right Pf (sensory-discriminative vs.
      affective-motivational for pain).

    - ↔ ../../../../../../left/ventral_nuclear_group/ventral_posterior_
      nucleus/ventral_posterior_medial_nucleus/ (hemisphere
      counterpart; no functional asymmetry assumed; but see the
      CONTRALATERAL clinical facts — right and left VPM lesions produce
      opposite-side facial hemianesthesia and opposite-side taste
      deficits).

Notes:
    - Delta file of ../../../../../../left/ventral_nuclear_group/
      ventral_posterior_nucleus/ventral_posterior_medial_nucleus/
      (to be drafted next; the source of truth). Not a full leaf. Do
      not duplicate.
    - THIS RIGHT VPM DELTA IS DRAFTED BEFORE ITS LEFT PARENT, following
      the same pattern as the right VL delta, the right VP sub-container
      delta, and the right VPL delta.
    - THE THALAMUS IS NOW COMPLETE — BOTH HEMISPHERES (with this file
      and the remaining left VPM leaf): the entire thalamus subtree is
      fully documented once the left VPM leaf is drafted. Currently
      drafted: anterior group (8 files), lateral group (8 files),
      medial group (20 files), metathalamus (6 files), reticular
      nucleus (2 files), ventral nuclear group (this file closes the
      right side; the left VPM leaf is the only remaining substantive
      file).
    - THE VPM IS A CHILD OF THE RIGHT VP SUB-CONTAINER (not a sibling
      of it). Same hierarchical parent pattern as the right VPL. The
      right VPM and right VPL are both children of
      right/ventral_nuclear_group/ventral_posterior_nucleus/.
    - THE VPM's TWO MODALITIES (face somatosensory + taste) are
      documented WITHIN this leaf, not as child nodes. The VPMpc
      taste sub-nucleus is a subregion, not a separate nucleus. Do not
      create vpm_face/, vpm_taste/, or vpm_pc/ as child nodes.
    - THE VPL vs. VPM (somatotopic split) and VPM vs. VPMpc
      (somatosensory vs. taste within the VPM) traps are reproduced
      in abbreviated form; the full text will be in the left VPM
      leaf.
    - THE VPL/VPM vs. LP and VPL/VPM vs. Pf cross-group traps are
      reproduced in abbreviated form; the canonical right-side
      first-order declaration is in the right VP sub-container
      (already drafted); this VPM delta enforces it at the leaf
      level.
    - THE CONTRALATERAL CLINICAL FACTS apply on the right with the
      correct direction: right VPM lesion → LEFT facial hemianesthesia;
      right VPMpc lesion → LEFT taste deficit (subtle, predominantly
      contralateral). The right and left VPM leaves document the
      opposite directions explicitly.
    - THE TASTE DEFICIT IS SUBTLE (predominantly contralateral; not
      complete unilateral ageusia). Documented honestly; not
      overclaimed. The taste pathway is bilaterally represented at
      multiple levels, so unilateral VPMpc lesions produce incomplete
      deficits.
    - NO FRAGMENT: same as the whole thalamus. The right VPM is a
      relay, not a state-emitter.
    - The right VPM is NOT the right VPL (body somatosensory), NOT the
      right LP (higher-order parietal association), NOT the right Pf
      (nociceptive-affective). The traps make these distinctions
      explicit on the right.
    - Midline targets (trigeminal nuclei, parabrachial nucleus) are
      flagged with "verify" so Stage 4 does not force a hemisphere
      split on structures that are not hemisphere-split in the tree.
      Right trigeminothalamic, right parabrachial, right S1, right
      gustatory cortex, right VPL, right LP, right Pf, and right VP
      sub-container are hemisphere-split and require right-side
      targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see the left
      VPM leaf (to be drafted) § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/ventral_nuclear_
      group/ventral_posterior_nucleus/.
"""