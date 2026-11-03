"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.left.preoptic_area.medial_preoptic_nucleus.inah_2
Anatomical Role:
    Interstitial nucleus of the anterior hypothalamus 2 (INAH-2). One of
    four INAH nuclei embedded within the medial preoptic nucleus (MPN);
    a very small collection of neurons in the left hemisphere, with
    sexually dimorphic volume. Human INAH-2 is intermediate in
    characterization between INAH-1 (less studied) and INAH-3 (the
    human homologue of the rodent SDN-POA, most studied). INAH-2 is
    typically studied as part of the INAH series for sexually dimorphic
    nucleus comparisons.

    INAH-2 is a COMPONENT of the MPN, not a separate anatomical
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
    - Sexually dimorphic volume: INAH-2 volume differs by sex in
      humans, with INAH-2 typically reported as larger in males
      (effect size comparable to INAH-1 and smaller than INAH-3 in most
      reports). The functional consequence of this volume difference in
      humans is not established.
    - Organizational hormonal effect: developmental testosterone
      (aromatized to estradiol locally) is the classic organizing
      signal for INAH-2 volume in the rodent homologue. This is
      documented as the developmental modulator; it does not imply an
      activational endocrine role for INAH-2 in adulthood.
    - Activational role: not established. Unlike the MPN broadly
      (which has clear activational roles in maternal and sexual
      behavior), INAH-2's specific contribution in adulthood is
      uncertain. Do not invent one.
    - Membership in the MPN: INAH-2 is one component of the MPN's
      sexually dimorphic circuitry. The MPN's functional roles
      (maternal, sexual, parental, GnRH-regulatory) are documented in
      the parent leaf; INAH-2's specific contribution to them is not
      separable from the surrounding MPN in the current literature.

Hormonal Modulation:
    - Testosterone (developmental; aromatized to estradiol locally):
      the organizing signal for INAH-2 volume. Organizational only.
    - Estradiol (developmental): the active aromatized metabolite;
      organizational only.
    - Activational hormonal modulation: not established. Do not list
      adult hormonal modulators for INAH-2 beyond what the parent MPN
      already documents.

Memory Interfaces:
    None. INAH-2 is a structural component with no documented
    episodic, semantic, or reinforcement-learning interface in its own
    right. The parent MPN's memory interfaces cover the broader
    reproductive-behavior circuit; do not duplicate them here.

Model Integration (Gemma-4-E2B):
    None. INAH-2 does not emit its own prompt fragment. The
    reproductive/parental fragment is emitted by the parent MPN
    (../__init__.py) and aggregated with the PeN and MnPO contributions
    at the anterior-division level. Do not add an INAH-2 fragment.

Reciprocal Connections:
    - ↔ ../ (parent MPN; INAH-2 is a component of the MPN).
    - ← hypothalamus/anterior/medial_area/left/preoptic_area
      (developmental and organizational context).
    No other reciprocal edges are documented for INAH-2; do not invent
    them. Add edges only if the literature later establishes them.

Notes:
    - Tier 2 organ-flavored leaf. Short by design. INAH-2 has thin
      functional literature; do not over-write it. Same template as
      inah_1/; this file is the pattern for inah_4/ as well (also very
      short). inah_3/ is slightly longer (SDN-POA homologue role).
    - No structural-identity trap and no fragment. The preoptic
      collision and MnPO disambiguation are reproduced only in
      abbreviated form because INAH-2's function is not the main
      content of the file.
    - Sex differences: documented factually (volume, organizational
      testosterone) without claiming functional consequences that the
      literature does not establish. Strictly descriptive, same as
      inah_1/.
    - Do not invent activational endocrine roles for INAH-2. The
      literature does not support them.
    - Vocabulary used above is defined in Stage 0 files:
      chemicals_hormones/01_* (HPG, estradiol, testosterone); memory/
      stores/; gateway/.
    - Connects upward to medial_preoptic_nucleus/.
"""