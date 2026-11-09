"""
Package: infrastructure.brainparts.forebrain.diencephalon.hypothalamus.anterior.medial_area.right.preoptic_area.medial_preoptic_nucleus.inah_4
Anatomical Role:
    Right hemisphere of the interstitial nucleus of the anterior
    hypothalamus 4 (INAH-4). Same very small, sexually dimorphic
    component of the medial preoptic nucleus (MPN) as ../left/, mirrored
    to the right hemisphere. Frequently grouped with INAH-3 in human
    studies, but a distinct nucleus with its own volume literature. See
    ../left/__init__.py for the full anatomical description and the
    "component of MPN, not a separate structure" framing.

    Reproduced notes (apply here and to sibling INAH):
    - This node is inside the MEDIAL preoptic area, distinct from
      lateral_area/right/preoptic_area/lateral_preoptic_nucleus/. The
      preoptic collision applies.
    - The "MnPO" acronym (median_preoptic_nucleus/, the sibling of the
      MPN) is not the ventrolateral sleep-active "MnPO" of the LPO.
      Do not confuse the two.

    Reproduced DISTINCTION FROM INAH-3 (the defining trap for INAH-4):
    INAH-4 is often grouped with INAH-3 in human studies, but the
    grouping is a reporting convention, not an identity. INAH-3 has
    distinct functional literature (rodent SDN-POA homologue; sexual
    behavior; PAG/VTA/medial amygdala projections). INAH-4 does NOT
    inherit that content. Do not copy INAH-3's PAG/VTA/amygdala
    projections into this file, and do not claim INAH-4-specific
    sexual-behavior functional content that the literature does not
    establish for INAH-4 separately.

Functional Mode:
    Same as ../left/. Sexually dimorphic volume (effect size comparable
    to INAH-3 in some series; smaller literature); presumed
    organizational testosterone (aromatized to estradiol) by analogy
    with INAH-3, evidence weaker; activational role not established for
    INAH-4 specifically; no INAH-4-specific projections distinct from
    the surrounding MPN; membership in the MPN's sexually dimorphic
    circuitry. No documented functional asymmetry between left and
    right INAH-4. Do not fabricate one. See ../left/__init__.py
    § Functional Mode.

Hormonal Modulation:
    Same as ../left/. Testosterone and estradiol, developmental
    (organizational) — presumed, by analogy with INAH-3; evidence
    weaker. Do not inherit INAH-3's activational estradiol/testosterone/
    progesterone roles. See ../left/__init__.py § Hormonal Modulation.

Memory Interfaces:
    None. Same as ../left/. INAH-4 has no documented memory interface in
    its own right; the parent MPN's memory interfaces cover the broader
    reproductive-behavior circuit.

Model Integration (Gemma-4-E2B):
    None. Same as ../left/. INAH-4 does not emit its own prompt
    fragment. The reproductive/parental fragment is emitted by the
    parent MPN (../../__init__.py) and aggregated with the PeN and MnPO
    contributions at the anterior-division level. Do not add an INAH-4
    fragment.

Reciprocal Connections:
    - ↔ ../ (parent right MPN; INAH-4 is a component of the MPN).
    - ← hypothalamus/anterior/medial_area/right/preoptic_area
      (developmental and organizational context).
    No other reciprocal edges are documented for INAH-4; do not invent
    them. Do NOT copy INAH-3's right-side PAG/VTA/medial amygdala edges
    into this file. Add edges only if the literature later establishes
    INAH-4-specific projections.

Notes:
    - Delta file of ../left/. Not a full leaf. Do not duplicate.
    - Tier 2 organ-flavored delta. Short by design. This is the LAST
      INAH delta; the INAH family is complete once this file exists:
      four left leaves + four right deltas.
    - The DISTINCTION FROM INAH-3 paragraph is the most important
      content in this delta. It prevents the grouping convention from
      leaking INAH-3's projection set and functional framing into
      INAH-4 on the right, just as it does on the left.
    - No structural-identity trap, no fragment, no memory interface,
      no independent edges beyond the two above. The file is
      deliberately minimal — the left counterpart carries the content.
    - Sex differences: documented factually on the left; not repeated
      here. Same "strictly descriptive" stance applies on the right,
      and especially important given the frequent grouping with INAH-3
      in the sexual-difference literature.
    - Vocabulary used above is defined in Stage 0 files; see
      ../left/__init__.py § Notes for the full list.
    - Connects upward to medial_preoptic_nucleus/ (right).
"""