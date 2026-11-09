"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.ventral_nuclear_group.ventral_lateral_nucleus
Anatomical Role:
    The right ventral lateral nucleus (VL). A motor thalamic nucleus in
    the right ventral nuclear group, situated posterior to the right VA
    and lateral to the right MD. Same CEREBELLAR MOTOR RELAY role as the
    left VL: the thalamic relay of the right
    cerebello-thalamo-cortical motor loop.

    The VL's distinct position within the ventral group's motor family:
        - VA (thalamus/right/ventral_nuclear_group/ventral_anterior_
          nucleus/): BASAL GANGLIA driver (right GPi/SNr → VA → right
          premotor/SMA/M1). Role: motor program SELECTION and
          INITIATION.
        - VL (this leaf): CEREBELLAR driver (right dentate → VL →
          right M1, with the VIM subnucleus). Role: motor
          COORDINATION, TIMING, and ERROR CORRECTION.
    The VA and VL are the two motor relays of the thalamus; the VL is
    the cerebellar half.

    The VIM (ventral-intermediate) subnucleus is documented WITHIN this
    leaf, not as a child node (same convention as the LGN's six layers,
    the MGN's three divisions, the pulvinar's three subregions, the MD's
    three subdivisions, and the VA's subdivisions). The VIM is the
    cerebellar-receiving portion of the VL and is the principal DBS
    target for essential tremor and Parkinsonian tremor. Do not create
    a vim/ child node on the right either.

    See ../../../../left/ventral_nuclear_group/ventral_lateral_
    nucleus/__init__.py for the full anatomical description, the VIM
    subnucleus framing, the motor coordination functional role, the
    cerebello-thalamo-cortical loop, and the full clinical fact list.

    Reproduced distinctions (apply equally on the right):

    - VA vs. VL (motor-family trap): the right VA is the BASAL GANGLIA
      driver (right GPi/SNr → right VA → premotor/SMA/M1); the right VL
      is the CEREBELLAR driver (right dentate → right VL → right M1,
      with VIM). Different drivers; different cortical emphases; do not
      merge; driver split within the motor thalamus.

    - VA/VL vs. CM (cross-group motor relay vs. intralaminar motor;
      declared from the CM side and canonically from the VA side; this
      VL delta enforces it from the VL side): right VA/VL are
      FIRST-ORDER motor relays (motor cortex targets); the right CM
      (right/medial_nuclear_group/centromedian_nucleus/) is an
      INTRALAMINAR motor/arousal relay with striatal output; different
      relay types; different output targets; do not merge.

    - VL vs. VA (from the VA side): different drivers; different
      cortical emphasis (VA: premotor/SMA dominant; VL: M1 dominant,
      with VIM); do not merge.

    - VL vs. VPL/VPM (motor vs. somatosensory in the ventral group):
      right VL is a MOTOR relay; right VPL/VPM
      (right/ventral_nuclear_group/ventral_posterior_nucleus/) are
      SOMATOSENSORY relays. Different relay types; different cortical
      targets; do not merge.

    - VL vs. MD (motor vs. prefrontal): right VL is a MOTOR relay;
      right MD (right/medial_nuclear_group/medial_dorsal_nucleus/) is a
      PREFRONTAL relay. Different functional systems; do not merge.

Functional Mode:
    Same as ../../../../left/ventral_nuclear_group/ventral_lateral_
    nucleus/. Cerebellar motor relay (the anchor); motor coordination,
    timing, error correction; the VIM subnucleus's role in tremor
    generation and in tremor suppression by DBS. No documented
    functional asymmetry between left and right VL. Do not fabricate
    one.

    CLINICAL FACTS (apply on the right identically, with
    CONTRALATERAL specification):
        * RIGHT VIM DBS: established DBS target for essential tremor
          and Parkinsonian tremor. A right VIM DBS lead suppresses
          predominantly LEFT-sided tremor (contralateral effect); with
          bilateral VIM DBS, both sides' tremor is suppressed.
          Long-established standard of care.
        * RIGHT VL LESIONS: produce CONTRALATERAL (LEFT) MOTOR
          COORDINATION DEFICITS (ataxia, tremor, dysmetria on the LEFT
          side); right VL-specific syndromes are rare in isolation
          (right VL is supplied by the right PCA territory).
        * RIGHT VL IN CEREBELLO-THALAMO-CORTICAL STROKE: right PCA
          territory infarcts can involve the right VL and produce
          LEFT-side motor coordination deficits, often with other PCA
          territory deficits.
        * Right VIM is the predominant target for tremor on the right;
          the left VIM is the predominant target for tremor on the
          left. Both are standard-of-care DBS targets.

Hormonal Modulation:
    Same as ../../../../left/ventral_nuclear_group/ventral_lateral_
    nucleus/. Minimal; dopaminergic (right SNc → striatum → basal
    ganglia → VL indirect modulation); cholinergic (brainstem, basal
    forebrain); monoaminergic (brainstem) arousal inputs. Not a
    principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/ventral_nuclear_group/ventral_lateral_
    nucleus/. Reads procedural (motor coordination depends on learned
    motor skills); short_term (current motor state buffer). Writes
    nothing directly (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right VL fragment. The VL is a motor relay; the model prompt
    does not need a VL block because the motor coordination signals it
    relays are already represented in the upstream (right dentate) and
    downstream (right M1) fragments. Same deliberate absence as on the
    left.

Right-specific reciprocal connections to enforce in Stage 4:

    Cerebello-thalamo-cortical motor loop (the anchor):
    - ← cerebellum/.../deep cerebellar nuclei/right (right dentate →
      right VL; the principal cerebellar motor input to the VL; the
      VL's driver input; right-side; the dentate nucleus is
      midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/frontal/
      primary_motor_cortex (right VL → right M1; the VL's principal
      cortical output; with VIM as the DBS-target subregion).
    - → telencephalon/cerebral_hemispheres/right/cortex/frontal/
      premotor_cortex (right VL → right premotor cortex; less dense
      than the VL's M1 projection but present).
    - ← telencephalon/cerebral_hemispheres/right/cortex/frontal/
      primary_motor_cortex (right M1 → right VL; corticothalamic
      feedback; the motor cortex modulates VL relay gain).

    Distinction (not signaling; structural note):
    - ↔ ../ventral_anterior_nucleus/ (right VA; the BASAL GANGLIA motor
      relay; distinct driver and distinct cortical emphasis; do not
      merge; the VA/VL driver split).
    - ↔ ../../medial_nuclear_group/centromedian_nucleus/ (right CM;
      INTRALAMINAR motor/arousal relay; striatal output, not motor
      cortex; distinct relay type; do not merge).
    - ↔ ../ventral_posterior_nucleus/ (right VPL/VPM; SOMATOSENSORY
      relays; distinct relay types; do not merge).

    - ↔ ../../../../left/ventral_nuclear_group/ventral_lateral_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed; but see
      the CONTRALATERAL clinical facts — right VIM DBS suppresses
      predominantly LEFT-sided tremor; left VIM DBS suppresses
      predominantly RIGHT-sided tremor; bilateral VIM DBS suppresses
      both sides. The two VL leaves document their respective
      contralateral VIM DBS effects).

Notes:
    - Delta file of ../../../../left/ventral_nuclear_group/
      ventral_lateral_nucleus/. Not a full leaf. Do not duplicate.
    - THE VL PAIR IS NOW COMPLETE: with this file, the VL is fully
      documented on both hemispheres, with the VIM DBS tremor anchor
      and the contralateral tremor suppression correctly specified for
      each side (right VIM DBS → left-side predominant suppression;
      left VIM DBS → right-side predominant suppression).
    - THE MOTOR FAMILY OF THE VENTRAL GROUP IS NOW COMPLETE: with the
      VA pair (drafted) and the VL pair (drafted via this delta), the
      two motor relays of the ventral nuclear group are fully
      documented on both hemispheres.
    - THE VIM SUBNUCLEUS is documented WITHIN the left VL leaf, not as
      a child node. Same convention on the right: do not create a vim/
      child node here either.
    - THE VA vs. VL, VA/VL vs. CM, VL vs. VPL/VPM, and VL vs. MD
      distinctions are reproduced in abbreviated form; the full text is
      in ../../../../left/ventral_nuclear_group/ventral_lateral_
      nucleus/ and ../../__init__.py.
    - THE CONTRALATERAL CLINICAL FACTS apply on the right with the
      correct direction: right VIM DBS → LEFT-side tremor suppression
      (contralateral effect); right VL lesion → LEFT-side motor
      coordination deficits. The right and left VL leaves document the
      opposite directions explicitly; do not flatten.
    - THE VIM DBS ANCHOR IS ESTABLISHED (unlike the VA's
      investigational/secondary DBS). Same on the right as on the left.
    - NO FRAGMENT: same as the whole thalamus. The right VL is a relay,
      not a state-emitter.
    - The right VL is NOT the right VA (basal ganglia), NOT the right
      CM (intralaminar motor/arousal), NOT the right VPL/VPM
      (somatosensory), NOT the right MD (prefrontal). The traps make
      these distinctions explicit on the right.
    - Midline targets (dentate nucleus) are flagged with "verify" so
      Stage 4 does not force a hemisphere split on structures that are
      not hemisphere-split in the tree. Right M1, right premotor cortex,
      right VIM, right VA, right CM, right VPL/VPM, and right MD are
      hemisphere-split and require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/ventral_nuclear_group/ventral_lateral_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/ventral_nuclear_
      group/.
"""