"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex
==================================================================================

The CORTEX of the left hemisphere — the representation layer.

The cortex is where the hemisphere *builds its model of the world*. It takes
sensory input (and top-down predictions from subcortical structures), encodes
it into typed representations, and publishes a single combined **cortical
state** that the evaluation layer (`subcortical/`) consumes. Crucially, the
cortex does not commit actions: it *proposes*. The basal ganglia gate every
proposal before it becomes behaviour. A cortex that emits motor output
directly is a bug.

This package instantiates six lobe modules with the LEFT cortical
configuration and composes their outputs into one cortical state object.

THE SIX LOBES (representation modules)
--------------------------------------
Each lobe is a computational unit with a documented encode() entry point. It
reads its inputs, writes a typed slice of the cortical state, and nothing
else. The per-lobe functional spec is in the telencephalon package docstring;
summarised here as "what each lobe contributes to the state":

    frontal/     goals, plans, working-memory contents, motor intentions,
                 and (left-weighted) language production. Contributes the
                 *intent* slice.
    parietal/    spatial attention, body schema, multisensory convergence.
                 Contributes the *where/how* slice.
    temporal/    object identity, audition, and (left-weighted) language
                 comprehension. Contributes the *what* slice.
    occipital/   visual features, V1–V4 and dorsal/ventral streams.
                 Contributes the *sight* slice.
    insular/     interoceptive state, taste, autonomic tone, emotional
                 awareness. Contributes the *interoception* slice.
    cingulate/   conflict/salience signals, pain affect, control demand.
                 Contributes the *salience* slice.

GRANULARITY DECISION (read before coding)
-----------------------------------------
The directory tree below each lobe is deep — brodmann_areas/, gyri/, sulci/,
and specific nuclei. These are **not** runtime objects. They are organisational
and annotation namespaces:

  - The runtime unit is the LOBE. Six lobes, six encode() implementations.
  - Brodmann areas, gyri, and sulci exist as named constants / config entries
    used *inside* a lobe to address sub-regions (e.g. `frontal.BRODMANN_44`,
    `temporal.WERNICKES_AREA`), or as data in the hormones/chemicals config
    layer that references them.
  - Where a sub-region genuinely needs distinct state (e.g. primary vs
    secondary visual cortex), it is a field or submodule *within* the lobe,
    not a top-level package with its own lifecycle.

This keeps the model tractable: we simulate six interacting representational
systems per hemisphere, not several hundred independent objects. The tree
stays as documentation and as a place to hang per-region config; the compute
graph is six nodes wide.

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

One dict-like object per hemisphere per tick. Immutable for the duration of
the tick; consumers downstream must not mutate it. Two things read it:

    subcortical/            evaluates it, gates actions, writes memory
    white_matter/           routes slices between lobes and to/from the
                            opposite hemisphere (via commissures only)

LEFT-SPECIFIC BIAS
------------------
The lobes are the same code as the right hemisphere; the LEFT config changes
the weights inside them:

    frontal      higher language-production weight (Broca dominance)
    temporal     higher language-comprehension weight (Wernicke dominance)
    occipital/   bias toward local/detail feature extraction over global
    parietal     gestalt integration
    insular/     left-leaning default valence (approach) is applied at the
    cingulate    subcortical evaluation stage, but the cortex feeds it the
                 representations that bias will act on.

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
This module may not import or read the right hemisphere's cortex. Anything
that must cross the midline goes through `telencephalon/commissures/`. Within
the left hemisphere, lobes may read each other's *published* state slices for
binding, but not each other's internal buffers.


Programming contract for this package
-------------------------------------
- Declarative __init__.py: import the six lobe packages, build LEFT_CORTEX_CONFIG,
  instantiate one shared Cortex class, expose it. No per-lobe logic here.
- Each lobe package exposes `encode(inputs, config) -> slice` and nothing else
  that the parent calls. Lobe internals are private.
- The shared Cortex class lives in a neutral location (e.g. `cortex/base.py`
  or the parent hemisphere package), not duplicated per side.
- Lobe sub-region names (Brodmann, gyri, sulci) are constants/config, not
  classes, unless a sub-region demonstrably needs its own state — in which
  case document why in that lobe's docstring.
- Cortical state is immutable per tick; mutation by a consumer is a bug.
- The cortex never emits motor output. It publishes state; `subcortical/`
  and the basal ganglia gate it.
"""