"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.frontal.cortex.primary_motor_cortex.precentral_gyrus
=====================================================================================================================================

The PRECENTRAL GYRUS — left hemisphere. A PURE ANATOMICAL ANNOTATION
NESTED INSIDE THE PRIMARY MOTOR CORTEX COMPUTE SUB-REGION.

This package contains:
  - no compute (no encode(), no step())
  - no state
  - no configuration (no LEFT_CONFIG, no SYSTEM)
  - no imports from or to any compute package

It exists solely so that the precentral gyrus — the surface expression of
Brodmann area 4 — has a canonical address in the tree, for cross-references
in docstrings and for per-region metadata that the chemicals/hormones
config layer may cite.

If you are looking for the compute that area 4 participates in, it lives
in the PARENT package (`primary_motor_cortex/`), not here. The precentral
gyrus is the anatomical surface of area 4; area 4's computation is
primary motor cortex's computation; this package documents the surface.

NESTED ANNOTATION — the unusual part of the placement
-----------------------------------------------------
This is the first ANNOTATION nested inside a COMPUTE SUB-REGION in the
project. Earlier annotations (`cingulate/indusium_griseum/`, the frontal
lobe's `gyri/` and `sulci/`) are at lobe level or as siblings of compute
sub-modules. This one is one level deeper, nested inside primary motor
cortex — because the precentral gyrus IS the surface of area 4, and area
4 is the primary motor cortex's sole registry source. The nesting
expresses the anatomical containment (gyrus is on top of the motor strip
that defines the motor strip's location) rather than a compute
relationship.

The nesting does NOT mean the precentral gyrus is a fifth sub-region of
primary motor. It has:
  - no encode() method
  - no config (not in LEFT_PRIMARY_MOTOR_CONFIG or any config dict)
  - no state
  - no entry in LEFT_FRONTAL_CORTEX_CONFIG["order"]
  - no entry in any sub-region list
  - no call from FrontalCortex, PrimaryMotorCortex, or anything else

The parent package (`primary_motor_cortex/__init__.py`) re-exports this
module for external cross-reference (`from .primary_motor_cortex import
precentral_gyrus`), but the parent's class does not read it. The
annotation is documentary.

THE GENERAL RULE (restated for this nesting)
--------------------------------------------
Annotation can appear anywhere a named anatomical structure needs a
canonical address, INCLUDING inside compute sub-regions. The rule is:

    - Annotation packages have ANATOMY and SIDE, and nothing else.
    - They are never in composition configs (order lists,
      primary_output_key maps, group/source maps).
    - They are never called by a compute class.
    - They may be re-exported by their parent for external
      cross-reference, but the parent's class does not read them.

This nesting is the first exercise of the rule at depth 2 (inside a
compute sub-region that itself is inside a lobe). A future annotation
inside SMA or premotor would follow the same pattern. The rule scales
to any depth; the placement is a tree-organisation detail, not a
functional relationship.

WHAT IT IS
----------
    ANATOMY = {
        "name": "Precentral gyrus",
        "kind": "anatomical annotation (non-compute)",
        "system": None,                 # not a functional sub-module
        "brodmann": 4,                  # the Brodmann area it is the
                                        # surface of
        "parent_compute": "primary_motor_cortex",
        "location": "the gyral surface immediately anterior to the "
                    "central sulcus, extending from the lateral "
                    "fissure (ventrolaterally) up over the convexity "
                    "and onto the medial surface (paracentral "
                    "lobule, in the longitudinal fissure); its "
                    "surface is the gyral expression of the "
                    "underlying primary motor cortex (area 4)",
        "notes": (
            "The precentral gyrus is the surface expression of the "
            "primary motor cortex (Brodmann area 4). It is one of "
            "the most recognisable landmarks of the human brain "
            "surface — the motor strip, the site of the motor "
            "homunculus, and the origin of the corticospinal and "
            "corticobulbar tracts. Its somatotopic organisation is "
            "the same on both hemispheres (face ventrolateral, hand "
            "mid-convexity, leg medial); the functional lateralisation "
            "of the underlying cortex (left: distal precision and "
            "speech articulators; right: proximal power and facial "
            "expression) is a property of area 4's config in the "
            "primary_motor_cortex package, not of the gyrus itself. "
            "The gyrus is documented here as an anatomical annotation "
            "because its surface anatomy is a canonical reference "
            "point for per-region metadata (receptor distributions, "
            "lesion annotation, electrophysiology) and because the "
            "motor homunculus is one of the most-cited topographic "
            "maps in neuroscience. It has no independent compute "
            "and no state. It is the third-category annotation "
            "pattern, same as indusium_griseum, applied inside a "
            "compute sub-region because of the anatomical "
            "containment relationship."
        ),
    }

RELATED STRUCTURES (for cross-reference, not definition)
--------------------------------------------------------
The precentral gyrus is bordered and connected with:
    - the central sulcus (its posterior boundary — separating it
      from the postcentral gyrus, the primary somatosensory
      surface)
    - the precentral sulcus (its anterior boundary — separating it
      from the premotor cortex's surface)
    - the superior, middle, and inferior frontal gyri (anterior to
      the precentral sulcus; the frontal lobe's other surface
      landmarks)
    - the paracentral lobule (the medial continuation, where the
      leg/trunk representation sits)

All of these are anatomical neighbours; none is a compute relationship.
The precentral sulcus and inferior frontal sulcus are documented as
annotations in the frontal lobe's `sulci/` package; the frontal gyri
are in the frontal lobe's `gyri/` package.

WHY IT LIVES INSIDE primary_motor_cortex/
-----------------------------------------
The placement reflects anatomical containment: the precentral gyrus is
literally the surface of the tissue that area 4 defines. It is not at
lobe level (where the other gyri and sulci are) because it is not one
of many equivalent gyri — it is specifically and uniquely the surface
of the primary motor cortex, and placing it outside primary motor's
package would make the relationship harder to see.

The alternative — placing it under the frontal lobe's `gyri/` package
alongside the superior/middle/inferior frontal gyri — would be
defensible on surface-anatomy grounds but would lose the containment
relationship. It would also imply (wrongly) that the precentral gyrus
is a peer of the other frontal gyri; it isn't, because it is the
surface of a specific Brodmann area (4) that maps to a specific
compute sub-region (primary motor cortex), whereas the other frontal
gyri are surface expressions of multiple areas spread across
prefrontal and premotor.

If a future refactor unifies all frontal gyri under `frontal/gyri/`,
the precentral gyrus could move there too, with its ANATOMY's
`parent_compute: "primary_motor_cortex"` field preserving the
containment relationship. Until then, the nesting is the documented
state and the ANATOMY field is the cross-reference.

SIDE
----
    SIDE = "left"

The anatomical structure is bilateral and symmetric. Its right-hemisphere
counterpart package is identical except for SIDE (and the SIDE in the
`notes` field's references to hemifield-specific lateralisation of the
underlying cortex — which is identical because the notes describe the
lateralisation of area 4, not the gyrus's own).

EXPORTS
-------
    from .precentral_gyrus import ANATOMY    # dict, as above
    from .precentral_gyrus import SIDE       # str, "left"

That is the entire public surface. There is no config, no computation,
and no sub-module contract to satisfy.

CROSS-MIDLINE RULE
------------------
This package has no state, no compute, and nothing to compute. The
standard "no cross-midline state bleed" rule is trivially satisfied.
The rule that *does* apply is **structural consistency**: this package
must be structurally identical to the right hemisphere's
precentral_gyrus package — same ANATOMY field set and content (except
SIDE and the hemifield-specific notes, if any), same absence of config,
same absence of encode(). Both are documenting the same anatomical
structure and the same nesting relationship; if they diverge in
structure, that is a bug.

The two hemispheres' *underlying compute* (primary motor cortex) is
independent and lateralised (via area 4's configs). That independence
is a property of the compute package, not of this annotation. The
annotation packages are structurally identical; the compute packages
are stateful (actually pure for primary motor, but distinct) and
independent.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not gain a `LEFT_CONFIG`, `RIGHT_CONFIG`, or `SYSTEM` key.
      The absence of configuration is the point: if a future change
      wants to give the precentral gyrus behaviour, that is a signal
      that the anatomical reality has been misunderstood (the gyrus
      is a surface, not a function) — not that the config needs
      extending.
    - Must not be added to LEFT_FRONTAL_CORTEX_CONFIG["order"] or to
      any sub-region list. It is not a compute sub-region, and adding
      it to the composition would break the parent's step() (an
      annotation has no encode() method to call).
    - Must not be imported by PrimaryMotorCortex's class. The parent
      package re-exports this module for external cross-reference,
      but the class itself is unaware of it. A runtime read from the
      class would couple the compute to the annotation.
    - Must not import from any compute package. The relationship is
      documentary (ANATOMY fields), not computational.
    - Must not be promoted to a runtime package without a documented
      functional justification. "It's an important anatomical
      landmark" is not a reason; "it demonstrably computes X" is.
    - Must not diverge in structure from the right hemisphere's
      precentral_gyrus package — same ANATOMY field set and content
      (except SIDE), same absence of config. The two are documenting
      the same structure; divergence is a bug.

WHERE IT WOULD GO IF THE TREE IS NORMALISED
-------------------------------------------
Two normalisation paths are possible, and the ANATOMY fields support
both:

    path A (surface-anatomy grouping):  move to `frontal/gyri/
        precentral_gyrus/` alongside the other frontal gyri. The
        ANATOMY["parent_compute"] field preserves the containment
        relationship to primary_motor_cortex.

    path B (keep the nesting):          leave it where it is. The
        nesting is the strongest expression of containment, and if
        a future contributor wonders why the precentral gyrus isn't
        with the other gyri, this file's docstring explains.

Neither path changes any compute. The annotation is documentary in
either placement; the choice is organisational, and the current
nesting is the documented state.

DISTINGUISHING THIS ANNOTATION FROM THE OTHER FRONTAL ANNOTATIONS
-----------------------------------------------------------------
This is one of three kinds of annotation in the frontal lobe:

    frontal/gyri/       the superior, middle, and inferior frontal
                        gyri — lobe-level annotations, peers of the
                        frontal sulci
    frontal/sulci/      the precentral, inferior frontal, orbital,
                        paracentral, superior frontal, and olfactory
                        sulci — lobe-level annotations

    primary_motor_cortex/precentral_gyrus/     THIS package — a
                        nested annotation, inside a compute
                        sub-region, documenting the surface of a
                        specific Brodmann area that maps to that
                        sub-region

The lobe-level annotations are peers of each other; this one is
contained. The distinction is anatomical (the precentral gyrus is
uniquely the surface of area 4; the other frontal gyri are surface
expressions of multiple areas), and it's why the placement differs.
"""