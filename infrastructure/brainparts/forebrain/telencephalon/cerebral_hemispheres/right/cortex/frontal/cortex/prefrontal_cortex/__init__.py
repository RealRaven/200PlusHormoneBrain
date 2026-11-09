"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.prefrontal_cortex
=================================================================================================================

The PREFRONTAL CORTEX — right hemisphere. FAMILY sub-region of the frontal
compute layer.

Mirror of the left prefrontal cortex package. Prefrontal is the only FAMILY
sub-region among the frontal cortex's four (prefrontal, premotor,
supplementary motor, primary motor). It contains five sub-sub-regions, and
its role in the frontal cortex's compute layer is to orchestrate them —
using the SAME pattern the FrontalCortex class uses to orchestrate its four
sub-regions. Recursion, not duplication.

If you are looking for the FrontalCortex class's composition contract (the
sub-region encode() signature, the growing peer_input mechanism, the
intent slice schema), that is documented at the parent level:
`.../frontal/cortex/__init__.py`. This file does not repeat it — it
documents *how prefrontal applies that contract to its five children*.

THE FIVE SUB-SUB-REGIONS
------------------------
Identical set to the left, with identical division of state:

    dorsomedial_prefrontal_cortex (DMPFC)
        Owns: goal_stack (persistent state).
        Computes: the active goal, pending goals, self-referential and
        social-evaluative content. On the right, goals lean toward
        spatially-situated and threat-relevant content.
        Registry areas: 8 (medial extension), 10 (medial portion).

    dorsolateral_prefrontal_cortex (DLPFC)
        Owns: working_memory (persistent state).
        Computes: working-memory contents, planning, cognitive control,
        rule representation, task-set maintenance. On the right, WM
        content is spatial (visuospatial sketchpad), rules are spatial-
        situational.
        Registry areas: 9, 46 (DLPFC).

    orbitofrontal_cortex (OFC)
        Owns: no persistent state (pure function).
        Computes: stimulus-outcome learning, reversal learning, outcome
        evaluation. On the right, outcomes are more directly visceral
        and threat-weighted (via area 12's stronger amygdala/insula
        coupling).
        Registry areas: 11, 12 (OFC) plus area 47's OFC block.

    ventromedial_prefrontal_cortex (VMPFC)
        Owns: no persistent state (pure function).
        Computes: integrated value, somatic-marker tagging, self-
        referential value. On the right, valuation is more affectively
        and viscerally mediated, valence bias leans toward negative/
        avoidance.
        Registry areas: 10 (VMPFC). NOTE: area 25 (the subgenual ACC)
        is a frontal-registry entry that POINTS to cingulate compute;
        it is NOT a VMPFC input area. The VMPFC sub-sub-region reads
        area 10 only.

    ventrolateral_prefrontal_cortex (VLPFC)
        Owns: no persistent state (pure function).
        Computes: semantic retrieval, selection, language control
        (Broca's area's prosody role + area 47's VLPFC block's scene-
        semantic control). On the right, semantic content is scene/
        situational rather than verbal.
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

The order is *causal*: goals set the task; working memory holds the
content relevant to the goal; OFC evaluates what's at stake in the current
context; VMPFC integrates stimulus value with self-relevance and body
state; VLPFC selects based on the full picture. The full rationale is
documented in the left file's complete text; the order itself is
structural and does not lateralise.

A child that receives an empty upstream contribution still runs — the
pipeline degrades gracefully rather than short-circuiting.

THE SUB-SUB-REGION encode() SIGNATURE
-------------------------------------
Identical to the parent's children signature:

    encode(
        sensory_input,      # pass-through from the parent
        top_down,           # pass-through from the parent
        peer_input,         # growing dict: sub_sub_region_name ->
                            # contribution, for all sub-sub-regions that
                            # have already run THIS TICK (empty for
                            # DMPFC)
        state,              # this sub-sub-region's own state dict
                            # ({} for pure-function sub-sub-regions)
        config,             # this sub-sub-region's config
    ) -> (contribution, new_state)

The pattern is identical to the parent's, applied one level down. A
sub-sub-region's `state` is `{}` if the sub-sub-region is a pure
function (OFC, VMPFC, VLPFC) and a non-empty dict if stateful (DMPFC's
goal_stack, DLPFC's working_memory). The parent threads `{}` through
pure-function sub-sub-regions exactly as it threads non-empty state
through the stateful ones. The signature and the state contract are
identical on the right.

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
level of prefrontal's contribution. This is what makes the parent's
`primary_output_key` map work. Identical on the right.

Everything else about the composite contribution is per-child, documented
in each child's own package. The schema is identical across hemispheres;
only the contents of the child contributions differ (spatial vs verbal,
scene vs semantic, threat vs positive, etc.).

STATE THREADING AT THIS LEVEL
-----------------------------
Prefrontal's encode() receives one state dict from the parent
(FrontalCortex), with five per-child entries:

    state = {
        "dorsomedial_prefrontal_cortex":  {"goal_stack": ...},
        "dorsolateral_prefrontal_cortex": {"working_memory": ...},
        "orbitofrontal_cortex":           {},   # pure function
        "ventromedial_prefrontal_cortex": {},   # pure function
        "ventrolateral_prefrontal_cortex":{},   # pure function
    }

The child states are threaded in the same way as on the left: each child
is called with its own sub-dict, its returned new_state is stored back
into the same shape, and the whole thing is returned to the parent.

The right's state *content* differs — right DLPFC's working memory holds
spatial rather than verbal content, right DMPFC's goal stack holds
threat-relevant and spatially-situated goals rather than verbal ones — but
the state *structure* and the threading contract are identical.

RIGHT-SPECIFIC BIAS
-------------------
Same code as the left prefrontal; the RIGHT configs (inside each of the
five sub-sub-regions, via their registry areas) change the weights. At
this composition layer, the lateralisation shows up only in what each
sub-sub-region's config contains:

    DMPFC    right-weighted on affective/social self-reference;
             left-weighted on verbal/social mentalizing
    DLPFC    right-weighted on spatial WM and spatial rules (via areas
             9, 46); left-weighted on verbal WM and verbal rules
    OFC      right-weighted on negative/avoidance value and direct
             reward cues; left-weighted on positive/approach value
             and verbal reward cues
    VMPFC    right-weighted on affective self-reference and autonomic
             suppression; left-weighted on verbal self-reference and
             reappraisal
    VLPFC    right-weighted on scene-semantic control; left-weighted
             on language control and verbal fluency

The composition order, the encode() signature, the composite contribution
shape, the state-threading contract, and the "goals" alias are IDENTICAL
across hemispheres. Only the config values inside the sub-sub-regions
differ. LEFT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left hemisphere's prefrontal cortex. Within the
right prefrontal, the five sub-sub-regions communicate through
`peer_input` (published contributions) and through their mutual
connectivity priors (in the registry configs) — but never by reading each
other's internal state.

The classic cross-midline cases at the right prefrontal level are:

    - Prosody-to-speech delivery. The right's VLPFC (Broca's-area
      prosody role, area 47's scene-semantic-to-affective-prosody
      conversion) computes the affective-prosodic content of an
      utterance; the left's VLPFC and primary motor compute the
      lexical and articulatory content. The prosody reaches the left's
      speech output via the commissures. A direct import would silently
      merge the two and make the flat-speech failure mode untestable.

    - Value-guided retrieval with cross-hemisphere content. A
      scene-semantic value that the right's VMPFC has evaluated may
      need verbal labels from the left's VLPFC for narrative
      expression ("I felt it was wrong but couldn't say why"). The
      exchange goes through the commissures, not direct access.

    - Affective-prosodic mentalizing. The right's DMPFC computes
      affective self-reference and social cognition; the left's DMPFC
      computes verbal mentalizing. Integrating the two for a complete
      social interpretation requires commissural handoff.

All three are commissural, not direct. The right's prefrontal must not
read the left's state directly, even "just for the prosody case" — that
is the exact temptation the rule exists to prevent.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define the five sub-sub-regions' computations. Each is
      defined in its own package; this file defines only their
      composition.
    - Must not hold persistent state itself. State lives in DMPFC
      (goal_stack) and DLPFC (working_memory); the PrefrontalCortex
      class holds opaque references and threads them.
    - Must not add a sixth contribution of its own. Prefrontal is a
      composite, not a merge.
    - Must not merge, flatten, or rewrite the contributions the five
      sub-sub-regions produce.
    - Must not short-circuit the pipeline when an upstream sub-sub-
      region returns an empty contribution.
    - Must not call a sub-sub-region more than once per tick.
    - Must not import area 25's cingulate compute. The frontal-registry
      area-25 entry is a cross-lobe POINTER; it does not participate in
      VMPFC's computation. If a future experiment wants area 25's
      affect channel to influence VMPFC's value integration, that is a
      connectivity prior in VMPFC's config (a signal from cingulate),
      not a direct registry-area read inside this package.
    - Must not import or reference the left hemisphere's prefrontal
      cortex. Cross-midline exchange goes through
      `telencephalon/commissures/`, never through direct access. The
      three right-hemisphere cross-midline cases above (prosody-to-
      speech, value-guided cross-hemisphere retrieval, affective-
      prosodic mentalizing) are all cases where direct import would
      bypass the commissural delay that gives the model its
      behavioural predictions.
    - Must not diverge in structure from the left hemisphere's
      prefrontal cortex package — same five sub-sub-regions, same
      order, same encode() signature, same composite contribution
      shape (including the "goals" alias), same state-threading
      contract. Only the config values inside the sub-sub-regions
      differ.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_PREFRONTAL_CORTEX_CONFIG = {
        # The five sub-sub-regions, in the fixed causal order.
        # IDENTICAL to the left's.
        "order": [
            "dorsomedial_prefrontal_cortex",
            "dorsolateral_prefrontal_cortex",
            "orbitofrontal_cortex",
            "ventromedial_prefrontal_cortex",
            "ventrolateral_prefrontal_cortex",
        ],

        # The "primary output" alias key that prefrontal exposes at
        # its top level. IDENTICAL to the left's.
        "primary_output_key": "goals",
        "primary_output_source": "dorsomedial_prefrontal_cortex",
    }

    RIGHT_PREFRONTAL_CORTEX_CONFIG is IDENTICAL to
    LEFT_PREFRONTAL_CORTEX_CONFIG — the composition order, the
    primary-output key, and its source are structural and do not
    lateralise. Only the sub-sub-regions' internal configs differ.
    The mirror test for this config is EQUALITY, not directionality:
    assert that LEFT == RIGHT here, and separately that each sub-sub-
    region's config is a directional mirror of its left counterpart.
    These are two different tests for two different kinds of config.

EXPORTS
-------
    from . import dorsomedial_prefrontal_cortex
    from . import dorsolateral_prefrontal_cortex
    from . import orbitofrontal_cortex
    from . import ventromedial_prefrontal_cortex
    from . import ventrolateral_prefrontal_cortex
    from .prefrontal_cortex import PrefrontalCortex    # composition class
    from .prefrontal_cortex import RIGHT_PREFRONTAL_CORTEX_CONFIG

    The five sub-sub-region packages are re-exported so that the
    FrontalCortex class and downstream consumers can reach them
    without knowing their exact import paths. The PrefrontalCortex
    class and its config are what this package is *for*; the sub-sub-
    region re-exports are a convenience.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin assembly module: import the five sub-sub-
  region packages, import the shared PrefrontalCortex class (from a
  neutral location shared with the left hemisphere), build
  RIGHT_PREFRONTAL_CORTEX_CONFIG, instantiate PrefrontalCortex, and
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
  `RIGHT_PREFRONTAL_CORTEX_CONFIG["order"]`, not from a hardcoded list.
- The `peer_input` dict passed to each sub-sub-region contains
  contributions from the sub-sub-regions earlier in the order, and only
  those.
- Sub-sub-region contributions are stored in the composite contribution
  under their sub-sub-region name, verbatim.
- The "goals" alias at the top of the composite contribution mirrors
  DMPFC's "goals" field. It is a reference, not a copy with modified
  contents.
- State dicts for the pure-function children (OFC, VMPFC, VLPFC) are
  `{}` and are threaded uniformly. The PrefrontalCortex class does not
  special-case stateful vs pure-function children.
- RIGHT_PREFRONTAL_CORTEX_CONFIG is STRUCTURALLY IDENTICAL to
  LEFT_PREFRONTAL_CORTEX_CONFIG — same order, same primary-output
  key and source. A test should assert this equality. The
  lateralisation lives in the five sub-sub-regions' internal configs,
  not here.
- Must not import or reference the left hemisphere's prefrontal cortex
  package. Cross-midline exchange goes through
  `telencephalon/commissures/`.
"""