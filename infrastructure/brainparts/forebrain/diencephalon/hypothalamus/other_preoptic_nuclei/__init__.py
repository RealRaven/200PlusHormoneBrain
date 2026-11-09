"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.other_preoptic_nuclei
Anatomical Role:
    A catch-all container for preoptic nuclei that are not classified
    under the lateral_area or medial_area preoptic sub-trees. It sits as
    a direct child of hypothalamus/ (not under anterior/) because its
    contents cut across the anterior division's lateral/medial
    compartments and are not cleanly assigned to either.

    The container holds the following named nuclei, each documented
    WITHIN the left/ and right/ hemisphere leaves (not as further
    child nodes):
        - Anteroventral periventricular nucleus (AVPV): a kisspeptin-
          expressing, sexually dimorphic periventricular nucleus. It is
          the principal estrogen-positive-feedback relay to GnRH neurons
          and is the anatomical neighbor of the periventricular preoptic
          nucleus (PeN). The AVPV is the population referenced by the
          "AVPV/PeN continuity edge" in
          lateral_area/*/periventricular_preoptic_nucleus/. Documenting
          it here closes that deferred edge.
        - Anterodorsal preoptic nucleus (ADP): a small vasopressin-
          expressing nucleus adjacent to the AVPV. Modulates fluid
          balance and social behavior.
        - Striohypothalamic nucleus: a small preoptic nucleus receiving
          striatal and limbic inputs; poorly characterized functionally.
        - Ventral preoptic area / lateral preoptic area proper: the
          non-nucleated preoptic region adjacent to the lateral
          preoptic area already documented in lateral_area/*/
          preoptic_area/. The distinction between the LPO (documented
          there) and this ventral preoptic region is anatomical
          adjacency, not duplication.
        - Other small preoptic cell groups: any preoptic nuclei not
          named above and not classified under lateral_area or
          medial_area.

    DISTINCTIONS (critical — preoptic naming collision applies here):
    - This container is NOT the lateral preoptic area
      (lateral_area/*/preoptic_area/) and NOT the medial preoptic area
      (medial_area/*/preoptic_area/). It is the "other" group — the
      nuclei that are neither.
    - The AVPV is DISTINCT from the PeN, but they are ADJACENT kisspeptin
      populations that function as a continuum in the literature. The
      AVPV-PeN edge is a continuity edge, not a duplicate-structure
      warning. Do not merge; do not treat as split structure.
    - The AVPV/PeN naming distinction is the defining trap of this
      container: both are periventricular kisspeptin nuclei, both are
      sexually dimorphic, and both relay estrogen feedback to GnRH. But
      they are anatomically distinct and functionally specialized (AVPV
      = positive feedback/surge; PeN = tonic drive). Do not conflate.

Functional Mode:
    - Estrogen positive feedback (AVPV; primary function): the AVPV is
      the principal anatomical substrate for the estradiol positive
      feedback that triggers the preovulatory GnRH/LH surge. AVPV
      kisspeptin neurons project to GnRH neurons and are activated by
      rising estradiol in the late follicular phase. This is the
      estrogen-positive-feedback complement of the PeN's tonic drive.
    - Sexual dimorphism (AVPV): the AVPV is larger and more
      kisspeptin-dense in females; its dimorphism is the anatomical
      substrate for the female-specific capacity to generate a GnRH
      surge. This is a distinct dimorphism from the INAH-3 dimorphism
      (which is male-larger); do not conflate.
    - Vasopressin and fluid balance (ADP; secondary function): the ADP
      expresses vasopressin and contributes to water-balance regulation
      via projections to the SON/PVN axis. Minor compared with the SON/
      PVN contribution; document as a supporting role.
    - Social behavior (ADP; minor): vasopressinergic projections to
      limbic circuits contribute to social recognition and affiliative
      behavior. Documented as a minor role; not the file's anchor.
    - Striohypothalamic and ventral preoptic (poorly characterized):
      these regions receive striatal and limbic inputs, but their
      specific functions are not well established. Document them
      factually without overclaiming; do not invent functional roles.
    - The container is therefore NOT a single functional unit — it is a
      collection of small preoptic nuclei whose unifying property is
      that they are preoptic and not classified elsewhere. Do not treat
      the file as a coherent hub; treat it as a catalogue.

Hormonal Modulation (container-level summary; per-nucleus wiring in
children):
    - AVPV: estradiol (positive feedback; the defining modulator);
      kisspeptin (intrinsic); GABA, glutamate (intrinsic); SCN
      vasopressin (circadian gating of the surge); progesterone
      (modulatory).
    - ADP: vasopressin (output); estradiol (modulatory); osmotic input
      via OVLT/SFO (indirect).
    - Striohypothalamic and ventral preoptic: poorly characterized;
      document estradiol and limbic input as presumed, not established.
    - Direction summary: estradiol ↑ AVPV kisspeptin activity (surge);
      SCN vasopressin ↑ AVPV gating (circadian restriction); ADP
      outputs vasopressin. These directions are the actionable content.

Memory Interfaces (container-level summary):
    - AVPV: reads short_term (current estradiol level, circadian phase),
      episodic (cycle history), emotional_valence (stress suppression
      of the surge). Writes none directly.
    - ADP: reads short_term (osmotic state). Writes none directly.
    - The striohypothalamic and ventral preoptic regions have no
      documented memory interfaces; do not invent them.
    - Store schemas are defined in memory/stores/.

Model Integration (Gemma-4-E2B):
    - No container-level prompt fragment. The AVPV's contribution is
      documented as a CONSTITUENT INPUT to the anterior-division
      reproductive fragment (aggregated with PeN + MPN + MnPO), and the
      ADP's vasopressin is upstream of the SON/PVN fluid fragment.
      Emitting a separate container-level fragment would double-count
      both signals.
    - The AVPV fragment role: the parent preoptic sub-tree
      (medial_area/*/preoptic_area/) and the PeN leaf
      (lateral_area/*/periventricular_preoptic_nucleus/) already cover
      the estrogen-positive-feedback state and the reproductive mode;
      the AVPV's kisspeptin activity is aggregated into that state.
      Do not add a separate AVPV fragment.
    - The ADP fragment role: the SON/PVN fluid fragment
      (aggregated at the anterior-division level) carries the state.
      Do not add a separate ADP fragment.
    - Guardrails: the reproductive fragment (carried by the MPN/PeN
      leaves) carries the standard "bias not impairment" clause. The
      container does not add a new guardrail.

Children (one child pair — each hemisphere's file carries all the
named nuclei):
    - left/    ★ Left hemisphere. Full leaf (not a delta). Documents
                 the left AVPV, left ADP, left striohypothalamic
                 nucleus, left ventral preoptic area, and any other
                 left preoptic cell groups not classified elsewhere.
                 The authoritative file for this container.
    - right/   ★ Right hemisphere. Delta mirror of left/, differing
                 only in the right-side reciprocal edges (right PeN,
                 right SON/PVN, right OVLT/SFO). No functional
                 asymmetry documented.

Notes:
    - Tier 1 catch-all container with a single child pair. Both left/
      and right/ are full leaves — the catch-all content is not
      reducible to a delta.
    - The preoptic collision applies here: this container is the "other"
      preoptic group, distinct from lateral_area/*/preoptic_area/ and
      medial_area/*/preoptic_area/. Reproduce the warning at every
      level where it applies.
    - The AVPV-PeN continuity edge is now closed by this container:
      lateral_area/*/periventricular_preoptic_nucleus/ declared the
      continuity edge (see its Notes); this container documents the
      AVPV side. Both files must declare the edge for the Stage 4
      audit to resolve it. Document the reciprocity explicitly in
      left/__init__.py.
    - The AVPV's sexual dimorphism is distinct from the INAH-3 dimorphism
      (AVPV is larger in females; INAH-3 is larger in males). Do not
      conflate; the dimorphism literatures are separate.
    - Do not create AVPV/, ADP/, striohypothalamic_nucleus/, or
      ventral_preoptic_area/ as separate child nodes. They are
      documented within the left/ and right/ hemisphere leaves. Same
      convention as mammillary_bodies/left|right carrying MM and LM
      within a single file.
    - The container does not hold a "left AVPV only" or "right AVPV
      only" content: both hemispheres contain all the named nuclei,
      and the left/right split is anatomical mirroring, not functional
      subdivision.
    - The striohypothalamic and ventral preoptic regions are poorly
      characterized. Document them factually; do not invent functional
      roles.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, kisspeptin, progesterone),
      05_* (GABA, glutamate), 07_* (fluid, vasopressin, angiotensin II,
      ANP), 10_* (circadian, SCN); memory/stores/ (short_term, episodic,
      emotional_valence, temporal_sequence_learning); gateway/.
    - Reciprocal connections to enforce in Stage 4:
        * other_preoptic_nuclei/left|right (AVPV) ↔
          lateral_area/left|right/periventricular_preoptic_nucleus
          (AVPV/PeN continuity edge; kisspeptin continuum; the critical
          edge this container closes).
        * other_preoptic_nuclei/left|right (AVPV) ↔
          hypothalamus/anterior/medial_area/left|right/preoptic_area/
          medial_preoptic_nucleus (adjacent preoptic GnRH-regulatory
          nodes).
        * other_preoptic_nuclei/left|right (AVPV) ↔
          hypothalamus/anterior/medial_area/left|right/
          suprachiasmatic_nucleus (SCN → AVPV circadian gating of the
          surge).
        * other_preoptic_nuclei/left|right (AVPV) ↔
          hypothalamus/tuberal/medial_area/left|right/arcuate_nucleus
          (kisspeptin KNDy input; the arcuate-to-AVPV kisspeptin
          network).
        * other_preoptic_nuclei/left|right (ADP) ↔
          hypothalamus/anterior/medial_area/left|right/supraoptic_nucleus
          and paraventricular_nucleus (vasopressin co-regulation).
        * other_preoptic_nuclei/left|right (ADP) ↔
          lamina_terminalis/vascular_organ_of_lamina_terminalis
          (OVLT; osmotic input).
        * other_preoptic_nuclei/left|right (ADP) ↔
          hypothalamus/subfornical_organ (SFO; angiotensin II input).
    - Connects upward to hypothalamus/.
"""