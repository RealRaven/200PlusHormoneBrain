"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_8
====================================================================================================================

Brodmann area 8 (frontal eye fields + dorsomedial prefrontal extension) —
left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 8, says which compute sub-regions own it,
and supplies the per-area weights that the owning sub-regions' `encode()`
methods read. It defines no classes and no functions; the public surface is
the exports listed under "EXPORTS".

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
    SUB_REGION = None         # multi-system — see note below
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping

Note on SUB_REGION being None with a non-trivial family system: this is
the HYBRID case. The package-level SUB_REGION field is set when the
*entire area* belongs to exactly one sub-region (that is the rule for
single-system areas like 44, 45, 9, 10, 11, 12, 46). For multi-system
areas, the package-level SUB_REGION is None because the area spans more
than one sub-region, and each per-system block carries its own
`sub_region` field if its system is a family (leaf systems do not need
one). This is the formal rule introduced by area 8 and reused by area
47; it generalises the pattern area 6 established implicitly (both its
blocks are leaf systems, so neither carries a `sub_region` field).

For area 8 specifically:
    premotor block:    leaf system, no `sub_region` field (implicit None)
    prefrontal block:  family system, `sub_region = "dorsomedial_prefrontal_cortex"`

THE HYBRID PER-SYSTEM CONFIG BLOCK PATTERN
------------------------------------------
Area 8's LEFT_CONFIG has one block per owning system:

    LEFT_CONFIG = {
        "premotor_cortex":    { ... FEF feature + connectivity ... },
        "prefrontal_cortex":  { "sub_region": "dorsomedial_prefrontal_cortex",
                                ... DMPFC feature + connectivity ... },
    }

Each owning sub-region reads its own block: `premotor_cortex/` reads
`LEFT_CONFIG["premotor_cortex"]`, and
`prefrontal_cortex/dorsomedial_prefrontal_cortex/` reads
`LEFT_CONFIG["prefrontal_cortex"]` after checking that
`sub_region == "dorsomedial_prefrontal_cortex"`. The `sub_region` field
is what tells the prefrontal family which of its five subdivisions the
block is for; without it, a DMPFC compute sub-region reading a
prefrontal block would not know it was the intended consumer.

There is NO sum-to-1 invariant across blocks (same as area 6): the
blocks are independent configs consumed by different sub-regions.

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
            "attention, and drives visual exploration. It contains a "
            "retinotopic map of the contralateral visual field, has "
            "direct visual cortex input (it is one of the few motor "
            "areas with a visual response), and projects to the "
            "superior colliculus and brainstem oculomotor nuclei via "
            "the paramedian pontine reticular formation. The MEDIAL "
            "part is a dorsomedial prefrontal extension (DMPFC) — part "
            "of the default-mode/mentalizing network, involved in "
            "self-referential processing, theory of mind, future "
            "prospection, and social cognition. That a single Brodmann "
            "number spans an oculomotor area and a self-referential "
            "area is a historical artifact of Brodmann's cytoarchi-"
            "tectonic criteria, not a functional unity. On the left, "
            "the FEF's reading-saccade role (precise, short saccades "
            "across text) and the DMPFC's verbal-mentalizing role are "
            "the anchors; the right's FEF (spatial attention orienting, "
            "visual exploration) and right's DMPFC (affective/social "
            "self-reference) are the anchors there. The left/right "
            "split is directional, not complementary."
        ),
    }

CONFIG (LEFT)
-------------
Area 8's LEFT_CONFIG has two per-system blocks. The premotor block has
no `sub_region` field (leaf system); the prefrontal block has one
(family system).

    LEFT_CONFIG = {

        # ============================================================
        # FIRST BLOCK — premotor_cortex (lateral area 8: FEF)
        # ============================================================
        # LEFT bias: reading saccades and predictive timing are the
        # left FEF's anchor roles; spatial attention orienting and
        # visual exploration are more right-lateralised and are
        # present but secondary.
        "premotor_cortex": {
            # ---- feature emphases ----
            "saccade_generation":      0.60,   # voluntary saccadic
                                               # eye movements
                                               # (structural role,
                                               # equal to left/right
                                               # baseline)
            "reading_saccades":        0.80,   # short, precise
                                               # saccades across text;
                                               # the left FEF anchor
            "attention_orienting":     0.55,   # visual attention
                                               # orienting; more
                                               # right-weighted
            "visual_exploration":      0.45,   # free-viewing scan
                                               # paths; more
                                               # right-weighted
            "predictive_timing":       0.70,   # predictive saccades
                                               # to expected locations
            "smooth_pursuit":          0.55,   # pursuit of moving
                                               # targets

            # ---- connectivity priors ----
            "to_superior_colliculus":  0.75,   # the primary FEF
                                               # output for saccades;
                                               # the oculomotor
                                               # pathway's first
                                               # subcortical relay
            "to_pprf":                 0.70,   # paramedian pontine
                                               # reticular formation;
                                               # horizontal saccade
                                               # generator
            "to_parietal":             0.70,   # LIP and other
                                               # intraparietal
                                               # attention areas;
                                               # the dorsal attention
                                               # network
            "to_occipital":            0.55,   # direct visual cortex
                                               # input — FEF is one of
                                               # few motor areas with
                                               # a visual response
            "to_dlpfc":                0.55,   # top-down attention
                                               # control from
                                               # prefrontal
            "to_basal_ganglia":        0.55,   # gating of saccade
                                               # programs (SNr /
                                               # caudate)
            "to_cerebellum":           0.55,   # saccade accuracy and
                                               # timing
            "to_commissures":          0.60,   # conjugate eye
                                               # movements require
                                               # interhemispheric
                                               # coordination of FEF
                                               # activity; see
                                               # CROSS-MIDLINE RULE
        },

        # ============================================================
        # SECOND BLOCK — prefrontal_cortex (medial area 8: DMPFC)
        # ============================================================
        # LEFT bias: verbal mentalizing and verbal self-reference are
        # the left DMPFC's anchor roles; affective/social self-
        # reference is more right-weighted.
        "prefrontal_cortex": {
            # The sub_region field identifies which prefrontal
            # subdivision owns this block. DMPFC reads it to confirm
            # it is the intended consumer. Multi-system areas are
            # the only place this field is present; single-system
            # prefrontal areas (9, 10, 11, 12, 46) set the package-
            # level SUB_REGION instead.
            "sub_region": "dorsomedial_prefrontal_cortex",

            # ---- feature emphases ----
            "self_reference":          0.70,   # self-related
                                               # processing;
                                               # verbal-weighted on
                                               # the left
            "mentalizing":             0.75,   # theory of mind;
                                               # verbal/narrative
                                               # weighted on the
                                               # left
            "social_cognition":        0.55,   # social judgement;
                                               # more right-weighted
            "future_prospection":      0.60,   # imagining future
                                               # scenarios;
                                               # verbal-weighted
            "autobiographical":        0.65,   # autobiographical
                                               # memory recall;
                                               # verbal-weighted
            "self_other_distinction":  0.55,   # distinguishing self
                                               # from other

            # ---- connectivity priors ----
            "to_posterior_cingulate":  0.75,   # strong coupling with
                                               # PCC; part of the
                                               # default-mode network
            "to_precuneus":            0.65,   # DMN coupling;
                                               # self-related
                                               # imagery
            "to_temporal_pole":        0.55,   # social-semantic
                                               # knowledge
            "to_vmpfc":                0.65,   # vmPFC coupling;
                                               # value/affect
                                               # integration
            "to_hippocampus":          0.60,   # autobiographical
                                               # memory retrieval
            "to_amygdala":             0.40,   # affective tagging of
                                               # self-relevant
                                               # memories;
                                               # more right-weighted
            "to_insula":               0.40,   # interoceptive
                                               # self-representation
            "to_dlpfc":                0.55,   # working-memory
                                               # coupling for
                                               # verbal mentalizing
            "to_commissures":          0.30,   # DMPFC ↔ DMPFC
                                               # exchange is modest;
                                               # social/self content
                                               # is more intra-
                                               # hemispheric than
                                               # motor content
        },
    }

    Notes on the weights:
      - The `sub_region` field in the prefrontal block is the schema
        addition that area 8 introduces. It is consumed by the DMPFC
        compute sub-region to confirm ownership; it is not consumed
        by the premotor block (which has no `sub_region` field because
        premotor is a leaf system — the block key itself is the
        disambiguation).
      - Feature weights are multipliers on features extracted by the
        corresponding sub-region. Within each block, the anchor
        features are the left's signature roles:
            premotor block: reading_saccades (0.80) — left FEF's
                            reading-saccade role
            prefrontal block: mentalizing (0.75) — verbal/narrative
                              mentalizing on the left
        The right-weighted features (attention_orienting,
        visual_exploration, social_cognition) are present at
        0.45–0.55 — not zero, but clearly below the anchors.
      - The two blocks are INDEPENDENT. There is no cross-block
        constraint relating premotor's weights to prefrontal's
        weights; they are consumed by different compute sub-regions.
      - `to_commissures` differs sharply between blocks: 0.60 in the
        premotor block vs 0.30 in the prefrontal block. Conjugate eye
        movements require the two FEFs to exchange state continuously
        (they drive both eyes, not just the ipsilateral one); self/
        social content is more intra-hemispheric. This is not an
        inconsistency — it is the FEF's structural commissural
        dependence showing up in the config.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) within each block, the anchor
        features match the left's functional signature; (b) structural
        priors are identical across hemispheres within a block;
        (c) lateralised priors directionally mirror.

MIRROR PATTERN
--------------
Area 8's config is a directional mirror, applied per-block, with one
schema difference on the prefrontal block:

    Left's premotor block         Right's premotor block
    reading_saccades      0.80    reading_saccades      0.30
    attention_orienting   0.55    attention_orienting   0.75
    visual_exploration    0.45    visual_exploration    0.75
    predictive_timing     0.70    predictive_timing     0.65
    to_parietal           0.70    to_parietal           0.75
    to_commissures        0.60    to_commissures        0.65

    Left's prefrontal block       Right's prefrontal block
    sub_region            DMPFC   sub_region            DMPFC
                                  (sub_region field is
                                   IDENTICAL across
                                   hemispheres — it is
                                   structural, not
                                   lateralised)
    mentalizing           0.75    mentalizing           0.55
    self_reference        0.70    self_reference        0.55
    social_cognition      0.55    social_cognition      0.70
    to_amygdala           0.40    to_amygdala           0.55
    to_insula             0.40    to_insula             0.50

The relationship is directional in each block. The `sub_region` field is
IDENTICAL across hemispheres (structural). Structural connectivity priors
(to_superior_colliculus, to_pprf, to_posterior_cingulate, to_precuneus,
to_vmpfc, to_hippocampus) are IDENTICAL across hemispheres within a
block. The mirror test must check:
    1. within-block direction on lateralised feature/connectivity keys;
    2. within-block equality on structural keys;
    3. `sub_region` equality across hemispheres (per-block, when present);
    4. no cross-block relations are checked.

EXPORTS
-------
    from .brodmann_area_8 import BRODMANN_8      # int, == AREA_ID
    from .brodmann_area_8 import ANATOMY
    from .brodmann_area_8 import LEFT_CONFIG
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
    - Must not add a top-level (non-per-system) `LEFT_CONFIG` that
      mixes the two blocks. The per-system block structure is the
      contract: each owning sub-region reads its own block.
    - Must not promote the prefrontal block's `sub_region` field to
      the package level. The field is per-block, because area 8 is
      multi-system — the package-level SUB_REGION is None and the
      block-level field carries the disambiguation for the family
      system. Promoting the field to the package level would make
      the premotor block's leaf-system ownership unclear (it does
      not belong to DMPFC).
    - Must not introduce a `premotor_weight + prefrontal_weight = 1.0`
      constraint. There is no such pair.
    - Must not import or reference the left hemisphere's area-8
      package. Cross-midline eye movement coordination goes through
      `telencephalon/commissures/`, never through direct registry
      access; see the CROSS-MIDLINE RULE note below for the FEF-
      specific version of this.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-8
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

Area 8 has a specific cross-midline property worth flagging, because
it is the strongest commissural dependence in the frontal registry so
far. Conjugate eye movements — the normal case, where both eyes move
together — require the two FEFs to coordinate. When the left FEF
generates a rightward saccade, the right FEF must also shift its
activity to hold the other eye in the same direction; without
commissural exchange, the eyes would lose conjugacy (the classic
clinical presentation of an interhemispheric lesion affecting the
frontal eye fields is a horizontal gaze palsy or a "wrong-way" eye
deviation). The `to_commissures: 0.60` prior in the premotor block is
the anatomical basis: it is the highest FEF connectivity prior except
for the primary oculomotor outputs, and it is substantially higher
than any prefrontal block's commissural prior.

Prediction: a commissure-lesion model should produce a conjugate
gaze deficit far more severe than its effect on DMPFC-mediated social
cognition. If we later want to test the commissures' behavioural
signature, conjugate eye movement is one of the cleanest probes in
the frontal lobe, because the failure mode is discrete and clinically
well-characterised.
"""