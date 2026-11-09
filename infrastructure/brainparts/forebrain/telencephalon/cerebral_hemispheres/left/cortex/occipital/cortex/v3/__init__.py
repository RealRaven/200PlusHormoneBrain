"""
Tertiary Visual Cortex (V3) — Left Hemisphere
==============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── v3   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the left
hemisphere's **V3** — the **tertiary visual cortex**, the second
extrastriate belt area, and the immediate downstream target of V2. It
is the **first V area in the hierarchy whose BA correlate spans two
Brodmann areas** (BA 18 **and** BA 19), and the **first V area whose
primary functional contribution is spatial-localization and
motion-boundary processing** rather than low-level feature extraction.

Parent: ``..cortex`` (left occipital functional / V-numbered parent)
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
``../../right/cortex/occipital/cortex/v3``. The V-number, the two-BA
correlate (18, 19), the V3d / V3v subregion distinction, the
mirror-flip retinotopy, the V2/V3 and V3/V4 borders, and the relay
to MT/V5 and V4 are identical on both sides; the **functional
emphasis** and **clinical significance** diverge — on the left, V3 is
weighted toward the **ventral-stream form-processing** aspect (V3d
and V3v both feeding V4 and the LOC, and from there the left VWFA),
the left V3's **spatial_localization** is **weaker than the right's**,
and left V3 lesions produce **local-level form-from-motion deficits**
and a narrower **motion-boundary impairment** than the right
equivalent.

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
                            **On the left, V3d's motion
                            contribution is present but weaker
                            than the right's** — the right V3d
                            and right MT/V5 are the dominant
                            motion-and-motion-in-depth substrate.

    V3v (ventral V3)        the ventral aspect, adjacent to V4v
                            and hV4. Functionally weighted
                            toward **form and shape from
                            motion**: kinetic boundaries,
                            shape from shading, shape from
                            texture, stereopsis via disparity.
                            Projects strongly to **V4**.
                            **On the left, V3v's form contribution
                            feeds the left V4 → LOC → left VWFA
                            (reading) pathway**.

**V3d and V3v are distinct enough that some parcellations split V3
into two separate V areas** (V3d and V3v, with V3v sometimes
called VP for "ventral posterior"). **The current tree keeps them
together as "V3"**, consistent with the parent's
``V_AREA_CORRELATE`` entry, but the docstring documents the split
because it is the **most important structural fact** about V3 and
because the eventual V3 → V3d + V3v split is the most likely future
promotion (see the PROMOTION RULE section).

**The relay to MT/V5 is V3's most consequential connectivity.**
V3's **dorsal component (V3d)** projects to **MT/V5** and is the
**principal cortical relay** for the dorsal stream's motion pathway:

    V1 → V2 (thick stripes) → V3 (V3d) → MT/V5
    V1 → V2 (thick stripes) → MT/V5 (direct)

Both routes exist, but the **V3d relay is the more elaborated one**
for **motion-boundary and motion-in-depth** signals (as opposed to
V2's thick-stripe direct projection, which carries the **low-level
motion signal**). **On the left, V3d's MT/V5 relay carries the left's
contribution to right-hemifield motion perception at a lower
weighting than the right V3d's** — the right V3d → right MT/V5
pathway is the dominant motion substrate.

**The relay to V4 is V3's second major connectivity.**
V3's **ventral component (V3v)** projects to **V4** and is the
**principal cortical relay** for the ventral stream's form pathway:

    V1 → V2 (thin stripes) → V4 (direct)
    V1 → V2 (thin stripes) → V3 (V3v) → V4

Both routes exist, and the **V3v relay is the more elaborated one**
for **kinetic boundaries and shape-from-motion** signals (as opposed
to V2's thin-stripe direct projection, which carries the **low-level
color and border signal**). **On the left, V3v's V4 relay feeds the
left V4 → LOC → left VWFA (reading) pathway** — the left's
ventral-stream contribution.

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

**Left-hemisphere specificity**: the left V3 processes the **RIGHT**
visual hemifield of both eyes. Its **dorsal component (V3d)** projects
to **left MT/V5**, contributing to right-hemifield motion perception
at a **lower weighting** than the right V3d's left-hemifield
contribution. Its **ventral component (V3v)** projects to **left V4**,
contributing to the left **V4 → LOC → left VWFA (reading)** pathway —
the left V3v is the **third stage of the left reading pathway** after
V1 and V2. The left V3's **spatial_localization** is **weaker than
the right's** — the right V3d and right MT/V5 are the dominant
motion-in-space substrate — and left V3 lesions produce **local-level
form-from-motion deficits** and a **narrower motion-boundary
impairment** than the right equivalent.

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
            V3 is **one of the two V areas** that span BA 18. The
            V2/V3 border represents the **horizontal meridian**,
            and the BA 18 / BA 19 border (which is **retinotopic
            and variable**) roughly coincides with the transition
            from V3 to V3A / V4.
        BA 19 — PARTIAL correspondence (V3 and V4 plus four
        forward references share BA 19)
            V3's **lateral extent** crosses the BA 18 / BA 19
            border into BA 19 territory. This is why V3's BA
            correlate is `(18, 19)` — the **only two-BA
            correlate** in the V hierarchy.
        V3d — dorsal component
            Motion, motion-boundary, optic flow, kinetic
            contours. Projects to MT/V5. **On the left, weaker
            than the right.**
        V3v — ventral component
            Kinetic boundaries, shape-from-motion, shape-from-
            shading, shape-from-texture, stereopsis via
            disparity. Projects to V4. **On the left, feeds the
            left V4 → LOC → left VWFA (reading) pathway.**
        cuneus — upper-bank V3
            The cuneus's lower margin carries the **V3 lower-field
            representation of the lower** contralateral visual
            field. **On the left, the lower RIGHT field.** (Note:
            **V3 aligns with V1's bank assignment** — upper field
            on lingual gyrus, lower field on cuneus — because V3
            is a **double mirror-flip** of V1.)
        lingual gyrus — lower-bank V3
            The lingual gyrus carries the **V3 upper-field
            representation of the upper** contralateral visual
            field. **On the left, the upper RIGHT field.**
            (Forward reference in ``..gyri`` — not yet a package.)
        calcarine sulcus — reference landmark
            The V2/V3 border (the **horizontal meridian**) is at
            the **fundus** of the calcarine sulcus. This is why
            the V2/V3 border is the **most retinotopically
            unambiguous** boundary in the occipital lobe — it
            coincides with the horizontal meridian, which is
            localized at the sulcal fundus.
        left visual word form area (VWFA) — downstream
        ventral-stream target
            **Left-specific overlay.** The left V3v's output — via
            V4 and the LOC — terminates in the left VWFA. The
            V3v → V4 → LOC → VWFA pathway is the **left reading
            pathway**, and V3v is its **third stage** after V1
            and V2.
        left MT/V5 — downstream dorsal-stream target
            **Left-specific overlay (weak).** The left V3d's
            output — via left MT/V5 — contributes to right-
            hemifield motion perception. The left V3d → left
            MT/V5 pathway is present but **weaker than the right
            V3d → right MT/V5 pathway**.

**This field is structurally identical to the right sibling's** — the
architectonic neighbours, the V3d / V3v distinction, the cuneus /
lingual-gyrus / calcarine overlays, and the **double-BA span** are the
same on both sides. What differs is the **visual hemifield** — the
left V3 processes the RIGHT hemifield — and the **downstream target
emphasis** — the left V3v feeds the left VWFA (reading), while the
right V3v feeds the right FFA (face).

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
                                           cortical afferent for the
                                           low-level motion and
                                           border signals that V3
                                           elaborates.
    V3A  (forward reference)               **dorsal rostral neighbour**
                                           — not yet a package. V3A
                                           continues the dorsal
                                           motion pathway and is
                                           the **core node of the
                                           right dorsal attention
                                           network**. V3d's output
                                           reaches V3A en route to
                                           MT/V5.
    V4                                     **ventral rostral
                                           neighbour**. V3v's output
                                           reaches V4 via the
                                           **V3v → V4 relay**, which
                                           is the second step of
                                           the ventral-stream form
                                           pathway (after V2's thin
                                           stripes).
    MT/V5  (forward reference)             **dorsal downstream target**
                                           — not yet a package.
                                           V3d's output reaches MT/V5
                                           via the **V3d → MT/V5
                                           relay**, which is the
                                           principal cortical relay
                                           for motion-boundary and
                                           motion-in-depth signals.
    BA 18                                  **Shared with V2** — V3 is
                                           **one of the two** V
                                           areas that span BA 18.
                                           The BA 18 / V3
                                           relationship is partial
                                           correspondence.
    BA 19                                  **Shared with V4 and four
                                           forward references** —
                                           V3's **lateral extent**
                                           crosses the BA 18 / BA
                                           19 border, which is why
                                           V3's BA correlate is
                                           `(18, 19)`. The BA 19 /
                                           V3 relationship is also
                                           partial correspondence.
    cuneus (medial-surface gyrus)          carries the **V3 lower-field
                                           representation** of the
                                           lower visual field
                                           (**lower RIGHT field on
                                           the left**). **V3 aligns
                                           with V1's bank
                                           assignment** (double
                                           mirror-flip).
    lingual gyrus (medial-surface          carries the **V3 upper-field
    gyrus; forward reference in ..gyri)    representation** of the
                                           upper visual field
                                           (**upper RIGHT field on
                                           the left**).
    calcarine sulcus                       the fundus of the sulcus
                                           carries the **horizontal
                                           meridian**, which is the
                                           V2/V3 border. **This is
                                           V3's most reliable
                                           retinotopic landmark.**

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

V3 participates in **three** canonical occipital functional domains —
the **same three-domain count as V2**, but with **different domains**.
The emphasis is as follows:

    spatial_localization                           (left emphasis — PRIMARY)
        **This is V3's defining contribution — the first V area
        in the hierarchy whose primary role is spatial
        localization.** V3's **motion-boundary** and **depth-
        from-motion** representations contribute to the early
        stages of spatial localization that continue in V3A and
        MT/V5. **On the left, the spatial-localization
        contribution is present but weaker than the right's** —
        the right V3d and right MT/V5 are the dominant motion-in-
        space and spatial-attention substrate. The left V3's
        spatial-localization contribution is predominantly via
        **V3d's relay to left MT/V5**, not via the right-
        lateralized dorsal attention network.

    form_and_object_perception                     (left emphasis — PRIMARY)
        **This is V3's second defining contribution.**
        V3v's **kinetic boundaries**, **shape-from-motion**,
        **shape-from-shading**, **shape-from-texture**, and
        **stereopsis via disparity** contribute to the **middle
        stages of form and object processing** that continue in
        V4 and the LOC. **On the left, the form-and-object
        contribution is weighted toward the ventral-stream
        endpoint** — V3v → left V4 → left LOC → **left VWFA
        (reading)**. This is the **left V3's most left-lateralized
        contribution** and the third stage of the left reading
        pathway.

    binocular_vision                               (left emphasis — SECONDARY)
        V3v's **disparity-tuned neurons** — which are **more
        numerous and more selective in V3v than in V1 or V2** —
        support **fine stereoscopic depth perception** and
        **stereo-defined shape** (the perception of form from
        binocular disparity alone). On the left, binocular vision
        in V3v combines the right-eye and left-eye inputs to the
        **RIGHT visual hemifield** and contributes to the left
        V4 → LOC → left VWFA pathway via stereo-defined form.

**Left-specific caveat on `motion_perception`.** V3 is **not** the
motion area — that is **MT/V5**, a forward reference in BA 19.
V3d's **motion-boundary** and **motion-in-depth** processing are the
**input** to MT/V5, but **conscious motion perception** emerges in
MT/V5. `motion_perception` is **omitted** from the V3
`FUNCTIONAL_DOMAINS` tuple. **On the right, V3d's role is more
strongly weighted** (the right V3d is dominant), but even the right
V3 does **not** claim `motion_perception` as a primary domain — that
is MT/V5's territory.

**Left-specific caveat on `color_vision`.** V3 is **not** the
color-vision area — that is **V4**. V3v **projects to V4**, and V4
performs conscious color perception. `color_vision` is **omitted**
from the V3 `FUNCTIONAL_DOMAINS` tuple.

**Left-specific caveat on `primary_visual_processing` and
`primary_visual_processing_secondary`.** These are V1's and V2's
domains, not V3's. V3 processes **elaborated** signals (motion
boundaries, kinetic form), not low-level features. Both are
**omitted**.

**Left-specific caveat on `visual_attention`.** V3 is a **target**
of top-down attentional modulation and a **relay** to the dorsal
attention network (via MT/V5), but it is **not itself an attentional
control area**. `visual_attention` is **omitted** as a primary
domain.

**Left-specific caveat on `visual_word_processing`.** V3v is the
**third stage** of the left reading pathway (V1 → V2 → V3v → V4 →
LOC → VWFA), but V3v itself does **not** perform word processing.
`visual_word_processing` is **omitted**.

**Left-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the left
V3 does **not** carry. `face_processing` is instantiated in the
right FFA (fed by the right V3v → V4 → LOC → right FFA pathway);
`global_visual_processing` begins at right V2. Neither appears in the
left V3 `FUNCTIONAL_DOMAINS` tuple.

**Summary**: V3 carries **exactly three** functional domains —
`spatial_localization`, `form_and_object_perception`, and
`binocular_vision`. **The FUNCTIONAL_DOMAINS set is IDENTICAL across
hemispheres** — unlike V1 (four on the right, three on the left) and
V2 (four on the right, three on the left), **V3 has the same three
domains on both sides**. **This is the first V area in the hierarchy
whose domain set is hemisphere-invariant.** The left-right
differences are **emphasis-only**:

    left V3   ←  spatial_localization weaker than right;
                 form_and_object_perception weighted toward
                 ventral-stream (reading) endpoint
    right V3  ←  spatial_localization dominant;
                 form_and_object_perception weighted toward
                 ventral-stream (face) endpoint

This is a **structural simplification** compared to V1 and V2, and it
reflects the fact that V3's defining contributions (motion
boundaries, depth from motion, kinetic form) are **lateralization-neutral** at the domain level — the lateralization is in **how strongly**
each domain is engaged, not in **which domains are carried**.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), left — **indirect, via
          V2 (principal) and V1 (indirect)**
            **V3's dominant input is from V2, not directly from the
            LGN or V1.** The LGN → V1 → V2 → V3 pathway is the
            **obligate relay** for V3's visual input. V3 has **no
            direct LGN projections** and **no direct V1
            projections** — the relay through V2 is obligate.
        → pulvinar (modulatory, **stronger to V3 than to V1**)
            The pulvinar sends a stronger modulatory projection to
            V3 than to V1, participating in the cortico-thalamo-
            cortical loops that support visual attention and
            visual short-term memory.

    cortical afferents
        → V2, left
            **V3's principal cortical afferent.** The V2 → V3
            projection carries the **thick-stripe** (motion) and
            **thin-stripe** (color/form) signals that V3
            elaborates into motion boundaries, kinetic form, and
            shape-from-motion.

    cortical efferents — **the two-pathway output (V3d → MT/V5,
    V3v → V4)**
        → MT/V5, left (via **V3d**) — **forward reference**
            The **V3d → MT/V5 relay** carries the **motion-
            boundary** and **motion-in-depth** signal forward to
            the motion area. **On the left, this pathway
            contributes to right-hemifield motion perception at a
            lower weighting than the right V3d → right MT/V5
            pathway.**
        → V4, left (via **V3v**)
            The **V3v → V4 relay** carries the **kinetic
            boundaries**, **shape-from-motion**, **shape-from-
            shading**, and **shape-from-texture** signals forward
            to V4. **On the left, this pathway feeds the left
            V4 → LOC → left VWFA (reading) pathway** — the left
            V3v is the **third stage of the left reading
            pathway**.
        → LOC, left (via **V3v** and **V4**)
            V3v's output reaches the LOC via V4, contributing to
            the **object-recognition** stage of the ventral
            stream. **On the left, the V3v → V4 → LOC pathway
            terminates at the left VWFA (reading)**.
        → V3A, left — **forward reference**
            V3d's output reaches V3A (the motion-in-depth and
            spatial-attention area) en route to MT/V5. **On the
            left, V3A's contribution is present but weaker than
            the right's.**

    callosal connections
        → right V3
            The callosal fibers connect the left V3 to the right
            V3 across the occipital midline, supporting **the
            fusion of the two hemifields** at the V3 stage.

    attentional feedback
        → frontal eye fields (BA 8), left
            The FEF sends **top-down attentional gain** to V3,
            modulating V3's responsiveness to behaviourally
            relevant stimuli. **On the left, the FEF → V3
            projection is present but weaker than the right
            FEF → right V3 projection.**
        → dorsolateral prefrontal cortex (BA 9 / BA 46), left
            The DLPFC sends top-down attentional and working-memory
            signals to V3.
        → intraparietal sulcus, left
            The IPS sends dorsal-attention-network signals to V3,
            supporting **spatial attention** in the RIGHT visual
            hemifield. **On the left, the IPS → V3 projection is
            present but weaker than the right's.**

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in three respects:
(a) the **V3v → V4 → LOC → left VWFA pathway** is the **left
reading pathway**, and it is the **stronger** of the two V3
efferents on the left;
(b) the **V3d → MT/V5 pathway** is present but weaker than the
right's (the right V3d → right MT/V5 pathway is the dominant motion
substrate);
(c) the FEF, IPS, and DLPFC → V3 feedback is present but weaker than
on the right (the right dorsal attention network dominates).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_v3_right_quadrantic_visual_field_defect
        **This is the left V3 anchor for the field defect.** V3's
        lesions produce **partial** field defects — a **right
        quadrantic** or **sectoranopic** defect — just as V2's
        do. The V3-specific field defect is often **more
        quadrantic** than V2's, because V3's upper and lower
        field banks are **widely separated** (the V2/V3 border
        is at the fundus of the calcarine sulcus), so a lesion
        in V3 is more likely to affect the upper **or** lower
        quadrant than to produce a complete hemianopia. **Often
        with macular sparing** (the fovea is fed by V1's dual
        blood supply).

    left_v3_motion_boundary_deficit
        **V3d's most distinctive clinical signature.** Left V3d
        lesions can produce **motion-boundary deficits** — the
        patient can perceive the motion of **individual** moving
        objects but cannot perceive the **boundary** defined by
        motion (e.g., a figure defined only by the relative
        motion of its parts against the background). **This is a
        V3d-specific deficit** that is **distinct** from
        akinetopsia (V5/MT+ lesion) and from motion-agnosia
        (higher-order deficit). **On the left, the motion-
        boundary deficit is present but milder than the right
        equivalent** — the right V3d's motion-boundary
        processing is the dominant substrate.

    left_v3_depth_from_motion_deficit
        **V3d's second distinctive clinical signature.** Left V3d
        lesions can produce **impaired depth-from-motion** — the
        patient cannot perceive the **three-dimensional shape**
        of an object from its motion (e.g., a rotating object
        appears as a flat pattern rather than a solid form). This
        is distinct from **stereopsis** (which V3v supports via
        disparity). **On the left, the depth-from-motion deficit
        is present but milder than the right equivalent.**

    left_v3_local_form_from_motion_deficit
        **V3v's most left-lateralized clinical signature.** Left
        V3v lesions can produce **local-level form-from-motion
        deficits** — the patient cannot perceive **fine local
        contours** defined by motion (e.g., the boundary of a
        small moving figure against a moving background).
        Navon's local-precedence asymmetry is the framework: the
        left V3v is weighted toward local / featural form-from-
        motion, and left V3v lesions produce the complementary
        deficit to the right V3v's global form-from-motion
        deficit.

    left_v3_hemianopic_alexia_right
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **right homonymous field defect** — is a
        recognized clinical entity after left V3 lesions that
        produce a partial right field defect. **The left V3v's
        contribution to the left reading pathway** (V3v → V4 →
        LOC → left VWFA) means that left V3v lesions can
        **also** produce a **direct reading deficit** — beyond
        the field-defect-induced hemianopic alexia — because the
        V3v → V4 form pathway is degraded. **The left V3 lesion
        produces a more specific reading deficit than the left
        V2 lesion** because V3v is closer to the reading
        endpoint.

    left_v3_stereopsis_deficit
        **V3v's clinical signature via disparity.** Left V3v
        lesions can produce **impaired stereopsis** — reduced
        ability to perceive depth from binocular disparity,
        especially for **stereo-defined form**. This is distinct
        from **V1's or V2's stereopsis deficits** (which are
        broader) because V3v's disparity neurons are **more
        selective** and support **higher-order stereo shape**.
        **On the left, the stereopsis deficit is present but is
        not the left's dominant V3 domain emphasis** — the
        left V3's dominant domains are `form_and_object_
        perception` and `spatial_localization`, not `binocular_
        vision`.

    left_v3_motion_defined_form_agnosia
        **A higher-order V3d/V3v interaction deficit.** Left V3
        lesions can produce **motion-defined form agnosia** — the
        patient cannot perceive **objects** or **letters** that
        are defined only by motion (e.g., a letter made of moving
        dots). **This is a "kinetic form" deficit** that
        involves **both** V3d's motion-boundary processing and
        V3v's form-from-motion processing. **On the left, the
        deficit has a language-linked component** — the patient
        may perceive kinetic form in isolation but cannot use it
        for **reading or naming**.

    left_v3_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct**
        involving V3 produces a **right quadrantic defect**
        (from V3) on top of a **right homonymous hemianopia**
        (from V1) and, if the splenium is involved, **alexia
        without agraphia**. **The V3-specific contribution is
        the motion-boundary and depth-from-motion deficits on
        top of the field defect** — these are the **V3-specific
        signatures** that distinguish a V3-involved infarct from
        a V1-only one.

    left_v3_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **V1, V2, AND V3**. **The V3
        contribution is the propagation of the aura into
        motion-defined and form-defined features** — the patient
        may see **kinetic fortifications** (moving zigzags) or
        **motion phosphenes** in addition to the color and
        static form features of V1 and V2. **This anchor is
        hemisphere-invariant.**

    left_v3_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **V1, V2, OR V3**. **V3 auras** are typically
        **more complex than V2 auras** — the patient may see
        **kinetic shapes, motion-defined forms, or stereo
        phenomena** in addition to elementary shapes and
        fortifications. **Left V3 auras** project to the
        **right visual field** and can be preceded or
        accompanied by **visual field defects** or **motion-
        boundary deficits** that persist after the seizure.

    left_v3_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1, V2, AND V3 bilaterally**
        in later stages, but early PCA affects the **dorsal and
        ventral association cortices** (V3A, V4, V5/MT+, LOC)
        more than V3 proper. **Left V3** is part of the
        substrate of the **progressive ventral stream
        dysfunction** that produces **progressive reading
        deficits** in later-stage PCA.

    left_v3_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects** from **bilateral occipital
        involvement**. **The V3 contribution** is the
        **extrastriate involvement** that produces **kinetic and
        motion-defined hallucinations** and **quadrantic defects**
        (V3 partial loss). **The syndrome is reversible** in
        most cases.

**The V3-specific clinical anchors** — `left_v3_motion_boundary_
deficit`, `left_v3_depth_from_motion_deficit`,
`left_v3_local_form_from_motion_deficit`,
`left_v3_stereopsis_deficit`, and
`left_v3_motion_defined_form_agnosia` — are the **most distinctive
V3 anchors**. They are **narrower** than the BA 18 anchors
(because V3 is a subset of BA 18) and **narrower** than the V2
anchors (because V3 processes **elaborated** motion and form
signals, not the low-level features that V2 processes). They are the
**V3-specific signatures** that distinguish a V3 lesion from a V2 or
V4 lesion.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, PRES, and occipital infarct — are **documented
identically in both siblings**, with the side-appropriate field
label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..cortex  (parent)
    The left occipital functional / V-numbered parent.

..primary_visual_cortex  (V1)
    **Distant caudal neighbour** via V2; no direct adjacency.

..v2
    **Caudal neighbour** via the **V2/V3 border** — the horizontal-
    meridian boundary at the fundus of the calcarine sulcus. **V2
    and V3 share BA 18.** V2 is V3's principal cortical afferent.

..v4
    **Ventral rostral neighbour**. V3v's output reaches V4 via the
    **V3v → V4 relay**.

...brodmann_areas.brodmann_area_18
    The **cytoarchitectonic counterpart — partial correspondence,
    not identity.** BA 18 spans **V2 and V3**. V3 is one of the
    two V areas that share BA 18.

...brodmann_areas.brodmann_area_19
    The **second cytoarchitectonic counterpart — partial
    correspondence, not identity.** BA 19 spans **V3, V4, V3A,
    V3B, V5/MT+, LOC**. V3's **lateral extent** crosses the
    BA 18 / BA 19 border, which is why V3's BA correlate is
    `(18, 19)` — the **only two-BA correlate** in the V
    hierarchy.

...cuneus
    The medial-surface gyral landmark. **On the left, the
    cuneus's V3 lower-field representation carries the lower
    RIGHT visual field.** V3 aligns with V1's bank assignment
    (double mirror-flip).

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus carries the **V3 upper-field representation
    of the upper** contralateral visual field. **On the left,
    the upper RIGHT field.**

...sulci.calcarine_sulcus
    The **reference landmark** for the V2/V3 border. The fundus
    of the calcarine sulcus carries the **horizontal meridian**,
    which is V3's most reliable retinotopic landmark.

...sulci.lunate_sulcus
    The inconstant lateral-surface landmark for the V1/V2 border
    (when present). **Not the V2/V3 border** — the V2/V3 border
    is retinotopic, not sulcal.

...sulci.transverse_occipital_sulcus
    The dorsal-surface landmark for the V3A / V3B territory. **Not
    the V2/V3 border** — the V2/V3 border is retinotopic.

..cortex.temporal
    The **ventral stream** continues from V3v (via V4 and the
    LOC) into the temporal lobe. **On the left, the ventral
    stream terminates in the left VWFA** (the reading area), and
    the left V3v is the **third stage** of this pathway. The
    temporal package must declare the left V3v as a source of
    its visual input via the ventral stream, and must note the
    **left-lateralized VWFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from V3d (via MT/V5) into
    the parietal lobe. **On the left, the dorsal stream supports
    right-hemifield spatial attention** at a lower weighting
    than the right's.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V3.

..cortex.cingulate  — indirect
    No direct cingulate → V3 projection.

..cortex.insular  — indirect
    No direct insular → V3 projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the **indirect** source of V3's input via the
    V1 → V2 → V3 relay. **V3 has no direct LGN projection.**

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V3
    than to V1**, participating in the cortico-thalamo-cortical
    loops that support visual attention and visual short-term
    memory.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from V3v (via V4 and the LOC)
    to the perirhinal, entorhinal, and parahippocampal cortices.
    **The left V3v is the third stage** of the occipito-
    temporal-hippocampal pathway.

../../right/cortex/occipital/cortex/v3
    The right-hemisphere homologue. Structural fields (V-number,
    two-BA correlate (18, 19), V3d/V3v distinction, mirror-flip
    retinotopy, V2/V3 and V3/V4 borders, double-BA span,
    FUNCTIONAL_DOMAINS set, forward-declaration caveat text) MUST
    be byte-identical. Functional emphasis and clinical
    significance diverge — the right V3 processes the **LEFT**
    visual hemifield, is weighted toward the **spatial-localization
    and motion-boundary** aspect, and its V3v output feeds the
    **right V4 → LOC → right FFA** (face) pathway rather than the
    left V4 → LOC → left VWFA (reading) pathway.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "v3"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    V_NUMBER            = "V3"
    ALTERNATE_NAMES     = ("tertiary_visual_cortex",
                           "v3",
                           "brodmann_area_18_and_19_double_partial")
        # **Note "double_partial"** — V3 is the **only V area**
        # whose BA correlate spans **two** BAs (18 and 19),
        # partially shared with V2 on the BA 18 side and with
        # V4/V3A/V3B/V5/MT+/LOC on the BA 19 side.

    ARCHITECTONIC_SIGNATURES = (
        "dysgranular_extrastriate_cortex",
        "retinotopic_boundary_v2_v3_horizontal_meridian",
        "no_single_architectonic_signature",
    )
        # **Three signatures**: dysgranular cytoarchitecture, the
        # **retinotopic** V2/V3 border (horizontal meridian, not
        # architectonic), and the **absence of a single defining
        # architectonic signature** (unlike V1's stria of Gennari
        # and V2's CO stripes).

    BRODMANN_CORRELATES = (18, 19)
        # **Two BAs** — the **only two-BA correlate** in the V
        # hierarchy. **V3 appears on both sides of the
        # BA↔V crosswalk.**

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** V3 is unique to the occipital
        # lobe.

    RETINOTOPIC_MAP     = "double_mirror_flip_of_V2_aligns_with_V1_bank_assignment"
        # The map's structure: V3 is a mirror-flip of V2 across
        # the horizontal-meridian V2/V3 border at the fundus of
        # the calcarine sulcus. Because V2 is a mirror-flip of
        # V1, V3's bank assignment **aligns with V1's** (upper
        # field on lingual gyrus, lower field on cuneus). **On
        # the left, the represented hemifield is the RIGHT
        # hemifield.**

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** — left V3
        # processes the RIGHT hemifield.

    FUNCTIONAL_DOMAINS  = (
                              "spatial_localization",
                              "form_and_object_perception",
                              "binocular_vision",
                              # **Three domains — same set on
                              # both hemispheres** (unlike V1
                              # and V2, which have four on the
                              # right and three on the left).
                              # **This is the first V area in the
                              # hierarchy whose FUNCTIONAL_
                              # DOMAINS set is hemisphere-
                              # invariant.** Left-right
                              # differences are emphasis-only.
                              # NOTE: motion_perception is
                              # EXCLUDED (MT/V5's domain; V3d
                              # feeds it via the V3d → MT/V5
                              # relay but does not perform it).
                              # NOTE: color_vision is EXCLUDED
                              # (V4's domain; V3v feeds it via
                              # the V3v → V4 relay but does not
                              # perform it).
                              # NOTE: primary_visual_processing
                              # and primary_visual_processing_
                              # secondary are EXCLUDED (V1's
                              # and V2's domains — V3 processes
                              # elaborated signals, not low-
                              # level features).
                              # NOTE: visual_attention is
                              # EXCLUDED as a primary domain.
                              # NOTE: visual_word_processing is
                              # EXCLUDED (V3v is the third
                              # stage of the left reading
                              # pathway, not the operation).
                              # NOTE: face_processing and
                              # global_visual_processing are
                              # EXCLUDED (right-lateralized; not
                              # instantiated on the left V3).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "spatial_localization":
                                  "motion_boundary_and_depth_from_"
                                  "motion_weaker_than_right_via_"
                                  "v3d_to_left_mt_v5",
                              "form_and_object_perception":
                                  "dynamic_form_and_shape_from_"
                                  "motion_feeding_left_v4_loc_left_"
                                  "vwfa_reading_pathway",
                              "binocular_vision":
                                  "stereo_depth_and_shape_from_"
                                  "disparity_v3v_right_hemifield",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_v3_right_quadrantic_visual_"
                              "field_defect",
                              "left_v3_motion_boundary_deficit",
                              "left_v3_depth_from_motion_"
                              "deficit",
                              "left_v3_local_form_from_motion_"
                              "deficit",
                              "left_v3_hemianopic_alexia_right",
                              "left_v3_stereopsis_deficit",
                              "left_v3_motion_defined_form_"
                              "agnosia",
                              "left_v3_occipital_infarct_pca_"
                              "territory",
                              "left_v3_migraine_visual_aura",
                              "left_v3_occipital_epilepsy_"
                              "visual_auras",
                              "left_v3_posterior_cortical_"
                              "atrophy",
                              "left_v3_pres_visual_symptoms",
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
   ``..cortex``. V3d's dorsal output reaches V3A, and V3A
   continues the dorsal motion and spatial-attention pathway.
   **On the right, V3A is a core node of the right dorsal
   attention network**, and creating the V3A package is the most
   urgent future resolution for the dorsal stream. Until then,
   V3A is a forward reference recorded in the parent's
   ``FORWARD_REFERENCE_V_AREAS`` tuple.

2. **MT/V5 is a forward reference** — not yet a package under
   ``..cortex``. V3d's principal output reaches MT/V5, and
   **conscious motion perception emerges in MT/V5**, not in V3.
   The V3d → MT/V5 relay is a **cross-package dependency** that
   is currently unresolved. **On the right, MT/V5 is the
   dominant motion hemisphere**, and creating the MT/V5 package
   is the second most urgent resolution.

**Both forward references must be resolved before V3's clinical
anchors are finalised** — the `motion_boundary_deficit` and
`depth_from_motion_deficit` anchors describe V3-specific processing
deficits, but **the conscious motion perception deficits
(akinetopsia) are MT/V5-specific** and live in the MT/V5 package.
Until MT/V5 is resolved, the V3 clinical anchors describe the
**sub-MT/V5 processing deficits only**.

**Both forward references are byte-identical to the left sibling's**
— they are properties of the V-area hierarchy, not of the hemisphere.

**All forward-declaration caveat text is byte-identical to the left
sibling's**, except for the emphasis note on the right
("on the right, V3A and MT/V5 are the dominant dorsal-stream
substrates, and creating their packages is more urgent than on the
left") — this right-specific emphasis is required by the right's
functional dominance in motion and attention.

--------------------------------------------------------------------------------
PROMOTION RULE (when a V sub-field becomes a package)
--------------------------------------------------------------------------------

V3 is **the most likely V area to be split in the current tree** —
the V3d / V3v distinction is well-established in the retinotopic
literature, and some parcellations already treat them as separate
areas (V3d and V3v, or V3 and VP). If a future parcellation
promotes this split, the promotion takes this form:

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
  4. Mirror the promotion on the right side in the same commit.

**The V3d / V3v split is a legitimate retinotopic subdivision** (not
an architectonic one — V3d and V3v have similar cytoarchitectures
but different retinotopic and functional signatures). **The split
preserves the two-BA span**: V3d and V3v both inherit the parent's
`(18, 19)` `BRODMANN_CORRELATES`, because the BA 18 / BA 19 border
sits **within** V3, and both V3d and V3v cross it.

**The split requires a joint revision of BA 18's and BA 19's
`V_AREA_CORRELATE` entries.** If V3 is split, BA 18's correlate
becomes `("v2", "v3d", "v3v")` (or `("v2", "v3")` if the BA
labeling convention treats the split as a refinement), and BA 19's
correlate becomes `("v3d", "v3v", "v4", "V3A", "V3B", "V5_MT_plus",
"LOC")`. **The exact form depends on the labeling convention, which
must be decided hemisphere-invariantly** and applied in the same
commit as the split, in both hemispheres.

**On the left, the V3v component is the dominant ventral-stream
contributor** (feeding the left V4 → LOC → left VWFA reading
pathway), and the V3d component is a **weaker dorsal-stream
contributor** than its right counterpart. On the right, the V3d
component is the **dominant dorsal-stream contributor**, and the V3v
component feeds the right FFA (face) pathway.

**No split should be performed while V3A and MT/V5 are unresolved**
— the split's main downstream targets are V3A and MT/V5 (for V3d)
and V4 (for V3v), and creating them first establishes the complete
V3 downstream context.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../v3``:

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
                                     structure, aligning V3's
                                     bank assignment with V1's
        FUNCTIONAL_DOMAINS set       the same three domains
                                     (spatial_localization,
                                     form_and_object_perception,
                                     binocular_vision) — **the
                                     first V area whose domain
                                     set is hemisphere-invariant**
        Bounding / overlapping territories
        V-to-neighbour adjacency
        CONNECTIVITY                 same bundle names (V2 → V3,
                                     V3v → V4, V3d → MT/V5)
        The forward-declaration caveat text (byte-identical,
                                     with the right-specific
                                     emphasis note documented)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — left V3 processes
                               the RIGHT hemifield; right V3
                               processes the LEFT hemifield.
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        DOMAIN_EMPHASIS        left: spatial_localization is
                               "motion_boundary_and_depth_from_
                               motion_weaker_than_right_via_v3d_
                               to_left_mt_v5"; form_and_object_
                               perception is "dynamic_form_and_
                               shape_from_motion_feeding_left_v4_
                               loc_left_vwfa_reading_pathway";
                               binocular_vision is "stereo_depth_
                               and_shape_from_disparity_v3v_
                               right_hemifield".
                               right: spatial_localization is
                               "motion_boundary_and_depth_from_
                               motion_dominant_via_v3d_to_right_
                               mt_v5"; form_and_object_perception
                               is "dynamic_form_and_shape_from_
                               motion_feeding_right_v4_loc_right_
                               ffa_face_pathway"; binocular_vision
                               is "stereo_depth_and_shape_from_
                               disparity_v3v_left_hemifield".
        CONNECTIVITY           same bundle names; left: the
                               V3v → V4 → LOC → left VWFA
                               pathway is the **dominant**
                               V3 efferent; the V3d → MT/V5
                               pathway is present but weaker.
                               right: the V3d → MT/V5 pathway
                               is the **dominant** V3 efferent;
                               the V3v → V4 → LOC → right FFA
                               pathway is present but weighted
                               toward the face endpoint.
        CLINICAL_ANCHORS       left: twelve anchors (right
                               quadrantic visual field defect,
                               motion-boundary deficit,
                               depth-from-motion deficit, **local**
                               form-from-motion deficit,
                               hemianopic alexia (right),
                               stereopsis deficit, motion-defined
                               form agnosia, left occipital
                               infarct, migraine aura, occipital
                               epilepsy, PCA, PRES).
                               right: twelve anchors (left
                               quadrantic visual field defect,
                               motion-boundary deficit (more
                               severe), depth-from-motion deficit
                               (more severe), **global**
                               form-from-motion deficit, **left
                               hemifield neglect contribution**,
                               hemianopic alexia (left, milder),
                               stereopsis deficit, motion-defined
                               form agnosia, right occipital
                               infarct, migraine aura, occipital
                               epilepsy, PCA (Benson syndrome),
                               PRES).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same V3, the same V3d / V3v
distinction, the same double-BA span, and the same three-domain set
— but the *represented hemifield* is **flipped**.

**The FUNCTIONAL_DOMAINS set is IDENTICAL across hemispheres.** This
is the **first V area in the hierarchy whose domain set is
hemisphere-invariant** (V1 and V2 both have four on the right and
three on the left). **The left-right differences are emphasis-only**
— V3's defining contributions (motion boundaries, depth from motion,
kinetic form) are **lateralization-neutral** at the domain level.

**The emphasis asymmetry is the second sharpest entry.** Both
hemispheres carry `spatial_localization`, `form_and_object_
perception`, and `binocular_vision` — but the **left** V3's
`spatial_localization` is **weaker than the right's** (the right V3d
is the dominant motion-in-space substrate), and the **left** V3's
`form_and_object_perception` is **weighted toward the ventral-stream
reading endpoint** (V3v → V4 → LOC → left VWFA). The right V3's
`form_and_object_perception` is weighted toward the face endpoint
(V3v → V4 → LOC → right FFA), and the right V3's
`spatial_localization` is **dominant**.

**The V3d / V3v split is a shared structural fact.** Both
hemispheres carry the same split, and both V3d and V3v inherit the
same `(18, 19)` BA correlate. The **relative weighting** of V3d vs
V3v differs — **left V3v is dominant**, **right V3d is dominant**
— but the structural fact of the split is hemisphere-invariant.

**The two-BA correlate (18, 19) is byte-identical on both sides.**
It is a property of V3's position at the BA 18 / BA 19 border, not
of the hemisphere.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "v3".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V3".
[ ] ALTERNATE_NAMES includes "tertiary_visual_cortex", "v3", and
    **"brodmann_area_18_and_19_double_partial"** — the **double
    partial correspondence** (V3 spans two BAs).
[ ] ARCHITECTONIC_SIGNATURES includes the **three** signatures:
    dysgranular extrastriate cortex, **retinotopic V2/V3 border**,
    and **no single architectonic signature**.
[ ] BRODMANN_CORRELATES is exactly ``(18, 19)`` — **two BAs, the
    only two-BA correlate in the V hierarchy**.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **double mirror-flip** structure:
    - V3 is a mirror-flip of V2 across the horizontal-meridian
      V2/V3 border at the fundus of the calcarine sulcus
    - Because V2 is a mirror-flip of V1, **V3 aligns with V1's
      bank assignment** (upper field on lingual gyrus, lower
      field on cuneus)
    - **represented hemifield = RIGHT hemifield on the left side**
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] FUNCTIONAL_DOMAINS contains **three** domains:
    - spatial_localization
    - form_and_object_perception
    - binocular_vision
[ ] **The FUNCTIONAL_DOMAINS set is verified to be IDENTICAL across
    hemispheres** — the **first V area with a hemisphere-invariant
    domain set**.
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (MT/V5's
    domain; V3d feeds it via the V3d → MT/V5 relay but does not
    perform it).
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision (V4's domain;
    V3v feeds it via the V3v → V4 relay but does not perform it).
[ ] FUNCTIONAL_DOMAINS **excludes** primary_visual_processing and
    primary_visual_processing_secondary (V1's and V2's domains).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a primary
    domain.
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing (V3v
    is the third stage of the left reading pathway, not the
    operation).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and
    global_visual_processing (right-lateralized).
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis** per
    domain:
    - spatial_localization → motion_boundary_and_depth_from_
      motion_weaker_than_right_via_v3d_to_left_mt_v5
    - form_and_object_perception → dynamic_form_and_shape_from_
      motion_feeding_left_v4_loc_left_vwfa_reading_pathway
    - binocular_vision → stereo_depth_and_shape_from_disparity_
      v3v_right_hemifield
[ ] CONNECTIVITY documents:
    - V2 → V3 principal cortical afferent (the obligate relay;
      V3 has **no direct LGN and no direct V1 projections**)
    - Pulvinar afferent (stronger to V3 than to V1)
    - **V3d → MT/V5 relay** (motion-boundary, motion-in-depth;
      **forward reference**; present but weaker than the right's)
    - **V3v → V4 relay** (kinetic form, shape-from-motion,
      shape-from-shading; feeds the left V4 → LOC → left VWFA
      reading pathway)
    - **V3v → LOC relay** (via V4, object-recognition endpoint)
    - V3d → V3A (forward reference; motion-in-depth and spatial
      attention)
    - Callosal connections to right V3
    - Attentional feedback from left FEF, left DLPFC, left IPS
      (present but weaker than the right's)
[ ] CLINICAL_ANCHORS contains the twelve left-specific anchors:
    - left_v3_right_quadrantic_visual_field_defect
    - left_v3_motion_boundary_deficit
    - left_v3_depth_from_motion_deficit
    - left_v3_local_form_from_motion_deficit
    - left_v3_hemianopic_alexia_right
    - left_v3_stereopsis_deficit
    - left_v3_motion_defined_form_agnosia
    - left_v3_occipital_infarct_pca_territory
    - left_v3_migraine_visual_aura
    - left_v3_occipital_epilepsy_visual_auras
    - left_v3_posterior_cortical_atrophy
    - left_v3_pres_visual_symptoms
[ ] The **V3-specific anchors** — motion-boundary deficit,
    depth-from-motion deficit, local form-from-motion deficit,
    stereopsis deficit, motion-defined form agnosia — are
    documented as **narrower** than the BA 18 anchors (V3 is a
    subset of BA 18) and **narrower** than the V2 anchors (V3
    processes elaborated motion and form, not low-level
    features).
[ ] The **local form-from-motion deficit** is documented as the
    left-lateralized form-from-motion anchor — the mirror of
    the right's global deficit.
[ ] **The two-BA span (18, 19)** is documented as **V3's defining
    structural fact** — the only V area whose cytoarchitectonic
    correlate spans two BAs.
[ ] The **V3d / V3v split** is documented as the **defining
    within-V3 structural distinction**, with the different
    functional roles and downstream targets (V3d → MT/V5,
    V3v → V4).
[ ] The **double mirror-flip** is documented — V3 aligns with
    V1's bank assignment (upper field on lingual gyrus, lower
    field on cuneus).
[ ] The **V2/V3 horizontal-meridian border at the fundus of the
    calcarine sulcus** is documented as V3's most reliable
    retinotopic landmark.
[ ] The **V3v → V4 → LOC → left VWFA** pathway is documented as
    the left reading pathway, with the V3v being its **third
    stage** after V1 and V2.
[ ] The **V3d → MT/V5** pathway is documented as the left's
    weaker dorsal-stream contribution, distinct from the
    right's dominant motion substrate.
[ ] **The two forward references — V3A and MT/V5** — are
    documented, and the **resolution rule** is recorded. Both
    are byte-identical to the left sibling's forward-reference
    list, and the right's emphasis note ("V3A and MT/V5 are the
    dominant dorsal-stream substrates, and creating their
    packages is more urgent than on the left") is present.
[ ] No SUBDIVISIONS promotion is performed while V3A and MT/V5
    are unresolved.
[ ] The **promotion rule for V3 → V3d + V3v** is documented, with
    the joint BA 18 / BA 19 update requirement, the
    hemisphere-invariant labeling convention, and the
    downstream V4 / MT/V5 prerequisites.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, **FUNCTIONAL_DOMAINS set**, forward-declaration
    caveat text) match the left sibling; VISUAL_HEMIFIELD,
    DOMAIN_EMPHASIS (spatial-localization weighting and
    form-processing endpoint), CONNECTIVITY emphasis (left
    V3v-dominant, right V3d-dominant), and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left V3
    carries "right_hemifield" in its DOMAIN_EMPHASIS entries and
    RETINOTOPIC_MAP; the right V3 carries "left_hemifield."
[ ] **The FUNCTIONAL_DOMAINS set is verified to be IDENTICAL
    across hemispheres** — V3 is the first V area with a
    hemisphere-invariant domain set.
[ ] **The emphasis asymmetry is verified**: the left V3's
    spatial_localization is "weaker than right"; the right V3's
    is "dominant."
[ ] **The V3d / V3v split is verified as shared** — both
    hemispheres have the same split, and the left V3v / right
    V3d dominance asymmetry is captured in the CONNECTIVITY and
    DOMAIN_EMPHASIS entries.
[ ] **The double-BA span is verified**: BRODMANN_CORRELATES is
    `(18, 19)` and is byte-identical to the right sibling's.
[ ] Any downstream code querying "what does the left V3 see?"
    must receive "the RIGHT visual hemifield."
[ ] Any downstream code querying "what is V3?" must receive
    "the tertiary visual cortex / V3 / part of BA 18 AND part
    of BA 19" — the **double partial correspondence** is
    enforced.
[ ] Any downstream code querying "which V area carries
    spatial_localization?" must receive "V3 (as the only
    V1–V4 area with it), plus V3A and V5/MT+ (as forward
    references)."
[ ] Any downstream code querying "which V area carries
    motion_perception?" must receive "V5/MT+ (not V3) — V3d
    feeds it but does not perform it."
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** V1 → V2 → V3v → V4 → LOC →
    left VWFA chain — the left V3v is the third stage.
[ ] Any downstream code assigning the right face pathway must
    route through the **right** V1 → V2 → V3v → V4 → LOC →
    right FFA chain.
[ ] Any downstream code assigning motion-boundary or
    depth-from-motion processing must route through the **V3d →
    MT/V5** chain — the V3d is the motion-boundary relay, not
    the motion-perception operation itself.
[ ] Any downstream code assigning shape-from-motion or kinetic
    form must route through the **V3v → V4** chain — the V3v is
    the form-from-motion relay, not the form-recognition
    operation itself.
[ ] Any downstream code querying "is V3's FUNCTIONAL_DOMAINS
    set the same on both hemispheres?" must receive "yes — V3
    is the first V area with a hemisphere-invariant domain
    set; only the emphasis differs."
"""