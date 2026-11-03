"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.brodmann_areas.brodmann_area_29_retrosplenial
=======================================================================================================================================

Brodmann area 29 (retrosplenial) — right hemisphere.

Mirror of the left area-29 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 29, says which
functional sub-module owns it, and supplies the per-area weights that the
owning sub-module's `encode()` reads. It defines no classes and no functions;
the public surface is the four names under "EXPORTS".

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
    SIDE      = "right"

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
            "navigation. On the right side the heading/egocentric "
            "component of this area's contribution is expressed more "
            "strongly than on the left (right RSC is more spatially "
            "dominant overall). The three retrosplenial areas 26/29/30 "
            "are all present as registry entries; the RSC sub-module "
            "combines their contributions via the share weights below."
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
        "rsc_weight":             0.325,   # area 26: 0.35, area 30: 0.325

        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: heading and egocentric frame are weighted up;
        # scene-identity-by-language and landmark-language binding are
        # weighted lower than the left's.
        "heading":                0.70,
        "scene_identity":         0.60,
        "egocentric_frame":       0.75,
        "allocentric_frame":      0.60,
        "landmark_binding":       0.50,
        "spatial_layout":         0.70,

        # ---- connectivity priors to partner structures ----
        "to_hippocampus":         0.60,   # weaker than area 26's 0.85
        "to_parahippocampal":     0.55,
        "to_anterior_thalamus":   0.75,
        "to_parietal":            0.65,   # right: stronger than left's 0.55
        "to_precuneus":           0.70,   # right: stronger precuneus coupling
        "to_posterior_cingulate": 0.60,
        "to_anterior_cingulate":  0.20,
        "to_commissures":         0.35,
    }

    Notes on the weights:
      - `rsc_weight` across areas 26, 29, and 30 sums to 1.0. On the right,
        the split is 0.35 / 0.325 / 0.325 — area 26 takes a slightly
        larger share than on the left (0.30), and 29/30 split the
        remainder evenly. The exact split is a prior, not measured; the
        sum-to-1 invariant is the constraint.
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
    from .brodmann_area_29_retrosplenial import RIGHT_CONFIG
    from .brodmann_area_29_retrosplenial import SYSTEM   # "retrosplenial_cortex"

The `_retrosplenial` suffix is part of the canonical identifier, for the
same reason documented in the area-26 package: 29 alone is ambiguous
within a registry that also holds 26 and 30, both of which are also
retrosplenial. The suffix must be used consistently on both sides.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `retrosplenial_cortex/` (cycle; the RSC imports from
      here, not the other way round).
    - Must not contain runtime logic of any kind.
    - Must not import or reference the left hemisphere's area-29 package.
      Cross-hemisphere state exchange goes through
      `telencephalon/commissures/`, never through direct registry access.
    - Must not diverge in structure from the left hemisphere's area-29
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights. The
      `rsc_weight` share is per-hemisphere (see area-26 docstring) and
      differs from the left's (0.325 vs 0.35); on each side the three-area
      sum must still be 1.0, and the two sides' shares together are not
      constrained to complement.
"""