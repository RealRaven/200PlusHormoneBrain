"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_6
=====================================================================================================================

Brodmann area 6 (premotor cortex and supplementary motor area) — right
hemisphere.

Mirror of the left area-6 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 6, says
which compute sub-regions own it, and supplies the per-area weights that
the owning sub-regions' `encode()` methods read. It defines no classes and
no functions; the public surface is the exports listed under "EXPORTS".

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
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping; see left area-6 docstring

The SYSTEM list, SUB_REGION (None), and GROUPING (None) are identical to
the left's — anatomy, system mapping, and grouping do not lateralise,
only weights do. The fields are documented in detail in the left area-6
docstring, including the per-system block pattern that area 6 introduces.

THE PER-SYSTEM CONFIG BLOCK PATTERN
-----------------------------------
Area 6's RIGHT_CONFIG has one block per owning system, exactly as the
left's does:

    RIGHT_CONFIG = {
        "premotor_cortex":             { ... feature + connectivity ... },
        "supplementary_motor_cortex":  { ... feature + connectivity ... },
    }

Each owning sub-region reads ITS OWN block — `premotor_cortex/` reads
`RIGHT_CONFIG["premotor_cortex"]`, and `supplementary_motor_cortex/`
reads `RIGHT_CONFIG["supplementary_motor_cortex"]`. Neither sub-region
sees the other's block.

There is NO sum-to-1 invariant across the two blocks. They are not two
halves of one budget; they are two independent configs. This is
documented at length in the left area-6 docstring and is not repeated
here. The block structure is the contract, on both hemispheres.

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
            "parameters, and holds motor intentions; the MEDIAL part is "
            "the supplementary motor area (SMA and pre-SMA), which "
            "sequences complex and internally-generated movements and "
            "coordinates bimanual actions. On the RIGHT, PMd's spatial "
            "reaching/grasping role and SMA's spatial/bimanual "
            "sequencing role dominate. The speech-articulatory roles "
            "(PMv ↔ Broca's area, SMA language-sequencing) are present "
            "but secondary — the left hemisphere is the primary owner "
            "of those. The left/right split is directional, not "
            "complementary — the right's area 6 is spatial/limb-forward, "
            "not 'the left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 6's RIGHT_CONFIG has two per-system blocks. Each block has its own
feature weights and connectivity priors; the two are independent.

    RIGHT_CONFIG = {

        # ============================================================
        # FIRST BLOCK — premotor_cortex (lateral area 6: PMd + PMv)
        # ============================================================
        # RIGHT bias: PMd (dorsal premotor) dominates — its spatial
        # reaching/grasping planning role is the right's signature.
        # PMv (ventral premotor) is present but secondary; its
        # speech-articulatory coupling is more left-weighted.
        "premotor_cortex": {
            # ---- feature emphases ----
            "movement_preparation":    0.75,   # holding a prepared
                                               # movement ready to
                                               # execute (structural
                                               # role, equal to left)
            "movement_parameter_selection": 0.70,  # direction, force,
                                                   # grasp type
                                                   # (structural role)
            "motor_imagery":           0.65,   # simulating movement
                                               # without executing
            "action_observation":      0.55,   # recognising others'
                                               # actions
            "speech_articulatory_planning": 0.30,  # PMv ↔ Broca's
                                                   # coupling; much
                                                   # reduced on the
                                                   # right
            "reaching_grasping_planning":   0.75,  # PMd's spatial
                                                   # role; the right's
                                                   # anchor feature

            # ---- connectivity priors ----
            "to_primary_motor":        0.85,   # structural, identical
                                               # across hemispheres
            "to_prefrontal_cortex":    0.65,   # structural
            "to_supplementary_motor":  0.55,   # structural
            "to_parietal":             0.75,   # UP from the left's
                                               # 0.60 — the right's
                                               # PMd is more strongly
                                               # coupled to parietal
                                               # spatial affordances
            "to_broca_area_44":        0.30,   # DOWN from the left's
                                               # 0.60 — PMv ↔ Broca's
                                               # coupling is
                                               # left-dominant
            "to_basal_ganglia":        0.60,   # structural
            "to_cerebellum":           0.55,   # structural
            "to_commissures":          0.40,   # UP mildly from the
                                               # left's 0.35; the
                                               # right's spatial
                                               # reaching/grasping
                                               # planning feeds into
                                               # bimanual coordination
                                               # via the commissures
        },

        # ============================================================
        # SECOND BLOCK — supplementary_motor_cortex (medial area 6:
        # SMA + pre-SMA)
        # ============================================================
        # RIGHT bias: spatial/bimanual sequence planning dominates.
        # Language-articulatory sequence planning is present but
        # secondary; that is the left's signature.
        "supplementary_motor_cortex": {
            # ---- feature emphases ----
            "movement_sequencing":     0.75,   # ordering a series of
                                               # movements (structural)
            "internally_generated_movement": 0.70,  # structural
            "bimanual_coordination":   0.75,   # UP from the left's
                                               # 0.40 — the right
                                               # SMA's bimanual role
                                               # is its anchor
            "motor_sequence_learning": 0.70,   # structural
            "language_articulatory_sequence": 0.35,  # DOWN from the
                                                     # left's 0.75
            "spatial_movement_sequence":     0.75,   # UP from the
                                                     # left's 0.45 —
                                                     # the right SMA's
                                                     # anchor feature

            # ---- connectivity priors ----
            "to_primary_motor":        0.55,   # structural
            "to_premotor_cortex":      0.55,   # structural
            "to_prefrontal_cortex":    0.60,   # structural
            "to_broca_area_44":        0.25,   # DOWN from the left's
                                               # 0.50
            "to_basal_ganglia":        0.60,   # structural
            "to_cerebellum":           0.55,   # structural
            "to_commissures":          0.65,   # UP from the left's
                                               # 0.50 — the right
                                               # SMA's bimanual
                                               # sequencing needs to
                                               # exchange sequence
                                               # state with the left
                                               # SMA more than the
                                               # left needs to
                                               # exchange with the
                                               # right (the right has
                                               # the spatial half of
                                               # the bimanual sequence)
        },
    }

    Notes on the weights:
      - Feature weights are multipliers on features extracted by the
        corresponding sub-region. Within each block, the anchor
        features are the right's signature roles:
            premotor block: reaching_grasping_planning (0.75) — PMd's
                            spatial reaching/grasping role
            SMA block:      spatial_movement_sequence (0.75) and
                            bimanual_coordination (0.75) — the right
                            SMA's spatial/bimanual role
        The left-weighted features (speech_articulatory_planning,
        language_articulatory_sequence) are present at 0.30 / 0.35 —
        not zero, because the right is still capable of these, but
        clearly below the anchors.
      - The two blocks are INDEPENDENT. There is no constraint that
        relates premotor's weights to SMA's weights; they are consumed
        by different compute sub-regions and are normalised by
        different internal logic. Same as the left.
      - Structural priors are IDENTICAL across hemispheres:
            premotor block: to_primary_motor 0.85, to_prefrontal_cortex
                            0.65, to_supplementary_motor 0.55,
                            to_basal_ganglia 0.60, to_cerebellum 0.55
            SMA block:      to_primary_motor 0.55, to_premotor_cortex
                            0.55, to_prefrontal_cortex 0.60,
                            to_basal_ganglia 0.60, to_cerebellum 0.55
        These encode anatomical connectivity, not lateralised function.
      - Lateralised priors directionally mirror:
            premotor block: to_parietal UP (0.60→0.75), to_broca_area_44
                            DOWN (0.60→0.30), to_commissures UP mildly
                            (0.35→0.40)
            SMA block:      to_broca_area_44 DOWN (0.50→0.25),
                            to_commissures UP (0.50→0.65)
      - The `to_commissures: 0.65` prior in the right SMA block is the
        highest commissural prior in area 6 on either side, and the
        highest in area 6's two blocks on the right. It reflects the
        right SMA's role as the primary driver of bimanual sequencing:
        the right proposes the spatial/bimanual plan, the left supplies
        the fine/distal component, and the two SMAs need to exchange
        sequence state across the midline to keep the bimanual action
        coherent. This is the anatomical basis for the specific
        prediction that a commissure lesion should impair bimanual
        sequencing more severely than single-limb movement preparation.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) within each block, the anchor
        features match the right's functional signature; (b) structural
        priors are identical across hemispheres within a block;
        (c) lateralised priors directionally mirror.

MIRROR PATTERN
--------------
This area's config is a directional mirror, applied per-block. Each
feature/connectivity key is compared between left and right
INDEPENDENTLY within its block; there is no cross-block pairing. This
is the same pattern the left area-6 docstring documents, evaluated in
the opposite direction:

    Left's premotor block        Right's premotor block
    speech_artic_planning 0.75   speech_artic_planning 0.30
    reaching_grasping     0.40   reaching_grasping     0.75
    to_broca_area_44      0.60   to_broca_area_44      0.30
    to_parietal           0.60   to_parietal           0.75
    to_commissures        0.35   to_commissures        0.40

    Left's SMA block             Right's SMA block
    language_artic_seq    0.75   language_artic_seq    0.35
    spatial_movement_seq  0.45   spatial_movement_seq  0.75
    bimanual_coordination 0.40   bimanual_coordination 0.75
    to_broca_area_44      0.50   to_broca_area_44      0.25
    to_commissures        0.50   to_commissures        0.65

The relationship is directional in each block. Structural priors
(to_primary_motor, to_prefrontal_cortex, to_supplementary_motor,
to_basal_ganglia, to_cerebellum) are IDENTICAL across hemispheres
within a block. The mirror test must check:
    1. within-block direction on lateralised keys (per-block, per-key);
    2. within-block equality on structural keys (per-block, per-key);
    3. no cross-block relations are checked (there are none to check).

EXPORTS
-------
    from .brodmann_area_6 import BRODMANN_6      # int, == AREA_ID
    from .brodmann_area_6 import ANATOMY
    from .brodmann_area_6 import RIGHT_CONFIG
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
    - Must not add a top-level (non-per-system) `RIGHT_CONFIG` that
      mixes the two blocks. The per-system block structure is the
      contract on both hemispheres: each owning sub-region reads its
      own block, and there is no combined "area-6-as-a-whole" config.
    - Must not introduce a `premotor_weight + sma_weight = 1.0`
      constraint. There is no such pair.
    - Must not import or reference the left hemisphere's area-6 package.
      Cross-midline motor sequencing goes through
      `telencephalon/commissures/`, never through direct registry
      access. The right SMA's `to_commissures: 0.65` prior is the
      highest in area 6 on either side, precisely because the right's
      bimanual sequencing must reach the left's fine/distal execution
      via the commissures — direct registry access would bypass the
      commissural delay and bandwidth that the model is supposed to
      exercise, and would silently make the bimanual prediction
      untestable.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-6
      package — same AREA_ID, SYSTEM, SUB_REGION (None), GROUPING
      (None), ANATOMY, same block keys, same feature/connectivity key
      names inside each block. Only the values differ, and only by
      the per-block directional mirror.
"""