"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brodmann_area_33
======================================================================================================================

Brodmann area 33 — left hemisphere — TREE ARTIFACT.

THIS IS NOT A COMPUTE NODE. It has no LEFT_CONFIG, no encode(), no state.
It is not a cross-lobe pointer either: there is no compute package
anywhere in the project that this entry refers to. `SYSTEM` is the empty
list; the package exports exactly three fields (BRODMANN_33, ANATOMY,
SYSTEM) plus two structural None fields (SUB_REGION, GROUPING) for
registry-shape consistency, and nothing else.

Why the empty SYSTEM: because there is no function to route it to. Area
33 has no independent cognitive function in the model, no compute
package that would want to read its config, and no realistic prospect of
acquiring one (see "WHAT AREA 33 IS" below). If a future experiment
wanted to model area 33 as a distinct functional node, that is a
model-design decision with architectural consequences — it is not a
reason to add a config to this file.

WHY IT IS IN THE FRONTAL TREE AT ALL
------------------------------------
This is the honest part, and it is the part that distinguishes this entry
from brodmann_area_25's cross-lobe pointer:

    Area 33 is anatomically a small, transitional cingulate area — the
    "precallosal" or "callosal" area, a thin strip of cortex just above
    the rostrum of the corpus callosum, transitional between the
    agranular anterior cingulate (area 24) and the less-developed
    cortex of the callosal sulcus. It is properly a cingulate area.

    The tree nonetheless places brodmann_area_33/ under the frontal
    tree. That placement is not anatomically justified; it is a
    historical filing decision that the tree inherits and has not
    corrected. The intent is that area 33 be understood as a
    cingulate area for ownership purposes, despite its current location
    in the frontal tree.

This entry therefore documents the artifact honestly rather than
pretending the placement is meaningful. It exists for two narrow reasons:

    1. REGISTRY COMPLETENESS. A registry that lists the Brodmann areas
       of the frontal lobe should have an explicit entry for every area
       that appears in the tree, even — especially — the ones that
       shouldn't be there, so the misplacement is visible rather than
       silently passable.

    2. PRE-EMPTING CONFUSION. A future contributor who notices
       brodmann_area_33/ in the frontal tree and wonders "what does
       area 33 compute?" will find a clear answer here: nothing, and
       the placement is an artifact. The alternative — no entry, or
       an entry with a plausible-sounding config — would invite
       speculation about its function that the model has no basis for.

WHAT AREA 33 IS (and why it has no compute)
-------------------------------------------
Area 33 is a small transitional area with no well-characterized
independent function in the mature brain. Its cytoarchitecture is a
blend of area 24's agranular cortex and the more rudimentary cortex of
the callosal sulcus; its connectivity is largely overlapping with the
adjacent area 24 and area 32 (which are the actual ACC compute
sub-regions in this project). The literature does not support treating
it as a distinct functional node: no behavioural syndrome is reliably
associated with selective area-33 lesions, no well-replicated task
activates it selectively, and its role is generally understood as part
of the anterior cingulate complex rather than as a separate module.

The model's position follows from that: area 33 has no compute package
because there is no function to compute. Its anatomical neighbours in
the ACC carry the function that is real and measurable; area 33 is part
of that complex, not a node of its own. If a future experiment wanted
to treat it as a node (e.g. to model a specific transition-zone
function that turned out to be real and separable), that would require
a new compute sub-module — not a config added to this registry entry.

CONTRAST WITH brodmann_area_25 (the other empty-SYSTEM entry)
-------------------------------------------------------------
Both brodmann_area_25 and brodmann_area_33 have `SYSTEM == []` and no
config. They are NOT the same kind of entry:

    brodmann_area_25    CROSS-LOBE POINTER. Compute exists; it lives
                        in cingulate/subgenual_area_25/. This file
                        documents the anatomical boundary and points
                        at the real compute package.

    brodmann_area_33    TREE ARTIFACT. Compute does not exist
                        anywhere. This file documents the anatomical
                        vestige and points at nothing.

Both entries set `SYSTEM == []` because both are non-compute from the
frontal tree's perspective; the difference is whether there's a real
compute package at the other end of the reference. Consumer code that
iterates the registry can skip both with the same `if not entry.SYSTEM`
check, but the *reason* to skip differs, and the docstrings make that
difference explicit so that a future contributor investigating either
entry knows which kind of non-compute they're looking at.

IDENTITY
--------
    AREA_ID    = 33
    NAME       = "Brodmann area 33"
    SYSTEM     = []           # empty — no compute exists anywhere
    SUB_REGION = None         # no sub-region owns it
    LOBE       = "frontal (tree artifact; anatomically cingulate)"
    SIDE       = "left"
    GROUPING   = None

ANATOMY
-------
    ANATOMY = {
        "name": "Brodmann area 33",
        "system": None,
        "sub_region": None,
        "grouping": None,
        "location": "a thin strip of cortex just above the rostrum of "
                    "the corpus callosum, transitional between the "
                    "agranular anterior cingulate (area 24) and the "
                    "rudimentary cortex of the callosal sulcus; "
                    "anatomically a cingulate area",
        "cytoarchitecture": "transitional cortex; a blend of the "
                            "agranular layer pattern of area 24 and "
                            "the less-developed lamination of the "
                            "callosal cortex. Sometimes subdivided "
                            "into 33a and 33b by degree of "
                            "differentiation.",
        "compute_location": None,
        "compute_summary": None,
        "notes": (
            "Brodmann area 33 is a small transitional cingulate area "
            "with no well-characterized independent function in the "
            "mature brain. Its connectivity overlaps largely with the "
            "adjacent area 24 and area 32 (which are the ACC's actual "
            "compute nodes in this project), and no behavioural "
            "syndrome or selective task activation is reliably "
            "associated with it. The model therefore carries it as a "
            "registry annotation with no compute: `SYSTEM == []` and "
            "no config. Its placement in the frontal tree is a "
            "historical filing artifact — anatomically it belongs to "
            "the cingulate, and if the tree is ever renormalised it "
            "moves to cingulate/brodmann_areas/. Until then, this "
            "entry documents the intended ownership and explains why "
            "there is no LEFT_CONFIG: there is no function to "
            "configure. See the contrast note in this file's docstring "
            "between this entry and brodmann_area_25/ (the cross-lobe "
            "pointer) — they share an empty SYSTEM but for different "
            "reasons."
        ),
    }

CONFIG
------
There is NO config. There is no `LEFT_CONFIG`, no `RIGHT_CONFIG`, no
per-system block, no `sub_region` field. Area 33 has no function in
this model that any compute sub-region would read config for. If you
are looking for area 33's config in this file and not finding it, this
paragraph is why. It is not an oversight — it is the model's position
that area 33 has no independent function to configure.

EXPORTS
-------
    from .brodmann_area_33 import BRODMANN_33     # int, == AREA_ID (33)
    from .brodmann_area_33 import ANATOMY
    from .brodmann_area_33 import SYSTEM          # [] — empty
    from .brodmann_area_33 import SUB_REGION      # None
    from .brodmann_area_33 import GROUPING        # None

That is the entire public surface. There is no config, no compute, no
class, no function.

Consumers should use the flat re-export path
(`from ...brodmann_areas import BRODMANN_33`) — area 33 is a direct child
of brodmann_areas/, not nested. Registry-iteration code that wants to
skip this entry should check `if not entry.SYSTEM: continue` with a
comment pointing at this file — the "documented skip, not silent skip"
rule from the parent registry's contract. Note that the same check also
skips brodmann_area_25 (the cross-lobe pointer), which is correct;
the difference between them is documentary, not behavioural.

CROSS-MIDLINE RULE
------------------
This package has no state, no compute, and nothing to compute. The
standard "no cross-midline state bleed" rule is trivially satisfied
because there is nothing to bleed. The rule that *does* apply is
**structural consistency**: this package must be structurally identical
to the right hemisphere's brodmann_area_33 package — same AREA_ID, empty
SYSTEM, same SUB_REGION/GROUPING (None/None), same ANATOMY field set
and content (except SIDE). Both are documenting the same anatomical
vestige and the same tree-placement artifact; if they diverge in
structure, that is a bug.

WHERE IT WOULD GO IF THE TREE IS NORMALISED
-------------------------------------------
If the frontal tree is ever renormalised, area 33's registry entry
moves from `frontal/brodmann_areas/brodmann_area_33/` to
`cingulate/brodmann_areas/brodmann_area_33/`. That move would:

    - put area 33 under the tree that anatomically owns it;
    - leave the frontal registry with only areas 4, 6, 8, 9, 10, 11,
      12, 25 (pointer), 44, 45, 46, 47 — the actually-frontal set;
    - not change any compute, because area 33 has none to move.

If the tree is never normalised, this file's documentation of the
intended ownership remains the operative record. Either way, the
absence of config and compute is correct: area 33 has no independent
function in the model, and this file is honest about that.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define `encode()`, `step()`, or any stateful object.
    - Must not gain a `LEFT_CONFIG`, `RIGHT_CONFIG`, or any config
      whatsoever. The absence of config is the point. A future
      contributor tempted to add one — e.g. "let's model area 33 as a
      small ACC-like node" — is signaling that the model needs a new
      compute sub-module, not that this registry entry needs a
      config. That's a much larger decision (with architectural
      consequences: a new compute sub-module in the cingulate tree)
      and it should be treated as such, not smuggled in as a config
      field.
    - Must not import any compute package (including cingulate's ACC
      packages, to which area 33 is anatomically adjacent). The
      adjacency is documentary, not computational.
    - Must not be imported by any compute package. Area 33 has no
      contribution to any compute sub-module's encode().
    - Must not acquire `compute_location` or `compute_summary` fields
      in ANATOMY. Those fields exist on brodmann_area_25 to point at
      a real compute package; here they would falsely imply that a
      compute package exists. Their absence is deliberate and
      distinguishes the two empty-SYSTEM entries at the ANATOMY level
      as well as the docstring level.
    - Must not diverge in structure from the right hemisphere's
      brodmann_area_33 package — same AREA_ID, empty SYSTEM, same
      SUB_REGION/GROUPING (None/None), same ANATOMY field set and
      content (except SIDE). The two are documenting the same
      anatomical artifact and the same intended (cingulate) ownership;
      if they diverge, that's a bug.
    - Must not be "fixed" by adding a token config or a nominal
      SYSTEM value in order to make the registry look more uniform.
      The empty SYSTEM is the load-bearing signal that this entry has
      no compute; filling it in would break the consumer-side skip
      logic and obscure the artifact.
"""