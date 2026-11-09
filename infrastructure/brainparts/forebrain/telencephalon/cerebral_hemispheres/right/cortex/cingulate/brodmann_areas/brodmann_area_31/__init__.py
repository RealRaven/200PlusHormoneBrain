"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.brodmann_areas.brodmann_area_31
==========================================================================================================================

Brodmann area 31 — right hemisphere.

Mirror of the left area-31 package. A CONSTANT + CONFIG HOLDER. No compute,
no state, no lifecycle. Declares the canonical identity of area 31, says which
functional sub-module owns it, and supplies the per-area weights that the
owning sub-module's `encode()` reads. It defines no classes and no functions;
the public surface is the four names under "EXPORTS".

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
    SIDE      = "right"

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
            "toward precuneus and visual scene. On the right side that "
            "pull is amplified by the right hemisphere's overall spatial "
            "bias, so area 31's scene weighting sits above what it would "
            "be on the left."
        ),
    }

    Anatomy is identical to the left. The right-side emphasis noted above
    is a functional, not anatomical, difference.

CONFIG (RIGHT)
--------------
The PCC has two output channels — `familiarity` and `self_relevance`. This
area contributes to both, with feature emphases below. Config is organised
as: (a) the area share within the two-area combination, summing to 1.0
across 23/31, and (b) per-feature emphases and connectivity priors used
inside this area's contribution.

    RIGHT_CONFIG = {
        # ---- area share within the PCC's combined signal ----
        # 23 : 31  sum to 1.0; on the right, area 31 takes the majority
        # share (it is the more scene/visuospatial area, matching the
        # right's spatial bias).
        "pcc_weight":             0.55,   # area 23: 0.45

        # ---- feature emphases inside this area's contribution ----
        # RIGHT bias: scene/visuospatial features are weighted up
        # relative to area 23's profile on this side, and above the left
        # area-31 levels; verbal/autobiographical are weighted lower.
        # Self-reference and subjective familiarity are higher than the
        # left area-31 because the right's holistic self-context leans
        # on scene and spatial self-representation.
        "verbal_context":         0.35,   # area 23 (R): 0.40
        "autobiographical":       0.45,   # area 23 (R): 0.50
        "scene_construction":     0.75,   # area 23 (R): 0.40
        "self_reference":         0.65,   # area 23 (R): 0.55
        "subjective_familiarity": 0.70,   # area 23 (R): 0.65

        # ---- connectivity priors to partner structures ----
        "to_hippocampus":         0.45,   # area 23 (R): 0.60
        "to_precuneus":           0.80,   # area 23 (R): 0.70
        "to_anterior_cingulate":  0.30,   # area 23 (R): 0.30
        "to_retrosplenial":       0.70,   # area 23 (R): 0.60
    }

    Notes on the weights:
      - `pcc_weight` across areas 23 and 31 sums to 1.0. On the right the
        split is 0.45 / 0.55 — area 31 takes the larger share because its
        scene/visuospatial contribution matches the right hemisphere's
        spatial bias. The left split is the mirror (23: 0.55, 31: 0.45).
      - Feature weights are multipliers on the corresponding features
        extracted by the PCC sub-module. Area 31's profile is the more
        scene/visuospatial of the two on both sides, and on the right the
        scene weighting is pushed further (0.75 vs 0.55 on the left) —
        the right's spatial bias amplifies what the anatomical area would
        express on its own.
      - Connectivity priors parameterise how strongly this area's signal
        reaches partner structures when the PCC combines areas. Area 31's
        connectivity profile is the more posterior of the two — stronger
        precuneus and retrosplenial coupling, weaker hippocampal coupling
        — and on the right those posterior couplings are higher than on
        the left (precuneus 0.80 vs 0.65, retrosplenial 0.70 vs 0.55),
        consistent with the right PCC's overall posterior dominance.
      - All values are plausible priors, not measured constants. The key
        constraints are the share-sum invariant and the left/right mirror.

EXPORTS
-------
    from .brodmann_area_31 import BRODMANN_31    # int, == AREA_ID
    from .brodmann_area_31 import ANATOMY
    from .brodmann_area_31 import RIGHT_CONFIG
    from .brodmann_area_31 import SYSTEM         # str, "posterior_cingulate"

Consumers should use these names directly. Anything not listed here is private
and may change.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not import `posterior_cingulate/` (cycle; the PCC imports from
      here, not the other way round).
    - Must not contain runtime logic of any kind.
    - Must not import or reference the left hemisphere's area-31 package.
      Cross-hemisphere state exchange goes through
      `telencephalon/commissures/`, never through direct registry access.
    - Must not diverge in structure from the left hemisphere's area-31
      package — same AREA_ID, SYSTEM, ANATOMY, same config keys; only the
      values differ, and only the feature/connectivity weights and the
      `pcc_weight` share. On each side the two-area sum must be 1.0.
"""