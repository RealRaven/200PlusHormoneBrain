"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.medial_nuclear_group
Anatomical Role:
    The left medial nuclear group of the thalamus. The LARGEST and most
    heterogeneous thalamic group: it contains NINE nuclei plus TWO
    sub-containers (intralaminar, midline), spanning three functional
    families:
        - PREFRONTAL RELAY (the group's anchor): the mediodorsal
          nucleus (MD). Relays amygdala, substantia innominata, ventral
          pallidum, and prefrontal cortex inputs to the prefrontal
          cortex. The MD is the thalamic hub of the executive/limbic
          loop.
        - AROUSAL / ATTENTION (intralaminar family): the central
          lateral nucleus, the centromedian nucleus, and the
          parafascicular nucleus (plus the intralaminar_nuclear_group/
          sub-container that groups them). Receive brainstem reticular
          and basal ganglia inputs; project diffusely to the cortex;
          contribute to arousal, attention, and the cortical activation
          that underlies consciousness.
        - LIMBIC (midline family): the paratenial nucleus, the
          reuniens nucleus, the rhomboidal nucleus, the paraventricular
          thalamic nucleus (PVT; see the trap below), and any other
          midline nuclei (grouped by the midline_nuclear_group/
          sub-container). Receive hypothalamic, brainstem, and limbic
          inputs; project to the hippocampal formation, amygdala,
          nucleus accumbens, and prefrontal cortex; contribute to
          limbic/visceral integration and to memory/emotional
          modulation.

    STRUCTURAL NOTE (the tree quirk; critical):
    The left medial nuclear group contains BOTH direct nucleus nodes
    AND two sub-containers:
        - Intralaminar family: central_lateral_nucleus/,
          centromedian_nucleus/, and parafascicular_nucleus/ are
          documented as DIRECT nodes under medial_nuclear_group/, AND
          there is also an intralaminar_nuclear_group/ container that
          groups them.
        - Midline family: paratenial_nucleus/, reuniens_nucleus/, and
          rhomboidal_nucleus/ are documented as DIRECT nodes, AND
          there is also a midline_nuclear_group/ container that groups
          them (and that would contain the paraventricular thalamic
          nucleus if it is added).
    The containers are an INTEGRATION LAYER: they group the direct
    nodes functionally, but do not duplicate content. The Stage 4
    audit should treat each container and its direct nodes as an
    integrated structure, not as duplicate declarations. Same
    structural note as the parent thalamus container.

    NAMING TRAPS (critical — THREE overlapping layers apply here):

    - TRAP 1: THALAMIC PVT vs. HYPOTHALAMIC PVN (the tree's most-flagged
      trap; already declared from posterior/lateral_area/.../
      posterior_part_of_lateral_nucleus/ and tuberal/medial_area/.../
      arcuate_nucleus/). The THALAMIC PARAVENTRICULAR NUCLEUS (PVT; in
      the left midline_nuclear_group/ if it is added as a direct
      node, or referenced by the midline group) is a LIMBIC/AROUSAL
      relay. The HYPOTHALAMIC PARAVENTRICULAR NUCLEUS (PVN;
      hypothalamus/anterior/medial_area/left/paraventricular_nucleus/)
      is the CRH/TRH/oxytocin/vasopressin hub. DIFFERENT STRUCTURES;
      confusingly similar names; do not merge. This container is the
      CANONICAL DECLARATION of the trap; the medial nuclear group's
      children (including the midline group and any PVT leaf) must be
      consistent with it.

    - TRAP 2: INTRALAMINAR vs. MIDLINE (the sub-trap). The intralaminar
      nuclei (centrolateral, centromedian, parafascicular) are AROUSAL
      and ATTENTION relays (brainstem reticular + basal ganglia
      driver; diffuse cortical projections). The midline nuclei
      (paratenial, reuniens, rhomboidal, PVT) are LIMBIC and VISCERAL
      relays (hypothalamic and limbic driver; hippocampal, amygdala,
      accumbens, PFC projections). Different drivers; different
      targets; different functions. Do not merge the two sub-families;
      they are often confused because both are "diffuse" thalamic
      nuclei, but they are functionally distinct.

    - TRAP 3: MEDIODORSAL vs. ANTERIOR NUCLEAR GROUP (subtle). Both are
      memory-related thalamic relays. The MD is the PREFRONTAL relay
      (amygdala/PFC → MD → PFC; executive and limbic-prefrontal
      loops). The anterior nuclei
      (thalamus/left/anterior_nuclear_group/) are the PAPEZ memory
      relays (hippocampus → mammillary bodies → anterior nuclei →
      cingulate). Different circuits; different nuclei; do not merge.

    - ADDITIONAL SUB-TRAP: the medial_dorsal nucleus vs. the
      midline_nuclear_group (both project to the PFC, but the MD is a
      discrete prefrontal relay and the midline nuclei are a
      distributed limbic/visceral family). Do not merge.

Functional Mode:
    - Prefrontal relay (MD; the group's anchor role):
        * The MD receives input from the amygdala, the substantia
          innominata, the ventral pallidum, and the prefrontal cortex
          itself; it projects back to the prefrontal cortex
          (especially the dorsolateral and orbitofrontal PFC).
        * The MD is the thalamic hub of the EXECUTIVE and LIMBIC-
          PREF RONTAL loops: it relays the amygdala's affective
          signal and the PFC's own recurrent signal, integrating
          affect with executive function. Its role in working memory,
          decision-making, and reward-based learning is established.
        * The MD also connects reciprocally with the PFC in the
          "prefrontal thalamo-cortical loop" that supports executive
          function; the MD is the MD of "MD-PFC" literature.
    - Arousal and attention (intralaminar family; the group's second
      role):
        * The intralaminar nuclei (centrolateral, centromedian,
          parafascicular) receive brainstem reticular and basal
          ganglia inputs and project diffusely to the cortex.
        * They contribute to AROUSAL, ATTENTION, and the cortical
          activation that underlies consciousness. The centromedian
          and parafascicular nuclei are also part of the
          basal-ganglia-thalamo-cortical motor loop (adjacent to the
          motor thalamus), and the centromedian is a DBS target for
          some movement disorders and for disorders of consciousness.
        * The intralaminar family is the thalamic counterpart of the
          brainstem arousal system: it is one of the nodes that
          translates brainstem arousal into cortical activation.
    - Limbic and visceral integration (midline family; the group's
      third role):
        * The midline nuclei (paratenial, reuniens, rhomboidal, PVT)
          receive hypothalamic, brainstem, and limbic inputs and
          project to the hippocampal formation, amygdala, nucleus
          accumbens, and prefrontal cortex.
        * The reuniens nucleus is a HIPPOCAMPAL RELAY: it is
          reciprocally connected with the hippocampus (especially the
          CA1 and subiculum) and the medial prefrontal cortex, and
          contributes to spatial working memory and to
          hippocampal-prefrontal communication. This is the midline
          family's most studied member.
        * The PVT (thalamic paraventricular nucleus) is a LIMBIC
          RELAY: it is reciprocally connected with the amygdala,
          hypothalamus, and nucleus accumbens, and contributes to
          stress, reward, and emotional regulation. It is the
          thalamic counterpart of the hypothalamic PVN but with
          completely different function — see Trap 1.
    - The medial nuclear group is therefore the THALAMUS'S
      HETEROGENEOUS MEDIAL GROUP: prefrontal relay (MD) + arousal
      (intralaminar) + limbic/visceral (midline). It is the least
      homogeneous of the thalamic groups (unlike the anterior group's
      Papez identity or the lateral group's higher-order association
      identity), and it is the group where the tree's structural quirk
      (direct nodes + sub-containers) is most evident.

    - CLINICAL FACTS (one per family):
        * MD lesions: EXECUTIVE and AFFECTIVE DEFICITS — deficits in
          working memory, decision-making, reward-based learning, and
          affective regulation (the "MD syndrome"). The MD is also
          implicated in schizophrenia (reduced MD volume and
          connectivity are reported), and MD DBS is investigated for
          treatment-resistant depression.
        * Intralaminar lesions: AROUSAL and ATTENTION deficits;
          severe bilateral intralaminar lesions can produce coma or
          persistent vegetative state (the intralaminar nuclei are
          part of the ascending arousal system). Centromedian DBS is
          used for some movement disorders and for disorders of
          consciousness.
        * Midline lesions: the reuniens nucleus is implicated in
          spatial working memory deficits; PVT lesions are implicated
          in stress and reward dysregulation. The midline family's
          clinical contribution is the least characterized of the
          three (the "less characterized" family within the group).
      The group's clinical anchor is the MD's executive-affective
      syndrome; the intralaminar and midline families contribute
      secondary clinical pictures.

Hormonal Modulation (group-wide summary; per-nucleus wiring in the
child leaves):
    - The medial nuclear group is NOT a neuroendocrine structure.
    - Modulators: cholinergic (basal forebrain), monoaminergic
      (brainstem), and histaminergic (TMN) arousal inputs contribute to
      the attentional gating of the prefrontal, arousal, and limbic
      relays. Document as arousal modulation, not endocrine
      modulators.
    - The medial nuclear group is NOT a principal target of the 12
      endocrine axes. Do not pad the section with CRH, cortisol, etc.

Memory Interfaces (group-wide summary):
    - MD: reads episodic, semantic, and reinforcement_value_based_
      learning (the MD-PFC loop uses all three; the MD relays them but
      does not store them).
    - Intralaminar: reads short_term (the arousal state that gates
      attention).
    - Midline (especially reuniens): reads episodic and short_term
      (the reuniens is a hippocampal relay; it reads the hippocampal
      memory signal).
    - Writes: none directly. The medial group relays association,
      arousal, and limbic signals; the memory content is stored in the
      cortex (and in the hippocampus, for the reuniens relay).
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No medial group fragment. The medial group contains relays
      (prefrontal, arousal, limbic), not state-emitters; the model
      prompt does not need a medial-group block. The relevant state is
      carried by the upstream sources (PFC, amygdala, brainstem,
      hypothalamus) and downstream targets (PFC, cortex, hippocampus).
    - AGGREGATION RULES: no fragments are emitted from this container
      or from any medial-group leaf. Deliberate absence, same as the
      whole thalamus.
    - The MD's clinical facts (executive-affective; depression;
      schizophrenia) are documented for completeness, but are not
      prompt fields.

Children (nine direct nuclei + two sub-containers; the sub-containers
group the intralaminar and midline families):
    Prefrontal relay (anchor):
    - medial_dorsal_nucleus/    ★ Tier 1 leaf. The MD; prefrontal
                                  relay; the group's clinical anchor.

    Intralaminar family (arousal/attention; direct nodes + sub-
    container):
    - central_lateral_nucleus/   Tier 1 leaf. Intralaminar arousal
                                  relay.
    - centromedian_nucleus/      Tier 1 leaf. Intralaminar; motor and
                                  arousal relay; DBS target.
    - parafascicular_nucleus/    Tier 1 leaf. Intralaminar arousal
                                  relay.
    - intralaminar_nuclear_group/ Sub-container grouping the three
                                  intralaminar direct nodes. See the
                                  structural note: it is an
                                  integration layer, not a duplicate.

    Midline family (limbic/visceral; direct nodes + sub-container):
    - paratenial_nucleus/        Tier 1 leaf. Midline; limbic relay.
    - reuniens_nucleus/          Tier 1 leaf. Midline; HIPPOCAMPAL
                                  relay; spatial working memory.
    - rhomboidal_nucleus/        Tier 1 leaf. Midline; limbic relay.
    - midline_nuclear_group/     Sub-container grouping the midline
                                  direct nodes (and the PVT if added).
                                  See the structural note.
    - (paraventricular thalamic nucleus, PVT: if added as a direct
      node, would be under midline_nuclear_group/; see Trap 1 for the
      PVN vs. PVT distinction. The tree's current structure does not
      have a separate PVT node, but the trap is declared here for
      consistency with the earlier declarations in the posterior LHA
      and arcuate leaves.)

Notes:
    - Group container. Names the nine direct nodes and two
      sub-containers; defers functional content to the leaves (except
      for the container-level summary above).
    - THREE TRAPS reproduced in full above (PVT vs. PVN; intralaminar
      vs. midline; MD vs. anterior group), plus the MD vs. midline
      sub-trap. All apply specifically to nuclei within this group.
      This is the most trap-dense thalamic group.
    - THE PVT vs. PVN TRAP IS THE TREE'S MOST-FLAGGED TRAP: it has
      been declared from the posterior LHA and arcuate leaves (in the
      hypothalamus), and this container is its CANONICAL THALAMIC
      DECLARATION. Every medial-group child that references the
      thalamic PVT (or its midline container) must be consistent
      with this declaration.
    - THE STRUCTURAL NOTE (direct nodes + sub-containers) is the
      tree's structural quirk, most pronounced here. The containers
      are integration layers, not duplicate declarations. Stage 4
      should treat each container and its direct nodes as an
      integrated structure.
    - THE MD IS THE GROUP'S ANCHOR: it is the largest, most studied,
      most clinically anchored nucleus of the group. It is the natural
      first leaf to draft.
    - THE INTRALAMINAR FAMILY IS THE SECOND PRIORITY: the three
      intralaminar nuclei (central lateral, centromedian,
      parafascicular) are the arousal relays; the centromedian is a
      DBS target. Their collective role (arousal, attention,
      consciousness) is one of the thalamus's most important
      contributions.
    - THE MIDLINE FAMILY IS THE THIRD PRIORITY: the three midline
      nuclei (paratenial, reuniens, rhomboidal) are the limbic/
      visceral relays; the reuniens is the most studied (hippocampal
      relay, spatial working memory). The PVT is the trap-focal
      midline nucleus.
    - THE MD'S CLINICAL ANCHOR IS ESTABLISHED: the MD's executive-
      affective syndrome; the MD's involvement in depression (DBS
      investigated) and schizophrenia (reduced volume/connectivity).
    - THE INTRALAMINAR'S CLINICAL ANCHOR IS ESTABLISHED: severe
      bilateral intralaminar lesions produce coma/persistent
      vegetative state; centromedian DBS is used for movement
      disorders and disorders of consciousness.
    - THE MIDLINE'S CLINICAL ANCHOR IS LESS ESTABLISHED: the reuniens
      is implicated in spatial working memory deficits; PVT in stress
      and reward dysregulation; the family is the group's least
      characterized.
    - NO FRAGMENT: same as the whole thalamus. The medial group is a
      relay, not a state-emitter.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, histamine);
      memory/stores/ (episodic, semantic, short_term,
      reinforcement_value_based_learning); gateway/.
    - Reciprocal connections to enforce in Stage 4 (summary; per-
      nucleus wiring in the child leaves):
        * medial_nuclear_group/left/medial_dorsal_nucleus ↔
          telencephalon/.../cortex/frontal/prefrontal_cortex (MD ↔
          PFC; executive/limbic-prefrontal loop).
        * medial_nuclear_group/left/medial_dorsal_nucleus ↔
          telencephalon/.../subcortical/medial_temporal_lobe/amygdala
          (MD ↔ amygdala; affective relay).
        * medial_nuclear_group/left/intralaminar family
          (central_lateral, centromedian, parafascicular) ↔
          brainstem/.../reticular_formation and telencephalon/.../
          basal_ganglia (arousal and attention inputs).
        * medial_nuclear_group/left/intralaminar family → cortex
          (diffuse arousal projections; no single cortical target).
        * medial_nuclear_group/left/midline family (paratenial,
          reuniens, rhomboidal) ↔ hypothalamus (limbic/visceral
          inputs).
        * medial_nuclear_group/left/reuniens_nucleus ↔ telencephalon/
          .../subcortical/medial_temporal_lobe/hippocampus (the
          reuniens-hippocampal relay; spatial working memory).
        * medial_nuclear_group/left/midline family → telencephalon/
          .../subcortical/medial_temporal_lobe/amygdala,
          telencephalon/.../basal_ganglia/ventral_striatum/
          nucleus_accumbens, telencephalon/.../cortex/frontal/
          prefrontal_cortex (limbic/visceral outputs).
        * (If the PVT is added: medial_nuclear_group/left/midline_
          nuclear_group/paraventricular_nucleus ↔ hypothalamus/
          amygdala/accumbens/PFC; the trap with the hypothalamic PVN
          is declared in Trap 1 above.)
    - Connects upward to diencephalon/thalamus/left/.
"""