"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_10
======================================================================================================================

Brodmann area 10 — right hemisphere.

Mirror of the left area-10 package. A CONSTANT + CONFIG HOLDER. No
compute, no state, no lifecycle. Declares the canonical identity of area
10, says which compute sub-region owns it, and supplies the per-area
weights that the owning sub-region's `encode()` reads. It defines no
classes and no functions; the public surface is the exports listed under
"EXPORTS".

If you are looking for the computation area 10 participates in, it lives
in
`.../frontal/cortex/prefrontal_cortex/ventromedial_prefrontal_cortex/` —
area 10 is the rostral ventromedial prefrontal cortex, and VMPFC is the
value-integration and self-referential core of the frontal lobe. This
package is the *label*; the VMPFC compute sub-region is the *agent*.

VMPFC vs. DLPFC (the framing this file inherits)
------------------------------------------------
The frontal lobe has two prefrontal poles, and they compute very
different things:

    DLPFC (areas 9, 46)    the EFFORTFUL, controlled, working-memory
                           executive. Deliberate. Holds information
                           online. Applies rules. Inhibits prepotent
                           responses. Costly to run.

    VMPFC (area 10)        the AUTOMATIC, integrated, value-based
                           evaluator. Fast. Tags options with value and
                           affect. Reads the body's state. Integrates
                           memory, emotion, and reward into a "how do I
                           feel about this?" signal. Cheap to run.

These are complementary, not redundant. DLPFC produces deliberate choice
when the situation is novel and demanding; VMPFC produces automatic
preference when the situation is familiar and valuation can be cached.
Both project to the basal ganglia, which arbitrates between them.

VMPFC is the area of Phineas Gage and of Damasio's somatic-marker
hypothesis: patients with VMPFC damage retain intact IQ, working memory,
and explicit knowledge of right and wrong, but make disastrous real-world
decisions — they lose the ability to *feel* the value of options and to
integrate that feeling into choice. The config below encodes the "feel"
side of that, not the "know" side. On the RIGHT, the "feel" side is more
directly affect- and body-driven than on the left, which is why the
right's VMPFC is the closer model of the classic somatic-marker failure
mode.

IDENTITY
--------
    AREA_ID    = 10
    NAME       = "Brodmann area 10"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "ventromedial_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping

The single-system prefrontal pattern (SYSTEM one-element list, SUB_REGION
package-level string, no per-block `sub_region` field) is identical to the
left's — it is the shape introduced by area 9 and reused by areas 10, 11,
12, 46. Lateralisation does not change the shape, only the values.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 10",
        "system": "prefrontal_cortex",
        "sub_region": "ventromedial_prefrontal_cortex",
        "grouping": None,
        "location": "the rostral-most part of the prefrontal cortex — "
                    "the frontal pole, on both the lateral surface of "
                    "the middle/superior frontal gyri and the medial "
                    "surface of the superior frontal gyrus, wrapping "
                    "around the rostral margin; the medial portion "
                    "(ventromedial) is the functionally dominant part "
                    "for this area's role",
        "cytoarchitecture": "granular cortex; the most heavily "
                            "granulated prefrontal area (layer IV is "
                            "prominent, layers II-III are well "
                            "developed) — the cytoarchitectonic "
                            "signature of the highest-order "
                            "association cortex",
        "notes": (
            "The rostral ventromedial prefrontal cortex and the frontal "
            "pole. Its core function is value integration: it combines "
            "reward and punishment signals, body-state information "
            "(interoception), autobiographical memory, and self-"
            "relevance into a single integrated value signal that tags "
            "options with 'how much do I want this / how bad is this'. "
            "This integrated signal is the substrate of the somatic-"
            "marker hypothesis (Damasio): bodily and affective states "
            "become part of decision-making by biasing the valuation "
            "of options. On the RIGHT, the integration is more "
            "affectively and viscerally weighted: threat signals, "
            "autonomic states, and bodily fear responses feed more "
            "strongly into the valuation, and the valence bias leans "
            "toward negative/avoidance. This makes the right's VMPFC "
            "the closer model of the classic somatic-marker failure: "
            "when right VMPFC is damaged, the patient fails to *feel* "
            "threat and so approaches options that should be avoided. "
            "The left's VMPFC, by contrast, is more verbally mediated "
            "and leans toward positive/approach. The left/right split "
            "is directional, not complementary — the right's area 10 "
            "is affective/threat-forward, not 'the left's at reduced "
            "weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 10's RIGHT_CONFIG is a single flat dict (single-system, single
block — no per-system nesting).

    RIGHT_CONFIG = {
        # ---- feature emphases ----
        # RIGHT bias: affective self-reference, autonomic emotion
        # regulation, and threat-weighted risk aversion are the
        # anchors. Verbal self-reference, verbal reappraisal, and
        # positive-approach valuation are present but secondary.
        "value_integration":        0.75,   # STRUCTURAL (equal across
                                            # hemispheres); the
                                            # integration mechanism is
                                            # shared, only the content
                                            # differs
        "somatic_marker":           0.65,   # STRUCTURAL (equal); the
                                            # body-state tagging
                                            # mechanism is shared, the
                                            # visceral content differs
        "verbal_self_reference":    0.40,   # DOWN from left's 0.80
        "affective_self_reference": 0.80,   # UP from left's 0.45;
                                            # the right's anchor —
                                            # self-related processing
                                            # via feeling and body
                                            # state
        "emotion_regulation_reappraisal": 0.40,
                                            # DOWN from left's 0.75;
                                            # verbal/cognitive
                                            # reappraisal is left-
                                            # weighted
        "emotion_regulation_suppression": 0.70,
                                            # UP from left's 0.35;
                                            # autonomic/expressive
                                            # downregulation is right-
                                            # weighted
        "autobiographical_recall":  0.70,   # STRUCTURAL (equal); the
                                            # content differs
                                            # (affective vs verbal)
                                            # but the weight is the
                                            # same
        "social_valuation":         0.55,   # STRUCTURAL (equal)
        "risk_aversion":            0.75,   # UP from left's 0.55 —
                                            # threat-weighted risk
                                            # assessment is the
                                            # right's dominant mode
        "moral_judgment":           0.55,   # STRUCTURAL (equal); the
                                            # content differs
                                            # (affective vs verbal)
                                            # but the weight is the
                                            # same

        # ---- connectivity priors ----
        "to_amygdala":              0.70,   # UP from left's 0.55;
                                            # VMPFC-amygdala fear
                                            # regulation is stronger
                                            # on the right
        "to_insula":                0.75,   # UP from left's 0.60;
                                            # the somatic-marker
                                            # pathway has stronger
                                            # interoceptive input on
                                            # the right
        "to_hippocampus":           0.65,   # STRUCTURAL (equal)
        "to_posterior_cingulate":   0.75,   # STRUCTURAL (equal); DMN
                                            # hub
        "to_precuneus":             0.60,   # STRUCTURAL (equal)
        "to_nucleus_accumbens":     0.70,   # STRUCTURAL (equal)
        "to_hypothalamus":          0.70,   # UP from left's 0.50;
                                            # autonomic output is
                                            # stronger on the right
        "to_dlpfc":                 0.60,   # STRUCTURAL (equal)
        "to_basal_ganglia":         0.70,   # STRUCTURAL (equal)
        "to_commissures":           0.55,   # UP from left's 0.45 —
                                            # the right's threat/
                                            # visceral valuation has
                                            # to reach the left's
                                            # verbal valuation for
                                            # narrative expression;
                                            # the left's verbally-
                                            # mediated value has less
                                            # need to reach the
                                            # right's affective side
    }

    Notes on the weights:
      - The structural-heavy profile is preserved on the right. Seven of
        ten features (`value_integration`, `somatic_marker`,
        `autobiographical_recall`, `social_valuation`, `moral_judgment`,
        plus `verbal_self_reference` / `affective_self_reference` as the
        lateralised pair) and six of ten connectivity priors
        (`to_hippocampus`, `to_posterior_cingulate`, `to_precuneus`,
        `to_nucleus_accumbens`, `to_dlpfc`, `to_basal_ganglia`) are
        equal across hemispheres. This is a substantially more
        structural config than area 9's, and the mirror tests must
        reflect that.
      - The two self-reference features swap direction (0.80→0.40 for
        verbal; 0.45→0.80 for affective), and the two emotion-
        regulation features swap (0.75→0.40 for reappraisal;
        0.35→0.70 for suppression). These are the four lateralised
        features. The remaining six are structural.
      - `value_integration` and `somatic_marker` are STRUCTURAL — the
        same single feature on both sides, with the same weight. The
        integration and tagging mechanisms are conserved; only the
        *inputs* to them differ (verbal vs affective; positive vs
        negative valence), which is expressed through the upstream
        features (`verbal_self_reference` vs `affective_self_reference`)
        and the upstream connectivity priors (`to_insula`,
        `to_amygdala`).
      - All three of the lateralised connectivity priors
        (`to_amygdala`, `to_insula`, `to_hypothalamus`) point the same
        direction: right stronger. Together they encode the right
        VMPFC's stronger grip on threat regulation, interoception, and
        autonomic control. On the left these are lower because the
        left's valuation is more verbally mediated and less directly
        coupled to the body.
      - `to_commissures: 0.55` is higher than the left's 0.45 because
        the right's threat/visceral valuation has to reach the left's
        verbal valuation for narrative expression ("I felt uneasy but
        couldn't say why" is the signature of the left hemisphere
        trying to verbalise a right hemisphere value). The reverse
        direction — the left's verbal value reaching the right's
        affective side — happens less often, which is why the left's
        commissural prior is lower.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) the right's anchors match its
        functional signature; (b) structural priors are identical
        across hemispheres; (c) lateralised priors directionally
        mirror.

MIRROR PATTERN
--------------
Area 10's config is a directional mirror on the same key set as the
left's, with the structural-heavy pattern preserved:

    left's area 10                right's area 10
    value_integration       0.75  value_integration       0.75  (equal)
    somatic_marker          0.65  somatic_marker          0.65  (equal)
    verbal_self_reference   0.80  verbal_self_reference   0.40
    affective_self_reference 0.45 affective_self_reference 0.80
    emotion_regulation_reappraisal 0.75
                                  emotion_regulation_reappraisal 0.40
    emotion_regulation_suppression 0.35
                                  emotion_regulation_suppression 0.70
    autobiographical_recall 0.70  autobiographical_recall 0.70  (equal)
    social_valuation        0.55  social_valuation        0.55  (equal)
    risk_aversion           0.55  risk_aversion           0.75
    moral_judgment          0.55  moral_judgment          0.55  (equal)
    to_amygdala             0.55  to_amygdala             0.70
    to_insula               0.60  to_insula               0.75
    to_hippocampus          0.65  to_hippocampus          0.65  (equal)
    to_posterior_cingulate  0.75  to_posterior_cingulate  0.75  (equal)
    to_precuneus            0.60  to_precuneus            0.60  (equal)
    to_nucleus_accumbens    0.70  to_nucleus_accumbens    0.70  (equal)
    to_hypothalamus         0.50  to_hypothalamus         0.70
    to_dlpfc                0.60  to_dlpfc                0.60  (equal)
    to_basal_ganglia        0.70  to_basal_ganglia        0.70  (equal)
    to_commissures          0.45  to_commissures          0.55

    The mirror test must check direction on the lateralised keys
    (`verbal_self_reference`, `affective_self_reference`,
    `emotion_regulation_reappraisal`, `emotion_regulation_suppression`,
    `risk_aversion`, `to_amygdala`, `to_insula`, `to_hypothalamus`,
    `to_commissures`) and equality on the structural keys (the rest).

PREDICTION (TESTABLE)
---------------------
The feature split supports the same double dissociation described on
the left, with the right's failure modes being the *classic* clinical
ones:

    VMPFC lesion, right hemisphere: impaired affective self-reference
                                    and autonomic emotion regulation;
                                    preserved verbal reappraisal;
                                    somatic markers fail to bias
                                    avoidance (patient fails to feel
                                    threat), producing approach to
                                    dangerous options — the classic
                                    Phineas Gage / Damasio patient
                                    profile.

    VMPFC lesion, left hemisphere:  impaired verbal self-reference and
                                    verbal reappraisal; preserved
                                    affective self-reference and
                                    autonomic regulation; somatic
                                    markers still present but not
                                    accessible to verbal reasoning
                                    ("I know it's dangerous but I
                                    can't explain why").

On the right, the somatic-marker prediction is stronger because the
right's valuation is more directly coupled to interoception and
amygdala/threat signals (the higher priors). The model should produce
the Phineas Gage pattern more clearly with a right VMPFC lesion, and
the "knows but can't explain" pattern more clearly with a left lesion.

EXPORTS
-------
    from .brodmann_area_10 import BRODMANN_10     # int, == AREA_ID
    from .brodmann_area_10 import ANATOMY
    from .brodmann_area_10 import RIGHT_CONFIG
    from .brodmann_area_10 import SYSTEM          # list, ["prefrontal_cortex"]
    from .brodmann_area_10 import SUB_REGION      # str, set for single-system
    from .brodmann_area_10 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_10`) — area 10 is a direct child
of brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in VMPFC, not here.
    - Must not import `prefrontal_cortex/` or
      `ventromedial_prefrontal_cortex/` (cycle; the compute imports
      from here, not the other way round).
    - Must not split into per-system or per-sub-region blocks. Area 10
      is single-system with SUB_REGION set; its config is a single
      flat dict.
    - Must not add a `sub_region` field INSIDE RIGHT_CONFIG. The
      package-level SUB_REGION handles the disambiguation.
    - Must not double-count area 10 with area 25 (the subgenual ACC).
      Area 10 is VMPFC's rostral portion; area 25 is the subgenual
      ACC's affective division, which lives in
      `cingulate/subgenual_area_25/` and is documented as a sibling
      of the frontal registry, not inside it. The two are adjacent
      anatomically and both involve "affect + decision-making", but
      they are separate compute sub-modules with separate state
      contracts (VMPFC is stateless across ticks in this design; area
      25 carries an `affective_setpoint`). If a future contributor is
      tempted to merge them, that is a signal that the VMPFC/area-25
      distinction needs re-documenting, not that the merge is correct.
    - Must not import or reference the left hemisphere's area-10
      package. Cross-midline valuation exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The right's higher `to_commissures: 0.55` prior is the
      baseline for "the right's threat/visceral valuation has to
      reach the left's verbal valuation for narrative expression";
      direct registry access would bypass the commissural delay
      that gives that handoff its behavioural signature.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-10
      package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING, ANATOMY,
      same config keys. Only the values differ, and only by the
      directional mirror described above.
"""