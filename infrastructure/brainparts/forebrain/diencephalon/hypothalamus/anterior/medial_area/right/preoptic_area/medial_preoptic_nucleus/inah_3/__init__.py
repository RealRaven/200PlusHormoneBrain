"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.preoptic_area.medial_preoptic_nucleus.inah_3
Anatomical Role:
    Right hemisphere of the interstitial nucleus of the anterior
    hypothalamus 3 (INAH-3). The human homologue of the rodent sexually
    dimorphic nucleus of the preoptic area (SDN-POA), mirrored to the
    right hemisphere. Same small collection of neurons embedded within
    the medial preoptic nucleus (MPN), with the same pronounced,
    reliably replicated sexually dimorphic volume (2–3× larger in males
    than in females in most post-mortem series). See
    ../left/__init__.py for the full anatomical description and the
    "component of MPN, not a separate structure" framing.

    Reproduced notes (apply here and to sibling INAH):
    - This node is inside the MEDIAL preoptic area, distinct from
      lateral_area/right/preoptic_area/lateral_preoptic_nucleus/. The
      preoptic collision applies.
    - The "MnPO" acronym (median_preoptic_nucleus/, the sibling of the
      MPN) is not the ventrolateral sleep-active "MnPO" of the LPO.
      Do not confuse the two.

Functional Mode:
    Same as ../left/. Sexually dimorphic volume (the defining feature);
    sexual behavior (rodent homologue: strong evidence via SDN-POA
    lesions and PAG/VTA projections; human: weak, contested
    literature); activational estradiol and testosterone roles (rodent);
    membership in the MPN's sexually dimorphic circuitry. No documented
    functional asymmetry between left and right INAH-3. Do not fabricate
    one. See ../left/__init__.py § Functional Mode.

Hormonal Modulation:
    Same as ../left/. Testosterone and estradiol, developmental
    (organizational) — perinatal testosterone → estradiol establishes
    the male-typical volume. Estradiol and testosterone, activational
    (rodent) — activates INAH-3/SDN-POA neurons for sexual behavior.
    Progesterone (activational, female, rodent) — facilitates sexual
    receptivity. Do not extrapolate activational roles to humans where
    the data are not established. See ../left/__init__.py § Hormonal
    Modulation.

Memory Interfaces:
    Same as ../left/. Reads short_term (reproductive-hormonal state),
    reinforcement_value_based_learning (reproductive outcomes),
    emotional_valence (stress suppression of sexual behavior). Rodent
    homologue; human data not established. No stored content writes.
    See ../left/__init__.py § Memory Interfaces.

Model Integration (Gemma-4-E2B):
    None. INAH-3 does not emit its own prompt fragment. The
    reproductive/parental fragment is emitted by the parent MPN
    (../../__init__.py) and aggregated with the PeN and MnPO
    contributions at the anterior-division level. Do not add an INAH-3
    fragment. See ../left/__init__.py § Model Integration.

Reciprocal Connections (right-side; rodent homologue; human data
weaker; do not duplicate the left-side edges in ../left/):
    - ↔ ../ (parent right MPN; INAH-3 is a component of the MPN).
    - → midbrain/tegmentum/periaqueductal_gray (sexual behavior motor
      patterns; PAG is midline-adjacent — verify). INAH-3-specific
      projection in the rodent literature.
    - → midbrain/tegmentum/ventral_tegmental_area (reproductive
      motivation and reward; VTA is midline-adjacent — verify).
      INAH-3-specific projection in the rodent literature.
    - ↔ telencephalon/cerebral_hemispheres/right/subcortical/
      medial_temporal_lobe/amygdala (reproductive and social context;
      medial amygdala projection to MPN/INAH-3 in rodents; right-side).
    - ← hypothalamus/anterior/medial_area/right/preoptic_area
      (developmental and organizational context).
    Do not list additional edges for INAH-3 beyond the above unless the
    literature establishes them. The PAG and VTA projections are the
    distinguishing edges for INAH-3 relative to INAH-1/2/4; they must be
    mirrored here so the audit resolves the right-side target.

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - Tier 2 organ-flavored delta, slightly longer than the INAH-1/2
      deltas (~55 lines vs ~45) because INAH-3 has distinguishing
      projections (PAG, VTA, medial amygdala) that must be mirrored on
      the right. This is the only INAH delta with meaningful content
      beyond the two-edge minimum.
    - Sex differences: INAH-3 is the most politically charged INAH
      because of the sexual-orientation literature. The file is
      STRICTLY DESCRIPTIVE on this point, same as ../left/: the
      literature exists, it is small and mixed, and the functional
      significance of INAH-3 volume in humans is NOT established. Do
      not overclaim, do not editorialize, do not repeat this on the
      right with any stronger framing than the left.
    - No structural-identity trap. INAH-3 is a component of the MPN;
      not a split structure. Preoptic collision and MnPO disambiguation
      reproduced in abbreviated form.
    - Midline targets (PAG, VTA) are flagged with "verify" so Stage 4
      does not force a hemisphere split on structures that are not
      hemisphere-split in the tree. The right medial amygdala is
      hemisphere-split and requires the right-side edge explicitly.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to medial_preoptic_nucleus/ (right).
"""