"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_9
=====================================================================================================================

Brodmann area 9 — right hemisphere.

Mirror of the left area-9 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 9, says
which compute sub-region owns it, and supplies the per-area weights that
the owning sub-region's `encode()` reads. It defines no classes and no
functions; the public surface is the exports listed under "EXPORTS".

If you are looking for the computation area 9 participates in, it lives in
`.../frontal/cortex/prefrontal_cortex/dorsolateral_prefrontal_cortex/` —
area 9 is the canonical dorsolateral prefrontal area, and DLPFC is the
executive core of the frontal lobe. This package is the *label*; the
DLPFC compute sub-region is the *agent*.

IDENTITY
--------
    AREA_ID    = 9
    NAME       = "Brodmann area 9"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "dorsolateral_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping

The single-system-prefrontal pattern (SYSTEM one-element list, SUB_REGION
package-level string, GROUPING None) is identical to the left's — it is
the shape introduced by area 9 and reused by areas 10, 11, 12, 46.
Lateralisation does not change the shape, only the values.

A NOTE ON AREA 9's MEDIAL EXTENSION
-----------------------------------
Brodmann 9 is anatomically not quite confined to DLPFC: it extends onto
the medial surface of the superior frontal gyrus, where its cytoarchi-
tecture becomes continuous with the dorsomedial prefrontal cortex
(DMPFC). As on the left, the registry treats DLPFC as the primary owner
and documents the medial extension here rather than splitting area 9
into two blocks.

On the RIGHT this caveat is arguably more consequential than on the
left, because the medial extension's DMPFC character is functionally
more active on the right — the right's DMPFC portion (social cognition,
affective self-reference) has a larger and more distinct role than the
left's, which is more subordinate to the left's DLPFC executive control.
The registry still documents the medial extension as a caveat rather
than a config block, for the same schema reason (avoiding a
multi-sub-region-within-one-family variant that no other area needs),
but the caveat is worth flagging on the right more than on the left.
If a future experiment specifically probes the medial extension, that
is the trigger for the schema extension — not a silent fork of area 9's
config.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 9",
        "system": "prefrontal_cortex",
        "sub_region": "dorsolateral_prefrontal_cortex",
        "grouping": None,
        "location": "middle frontal gyrus (lateral surface, between the "
                    "superior and inferior frontal sulci, rostral to "
                    "the precentral sulcus) and the adjacent medial "
                    "surface of the superior frontal gyrus (see the "
                    "medial-extension note above)",
        "cytoarchitecture": "granular cortex; prominent layer IV, "
                            "well-developed layers II-III (the "
                            "association-cortex signature). Brodmann's "
                            "area 9 is the rostral neighbour of area 46 "
                            "(also DLPFC) and the lateral neighbour of "
                            "area 32 (dorsal ACC).",
        "notes": (
            "The canonical dorsolateral prefrontal area and the core of "
            "the central executive. Area 9 is where working memory is "
            "held, where plans are constructed and maintained, where "
            "rules are represented, and where goal-directed behaviour "
            "is controlled against distraction. Its best-characterised "
            "role is in delayed-response tasks: a stimulus is presented, "
            "held in working memory through a delay, and used to guide "
            "a response — area 9 is the substrate of the holding. On "
            "the RIGHT, area 9's DLPFC is more strongly engaged during "
            "spatial working memory (the visuospatial sketchpad) and "
            "spatial planning. The right's DLPFC holds spatial layouts, "
            "object positions, and spatial sequences in working memory, "
            "and uses them to plan spatially-situated actions. The "
            "left/right split is directional, not complementary — the "
            "right's area 9 is spatial-WM-forward, not 'the left's at "
            "reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 9's RIGHT_CONFIG is a single flat dict (single-system, single block
— no per-system nesting).

    RIGHT_CONFIG = {
        # ---- feature emphases ----
        # RIGHT bias: spatial working memory and spatial planning are
        # the right DLPFC's anchors. Verbal working memory is present
        # but secondary — the left DLPFC owns that.
        "verbal_working_memory":    0.45,   # phonological loop content;
                                            # more left-weighted
        "spatial_working_memory":   0.80,   # visuospatial sketchpad;
                                            # the right's anchor
        "planning":                 0.70,   # structural (equal);
                                            # both verbal and spatial
                                            # planning use DLPFC, with
                                            # different content
        "cognitive_control":        0.65,   # structural (equal)
        "response_inhibition":      0.60,   # structural (equal)
        "rule_representation":      0.60,   # DOWN mildly from left's
                                            # 0.65 — rules are more
                                            # verbal on the left and
                                            # more situational on the
                                            # right; both are still
                                            # substantial
        "task_switching":           0.55,   # structural (equal)
        "abstract_reasoning":       0.55,   # DOWN from left's 0.65 —
                                            # verbal-relational is
                                            # the left's form; the
                                            # right's spatial-
                                            # relational form is a
                                            # different feature
        "goal_maintenance":         0.70,   # structural (equal)
        "distraction_resistance":   0.60,   # structural (equal)

        # ---- connectivity priors ----
        "to_parietal":              0.75,   # UP from left's 0.60;
                                            # spatial WM coupling
                                            # (intraparietal sulcus,
                                            # superior parietal
                                            # lobule) — the right's
                                            # anchor connectivity
        "to_temporal":              0.55,   # DOWN from left's 0.75;
                                            # verbal WM coupling is
                                            # more left-weighted
        "to_anterior_cingulate":    0.65,   # structural (equal)
        "to_ventrolateral_pfc":     0.65,   # structural (equal)
        "to_basal_ganglia":         0.65,   # structural (equal)
        "to_premotor_cortex":       0.60,   # structural (equal)
        "to_posterior_cingulate":   0.40,   # structural (equal);
                                            # task-positive/DMN
                                            # anti-correlation baseline
        "to_hippocampus":           0.50,   # structural (equal)
        "to_commissures":           0.50,   # UP from left's 0.40;
                                            # spatial WM tasks more
                                            # often need verbal-
                                            # symbolic labels from
                                            # the left (naming
                                            # locations, describing
                                            # spatial relations
                                            # verbally) than verbal
                                            # WM tasks need spatial
                                            # content from the right
    }

    Notes on the weights:
      - Feature weights are multipliers on features extracted by the
        DLPFC sub-region. The right's `spatial_working_memory` (0.80)
        is the anchor, mirroring the left's verbal_working_memory
        anchor.
      - The DLPFC sub-region reads RIGHT_CONFIG directly — no
        `sub_region` field inside the config. Same as the left; the
        package-level SUB_REGION handles the disambiguation.
      - `to_parietal` (0.75) vs `to_temporal` (0.55) is the right's
        signature: spatial WM is more strongly coupled to the parietal
        lobe than verbal WM is to the temporal lobe. On the left this
        inverts (to_temporal is the anchor).
      - The `to_posterior_cingulate: 0.40` prior is a task-positive/
        DMN anti-correlation, identical to the left's and for the same
        reason (see the left area-9 docstring's note on this prior —
        it is a target the DLPFC compute reaches for by suppressing
        DMN activity, not a "higher = better" coupling strength).
      - Structural priors (to_anterior_cingulate, to_ventrolateral_pfc,
        to_basal_ganglia, to_premotor_cortex, to_posterior_cingulate,
        to_hippocampus) are IDENTICAL across hemispheres. The
        lateralised ones (to_parietal, to_temporal, to_commissures)
        directionally mirror.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) the right's anchor features match its
        functional signature; (b) structural priors are identical
        across hemispheres; (c) lateralised priors directionally
        mirror.

MIRROR PATTERN
--------------
Area 9's config is a directional mirror on the same key set as the
left's:

    left's area 9                right's area 9
    verbal_working_memory   0.80 verbal_working_memory   0.45
    spatial_working_memory  0.45 spatial_working_memory  0.80
    planning                0.70 planning                0.70
    cognitive_control       0.65 cognitive_control       0.65
    rule_representation     0.65 rule_representation     0.60
    abstract_reasoning      0.65 abstract_reasoning      0.55
    to_temporal             0.75 to_temporal             0.55
    to_parietal             0.60 to_parietal             0.75
    to_commissures          0.40 to_commissures          0.50

The relationship is directional: verbal WM and verbal-temporal coupling
go down on the right; spatial WM and parietal coupling go up on the
right. Structural priors (to_anterior_cingulate, to_basal_ganglia, to_
premotor_cortex, to_posterior_cingulate, to_hippocampus, to_ventrolateral_pfc)
are IDENTICAL across hemispheres. The mirror test must check direction
on lateralised keys and equality on structural keys.

PREDICTION (TESTABLE)
---------------------
The anchor swap makes a specific, testable claim: left DLPFC (area 9)
lesions should produce verbal working-memory deficits (reduced span for
word sequences, impaired verbal delayed response) with largely spared
spatial WM, while right DLPFC (area 9) lesions should produce the
opposite pattern (reduced spatial span, impaired spatial delayed
response, spared verbal WM). This is a cleaner prediction than "DLPFC
lesions impair WM" — it is asymmetric, and it follows directly from the
anchor swap in the config.

EXPORTS
-------
    from .brodmann_area_9 import BRODMANN_9      # int, == AREA_ID
    from .brodmann_area_9 import ANATOMY
    from .brodmann_area_9 import RIGHT_CONFIG
    from .brodmann_area_9 import SYSTEM          # list, ["prefrontal_cortex"]
    from .brodmann_area_9 import SUB_REGION      # str, set for single-system
    from .brodmann_area_9 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_9`) — area 9 is a direct child of
brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in DLPFC, not here.
    - Must not import `prefrontal_cortex/` or
      `dorsolateral_prefrontal_cortex/` (cycle; the compute imports
      from here, not the other way round).
    - Must not split into per-system or per-sub-region blocks. Area 9
      is single-system with SUB_REGION set; its config is a single
      flat dict. The per-block pattern is reserved for multi-system
      areas (6, 8, 47).
    - Must not add a `sub_region` field INSIDE RIGHT_CONFIG. That field
      is only used in multi-system per-block configs.
    - Must not add a medial-DMPFC config block to area 9 without first
      documenting the schema extension. The right's medial extension is
      more functionally active than the left's, but the schema rule
      still applies: no new block without documenting the new schema
      variant.
    - Must not import or reference the left hemisphere's area-9
      package. Cross-midline WM exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The right's `to_commissures: 0.50` prior is the
      baseline for when a spatial WM task needs verbal-symbolic
      labels from the left; direct registry access would bypass the
      commissural delay and bandwidth the model is supposed to
      exercise.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-9
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only by the
      directional mirror described above.
"""