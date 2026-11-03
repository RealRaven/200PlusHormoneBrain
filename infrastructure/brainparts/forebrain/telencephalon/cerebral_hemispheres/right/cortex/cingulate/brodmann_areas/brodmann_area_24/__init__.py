"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.brodmann_areas.brodmann_area_24
==========================================================================================================================

Brodmann area 24 — right hemisphere.

Mirror of the left area-24 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 24, says which
functional sub-module owns it, and supplies the per-area weights that the
owning sub-module's `encode()` reads. It defines no classes and no functions;
the public surface is the four names under "EXPORTS".

If you are looking for the computation area 24 participates in, it is in
`.../cingulate/anterior_cingulate/` — area 24 is the principal conflict-
monitoring area of the ACC's dorsal cognitive division. This package is the
*label*, not the *agent*.

IDENTITY
--------
    AREA_ID   = 24
    NAME      = "Brodmann area 24"
    SYSTEM    = "anterior_cingulate"
    LOBE      = "cingulate"
    SIDE      = "right"

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 24",
        "system": "anterior_cingulate",
        "location": "dorsal anterior cingulate gyrus, anterior to the genu "
                    "of the corpus callosum and extending caudally along "
                    "the superior cingulate",
        "cytoarchitecture": "dysgranular/agranular cortex; six-layer "
                            "homologue with prominent layers II-III and V",
        "notes": (
            "Principal conflict-monitoring node of the dorsal cognitive "
            "ACC. Dense projections to and from dorsolateral prefrontal "
            "cortex (DLPFC) and pre-supplementary motor area; reciprocal "
            "connections with parietal cortex and with autonomic "
            "brainstem nuclei. On the right side the autonomic coupling "
            "is stronger than on the left; this is the anatomical basis "
            "for the right ACC's larger affective/visceral contribution. "
            "Sits upstream of the motor-selection hierarchy — its "
            "control_demand output biases which action candidates survive "
            "the basal ganglia gate. Along with area 32 it forms the "
            "dorsal cognitive division. Area 25, the affective division, "
            "lives as a sibling package (cingulate/subgenual_area_25/), "
            "not in this registry; it carries the affective channel and "
            "contributes no conflict, error, or control_demand signal."
        ),
    }

    Anatomy is identical to the left except for the noted right-side
    autonomic coupling emphasis.

CONFIG (RIGHT)
--------------
The ACC has FOUR output channels (conflict, error, affect, control_demand),
not one aggregate. Config is therefore organised per-channel: for each
channel, the areas that carry it each declare a share, and the shares across
areas sum to 1.0. Areas 24 and 32 share the three cognitive channels; area 25
carries the affect channel from its own package.

    RIGHT_CONFIG = {
        # ---- per-channel shares within the ACC ----
        # conflict: 24 carries the larger share (principal conflict
        # monitoring); 32 takes the remainder. Mirrored: on the right the
        # split is the same 0.60/0.40, because the *anatomical* division of
        # conflict monitoring does not lateralise — only the feature
        # emphases below do.
        "conflict_weight":        0.60,   # area 32: 0.40

        # error: 32 carries the larger share; 24 takes the remainder.
        "error_weight":           0.35,   # area 32: 0.65

        # control_demand: shared evenly.
        "control_demand_weight":  0.50,   # area 32: 0.50

        # affect: owned by area 25. Areas 24 and 32 contribute zero here
        # by design; a non-zero value would signal a bug in the channel
        # partition.
        "affect_weight":          0.00,   # area 25: 1.00

        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: spatial/visuomotor conflict and autonomic-threat
        # conflict; lower lexical/verbal conflict.
        "lexical_conflict":          0.40,
        "spatial_conflict":          0.70,
        "verbal_prediction_error":   0.35,
        "spatial_prediction_error":  0.55,
        "verbal_control_demand":     0.40,
        "spatial_control_demand":    0.65,

        # ---- connectivity priors to partner structures ----
        "to_dlpfc":               0.70,
        "to_pre_sma":             0.60,
        "to_parietal":            0.55,   # right: stronger parietal coupling
        "to_insula":              0.55,   # right: stronger visceral coupling
        "to_subgenual_25":        0.55,   # right: stronger affective handoff
        "to_posterior_cingulate": 0.30,
        "to_motor_cortex":        0.45,
        "to_commissures":         0.40,   # cross-midline conflict handoff
    }

    Notes on the weights:
      - Per-channel shares are constrained: for each channel, the shares
        across areas 24, 32, and 25 sum to 1.0. Mirror-assertion tests
        check this invariant independently of left/right symmetry.
      - The channel shares (conflict/error/control_demand/affect) are the
        SAME on left and right — the anatomical division of labour in the
        ACC is not lateralised. Only the feature emphases and connectivity
        priors differ. This is why `conflict_weight` etc. are not mirrored
        complements: they are structural, not configurable per side.
      - `affect_weight: 0.00` here is intentional and load-bearing. If area
        24 ever contributes to affect, the channel partition has been
        broken and should be fixed in the ACC class, not by tuning this
        weight.
      - Feature weights are multipliers on features extracted by the ACC
        sub-module; they do not stand alone.
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the ACC combines areas.
      - All values are plausible priors, not measured constants. The key
        constraints are the channel-sum invariant and the left/right mirror.

EXPORTS
-------
    from .brodmann_area_24 import BRODMANN_24    # int, == AREA_ID
    from .brodmann_area_24 import ANATOMY
    from .brodmann_area_24 import RIGHT_CONFIG
    from .brodmann_area_24 import SYSTEM         # str, "anterior_cingulate"

Consumers should use these names directly. Anything not listed here is private
and may change.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `anterior_cingulate/` (cycle; the ACC imports from
      here, not the other way round).
    - Must not import `subgenual_area_25/` (same layer; cross-references go
      through docstrings and the ACC class, not registry-to-package imports).
    - Must not contain runtime logic of any kind.
    - Must not import or reference the left hemisphere's area-24 package.
      Cross-hemisphere state exchange goes through
      `telencephalon/commissures/`, never through direct registry access.
    - Must not diverge in structure from the left hemisphere's area-24
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights.
"""