"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.ventral_nuclear_group.ventral_posterior_nucleus
Anatomical Role:
    The right ventral posterior nucleus (VP). A SUB-CONTAINER that
    groups the two right somatosensory relay nuclei of the right ventral
    nuclear group:
        - ventral_posterior_lateral_nucleus/ (VPL): BODY somatosensory
          relay (right medial lemniscus + right spinothalamic → right
          S1 body map).
        - ventral_posterior_medial_nucleus/ (VPM): FACE somatosensory
          relay (right trigeminothalamic → right S1 face map) and
          TASTE relay (right parabrachial → VPMpc → right gustatory
          cortex).

    STRUCTURAL NOTE (reproduced from the left VP sub-container; the
    only genuine hierarchical sub-container in the thalamus):
    The right VP is a STANDARD CONTAINER: its members (VPL, VPM) are its
    CHILDREN, not its siblings. This is STRUCTURALLY DIFFERENT from the
    medial group's intralaminar/midline sub-containers (which are
    integration layers whose members are also their siblings). The
    right VP sub-container is a genuine hierarchical grouping of the
    two somatosensory relays; its VPL and VPM children are the leaves.
    Stage 4 should treat the right VP as the parent of its two right
    children.

    See ../../../../left/ventral_nuclear_group/ventral_posterior_
    nucleus/__init__.py (to be drafted next) for the full anatomical
    description, the somatotopic-split framing, the VPL's two-driver
    framing (medial lemniscus + spinothalamic), the VPMpc taste
    sub-nucleus framing, and the full trap list. This right delta does
    not duplicate that content; it reproduces the traps in abbreviated
    form and points to the left sub-container for the full content.

    Reproduced TWO TRAPS (apply equally on the right):

    - VPL vs. VPM (group signature; SOMATOTOPIC SPLIT, not functional
      split): the right VPL is the BODY somatosensory relay (right
      medial lemniscus + right spinothalamic); the right VPM is the
      FACE somatosensory relay (right trigeminothalamic) plus the
      TASTE relay (right parabrachial → right VPMpc). Both are
      first-order somatosensory relays; the VPL/VPM split is a
      SOMATOTOPIC split of one functional system, not a functional
      split between two independent systems. Do not merge.

    - VPL vs. spinothalamic vs. medial lemniscus (the two-driver trap):
      the right VPL receives BOTH the right medial lemniscus (fine
      touch, vibration, proprioception) AND the right spinothalamic
      tract (pain, temperature, crude touch). Two separate drivers
      converging on the right VPL; do not treat it as a single
      undifferentiated somatosensory relay.

    Cross-group traps (reproduced in abbreviated form; declared from
    the other side; this sub-container is the canonical right-side
    first-order declaration):

    - VPL/VPM vs. LP (first-order vs. higher-order): the right VPL/VPM
      are FIRST-ORDER somatosensory relays (peripheral driver → right
      S1, areas 3/1/2); the right LP
      (right/lateral_nuclear_group/lateral_posterior_nucleus/) is a
      HIGHER-ORDER parietal association relay (cortical layer 5 driver
      → right posterior parietal cortex, areas 5/7). Different relay
      types; different cortical targets; do not merge.

    - VPL/VPM vs. Pf (sensory-discriminative vs. affective for pain):
      the right VPL/VPM carry the SENSORY-DISCRIMINATIVE dimension of
      pain (location, intensity, quality); the right Pf
      (right/medial_nuclear_group/parafascicular_nucleus/) carries the
      AFFECTIVE-MOTIVATIONAL dimension (arousal, attention, emotional
      response). Do not merge.

Functional Mode:
    Same as the left VP sub-container (to be drafted): first-order
    somatosensory relay — body (right VPL); first-order somatosensory
    relay — face + taste (right VPM with VPMpc). The right VP is the
    thalamic relay of the right body and face somatosensory pathways,
    plus the right taste pathway (via right VPMpc). No documented
    functional asymmetry between left and right VP sub-containers.

    CLINICAL FACTS (apply on the right identically, with
    CONTRALATERAL specification):
        * RIGHT VPL LESIONS: produce CONTRALATERAL (LEFT) BODY
          SOMATOSENSORY DEFICITS — LEFT body hemianesthesia (loss of
          touch, vibration, proprioception, pain, temperature on the
          LEFT side of the body). Right VPL lesions can also produce
          THALAMIC PAIN SYNDROME (Dejerine-Roussy; chronic LEFT-sided
          pain after a right thalamic stroke).
        * RIGHT VPM LESIONS: produce CONTRALATERAL (LEFT) FACE
          SOMATOSENSORY DEFICITS — LEFT facial hemianesthesia; right
          VPMpc lesions can produce taste deficits (LEFT-side taste
          recognition, with right anterior insula involvement).
        * The right and left VPL/VPM leaves document the opposite
          directions explicitly; do not flatten.

Hormonal Modulation:
    Same as the left VP sub-container (to be drafted). Minimal;
    cholinergic and monoaminergic arousal modulation of the right VPL/
    VPM sensory relay gain; right S1 corticothalamic feedback to right
    VPL/VPM. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as the left VP sub-container (to be drafted). Right VPL/VPM
    read short_term (somatosensory buffer). Writes nothing directly
    (sensory relays, not memory structures). Thin interface; do not
    pad.

Model Integration (Gemma-4-E2B):
    No right VP fragment. The VP is a first-order somatosensory relay
    group; the model prompt does not need a VP block because the
    somatosensory signals it relays are already represented in the
    upstream (right body/face periphery) and downstream (right S1)
    fragments. Same deliberate absence as on the left.

Children (two children — both right-side deltas of their left
counterparts; drafted later):
    - ventral_posterior_lateral_nucleus/   Delta of the left VPL. Right
                                             VPL; body somatosensory
                                             relay.
    - ventral_posterior_medial_nucleus/    Delta of the left VPM. Right
                                             VPM; face somatosensory +
                                             taste relay.

    Each of these two right children is a DELTA of its left
    counterpart. The left side carries the substantive content; the
    right side records only right-side reciprocal edges and reproduces
    the traps.

Right-specific reciprocal connections to enforce in Stage 4:

    Body somatosensory (right VPL):
    - ← spinal cord + brainstem (right medial lemniscus; fine touch,
      vibration, proprioception; right spinothalamic; pain,
      temperature, crude touch).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 body map).

    Face somatosensory + taste (right VPM):
    - ← brainstem trigeminal (right trigeminothalamic; right face
      somatosensory input).
    - → telencephalon/cerebral_hemispheres/right/cortex/parietal/
      primary_somatosensory_cortex (right S1 face map).
    - ← brainstem/.../parabrachial_nucleus (right taste input to right
      VPMpc).
    - → telencephalon/cerebral_hemispheres/right/cortex/insular/
      primary_gustatory_cortex (right gustatory output from right
      VPMpc).

    Cross-group traps (documented as distinctions, not signaling):
    - right VPL/VPM vs. right LP (first-order vs. higher-order).
    - right VPL/VPM vs. right Pf (sensory-discriminative vs.
      affective-motivational for pain).

    - ↔ ../../../../left/ventral_nuclear_group/ventral_posterior_
      nucleus/ (hemisphere counterpart; the left sub-container is the
      source of truth for the full content; but see the CONTRALATERAL
      clinical facts — right and left VPL/VPM lesions produce
      opposite-side hemianesthesia).

Notes:
    - Sub-container delta of ../../../../left/ventral_nuclear_group/
      ventral_posterior_nucleus/ (to be drafted next). Not a full
      sub-container. Do not duplicate the left VP's content.
    - THIS RIGHT VP SUB-CONTAINER DELTA IS DRAFTED BEFORE ITS LEFT
      PARENT, following the same pattern as the right VL delta
      (drafted before the left VL leaf). Once the left VP sub-container
      is drafted, the pair is closed. The pointer to the left VP
      sub-container in this file resolves when the left parent is
      drafted.
    - THE RIGHT VP IS THE PARENT OF ITS TWO RIGHT CHILDREN (VPL, VPM):
      this is a STANDARD CONTAINER pattern (VPL/VPM are children, not
      siblings), DIFFERENT from the medial group's intralaminar/midline
      sub-containers (which are siblings of their members). Stage 4
      should treat the right VP as the parent of its two right
      children; the right VPL and VPM deltas will be drafted later and
      will point to this sub-container as their parent.
    - THE VPL vs. VPM (somatotopic split) and VPL vs. spinothalamic
      vs. medial lemniscus (two drivers) traps are reproduced in
      abbreviated form; the full text will be in the left VP
      sub-container (to be drafted).
    - THE VPL/VPM vs. LP and VPL/VPM vs. Pf cross-group traps are
      reproduced in abbreviated form; this sub-container is the
      canonical right-side first-order declaration, matching the
      left-side declaration that the left VP sub-container will make.
    - THE CONTRALATERAL CLINICAL FACTS apply on the right with the
      correct direction: right VPL lesion → LEFT body hemianesthesia;
      right VPM lesion → LEFT facial hemianesthesia. The right and
      left VPL/VPM leaves document the opposite directions explicitly.
    - NO FRAGMENT: same as the whole thalamus. The right VP is a
      first-order somatosensory relay group, not a state-emitter.
    - The right VP is NOT a higher-order association group (the VPL/
      VPM are first-order relays); NOT the LP (which is higher-order);
      NOT the Pf (which is nociceptive-affective). The traps make
      these distinctions explicit.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right medial lemniscus, right spinothalamic, right
      trigeminothalamic, right parabrachial, right S1, right
      gustatory cortex, right LP, right Pf). Stage 4 should not
      confuse right-side edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see the left
      VP sub-container (to be drafted) § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/ventral_nuclear_
      group/.
"""