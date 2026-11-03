"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate.anterior_cingulate
=============================================================================================================

The ANTERIOR CINGULATE CORTEX (ACC) of the left hemisphere — conflict
monitoring, error detection, pain affect, and control allocation.

The ACC is the cognitive-affective division of the cingulate. It answers three
questions every tick, in this order:

    1. Did what happen match what was expected?      -> conflict / error
    2. Does this hurt, and how much?                 -> affect weight
    3. How much control should I demand next tick?   -> control_demand

Its output is not a representation of the world; it is a *signal about the
quality of the cortex's current processing* that modulates the cortex one tick
later. This is why it is the only sub-module with a legitimate same-tick read
of subcortical action-outcome feedback: to compute error, it must see what the
basal ganglia actually committed and what reward/outcome followed.

FUNCTIONAL COMPUTATION
----------------------
Three coupled signals, each returned in the parent's `salience` slice:

    conflict        scalar 0..1. Response conflict = competition between
                    simultaneously active but mutually incompatible action or
                    interpretation candidates. Sources: frontal/ intentions
                    vs. actual goal-relevant features; temporal/ competing
                    object interpretations; parietal/ competing spatial
                    targets. Modelled as a normalized measure of overlap/
                    interference among candidate representations, not as a
                    fixed input.

    error           scalar 0..1. Prediction error = discrepancy between the
                    predicted outcome (from frontal/) and the actual outcome
                    (from subcortical/ action-outcome feedback). This is the
                    ERN-like channel: it fires *after* a committed action's
                    result is known and feeds forward as a learning signal.

    affect          scalar 0..1. Affective (not sensory) component of pain
                    and threat. Reads interoceptive/affective state from
                    insular/ and threat state from subcortical/ (extended
                    amygdala); outputs the *unpleasantness* weight, distinct
                    from the sensory-discriminative pain signal that lives in
                    parietal/. This is the channel that lets ACC bias
                    avoidance/withdrawal via the subcortical valence system.

    control_demand  scalar 0..1. The allocated control signal. This is a
                    function of (conflict, error, current performance): high
                    conflict or high error with poor performance raises
                    control_demand; low conflict/error with good performance
                    lowers it. This is the ACC's *efferent* signal — the
                    output that will modulate other lobes next tick.

BRODMANN SUBDIVISIONS (constants, not classes)
----------------------------------------------
    BRODMANN_24         dorsal cognitive division — conflict monitoring
    BRODMANN_32         dorsal cognitive division — error/performance
    BRODMANN_25         subgenual affective division — affective pain,
                        negative valence, autonomic/visceral coupling

These are named constants used to address sub-regions inside the encode()
logic (e.g. weighting the affective contribution differently from the
cognitive contribution), or referenced by the chemicals/hormones config layer.
They are not instantiated as objects. Area 25 in particular may later gain its
own state (its role in treatment-resistant depression and DBS is well
documented), but it would become a field inside this package, not a new
package.

INPUTS
------
    from frontal/       goals, plans, predicted outcomes
    from temporal/      object interpretations (competing candidates)
    from parietal/      spatial targets (competing candidates)
    from insular/       interoceptive/affective state (feeds `affect`)
    from subcortical/   action-outcome feedback: what was committed, what
                        reward/outcome followed (feeds `error`)

OUTPUTS
-------
Returns three scalars into the parent Cingulate's slice:

    {"conflict": ..., "error": ..., "affect": ..., "control_demand": ...}

The parent assembles these into `salience`. Application of `control_demand`
as targeted gain on other lobes is the Cortex base class's job, one tick
later — ACC must not mutate other lobes directly.

LEFT-SPECIFIC BIAS
------------------
Same code as the right ACC; the LEFT config changes the weights:

    conflict        higher weight on *lexical/verbal* conflict (e.g.
                    competing word meanings, competing verbal responses);
                    lower weight on spatial/visuomotor conflict
    error           higher weight on language-related prediction error;
                    lower on spatial/motor prediction error
    affect          slightly lower weight than right on autonomic/visceral
                    affect; the left ACC's affective contribution is more
                    verbally mediated (e.g. rumination), less visceral
    control_demand  higher weight on verbal working-memory load and
                    lexical-selection demand; lower on spatial/motor demand

These are weights inside the same encode() function, not code branches. A
config-driven test should confirm that the left ACC's conflict signal is
dominated by lexical inputs and the right by spatial/visceral inputs when
both receive identical multimodal input.

CROSS-MIDLINE RULE
------------------
No import or read of the right hemisphere's ACC. Interhemispheric conflict
(when left and right disagree on a committed action or interpretation) is a
real signal and is fed in through `telencephalon/commissures/`, not by direct
access to the other side.


Programming contract for this package
-------------------------------------
- __init__.py is thin: build LEFT_ACC_CONFIG, instantiate the shared
  AnteriorCingulate class, expose it. The class lives in a neutral location
  shared with the right side.
- The class exposes `encode(inputs, config) -> dict` returning the four
  channels above. No side effects, no mutation of inputs.
- conflict, error, affect, and control_demand are each computed by a small
  private method (`_compute_conflict`, `_compute_error`, `_compute_affect`,
  `_compute_control_demand`) so they can be unit-tested in isolation.
- The same-tick read of subcortical action-outcome feedback is the only
  permitted upward read; document any other as a bug.
- LEFT_ACC_CONFIG mirrors RIGHT_ACC_CONFIG (identical keys, complementary
  weights); assert this in tests.
"""