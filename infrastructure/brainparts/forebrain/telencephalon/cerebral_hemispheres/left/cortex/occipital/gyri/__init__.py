"""
Occipital Gyri — Left Hemisphere
=================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── gyri   ← THIS PACKAGE

This is a **gyral-collection parent** of the left occipital lobe — a
registry package whose children are the **lateral-surface gyri** of
the occipital convexity. It is the **gyral** counterpart of
``..brodmann_areas`` (the cytoarchitectonic parent), ``..cortex`` (the
functional / V-numbered parent), and ``..sulci`` (the sulcal parent),
and it sits **alongside** them as a direct child of ``..occipital``.

Parent: ``..occipital`` — the left occipital lobe. Sibling to
``..brodmann_areas``, ``..cortex``, ``..cuneus``, and ``..sulci``.

This package is the **structural mirror** of
``../../right/cortex/occipital/gyri``. The gyrus child, its bounding
sulci, its functional overlays, and its lateral-surface placement are
identical on both sides; the **functional emphasis** and **clinical
significance** diverge — on the left, the lateral occipital gyrus's
V4d / LOC territory feeds the **left VWFA (reading)** endpoint, and
left lateral-occipital-gyrus lesions produce **visual object agnosia**,
**reading-related deficits**, and **color-form processing deficits**
that have no symmetric counterpart on the right at the same
weighting. The right lateral occipital gyrus feeds the **right FFA
(face)** endpoint, and right lateral-occipital-gyrus lesions produce
**prosopagnosia**, **visuospatial deficits**, and **left hemispatial
neglect** (via the LOC → FFA and LOC → right IPS pathways).

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
second. **The two gyri sit at different levels of the tree for
different structural reasons**, and the cuneus's placement is not an
oversight — it is the **correct decomposition** for a primary-sensory
surface landmark.

**The ``..cuneus`` package's own docstring documents this rationale
in full**, and the two packages cross-reference each other:
``..gyri`` lists the cuneus as a **parent-level sibling** (not a
child), and ``..cuneus`` lists ``..gyri`` as a **parent-level
sibling** (not a parent).

--------------------------------------------------------------------------------
DIRECT CHILDREN — SPEC
--------------------------------------------------------------------------------

1. lateral_occipital_gyrus
   ~~~~~~~~~~~~~~~~~~~~~~~~
   The **lateral occipital gyri** — the lateral-surface gyral folds
   of the occipital lobe, on the **lateral occipital convexity**
   between the **parieto-occipital sulcus** (rostrally) and the
   **occipital pole** (caudally), and between the **temporal lobe**
   (ventrolaterally) and the **parietal lobe** (dorsolaterally).

   **The lateral occipital gyri are sometimes subdivided** into
   **superior**, **middle**, and **inferior** lateral occipital
   gyri in some parcellations (analogous to the frontal lobe's
   SFG/MFG/IFG triad), but the current tree keeps them as a
   **single gyrus package** because the **functional overlays are
   continuous** across the three subdivisions — V3d, V4d, and the
   LOC span the full anteroposterior extent, and the subdivisions
   are not associated with distinct functional territories in the
   way that the frontal gyri are.

   **Functional overlays** (identical on both hemispheres):
       V3d (lateral V3)     the **motion-boundary and motion-in-
                            depth** area, at the caudal / dorsal
                            extent of the lateral occipital
                            gyrus. **On the right, V3d is the
                            dominant motion substrate** (right
                            V3d → right MT/V5 → right IPS).
       V4d (lateral V4)     the **color-form and surface-
                            segmentation** area, at the mid /
                            lateral extent. **On the left, V4d
                            feeds the left LOC → left VWFA
                            reading pathway.** **On the right,
                            V4d feeds the right LOC → right FFA
                            face pathway.**
       LOC (lateral occipital   the **object-recognition complex**,
       complex; forward         at the rostral extent. **LOC is a
       reference)               forward reference** — not yet a
                                package under ``..cortex``.
                                **On the left, LOC feeds the left
                                VWFA (reading).** **On the right,
                                LOC feeds the right FFA (faces).**
       MT/V5 (nearby,           the **motion area**, at the
       forward reference)       occipito-temporal junction near
                                the caudal lateral occipital
                                gyrus. **MT/V5 is a forward
                                reference** — not yet a package.

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
   gyrus ventrally** — the lateral occipital gyrus transitions into
   the fusiform gyrus at the **lateral occipitotemporal sulcus**.
   **On the left, the fusiform gyrus is where the left VWFA lives**
   (downstream of the left LOC); the lateral occipital gyrus is the
   **upstream LOC territory** that feeds the VWFA. **The two
   together form the left reading pathway's lateral / ventral
   territory.**

   **On the right, the lateral occipital gyrus is continuous with
   the right fusiform gyrus**, where the **right FFA lives**. The
   right lateral occipital gyrus is the **upstream LOC territory**
   that feeds the right FFA.

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

**The superior / middle / inferior lateral occipital gyri** (a
subdivision of the lateral occipital gyrus into three gyral folds in
some parcellations) are **forward references** — not yet packaged.
**The current tree keeps the lateral occipital gyrus as a single
gyrus** because the V3d / V4d / LOC overlays span the full
anteroposterior extent without clean anatomical breaks. **If a future
parcellation promotes the three-way subdivision**, it must be
mirrored on the right in the same commit.

**The LOC (lateral occipital complex) is a forward reference** — not
yet a package under ``..cortex``. **LOC overlaps the lateral
occipital gyrus** and extends into the fusiform gyrus. **It is a
functional territory, not a gyral one** — it lives in ``..cortex``
as a V-area forward reference, not here as a gyral child. When LOC
is created under ``..cortex``, it must cross-reference the lateral
occipital gyrus (and the fusiform gyrus) as its anatomical
substrates.

**The MT/V5 (motion area) is a forward reference** — not yet a
package under ``..cortex``. **MT/V5 overlaps the caudal lateral
occipital gyrus** near the occipito-temporal junction. **It is a
functional territory, not a gyral one** — it lives in ``..cortex``
as a V-area forward reference, not here as a gyral child.

**All forward references are byte-identical to the left sibling's**
— they are properties of the occipital lobe's anatomy, not of the
hemisphere.

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
                                    left's contribution is
                                    weaker than the right's**)
        color_vision               (V4d — color-form, surface
                                    segmentation)
        form_and_object_perception (V4d and LOC — object
                                    recognition; **the left's
                                    contribution feeds the left
                                    VWFA reading pathway**)

    Not covered (live in other overlays):
        primary_visual_processing  (V1 — calcarine banks, not the
                                    lateral occipital gyrus)
        binocular_vision           (V1, V2, V3v — not the lateral
                                    occipital gyrus)
        motion_perception          (MT/V5 — forward reference in
                                    ``..cortex``; not the lateral
                                    occipital gyrus proper)
        visual_attention           (target role, not a generator)
        visual_word_processing     (left VWFA — downstream in
                                    the fusiform gyrus, not the
                                    lateral occipital gyrus)
        face_processing            (right FFA — downstream in the
                                    right fusiform gyrus, not the
                                    lateral occipital gyrus)
        global_visual_processing   (right V2 — not the lateral
                                    occipital gyrus)

**The lateral occipital gyrus does not carry the reading or face
domains directly** — those live downstream in the fusiform gyrus
(left VWFA / right FFA). **The lateral occipital gyrus is the
upstream LOC territory** that feeds those downstream endpoints.
Downstream code that queries "which gyrus carries the reading
pathway?" must receive "**the lateral occipital gyrus is the upstream
input; the VWFA is downstream in the fusiform gyrus**." Similarly for
the face pathway.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..occipital  (parent)
    The left occipital lobe. This package's parent (alongside
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
    overlaps V3d, V4d, and the LOC** — three functional areas that
    are listed in ``..cortex``'s forward references. **When V3d,
    V4d, and LOC are created as packages under ``..cortex``**,
    they must cross-reference the lateral occipital gyrus as their
    primary lateral-surface anatomical substrate.

..cuneus
    The **medial-surface sibling** (a parent-level sibling, not a
    child of ``..gyri``). The cuneus is the **upper bank of the
    calcarine sulcus** (V1 dorsal bank); the lateral occipital
    gyrus is the **lateral surface of the occipital lobe**. They
    are **different surfaces of the same lobe** — medial vs
    lateral — and they are placed at **different levels of the
    tree** (parent level for the cuneus, ``..gyri`` child for the
    lateral occipital gyrus) because their primary functional
    identities differ (surface landmark vs gyral fold).

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
    left VWFA / right FFA). **On the left, the lateral occipital
    gyrus's LOC → fusiform → left VWFA pathway is the reading
    pathway.** **On the right, the lateral occipital gyrus's LOC
    → fusiform → right FFA pathway is the face pathway.** The
    temporal package must declare the left / right lateral
    occipital gyrus as a **source of upstream LOC input** to its
    fusiform gyrus children.

..cortex.parietal
    The **dorsal stream** continues from the lateral occipital
    gyrus's V3d territory (via MT/V5 → IPS) into the parietal
    lobe. **On the right, the lateral occipital gyrus's V3d
    contribution is the dominant dorsal-attention substrate.**
    The parietal package must declare the right lateral occipital
    gyrus as a **source of upstream V3d input** to its dorsal
    attention network children.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral
    prefrontal cortex** (BA 9 / BA 46) send top-down visual
    attentional signals to the lateral occipital gyrus's V3d /
    V4d territory.

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
    → hippocampus). **On the left, the lateral occipital gyrus's
    LOC → fusiform → left VWFA pathway is part of the reading-
    related memory pathway.** **On the right, the LOC → right FFA
    pathway is part of the scene / spatial memory pathway.**

../../right/cortex/occipital/gyri
    The right-hemisphere homologue. Structural fields (GYRI
    registry, lateral occipital gyrus child name, bounding sulci,
    functional overlays V3d / V4d / LOC, cuneus exclusion note,
    lingual gyrus forward-reference caveat text) MUST be
    byte-identical. Functional emphasis and clinical significance
    diverge — the right lateral occipital gyrus's V4d / LOC
    territory feeds the **right FFA (face)** endpoint, and right
    lateral-occipital-gyrus lesions produce **prosopagnosia**,
    **visuospatial deficits**, and **left hemispatial neglect**
    (via the LOC → FFA and LOC → right IPS pathways).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    LOBE                = "occipital"
    HEMISPHERE          = "left"

    GYRI_CHILDREN       = (
                              "lateral_occipital_gyrus",
                          )
        # **A single-child parent in the current tree.** The
        # cuneus and the lingual gyrus are **not** children —
        # the cuneus is a parent-level sibling, and the lingual
        # gyrus is a forward reference.

    GYRI_TO_V_OVERLAYS  = {
        # Which V areas overlap which gyri (the lateral-surface
        # functional overlays)
        "lateral_occipital_gyrus": (
            "v3",     # V3d, via the caudal-dorsal extent
            "v4",     # V4d, via the mid-lateral extent
            "LOC",    # forward reference in ..cortex
        ),
    }

    GYRI_TO_BA_OVERLAYS = {
        # Which BAs overlap which gyri (the lateral-surface
        # cytoarchitectonic overlays)
        "lateral_occipital_gyrus": (19,),
    }

    EXCLUDED_GYRI       = {
        # Gyri that are NOT children of this package, and why
        "cuneus": "parent-level sibling — medial-surface V1 "
                  "upper-bank surface landmark",
        "lingual_gyrus": "forward reference — medial-surface "
                         "V1 lower-bank surface landmark",
    }

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** for the left
        # lateral occipital gyrus's V3d / V4d / LOC territory.
        # The lateral occipital gyrus's overlays carry the
        # **right** hemifield on the left side.

    LEFT_LATERALIZED_FUNCTIONS = (
        "right_hemifield_lower_field_loc_to_left_vwfa",
    )
        # The left lateral occipital gyrus's LOC territory
        # feeds the **left VWFA reading pathway**. **This is a
        # right-hemisphere-specific absence on the right side**
        # (the right lateral occipital gyrus feeds the right
        # FFA, not the left VWFA).

    RIGHT_ONLY_DOMAINS  = (
        "face_processing",
    )
        # The right lateral occipital gyrus's LOC territory
        # feeds the **right FFA face pathway**. **This is a
        # left-hemisphere-specific absence on the left side**
        # (the left lateral occipital gyrus feeds the left
        # VWFA, not a face pathway).

    FORWARD_REFERENCE_GYRI = (
        "lingual_gyrus",
        "superior_lateral_occipital_gyrus",
        "middle_lateral_occipital_gyrus",
        "inferior_lateral_occipital_gyrus",
    )
        # **Byte-identical to the right sibling's.** When
        # created, these must be resolved in the same commit,
        # in both hemispheres. The lingual gyrus must preserve
        # the cuneus / lingual gyrus symmetry.

    FORWARD_REFERENCE_V_AREAS = (
        "V3d",
        "V4d",
        "LOC",
        "V5_MT_plus",
    )
        # **Byte-identical to the right sibling's and to the
        # sibling ..cortex / ..brodmann_areas forward-reference
        # lists.** These are the V areas that overlap the
        # lateral occipital gyrus but are not yet packages.

    CUNEUS_EXCLUSION_NOTE = (
        "The cuneus is NOT a child of this package. It sits at "
        "the ..occipital parent level because its primary "
        "functional identity is the V1 upper-bank surface "
        "landmark, not a generic gyral fold. See ..cuneus."
    )
        # **Byte-identical to the right sibling's.**

    LINGUAL_GYRUS_PLACEMENT_CAVEAT = (
        "The lingual gyrus is a forward reference. When created, "
        "it should be placed either at the ..occipital parent "
        "level (like the cuneus) or under ..gyri — the decision "
        "must preserve the cuneus / lingual gyrus symmetry, "
        "because the two gyri are the upper and lower banks of "
        "the calcarine sulcus."
    )
        # **Byte-identical to the right sibling's.**

    __all__ = [
        "LOBE",
        "HEMISPHERE",
        "GYRI_CHILDREN",
        "GYRI_TO_V_OVERLAYS",
        "GYRI_TO_BA_OVERLAYS",
        "EXCLUDED_GYRI",
        "VISUAL_HEMIFIELD",
        "LEFT_LATERALIZED_FUNCTIONS",
        "RIGHT_ONLY_DOMAINS",
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

3. Expose the **gyrus → V overlay** index:

       GYRI_TO_V_OVERLAYS = {
           "lateral_occipital_gyrus": ("v3", "v4", "LOC"),
       }

   The inversion must fail loudly if a listed V area is not in the
   parent ``..cortex``'s forward-reference list (unless it is a
   current package).

4. Expose the **gyrus → BA overlay** index:

       GYRI_TO_BA_OVERLAYS = {
           "lateral_occipital_gyrus": (19,),
       }

   The inversion must fail loudly if a listed BA is not in the
   parent ``..brodmann_areas``'s child registry.

5. Expose ``EXCLUDED_GYRI`` with the reason for each exclusion. The
   cuneus and the lingual gyrus are explicitly excluded, and their
   exclusion is a **structural choice**, not an oversight.

6. Expose ``FORWARD_REFERENCE_GYRI`` and
   ``FORWARD_REFERENCE_V_AREAS`` as the forward-reference lists for
   the occipital gyral and V-area hierarchies. **Both lists must be
   byte-identical to the right sibling's.**

7. Expose the cuneus exclusion note and the lingual gyrus placement
   caveat as **first-class strings**, so downstream code can query
   them rather than re-deriving the rationale from prose.

8. Expose ``VISUAL_HEMIFIELD`` = ``"right"`` for the left lateral
   occipital gyrus's V3d / V4d / LOC territory.

9. Expose ``LEFT_LATERALIZED_FUNCTIONS`` and ``RIGHT_ONLY_DOMAINS``
   as the left-lateralized and right-only downstream functions
   associated with the gyri in this package. **They must be
   byte-identical (as sets) to the corresponding tuples in the
   sibling ``..cortex`` and ``..brodmann_areas`` packages.**

10. Define ``__all__`` as shown in the implementation contract.

11. Contain **no** logic beyond the above.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are four forward references for this package**, and they are
the largest forward-reference list of any occipital gyral package (the
gyri parent has only one current child). They are:

1. **Lingual gyrus** — a **medial-surface gyrus** that carries the
   lower-bank V1 / V2 representation (the upper contralateral visual
   field). It should be placed either at the ``..occipital`` parent
   level (like the cuneus) or under ``..gyri`` — **the placement
   decision must preserve the cuneus / lingual gyrus symmetry**,
   because the two gyri are the upper and lower banks of the
   calcarine sulcus. The caveat text is byte-identical to the right
   sibling's.

2. **Superior lateral occipital gyrus** — a **forward reference** if
   the lateral occipital gyrus is ever subdivided into superior /
   middle / inferior thirds. The current tree keeps the gyrus as a
   single package because the V3d / V4d / LOC overlays span the
   full extent without clean anatomical breaks.

3. **Middle lateral occipital gyrus** — same as #2.

4. **Inferior lateral occipital gyrus** — same as #2.

**In addition, four V-area forward references are associated with the
lateral occipital gyrus's overlays**: **V3d**, **V4d**, **LOC**, and
**MT/V5**. These are forward references in ``..cortex``, not here,
but the ``GYRI_TO_V_OVERLAYS`` index references them. **When they
are created under ``..cortex``, this package's ``GYRI_TO_V_OVERLAYS``
must be updated in the same commit, in both hemispheres.**

**All forward references are byte-identical to the left sibling's.**
**The lingual gyrus placement caveat is byte-identical to the left
sibling's** — the placement question is a property of the occipital
lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a lateral occipital sub-region becomes a package)
--------------------------------------------------------------------------------

The lateral occipital gyrus is **the only lateral-surface gyrus of
the occipital lobe**, and it is **architectonically continuous**
across its anteroposterior extent. **The one natural split is the
superior / middle / inferior lateral occipital gyrus triad** — some
parcellations distinguish three gyral folds analogous to the frontal
lobe's SFG / MFG / IFG. **The current tree keeps them together as
a single gyrus** because the V3d / V4d / LOC overlays span the full
extent without clean anatomical breaks.

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
  4. Mirror the promotion on the right side in the same commit.

**The split preserves the cuneus exclusion** — the cuneus remains
a parent-level sibling, not a child of ``..gyri``.

**The split requires a joint revision of the ``..cortex`` V-area
packages' anatomical-substrate declarations** — V3d, V4d, and LOC
would each need to declare their specific lateral-occipital-gyrus
subdivision as their anatomical substrate. **The exact form must
be decided hemisphere-invariantly** and applied in the same commit,
in both hemispheres.

**No split should be performed while the LOC is unresolved** — LOC
is the most clinically consequential of the three overlays (it is
the upstream input to the left VWFA reading pathway and the right
FFA face pathway), and creating it first establishes the complete
lateral-occipital-gyrus downstream context.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/cortex/occipital/gyri``:

    MUST be identical (byte-for-byte):
        LOBE                         "occipital"
        GYRI_CHILDREN                ("lateral_occipital_gyrus",)
        GYRI_TO_V_OVERLAYS           same gyrus → V-area
                                     overlays (v3, v4, LOC)
        GYRI_TO_BA_OVERLAYS          same gyrus → BA-19 overlays
        EXCLUDED_GYRI                same cuneus / lingual gyrus
                                     exclusions
        FORWARD_REFERENCE_GYRI       same four forward
                                     references (lingual gyrus,
                                     superior / middle / inferior
                                     lateral occipital gyri)
        FORWARD_REFERENCE_V_AREAS    same four V areas (V3d,
                                     V4d, LOC, MT/V5)
        CUNEUS_EXCLUSION_NOTE        byte-identical
        LINGUAL_GYRUS_PLACEMENT_CAVEAT
                                     byte-identical
        The lateral occipital gyrus package's structural fields
                                     (bounds, overlays, forward
                                     references)
        The bounding sulci (transverse occipital, lateral
                                     occipitotemporal, parieto-
                                     occipital)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        LEFT_LATERALIZED_FUNCTIONS
                               left: ("right_hemifield_lower_
                               field_loc_to_left_vwfa",) — the
                               left lateral occipital gyrus's
                               LOC feeds the left VWFA reading
                               pathway.
                               right: () — the right lateral
                               occipital gyrus does not contribute
                               to the left reading pathway.
        RIGHT_ONLY_DOMAINS     left: () — the left lateral
                               occipital gyrus does not
                               contribute to the right face
                               pathway.
                               right: ("face_processing",) —
                               the right lateral occipital
                               gyrus's LOC feeds the right FFA
                               face pathway.
        CLINICAL_ANCHORS       left: visual object agnosia
                               (bilateral), **reading-related
                               deficits** via the LOC → left
                               VWFA pathway, color-form
                               processing deficits (V4d),
                               motion-boundary and depth-from-
                               motion deficits (V3d, milder
                               than right), migraine aura,
                               occipital epilepsy, occipital
                               infarct, PCA, PRES.
                               right: **prosopagnosia**
                               contribution, **visuospatial
                               deficits**, **left hemispatial
                               neglect** (via LOC → right IPS),
                               motion-boundary and depth-from-
                               motion deficits (V3d, **more
                               severe** than left), color-form
                               processing deficits (V4d),
                               migraine aura, occipital
                               epilepsy, occipital infarct,
                               PCA (Benson syndrome), PRES.

**The single-child structure, the lateral occipital gyrus's
overlays, the cuneus exclusion, the forward references, and the
bounding sulci are byte-identical on both sides.** They are
properties of the occipital lobe's anatomy, not of the hemisphere.

**The visual-hemifield asymmetry is the sharpest single entry.**
The left lateral occipital gyrus's V3d / V4d / LOC territory
represents the **right** hemifield; the right lateral occipital
gyrus's same territory represents the **left** hemifield.

**The downstream network asymmetry is the second sharpest entry.**
The left lateral occipital gyrus's LOC feeds the **left VWFA
reading** endpoint; the right lateral occipital gyrus's LOC feeds
the **right FFA face** endpoint. The
`LEFT_LATERALIZED_FUNCTIONS` / `RIGHT_ONLY_DOMAINS` tuples make this
explicit, and the two contributions are mirror-opposite.

**The right-specific clinical anchors are the third sharpest
entry.** The right lateral occipital gyrus carries **three anchors**
that the left does not carry at the same weighting:
`right_lateral_occipital_prosopagnosia_contribution`,
`right_lateral_occipital_visuospatial_deficit`, and
`right_lateral_occipital_left_hemifield_neglect_contribution`. The
left lateral occipital gyrus carries the mirror
`left_lateral_occipital_reading_related_deficit` and
`left_lateral_occipital_visual_object_agnosia` anchors.

**The cuneus exclusion and the lingual gyrus placement caveat are
byte-identical on both sides** and must not be allowed to drift.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/gyri/`` — a sibling of
    ``brodmann_areas``, ``cortex``, ``cuneus``, and ``sulci``.
[ ] The single gyrus child (``lateral_occipital_gyrus``) is
    imported and registered.
[ ] ``GYRI_CHILDREN`` lists the single child and is byte-identical
    to the right sibling's.
[ ] ``GYRI_TO_V_OVERLAYS`` is present and lists the lateral
    occipital gyrus's overlays (v3, v4, LOC) — byte-identical to
    the right sibling's.
[ ] ``GYRI_TO_BA_OVERLAYS`` is present and lists BA 19 — byte-
    identical to the right sibling's.
[ ] ``EXCLUDED_GYRI`` is present with the cuneus and lingual gyrus
    exclusions documented:
    - cuneus → parent-level sibling (medial-surface V1 upper-bank
      surface landmark)
    - lingual gyrus → forward reference (medial-surface V1 lower-
      bank surface landmark)
[ ] **The cuneus exclusion is documented** — the cuneus is **not**
    a child of ``..gyri``, and the reason (V1 upper-bank surface
    landmark, primary functional identity is the calcarine sulcus
    upper bank) is stated explicitly.
[ ] **The cuneus / lateral occipital gyrus contrast is
    documented** — the cuneus is a primary-sensory surface
    landmark (parent level), the lateral occipital gyrus is a
    gyral fold with extrastriate overlays (gyri child).
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] ``LEFT_LATERALIZED_FUNCTIONS`` contains
    "right_hemifield_lower_field_loc_to_left_vwfa" — the left
    lateral occipital gyrus's LOC feeds the left VWFA reading
    pathway.
[ ] ``RIGHT_ONLY_DOMAINS`` contains "face_processing" — **this is
    a left-side absence anchor**, documenting that the left
    lateral occipital gyrus does **not** contribute to the right
    face pathway at the same weighting as the right lateral
    occipital gyrus does.
[ ] ``FORWARD_REFERENCE_GYRI`` lists the four forward references
    (lingual gyrus, superior / middle / inferior lateral
    occipital gyri) and is byte-identical to the right sibling's.
[ ] ``FORWARD_REFERENCE_V_AREAS`` lists the four V areas (V3d,
    V4d, LOC, MT/V5) and is byte-identical to the right
    sibling's.
[ ] ``CUNEUS_EXCLUSION_NOTE`` is present and byte-identical to
    the right sibling's.
[ ] ``LINGUAL_GYRUS_PLACEMENT_CAVEAT`` is present and byte-
    identical to the right sibling's — the placement decision
    must preserve the cuneus / lingual gyrus symmetry.
[ ] **The lateral occipital gyrus's functional overlays (V3d,
    V4d, LOC) are documented** — three extrastriate and
    association areas spanning the full extent.
[ ] **The lateral occipital gyrus does NOT carry the reading or
    face domains directly** — those live downstream in the
    fusiform gyrus (left VWFA / right FFA). The lateral
    occipital gyrus is the **upstream LOC territory**.
[ ] **The superior / middle / inferior lateral occipital gyrus
    subdivision is documented as a forward reference** — the
    current tree keeps the gyrus as a single package because
    the overlays span the full extent.
[ ] **The lateral occipital gyrus → fusiform gyrus continuity**
    is documented — the lateral occipital gyrus transitions to
    the fusiform gyrus at the lateral occipitotemporal sulcus.
    **On the left, the fusiform gyrus's VWFA is downstream of
    the lateral occipital gyrus's LOC.** **On the right, the
    fusiform gyrus's FFA is downstream of the lateral occipital
    gyrus's LOC.**
[ ] **The transverse occipital sulcus** is documented as the
    dorsal boundary of the lateral occipital gyri.
[ ] **The lateral occipitotemporal sulcus** is documented as the
    ventral boundary (into the fusiform gyrus).
[ ] **The parieto-occipital sulcus** is documented as the rostral
    (medial) boundary.
[ ] **The calcarine sulcus is explicitly NOT a boundary of the
    lateral occipital gyrus** — it is the boundary of the cuneus
    and lingual gyrus, on the medial surface.
[ ] **The LOC and MT/V5 forward references are documented** —
    they live in ``..cortex`` as V-area forward references, not
    here as gyral children.
[ ] No SUBDIVISIONS promotion is performed while LOC is
    unresolved.
[ ] The **promotion rule for the three-way lateral occipital
    gyrus split** is documented, with the joint ``..cortex``
    update requirement and the downstream LOC prerequisite.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (GYRI_CHILDREN, GYRI_TO_V_OVERLAYS, GYRI_TO_BA_OVERLAYS,
    EXCLUDED_GYRI, FORWARD_REFERENCE_GYRI,
    FORWARD_REFERENCE_V_AREAS, CUNEUS_EXCLUSION_NOTE,
    LINGUAL_GYRUS_PLACEMENT_CAVEAT, lateral occipital gyrus's
    bounds and overlays) match the right sibling;
    VISUAL_HEMIFIELD, LEFT_LATERALIZED_FUNCTIONS,
    RIGHT_ONLY_DOMAINS, and CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    lateral occipital gyrus carries "right_hemifield"; the right
    carries "left_hemifield."
[ ] **The reading-vs-face downstream asymmetry is verified**:
    the left lateral occipital gyrus carries
    "right_hemifield_lower_field_loc_to_left_vwfa" and the right
    carries "face_processing" — the two are mirror-opposite.
[ ] **The cuneus exclusion is verified** — the cuneus is listed
    in ``EXCLUDED_GYRI``, not in ``GYRI_CHILDREN``. **The cuneus
    is a parent-level sibling, not a child of ``..gyri``.**
[ ] Any downstream code querying "what gyri are in the left
    occipital lobe's ``..gyri`` package?" must receive
    "only `lateral_occipital_gyrus` — the cuneus is at the
    parent level, and the lingual gyrus is a forward reference."
[ ] Any downstream code querying "what does the left lateral
    occipital gyrus see?" must receive "the RIGHT visual
    hemifield" (via its V3d / V4d / LOC territory).
[ ] Any downstream code querying "what does the left lateral
    occipital gyrus feed?" must receive "the left LOC, and from
    there the left VWFA (reading)" — the left lateral occipital
    gyrus is the upstream LOC input.
[ ] Any downstream code querying "what does the right lateral
    occipital gyrus feed?" must receive "the right LOC, and from
    there the right FFA (faces)" — the right lateral occipital
    gyrus is the upstream LOC input (documented in the right
    sibling).
[ ] Any downstream code assigning the left reading pathway must
    route through the left lateral occipital gyrus's LOC →
    left fusiform gyrus → left VWFA chain.
[ ] Any downstream code assigning the right face pathway must
    route through the right lateral occipital gyrus's LOC →
    right fusiform gyrus → right FFA chain.
[ ] Any downstream code assigning visual object agnosia must
    note that **bilateral lateral occipital gyrus lesions are
    required** — the left lateral occipital gyrus alone does not
    produce full visual object agnosia.
[ ] Any downstream code assigning prosopagnosia must route
    through the **right** lateral occipital gyrus's LOC →
    right FFA pathway.
[ ] Any downstream code assigning left hemispatial neglect must
    note that **the right lateral occipital gyrus's LOC →
    right IPS pathway is a contributor**, not a sole cause.
[ ] Any downstream code assigning motion-boundary or
    depth-from-motion processing must note that **the right
    lateral occipital gyrus's V3d territory is the dominant
    substrate** — the left's contribution is milder.
[ ] Any downstream code assigning the three-way lateral
    occipital gyrus split must first resolve LOC — the split
    is blocked while LOC is a forward reference.
[ ] **The cuneus exclusion note and the lingual gyrus placement
    caveat are byte-identical to the right sibling's** — they
    are properties of the occipital lobe, not of the
    hemisphere.
"""