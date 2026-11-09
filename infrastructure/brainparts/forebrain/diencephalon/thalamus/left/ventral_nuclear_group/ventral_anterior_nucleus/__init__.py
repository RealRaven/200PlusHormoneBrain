"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.ventral_nuclear_group.ventral_anterior_nucleus
Anatomical Role:
    The left ventral anterior nucleus (VA). A motor thalamic nucleus in
    the left ventral nuclear group, situated anterior to the left VL
    and lateral to the left MD. It is the BASAL GANGLIA MOTOR RELAY of
    the left thalamus: the thalamic relay of the
    basal-ganglia-thalamo-cortical motor loop.

    The VA's distinct position within the ventral group's motor family:
        - VA (this leaf): BASAL GANGLIA driver (left GPi and left SNr →
          VA → left premotor cortex, SMA, and M1). The VA's role is
          MOTOR PROGRAM SELECTION and MOTOR INITIATION — the basal
          ganglia's "selection" of which motor program to run.
        - VL (thalamus/left/ventral_nuclear_group/
          ventral_lateral_nucleus/): CEREBELLAR driver (left dentate →
          VL → left M1, with the VIM subnucleus). The VL's role is
          MOTOR COORDINATION, TIMING, and ERROR CORRECTION — the
          cerebellum's contribution.
    The VA and VL are the two motor relays of the thalamus, but with
    DIFFERENT DRIVERS (basal ganglia vs. cerebellum) and DIFFERENT
    CONTRIBUTIONS (selection/initiation vs. coordination/timing). Do
    not merge them; the VA is not "the motor thalamus" — it is the
    basal ganglia half of the motor thalamus.

    The VA's subdivisions (documented WITHIN this leaf, not as child
    nodes):
        - Principal VA (VApc; parvicellular): the main basal
          ganglia-receiving subdivision; projects primarily to the
          premotor cortex and SMA.
        - Magnocellular VA (VAmc): receives some nigral and
          pallidal input; projects to M1 and premotor areas;
          partially overlaps with the VL.
    Same convention as the LGN's six layers, the MGN's three
    divisions, the pulvinar's three subregions, the MD's three
    subdivisions, and the VL's VIM subnucleus: the VA's subdivisions
    are documented within this leaf, not as tree children. Do not
    create vapc/ or vamc/ as child nodes.

    DISTINCTIONS (critical):

    - VA vs. VL (the motor-family trap; reproduced from the ventral
      group container): both are motor thalamic relays; both project
      to motor cortex. But VA = BASAL GANGLIA driver (left GPi/SNr →
      VA → premotor/SMA/M1); VL = CEREBELLAR driver (left dentate →
      VL → M1, with VIM). Different drivers; different cortical
      targets (VA: premotor/SMA dominant; VL: M1 dominant); distinct
      nuclei. Do not merge; the VA/VL split is a DRIVER SPLIT within
      the motor thalamus, not "two motor relays with the same job."

    - VA/VL vs. CM (the motor-relay vs. intralaminar-motor trap;
      declared from the CM side in
      thalamus/left/medial_nuclear_group/centromedian_nucleus/; THIS
      LEAF IS THE CANONICAL FIRST-ORDER MOTOR SIDE of the trap). The
      VA and VL are FIRST-ORDER motor relays (basal ganglia or
      cerebellar driver → motor cortex). The CM is an INTRALAMINAR
      motor/arousal relay (basal ganglia driver → striatum; re-entrant
      loop; not motor cortex). Both receive basal ganglia input and
      are motor-adjacent, but for DIFFERENT relay types and DIFFERENT
      output targets. Do not merge.

    - VA vs. MD (both "medial group adjacent" but distinct): the VA
      is a MOTOR relay (basal ganglia → motor cortex); the MD
      (thalamus/left/medial_nuclear_group/medial_dorsal_nucleus/) is a
      PREFRONTAL relay (amygdala/PFC → PFC). Both are in the medial-
      adjacent thalamus, but for DIFFERENT functional systems. Do not
      merge.

    - VA vs. VPL/VPM (the motor-vs-somatosensory ventral group trap):
      the VA is a MOTOR relay (basal ganglia → motor cortex); the
      VPL/VPM (thalamus/left/ventral_nuclear_group/
      ventral_posterior_nucleus/) are SOMATOSENSORY relays (body/face
      periphery → S1). Both are in the ventral group, but for
      DIFFERENT relay types (motor vs. sensory) and DIFFERENT cortical
      targets (M1 vs. S1). Do not merge.

Functional Mode:
    - Motor program selection and initiation (the VA's anchor role):
        * The VA receives basal ganglia output from the left GPi (and
          the left SNr) — the same output that the basal ganglia's
          "direct" and "indirect" pathways converge on. The GPi/SNr
          output is GABAergic and tonically inhibitory; the VA
          receives this inhibition, and the basal ganglia's "release"
          of the VA (via transient GPi/SNr inhibition) allows motor
          programs to be initiated.
        * The VA projects to the left premotor cortex, the left SMA,
          and the left M1. The VA's role is therefore to SELECT and
          INITIATE motor programs: it relays the basal ganglia's
          "selected" motor program to the cortical motor areas that
          execute it.
        * The VA's contribution is DISTINCT from the VL's: the VA is
          the basal ganglia's "selection" signal; the VL is the
          cerebellum's "coordination" signal. The VA's role is
          MOTOR PROGRAM SELECTION and INITIATION; the VL's role is
          MOTOR COORDINATION, TIMING, and ERROR CORRECTION.
    - Premotor and SMA emphasis (the VA's distinctive cortical target
      pattern):
        * The VA projects MORE to the premotor cortex and SMA than to
          M1, in contrast to the VL, which projects MORE to M1. This
          cortical target pattern reflects the VA's role in motor
          PROGRAM SELECTION (premotor and SMA are involved in planning
          and selecting motor programs) rather than in motor
          EXECUTION (M1 is involved in executing the program).
        * The SMA's role in self-initiated movement and in the
          "readiness potential" (the premotor EEG signal that precedes
          voluntary movement) is anatomically linked to the VA's
          basal ganglia relay.
    - Hyperdirect and cortico-striatal loop coordination (secondary):
        * The VA relays the basal ganglia's contribution to motor
          selection, which is coordinated with the hyperdirect
          pathway (cortex → STN → GPi/SNr) and the cortico-striatal
          pathway (cortex → striatum → GPe/GPi). The VA is the final
          common thalamic pathway of the basal ganglia's motor
          selection output.
    - The VA is therefore the THALAMUS'S BASAL GANGLIA MOTOR RELAY: it
      is the thalamic relay of the
      basal-ganglia-thalamo-cortical motor loop, and the anatomical
      substrate of motor program selection and initiation.

    - CLINICAL FACTS (the VA's clinical anchors; subtler than the
      VL's VIM DBS anchor):
        * VA LESIONS: produce MOTOR DEFICITS (rare in isolation; the
          VA is supplied by the posterior cerebral artery territory
          and is rarely affected alone). VA-specific clinical
          syndromes are NOT well described; the VA's clinical
          relevance is as part of the basal ganglia motor system, not
          as an isolated clinical entity.
        * VA DBS (investigational): the VA has been investigated as a
          DBS target for some movement disorders (notably
          Parkinsonian tremor and some dystonias), but the VA DBS
          literature is THINNER than the VL's VIM DBS literature. The
          VIM (in the VL) is the principal DBS target for tremor; the
          VA is a secondary or alternative target. Document as
          "investigational/secondary."
        * VA-SPECIFIC SYNDROMES are NOT established. The VA's
          clinical contribution is as part of the basal ganglia motor
          system; its anatomical importance (the basal ganglia's
          motor output to the cortex) is greater than its clinical
          specificity.
        * The VA's clinical anchor is therefore the
          BASAL GANGLIA MOTOR SYSTEM (motor deficits from VA-region
          lesions; secondary DBS target), which is subtler than the
          VL's established VIM DBS anchor. This is the honest
          clinical framing.

Hormonal Modulation (minimal; the VA is a motor relay):
    - The VA is NOT a neuroendocrine structure.
    - Modulators: dopaminergic (SNc → striatum → basal ganglia → VA;
      the indirect dopamine modulation of the basal ganglia motor
      loop); cholinergic (brainstem, basal forebrain); monoaminergic
      (brainstem) arousal inputs. Document as motor and arousal
      modulation, not endocrine modulators.
    - The VA is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * procedural: the VA's motor program selection depends on
          learned motor programs (procedural memory); the basal
          ganglia's "selection" is of a learned program, not a novel
          movement.
        * short_term: the current motor state buffer (the VA's motor
          selection occurs in the context of the current motor state).
    - Writes: none directly. The VA is a RELAY: it transmits the basal
      ganglia's motor selection signal to the motor cortex; the motor
      programs themselves are stored in the cortex and basal ganglia.
    - The VA's memory interface is the THICKER of the two motor
      thalamic nuclei (procedural + short_term), matching the VL's
      memory interface. Both motor relays read procedural memory
      because both are part of motor program circuits.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No VA fragment. The VA is a motor relay; the model prompt does
      not need a VA block because the motor selection signals it
      relays are already represented in the upstream (basal ganglia)
      and downstream (premotor/SMA/M1) fragments. The motor cortical
      state is carried by the premotor/SMA/M1 fragments.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The VA's clinical facts (motor deficits; secondary DBS target)
      are documented for completeness, but are not prompt fields.

Reciprocal Connections (left-side; the right side is in
../../../../../right/ventral_nuclear_group/ventral_anterior_nucleus/):

    Basal ganglia motor loop (the anchor):
    - ← telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      left (GPi → VA; GABAergic; the principal basal ganglia motor
      output to the VA; the VA's driver input).
    - ← midbrain/tegmentum/substantia_nigra/left/pars_reticulata
      (SNr → VA; GABAergic; the basal ganglia's other output nucleus;
      the VA receives both GPi and SNr inhibition).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      premotor_cortex (VA → premotor cortex; the VA's premotor
      selection output; the VA's dominant cortical target for motor
      program selection).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      supplementary_motor_cortex (VA → SMA; the VA's SMA output;
      the SMA's role in self-initiated movement and readiness
      potential).
    - → telencephalon/cerebral_hemispheres/left/cortex/frontal/
      primary_motor_cortex (VA → M1; the VA's M1 output; less dense
      than the VL's M1 projection but present).

    Motor circuit feedback (secondary):
    - ← telencephalon/cerebral_hemispheres/left/cortex/frontal/
      premotor_cortex, supplementary_motor_cortex, and primary_motor_
      cortex (corticothalamic feedback from the motor cortex to the
      VA; the motor cortex modulates VA relay gain).

    Distinction (not signaling; structural note):
    - ↔ ../ventral_lateral_nucleus/ (left VL; the CEREBELLAR motor
      relay; distinct driver and distinct cortical emphasis; do not
      merge; the VA/VL driver split is the motor-family trap).
    - ↔ ../../medial_nuclear_group/centromedian_nucleus/ (left CM;
      INTRALAMINAR motor/arousal relay with striatal output, not
      motor cortex; distinct relay type; do not merge; the VA/VL vs.
      CM trap).
    - ↔ ../ventral_posterior_nucleus/ (the VPL/VPM somatosensory
      relays; MOTOR vs. SOMATOSENSORY in the same ventral group;
      distinct relay types; do not merge).

Notes:
    - Tier 1 full leaf (left). The BASAL GANGLIA MOTOR RELAY of the
      ventral group; the counterpart to the VL's CEREBELLAR motor
      relay.
    - THE VA vs. VL TRAP is the motor-family trap: both are motor
      relays; different drivers (basal ganglia vs. cerebellum);
      different cortical emphases (premotor/SMA vs. M1). Reproduced in
      full; the VA and VL leaves enforce it from their respective
      sides.
    - THE VA/VL vs. CM TRAP is the motor-relay vs. intralaminar-motor
      trap; declared from the CM side; THIS LEAF IS THE CANONICAL
      FIRST-ORDER MOTOR SIDE of the trap. Do not merge.
    - THE VA vs. MD and VA vs. VPL/VPM distinctions are reproduced
      (different functional systems within the thalamus).
    - THE VA's SUBDIVISIONS (VApc, VAmc) are documented WITHIN this
      leaf, not as child nodes. Same convention as the LGN's layers,
      the MGN's divisions, the pulvinar's subregions, the MD's
      subdivisions, and the VL's VIM subnucleus. Do not create vapc/
      or vamc/ as child nodes.
    - THE VA's PREMOTOR/SMA EMPHASIS is the VA's distinctive cortical
      target pattern (contrast with the VL's M1 emphasis). This is
      the anatomical basis of the VA's role in motor program
      SELECTION (premotor/SMA) rather than EXECUTION (M1).
    - THE VA's CLINICAL ANCHOR IS SUBTLER THAN THE VL's: the VA has no
      established DBS anchor comparable to the VL's VIM; the VA is a
      secondary/alternative DBS target. Documented honestly; do not
      overclaim.
    - VA-SPECIFIC SYNDROMES are NOT established (rare in isolation;
      the VA is part of the broader basal ganglia motor system). Do
      not invent a VA-specific syndrome.
    - NO FRAGMENT: same as the whole thalamus. The VA is a relay, not
      a state-emitter.
    - The VA is NOT the VL (cerebellar motor relay), NOT the CM
      (intralaminar motor/arousal), NOT the MD (prefrontal relay), NOT
      the VPL/VPM (somatosensory relays). The traps make these
      distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (dopamine, GABA, glutamate,
      acetylcholine, monoamines); memory/stores/ (procedural,
      short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/ventral_nuclear_
      group/.
"""