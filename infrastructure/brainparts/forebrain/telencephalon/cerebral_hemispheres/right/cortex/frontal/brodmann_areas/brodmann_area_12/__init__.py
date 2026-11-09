"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_12
=======================================================================================================================

Brodmann area 12 — right hemisphere.

Mirror of the left area-12 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 12, says
which compute sub-region owns it, and supplies the per-area weights that
the owning sub-region's `encode()` reads. It defines no classes and no
functions; the public surface is the exports listed under "EXPORTS".

If you are looking for the computation area 12 participates in, it lives
in `.../frontal/cortex/prefrontal_cortex/orbitofrontal_cortex/` — area 12
is the posterior orbitofrontal cortex, and OFC is the stimulus-outcome
learning and outcome-evaluation core of the frontal lobe. This package
is the *label*; the OFC compute sub-region is the *agent*.

AREA 12's PLACE WITHIN THE OFC SUBDIVISION
------------------------------------------
Areas 11 and 12 are the two Brodmann areas of the orbitofrontal cortex,
separated on an anterior-posterior axis by the abstraction level of the
outcomes they evaluate:

    area 11 (anterior)   "what did this mean?" — outcomes evaluated
                         in terms of their semantic/abstract identity;
                         coupled to VLPFC and medial PFC.
    area 12 (posterior)  "what did this do to me?" — outcomes
                         evaluated in terms of their direct sensory/
                         visceral consequences; coupled to amygdala
                         and insula.

Both are stimulus-outcome learners, both compute reversal, both carry
the OFC's signature clinical deficit. On the RIGHT, the visceral
character of area 12's outcomes is expressed more strongly than on the
left: the right's area 12 has the strongest amygdala and insula
coupling in the entire frontal registry, and its valence bias leans
more strongly toward threat/avoidance. The anterior/posterior
anatomical split (11 = semantic, 12 = visceral) does not lateralise —
it is the same on both hemispheres — but the intensity of the visceral
evaluation and its threat-weighted colour do.

OFC vs. VMPFC vs. DLPFC (the framing this file inherits)
--------------------------------------------------------
Same three-pole framing as area 11; documented fully in the area-11
docstrings. Briefly:

    DLPFC      effortful working-memory executive
    OFC        stimulus-outcome learner (11: semantic, 12: visceral)
    VMPFC      integrated value + self

Area 12 is the OFC pole's *visceral* face — the side of OFC that
answers "did this taste good, did it hurt, did it make me flinch?"
rather than "did this mean reward, did this mean punishment?"

IDENTITY
--------
    AREA_ID    = 12
    NAME       = "Brodmann area 12"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "orbitofrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping

The single-system prefrontal pattern (SYSTEM one-element list, SUB_REGION
package-level string, no per-block `sub_region` field) is identical to
the left's. Both 11 and 12 share SUB_REGION = "orbitofrontal_cortex" —
that shared value is deliberate: they are both OFC, and the distinction
between them is documented in ANATOMY and config, not in a finer
SUB_REGION granularity.

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
            "detection systems. On the RIGHT, this interface is the "
            "strongest in the frontal registry: the right's area 12 "
            "has the highest amygdala and insula coupling priors in "
            "the entire frontal lobe (0.85 each), and its valence "
            "bias leans most strongly toward threat/avoidance. The "
            "left's area 12 also evaluates visceral outcomes, but it "
            "labels them verbally ('that tasted bitter', 'that "
            "stung'), and the right's evaluates them more directly "
            "('that was bad', 'that hurt') without the verbal "
            "mediation. The left/right split is directional, not "
            "complementary — the right's area 12 is threat/visceral-"
            "forward, not 'the left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 12's RIGHT_CONFIG is a single flat dict (single-system, single
block — no per-system nesting). The schema is identical to areas 9,
10, and 11.

    RIGHT_CONFIG = {
        # ---- STRUCTURAL features (equal across hemispheres) ----
        # The five OFC mechanism features are equal to area 11's values
        # on the right, and equal to the left's. The OFC as a whole
        # computes these mechanisms; the sub-division is about WHAT the
        # outcomes are, not what computation is performed on them.
        "reward_prediction":        0.70,   # structural
        "punishment_prediction":    0.70,   # structural
        "stimulus_outcome_learning":0.75,   # structural
        "reversal_learning":        0.80,   # structural — the OFC's
                                            # signature, unchanged
                                            # from area 11 on either
                                            # side
        "outcome_evaluation":       0.75,   # structural

        # ---- AREA-12 SPECIFIC features (structural across
        # hemispheres) ----
        # The visceral/sensory character of area 12's outcomes does not
        # lateralise. The right and left area 12 both evaluate tastes,
        # smells, visceral discomfort, and social gut feelings. What
        # lateralises is the labelling and the valence bias, not the
        # evaluation itself.
        "taste_reward_evaluation":  0.70,   # structural
        "smell_threat_evaluation":  0.65,   # structural
        "visceral_punishment_evaluation": 0.70,  # structural
        "social_visceral_evaluation": 0.55,  # structural

        # ---- DIRECTIONAL features (lateralised content) ----
        # RIGHT bias: more negative-leaning valence (area 12's
        # outcomes span both valences, but the right weights the
        # threat end more heavily), and direct/unlabelled visceral
        # response rather than verbal labelling.
        "positive_valence_bias":    0.50,   # DOWN from left's 0.60
        "negative_valence_bias":    0.65,   # UP from left's 0.50;
                                            # the right's anchor
        "verbal_outcome_label":     0.40,   # DOWN from left's 0.70
        "direct_visceral_cue":      0.75,   # UP from left's 0.55;
                                            # the right's anchor —
                                            # unlabelled direct
                                            # visceral response

        # ---- connectivity priors ----
        # Area 12's signature connectivity is the amygdala and insula
        # coupling. On the right these are the highest connectivity
        # priors in the entire frontal registry.
        "to_amygdala":              0.85,   # UP from left's 0.80;
                                            # the highest OFC-amygdala
                                            # coupling in the
                                            # frontal lobe
        "to_insula":                0.85,   # UP from left's 0.80;
                                            # the highest OFC-insula
                                            # coupling in the
                                            # frontal lobe
        "to_nucleus_accumbens":     0.55,   # DOWN from left's 0.65;
                                            # positive-reward
                                            # prediction is more
                                            # left-weighted; the
                                            # right's NAcc coupling
                                            # serves threat/avoidance
        "to_hippocampus":           0.55,   # STRUCTURAL (equal)
        "to_vlpfc":                 0.35,   # DOWN from left's 0.45;
                                            # less verbal labelling
                                            # on the right
        "to_vmpfc":                 0.65,   # STRUCTURAL (equal) —
                                            # OFC → VMPFC is the
                                            # value-to-integration
                                            # path
        "to_basal_ganglia":         0.65,   # STRUCTURAL (equal)
        "to_anterior_cingulate":    0.55,   # STRUCTURAL (equal)
        "to_commissures":           0.55,   # UP from left's 0.45 —
                                            # the right's visceral
                                            # outcomes have to
                                            # reach the left's
                                            # verbal labelling for
                                            # narrative expression
                                            # ('I felt it was wrong
                                            # but couldn't say why')
    }

    Notes on the weights:
      - The nine structural features (five OFC mechanisms plus four
        area-12-specific visceral features) are equal across
        hemispheres AND, for the five OFC mechanisms, equal to area
        11's values. The OFC computes the same mechanisms regardless
        of which area is doing the work; the sub-division is about
        WHAT the outcomes are, not what computation is performed on
        them.
      - The four directional features are the lateralised content.
        Note the valence weights: left was 0.60/0.50 (mild positive-
        leaning); right is 0.50/0.65 (mild negative-leaning). The
        right's bias is slightly stronger (0.15 gap vs the left's
        0.10), because the right's visceral evaluation is more
        strongly threat-weighted. This is a milder lateralisation
        than area 11's (which was 0.70/0.45 vs 0.45/0.70 — a much
        larger gap), and that mildness is deliberate: area 12's
        outcomes span both valences more evenly than area 11's
        abstract rewards/punishments.
      - `to_amygdala: 0.85` and `to_insula: 0.85` are the two
        highest connectivity priors in the entire frontal registry
        (higher than area 12's own left side, which was 0.80/0.80;
        higher than area 11's 0.55/0.50; higher than any other
        frontal area's priors). This is the config-level expression
        of the OFC sub-division's functional separation at its
        strongest: the right's area 12 is the OFC's dominant
        visceral/threat interface.
      - `to_vlpfc: 0.35` is the lowest VLPFC coupling in the entire
        frontal registry. The right's area 12 does not label its
        outcomes verbally; it evaluates them directly. The left's
        area 12 (0.45) has more VLPFC coupling because it can label
        visceral outcomes in words ('that tasted bitter'), which
        recruits VLPFC's semantic machinery. On the right, the
        outcome is felt without being named, so VLPFC coupling is
        minimal.
      - `to_commissures: 0.55` is the mirror of the left's 0.45, for
        the standard reason: the right's visceral outcomes need to
        reach the left's verbal labelling for narrative expression.
        This is the same asymmetry as area 10 and area 11, but it
        reaches its strongest form here because the gap between
        "feeling without naming" (right) and "naming without
        feeling" (left) is largest at area 12.
      - All values are plausible priors, not measured constants.
        The key constraints are: (a) structural features equal
        across hemispheres and, for the OFC mechanisms, equal to
        area 11's; (b) directional features directionally mirror;
        (c) amygdala and insula coupling are the strongest priors
        in the file; (d) the valence gap is milder than area 11's.

MIRROR PATTERN
--------------
Area 12's config is a directional mirror with the structural-heavy
profile preserved. The structural features (nine) are equal across
hemispheres; the directional features (four) and directional
connectivity priors (five) mirror:

    left's area 12                right's area 12
    --- OFC mechanism features (structural, equal to area 11's) ---
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
    - direction on the four directional features and the five
      directional connectivity priors (to_amygdala, to_insula,
      to_nucleus_accumbens, to_vlpfc, to_commissures);
    - equality on the four structural connectivity priors
      (to_hippocampus, to_vmpfc, to_basal_ganglia,
      to_anterior_cingulate);
    - the cross-area comparison to area 11: the five OFC mechanism
      features should be equal between area 11 and area 12 on both
      hemispheres, while the outcome-specific features are disjoint
      (area 11: verbal_reward_cue / visual_reward_cue; area 12:
      taste_reward_evaluation / smell_threat_evaluation /
      visceral_punishment_evaluation / social_visceral_evaluation);
    - the amygdala/insula coupling on the right should be strictly
      higher than on the left AND higher than area 11 on either
      side — this is the strongest visceral-coupling signature in
      the frontal registry and it should be testable as a strict
      inequality.

PREDICTION (TESTABLE)
---------------------
Area 12's reversal-learning signature is more stimulus-specific
than area 11's, and the right's is more affectively immediate:

    area 12 lesion (either side):  reversal of SENSORY outcome
                                   contingencies (taste, smell,
                                   visceral discomfort) is impaired;
                                   reversal of VERBAL/CONCEPTUAL
                                   outcome contingencies is
                                   relatively spared.

    area 11 lesion (either side):  reversal of VERBAL/CONCEPTUAL
                                   outcome contingencies is impaired;
                                   reversal of SENSORY outcome
                                   contingencies is relatively spared.

The hemisphere-level valence dissociation is milder for area 12 than
for area 11 (the right's valence weights are 0.50/0.65, closer to
balanced than area 11's 0.45/0.70). The prediction from the left
area-12 file is therefore a weaker lateralisation of valence-driven
reversal than area 11 produces — both hemispheres of area 12 should
show roughly balanced positive/negative reversal deficits, with only
a mild tilt toward positive-outcome reversal on the left and toward
negative-outcome reversal on the right. If the model produces a
strong lateralisation of area-12 reversal, that is a signal that
area 11's pattern has been over-transferred.

On the RIGHT specifically, the specific prediction is:

    right area-12 lesion:  the "gut feeling" deficit is most acute —
                           threat-related sensory reversal is
                           severely impaired (a stimulus that used
                           to smell dangerous but no longer does
                           continues to be avoided), AND the patient
                           cannot verbally articulate WHY they are
                           avoiding it (because the direct visceral
                           cue fires but the verbal labelling
                           pathway through VLPFC is minimised on
                           this side). This is the "I can't explain
                           it, but something feels off" failure
                           mode, and it is more right-lateralised
                           than the left's equivalent.

EXPORTS
-------
    from .brodmann_area_12 import BRODMANN_12     # int, == AREA_ID
    from .brodmann_area_12 import ANATOMY
    from .brodmann_area_12 import RIGHT_CONFIG
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
    - Must not add a `sub_region` field INSIDE RIGHT_CONFIG. The
      package-level SUB_REGION handles the disambiguation.
    - Must not double-count area 12 with area 11. Both are OFC, both
      have SUB_REGION = "orbitofrontal_cortex", but they are separate
      areas with separate configs and different outcome-specific
      features.
    - Must not double-count area 12 with area 10 (VMPFC) or area 25
      (subgenual ACC). Area 12 is posterior-OFC stimulus-outcome
      learning; area 10 is integrated value + self; area 25 is
      sustained affect. Adjacent anatomically, distinct
      computationally.
    - Must not import or reference the left hemisphere's area-12
      package. Cross-midline outcome exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The right's higher `to_commissures: 0.55` prior is the
      baseline for "the right's visceral outcomes have to reach the
      left's verbal labelling for narrative expression"; direct
      registry access would bypass the commissural delay that gives
      that handoff its behavioural signature — the "I felt it was
      wrong but couldn't say why" failure mode.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's
      area-12 package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING,
      ANATOMY, same config keys. Only the values differ, and only by
      the directional mirror described above.
    - Must not duplicate area 11's outcome-specific features. Area 11
      carries verbal_reward_cue and visual_reward_cue; area 12
      carries taste_reward_evaluation, smell_threat_evaluation,
      visceral_punishment_evaluation, and social_visceral_evaluation.
      These feature sets are disjoint by design.
"""