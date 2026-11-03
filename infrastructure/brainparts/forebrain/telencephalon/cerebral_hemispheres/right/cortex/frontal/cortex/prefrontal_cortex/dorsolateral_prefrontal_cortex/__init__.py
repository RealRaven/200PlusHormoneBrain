"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.prefrontal_cortex.dorsolateral_prefrontal_cortex
=================================================================================================================================================

The DORSOLATERAL PREFRONTAL CORTEX (DLPFC) — right hemisphere. A compute
sub-sub-region of prefrontal, and one of the two stateful children of the
prefrontal family.

Mirror of the left DLPFC package. DLPFC is the working-memory executive: it
holds content online across a delay, applies rules to that content, plans
multi-step actions, and implements cognitive control. On the RIGHT, the
content it holds is predominantly SPATIAL — the visuospatial sketchpad —
and the rules it applies are predominantly spatial/situational. The
mechanics are the same as on the left; the content is mirrored.

DLPFC OWNS PERSISTENT STATE
----------------------------
Identical to the left. DLPFC carries state across ticks:

    working_memory    the working-memory buffer. A structured dict whose
                      slot organisation is documented below. On the
                      right, the contents held in the slots are spatial/
                      visual rather than verbal/symbolic; the slot
                      structure itself is identical.

The state is threaded by prefrontal's encode(): DLPFC receives its state
dict from last tick, returns a new one, and prefrontal stores it for the
next tick. The state-threading contract is uniform across hemispheres.

THE TWO REGISTRY AREAS AND THEIR SHARE
--------------------------------------
DLPFC is composed of two Brodmann areas:

    area 9    the HOLD-and-PLAN anchor.
    area 46   the RULE-and-CONTROL anchor.

The per-area shares are `dlpfc_weight`:

    9 : 46 = 0.55 : 0.45 on both hemispheres.

The shares are STRUCTURAL (equal across hemispheres); only the feature
values inside each area's RIGHT_CONFIG lateralise. The right's area 9
weights spatial WM and spatial planning higher than verbal; the right's
area 46 weights spatial rule content higher than verbal rule content.
Neither of those changes the share — the share is how much of DLPFC's
*aggregate* signal comes from each area, and that is symmetric.

PENDING AMENDMENT (HARD PRECONDITION)
-------------------------------------
This package depends on `brodmann_areas/brodmann_area_9/RIGHT_CONFIG`
containing the field `"dlpfc_weight": 0.55`. At the time this docstring
was written, that field is PENDING on both hemispheres — it is documented
in both area-46 files' SCHEMA ADDITION sections but not yet applied to
area 9's configs.

This package treats the amendment as a HARD PRECONDITION, exactly as the
left does:

    - If `brodmann_area_9.RIGHT_CONFIG["dlpfc_weight"]` is present and
      equals 0.55, the composition proceeds normally.
    - If it is absent, the DLPFC class raises a documented error at
      construction time, pointing at the SCHEMA ADDITION section of
      area-46's docstring. It does NOT silently default, does NOT
      compute a partial composition from area 46 alone, and does NOT
      infer the share.
    - If it is present but not 0.55, the DLPFC class raises ("The DLPFC
      shares are structural (equal across hemispheres) and must sum to
      1.0 across 9 and 46.").

The reason for the hard precondition is the same as on the left: a
silently-defaulted share would produce a subtly wrong DLPFC contribution,
which is worse than a loud construction failure. The amendment is small
and documented; failing loudly until it's applied is correct.

Note that the amendment is PENDING ON BOTH HEMISPHERES, not just the
left. Applying it to the left's area 9 without applying it to the
right's would leave DLPFC's right-hemisphere construction failing while
the left's succeeds — which is a signal that the amendment was applied
asymmetrically, not that the right has a special case.

THE COMPUTATION
---------------
    encode(sensory_input, top_down, peer_input, state, config)
        -> (contribution, new_state)

Identical to the left's. Steps:

        1. Read peer_input — DLPFC is called second in prefrontal's
           order (after DMPFC), so it has access to:
               peer_input["dorsomedial_prefrontal_cortex"]
                   — the current goals
        2. Extract DLPFC features from sensory_input, top_down, and
           peer_input. On the right, the extraction weights spatial/
           visual content higher than verbal/symbolic.
        3. For each area A in {9, 46}:
               for each feature f that A provides:
                   area_contrib_A[f] = extract(f) * A.RIGHT_CONFIG[f]
        4. Combine across areas using the per-area shares:
               for each feature f:
                   contribution[f] = (
                       A9.dlpfc_weight  * area_contrib_9[f]
                     + A46.dlpfc_weight * area_contrib_46[f]
                   )
        5. Update working_memory state (slots, age, salience,
           rehearsed, capacity, decay_rate). On the right, the
           rehearsal/decay dynamics are identical to the left's — the
           mechanism is the same; only the content held differs.
        6. Compute DLPFC's contribution.
        7. Return (contribution, new_state).

THE OVERLAP-AND-SPECIFIC FEATURES
---------------------------------
Identical structure to the left, with the right's feature contents:

    OVERLAPPING FEATURES (both 9 and 46 provide, blended via
    dlpfc_weight):
        verbal_working_memory, spatial_working_memory, planning,
        cognitive_control, response_inhibition, rule_representation,
        task_switching, abstract_reasoning, goal_maintenance,
        distraction_resistance.
        Blend produces a weighted average. On the right, both areas'
        values lean spatial — the blend is the combination of two
        spatial-leaning areas, not a verbal-spatial mix.

    AREA-46-ONLY FEATURES (only area 46 provides, pass through
    without blending):
        rule_maintenance_over_delay, sustained_attention,
        response_monitoring, task_set_binding, verbal_rule_content,
        spatial_rule_content.
        On the right, the rule-content pair weights spatial_rule_content
        higher than verbal_rule_content (via area 46's config). The
        rule-content distinction is the right's signature within area 46.

    AREA-9-ONLY FEATURES: (none at the feature-key level; area 9's
    right-specific content is its spatial-heavy values on the
    overlapping features.)

    The overlap-and-specific rule is identical: overlap features blend;
    area-specific features pass through. The rule is a DLPFC-wide
    pattern, not a left-DLPFC pattern — the right applies the same rule
    to the same feature keys, with right-specific values.

FEATURE EXTRACTION (the DLPFC's inputs)
---------------------------------------
Identical sources to the left:

    From sensory_input:
        content               — verbal/symbolic vs spatial/visual
                                components. On the right, spatial/
                                visual content is weighted higher.
        rule_cues             — task-rule signals.

    From top_down:
        basal_forebrain_gain  — attention/arousal modulator.
        cingulate_control     — targeted control from ACC.
        amygdala_salience     — threat/salience bias.
        basal_ganglia_gate    — previous tick's gating feedback.

    From peer_input:
        goals                 — the current goal from DMPFC. On the
                                right, goals lean spatially-situated
                                and threat-relevant, which biases
                                DLPFC's goal-relevance gate toward
                                spatial content.

The full extraction rules are documented in the DLPFC class
implementation. The feature set, the sources, and the extraction
pattern are identical across hemispheres; only the weighting of the
verbal-vs-spatial content component differs.

WORKING_MEMORY STATE STRUCTURE
------------------------------
    working_memory = {
        "slots":       list of currently held items, each:
                       {"content": <representation>,
                        "age":     <ticks held, incremented per tick>,
                        "salience": <from amygdala_salience>,
                        "rehearsed": <bool, refreshed this tick>},
        "capacity":    int, the maximum number of slots
                       (defaults to 7, from RIGHT_DLPFC_CONFIG),
        "decay_rate":  float per-tick decay probability for unrehearsed
                       items (defaults to 0.15),
    }

The structure is IDENTICAL to the left's. The capacity, the decay rate,
the rehearsal threshold, and the goal-relevance gate are STRUCTURAL —
equal across hemispheres. Only the CONTENT held in the slots differs:
on the right, slots hold spatial/visual content with a bias toward
threat-relevant and spatially-salient items (via DMPFC's goal bias);
on the left, slots hold verbal/symbolic content with the same
structure.

A test that assumed "the right's WM has different parameters" (e.g.
smaller capacity, faster decay) would fail — the parameters are the
same machinery, and the lateralisation is entirely in the content, not
the parameters. This is a common confusion worth flagging: "spatial
WM is right-lateralised" does NOT mean "right WM is a different
mechanism", it means "the right's WM holds spatial content more
readily".

RIGHT-SPECIFIC BIAS
------------------
Same class as the left DLPFC; the RIGHT config changes the weights
(via the two area configs):

    spatial_working_memory   higher weight (via area 9's anchor and
                             area 46's spatial_rule_content coupling)
    verbal_working_memory    lower weight
    rule content             spatial/situational (via area 46's
                             spatial_rule_content weight)
    parietal coupling        stronger (via area 9's to_parietal and
                             area 46's to_parietal)
    temporal coupling        weaker (via area 9's to_temporal and
                             area 46's to_temporal)
    dlpfc_weight             structural (0.55 : 0.45) — same on
                             both hemispheres

The class, the state structure, the composition logic, the blend rule,
and the feature extraction pipeline are IDENTICAL. Only the config
values inside the two area configs differ. LEFT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left DLPFC. Cross-midline working-memory
exchange goes through `telencephalon/commissures/`, never through direct
access.

The right's canonical case is the mirror of the left's: a spatial WM
task may need verbal-symbolic labels from the left DLPFC (e.g. holding
a visual scene while needing to name the objects in it), where the
left's canonical case is a verbal WM task needing spatial content from
the right (e.g. holding a word while visualising its referent). Both
exchanges are commissural, and both directions are real — neither
hemisphere is "the one that owns WM"; they hold different content and
exchange when the task requires the other's content.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not bypass the dlpfc_weight blend by hardcoding a share,
      inferring a share, or defaulting when the area-9 amendment is
      absent. The hard precondition is the contract.
    - Must not silently blend area-46-only features as if area 9
      provided them at weight 0. Overlap-and-specific is explicit.
    - Must not add a sixth contribution to prefrontal.
    - Must not hold module-level mutable state.
    - Must not import `brodmann_areas/` directly — the areas' configs
      are passed in via `config`.
    - Must not change the working-memory parameters (capacity, decay
      rate, rehearsal threshold, goal-relevance gate) on the right.
      These are STRUCTURAL — equal across hemispheres. The right's
      "spatial WM" character lives in the CONTENT weighting, not in
      the state parameters. A test that assumed "right WM has
      different parameters" would fail; a test that assumed "right
      WM parameters are equal to left" would pass. This is a
      deliberate design point, not an oversight.
    - Must not import or reference the left DLPFC. Cross-midline
      exchange goes through the commissures, never through direct
      access. The right's spatial-WM-needing-verbal-labels case is
      exactly a case where direct import would silently bypass the
      commissural delay that gives the model its behavioural
      predictions.
    - Must not diverge in structure from the left DLPFC — same class,
      same encode() signature, same state structure (slots/capacity/
      decay_rate with identical parameters), same overlap-and-
      specific composition rule. Only the two area configs' values
      differ.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_DLPFC_CONFIG = {
        # Composition-level config (structural; identical to the
        # left's apart from the area config values it inherits).
        "areas":               ["brodmann_area_9", "brodmann_area_46"],
        "share_field":         "dlpfc_weight",
        "expected_shares": {
            "brodmann_area_9":  0.55,
            "brodmann_area_46": 0.45,
        },

        # Working-memory parameters (STRUCTURAL — identical to the
        # left's. See the "MUST NOT DO" note above.)
        "working_memory_capacity":      7,
        "working_memory_decay_rate":    0.15,
        "rehearsal_threshold":          0.5,

        # Goal-relevance gate (STRUCTURAL).
        "goal_relevance_gate":          0.4,
    }

    The two area configs (brodmann_area_9.RIGHT_CONFIG and
    brodmann_area_46.RIGHT_CONFIG) are supplied by PrefrontalCortex at
    construction time, not built here. They are the source of the
    per-feature values that the blend combines; this package's config
    is only the composition-level parameters and the working-memory
    state parameters.

    RIGHT_DLPFC_CONFIG is IDENTICAL to LEFT_DLPFC_CONFIG except that it
    names the RIGHT_CONFIG exports of the two areas. The working-
    memory parameters, the goal-relevance gate, and the
    expected_shares map are STRUCTURAL — equal across hemispheres.
    A test should assert this equality, separately from the area
    configs' directional mirror tests.

    The expected_shares field is the source of the hard-precondition
    check. If either area's dlpfc_weight disagrees with the expected
    value, the class raises at construction.

EXPORTS
-------
    from .dorsolateral_prefrontal_cortex import DorsolateralPrefrontalCortex
    from .dorsolateral_prefrontal_cortex import RIGHT_DLPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. It raises a construction-time error if
    the right area-9 dlpfc_weight amendment has not been applied.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  DorsolateralPrefrontalCortex class, import the two registry areas'
  RIGHT_CONFIG exports, verify the dlpfc_weight precondition, build
  RIGHT_DLPFC_CONFIG, instantiate the class, expose the class and the
  config. No computation lives here.
- The class implements the sub-sub-region encode() signature. The
  state structure (working_memory with slots/capacity/decay_rate) is
  documented above and implemented in the class.
- The class is STATEFUL — it carries working_memory across ticks via
  the threaded state dict. It must NOT carry module-level mutable
  state.
- The overlap-and-specific composition rule (blend overlap features
  via dlpfc_weight; pass area-specific features through) is a
  documented, unit-testable function (`_combine_areas(...)`).
- The hard precondition on dlpfc_weight is checked at construction,
  against the RIGHT_CONFIG exports of the two areas. If applied, the
  class builds; if not, it raises. Do NOT add a fallback.
- Feature extraction and working-memory update are documented,
  unit-testable functions.
- The class does not import or access any peer sub-sub-region's state.
- RIGHT_DLPFC_CONFIG is structurally identical to LEFT_DLPFC_CONFIG
  except for the values inherited from the two area configs.
  Working-memory parameters, goal-relevance gate, expected_shares,
  and the area list are STRUCTURAL — equal across hemispheres.
  Two separate tests are needed:
    1. RIGHT_DLPFC_CONFIG == LEFT_DLPFC_CONFIG (structural equality).
    2. Each area's RIGHT_CONFIG is a directional mirror of that
       area's LEFT_CONFIG (feature and connectivity values mirror).
  A test that conflated these — e.g. checked working_memory_capacity
  for directionality — would fail spuriously, because capacity is
  structural, not lateralised.
- If a future change wants to add a third DLPFC registry area (unlikely
  — 9 and 46 are the DLPFC pair), the areas list gains an entry, the
  expected_shares map gains an entry, and the shares must still sum
  to 1.0 on both hemispheres.
- Must not import or reference the left DLPFC. Cross-midline exchange
  goes through `telencephalon/commissures/`.
"""