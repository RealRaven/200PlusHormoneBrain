"""
Occipital Gyri — Right Hemisphere
==================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── gyri   ← THIS PACKAGE

This is a **gyral-collection parent** of the right occipital lobe — a
registry package whose children are the **lateral-surface gyri** of
the occipital convexity. It is the **gyral** counterpart of
``..brodmann_areas`` (the cytoarchitectonic parent), ``..cortex`` (the
functional / V-numbered parent), and ``..sulci`` (the sulcal parent),
and it sits **alongside** them as a direct child of ``..occipital``.

Parent: ``..occipital`` — the right occipital lobe. Sibling to
``..brodmann_areas``, ``..cortex``, ``..cuneus``, and ``..sulci``.

This package is the **structural mirror** of
``../../left/cortex/occipital/gyri``. The gyrus child, its bounding
sulci, its functional overlays, and its lateral-surface placement are
identical on both sides; the **functional emphasis** and **clinical
significance** diverge — on the right, the lateral occipital gyrus's
V3d / V4d / LOC territory feeds the **right FFA (face)** endpoint,
and right lateral-occipital-gyrus lesions produce **prosopagnosia**,
**visuospatial deficits**, and **left hemispatial neglect** (via the
LOC → FFA and LOC → right IPS pathways). The right lateral occipital
gyrus's V3d territory is the **dominant motion-boundary and depth-
from-motion substrate** in the human brain. The left lateral
occipital gyrus feeds the **left VWFA (reading)** endpoint, and left
lateral-occipital-gyrus lesions produce **visual object agnosia**,
**reading-related deficits**, and **color-form processing deficits**
that have no symmetric counterpart on the right at the same
weighting.

Direct children (1)
-------------------
::

    gyri
    └── lateral_occipital_gyrus   [lateral occipital gyri, V3d/V4d/LOC]

**This is a single-child parent in the current tree.** The **lateral
occipital gyrus** is the only lateral-surface gyrus of the occipital
lobe that has been promoted to a package. The other candidate gyri —
the **lingual gyrus** (medial-surface, lower-bank V1/V2) and the
**cuneus** (medial-surface, upper-bank V1/V2) — are **not** children
of this package. The **cuneus** is a direct child of ``..occipital``
itself (see below). The **lingual gyrus** is a **forward reference**
(see the FORWARD-DECLARATION CAVEAT).

**The ``..gyri`` parent is unusual in two respects:**

1. **It is the only occipital parent with a single child.** The other
   occipital parents — ``brodmann_areas`` (3 children),
   ``cortex`` (4 children), ``sulci`` (3 children), and ``cuneus``
   (0 children, a leaf) — have more substantial child sets. The
   ``gyri`` parent's single child reflects the fact that **most
   occipital gyri are either medial-surface landmarks** (cuneus,
   lingual gyrus) **or functional territories** (the V areas in
   ``..cortex``), **not lateral-surface gyral folds**. The lateral
   occipital gyrus is the **only** classical lateral-surface gyrus
   of the occipital lobe that is modelled as a gyrus rather than as
   a V area.

2. **The cuneus is not a child of this package.** The cuneus is a
   medial-surface gyrus, and its primary functional identity is the
   V1 upper-bank surface landmark — which is why it sits at the
   ``..occipital`` parent level (alongside this package) rather than
   under it. See the ``..cuneus`` package for the full rationale.

--------------------------------------------------------------------------------
THE CUNEUS EXCLUSION — WHY THE CUNEUS IS NOT HERE
--------------------------------------------------------------------------------

The **cuneus** is a gyrus, and a naive decomposition might expect it
to be a child of ``..gyri``. **It is not**, and the reason is
structural:

  * The cuneus's primary functional identity is the **V1 upper-bank
    surface landmark** — its lower margin is the upper bank of the
    calcarine sulcus, carrying the dorsal V1 representation of the
    lower contralateral visual field.
  * The cuneus's **functional overlays are V1, V2, and V3d** — three
    different V areas — and its role is inseparable from the
    **calcarine sulcus** anatomy that defines V1's upper bank.
  * Placing the cuneus under ``..gyri`` would force it to be treated
    as a generic gyral fold, losing its status as a **surface
    landmark for primary sensory cortex**.

**The lateral occipital gyrus's placement under ``..gyri`` is
different.** The lateral occipital gyrus is a **lateral-surface gyral
fold** whose **primary functional overlays are V3d, V4d, and LOC** —
**three extrastriate and association areas, not primary sensory
cortex**. The lateral occipital gyrus is structurally a **gyral fold**
first and a **functional overlay** second, whereas the cuneus is a
**surface landmark for primary sensory cortex** first and a gyral fold
second.

**The ``..cuneus`` package's own docstring documents this rationale
in full**, and the two packages cross-reference each other:
``..gyri`` lists the cuneus as a **parent-level sibling** (not a
child), and ``..cuneus`` lists ``..gyri`` as a **parent-level
sibling** (not a parent).

**This cuneus-exclusion rationale is byte-identical to the left
sibling's** — it is a property of the occipital lobe's anatomy, not
of the hemisphere.

--------------------------------------------------------------------------------
DIRECT CHILDREN — SPEC
--------------------------------------------------------------------------------

1. lateral_occipital_gyrus
   ~~~~~~~~~~~~~~~~~~~~~~~~
   The **lateral occipital gyri** — the lateral-surface gyral folds
   of the right occipital lobe, on the **lateral occipital
   convexity** between the **parieto-occipital sulcus** (rostrally)
   and the **occipital pole** (caudally), and between the **temporal
   lobe** (ventrolaterally) and the **parietal lobe**
   (dorsolaterally).

   **The lateral occipital gyri are sometimes subdivided** into
   **superior**, **middle**, and **inferior** lateral occipital
   gyri in some parcellations, but the current tree keeps them as a
   **single gyrus package** because the **functional overlays are
   continuous** across the three subdivisions.

   **Functional overlays** (identical on both hemispheres):
       V3d (lateral V3)     the **motion-boundary and motion-in-
                            depth** area, at the caudal / dorsal
                            extent of the lateral occipital
                            gyrus. **On the right, V3d is the
                            DOMINANT motion substrate** — the
                            right V3d → right MT/V5 → right
                            IPS pathway is the dominant
                            motion-boundary and dorsal-attention
                            substrate.
       V4d (lateral V4)     the **color-form and surface-
                            segmentation** area, at the mid /
                            lateral extent. **On the right, V4d
                            feeds the right LOC → right FFA
                            face pathway.**
       LOC (lateral occipital   the **object-recognition complex**,
       complex; forward         at the rostral extent. **LOC is a
       reference)               forward reference** — not yet a
                                package under ``..cortex``.
                                **On the right, LOC feeds the
                                right FFA (faces).**
       MT/V5 (nearby,           the **motion area**, at the
       forward reference)       occipito-temoral junction near
                                the caudal lateral occipital
                                gyrus. **MT/V5 is a forward
                                reference** — not yet a package.
                                **On the right, MT/V5 is the
                                DOMINANT motion hemisphere.**

   **Bounding sulci:**
       rostrally             parieto-occipital sulcus (medial) /
                             an imaginary line from the parieto-
                             occipital sulcus to the preoccipital
                             notch (lateral)
       caudally              occipital pole (caudal convergence of
                             the lateral occipital gyrus and the
                             cuneus / lingual gyrus)
       dorsally              transverse occipital sulcus (the
                             dorsal boundary of the lateral
                             occipital gyri, separating them from
                             the parietal lobe)
       ventrally             lateral occipitotemporal sulcus /
                             occipitotemporal junction (the
                             boundary with the temporal lobe)

   **The lateral occipital gyrus is continuous with the fusiform
   gyrus ventrally.** **On the right, the fusiform gyrus is where
   the right FFA lives** (downstream of the right LOC); the lateral
   occipital gyrus is the **upstream LOC territory** that feeds the
   FFA. **The two together form the right face-recognition
   pathway's lateral / ventral territory.**

   **On the left, the lateral occipital gyrus is continuous with
   the left fusiform gyrus**, where the **left VWFA lives**. The
   left lateral occipital gyrus is the **upstream LOC territory**
   that feeds the left VWFA.

--------------------------------------------------------------------------------
FORWARD REFERENCES
--------------------------------------------------------------------------------

**The lingual gyrus** is a **forward reference** — not yet a package
in the current tree. When it is created, it should be placed **either**
under ``..gyri`` (as a **medial-surface gyral child**, alongside the
lateral occipital gyrus) **or** at the ``..occipital`` parent level
(as a **medial-surface surface landmark for V1's lower bank**,
alongside the cuneus). **The placement decision must preserve the
cuneus / lingual gyrus symmetry** — the two gyri are the upper and
lower banks of the calcarine sulcus, and their placements should be
symmetric.

**The superior / middle / inferior lateral occipital gyri** are
**forward references** — not yet packaged. **The current tree keeps
the lateral occipital gyrus as a single gyrus** because the V3d /
V4d / LOC overlays span the full extent without clean anatomical
breaks.

**The LOC (lateral occipital complex) is a forward reference** — not
yet a package under ``..cortex``. **LOC overlaps the lateral
occipital gyrus** and extends into the fusiform gyrus. **It is a
functional territory, not a gyral one** — it lives in ``..cortex``
as a V-area forward reference, not here as a gyral child.

**The MT/V5 (motion area) is a forward reference** — not yet a
package under ``..cortex``. **MT/V5 overlaps the caudal lateral
occipital gyrus** near the occipito-temporal junction. **On the
right, MT/V5 is the DOMINANT motion hemisphere**, and creating it is
the most urgent future V-area resolution for the dorsal stream.

**All forward references are byte-identical to the right sibling's**
— they are properties of the occipital lobe's anatomy, not of the
hemisphere. **The right's emphasis note on MT/V5's dominance is
added** and is consistent with the right `..cortex` parent's
forward-reference caveat.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAIN COVERAGE — WHAT THE LATERAL OCCIPITAL GYRUS CARRIES
--------------------------------------------------------------------------------

The **lateral occipital gyrus** is a **gyral territory** that
overlaps three functional areas — **V3d** (motion-boundary /
motion-in-depth), **V4d** (color-form / surface segmentation), and
the **LOC** (object recognition) — plus **MT/V5** at its caudal
margin. Its functional domain coverage is therefore:

    Covered domains (via the overlays):
        spatial_localization       (V3d — motion boundaries,
                                    depth from motion; **the
                                    right's contribution is
                                    DOMINANT** — the right
                                    V3d is the dominant
                                    motion-in-space substrate)
        color_vision               (V4d — color-form, surface
                                    segmentation)
        form_and_object_perception (V4d and LOC — object
                                    recognition; **the right's
                                    contribution feeds the right
                                    FFA face pathway**)

    Not covered (live in other overlays):
        primary_visual_processing  (V1 — calcarine banks)
        binocular_vision           (V1, V2, V3v)
        motion_perception          (MT/V5 — forward reference in
                                    ``..cortex``; **on the right,
                                    the dominant motion
                                    substrate**)
        visual_attention           (target role, not a generator;
                                    **right V3d → right MT/V5
                                    → right IPS is the dominant
                                    dorsal-attention substrate**)
        visual_word_processing     (left VWFA — downstream in
                                    the left fusiform gyrus, not
                                    the right lateral occipital
                                    gyrus)
        face_processing            (right FFA — downstream in
                                    the right fusiform gyrus, not
                                    the right lateral occipital
                                    gyrus)
        global_visual_processing   (right V2 — not the lateral
                                    occipital gyrus)

**The lateral occipital gyrus does not carry the reading or face
domains directly** — those live downstream in the fusiform gyrus
(left VWFA / right FFA). **The lateral occipital gyrus is the
upstream LOC territory** that feeds those downstream endpoints.
**On the right, the lateral occipital gyrus's LOC is the upstream
input to the right FFA (faces); on the left, the same LOC is the
upstream input to the left VWFA (reading).**

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..occipital  (parent)
    The right occipital lobe. This package's parent (alongside
    ``..cuneus``, ``..brodmann_areas``, ``..cortex``, and
    ``..sulci``).

..brodmann_areas
    The **cytoarchitectonic sibling**. **The lateral occipital
    gyrus overlaps BA 19** (the only occipital BA that contains
    V3d, V4d, and LOC). **The BA 19 package** must cross-reference
    the lateral occipital gyrus as its primary lateral-surface
    anatomical substrate.

..cortex
    The **functional sibling**. **The lateral occipital gyrus
    overlaps V3d, V4d, and the LOC.** **On the right, V3d is the
    DOMINANT motion substrate**, and the right lateral occipital
    gyrus's LOC feeds the right FFA. When V3d, V4d, and LOC are
    created as packages under ``..cortex``, they must
    cross-reference the right lateral occipital gyrus as their
    primary lateral-surface anatomical substrate.

..cuneus
    The **medial-surface sibling** (a parent-level sibling, not a
    child of ``..gyri``). The cuneus is the **upper bank of the
    calcarine sulcus** (V1 dorsal bank); the lateral occipital
    gyrus is the **lateral surface of the occipital lobe**. They
    are **different surfaces of the same lobe** — medial vs
    lateral — and they are placed at **different levels of the
    tree** because their primary functional identities differ.

..sulci
    The **sulcal sibling**. The **transverse occipital sulcus**
    bounds the lateral occipital gyri dorsally; the **lateral
    occipitotemporal sulcus** bounds them ventrally; the
    **parieto-occipital sulcus** bounds them rostrally (medially).
    The ``..sulci`` package cross-references the lateral
    occipital gyri as one of their bounding gyri.

..sulci.calcarine_sulcus
    The **calcarine sulcus is NOT a boundary of the lateral
    occipital gyrus** — it is the boundary of the **cuneus** and
    **lingual gyrus**. The lateral occipital gyrus is on the
    lateral surface, not the medial surface.

..sulci.transverse_occipital_sulcus
    The **dorsal boundary** of the lateral occipital gyri,
    separating them from the parietal lobe's angular gyrus.

..sulci.lateral_occipitotemporal_sulcus (if/when created)
    The **ventral boundary** of the lateral occipital gyri,
    separating them from the fusiform gyrus.

..cortex.temporal
    The **ventral stream** continues from the lateral occipital
    gyrus's LOC territory into the temporal lobe (fusiform gyrus,
    left VWFA / right FFA). **On the right, the lateral occipital
    gyrus's LOC → fusiform → right FFA pathway is the face
    pathway.** **On the left, the lateral occipital gyrus's LOC
    → fusiform → left VWFA pathway is the reading pathway.**
    **Right occipito-temporal lesions produce prosopagnosia** —
    the canonical right-lateralized visual-recognition deficit.

..cortex.parietal
    The **dorsal stream** continues from the lateral occipital
    gyrus's V3d territory (via MT/V5 → IPS) into the parietal
    lobe. **On the right, the lateral occipital gyrus's V3d
    contribution is the DOMINANT dorsal-attention substrate** —
    the right V3d → right MT/V5 → right IPS pathway is the
    dominant motion-boundary and spatial-attention substrate.
    The parietal package must declare the right lateral occipital
    gyrus as a **source of upstream V3d input** to its dorsal
    attention network children.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral
    prefrontal cortex** (BA 9 / BA 46) send top-down visual
    attentional signals to the lateral occipital gyrus's V3d /
    V4d territory. **On the right, the right FEF is the dominant
    node of the ventral attention network**, and right frontal
    lesions contribute to left hemispatial neglect.

..cortex.cingulate  — indirect
    No direct cingulate → lateral occipital gyrus projection.

..cortex.insular  — indirect
    No direct insular → lateral occipital gyrus projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the **indirect** source of the lateral
    occipital gyrus's V3d / V4d input via the V1 → V2 → V3 → V4
    relay.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **strong modulatory projection** to the
    lateral occipital gyrus's V3d / V4d territory.

../../subcortical/medial_temporal_lobe/hippocampus
    The lateral occipital gyrus's LOC output reaches the
    hippocampus via the ventral stream (LOC → fusiform → perirhinal
    → hippocampus). **On the right, the parahippocampal place
    area (PPA) and the retrosplenial complex receive visual input
    supporting scene and spatial memory**, which are more
    strongly right-lateralized. The right lateral occipital
    gyrus's LOC → fusiform → right FFA pathway is part of the
    right face-recognition system.

../../left/cortex/occipital/gyri
    The left-hemisphere homologue. Structural fields (GYRI
    registry, lateral occipital gyrus child name, bounding sulci,
    functional overlays V3d / V4d / LOC, cuneus exclusion note,
    lingual gyrus forward-reference caveat text) MUST be
    byte-identical. Functional emphasis and clinical significance
    diverge — the left lateral occipital gyrus's V4d / LOC
    territory feeds the **left VWFA (reading)** endpoint, and
    left lateral-occipital-gyrus lesions produce **visual object
    agnosia**, **reading-related deficits**, and **color-form
    processing deficits** that have no symmetric counterpart on
    the right at the same weighting.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    LOBE                = "occipital"
    HEMISPHERE          = "right"

    GYRI_CHILDREN       = (
                              "lateral_occipital_gyrus",
                          )
        # **Byte-identical to the left sibling's.** A single-
        # child parent; the cuneus and the lingual gyrus are
        # not children.

    GYRI_TO_V_OVERLAYS  = {
        # **Byte-identical to the left sibling's.**
        "lateral_occipital_gyrus": (
            "v3",     # V3d
            "v4",     # V4d
            "LOC",    # forward reference in ..cortex
        ),
    }

    GYRI_TO_BA_OVERLAYS = {
        # **Byte-identical to the left sibling's.**
        "lateral_occipital_gyrus": (19,),
    }

    EXCLUDED_GYRI       = {
        # **Byte-identical to the left sibling's.**
        "cuneus": "parent-level sibling — medial-surface V1 "
                  "upper-bank surface landmark",
        "lingual_gyrus": "forward reference — medial-surface "
                         "V1 lower-bank surface landmark",
    }

    VISUAL_HEMIFIELD    = "left"
        # **The represented visual hemifield** for the right
        # lateral occipital gyrus's V3d / V4d / LOC territory.
        # The right lateral occipital gyrus's overlays carry
        # the **left** hemifield on the right side.

    RIGHT_LATERALIZED_FUNCTIONS = (
        "left_hemifield_lower_field_loc_to_right_ffa",
    )
        # The right lateral occipital gyrus's LOC territory
        # feeds the **right FFA face pathway**. **This is the
        # mirror of the left's `LEFT_LATERALIZED_FUNCTIONS`
        # `right_hemifield_lower_field_loc_to_left_vwfa`.**
        # **This is a left-hemisphere-specific absence on the
        # left side** (the left lateral occipital gyrus feeds
        # the left VWFA, not a face pathway).

    LEFT_ONLY_DOMAINS   = (
        "right_hemifield_lower_field_loc_to_left_vwfa",
    )
        # The left-only function that the right lateral
        # occipital gyrus does **not** carry. **This is the
        # mirror of the left's `RIGHT_ONLY_DOMAINS`
        # `face_processing`.**

    FORWARD_REFERENCE_GYRI = (
        "lingual_gyrus",
        "superior_lateral_occipital_gyrus",
        "middle_lateral_occipital_gyrus",
        "inferior_lateral_occipital_gyrus",
    )
        # **Byte-identical to the left sibling's.**

    FORWARD_REFERENCE_V_AREAS = (
        "V3d",
        "V4d",
        "LOC",
        "V5_MT_plus",
    )
        # **Byte-identical to the left sibling's and to the
        # sibling ..cortex / ..brodmann_areas forward-reference
        # lists.**

    CUNEUS_EXCLUSION_NOTE = (
        "The cuneus is NOT a child of this package. It sits at "
        "the ..occipital parent level because its primary "
        "functional identity is the V1 upper-bank surface "
        "landmark, not a generic gyral fold. See ..cuneus."
    )
        # **Byte-identical to the left sibling's.**

    LINGUAL_GYRUS_PLACEMENT_CAVEAT = (
        "The lingual gyrus is a forward reference. When created, "
        "it should be placed either at the ..occipital parent "
        "level (like the cuneus) or under ..gyri — the decision "
        "must preserve the cuneus / lingual gyrus symmetry, "
        "because the two gyri are the upper and lower banks of "
        "the calcarine sulcus."
    )
        # **Byte-identical to the left sibling's.**

    __all__ = [
        "LOBE",
        "HEMISPHERE",
        "GYRI_CHILDREN",
        "GYRI_TO_V_OVERLAYS",
        "GYRI_TO_BA_OVERLAYS",
        "EXCLUDED_GYRI",
        "VISUAL_HEMIFIELD",
        "RIGHT_LATERALIZED_FUNCTIONS",
        "LEFT_ONLY_DOMAINS",
        "FORWARD_REFERENCE_GYRI",
        "FORWARD_REFERENCE_V_AREAS",
        "CUNEUS_EXCLUSION_NOTE",
        "LINGUAL_GYRUS_PLACEMENT_CAVEAT",
    ]

No behaviour. This package is a declarative registry; all
computation that references the lateral occipital gyrus lives in
``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``gyri/__init__.py`` must:

1. Import the single gyrus child (no side effects):
       from . import lateral_occipital_gyrus

2. Expose a registry of gyral children:

       OCCIPITAL_GYRI = {
           "lateral_occipital_gyrus": lateral_occipital_gyrus,
       }

3. Expose the **gyrus → V overlay** index (byte-identical to the
   left sibling's).

4. Expose the **gyrus → BA overlay** index (byte-identical to the
   left sibling's).

5. Expose ``EXCLUDED_GYRI`` with the cuneus and lingual gyrus
   exclusions and their reasons (byte-identical to the left
   sibling's).

6. Expose ``FORWARD_REFERENCE_GYRI`` and
   ``FORWARD_REFERENCE_V_AREAS`` as the forward-reference lists
   (byte-identical to the left sibling's).

7. Expose the cuneus exclusion note and the lingual gyrus placement
   caveat as first-class strings (byte-identical to the left
   sibling's).

8. Expose ``VISUAL_HEMIFIELD`` = ``"left"`` for the right lateral
   occipital gyrus's V3d / V4d / LOC territory.

9. Expose ``RIGHT_LATERALIZED_FUNCTIONS`` and ``LEFT_ONLY_DOMAINS``
   as the right-lateralized downstream function and the left-only
   downstream function associated with the gyri in this package.
   **The complementarity invariant holds**:
   - left.LEFT_LATERALIZED_FUNCTIONS (mirror) = right.RIGHT_
     LATERALIZED_FUNCTIONS
   - left.RIGHT_ONLY_DOMAINS (mirror) = right.LEFT_ONLY_DOMAINS

10. Define ``__all__`` as shown in the implementation contract.

11. Contain **no** logic beyond the above.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are four forward references for this package**, and they are
byte-identical to the left sibling's:

1. **Lingual gyrus** — a medial-surface gyrus that carries the
   lower-bank V1 / V2 representation. The placement decision
   (parent level vs under ``..gyri``) must preserve the cuneus /
   lingual gyrus symmetry.

2. **Superior lateral occipital gyrus** — a forward reference if
   the lateral occipital gyrus is ever subdivided.

3. **Middle lateral occipital gyrus** — same as #2.

4. **Inferior lateral occipital gyrus** — same as #2.

**In addition, four V-area forward references are associated with
the lateral occipital gyrus's overlays**: **V3d**, **V4d**,
**LOC**, and **MT/V5**. **On the right, resolving MT/V5 and V3d is
the most urgent future V-area work** — they are the dominant
motion and dorsal-attention substrates in the human brain, and the
right lateral occipital gyrus's V3d contribution is only fully
characterised when those areas are modelled. **Resolving LOC is
required for the right face-recognition pathway's occipital input
to be fully characterised**, because the right LOC → right FFA
pathway is the substrate of the prosopagnosia contribution anchor.

**All forward references are byte-identical to the left sibling's.**
**The lingual gyrus placement caveat is byte-identical to the left
sibling's** — the placement question is a property of the
occipital lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a lateral occipital sub-region becomes a
package)
--------------------------------------------------------------------------------

The lateral occipital gyrus is **the only lateral-surface gyrus of
the occipital lobe**, and it is **architectonically continuous**
across its anteroposterior extent. **The one natural split is the
superior / middle / inferior lateral occipital gyrus triad.**

**If a future parcellation promotes the three-way split**, the
promotion takes this form:

    gyri/
        __init__.py
        lateral_occipital_gyrus/
            __init__.py
            superior_lateral_occipital_gyrus/    # V3d
                __init__.py
            middle_lateral_occipital_gyrus/      # V4d
                __init__.py
            inferior_lateral_occipital_gyrus/    # LOC
                __init__.py

Then:

  1. Add the three component names to the
     ``lateral_occipital_gyrus`` package's ``SUBDIVISIONS``.
  2. Update the ``lateral_occipital_gyrus`` package's
     ``GYRI_TO_V_OVERLAYS`` to reflect the per-subdivision
     overlays (superior → V3d, middle → V4d, inferior → LOC).
  3. Update the parent ``..gyri``'s ``GYRI_TO_V_OVERLAYS``
     index accordingly.
  4. Mirror the promotion on the left side in the same commit.

**The split preserves the cuneus exclusion** — the cuneus remains
a parent-level sibling.

**On the right, the V3d subdivision is the dominant motion
substrate**, and the LOC subdivision is the upstream input to the
right FFA face pathway. **No split should be performed while LOC
and MT/V5 are unresolved.**

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/cortex/occipital/gyri``:

    MUST be identical (byte-for-byte):
        LOBE                         "occipital"
        GYRI_CHILDREN                ("lateral_occipital_gyrus",)
        GYRI_TO_V_OVERLAYS           same gyrus → V-area overlays
        GYRI_TO_BA_OVERLAYS          same gyrus → BA-19 overlays
        EXCLUDED_GYRI                same cuneus / lingual gyrus
                                     exclusions
        FORWARD_REFERENCE_GYRI       same four forward references
        FORWARD_REFERENCE_V_AREAS    same four V areas
        CUNEUS_EXCLUSION_NOTE        byte-identical
        LINGUAL_GYRUS_PLACEMENT_CAVEAT
                                     byte-identical
        The lateral occipital gyrus package's structural
                                     fields (bounds, overlays,
                                     forward references)
        The bounding sulci

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        RIGHT_LATERALIZED_FUNCTIONS
                               right: ("left_hemifield_lower_
                               field_loc_to_right_ffa",) — the
                               right lateral occipital gyrus's
                               LOC feeds the right FFA face
                               pathway.
                               left: () — the left lateral
                               occipital gyrus does not
                               contribute to the right face
                               pathway.
        LEFT_ONLY_DOMAINS      right: ("right_hemifield_lower_
                               field_loc_to_left_vwfa",) — the
                               left-only function the right
                               lateral occipital gyrus does
                               not carry.
                               left: () — the left lateral
                               occipital gyrus uses RIGHT_ONLY_
                               DOMAINS instead.
        CLINICAL_ANCHORS       right: **prosopagnosia
                               contribution**, **visuospatial
                               deficits**, **left hemispatial
                               neglect** (via LOC → right IPS),
                               **motion-boundary and depth-from-
                               motion deficits MORE SEVERE**
                               (via right V3d), color-form
                               processing deficits (V4d),
                               migraine aura, occipital
                               epilepsy, occipital infarct,
                               PCA (Benson syndrome), PRES.
                               left: visual object agnosia
                               (bilateral), **reading-related
                               deficits** via the LOC → left
                               VWFA pathway, color-form
                               processing deficits (V4d),
                               motion-boundary and depth-from-
                               motion deficits (milder),
                               migraine aura, occipital
                               epilepsy, occipital infarct,
                               PCA, PRES.

**The single-child structure, the lateral occipital gyrus's
overlays, the cuneus exclusion, the forward references, the bounding
sulci, and the caveat text are byte-identical on both sides.**

**The visual-hemifield asymmetry is the sharpest single entry.**
The right lateral occipital gyrus's V3d / V4d / LOC territory
represents the **left** hemifield.

**The downstream network asymmetry is the second sharpest entry.**
The right lateral occipital gyrus's LOC feeds the **right FFA face**
endpoint; the left lateral occipital gyrus's LOC feeds the **left
VWFA reading** endpoint. The `RIGHT_LATERALIZED_FUNCTIONS` /
`LEFT_ONLY_DOMAINS` tuples make this explicit, and the two
contributions are mirror-opposite.

**The right-specific clinical anchors are the third sharpest
entry.** The right lateral occipital gyrus carries three anchors
that the left does not carry at the same weighting:
`right_lateral_occipital_prosopagnosia_contribution`,
`right_lateral_occipital_visuospatial_deficit`, and
`right_lateral_occipital_left_hemifield_neglect_contribution`. The
right lateral occipital gyrus also carries the **more severe**
motion-boundary and depth-from-motion deficits (the right V3d is
the dominant motion substrate).

**The complementarity invariant is verified across schemes.** The
left's `LEFT_LATERALIZED_FUNCTIONS` (mirror) equals the right's
`RIGHT_LATERALIZED_FUNCTIONS`, and the left's `RIGHT_ONLY_DOMAINS`
(mirror) equals the right's `LEFT_ONLY_DOMAINS`.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/gyri/`` (right) — a
    sibling of ``brodmann_areas``, ``cortex``, ``cuneus``, and
    ``sulci``.
[ ] The single gyrus child (``lateral_occipital_gyrus``) is
    imported and registered.
[ ] ``GYRI_CHILDREN`` is byte-identical to the left sibling's.
[ ] ``GYRI_TO_V_OVERLAYS`` is byte-identical to the left
    sibling's (lateral_occipital_gyrus → v3, v4, LOC).
[ ] ``GYRI_TO_BA_OVERLAYS`` is byte-identical to the left
    sibling's (lateral_occipital_gyrus → (19,)).
[ ] ``EXCLUDED_GYRI`` is byte-identical to the left sibling's
    (cuneus → parent-level sibling; lingual gyrus → forward
    reference).
[ ] **The cuneus exclusion is documented** — the cuneus is not
    a child of ``..gyri``, and the reason (V1 upper-bank surface
    landmark) is stated explicitly.
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class
    field.
[ ] ``RIGHT_LATERALIZED_FUNCTIONS`` contains
    "left_hemifield_lower_field_loc_to_right_ffa" — the right
    lateral occipital gyrus's LOC feeds the right FFA face
    pathway.
[ ] ``LEFT_ONLY_DOMAINS`` contains
    "right_hemifield_lower_field_loc_to_left_vwfa" — the
    left-only function the right lateral occipital gyrus does
    **not** carry.
[ ] **The complementarity invariant is verified**: the left's
    `LEFT_LATERALIZED_FUNCTIONS` (mirror) equals the right's
    `RIGHT_LATERALIZED_FUNCTIONS`, and the left's `RIGHT_ONLY_
    DOMAINS` (mirror) equals the right's `LEFT_ONLY_DOMAINS`.
[ ] ``FORWARD_REFERENCE_GYRI`` and ``FORWARD_REFERENCE_V_AREAS``
    are present and byte-identical to the left sibling's.
[ ] ``CUNEUS_EXCLUSION_NOTE`` and
    ``LINGUAL_GYRUS_PLACEMENT_CAVEAT`` are byte-identical to the
    left sibling's.
[ ] **The right's MT/V5 and V3d dominance is documented** — the
    right lateral occipital gyrus's V3d territory is the
    dominant motion-boundary and depth-from-motion substrate,
    and MT/V5 is the dominant motion hemisphere.
[ ] **The right's LOC → right FFA pathway is documented** — the
    right lateral occipital gyrus's LOC is the upstream input
    to the right FFA face-recognition system.
[ ] **The lateral occipital gyrus does NOT carry the reading or
    face domains directly** — those live downstream in the
    fusiform gyrus (left VWFA / right FFA). The lateral
    occipital gyrus is the upstream LOC territory.
[ ] **The right lateral occipital gyrus → right fusiform gyrus
    continuity** is documented.
[ ] **The transverse occipital sulcus** is documented as the
    dorsal boundary.
[ ] **The lateral occipitotemporal sulcus** is documented as the
    ventral boundary.
[ ] **The parieto-occipital sulcus** is documented as the
    rostral (medial) boundary.
[ ] **The calcarine sulcus is explicitly NOT a boundary of the
    lateral occipital gyrus.**
[ ] **The LOC and MT/V5 forward references are documented** —
    they live in ``..cortex`` as V-area forward references,
    not here as gyral children.
[ ] No SUBDIVISIONS promotion is performed while LOC and MT/V5
    are unresolved.
[ ] The **promotion rule for the three-way lateral occipital
    gyrus split** is documented, with the joint ``..cortex``
    update requirement and the downstream LOC / MT/V5
    prerequisites.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (GYRI_CHILDREN, GYRI_TO_V_OVERLAYS, GYRI_TO_BA_OVERLAYS,
    EXCLUDED_GYRI, FORWARD_REFERENCE_GYRI,
    FORWARD_REFERENCE_V_AREAS, CUNEUS_EXCLUSION_NOTE,
    LINGUAL_GYRUS_PLACEMENT_CAVEAT, lateral occipital gyrus's
    bounds and overlays) match the left sibling;
    VISUAL_HEMIFIELD, RIGHT_LATERALIZED_FUNCTIONS,
    LEFT_ONLY_DOMAINS, and CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    lateral occipital gyrus carries "left_hemifield"; the left
    carries "right_hemifield."
[ ] **The reading-vs-face downstream asymmetry is verified**:
    the right lateral occipital gyrus carries "left_hemifield_
    lower_field_loc_to_right_ffa" and the left carries
    "right_hemifield_lower_field_loc_to_left_vwfa" — the two
    are mirror-opposite.
[ ] **The right-specific clinical anchors are verified**:
    `right_lateral_occipital_prosopagnosia_contribution`,
    `right_lateral_occipital_visuospatial_deficit`,
    `right_lateral_occipital_left_hemifield_neglect_contribution`,
    and the **more severe** motion-boundary / depth-from-motion
    deficits are present on the right and absent on the left.
    The left-only
    `left_lateral_occipital_reading_related_deficit` and
    `left_lateral_occipital_visual_object_agnosia` are absent
    on the right.
[ ] Any downstream code querying "what gyri are in the right
    occipital lobe's ``..gyri`` package?" must receive
    "only `lateral_occipital_gyrus` — the cuneus is at the
    parent level, and the lingual gyrus is a forward
    reference."
[ ] Any downstream code querying "what does the right lateral
    occipital gyrus see?" must receive "the LEFT visual
    hemifield."
[ ] Any downstream code querying "what does the right lateral
    occipital gyrus feed?" must receive "the right LOC, and
    from there the right FFA (faces)" — the right lateral
    occipital gyrus is the upstream LOC input.
[ ] Any downstream code querying "what does the left lateral
    occipital gyrus feed?" must receive "the left LOC, and
    from there the left VWFA (reading)" (documented in the
    left sibling).
[ ] Any downstream code assigning the right face pathway must
    route through the right lateral occipital gyrus's LOC →
    right fusiform gyrus → right FFA chain.
[ ] Any downstream code assigning the left reading pathway must
    route through the left lateral occipital gyrus's LOC →
    left fusiform gyrus → left VWFA chain.
[ ] Any downstream code assigning prosopagnosia must route
    through the **right** lateral occipital gyrus's LOC →
    right FFA pathway.
[ ] Any downstream code assigning left hemispatial neglect must
    note that **the right lateral occipital gyrus's LOC →
    right IPS pathway is a contributor**, not a sole cause.
[ ] Any downstream code assigning motion-boundary or
    depth-from-motion processing must weight the **right
    lateral occipital gyrus's V3d territory more heavily**
    than the left's — the right V3d is the dominant motion
    substrate.
[ ] **The cuneus exclusion note and the lingual gyrus placement
    caveat are byte-identical to the left sibling's.**
"""