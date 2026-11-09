"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_9
====================================================================================================================

Brodmann area 9 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 9, says which compute sub-region owns it,
and supplies the per-area weights that the owning sub-region's `encode()`
reads. It defines no classes and no functions; the public surface is the
exports listed under "EXPORTS".

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
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping

This is the FIRST single-system prefrontal area with SUB_REGION set. The
pattern (established here, reused by areas 10, 11, 12, 46):
    SYSTEM     is a single-element list         (["prefrontal_cortex"])
    SUB_REGION is a string                      ("dorsolateral_prefrontal_cortex")
    GROUPING   is None                          (DLPFC has no named subgrouping)

The rule: SUB_REGION is set at the package level when the whole area
belongs to exactly one sub-region (single-system) AND that sub-region is
a family subdivision (prefrontal has five). For single-system areas whose
system is already a leaf (area 4, primary_motor_cortex), SUB_REGION is
None. For multi-system areas (6, 8, 47), the package-level SUB_REGION is
None and per-block `sub_region` fields are used inside the config blocks.

A NOTE ON AREA 9's MEDIAL EXTENSION
-----------------------------------
Brodmann 9 is anatomically not quite confined to DLPFC: it extends onto
the medial surface of the superior frontal gyrus, where its cytoarchi-
tecture becomes continuous with the dorsomedial prefrontal cortex
(DMPFC). The registry treats DLPFC as the PRIMARY owner and documents
the medial extension here rather than splitting area 9 into two blocks
(a DLPFC block and a DMPFC block).

Why not split? Because the medial extension of area 9 is small, its
functional contribution is subsumed by DMPFC's own area 8 and area 10
portions, and splitting area 9 would require a new schema variant
(multi-sub-region-within-one-family) that no other area needs. The DLPFC
block's feature weights below carry the area's whole contribution, and
the small medial component is documented as a caveat rather than a
separate config block. If a future need justifies splitting (e.g. the
medial portion of area 9 turns out to have a distinct functional role
in some experiment), the split would be done as a documented schema
extension — but not by silently giving area 9 two blocks.

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
            "a response — area 9 is the substrate of the holding. "
            "Beyond working memory, area 9 subserves planning (mentally "
            "constructing a multi-step sequence), cognitive control "
            "(biasing processing toward task-relevant information), "
            "response inhibition (holding back a prepotent response), "
            "and abstract reasoning. The left's DLPFC is more strongly "
            "engaged during verbal working memory — phonological-loop "
            "maintenance of words and sentences — and verbal planning; "
            "the right's DLPFC is more strongly engaged during spatial "
            "working memory (the visuospatial sketchpad) and spatial "
            "planning. The left/right split is directional, not "
            "complementary — the right's area 9 is spatial-WM-forward, "
            "not 'the left's at reduced weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 9's LEFT_CONFIG is a single flat dict (single-system, single block
— no per-system nesting).

    LEFT_CONFIG = {
        # ---- feature emphases ----
        # LEFT bias: verbal working memory and verbal planning are the
        # left DLPFC's anchors. Spatial working memory is present but
        # secondary — the right DLPFC owns that.
        "verbal_working_memory":    0.80,   # phonological loop content;
                                            # the left's anchor
        "spatial_working_memory":   0.45,   # visuospatial sketchpad;
                                            # more right-weighted
        "planning":                 0.70,   # multi-step plan
                                            # construction; verbal-
                                            # weighted on the left
        "cognitive_control":        0.65,   # biasing toward task-
                                            # relevant information
        "response_inhibition":      0.60,   # holding back prepotent
                                            # responses
        "rule_representation":      0.65,   # representing task rules
                                            # (verbal-rule weighted
                                            # on the left)
        "task_switching":           0.55,   # shifting between task
                                            # sets
        "abstract_reasoning":       0.65,   # relational reasoning;
                                            # verbal-relational
                                            # weighted on the left
        "goal_maintenance":         0.70,   # holding a goal active
                                            # through a delay
        "distraction_resistance":   0.60,   # resisting irrelevant
                                            # stimuli

        # ---- connectivity priors ----
        "to_parietal":              0.60,   # visuospatial WM
                                            # coupling; lower on the
                                            # left than the right
        "to_temporal":              0.75,   # verbal WM coupling
                                            # (superior/middle
                                            # temporal for
                                            # phonological and
                                            # semantic content);
                                            # the left's anchor
                                            # connectivity
        "to_anterior_cingulate":    0.65,   # conflict/error
                                            # monitoring feeds
                                            # control demand
        "to_ventrolateral_pfc":     0.65,   # VLPFC coupling for
                                            # verbal maintenance
                                            # and selection
        "to_basal_ganglia":         0.65,   # gating of action
                                            # selection and
                                            # working-memory
                                            # updating
        "to_premotor_cortex":       0.60,   # prepared movements
                                            # are held in DLPFC
                                            # WM; premotor coupling
                                            # is the plan-to-action
                                            # path
        "to_posterior_cingulate":   0.40,   # DMN anti-correlation:
                                            # task-positive DLPFC
                                            # suppresses DMN during
                                            # effortful tasks
        "to_hippocampus":           0.50,   # WM-memory interaction:
                                            # DLPFC WM and
                                            # hippocampal LTM
                                            # communicate during
                                            # encoding/retrieval
        "to_commissures":           0.40,   # cross-midline WM
                                            # exchange (e.g. when
                                            # a verbal WM task
                                            # requires spatial
                                            # information from
                                            # the right)
    }

    Notes on the weights:
      - Feature weights are multipliers on features extracted by the
        DLPFC sub-region. The left's `verbal_working_memory` (0.80) is
        the anchor, mirroring the right's spatial_working_memory
        anchor.
      - The DLPFC sub-region reads LEFT_CONFIG directly — no
        `sub_region` field inside the config (that field is only used
        in multi-system per-block configs; for single-system areas the
        package-level SUB_REGION serves the same disambiguation role
        more cheaply).
      - `to_temporal` (0.75) vs `to_parietal` (0.60) is the left's
        signature: verbal WM is more strongly coupled to the temporal
        lobe than spatial WM is to the parietal lobe. On the right
        this inverts (`to_parietal` becomes the anchor).
      - The `to_posterior_cingulate: 0.40` prior is a task-positive/
        DMN anti-correlation — a higher value would mean DLPFC fails
        to suppress DMN during effortful tasks. It is a baseline
        prior, not a "higher = better" quantity; the DLPFC compute
        will use it as a target for the anti-correlation, and lower
        values during task blocks would be the effortful-state
        signature.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) the left's anchor features match its
        functional signature; (b) structural priors are identical
        across hemispheres; (c) lateralised priors directionally
        mirror.

MIRROR PATTERN
--------------
Area 9's config is a directional mirror, on the same key set as the
right's. Not complementary — directional:

    left's area 9                right's area 9
    verbal_working_memory   0.80 verbal_working_memory   0.45
    spatial_working_memory  0.45 spatial_working_memory  0.80
    planning                0.70 planning                0.70
    cognitive_control       0.65 cognitive_control       0.65
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

EXPORTS
-------
    from .brodmann_area_9 import BRODMANN_9      # int, == AREA_ID
    from .brodmann_area_9 import ANATOMY
    from .brodmann_area_9 import LEFT_CONFIG
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
    - Must not add a `sub_region` field INSIDE LEFT_CONFIG. That field
      is only used in multi-system per-block configs; for single-
      system areas, the package-level SUB_REGION serves the
      disambiguation role.
    - Must not add a medial-DMPFC config block to area 9 without first
      documenting the schema extension (multi-sub-region-within-one-
      family). The medial extension is currently documented as a
      caveat in ANATOMY, not as a compute contribution.
    - Must not contain runtime logic of any kind.
    - Must not import or reference the left hemisphere's area-9
      package. Cross-midline WM exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access.
    - Must not diverge in structure from the right hemisphere's area-9
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only by the
      directional mirror described above.
"""