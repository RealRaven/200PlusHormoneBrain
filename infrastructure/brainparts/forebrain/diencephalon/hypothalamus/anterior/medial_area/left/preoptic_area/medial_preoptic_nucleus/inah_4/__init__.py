"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.preoptic_area.medial_preoptic_nucleus.inah_4
Anatomical Role:
    Interstitial nucleus of the anterior hypothalamus 4 (INAH-4). The
    fourth and last of the four INAH nuclei embedded within the medial
    preoptic nucleus (MPN); a very small collection of neurons in the
    left hemisphere, with sexually dimorphic volume. INAH-4 is
    frequently grouped with INAH-3 in human studies (both are in the
    posterior part of the INAH series and both have more consistent
    volume measurements than INAH-1/2), but it is a distinct nucleus
    with its own volume literature.

    INAH-4 is a COMPONENT of the MPN, not a separate anatomical
    structure. Do not flatten it into a sibling of the MPN, and do not
    merge it into the MPN's main file.

    Reproduced notes (apply here and to sibling INAH):
    - This node is inside the MEDIAL preoptic area, distinct from
      lateral_area/*/preoptic_area/lateral_preoptic_nucleus/ (the
      VLPO-adjacent sleep nucleus). The preoptic collision applies.
    - The "MnPO" acronym (median_preoptic_nucleus/, the sibling of the
      MPN) is not the ventrolateral sleep-active "MnPO" of the LPO.
      Do not confuse the two.

    DISTINCTION FROM INAH-3 (do not transfer INAH-3 content here):
    INAH-4 is often grouped with INAH-3 in human studies, but the
    grouping is a reporting convention, not an identity. INAH-3 has
    distinct functional literature (rodent SDN-POA homologue; sexual
    behavior; PAG/VTA/medial amygdala projections). INAH-4 does NOT
    inherit that content. Do not copy INAH-3's PAG/VTA/amygdala
    projections into this file, and do not claim INAH-4-specific
    sexual-behavior functional content that the literature does not
    establish for INAH-4 separately.

Functional Mode:
    - Sexually dimorphic volume: INAH-4 volume differs by sex in
      humans, with INAH-4 typically reported as larger in males. The
      effect size is comparable to INAH-3 in some series but the
      literature is smaller; the grouping with INAH-3 is because both
      are posterior-part INAH and both have more consistent volume
      measurements than INAH-1/2. The functional consequence of this
      volume difference in humans is not established.
    - Organizational hormonal effect: developmental testosterone
      (aromatized to estradiol locally) is the presumed organizing
      signal for INAH-4 volume in the rodent homologue, by analogy
      with INAH-3. The evidence is weaker for INAH-4 specifically than
      for INAH-3. Document as presumed organizational, not established.
    - Activational role: not established for INAH-4 specifically. Do
      not inherit INAH-3's activational roles. If the literature later
      establishes INAH-4-specific activational roles, add them; until
      then, say "not established."
    - Projections: no INAH-4-specific projections are well established
      in the human or rodent literature distinct from the surrounding
      MPN. Do not copy INAH-3's PAG/VTA/amygdala projections into this
      file.
    - Membership in the MPN: INAH-4 is one component of the MPN's
      sexually dimorphic circuitry. The MPN's functional roles
      (maternal, sexual, parental, GnRH-regulatory) are documented in
      the parent leaf; INAH-4's specific contribution to them is not
      separable from the surrounding MPN in the current literature.

Hormonal Modulation:
    - Testosterone (developmental; aromatized to estradiol locally):
      the presumed organizing signal for INAH-4 volume, by analogy
      with INAH-3. Organizational only; evidence weaker than for
      INAH-3.
    - Estradiol (developmental): the active aromatized metabolite;
      organizational only.
    - Activational hormonal modulation: not established for INAH-4
      specifically. Do not inherit INAH-3's activational estradiol/
      testosterone/progesterone roles.

Memory Interfaces:
    None. INAH-4 is a structural component with no documented
    episodic, semantic, or reinforcement-learning interface in its own
    right. The parent MPN's memory interfaces cover the broader
    reproductive-behavior circuit; do not duplicate them here.

Model Integration (Gemma-4-E2B):
    None. INAH-4 does not emit its own prompt fragment. The
    reproductive/parental fragment is emitted by the parent MPN
    (../__init__.py) and aggregated with the PeN and MnPO contributions
    at the anterior-division level. Do not add an INAH-4 fragment.

Reciprocal Connections:
    - ↔ ../ (parent MPN; INAH-4 is a component of the MPN).
    - ← hypothalamus/anterior/medial_area/left/preoptic_area
      (developmental and organizational context).
    No other reciprocal edges are documented for INAH-4; do not invent
    them. Do NOT copy INAH-3's PAG/VTA/medial amygdala edges into this
    file. Add edges only if the literature later establishes
    INAH-4-specific projections.

Notes:
    - Tier 2 organ-flavored leaf. Short by design. INAH-4 has thinner
      INAH-4-specific literature than INAH-3; do not over-write it and
      do not transfer INAH-3's content. This is the last INAH leaf;
      once inah_4/right/ is drafted, the INAH family is complete.
    - No structural-identity trap and no fragment. The preoptic
      collision and MnPO disambiguation are reproduced only in
      abbreviated form because INAH-4's function is not the main
      content of the file.
    - Sex differences: documented factually (volume, presumed
      organizational testosterone) without claiming functional
      consequences that the literature does not establish. Strictly
      descriptive, same as inah_1/ and inah_2/ — and especially
      important here because of the frequent grouping with INAH-3 in
      the sexual-difference literature. Do not inherit that framing.
    - Grouping-with-INAH-3 is a reporting convention, not an identity.
      The DISTINCTION FROM INAH-3 paragraph is the most important
      content in this file: it prevents a future contributor from
      treating INAH-4 as a synonym for INAH-3 or from copying INAH-3's
      PAG/VTA/amygdala projections into this leaf.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, testosterone); memory/
      stores/; gateway/.
    - Connects upward to medial_preoptic_nucleus/.
"""