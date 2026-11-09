"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.lateral_nuclear_group.lateral_posterior_nucleus
Anatomical Role:
    The left lateral posterior nucleus (LP). A medium-sized nucleus in
    the left lateral nuclear group, situated between the left lateral
    dorsal nucleus (LD) and the left pulvinar. It is a PARIETAL
    ASSOCIATION RELAY: its driver input is primarily from the left
    parietal cortex (and from the left pulvinar), and its output is to
    the left posterior parietal cortex (areas 5, 7, and adjacent).

    The LP is the SECOND ANCHOR of the lateral nuclear group (after
    the pulvinar): it is one of the two principal higher-order
    association relays of the group (the pulvinar is visual; the LP
    is parietal). Together they cover the two dominant cortical
    association domains of the human brain.

    DISTINCTIONS (critical):

    - LP vs. PULVINAR (the group's signature trap): both are
      higher-order association relays; the LP is PARIETAL ASSOCIATION
      (posterior parietal cortex, areas 5/7); the pulvinar is VISUAL
      ASSOCIATION (V2–V5, MT, IT). Different cortical targets;
      different association domains. Do not merge; do not treat them
      as interchangeable higher-order relays.

    - LP vs. LD (intra-group): the LP is the parietal association
      relay; the LD is the limbic-adjacent association relay. Different
      cortical targets (posterior parietal vs. cingulate/
      retrosplenial); different association domains. Do not merge.

    - LP vs. VPL/VPM (a subtle trap): the LP is a HIGHER-ORDER
      PARIETAL ASSOCIATION relay (cortical layer 5 driver); the
      VPL/VPM (thalamus/left/ventral_nuclear_group/ventral_posterior_
      nucleus/) are FIRST-ORDER SOMATOSENSORY relays (peripheral
      driver). The LP is often confused with VPL because both project
      to the parietal lobe — but the LP's target is the POSTERIOR
      parietal association cortex (areas 5/7), while VPL/VPM's target
      is the PRIMARY somatosensory cortex (S1, areas 3/1/2).
      Different targets; different relay types; do not merge.

    - LP vs. ANTERIOR NUCLEAR GROUP (a subtle trap): both are thalamic
      relays that project to the parietal or limbic-adjacent cortices.
      The LP is a higher-order parietal association relay; the
      anterior nuclei are Papez memory relays. Different circuits;
      different functions; do not merge.

Functional Mode:
    - Parietal association (the LP's anchor role):
        * The LP receives input from the left parietal cortex (areas
          5, 7, and adjacent) and from the left pulvinar (which
          projects to the LP as part of the parietal association
          circuit); it projects back to the left posterior parietal
          cortex (areas 5 and 7).
        * The LP contributes to SPATIAL ATTENTION: the posterior
          parietal cortex is a key hub for spatial attention and
          visuomotor integration, and the LP is the thalamic relay
          that supports its cortico-cortical loops.
        * The LP contributes to VISUOMOTOR INTEGRATION: the
          translation of visual spatial information into motor
          plans (reaching, grasping, eye movements) depends on the
          posterior parietal cortex and its LP relay.
        * The LP contributes to MULTISENSORY INTEGRATION: the
          posterior parietal cortex integrates visual, somatosensory,
          and vestibular signals for spatial representation; the LP
          relays the cortico-cortical association that supports this
          integration.
    - Parietal-hippocampal interaction (secondary): the LP also
      receives some hippocampal-adjacent inputs and projects to
      retrosplenial-adjacent regions, contributing to spatial memory
      and navigation. This is a secondary role; the primary role is
      parietal association.
    - The LP is therefore the THALAMUS'S PARIETAL ASSOCIATION RELAY:
      its position in the cortico-cortical association hierarchy is
      analogous to the pulvinar's visual association role, but in the
      parietal domain.

    - CLINICAL FACT (the LP's defining clinical anchor; contralateral):
        * LP lesions can produce PARIETAL-LIKE DEFICITS:
          - Contralateral spatial attention deficits (left LP lesion
            → right hemifield spatial neglect-like symptoms; right LP
            lesion → left hemifield).
          - Contralateral visuomotor integration deficits (optic
            ataxia-like symptoms).
          - Contralateral multisensory integration deficits.
        * The LP's clinical picture overlaps with posterior parietal
          cortical lesions (the cortex the LP relays to), which is why
          it is called a "parietal-like" syndrome.
        * LP-SPECIFIC syndromes (isolated LP lesion without adjacent
          thalamic involvement) are RARE, because the LP is rarely
          affected in isolation. Document honestly; do not claim an
          LP-specific syndrome beyond the broader "parietal-like"
          picture. The LP's clinical relevance is as part of the
          thalamic-parietal system.
        * CONTRAALTERAL SPECIFICATION: like the pulvinar and the
          sensory relays, the LP's deficits are CONTRALATERAL. The
          left LP lesion produces right hemifield deficits; the right
          LP lesion produces left hemifield deficits. Document the
          direction explicitly; do not flatten to "LP lesion causes
          parietal deficits" without specifying the side.

Hormonal Modulation (minimal; the LP is a higher-order association relay):
    - The LP is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain) and monoaminergic
      (brainstem) arousal inputs contribute to the attentional gating
      of the parietal association relay. Document as arousal
      modulation, not endocrine modulators.
    - The LP is NOT a principal target of the 12 endocrine axes. Do
      not pad the section with CRH, cortisol, etc.

Memory Interfaces:
    - Reads:
        * short_term: the current state of the LP's parietal
          association loop (current spatial-attention buffer).
        * semantic: the LP contributes to parietal semantic
          association (object knowledge, spatial semantics) via its
          cortical loops.
        * episodic: some LP-hippocampal-adjacent contribution to
          episodic spatial memory (secondary; the LP's primary role is
          association, not memory).
    - Writes: none directly. The LP is a RELAY: it transmits
      association signals between cortical areas; the memory content
      is stored in the cortex, not the thalamus.
    - The LP's memory interfaces are one notch thicker than the LD's
      (the LD reads episodic + short_term; the LP adds semantic) but
      one notch thinner than the pulvinar's (the pulvinar's visual
      association is the most semantic-heavy).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No LP fragment. The LP is a higher-order association relay; the
      model prompt does not need an LP block because the association
      signals it relays are already represented in the upstream
      (parietal cortex) and downstream (posterior parietal cortex)
      fragments. The cortex carries the association state.
    - AGGREGATION RULES: no fragments are emitted from this leaf.
      Deliberate absence, same as the whole thalamus.
    - The LP's clinical fact (contralateral parietal-like deficits) is
      documented for completeness, but is not a prompt field.

Reciprocal Connections (left-side; the right side is in
../../../../right/lateral_nuclear_group/lateral_posterior_nucleus/):

    Parietal association (the anchor):
    - ← telencephalon/cerebral_hemispheres/left/cortex/parietal/
      posterior_parietal_cortex (cortical layer 5 input from the
      left posterior parietal cortex; the LP's driver input; left-side).
    - → telencephalon/cerebral_hemispheres/left/cortex/parietal/
      posterior_parietal_cortex (LP output to the left posterior
      parietal cortex; the higher-order parietal association loop).
    - ← ../pulvinar/ (left pulvinar → left LP; the pulvinar projects
      to the LP as part of the parietal association circuit; intra-
      group edge).

    Multisensory integration (secondary):
    - ↔ telencephalon/cerebral_hemispheres/left/cortex/parietal/*
      (parietal multisensory integration; the LP relays the
      cortico-cortical association that supports it).

    Parietal-hippocampal interaction (secondary):
    - ↔ telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/hippocampus/left (hippocampal-adjacent
      input to the LP; secondary contribution to spatial memory).
    - ↔ telencephalon/cerebral_hemispheres/left/cortex/cingulate/
      retrosplenial_cortex (retrosplenial-adjacent projection;
      secondary contribution to spatial memory).

    Intra-group:
    - ↔ ../lateral_dorsal_nucleus/ (left LD; limbic-adjacent
      association relay; different domain; do not merge).
    - ↔ ../pulvinar/ (left pulvinar; visual association relay;
      different domain; do not merge; the pulvinar → LP edge is the
      intra-group parietal-association link).

    Distinction (not signaling; structural note):
    - ↔ ../../ventral_nuclear_group/ventral_posterior_nucleus (the LP
      and VPL both project to the parietal lobe, but the LP targets
      POSTERIOR parietal association cortex (5/7) while VPL targets
      PRIMARY somatosensory cortex (S1, 3/1/2); different relay
      types; do not merge).

Notes:
    - Tier 1 full leaf (left). The SECOND ANCHOR of the lateral group
      (after the pulvinar); the PARIETAL ASSOCIATION relay.
    - THE LP vs. PULVINAR TRAP is the group's signature trap; the LP
      leaf enforces it from the LP side, matching the pulvinar leaf
      (when drafted).
    - THE LP vs. VPL/VPM TRAP is a NEW trap declared in this leaf:
      both project to the parietal lobe, but the LP is a HIGHER-ORDER
      PARIETAL ASSOCIATION relay (target: areas 5/7) and VPL/VPM are
      FIRST-ORDER SOMATOSENSORY relays (target: S1, areas 3/1/2).
      Different relay types; different cortical targets; do not merge.
      This trap is worth declaring explicitly because "parietal
      projections" is a surface similarity that hides a deep
      difference.
    - THE LP vs. ANTERIOR NUCLEAR GROUP distinction is reproduced: the
      LP is a parietal association relay; the anterior nuclei are
      Papez memory relays. Both project to parietal-adjacent or
      limbic-adjacent cortices; different circuits; do not merge.
    - CONTRALATERAL CLINICAL FACT: like the pulvinar, the LP's
      deficits are CONTRALATERAL (left LP lesion → right hemifield
      parietal-like deficits; right LP lesion → left hemifield). The
      leaf specifies the direction explicitly; the right delta will
      specify the other direction.
    - LP-SPECIFIC SYNDROME HONESTY: isolated LP lesions are rare;
      LP-specific syndromes are not established beyond the broader
      "parietal-like" picture. Document honestly; do not claim an
      LP-specific syndrome.
    - NO FRAGMENT: same as the whole thalamus. The LP is a relay, not
      a state-emitter.
    - The LP is NOT the pulvinar (visual association), NOT the LD
      (limbic-adjacent association), NOT the VPL/VPM (first-order
      somatosensory), NOT the anterior nuclei (Papez memory). The
      traps make these distinctions explicit.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines);
      memory/stores/ (short_term, semantic, episodic); gateway/.
    - Connects upward to diencephalon/thalamus/left/lateral_nuclear_
      group/.
"""