"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex
===============================================================================================

The FRONTAL CORTEX COMPUTE LAYER — right hemisphere.

Mirror of the left frontal cortex package. This package contains the four
frontal compute sub-regions and defines how they compose into the frontal
lobe's `intent` slice. It is the compute-layer parent of the right frontal
lobe: `frontal/__init__.py` (the lobe-level file) documents the 6-step
orchestration at a high level; this file documents the sub-region mechanics
that implement it; and each of the four sub-region packages documents its
own per-region computation.

If you are looking for the right frontal lobe's *registry* (Brodmann areas,
gyri, sulci), it lives in sibling packages (`brodmann_areas/`, `gyri/`,
`sulci/`). This file is the compute layer, and it has no registry entries
of its own.

THE FOUR COMPUTE SUB-REGIONS
----------------------------
Identical set to the left, with identical subdivision structure:

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
pattern this file documents for the four top-level sub-regions is applied
recursively one level down inside prefrontal, with its five sub-sub-regions
acting as the children. The FrontalCortex class (this layer) treats
prefrontal as a black box — it calls prefrontal's encode() once and gets
one contribution back — but prefrontal's encode() internally orchestrates
its own five children with the same pattern. Recursion, not duplication.

On the RIGHT, the same four sub-regions with the same subdivision
structure exist, and the same recursive composition applies inside
prefrontal. Anatomy and composition structure do not lateralise; only the
config values inside the sub-regions do.

THE COMPOSITION — sequential, prefrontal → premotor → SMA → primary motor
--------------------------------------------------------------------------
Each sub-region is called exactly once per tick, in this order:

    1. prefrontal_cortex          computes goals, plans, working-memory
                                  contents, value estimates, rule
                                  representations, scene-semantic
                                  candidates (on the right).
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
pipeline degrades gracefully rather than short-circuiting. This is
identical on the right — composition order is structural, not lateralised.

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

Two return values: contribution (which goes into `intent` and into
`peer_input` for downstream sub-regions) and new_state (which the parent
holds as this sub-region's state for the next tick).

The `peer_input` mechanism is a growing dict — primary_motor_cortex sees
prefrontal's goals, premotor's prepared programs, AND SMA's sequences, not
just SMA's. The rationale is documented in the left file's full text; the
mechanism is identical on the right. Sub-regions read only *published* peer
contributions, never each other's internal state, and each sub-region
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
read `intent`; consumers that only need the motor commands read
`intent["motor_output"]` and ignore the rest.

The `motor_output` key is the ONE key that leaves the lobe. It is the final
motor command stream from primary_motor_cortex, and it goes downstream to
the basal ganglia's gating and thence to the effector system. Everything
else in `intent` is intent-in-the-lobe.

On the right, the *content* of the intent slice is the right-hemisphere
version: prefrontal computes scene-semantic candidates rather than verbal
ones; premotor prepares spatial reaching/grasping programs rather than
speech-articulatory ones; SMA sequences spatial/bimanual plans rather than
language-articulatory sequences; primary motor produces proximal/gross
motor commands and facial expression commands rather than fine distal and
speech-articulatory commands. The schema of the intent slice is identical;
only the contents differ.

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

The right's state *content* differs — right DLPFC's working memory holds
spatial rather than verbal content, right DMPFC's goal stack holds
threat-relevant and spatially-situated goals rather than verbal ones, right
premotor's prepared programs are reaching/grasping rather than
speech-articulatory, right SMA's sequence state tracks spatial/bimanual
sequences rather than language-articulatory ones — but the state
*structure* and the threading contract are identical. From the
FrontalCortex class's perspective, the state dicts are opaque either way;
only the sub-regions know what's inside them.

RIGHT-SPECIFIC BIAS
-------------------
The four sub-regions are the same code on both hemispheres; the RIGHT
config (via the sub-regions' registry-area configs) changes the weights
inside them. At this composition layer, the lateralisation shows up only
in what each sub-region's config contains, not in the composition itself:

    prefrontal    right-weighted on spatial WM, spatial rules,
                  scene-semantic value, scene-semantic control (via
                  DLPFC, VMPFC, VLPFC configs)
    premotor      right-weighted on reaching/grasping planning (PMd)
    SMA           right-weighted on spatial/bimanual sequencing
    primary motor right-weighted on proximal power, corticospinal
                  output, facial expression

LEFT mirrors. The composition order, the encode() signature, the
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
No import or read of the left hemisphere's frontal cortex. Interhemispheric
motor and language exchange goes through `telencephalon/commissures/`, not
through this package.

On the RIGHT specifically, the classic cross-midline cases are:

    - Bimanual coordination. The right's premotor and SMA propose the
      gross/positional and spatial/bimanual components of a movement;
      the left's propose the fine/distal component; the commissures
      combine them into a coherent bimanual action. Neither hemisphere
      reads the other's prepared programs or sequence state directly —
      the bimanual action only works if the exchange goes through the
      commissures, with the delay and bandwidth they model.

    - Prosody-to-speech delivery. The right's prefrontal (via area 47
      and Broca's area's prosody role) computes the affective-prosodic
      content of an utterance; the left's prefrontal and primary motor
      compute the lexical and articulatory content. The prosody reaches
      the left's speech output via the commissures. A direct import
      would bypass the commissural handoff and make the flat-speech
      failure mode (intact content, no prosodic contour) untestable.

    - Visual exploration ↔ reading. The right's FEF (via area 8) drives
      the exploration scan path; the left's FEF drives reading
      saccades. Conjugate eye movements require continuous
      interhemispheric exchange of FEF activity; this is a per-tick
      commissural traffic pattern, not a one-time handoff.

All three are commissural, not direct. Within the right frontal cortex,
the four sub-regions communicate through `peer_input` (published
contributions) and through their mutual connectivity priors (in the
registry configs) — but never by reading each other's internal state. The
FrontalCortex class enforces this by construction: the only thing a
sub-region receives is its own `state`, its own `config`, the shared
`sensory_input`/`top_down`, and the `peer_input` dict of published prior
contributions.

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
      in order.
    - Must not import the registry packages directly. The sub-regions
      import their own registry areas; the FrontalCortex class imports
      the sub-regions, not the registry.
    - Must not call a sub-region more than once per tick. The
      state-threading contract depends on each sub-region being entered
      exactly once per tick, in the fixed order.
    - Must not import or reference the left hemisphere's frontal cortex
      package. Cross-midline exchange goes through
      `telencephalon/commissures/`, never through direct registry or
      compute access. The three right-hemisphere cross-midline cases
      listed above (bimanual coordination, prosody-to-speech, visual
      exploration/reading) are all cases where direct import would
      silently bypass the commissural delay that gives the model's
      behavioural predictions their teeth. If a future contributor
      finds themselves wanting to read the left's prepared motor
      programs "just for the bimanual case", that is the exact
      temptation the rule exists to prevent — the right answer is to
      put the bimanual handoff in the commissures, not to add a direct
      read.
    - Must not diverge in structure from the left hemisphere's frontal
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

This is identical on the right. The recursive-pattern rationale is
documented in the left file's full text; the mechanism is the same.

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

This is identical on the right, for the same reason (the precentral gyrus
is the surface expression of area 4 on both hemispheres). The rule is the
same: annotation can appear anywhere a named anatomical structure needs a
canonical address, including inside compute sub-regions. The
FrontalCortex class's boundary for what it calls is "the four sub-region
names in `RIGHT_FRONTAL_CORTEX_CONFIG["order"]`" — anything nested inside a
sub-region is that sub-region's concern, not this layer's.

RIGHT-HEMISPHERE CONFIG
-----------------------
The composition-level config is minimal — most of the actual config lives
in the sub-regions (which import their own registry areas' configs):

    RIGHT_FRONTAL_CORTEX_CONFIG = {
        # The four sub-regions, in the fixed causal order. Changing
        # this order changes the frontal lobe's computation
        # fundamentally, not cosmetically. IDENTICAL to the left's.
        "order": [
            "prefrontal_cortex",
            "premotor_cortex",
            "supplementary_motor_cortex",
            "primary_motor_cortex",
        ],

        # The key in each sub-region's contribution that constitutes
        # its "primary output" for the intent slice. IDENTICAL to the
        # left's — these are structural keys, not lateralised ones.
        "primary_output_key": {
            "prefrontal_cortex":          "goals",
            "premotor_cortex":            "prepared_programs",
            "supplementary_motor_cortex": "sequences",
            "primary_motor_cortex":       "motor_commands",
        },

        # The key in the primary_motor_cortex contribution that
        # constitutes the lobe's actual motor output. IDENTICAL to
        # the left's.
        "motor_output_key": "motor_commands",
    }

    RIGHT_FRONTAL_CORTEX_CONFIG is IDENTICAL to LEFT_FRONTAL_CORTEX_CONFIG
    — the composition order, the primary-output keys, and the
    motor-output key are structural and do not lateralise. Only the
    sub-regions' internal configs differ. The mirror test for this
    config is EQUALITY, not directionality: assert that LEFT == RIGHT
    here, and separately that each sub-region's config is a directional
    mirror of its left counterpart. These are two different tests for
    two different kinds of config, and conflating them would fail on
    this composition config.

EXPORTS
-------
    from . import prefrontal_cortex
    from . import premotor_cortex
    from . import supplementary_motor_cortex
    from . import primary_motor_cortex
    from .frontal_cortex import FrontalCortex    # the composition class
    from .frontal_cortex import RIGHT_FRONTAL_CORTEX_CONFIG

    The four sub-region packages are re-exported so that the frontal
    lobe's `__init__.py` and downstream consumers can reach them
    without knowing their exact import paths. The FrontalCortex class
    and its config are what this package is *for*; the sub-region
    re-exports are a convenience.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin assembly module: import the four sub-region
  packages, import the shared FrontalCortex class (from a neutral
  location shared with the left hemisphere), build
  RIGHT_FRONTAL_CORTEX_CONFIG, instantiate FrontalCortex, and expose it
  along with the four sub-region modules.
- The FrontalCortex class implements `step(sensory_input, top_down) ->
  (intent, new_states)` and nothing else. It does not expose
  per-sub-region accessors beyond the module re-exports; consumers that
  need sub-region internals reach the sub-region packages directly.
- The FrontalCortex class holds:
      - a dict of sub-region instances
      - a dict of per-sub-region configs (built from each sub-region's
        own registry-area configs, imported at construction time)
      - a dict of per-sub-region state references (opaque; threaded)
  and nothing else.
- The order of sub-region calls comes from
  `RIGHT_FRONTAL_CORTEX_CONFIG["order"]`, not from a hardcoded list.
- The `peer_input` dict passed to each sub-region contains contributions
  from the sub-regions earlier in the order, and only those. Later
  sub-regions do not appear in a peer's `peer_input`.
- Sub-region contributions are stored in `intent` by their sub-region
  name, verbatim. The parent does not merge, flatten, or rewrite them.
- State dicts are opaque to the parent.
- RIGHT_FRONTAL_CORTEX_CONFIG is STRUCTURALLY IDENTICAL to
  LEFT_FRONTAL_CORTEX_CONFIG — same order, same primary-output keys,
  same motor-output key. A test should assert this equality. The
  lateralisation lives in the sub-regions' internal configs, not here;
  the separate directional-mirror test for those sub-regions is not
  this file's concern.
"""