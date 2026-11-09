"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.ventral_nuclear_group
Anatomical Role:
    The right ventral nuclear group of the thalamus. Same FOUR nuclei
    organized into TWO RELAY FAMILIES as the left ventral group, mirrored
    to the right hemisphere:

        - MOTOR RELAYS (two nuclei):
            * ventral_anterior_nucleus/ (VA): the BASAL GANGLIA MOTOR
              RELAY. Receives input from the right GPi and right SNr;
              projects to the right premotor cortex, SMA, and M1.
            * ventral_lateral_nucleus/ (VL): the CEREBELLAR MOTOR
              RELAY. Receives input from the right cerebellar dentate
              nucleus; projects to the right M1. Contains the VIM
              (ventral-intermediate) subnucleus, the principal DBS
              target for essential tremor and Parkinsonian tremor.

        - SOMATOSENSORY RELAYS (two nuclei, under a SUB-CONTAINER):
            * ventral_posterior_nucleus/ (VP; SUB-CONTAINER):
                - ventral_posterior_lateral_nucleus/ (VPL): BODY
                  somatosensory relay (right medial lemniscus and
                  right spinothalamic → right S1 body map).
                - ventral_posterior_medial_nucleus/ (VPM): FACE
                  somatosensory relay (right trigeminothalamic → right
                  S1 face map) and TASTE relay (right parabrachial →
                  VPMpc → right gustatory cortex).

    See ../../left/ventral_nuclear_group/__init__.py for the full
    anatomical description, the two-groups-in-one framing, the
    sub-container pattern (children, not siblings), the VIM subnucleus
    framing, the VPMpc taste sub-nucleus framing, and the full clinical
    fact list.

    Reproduced SIX TRAPS (apply equally on the right):

    - TRAP 1: VPL vs. VPM (group signature; somatotopic split): the
      right VPL is BODY (right medial lemniscus + right spinothalamic);
      the right VPM is FACE (right trigeminothalamic) + TASTE (right
      parabrachial → VPMpc). Different maps; do not merge. The split
      is SOMATOTOPIC, not functional.

    - TRAP 2: VA vs. VL (motor driver split): the right VA is the BASAL
      GANGLIA driver (right GPi/SNr → VA → right premotor/SMA/M1); the
      right VL is the CEREBELLAR driver (right dentate → VL → right
      M1, with the VIM tremor target). Different drivers; do not merge.

    - TRAP 3: VPL/VPM vs. LP (cross-group first-order vs.
      higher-order; declared from the LP side; this container is the
      CANONICAL RIGHT-SIDE FIRST-ORDER declaration): right VPL/VPM are
      FIRST-ORDER somatosensory relays (peripheral driver → right S1);
      the right LP (right/lateral_nuclear_group/lateral_posterior_
      nucleus/) is a HIGHER-ORDER parietal association relay (cortical
      layer 5 driver → right posterior parietal cortex, areas 5/7).
      Different relay types; different cortical targets; do not merge.

    - TRAP 4: VPL/VPM vs. Pf (cross-group first-order vs.
      nociceptive-affective; declared from the Pf side; this container
      is the CANONICAL RIGHT-SIDE FIRST-ORDER declaration): right
      VPL/VPM carry the SENSORY-DISCRIMINATIVE dimension of pain
      (location, intensity, quality); the right Pf
      (right/medial_nuclear_group/parafascicular_nucleus/) carries the
      AFFECTIVE-MOTIVATIONAL dimension (arousal, attention, emotional
      response). Do not merge.

    - TRAP 5: VA/VL vs. CM (motor-relay vs. intralaminar-motor;
      declared from the CM side; this container is the CANONICAL
      RIGHT-SIDE MOTOR-RELAY declaration): right VA/VL are FIRST-ORDER
      motor relays (basal ganglia or cerebellar driver → motor
      cortex); the right CM (right/medial_nuclear_group/
      centromedian_nucleus/) is an INTRALAMINAR motor/arousal relay
      (basal ganglia driver → striatum, not motor cortex; re-entrant
      loop). Different relay types; different output targets; do not
      merge.

    - TRAP 6: VPL vs. spinothalamic vs. medial lemniscus (the two
      drivers trap): the right VPL receives BOTH the right medial
      lemniscus (fine touch, vibration, proprioception) AND the right
      spinothalamic tract (pain, temperature, crude touch). Two
      separate drivers converging on the right VPL; do not treat it as
      a single undifferentiated somatosensory relay.

Functional Mode:
    Same as ../../left/ventral_nuclear_group/. Motor relay — basal
    ganglia (right VA); motor relay — cerebellar (right VL, with VIM);
    somatosensory relay — body (right VPL); somatosensory relay — face
    + taste (right VPM, with VPMpc). No documented functional asymmetry
    between left and right ventral nuclear groups. Do not fabricate
    one.

    CLINICAL FACTS (apply on the right identically, with
    CONTRALATERAL specification):
        * RIGHT VPL LESIONS: produce CONTRALATERAL (LEFT) BODY
          SOMATOSENSORY DEFICITS — a RIGHT VPL lesion produces LEFT
          body hemianesthesia (loss of touch, vibration,
          proprioception, pain, temperature on the LEFT side of the
          body). The LEFT VPL lesion produces RIGHT body hemianesthesia
          (documented in ../../left/ventral_nuclear_group/). Right VPL
          lesions can also produce THALAMIC PAIN SYNDROME (Dejerine-
          Roussy; chronic LEFT-sided pain after a right thalamic
          stroke).
        * RIGHT VPM LESIONS: produce CONTRALATERAL (LEFT) FACE
          SOMATOSENSORY DEFICITS — a RIGHT VPM lesion produces LEFT
          facial hemianesthesia; right VPMpc lesions can produce taste
          deficits (bitter/sweet recognition on the LEFT side of the
          tongue, with right anterior insula involvement).
        * RIGHT VA LESIONS: motor deficits (rare in isolation; right
          VA supplied by the right PCA territory).
        * RIGHT VL LESIONS: tremor, ataxia, motor coordination
          deficits. The RIGHT VIM subregion is the principal DBS target
          for essential tremor and Parkinsonian tremor; right VIM DBS
          suppresses LEFT-side tremor predominantly (contralateral
          effect), with bilateral tremor suppression when bilateral
          DBS is used.

Hormonal Modulation:
    Same as ../../left/ventral_nuclear_group/. Minimal;
    dopaminergic/cholinergic/monoaminergic modulation of the right
    VA/VL motor loops; cholinergic/monoaminergic arousal modulation of
    the right VPL/VPM sensory relays; right S1 corticothalamic feedback
    to VPL/VPM. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../left/ventral_nuclear_group/. Right VA/VL reads
    procedural and short_term (motor loops); right VPL/VPM reads
    short_term (somatosensory buffer). Writes nothing directly.

Model Integration (Gemma-4-E2B):
    No right ventral group fragment. Same as ../../left/ and the whole
    thalamus: the ventral group is a motor and somatosensory relay
    group, not a state-emitter. The motor and somatosensory cortical
    states are carried by right M1 and right S1.

Children (four nuclei + one sub-container; all right-side deltas of
their left counterparts):
    Motor family:
    - ventral_anterior_nucleus/   Delta of ../../left/ventral_nuclear_
                                    group/ventral_anterior_nucleus/.
                                    Right VA; basal ganglia motor
                                    relay.
    - ventral_lateral_nucleus/    Delta of ../../left/ventral_nuclear_
                                    group/ventral_lateral_nucleus/.
                                    Right VL; cerebellar motor relay;
                                    right VIM DBS target.

    Somatosensory family (sub-container):
    - ventral_posterior_nucleus/  Delta of ../../left/ventral_nuclear_
                                    group/ventral_posterior_nucleus/.
                                    Right sub-container.
        ├── ventral_posterior_lateral_nucleus/  Delta of the left VPL;
        │                                         right VPL; body
        │                                         somatosensory.
        └── ventral_posterior_medial_nucleus/   Delta of the left VPM;
                                                  right VPM; face +
                                                  taste.

    Each of these five right children (four nuclei + one sub-container)
    is a DELTA of its left counterpart; no full right-side leaves are
    needed. The left side carries the substantive content; the right
    side records only right-side reciprocal edges and reproduces the
    traps.

Right-specific reciprocal connections to enforce in Stage 4 (summary;
the full edge list is in the child leaves):

    Motor relays:
    - right ventral_anterior_nucleus ← telencephalon/.../subcortical/
      basal_ganglia/right (GPi/SNr → right VA) and → telencephalon/.../
      cortex/frontal/premotor_cortex, supplementary_motor_cortex,
      primary_motor_cortex (right VA → right premotor/SMA/M1).
    - right ventral_lateral_nucleus ← cerebellum/.../deep cerebellar
      nuclei (right dentate → right VL) and → telencephalon/.../
      cortex/frontal/primary_motor_cortex (right VL → right M1, with
      VIM as the DBS target subregion).

    Somatosensory relays:
    - right ventral_posterior_lateral_nucleus ← spinal cord + brainstem
      (right medial lemniscus + right spinothalamic; body somatosensory
      input) and → telencephalon/.../cortex/parietal/
      primary_somatosensory_cortex (right S1 body map).
    - right ventral_posterior_medial_nucleus ← brainstem trigeminal
      (right face somatosensory input) and → right S1 face map; and
      ← brainstem/.../parabrachial_nucleus (taste input to right
      VPMpc) and → right gustatory cortex (anterior insula).

    Cross-group traps (documented as distinctions, not signaling):
    - right VPL/VPM vs. right LP (first-order vs. higher-order).
    - right VPL/VPM vs. right Pf (sensory-discriminative vs.
      affective-motivational for pain).
    - right VA/VL vs. right CM (first-order motor relay vs.
      intralaminar motor/arousal relay).

    - ↔ ../../left/ventral_nuclear_group/ (hemisphere counterpart; no
      functional asymmetry assumed; but see the CONTRALATERAL clinical
      facts — right and left VPL/VPM lesions produce opposite-side
      hemianesthesia; right and left VIM DBS target opposite-side
      tremor predominantly, though bilateral DBS targets both sides).

Notes:
    - Group-container delta of ../../left/ventral_nuclear_group/. Not a
      full container. Do not duplicate the left group's content.
    - SIX TRAPS reproduced in abbreviated form; the full text is in
      ../../left/ventral_nuclear_group/ and ../../__init__.py. A
      contributor entering at the right ventral group must see them.
    - DELTA-OF-A-DELTA CHAIN EXTENDS TO THIS GROUP: the four right
      nuclei (VA, VL, VPL, VPM) + the right ventral_posterior_
      nucleus/ sub-container are each deltas of their left
      counterparts, same as every other thalamic right leaf.
    - THE CONTRALATERAL CLINICAL FACTS ARE REVERSED ON THE RIGHT: right
      VPL lesion → LEFT body hemianesthesia; right VPM lesion → LEFT
      facial hemianesthesia. These are the sixth and seventh
      contralateral-clinical pairs in the tree (after the STN, LP,
      pulvinar, LGN, and (pending) the VPL/VPM pairs themselves). The
      right and left leaves document the opposite directions
      explicitly; do not flatten.
    - THE VENTRAL POSTERIOR SUB-CONTAINER IS A STANDARD CONTAINER:
      VPL and VPM are its CHILDREN (not siblings). This is
      structurally DIFFERENT from the medial group's intralaminar/
      midline sub-containers (which are siblings of their members).
      The right ventral_posterior_nucleus/ is a delta of the left
      sub-container, and its right VPL and VPM are delta children.
    - THE VIM (VENTRAL-INTERMEDIATE) SUBNUCLEUS is documented WITHIN
      the left VL leaf, not as a child node. Same convention applies on
      the right: do not create right-vim/ as a separate tree node.
    - THE VPMpc (parvicellular VPM) carries taste on the right as on
      the left; do not draft the right VPM as purely "face
      somatosensory."
    - THE VENTRAL GROUP IS TWO GROUPS IN ONE: motor (VA/VL) and
      somatosensory (VPL/VPM). Do not flatten on the right either.
    - NO FRAGMENT: same as the whole thalamus. The right ventral group
      is a relay group, not a state-emitter.
    - Midline targets: none in this file's specific edges; all targets
      are hemisphere-split and require right-side targets explicitly
      (right GPi/SNr, right dentate, right medial lemniscus/right
      spinothalamic, right trigeminothalamic, right parabrachial,
      right M1, right premotor/SMA, right S1, right gustatory cortex,
      right LP, right Pf, right CM). Stage 4 should not confuse
      right-side edges with left-side edges.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/ventral_nuclear_group/ § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/.
"""