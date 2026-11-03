"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.preoptic_area.medial_preoptic_nucleus.inah_3
Anatomical Role:
    Interstitial nucleus of the anterior hypothalamus 3 (INAH-3). The
    human homologue of the rodent sexually dimorphic nucleus of the
    preoptic area (SDN-POA), and the most-studied of the four INAH
    nuclei. It is a small collection of neurons embedded within the
    medial preoptic nucleus (MPN) in the left hemisphere, with a
    pronounced, reliably replicated sexually dimorphic volume: INAH-3
    is larger in males than in females, with the sex difference
    established by the late perinatal period and stable into adulthood.

    INAH-3 is a COMPONENT of the MPN, not a separate anatomical
    structure. Do not flatten it into a sibling of the MPN, and do not
    merge it into the MPN's main file.

    Reproduced notes (apply here and to sibling INAH):
    - This node is inside the MEDIAL preoptic area, distinct from
      lateral_area/*/preoptic_area/lateral_preoptic_nucleus/ (the
      VLPO-adjacent sleep nucleus). The preoptic collision applies.
    - The "MnPO" acronym (median_preoptic_nucleus/, the sibling of the
      MPN) is not the ventrolateral sleep-active "MnPO" of the LPO.
      Do not confuse the two.

Functional Mode:
    - Sexually dimorphic volume (the defining feature): INAH-3 volume
      is approximately 2-3× larger in males than in females in most
      human post-mortem series, making it the most consistently
      replicated sexually dimorphic brain structure. The volume
      difference is established by the perinatal testosterone surge
      and is stable thereafter.
    - Sexual behavior (rodent homologue, strongest evidence): in
      rodents, the SDN-POA (the homologue) projects to the medial
      amygdala and the periaqueductal gray, and to the ventral
      tegmental area, and is required for male sexual behavior
      (mounting, intromission, ejaculation) and for female sexual
      receptivity. Lesions of the SDN-POA impair male sexual behavior.
      This is the principal functional evidence for the nucleus.
    - Sexual behavior (human, weaker evidence): INAH-3 volume has been
      examined in relation to sexual orientation in a small number of
      studies with mixed and contested results. The functional
      significance of INAH-3 volume differences in humans is NOT
      established. Document the literature; do not claim a functional
      role that the human data do not support.
    - Projections (rodent homologue): MPN/INAH-3 → periaqueductal gray
      (sexual behavior motor patterns) and → ventral tegmental area
      (reproductive motivation and reward). These are the projections
      that INAH-3 specifically (unlike INAH-1/2/4) is associated with
      in the rodent literature.
    - Activational role (rodent): estradiol and testosterone activate
      INAH-3/SDN-POA neurons to drive sexual behavior. This is the
      clearest activational endocrine role in the INAH series.
    - Membership in the MPN: INAH-3 is the sexually dimorphic
      component of the MPN most closely linked to sexual behavior.
      The MPN's broader roles (maternal, parental, GnRH-regulatory)
      are documented in the parent leaf; INAH-3's specific contribution
      is the sexual-behavior component.

Hormonal Modulation:
    - Testosterone (developmental; aromatized to estradiol locally):
      the organizing signal for INAH-3 volume. The perinatal testosterone
      surge establishes the male-typical volume; organizational only.
    - Estradiol (developmental): the active aromatized metabolite;
      organizational only.
    - Estradiol (activational, rodent): activates INAH-3/SDN-POA
      neurons to drive male and female sexual behavior. The strongest
      activational role in the INAH series.
    - Testosterone (activational, rodent): aromatized to estradiol in
      the MPN/INAH-3 to activate male sexual behavior.
    - Progesterone (activational, female, rodent): facilitates sexual
      receptivity via MPN/INAH-3 circuitry.
    - Direction summary: perinatal testosterone ↑ INAH-3 volume
      (organizational); adult estradiol ↑ INAH-3 activity (activational,
      rodent); progesterone (female, rodent) ↑ INAH-3-mediated
      receptivity. Do not extrapolate activational roles to humans
      where the data are not established.

Memory Interfaces:
    - Reads (rodent homologue; human data not established):
        * short_term: current reproductive-hormonal state (estradiol,
          testosterone, progesterone levels).
        * reinforcement_value_based_learning: reproductive outcomes
          (mating success) feed back into reproductive-context value
          learning.
        * emotional_valence: stress context; chronic stress suppresses
          INAH-3-mediated sexual behavior.
    - Writes: none directly. INAH-3 modulates the reproductive-behavior
      state; it does not write stored content.
    - These interfaces are inherited from the parent MPN; do not
      duplicate them as INAH-3-specific circuits. The "rodent homologue;
      human data not established" caveat is essential.

Model Integration (Gemma-4-E2B):
    None. INAH-3 does not emit its own prompt fragment. The
    reproductive/parental fragment is emitted by the parent MPN
    (../__init__.py) and aggregated with the PeN and MnPO contributions
    at the anterior-division level. Do not add an INAH-3 fragment.
    The sexual-behavior component is documented functionally and is
    carried within the parent MPN's reproductive fragment, not as a
    separate INAH-3 fragment.

Reciprocal Connections (rodent homologue; human data weaker):
    - ↔ ../ (parent MPN; INAH-3 is a component of the MPN).
    - → midbrain/tegmentum/periaqueductal_gray (sexual behavior motor
      patterns; PAG is midline-adjacent — verify). This is the
      INAH-3-specific projection in the rodent literature.
    - → midbrain/tegmentum/ventral_tegmental_area (reproductive
      motivation and reward; VTA is midline-adjacent — verify). This is
      the INAH-3-specific projection in the rodent literature.
    - ↔ telencephalon/cerebral_hemispheres/left/subcortical/
      medial_temporal_lobe/amygdala (reproductive and social context;
      medial amygdala projection to the MPN/INAH-3 in rodents;
      left-side).
    - ← hypothalamus/anterior/medial_area/left/preoptic_area
      (developmental and organizational context).
    Do not list additional edges for INAH-3 beyond the above unless the
    literature establishes them. The PAG and VTA projections are the
    distinguishing edges for INAH-3 relative to INAH-1/2/4.

Notes:
    - Tier 2 organ-flavored leaf, slightly longer than INAH-1/2 (~70
      lines vs ~45) because the literature genuinely is. Still not a
      full Tier 1 leaf: INAH-3 is a component of the MPN with a
      volume-led identity.
    - This is the only INAH with genuine functional literature beyond
      volume: sexual behavior (rodent, strong; human, weak), PAG/VTA
      projections (rodent). The file documents the literature and is
      explicit about the strength of evidence in each case.
    - Sex differences: INAH-3 is the most politically charged INAH
      because of the sexual-orientation literature. The file is
      STRICTLY DESCRIPTIVE on this point: it notes that the
      sexual-orientation literature exists, that it is small and mixed,
      and that the functional significance of INAH-3 volume in humans
      is NOT established. Do not overclaim, do not editorialize.
    - No structural-identity trap. INAH-3 is a component of the MPN;
      not a split structure. Preoptic collision and MnPO disambiguation
      reproduced in abbreviated form.
    - Do not add a fragment, do not add memory writes, do not add
      edges beyond the PAG/VTA/medial amygdala edges. INAH-3 is a
      component of the MPN, not an independent circuit node.
    - The inah_3/right/ delta should follow this shape with the
      right-side volume note and right-side PAG/VTA/amygdala edges.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, testosterone,
      progesterone); memory/stores/; gateway/.
    - Connects upward to medial_preoptic_nucleus/.
"""