"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.medial_nuclear_group.intralaminar_nuclear_group
Anatomical Role:
    The left intralaminar nuclear group. A SUB-CONTAINER that groups
    the three intralaminar thalamic nuclei — central lateral (CL),
    centromedian (CM), and parafascicular (Pf) — that are ALSO
    documented as DIRECT nodes under
    left/medial_nuclear_group/central_lateral_nucleus/,
    left/medial_nuclear_group/centromedian_nucleus/, and
    left/medial_nuclear_group/parafascicular_nucleus/.

    STRUCTURAL NOTE (the tree quirk; critical):
    This sub-container is an INTEGRATION LAYER, not a duplicate
    declaration. The three intralaminar nuclei are documented as
    direct nodes under medial_nuclear_group/ (their substantive
    content: role, subregions, reciprocal connections, clinical
    facts); this sub-container documents the FAMILY-LEVEL context:
      - The family's collective role (arousal, attention,
        consciousness — the "intralaminar arousal system").
      - The family's internal organization (matrix-type vs. core-type;
        cortical vs. striatal projections).
      - The family's shared clinical facts (bilateral intralaminar
        lesion → coma).
      - The family's clinical anchors (CM DBS; CL/Pf investigational
        DBS for disorders of consciousness).
    Stage 4 audit should treat this sub-container and its three direct
    nodes as an INTEGRATED STRUCTURE. The sub-container does NOT
    duplicate the direct nodes' content; it provides the family-level
    synthesis that the direct nodes cannot provide individually. Same
    structural note as the parent thalamus and medial nuclear group
    containers.

    The three intralaminar nuclei (documented as direct nodes, not
    re-documented here):
        - central_lateral_nucleus/ (CL): matrix-type; diffuse cortical
          layer 1 projections; arousal/attention.
        - centromedian_nucleus/ (CM): core-type; striatal projections
          (re-entrant loop); motor/arousal; DBS anchor.
        - parafascicular_nucleus/ (Pf): matrix-type; diffuse cortical
          + striatal; arousal/nociceptive-adjacent.

    The intralaminar family is one of the two families within the
    medial nuclear group (the other being the midline family,
    documented under midline_nuclear_group/). The two families are
    FUNCTIONALLY DISTINCT — see Trap 2 below.

    NAMING TRAPS (critical — two apply at this family level):

    - TRAP 1: INTRALAMINAR vs. MIDLINE (the primary family-level
      trap; reproduced from the medial nuclear group container and
      the CL/CM leaves). The intralaminar nuclei are AROUSAL and
      ATTENTION relays (brainstem reticular + basal ganglia driver;
      diffuse cortical and striatal projections). The midline nuclei
      (paratenial, reuniens, rhomboidal, PVT) are LIMBIC and
      VISCERAL relays (hypothalamic and limbic driver; hippocampal,
      amygdala, accumbens, PFC projections). Both families are
      "diffuse" thalamic nuclei, but they are functionally distinct.
      Do not merge the two families.

    - TRAP 2: MATRIX-TYPE vs. CORE-TYPE (the intra-family trap). The
      CL and Pf are MATRIX-type (calbindin-positive; diffuse
      cortical layer 1 projections; arousal/attention emphasis). The
      CM is CORE-type (parvalbumin-positive; topographic striatal
      projections; motor/arousal emphasis). The two types have
      different projection patterns and functional emphases; do not
      treat the three nuclei as interchangeable.

Functional Mode (family-level synthesis; the individual nuclei's
functions are in their direct-node leaves):
    - Arousal and attention (the family's primary role):
        * The intralaminar nuclei collectively form the "intralaminar
          arousal system": they receive brainstem reticular and basal
          ganglia inputs and project diffusely to the cortex (CL, Pf)
          and topographically to the striatum (CM). Their collective
          activity sustains arousal, attention, and the cortical
          activation that underlies consciousness.
        * The intralaminar family is the thalamic component of the
          ascending arousal system. It complements the brainstem
          reticular formation (the other major arousal system) and
          the hypothalamic arousal nuclei (LPO, TMN, orexin).
    - Consciousness (the family's most significant functional
      contribution):
        * The intralaminar system is REQUIRED for normal
          consciousness. Its bilateral destruction produces coma or
          persistent vegetative state (see the family-level clinical
          fact). The CL and Pf's matrix projections to cortical
          layer 1 are the anatomical basis of the "thalamocortical
          loop" that sustains consciousness; the CM's striatal
          projections modulate the basal-ganglia-thalamo-cortical
          loop that supports motor and cognitive processing.
        * The intralaminar family is the thalamic counterpart of the
          brainstem reticular activating system: it translates
          brainstem arousal into cortical activation.
    - Motor modulation (family's secondary role; CM emphasis):
        * The CM's striatal projections form a
          basal-ganglia-thalamo-striatal re-entrant loop that
          modulates the basal ganglia's motor and cognitive
          processing. This is the family's motor-modulatory
          contribution; it is distinct from the first-order motor
          relay of the VA/VL.
    - Nociceptive-adjacent contribution (family's tertiary role; Pf
      emphasis):
        * The Pf has nociceptive-adjacent components; it contributes
          to the arousal and attention components of nociceptive
          processing. This is secondary to the arousal/attention
          role.
    - The intralaminar family is therefore a THREE-NUCLEUS AROUSAL
      SYSTEM with a motor-modulatory sub-loop (CM) and a
      nociceptive-adjacent sub-loop (Pf). Its collective role is one
      of the most important thalamic contributions to consciousness.

    - FAMILY-LEVEL CLINICAL FACTS (the shared anchors):
        * SEVERE BILATERAL INTRALAMINAR LESIONS produce coma or
          persistent vegetative state — the family's shared clinical
          anchor (the CL and CM leaves both document it from their
          sides).
        * CM DBS (established for Tourette's and some dystonias;
          investigational for disorders of consciousness) — the
          family's most established clinical application.
        * CL/Pf DBS for disorders of consciousness (investigational)
          — the family's active research area.
        * The intralaminar family is therefore the thalamus's most
          clinically significant arousal family — it is both a
          consciousness-critical system and a DBS target.

Hormonal Modulation (family-level summary):
    - The intralaminar family is NOT a neuroendocrine structure.
    - Modulators: the ascending arousal systems — cholinergic (basal
      forebrain, LDT/PPN), monoaminergic (LC, raphe), histaminergic
      (TMN), and orexinergic (LHA) — are the primary inputs that
      modulate the family's arousal and attention functions.
      Dopaminergic (SNc) and GABAergic (GPi/SNr) inputs modulate the
      CM's striatal loop specifically.
    - The intralaminar family is NOT a principal target of the 12
      endocrine axes. Do not pad the section with CRH, cortisol, etc.

Memory Interfaces (family-level summary):
    - CL: reads short_term (arousal/attention state buffer).
    - CM: reads procedural (the basal-ganglia-thalamo-striatal
      loop's procedural memory) and short_term (arousal/attention
      state).
    - Pf: reads short_term (arousal/attention state); nociceptive-
      adjacent reads (secondary).
    - Writes: none directly. The intralaminar family relays arousal,
      attention, and motor-modulatory signals; the memory content is
      stored in the cortex, striatum, and other downstream structures.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No intralaminar family fragment. The family is an
      arousal/attention/motor-modulatory relay system; the model
      prompt does not need an intralaminar-group block because the
      arousal/attention state is already represented in the upstream
      arousal fragments (LPO, TMN, LC, raphe, orexin) and the
      downstream cortical activation state. The individual nuclei
      emit no fragments either; the family collectively does not.
    - AGGREGATION RULES: no fragments are emitted from this
      sub-container. Deliberate absence, same as the whole thalamus.
    - The family's clinical facts (coma; DBS) are documented for
      completeness, but are not prompt fields.

Children (the sub-container has no children of its own in the tree
sense — its members are the direct nodes under medial_nuclear_group):
    - The three intralaminar nuclei are documented as direct nodes
      under left/medial_nuclear_group/:
        - central_lateral_nucleus/  (Tier 1 leaf; matrix-type;
                                      arousal/attention)
        - centromedian_nucleus/     (Tier 1 leaf; core-type;
                                      motor/arousal; DBS anchor)
        - parafascicular_nucleus/   (Tier 1 leaf; matrix-type;
                                      arousal/nociceptive-adjacent)
    - This sub-container does NOT have its own left/ and right/
      children; the sub-container itself is the family-level
      integration, and the direct nodes under medial_nuclear_group/
      are its members. The right-side equivalent is
      right/medial_nuclear_group/intralaminar_nuclear_group/ (a
      delta of this file).

    STRUCTURAL NOTE: the tree's "container + direct nodes" pattern
    means this sub-container is a SIBLING of its own members, not
    their parent. This is unusual but intentional (see the parent
    containers' structural notes). The audit should treat the
    sub-container and the three direct nodes as an INTEGRATED
    STRUCTURE for functional purposes, while respecting that the
    tree hierarchy places them as siblings.

Notes:
    - Sub-container. It is an INTEGRATION LAYER for the intralaminar
      family, not a duplicate of its members. Do not re-document the
      three nuclei here; point to their direct-node leaves.
    - THE TREE QUIRK (container + direct nodes) is the most important
      structural note in this file. Stage 4 must treat the
      sub-container and the three direct nodes as integrated, not as
      duplicates. This is the same structural pattern as the parent
      thalamus and medial nuclear group containers, but it is MOST
      PRONOUNCED here because the container's members are also its
      siblings (not children).
    - THE INTRALAMINAR vs. MIDLINE TRAP (Trap 1) is reproduced in
      full; it is the family-level trap (the two families are
      functionally distinct despite both being "diffuse").
    - THE MATRIX vs. CORE TRAP (Trap 2) is reproduced in full; it is
      the intra-family trap (CL/Pf are matrix; CM is core).
    - THE FAMILY-LEVEL CLINICAL FACTS are the family's collective
      anchors: coma from bilateral lesions; CM DBS; CL/Pf
      investigational DBS. The individual nucleus leaves document the
      nucleus-specific versions; this sub-container documents the
      family-level synthesis.
    - THE INTRALAMINAR FAMILY IS THE THALAMUS'S AROUSAL SYSTEM: it is
      the thalamic component of the ascending arousal system, along
      with the brainstem reticular formation and the hypothalamic
      arousal nuclei (LPO, TMN, orexin). Document this framing; it
      is the family's most important contribution.
    - NO FRAGMENT: same as the whole thalamus. The intralaminar
      family is a relay system, not a state-emitter. The arousal
      state is carried by the upstream arousal fragments.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, histamine,
      orexin, dopamine, GABA, glutamate); memory/stores/ (short_term,
      procedural); gateway/.
    - Reciprocal connections to enforce in Stage 4 (summary; per-
      nucleus wiring is in the direct-node leaves):
        * The sub-container itself has no direct reciprocal edges
          (it is a functional grouping, not a signaling node). The
          reciprocal edges are declared in the direct-node leaves
          (CL, CM, Pf).
        * The sub-container's "reciprocal" relationship is with its
          own members: it is the family-level integration of their
          collective role. No separate signaling edges.
    - Connects upward to diencephalon/thalamus/left/medial_nuclear_
      group/.
"""