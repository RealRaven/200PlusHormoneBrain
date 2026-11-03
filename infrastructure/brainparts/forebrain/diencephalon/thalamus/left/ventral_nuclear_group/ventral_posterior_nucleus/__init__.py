"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.ventral_nuclear_group.ventral_posterior_nucleus
Anatomical Role:
    The left ventral posterior nucleus (VP). A SUB-CONTAINER that
    groups the two left first-order somatosensory relay nuclei of the
    left ventral nuclear group:
        - ventral_posterior_lateral_nucleus/ (VPL): the BODY
          somatosensory relay. Receives the left medial lemniscus
          (dorsal column pathway; fine touch, vibration,
          proprioception) and the left spinothalamic tract (pain,
          temperature, crude touch); projects to the left primary
          somatosensory cortex (S1) body map (postcentral gyrus).
        - ventral_posterior_medial_nucleus/ (VPM): the FACE
          somatosensory relay AND the TASTE relay. Receives the left
          trigeminothalamic tract (face and head somatosensation);
          projects to the left S1 face map. Its parvicellular
          subdivision (VPMpc) receives taste input from the left
          parabrachial nucleus and projects to the left gustatory
          cortex (anterior insula).

    STRUCTURAL NOTE — THE ONLY GENUINE HIERARCHICAL SUB-CONTAINER IN
    THE THALAMUS:
    Unlike the medial group's intralaminar_nuclear_group/ and
    midline_nuclear_group/ sub-containers (which are INTEGRATION
    LAYERS whose members are their SIBLINGS), the VP sub-container is
    a TRUE PARENT: VPL and VPM are its CHILDREN. This is the only
    standard hierarchical container in the thalamus.
    Stage 4 should treat the VP sub-container as the parent of its
    two children (VPL and VPM). The children are documented under
    ventral_posterior_nucleus/ventral_posterior_lateral_nucleus/ and
    ventral_posterior_nucleus/ventral_posterior_medial_nucleus/. This
    is DIFFERENT from the medial group's sub-containers, whose members
    are NOT children of their sub-containers (they are direct nodes
    under medial_nuclear_group/, and the sub-containers are siblings
    of those nodes).

    The VP's role is the parent for its two first-order somatosensory
    children. It does not carry additional functional content beyond
    the VPL/VPM framing, the two-driver framing, the VPMpc framing,
    and the cross-group traps (all documented below).

    NAMING TRAPS (critical — four apply at this sub-container level):

    - TRAP 1: VPL vs. VPM (the SOMATOTOPIC-SPLIT trap; the VP's
      signature trap). Both are first-order somatosensory relays;
      both project to S1. But VPL = BODY (left medial lemniscus + left
      spinothalamic); VPM = FACE (left trigeminothalamic) + TASTE
      (left parabrachial → VPMpc). Different body maps; different
      drivers; distinct nuclei. Do not merge; the VPL/VPM split is a
      SOMATOTOPIC SPLIT of one functional system, NOT a functional
      split between two independent systems. The VPL and VPM are the
      SAME FUNCTION (somatosensory relay) applied to DIFFERENT PARTS
      of the body (body vs. face) — the split is anatomical/topographic,
      not functional.

    - TRAP 2: VPL vs. spinothalamic vs. medial lemniscus (the
      TWO-DRIVER trap). The VPL receives TWO separate ascending
      somatosensory pathways: the left medial lemniscus (dorsal column;
      fine touch, vibration, proprioception) and the left spinothalamic
      tract (pain, temperature, crude touch). These are SEPARATE
      DRIVERS converging on the same VPL; they map to slightly
      different VPL subregions (the VPL's shell vs. core). Do not
      treat the VPL as a single undifferentiated somatosensory relay;
      document both drivers.

    - TRAP 3: VPL/VPM vs. LP (the first-order-vs-higher-order
      somatosensory-parietal trap; declared from the LP side in
      thalamus/left/lateral_nuclear_group/lateral_posterior_nucleus/;
      THIS SUB-CONTAINER IS THE CANONICAL FIRST-ORDER DECLARATION
      from the first-order side). The VPL/VPM are FIRST-ORDER
      somatosensory relays (peripheral driver → left S1, areas 3/1/2).
      The LP is the HIGHER-ORDER parietal association relay (cortical
      layer 5 driver → left posterior parietal cortex, areas 5/7).
      Both project to the parietal lobe, but for DIFFERENT relay
      types and DIFFERENT cortical targets. Do not merge.

    - TRAP 4: VPL/VPM vs. Pf (the first-order-vs-affective
      nociceptive trap; declared from the Pf side in
      thalamus/left/medial_nuclear_group/parafascicular_nucleus/;
      THIS SUB-CONTAINER IS THE CANONICAL FIRST-ORDER DECLARATION
      from the first-order side). The VPL/VPM receive spinothalamic
      nociceptive input for the SENSORY-DISCRIMINATIVE dimension of
      pain (location, intensity, quality). The Pf receives
      spinothalamic nociceptive input for the AFFECTIVE-MOTIVATIONAL
      dimension (arousal, attention, emotional response). Both are
      involved in pain, but for DIFFERENT DIMENSIONS. Do not merge.

Functional Mode:
    - First-order somatosensory relay — body (VPL; the primary role):
        * The VPL receives two ascending somatosensory pathways from
          the body: the left medial lemniscus (fine touch, vibration,
          proprioception) and the left spinothalamic tract (pain,
          temperature, crude touch). It projects to the left S1 body
          map (postcentral gyrus).
        * The VPL is the thalamic relay of the ascending somatosensory
          pathways for the BODY; it is the anatomical substrate of
          discriminative touch and the sensory-discriminative
          dimension of pain for the contralateral body.
    - First-order somatosensory relay — face + taste (VPM; the second
      role):
        * The VPM receives the left trigeminothalamic tract (face and
          head somatosensation) and projects to the left S1 face map.
        * The VPM's parvicellular subdivision (VPMpc) receives taste
          input from the left parabrachial nucleus and projects to the
          left gustatory cortex (anterior insula). The VPM is therefore
          not purely somatosensory — it carries the taste pathway
          as well.
    - The VP is therefore the THALAMUS'S SOMATOSENSORY GROUP: it
      relays the body's discriminative touch and pain pathways (VPL)
      and the face's somatosensory and taste pathways (VPM). Together
      with the LGN (vision) and MGN (audition), the VP completes the
      thalamus's first-order sensory relay group coverage: vision,
      audition, and somatosensation.

    - CLINICAL FACTS (contralateral; per nucleus):
        * LEFT VPL LESIONS: produce CONTRALATERAL (RIGHT) BODY
          SOMATOSENSORY DEFICITS — RIGHT body hemianesthesia (loss of
          touch, vibration, proprioception, pain, temperature on the
          RIGHT side of the body). Left VPL lesions can also produce
          THALAMIC PAIN SYNDROME (Dejerine-Roussy; chronic RIGHT-sided
          pain after a left thalamic stroke; often with
          hyperalgesia/allodynia). The VPL's clinical anchor is the
          contralateral hemianesthesia.
        * LEFT VPM LESIONS: produce CONTRALATERAL (RIGHT) FACE
          SOMATOSENSORY DEFICITS — RIGHT facial hemianesthesia; left
          VPMpc lesions can produce taste deficits (RIGHT-side taste
          recognition, with left anterior insula involvement).
        * The VPL/VPM pair are therefore the fifth and sixth
          contralateral-clinical pairs in the tree (after the STN, LP,
          pulvinar, LGN, and (pending) the VPL/VPM pairs themselves).

Hormonal Modulation (group-level summary; minimal):
    - The VP is NOT a neuroendocrine structure.
    - Modulators: cholinergic (brainstem, basal forebrain) and
      monoaminergic (brainstem) arousal modulation of the VPL's and
      VPM's sensory relay gain; left S1 corticothalamic feedback to
      VPL/VPM modulates relay gain (attention-dependent). Document as
      arousal and attentional modulation, not endocrine modulators.
    - The VP is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces (group-level summary):
    - VPL: reads short_term (the current somatosensory buffer being
      relayed; the VPL is a sensory relay, not a memory structure).
    - VPM: reads short_term (the current face somatosensory and taste
      buffer being relayed).
    - Writes: none directly. The VP relays somatosensory and taste
      signals to S1 and the gustatory cortex; the memory content is
      stored in the cortex.
    - The VP's memory interface is THIN (short_term only), same as
      the LGN and MGN. Sensory relays do not have higher memory
      interfaces.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No VP fragment. The VP is a first-order somatosensory relay
      group; the model prompt does not need a VP block because the
      somatosensory and taste signals it relays are already
      represented in the upstream (body/face periphery, taste
      receptors) and downstream (S1, gustatory cortex) fragments.
    - AGGREGATION RULES: no fragments are emitted from this
      sub-container or from the VPL/VPM leaves. Deliberate absence,
      same as the whole thalamus.
    - The VP's clinical facts (contralateral hemianesthesia; thalamic
      pain syndrome; taste deficits) are documented for completeness,
      but are not prompt fields.

Children (two children — two full leaves, both children of THIS
sub-container, not siblings of it):
    - ventral_posterior_lateral_nucleus/   ★ Tier 1 leaf. The VPL;
                                             BODY somatosensory relay.
    - ventral_posterior_medial_nucleus/    ★ Tier 1 leaf. The VPM;
                                             FACE somatosensory + TASTE
                                             relay (with VPMpc).

    Both are full leaves (not deltas of each other). The left/right
    pairs follow the standard hemisphere-delta pattern.

    STRUCTURAL NOTE: the children are CHILDREN of this sub-container
    (not siblings, unlike the medial group's sub-containers). The
    audit should treat VPL and VPM as children of the VP
    sub-container.

Notes:
    - Sub-container. This is the ONLY GENUINE HIERARCHICAL
      SUB-CONTAINER IN THE THALAMUS: VPL and VPM are its CHILDREN,
      not its siblings. This is structurally DIFFERENT from the
      medial group's intralaminar_nuclear_group/ and
      midline_nuclear_group/ sub-containers.
    - THE VPL vs. VPM TRAP is the SOMATOTOPIC-SPLIT trap: both are
      first-order somatosensory relays; the split is body vs. face
      (anatomical/topographic), not functional. Reproduced in full;
      the VPL and VPM leaves must enforce it.
    - THE VPL's TWO DRIVERS (medial lemniscus + spinothalamic) are
      documented as the "two-driver" trap; both drivers converge on
      the VPL. Do not treat the VPL as a single undifferentiated
      somatosensory relay.
    - THE VPMpc TASTE SUB-NUCLEUS is documented within the VPM leaf
      (not as a child node). The VPM is not purely somatosensory; it
      carries taste from the parabrachial nucleus to the gustatory
      cortex. Same convention as the LGN's layers, the MGN's
      divisions, the pulvinar's subregions, the MD's subdivisions,
      the VA's subdivisions, and the VL's VIM.
    - THE VPL/VPM vs. LP and VPL/VPM vs. Pf CROSS-GROUP TRAPS are the
      two canonical first-order declarations; declared from the LP and
      Pf sides; THIS SUB-CONTAINER IS THE CANONICAL FIRST-ORDER SIDE.
    - NO FRAGMENT: same as the whole thalamus. The VP is a
      first-order somatosensory relay group, not a state-emitter.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (short_term); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * The sub-container itself has no direct reciprocal edges (it
          is a hierarchical grouping, not a signaling node). The
          reciprocal edges are declared in the VPL and VPM child
          leaves.
        * VPL child: ← left medial lemniscus and ← left spinothalamic
          (body somatosensory input) and → left S1 body map.
        * VPM child: ← left trigeminothalamic (face somatosensory
          input) and → left S1 face map; ← left parabrachial (taste
          input to VPMpc) and → left gustatory cortex.
    - Connects upward to diencephalon/thalamus/left/ventral_nuclear_
      group/.
"""