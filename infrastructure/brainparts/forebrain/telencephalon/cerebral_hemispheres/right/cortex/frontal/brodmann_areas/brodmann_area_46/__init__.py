"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_46
======================================================================================================================

Brodmann area 46 — right hemisphere.

Mirror of the left area-46 package. A CONSTANT + CONFIG HOLDER. No
compute, no state, no lifecycle. Declares the canonical identity of area
46, says which compute sub-region owns it, and supplies the per-area
weights that the owning sub-region's `encode()` reads. It defines no
classes and no functions; the public surface is the exports listed under
"EXPORTS".

If you are looking for the computation area 46 participates in, it lives
in
`.../frontal/cortex/prefrontal_cortex/dorsolateral_prefrontal_cortex/` —
area 46 is DLPFC's second area, and the pair (9, 46) constitutes the
dorsolateral prefrontal subdivision. This package is the *label*; the
DLPFC compute sub-region is the *agent*.

AREA 46's PLACE WITHIN THE DLPFC SUBDIVISION
--------------------------------------------
DLPFC has two Brodmann areas — 9 and 46 — separated by which *stage* of
the executive process they anchor:

    area 9     the HOLD-and-PLAN anchor — working memory contents held
               online, plans constructed, goals maintained.
    area 46    the RULE-and-CONTROL anchor — task sets maintained,
               rules represented and applied, responses monitored
               against the rule, sustained attention over the task.

On the RIGHT, area 46's rule/control role is expressed through
spatial and situational rule content: rules embedded in spatial
layouts, task sets tied to visual scenes, stimulus-rule-response
associations whose content is spatial rather than verbal. The right's
area 46 still does task-set maintenance and response monitoring (it is
the rule/control anchor on both sides), but its rules are more often
spatial-situational than verbally-stated. The left/right split is
directional, not complementary — the right's area 46 is spatial-rule-
forward, not 'the left's at reduced weight'.

SCHEMA ADDITION: `dlpfc_weight` (and the area-9 amendment)
----------------------------------------------------------
Areas 9 and 46 *overlap* on the core DLPFC features (both carry working
memory, planning, cognitive control, response inhibition, rule
representation, task switching, abstract reasoning, goal maintenance,
distraction resistance), weighting them differently. The DLPFC compute
sub-region therefore needs a per-area share to combine the two areas'
contributions: a straight `dlpfc_weight` blend, analogous to the PCC's
`pcc_weight` and the RSC's `rsc_weight`.

Area 46 (this file) introduces the `dlpfc_weight` field. The
corresponding amendment for area 9 (add `dlpfc_weight: 0.55` to its
LEFT_CONFIG and RIGHT_CONFIG) is documented as pending in the left
area-46 docstring's SCHEMA ADDITION section and is repeated here for
the right side:

    AREA 9'S AMENDMENT (pending, both hemispheres):
        Add to LEFT_CONFIG / RIGHT_CONFIG:
            "dlpfc_weight": 0.55   # structural; equal on both sides
        The split is 9 : 46 = 0.55 : 0.45 on both hemispheres. Area 9
        takes the larger share because it is the more established
        DLPFC anchor (working memory hold is the more thoroughly
        characterized DLPFC function); area 46 takes the smaller but
        still substantial share because rule maintenance is a distinct
        and important contribution.

The split itself is structural — identical on both hemispheres. Only
the feature values inside each area's config lateralise. The amendment
is documented here rather than silently backfilled so that anyone
reading area 9 sees the field's absence as "pending amendment,
documented in area 46" rather than "oversight".

IDENTITY
--------
    AREA_ID    = 46
    NAME       = "Brodmann area 46"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = "dorsolateral_prefrontal_cortex"
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping

The single-system prefrontal pattern (SYSTEM one-element list, SUB_REGION
package-level string, no per-block `sub_region` field) is identical to
the left's. Areas 9 and 46 share SUB_REGION = "dorsolateral_prefrontal_
cortex" on both hemispheres — that shared value is deliberate: they are
both DLPFC, and the distinction between them is documented in ANATOMY
and config, not in a finer SUB_REGION granularity.

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
            "system, and its rule-maintenance role is what makes the "
            "MD system flexibly applicable: the same neural machinery "
            "implements different rules without rewiring. On the "
            "RIGHT, the rule content is more spatially and "
            "situationally mediated: rules embedded in spatial "
            "layouts, task sets tied to visual scenes, "
            "stimulus-rule-response associations whose content is "
            "spatial rather than verbal. The right's area 46 still "
            "does task-set maintenance and response monitoring (it is "
            "the rule/control anchor on both sides), but its rules "
            "are more often spatial-situational than verbally-stated. "
            "The left/right split is directional, not complementary — "
            "the right's area 46 is spatial-rule-forward, not 'the "
            "left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 46's RIGHT_CONFIG is a single flat dict (single-system, single
block). It is schema-identical to area 9's EXCEPT for the
`dlpfc_weight` field introduced by area 46.

    RIGHT_CONFIG = {
        # ---- per-area share within DLPFC (structural) ----
        # 9 : 46 sum to 1.0. Structural — identical on both
        # hemispheres. Only the feature values inside each area's
        # config lateralise.
        "dlpfc_weight":             0.45,   # area 9: 0.55

        # ---- feature emphases ----
        # RIGHT bias: spatial rules, spatial task-set content. The
        # left's area 46 is verbal-rule-forward.
        "verbal_working_memory":    0.30,   # DOWN from area 9's 0.45;
                                            # area 46 is not the WM
                                            # anchor
        "spatial_working_memory":   0.45,   # DOWN from area 9's 0.80;
                                            # area 46 is not the WM
                                            # anchor, but spatial WM
                                            # is higher here than
                                            # verbal WM on the right
        "planning":                 0.50,   # structural (equal)
        "cognitive_control":        0.80,   # structural (equal);
                                            # the rule/control anchor
                                            # on both sides
        "response_inhibition":      0.75,   # structural (equal)
        "rule_representation":      0.80,   # DOWN mildly from left's
                                            # 0.85; still the
                                            # right's anchor
        "task_switching":           0.70,   # structural (equal)
        "abstract_reasoning":       0.45,   # DOWN from area 9's 0.55
        "goal_maintenance":         0.65,   # structural (equal)
        "distraction_resistance":   0.75,   # structural (equal)

        # ---- area-46-specific features ----
        # These are features area 46 carries that area 9 does not.
        # The rule-maintenance/attention/monitoring trio is
        # structural (both sides do it); the content pair
        # (verbal vs spatial rule content) is directional.
        "rule_maintenance_over_delay": 0.80,  # DOWN mildly from
                                              # left's 0.85; still
                                              # the defining
                                              # task-set operation
        "sustained_attention":         0.80,  # structural (equal)
        "response_monitoring":         0.75,  # structural (equal)
        "task_set_binding":            0.80,  # structural (equal)
        "verbal_rule_content":         0.40,  # DOWN from left's 0.70
        "spatial_rule_content":        0.65,  # UP from left's 0.35;
                                              # the right's anchor
                                              # for rule content

        # ---- connectivity priors ----
        "to_basal_ganglia":         0.75,   # structural (equal);
                                            # rule-based action
                                            # selection
        "to_anterior_cingulate":    0.70,   # structural (equal);
                                            # rule-conflict
                                            # monitoring
        "to_area_9":                0.80,   # structural (equal)
        "to_inferior_frontal_junction": 0.65,
                                            # structural (equal);
                                            # IFJ task-set node
        "to_parietal":              0.65,   # UP from left's 0.55;
                                            # spatial-rule
                                            # selection couples to
                                            # parietal spatial
                                            # representations
        "to_temporal":              0.45,   # DOWN from left's 0.55;
                                            # verbal-rule content
                                            # coupling is left-
                                            # weighted
        "to_premotor_cortex":       0.55,   # structural (equal)
        "to_vmpfc":                 0.40,   # structural (equal) —
                                            # rule maintenance is
                                            # not value-based; both
                                            # sides have low VMPFC
                                            # coupling
        "to_commissures":           0.50,   # structural (equal);
                                            # rule sets often need
                                            # cross-hemisphere
                                            # integration (spatial
                                            # rule on the right +
                                            # verbal rule on the
                                            # left)
    }

    Notes on the weights:
      - The `dlpfc_weight: 0.45` is structural — identical to the left.
        Area 9's corresponding `dlpfc_weight: 0.55` is pending
        amendment (documented above). The sum is 1.0 on each
        hemisphere. The share itself does not lateralise; only the
        feature values inside each area's config do.
      - The three control-implementation features (cognitive_control
        0.80, response_inhibition 0.75, task_switching 0.70,
        distraction_resistance 0.75) are STRUCTURAL — equal to the
        left's. The rule/control anchor's *implementation* does not
        lateralise; only the *content* of the rules does.
      - `rule_representation: 0.80` (right) vs `0.85` (left): a mild
        leftward tilt, because rule representation's dominant content
        (verbally-stated rules) is more left-lateralised. But the gap
        is small — the rule-representation *mechanism* is on both
        sides; the left just has more of its rules in verbal form.
      - `rule_maintenance_over_delay: 0.80` (right) vs `0.85` (left):
        same logic — the maintenance mechanism is symmetric, the
        content that's maintained is lateralised. The mild tilt
        reflects that verbal rules (left's dominant content) are
        marginally easier to hold through a delay than spatial rules
        (right's), which may explain why the left's maintenance weight
        is slightly higher despite the mechanism being symmetric.
      - The content pair (verbal_rule_content 0.40, spatial_rule_content
        0.65) is the file's cleanest directional mirror. Left was
        0.70/0.35; right is 0.40/0.65. Same pattern as area 9's
        verbal/spatial WM anchor swap, applied to rule content rather
        than WM content.
      - The two directional connectivity priors (to_parietal 0.65,
        to_temporal 0.45) mirror the content pair: spatial rules
        couple to parietal; verbal rules couple to temporal. On the
        right, parietal wins; on the left, temporal wins.
      - `to_vmpfc: 0.40` is the file's most deliberately low prior,
        identical to the left's. Rule maintenance is "cold" cognitive
        control — not value-based — and area 46's low VMPFC coupling is
        its signature "cold control" property. This is structural and
        should not be raised on either side; raising it would
        mischaracterize area 46's role.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) `dlpfc_weight` sums to 1.0 across 9
        and 46 on each hemisphere; (b) area 46's features weight the
        rule/control end higher than the WM/plan end; (c) the
        area-46-specific features are disjoint from area 9's; (d) the
        basal-ganglia and ACC priors are especially high; (e) the
        content pair mirrors directionally.

MIRROR PATTERN
--------------
Area 46's config is a directional mirror on the shared WM/content
keys and structural on the control-implementation keys:

    left's area 46                right's area 46
    --- structural (equal) ---
    dlpfc_weight            0.45  dlpfc_weight            0.45  (equal)
    planning                0.50  planning                0.50  (equal)
    cognitive_control       0.80  cognitive_control       0.80  (equal)
    response_inhibition     0.75  response_inhibition     0.75  (equal)
    task_switching          0.70  task_switching          0.70  (equal)
    goal_maintenance        0.65  goal_maintenance        0.65  (equal)
    distraction_resistance  0.75  distraction_resistance  0.75  (equal)
    sustained_attention     0.80  sustained_attention     0.80  (equal)
    response_monitoring     0.75  response_monitoring     0.75  (equal)
    task_set_binding        0.80  task_set_binding        0.80  (equal)
    to_basal_ganglia        0.75  to_basal_ganglia        0.75  (equal)
    to_anterior_cingulate   0.70  to_anterior_cingulate   0.70  (equal)
    to_area_9               0.80  to_area_9               0.80  (equal)
    to_inferior_frontal_junction 0.65
                                  to_inferior_frontal_junction 0.65 (equal)
    to_premotor_cortex      0.55  to_premotor_cortex      0.55  (equal)
    to_vmpfc                0.40  to_vmpfc                0.40  (equal)
    to_commissures          0.50  to_commissures          0.50  (equal)
    --- directional (mirror) ---
    verbal_working_memory   0.40  verbal_working_memory   0.30
    spatial_working_memory  0.30  spatial_working_memory  0.45
    rule_representation     0.85  rule_representation     0.80
    abstract_reasoning      0.50  abstract_reasoning      0.45
    rule_maintenance_over_delay 0.85
                                  rule_maintenance_over_delay 0.80
    verbal_rule_content     0.70  verbal_rule_content     0.40
    spatial_rule_content    0.35  spatial_rule_content    0.65
    to_parietal             0.55  to_parietal             0.65
    to_temporal             0.55  to_temporal             0.45

    The mirror test must check direction on the eight directional keys
    (verbal_working_memory L>R; spatial_working_memory R>L;
    rule_representation L>R mildly; abstract_reasoning L>R mildly;
    rule_maintenance_over_delay L>R mildly; verbal_rule_content L>R;
    spatial_rule_content R>L; to_parietal R>L; to_temporal L>R —
    nine keys), and equality on the fifteen structural keys listed in
    the equality block above.

    The structural-heavy profile is pronounced: fifteen of twenty-four
    keys are structural. This is a stronger structural signature than
    area 9's (where nearly everything mirrored), and the reason is
    that area 46's role — rule maintenance, task-set binding,
    response monitoring, sustained attention, response inhibition,
    cognitive control, task switching — is almost entirely
    content-neutral: the *machinery* of rule control is symmetric;
    only the *content* (verbal vs spatial rules) and a couple of
    closely-related weights (rule representation, rule maintenance,
    abstract reasoning) tilt mildly. The mirror test must know which
    keys these are, because a naive "everything mirrors" assumption
    would fail spuriously on fifteen of them.

    Cross-area comparison to area 9 (via the area-9 amendment): the
    dlpfc_weight values should sum to 1.0 across 9 and 46 on each
    hemisphere; the shared WM/plan keys should be lower in area 46
    than in area 9 on the same hemisphere; the shared control/rule
    keys should be higher in area 46 than in area 9 on the same
    hemisphere.

PREDICTION (TESTABLE)
---------------------
The double dissociation from area 9 (documented in the left area-46
docstring) applies identically on the right, with the hemisphere axis
producing the spatial-content version of the deficit:

    area 46 lesion, right:   severe impairment on SPATIAL rule-based
                             task-set maintenance and switching — the
                             patient cannot hold a spatial rule through
                             a delay, cannot switch spatial task sets
                             when the layout changes, shows
                             perseveration on the old spatial rule.
                             Verbal-rule maintenance is relatively
                             spared.

    area 9 lesion, right:    severe impairment on spatial working-
                             memory span and spatial multi-step
                             planning — the patient cannot hold
                             spatial content through a delay, cannot
                             plan a spatial multi-step sequence.
                             Spatial rule-based task-set maintenance
                             is relatively spared.

Combined with the left-hemisphere profiles (verbal-content versions),
this gives four distinguishable DLPFC lesion profiles, and the two
right-hemisphere ones are the spatial-content mirror of the left's two.
The 2×2×2 structure (area × hemisphere × content-type) is the testable
claim; a test that probes rule switching vs delayed response, with
verbal vs spatial content, should see the predicted pattern from all
four DLPFC lesion configs.

EXPORTS
-------
    from .brodmann_area_46 import BRODMANN_46     # int, == AREA_ID
    from .brodmann_area_46 import ANATOMY
    from .brodmann_area_46 import RIGHT_CONFIG
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
    - Must not split into per-system or per-sub-region blocks. Area
      46 is single-system with SUB_REGION set; its config is a
      single flat dict.
    - Must not add a `sub_region` field INSIDE RIGHT_CONFIG.
    - Must not double-count area 46 with area 9. Both are DLPFC; the
      DLPFC compute sub-region reads both, weighted by their
      `dlpfc_weight` shares.
    - Must not double-count area 46 with area 44/45 (Broca's area /
      IFJ). Area 46 is DLPFC; area 44/45 is VLPFC. They are coupled
      (the `to_inferior_frontal_junction` prior reflects that), but
      separate compute contributions.
    - Must not add `dlpfc_weight` to area 46's config without also
      documenting that area 9's corresponding amendment is pending
      (on both hemispheres). The SCHEMA ADDITION section of this
      file is the record of that amendment.
    - Must not raise `to_vmpfc` above its structural 0.40. The low
      VMPFC prior is area 46's "cold control" signature; raising it
      would mischaracterize the area's role.
    - Must not import or reference the left hemisphere's area-46
      package. Cross-midline rule exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The rule-content pair (verbal on the left, spatial on
      the right) is a canonical case: a spatial-rule task may need
      a verbal-rule constraint from the left, and the exchange must
      go through the commissures. The right's `to_commissures: 0.50`
      prior is structural (same as the left's) because the exchange
      need is symmetric — a verbal task needing spatial constraints
      is as common as a spatial task needing verbal constraints, at
      this level of abstraction.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's
      area-46 package — same AREA_ID, SYSTEM, SUB_REGION, GROUPING,
      ANATOMY, same config keys, same `dlpfc_weight` value
      (structural, equal across hemispheres). Only the feature and
      connectivity values differ, and only by the directional mirror
      described above.
"""