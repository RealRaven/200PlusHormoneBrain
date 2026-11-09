"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.medial_nuclear_group.centromedian_nucleus
Anatomical Role:
    The left centromedian nucleus (CM). One of the three intralaminar
    thalamic nuclei, situated in the medial nuclear group of the left
    thalamus, adjacent to the left central lateral (CL) and
    parafascicular (Pf) nuclei. It is an INTRALAMINAR CORE-TYPE
    MOTOR/AROUSAL RELAY: a core-type thalamic nucleus
    (parvalbumin-positive, topographically projecting) whose driver
    input is from the basal ganglia (especially the globus pallidus
    internus and substantia nigra pars reticulata) and the brainstem
    reticular formation, and whose output is PRIMARILY TO THE STRIATUM
    (not just the cortex).

    The CM is the core-type counterpart of the CL's matrix type: the
    CL projects diffusely to the cortex; the CM projects topographically
    to the striatum (and to a lesser extent to the cortex). This is the
    key distinction within the intralaminar family — the CL and Pf are
    matrix-type (diffuse cortical), the CM is core-type (striatal).

    DISTINCTIONS (critical):

    - CM vs. CL (intra-intralaminar; the core-vs-matrix distinction):
      the CM is a CORE-TYPE motor/arousal relay with prominent
      STRIATAL projections; the CL is a MATRIX-TYPE arousal/attention
      relay with diffuse CORTICAL projections. Different projection
      patterns; different functional emphases; do not treat them as
      interchangeable intralaminar nuclei.

    - CM vs. PARAFASCICULAR (intra-intralaminar): the CM is
      core-type (striatal); the Pf is matrix-type (diffuse cortical,
      with nociceptive-adjacent and striatal-projecting components).
      The Pf projects more diffusely; the CM projects more
      topographically to the striatum. Different emphases; do not
      merge.

    - CM vs. VA/VL (a subtle trap; both motor-adjacent): the CM is an
      INTRALAMINAR motor/arousal relay (striatal driver and striatal
      output); the VA/VL (thalamus/left/ventral_nuclear_group/) are
      FIRST-ORDER motor relays (basal ganglia/cerebellum driver;
      premotor/motor cortex output). Both receive basal ganglia input
      and are motor-adjacent, but the CM projects back to the striatum
      (basal ganglia loop) while the VA/VL project to the motor
      cortex (cortical loop). Different relay types; do not merge.

    - CM vs. MEDIAL DORSAL NUCLEUS (MD; both "medial group," different
      families): the CM is an INTRALAMINAR motor/arousal relay; the MD
      (thalamus/left/medial_nuclear_group/medial_dorsal_nucleus/) is a
      PREFRONTAL relay. Different families within the medial nuclear
      group; different functions; do not merge.

    - CM vs. MIDLINE FAMILY: the CM is AROUSAL/MOTOR; the midline
      nuclei are LIMBIC/VISCERAL. Different families; do not merge.

Functional Mode:
    - Basal-ganglia-thalamo-cortical motor loop (the CM's anchor
      role):
        * The CM receives input from the basal ganglia output nuclei
          (GPi, SNr) — the same nuclei that project to the VA/VL motor
          thalamus — and projects BACK TO THE STRIATUM (the
          "thalamostriatal" projection), completing a
          basal-ganglia-thalamo-striatal loop.
        * The CM is therefore part of a RE-ENTRANT motor loop: it
          receives the basal ganglia's output and feeds it back into
          the striatum. This loop is distinct from the VA/VL's
          basal-ganglia-thalamo-cortical loop (which goes to the
          motor cortex, not back to the striatum).
        * The CM's motor role is therefore MODULATORY and RE-ENTRANT:
          it modulates the striatum's processing rather than driving
          the motor cortex directly.
    - Arousal and attention (the CM's second role):
        * The CM also receives brainstem reticular inputs and
          contributes to arousal and attention, alongside the CL and
          Pf. Its arousal role is less purely cortical than the CL's
          (because its output is more striatal), but it is real.
        * The CM's arousal contribution is part of the intralaminar
          family's collective role in sustaining consciousness.
    - Consciousness (the intralaminar family's shared role):
        * The CM is one of the intralaminar nuclei whose activity
          contributes to normal consciousness. Its bilateral
          destruction, like the CL's, contributes to the
          intralaminar-arousal deficit picture (see clinical fact).
    - The CM is therefore the INTRALAMINAR CORE-TYPE MOTOR/AROUSAL
      RELAY: its distinctive contribution is the
      basal-ganglia-thalamo-striatal re-entrant loop, which modulates
      striatal processing rather than driving the motor cortex.

    - CLINICAL FACTS (the CM's defining clinical anchors):
        * CENTROMEDIAN DBS FOR MOVEMENT DISORDERS: the CM is a DBS
          target for some movement disorders (particularly
          Tourette syndrome, where CM DBS has been used for
          treatment-refractory tics; also investigated for some
          dystonias and for essential tremor). The CM DBS is
          established as an option in specialized centers, though less
          widely used than STN or GPi DBS for Parkinson's.
        * CENTROMEDIAN DBS FOR DISORDERS OF CONSCIOUSNESS: the CM is
          one of the intralaminar DBS targets investigated for
          promoting arousal/recovery in patients with disorders of
          consciousness (minimally conscious state, vegetative
          state). This is investigational but active; the CM DBS
          literature for disorders of consciousness is one of the
          more established experimental uses of intralaminar DBS.
        * SEVERE BILATERAL INTRALAMINAR LESIONS (including bilateral
          CM lesions) produce COMA OR PERSISTENT VEGETATIVE STATE;
          the family-level fact is shared with the CL and Pf.
        * CM-SPECIFIC SYNDROMES are NOT established beyond the DBS
          indications: isolated CM lesions are rare, and CM-specific
          clinical syndromes are not described beyond the broader
          intralaminar picture and the CM DBS indications.

Hormonal Modulation (minimal; the CM is a motor/arousal relay):
    - The CM is NOT a neuroendocrine structure.
    - Modulators: cholinergic, monoaminergic, histaminergic, and
      orexinergic arousal inputs; basal ganglia (GABAergic) inputs
      from GPi/SNr; dopaminergic input from the SNc. Document as
      arousal and motor modulation, not endocrine modulators.
    - The CM is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * procedural: the CM's basal-ganglia-thalamo-striatal loop is
          part of the procedural/habit-learning circuit; it reads the
          procedural memory store (motor habits and sequences).
        * short_term: the current arousal/attention state buffer.
    - Writes: none directly. The CM is a RELAY: it modulates striatal
      processing; it does not store content.
    - The CM's memory interfaces are THICKER than the CL's on the
      procedural dimension (the CM is motor-circuit-adjacent) and
      THINNER on the arousal dimension (its arousal role is less
      purely cortical than the CL's).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No CM fragment. The CM is a motor/arousal relay; the model
      prompt does not need a centromedian-nucleus block because the
      motor and arousal signals it relays are already represented in
      the upstream (basal ganglia, brainstem reticular) and
      downstream (striatum, diffuse cortical activation) fragments.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The CM's clinical facts (DBS for Tourette's, disorders of
      consciousness; coma from bilateral lesions) are documented for
      completeness, but are not prompt fields.

Reciprocal Connections (left-side; the right side is in
../../../../right/medial_nuclear_group/centromedian_nucleus/):

    Basal-ganglia-thalamo-striatal loop (the CM's anchor):
    - ← telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      left (GPi → CM; GABAergic; basal ganglia output to the CM; the
      CM receives the same output that the VA/VL motor thalamus
      receives).
    - ← midbrain/tegmentum/substantia_nigra/left/pars_reticulata
      (SNr → CM; GABAergic; basal ganglia output to the CM).
    - → telencephalon/.../subcortical/basal_ganglia/striatum/left
      (CM → striatum; the thalamostriatal projection; the RE-ENTRANT
      loop's defining edge; the CM's principal output).
    - ← midbrain/tegmentum/substantia_nigra/left/pars_compacta (SNc
      dopamine; dopaminergic modulation of the CM's striatal loop;
      SNc reciprocates when drafted).

    Arousal (secondary):
    - ← brainstem/.../reticular_formation (reticular activating
      system input; the reticular formation is midline-adjacent —
      verify).
    - ← brainstem/.../laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (cholinergic arousal input; both
      midline-adjacent — verify).
    - ← brainstem/.../locus_coeruleus (noradrenergic arousal input;
      LC is midline-adjacent — verify).
    - ← brainstem/.../dorsal_raphe_nucleus (serotonergic arousal
      input; raphe is midline).
    - ← hypothalamus/tuber_cinereum/left/tuberomammillary_nucleus
      (histaminergic arousal input).
    - ← hypothalamus/anterior/lateral_area/left/
      anterior_part_of_lateral_nucleus (orexinergic arousal input).
    - → telencephalon/cerebral_hemispheres/left/cortex/* (modest
      cortical projections; less extensive than the CL's diffuse
      cortical matrix, but present; the CM's cortical output is
      secondary to its striatal output).

    Intra-intralaminar:
    - ↔ ../central_lateral_nucleus/ (left CL; matrix-type
      arousal/attention relay; diffuse cortical projections; different
      projection pattern from the CM's striatal projection; do not
      merge).
    - ↔ ../parafascicular_nucleus/ (left Pf; matrix-type
      arousal/nociceptive-adjacent relay; different emphasis from the
      CM; do not merge).

    Distinction (not signaling; structural note):
    - ↔ ../../ventral_nuclear_group/ventral_anterior_nucleus and
      ventral_lateral_nucleus (the CM and the VA/VL both receive basal
      ganglia output, but the CM projects BACK TO THE STRIATUM
      (re-entrant loop) while the VA/VL project TO THE MOTOR CORTEX
      (cortical loop); different relay types; do not merge).
    - ↔ ../midline_nuclear_group/ (the midline family is LIMBIC/
      VISCERAL; the CM is AROUSAL/MOTOR; different families; do not
      merge).

Notes:
    - Tier 1 full leaf (left). The second intralaminar nucleus to be
      drafted (after the CL); the CORE-TYPE counterpart to the CL's
      matrix type.
    - THE CM vs. CL TRAP (core-vs-matrix) is the intralaminar family's
      most important internal distinction: the CM projects to the
      striatum (core-type, topographic); the CL projects diffusely to
      the cortex (matrix-type). Different projection patterns;
      different functional emphases; do not merge.
    - THE CM vs. VA/VL TRAP is a NEW trap declared in this leaf: both
      receive basal ganglia output, but the CM projects BACK TO THE
      STRIATUM (re-entrant loop) and the VA/VL project TO THE MOTOR
      CORTEX (cortical loop). Different relay types; different output
      targets; do not merge. This trap is worth declaring explicitly
      because "both are motor-adjacent thalamic nuclei receiving basal
      ganglia input" is a surface similarity that hides a deep
      difference.
    - THE CM DBS CLINICAL FACTS are the CM's distinctive clinical
      anchor: (1) CM DBS for Tourette syndrome (treatment-refractory
      tics; established as an option in specialized centers) and some
      other movement disorders; (2) CM DBS for disorders of
      consciousness (investigational; active area). The CM's DBS
      literature is more developed than the CL's or Pf's, making the
      CM the intralaminar family's clinical anchor for the DBS
      applications.
    - THE COMA FACT (bilateral intralaminar lesion) is a family-level
      fact shared with the CL and Pf; the CM leaf documents it from
      the CM side, as the CL leaf did from the CL side.
    - CM-SPECIFIC SYNDROME HONESTY: isolated CM lesions are rare;
      CM-specific clinical syndromes are not established beyond the
      DBS indications. Document honestly.
    - NO FRAGMENT: same as the whole thalamus. The CM is a relay, not
      a state-emitter.
    - The CM's "striatal output" is a SPECIFIC edge (CM → striatum),
      unlike the CL's diffuse cortical matrix. This is the core-vs-
      matrix distinction in practice.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, histamine,
      orexin, dopamine, GABA, glutamate); memory/stores/ (procedural,
      short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/medial_nuclear_
      group/.
"""