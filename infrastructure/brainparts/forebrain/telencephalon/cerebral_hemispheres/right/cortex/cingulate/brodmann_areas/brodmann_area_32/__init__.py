"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.brodmann_areas.brodmann_area_32
==========================================================================================================================

Brodmann area 32 — right hemisphere.

Mirror of the left area-32 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 32, says which
functional sub-module owns it, and supplies the per-area weights that the
owning sub-module's `encode()` reads. It defines no classes and no functions;
the public surface is the four names under "EXPORTS".

If you are looking for the computation area 32 participates in, it is in
`.../cingulate/anterior_cingulate/` — area 32 is the error/performance-
monitoring area of the ACC's dorsal cognitive division. This package is the
*label*, not the *agent*.

IDENTITY
--------
    AREA_ID   = 32
    NAME      = "Brodmann area 32"
    SYSTEM    = "anterior_cingulate"
    LOBE      = "cingulate"
    SIDE      = "right"

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 32",
        "system": "anterior_cingulate",
        "location": "dorsal anterior cingulate gyrus, anterior to area 24 "
                    "and extending rostrally toward the pregenual ACC and "
                    "the medial prefrontal cortex",
        "cytoarchitecture": "dysgranular/agranular cortex; transitional "
                            "between the agranular ACC and the granular "
                            "medial prefrontal cortex",
        "notes": (
            "Together with area 24 it forms the ACC's dorsal cognitive "
            "division. Area 32 sits more rostrally than area 24, closer "
            "to medial prefrontal cortex (mPFC), and its connectivity "
            "reflects that position: strong coupling to mPFC and to "
            "ventromedial prefrontal cortex, in addition to DLPFC. "
            "Functionally area 32 is the error/performance-monitoring "
            "node — it carries the larger share of the ACC's `error` "
            "channel, computing prediction error between expected and "
            "actual outcomes, and it weighs performance evaluation more "
            "heavily than conflict detection. On the right side the "
            "prediction error it monitors is predominantly spatial and "
            "visuomotor, and its vmPFC coupling is somewhat stronger "
            "than on the left — consistent with the right hemisphere's "
            "overall spatial/threat-evaluation profile. The division from "
            "area 24 is functional, not just anatomical: the two areas "
            "use the same four-channel ACC output, but with different "
            "per-channel shares and different feature emphases. Area 25, "
            "the affective division, lives as a sibling package "
            "(cingulate/subgenual_area_25/) and carries the affect channel "
            "alone."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
The ACC has FOUR output channels (conflict, error, affect, control_demand),
not one aggregate. Config is therefore organised per-channel: for each
channel, the areas that carry it each declare a share, and the shares
across areas sum to 1.0. Areas 24 and 32 share the three cognitive
channels; area 25 carries the affect channel from its own package.

    RIGHT_CONFIG = {
        # ---- per-channel shares within the ACC ----
        # STRUCTURAL — identical to the left. The anatomical division of
        # labour between areas 24, 32, and 25 is not lateralised; only the
        # feature emphases and connectivity priors below mirror.
        "conflict_weight":        0.40,   # area 24: 0.60
        "error_weight":           0.65,   # area 24: 0.35
        "control_demand_weight":  0.50,   # area 24: 0.50
        "affect_weight":          0.00,   # area 25: 1.00

        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: spatial/visuomotor prediction error is the anchor
        # feature; verbal/lexical features are weighted down relative to
        # the left. As on the left, area 32's conflict features sit below
        # area 24's, and its error features sit above area 24's — the
        # area's functional identity is error-dominant on both sides.
        "lexical_conflict":          0.35,   # area 24 (R): 0.40
        "spatial_conflict":          0.55,   # area 24 (R): 0.70
        "verbal_prediction_error":   0.40,   # area 24 (R): 0.35
        "spatial_prediction_error":  0.75,   # area 24 (R): 0.55
        "verbal_control_demand":     0.40,   # area 24 (R): 0.40
        "spatial_control_demand":    0.55,   # area 24 (R): 0.65

        # ---- connectivity priors to partner structures ----
        "to_dlpfc":               0.60,   # area 24 (R): 0.70
        "to_pre_sma":             0.50,   # area 24 (R): 0.60
        "to_mpfc":                0.65,   # strong; rostral position
        "to_vmpfc":               0.70,   # right: stronger vmPFC/outcome-
                                          # valuation coupling than left
        "to_parietal":            0.50,   # area 24 (R): 0.55
        "to_insula":              0.45,   # area 24 (R): 0.55
        "to_subgenual_25":        0.60,   # right: stronger affective handoff
        "to_posterior_cingulate": 0.35,   # area 24 (R): 0.30
        "to_motor_cortex":        0.40,   # area 24 (R): 0.45
        "to_commissures":         0.40,   # cross-midline error handoff
    }

    Notes on the weights:
      - Per-channel shares are STRUCTURAL: identical across hemispheres,
        and constrained so that for each channel the shares across areas
        24, 32, and 25 sum to 1.0. The mirror-assertion test should check
        both (a) the per-channel sum invariant and (b) structural-key
        equality across hemispheres, in addition to feature/connectivity
        mirroring.
      - `affect_weight: 0.00` here is intentional and load-bearing. If
        area 32 ever contributes to affect, the channel partition has
        been broken and should be fixed in the ACC class, not by tuning
        this weight.
      - Feature weights are multipliers on features extracted by the ACC
        sub-module. Area 32's `spatial_prediction_error` (0.75) is the
        single highest feature weight in the right ACC — the mirror of
        the left's `verbal_prediction_error: 0.75`. It is the area's
        principal contribution to the `error` channel on this side.
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the ACC combines areas. Area 32's
        profile is the more rostral/medial-prefrontal of the two cognitive
        areas on both sides; on the right the vmPFC and subgenual couplings
        are elevated (0.70 and 0.60 vs left 0.60 and 0.55), reflecting the
        right ACC's stronger affective/outcome coupling noted at the area
        24 level.
      - All values are plausible priors, not measured constants. The key
        constraints are the channel-sum invariant, the structural-key
        equality across hemispheres, and the feature/connectivity mirror.

EXPORTS
-------
    from .brodmann_area_32 import BRODMANN_32    # int, == AREA_ID
    from .brodmann_area_32 import ANATOMY
    from .brodmann_area_32 import RIGHT_CONFIG
    from .brodmann_area_32 import SYSTEM         # str, "anterior_cingulate"

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
    - Must not import or reference the left hemisphere's area-32 package.
      Cross-hemisphere state exchange goes through
      `telencephalon/commissures/`, never through direct registry access.
    - Must not diverge in structure from the left hemisphere's area-32
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys. The
      per-channel shares (conflict/error/control_demand/affect) are
      structural and identical across hemispheres; only feature/connectivity
      weights mirror. Any drift on a structural key is a bug.
"""