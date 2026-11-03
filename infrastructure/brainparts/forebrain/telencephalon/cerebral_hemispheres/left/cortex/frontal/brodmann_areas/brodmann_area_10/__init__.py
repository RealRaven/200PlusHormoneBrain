"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_10
=====================================================================================================================

Brodmann area 10 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 10, says which compute sub-region owns it,
and supplies the per-area weights that the owning sub-region's `encode()`
reads. It defines no classes and no functions; the public surface is the
exports listed under "EXPORTS".

If you are looking for the computation area 10 participates in, it lives in
`.../frontal/cortex/prefrontal_cortex/ventromedial_prefrontal_cortex/` —
area 10 is the rostral ventromedial prefrontal cortex, and VMPFC is the
value-integration and self-referential core of the frontal lobe. This
package is the *label*; the VMPFC compute sub-region is the *agent*.

VMPFC vs. DLPFC (the framing this file inherits)
------------------------------------------------
The frontal lobe has two prefrontal poles, and they compute very different
things:

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
side of that, not the "know" side.

IDENTITY
--------
    AREA_ID    = 10
    NAME       = "Brodmann area 10"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "ventromedial_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping

This follows the single-system prefrontal pattern introduced by area 9:
SYSTEM is a one-element list, SUB_REGION is a package-level string, no
per-block `sub_region` field (that field is reserved for multi-system
areas like 8 and 47). The pattern is identical; only the SUB_REGION value
differs (VMPFC instead of DLPFC).

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
            "of options. VMPFC damage spares explicit reasoning but "
            "removes this biasing — patients can describe the correct "
            "choice and fail to make it. Beyond valuation, area 10 is "
            "the self-referential core of the prefrontal cortex: it is "
            "the most consistently engaged prefrontal region in self-"
            "related processing, autobiographical recall, and "
            "mentalizing about close others. It is a default-mode "
            "network hub (strong coupling with posterior cingulate and "
            "precuneus), and its DMN membership is why VMPFC activity "
            "is high at rest and deactivates during effortful external "
            "tasks — the opposite pattern from DLPFC. On the left, "
            "area 10's valuation is more verbally mediated (words, "
            "narratives, semantic self-description), and its valence "
            "bias leans mildly toward positive/approach. On the right, "
            "valuation is more affectively and viscerally mediated "
            "(body states, threat, autonomic response) and the valence "
            "bias leans toward negative/avoidance. The left/right split "
            "is directional, not complementary — the right's area 10 is "
            "affective/threat-forward, not 'the left's at reduced "
            "weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 10's LEFT_CONFIG is a single flat dict (single-system, single
block — no per-system nesting). See the area-9 docstring for why the
schema is flat here.

    LEFT_CONFIG = {
        # ---- feature emphases ----
        # LEFT bias: verbally-mediated valuation, verbal self-reference,
        # and verbal reappraisal are the anchors. Affective/visceral
        # valuation and autonomic regulation are present but secondary.
        "value_integration":        0.75,   # the integrated reward/penalty
                                            # signal — structural (equal
                                            # across hemispheres; the
                                            # integration happens on both
                                            # sides)
        "somatic_marker":           0.65,   # body-state tagging of
                                            # options — structural;
                                            # the tagging mechanism is
                                            # the same on both sides,
                                            # the visceral content
                                            # differs
        "verbal_self_reference":    0.80,   # self-related processing
                                            # via words, narratives,
                                            # semantic self-description;
                                            # the left's anchor
        "affective_self_reference": 0.45,   # self-related processing
                                            # via feeling and body
                                            # state; more right-weighted
        "emotion_regulation_reappraisal": 0.75,  # verbal/cognitive
                                                 # reappraisal of
                                                 # affect; the left's
                                                 # anchor
        "emotion_regulation_suppression": 0.35,  # expressive suppression
                                                 # / autonomic
                                                 # downregulation;
                                                 # more right-weighted
        "autobiographical_recall":  0.70,   # self-memory recall;
                                            # structural weight, but
                                            # the left's recall is
                                            # more verbal-episodic
        "social_valuation":         0.55,   # valuation of social stimuli;
                                            # more verbal/conceptual
                                            # on the left
        "risk_aversion":            0.55,   # threat-weighted risk
                                            # assessment; more
                                            # right-weighted
        "moral_judgment":           0.55,   # harm/benefit evaluation;
                                            # verbally-mediated moral
                                            # reasoning on the left,
                                            # affectively-mediated on
                                            # the right

        # ---- connectivity priors ----
        "to_amygdala":              0.55,   # VMPFC-amygdala is the
                                            # fear-regulation loop;
                                            # right side has stronger
                                            # coupling (threat
                                            # regulation is right-
                                            # dominant)
        "to_insula":                0.60,   # interoceptive input —
                                            # the somatic-marker
                                            # pathway; right side
                                            # has stronger coupling
        "to_hippocampus":           0.65,   # autobiographical memory
                                            # retrieval; structural
                                            # (equal)
        "to_posterior_cingulate":   0.75,   # DMN hub coupling;
                                            # structural (equal)
        "to_precuneus":             0.60,   # DMN coupling; structural
                                            # (equal)
        "to_nucleus_accumbens":     0.70,   # reward signal source;
                                            # structural (equal)
        "to_hypothalamus":          0.50,   # autonomic output;
                                            # right side stronger
                                            # (autonomic regulation
                                            # is more right-weighted)
        "to_dlpfc":                 0.60,   # value → control
                                            # coupling: VMPFC's value
                                            # signal constrains
                                            # DLPFC's deliberate
                                            # search; structural
                                            # (equal)
        "to_basal_ganglia":         0.70,   # value → action gating;
                                            # the VMPFC-ventral-
                                            # striatum loop is a
                                            # primary pathway for
                                            # value-based choice
        "to_commissures":           0.45,   # cross-midline value
                                            # coordination; right
                                            # side higher (right's
                                            # threat/visceral value
                                            # has to reach left's
                                            # verbal valuation for
                                            # narrative expression)
    }

    Notes on the weights:
      - The two self-reference features (`verbal_self_reference`,
        `affective_self_reference`) are the cleanest lateralisation in
        the file: both are self-reference, but the medium differs
        (words vs feeling), and the weights show it (0.80 vs 0.45 on
        the left; the reverse on the right). They are NOT "the same
        thing at different weights" — they are different feature
        extractions with different upstream inputs.
      - The two emotion-regulation features split the same way:
        `reappraisal` (verbal/cognitive) is left-weighted;
        `suppression` (autonomic/expressive) is right-weighted. This
        is a well-established pattern in the emotion-regulation
        literature and the config reflects it.
      - `value_integration` and `somatic_marker` are STRUCTURAL
        (equal across hemispheres). The integrated value computation
        and the body-state tagging mechanism are the same on both
        sides; only the *content* of what is integrated differs
        (verbal vs affective; positive vs negative valence bias).
        This is a genuinely different case from area 9's
        `verbal_working_memory` vs `spatial_working_memory`, which
        were two different computations with separate features.
        Here there is one computation whose content is lateralised.
      - `to_amygdala`, `to_insula`, and `to_hypothalamus` are the
        three lateralised connectivity priors, all pointing the same
        direction: right stronger. Together they encode the right
        VMPFC's stronger grip on threat regulation, interoception,
        and autonomic control. On the left these are lower because
        the left's valuation is more verbally-mediated and less
        directly coupled to the body.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) the left's anchors match its
        functional signature; (b) structural priors are identical
        across hemispheres; (c) lateralised priors directionally
        mirror.

MIRROR PATTERN
--------------
Area 10's config is a directional mirror on the same key set as the
right's:

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

    The structure is the most "structural-heavy" config so far: seven of
    ten features and six of ten connectivity priors are equal across
    hemispheres. This is because VMPFC's core function (integrated
    valuation) is highly conserved — the *content* of what gets
    integrated and the *affective colour* it takes are lateralised, but
    the integration mechanism is not. This is a meaningfully different
    shape from area 9's config, where the anchor swap was near-total.

    The mirror test must check direction on the lateralised keys
    (`verbal_self_reference`, `affective_self_reference`,
    `emotion_regulation_reappraisal`, `emotion_regulation_suppression`,
    `risk_aversion`, `to_amygdala`, `to_insula`, `to_hypothalamus`,
    `to_commissures`) and equality on the structural keys (the rest).

PREDICTION (TESTABLE)
---------------------
The feature split supports a specific double dissociation:

    VMPFC lesion, left hemisphere:  impaired verbal self-reference and
                                    verbal reappraisal; preserved
                                    affective self-reference and
                                    autonomic regulation; somatic
                                    markers still present but not
                                    accessible to verbal reasoning.

    VMPFC lesion, right hemisphere: impaired affective self-reference
                                    and autonomic emotion regulation;
                                    preserved verbal reappraisal;
                                    somatic markers fail to bias
                                    avoidance (patient fails to feel
                                    threat), producing approach to
                                    dangerous options.

This is the VMPFC analogue of area 9's verbal/spatial WM dissociation.
It's the pattern that makes VMPFC lesion patients (Phineas Gage-style)
reachable in the model: the right lesion produces the classic
"knows the right answer, doesn't feel it" failure; the left lesion
produces a subtler "feels it, can't articulate it" failure.

EXPORTS
-------
    from .brodmann_area_10 import BRODMANN_10     # int, == AREA_ID
    from .brodmann_area_10 import ANATOMY
    from .brodmann_area_10 import LEFT_CONFIG
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
      flat dict. The per-block pattern is reserved for multi-system
      areas (6, 8, 47).
    - Must not add a `sub_region` field INSIDE LEFT_CONFIG. The
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
      package (this file is the left one; the right mirror is the
      peer). Cross-midline valuation exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's
      area-10 package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING,
      ANATOMY, same config keys. Only the values differ, and only by
      the directional mirror described above.
"""