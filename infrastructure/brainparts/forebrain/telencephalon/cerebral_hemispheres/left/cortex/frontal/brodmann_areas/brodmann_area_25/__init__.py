"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_25
======================================================================================================================

Brodmann area 25 (subgenual anterior cingulate) — left hemisphere — CROSS-
LOBE POINTER.

THIS IS NOT A COMPUTE NODE. It is not a config holder. It has no
LEFT_CONFIG, no encode(), no state. `SYSTEM` is the empty list. The
package exports exactly three fields (BRODMANN_25, ANATOMY, SYSTEM) plus
two structural None fields (SUB_REGION, GROUPING) for registry-shape
consistency, and nothing else.

The COMPUTE for area 25 lives in `cingulate/subgenual_area_25/`. That is
the stateful affect channel documented at length in the cingulate tree.
This package exists for two reasons, both narrow:

    1. ANATOMICAL COMPLETENESS. Brodmann 25 sits anatomically at the
       frontal/cingulate boundary (the subgenual region is on the
       medial surface of the frontal lobe, but it is cytoarchitecturally
       and functionally part of the anterior cingulate). Both the frontal
       tree and the cingulate tree are correct in claiming it, and the
       anatomical ambiguity is real, not a tree artifact to be resolved
       by fiat.

    2. REGISTRY CROSS-REFERENCE. Code that iterates the frontal registry
       and encounters brodmann_area_25 should see an explicit,
       documented entry saying "this area's compute is elsewhere,"
       rather than silently missing an area that the anatomy says
       should be there. The alternative — omitting area 25 from the
       frontal tree entirely — would leave an anatomical gap in the
       frontal registry that is not a real absence but a filing
       decision.

If you are looking for the affect computation that area 25 performs —
the stateful `encode()` that produces the ACC's fourth channel —
import it from `cingulate/subgenual_area_25/`. This package does not
contain that computation and must never grow it.

WHAT "CROSS-LOBE POINTER" MEANS (and does not mean)
----------------------------------------------------
It means this package's only runtime purpose is to answer the question
"is there a Brodmann 25 in the frontal tree, and if so, where's its
compute?" with "yes, and the compute is in the cingulate tree."

It does not mean:
    - duplicate compute (there is none here)
    - a second affect channel (there is one, in cingulate)
    - a forwarded compute (this package does not call into cingulate at
      runtime; the cingulate package is documented in ANATOMY, not
      imported)
    - an optional config that can be overridden here (there is no config;
      the affect channel's config is the LEFT_CONFIG / RIGHT_CONFIG in
      cingulate/subgenual_area_25/)

The relationship is documentary, not computational. Any runtime reference
from this package to the cingulate package is a bug (see the "MUST NOT
DO" section below).

IDENTITY
--------
    AREA_ID    = 25
    NAME       = "Brodmann area 25 (subgenual anterior cingulate)"
    SYSTEM     = []           # empty — this is not a frontal compute area
    SUB_REGION = None         # no sub-region owns it from the frontal side
    LOBE       = "frontal (boundary; compute in cingulate)"
    SIDE       = "left"
    GROUPING   = None

The empty SYSTEM list is the operative field. It is what consumer code
should check to distinguish a frontal compute area (SYSTEM non-empty) from
a cross-lobe pointer (SYSTEM empty). The registry parent's contract
(brodmann_areas/__init__.py) explicitly requires consumers to skip entries
with `SYSTEM == []`, with a documented comment explaining why — the
"documented skip, not silent skip" rule.

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 25 (subgenual anterior cingulate)",
        "system": None,
        "sub_region": None,
        "grouping": None,
        "location": "ventral anterior cingulate, subgenual to the genu "
                    "of the corpus callosum, on the medial surface of "
                    "the frontal lobe at the frontal/cingulate boundary",
        "cytoarchitecture": "agranular cortex; six-layer homologue with "
                            "prominent layer V projection neurons. "
                            "Cytoarchitecturally continuous with the "
                            "dorsal anterior cingulate (areas 24, 32) "
                            "and functionally grouped with the ACC, "
                            "despite the frontal-lobe location.",
        "compute_location": "cingulate/subgenual_area_25/",
        "compute_summary": (
            "The ACC's affective division. Single output channel: "
            "`affect` (scalar 0..1, the unpleasantness weight). "
            "Stateful across ticks — carries an `affective_setpoint` "
            "and a `treatment_response` parameter, documented in the "
            "cingulate package. Not duplicated here."
        ),
        "notes": (
            "Brodmann 25 is anatomically at the frontal/cingulate "
            "boundary. The subgenual region is physically on the "
            "medial surface of the frontal lobe (ventral to the genu "
            "of the corpus callosum), but its cytoarchitecture is "
            "continuous with the dorsal anterior cingulate (areas 24, "
            "32) and its function — sustained affect, threat, autonomic "
            "regulation, and the treatment-resistant-depression circuit "
            "targeted by DBS — is ACC function, not frontal-executive "
            "function. The cingulate tree therefore owns its compute, "
            "and the frontal tree carries a cross-lobe pointer. Both "
            "placements are correct: this entry documents the anatomy, "
            "the cingulate package documents the computation. See "
            "`cingulate/subgenual_area_25/` for the stateful affect "
            "channel, its setpoint dynamics, and its treatment-response "
            "knob."
        ),
    }

CONFIG
------
There is NO config. There is no `LEFT_CONFIG`, no `RIGHT_CONFIG`, no
`SUB_REGION`-specific config block, no per-system block. The affect
channel's config (interoceptive/threat/verbal weights, treatment_response,
setpoint_time_constant, affect_floor/affect_ceil) lives in
`cingulate/subgenual_area_25/LEFT_CONFIG` on this hemisphere and
`.../RIGHT_CONFIG` on the other.

If you are looking for area 25's config in this file and not finding
it, this paragraph is why. It is not an oversight.

EXPORTS
-------
    from .brodmann_area_25 import BRODMANN_25     # int, == AREA_ID (25)
    from .brodmann_area_25 import ANATOMY
    from .brodmann_area_25 import SYSTEM          # [] — empty
    from .brodmann_area_25 import SUB_REGION      # None
    from .brodmann_area_25 import GROUPING        # None

That is the entire public surface. There is no config, no compute, no
class, no function.

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_25`) — area 25 is a direct child
of brodmann_areas/, not nested. Registry-iteration code that wants to
skip this entry should check `if not entry.SYSTEM: continue` with a
comment pointing at this file — the "documented skip, not silent skip"
rule from the parent registry's contract.

CROSS-MIDLINE RULE
------------------
This package has no state, so the standard "no cross-midline state bleed"
rationale does not apply directly. The rule that does apply is
**structural consistency**: this package must be structurally identical
to the right hemisphere's brodmann_area_25 package — same AREA_ID, empty
SYSTEM, same SUB_REGION/GROUPING (None/None), same ANATOMY except for
SIDE. If the two hemispheres' pointer packages ever diverge, that is a
bug (they are documenting the same anatomical structure and pointing at
the same two compute packages, one per hemisphere).

The two hemispheres' *compute* packages
(cingulate/subgenual_area_25/left and /right) are independent and their
state diverges under sustained threat, as documented in the cingulate
tree. That independence is a property of the compute packages, not of
this pointer. The pointer packages are structurally identical; the
compute packages are stateful and independent.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define `encode()`, `step()`, or any stateful object.
    - Must not gain a `LEFT_CONFIG`, `RIGHT_CONFIG`, or any config
      whatsoever. The absence of config is the point. If a future
      change wants to give area 25 a frontal-lobe-specific config
      (e.g. to model a frontal contribution to the affect channel),
      that is a signal that the cingulate compute needs a documented
      frontal input — not that this pointer needs a config.
    - Must not import `cingulate/subgenual_area_25/` or reference it at
      runtime. The pointer relationship is documentary (ANATOMY notes
      and this docstring), not computational. A runtime import would
      couple the frontal registry to the cingulate compute, which is
      exactly the kind of layering violation the registry's
      "import direction one-way" rule prevents.
    - Must not be imported by `cingulate/subgenual_area_25/` or by
      any cingulate compute package. The cingulate tree does not need
      to know that the frontal tree carries a pointer to it.
    - Must not be promoted to a runtime package without a documented
      functional justification. "It's anatomically on the frontal
      lobe" is not a reason to give it compute — the anatomy is why
      it appears in the frontal tree, but the function is what makes
      the compute live in cingulate. If a future change wants area 25
      to be a frontal compute node, that change would need to also
      explain why the cingulate's affect channel is not the right
      home for it (and would essentially be a rearchitecture, not a
      config addition).
    - Must not diverge in structure from the right hemisphere's
      brodmann_area_25 package — same AREA_ID, empty SYSTEM, same
      SUB_REGION/GROUPING, same ANATOMY content (except SIDE). The
      two pointer packages are structurally identical by design.

RELATIONSHIP TO cingulate/subgenual_area_25/
---------------------------------------------
For reference, the cingulate package this file points at has the
following shape (documented fully in that package):

    subgenual_area_25/__init__.py
        SYSTEM     = ["anterior_cingulate"]
        LOBE       = "cingulate"
        SUB_REGION = None
        GROUPING   = None
        LEFT_CONFIG = {
            interoceptive_weight, threat_weight, verbal_affect_weight,
            treatment_response, top_down_weight,
            setpoint_time_constant, setpoint_initial,
            affect_floor, affect_ceil
        }
        LEFT_INITIAL_STATE = {"affective_setpoint": ...}
        SubgenualArea25 (class) — stateful compute
        encode(inputs, state, config) -> (affect, new_state)

The frontal tree's brodmann_area_25 is the anatomical counterpart of
that package: it says "this area exists, it appears here anatomically,
its compute is over there." It does NOT mirror the cingulate config,
duplicate the state contract, or provide a second access path to the
affect channel. Those all live exclusively in the cingulate package.
"""