"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.ventral_nuclear_group.ventral_lateral_nucleus
Anatomical Role:
    The left ventral lateral nucleus (VL). A motor thalamic nucleus in
    the left ventral nuclear group, situated posterior to the left VA
    and lateral to the left MD. It is the CEREBELLAR MOTOR RELAY of
    the left thalamus: the thalamic relay of the
    cerebello-thalamo-cortical motor loop.

    The VL's distinct position within the ventral group's motor family:
        - VA (thalamus/left/ventral_nuclear_group/ventral_anterior_
          nucleus/): BASAL GANGLIA driver (left GPi/SNr → VA → left
          premotor/SMA/M1). Role: motor program SELECTION and
          INITIATION.
        - VL (this leaf): CEREBELLAR driver (left dentate → VL → left
          M1, with the VIM subnucleus). Role: motor COORDINATION,
          TIMING, and ERROR CORRECTION.
    The VA and VL are the two motor relays of the thalamus; the VL is
    the cerebellar half.

    The VL's subdivisions (documented WITHIN this leaf, not as child
    nodes):
        - VIM (ventral-intermediate): the CEREBELLAR-RECEIVING
          subdivision. Receives input from the left dentate nucleus
          and projects to the left M1 (hand/face/arm areas). The VIM
          is the PRINCIPAL DBS TARGET for essential tremor and
          Parkinsonian tremor. The VIM is the VL's most clinically
          significant subdivision.
        - VLc (caudal VL): a cerebellar-receiving subdivision adjacent
          to the VIM; also receives dentate input and projects to M1.
        - VLps (posterior superior VL): a cerebellar-receiving
          subdivision; part of the cerebellar motor relay.
        - VLo (oral VL): a basal ganglia-receiving subdivision (overlaps
          with the VA); receives pallidal input; projects to premotor
          and motor areas. The VLo's basal ganglia input means the VL
          is not purely cerebellar — a small basal ganglia component
          exists at its anterior margin.
    Same convention as the LGN's six layers, the MGN's three
    divisions, the pulvinar's three subregions, the MD's three
    subdivisions, and the VA's subdivisions: the VL's subdivisions are
    documented within this leaf, not as tree children. Do not create
    vim/, vlc/, vlps/, or vlo/ as child nodes.

    DISTINCTIONS (critical):

    - VL vs. VA (the motor-family trap; reproduced from the ventral
      group container and the VA leaf): both are motor thalamic
      relays; both project to motor cortex. But VL = CEREBELLAR driver
      (left dentate → VL → left M1, with VIM); VA = BASAL GANGLIA
      driver (left GPi/SNr → VA → left premotor/SMA/M1). Different
      drivers; different cortical emphases (VL: M1 dominant; VA:
      premotor/SMA dominant); distinct nuclei. Do not merge; the
      VL/VA split is a DRIVER SPLIT within the motor thalamus.

    - VA/VL vs. CM (the motor-relay vs. intralaminar-motor trap;
      declared from the CM side and canonically from the VA side; this
      leaf enforces it from the VL side): the VL and VA are
      FIRST-ORDER motor relays (motor cortex targets); the CM
      (thalamus/left/medial_nuclear_group/centromedian_nucleus/) is an
      INTRALAMINAR motor/arousal relay (basal ganglia driver →
      striatum, not motor cortex; re-entrant loop). Both receive basal
      ganglia input and are motor-adjacent, but for DIFFERENT relay
      types and DIFFERENT output targets. Do not merge.

    - VL vs. MD (motor vs. prefrontal): the VL is a MOTOR relay
      (cerebellar → motor cortex); the MD
      (thalamus/left/medial_nuclear_group/medial_dorsal_nucleus/) is a
      PREFRONTAL relay (amygdala/PFC → PFC). Different functional
      systems; do not merge.

    - VL vs. VPL/VPM (motor vs. somatosensory in the ventral group):
      the VL is a MOTOR relay (cerebellar → M1); the VPL/VPM
      (thalamus/left/ventral_nuclear_group/ventral_posterior_nucleus/)
      are SOMATOSENSORY relays (body/face periphery → S1). Both are in
      the ventral group, but for DIFFERENT relay types and DIFFERENT
      cortical targets. Do not merge.

    - VL vs. STN (motor circuit vs. motor circuit, different nodes):
      both the VL and the STN (thalamus/left/subthalamus/subthalamic_
      nucleus/) participate in motor circuits, but through DIFFERENT
      roles: the VL is a THALAMIC motor RELAY (cerebellar → M1); the
      STN is a BASAL GANGLIA EXCITATORY node (indirect pathway).
      Adjacent in the motor circuit but at different levels; do not
      merge.

Functional Mode:
    - Cerebellar motor relay (the VL's anchor role):
        * The VL receives cerebellar output from the left dentate
          nucleus (and the interposed nucleus) — the cerebellar
          nuclei that carry the cerebellum's "coordination" signal.
        * The VL projects to the left M1, primarily to the hand/face/
          arm representations (the cerebellar motor cortex targets).
        * The VL's role is MOTOR COORDINATION, TIMING, and ERROR
          CORRECTION: it relays the cerebellum's contribution to
          ongoing movement, adjusting the motor program in real time.
        * The VL's contribution is DISTINCT from the VA's: the VL is
          the cerebellum's "coordination" signal; the VA is the basal
          ganglia's "selection" signal. The VL is involved in the
          EXECUTION and FINE-TUNING of movement; the VA is involved
          in SELECTING which movement to execute.
    - VIM subnucleus (the VL's most clinically significant subdivision):
        * The VIM (ventral-intermediate) is the cerebellar-receiving
          portion of the VL that projects to the M1 hand/arm/face
          representations.
        * The VIM is the PRINCIPAL DBS TARGET for essential tremor
          and Parkinsonian tremor: high-frequency DBS of the VIM
          suppresses tremor, presumably by disrupting the
          cerebello-thalamo-cortical tremor-generating circuit.
        * VIM DBS for tremor is a long-established standard of care
          (since the 1990s), with strong clinical evidence; it is one
          of the most-established deep brain stimulation targets in
          neurology.
    - Cerebello-thalamo-cortical loop (the VL's functional circuit):
        * The full circuit:
            cerebellum (dentate/interposed) → VL (VIM/VLc/VLps) →
            M1 → corticopontine → pontine nuclei → cerebellum.
          The VL is the thalamic node of this loop; the loop is
          essential for motor learning, coordination, and timing.
        * The VL's role in motor learning (particularly the early
          phase of motor skill acquisition) is established; the
          cerebellar-VL-M1 circuit is required for adapting motor
          programs to changing conditions.
    - Basal ganglia contribution at the VL's anterior margin (the VLo
      subdivision):
        * The VL's oral subdivision (VLo) receives some pallidal
          input, overlapping with the VA. The VLo is a transitional
          zone between the basal ganglia (VA-dominant) and cerebellar
          (VL-dominant) motor territories. Document this; do not
          draft the VL as "purely cerebellar."
    - The VL is therefore the THALAMUS'S CEREBELLAR MOTOR RELAY: it is
      the thalamic relay of the cerebello-thalamo-cortical motor loop,
      the anatomical substrate of motor coordination and timing, and
      the VIM DBS anchor for tremor.

    - CLINICAL FACTS (the VL's defining clinical anchors):
        * VIM DBS FOR TREMOR (the VL's most established clinical
          anchor): high-frequency DBS of the VIM suppresses essential
          tremor and Parkinsonian tremor. Established standard of
          care; long-term efficacy and safety data; one of the
          best-established DBS targets in neurology. Contralateral
          effect: left VIM DBS suppresses RIGHT-sided tremor
          predominantly (bilateral DBS suppresses both sides).
        * VL LESIONS: produce CONTRALATERAL MOTOR COORDINATION
          DEFICITS (ataxia, tremor, dysmetria, hypotonia on the
          contralateral side). VL lesions are rare in isolation
          because the VL is supplied by the posterior cerebral
          artery territory (VL strokes usually co-occur with other
          PCA-territory deficits). VL lesions can produce a
          contralateral "cerebellar-type" syndrome (ataxia, tremor),
          reflecting the loss of the cerebellar motor relay.
        * CEREBELLO-THALAMO-CORTICAL STROKE: PCA-territory infarcts
          involving the VL produce the contralateral cerebellar-type
          syndrome, often with other PCA-territory deficits (e.g.,
          hemianopia from LGN involvement, hemianesthesia from VPL
          involvement).
        * DENTATORUBROTHALAMIC ATROPHY (DRPLA) and other
          cerebellar-thalamic degenerations: the VL is involved in
          these conditions, contributing to the motor symptoms
          (ataxia, choreoathetosis, dementia in DRPLA). Documented as
          a degenerative context; not a VL-specific syndrome.
        * The VL's clinical anchor is therefore VIM DBS FOR TREMOR
          (established) plus CONTRALATERAL CEREBELLAR-TYPE DEFICITS
          from VL lesions. This is a STRONGER clinical anchor than
          the VA's (investigational/secondary DBS), and comparable in
          scope to the LGN's hemianopia and the CM's DBS anchor.

Hormonal Modulation (minimal; the VL is a motor relay):
    - The VL is NOT a neuroendocrine structure.
    - Modulators: dopaminergic (left SNc → striatum → basal ganglia →
      VLo's small basal ganglia component; the dopamine modulation of
      the VL's motor circuit); cholinergic (brainstem, basal
      forebrain); monoaminergic (brainstem) arousal inputs. Document
      as motor and arousal modulation, not endocrine modulators.
    - The VL is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * procedural: the VL's motor coordination depends on learned
          motor skills (procedural memory); the cerebellum-VL-M1 loop
          is required for motor learning and skill acquisition.
        * short_term: the current motor state buffer (the VL's
          coordination occurs in the context of the ongoing movement).
    - Writes: none directly. The VL is a RELAY: it transmits the
      cerebellum's coordination signal to M1; the motor skills
      themselves are stored in the cerebellum and cortex.
    - The VL's memory interface (procedural + short_term) is the same
      as the VA's, and it is the THICKER of the ventral group's motor
      interfaces (the somatosensory VPL/VPM read only short_term).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No VL fragment. The VL is a motor relay; the model prompt does
      not need a VL block because the motor coordination signals it
      relays are already represented in the upstream (cerebellum) and
      downstream (M1) fragments. The motor cortical state is carried
      by M1.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The VL's clinical facts (VIM DBS for tremor; VL lesions;
      cerebello-thalamo-cortical stroke) are documented for
      completeness, but are not prompt fields.

Reciprocal Connections (left-side; the right side is in
../../../../../right/ventral_nuclear_group/ventral_lateral_nucleus/):

    Cerebello-thalamo-cortical motor loop (the anchor):
    - ← cerebellum/.../deep_cerebellar_nuclei/left/dentate_nucleus
      (left dentate → left VL; the principal cerebellar motor input to
      the VL; the VL's driver input; the dentate nucleus is
      midline-adjacent — verify).
    - ← cerebellum/.../deep_cerebellar_nuclei/left/interposed_nucleus
      (left interposed → left VL; a secondary cerebellar motor input
      to the VL; the interposed nucleus is midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      primary_motor_cortex (left VL → left M1; the VL's principal
      cortical output; the VL projects to the M1 hand/arm/face
      representations; VIM is the DBS-target subregion).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      premotor_cortex (left VL → left premotor cortex; less dense
      than the M1 projection but present).
    - ← telencephalon/cerebral_hemispheres/left/cortex/frontal/
      primary_motor_cortex (left M1 → left VL; corticothalamic
      feedback; the motor cortex modulates VL relay gain).

    Basal ganglia component (secondary; VLo subdivision):
    - ← telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      left (left GPi → left VLo; the small basal ganglia component at
      the VL's anterior margin; overlapping with the VA).

    Distinction (not signaling; structural note):
    - ↔ ../ventral_anterior_nucleus/ (left VA; the BASAL GANGLIA motor
      relay; distinct driver and distinct cortical emphasis; do not
      merge; the VA/VL driver split).
    - ↔ ../../medial_nuclear_group/centromedian_nucleus/ (left CM;
      INTRALAMINAR motor/arousal relay; striatal output, not motor
      cortex; distinct relay type; do not merge).
    - ↔ ../ventral_posterior_nucleus/ (left VPL/VPM; SOMATOSENSORY
      relays; distinct relay types; do not merge).
    - ↔ ../../medial_nuclear_group/medial_dorsal_nucleus/ (left MD;
      PREFRONTAL relay; distinct functional system; do not merge).
    - ↔ ../../subthalamus/subthalamic_nucleus/ (left STN; BASAL GANGLIA
      excitatory node; different motor circuit role; do not merge).

Notes:
    - Tier 1 full leaf (left). The CEREBELLAR MOTOR RELAY of the
      ventral group; the counterpart to the VA's BASAL GANGLIA motor
      relay.
    - THE VIM SUBNUCLEUS is documented WITHIN this leaf, not as a
      child node. Same convention as the LGN's six layers, the MGN's
      three divisions, the pulvinar's three subregions, the MD's
      three subdivisions, and the VA's subdivisions. Do not create
      a vim/ child node.
    - THE VL's SUBDIVISIONS (VIM, VLc, VLps, VLo) are documented
      within this leaf. The VIM is the cerebellar-receiving
      tremor-DBS anchor; the VLo is the small basal ganglia component
      at the VL's anterior margin. Do not flatten the VL as
      "purely cerebellar" — the VLo carries a basal ganglia
      contribution.
    - THE VL vs. VA TRAP is the motor-family trap; reproduced in full
      (VA = basal ganglia driver; VL = cerebellar driver; different
      cortical emphases); the VA and VL leaves enforce it from their
      respective sides.
    - THE VA/VL vs. CM TRAP is the motor-relay vs. intralaminar-motor
      trap; this leaf enforces it from the VL side, matching the VA
      leaf's canonical declaration.
    - THE VL vs. VPL/VPM, VL vs. MD, and VL vs. STN distinctions are
      reproduced (different functional systems within the thalamus).
    - THE VIM DBS FOR TREMOR is the VL's defining clinical anchor: it
      is the most-established DBS target for tremor in neurology.
      Left VIM DBS suppresses RIGHT-sided tremor predominantly (the
      right VL delta documents the reverse: right VIM DBS suppresses
      LEFT-sided tremor predominantly). Bilateral VIM DBS suppresses
      both sides.
    - THE CONTRALATERAL CLINICAL FACTS apply on the left with the
      correct direction: left VIM DBS → predominantly RIGHT-sided
      tremor suppression; left VL lesion → RIGHT-side motor
      coordination deficits. The left and right VL leaves document
      the opposite directions explicitly.
    - THE VIM DBS ANCHOR IS ESTABLISHED (unlike the VA's
      investigational/secondary DBS). The VL has the strongest DBS
      anchor in the thalamus (VIM for tremor), with the CM (Tourette's,
      disorders of consciousness) and the MD (depression) being the
      other two.
    - NO FRAGMENT: same as the whole thalamus. The VL is a relay, not
      a state-emitter.
    - The VL is NOT the VA (basal ganglia), NOT the CM (intralaminar
      motor/arousal), NOT the VPL/VPM (somatosensory), NOT the MD
      (prefrontal), NOT the STN (basal ganglia excitatory node). The
      traps make these distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, GABA, glutamate,
      acetylcholine, monoamines); memory/stores/ (procedural,
      short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/ventral_nuclear_
      group/.
"""