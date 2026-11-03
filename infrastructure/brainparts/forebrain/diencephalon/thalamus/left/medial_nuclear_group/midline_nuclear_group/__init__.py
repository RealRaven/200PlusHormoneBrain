"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.left.medial_nuclear_group.midline_nuclear_group
Anatomical Role:
    The left midline nuclear group. A SUB-CONTAINER that groups the
    midline thalamic nuclei — paratenial (Pt), reuniens (Re), rhomboidal
    (Rh), and the paraventricular thalamic nucleus (PVT) if it is added
    as a direct node — that are ALSO documented as DIRECT nodes under
    left/medial_nuclear_group/paratenial_nucleus/,
    left/medial_nuclear_group/reuniens_nucleus/, and
    left/medial_nuclear_group/rhomboidal_nucleus/ (and
    left/medial_nuclear_group/midline_nuclear_group/paraventricular_
    nucleus/ if the PVT is added).

    STRUCTURAL NOTE (the tree quirk; critical; reproduced from the
    intralaminar sub-container):
    This sub-container is an INTEGRATION LAYER, not a duplicate
    declaration. The midline nuclei are documented as direct nodes
    under medial_nuclear_group/ (their substantive content: role,
    subdivisions, reciprocal connections, clinical facts); this
    sub-container documents the FAMILY-LEVEL context:
      - The family's collective role (limbic and visceral integration;
        hippocampal, amygdala, accumbens, and PFC modulation).
      - The family's internal organization (paratenial/rhomboidal:
        olfactory-limbic; reuniens: hippocampal; PVT: stress/reward).
      - The family's shared structural feature (midline position,
        "diffuse" projections to limbic and prefrontal targets).
      - The PVT-vs-PVN trap (the tree's most-flagged trap; this
        sub-container is the CANONICAL THALAMIC DECLARATION of it for
        the left hemisphere).
    Stage 4 audit should treat this sub-container and its direct nodes
    as an INTEGRATED STRUCTURE. The sub-container does NOT duplicate
    the direct nodes' content; it provides the family-level synthesis
    that the direct nodes cannot provide individually. Same structural
    pattern as the intralaminar sub-container, the medial nuclear
    group container, and the thalamus container.

    The midline family members (documented as direct nodes, not
    re-documented here):
        - paratenial_nucleus/ (Pt): an OLFACTORY-LIMBIC relay.
          Receives olfactory and limbic inputs; projects to the
          amygdala, hippocampus, and prefrontal cortex. The least
          studied of the three; document honestly.
        - reuniens_nucleus/ (Re): a HIPPOCAMPAL relay. The most
          studied of the three. Reciprocally connected with the
          hippocampus (CA1, subiculum) and the medial prefrontal
          cortex; contributes to spatial working memory and to
          hippocampal-prefrontal communication. The family's anchor.
        - rhomboidal_nucleus/ (Rh): a LIMBIC relay adjacent to the
          reuniens. Receives hypothalamic and limbic inputs; projects
          to the hippocampus and PFC. Less studied than the reuniens;
          document honestly.
        - paraventricular_nucleus/ (PVT; if added as a direct node):
          a STRESS/REWARD/AROUSAL relay. Reciprocally connected with
          the amygdala, hypothalamus, and nucleus accumbens; contributes
          to stress responses, reward, and emotional regulation. This
          is the TRAP FOCUS — see Trap 1 below.
    The tree's current structure does not list a separate PVT node,
    but the trap is declared here for consistency with the earlier
    declarations in the posterior LHA and arcuate leaves. If the PVT
    is added later, it goes under this sub-container.

    The midline family is one of the two families within the medial
    nuclear group (the other being the intralaminar family, documented
    under intralaminar_nuclear_group/). The two families are
    FUNCTIONALLY DISTINCT — see Trap 2 below.

    NAMING TRAPS (critical — THREE apply at this family level):

    - TRAP 1: THALAMIC PVT vs. HYPOTHALAMIC PVN (the tree's
      most-flagged trap; declared from posterior/lateral_area/.../
      posterior_part_of_lateral_nucleus/ and tuberal/medial_area/.../
      arcuate_nucleus/, and canonically from the medial nuclear group
      container). The THALAMIC PARAVENTRICULAR NUCLEUS (PVT; in this
      midline group) is a LIMBIC/STRESS/REWARD relay. The HYPOTHALAMIC
      PARAVENTRICULAR NUCLEUS (PVN; hypothalamus/anterior/medial_area/
      left/paraventricular_nucleus/) is the CRH/TRH/oxytocin/
      vasopressin hub. DIFFERENT STRUCTURES; confusingly similar names;
      DO NOT MERGE. This sub-container is the CANONICAL LEFT-HEMISPHERE
      THALAMIC DECLARATION of the trap; every midline-group child that
      references the left thalamic PVT must be consistent with it.

    - TRAP 2: INTRALAMINAR vs. MIDLINE (the primary family-level trap;
      reproduced from the medial nuclear group container, the CL/CM
      leaves, and the intralaminar sub-container). The midline nuclei
      are LIMBIC and VISCERAL relays (hypothalamic and limbic driver;
      hippocampal, amygdala, accumbens, PFC projections). The
      intralaminar nuclei are AROUSAL and ATTENTION relays (brainstem
      reticular + basal ganglia driver; diffuse cortical and striatal
      projections). Both families are "diffuse" thalamic nuclei, but
      they are FUNCTIONALLY DISTINCT. Do not merge.

    - TRAP 3: MIDLINE vs. MEDIODORSAL (the intra-group sub-trap;
      reproduced from the MD leaf and the medial nuclear group
      container). The midline nuclei are a DISTRIBUTED limbic/visceral
      family; the MD is a DISCRETE prefrontal relay. Both project to
      the PFC, but the midline family's PFC projections are part of
      its broader limbic/visceral role, not a dedicated prefrontal
      relay. Do not merge.

Functional Mode (family-level synthesis; the individual nuclei's
functions are in their direct-node leaves):
    - Limbic and visceral integration (the family's primary role):
        * The midline nuclei receive hypothalamic, brainstem, and
          limbic inputs, and project to the hippocampal formation,
          amygdala, nucleus accumbens, and prefrontal cortex. They
          integrate visceral, affective, and mnemonic signals across
          the limbic-prefrontal system.
        * The midline family is the thalamic component of the LIMBIC
          SYSTEM: it complements the anterior thalamic nuclei (Papez
          memory relay) and the MD (prefrontal relay) as the third
          limbic-related thalamic family.
    - Hippocampal relay (reuniens emphasis; the family's most studied
      function):
        * The reuniens nucleus is reciprocally connected with the
          hippocampus (CA1, subiculum) and the medial prefrontal
          cortex; it is the principal thalamic relay between the
          hippocampus and the mPFC.
        * The reuniens contributes to spatial working memory and to
          hippocampal-prefrontal communication; it is the midline
          family's clinical anchor.
    - Stress, reward, and emotional regulation (PVT emphasis; the
      family's second most studied function):
        * The PVT (if added) is reciprocally connected with the
          amygdala, hypothalamus, and nucleus accumbens; it
          contributes to stress responses, reward, and emotional
          regulation. The PVT's role in stress and reward is the
          family's second anchor.
    - Olfactory-limbic integration (paratenial, rhomboidal emphasis;
      the family's third role):
        * The paratenial and rhomboidal nuclei receive olfactory and
          limbic inputs and project to the amygdala, hippocampus, and
          PFC. Their specific contributions are less studied than the
          reuniens and PVT; document honestly.
    - The midline family is therefore a THREE-OR-FOUR-NUCLEUS LIMBIC
      SYSTEM with a hippocampal sub-relay (reuniens), a stress/reward
      sub-relay (PVT), and an olfactory-limbic sub-family (paratenial,
      rhomboidal). Its collective role is one of the thalamus's
      principal limbic contributions.

    - FAMILY-LEVEL CLINICAL FACTS:
        * REUNIENS: implicated in SPATIAL WORKING MEMORY DEFICITS in
          animal models; the reuniens is the family's most studied
          clinical-anatomy target.
        * PVT: implicated in STRESS AND REWARD DYSREGULATION (in
          animal models of stress, addiction, and affective
          disorders); the PVT's clinical anatomy is the family's
          second anchor.
        * PARATENIAL and RHOMBOIDAL: less characterized clinically;
          the family's "less characterized" members. Document
          honestly.
        * The midline family is therefore the medial nuclear group's
          LEAST CLINICALLY ANCHORED family (contrast with the MD's
          executive-affective syndrome and the intralaminar family's
          coma/DBS picture). The reuniens and PVT provide the
          family's clinical anchors; the paratenial and rhomboidal
          are documented as "less characterized."

Hormonal Modulation (family-level summary):
    - The midline family is NOT a neuroendocrine structure.
    - Modulators: hypothalamic inputs (including from the
      hypothalamic PVN — the actual endocrine hub, not this group's
      PVT), limbic inputs (amygdala, hippocampus), and brainstem
      arousal inputs. These modulate the family's limbic/visceral
      functions. Document as limbic modulation, not endocrine
      modulation.
    - The midline family is NOT a principal target of the 12 endocrine
      axes. Do not pad the section with CRH, cortisol, etc.

Memory Interfaces (family-level summary):
    - Paratenial: reads short_term (limbic state buffer); secondary
      olfactory-limbic reads.
    - Reuniens: reads episodic and short_term (the reuniens is the
      hippocampal relay; it reads the hippocampal episodic signal and
      the current spatial working-memory buffer).
    - Rhomboidal: reads short_term (limbic state buffer); secondary
      olfactory-limbic reads.
    - PVT: reads short_term (stress/reward state buffer) and
      reinforcement_value_based_learning (the PVT's role in reward
      and stress integration).
    - Writes: none directly. The midline family relays limbic/visceral
      and hippocampal signals; the memory content is stored in the
      cortex and hippocampus.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No midline family fragment. The family is a limbic/visceral
      relay system; the model prompt does not need a
      midline-group block because the limbic state is already
      represented in the upstream (hypothalamus, amygdala,
      hippocampus) and downstream (hippocampus, amygdala, accumbens,
      PFC) fragments. The emotional_valence, episodic, and short_term
      reads are carried by the upstream fragments; the midline family
      relays them.
    - AGGREGATION RULES: no fragments are emitted from this
      sub-container. Deliberate absence, same as the whole thalamus.
    - The family's clinical facts (reuniens spatial working memory;
      PVT stress/reward) are documented for completeness, but are not
      prompt fields.

Children (no children of its own in the tree sense — its members are
the direct nodes under medial_nuclear_group):
    - The midline nuclei are documented as direct nodes under
      left/medial_nuclear_group/:
        - paratenial_nucleus/        (Tier 1 leaf; olfactory-limbic)
        - reuniens_nucleus/          (Tier 1 leaf; hippocampal relay;
                                        family anchor)
        - rhomboidal_nucleus/        (Tier 1 leaf; olfactory-limbic)
        - (paraventricular_nucleus/  (Tier 1 leaf; PVT; stress/reward;
          IF ADDED)                   see Trap 1))
    - This sub-container does NOT have its own left/ and right/
      children; the sub-container itself is the family-level
      integration, and the direct nodes under medial_nuclear_group/
      are its members. The right-side equivalent is
      right/medial_nuclear_group/midline_nuclear_group/ (a delta of
      this file).

    STRUCTURAL NOTE (reproduced from the intralaminar sub-container):
    the tree's "container + direct nodes" pattern means this
    sub-container is a SIBLING of its own members, not their parent.
    This is unusual but intentional. The audit should treat the
    sub-container and its direct nodes as an INTEGRATED STRUCTURE for
    functional purposes, while respecting that the tree hierarchy
    places them as siblings.

Notes:
    - Sub-container. It is an INTEGRATION LAYER for the midline family,
      not a duplicate of its members. Do not re-document the direct
      nodes here; point to their leaves.
    - THE TREE QUIRK (container + direct nodes as siblings) is
      reproduced from the intralaminar sub-container; the same
      integration-not-duplication discipline applies.
    - THE PVT vs. PVN TRAP (Trap 1) is the tree's most-flagged trap;
      this sub-container is the CANONICAL LEFT-HEMISPHERE THALAMIC
      DECLARATION of it. Every midline-group child that references
      the left thalamic PVT must be consistent with this declaration.
      The trap is now declared at seven locations across the tree:
        (1) posterior/lateral_area/left/posterior_part_of_lateral_
            nucleus/
        (2) posterior/lateral_area/right/posterior_part_of_lateral_
            nucleus/
        (3) tuberal/medial_area/left/arcuate_nucleus/
        (4) tuberal/medial_area/right/arcuate_nucleus/
        (5) thalamus/left/medial_nuclear_group/ (canonical)
        (6) thalamus/right/medial_nuclear_group/ (canonical)
        (7) THIS FILE (midline sub-container, canonical for the left
            PVT specifically)
    - THE INTRALAMINAR vs. MIDLINE TRAP (Trap 2) is the primary
      family-level trap; reproduced in full.
    - THE MIDLINE vs. MEDIODORSAL TRAP (Trap 3) is the intra-group
      sub-trap; reproduced in abbreviated form (full text is in the
      MD leaf and the medial nuclear group container).
    - THE REUNIENS IS THE FAMILY'S ANCHOR: it is the most studied
      midline nucleus (hippocampal relay; spatial working memory).
    - THE PVT IS THE TRAP FOCUS: it is the family's stress/reward
      relay and the PVT-vs-PVN trap's focal structure.
    - THE PARATENIAL AND RHOMBOIDAL ARE THE FAMILY'S "LESS
      CHARACTERIZED" MEMBERS: document honestly; do not over-write.
    - THE MIDLINE FAMILY IS THE MEDIAL GROUP'S LEAST CLINICALLY
      ANCHORED FAMILY: contrast with the MD (executive-affective) and
      the intralaminar family (coma/DBS). The reuniens and PVT provide
      the family's clinical anchors; the paratenial and rhomboidal
      are documented as "less characterized."
    - NO FRAGMENT: same as the whole thalamus. The midline family is
      a limbic relay system, not a state-emitter. The emotional
      valence, episodic, and short-term state is carried by the
      upstream fragments.
    - NO DIRECT RECIPROCAL EDGES OF ITS OWN: the sub-container is not
      a signaling node; the reciprocal edges are declared in the
      direct-node leaves (paratenial, reuniens, rhomboidal, PVT if
      added).
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/05_* (acetylcholine, monoamines, GABA,
      glutamate); memory/stores/ (episodic, short_term,
      reinforcement_value_based_learning); gateway/.
    - Connects upward to diencephalon/thalamus/left/medial_nuclear_
      group/.
"""