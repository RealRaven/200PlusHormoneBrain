"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate.brodmann_areas.brodmann_area_26_retrosplenial
======================================================================================================================================

Brodmann area 26 (retrosplenial) — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares the
canonical identity of area 26, says which functional sub-module owns it, and
supplies the per-area weights that the owning sub-module's `encode()` reads.
It defines no classes and no functions; the public surface is the four names
under "EXPORTS".

If you are looking for the computation area 26 participates in, it is in
`.../cingulate/retrosplenial_cortex/` — area 26 is one of the three areas
(with 29 and 30) whose combined signal forms the RSC's `spatial_context` tag.
This package is the *label*, not the *agent*.

IDENTITY
--------
    AREA_ID   = 26
    NAME      = "Brodmann area 26 (retrosplenial)"
    SYSTEM    = "retrosplenial_cortex"
    LOBE      = "cingulate"
    SIDE      = "left"

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 26 (retrosplenial)",
        "system": "retrosplenial_cortex",
        "location": "ventral retrosplenial cortex, adjacent to the "
                    "subiculum and presubiculum, wrapping around the "
                    "caudal splenium of the corpus callosum",
        "cytoarchitecture": "granular cortex; sometimes subdivided into "
                            "26a/26b/26c by degree of granulation",
        "notes": (
            "The most ventral and most limbic-adjacent of the three "
            "retrosplenial areas. Dense reciprocal connectivity with the "
            "hippocampal formation (subiculum, presubiculum, "
            "parasubiculum) and with the anterior thalamic nuclei. "
            "Implicated in spatial memory consolidation and in scene "
            "recognition. Of the three retrosplenial areas, area 26 has "
            "the strongest hippocampal coupling and the weakest coupling "
            "to parietal association cortex; that connectivity profile "
            "is what makes it the 'spatial-memory-anchoring' contributor "
            "to the RSC's combined scene/heading signal. The three "
            "retrosplenial areas 26/29/30 are all present as registry "
            "entries; the RSC sub-module combines their contributions "
            "via the share weights below."
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
        # 26 : 29 : 30  sum to 1.0
        "rsc_weight":             0.30,   # area 29: 0.35, area 30: 0.35

        # ---- feature emphases inside this area's contribution ----
        # LEFT bias: less heading/layout dominance than the right, more
        # scene-identity and landmark-language weighting.
        "heading":                0.40,
        "scene_identity":         0.75,
        "egocentric_frame":       0.55,
        "allocentric_frame":      0.60,
        "landmark_binding":       0.60,
        "spatial_layout":         0.45,

        # ---- connectivity priors to partner structures ----
        "to_hippocampus":         0.80,   # strongest of the three areas
        "to_parahippocampal":     0.65,
        "to_anterior_thalamus":   0.70,
        "to_parietal":            0.25,   # weakest of the three areas
        "to_precuneus":           0.30,
        "to_posterior_cingulate": 0.55,
        "to_anterior_cingulate":  0.20,
        "to_commissures":         0.30,
    }

    Notes on the weights:
      - `rsc_weight` across areas 26, 29, and 30 sums to 1.0. On the left,
        the split is 0.30 / 0.35 / 0.35 — area 26 takes the smaller share
        because its contribution is more hippocampal-anchoring than
        scene-representational, and on the left that anchoring role is
        subsumed somewhat by the stronger left-hippocampal-coupling.
        (The exact split is a prior, not measured; the sum-to-1 invariant
        is the constraint.)
      - Feature weights are multipliers on the corresponding features
        extracted by the RSC sub-module.
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the RSC combines areas.
      - All values are plausible priors, not measured constants. The key
        constraints are the share-sum invariant and the left/right mirror.

EXPORTS
-------
    from .brodmann_area_26_retrosplenial import BRODMANN_26
    from .brodmann_area_26_retrosplenial import ANATOMY
    from .brodmann_area_26_retrosplenial import LEFT_CONFIG
    from .brodmann_area_26_retrosplenial import SYSTEM   # "retrosplenial_cortex"

The package name carries the `_retrosplenial` suffix because Brodmann 26
is not uniquely retrosplenial (Brodmann 29 and 30 also belong to the
retrosplenial group, and the name "area 26" alone would be ambiguous
against future registry entries). The suffix is part of the canonical
identifier and must be used consistently in imports.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `retrosplenial_cortex/` (cycle; the RSC imports from
      here, not the other way round).
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-26
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights (the
      `rsc_weight` share may differ as the mirror of the right's, but the
      three shares must still sum to 1.0).
"""