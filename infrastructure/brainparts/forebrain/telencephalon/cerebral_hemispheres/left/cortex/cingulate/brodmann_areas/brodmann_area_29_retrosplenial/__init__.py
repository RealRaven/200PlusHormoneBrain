"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate.brodmann_areas.brodmann_area_29_retrosplenial
======================================================================================================================================

Brodmann area 29 (retrosplenial) — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares the
canonical identity of area 29, says which functional sub-module owns it, and
supplies the per-area weights that the owning sub-module's `encode()` reads.
It defines no classes and no functions; the public surface is the four names
under "EXPORTS".

If you are looking for the computation area 29 participates in, it is in
`.../cingulate/retrosplenial_cortex/` — area 29 is one of the three areas
(with 26 and 30) whose combined signal forms the RSC's `spatial_context` tag.
This package is the *label*, not the *agent*.

IDENTITY
--------
    AREA_ID   = 29
    NAME      = "Brodmann area 29 (retrosplenial)"
    SYSTEM    = "retrosplenial_cortex"
    LOBE      = "cingulate"
    SIDE      = "left"

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 29 (retrosplenial)",
        "system": "retrosplenial_cortex",
        "location": "granular retrosplenial cortex, dorsal to area 26, "
                    "along the ventral bank of the caudal cingulate "
                    "sulcus and around the splenium",
        "cytoarchitecture": "granular cortex; prominent layer IV, "
                            "subdivided into 29a/29b/29c by some authors",
        "notes": (
            "The more dorsal and more heavily granular of the two "
            "principal retrosplenial areas (26 and 29; area 30 continues "
            "the strip caudally). Connectivity shifts away from the "
            "hippocampal formation toward parietal association cortex, "
            "the posterior cingulate, and the anterior thalamic nuclei. "
            "Implicated in scene construction, spatial-layout coding, and "
            "the egocentric/allocentric frame translation that underlies "
            "navigation. Its cytoarchitectural distinctness from area 26 "
            "— heavier granulation, weaker hippocampal input, stronger "
            "parietal input — is the anatomical basis for treating the "
            "two as separate registry entries rather than as one "
            "'retrosplenial area'. Of the three RSC areas, 29 and 30 "
            "share the larger aggregate share of the combined "
            "`spatial_context`; see CONFIG below."
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
        # majority evenly.
        "rsc_weight":             0.35,   # area 26: 0.30, area 30: 0.35

        # ---- feature emphases inside this area's contribution ----
        # LEFT bias: scene identity and landmark-language binding are
        # weighted up (verbal-scene association); heading and egocentric
        # frame are weighted lower than the right's.
        "heading":                0.45,
        "scene_identity":         0.80,
        "egocentric_frame":       0.50,
        "allocentric_frame":      0.65,
        "landmark_binding":       0.70,
        "spatial_layout":         0.55,

        # ---- connectivity priors to partner structures ----
        "to_hippocampus":         0.55,   # weaker than area 26's 0.80
        "to_parahippocampal":     0.60,
        "to_anterior_thalamus":   0.75,   # strong; anterior thalamic link
        "to_parietal":            0.55,   # stronger than area 26's 0.25
        "to_precuneus":           0.55,
        "to_posterior_cingulate": 0.60,
        "to_anterior_cingulate":  0.20,
        "to_commissures":         0.30,
    }

    Notes on the weights:
      - `rsc_weight` across areas 26, 29, and 30 sums to 1.0. On the left,
        the split is 0.30 / 0.35 / 0.35 — area 29 and area 30 share the
        scene-representational load, and both take more than area 26's
        hippocampal-anchoring share.
      - Feature weights are multipliers on the corresponding features
        extracted by the RSC sub-module.
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the RSC combines areas.
      - All values are plausible priors, not measured constants. The key
        constraints are the share-sum invariant and the left/right mirror.

EXPORTS
-------
    from .brodmann_area_29_retrosplenial import BRODMANN_29
    from .brodmann_area_29_retrosplenial import ANATOMY
    from .brodmann_area_29_retrosplenial import LEFT_CONFIG
    from .brodmann_area_29_retrosplenial import SYSTEM   # "retrosplenial_cortex"

The `_retrosplenial` suffix is part of the canonical identifier, for the
same reason documented in the area-26 package: 29 alone is ambiguous
within a registry that also holds 26 and 30, both of which are also
retrosplenial.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `retrosplenial_cortex/` (cycle; the RSC imports from
      here, not the other way round).
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-29
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights. The
      `rsc_weight` share is per-hemisphere (see area-26 docstring) and
      may differ from the right's; on each side the three-area sum must
      be 1.0.
"""