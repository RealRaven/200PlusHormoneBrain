"""
Primary Visual Cortex (V1) — Left Hemisphere
=============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── primary_visual_cortex   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the
left hemisphere's **V1** — the **primary visual cortex**, also called
the **striate cortex** because of the architectonically visible
**stria of Gennari**. It is the **first and tightest** V↔BA
correspondence in the human cortex: **V1 is BA 17**, one-to-one, with
no residual. It is the first cortical stage of the visual hierarchy,
the input point for the visual radiation from the lateral geniculate
nucleus (LGN), and the anatomical substrate of **conscious visual
perception**.

Parent: ``..cortex`` (left occipital functional / V-numbered parent)
— sibling to V2, V3, V4. **Sibling — not parent —** of
``...brodmann_areas/brodmann_area_17_primary_visual``, which sits at
the ``..brodmann_areas`` parent level. The V1 / BA 17 relationship is
**1:1 correspondence, not nesting** — both packages describe the same
cortical territory from different angles (functional-retinotopic vs
cytoarchitectonic), and downstream code should treat them as
interchangeable identifiers for the same thing.

This package is the **structural mirror** of
``../../right/cortex/occipital/cortex/primary_visual_cortex``. The
V-number, the BA correlate (17), the architectonic signature (stria
of Gennari), the calcarine-sulcus surface landmark, and the retinotopic
map structure are identical on both sides; the **functional emphasis**
and **clinical significance** diverge — on the left, V1 processes the
**right** visual hemifield, and its ventral-stream output feeds the
left visual word form area (VWFA) via V2 / V3 / V4.

**This is the canonical V-area package** — the functional counterpart
of BA 17. The two packages are the tightest 1:1 correspondence in the
cortex tree, and any change to one must be mirrored in the other in
the same commit.

--------------------------------------------------------------------------------
WHAT V1 IS
--------------------------------------------------------------------------------

V1 occupies the **banks of the calcarine sulcus** — the **upper bank**
(the lower margin of the **cuneus**) and the **lower bank** (the upper
margin of the **lingual gyrus**). It extends from the **occipital pole**
(where the fovea is represented) rostrally along the calcarine sulcus
to the **anterior limit of the striate cortex**, where the calcarine
sulcus meets the parieto-occipital sulcus. The two banks converge at
the occipital pole and diverge caudo-rostrally, forming the
characteristic **wedge shape** of V1 in midsagittal section.

The **architectonic signature** of V1 is the **stria of Gennari** — a
band of myelinated axons running through layer IV of the striate
cortex. The stria is **visible to the naked eye** on a gross specimen
and is the reason the occipital cortex can be parcellated without
microscopy. This is why **BA 17 was Brodmann's first area** (1909),
and why the **V1/V2 border is architectonically unambiguous** in a way
that no other BA boundary in the cortex is.

**The 1:1 V1 ↔ BA 17 correspondence** is the tightest in the entire
cortex. Unlike V2 (which spans BA 18's full extent) or V3 (which
spans BA 18 and BA 19), **V1 is exactly BA 17** — the
functional-retinotopic boundary (the V1/V2 border) and the
cytoarchitectonic boundary (the stria of Gennari's abrupt
disappearance) **coincide**. This is why the
``primary_visual_cortex`` package has a **single-element
``BRODMANN_CORRELATES`` field** (``(17,)``) and does not need a
multi-element tuple.

**The retinotopic organization of V1** is the most precise in the
human cortex and is worth documenting in detail because it drives the
clinical presentation of V1 lesions:

    Fovea (macular representation)
        At the **occipital pole** — the most posterior point of the
        hemisphere. The fovea's cortical magnification is enormous
        (roughly 100× the peripheral representation per degree of
        visual angle), and the foveal representation in V1 is
        disproportionately large.

    Eccentricity gradient
        From the occipital pole **rostrally** along the calcarine
        sulcus. The **central 10° of vision** occupies roughly
        **half** of the total V1 surface area; the peripheral visual
        field is represented at the **anterior calcarine banks**,
        near the junction with the parieto-occipital sulcus.

    Upper visual field → lower bank of the calcarine sulcus
        The **lingual gyrus** (the lower bank of the calcarine
        sulcus) represents the **upper** visual field of the
        **contralateral** hemifield. **On the left, the lingual
        gyrus represents the upper RIGHT visual field.**

    Lower visual field → upper bank of the calcarine sulcus
        The **cuneus** (the upper bank of the calcarine sulcus)
        represents the **lower** visual field of the **contralateral**
        hemifield. **On the left, the cuneus represents the lower
        RIGHT visual field.**

    Vertical meridian → V1/V2 border
        The vertical meridian of the visual field is represented at
        the **V1/V2 border** (the BA 17 / BA 18 border), which lies
        **caudomedially** on the banks of the calcarine sulcus. The
        callosal connections between the left and right V1 meet at
        this border, in the V2 territory.

    Horizontal meridian → base of the calcarine sulcus
        The horizontal meridian is represented at the **fundus**
        (deepest part) of the calcarine sulcus.

**Left-hemisphere specificity**: the left V1 processes the **RIGHT**
visual hemifield of both eyes (contralateral processing). The
**right homonymous hemianopia** that follows a left V1 lesion is the
canonical left-lateralized visual-field deficit. On the left, V1 is
also the **input stage of the ventral stream that feeds the left
VWFA** — the reading pathway begins in the left V1 and terminates in
the left fusiform gyrus; this is why left V1 lesions can contribute
to reading deficits when the splenium is also involved (see the
clinical section).

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours (functional)
        rostrally              V2 (the V1/V2 border, which coincides
                               with BA 17 / BA 18)
        caudomedially          V2 (upper-bank continuation)
        laterally              the cuneus (medial surface) and the
                               lingual gyrus (medial surface); the
                               lateral surface of V1 is only
                               visible at the occipital pole
        ventrally              the lingual gyrus
        dorsally               the cuneus

    Functional overlays
        BA 17 — 1:1 correspondence
            V1 **is** BA 17. The functional-retinotopic parent
            ``..cortex`` and the cytoarchitectonic parent
            ``..brodmann_areas`` describe the **same cortical
            territory** from two angles. Downstream code should
            treat V1 and BA 17 as interchangeable identifiers for
            the same thing.
        cuneus — upper-bank V1
            The cuneus (upper bank of the calcarine sulcus) carries
            the dorsal V1 representation of the **lower** contralateral
            visual field. **On the left, the lower RIGHT field.**
        lingual gyrus — lower-bank V1
            The lingual gyrus (lower bank of the calcarine sulcus)
            carries the ventral V1 representation of the **upper**
            contralateral visual field. **On the left, the upper
            RIGHT field.** (Note: the lingual gyrus is a **forward
            reference** in ``..gyri`` — it is not yet a package.)
        calcarine sulcus — defining surface landmark
            The calcarine sulcus is the **defining sulcus** of V1
            and the surface landmark for V1's representation. The
            ``..sulci/calcarine_sulcus`` package declares V1 (and
            BA 17) as its primary functional overlay.
        left visual word form area (VWFA) — downstream ventral-
        stream target
            **Left-specific overlay.** The left V1's ventral-stream
            output — via V2, V3, V4, and the LOC — terminates in
            the **left VWFA** in the left fusiform gyrus. The V1 →
            V2 → V3 → V4 → LOC → VWFA pathway is the **left
            reading pathway**, and left V1 is its **input stage**.

**This field is structurally identical to the right sibling's** — the
architectonic neighbours and the cuneus / lingual-gyrus / calcarine
overlays are the same on both sides. What differs is the **visual
hemifield** — the left V1 processes the RIGHT hemifield, and the
cuneus / lingual gyrus representations carry the upper / lower RIGHT
field on the left. The **left VWFA downstream target** is a
left-specific functional overlay that the right V1 package declares
as the **right FFA** (the face-recognition endpoint) instead.

--------------------------------------------------------------------------------
V-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    V2                                     **rostral neighbour** via the
                                           V1/V2 border. The V1 → V2
                                           projection is the first
                                           step of the V1 → V2 → V3
                                           → V4 hierarchy. **The
                                           vertical meridian of the
                                           visual field is
                                           represented at the V1/V2
                                           border**, and the callosal
                                           connections between the
                                           left and right V1 meet at
                                           this border.
    V3                                     **distant rostral neighbour**
                                           via V2; no direct
                                           adjacency
    V4                                     **distant rostral neighbour**
                                           via V2 and V3; no direct
                                           adjacency
    BA 17                                  **1:1 correspondence** —
                                           the cytoarchitectonic
                                           counterpart of V1. Same
                                           territory, different
                                           decomposition scheme.
    cuneus (medial-surface gyrus)          dorsal bank of the calcarine
                                           sulcus; the upper-bank V1
                                           representation of the
                                           **lower** visual field
                                           (**lower RIGHT field on
                                           the left**)
    lingual gyrus (medial-surface          ventral bank of the calcarine
    gyrus; forward reference in ..gyri)    sulcus; the lower-bank V1
                                           representation of the
                                           **upper** visual field
                                           (**upper RIGHT field on
                                           the left**)
    calcarine sulcus (defining sulcus)     the fundus of the sulcus
                                           represents the horizontal
                                           meridian; the banks
                                           represent the upper /
                                           lower fields

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

V1 participates in **three** canonical occipital functional domains.
The domain **set is identical** to BA 17's (the 1:1 correspondence
extends to the functional domains), and the **emphasis** is the same
as BA 17's left-side emphasis:

    primary_visual_processing                      (left emphasis — PRIMARY)
        **This is V1's defining contribution.** The first
        cortical stage of vision: orientation selectivity,
        ocular-dominance columns, spatial-frequency tuning, contrast
        sensitivity, edge detection, and retinotopic mapping. On the
        left, V1 processes the **RIGHT visual hemifield**; right
        homonymous hemianopia follows left V1 lesions.

    retinotopic_organization                       (left emphasis — PRIMARY)
        **This is V1's second primary contribution.** The
        topographic mapping of the **RIGHT visual hemifield** onto
        the left calcarine banks, with the fovea at the occipital
        pole and the periphery at the anterior calcarine banks. The
        left V1's retinotopic map is essentially a mirror image of
        the right V1's, with the field label flipped.

    binocular_vision                               (left emphasis — PRIMARY)
        Ocular-dominance columns and their convergence onto
        binocular cells support depth perception, stereopsis, and
        binocular fusion. On the left, binocular vision combines
        the right-eye and left-eye inputs to the **RIGHT visual
        hemifield**.

**Left-specific caveat on `color_vision`.** V1 is **not** the
color-vision area — that is V4, in BA 19. V1 has some wavelength
selectivity (via the koniocellular pathway from the LGN), but the
**conscious perception of color** emerges in V4 and the ventral
stream. `color_vision` is **omitted** from the V1
`FUNCTIONAL_DOMAINS` tuple; it appears in V4 instead.

**Left-specific caveat on `motion_perception`.** V1 is **not** the
motion area — that is V5/MT+, a forward reference in BA 19. V1 has
some direction selectivity, but **conscious motion perception**
emerges in MT/V5 and the dorsal stream. `motion_perception` is
**omitted** from the V1 `FUNCTIONAL_DOMAINS` tuple.

**Left-specific caveat on `form_and_object_perception`.** V1
contributes to the **early stages** of form processing (edge
detection, contour integration), but **object recognition** emerges
in V4, the LOC, and the ventral stream. `form_and_object_perception`
is **omitted** from the V1 `FUNCTIONAL_DOMAINS` tuple.

**Left-specific caveat on `spatial_localization`.** V1 contributes
to the **early stages** of spatial localization (retinotopic
position), but **full spatial localization** emerges in V3, V3A, and
V5/MT+. `spatial_localization` is **omitted** from the V1
`FUNCTIONAL_DOMAINS` tuple.

**Left-specific caveat on `visual_attention`.** V1 is a **target**
of top-down attentional modulation from the frontal eye fields (BA
8) and the dorsolateral prefrontal cortex, but it is **not** itself
an attentional control area. `visual_attention` is **omitted** from
the V1 `FUNCTIONAL_DOMAINS` tuple as a primary domain; the
attentional modulation of V1 is captured under the connectivity
section (feedback from FEF and DLPFC).

**Left-specific caveat on `visual_word_processing`.** V1 is the
**input stage** of the left ventral stream that feeds the left VWFA,
but V1 itself does **not** perform word processing. The VWFA is in
the left fusiform gyrus, several synapses downstream. `visual_word_
processing` is **omitted** from the V1 `FUNCTIONAL_DOMAINS` tuple.

**Left-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the left
V1 does **not** carry. They are instantiated in the right FFA and
the right BA 18 emphasis, respectively. Neither appears in the left
V1 `FUNCTIONAL_DOMAINS` tuple.

**Summary**: V1 carries **exactly three** functional domains —
`primary_visual_processing`, `retinotopic_organization`, and
`binocular_vision` — the same domain set as BA 17. This is the
**only V-area package in the tree whose FUNCTIONAL_DOMAINS tuple
matches its BA counterpart exactly** (the 1:1 correspondence extends
to the functional domains). The **emphasis** is also identical to BA
17's, because the two packages describe the same territory.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), left
            **V1's primary and dominant thalamic afferent.** The
            LGN relays the visual signal from the left hemiretinas
            of both eyes (via the optic chiasm and the left optic
            tract). The LGN → V1 projection terminates in layer IV
            of the striate cortex — **layer IV is where the stria
            of Gennari runs** — and the LGN input is segregated
            into ocular-dominance columns that alternate between
            the left-eye and right-eye inputs. This is the
            anatomical substrate of the first cortical stage of
            vision.
        → pulvinar (secondary, modulatory)
            The pulvinar sends a weaker modulatory projection to
            V1 (and stronger projections to V2, V3, and V4),
            participating in the cortico-thalamo-cortical loops
            that support visual attention and visual short-term
            memory.
        → LGN feedback from layer VI
            V1 layer VI projects **back** to the LGN, forming the
            cortico-geniculate feedback loop that modulates the
            thalamic relay. This is a **top-down** modulation of
            the incoming visual signal, not a forward projection.

    cortical efferents
        → V2, left
            **V1's principal cortical target.** The V1 → V2
            projection carries V1's output to V2 (the first
            extrastriate stage). This is the first step of the
            V1 → V2 → V3 → V4 hierarchy.
        → V3 and V4 (via the V2 relay)
            V1's output reaches V3 and V4 via the **V2 relay**,
            not directly. There are **no direct V1 → V3 or V1 →
            V4 projections** — the relay through V2 is obligate.
        → MT/V5 (via V2, dorsal stream — forward reference)
            The motion pathway (V1 → V2 → MT/V5) carries the
            low-level motion signal from V1 to the motion area.
            On the left, this pathway supports **right-hemifield**
            motion perception, though the right MT/V5 is the
            dominant motion hemisphere.
        → LOC (via V2, V3, V4, ventral stream — forward reference)
            The color/form/object pathway (V1 → V2 → V3 → V4 →
            LOC) carries the low-level object signal from V1 to
            the LOC. **On the left, the LOC → left VWFA pathway
            carries the object-form signal forward to the reading
            endpoint.**

    callosal connections
        → right V1
            The callosal fibers connect the left V1 to the right
            V1 at the **vertical meridian** (the V1/V2 border),
            where the two hemispheres' visual fields meet. This
            callosal connection is essential for the **fusion of
            the two hemifields** and for the **continuity of
            vision across the vertical midline**. Interruption of
            the callosal connections produces a **split-field**
            visual experience.

    attentional feedback
        → frontal eye fields (BA 8), left
            The left FEF sends **top-down attentional gain** to
            V1, modulating the responsiveness of V1 neurons to
            behaviourally relevant stimuli.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), left
            The left DLPFC sends top-down attentional and
            working-memory signals to V1, supporting **visual
            working memory** and **visual imagery**.
        → intraparietal sulcus, left
            The left IPS sends dorsal-attention-network signals
            to V1, supporting **spatial attention** in the RIGHT
            visual hemifield.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in two respects:
(a) the V1 → V2 → V4 → LOC → left VWFA pathway is the **verbal-
visual pathway** that the left hemisphere dominates (reading);
(b) the callosal vertical-meridian connection carries the
**right-hemifield / left-hemifield fusion** signal, which on the
left is the **left half of the fused visual field**.

**Note: the connectivity is identical in structure to BA 17's.** The
1:1 correspondence between V1 and BA 17 extends to connectivity —
they describe the same territory. Downstream code can query either
package for the same connectivity dictionary.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_v1_right_homonymous_hemianopia
        **This is the left V1 anchor par excellence.** A lesion of
        the left V1 (or the left optic radiation, or the left LGN)
        produces a **right homonymous hemianopia** — loss of the
        right half of the visual field in both eyes. The deficit
        is **homonymous** (both eyes lose the same side),
        **hemianopic** (half the field is lost), and
        **contralateral** (right side from a left lesion). This is
        the single most common and most clinically consequential
        effect of a left V1 lesion.

    macular_sparing_right
        **Macular sparing** — preservation of the central 5–10° of
        the visual field within an otherwise complete homonymous
        hemianopia — is a well-known phenomenon in V1 lesions.
        The mechanism is debated but is generally attributed to
        the **dual blood supply** of the occipital pole: the
        occipital pole (where the fovea is over-represented)
        receives blood from **both the posterior cerebral artery
        (PCA) and the middle cerebral artery (MCA)**, whereas the
        anterior calcarine banks receive blood from the PCA alone.
        **An MCA-PCA watershed infarct spares the occipital pole,
        sparing the macula** — and this is why macular sparing is
        a **hallmark of occipital (PCA) lesions** and is **less
        common** in optic-tract or chiasmal lesions.
        **On the left, a left V1 lesion produces a right
        hemianopia with right macular sparing.**

    cortical_blindness_bilateral
        **Bilateral V1 lesions** produce **cortical blindness** —
        complete loss of vision despite intact eyes, optic nerves,
        and LGN. The patient has no visual perception but may
        retain pupillary light reflexes (because the reflex arc
        goes through the pretectum and the Edinger-Westphal
        nucleus, not V1). Bilateral lesions can result from
        **bilateral PCA infarcts**, **hypoxic-ischemic
        encephalopathy**, **PRES**, or **trauma**. **This anchor
        is hemisphere-invariant** — it appears on both sides with
        the same clinical significance.

    anton_syndrome
        **Anton syndrome** — **cortical blindness with denial of
        blindness** — is a rare complication of bilateral V1
        lesions. The patient is cortically blind but **insists that
        they can see**, and may confabulate visual experiences.
        **This anchor is hemisphere-invariant.**

    blindsight
        **Blindsight** — residual visual function (detection,
        localization, and sometimes discrimination of stimuli) in
        the absence of conscious visual perception — is a
        well-documented phenomenon after **V1 lesions**. The
        residual function is mediated by **subcortical visual
        pathways** (the superior colliculus and the pulvinar, which
        project to MT/V5 and to the extrastriate cortex bypassing
        V1). **This anchor is hemisphere-invariant.**

    hemianopic_alexia_right
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **right homonymous hemianopia** (from a
        left V1 lesion) — is a recognized clinical entity. The
        patient's reading is slowed or impaired because they must
        make large **rightward saccades** to compensate for the
        missing right hemifield, and the **left-hemisphere reading
        network** (the left VWFA) cannot function efficiently
        without the full right-hemifield input. This is the
        **mildest form of alexia** and is often clinically
        under-recognized compared to the more severe alexia
        without agraphia.

    alexia_without_agraphia_left_v1_plus_splenium
        **Alexia without agraphia** (Dejerine 1892) — the patient
        can **write** but cannot **read what they have written** —
        results from a **left occipital lesion that disconnects
        the intact right occipital cortex from the left language
        areas**. The classic lesion is **left PCA infarct
        (involving left V1 and the left splenium of the corpus
        callosum)**. The mechanism is: the right hemisphere can
        still see, but its visual signal cannot reach the left
        VWFA because the splenium is destroyed; the left VWFA has
        no visual input. The patient can write (because writing is
        a left-hemisphere motor program) but cannot read (because
        the left VWFA is disconnected from vision). **This is the
        canonical clinical demonstration that the left V1's
        contribution to reading is via the left VWFA, and that the
        callosal pathway is essential for the intact reading
        circuit.**

    migraine_visual_aura
        **Migraine visual aura** — the transient, typically
        bilateral, scintillating scotomata and fortification
        spectra that precede a migraine headache — reflects
        **cortical spreading depression** spreading across the
        **occipital cortex**, including V1. The phenomenon is
        not a lesion, but it is a **functional disturbance of
        V1**, and it is one of the most common clinical
        phenomena involving the primary visual cortex.
        **This anchor is hemisphere-invariant.**

    occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** —
        elementary visual hallucinations (flashing lights, colored
        shapes, geometric patterns) in the **contralateral visual
        field** — is a well-characterized epilepsy syndrome. The
        auras arise from **epileptiform discharge in V1 (or V2)**
        and project to the **right visual field** when they arise
        from the left occipital cortex.

    posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1 and V2** bilaterally in later
        stages. Early stages affect the **dorsal and ventral
        association cortices** more than V1 proper, but the
        disease eventually involves the striate cortex and
        produces **cortical blindness**. **On the left, PCA can
        produce progressive reading deficits** (the "visual
        variant" of progressive aphasia).

    pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia** from
        bilateral occipital involvement. **The syndrome is
        reversible** in most cases.

    occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** involving
        the left V1 produces **right homonymous hemianopia**,
        often with **macular sparing** (as described above), and
        can also produce the **alexia without agraphia** syndrome
        if the left splenium is involved. The left PCA territory
        includes the left calcarine cortex, the left lingual gyrus,
        and (via the posterior pericallosal artery) the left
        splenium. This is the most common single-lesion syndrome
        involving the left V1.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left V1 processes the **RIGHT visual hemifield**, so left
V1 lesions produce **right-sided** visual deficits; (b) the left
V1 is the **input stage of the left reading pathway**, so left
V1 lesions can contribute to reading deficits (hemianopic alexia,
alexia without agraphia) that have no symmetric counterpart on the
right. The right sibling's docstring carries the corresponding
right-sided anchors (left homonymous hemianopia, left macular
sparing, prosopagnosia from right occipito-temporal lesions, and
the right-lateralized attentional contributions).

**The clinical anchors are identical to BA 17's** — the 1:1
correspondence between V1 and BA 17 extends to the clinical
syndromes. Downstream code that queries V1 for a clinical anchor
receives the same result as querying BA 17.

**The `macular_sparing`, `blindsight`, `Anton syndrome`, and
`cortical blindness` anchors are hemisphere-invariant** — they appear
on both sides and are documented identically in both siblings.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..cortex  (parent)
    The left occipital functional / V-numbered parent. This
    package's parent, source of the ``BA_TO_V_CROSSWALK``,
    ``V_TO_BA_CROSSWALK``, ``FORWARD_REFERENCE_V_AREAS``, and
    ``DOMAIN_COVERAGE`` registries, and enforcer of the **V1 ↔ BA
    17 1:1 correspondence**.

..v2
    **Rostral neighbour** via the V1/V2 border. The V1 → V2
    projection is the first step of the V1 → V2 → V3 → V4
    hierarchy. **The vertical meridian of the visual field is
    represented at the V1/V2 border**, and the callosal
    connections between the left and right hemispheres meet at
    this border.

..v3
    **Distant rostral neighbour** via V2; no direct adjacency.

..v4
    **Distant rostral neighbour** via V2 and V3; no direct
    adjacency.

...brodmann_areas.brodmann_area_17_primary_visual
    **The cytoarchitectonic counterpart — the 1:1 correspondence
    of this package.** V1 and BA 17 are the **same cortical
    territory** described from two angles. Downstream code should
    treat them as interchangeable identifiers and query either
    package for the same set of functional domains, connectivity,
    and clinical anchors.

...cuneus
    The medial-surface gyral landmark. The cuneus's lower margin
    (the upper bank of the calcarine sulcus) carries the **dorsal
    V1 representation of the lower** contralateral visual field.
    **On the left, the lower RIGHT field.**

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus (lower bank of the calcarine sulcus) carries
    the **ventral V1 representation of the upper** contralateral
    visual field. **On the left, the upper RIGHT field.**

...sulci.calcarine_sulcus
    **The defining sulcus of V1.** The banks of the calcarine
    sulcus carry the V1 representation, and the **fundus** of the
    sulcus represents the **horizontal meridian** of the visual
    field.

...sulci.lunate_sulcus
    An inconstant lateral-surface sulcus that, when present, marks
    the **anterior boundary of V1 on the lateral surface**.

..cortex.temporal
    The **ventral stream** continues from V2 / V3 / V4 / LOC into
    the temporal lobe. **On the left, the ventral stream
    terminates in the left VWFA** (the reading area), and the left
    V1 is the **input stage** of this pathway. The temporal
    package must declare the left V1 as the source of its visual
    input via the ventral stream, and must note the
    **left-lateralized VWFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from V2 / V3 / V4 into the
    parietal lobe. **On the left, the dorsal stream supports
    right-hemifield spatial attention.** The parietal package must
    declare the left V1 as the source of its visual input for the
    dorsal stream via the V2 / V3 / V4 relay.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V1 via the V2 relay. The frontal package must
    declare the left V1 as a target of its attentional
    projections.

..cortex.cingulate  — indirect
    No direct cingulate → V1 projection. Recorded here to
    pre-empt a false cross-reference.

..cortex.insular  — indirect
    No direct insular → V1 projection. Recorded here to
    pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **The LGN is V1's primary and dominant thalamic afferent.**
    The LGN → V1 projection terminates in layer IV (where the
    stria of Gennari runs) and is segregated into ocular-dominance
    columns.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a secondary, modulatory projection to V1
    (stronger to V2, V3, and V4).

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream terminates in the perirhinal, entorhinal,
    and parahippocampal cortices. **The left V1 is the input
    stage** of the occipito-temporal-hippocampal pathway that
    supports visual object recognition and visual memory.

../../right/cortex/occipital/cortex/primary_visual_cortex
    The right-hemisphere homologue. Structural fields (V-number,
    BA correlate, architectonic signature, calcarine-sulcus
    surface landmark, retinotopic map structure, cuneus /
    lingual-gyrus relationship) MUST be byte-identical. Functional
    emphasis and clinical significance diverge — the right V1
    processes the **LEFT** visual hemifield, and right V1 lesions
    produce **left** homonymous hemianopia. The right V1 is the
    input stage of the right ventral stream that feeds the right
    FFA, not the left VWFA.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "primary_visual_cortex"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    V_NUMBER            = "V1"
    ALTERNATE_NAMES     = ("striate_cortex",
                           "V1",
                           "brodmann_area_17_primary_visual")
        # **The 1:1 BA correspondence is recorded in the
        # ALTERNATE_NAMES field** — V1 is BA 17, and downstream
        # code may refer to the territory by either name.

    ARCHITECTONIC_SIGNATURE = "stria_of_gennari"
        # **The only V area in the cortex tree where the
        # architectonic boundary is visible to the naked eye.**

    BRODMANN_CORRELATES = (17,)
        # **Exactly one** BA — the tightest V↔BA correspondence
        # in the cortex. Unlike V3 (BA 18 + BA 19), V1 has no
        # residual.

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** V1 is unique to the occipital
        # lobe.

    RETINOTOPIC_MAP     = "fovea_at_pole_contralateral_hemifield"
        # The fovea is at the occipital pole; the periphery is at
        # the anterior calcarine banks; the vertical meridian is at
        # the V1/V2 border; the horizontal meridian is at the
        # fundus of the calcarine sulcus. **On the left, the
        # represented hemifield is the RIGHT hemifield.**

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** — the most important
        # single fact about the left V1. Downstream code that
        # queries "what does the left V1 see?" must receive "the
        # RIGHT visual hemifield."

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing",
                              "retinotopic_organization",
                              "binocular_vision",
                              # **Identical to BA 17's domain set**
                              # — the 1:1 correspondence extends to
                              # the functional domains.
                              # NOTE: color_vision is EXCLUDED (V4,
                              # BA 19 territory).
                              # NOTE: motion_perception is EXCLUDED
                              # (V5/MT+, BA 19 territory).
                              # NOTE: form_and_object_perception is
                              # EXCLUDED (V2, V3, V4, LOC — BA 18
                              # and BA 19 territory).
                              # NOTE: spatial_localization is
                              # EXCLUDED (V3, V3A — BA 18 and BA 19
                              # territory).
                              # NOTE: visual_attention is
                              # EXCLUDED as a primary domain (V1 is
                              # a *target* of attention, not a
                              # *generator*).
                              # NOTE: visual_word_processing is
                              # EXCLUDED (V1 is the input stage of
                              # the left reading pathway, not the
                              # reading operation).
                              # NOTE: face_processing and
                              # global_visual_processing are
                              # EXCLUDED (right-lateralized; not
                              # instantiated on the left V1).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "primary_visual_processing":
                                  "first_cortical_stage_of_vision_"
                                  "right_hemifield",
                              "retinotopic_organization":
                                  "fovea_at_pole_right_hemifield_"
                                  "eccentricity_gradient",
                              "binocular_vision":
                                  "ocular_dominance_columns_right_"
                                  "hemifield_stereopsis",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_v1_right_homonymous_"
                              "hemianopia",
                              "macular_sparing_right",
                              "cortical_blindness_bilateral",
                              "anton_syndrome",
                              "blindsight",
                              "hemianopic_alexia_right",
                              "alexia_without_agraphia_left_"
                              "v1_plus_splenium",
                              "migraine_visual_aura",
                              "occipital_epilepsy_visual_auras",
                              "posterior_cortical_atrophy",
                              "pres_visual_symptoms",
                              "occipital_infarct_pca_territory",
                          )

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "AREA_NAME",
        "HEMISPHERE",
        "LOBE",
        "V_NUMBER",
        "ALTERNATE_NAMES",
        "ARCHITECTONIC_SIGNATURE",
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
computation that references V1 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this package.** V1 is a
leaf V package whose structural neighbours (V2, V3, V4, BA 17, the
cuneus, the calcarine sulcus, and the LGN) all exist as packages in
the tree. The **lingual gyrus** (the lower bank of the calcarine
sulcus) is a forward reference in ``..gyri`` — it is not yet a
package — but the V1 package does not depend on it: the lingual
gyrus is a *surface landmark* for the ventral V1 representation, and
V1's own structural fields (the calcarine sulcus, the cuneus, and
BA 17) resolve fully.

**The one open question** is whether the **lingual gyrus** should be
placed under ``..occipital/gyri/`` alongside the lateral occipital
gyrus, or under a separate medial-surface gyral parent (like the
cuneus's parent-level placement). This caveat is byte-identical to
the BA 17 sibling's.

--------------------------------------------------------------------------------
PROMOTION RULE (when a V sub-field becomes a package)
--------------------------------------------------------------------------------

V1 is **architectonically homogeneous** — the stria of Gennari runs
continuously across the entire territory — and there is no natural
architectonic subdivision. The **one conceivable split** is the
**foveal (macular) representation vs the peripheral representation**,
since the fovea is enormously over-represented. If a future
parcellation decides to split V1 into its foveal and peripheral
components, the promotion takes this form:

    primary_visual_cortex/
        __init__.py
        foveal_representation/
            __init__.py
        peripheral_representation/
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The foveal / peripheral split is a FUNCTIONAL subdivision, not an
architectonic one.** The stria of Gennari does not distinguish foveal
from peripheral V1.

**The foveal component is the macular-sparing substrate.** The
macular-sparing clinical anchor is directly tied to the foveal
component's **dual blood supply** (PCA + MCA at the occipital pole).

**No split should be performed while the BA 17 functional counterpart
under ``..brodmann_areas/brodmann_area_17_primary_visual`` is not yet
split.** The V1 ↔ BA 17 1:1 correspondence means that any V1 split
must be mirrored by a corresponding BA 17 split, in the same commit,
in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../primary_visual_cortex``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "primary_visual_cortex"
        LOBE                         "occipital"
        V_NUMBER                     "V1"
        ALTERNATE_NAMES              ("striate_cortex", "V1",
                                     "brodmann_area_17_primary_
                                     visual")
        ARCHITECTONIC_SIGNATURE      "stria_of_gennari"
        BRODMANN_CORRELATES          (17,) — the 1:1 V1 ↔ BA 17
                                     correspondence is
                                     hemisphere-invariant
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same fovea-at-pole /
                                     eccentricity-gradient /
                                     vertical-meridian /
                                     horizontal-meridian structure
        FUNCTIONAL_DOMAINS set       the same three domains
                                     (primary_visual_processing,
                                     retinotopic_organization,
                                     binocular_vision)
        Bounding / overlapping territories
        V-to-neighbour adjacency
        CONNECTIVITY                 same bundle names
        The forward-declaration caveat text (byte-identical —
                                     the lingual-gyrus placement
                                     question is a lobe-level
                                     concern)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — left V1 processes
                               the RIGHT hemifield; right V1
                               processes the LEFT hemifield.
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        DOMAIN_EMPHASIS        left: primary_visual_processing is
                               "first_cortical_stage_of_vision_
                               right_hemifield"; retinotopic_
                               organization is "fovea_at_pole_
                               right_hemifield_eccentricity_
                               gradient"; binocular_vision is
                               "ocular_dominance_columns_right_
                               hemifield_stereopsis".
                               right: primary_visual_processing is
                               "first_cortical_stage_of_vision_
                               left_hemifield"; retinotopic_
                               organization is "fovea_at_pole_
                               left_hemifield_eccentricity_
                               gradient"; binocular_vision is
                               "ocular_dominance_columns_left_
                               hemifield_stereopsis".
        CONNECTIVITY           same bundle names; left: the V1 → V2
                               → V4 → LOC → left VWFA pathway is
                               the left reading pathway; the
                               callosal traffic carries the left
                               half of the fused visual field.
                               right: the V1 → V2 → V4 → LOC →
                               right FFA pathway is the right
                               face-recognition pathway; the
                               callosal traffic carries the right
                               half of the fused visual field.
        CLINICAL_ANCHORS       left: twelve anchors (right
                               homonymous hemianopia, **right
                               macular sparing**, cortical
                               blindness, Anton syndrome,
                               blindsight, hemianopic alexia
                               (right), **alexia without
                               agraphia (left V1 + splenium)**,
                               migraine aura, occipital epilepsy,
                               PCA, PRES, occipital infarct).
                               right: twelve anchors (left
                               homonymous hemianopia, **left
                               macular sparing**, cortical
                               blindness, Anton syndrome,
                               blindsight, **hemianopic alexia
                               (left, milder)**, migraine aura,
                               occipital epilepsy, PCA, PRES,
                               occipital infarct; plus the
                               right-lateralized prosopagnosia
                               contribution from right
                               occipito-temporal lesions).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same V1, the same architectonic
signature, the same LGN input, and the same V1 → V2 hierarchy — but
the *represented hemifield* is **flipped**. Left V1 → right hemifield;
right V1 → left hemifield.

**The macular-sparing field label flips.** A **left V1 lesion**
produces a **right hemianopia with right macular sparing**; a **right
V1 lesion** produces a **left hemianopia with left macular sparing**.

**The clinical anchors are identical to BA 17's** — the 1:1
correspondence between V1 and BA 17 extends to the clinical
syndromes.

**The hemisphere-invariant anchors** — cortical blindness, Anton
syndrome, blindsight, migraine aura, occipital epilepsy, PCA, PRES,
and occipital infarct — are **documented identically in both
siblings** and must not be allowed to drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "primary_visual_cortex".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V1".
[ ] ALTERNATE_NAMES includes "striate_cortex", "V1", and
    "brodmann_area_17_primary_visual" — **the 1:1 BA
    correspondence must be recorded**.
[ ] ARCHITECTONIC_SIGNATURE is "stria_of_gennari" — the **only V
    area in the cortex tree where the architectonic boundary is
    visible to the naked eye**.
[ ] BRODMANN_CORRELATES is exactly ``(17,)`` — the 1:1
    correspondence, no residual.
[ ] NAMING_COLLISION_WITH is an empty tuple — V1 has no naming
    collision.
[ ] RETINOTOPIC_MAP is "fovea_at_pole_contralateral_hemifield" and
    the docstring documents the four sub-features:
    - fovea at the occipital pole
    - eccentricity gradient (fovea → anterior calcarine)
    - vertical meridian at the V1/V2 border
    - horizontal meridian at the fundus of the calcarine sulcus
    - **the represented hemifield is the RIGHT hemifield on the
      left side**
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class,
    queryable field.
[ ] FUNCTIONAL_DOMAINS contains exactly:
    - primary_visual_processing
    - retinotopic_organization
    - binocular_vision
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision (V4, BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (V5/MT+, BA
    19).
[ ] FUNCTIONAL_DOMAINS **excludes** form_and_object_perception
    (V2, V3, V4, LOC — BA 18 and BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** spatial_localization (V3, V3A
    — BA 18 and BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a primary
    domain (V1 is a *target*, not a *generator*).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing (V1 is
    the *input stage*, not the *operation*).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing (right-lateralized).
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical to
    BA 17's** — the 1:1 correspondence extends to the functional
    domains.
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis**:
    - primary_visual_processing → first_cortical_stage_of_vision_
      right_hemifield
    - retinotopic_organization → fovea_at_pole_right_hemifield_
      eccentricity_gradient
    - binocular_vision → ocular_dominance_columns_right_
      hemifield_stereopsis
[ ] CONNECTIVITY documents:
    - LGN thalamic afferent (primary, dominant, terminates in
      layer IV / stria of Gennari)
    - Pulvinar afferent (secondary, modulatory)
    - V1 → V2 principal cortical target (the obligate relay)
    - **no direct V1 → V3 or V1 → V4 projections**
    - **V1 → V2 → V4 → LOC → left VWFA pathway** (the left
      reading pathway)
    - **V1 → V2 → MT/V5 pathway** (the motion pathway)
    - callosal connections to the right V1 at the vertical
      meridian (V1/V2 border)
    - attentional feedback from the left FEF (BA 8), left DLPFC
      (BA 9 / BA 46), and left IPS
[ ] CLINICAL_ANCHORS contains the twelve left-specific anchors:
    - left_v1_right_homonymous_hemianopia
    - macular_sparing_right
    - cortical_blindness_bilateral
    - anton_syndrome
    - blindsight
    - hemianopic_alexia_right
    - alexia_without_agraphia_left_v1_plus_splenium
    - migraine_visual_aura
    - occipital_epilepsy_visual_auras
    - posterior_cortical_atrophy
    - pres_visual_symptoms
    - occipital_infarct_pca_territory
[ ] The **right homonymous hemianopia** is documented as the
    primary left V1 anchor.
[ ] **Right macular sparing** is documented with its dual-blood-
    supply mechanism.
[ ] **Cortical blindness, Anton syndrome, and blindsight** are
    documented as the hemisphere-invariant bilateral-lesion
    syndromes.
[ ] **Hemianopic alexia** and **alexia without agraphia** are
    documented as the left-lateralized reading deficits that arise
    because the left V1 is the input stage of the left reading
    pathway (left V1 → V2 → V3 → V4 → LOC → left VWFA).
[ ] **The V1 ↔ BA 17 1:1 correspondence** is documented explicitly
    in the ALTERNATE_NAMES field and in the cross-references to
    ``...brodmann_areas.brodmann_area_17_primary_visual`` — V1
    and BA 17 are the **same cortical territory** described from
    two angles.
[ ] **The clinical anchors are verified to be identical to BA
    17's** — the 1:1 correspondence extends to the clinical
    syndromes.
[ ] The **stria of Gennari** is documented as the architectonic
    signature and the reason the V1 / V2 border is
    architectonically unambiguous.
[ ] The **calcarine sulcus** is documented as the defining sulcus
    and the surface landmark for V1, with the horizontal meridian
    at the fundus and the upper / lower fields on the two banks.
[ ] The **cuneus and lingual gyrus** are documented as the upper
    and lower banks of the calcarine sulcus, carrying the lower
    and upper contralateral field representations respectively
    (**lower RIGHT and upper RIGHT on the left side**).
[ ] The **V1 / V2 vertical meridian** is documented as the
    representation of the vertical midline of the visual field.
[ ] No forward-declaration caveat is needed for the V-side
    neighbours (V2, V3, V4, BA 17, cuneus, calcarine sulcus, LGN
    all exist). The **lingual gyrus** is noted as a forward
    reference in ``..gyri``.
[ ] No SUBDIVISIONS promotion is performed while the BA 17
    functional counterpart under ``...brodmann_areas/
    brodmann_area_17_primary_visual`` is not yet split — the 1:1
    V1 ↔ BA 17 correspondence must be preserved.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURE,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, FUNCTIONAL_DOMAINS set, forward-declaration caveat
    text) match the right sibling; VISUAL_HEMIFIELD,
    DOMAIN_EMPHASIS, CONNECTIVITY emphasis, and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left V1
    carries "right_hemifield" in its DOMAIN_EMPHASIS entries and
    RETINOTOPIC_MAP; the right V1 carries "left_hemifield."
[ ] **The macular-sparing asymmetry is verified**: the left V1
    carries a **right** macular sparing anchor.
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical to
    BA 17's** — the 1:1 correspondence extends to the domains.
[ ] **The clinical anchors are verified to be identical to BA
    17's** — the 1:1 correspondence extends to the clinical
    syndromes.
[ ] **The left V1's downstream pathway** is verified to be the
    **left V1 → V2 → V3 → V4 → LOC → left VWFA** (reading), not
    the right FFA (faces).
[ ] Any downstream code querying "what does the left V1 see?"
    must receive "the RIGHT visual hemifield."
[ ] Any downstream code querying "what is V1?" must receive
    "the striate cortex / primary visual cortex / BA 17" — the
    1:1 V1 ↔ BA 17 correspondence is enforced.
[ ] Any downstream code assigning the reading pathway must route
    through the **left** V1 → V2 → V3 → V4 → LOC → left VWFA
    chain — the left V1 is the input stage, but it is **not**
    the reading operation.
[ ] Any downstream code assigning face processing must route
    through the **right** V1 → V2 → V3 → V4 → LOC → right FFA
    chain — the right V1 is the input stage of the right face
    pathway, but it is **not** the face operation.
[ ] **Any change to V1 must be mirrored to BA 17 in the same
    commit, in both hemispheres** — the 1:1 V1 ↔ BA 17
    correspondence requires the two packages to stay in lockstep.
"""