"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.primary_motor_cortex
====================================================================================================================

The PRIMARY MOTOR CORTEX — left hemisphere. A LEAF compute sub-region of the
frontal cortex, the final stage of the frontal motor hierarchy, and the ONLY
sub-region whose output leaves the frontal lobe.

Primary motor is the movement-EXECUTION core: given sequenced programs
(from SMA, which sequenced the prepared programs from premotor, which were
prepared toward goals from prefrontal), it produces the actual motor
commands that drive the effectors. It is the end of the frontal
computation — the point at which "intent" becomes "action".

Primary motor is called FOURTH (last) in the frontal cortex's composition
order. It sees all three upstream sub-regions' contributions via
peer_input: prefrontal's goals and value, premotor's prepared_programs,
and SMA's sequences. It publishes its `motor_commands` as
`intent["motor_output"]` — the one key that leaves the lobe.

TWO STRUCTURAL FIRSTS
---------------------
This file introduces two structures not seen in any earlier frontal
sub-region:

    1. THE LOBE'S OUTPUT. Every other frontal sub-region contributes to
       `intent` (which stays inside the lobe). Primary motor's
       `motor_commands` is copied to `intent["motor_output"]` and is
       consumed by the basal ganglia's gating and, if approved, by the
       effector system. The "final cortical motor output stage" is not
       a metaphor — this is literally where the lobe's action output
       originates.

    2. THE NESTED ANNOTATION. `primary_motor_cortex/` contains a
       sub-package, `precentral_gyrus/`, which is an ANNOTATION (like
       the frontal lobe's `gyri/` and `sulci/` at the lobe level and
       like `cingulate/indusium_griseum/` at the lobe level) — not a
       compute sub-region. It exists because the precentral gyrus is
       the surface expression of area 4 and needs a canonical address
       for anatomical cross-reference. It has NO `encode()` method,
       NO config, NO state. See the ANNOTATION NESTING section below.

PRIMARY MOTOR IS A PURE FUNCTION (a deliberate design decision)
---------------------------------------------------------------
Primary motor carries NO persistent state across ticks. It is a pure
function of its inputs: sensory_input, top_down, peer_input, its config.
The parent threads `{}` through primary motor's state slot, and
`encode()` does not read or write state.

This is a deliberate design choice, not an oversight, and it's worth
spelling out because the motor hierarchy's state is asymmetric:

    premotor       STATEFUL — holds prepared_programs (candidates being
                   readied, decaying unless rehearsed)
    SMA            STATEFUL — holds sequence_state (ordered programs
                   being sequenced across ticks)
    primary motor  PURE — executes the current tick's sequenced
                   commands, holds nothing

The rationale: persistence lives upstream, where candidates and
sequences are being *assembled over time*. Primary motor's job is the
final conversion — sequenced-programs-this-tick → motor-commands-this-
tick — which has no temporal extent of its own. If the system needs to
"hold a motor command ready" (e.g. prepare to strike on a cue), that
persistence belongs in premotor's prepared_programs or SMA's
sequence_state, not in primary motor. Adding a motor-command buffer to
primary motor would blur the prepare/sequence/execute division and
would duplicate the persistence already upstream.

If a future experiment genuinely needs a primary-motor-level buffer
(e.g. a refractory period after execution, or a last-command memory
for error monitoring), that is a schema change documented in the leaf
sub-regions' state contract — not an ad-hoc state addition here.

PRIMARY MOTOR'S REGISTRY-AREA SOURCE
------------------------------------
Primary motor has ONE frontal-registry area source:

    brodmann_area_4/        primary motor cortex

Its config (in `brodmann_area_4.LEFT_CONFIG`) provides the primary
motor feature weights and connectivity priors: distal_precision,
proximal_power, corticobulbar_speech, corticobulbar_expression,
force_gain, velocity_gain, plus priors to premotor_cortex,
supplementary_motor_cortex, basal_ganglia, cerebellum,
primary_somatosensory_cortex, corticospinal_tract,
corticobulbar_tract, and commissures.

Because there is only one area source, there is NO share weight — no
`primary_motor_weight` field. Same pattern as DMPFC, VMPFC, premotor.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

        1. Read peer_input — primary motor is called FOURTH (last),
           so it sees all three upstream contributions:
               peer_input["prefrontal_cortex"]            — goals,
                   value signals (for directing the commands
                   toward the intended target)
               peer_input["premotor_cortex"]              —
                   prepared_programs (the movement candidates)
               peer_input["supplementary_motor_cortex"]   —
                   sequences (the ordered multi-step programs)

        2. Extract primary motor features from sensory_input and
           top_down. On the left, extraction weights distal_precision
           and corticobulbar_speech higher.

        3. Apply area 4's config to weight the features.

        4. Execute (see EXECUTION below):
               a. Read the sequences from SMA's contribution. These
                  are the ordered programs for this tick.
               b. For each element in the current sequence's active
                  step, generate the corresponding motor command —
                  direction, force, velocity, and (for speech tasks)
                  the articulatory target. The commands are the
                  *executable* form of the prepared program's
                  parameters, converted to the effector system's
                  interface.
               c. Apply the gain modulators from area 4's config
                  (force_gain, velocity_gain) to scale the commands.
               d. If no sequences are present (SMA published empty),
                  emit empty motor_commands — primary motor does
                  not improvise.

        5. Compute primary motor's contribution:
               - the motor_commands (this tick's executable output)
               - the feature dict (from step 3)

        6. Return (contribution, new_state) where new_state is {}
           (primary motor is pure).

The motor_commands are what `intent["motor_output"]` will be, and
what the basal ganglia gate.

EXECUTION (the primary-motor-specific operational pattern)
----------------------------------------------------------
Primary motor's distinctive computation is execution — converting
sequenced programs into motor commands. Each command is:

    {
        "command_id":      unique within-hemisphere monotonic ID,
        "source_program_id": the program_id from premotor's
                           prepared_programs that this command
                           executes (for traceability),
        "source_sequence_id": the sequence_id from SMA's
                           sequence_state that this command
                           belongs to,
        "effector":        which effector(s) — categorical
                           ("left_hand", "right_hand", "vocal_tract",
                           "eyes", ...); on the left, distal
                           effectors (fingers, articulators) are
                           weighted higher,
        "parameters": {
            "direction":   unit vector or symbolic,
            "force":       scalar,
            "velocity":    scalar,
            "articulatory_target": phonological representation
                           (for speech commands; None for limb
                           commands),
        },
        "gain_applied": {
            "force_gain":    the gain applied this tick,
            "velocity_gain": the gain applied this tick,
        },
    }

The command list is this tick's executable output. The basal ganglia
gate it: approved commands proceed to the effectors; vetoed commands
are dropped, and the veto is fed back to premotor (via top_down's
basal_ganglia_gate) to suppress the corresponding prepared program.

Execution is the *conversion* — not the *choice*. Which program to
execute is determined upstream (premotor prepared it, SMA sequenced
it, prefrontal's goals directed it). Primary motor's job is to
produce a well-formed executable command for each sequenced step,
scaled by the appropriate gains.

If SMA publishes an empty sequence list, primary motor emits an empty
command list. It does not reach back into premotor's prepared
programs to execute an unsequenced candidate — that would bypass
SMA's sequencing role and would break the causal order (premotor →
SMA → primary motor).

FEATURE EXTRACTION (the primary motor's inputs)
-----------------------------------------------
    From sensory_input:
        target_state          — the current state of the effectors
                                and the environment they're acting on
                                (limb position, articulator position,
                                visual target position); primary
                                motor uses this to compute the
                                direction/force needed to reach the
                                commanded target from the current
                                state (the actual motor command is
                                a delta from current state to target)
        proprioceptive_feedback — the body's own position feedback
                                (also via top_down's
                                primary_somatosensory input)

    From top_down:
        basal_forebrain_gain  — attention/arousal
        cingulate_control     — targeted control from ACC
        basal_ganglia_gate    — the previous tick's gating decisions
                                (approved/vetoed feedback)
        cerebellar_feedback   — timing and error-correction; on the
                                left, more relevant for speech
                                articulatory timing; on the right,
                                for gross motor timing
        primary_somatosensory — sensory feedback from the moving
                                body part (the sensorimotor loop);
                                used to correct the command mid-
                                execution

    From peer_input:
        peer_input["prefrontal_cortex"]           — goals, value
        peer_input["premotor_cortex"]             — prepared_programs
                                                    (the candidates
                                                    being executed)
        peer_input["supplementary_motor_cortex"]  — sequences (the
                                                    ordered programs;
                                                    primary motor
                                                    executes the
                                                    current step of
                                                    the active sequence)

    The extraction rules are documented in the primary motor class.
    On the left, extraction weights distal/speech-affector targets
    higher; on the right, proximal/gross targets.

CONTRIBUTION SHAPE
------------------
    contribution = {
        # The six primary motor features (weighted by area 4's config)
        "distal_precision":         <scalar>,
        "proximal_power":           <scalar>,
        "corticobulbar_speech":     <scalar>,
        "corticobulbar_expression": <scalar>,
        "force_gain":               <scalar>,
        "velocity_gain":            <scalar>,

        # Operational output — the executable motor commands
        "motor_commands": [
            {command dict (see EXECUTION)},
            ...
        ],
        "active_sequence_id":  the sequence_id from SMA that the
                              commands belong to (or None if
                              execution was empty),
    }

`motor_commands` is copied to `intent["motor_output"]` by FrontalCortex
and is the lobe's actual signal to the effector system.

LEFT-SPECIFIC BIAS
------------------
Same class as the right primary motor; the LEFT config changes the
weights (via area 4's config):

    distal_precision          higher (0.85) — fine hand/finger
                              control; the left's anchor
    proximal_power            lower (0.40)
    corticobulbar_speech      higher (0.80) — speech articulators;
                              the left's signature
    corticobulbar_expression  lower (0.35)
    to_corticospinal_tract    lower (0.70)
    to_corticobulbar_tract    higher (0.75) — the left's dominant
                              motor output is speech
    to_commissures            lower (0.30)

The class, the execution logic, the command structure, the gain
application, and the empty-sequence fallback are IDENTICAL across
hemispheres. Only area 4's feature values differ. RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right primary motor. Cross-midline primary
motor exchange is about combining effector commands from the two
hemispheres:

    - Bimanual execution. When SMA has sequenced a bimanual action,
      the right's primary motor executes the gross/positional
      commands (right arm, right hand as stabiliser) and the left's
      executes the fine/distal commands (left hand as actor). The
      two hemispheres' motor_commands are combined for coordinated
      bimanual execution. The combination is commissural; neither
      primary motor reads the other's commands directly.

    - Speech execution. The left's primary motor executes the
      lexical/articulatory commands (phoneme motor programs); the
      right's executes the prosodic commands (intonation contour,
      facial expression for speech). The two are combined at the
      speech effectors (vocal tract, face) for fluent, intoned
      speech. Direct import would silently merge the two and make
      the "flat speech with intact content" failure mode untestable.

    - Conjugate eye movements. The FEF's commands (via premotor's
      pathway to primary motor's face representation) require
      conjugate execution — both eyes move together. The two
      hemispheres' eye commands must be coordinated; the
      coordination is commissural.

All three are commissural. The speech-execution case is the canonical
one, and the "flat speech with intact content" failure mode — a
right-sided primary motor lesion alone, or a commissure cut — is the
most directly testable consequence.

ANNOTATION NESTING — precentral_gyrus/
--------------------------------------
`primary_motor_cortex/` contains a nested sub-package,
`precentral_gyrus/`, which is an ANNOTATION. It:

    - has NO `encode()` method
    - has NO `LEFT_CONFIG` or `RIGHT_CONFIG`
    - has NO state
    - is NOT in `LEFT_FRONTAL_CORTEX_CONFIG["order"]`
    - is NOT called by FrontalCortex
    - is NOT part of the four-sub-region composition

It exists because the precentral gyrus is the surface expression of
area 4 and needs a canonical address for anatomical cross-reference
(receptor distribution lookups, lesion annotation, connectivity
metadata). It is the same third-category pattern as
`cingulate/indusium_griseum/` and as the frontal lobe's `gyri/` and
`sulci/` — a pure anatomical annotation.

The general rule: annotation can appear anywhere a named anatomical
structure needs a canonical address, INCLUDING inside compute
sub-regions. The nesting is a tree-organisation detail; the annotation
is a documentary namespace, not an agent. Do not give it a lifecycle.

Note that primary motor's `precentral_gyrus/` is the only annotation
currently nested inside a compute sub-region. It is documented here
because the nesting is new; a future annotation inside SMA or
premotor would follow the same pattern.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. Primary motor is pure; the
      persistence lives upstream (premotor's prepared_programs, SMA's
      sequence_state). Adding a motor-command buffer here would
      duplicate the upstream state and blur the division of labour.
    - Must not add a `primary_motor_weight` field. Single area source.
    - Must not add a `precentral_gyrus` entry to
      LEFT_FRONTAL_CORTEX_CONFIG["order"], or to any sub-region list.
      It is an annotation, not a compute sub-region. Adding it would
      break the composition (an annotation has no encode() method).
    - Must not give `precentral_gyrus/` a config, a state, or an
      encode() method. The absence of these is the point; the
      annotation is documentary.
    - Must not reach back into premotor's prepared_programs when SMA
      publishes an empty sequence. If nothing is sequenced, nothing
      is executed. Bypassing SMA would break the causal order
      (premotor → SMA → primary motor) and would make the
      sequencing stage's role meaningless.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not implement sequencing (SMA's job) or preparation
      (premotor's job). Primary motor executes.
    - Must not read area 4's config directly — passed in via `config`.
    - Must not import or reference the right primary motor.
      Cross-midline exchange goes through
      `telencephalon/commissures/`. The speech-execution case is the
      prime example: direct import would silently merge the left's
      articulatory commands with the right's prosodic commands and
      make the "flat speech with intact content" failure mode
      untestable.
    - Must not diverge in structure from the right primary motor —
      same class, same encode() signature, no state (both pure
      functions), same execution logic, same command structure, same
      empty-sequence fallback, same nested annotation. Only area 4's
      config differs.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_PRIMARY_MOTOR_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_4",

        # Execution parameters (STRUCTURAL — equal across
        # hemispheres).
        "default_force_gain":     1.0,    # baseline; the config's
                                          # feature weights modulate
                                          # this per-tick
        "default_velocity_gain":  1.0,
        "max_commands_per_tick":  10,     # safety cap; a sequence
                                          # step larger than this is
                                          # truncated (with a
                                          # logged warning)
        "empty_sequence_emits":   [],     # the explicit empty output
                                          # (documented; see the
                                          # "MUST NOT DO" item above)
    }

    Area 4's config (brodmann_area_4.LEFT_CONFIG) is supplied by
    FrontalCortex at construction. It provides the six feature
    weights and the connectivity priors.

    RIGHT_PRIMARY_MOTOR_CONFIG is IDENTICAL except that it names
    brodmann_area_4.RIGHT_CONFIG. The execution parameters are
    STRUCTURAL — equal across hemispheres. The lateralisation lives
    entirely in area 4's feature weights and connectivity priors.

    Two separate tests are needed:
        1. RIGHT_PRIMARY_MOTOR_CONFIG == LEFT_PRIMARY_MOTOR_CONFIG on
           execution parameters (structural equality).
        2. brodmann_area_4.RIGHT_CONFIG is a directional mirror of
           LEFT_CONFIG (feature and connectivity values mirror). The
           `precentral_gyrus/` annotation is tested for structural
           equality only — it has no configurable fields.

EXPORTS
-------
    from .primary_motor_cortex import PrimaryMotorCortex
    from .primary_motor_cortex import LEFT_PRIMARY_MOTOR_CONFIG
    from . import precentral_gyrus    # the nested annotation; re-export
                                      # for cross-reference access

    The class implements the leaf sub-region encode() signature that
    FrontalCortex expects. No dlpfc_weight-style precondition.

    NOTE: This package's construction does NOT depend on the pending
    area-9 amendment (that affects DLPFC only).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  PrimaryMotorCortex class, import area 4's LEFT_CONFIG, build
  LEFT_PRIMARY_MOTOR_CONFIG, instantiate the class, expose the class,
  the config, and the nested precentral_gyrus annotation module.
- The class implements the leaf sub-region encode() signature.
  Primary motor is PURE — state input is always {}, output state is
  always {}.
- The class is STATELESS — it holds nothing across ticks.
- Execution is broken into documented, unit-testable functions:
  `_commands_from_sequences(sequences, current_state, config)`,
  `_apply_gain(commands, force_gain, velocity_gain)`. Each tested
  with synthetic sequences and state.
- Feature extraction is a documented, unit-testable function.
- The class does not reach back into premotor's prepared_programs
  when sequences are empty. Empty sequences → empty commands. This
  is a documented contract, tested with a synthetic empty-sequences
  input.
- The class does not import or access any peer sub-sub-region's
  state — only peer_input contributions.
- The class does not read `precentral_gyrus`'s contents. The
  annotation is documentary; the class is unaware of it at runtime
  (the parent's re-export is for external cross-reference only).
- `LEFT_PRIMARY_MOTOR_CONFIG` is structurally identical to
  `RIGHT_PRIMARY_MOTOR_CONFIG` except for the source config
  reference. Execution parameters are STRUCTURAL.
- `precentral_gyrus/` has no config, no state, no encode(). It is a
  pure annotation with only `ANATOMY` and `SIDE` (left) exports. A
  test should assert that it is NOT importable as a compute
  sub-region (i.e. it has no `encode` attribute).
- `motor_commands` is the lobe's actual output. The FrontalCortex
  class copies it to `intent["motor_output"]`; the basal ganglia
  gate it before it reaches the effectors. Do not add downstream
  execution logic here — primary motor produces commands; the
  effectors execute them.
- Must not import or reference the right primary motor. Cross-midline
  exchange goes through `telencephalon/commissures/`.
"""