"""
Brodmann Area 19 (Tertiary Visual Cortex) — Left Hemisphere
============================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── brodmann_areas
                                    └── brodmann_area_19   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 19** — the **tertiary visual cortex**, the
extrastriate territory that **surrounds BA 18 (V2 + V3)** on the
lateral, dorsal, and ventral surfaces of the occipital lobe. It is the
**most heterogeneous** of the three occipital BAs and the **only one**
whose V-area correlates span **both** the ventral stream (V4, LOC) and
the dorsal stream (V5/MT+, V3A, V3B) — which is why its
`V_AREA_CORRELATE` field is a **six-element tuple**, the largest in the
cortex tree.

Parent: ``..brodmann_areas`` (left occipital BA registry) — sibling to
BA 17 and BA 18.

This package is the **structural mirror** of
``../../right/cortex/occipital/brodmann_areas/brodmann_area_19``. The
BA number, the six V-area correlates, the architectonic signatures, the
BA 18 / BA 19 border variability, and the stream-separation properties
are identical on both sides; the **functional emphasis** and
**clinical significance** diverge — on the left, BA 19 is weighted
toward **color / form / object processing** (the ventral stream and the
left visual word form area), **pure alexia without agraphia**, and
**left-lateralized color and object agnosia**, while the right BA 19
is weighted toward **motion / spatial / attentional processing** (the
dorsal stream and the right dorsal attention network), **prosopagnosia**,
and **left hemispatial neglect**.

**The most consequential structural fact about BA 19** is that it is
the **first BA in the cortex tree whose functional correlates span
BOTH visual streams**:

    Ventral stream (object / color / form)
        V4   — color and form; the origin of the ventral stream
        LOC  — lateral occipital complex; object recognition

    Dorsal stream (motion / space / attention)
        V3A  — motion and motion-in-depth
        V3B  — kinetic contours
        V5/MT+ — motion

    Shared with BA 18
        V3   — V3's lateral portion extends into BA 19 territory

This dual-stream identity is why **BA 19 lesions can produce deficits
in both ventral and dorsal visual processing**, and why the clinical
literature on BA 19 is dominated by **dissociations** (achromatopsia
without akinetopsia, akinetopsia without achromatopsia, object agnosia
without prosopagnosia, etc.) rather than by a single BA-19 syndrome.

--------------------------------------------------------------------------------
WHAT BA 19 IS
--------------------------------------------------------------------------------

BA 19 is the **tertiary visual cortex** — the extrastriate belt that
surrounds BA 18 and extends across:

    lateral surface         the **lateral occipital gyri** (the
                            lateral occipital complex, LOC, and
                            the lateral portion of V5/MT+)
    dorsal surface          the **dorsal V3A / V3B** territory
                            along the transverse occipital sulcus
    ventral surface         the **V4 / fusiform** territory and the
                            **ventral LOC**
    medial surface          small extensions adjacent to the
                            parieto-occipital sulcus

In Brodmann's original map, BA 19 is a **single cytoarchitectonic
area** — but modern retinotopic and functional parcellations
**subdivide it extensively**, because BA 19 is **not
architectonically homogeneous**. It is a **belt of association
cortex** whose subregions are distinguished primarily by their
**retinotopic signatures and functional properties**, not by
cytoarchitecture. The result is that BA 19 is the **least
architectonically specific** of the three occipital BAs, and the most
**functionally heterogeneous**.

**A note on the BA 18 / BA 19 border**. As documented in the BA 18
sibling, this is the **only variable BA border in the occipital
lobe**. The border roughly coincides with the **lunate sulcus**
(when present) on the lateral surface and with the **transverse
occipital sulcus** on the dorsal surface, but neither is a perfectly
reliable landmark. Modern parcellations subdivide the BA 18 / BA 19
transition under different labels, and downstream code should use the
**retinotopic** border (the V2/V3 border at the horizontal meridian,
or the V3/V3A border) rather than the architectonic one when
available.

**The architectonic signatures of BA 19** are:

    V4 (part of BA 19)      The **dysgranular / granular**
                            color-and-form cortex on the fusiform
                            gyrus and adjacent lateral occipital
                            cortex. Contains the **color globs**
                            (V4's modular organization for hue)
                            and projects forward to the LOC.

    V5 / MT+ (part of BA 19) The **agranular / dysgranular** motion
                            cortex at the occipito-temporal
                            junction. The **middle temporal area
                            (MT)** and the **medial superior
                            temporal area (MST)** are the two
                            main subregions of the MT+ complex.

    LOC (part of BA 19)     The **lateral occipital complex**, a
                            large object-recognition territory
                            on the lateral occipital surface.
                            Contains the **lateral occipital
                            (LO)** area for general objects and
                            the **fusiform face area (FFA)** at
                            its ventral edge (though FFA is
                            often assigned to BA 37 / temporal).

    V3A / V3B (part of BA 19) The **dorsal extrastriate** areas
                            adjacent to V3. V3A is the
                            motion-in-depth and motion-boundary
                            area; V3B is the kinetic-occipital
                            area.

**A crucial caveat about BA 19's functional specificity.** Unlike BA 17
(striate cortex, 1:1 with V1) or BA 18 (V2 + V3, two clean
functional areas), **BA 19 is a family of at least five distinct
functional areas** (V3A, V3B, V4, V5/MT+, LOC), each with its own
retinotopic map, its own architectonic signature, and its own
functional domain. The BA 19 label is therefore a **cytoarchitectonic
convenience** that groups together territories that modern
neuroscience would **not** treat as a single unit. Downstream code
that needs a specific functional area should query the V package
(V4, V5/MT+, LOC, etc.), not BA 19 as a whole.

**Left-hemisphere specificity**: the left BA 19's V4 and LOC
subregions are the **origin of the left ventral stream** that feeds
the **left visual word form area (VWFA)**. The left V4 → LOC → VWFA
pathway is the **left reading pathway**, and left BA 19 lesions can
produce **pure alexia without agraphia** when the lesion extends into
the left splenium (Dejerine syndrome) — the canonical
left-lateralized BA 19 deficit. **The left BA 19's V4 also carries
the left-lateralized color-and-form contribution to object
recognition**, and left V4 lesions produce **right hemiachromatopsia**
and **color agnosia**. The left BA 19's V5/MT+ contributes to
**right-hemifield motion perception**, but at a **weaker weighting
than the right BA 19's V5/MT+** (the right is the dominant motion
hemisphere).

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours
        caudomedially          BA 18 (V2 + V3) via the BA 18 / BA 19
                               border (variable; see caveat)
        rostrally              BA 37 (temporal, fusiform) ventrally;
                               BA 7 / BA 39 (parietal, superior
                               parietal lobule / angular gyrus)
                               dorsally; BA 21 / BA 22 (temporal)
                               rostroventrally
        medially               the parieto-occipital sulcus
                               (boundary with the parietal lobe)
        ventrally              the collateral sulcus / lingual
                               gyrus
        laterally             the lateral occipital gyri and the
                               occipito-temporal junction

    Functional overlays
        V4 — color and form (part of BA 19)
            The color and form area on the fusiform gyrus and
            adjacent lateral occipital cortex. **The origin of
            the ventral stream.** On the left, V4's outputs feed
            the LOC and the left VWFA — the **reading pathway**.
        V5 / MT+ — motion (part of BA 19)
            The motion area at the occipito-temporal junction.
            **The origin of the dorsal stream.** On the left,
            V5/MT+ contributes to right-hemifield motion
            perception, but the **right V5/MT+ is the dominant
            motion hemisphere**.
        LOC — object recognition (part of BA 19)
            The lateral occipital complex on the lateral occipital
            surface. **The object-recognition area of the ventral
            stream.** On the left, LOC's outputs feed the left
            VWFA for reading; on the right, LOC's outputs feed
            the right FFA for faces.
        V3A / V3B — motion and kinetic contours (part of BA 19,
        forward references)
            The dorsal extrastriate areas adjacent to V3. **Not
            yet packages under ``..cortex``** — recorded as
            forward references. On the right, V3A is more strongly
            engaged for motion-in-depth and visuospatial attention;
            on the left, V3A is present but weaker.
        lateral occipital gyrus — lateral surface
            The lateral occipital gyri carry the LOC and the
            lateral portion of V5/MT+. The gyral package
            cross-references BA 19 as its primary functional
            overlay.
        fusiform gyrus — ventral surface (forward reference in
        ``..gyri`` — not yet a package)
            The fusiform gyrus carries V4 and the ventral portion
            of LOC. **On the left, the fusiform gyrus's V4 → LOC
            output feeds the left VWFA** — the reading endpoint.
        lunate sulcus / transverse occipital sulcus — borders
            The lunate sulcus (when present) and the transverse
            occipital sulcus are the lateral / dorsal landmarks
            for the BA 18 / BA 19 border, **both variable**.

**This field is structurally identical to the right sibling's** — the
architectonic neighbours, the V4 / V5/MT+ / LOC / V3A / V3B overlays,
and the lateral occipital gyrus / fusiform gyrus / lunate sulcus /
transverse occipital sulcus landmarks are the same on both sides. What
differs is the **visual hemifield** — the left BA 19 processes the
RIGHT hemifield — and the **stream weighting** — the left BA 19 is
ventral-dominant (V4, LOC), the right BA 19 is dorsal-dominant
(V3A, V5/MT+).

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 18 (V2 + V3)                        **caudomedial neighbour** via
                                           the BA 18 / BA 19 border
                                           (variable; see caveat).
                                           **V3 is shared between
                                           BA 18 and BA 19** — its
                                           lateral portion extends
                                           into BA 19 territory.
    BA 17 (V1)                             **distant caudal neighbour**
                                           via BA 18; no direct
                                           adjacency
    BA 37 (temporal, fusiform)             **rostroventral neighbour**;
                                           continues the ventral
                                           stream from V4 / LOC
                                           into the fusiform face
                                           area (FFA) and the visual
                                           word form area (VWFA)
    BA 7 / BA 39 (parietal)                **rostrodorsal neighbour**;
                                           continues the dorsal stream
                                           from V5/MT+ / V3A into
                                           the parietal attention
                                           network
    BA 21 / BA 22 (temporal)               **rostrolateral neighbour**;
                                           the motion and object
                                           pathways continue into
                                           the lateral temporal
                                           cortex
    lateral occipital gyrus                carries the LOC and the
                                           lateral V5/MT+; **on the
                                           left, LOC feeds the left
                                           VWFA**
    fusiform gyrus (forward reference in   carries V4 and the ventral
    ..gyri)                                LOC; **on the left, the
                                           V4 → LOC → VWFA
                                           pathway is the reading
                                           pathway**
    lunate sulcus                          **lateral-surface landmark**
                                           for the BA 18 / BA 19
                                           border, **when present**
                                           (the lunate sulcus is
                                           inconstant in humans)
    transverse occipital sulcus            **dorsal-surface landmark**
                                           for the posterior boundary
                                           of the lateral occipital
                                           gyri and the V3A / V3B
                                           territory

**This field is byte-identical to the left sibling's** at the level of
BA-numbered neighbours and sulcal/gyral landmarks. The adjacency
relationships are topological, not lateralized.

**A note on BA 19's dual-stream neighbours.** BA 19 has **two distinct
downstream targets** — the **temporal lobe** (ventral stream: BA 37,
BA 21) and the **parietal lobe** (dorsal stream: BA 7, BA 39). This is
unlike BA 17 and BA 18, whose downstream targets are predominantly the
occipital hierarchy itself. **The dual-stream adjacency is a defining
structural feature of BA 19** and must be preserved in the
cross-references.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 19 participates in **five** canonical occipital functional domains,
the largest domain set of any occipital BA. On the left, the emphasis
is as follows:

    color_vision                                   (left emphasis — PRIMARY)
        **This is BA 19's most distinctive contribution** — the
        conscious perception of color, localized to V4 on the
        fusiform gyrus and adjacent lateral occipital cortex. V4's
        **color globs** are modular for hue, and V4 lesions produce
        **achromatopsia** (loss of color vision). **On the left,
        the color contribution is weighted toward the
        COLOR-FORM-LANGUAGE integration** — the left V4 → LOC →
        VWFA pathway carries color information forward to the
        reading network, and left V4 lesions produce **right
        hemiachromatopsia** plus **color agnosia** (impaired
        color naming).

    motion_perception                              (left emphasis — SECONDARY)
        **This is BA 19's second major contribution** — the
        perception of motion, localized to V5/MT+ at the
        occipito-temporal junction. V5/MT+ lesions produce
        **akinetopsia** (loss of motion perception). **On the
        left, the motion contribution is present but weaker than
        on the right** — the right V5/MT+ is the **dominant
        motion hemisphere**, and right V5/MT+ lesions produce
        more severe akinetopsia. The left V5/MT+ contributes to
        right-hemifield motion perception, but the left's
        contribution is a **contributor**, not the **substrate**.

    form_and_object_perception                     (left emphasis — PRIMARY)
        **This is BA 19's most left-lateralized contribution.**
        V4's color-form representations and the LOC's object
        representations contribute to **object recognition** in
        the ventral stream. **On the left, the form-and-object
        contribution is weighted toward the V4 → LOC → left VWFA
        pathway** — the **reading endpoint**. Left BA 19 lesions
        can produce **pure alexia without agraphia** (Dejerine
        syndrome) when the lesion extends into the left splenium.
        **The left BA 19 also contributes to visual object
        agnosia** (bilateral lesions are typically needed), and
        to **color-form agnosia** (left-lateralized).

    spatial_localization                           (left emphasis — SECONDARY)
        **This is BA 19's fourth contribution** — the early
        spatial-localization processing carried by V3A and
        V5/MT+'s motion-in-depth representation. **On the left,
        the spatial-localization contribution is present but
        weaker than on the right** — the right V3A and right
        V5/MT+ are more strongly engaged during visuospatial
        attention and motion-in-space processing, and the right
        BA 19 is part of the **right dorsal attention
        network**.

    visual_attention                               (left emphasis — SECONDARY)
        **This is BA 19's fifth contribution** — the dorsal-
        stream attentional target role carried by V3A and
        V5/MT+ in the right-lateralized dorsal attention network.
        **On the left, the attentional contribution is present
        but weaker than on the right** — the left V3A and left
        V5/MT+ receive attentional gain from the left IPS and
        left FEF, but the **right-lateralized dorsal attention
        network** is the dominant one.

**Left-specific caveat on `visual_word_processing`.** BA 19 is the
**third stage** of the left ventral stream that feeds the left
VWFA — V1 → V2 / V3 (BA 18) → V4 / LOC (BA 19) → VWFA (left fusiform).
**BA 19 is the stage where the reading pathway becomes functionally
distinguishable from other ventral-stream object processing**, because
the LOC's ventral stream can feed either the left VWFA (reading) or
the right FFA (faces). **The left BA 19's LOC feeds the left VWFA**,
and the left BA 19's role in the reading pathway is captured here as
**the downstream `form_and_object_perception` → left VWFA pathway**.
`visual_word_processing` as such is **not a primary domain** of BA 19
— the VWFA is in the fusiform gyrus, downstream of BA 19 — but the
left BA 19 is the **necessary input stage** for it.

**Left-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the left
BA 19 does **not** carry. `face_processing` is instantiated in the
right FFA (fed by the right BA 19 → LOC → FFA pathway);
`global_visual_processing` is a distributed right-hemisphere property
beginning at right BA 18 and continuing through the right BA 19.
Neither appears in the left BA 19 `FUNCTIONAL_DOMAINS` tuple.

**Summary**: BA 19 carries **exactly five** functional domains —
`color_vision`, `motion_perception`, `form_and_object_perception`,
`spatial_localization`, and `visual_attention`. This is the **largest
domain set of any occipital BA** (BA 17 has three, BA 18 has four),
reflecting BA 19's **dual-stream identity** and the **five distinct
V-areas it spans**. **The left emphasis is on `color_vision` (V4)
and `form_and_object_perception` (V4 + LOC → left VWFA)** — the
ventral stream — while the right's emphasis is on `motion_perception`
(V5/MT+), `spatial_localization` (V3A), and `visual_attention`
(dorsal attention network) — the dorsal stream.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → pulvinar (dominant, modulatory)
            **BA 19's dominant thalamic input is from the
            pulvinar**, not from the LGN. The pulvinar → V4 and
            pulvinar → MT/V5 projections are the primary
            subcortical inputs to BA 19, and they are part of the
            **cortico-thalamo-cortical loops** that support
            visual attention and visual short-term memory. This is
            unlike BA 17 (LGN-dominant) and BA 18 (V1-dominant via
            the relay), and it reflects BA 19's status as an
            **associative visual area** rather than a primary
            sensory cortex.
        → LGN (weak, koniocellular)
            The **koniocellular pathway** (via the LGN's
            koniocellular layers) provides a weak direct projection
            to V4, bypassing V1. This pathway carries the
            **blue-yellow (S-cone) color signal** and is part of
            the subcortical substrate for color vision that
            **survives V1 lesions** — the phenomenon of **blindsight
            for color**.

    cortical afferents
        → V2 / V3 (BA 18), left
            **BA 19's principal cortical afferent.** The V2 thin
            stripes project to V4 (color / form); the V2 thick
            stripes and V3 project to MT/V5 (motion); the V3 / V3A
            transition projects to V3A (motion-in-depth); and the
            V2 pale stripes project to the LOC (object form).
            **The V2 → BA 19 projections are the main cortical
            inputs to all five BA 19 functional areas**, and they
            are the reason BA 19 is the **third stage** of the
            visual hierarchy.
        → V1 (indirect, via BA 18)
            BA 19 has **no direct V1 projections** — the V1 →
            BA 18 → BA 19 relay is obligate for the V1-driven
            component of BA 19's input.

    cortical efferents
        → LOC (intra-BA 19), left
            V4's outputs project to the LOC within BA 19,
            contributing to the **object-recognition stage** of
            the ventral stream. On the left, the V4 → LOC pathway
            is the **first step of the left reading pathway**.
        → left visual word form area (VWFA), left
            The **LOC → VWFA projection** carries the object-form
            signal forward to the reading endpoint. **This is the
            left BA 19's most important efferent** and the basis
            of the left-lateralized reading pathway.
        → right fusiform face area (FFA), right — via the left
            BA 19 is **not** the source of the right FFA input;
            the right BA 19 is. The left BA 19 → right FFA
            connection exists via the callosal pathway but is
            **modulatory, not driving**.
        → parietal cortex (V3A, V5/MT+ → IPS, area 7), left
            V3A and V5/MT+ project forward to the **left
            intraparietal sulcus** and the **left dorsal
            attention network**. On the left, this projection is
            the substrate for **right-hemifield spatial
            attention**, but the left's contribution is weaker
            than the right's.
        → temporal cortex (V4, LOC → inferotemporal), left
            V4 and LOC project forward to the **left inferior
            temporal cortex** (BA 37, BA 21), continuing the
            ventral stream's object-recognition hierarchy. On the
            left, this pathway terminates at the **left VWFA**
            (reading) and the **left anterior temporal semantic
            hub**.
        → MT/V5 (intra-BA 19), left
            V3A's outputs project to MT/V5 within BA 19,
            contributing to the **motion-perception stage** of
            the dorsal stream. On the left, the V3A → MT/V5
            pathway is the left's contribution to right-hemifield
            motion perception.

    callosal connections
        → right BA 19
            The callosal fibers connect the left BA 19 to the
            right BA 19 across the occipital midline, supporting
            **the fusion of the two hemifields** at the V4 and
            MT/V5 stage. The callosal traffic carries the **right-
            hemifield color-form signal** (left BA 19) and the
            **left-hemifield motion signal** (right BA 19).

    attentional feedback
        → frontal eye fields (BA 8), left
            The left FEF sends **top-down attentional gain** to
            the left BA 19, modulating V4 and MT/V5 responses to
            behaviourally relevant stimuli. **On the left, the FEF
            → BA 19 projection is part of the left dorsal
            attention network's contribution to right-hemifield
            spatial attention** — present but weaker than the
            right FEF → right BA 19 projection.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), left
            The DLPFC sends top-down attentional and working-memory
            signals to the left BA 19, supporting **visual
            working memory** and **visual imagery**, and
            contributing to the **left reading network**'s
            top-down control.
        → intraparietal sulcus, left
            The left IPS sends dorsal-attention-network signals to
            the left BA 19, supporting **spatial attention** in
            the RIGHT visual hemifield. **On the left, the IPS →
            BA 19 projection is present but weaker than on the
            right.**

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in four respects:
(a) the **pulvinar → V4** projection carries the color-form signal
that the left uses for **color-form-language integration** and the
reading pathway;
(b) the **LOC → left VWFA** pathway is the **reading endpoint**, not
the face endpoint (which is the right's LOC → FFA pathway);
(c) the **V3A / V5/MT+ → left IPS** pathway is present but weaker than
the right's, consistent with the right's dominant dorsal attention
network;
(d) the callosal traffic carries the **right-hemifield color-form**
signal (from the left) and the **left-hemifield motion** signal (from
the right).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_ba19_right_hemiachromatopsia
        **This is the left BA 19 anchor par excellence.** A lesion
        of the left V4 (part of BA 19 on the fusiform gyrus)
        produces **right hemiachromatopsia** — loss of color
        vision in the RIGHT half of the visual field of both eyes,
        with preserved color vision in the left hemifield. **The
        left V4 lesion spares the left hemifield's color
        perception** because the right V4 (fed by the right
        occipital lobe) is intact. **Bilateral V4 lesions produce
        complete achromatopsia** — the patient sees the world in
        shades of gray. **This is the mirror of the right BA 19's
        left hemiachromatopsia anchor.**

    left_ba19_pure_alexia_without_agraphia
        **Alexia without agraphia** (Dejerine 1892) — the patient
        can **write** but cannot **read what they have written** —
        results from a **left occipital lesion that disconnects
        the intact right occipital cortex from the left language
        areas**. The classic lesion is **left PCA infarct
        involving the left BA 19 (V4 and LOC) and the left
        splenium of the corpus callosum**. **The BA 19-specific
        contribution is the left V4 / LOC damage**, which removes
        the left hemifield's object-form input to the left VWFA;
        the **splenium damage** removes the callosal relay of the
        intact right hemifield's object-form signal. **This is
        the canonical left-lateralized BA 19 clinical syndrome**,
        and it has no symmetric counterpart on the right — the
        right splenium does not connect to a right reading
        network.

    left_ba19_color_agnosia
        **Color agnosia** — impaired ability to **name** or
        **recognize** colors despite intact color perception —
        is a **left-lateralized** syndrome that involves the left
        V4 → LOC → left temporal language network. The patient
        can match colors (V4 perception is intact) but cannot
        name them or use them semantically. **This is a left-
        lateralized anchor** — right V4 lesions produce
        hemiachromatopsia (perceptual deficit) but not color
        agnosia (recognition deficit) at the same weighting.

    left_ba19_visual_object_agnosia
        **Visual object agnosia** — impaired ability to recognize
        objects despite intact visual perception — typically
        requires **bilateral** lesions of the ventral stream
        (V4, LOC, and inferotemporal cortex). **Left BA 19
        lesions contribute to the apperceptive component** of
        visual object agnosia (the failure to form a coherent
        object percept from visual features) more than the
        associative component (the failure to link a percept to
        semantic knowledge). **The bilateral requirement** means
        that isolated left BA 19 lesions produce a **milder**
        object-recognition deficit than isolated left BA 18 or
        BA 17 lesions, because the right hemifield's object-form
        signal can compensate via the callosum.

    left_ba19_right_hemifield_akinetopsia
        **Akinetopsia** — impaired motion perception — from a
        **left V5/MT+ lesion** produces **right hemifield
        motion deficits** (the patient has difficulty perceiving
        motion in the RIGHT visual field). **The deficit is
        milder than the right V5/MT+ lesion's left hemifield
        deficit** — the right V5/MT+ is the dominant motion
        hemisphere, and the left V5/MT+ contributes but is not
        the primary substrate. **Complete akinetopsia** (the
        famous "motion blindness" of patient LM) requires
        **bilateral V5/MT+ lesions**.

    left_ba19_right_hemifield_motion_deficit_in_daily_life
        **Left V5/MT+ lesions can produce functional motion
        deficits** — difficulty judging the speed of approaching
        objects, difficulty following moving targets, and
        difficulty in motion-heavy environments (traffic,
        crowds) — **in the RIGHT visual field**. The deficit is
        typically **milder** than the right-side equivalent
        because the left's motion contribution is smaller, and
        the patient often compensates by using the intact left
        hemifield.

    left_ba19_color_and_motion_processing_dissociation
        **The left BA 19's five functional areas are
        architectonically interleaved but functionally
        dissociable.** A focal left V4 lesion produces
        achromatopsia **without** akinetopsia; a focal left
        V5/MT+ lesion produces akinetopsia **without**
        achromatopsia. **The dissociations are the strongest
        clinical evidence that color and motion are processed
        by separate cortical areas**, and the left BA 19 is a
        clean natural experiment for this dissociation because
        both V4 and V5/MT+ live within its territory.

    left_ba19_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** involving
        BA 19 produces a **right homonymous hemianopia or
        quadrantic defect** (from BA 17 / BA 18 involvement)
        **plus** a **right hemiachromatopsia** (from left V4
        involvement) **plus** a **right hemifield
        motion-perception deficit** (from left V5/MT+
        involvement) **plus** — if the left splenium is
        involved — **alexia without agraphia**. **The BA 19-
        specific contribution is the color and motion deficits
        that extend beyond the field defect**, and the alexia
        without agraphia when the splenium is involved.

    left_ba19_color_form_language_integration_deficit
        **Left BA 19's V4 → LOC → left VWFA pathway is the
        substrate of color-form-language integration** — the
        ability to name colored objects, use color in reading
        (e.g., colored letters), and integrate color with
        object semantics. Left BA 19 lesions can produce
        **color-form-language integration deficits** — the
        patient can name objects and colors separately but
        cannot integrate them in a linguistic context. **This
        is a left-lateralized anchor** with no symmetric
        counterpart on the right.

    left_ba19_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **BA 17, BA 18, AND BA 19**. **The
        BA 19 contribution is the propagation of the visual aura
        into the** color (V4) **and** motion (V5/MT+) **features
        of the aura** — colored fortifications, motion phosphenes,
        and complex visual hallucinations. **This anchor is
        hemisphere-invariant**, but the aura's field involvement
        is contralateral (right field on the left side).

    left_ba19_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **BA 17, BA 18, OR BA 19**. **BA 19 auras**
        are typically **more complex than BA 18 auras** — the
        patient may see **formed objects, colored scenes, or
        motion hallucinations** in addition to elementary shapes
        and fortifications. **Left BA 19 auras** project to the
        **right visual field** and can be preceded or accompanied
        by **visual field defects, achromatopsia, or
        akinetopsia** that persist after the seizure.

    left_ba19_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **BA 19 extensively**, including
        V4, V5/MT+, and the LOC. **Left BA 19** is part of the
        substrate of the **progressive ventral stream
        dysfunction** that produces **progressive reading
        deficits** (the "visual variant" of progressive
        aphasia) and **progressive color and object agnosia**.
        **On the left, PCA presents with the language-and-reading
        syndrome**; on the right, with the visuospatial /
        prosopagnosic syndrome (Benson syndrome).

    left_ba19_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects** from **bilateral occipital
        involvement**. **The BA 19 contribution is the
        extrastriate involvement** that produces **complex visual
        hallucinations** (V4 color hallucinations, V5/MT+ motion
        hallucinations) and **higher-order visual field defects**
        (V4 and MT/V5 partial loss). **The syndrome is
        reversible** in most cases.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 19 processes the **RIGHT visual hemifield**, so
left BA 19 lesions produce **right-sided** visual deficits; (b) the
left BA 19 is the **third stage of the left reading pathway** and
the **left-lateralized color-form-language integration substrate**,
so left BA 19 lesions can produce **pure alexia without agraphia**
and **color agnosia** that have no symmetric counterpart on the
right. **The V4 / LOC → left VWFA pathway** is a third
left-specific feature — the left BA 19 is ventral-stream-dominant,
while the right BA 19 is dorsal-stream-dominant. The right sibling's
docstring carries the corresponding right-sided anchors (left
hemiachromatopsia, prosopagnosia from right LOC → FFA involvement,
left hemifield akinetopsia (more severe), left hemispatial neglect
contribution, and the right-lateralized dorsal-attention emphasis).

**The `migraine_aura`, `occipital_epilepsy`, `PCA`, `PRES`, and
`occipital_infarct` anchors are hemisphere-invariant** — they appear
on both sides and are documented identically in both siblings, with
the side-appropriate field label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left occipital BA registry. This package's parent, source
    of the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 19 (which on
    the left is ``("color_vision",
    "motion_perception_weaker_than_right",
    "form_and_object_perception_ventral_stream_to_left_vwfa",
    "spatial_localization_v3a_weaker_than_right",
    "visual_attention_lower_weighting_than_right")``), and enforcer
    of the **six-element V_AREA_CORRELATE** (v3, v4, V3A, V3B,
    V5_MT_plus, LOC) — the largest in the cortex tree.

..brodmann_area_17_primary_visual
    **Distant caudal neighbour**; no direct adjacency (BA 18
    intervenes). BA 17's V1 outputs reach BA 19 via the **BA 18
    relay**, not directly. BA 17 is the primary sensory cortex;
    BA 19 is the associative extrastriate cortex — different
    levels of the visual hierarchy.

..brodmann_area_18
    **Caudomedial neighbour** via the **variable** BA 18 / BA 19
    border. V2's and V3's outputs are the principal cortical
    inputs to all five BA 19 functional areas. **V3 is shared
    between BA 18 and BA 19** — its lateral portion extends
    into BA 19 territory. **The BA 18 / BA 19 border variability
    is the most consequential adjacency issue for BA 19** —
    downstream code must use the retinotopic landmark when
    available.

...cortex.v4
    The **functional V4 package under ``..cortex``** — the direct
    counterpart of the V4 component of BA 19. **On the left,
    V4's outputs feed the LOC and the left VWFA** — the reading
    pathway. V4 is the **color and form origin of the ventral
    stream** and the substrate of achromatopsia.

...cortex.v5_mt_plus  (forward reference in the sense that
    V5/MT+ is not yet a package, but the V_AREA_CORRELATE
    field references it)
    The **functional V5/MT+ package** — not yet a package under
    ``..cortex``, but a **required forward reference** in the
    BA 19 crosswalk. **On the left, V5/MT+ contributes to
    right-hemifield motion perception** at a **weaker weighting**
    than the right V5/MT+. V5/MT+ is the substrate of
    akinetopsia.

...cortex.loc  (forward reference)
    The **functional LOC package** — not yet a package under
    ``..cortex``, but a **required forward reference** in the
    BA 19 crosswalk. **On the left, LOC's outputs feed the left
    VWFA** — the reading endpoint.

...cortex.v3  (shared with BA 18)
    The **functional V3 package under ``..cortex``** — shared
    between BA 18 and BA 19. **V3's lateral portion extends
    into BA 19 territory**, which is why V3 appears in both
    BA 18's and BA 19's `V_AREA_CORRELATE` tuples.

...cortex.v3a / ...cortex.v3b  (forward references)
    The **functional V3A and V3B packages** — not yet packages
    under ``..cortex``. Recorded as forward references in the
    parent registry. **On the right, V3A is the more strongly
    engaged side** for motion-in-depth and visuospatial attention.

...gyri.lateral_occipital_gyrus
    The lateral-surface gyral territory. BA 19's LOC and lateral
    V5/MT+ overlay the lateral occipital gyrus. **On the left,
    the lateral occipital gyrus's LOC is part of the left
    reading pathway** (LOC → VWFA).

...gyri  (forward reference — the fusiform gyrus is not yet a
    package)
    The fusiform gyrus carries V4 and the ventral LOC. **On the
    left, the fusiform gyrus's V4 → LOC output feeds the left
    VWFA** — the reading endpoint. The **right FFA** is also on
    the fusiform gyrus (right side), but the FFA is downstream
    of BA 19 (in BA 37 territory), not part of BA 19 proper.

...sulci.lunate_sulcus
    The **lateral-surface landmark** for the BA 18 / BA 19
    border, **when present** (the lunate sulcus is inconstant in
    humans). When absent, the BA 18 / BA 19 border must be
    inferred from the retinotopic V2/V3 border rather than the
    architectonic one.

...sulci.transverse_occipital_sulcus
    The **dorsal-surface landmark** for the posterior boundary
    of the lateral occipital gyri and the V3A / V3B territory.

..cortex.temporal
    The **ventral stream** continues from BA 19 (V4, LOC) into
    the temporal lobe (inferior temporal cortex, fusiform
    gyrus). **On the left, the ventral stream terminates in
    the left VWFA** (the reading area), and the left BA 19 is
    the **third stage** of this pathway. **Right occipito-
    temporal lesions produce prosopagnosia** — the canonical
    right-lateralized visual-recognition deficit, with the
    right FFA as its endpoint. The temporal package must declare
    the left BA 19 as a source of its visual input via the
    ventral stream, and must note both the **left-lateralized
    VWFA** and the **right-lateralized FFA** specializations.

..cortex.parietal
    The **dorsal stream** continues from BA 19 (V3A, V5/MT+)
    into the parietal lobe (IPS, area 7). **On the right, the
    dorsal stream is more strongly engaged during visuospatial
    attention** — the right V3A and right V5/MT+ are core nodes
    of the right-lateralized dorsal attention network. The
    parietal package must declare the left BA 19 as a source of
    its visual input for the dorsal stream, and must note the
    right-lateralized attentional emphasis.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to BA 19. **On the right, the right FEF is the
    dominant node of the ventral attention network**, and right
    frontal lesions contribute to left hemispatial neglect. The
    frontal package must declare the left BA 19 as a target of
    its attentional projections.

..cortex.cingulate  — indirect
    No direct cingulate → BA 19 projection. Recorded here to
    pre-empt a false cross-reference.

..cortex.insular  — indirect
    No direct insular → BA 19 projection. Recorded here to
    pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/pulvinar
    **The pulvinar is BA 19's dominant thalamic input.** The
    pulvinar → V4 and pulvinar → MT/V5 projections are the
    primary subcortical inputs to BA 19, unlike BA 17 (LGN) and
    BA 18 (V1 relay). The thalamus package must declare the
    pulvinar as the dominant thalamic relay to BA 19, and must
    note the pulvinar's role in the cortico-thalamo-cortical
    loops that support visual attention and visual short-term
    memory.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN's koniocellular pathway** provides a **weak direct
    projection to V4**, bypassing V1. This pathway carries the
    **blue-yellow (S-cone) color signal** and is part of the
    subcortical substrate that **survives V1 lesions** — the
    phenomenon of **blindsight for color**. The thalamus package
    must declare the LGN's koniocellular layers as a weak
    afferent to left BA 19 (V4).

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from BA 19 (V4, LOC) to the
    perirhinal, entorhinal, and parahippocampal cortices.
    **The left BA 19 is the third stage** of the occipito-
    temporal-hippocampal pathway that supports visual object
    recognition and visual memory. **On the right, the
    parahippocampal place area (PPA) and the retrosplenial
    complex receive visual input supporting scene and spatial
    memory**, which are more strongly right-lateralized.

../../right/cortex/occipital/brodmann_areas/brodmann_area_19
    The right-hemisphere homologue. Structural fields (BA
    number, six-element V-area correlates, architectonic
    signatures, BA 18 / BA 19 border variability, dual-stream
    identity, lateral occipital gyrus / fusiform gyrus
    relationships) MUST be byte-identical. Functional emphasis
    and clinical significance diverge — the right BA 19
    processes the **LEFT** visual hemifield, is weighted toward
    **motion perception (V5/MT+), spatial localization (V3A),
    and visual attention (dorsal attention network)**, and its
    V4 / LOC outputs feed the right ventral stream toward the
    right FFA (for faces) rather than the left VWFA (for
    reading).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_19"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    BRODMANN_NUMBER     = 19
    ALTERNATE_NAMES     = ("tertiary_visual_cortex",
                           "extrastriate_association_cortex",
                           "V3A_V3B_V4_V5MT_LOC_complex")
        # **Five-component complex** — the largest alternate-name
        # set in the cortex tree. BA 19 is not a single V area
        # but a **family** of at least five.

    ARCHITECTONIC_SIGNATURES = (
        "color_globs_in_V4",
        "agranular_V5_MT_plus",
        "variable_BA18_BA19_border",
        "dual_stream_identity",
    )
        # **Four signatures**: V4's color globs, V5/MT+'s
        # agranular motion cortex, the variable BA 18 / BA 19
        # border, and the **dual-stream identity** (BA 19 is the
        # only BA whose V correlates span both ventral and
        # dorsal streams).

    V_AREA_CORRELATE    = ("v3", "v4", "V3A", "V3B", "V5_MT_plus",
                           "LOC")
        # **Six elements** — the largest V_AREA_CORRELATE in the
        # cortex tree. **Two current packages** (v3, v4) plus
        # **four forward references** (V3A, V3B, V5_MT_plus,
        # LOC). **v3 is shared with BA 18** — the lateral
        # portion of V3 extends into BA 19 territory.

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** BA 19 is unique to the
        # occipital lobe.

    RETINOTOPIC_MAP     = "multiple_mirror_flips_V3A_V4_V5MT_LOC"
        # BA 19 is not a single retinotopic map but **five
        # distinct maps**, each mirror-flipped relative to its
        # predecessor. V3A is a mirror-flip of V3 across the
        # V3/V3A border; V4 is a mirror-flip of V3A (or V3) across
        # the ventral border; MT/V5 has its own retinotopic map
        # (with a coarse hemifield representation and a strong
        # foveal emphasis); LOC has a **large receptive field,
        # partially retinotopic** representation. **On the left,
        # the represented hemifield is the RIGHT hemifield for
        # all five maps.**

    FUNCTIONAL_DOMAINS  = (
                              "color_vision",
                              "motion_perception",
                              "form_and_object_perception",
                              "spatial_localization",
                              "visual_attention",
                              # NOTE: primary_visual_processing is
                              # EXCLUDED (that is BA 17's domain).
                              # NOTE: primary_visual_processing_
                              # secondary and binocular_vision are
                              # EXCLUDED (BA 18's domains).
                              # NOTE: visual_word_processing is
                              # EXCLUDED as a BA 19 domain — BA 19
                              # is the *third stage* of the left
                              # reading pathway, but the reading
                              # operation is in the left VWFA
                              # (fusiform, downstream of BA 19).
                              # NOTE: face_processing is EXCLUDED
                              # (right-lateralized; not
                              # instantiated on the left BA 19).
                              # NOTE: global_visual_processing is
                              # EXCLUDED (a right-hemisphere
                              # emphasis within `form_and_object_
                              # perception`, not a separate
                              # domain).
                          )

    DOMAIN_EMPHASIS     = {   # left-side emphasis per domain
                              "color_vision":
                                  "color_form_language_integration_"
                                  "left_vwfa_pathway_right_"
                                  "hemiachromatopsia",
                              "motion_perception":
                                  "motion_perception_weaker_than_"
                                  "right_left_hemifield_motion_"
                                  "boundary",
                              "form_and_object_perception":
                                  "object_recognition_left_vwfa_"
                                  "reading_pathway_ventral_stream_"
                                  "right_hemifield",
                              "spatial_localization":
                                  "v3a_v5_spatial_localization_"
                                  "weaker_than_right_left_"
                                  "hemifield",
                              "visual_attention":
                                  "attentional_target_lower_"
                                  "weighting_than_right",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_ba19_right_hemiachromatopsia",
                              "left_ba19_pure_alexia_without_"
                              "agraphia",
                              "left_ba19_color_agnosia",
                              "left_ba19_visual_object_agnosia",
                              "left_ba19_right_hemifield_"
                              "akinetopsia",
                              "left_ba19_right_hemifield_motion_"
                              "deficit_in_daily_life",
                              "left_ba19_color_and_motion_"
                              "processing_dissociation",
                              "left_ba19_occipital_infarct_pca_"
                              "territory",
                              "left_ba19_color_form_language_"
                              "integration_deficit",
                              "left_ba19_migraine_visual_aura",
                              "left_ba19_occipital_epilepsy_"
                              "visual_auras",
                              "left_ba19_posterior_cortical_"
                              "atrophy",
                              "left_ba19_pres_visual_symptoms",
                          )

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "AREA_NAME",
        "HEMISPHERE",
        "LOBE",
        "BRODMANN_NUMBER",
        "ALTERNATE_NAMES",
        "ARCHITECTONIC_SIGNATURES",
        "V_AREA_CORRELATE",
        "NAMING_COLLISION_WITH",
        "RETINOTOPIC_MAP",
        "FUNCTIONAL_DOMAINS",
        "DOMAIN_EMPHASIS",
        "CONNECTIVITY",
        "CLINICAL_ANCHORS",
        "SUBDIVISIONS",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references BA 19 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is a forward-declaration caveat for this package, and it is the
largest in the cortex tree.** Of the six V-area correlates in the
`V_AREA_CORRELATE` field, only **two are current packages** under
``..cortex`` (v3, v4). The other **four are forward references**:

    V3A          — motion-in-depth and motion-boundary area;
                   **on the right, the more strongly engaged side**
    V3B          — kinetic-occipital area; motion processing
    V5_MT_plus   — motion area; **on the right, the dominant
                   motion hemisphere**
    LOC          — lateral occipital complex; object recognition;
                   **on the left, feeds the left VWFA**

**The four forward references must be resolved before BA 19's package
is finalised**, because BA 19 is not a coherent territory without
them — it is defined as the extrastriate belt **surrounding** BA 18,
and the four forward-reference areas are **most of that belt**. When
they are created under ``..cortex``:

  1. Add the V packages under ``..cortex/``.
  2. Remove the corresponding entries from ``FORWARD_REFERENCE_V_
     AREAS`` in the parent registry, **in both hemispheres in the
     same commit**.
  3. Update each V child's ``BRODMANN_CORRELATES`` to declare
     ``(19,)`` (matching the parent's ``V_TO_BA_CROSSWALK``).
  4. Verify the parent's ``BA_TO_V_CROSSWALK`` and
     ``V_TO_BA_CROSSWALK`` remain exact inverses.

**No asymmetry is permitted in the V-area forward references.** Both
hemispheres must declare the same forward-reference list and must
resolve them in the same commit.

**A second caveat**: the **BA 18 / BA 19 border variability** is
documented in the BA 18 sibling, but it is **more consequential for
BA 19** because BA 19's V4 and V3A correlates straddle the border.
The border is not architectonically crisp, and downstream code must
use the **retinotopic** landmark (V2/V3 border, V3/V3A border) when
available.

**A third caveat**: the **lingual gyrus** is a forward reference in
``..gyri`` — not yet a package. As with BA 17 and BA 18, its placement
question (parent level, like the cuneus, or under ``..gyri``) is
open and must be resolved in the same commit as its creation.

**All caveats are byte-identical to the right sibling's** — they are
properties of the occipital lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 19 is **the most architectonically heterogeneous** of the three
occipital BAs, and the **natural split** is into its **five functional
components**:

    brodmann_area_19/
        __init__.py
        v4_component/
            __init__.py
        v5_mt_plus_component/
            __init__.py
        loc_component/
            __init__.py
        v3a_component/           # forward reference
            __init__.py
        v3b_component/           # forward reference
            __init__.py

Then:

  1. Add the five component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**This promotion is strongly recommended** — BA 19 is not a coherent
territory in modern neuroscience, and the six-element
`V_AREA_CORRELATE` field records the **incoherence**. If the promotion
is performed, the parent BA 19 package becomes a **registry of five
sub-packages** rather than a description of a single architectonic
entity, which is more honest about BA 19's actual structure.

**The V4 / V5/MT+ / LOC split must be mirrored by corresponding splits
of the `..cortex/v4`, `..cortex/v5_mt_plus`, and `..cortex/loc`
packages** — the BA 19 → V4 / V5/MT+ / LOC correspondence means that
any BA 19 split must be matched by a V-area split in ``..cortex``, in
the same commit, in both hemispheres.

**The V3A / V3B split is blocked** until V3A and V3B are themselves
resolved as packages (currently forward references). The resolution
(V3A / V3B as BA 19 sub-areas, or as BA 18 sub-areas) must be made
**before** the BA 19 five-way split, and the resolution must be
hemisphere-invariant.

**A particular caution about V4**: V4 is often **split into V4 and
V4α (or V4v)** in modern parcellations, with V4α in the collateral
sulcus / fusiform region and V4 in the lateral occipital region.
**Any BA 19 split must decide whether V4 is one component or two**,
and the decision must be made in the same commit as the V4 package's
own subdivision (if any).

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_19``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "brodmann_area_19"
        LOBE                         "occipital"
        BRODMANN_NUMBER              19
        ALTERNATE_NAMES              (the five-component complex
                                     name)
        ARCHITECTONIC_SIGNATURES     (four signatures —
                                     V4 color globs, V5/MT+
                                     agranular, variable BA 18 /
                                     BA 19 border, dual-stream
                                     identity)
        V_AREA_CORRELATE             ("v3", "v4", "V3A", "V3B",
                                     "V5_MT_plus", "LOC") — six
                                     elements, largest in the
                                     cortex tree
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same multi-mirror-flip
                                     structure (V3A, V4, V5/MT+,
                                     LOC each with their own map)
        FUNCTIONAL_DOMAINS set       the same five domains
                                     (color_vision,
                                     motion_perception,
                                     form_and_object_perception,
                                     spatial_localization,
                                     visual_attention)
        Bounding / overlapping territories
        BA-to-neighbour adjacency
        CONNECTIVITY                 same bundle names (pulvinar
                                     dominant; the V2 → BA 19
                                     pathway is the same)
        The forward-declaration caveat text (byte-identical —
                                     the four V-area forward
                                     references, the BA 18 / BA
                                     19 border variability, and the
                                     lingual gyrus placement are
                                     all lobe-level concerns, not
                                     hemisphere-level)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — left BA 19 processes
                               the RIGHT hemifield; right BA 19
                               processes the LEFT hemifield.
                               The maps' *structure* is the same;
                               the *label* is flipped.
        DOMAIN_EMPHASIS        left: color_vision is "color_form_
                               language_integration_left_vwfa_
                               pathway_right_hemiachromatopsia";
                               motion_perception is "motion_
                               perception_weaker_than_right_left_
                               hemifield_motion_boundary";
                               form_and_object_perception is
                               "object_recognition_left_vwfa_
                               reading_pathway_ventral_stream_
                               right_hemifield";
                               spatial_localization is "v3a_v5_
                               spatial_localization_weaker_than_
                               right_left_hemifield";
                               visual_attention is "attentional_
                               target_lower_weighting_than_right".
                               right: color_vision is "color_
                               form_right_hemiachromatopsia_
                               left_hemifield"; motion_perception
                               is "motion_perception_dominant_
                               left_hemifield_akinetopsia"; form_
                               and_object_perception is "object_
                               recognition_right_ffa_face_
                               pathway_ventral_stream_left_
                               hemifield"; spatial_localization
                               is "v3a_v5_spatial_localization_
                               dominant_left_hemifield"; visual_
                               attention is "attentional_target_
                               dorsal_attention_network_dominant".
        CONNECTIVITY           same bundle names; left: the
                               pulvinar → V4 loop feeds the left
                               color-form-language integration;
                               the LOC → left VWFA pathway is
                               the reading endpoint; the
                               V3A / V5/MT+ → left IPS pathway
                               is present but weaker than the
                               right's.
                               right: the pulvinar → V5/MT+ loop
                               feeds the right motion hemisphere;
                               the LOC → right FFA pathway is
                               the face endpoint; the
                               V3A / V5/MT+ → right IPS pathway
                               is the dominant dorsal-stream
                               contribution.
        CLINICAL_ANCHORS       left: thirteen anchors (right
                               hemiachromatopsia, pure alexia
                               without agraphia (Dejerine),
                               color agnosia, visual object
                               agnosia (apperceptive component),
                               right hemifield akinetopsia,
                               right hemifield motion deficit,
                               color/motion dissociation, left
                               PCA infarct, color-form-language
                               integration deficit, migraine
                               aura, occipital epilepsy, PCA,
                               PRES).
                               right: fourteen anchors (left
                               hemiachromatopsia, **prosopagnosia
                               from right LOC → FFA involvement**,
                               **left hemifield akinetopsia
                               (more severe)**, **left
                               hemispatial neglect contribution**,
                               **right dorsal attention network
                               target**, visual object agnosia
                               (associative component, bilateral),
                               color/motion dissociation, right
                               PCA infarct, global form
                               processing deficit, migraine
                               aura, occipital epilepsy, PCA
                               (Benson syndrome), PRES).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same BA 19, the same six
V-area correlates, the same dual-stream identity, and the same
multi-mirror-flip retinotopy — but the *represented hemifield* is
**flipped**.

**The ventral-vs-dorsal stream emphasis is the second sharpest entry.**
Both hemispheres carry the same five functional domains — the set is
**identical** — but the **left** BA 19's emphasis is on **color /
form / object processing** (the ventral stream and the left VWFA),
and the **right** BA 19's emphasis is on **motion / spatial /
attentional processing** (the dorsal stream and the right dorsal
attention network). **Neither emphasis is a separate domain** — the
domain set is identical — but the emphasis determines which **clinical
deficit pattern** a lesion produces.

**The right-specific clinical anchors are the third sharpest entry.**
The right BA 19 carries **four anchors** that the left does not carry
at the same weighting: `right_ba19_left_hemispatial_neglect_
contribution`, `right_ba19_right_dorsal_attention_network_target`,
`right_ba19_prosopagnosia` (via the right LOC → FFA pathway), and
`right_ba19_left_hemifield_akinetopsia` (more severe than the left's).
The left BA 19's `left_ba19_pure_alexia_without_agraphia`,
`left_ba19_color_agnosia`, and `left_ba19_color_form_language_
integration_deficit` anchors are **left-only**. The checklist
verifies these asymmetries.

**The V_AREA_CORRELATE, the four ARCHITECTONIC_SIGNATURES, the
RETINOTOPIC_MAP structure, and the FUNCTIONAL_DOMAINS set are
byte-identical on both sides.** They are properties of the
extrastriate cortex itself, not of the hemisphere.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (the syndrome, not the subtype emphasis), PRES, and
occipital infarct — are **documented identically in both siblings**
and must not be allowed to drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_19".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] BRODMANN_NUMBER is 19.
[ ] ALTERNATE_NAMES includes "tertiary_visual_cortex",
    "extrastriate_association_cortex", and
    "V3A_V3B_V4_V5MT_LOC_complex".
[ ] ARCHITECTONIC_SIGNATURES includes the **four** signatures:
    color globs in V4, agranular V5/MT+, variable BA 18 / BA 19
    border, and **dual-stream identity** (the key feature — BA 19
    is the only BA whose V correlates span both streams).
[ ] V_AREA_CORRELATE is **exactly** ``("v3", "v4", "V3A", "V3B",
    "V5_MT_plus", "LOC")`` — a **six-element tuple**, the largest
    in the cortex tree. **Two current packages** (v3, v4) plus
    **four forward references** (V3A, V3B, V5_MT_plus, LOC).
[ ] **v3 is shared with BA 18** — the lateral portion of V3
    extends into BA 19 territory, which is why v3 appears in both
    BA 18's and BA 19's `V_AREA_CORRELATE` tuples.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **multi-mirror-flip** structure:
    - V3A is a mirror-flip of V3
    - V4 is a mirror-flip of V3A (or V3)
    - V5/MT+ has its own retinotopic map
    - LOC has a large-receptive-field, partially retinotopic map
    - **represented hemifield = RIGHT hemifield on the left side**
[ ] FUNCTIONAL_DOMAINS contains **five** domains — the largest
    domain set of any occipital BA:
    - color_vision
    - motion_perception
    - form_and_object_perception
    - spatial_localization
    - visual_attention
[ ] FUNCTIONAL_DOMAINS **excludes** primary_visual_processing (BA
    17's domain).
[ ] FUNCTIONAL_DOMAINS **excludes** primary_visual_processing_
    secondary and binocular_vision (BA 18's domains).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing as a
    **BA 19 domain** — BA 19 is the *third stage* of the left
    reading pathway, but the reading operation is in the left
    VWFA (fusiform, downstream of BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing (right-
    lateralized; not instantiated on the left BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** global_visual_processing (a
    right-hemisphere emphasis within `form_and_object_
    perception`, not a separate domain).
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis**:
    - color_vision → color_form_language_integration_left_vwfa_
      pathway_right_hemiachromatopsia
    - motion_perception → motion_perception_weaker_than_right_
      left_hemifield_motion_boundary
    - form_and_object_perception → object_recognition_left_vwfa_
      reading_pathway_ventral_stream_right_hemifield
    - spatial_localization → v3a_v5_spatial_localization_weaker_
      than_right_left_hemifield
    - visual_attention → attentional_target_lower_weighting_than_
      right
[ ] CONNECTIVITY documents:
    - Pulvinar thalamic afferent (dominant; stronger to BA 19
      than to BA 17 / BA 18; part of the cortico-thalamo-
      cortical attention and working-memory loops)
    - LGN koniocellular direct-to-V4 afferent (weak; carries
      S-cone blue-yellow color; survives V1 lesions = blindsight
      for color)
    - V2 / V3 → BA 19 principal cortical afferent (via the
      three-stripe V2 output plus V3)
    - **No direct V1 → BA 19 projection** (the V1 → BA 18 → BA 19
      relay is obligate)
    - **V4 → LOC intra-BA 19** (first step of the reading pathway)
    - **LOC → left VWFA** (the reading endpoint)
    - **V3A / V5/MT+ → left IPS** (the left dorsal-attention
      contribution, weaker than the right's)
    - **V4 / LOC → left inferotemporal** (the ventral stream
      object-recognition hierarchy)
    - **V3A → MT/V5 intra-BA 19** (motion-perception stage)
    - Callosal connections to right BA 19
    - Attentional feedback from left FEF, left DLPFC, left IPS
[ ] CLINICAL_ANCHORS contains the thirteen left-specific anchors:
    - left_ba19_right_hemiachromatopsia
    - left_ba19_pure_alexia_without_agraphia
    - left_ba19_color_agnosia
    - left_ba19_visual_object_agnosia
    - left_ba19_right_hemifield_akinetopsia
    - left_ba19_right_hemifield_motion_deficit_in_daily_life
    - left_ba19_color_and_motion_processing_dissociation
    - left_ba19_occipital_infarct_pca_territory
    - left_ba19_color_form_language_integration_deficit
    - left_ba19_migraine_visual_aura
    - left_ba19_occipital_epilepsy_visual_auras
    - left_ba19_posterior_cortical_atrophy
    - left_ba19_pres_visual_symptoms
[ ] The **right hemiachromatopsia** is documented as the primary
    left BA 19 anchor — the canonical V4 lesion deficit.
[ ] **Pure alexia without agraphia** is documented as the canonical
    left-lateralized reading deficit — the Dejerine syndrome from
    left BA 19 (V4 / LOC) + left splenium involvement.
[ ] **Color agnosia** and **color-form-language integration
    deficit** are documented as **left-lateralized** anchors with
    no symmetric counterpart on the right.
[ ] **Right hemifield akinetopsia** is documented as a **left
    BA 19 anchor** that is **milder than the right BA 19
    equivalent** — the right V5/MT+ is the dominant motion
    hemisphere, and complete akinetopsia requires bilateral
    lesions.
[ ] **Visual object agnosia** is documented as requiring
    **bilateral** lesions; isolated left BA 19 lesions produce a
    **milder, apperceptive** component (not associative).
[ ] **Color-motion dissociation** is documented as the strongest
    clinical evidence that V4 and V5/MT+ are separate areas —
    the left BA 19 is a clean natural experiment because both
    live within its territory.
[ ] **Migraine aura, occipital epilepsy, PCA, PRES, and occipital
    infarct** are documented with the **BA 19-specific
    contributions** (color hallucinations, motion phosphenes,
    complex auras), byte-identically to the left sibling's
    treatment (of these specific entries).
[ ] The **retinotopic multi-mirror-flip** is documented explicitly,
    with the upper-field / lower-field bank assignments and the
    field label flipped.
[ ] The **pulvinar-dominant thalamic input** is documented, and
    it is distinguished from BA 17 (LGN-dominant) and BA 18
    (V1-relay-dominant) — BA 19 is the **associative** visual
    cortex.
[ ] The **koniocellular LGN → V4 pathway** is documented as the
    subcortical substrate of **blindsight for color**.
[ ] The **BA 18 / BA 19 border variability** is documented as a
    caveat, byte-identically to the BA 18 sibling's treatment.
[ ] **Four V-area forward references** (V3A, V3B, V5_MT_plus,
    LOC) are documented, the `FORWARD_REFERENCE_V_AREAS` list is
    referenced (byte-identical to the left sibling's), and the
    resolution rule (remove from both hemispheres in the same
    commit) is recorded.
[ ] **The lingual gyrus forward reference** is documented, and
    its placement question is byte-identical to the left
    sibling's.
[ ] No SUBDIVISIONS promotion is performed while the V4 / V5/MT+
    / LOC split has not been matched by corresponding splits of
    the `..cortex/v4`, `..cortex/v5_mt_plus`, and `..cortex/loc`
    packages.
[ ] **V3A and V3B are not yet resolved** — their assignment to
    BA 19 or BA 18 must be resolved before the BA 19 split, and
    the resolution must be hemisphere-invariant.
[ ] **V4 / V4α subdivision** must be decided in the same commit
    as any V4 split, if the split is performed.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    V_AREA_CORRELATE, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, **FUNCTIONAL_DOMAINS set**, forward-declaration
    caveat text) match the left sibling; the RETINOTOPIC_MAP's
    represented hemifield, DOMAIN_EMPHASIS (ventral vs dorsal
    emphasis), CONNECTIVITY emphasis, and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left BA 19
    carries "right_hemifield" in its DOMAIN_EMPHASIS entries and
    RETINOTOPIC_MAP; the right BA 19 carries "left_hemifield."
[ ] **The ventral-vs-dorsal emphasis is verified**: the left
    BA 19 carries "color_form_language_integration" and
    "object_recognition_left_vwfa_reading_pathway"; the right
    BA 19 carries "motion_perception_dominant" and "dorsal_
    attention_network_dominant."
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — both carry the same five domains.
[ ] **The right-only clinical anchors are verified**:
    `right_ba19_left_hemispatial_neglect_contribution`,
    `right_ba19_right_dorsal_attention_network_target`,
    `right_ba19_prosopagnosia`, and `right_ba19_left_hemifield_
    akinetopsia` are present on the right and absent on the
    left. The left-only `left_ba19_pure_alexia_without_agraphia`,
    `left_ba19_color_agnosia`, and `left_ba19_color_form_
    language_integration_deficit` anchors are absent on the
    right.
[ ] Any downstream code querying "what does the left BA 19 see?"
    must receive "the RIGHT visual hemifield."
[ ] Any downstream code querying "what is BA 19?" must receive
    "the V3A + V3B + V4 + V5/MT+ + LOC complex" — the
    five-component identity is enforced through the
    ALTERNATE_NAMES and V_AREA_CORRELATE.
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** BA 19 (V4 / LOC) → left VWFA
    chain — the left BA 19 is the **third stage**, not the
    reading operation.
[ ] Any downstream code assigning face processing must route
    through the **right** BA 19 (V4 / LOC) → right FFA chain.
[ ] Any downstream code assigning motion perception must weight
    the **right** BA 19 (V5/MT+) more heavily — the right V5/MT+
    is the dominant motion hemisphere.
[ ] Any downstream code assigning color perception must weight
    the **left** BA 19 (V4) more heavily for **color-form-
    language integration**, and the **right** BA 19 (V4) more
    heavily for **pure color perception**.
"""