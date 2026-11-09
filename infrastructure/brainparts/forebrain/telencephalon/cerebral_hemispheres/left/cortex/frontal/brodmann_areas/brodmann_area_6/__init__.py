"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_6
====================================================================================================================

Brodmann area 6 (premotor cortex and supplementary motor area) — left
hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 6, says which compute sub-regions own it,
and supplies the per-area weights that the owning sub-regions' `encode()`
methods read. It defines no classes and no functions; the public surface is
the exports listed under "EXPORTS".

If you are looking for the computation area 6 participates in, it lives in
TWO compute sub-regions:
    `.../frontal/cortex/premotor_cortex/`              (lateral area 6)
    `.../frontal/cortex/supplementary_motor_cortex/`   (medial area 6)
Area 6 is the one Brodmann area that spans two functional sub-regions,
because the anatomical strip is continuous while the function is not:
lateral area 6 is premotor (movement preparation), medial area 6 is the
supplementary motor area (movement sequencing). This package is the
*label*; the two compute sub-regions are the *agents*.

IDENTITY
--------
    AREA_ID    = 6
    NAME       = "Brodmann area 6 (premotor cortex + supplementary motor area)"
    SYSTEM     = ["premotor_cortex", "supplementary_motor_cortex"]
    SUB_REGION = None         # both systems are leaf sub-regions
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping; see note below

Note on SUB_REGION being None: SUB_REGION exists to disambiguate within a
*family* system (like prefrontal_cortex, which has five sub-regions). Here
the two systems (premotor_cortex, supplementary_motor_cortex) are both
leaf sub-regions — there is no further disambiguation needed. Area 6 is
the first frontal registry entry whose SYSTEM has more than one element
while SUB_REGION is still None; area 8 will follow the same shape (two
leaf systems: premotor + prefrontal), and area 47 will be the mirror
(prefrontal family, so SUB_REGION is set).

Note on GROUPING being None: area 6's two functional halves (lateral
premotor, medial SMA) are not a *named sub-grouping* within a sub-region —
they are subdivisions that belong to two separate compute sub-regions.
GROUPING names sub-groupings within a single sub-region (like brocas_area
within VLPFC); area 6's split is at the system level, not the grouping
level. It is None.

THE PER-SYSTEM CONFIG BLOCK PATTERN
-----------------------------------
Area 6's LEFT_CONFIG is not a flat dict. It has one block per owning
system:

    LEFT_CONFIG = {
        "premotor_cortex":             { ... feature + connectivity ... },
        "supplementary_motor_cortex":  { ... feature + connectivity ... },
    }

Each owning sub-region reads ITS OWN block — `premotor_cortex/` reads
`LEFT_CONFIG["premotor_cortex"]`, and `supplementary_motor_cortex/` reads
`LEFT_CONFIG["supplementary_motor_cortex"]`. Neither sub-region sees the
other's block. The blocks share key names for the shared conceptual
dimensions (feature names, connectivity partner names) but the values are
independent.

There is NO sum-to-1 invariant across the two blocks. They are not two
halves of one budget; they are two independent configs that happen to
live in the same package because the anatomical strip is continuous.
Premotor's block is normalised by premotor's own internal logic (its
feature weights are relative importances within premotor's computation);
SMA's block is normalised by SMA's own internal logic. A naive
"premotor_weight + sma_weight == 1" check would be wrong — there is no
such pair.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 6 (premotor cortex + supplementary motor area)",
        "system": "premotor_cortex + supplementary_motor_cortex",
        "sub_region": None,
        "grouping": None,
        "location": "anterior to the primary motor cortex (area 4), "
                    "extending from the lateral convexity (lateral "
                    "area 6: premotor cortex) across the superior "
                    "frontal gyrus and onto the medial wall (medial "
                    "area 6: supplementary motor area, on the medial "
                    "surface of the superior frontal gyrus and the "
                    "paracentral lobule)",
        "cytoarchitecture": "dysgranular cortex — a thin but present "
                            "layer IV, transitional between the "
                            "agranular area 4 (posterior) and the "
                            "granular prefrontal cortex (anterior). "
                            "The transition is why the lateral strip "
                            "(premotor) and the medial strip (SMA) are "
                            "the same Brodmann number: the "
                            "cytoarchitectonic signature is continuous "
                            "across them, even though the functional "
                            "roles are not.",
        "notes": (
            "Area 6 is the preparatory motor strip anterior to area 4. "
            "It is one continuous Brodmann area with two functionally "
            "distinct subdivisions: the LATERAL part is premotor cortex "
            "(PMd and PMv), which prepares movements, selects movement "
            "parameters (direction, force, grasp type), and holds motor "
            "intentions; the MEDIAL part is the supplementary motor "
            "area (SMA and pre-SMA), which sequences complex and "
            "internally-generated movements and coordinates bimanual "
            "actions. The two subdivisions project to different parts "
            "of area 4 and have different computational roles, but they "
            "share a cytoarchitectonic signature. This is why area 6 is "
            "the first multi-system registry entry: the anatomy is one "
            "area, the function is two. On the left, premotor's "
            "dominant role is the ventral premotor's (PMv) coupling to "
            "Broca's area for speech-articulatory planning, and SMA's "
            "dominant role is language-articulatory sequence planning. "
            "On the right, PMd's spatial reaching/grasping role and "
            "SMA's spatial/bimanual sequencing role dominate. The "
            "left/right split is directional, not complementary."
        ),
    }

CONFIG (LEFT)
-------------
Area 6's LEFT_CONFIG has two per-system blocks. Each block has its own
feature weights and connectivity priors; the two are independent.

    LEFT_CONFIG = {

        # ============================================================
        # PREMIER BLOCK — premotor_cortex (lateral area 6: PMd + PMv)
        # ============================================================
        # LEFT bias: PMv (ventral premotor) dominates — its speech-
        # articulatory planning role via coupling to Broca's area is the
        # left's signature. PMd (dorsal premotor) is present but
        # secondary; spatial reaching/grasping is more right-weighted.
        "premotor_cortex": {
            # ---- feature emphases ----
            "movement_preparation":    0.75,   # holding a prepared
                                               # movement ready to
                                               # execute
            "movement_parameter_selection": 0.70,  # direction, force,
                                                   # grasp type
            "motor_imagery":           0.65,   # simulating movement
                                               # without executing
            "action_observation":      0.55,   # recognising others'
                                               # actions for imitation
            "speech_articulatory_planning": 0.75,  # PMv's coupling
                                                   # to Broca's area;
                                                   # the left's anchor
            "reaching_grasping_planning":   0.40,  # PMd's spatial
                                                   # role; more
                                                   # right-weighted

            # ---- connectivity priors ----
            "to_primary_motor":        0.85,   # premotor → primary
                                               # motor is the strongest
                                               # link in the motor
                                               # hierarchy (structural,
                                               # identical across sides)
            "to_prefrontal_cortex":    0.65,   # goals come down from
                                               # PFC to constrain
                                               # prepared movements
            "to_supplementary_motor":  0.55,   # PM and SMA coordinate;
                                               # PM prepares single
                                               # movements, SMA
                                               # sequences them
            "to_parietal":             0.60,   # reaching/grasping
                                               # planning uses
                                               # parietal spatial
                                               # affordances
            "to_broca_area_44":        0.60,   # PMv ↔ area 44 for
                                               # speech-articulatory
                                               # planning; the left's
                                               # signature coupling
            "to_basal_ganglia":        0.60,   # gating of prepared
                                               # movements
            "to_cerebellum":           0.55,   # cerebellar timing
                                               # modulation of
                                               # prepared movements
            "to_commissures":          0.35,   # cross-midline motor
                                               # planning
        },

        # ============================================================
        # SECOND BLOCK — supplementary_motor_cortex (medial area 6:
        # SMA + pre-SMA)
        # ============================================================
        # LEFT bias: language-articulatory sequence planning dominates
        # (the left SMA's speech-sequencing role). Spatial/bimanual
        # sequence planning is present but secondary; that is the
        # right's signature.
        "supplementary_motor_cortex": {
            # ---- feature emphases ----
            "movement_sequencing":     0.75,   # ordering a series of
                                               # movements
            "internally_generated_movement": 0.70,  # movements not
                                                    # cued by external
                                                    # stimuli
            "bimanual_coordination":   0.40,   # left SMA's bimanual
                                               # role; more right-
                                               # weighted
            "motor_sequence_learning": 0.70,   # acquiring new
                                               # sequences
            "language_articulatory_sequence": 0.75,  # speech sequence
                                                     # planning; the
                                                     # left SMA's anchor
            "spatial_movement_sequence":     0.45,   # right-weighted;
                                                     # present but not
                                                     # dominant here

            # ---- connectivity priors ----
            "to_primary_motor":        0.55,   # SMA → primary motor
                                               # (sequences feed into
                                               # execution)
            "to_premotor_cortex":      0.55,   # SMA ↔ PM coordination
            "to_prefrontal_cortex":    0.60,   # PFC supplies the goal
                                               # structure that SMA
                                               # sequences
            "to_broca_area_44":        0.50,   # SMA ↔ area 44 for
                                               # speech sequence
                                               # planning
            "to_basal_ganglia":        0.60,   # gating of sequence
                                               # elements; SMA ↔
                                               # striatum is a key
                                               # sequence-learning loop
            "to_cerebellum":           0.55,   # cerebellar timing of
                                               # sequences
            "to_commissures":          0.50,   # cross-midline bimanual
                                               # coordination; higher
                                               # than the premotor
                                               # block's 0.35 because
                                               # bimanual sequencing
                                               # needs the two SMAs
                                               # to coordinate
        },
    }

    Notes on the weights:
      - Feature weights are multipliers on features extracted by the
        corresponding sub-region. Within each block, the anchor
        features are the left's signature roles:
            premotor block: speech_articulatory_planning (0.75) —
                            PMv ↔ Broca's coupling
            SMA block:      language_articulatory_sequence (0.75) —
                            the left SMA's speech-sequencing role
        The right-weighted features (reaching_grasping_planning,
        spatial_movement_sequence) are present at 0.40 / 0.45 — not
        zero, because the left is still capable of these, but clearly
        below the anchors.
      - The two blocks are INDEPENDENT. There is no constraint that
        relates premotor's weights to SMA's weights; they are consumed
        by different compute sub-regions and are normalised by
        different internal logic.
      - Within each block, feature weights are relative importances
        (their ratios matter, not their sum); the connectivity priors
        are independent magnitudes (higher = stronger coupling), not
        constrained to sum.
      - `to_primary_motor` differs between blocks: 0.85 in the
        premotor block (premotor → primary motor is the dominant
        input) vs 0.55 in the SMA block (SMA → primary motor is one
        of several SMA outputs; SMA also projects to premotor, basal
        ganglia, and brainstem). This is not an inconsistency — the
        two sub-regions have different roles in the motor hierarchy.
      - `to_commissures` differs between blocks: 0.35 in the
        premotor block vs 0.50 in the SMA block. The higher SMA
        prior reflects bimanual coordination needing both SMAs to
        exchange sequence state across the midline. Premotor's lower
        prior reflects single-movement preparation being more
        intra-hemispheric.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) within each block, the anchor
        features match the left's functional signature; (b) the
        structural priors (to_primary_motor, to_basal_ganglia,
        to_cerebellum) are the ones that stay roughly equal across
        hemispheres when mirrored, while the lateralised priors
        (to_broca_area_44, to_parietal, to_commissures) directionally
        change.

MIRROR PATTERN
--------------
Area 6's config is a directional mirror, applied per-block. Each
feature/connectivity key is compared between left and right
INDEPENDENTLY within its block; there is no cross-block pairing.

    Left's premotor block        Right's premotor block
    speech_artic_planning 0.75   speech_artic_planning 0.30
    reaching_grasping     0.40   reaching_grasping     0.75
    to_broca_area_44      0.60   to_broca_area_44      0.30
    to_parietal           0.60   to_parietal           0.75

    Left's SMA block             Right's SMA block
    language_artic_seq    0.75   language_artic_seq    0.35
    spatial_movement_seq  0.45   spatial_movement_seq  0.75
    to_broca_area_44      0.50   to_broca_area_44      0.25
    to_commissures        0.50   to_commissures        0.65

The relationship is directional in each block. Structural priors
(to_primary_motor, to_basal_ganglia, to_cerebellum) are IDENTICAL
across hemispheres within a block. The mirror test must check:
    1. within-block direction on lateralised keys (per-block, per-key);
    2. within-block equality on structural keys (per-block, per-key);
    3. no cross-block relations are checked (there are none to check).

EXPORTS
-------
    from .brodmann_area_6 import BRODMANN_6      # int, == AREA_ID
    from .brodmann_area_6 import ANATOMY
    from .brodmann_area_6 import LEFT_CONFIG
    from .brodmann_area_6 import SYSTEM          # list, two elements
    from .brodmann_area_6 import SUB_REGION      # None
    from .brodmann_area_6 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_6`) — area 6 is a direct child of
brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in premotor_cortex/ and
      supplementary_motor_cortex/, not here.
    - Must not import `premotor_cortex/` or
      `supplementary_motor_cortex/` (cycle; the compute imports from
      here, not the other way round).
    - Must not add a top-level (non-per-system) `LEFT_CONFIG` that
      mixes the two blocks. The per-system block structure is the
      contract: each owning sub-region reads its own block, and there
      is no combined "area-6-as-a-whole" config. Merging the blocks
      would force one sub-region to see the other's weights, which is
      exactly the cross-sub-region information leak the block
      structure prevents.
    - Must not introduce a `premotor_weight + sma_weight = 1.0`
      constraint. There is no such pair. The blocks are independent
      because they are consumed independently.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-6
      package — same AREA_ID, SYSTEM, SUB_REGION (None), GROUPING
      (None), ANATOMY, same block keys, same feature/connectivity key
      names inside each block. Only the values differ, and only by
      the per-block directional mirror.
"""