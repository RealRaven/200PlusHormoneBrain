"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.brodmann_areas.brocas_area
================================================================================================================

BROCA'S AREA — left hemisphere.

A NESTED REGISTRY PARENT. Not a compute node, not a registry entry, not an
annotation. This package groups two Brodmann area registry entries —
brodmann_area_44/ and brodmann_area_45/ — under a single named sub-package,
and re-exports their constants so that consumers can write flat imports
against the parent registry rather than deep paths.

If you are looking for the compute that Broca's area participates in, it
lives in
`.../frontal/cortex/prefrontal_cortex/ventrolateral_prefrontal_cortex/` —
Broca's area is a Brodmann-area-level LABEL on a VLPFC sub-region, not a
fifth compute sub-region of its own. There is no Broca's-area compute
package, and there should not be one.

If you are looking for the two individual areas, they are here:
    brodmann_area_44/   pars opercularis
    brodmann_area_45/   pars triangularis

WHY IT'S NESTED
---------------
The nesting is not cosmetic. Three reasons, in order of importance:

    1. FUNCTIONAL COUPLING. Areas 44 and 45 together implement language
       production (in the classic model: 44 = phonological/articulatory,
       45 = lexical/semantic selection). Treating them as a coupled
       pair is the anatomically standard move, and the sub-package makes
       the coupling visible in the import path and in the tree.

    2. TREE VISIBILITY. If 44 and 45 were siblings of the other frontal
       areas, the tree would look like Broca's area did not exist as a
       named anatomical unit — it would appear only as two adjacent
       registry entries that a reader might or might not recognise as
       Broca's. The nesting makes the functional grouping visible at the
       tree level.

    3. CROSS-LOBE CORRECTNESS. Broca's area is a classic "what is this
       lobe's role?" reference point, and both the left hemisphere's
       language-production dominance and the right's prosody/affective
       roles are anchored to it in the literature. Keeping 44 and 45
       grouped makes it easy to reference "Broca's area, left" and
       "Broca's area, right" as coherent units in the rest of the
       project's documentation.

WHAT IS ACTUALLY IN THIS PACKAGE
--------------------------------
Two sub-directories and the re-exports:

    brodmann_area_44/       registry entry (constants + LEFT_CONFIG + ANATOMY)
    brodmann_area_45/       registry entry (constants + LEFT_CONFIG + ANATOMY)

And the flat re-exports:

    BRODMANN_44             int, == 44
    BRODMANN_45             int, == 45
    BROCA_AREAS             list, == [44, 45], useful for iteration
    LEFT_CONFIG_44          convenience re-export of 44's LEFT_CONFIG
    LEFT_CONFIG_45          convenience re-export of 45's LEFT_CONFIG

The re-exports exist so that the parent registry (and consumers writing
against it) can do:

    from ...brodmann_areas import BRODMANN_44, BRODMANN_45

rather than reaching into the nesting. The sub-package is the *canonical
location* of the two areas; the flat re-exports are the *convenient path*.

WHAT IT IS NOT
--------------
    - Not a compute sub-region. There is no encode() here, no state, no
      LEFT_CONFIG at the brocas_area level. The area-level configs live
      in each child area package.
    - Not a registry entry in its own right. There is no AREA_ID, no
      SYSTEM, no ANATOMY at this level; those live in the children. A
      consumer that iterates the frontal registry's areas should see
      44 and 45 as two areas, not Broca's area as one.
    - Not an annotation. Gyri/sulci are annotations; Broca's area is a
      functional grouping of Brodmann areas, which is the registry's
      category.
    - Not a separate lateralisation mechanism. The left/right difference
      in Broca's area is expressed in each child area's LEFT_CONFIG vs
      RIGHT_CONFIG; it is not expressed at this package level.

LEFT-SPECIFIC BIAS (expressed in the children, not here)
--------------------------------------------------------
On the left, Broca's area (44 + 45) carries the dominant lexical
language-production weight. The two areas split that role:

    area 44     phonological and articulatory production — the
                motor-speech output of language. Left-weighted heavily
                toward this role; the right's 44 carries a much smaller
                motor-speech contribution and a larger prosodic one.
    area 45     lexical/semantic selection — choosing words. Left-
                weighted heavily toward this role; the right's 45 is
                small and carries little lexical-selection weight.

On the right, the same two areas carry the prosodic and affective
counterparts (expressive prosody, emotional tone in speech), not the
lexical/motor production roles. The RIGHT_CONFIG in each child area
expresses that.

All of this lives in the child area configs. This package does not
carry a config; it groups and re-exports.

CROSS-MIDLINE RULE
------------------
This package must never import or reference the right hemisphere's
brocas_area. The cross-hemisphere relationship between left and right
Broca's areas is asserted by the test suite (via the child areas' config
mirrors) and expressed at runtime only through the commissures, not by
direct access. In practice, the case that matters for Broca's area is
cross-midline *speech* coordination — prosody from the right, lexical
and articulatory content from the left, combined into fluent speech by
the commissural traffic. That coordination is a commissures job; neither
hemisphere's Broca's area reads the other's.


Programming contract for this package
-------------------------------------
- This __init__.py is a thin re-export module. It imports the two
  child area modules and re-exports their constants and configs. It
  defines no classes and no functions.
- The two children, brodmann_area_44/ and brodmann_area_45/, each follow
  the standard registry-entry contract: constants, config dicts,
  docstring; no classes; no functions; SYSTEM is a list (both areas
  belong to prefrontal_cortex, specifically VLPFC).
- Consumers should prefer the flat re-exports
  (`from ...brodmann_areas import BRODMANN_44`) over reaching into the
  nesting; the nesting is a tree-organisation detail and the flat path
  is the stable API.
- Neither child area is a compute node. If a future change wants
  Broca's-area compute as a distinct unit, that change is a compute-layer
  decision that belongs in `prefrontal_cortex/ventrolateral_prefrontal_
  cortex/`, not in this registry sub-package. Do not give this package
  an encode().
- The re-export list (BRODMANN_44, BRODMANN_45, BROCA_AREAS,
  LEFT_CONFIG_44, LEFT_CONFIG_45) is the entire public surface of this
  package at its own level. Adding a re-export is a small, stable change
  to the registry's API; do it intentionally, not incidentally.
- Structural-equality test: the left and right brocas_area packages
  must have identical re-export lists and identical child-area structures
  (same AREA_IDs, same SYSTEM, same ANATOMY). Only the LEFT_CONFIG vs
  RIGHT_CONFIG values inside the children differ. Assert this alongside
  the directional-weight mirror test that already exists for the
  children.
"""