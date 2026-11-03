"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_25
=======================================================================================================================

Brodmann area 25 (subgenual anterior cingulate) — right hemisphere — CROSS-
LOBE POINTER.

Mirror of the left brodmann_area_25 package. THIS IS NOT A COMPUTE NODE. It
is not a config holder. It has no RIGHT_CONFIG, no encode(), no state.
`SYSTEM` is the empty list. The package exports exactly three fields
(BRODMANN_25, ANATOMY, SYSTEM) plus two structural None fields
(SUB_REGION, GROUPING) for registry-shape consistency, and nothing else.

The COMPUTE for area 25 on this hemisphere lives in the RIGHT
`cingulate/subgenual_area_25/`. That is the stateful affect channel
documented at length in the cingulate tree; on the right its
`affective_setpoint` has a shorter time constant and its valence bias
leans more strongly toward threat, as documented there. This package
exists for two reasons, both narrow:

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
       should be there.

If you are looking for the affect computation that area 25 performs on
this hemisphere — the stateful `encode()` that produces the ACC's fourth
channel, with the right's shorter setpoint time constant — import it
from the RIGHT `cingulate/subgenual_area_25/`. This package does not
contain that computation and must never grow it.

WHAT "CROSS-LOBE POINTER" MEANS (and does not mean)
----------------------------------------------------
Identical to the left's definition, restated for readers who only see
the right side:

It means this package's only runtime purpose is to answer "is there a
Brodmann 25 in the right frontal tree, and if so, where's its compute?"
with "yes, and the compute is in the right cingulate tree."

It does not mean:
    - duplicate compute (there is none here)
    - a second affect channel (there is one per hemisphere, in cingulate)
    - a forwarded compute (this package does not call into cingulate at
      runtime; the cingulate package is documented in ANATOMY, not
      imported)
    - an optional config that can be overridden here (there is no config)

The relationship is documentary, not computational. Any runtime reference
from this package to the right cingulate package is a bug.

IDENTITY
--------
    AREA_ID    = 25
    NAME       = "Brodmann area 25 (subgenual anterior cingulate)"
    SYSTEM     = []           # empty — this is not a frontal compute area
    SUB_REGION = None         # no sub-region owns it from the frontal side
    LOBE       = "frontal (boundary; compute in cingulate)"
    SIDE       = "right"
    GROUPING   = None

The empty SYSTEM list is the operative field, exactly as on the left.
Consumer code that iterates the right frontal registry skips it with a
documented comment pointing here, per the parent registry's "documented
skip, not silent skip" rule.

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
            "The ACC's affective division on the right hemisphere. "
            "Single output channel: `affect` (scalar 0..1). Stateful "
            "across ticks — carries an `affective_setpoint` and a "
            "`treatment_response` parameter. On the right, the "
            "interoceptive and threat contributors are weighted more "
            "heavily, the verbal-affect contributor less heavily, and "
            "the setpoint time constant is shorter than on the left "
            "(8 ticks vs 20), so the right's setpoint drifts more "
            "rapidly under sustained threat. Fully documented in the "
            "right cingulate package. Not duplicated here."
        ),
        "notes": (
            "Brodmann 25 is anatomically at the frontal/cingulate "
            "boundary. The subgenual region is physically on the "
            "medial surface of the frontal lobe, but its cytoarchitecture "
            "is continuous with the dorsal anterior cingulate (areas 24, "
            "32) and its function — sustained affect, threat, autonomic "
            "regulation, and the treatment-resistant-depression circuit "
            "targeted by DBS — is ACC function. The cingulate tree owns "
            "its compute; the frontal tree carries a cross-lobe pointer. "
            "See the RIGHT `cingulate/subgenual_area_25/` for the "
            "stateful affect channel with the right hemisphere's "
            "setpoint dynamics (shorter time constant, faster drift "
            "under threat, stronger interoceptive/threat weighting)."
        ),
    }

    Anatomy is identical to the left's except for the SIDE field and the
    two cross-reference fields (`compute_location` and
    `compute_summary`), which point at the right hemisphere's cingulate
    package and note the right-side setpoint dynamics. The anatomical
    structure itself is bilateral and symmetric; the functional
    difference lives in the compute package this pointer points at.

CONFIG
------
There is NO config. The affect channel's config lives in the RIGHT
`cingulate/subgenual_area_25/RIGHT_CONFIG` — including the right's
shorter `setpoint_time_constant` (8 ticks), higher interoceptive and
threat weights, and lower verbal-affect weight.

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
comment pointing at this file.

CROSS-MIDLINE RULE
------------------
This package has no state, so the standard "no state bleed between
hemispheres" rationale does not apply directly. The rule that does
apply is **structural consistency**: this package must be structurally
identical to the LEFT hemisphere's brodmann_area_25 package — same
AREA_ID, empty SYSTEM, same SUB_REGION/GROUPING (None/None), same ANATOMY
content except for the SIDE field and the two cross-reference fields
(`compute_location`, `compute_summary`, which are per-hemisphere by
design). If the two pointer packages' *structure* ever diverges (e.g. one
gains a config, or one's SYSTEM becomes non-empty), that is a bug: they
are documenting the same anatomical structure and should be structurally
identical.

The two hemispheres' *compute* packages
(cingulate/subgenual_area_25/left and /right) are independent, and their
state diverges under sustained threat as documented in the cingulate
tree (right setpoint drifts faster because its time constant is shorter).
That independence is a property of the compute packages, not of this
pointer. The pointer packages are structurally identical; the compute
packages are stateful and independent.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define `encode()`, `step()`, or any stateful object.
    - Must not gain a `LEFT_CONFIG`, `RIGHT_CONFIG`, or any config
      whatsoever. The absence of config is the point.
    - Must not import the RIGHT `cingulate/subgenual_area_25/` or
      reference it at runtime. The pointer relationship is documentary,
      not computational. A runtime import would couple the right
      frontal registry to the right cingulate compute.
    - Must not import the LEFT `cingulate/subgenual_area_25/` either.
      Cross-midline access goes through the commissures, never through
      direct import — and for a pointer package, "cross-midline access"
      means importing the other hemisphere's compute, which is doubly
      wrong (it bypasses the commissures AND it bypasses the pointer's
      own hemisphere's compute).
    - Must not be imported by either cingulate package. The cingulate
      tree does not need to know that the frontal tree carries a
      pointer to it.
    - Must not be promoted to a runtime package without a documented
      functional justification.
    - Must not diverge in STRUCTURE from the left hemisphere's
      brodmann_area_25 package — same AREA_ID, empty SYSTEM, same
      SUB_REGION/GROUPING (None/None), same ANATOMY field set. Only
      SIDE and the two cross-reference fields (compute_location,
      compute_summary) differ. If the two pointer packages' *structure*
      diverges, that is a bug, not a lateralisation decision.

RELATIONSHIP TO the RIGHT cingulate/subgenual_area_25/
-----------------------------------------------------
For reference, the right cingulate package this file points at has the
following shape (documented fully in that package):

    subgenual_area_25/__init__.py      [right hemisphere]
        SYSTEM     = ["anterior_cingulate"]
        LOBE       = "cingulate"
        SUB_REGION = None
        GROUPING   = None
        RIGHT_CONFIG = {
            interoceptive_weight:      0.75,   # left: 0.55
            threat_weight:             0.45,   # left: 0.30
            verbal_affect_weight:      0.10,   # left: 0.35
            treatment_response:        0.35,   # left: 0.55
            top_down_weight:           0.35,   # left: 0.50
            setpoint_time_constant:    8.0,    # left: 20.0
            setpoint_initial:          0.35,   # left: 0.30
            affect_floor:              0.00,
            affect_ceil:               1.00,
        }
        RIGHT_INITIAL_STATE = {"affective_setpoint": 0.35}
        SubgenualArea25 (class) — stateful compute
        encode(inputs, state, config) -> (affect, new_state)

The right frontal tree's brodmann_area_25 is the anatomical counterpart
of that package: it says "this area exists, it appears here anatomically,
its compute is over there." It does NOT mirror the cingulate config,
duplicate the state contract, or provide a second access path to the
affect channel. Those all live exclusively in the right cingulate
package.
"""