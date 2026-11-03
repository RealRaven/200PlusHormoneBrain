"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_4
=====================================================================================================================

Brodmann area 4 (primary motor cortex) — right hemisphere.

Mirror of the left area-4 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 4, says
which compute sub-region owns it, and supplies the per-area weights that
the owning sub-region's `encode()` reads. It defines no classes and no
functions; the public surface is the exports listed under "EXPORTS".

If you are looking for the computation area 4 participates in, it lives in
`.../frontal/cortex/primary_motor_cortex/` — area 4 is the primary motor
cortex, and it is the final cortical stage of voluntary movement output.
This package is the *label*; the compute sub-region is the *agent*. Area
4's owning system IS the leaf sub-region: the primary motor cortex compute
package consumes area 4's config directly, with no intermediate family
layer.

IDENTITY
--------
    AREA_ID    = 4
    NAME       = "Brodmann area 4 (primary motor cortex)"
    SYSTEM     = ["primary_motor_cortex"]
    SUB_REGION = None         # SYSTEM already names the leaf sub-region
    LOBE       = "frontal"
    SIDE       = "right"
    GROUPING   = None         # no named sub-grouping; see left area-4 docstring

The SUB_REGION and GROUPING fields are None for the same reasons as on
the left: SUB_REGION exists to disambiguate within a *family* system (like
prefrontal_cortex), and primary_motor_cortex is already a leaf; GROUPING
exists to name a *named sub-grouping* within a sub-region, and primary
motor cortex is one continuous somatotopic map with no such sub-grouping.
Both fields are identical across hemispheres — anatomy and structure do
not lateralise, only weights do.

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
            "corticospinal and corticobulbar tracts. Its somatotopic "
            "organization — the motor homunculus — is the same on both "
            "hemispheres: face ventrolateral, hand mid-convexity, leg "
            "medial. On the RIGHT, area 4's representation is weighted "
            "toward proximal limb, trunk, and postural control, and "
            "toward the facial-expression part of the face/mouth "
            "representation (emotional expression, not speech "
            "articulation). The speech-articulator component of the "
            "face/mouth representation is present but is not the "
            "right's dominant driver; on the right, the face/mouth "
            "region is more strongly recruited for emotional and "
            "affective facial movement than for propositional speech. "
            "The left/right split is directional, not complementary — "
            "the right's area 4 is proximal/postural-forward, not 'the "
            "left's at reduced weight'."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
Area 4's config has two parts: (a) its feature emphases within the
primary motor cortex sub-region's computation, and (b) its connectivity
priors to partner structures. There is no per-area share weight (unlike
Broca's area's `brocas_weight`) because area 4 is the sole Brodmann area
within its owning system.

    RIGHT_CONFIG = {
        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: proximal_power (arm/shoulder/trunk) and
        # corticobulbar_expression (facial expression) are the anchor
        # features — the right's primary motor role is gross, proximal,
        # postural, and expression-related movement. distal_precision
        # and corticobulbar_speech are present but much reduced, because
        # fine distal control and speech articulation are
        # left-lateralised.
        "distal_precision":        0.40,   # fine hand/finger/wrist
        "proximal_power":          0.80,   # arm/shoulder/trunk
        "corticobulbar_speech":    0.30,   # lips, tongue, jaw, larynx
        "corticobulbar_expression":0.65,   # facial expression (smile,
                                           # eyebrow, etc.) — the right's
                                           # anchor face/mouth function
        "force_gain":              0.70,   # multiplicative gain on
                                           # output force; higher on the
                                           # right because proximal
                                           # movements need more force
                                           # scaling
        "velocity_gain":           0.65,   # multiplicative gain on
                                           # output velocity/smoothness;
                                           # higher on the right for
                                           # whole-body movement
                                           # smoothness

        # ---- connectivity priors to partner structures ----
        "to_premotor_cortex":      0.85,   # the strongest input to
                                           # area 4 (same as left);
                                           # premotor plans what area 4
                                           # will execute
        "to_supplementary_motor":  0.60,   # SMA sequences complex
                                           # movements; slightly higher
                                           # on the right because
                                           # bimanual and whole-body
                                           # sequences are right-
                                           # lateralised
        "to_basal_ganglia":        0.70,   # the basal ganglia gate
                                           # which motor programs area
                                           # 4 receives (same as left)
        "to_cerebellum":           0.65,   # cerebellar modulation of
                                           # timing and error-correction
                                           # (same as left)
        "to_primary_somatosensory":0.70,   # sensory feedback from the
                                           # moving body part; the
                                           # sensorimotor loop is tight
                                           # (same as left)
        "to_corticospinal_tract":  0.80,   # the output pathway for
                                           # body/lower-limb movements;
                                           # higher on the right than
                                           # on the left because the
                                           # right's dominant motor
                                           # output is limb/postural,
                                           # not speech
        "to_corticobulbar_tract":  0.35,   # the output pathway for
                                           # cranial nerve targets;
                                           # lower on the right than
                                           # on the left because speech
                                           # articulator control is
                                           # left-dominant. The right's
                                           # corticobulbar output is
                                           # primarily facial expression,
                                           # not speech
        "to_commissures":          0.45,   # cross-midline motor
                                           # coordination; higher on
                                           # the right than on the left
                                           # because the right's gross/
                                           # postural output is what
                                           # bimanual coordination
                                           # needs to reach the left's
                                           # fine/distal output
    }

    Notes on the weights:
      - Feature weights are multipliers on features extracted by the
        primary_motor_cortex sub-region. The right's `proximal_power`
        (0.80) and `corticobulbar_expression` (0.65) are the two anchor
        features — the right's primary motor role is gross, proximal,
        postural, and expression-related movement.
      - `distal_precision` vs `proximal_power` is the fine-vs-gross
        lateralisation: left-weighted toward fine, right-weighted
        toward gross. They are directional, not complementary. On the
        right, `proximal_power` (0.80) is the highest feature weight;
        on the left, `distal_precision` (0.85) was.
      - `corticobulbar_speech` vs `corticobulbar_expression` flips: on
        the left, speech (0.80) dominated expression (0.35); on the
        right, expression (0.65) dominates speech (0.30). The mechanism
        is the same tract with different targets, and the flip is the
        right hemisphere's signature for that tract.
      - Connectivity priors flip directionally:
          * `to_corticospinal_tract` goes UP on the right (0.70 → 0.80)
            — the right's dominant motor output is limb/postural;
          * `to_corticobulbar_tract` goes DOWN on the right (0.75 →
            0.35) — speech articulator control is left-dominant;
          * `to_commissures` goes UP on the right (0.30 → 0.45) — the
            right's gross/postural output is what bimanual coordination
            needs to deliver to the left's fine/distal output;
          * `to_supplementary_motor` goes UP mildly (0.55 → 0.60) —
            bimanual and whole-body sequences are more right-lateralised.
      - The `to_premotor_cortex: 0.85` prior is identical across
        hemispheres — premotor → primary motor is the strongest input
        path on both sides, and it is structural (anatomy does not
        lateralise).
      - All values are plausible priors, not measured constants. The
        key constraints are the left/right directional mirror.

MIRROR PATTERN
--------------
This area's config is a directional mirror, not a complementary one —
the same pattern as Broca's areas 44 and 45, and the same pattern as the
left area-4's mirror description:

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

The relationship is directional. The structural priors (`to_premotor_
cortex`, `to_basal_ganglia`, `to_cerebellum`, `to_primary_somatosensory`)
are IDENTICAL across hemispheres — they encode anatomical connectivity,
not lateralised function. The mirror test must check direction on the
configurable keys and equality on the structural keys.

EXPORTS
-------
    from .brodmann_area_4 import BRODMANN_4      # int, == AREA_ID
    from .brodmann_area_4 import ANATOMY
    from .brodmann_area_4 import RIGHT_CONFIG
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
    - Must not import or reference the left hemisphere's area-4 package.
      Cross-midline motor coordination goes through
      `telencephalon/commissures/`, never through direct registry access.
      The classic case is bimanual fine/gross coordination: the right's
      area 4 sends the gross/positional component of a bimanual movement
      across the commissures to be combined with the left's fine/distal
      component. Direct registry access would silently merge the two
      components without the commissural delay and bandwidth that the
      model is supposed to exercise.
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the left hemisphere's area-4
      package — same AREA_ID, SYSTEM, SUB_REGION (None), GROUPING
      (None), ANATOMY, same config keys. Only the values differ, and
      only by the directional mirror described above.
"""