"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left
============================================================================

The LEFT HEMISPHERE instance.

This package does not define new structure. It constructs one `Hemisphere`
(the shared class defined in the parent package) using the LEFT configuration,
and exposes it. Everything below the surface — cortex, rhinencephalon,
subcortical, white_matter — is the same code the right hemisphere runs; only
the weights and lateralised specialisations differ. Keeping this module thin
is deliberate: if the left hemisphere ever needs behaviour the right cannot
express, that behaviour belongs in the shared class, not here.

WHAT THIS MODULE OWNS
---------------------
One Hemisphere object, configured for the left side, holding four subsystems:

    cortex/          six lobes — representation layer
    rhinencephalon/  ipsilateral smell/affect channel
    subcortical/     evaluation and commitment layer
    white_matter/    intra-hemispheric routing

Per-subsystem specs are documented in the parent and grandparent packages and
are not duplicated here. This module only decides *how* they are weighted.

LEFT-DEFAULT CONFIGURATION
--------------------------
These are defaults, expressed as weights/priors so they can be tuned or
ablated for experiments. They describe tendencies, not capabilities — the
left hemisphere still runs the full shared code and can do anything the right
can, just with different emphasis.

    language          high weight on production (Broca) and comprehension
                      (Wernicke); the left side is the default language owner.
    sequencing        high weight on serial/sequential processing and
                      rule-based, step-by-step reasoning.
    granularity       bias toward local detail and categorical classification
                      over global/gestalt pattern matching.
    motor             fine, contralateral control of the right side of the
                      body; precision over gross movement.
    valence           default bias toward positive-valence approach and
                      reward tracking.
    arousal           lower baseline vigilance than the right; slower to
                      orient to novelty.

A representative config (illustrative, to be finalised in code):

    LEFT_CONFIG = {
        "language":   {"production": 0.9, "comprehension": 0.9},
        "sequencing": 0.8,
        "granularity": {"local": 0.75, "global": 0.35},
        "motor":      {"fine": 0.8, "gross": 0.4},
        "valence":    {"positive": 0.7, "negative": 0.4},
        "arousal":    0.45,
    }

INTERFACE
---------
    left.step(sensory_input) -> motor_output

    executes one hemisphere tick in the shared order:
        represent (cortex) -> evaluate (subcortical) -> commit (basal ganglia
        gate) -> route (white_matter) -> emit motor output.
    The medial temporal lobe writes the episode after the tick resolves.

CROSS-MIDLINE RULE
------------------
This module must never import or reference the right hemisphere. All
cross-midline exchange happens through the `commissures` package in the
grandparent (`telencephalon/commissures/`), which applies transfer delay and
bandwidth. A direct attribute read of `right` from here is a bug, not an
optimisation.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: build LEFT_CONFIG, pass it
  to the shared Hemisphere class, expose the resulting instance. No logic
  beyond construction and config.
- Config is data, not code: weights live in a dict (or YAML under config/) so
  lateralised experiments can override them without touching this file.
- The exposed object satisfies the same `step(sensory_input) -> motor_output`
  contract as the right hemisphere, so identical unit tests run against both.
- Any behaviour that cannot be expressed as a weight difference is a signal
  that the shared Hemisphere class needs extending — fix it there, not here.
"""