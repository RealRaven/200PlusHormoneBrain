"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.supplementary_motor_cortex
=========================================================================================================================

The SUPPLEMENTARY MOTOR AREA (SMA) — left hemisphere. A LEAF compute
sub-region of the frontal cortex, the third stage of the motor hierarchy,
and the last leaf sub-region.

SMA is the movement-SEQUENCING core of the frontal motor hierarchy: given
prepared programs (from premotor, which prepared them toward goals from
prefrontal), SMA orders them into multi-step sequences, coordinates
bimanual actions, and tracks progress through the sequence across ticks.
It is the bridge between premotor's individual prepared movements and
primary motor's per-tick execution — the stage that turns "here are the
pieces" into "here is the order, and here's where we are in it".

SMA is called THIRD in the frontal cortex's composition order (after
prefrontal and premotor, before primary motor). It reads prefrontal's
goals AND premotor's prepared_programs from peer_input, and it publishes
its sequences for primary motor to execute.

THE LAST LEAF — and the most complex one
----------------------------------------
SMA is the third and final leaf sub-region. It shares the leaf pattern
established by premotor and primary motor (single registry-area source,
no internal composition, standard encode() signature, publishes a
contribution), but it has two features that make it the most complex
leaf:

    1. TEMPORAL STATE, not decaying state. Premotor's prepared_programs
       is a buffer whose contents decay if unrehearsed. SMA's
       sequence_state is an ordered sequence with an explicit current
       position and a progression through steps. State is *trajectory*,
       not *activation*.

    2. THE WIDEST PEER_INPUT DEPENDENCIES OF ANY LEAF. Premotor reads
       only prefrontal (one upstream). Primary motor reads all three
       upstreams (prefrontal + premotor + SMA). SMA reads two
       upstreams (prefrontal + premotor) — but its use of them is the
       most structurally integrated: it needs premotor's prepared
       programs as raw material and prefrontal's goals as the
       sequencing target, and it cannot sequence without both.

Both features are why SMA is the last leaf written: it needs the leaf
pattern (established by premotor) and the peer_input contract (established
by premotor for two-upstream reads is the same as one-upstream, just
more inputs) and the sequencing semantics (new, and the deepest single
operation in the frontal motor hierarchy).

SMA OWNS PERSISTENT STATE
--------------------------
SMA carries state across ticks:

    sequence_state    the currently active sequence(s) and their
                      progress. A structured dict with the current
                      sequence (the ordered list of program steps),
                      the current position (which step is being
                      executed this tick), and the per-step
                      preconditions/postconditions that determine
                      when to advance.

The state is threaded by FrontalCortex's step(): SMA receives its state
dict from last tick, returns a new one, and FrontalCortex stores it for
the next tick.

Why temporal state is different from premotor's buffer state: premotor's
prepared_programs are a *set of active candidates* whose individual
activations go up and down. SMA's sequence_state is a *trajectory* — a
single ordered list with a definite position, and the position advances
(or not, or resets) based on preconditions. The two are both persistent,
but they carry different kinds of information and have different
operational dynamics. This is why the two stateful leaf sub-regions are
distinct, rather than one "motor state" dict.

SMA'S REGISTRY-AREA SOURCE
--------------------------
SMA has ONE frontal-registry area source:

    brodmann_area_6/        the "supplementary_motor_cortex" block
                            (the MEDIAL area 6; sub_region = None,
                            because supplementary_motor_cortex is a
                            leaf system named in SYSTEM directly)

Its config (in `brodmann_area_6.LEFT_CONFIG["supplementary_motor_cortex"]`)
provides the SMA feature weights and connectivity priors:
movement_sequencing, internally_generated_movement,
bimanual_coordination, motor_sequence_learning,
language_articulatory_sequence, spatial_movement_sequence, plus priors
to primary_motor, premotor, prefrontal, Broca's area, basal ganglia,
cerebellum, and commissures.

Because there is only one area source, there is NO share weight — no
`sma_weight` field. Same pattern as DMPFC, VMPFC, premotor, primary
motor.

Note that area 6 contributes to BOTH premotor AND SMA (the two blocks
of its config are consumed by the two leaf sub-regions), but each
sub-region reads ONLY its own block. This is the multi-system pattern
established at area 6's registry file: two systems, two blocks, no
cross-reads.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

        1. Read peer_input — SMA is called third, so it has access to:
               peer_input["prefrontal_cortex"]   — goals (from
                   prefrontal's `goals` alias, sourced from DMPFC),
                   value signals, working memory (for knowing what
                   the system is currently trying to accomplish)
               peer_input["premotor_cortex"]     — prepared_programs
                   (the movement candidates being readied; the raw
                   material for sequencing)

        2. Extract SMA features from sensory_input, top_down, and
           peer_input. On the left, extraction weights
           language-articulatory sequence features higher.

        3. Apply area 6's SMA block config to weight the features.

        4. Update sequence_state (see SEQUENCING below):
               a. Read premotor's prepared_programs.
               b. If there is no current sequence, and the goal
                  warrants a multi-step action, build one from the
                  prepared programs (order them, assign
                  preconditions and postconditions).
               c. If there is a current sequence, evaluate its
                  current step's precondition: is it satisfied
                  (ready to execute)? If yes, mark it for execution
                  this tick. Evaluate its postcondition: is it
                  satisfied (step complete)? If yes, advance the
                  position.
               d. Handle bimanual coordination: if the sequence
                  involves both hands (or both sides of the body),
                  coordinate the left and right steps' timing.
               e. Handle sequence reset/abandonment: if the goal is
                  no longer relevant (DMPFC no longer has it active),
                  or the sequence has been stuck at a step too long,
                  reset or abandon.

        5. Compute SMA's contribution:
               - the sequences (current step(s) and any lookahead,
                 published for primary motor to execute)
               - the feature dict (from step 3)

        6. Return (contribution, new_state).

SEQUENCING (the SMA-specific operational pattern)
-------------------------------------------------
SMA's distinctive computation is sequencing — building and advancing an
ordered multi-step plan. Each sequence has:

    sequence_state = {
        "active_sequence": {
            "sequence_id":      unique within-hemisphere monotonic ID,
            "goal_context":     which goal this sequence serves (the
                                goal_id from DMPFC, when available),
            "steps": [
                {
                    "step_id":       unique within-sequence ID,
                    "program_id":    the program_id from premotor's
                                     prepared_programs that this
                                     step executes (for traceability),
                    "precondition":  a predicate describing when
                                     this step can execute (e.g.
                                     "hand has reached target",
                                     "previous step complete",
                                     "articulatory target set"),
                    "postcondition": a predicate describing when
                                     this step is complete (e.g.
                                     "target reached", "sound
                                     produced"),
                    "bimanual_role": "left_only" | "right_only" |
                                     "both" — for bimanual
                                     coordination; on the left
                                     hemisphere's SMA, "left_only"
                                     steps are "our contribution to
                                     the bimanual action" and
                                     "right_only" steps are "the
                                     other hemisphere's contribution
                                     we need to coordinate with"
                },
                ...
            ],
            "current_position":  int, index into steps,
            "progress_ticks":    int, ticks since the current step
                                 started (for timeout detection),
            "status":            "running" | "completed" | "abandoned"
        } or None,
    }

The sequencing dynamics:
    - Build: when sequence_state["active_sequence"] is None and the
      goal requires multi-step action, construct a sequence from
      premotor's prepared_programs (order them by goal-relevance,
      assign preconditions/postconditions).
    - Advance: when the current step's postcondition is satisfied,
      increment current_position. If current_position exceeds
      steps length, mark completed.
    - Hold: when the current step's precondition is not yet
      satisfied (e.g. "hand has reached the pre-grasp position"), no
      execution happens this tick; progress_ticks increments. If
      progress_ticks exceeds a timeout, abandon (the step is stuck).
    - Reset/abandon: when the goal context is no longer active in
      DMPFC (peer_input["prefrontal_cortex"]["goals"] no longer
      contains the sequence's goal_context), mark abandoned.

The sequence's `steps` are the *current step and any lookahead*. SMA
publishes to primary motor the step(s) that are ready to execute this
tick (precondition satisfied), plus optionally the next 1-2 steps as
lookahead (so primary motor can pre-position effectors). It does NOT
publish the entire sequence — primary motor executes step by step.

THE MANY WAYS A SEQUENCE CAN FAIL (and how SMA handles them)
------------------------------------------------------------
Sequencing is where a lot of failure modes concentrate. SMA documents
and handles them explicitly:

    STUCK STEP        the precondition never becomes satisfied. SMA
                      increments progress_ticks; after a timeout,
                      the step is abandoned and the sequence resets
                      (or advances to a fallback step if the sequence
                      was built with one).

    GOAL DRIFT        DMPFC's active goal changes while SMA is
                      sequencing. If the goal context is no longer
                      active, SMA abandons the sequence (the prepared
                      program was toward a goal the system no longer
                      has). This is the correct behaviour — a
                      sequence built for "pick up the cup" should
                      not continue if the goal has changed to
                      "answer the phone".

    PREPARED PROGRAM GONE
                      premotor evicts a prepared program (due to
                      decay) while SMA's sequence references it.
                      SMA detects the missing program_id and
                      either waits (if premotor is likely to
                      re-prepare it) or abandons (if it's not).
                      Which is chosen is a config parameter.

    BIMANUAL DESYNC   in a bimanual sequence, the left and right
                      steps get out of sync (the other hemisphere
                      didn't execute its step when SMA expected).
                      SMA coordinates via the commissures; when the
                      desync is detected, the sequence pauses at the
                      current step until coordination is
                      re-established, or abandons.

    POSTCONDITION NEVER SATISFIED
                      similar to stuck step, but at the far end: the
                      step executed (precondition was met) but the
                      postcondition never becomes true. This is
                      usually a sensory-feedback mismatch or a
                      motor error. SMA treats it as stuck after a
                      timeout.

Each of these is a documented, unit-testable scenario. SMA's operational
complexity is entirely in handling them correctly — the happy path
(sequence built, steps advance, sequence completes) is the simple case.

FEATURE EXTRACTION (the SMA's inputs)
-------------------------------------
    From sensory_input:
        sequence_cues         — sensory content that might indicate a
                                multi-step plan is needed (e.g. a
                                task instruction, a complex object
                                that requires sequenced manipulation)
        current_state         — the state of the effectors and the
                                environment, used to evaluate
                                preconditions and postconditions

    From top_down:
        basal_forebrain_gain  — attention/arousal; may affect step
                                timeout
        cingulate_control     — targeted control from ACC; on high
                                conflict/error, SMA may abandon the
                                current sequence (the ACC's signal is
                                that something is wrong)
        basal_ganglia_gate    — gating feedback on the current step's
                                execution; a vetoed step causes SMA
                                to reset its current position
        cerebellar_feedback   — timing signals; SMA sequences
                                temporal steps against cerebellar
                                timing, especially for articulation
                                (on the left) and gross motor (on
                                the right)

    From peer_input:
        peer_input["prefrontal_cortex"]   — goals (the sequencing
                                            target: what is this
                                            sequence for?),
                                            working_memory (may
                                            hold a multi-step plan),
                                            value (goals with
                                            higher value get higher
                                            sequencing priority)
        peer_input["premotor_cortex"]     — prepared_programs (the
                                            raw material: which
                                            candidate movements
                                            exist, with what
                                            parameters)

CONTRIBUTION SHAPE
------------------
    contribution = {
        # The six SMA features (weighted by area 6's SMA block config)
        "movement_sequencing":         <scalar>,
        "internally_generated_movement": <scalar>,
        "bimanual_coordination":       <scalar>,
        "motor_sequence_learning":     <scalar>,
        "language_articulatory_sequence": <scalar>,
        "spatial_movement_sequence":   <scalar>,

        # Operational output — the current step(s) ready to execute
        "sequences": [
            {
                "sequence_id":    ...,
                "step_id":        ...,
                "program_id":     ...,
                "bimanual_role":  ...,
                # Any lookahead steps are marked "lookahead": True
            },
            ...
        ],
        "sequence_status": {
            "active_sequence_id":  or None,
            "current_position":    ...,
            "progress_ticks":      ...,
            "total_steps":         ...,
        },
    }

`sequences` is the list of steps ready for primary motor to execute this
tick. `sequence_status` is the metadata about the active sequence's
progress — useful for upstream consumers (e.g. DMPFC might want to know
how far along a multi-step goal is; VMPFC might want to value a
mid-sequence state differently from a fresh one).

LEFT-SPECIFIC BIAS
------------------
Same class as the right SMA; the LEFT config changes the weights (via
area 6's SMA block config):

    language_articulatory_sequence  higher (0.75) — the left's
                                    anchor; SMA's speech-sequencing
                                    role
    spatial_movement_sequence       lower (0.45)
    bimanual_coordination           lower (0.40) — bimanual
                                    coordination is more
                                    right-lateralised
    to_broca_area_44                higher (0.50) — SMA ↔ Broca's
                                    for speech sequencing
    to_commissures                  lower than the right's (0.50 on
                                    both sides — structural, but the
                                    *content* of the traffic is
                                    different; see CROSS-MIDLINE)

The state structure (sequence_state with active_sequence and
current_position), the sequencing dynamics, the failure-mode handling,
the feature extraction, and the contribution shape are IDENTICAL across
hemispheres. Only the config values inside area 6's SMA block differ.
RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right SMA. Cross-midline SMA exchange is
bimanual coordination — the case the higher to_commissures prior is
about:

    - Bimanual sequencing (the primary case). For a bimanual multi-
      step action, the left's SMA sequences the left-hand steps and
      the right's sequences the right-hand steps; the two have to be
      interleaved so that the bimanual action is coherent. The
      coordination happens via the commissures: the left proposes
      its step timing, the right proposes its own, and the
      interleaving is negotiated. Neither SMA reads the other's
      sequence_state directly.

      The `to_commissures` prior is 0.50 on both hemispheres — this
      is a *structural* equality, not a directional mirror, because
      bimanual sequencing is inherently two-way (each hemisphere
      needs to coordinate with the other). The *content* of the
      traffic differs (left's speech sequences vs right's spatial
      sequences), but the *bandwidth* of the coordination is
      symmetric. This is a departure from premotor's directional
      asymmetry (right 0.40 vs left 0.35), and the reason is
      instructive: premotor's gross programs have to reach the
      left's fine programs more than the reverse (one-way handoff),
      but SMA's bimanual sequencing needs continuous two-way
      coordination throughout the action. Different dynamics, same
      prior mechanism.

    - Speech sequencing. The left's SMA sequences the language-
      articulatory steps (phoneme ordering, syllable structure); the
      right's sequences prosodic contour steps (intonation contour
      progression). The two are combined at the speech effectors,
      and the coordination is commissural. A left SMA lesion
      produces stuttering-like articulation deficits; a right SMA
      lesion produces flat/atonal sequencing.

    - Sequence learning. When a new multi-step motor skill is being
      learned, both SMAs participate, and their learning is
      coordinated across the commissures. A right SMA lesion
      impairs spatial/bimanual sequence learning more than a left
      lesion; a left SMA lesion impairs language-articulatory
      sequence learning.

All three are commissural. The bimanual-sequencing case is the primary
one for SMA specifically (it's the sub-region whose distinctive
operation is sequencing), and the structural `to_commissures: 0.50`
reflects that the coordination is inherently two-way.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not compose sub-sub-regions. SMA is a LEAF.
    - Must not add an `sma_weight` field. Single area source.
    - Must not implement program preparation (premotor's job) or
      execution (primary motor's job). SMA sequences — it orders,
      progresses, and coordinates; it does not prepare individual
      programs or execute individual steps.
    - Must not reach back into premotor's prepared_programs for
      programs it didn't publish in this tick's peer_input. A
      program premotor evicted is gone; SMA must handle the
      "prepared program gone" case (see the failure-modes section),
      not resurrect the program.
    - Must not read area 6's premotor block config. SMA reads only
      its own block (`supplementary_motor_cortex`). Same multi-
      system rule as premotor.
    - Must not carry peer_input assumptions beyond prefrontal and
      premotor. If a future reorder puts another sub-region before
      SMA, that's a config change in
      LEFT_FRONTAL_CORTEX_CONFIG["order"].
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not hold module-level mutable state. The sequence_state
      lives in the state dict returned by encode().
    - Must not change the to_commissures prior to be directional
      (right > left). It is 0.50 on both sides because bimanual
      coordination is inherently two-way. The *content* of the
      exchange differs (see CROSS-MIDLINE), but the prior is
      structural. A future contributor who assumes "the right's
      prior should be higher" (because premotor's is) would be
      wrong — the two leaves' coordination dynamics differ, and
      SMA's are symmetric.
    - Must not read area 6's SMA block config directly — passed in
      via `config`.
    - Must not import or reference the right SMA. Cross-midline
      exchange goes through `telencephalon/commissures/`. The
      bimanual-sequencing case is the prime example: direct import
      would silently merge the two hemispheres' sequences and make
      the "bimanual desync detection" failure mode untestable.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_SMA_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_6",
        "source_block": "supplementary_motor_cortex",

        # sequence_state parameters (STRUCTURAL — equal across
        # hemispheres).
        "max_sequence_length":            20,   # safety cap; longer
                                                # sequences are
                                                # truncated (with
                                                # a logged warning)
        "step_timeout_ticks":             10,   # if a step's
                                                # precondition isn't
                                                # satisfied within
                                                # this many ticks,
                                                # treat as stuck
        "postcondition_timeout_ticks":    15,   # if a step's
                                                # postcondition isn't
                                                # satisfied after
                                                # execution within
                                                # this many ticks,
                                                # treat as stuck
        "bimanual_desync_tolerance":      2,    # ticks of desync
                                                # before treating as
                                                # failed coordination
        "lookahead_steps":                2,    # how many future
                                                # steps SMA publishes
                                                # alongside the
                                                # current step (for
                                                # primary motor's
                                                # pre-positioning)
        "missing_program_action":         "wait_then_abandon",
                                                # "wait" | "abandon" |
                                                # "wait_then_abandon";
                                                # behaviour when a
                                                # sequence references
                                                # a program premotor
                                                # no longer has
        "missing_program_wait_ticks":     3,    # how long to wait
                                                # before abandoning
                                                # in
                                                # "wait_then_abandon"
                                                # mode
    }

    Area 6's supplementary_motor_cortex block config
    (brodmann_area_6.LEFT_CONFIG["supplementary_motor_cortex"]) is
    supplied by FrontalCortex at construction. It provides the
    feature weights and connectivity priors.

    RIGHT_SMA_CONFIG is IDENTICAL except that it names
    brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"]. The
    sequence_state parameters and failure-mode configs are
    STRUCTURAL — equal across hemispheres.

    Two separate tests are needed:
        1. RIGHT_SMA_CONFIG == LEFT_SMA_CONFIG on state parameters
           and failure-mode configs (structural equality).
        2. brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"]
           is a directional mirror of the left's SMA block. NOTE: the
           premotor block is tested separately; no cross-block
           relations are checked.

EXPORTS
-------
    from .supplementary_motor_cortex import SupplementaryMotorCortex
    from .supplementary_motor_cortex import LEFT_SMA_CONFIG

    The class implements the leaf sub-region encode() signature that
    FrontalCortex expects. No dlpfc_weight-style precondition.

    NOTE: This package's construction does NOT depend on the pending
    area-9 amendment (that affects DLPFC only).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  SupplementaryMotorCortex class, import area 6's LEFT_CONFIG SMA
  block, build LEFT_SMA_CONFIG, instantiate the class, expose the
  class and the config.
- The class implements the leaf sub-region encode() signature. It
  owns sequence_state (non-empty persistent dict).
- The class is STATEFUL — carries sequence_state across ticks. No
  module-level mutable state.
- Sequencing is broken into documented, unit-testable functions:
      `_build_sequence(goal, prepared_programs, config)` -> sequence
          or None; orders prepared programs into a sequence
          (assigns preconditions/postconditions/bimanual_role)
      `_advance_sequence(sequence, sensory_state, config)` ->
          (new_sequence, steps_to_execute)
          evaluates precondition of current step; if met, returns
          the step(s) to execute; evaluates postcondition; if met,
          advances position
      `_handle_failure_modes(sequence, peer_context, config)` ->
          (new_sequence, failure_action)
          handles stuck step, goal drift, prepared-program-gone,
          bimanual desync, postcondition-never-satisfied
  Each tested in isolation with synthetic state and inputs.
- The failure-mode handler is the most important unit-testable piece.
  Each of the five documented failure modes should have at least one
  test case.
- Feature extraction is a documented, unit-testable function. On
  the left, extraction weights language-articulatory sequence
  features higher.
- The class does not read area 6's premotor block config.
- The class does not import or access any peer sub-sub-region's
  state.
- The class does not implement preparation or execution.
- LEFT_SMA_CONFIG is structurally identical to RIGHT_SMA_CONFIG
  except for the source block reference. State parameters and
  failure-mode configs are STRUCTURAL.
- `sequences` output includes the current step(s) ready to execute
  this tick, plus up to `lookahead_steps` future steps marked
  "lookahead": True. Primary motor executes only the non-lookahead
  steps; lookahead is for pre-positioning.
- Sequence IDs and step IDs are monotonic within a hemisphere.
  Cross-hemisphere collisions are fine; bimanual coordination
  matches by program_id (which is also monotonic within a
  hemisphere) and by goal_context.
- Must not import or reference the right SMA. Cross-midline
  exchange goes through `telencephalon/commissures/`.
- Must not make the to_commissures prior directional. It is 0.50 on
  both sides because bimanual sequencing is two-way. If a future
  change wants it directional, that change would need to document
  a reason (e.g. a specific asymmetric sequencing task), not just
  "mirror the premotor pattern".

FRONTAL COMPUTE LAYER STATUS (both hemispheres)
-----------------------------------------------
With this file, ALL THREE leaf sub-regions are complete on the LEFT
hemisphere:

    frontal/cortex/__init__.py                          L ✅  R ✅
    prefrontal_cortex/__init__.py                       L ✅  R ✅
    prefrontal_cortex/dorsomedial_prefrontal_cortex/    L ✅  R ✅
    prefrontal_cortex/dorsolateral_prefrontal_cortex/   L ✅  R ⬜ (amendment)
    prefrontal_cortex/orbitofrontal_cortex/             L ✅  R ✅
    prefrontal_cortex/ventromedial_prefrontal_cortex/   L ✅  R ✅
    prefrontal_cortex/ventrolateral_prefrontal_cortex/  L ✅  R ✅
    premotor_cortex/                                    L ✅  R ✅
    supplementary_motor_cortex/                         L ✅  R ⬜
    primary_motor_cortex/                               L ✅  R ✅
    primary_motor_cortex/precentral_gyrus/              L ✅  R ✅

The LEFT frontal compute layer is now COMPLETE (modulo the frontal
gyri/sulci annotations, which are not compute sub-regions). Remaining
on the right: SMA-right, DLPFC-right (blocked by amendment), and the
annotation mirrors.
""""""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.supplementary_motor_cortex
=========================================================================================================================

The SUPPLEMENTARY MOTOR AREA (SMA) — left hemisphere. A LEAF compute
sub-region of the frontal cortex, the third stage of the motor hierarchy,
and the last leaf sub-region.

SMA is the movement-SEQUENCING core of the frontal motor hierarchy: given
prepared programs (from premotor, which prepared them toward goals from
prefrontal), SMA orders them into multi-step sequences, coordinates
bimanual actions, and tracks progress through the sequence across ticks.
It is the bridge between premotor's individual prepared movements and
primary motor's per-tick execution — the stage that turns "here are the
pieces" into "here is the order, and here's where we are in it".

SMA is called THIRD in the frontal cortex's composition order (after
prefrontal and premotor, before primary motor). It reads prefrontal's
goals AND premotor's prepared_programs from peer_input, and it publishes
its sequences for primary motor to execute.

THE LAST LEAF — and the most complex one
----------------------------------------
SMA is the third and final leaf sub-region. It shares the leaf pattern
established by premotor and primary motor (single registry-area source,
no internal composition, standard encode() signature, publishes a
contribution), but it has two features that make it the most complex
leaf:

    1. TEMPORAL STATE, not decaying state. Premotor's prepared_programs
       is a buffer whose contents decay if unrehearsed. SMA's
       sequence_state is an ordered sequence with an explicit current
       position and a progression through steps. State is *trajectory*,
       not *activation*.

    2. THE WIDEST PEER_INPUT DEPENDENCIES OF ANY LEAF. Premotor reads
       only prefrontal (one upstream). Primary motor reads all three
       upstreams (prefrontal + premotor + SMA). SMA reads two
       upstreams (prefrontal + premotor) — but its use of them is the
       most structurally integrated: it needs premotor's prepared
       programs as raw material and prefrontal's goals as the
       sequencing target, and it cannot sequence without both.

Both features are why SMA is the last leaf written: it needs the leaf
pattern (established by premotor) and the peer_input contract (established
by premotor for two-upstream reads is the same as one-upstream, just
more inputs) and the sequencing semantics (new, and the deepest single
operation in the frontal motor hierarchy).

SMA OWNS PERSISTENT STATE
--------------------------
SMA carries state across ticks:

    sequence_state    the currently active sequence(s) and their
                      progress. A structured dict with the current
                      sequence (the ordered list of program steps),
                      the current position (which step is being
                      executed this tick), and the per-step
                      preconditions/postconditions that determine
                      when to advance.

The state is threaded by FrontalCortex's step(): SMA receives its state
dict from last tick, returns a new one, and FrontalCortex stores it for
the next tick.

Why temporal state is different from premotor's buffer state: premotor's
prepared_programs are a *set of active candidates* whose individual
activations go up and down. SMA's sequence_state is a *trajectory* — a
single ordered list with a definite position, and the position advances
(or not, or resets) based on preconditions. The two are both persistent,
but they carry different kinds of information and have different
operational dynamics. This is why the two stateful leaf sub-regions are
distinct, rather than one "motor state" dict.

SMA'S REGISTRY-AREA SOURCE
--------------------------
SMA has ONE frontal-registry area source:

    brodmann_area_6/        the "supplementary_motor_cortex" block
                            (the MEDIAL area 6; sub_region = None,
                            because supplementary_motor_cortex is a
                            leaf system named in SYSTEM directly)

Its config (in `brodmann_area_6.LEFT_CONFIG["supplementary_motor_cortex"]`)
provides the SMA feature weights and connectivity priors:
movement_sequencing, internally_generated_movement,
bimanual_coordination, motor_sequence_learning,
language_articulatory_sequence, spatial_movement_sequence, plus priors
to primary_motor, premotor, prefrontal, Broca's area, basal ganglia,
cerebellum, and commissures.

Because there is only one area source, there is NO share weight — no
`sma_weight` field. Same pattern as DMPFC, VMPFC, premotor, primary
motor.

Note that area 6 contributes to BOTH premotor AND SMA (the two blocks
of its config are consumed by the two leaf sub-regions), but each
sub-region reads ONLY its own block. This is the multi-system pattern
established at area 6's registry file: two systems, two blocks, no
cross-reads.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

        1. Read peer_input — SMA is called third, so it has access to:
               peer_input["prefrontal_cortex"]   — goals (from
                   prefrontal's `goals` alias, sourced from DMPFC),
                   value signals, working memory (for knowing what
                   the system is currently trying to accomplish)
               peer_input["premotor_cortex"]     — prepared_programs
                   (the movement candidates being readied; the raw
                   material for sequencing)

        2. Extract SMA features from sensory_input, top_down, and
           peer_input. On the left, extraction weights
           language-articulatory sequence features higher.

        3. Apply area 6's SMA block config to weight the features.

        4. Update sequence_state (see SEQUENCING below):
               a. Read premotor's prepared_programs.
               b. If there is no current sequence, and the goal
                  warrants a multi-step action, build one from the
                  prepared programs (order them, assign
                  preconditions and postconditions).
               c. If there is a current sequence, evaluate its
                  current step's precondition: is it satisfied
                  (ready to execute)? If yes, mark it for execution
                  this tick. Evaluate its postcondition: is it
                  satisfied (step complete)? If yes, advance the
                  position.
               d. Handle bimanual coordination: if the sequence
                  involves both hands (or both sides of the body),
                  coordinate the left and right steps' timing.
               e. Handle sequence reset/abandonment: if the goal is
                  no longer relevant (DMPFC no longer has it active),
                  or the sequence has been stuck at a step too long,
                  reset or abandon.

        5. Compute SMA's contribution:
               - the sequences (current step(s) and any lookahead,
                 published for primary motor to execute)
               - the feature dict (from step 3)

        6. Return (contribution, new_state).

SEQUENCING (the SMA-specific operational pattern)
-------------------------------------------------
SMA's distinctive computation is sequencing — building and advancing an
ordered multi-step plan. Each sequence has:

    sequence_state = {
        "active_sequence": {
            "sequence_id":      unique within-hemisphere monotonic ID,
            "goal_context":     which goal this sequence serves (the
                                goal_id from DMPFC, when available),
            "steps": [
                {
                    "step_id":       unique within-sequence ID,
                    "program_id":    the program_id from premotor's
                                     prepared_programs that this
                                     step executes (for traceability),
                    "precondition":  a predicate describing when
                                     this step can execute (e.g.
                                     "hand has reached target",
                                     "previous step complete",
                                     "articulatory target set"),
                    "postcondition": a predicate describing when
                                     this step is complete (e.g.
                                     "target reached", "sound
                                     produced"),
                    "bimanual_role": "left_only" | "right_only" |
                                     "both" — for bimanual
                                     coordination; on the left
                                     hemisphere's SMA, "left_only"
                                     steps are "our contribution to
                                     the bimanual action" and
                                     "right_only" steps are "the
                                     other hemisphere's contribution
                                     we need to coordinate with"
                },
                ...
            ],
            "current_position":  int, index into steps,
            "progress_ticks":    int, ticks since the current step
                                 started (for timeout detection),
            "status":            "running" | "completed" | "abandoned"
        } or None,
    }

The sequencing dynamics:
    - Build: when sequence_state["active_sequence"] is None and the
      goal requires multi-step action, construct a sequence from
      premotor's prepared_programs (order them by goal-relevance,
      assign preconditions/postconditions).
    - Advance: when the current step's postcondition is satisfied,
      increment current_position. If current_position exceeds
      steps length, mark completed.
    - Hold: when the current step's precondition is not yet
      satisfied (e.g. "hand has reached the pre-grasp position"), no
      execution happens this tick; progress_ticks increments. If
      progress_ticks exceeds a timeout, abandon (the step is stuck).
    - Reset/abandon: when the goal context is no longer active in
      DMPFC (peer_input["prefrontal_cortex"]["goals"] no longer
      contains the sequence's goal_context), mark abandoned.

The sequence's `steps` are the *current step and any lookahead*. SMA
publishes to primary motor the step(s) that are ready to execute this
tick (precondition satisfied), plus optionally the next 1-2 steps as
lookahead (so primary motor can pre-position effectors). It does NOT
publish the entire sequence — primary motor executes step by step.

THE MANY WAYS A SEQUENCE CAN FAIL (and how SMA handles them)
------------------------------------------------------------
Sequencing is where a lot of failure modes concentrate. SMA documents
and handles them explicitly:

    STUCK STEP        the precondition never becomes satisfied. SMA
                      increments progress_ticks; after a timeout,
                      the step is abandoned and the sequence resets
                      (or advances to a fallback step if the sequence
                      was built with one).

    GOAL DRIFT        DMPFC's active goal changes while SMA is
                      sequencing. If the goal context is no longer
                      active, SMA abandons the sequence (the prepared
                      program was toward a goal the system no longer
                      has). This is the correct behaviour — a
                      sequence built for "pick up the cup" should
                      not continue if the goal has changed to
                      "answer the phone".

    PREPARED PROGRAM GONE
                      premotor evicts a prepared program (due to
                      decay) while SMA's sequence references it.
                      SMA detects the missing program_id and
                      either waits (if premotor is likely to
                      re-prepare it) or abandons (if it's not).
                      Which is chosen is a config parameter.

    BIMANUAL DESYNC   in a bimanual sequence, the left and right
                      steps get out of sync (the other hemisphere
                      didn't execute its step when SMA expected).
                      SMA coordinates via the commissures; when the
                      desync is detected, the sequence pauses at the
                      current step until coordination is
                      re-established, or abandons.

    POSTCONDITION NEVER SATISFIED
                      similar to stuck step, but at the far end: the
                      step executed (precondition was met) but the
                      postcondition never becomes true. This is
                      usually a sensory-feedback mismatch or a
                      motor error. SMA treats it as stuck after a
                      timeout.

Each of these is a documented, unit-testable scenario. SMA's operational
complexity is entirely in handling them correctly — the happy path
(sequence built, steps advance, sequence completes) is the simple case.

FEATURE EXTRACTION (the SMA's inputs)
-------------------------------------
    From sensory_input:
        sequence_cues         — sensory content that might indicate a
                                multi-step plan is needed (e.g. a
                                task instruction, a complex object
                                that requires sequenced manipulation)
        current_state         — the state of the effectors and the
                                environment, used to evaluate
                                preconditions and postconditions

    From top_down:
        basal_forebrain_gain  — attention/arousal; may affect step
                                timeout
        cingulate_control     — targeted control from ACC; on high
                                conflict/error, SMA may abandon the
                                current sequence (the ACC's signal is
                                that something is wrong)
        basal_ganglia_gate    — gating feedback on the current step's
                                execution; a vetoed step causes SMA
                                to reset its current position
        cerebellar_feedback   — timing signals; SMA sequences
                                temporal steps against cerebellar
                                timing, especially for articulation
                                (on the left) and gross motor (on
                                the right)

    From peer_input:
        peer_input["prefrontal_cortex"]   — goals (the sequencing
                                            target: what is this
                                            sequence for?),
                                            working_memory (may
                                            hold a multi-step plan),
                                            value (goals with
                                            higher value get higher
                                            sequencing priority)
        peer_input["premotor_cortex"]     — prepared_programs (the
                                            raw material: which
                                            candidate movements
                                            exist, with what
                                            parameters)

CONTRIBUTION SHAPE
------------------
    contribution = {
        # The six SMA features (weighted by area 6's SMA block config)
        "movement_sequencing":         <scalar>,
        "internally_generated_movement": <scalar>,
        "bimanual_coordination":       <scalar>,
        "motor_sequence_learning":     <scalar>,
        "language_articulatory_sequence": <scalar>,
        "spatial_movement_sequence":   <scalar>,

        # Operational output — the current step(s) ready to execute
        "sequences": [
            {
                "sequence_id":    ...,
                "step_id":        ...,
                "program_id":     ...,
                "bimanual_role":  ...,
                # Any lookahead steps are marked "lookahead": True
            },
            ...
        ],
        "sequence_status": {
            "active_sequence_id":  or None,
            "current_position":    ...,
            "progress_ticks":      ...,
            "total_steps":         ...,
        },
    }

`sequences` is the list of steps ready for primary motor to execute this
tick. `sequence_status` is the metadata about the active sequence's
progress — useful for upstream consumers (e.g. DMPFC might want to know
how far along a multi-step goal is; VMPFC might want to value a
mid-sequence state differently from a fresh one).

LEFT-SPECIFIC BIAS
------------------
Same class as the right SMA; the LEFT config changes the weights (via
area 6's SMA block config):

    language_articulatory_sequence  higher (0.75) — the left's
                                    anchor; SMA's speech-sequencing
                                    role
    spatial_movement_sequence       lower (0.45)
    bimanual_coordination           lower (0.40) — bimanual
                                    coordination is more
                                    right-lateralised
    to_broca_area_44                higher (0.50) — SMA ↔ Broca's
                                    for speech sequencing
    to_commissures                  lower than the right's (0.50 on
                                    both sides — structural, but the
                                    *content* of the traffic is
                                    different; see CROSS-MIDLINE)

The state structure (sequence_state with active_sequence and
current_position), the sequencing dynamics, the failure-mode handling,
the feature extraction, and the contribution shape are IDENTICAL across
hemispheres. Only the config values inside area 6's SMA block differ.
RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right SMA. Cross-midline SMA exchange is
bimanual coordination — the case the higher to_commissures prior is
about:

    - Bimanual sequencing (the primary case). For a bimanual multi-
      step action, the left's SMA sequences the left-hand steps and
      the right's sequences the right-hand steps; the two have to be
      interleaved so that the bimanual action is coherent. The
      coordination happens via the commissures: the left proposes
      its step timing, the right proposes its own, and the
      interleaving is negotiated. Neither SMA reads the other's
      sequence_state directly.

      The `to_commissures` prior is 0.50 on both hemispheres — this
      is a *structural* equality, not a directional mirror, because
      bimanual sequencing is inherently two-way (each hemisphere
      needs to coordinate with the other). The *content* of the
      traffic differs (left's speech sequences vs right's spatial
      sequences), but the *bandwidth* of the coordination is
      symmetric. This is a departure from premotor's directional
      asymmetry (right 0.40 vs left 0.35), and the reason is
      instructive: premotor's gross programs have to reach the
      left's fine programs more than the reverse (one-way handoff),
      but SMA's bimanual sequencing needs continuous two-way
      coordination throughout the action. Different dynamics, same
      prior mechanism.

    - Speech sequencing. The left's SMA sequences the language-
      articulatory steps (phoneme ordering, syllable structure); the
      right's sequences prosodic contour steps (intonation contour
      progression). The two are combined at the speech effectors,
      and the coordination is commissural. A left SMA lesion
      produces stuttering-like articulation deficits; a right SMA
      lesion produces flat/atonal sequencing.

    - Sequence learning. When a new multi-step motor skill is being
      learned, both SMAs participate, and their learning is
      coordinated across the commissures. A right SMA lesion
      impairs spatial/bimanual sequence learning more than a left
      lesion; a left SMA lesion impairs language-articulatory
      sequence learning.

All three are commissural. The bimanual-sequencing case is the primary
one for SMA specifically (it's the sub-region whose distinctive
operation is sequencing), and the structural `to_commissures: 0.50`
reflects that the coordination is inherently two-way.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not compose sub-sub-regions. SMA is a LEAF.
    - Must not add an `sma_weight` field. Single area source.
    - Must not implement program preparation (premotor's job) or
      execution (primary motor's job). SMA sequences — it orders,
      progresses, and coordinates; it does not prepare individual
      programs or execute individual steps.
    - Must not reach back into premotor's prepared_programs for
      programs it didn't publish in this tick's peer_input. A
      program premotor evicted is gone; SMA must handle the
      "prepared program gone" case (see the failure-modes section),
      not resurrect the program.
    - Must not read area 6's premotor block config. SMA reads only
      its own block (`supplementary_motor_cortex`). Same multi-
      system rule as premotor.
    - Must not carry peer_input assumptions beyond prefrontal and
      premotor. If a future reorder puts another sub-region before
      SMA, that's a config change in
      LEFT_FRONTAL_CORTEX_CONFIG["order"].
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not hold module-level mutable state. The sequence_state
      lives in the state dict returned by encode().
    - Must not change the to_commissures prior to be directional
      (right > left). It is 0.50 on both sides because bimanual
      coordination is inherently two-way. The *content* of the
      exchange differs (see CROSS-MIDLINE), but the prior is
      structural. A future contributor who assumes "the right's
      prior should be higher" (because premotor's is) would be
      wrong — the two leaves' coordination dynamics differ, and
      SMA's are symmetric.
    - Must not read area 6's SMA block config directly — passed in
      via `config`.
    - Must not import or reference the right SMA. Cross-midline
      exchange goes through `telencephalon/commissures/`. The
      bimanual-sequencing case is the prime example: direct import
      would silently merge the two hemispheres' sequences and make
      the "bimanual desync detection" failure mode untestable.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_SMA_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_6",
        "source_block": "supplementary_motor_cortex",

        # sequence_state parameters (STRUCTURAL — equal across
        # hemispheres).
        "max_sequence_length":            20,   # safety cap; longer
                                                # sequences are
                                                # truncated (with
                                                # a logged warning)
        "step_timeout_ticks":             10,   # if a step's
                                                # precondition isn't
                                                # satisfied within
                                                # this many ticks,
                                                # treat as stuck
        "postcondition_timeout_ticks":    15,   # if a step's
                                                # postcondition isn't
                                                # satisfied after
                                                # execution within
                                                # this many ticks,
                                                # treat as stuck
        "bimanual_desync_tolerance":      2,    # ticks of desync
                                                # before treating as
                                                # failed coordination
        "lookahead_steps":                2,    # how many future
                                                # steps SMA publishes
                                                # alongside the
                                                # current step (for
                                                # primary motor's
                                                # pre-positioning)
        "missing_program_action":         "wait_then_abandon",
                                                # "wait" | "abandon" |
                                                # "wait_then_abandon";
                                                # behaviour when a
                                                # sequence references
                                                # a program premotor
                                                # no longer has
        "missing_program_wait_ticks":     3,    # how long to wait
                                                # before abandoning
                                                # in
                                                # "wait_then_abandon"
                                                # mode
    }

    Area 6's supplementary_motor_cortex block config
    (brodmann_area_6.LEFT_CONFIG["supplementary_motor_cortex"]) is
    supplied by FrontalCortex at construction. It provides the
    feature weights and connectivity priors.

    RIGHT_SMA_CONFIG is IDENTICAL except that it names
    brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"]. The
    sequence_state parameters and failure-mode configs are
    STRUCTURAL — equal across hemispheres.

    Two separate tests are needed:
        1. RIGHT_SMA_CONFIG == LEFT_SMA_CONFIG on state parameters
           and failure-mode configs (structural equality).
        2. brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"]
           is a directional mirror of the left's SMA block. NOTE: the
           premotor block is tested separately; no cross-block
           relations are checked.

EXPORTS
-------
    from .supplementary_motor_cortex import SupplementaryMotorCortex
    from .supplementary_motor_cortex import LEFT_SMA_CONFIG

    The class implements the leaf sub-region encode() signature that
    FrontalCortex expects. No dlpfc_weight-style precondition.

    NOTE: This package's construction does NOT depend on the pending
    area-9 amendment (that affects DLPFC only).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  SupplementaryMotorCortex class, import area 6's LEFT_CONFIG SMA
  block, build LEFT_SMA_CONFIG, instantiate the class, expose the
  class and the config.
- The class implements the leaf sub-region encode() signature. It
  owns sequence_state (non-empty persistent dict).
- The class is STATEFUL — carries sequence_state across ticks. No
  module-level mutable state.
- Sequencing is broken into documented, unit-testable functions:
      `_build_sequence(goal, prepared_programs, config)` -> sequence
          or None; orders prepared programs into a sequence
          (assigns preconditions/postconditions/bimanual_role)
      `_advance_sequence(sequence, sensory_state, config)` ->
          (new_sequence, steps_to_execute)
          evaluates precondition of current step; if met, returns
          the step(s) to execute; evaluates postcondition; if met,
          advances position
      `_handle_failure_modes(sequence, peer_context, config)` ->
          (new_sequence, failure_action)
          handles stuck step, goal drift, prepared-program-gone,
          bimanual desync, postcondition-never-satisfied
  Each tested in isolation with synthetic state and inputs.
- The failure-mode handler is the most important unit-testable piece.
  Each of the five documented failure modes should have at least one
  test case.
- Feature extraction is a documented, unit-testable function. On
  the left, extraction weights language-articulatory sequence
  features higher.
- The class does not read area 6's premotor block config.
- The class does not import or access any peer sub-sub-region's
  state.
- The class does not implement preparation or execution.
- LEFT_SMA_CONFIG is structurally identical to RIGHT_SMA_CONFIG
  except for the source block reference. State parameters and
  failure-mode configs are STRUCTURAL.
- `sequences` output includes the current step(s) ready to execute
  this tick, plus up to `lookahead_steps` future steps marked
  "lookahead": True. Primary motor executes only the non-lookahead
  steps; lookahead is for pre-positioning.
- Sequence IDs and step IDs are monotonic within a hemisphere.
  Cross-hemisphere collisions are fine; bimanual coordination
  matches by program_id (which is also monotonic within a
  hemisphere) and by goal_context.
- Must not import or reference the right SMA. Cross-midline
  exchange goes through `telencephalon/commissures/`.
- Must not make the to_commissures prior directional. It is 0.50 on
  both sides because bimanual sequencing is two-way. If a future
  change wants it directional, that change would need to document
  a reason (e.g. a specific asymmetric sequencing task), not just
  "mirror the premotor pattern".

FRONTAL COMPUTE LAYER STATUS (both hemispheres)
-----------------------------------------------
With this file, ALL THREE leaf sub-regions are complete on the LEFT
hemisphere:

    frontal/cortex/__init__.py                          L ✅  R ✅
    prefrontal_cortex/__init__.py                       L ✅  R ✅
    prefrontal_cortex/dorsomedial_prefrontal_cortex/    L ✅  R ✅
    prefrontal_cortex/dorsolateral_prefrontal_cortex/   L ✅  R ⬜ (amendment)
    prefrontal_cortex/orbitofrontal_cortex/             L ✅  R ✅
    prefrontal_cortex/ventromedial_prefrontal_cortex/   L ✅  R ✅
    prefrontal_cortex/ventrolateral_prefrontal_cortex/  L ✅  R ✅
    premotor_cortex/                                    L ✅  R ✅
    supplementary_motor_cortex/                         L ✅  R ⬜
    primary_motor_cortex/                               L ✅  R ✅
    primary_motor_cortex/precentral_gyrus/              L ✅  R ✅

The LEFT frontal compute layer is now COMPLETE (modulo the frontal
gyri/sulci annotations, which are not compute sub-regions). Remaining
on the right: SMA-right, DLPFC-right (blocked by amendment), and the
annotation mirrors.
"""