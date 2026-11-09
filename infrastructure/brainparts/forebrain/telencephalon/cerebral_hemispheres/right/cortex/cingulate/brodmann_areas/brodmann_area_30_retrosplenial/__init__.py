"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.brodmann_areas.brodmann_area_30_retrosplenial
=======================================================================================================================================

Brodmann area 30 (retrosplenial) — right hemisphere.

Mirror of the left area-30 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 30, says which
functional sub-module owns it, and supplies the per-area weights that the
owning sub-module's `encode()` reads. It defines no classes and no functions;
the public surface is the four names under "EXPORTS".

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
    SIDE      = "right"

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
            "driven by incoming visual scene information. On the right "
            "side this visual-scene-driven role is expressed with a "
            "stronger spatial-layout and heading component than on the "
            "left. Its share is the mirror of area 29's on the right "
            "(0.325 each), which is deliberate — the two together carry "
            "the scene-representational load that area 26's anchoring "
            "share (0.35) does not."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
The RSC produces one output channel, `spatial_context` (a vector with
dimensions for heading, scene identity, egocentric/allocentric frame, and
landmark binding). Config is organised as: (a) a share weight for this
area within the three-area combination, summing to 1.0 across 26/29/30,
and (b) per-feature emphases and connectivity priors used inside this
area's contribution.

    RIGHT_CONFIG = {
        # ---- area share within the RSC's combined spatial_context ----
        # 26 : 29 : 30  sum to 1.0; on the right, area 26 takes slightly
        # more than on the left (0.35), and 29/30 split the remainder
        # evenly.
        "rsc_weight":             0.325,   # area 26: 0.35, area 29: 0.325

        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: scene-identity and spatial-layout weighting higher
        # than area 29's, and heading/egocentric weighting lower — area
        # 30 is the most scene-identity- and layout-driven contributor on
        # this side, but still expressed through a right-leaning spatial
        # profile (heading and egocentric remain well above the left's).
        "heading":                0.55,
        "scene_identity":         0.75,
        "egocentric_frame":       0.60,
        "allocentric_frame":      0.65,
        "landmark_binding":       0.55,
        "spatial_layout":         0.75,

        # ---- connectivity priors to partner structures ----
        "to_hippocampus":         0.50,   # weakest of the three areas
        "to_parahippocampal":     0.65,
        "to_anterior_thalamus":   0.55,   # weaker than 29's 0.75
        "to_parietal":            0.75,   # strongest of the three areas
        "to_precuneus":           0.80,   # strongest of the three areas
        "to_posterior_cingulate": 0.55,
        "to_anterior_cingulate":  0.15,
        "to_commissures":         0.35,
    }

    Notes on the weights:
      - `rsc_weight` across areas 26, 29, and 30 sums to 1.0. On the right,
        the split is 0.35 / 0.325 / 0.325 — area 26 takes a slightly larger
        share than on the left (0.30), and 29/30 split the remainder
        evenly. The exact split is a prior, not measured; the sum-to-1
        invariant is the constraint.
      - Feature weights are multipliers on the corresponding features
        extracted by the RSC sub-module. Area 30's profile is the most
        scene-identity/layout-heavy of the three on the right, while
        remaining clearly more spatially-weighted than its left
        counterpart (heading 0.55 vs 0.40, egocentric 0.60 vs 0.45,
        layout 0.75 vs 0.60).
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the RSC combines areas. Area 30's
        connectivity profile is the most posterior of the three —
        strongest parietal and precuneus coupling, weakest hippocampal
        and anterior-thalamic coupling — consistent with its role as the
        visual-scene-driven contributor, and on the right those posterior
        couplings are higher than on the left (parietal 0.75 vs 0.65,
        precuneus 0.80 vs 0.70), reflecting the right RSC's overall
        posterior/parietal dominance.
      - All values are plausible priors, not measured constants. The key
        constraints are the share-sum invariant and the left/right mirror.

EXPORTS
-------
    from .brodmann_area_30_retrosplenial import BRODMANN_30
    from .brodmann_area_30_retrosplenial import ANATOMY
    from .brodmann_area_30_retrosplenial import RIGHT_CONFIG
    from .brodmann_area_30_retrosplenial import SYSTEM   # "retrosplenial_cortex"

The `_retrosplenial` suffix is part of the canonical identifier, for the
same reason documented in the area-26 package: 30 alone is ambiguous
within a registry that also holds 26 and 29, both of which are also
retrosplenial. The suffix must be used consistently on both sides.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `retrosplenial_cortex/` (cycle; the RSC imports from
      here, not the other way round).
    - Must not contain runtime logic of any kind.
    - Must not import or reference the left hemisphere's area-30 package.
      Cross-hemisphere state exchange goes through
      `telencephalon/commissures/`, never through direct registry access.
    - Must not diverge in structure from the left hemisphere's area-30
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights. The
      `rsc_weight` share is per-hemisphere (see area-26 docstring) and
      differs from the left's (0.325 vs 0.35); on each side the three-area
      sum must still be 1.0, and the two sides' shares together are not
      constrained to complement.
"""