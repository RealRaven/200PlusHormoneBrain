"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brocas_area.brodmann_area_45
==================================================================================================================================

Brodmann area 45 (pars triangularis) — right hemisphere.

Mirror of the left area-45 package. A CONSTANT + CONFIG HOLDER inside the
brocas_area nested registry sub-package. No compute, no state, no lifecycle.
Declares the canonical identity of area 45, says which compute sub-region
owns it, and supplies the per-area weights that the owning sub-region's
`encode()` reads. It defines no classes and no functions; the public surface
is the exports listed under "EXPORTS".

If you are looking for the computation area 45 participates in, it lives
in
`.../frontal/cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/`
— area 45 is the pars triangularis component of Broca's area, and Broca's
area is a Brodmann-area-level label on a sub-region of VLPFC. This
package is the *label*, not the *agent*.

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
    SIDE       = "right"
    GROUPING   = "brocas_area"

The SYSTEM list, SUB_REGION field, and GROUPING field are identical to
the left's — anatomy and grouping do not lateralise within Broca's area,
only weights do. The fields are documented in detail in the left
area-45 docstring.

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
            "cytoarchitecture is more granular than area 44's, with a "
            "connectivity profile more strongly to posterior "
            "association cortex than to motor cortex. On the RIGHT, "
            "area 45's function is not the left's lexical-selection role "
            "at low weight — it is the prosodic-lexical interface. The "
            "right's area 45 contributes the melodic structure of "
            "speech: matching prosodic contour to affective content, "
            "producing the intonation pattern that carries semantic "
            "emphasis and emotional meaning. The lexical-selection "
            "machinery is present (it is anatomically the same area) "
            "but is not the primary driver: on the right, word-level "
            "selection is minimal, and the area's dominant contribution "
            "is prosody. The left/right split is directional, not "
            "complementary — the right's area 45 is prosody-anchored, "
            "not 'the left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 45's config has three parts: (a) its share within Broca's area's
contribution to VLPFC, summing to 1.0 with area 44's share; (b) its
feature emphases within that contribution; and (c) its connectivity
priors to partner structures.

    RIGHT_CONFIG = {
        # ---- share within Broca's area's contribution to VLPFC ----
        # 44 : 45  sum to 1.0. On the right, 45 takes the LARGER share
        # (0.55) — the right's Broca's-area contribution is
        # prosody-anchored, and area 45 carries the prosodic-lexical
        # interface. On the left the split is the mirror (44: 0.55,
        # 45: 0.45).
        "brocas_weight":          0.55,   # area 44: 0.45

        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: prosody is the anchor feature; lexical-selection
        # and syntactic are much reduced (lexical selection and grammar
        # are the left's business); phonological is present (prosodic
        # contours are phonologically structured) but lower than the
        # left's.
        "phonological":           0.40,   # prosodic contours are
                                          # phonologically structured
        "articulatory":           0.20,   # machinery present, not
                                          # primary driver
        "lexical_selection":      0.25,   # left's business on the
                                          # right, small here
        "prosodic":               0.85,   # the right's area-45 anchor
                                          # feature — melodic contour
                                          # of speech
        "syntactic":              0.30,   # much reduced; grammar is
                                          # left-lateralised
        "verbal_working_memory":  0.30,   # smaller contribution to the
                                          # phonological loop buffer;
                                          # prosodic contour is held in
                                          # working memory differently
                                          # from verbal content

        # ---- connectivity priors to partner structures ----
        "to_primary_motor":       0.25,   # much lower than the left's
                                          # 0.35 — no direct
                                          # articulatory output path
                                          # from the right's 45
        "to_premotor_cortex":     0.35,   # prosodic motor planning
        "to_area_44":             0.85,   # strongest coupling in the
                                          # area — prosodic contour
                                          # feeds into the right's 44,
                                          # which then hands off to the
                                          # commissures for delivery
        "to_arcuate_fasciculus":  0.40,   # much lower than the left's
                                          # 0.60 — the dorsal language
                                          # pathway is not the right's
                                          # 45 primary input
        "to_middle_temporal_gyrus": 0.45, # much lower than the left's
                                          # 0.75 — lexical-semantic
                                          # input is the left's job;
                                          # the right's 45 gets more
                                          # input from auditory
                                          # association and affective
                                          # temporal regions
        "to_insula":              0.55,   # higher than the left's 0.30
                                          # — the right's prosodic
                                          # contour is strongly coupled
                                          # to autonomic-affective
                                          # state
        "to_dlpfc":               0.35,   # lower than the left's 0.60
                                          # — less verbal working-
                                          # memory coupling
        "to_basal_ganglia":       0.40,   # gating of speech acts
        "to_commissures":         0.75,   # the highest commissural
                                          # prior in Broca's area — the
                                          # right's prosodic contour
                                          # has to cross the midline to
                                          # reach the left's speech
                                          # output. This is the
                                          # anatomical basis for the
                                          # flat-speech failure mode
                                          # if the commissures are
                                          # cut.
    }

    Notes on the weights:
      - `brocas_weight` sums to 1.0 across areas 44 and 45. On the right
        the split is 0.45 / 0.55 — 45 takes the larger share, because
        the right's prosody role makes 45's prosodic-lexical interface
        the anchor of the right's Broca's-area contribution. The
        invariant is per-hemisphere: 44 + 45 = 1.0 on each side, and
        the two sides' splits together are not constrained to
        complement.
      - Feature weights are multipliers on features extracted by the
        VLPFC sub-module. The right's `prosodic` (0.85) is the highest
        feature weight in Broca's area on either side, and it is the
        mirror of the left's `lexical_selection` (0.80). The two
        Broca's-area halves' anchor features swap sides: 45 on the left
        anchors lexical selection; 45 on the right anchors prosody.
      - The `lexical_selection` weight (0.25) is the largest
        single-direction change in the area-45 mirror, mirroring the
        area-44 pair's articulatory change (0.80 → 0.35). The
        machinery is present (0.25 is not zero) but is not what the
        area is for on the right.
      - Connectivity priors flip directionally:
          * `to_primary_motor`, `to_arcuate_fasciculus`, and
            `to_middle_temporal_gyrus` go DOWN on the right (the
            articulatory output path, the dorsal language pathway, and
            the ventral semantic pathway are all left-dominant);
          * `to_insula` and `to_commissures` go UP on the right
            (autonomic-affective coupling and cross-midline prosody
            delivery, both stronger on the right);
          * `to_area_44`, `to_premotor_cortex`, `to_basal_ganglia` stay
            roughly the same or shift mildly (structural coupling
            within VLPFC does not lateralise).
      - The `to_commissures: 0.75` prior is the highest commissural
        prior in Broca's area and one of the highest in the whole
        frontal lobe. It reflects the right's prosody having to cross
        the midline to reach the left's speech output — the anatomical
        basis for the flat-speech failure mode when the commissures
        are interrupted. The left's area-45 commissural prior is 0.45;
        the right's is 0.75. The asymmetry is the point.
      - All values are plausible priors, not measured constants. The
        key constraints are the brocas_weight sum-to-1 invariant and
        the left/right DIRECTIONAL mirror.

MIRROR PATTERN
--------------
This area's config is a directional mirror, not a complementary one —
the mirror of the area-44 pattern. The Broca's-area weights are NOT two
halves of a single budget that sum to 1 across hemispheres:

    left's area 45              right's area 45
    lexical_selection 0.80      lexical_selection 0.25
    syntactic         0.70      syntactic         0.30
    prosodic          0.15      prosodic          0.85
    phonological      0.45      phonological      0.40

The relationship is directional: lexical and syntactic go down on the
right, prosodic goes up on the right. The mirror test must check
direction (right < left on lexical_selection, right > left on prosodic,
etc.), not complementarity. The `to_commissures` prior is the cleanest
instance: it goes UP on the right (0.45 → 0.75), because the right's
prosody has to cross the midline to be delivered.

EXPORTS
-------
    from .brodmann_area_45 import BRODMANN_45    # int, == AREA_ID
    from .brodmann_area_45 import ANATOMY
    from .brodmann_area_45 import RIGHT_CONFIG
    from .brodmann_area_45 import SYSTEM         # list, ["prefrontal_cortex"]
    from .brodmann_area_45 import SUB_REGION     # str
    from .brodmann_area_45 import GROUPING       # str, "brocas_area"

The export names and structure are identical to the left's. Consumers
should prefer the flat re-export path
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
      The `to_area_44` connectivity prior in RIGHT_CONFIG is the
      expression of the coupling; there is no runtime import between
      the two areas.
    - Must not import or reference the left hemisphere's area-45 package.
      Cross-midline state exchange goes through
      `telencephalon/commissures/`, never through direct registry access.
      For Broca's area specifically, the direct-registry-access failure
      mode is "silently treating the right's prosody as the left's
      lexical selection" — the exact mistake this area's config is
      designed to prevent, and the reason the right's `to_commissures`
      prior (0.75) is so high.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-45
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only by the
      directional mirror described above.
"""