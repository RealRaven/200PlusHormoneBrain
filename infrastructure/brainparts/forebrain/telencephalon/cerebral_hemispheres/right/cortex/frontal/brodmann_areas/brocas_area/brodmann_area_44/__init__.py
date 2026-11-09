"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brocas_area.brodmann_area_44
==================================================================================================================================

Brodmann area 44 (pars opercularis) — right hemisphere.

Mirror of the left area-44 package. A CONSTANT + CONFIG HOLDER inside the
brocas_area nested registry sub-package. No compute, no state, no lifecycle.
Declares the canonical identity of area 44, says which compute sub-region
owns it, and supplies the per-area weights that the owning sub-region's
`encode()` reads. It defines no classes and no functions; the public surface
is the exports listed under "EXPORTS".

If you are looking for the computation area 44 participates in, it lives
in
`.../frontal/cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/`
— area 44 is the pars opercularis component of Broca's area, and Broca's
area is a Brodmann-area-level label on a sub-region of VLPFC. This
package is the *label*, not the *agent*.

If you are looking for the other half of Broca's area, it is
`brodmann_area_45/` (pars triangularis), in the same brocas_area
sub-package. The two are the two halves of a single coupled unit, and
the coupling is expressed through their `brocas_weight` shares and their
`to_area_45` / `to_area_44` connectivity priors, not through imports.

IDENTITY
--------
    AREA_ID    = 44
    NAME       = "Brodmann area 44 (pars opercularis)"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "ventrolateral_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = "brocas_area"

The SYSTEM list, SUB_REGION field, and GROUPING field are documented in
detail in the left area-44 docstring. In brief: SYSTEM is a list
uniformly across the frontal registry; SUB_REGION names the specific
prefrontal sub-region (VLPFC) that imports this area's config; GROUPING
names the named sub-grouping (brocas_area) that this area belongs to,
so that VLPFC's language-production pathway can filter by it rather than
hardcoding {44, 45}. All three fields are identical on the left and
right — anatomy does not lateralise, only weights do.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 44 (pars opercularis)",
        "system": "prefrontal_cortex",
        "sub_region": "ventrolateral_prefrontal_cortex",
        "grouping": "brocas_area",
        "location": "posterior part of the inferior frontal gyrus, "
                    "just anterior to the ventral precentral gyrus",
        "cytoarchitecture": "dysgranular cortex; transitional between the "
                            "agranular motor cortex (area 4, immediately "
                            "posterior) and the granular prefrontal cortex "
                            "(area 45, immediately anterior)",
        "notes": (
            "Pars opercularis — the posterior half of Broca's area, and "
            "the more motor-speech-like of the two areas. Its cytoarchi-"
            "tecture is transitional: it sits directly anterior to the "
            "ventral precentral gyrus (area 4's face/mouth "
            "representation), and its layer V projection neurons are "
            "more motor-like than area 45's. On the RIGHT, area 44's "
            "function is not the left's articulatory production at low "
            "weight — it is prosody-forward. The right's area 44 "
            "contributes expressive prosody, emotional tone, and the "
            "melodic contour of speech. The articulatory machinery is "
            "present (it is anatomically the same area) but is not the "
            "primary driver: on the right, the face/mouth motor output "
            "is more typically driven by emotional/affective speech "
            "acts (laughter, exclamation, affective interjection) than "
            "by propositional speech production, which the left owns. "
            "The left/right split is directional, not complementary — "
            "the right's area 44 is prosody-forward, not 'the left's at "
            "reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 44's config has three parts: (a) its share within Broca's area's
contribution to VLPFC, summing to 1.0 with area 45's share; (b) its
feature emphases within that contribution; and (c) its connectivity
priors to partner structures.

    RIGHT_CONFIG = {
        # ---- share within Broca's area's contribution to VLPFC ----
        # 44 : 45  sum to 1.0. On the right, 44 takes the SMALLER share
        # (0.45) because the right's Broca's-area contribution is more
        # prosody-anchored and area 45 (pars triangularis) carries the
        # prosodic-lexical interface. On the left the split is the
        # mirror (44: 0.55, 45: 0.45).
        "brocas_weight":          0.45,   # area 45: 0.55

        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: prosody is the anchor feature; articulatory is
        # much reduced; phonological is present (prosodic contours are
        # phonologically structured) but lower than the left's. Lexical
        # and syntactic are area 45's business on this side, small here.
        "phonological":           0.45,   # prosodic contours are
                                          # phonologically structured
        "articulatory":           0.35,   # machinery present, not
                                          # primary driver
        "lexical_selection":      0.20,   # area 45's business on the
                                          # right, smaller here
        "prosodic":               0.80,   # the right's area 44 anchor
                                          # feature — expressive
                                          # prosody, emotional tone
        "syntactic":              0.25,   # less grammatical-sequencing
                                          # role on the right
        "verbal_working_memory":  0.20,   # smaller contribution to the
                                          # phonological loop buffer

        # ---- connectivity priors to partner structures ----
        "to_primary_motor":       0.45,   # to area 4 face/mouth — lower
                                          # than the left's 0.75, because
                                          # articulatory output is not
                                          # this area's primary driver
        "to_premotor_cortex":     0.55,   # prosodic motor planning; lower
                                          # than the left's 0.65
        "to_area_45":             0.70,   # coupling within Broca's area
                                          # (same as left)
        "to_arcuate_fasciculus":  0.45,   # lower than the left's 0.70;
                                          # the right's dorsal language
                                          # pathway is less dominant for
                                          # phonological-motor mapping
        "to_insula":              0.60,   # higher than the left's 0.45;
                                          # the right's insular coupling
                                          # for autonomic/affective speech
                                          # is stronger
        "to_dlpfc":               0.35,   # same as left
        "to_basal_ganglia":       0.40,   # same as left
        "to_commissures":         0.55,   # higher than the left's 0.50;
                                          # the right's prosody must
                                          # cross the midline to reach
                                          # the left's speech output
    }

    Notes on the weights:
      - `brocas_weight` sums to 1.0 across areas 44 and 45. On the right
        the split is 0.45 / 0.55 — 44 takes the smaller share, because
        the right's prosody role makes the 44/45 coupling more balanced
        than on the left, where 44's articulatory dominance gives it the
        majority. The invariant is per-hemisphere: 44 + 45 = 1.0 on each
        side, and the two sides' splits together are not constrained to
        complement. (Left is 0.55 / 0.45; right is 0.45 / 0.55 — the
        shares are separately normalised, not cross-side paired.)
      - Feature weights are multipliers on features extracted by the
        VLPFC sub-module. The right's `prosodic` (0.80) is the highest
        feature weight in Broca's area on either side, and it is the
        mirror of the left's `phonological`/`articulatory` (0.80) pair.
        The three anchor features swap sides: 44 on the left anchors
        phonology/articulation; 44 on the right anchors prosody.
      - The `articulatory` weight is 0.35 on the right vs 0.80 on the
        left. This is the largest single-direction change in the
        Broca's-area mirror, and it is intentional — the right's area 44
        is anatomically the same structure but functionally the
        articulatory role is subordinate. The motor machinery is present
        (0.35 is not zero), but it is not what the area is for on the
        right.
      - Connectivity priors flip directionally:
          * `to_primary_motor` and `to_arcuate_fasciculus` go DOWN on
            the right (articulatory and dorsal-language roles reduced);
          * `to_insula` and `to_commissures` go UP on the right
            (autonomic-affective coupling and cross-midline prosody
            delivery, both stronger on the right);
          * `to_area_45`, `to_dlpfc`, `to_basal_ganglia` stay the same
            (structural coupling within VLPFC does not lateralise).
      - All values are plausible priors, not measured constants. The
        key constraints are the brocas_weight sum-to-1 invariant and
        the left/right DIRECTIONAL mirror (not numerical complementarity
        — see below).

MIRROR PATTERN
--------------
This area's config is a directional mirror, not a complementary one.
The Broca's-area weights are NOT two halves of a single budget that sum
to 1 across hemispheres:

    left's area 44              right's area 44
    phonological   0.80         phonological   0.45
    articulatory   0.80         articulatory   0.35
    prosodic       0.15         prosodic       0.80
    lexical        0.35         lexical        0.20

The relationship is directional: phonological and articulatory go down
on the right, prosodic goes up on the right. The mirror test must check
direction (right < left on articulatory, right > left on prosodic, etc.),
not complementarity (which would incorrectly expect right = 1 - left on
each key).

This is the same pattern the frontal parent registry and the brocas_area
parent both flagged: directional, not complementary. Area 44 is the
cleanest instance of the pattern in the project.

EXPORTS
-------
    from .brodmann_area_44 import BRODMANN_44    # int, == AREA_ID
    from .brodmann_area_44 import ANATOMY
    from .brodmann_area_44 import RIGHT_CONFIG
    from .brodmann_area_44 import SYSTEM         # list, ["prefrontal_cortex"]
    from .brodmann_area_44 import SUB_REGION     # str
    from .brodmann_area_44 import GROUPING       # str, "brocas_area"

The export names and structure are identical to the left's. Consumers
should prefer the flat re-export path
(`from ...brodmann_areas import BRODMANN_44`) over reaching into the
brocas_area nesting; the nesting is a tree-organisation detail and the
flat path is the stable API.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in VLPFC, not here.
    - Must not import `prefrontal_cortex/` or any of its sub-regions
      (cycle; the compute imports from here, not the other way round).
    - Must not import `brodmann_area_45/` (sibling; the coupling is via
      the VLPFC compute layer, not via registry-to-registry imports).
      The `to_area_45` connectivity prior in RIGHT_CONFIG is the
      expression of the coupling; there is no runtime import between
      the two areas.
    - Must not import or reference the left hemisphere's area-44 package.
      Cross-midline state exchange goes through
      `telencephalon/commissures/`, never through direct registry access.
      For Broca's area specifically, the direct-registry-access failure
      mode is "silently treating the right's prosody as the left's
      articulation" — the exact mistake this area's config is designed to
      prevent.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-44
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only by the
      directional mirror described above.
"""