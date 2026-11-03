"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_8
=====================================================================================================================

Brodmann area 8 (frontal eye fields + dorsomedial prefrontal extension) —
right hemisphere.

Mirror of the left area-8 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 8, says
which compute sub-regions own it, and supplies the per-area weights that
the owning sub-regions' `encode()` methods read. It defines no classes and
no functions; the public surface is the exports listed under "EXPORTS".

If you are looking for the computation area 8 participates in, it lives in
TWO compute sub-regions:
    `.../frontal/cortex/premotor_cortex/`              (lateral area 8:
                                                       frontal eye fields)
    `.../frontal/cortex/prefrontal_cortex/dorsomedial_prefrontal_cortex/`
                                                       (medial area 8:
                                                       DMPFC extension)
Area 8 is the HYBRID multi-system case: one leaf system (premotor_cortex
— no sub-region disambiguation needed) and one family system
(prefrontal_cortex — needs to name which of its five subdivisions). This
package is the *label*; the two compute sub-regions are the *agents*.

IDENTITY
--------
    AREA_ID    = 8
    NAME       = "Brodmann area 8 (FEF + DMPFC extension)"
    SYSTEM     = ["premotor_cortex", "prefrontal_cortex"]
    SUB_REGION = None         # multi-system — see left area-8 docstring
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping

The hybrid SUB_REGION rule is identical to the left's: the package-level
SUB_REGION is None because the area spans two systems; the family
system's block carries its own `sub_region` field; the leaf system's
block does not. This is the schema introduced by area 8 and reused by
area 47. The full rationale is in the left area-8 docstring; it is not
repeated here, but the structural invariants it establishes are the same
on both hemispheres.

THE HYBRID PER-SYSTEM CONFIG BLOCK PATTERN
------------------------------------------
Area 8's RIGHT_CONFIG has one block per owning system, exactly as the
left's does:

    RIGHT_CONFIG = {
        "premotor_cortex":    { ... FEF feature + connectivity ... },
        "prefrontal_cortex":  { "sub_region": "dorsomedial_prefrontal_cortex",
                                ... DMPFC feature + connectivity ... },
    }

The `sub_region` field in the prefrontal block is IDENTICAL across
hemispheres — it identifies which prefrontal subdivision owns the block,
and that is an anatomical fact, not a lateralised parameter. The DMPFC
compute sub-region on the right reads
`RIGHT_CONFIG["prefrontal_cortex"]` after checking
`sub_region == "dorsomedial_prefrontal_cortex"`, exactly as the left
DMPFC does.

There is NO sum-to-1 invariant across blocks (same as area 6 and left
area 8): the blocks are independent configs consumed by different
sub-regions.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 8 (frontal eye fields + dorsomedial prefrontal extension)",
        "system": "premotor_cortex + prefrontal_cortex",
        "sub_region": None,
        "grouping": None,
        "location": "the lateral area 8 (FEF proper) lies at the "
                    "junction of the precentral and superior frontal "
                    "sulci, on the middle frontal gyrus; the medial "
                    "extension continues onto the medial surface of "
                    "the superior frontal gyrus (DMPFC portion)",
        "cytoarchitecture": "dysgranular (lateral FEF, transitioning "
                            "to agranular anteriorly) to granular "
                            "(medial DMPFC); the lateral and medial "
                            "portions are cytoarchitectonically "
                            "continuous with the premotor strip and "
                            "the prefrontal cortex respectively, which "
                            "is why area 8 is classified as a hybrid",
        "notes": (
            "Area 8 has two functionally distinct subdivisions with "
            "different cytoarchitectonic signatures. The LATERAL part "
            "is the frontal eye fields (FEF) — an oculomotor premotor "
            "area that generates voluntary saccades, orients visual "
            "attention, and drives visual exploration. The MEDIAL part "
            "is a dorsomedial prefrontal extension (DMPFC) — part of "
            "the default-mode/mentalizing network. That a single "
            "Brodmann number spans an oculomotor area and a "
            "self-referential area is a historical artifact of "
            "Brodmann's cytoarchitectonic criteria, not a functional "
            "unity. On the RIGHT, the FEF's spatial attention "
            "orienting and free-viewing visual exploration roles "
            "dominate over the left's reading-saccade role; the right "
            "FEF is the dominant node of the dorsal attention network "
            "for exogenous spatial attention. The DMPFC's affective/"
            "social self-reference role dominates over the left's "
            "verbal mentalizing role; the right DMPFC is more strongly "
            "coupled to the amygdala and to autonomic/affective "
            "self-representation. The left/right split is directional, "
            "not complementary — the right's area 8 is spatial/affective-"
            "forward, not 'the left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 8's RIGHT_CONFIG has two per-system blocks. The premotor block has
no `sub_region` field (leaf system); the prefrontal block has one
(family system).

    RIGHT_CONFIG = {

        # ============================================================
        # FIRST BLOCK — premotor_cortex (lateral area 8: FEF)
        # ============================================================
        # RIGHT bias: spatial attention orienting and free-viewing
        # visual exploration are the right FEF's anchor roles; reading
        # saccades and predictive timing are present but secondary.
        "premotor_cortex": {
            # ---- feature emphases ----
            "saccade_generation":      0.60,   # structural baseline
                                               # (equal to left)
            "reading_saccades":        0.30,   # DOWN from left's 0.80
            "attention_orienting":     0.75,   # UP from left's 0.55;
                                               # the right FEF anchor
            "visual_exploration":      0.75,   # UP from left's 0.45;
                                               # the right FEF anchor
            "predictive_timing":       0.65,   # DOWN from left's 0.70;
                                               # mildly left-lateralised
            "smooth_pursuit":          0.55,   # structural (equal)

            # ---- connectivity priors ----
            "to_superior_colliculus":  0.75,   # structural (equal)
            "to_pprf":                 0.70,   # structural (equal)
            "to_parietal":             0.75,   # UP from left's 0.70;
                                               # the right FEF is the
                                               # dominant dorsal-
                                               # attention node
            "to_occipital":            0.55,   # structural (equal)
            "to_dlpfc":                0.55,   # structural (equal)
            "to_basal_ganglia":        0.55,   # structural (equal)
            "to_cerebellum":           0.55,   # structural (equal)
            "to_commissures":          0.65,   # UP from left's 0.60;
                                               # the right FEF has a
                                               # slightly heavier
                                               # commissural load
                                               # because its
                                               # exploration scan paths
                                               # span the whole visual
                                               # field and must be
                                               # conjugated with the
                                               # left FEF
        },

        # ============================================================
        # SECOND BLOCK — prefrontal_cortex (medial area 8: DMPFC)
        # ============================================================
        # RIGHT bias: affective/social self-reference and
        # autobiographical recall are the right DMPFC's anchor roles;
        # verbal mentalizing is present but secondary.
        "prefrontal_cortex": {
            # The sub_region field identifies which prefrontal
            # subdivision owns this block. IDENTICAL to the left's
            # value — it is structural.
            "sub_region": "dorsomedial_prefrontal_cortex",

            # ---- feature emphases ----
            "self_reference":          0.55,   # DOWN from left's 0.70;
                                               # affective self-
                                               # reference, not
                                               # verbal
            "mentalizing":             0.55,   # DOWN from left's 0.75;
                                               # more affectively-
                                               # anchored on the right
            "social_cognition":        0.70,   # UP from left's 0.55;
                                               # the right DMPFC
                                               # anchor — social
                                               # judgement, affective
                                               # Theory of Mind
            "future_prospection":      0.55,   # DOWN mildly from
                                               # left's 0.60;
                                               # more verbally-loaded
                                               # on the left
            "autobiographical":        0.65,   # structural (equal);
                                               # recall content
                                               # differs (affective vs
                                               # verbal), but the
                                               # weight is the same
            "self_other_distinction":  0.55,   # structural (equal)

            # ---- connectivity priors ----
            "to_posterior_cingulate":  0.75,   # structural (equal);
                                               # DMN hub coupling
            "to_precuneus":            0.65,   # structural (equal)
            "to_temporal_pole":        0.55,   # structural (equal)
            "to_vmpfc":                0.65,   # structural (equal)
            "to_hippocampus":          0.55,   # DOWN from left's 0.60;
                                               # affective > verbal
                                               # autobiographical
                                               # recall
            "to_amygdala":             0.55,   # UP from left's 0.40;
                                               # the right DMPFC is
                                               # strongly coupled to
                                               # affective self-
                                               # representation
            "to_insula":               0.50,   # UP from left's 0.40;
                                               # interoceptive self-
                                               # representation
            "to_dlpfc":                0.55,   # structural (equal)
            "to_commissures":          0.30,   # structural (equal)
        },
    }

    Notes on the weights:
      - The `sub_region` field is IDENTICAL to the left's value
        ("dorsomedial_prefrontal_cortex"). It identifies which
        prefrontal subdivision owns the block; that is an anatomical
        fact, not a lateralised parameter. The mirror test checks it
        for equality, not direction.
      - Feature weights mirror directionally per block. The right's
        anchors are:
            premotor block: attention_orienting (0.75) and
                            visual_exploration (0.75) — the right
                            FEF's dorsal-attention roles
            prefrontal block: social_cognition (0.70) — the right
                              DMPFC's affective/social anchor
        The left-weighted features (reading_saccades,
        predictive_timing, mentalizing, self_reference) are present at
        0.30–0.65 — not zero, but clearly below the anchors where
        applicable.
      - The two blocks are INDEPENDENT. No cross-block constraint.
      - Structural priors are IDENTICAL across hemispheres within each
        block. The premotor block has the strongest structural set
        (to_superior_colliculus 0.75, to_pprf 0.70, to_parietal 0.75
        on the right / 0.70 on the left, to_occipital 0.55, to_dlpfc
        0.55, to_basal_ganglia 0.55, to_cerebellum 0.55). The
        prefrontal block has DMN-hub structural priors (to_posterior_
        cingulate 0.75, to_precuneus 0.65, to_vmpfc 0.65, to_temporal_
        pole 0.55, to_dlpfc 0.55).
      - Lateralised connectivity priors directionally mirror:
            premotor block: to_parietal UP (0.70→0.75), to_commissures
                            UP (0.60→0.65)
            prefrontal block: to_amygdala UP (0.40→0.55), to_insula UP
                              (0.40→0.50), to_hippocampus DOWN
                              (0.60→0.55)
      - The `to_commissures: 0.65` prior in the right premotor block is
        the highest in area 8 on either side. It reflects the right
        FEF's heavier commissural load: the right FEF drives the
        exploration scan path across the whole visual field, and for
        the eyes to remain conjugate throughout the scan, the right
        FEF's activity has to be continuously coordinated with the
        left FEF's. Slightly higher than the left's 0.60 for the same
        reason.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) within each block, the anchor
        features match the right's functional signature; (b) structural
        priors are identical across hemispheres within a block;
        (c) the `sub_region` field is identical across hemispheres;
        (d) lateralised priors directionally mirror.

MIRROR PATTERN
--------------
Area 8's config is a directional mirror, applied per-block, with the
same schema on both sides:

    Left's premotor block         Right's premotor block
    reading_saccades      0.80    reading_saccades      0.30
    attention_orienting   0.55    attention_orienting   0.75
    visual_exploration    0.45    visual_exploration    0.75
    predictive_timing     0.70    predictive_timing     0.65
    to_parietal           0.70    to_parietal           0.75
    to_commissures        0.60    to_commissures        0.65

    Left's prefrontal block       Right's prefrontal block
    sub_region            DMPFC   sub_region            DMPFC
                                  (IDENTICAL — structural)
    mentalizing           0.75    mentalizing           0.55
    self_reference        0.70    self_reference        0.55
    social_cognition      0.55    social_cognition      0.70
    to_amygdala           0.40    to_amygdala           0.55
    to_insula             0.40    to_insula             0.50
    to_hippocampus        0.60    to_hippocampus        0.55

The relationship is directional in each block, with one equality case
(`sub_region`). The mirror test must check:
    1. within-block direction on lateralised feature/connectivity keys;
    2. within-block equality on structural keys;
    3. `sub_region` equality across hemispheres (per-block, when present);
    4. no cross-block relations are checked.

EXPORTS
-------
    from .brodmann_area_8 import BRODMANN_8      # int, == AREA_ID
    from .brodmann_area_8 import ANATOMY
    from .brodmann_area_8 import RIGHT_CONFIG
    from .brodmann_area_8 import SYSTEM          # list, two elements
    from .brodmann_area_8 import SUB_REGION      # None (multi-system;
                                                 # see per-block sub_region)
    from .brodmann_area_8 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_8`) — area 8 is a direct child of
brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in premotor_cortex/ and
      prefrontal_cortex/dorsomedial_prefrontal_cortex/, not here.
    - Must not import `premotor_cortex/` or `prefrontal_cortex/`
      (cycle; the compute imports from here, not the other way round).
    - Must not add a top-level (non-per-system) `RIGHT_CONFIG` that
      mixes the two blocks. The per-system block structure is the
      contract on both hemispheres.
    - Must not change the `sub_region` field's value on the right. It
      is identical to the left's; the block's owner (DMPFC) does not
      lateralise. If it ever appears different, that is a structural
      bug, not a lateralisation decision.
    - Must not promote the prefrontal block's `sub_region` field to
      the package level. The field is per-block, because area 8 is
      multi-system.
    - Must not introduce a `premotor_weight + prefrontal_weight = 1.0`
      constraint. There is no such pair.
    - Must not import or reference the left hemisphere's area-8
      package. Cross-midline eye movement coordination goes through
      `telencephalon/commissures/`, never through direct registry
      access.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-8
      package — same AREA_ID, SYSTEM, SUB_REGION (None), GROUPING
      (None), ANATOMY, same block keys, same feature/connectivity key
      names inside each block, same `sub_region` value in the
      prefrontal block. Only the values differ, and only by the
      per-block directional mirror.

CROSS-MIDLINE RULE (FEF-SPECIFIC NOTE)
--------------------------------------
The general rule applies as usual: no direct import or reference to
the left hemisphere's area-8 package; all cross-midline state
exchange goes through `telencephalon/commissures/`.

Area 8 has the strongest commissural dependence in the frontal
registry so far, for the conjugate-eye-movement reason documented in
detail in the left area-8 docstring. On the right, the
`to_commissures: 0.65` prior is slightly higher than the left's
0.60, reflecting the right FEF's heavier exploration-scan load — the
right FEF drives the scan path across the whole visual field, and
conjugacy has to be maintained throughout, which requires more
continuous interhemispheric exchange. The prediction remains that a
commissure-lesion model should produce a conjugate gaze deficit far
more severe than its effect on DMPFC-mediated social cognition; on
the right, the deficit should be dominated by disrupted free-viewing
exploration (spatial exploration degrades), while on the left the
deficit should be dominated by disrupted reading saccades (text
fixation becomes erratic). The two failure modes are asymmetric,
because the anchor features they disrupt are asymmetric.
"""