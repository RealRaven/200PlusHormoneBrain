"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.brodmann_areas.brocas_area
=================================================================================================================

BROCA'S AREA — right hemisphere.

Mirror of the left brocas_area package. A NESTED REGISTRY PARENT. Not a
compute node, not a registry entry, not an annotation. This package groups
two Brodmann area registry entries — brodmann_area_44/ and
brodmann_area_45/ — under a single named sub-package, and re-exports their
constants so that consumers can write flat imports against the parent
registry rather than deep paths.

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
The nesting rationale is identical to the left's — the coupling of 44 and
45 into a functionally meaningful unit, and the tree visibility of Broca's
area as a named anatomical region, are facts about anatomy and about the
literature, not about hemisphere. Briefly:

    1. FUNCTIONAL COUPLING. Areas 44 and 45 together form a coupled pair
       (44 = phonological/articulatory, 45 = lexical/semantic selection
       on the left; prosody/affective variants on the right). The
       sub-package makes the coupling visible.
    2. TREE VISIBILITY. Grouping keeps Broca's area recognisable as a
       named region rather than as two adjacent registry entries.
    3. CROSS-LOBE CORRECTNESS. The right hemisphere's prosodic and
       affective Broca's-area roles are anchored in the literature just
       as the left's lexical roles are; grouping makes "Broca's area,
       right" a coherent reference unit.

The right hemisphere's Broca's area IS Broca's area — it is the same
anatomical structure, the same two Brodmann areas, with a different
functional weighting. The nesting reflects the anatomical unit, not the
left's particular use of it.

WHAT IS ACTUALLY IN THIS PACKAGE
--------------------------------
Two sub-directories and the re-exports:

    brodmann_area_44/       registry entry (constants + RIGHT_CONFIG + ANATOMY)
    brodmann_area_45/       registry entry (constants + RIGHT_CONFIG + ANATOMY)

And the flat re-exports:

    BRODMANN_44             int, == 44
    BRODMANN_45             int, == 45
    BROCA_AREAS             list, == [44, 45], useful for iteration
    RIGHT_CONFIG_44         convenience re-export of 44's RIGHT_CONFIG
    RIGHT_CONFIG_45         convenience re-export of 45's RIGHT_CONFIG

The re-exports exist so that the parent registry (and consumers writing
against it) can do:

    from ...brodmann_areas import BRODMANN_44, BRODMANN_45

rather than reaching into the nesting. The re-export names and structure
are IDENTICAL to the left's; only the configs' contents differ.

WHAT IT IS NOT
--------------
    - Not a compute sub-region. There is no encode() here, no state, no
      RIGHT_CONFIG at the brocas_area level. The area-level configs live
      in each child area package.
    - Not a registry entry in its own right. There is no AREA_ID, no
      SYSTEM, no ANATOMY at this level; those live in the children. A
      consumer iterating the frontal registry should see 44 and 45 as
      two areas, not Broca's area as one.
    - Not an annotation. Broca's area is a functional grouping of
      Brodmann areas, which is the registry's category, not the
      annotation layer.
    - Not a separate lateralisation mechanism. The left/right difference
      in Broca's area is expressed in each child area's LEFT_CONFIG vs
      RIGHT_CONFIG; it is not expressed at this package level.

RIGHT-SPECIFIC BIAS (expressed in the children, not here)
---------------------------------------------------------
On the right, Broca's area (44 + 45) carries the prosodic and affective
speech roles rather than the lexical/motor-production roles:

    area 44     On the right, area 44's phonological/articulatory
                motor-speech role is much reduced — the right's 44 is
                not the dominant motor-speech output. What the right's
                44 contributes is expressive prosody and emotional tone,
                with the articulatory machinery present but not the
                primary driver. The RIGHT_CONFIG_44 expresses a
                prosody-forward profile with a small residual
                articulatory weight.

    area 45     On the right, area 45's lexical/semantic-selection role
                is minimal — the right's 45 does not choose words. What
                it contributes is the affective-prosodic interface:
                matching prosodic contour to emotional content,
                producing the melodic contour of speech rather than its
                lexical content. The RIGHT_CONFIG_45 expresses a
                prosody/affect-forward profile with a small residual
                lexical weight.

The important point: the right's Broca's area is not "the left's
Broca's area at low weight." It is a functionally different
contributor — prosody and emotional tone rather than lexicon and
articulation — and the RIGHT_CONFIG for each child area reflects that
distinct function, not a scaled-down version of the left's function.
This is the same distinction the frontal lobe docstring drew for the
Broca's-area mirror: directional, not complementary.

All of this lives in the child area configs. This package does not
carry a config; it groups and re-exports.

CROSS-MIDLINE RULE
------------------
This package must never import or reference the left hemisphere's
brocas_area. The cross-hemisphere relationship between right and left
Broca's areas is asserted by the test suite (via the child areas' config
mirrors) and expressed at runtime only through the commissures.

The case that matters most for Broca's area is cross-midline speech
coordination: prosody from the right, lexical and articulatory content
from the left, combined into fluent speech by commissural traffic. That
coordination is a commissures job; neither hemisphere's Broca's area
reads the other's. On the right specifically, the failure mode of the
commissures is flat, literal speech with intact content but no
prosodic contour — the right's Broca's area has the prosody ready but
cannot deliver it to the left's output stream. Surfacing that failure
mode correctly is the commissures' responsibility, not this package's.


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
  RIGHT_CONFIG_44, RIGHT_CONFIG_45) is the entire public surface of this
  package at its own level. It must be STRUCTURALLY IDENTICAL to the
  left's re-export list — same names, same list contents for BROCA_AREAS,
  same int values for BRODMANN_44/45. Only the config contents differ.
- This package must never import or reference the left hemisphere's
  brocas_area. Cross-midline registry access is a bug; the relationship
  between left and right Broca's areas is validated by the test suite,
  not by runtime import.
- Structural-equality test: the left and right brocas_area packages must
  have identical re-export lists and identical child-area structures
  (same AREA_IDs, same SYSTEM, same ANATOMY). Only the RIGHT_CONFIG vs
  LEFT_CONFIG values inside the children differ, and the mirror test for
  those is DIRECTIONAL (prosody/affect weights up on the right, lexical
  and articulatory weights down on the right), not complementary.
"""