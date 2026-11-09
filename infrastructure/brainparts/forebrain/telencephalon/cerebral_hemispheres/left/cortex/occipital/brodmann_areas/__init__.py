"""
Occipital Brodmann Areas — Left Hemisphere
===========================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── brodmann_areas   ← THIS PACKAGE

This is a **cytoarchitectonic-collection parent** — a registry package
whose children are the three Brodmann-area packages assigned to the
left occipital lobe. It is the **cytoarchitectonic** counterpart of
``..cortex`` (the functional V-numbered parent) and the sibling of
``..cuneus``, ``..gyri``, and ``..sulci`` under ``..occipital``.

Parent: ``..occipital`` — the left occipital lobe. Sibling to
``..cortex``, ``..cuneus``, ``..gyri``, and ``..sulci``.

This package is the **structural mirror** of
``../../right/cortex/occipital/brodmann_areas``. The three BA
children, their names, and their BA numbers are identical on both
sides; the **functional emphasis** and **clinical significance** of
each BA diverge between hemispheres in the same way that the occipital
lobe itself diverges (left → verbal visual processing, right → face
processing and visuospatial attention).

Direct children (3)
-------------------
::

    brodmann_areas
    ├── brodmann_area_17_primary_visual   [BA 17 — V1, striate cortex]
    ├── brodmann_area_18                  [BA 18 — V2 + V3]
    └── brodmann_area_19                  [BA 19 — V3A + V4 + V5/MT+]

**The three children are not equal in scope.** BA 17 corresponds
**tightly** to V1 (1:1); BA 18 covers **two** modern V areas (V2 + V3);
BA 19 covers **three or more** (V3A + V4 + V5/MT+, with V3B and LOC as
nearby forward references). The parent must therefore carry an
asymmetric crosswalk, and downstream code must not treat the three BAs
as equivalent-sized units.

--------------------------------------------------------------------------------
THE BA NUMBERING IN THE OCCIPITAL LOBE — WHY IT IS CLEAN
--------------------------------------------------------------------------------

Unlike the insular BA packages, whose numbers are **conventional labels**
that modern parcellations do not preserve, the occipital BA numbers are
**the original Brodmann areas** that Brodmann himself defined — BA 17
was **the very first area Brodmann ever delineated** (1909), and it is
visible to the naked eye because of the **stria of Gennari**. The V1/V2
border (BA 17 / BA 18 border) is architectonically unambiguous. BA 18
and BA 19 are Brodmann's own extrastriate subdivisions, and they have
been **continuously in use** since 1909.

**Consequence for the architecture**: unlike the insular BA packages,
the occipital BA numbers are **not** subject to a `PARCELATION_AMBIGUITY`
caveat. They are the classical numbers, they are stable across modern
parcellations, and they map cleanly onto the striate / extrastriate
distinction. **No `MODERN_CROSSWALK` field is required** — the HCP,
Öngür-Price, and Petrides-Pandya schemes all retain BA 17 and BA 18 as
distinct architectonic entities, and the occipital BA package is the
**only one in the cortex tree** where the Brodmann scheme is a
first-class modern reference rather than a historical convention.

**The one caveat** is that **BA 19 is a large, heterogeneous
territory** spanning V3A, V4, V5/MT+, and portions of the lateral
occipital complex. Modern parcellations subdivide BA 19 into several
distinct parcels, and downstream code that needs a specific modern
parcel must go through the ``MODERN_CROSSWALK`` on the BA 19 child
(not on this parent). The parent's crosswalk is the **V-area**
correspondence, not the modern-parcel correspondence.

--------------------------------------------------------------------------------
THE BA ↔ V CROSSWALK — THIS PACKAGE'S CRITICAL CONTRACT
--------------------------------------------------------------------------------

The **single most important structural concern** of this package is the
**BA ↔ V crosswalk**. The BA decomposition and the V decomposition are
**independent** and **overlapping**:

    BA 17  ↔  V1                             (1:1 — tight)
    BA 18  ↔  V2, V3                         (1:2 — partial)
    BA 19  ↔  V3A, V4, V5/MT+                (1:3+ — partial,
                                              with V3B and LOC as
                                              nearby forward
                                              references)

**The crosswalk lives in ``..occipital``**, in the parent's
``BA_TO_V_CROSSWALK`` and ``V_TO_BA_CROSSWALK`` registries. This
package **re-exports** those registries — it does **not** redefine them.
The single-source-of-truth rule is required because:

  * ``..occipital`` is the parent of both ``brodmann_areas`` and
    ``cortex``, and it is where the two decompositions must be
    reconciled.
  * The ``cortex`` package's V-numbered children also cross-reference
    the crosswalk, and both branches must use the same source.
  * Any drift between the two copies of the crosswalk would be a
    silent bug that makes downstream "which BA contains this V area?"
    queries return inconsistent results.

**The crosswalk must be complete in both directions** — every BA child
must declare its V correlates, every V child must declare its BA
correlates, and the parent's ``BA_TO_V_CROSSWALK`` and
``V_TO_BA_CROSSWALK`` must be exact inverses of each other. The
parent inversion function must fail loudly if the two registries
diverge.

**The crosswalk is hemisphere-invariant** — the BA-to-V mapping is a
property of the occipital lobe itself, not of the hemisphere. The
left and right ``brodmann_areas`` parents must re-export
**byte-identical** crosswalk dicts.

--------------------------------------------------------------------------------
THE V-AREA FORWARD REFERENCES
--------------------------------------------------------------------------------

The parent's crosswalk references **six V-numbered functional areas**,
but only four of them are **current children** of ``..cortex``:

    Current children of ..cortex:
        primary_visual_cortex   (V1)   — BA 17
        v2                             — BA 18
        v3                             — BA 18, BA 19
        v4                             — BA 19

    Forward references (not yet packages):
        V3A                     — BA 19 (sub-area of V3 in some
                                  parcellations, V4 in others;
                                  **core node of the right dorsal
                                  attention network** — the left's
                                  V3A is part of the dorsal stream
                                  but less dominant)
        V3B                     — BA 19 (kinetic-occipital area)
        V5 / MT+                — BA 19 (motion area; **more strongly
                                  engaged on the right**)
        LOC (lateral occipital   — BA 19 (object-recognition complex)
             complex)

**The crosswalk must be tolerant of forward references.** A BA child
may declare a V correlate that is not yet a package (e.g., BA 19 →
V3A, V5/MT+, LOC); the parent must accept such entries and record them
as **forward references** rather than failing. When those V packages
are eventually created under ``..cortex``, the crosswalk entries
resolve fully and the forward-reference status is cleared in the same
commit, in both hemispheres.

**This tolerance is the only "forward reference" mechanism in the
occipital BA package** — there are no missing BA children and no
missing bounding gyri. The forward references are entirely on the
``..cortex`` side, and they are documented on the affected V-area
children, not here. The parent only needs to record them in the
crosswalk.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAIN EMPHASIS (left-hemisphere-specific)
--------------------------------------------------------------------------------

This package's children collectively cover **all twelve** occipital
functional domains. The **left-side emphasis** per BA is:

    BA 17 (V1)     primary_visual_processing,
                   retinotopic_organization,
                   binocular_vision
                   **On the left, V1 processes the RIGHT visual
                   hemifield.** The primary contribution is the
                   first cortical stage of vision — orientation,
                   contrast, spatial frequency, retinotopic mapping.

    BA 18 (V2+V3)  primary_visual_processing (secondary),
                   binocular_vision,
                   form_and_object_perception (surface / texture
                   / border ownership),
                   spatial_localization (V3)
                   **On the left, BA 18's form and object
                   contribution is weighted toward the LOCAL /
                   FEATURAL aspect** — the left hemisphere's
                   documented advantage in local processing
                   (Navon's local-precedence asymmetry is the
                   mirror of the right's global-precedence).

    BA 19 (V3A+V4+  color_vision (V4),
           V5/MT+)  motion_perception (V5/MT+),
                   form_and_object_perception (V4, LOC),
                   spatial_localization (V3A),
                   visual_attention (V3A, MT/V5 — **more
                   strongly engaged on the right**, but the
                   left's V3A and MT/V5 participate in the
                   dorsal stream at a lower weighting)
                   **On the left, BA 19's contribution is
                   weighted toward the VENTRAL stream** — V4
                   and the LOC-side form/object processing that
                   feeds the left VWFA and the reading pathway.
                   The left's dorsal-stream contribution (V3A,
                   MT/V5) is present but weaker than the
                   right's.

**The left-specific caveats**:

  * **`visual_word_processing` is a left-lateralized function that
    the occipital BA children collectively support** — via the
    ventral-stream output of BA 19 (V4, LOC) to the left VWFA. **No
    single BA claims this domain as its primary contribution**;
    it is a network property of the left occipital + left fusiform
    pathway, and it is documented at the `..occipital` parent level
    and on the left VWFA in `..cortex.temporal`.
  * **`face_processing` is right-lateralized** and does **not**
    appear in the left occipital BA children at the same weighting.
    The left BA 19's ventral-stream output supports form and
    object processing generally, but **not** face-selective
    processing — that is a right-hemisphere specialization.
  * **`global_visual_processing` is right-lateralized** and does
    **not** appear in the left occipital BA children. The left's
    documented advantage is in **local / featural processing**,
    which is captured under BA 18's `form_and_object_perception`
    emphasis and is not a separate domain.
  * **`visual_attention`** — the left occipital BA 19 children
    (V3A, MT/V5) participate in the dorsal attention network at a
    lower weighting than the right. The dominant attentional
    contributions are right-lateralized and documented in the
    right sibling.

**The BA children share these domain assignments; the parent captures
the left-specific emphasis per BA.**

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..occipital
    The parent occipital lobe. This package's parent and the source
    of the ``BA_TO_V_CROSSWALK``, ``V_TO_BA_CROSSWALK``, and
    ``DOMAIN_TO_CHILDREN`` registries. This package **re-exports**
    those indices; it does not redefine them.

..cortex
    The **functional V-numbered sibling** of this package. Where this
    package decomposes the occipital lobe **cytoarchitectonically**
    (BA 17 / 18 / 19), ``..cortex`` decomposes the **same territory
    functionally** (V1 / V2 / V3 / V4). The two decompositions
    overlap and must be cross-referenced via the parent's
    ``BA_TO_V_CROSSWALK``. **The V-area forward references** (V3A,
    V3B, V5/MT+, LOC) are on the ``cortex`` side, not this side.

..cuneus
    The medial-surface gyral landmark for V1's upper bank. The BA 17
    child's V1 representation extends into the cuneus's lower
    margin (the upper bank of the calcarine sulcus), and the
    ``..cuneus`` package cross-references BA 17 as its primary
    functional overlay.

..gyri
    The lateral-surface gyral child. The lateral occipital gyrus
    overlays BA 19 (the extrastriate territory), and the gyral
    package cross-references BA 19 as its primary functional
    overlay.

..sulci
    The sulcal child. The calcarine sulcus is the surface landmark
    for BA 17's V1 representation; the lunate sulcus (when present)
    marks the BA 17 / BA 18 border on the lateral surface; the
    transverse occipital sulcus marks the posterior boundary of
    the lateral occipital gyri (BA 19 territory).

..cortex.temporal
    The **ventral stream** continues from BA 18 (V2 / V3) and BA 19
    (V4, LOC) into the temporal lobe (inferior temporal cortex,
    fusiform gyrus, VWFA, FFA). **The left VWFA is the left-
    lateralized reading-related endpoint of the BA 19 ventral
    stream.** The temporal package must declare the left BA 18 and
    BA 19 as sources of its visual input for the ventral stream,
    and must note the left-lateralized VWFA specialization.

..cortex.parietal
    The **dorsal stream** continues from BA 19 (V3A, V5/MT+) into
    the parietal lobe. **The left's dorsal-stream contribution is
    present but weaker than the right's.** The parietal package
    must declare the left BA 19 as a source of its visual input
    for the dorsal stream, and must note the right-lateralized
    attentional emphasis that lives in the right sibling.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** send top-down visual attentional signals to the
    occipital BA territories. The frontal package must declare the
    occipital BA 18 and BA 19 as targets of its attentional
    projections.

..cortex.cingulate  — indirect
    The cingulate participates in visual attention and visual
    memory via the cingulum bundle and the salience network.
    No direct cingulate → occipital BA projection originates in
    the cingulate proper. Recorded here to pre-empt a false
    cross-reference.

..cortex.insular  — indirect
    The insular lobe is not a direct visual area. Its visual
    contributions are through the salience network and multimodal
    integration. Recorded here to pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **lateral geniculate nucleus (LGN)** is the thalamic relay
    from the retina to BA 17 (V1). The LGN → BA 17 projection is
    the anatomical substrate of primary visual processing, and BA
    17's **stria of Gennari** is the architectonic signature of
    this first thalamocortical relay. The thalamus package must
    declare the LGN as the primary visual thalamic relay to the
    left BA 17.

../../right/cortex/occipital/brodmann_areas
    The right-hemisphere homologue. Structural fields
    (``BA_TO_V_CROSSWALK``, child names, BA numbers, V-area
    correlates) MUST be byte-identical. Functional emphasis and
    clinical significance diverge — the left BA children are
    weighted toward the **right hemifield**, **verbal visual
    processing**, **local / featural processing**; the right BA
    children are weighted toward the **left hemifield**, **face
    processing**, **visuospatial attention**, **global visual
    processing**.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    LOBE                = "occipital"
    HEMISPHERE          = "left"

    BA_CHILDREN         = (
                              "brodmann_area_17_primary_visual",
                              "brodmann_area_18",
                              "brodmann_area_19",
                          )

    BA_TO_V_CROSSWALK   = {   # re-exported from ..occipital,
                              # NOT redefined — single source of
                              # truth
                              17: ("primary_visual_cortex",),
                              18: ("v2", "v3"),
                              19: ("v3", "v4",
                                   "V3A", "V3B", "V5_MT_plus",
                                   "LOC"),
                              # The V3A, V3B, V5_MT_plus, and LOC
                              # entries are FORWARD REFERENCES — the
                              # packages do not yet exist under
                              # ..cortex. The parent must accept
                              # them and mark them as forward
                              # references rather than failing.
                          }

    V_TO_BA_CROSSWALK   = {   # re-exported from ..occipital,
                              # NOT redefined — single source of
                              # truth. Must be an exact inverse of
                              # BA_TO_V_CROSSWALK.
                              "primary_visual_cortex": (17,),
                              "v2":                    (18,),
                              "v3":                    (18, 19),
                              "v4":                    (19,),
                              "V3A":                   (19,),
                              "V3B":                   (19,),
                              "V5_MT_plus":            (19,),
                              "LOC":                   (19,),
                          }

    FORWARD_REFERENCE_V_AREAS = (
        "V3A",
        "V3B",
        "V5_MT_plus",
        "LOC",
    )
        # The V-numbered areas that appear in the crosswalk but are
        # not yet packages under ..cortex. When they are created,
        # this tuple must be emptied in the same commit, in both
        # hemispheres.

    FUNCTIONAL_DOMAIN_EMPHASIS = {   # left-side emphasis per BA
        "brodmann_area_17_primary_visual": (
            "primary_visual_processing",
            "retinotopic_organization",
            "binocular_vision",
        ),
        "brodmann_area_18": (
            "primary_visual_processing_secondary",
            "binocular_vision",
            "form_and_object_perception_local_featural",
            "spatial_localization_v3",
        ),
        "brodmann_area_19": (
            "color_vision",
            "motion_perception_weaker_than_right",
            "form_and_object_perception_ventral_stream",
            "spatial_localization_v3a",
            "visual_attention_lower_weighting_than_right",
            "visual_word_processing_downstream_via_vwfa",
        ),
    }

    LEFT_LATERALIZED_FUNCTIONS = (
        "visual_word_processing",
        "local_featural_processing",
    )
        # The functions that the left occipital BA children
        # collectively support but that are absent or weaker on
        # the right. The left BA children contribute to these via
        # their ventral-stream output, but no single BA claims them
        # as a primary contribution — they are network properties
        # of the left occipital + left fusiform pathway.

    RIGHT_ONLY_DOMAINS = (
        "face_processing",
        "global_visual_processing",
    )
        # The domains that are right-lateralized and do NOT appear
        # in the left occipital BA children at the same weighting.
        # These are captured in the right sibling's
        # FUNCTIONAL_DOMAIN_EMPHASIS and are documented here only
        # as exclusions so downstream code knows the left BA
        # children do not carry them.

    __all__ = [
        "LOBE",
        "HEMISPHERE",
        "BA_CHILDREN",
        "BA_TO_V_CROSSWALK",
        "V_TO_BA_CROSSWALK",
        "FORWARD_REFERENCE_V_AREAS",
        "FUNCTIONAL_DOMAIN_EMPHASIS",
        "LEFT_LATERALIZED_FUNCTIONS",
        "RIGHT_ONLY_DOMAINS",
    ]

No behaviour. This package is a declarative registry; all computation
that references the occipital BA packages lives in ``cortex/`` or
``memory/``.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``brodmann_areas/__init__.py`` must:

1. Import the three BA children (no side effects):
       from . import brodmann_area_17_primary_visual
       from . import brodmann_area_18
       from . import brodmann_area_19

2. Re-export ``BA_TO_V_CROSSWALK`` and ``V_TO_BA_CROSSWALK`` from
   ``..occipital`` — **do not redefine them**. The occipital parent
   is the single source of truth for the BA ↔ V mapping, and the
   ``..cortex`` children depend on the same dicts.

3. Expose ``FORWARD_REFERENCE_V_AREAS`` so that downstream code
   querying "which V areas have BA correlates?" can distinguish
   between **resolved** V areas (V1, V2, V3, V4) and **forward-
   reference** V areas (V3A, V3B, V5/MT+, LOC).

4. Expose ``FUNCTIONAL_DOMAIN_EMPHASIS`` as a **left-side view** of
   the children's ``FUNCTIONAL_DOMAINS``. This is hand-written and
   is where the left-side emphasis is captured. The right sibling's
   version differs.

5. Expose ``LEFT_LATERALIZED_FUNCTIONS`` and ``RIGHT_ONLY_DOMAINS``
   so downstream code can see, at a glance, which functional
   domains are hemisphere-asymmetric and which side carries them.
   These tuples must be byte-identical to the **complementary**
   tuples on the right sibling — the left's `LEFT_LATERALIZED_
   FUNCTIONS` must be the right's `RIGHT_ONLY_DOMAINS`, and vice
   versa.

6. Define ``__all__`` as shown in the implementation contract.

7. Contain **no** logic beyond the above.

--------------------------------------------------------------------------------
FORWARD-REFERENCE CAVEAT
--------------------------------------------------------------------------------

**The only forward-reference caveat for this package is on the V-area
side, not the BA side.** All three BA children (BA 17, BA 18, BA 19)
exist as packages under ``..brodmann_areas/``, and all their
structural fields resolve. **There are no missing BA children** and
**no naming collisions** (unlike the insular BA 41 / BA 42 packages,
which collide with the temporal auditory cortex).

**Four V-numbered functional areas are forward references**:
``V3A``, ``V3B``, ``V5/MT+``, and ``LOC``. They appear in the
parent's crosswalk (as BA 19 correlates) but are not yet packages
under ``..cortex``. When they are created:

  1. Add the V package under ``..cortex/``.
  2. Remove the corresponding entry from ``FORWARD_REFERENCE_V_AREAS``
     in this package **and** in the right sibling, in the same
     commit.
  3. Update the V child's ``BRODMANN_CORRELATES`` to declare the same
     BA number(s) that appear in the parent's ``V_TO_BA_CROSSWALK``.
  4. Verify the parent's ``BA_TO_V_CROSSWALK`` and
     ``V_TO_BA_CROSSWALK`` remain exact inverses after the update.

**No asymmetry is permitted in the V-area forward references** — both
hemispheres must declare the same forward-reference list and must
resolve them in the same commit. The occipital lobe's BA ↔ V mapping
is hemisphere-invariant.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/cortex/occipital/brodmann_areas``:

    MUST be identical (byte-for-byte):
        LOBE                          "occipital"
        BA_CHILDREN                   the same three child names,
                                      in the same order
        BA_TO_V_CROSSWALK             the same BA → V mapping
        V_TO_BA_CROSSWALK             the same V → BA mapping
                                      (exact inverse)
        FORWARD_REFERENCE_V_AREAS     the same four V areas
                                      (V3A, V3B, V5/MT+, LOC)
        The three BA children's structural fields (AREA_NAME,
        LOBE, BRODMANN_NUMBER, FUNCTIONAL_CORRELATES,
        RETINOTOPIC_MAP)

    MUST differ (and the difference must be documented here):
        HEMISPHERE                    "left" vs "right"
        FUNCTIONAL_DOMAIN_EMPHASIS    left: BA 17 processes RIGHT
                                      hemifield; BA 18 carries LOCAL
                                      / FEATURAL processing emphasis;
                                      BA 19's ventral stream feeds
                                      the left VWFA.
                                      right: BA 17 processes LEFT
                                      hemifield; BA 18 carries
                                      GLOBAL processing emphasis;
                                      BA 19's dorsal stream is more
                                      strongly engaged (visuospatial
                                      attention, motion).
        LEFT_LATERALIZED_FUNCTIONS    left: ("visual_word_processing",
                                      "local_featural_processing").
                                      right: () — the right side's
                                      LEFT_LATERALIZED_FUNCTIONS
                                      tuple is empty.
        RIGHT_ONLY_DOMAINS            left: ("face_processing",
                                      "global_visual_processing").
                                      right: () — the right side's
                                      RIGHT_ONLY_DOMAINS tuple is
                                      empty.

**The left's `LEFT_LATERALIZED_FUNCTIONS` must equal the right's
`RIGHT_ONLY_DOMAINS`, and vice versa.** This is the fundamental
symmetry invariant of the lateralized-domain lists — if the left
says "visual_word_processing is left-lateralized," the right must
say "visual_word_processing is left-only," and neither side can
contain the other's entries.

**The `FORWARD_REFERENCE_V_AREAS` tuple is byte-identical on both
sides.** The V-area forward references are a property of the
occipital lobe, not of the hemisphere, and any asymmetry in their
declaration is a bug.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/brodmann_areas/`` — a
    sibling of ``cortex``, ``cuneus``, ``gyri``, and ``sulci``.
[ ] All three BA children are imported and registered.
[ ] ``BA_CHILDREN`` lists the three child names in the canonical
    order (17, 18, 19) and is byte-identical to the right
    sibling's.
[ ] ``BA_TO_V_CROSSWALK`` is **re-exported** from ``..occipital``,
    not redefined, and is byte-identical to the right sibling's.
[ ] ``V_TO_BA_CROSSWALK`` is **re-exported** from ``..occipital``,
    not redefined, is byte-identical to the right sibling's, and is
    an exact inverse of ``BA_TO_V_CROSSWALK``.
[ ] ``FORWARD_REFERENCE_V_AREAS`` is present, lists exactly the
    four forward references (V3A, V3B, V5/MT+, LOC), and is
    byte-identical to the right sibling's.
[ ] ``FUNCTIONAL_DOMAIN_EMPHASIS`` captures the **left-side
    emphasis**:
    - BA 17: primary_visual_processing, retinotopic_organization,
      binocular_vision (**RIGHT hemifield**)
    - BA 18: primary_visual_processing_secondary,
      binocular_vision, form_and_object_perception_local_featural,
      spatial_localization_v3
    - BA 19: color_vision, motion_perception_weaker_than_right,
      form_and_object_perception_ventral_stream,
      spatial_localization_v3a,
      visual_attention_lower_weighting_than_right,
      visual_word_processing_downstream_via_vwfa
[ ] ``LEFT_LATERALIZED_FUNCTIONS`` is present with exactly
    ``("visual_word_processing", "local_featural_processing")``.
[ ] ``RIGHT_ONLY_DOMAINS`` is present with exactly
    ``("face_processing", "global_visual_processing")``.
[ ] **The symmetry invariant** is documented: the left's
    `LEFT_LATERALIZED_FUNCTIONS` must equal the right's
    `RIGHT_ONLY_DOMAINS`, and vice versa. The checklist verifies
    this — a missing or extra entry in either tuple is a bug.
[ ] The **BA numbering in the occipital lobe is clean** — the
    three BAs are the classical Brodmann areas, not conventional
    labels. **No `PARCELATION_AMBIGUITY` field is required, and no
    `MODERN_CROSSWALK` field is required on this parent.** BA 17
    was Brodmann's first area, its V1/V2 border is
    architectonically unambiguous, and the numbers remain in use
    in modern parcellations.
[ ] The **asymmetric BA-to-V mapping** is documented:
    - BA 17 ↔ V1 (1:1, tight)
    - BA 18 ↔ V2 + V3 (1:2, partial)
    - BA 19 ↔ V3A + V4 + V5/MT+ (1:3+, partial, with V3B and LOC
      as nearby forward references)
    The asymmetry is not a defect — it reflects the different
    territory sizes of the three BAs, and downstream code must
    not assume the BAs are equivalent units.
[ ] The **V-area forward references** are documented, the
    `FORWARD_REFERENCE_V_AREAS` tuple is present, and the
    resolution rule (remove the entry from both hemispheres in
    the same commit when the V package is created) is recorded.
[ ] The **left-lateralized functions** (verbal visual processing,
    local / featural processing) are documented as **network
    properties of the left occipital + left fusiform pathway**,
    not as BA-specific claims. The left BA 19's ventral-stream
    output feeds the left VWFA, but no single BA claims
    `visual_word_processing` as a primary contribution.
[ ] The **right-only domains** (`face_processing`,
    `global_visual_processing`) are documented as **excluded**
    from the left occipital BA children at the same weighting.
    These are documented on the right sibling's
    `FUNCTIONAL_DOMAIN_EMPHASIS`, not here.
[ ] The **left-specific visual hemifield rule** is documented:
    the left occipital BA children process the **RIGHT** visual
    hemifield, not the left, not both. This is the primary
    lateralization fact for the left occipital lobe.
[ ] The **BA ↔ V crosswalk source-of-truth rule** is documented:
    the crosswalk lives in ``..occipital``, this package
    re-exports it, and any redefinition here would be a bug.
[ ] No naming collision exists — unlike the insular BA 41/42
    packages, the occipital BA numbers are unique to the
    occipital lobe and there is no `NAMING_COLLISION_WITH` field.
[ ] Every child's own docstring (BA 17, BA 18, BA 19) follows the
    same template used in the other child packages — hierarchical
    location → what the BA is → V correlates → territories →
    retinotopic map → functional domains → clinical significance
    → cross-references → contract → checklist.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA numbers, V correlates, crosswalks, forward references)
    match the right sibling; FUNCTIONAL_DOMAIN_EMPHASIS and the
    lateralized-domain tuples deliberately differ, and the
    complementarity invariant (left's LEFT = right's RIGHT-only,
    and vice versa) is verified.
[ ] Any downstream code that queries "which BA contains V3A?" must
    receive ``(19,)`` and must also receive the **forward-reference
    flag** — V3A is not yet a package, so the answer is
    conditional.
[ ] Any downstream code that queries "which V areas does BA 19
    contain?" must receive the four current children (V3, V4) plus
    the four forward references (V3A, V3B, V5/MT+, LOC), with the
    forward references marked.
[ ] Any downstream code that queries "which occipital functions
    are left-lateralized?" must receive
    `LEFT_LATERALIZED_FUNCTIONS` from this package, not from
    `FUNCTIONAL_DOMAIN_EMPHASIS` — the emphasis dict records
    weighting, while the lateralized-functions tuple records
    presence/absence at the hemisphere level.
"""