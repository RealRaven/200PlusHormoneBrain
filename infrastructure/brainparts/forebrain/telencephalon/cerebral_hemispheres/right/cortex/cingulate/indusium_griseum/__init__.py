"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.cingulate.indusium_griseum
============================================================================================================

The INDUSIUM GRISEUM — right hemisphere.

Mirror of the left indusium griseum package. A PURE ANATOMICAL ANNOTATION
NAMESPACE. This package contains:
  - no compute (no encode(), no step())
  - no state
  - no configuration (no RIGHT_CONFIG, no SYSTEM)
  - no imports from or to any sub-module

It exists solely so that the anatomical structure has a canonical address in
the tree — for cross-references in docstrings, for per-region metadata that
the chemicals/hormones config layer may cite, and because the anatomical
reality is there and silently omitting it would be a lie about the brain. It
is not intended to gain compute, config, or state as the project develops.

If you are looking for the cingulate's functional computation, the three
sub-modules are `anterior_cingulate/`, `posterior_cingulate/`, and
`retrosplenial_cortex/`. If you are looking for the cingulate's seven
Brodmann areas, they are in `brodmann_areas/`. This package is neither.

WHAT IT IS
----------
    ANATOMY = {
        "name": "Indusium griseum",
        "kind": "anatomical vestige (non-compute)",
        "system": None,                 # not a functional sub-module
        "brodmann": None,               # not a Brodmann area
        "location": "thin layer of grey matter covering the dorsal "
                    "surface of the corpus callosum, extending from the "
                    "septum pellucidum rostrally to the splenium caudally",
        "cytoarchitecture": "rudimentary cortex-like layer, "
                            "cytoarchitecturally continuous with the "
                            "hippocampal formation",
        "notes": (
            "A thin sheet of grey matter that sits on the dorsal surface "
            "of the corpus callosum. It is a vestigial remnant of the "
            "hippocampal formation — ontogenetically a continuation of "
            "the hippocampus that gets stretched across the callosum as "
            "the hemispheres rotate during development. Its "
            "cytoarchitecture is hippocampus-like rather than cortical, "
            "and it is grouped with the hippocampal formation (along "
            "with the taenia tecta, the fimbria, and the longitudinal "
            "striae) rather than with the cingulate proper. It is not a "
            "Brodmann area and is not a member of any of the ACC, PCC, "
            "or RSC functional sub-modules. It has no known independent "
            "cognitive function in the mature brain; it is occasionally "
            "noted as a pathway for seizure spread and as a source of "
            "adult neural stem cells, but neither role is load-bearing "
            "for the model. It is documented here for anatomical "
            "completeness and because its presence in the tree is "
            "expected — it is simply not a compute node."
        ),
    }

    Anatomy is identical to the left. The structure is bilateral and
    symmetric; there is no documented right-side anatomical difference
    for the indusium griseum. The `notes` field is repeated verbatim
    rather than referenced, so that this file stands on its own for a
    reader who only sees the right hemisphere.

RELATED STRUCTURES (for cross-reference, not definition)
--------------------------------------------------------
The indusium griseum is part of the broader hippocampal formation, along
with:
    - taenia tecta (the rostral continuation of the same strip)
    - longitudinal striae (fibre bundles running along the indusium's
      surface — grey matter's white-matter escort)
    - fimbria and fornix (the efferent tract of the hippocampus)
In the model, those structures are not instantiated as separate packages
either, for the same reason: they are anatomical scaffolding, not compute.
The hippocampal compute itself lives in `medial_temporal_lobe/hippocampus/`
under the right hemisphere's `subcortical/` tree, not here.

WHY IT LIVES AT `cingulate/` LEVEL
----------------------------------
It would be tempting to file this under `brodmann_areas/` (as a
non-numbered area) or under `anterior_cingulate/` (as a limbic-associated
node). Both would be wrong:

    - It is not a Brodmann area — Brodmann did not number it, and it
      does not belong in a registry whose contract is "one entry per
      Brodmann number."
    - It is not a member of any functional sub-module — it is not an
      ACC, PCC, or RSC structure, and adding it under any of them
      would falsely attribute function it does not have.

It is a sibling of the functional sub-modules because that is the only
level at which "cingulate-associated structure with no functional role
in the model" is a coherent description. This is the documented exception
to the "everything under cingulate/ is either a sub-module or a registry
entry" pattern, and it is the third category: anatomical annotation.

CROSS-MIDLINE RULE
------------------
No import or reference to the left hemisphere's indusium griseum package.
Because this package has no compute and no config, the ordinary reason for
the rule (avoid state bleed between hemispheres) does not apply; the rule
is repeated here for structural consistency. If a future change ever gives
this package runtime behaviour, the standard rule applies in full: any
cross-midline exchange goes through `telencephalon/commissures/`, never
through direct access.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not gain a `LEFT_CONFIG`, `RIGHT_CONFIG`, or `SYSTEM` key.
      The absence of configuration is the point: if a future change
      wants to give the indusium griseum behaviour, that is a signal
      that the anatomical reality has been misunderstood, not that the
      config needs extending.
    - Must not import from any sub-module or from `brodmann_areas/`.
    - Must not be imported by any sub-module or by `brodmann_areas/`.
      It may be referenced by docstrings (as it is here), but not by
      runtime code.
    - Must not be promoted to a runtime package without a documented
      functional justification in the project's architecture notes.
      "It's in the tree" is not a reason; "it demonstrably computes X"
      is.
    - Must not diverge in structure from the left hemisphere's indusium
      griseum package — same ANATOMY, same (absent) config; only SIDE
      differs.

SIDE
----
    SIDE = "right"

EXPORTS
-------
    from .indusium_griseum import ANATOMY    # dict, as above
    from .indusium_griseum import SIDE       # str, "right"

That is the entire public surface. There is no config, no computation, and
no sub-module contract to satisfy.
"""