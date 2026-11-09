"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex
==============================================================================================

The FRONTAL CORTEX COMPUTE LAYER — left hemisphere.

This package contains the four frontal compute sub-regions and defines how
they compose into the frontal lobe's `intent` slice. It is the compute-layer
parent of the frontal lobe: `frontal/__init__.py` (the lobe-level file)
documents the 6-step orchestration at a high level; this file documents the
sub-region mechanics that implement it; and each of the four sub-region
packages documents its own per-region computation.

If you are looking for the frontal lobe's *registry* (Brodmann areas, gyri,
sulci), it lives in sibling packages (`brodmann_areas/`, `gyri/`, `sulci/`).
This file is the compute layer, and it has no registry entries of its own.

THE FOUR COMPUTE SUB-REGIONS
----------------------------
    prefrontal_cortex/           FAMILY — five sub-sub-regions:
                                    dorsolateral_prefrontal_cortex (DLPFC)
                                    dorsomedial_prefrontal_cortex (DMPFC)
                                    orbitofrontal_cortex (OFC)
                                    ventrolateral_prefrontal_cortex (VLPFC)
                                    ventromedial_prefrontal_cortex (VMPFC)
                                 Owns the working_memory and goal_stack
                                 state (in DLPFC and DMPFC respectively).

    premotor_cortex/             LEAF — single compute sub-region.
                                 Owns prepared motor programs.

    supplementary_motor_cortex/  LEAF — single compute sub-region.
                                 Owns sequenced multi-step programs.

    primary_motor_cortex/        LEAF — single compute sub-region, with
                                 a nested annotation sub-package
                                 (precentral_gyrus/) that is metadata,
                                 not compute.

Prefrontal is the only family sub-region, and it is a *composite*: the
pattern this file documents for the four top-level sub-regions (parent
calls each child's encode() once per tick, collects one contribution per
child) is applied *recursively* one level down inside prefrontal, with its
five sub-sub-regions acting as the children. The FrontalCortex class
(this layer) treats prefrontal as a black box — it calls prefrontal's
encode() once and gets one contribution back — but prefrontal's encode()
internally orchestrates its own five children with the same pattern.
Recursion, not duplication.

THE COMPOSITION — sequential, prefrontal → premotor → SMA → primary motor
--------------------------------------------------------------------------
Each sub-region is called exactly once per tick, in this order:

    1. prefrontal_cortex          computes goals, plans, working-memory
                                  contents, value estimates, rule
                                  representations, semantic candidates.
                                  Publishes to `peer_input`.

    2. premotor_cortex            reads prefrontal's output (via
                                  `peer_input`), prepares candidate
                                  movement programs with parameters
                                  selected (direction, force, grasp,
                                  target). Publishes to `peer_input`.

    3. supplementary_motor_cortex reads prefrontal and premotor's
                                  output, sequences the prepared
                                  programs into multi-step plans and
                                  bimanual coordinations. Publishes to
                                  `peer_input`.

    4. primary_motor_cortex       reads all three prior contributions,
                                  produces the final executable motor
                                  commands. Its `motor_output` key is
                                  the lobe's actual signal to the
                                  effector system (which the basal
                                  ganglia gate downstream).

The order is *causal*, not arbitrary: prefrontal must produce a goal before
premotor can prepare a movement toward it, premotor must prepare programs
before SMA can sequence them, and SMA must sequence them before primary
motor can execute them. A sub-region that receives an empty upstream
contribution still runs (producing an empty contribution of its own); the
pipeline degrades gracefully rather than short-circuiting.

THE SUB-REGION encode() SIGNATURE
---------------------------------
Each of the four sub-regions exposes exactly one method the parent calls:

    encode(
        sensory_input,      # dict: modality -> representation, from the
                            # other lobes (occipital/temporal/parietal/
                            # insular), passed through unchanged
        top_down,           # dict: modulator -> value, from subcortical
                            # (basal forebrain gain, basal ganglia gating
                            # feedback, amygdala salience bias), passed
                            # through unchanged
        peer_input,         # dict: sub_region_name -> contribution, for
                            # all sub-regions that have already run THIS
                            # TICK (growing; empty for prefrontal)
        state,              # dict: this sub-region's own persistent state,
                            # threaded by the parent from the previous tick
        config,             # dict: this sub-region's config, built from
                            # its own registry areas' configs
    ) -> (contribution, new_state)

Two return values, not one: the contribution (which goes into `intent` and
into `peer_input` for downstream sub-regions) and the new_state (which the
parent holds as this sub-region's state for the next tick).

The `peer_input` mechanism is a growing dict, not a predecessor-only handoff:
primary_motor_cortex sees prefrontal's goals, premotor's prepared programs,
AND SMA's sequences, not just SMA's. This is deliberate — a final motor
command needs to be goal-directed (so primary motor reads prefrontal),
parameterised (so it reads premotor), and sequenced (so it reads SMA). The
alternative — each sub-region only seeing its immediate predecessor — would
force primary motor to reconstruct upstream context from SMA's output alone,
which is lossy. The growing dict is a bit more schema-coupling between
sub-regions, but it's the right trade: sub-regions read only *published*
peer contributions (never each other's internal buffers), and each sub-region
documents which peer keys it reads.

THE INTENT SLICE
----------------
The FrontalCortex class assembles `intent` from the four contributions plus
the final motor output:

    intent = {
        "prefrontal_cortex":         <prefrontal contribution>,
        "premotor_cortex":           <premotor contribution>,
        "supplementary_motor_cortex":<sma contribution>,
        "primary_motor_cortex":      <primary motor contribution>,
        "motor_output":              <executable output from primary motor>,
    }

The four `*_cortex` keys are the sub-regions' contributions *as they
returned them* — the parent does not merge, flatten, or rewrite them. Each
sub-region's contribution is a dict whose keys are documented in that
sub-region's own package docstring. Consumers that need the whole pipeline
read `intent`; consumers that only need, say, the motor commands, read
`intent["motor_output"]` and ignore the rest.

The `motor_output` key is the ONE key that leaves the lobe. It is the final
motor command stream from primary_motor_cortex, and it goes downstream to
the basal ganglia's gating (which can approve, modify, or veto it) and
thence to the effector system. Everything else in `intent` is intent-in-
the-lobe: goals, plans, prepared programs, sequences — all internal, all
subject to downstream revision.

STATE THREADING
---------------
Persistent state lives in the sub-regions, not in the FrontalCortex class:

    prefrontal_cortex/dorsolateral_prefrontal_cortex/   owns working_memory
    prefrontal_cortex/dorsomedial_prefrontal_cortex/    owns goal_stack
    premotor_cortex/                                    owns prepared_programs
    supplementary_motor_cortex/                         owns sequence_state

The FrontalCortex class holds *references* to these states (one dict per
sub-region, opaque) and threads them:

    new_states = {}
    for name in order:
        contribution, new_state = sub_regions[name].encode(
            sensory_input, top_down, peer_input, states[name], configs[name]
        )
        peer_input[name] = contribution
        new_states[name] = new_state
    states = new_states

The parent never inspects or mutates the state dicts' contents. It does not
know what working_memory holds, or what sequence_state tracks — only that
each sub-region's state is a dict it received from that sub-region last
tick and must return to it this tick. That encapsulation is what lets each
sub-region's state structure evolve independently.

LEFT-SPECIFIC BIAS
------------------
The four sub-regions are the same code on both hemispheres; the LEFT
config (via the sub-regions' registry-area configs) changes the weights
inside them. At this composition layer, the lateralisation shows up only
in what each sub-region's config contains, not in the composition itself:

    prefrontal    left-weighted on verbal WM, verbal rules, semantic
                  value, verbal fluency (via DLPFC, VLPFC configs)
    premotor      left-weighted on speech-articulatory planning (PMv)
    SMA           left-weighted on language-articulatory sequences
    primary motor left-weighted on distal precision, corticobulbar
                  speech output

RIGHT mirrors. The composition order, the encode() signature, the
peer_input mechanism, the intent slice schema, and the state-threading
contract are IDENTICAL across hemispheres. Only the config values differ.

INPUT / OUTPUT CONTRACT
-----------------------
    frontal_cortex.step(sensory_input, top_down) -> (intent, new_states)

    sensory_input  : dict, passed through to each sub-region unchanged
    top_down       : dict, passed through to each sub-region unchanged
    returns        : (intent, new_states)
                     intent      — as documented in THE INTENT SLICE above
                     new_states  — dict: sub_region_name -> state dict,
                                   for the next tick

    The FrontalCortex class owns the orchestration; it does not own any
    sub-region's computation, and it does not modify or merge the
    contributions the sub-regions produce.

CROSS-MIDLINE RULE
------------------
No import or read of the right hemisphere's frontal cortex. Interhemispheric
motor and language exchange goes through `telencephalon/commissures/`, not
through this package. Within the left frontal cortex, the four sub-regions
communicate through `peer_input` (published contributions) and through
their mutual connectivity priors (in the registry configs) — but never by
reading each other's internal state. The FrontalCortex class enforces this
by construction: the only thing a sub-region receives is its own `state`,
its own `config`, the shared `sensory_input`/`top_down`, and the
`peer_input` dict of published prior contributions. It cannot reach into
a peer's state because the parent never passes it.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define the four sub-regions' computations. Each is defined
      in its own package; this file defines only their composition.
    - Must not hold persistent state itself. State lives in the
      sub-regions; the FrontalCortex class holds opaque references and
      threads them, but never inspects or mutates their contents.
    - Must not merge, flatten, or rewrite the contributions the
      sub-regions produce. The `intent` slice contains each sub-region's
      contribution verbatim, keyed by sub-region name.
    - Must not short-circuit the pipeline when an upstream sub-region
      returns an empty contribution. Every sub-region runs, every tick,
      in order. Empty upstream means empty downstream; it does not mean
      skipped downstream.
    - Must not import the registry packages directly. The sub-regions
      import their own registry areas; the FrontalCortex class imports
      the sub-regions, not the registry. (The registry is a *sub-region*
      concern, not a *composition* concern.)
    - Must not call a sub-region more than once per tick. The
      state-threading contract depends on each sub-region being entered
      exactly once per tick, in the fixed order. Re-entrancy would
      advance the sub-region's state twice and corrupt the tick
      semantics.
    - Must not diverge in structure from the right hemisphere's frontal
      cortex package — same four sub-regions, same order, same encode()
      signature, same intent slice schema, same peer_input mechanism.
      Only the config values inside the sub-regions differ, and only by
      the directional mirror documented in their registry areas.

NOTE ON THE RECURSIVE COMPOSITION
---------------------------------
The pattern this file documents — "parent calls each child's encode() once
per tick, collects one contribution per child, threads their state" — is
applied recursively one level down inside `prefrontal_cortex/`. Prefrontal
is itself a family of five sub-sub-regions (DLPFC, DMPFC, OFC, VLPFC,
VMPFC), and its encode() internally orchestrates them with the same
pattern: call each in some fixed order, collect contributions, thread
state. From the FrontalCortex class's perspective, prefrontal is a black
box — one encode() call, one contribution back — but the pattern inside
prefrontal is the same one this file documents.

This is intentional: the composition pattern is the same at every level
of the frontal lobe's hierarchy (cortex → sub-region → sub-sub-region →
registry area), so a reader who understands one level understands all of
them. The alternative — different composition patterns at different
levels — would make the lobe harder to reason about for no benefit.

The order of prefrontal's five sub-sub-regions is a *prefrontal* concern,
not a frontal-cortex concern; it is documented in
`prefrontal_cortex/__init__.py`. The FrontalCortex class does not know or
care what order prefrontal's five children run in — it only calls
prefrontal once.

NOTE ON THE `precentral_gyrus` ANNOTATION
------------------------------------------
`primary_motor_cortex/` contains a nested sub-package, `precentral_gyrus/`,
which is an ANNOTATION (like the frontal lobe's `gyri/` and `sulci/` at the
lobe level), not a compute sub-region. It exists because the precentral
gyrus is the surface expression of area 4 and needs a canonical address for
anatomical cross-reference. The FrontalCortex class does not call it; it is
not in the four-sub-region list; and it has no encode() method.

This is the same "annotation can nest inside a compute sub-region" pattern
as `brocas_area/` (which nests inside `brodmann_areas/` at the registry
level). The general rule: annotation can appear anywhere a named anatomical
structure needs a canonical address, including inside compute sub-regions.
The FrontalCortex class's boundary for what it calls is "the four sub-region
names in `LEFT_FRONTAL_CORTEX_CONFIG["order"]`" — anything nested inside a
sub-region is that sub-region's concern, not this layer's.

LEFT-HEMISPHERE CONFIG
----------------------
The composition-level config is minimal — most of the actual config lives
in the sub-regions (which import their own registry areas' configs):

    LEFT_FRONTAL_CORTEX_CONFIG = {
        # The four sub-regions, in the fixed causal order. Changing
        # this order changes the frontal lobe's computation
        # fundamentally, not cosmetically.
        "order": [
            "prefrontal_cortex",
            "premotor_cortex",
            "supplementary_motor_cortex",
            "primary_motor_cortex",
        ],

        # The key in each sub-region's contribution that constitutes
        # its "primary output" for the intent slice. This is used by
        # consumers that want a sub-region's single most important
        # value without reading the whole contribution.
        "primary_output_key": {
            "prefrontal_cortex":          "goals",
            "premotor_cortex":            "prepared_programs",
            "supplementary_motor_cortex": "sequences",
            "primary_motor_cortex":       "motor_commands",
        },

        # The key in the primary_motor_cortex contribution that
        # constitutes the lobe's actual motor output (the signal
        # that leaves the lobe). It is also copied to
        # intent["motor_output"] for convenience.
        "motor_output_key": "motor_commands",
    }

    RIGHT_FRONTAL_CORTEX_CONFIG is IDENTICAL — the composition order,
    the primary-output keys, and the motor-output key are structural
    and do not lateralise. Only the sub-regions' internal configs
    differ.

EXPORTS
-------
    from . import prefrontal_cortex
    from . import premotor_cortex
    from . import supplementary_motor_cortex
    from . import primary_motor_cortex
    from .frontal_cortex import FrontalCortex    # the composition class
    from .frontal_cortex import LEFT_FRONTAL_CORTEX_CONFIG

    The four sub-region packages are re-exported so that the frontal
    lobe's `__init__.py` and downstream consumers can reach them
    without knowing their exact import paths. The FrontalCortex class
    and its config are what this package is *for*; the sub-region
    re-exports are a convenience.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin assembly module: import the four sub-region
  packages, import the shared FrontalCortex class (from a neutral
  location shared with the right hemisphere), build
  LEFT_FRONTAL_CORTEX_CONFIG, instantiate FrontalCortex, and expose it
  along with the four sub-region modules.
- The FrontalCortex class implements `step(sensory_input, top_down) ->
  (intent, new_states)` and nothing else. It does not expose
  per-sub-region accessors beyond the module re-exports; consumers that
  need sub-region internals reach the sub-region packages directly.
- The FrontalCortex class holds:
      - a dict of sub-region instances (`{"prefrontal_cortex": ..., ...}`)
      - a dict of per-sub-region configs (built from each sub-region's
        own registry-area configs, imported at construction time)
      - a dict of per-sub-region state references (opaque; threaded)
  and nothing else. It is stateless across ticks beyond the state dicts
  it threads.
- The order of sub-region calls comes from
  `LEFT_FRONTAL_CORTEX_CONFIG["order"]`, not from a hardcoded list. If
  a future experiment needs a different order (e.g. to model a
  pathological case where premotor runs before prefrontal), it is a
  config change, not a code change.
- The `peer_input` dict passed to each sub-region contains contributions
  from the sub-regions earlier in the order, and only those. Later
  sub-regions do not appear in a peer's `peer_input`. This is enforced
  by construction (the dict grows during the loop), not by convention.
- Sub-region contributions are stored in `intent` by their sub-region
  name, verbatim. The parent does not merge, flatten, or rewrite them.
  Consumers read whichever sub-regions' contributions they need.
- State dicts are opaque to the parent. The parent stores references,
  threads them through, and stores the returned new_state for the next
  tick. It does not inspect, mutate, or merge state dicts. If a
  sub-region's state structure needs to change, that is a sub-region
  concern, not this layer's.
- LEFT_FRONTAL_CORTEX_CONFIG mirrors RIGHT_FRONTAL_CORTEX_CONFIG with
  EQUALITY, not directionality: the composition config is structural
  (order, primary-output keys, motor-output key are identical across
  hemispheres). The lateralisation lives in the sub-regions' internal
  configs, not here. A test should assert that the two configs are
  identical, and separately that the sub-regions' configs are
  directional mirrors of each other.
"""