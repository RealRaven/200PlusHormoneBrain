"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.prefrontal_cortex
================================================================================================================

The PREFRONTAL CORTEX — left hemisphere. FAMILY sub-region of the frontal
compute layer.

Prefrontal is the only FAMILY sub-region among the frontal cortex's four
(prefrontal, premotor, supplementary motor, primary motor). It contains
five sub-sub-regions, and its role in the frontal cortex's compute layer
is to orchestrate them — using the SAME pattern the FrontalCortex class
uses to orchestrate its four sub-regions. Recursion, not duplication.

If you are looking for the FrontalCortex class's composition contract (the
sub-region encode() signature, the growing peer_input mechanism, the
intent slice schema), that is documented at the parent level:
`.../frontal/cortex/__init__.py`. This file does not repeat it — it
documents *how prefrontal applies that contract to its five children*.

THE FIVE SUB-SUB-REGIONS
------------------------
    dorsomedial_prefrontal_cortex (DMPFC)
        Owns: goal_stack (persistent state).
        Computes: the active goal, pending goals, self-referential and
        social-evaluative content. The top of the goal stack is this
        tick's target.
        Registry areas: 8 (medial extension), 10 (medial portion),
        32 (cingulate — via cross-reference, NOT here), plus DMPFC
        coupling with PCC. (See the DMPFC package for its own precise
        area set.)

    dorsolateral_prefrontal_cortex (DLPFC)
        Owns: working_memory (persistent state).
        Computes: working-memory contents (verbal on the left, spatial
        on the right), planning, cognitive control, rule representation,
        task-set maintenance.
        Registry areas: 9, 46 (DLPFC) — the DLPFC pair.

    orbitofrontal_cortex (OFC)
        Owns: no persistent state (pure function).
        Computes: stimulus-outcome learning, reversal learning, outcome
        evaluation.
        Registry areas: 11, 12 (OFC) plus area 47's OFC block.

    ventromedial_prefrontal_cortex (VMPFC)
        Owns: no persistent state (pure function).
        Computes: integrated value, somatic-marker tagging, self-
        referential value.
        Registry areas: 10 (VMPFC). NOTE: area 25 (the subgenual ACC) is
        a frontal-registry entry that POINTS to cingulate compute; it is
        NOT a VMPFC input area. The VMPFC sub-sub-region reads area 10
        only. The frontal-registry area-25 entry is documented as a
        cross-lobe pointer and has no config to read.

    ventrolateral_prefrontal_cortex (VLPFC)
        Owns: no persistent state (pure function).
        Computes: semantic retrieval, selection, language control
        (Broca's area's articulatory and lexical roles), and area 47's
        VLPFC block's value-guided semantic retrieval.
        Registry areas: 44, 45 (Broca's area) plus area 47's VLPFC block.

Two of the five own persistent state (DMPFC's goal_stack, DLPFC's
working_memory); the other three are pure functions of their inputs. This
is a mixed-state family — the same mixed-state pattern as the ACC, one
level down. Prefrontal's encode() must honour each child's state contract
individually (some stateful, some pure) while composing them uniformly.

THE COMPOSITION ORDER (left and right identical)
------------------------------------------------
The five sub-sub-regions are called exactly once per tick, in this order:

    1. dorsomedial_prefrontal_cortex   (goals)
    2. dorsolateral_prefrontal_cortex  (working memory)
    3. orbitofrontal_cortex            (stimulus value)
    4. ventromedial_prefrontal_cortex  (integrated value + self)
    5. ventrolateral_prefrontal_cortex (selection)

The order is *causal*:
    - Goals come first because they set the task for the tick. Nothing
      downstream makes sense without knowing what the current goal is.
    - Working memory comes second because it holds the content relevant
      to the goal, which value evaluation will need to consider.
    - Stimulus value (OFC) comes third because it evaluates what's at
      stake in the current context, given the goal and held content.
    - Integrated value (VMPFC) comes fourth because it combines OFC's
      stimulus value with self-relevance and body state — a
      *higher-order* evaluation of what the world is worth to *me*,
      which requires OFC's first-order value as input.
    - Selection (VLPFC) comes last because it needs the full picture:
      the goal (DMPFC), the working content (DLPFC), the stimulus
      value (OFC), and the integrated value (VMPFC) are all inputs to
      what gets selected.

A child that receives an empty upstream contribution still runs — the
pipeline degrades gracefully rather than short-circuiting. This is the
same rule as the parent's.

THE SUB-SUB-REGION encode() SIGNATURE
-------------------------------------
Identical to the parent's children signature. Each sub-sub-region exposes:

    encode(
        sensory_input,      # pass-through from the parent
        top_down,           # pass-through from the parent
        peer_input,         # growing dict: sub_sub_region_name ->
                            # contribution, for all sub-sub-regions that
                            # have already run THIS TICK (empty for
                            # DMPFC)
        state,              # this sub-sub-region's own state dict
                            # (may be {} for pure-function sub-sub-
                            # regions)
        config,             # this sub-sub-region's config, built from
                            # its own registry areas' configs
    ) -> (contribution, new_state)

The pattern is identical to the parent's, applied one level down. A
sub-sub-region's `state` is `{}` if the sub-sub-region is a pure
function (OFC, VMPFC, VLPFC) and a non-empty dict if stateful (DMPFC's
goal_stack, DLPFC's working_memory). The parent (PrefrontalCortex) does
not care which sub-sub-regions are stateful — it threads `{}` through
pure-function sub-sub-regions exactly as it threads non-empty state
through the stateful ones.

THE COMPOSITE CONTRIBUTION
--------------------------
Prefrontal's encode() returns a contribution of the form:

    contribution = {
        "dorsomedial_prefrontal_cortex":  <DMPFC contribution>,
        "dorsolateral_prefrontal_cortex": <DLPFC contribution>,
        "orbitofrontal_cortex":           <OFC contribution>,
        "ventromedial_prefrontal_cortex": <VMPFC contribution>,
        "ventrolateral_prefrontal_cortex":<VLPFC contribution>,

        # Primary-output alias, per the parent's config
        # (prefrontal_cortex's primary_output_key is "goals").
        "goals":                          <DMPFC contribution's goals>,
    }

The five sub-sub-region keys hold each child's contribution VERBATIM —
prefrontal does not merge, flatten, or rewrite them. The "goals" key is
the ONE convenience alias: it copies DMPFC's "goals" field to the top
level of prefrontal's contribution, so that the FrontalCortex class can
read `contribution["goals"]` without knowing prefrontal's internal
structure. This is what makes the parent's `primary_output_key` map work.

Everything else about the composite contribution is per-child, documented
in each child's own package. Consumers that need a specific sub-sub-
region's output read `contribution[<sub_sub_region_name>][<field>]`;
consumers that need prefrontal's headline output read
`contribution["goals"]`.

Prefrontal's encode() does not add its own computation on top of the five
children's. It orchestrates them and returns their contributions plus the
alias. The pattern is: prefrontal is a *composite*, not a *merge* — it
composes its five children, it does not add a sixth contribution of its
own. This is identical to how the FrontalCortex class relates to its four
sub-regions: it orchestrates, it does not compute.

STATE THREADING AT THIS LEVEL
-----------------------------
Prefrontal's encode() receives one state dict from the parent
(FrontalCortex). Internally, that dict has five per-child entries:

    state = {
        "dorsomedial_prefrontal_cortex":  {"goal_stack": ...},
        "dorsolateral_prefrontal_cortex": {"working_memory": ...},
        "orbitofrontal_cortex":           {},   # pure function
        "ventromedial_prefrontal_cortex": {},   # pure function
        "ventrolateral_prefrontal_cortex":{},   # pure function
    }

Prefrontal's encode() calls each child in the order above, threading that
child's sub-dict, then stores the child's returned new_state back into
the same shape:

    new_child_states = {}
    peer_input = {}
    for name in order:
        contribution, new_state = children[name].encode(
            sensory_input, top_down, peer_input,
            state[name], child_configs[name],
        )
        peer_input[name] = contribution
        new_child_states[name] = new_state
    new_state = new_child_states
    contribution = {**{name: peer_input[name] for name in order},
                    "goals": peer_input["dorsomedial_prefrontal_cortex"]["goals"]}

The parent (FrontalCortex) sees none of this — from its perspective,
prefrontal is a black box with a state dict and a contribution. But
the pattern inside prefrontal is the same one the parent applies to its
four children, one level down. A reader who understands the parent
understands this layer, and vice versa.

LEFT-SPECIFIC BIAS
------------------
Same code as the right prefrontal; the LEFT configs (inside each of the
five sub-sub-regions, via their registry areas) change the weights. At
this composition layer, the lateralisation shows up only in what each
sub-sub-region's config contains:

    DMPFC    left-weighted on verbal/social mentalizing; right-weighted
             on affective/social self-reference
    DLPFC    left-weighted on verbal WM and verbal rules (via areas 9,
             46); right-weighted on spatial WM and spatial rules
    OFC      left-weighted on positive/approach value and verbal
             reward cues; right-weighted on negative/avoidance value
             and direct reward cues
    VMPFC    left-weighted on verbal self-reference and reappraisal;
             right-weighted on affective self-reference and suppression
    VLPFC    left-weighted on language control and verbal fluency
             (Broca's area); right-weighted on scene-semantic control

The composition order, the encode() signature, the composite contribution
shape, the state-threading contract, and the "goals" alias are IDENTICAL
across hemispheres. Only the config values inside the sub-sub-regions
differ. RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right hemisphere's prefrontal cortex. Within the
left prefrontal, the five sub-sub-regions communicate through `peer_input`
(published contributions) and through their mutual connectivity priors
(in the registry configs) — but never by reading each other's internal
state.

The classic cross-midline case at this level is prefrontal's contribution
to language prosody. The right's prefrontal — specifically VLPFC's
Broca's-area prosody role and DMPFC's affective self-reference — carries
the affective-prosodic content of an utterance, while the left's
prefrontal carries the lexical and articulatory content. The two are
combined by the commissures, not by direct access. A direct import here
would silently merge the left's lexical content with the right's prosodic
content and make the "flat speech with intact content" failure mode
untestable.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define the five sub-sub-regions' computations. Each is
      defined in its own package; this file defines only their
      composition.
    - Must not hold persistent state itself. State lives in DMPFC
      (goal_stack) and DLPFC (working_memory); the PrefrontalCortex
      class holds opaque references and threads them.
    - Must not add a sixth contribution of its own. Prefrontal is a
      composite, not a merge — its contribution is the five children's
      contributions verbatim, plus the "goals" alias. A sixth
      contribution would mean prefrontal is doing its own computation,
      which it isn't.
    - Must not merge, flatten, or rewrite the contributions the five
      sub-sub-regions produce. Each is stored under its own name.
    - Must not short-circuit the pipeline when an upstream sub-sub-
      region returns an empty contribution. Every child runs, every
      tick, in order.
    - Must not call a sub-sub-region more than once per tick. The
      state-threading contract depends on each child being entered
      exactly once per tick.
    - Must not import area 25's cingulate compute. The frontal-registry
      area-25 entry is a cross-lobe POINTER — it documents the anatomy
      and points at the cingulate package, but does not participate in
      VMPFC's computation. VMPFC reads area 10 only. If a future
      experiment wants area 25's affect channel to influence VMPFC's
      value integration, that is a documented *connectivity prior* in
      VMPFC's config (a signal from the cingulate), not a direct
      registry-area read inside this package. The two are different
      mechanisms and must not be conflated.
    - Must not import or reference the right hemisphere's prefrontal
      cortex. Cross-midline exchange goes through
      `telencephalon/commissures/`, never through direct access.
    - Must not diverge in structure from the right hemisphere's
      prefrontal cortex package — same five sub-sub-regions, same
      order, same encode() signature, same composite contribution
      shape (including the "goals" alias), same state-threading
      contract. Only the config values inside the sub-sub-regions
      differ.

LEFT-HEMISPHERE CONFIG
----------------------
The composition-level config is minimal — the actual config lives inside
the five sub-sub-regions (which import their own registry areas'
configs):

    LEFT_PREFRONTAL_CORTEX_CONFIG = {
        # The five sub-sub-regions, in the fixed causal order. Changing
        # this order changes prefrontal's computation fundamentally,
        # not cosmetically.
        "order": [
            "dorsomedial_prefrontal_cortex",
            "dorsolateral_prefrontal_cortex",
            "orbitofrontal_cortex",
            "ventromedial_prefrontal_cortex",
            "ventrolateral_prefrontal_cortex",
        ],

        # The "primary output" alias key that prefrontal exposes at
        # its top level. Per the parent's primary_output_key map,
        # prefrontal's primary output is "goals", sourced from DMPFC.
        "primary_output_key": "goals",
        "primary_output_source": "dorsomedial_prefrontal_cortex",
    }

    RIGHT_PREFRONTAL_CORTEX_CONFIG is IDENTICAL — the composition order,
    the primary-output key, and its source are structural and do not
    lateralise. Only the sub-sub-regions' internal configs differ.

EXPORTS
-------
    from . import dorsomedial_prefrontal_cortex
    from . import dorsolateral_prefrontal_cortex
    from . import orbitofrontal_cortex
    from . import ventromedial_prefrontal_cortex
    from . import ventrolateral_prefrontal_cortex
    from .prefrontal_cortex import PrefrontalCortex    # composition class
    from .prefrontal_cortex import LEFT_PREFRONTAL_CORTEX_CONFIG

    The five sub-sub-region packages are re-exported so that the
    FrontalCortex class and downstream consumers can reach them
    without knowing their exact import paths. The PrefrontalCortex
    class and its config are what this package is *for*; the sub-sub-
    region re-exports are a convenience.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin assembly module: import the five sub-sub-
  region packages, import the shared PrefrontalCortex class (from a
  neutral location shared with the right hemisphere), build
  LEFT_PREFRONTAL_CORTEX_CONFIG, instantiate PrefrontalCortex, and
  expose it along with the five sub-sub-region modules.
- The PrefrontalCortex class implements the same `encode(sensory_input,
  top_down, peer_input, state, config) -> (contribution, new_state)`
  signature that the FrontalCortex class expects of its children.
  Signature identity is what makes prefrontal substitutable as a child
  of FrontalCortex despite being a family.
- The PrefrontalCortex class holds:
      - a dict of sub-sub-region instances
      - a dict of per-sub-sub-region configs
      - nothing else. It is stateless across ticks beyond the state
        dict it receives and returns.
- The order of sub-sub-region calls comes from
  `LEFT_PREFRONTAL_CORTEX_CONFIG["order"]`, not from a hardcoded list.
  A reordering experiment is a config change, not a code change.
- The `peer_input` dict passed to each sub-sub-region contains
  contributions from the sub-sub-regions earlier in the order, and only
  those. Later children do not appear in an earlier child's peer_input.
- Sub-sub-region contributions are stored in the composite contribution
  under their sub-sub-region name, verbatim. Prefrontal does not merge,
  flatten, or rewrite them.
- The "goals" alias at the top of the composite contribution mirrors
  DMPFC's "goals" field. It is a reference, not a copy with modified
  contents — if DMPFC's goals change, the alias reflects the change on
  the next tick. The alias exists so that the FrontalCortex class can
  read contribution["goals"] without knowing prefrontal's internal
  structure.
- State dicts for the pure-function children (OFC, VMPFC, VLPFC) are
  `{}` and are threaded uniformly. The PrefrontalCortex class does not
  special-case stateful vs pure-function children; it threads whatever
  each child returned last tick.
- LEFT_PREFRONTAL_CORTEX_CONFIG is STRUCTURALLY IDENTICAL to
  RIGHT_PREFRONTAL_CORTEX_CONFIG — same order, same primary-output
  key and source. A test should assert this equality. The
  lateralisation lives in the five sub-sub-regions' internal configs,
  not here.
- If a future change wants to add a sixth sub-sub-region (e.g. to
  model a specific prefrontal function that doesn't fit DMPFC, DLPFC,
  OFC, VMPFC, or VLPFC), the composition config gains a sixth entry
  and the order gains a position. This is a substantive modeling
  decision, not a config tweak — it changes prefrontal's computation.
  The file is structured so that it's a clean extension (the pattern
  generalises), but the decision should be documented.
"""