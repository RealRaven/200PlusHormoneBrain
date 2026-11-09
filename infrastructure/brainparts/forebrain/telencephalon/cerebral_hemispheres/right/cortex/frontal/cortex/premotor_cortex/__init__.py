"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.premotor_cortex
===============================================================================================================

The PREMOTOR CORTEX — right hemisphere. A LEAF compute sub-region of the
frontal cortex, and one of the two stateful leaf sub-regions (the other is
supplementary_motor_cortex).

Mirror of the left premotor package. Premotor is the movement-PREPARATION
core of the frontal motor hierarchy: given a goal, it selects a candidate
movement, chooses its parameters, and holds it as a prepared program ready
to be sequenced (by SMA) and executed (by primary motor). On the RIGHT, the
movements prepared are predominantly gross/proximal and spatially-directed
— reaching, grasping, orienting, postural adjustment — the PMd role. The
speech-articulatory role (PMv) is present but secondary. The mechanics of
preparation are the same as on the left; the content and its lateralised
weighting are mirrored.

Premotor is called SECOND in the frontal cortex's composition order (after
prefrontal, before SMA and primary motor). It reads prefrontal's published
goals, WM contents, and value signals from peer_input, and it publishes its
prepared_programs for SMA and primary motor to consume.

LEAF-LEVEL SHAPE (the pattern for the other two leaf sub-regions)
-----------------------------------------------------------------
Identical to the left. Premotor is a LEAF: no internal composition, no
per-sub-sub-region shares, no nested peer_input routing. It:

    - consumes one registry area's config DIRECTLY
    - owns its own persistent state (prepared_programs)
    - exposes the standard encode() signature
    - publishes its contribution for downstream sub-regions

The registry-area-to-config mapping is one-to-one: area 6's
"premotor_cortex" block is the entire config source; RIGHT_PREMOTOR_CONFIG
adds only the state parameters and thresholds.

PREMOTOR'S REGISTRY-AREA SOURCE
-------------------------------
Premotor has ONE frontal-registry area source:

    brodmann_area_6/        the "premotor_cortex" block (the LATERAL
                            area 6; sub_region = None, because
                            premotor_cortex is a leaf system named in
                            SYSTEM directly)

Its config (in `brodmann_area_6.RIGHT_CONFIG["premotor_cortex"]`)
provides the premotor feature weights and connectivity priors. On the
right, the weights lean toward reaching/grasping planning (0.75) and
away from speech_articulatory_planning (0.30); the connectivity priors
reflect the right's stronger parietal coupling (0.75 vs the left's 0.60)
and weaker Broca's-area coupling (0.30 vs 0.60).

Because there is only one area source, there is NO share weight — no
`premotor_weight` field. Same pattern as the left.

PREMOTOR OWNS PERSISTENT STATE
-------------------------------
Identical structure to the left:

    prepared_programs    a list of candidate movement programs,
                         each with selected parameters and an
                         activation level. On the right, the targets
                         are predominantly spatial (objects to reach,
                         locations to orient toward, postures to
                         adopt); on the left, they are
                         predominantly speech-articulatory (phonemes
                         to produce, words to articulate). The
                         state structure (target, parameters,
                         activation) is identical.

The state is threaded by FrontalCortex's step(): premotor receives its
state dict from last tick, returns a new one, FrontalCortex stores it.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

Identical to the left. Steps:

        1. Read peer_input — premotor is called second, so it has
           access to peer_input["prefrontal_cortex"] (goals, WM,
           value signals).
        2. Extract premotor features. On the right, extraction weights
           spatial affordances and reaching/grasping candidates
           higher than speech-articulatory candidates.
        3. Apply area 6's premotor_cortex block config to weight the
           features.
        4. Prepare and update prepared_programs (refresh, decay,
           insert, evict, capacity).
        5. Compute premotor's contribution (prepared_programs plus
           feature dict).
        6. Return (contribution, new_state).

PROGRAM PREPARATION (the premotor-specific operational pattern)
---------------------------------------------------------------
Same program structure and dynamics as the left:

    {
        "program_id":     unique within-hemisphere monotonic ID,
        "target":         on the right, predominantly a spatial
                          object / location / posture; on the left,
                          predominantly a speech-articulatory unit,
        "parameters": {
            "direction":  unit vector or symbolic,
            "force":      scalar,
            "velocity":   scalar,
            "grasp_type": categorical,
            "articulatory_target": phonological representation,
            "target_frame": "egocentric" or "allocentric"; on the
                          right, more egocentric due to the strong
                          PMd-parietal coupling's body-relative
                          frame, but with allocentric available for
                          spatial navigation,
        },
        "activation":     scalar in [0, 1],
    }

The activation dynamics (refresh, decay, eviction, capacity) are
identical — same parameters in RIGHT_PREMOTOR_CONFIG as the left's.
The difference is which candidate programs are being prepared:
right's candidates are spatial/reaching, left's are
speech-articulatory.

The parameter-selection logic (choose direction, force, grasp type,
target) is the same. On the right, the spatial parameters (direction,
target_frame) are more finely selected because the right's premotor
is doing more spatial work; on the left, the articulatory parameters
(articulatory_target) are more finely selected.

FEATURE EXTRACTION (the premotor's inputs)
------------------------------------------
    From sensory_input:
        target_affordances   — on the right, spatial affordances
                               (reachable objects, graspable items,
                               navigable locations) are weighted
                               higher; articulable sounds are
                               present but secondary
        goal_relevant_objects — objects the goal is about

    From top_down:
        (same four modulators as left: basal_forebrain_gain,
        cingulate_control, basal_ganglia_gate, cerebellar_feedback)
        cerebellar_feedback — on the right, this carries more weight
                              in the parameter selection because the
                              right's reaching/grasping relies more
                              on cerebellar timing and error-
                              correction (the left's speech-articulatory
                              execution is more cortically driven)

    From peer_input:
        (Premotor reads ONLY peer_input["prefrontal_cortex"].)
        goal                  — from DMPFC (via prefrontal's `goals`)
        working_memory        — DLPFC's held contents (on the right,
                                spatial WM contents bias which
                                spatial targets are prepared)
        integrated_value      — VMPFC's value signal (affective
                                valuation of targets)
        stimulus_value        — OFC's per-stimulus value

    Feature extraction rules are documented in the premotor class.
    On the right, extraction weights spatial affordances higher than
    articulatory ones.

CONTRIBUTION SHAPE
------------------
    contribution = {
        # The six premotor features (weighted by area 6's premotor
        # block config)
        "movement_preparation":        <scalar>,
        "movement_parameter_selection":<scalar>,
        "motor_imagery":               <scalar>,
        "action_observation":          <scalar>,
        "speech_articulatory_planning":<scalar>,
        "reaching_grasping_planning":  <scalar>,

        # Operational output
        "prepared_programs": [ {program dict}, ... ],
        "top_program":     highest-activation program, or None,
    }

The schema is identical. The right's contents are predominantly
spatial/reaching (reaching_grasping_planning feature high;
prepared_programs targets spatial).

RIGHT-SPECIFIC BIAS
------------------
Same class as the left premotor; the RIGHT config changes the weights
(via area 6's premotor block config):

    reaching_grasping_planning     higher (0.75) — the right's
                                   anchor feature; PMd's spatial
                                   role
    speech_articulatory_planning   lower (0.30)
    to_parietal                    higher (0.75) — reaching/grasping
                                   relies on parietal spatial
                                   affordances
    to_broca_area_44               lower (0.30) — speech-articulatory
                                   planning is more left-lateralised
    to_commissures                 higher (0.40) — the right's
                                   gross/positional prepared programs
                                   are the ones that need to reach
                                   the left for bimanual coherence

The state structure (prepared_programs, capacity, decay rate,
activation threshold), the encoding pipeline, the parameter-selection
logic, and the contribution shape are IDENTICAL across hemispheres.
Only the config values inside area 6's premotor block differ. LEFT
mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left premotor. Cross-midline premotor
exchange is the coordination of prepared movement programs between
hemispheres. On the right, the cases emphasise the right's role as the
SENDER of the gross/positional component:

    - Bimanual coordination (the right's primary cross-midline
      role). For a bimanual action, the right's premotor prepares
      the gross/positional component (the reaching, the
      stabilisation, the whole-limb positioning) and the left's
      prepares the fine/distal component (the finger shaping, the
      precision grip, the articulatory fine-tuning). The two have to
      be combined into a coherent bimanual action, and the
      combination happens via the commissures. The right's
      `to_commissures` prior (0.40) is higher than the left's
      (0.35) because the right's gross programs are the ones that
      more often need to cross — the gross positioning has to be
      shared for the fine execution to be coordinated. A commissure
      lesion on the right would therefore impair bimanual
      coordination more severely than one on the left.

    - Prosody-to-speech motor coordination. The right's PMv prepares
      prosodic articulatory programs (intonation contours,
      expressive facial movements for speech); the left's PMv
      prepares lexical articulatory programs (phonemes, words).
      The two have to combine for fluent, intoned speech. Direct
      import would silently merge them and make the "flat speech
      with intact content" failure mode untestable.

    - Postural / reaching coordination. The right's premotor often
      prepares the postural adjustment that enables the left's
      fine-motor target. The postural program reaches the left via
      the commissures; the left's fine-motor execution proceeds once
      the posture is set.

All three are commissural. The bimanual-coordination case is the
right's most frequently exercised cross-midline pattern, and the
asymmetry (right sends more than left for bimanual tasks) is
testable — a right-sided commissure lesion should impair bimanual
coordination more than a left-sided one.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not compose sub-sub-regions. Premotor is a LEAF.
    - Must not add a `premotor_weight` field.
    - Must not carry peer_input assumptions beyond prefrontal.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not hold module-level mutable state.
    - Must not implement program sequencing (SMA's job) or program
      execution (primary motor's job).
    - Must not read area 6's premotor block config directly — the
      config is passed in via `config`.
    - Must not read area 6's supplementary_motor block.
    - Must not change the state parameters (capacity, decay rate,
      refresh rate, activation threshold) on the right. These are
      STRUCTURAL — equal across hemispheres. The right's spatial
      character lives in the source config's feature weights, not in
      the state parameters. A test that assumed "right premotor has
      different capacity or decay" would fail; the parameters are
      equal, and the lateralisation is entirely in what gets prepared.
    - Must not import or reference the left premotor. Cross-midline
      exchange goes through `telencephalon/commissures/`. The
      bimanual-coordination case is the prime example: direct import
      would silently merge the right's gross programs with the left's
      fine programs and make the "commissure lesion impairs bimanual
      coordination" prediction untestable.
    - Must not diverge in structure from the left premotor — same
      class, same encode() signature, same state structure, same
      parameter-selection logic. Only area 6's premotor block config
      differs.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_PREMOTOR_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_6",
        "source_block": "premotor_cortex",

        # prepared_programs state parameters (STRUCTURAL — identical
        # to the left's).
        "prepared_programs_capacity":        5,
        "activation_decay_rate":             0.10,
        "activation_refresh_rate":           0.20,
        "activation_threshold":              0.20,

        # Parameter-selection thresholds (STRUCTURAL).
        "parameter_selection_confidence_threshold": 0.4,
    }

    Area 6's premotor_cortex block config
    (brodmann_area_6.RIGHT_CONFIG["premotor_cortex"]) is supplied by
    FrontalCortex at construction. It provides the feature weights
    and connectivity priors, with the right's reaching/grasping lean.

    RIGHT_PREMOTOR_CONFIG is IDENTICAL to LEFT_PREMOTOR_CONFIG except
    that it names brodmann_area_6.RIGHT_CONFIG["premotor_cortex"]. The
    state parameters and thresholds are STRUCTURAL — equal across
    hemispheres.

    Two separate tests are needed:
        1. RIGHT_PREMOTOR_CONFIG == LEFT_PREMOTOR_CONFIG on state
           parameters and thresholds (structural equality).
        2. brodmann_area_6.RIGHT_CONFIG["premotor_cortex"] is a
           directional mirror of the left's premotor block. NOTE: the
           SMA block is tested separately against its own right
           counterpart; the mirror test does NOT check relations
           between the two blocks.

EXPORTS
-------
    from .premotor_cortex import PremotorCortex
    from .premotor_cortex import RIGHT_PREMOTOR_CONFIG

    The class implements the leaf sub-region encode() signature that
    FrontalCortex expects. No dlpfc_weight-style precondition.

    NOTE: This package's construction does NOT depend on the pending
    area-9 amendment (that affects DLPFC only).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  PremotorCortex class, import area 6's RIGHT_CONFIG premotor block,
  build RIGHT_PREMOTOR_CONFIG, instantiate the class, expose the class
  and the config.
- The class implements the leaf sub-region encode() signature. It
  owns prepared_programs state (non-empty persistent dict).
- The class is STATEFUL — it carries prepared_programs across ticks.
  No module-level mutable state.
- Program preparation is broken into documented, unit-testable
  functions (`_candidate_programs`, `_select_parameters`,
  `_update_prepared_programs`, `_select_top_program`). Same functions
  as on the left; only the config inputs to them differ (right's
  extraction weights spatial affordances higher).
- Feature extraction is a documented, unit-testable function.
- The class does not read area 6's SMA block.
- The class does not import or access any peer sub-sub-region's
  state.
- The class does not implement sequencing or execution.
- RIGHT_PREMOTOR_CONFIG is structurally identical to
  LEFT_PREMOTOR_CONFIG except for the source block reference. State
  parameters and thresholds are STRUCTURAL.
- Program IDs are monotonic within a hemisphere; cross-hemisphere
  collisions fine.
- Must not import or reference the left premotor. Cross-midline
  exchange goes through `telencephalon/commissures/`.
"""