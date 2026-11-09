"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas
======================================================================================================

The BRODMANN AREA REGISTRY for the right frontal cortex.

Mirror of the left frontal Brodmann registry. NOT a runtime compute node. No
encode(), no step(), no state. This is a reference namespace: the canonical
place where the Brodmann numbers that make up the frontal lobe are declared,
annotated, and given per-hemisphere configuration values. The four compute
sub-regions of the frontal cortex (`prefrontal_cortex/`, `premotor_cortex/`,
`primary_motor_cortex/`, `supplementary_motor_cortex/`) import their area
constants and per-area weights from here rather than defining them locally.

WHERE IT DIFFERS FROM THE CINGULATE REGISTRY
--------------------------------------------
Inherited unchanged from the left frontal registry; see
`.../left/cortex/frontal/brodmann_areas/__init__.py` for the full rationale.
In short, three structural differences:

    1. NESTED SUB-PACKAGE. `brocas_area/` contains brodmann_area_44/ and
       brodmann_area_45/, grouping the two coupled Brodmann areas that
       together implement language production.
    2. MULTI-SYSTEM MAPPING. Several areas belong to more than one
       compute sub-region (6: premotor + SMA; 8: premotor + prefrontal;
       47: OFC + VLPFC). SYSTEM is a list, not a string.
    3. ENTRIES THAT ARE NOT FRONTAL AREAS. brodmann_area_25/ is a
       cross-lobe pointer (compute in `cingulate/subgenual_area_25/`) and
       brodmann_area_33/ is a tree artifact (a cingulate area living under
       the frontal tree). Both are documented below and both have
       `SYSTEM == []`.

WHAT LIVES HERE
---------------
Twelve directory entries, containing thirteen Brodmann areas. Identical to
the left's list — the areas themselves are bilateral, only their weights
differ:

    brocas_area/                          (sub-package; two areas inside)
        brodmann_area_44/                 VLPFC  — pars opercularis
        brodmann_area_45/                 VLPFC  — pars triangularis
    brodmann_area_4/                      primary motor
    brodmann_area_6/                      premotor + supplementary motor
    brodmann_area_8/                      premotor (FEF) + prefrontal (DMPFC)
    brodmann_area_9/                      prefrontal (DLPFC + DMPFC)
    brodmann_area_10/                     prefrontal (VMPFC, rostral)
    brodmann_area_11/                     prefrontal (OFC)
    brodmann_area_12/                     prefrontal (OFC)
    brodmann_area_25/                     CROSS-LOBE — see below
    brodmann_area_33/                     TREE ARTIFACT — see below
    brodmann_area_46/                     prefrontal (DLPFC)
    brodmann_area_47/                     prefrontal (OFC + VLPFC)

Each `brodmann_area_XX/` sub-package is a thin constant + config holder
exposing, at minimum:

    AREA_ID          int, the canonical Brodmann number
    SYSTEM           list[str], which compute sub-region(s) own it
                     (values drawn from {"prefrontal_cortex",
                     "premotor_cortex", "primary_motor_cortex",
                     "supplementary_motor_cortex"}); empty list for
                     cross-lobe pointers and tree artifacts
    RIGHT_CONFIG     per-area weights used by the owning sub-region's
                     encode(); mirrors LEFT_CONFIG (directionally, for
                     the lateralised frontal weights)
    ANATOMY          metadata: name, location, notes

These are constants and plain dicts, not classes. A Brodmann area is a
reference label, not an agent — it has no lifecycle. The thing that
computes is the sub-region; the thing that gets labelled is the area.

SYSTEM MAPPING (identical to the left's)
----------------------------------------
    prefrontal_cortex             areas 8 (dorsomedial), 9, 10, 11, 12,
                                  44, 45, 46, 47
    premotor_cortex               areas 6 (lateral), 8 (frontal eye
                                  fields)
    primary_motor_cortex          area 4
    supplementary_motor_cortex    area 6 (medial)

Three areas appear in more than one system:
    area 6      premotor (lateral PMd/PMv) + supplementary motor (medial
                SMA/pre-SMA)
    area 8      premotor (FEF, lateral) + prefrontal (DMPFC, medial)
    area 47     prefrontal (both OFC and VLPFC subdivisions)

For the shared areas, the per-area RIGHT_CONFIG contains *per-system*
weights — e.g. area 6's config has a "premotor" block and a
"supplementary_motor" block, and each sub-region reads its own block.
This is documented in each shared area's individual file. The registry
itself does not arbitrate between the systems.

BROCAS_AREA
-----------
`brocas_area/` is a sub-package containing brodmann_area_44/ and
brodmann_area_45/. On the right, Broca's area still exists as a
Brodmann-area label, but its language-production compute is heavily
left-lateralised — the right Broca's area contributes prosody,
emotional tone, and non-lexical speech features, and its lexical
production weight is minimal. The nesting and the re-export pattern are
identical to the left's; only the weight profile inside each area's
RIGHT_CONFIG differs.

CROSS-LOBE ENTRY: brodmann_area_25
----------------------------------
The directory `brodmann_area_25/` exists under
right/frontal/brodmann_areas/ for the same anatomical reason as on the
left: Brodmann 25 (subgenual ACC) sits at the frontal/cingulate boundary
and appears in both trees. BUT:

    The COMPUTE for area 25 lives in the RIGHT hemisphere's
    `cingulate/subgenual_area_25/`. The entry here is a registry
    annotation and a documented cross-reference.

    Code that needs area 25's affect computation imports from the RIGHT
    cingulate package, not the left and not this one. Code that needs
    area 25's anatomical metadata imports from here.

    SYSTEM is an empty list. There is no RIGHT_CONFIG for a frontal
    compute that does not exist; the entry's only runtime content is
    ANATOMY metadata that cross-references the cingulate package.

TREE ARTIFACT: brodmann_area_33
-------------------------------
The directory `brodmann_area_33/` exists under
right/frontal/brodmann_areas/ but area 33 is anatomically part of the
cingulate. It is in the frontal tree for the same reason as on the
left; it should be understood as a cingulate area for ownership
purposes.

    The COMPUTE for area 33 — such as it is; area 33 is a tiny
    transitional area — would live in the cingulate package if it were
    ever instantiated. It is not instantiated as a compute node.

    SYSTEM is an empty list. There is no RIGHT_CONFIG. If the tree is
    ever normalised, brodmann_area_33/ moves to
    `cingulate/brodmann_areas/brodmann_area_33/`; until then, this
    entry documents the intended ownership.

ANATOMY vs. COMPUTE (the parent-level note)
-------------------------------------------
Same layering as the left: compute sub-regions import FROM this
registry; this registry imports from NOTHING except the chemicals/
hormones config layer; importing a compute sub-region from this
registry would create a cycle.

RIGHT-HEMISPHERE CONFIG NOTE
----------------------------
The area IDs and anatomical metadata are identical across hemispheres.
Only RIGHT_CONFIG differs from LEFT_CONFIG — and, as on the left, the
difference is DIRECTIONAL rather than complementary:

    - Broca's area (44/45): right has minimal lexical weight, larger
      prosodic/affective weight; the left has the opposite profile. The
      two are not two halves of one budget — the right's Broca's area is
      not "the left's Broca's area at 10% weight", it is a functionally
      different contributor (prosody vs lexicon).
    - Dorsolateral prefrontal: right-weighted spatial WM,
      left-weighted verbal WM — directional, not complementary.
    - OFC (11/12): right-weighted negative-valence/threat,
      left-weighted positive-valence/approach — directional, not
      complementary.
    - Motor areas: right-weighted gross/proximal, left-weighted fine/
      distal — directional, not complementary.
    - Supplementary motor: right-weighted spatial/bimanual sequence
      planning, left-weighted language-articulatory sequences.

The mirror-assertion test for this registry is therefore the same
DIRECTIONAL check per lateralised key that the left's registry
specifies, just evaluated in the opposite direction. For structural
keys (anatomy, area IDs), the check is equality. For shared areas
(6, 8, 47), the per-system blocks are checked independently.

The cross-lobe and tree-artifact entries (25, 33) have NO config on
either side; their mirror check is "both are empty", asserted so a
future change adding config to them fails the test.

CROSS-MIDLINE RULE
------------------
This registry must never import or reference the left hemisphere's
frontal Brodmann registry. The two registries have identical structure
and identical area IDs by design, and the config-mirror test enforces
that relationship, but the relationship is asserted by the test suite,
not by runtime import. A runtime cross-reference between the two
registries would create the exact kind of direct mid-line state
sharing that the commissures exist to prevent — and would also make
the mirror test circular (each registry would be checking itself
against the other at import time rather than being independently
validated).


Programming contract for this package
-------------------------------------
- This __init__.py does no computation. It re-exports the area constants
  (e.g. `from .brodmann_area_4 import BRODMANN_4` and
  `from .brocas_area.brodmann_area_44 import BRODMANN_44`) so that
  consumers write flat imports against this package. Identical pattern
  to the left's registry.
- Each `brodmann_area_XX/__init__.py` contains only constants, dicts,
  and docstring. No classes, no functions beyond optional trivial
  accessors.
- `brocas_area/__init__.py` is itself a nested registry parent; it
  re-exports its two areas the same way this package does.
- The `SYSTEM` field is a list. Consumers must handle the list (assert
  len==1, or iterate, or check membership). On the right this matters
  for exactly the same three shared areas as on the left (6, 8, 47),
  plus the two empty-SYSTEM entries (25, 33).
- The empty-SYSTEM entries (25, 33) are first-class members of the
  registry with `SYSTEM == []`. Consumer code must handle them
  explicitly, with a documented skip rather than a silent one, for the
  same reason as on the left: future additions should be reviewed.
- This registry must never import a compute sub-region. Any upward
  import is a layering bug.
- This registry must never import or reference the left hemisphere's
  frontal Brodmann registry. The relationship between the two is
  validated by the test suite, not by runtime import. Direct
  cross-midline registry access is a bug — the commissures exist
  precisely to prevent this kind of direct mid-line coupling.
- The mirror-assertion test for RIGHT_CONFIG vs LEFT_CONFIG is
  directional for lateralised keys and equal for structural keys. The
  cross-lobe and tree-artifact entries assert "both empty".
- If a Brodmann area ever genuinely needs its own state (rather than
  just config values), it is promoted out of this registry into its own
  package at the `frontal/` level — the way `subgenual_area_25` is
  promoted in the cingulate. Do not give a registry entry a lifecycle.
- The right registry's structure (list of area IDs, SYSTEM values,
  anatomy) must be identical to the left's. If the two registries ever
  diverge in area list or system mapping, that is a bug — the areas
  are bilateral; only the weights differ. A structural-equality test
  should assert this alongside the directional-weight test.
"""