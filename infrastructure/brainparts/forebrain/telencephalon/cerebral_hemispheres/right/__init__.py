"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right
=============================================================================

The RIGHT HEMISPHERE instance.

Mirror of the left package: this module constructs one `Hemisphere` (the
shared class defined in the parent package) using the RIGHT configuration and
exposes it. All internal structure — cortex, rhinencephalon, subcortical,
white_matter — is the same code the left hemisphere runs. Only the weights
and lateralised specialisations differ. This module stays thin on purpose: if
the right hemisphere ever needs behaviour the left cannot express, that
behaviour belongs in the shared class, not here.

WHAT THIS MODULE OWNS
---------------------
One Hemisphere object, configured for the right side, holding four subsystems:

    cortex/          six lobes — representation layer
    rhinencephalon/  ipsilateral smell/affect channel
    subcortical/     evaluation and commitment layer
    white_matter/    intra-hemispheric routing

Per-subsystem specs live in the parent and grandparent packages and are not
duplicated here. This module only decides *how* they are weighted.

RIGHT-DEFAULT CONFIGURATION
---------------------------
Mirror of LEFT_CONFIG: same keys, complementary values. These are defaults
expressed as weights/priors so they can be tuned or ablated. They describe
tendencies, not capabilities — the right hemisphere runs the full shared code
and can do anything the left can, just with different emphasis.

    language          low weight; the right side contributes prosody, humour,
                      and metaphor rather than grammar and lexicon.
    sequencing        lower serial/rule-based weight; stronger parallel and
                      simultaneous processing.
    granularity       bias toward global/gestalt pattern matching and face
                      processing over local detail.
    motor             gross, contralateral control of the left side of the
                      body; posture, orientation, whole-limb movement.
    valence           default bias toward negative-valence avoidance and
                      threat tracking.
    arousal           higher baseline vigilance; faster orienting to novelty
                      and unexpected stimuli.

A representative config (illustrative, the exact mirror of the left):

    RIGHT_CONFIG = {
        "language":   {"production": 0.3, "comprehension": 0.4},
        "sequencing": 0.45,
        "granularity": {"local": 0.4, "global": 0.75},
        "motor":      {"fine": 0.4, "gross": 0.8},
        "valence":    {"positive": 0.4, "negative": 0.7},
        "arousal":    0.7,
    }

Note the values are not arbitrary: each is set so that LEFT_CONFIG and
RIGHT_CONFIG differ only in emphasis, never in capability. Swapping them
(e.g. to model a reversed-lateralisation subject) should produce a coherent
but mirrored individual.

INTERFACE
---------
    right.step(sensory_input) -> motor_output

    executes one hemisphere tick in the shared order:
        represent (cortex) -> evaluate (subcortical) -> commit (basal ganglia
        gate) -> route (white_matter) -> emit motor output.
    The medial temporal lobe writes the episode after the tick resolves.

CROSS-MIDLINE RULE
------------------
This module must never import or reference the left hemisphere. All
cross-midline exchange happens through the `commissures` package in the
grandparent (`telencephalon/commissures/`), which applies transfer delay and
bandwidth. A direct attribute read of `left` from here is a bug, not an
optimisation.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: build RIGHT_CONFIG, pass
  it to the shared Hemisphere class, expose the resulting instance. No logic
  beyond construction and config.
- Config is data, not code: weights live in a dict (or YAML under config/) so
  lateralised experiments can override them without touching this file.
- The exposed object satisfies the same `step(sensory_input) -> motor_output`
  contract as the left hemisphere, so identical unit tests run against both.
- Any behaviour that cannot be expressed as a weight difference is a signal
  that the shared Hemisphere class needs extending — fix it there, not here.
- RIGHT_CONFIG should be maintained as the documented mirror of LEFT_CONFIG:
  when one changes, the other changes with it, and a test should assert that
  the two configs share identical keys and complementary weights.
"""