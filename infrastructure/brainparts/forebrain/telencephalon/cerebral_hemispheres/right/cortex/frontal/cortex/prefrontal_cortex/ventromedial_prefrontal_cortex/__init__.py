"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.prefrontal_cortex.ventromedial_prefrontal_cortex
================================================================================================================================================

The VENTROMEDIAL PREFRONTAL CORTEX (VMPFC) — right hemisphere. A compute
sub-sub-region of prefrontal, and one of the three pure-function children
of the prefrontal family.

Mirror of the left VMPFC package. VMPFC is the value-integration and
self-referential core of the prefrontal cortex. On the RIGHT, the
self-referential content is more affectively and bodily anchored
(interoceptive self-state, autonomic self-representation, affective
self-reference), and the somatic-marker integration weighs the
body-state and affective-tag inputs more heavily *through the source
config's feature weights* (the integration formula itself is
structural). The right's VMPFC is therefore the more direct analogue
of the classic somatic-marker case, and a right-VMPFC lesion produces
the canonical Phineas Gage pattern more clearly than a left lesion.

VMPFC is the area of the somatic-marker hypothesis (Damasio) and of the
Phineas Gage syndrome. The RIGHT VMPFC's damage is the classic
presentation: the patient can still describe the correct choice (the
left's verbal machinery is intact) but cannot feel the value of it (the
right's affective integration is degraded), and so makes disastrous
real-world decisions despite intact reasoning.

VMPFC IS A PURE FUNCTION (with a clarification about the somatic-marker loop)
---------------------------------------------------------------------------
Identical to the left. VMPFC carries NO persistent state across ticks.
It is a pure function of its inputs. The parent threads `{}` through
VMPFC's state slot, and VMPFC's encode() does not read or write state.

The somatic-marker division of labour is the same on both hemispheres:

    VMPFC             integrates the current tick's stimuli, body state,
                      affect, memory, and self-reference into a
                      *present* self-relevant value signal. Its half
                      of the somatic-marker mechanism is pure.

    the associative store  lives elsewhere — the insula (interoceptive
    (outside VMPFC)  memory), the amygdala (affective tagging), and the
                      striatum (value estimates). VMPFC does not store
                      the associations; it reads the currently-active
                      ones and integrates them.

On the right, the "currently-active associations" that VMPFC reads are
more affective and body-state weighted (via the higher to_amygdala and
to_insula priors in area 10's right config), so the right's integration
leans more heavily on those inputs. The integration formula is
unchanged; the inputs it receives lean affective.

REGISTRY-AREA SOURCE (single source — same structure as the left)
-----------------------------------------------------------------
VMPFC has ONE frontal-registry area source on the right, as on the
left:

    brodmann_area_10/       the "ventromedial_prefrontal_cortex" area

Its config (in `brodmann_area_10.RIGHT_CONFIG`) provides the VMPFC
feature weights: value_integration, somatic_marker,
verbal_self_reference, affective_self_reference,
emotion_regulation_reappraisal, emotion_regulation_suppression,
autobiographical_recall, social_valuation, risk_aversion, moral_judgment,
plus connectivity priors to amygdala, insula, hippocampus, PCC,
precuneus, NAcc, hypothalamus, DLPFC, basal ganglia, and commissures.

On the right, the feature weights lean toward affective_self_reference
(0.80 vs the left's 0.45) and emotion_regulation_suppression (0.70 vs
0.35); the verbal counterpart weights are correspondingly reduced
(verbal_self_reference 0.40, reappraisal 0.40). The connectivity priors
reflect the right's stronger amygdala (0.70 vs 0.55), insula (0.75 vs
0.60), and hypothalamus (0.70 vs 0.50) coupling. The two structural
features (`value_integration`, `somatic_marker`) and several others
(`autobiographical_recall`, `social_valuation`, `moral_judgment`) are
equal across hemispheres — the same "structural-heavy" profile as on
the left.

Because there is only one area source, there is NO share weight — no
`vmpfc_weight` field. VMPFC's config for composition is just
`brodmann_area_10.RIGHT_CONFIG` plus `RIGHT_VMPFC_CONFIG` (which carries
the integration weights and the renormalisation flag).

IMPORTANT CAVEAT — AREA 25 (SUBGENUAL ACC) IS NOT A VMPFC SOURCE
----------------------------------------------------------------
Same caveat as on the left, restated for the right because the
temptation to read area 25 is equally strong from this side:

    Area 25's COMPUTE lives in the RIGHT
    `cingulate/subgenual_area_25/`. On the right its `affective_setpoint`
    has a shorter time constant (8 ticks vs the left's 20) and its
    valence bias is more threat-weighted. It produces the ACC's `affect`
    scalar, which carries the unpleasantness weight across ticks.

    Area 25 is NOT a VMPFC registry-area source. Its contribution to
    VMPFC is a SIGNAL, not a config read. Two documented pathways:

        pathway 1 (default)    top_down["cingulate_affect"] — the
                               ACC's affect channel, via the salience
                               slice. VMPFC reads it as an affective
                               bias on its own integration. Same
                               mechanism by which VMPFC reads
                               top_down["cingulate_control"].

        pathway 2 (optional)   a connectivity prior on VMPFC's area 10
                               config (e.g. `to_subgenual_area_25`).
                               Anatomical coupling, without making
                               VMPFC's computation depend on the
                               cingulate's state. NOT currently added
                               to area 10's RIGHT_CONFIG; documented
                               as the future mechanism if an experiment
                               needs it.

    What VMPFC must NOT do is read area 25's config or state directly,
    or import `cingulate/subgenual_area_25/`. That would couple
    VMPFC's pure function to the cingulate's stateful compute — a
    layering violation, and the exact kind of cross-tree read that
    every earlier caveat in this project has been preventing.

THE COMPOSITION — single-source, the trivial N=1 case
-----------------------------------------------------
Same as the left: single source (area 10), no blend, every feature
passed through from the source's config-weighted extraction. The
overlap-and-specific rule's N=1 degenerate case. If a future change
adds a second source, the rule would apply at that point — documented
in the extension note in the programming contract.

THE SOMATIC-MARKER INTEGRATION (the VMPFC-specific operational pattern)
-----------------------------------------------------------------------
Same formula as the left, with the right's input leans:

    1. Read the value sources:
           stimulus_value       from OFC's contribution (via peer_input)
           body_state           from top_down["insular_state"]
           affective_tag        from top_down["amygdala_affect"]
           self_context         from VMPFC's own feature extraction
                                (on the right, affective_self_reference
                                is the dominant self-context channel)
           autobiographical_cue from top_down["hippocampal_recall"]
           acc_affect           from top_down["cingulate_affect"]
                                (may be None)

    2. Integrate per `somatic_marker_weights` (STRUCTURAL — the same
       weights as on the left). On the right, the inputs to those
       weights are more affective because the source config's feature
       weights are affective; the weights themselves are identical.

    3. Bias:
           somatic_marker_bias = integrated_value - stimulus_value

    4. Emit integrated_value, somatic_marker_bias, and the per-feature
       vector.

On the right, the somatic_marker_bias is the "something feels wrong"
signal that reaches downstream selection *through* the right VMPFC's
stronger affective coupling. In a right-VMPFC lesion, the bias is
degraded, and downstream selection proceeds without the affective
warning — the classic Phineas Gage pattern.

THE DOUBLE DISSOCIATION (reversed on the right)
-----------------------------------------------
The VMPFC pair's lateralisation gives the classic double dissociation.
On the right, the dissociation is the canonical Phineas Gage pattern:

    Right VMPFC lesion:   affective_self_reference and
                          emotion_regulation_suppression are
                          degraded (per area 10's RIGHT_CONFIG);
                          verbal_self_reference and reappraisal
                          are spared. The patient can explain but
                          cannot feel. The somatic_marker_bias is
                          degraded (the affective and body-state
                          inputs are damaged), while the verbal
                          narrative is preserved. This is the
                          classic Damasio presentation.

    Left VMPFC lesion:    verbal_self_reference and reappraisal
                          are degraded; affective_self_reference
                          and suppression are spared. The patient
                          can feel but cannot explain. The
                          somatic_marker_bias is present (the
                          affective inputs are intact), but the
                          verbal narrative around it is impaired.

The right-sided presentation is the more studied one in the
literature, and the model should reach it more clearly because the
right's integration leans more heavily on the damaged inputs (the
affective ones) — the bias degradation is more severe on the right
for the same nominal lesion severity.

FEATURE EXTRACTION (the VMPFC's inputs)
---------------------------------------
Same sources as the left; extraction weights affective and bodily
content higher on the right:

    From sensory_input:
        self_relevant_cues    — on the right, more strongly weighted
                                for affective/bodily content
                                (interoceptive state, autonomic cues)
                                than for verbal self-description
        social_content        — social/moral content; on the right,
                                weighted toward the affective
                                (empathic) dimension rather than
                                the verbally-mediated one

    From top_down:
        insular_state         — interoceptive/body state; stronger
                                input on the right (higher to_insula
                                prior)
        amygdala_affect       — current affective tagging; stronger
                                on the right (higher to_amygdala
                                prior)
        hippocampal_recall    — episodic retrieval
        cingulate_affect      — ACC's affect channel (may be None)
        basal_ganglia_current_value_estimate
                              — striatum's stored value
        cingulate_control     — ACC's control_demand
        basal_forebrain_gain  — attention/arousal

    From peer_input:
        (VMPFC is called fourth in prefrontal's order.)
        peer_input["orbitofrontal_cortex"]           — stimulus value
        peer_input["dorsomedial_prefrontal_cortex"]  — current goal
        peer_input["dorsolateral_prefrontal_cortex"] — WM contents

    The extraction rules are documented in the VMPFC class.

CONTRIBUTION SHAPE
------------------
    contribution = {
        # The ten VMPFC features (passed through from area 10)
        "value_integration":             <scalar>,
        "somatic_marker":                <scalar>,
        "verbal_self_reference":         <scalar>,
        "affective_self_reference":      <scalar>,
        "emotion_regulation_reappraisal":<scalar>,
        "emotion_regulation_suppression":<scalar>,
        "autobiographical_recall":       <scalar>,
        "social_valuation":              <scalar>,
        "risk_aversion":                 <scalar>,
        "moral_judgment":                <scalar>,

        # Operational output
        "integrated_value":              <scalar>,
        "somatic_marker_bias":           <scalar>,
    }

The schema is identical to the left's. The right's contents are more
affective (affective_self_reference higher, risk_aversion higher,
verbal_self_reference lower); the schema is unchanged.

On the right, `risk_aversion` is at 0.75 (the left's is 0.55) — the
largest single-feature lateralisation in the file — reflecting the
right's more threat-weighted risk assessment. The
`somatic_marker_bias` therefore carries a stronger "avoid this"
component on the right; this is the config-level expression of the
right's role in generating the affective warning that the left's
selection may or may not heed.

RIGHT-SPECIFIC BIAS
------------------
Same class as the left VMPFC; the RIGHT config changes the weights
(via area 10's config):

    affective_self_reference      higher (0.80)
    verbal_self_reference         lower (0.40)
    emotion_regulation_suppression higher (0.70)
    emotion_regulation_reappraisal lower (0.40)
    risk_aversion                 higher (0.75)
    to_amygdala                   higher (0.70)
    to_insula                     higher (0.75)
    to_hypothalamus               higher (0.70)
    to_commissures                higher (0.55)

The class, the integration formula, the bias computation, the feature
extraction, and the somatic_marker_weights are IDENTICAL across
hemispheres. Only area 10's feature values and connectivity priors
differ. LEFT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left VMPFC. Cross-midline VMPFC exchange is
the "feels but can't explain" / "explains but can't feel" pair. On the
right, the cases emphasise the right's role as the AFFECTIVE SENDER —
its integrated value and somatic_marker_bias are what the left's
narrative machinery has to reconcile with:

    - Value-to-narrative (the right's primary cross-midline role).
      The right's VMPFC produces an affectively-weighted integrated
      value (a "this feels wrong" signal); the left's produces a
      verbally-mediated integrated value (a "this fits my story"
      signal). For a self-relevant outcome, the two can differ — a
      scene that fits the left's narrative but triggers the right's
      unease. The divergence is the signal, and the exchange is
      commissural. The right's higher to_commissures prior (0.55 vs
      the left's 0.45) reflects that the right's affective value has
      to reach the left's narrative machinery for expression ("I
      felt it was wrong but couldn't say why") more often than the
      reverse.

    - Autonomic handoff. The right's stronger to_hypothalamus prior
      (0.70) means the right's affective integration more directly
      drives autonomic responses (the gut feeling, the racing
      heart). When the left's narrative machinery needs to describe
      that state, the autonomic signal has to reach the left via the
      commissures. The right's stronger autonomic coupling is
      documented in area 10's RIGHT_CONFIG, not as a change to the
      integration formula.

    - Moral judgment split. The right's affectively-mediated moral
      intuition and the left's verbally-mediated moral reasoning
      often disagree; the disagreement is the classic dual-process
      moral psychology pattern. The right's contribution to the
      disagreement is its affective integration; the left's is its
      verbal reasoning. The commissures surface the composite.

All three are commissural. The "value-to-narrative" case is the
canonical VMPFC cross-midline case from the right's side, and its
behavioural signature ("I want it, but I feel uneasy") is the
composite of the two hemispheres' integrated values, with the right
on the sending side of the uneasy component.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. VMPFC is pure; the somatic-
      marker associations live in the insula, amygdala, and striatum
      that VMPFC reads from.
    - Must not read area 10's config directly — it is passed in via
      `config`.
    - Must not add a `vmpfc_weight` field. VMPFC has a single
      registry-area source.
    - Must not read area 25's config or state. Area 25 is a cingulate
      compute sub-module. The ACC's affect reaches VMPFC via
      top_down["cingulate_affect"], never via a direct read. On the
      right, the temptation is particularly strong because the right
      area 25's affect channel has faster setpoint dynamics (shorter
      time constant) and would be an interesting signal — but the
      correct pathway is still the top_down signal, not a direct
      registry read.
    - Must not read area 9 or area 8's medial extensions. Anatomical
      adjacency, not configurable input.
    - Must not implement the associative store.
    - Must not implement the striatum's value update.
    - Must not change the somatic_marker_weights on the right. Those
      weights are STRUCTURAL. The right's "more affective" character
      lives in area 10's directionally-mirrored feature weights, not
      in the integration weights. A test that assumed "right VMPFC
      weighs body state more heavily at the integration level" would
      fail; the integration weights are equal, and the lateralised
      character comes from the source config's feature values.
    - Must not conflate `affective_self_reference`'s higher weight on
      the right with a change to the somatic_marker_weights'
      `self_relevance` coefficient. The `self_relevance` coefficient
      (0.15) is structural; the *value* of `self_context` that feeds
      it is more affective on the right because area 10's
      affective_self_reference feature is weighted higher. Two
      different things.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not import `brodmann_areas/` directly.
    - Must not import or reference the left VMPFC. Cross-midline
      exchange goes through `telencephalon/commissures/`. The
      "value-to-narrative" case is the prime example: direct import
      would silently merge the two hemispheres' integrated values and
      make the "explains but can't feel" Phineas Gage pattern
      untestable.
    - Must not diverge in structure from the left VMPFC — same class,
      same encode() signature, no state (both pure functions), same
      single-source composition, same somatic-marker integration, same
      integration weights. Only area 10's feature values and
      connectivity priors differ.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_VMPFC_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_10",

        # Somatic-marker integration weights (STRUCTURAL — identical
        # to the left's).
        "somatic_marker_weights": {
            "stimulus_value":    0.30,
            "body_state":        0.20,
            "affective_tag":     0.20,
            "self_relevance":    0.15,
            "autobiographical":  0.10,
            "acc_affect":        0.05,
        },

        # ACC affect reading (STRUCTURAL — identical to the left's).
        "acc_affect_renormalise_when_absent": True,
    }

    Area 10's config (brodmann_area_10.RIGHT_CONFIG) is supplied by
    PrefrontalCortex at construction. It provides the ten feature
    weights and the connectivity priors, with the right's affective
    lean.

    RIGHT_VMPFC_CONFIG is IDENTICAL to LEFT_VMPFC_CONFIG except that
    it names brodmann_area_10.RIGHT_CONFIG. The somatic_marker_weights
    and the renormalisation flag are STRUCTURAL — equal across
    hemispheres.

    Two separate tests are needed:
        1. RIGHT_VMPFC_CONFIG == LEFT_VMPFC_CONFIG on
           somatic_marker_weights and renormalisation (structural
           equality).
        2. brodmann_area_10.RIGHT_CONFIG is a directional mirror of
           LEFT_CONFIG (feature and connectivity values mirror).
    A test that checked somatic_marker_weights for directionality
    would fail spuriously.

EXPORTS
-------
    from .ventromedial_prefrontal_cortex import VentromedialPrefrontalCortex
    from .ventromedial_prefrontal_cortex import RIGHT_VMPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. No dlpfc_weight-style precondition:
    VMPFC's single source means there is no share to verify.

    NOTE: This package's construction does NOT depend on the pending
    area-9 dlpfc_weight amendment (that affects DLPFC only). VMPFC-
    right can be instantiated as soon as the class is implemented,
    using area 10's RIGHT_CONFIG as-is.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  VentromedialPrefrontalCortex class, import brodmann_area_10's
  RIGHT_CONFIG, build RIGHT_VMPFC_CONFIG, instantiate the class,
  expose the class and the config.
- The class implements the sub-sub-region encode() signature. VMPFC
  is PURE — state input is always {}, output state is always {}.
- The single-source composition is trivial (pass through every
  feature from area 10's config-weighted extraction). No
  `_blend_*` function is needed; if a second source is ever added,
  the overlap-and-specific rule applies at that point.
- The somatic-marker integration is a documented, unit-testable
  function (`_integrate_value(sources, weights) -> integrated_value`).
- The bias computation is a documented, unit-testable function
  (`_somatic_marker_bias(integrated_value, stimulus_value)`).
- Feature extraction is a documented, unit-testable function. On the
  right, extraction weights affective/bodily content higher than
  verbal content; the extraction function reads this from the
  config, not from hardcoded weights.
- The class does not import or access any peer sub-sub-region's
  state.
- The class does not read area 25, area 9, or area 8's config. Any
  ACC affect reaches VMPFC via top_down["cingulate_affect"].
- The class does not implement the somatic-marker associative store.
- RIGHT_VMPFC_CONFIG is structurally identical to LEFT_VMPFC_CONFIG
  except for the area-config source reference. Integration weights
  and renormalisation are STRUCTURAL.
- If a future change wants to add a second VMPFC source, the
  composition becomes N=2 and the overlap-and-specific rule applies.
- Must not import or reference the left VMPFC. Cross-midline exchange
  goes through `telencephalon/commissures/`.

PREFrontal family status (both hemispheres)
-------------------------------------------
With this file, four of the five prefrontal sub-sub-regions are
complete on both hemispheres, and the fifth (DLPFC-right) is
structurally documented but blocked by the pending area-9
dlpfc_weight amendment:

    prefrontal_cortex/__init__.py                L ✅  R ✅
    dorsomedial_prefrontal_cortex/               L ✅  R ✅
    dorsolateral_prefrontal_cortex/              L ✅  R ✅
    orbitofrontal_cortex/                        L ✅  R ✅
    ventromedial_prefrontal_cortex/              L ✅  R ✅
    ventrolateral_prefrontal_cortex/             L ✅  R ✅

Once the area-9 amendment is applied to both hemispheres, the entire
prefrontal family is complete on both sides.
"""