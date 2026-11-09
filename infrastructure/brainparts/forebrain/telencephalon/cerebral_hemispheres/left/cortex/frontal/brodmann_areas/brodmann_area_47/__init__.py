"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_47
======================================================================================================================

Brodmann area 47 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 47, says which compute sub-regions own it,
and supplies the per-area weights that the owning sub-regions' `encode()`
methods read. It defines no classes and no functions; the public surface
is the exports listed under "EXPORTS".

If you are looking for the computation area 47 participates in, it lives
in TWO compute sub-regions of the same prefrontal family:
    `.../frontal/cortex/prefrontal_cortex/orbitofrontal_cortex/`
        (areas 11, 12, AND the OFC portion of 47)
    `.../frontal/cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/`
        (areas 44, 45, AND the VLPFC portion of 47)
Area 47 is the ONLY frontal area that contributes to two sub-regions of
the same family. This is what makes it the last distinct schema shape in
the frontal registry.

WHAT AREA 47 IS (functionally)
------------------------------
Brodmann area 47 is the orbital part of the inferior frontal gyrus,
extending onto the orbital surface. It sits functionally at the junction
between two prefrontal sub-regions:

    OFC (areas 11, 12)       stimulus-outcome learning; "what is this
                             worth right now?"
    VLPFC (areas 44, 45)     semantic retrieval, selection, and
                             language control; "what does this mean,
                             and which meaning do I select?"

Area 47 is the *bridge* between them, and its specific contribution is
**value-guided semantic retrieval**: it uses reward/outcome value to
guide which semantic content gets retrieved and selected. The OFC
portion of 47 evaluates the value of semantic candidates; the VLPFC
portion of 47 performs the retrieval and selection based on that value.
Neither portion is a duplicate of the areas it sits alongside — 11/12
evaluate all outcomes (not just semantic ones); 44/45 handle language
control (not value-guided language control). Area 47 is the point where
value and semantic selection meet, and that's why it can't be cleanly
filed under either OFC or VLPFC alone.

The other interpretation sometimes offered — that area 47 is "just" a
VLPFC area with some OFC-adjacent features — understates the value
component. The left/right asymmetry matters here too: on the left,
value-guided retrieval is verbally mediated (which words are worth
retrieving?); on the right, it's more semantically/spatially mediated
(which scene-object associations are worth retrieving?).

THE SCHEMA SHAPE — multi-sub-region-within-one-family
------------------------------------------------------
Areas 6, 8, and 47 are all multi-system entries, but they are three
different shapes:

    area 6    TWO LEAF SYSTEMS. Blocks keyed by system name
              ("premotor_cortex", "supplementary_motor_cortex"),
              no `sub_region` field inside. Established the
              per-system block pattern.

    area 8    ONE LEAF + ONE FAMILY. Blocks keyed by system name
              ("premotor_cortex", "prefrontal_cortex"), and the
              family block carried a `sub_region` field inside
              ("dorsomedial_prefrontal_cortex"). Established the
              per-block `sub_region` field pattern.

    area 47   ONE FAMILY, TWO SUB-REGIONS. The two blocks are both
              from `prefrontal_cortex`; the "block key = system name"
              convention would produce two blocks with the same key,
              which is impossible. Block keys are therefore the
              SUB-REGION names themselves ("orbitofrontal_cortex",
              "ventrolateral_prefrontal_cortex"), and NO `sub_region`
              field is used inside them (the key IS the identifier).

The refinement is minimal but it needed to be documented, because a
future contributor reading areas 6, 8, and 47 in sequence could
otherwise conclude that the schema was inconsistent. It isn't — each
of the three shapes follows the same underlying rule ("the block key
must uniquely identify the consuming sub-region"), and that rule
happens to be satisfiable three different ways depending on whether
the systems are leaf, family, or multiple sub-regions of the same
family.

    UNDERLYING RULE: block key MUST uniquely identify the consuming
    sub-region. When the consumer is a leaf system, its name is
    unique. When the consumer is a sub-region of a family and only
    ONE sub-region of that family is involved, the family name plus a
    `sub_region` field disambiguates. When TWO OR MORE sub-regions of
    the same family are involved, the sub-region names must be used
    directly as keys (since the family name isn't unique within the
    config).

PENDING SCHEMA AMENDMENT (optional): area 8's `prefrontal_cortex`
block could be renamed to `dorsomedial_prefrontal_cortex` to match the
"sub-region name as key" convention introduced here, with the
`sub_region` field removed (redundant). The amendment is not required
— area 8's current arrangement works, because only one sub-region of
the family is involved there — but it would make the schema uniform
across all multi-system areas. Documented here so that if a future
refactor wants to normalise, there's a target state; not applied now
to avoid churning area 8's file for a cosmetic change.

IDENTITY
--------
    AREA_ID    = 47
    NAME       = "Brodmann area 47"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = None         # multi-sub-region — see per-block keys
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # not part of Broca's area

Note on SUB_REGION being None with a non-trivial config: as with areas
6 and 8, the package-level SUB_REGION is None because the area spans
more than one sub-region. Here the two sub-regions are both from
prefrontal_cortex, and their disambiguation is carried by the block
KEYS (not a `sub_region` field inside blocks — see SCHEMA SHAPE above).

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 47",
        "system": "prefrontal_cortex (spanning OFC and VLPFC)",
        "sub_region": None,
        "grouping": None,
        "location": "the orbital part of the inferior frontal gyrus, "
                    "extending from the anterior horizontal ramus of "
                    "the lateral sulcus caudally, and onto the "
                    "orbital surface where it meets the anterior "
                    "orbital gyri; between area 45 (VLPFC, rostral) "
                    "and area 12 (posterior OFC, ventromedial)",
        "cytoarchitecture": "granular cortex; heavily granulated in "
                            "the more VLPFC-like posterior portion, "
                            "lighter in the anterior orbital portion "
                            "approaching the OFC transition; "
                            "subdivided into 47a and 47b by some "
                            "authors, though the boundary is "
                            "variable",
        "notes": (
            "Brodmann area 47 is the orbital part of the inferior "
            "frontal gyrus and the bridge between the orbitofrontal "
            "and ventrolateral prefrontal sub-regions. Its specific "
            "function is value-guided semantic retrieval: using "
            "reward/outcome value to guide which semantic content "
            "gets retrieved and selected. The OFC portion of 47 "
            "evaluates the value of semantic candidates; the VLPFC "
            "portion performs the retrieval and selection. This makes "
            "area 47 the only frontal area that contributes to two "
            "sub-regions of the same family (OFC and VLPFC) without "
            "being a clear member of either alone. On the left, "
            "value-guided retrieval is verbally mediated — which "
            "words are worth retrieving, which meaning fits best — "
            "and the left's area 47 is a key node in controlled "
            "verbal fluency. On the right, value-guided retrieval is "
            "more scene/semantic and less language-specific — which "
            "object associations are worth retrieving, which scene "
            "interpretation fits best — and the right's area 47 is "
            "more engaged in non-verbal semantic control. The "
            "left/right split is directional, not complementary — "
            "the right's area 47 is scene-semantic-forward, not 'the "
            "left's at reduced weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 47's LEFT_CONFIG has two per-sub-region blocks, keyed by the
sub-region names themselves (no `sub_region` field inside, because the
key IS the identifier — see SCHEMA SHAPE above).

    LEFT_CONFIG = {

        # ============================================================
        # FIRST BLOCK — orbitofrontal_cortex
        # (the value side of value-guided semantic retrieval)
        # ============================================================
        # Area 47's OFC block contributes to the OFC compute
        # sub-region alongside areas 11 and 12. Its specific
        # contribution is the value of SEMANTIC candidates:
        # evaluating how much a given semantic content (word,
        # concept, meaning) is worth retrieving.
        "orbitofrontal_cortex": {
            # ---- feature emphases ----
            # LEFT bias: verbal-semantic content is the thing whose
            # value is being evaluated on the left.
            "semantic_value_evaluation":  0.80,  # evaluating the
                                                 # reward/outcome
                                                 # value of semantic
                                                 # candidates
            "value_guided_retrieval":     0.75,  # using value to
                                                 # guide which
                                                 # semantic content
                                                 # to retrieve
            "semantic_outcome_prediction":0.70,  # predicting what
                                                 # semantic outcome a
                                                 # cue will lead to
            "verbal_semantic_value":      0.75,  # value of verbal
                                                 # semantic content;
                                                 # the left's anchor
            "scene_semantic_value":       0.40,  # value of
                                                 # scene/visual
                                                 # semantic content;
                                                 # more right-
                                                 # weighted

            # ---- connectivity priors ----
            "to_nucleus_accumbens":       0.70,  # reward-value
                                                 # source; the OFC
                                                 # block reads it
                                                 # directly
            "to_amygdala":                0.55,  # affective-value
                                                 # source; lower
                                                 # here than area 12
                                                 # (semantic value
                                                 # is less directly
                                                 # affective)
            "to_vmpfc":                   0.70,  # value-to-
                                                 # integration path
                                                 # toward VMPFC
            "to_temporal":                0.70,  # semantic-content
                                                 # source (middle
                                                 # temporal gyrus);
                                                 # the OFC block
                                                 # evaluates the
                                                 # value of what
                                                 # temporal retrieves
            "to_ventrolateral_prefrontal_cortex": 0.75,
                                                 # the bridge to
                                                 # area 47's VLPFC
                                                 # block — value
                                                 # feeds selection
            "to_basal_ganglia":           0.60,  # value → action
                                                 # gating
            "to_commissures":             0.45,  # cross-midline
                                                 # value exchange
        },

        # ============================================================
        # SECOND BLOCK — ventrolateral_prefrontal_cortex
        # (the retrieval/selection side of value-guided semantic
        # retrieval)
        # ============================================================
        # Area 47's VLPFC block contributes to the VLPFC compute
        # sub-region alongside areas 44 and 45. Its specific
        # contribution is CONTROLLED semantic retrieval — retrieving
        # and selecting semantic content under value-driven
        # constraint. This is distinct from area 44's articulatory
        # role and area 45's lexical-selection role; area 47's
        # VLPFC block adds the value-guided dimension to selection.
        "ventrolateral_prefrontal_cortex": {
            # ---- feature emphases ----
            # LEFT bias: verbal-semantic retrieval is the dominant
            # operation on the left.
            "semantic_retrieval":         0.80,  # retrieving
                                                 # semantic knowledge
            "controlled_semantic_retrieval": 0.80,  # retrieval under
                                                    # value-driven or
                                                    # task-driven
                                                    # constraint; the
                                                    # left's anchor
            "semantic_selection":         0.75,  # selecting among
                                                 # competing semantic
                                                 # candidates
            "verbal_fluency":             0.75,  # generating words
                                                 # under constraint;
                                                 # the left's
                                                 # signature
                                                 # operation
            "scene_semantic_control":     0.40,  # controlling scene/
                                                 # object-semantic
                                                 # retrieval; more
                                                 # right-weighted
            "language_comprehension_interface": 0.70,
                                                 # coupling to
                                                 # Wernicke's area
                                                 # and the semantic
                                                 # network

            # ---- connectivity priors ----
            "to_temporal":                0.80,  # semantic-network
                                                 # coupling (middle
                                                 # and inferior
                                                 # temporal); the
                                                 # VLPFC block's
                                                 # dominant input
            "to_middle_temporal_gyrus":   0.75,  # semantic-content
                                                 # source
            "to_angular_gyrus":           0.65,  # semantic
                                                 # integration
                                                 # (parietal)
            "to_arcuate_fasciculus":      0.65,  # dorsal language
                                                 # pathway to
                                                 # Wernicke's
            "to_broca_area_45":           0.70,  # lexical-selection
                                                 # coupling —
                                                 # area 47's
                                                 # controlled
                                                 # retrieval feeds
                                                 # area 45's
                                                 # selection
            "to_orbitofrontal_cortex":    0.75,  # the bridge back to
                                                 # area 47's OFC
                                                 # block — value
                                                 # arrives here as
                                                 # a constraint
            "to_basal_ganglia":           0.65,  # selection
                                                 # gating
            "to_commissures":             0.50,  # cross-midline
                                                 # semantic exchange
        },
    }

    Notes on the weights:
      - The two blocks are INDEPENDENT configs consumed by different
        compute sub-regions. The OFC sub-region reads only
        `LEFT_CONFIG["orbitofrontal_cortex"]`; the VLPFC sub-region
        reads only `LEFT_CONFIG["ventrolateral_prefrontal_cortex"]`.
        Neither sub-region sees the other's block.
      - The two blocks are COUPLED through their mutual
        `to_ventrolateral_prefrontal_cortex` / `to_orbitofrontal_cortex`
        connectivity priors (0.75 each). This is the value-to-
        selection handoff that makes area 47 a bridge rather than two
        unrelated contributions. If a future experiment probes
        value-guided semantic retrieval specifically, that coupling
        is what to look at.
      - There is NO sum-to-1 invariant across the two blocks. They
        are consumed independently; each is normalised by its own
        compute sub-region's internal logic.
      - Feature weights are multipliers on features extracted by the
        corresponding sub-region. The left's anchors are
        `semantic_value_evaluation` (0.80, in the OFC block) and
        `controlled_semantic_retrieval` (0.80, in the VLPFC block) —
        the two halves of "value-guided semantic retrieval", one in
        each block.
      - `to_amygdala` is lower in the OFC block (0.55) than in area
        12's OFC config (0.80), because area 47's semantic value is
        less directly affective than area 12's visceral value. The
        semantic-value path runs through NAcc and VMPFC, not
        primarily through amygdala.
      - `to_temporal` is high in BOTH blocks (0.70 in OFC, 0.80 in
        VLPFC), which reflects that area 47 is fundamentally a
        semantic-coupling area: even its value-evaluation role is
        about evaluating the value of *semantic* content, which means
        reading from the semantic network (temporal).
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) each block's anchor features match
        the consuming sub-region's role; (b) the mutual coupling
        priors are strong in both directions; (c) structural features
        (e.g. semantic_retrieval, semantic_selection, value-
        integration-adjacent features) will be equal across
        hemispheres when mirrored; (d) the content-driven features
        (verbal vs scene) mirror directionally.

MIRROR PATTERN
--------------
Area 47's config is a directional mirror applied per-block. The
partition of structural vs directional keys, block by block:

    OFC BLOCK:
    left's area 47 OFC            right's area 47 OFC
    semantic_value_evaluation 0.80
                                  semantic_value_evaluation 0.75
    value_guided_retrieval    0.75
                                  value_guided_retrieval    0.75  (equal)
    semantic_outcome_prediction 0.70
                                  semantic_outcome_prediction 0.70 (equal)
    verbal_semantic_value     0.75
                                  verbal_semantic_value     0.35
    scene_semantic_value      0.40
                                  scene_semantic_value      0.75
    to_nucleus_accumbens      0.70
                                  to_nucleus_accumbens      0.65
    to_amygdala               0.55
                                  to_amygdala               0.65
    to_vmpfc                  0.70
                                  to_vmpfc                  0.70  (equal)
    to_temporal               0.70
                                  to_temporal               0.60
    to_ventrolateral_prefrontal_cortex 0.75
                                  to_ventrolateral_prefrontal_cortex 0.75 (equal)
    to_basal_ganglia          0.60
                                  to_basal_ganglia          0.60  (equal)
    to_commissures            0.45
                                  to_commissures            0.55

    VLPFC BLOCK:
    left's area 47 VLPFC          right's area 47 VLPFC
    semantic_retrieval        0.80
                                  semantic_retrieval        0.75
    controlled_semantic_retrieval 0.80
                                  controlled_semantic_retrieval 0.75
    semantic_selection        0.75
                                  semantic_selection        0.75  (equal)
    verbal_fluency            0.75
                                  verbal_fluency            0.40
    scene_semantic_control    0.40
                                  scene_semantic_control    0.70
    language_comprehension_interface 0.70
                                  language_comprehension_interface 0.45
    to_temporal               0.80
                                  to_temporal               0.65
    to_middle_temporal_gyrus  0.75
                                  to_middle_temporal_gyrus  0.65
    to_angular_gyrus          0.65
                                  to_angular_gyrus          0.55
    to_arcuate_fasciculus     0.65
                                  to_arcuate_fasciculus     0.40
    to_broca_area_45          0.70
                                  to_broca_area_45          0.45
    to_orbitofrontal_cortex   0.75
                                  to_orbitofrontal_cortex   0.75  (equal)
    to_basal_ganglia          0.65
                                  to_basal_ganglia          0.65  (equal)
    to_commissures            0.50
                                  to_commissures            0.50  (equal)

    The mirror test must check direction or equality per key, per
    block, with no cross-block relations checked (there are none —
    the blocks are independent configs).

    Cross-area comparisons to note:
    - OFC block vs area 11 / area 12: semantic_value_evaluation is
      unique to area 47's OFC block (areas 11 and 12 don't have it),
      because area 47's OFC contribution is specifically about
      semantic value, not general stimulus-outcome value.
    - VLPFC block vs area 44 / area 45: controlled_semantic_retrieval
      is unique to area 47's VLPFC block, because areas 44 and 45
      do phonological/lexical processing but not value-driven
      semantic retrieval.

PREDICTION (TESTABLE)
---------------------
Area 47's bridge role supports a specific clinical prediction that
neither OFC-only nor VLPFC-only lesions should produce:

    area 47 lesion (either side):  impaired VALUE-GUIDED semantic
                                   retrieval — the patient can still
                                   retrieve semantic content (VLPFC
                                   intact), can still evaluate
                                   stimulus-outcome value (OFC
                                   intact), but cannot use value
                                   to guide WHICH semantic content
                                   is retrieved. Symptom: intact
                                   semantic knowledge, intact
                                   reward/punishment learning,
                                   but flat verbal fluency that
                                   doesn't respond to reward
                                   manipulations.

    OFC-only lesion:               impaired value evaluation (e.g.
                                   reversal learning), with
                                   intact value-GUIDED semantic
                                   retrieval (the selection
                                   machinery is fine, it just has
                                   less value to work with).

    VLPFC-only lesion:             impaired semantic retrieval/
                                   selection (e.g. verb generation,
                                   semantic fluency), with intact
                                   value evaluation (the value
                                   signal is there, but there's
                                   less content to select from).

The dissociation is what makes area 47's bridge role testable — none
of the three lesions produces the same symptom pattern, because each
breaks a different segment of the value-guided-retrieval pipeline.

EXPORTS
-------
    from .brodmann_area_47 import BRODMANN_47     # int, == AREA_ID
    from .brodmann_area_47 import ANATOMY
    from .brodmann_area_47 import LEFT_CONFIG
    from .brodmann_area_47 import SYSTEM          # list, ["prefrontal_cortex"]
    from .brodmann_area_47 import SUB_REGION      # None (multi-sub-
                                                 # region; per-block
                                                 # keys carry the
                                                 # disambiguation)
    from .brodmann_area_47 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_47`) — area 47 is a direct
child of brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful
      object. The compute is in OFC and VLPFC, not here.
    - Must not import `prefrontal_cortex/`,
      `orbitofrontal_cortex/`, or `ventrolateral_prefrontal_cortex/`
      (cycle; the compute imports from here, not the other way round).
    - Must not merge the two blocks into a single flat config. The
      two blocks are consumed by two different compute sub-regions,
      and merging them would force each sub-region to see the
      other's weights — exactly the cross-sub-region information
      leak the block structure prevents.
    - Must not add `sub_region` fields inside the two blocks. The
      block KEYS are the identifiers, per the schema refinement
      documented above. Adding `sub_region` fields would be
      redundant and would obscure the rule that block key uniquely
      identifies the consumer.
    - Must not introduce a sum-to-1 invariant across the two blocks.
      There is no such pair; the blocks are independently normalised.
    - Must not add a `dlpfc_weight`-style share to area 47. Area 47
      doesn't participate in DLPFC; the `dlpfc_weight` field is a
      DLPFC-internal share (between areas 9 and 46), not a
      prefrontal-wide share.
    - Must not import or reference the left hemisphere's area-47
      package (this file is the left one). Cross-midline semantic
      exchange goes through `telencephalon/commissures/`, never
      through direct registry access. The value-content pair
      (verbal on the left, scene on the right) is a canonical case:
      a verbal-fluency task may need scene-semantic content from the
      right, and vice versa.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's
      area-47 package — same AREA_ID, SYSTEM, SUB_REGION (None),
      GROUPING (None), ANATOMY, same block keys
      ("orbitofrontal_cortex", "ventrolateral_prefrontal_cortex"),
      same feature/connectivity key names inside each block. Only
      the values differ, and only by the per-block directional
      mirror.

PENDING AMENDMENTS TO OTHER AREAS (flagged, not applied)
--------------------------------------------------------
Two schema amendments are now on record across the frontal registry,
both documented here for the record but not applied to keep the
current files stable:

    1. Area 9: add `dlpfc_weight: 0.55` to LEFT_CONFIG and
       RIGHT_CONFIG. Documented in both area-46 files' SCHEMA
       ADDITION sections. Required for the DLPFC pair to be
       complete under the share-weight pattern.

    2. Area 8: optionally rename its `prefrontal_cortex` block to
       `dorsomedial_prefrontal_cortex` and remove the now-redundant
       `sub_region` field inside. This would make the schema uniform
       across all multi-sub-region entries. NOT required — area 8's
       current arrangement works — but documented here so that a
       future normalisation pass has a target state.

Neither amendment is applied here; both are documented so that
anyone reading the registry end-to-end can see the intended final
state, even if the current state has diverged for stability.
"""