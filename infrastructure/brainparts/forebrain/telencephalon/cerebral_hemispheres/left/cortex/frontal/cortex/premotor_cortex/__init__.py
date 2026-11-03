"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.premotor_cortex
==============================================================================================================

The PREMOTOR CORTEX — left hemisphere. A LEAF compute sub-region of the
frontal cortex, and one of the two stateful leaf sub-regions (the other is
supplementary_motor_cortex).

Premotor is the movement-PREPARATION core of the frontal motor hierarchy:
given a goal, it selects a candidate movement, chooses its parameters
(direction, force, grasp type, target), and holds it as a prepared program
ready to be sequenced (by SMA) and executed (by primary motor). It is the
bridge between the executive's goal (from prefrontal) and the executable
motor command (from primary motor).

Premotor is called SECOND in the frontal cortex's composition order
(after prefrontal, before SMA and primary motor). It reads prefrontal's
published goals, WM contents, and value signals from peer_input, and it
publishes its prepared_programs for SMA and primary motor to consume.

LEAF-LEVEL SHAPE (the pattern for the other two leaf sub-regions)
-----------------------------------------------------------------
Unlike prefrontal (a FAMILY with five sub-sub-regions), premotor is a
LEAF: it has no internal composition, no per-sub-sub-region shares, no
nested peer_input routing. It is a single compute sub-region that:

    - consumes one or more registry areas' configs DIRECTLY
      (no intermediate composition layer between it and the registry)
    - owns its own persistent state (prepared_programs)
    - exposes the standard encode() signature
    - publishes its contribution for downstream sub-regions to read

The two other leaf sub-regions (SMA, primary motor) follow the same shape.
The registry-area-to-config mapping is one-to-one: a leaf sub-region's
config is a direct application of its source areas' configs, with any
sub-region-specific parameters (state parameters, thresholds) in the
sub-region's own config dict.

PREMOTOR'S REGISTRY-AREA SOURCE
-------------------------------
Premotor has ONE frontal-registry area source:

    brodmann_area_6/        the "premotor_cortex" block (the LATERAL
                            area 6; sub_region = None, because
                            premotor_cortex is a leaf system named in
                            SYSTEM directly)

Its config (in `brodmann_area_6.LEFT_CONFIG["premotor_cortex"]`)
provides the premotor feature weights and connectivity priors:
movement_preparation, movement_parameter_selection, motor_imagery,
action_observation, speech_articulatory_planning, reaching_grasping_planning,
plus priors to primary_motor, prefrontal, SMA, parietal, Broca's area,
basal ganglia, cerebellum, and commissures.

Because there is only one area source, there is NO share weight — no
`premotor_weight` field. This is the same pattern as DMPFC (single
source, no share) and VMPFC (single source, no share). Area 6's
"premotor_cortex" block is the entire config source; `LEFT_PREMOTOR_CONFIG`
adds only the state parameters and the sub-region-specific thresholds.

PREMOTOR OWNS PERSISTENT STATE
-------------------------------
Premotor carries state across ticks:

    prepared_programs    a list of candidate movement programs that
                         have been prepared this tick or in previous
                         ticks and not yet consumed. Each program is
                         a dict with selected parameters (direction,
                         force, grasp type, target) and an activation
                         level. Programs decay unless refreshed; the
                         top-activation program(s) are what SMA reads
                         to sequence and primary motor reads to
                         execute.

The state is threaded by FrontalCortex's step(): premotor receives its
state dict from last tick, returns a new one, and FrontalCortex stores
it for the next tick.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

        1. Read peer_input — premotor is called second in
           FrontalCortex's order, so it has access to:
               peer_input["prefrontal_cortex"] — the prefrontal
                   contribution, which includes the current goal
                   (prefrontal's `goals` alias, sourced from DMPFC),
                   the working-memory contents (from DLPFC), and the
                   integrated value (from VMPFC and OFC via their
                   blocks in the prefrontal composite).

        2. Extract premotor features from sensory_input, top_down, and
           peer_input (see FEATURE EXTRACTION below).

        3. Apply area 6's premotor_cortex block config to weight the
           features.

        4. Prepare and update prepared_programs (see PROGRAM
           PREPARATION below):
               a. Evaluate the current tick's candidates: which
                  movements are currently being considered, given
                  the goal and the current sensory context?
               b. For each candidate, select parameters (direction,
                  force, grasp type, target) based on the goal and
                  the sensory affordances.
               c. Compute an activation level per candidate (how
                  strongly it's currently prepared).
               d. Merge with the previous tick's prepared_programs:
                  refresh activation for existing candidates,
                  decay unrehearsed ones, insert new candidates,
                  evict below-threshold ones.
               e. Store the merged prepared_programs as new_state.

        5. Compute premotor's contribution:
               - the prepared_programs (top-activation candidates,
                 published for SMA and primary motor)
               - the feature dict (from step 3)

        6. Return (contribution, new_state).

PROGRAM PREPARATION (the premotor-specific operational pattern)
---------------------------------------------------------------
Premotor's distinctive computation is program preparation — assembling
a candidate movement with selected parameters, in a form that SMA can
sequence and primary motor can execute. Each program has:

    {
        "program_id":     unique identifier (within-hemisphere
                          monotonic; cross-hemisphere collisions fine),
        "target":         the movement's target — an object, a location,
                          a sound to articulate, or an internal state
                          to reach;
        "parameters": {
            "direction":  unit vector or symbolic (for reaching/grasping),
            "force":      scalar (movement effort),
            "velocity":   scalar (movement speed),
            "grasp_type": categorical (for reaching tasks),
            "articulatory_target": phonological representation (for
                          speech tasks),
            "target_frame": "egocentric" or "allocentric" (for spatial
                          tasks; on the left, more allocentric due to
                          parietal coupling),
        },
        "activation":     scalar in [0, 1]; higher = more strongly
                          prepared. Refreshed this tick if the goal
                          and sensory context still support this
                          program; decayed otherwise.
    }

The activation dynamics:
    - A candidate whose target is currently goal-relevant and sensory-
      available gets its activation refreshed upward.
    - A candidate whose target is no longer goal-relevant or not
      sensory-available decays by a documented rate.
    - Activation is clipped to [0, 1].
    - Programs below activation_threshold are evicted.

The capacity of prepared_programs (how many candidate programs can
be held simultaneously) is a config parameter (STRUCTURAL — equal
across hemispheres). When the capacity is exceeded, the lowest-
activation programs are evicted.

Program IDs are monotonically increasing within a hemisphere's lifetime.
Cross-hemisphere ID collisions are fine — the two hemispheres'
prepared_programs are independent, and the commissures handle any
cross-midline coordination by content, not by ID.

FEATURE EXTRACTION (the premotor's inputs)
------------------------------------------
    From sensory_input:
        target_affordances   — what movements are possible given the
                               current environment (reachable objects,
                               graspable items, articulable sounds);
                               the "affordances" in Gibson's sense
        goal_relevant_objects — objects the current goal is about,
                               identified by the sensory system

    From top_down:
        basal_forebrain_gain — attention/arousal; modulates how many
                               candidates are prepared and their decay
                               rate
        cingulate_control    — targeted control from ACC (may bias
                               which candidate is prepared)
        basal_ganglia_gate   — previous tick's gating feedback; a
                               vetoed program gets its activation
                               reduced (the BG said no to it)
        cerebellar_feedback  — timing and error-correction signals
                               from the cerebellum (for parameter
                               selection: velocity, force)

    From peer_input:
        (Premotor reads ONLY peer_input["prefrontal_cortex"] —
        prefrontal is the only sub-region that has run before it.)
        goal                  — the current goal from DMPFC (via
                                prefrontal's `goals` alias); selects
                                which targets are relevant
        working_memory        — DLPFC's held contents; may include
                                a target the system is currently
                                pursuing across ticks
        integrated_value      — VMPFC's value signal; high-value
                                targets get activation boost
        stimulus_value        — OFC's per-stimulus value (via
                                prefrontal's composite)

    Feature extraction is documented in the premotor class
    implementation. On the left, the extraction weights speech-
    articulatory affordances higher than reaching/grasping (PMv vs
    PMd), consistent with the left's anchor feature
    (speech_articulatory_planning).

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

        # Operational output — the prepared programs
        "prepared_programs": [
            {program dict (see PROGRAM PREPARATION)},
            ...
        ],
        "top_program":     the single highest-activation program, or
                           None if no programs are prepared,
    }

The `prepared_programs` list is what SMA reads (to sequence) and
primary motor reads (to execute). The `top_program` is a convenience
alias for the single most-ready candidate — a consumer that wants
"what's the system about to do" reads `top_program` without sorting
`prepared_programs`.

LEFT-SPECIFIC BIAS
------------------
Same class as the right premotor; the LEFT config changes the weights
(via area 6's premotor block config):

    speech_articulatory_planning   higher (0.75) — the left's anchor
                                   feature; PMv ↔ Broca's coupling
    reaching_grasping_planning     lower (0.40)
    to_broca_area_44               higher (0.60) — PMv's coupling to
                                   Broca's area for speech planning
    to_parietal                    lower (0.60) — reaching/grasping
                                   is more right-lateralised
    to_commissures                 lower (0.35)

The state structure (prepared_programs, capacity, decay rate,
activation threshold), the encoding pipeline, the parameter-selection
logic, and the contribution shape are IDENTICAL across hemispheres.
Only the config values inside area 6's premotor block differ. RIGHT
mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right premotor. Cross-midline premotor
exchange is the coordination of prepared movement programs between
hemispheres:

    - Bimanual coordination (the primary case). For a bimanual action
      (tying shoelaces, playing piano, holding a cup with one hand
      and pouring with the other), the right's premotor prepares the
      gross/positional component and the left's prepares the
      fine/distal component. The two hemispheres' prepared programs
      have to be combined into a coherent bimanual action, and that
      combination is the commissures' job. Neither premotor reads the
      other's prepared_programs directly.

    - Speech-articulatory / prosodic coupling. The left's PMv
      prepares articulatory movements (via Broca's area coupling);
      the right's PMv prepares prosodic movements (intonation
      contours, expressive facial movements for speech). The two
      have to be combined for fluent, intoned speech. Direct import
      would silently merge them and make the "flat speech with
      intact content" failure mode untestable.

    - Postural / reaching coordination. The right's premotor often
      prepares the postural adjustment that enables the left's
      fine-motor target. The coordination goes through the
      commissures, not through direct read.

All three are commissural. On the left, the bimanual-coordination
case is the one premotor's lower to_commissures prior (0.35) is
calibrated against — the left's prepared programs need to reach the
right for the gross component, but less so than the right's need to
reach the left (whose to_commissures prior is 0.40). The asymmetry
reflects that the right's gross/positional programs are the ones that
have to reach across for bimanual coherence; the left's fine/distal
programs often execute locally once the right's gross positioning
is in place.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not compose sub-sub-regions. Premotor is a LEAF: its
      config comes from area 6's premotor block directly, with no
      intermediate composition. The `_blend_*` patterns from
      prefrontal's sub-sub-regions do not apply here.
    - Must not add a `premotor_weight` field. Premotor has a single
      registry-area source; there is no share.
    - Must not carry peer_input assumptions beyond prefrontal.
      Premotor runs SECOND; only prefrontal's contribution is
      available. If a future reorder puts another sub-region before
      premotor, that is a config change in
      LEFT_FRONTAL_CORTEX_CONFIG["order"], not a code change here.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not hold module-level mutable state. The
      prepared_programs live in the state dict returned by encode(),
      not in module globals.
    - Must not implement program sequencing. Premotor prepares
      individual programs; SMA sequences them. Adding sequencing
      logic to premotor would blur the two leaf sub-regions'
      roles and would break the causal composition order (SMA comes
      after premotor for a reason).
    - Must not implement program execution. Primary motor executes;
      premotor prepares.
    - Must not read area 6's premotor block config directly — the
      config is passed in via `config` (built by FrontalCortex at
      construction).
    - Must not read area 6's supplementary_motor block. Premotor
      reads only its own block. The SMA block is for the SMA
      sub-region (the second leaf, coming next).
    - Must not import or reference the right premotor. Cross-midline
      exchange goes through `telencephalon/commissures/`.
    - Must not diverge in structure from the right premotor — same
      class, same encode() signature, same state structure
      (prepared_programs with the fields documented above), same
      parameter-selection logic. Only area 6's premotor block config
      differs, and only by the directional mirror.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_PREMOTOR_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_6",
        "source_block": "premotor_cortex",

        # prepared_programs state parameters (STRUCTURAL — equal
        # across hemispheres).
        "prepared_programs_capacity":        5,
        "activation_decay_rate":             0.10,  # per-tick
                                                    # activation
                                                    # decay for
                                                    # unrehearsed
                                                    # programs
        "activation_refresh_rate":           0.20,  # per-tick
                                                    # activation
                                                    # increase for
                                                    # rehearsed
                                                    # programs
        "activation_threshold":              0.20,  # below this,
                                                    # programs are
                                                    # evicted

        # Parameter-selection thresholds (STRUCTURAL).
        "parameter_selection_confidence_threshold": 0.4,
            # a program with parameters whose selection confidence
            # is below this is not added to prepared_programs (it's
            # not yet well-specified enough to prepare)
    }

    Area 6's premotor_cortex block config
    (brodmann_area_6.LEFT_CONFIG["premotor_cortex"]) is supplied by
    FrontalCortex at construction. It provides the feature weights
    and connectivity priors.

    RIGHT_PREMOTOR_CONFIG is IDENTICAL except that it names
    brodmann_area_6.RIGHT_CONFIG["premotor_cortex"]. The state
    parameters and thresholds are STRUCTURAL — equal across
    hemispheres. The lateralisation lives entirely in the source
    block's feature weights and connectivity priors.

    Two separate tests are needed:
        1. RIGHT_PREMOTOR_CONFIG == LEFT_PREMOTOR_CONFIG on state
           parameters and thresholds (structural equality).
        2. brodmann_area_6.RIGHT_CONFIG["premotor_cortex"] is a
           directional mirror of the left's premotor block (feature
           and connectivity values mirror). NOTE: area 6's two blocks
           (premotor and SMA) are each tested independently against
           their counterparts; the mirror test does NOT check
           relations between the two blocks.

EXPORTS
-------
    from .premotor_cortex import PremotorCortex
    from .premotor_cortex import LEFT_PREMOTOR_CONFIG

    The class implements the leaf sub-region encode() signature that
    FrontalCortex expects. No dlpfc_weight-style precondition: the
    source config is present and correct (no pending amendment).

    NOTE: This package's construction does NOT depend on the pending
    area-9 amendment (that affects DLPFC only).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  PremotorCortex class, import area 6's LEFT_CONFIG premotor block,
  build LEFT_PREMOTOR_CONFIG, instantiate the class, expose the class
  and the config. No computation lives here.
- The class implements the leaf sub-region encode() signature. It
  owns prepared_programs state (non-empty persistent dict).
- The class is STATEFUL — it carries prepared_programs across ticks.
  No module-level mutable state; the state lives in the dicts
  returned by encode().
- Program preparation is broken into documented, unit-testable
  functions: `_candidate_programs(...)` (identify candidates from
  goal + affordances), `_select_parameters(...)` (choose direction,
  force, grasp type, target for each candidate),
  `_update_prepared_programs(...)` (refresh/decay/insert/evict), and
  `_select_top_program(...)` (highest activation, for the top_program
  alias). Each is tested in isolation with synthetic state and
  inputs.
- Feature extraction is a documented, unit-testable function.
- The class does not read area 6's SMA block, nor any other sub-
  region's config. Only its own source block.
- The class does not import or access any peer sub-sub-region's
  state. It reads peer_input["prefrontal_cortex"] only (prefrontal
  is the only sub-region that has run before premotor).
- The class does not implement sequencing (that's SMA) or execution
  (that's primary motor). It prepares individual programs.
- LEFT_PREMOTOR_CONFIG is structurally identical to
  RIGHT_PREMOTOR_CONFIG except for the source block reference. State
  parameters and thresholds are STRUCTURAL.
- Program IDs are monotonic within a hemisphere. Cross-hemisphere
  collisions are fine; the commissures coordinate by content, not
  by ID.
- If a future change wants to add a second premotor source (e.g. a
  sub-region of area 6 that only premotor reads), the composition
  becomes N=2 and the overlap-and-specific rule applies. This is
  unlikely for premotor (area 6's premotor block is the natural
  source), but documented for completeness.
- Must not import or reference the right premotor. Cross-midline
  exchange goes through `telencephalon/commissures/`.
"""