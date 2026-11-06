"""
Occipital Lobe — Right Hemisphere
==================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital          ← THIS PACKAGE

The **occipital lobe** is the **primary visual cortex and its
association cortices** — the cortical territory at the caudal pole of
the hemisphere that receives the visual radiation from the lateral
geniculate nucleus (LGN) and hosts the entire hierarchy of
retinotopically organized visual areas from V1 through V4 and beyond.
In this architecture the occipital package is a direct child of
``cortex/``, alongside ``frontal``, ``parietal``, ``temporal``,
``insular``, and ``cingulate``.

The occipital lobe is the **most architecturally well-defined** of the
cortical lobes — the retinotopic organization is cleaner than any other
sensory system, the V1/V2 border is architectonically unambiguous (the
stria of Gennari), and the V1 → V2 → V3 → V4 → MT/V5 hierarchy is the
best-characterized cortical processing stream in the human brain. This
anatomical precision is why the occipital package has a **functional
cortex/** child (the V-numbered areas) in addition to the classical
structural children (Brodmann areas, gyri, sulci).

Direct children (5)
-------------------
::

    occipital
    ├── brodmann_areas          [cytoarchitectonic: BA 17, 18, 19]
    ├── cortex                  [functional: V1, V2, V3, V4]
    ├── cuneus                  [medial-surface gyrus: V1 on its banks]
    ├── gyri                    [lateral_occipital_gyrus]
    └── sulci                   [calcarine, lunate, transverse occipital]

**This is a mixed-children parent.** ``brodmann_areas`` and ``cortex``
are two **overlapping** decompositions of the same territory — BA 17 /
18 / 19 are Brodmann's classical numbers, while V1 / V2 / V3 / V4 are
the modern retinotopic functional areas. The mapping between them is
**many-to-many** and must be documented in both packages:

    BA 17  ≈ V1                (tight correspondence — primary
                                visual cortex / striate cortex)
    BA 18  ≈ V2 + V3           (partial — Brodmann's BA 18 covers
                                both V2 and V3)
    BA 19  ≈ V3A + V4 + V5/MT+ (partial — Brodmann's BA 19 covers
                                the extrastriate association areas)

Neither decomposition is a child of the other. Downstream code that
needs a **retinotopic functional area** must query ``cortex``;
downstream code that needs a **cytoarchitectonic area** must query
``brodmann_areas``. The two packages cross-reference the same
territory from different angles, and any attempt to flatten them into
a single hierarchy will lose information.

**The ``cuneus`` child is unusual.** It is a **gyrus**, but it is
placed **directly under occipital** rather than under ``gyri``. This
is because the cuneus is the **medial-surface landmark for V1** — the
**banks of the calcarine sulcus**, which lie between the cuneus above
and the lingual gyrus below, are where the striate cortex lives. The
cuneus is therefore simultaneously a gyral territory and a **surface
landmark for the primary visual area**, and the architecture places it
at the parent level to reflect this dual identity. When the
``gyri`` package is built out, the cuneus should be cross-referenced
from the gyral side as well, but the canonical entry stays here.

Lateralization note
-------------------
This is the **right** hemisphere. The occipital lobe is the **most
symmetric of the cortical lobes** in its retinotopic organization —
V1 surface area differs only slightly between hemispheres, and the
retinotopic maps are essentially mirror-symmetric. **But the right
occipital lobe processes the LEFT visual hemifield** of both eyes
(contralateral visual field), and the left occipital lobe processes
the RIGHT visual hemifield. This is the primary lateralization fact
for the occipital lobe, and it is a **contralateral-visual-field**
rule, not a verbal/spatial asymmetry.

Beyond this contralateral rule, the **right** occipital lobe carries
the following lateralized specializations:

* **face processing** — the **right fusiform face area (FFA)** is
  right-lateralized and receives its occipital input from the right
  occipital lobe via the right ventral stream. Right
  occipito-temporal lesions produce **prosopagnosia** (impaired
  face recognition), the canonical right-lateralized
  visual-recognition deficit. The right FFA is the **most
  face-selective** cortical region in humans
* **visuospatial attention** — the right occipital and
  occipito-parietal cortex (especially right V3A and right MT/V5)
  forms the **dorsal frontoparietal attention network** with the
  right intraparietal sulcus and right frontal eye fields. Right
  occipital and right parietal lesions contribute to
  **left hemispatial neglect** — the canonical right-lateralized
  attentional deficit. **Right V1 is also a target of the right
  ventral attention network** (with right TPJ and right FEF) that
  reorients to salient visual events
* **global visual processing** — the right hemisphere has a
  documented advantage in processing **global / holistic visual
  properties** (overall shape, gestalt, spatial layout), while the
  left has a documented advantage in processing **local / featural
  properties**. This is Navon's global-precedence asymmetry, and
  right occipital and right temporal lesions disproportionately
  impair global processing
* **left homonymous hemianopia** — right occipital lesions produce
  **left homonymous hemianopia** (loss of the left half of the
  visual field in both eyes)
* **left hemifield achromatopsia** — a right V4 lesion produces loss
  of color vision in the **left** hemifield
* **left hemifield akinetopsia** — a right MT/V5 lesion produces
  impaired motion perception in the **left** hemifield

The left occipital lobe carries the complementary specializations:
**verbal visual processing** (the left visual word form area),
**reading**, and **local / featural processing**. See the left
sibling's docstring.

--------------------------------------------------------------------------------
WHAT THE OCCIPITAL LOBE IS
--------------------------------------------------------------------------------

The occipital lobe is bounded:

    rostrally     by the **parieto-occipital sulcus** on the medial
                  surface, and (less clearly) by an imaginary line
                  from the parieto-occipital sulcus to the
                  preoccipital notch on the lateral surface
    medially      by the **interhemispheric fissure**
    caudally      by the **occipital pole** (the most posterior point
                  of the hemisphere)
    inferiorly    by the **tentorium cerebelli** and the cerebellum
    laterally     by the **lateral occipital gyri** and the
                  **transverse occipital sulcus** (the boundary with
                  the parietal and temporal lobes)

The lobe contains **four architectonically distinct functional zones**
within a retinotopic hierarchy:

    V1 (BA 17, striate cortex)
        The primary visual cortex, on the **banks of the calcarine
        sulcus** (both the upper bank — cuneus — and the lower
        bank — lingual gyrus). Contains the **stria of Gennari**,
        an architectonically visible band that is the reason BA 17
        was the first area Brodmann ever defined. Retinotopic
        representation is precise; the **fovea (macular region)**
        is represented at the **occipital pole** and the
        peripheral visual field at the more anterior banks of the
        calcarine sulcus.

    V2 (part of BA 18)
        The secondary visual cortex, surrounding V1. Processes
        border ownership, texture, illusory contours, and the
        "filling-in" of surfaces.

    V3 / V3A (part of BA 18 / BA 19)
        The tertiary visual cortex, with dynamic-form and
        motion-boundary processing.

    V4 (part of BA 19)
        The color and form area, on the **fusiform gyrus** and
        adjacent lateral occipital cortex. The **ventral stream**
        (the "what" pathway) originates here.

    V5 / MT+ (part of BA 19 or nearby)
        The motion area, on the lateral occipital cortex near
        the temporoparietal junction. The **dorsal stream** (the
        "where" pathway) originates here. **On the right, MT/V5
        is more strongly engaged during visuospatial attention
        tasks than on the left** — it is part of the
        right-lateralized dorsal attention network.

The **V1 → V2 → V3 → V4 → MT/V5** hierarchy is the best-characterized
cortical processing stream in the human brain. On the right, the
**dorsal-stream end of the hierarchy (V3A, MT/V5) is weighted toward
visuospatial attention and motion-in-space processing**, while the
**ventral-stream end (V4, LOC) is weighted toward face processing**
(via the right FFA).

--------------------------------------------------------------------------------
DIRECT CHILDREN — SPEC
--------------------------------------------------------------------------------

1. brodmann_areas
   ~~~~~~~~~~~~~~~~
   The **cytoarchitectonic** parcellation of the right occipital lobe,
   as the three classical Brodmann areas:

       brodmann_area_17_primary_visual   BA 17 — striate cortex, V1;
                                         the banks of the calcarine
                                         sulcus; the stria of Gennari
       brodmann_area_18                  BA 18 — secondary visual
                                         cortex, V2 + V3
       brodmann_area_19                  BA 19 — tertiary visual
                                         cortex, V3A + V4 + V5/MT+

   **The BA 17 / 18 / 19 ↔ V1 / V2 / V3 / V4 mapping is many-to-many
   and must be documented in the ``brodmann_areas`` parent and in
   each of the three children.** The tight BA 17 ↔ V1 correspondence
   is the only clean one; BA 18 and BA 19 each span multiple modern
   visual areas. **The mapping is hemisphere-invariant** — both
   hemispheres use the same BA-to-V crosswalk.

2. cortex
   ~~~~~~~~
   The **functional / retinotopic** parcellation of the right
   occipital lobe, as the modern V-numbered visual areas:

       primary_visual_cortex   V1 (BA 17) — striate cortex
       v2                      V2 — secondary visual cortex
       v3                      V3 — tertiary visual cortex,
                               motion boundaries
       v4                      V4 — color and form, ventral
                               stream origin

   **Additional functional areas not yet modelled as children** —
   V3A, V3B, V5/MT+, and the lateral occipital complex (LOC) — are
   noted as **forward references** to be added when the tree is
   expanded. **On the right, V3A and MT/V5 are the more strongly
   engaged dorsal-stream areas**, contributing to the right-
   lateralized dorsal attention network.

3. cuneus
   ~~~~~~~~
   The **wedge-shaped medial-surface gyrus** between the
   **parieto-occipital sulcus** (rostrally) and the **calcarine
   sulcus** (caudally). The **upper bank of the calcarine sulcus**
   — the lower margin of the cuneus — is the seat of the **dorsal
   V1 representation of the lower contralateral visual field**
   (because the upper bank of the calcarine represents the lower
   visual field of the contralateral hemifield). **On the right,
   the cuneus's V1 upper bank represents the lower LEFT visual
   field.**

   **The cuneus is the medial-surface surface-landmark for V1**, and
   this is why it sits at the parent level rather than under ``gyri``.
   When the ``gyri`` package is built out, the cuneus should be
   cross-referenced from the gyral side as well, but the canonical
   entry stays here.

   The cuneus is also the occipital-lobe counterpart of the frontal
   lobe's **paracentral lobule**: both are **medial-surface
   gyral/lobular territories** that function as surface landmarks
   for primary sensory cortex (the paracentral lobule for leg
   somatosensory/motor; the cuneus for upper-bank V1).

4. gyri
   ~~~~~~
   The **lateral-surface gyri** of the right occipital lobe:

       lateral_occipital_gyrus   the lateral occipital gyri
                                 (sometimes subdivided into
                                 superior, middle, and inferior
                                 lateral occipital gyri), forming
                                 the lateral surface of the lobe

   The **lingual gyrus** (below the calcarine sulcus, forming the
   lower bank of V1) is **not yet a child of this package** — it is
   a forward reference. When built out, it should be added as a
   second gyral child of the occipital parent (or of ``gyri``,
   with cross-reference from this parent).

5. sulci
   ~~~~~~~
   The **sulcal landmarks** of the right occipital lobe:

       calcarine_sulcus             the calcarine sulcus — the
                                    defining sulcus of the occipital
                                    lobe; V1 lies on its banks
       lunate_sulcus                the lunate sulcus — an inconstant
                                    sulcus that (when present) marks
                                    the anterior boundary of V1 on
                                    the lateral surface
       transverse_occipital_sulcus  the transverse occipital sulcus
                                    — the posterior boundary of the
                                    lateral occipital gyri

   **The calcarine sulcus is the most consequential sulcus in the
   lobe** — it is the surface landmark for V1, and its banks are
   where the striate cortex lives. The lunate and transverse
   occipital sulci are less architecturally load-bearing but are
   the lateral-surface landmarks for the V1/V2 border (lunate,
   when present) and for the boundary between the lateral occipital
   gyri and the parietal/temporal cortex (transverse).

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (this architecture's tags)
--------------------------------------------------------------------------------

The occipital lobe is the substrate of the following functional
domains. Each domain is tagged here so that downstream code can query
"what does the occipital lobe do?" without reading every child
package:

    primary_visual_processing
        V1 — the first cortical stage of vision. Orientation
        columns, ocular-dominance columns, spatial-frequency
        tuning, contrast sensitivity, and retinotopic mapping.
        The **stria of Gennari** is the architectonic signature.
        **On the right, V1 processes the LEFT visual hemifield.**

    retinotopic_organization
        The topographic mapping of the visual field onto the
        cortical surface — the property that makes the occipital
        lobe the most architecturally precise sensory cortex.
        **The right hemisphere maps the LEFT contralateral visual
        hemifield**, with the fovea at the occipital pole and the
        periphery at the anterior calcarine banks.

    binocular_vision
        V1's ocular-dominance columns and their convergence in V2
        and beyond support depth perception, stereopsis, and
        binocular fusion.

    color_vision
        V4 and the adjacent ventral occipito-temporal cortex.
        Achromatopsia (loss of color vision) follows V4 lesions.
        **On the right, V4 lesions produce LEFT hemifield
        achromatopsia.**

    motion_perception
        V5 / MT+ and the adjacent dorsal occipito-parietal cortex.
        Akinetopsia (loss of motion perception) follows MT/V5
        lesions. **On the right, MT/V5 is more strongly engaged
        during visuospatial attention and motion-in-space
        processing than on the left; right MT/V5 lesions produce
        LEFT hemifield akinetopsia.**

    form_and_object_perception
        V2, V3, V4, and the lateral occipital complex (LOC,
        forward reference). The **ventral stream** ("what"
        pathway) originates here and continues to the temporal
        lobe. **On the right, the ventral stream's endpoint (right
        FFA) is specialized for faces** — a right-lateralized
        function documented under `face_processing`.

    spatial_localization
        V3, V3A, and MT/V5. The **dorsal stream** ("where"
        pathway) originates here and continues to the parietal
        lobe. **On the right, the dorsal stream is more strongly
        engaged during visuospatial attention** — the right V3A
        and right MT/V5 are core nodes of the right-lateralized
        dorsal attention network.

    visual_attention
        The occipital lobe is the target of **top-down attentional
        gain** from the frontal and parietal cortices. The right
        occipital lobe is the more strongly engaged side for
        **stimulus-driven reorienting to salient visual events**
        (via the right ventral attention network with the right
        TPJ and right FEF), and for **sustained spatial attention**
        (via the right dorsal attention network). **Right parietal
        and right frontal lesions produce left hemispatial
        neglect**, the canonical right-lateralized attentional
        deficit.

    visual_word_processing (left-lateralized)
        The left occipital lobe's ventral stream output feeds
        the **left visual word form area (VWFA)** in the left
        fusiform gyrus. This is the **reading-related**
        specialization of the left occipital-temporal pathway,
        and it is the reason alexia is a **left**-lateralized
        syndrome. **It is documented in the left sibling, not
        here**, but is cross-referenced because the right
        occipital lobe does not carry this function at the same
        weighting.

    face_processing (right-lateralized)
        **The right fusiform face area (FFA) is the canonical
        right-lateralized visual-recognition specialisation**,
        and it receives its occipital input from the right
        occipital lobe via the right ventral stream. Right
        occipito-temporal lesions produce **prosopagnosia** —
        impaired face recognition — the canonical right-
        lateralized visual-recognition deficit. The right
        occipital lobe is the occipital input stage of this
        right-lateralized pathway.

    global_visual_processing (right-lateralized)
        The right hemisphere has a documented advantage in
        processing **global / holistic visual properties** —
        overall shape, gestalt, spatial layout. This is Navon's
        global-precedence asymmetry, and right occipital and
        right temporal lesions disproportionately impair global
        processing. The left hemisphere has a complementary
        advantage in **local / featural processing**.

    visual_memory_and_imagery
        The occipital lobe participates in visual imagery and
        visual working memory, receiving top-down signals from
        the frontal and parietal cortices. **The right occipital
        lobe's imagery contribution is weighted toward spatial
        and face imagery**; the left's toward verbal imagery.

These tags map onto the memory subsystem as follows:

    primary_visual_processing    → memory/stores/short_term (visual sensory buffer)
    retinotopic_organization     → memory/stores/short_term (spatial buffer)
    binocular_vision             → memory/stores/short_term (depth buffer)
    color_vision                 → memory/stores/short_term (chromatic buffer)
    motion_perception            → memory/stores/short_term (motion buffer)
    form_and_object_perception   → memory/stores/long_term/explicit/semantic (ventral stream)
    spatial_localization         → memory/stores/short_term (dorsal stream buffer)
    visual_attention             → memory/stores/short_term (attentional gain)
    visual_word_processing       → memory/stores/long_term/explicit/semantic  # LEFT-ONLY
    face_processing              → memory/stores/long_term/implicit/implicit_social_cognitive  # RIGHT-ONLY
    global_visual_processing     → memory/stores/short_term (gestalt buffer)  # RIGHT-ONLY
    visual_memory_and_imagery    → memory/stores/long_term/explicit/episodic

**Right-side note on `visual_word_processing`:** this domain is
**left-lateralized** and does not route to any right-hemisphere store.
The right occipital parent must still **declare** the domain in its
`FUNCTIONAL_DOMAINS` tuple (for hemisphere-invariant schema
compliance), but must mark it `LATERALIZATION = "left_only"` so
downstream code does not attempt to instantiate it on the right.

**Right-side note on `face_processing`:** this domain is
**right-lateralized** and **is instantiated on the right**. The left
sibling declares it with `LATERALIZATION = "right_only"` and does not
route it; the right parent routes it to
`implicit_social_cognitive`.

**Right-side note on `global_visual_processing`:** this domain is a
**new domain on the right** that does not appear at left-occipital
weighting. The left sibling declares it with `LATERALIZATION =
"right_only"` and does not route it; the right parent routes it to a
`short_term` gestalt buffer.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (within this package)
    The cytoarchitectonic child. Every BA package under
    ``occipital/brodmann_areas/`` must declare the occipital lobe
    as its parent and must cross-reference the corresponding
    V-numbered functional area(s) under ``..cortex``. **The BA-to-V
    crosswalk is hemisphere-invariant** — both hemispheres use the
    same mapping.

..cortex  (within this package)
    The functional child. Every V-numbered package under
    ``occipital/cortex/`` must declare the occipital lobe as its
    parent and must cross-reference the corresponding Brodmann
    area(s) under ``..brodmann_areas``. **On the right, V3A and
    MT/V5 are the more strongly engaged dorsal-stream areas.**

..cuneus  (within this package)
    The medial-surface gyral landmark. Its banks (the upper bank
    of the calcarine sulcus) are the dorsal V1 representation.
    **On the right, the cuneus's V1 upper bank represents the
    lower LEFT visual field.**

..gyri  (within this package)
    The lateral-surface gyral child. The lateral occipital gyri
    are the lateral surface of the lobe; their rostral boundary
    is the transverse occipital sulcus and their caudal boundary
    is the occipital pole.

..sulci  (within this package)
    The sulcal child. The calcarine sulcus is the defining
    sulcus of the lobe; the lunate and transverse occipital
    sulci are the lateral-surface landmarks.

..cortex.parietal
    The **dorsal stream** continues from V5/MT+ and V3A into the
    parietal lobe (intraparietal sulcus, area 7, etc.). **On the
    right, the dorsal stream is more strongly engaged during
    visuospatial attention**, and the right parietal lobe is a
    core node of the right-lateralized dorsal attention network.
    The parietal package must declare the occipital lobe as the
    source of its visual input for the dorsal stream, and must
    note the right-lateralized attentional emphasis.

..cortex.temporal
    The **ventral stream** continues from V4 and LOC into the
    temporal lobe (inferior temporal cortex, fusiform gyrus,
    VWFA, FFA). The temporal package must declare the occipital
    lobe as the source of its visual input for the ventral
    stream, and must note the **left-lateralized VWFA** and
    **right-lateralized FFA** specializations. **On the right,
    the FFA is the canonical face-recognition endpoint of the
    ventral stream**, and right occipito-temporal lesions produce
    prosopagnosia.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral
    prefrontal cortex** send top-down visual attentional signals
    to the occipital lobe. **On the right, the right FEF is the
    dominant node of the ventral attention network**, and right
    frontal lesions contribute to left hemispatial neglect. The
    frontal package must declare the occipital lobe as a target
    of its attentional projections, and must note the right-
    lateralized attentional emphasis.

..cortex.cingulate  — indirect
    The cingulate participates in visual attention and visual
    memory via the cingulum bundle and the salience network.
    No direct cingulate → occipital projection originates in the
    cingulate proper. Recorded here to pre-empt a false
    cross-reference.

..cortex.insular  — indirect
    The insular lobe is not a direct visual area. Its visual
    contributions are through the salience network (detecting
    behaviourally relevant visual stimuli) and through
    multimodal integration. Recorded here to pre-empt a false
    cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **lateral geniculate nucleus (LGN)** is the thalamic relay
    from the retina to V1. The LGN → V1 projection is the
    anatomical substrate of primary visual processing, and the
    LGN is the **first visual relay** after the optic chiasm and
    the optic tract. The thalamus package must declare the LGN
    as the primary visual thalamic relay.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream terminates in the perirhinal, entorhinal,
    and parahippocampal cortices, which are hippocampal
    formation structures. Visual object recognition and visual
    memory are supported by the occipito-temporal-hippocampal
    pathway. **On the right, the parahippocampal place area
    (PPA) and the retrosplenial complex receive visual input
    supporting scene and spatial memory**, which are more
    strongly right-lateralized. The hippocampus package must
    declare the occipital lobe as the source of its visual
    input, and must note the right-lateralized scene-memory
    emphasis.

../../left/cortex/occipital
    The left-hemisphere homologue. The **anatomical children**
    (brodmann_areas, cortex, cuneus, gyri, sulci) exist on both
    sides with the same names and the same structural fields, but
    the **functional lateralization** diverges:
        right → left hemifield processing; face processing
                (FFA); visuospatial attention; global visual
                processing; left homonymous hemianopia from
                right lesions; prosopagnosia from right
                occipito-temporal lesions; left hemispatial
                neglect (with right parietal/frontal)
        left  → right hemifield processing; verbal visual
                processing (VWFA); reading; local / featural
                processing; right homonymous hemianopia from
                left lesions; alexia without agraphia from
                left occipital + splenium lesions
    The left sibling's docstring carries the full left-side
    contract.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT FOR EACH CHILD PACKAGE
--------------------------------------------------------------------------------

Every child of ``occipital/`` MUST expose the following module-level
names so the rest of the system can query the lobe uniformly. The
fields differ by child type (BA vs V-numbered vs gyral vs sulcal vs
the cuneus).

Brodmann child (``brodmann_areas/*``):

    AREA_NAME : str
        Canonical snake_case name, identical to the folder name.

    HEMISPHERE : str
        "right" (this branch) or "left" (the sibling branch).

    LOBE : str
        "occipital"

    BRODMANN_NUMBER : int
        The BA number (17, 18, or 19).

    FUNCTIONAL_CORRELATES : dict[str, tuple[str, ...]]
        The V-numbered functional areas that overlap this BA.
        BA 17 is the tight case (V1 only); BA 18 and BA 19 are
        many-to-many.

    RETINOTOPIC_MAP : str
        One of "fovea_at_pole", "fovea_at_pole_macula_dominant",
        "eccentricity_gradient", "not_retinotopic" (for
        association areas that are only partially retinotopic).

    FUNCTIONAL_DOMAINS : tuple[str, ...]
        Subset of the twelve functional-domain tags listed above.

    CONNECTIVITY : dict[str, tuple[str, ...]]
        Thalamic afferents and cortical/subcortical targets.

    __all__ : list[str]
        Every public name above.

Functional child (``cortex/*``):

    AREA_NAME : str
        Canonical snake_case name, identical to the folder name.

    HEMISPHERE : str
        "right" or "left"

    LOBE : str
        "occipital"

    V_NUMBER : str
        The V-numbered designation ("V1", "V2", "V3", "V4").

    BRODMANN_CORRELATES : tuple[int, ...]
        The BA number(s) that overlap this V area. V1 → (17,);
        V2 → (18,); V3 → (18, 19); V4 → (19,).

    RETINOTOPIC_MAP : str
        Same as for the BA children.

    FUNCTIONAL_DOMAINS : tuple[str, ...]
        Same as for the BA children.

    CONNECTIVITY : dict[str, tuple[str, ...]]
        Same as for the BA children.

    __all__ : list[str]
        Every public name above.

Gyral child (``gyri/*``):

    GYRUS_NAME : str
        Canonical snake_case name.

    HEMISPHERE : str
        "right" or "left"

    LOBE : str
        "occipital"

    BOUNDING_SULCI : dict[str, tuple[str, ...]]
        Direction → sulcus names.

    FUNCTIONAL_OVERLAYS : tuple[str, ...]
        The V-numbered functional areas that overlay this gyrus.

    __all__ : list[str]
        Every public name above.

Sulcal child (``sulci/*``):

    SULCUS_NAME : str
        Canonical snake_case name.

    HEMISPHERE : str
        "right" or "left"

    LOBE : str
        "occipital"

    BOUNDING_GYRI : dict[str, tuple[str, ...]]
        Direction → gyrus names.

    FUNCTIONAL_LANDMARK : str
        Which functional area this sulcus is the surface landmark
        for.

    __all__ : list[str]
        Every public name above.

Cuneus child (``cuneus/*``):

    GYRUS_NAME           = "cuneus"
    HEMISPHERE           "right" or "left"
    LOBE                 "occipital"
    BOUNDING_SULCI       {"rostral": ("parieto_occipital_sulcus",),
                          "caudal": ("calcarine_sulcus",)}
    FUNCTIONAL_OVERLAYS  ("primary_visual_cortex_dorsal_bank",)
        # The lower margin of the cuneus is the upper bank of
        # the calcarine sulcus, which carries the dorsal V1
        # representation of the LOWER contralateral visual field.
        # **On the right, this is the lower LEFT visual field.**
    LATERALIZATION_NOTE  "medial_surface_landmark_for_V1"
    __all__              every public name above

The child's ``__init__.py`` should additionally contain a docstring
following the same template used in the child packages already
written: hierarchical location → what the field is → territories →
BA or V adjacency → extent → variants → clinical significance →
cross-references → implementation contract → checklist.

--------------------------------------------------------------------------------
PACKAGE-LEVEL EXPORTS (this file)
--------------------------------------------------------------------------------

This ``occipital/__init__.py`` is a namespace + registry. It must:

1. Import the five children (no side effects):
       from . import brodmann_areas
       from . import cortex
       from . import cuneus
       from . import gyri
       from . import sulci

2. Expose a registry of cytoarchitectonic children:

       OCCIPITAL_BA_PACKAGES = {
           "brodmann_area_17_primary_visual": brodmann_areas.brodmann_area_17_primary_visual,
           "brodmann_area_18":                brodmann_areas.brodmann_area_18,
           "brodmann_area_19":                brodmann_areas.brodmann_area_19,
       }

3. Expose a registry of functional children:

       OCCIPITAL_V_PACKAGES = {
           "primary_visual_cortex": cortex.primary_visual_cortex,
           "v2":                    cortex.v2,
           "v3":                    cortex.v3,
           "v4":                    cortex.v4,
       }

4. Expose a registry of gyral / sulcal children:

       OCCIPITAL_GYRI = {
           "cuneus":                cuneus,
           "lateral_occipital_gyrus": gyri.lateral_occipital_gyrus,
       }

       OCCIPITAL_SULCI = {
           "calcarine_sulcus":            sulci.calcarine_sulcus,
           "lunate_sulcus":               sulci.lunate_sulcus,
           "transverse_occipital_sulcus": sulci.transverse_occipital_sulcus,
       }

5. Expose a **BA ↔ V crosswalk** (hand-written because the mapping
   is a convention, not a derivation) — **byte-identical to the left
   sibling's**:

       BA_TO_V_CROSSWALK = {
           17: ("primary_visual_cortex",),
           18: ("v2", "v3"),
           19: ("v3", "v4"),
       }

       V_TO_BA_CROSSWALK = {
           "primary_visual_cortex": (17,),
           "v2":                    (18,),
           "v3":                    (18, 19),
           "v4":                    (19,),
       }

   The crosswalk must fail loudly if any BA or V-numbered package
   declares a correlate that is not in the corresponding tuple.

6. Expose a **functional domain → child packages** index, derived
   from the children's ``FUNCTIONAL_DOMAINS`` fields:

       DOMAIN_TO_CHILDREN = {
           # computed at import time by inverting FUNCTIONAL_DOMAINS
           # on each child
           "primary_visual_processing": (...),
           "retinotopic_organization":  (...),
           "color_vision":              (...),
           "motion_perception":         (...),
           "face_processing":           (...),   # right-instantiating
           "global_visual_processing":  (...),   # right-only
           ...
       }

   The inversion must fail loudly if a child declares a domain that
   is not in the canonical domain list above.

7. Expose a **lateralization profile**:

       LATERALIZATION_PROFILE = {
           "processes_visual_hemifield":     "left",    # right occipital
                                                        # processes the
                                                        # LEFT hemifield
           "face_processing":                "right_dominant",
           "visuospatial_attention":         "right_dominant",
           "global_visual_processing":       "right_dominant",
           "verbal_visual_processing":       "left_dominant",
           "local_featural_processing":      "left_dominant",
           "prosopagnosia":                  "right_occipito_temporal",
           "hemispatial_neglect":            "right_parietal_and_frontal",
           "alexia_without_agraphia":        "left_occipital_plus_splenium",
       }

   This is a **right-hemisphere-specific** profile. The left sibling
   carries its own, mirrored version.

8. Define ``__all__`` as shown in the implementation contract.

9. Contain **no** logic beyond the above. Any behaviour belongs in
   the child packages or in ``cortex/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**The following functional areas are not yet packages** and are
documented here as forward references:

    V3A                — sub-area of V3 / V4 in different
                         parcellations; motion-boundary and
                         motion-in-depth processing. **On the
                         right, V3A is a core node of the
                         right-lateralized dorsal attention
                         network.**
    V3B                — kinetic-occipital area; motion processing
    V5 / MT+           — the motion area; akinetopsia follows its
                         lesion. **On the right, MT/V5 is more
                         strongly engaged during visuospatial
                         attention and motion-in-space processing
                         than on the left.**
    lateral occipital   — object-recognition complex; the "LOC"
    complex (LOC)       — is the ventral stream's object area
    lingual gyrus      — the lower bank of the calcarine sulcus,
                         the ventral V1 representation

None is a forward-declaration caveat in the sense of the sulci
packages (where a bounding gyrus is not yet modelled). They are
**forward references** — future packages that will be added to
``..cortex`` (for V3A, V3B, V5/MT+, LOC) or to ``..gyri`` (for the
lingual gyrus). The occipital parent already works without them; they
will be added when the tree is expanded, and the parent's registries
will be updated in the same commit as their addition, **in both
hemispheres**.

**There is no forward-declaration caveat for the existing children**
— all five direct children (brodmann_areas, cortex, cuneus, gyri,
sulci) exist as packages under ``..occipital/``, and all their
structural fields resolve.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/cortex/occipital``:

    MUST be identical (byte-for-byte):
        The set of direct child package names (brodmann_areas,
        cortex, cuneus, gyri, sulci).
        The set of BA child names (BA 17, 18, 19).
        The set of V child names (V1, V2, V3, V4).
        The set of gyrus child names (cuneus, lateral occipital
        gyrus).
        The set of sulcus child names (calcarine, lunate,
        transverse occipital).
        The BA_TO_V_CROSSWALK and V_TO_BA_CROSSWALK.
        The LATERALIZATION_PROFILE's **structure** (though the
        values differ — see below).
        The forward-reference list (V3A, V3B, V5/MT+, LOC,
        lingual gyrus).
        The cuneus placement rationale (parent level, not under
        gyri).
        The calcarine sulcus defining role.

    MUST differ (and the difference must be documented here):
        HEMISPHERE                "left" vs "right"
        LATERALIZATION_PROFILE    right: processes LEFT visual
                                  hemifield; face processing
                                  dominant; global visual
                                  processing dominant;
                                  visuospatial attention dominant;
                                  prosopagnosia follows right
                                  occipito-temporal lesions;
                                  left homonymous hemianopia from
                                  right lesions; left hemispatial
                                  neglect from right parietal +
                                  frontal lesions.
                                  left: processes RIGHT visual
                                  hemifield; verbal visual
                                  processing dominant; local /
                                  featural processing dominant;
                                  alexia without agraphia follows
                                  left occipital + splenium
                                  lesions.
        FUNCTIONAL_DOMAINS        both sides carry the same base
                                  ten domains, PLUS:
                                  - `face_processing` is
                                    right-instantiating here; the
                                    left parent declares it with
                                    LATERALIZATION = "right_only"
                                  - `global_visual_processing` is
                                    a right-only domain; the left
                                    parent declares it with
                                    LATERALIZATION = "right_only"
                                  - `visual_word_processing` is
                                    left-only; the right parent
                                    declares it with
                                    LATERALIZATION = "left_only"
        CLINICAL_ANCHORS          right: left homonymous hemianopia;
                                  prosopagnosia (right occipito-
                                  temporal); left hemifield
                                  achromatopsia (right V4); left
                                  hemifield akinetopsia (right
                                  MT/V5); left hemispatial neglect
                                  (with right parietal + frontal
                                  lesions); global processing
                                  deficit.
                                  left: right homonymous
                                  hemianopia; alexia without
                                  agraphia (left occipital +
                                  splenium); right hemifield
                                  achromatopsia; right hemifield
                                  akinetopsia; local / featural
                                  processing deficit.

Any deviation from the "MUST be identical" list is a bug — the
occipital lobe has the same anatomical children on both sides, and
the BA / V numbering is symmetric. Any unexpected similarity in the
"MUST differ" list is also a bug — the occipital lobe is the most
retinotopically symmetric lobe, but it is **not** functionally
symmetric, and if left and right occipital end up with the same
LATERALIZATION_PROFILE, the hemisphere split has collapsed.

**The visual hemifield rule is the one thing that must not be
averaged.** Each hemisphere processes the **contralateral** visual
hemifield. **The right hemisphere processes the LEFT hemifield.**
This is the primary lateralization fact for the right occipital lobe,
and any downstream code that queries "what does the right occipital
lobe see?" must receive "the LEFT hemifield" — not "the right
hemifield," not "both hemifields."

**The functional asymmetry is the second sharpest entry.** The right
occipital lobe is dominant for **face processing**, **visuospatial
attention**, and **global visual processing** — three domains that the
left occipital lobe either does not carry at all (`face_processing`,
`global_visual_processing`) or carries at lower weighting
(`visual_attention`). The checklist verifies that these domains are
declared and instantiated appropriately.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] The package sits at ``cortex/occipital/``, directly under
    ``cortex/`` — not under ``gyri`` or ``sulci``.
[ ] The five direct children (``brodmann_areas``, ``cortex``,
    ``cuneus``, ``gyri``, ``sulci``) are imported and registered.
[ ] ``OCCIPITAL_BA_PACKAGES`` has exactly the three BA children:
    17, 18, 19.
[ ] ``OCCIPITAL_V_PACKAGES`` has exactly the four V children:
    V1, V2, V3, V4.
[ ] ``OCCIPITAL_GYRI`` has exactly the two gyral children:
    cuneus, lateral_occipital_gyrus.
[ ] ``OCCIPITAL_SULCI`` has exactly the three sulcal children:
    calcarine, lunate, transverse occipital.
[ ] ``BA_TO_V_CROSSWALK`` and ``V_TO_BA_CROSSWALK`` are present,
    consistent, and **byte-identical to the left sibling's**.
[ ] ``DOMAIN_TO_CHILDREN`` is **derived**, not hand-written, and
    fails loudly on unknown domains.
[ ] ``LATERALIZATION_PROFILE`` is present with the **right-specific
    values**: **left** hemifield processing, face processing
    dominant, visuospatial attention dominant, global visual
    processing dominant, prosopagnosia from right occipito-temporal
    lesions, left hemispatial neglect from right parietal + frontal
    lesions.
[ ] The **twelve functional domains** are listed with their
    memory-subsystem routings, and the **three lateralized
    routings** (`visual_word_processing` left-only,
    `face_processing` right-only, `global_visual_processing`
    right-only) are flagged.
[ ] `visual_word_processing` is declared in `FUNCTIONAL_DOMAINS` but
    marked `LATERALIZATION = "left_only"` — the right parent
    declares it and does **not** instantiate it.
[ ] `face_processing` is declared in `FUNCTIONAL_DOMAINS` and
    **instantiated** on the right — routes to
    `memory/stores/long_term/implicit/implicit_social_cognitive`.
    The left parent declares it as `right_only` and does not
    instantiate it.
[ ] `global_visual_processing` is declared in `FUNCTIONAL_DOMAINS`
    and **instantiated** on the right — routes to a `short_term`
    gestalt buffer. The left parent declares it as `right_only` and
    does not instantiate it.
[ ] The **visual hemifield rule** is documented: right occipital
    processes the **LEFT** visual hemifield; left occipital
    processes the RIGHT visual hemifield. **This is the primary
    lateralization fact and must not be averaged.**
[ ] The **BA ↔ V many-to-many mapping** is documented: BA 17 ≈ V1
    (tight), BA 18 ≈ V2 + V3, BA 19 ≈ V3A + V4 + V5/MT+ (partial).
    No attempt to flatten the mapping into a single hierarchy is
    permitted. The crosswalk is hemisphere-invariant.
[ ] The **cuneus placement** is documented: it sits at the parent
    level (not under ``gyri``) because it is the medial-surface
    landmark for the upper bank of the calcarine sulcus (V1). On
    the right, the cuneus's V1 upper bank represents the **lower
    LEFT visual field**.
[ ] The **calcarine sulcus** is documented as the defining sulcus
    of the lobe and the surface landmark for V1.
[ ] The **forward references** (V3A, V3B, V5/MT+, LOC, lingual
    gyrus) are documented as future packages, not as current
    children. V3A and MT/V5 are noted as the more strongly engaged
    dorsal-stream areas on the right.
[ ] The **ventral and dorsal streams** are cross-referenced to
    ``cortex.temporal`` and ``cortex.parietal`` respectively. The
    right dorsal stream is noted as more strongly engaged during
    visuospatial attention; the right ventral stream's endpoint
    (right FFA) is noted as face-selective.
[ ] The **LGN** is cross-referenced as the thalamic relay.
[ ] The **right-lateralized face processing** and the right-
    lateralized **visuospatial attention** and **global visual
    processing** are documented as the primary right-lateralized
    functional asymmetries.
[ ] The **prosopagnosia** anchor is documented as the canonical
    right-occipito-temporal deficit, and the **left hemispatial
    neglect** anchor is documented as the canonical right-parietal
    + frontal deficit.
[ ] The **visual word processing** domain is documented as a
    left-lateralized function that the right occipital lobe does
    not carry at the same weighting, and the **alexia without
    agraphia** anchor is noted as left-only.
[ ] Every child package's docstring follows the same template used
    in the already-written child packages.
[ ] Cross-hemisphere symmetry test passes: structural fields match
    the left sibling; LATERALIZATION_PROFILE, functional-domain
    lateralization flags, and clinical anchors deliberately differ.
[ ] **The visual hemifield rule is verified**: the right parent
    processes the LEFT hemifield, the left parent processes the
    RIGHT hemifield, and neither has been copied verbatim from the
    other.
[ ] Any downstream code querying "what does the right occipital
    lobe see?" must receive "the LEFT hemifield" — the
    contralateral-visual-field rule is enforced.
[ ] Any downstream code assigning visual-word processing must
    weight the left occipital lobe more heavily; any downstream
    code assigning face processing must weight the right occipital
    lobe more heavily; any downstream code assigning global visual
    processing must weight the right occipital lobe more heavily.
    Averaging left and right would erase the lateralized signals.
"""