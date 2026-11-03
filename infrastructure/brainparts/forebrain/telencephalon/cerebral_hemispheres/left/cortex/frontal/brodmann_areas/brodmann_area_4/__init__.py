"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_4
====================================================================================================================

Brodmann area 4 (primary motor cortex) — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares
the canonical identity of area 4, says which compute sub-region owns it,
and supplies the per-area weights that the owning sub-region's `encode()`
reads. It defines no classes and no functions; the public surface is the
exports listed under "EXPORTS".

If you are looking for the computation area 4 participates in, it lives in
`.../frontal/cortex/primary_motor_cortex/` — area 4 is the primary motor
cortex, and it is the final cortical stage of voluntary movement output.
This package is the *label*; the compute sub-region is the *agent*. Unlike
Broca's area (which was a label on a sub-region of a five-part family),
area 4's owning system IS the leaf sub-region: the primary motor cortex
compute package consumes area 4's config directly, with no intermediate
family layer.

IDENTITY
--------
    AREA_ID    = 4
    NAME       = "Brodmann area 4 (primary motor cortex)"
    SYSTEM     = ["primary_motor_cortex"]
    SUB_REGION = None         # see note below
    LOBE       = "frontal"
    SIDE       = "left"
    GROUPING   = None         # no named sub-grouping; see note below

Note on SUB_REGION being None: this field exists to disambiguate within a
*family* system (like prefrontal_cortex, which has five sub-regions). When
SYSTEM already names a leaf sub-region — primary_motor_cortex,
premotor_cortex, supplementary_motor_cortex — SUB_REGION adds nothing and
is set to None. Area 4 is the first frontal registry entry with this
shape; areas 6 and 8 will follow (SYSTEM names the leaf sub-regions
directly), and area 47 will be the mirror case (prefrontal, so SUB_REGION
is set).

Note on GROUPING being None: this field names the *named sub-grouping*
within a sub-region (e.g. brocas_area within VLPFC). Primary motor cortex
has no such named sub-grouping — it is one continuous somatotopic map, not
a collection of named sub-units. GROUPING is None for area 4 and for the
large majority of frontal areas; brodmann_area_44 and brodmann_area_45
are the only current entries with a non-None value.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 4 (primary motor cortex)",
        "system": "primary_motor_cortex",
        "sub_region": None,
        "grouping": None,
        "location": "precentral gyrus, immediately anterior to the "
                    "central sulcus; the face/mouth representation lies "
                    "ventrolateral (adjacent to the lateral sulcus), "
                    "the hand/arm representation mid-convexity, and "
                    "the leg/trunk representation medial (on the "
                    "paracentral lobule and into the longitudinal "
                    "fissure)",
        "cytoarchitecture": "agranular cortex — no prominent layer IV. "
                            "The defining feature is the giant Betz "
                            "cells of layer V, whose axons form a large "
                            "fraction of the corticospinal tract. The "
                            "absence of a granular layer is what makes "
                            "this cortex 'motor' rather than 'sensory' "
                            "in the classical cytoarchitectonic scheme.",
        "notes": (
            "The primary motor cortex and the final cortical stage of "
            "voluntary movement. It is agranular (no layer IV), with "
            "giant Betz cells in layer V that send their axons down the "
            "corticospinal and corticobulbar tracts. Its most famous "
            "property is the somatotopic map — the motor homunculus — "
            "in which the body's parts are laid out along the gyrus "
            "with disproportionate representation of the hand and the "
            "face/mouth. The face/mouth representation is adjacent to "
            "Broca's area (with VLPFC immediately anterior via the "
            "ventral premotor cortex, area 6), which is the anatomical "
            "basis for area 44's direct motor-speech output path to "
            "area 4 — speech articulators are represented in area 4, "
            "and area 44 drives them. On the left, area 4's "
            "representation is weighted toward the hand/finger "
            "representation and the face/mouth (speech) representation; "
            "on the right, it is weighted toward the proximal limb, "
            "trunk, and postural representations. The left/right split "
            "is directional, not complementary — the right's area 4 is "
            "proximal/postural-forward, not 'the left's at reduced "
            "weight'."
        ),
    }

CONFIG (LEFT)
-------------
Area 4's config has two parts: (a) its feature emphases within the
primary motor cortex sub-region's computation, and (b) its connectivity
priors to partner structures. There is no per-area share weight (unlike
Broca's area's `brocas_weight`) because area 4 is the sole Brodmann area
within its owning system — primary_motor_cortex has no other area to
share with.

    LEFT_CONFIG = {
        # ---- feature emphases inside this area's contribution ----
        # LEFT bias: distal_precision (fine hand/finger control) and
        # corticobulbar_speech (speech articulators) are the anchor
        # features — the left's primary motor role is fine, distal,
        # and speech-related movement. Proximal_power and
        # corticobulbar_expression (facial expression) are secondary,
        # because gross limb movement and emotional facial expression
        # are more right-lateralised.
        "distal_precision":        0.85,   # fine hand/finger/wrist
        "proximal_power":          0.40,   # arm/shoulder/trunk
        "corticobulbar_speech":    0.80,   # lips, tongue, jaw, larynx
        "corticobulbar_expression":0.35,   # facial expression (smile,
                                           # eyebrow, etc.)
        "force_gain":              0.55,   # multiplicative gain on
                                           # output force
        "velocity_gain":           0.55,   # multiplicative gain on
                                           # output velocity/smoothness

        # ---- connectivity priors to partner structures ----
        "to_premotor_cortex":      0.85,   # the strongest input to
                                           # area 4; premotor plans
                                           # what area 4 will execute
        "to_supplementary_motor":  0.55,   # SMA sequences complex
                                           # movements that area 4 then
                                           # executes one element at a
                                           # time
        "to_basal_ganglia":        0.70,   # the basal ganglia gate
                                           # which motor programs area
                                           # 4 receives; area 4's output
                                           # also feeds back via the
                                           # cortico-striatal loop
        "to_cerebellum":           0.65,   # cerebellar modulation of
                                           # timing and error-correction
                                           # in the descending motor
                                           # command
        "to_primary_somatosensory":0.70,   # sensory feedback from the
                                           # moving body part; the
                                           # sensorimotor loop is tight
                                           # (area 4 and the primary
                                           # somatosensory cortex are
                                           # adjacent and reciprocally
                                           # connected)
        "to_corticospinal_tract":  0.70,   # the output pathway for
                                           # body/lower-limb movements;
                                           # on the left, somewhat lower
                                           # than on the right because
                                           # the left's dominant motor
                                           # output is speech
                                           # (corticobulbar), not
                                           # limb (corticospinal)
        "to_corticobulbar_tract":  0.75,   # the output pathway for
                                           # cranial nerve targets
                                           # (speech articulators,
                                           # facial muscles); the
                                           # left's highest output
                                           # prior — speech is the
                                           # left's dominant motor
                                           # function
        "to_commissures":          0.30,   # cross-midline motor
                                           # coordination; lower on
                                           # the left than on the right
                                           # because the right's gross/
                                           # postural output is what
                                           # bimanual coordination
                                           # needs to reach the left's
    }

    Notes on the weights:
      - Feature weights are multipliers on features extracted by the
        primary_motor_cortex sub-region. The left's `distal_precision`
        (0.85) and `corticobulbar_speech` (0.80) are the two anchor
        features — the left's primary motor role is fine, distal, and
        speech-related movement.
      - `distal_precision` vs `proximal_power` is the classic
        fine-vs-gross lateralisation: left-weighted toward fine (hand/
        finger), right-weighted toward gross (arm/leg/trunk). They are
        directional, not complementary; a naive "sum to 1" reading is
        wrong.
      - `corticobulbar_speech` vs `corticobulbar_expression` separates
        two motor functions that happen to use the same descending
        pathway: the left's speech articulators (lips, tongue, jaw,
        larynx) are a dominant role, while the right's facial
        expression (smile, eyebrow, etc.) is a dominant role. Same
        tract, different targets — the separation is the point.
      - Connectivity priors parameterise how strongly this area's
        signal reaches partner structures. The highest are
        `to_premotor_cortex` (0.85) and `to_corticobulbar_tract`
        (0.75) — premotor is the input path, corticobulbar is the
        output path for the left's dominant motor function (speech).
      - The `to_corticospinal_tract` (0.70) vs `to_corticobulbar_tract`
        (0.75) asymmetry is the left's signature: corticobulbar is
        higher, because speech articulators are represented in area 4's
        ventral region and are driven by the left's dominant
        language-production stream. On the right the asymmetry inverts
        — corticospinal becomes the higher output prior.
      - All values are plausible priors, not measured constants. The
        key constraints are the left/right directional mirror and the
        left/right functional asymmetry described above.

MIRROR PATTERN
--------------
This area's config is a directional mirror, not a complementary one —
the same pattern as Broca's areas 44 and 45:

    left's area 4               right's area 4
    distal_precision  0.85      distal_precision  0.40
    proximal_power    0.40      proximal_power    0.80
    corticobulbar_speech   0.80 corticobulbar_speech   0.30
    corticobulbar_expression 0.35 corticobulbar_expression 0.65
    force_gain        0.55      force_gain        0.70
    velocity_gain     0.55      velocity_gain     0.65

    to_corticospinal  0.70      to_corticospinal  0.80
    to_corticobulbar  0.75      to_corticobulbar  0.35
    to_commissures    0.30      to_commissures    0.45

The relationship is directional: distal, speech, and corticobulbar go
down on the right; proximal, expression, force, velocity, and
corticospinal go up on the right. The mirror test must check direction,
not complementarity.

EXPORTS
-------
    from .brodmann_area_4 import BRODMANN_4      # int, == AREA_ID
    from .brodmann_area_4 import ANATOMY
    from .brodmann_area_4 import LEFT_CONFIG
    from .brodmann_area_4 import SYSTEM          # list, ["primary_motor_cortex"]
    from .brodmann_area_4 import SUB_REGION      # None
    from .brodmann_area_4 import GROUPING        # None

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_4`) — area 4 is a direct child of
brodmann_areas/, not nested, so there is no nesting to hide.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
      The compute is in primary_motor_cortex/, not here.
    - Must not import `primary_motor_cortex/` (cycle; the compute
      imports from here, not the other way round).
    - Must not import any other Brodmann area. Area 4's relationship to
      area 6 (premotor/SMA feeding it) and to area 44 (Broca's speech
      output driving its face/mouth representation) is expressed via
      connectivity priors and via the compute sub-regions' inter-area
      wiring, not by registry-to-registry imports.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-4
      package — same AREA_ID, SYSTEM, SUB_REGION (None), GROUPING
      (None), ANATOMY, same config keys. Only the values differ, and
      only by the directional mirror described above.
"""