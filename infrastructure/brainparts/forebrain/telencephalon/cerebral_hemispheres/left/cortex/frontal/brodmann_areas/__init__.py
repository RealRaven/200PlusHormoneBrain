"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas
=====================================================================================================

The BRODMANN AREA REGISTRY for the left frontal cortex.

NOT a runtime compute node. No encode(), no step(), no state. This is a
reference namespace: the canonical place where the Brodmann numbers that
make up the frontal lobe are declared, annotated, and given per-hemisphere
configuration values. The four compute sub-regions of the frontal cortex
(`prefrontal_cortex/`, `premotor_cortex/`, `primary_motor_cortex/`,
`supplementary_motor_cortex/`) import their area constants and per-area
weights from here rather than defining them locally.

WHERE IT DIFFERS FROM THE CINGULATE REGISTRY
--------------------------------------------
Three structural differences, each with a documented reason:

    1. NESTED SUB-PACKAGE. The cingulate registry is a flat list of
       brodmann_area_XX/ directories. The frontal registry has one nested
       sub-package, `brocas_area/`, containing brodmann_area_44/ and
       brodmann_area_45/. Broca's area is a tree-visible functional
       grouping of two Brodmann areas, and the nesting makes the
       coupling explicit in the import path. See the BROCAS_AREA section.

    2. MULTI-SYSTEM MAPPING. In the cingulate, each area maps to exactly
       one functional sub-module (ACC, PCC, or RSC). In the frontal lobe,
       several areas belong to more than one compute sub-region — area 6
       spans premotor and supplementary motor, area 8 spans premotor and
       prefrontal (dorsomedial), and area 47 spans orbitofrontal and
       ventrolateral prefrontal. Each area file's SYSTEM field is a
       list of systems, not a single string, and the compute sub-regions
       import from the intersection of their own system and the areas
       that cite them. See the SYSTEM MAPPING section.

    3. ENTRIES THAT ARE NOT FRONTAL AREAS. Two entries in this directory
       are not frontal compute areas at all — brodmann_area_25/ is a
       cross-lobe pointer (the subgenual ACC's compute lives in
       `cingulate/subgenual_area_25/`) and brodmann_area_33/ is a tree
       artifact (a cingulate area living under the frontal tree). Both
       are documented in detail below. They exist in the tree for
       anatomical completeness, not because the frontal lobe computes
       them.

WHAT LIVES HERE
---------------
Twelve directory entries, containing thirteen Brodmann areas:

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
    LEFT_CONFIG      per-area weights used by the owning sub-region's
                     encode(); mirrors RIGHT_CONFIG with complementary
                     values (or directionally-biased values, for the
                     lateralised frontal weights)
    ANATOMY          metadata: name, location, notes

These are constants and plain dicts, not classes. A Brodmann area is a
reference label, not an agent — it has no lifecycle. The thing that
computes is the sub-region; the thing that gets labelled is the area.

SYSTEM MAPPING (the difference from cingulate's one-area-one-system)
--------------------------------------------------------------------
The frontal lobe's compute sub-regions do not map to disjoint sets of
Brodmann areas. The mapping, in a form the sub-regions can use:

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

For the shared areas, the per-area LEFT_CONFIG contains *per-system*
weights — e.g. area 6's config has a "premotor" block and a
"supplementary_motor" block, and each sub-region reads its own block.
This is documented in each shared area's individual file. The registry
itself does not arbitrate between the systems; it just labels the areas
and provides the per-system config blocks.

BROCAS_AREA
-----------
`brocas_area/` is a sub-package containing brodmann_area_44/ and
brodmann_area_45/. It exists because Broca's area is a well-known,
functionally-coupled two-area unit (pars opercularis + pars triangularis
together implement language production), and the nesting makes that
coupling visible in the import path:
    from .brocas_area.brodmann_area_44 import BRODMANN_44
    from .brocas_area.brodmann_area_45 import BRODMANN_45
The registry re-exports the two area constants at this level so that
consumers can write `from ...brodmann_areas import BRODMANN_44` without
knowing about the nesting. The compute that Broca's area participates in
lives in `cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/`,
not in a separate Broca's compute package — Broca's area is a labelling
of a VLPFC sub-region, not a fifth compute sub-region.

CROSS-LOBE ENTRY: brodmann_area_25
----------------------------------
The directory `brodmann_area_25/` exists under frontal/brodmann_areas/
because Brodmann 25 (subgenual ACC) sits anatomically at the
frontal/cingulate boundary and appears in both trees. BUT:

    The COMPUTE for area 25 lives in `cingulate/subgenual_area_25/`
    (specifically, the stateful affect channel). The entry here is
    a registry annotation and a documented cross-reference.

    Code that needs area 25's affect computation imports from
    `cingulate/subgenual_area_25/`. Code that needs area 25's
    anatomical metadata (for receptor-distribution lookups, lesion
    annotation, etc.) imports from here.

    SYSTEM is an empty list — area 25 is not a frontal compute area.
    There is no LEFT_CONFIG for a frontal compute that does not exist;
    the entry's only runtime content is ANATOMY metadata that
    cross-references the cingulate package.

    If you are looking for Brodmann 25's config in this registry and
    not finding it, this paragraph is why. It is not an oversight.

TREE ARTIFACT: brodmann_area_33
-------------------------------
The directory `brodmann_area_33/` exists under frontal/brodmann_areas/
but area 33 is anatomically part of the cingulate (it is a small
transitional area adjacent to area 24 on the medial wall). It is in
the frontal tree because the tree's organisation places it here; it
should be understood as a cingulate area for ownership purposes.

    The COMPUTE for area 33 — such as it is; area 33 is a tiny
    transitional area with no clearly-defined independent function in
    the model — would live in the cingulate package if it were ever
    instantiated. It is not instantiated as a compute node; the entry
    here is a registry annotation only.

    SYSTEM is an empty list. There is no LEFT_CONFIG. If the tree is
    ever normalised, brodmann_area_33/ moves to
    `cingulate/brodmann_areas/brodmann_area_33/`; until then, this
    entry documents the intended ownership and pre-empts the
    confusion of finding a cingulate area under the frontal tree.

ANATOMY vs. COMPUTE (the parent-level note)
-------------------------------------------
The frontal lobe's cortex/ tree contains the compute; this registry
contains the labelling. That distinction is enforced by the import
direction:

    - Compute sub-regions (prefrontal_cortex, premotor_cortex,
      primary_motor_cortex, supplementary_motor_cortex) import FROM
      this registry.
    - This registry imports from NOTHING except the chemicals/hormones
      config layer, for per-area hormone-receptor metadata.
    - Importing a compute sub-region from this registry would create a
      cycle and is a layering bug.

The registry does not know what computation happens on any of its
labelled areas. That knowledge lives in the sub-regions.

LEFT-HEMISPHERE CONFIG NOTE
---------------------------
The area IDs and anatomical metadata are identical across hemispheres.
Only LEFT_CONFIG differs from RIGHT_CONFIG — and, for the frontal lobe,
the difference is DIRECTIONAL rather than complementary, because many
of the frontal lateralised weights are not two halves of a single
budget:

    - Broca's area (44/45): left weight >> right weight on lexical
      production; right has a separate (smaller) prosodic weight, not
      the complement of the left's.
    - Dorsolateral prefrontal: left-weighted verbal WM, right-weighted
      spatial WM — the two are not complements.
    - OFC (11/12): left-weighted positive-valence, right-weighted
      negative-valence — directional, not complementary.
    - Motor areas: left-weighted fine distal, right-weighted gross
      proximal — directional.

The mirror-assertion test for this registry is therefore a *directional*
check per lateralised key, not a "sum to 1" check. For shared keys
(anatomy, area IDs, structural weights like the LEFT_CONFIG / RIGHT_CONFIG
sharing the same sub-keys), the check is equality. The pattern is the
same distinction we drew in the cingulate between structural and
configurable keys; frontal simply has more configurable keys, and more
of them are directional rather than complementary.

The cross-lobe and tree-artifact entries (25, 33) have NO config on
either side; their mirror check is "both are empty", which is trivially
true and should be asserted as such so a future change adding config to
them fails the test.


Programming contract for this package
-------------------------------------
- This __init__.py does no computation. It re-exports the area constants
  (e.g. `from .brodmann_area_4 import BRODMANN_4` and
  `from .brocas_area.brodmann_area_44 import BRODMANN_44`) so that
  consumers write flat imports against this package.
- Each `brodmann_area_XX/__init__.py` contains only constants, dicts,
  and docstring. No classes, no functions beyond optional trivial
  accessors.
- `brocas_area/__init__.py` is itself a nested registry parent; it
  re-exports its two areas the same way this package does.
- The `SYSTEM` field is a list. Consumers that expect a single system
  must handle the list (either by asserting len==1, or by iterating to
  find the system they care about, or by checking membership). This is
  the main structural difference from the cingulate registry, and code
  that reuses cingulate-shaped registry consumers against this one will
  break on shared areas and cross-lobe entries.
- The empty-SYSTEM entries (25, 33) are first-class members of the
  registry with `SYSTEM == []`. Consumer code must handle them
  explicitly (typically: skip them for compute purposes). Silently
  ignoring them is a bug — they should be skipped with a documented
  comment explaining why, so that adding an entry to the registry
  forces the skip to be reviewed.
- This registry must never import a compute sub-region. Any upward
  import is a layering bug.
- The mirror-assertion test for LEFT_CONFIG vs RIGHT_CONFIG is directional
  for lateralised keys and equal for structural keys, as described
  above; the cross-lobe and tree-artifact entries assert "both empty"
  rather than mirroring.
- If a Brodmann area ever genuinely needs its own state (rather than
  just config values), it is promoted out of this registry into its own
  package at the `frontal/` level — the way `subgenual_area_25` is
  promoted in the cingulate — rather than being given a lifecycle inside
  this registry. Do not give a registry entry a lifecycle.
"""