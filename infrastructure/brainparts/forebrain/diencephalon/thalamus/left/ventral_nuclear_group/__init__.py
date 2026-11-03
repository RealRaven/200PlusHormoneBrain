"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.ventral_nuclear_group
Anatomical Role:
    The left ventral nuclear group of the thalamus. A cluster of FOUR
    nuclei on the ventral-lateral aspect of the left thalamus,
    organized into TWO RELAY FAMILIES:

        - MOTOR RELAYS (two nuclei):
            * ventral_anterior_nucleus/ (VA): the BASAL GANGLIA MOTOR
              RELAY. Receives input from the basal ganglia output
              nuclei (left GPi, left SNr); projects to the left
              premotor and motor cortices (SMA, premotor, M1). The VA
              is the thalamic relay of the basal-ganglia-thalamo-
              cortical motor loop.
            * ventral_lateral_nucleus/ (VL): the CEREBELLAR MOTOR
              RELAY. Receives input from the left cerebellar dentate
              nucleus (and interposed nucleus); projects to the left
              motor cortex (M1). The VL contains the VIM
              (ventral-intermediate) subnucleus, the principal DBS
              target for essential tremor and Parkinsonian tremor.
              The VL is the thalamic relay of the
              cerebello-thalamo-cortical motor loop.

        - SOMATOSENSORY RELAYS (two nuclei, organized under a
          SUB-CONTAINER):
            * ventral_posterior_nucleus/ (VP; SUB-CONTAINER):
                - ventral_posterior_lateral_nucleus/ (VPL): the BODY
                  SOMATOSENSORY relay. Receives the medial lemniscus
                  (dorsal column pathway; fine touch, vibration,
                  proprioception) and the spinothalamic tract (pain,
                  temperature, crude touch) from the body; projects to
                  the left primary somatosensory cortex (S1) body map
                  (postcentral gyrus, hand/face areas).
                - ventral_posterior_medial_nucleus/ (VPM): the FACE
                  SOMATOSENSORY relay. Receives the trigeminothalamic
                  tract from the face and head; projects to the left
                  S1 face map. (Note: the VPM also receives taste
                  input from the parabrachial nucleus to its
                  parvicellular subdivision, projecting to the
                  gustatory cortex.)
              The VPL and VPM are organized under the
              ventral_posterior_nucleus/ sub-container because they are
              a SOMATOTOPIC SPLIT of one functional system (the body
              vs. face maps), not two functionally independent nuclei.
              This is a STANDARD CONTAINER pattern (VPL and VPM are
              CHILDREN of the sub-container), NOT the "sibling"
              pattern of the medial group's intralaminar/midline
              sub-containers.

    The ventral group is therefore TWO GROUPS IN ONE: motor (VA/VL) and
    somatosensory (VPL/VPM). Its four nuclei are the thalamic relays of
    the two sensory-motor systems that dominate the lateral thalamus.
    It is the LAST thalamic group to be drafted, and its completion
    finishes the entire thalamus subtree.

    NAMING TRAPS (critical — SIX apply at this group level):

    - TRAP 1: VPL vs. VPM (the somatotopic-split trap; the group's
      signature trap). Both are primary somatosensory relays; both
      project to S1. But VPL = BODY (medial lemniscus + spinothalamic);
      VPM = FACE (trigeminothalamic) + TASTE (parabrachial to the
      parvicellular VPM). Different body maps; different drivers;
      distinct nuclei. Do not merge; the VPL/VPM distinction is a
      SOMATOTOPIC SPLIT of one functional system, NOT a functional
      split between two independent systems.

    - TRAP 2: VA vs. VL (the motor-relay-family trap). Both are motor
      thalamic relays; both project to motor cortex. But VA = BASAL
      GANGLIA driver (GPi/SNr → VA → premotor/SMA/M1); VL = CEREBELLAR
      driver (dentate → VL → M1). Different drivers; different cortical
      targets (VA: premotor/SMA dominant; VL: M1 dominant, with the
      VIM tremor target); distinct nuclei. Do not merge; the VA/VL
      distinction is a DRIVER split within the motor thalamus, not a
      "two motor relays with the same job."

    - TRAP 3: VPL/VPM vs. LP (the first-order-vs-higher-order
      somatosensory-parietal trap; declared from the LP side in
      thalamus/left/lateral_nuclear_group/lateral_posterior_nucleus/;
      THIS CONTAINER IS THE CANONICAL DECLARATION FROM THE FIRST-ORDER
      SIDE). The VPL/VPM are FIRST-ORDER somatosensory relays (peripheral
      driver → S1, areas 3/1/2). The LP is the HIGHER-ORDER parietal
      association relay (cortical layer 5 driver → posterior parietal
      cortex, areas 5/7). Both project to the parietal lobe, but for
      DIFFERENT relay types and DIFFERENT cortical targets. Do not
      merge.

    - TRAP 4: VPL/VPM vs. Pf (the first-order-vs-affective nociceptive
      trap; declared from the Pf side in
      thalamus/left/medial_nuclear_group/parafascicular_nucleus/; THIS
      CONTAINER IS THE CANONICAL DECLARATION FROM THE FIRST-ORDER
      SIDE). The VPL/VPM receive spinothalamic nociceptive input for
      the SENSORY-DISCRIMINATIVE dimension of pain (location,
      intensity, quality). The Pf receives spinothalamic nociceptive
      input for the AFFECTIVE-MOTIVATIONAL dimension (arousal,
      attention, emotional response). Both are involved in pain, but
      for DIFFERENT DIMENSIONS. Do not merge.

    - TRAP 5: VA/VL vs. CM (the motor-relay vs. intralaminar-motor
      trap; declared from the CM side in
      thalamus/left/medial_nuclear_group/centromedian_nucleus/; THIS
      CONTAINER IS THE CANONICAL DECLARATION FROM THE MOTOR-RELAY
      SIDE). The VA/VL are FIRST-ORDER motor relays (basal ganglia or
      cerebellar driver → motor cortex). The CM is an INTRALAMINAR
      motor/arousal relay (basal ganglia driver → striatum, not motor
      cortex; re-entrant loop). Both receive basal ganglia input and
      are motor-adjacent, but for DIFFERENT relay types and DIFFERENT
      output targets. Do not merge.

    - TRAP 6: VPL vs. SPINOTHALAMIC vs. MEDIAL LEMNISCUS (the
      "where does the driver come from" trap). The VPL receives TWO
      distinct ascending somatosensory pathways: the medial lemniscus
      (dorsal column; fine touch, vibration, proprioception) and the
      spinothalamic tract (pain, temperature, crude touch). These are
      SEPARATE DRIVERS converging on the same VPL, and they map to
      slightly different VPL subregions (the VPL's "shell" vs. "core"
      in some species). Do not treat the VPL as a single undifferentiated
      somatosensory relay; document both drivers.

Functional Mode:
    - Motor relay — basal ganglia (VA; the anchor role):
        * VA receives basal ganglia output from the left GPi (and
          SNr), and projects to the left premotor cortex, the
          supplementary motor area (SMA), and M1.
        * The VA is the thalamic relay of the basal-ganglia-thalamo-
          cortical motor loop. Its contribution is MOTOR PROGRAM
          SELECTION and MOTOR INITIATION (the basal ganglia's
          "selection" of which motor program to run).
    - Motor relay — cerebellar (VL; the second motor role):
        * VL receives cerebellar output from the left dentate nucleus
          (and interposed nucleus), and projects to the left M1.
        * The VL is the thalamic relay of the cerebello-thalamo-cortical
          motor loop. Its contribution is MOTOR COORDINATION,
          TIMING, and ERROR CORRECTION (the cerebellum's role).
        * The VL contains the VIM (ventral-intermediate) subnucleus,
          which is the principal DBS target for essential tremor and
          Parkinsonian tremor. The VIM is the cerebellar-receiving
          portion of the VL; its DBS suppresses tremor via its
          cerebello-thalamo-cortical pathway.
    - Somatosensory relay — body (VPL; the first somatosensory role):
        * VPL receives the medial lemniscus (dorsal column pathway;
          fine touch, vibration, proprioception) and the spinothalamic
          tract (pain, temperature, crude touch) from the body, and
          projects to the S1 body map (postcentral gyrus).
        * The VPL is the thalamic relay of the ascending somatosensory
          pathways for the BODY.
    - Somatosensory relay — face + taste (VPM; the second somatosensory
      role):
        * VPM receives the trigeminothalamic tract (face and head
          somatosensation) and projects to the S1 face map.
        * VPM also receives taste input from the parabrachial nucleus
          to its PARVICELLULAR subdivision (VPMpc), which projects to
          the gustatory cortex (anterior insula). The VPM is therefore
          not purely somatosensory — it carries the taste pathway as
          well.
        * The VPM is the thalamic relay of the face somatosensory and
          taste pathways.
    - The ventral group is therefore the THALAMUS'S MOTOR AND
      SOMATOSENSORY GROUP: it is the thalamic relay of two motor loops
      (basal ganglia, cerebellar) and two somatosensory modalities
      (body, face + taste). Its completion finishes the thalamus's
      relay documentation.

    - CLINICAL FACTS (one per nucleus; all with contralateral
      specification where applicable):
        * VPL LESIONS: produce CONTRALATERAL BODY SOMATOSENSORY
          DEFICITS — a left VPL lesion produces RIGHT body
          somatosensory loss (hemianesthesia; loss of fine touch,
          vibration, proprioception, pain, and temperature on the
          right side of the body). VPL lesions can also produce
          THALAMIC PAIN SYNDROME (Dejerine-Roussy syndrome; chronic
          contralateral pain after a thalamic stroke). The VPL's
          clinical anchor is the contralateral hemianesthesia.
        * VPM LESIONS: produce CONTRALATERAL FACE SOMATOSENSORY
          DEFICITS — a left VPM lesion produces RIGHT face
          somatosensory loss (facial hemianesthesia; loss of touch,
          pain, temperature on the right side of the face). VPM
          lesions can also produce taste deficits if the parvicellular
          subdivision is affected.
        * VA LESIONS: produce MOTOR DEFICITS (rare in isolation;
          the VA is supplied by the posterior cerebral artery
          territory). VA-specific syndromes are not well described
          because the VA is rarely affected in isolation.
        * VL LESIONS: produce TREMOR, ATAXIA, and MOTOR
          COORDINATION DEFICITS. The VIM subregion is the principal
          DBS target for essential tremor and Parkinsonian tremor;
          VIM DBS is an established treatment for medication-refractory
          tremor.
        * The ventral group's clinical anchors are therefore
          MODALITY-SPECIFIC and CONTRALATERAL:
            - VPL: contralateral body hemianesthesia (established).
            - VPM: contralateral face hemianesthesia (established).
            - VA: motor deficits (rare in isolation).
            - VL: tremor/ataxia; VIM DBS for tremor (established
              treatment).

Hormonal Modulation (group-wide summary; per-nucleus wiring in the
child leaves):
    - The ventral group is NOT a neuroendocrine structure.
    - Modulators:
        * VA/VL: dopaminergic (SNc → striatum → basal ganglia → VA/VL;
          the motor loop's dopamine modulation); cholinergic
          (brainstem, basal forebrain); monoaminergic (brainstem).
        * VPL/VPM: cholinergic (brainstem, basal forebrain) and
          monoaminergic (brainstem) arousal modulation of sensory
          relay gain; cortical corticothalamic feedback from S1
          modulates VPL/VPM gain.
    - The ventral group is NOT a principal target of the 12 endocrine
      axes. Do not pad the section with CRH, cortisol, etc.

Memory Interfaces (group-wide summary):
    - VA/VL: reads procedural (the motor loops use procedural memory
      for motor programs and skills); short_term (current motor
      state buffer).
    - VPL/VPM: reads short_term (the current somatosensory sensory
      buffer being relayed).
    - Writes: none directly. The ventral group relays motor and
      sensory signals; the memory content is stored in the cortex and
      basal ganglia/cerebellum.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No ventral group fragment. The ventral group is a motor and
      somatosensory relay group; the model prompt does not need a
      ventral-group block because the motor and sensory signals it
      relays are already represented in the upstream (basal ganglia,
      cerebellum, body/face periphery) and downstream (motor cortex,
      S1) fragments. The motor and somatosensory cortical states are
      carried by M1 and S1.
    - AGGREGATION RULES: no fragments are emitted from this container
      or from any ventral-group leaf. Deliberate absence, same as the
      whole thalamus.
    - The ventral group's clinical facts (contralateral hemianesthesia;
      VIM DBS for tremor) are documented for completeness, but are not
      prompt fields.

Children (four nuclei + one sub-container):
    Motor family (two full leaves):
    - ventral_anterior_nucleus/   ★ Tier 1 leaf. The VA; basal ganglia
                                    motor relay.
    - ventral_lateral_nucleus/    ★ Tier 1 leaf. The VL; cerebellar
                                    motor relay; VIM DBS target for
                                    tremor.

    Somatosensory family (sub-container with two full leaves):
    - ventral_posterior_nucleus/  Sub-container. Groups VPL and VPM as
                                    a SOMATOTOPIC SPLIT (body vs.
                                    face); NOT a functional split.
        ├── ventral_posterior_lateral_nucleus/  ★ Tier 1 leaf. The
        │                                         VPL; body
        │                                         somatosensory
        │                                         relay.
        └── ventral_posterior_medial_nucleus/   ★ Tier 1 leaf. The
                                                  VPM; face
                                                  somatosensory and
                                                  taste relay.

    All four nuclei are full leaves (not deltas of each other); the
    left/right pairs follow the standard hemisphere-delta pattern.

Notes:
    - Group container. Names the four nuclei and the sub-container;
      defers functional content to the leaves (except for the
      container-level summary above).
    - THE VPL vs. VPM TRAP is the group's signature trap: both are
      first-order somatosensory relays, but the VPL/VPM split is a
      SOMATOTOPIC SPLIT (body vs. face maps), not a functional split.
      Reproduced in full; the VPL/VPM leaves must enforce it.
    - THE VA vs. VL TRAP is the motor-family trap: both are motor
      relays, but the VA/VL split is a DRIVER SPLIT (basal ganglia vs.
      cerebellum), not a "two motor relays with the same job."
      Reproduced in full; the VA/VL leaves must enforce it.
    - THE VPL/VPM vs. LP TRAP and the VPL/VPM vs. Pf TRAP are the two
      cross-group first-order-vs-higher-order/nociceptive traps;
      declared from the LP and Pf sides; THIS CONTAINER IS THE
      CANONICAL DECLARATION FROM THE FIRST-ORDER SIDE.
    - THE VA/VL vs. CM TRAP is the motor-relay-vs-intralaminar-motor
      trap; declared from the CM side; THIS CONTAINER IS THE CANONICAL
      DECLARATION FROM THE MOTOR-RELAY SIDE.
    - THE VPL's TWO DRIVERS (medial lemniscus + spinothalamic) is a
      "where does the driver come from" trap; both drivers converge on
      the VPL. Document both.
    - THE VENTRAL_POTTERIOR_NUCLEUS SUB-CONTAINER IS A STANDARD
      CONTAINER: VPL and VPM are its CHILDREN, not its siblings. This
      is DIFFERENT from the medial group's intralaminar/midline
      sub-containers (which are siblings of their members). The
      ventral posterior sub-container is a genuine hierarchical
      container; the intralaminar/midline sub-containers are
      integration layers whose members are also their siblings.
    - THE VENTRAL GROUP IS TWO GROUPS IN ONE: motor (VA/VL) and
      somatosensory (VPL/VPM). Do not flatten them into a single
      functional family.
    - THE VIM (VENTRAL-INTERMEDIATE) SUBNUCLEUS is part of the VL and
      is the principal DBS target for essential tremor and Parkinsonian
      tremor. The VL leaf must document the VIM as a subregion, not as
      a child node (same convention as the LGN's layers, the MGN's
      divisions, and the pulvinar's subregions).
    - THE VPMpc (parvicellular VPM) CARRIES TASTE: the VPM is not purely
      somatosensory; it carries the taste pathway from the parabrachial
      nucleus. Document this; do not draft the VPM as purely
      "face somatosensory."
    - NO FRAGMENT: same as the whole thalamus. The ventral group is a
      relay group, not a state-emitter.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, dopamine,
      GABA, glutamate); memory/stores/ (procedural, short_term);
      gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * ventral_nuclear_group/left/ventral_anterior_nucleus ↔
          telencephalon/.../subcortical/basal_ganglia/left (GPi/SNr →
          VA; basal ganglia motor input) and → telencephalon/.../
          cortex/frontal/premotor_cortex and supplementary_motor_cortex
          and primary_motor_cortex (VA → premotor/SMA/M1; cortical
          motor output).
        * ventral_nuclear_group/left/ventral_lateral_nucleus ↔
          cerebellum/.../deep cerebellar nuclei (left dentate →
          VL; cerebellar motor input) and → telencephalon/.../
          cortex/frontal/primary_motor_cortex (VL → M1; with VIM as a
          DBS target subregion).
        * ventral_nuclear_group/left/ventral_posterior_nucleus/
          ventral_posterior_lateral_nucleus ↔ spinal cord + brainstem
          (medial lemniscus and spinothalamic; body somatosensory
          input) and → telencephalon/.../cortex/parietal/
          primary_somatosensory_cortex (S1 body map).
        * ventral_nuclear_group/left/ventral_posterior_nucleus/
          ventral_posterior_medial_nucleus ↔ brainstem trigeminal
          (face somatosensory input) and → telencephalon/.../
          cortex/parietal/primary_somatosensory_cortex (S1 face map);
          and ↔ brainstem/.../parabrachial_nucleus (taste input to
          VPMpc) and → telencephalon/.../cortex/insular/primary_
          gustatory_cortex (taste output from VPMpc).
        * The VPL/VPM vs. LP, VPL/VPM vs. Pf, and VA/VL vs. CM traps
          are documented as cross-group distinctions (not signaling
          edges) — see the TRAP sections above.
    - Connects upward to diencephalon/thalamus/left/.
"""