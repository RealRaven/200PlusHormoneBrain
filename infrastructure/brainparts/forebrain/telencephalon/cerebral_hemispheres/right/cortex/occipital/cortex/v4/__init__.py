"""
Quaternary Visual Cortex (V4) — Right Hemisphere
=================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── v4   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the right
hemisphere's **V4** — the **quaternary visual cortex**, the **color and
form area**, and the **fourth step of the V1 → V2 → V3 → V4 hierarchy**.
It is the **first V area in the hierarchy whose defining functional
contribution is a single, named visual dimension** (color), and the
**first V area whose primary output is not another occipital V area
but the lateral occipital complex (LOC)** — the gateway to the ventral
stream's object-recognition machinery.

Parent: ``..cortex`` (right occipital functional / V-numbered parent)
— sibling to V1, V2, V3. **Sibling — not parent —** of
``...brodmann_areas/brodmann_area_19``, which sits at the
``..brodmann_areas`` parent level. The V4 / BA 19 relationship is
**partial correspondence, not nesting** — BA 19 spans **V3, V4, V3A,
V3B, V5/MT+, and LOC**, so V4 is **one of six** V areas that share
BA 19.

This package is the **structural mirror** of
``../../left/cortex/occipital/cortex/v4``. The V-number, the BA
correlate (19, shared with five other V areas), the architectonic
signature (color globs), the V3/V4 border, the retinotopic triple
mirror-flip, and the two-domain functional set are identical on both
sides; the **functional emphasis** and **clinical significance**
diverge — on the right, V4 is weighted toward **pure color perception
and the felt / phenomenal aspect of color experience**, its **LOC**
output feeds the **right FFA (face)** endpoint, and right V4 lesions
produce **left hemiachromatopsia** without the language-linked color
deficits (no color agnosia, no color anomia, no color-form-language
integration deficit), plus a **contribution to prosopagnosia** via
the right V4v → LOC → right FFA pathway. On the left, V4 is weighted
toward **color-form-language integration**, its **LOC** output feeds
the **left VWFA (reading)** endpoint, and left V4 lesions produce
**color agnosia**, **color-form-language integration deficits**,
**color anomia**, and — when the lesion extends into the splenium —
**alexia without agraphia**.

**The defining structural fact about V4** is that it is the **second
V area in the hierarchy whose BA correlate is a partial
correspondence** — BA 19 spans six V areas, and V4 is the **first of
them in the V1–V4 hierarchy** (V3 is the second, sharing BA 19 with
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
                        **stereo-defined form**. **On the right,
                        V4v feeds the right LOC → right FFA
                        (face) pathway via its color-form
                        output, and it also feeds the felt /
                        phenomenal aspect of color experience.**

    V4d (or V4)         the **dorsal component**, on the **lateral
                        occipital cortex**. Represents the **lower**
                        visual field. Functionally weighted toward
                        **color-form interaction**, **shape from
                        color**, and **surface segmentation by
                        color**. **On the right, V4d's output
                        feeds the right LOC for general object
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

**Right-hemisphere specificity**: the right V4 processes the **LEFT**
visual hemifield of both eyes. Its **V4v** output feeds the **right
V4v → LOC → right FFA (face)** pathway — the right V4 is the
**fourth stage of the right face-recognition pathway** after V1, V2,
and V3v. Its **V4d** output feeds the right LOC for general object
recognition. The right V4 is weighted toward **pure color
perception** and the **felt / phenomenal aspect of color
experience** — the qualitative "what it is like" to see a color, in
the sense of the phenomenal character of color experience, which is
more strongly right-lateralized in the neuropsychological literature
(as distinct from the language-linked color naming that is left-
lateralized). **The right V4's color deficit is perceptual only**
— hemiachromatopsia — and it is **not** accompanied by color agnosia
or color anomia, because the right hemisphere does not have the
language network that color naming and color semantics require. The
right V4 does **not** carry the left-lateralized **color-form-
language integration** function; instead, it carries the **pure
color perception / felt aspect** function.

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
            Hue, saturation, stereo-defined form. **On the right,
            feeds the right LOC → right FFA (face) pathway, and
            contributes to the felt / phenomenal aspect of
            color experience.**
        V4d — dorsal component
            Lower-field representation on the lateral occipital
            cortex. Color-form interaction, shape from color,
            surface segmentation. **On the right, feeds the right
            LOC for object recognition.**
        color globs — architectonic signature
            Modular clusters of hue-selective neurons. The
            anatomical basis of V4's **color perception** role,
            and the **only architectonic feature in the occipital
            lobe specifically associated with a named visual
            dimension**.
        fusiform gyrus — ventral component (V4v)
            The fusiform gyrus carries V4v's upper-field
            representation. **On the right, the fusiform gyrus's
            V4v → LOC → right FFA pathway is the face-recognition
            pathway.** (Forward reference in ``..gyri`` — not
            yet a package.)
        lateral occipital gyrus — dorsal component (V4d)
            The lateral occipital gyrus carries V4d's lower-field
            representation and its lateral extent. **On the
            right, feeds the right LOC.**
        right fusiform face area (FFA) — downstream ventral-
        stream target
            **Right-specific overlay.** The right V4v's output —
            via the LOC — terminates in the right FFA. The
            V4v → LOC → FFA pathway is the **right face-
            recognition pathway**, and V4v is its **fourth stage**
            after V1, V2, and V3v. **The right V4v → LOC →
            right FFA pathway is the anatomical substrate of the
            right face-recognition system**, and it does **not**
            carry the left-lateralized color-form-language
            integration.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours, the V4v / V4d distinction, the color globs,
and the fusiform / lateral-occipital / collateral-sulcus overlays are
the same on both sides. What differs is the **visual hemifield** —
the right V4 processes the LEFT hemifield — and the **downstream
target emphasis** — the right V4v → LOC → **right FFA (face)**, the
left V4v → LOC → **left VWFA (reading)**.

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
                                           and V3 share BA 19.**
    V4A  (forward reference)               **Dorsal / lateral
                                           neighbour** — some
                                           parcellations treat V4d
                                           as "V4A" (a distinct
                                           area). **Not yet a
                                           package**.
    V3A  (forward reference)               **Dorsal rostral neighbour**
                                           — not yet a package.
    V5 / MT+  (forward reference)          **Dorsal / lateral
                                           neighbour** — not yet a
                                           package.
    LOC  (forward reference)               **Rostral neighbour** — not
                                           yet a package. **V4's
                                           primary output target**
                                           (via V4v and V4d). **On
                                           the right, LOC is the
                                           occipital input to the
                                           right FFA (faces).**
    BA 19                                  **Shared with V3, V3A,
                                           V3B, V5/MT+, LOC** — V4
                                           is one of six V areas
                                           that span BA 19.
    fusiform gyrus (medial-surface          carries V4v's upper-field
    gyrus; forward reference in ..gyri)    representation (**upper
                                           LEFT field on the
                                           right**).
    lateral occipital gyrus                carries V4d's lower-field
                                           representation (**lower
                                           LEFT field on the
                                           right**). **On the
                                           right, feeds the right
                                           LOC.**
    collateral sulcus                      the ventral boundary of
                                           V4v on the fusiform gyrus.

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized. The field labels (LEFT vs RIGHT) in the
fusiform and lateral occipital gyrus entries are updated for the
right hemisphere, and the LOC note is updated to point to the right
FFA endpoint.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

V4 participates in **two** canonical occipital functional domains —
the **smallest domain set of any current V area**. The set is
**identical to the left's** — this is one of the **two hemisphere-
invariant V-area domain sets** (the other is V3's). The right-side
emphasis is as follows:

    color_vision                                   (right emphasis — PRIMARY)
        **This is V4's defining contribution — and the only V
        area in the V1–V4 hierarchy whose primary domain includes
        color_vision.** V4's **color globs** are the anatomical
        substrate of hue perception, saturation perception, and
        **color-form interaction**. **On the right, V4's color
        contribution is weighted toward pure color perception
        and the felt / phenomenal aspect of color experience**
        — the qualitative "what it is like" to see a color, which
        is more strongly right-lateralized than the language-
        linked color naming that is left-lateralized. **Right V4
        lesions produce left hemiachromatopsia** — loss of color
        vision in the left hemifield — **without color agnosia,
        color anomia, or color-form-language integration
        deficits**, because the right hemisphere does not have
        the language network that color naming and color
        semantics require.

    form_and_object_perception                     (right emphasis — PRIMARY)
        **This is V4's second defining contribution.**
        V4v and V4d contribute to the **early-to-mid stages of
        form and object processing** that continue in the LOC.
        V4's form contribution is weighted toward **color-
        defined form** (shape from color), **stereo-defined
        form** (V4v), and **surface segmentation by color**
        (V4d). **On the right, the form-and-object contribution
        is weighted toward the ventral-stream endpoint** —
        V4v → right LOC → **right FFA (face)**. This is the
        **right V4's most right-lateralized contribution** and
        the **fourth stage of the right face-recognition
        pathway**.

**Right-specific caveat on `spatial_localization`.** V4 is **not**
the spatial-localization area — that is V3 and V3A. `spatial_
localization` is **omitted**.

**Right-specific caveat on `binocular_vision`.** V4v has some
disparity-sensitive neurons, but the **fine stereopsis machinery**
is V1, V2, and V3v. V4's stereo contribution is **limited to
stereo-defined form**. `binocular_vision` is **omitted**.

**Right-specific caveat on `motion_perception`.** V4 is **not** the
motion area — that is MT/V5. `motion_perception` is **omitted**.

**Right-specific caveat on `primary_visual_processing` and
`primary_visual_processing_secondary`.** These are V1's and V2's
domains. Both are **omitted**.

**Right-specific caveat on `visual_attention`.** V4 is a **target**
of top-down attentional modulation. `visual_attention` is
**omitted** as a primary domain.

**Right-specific caveat on `visual_word_processing` and `local_
featural_processing`.** These are **left-lateralized** functions
that the right V4 does **not** carry. `visual_word_processing` is
instantiated in the left VWFA (fed by the left V4v → LOC → left
VWFA pathway); `local_featural_processing` is a left-hemisphere
emphasis. Neither appears in the right V4 `FUNCTIONAL_DOMAINS`
tuple.

**Right-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the
**right V4 supports as an input stage** but does **not** carry as
primary functional domains. `face_processing` is instantiated in the
right FFA (fed by the right V4v → LOC → right FFA pathway);
`global_visual_processing` begins at right V2. Neither appears in
the right V4 `FUNCTIONAL_DOMAINS` tuple — **but the right V4v is the
fourth stage of the right face pathway**, and right V4 lesions can
contribute to face-processing deficits (prosopagnosia) when the
downstream FFA is also affected.

**Summary**: V4 carries **exactly two** functional domains —
`color_vision` and `form_and_object_perception`. **This is the
smallest domain set of any current V area** (V1 has three on the
left / four on the right; V2 has three on the left / four on the
right; V3 has three on both; V4 has two on both). **The V4
FUNCTIONAL_DOMAINS set is IDENTICAL across hemispheres** — the left-
right differences are **emphasis-only**:

    right V4  ←  color_vision weighted toward **pure color
                 perception / felt aspect**; form_and_object_
                 perception weighted toward **right FFA (face)**
                 endpoint
    left V4   ←  color_vision weighted toward **color-form-
                 language integration**; form_and_object_perception
                 weighted toward **left VWFA (reading)** endpoint

V4 is the **most functionally specialized V area in the current
tree** — it is the **only V area whose defining contribution is a
single named visual dimension (color)**, and it is the **only V area
whose output does not include another current V area** (V4 feeds the
LOC, which is a forward reference, not a current package).

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), right — **indirect, via
          V2, V3, and V1**
            **V4's dominant input is from V2 and V3, not directly
            from the LGN or V1.** V4 has **no direct LGN
            projections** and **no direct V1 projections** — the
            relay through V2 and V3 is obligate.
        → LGN koniocellular pathway — **weak, direct**
            A **weak, direct LGN → V4 projection** exists via the
            koniocellular layers. It bypasses V1 and V2 and
            carries the **blue-yellow (S-cone) color signal**.
        → pulvinar (modulatory, **stronger to V4 than to V1**)
            The pulvinar sends a stronger modulatory projection to
            V4 than to V1.

    cortical afferents
        → V2, right (via **thin stripes**)
            The **V2 thin stripes** carry the color and border
            signal forward to V4.
        → V3v, right
            The **V3v → V4 relay** carries the **kinetic
            boundaries**, **shape-from-motion**, **shape-from-
            shading**, and **shape-from-texture** signals forward
            to V4.

    cortical efferents — **the V4 → LOC output**
        → LOC, right — **forward reference**
            **V4's principal cortical target.** The **V4 → LOC
            relay** carries the color and form signal forward to
            the **lateral occipital complex** — the object-
            recognition complex of the ventral stream. **On the
            right, the LOC then feeds the right FFA (face) via
            the LOC → right FFA pathway.** The V4 → LOC →
            right FFA pathway is the **right face-recognition
            pathway**, and V4v is its **fourth stage** after V1,
            V2, and V3v.
        → inferotemporal cortex, right (via LOC)
            V4's output reaches the inferotemporal cortex via
            the LOC. **On the right, this pathway terminates at
            the right FFA (faces)** and the right anterior
            temporal semantic hub.
        → V4d → V4v (intra-V4)
            V4d's output reaches V4v within V4, contributing to
            the **color-form integration** that underlies V4's
            color-defined form perception.
        → V2 (feedback)
            V4 sends feedback to V2, participating in the
            cortico-cortical feedback loops that support
            figure-ground segregation and visual attention.

    callosal connections
        → left V4
            The callosal fibers connect the right V4 to the left
            V4 across the occipital midline, supporting **the
            fusion of the two hemifields** at the V4 stage and
            the **integration of color information across the
            vertical midline**.

    attentional feedback
        → frontal eye fields (BA 8), right
            **Right-emphasized.** The right FEF is the dominant
            node of the right ventral attention network and sends
            strong **top-down and bottom-up attentional gain** to
            right V4.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), right
            The right DLPFC sends top-down attentional and
            working-memory signals to V4, supporting **color
            working memory** and **color imagery**.
        → intraparietal sulcus, right
            **Right-emphasized.** The right IPS sends dorsal-
            attention-network signals to V4, supporting
            **color-based spatial attention** in the LEFT visual
            hemifield.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in two respects:
(a) the **V4v → right LOC → right FFA pathway** is the **right face-
recognition pathway**;
(b) the pulvinar → V4 loop and the FEF/IPS → V4 feedback carry
**pure color perception** modulation on the right (vs the
**color-form-language integration** modulation on the left).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_v4_left_hemiachromatopsia
        **This is the right V4 anchor par excellence.** A lesion of
        the right V4 produces **left hemiachromatopsia** — loss
        of color vision in the LEFT half of the visual field of
        both eyes, with preserved color vision in the right
        hemifield. **The right V4 lesion spares the right
        hemifield's color perception** because the left V4 (fed
        by the left occipital lobe) is intact. **Bilateral V4
        lesions produce complete achromatopsia** — the patient
        sees the world in shades of gray. **The right V4's
        hemiachromatopsia is the mirror of the left V4's right
        hemiachromatopsia.**

    right_v4_pure_color_perception_deficit
        **The right V4's most distinctive functional anchor.**
        The right V4 is weighted toward **pure color perception**
        — the qualitative "what it is like" to see a color — in
        a way that the left V4 is not. **Right V4 lesions can
        produce a specific deficit in the phenomenal / felt
        aspect of color experience** — the patient still
        perceives that a color is present and can match colors
        (V4 perception is intact), but the **vividness** or
        **phenomenal character** of the color experience is
        reduced. **This anchor has no symmetric counterpart on
        the left** — the left V4's dominant function is
        color-form-language integration, not pure phenomenal
        color.

    right_v4_contribution_to_prosopagnosia
        **Right-emphasized.** Right V4v is the **fourth stage**
        (after V1, V2, and V3v) of the right ventral stream that
        feeds the right FFA, and **right occipito-temporal
        lesions** that involve the right FFA or its input pathway
        produce **prosopagnosia**. **Isolated right V4 lesions
        do not produce prosopagnosia** — the right FFA is spared
        — but the right V4v is part of the **occipital input
        pathway** of the right-lateralized face-recognition
        system. **This anchor has no symmetric counterpart on
        the left** — the left V4 feeds the left VWFA (reading),
        not a prosopagnosia pathway.

    right_v4_no_color_agnosia
        **This is a right-specific ABSENCE anchor — the mirror of
        the left's `color_agnosia` anchor.** **Right V4 lesions
        do NOT produce color agnosia** — the patient can match
        colors, and, because the right hemisphere does not have
        the language network required for color naming and
        color semantics, the right V4 lesion does not produce
        the language-linked color-recognition deficit that a
        left V4 lesion does. **The right V4's color deficit is
        perceptual only** (hemiachromatopsia), not
        language-linked (color agnosia). **This absence is the
        sharpest structural asymmetry in the V4 clinical
        anchors** — it is the mirror-opposite of the left's
        presence.

    right_v4_no_color_anomia
        **This is a right-specific ABSENCE anchor.** **Right V4
        lesions do NOT produce color anomia** — the patient can
        name colors (using the intact left language network),
        and the right V4 lesion does not produce the naming
        deficit. **Color anomia is left-lateralized** and is
        absent from the right V4 clinical anchors.

    right_v4_no_color_form_language_integration_deficit
        **This is a right-specific ABSENCE anchor.** **Right V4
        lesions do NOT produce color-form-language integration
        deficits** — the patient can use color in a linguistic
        context (using the intact left V4v → LOC → left VWFA
        pathway), and the right V4 lesion does not produce the
        integration deficit. **Color-form-language integration
        is left-lateralized** and is absent from the right V4
        clinical anchors.

    right_v4_visual_object_agnosia_color_component
        **Visual object agnosia** — impaired ability to recognize
        objects despite intact visual perception — typically
        requires **bilateral** lesions of the ventral stream.
        **Right V4 lesions contribute to the color-related
        component** of visual object agnosia — the failure to
        use color as an object-recognition cue. **The bilateral
        requirement** means that isolated right V4 lesions
        produce a **milder** object-recognition deficit than
        bilateral V4 lesions.

    right_v4_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct**
        involving V4 produces a **left hemiachromatopsia**
        (from V4) plus a **left homonymous hemianopia or
        quadrantic defect** (from V1/V2/V3 involvement). **The
        V4-specific contribution is the hemiachromatopsia** —
        the color loss in the left hemifield that distinguishes
        a V4-involved infarct from a V1-only one. **Isolated
        right PCA infarcts do not produce alexia without
        agraphia** — that syndrome is left-lateralized.

    right_v4_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **V1, V2, V3, AND V4**. **The V4
        contribution is the propagation of the aura into
        color-defined features** — colored fortifications,
        chromatic scotomata, and color hallucinations. **This
        anchor is hemisphere-invariant**, but the aura's field
        involvement is contralateral (left field on the right
        side).

    right_v4_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **V1, V2, V3, OR V4**. **V4 auras** are
        typically **dominated by color** — the patient may see
        **colored shapes, chromatic phosphenes, or colored
        fortifications**. **Right V4 auras** project to the
        **left visual field** and can be preceded or accompanied
        by **hemiachromatopsia** that persists after the
        seizure.

    right_v4_posterior_cortical_atrophy_benson_syndrome
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1, V2, V3, AND V4 bilaterally**
        in later stages. **Right V4** is part of the substrate
        of the **progressive ventral stream dysfunction** that
        produces **Benson syndrome** — the right-lateralized
        clinical presentation with **progressive prosopagnosia,
        visuospatial deficits, optic ataxia, simultanagnosia**,
        and **progressive color perception deficits**. **On
        the right, PCA presents with the visuospatial /
        prosopagnosic syndrome**; on the left, with the
        progressive color agnosia and reading deficits.

    right_v4_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects** from **bilateral occipital
        involvement**. **The V4 contribution** is the
        **extrastriate involvement** that produces **color
        hallucinations** and **hemiachromatopsia** (V4 partial
        loss). **The syndrome is reversible** in most cases.

**The V4-specific clinical anchors** — `right_v4_left_
hemiachromatopsia`, `right_v4_pure_color_perception_deficit`,
`right_v4_contribution_to_prosopagnosia`, and the three
**right-specific absence anchors** (`right_v4_no_color_agnosia`,
`right_v4_no_color_anomia`, `right_v4_no_color_form_language_
integration_deficit`) — are the **right-emphasized mirror** of the
left V4 anchors. **The three absence anchors are the sharpest
structural asymmetry in the V4 clinical anchors** — they document
that the left V4's three language-linked color anchors (color
agnosia, color-form-language integration deficit, color anomia) are
**left-only** and are **explicitly absent from the right V4**.

**The `right_v4_pure_color_perception_deficit` and
`right_v4_contribution_to_prosopagnosia` are the two positive
right-only anchors** — the first captures the right V4's unique
contribution to the phenomenal aspect of color experience, and the
second captures its role in the right face-recognition pathway.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..cortex  (parent)
    The right occipital functional / V-numbered parent.

..primary_visual_cortex  (V1)
    **Distant caudal neighbour** via V2 and V3; no direct
    adjacency.

..v2
    **Distant caudal neighbour** via V3; V2's thin stripes
    project directly to V4.

..v3
    **Caudal neighbour** via the **V3/V4 border** (retinotopic).
    **V3v → V4 is V4's principal cortical afferent for form-from-
    motion.** **V3 and V4 share BA 19.**

...brodmann_areas.brodmann_area_19
    The **cytoarchitectonic counterpart — partial correspondence,
    not identity.** BA 19 spans **V3, V4, V3A, V3B, V5/MT+,
    LOC**. V4 is **one of six** V areas in BA 19.

...cuneus
    The medial-surface gyral landmark (V1's territory, not V4's).
    **V4 is not on the calcarine banks** — its representation is
    on the fusiform gyrus (V4v) and the lateral occipital
    cortex (V4d).

...gyri  (forward reference — the fusiform gyrus and lateral
    occipital gyrus are not yet packaged at their full
    anatomical extents)
    The **fusiform gyrus** carries V4v's upper-field
    representation. **On the right, the fusiform gyrus's V4v →
    LOC → right FFA pathway is the face-recognition pathway.**
    The **lateral occipital gyrus** carries V4d's lower-field
    representation. **On the right, feeds the right LOC.**

...sulci.calcarine_sulcus
    The reference landmark for V1's territory. **V4 is not on
    the calcarine banks.**

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
    the temporal lobe. **On the right, the ventral stream
    terminates in the right FFA** (the face area), and the
    right V4 is the **fourth stage** of this pathway. **Right
    occipito-temporal lesions produce prosopagnosia** — the
    canonical right-lateralized visual-recognition deficit.
    The temporal package must declare the right V4 as a source
    of its visual input via the ventral stream, and must note
    the **right-lateralized FFA specialization**.

..cortex.parietal  — indirect
    V4's contribution to the dorsal stream is **marginal** —
    V4's color-form output feeds the LOC, not MT/V5. The
    parietal package should note the **V4 → LOC (ventral
    stream)** relationship but should **not** declare V4 as a
    direct source of dorsal-stream input.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V4. **On the right, the right FEF is the
    dominant node of the ventral attention network**, and right
    frontal lesions contribute to left hemispatial neglect.

..cortex.cingulate  — indirect
    No direct cingulate → V4 projection.

..cortex.insular  — indirect
    No direct insular → V4 projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** provides a **weak, direct koniocellular
    projection** to V4 (bypassing V1 and V2). The koniocellular
    pathway carries the **blue-yellow (S-cone) color signal**.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V4
    than to V1**.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from V4 (via the LOC) to the
    perirhinal, entorhinal, and parahippocampal cortices. **On
    the right, the parahippocampal place area (PPA) and the
    retrosplenial complex receive visual input supporting scene
    and spatial memory**, which are more strongly right-
    lateralized.

../../subcortical/medial_temporal_lobe/amygdala
    **Weak, indirect.** V4 has **no direct amygdala projection**
    — the amygdala receives visual input via the LOC and the
    inferotemporal cortex, not via V4.

../../left/cortex/occipital/cortex/v4
    The left-hemisphere homologue. Structural fields (V-number,
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
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    V_NUMBER            = "V4"
    ALTERNATE_NAMES     = ("quaternary_visual_cortex",
                           "color_and_form_area",
                           "v4",
                           "hv4",
                           "brodmann_area_19_partial")
        # **Byte-identical to the left sibling's.**

    ARCHITECTONIC_SIGNATURES = (
        "color_globs",
        "dysgranular_extrastriate_cortex",
        "retinotopic_boundary_v3_v4",
    )
        # **Byte-identical to the left sibling's.**

    BRODMANN_CORRELATES = (19,)
        # **One BA** — partial correspondence. **Byte-identical
        # to the left sibling's.**

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** Byte-identical.

    RETINOTOPIC_MAP     = "triple_mirror_flip_of_v1"
        # The map's *structure* is identical to the left's.
        # **On the right, the represented hemifield is the LEFT
        # hemifield.**

    VISUAL_HEMIFIELD    = "left"
        # **The represented visual hemifield** — right V4
        # processes the LEFT hemifield.

    FUNCTIONAL_DOMAINS  = (
                              "color_vision",
                              "form_and_object_perception",
                              # **Two domains** — the **smallest
                              # domain set of any current V
                              # area**, and **identical set on
                              # both hemispheres**. **V4 shares
                              # the hemisphere-invariant domain-
                              # set property with V3.** V4 is the
                              # only V area whose primary domain
                              # includes `color_vision`.
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "color_vision":
                                  "pure_color_perception_felt_"
                                  "aspect_left_hemiachromatopsia",
                              "form_and_object_perception":
                                  "color_form_and_stereo_defined_"
                                  "form_feeding_right_loc_right_"
                                  "ffa_face_pathway",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_v4_left_hemiachromatopsia",
                              "right_v4_pure_color_perception_"
                              "deficit",
                              "right_v4_contribution_to_"
                              "prosopagnosia",
                              "right_v4_no_color_agnosia",
                              "right_v4_no_color_anomia",
                              "right_v4_no_color_form_language_"
                              "integration_deficit",
                              "right_v4_visual_object_agnosia_"
                              "color_component",
                              "right_v4_occipital_infarct_pca_"
                              "territory",
                              "right_v4_migraine_visual_aura",
                              "right_v4_occipital_epilepsy_"
                              "visual_auras",
                              "right_v4_posterior_cortical_"
                              "atrophy_benson_syndrome",
                              "right_v4_pres_visual_symptoms",
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
   the V4 → LOC → right FFA pathway is the **right face-
   recognition pathway**. **On the right, resolving the LOC
   package is the most urgent future resolution for the
   ventral stream**, and creating it is required for V4's
   clinical anchors to be fully characterised (specifically the
   `right_v4_contribution_to_prosopagnosia` anchor).

2. **V4A / V4α is a forward reference** — some parcellations
   treat the dorsal V4d as "V4A" or the ventral V4v as "V4α".
   **Not yet a package** — the current tree keeps the V4d / V4v
   distinction as a **sub-division within V4**, not as separate
   V areas.

**Both forward references must be resolved before V4's clinical
anchors are fully characterised** — **on the right, resolving LOC
is the priority**, because the right V4v → LOC → right FFA pathway
is the substrate of the prosopagnosia contribution anchor.

**Both forward references are byte-identical to the left
sibling's** — they are properties of the V-area hierarchy, not of
the hemisphere.

**All forward-declaration caveat text is byte-identical to the left
sibling's.**

--------------------------------------------------------------------------------
PROMOTION RULE (when a V sub-field becomes a package)
--------------------------------------------------------------------------------

V4 has **one** natural sub-division: the **V4v / V4d split**. The
promotion takes this form if performed:

    v4/
        __init__.py
        v4v_ventral_hv4/        # → LOC, color-form → face
            __init__.py
        v4d_dorsal_v4a/         # → LOC, color-form → object
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the left side in the same commit.

**The V4v / V4d split is a legitimate retinotopic subdivision.** **On
the right, the V4v component is the dominant ventral-stream
contributor** — it feeds the right LOC → right FFA (face) pathway,
and it is the substrate for the **pure color perception / felt
aspect** and the **prosopagnosia contribution** anchors.

**The split preserves the BA 19 correlate**: V4v and V4d both
inherit the parent's `(19,)` `BRODMANN_CORRELATES`.

**The split requires a joint revision of BA 19's
`V_AREA_CORRELATE` entry.** **No split should be performed while
LOC is unresolved.**

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../v4``:

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
        V-to-neighbour adjacency (with the LEFT / RIGHT field
                                     labels updated)
        CONNECTIVITY                 same bundle names
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — right V4 processes
                               the LEFT hemifield.
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        DOMAIN_EMPHASIS        right: color_vision is "pure_color_
                               perception_felt_aspect_left_
                               hemiachromatopsia"; form_and_object_
                               perception is "color_form_and_
                               stereo_defined_form_feeding_right_
                               loc_right_ffa_face_pathway".
                               left: color_vision is "color_form_
                               language_integration_right_
                               hemiachromatopsia_color_agnosia_
                               color_anomia"; etc.
        CONNECTIVITY           same bundle names; right: the
                               V4v → right LOC → right FFA
                               pathway carries pure color
                               perception and the felt aspect
                               of color experience.
                               left: the V4v → left LOC → left
                               VWFA pathway carries color-form-
                               language integration.
        CLINICAL_ANCHORS       right: twelve anchors (left
                               hemiachromatopsia, **pure color
                               perception deficit**, **felt
                               aspect of color loss**,
                               **prosopagnosia contribution**,
                               **three explicit absence anchors**
                               — `no_color_agnosia`,
                               `no_color_anomia`,
                               `no_color_form_language_
                               integration_deficit` — visual
                               object agnosia (color component),
                               right occipital infarct, migraine
                               aura, occipital epilepsy, PCA with
                               Benson syndrome, PRES).
                               left: eleven anchors (right
                               hemiachromatopsia, **color
                               agnosia**, **color-form-language
                               integration deficit**, **alexia
                               without agraphia (left V4 +
                               splenium)**, **color anomia**,
                               visual object agnosia (color
                               component), left occipital
                               infarct, migraine aura, occipital
                               epilepsy, PCA, PRES).

**The visual-hemifield asymmetry is the sharpest single entry.**

**The FUNCTIONAL_DOMAINS set is IDENTICAL across hemispheres.** V4
shares this property with V3 — **V3 and V4 are the only two V areas
in the current tree whose domain set is hemisphere-invariant**.

**The three explicit ABSENCE anchors on the right are the second
sharpest entry.** The right V4 carries **three explicitly-named
absence anchors** — `right_v4_no_color_agnosia`,
`right_v4_no_color_anomia`, and
`right_v4_no_color_form_language_integration_deficit` — that
document the **mirror-opposite** of the left's three presence
anchors. **These three absences are the sharpest structural
asymmetry in the entire occipital lobe's clinical anchors** — they
make explicit that the left V4's language-linked color deficits
have **no right-side counterpart**, and the right V4's dominant
function (pure color perception) is a **different** function from
the left V4's dominant function (color-form-language integration).

**The pure color perception anchor is a right-only positive
anchor.** `right_v4_pure_color_perception_deficit` captures the
right V4's unique contribution to the phenomenal / felt aspect of
color experience, which the left V4 does not carry at the same
weighting.

**The prosopagnosia contribution anchor is a right-only positive
anchor.** `right_v4_contribution_to_prosopagnosia` captures the
right V4v's role in the right face-recognition pathway, which the
left V4 does not carry (the left V4 feeds the left VWFA reading
pathway instead).

**The two-domain FUNCTIONAL_DOMAINS set is the smallest in the
V1-V4 hierarchy.** V4 is the **most functionally specialized** V
area.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "v4" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V4".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's
    (including "hv4" and "brodmann_area_19_partial").
[ ] ARCHITECTONIC_SIGNATURES is byte-identical to the left
    sibling's (color globs, dysgranular, retinotopic V3/V4
    border).
[ ] BRODMANN_CORRELATES is exactly ``(19,)`` — byte-identical to
    the left sibling's.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **triple mirror-flip** structure
    with the **LEFT hemifield label**.
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class
    field.
[ ] FUNCTIONAL_DOMAINS contains **two** domains:
    - color_vision
    - form_and_object_perception
[ ] **The FUNCTIONAL_DOMAINS set is verified to be IDENTICAL across
    hemispheres** — V4 shares this property with V3 (the two
    hemisphere-invariant domain sets).
[ ] FUNCTIONAL_DOMAINS **excludes** spatial_localization,
    binocular_vision, motion_perception, primary_visual_processing,
    primary_visual_processing_secondary, visual_attention,
    visual_word_processing, face_processing, and global_visual_
    processing (same exclusions as left V4).
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis**:
    - color_vision → pure_color_perception_felt_aspect_left_
      hemiachromatopsia
    - form_and_object_perception → color_form_and_stereo_defined_
      form_feeding_right_loc_right_ffa_face_pathway
[ ] CONNECTIVITY documents:
    - V2 (thin stripes) → V4 (color/border)
    - V3v → V4 (form-from-motion)
    - LGN koniocellular direct-to-V4 (weak; S-cone blue-yellow
      color)
    - Pulvinar afferent (stronger to V4 than to V1)
    - **V4 → LOC** (principal cortical target, feeding the right
      FFA face pathway)
    - **V4v → right LOC → right FFA** pathway (the right face-
      recognition pathway, with V4v being its fourth stage)
    - V4d → V4v intra-V4 relay (color-form integration)
    - V4 → V2 feedback
    - Callosal connections to left V4
    - Attentional feedback from right FEF, right DLPFC, right IPS
[ ] CLINICAL_ANCHORS contains the twelve right-specific anchors:
    - right_v4_left_hemiachromatopsia
    - **right_v4_pure_color_perception_deficit**
    - **right_v4_contribution_to_prosopagnosia**
    - **right_v4_no_color_agnosia** (absence)
    - **right_v4_no_color_anomia** (absence)
    - **right_v4_no_color_form_language_integration_deficit**
      (absence)
    - right_v4_visual_object_agnosia_color_component
    - right_v4_occipital_infarct_pca_territory
    - right_v4_migraine_visual_aura
    - right_v4_occipital_epilepsy_visual_auras
    - right_v4_posterior_cortical_atrophy_benson_syndrome
    - right_v4_pres_visual_symptoms
[ ] The **left hemiachromatopsia** is documented as the primary
    right V4 anchor.
[ ] The **pure color perception deficit** is documented as a
    **right-only positive anchor** — the phenomenal / felt aspect
    of color experience, which the left V4 does not carry at the
    same weighting.
[ ] The **prosopagnosia contribution** is documented as a
    **right-only positive anchor** — the right V4v's role in
    the right face-recognition pathway.
[ ] **The three absence anchors** — `no_color_agnosia`,
    `no_color_anomia`, `no_color_form_language_integration_
    deficit` — are documented as **right-specific ABSENCE
    anchors**. They explicitly record that the left V4's three
    language-linked color deficits are **left-only** and are
    **absent from the right V4**. **These absences are the
    sharpest structural asymmetry in the entire occipital
    lobe's clinical anchors.**
[ ] The **fusiform gyrus (V4v)** and **lateral occipital gyrus
    (V4d)** are documented, with the right-specific endpoint
    (right FFA face pathway) noted.
[ ] The **color globs** are documented as the only architectonic
    feature in the occipital lobe specifically associated with a
    named visual dimension.
[ ] The **triple mirror-flip** is documented with the LEFT
    hemifield label.
[ ] The **V4v / V4d split** is documented, with the right V4v
    being the dominant ventral-stream contributor.
[ ] **The two forward references — LOC and V4A / V4α** — are
    documented, the **resolution rule** is recorded, and the
    **right priority** (LOC first, for the prosopagnosia
    contribution) is noted.
[ ] No SUBDIVISIONS promotion is performed while LOC is
    unresolved.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, **FUNCTIONAL_DOMAINS set**, forward-declaration
    caveat text) match the left sibling; VISUAL_HEMIFIELD,
    DOMAIN_EMPHASIS (pure color perception vs color-form-
    language integration; right FFA vs left VWFA endpoint),
    CONNECTIVITY emphasis, and CLINICAL_ANCHORS deliberately
    differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    V4 carries "left_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP.
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — V4 and V3 are the only two V areas
    with hemisphere-invariant domain sets.
[ ] **The three absence anchors are verified**:
    `right_v4_no_color_agnosia`,
    `right_v4_no_color_anomia`, and
    `right_v4_no_color_form_language_integration_deficit` are
    present on the right **specifically to document the
    absence** of the left's three language-linked color
    deficits.
[ ] **The two right-only positive anchors are verified**:
    `right_v4_pure_color_perception_deficit` and
    `right_v4_contribution_to_prosopagnosia` are present on
    the right and absent on the left.
[ ] Any downstream code querying "what does the right V4 see?"
    must receive "the LEFT visual hemifield."
[ ] Any downstream code querying "what is V4?" must receive
    "the quaternary visual cortex / color and form area / V4
    / hV4 / part of BA 19."
[ ] Any downstream code querying "which V area carries
    `color_vision`?" must receive "V4 (the only V1–V4 area
    with it)."
[ ] Any downstream code querying "does the right V4 carry color
    agnosia?" must receive "**no** — color agnosia is
    left-lateralized and is explicitly absent from the right V4;
    see the `right_v4_no_color_agnosia` anchor."
[ ] Any downstream code querying "does the right V4 carry
    color anomia?" must receive "**no** — color anomia is
    left-lateralized and is explicitly absent from the right V4;
    see the `right_v4_no_color_anomia` anchor."
[ ] Any downstream code querying "does the right V4 carry
    color-form-language integration deficit?" must receive
    "**no** — this deficit is left-lateralized and is explicitly
    absent from the right V4; see the
    `right_v4_no_color_form_language_integration_deficit`
    anchor."
[ ] Any downstream code querying "what is the right V4's primary
    color function?" must receive "pure color perception and the
    felt / phenomenal aspect of color experience — the
    qualitative 'what it is like' to see a color."
[ ] Any downstream code assigning the right face pathway must
    route through the **right** V1 → V2 → V3v → V4v → LOC →
    right FFA chain — the right V4v is the fourth stage.
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** V1 → V2 → V3v → V4v → LOC →
    left VWFA chain.
[ ] Any downstream code assigning **color agnosia, color anomia,
    or color-form-language integration deficit** must route
    through the **left** V4 only — these deficits are
    left-lateralized and are explicitly absent from the right
    V4.
"""