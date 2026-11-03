"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.medial_nuclear_group.central_lateral_nucleus
Anatomical Role:
    The left central lateral nucleus (CL). One of the three
    intralaminar thalamic nuclei, situated in the medial nuclear group
    of the left thalamus, adjacent to the left centromedian and
    parafascicular nuclei. It is an INTRALAMINAR AROUSAL/ATTENTION
    RELAY: a matrix-type thalamic nucleus (calbindin-positive,
    diffusely projecting) whose driver input is from the brainstem
    reticular formation and the basal ganglia, and whose output is
    DIFFUSE to the cerebral cortex (particularly layer 1 of multiple
    cortical areas).

    The CL is one of the three intralaminar nuclei (the other two
    being the centromedian and the parafascicular), and one of the
    two diffuse-projecting "matrix" thalamic nuclei (the other being
    the parafascicular, with the centromedian being more
    core-type/projecting to the striatum). The CL's matrix
    projections to cortical layer 1 are the anatomical basis of its
    arousal/attention role.

    DISTINCTIONS (critical):

    - CL vs. MIDLINE FAMILY (the primary intra-group trap): the CL
      is an AROUSAL/ATTENTION relay (brainstem reticular + basal
      ganglia driver; diffuse cortical projections). The midline
      nuclei (paratenial, reuniens, rhomboidal, PVT; documented in
      the midline_nuclear_group/) are LIMBIC/VISCERAL relays
      (hypothalamic and limbic driver; hippocampal/amygdala/accumbens
      projections). Both families are "diffuse" thalamic nuclei, but
      they are FUNCTIONALLY DISTINCT. Do not merge the CL with the
      midline family.

    - CL vs. CENTROMEDIAN (intra-intralaminar distinction): both are
      intralaminar nuclei; the CL is a MATRIX-type arousal/attention
      relay with diffuse cortical layer 1 projections; the
      CENTROMEDIAN is a CORE-type motor/arousal relay with prominent
      projections to the striatum. Different projection patterns;
      different functional emphases; do not treat them as
      interchangeable intralaminar nuclei.

    - CL vs. PARAFASCICULAR (intra-intralaminar distinction): both
      are matrix-type intralaminar nuclei; the CL is more purely
      arousal/attention; the PARAFASCICULAR has additional
      nociceptive-adjacent and striatal-projecting components
      (overlapping with the centromedian). Different functional
      emphases; do not merge.

    - CL vs. VENTRAL NUCLEAR GROUP (a subtle trap): the CL is an
      INTRALAMINAR arousal relay (brainstem reticular + basal ganglia
      driver); the VA/VL (thalamus/left/ventral_nuclear_group/) are
      FIRST-ORDER motor relays (basal ganglia/cerebellum driver;
      premotor and motor cortex projections). Both receive basal
      ganglia input, but the CL's role is arousal/attention, not
      motor relay. Do not merge.

Functional Mode:
    - Arousal and attention (the CL's anchor role):
        * The CL receives brainstem reticular activating system
          inputs and basal ganglia inputs, and projects diffusely to
          cortical layer 1. This is the anatomical basis of its
          arousal/attention role.
        * The CL contributes to CORTICAL ACTIVATION — the diffuse
          cortical excitation that underlies wakefulness and
          consciousness. It is one of the nodes that translates
          brainstem arousal into cortical activation.
        * The CL contributes to ATTENTION — particularly to
          attentional gating and to the transition between different
          states of arousal (e.g., the sleep-wake transition). Its
          matrix projections to cortical layer 1 are thought to
          modulate the gain of cortical processing in a
          state-dependent manner.
    - Consciousness (the CL's most significant functional
      contribution):
        * The CL is one of the thalamic nuclei whose activity is
          REQUIRED for normal consciousness. The intralaminar system
          (CL, centromedian, parafascicular) is the thalamic
          component of the ascending arousal system; its
          bilateral destruction produces severe impairment of
          consciousness (see clinical fact).
        * The CL's matrix projections to cortical layer 1 are the
          anatomical basis of the "thalamocortical loop" that
          sustains consciousness; the intralaminar nuclei are
          sometimes described as the "thalamic reticular activating
          system" (though this term overlaps with the brainstem
          reticular formation).
    - Striatal and motor-adjacent contributions (secondary): the CL
      also projects to the striatum (alongside the centromedian), and
      contributes to the basal-ganglia-thalamo-cortical loop.
      Secondary to the arousal/attention role.
    - The CL is therefore the INTRALAMINAR AROUSAL/ATTENTION RELAY:
      its position in the ascending arousal system is one of the
      thalamic components that sustain consciousness.

    - CLINICAL FACT (the CL's defining clinical anchor):
        * SEVERE BILATERAL INTRALAMINAR LESIONS (including bilateral
          CL lesions) produce COMA OR PERSISTENT VEGETATIVE STATE:
          the intralaminar system is the thalamic component of the
          ascending arousal system, and its bilateral destruction
          produces the same picture as severe brainstem reticular
          lesions. This is the intralaminar family's defining clinical
          fact (shared with the centromedian and parafascicular).
        * CL-SPECIFIC SYNDROMES are NOT established: isolated CL
          lesions are rare, and CL-specific clinical syndromes are not
          described beyond the broader intralaminar-arousal picture.
          Document honestly; do not claim a CL-specific syndrome that
          the literature does not establish.
        * The CL is also a research target in DEEP BRAIN STIMULATION
          FOR DISORDERS OF CONSCIOUSNESS (alongside the centromedian);
          the experimental use of intralaminar DBS to promote
          arousal/recovery in patients with disorders of consciousness
          is investigational but active.

Hormonal Modulation (minimal; the CL is an arousal/attention relay):
    - The CL is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain; pedunculopontine/
      laterodorsal tegmental), monoaminergic (brainstem LC, raphe),
      histaminergic (TMN), and orexinergic (LHA) inputs are the
      ascending arousal systems that modulate the CL's diffuse
      cortical projections. Document as arousal modulation, not
      endocrine modulators.
    - The CL is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * short_term: the current arousal/attention state buffer (the
          CL's diffuse cortical projections are gated by the current
          arousal state).
    - Writes: none directly. The CL is a RELAY: it transmits arousal
      and attention signals to the cortex; it does not store content.
    - The CL's memory interface is THIN (short_term only): it does
      not read episodic, semantic, procedural, or reinforcement
      memory. It gates attention, not memory content.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No CL fragment. The CL is an arousal/attention relay; the model
      prompt does not need a central-lateral-nucleus block because
      the arousal/attention signals it relays are already represented
      in the upstream (brainstem reticular, basal ganglia) and
      downstream (diffuse cortical activation) fragments. The
      arousal/thermoregulatory fragments (from LPO, TMN, LC, raphe,
      orexin) carry the model-relevant arousal state; the CL is
      downstream modulation, not an independent state.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The CL's clinical facts (coma from bilateral lesions;
      investigational DBS for disorders of consciousness) are
      documented for completeness, but are not prompt fields.

Reciprocal Connections (left-side; the right side is in
../../../../right/medial_nuclear_group/central_lateral_nucleus/):

    Arousal/attention (the anchor):
    - ← brainstem/.../reticular_formation (reticular activating
      system input; the CL's primary arousal driver; the reticular
      formation is midline-adjacent — verify).
    - ← brainstem/.../laterodorsal_tegmental_nucleus and
      pedunculopontine_nucleus (cholinergic arousal input; both
      midline-adjacent — verify).
    - ← brainstem/.../locus_coeruleus (noradrenergic arousal input;
      LC is midline-adjacent — verify).
    - ← brainstem/.../dorsal_raphe_nucleus (serotonergic arousal
      input; raphe is midline).
    - ← hypothalamus/tuber_cinereum/left/tuberomammillary_nucleus
      (histaminergic arousal input; the TMN projects to the
      intralaminar nuclei).
    - ← hypothalamus/anterior/lateral_area/left/
      anterior_part_of_lateral_nucleus (orexinergic arousal input;
      the LHA orexin neurons project to the intralaminar nuclei).
    - → telencephalon/cerebral_hemispheres/left/cortex/* (diffuse
      cortical layer 1 projections; the CL's arousal/attention
      output; no single cortical target — it is a matrix-type
      projection to many cortical areas).

    Striatal and motor-adjacent (secondary):
    - ↔ telencephalon/.../subcortical/basal_ganglia/striatum/left
      (basal ganglia input and striatal projection; the CL's
      striatal-adjacent role; secondary to arousal/attention).
    - ↔ brainstem/.../superior_colliculus (midbrain visual-motor
      input; the CL also receives collicular input as part of its
      arousal-orienting role; the superior colliculus is
      midline-adjacent — verify).

    Intra-intralaminar:
    - ↔ ../centromedian_nucleus/ (adjacent intralaminar nucleus;
      CM is the core-type motor/arousal relay; CL is the matrix-type
      arousal/attention relay; different projections; do not merge).
    - ↔ ../parafascicular_nucleus/ (adjacent intralaminar nucleus;
      Pf is the matrix-type arousal/nociceptive-adjacent relay;
      distinct from CL; do not merge).

    Distinction (not signaling; structural note):
    - ↔ ../midline_nuclear_group/ (the midline family is the LIMBIC/
      VISCERAL relay family; the CL is the AROUSAL/ATTENTION relay;
      different families; do not merge).

Notes:
    - Tier 1 full leaf (left). The first intralaminar nucleus to be
      drafted; a Tier 1 hub of the arousal/attention family.
    - THE CL vs. MIDLINE TRAP is the group's most important
      intra-group trap for this leaf: both are "diffuse" thalamic
      nuclei, but the CL is AROUSAL/ATTENTION (brainstem reticular +
      basal ganglia driver) and the midline family is LIMBIC/
      VISCERAL (hypothalamic + limbic driver). Different functions;
      do not merge. The group container declares this trap; the CL
      leaf enforces it from the CL side.
    - THE CL vs. CENTROMEDIAN and CL vs. PARAFASCICULAR distinctions
      are reproduced: all three are intralaminar, but the CL is the
      matrix-type arousal/attention relay, the CM is the core-type
      motor/arousal relay (with prominent striatal projections), and
      the Pf is the matrix-type arousal/nociceptive-adjacent relay.
      Different projection patterns; different emphases; do not
      merge.
    - THE CL vs. VA/VL distinction is reproduced: both receive basal
      ganglia input, but the CL is an INTRALAMINAR arousal relay
      (diffuse cortical projections) and the VA/VL are FIRST-ORDER
      motor relays (premotor/motor cortex projections). Do not merge.
    - THE CLINICAL FACT (bilateral intralaminar lesion → coma/
      vegetative state) is the intralaminar family's shared
      clinical anchor. The CL leaf documents the family-level fact;
      the CM and Pf leaves will document the same fact from their
      side.
    - CL-SPECIFIC SYNDROME HONESTY: isolated CL lesions are rare;
      CL-specific syndromes are not established beyond the broader
      intralaminar picture. Do not claim a CL-specific syndrome.
    - NO FRAGMENT: same as the whole thalamus. The CL is a relay, not
      a state-emitter. The arousal state is carried by the upstream
      arousal fragments (LC, raphe, TMN, orexin, LPO).
    - The CL's "diffuse cortical projections" are NOT a single
      cortical edge: they are a matrix-type projection to multiple
      cortical areas (particularly layer 1), and the file should NOT
      name a single cortical target. The diffuse projection is the
      CL's defining output.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, histamine,
      orexin); memory/stores/ (short_term); gateway/.
    - Connects upward to diencephalon/thalamus/left/medial_nuclear_
      group/.
"""