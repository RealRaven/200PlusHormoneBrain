"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex
===================================================================================

The CORTEX of the right hemisphere — the representation layer.

Mirror of the left cortex package. The cortex is where the hemisphere *builds
its model of the world*: it encodes sensory input (and top-down predictions
from subcortical structures) into typed representations and publishes a single
combined **cortical state** for the evaluation layer (`subcortical/`) to
consume. The cortex does not commit actions — it *proposes*. The basal ganglia
gate every proposal before it becomes behaviour. A cortex that emits motor
output directly is a bug.

This package instantiates six lobe modules with the RIGHT cortical
configuration and composes their outputs into one cortical state object.

THE SIX LOBES (representation modules)
--------------------------------------
Identical to the left in code; the RIGHT config changes the weights inside
them. Summarised as "what each lobe contributes to the state":

    frontal/     goals, plans, working-memory contents, motor intentions,
                 and (right-weighted) emotional prosody, humour, metaphor.
                 Contributes the *intent* slice.
    parietal/    spatial attention, body schema, navigation, multisensory
                 convergence — right-weighted for global spatial layout.
                 Contributes the *where/how* slice.
    temporal/    object identity, audition, face processing, and
                 (right-weighted) prosody/comprehension of tone. Contributes
                 the *what* slice.
    occipital/   visual features, V1–V4 and dorsal/ventral streams —
                 right-weighted toward global/gestalt feature extraction.
                 Contributes the *sight* slice.
    insular/     interoceptive state, taste, autonomic tone, emotional
                 awareness. Contributes the *interoception* slice.
    cingulate/   conflict/salience signals, pain affect, control demand,
                 vigilance. Contributes the *salience* slice.

GRANULARITY DECISION (read before coding)
-----------------------------------------
Inherited unchanged from the left cortex; see
`.../left/cortex/__init__.py` for the full rationale. In short:

  - The runtime unit is the LOBE. Six lobes, six encode() implementations.
  - brodmann_areas/, gyri/, sulci/ are organisational and annotation
    namespaces, not runtime objects. They become named constants/config
    entries inside a lobe (e.g. `parietal.BRODMANN_7`), or data referenced by
    the chemicals/hormones config layer.
  - A sub-region gets its own state only if demonstrably necessary, and then
    as a field/submodule *within* the lobe, not a top-level package.
  - The compute graph stays six nodes wide per hemisphere. The tree remains
    documentation and a place to hang per-region config.

CORTICAL STATE
--------------
    CorticalState = {
        "intent":        frontal.encode(...),
        "where":         parietal.encode(...),
        "what":          temporal.encode(...),
        "sight":         occipital.encode(...),
        "interoception": insular.encode(...),
        "salience":      cingulate.encode(...),
    }

Same shape and same immutability rule as the left hemisphere: one dict-like
object per hemisphere per tick, immutable for the tick, consumed downstream by
`subcortical/` and `white_matter/` only.

RIGHT-SPECIFIC BIAS
-------------------
The lobes are the same code as the left hemisphere; the RIGHT config changes
the weights inside them:

    frontal      higher weight on prosody/humour/metaphor; lower on grammar
                 and lexicon (which the left owns by default)
    temporal     higher weight on tonal/emotional prosody and face identity;
                 lower on lexical comprehension
    occipital/   bias toward global/gestalt feature extraction and whole-
    parietal     scene/spatial layout over local detail
    insular/     right-leaning default valence (avoidance) and higher
    cingulate    arousal/vigilance baseline are applied at the subcortical
                 evaluation stage, but the cortex feeds it the representations
                 that bias will act on.

These are weights, not branches. The same Cortex class runs both sides.

INPUT / OUTPUT CONTRACT
-----------------------
    cortex.step(sensory_input, top_down) -> CorticalState

    sensory_input : dict of modality -> raw/embedded signal for this tick
    top_down      : predictions/priors from subcortical (thalamic relay,
                    basal forebrain gain, amygdala salience bias)
    returns       : the cortical state object described above

    Order within step():
        1. apply top-down gain from basal forebrain (attention)
        2. each lobe encodes its slice
        3. cross-lobe binding (claustrum handoff is triggered downstream,
           not here; cortex only publishes)
        4. return the assembled state

CROSS-MIDLINE RULE
------------------
This module may not import or read the left hemisphere's cortex. Anything
that must cross the midline goes through `telencephalon/commissures/`. Within
the right hemisphere, lobes may read each other's *published* state slices for
binding, but not each other's internal buffers.


Programming contract for this package
-------------------------------------
- Declarative __init__.py: import the six lobe packages, build
  RIGHT_CORTEX_CONFIG, instantiate one shared Cortex class, expose it. No
  per-lobe logic here.
- Each lobe package exposes `encode(inputs, config) -> slice` and nothing else
  that the parent calls. Lobe internals are private.
- The shared Cortex class lives in a neutral location shared with the left
  hemisphere; never duplicate it per side.
- Lobe sub-region names (Brodmann, gyri, sulci) are constants/config, not
  classes, unless a sub-region demonstrably needs its own state.
- Cortical state is immutable per tick; mutation by a consumer is a bug.
- The cortex never emits motor output. It publishes state; `subcortical/`
  and the basal ganglia gate it.
- RIGHT_CORTEX_CONFIG is maintained as the documented mirror of
  LEFT_CORTEX_CONFIG: identical keys, complementary weights. A test should
  assert this so lateralisation cannot drift silently when one side is tuned.
"""