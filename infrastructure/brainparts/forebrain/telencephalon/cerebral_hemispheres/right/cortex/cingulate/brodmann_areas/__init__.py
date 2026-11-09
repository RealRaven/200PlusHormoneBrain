"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.cingulate.brodmann_areas
========================================================================================================

The BRODMANN AREA REGISTRY for the left cingulate cortex.

Mirror of the right cingulate Brodmann registry. This package is NOT a runtime
compute node. It has no `encode()`, no `step()`, and no state of its own. It is
a *reference namespace*: the single canonical place where the Brodmann numbers
that make up the cingulate are declared, annotated, and given per-hemisphere
configuration values. The three functional sub-modules of the cingulate —
`anterior_cingulate/`, `posterior_cingulate/`, `retrosplenial_cortex/` —
import their area constants and per-area weights from here rather than
defining them locally.

The reason this is a sibling of the sub-modules, not a child of any one of
them, is that the Brodmann numbering cuts across the functional divisions.
The cingulate's three functional systems use seven areas, and the areas do
not map one-to-one onto the systems. A registry that lived inside any single
sub-module would be mis-scoped.

WHAT LIVES HERE
---------------
Each `brodmann_area_XX/` sub-package is a thin constant + config holder:

    brodmann_area_23/              PCC      contextual/self-referential
    brodmann_area_24/              ACC      dorsal cognitive (conflict)
    brodmann_area_26_retrosplenial/ RSC     spatial context
    brodmann_area_29_retrosplenial/ RSC     spatial context
    brodmann_area_30_retrosplenial/ RSC     spatial context
    brodmann_area_31/              PCC      contextual/self-referential
    brodmann_area_32/              ACC      dorsal cognitive (error/control)

Each exposes, at minimum:

    AREA_ID          int, the canonical Brodmann number
    SYSTEM           which functional sub-module owns it
                     (one of "anterior_cingulate", "posterior_cingulate",
                     "retrosplenial_cortex")
    LEFT_CONFIG      per-area weights used by the owning sub-module's encode()
                     (e.g. feature weights, laminar priors, connectivity
                     weights); mirrors RIGHT_CONFIG with complementary values
    ANATOMY          metadata: name, approximate location, notes

These are constants and plain dicts, not classes. A Brodmann area is a
reference label, not an agent — it has no lifecycle. The thing that computes
is the sub-module; the thing that gets labelled is the area.

MAPPING TO THE FUNCTIONAL SUB-MODULES
-------------------------------------
    anterior_cingulate/     imports BRODMANN_24, BRODMANN_32
                            (and references area 25, see note below)
    posterior_cingulate/    imports BRODMANN_23, BRODMANN_31
    retrosplenial_cortex/   imports BRODMANN_26, BRODMANN_29, BRODMANN_30

The import direction is one-way: sub-modules import from this registry, this
registry imports from nothing except the chemicals/hormones config layer (for
per-area hormone receptor metadata). It must not import the sub-modules — that
would create a cycle.

A NOTE ON `subgenual_area_25/`
------------------------------
The tree places `subgenual_area_25/` as a sibling of this registry at the
`cingulate/` level, not inside `brodmann_areas/`. That is a deliberate
exception, not an oversight:

    Area 25 is the only cingulate area whose functional role is
    distinctive enough to warrant its own package — its involvement in
    treatment-resistant depression, autonomic regulation, and DBS response
    is well-documented, and it is expected to hold its own state (affective
    set-point, treatment-response parameters) as the project develops.

It is therefore documented as belonging to the `anterior_cingulate/` family
(it is the affective division of the ACC) but living as a sibling of this
registry. Cross-references should point to `cingulate/subgenual_area_25/`, not
`cingulate/brodmann_areas/brodmann_area_25/`. If a future refactor unifies
the two layouts, that refactor should move `subgenual_area_25/` *into* this
registry and update the importing sub-module — until then, the split is the
documented state.

LEFT-HEMISPHERE CONFIG NOTE
---------------------------
The area IDs and anatomical metadata are identical on the left and right.
Only `LEFT_CONFIG` differs from `RIGHT_CONFIG` — and only by weight, never by
capability, consistent with the lateralisation rule applied everywhere else
in this project. On the left, the per-area weights lean toward the left ACC's
lexical/verbal conflict weighting, the left PCC's verbal/autobiographical
context weighting, and the left RSC's mildly lower heading/layout weighting
(compared with the right). The left cingulate's functional sub-modules import
their weights from this registry's `LEFT_CONFIG` blocks; a mirror-assertion
test should confirm that every `brodmann_area_XX.LEFT_CONFIG` mirrors the
corresponding `RIGHT_CONFIG` key-for-key, with complementary values.


Programming contract for this package
-------------------------------------
- This __init__.py does no computation. It re-exports the area constants
  (e.g. `from .brodmann_area_24 import BRODMANN_24`) so that consumers write
  `from ...cingulate.brodmann_areas import BRODMANN_24`, not a deep path.
- Each `brodmann_area_XX/__init__.py` contains only constants, dicts, and
  docstring. No classes, no functions beyond optional trivial accessors.
- This registry must never import the functional sub-modules. Any upward
  import is a layering bug.
- Adding a new area is a data operation: create `brodmann_area_XX/`, add the
  constants and config blocks, re-export from the parent. No changes to the
  compute layer unless the new area belongs to a new functional sub-module.
- The mirror-assertion test for `LEFT_CONFIG` vs. `RIGHT_CONFIG` lives with
  the config-validation tests, not inside this package. Because registries on
  both sides share the same area IDs and anatomy, the test can be a single
  parametrised check over both hemispheres.
- If a Brodmann area ever genuinely needs its own state (rather than just
  config values), it is promoted out of this registry into its own package
  at the `cingulate/` level — exactly as `subgenual_area_25/` already is. Do
  not give a registry entry a lifecycle.
- The registry content should be *identical in structure* to the right
  hemisphere's registry; only the `*_CONFIG` values differ. If the two
  registries ever diverge in keys or area list, that is a bug.
"""