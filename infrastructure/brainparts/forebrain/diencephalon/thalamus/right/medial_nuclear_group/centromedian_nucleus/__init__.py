"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.centromedian_nucleus
Anatomical Role:
    The right centromedian nucleus (CM). One of the three intralaminar
    thalamic nuclei, situated in the medial nuclear group of the right
    thalamus, adjacent to the right central lateral (CL) and
    parafascicular (Pf) nuclei. Same INTRALAMINAR CORE-TYPE
    MOTOR/AROUSAL RELAY role as the left CM: a core-type thalamic
    nucleus whose driver input is from the basal ganglia (especially
    the right globus pallidus internus and right substantia nigra pars
    reticulata) and the brainstem reticular formation, and whose output
    is PRIMARILY TO THE RIGHT STRIATUM (not just the cortex).

    See ../../../../left/medial_nuclear_group/centromedian_nucleus/
    __init__.py for the full anatomical description, the
    core-vs-matrix framing, the basal-ganglia-thalamo-striatal re-entrant
    loop framing, the CM DBS clinical facts, and the "CM-specific
    syndrome honesty" stance.

    Reproduced distinctions (apply equally on the right):
    - CM vs. CL (core-vs-matrix; the intralaminar family's most
      important internal distinction): the right CM is a CORE-TYPE
      motor/arousal relay with prominent STRIATAL projections; the
      right CL is a MATRIX-TYPE arousal/attention relay with diffuse
      CORTICAL projections. Different projection patterns; do not
      treat as interchangeable.
    - CM vs. PARAFASCICULAR: the right CM is core-type (striatal); the
      right Pf is matrix-type (diffuse cortical, with
      nociceptive-adjacent and striatal-projecting components).
      Different emphases; do not merge.
    - CM vs. VA/VL (subtle; both motor-adjacent): the right CM is an
      INTRALAMINAR motor/arousal relay that projects BACK TO THE
      STRIATUM (re-entrant loop); the right VA/VL
      (right/ventral_nuclear_group/) are FIRST-ORDER motor relays that
      project TO THE MOTOR CORTEX (cortical loop). Different relay
      types; different output targets; do not merge.
    - CM vs. MEDIAL DORSAL NUCLEUS (MD): the right CM is an
      INTRALAMINAR motor/arousal relay; the right MD
      (right/medial_nuclear_group/medial_dorsal_nucleus/) is a
      PREFRONTAL relay. Different families; do not merge.
    - CM vs. MIDLINE FAMILY: the right CM is AROUSAL/MOTOR; the right
      midline nuclei are LIMBIC/VISCERAL. Different families; do not
      merge.

Functional Mode:
    Same as ../../../../left/medial_nuclear_group/centromedian_
    nucleus/. Basal-ganglia-thalamo-striatal re-entrant loop (the
    anchor); arousal and attention (secondary); consciousness
    (family-level). No documented functional asymmetry between left
    and right CM. Do not fabricate one.

    CLINICAL FACTS (apply on the right identically):
        * CM DBS FOR MOVEMENT DISORDERS: the right CM is a DBS target
          for some movement disorders (particularly Tourette syndrome;
          also investigated for some dystonias and essential tremor).
          Same established-but-specialized status as on the left.
        * CM DBS FOR DISORDERS OF CONSCIOUSNESS: the right CM is one
          of the intralaminar DBS targets investigated for promoting
          arousal/recovery in disorders of consciousness. Investigational
          but active; same status as on the left.
        * SEVERE BILATERAL INTRALAMINAR LESIONS produce coma or
          persistent vegetative state; the right CM lesion contributes
          the right-sided component. BILATERAL is required for the
          full picture; document the family-level scope honestly.
        * CM-SPECIFIC SYNDROMES are NOT established beyond the DBS
          indications on the right either.

Hormonal Modulation:
    Same as ../../../../left/medial_nuclear_group/centromedian_
    nucleus/. Minimal; cholinergic, monoaminergic, histaminergic,
    orexinergic arousal inputs; basal ganglia GABAergic inputs from
    the right GPi/SNr; dopaminergic input from the right SNc. Not a
    principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/medial_nuclear_group/centromedian_
    nucleus/. Reads procedural (the right
    basal-ganglia-thalamo-striatal loop's procedural memory) and
    short_term (arousal/attention state). Writes nothing directly
    (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right CM fragment. The CM is a motor/arousal relay; the model
    prompt does not need a centromedian-nucleus block. The motor and
    arousal signals it relays are already represented in the upstream
    (right basal ganglia, brainstem reticular) and downstream (right
    striatum, diffuse cortical activation) fragments.

Right-specific reciprocal connections to enforce in Stage 4:

    Basal-ganglia-thalamo-striatal loop (the CM's anchor):
    - ← telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      right (GPi → CM; GABAergic; right-side).
    - ← midbrain/tegmentum/substantia_nigra/right/pars_reticulata
      (SNr → CM; GABAergic; right-side).
    - → telencephalon/.../subcortical/basal_ganglia/striatum/right
      (CM → striatum; the thalamostriatal projection; the RE-ENTRANT
      loop's defining edge; the CM's principal output; right-side).
    - ← midbrain/tegmentum/substantia_nigra/right/pars_compacta (SNc
      dopamine; dopaminergic modulation of the CM's striatal loop;
      right-side; SNc reciprocates when drafted).

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
    - ← hypothalamus/tuber_cinereum/right/tuberomammillary_nucleus
      (histaminergic arousal input; right-side).
    - ← hypothalamus/anterior/lateral_area/right/
      anterior_part_of_lateral_nucleus (orexinergic arousal input;
      right-side).
    - → telencephalon/cerebral_hemispheres/right/cortex/* (modest
      right-cortical projections; less extensive than the right CL's
      diffuse cortical matrix; secondary to the CM's striatal output).

    Intra-intralaminar:
    - ↔ ../central_lateral_nucleus/ (right CL; matrix-type
      arousal/attention; diffuse cortical projections; do not merge).
    - ↔ ../parafascicular_nucleus/ (right Pf; matrix-type
      arousal/nociceptive-adjacent; different emphasis; do not merge).

    Distinction (not signaling; structural note):
    - ↔ ../../ventral_nuclear_group/ventral_anterior_nucleus and
      ventral_lateral_nucleus (the right CM projects BACK TO THE
      STRIATUM; the right VA/VL project TO THE MOTOR CORTEX; different
      relay types; do not merge).
    - ↔ ../midline_nuclear_group/ (right midline family is LIMBIC/
      VISCERAL; the right CM is AROUSAL/MOTOR; different families; do
      not merge).

    - ↔ ../../../../left/medial_nuclear_group/centromedian_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/medial_nuclear_group/
      centromedian_nucleus/. Not a full leaf. Do not duplicate.
    - THE CM PAIR IS NOW COMPLETE: with this file, the centromedian
      nucleus is fully documented on both hemispheres — the
      intralaminar family's DBS anchor is done.
    - THE CM vs. CL (core-vs-matrix) TRAP is reproduced in abbreviated
      form; the full text is in
      ../../../../left/medial_nuclear_group/centromedian_nucleus/ and
      ../../../__init__.py. A contributor entering at the right CM
      must see it.
    - THE CM vs. VA/VL TRAP (new, declared in the left CM leaf) is
      reproduced in abbreviated form: the right CM projects BACK TO
      THE STRIATUM; the right VA/VL project TO THE MOTOR CORTEX.
      Different relay types; different output targets.
    - THE CM DBS CLINICAL FACTS (Tourette's established; disorders of
      consciousness investigational) apply on the right identically.
      The right CM's DBS literature is part of the same specialized-
      center body of evidence as the left CM's.
    - THE COMA FACT (bilateral intralaminar lesion) is a family-level
      fact; the right CM lesion contributes the right-sided component;
      BILATERAL is required for the full picture. Document honestly.
    - CM-SPECIFIC SYNDROME HONESTY: isolated right CM lesions are rare;
      right-CM-specific syndromes are not established beyond the DBS
      indications.
    - NO FRAGMENT: same as the whole thalamus. The right CM is a relay,
      not a state-emitter.
    - The right CM's "striatal output" is a SPECIFIC edge (right CM →
      right striatum), unlike the right CL's diffuse cortical matrix.
      The core-vs-matrix distinction is documented on the right as on
      the left.
    - Midline targets (reticular formation, LDT/PPN, LC, raphe) are
      flagged with "verify" so Stage 4 does not force a hemisphere
      split on structures that are not hemisphere-split in the tree.
      Right GPi, right SNr, right striatum, right SNc, right TMN,
      right orexin, right diffuse cortical projections, right CL/Pf
      intra-group edges, and right midline family are hemisphere-split
      and require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/medial_nuclear_group/centromedian_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""