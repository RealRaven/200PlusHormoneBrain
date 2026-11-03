"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.prefrontal_cortex.ventrolateral_prefrontal_cortex
================================================================================================================================================

The VENTROLATERAL PREFRONTAL CORTEX (VLPFC) — left hemisphere. A compute
sub-sub-region of prefrontal, and one of the three pure-function children of
the prefrontal family.

VLPFC is the SELECTION core of the prefrontal cortex: given candidate
interpretations (semantic candidates, phonological candidates, articulatory
candidates, lexical candidates) from upstream, it selects among them based
on value, goal-relevance, task-context, and salience. It is the output-side
of prefrontal — the last sub-sub-region in the composition order, and the
one whose selected candidates feed downstream motor planning and execution.
In the language system, this is Broca's area performing lexical and
articulatory selection; in the general case, it is the selection of any
goal-directed action candidate from a competing set.

VLPFC IS A PURE FUNCTION
-------------------------
VLPFC carries NO persistent state across ticks. It is a pure function of
its inputs: sensory_input, top_down, peer_input, and its config. The parent
(PrefrontalCortex) threads `{}` through VLPFC's state slot, and VLPFC's
encode() does not read or write state.

This is deliberately different from DLPFC (working_memory) and DMPFC
(goal_stack). VLPFC's selection depends on the *current* candidates and
their *current* evaluation, not on a stored selection. Persistence across
ticks (remembering what was selected) is not VLPFC's job — that lives in
the working-memory buffers (DLPFC) and in the downstream motor plan state
(premotor). VLPFC selects this tick; DLPFC remembers next tick.

THE THREE REGISTRY-AREA SOURCES AND THE NESTED GROUPING
-------------------------------------------------------
VLPFC is composed of three Brodmann area sources, structured as a two-level
composition:

    brocas_area (a GROUPING — two member areas share this group):
        brodmann_area_44    pars opercularis, the articulatory/
                            phonological half
        brodmann_area_45    pars triangularis, the lexical/syntactic half

    area_47_vlpfc (a SINGLE-SOURCE group):
        brodmann_area_47    the "ventrolateral_prefrontal_cortex" block of
                            area 47 — value-guided semantic retrieval

This is the LAST new composition shape in the project. It differs from the
two earlier multi-source shapes:

    OFC's three-source composition: flat, all three sources peer, no
    grouping. Shares are (11 : 12 : 47-OFC) directly.

    DLPFC's two-source composition: flat, both sources peer. Shares
    are (9 : 46) directly.

    VLPFC's nested composition: one group (Broca's) with two members,
    plus one single-source group (area 47-VLPFC). The group-level
    share splits between the group and the singleton, then the
    within-group share splits between the two members.

The grouping matters because areas 44 and 45 are not independent
contributors to VLPFC — they are two halves of one functional unit
(Broca's area), whose internal coupling is documented in their own configs
via the `brocas_weight` field (0.55 : 0.45 on the left). VLPFC must
respect that internal split when combining them.

THE COMPOSITION — two-stage blend, then selection
-------------------------------------------------
VLPFC's encode() executes in three stages:

    Stage 1 — within-group blend (Broca's area)
        For each shared feature f (phonological, articulatory,
        lexical_selection, prosodic, syntactic, verbal_working_memory —
        the features present in BOTH area 44's and 45's configs):
            broca_f = (44.brocas_weight * 44.contribution[f]
                     + 45.brocas_weight * 45.contribution[f])
        This is the area-44-and-45 blend by their `brocas_weight`
        (which sums to 1.0 within the group). The result is one
        Broca's-area aggregate contribution.

    Stage 2 — top-level blend (Broca's area vs area 47-VLPFC)
        For each feature f:
            contribution[f] = (
                group_weights["brocas_area"]      * broca_f
              + group_weights["area_47_vlpfc"]    * area_47_vlpfc[f]
            )
        Where group_weights sum to 1.0 across the two groups. For the
        Broca's-shared features, area_47_vlpfc[f] is 0 (area 47 does
        not contribute to those features), so the top-level blend
        simply scales broca_f by 0.75 — but the mechanism is the
        same as for any feature, and it handles feature disjointness
        uniformly.

    Stage 3 — selection operation (VLPFC-specific)
        Given the blended feature vector and the peer_input context
        (goals from DMPFC, WM contents from DLPFC, value from OFC and
        VMPFC), select among the activated candidates. See SELECTION
        OPERATION below.

The two-stage blend mirrors the two-stage structure of the sources. It is
NOT a flat three-way blend — that would ignore the grouping and would let
area 47-VLPFC's contribution be weighed as if it were a peer of 44 and 45
individually. The grouping is a real structural relationship, and the
composition preserves it.

The group weights and the within-group shares:
    group_weights["brocas_area"]      = 0.75     (Broca's area's share of
                                                  VLPFC's aggregate)
    group_weights["area_47_vlpfc"]    = 0.25     (area 47-VLPFC's share)
    within Broca's area:
        area_44's effective share     = 0.75 * 0.55 = 0.4125
        area_45's effective share     = 0.75 * 0.45 = 0.3375
    (The 0.55 : 0.45 within-group split comes from each area's own
    `brocas_weight` field — VLPFC does NOT duplicate this split; it
    reads it from the areas' configs.)

The shares (group-level 0.75/0.25 and the effective per-area 0.4125/
0.3375/0.25) are STRUCTURAL — equal across hemispheres. The 0.75/0.25
split reflects that Broca's area is the dominant VLPFC contributor
(language production is the core function), while area 47's VLPFC block
is a specialized value-guided add-on. The within-group 0.55/0.45 split
reflects Broca's area's internal structure (already established in
44's and 45's registry configs).

THE SELECTION OPERATION (the VLPFC-specific operational pattern)
----------------------------------------------------------------
VLPFC's most distinctive computation is *selection* — picking among the
activated candidates. Each tick:

    1. Identify the CANDIDATE SET. Candidates are the activated items
       from:
           - Broca's area's contribution (phonological candidates:
             which sound sequences; articulatory candidates: which
             motor programs; lexical candidates: which words;
             syntactic candidates: which structures)
           - area 47-VLPFC's contribution (semantic candidates:
             which meanings; scene-semantic candidates: which scene
             interpretations)
       Candidates are items in the feature vector that exceed an
       activation threshold. Weakly-activated candidates are not in
       the set.

    2. Score each candidate on four dimensions:
           value         — from OFC's contribution (stimulus value)
                           and VMPFC's contribution (integrated
                           value), via their peer contributions
           goal_relevance — from DMPFC's contribution (current goal)
           task_relevance — from DLPFC's contribution (working-
                           memory content and rule representation)
           salience       — from top_down["amygdala_salience"]
       The four scores are combined (weighted sum, documented in the
       VLPFC class) into a per-candidate selection score.

    3. Select the top candidate (winner-take-all) OR a soft-max set
       of candidates (if selection_temperature > 0, the VLPFC emits a
       soft distribution; if selection_temperature == 0, it is hard
       winner-take-all). The default is soft with a low temperature
       — selection is usually nearly-hard, but not quite (the small
       soft component models the rare cases where two candidates are
       very close).

    4. Emit both:
           - the blended feature vector (for downstream feature-level
             consumers, e.g. VMPFC's re-evaluation on a later tick)
           - the SELECTION output — the selected candidates, their
             scores, and the selection confidence (how clear the top
             candidate was).

The selection output is what distinguishes VLPFC from the other
prefrontal sub-sub-regions. DLPFC holds, DMPFC manages goals, OFC
evaluates, VMPFC integrates value, VLPFC selects. Each is a distinct
operation, and VLPFC's is the one whose output directly feeds action.

SELECTION IS NOT "PICK THE HIGHEST VALUE"
------------------------------------------
An important clarification: VLPFC's selection is not simply "pick the
candidate with the highest OFC value." A high-value candidate can still
lose if its goal-relevance is low (the goal is "read this word", the
high-value candidate is a food-word irrelevant to reading). A
high-salience candidate can win even at lower value if threat is
involved. A candidate that fits the current rule (from DLPFC) beats a
candidate that fits an older rule. The four dimensions (value, goal,
task, salience) all matter, and their combination is what makes the
selection goal-directed rather than value-maximising.

The combination weights are in LEFT_VLPFC_CONFIG (STRUCTURAL — equal
across hemispheres). A future experiment that changes them is changing
VLPFC's behaviour fundamentally, not cosmetically.

FEATURE EXTRACTION (the VLPFC's inputs)
---------------------------------------
    From sensory_input:
        candidate_content   — the current stimulus's content, used to
                             generate candidates (words, meanings,
                             scene interpretations, articulatory
                             programs)

    From top_down:
        basal_forebrain_gain — attention/arousal
        amygdala_salience    — salience score for candidate scoring
        cingulate_control    — targeted control from ACC
        basal_ganglia_gate   — previous selection's gating feedback
                               (approved/vetoed) — affects the next
                               tick's candidate activation

    From peer_input:
        (VLPFC is called LAST in prefrontal's order, so it sees ALL
        four upstream sub-sub-regions' contributions.)
        peer_input["dorsomedial_prefrontal_cortex"]  — goals (for
            goal_relevance)
        peer_input["dorsolateral_prefrontal_cortex"] — working_memory
            contents and rule representation (for task_relevance)
        peer_input["orbitofrontal_cortex"]           — stimulus value
            (for value score)
        peer_input["ventromedial_prefrontal_cortex"] — integrated
            value (for value score; VMPFC's value is the more
            complete, self-relevant signal)

    The extraction rules are documented in the VLPFC class implementation.

CONTRIBUTION SHAPE
------------------
    contribution = {
        # Blended feature vector (from stage 2) — per-feature
        "phonological":              <blended scalar>,
        "articulatory":              <blended scalar>,
        "lexical_selection":         <blended scalar>,
        "prosodic":                  <blended scalar>,
        "syntactic":                 <blended scalar>,
        "verbal_working_memory":     <blended scalar>,

        "semantic_retrieval":        <scalar>,
        "controlled_semantic_retrieval": <scalar>,
        "semantic_selection":        <scalar>,
        "verbal_fluency":            <scalar>,
        "scene_semantic_control":    <scalar>,
        "language_comprehension_interface": <scalar>,

        # Selection output (from stage 3)
        "selection": {
            "selected":          <list of selected candidate dicts,
                                  each: {content, score, dimension_scores}>,
            "confidence":        <scalar in [0, 1]; 1.0 = unanimous
                                  winner, 0.0 = no clear winner>,
            "candidate_count":   <int>,
        },

        # Broca's-area sub-grouping (optional passthrough for consumers
        # that need to distinguish Broca's area's contribution from
        # area 47-VLPFC's)
        "brocas_area_aggregate": {
            <the un-blended Broca's-area aggregate (before top-level
             blend with area 47-VLPFC), for consumers that want to
             see Broca's-area-only contribution>
        },
    }

The `selection` output is what downstream action consumers read. Premotor
reads `selection["selected"]` to prepare the corresponding movement
program; primary motor reads it to execute; DLPFC reads it (via the next
tick's peer_input) as part of working-memory updating (the selected
candidate is likely to be held).

The `brocas_area_aggregate` is optional passthrough — most consumers
won't need it, but tests that want to verify Broca's-area-only behaviour
in isolation can read it.

LEFT-SPECIFIC BIAS
------------------
Same class as the right VLPFC; the LEFT config changes the weights (via
the three area configs):

    group_weights                structural (0.75 : 0.25) — same on
                                 both hemispheres
    within-group shares          structural (44: 0.55, 45: 0.45,
                                 from brocas_weight) — same on both
                                 hemispheres
    linguistic content           higher weight (via 44/45's left-
                                 leaning lexical/articulatory
                                 features: verbal_fluency 0.75,
                                 lexical_selection 0.80)
    scene-semantic content       lower weight (via 47-VLPFC's left-
                                 leaning verbal_semantic_value)
    to_temporal                  higher (via 44/45's strong temporal
                                 coupling)
    to_broca_area_45             higher (via 47-VLPFC's left-
                                 leaning lexical coupling)

The class, the two-stage composition, the selection operation, the
feature extraction, and the group/share structure are IDENTICAL across
hemispheres. Only the config values inside the three area configs differ.
RIGHT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the right VLPFC. Cross-midline VLPFC exchange is
the most studied case in the frontal lobe, because Broca's area is the
canonical lateralised function:

    - Prosody-to-speech delivery. The left's VLPFC (via 44/45's
      lexical/articulatory features) computes lexical and articulatory
      candidates; the right's VLPFC (via 44/45's prosodic features)
      computes prosodic contour candidates. The two are combined at
      the speech output stage — the left's selection is combined with
      the right's prosodic contour to produce fluent, intoned
      speech. Direct import would silently merge the two, producing
      flat speech (lexicon with no prosody).

    - Value-guided semantic retrieval. When a scene-semantic value
      (from the right's VLPFC area 47 block) needs verbal expression,
      the exchange is commissural. The left can describe the scene
      only if the right's value signal reaches the left's selection.

    - Selection competition. When both hemispheres have activated
      candidates for the same stimulus (common — a word has both a
      lexical and a prosodic activation on both sides, with different
      weights), the two hemispheres' selections may agree or disagree.
      Agreement produces confident selection; disagreement produces
      lower confidence and (often) a slower downstream response.
      The commissures surface the agreement/disagreement signal.

All three are commissural. The prosody-to-speech case is the canonical
Broca's case, and its "flat speech with intact content" failure mode
under commissural cut is one of the cleanest testable predictions in
the frontal lobe.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. VLPFC is pure; remembering what
      was selected is DLPFC's job (working_memory) and premotor's job
      (prepared programs), not VLPFC's.
    - Must not read area 44, 45, or 47's config directly — the configs
      are passed in via `config`.
    - Must not duplicate the within-group 0.55 : 0.45 split in VLPFC's
      config. That split is `brocas_weight` in each area's config;
      VLPFC reads it from there. Duplicating it would create a
      consistency hazard (two places to update when the split changes).
    - Must not flatten the grouping. A flat three-way blend (44, 45,
      47-VLPFC as peers) would ignore the real structural
      relationship between 44 and 45, and would mis-weight area 47's
      contribution. The two-stage blend is the contract.
    - Must not implement selection as "pick the highest OFC value".
      Selection combines four dimensions (value, goal-relevance,
      task-relevance, salience), and the combination weights are in
      LEFT_VLPFC_CONFIG. A "pick the highest value" shortcut would
      produce a different (and wrong) behaviour.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not import `brodmann_areas/` directly.
    - Must not import or reference the right VLPFC. Cross-midline
      exchange goes through the commissures. The prosody-to-speech
      case is a prime example: direct import would silently merge the
      left's lexical content with the right's prosodic content and
      make the "flat speech with intact content" failure mode
      untestable.
    - Must not diverge in structure from the right VLPFC — same class,
      same encode() signature, no state (both pure functions), same
      two-stage composition (group + within-group), same selection
      operation, same feature extraction. Only the three area configs'
      values differ.

LEFT-HEMISPHERE CONFIG
----------------------
    LEFT_VLPFC_CONFIG = {
        # Composition structure (STRUCTURAL).
        "groups": {
            "brocas_area": {
                "members":           ["brodmann_area_44",
                                      "brodmann_area_45"],
                "group_weight":      0.75,
                "within_group_field": "brocas_weight",  # read from
                                                        # each member's
                                                        # config, not
                                                        # duplicated here
            },
            "area_47_vlpfc": {
                "members":           ["brodmann_area_47"],
                "block":             "ventrolateral_prefrontal_cortex",
                "group_weight":      0.25,
            },
        },
        "share_sum_check": 1.0,   # group weights sum to 1.0 (asserted at
                                  # construction); within-group shares
                                  # sum to 1.0 by the areas' own
                                  # brocas_weight constraint

        # Selection parameters (STRUCTURAL).
        "candidate_activation_threshold": 0.3,   # below this, an item
                                                 # is not a candidate
        "selection_dimension_weights": {
            "value":              0.35,
            "goal_relevance":     0.30,
            "task_relevance":     0.20,
            "salience":           0.15,
            # sum to 1.0
        },
        "selection_temperature":  0.1,   # >0 = soft-max; 0 = winner-
                                         # take-all. Default is a very
                                         # low temperature (nearly hard
                                         # selection, with a small soft
                                         # component for near-tie cases)
        "selection_confidence_gap_threshold": 0.15,  # above this gap
                                         # between top and second
                                         # candidate, confidence is
                                         # "clear"; below, confidence
                                         # drops
    }

    The three area configs (brodmann_area_44.LEFT_CONFIG,
    brodmann_area_45.LEFT_CONFIG, brodmann_area_47.LEFT_CONFIG[
    "ventrolateral_prefrontal_cortex"]) are supplied by PrefrontalCortex
    at construction, not built here.

    RIGHT_VLPFC_CONFIG is IDENTICAL except that it names the
    RIGHT_CONFIG exports of the three areas. Group weights, within-
    group field name, and selection parameters are STRUCTURAL — equal
    across hemispheres. The lateralisation lives entirely in the three
    areas' feature weights and connectivity priors.

    Two separate tests are needed:
        1. RIGHT_VLPFC_CONFIG == LEFT_VLPFC_CONFIG on group weights,
           share sum, within-group field name, and selection
           parameters (structural equality).
        2. Each of the three areas' RIGHT_CONFIG is a directional
           mirror of that area's LEFT_CONFIG (feature and connectivity
           values mirror).

EXPORTS
-------
    from .ventrolateral_prefrontal_cortex import VentrolateralPrefrontalCortex
    from .ventrolateral_prefrontal_cortex import LEFT_VLPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. No dlpfc_weight-style precondition: the
    group weights are in LEFT_VLPFC_CONFIG, and the within-group shares
    come from the areas' own brocas_weight (which is present and correct
    in 44's and 45's registry configs, no amendment pending).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  VentrolateralPrefrontalCortex class, import the three area configs
  (brodmann_area_44, brodmann_area_45, and brodmann_area_47's VLPFC
  block), verify the group-weight sum precondition, build
  LEFT_VLPFC_CONFIG, instantiate the class, expose the class and the
  config.
- The class implements the sub-sub-region encode() signature. VLPFC is
  PURE — its state input is always {} and its output state is always
  {}.
- The two-stage composition is implemented as two documented, unit-
  testable functions:
      `_blend_brocas_area(area_44_contribution, area_45_contribution,
                          brocas_weight_44, brocas_weight_45)`
          -> broca_aggregate
      `_blend_groups(broca_aggregate, area_47_vlpfc_contribution,
                     group_weights)`
          -> final_contribution
  Each is tested with synthetic inputs.
- The selection operation is a documented, unit-testable function
  (`_select(blended_contribution, peer_context, top_down, config) ->
  selection_dict`). It reads the four dimensions, combines them per
  `selection_dimension_weights`, applies soft-max at the configured
  temperature, computes confidence, and returns the selection dict.
- Feature extraction is a documented, unit-testable function.
- The class does not import or access any peer sub-sub-region's state
  — it reads peer_input contributions (goals from DMPFC, WM from
  DLPFC, value from OFC and VMPFC).
- The within-group 0.55 : 0.45 split is NOT stored in
  LEFT_VLPFC_CONFIG. The class reads it from `brodmann_area_44.
  LEFT_CONFIG["brocas_weight"]` and `brodmann_area_45.LEFT_CONFIG
  ["brocas_weight"]` (both are already present in the areas' configs).
  A test should assert that these sum to 1.0 within the group.
- LEFT_VLPFC_CONFIG is structurally identical to RIGHT_VLPFC_CONFIG
  except for the area-config source references (LEFT vs RIGHT). Group
  weights and selection parameters are STRUCTURAL.
- Selection confidence is `confidence_gap_threshold`-gated: if the
  gap between the top and second candidates exceeds the threshold,
  confidence is reported as "clear" (high); otherwise, it is scaled
  by the gap. This gives a testable confidence signal that a
  downstream consumer (premotor, for motor readiness) can use to
  adjust its behaviour.
- If a future change wants to add a fourth VLPFC source (unlikely
  without anatomy changes), the groups map gains an entry (either as
  a new group, or as a member of an existing group), the group weights
  must still sum to 1.0, and within-group shares must still sum to
  1.0. This is a substantive modeling decision, not a config tweak.
- Must not import or reference the right VLPFC. Cross-midline exchange
  goes through `telencephalon/commissures/`.
"""