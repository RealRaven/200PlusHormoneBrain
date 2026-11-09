"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.anterior_cingulate
==============================================================================================================

The ANTERIOR CINGULATE CORTEX (ACC) of the right hemisphere — conflict
monitoring, error detection, pain affect, and control allocation.

Mirror of the left ACC package. The ACC answers three questions every tick,
in this order:

    1. Did what happen match what was expected?      -> conflict / error
    2. Does this hurt, and how much?                 -> affect weight
    3. How much control should I demand next tick?   -> control_demand

Its output is not a representation of the world; it is a *signal about the
quality of the cortex's current processing* that modulates the cortex one tick
later. It is the only sub-module with a legitimate same-tick read of
subcortical action-outcome feedback: to compute error, it must see what the
basal ganglia actually committed and what reward/outcome followed.

FUNCTIONAL COMPUTATION
----------------------
Identical to the left; the RIGHT config changes the weights. Four channels
returned into the parent's `salience` slice:

    conflict        scalar 0..1. Response conflict = competition between
                    simultaneously active but mutually incompatible action or
                    interpretation candidates. Right-weighted sources:
                    competing spatial targets (parietal/), competing
                    visuomotor responses, competing threat interpretations.
                    Modelled as a normalized measure of overlap/interference
                    among candidate representations.

    error           scalar 0..1. Prediction error between predicted outcome
                    (frontal/) and actual outcome (subcortical/ feedback).
                    The ERN-like channel; fires after a committed action's
                    result is known and feeds forward as a learning signal.
                    Right-weighted toward spatial/motor prediction error.

    affect          scalar 0..1. Affective (not sensory) component of pain
                    and threat. Reads interoceptive/affective state from
                    insular/ and threat state from subcortical/ (extended
                    amygdala). Outputs the *unpleasantness* weight, distinct
                    from the sensory-discriminative signal in parietal/.
                    Right-weighted toward autonomic/visceral affect.

    control_demand  scalar 0..1. Allocated control = f(conflict, error,
                    current performance). The ACC's efferent signal; the
                    output that modulates other lobes next tick.
                    Right-weighted toward spatial/motor and autonomic demand.

BRODMANN SUBDIVISIONS (constants, not classes)
----------------------------------------------
    BRODMANN_24         dorsal cognitive division — conflict monitoring
    BRODMANN_32         dorsal cognitive division — error/performance
    BRODMANN_25         subgenual affective division — affective pain,
                        negative valence, autonomic/visceral coupling

Named constants used to address sub-regions inside encode(), or referenced by
the chemicals/hormones config layer. Not instantiated as objects. Area 25 may
later gain its own state (depression/DBS); it would become a field inside this
package, not a new package.

INPUTS
------
    from frontal/       goals, plans, predicted outcomes
    from temporal/      object interpretations (competing candidates)
    from parietal/      spatial targets (competing candidates)
    from insular/       interoceptive/affective state (feeds `affect`)
    from subcortical/   action-outcome feedback (feeds `error`)

OUTPUTS
-------
    {"conflict": ..., "error": ..., "affect": ..., "control_demand": ...}

The parent assembles these into `salience`. Application of `control_demand`
as targeted gain on other lobes is the Cortex base class's job, one tick
later — ACC must not mutate other lobes directly.

RIGHT-SPECIFIC BIAS
-------------------
Same code as the left ACC; the RIGHT config changes the weights:

    conflict        higher weight on *spatial/visuomotor* conflict (e.g.
                    competing spatial targets, competing reach/gaze
                    responses, competing threat interpretations); lower
                    weight on lexical/verbal conflict
    error           higher weight on spatial/motor prediction error; lower
                    on language-related prediction error
    affect          higher weight than left on autonomic/visceral affect;
                    right ACC's affective contribution is more bodily and
                    threat-driven, less verbally mediated
    control_demand  higher weight on spatial/motor demand and autonomic
                    regulation; lower on verbal working-memory demand

These are weights inside the same encode() function, not code branches. A
config-driven test should confirm that the right ACC's conflict signal is
dominated by spatial/visceral inputs and the left by lexical inputs when both
receive identical multimodal input.

CROSS-MIDLINE RULE
------------------
No import or read of the left hemisphere's ACC. Interhemispheric conflict
(when left and right disagree on a committed action or interpretation) is a
real signal and is fed in through `telencephalon/commissures/`, not by direct
access to the other side.


Programming contract for this package
-------------------------------------
- __init__.py is thin: build RIGHT_ACC_CONFIG, instantiate the shared
  AnteriorCingulate class, expose it. The class lives in a neutral location
  shared with the left side.
- The class exposes `encode(inputs, config) -> dict` returning the four
  channels above. No side effects, no mutation of inputs.
- conflict, error, affect, and control_demand are each computed by a small
  private method (`_compute_conflict`, `_compute_error`, `_compute_affect`,
  `_compute_control_demand`) so they can be unit-tested in isolation.
- The same-tick read of subcortical action-outcome feedback is the only
  permitted upward read; document any other as a bug.
- RIGHT_ACC_CONFIG mirrors LEFT_ACC_CONFIG (identical keys, complementary
  weights); assert this in tests.
"""