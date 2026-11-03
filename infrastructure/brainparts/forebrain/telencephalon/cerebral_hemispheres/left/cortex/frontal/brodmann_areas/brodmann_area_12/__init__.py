"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_12
======================================================================================================================

Brodmann area 12 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 12, says which compute sub-region owns it,
and supplies the per-area weights that the owning sub-region's `encode()`
reads. It defines no classes and no functions; the public surface is the
exports listed under "EXPORTS".

If you are looking for the computation area 12 participates in, it lives
in `.../frontal/cortex/prefrontal_cortex/orbitofrontal_cortex/` — area 12
is the posterior orbitofrontal cortex, and OFC is the stimulus-outcome
learning and outcome-evaluation core of the frontal lobe. This package
is the *label*; the OFC compute sub-region is the *agent*.

AREA 12's PLACE WITHIN THE OFC SUBDIVISION
------------------------------------------
Areas 11 and 12 are the two Brodmann areas of the orbitofrontal cortex,
and they are separated on an anterior-posterior axis by the abstraction
level of the outcomes they evaluate:

    area 11 (anterior)   "what did this mean?" — outcomes evaluated
                         in terms of their semantic/abstract identity;
                         coupled to VLPFC and medial PFC; more
                         conceptual reward/punishment.

    area 12 (posterior)  "what did this do to me?" — outcomes
                         evaluated in terms of their direct sensory/
                         visceral consequences; coupled to amygdala and
                         insula; more stimulus-driven reward/punishment.

Both are stimulus-outcome learners, both compute reversal, both carry
the OFC's signature clinical deficit (intact initial learning, failed
reversal) — but the "outcome" they learn about is at a different level
of abstraction. Area 12's outcomes are more directly the *felt*
consequences of a stimulus (the reward's taste, the punishment's
pain, the autonomic response) rather than its semantic significance.

This distinction is why area 12's amygdala and insula coupling priors
are significantly higher than area 11's — the posterior OFC's job is
to learn stimulus-outcome associations where the outcome is a body
state, and it needs direct lines to the structures that read body
state (insula) and tag threat/reward with affect (amygdala).

OFC vs. VMPFC vs. DLPFC (the framing this file inherits)
--------------------------------------------------------
Same three-pole framing as area 11; documented fully in the area-11
docstrings. Briefly:

    DLPFC      effortful working-memory executive
    OFC        stimulus-outcome learner (11: semantic, 12: visceral)
    VMPFC      integrated value + self

Area 12 is the OFC pole's *visceral* face — the side of OFC that
answers "did this taste good, did it hurt, did it make me flinch?"
rather than "did this mean reward, did this mean punishment?" Both
answers are OFC computations, and they are complementary: the OFC
compute sub-region combines them (with per-area shares, documented
once the OFC sub-region file exists) to produce a full outcome-
evaluation signal.

IDENTITY
--------
    AREA_ID    = 12
    NAME       = "Brodmann area 12"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "orbitofrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping

This follows the single-system prefrontal pattern introduced by area 9:
SYSTEM is a one-element list, SUB_REGION is a package-level string, no
per-block `sub_region` field. The pattern is identical to areas 10 and
11; only the SUB_REGION value differs (both 11 and 12 are
"orbitofrontal_cortex" — that shared value is deliberate and correct:
they are both OFC, and the distinction between them is documented in
ANATOMY and config, not in a finer SUB_REGION granularity).

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 12",
        "system": "prefrontal_cortex",
        "sub_region": "orbitofrontal_cortex",
        "grouping": None,
        "location": "the posterior part of the orbital surface of the "
                    "frontal lobe — the posterior orbital gyrus and "
                    "the lateral orbital gyrus, just posterior to area "
                    "11 and anterior to the insula's anterior limit; "
                    "sits above the olfactory bulb and the orbital "
                    "gyri that receive direct olfactory and gustatory "
                    "input",
        "cytoarchitecture": "granular cortex; prominent layer IV, "
                            "well-developed layers II-III, with a "
                            "slightly less columnar organisation than "
                            "area 11 (reflecting its closer coupling "
                            "to sensory than to association cortex). "
                            "The area's lamination is intermediate "
                            "between typical association cortex and "
                            "the more 'sensory-flavoured' agranular "
                            "cortex of the adjacent anterior insula",
        "notes": (
            "The posterior orbitofrontal cortex, the more "
            "stimulus-driven and visceral of the two OFC areas. Its "
            "core function is stimulus-outcome learning, as with area "
            "11, but the outcomes it learns about are more directly "
            "sensory and bodily: the taste of a food, the smell of a "
            "predator, the autonomic response to a social signal, the "
            "visceral discomfort of a punishment. This makes area 12 "
            "the OFC's interface with the body-state and threat-"
            "detection systems — its coupling to the insula "
            "(interoception) and the amygdala (threat/affect tagging) "
            "is significantly stronger than area 11's. Functionally "
            "the two areas are complementary: area 11 evaluates 'what "
            "did this mean' (semantic/conceptual), area 12 evaluates "
            "'what did this do to me' (visceral/sensory). Both "
            "contribute to the OFC's full outcome-evaluation signal, "
            "and both carry the reversal-learning signature — area 12's "
            "reversal deficits are typically more severe for outcomes "
            "that are tasted, smelled, or felt than for outcomes that "
            "are described. On the left, area 12's outcome evaluation "
            "is more verbally labelled (the patient can describe the "
            "taste or the pain in words), and the valence bias leans "
            "mildly positive; on the right, outcome evaluation is more "
            "directly affective and the valence bias leans more "
            "strongly negative. The left/right split is directional, "
            "not complementary — the right's area 12 is more "
            "threat/visceral-forward, not 'the left's at reduced "
            "weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 12's LEFT_CONFIG is a single flat dict (single-system, single
block — no per-system nesting). The schema is identical to areas 9,
10, and 11; see the area-9 docstring for the schema rationale.

    LEFT_CONFIG = {
        # ---- STRUCTURAL features (equal across hemispheres) ----
        # The OFC's core computations are conserved, as with area 11.
        # The five mechanism features below are the same features
        # area 11 carries (reward_prediction, punishment_prediction,
        # stimulus_outcome_learning, reversal_learning,
        # outcome_evaluation), and they are equal across hemispheres
        # and across the two OFC areas. Both 11 and 12 compute these;
        # the difference is which *outcomes* they compute them about.
        "reward_prediction":        0.70,   # structural
        "punishment_prediction":    0.70,   # structural
        "stimulus_outcome_learning":0.75,   # structural
        "reversal_learning":        0.80,   # structural — the OFC's
                                            # signature, unchanged
                                            # from area 11
        "outcome_evaluation":       0.75,   # structural

        # ---- AREA-12 SPECIFIC features (structural across
        # hemispheres; the 11-vs-12 difference is what's shown here) ----
        # These are the "what did this do to me" features that
        # distinguish area 12 from area 11. They are STRUCTURAL
        # (equal across hemispheres) — the visceral/sensory character
        # of area 12's outcomes does not lateralise; only the
        # valence and cue route do.
        "taste_reward_evaluation":  0.70,   # the taste of a food as
                                            # reward — area 12 receives
                                            # direct gustatory input
        "smell_threat_evaluation":  0.65,   # the smell of a threat —
                                            # area 12 receives direct
                                            # olfactory input, which is
                                            # the fastest threat-
                                            # detection channel
        "visceral_punishment_evaluation": 0.70,
                                            # the felt discomfort of a
                                            # punishment (autonomic,
                                            # somatic)
        "social_visceral_evaluation": 0.55, # visceral response to
                                            # social signals (the
                                            # 'gut feeling' about a
                                            # person or a scene)

        # ---- DIRECTIONAL features (lateralised content) ----
        # LEFT bias: mildly positive valence, verbal labelling of
        # visceral states. The mechanism evaluates both valences; the
        # left's operating regime leans mildly positive, and its
        # evaluations are more verbally labelled.
        "positive_valence_bias":    0.60,   # mildly positive
                                            # (area 11's is 0.70;
                                            # area 12 leans less
                                            # positive than area 11
                                            # because its outcomes
                                            # include punishment)
        "negative_valence_bias":    0.50,   # mildly negative;
                                            # area 11's is 0.45;
                                            # area 12 is more
                                            # punishment-aware
        "verbal_outcome_label":     0.70,   # labeling the visceral
                                            # outcome in words —
                                            # "that tasted bitter",
                                            # "that stung" — the
                                            # left's anchor feature
                                            # for area 12; the right
                                            # has lower
        "direct_visceral_cue":      0.55,   # unlabelled direct
                                            # visceral response —
                                            # more right-weighted

        # ---- connectivity priors ----
        # Area 12's signature connectivity is the amygdala and insula
        # coupling — these are the body-state and threat-tagging
        # partners that make its outcomes visceral rather than
        # semantic. Both are significantly higher than area 11's.
        "to_amygdala":              0.80,   # UP significantly from
                                            # area 11's 0.55; the
                                            # strongest OFC-amygdala
                                            # coupling — area 12 is
                                            # the OFC's threat-
                                            # detection interface
        "to_insula":                0.80,   # UP significantly from
                                            # area 11's 0.50; the
                                            # strongest OFC-insula
                                            # coupling — area 12 is
                                            # the OFC's interoceptive
                                            # interface
        "to_nucleus_accumbens":     0.65,   # reward prediction; lower
                                            # than area 11's 0.75
                                            # because area 12's
                                            # reward is more sensory
                                            # than conceptual
        "to_hippocampus":           0.55,   # structural (equal)
        "to_vlpfc":                 0.45,   # DOWN from area 11's
                                            # 0.70 — area 12's
                                            # outcomes are less
                                            # semantic, so VLPFC
                                            # coupling is lower;
                                            # still substantial for
                                            # affectively-labelled
                                            # outcomes
        "to_vmpfc":                 0.65,   # structural (equal) —
                                            # OFC → VMPFC is the
                                            # value-to-integration
                                            # path; both OFC areas
                                            # feed it
        "to_basal_ganglia":         0.65,   # structural (equal)
        "to_anterior_cingulate":    0.55,   # structural (equal)
        "to_commissures":           0.45,   # structural (equal on
                                            # the left; the right's
                                            # is higher because the
                                            # right's visceral
                                            # outcomes have to
                                            # reach the left's
                                            # verbal labelling for
                                            # narrative expression)
    }

    Notes on the weights:
      - The five OFC mechanism features (reward_prediction,
        punishment_prediction, stimulus_outcome_learning,
        reversal_learning, outcome_evaluation) are equal to area 11's
        values on both sides. The OFC as a whole computes the same
        mechanisms regardless of which area is doing the work; the
        sub-division is about WHAT the outcomes are, not what
        computation is performed on them.
      - The four area-12-specific features (taste_reward_evaluation,
        smell_threat_evaluation, visceral_punishment_evaluation,
        social_visceral_evaluation) are STRUCTURAL across
        hemispheres, because the visceral/sensory character of
        area 12's outcomes does not lateralise. The left and right
        area 12 both evaluate tastes, smells, visceral discomfort,
        and social gut feelings. What lateralises is the labelling
        and the valence bias, not the evaluation itself.
      - The four directional features (positive_valence_bias,
        negative_valence_bias, verbal_outcome_label,
        direct_visceral_cue) carry the lateralised content. Note that
        the valence weights are different from area 11's: area 11
        was 0.70/0.45 (strongly positive-leaning); area 12 is
        0.60/0.50 (mildly positive-leaning, more punishment-aware).
        This is because area 12's outcomes include tastes and
        smells, which are more evenly balanced across valences than
        area 11's more abstract reward/punishment outcomes. The
        positive-leaning bias is still there, just less extreme.
      - `to_amygdala: 0.80` and `to_insula: 0.80` are the two
        highest connectivity priors in the file, and both are
        substantially higher than the corresponding priors in area 11
        (0.55 and 0.50). This is the config-level expression of the
        OFC sub-division's functional separation: area 12 is the
        OFC's body-state and threat-tagging interface, and its
        amygdala/insula coupling reflects that.
      - `to_vlpfc: 0.45` is much lower than area 11's 0.70. VLPFC
        coupling serves semantic stimulus evaluation, which is area
        11's role more than area 12's. Area 12 still has some VLPFC
        coupling because it labels visceral outcomes affectively
        (which uses VLPFC's semantic machinery for the labelling
        itself), but the dominant coupling routes are amygdala and
        insula, not VLPFC.
      - `to_commissures: 0.45` is structural and equal to area 11's.
        The left's visceral outcomes do not need to cross the
        midline more than the right's — the direction is opposite
        (right's visceral outcomes need to reach left's verbal
        labelling), which is why the right's is higher.
      - All values are plausible priors, not measured constants.
        The key constraints are: (a) OFC mechanism features equal
        across hemispheres and equal to area 11's; (b) area-12
        specific features structural across hemispheres;
        (c) directional features directionally mirror; (d)
        amygdala/insula coupling substantially higher than area 11's.

MIRROR PATTERN
--------------
Area 12's config is a directional mirror with the structural-heavy
profile preserved. Structural features (the five OFC mechanisms plus
the four area-12-specific features) are equal across hemispheres;
directional features (four) and directional connectivity priors (three
of nine) mirror:

    left's area 12                right's area 12
    --- OFC mechanism features (structural, equal to area 11) ---
    reward_prediction       0.70  (equal)
    punishment_prediction   0.70  (equal)
    stimulus_outcome_learning 0.75 (equal)
    reversal_learning       0.80  (equal)
    outcome_evaluation      0.75  (equal)
    --- Area-12-specific features (structural) ---
    taste_reward_evaluation 0.70  (equal)
    smell_threat_evaluation 0.65  (equal)
    visceral_punishment_evaluation 0.70 (equal)
    social_visceral_evaluation 0.55 (equal)
    --- Directional features ---
    positive_valence_bias   0.60  positive_valence_bias   0.50
    negative_valence_bias   0.50  negative_valence_bias   0.65
    verbal_outcome_label    0.70  verbal_outcome_label    0.40
    direct_visceral_cue     0.55  direct_visceral_cue     0.75
    --- Connectivity priors ---
    to_amygdala             0.80  to_amygdala             0.85
    to_insula               0.80  to_insula               0.85
    to_nucleus_accumbens    0.65  to_nucleus_accumbens    0.55
    to_hippocampus          0.55  to_hippocampus          0.55  (equal)
    to_vlpfc                0.45  to_vlpfc                0.35
    to_vmpfc                0.65  to_vmpfc                0.65  (equal)
    to_basal_ganglia        0.65  to_basal_ganglia        0.65  (equal)
    to_anterior_cingulate   0.55  to_anterior_cingulate   0.55  (equal)
    to_commissures          0.45  to_commissures          0.55

    The mirror test must check:
    - equality on the nine structural features;
    - direction on the four directional features and the four
      directional connectivity priors (to_amygdala, to_insula,
      to_nucleus_accumbens, to_vlpfc, to_commissures — five
      directional);
    - equality on the four structural connectivity priors
      (to_hippocampus, to_vmpfc, to_basal_ganglia,
      to_anterior_cingulate);
    - AND the cross-area comparison to area 11: the five OFC
      mechanism features should be equal between area 11 and area
      12, while the area-12-specific features are unique to area 12
      (area 11 has verbal_reward_cue / visual_reward_cue, which are
      not present in area 12).

    That last comparison (area 11 vs area 12) is the one that
    distinguishes OFC's internal structure from its external mirror.
    Both areas compute OFC mechanisms equally; they differ in what
    outcomes they apply the mechanisms to. The mirror test should
    check that the OFC mechanism features are equal across the two
    areas (they're the shared substrate), and that the outcome-
    specific features are disjoint (area 11 has semantic cues,
    area 12 has visceral cues, and neither has the other's).

PREDICTION (TESTABLE)
---------------------
Area 12's reversal-learning signature is more stimulus-specific
than area 11's, and this supports a specific clinical dissociation:

    area 12 lesion (either side):  reversal of SENSORY outcome
                                   contingencies (taste, smell,
                                   visceral discomfort) is impaired;
                                   reversal of VERBAL/CONCEPTUAL
                                   outcome contingencies (described
                                   rewards, stated punishments) is
                                   relatively spared.

    area 11 lesion (either side):  reversal of VERBAL/CONCEPTUAL
                                   outcome contingencies is impaired;
                                   reversal of SENSORY outcome
                                   contingencies is relatively spared.

This is a within-OFC dissociation that the model should produce
because of the two areas' differing outcome-specific features. It is
sharper than the classic "OFC lesion impairs reversal" story because
it specifies *which* outcomes reverse poorly depending on *which*
OFC area is lesioned, not just which hemisphere.

The hemisphere-level valence dissociation is milder for area 12 than
for area 11 (the valence biases are closer to 0.5/0.5 for area 12),
because area 12's outcomes span both valences more evenly. The
prediction from the left area-12 file is therefore a *weaker*
lateralisation of valence-driven reversal than area 11 produces —
both hemispheres of area 12 should show roughly balanced positive/
negative reversal deficits, with only a mild leftward tilt toward
positive-outcome reversal and a mild rightward tilt toward
negative-outcome reversal. If the model produces a strong
lateralisation of area-12 reversal, that's a signal that area 11's
pattern has been over-transferred.

EXPORTS
-------
    from .brodmann_area_12 import BRODMANN_12     # int, == AREA_ID
    from .brodmann_area_12 import ANATOMY
    from .brodmann_area_12 import LEFT_CONFIG
    from .brodmann_area_12 import SYSTEM          # list, ["prefrontal_cortex"]
    from .brodmann_area_12 import SUB_REGION      # str, "orbitofrontal_cortex"
    from .brodmann_area_12 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_12`) — area 12 is a direct
child of brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in OFC, not here.
    - Must not import `prefrontal_cortex/` or `orbitofrontal_cortex/`
      (cycle; the compute imports from here, not the other way round).
    - Must not split into per-system or per-sub-region blocks. Area 12
      is single-system with SUB_REGION set; its config is a single
      flat dict.
    - Must not add a `sub_region` field INSIDE LEFT_CONFIG. The
      package-level SUB_REGION handles the disambiguation.
    - Must not double-count area 12 with area 11. Both are OFC, both
      have SUB_REGION = "orbitofrontal_cortex", but they are separate
      areas with separate configs and different outcome-specific
      features (area 11: semantic cues; area 12: visceral cues).
      The OFC compute sub-region reads both.
    - Must not double-count area 12 with area 10 (VMPFC) or area 25
      (subgenual ACC). Area 12 is posterior-OFC stimulus-outcome
      learning; area 10 is integrated value + self; area 25 is
      sustained affect. Adjacent anatomically, distinct
      computationally.
    - Must not import or reference the left hemisphere's area-12
      package (this file is the left one; the right mirror is the
      peer). Cross-midline outcome exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's
      area-12 package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING,
      ANATOMY, same config keys. Only the values differ, and only by
      the directional mirror described above.
    - Must not duplicate area 11's outcome-specific features. Area 11
      carries verbal_reward_cue and visual_reward_cue (semantic
      routes to reward); area 12 carries taste_reward_evaluation,
      smell_threat_evaluation, visceral_punishment_evaluation, and
      social_visceral_evaluation (visceral routes to outcome). These
      feature sets are disjoint by design — each area carries the
      outcome-specific features that match its dominant connectivity.
      If a future change wants to add a feature to one area that
      matches the other area's profile, that is a signal that the
      area's identity is being blurred and should be re-examined, not
      that the feature should be added.
"""