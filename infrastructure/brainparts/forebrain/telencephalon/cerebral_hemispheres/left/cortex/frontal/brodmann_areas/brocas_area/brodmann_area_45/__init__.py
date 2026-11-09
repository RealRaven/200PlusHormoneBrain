"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brocas_area.brodmann_area_45
=================================================================================================================================

Brodmann area 45 (pars triangularis) — left hemisphere.

A CONSTANT + CONFIG HOLDER inside the brocas_area nested registry
sub-package. No compute, no state, no lifecycle. Declares the canonical
identity of area 45, says which compute sub-region owns it, and supplies
the per-area weights that the owning sub-region's `encode()` reads. It
defines no classes and no functions; the public surface is the exports
listed under "EXPORTS".

If you are looking for the computation area 45 participates in, it lives
in
`.../frontal/cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/`
— area 45 is the pars triangularis component of Broca's area, and
Broca's area is a Brodmann-area-level label on a sub-region of VLPFC.
This package is the *label*, not the *agent*.

If you are looking for the other half of Broca's area, it is
`brodmann_area_44/` (pars opercularis), in the same brocas_area
sub-package. The two are the two halves of a single coupled unit, and
the coupling is expressed through their `brocas_weight` shares and their
`to_area_44` / `to_area_45` connectivity priors, not through imports.

IDENTITY
--------
    AREA_ID    = 45
    NAME       = "Brodmann area 45 (pars triangularis)"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "ventrolateral_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = "brocas_area"

The SYSTEM list, SUB_REGION field, and GROUPING field are documented in
detail in the area-44 docstring. In brief: SYSTEM is a list uniformly
across the frontal registry; SUB_REGION names the specific prefrontal
sub-region (VLPFC) that imports this area's config; GROUPING names the
named sub-grouping (brocas_area) that this area belongs to, so that
VLPFC's language-production pathway can filter by it rather than
hardcoding {44, 45}. Area 45 is the sibling of area 44 and shares all
four fields — anatomy and grouping do not lateralise within Broca's
area, only weights do.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 45 (pars triangularis)",
        "system": "prefrontal_cortex",
        "sub_region": "ventrolateral_prefrontal_cortex",
        "grouping": "brocas_area",
        "location": "anterior part of the inferior frontal gyrus, "
                    "rostral to area 44 and continuing to the anterior "
                    "horizontal ramus of the lateral sulcus",
        "cytoarchitecture": "granular cortex; more heavily granulated "
                            "than area 44, with a prominent layer IV — "
                            "the cytoarchitectonic signature of a more "
                            "associative (less motor) region",
        "notes": (
            "Pars triangularis — the anterior half of Broca's area, and "
            "the more associative (less motor) of the two areas. Its "
            "cytoarchitecture is more granular than area 44's: it sits "
            "further from the motor strip and its connectivity is more "
            "strongly to posterior association cortex (middle temporal "
            "gyrus, superior temporal sulcus) than to motor cortex. "
            "Functionally it is the lexical and semantic component of "
            "language production: selecting which words to say, "
            "integrating grammatical structure, and mapping semantic "
            "content onto the lexical items that area 44 will then "
            "articulate. The distinction from area 44 is between 'what "
            "to say' (45) and 'how to say it' (44). On the left, area "
            "45 carries the dominant lexical-selection role; on the "
            "right, its role is the prosodic-lexical interface — "
            "matching prosodic contour to affective content and "
            "producing the melodic structure of speech, with a much "
            "smaller lexical-selection contribution. The left/right "
            "split is directional, not complementary — the right's "
            "area 45 is prosody-anchored, not 'the left's at reduced "
            "weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 45's config has three parts: (a) its share within Broca's area's
contribution to VLPFC, summing to 1.0 with area 44's share; (b) its
feature emphases within that contribution; and (c) its connectivity
priors to partner structures.

    LEFT_CONFIG = {
        # ---- share within Broca's area's contribution to VLPFC ----
        # 44 : 45  sum to 1.0. On the left, 45 takes the SMALLER share
        # (0.45) — the left's language production is more
        # articulatory-dominant than lexical-selection-dominant, so 44
        # carries the larger share. On the right the split is the
        # mirror (44: 0.45, 45: 0.55) because the right's Broca's-area
        # contribution is more prosody-anchored and 45 carries the
        # prosodic-lexical interface there.
        "brocas_weight":          0.45,   # area 44: 0.55

        # ---- feature emphases inside this area's contribution ----
        # LEFT bias: strong lexical-selection and syntactic weights
        # (the core of left-lateralised language production); the
        # phonological and articulatory weights are area 44's business
        # and are present here only at moderate levels (the interface
        # between lexical selection and phonological encoding);
        # prosodic is the right hemisphere's role and is tiny here.
        "phonological":           0.45,   # interface with 44's
                                          # phonological encoding
        "articulatory":           0.25,   # area 44's business, small here
        "lexical_selection":      0.80,   # the left's area-45 anchor
                                          # feature — word selection
        "prosodic":               0.15,   # right hemisphere's role, tiny
                                          # here
        "syntactic":              0.70,   # grammatical structure
                                          # integration — stronger here
                                          # than in area 44
        "verbal_working_memory":  0.45,   # contribution to the
                                          # phonological loop buffer;
                                          # larger than area 44's because
                                          # lexical selection requires
                                          # holding candidate words in
                                          # mind

        # ---- connectivity priors to partner structures ----
        "to_primary_motor":       0.35,   # lower than area 44's 0.75 —
                                          # the output path goes via
                                          # area 44
        "to_premotor_cortex":     0.45,   # via area 44
        "to_area_44":             0.85,   # strongest coupling in the
                                          # area — lexical selection
                                          # feeds directly into
                                          # articulatory encoding
        "to_arcuate_fasciculus":  0.60,   # lower than area 44's 0.70;
                                          # the ventral semantic pathway
                                          # matters more here
        "to_middle_temporal_gyrus": 0.75, # the ventral semantic
                                          # pathway — lexical-semantic
                                          # content source
        "to_insula":              0.30,   # lower than area 44's 0.45
        "to_dlpfc":               0.60,   # higher than area 44's 0.35 —
                                          # verbal working-memory
                                          # coupling for lexical
                                          # selection
        "to_basal_ganglia":       0.40,   # gating of speech acts
        "to_commissures":         0.45,   # cross-midline lexical-
                                          # prosodic coordination;
                                          # lower than area 44's 0.50
                                          # because the prosody handoff
                                          # is 44's job more than 45's
    }

    Notes on the weights:
      - `brocas_weight` sums to 1.0 across areas 44 and 45. On the left
        the split is 0.55 / 0.45 — 45 takes the smaller share because
        the left's language production is more articulatory-dominant.
        The invariant is per-hemisphere: 44 + 45 = 1.0 on each side, and
        the two sides' splits together are not constrained to
        complement.
      - Feature weights are multipliers on features extracted by the
        VLPFC sub-module. The left's `lexical_selection` (0.80) is the
        highest feature weight in area 45 on either side, and it is the
        mirror of the left's area-44 `phonological`/`articulatory` pair
        — the two Broca's-area halves anchor different aspects of
        language production, and each is the dominant anchor for its
        aspect on the left.
      - The `syntactic` weight (0.70) is notably higher than area 44's
        (0.40). This reflects area 45's role in grammatical-structure
        integration — constructing the syntactic frame into which
        lexical items are placed, which is a prerequisite for area 44's
        articulatory encoding.
      - The `to_middle_temporal_gyrus` prior (0.75) is the highest
        connectivity prior in area 45 and one of the highest in the
        whole VLPFC. It reflects the ventral semantic pathway — the
        route by which lexical-semantic content flows from the temporal
        lobe into Broca's area for selection and production. This is
        the anatomical basis for the "what to say" role: without MTG
        input, area 45 has nothing to select from.
      - The `to_area_44` prior (0.85) is the highest intra-Broca's
        coupling. Lexical selection (45) feeds directly into
        articulatory encoding (44); the output path for speech runs
        45 → 44 → primary motor, and the high connectivity prior
        reflects that.
      - All values are plausible priors, not measured constants. The
        key constraints are the brocas_weight sum-to-1 invariant and
        the left/right directional mirror.

EXPORTS
-------
    from .brodmann_area_45 import BRODMANN_45    # int, == AREA_ID
    from .brodmann_area_45 import ANATOMY
    from .brodmann_area_45 import LEFT_CONFIG
    from .brodmann_area_45 import SYSTEM         # list, ["prefrontal_cortex"]
    from .brodmann_area_45 import SUB_REGION     # str
    from .brodmann_area_45 import GROUPING       # str, "brocas_area"

Consumers should prefer the flat re-export path
(`from ...brodmann_areas import BRODMANN_45`) over reaching into the
brocas_area nesting; the nesting is a tree-organisation detail and the
flat path is the stable API.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in VLPFC, not here.
    - Must not import `prefrontal_cortex/` or any of its sub-regions
      (cycle; the compute imports from here, not the other way round).
    - Must not import `brodmann_area_44/` (sibling; the coupling is via
      the VLPFC compute layer, not via registry-to-registry imports).
      The `to_area_44` connectivity prior in LEFT_CONFIG is the
      expression of the coupling; there is no runtime import between
      the two areas.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-45
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only the
      feature/connectivity weights and the brocas_weight share.
"""