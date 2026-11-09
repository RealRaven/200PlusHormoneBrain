"""
Package: infrastructure.brainparts.forebrain.diencephalon.thalamus.right.medial_nuclear_group.midline_nuclear_group
Anatomical Role:
    The right midline nuclear group. A SUB-CONTAINER that groups the
    right midline thalamic nuclei — paratenial (Pt), reuniens (Re),
    rhomboidal (Rh), and the paraventricular thalamic nucleus (PVT) if
    it is added as a direct node — that are ALSO documented as DIRECT
    nodes under right/medial_nuclear_group/paratenial_nucleus/,
    right/medial_nuclear_group/reuniens_nucleus/, and
    right/medial_nuclear_group/rhomboidal_nucleus/ (and
    right/medial_nuclear_group/midline_nuclear_group/paraventricular_
    nucleus/ if the PVT is added).

    See ../../left/medial_nuclear_group/midline_nuclear_group/
    __init__.py for the full family-level synthesis: the limbic/
    visceral integration role, the hippocampal relay (reuniens), the
    stress/reward relay (PVT), the olfactory-limbic sub-family
    (paratenial, rhomboidal), the family-level clinical facts, and
    the "midline family is the limbic system's thalamic component"
    framing. This right delta does not duplicate that synthesis; it
    reproduces the three family-level traps and the family-level
    clinical facts in abbreviated form, and points to the left
    sub-container for the full content.

    STRUCTURAL NOTE (reproduced from the left sub-container; applies
    on the right identically):
    This right sub-container is an INTEGRATION LAYER, not a duplicate
    declaration. The right midline nuclei are documented as direct
    nodes under right/medial_nuclear_group/ (their substantive
    content); this right sub-container documents the FAMILY-LEVEL
    context for the right hemisphere. Stage 4 audit should treat this
    right sub-container and its right direct nodes as an INTEGRATED
    STRUCTURE. The sub-container's members are its SIBLINGS (not
    children) — same structural quirk as on the left.

    Reproduced THREE TRAPS (apply equally on the right):

    - TRAP 1: THALAMIC PVT vs. HYPOTHALAMIC PVN (the tree's
      most-flagged trap; canonical right-hemisphere thalamic
      declaration). The RIGHT THALAMIC PARAVENTRICULAR NUCLEUS (PVT;
      in this right midline group) is a LIMBIC/STRESS/REWARD relay.
      The RIGHT HYPOTHALAMIC PARAVENTRICULAR NUCLEUS (PVN;
      hypothalamus/anterior/medial_area/right/paraventricular_nucleus/)
      is the CRH/TRH/oxytocin/vasopressin hub. DIFFERENT STRUCTURES;
      confusingly similar names; DO NOT MERGE. This sub-container is
      the CANONICAL RIGHT-HEMISPHERE THALAMIC DECLARATION of the trap;
      every right midline-group child that references the right
      thalamic PVT must be consistent with it.

    - TRAP 2: INTRALAMINAR vs. MIDLINE (the primary family-level trap;
      reproduced from the right medial nuclear group container, the
      right CL/CM leaves, and the right intralaminar sub-container).
      The right midline nuclei are LIMBIC and VISCERAL relays
      (hypothalamic and limbic driver; hippocampal, amygdala,
      accumbens, PFC projections). The right intralaminar nuclei are
      AROUSAL and ATTENTION relays. Both families are "diffuse"
      thalamic nuclei; functionally distinct. Do not merge.

    - TRAP 3: MIDLINE vs. MEDIODORSAL (the intra-group sub-trap;
      reproduced from the right MD leaf and the right medial nuclear
      group container). The right midline nuclei are a DISTRIBUTED
      limbic/visceral family; the right MD is a DISCRETE prefrontal
      relay. Both project to the PFC, but the midline family's PFC
      projections are part of its broader limbic/visceral role. Do not
      merge.

Functional Mode (family-level synthesis; applies on the right
identically to the left):
    - Limbic and visceral integration: the right midline nuclei
      collectively integrate visceral, affective, and mnemonic signals
      across the right limbic-prefrontal system. The right midline
      family is the right hemisphere's thalamic component of the
      limbic system.
    - Hippocampal relay (reuniens emphasis): the right reuniens is the
      principal thalamic relay between the right hippocampus (CA1,
      subiculum) and the right medial prefrontal cortex; it
      contributes to spatial working memory and to right
      hippocampal-prefrontal communication.
    - Stress, reward, and emotional regulation (PVT emphasis): the
      right PVT (if added) is reciprocally connected with the right
      amygdala, right hypothalamus, and right nucleus accumbens; it
      contributes to stress responses, reward, and emotional
      regulation.
    - Olfactory-limbic integration (paratenial, rhomboidal emphasis):
      the right paratenial and rhomboidal receive olfactory and
      limbic inputs; their specific contributions are less studied
      than the reuniens and PVT.
    See ../../left/medial_nuclear_group/midline_nuclear_group/
    § Functional Mode for the full family-level description.

    FAMILY-LEVEL CLINICAL FACTS (apply on the right identically):
        * RIGHT REUNIENS: implicated in spatial working memory deficits
          in animal models (the right reuniens' contribution to
          right hippocampal-prefrontal communication).
        * RIGHT PVT: implicated in stress and reward dysregulation (in
          animal models of stress, addiction, and affective
          disorders).
        * RIGHT PARATENIAL and RHOMBOIDAL: less characterized
          clinically; the family's "less characterized" members.
        * The right midline family is therefore the right medial
          nuclear group's LEAST CLINICALLY ANCHORED family (contrast
          with the right MD's executive-affective syndrome and the
          right intralaminar family's coma/DBS picture). The reuniens
          and PVT provide the family's clinical anchors; the
          paratenial and rhomboidal are documented as "less
          characterized."

Hormonal Modulation:
    Same as ../../left/medial_nuclear_group/midline_nuclear_group/.
    Minimal; hypothalamic inputs (including from the right
    hypothalamic PVN — the actual endocrine hub, not this group's
    PVT), limbic inputs (right amygdala, right hippocampus), and
    brainstem arousal inputs modulate the family's limbic/visceral
    functions. Not a principal target of the 12 endocrine axes.

Memory Interfaces:
    Same as ../../left/medial_nuclear_group/midline_nuclear_group/.
    Right paratenial reads short_term (limbic state); right reuniens
    reads episodic and short_term (hippocampal relay); right
    rhomboidal reads short_term (limbic state); right PVT reads
    short_term (stress/reward state) and reinforcement_value_based_
    learning (reward/stress integration). Writes nothing directly
    (relay, not encoder).

Model Integration (Gemma-4-E2B):
    No right midline family fragment. Same as
    ../../left/medial_nuclear_group/midline_nuclear_group/ and the
    whole thalamus: the family is a limbic/visceral relay system, not
    a state-emitter. The emotional_valence, episodic, and short_term
    state is carried by the upstream fragments (hypothalamus,
    amygdala, hippocampus).

Children (no children of its own; its members are the right direct
nodes under right/medial_nuclear_group/):
    - The right midline nuclei are documented as direct nodes under
      right/medial_nuclear_group/:
        - paratenial_nucleus/        (delta of the left Pt;
                                        olfactory-limbic)
        - reuniens_nucleus/          (delta of the left Re; hippocampal
                                        relay; family anchor)
        - rhomboidal_nucleus/        (delta of the left Rh;
                                        olfactory-limbic)
        - (paraventricular_nucleus/  (delta of the left PVT if added;
          IF ADDED)                   see Trap 1))
    - This sub-container does NOT have its own left/ and right/
      children; it is a sibling of its own members (same structural
      quirk as on the left).

Notes:
    - Sub-container delta of ../../left/medial_nuclear_group/
      midline_nuclear_group/. Inherits everything structural and
      functional from the left. Do not duplicate.
    - THE STRUCTURAL QUIRK (container + direct nodes as siblings) is
      reproduced above for the right. The right sub-container and its
      right direct nodes are an INTEGRATED STRUCTURE for functional
      purposes, even though the tree hierarchy places them as
      siblings.
    - THE PVT vs. PVN TRAP IS NOW DECLARED AT EIGHT LOCATIONS ACROSS
      THE TREE (the most-reproduced trap by a wide margin):
        (1) posterior/lateral_area/left/posterior_part_of_lateral_
            nucleus/
        (2) posterior/lateral_area/right/posterior_part_of_lateral_
            nucleus/
        (3) tuberal/medial_area/left/arcuate_nucleus/
        (4) tuberal/medial_area/right/arcuate_nucleus/
        (5) thalamus/left/medial_nuclear_group/
        (6) thalamus/right/medial_nuclear_group/
        (7) thalamus/left/medial_nuclear_group/midline_nuclear_group/
        (8) THIS FILE (thalamus/right/medial_nuclear_group/midline_
            nuclear_group/; canonical for the right PVT specifically)
      The redundancy is by design: the trap is the most likely
      conflation in the entire thalamus.
    - BOTH OTHER FAMILY-LEVEL TRAPS are reproduced in abbreviated form;
      the full text is in ../../left/medial_nuclear_group/midline_
      nuclear_group/ and ../../../__init__.py. A contributor entering
      at the right midline sub-container must see them.
    - THE FAMILY-LEVEL CLINICAL FACTS (reuniens spatial working memory;
      PVT stress/reward; paratenial/rhomboidal less characterized) are
      reproduced in abbreviated form; the full family-level synthesis
      is in the left sub-container.
    - NO DIRECT RECIPROCAL EDGES OF ITS OWN: the sub-container is not
      a signaling node; the reciprocal edges are declared in the
      right midline direct-node deltas (paratenial, reuniens,
      rhomboidal, PVT if added). Do not add reciprocal edges to this
      sub-container file.
    - NO FRAGMENT: same as the whole thalamus. The right midline
      family is a limbic relay system, not a state-emitter.
    - THE RIGHT MIDLINE SUB-CONTAINER PAIR IS NOW COMPLETE: with this
      file, the midline sub-container is fully documented on both
      hemispheres — the family-level integration layer is done. The
      right three (or four) direct nuclei are still pending as deltas
      of their left counterparts.
    - Vocabulary used above is defined in Stage 0 files; see
      ../../left/medial_nuclear_group/midline_nuclear_group/ § Notes
      for the full list.
    - Connects upward to diencephalon/thalamus/right/medial_nuclear_
      group/.
"""