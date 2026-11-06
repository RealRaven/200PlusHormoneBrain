"""
Occipital Brodmann Areas — Right Hemisphere
============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── brodmann_areas   ← THIS PACKAGE

This is a **cytoarchitectonic-collection parent** — a registry package
whose children are the three Brodmann-area packages assigned to the
right occipital lobe. It is the **cytoarchitectonic** counterpart of
``..cortex`` (the functional V-numbered parent) and the sibling of
``..cuneus``, ``..gyri``, and ``..sulci`` under ``..occipital``.

Parent: ``..occipital`` — the right occipital lobe. Sibling to
``..cortex``, ``..cuneus``, ``..gyri``, and ``..sulci``.

This package is the **structural mirror** of
``../../left/cortex/occipital/brodmann_areas``. The three BA
children, their names, their BA numbers, and their V-area correlates
are identical on both sides; the **functional emphasis** and
**clinical significance** of each BA diverge between hemispheres in
the same way that the occipital lobe itself diverges (right → face
processing, visuospatial attention, global visual processing;
left → verbal visual processing, local / featural processing).

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
as equivalent-sized units. **On the right, BA 19's dorsal-stream end
(V3A, V5/MT+) is the more strongly engaged side**, and BA 19's
ventral-stream end (V4) terminates at the right FFA rather than at the
left VWFA.

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

**This caveat text is byte-identical to the left sibling's** — the
BA numbering is a species-level convention, not a hemisphere-level one.

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

**The crosswalk's ASYMMETRY is also hemisphere-invariant.** BA 19's
coverage of V3A, V4, V5/MT+, V3B, and LOC is the same on both sides.
What differs is **which of BA 19's V correlates is the dominant
functional contributor** — on the right, V3A and V5/MT+ are the
dominant dorsal-stream contributors (visuospatial attention, motion),
while on the left V4 and the LOC-side ventral-stream contributors
dominate (form, color, the reading pathway). The crosswalk dict itself
does not record which is dominant; that asymmetry lives in
`FUNCTIONAL_DOMAIN_EMPHASIS`.

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
                                  attention network — the right
                                  V3A is more strongly engaged
                                  than the left V3A**)
        V3B                     — BA 19 (kinetic-occipital area;
                                  **more strongly engaged on the
                                  right** for motion-in-depth and
                                  kinetic contours)
        V5 / MT+                — BA 19 (motion area; **more strongly
                                  engaged on the right** for
                                  visuospatial attention and
                                  motion-in-space processing)
        LOC (lateral occipital   — BA 19 (object-recognition complex;
             complex)             **right LOC contributes to the
                                  right FFA face-recognition
                                  endpoint** via the ventral
                                  stream)

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

**The forward-reference list is byte-identical to the left sibling's.**
The four V areas (V3A, V3B, V5/MT+, LOC) are forward references on
both sides, and the resolution rule (clear the entry from both
hemispheres in the same commit) applies symmetrically.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAIN EMPHASIS (right-hemisphere-specific)
--------------------------------------------------------------------------------

This package's children collectively cover **all twelve** occipital
functional domains, plus the two **right-emphasized** domains
(`face_processing`, `global_visual_processing`) that the left side
does not carry at the same weighting. The **right-side emphasis** per
BA is:

    BA 17 (V1)     primary_visual_processing,
                   retinotopic_organization,
                   binocular_vision
                   **On the right, V1 processes the LEFT visual
                   hemifield.** The primary contribution is the
                   first cortical stage of vision — orientation,
                   contrast, spatial frequency, retinotopic mapping.
                   The right V1 is also a target of the right
                   ventral attention network (with right TPJ and
                   right FEF) that reorients to salient visual
                   events.

    BA 18 (V2+V3)  primary_visual_processing (secondary),
                   binocular_vision,
                   form_and_object_perception (surface / texture
                   / border ownership),
                   spatial_localization (V3)
                   **On the right, BA 18's form and object
                   contribution is weighted toward the GLOBAL /
                   HOLISTIC aspect** — the right hemisphere's
                   documented advantage in global processing
                   (Navon's global-precedence asymmetry). The
                   left's BA 18 is weighted toward the local /
                   featural aspect.

    BA 19 (V3A+V4+  color_vision (V4),
           V5/MT+)  motion_perception (**more strongly engaged on
                   the right** — right V5/MT+ is a core node of
                   the right-lateralized dorsal attention
                   network),
                   form_and_object_perception (V4, LOC — **right
                   LOC feeds the right FFA face-recognition
                   endpoint**),
                   spatial_localization (V3A — **more strongly
                   engaged on the right**),
                   visual_attention (**more strongly engaged on
                   the right** — right V3A and right MT/V5 are
                   core nodes of the right dorsal attention
                   network; right occipital lobe is a target of
                   the right ventral attention network)
                   **On the right, BA 19's contribution is
                   weighted toward the DORSAL stream** — V3A and
                   V5/MT+ drive the visuospatial attention and
                   motion-in-space processing that the right
                   hemisphere dominates. The right's ventral-
                   stream contribution (V4, LOC) is present, and
                   it feeds the right FFA face-recognition
                   endpoint via the right fusiform gyrus.

**The right-specific caveats**:

  * **`face_processing` is instantiated on the right** — via the
    right BA 19 ventral-stream output (V4, LOC) to the right FFA.
    **No single occipital BA claims `face_processing` as its
    primary contribution**; it is a network property of the right
    occipital + right fusiform pathway, documented at the
    `..occipital` parent level and on the right FFA in
    `..cortex.temporal`. BA 19 is the **occipital input stage** of
    this right-lateralized pathway.
  * **`global_visual_processing` is instantiated on the right** —
    via BA 18's global / holistic emphasis. This is a **right-only
    domain** that the left occipital BA children do not carry at
    the same weighting. It is documented in `FUNCTIONAL_DOMAIN_
    EMPHASIS` under BA 18 and routes to a `short_term` gestalt
    buffer.
  * **`visuospatial_attention` is more strongly engaged on the
    right** — the right BA 19's V3A and V5/MT+ are core nodes of
    the right dorsal attention network, and the right occipital
    lobe is a target of the right ventral attention network.
    Right parietal + frontal lesions produce **left hemispatial
    neglect**, the canonical right-lateralized attentional
    deficit, and the right occipital lobe is part of the substrate.
  * **`visual_word_processing` is left-lateralized** and does
    **not** appear in the right occipital BA children at the same
    weighting. The right BA 19's ventral-stream output supports
    form and object processing generally, and face processing
    specifically, but **not** reading. The left VWFA is the
    reading endpoint; the right occipital lobe does not feed an
    equivalent right-lateralized reading pathway.
  * **`local_featural_processing` is left-lateralized** and does
    **not** appear in the right occipital BA children. The right's
    documented advantage is in **global / holistic processing**,
    which is captured under BA 18's `global_visual_processing`
    emphasis and is a right-only domain.

**The BA children share these domain assignments; the parent captures
the right-specific emphasis per BA. The two right-emphasized domains
(`face_processing`, `global_visual_processing`) are absent from the
left sibling's `FUNCTIONAL_DOMAIN_EMPHASIS` and present here; the two
left-lateralized functions (`visual_word_processing`,
`local_featural_processing`) are present on the left sibling and
absent here.**

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
    **On the right, V3A and V5/MT+ are the more strongly engaged
    dorsal-stream areas**, and the right LOC feeds the right FFA.

..cuneus
    The medial-surface gyral landmark for V1's upper bank. The BA 17
    child's V1 representation extends into the cuneus's lower
    margin (the upper bank of the calcarine sulcus), and the
    ``..cuneus`` package cross-references BA 17 as its primary
    functional overlay. **On the right, the cuneus's V1 upper bank
    represents the lower LEFT visual field.**

..gyri
    The lateral-surface gyral child. The lateral occipital gyrus
    overlays BA 19 (the extrastriate territory), and the gyral
    package cross-references BA 19 as its primary functional
    overlay. On the right, the lateral occipital gyrus is part of
    the dorsal attention network substrate via its V3A and V5/MT+
    overlays.

..sulci
    The sulcal child. The calcarine sulcus is the surface landmark
    for BA 17's V1 representation; the lunate sulcus (when present)
    marks the BA 17 / BA 18 border on the lateral surface; the
    transverse occipital sulcus marks the posterior boundary of
    the lateral occipital gyri (BA 19 territory).

..cortex.temporal
    The **ventral stream** continues from BA 18 (V2 / V3) and BA 19
    (V4, LOC) into the temporal lobe (inferior temporal cortex,
    fusiform gyrus, VWFA, FFA). **The right FFA is the right-
    lateralized face-recognition endpoint of the BA 19 ventral
    stream**, and right occipito-temporal lesions produce
    prosopagnosia. The temporal package must declare the right BA
    18 and BA 19 as sources of its visual input for the ventral
    stream, and must note the right-lateralized FFA
    specialization.

..cortex.parietal
    The **dorsal stream** continues from BA 19 (V3A, V5/MT+) into
    the parietal lobe. **On the right, the dorsal stream is more
    strongly engaged** during visuospatial attention, and the
    right parietal lobe is a core node of the right-lateralized
    dorsal attention network. The parietal package must declare
    the right BA 19 as a source of its visual input for the dorsal
    stream, and must note the right-lateralized attentional
    emphasis.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** send top-down visual attentional signals to the
    occipital BA territories. **On the right, the right FEF is the
    dominant node of the ventral attention network**, and right
    frontal lesions contribute to left hemispatial neglect. The
    frontal package must declare the right occipital BA 18 and BA
    19 as targets of its attentional projections, and must note
    the right-lateralized attentional emphasis.

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
    right BA 17.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream terminates in the perirhinal, entorhinal,
    and parahippocampal cortices. **On the right, the
    parahippocampal place area (PPA) and the retrosplenial complex
    receive visual input supporting scene and spatial memory**,
    which are more strongly right-lateralized. The hippocampus
    package must declare the right occipital BA 18 and BA 19 as
    sources of its visual input, and must note the
    right-lateralized scene-memory emphasis.

../../left/cortex/occipital/brodmann_areas
    The left-hemisphere homologue. Structural fields
    (``BA_TO_V_CROSSWALK``, child names, BA numbers, V-area
    correlates, forward-reference list) MUST be byte-identical.
    Functional emphasis and clinical significance diverge — the
    right BA children are weighted toward the **left hemifield**,
    **face processing**, **visuospatial attention**, **global
    visual processing**, **dorsal-stream dominance**; the left BA
    children are weighted toward the **right hemifield**,
    **verbal visual processing**, **local / featural processing**,
    **ventral-stream dominance**.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    LOBE                = "occipital"
    HEMISPHERE          = "right"

    BA_CHILDREN         = (
                              "brodmann_area_17_primary_visual",
                              "brodmann_area_18",
                              "brodmann_area_19",
                          )

    BA_TO_V_CROSSWALK   = {   # re-exported from ..occipital,
                              # NOT redefined — single source of
                              # truth. Byte-identical to the left
                              # sibling's.
                              17: ("primary_visual_cortex",),
                              18: ("v2", "v3"),
                              19: ("v3", "v4",
                                   "V3A", "V3B", "V5_MT_plus",
                                   "LOC"),
                          }

    V_TO_BA_CROSSWALK   = {   # re-exported from ..occipital,
                              # NOT redefined — single source of
                              # truth. Must be an exact inverse of
                              # BA_TO_V_CROSSWALK. Byte-identical
                              # to the left sibling's.
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
        # **Byte-identical to the left sibling's.** When the V
        # packages are created, this tuple must be emptied in the
        # same commit, in both hemispheres.

    FUNCTIONAL_DOMAIN_EMPHASIS = {   # right-side emphasis per BA
        "brodmann_area_17_primary_visual": (
            "primary_visual_processing",
            "retinotopic_organization",
            "binocular_vision",
            "visual_attention_ventral_network_target",
        ),
        "brodmann_area_18": (
            "primary_visual_processing_secondary",
            "binocular_vision",
            "form_and_object_perception_global_holistic",
            "spatial_localization_v3",
            "global_visual_processing",   # right-only domain
        ),
        "brodmann_area_19": (
            "color_vision",
            "motion_perception_dominant",    # right-dominant
            "form_and_object_perception_ventral_stream",
            "spatial_localization_v3a_dominant",  # right-dominant
            "visual_attention_dominant",          # right-dominant
            "face_processing_downstream_via_ffa", # right-only
        ),
    }

    RIGHT_LATERALIZED_FUNCTIONS = (
        "face_processing",
        "global_visual_processing",
        "visuospatial_attention_dominant",
    )
        # The functions that the right occipital BA children
        # collectively support and that are absent or weaker on
        # the left. **The right BA children are the occipital
        # input stage of these functions, not their sole
        # substrate** — `face_processing` terminates at the right
        # FFA, `global_visual_processing` is a distributed right-
        # hemisphere property, and `visuospatial_attention_
        # dominant` is a network property with the right parietal
        # and right frontal lobes.

    LEFT_ONLY_DOMAINS = (
        "visual_word_processing",
        "local_featural_processing",
    )
        # The domains that are left-lateralized and do NOT appear
        # in the right occipital BA children at the same
        # weighting. These are captured in the left sibling's
        # FUNCTIONAL_DOMAIN_EMPHASIS and are documented here only
        # as exclusions so downstream code knows the right BA
        # children do not carry them.

    __all__ = [
        "LOBE",
        "HEMISPHERE",
        "BA_CHILDREN",
        "BA_TO_V_CROSSWALK",
        "V_TO_BA_CROSSWALK",
        "FORWARD_REFERENCE_V_AREAS",
        "FUNCTIONAL_DOMAIN_EMPHASIS",
        "RIGHT_LATERALIZED_FUNCTIONS",
        "LEFT_ONLY_DOMAINS",
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

4. Expose ``FUNCTIONAL_DOMAIN_EMPHASIS`` as a **right-side view** of
   the children's ``FUNCTIONAL_DOMAINS``. This is hand-written and
   is where the right-side emphasis is captured. It differs from
   the left sibling's by:
       - adding `visual_attention_ventral_network_target` to BA 17
       - replacing `form_and_object_perception_local_featural`
         with `form_and_object_perception_global_holistic` for
         BA 18
       - adding `global_visual_processing` (right-only domain) to
         BA 18
       - changing `motion_perception_weaker_than_right` to
         `motion_perception_dominant` for BA 19
       - changing `spatial_localization_v3a` to
         `spatial_localization_v3a_dominant` for BA 19
       - changing `visual_attention_lower_weighting_than_right`
         to `visual_attention_dominant` for BA 19
       - replacing `visual_word_processing_downstream_via_vwfa`
         with `face_processing_downstream_via_ffa` for BA 19

5. Expose ``RIGHT_LATERALIZED_FUNCTIONS`` and ``LEFT_ONLY_DOMAINS``
   so downstream code can see, at a glance, which functional
   domains are hemisphere-asymmetric and which side carries them.
   **The right's `RIGHT_LATERALIZED_FUNCTIONS` must be byte-
   identical to the left sibling's `LEFT_LATERALIZED_FUNCTIONS`
   (as sets — the tuple ordering may differ), and the right's
   `LEFT_ONLY_DOMAINS` must be byte-identical to the left
   sibling's `RIGHT_ONLY_DOMAINS`.** These are the complementarity
   invariant.

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
     in this package **and** in the left sibling, in the same
     commit.
  3. Update the V child's ``BRODMANN_CORRELATES`` to declare the same
     BA number(s) that appear in the parent's ``V_TO_BA_CROSSWALK``.
  4. Verify the parent's ``BA_TO_V_CROSSWALK`` and
     ``V_TO_BA_CROSSWALK`` remain exact inverses after the update.

**No asymmetry is permitted in the V-area forward references** — both
hemispheres must declare the same forward-reference list and must
resolve them in the same commit. The occipital lobe's BA ↔ V mapping
is hemisphere-invariant.

**All forward-reference caveat text is byte-identical to the left
sibling's** — the V-area forward references and the resolution rule
are properties of the occipital lobe, not of the hemisphere.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/cortex/occipital/brodmann_areas``:

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
        The forward-reference caveat text

    MUST differ (and the difference must be documented here):
        HEMISPHERE                    "left" vs "right"
        FUNCTIONAL_DOMAIN_EMPHASIS    right: BA 17 processes LEFT
                                      hemifield; BA 18 carries
                                      GLOBAL / HOLISTIC processing
                                      emphasis and includes the
                                      right-only `global_visual_
                                      processing` domain; BA 19's
                                      dorsal stream is more
                                      strongly engaged (visuospatial
                                      attention, motion), and its
                                      ventral-stream output feeds
                                      the right FFA.
                                      left: BA 17 processes RIGHT
                                      hemifield; BA 18 carries
                                      LOCAL / FEATURAL processing
                                      emphasis; BA 19's ventral
                                      stream feeds the left VWFA.
        RIGHT_LATERALIZED_FUNCTIONS   right: ("face_processing",
                                      "global_visual_processing",
                                      "visuospatial_attention_
                                      dominant").
                                      left: () — the left side's
                                      RIGHT_LATERALIZED_FUNCTIONS
                                      tuple is empty.
        LEFT_ONLY_DOMAINS             right: ("visual_word_processing",
                                      "local_featural_processing").
                                      left: () — the left side's
                                      LEFT_ONLY_DOMAINS tuple is
                                      empty.

**The complementarity invariant is verified**: the right's
`RIGHT_LATERALIZED_FUNCTIONS` must equal (as a set) the left's
`LEFT_LATERALIZED_FUNCTIONS`, and the right's `LEFT_ONLY_DOMAINS` must
equal (as a set) the left's `RIGHT_ONLY_DOMAINS`. A missing or extra
entry in any of the four tuples is a bug.

**The `FORWARD_REFERENCE_V_AREAS` tuple is byte-identical on both
sides.** The V-area forward references are a property of the
occipital lobe, not of the hemisphere, and any asymmetry in their
declaration is a bug.

**The BA ↔ V crosswalk is byte-identical on both sides.** What
differs is only which V correlate is the **dominant functional
contributor** on each side — on the right, the BA 19 dorsal-stream
correlates (V3A, V5/MT+) are dominant; on the left, the BA 19
ventral-stream correlates (V4, LOC) are dominant. This dominance
asymmetry is captured in `FUNCTIONAL_DOMAIN_EMPHASIS`, not in the
crosswalk dict.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/brodmann_areas/`` (right) —
    a sibling of ``cortex``, ``cuneus``, ``gyri``, and ``sulci``.
[ ] All three BA children are imported and registered.
[ ] ``BA_CHILDREN`` lists the three child names in the canonical
    order (17, 18, 19) and is byte-identical to the left sibling's.
[ ] ``BA_TO_V_CROSSWALK`` is **re-exported** from ``..occipital``,
    not redefined, and is byte-identical to the left sibling's.
[ ] ``V_TO_BA_CROSSWALK`` is **re-exported** from ``..occipital``,
    not redefined, is byte-identical to the left sibling's, and is
    an exact inverse of ``BA_TO_V_CROSSWALK``.
[ ] ``FORWARD_REFERENCE_V_AREAS`` is present, lists exactly the
    four forward references (V3A, V3B, V5/MT+, LOC), and is
    byte-identical to the left sibling's.
[ ] ``FUNCTIONAL_DOMAIN_EMPHASIS`` captures the **right-side
    emphasis**:
    - BA 17: primary_visual_processing, retinotopic_organization,
      binocular_vision, visual_attention_ventral_network_target
      (**LEFT hemifield**)
    - BA 18: primary_visual_processing_secondary,
      binocular_vision, form_and_object_perception_global_holistic,
      spatial_localization_v3, **global_visual_processing**
    - BA 19: color_vision, motion_perception_dominant,
      form_and_object_perception_ventral_stream,
      spatial_localization_v3a_dominant, visual_attention_dominant,
      **face_processing_downstream_via_ffa**
[ ] ``RIGHT_LATERALIZED_FUNCTIONS`` is present with exactly
    ``("face_processing", "global_visual_processing",
    "visuospatial_attention_dominant")``.
[ ] ``LEFT_ONLY_DOMAINS`` is present with exactly
    ``("visual_word_processing", "local_featural_processing")``.
[ ] **The complementarity invariant is verified**: the right's
    `RIGHT_LATERALIZED_FUNCTIONS` equals (as a set) the left's
    `LEFT_LATERALIZED_FUNCTIONS`, and the right's `LEFT_ONLY_
    DOMAINS` equals (as a set) the left's `RIGHT_ONLY_DOMAINS`. A
    missing or extra entry in any of the four tuples is a bug.
[ ] The **BA numbering in the occipital lobe is clean** — the
    three BAs are the classical Brodmann areas, not conventional
    labels. **No `PARCELATION_AMBIGUITY` field is required, and no
    `MODERN_CROSSWALK` field is required on this parent.**
[ ] The **asymmetric BA-to-V mapping** is documented:
    - BA 17 ↔ V1 (1:1, tight)
    - BA 18 ↔ V2 + V3 (1:2, partial)
    - BA 19 ↔ V3A + V4 + V5/MT+ (1:3+, partial, with V3B and LOC
      as nearby forward references)
    The asymmetry is not a defect — downstream code must not
    assume the BAs are equivalent units.
[ ] The **V-area forward references** are documented, the
    `FORWARD_REFERENCE_V_AREAS` tuple is present, and the
    resolution rule is recorded.
[ ] The **right-lateralized functions** (`face_processing`,
    `global_visual_processing`, `visuospatial_attention_dominant`)
    are documented as **network properties of the right occipital +
    right fusiform / right parietal / right frontal pathways**, not
    as BA-specific claims. The right BA 19's ventral-stream
    output feeds the right FFA, but no single BA claims
    `face_processing` as a primary contribution.
[ ] The **left-only domains** (`visual_word_processing`,
    `local_featural_processing`) are documented as **excluded**
    from the right occipital BA children at the same weighting.
[ ] The **right-specific visual hemifield rule** is documented:
    the right occipital BA children process the **LEFT** visual
    hemifield, not the right, not both. This is the primary
    lateralization fact for the right occipital lobe.
[ ] The **right-dominant motion / spatial / attentional
    contributions** of BA 19 (V3A, V5/MT+) are documented, and
    they are distinguished from the left's dorsal-stream
    contributions, which are present but weaker.
[ ] The **right FFA face-recognition endpoint** is documented as
    the downstream target of the right BA 19 ventral-stream
    output, and prosopagnosia is cross-referenced as the
    canonical right-occipito-temporal deficit.
[ ] The **left hemispatial neglect** anchor is documented as the
    canonical right-parietal + frontal deficit, with the right
    occipital lobe contributing via the right ventral attention
    network.
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
    (BA numbers, V correlates, crosswalks, forward references,
    forward-reference caveat text) match the left sibling;
    FUNCTIONAL_DOMAIN_EMPHASIS and the lateralized-domain tuples
    deliberately differ, and the complementarity invariant is
    verified.
[ ] Any downstream code that queries "which BA contains V3A?" must
    receive ``(19,)`` and must also receive the **forward-reference
    flag** — V3A is not yet a package, so the answer is
    conditional.
[ ] Any downstream code that queries "which V areas does BA 19
    contain?" must receive the four current children (V3, V4) plus
    the four forward references (V3A, V3B, V5/MT+, LOC), with the
    forward references marked.
[ ] Any downstream code that queries "which occipital functions
    are right-lateralized?" must receive
    `RIGHT_LATERALIZED_FUNCTIONS` from this package, not from
    `FUNCTIONAL_DOMAIN_EMPHASIS` — the emphasis dict records
    weighting, while the lateralized-functions tuple records
    presence/absence at the hemisphere level.
[ ] Any downstream code querying "what does the right occipital
    BA children see?" must receive "the LEFT hemifield" — the
    contralateral-visual-field rule is enforced.
[ ] Any downstream code that queries "which occipital functions
    are left-only?" must consult the right's `LEFT_ONLY_DOMAINS`
    tuple — `visual_word_processing` and
    `local_featural_processing` are left-only, and the right BA
    children must not claim them.
"""