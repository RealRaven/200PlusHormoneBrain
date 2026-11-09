"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.prefrontal_cortex.orbitofrontal_cortex
======================================================================================================================================

The ORBITOFRONTAL CORTEX (OFC) — right hemisphere. A compute sub-sub-region
of prefrontal, and one of the three pure-function children of the prefrontal
family.

Mirror of the left OFC package. OFC is the stimulus-outcome learner: it
evaluates what stimuli are worth, computes prediction errors when actual
outcomes diverge from expected ones, and drives the reversal-learning loop
that keeps the value system adapting to changing contingencies. On the
RIGHT, the outcomes evaluated are more directly visceral, sensory, and
threat-relevant — the right's OFC evaluates "what does this do to me?"
where the left's evaluates "what does this mean?". The mechanics of the
loop are the same; the content and its valence colour are mirrored.

OFC IS A PURE FUNCTION (with a clarification about reversal learning)
---------------------------------------------------------------------
Identical to the left. OFC carries NO persistent state across ticks. It is
a pure function of its inputs: sensory_input, top_down, peer_input, and
its config. The parent (PrefrontalCortex) threads `{}` through OFC's state
slot as a matter of contract uniformity, but OFC's encode() does not read
or write state.

The reversal-learning division of labour is the same on both hemispheres:

    OFC               evaluates the current stimulus's value and computes
                      the prediction error (PE = actual - expected).
    ventral striatum  stores the running value estimate per stimulus, and
    (basal ganglia)   updates it by the PE that OFC emitted. The updated
                      estimate is exposed to OFC next tick via
                      top_down["basal_ganglia"]["current_value_estimate"].

The reversal learning is real and complete — but its store lives in the
striatum, not in OFC. OFC's half of the loop is pure; the striatum's half
is stateful. This is the same architecture on both hemispheres.

THE THREE REGISTRY-AREA SOURCES AND THEIR SHARES
------------------------------------------------
OFC is composed of three Brodmann area sources:

    brodmann_area_11        anterior OFC — semantic outcome evaluation
    brodmann_area_12        posterior OFC — visceral outcome evaluation
    brodmann_area_47        the OFC block of area 47 — value-guided
                            semantic retrieval

Each contributes to OFC's computation via its RIGHT_CONFIG block in
`brodmann_areas/`. The per-area shares live in `RIGHT_OFC_CONFIG` (NOT in
the areas' configs — no amendment is needed to areas 11, 12, or 47):

    11 : 12 : 47-OFC = 0.40 : 0.40 : 0.20

The shares are STRUCTURAL (equal across hemispheres); only the feature
values inside each area's config lateralise. The shares are chosen so
that the two primary OFC areas (11 and 12) dominate the aggregate and
area 47's OFC block contributes a meaningful but smaller dimension. The
share structure is identical on both sides — the right's OFC is not
"more area 12" or "less area 47", it is the same three-source blend with
right-specific feature values in each source.

On the right, area 12's contribution carries more weight *within its
share* (its amygdala and insula coupling is stronger, and its threat-
relevant outcomes dominate the right's evaluation) but the share itself
is 0.40 — equal to area 11's, because the OFC's three-source composition
structure does not lateralise. Only the feature values inside each source
differ.

THE COMPOSITION RULE — overlap-and-specific, generalized to three sources
------------------------------------------------------------------------
Same as the left. OFC uses the overlap-and-specific rule, generalized
from two sources (DLPFC) to three (OFC):

    OVERLAPPING FEATURES (present in 2+ source configs, blended by share):
        The five mechanism features — reward_prediction,
        punishment_prediction, stimulus_outcome_learning,
        reversal_learning, outcome_evaluation — are present in both
        areas 11 and 12 (NOT in area 47-OFC).
        The valence pair — positive_valence_bias, negative_valence_bias
        — is present in both areas 11 and 12.

    AREA-11-SPECIFIC FEATURES (pass through at 0.40 weight):
        verbal_reward_cue, visual_reward_cue.

    AREA-12-SPECIFIC FEATURES (pass through at 0.40 weight):
        taste_reward_evaluation, smell_threat_evaluation,
        visceral_punishment_evaluation, social_visceral_evaluation,
        verbal_outcome_label, direct_visceral_cue.
        On the right, the visceral features (taste, smell, visceral
        punishment) are more strongly weighted within area 12's
        contribution, and the direct_visceral_cue is at anchor level
        (0.75) — the right's signature route to outcome value.

    AREA-47-OFC-SPECIFIC FEATURES (pass through at 0.20 weight):
        semantic_value_evaluation, value_guided_retrieval,
        semantic_outcome_prediction, verbal_semantic_value,
        scene_semantic_value.
        On the right, scene_semantic_value is higher than
        verbal_semantic_value (the mirror of the left's verbal-leaning
        profile).

    Area 47-OFC does NOT carry the five mechanism features or the
    valence pair. Its features are disjoint from the {11, 12} cluster.

The generalized rule is identical: for each feature key, collect the
sources that carry it; one source → pass through; two sources → blend by
their shares; three sources → blend by all three. The rule is structural
and applies the same way on both hemispheres.

THE REVERSAL-LEARNING LOOP (the OFC-specific operational pattern)
------------------------------------------------------------------
OFC's most distinctive computation is the prediction-error signal. Each
tick:

    1. OFC reads `top_down["basal_ganglia"]["current_value_estimate"]`
       — the striatum's current estimate of the current stimulus's
       value.
    2. OFC reads `top_down["reward_signal"]` — the actual outcome.
    3. When an outcome occurred:
           prediction_error = actual_outcome - current_value_estimate
       The PE is emitted in the `reversal_learning` feature slot.
    4. OFC emits its current value evaluation (its feature-weighted
       "opinion" of what the stimulus is worth).

Same loop structure on the right; the content of "what the outcome is
worth" differs — the right's outcomes are more visceral and threat-
weighted, so the PEs the right's OFC computes reflect visceral/threat
dimensions of the same events. A food that the left's OFC evaluates as
"nutritious" may be evaluated by the right's OFC as "safe vs. potentially
harmful"; the PE for the same outcome is different because the
evaluation's axes differ.

Crucially: this loop is NOT stateful on OFC's side, on the right as on
the left. The persistence is in the striatum.

FEATURE EXTRACTION (the OFC's inputs)
-------------------------------------
Same sources as the left, with the right's emphasis:

    From sensory_input:
        stimulus_content      — the current stimulus's representation
        stimulus_identity     — which stimulus class (for the striatum's
                                per-stimulus estimates)

    From top_down:
        basal_ganglia_current_value_estimate
                              — the striatum's stored value
        reward_signal         — actual outcome (None if none)
        basal_forebrain_gain  — attention/arousal
        amygdala_salience     — threat/salience bias. On the right,
                                this feeds the negative_valence_bias
                                feature more strongly (the right's OFC
                                is more threat-attuned).
        cingulate_control     — targeted control from ACC

    From peer_input:
        (OFC is called third in prefrontal's order, after DMPFC and
        DLPFC. Same peer dependencies as on the left.)

The extraction rules are documented in the OFC class implementation.
The right's extraction weights visceral/sensory features higher than
verbal ones; the left's extraction weights verbal/semantic features
higher. The extraction function reads this from the config, not from
hardcoded weights.

CONTRIBUTION SHAPE
------------------
    contribution = {
        # Five mechanism features (blended from areas 11, 12)
        "reward_prediction":              <blended scalar>,
        "punishment_prediction":          <blended scalar>,
        "stimulus_outcome_learning":      <blended scalar>,
        "reversal_learning":              <blended scalar>,
        "outcome_evaluation":             <blended scalar>,

        # Valence pair (blended from areas 11, 12)
        "positive_valence_bias":          <blended scalar>,
        "negative_valence_bias":          <blended scalar>,

        # Area-11-specific (passed through at 0.40 weight)
        "verbal_reward_cue":              <scalar>,
        "visual_reward_cue":              <scalar>,

        # Area-12-specific (passed through at 0.40 weight)
        "taste_reward_evaluation":        <scalar>,
        "smell_threat_evaluation":        <scalar>,
        "visceral_punishment_evaluation": <scalar>,
        "social_visceral_evaluation":     <scalar>,
        "verbal_outcome_label":           <scalar>,
        "direct_visceral_cue":            <scalar>,

        # Area-47-OFC-specific (passed through at 0.20 weight)
        "semantic_value_evaluation":      <scalar>,
        "value_guided_retrieval":         <scalar>,
        "semantic_outcome_prediction":    <scalar>,
        "verbal_semantic_value":          <scalar>,
        "scene_semantic_value":           <scalar>,

        # Operational output
        "prediction_error":               <scalar in [-1, 1] or None>,

        # Identity passthrough
        "stimulus_identity":              <representation>,
    }

The schema is identical across hemispheres. The right's contents are
more visceral/threat-leaning (negative_valence_bias higher, visceral
features weighted higher within their sources), but the schema is
unchanged.

RIGHT-SPECIFIC BIAS
------------------
Same class as the left OFC; the RIGHT config changes the weights (via
the three area configs and the share structure, which is structural):

    positive_valence_bias    lower (avoidance-leaning, via areas 11
                             and 12's right biases)
    negative_valence_bias    higher
    direct_visceral_cue      higher (via area 12)
    scene_semantic_value     higher (via area 47-OFC)
    to_nucleus_accumbens     lower (positive-reward prediction is
                             left-lateralised)
    to_amygdala              higher (threat learning is right-
                             lateralised)
    to_insula                higher (visceral outcome state)
    shares (11:12:47-OFC)    structural (0.40 : 0.40 : 0.20)

The class, the composition logic, the overlap-and-specific rule, the
reversal-learning loop, and the prediction-error computation are
IDENTICAL across hemispheres. Only the config values inside the three
area configs differ. LEFT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left OFC. Cross-midline OFC exchange is one of
the most interesting in the prefrontal family. On the right, the cases
emphasise the right's role as the DISSONANCE SOURCE — the right's
threat/visceral evaluation is what the left's positive/semantic
evaluation has to reconcile with for narrative expression:

    - Valence divergence. The left's OFC computes positive-leaning
      value; the right's computes negative-leaning value. For the same
      stimulus, the two evaluate differently. This is EXPECTED and
      INFORMATIVE — the divergence is a signal about the stimulus's
      mixed valence, not a bug. The commissures surface it. A food
      that seems appealing (left) but unsettling (right) is a real
      pattern (approach-avoidance conflict), and the two OFCs
      disagreeing on it is the neurological signature of that pattern.

    - Reversal rate divergence. The two striata update independently,
      and their divergence is the signal. A contingency reversal that
      is fast for one hemisphere's valence evaluation may be slow for
      the other's — the two rates will differ because the two OFCs'
      prior valences differ. This is testable: feed the model a
      reversal task with a mixed-valence stimulus, and the two
      hemispheres' reversal rates should differ in a direction
      predictable from their valence biases.

    - Dissonance-to-narrative. When the right's negative-leaning
      evaluation conflicts with the left's positive-leaning one, the
      conflict has to be resolved for narrative expression. The left
      cannot express "I feel something bad about this" if the left's
      OFC says the stimulus is good — the bad feeling has to reach
      the left from the right. The right's higher to_commissures
      prior (0.55 vs 0.45) is the anatomical basis; direct import
      would bypass the commissural delay that gives the dissonance
      its behavioural signature ("I want it, but I'm not sure why
      I'm uneasy").

All three are commissural. The dissonance-to-narrative case is the
right's most frequently exercised cross-midline pattern in the frontal
lobe, because the right's threat-leaning evaluation conflicts with the
left's positive-leaning evaluation often, and each conflict needs the
commissural handoff to reach the left's narrative machinery.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. OFC is pure; the store is in
      the striatum.
    - Must not read area 11, 12, or 47's config directly — the configs
      are passed in via `config`.
    - Must not put the per-area shares into the area configs. Shares
      are STRUCTURAL and live in RIGHT_OFC_CONFIG.
    - Must not change the shares (0.40 : 0.40 : 0.20) on the right.
      The shares are STRUCTURAL — equal across hemispheres. The
      right's "more visceral" character lives in area 12's FEATURE
      WEIGHTS within its 0.40 share (and in area 12's higher
      connectivity priors to amygdala/insula), not in a larger
      area-12 share. A test that assumed "right OFC weights area 12
      more heavily" (at the share level) would fail; the share is
      equal, only the values within it differ.
    - Must not blend area-47-OFC's features with the mechanism cluster.
      Area 47-OFC's features are disjoint from the five mechanism
      features and the valence pair.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not implement the striatum's value update.
    - Must not import `brodmann_areas/` directly.
    - Must not import or reference the left OFC. Cross-midline
      exchange goes through the commissures. The dissonance-to-
      narrative case is a prime example: direct import would silently
      merge the two valence prisms and make the "approach-avoidance
      conflict expressed as narrative ambivalence" pattern
      untestable.
    - Must not diverge in structure from the left OFC — same class,
      same encode() signature, no state (both pure functions), same
      three-source composition, same overlap-and-specific rule, same
      reversal-learning loop, same share structure. Only the three
      area configs' values differ.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_OFC_CONFIG = {
        # Composition sources and their shares. STRUCTURAL — equal to
        # the left's.
        "sources": {
            "brodmann_area_11":      0.40,
            "brodmann_area_12":      0.40,
            "brodmann_area_47_ofc":  0.20,
        },
        "share_sum_check":      1.0,

        # Prediction-error computation parameters. STRUCTURAL.
        "prediction_error_clip":        [-1.0, 1.0],
        "prediction_error_emit_when":   "outcome_present",
    }

    The three area configs (brodmann_area_11.RIGHT_CONFIG,
    brodmann_area_12.RIGHT_CONFIG, brodmann_area_47's
    orbitofrontal_cortex block in RIGHT_CONFIG) are supplied by
    PrefrontalCortex at construction, not built here.

    RIGHT_OFC_CONFIG is IDENTICAL to LEFT_OFC_CONFIG except that it
    names the RIGHT_CONFIG exports of the three areas. Shares, share
    sum, and PE parameters are STRUCTURAL — equal across hemispheres.

    Two separate tests are needed:
        1. RIGHT_OFC_CONFIG == LEFT_OFC_CONFIG on shares, share sum,
           and PE parameters (structural equality).
        2. Each of the three areas' RIGHT_CONFIG is a directional
           mirror of that area's LEFT_CONFIG (feature and connectivity
           values mirror).
    A test that checked shares for directionality would fail spuriously
    — shares are structural, not lateralised.

EXPORTS
-------
    from .orbitofrontal_cortex import OrbitofrontalCortex
    from .orbitofrontal_cortex import RIGHT_OFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. No dlpfc_weight-style precondition: OFC's
    shares are defined in RIGHT_OFC_CONFIG, not in the areas' configs.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  OrbitofrontalCortex class, import the three area configs (brodmann_
  area_11, brodmann_area_12, brodmann_area_47's OFC block), verify the
  share-sum precondition, build RIGHT_OFC_CONFIG, instantiate the class,
  expose the class and the config.
- The class implements the sub-sub-region encode() signature. OFC is
  PURE — its state input is always {} and its output state is always
  {}.
- The overlap-and-specific composition rule, generalized to three
  sources, is a documented, unit-testable function
  (`_combine_areas(source_contributions, shares)`).
- The prediction-error computation is a documented, unit-testable
  function (`_compute_prediction_error(actual, estimate)`). Clipped
  to [-1, 1] per RIGHT_OFC_CONFIG.
- Feature extraction is a documented, unit-testable function. On the
  right, extraction weights visceral/sensory content higher than
  verbal/semantic; the extraction function reads this from the config,
  not from hardcoded weights.
- The class does not import or access any peer sub-sub-region's state.
- The class does not implement the striatum's value update.
- RIGHT_OFC_CONFIG is structurally identical to LEFT_OFC_CONFIG except
  for the area-config source references (RIGHT vs LEFT). Shares and PE
  parameters are STRUCTURAL.
- If a future change wants to add a fourth OFC source, the `sources`
  map gains an entry, the shares must still sum to 1.0 on both
  hemispheres, and the feature-key class map is re-derived.
- Must not import or reference the left OFC. Cross-midline exchange
  goes through `telencephalon/commissures/`.
"""