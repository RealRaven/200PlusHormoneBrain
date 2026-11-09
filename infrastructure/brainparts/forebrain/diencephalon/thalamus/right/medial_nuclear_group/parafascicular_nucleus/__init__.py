"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.parafascicular_nucleus
Anatomical Role:
    The right parafascicular nucleus (Pf). One of the three intralaminar
    thalamic nuclei, situated in the medial nuclear group of the right
    thalamus, adjacent to the right centromedian (CM) and central
    lateral (CL) nuclei, in the caudal intralaminar region. Same
    INTRALAMINAR AROUSAL/ATTENTION/NOCICEPTIVE-ADJACENT relay role as
    the left Pf: a matrix-type thalamic nucleus with diffuse cortical
    projections, a striatal-projecting component, and a distinctive
    nociceptive-adjacent input from the right spinothalamic and
    trigeminothalamic pathways.

    See ../../../../left/medial_nuclear_group/parafascicular_nucleus/
    __init__.py for the full anatomical description, the "matrix +
    nociception + striatum" hybrid framing, the affective/motivational
    dimension of pain role, the Pf-specific syndrome honesty, and the
    Pf DBS investigational framing.

    Reproduced distinctions (apply equally on the right):
    - Pf vs. CL (intra-intralaminar): both are matrix-type with diffuse
      cortical projections; the right Pf adds nociceptive-adjacent
      input and a striatal component. Do not merge.
    - Pf vs. CM (intra-intralaminar): both have striatal-projecting
      components; the right Pf is matrix-type (diffuse cortical
      dominant), the right CM is core-type (topographic striatal
      dominant). Different emphases; do not merge.
    - Pf vs. MIDLINE FAMILY: the right Pf is an AROUSAL/ATTENTION/
      NOCICEPTIVE-ADJACENT relay; the right midline nuclei
      (right/medial_nuclear_group/midline_nuclear_group/) are LIMBIC/
      VISCERAL relays. Both are "diffuse"; functionally distinct; do
      not merge.
    - Pf vs. MD: the right Pf is INTRALAMINAR (arousal/nociceptive-
      adjacent); the right MD is PREFRONTAL relay. Different families;
      do not merge.
    - Pf vs. VPL/VPM (the nociceptive-adjacent trap, new): both receive
      right spinothalamic nociceptive input, but the right Pf's role is
      AFFECTIVE/MOTIVATIONAL (arousal, attention, emotional response
      to pain; right anterior cingulate and right insula targets)
      while the right VPL/VPM's role is SENSORY-DISCRIMINATIVE
      (location, intensity, quality; right S1 target). Different relay
      types; different roles in pain; do not merge.

Functional Mode:
    Same as ../../../../left/medial_nuclear_group/parafascicular_
    nucleus/. Arousal and attention (the anchor; shared with the CL);
    nociceptive-adjacent processing (the distinctive
    affective/motivational dimension of pain); consciousness
    (family-level); striatal and motor-adjacent contributions
    (secondary). No documented functional asymmetry between left and
    right Pf. Do not fabricate one.

    CLINICAL FACTS (apply on the right identically):
        * SEVERE BILATERAL INTRALAMINAR LESIONS produce coma or
          persistent vegetative state; the right Pf lesion contributes
          the right-sided component. BILATERAL is required for the full
          picture; document honestly.
        * PF-SPECIFIC SYNDROMES are NOT established on the right
          either: isolated right Pf lesions are rare, and right
          Pf-specific clinical syndromes are not described beyond the
          broader intralaminar picture.
        * PF DBS is INVESTIGATIONAL on the right as on the left; the
          right Pf DBS literature is THINNER than the right CM DBS
          literature. Document as investigational; do not treat the
          right Pf as equivalent to the right CM for DBS.

Hormonal Modulation:
    Same as ../../../../left/medial_nuclear_group/parafascicular_
    nucleus/. Minimal; cholinergic, monoaminergic, histaminergic,
    orexinergic arousal inputs; right spinothalamic/trigeminothalamic
    nociceptive inputs; basal ganglia (GABAergic) inputs from the right
    GPi/SNr. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../../../left/medial_nuclear_group/parafascicular_
    nucleus/. Reads short_term (arousal/attention state buffer and
    nociceptive-affective state buffer). Writes nothing directly
    (relay, not encoder). Thin memory interface; no episodic, semantic,
    procedural, or reinforcement_value_based_learning read.

Model Integration (Gemma-4-E2B):
    No right Pf fragment. The Pf is an arousal/nociceptive-adjacent
    relay; the model prompt does not need a parafascicular-nucleus
    block. The arousal and nociceptive-affective signals it relays are
    already represented in the upstream (right brainstem reticular,
    right spinothalamic/trigeminothalamic) and downstream (right
    diffuse cortical activation, right striatum, right anterior
    cingulate, right insula) fragments.

Right-specific reciprocal connections to enforce in Stage 4:

    Arousal/attention (the anchor; shared with the CL):
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
      right-cortical layer 1 projections; matrix-type; no single
      cortical target).

    Nociceptive-adjacent (the Pf's distinctive input):
    - ← spinal_cord/gray_matter/right/dorsal_horn and the right
      spinothalamic tract (spinothalamic nociceptive input; the dorsal
      horn and spinothalamic tract are midline-adjacent — verify).
    - ← brainstem/.../trigeminal_nuclei (trigeminothalamic nociceptive
      input; the trigeminal nuclei are midline-adjacent — verify).
    - → telencephalon/cerebral_hemispheres/right/cortex/cingulate/
      anterior_cingulate and telencephalon/.../cortex/insular/*
      (right nociceptive-affective cortical targets; the
      arousal/attention component of pain affect; right-side).

    Striatal and motor-adjacent (secondary; shared with the CM):
    - ↔ telencephalon/.../subcortical/basal_ganglia/striatum/right
      (basal ganglia input and striatal projection; right-side).
    - ↔ telencephalon/.../subcortical/basal_ganglia/globus_pallidus/
      right (GPi → Pf; GABAergic; right-side).

    Intra-intralaminar:
    - ↔ ../central_lateral_nucleus/ (right CL; matrix-type
      arousal/attention; distinct from Pf; do not merge).
    - ↔ ../centromedian_nucleus/ (right CM; core-type motor/arousal;
      both have striatal components but different emphases; do not
      merge).

    Distinction (not signaling; structural note):
    - ↔ ../../ventral_nuclear_group/ventral_posterior_nucleus (the
      right Pf is AFFECTIVE/MOTIVATIONAL for pain; the right VPL/VPM
      is SENSORY-DISCRIMINATIVE; different relay types; do not merge).
    - ↔ ../midline_nuclear_group/ (right midline family is LIMBIC/
      VISCERAL; the right Pf is AROUSAL/ATTENTION/NOCICEPTIVE-
      ADJACENT; different families; do not merge).

    - ↔ ../../../../left/medial_nuclear_group/parafascicular_nucleus/
      (hemisphere counterpart; no functional asymmetry assumed).

Notes:
    - Delta file of ../../../../left/medial_nuclear_group/
      parafascicular_nucleus/. Not a full leaf. Do not duplicate.
    - THE INTRALAMINAR FAMILY IS NOW COMPLETE — BOTH HEMISPHERES: with
      this file, the entire intralaminar family is fully documented:
        * CL pair (left leaf + right delta).
        * CM pair (left leaf + right delta).
        * Pf pair (left leaf + right delta; this file).
        * Intralaminar sub-container pair (left sub-container + right
          sub-container delta).
      8 files, all complete.
    - THE INTRA-INTRALAMINAR DISTINCTIONS are reproduced: Pf vs. CL
      (both matrix; Pf adds nociception + striatum); Pf vs. CM (both
      have striatal components; Pf is matrix; CM is core).
    - THE PF vs. VPL/VPM NOCICEPTIVE-ADJACENT TRAP is reproduced in
      abbreviated form (new, declared in the left Pf leaf): the right
      Pf is AFFECTIVE/MOTIVATIONAL for pain; the right VPL/VPM is
      SENSORY-DISCRIMINATIVE. Different roles in pain; do not merge.
    - THE PF vs. MIDLINE FAMILY TRAP is reproduced in abbreviated form.
    - THE COMA FACT (bilateral intralaminar lesion) is a family-level
      fact; the right Pf lesion contributes the right-sided component;
      BILATERAL is required for the full picture.
    - PF-SPECIFIC SYNDROME HONESTY and PF DBS HONESTY apply on the
      right identically: no right-Pf-specific syndrome; right Pf DBS
      is investigational and thinner than the right CM DBS literature.
    - NO FRAGMENT: same as the whole thalamus. The right Pf is a
      relay, not a state-emitter.
    - The right Pf's "diffuse cortical projections" are NOT a single
      cortical edge; the nociceptive-affective projections to the
      right anterior cingulate and right insula are SPECIFIC enough
      to name, but the diffuse cortical matrix is not.
    - Midline targets (reticular formation, LDT/PPN, LC, raphe,
      trigeminal nuclei, spinothalamic tract) are flagged with
      "verify" so Stage 4 does not force a hemisphere split on
      structures that are not hemisphere-split in the tree. Right TMN,
      right orexin, right diffuse cortical projections, right
      spinothalamic/trigeminal, right anterior cingulate, right insula,
      right striatum, right GPi, right CL/CM intra-group edges, right
      midline family, and right VPL/VPM are hemisphere-split and
      require right-side targets explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../../../left/medial_nuclear_group/parafascicular_nucleus/
      § Notes for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""