"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brodmann_area_33
=======================================================================================================================

Brodmann area 33 — right hemisphere — TREE ARTIFACT.

Mirror of the left brodmann_area_33 package. THIS IS NOT A COMPUTE NODE.
It has no RIGHT_CONFIG, no encode(), no state. It is not a cross-lobe
pointer either: there is no compute package anywhere in the project that
this entry refers to. `SYSTEM` is the empty list; the package exports
exactly three fields (BRODMANN_33, ANATOMY, SYSTEM) plus two structural
None fields (SUB_REGION, GROUPING) for registry-shape consistency, and
nothing else.

Why the empty SYSTEM: because there is no function to route it to. Area
33 has no independent cognitive function in the model, no compute
package that would want to read its config, and no realistic prospect of
acquiring one. This is the same on both hemispheres — the artifact is a
tree-placement decision, and tree-placement decisions do not lateralise.

WHY IT IS IN THE FRONTAL TREE AT ALL
------------------------------------
The placement and the reason are identical to the left's; see
`.../left/cortex/frontal/brodmann_areas/brodmann_area_33/__init__.py`
for the full rationale. In brief:

    Area 33 is anatomically a small, transitional cingulate area — the
    "precallosal" or "callosal" area, a thin strip of cortex just above
    the rostrum of the corpus callosum, transitional between the
    agranular anterior cingulate (area 24) and the less-developed
    cortex of the callosal sulcus. It is properly a cingulate area.

    The tree nonetheless places brodmann_area_33/ under the frontal
    tree. That placement is a historical filing decision, not an
    anatomical claim, and it is the same on both hemispheres.

This entry documents the artifact honestly rather than pretending the
placement is meaningful, for the same two narrow reasons as on the left:

    1. REGISTRY COMPLETENESS. A registry that lists the Brodmann areas
       of the right frontal lobe should have an explicit entry for
       every area that appears in the tree, even the ones that
       shouldn't be there.
    2. PRE-EMPTING CONFUSION. A future contributor who notices
       brodmann_area_33/ in the right frontal tree and wonders "what
       does area 33 compute?" will find a clear answer here: nothing,
       and the placement is an artifact.

WHAT AREA 33 IS (and why it has no compute)
-------------------------------------------
Identical to the left's description: a small transitional area with no
well-characterized independent function in the mature brain, whose
connectivity overlaps largely with adjacent area 24 and area 32. No
behavioural syndrome is reliably associated with selective area-33
lesions, and no well-replicated task activates it selectively. The
model's position is the same on both hemispheres: area 33 has no
compute because there is no function to compute.

CONTRAST WITH brodmann_area_25 (the other empty-SYSTEM entry)
-------------------------------------------------------------
On the right, the contrast is exactly as on the left:

    brodmann_area_25    CROSS-LOBE POINTER. Compute exists; it lives
                        in the RIGHT cingulate/subgenual_area_25/.
                        This file documents the anatomical boundary
                        and points at the real compute package.
                        ANATOMY has compute_location and
                        compute_summary populated.

    brodmann_area_33    TREE ARTIFACT. Compute does not exist
                        anywhere. This file documents the anatomical
                        vestige and points at nothing. ANATOMY has
                        compute_location and compute_summary set to
                        None.

Both set `SYSTEM == []`; consumer code skips both with the same
`if not entry.SYSTEM: continue` check. The *reason* to skip differs,
and the docstrings make that difference explicit so that a future
contributor investigating either entry knows which kind of non-compute
they're looking at.

IDENTITY
--------
    AREA_ID    = 33
    NAME       = "Brodmann area 33"
    SYSTEM     = []           # empty — no compute exists anywhere
    SUB_REGION = None         # no sub-region owns it
    LOBE       = "frontal (tree artifact; anatomically cingulate)"
    SIDE       = "right"
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
            "compute nodes in this project). The model therefore "
            "carries it as a registry annotation with no compute: "
            "`SYSTEM == []` and no config. The anatomical structure "
            "and the tree-placement artifact are identical on both "
            "hemispheres; only SIDE differs between the two pointer "
            "packages. If the tree is ever renormalised, this entry "
            "moves to the right cingulate/brodmann_areas/. Until then, "
            "this entry documents the intended ownership and explains "
            "why there is no RIGHT_CONFIG: there is no function to "
            "configure. See the contrast note in this file's docstring "
            "between this entry and brodmann_area_25/ (the cross-lobe "
            "pointer) — they share an empty SYSTEM but for different "
            "reasons."
        ),
    }

    Anatomy is identical to the left's except for the SIDE field and
    the minor wording in `notes` that references the right hemisphere's
    target package for any future renormalisation. The structure, the
    absence of config, and the presence of `compute_location: None` /
    `compute_summary: None` are the same on both sides — there is
    nothing here to lateralise.

CONFIG
------
There is NO config. There is no `LEFT_CONFIG`, no `RIGHT_CONFIG`, no
per-system block. Area 33 has no function in this model that any
compute sub-region would read config for. If you are looking for area
33's config in this file and not finding it, this paragraph is why. It
is not an oversight — it is the model's position that area 33 has no
independent function to configure, on either hemisphere.

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
(`from ...brodmann_areas import BRODMANN_33`) — area 33 is a direct
child of brodmann_areas/, not nested. Registry-iteration code that
wants to skip this entry should check `if not entry.SYSTEM: continue`
with a comment pointing at this file — the "documented skip, not silent
skip" rule from the parent registry's contract. The same check also
skips brodmann_area_25 (the cross-lobe pointer), which is correct; the
difference between them is documentary, not behavioural.

CROSS-MIDLINE RULE
------------------
This package has no state, no compute, and nothing to compute. The
standard "no cross-midline state bleed" rule is trivially satisfied
because there is nothing to bleed. The rule that *does* apply is
**structural consistency**: this package must be structurally identical
to the LEFT hemisphere's brodmann_area_33 package — same AREA_ID, empty
SYSTEM, same SUB_REGION/GROUPING (None/None), same ANATOMY field set
and content (except SIDE and the minor right-reference wording in
`notes`). Both are documenting the same anatomical vestige and the same
tree-placement artifact; if they diverge in structure, that is a bug.

WHERE IT WOULD GO IF THE TREE IS NORMALISED
-------------------------------------------
If the right frontal tree is ever renormalised, this registry entry
moves from `right/frontal/brodmann_areas/brodmann_area_33/` to
`right/cingulate/brodmann_areas/brodmann_area_33/`. That move would:

    - put area 33 under the tree that anatomically owns it;
    - leave the right frontal registry with only areas 4, 6, 8, 9,
      10, 11, 12, 25 (pointer), 44, 45, 46, 47 — the actually-frontal
      set;
    - not change any compute, because area 33 has none to move.

The left and right moves would be symmetric and independent; neither
requires the other to have happened first. If the tree is never
normalised, this file's documentation of the intended ownership remains
the operative record.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define `encode()`, `step()`, or any stateful object.
    - Must not gain a `LEFT_CONFIG`, `RIGHT_CONFIG`, or any config
      whatsoever. The absence of config is the point. A future
      contributor tempted to add one is signaling that the model needs
      a new compute sub-module (a new cingulate sub-region for
      area-33-like transition-zone function), not that this registry
      entry needs a config.
    - Must not import any compute package (including the right
      cingulate's ACC packages, to which area 33 is anatomically
      adjacent). The adjacency is documentary, not computational.
    - Must not be imported by any compute package. Area 33 has no
      contribution to any compute sub-module's encode().
    - Must not acquire `compute_location` or `compute_summary` values.
      Those fields exist on brodmann_area_25 to point at a real
      compute package; here they are set to None to record that no
      compute package exists. Populating them would falsely imply a
      compute package exists.
    - Must not import or reference the left hemisphere's
      brodmann_area_33 package. The two pointer packages are
      structurally identical by design, and that identity is asserted
      by the test suite, not by runtime import. Cross-midline registry
      access is a bug, even for non-compute entries — the practice of
      cross-midline import is what the rule guards against, and an
      exception for "harmless" pointers would erode it.
    - Must not diverge in structure from the left hemisphere's
      brodmann_area_33 package — same AREA_ID, empty SYSTEM, same
      SUB_REGION/GROUPING (None/None), same ANATOMY field set and
      content (except SIDE and the minor right-reference wording). The
      two are documenting the same artifact; if they diverge in
      structure, that's a bug.
    - Must not be "fixed" by adding a token config or a nominal
      SYSTEM value in order to make the registry look more uniform.
      The empty SYSTEM is the load-bearing signal that this entry has
      no compute; filling it in would break the consumer-side skip
      logic and obscure the artifact.
"""