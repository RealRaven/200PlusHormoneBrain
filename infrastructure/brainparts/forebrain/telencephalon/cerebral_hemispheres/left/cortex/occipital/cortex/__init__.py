"""
Occipital Functional Cortex (V-Numbered) — Left Hemisphere
==========================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── cortex   ← THIS PACKAGE

This is the **functional / retinotopic-collection parent** of the left
occipital lobe — a registry package whose children are the four
currently-modelled **V-numbered functional areas** (V1, V2, V3, V4) that
comprise the core of the visual hierarchy. It is the **functional**
counterpart of ``..brodmann_areas`` (the cytoarchitectonic parent), and
the sibling of ``..cuneus``, ``..gyri``, and ``..sulci`` under
``..occipital``.

Parent: ``..occipital`` — the left occipital lobe. Sibling to
``..brodmann_areas``, ``..cuneus``, ``..gyri``, and ``..sulci``.

This package is the **structural mirror** of
``../../right/cortex/occipital/cortex``. The four V children, their
names, their BA correlates, their retinotopic maps, and the V-numbering
scheme are identical on both sides; the **functional emphasis** and
**clinical significance** diverge between hemispheres in the same way
that the occipital lobe itself diverges (left → verbal visual
processing; right → face processing and visuospatial attention).

Direct children (4)
-------------------
::

    cortex
    ├── primary_visual_cortex   [V1 — BA 17]
    ├── v2                      [V2 — BA 18]
    ├── v3                      [V3 — BA 18 + BA 19]
    └── v4                      [V4 — BA 19]

**The children are in hierarchy order** — V1 → V2 → V3 → V4 — and
downstream code that traverses the visual hierarchy must follow this
order. Unlike ``..brodmann_areas``, whose three BA children are
**cytoarchitectonically independent** (each is a distinct Brodmann
area), the four V children are **functionally sequential** (each feeds
the next in the V1 → V2 → V3 → V4 processing stream).

**One V child is a direct child of ``..occipital`` itself** — the
``..cuneus`` package, which is a medial-surface gyral landmark for
V1's upper bank. It is **not** a child of this package (it is a
sibling of ``..brodmann_areas`` and ``..cortex`` at the
``..occipital`` parent level), and this package does **not** duplicate
it. The cuneus is cross-referenced from here as the surface landmark
for V1's dorsal bank.

--------------------------------------------------------------------------------
THE V-NUMBERING SCHEME — WHY IT IS CLEAN
--------------------------------------------------------------------------------

The V-numbering scheme (**V1, V2, V3, V4, …**) is the modern
functional-retinotopic nomenclature for the extrastriate visual areas.
It has the following properties that make it **structurally clean** in
a way that the Brodmann scheme is not:

    Retinotopic signature
        Each V area is defined by its **retinotopic map** — a
        systematic, mirror-flipped representation of the
        contralateral hemifield. The retinotopic map is
        **architectonically independent of the BA boundary**: two
        different BAs may share a single V area, and two different
        V areas may share a single BA.

    Functional specialization
        Each V area is defined by its **functional specialization**
        — V1 for low-level features, V2 for border ownership and
        texture, V3 for dynamic form and motion boundaries, V4 for
        color and form. This is a **stronger** and **more
        mechanistically grounded** definition than the BA scheme,
        which is defined by cytoarchitecture alone.

    Modern continuity
        The V-numbering scheme is **in continuous use** in modern
        visual neuroscience, unlike the BA scheme (which is
        historical for most of the cortex). The four V areas
        modelled here (V1–V4) are the **core of the visual
        hierarchy** and are agreed upon by essentially every
        modern parcellation (HCP, Öngür-Price, Petrides-Pandya,
        and the retinotopic-mapping literature).

**Consequence for the architecture**: this ``cortex`` package is the
**primary** functional decomposition of the occipital lobe, and
downstream code that needs a functional visual area should query here
first. The ``..brodmann_areas`` package is the **cytoarchitectonic**
decomposition, which is required for those questions (e.g., "is this
V2 or V3?") where the BA boundary provides additional resolution. Both
packages are required; neither subsumes the other.

--------------------------------------------------------------------------------
THE BA ↔ V CROSSWALK — THIS PACKAGE'S CRITICAL CONTRACT
--------------------------------------------------------------------------------

The **single most important structural concern** of this package is the
**BA ↔ V crosswalk**. The BA decomposition and the V decomposition are
**independent** and **overlapping**:

    BA 17  ↔  V1                             (1:1 — tight)
    BA 18  ↔  V2, V3                         (1:2 — partial)
    BA 19  ↔  V3, V4, V3A, V3B, V5/MT+, LOC  (1:6 — partial,
                                              with four forward
                                              references)

**The crosswalk lives in ``..occipital``**, in the parent's
``BA_TO_V_CROSSWALK`` and ``V_TO_BA_CROSSWALK`` registries. This
package **re-exports** those registries — it does **not** redefine them.
The single-source-of-truth rule is required because:

  * ``..occipital`` is the parent of both ``brodmann_areas`` and
    ``cortex``, and it is where the two decompositions must be
    reconciled.
  * ``..brodmann_areas`` also re-exports the same dicts, and the two
    branches must use the same source.
  * Any drift between the copies of the crosswalk would be a silent
    bug that makes downstream "which BA contains this V area?"
    queries return inconsistent results.

**The crosswalk must be complete in both directions** — every V child
must declare its BA correlates (in its own ``BRODMANN_CORRELATES``
field), and the parent's ``BA_TO_V_CROSSWALK`` and
``V_TO_BA_CROSSWALK`` must be exact inverses of each other. The
parent inversion function must fail loudly if the two registries
diverge.

**The crosswalk is hemisphere-invariant** — the V-to-BA mapping is a
property of the occipital lobe itself, not of the hemisphere. The
left and right ``cortex`` parents must re-export **byte-identical**
crosswalk dicts.

**A special note on V3.** V3 is **the only V area in the current
tree whose BA correlate spans two BAs** — V3 ↔ (BA 18, BA 19). The
lateral portion of V3 extends into BA 19 territory, while the
dorsomedial portion remains in BA 18. This is why V3 appears in
**both** ``..brodmann_areas/brodmann_area_18/`` and
``..brodmann_areas/brodmann_area_19/``, and why the V3 package must
cross-reference both.

--------------------------------------------------------------------------------
THE V-AREA FORWARD REFERENCES
--------------------------------------------------------------------------------

The parent crosswalk references **six V-numbered functional areas**,
but only four of them are **current children** of this package:

    Current children of this package:
        primary_visual_cortex   (V1)   — BA 17
        v2                             — BA 18
        v3                             — BA 18 + BA 19
        v4                             — BA 19

    Forward references (not yet packages):
        V3A                     — BA 19 (motion-in-depth and
                                  motion-boundary area; **core node
                                  of the right dorsal attention
                                  network — the left's V3A is part
                                  of the dorsal stream but less
                                  dominant**)
        V3B                     — BA 19 (kinetic-occipital area;
                                  motion processing)
        V5 / MT+                — BA 19 (motion area; **more strongly
                                  engaged on the right** for
                                  visuospatial attention and
                                  motion-in-space processing)
        LOC (lateral occipital   — BA 19 (object-recognition complex;
             complex)             **right LOC feeds the right FFA
                                  face-recognition endpoint** via
                                  the ventral stream)

**The crosswalk must be tolerant of forward references.** The parent's
``V_TO_BA_CROSSWALK`` includes entries for V3A, V3B, V5/MT+, and LOC,
each mapped to ``(19,)``, but those entries are **forward references**
— the packages do not yet exist under this ``..cortex`` parent. The
parent must accept such entries and record them as **forward
references** rather than failing.

**The four forward references must be resolved before this package's
own child set is considered complete**, because the full V1–V5/MT+
hierarchy and the full V1–LOC object-recognition pathway are the
substrate of motion perception and face processing respectively, and
those domains are **not fully covered by V1–V4 alone**. See the
``DOMAIN_COVERAGE`` section below.

**This tolerance is the only "forward reference" mechanism in the
occipital ``cortex`` package** — there are no missing V children
within V1–V4 and no missing bounding gyri. The forward references are
entirely on the **V5/MT+, V3A, V3B, and LOC** side, and they are
documented on the affected V-area entries in the parent crosswalk,
not here. This package only needs to record them and defer.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAIN COVERAGE — WHAT V1–V4 COVER AND WHAT THEY DO NOT
--------------------------------------------------------------------------------

The **twelve** occipital functional domains are distributed across the
**twelve** known V-numbered areas (V1, V2, V3, V4, V3A, V3B, V5/MT+,
LOC, plus downstream FFA, VWFA, and others). The **four current
children** of this package (V1–V4) cover **six** of the twelve
domains:

    DOMAIN_COVERAGE (by the four current V children):
        primary_visual_processing     (V1)
        retinotopic_organization      (V1, V2, V3, V4 — all
                                       retinotopic)
        binocular_vision              (V1, V2)
        form_and_object_perception    (V2, V3, V4 — early stages)
        spatial_localization          (V3 — motion boundaries;
                                       full spatial localization
                                       requires V3A, V5/MT+)
        color_vision                  (V4)

    DOMAINS NOT COVERED by the four current children:
        motion_perception             — **V5/MT+** (forward
                                       reference)
        visual_attention              — **V3A / V5/MT+** as
                                       targets (forward reference)
        face_processing               — **right FFA** downstream
                                       of LOC (right-only domain)
        global_visual_processing      — **right BA 18 emphasis**
                                       (right-only domain)
        visual_word_processing        — **left VWFA** downstream
                                       of LOC (left-lateralized)
        local_featural_processing     — **left BA 18 emphasis**
                                       (left-lateralized)

**The left hemisphere's six-domain coverage by V1–V4 is biased toward
the ventral stream** (form, object, color) and the **early stages of
spatial localization** (V3's motion boundaries). The remaining six
domains are either **dorsal-stream** functions of the forward-reference
areas (V3A, V5/MT+) or **lateralized emphasis / downstream** functions
of the face, reading, and global-processing pathways.

**Downstream code must not assume that V1–V4 alone are the complete
occipital functional hierarchy.** The four current children are the
**core** of the hierarchy but not the whole of it. Motion perception
requires V5/MT+, spatial attention requires V3A / V5/MT+, face
processing requires the right FFA (downstream of right LOC), and
reading requires the left VWFA (downstream of left LOC). All of these
are **downstream of the current children** and must be cross-referenced
through the forward-reference mechanism or through the temporal-lobe
packages.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAIN EMPHASIS (left-hemisphere-specific, per V child)
--------------------------------------------------------------------------------

The left-side emphasis for each of the four current V children is:

    V1 (primary_visual_cortex)    primary_visual_processing,
                                  retinotopic_organization,
                                  binocular_vision
                                  **On the left, V1 processes the
                                  RIGHT visual hemifield.** The
                                  primary contribution is the first
                                  cortical stage of vision —
                                  orientation, contrast, spatial
                                  frequency, retinotopic mapping.

    V2                             primary_visual_processing
                                  (secondary),
                                  binocular_vision,
                                  form_and_object_perception
                                  (border ownership, texture,
                                  illusory contours, surface
                                  filling-in)
                                  **On the left, V2's form-and-
                                  object contribution is weighted
                                  toward the LOCAL / FEATURAL
                                  aspect** (Navon's local-
                                  precedence asymmetry, the
                                  mirror of the right's global-
                                  precedence). **The left V2's
                                  LOCAL emphasis is the primary
                                  left-lateralized occipital
                                  contribution** and is
                                  documented in the left BA 18
                                  sibling as the
                                  `form_and_object_perception_
                                  local_featural` emphasis.

    V3                             form_and_object_perception
                                  (dynamic form),
                                  spatial_localization
                                  (motion boundaries, depth
                                  from motion)
                                  **On the left, V3's
                                  spatial-localization
                                  contribution is present but
                                  **weaker than the right's** —
                                  the right V3 is more strongly
                                  engaged during visuospatial
                                  attention and motion-in-space
                                  processing. The left V3's
                                  contribution is predominantly
                                  to the **ventral stream**
                                  (dynamic form feeding V4 and
                                  the LOC) rather than the
                                  dorsal stream.

    V4                             color_vision,
                                  form_and_object_perception
                                  (ventral stream origin)
                                  **On the left, V4 is the
                                  origin of the left ventral
                                  stream** — the pathway that
                                  feeds the left LOC and, from
                                  there, the left visual word
                                  form area (VWFA) for reading.
                                  **The left V4 is also
                                  weighted toward the
                                  color-form-language
                                  integration** — the left V4
                                  → LOC → left VWFA pathway
                                  carries color information
                                  forward to the reading
                                  network, and left V4
                                  lesions produce **color
                                  agnosia** and **color-form-
                                  language integration
                                  deficits** that have no
                                  symmetric counterpart on
                                  the right.

**The left-specific caveats**:

  * **`visual_word_processing` is a left-lateralized function that
    V4 and the LOC collectively support** — via the left V4 → LOC
    → left VWFA pathway. **No single V child claims this domain as
    a primary contribution**; V4's emphasis is `color_vision` and
    `form_and_object_perception`, and `visual_word_processing` is a
    downstream property of the left occipital + left fusiform
    pathway.
  * **`face_processing` is right-lateralized** and does **not**
    appear in the left V children at the same weighting.
  * **`global_visual_processing` is right-lateralized** and does
    **not** appear in the left V children. The left's emphasis is
    on **local / featural processing** (V2's emphasis, and the
    left BA 18's emphasis in the BA sibling).
  * **`motion_perception` and `visual_attention`** — the left V
    children (V3 alone, without V3A / V5/MT+) contribute to the
    early stages of these domains but do not cover them fully. The
    dominant contributions are in the forward-reference areas
    (V3A, V5/MT+), and the dominant hemisphere is the right.

**The V children share these domain assignments; the parent captures
the left-specific emphasis per V child. The `LEFT_LATERALIZED_
FUNCTIONS` and `RIGHT_ONLY_DOMAINS` tuples must be byte-identical
(as sets) to the corresponding tuples in the sibling
``..brodmann_areas`` package** — the left-lateralized and
right-only functions are properties of the occipital lobe, not of
the decomposition scheme.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..occipital
    The parent occipital lobe. This package's parent and the source
    of the ``BA_TO_V_CROSSWALK``, ``V_TO_BA_CROSSWALK``, and
    ``DOMAIN_TO_CHILDREN`` registries. This package **re-exports**
    those indices; it does not redefine them.

..brodmann_areas
    The **cytoarchitectonic sibling** of this package. Where this
    package decomposes the occipital lobe **functionally /
    retinotopically** (V1–V4 + four forward references), the
    ``..brodmann_areas`` package decomposes the **same territory
    cytoarchitectonically** (BA 17, BA 18, BA 19). The two
    decompositions overlap and must be cross-referenced via the
    parent's ``BA_TO_V_CROSSWALK``. **Neither is a child of the
    other** — they are parallel decompositions of the same
    territory, and downstream code must query the one that matches
    its question ("which functional area?" → ``..cortex``;
    "which cytoarchitectonic area?" → ``..brodmann_areas``).

..cuneus
    The medial-surface gyral landmark for V1's upper bank. The
    ``..cuneus`` package cross-references V1 as its primary
    functional overlay. **On the left, the cuneus's V1 upper bank
    represents the lower RIGHT visual field.**

..gyri
    The lateral-surface gyral child. The lateral occipital gyrus
    overlays the LOC (a forward reference) and the lateral
    portion of V3. **On the left, the lateral occipital gyrus's
    LOC is part of the left reading pathway** (LOC → left VWFA).

..sulci
    The sulcal child. The calcarine sulcus is the surface
    landmark for V1; the lunate sulcus (when present) marks the
    V1/V2 border on the lateral surface; the transverse
    occipital sulcus is the posterior boundary of the lateral
    occipital gyri and the V3A / V3B territory.

..cortex.temporal
    The **ventral stream** continues from V4 and the LOC into the
    temporal lobe (inferior temporal cortex, fusiform gyrus,
    VWFA, FFA). **On the left, the ventral stream terminates in
    the left VWFA** (the reading area), and the left V4 is the
    origin of this pathway. **Right occipito-temporal lesions
    produce prosopagnosia** — the canonical right-lateralized
    visual-recognition deficit — but the right V4's contribution
    to the FFA is via the right LOC, and this is documented in
    the right sibling's cross-references. The temporal package
    must declare the left V4 as a source of its visual input for
    the ventral stream, and must note the **left-lateralized
    VWFA** specialization.

..cortex.parietal
    The **dorsal stream** continues from V3 (and from V3A, V5/MT+
    in the forward references) into the parietal lobe. **On the
    left, the dorsal stream supports right-hemifield spatial
    attention**, but the left's contribution is weaker than the
    right's (documented in the right sibling's cross-references
    to the right parietal and right frontal territories). The
    parietal package must declare the left V3 as a source of its
    visual input for the dorsal stream, and must note the
    right-lateralized attentional emphasis.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V1, V2, V3, and V4. The frontal package must
    declare these V children as targets of its attentional
    projections.

..cortex.cingulate  — indirect
    No direct cingulate → V-numbered projection. Recorded here to
    pre-empt a false cross-reference.

..cortex.insular  — indirect
    No direct insular → V-numbered projection. Recorded here to
    pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the thalamic relay from the retina to V1. The
    LGN → V1 projection is the anatomical substrate of primary
    visual processing. The thalamus package must declare the LGN
    as the primary visual thalamic relay to the left V1.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar is V2, V3, and V4's dominant thalamic input
    (stronger to these areas than to V1), participating in the
    cortico-thalamo-cortical loops that support visual attention
    and visual short-term memory.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from V4 and the LOC to the
    perirhinal, entorhinal, and parahippocampal cortices. The
    left V4 is the origin of the occipito-temporal-hippocampal
    pathway that supports visual object recognition and visual
    memory.

../../right/cortex/occipital/cortex
    The right-hemisphere homologue. Structural fields
    (``BA_TO_V_CROSSWALK``, child names, V-numbering, hierarchy
    order, forward-reference list, FUNCTIONAL_DOMAINS coverage
    set, LEFT_LATERALIZED_FUNCTIONS, RIGHT_ONLY_DOMAINS) MUST be
    byte-identical to this package's, with the **only** differences
    being the **hemisphere** and the **represented visual
    hemifield** — the right V1–V4 process the LEFT visual
    hemifield, while the left V1–V4 process the RIGHT. See the
    right sibling for the right-lateralized clinical anchors
    (left hemiachromatopsia, prosopagnosia from right LOC → FFA,
    left hemifield akinetopsia more severe, left hemispatial
    neglect contribution) and the right-emphasized global /
    dorsal-stream functions.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    LOBE                = "occipital"
    HEMISPHERE          = "left"

    V_CHILDREN          = (
                              "primary_visual_cortex",
                              "v2",
                              "v3",
                              "v4",
                          )
        # **Hierarchy order**: V1 → V2 → V3 → V4. Downstream code
        # that traverses the visual hierarchy must follow this
        # order. **v3 is a special case** — its BA correlate
        # spans two BAs (BA 18 and BA 19), unlike the other V
        # children, which each map to a single BA.

    BA_TO_V_CROSSWALK   = {   # re-exported from ..occipital,
                              # NOT redefined — single source of
                              # truth. Byte-identical to the right
                              # sibling's.
                              17: ("primary_visual_cortex",),
                              18: ("v2", "v3"),
                              19: ("v3", "v4",
                                   "V3A", "V3B", "V5_MT_plus",
                                   "LOC"),
                          }

    V_TO_BA_CROSSWALK   = {   # re-exported from ..occipital,
                              # NOT redefined. Exact inverse of
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
        # **Byte-identical to the right sibling's.** When the V
        # packages are created, this tuple must be emptied in the
        # same commit, in both hemispheres.

    DOMAIN_COVERAGE     = {
        # Which domains the four current V children cover
        "primary_visual_processing":  ("primary_visual_cortex",),
        "retinotopic_organization":   ("primary_visual_cortex",
                                       "v2", "v3", "v4"),
        "binocular_vision":           ("primary_visual_cortex",
                                       "v2"),
        "form_and_object_perception": ("v2", "v3", "v4"),
        "spatial_localization":       ("v3",),   # early stages;
                                                 # full spatial
                                                 # requires V3A,
                                                 # V5/MT+
        "color_vision":               ("v4",),
    }

    DOMAINS_NOT_COVERED = {
        # Domains not covered by the four current V children
        # (each entry names where the domain lives)
        "motion_perception":          "V5_MT_plus (forward ref)",
        "visual_attention":           "V3A, V5_MT_plus (forward "
                                      "refs, as targets)",
        "face_processing":            "right_ffa (right-only, "
                                      "downstream of LOC)",
        "global_visual_processing":   "right_BA18 (right-only "
                                      "emphasis)",
        "visual_word_processing":     "left_vwfa (left-lateralized, "
                                      "downstream of LOC)",
        "local_featural_processing":  "left_BA18 (left-lateralized "
                                      "emphasis)",
    }

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** — the most important
        # single fact about the left V1–V4. Downstream code that
        # queries "what does the left V1–V4 see?" must receive
        # "the RIGHT visual hemifield." The contralateral rule is
        # enforced through this field.

    FUNCTIONAL_DOMAIN_EMPHASIS = {   # left-side emphasis per V
        "primary_visual_cortex": (
            "primary_visual_processing_right_hemifield",
            "retinotopic_organization_right_hemifield",
            "binocular_vision_right_hemifield_stereopsis",
        ),
        "v2": (
            "primary_visual_processing_secondary",
            "binocular_vision",
            "form_and_object_perception_local_featural",
        ),
        "v3": (
            "form_and_object_perception_dynamic_form",
            "spatial_localization_weaker_than_right",
        ),
        "v4": (
            "color_vision_color_form_language_integration",
            "form_and_object_perception_ventral_stream_origin_"
            "to_left_vwfa",
        ),
    }

    LEFT_LATERALIZED_FUNCTIONS = (
        "visual_word_processing",
        "local_featural_processing",
    )
        # **Byte-identical (as a set) to the sibling
        # ``..brodmann_areas`` package's
        # LEFT_LATERALIZED_FUNCTIONS tuple** — the left-lateralized
        # functions are properties of the left occipital lobe,
        # not of the decomposition scheme.

    RIGHT_ONLY_DOMAINS = (
        "face_processing",
        "global_visual_processing",
    )
        # **Byte-identical (as a set) to the sibling
        # ``..brodmann_areas`` package's RIGHT_ONLY_DOMAINS tuple.**

    __all__ = [
        "LOBE",
        "HEMISPHERE",
        "V_CHILDREN",
        "BA_TO_V_CROSSWALK",
        "V_TO_BA_CROSSWALK",
        "FORWARD_REFERENCE_V_AREAS",
        "DOMAIN_COVERAGE",
        "DOMAINS_NOT_COVERED",
        "VISUAL_HEMIFIELD",
        "FUNCTIONAL_DOMAIN_EMPHASIS",
        "LEFT_LATERALIZED_FUNCTIONS",
        "RIGHT_ONLY_DOMAINS",
    ]

No behaviour. This package is a declarative registry; all computation
that references the V-numbered packages lives in ``cortex/`` or
``memory/``.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``cortex/__init__.py`` must:

1. Import the four V children (no side effects):
       from . import primary_visual_cortex
       from . import v2
       from . import v3
       from . import v4

2. Re-export ``BA_TO_V_CROSSWALK`` and ``V_TO_BA_CROSSWALK`` from
   ``..occipital`` — **do not redefine them**. The occipital parent
   is the single source of truth for the BA ↔ V mapping, and both
   the ``..brodmann_areas`` and ``..cortex`` packages depend on the
   same dicts.

3. Expose ``FORWARD_REFERENCE_V_AREAS`` so downstream code querying
   "which V areas are current packages?" can distinguish between
   **resolved** V areas (V1, V2, V3, V4) and **forward-reference**
   V areas (V3A, V3B, V5/MT+, LOC).

4. Expose ``DOMAIN_COVERAGE`` and ``DOMAINS_NOT_COVERED`` as a
   **left-side view** of the four current V children's domain
   coverage. These are hand-written and are where the **coverage
   gaps** (the six domains not covered by V1–V4) are made explicit.
   Downstream code that needs motion, attention, or face / reading
   processing must consult ``DOMAINS_NOT_COVERED`` to find where
   those domains live.

5. Expose ``VISUAL_HEMIFIELD`` = ``"right"`` — the represented
   visual hemifield is the **RIGHT** hemifield on the left side.
   This is the single most important property of the left V1–V4,
   and it must be queryable rather than buried in prose.

6. Expose ``FUNCTIONAL_DOMAIN_EMPHASIS`` as a **left-side view** of
   the children's ``FUNCTIONAL_DOMAINS``. This differs from the
   right sibling's by:
       - V2: emphasis on `local_featural` form processing (right
         is `global_holistic`)
       - V3: emphasis on `weaker_than_right` spatial localization
       - V4: emphasis on `color_form_language_integration` and
         `to_left_vwfa` (right is `color_form_face_integration`
         and `to_right_ffa`)

7. Expose ``LEFT_LATERALIZED_FUNCTIONS`` and ``RIGHT_ONLY_DOMAINS``
   — **byte-identical (as sets) to the sibling ``..brodmann_
   areas`` package's corresponding tuples**. The complementarity
   invariant applies: the left's LEFT_LATERALIZED_FUNCTIONS must
   equal (as a set) the right's RIGHT_ONLY_DOMAINS, and vice
   versa. This **cross-scheme** byte-identity is required so
   that downstream code that queries the same domain through
   either the ``..cortex`` or the ``..brodmann_areas`` package
   receives the same answer.

8. Define ``__all__`` as shown in the implementation contract.

9. Contain **no** logic beyond the above.

--------------------------------------------------------------------------------
FORWARD-REFERENCE CAVEAT
--------------------------------------------------------------------------------

**The only forward-reference caveat for this package is on the V-area
side, not the BA side** — and it is the largest in the cortex tree
(shared with the ``..brodmann_areas`` sibling). All four V children
(V1, V2, V3, V4) exist as packages under this ``..cortex/`` parent,
and all their structural fields resolve. The **four forward
references** — V3A, V3B, V5/MT+, LOC — are documented in the parent
``..occipital``'s ``FORWARD_REFERENCE_V_AREAS`` tuple and are listed
in this package's ``FORWARD_REFERENCE_V_AREAS`` re-export.

**The four forward references must be resolved before this package's
own child set is considered complete**, because they cover four of
the twelve occipital functional domains that V1–V4 do not:
motion_perception (V5/MT+), visual_attention (V3A / V5/MT+ as
targets), face_processing (via LOC → right FFA — but the **occipital
input stage** LOC is a V-area forward reference), and
visual_word_processing (via LOC → left VWFA — the **occipital input
stage** LOC is also a forward reference). When they are created
under this ``..cortex/`` parent:

  1. Add the V packages under this parent.
  2. Remove the corresponding entries from
     ``FORWARD_REFERENCE_V_AREAS`` in this package **and** in the
     right sibling, in the same commit.
  3. Update ``DOMAIN_COVERAGE`` to add the new domains.
  4. Update ``DOMAINS_NOT_COVERED`` to remove the newly covered
     domains.
  5. Update each V child's ``BRODMANN_CORRELATES`` to declare the
     same BA number(s) as the parent's ``V_TO_BA_CROSSWALK``.
  6. Verify the parent's ``BA_TO_V_CROSSWALK`` and
     ``V_TO_BA_CROSSWALK`` remain exact inverses after the update.

**No asymmetry is permitted in the V-area forward references** — both
hemispheres must declare the same forward-reference list and must
resolve them in the same commit.

--------------------------------------------------------------------------------
PROMOTION RULE (when a V area gains a sub-package)
--------------------------------------------------------------------------------

The four current V children (V1, V2, V3, V4) are **already canonical
V-numbered areas** and do not need promotion. The only conceivable
promotions are:

1. **V3 → V3d + V3v**. Some parcellations split V3 into a dorsal
   (V3d) and a ventral (V3v) component, with the dorsal component
   sharing more properties with V3A and the ventral component
   sharing more properties with V4. **If this split is performed,
   it must be mirrored by a corresponding split of BA 18's and BA
   19's V_AREA_CORRELATE entries**, because V3 is shared between
   the two BAs.

2. **V4 → V4 + V4α (V4v)**. Some parcellations split V4 into a
   lateral component (V4) and a ventral component in the collateral
   sulcus (V4α / V4v). **If this split is performed, the V4
   package's own BA correlate remains (19,), but the two
   sub-packages may have different clinical signatures** (V4α is
   closer to the fusiform face area, V4 is closer to the
   lateral-occipital LOC).

3. **Forward reference → full V package**. When V3A, V3B, V5/MT+,
   or LOC is created, the promotion is **not** a sub-package of an
   existing V child — it is a **new child of this ``..cortex``
   parent**, added in the same commit as its removal from the
   ``FORWARD_REFERENCE_V_AREAS`` list.

**None of these promotions is recommended in the current tree.**
The four current V children are canonical and stable; V3A, V3B,
V5/MT+, and LOC are the more urgent work.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/cortex/occipital/cortex``:

    MUST be identical (byte-for-byte):
        LOBE                          "occipital"
        V_CHILDREN                    the same four child names,
                                      in the same hierarchy order
                                      (V1, V2, V3, V4)
        BA_TO_V_CROSSWALK             the same BA → V mapping
        V_TO_BA_CROSSWALK             the same V → BA mapping
                                      (exact inverse)
        FORWARD_REFERENCE_V_AREAS     the same four V areas
                                      (V3A, V3B, V5/MT+, LOC)
        DOMAIN_COVERAGE               the same four-child
                                      coverage structure
        DOMAINS_NOT_COVERED           the same six entries
                                      (with the same target
                                      locations)
        LEFT_LATERALIZED_FUNCTIONS    the same set (though the
                                      tuple is **empty on the
                                      right** — see below)
        RIGHT_ONLY_DOMAINS            the same set (though the
                                      tuple is **empty on the
                                      left** — see below)
        The V children's structural fields (AREA_NAME, LOBE,
                                      V_NUMBER, BRODMANN_
                                      CORRELATES, RETINOTOPIC_MAP)
        The forward-reference caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       **"right"** (left) vs **"left"**
                               (right) — the most important
                               lateralized field. The
                               contralateral-visual-field rule
                               is the defining property of the
                               occipital cortex, and downstream
                               code must receive the correct
                               hemifield from each side.
        FUNCTIONAL_DOMAIN_EMPHASIS   left: V2 is "local_featural";
                               V3 is "weaker_than_right"; V4 is
                               "color_form_language_integration"
                               and "to_left_vwfa".
                               right: V2 is "global_holistic";
                               V3 is "dominant"; V4 is "color_
                               form_face_integration" and
                               "to_right_ffa".
        LEFT_LATERALIZED_FUNCTIONS   left: ("visual_word_
                               processing", "local_featural_
                               processing").
                               right: () — the right's
                               LEFT_LATERALIZED_FUNCTIONS
                               tuple is **empty**.
        RIGHT_ONLY_DOMAINS           left: () — the left's
                               RIGHT_ONLY_DOMAINS tuple is
                               **empty**.
                               right: ("face_processing",
                               "global_visual_processing").
        CLINICAL_ANCHORS       left: right homonymous
                               hemianopia (V1); right hemiachroma-
                               topsia (V4); right hemifield
                               akinetopsia (V3 / V5/MT+); pure
                               alexia without agraphia (left
                               V4 + splenium); color agnosia
                               (left V4); visual object agnosia
                               (bilateral); right hemifield
                               motion deficit in daily life;
                               color-form-language integration
                               deficit (left V4 → VWFA); PCA
                               with progressive reading deficits
                               (left); plus the hemisphere-
                               invariant anchors (cortical
                               blindness, Anton syndrome,
                               blindsight, migraine aura,
                               occipital epilepsy, PCA, PRES,
                               occipital infarct).
                               right: left homonymous
                               hemianopia (V1); left
                               hemiachromatopsia (V4); left
                               hemifield akinetopsia **more
                               severe** (V3 / V5/MT+);
                               prosopagnosia (right LOC →
                               FFA); left hemispatial neglect
                               (right V3A / V5/MT+ → right
                               IPS); right motion hemisphere
                               emphasis; global visual
                               processing contribution; PCA
                               with Benson syndrome (right);
                               plus the hemisphere-invariant
                               anchors.

**The complementarity invariant is verified across schemes.** The
left's ``LEFT_LATERALIZED_FUNCTIONS`` must equal (as a set) the
right's ``RIGHT_ONLY_DOMAINS``, and the left's ``RIGHT_ONLY_DOMAINS``
must equal (as a set) the right's ``LEFT_LATERALIZED_FUNCTIONS``.
**This invariant must hold not only within this package but also
across the ``..brodmann_areas`` sibling** — the left's
``LEFT_LATERALIZED_FUNCTIONS`` in this package must equal the left
``..brodmann_areas``'s ``LEFT_LATERALIZED_FUNCTIONS``, and likewise
for the right side.

**The `VISUAL_HEMIFIELD` field is the sharpest single entry in this
contract.** Left V1–V4 = right hemifield; right V1–V4 = left
hemifield. Any downstream code that queries "what does the left V1–V4
see?" must receive `"right"`, and any downstream code that queries
"what does the right V1–V4 see?" must receive `"left"`. Averaging the
two would erase the fundamental contralateral-visual-field
organization.

**The `FUNCTIONAL_DOMAIN_EMPHASIS` asymmetry is the second sharpest
entry.** Both hemispheres carry the same four V children with the
same FUNCTIONAL_DOMAINS **coverage** (V1–V4 cover the same six
domains on both sides), but the **emphasis** within those domains
diverges — the left emphasizes local processing, the weaker spatial
localization, and the color-form-language / VWFA pathway; the right
emphasizes global processing, dominant spatial localization, and
the color-form-face / FFA pathway.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/cortex/`` — a sibling of
    ``brodmann_areas``, ``cuneus``, ``gyri``, and ``sulci``.
[ ] All four V children are imported and registered.
[ ] ``V_CHILDREN`` lists the four child names in **hierarchy
    order** (V1, V2, V3, V4) and is byte-identical to the right
    sibling's.
[ ] ``BA_TO_V_CROSSWALK`` is **re-exported** from ``..occipital``,
    not redefined, and is byte-identical to the right sibling's
    AND to the sibling ``..brodmann_areas`` package's.
[ ] ``V_TO_BA_CROSSWALK`` is **re-exported** from ``..occipital``,
    not redefined, is byte-identical to the right sibling's, and is
    an exact inverse of ``BA_TO_V_CROSSWALK``.
[ ] ``FORWARD_REFERENCE_V_AREAS`` is present, lists exactly the
    four forward references (V3A, V3B, V5/MT+, LOC), and is
    byte-identical to the right sibling's.
[ ] **`v3` is noted as the only V child whose BA correlate spans
    two BAs** — V3 ↔ (BA 18, BA 19). The V3 package must
    cross-reference both BAs, and both BA 18 and BA 19 packages
    must include V3 in their `V_AREA_CORRELATE`.
[ ] ``DOMAIN_COVERAGE`` lists exactly the six domains covered by
    the four current V children:
    - primary_visual_processing (V1)
    - retinotopic_organization (V1, V2, V3, V4)
    - binocular_vision (V1, V2)
    - form_and_object_perception (V2, V3, V4)
    - spatial_localization (V3, early stages)
    - color_vision (V4)
[ ] ``DOMAINS_NOT_COVERED`` lists exactly the six domains **not**
    covered by the four current V children, with their target
    locations:
    - motion_perception → V5/MT+ (forward ref)
    - visual_attention → V3A / V5/MT+ (forward refs, as targets)
    - face_processing → right FFA (right-only, downstream)
    - global_visual_processing → right BA 18 (right-only emphasis)
    - visual_word_processing → left VWFA (left-lateralized,
      downstream)
    - local_featural_processing → left BA 18 (left-lateralized
      emphasis)
[ ] **`VISUAL_HEMIFIELD` = "right"** is present as a first-class,
    queryable field, not buried in prose. The contralateral-
    visual-field rule is enforced.
[ ] ``FUNCTIONAL_DOMAIN_EMPHASIS`` captures the **left-side
    emphasis** per V child:
    - V1: primary_visual_processing, retinotopic_organization,
      binocular_vision (RIGHT hemifield)
    - V2: primary_visual_processing_secondary, binocular_vision,
      **form_and_object_perception_local_featural**
    - V3: form_and_object_perception_dynamic_form,
      spatial_localization_weaker_than_right
    - V4: **color_vision_color_form_language_integration**,
      **form_and_object_perception_ventral_stream_origin_to_left_
      vwfa**
[ ] ``LEFT_LATERALIZED_FUNCTIONS`` is present with exactly
    ``("visual_word_processing", "local_featural_processing")`` and
    is **byte-identical (as a set) to the sibling
    ``..brodmann_areas`` package's tuple**.
[ ] ``RIGHT_ONLY_DOMAINS`` is present with exactly
    ``("face_processing", "global_visual_processing")`` and is
    **byte-identical (as a set) to the sibling
    ``..brodmann_areas`` package's tuple**.
[ ] **The complementarity invariant is verified across schemes**:
    - left's LEFT_LATERALIZED_FUNCTIONS = right's
      RIGHT_ONLY_DOMAINS (as a set)
    - left's RIGHT_ONLY_DOMAINS = right's LEFT_LATERALIZED_
      FUNCTIONS (as a set)
    - left's LEFT_LATERALIZED_FUNCTIONS = left's sibling
      `..brodmann_areas`'s LEFT_LATERALIZED_FUNCTIONS (byte-
      identical)
    - right's RIGHT_ONLY_DOMAINS = right's sibling
      `..brodmann_areas`'s RIGHT_ONLY_DOMAINS (byte-identical)
[ ] The **V-numbering scheme is clean** — no `PARCELATION_
    AMBIGUITY` field is required, no `MODERN_CROSSWALK` field is
    required, and there are no naming collisions. The four V
    children are canonical, stable across modern parcellations,
    and defined by retinotopic signatures.
[ ] The **BA ↔ V crosswalk source-of-truth rule** is documented:
    the crosswalk lives in ``..occipital``, this package
    re-exports it, and any redefinition here would be a bug.
[ ] The **`..brodmann_areas` and `..cortex` relationship** is
    documented as **parallel decompositions**, not parent-child.
    Downstream code querying "which functional area?" goes through
    ``..cortex``; downstream code querying "which cytoarchitectonic
    area?" goes through ``..brodmann_areas``. **Neither is
    canonical for both questions.**
[ ] The **cuneus placement** is documented as a **sibling of this
    package** (a direct child of ``..occipital``, not of
    ``..cortex``). The cuneus is a medial-surface gyral landmark,
    not a V area, and it is cross-referenced here as V1's upper-
    bank surface landmark.
[ ] The **forward references** (V3A, V3B, V5/MT+, LOC) are
    documented, the `FORWARD_REFERENCE_V_AREAS` tuple is
    re-exported, and the **resolution rule** is recorded (add the
    V package, remove the forward reference from both hemispheres
    in the same commit, update DOMAIN_COVERAGE and DOMAINS_NOT_
    COVERED).
[ ] The **V1–V4 domain coverage is explicitly partial** — the
    six covered domains are listed, and the six uncovered domains
    are listed with their target locations. **Downstream code must
    not assume V1–V4 alone are the complete occipital hierarchy.**
[ ] The **left V4 → LOC → left VWFA pathway** is documented as
    the left reading pathway, with pure alexia without agraphia
    (when the splenium is also involved) and color agnosia as
    its left-lateralized clinical anchors.
[ ] The **right V4 → LOC → right FFA pathway** is cross-referenced
    from the right sibling as the face-recognition pathway, with
    prosopagnosia as its right-lateralized clinical anchor.
[ ] The **`VISUAL_HEMIFIELD` field is byte-identical to the
    contralateral of the right sibling's** — left = "right",
    right = "left".
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V children names and order, BA↔V crosswalk, forward
    references, DOMAIN_COVERAGE, DOMAINS_NOT_COVERED structure,
    forward-reference caveat text) match the right sibling;
    VISUAL_HEMIFIELD, FUNCTIONAL_DOMAIN_EMPHASIS, the
    LEFT_LATERALIZED_FUNCTIONS / RIGHT_ONLY_DOMAINS values, and
    CLINICAL_ANCHORS deliberately differ, and the **cross-scheme
    complementarity** (this package's lateralized-domain tuples
    match the sibling `..brodmann_areas` package's) is verified.
[ ] Any downstream code querying "what does the left V1–V4 see?"
    must receive "the RIGHT visual hemifield" — the
    contralateral-visual-field rule is enforced through
    `VISUAL_HEMIFIELD`.
[ ] Any downstream code querying "which V areas are current
    packages?" must receive the four children (V1, V2, V3, V4)
    plus the four forward references (V3A, V3B, V5/MT+, LOC),
    with the forward references marked.
[ ] Any downstream code querying "what is V3?" must receive
    "V3 / BA 18 + BA 19 / dynamic form + motion boundaries" —
    the two-BA identity is enforced.
[ ] Any downstream code querying "what does the left V4 feed?"
    must receive "the left LOC, and from there the left VWFA
    (reading)" — the left ventral-stream endpoint.
[ ] Any downstream code querying "what does the right V4 feed?"
    must receive "the right LOC, and from there the right FFA
    (faces)" — the right ventral-stream endpoint (documented in
    the right sibling).
"""