"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.prefrontal_cortex.orbitofrontal_cortex
======================================================================================================================================

The ORBITOFRONTAL CORTEX (OFC) — left hemisphere. A compute sub-sub-region
of prefrontal, and one of the three pure-function children of the
prefrontal family.

OFC is the stimulus-outcome learner: it evaluates what stimuli are worth,
computes prediction errors when actual outcomes diverge from expected
ones, and drives the reversal-learning loop that keeps the value system
adapting to changing contingencies. It is the "what is this worth right
now, and has that changed?" pole of the prefrontal cortex.

OFC IS A PURE FUNCTION (with a clarification about reversal learning)
---------------------------------------------------------------------
OFC carries NO persistent state across ticks. It is a pure function of its
inputs: sensory_input, top_down, peer_input, and its config. The parent
(PrefrontalCortex) threads `{}` through OFC's state slot as a matter of
contract uniformity, but OFC's encode() does not read or write state.

This raises an obvious question for OFC specifically: "reversal learning
is *learning* — how can OFC be stateless?" The answer is a division of
labour across the OFC-basal-ganglia loop:

    OFC               evaluates the current stimulus's value from its
                      inputs (feature computation) and computes the
                      prediction error between that expectation and the
                      actual outcome (PE = actual - expected). It emits
                      the PE as part of its contribution.

    ventral striatum  stores the running value estimate per stimulus,
    (basal ganglia)   and updates it by the PE that OFC emitted. The
                      updated estimate is exposed to OFC next tick via
                      top_down["basal_ganglia"]["current_value_estimate"].

So the *reversal learning* is real and complete — but its store lives in
the striatum, not in OFC. OFC's half of the loop is pure (evaluate + PE);
the striatum's half is stateful (store + update). From OFC's perspective,
the value of the current stimulus is simply one of its top_down inputs,
and the PE it computes this tick is simply one of its outputs.

This is consistent with the project's architecture throughout: the
basal ganglia are the value store and gating mechanism; OFC evaluates
and signals; the loop between them produces reversal behaviour. OFC is
not a memory organ in this model; it is the evaluator at the head of
the memory-bearing basal ganglia.

THE THREE REGISTRY-AREA SOURCES AND THEIR SHARES
------------------------------------------------
OFC is composed of three Brodmann area sources:

    brodmann_area_11        anterior OFC — semantic outcome evaluation
    brodmann_area_12        posterior OFC — visceral outcome evaluation
    brodmann_area_47        the OFC block of area 47 — value-guided
                            semantic retrieval

Each contributes to OFC's computation via its LEFT_CONFIG block in
`brodmann_areas/`. The per-area shares live in `LEFT_OFC_CONFIG` (NOT in
the areas' configs — no amendment is needed to areas 11, 12, or 47):

    11 : 12 : 47-OFC = 0.40 : 0.40 : 0.20

The shares are STRUCTURAL (equal across hemispheres); only the feature
values inside each area's config lateralise. The shares are chosen so
that the two primary OFC areas (11 and 12) dominate the aggregate and
area 47's OFC block contributes a meaningful but smaller dimension (the
semantic-value-specific part of OFC's role).

THE COMPOSITION RULE — overlap-and-specific, generalized to three sources
------------------------------------------------------------------------
This file corrects the earlier characterisation (in DLPFC's docstring)
that OFC's composition was "disjoint." That was imprecise. The accurate
picture is: OFC uses the SAME overlap-and-specific rule that DLPFC
introduced, generalized from two sources to three:

    OVERLAPPING FEATURES (present in 2+ source configs, blended by share):
        The five mechanism features — reward_prediction,
        punishment_prediction, stimulus_outcome_learning,
        reversal_learning, outcome_evaluation — are present in both
        area 11 and area 12 (NOT in area 47-OFC; see below).

        The valence pair — positive_valence_bias,
        negative_valence_bias — is present in both area 11 and area 12.

        These are blended by 11's and 12's shares (0.40 / 0.40 →
        effective blend ratio 0.5:0.5 when the 47-OFC share is not
        applicable to that feature).

    AREA-11-SPECIFIC FEATURES (pass through from area 11 at full weight):
        verbal_reward_cue, visual_reward_cue.

    AREA-12-SPECIFIC FEATURES (pass through from area 12 at full weight):
        taste_reward_evaluation, smell_threat_evaluation,
        visceral_punishment_evaluation, social_visceral_evaluation,
        verbal_outcome_label, direct_visceral_cue.

    AREA-47-OFC-SPECIFIC FEATURES (pass through from area 47-OFC at
    full weight, scaled by 47-OFC's share):
        semantic_value_evaluation, value_guided_retrieval,
        semantic_outcome_prediction, verbal_semantic_value,
        scene_semantic_value.

    Note: area 47-OFC does NOT carry the five mechanism features or the
    valence pair. Its contribution is the semantic-value-specific
    dimension of OFC's role — the bridge to VLPFC's retrieval — not the
    generic stimulus-outcome mechanism. So area 47-OFC's features are
    disjoint from the {11, 12} mechanism cluster; there is no
    three-way blend anywhere.

The generalized rule: for each feature key, collect the source configs
that carry it. If one source carries it, pass it through at full weight
(or scaled by that source's share if the feature is "shared" in the
sense of being area-specific). If two sources carry it, blend by their
shares. If three sources carried it (which no current feature does),
blend by all three.

This is DLPFC's rule, applied to N sources instead of two.

THE REVERSAL-LEARNING LOOP (the OFC-specific operational pattern)
------------------------------------------------------------------
OFC's most distinctive computation is the prediction-error signal that
drives reversal learning. Each tick:

    1. OFC reads `top_down["basal_ganglia"]["current_value_estimate"]`
       — the striatum's current estimate of the value of the current
       stimulus (stateful; stored outside OFC).
    2. OFC reads `top_down["reward_signal"]` — the actual outcome, if
       any occurred this tick (e.g. a reward delivered, a punishment
       suffered, a neutral outcome). When no outcome occurred, this is
       None and step 3 is skipped.
    3. When an actual outcome is present:
           prediction_error = actual_outcome - current_value_estimate
       This PE is what OFC emits in its `reversal_learning` feature
       slot (and it is the reason `reversal_learning` is such a high-
       weighted feature in both area 11 and area 12: it is OFC's
       primary contribution to the loop).
    4. OFC also emits its current value *evaluation* (the weighted
       combination of its feature weights applied to the current
       stimulus) — this is OFC's "opinion" of what the stimulus is
       worth, used by downstream consumers (VMPFC's value integration,
       VLPFC's value-guided selection).

The prediction error is then consumed by the basal ganglia (via the
`to_nucleus_accumbens` and `to_basal_ganglia` connectivity priors in
areas 11 and 12), which updates its stored estimate. Next tick, the
updated estimate is available to OFC via `current_value_estimate`.

Crucially: this loop is NOT stateful on OFC's side. OFC reads two scalars
from top_down and emits one scalar (PE) per tick. The persistence is in
the striatum. OFC's contribution to reversal behaviour is the signal, not
the store.

THIS IS THE OFC-SPECIFIC OPERATIONAL PATTERN
--------------------------------------------
Like DLPFC's working_memory update and DMPFC's goal-stack management,
OFC's prediction-error computation is a documented, unit-testable
operation that goes beyond simple feature weighting. It reads two top_down
signals, computes a difference, clips it to [-1, 1], and emits it. The
function `_compute_prediction_error(actual, estimate)` is unit-testable
in isolation; the full loop (OFC ↔ striatum) is testable end-to-end
against the reversal-learning task predictions from the registry files.

FEATURE EXTRACTION (the OFC's inputs)
-------------------------------------
    From sensory_input:
        stimulus_content      — the current stimulus's representation,
                                used to compute the feature weights
        stimulus_identity     — which stimulus class this is, used by
                                the striatum's per-stimulus value
                                estimates (passed through in the
                                contribution so downstream can key on
                                it)

    From top_down:
        basal_ganglia_current_value_estimate
                              — the striatum's stored value for the
                                current stimulus (stateful; the store)
        reward_signal         — actual outcome this tick (None if no
                                outcome occurred)
        basal_forebrain_gain  — attention/arousal
        amygdala_salience     — threat/salience bias (feeds the
                                negative_valence_bias feature)
        cingulate_control     — targeted control from ACC (may trigger
                                re-evaluation of an outcome's value)

    From peer_input:
        (OFC is called third in prefrontal's order, after DMPFC and
        DLPFC. It reads DMPFC's goals to bias which outcomes are
        relevant to the current goal — e.g. if the goal is "get food",
        food outcomes are weighted higher. It reads DLPFC's working-
        memory contents to bias value attribution — e.g. if the
        working-memory slot holds a particular stimulus, its value
        is weighted higher.)

    Full extraction rules are documented in the OFC class implementation.

CONTRIBUTION SHAPE
------------------
    contribution = {
        # The five mechanism features (blended from areas 11 and 12)
        "reward_prediction":              <blended scalar>,
        "punishment_prediction":          <blended scalar>,
        "stimulus_outcome_learning":      <blended scalar>,
        "reversal_learning":              <blended scalar>,
        "outcome_evaluation":             <blended scalar>,

        # The valence pair (blended from areas 11 and 12)
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

        # Operational output — not a feature
        "prediction_error":               <scalar in [-1, 1] or None>,

        # Identity passthrough for downstream consumers
        "stimulus_identity":              <representation>,
    }

    The `prediction_error` field is OFC's operational output — the signal
    the basal ganglia consume to update their value estimates. It is
    NOT a feature weight; it is a per-tick computed value. Consumers that
    care about OFC's feature-level evaluation read the feature fields;
    the basal ganglia read `prediction_error`.

    The `stimulus_identity` passthrough lets downstream consumers (the
    basal ganglia, in particular) key their per-stimulus value estimates
    on the correct stimulus.

LEFT-SPECIFIC BIAS
------------------
Same class as the right OFC; the LEFT config changes the weights (via
the three area configs and the share structure):

    positive_valence_bias    higher weight (approach, via areas 11 and
                             12's left-leaning biases)
    negative_valence_bias    lower weight
    verbal_reward_cue        higher (via area 11)
    verbal_outcome_label     higher (via area 12)
    verbal_semantic_value    higher (via area 47-OFC)
    to_nucleus_accumbens     higher (via areas 11 and 12 — positive
                             reward prediction is left-lateralised)
    to_amygdala              lower (via areas 11 and 12 — threat
                             learning is right-lateralised)
    to_insula                lower
    shares (11:12:47-OFC)    structural (0.40 : 0.40 : 0.20)

The class, the composition logic, the overlap-and-specific rule, the
reversal-learning loop, and the prediction-error computation are
IDENTICAL across hemispheres. Only the config values inside the three
area configs differ. RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right OFC. Cross-midline OFC exchange is one
of the most interesting in the prefrontal family:

    - Valence divergence. The left's OFC computes positive-leaning
      value; the right's OFC computes negative-leaning value. For the
      SAME stimulus, the two can evaluate it differently — a food
      that seems safe (left) may seem risky (right) if the right's
      visceral-aversive memory is stronger. The divergence is expected
      and informative; the commissures surface it.

    - Reversal rate divergence. When the basal ganglia's stored value
      updates, the two hemispheres' PEs may diverge (the left's
      positive-leaning prior yields a different PE than the right's
      negative-leaning one for the same outcome). The two striata
      update independently, and their divergence is the signal.

    - Motivation-weighted choice. When a choice has both positive and
      negative aspects, the left's OFC may dominate if positive,
      right's if negative. The arbitration happens downstream
      (basal ganglia gating, ACC conflict), with the two OFCs' values
      exchanged via the commissures.

All three are commissural. Direct OFC-to-OFC access would silently
merge the two valence prisms and make the "left finds this appealing,
right finds it threatening" failure mode untestable.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. OFC is pure; the store is in
      the striatum. If a future experiment needs OFC-specific stored
      state (e.g. per-stimulus value estimates that are NOT in the
      striatum), that is a schema change documented in the prefrontal
      family's state contract — not an ad-hoc state added to OFC.
    - Must not read area 11, 12, or 47's config directly — the configs
      are passed in via `config` (built by PrefrontalCortex at
      construction).
    - Must not put the per-area shares (11, 12, 47-OFC) into the area
      configs. The shares are STRUCTURAL and live in LEFT_OFC_CONFIG.
      This is a deliberate design choice: the shares describe how
      OFC composes its sources, not what each source contributes; the
      latter is the areas' feature weights.
    - Must not blend area-47-OFC's features with the mechanism cluster.
      Area 47-OFC's features are disjoint from the five mechanism
      features and the valence pair. Passing them through at 0.20
      weight is correct; blending them with the mechanism cluster
      would falsely suggest 47-OFC contributes to those mechanisms.
    - Must not inspect or mutate peer sub-sub-regions' state. OFC
      reads DMPFC's goals and DLPFC's working-memory contents from
      peer_input (published contributions), not from their state
      dicts.
    - Must not implement the striatum's value update. OFC emits the
      PE; the basal ganglia apply it. Adding value-store logic to
      OFC would violate the pure-function contract and would break
      the "OFC ↔ striatum is a loop, not a store" architecture.
    - Must not import `brodmann_areas/` directly.
    - Must not import or reference the right OFC. Cross-midline
      exchange goes through the commissures.
    - Must not diverge in structure from the right OFC — same class,
      same encode() signature, no state (both pure functions), same
      three-source composition, same overlap-and-specific rule, same
      reversal-learning loop. Only the three area configs' values
      differ.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_OFC_CONFIG = {
        # Composition sources and their shares. STRUCTURAL — equal
        # across hemispheres.
        "sources": {
            "brodmann_area_11":      0.40,
            "brodmann_area_12":      0.40,
            "brodmann_area_47_ofc":  0.20,   # area 47's OFC block
        },
        "share_sum_check":      1.0,         # all shares sum to 1.0
                                             # (asserted at construction)

        # Feature-key class map. Determines which features are
        # blended (present in >1 source) vs passed through (present
        # in exactly 1 source). This map is derived from the three
        # area configs at construction time; listed here for
        # documentation, not set explicitly.
        #
        # Mechanism five + valence pair:  blended between areas 11, 12.
        # Area-11-specific:               pass-through from area 11.
        # Area-12-specific:               pass-through from area 12.
        # Area-47-OFC-specific:           pass-through from area 47.

        # Prediction-error computation parameters. STRUCTURAL.
        "prediction_error_clip":        [-1.0, 1.0],   # clip range
        "prediction_error_emit_when":   "outcome_present",  # PE is
                                             # emitted only when
                                             # top_down["reward_signal"]
                                             # is not None; otherwise
                                             # the field is None
    }

    The three area configs (brodmann_area_11, brodmann_area_12,
    brodmann_area_47's orbitofrontal_cortex block) are supplied by
    PrefrontalCortex at construction, not built here. They provide
    the per-feature weights and connectivity priors.

    RIGHT_OFC_CONFIG is IDENTICAL except that it names the
    RIGHT_CONFIG exports of the three areas. The shares (0.40/0.40/
    0.20), the feature-class map structure, and the PE computation
    parameters are STRUCTURAL — equal across hemispheres. The
    lateralisation lives entirely in the three areas' feature
    weights and connectivity priors.

    Two separate tests are needed:
        1. RIGHT_OFC_CONFIG == LEFT_OFC_CONFIG on shares, share sum,
           and PE parameters (structural equality).
        2. Each of the three areas' RIGHT_CONFIG is a directional
           mirror of that area's LEFT_CONFIG (feature and connectivity
           values mirror).

EXPORTS
-------
    from .orbitofrontal_cortex import OrbitofrontalCortex
    from .orbitofrontal_cortex import LEFT_OFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. It requires no dlpfc_weight-style
    precondition: OFC's shares are defined in LEFT_OFC_CONFIG, not in
    the areas' configs, so there is nothing pending in the registry.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  OrbitofrontalCortex class, import the three area configs (brodmann_
  area_11, brodmann_area_12, brodmann_area_47's OFC block), verify the
  share-sum precondition, build LEFT_OFC_CONFIG, instantiate the class,
  expose the class and the config.
- The class implements the sub-sub-region encode() signature. OFC is
  PURE — its state input is always {} and its output state is always
  {}. The parent threads {} uniformly; the class does not use it.
- The overlap-and-specific composition rule, generalized to three
  sources, is a documented, unit-testable function
  (`_combine_areas(source_contributions, shares)`), tested with
  synthetic feature dicts to confirm the blend/pass-through rule is
  applied correctly.
- The prediction-error computation is a documented, unit-testable
  function (`_compute_prediction_error(actual, estimate)`). Clipped
  to [-1, 1] per LEFT_OFC_CONFIG.
- Feature extraction is a documented, unit-testable function.
- The class does not import or access any peer sub-sub-region's state
  — it reads peer_input contributions (DMPFC goals, DLPFC WM) only.
- The class does not implement the striatum's value update. It emits
  PE; the basal ganglia apply it.
- LEFT_OFC_CONFIG is structurally identical to RIGHT_OFC_CONFIG
  except for the area-config source references (LEFT vs RIGHT). Shares
  and PE parameters are STRUCTURAL.
- If a future change wants to add a fourth OFC source (unlikely
  without anatomy changes), the `sources` map gains an entry, the
  shares must still sum to 1.0, and the feature-key class map is
  re-derived. This is a substantive modeling decision, not a config
  tweak.
- Must not import or reference the right OFC. Cross-midline exchange
  goes through `telencephalon/commissures/`.
"""