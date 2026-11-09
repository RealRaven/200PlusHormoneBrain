"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.prefrontal_cortex.ventromedial_prefrontal_cortex
================================================================================================================================================

The VENTROMEDIAL PREFRONTAL CORTEX (VMPFC) — left hemisphere. A compute
sub-sub-region of prefrontal, and one of the three pure-function children
of the prefrontal family.

VMPFC is the VALUE-INTEGRATION and SELF-REFERENTIAL core of the prefrontal
cortex: it combines stimulus value (from OFC), body-state information (from
the insula), affective tagging (from the amygdala), autobiographical
recall (from the hippocampus), and self-referential content (from its own
feature extraction) into a single integrated value signal that is
*self-relevant* — not "what is this worth" (OFC's question), but "how do I
feel about this, and does it matter to me". This integrated self-relevant
value is the input that biases downstream selection (VLPFC) and
goal-management (DMPFC) toward options that the system *feels* are right.

VMPFC is the area of the somatic-marker hypothesis (Damasio) and of the
Phineas Gage syndrome: damage spares explicit reasoning and IQ but
produces disastrous real-world decisions because the patient loses the
ability to *feel* the value of options and to integrate that feeling into
choice.

VMPFC IS A PURE FUNCTION (with a clarification about the somatic-marker loop)
---------------------------------------------------------------------------
VMPFC carries NO persistent state across ticks. It is a pure function of
its inputs. The parent (PrefrontalCortex) threads `{}` through VMPFC's
state slot, and VMPFC's encode() does not read or write state.

The obvious question — "the somatic-marker hypothesis is about *learning*
to associate situations with bodily states, which sounds stateful" — has
the same answer as OFC's reversal-learning case:

    VMPFC             integrates the current tick's stimuli, body state,
                      affect, memory, and self-reference into a
                      *present* self-relevant value signal. Its half of
                      the somatic-marker mechanism is pure: given the
                      current inputs, compute the integrated value.

    the associative store  lives elsewhere. Bodily-state associations
    (outside VMPFC)  (this situation → that gut feeling) are stored in
                      the insula (interoceptive memory), the amygdala
                      (affective tagging), and the striatum (value
                      estimates). The VMPFC does not store the
                      associations; it *reads* the currently-active ones
                      and integrates them.

So VMPFC's somatic-marker role is real and complete — but its
*associative* half lives in the structures VMPFC reads from, not in VMPFC
itself. VMPFC is the integrator at the head of the somatic-marker system,
not the memory organ at its core. This is consistent with how OFC relates
to the striatum: the evaluator is pure; the store is in the loop.

REGISTRY-AREA SOURCE (single source — same pattern as DMPFC)
-------------------------------------------------------------
VMPFC has ONE frontal-registry area source:

    brodmann_area_10/       the "ventromedial_prefrontal_cortex" area

Its config (in `brodmann_area_10.LEFT_CONFIG`) provides the VMPFC feature
weights: value_integration, somatic_marker, verbal_self_reference,
affective_self_reference, emotion_regulation_reappraisal,
emotion_regulation_suppression, autobiographical_recall,
social_valuation, risk_aversion, moral_judgment, plus connectivity
priors to amygdala, insula, hippocampus, PCC, precuneus, NAcc,
hypothalamus, DLPFC, basal ganglia, and commissures.

Because there is only one area source, there is NO share weight — no
`vmpfc_weight` field, analogous to how DMPFC has no `dmpfc_weight`.

IMPORTANT CAVEAT — AREA 25 (SUBGENUAL ACC) IS NOT A VMPFC SOURCE
----------------------------------------------------------------
A future contributor is very likely to ask "VMPFC integrates affect; area
25 is the affective division of the ACC; why isn't area 25 a VMPFC input?"
The answer is architectural and must be documented clearly:

    Area 25's COMPUTE lives in `cingulate/subgenual_area_25/`. It is a
    stateful compute sub-module that produces the ACC's `affect` scalar
    (the unpleasantness weight) and carries an `affective_setpoint`
    across ticks.

    Area 25 is NOT a VMPFC registry-area source. Its contribution to
    VMPFC is a SIGNAL, not a config read. The signal reaches VMPFC via
    one of two documented pathways, depending on which is more
    appropriate for a given experiment:

        pathway 1 (default)    top_down["cingulate_affect"]
                               — the ACC's affect channel, as part of
                               the salience slice. VMPFC reads it as
                               an affective bias on its own
                               integration. This is the same
                               mechanism by which VMPFC reads the
                               ACC's control_demand channel
                               (top_down["cingulate_control"]).

        pathway 2 (optional)   a connectivity prior on VMPFC's area 10
                               config (e.g. `to_subgenual_area_25`).
                               This models the anatomical coupling
                               without making VMPFC's computation
                               depend on the cingulate's state. It is
                               NOT added by this file (area 10's config
                               does not currently have such a prior),
                               but it is the documented mechanism if a
                               future experiment needs it.

    What VMPFC must NOT do is read area 25's config or state directly,
    or import `cingulate/subgenual_area_25/`. That would couple
    VMPFC's pure function to the cingulate's stateful compute — a
    layering violation, and the exact kind of cross-tree read that
    every earlier caveat in this project has been preventing.

    The architectural claim (VMPFC reads the ACC's affect via top_down,
    not via registry) is the same pattern as the ACC's control_demand
    being read via top_down by DLPFC, DMPFC, OFC, and VLPFC. Consistency
    across the prefrontal family matters here.

THE COMPOSITION — single-source, the trivial N=1 case
-----------------------------------------------------
VMPFC's composition is the N=1 case of the overlap-and-specific rule:
there is one source (area 10), so there is nothing to blend. The rule's
general form (blend features present in multiple sources; pass through
features present in one source) reduces to "pass through every feature
from the single source", which is what VMPFC does.

The docstring notes this explicitly so that a future contributor adding
a second VMPFC source (e.g. a documented VMPFC portion of area 10's
medial extension, if the schema ever allows it) would apply the
overlap-and-specific rule at that point, rather than inventing a new
pattern. Until then, N=1 is the correct shape.

THE SOMATIC-MARKER INTEGRATION (the VMPFC-specific operational pattern)
-----------------------------------------------------------------------
VMPFC's most distinctive computation is the somatic-marker integration.
Each tick:

    1. Read the value sources:
           stimulus_value       from OFC's contribution (via peer_input)
           body_state           from top_down["insular_state"]
                                (interoceptive input from the insula —
                                autonomic, visceral, homeostatic)
           affective_tag        from top_down["amygdala_affect"]
                                (the amygdala's current affective
                                tagging of the stimulus)
           self_context         from VMPFC's own feature extraction
                                (verbal_self_reference or
                                affective_self_reference, per the
                                hemisphere's bias)
           autobiographical_cue from top_down["hippocampal_recall"]
                                (the current retrieval from episodic
                                memory)
           acc_affect           from top_down["cingulate_affect"]
                                (the ACC's affect channel; optional,
                                may be None when area 25 is quiet)

    2. Integrate the sources:
           integrated_value = (
               w_stimulus_value    * stimulus_value
             + w_body_state        * body_state
             + w_affective_tag     * affective_tag
             + w_self_relevance    * self_context
             + w_autobiographical  * autobiographical_cue
             + w_acc_affect        * acc_affect
           )
       The weights (the `somatic_marker_weights`) are in
       LEFT_VMPFC_CONFIG, STRUCTURAL — equal across hemispheres. They
       define how much each source contributes to the integrated
       value.

    3. Bias downstream via the somatic-marker signal:
           somatic_marker_bias = integrated_value - stimulus_value
       The bias is the *added* signal beyond what OFC alone would
       provide — the contribution of body state, affect, memory, and
       self-reference. When OFC says "this is worth X" and VMPFC's
       integration says "it's worth X plus a gut feeling of unease",
       the bias is the unease. This bias is what downstream
       selection (VLPFC) and goal-management (DMPFC) consume as the
       "something feels off about this" signal.

    4. Emit both:
           - the integrated value (VMPFC's headline valuation)
           - the somatic-marker bias (the added signal beyond OFC)
           - the feature vector (per-feature values, for downstream
             consumers that want to inspect the self-referential
             dimensions directly)

The integrated value and the somatic-marker bias are the two outputs
downstream consumers care about. VLPFC reads the integrated value as
one of the inputs to its selection scoring; DMPFC reads the
somatic-marker bias as a potential goal-reprioritisation trigger ("this
goal suddenly feels less urgent").

The somatic-marker bias is what makes the Phineas Gage failure mode
testable. In a right-VMPFC lesion, the integrated_value is computed but
the somatic_marker_bias is degraded — the patient can report the
integrated value verbally ("I know this is dangerous") but the bias
signal that would have biased selection is absent, so selection proceeds
without it. The behaviour matches the classic pattern: knows the
correct answer, cannot act on it.

THE DOUBLE DISSOCIATION (documented at config, testable at compute)
-------------------------------------------------------------------
The VMPFC pair's lateralisation gives the classic double dissociation,
which this sub-sub-region's compute makes reachable:

    Left VMPFC lesion:    verbal_self_reference and
                          emotion_regulation_reappraisal are
                          degraded; affective_self_reference and
                          emotion_regulation_suppression are spared.
                          The patient can feel but cannot explain.
                          The somatic_marker_bias is present (the
                          affective inputs are intact) but the
                          verbal narrative around it is impaired.

    Right VMPFC lesion:   affective_self_reference and
                          emotion_regulation_suppression are
                          degraded; verbal_self_reference and
                          reappraisal are spared. The patient can
                          explain but cannot feel. The
                          somatic_marker_bias is degraded (the
                          affective and body-state inputs are
                          damaged) but the verbal narrative is
                          preserved.

The dissociation is entirely expressed via the source config's
directionally-mirrored feature weights. The VMPFC class, the
integration formula, the bias computation, and the structural
weights are identical across hemispheres — only the source config's
feature values (affective vs verbal) differ.

FEATURE EXTRACTION (the VMPFC's inputs)
---------------------------------------
    From sensory_input:
        self_relevant_cues    — content referring to the system's
                                own state, history, or identity
        social_content        — content with social or moral
                                relevance (feeds social_valuation
                                and moral_judgment)

    From top_down:
        insular_state         — interoceptive/body state (autonomic,
                                visceral, homeostatic)
        amygdala_affect       — current affective tagging
        hippocampal_recall    — current episodic retrieval
        cingulate_affect      — ACC's affect channel (may be None)
        basal_ganglia_current_value_estimate
                              — the striatum's stored value (same
                                input OFC uses; VMPFC uses it for
                                comparison with OFC's per-tick
                                evaluation)
        cingulate_control     — ACC's control_demand (bias on how
                                strongly to weight self-relevance
                                this tick)
        basal_forebrain_gain  — attention/arousal

    From peer_input:
        (VMPFC is called fourth in prefrontal's order, after DMPFC,
        DLPFC, and OFC.)
        peer_input["orbitofrontal_cortex"]           — stimulus
            value (OFC's per-tick evaluation)
        peer_input["dorsomedial_prefrontal_cortex"]  — current goal
            (may bias which self-relevant content is activated)
        peer_input["dorsolateral_prefrontal_cortex"] — working
            memory contents (may provide autobiographical cues)

    The extraction rules are documented in the VMPFC class
    implementation.

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

        # Operational output — the integration result
        "integrated_value":              <scalar>,
        "somatic_marker_bias":           <scalar>,   # integrated_value
                                                     # minus stimulus_value
    }

    The ten feature fields are VMPFC's feature-level evaluation. The
    integrated_value is the headline (the whole point of VMPFC), and
    the somatic_marker_bias is the "something feels off" signal that
    downstream consumers read when they want the *added* information
    beyond OFC's per-stimulus value.

    The two operational fields are not feature weights — they are
    per-tick computed quantities. Downstream consumers that care about
    VMPFC's headline read `integrated_value`; consumers that want the
    bias read `somatic_marker_bias`.

LEFT-SPECIFIC BIAS
------------------
Same class as the right VMPFC; the LEFT config changes the weights
(via area 10's config):

    verbal_self_reference         higher (0.80)
    affective_self_reference      lower (0.45)
    emotion_regulation_reappraisal higher (0.75)
    emotion_regulation_suppression lower (0.35)
    risk_aversion                 lower (0.55)
    to_amygdala                   lower (0.55)
    to_insula                     lower (0.60)
    to_hypothalamus               lower (0.50)
    to_commissures                lower (0.45)

The class, the integration formula, the bias computation, the feature
extraction, and the somatic_marker_weights are IDENTICAL across
hemispheres. Only area 10's feature values and connectivity priors
differ. RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right VMPFC. Cross-midline VMPFC exchange is
the "feels but can't explain" / "explains but can't feel" pair that the
clinical dissociation is built on:

    - Value-to-narrative. The right's VMPFC produces an affectively-
      weighted integrated value (a "this feels wrong" signal); the
      left's VMPFC produces a verbally-mediated integrated value (a
      "this fits my story" signal). For a self-relevant outcome,
      the two can differ — a scene that fits the left's narrative but
      triggers the right's unease. The dissonance is the signal, and
      the exchange is commissural (the right's affective value
      reaching the left's narrative machinery for expression:
      "I felt it was wrong but couldn't say why").

    - Reappraisal handoff. The left's reappraisal machinery may
      attempt to talk the right's affective self-reference down; the
      right's autonomic suppression may attempt to dampen the
      left's verbally-aroused affect. Both handoffs are commissural.

    - Moral judgment split. The left's verbally-mediated moral
      reasoning and the right's affectively-mediated moral intuition
      often disagree; the disagreement is the classic dual-process
      moral psychology pattern, and the commissures surface it.

All three are commissural. The "value-to-narrative" case is the
canonical VMPFC cross-midline case, and its behavioural signature
("I want it, but I feel uneasy") is the composite of the two
hemispheres' integrated values.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. VMPFC is pure; the somatic-
      marker associations live in the insula, amygdala, and striatum
      that VMPFC reads from.
    - Must not read area 10's config directly — it is passed in via
      `config`.
    - Must not add a `vmpfc_weight` field. VMPFC has a single
      registry-area source; the `dlpfc_weight` pattern does not apply.
    - Must not read area 25's config or state. Area 25 is a cingulate
      compute sub-module, not a VMPFC registry source. The ACC's
      affect reaches VMPFC via top_down["cingulate_affect"] (or, in
      a future schema change, a connectivity prior on area 10's
      config), never via a direct read.
    - Must not read area 9 or area 8's medial extensions. As with
      DMPFC, anatomical adjacency is documented as a caveat, not as
      a configurable input. VMPFC reads area 10 only.
    - Must not implement the associative store (which situation goes
      with which bodily state). That store lives in the insula,
      amygdala, and striatum; VMPFC integrates the *currently
      active* associations, it does not maintain them.
    - Must not implement the striatum's value update. VMPFC reads
      `basal_ganglia_current_value_estimate` and uses it in the
      integration; it does not write back to the striatum's store.
    - Must not change the `somatic_marker_weights` on the right.
      Those weights (how much each source contributes to the
      integration) are STRUCTURAL — equal across hemispheres. The
      right's "more affective" character lives in area 10's
      directionally-mirrored feature weights (affective vs verbal
      self-reference, etc.), not in the integration weights. A test
      that assumed "right VMPFC weighs body state more heavily" at
      the integration level would fail; the integration weights are
      equal, and the lateralised character comes from the source
      config's feature values.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not import `brodmann_areas/` directly.
    - Must not import or reference the right VMPFC. Cross-midline
      exchange goes through `telencephalon/commissures/`.
    - Must not diverge in structure from the right VMPFC — same class,
      same encode() signature, no state (both pure functions), same
      single-source composition, same somatic-marker integration,
      same integration weights. Only area 10's feature values and
      connectivity priors differ.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_VMPFC_CONFIG = {
        # Composition source (single area source; no share weight).
        "source_area":  "brodmann_area_10",

        # Somatic-marker integration weights (STRUCTURAL — equal
        # across hemispheres). These are the coefficients in the
        # integrated_value formula. They define how much each
        # source contributes; they do NOT define which source is
        # more "affective" (that's area 10's feature weights).
        "somatic_marker_weights": {
            "stimulus_value":    0.30,   # from OFC
            "body_state":        0.20,   # from insula
            "affective_tag":     0.20,   # from amygdala
            "self_relevance":    0.15,   # from area 10's feature
            "autobiographical":  0.10,   # from hippocampus
            "acc_affect":        0.05,   # from area 25 (top_down)
            # sum to 1.0
        },

        # Bias computation (STRUCTURAL).
        # somatic_marker_bias = integrated_value - stimulus_value
        # The bias is the added signal beyond OFC's per-stimulus
        # value. No tunable weight; the formula is the contract.

        # ACC affect reading (STRUCTURAL).
        # VMPFC reads top_down["cingulate_affect"] when present;
        # when absent (None), the acc_affect term is treated as 0.0
        # and the remaining weights are renormalised to sum to 1.0.
        # This is documented behaviour so that a quiet area 25 does
        # not spuriously pull the integrated value downward.
        "acc_affect_renormalise_when_absent": True,
    }

    Area 10's config (brodmann_area_10.LEFT_CONFIG) is supplied by
    PrefrontalCortex at construction. It provides the ten feature
    weights and the connectivity priors.

    RIGHT_VMPFC_CONFIG is IDENTICAL except that it names
    brodmann_area_10.RIGHT_CONFIG. The somatic_marker_weights and
    the renormalisation flag are STRUCTURAL — equal across
    hemispheres.

    Two separate tests are needed:
        1. RIGHT_VMPFC_CONFIG == LEFT_VMPFC_CONFIG on
           somatic_marker_weights and renormalisation
           (structural equality).
        2. brodmann_area_10.RIGHT_CONFIG is a directional mirror of
           LEFT_CONFIG (feature and connectivity values mirror).
    A test that checked somatic_marker_weights for directionality
    would fail spuriously — they are structural, not lateralised.

EXPORTS
-------
    from .ventromedial_prefrontal_cortex import VentromedialPrefrontalCortex
    from .ventromedial_prefrontal_cortex import LEFT_VMPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. No dlpfc_weight-style precondition:
    VMPFC's single source means there is no share to verify.

    NOTE: This package's construction does NOT depend on the pending
    area-9 dlpfc_weight amendment (that affects DLPFC only). VMPFC
    can be instantiated as soon as the class is implemented, using
    area 10's config as-is.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  VentromedialPrefrontalCortex class, import brodmann_area_10's
  LEFT_CONFIG, build LEFT_VMPFC_CONFIG, instantiate the class, expose
  the class and the config.
- The class implements the sub-sub-region encode() signature. VMPFC
  is PURE — state input is always {}, output state is always {}.
- The single-source composition is trivial (pass through every
  feature from area 10's config-weighted extraction). The class
  does not need a `_blend_*` function — there is nothing to blend.
  But the class DOES document that adding a second source would
  apply the overlap-and-specific rule; a future extension is
  foreseen, not designed-in.
- The somatic-marker integration is a documented, unit-testable
  function (`_integrate_value(sources, weights) -> integrated_value`).
  Tested with synthetic source values to confirm the weighting is
  applied correctly and the renormalisation behaves as specified
  when acc_affect is None.
- The bias computation is a documented, unit-testable function
  (`_somatic_marker_bias(integrated_value, stimulus_value)`).
- Feature extraction is a documented, unit-testable function.
- The class does not import or access any peer sub-sub-region's
  state — it reads peer_input contributions (OFC's stimulus value,
  DMPFC's goals, DLPFC's WM).
- The class does not read area 25, area 9, or area 8's config. Any
  ACC affect reaches VMPFC via top_down["cingulate_affect"], not
  via config.
- The class does not implement the somatic-marker associative store.
  It integrates the currently-active associations; the store lives
  in the insula, amygdala, and striatum that VMPFC reads from.
- LEFT_VMPFC_CONFIG is structurally identical to RIGHT_VMPFC_CONFIG
  except for the area-config source reference. Integration weights
  and renormalisation are STRUCTURAL.
- If a future change wants to add a second VMPFC source (e.g. a
  documented VMPFC portion of the medial extension of area 9 or
  area 10), the composition becomes N=2 and the overlap-and-specific
  rule applies: shared features blend by shares, source-specific
  features pass through. That is a substantive schema change,
  documented in the registry area's config as a new sub-region
  block — not an ad-hoc config addition here.
- Must not import or reference the right VMPFC. Cross-midline
  exchange goes through `telencephalon/commissures/`.
"""