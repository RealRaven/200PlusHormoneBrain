"""
Secondary Visual Cortex (V2) — Right Hemisphere
================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── v2   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the right
hemisphere's **V2** — the **secondary visual cortex**, the first
extrastriate area, and the immediate downstream target of V1. It is
the **first step of the extrastriate hierarchy** and the territory in
which the visual signal is **first split** into the **three parallel
output streams** that will feed the ventral (object/color), dorsal
(motion), and inferotemporal (form) pathways.

Parent: ``..cortex`` (right occipital functional / V-numbered parent)
— sibling to V1, V3, V4. **Sibling — not parent —** of
``...brodmann_areas/brodmann_area_18``, which sits at the
``..brodmann_areas`` parent level. The V2 / BA 18 relationship is
**partial correspondence, not nesting** — BA 18 spans **both** V2 and
V3, so neither V2 nor V3 is co-extensive with BA 18.

This package is the **structural mirror** of
``../../left/cortex/occipital/cortex/v2``. The V-number, the BA
correlate (18, shared with V3), the architectonic signature (V2 CO
stripes), the V1/V2 border, the retinotopic mirror-flip, and the
three-stripe output organization are identical on both sides; the
**functional emphasis** and **clinical significance** diverge — on
the right, V2's form-and-object contribution is weighted toward the
**global / holistic** aspect, its **thin-stripe** output feeds the
**right V4 → LOC → right FFA** (face) pathway, its **thick-stripe**
output is the **dominant dorsal-stream contribution** on the right,
and right V2 lesions contribute to **global-level form processing
deficits**, to the **right face-recognition input**, and to
**left quadrantic visual field defects**.

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
with V4, V3A, V3B, V5/MT+, and LOC. **V2 is the simpler case.** **This
structural fact is byte-identical to the left sibling's — the
partial correspondence is a property of the BA scheme, not of the
hemisphere.**

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
                          → **on the right, feed the right
                          V4 → LOC → right FFA (face) pathway**

    Thick stripes       → project to MT/V5 (motion)
                          → part of the dorsal stream
                          → **on the right, are the DOMINANT
                          dorsal-stream contribution** — the
                          right MT/V5 is more strongly engaged
                          than the left's

    Pale stripes        → project to the inferotemporal cortex
    (interstripes)        (object form)
                          → part of the ventral stream
                          → **on the right, feed the right
                          object-recognition hierarchy, ending
                          at the right FFA for faces**

This **three-stripe output organization** is the **anatomical basis
of the V2 → three-stream split** — the single most important
functional fact about V2. It is why V2 is sometimes described as the
"gateway to the extrastriate cortex," and why lesions of V2 can
produce **combined** deficits that a lesion of V4 or MT/V5 alone does
not. **On the right, the thick-stripe → MT/V5 contribution is the
dominant one**, consistent with the right-lateralized dorsal
attention network and the right motion-hemisphere dominance.

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
than a complete hemianopia.

**Right-hemisphere specificity**: the right V2 processes the **LEFT**
visual hemifield of both eyes. Its **thin-stripe** output feeds the
**right V4 → LOC → right FFA** pathway — the right face-recognition
pathway — and the right V2 is therefore the **second stage of the
right face pathway** after V1. The right V2's **form-and-object
perception** is weighted toward the **global / holistic** aspect
(Navon's global-precedence asymmetry, the mirror of the left's
local-precedence), and right V2 lesions produce **global-level form
processing deficits** that have no symmetric counterpart on the left
at the same weighting. **Right V2 is the only V area in the tree
whose FUNCTIONAL_DOMAINS set includes `global_visual_processing`**
— the right-lateralized domain that begins at V2 in the right
hemisphere.

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
            co-extensive with BA 18 — V3 shares the same BA.
        V2 CO stripes — the three-stripe organization
            The **thin / thick / pale** stripe pattern is V2's
            defining architectonic signature. **On the right,
            the thick-stripe → MT/V5 projection is the dominant
            dorsal-stream contribution.**
        cuneus — upper-bank V2
            The cuneus's lower margin carries the **V2 upper-bank
            representation of the lower** contralateral visual
            field. **On the right, the lower LEFT field.**
            (Mirror-flip: **V1's upper field is on the LOWER
            bank; V2's upper field is on the UPPER bank.**)
        lingual gyrus — lower-bank V2
            The lingual gyrus carries the **V2 lower-bank
            representation of the upper** contralateral visual
            field. **On the right, the upper LEFT field.**
        calcarine sulcus — reference landmark
            The V1/V2 border (the caudomedial boundary of V2) is
            adjacent to the calcarine sulcus.
        right fusiform face area (FFA) — downstream ventral-
        stream target
            **Right-specific overlay.** The right V2's
            **thin-stripe** output — via V4 and the LOC —
            terminates in the right FFA. The V2 → V4 → LOC → FFA
            pathway is the **right face-recognition pathway**,
            and V2 is its **second stage** after V1.
        right dorsal attention network — thick-stripe target
            **Right-emphasized overlay.** The right V2's
            **thick-stripe** output — via MT/V5 — feeds the
            **right dorsal attention network** (right IPS, right
            FEF). The right's thick-stripe → MT/V5 contribution
            is the **dominant dorsal-stream substrate** for
            left-hemifield motion perception and spatial
            attention.
        global_visual_processing — right-specific domain
            **Right-specific overlay.** The right V2 is the
            **first area in the visual hierarchy** whose
            FUNCTIONAL_DOMAINS set includes
            `global_visual_processing`. The right hemisphere's
            documented advantage for global / holistic visual
            properties (Navon's global-precedence asymmetry)
            **begins at right V2**.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours, the V2 CO stripes, and the cuneus /
lingual-gyrus / calcarine overlays are the same on both sides. What
differs is the **visual hemifield** — the right V2 processes the
LEFT hemifield. The **right FFA downstream target** is a
right-specific overlay that the left V2 package declares as the
**left VWFA** (reading endpoint) instead, and the **right dorsal
attention network thick-stripe target** and **`global_visual_
processing` domain** are right-only additions.

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
                                           V1 is V2's **principal
                                           cortical afferent** — the
                                           obligate relay.
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
                                           (**lower LEFT field on
                                           the right**).
    lingual gyrus (medial-surface          carries the **V2 lower-bank**
    gyrus; forward reference in ..gyri)    representation of the
                                           **upper** visual field
                                           (**upper LEFT field on
                                           the right**).
    calcarine sulcus (reference landmark)  the V1/V2 border is adjacent
                                           to the calcarine sulcus.
    lateral occipital gyrus                V2's lateral extent; part
                                           of the ventral stream's
                                           forward projections to
                                           the LOC and, on the
                                           right, to the FFA.

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized. The field labels (LEFT vs RIGHT) in the
cuneus and lingual gyrus entries are updated for the right hemisphere,
and the lateral-occipital-gyrus note adds the right FFA endpoint.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

V2 participates in **four** canonical occipital functional domains on
the right — **one more than the left V2** (which has three). The
right V2's domain set is:

    primary_visual_processing (secondary)          (right emphasis — PRIMARY)
        **This is V2's defining contribution.** The **second**
        cortical stage of vision, after V1. V2 adds **border
        ownership, texture, illusory contours, surface
        filling-in, and stereoscopic depth from binocular
        disparity** to the low-level features extracted by V1.
        On the right, V2 processes the **LEFT visual hemifield**.

    binocular_vision                               (right emphasis — PRIMARY)
        V2's **binocular disparity neurons** — which are **more
        numerous and more selective than in V1** — support
        **fine stereoscopic depth perception** and **binocular
        fusion**. On the right, binocular vision in V2 combines
        the right-eye and left-eye inputs to the **LEFT visual
        hemifield**.

    form_and_object_perception                     (right emphasis — SECONDARY)
        **This is V2's most right-lateralized contribution.**
        V2's **thin stripes** (color/form) and **pale stripes**
        (object form) contribute to the **early stages of form
        and object processing** that continue in V4 and the LOC.
        **On the right, the form-and-object contribution is
        weighted toward the GLOBAL / HOLISTIC aspect** — the
        right hemisphere's documented advantage in global
        processing (Navon's global-precedence asymmetry is the
        mirror of the left's local-precedence). **The right V2's
        thin-stripe output feeds the right V4 → LOC → right FFA
        pathway** — the face-recognition endpoint.

    global_visual_processing                       (right emphasis — RIGHT-ONLY)
        **This domain is present on the right and absent on the
        left.** The right hemisphere's documented advantage for
        **global / holistic visual properties** — overall shape,
        gestalt, spatial layout — **begins at right V2**, and
        right V2 is the **first area in the visual hierarchy**
        whose FUNCTIONAL_DOMAINS set includes this domain. The
        left V2 does **not** carry it; the left's emphasis is on
        **local / featural processing** (captured within
        `form_and_object_perception` on the left). **The domain-
        set divergence between left V2 (three domains) and
        right V2 (four domains) is this addition**, and it is
        the same divergence pattern as V1 (three on the left,
        four on the right).

**Right-specific caveat on `spatial_localization`.** V2 is **not**
the spatial-localization area — that is **V3**. V2's **thick
stripes** project to MT/V5, but **full spatial localization**
emerges in V3 and V3A. `spatial_localization` is **omitted** from
the V2 `FUNCTIONAL_DOMAINS` tuple; it appears in V3.

**Right-specific caveat on `color_vision`.** V2 is **not** the
color-vision area — that is V4. V2's thin stripes **project to V4**,
but conscious color perception emerges in V4. `color_vision` is
**omitted**.

**Right-specific caveat on `motion_perception`.** V2 is **not** the
motion area — that is V5/MT+, a forward reference. V2's thick
stripes **project to MT/V5**, and **on the right this contribution
is the dominant dorsal-stream pathway**, but conscious motion
perception emerges in MT/V5. `motion_perception` is **omitted**.

**Right-specific caveat on `visual_attention`.** V2 is a **target**
of top-down attentional modulation. It is **not** an attentional
control area. `visual_attention` is **omitted** as a primary domain.

**Right-specific caveat on `visual_word_processing` and `local_
featural_processing`.** These are **left-lateralized** functions
that the right V2 does **not** carry. `visual_word_processing` is
instantiated in the left VWFA (fed by the left V2's thin-stripe
output); `local_featural_processing` is a left-hemisphere emphasis
**within** `form_and_object_perception`. Neither appears in the
right V2 `FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `face_processing`.** The right V2 is the
**input stage** of the right face pathway, but `face_processing`
itself is instantiated in the **right FFA**, not in V2. **No V area
claims `face_processing` as a primary contribution** — it is a
downstream network property of the right occipital + right fusiform
pathway.

**Summary**: V2 carries **exactly four** functional domains on the
right — `primary_visual_processing (secondary)`, `binocular_vision`,
`form_and_object_perception`, and `global_visual_processing`. This is
**one more than the left V2**, which has three (the same first
three). **The right V2's FUNCTIONAL_DOMAINS set matches the right
BA 18's set minus V3's `spatial_localization`** — the same subset
pattern as on the left, with the right-only `global_visual_
processing` domain added.

**Structural note**: V2 carries **one fewer domain than BA 18** on
both hemispheres, because BA 18's fourth domain
(`spatial_localization`) is V3's. **The V2 / BA 18 relationship is a
partial correspondence in the functional domain set as well as in
the cytoarchitectonic correlate** — V2 is a subset of BA 18's
territory and a subset of BA 18's domains, plus the right-only
`global_visual_processing` addition. **The partial correspondence is
a structural property of the BA scheme, byte-identical on both
hemispheres** — the domains that differ between left and right V2
are the **lateralized additions** (`global_visual_processing`), not
the partial-correspondence structure itself.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), right — **indirect, via
          V1**
            **V2's dominant input is from V1, not directly from
            the LGN.** The LGN → V1 → V2 pathway is the **obligate
            relay** for V2's visual input.
        → LGN koniocellular pathway — **weak, direct**
            A **weak, direct LGN → V2 projection** exists via the
            koniocellular layers. It bypasses V1 and carries the
            **blue-yellow (S-cone) color signal**.
        → pulvinar (modulatory, **stronger to V2 than to V1**)
            The pulvinar sends a stronger modulatory projection to
            V2 than to V1. **On the right, the pulvinar → V2 loop
            is part of the right dorsal attention network
            substrate** (via its coupling with the thick-stripe
            → MT/V5 pathway).

    cortical afferents
        → V1, right
            **V2's principal cortical afferent.** The V1 → V2
            projection carries the low-level features that V2
            transforms into border ownership, texture, and
            surface representations.

    cortical efferents — **the three-stripe output**
        → V4, right (via **thin stripes**)
            The **V2 thin stripes** carry the color and form
            signal forward to V4. **On the right, this is the
            first step of the right V4 → LOC → right FFA (face)
            pathway.**
        → MT/V5, right (via **thick stripes**)
            The **V2 thick stripes** carry the motion and
            motion-boundary signal forward to MT/V5. **On the
            right, this pathway is the DOMINANT dorsal-stream
            contribution** — the right MT/V5 is more strongly
            engaged during visuospatial attention and motion-in-
            space processing than the left's. **On the right,
            this pathway supports LEFT-hemifield motion
            perception and feeds the right dorsal attention
            network.**
        → inferotemporal cortex, right (via **pale stripes**)
            The **V2 pale stripes** carry the object-form signal
            forward to the inferotemporal cortex, contributing to
            the ventral stream's object-recognition hierarchy.
            **On the right, this pathway terminates at the right
            FFA (faces)** and the right anterior temporal
            semantic hub.
        → V3, right
            V2 projects rostrally to V3 (the second step of the
            hierarchy), which continues the processing toward V4
            and MT/V5.

    callosal connections
        → left V2
            The callosal fibers connect the right V2 to the left
            V2 at the **vertical meridian** (the V1/V2 border) and
            across the upper and lower banks of the calcarine
            region. This callosal connection supports **the fusion
            of the two hemifields** at the V2 stage.

    attentional feedback
        → frontal eye fields (BA 8), right
            **Right-emphasized.** The right FEF is the dominant
            node of the right ventral attention network and sends
            strong **top-down and bottom-up attentional gain** to
            right V2.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), right
            The right DLPFC sends top-down attentional and
            working-memory signals to V2.
        → intraparietal sulcus, right
            **Right-emphasized.** The right IPS is a core node of
            the right dorsal attention network and sends strong
            top-down spatial-attention signals to right V2,
            supporting **spatial attention** in the LEFT visual
            hemifield.
        → temporoparietal junction, right
            **Right-emphasized.** The right TPJ is the other core
            node of the right ventral attention network and sends
            reorienting signals to right V2 via the right FEF.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the **V2 thin stripes → V4 → LOC → right FFA pathway** is the
**right face-recognition pathway**;
(b) the **V2 thick stripes → MT/V5 pathway** is the **dominant
dorsal-stream contribution** on the right, and it feeds the right
dorsal attention network;
(c) the right FEF, right IPS, and right TPJ send **stronger
attentional gain** to right V2 than the left's counterparts send to
left V2.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_v2_left_quadrantic_visual_field_defect
        **This is the right V2 anchor par excellence.** Unlike V1,
        whose lesions produce a **complete** left homonymous
        hemianopia, V2's lesions produce **partial** field
        defects — most characteristically a **left quadrantic**
        or **sectoranopic** defect. The classic V2-lesion field
        defect is a **left inferior quadrantic** field loss
        (from an upper-bank V2 lesion) or a **left superior
        quadrantic** field loss (from a lower-bank V2 lesion),
        **often with macular sparing** because the foveal
        representation at the occipital pole is fed by the
        dual-blood-supply V1 territory.

    right_v2_global_form_processing_deficit
        **On the right, V2's contribution to form and object
        processing is weighted toward the global / holistic
        aspect.** Right V2 lesions can produce **global-level
        form processing deficits** — the patient may still
        perceive local features but cannot integrate them into a
        coherent global shape (Navon's global-precedence
        asymmetry is the framework). **This is a right-weighted
        anchor**; the left V2 lesion produces the complementary
        **local-level form processing deficit**. **The
        `global_visual_processing` domain that the right V2
        carries (and the left does not) is the additional
        functional substrate for this anchor.**

    right_v2_hemianopic_alexia_left
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **left homonymous field defect** (from a
        right V2 lesion) — is a recognized clinical entity, but
        **weaker than the left-side equivalent**. The reading
        deficit arises because the patient must make large
        **leftward saccades** to compensate for the missing left
        hemifield, and the **left-hemisphere reading network**
        cannot function efficiently without the full right-
        hemifield input. **A right V2 lesion produces a milder
        hemianopic alexia than a left V2 lesion** — the right-
        side lesion is in the non-dominant hemisphere for
        reading, and the reading network itself (left VWFA) is
        intact.

    right_v2_indirect_color_and_motion_deficits
        **V2's thin stripes project to V4 and its thick stripes
        project to MT/V5.** Right V2 lesions can produce
        **indirect color or motion processing deficits** — the
        V4 and MT/V5 areas themselves are intact, but their
        input from V2 is degraded. **On the right, the motion
        deficit is more likely to be clinically apparent than on
        the left**, because the right MT/V5 is the dominant
        motion area and the right V2's thick-stripe → MT/V5
        pathway is the dominant dorsal-stream contribution. The
        color deficit in a V2 lesion is typically **milder**
        than in a V4 lesion. **Isolated achromatopsia (V4) or
        akinetopsia (V5/MT+) from a V2 lesion would be
        unexpected.**

    right_v2_contribution_to_prosopagnosia
        **Right-emphasized.** Right V2 is the **second stage**
        (after V1) of the right ventral stream that feeds the
        right FFA, and **right occipito-temporal lesions** that
        involve the right FFA or its input pathway produce
        **prosopagnosia**. **Isolated right V2 lesions do not
        produce prosopagnosia** — the right FFA is spared — but
        the right V2 is part of the **occipital input pathway**
        of the right-lateralized face-recognition system.
        **Prosopagnosia is the canonical right-lateralized
        visual-recognition deficit**, and right V2 is its
        second cortical stage. **This anchor has no symmetric
        counterpart on the left** — the left V2 feeds the left
        VWFA (reading), not a prosopagnosia pathway.

    right_v2_left_hemifield_neglect_contribution
        **Right-emphasized.** Right V2 lesions contribute to
        **left hemispatial neglect** when the lesion extends
        beyond V2 into the right parietal and right frontal
        territories. **Isolated right V2 lesions do not produce
        neglect** — the patient has a left quadrantic field
        defect but can attend to the left field cognitively —
        but the right V2's **thick-stripe → MT/V5 pathway** is
        part of the **right dorsal attention network** substrate
        that, when damaged together with the right IPS and right
        FEF, contributes to the neglect syndrome. **The right
        V2's contribution to neglect is via its thick-stripe
        output**, distinct from the right V1's contribution via
        the right ventral attention network. **This anchor has
        no symmetric counterpart on the left.**

    right_v2_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct**
        involving V2 produces a **left quadrantic or
        sectoranopic defect** (from V2) on top of a **left
        homonymous hemianopia** (from V1). **Isolated right PCA
        infarcts do not produce alexia without agraphia** —
        that syndrome is left-lateralized. **The V2-specific
        contribution is the quadrantic extension of the field
        defect beyond the V1-only hemianopia.**

    right_v2_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **V1 AND V2**. **The V2 contribution
        is the propagation of the visual aura from V1's simple
        features (flashes) to V2's more complex features (the
        zigzag fortification lines)**. **This anchor is
        hemisphere-invariant**, but the aura's field involvement
        is contralateral (left field on the right side).

    right_v2_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **V1 OR V2**. **V2 auras** are typically **more
        complex** than V1 auras — the patient may see **formed
        objects, recognizable scenes, or specific colors** in
        addition to elementary shapes. **Right V2 auras** project
        to the **left visual field** and can be preceded or
        accompanied by **visual field defects** that persist
        after the seizure.

    right_v2_posterior_cortical_atrophy_benson_syndrome
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1 AND V2 bilaterally** in
        later stages. **Right V2** is part of the substrate of
        the **progressive dorsal-stream dysfunction** that
        produces **Benson syndrome** — the right-lateralized
        clinical presentation with **progressive prosopagnosia,
        visuospatial deficits, optic ataxia, and
        simultanagnosia**. **On the right, PCA presents with the
        visuospatial / prosopagnosic syndrome**; on the left,
        with the progressive reading deficits.

    right_v2_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects** from **bilateral occipital
        involvement**. **The V2 contribution** is the
        **extrastriate involvement** that produces **visual
        hallucinations** (V2 hyperexcitability) and **quadrantic
        defects** (V2 partial loss). **The syndrome is
        reversible** in most cases.

**The V2-specific clinical anchors** — `right_v2_left_quadrantic_
visual_field_defect`, `right_v2_global_form_processing_deficit`,
`right_v2_hemianopic_alexia_left`, `right_v2_indirect_color_and_
motion_deficits`, `right_v2_contribution_to_prosopagnosia`, and
`right_v2_left_hemifield_neglect_contribution` — are the **mirror of
the right BA 18 anchors** with a narrower scope (V2 only, not V2+V3)
and the **right-emphasized additions** (prosopagnosia contribution,
left hemifield neglect contribution via thick-stripe → MT/V5).

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (the syndrome, with the right's Benson subtype
emphasis), PRES, and occipital infarct — are **documented
identically in both siblings**, with the side-appropriate field
label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..cortex  (parent)
    The right occipital functional / V-numbered parent.

..primary_visual_cortex  (V1)
    **Caudal neighbour** via the **V1/V2 border**. V1 is V2's
    principal cortical afferent.

..v3
    **Rostral neighbour** via the **V2/V3 border** — the
    retinotopically defined horizontal-meridian boundary. **V2 and
    V3 share BA 18.** V3 carries the `spatial_localization` domain
    that V2 does not. **On the right, V3's motion-boundary and
    depth-from-motion contributions are more strongly engaged than
    the left's**, and V3's thick-stripe → MT/V5 relay is part of
    the dominant right dorsal-stream substrate.

..v4
    **Distant rostral neighbour** via V3; **V2's thin stripes
    project directly to V4**.

...brodmann_areas.brodmann_area_18
    The **cytoarchitectonic counterpart — partial correspondence,
    not identity.** BA 18 spans **V2 and V3**. The BA 18 package's
    ``V_AREA_CORRELATE`` is `("v2", "v3")`.

...cuneus
    The medial-surface gyral landmark. **On the right, the
    cuneus's V2 upper-bank representation carries the lower LEFT
    visual field.**

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus carries the **V2 lower-bank representation
    of the upper** contralateral visual field. **On the right,
    the upper LEFT field.**

...sulci.calcarine_sulcus
    The **reference landmark** for the V1/V2 border.

...sulci.lunate_sulcus
    The inconstant lateral-surface landmark for the V1/V2 border
    (when present).

..cortex.temporal
    The **ventral stream** continues from V2's thin and pale
    stripes (via V4 and the LOC) into the temporal lobe. **On the
    right, the ventral stream terminates in the right FFA** (the
    face area). The temporal package must declare the right V2 as
    a source of its visual input via the ventral stream, and must
    note the **right-lateralized FFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from V2's thick stripes (via
    MT/V5) into the parietal lobe. **On the right, the dorsal
    stream is more strongly engaged during visuospatial
    attention**, and the right V2's thick-stripe → MT/V5 pathway
    is the **dominant dorsal-stream contribution**. The parietal
    package must declare the right V2 as a source of its visual
    input for the dorsal stream, and must note the
    **right-lateralized attentional emphasis**.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V2. **On the right, the right FEF is the dominant
    node of the ventral attention network**, and right frontal
    lesions contribute to left hemispatial neglect.

..cortex.cingulate  — indirect
    No direct cingulate → V2 projection.

..cortex.insular  — indirect
    No direct insular → V2 projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** provides a **weak, direct koniocellular projection**
    to V2 (bypassing V1). The koniocellular pathway carries the
    **blue-yellow (S-cone) color signal**.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V2
    than to V1**. **On the right, the pulvinar → V2 loop is part
    of the right dorsal attention network substrate.**

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from V2 (via V4 and the LOC) to
    the perirhinal, entorhinal, and parahippocampal cortices.
    **On the right, the parahippocampal place area (PPA) and the
    retrosplenial complex receive visual input supporting scene
    and spatial memory**, which are more strongly right-
    lateralized.

../../left/cortex/occipital/cortex/v2
    The left-hemisphere homologue. Structural fields (V-number,
    BA correlate 18, three-stripe CO organization, V1/V2 and
    V2/V3 borders, retinotopic mirror-flip, cuneus / lingual-
    gyrus relationship, forward-declaration caveat text) MUST be
    byte-identical. Functional emphasis and clinical
    significance diverge — the right V2 processes the **LEFT**
    visual hemifield, is weighted toward the **global /
    holistic** aspect of form processing, carries the
    **`global_visual_processing` domain** (right-only), and its
    thin-stripe output feeds the **right V4 → LOC → right FFA**
    (face) pathway rather than the left V4 → LOC → left VWFA
    (reading) pathway.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "v2"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    V_NUMBER            = "V2"
    ALTERNATE_NAMES     = ("secondary_visual_cortex",
                           "v2",
                           "brodmann_area_18_partial")
        # **Byte-identical to the left sibling's.** The partial
        # BA 18 correspondence is a property of the territory,
        # not of the hemisphere.

    ARCHITECTONIC_SIGNATURES = (
        "cytochrome_oxidase_stripes_thin_thick_pale",
        "dysgranular_extrastriate_cortex",
    )
        # **Byte-identical to the left sibling's.**

    BRODMANN_CORRELATES = (18,)
        # **One BA** — partial correspondence. **Byte-identical
        # to the left sibling's.**

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** Byte-identical.

    RETINOTOPIC_MAP     = "mirror_flip_of_V1_across_V1_V2_border"
        # The map's *structure* is identical to the left's.
        # **On the right, the represented hemifield is the LEFT
        # hemifield.**

    VISUAL_HEMIFIELD    = "left"
        # **The represented visual hemifield** — right V2
        # processes the LEFT hemifield.

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing_secondary",
                              "binocular_vision",
                              "form_and_object_perception",
                              "global_visual_processing",
                                                       # right-
                                                       # only
                              # **Four domains** — one more than
                              # the left V2 (which has three).
                              # The right V2 adds the right-only
                              # `global_visual_processing` domain.
                              # NOTE: spatial_localization is
                              # EXCLUDED (V3's domain).
                              # NOTE: color_vision, motion_
                              # perception, visual_attention,
                              # visual_word_processing are
                              # EXCLUDED (same rationale as on
                              # the left).
                              # NOTE: face_processing is
                              # EXCLUDED as a *V2 domain* (it
                              # lives downstream in the right
                              # FFA).
                              # NOTE: local_featural_processing
                              # is EXCLUDED (left-lateralized).
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "primary_visual_processing_secondary":
                                  "second_cortical_stage_of_vision_"
                                  "left_hemifield_border_ownership_"
                                  "texture_filling_in",
                              "binocular_vision":
                                  "stereoscopic_depth_from_"
                                  "disparity_left_hemifield_"
                                  "fusion",
                              "form_and_object_perception":
                                  "global_holistic_form_processing_"
                                  "left_hemifield_ventral_stream_"
                                  "to_right_ffa",
                              "global_visual_processing":
                                  "right_hemisphere_global_"
                                  "precedence_beginning_at_V2",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_v2_left_quadrantic_visual_"
                              "field_defect",
                              "right_v2_global_form_processing_"
                              "deficit",
                              "right_v2_hemianopic_alexia_left",
                              "right_v2_indirect_color_and_motion_"
                              "deficits",
                              "right_v2_contribution_to_"
                              "prosopagnosia",
                              "right_v2_left_hemifield_neglect_"
                              "contribution",
                              "right_v2_occipital_infarct_pca_"
                              "territory",
                              "right_v2_migraine_visual_aura",
                              "right_v2_occipital_epilepsy_"
                              "visual_auras",
                              "right_v2_posterior_cortical_"
                              "atrophy_benson_syndrome",
                              "right_v2_pres_visual_symptoms",
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
byte-identical to the left sibling's.

**All forward-declaration caveat text is byte-identical to the left
sibling's.**

--------------------------------------------------------------------------------
PROMOTION RULE (when a V sub-field becomes a package)
--------------------------------------------------------------------------------

V2 is **architectonically homogeneous**, but the **three-stripe
organization** is a functional subdivision that is sometimes
promoted:

    v2/
        __init__.py
        thin_stripes/            # → V4, color/form, ventral
            __init__.py
        thick_stripes/           # → MT/V5, motion, dorsal
            __init__.py
        pale_stripes/            # → IT, object form, ventral
            __init__.py

Then:

  1. Add the three component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the left side in the same commit.

**The stripe split is a FUNCTIONAL subdivision, not an architectonic
one.** **On the right, the thick-stripe component is the dominant
dorsal-stream contributor** — right thick stripes → MT/V5 → right
IPS is the dominant dorsal-attention substrate. The thin-stripe
component feeds the right V4 → LOC → right FFA pathway (faces). The
pale-stripe component feeds the right IT object-recognition
hierarchy.

**No split should be performed while BA 18's `V_AREA_CORRELATE`
still references V2 as a single unit.**

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../v2``:

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
        Bounding / overlapping territories (with the LEFT / RIGHT
                                     field labels updated)
        V-to-neighbour adjacency
        CONNECTIVITY                 same bundle names
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — right V2 processes
                               the LEFT hemifield.
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        FUNCTIONAL_DOMAINS     the right has **four** domains
                               (the left's three PLUS `global_
                               visual_processing`, a right-only
                               emphasis). **The right V2's set
                               matches the right BA 18's minus
                               V3's `spatial_localization`.**
        DOMAIN_EMPHASIS        right: form_and_object_perception
                               is "global_holistic_form_processing_
                               left_hemifield_ventral_stream_to_
                               right_ffa"; and the right V2 adds
                               the `global_visual_processing`
                               emphasis entry.
                               left: form_and_object_perception
                               is "local_featural_form_processing_
                               right_hemifield_ventral_stream_to_
                               left_vwfa".
        CONNECTIVITY           same bundle names; right: the V2
                               thin-stripe → V4 → LOC → right FFA
                               pathway feeds the right face-
                               recognition endpoint; the V2
                               thick-stripe → MT/V5 pathway is
                               the **dominant dorsal-stream
                               contribution**; the right FEF,
                               right IPS, and right TPJ send
                               strong attentional gain.
                               left: the V2 thin-stripe → V4 →
                               LOC → left VWFA pathway feeds the
                               left reading endpoint.
        CLINICAL_ANCHORS       right: eleven anchors (left
                               quadrantic visual field defect,
                               global form processing deficit,
                               hemianopic alexia (left, milder),
                               indirect color/motion deficits
                               with dominant motion emphasis,
                               **contribution to prosopagnosia**,
                               **left hemifield neglect
                               contribution** via thick stripes,
                               right occipital infarct, migraine
                               aura, occipital epilepsy, PCA
                               (Benson syndrome), PRES).
                               left: nine anchors (right
                               quadrantic visual field defect,
                               local form processing deficit,
                               hemianopic alexia (right), indirect
                               color/motion deficits, left
                               occipital infarct, migraine aura,
                               occipital epilepsy, PCA, PRES).

**The visual-hemifield asymmetry is the sharpest single entry.**

**The local-vs-global emphasis is the second sharpest entry.** Both
hemispheres carry `form_and_object_perception`, but the **left**
V2's emphasis is on **local / featural**, and the **right** V2's
emphasis is on **global / holistic**. **The right V2 adds the
`global_visual_processing` domain** — the **domain-set divergence**
that mirrors V1's pattern (three on the left, four on the right).

**The FUNCTIONAL_DOMAINS set is one element larger on the right.**
The left V2 has **three** domains; the right V2 has **four** (the
left's three plus `global_visual_processing`). This matches the
right BA 18's set minus V3's `spatial_localization`, confirming the
partial correspondence.

**The three-stripe output pattern, the V1/V2 and V2/V3 borders, the
CO stripes, the retinotopic mirror-flip, the BA 18 partial
correspondence, and the FUNCTIONAL_DOMAINS subset structure are
byte-identical on both sides.**

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "v2" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V2".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's
    (including "brodmann_area_18_partial").
[ ] ARCHITECTONIC_SIGNATURES is byte-identical to the left
    sibling's (CO stripes, dysgranular).
[ ] BRODMANN_CORRELATES is exactly ``(18,)`` — byte-identical to
    the left sibling's.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **mirror-flip** structure with
    the **LEFT hemifield label**.
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class
    field.
[ ] FUNCTIONAL_DOMAINS contains **four** domains:
    - primary_visual_processing_secondary
    - binocular_vision
    - form_and_object_perception
    - **global_visual_processing** (right-only)
[ ] FUNCTIONAL_DOMAINS **excludes** spatial_localization (V3's
    domain — same exclusion as left V2).
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision, motion_perception
    (V4 and V5/MT+ domains).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a primary
    domain.
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing and
    local_featural_processing (left-lateralized).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing as a **V2
    domain** (lives downstream in the right FFA).
[ ] **The FUNCTIONAL_DOMAINS set is verified to be a SUBSET of
    right BA 18's minus V3's `spatial_localization`** — the
    partial correspondence extends to the domains on both
    hemispheres.
[ ] **The right's `global_visual_processing` addition is
    verified** — it is present on the right V2 and absent on
    the left V2. **This is a domain-set divergence, not just a
    weighting divergence.**
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis** per
    domain:
    - primary_visual_processing_secondary → second_cortical_stage_
      of_vision_left_hemifield_border_ownership_texture_
      filling_in
    - binocular_vision → stereoscopic_depth_from_disparity_left_
      hemifield_fusion
    - form_and_object_perception → **global_holistic_form_
      processing_left_hemifield_ventral_stream_to_right_ffa**
    - global_visual_processing → right_hemisphere_global_
      precedence_beginning_at_V2
[ ] CONNECTIVITY documents:
    - V1 → V2 principal cortical afferent (the obligate relay,
      carrying the LEFT hemifield)
    - LGN koniocellular direct-to-V2 (weak; S-cone blue-yellow
      color; survives V1 lesions)
    - Pulvinar afferent (stronger to V2 than to V1; part of the
      right dorsal attention network substrate)
    - **Three-stripe V2 output pattern**:
        - thin stripes → V4 (color / form, feeds the right FFA
          endpoint)
        - thick stripes → MT/V5 (**dominant dorsal-stream
          contribution on the right**, feeding the right IPS /
          right FEF)
        - pale stripes → IT (object form, right FFA endpoint)
    - **V2 → V3 relay** (V3 is the second V area in BA 18)
    - Callosal connections to left V2
    - Attentional feedback from right FEF, right DLPFC, right
      IPS, right TPJ
[ ] CLINICAL_ANCHORS contains the eleven right-specific anchors:
    - right_v2_left_quadrantic_visual_field_defect
    - right_v2_global_form_processing_deficit
    - right_v2_hemianopic_alexia_left
    - right_v2_indirect_color_and_motion_deficits
    - **right_v2_contribution_to_prosopagnosia**
    - **right_v2_left_hemifield_neglect_contribution**
    - right_v2_occipital_infarct_pca_territory
    - right_v2_migraine_visual_aura
    - right_v2_occipital_epilepsy_visual_auras
    - right_v2_posterior_cortical_atrophy_benson_syndrome
    - right_v2_pres_visual_symptoms
[ ] The **left quadrantic visual field defect** is documented as
    the primary right V2 anchor.
[ ] The **global form processing deficit** is documented as the
    right-lateralized form anchor — the mirror of the left's
    local deficit.
[ ] **Hemianopic alexia (left)** is documented as a right-side
    anchor that is **milder** than the left-side equivalent.
[ ] The **indirect color / motion deficits** are documented as
    *processing* impairments, with the **motion deficit more
    clinically prominent on the right** (dominant motion
    hemisphere).
[ ] **The right V2's contribution to prosopagnosia** is documented
    as a right-emphasized anchor — **isolated right V2 lesions do
    not produce prosopagnosia**, but the right V2 is part of the
    occipital input pathway of the right face-recognition system.
[ ] **The right V2's contribution to left hemispatial neglect**
    is documented as a right-emphasized anchor — **isolated right
    V2 lesions do not produce neglect**, but the right V2's
    thick-stripe → MT/V5 pathway is part of the right dorsal
    attention network substrate.
[ ] The **three-stripe output pattern** is documented, with the
    **thick-stripe component being dominant on the right**.
[ ] The **retinotopic mirror-flip** is documented with the LEFT
    hemifield label.
[ ] **The BA 18 / V2 partial correspondence is documented as
    PARTIAL, not identity** — V2 is part of BA 18, but BA 18 also
    includes V3. Byte-identical to the left sibling's structural
    note.
[ ] No forward-declaration caveat is needed. The lingual gyrus
    forward-reference caveat is byte-identical to the left
    sibling's.
[ ] No SUBDIVISIONS promotion is performed while BA 18's
    V_AREA_CORRELATE still references V2 as a single unit.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, forward-declaration caveat text) match the left
    sibling; VISUAL_HEMIFIELD, FUNCTIONAL_DOMAINS set (four on
    the right, three on the left), DOMAIN_EMPHASIS (global vs
    local emphasis), CONNECTIVITY emphasis (right FFA vs left
    VWFA endpoint; dominant thick-stripe on the right), and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    V2 carries "left_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP; the left V2 carries "right_hemifield."
[ ] **The local-vs-global emphasis is verified**: the right V2
    carries "global_holistic" in its `form_and_object_perception`
    emphasis; the left V2 carries "local_featural."
[ ] **The right-specific FUNCTIONAL_DOMAINS addition is
    verified**: `global_visual_processing` is present on the
    right V2 and absent on the left V2.
[ ] **The FUNCTIONAL_DOMAINS set is verified to be a SUBSET of
    right BA 18's minus V3's `spatial_localization`** — the
    partial correspondence extends to the domains.
[ ] **The right V2's `FUNCTIONAL_DOMAINS` set is one element
    larger than the left V2's** — the same domain-set
    divergence pattern as V1 (four on the right, three on the
    left).
[ ] **The right-only clinical anchors are verified**:
    `right_v2_contribution_to_prosopagnosia` and
    `right_v2_left_hemifield_neglect_contribution` are present
    on the right and absent on the left.
[ ] Any downstream code querying "what does the right V2 see?"
    must receive "the LEFT visual hemifield."
[ ] Any downstream code querying "what is V2?" must receive
    "the secondary visual cortex / V2 / part of BA 18" — the
    partial BA 18 correspondence is enforced.
[ ] Any downstream code querying "which V area carries
    spatial_localization?" must receive "V3, not V2" — the
    domain allocation between V2 and V3 is enforced.
[ ] Any downstream code querying "which V area carries
    global_visual_processing?" must receive "right V2 (as a
    right-only domain), not left V2."
[ ] Any downstream code assigning the right face pathway must
    route through the **right** V1 → V2 → V4 → LOC → right FFA
    chain — the right V2 is the second stage.
[ ] Any downstream code assigning left hemispatial neglect must
    note that **right V2's thick-stripe → MT/V5 pathway is a
    contributor**, not a sole cause.
"""