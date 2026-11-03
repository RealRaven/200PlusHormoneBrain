"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate.brodmann_areas.brodmann_area_31
=========================================================================================================================

Brodmann area 31 — left hemisphere.

A CONSTANT + CONFIG HOLDER. No compute, no state, no lifecycle. Declares the
canonical identity of area 31, says which functional sub-module owns it, and
supplies the per-area weights that the owning sub-module's `encode()` reads.
It defines no classes and no functions; the public surface is the four names
under "EXPORTS".

If you are looking for the computation area 31 participates in, it is in
`.../cingulate/posterior_cingulate/` — area 31 is one of the two areas (with
area 23) that make up the PCC's contextual/self-referential system. This
package is the *label*, not the *agent*.

IDENTITY
--------
    AREA_ID   = 31
    NAME      = "Brodmann area 31"
    SYSTEM    = "posterior_cingulate"
    LOBE      = "cingulate"
    SIDE      = "left"

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 31",
        "system": "posterior_cingulate",
        "location": "dorsal posterior cingulate gyrus, above area 23 and "
                    "extending caudally toward the precuneus and the "
                    "parieto-occipital junction",
        "cytoarchitecture": "granular cortex; six layers, layer IV less "
                            "prominent than in area 23",
        "notes": (
            "The more dorsal of the two PCC areas, and the one whose "
            "connectivity shifts away from the medial temporal lobe "
            "toward the precuneus, the lateral parietal cortex, and the "
            "visual association areas. Together with area 23 it "
            "constitutes the PCC hub whose dysfunction is associated "
            "with early Alzheimer's pathology; unlike area 23, area 31's "
            "contribution is more scene/visuospatial than "
            "verbal-autobiographical. The two areas are modelled as "
            "separate registry entries precisely because their "
            "connectivity profiles differ in this direction: area 23 "
            "pulls toward hippocampus and verbal context, area 31 pulls "
            "toward precuneus and visual scene. On the left side that "
            "pull is moderated by the left hemisphere's overall verbal "
            "bias, so area 31's scene weighting sits below what it would "
            "be on the right."
        ),
    }

CONFIG (LEFT)
-------------
The PCC has two output channels — `familiarity` and `self_relevance`. This
area contributes to both, with feature emphases below. Config is organised
as: (a) the area share within the two-area combination, summing to 1.0
across 23/31, and (b) per-feature emphases and connectivity priors used
inside this area's contribution.

    LEFT_CONFIG = {
        # ---- area share within the PCC's combined signal ----
        # 23 : 31  sum to 1.0; on the left, area 23 takes the majority
        # share (it is the more verbally-contextual area, matching the
        # left's verbal bias).
        "pcc_weight":             0.45,   # area 23: 0.55

        # ---- feature emphases inside this area's contribution ----
        # LEFT bias: scene/visual features are weighted up relative to
        # area 23's profile (because area 31 is the visual/spatial PCC
        # node), but remain below the right hemisphere's levels because
        # the left hemisphere's overall bias is verbal. Self-reference
        # and subjective familiarity are weighted slightly below area 23.
        "verbal_context":         0.50,   # area 23: 0.70
        "autobiographical":       0.55,   # area 23: 0.75
        "scene_construction":     0.55,   # area 23: 0.40
        "self_reference":         0.55,   # area 23: 0.65
        "subjective_familiarity": 0.55,   # area 23: 0.60

        # ---- connectivity priors to partner structures ----
        "to_hippocampus":         0.50,   # area 23: 0.65
        "to_precuneus":           0.65,   # area 23: 0.50
        "to_anterior_cingulate":  0.30,   # area 23: 0.30
        "to_retrosplenial":       0.55,   # area 23: 0.45
    }

    Notes on the weights:
      - `pcc_weight` across areas 23 and 31 sums to 1.0. On the left the
        split is 0.55 / 0.45 — area 23 takes the larger share because
        its verbal-contextual contribution matches the left hemisphere's
        verbal bias. On the right the split inverts (23: 0.45, 31: 0.55)
        because area 31's scene/visuospatial contribution matches the
        right hemisphere's spatial bias.
      - Feature weights are multipliers on the corresponding features
        extracted by the PCC sub-module. Area 31's profile is the more
        scene/visuospatial of the two, but on the left the scene
        weighting (0.55) is deliberately kept below the level area 31
        would take on the right (0.75) — the left's verbal bias
        moderates what the anatomical area would otherwise express.
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the PCC combines areas. Area 31's
        connectivity profile is the more posterior of the two — stronger
        precuneus and retrosplenial coupling, weaker hippocampal coupling
        — consistent with its role as the scene/visual contributor.
      - All values are plausible priors, not measured constants. The key
        constraints are the share-sum invariant and the left/right mirror.

EXPORTS
-------
    from .brodmann_area_31 import BRODMANN_31    # int, == AREA_ID
    from .brodmann_area_31 import ANATOMY
    from .brodmann_area_31 import LEFT_CONFIG
    from .brodmann_area_31 import SYSTEM         # str, "posterior_cingulate"

Consumers should use these names directly. Anything not listed here is private
and may change.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `posterior_cingulate/` (cycle; the PCC imports from
      here, not the other way round).
    - Must not contain runtime logic of any kind.
    - Must not diverge in structure from the right hemisphere's area-31
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights and the
      `pcc_weight` share. On each side the two-area sum must be 1.0.
"""