"""
Quaternary Visual Cortex (V4) — Left Hemisphere
================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── v4   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the left
hemisphere's **V4** — the **quaternary visual cortex**, the **color and
form area**, and the **fourth step of the V1 → V2 → V3 → V4 hierarchy**.
It is the **first V area in the hierarchy whose defining functional
contribution is a single, named visual dimension** (color), and the
**first V area whose primary output is not another occipital V area
but the lateral occipital complex (LOC)** — the gateway to the ventral
stream's object-recognition machinery.

Parent: ``..cortex`` (left occipital functional / V-numbered parent)
— sibling to V1, V2, V3. **Sibling — not parent —** of
``...brodmann_areas/brodmann_area_19``, which sits at the
``..brodmann_areas`` parent level. The V4 / BA 19 relationship is
**partial correspondence, not nesting** — BA 19 spans **V3, V4, V3A,
V3B, V5/MT+, and LOC**, so V4 is **one of six** V areas that share
BA 19.

This package is the **structural mirror** of
``../../right/cortex/occipital/cortex/v4``. The V-number, the BA
correlate (19, shared with five other V areas), the architectonic
signature (color globs), the V3/V4 border, the retinotopic triple
mirror-flip, and the two-domain functional set are identical on both
sides; the **functional emphasis** and **clinical significance**
diverge — on the left, V4 is weighted toward **color-form-language
integration**, its **LOC** output feeds the **left VWFA (reading)**
endpoint, and left V4 lesions produce **color agnosia**,
**color-form-language integration deficits**, and — when the lesion
extends into the splenium — **alexia without agraphia**. On the right,
V4 is weighted toward **pure color perception and the felt /
phenomenal aspect of color experience**, its **LOC** output feeds the
**right FFA (face)** endpoint, and right V4 lesions produce
**hemiachromatopsia without the language-linked color deficits**.

**The defining structural fact about V4** is that it is the **second
V area in the hierarchy whose BA correlate is a partial
correspondence** — BA 19 spans six V areas, and V4 is the **first of
them in the V1-V4 hierarchy** (V3 is the second, sharing BA 19 with
V4). This makes the V4 / BA 19 relationship **the most extreme
partial correspondence** in the V1–V4 set:

    BA 17  =  V1                             (exactly)
    BA 18  =  V2 + V3                        (partial, 2 V areas)
    BA 19  =  V3 + V4 + V3A + V3B + V5/MT+ + LOC  (partial, 6 V areas)

**V4 is the first V area whose BA correlate is a "1-of-many"
relationship** — its domain set is a **subset** of BA 19's
territory, not co-extensive with it.

--------------------------------------------------------------------------------
WHAT V4 IS
--------------------------------------------------------------------------------

V4 is the **quaternary visual cortex** — the **color and form area**
of the ventral extrastriate cortex. It occupies **two anatomical
components** with slightly different locations and slightly different
functional roles:

    V4v (or hV4)        the **ventral component**, on the
                        **fusiform gyrus** and the **collateral
                        sulcus**. Represents the **upper** visual
                        field. Functionally weighted toward **hue
                        perception**, **saturation**, and
                        **stereo-defined form**. **On the left,
                        V4v feeds the left LOC → left VWFA
                        (reading) pathway via its color-form
                        output.**

    V4d (or V4)         the **dorsal component**, on the **lateral
                        occipital cortex**. Represents the **lower**
                        visual field. Functionally weighted toward
                        **color-form interaction**, **shape from
                        color**, and **surface segmentation by
                        color**. **On the left, V4d's output
                        feeds the left LOC for general object
                        recognition.**

The **V4v / V4d split is analogous to the V3d / V3v split** —
**two distinct subregions with different retinotopic and functional
signatures, sometimes treated as separate V areas** (V4v / hV4 and
V4d / V4) in the parcellation literature. **The current tree keeps
them together as "V4"**, consistent with the parent's
``V_AREA_CORRELATE`` entry.

**The architectonic signature of V4 is the color globs** — modular
clusters of **hue-selective neurons** that are visible on
cytochrome-oxidase and functional imaging as discrete "blobs" or
"globs" within V4. The globs are the anatomical basis of V4's
**color perception** role, and they are the **only architectonic
feature in the occipital lobe that is specifically associated with a
named visual dimension (color)**.

**The retinotopic organization of V4 is a triple mirror-flip of
V1** — the fourth stage in the alternating mirror-image hierarchy:

    V1 upper field → lower bank (lingual gyrus)
    V2 upper field → upper bank (cuneus)   [flip 1 — reversed]
    V3 upper field → lower bank (lingual gyrus)  [flip 2 — back
                                                  to V1]
    V4 upper field → **lateral fusiform** (V4v)  [flip 3 —
                                                  reversed again]

V4's bank assignment is **not** the calcarine banks — V4 is primarily
on the **fusiform gyrus** (below the lingual gyrus) and the **lateral
occipital cortex**, not on the calcarine sulcus. Its retinotopic
arrangement preserves the alternating mirror-flip pattern, but the
**physical location is different** from V1, V2, and V3.

**Left-hemisphere specificity**: the left V4 processes the **RIGHT**
visual hemifield of both eyes. Its **V4v** output feeds the **left
V4v → LOC → left VWFA (reading)** pathway — the left V4 is the
**fourth stage of the left reading pathway** after V1, V2, and V3v.
Its **V4d** output feeds the left LOC for general object recognition.
The left V4 is weighted toward **color-form-language integration** —
the use of color information in the left hemisphere's language-linked
object-recognition network — and left V4 lesions produce **color
agnosia** (impaired ability to **name** colors despite intact color
perception), **color-form-language integration deficits**, and —
when the lesion extends into the splenium — **alexia without
agraphia**. **The left V4 does not carry the "felt / phenomenal
aspect of color experience" at the same weighting as the right V4** —
the left V4's primary domain is **color-form-language integration**,
not pure color perception.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours (functional)
        caudally / medially    V3 (V3v ventral, V3d dorsal) via the
                               **V3/V4 border** (retinotopic, not
                               architectonic)
        rostrally              the LOC (lateral occipital complex)
                               — a **forward reference** in the
                               current tree
        ventrally              the collateral sulcus and the
                               lingual gyrus (V4v's ventral edge)
        laterally              the lateral occipital gyrus (V4d's
                               lateral extent)
        dorsally               V3d / V3A territory (V4d's dorsal
                               edge)

    Functional overlays
        BA 19 — PARTIAL correspondence (V4 shares BA 19 with V3,
        V3A, V3B, V5/MT+, LOC)
            V4 is **one of six V areas** that span BA 19. This is
            the **most extreme partial correspondence** in the
            V1–V4 set — 6 V areas per BA.
        V4v (hV4) — ventral component
            Upper-field representation on the fusiform gyrus.
            Hue, saturation, stereo-defined form. **On the left,
            feeds the left LOC → left VWFA (reading) pathway.**
        V4d — dorsal component
            Lower-field representation on the lateral occipital
            cortex. Color-form interaction, shape from color,
            surface segmentation. **On the left, feeds the left
            LOC for object recognition.**
        color globs — architectonic signature
            Modular clusters of hue-selective neurons. The
            anatomical basis of V4's **color perception** role,
            and the **only architectonic feature in the occipital
            lobe specifically associated with a named visual
            dimension**.
        fusiform gyrus — ventral component (V4v)
            The fusiform gyrus carries V4v's upper-field
            representation. **On the left, the fusiform gyrus's
            V4v → LOC → left VWFA pathway is the reading
            pathway.** (Forward reference in ``..gyri`` — not
            yet a package.)
        lateral occipital gyrus — dorsal component (V4d)
            The lateral occipital gyrus carries V4d's lower-field
            representation and its lateral extent. **On the
            left, feeds the left LOC.**
        left visual word form area (VWFA) — downstream
        ventral-stream target
            **Left-specific overlay.** The left V4v's output —
            via the LOC — terminates in the left VWFA. The
            V4v → LOC → VWFA pathway is the **left reading
            pathway**, and V4v is its **fourth stage** after
            V1, V2, and V3v. **The V4v → LOC → left VWFA pathway
            is the anatomical substrate of color-form-language
            integration.**

**This field is structurally identical to the right sibling's** — the
architectonic neighbours, the V4v / V4d distinction, the color globs,
and the fusiform / lateral-occipital / collateral-sulcus overlays are
the same on both sides. What differs is the **visual hemifield** —
the left V4 processes the RIGHT hemifield — and the **downstream
target emphasis** — the left V4v → LOC → **left VWFA (reading)**, the
right V4v → LOC → **right FFA (face)**.

--------------------------------------------------------------------------------
V-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    V3                                     **caudal neighbour** via the
                                           **V3/V4 border** — the
                                           retinotopic boundary
                                           (V3v ventral, V3d
                                           dorsal). **V3v → V4 is
                                           the principal cortical
                                           afferent** for V4's
                                           form-from-motion and
                                           color-form signals. **V4
                                           and V3 share BA 19** —
                                           they are the two V
                                           areas of the V1-V4
                                           hierarchy that sit in
                                           the same BA.
    V4A  (forward reference)               **Dorsal / lateral
                                           neighbour** — some
                                           parcellations treat V4d
                                           as "V4A" (a distinct
                                           area). **Not yet a
                                           package** — recorded as
                                           a forward reference.
    V3A  (forward reference)               **Dorsal rostral neighbour**
                                           — not yet a package. V3A
                                           is the motion-in-depth
                                           and spatial-attention
                                           area.
    V5 / MT+  (forward reference)          **Dorsal / lateral
                                           neighbour** — not yet a
                                           package. V5/MT+ is the
                                           motion area.
    LOC  (forward reference)               **Rostral neighbour** — not
                                           yet a package. **V4's
                                           primary output target**
                                           (via V4v and V4d). LOC
                                           is the object-recognition
                                           complex of the ventral
                                           stream, and the occipital
                                           input to the left VWFA
                                           (reading) or right FFA
                                           (faces).
    BA 19                                  **Shared with V3, V3A,
                                           V3B, V5/MT+, LOC** — V4
                                           is one of six V areas
                                           that span BA 19. The BA
                                           19 / V4 relationship is
                                           the **most extreme
                                           partial correspondence**
                                           in the V1-V4 set.
    fusiform gyrus (medial-surface          carries V4v's upper-field
    gyrus; forward reference in ..gyri)    representation (**upper
                                           RIGHT field on the
                                           left**).
    lateral occipital gyrus                carries V4d's lower-field
                                           representation (**lower
                                           RIGHT field on the
                                           left**). **On the left,
                                           the lateral occipital
                                           gyrus's V4d feeds the
                                           left LOC.**
    collateral sulcus                      the ventral boundary of
                                           V4v on the fusiform gyrus.

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

V4 participates in **two** canonical occipital functional domains —
the **smallest domain set of any current V area**. V4's domains are:

    color_vision                                   (left emphasis — PRIMARY)
        **This is V4's defining contribution — and the only
        V area in the V1–V4 hierarchy whose primary domain
        includes color_vision.** V4's **color globs** are the
        anatomical substrate of hue perception, saturation
        perception, and **color-form interaction**. On the left,
        V4's color contribution is weighted toward the
        **color-form-language integration** — the use of color
        information in the left hemisphere's language-linked
        object-recognition network. **Left V4 lesions produce
        color agnosia** (impaired color naming) **more severely
        than right V4 lesions**, because the left hemisphere's
        language areas are essential for color naming.

    form_and_object_perception                     (left emphasis — PRIMARY)
        **This is V4's second defining contribution.**
        V4v and V4d contribute to the **early-to-mid stages of
        form and object processing** that continue in the LOC.
        V4's form contribution is weighted toward **color-
        defined form** (shape from color), **stereo-defined
        form** (V4v), and **surface segmentation by color**
        (V4d). **On the left, the form-and-object contribution
        is weighted toward the ventral-stream endpoint** —
        V4v → left LOC → **left VWFA (reading)**. This is the
        **left V4's most left-lateralized contribution** and
        the **fourth stage of the left reading pathway**.

**Left-specific caveat on `spatial_localization`.** V4 is **not**
the spatial-localization area — that is V3 and V3A. V4's role in
spatial localization is **marginal** — it contributes to the
color-defined and stereo-defined **position** of objects, but the
**full spatial-localization machinery** (motion boundaries, depth
from motion, optic flow) is V3d, V3A, and MT/V5. `spatial_
localization` is **omitted** from the V4 `FUNCTIONAL_DOMAINS`
tuple.

**Left-specific caveat on `binocular_vision`.** V4v has some
disparity-sensitive neurons, but the **fine stereopsis machinery**
is V1, V2, and V3v. V4's stereo contribution is **limited to
stereo-defined form** — the use of disparity to define shape — not
the **full stereoscopic depth perception** that V1, V2, and V3v
support. `binocular_vision` is **omitted** from the V4 `FUNCTIONAL_
DOMAINS` tuple.

**Left-specific caveat on `motion_perception`.** V4 is **not** the
motion area — that is MT/V5. `motion_perception` is **omitted**.

**Left-specific caveat on `primary_visual_processing` and
`primary_visual_processing_secondary`.** These are V1's and V2's
domains. Both are **omitted**.

**Left-specific caveat on `visual_attention`.** V4 is a **target**
of top-down attentional modulation, but it is **not** an attentional
control area. `visual_attention` is **omitted** as a primary domain.

**Left-specific caveat on `visual_word_processing`.** V4v is the
**fourth stage** of the left reading pathway (V1 → V2 → V3v → V4v
→ LOC → VWFA), but V4v itself does **not** perform word processing.
`visual_word_processing` is **omitted**.

**Left-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the left
V4 does **not** carry. `face_processing` is instantiated in the
right FFA (fed by the right V4v → LOC → right FFA pathway);
`global_visual_processing` begins at right V2. Neither appears in the
left V4 `FUNCTIONAL_DOMAINS` tuple.

**Summary**: V4 carries **exactly two** functional domains —
`color_vision` and `form_and_object_perception`. **This is the
smallest domain set of any current V area** (V1 has three on the
left / four on the right; V2 has three on the left / four on the
right; V3 has three on both; V4 has two on both). **The V4
FUNCTIONAL_DOMAINS set is IDENTICAL across hemispheres** — the left-
right differences are **emphasis-only**:

    left V4   ←  color_vision weighted toward **color-form-
                 language integration**; form_and_object_perception
                 weighted toward **left VWFA (reading)** endpoint
    right V4  ←  color_vision weighted toward **pure color
                 perception / felt aspect**; form_and_object_
                 perception weighted toward **right FFA (face)**
                 endpoint

V4 is the **most functionally specialized V area in the current
tree** — it is the **only V area whose defining contribution is a
single named visual dimension (color)**, and it is the **only V area
whose output does not include another current V area** (V4 feeds the
LOC, which is a forward reference, not a current package).

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), left — **indirect, via
          V2, V3, and V1**
            **V4's dominant input is from V2 and V3, not directly
            from the LGN or V1.** V4 has **no direct LGN
            projections** and **no direct V1 projections** — the
            relay through V2 and V3 is obligate.
        → LGN koniocellular pathway — **weak, direct**
            A **weak, direct LGN → V4 projection** exists via the
            koniocellular layers. It bypasses V1 and V2 and
            carries the **blue-yellow (S-cone) color signal**.
            This is part of the subcortical substrate that
            survives V1 lesions (blindsight for color).
        → pulvinar (modulatory, **stronger to V4 than to V1**)
            The pulvinar sends a stronger modulatory projection to
            V4 than to V1, participating in the cortico-thalamo-
            cortical loops that support visual attention and
            visual short-term memory.

    cortical afferents
        → V2, left (via **thin stripes**)
            The **V2 thin stripes** carry the color and border
            signal forward to V4. **This is V4's principal
            cortical afferent for color.**
        → V3v, left
            The **V3v → V4 relay** carries the **kinetic
            boundaries**, **shape-from-motion**, **shape-from-
            shading**, and **shape-from-texture** signals forward
            to V4. **This is V4's principal cortical afferent
            for form-from-motion.**

    cortical efferents — **the V4 → LOC output**
        → LOC, left — **forward reference**
            **V4's principal cortical target.** The **V4 → LOC
            relay** carries the color and form signal forward to
            the **lateral occipital complex** — the object-
            recognition complex of the ventral stream. **On the
            left, the LOC then feeds the left VWFA (reading)
            via the LOC → left VWFA pathway.** The V4 → LOC →
            left VWFA pathway is the **left reading pathway**,
            and V4v is its **fourth stage** after V1, V2, and
            V3v.
        → inferotemporal cortex, left (via LOC)
            V4's output reaches the inferotemporal cortex via
            the LOC, contributing to the ventral stream's object-
            recognition hierarchy. **On the left, this pathway
            terminates at the left VWFA** (reading) and the
            left anterior temporal semantic hub.
        → V4d → V4v (intra-V4)
            V4d's output reaches V4v within V4, contributing to
            the **color-form integration** that underlies V4's
            color-defined form perception.
        → V2 (feedback)
            V4 sends feedback to V2, participating in the
            cortico-cortical feedback loops that support
            figure-ground segregation and visual attention.

    callosal connections
        → right V4
            The callosal fibers connect the left V4 to the right
            V4 across the occipital midline, supporting **the
            fusion of the two hemifields** at the V4 stage and
            the **integration of color information across the
            vertical midline**.

    attentional feedback
        → frontal eye fields (BA 8), left
            The FEF sends **top-down attentional gain** to V4,
            modulating V4's responsiveness to behaviourally
            relevant color and form stimuli.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), left
            The DLPFC sends top-down attentional and working-memory
            signals to V4, supporting **color working memory**
            and **color imagery**.
        → intraparietal sulcus, left
            The IPS sends dorsal-attention-network signals to V4,
            supporting **color-based spatial attention** in the
            RIGHT visual hemifield.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in two respects:
(a) the **V4v → LOC → left VWFA pathway** is the **left reading
pathway**, and it carries the **color-form-language integration**
signal;
(b) the pulvinar → V4 loop and the FEF/IPC → V4 feedback are present
but carry the **color-form-language integration** modulation on the
left (vs the **pure color perception** modulation on the right).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_v4_right_hemiachromatopsia
        **This is the left V4 anchor par excellence.** A lesion of
        the left V4 produces **right hemiachromatopsia** — loss
        of color vision in the RIGHT half of the visual field of
        both eyes, with preserved color vision in the left
        hemifield. **The left V4 lesion spares the left
        hemifield's color perception** because the right V4 (fed
        by the right occipital lobe) is intact. **Bilateral V4
        lesions produce complete achromatopsia** — the patient
        sees the world in shades of gray. **The left V4's
        hemiachromatopsia is the mirror of the right V4's left
        hemiachromatopsia.**

    left_v4_color_agnosia
        **This is the left-lateralized V4 anchor that has no
        symmetric counterpart on the right.** **Color agnosia** —
        impaired ability to **name** or **recognize** colors
        despite intact color perception — is a **left-lateralized**
        syndrome that involves the left V4 → LOC → left VWFA →
        left language areas pathway. The patient can **match**
        colors (V4 perception is intact) but cannot **name**
        them or use them semantically. **Right V4 lesions
        produce hemiachromatopsia (perceptual deficit) but not
        color agnosia (recognition deficit) at the same
        weighting**, because the right hemisphere does not have
        the language network that color naming requires.

    left_v4_color_form_language_integration_deficit
        **The left V4's most distinctive functional anchor.**
        Left V4's V4v → LOC → left VWFA pathway is the substrate
        of **color-form-language integration** — the ability to
        name colored objects, use color in reading (e.g., colored
        letters), and integrate color with object semantics.
        Left V4 lesions can produce **color-form-language
        integration deficits** — the patient can name objects
        and colors separately but cannot integrate them in a
        linguistic context. **This anchor has no symmetric
        counterpart on the right** — the right V4's color
        contribution is weighted toward pure color perception,
        not color-form-language integration.

    left_v4_alexia_without_agraphia_left_v4_plus_splenium
        **Alexia without agraphia** (Dejerine 1892) — the patient
        can **write** but cannot **read what they have written**
        — results from a **left occipital lesion that disconnects
        the intact right occipital cortex from the left language
        areas**. The classic lesion is **left PCA infarct
        involving the left V4 (color-form) and/or the left
        V3v (form-from-motion), plus the left splenium of the
        corpus callosum**. **The V4-specific contribution is
        the left V4v damage**, which removes the left
        hemifield's color-form input to the left VWFA; the
        **splenium damage** removes the callosal relay of the
        intact right hemifield's color-form signal. **This is
        the canonical left-lateralized V4 clinical syndrome,
        and it has no symmetric counterpart on the right.**

    left_v4_color_anomia
        **A milder variant of color agnosia.** Left V4 lesions
        can produce **color anomia** — the patient can **point
        to** a named color but cannot **name** a color that is
        shown to them. This is distinguished from color agnosia
        (impaired color **recognition** even when matching is
        intact) by the preservation of color matching with
        impaired color naming. **Color anomia is left-
        lateralized** because it requires the left language
        network; **the right V4 does not carry this anchor.**

    left_v4_visual_object_agnosia_color_component
        **Visual object agnosia** — impaired ability to recognize
        objects despite intact visual perception — typically
        requires **bilateral** lesions of the ventral stream.
        **Left V4 lesions contribute to the color-related
        component** of visual object agnosia — the failure to
        use color as an object-recognition cue. **The bilateral
        requirement** means that isolated left V4 lesions
        produce a **milder** object-recognition deficit than
        bilateral V4 lesions.

    left_v4_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct**
        involving V4 produces a **right hemiachromatopsia**
        (from V4) plus a **right homonymous hemianopia or
        quadrantic defect** (from V1/V2/V3 involvement) plus,
        if the splenium is involved, **alexia without agraphia**.
        **The V4-specific contribution is the hemiachromatopsia**
        — the color loss in the right hemifield that
        distinguishes a V4-involved infarct from a V1-only one.

    left_v4_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **V1, V2, V3, AND V4**. **The V4
        contribution is the propagation of the aura into
        color-defined features** — colored fortifications,
        chromatic scotomata, and color hallucinations in
        addition to the motion and form features of V1–V3.
        **This anchor is hemisphere-invariant**, but the
        aura's field involvement is contralateral (right field
        on the left side).

    left_v4_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **V1, V2, V3, OR V4**. **V4 auras** are
        typically **dominated by color** — the patient may see
        **colored shapes, chromatic phosphenes, or colored
        fortifications** in addition to the elementary shapes
        and motion features of V1–V3. **Left V4 auras** project
        to the **right visual field** and can be preceded or
        accompanied by **hemiachromatopsia** that persists after
        the seizure.

    left_v4_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1, V2, V3, AND V4 bilaterally**
        in later stages, but early PCA affects the **dorsal and
        ventral association cortices** (V3A, V4, V5/MT+, LOC)
        more than the early V areas. **Left V4** is part of the
        substrate of the **progressive ventral stream
        dysfunction** that produces **progressive color
        agnosia** and **progressive reading deficits** in later-
        stage PCA on the left.

    left_v4_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects** from **bilateral occipital
        involvement**. **The V4 contribution** is the
        **extrastriate involvement** that produces **color
        hallucinations** and **hemiachromatopsia** (V4 partial
        loss). **The syndrome is reversible** in most cases.

**The V4-specific clinical anchors** — `left_v4_right_hemiachromatopsia`,
`left_v4_color_agnosia`, `left_v4_color_form_language_integration_
deficit`, `left_v4_alexia_without_agraphia_left_v4_plus_splenium`,
and `left_v4_color_anomia` — are the **most distinctive V4
anchors**. **Three of them** (`color_agnosia`, `color_form_language_
integration_deficit`, `color_anomia`) are **left-lateralized** and
have no symmetric counterpart on the right — they are the **most
strongly left-lateralized clinical anchors in the entire occipital
lobe**, and they reflect the left V4's unique role in **color-form-
language integration**.

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
    **Distant caudal neighbour** via V2 and V3; no direct
    adjacency.

..v2
    **Distant caudal neighbour** via V3; V2's thin stripes
    project directly to V4. **V2 and V4 are connected via the
    thin-stripe → V4 pathway**, which is one of V2's three-stripe
    output targets.

..v3
    **Caudal neighbour** via the **V3/V4 border** (retinotopic,
    not architectonic). **V3v → V4 is V4's principal cortical
    afferent for form-from-motion.** **V3 and V4 share BA 19** —
    they are the two V areas of the V1-V4 hierarchy that sit in
    the same BA.

...brodmann_areas.brodmann_area_19
    The **cytoarchitectonic counterpart — partial correspondence,
    not identity.** BA 19 spans **V3, V4, V3A, V3B, V5/MT+,
    LOC**. V4 is **one of six** V areas in BA 19. The BA 19
    package's ``V_AREA_CORRELATE`` is a **six-element tuple**.

...cuneus
    The medial-surface gyral landmark (V1's territory, not V4's).
    **V4 is not on the calcarine banks** — its representation is
    on the fusiform gyrus (V4v) and the lateral occipital
    cortex (V4d).

...gyri  (forward reference — the lingual gyrus, fusiform gyrus,
    and lateral occipital gyrus are not yet packaged at their
    full anatomical extents)
    The **fusiform gyrus** carries V4v's upper-field
    representation. **On the left, the fusiform gyrus's V4v →
    LOC → left VWFA pathway is the reading pathway.** The
    **lateral occipital gyrus** carries V4d's lower-field
    representation. **On the left, feeds the left LOC.**

...sulci.calcarine_sulcus
    The reference landmark for V1's territory. **V4 is not on
    the calcarine banks** — the calcarine sulcus is **not** a
    primary landmark for V4.

...sulci.collateral_sulcus
    The **ventral boundary of V4v** on the fusiform gyrus.

...sulci.lunate_sulcus
    The inconstant lateral-surface landmark for the V1/V2 border.
    **Not a landmark for V4.**

...sulci.transverse_occipital_sulcus
    The dorsal-surface landmark for the V3A / V3B territory. **Not
    a landmark for V4.**

..cortex.temporal
    The **ventral stream** continues from V4 (via the LOC) into
    the temporal lobe. **On the left, the ventral stream
    terminates in the left VWFA** (the reading area), and the
    left V4 is the **fourth stage** of this pathway. The
    temporal package must declare the left V4 as a source of its
    visual input via the ventral stream, and must note the
    **left-lateralized VWFA specialization**.

..cortex.parietal  — indirect
    V4's contribution to the dorsal stream is **marginal** —
    V4's color-form output feeds the LOC, not MT/V5. The
    parietal package should note the **V4 → LOC (ventral stream)**
    relationship but should **not** declare V4 as a direct
    source of dorsal-stream input.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V4.

..cortex.cingulate  — indirect
    No direct cingulate → V4 projection.

..cortex.insular  — indirect
    No direct insular → V4 projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** provides a **weak, direct koniocellular
    projection** to V4 (bypassing V1 and V2). The koniocellular
    pathway carries the **blue-yellow (S-cone) color signal**
    and is part of the subcortical substrate of blindsight for
    color.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V4
    than to V1**, participating in the cortico-thalamo-cortical
    loops that support visual attention and visual short-term
    memory.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from V4 (via the LOC) to the
    perirhinal, entorhinal, and parahippocampal cortices. **The
    left V4 is the fourth stage** of the occipito-temporal-
    hippocampal pathway.

../../subcortical/medial_temporal_lobe/amygdala
    **Weak, indirect.** V4 has **no direct amygdala projection**
    — the amygdala receives visual input via the LOC and the
    inferotemporal cortex, not via V4.

../../right/cortex/occipital/cortex/v4
    The right-hemisphere homologue. Structural fields (V-number,
    BA correlate 19, color globs, V4v / V4d distinction,
    V3/V4 border, triple mirror-flip retinotopy, FUNCTIONAL_
    DOMAINS set, forward-declaration caveat text) MUST be
    byte-identical. Functional emphasis and clinical
    significance diverge — the right V4 processes the **LEFT**
    visual hemifield, is weighted toward **pure color
    perception and the felt / phenomenal aspect of color
    experience**, and its V4v output feeds the **right LOC →
    right FFA** (face) pathway rather than the left LOC → left
    VWFA (reading) pathway.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "v4"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    V_NUMBER            = "V4"
    ALTERNATE_NAMES     = ("quaternary_visual_cortex",
                           "color_and_form_area",
                           "v4",
                           "hv4",
                           "brodmann_area_19_partial")
        # **Note "hv4"** — some parcellations call the human V4
        # "hV4" to distinguish it from monkey V4. **Note
        # "brodmann_area_19_partial"** — V4 is one of six V
        # areas in BA 19.

    ARCHITECTONIC_SIGNATURES = (
        "color_globs",
        "dysgranular_extrastriate_cortex",
        "retinotopic_boundary_v3_v4",
    )
        # **Three signatures**: **color globs** (the only
        # architectonic feature in the occipital lobe
        # specifically associated with a named visual dimension),
        # dysgranular cytoarchitecture, and the **retinotopic**
        # V3/V4 border.

    BRODMANN_CORRELATES = (19,)
        # **One BA** — but **partial correspondence** — BA 19
        # spans six V areas. V4 is one of them.

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** V4 is unique to the occipital
        # lobe.

    RETINOTOPIC_MAP     = "triple_mirror_flip_of_v1"
        # V4's retinotopic map is the **third mirror-flip** of V1
        # (V2 = flip 1, V3 = flip 2 back to V1's arrangement,
        # V4 = flip 3 reversed again). **V4's primary location is
        # the fusiform gyrus (V4v) and the lateral occipital
        # cortex (V4d)** — not the calcarine banks. **On the
        # left, the represented hemifield is the RIGHT
        # hemifield.**

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** — left V4
        # processes the RIGHT hemifield.

    FUNCTIONAL_DOMAINS  = (
                              "color_vision",
                              "form_and_object_perception",
                              # **Two domains** — the **smallest
                              # domain set of any current V
                              # area**. **Identical set on both
                              # hemispheres** (V4's domain set
                              # is hemisphere-invariant, like
                              # V3's). **V4 is the only V area
                              # whose primary domain is
                              # `color_vision`.**
                              # NOTE: spatial_localization is
                              # EXCLUDED (V3, V3A territory; V4
                              # is not a spatial-localization
                              # area).
                              # NOTE: binocular_vision is
                              # EXCLUDED (V1, V2, V3v; V4's
                              # stereo role is limited to
                              # stereo-defined form).
                              # NOTE: motion_perception is
                              # EXCLUDED (MT/V5's domain).
                              # NOTE: primary_visual_processing
                              # and primary_visual_processing_
                              # secondary are EXCLUDED (V1's
                              # and V2's domains).
                              # NOTE: visual_attention is
                              # EXCLUDED as a primary domain.
                              # NOTE: visual_word_processing is
                              # EXCLUDED (V4v is the fourth
                              # stage of the left reading
                              # pathway, not the operation).
                              # NOTE: face_processing and
                              # global_visual_processing are
                              # EXCLUDED (right-lateralized;
                              # not instantiated on the left
                              # V4).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "color_vision":
                                  "color_form_language_integration_"
                                  "right_hemiachromatopsia_color_"
                                  "agnosia_color_anomia",
                              "form_and_object_perception":
                                  "color_form_and_stereo_defined_"
                                  "form_feeding_left_loc_left_vwfa_"
                                  "reading_pathway",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_v4_right_hemiachromatopsia",
                              "left_v4_color_agnosia",
                              "left_v4_color_form_language_"
                              "integration_deficit",
                              "left_v4_alexia_without_agraphia_"
                              "left_v4_plus_splenium",
                              "left_v4_color_anomia",
                              "left_v4_visual_object_agnosia_"
                              "color_component",
                              "left_v4_occipital_infarct_pca_"
                              "territory",
                              "left_v4_migraine_visual_aura",
                              "left_v4_occipital_epilepsy_"
                              "visual_auras",
                              "left_v4_posterior_cortical_"
                              "atrophy",
                              "left_v4_pres_visual_symptoms",
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
computation that references V4 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are two forward-declaration caveats for this package.**

1. **LOC is a forward reference** — not yet a package under
   ``..cortex``. **LOC is V4's primary cortical target**, and
   the V4 → LOC → left VWFA pathway is the **left reading
   pathway**. **On the left, resolving the LOC package is the
   most urgent future resolution for the ventral stream**, and
   creating it is required for V4's clinical anchors to be fully
   characterised.

2. **V4A / V4α is a forward reference** — some parcellations
   treat the dorsal V4d as "V4A" or the ventral V4v as "V4α".
   **Not yet a package** — the current tree keeps the V4d / V4v
   distinction as a **sub-division within V4**, not as separate
   V areas. This is analogous to V3d / V3v.

**Both forward references must be resolved before V4's clinical
anchors are fully characterised** — the `color_form_language_
integration_deficit` and `alexia_without_agraphia` anchors depend
on the V4 → LOC → left VWFA pathway, and the `color_agnosia` anchor
depends on the V4 → LOC → left VWFA → left language areas pathway.
Until LOC is resolved, V4's clinical anchors describe the
**color-perception** and **color-form** deficits at the V4 stage,
not the full downstream language-linked syndromes.

**Both forward references are byte-identical to the left sibling's**
— they are properties of the V-area hierarchy, not of the
hemisphere.

**All forward-declaration caveat text is byte-identical to the left
sibling's.**

--------------------------------------------------------------------------------
PROMOTION RULE (when a V sub-field becomes a package)
--------------------------------------------------------------------------------

V4 has **one** natural sub-division: the **V4v / V4d split** —
the ventral component on the fusiform gyrus (hV4) and the dorsal
component on the lateral occipital cortex (V4d). Some parcellations
already treat them as separate areas (V4v / hV4 and V4d / V4A). **The
current tree keeps them together as "V4"**, but the promotion takes
this form if performed:

    v4/
        __init__.py
        v4v_ventral_hv4/        # → LOC, color-form → reading
            __init__.py
        v4d_dorsal_v4a/         # → LOC, color-form → object
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The V4v / V4d split is a legitimate retinotopic subdivision.** **On
the left, the V4v component is the dominant ventral-stream
contributor** — it feeds the left LOC → left VWFA (reading)
pathway, and it is the substrate for the color-form-language
integration deficit and color agnosia anchors. **The right V4v
component feeds the right LOC → right FFA (face) pathway.**

**The split preserves the BA 19 correlate**: V4v and V4d both
inherit the parent's `(19,)` `BRODMANN_CORRELATES`.

**The split requires a joint revision of BA 19's
`V_AREA_CORRELATE` entry** — if V4 is split, BA 19's correlate
becomes `("v3", "v4v", "v4d", "V3A", "V3B", "V5_MT_plus", "LOC")`
(or `("v3", "v4", "V3A", "V3B", "V5_MT_plus", "LOC")` if the BA
labeling convention treats the split as a refinement). **The exact
form must be decided hemisphere-invariantly** and applied in the same
commit as the split, in both hemispheres.

**No split should be performed while LOC is unresolved** — LOC is
V4's main downstream target, and creating it first establishes the
complete V4 downstream context.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../v4``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "v4"
        LOBE                         "occipital"
        V_NUMBER                     "V4"
        ALTERNATE_NAMES              ("quaternary_visual_cortex",
                                     "color_and_form_area",
                                     "v4",
                                     "hv4",
                                     "brodmann_area_19_partial")
        ARCHITECTONIC_SIGNATURES     (three signatures —
                                     color globs, dysgranular,
                                     retinotopic V3/V4 border)
        BRODMANN_CORRELATES          (19,)
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same triple mirror-flip
                                     structure
        FUNCTIONAL_DOMAINS set       the same two domains
                                     (color_vision, form_and_
                                     object_perception) — **V4
                                     and V3 are the two V areas
                                     whose domain sets are
                                     hemisphere-invariant**
        Bounding / overlapping territories
        V-to-neighbour adjacency
        CONNECTIVITY                 same bundle names (V2 thin
                                     stripes → V4, V3v → V4,
                                     V4 → LOC)
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — left V4 processes
                               the RIGHT hemifield; right V4
                               processes the LEFT hemifield.
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        DOMAIN_EMPHASIS        left: color_vision is "color_form_
                               language_integration_right_
                               hemiachromatopsia_color_agnosia_
                               color_anomia"; form_and_object_
                               perception is "color_form_and_
                               stereo_defined_form_feeding_left_
                               loc_left_vwfa_reading_pathway".
                               right: color_vision is "pure_
                               color_perception_felt_aspect_
                               left_hemiachromatopsia"; form_
                               and_object_perception is "color_
                               form_and_stereo_defined_form_
                               feeding_right_loc_right_ffa_face_
                               pathway".
        CONNECTIVITY           same bundle names; left: the
                               V4v → left LOC → left VWFA
                               pathway carries the color-form-
                               language integration signal.
                               right: the V4v → right LOC →
                               right FFA pathway carries the
                               pure color perception and the
                               felt aspect of color experience.
        CLINICAL_ANCHORS       left: eleven anchors (right
                               hemiachromatopsia, **color
                               agnosia**, **color-form-language
                               integration deficit**, **alexia
                               without agraphia (left V4 +
                               splenium)**, **color anomia**,
                               visual object agnosia (color
                               component), left occipital
                               infarct, migraine aura, occipital
                               epilepsy, PCA, PRES).
                               right: nine anchors (left
                               hemiachromatopsia, **pure color
                               perception deficit**, **felt
                               aspect of color loss**, **left
                               hemifield color loss without
                               agnosia**, right occipital
                               infarct, migraine aura, occipital
                               epilepsy, PCA (Benson syndrome),
                               PRES).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same V4, the same color globs,
and the same V4v / V4d distinction — but the *represented hemifield*
is **flipped**.

**The FUNCTIONAL_DOMAINS set is IDENTICAL across hemispheres.** V4
shares this property with V3 — **V3 and V4 are the only two V areas
in the current tree whose domain set is hemisphere-invariant** (V1
and V2 both have four on the right and three on the left).

**The three left-lateralized clinical anchors are the most striking
feature of this contract.** `left_v4_color_agnosia`,
`left_v4_color_form_language_integration_deficit`, and
`left_v4_color_anomia` are **left-lateralized** — they involve the
left V4 → LOC → left VWFA → left language areas pathway, and they
**have no symmetric counterpart on the right**. The right V4's
color deficit is **perceptual only** (hemiachromatopsia), not
**language-linked** (color agnosia). **This is the sharpest
functional asymmetry in the entire occipital lobe**, and it reflects
the left hemisphere's unique role in color-form-language
integration.

**The V4v / V4d split is a shared structural fact.** Both
hemispheres carry the same split, but the **downstream target**
differs — **left V4v → left LOC → left VWFA (reading)**, **right
V4v → right LOC → right FFA (face)**.

**The two-domain FUNCTIONAL_DOMAINS set is the smallest in the V1-V4
hierarchy.** V4 is the **most functionally specialized** V area —
it is the **only V area whose primary domain includes
`color_vision`**, and it is the **only V area whose output does not
include another current V area** (V4 feeds the LOC, a forward
reference).

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "v4".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V4".
[ ] ALTERNATE_NAMES includes "quaternary_visual_cortex",
    "color_and_form_area", "v4", "hv4", and
    **"brodmann_area_19_partial"** — V4 is one of **six** V areas
    in BA 19.
[ ] ARCHITECTONIC_SIGNATURES includes the **three** signatures:
    **color globs**, dysgranular extrastriate cortex, and the
    **retinotopic** V3/V4 border.
[ ] BRODMANN_CORRELATES is exactly ``(19,)`` — **one BA**, but
    **partial correspondence** — six V areas share BA 19.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **triple mirror-flip** structure:
    - V4 is the third mirror-flip of V1
    - V4's primary location is the **fusiform gyrus (V4v)** and
      the **lateral occipital cortex (V4d)** — not the
      calcarine banks
    - **represented hemifield = RIGHT hemifield on the left side**
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] FUNCTIONAL_DOMAINS contains **two** domains:
    - color_vision
    - form_and_object_perception
[ ] **The FUNCTIONAL_DOMAINS set is verified to be IDENTICAL across
    hemispheres** — V4 shares this property with V3 (the two
    hemisphere-invariant domain sets in the current tree).
[ ] **`color_vision` is V4's defining contribution and the only V
    area in the V1–V4 hierarchy whose primary domain includes
    `color_vision`.**
[ ] FUNCTIONAL_DOMAINS **excludes** spatial_localization (V3,
    V3A territory).
[ ] FUNCTIONAL_DOMAINS **excludes** binocular_vision (V1, V2,
    V3v; V4's stereo role is limited to stereo-defined form).
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (MT/V5's
    domain).
[ ] FUNCTIONAL_DOMAINS **excludes** primary_visual_processing and
    primary_visual_processing_secondary (V1's and V2's domains).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a primary
    domain.
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing (V4v
    is the fourth stage of the left reading pathway, not the
    operation).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing (right-lateralized).
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis**:
    - color_vision → color_form_language_integration_right_
      hemiachromatopsia_color_agnosia_color_anomia
    - form_and_object_perception → color_form_and_stereo_defined_
      form_feeding_left_loc_left_vwfa_reading_pathway
[ ] CONNECTIVITY documents:
    - V2 (thin stripes) → V4 (color/border)
    - V3v → V4 (form-from-motion)
    - LGN koniocellular direct-to-V4 (weak; S-cone blue-yellow
      color; survives V1 lesions)
    - Pulvinar afferent (stronger to V4 than to V1)
    - **V4 → LOC** (principal cortical target, feeding left
      VWFA reading pathway)
    - **V4v → left LOC → left VWFA** pathway (the left reading
      pathway, with V4v being its fourth stage)
    - **V4d → V4v intra-V4 relay** (color-form integration)
    - V4 → V2 feedback (figure-ground segregation)
    - Callosal connections to right V4 (color integration across
      the vertical midline)
    - Attentional feedback from left FEF, left DLPFC, left IPS
[ ] CLINICAL_ANCHORS contains the eleven left-specific anchors:
    - left_v4_right_hemiachromatopsia
    - **left_v4_color_agnosia**
    - **left_v4_color_form_language_integration_deficit**
    - **left_v4_alexia_without_agraphia_left_v4_plus_splenium**
    - **left_v4_color_anomia**
    - left_v4_visual_object_agnosia_color_component
    - left_v4_occipital_infarct_pca_territory
    - left_v4_migraine_visual_aura
    - left_v4_occipital_epilepsy_visual_auras
    - left_v4_posterior_cortical_atrophy
    - left_v4_pres_visual_symptoms
[ ] The **right hemiachromatopsia** is documented as the primary
    left V4 anchor — the canonical color loss in the right
    hemifield.
[ ] **Color agnosia** is documented as a **left-lateralized**
    anchor — impaired color **naming** despite intact color
    perception, requiring the left V4 → LOC → left VWFA → left
    language areas pathway.
[ ] **Color-form-language integration deficit** is documented as
    a **left-lateralized** anchor — impaired ability to use
    color in a linguistic context, requiring the left V4v →
    LOC → left VWFA pathway.
[ ] **Alexia without agraphia (left V4 + splenium)** is
    documented as the canonical left-lateralized reading deficit
    that requires V4 involvement — the left V4v damage removes
    the right-hemifield color-form input to the left VWFA, and
    the splenium damage removes the callosal relay of the
    left-hemifield signal.
[ ] **Color anomia** is documented as a **left-lateralized**
    anchor — a milder variant of color agnosia.
[ ] The **fusiform gyrus (V4v)** and **lateral occipital gyrus
    (V4d)** are documented as V4's primary anatomical components
    — **V4 is not on the calcarine banks**.
[ ] The **color globs** are documented as the **only
    architectonic feature in the occipital lobe specifically
    associated with a named visual dimension** (color).
[ ] The **triple mirror-flip** is documented — V4's map is the
    third mirror-flip of V1, and its physical location (fusiform
    / lateral occipital) is different from V1, V2, and V3.
[ ] The **V4v / V4d split** is documented, with the different
    downstream targets (V4v → left VWFA reading, V4d → left LOC
    object).
[ ] The **V4v → left LOC → left VWFA** pathway is documented as
    the left reading pathway, with V4v being its fourth stage.
[ ] **The two forward references — LOC and V4A / V4α** — are
    documented, and the **resolution rule** is recorded. Both
    are byte-identical to the left sibling's.
[ ] No SUBDIVISIONS promotion is performed while LOC is
    unresolved.
[ ] The **promotion rule for V4 → V4v + V4d** is documented,
    with the joint BA 19 update requirement, the
    hemisphere-invariant labeling convention, and the
    downstream LOC prerequisite.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, **FUNCTIONAL_DOMAINS set**, forward-declaration
    caveat text) match the left sibling; VISUAL_HEMIFIELD,
    DOMAIN_EMPHASIS (color-form-language integration vs pure
    color perception; left VWFA vs right FFA endpoint),
    CONNECTIVITY emphasis, and CLINICAL_ANCHORS deliberately
    differ.
[ ] **The visual-hemifield asymmetry is verified**: the left V4
    carries "right_hemifield" in its DOMAIN_EMPHASIS entries and
    RETINOTOPIC_MAP; the right V4 carries "left_hemifield."
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — V4 and V3 are the only two V areas
    with hemisphere-invariant domain sets.
[ ] **The three left-lateralized clinical anchors are verified**:
    `left_v4_color_agnosia`, `left_v4_color_form_language_
    integration_deficit`, and `left_v4_color_anomia` are
    present on the left and **absent** on the right (or present
    with a different weighting). **These are the sharpest
    functional asymmetries in the entire occipital lobe.**
[ ] **The two-domain FUNCTIONAL_DOMAINS set is verified** —
    V4 has the smallest domain set in the V1-V4 hierarchy.
[ ] **The `color_vision` domain is verified to be V4's
    defining contribution and unique to V4 in the V1–V4
    hierarchy.**
[ ] Any downstream code querying "what does the left V4 see?"
    must receive "the RIGHT visual hemifield."
[ ] Any downstream code querying "what is V4?" must receive
    "the quaternary visual cortex / color and form area / V4
    / hV4 / part of BA 19" — the partial correspondence with
    BA 19 (one of six V areas) is enforced.
[ ] Any downstream code querying "which V area carries
    `color_vision`?" must receive "V4 (the only V1–V4 area
    with it)."
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** V1 → V2 → V3v → V4v → LOC →
    left VWFA chain — the left V4v is the fourth stage.
[ ] Any downstream code assigning the right face pathway must
    route through the **right** V1 → V2 → V3v → V4v → LOC →
    right FFA chain.
[ ] Any downstream code assigning **color agnosia** must
    weight the left V4 more heavily — the left is the side with
    the language-linked color-recognition deficit.
[ ] Any downstream code assigning **color-form-language
    integration** must weight the left V4 more heavily — the
    left is the side with the VWFA-linked color-use deficit.
[ ] Any downstream code querying "what is the minimum domain
    set among V1–V4?" must receive "V4 (two domains: color_
    vision and form_and_object_perception) — the most
    functionally specialized V area."
"""