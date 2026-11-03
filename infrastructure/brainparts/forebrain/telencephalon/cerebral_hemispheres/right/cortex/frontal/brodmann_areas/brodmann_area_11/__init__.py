"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_11
=======================================================================================================================

Brodmann area 11 — right hemisphere.

Mirror of the left area-11 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 11, says
which compute sub-region owns it, and supplies the per-area weights that
the owning sub-region's `encode()` reads. It defines no classes and no
functions; the public surface is the exports listed under "EXPORTS".

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
adjacent and reciprocally connected, and their clinical syndromes
overlap, but they are not the same computation. The OFC's signature
finding — reversal learning — is documented in detail on the left
area-11 docstring; it is not repeated here, but it is the same
computation on both sides. `reversal_learning: 0.80` is the highest
feature weight in the file on the right, exactly as on the left, because
reversal learning as a *computation* is not lateralised — only the
*content* of what reverses poorly is.

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

On the RIGHT, this anterior/posterior distinction interacts with the
hemisphere's affective bias: the right's area 11 is still the anterior/
semantic OFC (that anatomical fact does not lateralise), but its
semantic evaluation is more affectively coloured than the left's
(verbal-semantic vs affective-semantic), and its posterior neighbour
(area 12) has a stronger visceral grip than the left's. The OFC compute
sub-region will combine both areas with per-area shares; this file
documents area 11's contribution.

IDENTITY
--------
    AREA_ID    = 11
    NAME       = "Brodmann area 11"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "orbitofrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping

The single-system prefrontal pattern (SYSTEM one-element list, SUB_REGION
package-level string, no per-block `sub_region` field) is identical to
the left's — it is the shape introduced by area 9 and reused by areas 10,
11, 12, 46. Lateralisation does not change the shape, only the values.

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
            "stimulus-outcome learning: learning which stimuli predict "
            "which outcomes, tracking outcome value as it arrives, and "
            "updating the association when the contingency reverses. "
            "The reversal-learning signature is the OFC's most specific "
            "clinical finding: intact learning, failed updating. On "
            "the RIGHT, outcome evaluation is more viscerally and "
            "affectively mediated than on the left, and the valence "
            "bias leans toward negative/avoidance. The right's area 11 "
            "still does semantic/abstract evaluation (it is the anterior "
            "OFC on both sides), but its semantics are more affectively "
            "coloured — 'what this meant' is more often 'how this felt' "
            "than on the left, where it is more often 'what this was "
            "called'. The left/right split is directional, not "
            "complementary — the right's area 11 is threat/visceral-"
            "forward, not 'the left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 11's RIGHT_CONFIG is a single flat dict (single-system, single
block — no per-system nesting).

    RIGHT_CONFIG = {
        # ---- STRUCTURAL features (equal across hemispheres) ----
        # The OFC's core computations — learning, reversal,
        # prediction, evaluation — are highly conserved. What
        # lateralises is the CONTENT of what is learned and the
        # VALENCE BIAS it takes, not the mechanism itself.
        "reward_prediction":        0.70,   # STRUCTURAL (equal)
        "punishment_prediction":    0.70,   # STRUCTURAL (equal)
        "stimulus_outcome_learning":0.75,   # STRUCTURAL (equal)
        "reversal_learning":        0.80,   # STRUCTURAL (equal) —
                                            # the OFC's signature,
                                            # unchanged on the right
        "outcome_evaluation":       0.75,   # STRUCTURAL (equal)

        # ---- DIRECTIONAL features (lateralised content) ----
        # RIGHT bias: negative valence, visceral/direct reward cues,
        # avoidance tendency. The mechanism learns both valences, but
        # the right's dominant operating regime is negative/avoidance,
        # and its cues are more direct/visceral.
        "positive_valence_bias":    0.45,   # DOWN from left's 0.70
        "negative_valence_bias":    0.70,   # UP from left's 0.45;
                                            # the right's anchor
        "verbal_reward_cue":        0.35,   # DOWN from left's 0.70
        "visual_reward_cue":        0.70,   # UP from left's 0.40;
                                            # direct stimulus-driven
                                            # reward cues are the
                                            # right's route

        # ---- connectivity priors ----
        "to_amygdala":              0.70,   # UP from left's 0.55 —
                                            # stimulus-outcome
                                            # associations for threat
                                            # are stronger on the
                                            # right
        "to_nucleus_accumbens":     0.65,   # DOWN from left's 0.75 —
                                            # positive-reward
                                            # prediction is more
                                            # left-weighted; the
                                            # right's NAcc coupling
                                            # serves threat/avoidance
                                            # prediction
        "to_insula":                0.65,   # UP from left's 0.50 —
                                            # interoceptive outcome
                                            # state is stronger on
                                            # the right
        "to_hippocampus":           0.60,   # STRUCTURAL (equal)
        "to_vlpfc":                 0.55,   # DOWN from left's 0.70 —
                                            # VLPFC coupling serves
                                            # semantic stimulus
                                            # evaluation; left-
                                            # weighted, but still
                                            # substantial on the
                                            # right for affective-
                                            # semantic evaluation
        "to_vmpfc":                 0.65,   # STRUCTURAL (equal) —
                                            # OFC → VMPFC is the
                                            # value-to-integration
                                            # path; the path is the
                                            # same on both sides
        "to_basal_ganglia":         0.65,   # STRUCTURAL (equal)
        "to_anterior_cingulate":    0.55,   # STRUCTURAL (equal)
        "to_commissures":           0.55,   # UP from left's 0.45 —
                                            # the right's threat/
                                            # visceral outcomes
                                            # need to reach the
                                            # left's semantic
                                            # evaluation for
                                            # narrative expression
                                            # ('I felt it was wrong
                                            # but couldn't say why')
    }

    Notes on the weights:
      - The five STRUCTURAL features are the OFC's core mechanisms and
        are equal across hemispheres. This is a genuine claim about
        OFC: reward prediction, punishment prediction, stimulus-outcome
        learning, reversal, and outcome evaluation are not lateralised.
        Only the *content* is.
      - `reversal_learning: 0.80` remains the highest feature weight in
        the file on the right. The clinical picture is that both sides
        produce reversal deficits when lesioned; the *content* of what
        reverses poorly differs, not the severity. The weight reflects
        the severity side of that, and the valence/cue features reflect
        the content side.
      - The four DIRECTIONAL features carry the content lateralisation:
        positive vs negative valence (0.70/0.45 on the right vs
        0.70/0.45 inverted on the left), verbal vs visual reward cue
        (0.70/0.40 inverted). These are different feature extractions,
        not the same feature at different weights.
      - Three lateralised connectivity priors, all directional:
            to_amygdala       UP   (0.55 → 0.70)
            to_insula         UP   (0.50 → 0.65)
            to_commissures    UP   (0.45 → 0.55)
            to_nucleus_accumbens DOWN (0.75 → 0.65)
            to_vlpfc          DOWN (0.70 → 0.55)
        The ups are the right's threat/visceral/affective routes; the
        downs are the left-weighted reward-semantic routes.
      - `to_vmpfc: 0.65` is structural and equal across hemispheres.
        The OFC → VMPFC integration path is the same on both sides;
        only the content being integrated differs. This is the same
        structure/value split that area 10's pair used (integration
        structural, content lateralised).
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) structural features equal across
        hemispheres; (b) directional features directionally mirror;
        (c) reversal_learning highest feature weight on both sides;
        (d) structural connectivity priors equal across hemispheres.

MIRROR PATTERN
--------------
Area 11's config is a directional mirror with the structural-heavy
profile preserved. The five OFC mechanism features are equal; the four
content features mirror directionally:

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
    structural connectivity priors (five of nine features; four of
    nine connectivity priors).

    The structural-heavy shape mirrors area 10's: five structural
    features, four directional features, four structural connectivity
    priors, five directional connectivity priors. The partition (which
    keys are structural vs directional) is what the mirror test needs
    to know, not the overall "mirror" intent.

PREDICTION (TESTABLE)
---------------------
The OFC's reversal-learning signature supports the same valence-
lateralised double dissociation that the left area-11 docstring
documents, now stated from the right side:

    OFC lesion, right hemisphere: impaired reversal of PUNISHMENT/
                                  THREAT contingencies (patient keeps
                                  avoiding a stimulus that used to give
                                  punishment but no longer does);
                                  reward reversal is relatively spared.
                                  On the right, the deficit is
                                  accentuated because the right's
                                  valence bias is threat-forward
                                  (0.70 negative vs 0.45 positive),
                                  so the reversal mechanism is
                                  operating in its dominant regime
                                  and its failure is most visible
                                  there.

    OFC lesion, left hemisphere:  impaired reversal of POSITIVE reward
                                  contingencies; threat-related
                                  reversal is relatively spared.

The non-lateralised part (intact initial learning, impaired reversal on
both sides) is the same as on the left. The lateralised part (which
content reverses poorly) is the right's signature: negative/threat
reversal is the right's dominant failure mode, and on the right that
failure is more clinically visible than the left's positive-reward
failure because the right's operating regime is already threat-
weighted.

EXPORTS
-------
    from .brodmann_area_11 import BRODMANN_11     # int, == AREA_ID
    from .brodmann_area_11 import ANATOMY
    from .brodmann_area_11 import RIGHT_CONFIG
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
    - Must not add a `sub_region` field INSIDE RIGHT_CONFIG. The
      package-level SUB_REGION handles the disambiguation.
    - Must not double-count area 11 with area 12. Both are OFC, both
      have SUB_REGION = "orbitofrontal_cortex", but they are separate
      areas with separate configs. Area 11 is the anterior/semantic
      OFC; area 12 is the posterior/visceral OFC.
    - Must not double-count area 11 with area 10 (VMPFC) or area 25
      (subgenual ACC). Area 11 is stimulus-outcome learning; area 10
      is integrated value + self; area 25 is sustained affect.
      Adjacent anatomically, distinct computationally.
    - Must not import or reference the left hemisphere's area-11
      package. Cross-midline outcome exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The right's higher `to_commissures: 0.55` prior is the
      baseline for "the right's threat/visceral outcomes have to
      reach the left's semantic evaluation for narrative expression";
      direct registry access would bypass the commissural delay that
      gives that handoff its behavioural signature.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-11
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only by the
      directional mirror described above.
""""""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_11
=======================================================================================================================

Brodmann area 11 — right hemisphere.

Mirror of the left area-11 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 11, says
which compute sub-region owns it, and supplies the per-area weights that
the owning sub-region's `encode()` reads. It defines no classes and no
functions; the public surface is the exports listed under "EXPORTS".

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
adjacent and reciprocally connected, and their clinical syndromes
overlap, but they are not the same computation. The OFC's signature
finding — reversal learning — is documented in detail on the left
area-11 docstring; it is not repeated here, but it is the same
computation on both sides. `reversal_learning: 0.80` is the highest
feature weight in the file on the right, exactly as on the left, because
reversal learning as a *computation* is not lateralised — only the
*content* of what reverses poorly is.

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

On the RIGHT, this anterior/posterior distinction interacts with the
hemisphere's affective bias: the right's area 11 is still the anterior/
semantic OFC (that anatomical fact does not lateralise), but its
semantic evaluation is more affectively coloured than the left's
(verbal-semantic vs affective-semantic), and its posterior neighbour
(area 12) has a stronger visceral grip than the left's. The OFC compute
sub-region will combine both areas with per-area shares; this file
documents area 11's contribution.

IDENTITY
--------
    AREA_ID    = 11
    NAME       = "Brodmann area 11"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "orbitofrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping

The single-system prefrontal pattern (SYSTEM one-element list, SUB_REGION
package-level string, no per-block `sub_region` field) is identical to
the left's — it is the shape introduced by area 9 and reused by areas 10,
11, 12, 46. Lateralisation does not change the shape, only the values.

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
            "stimulus-outcome learning: learning which stimuli predict "
            "which outcomes, tracking outcome value as it arrives, and "
            "updating the association when the contingency reverses. "
            "The reversal-learning signature is the OFC's most specific "
            "clinical finding: intact learning, failed updating. On "
            "the RIGHT, outcome evaluation is more viscerally and "
            "affectively mediated than on the left, and the valence "
            "bias leans toward negative/avoidance. The right's area 11 "
            "still does semantic/abstract evaluation (it is the anterior "
            "OFC on both sides), but its semantics are more affectively "
            "coloured — 'what this meant' is more often 'how this felt' "
            "than on the left, where it is more often 'what this was "
            "called'. The left/right split is directional, not "
            "complementary — the right's area 11 is threat/visceral-"
            "forward, not 'the left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 11's RIGHT_CONFIG is a single flat dict (single-system, single
block — no per-system nesting).

    RIGHT_CONFIG = {
        # ---- STRUCTURAL features (equal across hemispheres) ----
        # The OFC's core computations — learning, reversal,
        # prediction, evaluation — are highly conserved. What
        # lateralises is the CONTENT of what is learned and the
        # VALENCE BIAS it takes, not the mechanism itself.
        "reward_prediction":        0.70,   # STRUCTURAL (equal)
        "punishment_prediction":    0.70,   # STRUCTURAL (equal)
        "stimulus_outcome_learning":0.75,   # STRUCTURAL (equal)
        "reversal_learning":        0.80,   # STRUCTURAL (equal) —
                                            # the OFC's signature,
                                            # unchanged on the right
        "outcome_evaluation":       0.75,   # STRUCTURAL (equal)

        # ---- DIRECTIONAL features (lateralised content) ----
        # RIGHT bias: negative valence, visceral/direct reward cues,
        # avoidance tendency. The mechanism learns both valences, but
        # the right's dominant operating regime is negative/avoidance,
        # and its cues are more direct/visceral.
        "positive_valence_bias":    0.45,   # DOWN from left's 0.70
        "negative_valence_bias":    0.70,   # UP from left's 0.45;
                                            # the right's anchor
        "verbal_reward_cue":        0.35,   # DOWN from left's 0.70
        "visual_reward_cue":        0.70,   # UP from left's 0.40;
                                            # direct stimulus-driven
                                            # reward cues are the
                                            # right's route

        # ---- connectivity priors ----
        "to_amygdala":              0.70,   # UP from left's 0.55 —
                                            # stimulus-outcome
                                            # associations for threat
                                            # are stronger on the
                                            # right
        "to_nucleus_accumbens":     0.65,   # DOWN from left's 0.75 —
                                            # positive-reward
                                            # prediction is more
                                            # left-weighted; the
                                            # right's NAcc coupling
                                            # serves threat/avoidance
                                            # prediction
        "to_insula":                0.65,   # UP from left's 0.50 —
                                            # interoceptive outcome
                                            # state is stronger on
                                            # the right
        "to_hippocampus":           0.60,   # STRUCTURAL (equal)
        "to_vlpfc":                 0.55,   # DOWN from left's 0.70 —
                                            # VLPFC coupling serves
                                            # semantic stimulus
                                            # evaluation; left-
                                            # weighted, but still
                                            # substantial on the
                                            # right for affective-
                                            # semantic evaluation
        "to_vmpfc":                 0.65,   # STRUCTURAL (equal) —
                                            # OFC → VMPFC is the
                                            # value-to-integration
                                            # path; the path is the
                                            # same on both sides
        "to_basal_ganglia":         0.65,   # STRUCTURAL (equal)
        "to_anterior_cingulate":    0.55,   # STRUCTURAL (equal)
        "to_commissures":           0.55,   # UP from left's 0.45 —
                                            # the right's threat/
                                            # visceral outcomes
                                            # need to reach the
                                            # left's semantic
                                            # evaluation for
                                            # narrative expression
                                            # ('I felt it was wrong
                                            # but couldn't say why')
    }

    Notes on the weights:
      - The five STRUCTURAL features are the OFC's core mechanisms and
        are equal across hemispheres. This is a genuine claim about
        OFC: reward prediction, punishment prediction, stimulus-outcome
        learning, reversal, and outcome evaluation are not lateralised.
        Only the *content* is.
      - `reversal_learning: 0.80` remains the highest feature weight in
        the file on the right. The clinical picture is that both sides
        produce reversal deficits when lesioned; the *content* of what
        reverses poorly differs, not the severity. The weight reflects
        the severity side of that, and the valence/cue features reflect
        the content side.
      - The four DIRECTIONAL features carry the content lateralisation:
        positive vs negative valence (0.70/0.45 on the right vs
        0.70/0.45 inverted on the left), verbal vs visual reward cue
        (0.70/0.40 inverted). These are different feature extractions,
        not the same feature at different weights.
      - Three lateralised connectivity priors, all directional:
            to_amygdala       UP   (0.55 → 0.70)
            to_insula         UP   (0.50 → 0.65)
            to_commissures    UP   (0.45 → 0.55)
            to_nucleus_accumbens DOWN (0.75 → 0.65)
            to_vlpfc          DOWN (0.70 → 0.55)
        The ups are the right's threat/visceral/affective routes; the
        downs are the left-weighted reward-semantic routes.
      - `to_vmpfc: 0.65` is structural and equal across hemispheres.
        The OFC → VMPFC integration path is the same on both sides;
        only the content being integrated differs. This is the same
        structure/value split that area 10's pair used (integration
        structural, content lateralised).
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) structural features equal across
        hemispheres; (b) directional features directionally mirror;
        (c) reversal_learning highest feature weight on both sides;
        (d) structural connectivity priors equal across hemispheres.

MIRROR PATTERN
--------------
Area 11's config is a directional mirror with the structural-heavy
profile preserved. The five OFC mechanism features are equal; the four
content features mirror directionally:

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
    structural connectivity priors (five of nine features; four of
    nine connectivity priors).

    The structural-heavy shape mirrors area 10's: five structural
    features, four directional features, four structural connectivity
    priors, five directional connectivity priors. The partition (which
    keys are structural vs directional) is what the mirror test needs
    to know, not the overall "mirror" intent.

PREDICTION (TESTABLE)
---------------------
The OFC's reversal-learning signature supports the same valence-
lateralised double dissociation that the left area-11 docstring
documents, now stated from the right side:

    OFC lesion, right hemisphere: impaired reversal of PUNISHMENT/
                                  THREAT contingencies (patient keeps
                                  avoiding a stimulus that used to give
                                  punishment but no longer does);
                                  reward reversal is relatively spared.
                                  On the right, the deficit is
                                  accentuated because the right's
                                  valence bias is threat-forward
                                  (0.70 negative vs 0.45 positive),
                                  so the reversal mechanism is
                                  operating in its dominant regime
                                  and its failure is most visible
                                  there.

    OFC lesion, left hemisphere:  impaired reversal of POSITIVE reward
                                  contingencies; threat-related
                                  reversal is relatively spared.

The non-lateralised part (intact initial learning, impaired reversal on
both sides) is the same as on the left. The lateralised part (which
content reverses poorly) is the right's signature: negative/threat
reversal is the right's dominant failure mode, and on the right that
failure is more clinically visible than the left's positive-reward
failure because the right's operating regime is already threat-
weighted.

EXPORTS
-------
    from .brodmann_area_11 import BRODMANN_11     # int, == AREA_ID
    from .brodmann_area_11 import ANATOMY
    from .brodmann_area_11 import RIGHT_CONFIG
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
    - Must not add a `sub_region` field INSIDE RIGHT_CONFIG. The
      package-level SUB_REGION handles the disambiguation.
    - Must not double-count area 11 with area 12. Both are OFC, both
      have SUB_REGION = "orbitofrontal_cortex", but they are separate
      areas with separate configs. Area 11 is the anterior/semantic
      OFC; area 12 is the posterior/visceral OFC.
    - Must not double-count area 11 with area 10 (VMPFC) or area 25
      (subgenual ACC). Area 11 is stimulus-outcome learning; area 10
      is integrated value + self; area 25 is sustained affect.
      Adjacent anatomically, distinct computationally.
    - Must not import or reference the left hemisphere's area-11
      package. Cross-midline outcome exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The right's higher `to_commissures: 0.55` prior is the
      baseline for "the right's threat/visceral outcomes have to
      reach the left's semantic evaluation for narrative expression";
      direct registry access would bypass the commissural delay that
      gives that handoff its behavioural signature.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-11
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only by the
      directional mirror described above.
"""