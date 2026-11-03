"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.supplementary_motor_cortex
==========================================================================================================================

The SUPPLEMENTARY MOTOR AREA (SMA) — right hemisphere. A LEAF compute
sub-region of the frontal cortex, the third stage of the motor hierarchy,
and the last leaf sub-region.

Mirror of the left SMA package. SMA is the movement-SEQUENCING core of
the frontal motor hierarchy: given prepared programs (from premotor,
which prepared them toward goals from prefrontal), SMA orders them into
multi-step sequences, coordinates bimanual actions, and tracks progress
through the sequence across ticks. On the RIGHT, the sequences ordered
are predominantly spatial and bimanual — multi-step reaching sequences,
object-manipulation sequences, spatial-navigation sequences, and the
bimanual coordination that drives two-handed tasks. The
language-articulatory sequence role is present but secondary (the left's
anchor). The sequencing mechanics are the same as on the left; the
content and its lateralised weighting are mirrored.

SMA is called THIRD in the frontal cortex's composition order (after
prefrontal and premotor, before primary motor). It reads prefrontal's
goals AND premotor's prepared_programs from peer_input, and it publishes
its sequences for primary motor to execute.

THE LAST LEAF — and the most complex one
----------------------------------------
Identical to the left. SMA has two features that make it the most
complex leaf:

    1. TEMPORAL STATE, not decaying state. sequence_state is an
       ordered sequence with an explicit current position and a
       progression through steps — a trajectory, not a buffer.

    2. THE WIDEST PEER_INPUT DEPENDENCIES OF ANY LEAF (after primary
       motor). Premotor reads only prefrontal (one upstream). SMA
       reads two upstreams (prefrontal + premotor) whose roles are
       structurally interlocked: premotor's prepared programs are
       the raw material, prefrontal's goals are the sequencing
       target, and SMA cannot sequence without both.

On the right, the sequences are predominantly spatial/bimanual; the
structure (sequence_state, sequencing dynamics, failure-mode handling)
is identical to the left's.

SMA OWNS PERSISTENT STATE
--------------------------
SMA carries state across ticks:

    sequence_state    the currently active sequence(s) and their
                      progress. On the right, the sequences are more
                      often multi-step spatial/bimanual actions; the
                      state structure (active_sequence with ordered
                      steps, current_position, progress_ticks,
                      status) is identical to the left's.

The state is threaded by FrontalCortex's step(): SMA receives its
state dict from last tick, returns a new one, FrontalCortex stores it.

Why temporal state differs from premotor's buffer state: same as the
left's explanation — prepared_programs is a set of active candidates
whose activations go up and down; sequence_state is a single ordered
list with a definite position. Different kinds of persistent state,
which is why the two stateful leaves are distinct sub-regions.

SMA'S REGISTRY-AREA SOURCE
--------------------------
SMA has ONE frontal-registry area source:

    brodmann_area_6/        the "supplementary_motor_cortex" block
                            (the MEDIAL area 6; sub_region = None,
                            because supplementary_motor_cortex is a
                            leaf system named in SYSTEM directly)

Its config (in
`brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"]`)
provides the SMA feature weights and connectivity priors. On the right,
the weights lean toward bimanual_coordination (0.75),
spatial_movement_sequence (0.75), and movement_sequencing (0.75);
language_articulatory_sequence is reduced (0.35). The connectivity
priors reflect the right's higher to_commissures (0.65 vs the left's
0.50) and lower to_broca_area_44 (0.25 vs 0.50).

Because there is only one area source, there is NO share weight.

Note that area 6 contributes to BOTH premotor AND SMA (the two blocks
of its config are consumed by the two leaf sub-regions), but each
sub-region reads ONLY its own block. Same multi-system rule as on the
left.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

Identical to the left. Steps:

        1. Read peer_input — SMA is called third, so it has access to
           peer_input["prefrontal_cortex"] (goals, WM, value) and
           peer_input["premotor_cortex"] (prepared_programs).

        2. Extract SMA features. On the right, extraction weights
           spatial/bimanual sequence features higher than
           language-articulatory ones.

        3. Apply area 6's SMA block config to weight the features.

        4. Update sequence_state: build (if no active sequence and
           the goal warrants multi-step action), advance (when
           current step's postcondition is satisfied), hold (when
           precondition isn't yet satisfied), reset/abandon (on
           goal drift, stuck step, or missing program).

        5. Compute SMA's contribution (sequences + feature dict).

        6. Return (contribution, new_state).

On the right, the sequences SMA builds are more often bimanual: the
goal is "tie the shoelace", and the sequence interleaves left-hand
and right-hand steps. The interleaving is coordinated with the left
SMA via the commissures (see CROSS-MIDLINE).

SEQUENCING (the SMA-specific operational pattern)
-------------------------------------------------
Same sequence structure and dynamics as the left:

    sequence_state = {
        "active_sequence": {
            "sequence_id":      unique within-hemisphere monotonic ID,
            "goal_context":     which goal this sequence serves,
            "steps": [
                {
                    "step_id":       unique within-sequence ID,
                    "program_id":    from premotor's
                                     prepared_programs,
                    "precondition":  predicate for when this step
                                     can execute,
                    "postcondition": predicate for when this step
                                     is complete,
                    "bimanual_role": "left_only" | "right_only" |
                                     "both" — on the RIGHT hemisphere's
                                     SMA, "right_only" steps are "our
                                     contribution to the bimanual
                                     action" and "left_only" steps
                                     are "the other hemisphere's
                                     contribution we need to
                                     coordinate with",
                },
                ...
            ],
            "current_position":  int,
            "progress_ticks":    int,
            "status":            "running" | "completed" | "abandoned"
        } or None,
    }

The `bimanual_role` field's semantics are MIRRORED on the right: on
the left's SMA, "left_only" was "our contribution"; on the right's,
"right_only" is "our contribution". This is a small but important
asymmetry in the field's interpretation — the *field name* is the
same ("left_only" always means left-hand-only), but the *hemisphere's
relationship to it* is mirrored. This matters for the bimanual
coordination logic: each SMA is primarily responsible for its own
side's steps and coordinates with the other's, and which steps are
"ours" flips by hemisphere.

The sequencing dynamics (build, advance, hold, reset/abandon) are
identical. The failure modes (see the failure-modes section on the
left) are identical: stuck step, goal drift, prepared-program-gone,
bimanual desync, postcondition-never-satisfied.

THE FIVE FAILURE MODES (restated for the right)
-----------------------------------------------
Same five failure modes as on the left, all documented and handled:

    STUCK STEP, GOAL DRIFT, PREPARED PROGRAM GONE, BIMANUAL DESYNC,
    POSTCONDITION NEVER SATISFIED

On the right, the BIMANUAL DESYNC mode is *more frequently exercised*
because the right's SMA is more often the sequencing driver for
bimanual actions (via its higher bimanual_coordination weight). The
right's SMA is the hemisphere that proposes the interleaving more
often; the left's is the one that follows (or catches up) more often.
This asymmetry is expressed via the to_commissures priors (0.65 on
the right's SMA block vs 0.50 on the left's SMA block — see the note
in CROSS-MIDLINE, which explains why this one place has an
asymmetric prior while the composition-level to_commissures is
symmetric).

FEATURE EXTRACTION (the SMA's inputs)
-------------------------------------
    From sensory_input:
        sequence_cues         — on the right, weighted higher for
                                spatially-complex objects and
                                multi-step bimanual tasks
        current_state         — effector and environment state,
                                used for precondition/postcondition
                                evaluation

    From top_down:
        (same four modulators as left: basal_forebrain_gain,
        cingulate_control, basal_ganglia_gate, cerebellar_feedback)
        cerebellar_feedback   — on the right, more relevant for
                                spatial sequence timing (reaching,
                                multi-step manipulation); on the
                                left, for articulatory sequence
                                timing

    From peer_input:
        (same two upstreams as left: prefrontal, premotor)

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

        # Operational output
        "sequences": [
            {
                "sequence_id":    ...,
                "step_id":        ...,
                "program_id":     ...,
                "bimanual_role":  ...,
                # lookahead steps are marked "lookahead": True
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

The schema is identical. The right's contents are predominantly
spatial/bimanual (spatial_movement_sequence feature high; sequences
target spatial/bimanual steps).

RIGHT-SPECIFIC BIAS
------------------
Same class as the left SMA; the RIGHT config changes the weights
(via area 6's SMA block config):

    bimanual_coordination          higher (0.75) — the right's
                                   anchor; SMA's bimanual driver
                                   role
    spatial_movement_sequence      higher (0.75)
    language_articulatory_sequence lower (0.35)
    to_broca_area_44               lower (0.25)
    to_commissures                 higher (0.65) — the right's SMA
                                   block's prior; the composition-
                                   level prior is symmetric (0.50),
                                   but the right's SMA block's
                                   anatomically stronger coupling
                                   reflects that the right is more
                                   often the bimanual driver (see
                                   CROSS-MIDLINE)

The state structure (sequence_state), the sequencing dynamics, the
five failure-mode handlers, the feature extraction, and the
contribution shape are IDENTICAL across hemispheres. Only area 6's
SMA block config differs. LEFT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left SMA. Cross-midline SMA exchange is
bimanual coordination — the case the right's higher SMA-block
to_commissures prior is about:

    - Bimanual sequencing (the right's primary cross-midline role).
      For a bimanual multi-step action, the right's SMA more often
      drives the interleaving: it proposes the sequence of left- and
      right-hand steps, coordinates the timing, and handles desync
      (its bimanual_coordination weight is the anchor). The left's
      SMA follows the proposed sequence for its own steps and
      coordinates back when it detects a desync from its side.
      Neither reads the other's sequence_state directly; the
      coordination is commissural.

      Note on the to_commissures asymmetry: the composition-level
      (symmetric) prior is 0.50 on both sides; the SMA *block's*
      to_commissures prior is 0.65 on the right and 0.50 on the
      left. These are two different priors at two different levels:
          - the composition-level prior (0.50/0.50) is the
            *bandwidth* of SMA↔SMA exchange, which is inherently
            two-way;
          - the block-level prior (0.65 right / 0.50 left) is the
            *coupling strength* of the right's SMA to the
            commissures specifically, which is higher because the
            right drives the interleaving more often.
      This two-level structure is not a contradiction — it is the
      correct model: the *bandwidth* of two-way coordination is
      symmetric (each side sends on every step), but the *initiative*
      for the interleaving is right-dominant, which shows up as a
      higher block-level coupling on the right.

    - Speech sequencing. The left's SMA sequences the language-
      articulatory steps; the right's sequences prosodic contour
      steps (intonation progression). On the right, the prosodic
      contour is the primary content, and the left's articulatory
      sequence is coordinated via the commissures. A right SMA
      lesion produces flat/atonal sequencing; a left SMA lesion
      produces stuttering-like articulation.

    - Sequence learning. Both SMAs participate in learning a new
      multi-step motor skill; the right's learns spatial/bimanual
      sequences faster (its higher motor_sequence_learning weight
      for spatial content), the left's learns language-articulatory
      sequences faster. The two learning curves are coordinated via
      the commissures.

All three are commissural. The bimanual-sequencing case is the
right's primary role (SMA's distinctive operation is sequencing, and
the right's sequencing is bimanual-dominant), and the two-level
commissural prior structure is the design's way of expressing the
"two-way bandwidth, right-dominant initiative" pattern.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not compose sub-sub-regions. SMA is a LEAF.
    - Must not add an `sma_weight` field. Single area source.
    - Must not implement preparation or execution.
    - Must not reach back into premotor's prepared_programs for
      programs it didn't publish.
    - Must not read area 6's premotor block config.
    - Must not carry peer_input assumptions beyond prefrontal and
      premotor.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not hold module-level mutable state.
    - Must not "fix" the composition-level to_commissures prior
      (0.50/0.50) to be directional because the SMA block's is
      (0.65 right / 0.50 left). The two levels encode different
      things: bandwidth (symmetric) vs initiative (right-dominant).
      Conflating them would either make the bandwidth asymmetric
      (wrong) or make the initiative symmetric (wrong). The
      two-level structure is the correct model.
    - Must not change the sequence-state parameters (capacity,
      timeouts, desync tolerance, lookahead, missing-program
      handling) on the right. These are STRUCTURAL — equal across
      hemispheres. The right's bimanual character emerges from the
      config's feature weights and the SMA-block prior, not from
      different state-management parameters.
    - Must not conflate `bimanual_coordination`'s higher weight on
      the right with a change to the sequence_state's `bimanual_
      role` field's semantics. The field's name ("left_only" =
      left-hand-only, "right_only" = right-hand-only) is symmetric
      across hemispheres; what flips is the *hemisphere's
      relationship* to the field (on the left, "left_only" is
      "ours"; on the right, "right_only" is "ours"). The field name
      and the values are identical; only the interpretation of
      ownership is mirrored.
    - Must not read area 6's SMA block config directly — passed in
      via `config`.
    - Must not import or reference the left SMA. Cross-midline
      exchange goes through `telencephalon/commissures/`. The
      bimanual-sequencing case is the prime example: direct import
      would silently merge the two hemispheres' sequences and make
      the "bimanual desync detection" failure mode untestable.
    - Must not diverge in structure from the left SMA — same class,
      same encode() signature, same state structure (sequence_state
      with active_sequence and current_position), same sequencing
      dynamics, same five failure-mode handlers, same feature
      extraction. Only area 6's SMA block config differs, and only
      by the directional mirror.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_SMA_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_6",
        "source_block": "supplementary_motor_cortex",

        # sequence_state parameters (STRUCTURAL — identical to the
        # left's).
        "max_sequence_length":            20,
        "step_timeout_ticks":             10,
        "postcondition_timeout_ticks":    15,
        "bimanual_desync_tolerance":      2,
        "lookahead_steps":                2,
        "missing_program_action":         "wait_then_abandon",
        "missing_program_wait_ticks":     3,
    }

    Area 6's supplementary_motor_cortex block config
    (brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"]) is
    supplied by FrontalCortex at construction. It provides the
    feature weights and connectivity priors, with the right's
    spatial/bimanual lean.

    RIGHT_SMA_CONFIG is IDENTICAL to LEFT_SMA_CONFIG except that it
    names brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"].
    The state parameters and failure-mode configs are STRUCTURAL —
    equal across hemispheres.

    Two separate tests are needed:
        1. RIGHT_SMA_CONFIG == LEFT_SMA_CONFIG on state parameters
           and failure-mode configs (structural equality).
        2. brodmann_area_6.RIGHT_CONFIG["supplementary_motor_cortex"]
           is a directional mirror of the left's SMA block. NOTE:
           the SMA block's to_commissures prior (0.65 right vs 0.50
           left) is directional (initiative); this is a *block-level*
           prior, and its directionality is correct. The
           composition-level to_commissures (0.50/0.50, in
           RIGHT_FRONTAL_CORTEX_CONFIG) is symmetric (bandwidth) and
           is tested separately. The two are different priors at
           different levels; do not conflate them in the mirror test.

EXPORTS
-------
    from .supplementary_motor_cortex import SupplementaryMotorCortex
    from .supplementary_motor_cortex import RIGHT_SMA_CONFIG

    The class implements the leaf sub-region encode() signature that
    FrontalCortex expects. No dlpfc_weight-style precondition.

    NOTE: This package's construction does NOT depend on the pending
    area-9 amendment (that affects DLPFC only).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  SupplementaryMotorCortex class, import area 6's RIGHT_CONFIG SMA
  block, build RIGHT_SMA_CONFIG, instantiate the class, expose the
  class and the config.
- The class implements the leaf sub-region encode() signature. It
  owns sequence_state (non-empty persistent dict).
- The class is STATEFUL — carries sequence_state across ticks. No
  module-level mutable state.
- Sequencing is broken into documented, unit-testable functions
  (`_build_sequence`, `_advance_sequence`, `_handle_failure_modes`).
  Same functions as on the left; only the config inputs differ
  (right's extraction weights spatial/bimanual features higher).
- The failure-mode handler has one test case per mode (five total).
  The bimanual_desync mode is tested more thoroughly on the right
  because the right is the more frequent driver of bimanual
  interleaving.
- Feature extraction is a documented, unit-testable function.
- The class does not read area 6's premotor block config.
- The class does not import or access any peer sub-sub-region's
  state.
- The class does not implement preparation or execution.
- RIGHT_SMA_CONFIG is structurally identical to LEFT_SMA_CONFIG
  except for the source block reference. State parameters and
  failure-mode configs are STRUCTURAL.
- `sequences` output includes the current step(s) ready to execute
  this tick, plus up to `lookahead_steps` future steps marked
  "lookahead": True. Primary motor executes only the non-lookahead
  steps.
- The `bimanual_role` field's semantics: "left_only" = left-hand-
  only step, "right_only" = right-hand-only step, "both" = bimanual
  step. The field values are symmetric across hemispheres. What
  flips is the *hemisphere's relationship* to the field (on the
  left, "left_only" is "ours"; on the right, "right_only" is
  "ours"). The bimanual coordination logic uses the field values
  and the hemisphere context together, not just the field values.
- Must not import or reference the left SMA. Cross-midline
  exchange goes through `telencephalon/commissures/`.
- Must not change the composition-level to_commissures prior to be
  directional because the SMA block's is. The two levels encode
  bandwidth (symmetric) vs initiative (right-dominant); both are
  correct.

FRONTAL COMPUTE LAYER STATUS (both hemispheres)
-----------------------------------------------
With this file, ALL THREE leaf sub-regions are complete on BOTH
hemispheres, and the frontal compute layer's structure is complete
on both sides modulo the DLPFC-right amendment-blocked file:

    frontal/cortex/__init__.py                          L ✅  R ✅
    prefrontal_cortex/__init__.py                       L ✅  R ✅
    prefrontal_cortex/dorsomedial_prefrontal_cortex/    L ✅  R ✅
    prefrontal_cortex/dorsolateral_prefrontal_cortex/   L ✅  R ✅
    prefrontal_cortex/orbitofrontal_cortex/             L ✅  R ✅
    prefrontal_cortex/ventromedial_prefrontal_cortex/   L ✅  R ✅
    prefrontal_cortex/ventrolateral_prefrontal_cortex/  L ✅  R ✅
    premotor_cortex/                                    L ✅  R ✅
    supplementary_motor_cortex/                         L ✅  R ✅
    primary_motor_cortex/                               L ✅  R ✅
    primary_motor_cortex/precentral_gyrus/              L ✅  R ✅

The only structural gaps remaining in the frontal compute layer are:
    - DLPFC-right (blocked by the area-9 dlpfc_weight amendment)
    - The frontal gyri/sulci annotations (documentary, not compute)
    - The area-8 block-rename cosmetic amendment (optional)
"""