"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.frontal.cortex.primary_motor_cortex.precentral_gyrus
======================================================================================================================================

The PRECENTRAL GYRUS — right hemisphere. A PURE ANATOMICAL ANNOTATION
NESTED INSIDE THE PRIMARY MOTOR CORTEX COMPUTE SUB-REGION.

Mirror of the left precentral_gyrus package. This package contains:
  - no compute (no encode(), no step())
  - no state
  - no configuration (no RIGHT_CONFIG, no SYSTEM)
  - no imports from or to any compute package

It exists solely so that the precentral gyrus — the surface expression of
Brodmann area 4 — has a canonical address in the tree, for cross-references
in docstrings and for per-region metadata that the chemicals/hormones
config layer may cite.

If you are looking for the compute that area 4 participates in, it lives
in the PARENT package (`primary_motor_cortex/`), not here. The precentral
gyrus is the anatomical surface of area 4; area 4's computation is
primary motor cortex's computation; this package documents the surface.
On the right, the surface is the same anatomical structure as on the
left; the underlying cortex's lateralisation (right: proximal power and
facial expression; left: distal precision and speech articulators) is a
property of area 4's RIGHT_CONFIG, not of the gyrus.

NESTED ANNOTATION — the unusual part of the placement
-----------------------------------------------------
This is the second of two annotations nested inside a compute sub-region
in the project (the left precentral_gyrus is the first). The nesting is
the same on both hemispheres, for the same reason: the precentral gyrus
IS the surface of area 4, and area 4 is the primary motor cortex's sole
registry source. The nesting expresses anatomical containment.

The nesting does NOT mean the precentral gyrus is a fifth sub-region of
primary motor. It has:
  - no encode() method
  - no config (not in RIGHT_PRIMARY_MOTOR_CONFIG or any config dict)
  - no state
  - no entry in RIGHT_FRONTAL_CORTEX_CONFIG["order"]
  - no entry in any sub-region list
  - no call from FrontalCortex, PrimaryMotorCortex, or anything else

The parent package (`primary_motor_cortex/__init__.py`) re-exports this
module for external cross-reference
(`from .primary_motor_cortex import precentral_gyrus`), but the parent's
class does not read it. The annotation is documentary.

THE GENERAL RULE (restated for this nesting)
--------------------------------------------
Same rule as on the left:

    - Annotation packages have ANATOMY and SIDE, and nothing else.
    - They are never in composition configs (order lists,
      primary_output_key maps, group/source maps).
    - They are never called by a compute class.
    - They may be re-exported by their parent for external
      cross-reference, but the parent's class does not read them.

The rule scales to any depth; the placement is a tree-organisation
detail, not a functional relationship.

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
            "of the underlying cortex (right: proximal power and "
            "facial expression; left: distal precision and speech "
            "articulators) is a property of area 4's RIGHT_CONFIG in "
            "the primary_motor_cortex package, not of the gyrus "
            "itself. The gyrus is documented here as an anatomical "
            "annotation because its surface anatomy is a canonical "
            "reference point for per-region metadata (receptor "
            "distributions, lesion annotation, electrophysiology) "
            "and because the motor homunculus is one of the "
            "most-cited topographic maps in neuroscience. It has no "
            "independent compute and no state. It is the "
            "third-category annotation pattern, same as "
            "indusium_griseum, applied inside a compute sub-region "
            "because of the anatomical containment relationship."
        ),
    }

    Anatomy is identical to the left's except for the SIDE field and
    the minor right-specific wording in `notes` (which names the
    right's lateralisation of the underlying area-4 cortex). The
    somatotopic organisation (face ventrolateral, hand mid-
    convexity, leg medial) is the same on both hemispheres — it is
    a property of the surface anatomy, not of the functional
    lateralisation.

RELATED STRUCTURES (for cross-reference, not definition)
--------------------------------------------------------
Same as on the left:
    - the central sulcus (posterior boundary)
    - the precentral sulcus (anterior boundary)
    - the superior, middle, and inferior frontal gyri (anterior to
      the precentral sulcus)
    - the paracentral lobule (medial continuation)

All anatomical neighbours; none is a compute relationship. The sulci
and gyri are documented as lobe-level annotations in `frontal/sulci/`
and `frontal/gyri/`.

WHY IT LIVES INSIDE primary_motor_cortex/
-----------------------------------------
Same as on the left: the placement reflects anatomical containment.
The precentral gyrus is uniquely the surface of area 4, which is
uniquely primary motor cortex's sole registry source. Placing it
outside primary motor's package would make the containment
relationship harder to see. If a future refactor unifies all frontal
gyri under `frontal/gyri/`, the ANATOMY["parent_compute"] field
preserves the containment relationship; until then, the nesting is the
documented state.

CROSS-MIDLINE RULE
------------------
This package has no state, no compute, and nothing to compute. The
standard "no cross-midline state bleed" rule is trivially satisfied.
The rule that *does* apply is **structural consistency**: this package
must be structurally identical to the LEFT hemisphere's
precentral_gyrus package — same ANATOMY field set and content (except
SIDE and the minor right-specific wording in `notes`), same absence of
config, same absence of encode(). Both are documenting the same
anatomical structure and the same nesting relationship; if they
diverge in structure, that is a bug.

Note that "structurally identical except for SIDE and the notes
wording" is the correct contract for an ANNOTATION. Anatomical
structures do not lateralise; only the functional lateralisation of
the underlying cortex does. The right's precentral gyrus is the same
gyrus as the left's — the somatotopic map is the same, the surface
landmarks are the same — and its only "right-ness" is which
hemisphere it is on. If a future contributor is tempted to give the
two precentral_gyrus packages directional configs (e.g. to mirror
"right premotor's proximal emphasis" into the gyrus's ANATOMY), that
would be a misunderstanding of what an annotation is — the
lateralisation lives in area 4's configs, not in the annotation.

The two hemispheres' *underlying compute* (primary motor cortex) is
independent and lateralised via area 4's RIGHT_CONFIG vs LEFT_CONFIG.
That independence is a property of the compute package, not of this
annotation.

WHAT THIS PACKAGE MUST NOT DO
-----------------------------
    - Must not define an `encode()`, `step()`, or any stateful object.
    - Must not gain a `LEFT_CONFIG`, `RIGHT_CONFIG`, or `SYSTEM` key.
    - Must not be added to RIGHT_FRONTAL_CORTEX_CONFIG["order"] or to
      any sub-region list. Adding it would break the parent's step()
      (an annotation has no encode() method to call).
    - Must not be imported by PrimaryMotorCortex's class. The parent
      package re-exports this module for external cross-reference,
      but the class itself is unaware of it.
    - Must not import from any compute package. The relationship is
      documentary (ANATOMY fields), not computational.
    - Must not be promoted to a runtime package without a documented
      functional justification.
    - Must not diverge in structure from the left hemisphere's
      precentral_gyrus package — same ANATOMY field set and content
      (except SIDE and the minor right-specific wording in `notes`),
      same absence of config. The two are documenting the same
      structure; divergence is a bug.
    - Must not acquire directional ANATOMY fields to mirror the
      underlying cortex's lateralisation. The gyrus's anatomy is
      symmetric; the lateralisation is in area 4's configs, not in
      the annotation. If a future contributor wants the gyrus's
      ANATOMY to carry "the right's motor strip emphasises proximal
      power", that is exactly the kind of misfiling the annotation
      category exists to prevent — the proximal-power emphasis is a
      property of the right's area 4 config, not of the precentral
      gyrus surface.

WHERE IT WOULD GO IF THE TREE IS NORMALISED
-------------------------------------------
Same two normalisation paths as on the left, and they apply
symmetrically:

    path A (surface-anatomy grouping):  move to
        `frontal/gyri/precentral_gyrus/` alongside the other frontal
        gyri. ANATOMY["parent_compute"] preserves the containment
        relationship.
    path B (keep the nesting):          leave it where it is.

Neither path changes any compute; the choice is organisational. Both
hemispheres would move together under path A (the two precentral_gyrus
packages stay structurally identical).

DISTINGUISHING THIS ANNOTATION FROM THE OTHER FRONTAL ANNOTATIONS
-----------------------------------------------------------------
Same three kinds of annotation as on the left:

    frontal/gyri/       the superior, middle, and inferior frontal
                        gyri — lobe-level annotations, peers of the
                        frontal sulci
    frontal/sulci/      the six frontal sulci — lobe-level
                        annotations

    primary_motor_cortex/precentral_gyrus/     THIS package — a
                        nested annotation, inside a compute
                        sub-region, documenting the surface of a
                        specific Brodmann area that maps to that
                        sub-region

The lobe-level annotations are peers of each other; this one is
contained. The distinction is anatomical and identical across
hemispheres.

SIDE
----
    SIDE = "right"

EXPORTS
-------
    from .precentral_gyrus import ANATOMY    # dict, as above
    from .precentral_gyrus import SIDE       # str, "right"

That is the entire public surface. There is no config, no computation,
and no sub-module contract to satisfy.


Programming contract for this package
-------------------------------------
- This __init__.py contains only constants and docstring. No classes,
  no functions, no runtime logic.
- The ANATOMY dict has the same field set and content as the left's
  (except SIDE and the minor right-specific wording in `notes`). A
  structural-equality test should assert this; a directionality test
  would fail spuriously, because annotations are not lateralised.
- The parent (primary_motor_cortex/__init__.py) re-exports this
  module but does not read it at runtime.
- The module has no `encode` attribute. A test should assert that
  (guards against accidental promotion to compute).
- The module has no config attribute. A test should assert that.
- Must not import or reference the left hemisphere's precentral_gyrus
  package. The relationship between the two is structural equality,
  asserted by the test suite, not by runtime import.
"""