"""
Secondary Visual Cortex (V2) — Left Hemisphere
===============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── v2   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the left
hemisphere's **V2** — the **secondary visual cortex**, the first
extrastriate area, and the immediate downstream target of V1. It is
the **first step of the extrastriate hierarchy** and the territory in
which the visual signal is **first split** into the **three parallel
output streams** that will feed the ventral (object/color), dorsal
(motion), and inferotemporal (form) pathways.

Parent: ``..cortex`` (left occipital functional / V-numbered parent)
— sibling to V1, V3, V4. **Sibling — not parent —** of
``...brodmann_areas/brodmann_area_18``, which sits at the
``..brodmann_areas`` parent level. The V2 / BA 18 relationship is
**partial correspondence, not nesting** — BA 18 spans **both** V2 and
V3, so neither V2 nor V3 is co-extensive with BA 18.

This package is the **structural mirror** of
``../../right/cortex/occipital/cortex/v2``. The V-number, the BA
correlate (18, shared with V3), the architectonic signature (V2 CO
stripes), the V1/V2 border, the retinotopic mirror-flip, and the
three-stripe output organization are identical on both sides; the
**functional emphasis** and **clinical significance** diverge — on
the left, V2's form-and-object contribution is weighted toward the
**local / featural** aspect, its **thin-stripe** output feeds the
**left V4 → LOC → left VWFA** (reading) pathway, and left V2 lesions
contribute to **local-level form processing deficits** and to the
**left reading deficit** when the downstream pathway is affected.

**The defining structural fact about V2** is that it is **the
first area in the visual hierarchy that is NOT co-extensive with a
single BA**. V1 is exactly BA 17; **V2 shares BA 18 with V3**. This
is why V2's `BRODMANN_CORRELATES` field is `(18,)` — the BA
correlate is correct, but it is **not exclusive** — and why
downstream code must not assume "BA 18 = V2" or "V2 = BA 18".
Instead:

    BA 18  =  V2 + V3  (the two V areas share the same BA)

This partial correspondence is the same as V3's (V3 ↔ BA 18 + BA
19), but in the opposite direction: V2 shares one BA with one other
V area, whereas V3 shares one BA (BA 18) with V2 and another (BA 19)
with V4, V3A, V3B, V5/MT+, and LOC. **V2 is the simpler case.**

--------------------------------------------------------------------------------
WHAT V2 IS
--------------------------------------------------------------------------------

V2 is the **secondary visual cortex** — the first extrastriate belt
area, immediately **surrounding V1** on both banks of the calcarine
sulcus and extending onto the lateral occipital surface. It is
bounded **caudally** by V1 (the V1/V2 border, architectonically
marked by the abrupt disappearance of the stria of Gennari) and
**rostrally** by V3 (the V2/V3 border, which represents the
**horizontal meridian** of the visual field). V2 does **not** have a
crisp architectonic boundary with V3 — the V2/V3 border is defined
**retinotopically**, by the horizontal-meridian representation, not
cytoarchitectonically.

**The architectonic signature** of V2 is the **cytochrome-oxidase
(CO) stripe pattern** — a characteristic alternating pattern of
**thin stripes**, **thick stripes**, and **pale (interstripe) bands**
visible on histochemical staining. The three stripe types have
**distinct anatomical connections and distinct functional roles**:

    Thin stripes        → project to V4 (color and form)
                          → part of the ventral stream
                          → **on the left, feed the left
                          V4 → LOC → left VWFA (reading) pathway**

    Thick stripes       → project to MT/V5 (motion)
                          → part of the dorsal stream
                          → **on the left, contribute to
                          right-hemifield motion perception at
                          a lower weighting than the right's**

    Pale stripes        → project to the inferotemporal cortex
    (interstripes)        (object form)
                          → part of the ventral stream
                          → **on the left, feed the left
                          object-recognition hierarchy (via V4
                          and the LOC)**

This **three-stripe output organization** is the **anatomical basis
of the V2 → three-stream split** — the single most important
functional fact about V2. It is why V2 is sometimes described as the
"gateway to the extrastriate cortex," and why lesions of V2 can
produce **combined** deficits that a lesion of V4 or MT/V5 alone
does not.

**The retinotopic organization of V2 is the mirror image of V1.**
This mirror-flip is the second defining structural fact:

    V1 upper field → V1 lower bank (lingual gyrus)
    V2 upper field → V2 **upper** bank (cuneus)

    V1 lower field → V1 upper bank (cuneus)
    V2 lower field → V2 **lower** bank (lingual gyrus)

The V2 map is **reversed** relative to V1 across the V1/V2 border,
which represents the **vertical meridian** in both areas. The
V2/V3 border represents the **horizontal meridian**, and V3 is a
second mirror-flip of V2. This **alternating mirror-image
organization** (V1 → V2 flipped, V2 → V3 flipped back) is the
defining feature of the retinotopic hierarchy, and it is why a
lesion in V2 can produce a **quadrantic** visual field defect rather
than a complete hemianopia — V2's upper-bank and lower-bank
representations are on **different** banks than V1's.

**Left-hemisphere specificity**: the left V2 processes the **RIGHT**
visual hemifield of both eyes. Its **thin-stripe** output feeds the
**left V4 → LOC → left VWFA** pathway — the left reading pathway —
and the left V2 is therefore the **second stage of the left reading
pathway** after V1. The left V2's **form-and-object perception** is
weighted toward the **local / featural** aspect (Navon's
local-precedence asymmetry, the mirror of the right's
global-precedence), and left V2 lesions produce **local-level form
processing deficits** that have no symmetric counterpart on the
right at the same weighting.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours (functional)
        caudally               V1 via the **V1/V2 border**
                               (architectonically crisp — the
                               stria of Gennari's abrupt
                               disappearance)
        rostrally              V3 via the **V2/V3 border**
                               (retinotopically defined — the
                               horizontal meridian)
        laterally              the lateral occipital gyrus (V2's
                               lateral extent)
        medially               the cuneus (upper bank) and the
                               lingual gyrus (lower bank)
        ventrally              the lingual gyrus / parahippocampal
                               region

    Functional overlays
        BA 18 — PARTIAL correspondence (V2 shares BA 18 with V3)
            V2 is **one of the two V areas** that span BA 18.
            Unlike V1 (which is exactly BA 17), V2 is **not**
            co-extensive with BA 18 — V3 shares the same BA. This
            is why V2's ``BRODMANN_CORRELATES`` is ``(18,)`` (the
            BA is correct) but is **not exclusive**.
        V2 CO stripes — the three-stripe organization
            The **thin / thick / pale** stripe pattern is V2's
            defining architectonic signature, and it is the
            anatomical basis of the **three-stream output**:
                thin → V4 (color/form, ventral)
                thick → MT/V5 (motion, dorsal)
                pale → IT (object form, ventral)
        cuneus — upper-bank V2
            The cuneus's lower margin carries the **V2 upper-bank
            representation of the lower** contralateral visual
            field. **On the left, the lower RIGHT field.**
            (Note the mirror-flip: **V1's upper field is on the
            LOWER bank, but V2's upper field is on the UPPER
            bank.**)
        lingual gyrus — lower-bank V2
            The lingual gyrus carries the **V2 lower-bank
            representation of the upper** contralateral visual
            field. **On the left, the upper RIGHT field.**
            (Forward reference in ``..gyri`` — not yet a package.)
        calcarine sulcus — reference landmark
            The V1/V2 border (the caudomedial boundary of V2) is
            adjacent to the calcarine sulcus.
        left visual word form area (VWFA) — downstream
        ventral-stream target
            **Left-specific overlay.** The left V2's **thin-stripe**
            output — via V4 and the LOC — terminates in the left
            VWFA. The V2 → V4 → LOC → VWFA pathway is the **left
            reading pathway**, and V2 is its **second stage** after
            V1.

**This field is structurally identical to the right sibling's** — the
architectonic neighbours, the V2 CO stripes, and the cuneus /
lingual-gyrus / calcarine overlays are the same on both sides. What
differs is the **visual hemifield** — the left V2 processes the
RIGHT hemifield, and the cuneus / lingual gyrus representations carry
the upper / lower RIGHT field on the left. The **left VWFA downstream
target** is a left-specific overlay that the right V2 package declares
as the **right FFA** (the face endpoint) instead.

--------------------------------------------------------------------------------
V-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    V1                                     **caudal neighbour** via the
                                           **V1/V2 border** — the
                                           architectonically crisp
                                           boundary marked by the
                                           abrupt disappearance of
                                           the stria of Gennari. The
                                           **vertical meridian** of
                                           the visual field is
                                           represented at this border.
                                           The V1 → V2 projection is
                                           V2's **principal cortical
                                           afferent** — the obligate
                                           relay through which V2
                                           receives its visual input.
    V3                                     **rostral neighbour** via the
                                           **V2/V3 border** — the
                                           retinotopically defined
                                           boundary at the
                                           **horizontal meridian**.
                                           V3 is a **second
                                           mirror-flip** of V2.
                                           **V2 and V3 share BA 18**
                                           — the only pair of V areas
                                           in the tree that share a
                                           BA without either being
                                           co-extensive with the BA.
    V4                                     **distant rostral neighbour**
                                           via V3; no direct
                                           adjacency, though **V2's
                                           thin stripes project
                                           directly to V4**
    BA 17                                  The **V1** BA — cross-
                                           referenced as the
                                           cytoarchitectonic
                                           counterpart of V2's
                                           caudal neighbour.
    BA 18                                  **Shared with V3** — V2 is
                                           **one of the two** V
                                           areas that span BA 18.
                                           The BA 18 / V2
                                           relationship is partial
                                           correspondence, not
                                           identity.
    cuneus (medial-surface gyrus)          carries the **V2 upper-bank**
                                           representation of the
                                           **lower** visual field
                                           (**lower RIGHT field on
                                           the left**). **Mirror-flip
                                           from V1: V1's upper field
                                           is on the lower bank.**
    lingual gyrus (medial-surface          carries the **V2 lower-bank**
    gyrus; forward reference in ..gyri)    representation of the
                                           **upper** visual field
                                           (**upper RIGHT field on
                                           the left**).
    calcarine sulcus (reference landmark)  the V1/V2 border is adjacent
                                           to the calcarine sulcus.
    lateral occipital gyrus                V2's lateral extent; part
                                           of the ventral stream's
                                           forward projections to
                                           the LOC.

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

V2 participates in **three** canonical occipital functional domains —
the **first V area in the hierarchy with fewer than four domains**.
V3's `spatial_localization` is **not** a V2 domain (it emerges in V3);
V4's `color_vision` is **not** a V2 domain (V2 **feeds** it via thin
stripes, but the conscious perception of color emerges in V4). The
emphasis is as follows:

    primary_visual_processing (secondary)          (left emphasis — PRIMARY)
        **This is V2's defining contribution.** The **second**
        cortical stage of vision, after V1. V2 adds **border
        ownership, texture, illusory contours, surface
        filling-in, and stereoscopic depth from binocular
        disparity** to the low-level features extracted by V1.
        On the left, V2 processes the **RIGHT visual hemifield**.

    binocular_vision                               (left emphasis — PRIMARY)
        V2's **binocular disparity neurons** — which are **more
        numerous and more selective than in V1** — support
        **fine stereoscopic depth perception** and **binocular
        fusion**. On the left, binocular vision in V2 combines
        the right-eye and left-eye inputs to the **RIGHT visual
        hemifield**.

    form_and_object_perception                     (left emphasis — SECONDARY)
        **This is V2's most left-lateralized contribution.**
        V2's **thin stripes** (color/form) and **pale stripes**
        (object form) contribute to the **early stages of form
        and object processing** that continue in V4 and the LOC.
        **On the left, the form-and-object contribution is
        weighted toward the LOCAL / FEATURAL aspect** — the left
        hemisphere's documented advantage in local processing
        (Navon's local-precedence asymmetry is the mirror of the
        right's global-precedence). **The left V2's thin-stripe
        output feeds the left V4 → LOC → left VWFA pathway** —
        the reading endpoint.

**Left-specific caveat on `spatial_localization`.** V2 is **not**
the spatial-localization area — that is **V3**, which is V2's
rostral neighbour and the second V area within BA 18. V2's **thick
stripes** project to MT/V5, but the **motion-boundary and
depth-from-motion** processing that underlies spatial localization
emerges in V3, not V2. `spatial_localization` is **omitted** from
the V2 `FUNCTIONAL_DOMAINS` tuple; it appears in V3 instead.

**Left-specific caveat on `color_vision`.** V2 is **not** the
color-vision area — that is V4, in BA 19. V2's **thin stripes
project to V4**, but the **conscious perception of color** emerges
in V4. `color_vision` is **omitted** from the V2 `FUNCTIONAL_DOMAINS`
tuple; it appears in V4 instead.

**Left-specific caveat on `motion_perception`.** V2 is **not** the
motion area — that is V5/MT+, a forward reference in BA 19. V2's
**thick stripes project to MT/V5**, but **conscious motion
perception** emerges in MT/V5. `motion_perception` is **omitted**
from the V2 `FUNCTIONAL_DOMAINS` tuple.

**Left-specific caveat on `visual_attention`.** V2 is a **target**
of top-down attentional modulation, but it is **not** an attentional
control area. `visual_attention` is **omitted**.

**Left-specific caveat on `visual_word_processing`.** V2 is the
**second stage** of the left reading pathway (V1 → V2 → V4 → LOC →
VWFA), but V2 itself does **not** perform word processing. `visual_
word_processing` is **omitted**.

**Left-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the left
V2 does **not** carry. `global_visual_processing` **begins at right
V2** (as the right BA 18 emphasis), not at left V2. Neither appears
in the left V2 `FUNCTIONAL_DOMAINS` tuple.

**Summary**: V2 carries **exactly three** functional domains —
`primary_visual_processing (secondary)`, `binocular_vision`, and
`form_and_object_perception`. This is **one fewer than BA 18**,
because BA 18's fourth domain (`spatial_localization`) is V3's, not
V2's. **The V2 / BA 18 relationship is a partial correspondence in
the functional domain set as well as in the cytoarchitectonic
correlate** — V2 is a subset of BA 18's territory and a subset of BA
18's domains.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), left — **indirect, via
          V1**
            **V2's dominant input is from V1, not directly from
            the LGN.** The LGN → V1 → V2 pathway is the **obligate
            relay** for V2's visual input.
        → LGN koniocellular pathway — **weak, direct**
            A **weak, direct LGN → V2 projection** exists via the
            koniocellular layers. It bypasses V1 and carries the
            **blue-yellow (S-cone) color signal**. This is part
            of the subcortical substrate that survives V1 lesions
            (blindsight for color).
        → pulvinar (modulatory, **stronger to V2 than to V1**)
            The pulvinar sends a stronger modulatory projection to
            V2 than to V1, participating in the cortico-thalamo-
            cortical loops that support visual attention and
            visual short-term memory.

    cortical afferents
        → V1, left
            **V2's principal cortical afferent.** The V1 → V2
            projection is the first step of the V1 → V2 → V3 →
            V4 hierarchy and carries the low-level features that
            V2 transforms into border ownership, texture, and
            surface representations.

    cortical efferents — **the three-stripe output**
        → V4, left (via **thin stripes**)
            The **V2 thin stripes** carry the color and form
            signal forward to V4. **On the left, this is the first
            step of the left V4 → LOC → left VWFA (reading)
            pathway.**
        → MT/V5, left (via **thick stripes**)
            The **V2 thick stripes** carry the motion and
            motion-boundary signal forward to MT/V5. On the left,
            this pathway contributes to right-hemifield motion
            perception at a **lower weighting** than the right's.
        → inferotemporal cortex, left (via **pale stripes**)
            The **V2 pale stripes** carry the object-form signal
            forward to the inferotemporal cortex, contributing to
            the ventral stream's object-recognition hierarchy.
        → V3, left
            V2 projects rostrally to V3 (the second step of the
            hierarchy), which continues the processing toward V4
            and MT/V5.

    callosal connections
        → right V2
            The callosal fibers connect the left V2 to the right
            V2 at the **vertical meridian** (the V1/V2 border) and
            across the upper and lower banks of the calcarine
            region. This callosal connection supports **the fusion
            of the two hemifields** at the V2 stage, and it is
            essential for the **continuity of visual perception
            across the vertical midline**.

    attentional feedback
        → frontal eye fields (BA 8), left
            The FEF sends **top-down attentional gain** to V2,
            modulating V2's responsiveness to behaviourally
            relevant stimuli.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), left
            The DLPFC sends top-down attentional and working-memory
            signals to V2, supporting **visual working memory**.
        → intraparietal sulcus, left
            The IPS sends dorsal-attention-network signals to V2,
            supporting **spatial attention** in the RIGHT visual
            hemifield.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in two respects:
(a) the **V2 thin stripes → V4 → LOC → left VWFA pathway** is the
**left reading pathway**;
(b) the **V2 thick stripes → MT/V5 pathway** carries the left's
contribution to right-hemifield motion perception at a **lower
weighting** than the right's.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_v2_right_quadrantic_visual_field_defect
        **This is the left V2 anchor par excellence.** Unlike V1,
        whose lesions produce a **complete** right homonymous
        hemianopia (V1 represents the entire contralateral
        hemifield), V2's lesions produce **partial** field
        defects — most characteristically a **right quadrantic**
        or **sectoranopic** defect. The classic V2-lesion field
        defect is a **right inferior quadrantic** field loss
        (from an upper-bank V2 lesion) or a **right superior
        quadrantic** field loss (from a lower-bank V2 lesion),
        **often with macular sparing** because the foveal
        representation at the occipital pole is fed by the
        dual-blood-supply V1 territory rather than V2 proper.

    left_v2_local_form_processing_deficit
        **On the left, V2's contribution to form and object
        processing is weighted toward the local / featural
        aspect.** Left V2 lesions can produce **local-level form
        processing deficits** — the patient may still perceive
        global shape but cannot resolve fine local features
        (Navon's local-precedence asymmetry is the framework).
        **This is a left-weighted anchor**; the right V2 lesion
        produces the complementary **global-level form
        processing deficit**.

    left_v2_hemianopic_alexia_right
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **right homonymous field defect** — is
        a recognized clinical entity after left V2 lesions that
        produce a partial right field defect. The patient's
        reading is slowed because they must make **large
        rightward saccades** to compensate for the missing right
        hemifield. **The left V2 lesion produces a milder alexia
        than a complete left V1 lesion** — the partial field
        defect is less disruptive than the complete hemianopia,
        and the reading network itself (left VWFA, left angular
        gyrus) is intact.

    left_v2_indirect_color_and_motion_deficits
        **V2's thin stripes project to V4 and its thick stripes
        project to MT/V5.** Left V2 lesions can produce **indirect
        color or motion processing deficits** — the V4 and MT/V5
        areas themselves are intact, but their input from V2 is
        degraded. The color deficit in a V2 lesion is typically
        **milder** than in a V4 lesion, and the motion deficit in
        a V2 lesion is typically **milder** than in a V5/MT+
        lesion. **Isolated achromatopsia (V4) or akinetopsia
        (V5/MT+) from a V2 lesion would be unexpected** — the
        deficit is a *processing* impairment, not a *perceptual
        absence*.

    left_v2_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** involving
        V2 produces a **right quadrantic or sectoranopic defect**
        (from V2) on top of a **right homonymous hemianopia**
        (from V1) and, if the splenium is involved, **alexia
        without agraphia** (from the left V1 + splenium
        disconnection). **The V2-specific contribution is the
        quadrantic extension of the field defect beyond the
        V1-only hemianopia.**

    left_v2_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **V1 AND V2**. **The V2 contribution
        is the propagation of the visual aura from V1's simple
        features (flashes) to V2's more complex features (the
        zigzag fortification lines)** — the classic fortification
        spectrum is a **V2 phenomenon**. **This anchor is
        hemisphere-invariant**, but the aura's field involvement
        is contralateral (right field on the left side).

    left_v2_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **V1 OR V2**. **V2 auras** are typically **more
        complex** than V1 auras — the patient may see **formed
        objects, recognizable scenes, or specific colors** in
        addition to elementary shapes. **Left V2 auras** project
        to the **right visual field** and can be preceded or
        accompanied by **visual field defects** that persist
        after the seizure.

    left_v2_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1 AND V2 bilaterally** in later
        stages. **Left V2** is part of the substrate of the
        **progressive ventral stream dysfunction** that produces
        **progressive reading deficits** in later-stage PCA.

    left_v2_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects** from **bilateral occipital
        involvement**. **The V2 contribution** is the
        **extrastriate involvement** that produces **visual
        hallucinations** (V2 hyperexcitability) and **quadrantic
        defects** (V2 partial loss). **The syndrome is reversible**
        in most cases.

**The V2-specific clinical anchors** — `left_v2_right_quadrantic_
visual_field_defect`, `left_v2_local_form_processing_deficit`,
`left_v2_hemianopic_alexia_right`, and
`left_v2_indirect_color_and_motion_deficits` — are the **mirror of
the left BA 18 anchors** with a narrower scope, because V2 is a
subset of BA 18. The BA 18 anchors that are **V3's** (`spatial_
localization`-related deficits, motion-boundary and
depth-from-motion deficits) are **not** V2 anchors and appear in the
V3 package instead.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, PRES, and occipital infarct — are **documented
identically in both siblings**, with the side-appropriate field
label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..cortex  (parent)
    The left occipital functional / V-numbered parent. This
    package's parent, source of the ``BA_TO_V_CROSSWALK``,
    ``V_TO_BA_CROSSWALK``, ``FORWARD_REFERENCE_V_AREAS``, and
    ``DOMAIN_COVERAGE`` registries.

..primary_visual_cortex  (V1)
    **Caudal neighbour** via the **V1/V2 border** — the
    architectonically crisp boundary marked by the stria of
    Gennari's abrupt disappearance. V1 is V2's principal cortical
    afferent.

..v3
    **Rostral neighbour** via the **V2/V3 border** — the
    retinotopically defined horizontal-meridian boundary. **V2 and
    V3 share BA 18** — the only pair of V areas in the tree that
    share a BA without either being co-extensive with it. V3
    carries the `spatial_localization` domain that V2 does not.

..v4
    **Distant rostral neighbour** via V3; **V2's thin stripes
    project directly to V4**.

...brodmann_areas.brodmann_area_18
    The **cytoarchitectonic counterpart — partial correspondence,
    not identity.** BA 18 spans **V2 and V3**, so V2 is **not**
    co-extensive with BA 18. The BA 18 package's
    ``V_AREA_CORRELATE`` is `("v2", "v3")` — a two-element tuple
    — and its functional-domain set includes V2's three domains
    **plus** V3's `spatial_localization`. Downstream code that
    queries BA 18 gets the union of V2 and V3; downstream code
    that queries V2 gets a **subset** of BA 18.

...cuneus
    The medial-surface gyral landmark. The cuneus's lower margin
    (the upper bank of the calcarine region) carries the **V2
    upper-bank representation of the lower** contralateral visual
    field. **On the left, the lower RIGHT field.** Note the
    mirror-flip: V1's upper field is on the **lower** bank, but
    V2's upper field is on the **upper** bank.

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus carries the **V2 lower-bank representation
    of the upper** contralateral visual field. **On the left,
    the upper RIGHT field.**

...sulci.calcarine_sulcus
    The **reference landmark** for the V1/V2 border — the
    caudomedial boundary of V2 is adjacent to the calcarine
    sulcus.

...sulci.lunate_sulcus
    An inconstant lateral-surface sulcus that, when present, marks
    the **V1/V2 border on the lateral surface**.

..cortex.temporal
    The **ventral stream** continues from V2's thin and pale
    stripes (via V4 and the LOC) into the temporal lobe. **On the
    left, the ventral stream terminates in the left VWFA** (the
    reading area). The temporal package must declare the left V2
    as a source of its visual input via the ventral stream, and
    must note the **left-lateralized VWFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from V2's thick stripes (via
    MT/V5) into the parietal lobe. **On the left, the dorsal
    stream supports right-hemifield spatial attention** at a
    lower weighting than the right's.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V2.

..cortex.cingulate  — indirect
    No direct cingulate → V2 projection.

..cortex.insular  — indirect
    No direct insular → V2 projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** provides a **weak, direct koniocellular projection**
    to V2 (bypassing V1) in addition to V2's indirect LGN input
    via V1. The koniocellular pathway carries the **blue-yellow
    (S-cone) color signal**.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V2
    than to V1**, participating in the cortico-thalamo-cortical
    loops that support visual attention and visual short-term
    memory.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from V2 (via V4 and the LOC) to
    the perirhinal, entorhinal, and parahippocampal cortices.
    **The left V2 is the second stage** of the occipito-
    temporal-hippocampal pathway.

../../right/cortex/occipital/cortex/v2
    The right-hemisphere homologue. Structural fields (V-number,
    BA correlate 18, three-stripe CO organization, V1/V2 and
    V2/V3 borders, retinotopic mirror-flip, cuneus / lingual-
    gyrus relationship, FUNCTIONAL_DOMAINS set, forward-
    declaration caveat text) MUST be byte-identical. Functional
    emphasis and clinical significance diverge — the right V2
    processes the **LEFT** visual hemifield, is weighted toward
    the **global / holistic** aspect of form processing, and its
    thin-stripe output feeds the **right V4 → LOC → right FFA**
    (face) pathway rather than the left V4 → LOC → left VWFA
    (reading) pathway.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "v2"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    V_NUMBER            = "V2"
    ALTERNATE_NAMES     = ("secondary_visual_cortex",
                           "v2",
                           "brodmann_area_18_partial")
        # **Note "brodmann_area_18_partial"** — V2 is **part of**
        # BA 18, sharing the BA with V3. Unlike V1 (whose
        # ALTERNATE_NAMES include "brodmann_area_17_primary_
        # visual" as an exact synonym), V2's BA name is
        # **partial correspondence**, not identity.

    ARCHITECTONIC_SIGNATURES = (
        "cytochrome_oxidase_stripes_thin_thick_pale",
        "dysgranular_extrastriate_cortex",
    )
        # **Two signatures**: the V2 CO stripes (thin / thick /
        # pale), and the dysgranular cytoarchitecture. **The
        # CO stripes are V2's defining architectonic feature**
        # and the anatomical basis of the three-stream output.

    BRODMANN_CORRELATES = (18,)
        # **One BA** — V2 is part of BA 18. But **BA 18 is not
        # exclusive to V2** — V3 shares the same BA. This is
        # why the correspondence is **partial**, not exact,
        # unlike V1 ↔ BA 17.

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** V2 is unique to the occipital
        # lobe.

    RETINOTOPIC_MAP     = "mirror_flip_of_V1_across_V1_V2_border"
        # The map's structure: V2's upper field on the **upper**
        # bank (opposite V1's lower-bank upper field), V2's
        # lower field on the **lower** bank (opposite V1's
        # upper-bank lower field), the V1/V2 border is the
        # vertical meridian, the V2/V3 border is the horizontal
        # meridian. **On the left, the represented hemifield is
        # the RIGHT hemifield.**

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** — left V2
        # processes the RIGHT hemifield.

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing_secondary",
                              "binocular_vision",
                              "form_and_object_perception",
                              # **Three domains** — one fewer than
                              # BA 18 (which has four, adding
                              # `spatial_localization` for V3).
                              # **Three domains** — one fewer than
                              # the right V2 (which has four,
                              # adding `global_visual_processing`
                              # as a right-only emphasis).
                              # NOTE: spatial_localization is
                              # EXCLUDED (V3's domain, not V2's).
                              # NOTE: color_vision is EXCLUDED
                              # (V4's domain; V2 feeds it via
                              # thin stripes but does not
                              # perform it).
                              # NOTE: motion_perception is
                              # EXCLUDED (V5/MT+'s domain; V2
                              # feeds it via thick stripes but
                              # does not perform it).
                              # NOTE: visual_attention is
                              # EXCLUDED as a primary domain.
                              # NOTE: visual_word_processing is
                              # EXCLUDED (V2 is the second stage
                              # of the left reading pathway, not
                              # the operation).
                              # NOTE: face_processing and
                              # global_visual_processing are
                              # EXCLUDED (right-lateralized; the
                              # right V2 carries global_visual_
                              # processing as a right-only
                              # emphasis, but the left V2 does
                              # not).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "primary_visual_processing_secondary":
                                  "second_cortical_stage_of_vision_"
                                  "right_hemifield_border_ownership_"
                                  "texture_filling_in",
                              "binocular_vision":
                                  "stereoscopic_depth_from_"
                                  "disparity_right_hemifield_"
                                  "fusion",
                              "form_and_object_perception":
                                  "local_featural_form_processing_"
                                  "right_hemifield_ventral_stream_"
                                  "to_left_vwfa",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_v2_right_quadrantic_visual_"
                              "field_defect",
                              "left_v2_local_form_processing_"
                              "deficit",
                              "left_v2_hemianopic_alexia_right",
                              "left_v2_indirect_color_and_motion_"
                              "deficits",
                              "left_v2_occipital_infarct_pca_"
                              "territory",
                              "left_v2_migraine_visual_aura",
                              "left_v2_occipital_epilepsy_"
                              "visual_auras",
                              "left_v2_posterior_cortical_"
                              "atrophy",
                              "left_v2_pres_visual_symptoms",
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
computation that references V2 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this package's own
structural fields.** V2 is a leaf V package whose structural
neighbours (V1, V3, V4, BA 18, the cuneus, the calcarine sulcus, the
lateral occipital gyrus, and the LGN) all exist as packages in the
tree. The **lingual gyrus** is a forward reference in ``..gyri``,
but the V2 package does not depend on it.

**The one open question** — the lingual gyrus placement — is
byte-identical to the V1 sibling's. It is a property of the occipital
lobe, not of the hemisphere.

**All forward-declaration caveat text is byte-identical to the left
sibling's.**

--------------------------------------------------------------------------------
PROMOTION RULE (when a V sub-field becomes a package)
--------------------------------------------------------------------------------

V2 is **architectonically homogeneous** — the CO stripes run across
the entire territory — but the **three-stripe organization** is a
**functional subdivision** that is sometimes promoted. If a future
parcellation decides to split V2 into its **three stripe components**
(thin / thick / pale), the promotion takes this form:

    v2/
        __init__.py
        thin_stripes/            # → V4, color/form, ventral stream
            __init__.py
        thick_stripes/           # → MT/V5, motion, dorsal stream
            __init__.py
        pale_stripes/            # → IT, object form, ventral stream
            __init__.py

Then:

  1. Add the three component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The stripe split is a FUNCTIONAL subdivision, not an architectonic
one.** All three stripes are architectonically part of the same
dysgranular V2 territory; they differ in their **connectivity**, not
in their cytoarchitecture.

**No split should be performed while BA 18's `V_AREA_CORRELATE`
still references V2 as a single unit.** The BA 18 → V2 partial
correspondence means that any V2 split must be matched by a
corresponding update to the BA 18 package, in the same commit, in
both hemispheres. Similarly, if V3 is split, the BA 18 package must
be updated in the same commit.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../v2``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "v2"
        LOBE                         "occipital"
        V_NUMBER                     "V2"
        ALTERNATE_NAMES              ("secondary_visual_cortex",
                                     "v2",
                                     "brodmann_area_18_partial")
        ARCHITECTONIC_SIGNATURES     (CO stripes thin/thick/pale,
                                     dysgranular)
        BRODMANN_CORRELATES          (18,)
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same V2 mirror-flip of V1
                                     across the V1/V2 border
        Bounding / overlapping territories (with the LEFT / RIGHT
                                     field labels updated for the
                                     cuneus and lingual gyrus)
        V-to-neighbour adjacency
        CONNECTIVITY                 same bundle names (the
                                     three-stripe → V4 / MT/V5 /
                                     IT pattern is hemisphere-
                                     invariant)
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — left V2 processes
                               the RIGHT hemifield; right V2
                               processes the LEFT hemifield.
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        FUNCTIONAL_DOMAINS     the left has **three** domains
                               (primary_visual_processing_
                               secondary, binocular_vision,
                               form_and_object_perception);
                               the right has **four** (the left's
                               three PLUS `global_visual_
                               processing`, a right-only
                               emphasis).
        DOMAIN_EMPHASIS        left: form_and_object_perception is
                               "local_featural_form_processing_
                               right_hemifield_ventral_stream_to_
                               left_vwfa".
                               right: form_and_object_perception
                               is "global_holistic_form_processing_
                               left_hemifield_ventral_stream_to_
                               right_ffa", and the right's
                               `global_visual_processing` domain
                               is part of this emphasis.
        CONNECTIVITY           same bundle names; left: the V2
                               thin-stripe → V4 → LOC → left VWFA
                               pathway feeds the left reading
                               endpoint.
                               right: the V2 thin-stripe → V4 →
                               LOC → right FFA pathway feeds the
                               right face-recognition endpoint;
                               the thick-stripe → MT/V5 pathway
                               is the dominant dorsal-stream
                               contribution on the right.
        CLINICAL_ANCHORS       left: nine anchors (right
                               quadrantic visual field defect,
                               local form processing deficit,
                               hemianopic alexia (right), indirect
                               color/motion deficits, left
                               occipital infarct, migraine aura,
                               occipital epilepsy, PCA, PRES).
                               right: nine anchors (left
                               quadrantic visual field defect,
                               global form processing deficit,
                               hemianopic alexia (left, milder),
                               indirect color/motion deficits
                               with dominant motion emphasis,
                               right occipital infarct, migraine
                               aura, occipital epilepsy, PCA,
                               PRES).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same V2, the same CO stripes,
and the same three-stripe output — but the *represented hemifield*
is **flipped**.

**The local-vs-global emphasis is the second sharpest entry.** Both
hemispheres carry `form_and_object_perception`, but the **left**
V2's emphasis is on **local / featural** form processing, and the
**right** V2's emphasis is on **global / holistic** form processing.
Additionally, the right V2 carries the `global_visual_processing`
domain (right-only), while the left V2 does not — a **domain-set
divergence**.

**The FUNCTIONAL_DOMAINS set is one element larger on the right.**
The left V2 has **three** domains; the right V2 has **four** (the
left's three plus `global_visual_processing`). This is the mirror of
V1's pattern (three on the left, four on the right), and it is
consistent with BA 18's treatment (five on the left, five on the
right — the same domain set but different emphasis).

**The three-stripe output pattern, the V1/V2 and V2/V3 borders, the
CO stripes, the retinotopic mirror-flip, and the BA 18 partial
correspondence are byte-identical on both sides.** They are
properties of the extrastriate cortex itself, not of the hemisphere.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, PRES, and occipital infarct — are **documented
identically in both siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "v2".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V2".
[ ] ALTERNATE_NAMES includes "secondary_visual_cortex", "v2", and
    **"brodmann_area_18_partial"** — the BA 18 correspondence is
    **partial, not identity** (V3 shares BA 18 with V2).
[ ] ARCHITECTONIC_SIGNATURES includes the **two** signatures:
    CO stripes (thin / thick / pale) and dysgranular extrastriate
    cortex.
[ ] BRODMANN_CORRELATES is exactly ``(18,)`` — **one BA**, but
    **not exclusive** — V3 shares BA 18.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **mirror-flip** structure:
    - V2 upper field on the **upper** bank (opposite V1's lower-
      bank upper field)
    - V2 lower field on the **lower** bank (opposite V1's upper-
      bank lower field)
    - V1/V2 border = vertical meridian
    - V2/V3 border = horizontal meridian
    - **represented hemifield = RIGHT hemifield on the left side**
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] FUNCTIONAL_DOMAINS contains **three** domains:
    - primary_visual_processing_secondary
    - binocular_vision
    - form_and_object_perception
[ ] FUNCTIONAL_DOMAINS **excludes** spatial_localization — **V3's
    domain**, not V2's. The left V2's exclusion of
    `spatial_localization` is why **V2 has three domains and BA
    18 has four**.
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision (V4's domain; V2
    feeds it via thin stripes but does not perform it).
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (V5/MT+'s
    domain; V2 feeds it via thick stripes but does not perform
    it).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a primary
    domain.
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing (V2 is
    the second stage of the left reading pathway, not the
    operation).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing (right-lateralized; the right V2 carries
    global_visual_processing as a right-only emphasis, but the
    left V2 does not).
[ ] **The FUNCTIONAL_DOMAINS set is verified to be a SUBSET of
    BA 18's set** — V2 carries three domains (primary_visual_
    processing_secondary, binocular_vision, form_and_object_
    perception), and BA 18 carries four (the same three plus
    spatial_localization, which is V3's). **V2 is not co-extensive
    with BA 18 in the functional domain set** — the partial
    correspondence extends to the domains.
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis**:
    - primary_visual_processing_secondary → second_cortical_stage_
      of_vision_right_hemifield_border_ownership_texture_filling_in
    - binocular_vision → stereoscopic_depth_from_disparity_right_
      hemifield_fusion
    - form_and_object_perception → **local_featural_form_
      processing_right_hemifield_ventral_stream_to_left_vwfa**
[ ] CONNECTIVITY documents:
    - V1 → V2 principal cortical afferent (the obligate relay)
    - LGN koniocellular direct-to-V2 (weak; carries S-cone
      blue-yellow color; survives V1 lesions)
    - Pulvinar afferent (stronger to V2 than to V1)
    - **Three-stripe V2 output pattern**:
        - thin stripes → V4 (color / form, ventral stream)
        - thick stripes → MT/V5 (motion, dorsal stream)
        - pale stripes → IT (object form, ventral stream)
    - **V2 → V3 relay** (V3 is the second V area in BA 18)
    - Callosal connections to right V2 at the vertical meridian
    - Attentional feedback from left FEF, left DLPFC, left IPS
[ ] CLINICAL_ANCHORS contains the nine left-specific anchors:
    - left_v2_right_quadrantic_visual_field_defect
    - left_v2_local_form_processing_deficit
    - left_v2_hemianopic_alexia_right
    - left_v2_indirect_color_and_motion_deficits
    - left_v2_occipital_infarct_pca_territory
    - left_v2_migraine_visual_aura
    - left_v2_occipital_epilepsy_visual_auras
    - left_v2_posterior_cortical_atrophy
    - left_v2_pres_visual_symptoms
[ ] The **right quadrantic visual field defect** is documented as
    the primary left V2 anchor.
[ ] The **local form processing deficit** is documented as the
    left-lateralized form anchor — the mirror of the right's
    global / holistic deficit.
[ ] **Hemianopic alexia (right)** is documented as a left-
    lateralized reading deficit from the partial right field
    defect, and is described as **milder than a complete left V1
    hemianopia**.
[ ] The **indirect color / motion deficits** are documented as
    *processing* impairments (V2 feeds V4 and MT/V5), not
    *perceptual absences*.
[ ] The **three-stripe output pattern** is documented as the
    anatomical basis for the V2 → three-stream split, and the
    **V2 thin-stripe → V4 → LOC → left VWFA** pathway is
    documented as the left reading pathway.
[ ] The **retinotopic mirror-flip** is documented explicitly,
    with the upper-field / lower-field bank assignments **reversed**
    relative to V1.
[ ] **The BA 18 / V2 relationship is documented as PARTIAL
    correspondence, not identity** — V2 is part of BA 18, but BA
    18 also includes V3. This is the key structural fact about
    V2's cytoarchitectonic correlate, and it distinguishes V2
    from V1 (whose BA 17 correspondence is exact).
[ ] No forward-declaration caveat is needed for the BA-side
    neighbours. The lingual gyrus forward-reference caveat is
    byte-identical to the left sibling's.
[ ] No SUBDIVISIONS promotion is performed while BA 18's
    `V_AREA_CORRELATE` still references V2 as a single unit.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, forward-declaration caveat text) match the left
    sibling; VISUAL_HEMIFIELD, FUNCTIONAL_DOMAINS set (three on
    the left, four on the right), DOMAIN_EMPHASIS (local vs
    global emphasis), CONNECTIVITY emphasis (left VWFA vs right
    FFA endpoint), and CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left V2
    carries "right_hemifield" in its DOMAIN_EMPHASIS entries and
    RETINOTOPIC_MAP; the right V2 carries "left_hemifield."
[ ] **The local-vs-global emphasis is verified**: the left V2
    carries "local_featural" in its `form_and_object_perception`
    emphasis; the right V2 carries "global_holistic."
[ ] **The FUNCTIONAL_DOMAINS set is verified to be a SUBSET of
    BA 18's** — the partial correspondence extends to the
    domains. V2 has three; BA 18 has four (V3 adds
    spatial_localization).
[ ] **The partial correspondence is verified**: V2's
    `BRODMANN_CORRELATES` is `(18,)`, and BA 18's
    `V_AREA_CORRELATE` is `("v2", "v3")`. The two fields are
    consistent (V2 ↔ BA 18; BA 18 → V2 + V3), and the asymmetry
    reflects the partial-correspondence relationship.
[ ] **The three-stripe output pattern is verified** — thin →
    V4, thick → MT/V5, pale → IT. This is the anatomical basis
    of the V2 → three-stream split, and it is **byte-identical
    on both hemispheres**.
[ ] Any downstream code querying "what does the left V2 see?"
    must receive "the RIGHT visual hemifield."
[ ] Any downstream code querying "what is V2?" must receive
    "the secondary visual cortex / V2 / part of BA 18" — the
    **partial** BA 18 correspondence is enforced (V2 is not
    co-extensive with BA 18; V3 shares the same BA).
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** V1 → V2 → V4 → LOC → left VWFA
    chain — the left V2 is the **second stage**, not the reading
    operation.
[ ] Any downstream code assigning face processing must route
    through the **right** V1 → V2 → V4 → LOC → right FFA chain.
[ ] Any downstream code querying "which V area carries
    spatial_localization?" must receive "V3, not V2" — the
    domain allocation between V2 and V3 (both inside BA 18) is
    enforced.
[ ] Any downstream code querying "which V area carries
    global_visual_processing?" must receive "right V2 (as a
    right-only emphasis), not left V2."
[ ] Any downstream code querying "which V area carries
    local_featural_processing?" must receive "left V2 (as an
    emphasis), not right V2."
"""