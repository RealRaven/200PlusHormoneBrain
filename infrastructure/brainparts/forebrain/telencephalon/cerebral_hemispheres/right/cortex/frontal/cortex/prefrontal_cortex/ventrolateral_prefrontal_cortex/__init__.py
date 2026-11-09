"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.prefrontal_cortex.ventrolateral_prefrontal_cortex
================================================================================================================================================

The VENTROLATERAL PREFRONTAL CORTEX (VLPFC) — right hemisphere. A compute
sub-sub-region of prefrontal, and one of the three pure-function children of
the prefrontal family.

Mirror of the left VLPFC package. VLPFC is the SELECTION core of the
prefrontal cortex: given candidate interpretations from upstream, it selects
among them based on value, goal-relevance, task-context, and salience. On
the RIGHT, the candidates selected are more prosodic and scene-semantic in
character — the right's VLPFC evaluates and selects among expressive-
prosodic candidates (intonation contours, affective vocalizations) and
scene-semantic candidates (which visual interpretation of a scene to
select), where the left's selects among lexical/articulatory/verbal
candidates. The mechanics of the selection are the same; the content is
mirrored.

VLPFC IS A PURE FUNCTION
-------------------------
Identical to the left. VLPFC carries NO persistent state across ticks. It
is a pure function of its inputs. The parent threads `{}` through VLPFC's
state slot, and VLPFC's encode() does not read or write state.

THE THREE REGISTRY-AREA SOURCES AND THE NESTED GROUPING
-------------------------------------------------------
VLPFC is composed of three Brodmann area sources, structured as a
two-level composition:

    brocas_area (a GROUPING — two member areas share this group):
        brodmann_area_44    pars opercularis
        brodmann_area_45    pars triangularis

    area_47_vlpfc (a SINGLE-SOURCE group):
        brodmann_area_47    the "ventrolateral_prefrontal_cortex" block of
                            area 47 — value-guided semantic retrieval

On the right, the Broca's-area members carry the prosodic roles (44 =
expressive prosody, 45 = prosodic-lexical interface) rather than the
left's lexical/articulatory roles. The grouping structure is identical —
the right's Broca's area is still a coupled pair, and its two members
still share a `brocas_weight` split (0.45 : 0.55 on the right, mirroring
the left's 0.55 : 0.45).

The grouping is preserved structurally for the same reason as on the
left: areas 44 and 45 are not independent contributors to VLPFC, they
are two halves of one functional unit, whose internal coupling is
documented via the `brocas_weight` field. The right's `brocas_weight`
split (44: 0.45, 45: 0.55) is the mirror of the left's — on the right,
area 45 (the prosodic-lexical interface) takes the larger share, because
the right's Broca's-area contribution is prosody-anchored.

THE COMPOSITION — two-stage blend, then selection
-------------------------------------------------
Identical to the left. VLPFC's encode() executes in three stages:

    Stage 1 — within-group blend (Broca's area)
        For each shared feature f (phonological, articulatory,
        lexical_selection, prosodic, syntactic, verbal_working_memory):
            broca_f = (44.brocas_weight * 44.contribution[f]
                     + 45.brocas_weight * 45.contribution[f])
        On the right, the blend gives more weight to area 45's
        prosodic-lexical-interface features; the mechanism is the same.

    Stage 2 — top-level blend (Broca's area vs area 47-VLPFC)
        For each feature f:
            contribution[f] = (
                group_weights["brocas_area"]      * broca_f
              + group_weights["area_47_vlpfc"]    * area_47_vlpfc[f]
            )
        Group weights are 0.75 : 0.25 (structural, same as left). On
        the right, area 47-VLPFC's contribution leans scene-semantic
        (via its scene_semantic_control feature), so the right's
        combined VLPFC output leans toward scene-semantic selection
        rather than verbal selection.

    Stage 3 — selection operation (VLPFC-specific)
        Same as the left: identify candidates, score on four
        dimensions (value, goal-relevance, task-relevance, salience),
        combine per selection_dimension_weights, soft-max at the
        configured temperature, emit selection dict. On the right,
        the candidate set is prosodic/scene-semantic; the scoring
        dimensions and their combination weights are the same.

The group weights (0.75 : 0.25) and the within-group shares (from
`brocas_weight`) are the same as on the left. The two-stage structure,
the blend function signatures, and the selection scoring formula are
all structural — identical across hemispheres. Only the config values
inside the three areas differ.

THE SELECTION OPERATION (the VLPFC-specific operational pattern)
----------------------------------------------------------------
Same as the left. See the left VLPFC docstring for the full selection
mechanics; summarised:

    1. Identify the candidate set (from the blended feature vector,
       items above candidate_activation_threshold).
    2. Score each candidate on four dimensions:
           value            — from OFC and VMPFC contributions
           goal_relevance   — from DMPFC's current goal
           task_relevance   — from DLPFC's working-memory / rule
           salience         — from top_down["amygdala_salience"]
    3. Select via soft-max at the configured temperature.
    4. Emit selection (selected candidates, confidence, candidate
       count) plus the blended feature vector and the Broca's-area
       aggregate passthrough.

On the right, the four dimensions are the same, but their WEIGHTINGS
with respect to right-specific candidates differ implicitly: a
prosodic candidate's "value" score is driven by OFC's affective value
(right's OFC is threat/visceral-leaning), a scene-semantic candidate's
"task-relevance" score is driven by DLPFC's spatial WM, and so on. The
scoring formula is structural; the inputs to it are lateralised.

SELECTION IS NOT "PICK THE HIGHEST VALUE"
------------------------------------------
Same clarification as on the left: selection combines four dimensions,
not just value. On the right specifically, the "salience" dimension is
often more influential because threat-relevant prosodic cues and
threat-relevant scene-semantic candidates can win selection even at
moderate value — the right's selection is more salience-sensitive,
consistent with the right's overall threat-attentive profile. This is
expressed via the higher `to_amygdala` prior in the relevant area
configs, not via a different selection formula.

FEATURE EXTRACTION (the VLPFC's inputs)
---------------------------------------
    From sensory_input:
        candidate_content   — the current stimulus's content. On the
                             right, this includes prosodic cues
                             (intonation contours, emotional tone,
                             vocal affect) and scene-semantic cues
                             (visual scene interpretations, spatial
                             object associations), with the prosodic
                             and scene-semantic candidates weighted
                             higher than verbal/lexical ones.

    From top_down:
        (same four modulators as left: basal_forebrain_gain,
        amygdala_salience, cingulate_control, basal_ganglia_gate)

    From peer_input:
        (VLPFC is called LAST, so it sees all four upstream sub-sub-
        regions' contributions.)
        peer_input["dorsomedial_prefrontal_cortex"]  — goals
        peer_input["dorsolateral_prefrontal_cortex"] — WM contents
        peer_input["orbitofrontal_cortex"]           — stimulus value
        peer_input["ventromedial_prefrontal_cortex"] — integrated
            value (self-relevant; on the right, this is affectively
            weighted)

    The extraction rules are documented in the VLPFC class
    implementation. On the right, the extraction weights prosodic
    features and scene-semantic features higher than verbal/lexical.

CONTRIBUTION SHAPE
------------------
    contribution = {
        # Blended feature vector (from stage 2)
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
            "selected":          <list of selected candidate dicts>,
            "confidence":        <scalar in [0, 1]>,
            "candidate_count":   <int>,
        },

        # Broca's-area sub-grouping (optional passthrough)
        "brocas_area_aggregate": {
            <the un-blended Broca's-area aggregate, for tests>
        },
    }

The schema is identical to the left's. The right's contents are more
prosodic and scene-semantic (prosodic feature weight higher,
scene_semantic_control higher, verbal_fluency lower); the schema is
unchanged.

The `selection["selected"]` output is what downstream action consumers
read. Premotor reads it to prepare prosodic motor programs (for the
right's speech-adjacent role) or scene-driven movement programs (for
the right's broader spatial role). Primary motor reads it to drive the
corresponding effectors.

RIGHT-SPECIFIC BIAS
------------------
Same class as the left VLPFC; the RIGHT config changes the weights
(via the three area configs):

    group_weights                structural (0.75 : 0.25) — same on
                                 both hemispheres
    within-group shares          structural (44: 0.45, 45: 0.55 on
                                 the right, from brocas_weight —
                                 mirror of the left's 0.55 : 0.45)
    prosodic content             higher weight (via 44/45's right-
                                 leaning prosodic features: prosodic
                                 0.80 in area 44, 0.85 in area 45)
    scene-semantic content       higher weight (via 47-VLPFC's right-
                                 leaning scene_semantic_control 0.70)
    verbal_fluency               lower (via 44/45's right-leaning
                                 verbal_fluency 0.40, down from
                                 left's 0.75)
    lexical_selection            lower (via 45's right-leaning
                                 lexical_selection 0.25)
    to_temporal                  lower (via 44/45's lower temporal
                                 coupling — semantic content still
                                 reaches VLPFC, but through less
                                 language-tuned routes)
    to_broca_area_45             lower (via 47-VLPFC's lower lexical
                                 coupling on the right)

The class, the two-stage composition, the selection operation, the
feature extraction, and the group/share structure are IDENTICAL across
hemispheres. Only the config values inside the three area configs
differ. LEFT mirrors.

CROSS-MIDLINE RULE
------------------
No import or read of the left VLPFC. Cross-midline VLPFC exchange is
the most studied case in the frontal lobe, and on the right the cases
emphasise the right's role as the SENDER in the prosody-to-speech
handoff:

    - Prosody-to-speech delivery (the right's primary cross-midline
      role). The right's VLPFC computes prosodic contour candidates
      (intonation, emotional tone, emphatic stress); the left's
      computes lexical and articulatory candidates. The two are
      combined at the speech output stage, and the combination
      happens via the commissures. The right's selection output is
      what reaches the left's motor execution for prosodic delivery.
      Direct import would silently merge the two, producing flat
      speech (lexicon intact, prosody absent).

    - Scene-semantic handoff. When a scene-semantic value (from the
      right's VLPFC area 47-VLPFC) needs verbal expression, the
      exchange is commissural. The left can describe the scene only
      if the right's selection output reaches the left's verbal
      selection.

    - Selection competition. When both hemispheres have activated
      candidates for the same stimulus (common — a word has both a
      lexical activation on the left and a prosodic activation on the
      right, weighted differently), the two hemispheres' selections
      may agree or disagree. Agreement produces confident selection;
      disagreement produces lower confidence and (often) a slower
      downstream response. The commissures surface the agreement/
      disagreement signal.

All three are commissural. The prosody-to-speech case is the canonical
Broca's case from the right's side, and its "flat speech with intact
content" failure mode under commissural cut is the mirror of the left's
described case — same failure mode, opposite sending side.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not carry persistent state. VLPFC is pure on the right as
      on the left; remembering what was selected is DLPFC's job and
      premotor's job.
    - Must not read area 44, 45, or 47's config directly — the configs
      are passed in via `config`.
    - Must not duplicate the within-group 0.45 : 0.55 split (right's
      values) in VLPFC's config. That split is `brocas_weight` in each
      area's RIGHT_CONFIG; VLPFC reads it from there.
    - Must not flatten the grouping. Two-stage blend is the contract;
      a flat three-way blend would ignore the real structural
      relationship between 44 and 45 and mis-weight area 47's
      contribution.
    - Must not implement selection as "pick the highest OFC value".
      The four-dimension formula is structural, identical to the
      left's.
    - Must not change the selection parameters (dimension weights,
      temperature, activation threshold) on the right. These are
      STRUCTURAL — equal across hemispheres. The right's more
      salience-sensitive selection emerges from the higher salience
      *inputs* (via amygdala_salience's stronger influence through
      the areas' configs), not from a different selection formula. A
      test that assumed "right VLPFC has different selection
      parameters" would fail; the parameters are equal, and the
      behavioural difference emerges from the lateralised inputs.
    - Must not change the group weights (0.75 : 0.25) or the within-
      group shares' SUM (which is 1.0 by the areas' own brocas_weight
      constraint). The right's within-group split (0.45 : 0.55) is the
      mirror of the left's (0.55 : 0.45); both sum to 1.0. The
      group weights themselves are equal across hemispheres.
    - Must not inspect or mutate peer sub-sub-regions' state.
    - Must not import `brodmann_areas/` directly.
    - Must not import or reference the left VLPFC. Cross-midline
      exchange goes through the commissures. The prosody-to-speech
      case is the prime example: direct import would silently merge
      the right's prosodic contour with the left's lexical content
      and make the "flat speech with intact content" failure mode
      untestable.
    - Must not diverge in structure from the left VLPFC — same class,
      same encode() signature, no state (both pure functions), same
      two-stage composition, same selection operation, same feature
      extraction. Only the three area configs' values differ.

RIGHT-HEMISPHERE CONFIG
-----------------------
    RIGHT_VLPFC_CONFIG = {
        # Composition structure (STRUCTURAL — identical to the left's).
        "groups": {
            "brocas_area": {
                "members":           ["brodmann_area_44",
                                      "brodmann_area_45"],
                "group_weight":      0.75,
                "within_group_field": "brocas_weight",  # read from
                                                        # each member's
                                                        # RIGHT_CONFIG
            },
            "area_47_vlpfc": {
                "members":           ["brodmann_area_47"],
                "block":             "ventrolateral_prefrontal_cortex",
                "group_weight":      0.25,
            },
        },
        "share_sum_check": 1.0,

        # Selection parameters (STRUCTURAL — identical to the left's).
        "candidate_activation_threshold": 0.3,
        "selection_dimension_weights": {
            "value":              0.35,
            "goal_relevance":     0.30,
            "task_relevance":     0.20,
            "salience":           0.15,
        },
        "selection_temperature":  0.1,
        "selection_confidence_gap_threshold": 0.15,
    }

    The three area configs (brodmann_area_44.RIGHT_CONFIG,
    brodmann_area_45.RIGHT_CONFIG, brodmann_area_47.RIGHT_CONFIG[
    "ventrolateral_prefrontal_cortex"]) are supplied by PrefrontalCortex
    at construction, not built here.

    RIGHT_VLPFC_CONFIG is IDENTICAL to LEFT_VLPFC_CONFIG except that it
    names the RIGHT_CONFIG exports of the three areas. Group weights,
    within-group field name, and selection parameters are STRUCTURAL —
    equal across hemispheres.

    Two separate tests are needed:
        1. RIGHT_VLPFC_CONFIG == LEFT_VLPFC_CONFIG on group weights,
           share sum, within-group field name, and selection
           parameters.
        2. Each of the three areas' RIGHT_CONFIG is a directional
           mirror of that area's LEFT_CONFIG. Note: the within-group
           `brocas_weight` values are in this directional-mirror test
           (left's 0.55 : 0.45 becomes right's 0.45 : 0.55; both sum
           to 1.0). The `brocas_weight` fields are per-area
           directional, not structural — they're how the within-group
           share tilts on each side.

EXPORTS
-------
    from .ventrolateral_prefrontal_cortex import VentrolateralPrefrontalCortex
    from .ventrolateral_prefrontal_cortex import RIGHT_VLPFC_CONFIG

    The class implements the sub-sub-region encode() signature that
    PrefrontalCortex expects. No dlpfc_weight-style precondition: the
    group weights are in RIGHT_VLPFC_CONFIG, and the within-group
    shares come from the areas' own brocas_weight (which is present and
    correct in 44's and 45's RIGHT_CONFIGs, no amendment pending).


Programming contract for this package
-------------------------------------
- This __init__.py is a thin instantiation module: import the shared
  VentrolateralPrefrontalCortex class, import the three area configs
  (brodmann_area_44, brodmann_area_45, and brodmann_area_47's VLPFC
  block), verify the group-weight sum precondition, build
  RIGHT_VLPFC_CONFIG, instantiate the class, expose the class and the
  config.
- The class implements the sub-sub-region encode() signature. VLPFC is
  PURE — state input is always {}, output state is always {}.
- The two-stage composition is implemented as two documented,
  unit-testable functions (`_blend_brocas_area`,
  `_blend_groups`). Same functions as on the left; only the config
  values feeding them differ.
- The selection operation is a documented, unit-testable function
  (`_select`). Reads four dimensions per selection_dimension_weights,
  applies soft-max at selection_temperature, computes confidence.
- Feature extraction is a documented, unit-testable function. On the
  right, extraction weights prosodic and scene-semantic content higher
  than verbal/lexical.
- The class does not import or access any peer sub-sub-region's state.
- The within-group 0.45 : 0.55 split is NOT stored in
  RIGHT_VLPFC_CONFIG. The class reads it from
  `brodmann_area_44.RIGHT_CONFIG["brocas_weight"]` and
  `brodmann_area_45.RIGHT_CONFIG["brocas_weight"]`. A test should
  assert that these sum to 1.0 within the group.
- RIGHT_VLPFC_CONFIG is structurally identical to LEFT_VLPFC_CONFIG
  except for the area-config source references (RIGHT vs LEFT). Group
  weights and selection parameters are STRUCTURAL. The
  `brocas_weight` values inside the areas are DIRECTIONAL (per-area
  feature weights), tested via the area configs' mirror check.
- Selection confidence is `confidence_gap_threshold`-gated; same
  mechanism as the left.
- If a future change wants to add a fourth VLPFC source, the groups
  map gains an entry, group weights must sum to 1.0, and within-group
  shares must sum to 1.0.
- Must not import or reference the left VLPFC. Cross-midline exchange
  goes through `telencephalon/commissures/`.
"""