"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_47
=======================================================================================================================

Brodmann area 47 — right hemisphere.

Mirror of the left area-47 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 47, says
which compute sub-regions own it, and supplies the per-area weights that
the owning sub-regions' `encode()` methods read. It defines no classes and
no functions; the public surface is the exports listed under "EXPORTS".

If you are looking for the computation area 47 participates in, it lives
in TWO compute sub-regions of the same prefrontal family:
    `.../frontal/cortex/prefrontal_cortex/orbitofrontal_cortex/`
        (areas 11, 12, AND the OFC portion of 47)
    `.../frontal/cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/`
        (areas 44, 45, AND the VLPFC portion of 47)
Area 47 is the ONLY frontal area that contributes to two sub-regions of
the same family. On the right, its value-guided retrieval is expressed
through scene/object-semantic content rather than verbal content, as
documented below.

WHAT AREA 47 IS (functionally)
------------------------------
Area 47 is the orbital part of the inferior frontal gyrus and the bridge
between the orbitofrontal and ventrolateral prefrontal sub-regions. Its
specific contribution is **value-guided semantic retrieval**: using
reward/outcome value to guide which semantic content gets retrieved and
selected. The OFC portion of 47 evaluates the value of semantic
candidates; the VLPFC portion performs the retrieval and selection based
on that value.

On the RIGHT, the content of value-guided retrieval is more
scene/semantic and less language-specific: which object associations are
worth retrieving, which scene interpretation fits best, which
spatial-situational meaning is worth selecting. The right's area 47 is
more engaged in non-verbal semantic control — the retrieval and
selection of *situational* meaning rather than *word* meaning. It still
performs value-guided retrieval (the mechanism is the same on both
sides), but the content is scene/situational rather than verbal. The
left/right split is directional, not complementary — the right's area
47 is scene-semantic-forward, not 'the left's at reduced weight'.

THE SCHEMA SHAPE — multi-sub-region-within-one-family
-----------------------------------------------------
Areas 6, 8, and 47 are all multi-system entries in three different
shapes. On the right, the shapes are the same as on the left — the
schema does not lateralise, only the config values do:

    area 6    TWO LEAF SYSTEMS. Blocks keyed by system name, no
              `sub_region` field inside.

    area 8    ONE LEAF + ONE FAMILY. Blocks keyed by system name; the
              family block carries a `sub_region` field inside.

    area 47   ONE FAMILY, TWO SUB-REGIONS. Block keys are the
              SUB-REGION names themselves ("orbitofrontal_cortex",
              "ventrolateral_prefrontal_cortex"), and NO `sub_region`
              field is used inside them (the key IS the identifier).

The underlying rule, restated for the right hemisphere because it is the
schema that this file exercises: block key MUST uniquely identify the
consuming sub-region. When the consumer is a leaf system, its name is
unique. When the consumer is a single sub-region of a family, the
family name plus `sub_region` field disambiguates. When two or more
sub-regions of the same family are involved, the sub-region names must
be used directly as keys. This is the same rule on both hemispheres.

PENDING SCHEMA AMENDMENT (optional): area 8's `prefrontal_cortex` block
could be renamed to `dorsomedial_prefrontal_cortex` to match the
"sub-region name as key" convention, with the `sub_region` field
removed (redundant). Not required; documented in the left area-47
docstring and repeated here for the right side so that a future
normalisation pass on the right frontal registry has the same target
state.

IDENTITY
--------
    AREA_ID    = 47
    NAME       = "Brodmann area 47"
    SYSTEM     = ["prefrontal_cortex"]
    SUB_REGION = None         # multi-sub-region — see per-block keys
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # not part of Broca's area

Note on SUB_REGION being None with a non-trivial config: as with areas
6 and 8, the package-level SUB_REGION is None because the area spans
more than one sub-region. Here the two sub-regions are both from
prefrontal_cortex, and their disambiguation is carried by the block
KEYS.

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
            "gets retrieved and selected. On the RIGHT, value-guided "
            "retrieval is more scene/semantic and less language-"
            "specific than on the left: which object associations "
            "are worth retrieving, which scene interpretation fits "
            "best, which spatial-situational meaning is worth "
            "selecting. The right's area 47 still performs "
            "value-guided retrieval (the mechanism is the same on "
            "both sides), but the content is scene/situational rather "
            "than verbal. The left/right split is directional, not "
            "complementary — the right's area 47 is scene-semantic-"
            "forward, not 'the left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 47's RIGHT_CONFIG has two per-sub-region blocks, keyed by the
sub-region names themselves (no `sub_region` field inside).

    RIGHT_CONFIG = {

        # ============================================================
        # FIRST BLOCK — orbitofrontal_cortex
        # (the value side of value-guided semantic retrieval)
        # ============================================================
        # Area 47's OFC block contributes to the OFC compute
        # sub-region alongside areas 11 and 12. Its specific
        # contribution is the value of SEMANTIC candidates. On the
        # right, the semantic content whose value is being evaluated
        # is more scene/situational than verbal.
        "orbitofrontal_cortex": {
            # ---- feature emphases ----
            # RIGHT bias: scene/semantic content is the thing whose
            # value is being evaluated; verbal-semantic value is
            # present but secondary.
            "semantic_value_evaluation":  0.75,  # DOWN mildly from
                                                 # left's 0.80;
                                                 # still the anchor
            "value_guided_retrieval":     0.75,  # structural (equal)
            "semantic_outcome_prediction":0.70,  # structural (equal)
            "verbal_semantic_value":      0.35,  # DOWN from left's
                                                 # 0.75
            "scene_semantic_value":       0.75,  # UP from left's
                                                 # 0.40; the right's
                                                 # anchor

            # ---- connectivity priors ----
            "to_nucleus_accumbens":       0.65,  # DOWN mildly from
                                                 # left's 0.70;
                                                 # positive-reward
                                                 # weighting is
                                                 # more left-
                                                 # lateralised
            "to_amygdala":                0.65,  # UP from left's
                                                 # 0.55; scene/
                                                 # situational value
                                                 # is more affect-
                                                 # anchored on the
                                                 # right
            "to_vmpfc":                   0.70,  # structural (equal)
            "to_temporal":                0.60,  # DOWN from left's
                                                 # 0.70; less
                                                 # verbal-semantic
                                                 # content source
            "to_ventrolateral_prefrontal_cortex": 0.75,
                                                 # structural (equal);
                                                 # the bridge to
                                                 # area 47's VLPFC
                                                 # block
            "to_basal_ganglia":           0.60,  # structural (equal)
            "to_commissures":             0.55,  # UP from left's
                                                 # 0.45; scene-
                                                 # semantic value
                                                 # has to reach the
                                                 # left's verbal
                                                 # labelling for
                                                 # narrative
                                                 # expression
        },

        # ============================================================
        # SECOND BLOCK — ventrolateral_prefrontal_cortex
        # (the retrieval/selection side of value-guided semantic
        # retrieval)
        # ============================================================
        # Area 47's VLPFC block contributes to the VLPFC compute
        # sub-region alongside areas 44 and 45. Its specific
        # contribution is CONTROLLED semantic retrieval, driven by
        # value. On the right, the content is scene/situational
        # rather than verbal, so the semantic-network coupling is
        # less strongly language-tuned.
        "ventrolateral_prefrontal_cortex": {
            # ---- feature emphases ----
            # RIGHT bias: scene/object-semantic retrieval and
            # control are the anchors; verbal fluency is present but
            # much reduced.
            "semantic_retrieval":         0.75,  # DOWN mildly from
                                                 # left's 0.80;
                                                 # still the anchor
                                                 # mechanism
            "controlled_semantic_retrieval": 0.75,
                                                 # DOWN mildly from
                                                 # left's 0.80;
                                                 # still the anchor
                                                 # mechanism
            "semantic_selection":         0.75,  # structural (equal)
            "verbal_fluency":             0.40,  # DOWN from left's
                                                 # 0.75; verbal
                                                 # fluency is a
                                                 # left-lateralised
                                                 # signature
            "scene_semantic_control":     0.70,  # UP from left's
                                                 # 0.40; the right's
                                                 # anchor — control
                                                 # of scene/object-
                                                 # semantic
                                                 # retrieval
            "language_comprehension_interface": 0.45,
                                                 # DOWN from left's
                                                 # 0.70; the right's
                                                 # VLPFC semantic
                                                 # control is less
                                                 # language-bound

            # ---- connectivity priors ----
            "to_temporal":                0.65,  # DOWN from left's
                                                 # 0.80; still
                                                 # strong — the
                                                 # semantic network
                                                 # is the content
                                                 # source — but less
                                                 # language-tuned
            "to_middle_temporal_gyrus":   0.65,  # DOWN from left's
                                                 # 0.75
            "to_angular_gyrus":           0.55,  # DOWN from left's
                                                 # 0.65
            "to_arcuate_fasciculus":      0.40,  # DOWN from left's
                                                 # 0.65; the dorsal
                                                 # language pathway
                                                 # is not the right's
                                                 # VLPFC semantic
                                                 # control's primary
                                                 # input
            "to_broca_area_45":           0.45,  # DOWN from left's
                                                 # 0.70; lexical-
                                                 # selection
                                                 # coupling is
                                                 # left-dominant
            "to_orbitofrontal_cortex":    0.75,  # structural (equal);
                                                 # the bridge back to
                                                 # area 47's OFC block
            "to_basal_ganglia":           0.65,  # structural (equal)
            "to_commissures":             0.50,  # structural (equal);
                                                 # the semantic
                                                 # exchange need is
                                                 # symmetric (a
                                                 # scene-semantic
                                                 # task needing
                                                 # verbal labels is
                                                 # as common as a
                                                 # verbal-semantic
                                                 # task needing
                                                 # scene content)
        },
    }

    Notes on the weights:
      - The two blocks are INDEPENDENT configs consumed by different
        compute sub-regions. The OFC sub-region reads only
        `RIGHT_CONFIG["orbitofrontal_cortex"]`; the VLPFC sub-region
        reads only `RIGHT_CONFIG["ventrolateral_prefrontal_cortex"]`.
      - The two blocks are COUPLED through the mutual
        `to_ventrolateral_prefrontal_cortex` / `to_orbitofrontal_cortex`
        priors (0.75 each, both structural — identical to the left's).
        This is the value-to-selection handoff that makes area 47 a
        bridge rather than two unrelated contributions, and it is the
        same bridge on both hemispheres. Only its *content* changes.
      - There is NO sum-to-1 invariant across the two blocks. They are
        consumed independently.
      - The left's verbal anchors (verbal_semantic_value 0.75,
        verbal_fluency 0.75) are the right's non-anchors (0.35, 0.40);
        the left's non-anchors (scene_semantic_value 0.40,
        scene_semantic_control 0.40) are the right's anchors (0.75,
        0.70). The anchor pair swaps sides cleanly.
      - The VLPFC block's semantic-network priors (to_temporal,
        to_middle_temporal_gyrus, to_angular_gyrus, to_arcuate_fasciculus,
        to_broca_area_45) all drop on the right. The semantic network
        on the right is still the content source (0.65, 0.65, 0.55
        are not low), but it is less strongly language-tuned — the
        right reads scene/object semantics from temporal rather than
        word semantics, so the dorsal-language-pathway coupling
        (arcuate, broca 45) drops most sharply.
      - `to_commissures` is asymmetric between blocks on the right:
        0.55 in the OFC block (up from the left's 0.45) vs 0.50 in
        the VLPFC block (equal to the left's 0.50). The OFC-block
        asymmetry follows the familiar pattern — the right's
        scene-semantic value has to reach the left's verbal labelling
        for narrative expression. The VLPFC-block symmetry is
        different, and deliberate: at the level of retrieval/selection
        *control*, the exchange need is genuinely two-way (a
        scene-semantic task needing verbal labels is as common as a
        verbal-semantic task needing scene content). The two blocks
        therefore have different commissural asymmetries for
        different reasons, and the mirror test must check each
        separately.
      - All values are plausible priors, not measured constants. The
        key constraints are: (a) each block's anchor features match
        the consuming sub-region's role; (b) the mutual coupling
        priors are structural (0.75 on both sides, both blocks);
        (c) mechanism features (semantic_retrieval,
        semantic_selection, value_guided_retrieval,
        semantic_outcome_prediction) are structural; (d) content
        features (verbal vs scene) mirror directionally; (e) the
        language-network priors (temporal, MTG, angular, arcuate,
        Broca 45) drop on the right.

MIRROR PATTERN
--------------
Area 47's config is a directional mirror applied per-block:

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

    Structural keys (equal across hemispheres) in the OFC block:
    value_guided_retrieval, semantic_outcome_prediction,
    to_vmpfc, to_ventrolateral_prefrontal_cortex, to_basal_ganglia.
    Structural keys in the VLPFC block: semantic_selection,
    to_orbitofrontal_cortex, to_basal_ganglia, to_commissures.

    Directional keys (mirror) in the OFC block:
    semantic_value_evaluation (L>R mildly), verbal_semantic_value
    (L>R), scene_semantic_value (R>L), to_nucleus_accumbens (L>R
    mildly), to_amygdala (R>L), to_temporal (L>R),
    to_commissures (R>L). Directional keys in the VLPFC block:
    semantic_retrieval (L>R mildly), controlled_semantic_retrieval
    (L>R mildly), verbal_fluency (L>R), scene_semantic_control
    (R>L), language_comprehension_interface (L>R), to_temporal
    (L>R), to_middle_temporal_gyrus (L>R), to_angular_gyrus (L>R),
    to_arcuate_fasciculus (L>R), to_broca_area_45 (L>R).

    Cross-area comparisons to note (same as left, evaluated from the
    right side): semantic_value_evaluation is unique to area 47's
    OFC block (not present in areas 11, 12); controlled_semantic_
    retrieval is unique to area 47's VLPFC block (not present in
    areas 44, 45).

    Commissural asymmetry to note (unique to area 47): the OFC
    block's to_commissures (0.55) is UP from the left's (0.45);
    the VLPFC block's to_commissures (0.50) is EQUAL to the left's
    (0.50). The two blocks have different commissural asymmetries
    for different reasons — the mirror test must check them
    separately, not as a single area-47-level value.

PREDICTION (TESTABLE)
---------------------
Area 47's bridge role supports the same three-way clinical
dissociation documented on the left, with the right-side content:

    area 47 lesion, right:  impaired VALUE-GUIDED scene/semantic
                            retrieval — the patient can still
                            retrieve scene/object semantic content
                            (VLPFC intact), can still evaluate
                            stimulus-outcome value (OFC intact),
                            but cannot use value to guide WHICH
                            scene/semantic content is retrieved.
                            Symptom: intact scene recognition,
                            intact reward learning, but flat
                            scene-semantic fluency that doesn't
                            respond to reward manipulations.

    OFC-only lesion, right:  impaired value evaluation with intact
                             value-guided retrieval; the selection
                             machinery has less value to work
                             with.

    VLPFC-only lesion, right: impaired scene/semantic retrieval
                              with intact value evaluation; the
                              value signal has less scene content
                              to select from.

Compared with the left-side profiles, the right-side ones are the
scene-semantic counterpart of the left's verbal-semantic ones. The
combined 3×2 structure (three lesion types × two hemispheres) gives
six distinguishable profiles for the area-47 bridge, none of which
overlap with the OFC-only or VLPFC-only profiles.

EXPORTS
-------
    from .brodmann_area_47 import BRODMANN_47     # int, == AREA_ID
    from .brodmann_area_47 import ANATOMY
    from .brodmann_area_47 import RIGHT_CONFIG
    from .brodmann_area_47 import SYSTEM          # list, ["prefrontal_cortex"]
    from .brodmann_area_47 import SUB_REGION      # None (multi-sub-
                                                 # region; per-block
                                                 # keys carry the
                                                 # disambiguation)
    from .brodmann_area_47 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_47`) — area 47 is a direct child
of brodmann_areas/, not nested.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in OFC and VLPFC, not here.
    - Must not import `prefrontal_cortex/`,
      `orbitofrontal_cortex/`, or `ventrolateral_prefrontal_cortex/`
      (cycle; the compute imports from here, not the other way round).
    - Must not merge the two blocks into a single flat config. The
      two blocks are consumed by two different compute sub-regions,
      and merging them would force each sub-region to see the
      other's weights.
    - Must not add `sub_region` fields inside the two blocks. The
      block KEYS are the identifiers.
    - Must not introduce a sum-to-1 invariant across the two blocks.
    - Must not add a `dlpfc_weight`-style share to area 47. Area 47
      doesn't participate in DLPFC.
    - Must not import or reference the left hemisphere's area-47
      package. Cross-midline semantic exchange goes through
      `telencephalon/commissures/`, never through direct registry
      access. The content pair (verbal on the left, scene on the
      right) is a canonical case: a scene-semantic task may need
      verbal content from the left, and vice versa.
    - Must not conflate the two blocks' commissural asymmetries.
      The OFC block's to_commissures goes UP on the right (0.45→0.55);
      the VLPFC block's stays EQUAL (0.50→0.50). A single area-47-
      level to_commissures value would be a bug — the asymmetry is
      per-block, for the two different reasons documented in the
      notes.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's
      area-47 package — same AREA_ID, SYSTEM, SUB_REGION (None),
      GROUPING (None), ANATOMY, same block keys
      ("orbitofrontal_cortex", "ventrolateral_prefrontal_cortex"),
      same feature/connectivity key names inside each block. Only
      the values differ, and only by the per-block directional
      mirror.

PENDING AMENDMENTS TO OTHER AREAS (flagged, not applied)
--------------------------------------------------------
Same two schema amendments on record from the left area-47 file,
restated for the right side so that the right registry's outstanding
items are also documented at the natural stopping point:

    1. Area 9: add `dlpfc_weight: 0.55` to LEFT_CONFIG and
       RIGHT_CONFIG. Documented in both area-46 files' SCHEMA
       ADDITION sections. Required for the DLPFC pair to be
       complete under the share-weight pattern.

    2. Area 8: optionally rename its `prefrontal_cortex` block to
       `dorsomedial_prefrontal_cortex` and remove the now-redundant
       `sub_region` field inside. Optional, cosmetic.

Neither amendment is applied here; both are documented so that a
future normalisation pass on the right frontal registry has the
same target state as the left's.

FRONTAL REGISTRY STATUS (both hemispheres)
------------------------------------------
With this file, the entire frontal registry is now on record on both
hemispheres:

    brodmann_areas/__init__.py                      L ✅  R ✅
    brocas_area/{__init__,44,45}                    L ✅  R ✅
    brodmann_area_4                                 L ✅  R ✅
    brodmann_area_6                                 L ✅  R ✅
    brodmann_area_8                                 L ✅  R ✅
    brodmann_area_9                                 L ✅  R ✅
    brodmann_area_10                                L ✅  R ✅
    brodmann_area_11                                L ✅  R ✅
    brodmann_area_12                                L ✅  R ✅
    brodmann_area_25 (cross-lobe pointer)           L ✅  R ✅
    brodmann_area_33 (tree artifact)                L ✅  R ✅
    brodmann_area_46                                L ✅  R ✅
    brodmann_area_47                                L ✅  R ✅

Two amendments are outstanding (area 9's `dlpfc_weight` on both sides;
area 8's optional block rename on both sides). Everything else in
the frontal registry is complete.
"""