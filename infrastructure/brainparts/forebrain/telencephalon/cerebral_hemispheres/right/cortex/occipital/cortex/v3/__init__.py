"""
Tertiary Visual Cortex (V3) — Right Hemisphere
===============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── v3   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the right
hemisphere's **V3** — the **tertiary visual cortex**, the second
extrastriate belt area, and the immediate downstream target of V2. It
is the **first V area in the hierarchy whose BA correlate spans two
Brodmann areas** (BA 18 **and** BA 19), and the **first V area whose
primary functional contribution is spatial-localization and
motion-boundary processing** rather than low-level feature extraction.

Parent: ``..cortex`` (right occipital functional / V-numbered parent)
— sibling to V1, V2, V4. **Sibling — not parent —** of
``...brodmann_areas/brodmann_area_18`` **and**
``...brodmann_areas/brodmann_area_19``, both of which include V3 in
their own ``V_AREA_CORRELATE`` fields. The V3 / BA 18 / BA 19
relationship is **double partial correspondence** — BA 18 spans V2
**and** V3, while BA 19 spans V3 **and** V4 (plus four forward
references). V3 sits **at the boundary between the two BAs**, which
is why its cytoarchitectonic correlate is a **two-element tuple**
``(18, 19)``.

This package is the **structural mirror** of
``../../left/cortex/occipital/cortex/v3``. The V-number, the two-BA
correlate (18, 19), the V3d / V3v subregion distinction, the
mirror-flip retinotopy, the V2/V3 and V3/V4 borders, and the relay
to MT/V5 and V4 are identical on both sides; the **functional
emphasis** and **clinical significance** diverge — on the right, V3
is weighted toward the **spatial-localization and motion-boundary**
aspect (V3d → MT/V5 is the dominant dorsal-stream relay, and the
right V3d and right MT/V5 are the dominant motion-in-space
substrate), the right V3v feeds the **right V4 → LOC → right FFA**
(face) pathway, and right V3 lesions produce **more severe
motion-boundary and depth-from-motion deficits**, **global form-
from-motion deficits**, **left hemifield neglect contribution**, and
contribute to **prosopagnosia** via the right V3v → V4 → LOC → FFA
pathway.

**The defining structural fact about V3 is its double-BA span.**
Unlike V1 (exactly BA 17) and V2 (partially BA 18), **V3 is the only
V area in the tree whose cytoarchitectonic correlate spans two BAs**:

    V1  ↔  BA 17  (exactly)
    V2  ↔  BA 18  (partially — shared with V3)
    V3  ↔  BA 18 + BA 19  (double partial — shared with V2 on the
                           BA 18 side, shared with V4/V3A/V3B/
                           V5/MT+/LOC on the BA 19 side)
    V4  ↔  BA 19  (partially — shared with V3, V3A, V3B, V5/MT+,
                   LOC)

This means downstream code **cannot** assume "V3 = BA 18 + BA 19" or
"BA 18 + BA 19 = V3" — the BA-to-V mapping is **many-to-many**, and
V3 is the pivot point. The parent's ``BA_TO_V_CROSSWALK`` and
``V_TO_BA_CROSSWALK`` record this:

    18 → (v2, v3)          v2 → (18,)
    19 → (v3, v4, V3A,     v3 → (18, 19)
          V3B, V5_MT_plus, v4 → (19,)
          LOC)

V3 is the **only V area that appears on both sides of the crosswalk**
— it is a BA 18 territory **and** a BA 19 territory at the same time.
**This structural fact is byte-identical to the left sibling's — the
double-BA span is a property of the BA scheme, not of the hemisphere.**

--------------------------------------------------------------------------------
WHAT V3 IS
--------------------------------------------------------------------------------

V3 is the **tertiary visual cortex** — the second extrastriate belt
area, immediately **surrounding V2** on both the **dorsal** and
**ventral** aspects of the occipital lobe. It is bounded **caudally**
by V2 (the V2/V3 border, which represents the **horizontal
meridian** of the visual field) and **rostrally** by V3A (dorsally)
and V4 (ventrally). Unlike V1 and V2, whose boundaries are marked by
crisp architectonic features (the stria of Gennari for V1, the CO
stripes for V2), **V3 has no single architectonic signature** — its
boundaries and subregions are defined **retinotopically**.

**The defining structural distinction within V3 is the V3d / V3v
split** — a **dorsal component (V3d)** and a **ventral component
(V3v)** that have **different functional roles and different
downstream targets**:

    V3d (dorsal V3)         the dorsal aspect, adjacent to V3A.
                            Functionally weighted toward **motion
                            and motion-in-depth**: coherent
                            motion, motion-boundary detection,
                            optic flow, kinetic contours.
                            Projects strongly to **MT/V5**.
                            **On the right, V3d's motion
                            contribution is DOMINANT** — the
                            right V3d and right MT/V5 are the
                            **dominant motion-and-motion-in-depth
                            substrate** in the human brain, and
                            the right V3d → right MT/V5 relay is
                            the dominant dorsal-stream pathway.

    V3v (ventral V3)        the ventral aspect, adjacent to V4v
                            and hV4. Functionally weighted
                            toward **form and shape from
                            motion**: kinetic boundaries,
                            shape from shading, shape from
                            texture, stereopsis via disparity.
                            Projects strongly to **V4**.
                            **On the right, V3v's form
                            contribution feeds the right
                            V4 → LOC → right FFA (face)
                            pathway** — the right V3v is the
                            **third stage of the right face-
                            recognition pathway** after V1 and
                            V2.

**V3d and V3v are distinct enough that some parcellations split V3
into two separate V areas** (V3d and V3v, with V3v sometimes
called VP for "ventral posterior"). **The current tree keeps them
together as "V3"**, consistent with the parent's
``V_AREA_CORRELATE`` entry, but the docstring documents the split
because it is the **most important structural fact** about V3 and
because the eventual V3 → V3d + V3v split is the most likely future
promotion.

**The relay to MT/V5 is V3's most consequential connectivity — and
it is the dominant one on the right.** V3's **dorsal component
(V3d)** projects to **MT/V5** and is the **principal cortical
relay** for the dorsal stream's motion pathway:

    V1 → V2 (thick stripes) → V3 (V3d) → MT/V5
    V1 → V2 (thick stripes) → MT/V5 (direct)

Both routes exist, but the **V3d relay is the more elaborated one**
for **motion-boundary and motion-in-depth** signals (as opposed to
V2's thick-stripe direct projection, which carries the **low-level
motion signal**). **On the right, V3d's MT/V5 relay is the dominant
motion substrate** — the right V3d → right MT/V5 pathway is the
principal cortical substrate for **left-hemifield motion perception
and motion-in-space processing**, and it feeds the right dorsal
attention network (right IPS, right FEF). **The right V3d's
contribution to motion-boundary and depth-from-motion processing is
stronger than the left's.**

**The relay to V4 is V3's second major connectivity — and on the
right, it feeds the face pathway.** V3's **ventral component (V3v)**
projects to **V4** and is the **principal cortical relay** for the
ventral stream's form pathway:

    V1 → V2 (thin stripes) → V4 (direct)
    V1 → V2 (thin stripes) → V3 (V3v) → V4

Both routes exist, and the **V3v relay is the more elaborated one**
for **kinetic boundaries and shape-from-motion** signals (as opposed
to V2's thin-stripe direct projection, which carries the **low-level
color and border signal**). **On the right, V3v's V4 relay feeds
the right V4 → LOC → right FFA (face) pathway** — the right's
ventral-stream face-recognition endpoint. **The right V3v is the
third stage of the right face-recognition pathway** after V1 and V2.

**The retinotopic organization of V3 is the second mirror-flip in
the hierarchy.** The alternating mirror-image pattern is:

    V1 upper field  →  lower bank (lingual gyrus)
    V2 upper field  →  upper bank (cuneus)  [mirror-flip #1, across
                                              the V1/V2 border =
                                              vertical meridian]
    V3 upper field  →  lower bank (lingual gyrus)  [mirror-flip #2,
                                              across the V2/V3 border
                                              = horizontal meridian,
                                              restoring V1's
                                              arrangement]

So **V3's bank assignment is the same as V1's** — the upper field is
on the lower bank (lingual gyrus) and the lower field is on the upper
bank (cuneus). This is the hallmark of an **even-numbered mirror-flip**
relative to V1: V1 (original), V2 (flip 1, reversed), V3 (flip 2,
back to V1's arrangement), V4 (flip 3, reversed again), and so on.

**Right-hemisphere specificity**: the right V3 processes the **LEFT**
visual hemifield of both eyes. Its **dorsal component (V3d)** projects
to **right MT/V5**, and the **right V3d → right MT/V5 relay is the
dominant motion-in-space substrate** in the human brain — it is the
principal cortical pathway for left-hemifield motion perception and
motion-in-depth, and it feeds the **right dorsal attention network**
(right IPS, right FEF). Its **ventral component (V3v)** projects to
**right V4**, contributing to the right **V4 → LOC → right FFA
(face)** pathway — the right V3v is the **third stage of the right
face-recognition pathway** after V1 and V2. The right V3's
**spatial_localization** is **dominant** — the right V3d and right
MT/V5 are the dominant motion-in-space and spatial-attention
substrate — and right V3 lesions produce **more severe
motion-boundary and depth-from-motion deficits**, **global
form-from-motion deficits**, and contribute to **left hemifield
neglect** (via the right V3d → right IPS pathway) and to
**prosopagnosia** (via the right V3v → right V4 → right LOC → right
FFA pathway).

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours (functional)
        caudally               V2 via the **V2/V3 border**
                               (retinotopically defined — the
                               horizontal meridian)
        dorsally               V3A via the **V3/V3A border**
                               (forward reference — not yet a
                               package under ``..cortex``)
        ventrally              V4 via the **V3/V4 border**
                               (V4 is a current package)
        medially               the cuneus (upper bank, lower-field
                               V3) and the lingual gyrus (lower
                               bank, upper-field V3)
        laterally              the lateral occipital gyrus (V3d
                               on the lateral surface)

    Functional overlays
        BA 18 — PARTIAL correspondence (V2 and V3 share BA 18)
            V3 is **one of the two V areas** that span BA 18.
        BA 19 — PARTIAL correspondence (V3 and V4 plus four
        forward references share BA 19)
            V3's **lateral extent** crosses the BA 18 / BA 19
            border into BA 19 territory. This is why V3's BA
            correlate is `(18, 19)` — the **only two-BA
            correlate** in the V hierarchy.
        V3d — dorsal component
            Motion, motion-boundary, optic flow, kinetic
            contours. Projects to MT/V5. **On the right, V3d is
            the DOMINANT motion substrate** — the right V3d →
            right MT/V5 relay is the dominant motion-in-space
            pathway and feeds the right dorsal attention
            network.
        V3v — ventral component
            Kinetic boundaries, shape-from-motion, shape-from-
            shading, shape-from-texture, stereopsis via
            disparity. Projects to V4. **On the right, V3v
            feeds the right V4 → LOC → right FFA (face)
            pathway.**
        cuneus — upper-bank V3
            The cuneus's lower margin carries the **V3 lower-field
            representation of the lower** contralateral visual
            field. **On the right, the lower LEFT field.** (Note:
            **V3 aligns with V1's bank assignment** — upper field
            on lingual gyrus, lower field on cuneus — because V3
            is a **double mirror-flip** of V1.)
        lingual gyrus — lower-bank V3
            The lingual gyrus carries the **V3 upper-field
            representation of the upper** contralateral visual
            field. **On the right, the upper LEFT field.**
            (Forward reference in ``..gyri`` — not yet a package.)
        calcarine sulcus — reference landmark
            The V2/V3 border (the **horizontal meridian**) is at
            the **fundus** of the calcarine sulcus. This is why
            the V2/V3 border is the **most retinotopically
            unambiguous** boundary in the occipital lobe.
        right fusiform face area (FFA) — downstream ventral-
        stream target
            **Right-specific overlay.** The right V3v's output —
            via V4 and the LOC — terminates in the right FFA.
            The V3v → V4 → LOC → FFA pathway is the **right
            face-recognition pathway**, and V3v is its **third
            stage** after V1 and V2.
        right MT/V5 — dominant dorsal-stream target
            **Right-specific overlay.** The right V3d's output —
            via right MT/V5 — is the **dominant motion-in-space
            substrate** for left-hemifield motion perception.
            The right V3d → right MT/V5 pathway is **stronger
            than the left V3d → left MT/V5 pathway**.
        right dorsal attention network — V3d downstream target
            **Right-emphasized overlay.** The right V3d's
            output — via MT/V5 — feeds the **right dorsal
            attention network** (right IPS, right FEF). The
            right V3d's contribution to left-hemifield spatial
            attention is part of the **right-lateralized dorsal
            attention substrate**.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours, the V3d / V3v distinction, the cuneus /
lingual-gyrus / calcarine overlays, and the **double-BA span** are the
same on both sides. What differs is the **visual hemifield** — the
right V3 processes the LEFT hemifield — the **downstream target
emphasis** — the right V3d → right MT/V5 pathway is the dominant
motion substrate, while the right V3v feeds the **right FFA (face)**
endpoint — and the **right dorsal attention network contribution**
via V3d.

--------------------------------------------------------------------------------
V-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    V2                                     **caudal neighbour** via the
                                           **V2/V3 border** — the
                                           horizontal-meridian
                                           boundary at the fundus of
                                           the calcarine sulcus.
                                           **V2 and V3 share BA 18.**
                                           V2 is V3's principal
                                           cortical afferent.
    V3A  (forward reference)               **dorsal rostral neighbour**
                                           — not yet a package. V3A
                                           continues the dorsal
                                           motion pathway and is
                                           the **core node of the
                                           right dorsal attention
                                           network**. V3d's output
                                           reaches V3A en route to
                                           MT/V5. **On the right,
                                           V3A is the more strongly
                                           engaged side.**
    V4                                     **ventral rostral
                                           neighbour**. V3v's output
                                           reaches V4 via the
                                           **V3v → V4 relay**. **On
                                           the right, V4 → LOC →
                                           right FFA is the face-
                                           recognition endpoint.**
    MT/V5  (forward reference)             **dorsal downstream target**
                                           — not yet a package.
                                           V3d's output reaches MT/V5
                                           via the **V3d → MT/V5
                                           relay**. **On the right,
                                           this relay is the
                                           DOMINANT motion
                                           substrate**.
    BA 18                                  **Shared with V2** — V3 is
                                           **one of the two** V
                                           areas that span BA 18.
    BA 19                                  **Shared with V4 and four
                                           forward references** —
                                           V3's **lateral extent**
                                           crosses the BA 18 / BA
                                           19 border, which is why
                                           V3's BA correlate is
                                           `(18, 19)`.
    cuneus (medial-surface gyrus)          carries the **V3 lower-field
                                           representation** of the
                                           lower visual field
                                           (**lower LEFT field on
                                           the right**). **V3 aligns
                                           with V1's bank
                                           assignment** (double
                                           mirror-flip).
    lingual gyrus (medial-surface          carries the **V3 upper-field
    gyrus; forward reference in ..gyri)    representation** of the
                                           upper visual field
                                           (**upper LEFT field on
                                           the right**).
    calcarine sulcus                       the fundus of the sulcus
                                           carries the **horizontal
                                           meridian**, which is the
                                           V2/V3 border.

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized. The field labels (LEFT vs RIGHT) in the
cuneus and lingual gyrus entries are updated for the right hemisphere,
and the right-emphasized notes on V3A and MT/V5 are added.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

V3 participates in **three** canonical occipital functional domains —
the **same three-domain count as V2**, but with **different domains**,
and **the same three-domain set on both hemispheres**. The emphasis is
as follows:

    spatial_localization                           (right emphasis — PRIMARY)
        **This is V3's defining contribution on the right — and the
        right's dominant one.** V3's **motion-boundary** and
        **depth-from-motion** representations contribute to the
        spatial localization that continues in V3A and MT/V5. **On
        the right, the spatial-localization contribution is
        DOMINANT** — the right V3d and right MT/V5 are the dominant
        motion-in-space and spatial-attention substrate, and the
        right V3d → right MT/V5 → right IPS pathway is part of the
        **right-lateralized dorsal attention network**. Right V3
        lesions contribute to **left hemispatial neglect** when the
        lesion extends to the right parietal and right frontal
        territories.

    form_and_object_perception                     (right emphasis — PRIMARY)
        **This is V3's second defining contribution.**
        V3v's **kinetic boundaries**, **shape-from-motion**,
        **shape-from-shading**, **shape-from-texture**, and
        **stereopsis via disparity** contribute to the **middle
        stages of form and object processing** that continue in
        V4 and the LOC. **On the right, the form-and-object
        contribution is weighted toward the ventral-stream
        endpoint** — V3v → right V4 → right LOC → **right FFA
        (face)**. This is the **right V3's most right-lateralized
        contribution** and the third stage of the right
        face-recognition pathway.

    binocular_vision                               (right emphasis — SECONDARY)
        V3v's **disparity-tuned neurons** — which are **more
        numerous and more selective in V3v than in V1 or V2** —
        support **fine stereoscopic depth perception** and
        **stereo-defined shape** (the perception of form from
        binocular disparity alone). On the right, binocular vision
        in V3v combines the right-eye and left-eye inputs to the
        **LEFT visual hemifield** and contributes to the right
        V4 → LOC → right FFA pathway via stereo-defined form.

**Right-specific caveat on `motion_perception`.** V3 is **not** the
motion area — that is **MT/V5**, a forward reference in BA 19.
V3d's **motion-boundary** and **motion-in-depth** processing are the
**input** to MT/V5, but **conscious motion perception** emerges in
MT/V5. `motion_perception` is **omitted** from the V3
`FUNCTIONAL_DOMAINS` tuple. **On the right, V3d's role is dominant**
(the right V3d is the dominant motion substrate), but even the right
V3 does **not** claim `motion_perception` as a primary domain — that
is MT/V5's territory.

**Right-specific caveat on `color_vision`.** V3 is **not** the
color-vision area — that is **V4**. V3v **projects to V4**, and V4
performs conscious color perception. `color_vision` is **omitted**.

**Right-specific caveat on `primary_visual_processing` and
`primary_visual_processing_secondary`.** These are V1's and V2's
domains, not V3's. Both are **omitted**.

**Right-specific caveat on `visual_attention`.** V3 is a **target**
of top-down attentional modulation and a **relay** to the dorsal
attention network (via MT/V5), but it is **not itself an attentional
control area**. `visual_attention` is **omitted** as a primary
domain.

**Right-specific caveat on `visual_word_processing` and `local_
featural_processing`.** These are **left-lateralized** functions
that the right V3 does **not** carry. `visual_word_processing` is
instantiated in the left VWFA (fed by the left V3v → left V4 → left
LOC → left VWFA pathway); `local_featural_processing` is a
left-hemisphere emphasis within `form_and_object_perception`. Neither
appears in the right V3 `FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the
**right V3 supports as an input stage** but does **not** carry as
primary functional domains. `face_processing` is instantiated in the
right FFA (fed by the right V3v → V4 → LOC → right FFA pathway);
`global_visual_processing` begins at right V2. Neither appears in
the right V3 `FUNCTIONAL_DOMAINS` tuple — **but the right V3v is the
third stage of the right face pathway and the right V3d's motion
processing contributes to the right dorsal attention network**.

**Summary**: V3 carries **exactly three** functional domains —
`spatial_localization`, `form_and_object_perception`, and
`binocular_vision`. **The FUNCTIONAL_DOMAINS set is IDENTICAL across
hemispheres** — **the first V area in the hierarchy whose domain set
is hemisphere-invariant**. The left-right differences are
**emphasis-only**:

    right V3  ←  spatial_localization DOMINANT (right V3d is the
                 dominant motion substrate; right V3d → right MT/V5
                 → right IPS is the dominant dorsal-attention
                 pathway); form_and_object_perception weighted
                 toward right FFA (face) endpoint
    left V3   ←  spatial_localization weaker than right;
                 form_and_object_perception weighted toward left
                 VWFA (reading) endpoint

This is a **structural simplification** compared to V1 and V2, and it
reflects the fact that V3's defining contributions (motion
boundaries, depth from motion, kinetic form) are
**lateralization-neutral** at the domain level — the lateralization
is in **how strongly** each domain is engaged, not in **which
domains are carried**.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), right — **indirect, via
          V2 (principal) and V1 (indirect)**
            **V3's dominant input is from V2, not directly from the
            LGN or V1.** V3 has **no direct LGN projections** and
            **no direct V1 projections** — the relay through V2 is
            obligate.
        → pulvinar (modulatory, **stronger to V3 than to V1**)
            The pulvinar sends a stronger modulatory projection to
            V3 than to V1. **On the right, the pulvinar → V3 loop
            is part of the right dorsal attention network
            substrate** (via its coupling with the V3d → MT/V5
            pathway).

    cortical afferents
        → V2, right
            **V3's principal cortical afferent.** The V2 → V3
            projection carries the **thick-stripe** (motion) and
            **thin-stripe** (color/form) signals that V3
            elaborates into motion boundaries, kinetic form, and
            shape-from-motion.

    cortical efferents — **the two-pathway output (V3d → MT/V5,
    V3v → V4)**
        → MT/V5, right (via **V3d**) — **forward reference**
            The **V3d → MT/V5 relay** carries the **motion-
            boundary** and **motion-in-depth** signal forward to
            the motion area. **On the right, this pathway is the
            DOMINANT motion substrate** — the right V3d → right
            MT/V5 relay is the dominant motion-in-space pathway,
            and it feeds the right dorsal attention network.
        → V4, right (via **V3v**)
            The **V3v → V4 relay** carries the **kinetic
            boundaries**, **shape-from-motion**, **shape-from-
            shading**, and **shape-from-texture** signals forward
            to V4. **On the right, this pathway feeds the right
            V4 → LOC → right FFA (face) pathway** — the right
            V3v is the **third stage of the right face pathway**.
        → LOC, right (via **V3v** and **V4**)
            V3v's output reaches the LOC via V4, contributing to
            the **object-recognition** stage of the ventral
            stream. **On the right, the V3v → V4 → LOC pathway
            terminates at the right FFA (faces)**.
        → V3A, right — **forward reference**
            V3d's output reaches V3A (the motion-in-depth and
            spatial-attention area) en route to MT/V5. **On the
            right, V3A is the more strongly engaged side**, and
            it is a core node of the right dorsal attention
            network.

    callosal connections
        → left V3
            The callosal fibers connect the right V3 to the left
            V3 across the occipital midline, supporting **the
            fusion of the two hemifields** at the V3 stage.

    attentional feedback
        → frontal eye fields (BA 8), right
            **Right-emphasized.** The right FEF is the dominant
            node of the right ventral attention network and sends
            strong **top-down and bottom-up attentional gain** to
            right V3.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), right
            The right DLPFC sends top-down attentional and
            working-memory signals to V3.
        → intraparietal sulcus, right
            **Right-emphasized.** The right IPS is a core node of
            the right dorsal attention network and sends strong
            top-down spatial-attention signals to right V3,
            supporting **spatial attention** in the LEFT visual
            hemifield. The right IPS → right V3 projection is
            part of the substrate for **sustained spatial
            attention**.
        → temporoparietal junction, right
            **Right-emphasized.** The right TPJ is the other core
            node of the right ventral attention network and sends
            reorienting signals to right V3 via the right FEF.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the **V3d → MT/V5 pathway** is the **dominant** V3 efferent on
the right, and it feeds the right dorsal attention network;
(b) the **V3v → V4 → LOC → right FFA pathway** is present and is
the third stage of the right face-recognition pathway;
(c) the right FEF, right IPS, and right TPJ send **stronger
attentional gain** to right V3 than the left's counterparts send to
left V3 (the right dorsal attention network dominates).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_v3_left_quadrantic_visual_field_defect
        **This is the right V3 anchor for the field defect.** V3's
        lesions produce **partial** field defects — a **left
        quadrantic** or **sectoranopic** defect — just as V2's
        do. The V3-specific field defect is often **more
        quadrantic** than V2's, because V3's upper and lower
        field banks are **widely separated**, so a lesion in V3
        is more likely to affect the upper **or** lower quadrant
        than to produce a complete hemianopia. **Often with
        macular sparing.**

    right_v3_motion_boundary_deficit_more_severe
        **This is the right V3 anchor par excellence.** Right V3d
        lesions produce **motion-boundary deficits** — the
        patient cannot perceive the **boundary** defined by
        motion (e.g., a figure defined only by the relative
        motion of its parts against the background). **The
        deficit is MORE SEVERE than the left V3d lesion's right
        hemifield deficit** — the right V3d is the **dominant
        motion-boundary substrate**, and the left V3d contributes
        but is not the primary substrate.

    right_v3_depth_from_motion_deficit_more_severe
        **This is the right V3's second dominant clinical
        signature.** Right V3d lesions produce **more severe
        impaired depth-from-motion** — the patient cannot
        perceive the **three-dimensional shape** of an object
        from its motion. **The deficit is MORE SEVERE than the
        left equivalent** — the right V3d is the dominant
        motion-in-depth substrate.

    right_v3_global_form_from_motion_deficit
        **On the right, V3v's contribution to form-from-motion
        is weighted toward the global / holistic aspect.**
        Right V3v lesions can produce **global-level form-from-
        motion deficits** — the patient may still perceive local
        contours defined by motion but cannot integrate them
        into a coherent global shape (Navon's global-precedence
        asymmetry is the framework). **This is a right-weighted
        anchor**; the left V3v lesion produces the complementary
        **local-level form-from-motion deficit**.

    right_v3_left_hemifield_neglect_contribution
        **Right-emphasized.** Right V3 lesions contribute to
        **left hemispatial neglect** when the lesion extends
        beyond V3 into the right parietal and right frontal
        territories. **Isolated right V3 lesions do not produce
        neglect** — the patient has a left quadrantic field
        defect but can attend to the left field cognitively —
        but the right V3's **V3d → MT/V5 → right IPS pathway**
        is part of the **right dorsal attention network**
        substrate that contributes to the neglect syndrome.
        **The right V3 is therefore the right-lateralized
        attentional substrate that the left V3 is not.** This
        anchor has no symmetric counterpart on the left.

    right_v3_contribution_to_prosopagnosia
        **Right-emphasized.** Right V3v is the **third stage**
        (after V1 and V2) of the right ventral stream that feeds
        the right FFA, and **right occipito-temporal lesions**
        that involve the right FFA or its input pathway produce
        **prosopagnosia**. **Isolated right V3 lesions do not
        produce prosopagnosia** — the right FFA is spared — but
        the right V3v is part of the **occipital input pathway**
        of the right-lateralized face-recognition system.
        **This anchor has no symmetric counterpart on the
        left.**

    right_v3_hemianopic_alexia_left
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **left homonymous field defect** (from
        a right V3 lesion) — is a recognized clinical entity,
        but **weaker than the left-side equivalent**. **A right
        V3 lesion produces a milder hemianopic alexia than a
        left V3 lesion** — the right-side lesion is in the non-
        dominant hemisphere for reading, and the reading network
        itself (left VWFA) is intact.

    right_v3_stereopsis_deficit
        **V3v's clinical signature via disparity.** Right V3v
        lesions can produce **impaired stereopsis** — reduced
        ability to perceive depth from binocular disparity,
        especially for **stereo-defined form**.

    right_v3_motion_defined_form_agnosia
        **A higher-order V3d/V3v interaction deficit.** Right V3
        lesions can produce **motion-defined form agnosia** —
        the patient cannot perceive **objects** or **faces**
        that are defined only by motion. **On the right, the
        deficit has an affective-salience component** — the
        patient may perceive kinetic form in isolation but
        cannot use it for **face recognition or emotional
        appraisal**.

    right_v3_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct**
        involving V3 produces a **left quadrantic defect**
        (from V3) on top of a **left homonymous hemianopia**
        (from V1). **Isolated right PCA infarcts do not
        produce alexia without agraphia.** **The V3-specific
        contribution is the motion-boundary and depth-from-
        motion deficits on top of the field defect** — and
        these are **more severe on the right** than the left
        equivalent.

    right_v3_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **V1, V2, AND V3**. **The V3
        contribution is the propagation of the aura into
        motion-defined and form-defined features** — kinetic
        fortifications, motion phosphenes. **This anchor is
        hemisphere-invariant.**

    right_v3_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **V1, V2, OR V3**. **V3 auras** are
        typically **more complex than V2 auras** — kinetic
        shapes, motion-defined forms, stereo phenomena. **Right
        V3 auras** project to the **left visual field**.

    right_v3_posterior_cortical_atrophy_benson_syndrome
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1, V2, AND V3 bilaterally**
        in later stages. **Right V3** is part of the substrate
        of the **progressive dorsal-stream dysfunction** that
        produces **Benson syndrome** — progressive
        prosopagnosia, visuospatial deficits, optic ataxia,
        simultanagnosia. **On the right, PCA presents with the
        visuospatial / prosopagnosic syndrome**; on the left,
        with progressive reading deficits.

    right_v3_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects**. **The V3 contribution** is the
        extrastriate involvement that produces **kinetic and
        motion-defined hallucinations** and **quadrantic
        defects**. **The syndrome is reversible** in most cases.

**The V3-specific clinical anchors** — `right_v3_motion_boundary_
deficit_more_severe`, `right_v3_depth_from_motion_deficit_more_
severe`, `right_v3_global_form_from_motion_deficit`,
`right_v3_left_hemifield_neglect_contribution`,
`right_v3_contribution_to_prosopagnosia`,
`right_v3_stereopsis_deficit`, and
`right_v3_motion_defined_form_agnosia` — are the **right-emphasized
mirror** of the left V3 anchors. **The motion-boundary and
depth-from-motion deficits are more severe on the right** because
the right V3d is the dominant motion substrate. **The
form-from-motion deficit is global rather than local** because the
right hemisphere is weighted toward global processing. **The left
hemifield neglect contribution and the prosopagnosia contribution
are right-only anchors** that have no symmetric counterpart on the
left.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both siblings**.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..cortex  (parent)
    The right occipital functional / V-numbered parent.

..primary_visual_cortex  (V1)
    **Distant caudal neighbour** via V2; no direct adjacency.

..v2
    **Caudal neighbour** via the **V2/V3 border** — the horizontal-
    meridian boundary at the fundus of the calcarine sulcus. **V2
    and V3 share BA 18.** V2 is V3's principal cortical afferent.

..v4
    **Ventral rostral neighbour**. V3v's output reaches V4 via the
    **V3v → V4 relay**. **On the right, V4 → LOC → right FFA is
    the face-recognition endpoint.**

...brodmann_areas.brodmann_area_18
    The **cytoarchitectonic counterpart — partial correspondence,
    not identity.** BA 18 spans **V2 and V3**.

...brodmann_areas.brodmann_area_19
    The **second cytoarchitectonic counterpart — partial
    correspondence, not identity.** BA 19 spans **V3, V4, V3A,
    V3B, V5/MT+, LOC**. V3's **lateral extent** crosses the BA
    18 / BA 19 border, which is why V3's BA correlate is
    `(18, 19)`.

...cuneus
    The medial-surface gyral landmark. **On the right, the
    cuneus's V3 lower-field representation carries the lower LEFT
    visual field.** V3 aligns with V1's bank assignment (double
    mirror-flip).

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus carries the **V3 upper-field representation
    of the upper** contralateral visual field. **On the right,
    the upper LEFT field.**

...sulci.calcarine_sulcus
    The **reference landmark** for the V2/V3 border.

...sulci.lunate_sulcus
    The inconstant lateral-surface landmark for the V1/V2 border
    (when present). **Not the V2/V3 border** — the V2/V3 border
    is retinotopic.

...sulci.transverse_occipital_sulcus
    The dorsal-surface landmark for the V3A / V3B territory.

..cortex.temporal
    The **ventral stream** continues from V3v (via V4 and the
    LOC) into the temporal lobe. **On the right, the ventral
    stream terminates in the right FFA** (the face area), and the
    right V3v is the **third stage** of this pathway. **Right
    occipito-temporal lesions produce prosopagnosia** — the
    canonical right-lateralized visual-recognition deficit. The
    temporal package must declare the right V3v as a source of
    its visual input via the ventral stream, and must note the
    **right-lateralized FFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from V3d (via MT/V5) into the
    parietal lobe. **On the right, the dorsal stream is more
    strongly engaged during visuospatial attention**, and the
    right V3d → right MT/V5 → right IPS pathway is the dominant
    dorsal-attention substrate. The parietal package must declare
    the right V3d as a source of its visual input for the dorsal
    stream, and must note the **right-lateralized attentional
    emphasis**.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V3. **On the right, the right FEF is the dominant
    node of the ventral attention network**, and right frontal
    lesions contribute to left hemispatial neglect.

..cortex.cingulate  — indirect
    No direct cingulate → V3 projection.

..cortex.insular  — indirect
    No direct insular → V3 projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the **indirect** source of V3's input via the
    V1 → V2 → V3 relay. **V3 has no direct LGN projection.**

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V3
    than to V1**. **On the right, the pulvinar → V3 loop is part
    of the right dorsal attention network substrate.**

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from V3v (via V4 and the LOC)
    to the perirhinal, entorhinal, and parahippocampal cortices.
    **On the right, the parahippocampal place area (PPA) and the
    retrosplenial complex receive visual input supporting scene
    and spatial memory**, which are more strongly right-
    lateralized.

../../left/cortex/occipital/cortex/v3
    The left-hemisphere homologue. Structural fields (V-number,
    two-BA correlate (18, 19), V3d/V3v distinction, mirror-flip
    retinotopy, V2/V3 and V3/V4 borders, double-BA span,
    FUNCTIONAL_DOMAINS set, forward-declaration caveat text) MUST
    be byte-identical. Functional emphasis and clinical
    significance diverge — the right V3 processes the **LEFT**
    visual hemifield, is weighted toward the
    **spatial-localization and motion-boundary** aspect, and its
    V3v output feeds the **right V4 → LOC → right FFA** (face)
    pathway rather than the left V4 → LOC → left VWFA (reading)
    pathway.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "v3"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    V_NUMBER            = "V3"
    ALTERNATE_NAMES     = ("tertiary_visual_cortex",
                           "v3",
                           "brodmann_area_18_and_19_double_partial")
        # **Byte-identical to the left sibling's.**

    ARCHITECTONIC_SIGNATURES = (
        "dysgranular_extrastriate_cortex",
        "retinotopic_boundary_v2_v3_horizontal_meridian",
        "no_single_architectonic_signature",
    )
        # **Byte-identical to the left sibling's.**

    BRODMANN_CORRELATES = (18, 19)
        # **Two BAs** — the **only two-BA correlate** in the V
        # hierarchy. **Byte-identical to the left sibling's.**

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** Byte-identical.

    RETINOTOPIC_MAP     = "double_mirror_flip_of_V2_aligns_with_V1_bank_assignment"
        # The map's *structure* is identical to the left's.
        # **On the right, the represented hemifield is the LEFT
        # hemifield.**

    VISUAL_HEMIFIELD    = "left"
        # **The represented visual hemifield** — right V3
        # processes the LEFT hemifield.

    FUNCTIONAL_DOMAINS  = (
                              "spatial_localization",
                              "form_and_object_perception",
                              "binocular_vision",
                              # **Identical set to the left V3's
                              # AND to the right V2's-minus-V3's-
                              # spatial_localization.** V3 is the
                              # **first V area whose FUNCTIONAL_
                              # DOMAINS set is hemisphere-
                              # invariant**. The left-right
                              # differences are emphasis-only.
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "spatial_localization":
                                  "motion_boundary_and_depth_from_"
                                  "motion_dominant_via_v3d_to_"
                                  "right_mt_v5_dorsal_attention_"
                                  "network",
                              "form_and_object_perception":
                                  "dynamic_form_and_shape_from_"
                                  "motion_feeding_right_v4_loc_"
                                  "right_ffa_face_pathway",
                              "binocular_vision":
                                  "stereo_depth_and_shape_from_"
                                  "disparity_v3v_left_hemifield",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_v3_left_quadrantic_visual_"
                              "field_defect",
                              "right_v3_motion_boundary_deficit_"
                              "more_severe",
                              "right_v3_depth_from_motion_"
                              "deficit_more_severe",
                              "right_v3_global_form_from_motion_"
                              "deficit",
                              "right_v3_left_hemifield_neglect_"
                              "contribution",
                              "right_v3_contribution_to_"
                              "prosopagnosia",
                              "right_v3_hemianopic_alexia_left",
                              "right_v3_stereopsis_deficit",
                              "right_v3_motion_defined_form_"
                              "agnosia",
                              "right_v3_occipital_infarct_pca_"
                              "territory",
                              "right_v3_migraine_visual_aura",
                              "right_v3_occipital_epilepsy_"
                              "visual_auras",
                              "right_v3_posterior_cortical_"
                              "atrophy_benson_syndrome",
                              "right_v3_pres_visual_symptoms",
                          )

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "AREA_NAME",
        "HEMISPHERE",
        "LOBE",
        "V_NUMBER",
        "ALTERNATE_NAMES",
        "ARCHITECTONIC_SIGNATURES",
        "BRODMANN_CORRELATES",
        "NAMING_COLLISION_WITH",
        "RETINOTOPIC_MAP",
        "VISUAL_HEMIFIELD",
        "FUNCTIONAL_DOMAINS",
        "DOMAIN_EMPHASIS",
        "CONNECTIVITY",
        "CLINICAL_ANCHORS",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references V3 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are two forward-declaration caveats for this package.**

1. **V3A is a forward reference** — not yet a package under
   ``..cortex``. **On the right, V3A is the more strongly engaged
   side**, and it is a core node of the right dorsal attention
   network. Creating the V3A package is the most urgent future
   resolution for the dorsal stream.

2. **MT/V5 is a forward reference** — not yet a package under
   ``..cortex``. **On the right, MT/V5 is the dominant motion
   hemisphere**, and the right V3d → right MT/V5 relay is the
   dominant motion-in-space pathway. Creating the MT/V5 package is
   the second most urgent resolution.

**Both forward references must be resolved before V3's clinical
anchors are finalised** — **on the right, resolving them is more
urgent than on the left**, because the right V3A and right MT/V5 are
the **dominant dorsal-stream substrates**, and the right V3d's
contribution is only fully characterised when those two areas are
modelled.

**Both forward references are byte-identical to the left sibling's**
— they are properties of the V-area hierarchy, not of the
hemisphere. **The right-specific urgency emphasis is the only
textual divergence**, and it is required by the right's functional
dominance in motion and attention.

--------------------------------------------------------------------------------
PROMOTION RULE (when a V sub-field becomes a package)
--------------------------------------------------------------------------------

V3 is **the most likely V area to be split in the current tree** —
the V3d / V3v distinction is well-established in the retinotopic
literature. If a future parcellation promotes this split, the
promotion takes this form:

    v3/
        __init__.py
        v3d_dorsal/             # → MT/V5, motion/motion-in-depth
            __init__.py
        v3v_ventral/            # → V4, kinetic form/shape-from-motion
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the left side in the same commit.

**The V3d / V3v split is a legitimate retinotopic subdivision.** **On
the right, the V3d component is the DOMINANT dorsal-stream
contributor** — it feeds the right MT/V5, which is the dominant
motion hemisphere, and it is the substrate for the more severe
motion-boundary and depth-from-motion deficits on the right. **The
right V3v component feeds the right FFA (face) pathway** and is the
third stage of the right face-recognition system.

**The split preserves the two-BA span**: V3d and V3v both inherit the
parent's `(18, 19)` `BRODMANN_CORRELATES`, because the BA 18 / BA 19
border sits **within** V3.

**The split requires a joint revision of BA 18's and BA 19's
`V_AREA_CORRELATE` entries**, with the same hemisphere-invariant
labeling convention as the left's promotion — the exact form must be
decided **once** and applied to both hemispheres in the same commit.

**No split should be performed while V3A and MT/V5 are unresolved**
— the split's main downstream targets are V3A and MT/V5 (for V3d)
and V4 (for V3v).

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../v3``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "v3"
        LOBE                         "occipital"
        V_NUMBER                     "V3"
        ALTERNATE_NAMES              ("tertiary_visual_cortex",
                                     "v3",
                                     "brodmann_area_18_and_19_"
                                     "double_partial")
        ARCHITECTONIC_SIGNATURES     (three signatures —
                                     dysgranular, retinotopic
                                     V2/V3 border, no single
                                     architectonic signature)
        BRODMANN_CORRELATES          (18, 19) — two BAs
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same double mirror-flip
                                     structure
        FUNCTIONAL_DOMAINS set       the same three domains
                                     (spatial_localization,
                                     form_and_object_perception,
                                     binocular_vision) — **the
                                     first V area whose domain
                                     set is hemisphere-invariant**
        Bounding / overlapping territories
        V-to-neighbour adjacency (with the LEFT / RIGHT field
                                     labels updated)
        CONNECTIVITY                 same bundle names
        The forward-declaration caveat text (byte-identical,
                                     with the right-specific
                                     emphasis note documented)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — right V3 processes
                               the LEFT hemifield.
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        DOMAIN_EMPHASIS        right: spatial_localization is
                               "motion_boundary_and_depth_from_
                               motion_dominant_via_v3d_to_right_
                               mt_v5_dorsal_attention_network";
                               form_and_object_perception is
                               "dynamic_form_and_shape_from_
                               motion_feeding_right_v4_loc_right_
                               ffa_face_pathway"; binocular_
                               vision is "stereo_depth_and_shape_
                               from_disparity_v3v_left_hemifield".
                               left: spatial_localization is
                               "motion_boundary_and_depth_from_
                               motion_weaker_than_right_via_v3d_
                               to_left_mt_v5"; etc.
        CONNECTIVITY           same bundle names; right: the
                               V3d → MT/V5 pathway is the
                               **dominant** V3 efferent (feeds
                               the right MT/V5 and the right
                               dorsal attention network); the
                               V3v → V4 → LOC → right FFA
                               pathway is the third stage of
                               the right face-recognition
                               pathway.
                               left: the V3v → V4 → LOC → left
                               VWFA pathway is the **dominant**
                               V3 efferent (reading endpoint);
                               the V3d → MT/V5 pathway is
                               present but weaker.
        CLINICAL_ANCHORS       right: fourteen anchors (left
                               quadrantic visual field defect,
                               **motion-boundary deficit more
                               severe**, **depth-from-motion
                               deficit more severe**, **global
                               form-from-motion deficit**,
                               **left hemifield neglect
                               contribution**, **prosopagnosia
                               contribution**, hemianopic alexia
                               (left, milder), stereopsis
                               deficit, motion-defined form
                               agnosia, right occipital
                               infarct, migraine aura, occipital
                               epilepsy, PCA with Benson
                               syndrome, PRES).
                               left: twelve anchors (right
                               quadrantic visual field defect,
                               motion-boundary deficit, depth-
                               from-motion deficit, local
                               form-from-motion deficit,
                               hemianopic alexia (right),
                               stereopsis deficit, motion-
                               defined form agnosia, left
                               occipital infarct, migraine
                               aura, occipital epilepsy, PCA,
                               PRES).

**The visual-hemifield asymmetry is the sharpest single entry.**

**The FUNCTIONAL_DOMAINS set is IDENTICAL across hemispheres.** This
is the **first V area in the hierarchy whose domain set is
hemisphere-invariant** — V1 and V2 both have four on the right and
three on the left, but **V3 has the same three on both sides**. The
left-right differences are **emphasis-only**.

**The emphasis asymmetry is the second sharpest entry.** The **right**
V3's `spatial_localization` is **dominant** (right V3d is the
dominant motion substrate; right V3d → right MT/V5 → right IPS is
the dominant dorsal-attention pathway), while the **left** V3's is
weaker. The **right** V3's `form_and_object_perception` is weighted
toward the **right FFA (face)** endpoint, while the **left** V3's is
weighted toward the **left VWFA (reading)** endpoint.

**The right-specific clinical anchors are the third sharpest entry.**
The right V3 carries **four anchors** that the left does not carry at
the same weighting: `right_v3_motion_boundary_deficit_more_severe`,
`right_v3_depth_from_motion_deficit_more_severe`,
`right_v3_left_hemifield_neglect_contribution`, and
`right_v3_contribution_to_prosopagnosia`. The `global_form_from_
motion_deficit` is the right's mirror of the left's
`local_form_from_motion_deficit`. The left V3's
`left_v3_local_form_from_motion_deficit` anchor is **left-only**.

**The V3d / V3v split is a shared structural fact.** Both
hemispheres carry the same split, but the **relative weighting**
differs — **right V3d is dominant**, **left V3v is dominant**.

**The two-BA correlate (18, 19), the mirror-flip retinotopy, the
architectonic signatures, and the FUNCTIONAL_DOMAINS set are
byte-identical on both sides.**

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "v3" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V3".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's
    (including "brodmann_area_18_and_19_double_partial").
[ ] ARCHITECTONIC_SIGNATURES is byte-identical to the left
    sibling's (dysgranular, retinotopic V2/V3 border, no single
    signature).
[ ] BRODMANN_CORRELATES is exactly ``(18, 19)`` — byte-identical
    to the left sibling's.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **double mirror-flip** structure
    with the **LEFT hemifield label**.
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class
    field.
[ ] FUNCTIONAL_DOMAINS contains **three** domains:
    - spatial_localization
    - form_and_object_perception
    - binocular_vision
[ ] **The FUNCTIONAL_DOMAINS set is verified to be IDENTICAL across
    hemispheres** — the **first V area with a hemisphere-invariant
    domain set**.
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception,
    color_vision, primary_visual_processing,
    primary_visual_processing_secondary, visual_attention,
    visual_word_processing, face_processing, global_visual_
    processing (same exclusions as left V3).
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis** per
    domain:
    - spatial_localization → motion_boundary_and_depth_from_
      motion_dominant_via_v3d_to_right_mt_v5_dorsal_attention_
      network
    - form_and_object_perception → dynamic_form_and_shape_from_
      motion_feeding_right_v4_loc_right_ffa_face_pathway
    - binocular_vision → stereo_depth_and_shape_from_disparity_v3v_
      left_hemifield
[ ] CONNECTIVITY documents:
    - V2 → V3 principal cortical afferent (the obligate relay;
      V3 has **no direct LGN and no direct V1 projections**)
    - Pulvinar afferent (stronger to V3 than to V1; part of the
      right dorsal attention network substrate)
    - **V3d → MT/V5 relay** (motion-boundary, motion-in-depth;
      **DOMINANT on the right**; feeds the right MT/V5 and the
      right dorsal attention network)
    - **V3v → V4 relay** (kinetic form, shape-from-motion; feeds
      the right V4 → LOC → right FFA face pathway)
    - **V3v → LOC relay** (via V4, right FFA face endpoint)
    - V3d → V3A (forward reference; motion-in-depth and spatial
      attention; dominant on the right)
    - Callosal connections to left V3
    - Attentional feedback from right FEF, right DLPFC, right
      IPS, right TPJ
[ ] CLINICAL_ANCHORS contains the fourteen right-specific anchors:
    - right_v3_left_quadrantic_visual_field_defect
    - **right_v3_motion_boundary_deficit_more_severe**
    - **right_v3_depth_from_motion_deficit_more_severe**
    - **right_v3_global_form_from_motion_deficit**
    - **right_v3_left_hemifield_neglect_contribution**
    - **right_v3_contribution_to_prosopagnosia**
    - right_v3_hemianopic_alexia_left
    - right_v3_stereopsis_deficit
    - right_v3_motion_defined_form_agnosia
    - right_v3_occipital_infarct_pca_territory
    - right_v3_migraine_visual_aura
    - right_v3_occipital_epilepsy_visual_auras
    - right_v3_posterior_cortical_atrophy_benson_syndrome
    - right_v3_pres_visual_symptoms
[ ] The **motion-boundary deficit (more severe)** is documented
    as the primary right V3 anchor — the right V3d is the dominant
    motion-boundary substrate.
[ ] The **depth-from-motion deficit (more severe)** is documented
    as the second dominant right V3 anchor.
[ ] The **global form-from-motion deficit** is documented as the
    right-lateralized form-from-motion anchor — the mirror of the
    left's local deficit.
[ ] **Left hemifield neglect contribution** and **prosopagnosia
    contribution** are documented as **right-emphasized anchors**
    that have no symmetric counterpart on the left.
[ ] **Hemianopic alexia (left)** is documented as a right-side
    anchor that is **milder** than the left-side equivalent.
[ ] **The right V3's dominant spatial_localization contribution**
    is documented — the right V3d → right MT/V5 → right IPS
    pathway is the dominant dorsal-attention substrate, and
    right V3 lesions contribute to left hemispatial neglect.
[ ] **The right V3v → right V4 → right LOC → right FFA pathway**
    is documented as the right face-recognition pathway, with
    the right V3v being its **third stage**.
[ ] **The two-BA span (18, 19)** is documented as V3's defining
    structural fact.
[ ] **The V3d / V3v split** is documented, with the **right V3d
    being dominant** (vs left V3v).
[ ] **The double mirror-flip** is documented with the LEFT
    hemifield label.
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — V3 is the first V area with a
    hemisphere-invariant domain set.
[ ] **The emphasis asymmetry is verified**: right
    spatial_localization is "dominant"; left is "weaker than
    right." Right form_and_object_perception feeds the right
    FFA; left feeds the left VWFA.
[ ] **The right V3d / V3v weighting is verified**: V3d is
    dominant on the right (feeds MT/V5 and the dorsal attention
    network); V3v feeds the right FFA (face) endpoint.
[ ] **The two forward references — V3A and MT/V5** — are
    documented, the **resolution rule** is recorded, and the
    **right-specific urgency emphasis** is present.
[ ] No SUBDIVISIONS promotion is performed while V3A and MT/V5
    are unresolved.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, **FUNCTIONAL_DOMAINS set**, forward-declaration
    caveat text) match the left sibling; VISUAL_HEMIFIELD,
    DOMAIN_EMPHASIS (spatial-localization dominant vs weaker;
    form endpoint = right FFA vs left VWFA), CONNECTIVITY emphasis
    (right V3d-dominant vs left V3v-dominant), and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    V3 carries "left_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP.
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — V3's three-domain set is hemisphere-
    invariant.
[ ] **The right-specific clinical anchors are verified**:
    `right_v3_motion_boundary_deficit_more_severe`,
    `right_v3_depth_from_motion_deficit_more_severe`,
    `right_v3_left_hemifield_neglect_contribution`, and
    `right_v3_contribution_to_prosopagnosia` are present on the
    right and absent on the left. The left-only
    `left_v3_local_form_from_motion_deficit` is absent on the
    right.
[ ] Any downstream code querying "what does the right V3 see?"
    must receive "the LEFT visual hemifield."
[ ] Any downstream code querying "what is V3?" must receive "the
    tertiary visual cortex / V3 / part of BA 18 AND part of
    BA 19" — the **double partial correspondence** is enforced.
[ ] Any downstream code querying "is V3's FUNCTIONAL_DOMAINS set
    the same on both hemispheres?" must receive "yes — V3 is the
    first V area with a hemisphere-invariant domain set; only
    the emphasis differs."
[ ] Any downstream code assigning the right face pathway must
    route through the **right** V1 → V2 → V3v → V4 → LOC →
    right FFA chain.
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** V1 → V2 → V3v → V4 → LOC →
    left VWFA chain.
[ ] Any downstream code assigning motion-boundary or
    depth-from-motion processing must route through the **V3d →
    MT/V5** chain — the V3d is the motion-boundary relay, not
    the motion-perception operation itself. **On the right, this
    chain is the dominant motion substrate.**
[ ] Any downstream code assigning left hemispatial neglect must
    note that **right V3d's V3d → MT/V5 → right IPS pathway is a
    contributor**, not a sole cause.
"""