"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.central_lateral_nucleus
Anatomical Role:
    The right central lateral nucleus (CL). One of the three
    intralaminar thalamic nuclei, situated in the medial nuclear group
    of the right thalamus, adjacent to the right centromedian and
    parafascicular nuclei. Same INTRALAMINAR AROUSAL/ATTENTION RELAY
    role as the left CL: a matrix-type thalamic nucleus
    (calbindin-positive, diffusely projecting) whose driver input is
    from the brainstem reticular formation and the basal ganglia, and
    whose output is DIFFUSE to the right cerebral cortex (particularly
    layer 1 of multiple right cortical areas).

    See ../../../../left/medial_nuclear_group/central_lateral_
    nucleus/__init__.py for the full anatomical description, the
    matrix-vs-core framing, the arousal/attention/consciousness role,
    the family-level coma clinical fact, the "no CL-specific syndrome"
    honesty, and the "diffuse cortical projections are not a single
    edge" discipline.

    Reproduced distinctions (apply equally on the right):
    - CL vs. MIDLINE FAMILY (primary intra-group trap): the right CL
      is an AROUSAL/ATTENTION relay (brainstem reticular + basal
      ganglia driver; diffuse cortical layer 1 projections). The right
      midline nuclei (paratenial, reuniens, rhomboidal, PVT;
      documented under right/medial_nuclear_group/midline_nuclear_
      group/) are LIMBIC/VISCERAL relays (hypothalamic and limbic
      driver). Both families are "diffuse" thalamic nuclei, but they
      are FUNCTIONALLY DISTINCT. Do not merge.
    - CL vs. CENTROMEDIAN (intra-intralaminar): the right CM is the
      core-type motor/arousal relay with prominent striatal
      projections; the right CL is the matrix-type arousal/attention
      relay with diffuse cortical layer 1 projections. Different
      projection patterns; do not merge.
    - CL vs. PARAFASCICULAR (intra-intralaminar): the right Pf is the
      matrix-type arousal/nociceptive-adjacent relay; the right CL is
      the matrix-type arousal/attention relay. Different emphases; do
      not merge.
    - CL vs. VA/VL (subtle): both receive basal ganglia input, but the
      right CL is an INTRALAMINAR arousal relay (diffuse cortical
      projections) and the right VA/VL
      (right/ventral_nuclear_group/) are FIRST-ORDER motor relays
      (premotor/motor cortex projections). Do not merge.

Functional Mode:
    Same as ../../../../left/medial_nuclear_group/central_lateral_
    nucleus/. Arousal and attention (the anchor); consciousness (the
    family's most significant functional contribution); striatal and
    motor-adjacent contributions (secondary). No documented functional
    asymmetry between left and right CL. Do not fabricate one.

    CLINICAL FACT (family-level; applies on the right):
        * SEVERE BILATERAL INTRALAMINAR LESIONS (left + right CL, CM,
          Pf collectively) produce COMA OR PERSISTENT VEGETATIVE
          STATE. Bilateral — not right-sided alone — is required for
          the most severe picture; the right CL lesion contributes to
          the right-sided component of the arousal deficit.
        * CL-SPECIFIC SYNDROMES are NOT established on the right
          either: isolated right CL lesions are rare, and right
          CL-specific clinical syndromes are not described beyond the
          broader intralaminar-arousal picture.
        * CL DBS for disorders of consciousness is investigational on
          the right as on the left.

Hormonal Modulation:
    Same as ../../../../left/medial_nuclear_group/central_lateral_
    nucleus/. Minimal; the ascending arousal systems (cholinergic,
    monoaminergic, histaminergic, orexinergic) modulate the right CL's
    diffuse cortical projections. Not a principal target of the 12
    endocrine axes.

Memory Interfaces:
    Same as ../../../../left/medial_nuclear_group/central_lateral_
    nucleus/. Reads short_term (arousal/attention state buffer).
    Writes nothing directly (relay, not encoder). Thin memory
    interface; no episodic, semantic, procedural, or
    reinforcement_value_based_learning read.

Model Integration (Gemma-4-E2B):
    No right CL fragment. Same as ../../../../left/medial_nuclear_
    group/central_lateral_nucleus/ and the whole thalamus: the CL is
    an arousal/attention relay, not a state-emitter. The
    model-relevant arousal state is carried by the upstream arousal
    fragments (LPO, TMN, LC, raphe, orexin).

Right-specific reciprocal connections to enforce in Stage 4:

    Arousal/attention (the anchor):
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
    - → telencephalon/cerebral_hemispheres/right/cortex/* (diffuse
      right-cortical layer 1 projections; matrix-type projection to
      multiple right cortical areas; NO SINGLE cortical target — the
      diffuse projection is the CL's defining output).

    Striatal and motor-adjacent (secondary):
    - ↔ telencephalon/.../subcortical/basal_ganglia/striatum/right
      (basal ganglia input and striatal projection; right-side).
    - ↔ brainstem/.../superior_colliculus (midbrain visual-motor
      input; the superior colliculus is midline-adjacent — verify).

    Intra-intralaminar:
    - ↔ ../centromedian_nucleus/ (right CM; core-type motor/arousal
      relay; different projections; do not merge).
    - ↔ ../parafascicular_nucleus/ (right Pf; matrix-type arousal/
      nociceptive-adjacent relay; distinct from CL; do not merge).

    Distinction (not signaling; structural note):
    - ↔ ../midline_nuclear_group/ (right midline family is
      LIMBIC/VISCERAL; the right CL is AROUSAL/ATTENTION; different
      families; do not merge).

    - ↔ ../../../../left/medial_nuclear_group/central_lateral_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/medial_nuclear_group/
      central_lateral_nucleus/. Not a full leaf. Do not duplicate.
    - THE CL vs. MIDLINE TRAP is reproduced in abbreviated form; the
      full text is in ../../../../left/medial_nuclear_group/
      central_lateral_nucleus/ and ../../../__init__.py. A
      contributor entering at the right CL must see it.
    - THE CL vs. CM and CL vs. Pf distinctions are reproduced: all
      three are intralaminar, but the right CL is the matrix-type
      arousal/attention relay, the right CM is the core-type
      motor/arousal relay, and the right Pf is the matrix-type
      arousal/nociceptive-adjacent relay. Different projection
      patterns; do not merge.
    - THE CL vs. VA/VL distinction is reproduced: both receive basal
      ganglia input, but the right CL is an INTRALAMINAR arousal
      relay and the right VA/VL are FIRST-ORDER motor relays. Do not
      merge.
    - DIFFUSE CORTICAL PROJECTIONS: the right CL's output is a
      matrix-type projection to multiple right cortical areas
      (particularly layer 1), NOT a single cortical edge. Do not name
      a single right-cortical target; the diffuse projection is the
      CL's defining output on the right as well.
    - THE CLINICAL FACT (bilateral intralaminar lesion → coma) is a
      family-level fact that requires BILATERAL involvement; the
      right CL lesion contributes the right-sided component. Document
      honestly; do not claim a right-CL-specific coma syndrome.
    - CL-SPECIFIC SYNDROME HONESTY: isolated right CL lesions are
      rare; right-CL-specific syndromes are not established.
    - NO FRAGMENT: same as the whole thalamus. The right CL is a
      relay, not a state-emitter.
    - Midline targets (reticular formation, LDT/PPN, LC, raphe,
      superior colliculus) are flagged with "verify" so Stage 4 does
      not force a hemisphere split on structures that are not
      hemisphere-split in the tree. Right TMN, right LHA orexin, right
      striatum, right diffuse cortical projections, right CL/CM/Pf
      intra-group edges, and right midline family are hemisphere-split
      and require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/medial_nuclear_group/central_lateral_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""