"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_46
======================================================================================================================

Brodmann area 46 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 46, says which compute sub-region owns it,
and supplies the per-area weights that the owning sub-region's `encode()`
reads. It defines no classes and no functions; the public surface is the
exports listed under "EXPORTS".

If you are looking for the computation area 46 participates in, it lives
in
`.../frontal/cortex/prefrontal_cortex/dorsolateral_prefrontal_cortex/` —
area 46 is DLPFC's second area, and the pair (9, 46) constitutes the
dorsolateral prefrontal subdivision. This package is the *label*; the
DLPFC compute sub-region is the *agent*.

AREA 46's PLACE WITHIN THE DLPFC SUBDIVISION
--------------------------------------------
DLPFC has two Brodmann areas — 9 and 46 — and unlike OFC (11, 12), which
split their outcomes by *content* (semantic vs visceral), DLPFC's two
areas overlap on the same cognitive operations but anchor different
*stages* of the executive process:

    area 9     the HOLD-and-PLAN anchor — working memory contents held
               online, plans constructed, goals maintained. The
               "what am I working on, and what is the multi-step path
               to it?" part of the executive.

    area 46    the RULE-and-CONTROL anchor — task sets maintained,
               rules represented and applied, responses monitored
               against the rule, sustained attention over the task.
               The "what are the rules, and am I still following
               them?" part of the executive.

Both areas participate in both stages — neither is strictly one or the
other — but their configs weight the stages differently. Area 46 is
higher on rule maintenance, cognitive control, response monitoring, and
task-set binding; area 9 is higher on working memory hold, planning,
and goal maintenance.

This overlap is why area 46 introduces a per-area share weight —
`dlpfc_weight` — that area 9 does NOT yet have. See the SCHEMA
ADDITION section below.

SCHEMA ADDITION: `dlpfc_weight` (and the area-9 amendment)
----------------------------------------------------------
Areas 11 and 12 (OFC) had *disjoint* outcome-specific features: 11
carried semantic_reward_cue and visual_reward_cue; 12 carried
taste_reward_evaluation, smell_threat_evaluation, etc. The two areas
contributed to the OFC compute sub-region through feature-level
synthesis, not through a weighted blend of overlapping signals. So
neither had a share weight, and that was correct.

Areas 9 and 46 (DLPFC) *overlap* on the core DLPFC features: both
carry working memory, planning, cognitive control, response
inhibition, rule representation, task switching, abstract reasoning,
goal maintenance, distraction resistance. They weight these features
differently (46 anchors the rule/control end; 9 anchors the WM/plan
end), but they are the same feature *keys* with different values. The
DLPFC compute sub-region therefore needs a per-area share to combine
the two areas' contributions into a single DLPFC signal — a straight
`dlpfc_weight` blend, analogous to the PCC's `pcc_weight` (between
areas 23 and 31) and the RSC's `rsc_weight` (between areas 26, 29,
30).

Area 46 (this file) introduces the `dlpfc_weight` field. Area 9
(already written) does NOT currently have it — area 9's docstring was
written before area 46's pair structure was settled, and it presented
area 9 as a standalone config. Adding the field to area 9 is a
follow-up amendment:

    AREA 9'S AMENDMENT (pending):
        Add to LEFT_CONFIG / RIGHT_CONFIG:
            "dlpfc_weight": 0.55   # left; right is also 0.55 (structural)
        The split is 9 : 46 = 0.55 : 0.45 on both hemispheres (the
        share itself does not lateralise; only the feature values do).
        Area 9's share is larger because it is the more established
        DLPFC anchor (working memory hold is the more thoroughly
        characterized DLPFC function); area 46's share is smaller but
        still substantial because rule maintenance is a distinct and
        important contribution.

This amendment is documented here rather than silently backfilled,
so that anyone reading area 9 sees the field's absence as "pending
amendment, documented in area 46" rather than "oversight". The
alternative — quietly adding `dlpfc_weight` to area 9 without
documenting the schema decision — would leave the share's rationale
unrecorded and would make it look like area 9 had always been a
DLPFC pair member. Doing it here keeps the record honest.

IDENTITY
--------
    AREA_ID    = 46
    NAME       = "Brodmann area 46"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "dorsolateral_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping

This follows the single-system prefrontal pattern introduced by area 9:
SYSTEM is a one-element list, SUB_REGION is a package-level string, no
per-block `sub_region` field. Areas 9 and 46 share the same
SUB_REGION value ("dorsolateral_prefrontal_cortex") — that shared value
is deliberate and correct: they are both DLPFC, and the distinction
between them is documented in ANATOMY and config, not in a finer
SUB_REGION granularity.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 46",
        "system": "prefrontal_cortex",
        "sub_region": "dorsolateral_prefrontal_cortex",
        "grouping": None,
        "location": "middle frontal gyrus, roughly midway between the "
                    "superior and inferior frontal sulci, extending "
                    "from the anterior bank of the precentral sulcus "
                    "rostrally to the frontal pole; lies just "
                    "anterior-ventral to area 9 in the DLPFC strip",
        "cytoarchitecture": "granular cortex; prominent layer IV, "
                            "well-developed layers II-III; heavily "
                            "interconnected with area 9 and with the "
                            "inferior frontal junction (area 44/45 "
                            "region) — the latter coupling is what "
                            "supports rule-based task control across "
                            "the DLPFC-VLPFC boundary",
        "notes": (
            "DLPFC's second area and the rule/control anchor of the "
            "dorsolateral executive. Area 46's core function is "
            "task-set maintenance: holding a representation of the "
            "rules that currently apply, monitoring responses against "
            "those rules, and switching task sets when the situation "
            "changes. It is a key node of the multiple-demand (MD) "
            "system — the fronto-parietal network that activates "
            "across many demanding tasks regardless of content — and "
            "its rule-maintenance role is what makes the MD system "
            "flexibly applicable: the same neural machinery can "
            "implement different rules without rewiring. Beyond rule "
            "maintenance, area 46 contributes to cognitive control "
            "implementation (applying the rule, not just representing "
            "it), response inhibition under rule constraints, "
            "sustained attention over the task, and task-set binding "
            "(the stimulus-rule-response associations that define a "
            "task). It overlaps with area 9 on working memory and "
            "planning (both areas carry these features) but is less "
            "weighted on raw WM hold and multi-step planning, which "
            "are area 9's anchors. On the left, area 46's rule "
            "content is more verbally and symbolically mediated "
            "(rules stated in words, task sets described in "
            "propositions), and its working-memory coupling is more "
            "verbal-temporal. On the right, rule content is more "
            "spatially and situationally mediated (rules embedded in "
            "spatial layouts, task sets tied to visual scenes), and "
            "its working-memory coupling is more spatial-parietal. "
            "The left/right split is directional, not complementary — "
            "the right's area 46 is spatial-rule-forward, not 'the "
            "left's at reduced weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 46's LEFT_CONFIG is a single flat dict (single-system, single
block). It is schema-identical to area 9's EXCEPT for the new
`dlpfc_weight` field documented in the SCHEMA ADDITION section above.

    LEFT_CONFIG = {
        # ---- per-area share within DLPFC (NEW in area 46) ----
        # 9 : 46 sum to 1.0. Structural — identical on both
        # hemispheres, because the DLPFC pair's share of the
        # executive budget does not lateralise. Only the feature
        # values inside each area's config do.
        "dlpfc_weight":             0.45,   # area 9: 0.55

        # ---- feature emphases ----
        # LEFT bias: verbal rules, verbal task-set content. The
        # right's area 46 is spatial-rule-forward.
        "verbal_working_memory":    0.40,   # DOWN from area 9's 0.80;
                                            # area 46 is not the WM
                                            # anchor
        "spatial_working_memory":   0.30,   # DOWN from area 9's 0.45
        "planning":                 0.50,   # DOWN from area 9's 0.70;
                                            # multi-step planning is
                                            # area 9's anchor
        "cognitive_control":        0.80,   # UP from area 9's 0.65;
                                            # implementing control is
                                            # area 46's anchor
        "response_inhibition":      0.75,   # UP from area 9's 0.60;
                                            # rule-constrained
                                            # inhibition
        "rule_representation":      0.85,   # UP from area 9's 0.65;
                                            # area 46's primary
                                            # anchor — the rule
                                            # itself
        "task_switching":           0.70,   # UP from area 9's 0.55;
                                            # switching task sets is
                                            # an area-46 function
        "abstract_reasoning":       0.50,   # DOWN mildly from area
                                            # 9's 0.65; relational
                                            # reasoning is more 9
        "goal_maintenance":         0.65,   # DOWN mildly from area
                                            # 9's 0.70; both areas
                                            # maintain goals, 9 is
                                            # slightly more weighted
        "distraction_resistance":   0.75,   # UP from area 9's 0.60;
                                            # resisting distraction
                                            # from the current rule
                                            # set is an area-46
                                            # function

        # ---- area-46-specific features ----
        # These are features area 46 carries that area 9 does not
        # (or carries at much lower weight). They are the file's
        # distinctive content.
        "rule_maintenance_over_delay": 0.85,  # holding a rule active
                                              # across a delay; the
                                              # defining task-set
                                              # operation
        "sustained_attention":         0.80,  # maintaining attention
                                              # over a demanding task
        "response_monitoring":         0.75,  # checking whether the
                                              # response matched the
                                              # rule
        "task_set_binding":            0.80,  # binding stimulus-rule-
                                              # response associations
                                              # that define a task
        "verbal_rule_content":         0.70,  # rules stated
                                              # verbally/symbolically;
                                              # the left's anchor
        "spatial_rule_content":        0.35,  # rules embedded in
                                              # spatial layouts;
                                              # more right-weighted

        # ---- connectivity priors ----
        "to_basal_ganglia":         0.75,   # UP from area 9's 0.65;
                                            # rule-based action
                                            # selection is basal-
                                            # ganglia dependent;
                                            # the striatum receives
                                            # the rule and selects
                                            # the response
        "to_anterior_cingulate":    0.70,   # UP from area 9's 0.65;
                                            # rule-conflict
                                            # monitoring feeds the
                                            # ACC's conflict channel;
                                            # area 46 and ACC are
                                            # tightly coupled
        "to_area_9":                0.80,   # strong intra-DLPFC
                                            # coupling; rules
                                            # constrain what WM holds
        "to_inferior_frontal_junction": 0.65,
                                            # the IFJ (area 44/45
                                            # region) is the task-
                                            # set node; area 46
                                            # binds task sets to
                                            # motor programs there
        "to_parietal":              0.55,   # DOWN from area 9's 0.60;
                                            # less WM-content
                                            # coupling, more rule
                                            # selection
        "to_temporal":              0.55,   # DOWN from area 9's 0.75;
                                            # less verbal-content
                                            # coupling
        "to_premotor_cortex":       0.55,   # rules bias motor
                                            # selection
        "to_vmpfc":                 0.40,   # LOW — rule maintenance
                                            # is not value-based;
                                            # OFC/VMPFC coupling is
                                            # minimal
        "to_commissures":           0.50,   # UP from area 9's 0.40;
                                            # rule sets often need
                                            # cross-hemisphere
                                            # integration (verbal
                                            # rule + spatial layout)
    }

    Notes on the weights:
      - The `dlpfc_weight: 0.45` is the new field this file
        introduces. Area 9 has the corresponding `dlpfc_weight: 0.55`
        pending amendment. The sum is 1.0 on each hemisphere. The
        share itself is structural (equal across hemispheres); only
        the feature values inside each area's config lateralise.
      - The four core-feature weights (verbal_working_memory,
        spatial_working_memory, planning, abstract_reasoning) go
        DOWN relative to area 9; the control/rule features
        (cognitive_control, response_inhibition,
        rule_representation, task_switching,
        distraction_resistance) go UP. The anchor is
        `rule_representation: 0.85` — the highest feature weight in
        the file on either side, and the highest in any DLPFC area
        (area 9's highest was `verbal_working_memory: 0.80` on the
        left).
      - The five area-46-specific features
        (rule_maintenance_over_delay, sustained_attention,
        response_monitoring, task_set_binding,
        verbal_rule_content / spatial_rule_content) are what
        area 46 adds to the DLPFC pair. They are NOT present in
        area 9's config. This is the opposite pattern from the
        OFC pair (11, 12), where the two areas had disjoint
        outcome features and no shared mechanism features — DLPFC
        has shared core features AND area-specific additions.
      - `to_basal_ganglia: 0.75` and `to_anterior_cingulate: 0.70`
        are area 46's two highest connectivity priors, both
        higher than area 9's corresponding priors. Rule-based
        action selection runs through the basal ganglia (the
        striatum receives the rule and selects the response), and
        rule-conflict monitoring runs through the ACC (which
        detects when a rule is being violated). These are
        area 46's functional partners in a way they are not quite
        area 9's.
      - `to_vmpfc: 0.40` is deliberately low — rule maintenance is
        not value-based, and area 46 has minimal OFC/VMPFC
        coupling compared with its other inputs. This is a
        distinguishing feature: area 46's role is more "cold"
        cognitive control, and its connectivity profile is more
        basal-ganglia/ACC/PFC-internal than value-adjacent.
      - All values are plausible priors, not measured constants.
        The key constraints are: (a) `dlpfc_weight` sums to 1.0
        across 9 and 46; (b) area 46's features weight the
        rule/control end higher than the WM/plan end; (c) the
        area-46-specific features are disjoint from area 9's
        feature set; (d) basal-ganglia and ACC priors are
        especially high.

MIRROR PATTERN
--------------
Area 46's config is a directional mirror with the structural/override
pattern:

    left's area 46                right's area 46
    --- structural (equal) ---
    dlpfc_weight            0.45  dlpfc_weight            0.45  (equal)
    --- shared with area 9, but area-46 values ---
    verbal_working_memory   0.40  verbal_working_memory   0.30
    spatial_working_memory  0.30  spatial_working_memory  0.45
    planning                0.50  planning                0.50  (equal)
    cognitive_control       0.80  cognitive_control       0.80  (equal)
    response_inhibition     0.75  response_inhibition     0.75  (equal)
    rule_representation     0.85  rule_representation     0.80
    task_switching          0.70  task_switching          0.70  (equal)
    abstract_reasoning      0.50  abstract_reasoning      0.45
    goal_maintenance        0.65  goal_maintenance        0.65  (equal)
    distraction_resistance  0.75  distraction_resistance  0.75  (equal)
    --- area-46-specific ---
    rule_maintenance_over_delay 0.85
                                  rule_maintenance_over_delay 0.80
    sustained_attention     0.80  sustained_attention     0.80  (equal)
    response_monitoring     0.75  response_monitoring     0.75  (equal)
    task_set_binding        0.80  task_set_binding        0.80  (equal)
    verbal_rule_content     0.70  verbal_rule_content     0.40
    spatial_rule_content    0.35  spatial_rule_content    0.65
    --- connectivity ---
    to_basal_ganglia        0.75  to_basal_ganglia        0.75  (equal)
    to_anterior_cingulate   0.70  to_anterior_cingulate   0.70  (equal)
    to_area_9               0.80  to_area_9               0.80  (equal)
    to_inferior_frontal_junction 0.65
                                  to_inferior_frontal_junction 0.65 (equal)
    to_parietal             0.55  to_parietal             0.65
    to_temporal             0.55  to_temporal             0.45
    to_premotor_cortex      0.55  to_premotor_cortex      0.55  (equal)
    to_vmpfc                0.40  to_vmpfc                0.40  (equal)
    to_commissures          0.50  to_commissures          0.50  (equal)

    The relationship is directional on the shared WM/coupling keys
    (verbal vs spatial) and on the rule-content keys, and equal on
    the structural and control-implementation keys. The mirror test
    must check:
    - direction on verbal_working_memory (L>R),
      spatial_working_memory (R>L), rule_representation (L>R mildly),
      abstract_reasoning (L>R mildly),
      rule_maintenance_over_delay (L>R mildly),
      verbal_rule_content (L>R), spatial_rule_content (R>L),
      to_parietal (R>L), to_temporal (L>R);
    - equality on the structural keys (dlpfc_weight, planning,
      cognitive_control, response_inhibition, task_switching,
      goal_maintenance, distraction_resistance,
      sustained_attention, response_monitoring, task_set_binding,
      to_basal_ganglia, to_anterior_cingulate, to_area_9,
      to_inferior_frontal_junction, to_premotor_cortex, to_vmpfc,
      to_commissures);
    - cross-area comparison to area 9: the shared feature keys
      should have smaller magnitude in area 46 for the WM/plan
      group and larger magnitude for the control/rule group, on
      both hemispheres. The `dlpfc_weight` values should sum to
      1.0 across areas 9 and 46 on each hemisphere.

PREDICTION (TESTABLE)
---------------------
Area 46's rule/control anchor supports a specific double
dissociation from area 9, within DLPFC:

    area 46 lesion (either side):  severe impairment on rule-based
                                   task-set maintenance and
                                   switching — the patient cannot
                                   hold a rule through a delay,
                                   cannot switch tasks when the
                                   rule changes, shows perseveration
                                   on the old rule. Working-memory
                                   span (for content) is relatively
                                   spared.

    area 9 lesion (either side):   severe impairment on working-
                                   memory span and multi-step
                                   planning — the patient cannot
                                   hold content through a delay,
                                   cannot plan a multi-step
                                   sequence. Rule-based task-set
                                   maintenance is relatively spared.

The hemisphere-level split adds a second dimension:
    - left-sided lesions on either area primarily impair
      verbal/symbolic content (verbal rules, verbal WM);
    - right-sided lesions primarily impair spatial/situational
      content (spatial rules, spatial WM).

Combined, this gives the model four distinguishable DLPFC lesion
profiles (area × hemisphere), and they can be probed with
rule-switching tasks (to probe area 46) and delayed-response tasks
(to probe area 9), with verbal vs spatial content. The 2×2
dissociation structure is a substantial testable claim about
DLPFC's internal organisation.

EXPORTS
-------
    from .brodmann_area_46 import BRODMANN_46     # int, == AREA_ID
    from .brodmann_area_46 import ANATOMY
    from .brodmann_area_46 import LEFT_CONFIG
    from .brodmann_area_46 import SYSTEM          # list, ["prefrontal_cortex"]
    from .brodmann_area_46 import SUB_REGION      # str, "dorsolateral_prefrontal_cortex"
    from .brodmann_area_46 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_46`) — area 46 is a direct
child of brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful
      object. The compute is in DLPFC, not here.
    - Must not import `prefrontal_cortex/` or
      `dorsolateral_prefrontal_cortex/` (cycle; the compute imports
      from here, not the other way round).
    - Must not split into per-system or per-sub-region blocks.
      Area 46 is single-system with SUB_REGION set; its config is a
      single flat dict.
    - Must not add a `sub_region` field INSIDE LEFT_CONFIG. The
      package-level SUB_REGION handles the disambiguation.
    - Must not double-count area 46 with area 9. Both are DLPFC, both
      have SUB_REGION = "dorsolateral_prefrontal_cortex", but they
      are separate areas with separate configs and different
      feature profiles (46 anchors the rule/control end; 9 anchors
      the WM/plan end). The DLPFC compute sub-region reads both,
      weighted by their `dlpfc_weight` shares.
    - Must not double-count area 46 with area 44/45 (Broca's area
      / IFJ). Area 46 is DLPFC; area 44/45 is VLPFC. They are
      coupled (the `to_inferior_frontal_junction` prior reflects
      that), but they are separate compute contributions to the
      frontal lobe. Rule-based task control is a joint DLPFC-VLPFC
      operation; neither area "owns" it alone.
    - Must not add `dlpfc_weight` to area 46's config without also
      documenting that area 9's corresponding amendment is pending.
      The SCHEMA ADDITION section of this file is the record of
      that amendment; if the amendment is completed, the section
      should be updated to note it as complete rather than pending.
    - Must not import or reference the left hemisphere's area-46
      package (this file is the left one; the right mirror is the
      peer). Cross-midline rule exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The rule-content pair (verbal on the left, spatial
      on the right) is a canonical case: a verbal-rule task may
      need a spatial-layout rule from the right, and the exchange
      must go through the commissures.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's
      area-46 package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING,
      ANATOMY, same config keys, same `dlpfc_weight` value
      (structural, equal across hemispheres). Only the feature
      and connectivity values differ, and only by the directional
      mirror described above.
"""