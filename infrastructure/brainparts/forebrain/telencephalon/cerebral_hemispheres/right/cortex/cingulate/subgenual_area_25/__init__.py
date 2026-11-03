"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.subgenual_area_25
=============================================================================================================

The SUBGENUAL ANTERIOR CINGULATE (Brodmann area 25) — right hemisphere.

Mirror of the left area-25 package. A COMPUTE SUB-MODULE of the ACC's
affective division, living as a sibling of `brodmann_areas/` rather than
inside it. This is the documented layout exception in the cingulate tree,
and it is deliberate:

    - Area 25 is the only cingulate Brodmann area whose functional role is
      distinctive enough to warrant its own compute package rather than a
      config-only registry entry. It carries the ACC's ENTIRE affect
      channel (areas 24 and 32 contribute nothing to it), and its role in
      treatment-resistant depression, autonomic regulation, and DBS
      response means it is expected to grow state as the project develops.
    - Filing it inside `brodmann_areas/` would have made it look like a
      registry entry with config values, which is the wrong shape. Filing
      it under `anterior_cingulate/` would have hidden that it is the
      affect channel's sole owner. Living as a sibling of both is the
      only placement that is honest about what it is.

If you are looking for the registry entry that maps Brodmann area 25 to
this package, it does not exist inside `brodmann_areas/` — this package
IS the registry entry for area 25, plus the compute. Cross-references in
the other Brodmann area configs point here by package name
(`cingulate/subgenual_area_25/`), not by Brodmann number inside
`brodmann_areas/`.

WHAT IT COMPUTES
----------------
One scalar, every tick:

    affect          scalar 0..1. The affective (not sensory) component of
                    pain, threat, and negative valence. This is the
                    *unpleasantness* weight — how much the current state
                    should bias avoidance, withdrawal, and negative-
                    valence weighting in downstream subcortical systems.
                    It is distinct from the sensory-discriminative pain
                    signal (which lives in `parietal/`) and from the
                    phasic fear signal (which lives in
                    `subcortical/medial_temporal_lobe/amygdala/`).

The `affect` scalar is the ACC's fourth channel; areas 24 and 32 carry
the other three (conflict, error, control_demand). Area 25 is the sole
producer of `affect`, and the ACC combines it with the other three into
the `salience` slice. On the right, the affect channel is weighted
toward autonomic/visceral and threat-related contributors — see
RIGHT-SPECIFIC BIAS.

STATE (THE REASON THIS PACKAGE IS DIFFERENT)
--------------------------------------------
Unlike the PCC and RSC, which are pure functions of their inputs, area 25
is stateful. It holds two pieces of persistent state:

    affective_setpoint    a slow-moving baseline of affective tone. The
                          tick-by-tick `affect` output is *relative to*
                          this setpoint, so a chronically elevated
                          threat environment produces a sustained
                          elevation of the baseline rather than a
                          one-tick spike that decays. The setpoint
                          drifts toward the recent average of the raw
                          affect signal (with a time constant
                          documented in the config).

    treatment_response    a parameter that governs how strongly the
                          affect signal responds to top-down regulation
                          attempts (from frontal/) and to DBS-like
                          modulation (a config-level knob for experiments
                          that model treatment-resistant depression).
                          Not a clinical claim; a modelling affordance.

Both are per-hemisphere state, retained across ticks, and are the reason
this package cannot use the same "pure function" contract as the PCC and
RSC. The ACC class that consumes this sub-module must therefore call it
once per tick in a fixed order, and must not re-enter it.

COMPUTATION
-----------
    encode(inputs, state, config) -> (affect, new_state)

        1. Read raw affect contributors from inputs (see INPUTS below).
        2. Compute raw_affect = weighted_combination(contributors, config).
        3. Regulate: raw_affect is attenuated by top-down control from
           frontal/ according to `treatment_response`:
               regulated = raw_affect * (1 - treatment_response * top_down_control)
        4. Emit: affect = clip(regulated + affective_setpoint, 0, 1)
        5. Update setpoint: affective_setpoint = drift_toward(
               affective_setpoint, regulated, time_constant)
        6. Return (affect, new_state) where new_state carries the updated
           setpoint and any other persistent fields.

The order matters: the setpoint influences the output *before* it drifts
toward the current signal. This makes the setpoint a genuine baseline,
not just a smoothed version of the output. The same order applies on
both hemispheres.

INPUTS
------
    from insular/       interoceptive/affective state (the primary input
                        on the right; visceral sensation, autonomic tone)
    from frontal/       top-down control signal (regulatory attempt;
                        used in step 3, not step 2)
    from subcortical/   threat state from extended_amygdala; the
                        sustained-threat input that distinguishes area 25
                        from the phasic amygdala
    from parietal/      sensory-discriminative pain input (received but
                        NOT used for the affect computation; area 25
                        produces the affective component only, and the
                        two components are recombined downstream by the
                        ACC when it assembles the salience slice — this
                        keeps the affective and sensory components of
                        pain separable in the model)

The parietal/ input is read but not used; it is passed through to the
ACC's salience assembly alongside the `affect` scalar. This is documented
explicitly because an unused input looks like a bug otherwise. On the
right, the interoceptive and threat inputs carry a larger share of the
raw affect — see RIGHT-SPECIFIC BIAS.

RIGHT-SPECIFIC BIAS
-------------------
Same code as the left area 25; the RIGHT config changes the weights and
the setpoint dynamics:

    raw_affect weighting    higher weight on interoceptive and threat
                            contributors (the right's affect is more
                            bodily and threat-driven, less verbally
                            mediated)
    affective_setpoint      shorter drift (faster time constant) than the
                            left; the right baseline is more reactive to
                            acute threat, less stable
    treatment_response      lower baseline responsivity to top-down
                            control (the right's affect is less easily
                            regulated by verbal/cognitive means; more
                            responsive to autonomic/threat signals)

    RIGHT_CONFIG = {
        # ---- raw_affect weighting ----
        "interoceptive_weight":      0.75,   # left: 0.55
        "threat_weight":             0.45,   # left: 0.30
        "verbal_affect_weight":      0.10,   # left: 0.35

        # ---- regulation ----
        "treatment_response":        0.35,   # left: 0.55
        "top_down_weight":           0.35,   # left: 0.50

        # ---- setpoint dynamics ----
        "setpoint_time_constant":    8.0,    # ticks; left: 20.0
        "setpoint_initial":          0.35,   # left: 0.30

        # ---- output clipping (structural, identical to left) ----
        "affect_floor":              0.00,
        "affect_ceil":               1.00,
    }

    All weights are plausible priors, not measured constants. The two key
    constraints are:
      - the three raw_affect weights (interoceptive, threat, verbal) are
        relative importances; their *ratios* matter, not their sum (they
        are not constrained to sum to 1.0)
      - the setpoint dynamics must be well-defined: time_constant > 0,
        setpoint_initial in [affect_floor, affect_ceil]

    The mirror test (see the programming contract) checks these
    DIRECTIONALLY: interoceptive and threat weights go up from left to
    right, verbal weight goes down, treatment_response goes down,
    time_constant goes down, setpoint_initial goes up. It is not a
    numerical complementarity check — these are directional biases, not
    two halves of a budget.

EXPORTS
-------
    from .subgenual_area_25 import SUBGENUAL_25    # int, == AREA_ID (25)
    from .subgenual_area_25 import ANATOMY
    from .subgenual_area_25 import RIGHT_CONFIG
    from .subgenual_area_25 import RIGHT_INITIAL_STATE
    from .subgenual_area_25 import SubgenualArea25  # the compute class
    from .subgenual_area_25 import SYSTEM           # str, "anterior_cingulate"

    The class is exported here (unlike the Brodmann area registry entries,
    which export only constants). The pattern is different because this
    package is a compute node, not a config-holder.

    `RIGHT_INITIAL_STATE` is a dict:
        {"affective_setpoint": <from RIGHT_CONFIG["setpoint_initial"]>}
    The ACC class constructs the initial state from this dict; the class
    does not carry module-level mutable state.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 25 / subgenual anterior cingulate",
        "system": "anterior_cingulate (affective division)",
        "location": "ventral anterior cingulate, subgenual to the genu "
                    "of the corpus callosum, on the medial surface of "
                    "the frontal lobe",
        "cytoarchitecture": "agranular cortex; six-layer homologue with "
                            "prominent layer V projection neurons",
        "notes": (
            "The affective division of the ACC. Dense reciprocal "
            "connectivity with the insula, amygdala, hypothalamus, "
            "periaqueductal gray, and brainstem autonomic nuclei; "
            "reciprocal with medial prefrontal cortex. The single most "
            "reproducible finding in treatment-resistant depression "
            "neuroimaging is abnormal area-25 activity, and it is the "
            "principal DBS target for that condition — which is why this "
            "package carries the `treatment_response` knob. Not a claim "
            "that the model has any clinical validity; a modelling "
            "affordance for experiments that want to vary the "
            "regulability of affect. On the right side the autonomic "
            "and visceral couplings are somewhat stronger than on the "
            "left (consistent with the right ACC's overall affective "
            "profile); this is a functional emphasis, not an anatomical "
            "difference. The anatomical area is bilateral and symmetric."
        ),
    }

    Anatomy is identical to the left except for the noted right-side
    functional emphasis. The structure is the same; the affect profile
    differs.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not compute conflict, error, or control_demand. Those belong to
      areas 24 and 32. Area 25's ONLY output channel is `affect`.
    - Must not represent the sensory-discriminative component of pain.
      That lives in parietal/; area 25 receives it and passes it through
      to the ACC's salience assembly, but does not compute it.
    - Must not carry module-level mutable state. The setpoint lives in
      the instance returned by the SubgenualArea25 class, constructed
      from RIGHT_INITIAL_STATE. This keeps the class testable and
      prevents accidental cross-tick state bleed between instances.
    - Must not be re-entered within a tick. The ACC class must call
      `encode()` exactly once per tick, in a fixed order relative to the
      other ACC channels. Re-entrancy would advance the setpoint twice
      and corrupt the drift dynamics.
    - Must not import `anterior_cingulate/` (cycle; the ACC imports from
      here, not the other way round).
    - Must not import any of the `brodmann_areas/brodmann_area_24` or
      `brodmann_area_32` packages (the sibling relationship is by
      reference in docstrings, not by import). The three areas are
      independent producers whose outputs are combined by the ACC class.
    - Must not import or reference the left hemisphere's area 25.
      Cross-hemisphere affective state exchange goes through
      `telencephalon/commissures/`, never by direct access. In particular,
      the two hemispheres' `affective_setpoint` values are independent
      and are expected to diverge under sustained threat — the right
      setpoint will drift upward faster and further than the left's
      because its time constant is shorter. Surfacing that divergence
      is the commissures' job, not area 25's.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  SubgenualArea25 class, build RIGHT_CONFIG and RIGHT_INITIAL_STATE,
  expose the class and the config. The class itself lives in a neutral
  shared location, not in this file.
- The class exposes `encode(inputs, state, config) -> (affect, new_state)`.
  The two-tuple return is deliberate: the class does not mutate the
  state dict in place, so the caller decides when to commit the new
  state. This makes the class testable with fixed inputs and predictable
  across ticks.
- The class must implement `drift_toward(current, target, time_constant)`
  as a documented, unit-testable function: the standard exponential
  smoothing with the given time constant, expressed in ticks:
      new = current + (target - current) / time_constant
  and clip new to [affect_floor, affect_ceil].
- The `treatment_response` and `top_down_weight` parameters must be
  validated: top_down_control is expected in [0, 1]; the effective
  regulation is clipped so that regulated >= 0.
- RIGHT_CONFIG mirrors LEFT_CONFIG with complementary values: interoceptive
  and threat weights go up (right) / down (left), verbal weight goes down
  (right) / up (left), treatment_response down (right) / up (left),
  time_constant shorter (right) / longer (left). The mirror test must
  check these directionally, not just for numerical complementarity —
  these are not "sum to 1" pairs, they are directional biases.
- The `affect_floor` and `affect_ceil` are IDENTICAL across hemispheres
  (structural, like the RSC's clip bounds).
- Cross-references from area 24 and area 32 configs point to this
  package; the reverse import must never happen.
- RIGHT_INITIAL_STATE uses RIGHT_CONFIG["setpoint_initial"] (0.35), not
  LEFT_CONFIG's (0.30) — the initial state must be built from the same
  config that the instance uses, not from the sibling hemisphere's
  config.
"""