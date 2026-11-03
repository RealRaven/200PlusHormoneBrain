"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_11
======================================================================================================================

Brodmann area 11 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 11, says which compute sub-region owns it,
and supplies the per-area weights that the owning sub-region's `encode()`
reads. It defines no classes and no functions; the public surface is the
exports listed under "EXPORTS".

If you are looking for the computation area 11 participates in, it lives in
`.../frontal/cortex/prefrontal_cortex/orbitofrontal_cortex/` — area 11 is
the anterior orbitofrontal cortex, and OFC is the stimulus-outcome learning
and outcome-evaluation core of the frontal lobe. This package is the
*label*; the OFC compute sub-region is the *agent*.

OFC vs. VMPFC vs. DLPFC (the framing this file inherits)
--------------------------------------------------------
The prefrontal cortex has three poles that are easy to conflate but
compute different things:

    DLPFC (areas 9, 46)   the EFFORTFUL, working-memory executive.
                          Holds information online. Deliberate. Answers
                          "what rules apply, and what should I do
                          about it?"

    OFC (areas 11, 12)    the STIMULUS-OUTCOME LEARNER. Learns which
                          stimuli predict which outcomes. Tracks
                          reward/punishment as it arrives. Answers
                          "what is this stimulus worth right now, and
                          has that changed?"

    VMPFC (area 10)       the INTEGRATED VALUE and SELF. Combines
                          stimulus value, body state, memory, and
                          self-relevance into a single overall
                          valuation. Answers "how do I feel about this
                          overall, and does it matter to me?"

OFC is the "now" of value — it learns and updates what a stimulus is
currently worth, and it is the mechanism by which the system *reverses*
when contingencies change. VMPFC is the "overall" of value — it holds
the integrated picture that persists across stimuli. The two are
adjacent and reciprocally connected (OFC → VMPFC is one of the
strongest intra-prefrontal coupling priors), and their clinical
syndromes overlap (both produce impaired real-world decision-making),
but they are not the same computation and their configs should not be
merged.

The OFC's signature finding — the one that most cleanly distinguishes
it from VMPFC — is **reversal learning**. An OFC-lesioned animal or
patient can learn a stimulus-reward association as well as an intact
subject; what they cannot do is *update* it when the reward
contingency reverses. They perseverate on the now-wrong stimulus. This
is the OFC-specific deficit, and the reversal_learning feature below is
its config representation. It is the OFC analogue of the VMPFC
somatic-marker finding: both are clinically famous, both point to a
specific computation, and neither is the other.

A NOTE ON AREA 11 vs. AREA 12 (both OFC)
----------------------------------------
Areas 11 and 12 are both orbitofrontal, and both carry SUB_REGION =
"orbitofrontal_cortex". They differ in anterior-posterior position and
in their dominant coupling:

    area 11 (this file)   anterior OFC, more strongly coupled to VLPFC
                          and medial PFC, more involved in abstract/
                          semantic outcome evaluation — "what did this
                          mean?"
    area 12               posterior OFC, more strongly coupled to the
                          amygdala and insula, more involved in
                          visceral/stimulus-driven outcome evaluation
                          — "what did this do to me?"

Both are stimulus-outcome learners; the difference is the abstraction
level of the "outcome" they learn about. The OFC compute sub-region
will combine both areas, with area 11 weighted toward the semantic
side and area 12 toward the visceral side. This file documents area
11's contribution; area 12's will document its own.

IDENTITY
--------
    AREA_ID    = 11
    NAME       = "Brodmann area 11"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "orbitofrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping

This follows the single-system prefrontal pattern introduced by area 9:
SYSTEM is a one-element list, SUB_REGION is a package-level string, no
per-block `sub_region` field.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 11",
        "system": "prefrontal_cortex",
        "sub_region": "orbitofrontal_cortex",
        "grouping": None,
        "location": "the anterior part of the orbital surface of the "
                    "frontal lobe — the gyrus rectus (medial) and the "
                    "medial orbital gyrus (lateral), just anterior to "
                    "area 12 and inferior to area 10 (which wraps the "
                    "frontal pole from above)",
        "cytoarchitecture": "granular cortex; prominent layer IV, "
                            "well-developed layers II-III (the "
                            "association-cortex signature), with a "
                            "distinctive columnar organisation in the "
                            "orbital region that reflects the "
                            "topographic mapping of outcome value",
        "notes": (
            "The anterior orbitofrontal cortex. Its core function is "
            "stimulus-outcome learning: it learns which stimuli "
            "predict which outcomes (reward, punishment, or neutral), "
            "tracks the value of those outcomes as they arrive, and "
            "updates the association when the contingency changes. The "
            "reversal-learning signature is the OFC's most specific "
            "clinical finding: intact learning, failed updating. "
            "Beyond reversal, the OFC evaluates outcomes after the "
            "fact (did the reward match the prediction?), generates "
            "reward predictions (what do I expect to happen?), and "
            "assigns credit to the stimuli that were present when the "
            "outcome occurred. It is reciprocally connected with the "
            "amygdala (stimulus-outcome associations), the ventral "
            "striatum (reward prediction and reward prediction error), "
            "the insula (interoceptive outcome state), and VMPFC "
            "(integrated value). On the left, area 11's outcome "
            "evaluation is more verbally and semantically mediated — "
            "what the outcome *means*, as encoded in words and "
            "concepts — and the valence bias leans toward positive/"
            "approach. On the right, outcome evaluation is more "
            "viscerally and affectively mediated, and the valence bias "
            "leans toward negative/avoidance. The left/right split is "
            "directional, not complementary — the right's area 11 is "
            "threat/visceral-forward, not 'the left's at reduced "
            "weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 11's LEFT_CONFIG is a single flat dict (single-system, single
block — no per-system nesting). The schema is identical to areas 9 and
10; see the area-9 docstring for the schema rationale.

    LEFT_CONFIG = {
        # ---- STRUCTURAL features (equal across hemispheres) ----
        # The OFC's core computations — learning, reversal,
        # prediction, evaluation — are highly conserved. What
        # lateralises is the CONTENT of what is learned and the
        # VALENCE BIAS it takes, not the mechanism itself.
        "reward_prediction":        0.70,   # expecting reward
        "punishment_prediction":    0.70,   # expecting punishment
        "stimulus_outcome_learning":0.75,   # learning which stimulus
                                            # predicts which outcome
        "reversal_learning":        0.80,   # the OFC's signature —
                                            # updating the association
                                            # when the contingency
                                            # reverses; structural
        "outcome_evaluation":       0.75,   # evaluating the outcome
                                            # after it arrives

        # ---- DIRECTIONAL features (lateralised content) ----
        # LEFT bias: positive valence, verbal/semantic reward cues,
        # approach tendency. The mechanism learns both valences, but
        # the left's dominant operating regime is positive/approach,
        # and its cues are more verbally encoded.
        "positive_valence_bias":    0.70,   # positive outcomes
                                            # weighted more heavily
        "negative_valence_bias":    0.45,   # negative outcomes
                                            # weighted less heavily
        "verbal_reward_cue":        0.70,   # reward cues arrive via
                                            # verbal/semantic routes;
                                            # the left's anchor
        "visual_reward_cue":        0.40,   # reward cues via direct
                                            # visual/stimulus routes;
                                            # more right-weighted

        # ---- connectivity priors ----
        "to_amygdala":              0.55,   # stimulus-outcome
                                            # associations; right
                                            # stronger (threat
                                            # learning is right-
                                            # lateralised)
        "to_nucleus_accumbens":     0.75,   # reward prediction and
                                            # reward prediction
                                            # error; left slightly
                                            # stronger (positive-
                                            # reward learning)
        "to_insula":                0.50,   # interoceptive outcome
                                            # state; right stronger
        "to_hippocampus":           0.60,   # contextual modulation
                                            # of outcome learning;
                                            # structural (equal)
        "to_vlpfc":                 0.70,   # coupling to VLPFC for
                                            # stimulus evaluation
                                            # and selection; left
                                            # stronger (semantic
                                            # evaluation)
        "to_vmpfc":                 0.65,   # OFC → VMPFC is the
                                            # value-to-integration
                                            # path; structural
                                            # (equal)
        "to_basal_ganglia":         0.65,   # value → action gating;
                                            # structural (equal)
        "to_anterior_cingulate":    0.55,   # outcome monitoring
                                            # feeds ACC's error
                                            # channel; structural
                                            # (equal)
        "to_commissures":           0.45,   # cross-midline outcome
                                            # exchange; right
                                            # stronger (right's
                                            # threat/visceral
                                            # outcomes need to
                                            # reach the left's
                                            # semantic evaluation
                                            # for narrative
                                            # expression)
    }

    Notes on the weights:
      - The five STRUCTURAL features (reward_prediction,
        punishment_prediction, stimulus_outcome_learning,
        reversal_learning, outcome_evaluation) are the OFC's core
        computations, and they are equal across hemispheres. The OFC
        as a whole computes all of these on both sides.
      - The four DIRECTIONAL features carry the lateralised content:
        positive vs negative valence, verbal vs visual reward cueing.
        They are not "the same computation at different weights" —
        they are different feature extractions with different
        upstream inputs.
      - `reversal_learning: 0.80` is the highest feature weight in
        the file, on either side. The reversal-learning computation
        is the OFC's core function, and its weight should reflect
        that. This is the file's most important number.
      - `to_vlpfc: 0.70` is the file's strongest non-striatal
        connectivity prior. The OFC → VLPFC coupling is how learned
        outcome value reaches the stimulus-selection machinery in
        VLPFC; without it, the OFC learns values but cannot act on
        them. On the left this coupling is stronger because VLPFC
        (Broca's area and area 47) is doing more of the semantic
        stimulus-evaluation work.
      - `to_vmpfc: 0.65` is the value-to-integration path. OFC
        learns per-stimulus value; VMPFC integrates it into the
        overall picture. The structural equality reflects that the
        integration pathway is the same on both sides; only the
        content being integrated differs.
      - All values are plausible priors, not measured constants.
        The key constraints are: (a) structural features are equal
        across hemispheres; (b) directional features directionally
        mirror; (c) reversal_learning is the highest feature weight;
        (d) structural connectivity priors are equal across
        hemispheres.

MIRROR PATTERN
--------------
Area 11's config is a directional mirror with a structural-heavy
profile. The five OFC mechanism features are equal; the four content
features mirror directionally:

    left's area 11                right's area 11
    reward_prediction       0.70  reward_prediction       0.70  (equal)
    punishment_prediction   0.70  punishment_prediction   0.70  (equal)
    stimulus_outcome_learning 0.75
                                  stimulus_outcome_learning 0.75 (equal)
    reversal_learning       0.80  reversal_learning       0.80  (equal)
    outcome_evaluation      0.75  outcome_evaluation      0.75  (equal)
    positive_valence_bias   0.70  positive_valence_bias   0.45
    negative_valence_bias   0.45  negative_valence_bias   0.70
    verbal_reward_cue       0.70  verbal_reward_cue       0.35
    visual_reward_cue       0.40  visual_reward_cue       0.70

    to_amygdala             0.55  to_amygdala             0.70
    to_nucleus_accumbens    0.75  to_nucleus_accumbens    0.65
    to_insula               0.50  to_insula               0.65
    to_hippocampus          0.60  to_hippocampus          0.60  (equal)
    to_vlpfc                0.70  to_vlpfc                0.55
    to_vmpfc                0.65  to_vmpfc                0.65  (equal)
    to_basal_ganglia        0.65  to_basal_ganglia        0.65  (equal)
    to_anterior_cingulate   0.55  to_anterior_cingulate   0.55  (equal)
    to_commissures          0.45  to_commissures          0.55

    The mirror test must check direction on the four directional
    features and the five directional connectivity priors
    (`to_amygdala`, `to_nucleus_accumbens`, `to_insula`, `to_vlpfc`,
    `to_commissures`), and equality on the structural features and
    structural connectivity priors.

    The structural-heavy pattern (five of nine features equal) is the
    same shape as area 10's, but with a different partition: area 10's
    structural features were the *integration* mechanisms; area 11's
    are the *learning* mechanisms. Both sets of mechanisms are
    conserved; only the content of what is learned or integrated
    lateralises.

PREDICTION (TESTABLE)
---------------------
The OFC's reversal-learning signature supports a specific, valence-
lateralised double dissociation:

    OFC lesion, left hemisphere:  impaired reversal of POSITIVE reward
                                  contingencies (patient keeps pursuing
                                  a stimulus that used to give reward
                                  but no longer does); threat-related
                                  reversal is relatively spared.

    OFC lesion, right hemisphere: impaired reversal of PUNISHMENT/
                                  THREAT contingencies (patient keeps
                                  avoiding a stimulus that used to give
                                  punishment but no longer does); reward
                                  reversal is relatively spared.

The non-lateralised part of the prediction is the classic finding:

    ANY significant OFC lesion:   intact initial learning of a
                                  stimulus-outcome association;
                                  severe impairment when the
                                  contingency reverses — the
                                  perseveration that distinguishes
                                  OFC from VMPFC.

Combined, these give the model three testable probes:
    1. Initial learning should be intact on both sides (structural
       features equal).
    2. Reversal should be impaired on both sides (reversal_learning
       equal, both at 0.80).
    3. The CONTENT of the reversal deficit should differ by side —
       left's deficit is on positive/reward reversal, right's on
       negative/threat reversal — because the valence biases and
       cue-route features are lateralised.

That third probe is the one that distinguishes the model from a
generic "OFC = reversal learning" story; it makes a specific claim
about *what* reverses poorly depending on which side is lesioned.

EXPORTS
-------
    from .brodmann_area_11 import BRODMANN_11     # int, == AREA_ID
    from .brodmann_area_11 import ANATOMY
    from .brodmann_area_11 import LEFT_CONFIG
    from .brodmann_area_11 import SYSTEM          # list, ["prefrontal_cortex"]
    from .brodmann_area_11 import SUB_REGION      # str, "orbitofrontal_cortex"
    from .brodmann_area_11 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_11`) — area 11 is a direct child
of brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in OFC, not here.
    - Must not import `prefrontal_cortex/` or `orbitofrontal_cortex/`
      (cycle; the compute imports from here, not the other way round).
    - Must not split into per-system or per-sub-region blocks. Area 11
      is single-system with SUB_REGION set; its config is a single
      flat dict.
    - Must not add a `sub_region` field INSIDE LEFT_CONFIG. The
      package-level SUB_REGION handles the disambiguation.
    - Must not double-count area 11 with area 12. Both are OFC, both
      have SUB_REGION = "orbitofrontal_cortex", but they are separate
      areas with separate configs. Area 11 is the anterior/semantic
      OFC; area 12 is the posterior/visceral OFC. The OFC compute
      sub-region reads both, weighting them by their per-area shares
      (documented separately once both files exist).
    - Must not double-count area 11 with area 10 (VMPFC) or area 25
      (subgenual ACC). Area 11 is stimulus-outcome learning; area 10
      is integrated value + self; area 25 is sustained affect.
      Adjacent anatomically, distinct computationally. Merging any of
      these would erase the OFC/VMPFC/area-25 distinctions that the
      clinical syndromes depend on.
    - Must not import or reference the left hemisphere's area-11
      package (this file is the left one; the right mirror is the
      peer). Cross-midline outcome exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's
      area-11 package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING,
      ANATOMY, same config keys. Only the values differ, and only by
      the directional mirror described above.
"""