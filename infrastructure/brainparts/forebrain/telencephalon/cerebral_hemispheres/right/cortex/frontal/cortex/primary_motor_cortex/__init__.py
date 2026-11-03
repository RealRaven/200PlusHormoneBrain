"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.primary_motor_cortex
======================================================================================================================

The PRIMARY MOTOR CORTEX — right hemisphere. A LEAF compute sub-region of
the frontal cortex, the final stage of the frontal motor hierarchy, and the
ONLY sub-region whose output leaves the frontal lobe.

Mirror of the left primary motor package. Primary motor is the
movement-EXECUTION core: given sequenced programs (from SMA, which
sequenced the prepared programs from premotor, which were prepared toward
goals from prefrontal), it produces the actual motor commands that drive
the effectors. On the RIGHT, the commands executed are predominantly
gross/proximal (arm, leg, trunk, postural adjustments) and corticobulbar-
expression (facial expression, emotional facial movement) rather than the
left's fine/distal and speech-articulatory commands. The execution
mechanics are the same; the effectors driven and their lateralised
weighting are mirrored.

Primary motor is called FOURTH (last) in the frontal cortex's composition
order. It sees all three upstream sub-regions' contributions via
peer_input, and it publishes its `motor_commands` as
`intent["motor_output"]` — the one key that leaves the lobe.

TWO STRUCTURAL FIRSTS (both inherited from the left; documented here for
completeness)
------------------------------------------------------------------------
1. THE LOBE'S OUTPUT. Primary motor's `motor_commands` is copied to
   `intent["motor_output"]` and is consumed by the basal ganglia's
   gating and, if approved, by the effector system. On the right, the
   commands executed are the gross/proximal component and the
   affective-expression component of the system's behaviour.

2. THE NESTED ANNOTATION. `primary_motor_cortex/` contains a
   sub-package, `precentral_gyrus/`, which is an ANNOTATION (like the
   frontal lobe's `gyri/` and `sulci/` and like
   `cingulate/indusium_griseum/`). It has NO `encode()` method, NO
   config, NO state. See the ANNOTATION NESTING section below.

PRIMARY MOTOR IS A PURE FUNCTION (same as the left)
---------------------------------------------------
Primary motor carries NO persistent state across ticks. It is a pure
function of its inputs. The parent threads `{}` through primary motor's
state slot, and `encode()` does not read or write state.

The state-asymmetric motor hierarchy is the same on both sides:

    premotor       STATEFUL — prepared_programs
    SMA            STATEFUL — sequence_state
    primary motor  PURE — executes the current tick's sequenced
                   commands, holds nothing

Persistence lives upstream, where candidates and sequences are being
assembled over time. Primary motor's conversion has no temporal extent.
If a future experiment needs a primary-motor-level buffer (refractory
period, last-command memory), that's a schema change in the leaf
sub-regions' state contract — not an ad-hoc state addition here.

PRIMARY MOTOR'S REGISTRY-AREA SOURCE
------------------------------------
Primary motor has ONE frontal-registry area source:

    brodmann_area_4/        primary motor cortex

Its config (in `brodmann_area_4.RIGHT_CONFIG`) provides the primary
motor feature weights and connectivity priors. On the right, the
weights lean toward proximal_power (0.80), corticobulbar_expression
(0.65), force_gain (0.70), and velocity_gain (0.65); distal_precision
(0.40) and corticobulbar_speech (0.30) are reduced. The connectivity
priors reflect the right's stronger corticospinal coupling (0.80) and
weaker corticobulbar coupling (0.35).

Because there is only one area source, there is NO share weight.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

Identical to the left. Steps:

        1. Read peer_input — primary motor is called FOURTH (last), so
           it sees all three upstream contributions:
               peer_input["prefrontal_cortex"]            — goals,
                   value signals
               peer_input["premotor_cortex"]              —
                   prepared_programs
               peer_input["supplementary_motor_cortex"]   —
                   sequences

        2. Extract primary motor features. On the right, extraction
           weights proximal/gross and expression-affector targets
           higher.

        3. Apply area 4's config to weight the features.

        4. Execute: convert SMA's sequences into motor commands,
           apply force/velocity gains, emit. Empty sequences → empty
           commands (no reaching back into premotor's prepared
           programs).

        5. Compute primary motor's contribution.

        6. Return (contribution, new_state) where new_state is {}
           (primary motor is pure).

The motor_commands are what `intent["motor_output"]` will be, and
what the basal ganglia gate.

EXECUTION (the primary-motor-specific operational pattern)
----------------------------------------------------------
Same command structure as the left:

    {
        "command_id":      unique within-hemisphere monotonic ID,
        "source_program_id": the program_id from premotor's
                           prepared_programs,
        "source_sequence_id": the sequence_id from SMA's
                           sequence_state,
        "effector":        which effector(s). On the right, more
                           often "left_arm", "left_leg", "trunk",
                           "facial_expression_left"; on the left,
                           "right_hand", "vocal_tract", "facial_
                           expression_right". The two hemispheres
                           together cover both sides of the body and
                           both facial expressions, with the
                           contralateral mapping.
        "parameters": {
            "direction":   unit vector or symbolic,
            "force":       scalar,
            "velocity":    scalar,
            "articulatory_target": None on the right (except for
                           prosodic features, which are carried
                           separately as intonation contours),
        },
        "gain_applied": {
            "force_gain":    the gain applied this tick,
            "velocity_gain": the gain applied this tick,
        },
    }

The command list is the tick's executable output. The basal ganglia
gate it; approved commands proceed, vetoed commands are dropped and
the veto is fed back to premotor.

On the right, force_gain is typically higher than on the left (the
right's proximal movements need more force scaling), and velocity_gain
is typically higher (whole-body movement smoothness). Both are the
right's config's feature weights, applied at execution time.

Empty sequences → empty commands. This is the same contract; it does
NOT reach back into premotor's prepared_programs.

FEATURE EXTRACTION (the primary motor's inputs)
-----------------------------------------------
    From sensory_input:
        target_state          — effectors' and environment's current
                                state (limb position, visual target
                                position). On the right, limb
                                position is more finely represented
                                (proximal/gross motor's proprioceptive
                                feedback is more detailed for limb
                                movements); on the left, articulator
                                position is more finely represented.
        proprioceptive_feedback — body position feedback

    From top_down:
        basal_forebrain_gain  — attention/arousal
        cingulate_control     — targeted control from ACC
        basal_ganglia_gate    — previous tick's gating decisions
        cerebellar_feedback   — timing and error-correction. On the
                                right, more relevant for gross motor
                                timing (the right's proximal/reaching
                                execution relies more on cerebellar
                                correction than the left's speech
                                articulation).
        primary_somatosensory — sensory feedback from the moving
                                body part

    From peer_input:
        (same three upstream sub-regions as on the left)

    Extraction rules documented in the primary motor class. On the
    right, extraction weights proximal/gross/expression-affector
    targets higher.

CONTRIBUTION SHAPE
------------------
    contribution = {
        "distal_precision":         <scalar>,
        "proximal_power":           <scalar>,
        "corticobulbar_speech":     <scalar>,
        "corticobulbar_expression": <scalar>,
        "force_gain":               <scalar>,
        "velocity_gain":            <scalar>,

        "motor_commands": [
            {command dict (see EXECUTION)},
            ...
        ],
        "active_sequence_id":  the sequence_id from SMA that the
                              commands belong to (or None),
    }

`motor_commands` is copied to `intent["motor_output"]` by
FrontalCortex and is the lobe's actual signal to the effector system.
On the right, the commands are predominantly limb and facial-expression
movements.

RIGHT-SPECIFIC BIAS
------------------
Same class as the left primary motor; the RIGHT config changes the
weights (via area 4's config):

    proximal_power            higher (0.80) — the right's anchor;
                              gross/proximal control
    distal_precision          lower (0.40)
    corticobulbar_expression  higher (0.65) — facial expression; the
                              right's anchor for the face
    corticobulbar_speech      lower (0.30) — speech articulators are
                              more left-lateralised
    force_gain                higher (0.70)
    velocity_gain             higher (0.65)
    to_corticospinal_tract    higher (0.80) — the right's dominant
                              motor output is limb/postural
    to_corticobulbar_tract    lower (0.35)
    to_commissures            higher (0.45) — the right's gross/
                              postural output is what bimanual
                              coordination needs to reach the left's
                              fine/distal output

The class, the execution logic, the command structure, the gain
application, the empty-sequence fallback, and the nested annotation
are IDENTICAL across hemispheres. Only area 4's feature values differ.
LEFT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left primary motor. Cross-midline primary
motor exchange is about combining effector commands. On the right,
the cases emphasise the right's role as the SENDER of the gross/
positional and expression components:

    - Bimanual execution. The right's primary motor executes the
      gross/positional commands (left arm, left leg, trunk, posture);
      the left's executes the fine/distal commands (right hand,
      fingers, precision grip). The two hemispheres' commands are
      combined for coordinated bimanual execution. The right's higher
      to_commissures prior (0.45 vs the left's 0.30) is the
      anatomical basis: the right's gross/positional commands are
      the ones that most often need to cross to enable the left's
      fine coordination.

    - Speech execution. The left's primary motor executes the
      lexical/articulatory commands; the right's executes the
      prosodic commands (intonation contour, facial expression for
      speech). The two are combined at the speech effectors for
      fluent, intoned speech. Direct import would silently merge the
      two and make the "flat speech with intact content" failure
      mode untestable.

    - Facial expression. The right's primary motor executes the
      expression commands (spontaneous, emotionally-driven facial
      movements — the right is dominant for spontaneous expression);
      the left's executes the volitional expression commands (posed
      smiles, deliberate facial movements). This is a real
      asymmetric pattern: a right primary motor lesion impairs
      spontaneous emotional expression more than posed expression,
      and a left lesion produces the reverse. The two hemispheres'
      expression commands combine at the facial effectors, with the
      right contributing the affective dimension and the left the
      volitional dimension.

    - Conjugate eye movements. The FEF's commands require conjugate
      execution — both eyes move together. The coordination is
      commissural.

All four are commissural. The bimanual-execution and speech-execution
cases are the most studied; the facial-expression case is a specific
right-side signature that a left-side file wouldn't emphasise as
strongly. All are testable predictions of the commissural
architecture.

ANNOTATION NESTING — precentral_gyrus/
--------------------------------------
`primary_motor_cortex/` contains the nested `precentral_gyrus/`
annotation on the right as on the left. Same contract:

    - has NO `encode()` method
    - has NO `LEFT_CONFIG` or `RIGHT_CONFIG`
    - has NO state
    - is NOT in `RIGHT_FRONTAL_CORTEX_CONFIG["order"]`
    - is NOT called by FrontalCortex
    - is NOT part of the four-sub-region composition

It exists because the precentral gyrus is the surface expression of
area 4 and needs a canonical address for anatomical cross-reference.
The annotation's `ANATOMY` is identical across hemispheres (anatomy
does not lateralise); only `SIDE` differs.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. Primary motor is pure on the
      right as on the left; persistence lives upstream.
    - Must not add a `primary_motor_weight` field.
    - Must not add a `precentral_gyrus` entry to
      RIGHT_FRONTAL_CORTEX_CONFIG["order"]. It is an annotation.
    - Must not give `precentral_gyrus/` a config, a state, or an
      encode() method.
    - Must not reach back into premotor's prepared_programs when SMA
      publishes an empty sequence.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not implement sequencing (SMA) or preparation (premotor).
    - Must not read area 4's config directly.
    - Must not change the execution parameters (default_force_gain,
      default_velocity_gain, max_commands_per_tick,
      empty_sequence_emits) on the right. These are STRUCTURAL.
      The right's higher force and velocity at execution emerge from
      area 4's feature weights (force_gain 0.70, velocity_gain 0.65),
      not from different defaults. A test that assumed "right
      primary motor has different default gains" would fail; the
      defaults are equal, and the effective per-tick gains come from
      the config's feature weights applied to the current state.
    - Must not import or reference the left primary motor.
      Cross-midline exchange goes through
      `telencephalon/commissures/`. The speech-execution and
      facial-expression cases are the prime examples: direct import
      would silently merge the two hemispheres' effector commands
      and make the "flat speech with intact content" and
      "spontaneous-expression deficit" failure modes untestable.
    - Must not diverge in structure from the left primary motor —
      same class, same encode() signature, no state (both pure
      functions), same execution logic, same command structure, same
      empty-sequence fallback, same nested annotation. Only area 4's
      config differs.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_PRIMARY_MOTOR_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_4",

        # Execution parameters (STRUCTURAL — identical to the
        # left's).
        "default_force_gain":     1.0,
        "default_velocity_gain":  1.0,
        "max_commands_per_tick":  10,
        "empty_sequence_emits":   [],
    }

    Area 4's config (brodmann_area_4.RIGHT_CONFIG) is supplied by
    FrontalCortex at construction. It provides the six feature
    weights and the connectivity priors.

    RIGHT_PRIMARY_MOTOR_CONFIG is IDENTICAL to
    LEFT_PRIMARY_MOTOR_CONFIG except that it names
    brodmann_area_4.RIGHT_CONFIG. Execution parameters are
    STRUCTURAL — equal across hemispheres.

    Two separate tests are needed:
        1. RIGHT_PRIMARY_MOTOR_CONFIG == LEFT_PRIMARY_MOTOR_CONFIG on
           execution parameters (structural equality).
        2. brodmann_area_4.RIGHT_CONFIG is a directional mirror of
           LEFT_CONFIG (feature and connectivity values mirror).
           `precentral_gyrus/` is tested for structural equality
           only — it has no configurable fields.

EXPORTS
-------
    from .primary_motor_cortex import PrimaryMotorCortex
    from .primary_motor_cortex import RIGHT_PRIMARY_MOTOR_CONFIG
    from . import precentral_gyrus    # the nested annotation; re-export
                                      # for cross-reference access

    The class implements the leaf sub-region encode() signature that
    FrontalCortex expects. No dlpfc_weight-style precondition.

    NOTE: This package's construction does NOT depend on the pending
    area-9 amendment (that affects DLPFC only).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  PrimaryMotorCortex class, import area 4's RIGHT_CONFIG, build
  RIGHT_PRIMARY_MOTOR_CONFIG, instantiate the class, expose the
  class, the config, and the nested precentral_gyrus annotation.
- The class implements the leaf sub-region encode() signature.
  Primary motor is PURE — state input is always {}, output state is
  always {}.
- The class is STATELESS.
- Execution is broken into documented, unit-testable functions
  (`_commands_from_sequences`, `_apply_gain`).
- Feature extraction is a documented, unit-testable function. On the
  right, extraction weights proximal/gross and expression-effector
  targets higher.
- The class does not reach back into premotor's prepared_programs
  when sequences are empty.
- The class does not import or access any peer sub-sub-region's
  state.
- The class does not read `precentral_gyrus`'s contents.
- RIGHT_PRIMARY_MOTOR_CONFIG is structurally identical to
  LEFT_PRIMARY_MOTOR_CONFIG except for the source config reference.
  Execution parameters are STRUCTURAL.
- `precentral_gyrus/` has no config, no state, no encode(). A test
  should assert it has no `encode` attribute.
- `motor_commands` is the lobe's actual output. FrontalCortex copies
  it to `intent["motor_output"]`; the basal ganglia gate it.
- Must not import or reference the left primary motor. Cross-midline
  exchange goes through `telencephalon/commissures/`.

FRONTAL COMPUTE LAYER STATUS (both hemispheres)
-----------------------------------------------
With this file, two of the three leaf sub-regions (premotor, primary
motor) are complete on both hemispheres, and the third (SMA) is
pending on both sides:

    frontal/cortex/__init__.py                          L ✅  R ✅
    prefrontal_cortex/__init__.py                       L ✅  R ✅
    prefrontal_cortex/dorsomedial_prefrontal_cortex/    L ✅  R ✅
    prefrontal_cortex/dorsolateral_prefrontal_cortex/   L ✅  R ⬜ (amendment)
    prefrontal_cortex/orbitofrontal_cortex/             L ✅  R ✅
    prefrontal_cortex/ventromedial_prefrontal_cortex/   L ✅  R ✅
    prefrontal_cortex/ventrolateral_prefrontal_cortex/  L ✅  R ✅
    premotor_cortex/                                    L ✅  R ✅
    supplementary_motor_cortex/                         L ⬜  R ⬜
    primary_motor_cortex/                               L ✅  R ✅
"""