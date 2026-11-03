"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate.brodmann_areas.brodmann_area_30_retrosplenial
======================================================================================================================================

Brodmann area 30 (retrosplenial) — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares the
canonical identity of area 30, says which functional sub-module owns it, and
supplies the per-area weights that the owning sub-module's `encode()` reads.
It defines no classes and no functions; the public surface is the four names
under "EXPORTS".

If you are looking for the computation area 30 participates in, it is in
`.../cingulate/retrosplenial_cortex/` — area 30 is one of the three areas
(with 26 and 29) whose combined signal forms the RSC's `spatial_context` tag.
This package is the *label*, not the *agent*.

IDENTITY
--------
    AREA_ID   = 30
    NAME      = "Brodmann area 30 (retrosplenial)"
    SYSTEM    = "retrosplenial_cortex"
    LOBE      = "cingulate"
    SIDE      = "left"

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 30 (retrosplenial)",
        "system": "retrosplenial_cortex",
        "location": "caudal continuation of the granular retrosplenial "
                    "strip, dorsal and caudal to area 29, extending "
                    "toward the parieto-occipital junction",
        "cytoarchitecture": "granular cortex; the most caudal of the "
                            "three retrosplenial areas, sometimes "
                            "subdivided into 30a/30b",
        "notes": (
            "The most caudal and most visually/associatively coupled of "
            "the three retrosplenial areas. Connectivity continues the "
            "shift seen from 26 to 29 — away from the hippocampal "
            "formation, toward parietal association cortex, precuneus, "
            "and the occipital visual association areas. Implicated in "
            "scene recognition, spatial context updating, and the "
            "translation of visual scene information into a navigable "
            "spatial frame. Where 29 is the 'scene-construction' area "
            "and 26 the 'hippocampal-anchoring' area, 30 is the "
            "'scene-update' area: it is the RSC member most directly "
            "driven by incoming visual scene information, and its "
            "contribution to the combined `spatial_context` is weighted "
            "toward scene-identity and layout features rather than "
            "heading. Its share is the mirror of area 29's on the left "
            "(0.35 each), which is deliberate — the two together carry "
            "the scene-representational load that area 26's anchoring "
            "share (0.30) does not."
        ),
    }

CONFIG (LEFT)
-------------
The RSC produces one output channel, `spatial_context` (a vector with
dimensions for heading, scene identity, egocentric/allocentric frame, and
landmark binding). Config is organised as: (a) a share weight for this
area within the three-area combination, summing to 1.0 across 26/29/30,
and (b) per-feature emphases and connectivity priors used inside this
area's contribution.

    LEFT_CONFIG = {
        # ---- area share within the RSC's combined spatial_context ----
        # 26 : 29 : 30  sum to 1.0; on the left, 29 and 30 split the
        # scene-representational majority evenly.
        "rsc_weight":             0.35,   # area 26: 0.30, area 29: 0.35

        # ---- feature emphases inside this area's contribution ----
        # LEFT bias: strongest scene-identity and landmark-language
        # weighting of the three areas; heading and egocentric-frame
        # weighting lower than the right's. Area 30 is the most
        # scene-identity-driven contributor on this side.
        "heading":                0.40,
        "scene_identity":         0.85,
        "egocentric_frame":       0.45,
        "allocentric_frame":      0.65,
        "landmark_binding":       0.75,
        "spatial_layout":         0.60,

        # ---- connectivity priors to partner structures ----
        "to_hippocampus":         0.45,   # weakest of the three areas
        "to_parahippocampal":     0.65,
        "to_anterior_thalamus":   0.55,   # weaker than 29's 0.75
        "to_parietal":            0.65,   # strongest of the three areas
        "to_precuneus":           0.70,   # strongest of the three areas
        "to_posterior_cingulate": 0.55,
        "to_anterior_cingulate":  0.15,
        "to_commissures":         0.30,
    }

    Notes on the weights:
      - `rsc_weight` across areas 26, 29, and 30 sums to 1.0. On the left,
        the split is 0.30 / 0.35 / 0.35 — area 29 and area 30 share the
        scene-representational load equally, and both exceed area 26's
        hippocampal-anchoring share.
      - Feature weights are multipliers on the corresponding features
        extracted by the RSC sub-module. Area 30's profile is the most
        scene-identity-heavy of the three; on the left, that profile is
        pushed further toward the verbal-scene association side
        (`landmark_binding` 0.75, higher than 29's 0.70) because the left
        hemisphere's scene representation is more lexically entangled.
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the RSC combines areas. Area 30's
        connectivity profile is the most posterior of the three —
        strongest parietal and precuneus coupling, weakest hippocampal
        and anterior-thalamic coupling — consistent with its role as the
        visual-scene-driven contributor.
      - All values are plausible priors, not measured constants. The key
        constraints are the share-sum invariant and the left/right mirror.

EXPORTS
-------
    from .brodmann_area_30_retrosplenial import BRODMANN_30
    from .brodmann_area_30_retrosplenial import ANATOMY
    from .brodmann_area_30_retrosplenial import LEFT_CONFIG
    from .brodmann_area_30_retrosplenial import SYSTEM   # "retrosplenial_cortex"

The `_retrosplenial` suffix is part of the canonical identifier, for the
same reason documented in the area-26 package: 30 alone is ambiguous
within a registry that also holds 26 and 29, both of which are also
retrosplenial.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `retrosplenial_cortex/` (cycle; the RSC imports from
      here, not the other way round).
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-30
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights. The
      `rsc_weight` share is per-hemisphere (see area-26 docstring) and
      may differ from the right's; on each side the three-area sum must
      be 1.0.
"""