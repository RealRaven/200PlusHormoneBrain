"""
Brodmann Area 19 (Tertiary Visual Cortex) — Right Hemisphere
=============================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── brodmann_areas
                                    └── brodmann_area_19   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the right
hemisphere's **BA 19** — the **tertiary visual cortex**, the
extrastriate territory that **surrounds BA 18 (V2 + V3)** on the
lateral, dorsal, and ventral surfaces of the occipital lobe. It is the
**most heterogeneous** of the three occipital BAs and the **only one**
whose V-area correlates span **both** the ventral stream (V4, LOC) and
the dorsal stream (V5/MT+, V3A, V3B) — which is why its
`V_AREA_CORRELATE` field is a **six-element tuple**, the largest in the
cortex tree.

Parent: ``..brodmann_areas`` (right occipital BA registry) — sibling to
BA 17 and BA 18.

This package is the **structural mirror** of
``../../left/cortex/occipital/brodmann_areas/brodmann_area_19``. The
BA number, the six V-area correlates, the architectonic signatures, the
BA 18 / BA 19 border variability, and the stream-separation properties
are identical on both sides; the **functional emphasis** and
**clinical significance** diverge — on the right, BA 19 is weighted
toward **motion / spatial / attentional processing** (the dorsal
stream and the right dorsal attention network), **prosopagnosia**,
**left hemifield akinetopsia**, and **left hemispatial neglect**, while
the left BA 19 is weighted toward **color / form / object processing**
(the ventral stream and the left visual word form area), **pure alexia
without agraphia**, and **left-lateralized color and object agnosia**.

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
**On the right, the dorsal-stream components (V3A, V3B, V5/MT+) are the
more strongly engaged ones**, and the right BA 19 is the **dominant
motion and spatial-attention hemisphere** — the mirror of the left's
ventral-stream dominance.

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
available. **This caveat is byte-identical to the left sibling's.**

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
                            **On the right, V5/MT+ is the
                            dominant motion hemisphere** — the
                            right MT/MST is more strongly engaged
                            during coherent motion, motion-in-
                            depth, and optic-flow processing than
                            the left's.

    LOC (part of BA 19)     The **lateral occipital complex**, a
                            large object-recognition territory
                            on the lateral occipital surface.
                            Contains the **lateral occipital
                            (LO)** area for general objects and
                            the **fusiform face area (FFA)** at
                            its ventral edge. **On the right, the
                            LOC → FFA pathway is the face-
                            recognition endpoint**, and the right
                            FFA is the canonical face-processing
                            area.

    V3A / V3B (part of BA 19) The **dorsal extrastriate** areas
                            adjacent to V3. V3A is the
                            motion-in-depth and motion-boundary
                            area; V3B is the kinetic-occipital
                            area. **On the right, V3A is more
                            strongly engaged** for motion-in-
                            depth and visuospatial attention, and
                            the right V3A is a core node of the
                            right-lateralized dorsal attention
                            network.

**A crucial caveat about BA 19's functional specificity.** Unlike BA 17
(striate cortex, 1:1 with V1) or BA 18 (V2 + V3, two clean
functional areas), **BA 19 is a family of at least five distinct
functional areas** (V3A, V3B, V4, V5/MT+, LOC), each with its own
retinotopic map, its own architectonic signature, and its own
functional domain. The BA 19 label is therefore a **cytoarchitectonic
convenience** that groups together territories that modern
neuroscience would **not** treat as a single unit.

**Right-hemisphere specificity**: the right BA 19's V5/MT+, V3A, and
V3B subregions are the **origin of the right dorsal stream** that
feeds the **right intraparietal sulcus** and the **right-lateralized
dorsal attention network**. The right V3A → MT/V5 → right IPS pathway
is the **right motion and spatial-attention pathway**, and right BA 19
lesions can produce **left hemifield akinetopsia** (more severe than
the left BA 19 equivalent) and **left hemispatial neglect** (when the
lesion extends to the right parietal and right frontal territories).
**The right BA 19's LOC also feeds the right FFA**, and **right LOC /
FFA lesions produce prosopagnosia** — the canonical right-lateralized
visual-recognition deficit. The right BA 19's V4 contributes to
**left hemifield color perception** and **pure color processing**
(with a right-hemisphere bias for the felt / phenomenal aspect of
color experience), but the **left-lateralized color-form-language
integration and color agnosia** are left-side anchors, not right.

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
            the ventral stream.** On the right, V4's outputs feed
            the LOC and the right FFA — the **face-recognition
            pathway**. The right V4 is also a contributor to
            **pure color perception** and the **felt aspect of
            color experience**, but the left-lateralized
            color-form-language integration is left-only.
        V5 / MT+ — motion (part of BA 19)
            The motion area at the occipito-temporal junction.
            **The origin of the dorsal stream.** **On the right,
            V5/MT+ is the dominant motion hemisphere** — the
            right MT/MST is more strongly engaged during coherent
            motion, motion-in-depth, and optic-flow processing
            than the left's.
        LOC — object recognition (part of BA 19)
            The lateral occipital complex on the lateral occipital
            surface. **The object-recognition area of the ventral
            stream.** **On the right, LOC's outputs feed the
            right FFA for faces**; the left LOC's outputs feed
            the left VWFA for reading.
        V3A / V3B — motion and kinetic contours (part of BA 19,
        forward references)
            The dorsal extrastriate areas adjacent to V3. **Not
            yet packages under ``..cortex``** — recorded as
            forward references. **On the right, V3A is the more
            strongly engaged side** for motion-in-depth and
            visuospatial attention, and right V3A is a core node
            of the right dorsal attention network.
        lateral occipital gyrus — lateral surface
            The lateral occipital gyri carry the LOC and the
            lateral portion of V5/MT+. The gyral package
            cross-references BA 19 as its primary functional
            overlay. **On the right, the lateral occipital
            gyrus's LOC and V5/MT+ are part of the right
            face-recognition and motion pathways** respectively.
        fusiform gyrus — ventral surface (forward reference in
        ``..gyri`` — not yet a package)
            The fusiform gyrus carries V4 and the ventral portion
            of LOC. **On the right, the fusiform gyrus's V4 → LOC
            output feeds the right FFA** — the face-recognition
            endpoint. The right FFA is the canonical face area.
        lunate sulcus / transverse occipital sulcus — borders
            The lunate sulcus (when present) and the transverse
            occipital sulcus are the lateral / dorsal landmarks
            for the BA 18 / BA 19 border, **both variable**.
        right dorsal attention network — target
            **Right-emphasized overlay.** The right BA 19's V3A
            and V5/MT+ are core nodes of the **right-lateralized
            dorsal attention network** (with the right
            intraparietal sulcus and right frontal eye fields),
            which supports **top-down spatial attention** in the
            LEFT visual hemifield. The left BA 19 is also a
            target of the left dorsal attention network, but the
            right network is the dominant one.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours, the V4 / V5/MT+ / LOC / V3A / V3B overlays,
and the lateral occipital gyrus / fusiform gyrus / lunate sulcus /
transverse occipital sulcus landmarks are the same on both sides. What
differs is the **visual hemifield** — the right BA 19 processes the
LEFT hemifield — and the **stream weighting** — the right BA 19 is
dorsal-dominant (V3A, V5/MT+), the left BA 19 is ventral-dominant
(V4, LOC). The **right dorsal attention network overlay** is a
right-emphasized functional overlay that the left BA 19 package
declares at lower weighting.

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
                                           area (FFA). **On the
                                           right, the FFA is the
                                           canonical face-
                                           processing endpoint.**
    BA 7 / BA 39 (parietal)                **rostrodorsal neighbour**;
                                           continues the dorsal stream
                                           from V5/MT+ / V3A into
                                           the right parietal
                                           attention network. **On
                                           the right, the right IPS
                                           and area 7 are core nodes
                                           of the right dorsal
                                           attention network.**
    BA 21 / BA 22 (temporal)               **rostrolateral neighbour**;
                                           the motion and object
                                           pathways continue into
                                           the lateral temporal
                                           cortex
    lateral occipital gyrus                carries the LOC and the
                                           lateral V5/MT+; **on the
                                           right, LOC feeds the right
                                           FFA and V5/MT+ is the
                                           dominant motion
                                           substrate**
    fusiform gyrus (forward reference in   carries V4 and the ventral
    ..gyri)                                LOC; **on the right, the
                                           V4 → LOC → FFA pathway
                                           is the face-recognition
                                           pathway**
    lunate sulcus                          **lateral-surface landmark**
                                           for the BA 18 / BA 19
                                           border, **when present**
    transverse occipital sulcus            **dorsal-surface landmark**
                                           for the posterior boundary
                                           of the lateral occipital
                                           gyri and the V3A / V3B
                                           territory

**This field is byte-identical to the left sibling's** at the level of
BA-numbered neighbours and sulcal/gyral landmarks. The adjacency
relationships are topological, not lateralized. The field notes in
the BA 37 and BA 7 entries (FFA and IPS) are right-emphasized
annotations consistent with the right's dorsal-stream and face-
processing dominance.

**A note on BA 19's dual-stream neighbours.** BA 19 has **two distinct
downstream targets** — the **temporal lobe** (ventral stream: BA 37,
BA 21) and the **parietal lobe** (dorsal stream: BA 7, BA 39). This is
unlike BA 17 and BA 18, whose downstream targets are predominantly the
occipital hierarchy itself. **The dual-stream adjacency is a defining
structural feature of BA 19** and must be preserved in the
cross-references.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 19 participates in **five** canonical occipital functional domains,
the largest domain set of any occipital BA. The set is **identical on
both hemispheres** (unlike BA 17's four-vs-three divergence); the
**emphasis** differs. On the right, the emphasis is as follows:

    motion_perception                              (right emphasis — PRIMARY)
        **This is BA 19's dominant contribution on the right** —
        the perception of motion, localized to V5/MT+ at the
        occipito-temporal junction. **The right V5/MT+ is the
        dominant motion hemisphere** — the right MT/MST is more
        strongly engaged during coherent motion, motion-in-depth,
        and optic-flow processing than the left's. Right V5/MT+
        lesions produce **left hemifield akinetopsia** (more
        severe than the left-side equivalent), and complete
        akinetopsia requires **bilateral** V5/MT+ lesions.

    spatial_localization                           (right emphasis — PRIMARY)
        **This is BA 19's second major contribution** — the early
        spatial-localization processing carried by V3A and
        V5/MT+'s motion-in-depth representation. **On the right,
        the spatial-localization contribution is dominant** —
        the right V3A and right V5/MT+ are core nodes of the
        right-lateralized dorsal attention network, and they
        support **spatial attention in the LEFT visual
        hemifield**. Right BA 19 lesions contribute to **left
        hemispatial neglect** when the lesion extends to the
        right parietal and right frontal territories.

    visual_attention                               (right emphasis — SECONDARY)
        **This is BA 19's third contribution** — the dorsal-
        stream attentional target role carried by V3A and
        V5/MT+ in the right-lateralized dorsal attention
        network. **On the right, the attentional contribution
        is dominant** — the right V3A and right V5/MT+ receive
        strong top-down attentional gain from the right IPS and
        right FEF, and they are **targets** (not generators) of
        the right dorsal attention network. The right BA 19 is
        part of the substrate that, when damaged together with
        the right parietal and frontal territories, produces
        **left hemispatial neglect**.

    color_vision                                   (right emphasis — SECONDARY)
        **This is BA 19's fourth contribution** — the conscious
        perception of color, localized to V4 on the fusiform
        gyrus and adjacent lateral occipital cortex. **On the
        right, the color contribution is present but weighted
        toward pure color perception** — the right V4 is a
        contributor to the **felt / phenomenal aspect of color
        experience** and to **left hemifield color perception**.
        Right V4 lesions produce **left hemiachromatopsia** (loss
        of color vision in the left hemifield), and bilateral V4
        lesions produce complete achromatopsia. **The left-
        lateralized color-form-language integration and color
        agnosia are left-only** — the right BA 19 does not
        carry them at the same weighting.

    form_and_object_perception                     (right emphasis — SECONDARY)
        **This is BA 19's fifth contribution** — the object-
        recognition processing carried by V4 and the LOC in the
        ventral stream. **On the right, the form-and-object
        contribution is weighted toward the LOC → right FFA
        pathway** — the **face-recognition endpoint**. Right
        BA 19 / LOC / FFA lesions produce **prosopagnosia**
        (impaired face recognition) — the canonical right-
        lateralized visual-recognition deficit. The right BA
        19 also contributes to **visual object agnosia**
        (bilateral lesions are typically needed), and to
        **associative object agnosia** more than the apperceptive
        component.

**Right-specific caveat on `primary_visual_processing` (BA 17's
domain).** The label is shared with BA 17, but BA 19 does **not**
carry it. `primary_visual_processing` is **omitted** from the BA 19
`FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `primary_visual_processing` (secondary)
and `binocular_vision` (BA 18's domains).** These are BA 18's
domains, not BA 19's. They are **omitted** from the BA 19
`FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `visual_word_processing`.** This is a
**left-lateralized** function that the right BA 19 does **not**
carry. `visual_word_processing` is instantiated in the left VWFA
(fed by the left BA 19 → LOC → VWFA pathway). It is **omitted** from
the right BA 19 `FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the
**right BA 19 supports as an input stage** but does **not** carry
as primary functional domains. `face_processing` is instantiated in
the right FFA (fed by the right BA 19 → LOC → FFA pathway);
`global_visual_processing` is a distributed right-hemisphere
property beginning at right BA 18 and continuing through the right
BA 19. **No single occipital BA claims `face_processing` or
`global_visual_processing` as a primary contribution** — they are
network properties of the right occipital + right fusiform / right
hemisphere pathways. The right BA 19 package **contributes to**
these pathways via its `form_and_object_perception` domain, but does
not carry the downstream domains themselves.

**Summary**: BA 19 carries **exactly five** functional domains —
`motion_perception`, `spatial_localization`, `visual_attention`,
`color_vision`, and `form_and_object_perception`. **The
FUNCTIONAL_DOMAINS set is identical across hemispheres** — both sides
carry the same five domains. **The emphasis differs**: the right
emphasizes motion, spatial localization, and attention (the dorsal
stream and the right dorsal attention network); the left emphasizes
color and form/object processing (the ventral stream and the left
VWFA). **This is a weighting-only divergence, not a domain-set
divergence** — consistent with BA 18's treatment, and unlike BA 17's
four-vs-three divergence.

**A note on the emphasis ordering.** On the right, the domains are
listed in the order of **right-sided emphasis**: motion and spatial
localization first (the right's dominant contributions), then
attention, then color and form/object. On the left, the order is
**color** and **form/object** first (the left's dominant
contributions), then motion, spatial localization, and attention.
**The DOMAIN_EMPHASIS dict's ordering reflects the hemisphere's
dominant contributions** — the domain *set* is the same, but the
*priority* differs.

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
            visual attention and visual short-term memory.
            **On the right, the pulvinar → V5/MT+ and pulvinar →
            V3A projections are the dominant ones**, and they
            are part of the right dorsal attention network
            substrate.
        → LGN (weak, koniocellular)
            The **koniocellular pathway** (via the LGN's
            koniocellular layers) provides a weak direct projection
            to V4, bypassing V1. This pathway carries the
            **blue-yellow (S-cone) color signal** and is part of
            the subcortical substrate for color vision that
            **survives V1 lesions** — the phenomenon of **blindsight
            for color**.

    cortical afferents
        → V2 / V3 (BA 18), right
            **BA 19's principal cortical afferent.** The V2 thin
            stripes project to V4 (color / form); the V2 thick
            stripes and V3 project to MT/V5 (motion); the V3 / V3A
            transition projects to V3A (motion-in-depth); and the
            V2 pale stripes project to the LOC (object form).
            **On the right, the V2 / V3 → MT/V5 and V2 / V3 →
            V3A pathways are the dominant ones**, consistent with
            the right's dorsal-stream weighting.
        → V1 (indirect, via BA 18)
            BA 19 has **no direct V1 projections** — the V1 →
            BA 18 → BA 19 relay is obligate.

    cortical efferents
        → LOC (intra-BA 19), right
            V4's outputs project to the LOC within BA 19,
            contributing to the **object-recognition stage** of
            the ventral stream. **On the right, the V4 → LOC
            pathway feeds the right FFA** — the face-recognition
            endpoint.
        → right fusiform face area (FFA), right
            The **LOC → FFA projection** carries the object-form
            signal forward to the face-recognition endpoint.
            **This is the right BA 19's most important efferent
            for ventral-stream processing**, and it is the mirror
            of the left's LOC → left VWFA projection.
        → parietal cortex (V3A, V5/MT+ → IPS, area 7), right
            **Right-emphasized.** V3A and V5/MT+ project forward
            to the **right intraparietal sulcus** and the **right
            dorsal attention network**. **On the right, this
            projection is the substrate for LEFT-hemifield
            spatial attention**, and it is the dominant
            attentional contribution — the right's V3A / V5/MT+
            → right IPS pathway is the **core of the
            right-lateralized dorsal attention network**.
        → temporal cortex (V4, LOC → inferotemporal), right
            V4 and LOC project forward to the **right inferior
            temporal cortex** (BA 37, BA 21), continuing the
            ventral stream's object-recognition hierarchy. **On
            the right, this pathway terminates at the right
            FFA** (faces) and the **right anterior temporal
            semantic hub**.
        → MT/V5 (intra-BA 19), right
            V3A's outputs project to MT/V5 within BA 19,
            contributing to the **motion-perception stage** of
            the dorsal stream. **On the right, the V3A → MT/V5
            pathway is the dominant motion pathway** — the right
            MT/MST is the dominant motion hemisphere.

    callosal connections
        → left BA 19
            The callosal fibers connect the right BA 19 to the
            left BA 19 across the occipital midline, supporting
            **the fusion of the two hemifields** at the V4 and
            MT/V5 stage. The callosal traffic carries the **left-
            hemifield color-form signal** (right BA 19) and the
            **right-hemifield motion signal** (left BA 19).

    attentional feedback
        → frontal eye fields (BA 8), right
            **Right-emphasized.** The right FEF is the dominant
            node of the right ventral attention network and sends
            strong **top-down and bottom-up attentional gain** to
            the right BA 19, modulating V4 and MT/V5 responses to
            behaviourally relevant stimuli.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), right
            The DLPFC sends top-down attentional and working-memory
            signals to the right BA 19, supporting **visual
            working memory** and **visual imagery**.
        → intraparietal sulcus, right
            **Right-emphasized.** The right IPS is a core node of
            the right dorsal attention network and sends strong
            top-down spatial-attention signals to the right BA 19,
            supporting **spatial attention** in the LEFT visual
            hemifield. The right IPS → right BA 19 projection is
            part of the substrate for **sustained spatial
            attention**.
        → temporoparietal junction, right
            **Right-emphasized.** The right TPJ is the other core
            node of the right ventral attention network and sends
            reorienting signals to the right BA 19 via the right
            FEF.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in four respects:
(a) the **pulvinar → V5/MT+ and pulvinar → V3A** projections are the
dominant ones on the right, consistent with the right's dorsal-stream
weighting;
(b) the **LOC → right FFA** pathway is the face-recognition endpoint
(not the left VWFA);
(c) the **V3A / V5/MT+ → right IPS** pathway is the dominant dorsal
attention network contribution — the left's is present but weaker;
(d) the callosal traffic carries the **left-hemifield color-form**
signal (from the right) and the **right-hemifield motion** signal
(from the left).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ba19_left_hemiachromatopsia
        **This is the right BA 19 anchor for V4.** A lesion of the
        right V4 (part of BA 19 on the fusiform gyrus) produces
        **left hemiachromatopsia** — loss of color vision in the
        LEFT half of the visual field of both eyes, with preserved
        color vision in the right hemifield. **The right V4
        lesion spares the right hemifield's color perception**
        because the left V4 (fed by the left occipital lobe) is
        intact. **Bilateral V4 lesions produce complete
        achromatopsia** — the patient sees the world in shades of
        gray. **This is the mirror of the left BA 19's right
        hemiachromatopsia anchor.**

    right_ba19_left_hemifield_akinetopsia_more_severe
        **This is the right BA 19 anchor par excellence.** A
        lesion of the right V5/MT+ produces **left hemifield
        akinetopsia** — impaired motion perception in the LEFT
        visual field. **The deficit is MORE SEVERE than the left
        V5/MT+ lesion's right hemifield deficit** — the right
        V5/MT+ is the **dominant motion hemisphere**, and the
        left V5/MT+ contributes but is not the primary
        substrate. **Complete akinetopsia** (the famous "motion
        blindness" of patient LM) requires **bilateral V5/MT+
        lesions**, but the right lesion alone produces a
        **clinically prominent** left hemifield deficit that is
        more disruptive than the left's right hemifield
        equivalent. **This is the dominant motion anchor for
        the right BA 19.**

    right_ba19_contribution_to_prosopagnosia
        **Right-emphasized.** The right BA 19's LOC is the
        **second stage** of the right ventral stream that feeds
        the right FFA, and **right occipito-temporal lesions**
        that involve the right FFA or its input pathway produce
        **prosopagnosia** — impaired face recognition. **Isolated
        right BA 19 lesions do not produce prosopagnosia** — the
        right FFA is spared — but the right BA 19 is the
        **occipital input stage** of the right-lateralized face
        pathway, and its lesions can contribute to face-
        processing deficits when the downstream FFA is also
        affected. **Prosopagnosia is the canonical
        right-lateralized visual-recognition deficit**, and
        right BA 19 is its occipital input stage. **This
        anchor has no symmetric counterpart on the left** — the
        left BA 19 feeds the left VWFA (reading), not a
        prosopagnosia pathway.

    right_ba19_left_hemispatial_neglect_contribution
        **Right-emphasized.** Right BA 19 lesions contribute to
        **left hemispatial neglect** when the lesion extends
        beyond BA 19 into the right parietal and right frontal
        territories. **Isolated right BA 19 lesions do not
        produce neglect** — the patient has a left hemifield
        akinetopsia but can attend to the left field cognitively
        — but the right BA 19 is part of the **right dorsal
        attention network** substrate (via V3A and V5/MT+) that,
        when damaged together with the right IPS and right FEF,
        contributes to the neglect syndrome. **The right BA 19
        is therefore the right-lateralized attentional substrate
        that the left BA 19 is not**, and its damage is more
        consequential for hemispatial attention than isolated
        left BA 19 damage. **This anchor has no symmetric
        counterpart on the left.**

    right_ba19_right_dorsal_attention_network_target
        **Right-emphasized.** The right BA 19's V3A and V5/MT+
        are core nodes of the **right-lateralized dorsal
        attention network** (right IPS + right FEF). Right BA 19
        is a **target** of the right IPS and right FEF
        attentional gain, and the right V3A / V5/MT+ → right IPS
        pathway is the dominant dorsal-stream contribution to
        **left-hemifield spatial attention**. **Isolated right
        BA 19 lesions do not produce the full neglect syndrome**
        — the right IPS and right FEF must also be damaged —
        but the right BA 19's participation is a necessary
        substrate.

    right_ba19_left_hemifield_motion_deficit_in_daily_life
        **Right V5/MT+ lesions can produce prominent functional
        motion deficits** — difficulty judging the speed of
        approaching objects, difficulty following moving targets,
        difficulty in motion-heavy environments (traffic,
        crowds), and difficulty in sports or driving — **in the
        LEFT visual field**. The deficit is typically **more
        severe** than the left-side equivalent because the right
        V5/MT+ is the dominant motion hemisphere, and the patient
        often cannot fully compensate with the intact right
        hemifield. **This is a right-emphasized anchor.**

    right_ba19_visual_object_agnosia_associative
        **Visual object agnosia** — impaired ability to recognize
        objects despite intact visual perception — typically
        requires **bilateral** lesions of the ventral stream
        (V4, LOC, and inferotemporal cortex). **Right BA 19
        lesions contribute to the associative component** of
        visual object agnosia (the failure to link a percept to
        semantic knowledge) more than the apperceptive component
        (the failure to form a coherent object percept). **The
        bilateral requirement** means that isolated right BA 19
        lesions produce a **milder** object-recognition deficit
        than isolated right BA 18 or BA 17 lesions.

    right_ba19_color_and_motion_processing_dissociation
        **The right BA 19's five functional areas are
        architectonically interleaved but functionally
        dissociable.** A focal right V4 lesion produces
        hemiachromatopsia **without** akinetopsia; a focal right
        V5/MT+ lesion produces akinetopsia **without**
        hemiachromatopsia. **The dissociations are the strongest
        clinical evidence that color and motion are processed
        by separate cortical areas**, and the right BA 19 is a
        clean natural experiment for this dissociation because
        both V4 and V5/MT+ live within its territory. **On the
        right, the dissociation is more clinically prominent
        for motion than for color** — because the right is the
        dominant motion hemisphere, right V5/MT+ lesions are
        more easily detected and produce more severe deficits
        than right V4 lesions.

    right_ba19_right_motion_hemisphere_emphasis
        **Right-emphasized.** The right BA 19's V5/MT+ and V3A
        are the **dominant motion and motion-in-depth
        processing areas in the human brain**. Right V5/MT+
        lesions produce more severe deficits than left V5/MT+
        lesions; right V3A lesions produce more severe
        motion-in-depth and optokinetic deficits than left V3A
        lesions. **The right hemisphere's motion dominance is a
        consistent finding across fMRI, TMS, and lesion
        studies**, and it is one of the clearest examples of
        visual lateralization.

    right_ba19_global_visual_processing_contribution
        **Right-emphasized.** The right BA 19's LOC and V5/MT+
        contribute to the **global / holistic** aspect of
        visual processing (Navon's global-precedence
        asymmetry), which is a right-hemisphere advantage
        beginning at right BA 18 and continuing through right
        BA 19. **Right BA 19 lesions can produce global-level
        form and motion processing deficits** — the patient may
        still perceive local features and motion segments but
        cannot integrate them into a coherent global percept.
        **This anchor has no symmetric counterpart on the
        left** — the left BA 19 is weighted toward local /
        featural processing.

    right_ba19_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct**
        involving BA 19 produces a **left homonymous hemianopia
        or quadrantic defect** (from BA 17 / BA 18 involvement)
        **plus** a **left hemiachromatopsia** (from right V4
        involvement) **plus** a **left hemifield motion-
        perception deficit** (from right V5/MT+ involvement,
        often the most disabling of the three). **Isolated right
        PCA infarcts do not produce alexia without agraphia** —
        that syndrome is left-lateralized — because the right
        splenium does not connect to a right reading network.
        **The right PCA infarct's clinical signature is
        therefore the left hemianopia plus left hemiachromatopsia
        plus left hemifield motion deficit**, and the motion
        deficit is often the most functionally disabling.

    right_ba19_migraine_visual_aura
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
        is contralateral (left field on the right side).

    right_ba19_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from **BA 17, BA 18, OR BA 19**. **BA 19 auras**
        are typically **more complex than BA 18 auras** — the
        patient may see **formed objects, colored scenes, or
        motion hallucinations** in addition to elementary shapes
        and fortifications. **Right BA 19 auras** project to the
        **left visual field** and can be preceded or accompanied
        by **visual field defects, hemiachromatopsia, or
        akinetopsia** that persist after the seizure.

    right_ba19_posterior_cortical_atrophy_benson_syndrome
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **BA 19 extensively**, including
        V4, V5/MT+, and the LOC. **Right BA 19** is part of the
        substrate of the **progressive dorsal-stream dysfunction**
        that produces **Benson syndrome** — the right-lateralized
        clinical presentation with **progressive prosopagnosia,
        visuospatial deficits, optic ataxia, and simultanagnosia**.
        **On the right, PCA presents with the visuospatial /
        prosopagnosic syndrome (Benson syndrome)**; on the left,
        with the progressive reading deficits and color agnosia.

    right_ba19_pres_visual_symptoms
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

These anchors are **right-hemisphere-specific** in two senses:
(a) the right BA 19 processes the **LEFT visual hemifield**, so
right BA 19 lesions produce **left-sided** visual deficits; (b) the
right BA 19 is the **dominant motion and spatial-attention
hemisphere**, and right BA 19 lesions can produce **left hemifield
akinetopsia** and **left hemispatial neglect** that have no symmetric
counterpart on the left. **The LOC → right FFA pathway** is a third
right-specific feature — the right BA 19 is face-pathway-dominant,
while the left BA 19 is reading-pathway-dominant. The left sibling's
docstring carries the corresponding left-sided anchors (right
hemiachromatopsia, pure alexia without agraphia, color agnosia,
color-form-language integration deficit, milder right hemifield
akinetopsia).

**The `migraine_aura`, `occipital_epilepsy`, `PCA` (the syndrome,
though the subtype emphasis differs), `PRES`, and `occipital_infarct`
anchors are hemisphere-invariant** — they appear on both sides and
are documented identically in both siblings, with the side-appropriate
field label. The **subtype emphasis of PCA** differs (right → Benson
syndrome; left → progressive reading deficits), but the syndrome as a
whole is bilateral.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The right occipital BA registry. This package's parent, source
    of the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 19 (which on
    the right is ``("motion_perception_dominant",
    "spatial_localization_v3a_dominant",
    "visual_attention_dorsal_attention_network_dominant",
    "color_vision_right_hemiachromatopsia",
    "form_and_object_perception_right_ffa_face_pathway")``), and
    enforcer of the **six-element V_AREA_CORRELATE**.

..brodmann_area_17_primary_visual
    **Distant caudal neighbour**; no direct adjacency (BA 18
    intervenes). BA 17's V1 outputs reach BA 19 via the **BA 18
    relay**, not directly.

..brodmann_area_18
    **Caudomedial neighbour** via the **variable** BA 18 / BA 19
    border. V2's and V3's outputs are the principal cortical
    inputs to all five BA 19 functional areas. **On the right,
    the V2 / V3 → MT/V5 and V2 / V3 → V3A pathways are the
    dominant ones.**

...cortex.v4
    The **functional V4 package under ``..cortex``** — the direct
    counterpart of the V4 component of BA 19. **On the right,
    V4's outputs feed the LOC and the right FFA** — the face-
    recognition pathway. **On the right, V4 is weighted toward
    pure color perception and left hemifield color perception**
    (the color-form-language integration is left-only).

...cortex.v5_mt_plus  (forward reference)
    The **functional V5/MT+ package** — not yet a package under
    ``..cortex``. **On the right, V5/MT+ is the dominant motion
    hemisphere** — the right MT/MST is more strongly engaged than
    the left's. V5/MT+ is the substrate of akinetopsia, and the
    right V5/MT+ lesion produces the more severe left hemifield
    akinetopsia.

...cortex.loc  (forward reference)
    The **functional LOC package** — not yet a package under
    ``..cortex``. **On the right, LOC's outputs feed the right
    FFA** — the face-recognition endpoint.

...cortex.v3  (shared with BA 18)
    The **functional V3 package under ``..cortex``** — shared
    between BA 18 and BA 19. **V3's lateral portion extends
    into BA 19 territory.**

...cortex.v3a / ...cortex.v3b  (forward references)
    The **functional V3A and V3B packages** — not yet packages
    under ``..cortex``. **On the right, V3A is the more strongly
    engaged side** for motion-in-depth and visuospatial attention,
    and right V3A is a core node of the right dorsal attention
    network.

...gyri.lateral_occipital_gyrus
    The lateral-surface gyral territory. BA 19's LOC and lateral
    V5/MT+ overlay the lateral occipital gyrus. **On the right,
    the lateral occipital gyrus's LOC is part of the right face
    pathway** (LOC → FFA), and its lateral V5/MT+ is part of the
    dominant motion substrate.

...gyri  (forward reference — the fusiform gyrus is not yet a
    package)
    The fusiform gyrus carries V4 and the ventral LOC. **On the
    right, the fusiform gyrus's V4 → LOC output feeds the right
    FFA** — the face-recognition endpoint.

...sulci.lunate_sulcus
    The **lateral-surface landmark** for the BA 18 / BA 19
    border, **when present**.

...sulci.transverse_occipital_sulcus
    The **dorsal-surface landmark** for the posterior boundary
    of the lateral occipital gyri and the V3A / V3B territory.

..cortex.temporal
    The **ventral stream** continues from BA 19 (V4, LOC) into
    the temporal lobe (inferior temporal cortex, fusiform
    gyrus). **On the right, the ventral stream terminates in
    the right FFA** (the face area), and the right BA 19 is the
    **third stage** of this pathway. **Right occipito-temporal
    lesions produce prosopagnosia** — the canonical
    right-lateralized visual-recognition deficit. The temporal
    package must declare the right BA 19 as a source of its
    visual input via the ventral stream, and must note the
    **right-lateralized FFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from BA 19 (V3A, V5/MT+)
    into the parietal lobe (IPS, area 7). **On the right, the
    dorsal stream is more strongly engaged during visuospatial
    attention** — the right V3A and right V5/MT+ are core nodes
    of the right-lateralized dorsal attention network. The
    parietal package must declare the right BA 19 as a source of
    its visual input for the dorsal stream, and must note the
    right-lateralized attentional emphasis.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to BA 19. **On the right, the right FEF is the
    dominant node of the ventral attention network**, and right
    frontal lesions contribute to left hemispatial neglect.

..cortex.cingulate  — indirect
    No direct cingulate → BA 19 projection.

..cortex.insular  — indirect
    No direct insular → BA 19 projection.

../../subcortical/diencephalon/thalamus/pulvinar
    **The pulvinar is BA 19's dominant thalamic input.** **On
    the right, the pulvinar → V5/MT+ and pulvinar → V3A
    projections are the dominant ones**, and they are part of
    the right dorsal attention network substrate. The thalamus
    package must declare the pulvinar as the dominant thalamic
    relay to right BA 19.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN's koniocellular pathway** provides a **weak direct
    projection to V4**, bypassing V1. This pathway carries the
    **blue-yellow (S-cone) color signal** and is part of the
    subcortical substrate that **survives V1 lesions** —
    blindsight for color.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from BA 19 (V4, LOC) to the
    perirhinal, entorhinal, and parahippocampal cortices. **On
    the right, the parahippocampal place area (PPA) and the
    retrosplenial complex receive visual input supporting scene
    and spatial memory**, which are more strongly right-
    lateralized. **The right BA 19 is the third stage** of this
    pathway.

../../left/cortex/occipital/brodmann_areas/brodmann_area_19
    The left-hemisphere homologue. Structural fields (BA
    number, six-element V-area correlates, architectonic
    signatures, BA 18 / BA 19 border variability, dual-stream
    identity, lateral occipital gyrus / fusiform gyrus
    relationships, **FUNCTIONAL_DOMAINS set**, forward-
    declaration caveat text) MUST be byte-identical. Functional
    emphasis and clinical significance diverge — the right
    BA 19 processes the **LEFT** visual hemifield, is weighted
    toward **motion perception (V5/MT+), spatial localization
    (V3A), and visual attention (dorsal attention network)**,
    and its V4 / LOC outputs feed the right ventral stream
    toward the right FFA (for faces) rather than the left VWFA
    (for reading).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_19"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    BRODMANN_NUMBER     = 19
    ALTERNATE_NAMES     = ("tertiary_visual_cortex",
                           "extrastriate_association_cortex",
                           "V3A_V3B_V4_V5MT_LOC_complex")
        # **Byte-identical to the left sibling's.**

    ARCHITECTONIC_SIGNATURES = (
        "color_globs_in_V4",
        "agranular_V5_MT_plus",
        "variable_BA18_BA19_border",
        "dual_stream_identity",
    )
        # **Byte-identical to the left sibling's.** The dual-
        # stream identity is a property of BA 19 itself, not of
        # the hemisphere.

    V_AREA_CORRELATE    = ("v3", "v4", "V3A", "V3B", "V5_MT_plus",
                           "LOC")
        # **Six elements** — byte-identical to the left
        # sibling's. **Two current packages** (v3, v4) plus
        # **four forward references** (V3A, V3B, V5_MT_plus,
        # LOC).

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** Byte-identical to the left
        # sibling's.

    RETINOTOPIC_MAP     = "multiple_mirror_flips_V3A_V4_V5MT_LOC"
        # The map's *structure* is identical to the left's —
        # V3A, V4, V5/MT+, LOC each with their own retinotopic
        # map. **On the right, the represented hemifield is the
        # LEFT hemifield.**

    FUNCTIONAL_DOMAINS  = (
                              "motion_perception",
                              "spatial_localization",
                              "visual_attention",
                              "color_vision",
                              "form_and_object_perception",
                              # **Identical set to the left
                              # sibling's** — the five domains are
                              # the same on both hemispheres.
                              # The **ordering** differs: on the
                              # right, motion and spatial
                              # localization are listed first
                              # (the right's dominant
                              # contributions); on the left, color
                              # and form/object are listed first.
                              # NOTE: primary_visual_processing is
                              # EXCLUDED (BA 17's domain).
                              # NOTE: primary_visual_processing_
                              # secondary and binocular_vision are
                              # EXCLUDED (BA 18's domains).
                              # NOTE: visual_word_processing is
                              # EXCLUDED (left-lateralized; the
                              # right BA 19 does not feed the
                              # left VWFA).
                              # NOTE: face_processing is EXCLUDED
                              # as a *BA 19 domain* — it lives in
                              # the right FFA downstream.
                              # NOTE: global_visual_processing is
                              # EXCLUDED as a *BA 19 domain* —
                              # it is a right-hemisphere
                              # emphasis within `form_and_object_
                              # perception`, not a separate
                              # domain.
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "motion_perception":
                                  "motion_perception_dominant_"
                                  "left_hemifield_akinetopsia_more_"
                                  "severe_than_left",
                              "spatial_localization":
                                  "v3a_v5_spatial_localization_"
                                  "dominant_left_hemifield_dorsal_"
                                  "attention_network",
                              "visual_attention":
                                  "attentional_target_dorsal_"
                                  "attention_network_dominant",
                              "color_vision":
                                  "pure_color_perception_left_"
                                  "hemiachromatopsia_felt_aspect",
                              "form_and_object_perception":
                                  "object_recognition_right_ffa_"
                                  "face_pathway_ventral_stream_"
                                  "left_hemifield",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_ba19_left_hemiachromatopsia",
                              "right_ba19_left_hemifield_"
                              "akinetopsia_more_severe",
                              "right_ba19_contribution_to_"
                              "prosopagnosia",
                              "right_ba19_left_hemispatial_"
                              "neglect_contribution",
                              "right_ba19_right_dorsal_"
                              "attention_network_target",
                              "right_ba19_left_hemifield_motion_"
                              "deficit_in_daily_life",
                              "right_ba19_visual_object_agnosia_"
                              "associative",
                              "right_ba19_color_and_motion_"
                              "processing_dissociation",
                              "right_ba19_right_motion_"
                              "hemisphere_emphasis",
                              "right_ba19_global_visual_"
                              "processing_contribution",
                              "right_ba19_occipital_infarct_"
                              "pca_territory",
                              "right_ba19_migraine_visual_aura",
                              "right_ba19_occipital_epilepsy_"
                              "visual_auras",
                              "right_ba19_posterior_cortical_"
                              "atrophy_benson_syndrome",
                              "right_ba19_pres_visual_symptoms",
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
                   **on the right, feeds the right FFA**

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
use the **retinotopic** landmark when available.

**A third caveat**: the **lingual gyrus** is a forward reference in
``..gyri`` — not yet a package. As with BA 17 and BA 18, its
placement question is open and must be resolved in the same commit as
its creation.

**All caveats are byte-identical to the left sibling's** — they are
properties of the occipital lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 19 is **the most architectonically heterogeneous** of the three
occipital BAs, and the **natural split** is into its **five
functional components**:

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
  4. Mirror the promotion on the left side in the same commit.

**This promotion is strongly recommended** — BA 19 is not a coherent
territory in modern neuroscience, and the six-element
`V_AREA_CORRELATE` field records the **incoherence**.

**The V4 / V5/MT+ / LOC split must be mirrored by corresponding splits
of the `..cortex/v4`, `..cortex/v5_mt_plus`, and `..cortex/loc`
packages** — the BA 19 → V4 / V5/MT+ / LOC correspondence means that
any BA 19 split must be matched by a V-area split in ``..cortex``, in
the same commit, in both hemispheres.

**On the right, the V5/MT+ and V3A components are the dominant
dorsal-stream contributors.** If BA 19 is split, the right V5/MT+
component must carry the right-emphasized motion, akinetopsia, and
dorsal-attention contributions, and the right V3A component must carry
the right-emphasized motion-in-depth, spatial-localization, and
dorsal-attention contributions. **The right V4 and LOC components
must carry the complementary face-pathway emphasis** (LOC → FFA), and
the right V4 must carry pure color perception and left
hemiachromatopsia.

**The V3A / V3B split is blocked** until V3A and V3B are themselves
resolved as packages. The resolution (V3A / V3B as BA 19 sub-areas, or
as BA 18 sub-areas) must be made **before** the BA 19 five-way split,
and the resolution must be hemisphere-invariant.

**A particular caution about V4**: V4 is often **split into V4 and
V4α** in modern parcellations. **Any BA 19 split must decide whether
V4 is one component or two**, and the decision must be made in the
same commit as the V4 package's own subdivision (if any).

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../brodmann_area_19``:

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
                                     elements
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same multi-mirror-flip
                                     structure
        FUNCTIONAL_DOMAINS set       the same five domains
                                     (motion_perception,
                                     spatial_localization,
                                     visual_attention,
                                     color_vision,
                                     form_and_object_perception)
        Bounding / overlapping territories
        BA-to-neighbour adjacency
        CONNECTIVITY                 same bundle names (pulvinar
                                     dominant; the V2 → BA 19
                                     pathway is the same)
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — right BA 19 processes
                               the LEFT hemifield; left BA 19
                               processes the RIGHT hemifield.
        FUNCTIONAL_DOMAINS     **identical set** across
                               hemispheres. **The ordering
                               differs** — the right lists
                               motion_perception first (the
                               right's dominant contribution);
                               the left lists color_vision first.
                               The **set** is the same, the
                               **priority** differs.
        DOMAIN_EMPHASIS        right: motion_perception is "motion_
                               perception_dominant_left_hemifield_
                               akinetopsia_more_severe_than_left";
                               spatial_localization is "v3a_v5_
                               spatial_localization_dominant_left_
                               hemifield_dorsal_attention_network";
                               visual_attention is "attentional_
                               target_dorsal_attention_network_
                               dominant"; color_vision is "pure_
                               color_perception_left_hemiachromatopsia_
                               felt_aspect"; form_and_object_
                               perception is "object_recognition_
                               right_ffa_face_pathway_ventral_
                               stream_left_hemifield".
                               left: color_vision is "color_form_
                               language_integration_left_vwfa_
                               pathway_right_hemiachromatopsia";
                               motion_perception is "motion_
                               perception_weaker_than_right_left_
                               hemifield_motion_boundary"; form_
                               and_object_perception is "object_
                               recognition_left_vwfa_reading_
                               pathway_ventral_stream_right_
                               hemifield"; spatial_localization
                               is "v3a_v5_spatial_localization_
                               weaker_than_right_left_hemifield";
                               visual_attention is "attentional_
                               target_lower_weighting_than_
                               right".
        CONNECTIVITY           same bundle names; right: the
                               pulvinar → V5/MT+ and pulvinar →
                               V3A loops are the dominant ones;
                               the LOC → right FFA pathway is
                               the face endpoint; the
                               V3A / V5/MT+ → right IPS pathway
                               is the dominant dorsal-stream
                               contribution.
                               left: the pulvinar → V4 loop
                               feeds the left color-form-
                               language integration; the
                               LOC → left VWFA pathway is the
                               reading endpoint; the
                               V3A / V5/MT+ → left IPS pathway
                               is present but weaker than the
                               right's.
        CLINICAL_ANCHORS       right: fifteen anchors (left
                               hemiachromatopsia, **left hemifield
                               akinetopsia (more severe)**,
                               **contribution to prosopagnosia**,
                               **left hemispatial neglect
                               contribution**, **right dorsal
                               attention network target**,
                               left hemifield motion deficit in
                               daily life, visual object agnosia
                               (associative component),
                               color/motion dissociation,
                               **right motion hemisphere
                               emphasis**, **global visual
                               processing contribution**,
                               right PCA infarct, migraine aura,
                               occipital epilepsy, PCA (Benson
                               syndrome), PRES).
                               left: thirteen anchors (right
                               hemiachromatopsia, pure alexia
                               without agraphia, color agnosia,
                               visual object agnosia
                               (apperceptive component), right
                               hemifield akinetopsia (milder),
                               right hemifield motion deficit in
                               daily life, color/motion
                               dissociation, left PCA infarct,
                               color-form-language integration
                               deficit, migraine aura, occipital
                               epilepsy, PCA, PRES).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same BA 19, the same six
V-area correlates, the same dual-stream identity, and the same
multi-mirror-flip retinotopy — but the *represented hemifield* is
**flipped**.

**The dorsal-vs-ventral stream emphasis is the second sharpest entry.**
Both hemispheres carry the same five functional domains — the set is
**identical** — but the **right** BA 19's emphasis is on **motion /
spatial / attentional processing** (the dorsal stream and the right
dorsal attention network), and the **left** BA 19's emphasis is on
**color / form / object processing** (the ventral stream and the left
VWFA). **Neither emphasis is a separate domain** — the domain set is
identical — but the emphasis determines which **clinical deficit
pattern** a lesion produces.

**The right-specific clinical anchors are the third sharpest entry.**
The right BA 19 carries **five anchors** that the left does not carry
at the same weighting: `right_ba19_left_hemispatial_neglect_
contribution`, `right_ba19_right_dorsal_attention_network_target`,
`right_ba19_contribution_to_prosopagnosia`,
`right_ba19_left_hemifield_akinetopsia_more_severe`, and
`right_ba19_right_motion_hemisphere_emphasis`. Plus the right-only
`right_ba19_global_visual_processing_contribution` and
`right_ba19_visual_object_agnosia_associative`. The left BA 19's
`left_ba19_pure_alexia_without_agraphia`,
`left_ba19_color_agnosia`, and `left_ba19_color_form_language_
integration_deficit` anchors are **left-only**.

**The V_AREA_CORRELATE, the four ARCHITECTONIC_SIGNATURES, the
RETINOTOPIC_MAP structure, and the FUNCTIONAL_DOMAINS set are
byte-identical on both sides.**

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (the syndrome, though the subtype emphasis differs —
right → Benson syndrome; left → progressive reading deficits), PRES,
and occipital infarct — are **documented identically in both
siblings**, with the side-appropriate field label.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_19" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] BRODMANN_NUMBER is 19.
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's.
[ ] ARCHITECTONIC_SIGNATURES is byte-identical to the left
    sibling's (including the dual-stream identity — the key
    feature).
[ ] V_AREA_CORRELATE is **exactly** ``("v3", "v4", "V3A", "V3B",
    "V5_MT_plus", "LOC")`` — byte-identical to the left
    sibling's.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **multi-mirror-flip** structure
    with the **LEFT hemifield label**.
[ ] FUNCTIONAL_DOMAINS contains **five** domains, **identical set
    to the left sibling's**:
    - motion_perception
    - spatial_localization
    - visual_attention
    - color_vision
    - form_and_object_perception
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — the same five domains.
[ ] **The FUNCTIONAL_DOMAINS ordering** lists motion_perception
    first (the right's dominant contribution), in contrast to
    the left's color_vision-first ordering. **The set is
    identical; the priority differs.**
[ ] FUNCTIONAL_DOMAINS **excludes** primary_visual_processing (BA
    17's domain).
[ ] FUNCTIONAL_DOMAINS **excludes** primary_visual_processing_
    secondary and binocular_vision (BA 18's domains).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing (left-
    lateralized; not instantiated on the right).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing as **BA 19 domains** — the right BA 19 is
    the *input stage* of the right face pathway and the
    *continuation* of the right global-processing advantage, but
    the domains live downstream.
[ ] **`global_visual_processing` is a right-specific emphasis
    within `form_and_object_perception`**, not a separate domain.
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis**:
    - motion_perception → motion_perception_dominant_left_hemifield_
      akinetopsia_more_severe_than_left
    - spatial_localization → v3a_v5_spatial_localization_dominant_
      left_hemifield_dorsal_attention_network
    - visual_attention → attentional_target_dorsal_attention_
      network_dominant
    - color_vision → pure_color_perception_left_hemiachromatopsia_
      felt_aspect
    - form_and_object_perception → object_recognition_right_ffa_
      face_pathway_ventral_stream_left_hemifield
[ ] CONNECTIVITY documents:
    - Pulvinar thalamic afferent (dominant; **on the right, the
      pulvinar → V5/MT+ and pulvinar → V3A projections are the
      dominant ones**)
    - LGN koniocellular direct-to-V4 afferent (weak; carries
      S-cone blue-yellow color; survives V1 lesions)
    - V2 / V3 → BA 19 principal cortical afferent (**on the
      right, the V2 / V3 → MT/V5 and V2 / V3 → V3A pathways are
      the dominant ones**)
    - **No direct V1 → BA 19 projection**
    - **V4 → LOC intra-BA 19**
    - **LOC → right FFA** (the face endpoint)
    - **V3A / V5/MT+ → right IPS** (the dominant dorsal-attention
      contribution)
    - **V4 / LOC → right inferotemporal** (the ventral stream)
    - **V3A → MT/V5 intra-BA 19** (the dominant motion pathway)
    - Callosal connections to left BA 19
    - Attentional feedback from right FEF, right DLPFC, right IPS,
      right TPJ
[ ] CLINICAL_ANCHORS contains the fifteen right-specific anchors:
    - right_ba19_left_hemiachromatopsia
    - right_ba19_left_hemifield_akinetopsia_more_severe
    - right_ba19_contribution_to_prosopagnosia
    - right_ba19_left_hemispatial_neglect_contribution
    - right_ba19_right_dorsal_attention_network_target
    - right_ba19_left_hemifield_motion_deficit_in_daily_life
    - right_ba19_visual_object_agnosia_associative
    - right_ba19_color_and_motion_processing_dissociation
    - right_ba19_right_motion_hemisphere_emphasis
    - right_ba19_global_visual_processing_contribution
    - right_ba19_occipital_infarct_pca_territory
    - right_ba19_migraine_visual_aura
    - right_ba19_occipital_epilepsy_visual_auras
    - right_ba19_posterior_cortical_atrophy_benson_syndrome
    - right_ba19_pres_visual_symptoms
[ ] The **left hemifield akinetopsia (more severe)** is documented
    as the primary right BA 19 anchor — the right V5/MT+ is the
    dominant motion hemisphere, and the right lesion produces a
    more severe deficit than the left equivalent.
[ ] **Prosopagnosia contribution** is documented as a right-
    emphasized anchor — **isolated right BA 19 lesions do not
    produce prosopagnosia**, but the right BA 19 is the occipital
    input stage of the right face pathway, and right occipito-
    temporal lesions that involve the right FFA or its input
    pathway produce prosopagnosia.
[ ] **Left hemispatial neglect contribution** is documented as a
    right-emphasized anchor — **isolated right BA 19 lesions do
    not produce neglect**, but right BA 19 is part of the right
    dorsal attention network substrate.
[ ] **Right dorsal attention network target** is documented as
    the right-specific attentional substrate.
[ ] **Right motion hemisphere emphasis** is documented as the
    right-emphasized anchor that underlies the more severe
    akinetopsia.
[ ] **Global visual processing contribution** is documented as a
    right-emphasized anchor (continuation of the right BA 18
    global emphasis).
[ ] The **color-motion dissociation** is documented as the
    strongest clinical evidence that V4 and V5/MT+ are separate
    areas — **on the right, the dissociation is more clinically
    prominent for motion than for color** because the right is
    the dominant motion hemisphere.
[ ] The **right PCA infarct's clinical signature** is documented
    as left hemianopia plus left hemiachromatopsia plus left
    hemifield motion deficit — the motion deficit is often the
    most functionally disabling.
[ ] **PCA subtype emphasis** is documented as right-lateralized
    to **Benson syndrome** (progressive prosopagnosia,
    visuospatial deficits, optic ataxia, simultanagnosia).
[ ] **Migraine aura and occipital epilepsy** are documented with
    the **BA 19-specific contributions** (color hallucinations,
    motion phosphenes, complex auras), byte-identically to the
    left sibling's treatment.
[ ] The **retinotopic multi-mirror-flip** is documented
    explicitly, with the LEFT hemifield label.
[ ] The **pulvinar-dominant thalamic input** is documented, with
    the right-emphasized V5/MT+ and V3A projections.
[ ] The **koniocellular LGN → V4 pathway** is documented as the
    subcortical substrate of blindsight for color.
[ ] The **BA 18 / BA 19 border variability** is documented as a
    caveat, byte-identically to the BA 18 sibling's treatment.
[ ] **Four V-area forward references** (V3A, V3B, V5_MT_plus,
    LOC) are documented; the resolution rule (remove from both
    hemispheres in the same commit) is recorded.
[ ] **The lingual gyrus forward reference** is documented,
    byte-identical to the left sibling's.
[ ] No SUBDIVISIONS promotion is performed while the V4 / V5/MT+
    / LOC split has not been matched by corresponding splits of
    the `..cortex/v4`, `..cortex/v5_mt_plus`, and `..cortex/loc`
    packages.
[ ] **V3A and V3B are not yet resolved** — their assignment to
    BA 19 or BA 18 must be resolved before the BA 19 split,
    hemisphere-invariant.
[ ] **V4 / V4α subdivision** must be decided in the same commit
    as any V4 split.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    V_AREA_CORRELATE, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, **FUNCTIONAL_DOMAINS set**, forward-declaration
    caveat text) match the left sibling; the RETINOTOPIC_MAP's
    represented hemifield, FUNCTIONAL_DOMAINS ordering,
    DOMAIN_EMPHASIS (dorsal vs ventral emphasis), CONNECTIVITY
    emphasis, and CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    BA 19 carries "left_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP; the left BA 19 carries "right_hemifield."
[ ] **The dorsal-vs-ventral emphasis is verified**: the right
    BA 19 carries "motion_perception_dominant" and "dorsal_
    attention_network_dominant"; the left BA 19 carries "color_
    form_language_integration" and "object_recognition_left_
    vwfa_reading_pathway."
[ ] **The right-only clinical anchors are verified**:
    `right_ba19_left_hemispatial_neglect_contribution`,
    `right_ba19_right_dorsal_attention_network_target`,
    `right_ba19_contribution_to_prosopagnosia`,
    `right_ba19_left_hemifield_akinetopsia_more_severe`,
    `right_ba19_right_motion_hemisphere_emphasis`,
    `right_ba19_global_visual_processing_contribution`, and
    `right_ba19_visual_object_agnosia_associative` are present
    on the right and absent on the left. The left-only
    `left_ba19_pure_alexia_without_agraphia`,
    `left_ba19_color_agnosia`, and `left_ba19_color_form_
    language_integration_deficit` anchors are absent on the
    right.
[ ] Any downstream code querying "what does the right BA 19
    see?" must receive "the LEFT visual hemifield."
[ ] Any downstream code querying "what is BA 19?" must receive
    "the V3A + V3B + V4 + V5/MT+ + LOC complex."
[ ] Any downstream code assigning the right face pathway must
    route through the **right** BA 19 (V4 / LOC) → right FFA
    chain.
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** BA 19 (V4 / LOC) → left VWFA
    chain.
[ ] Any downstream code assigning motion perception must weight
    the **right** BA 19 (V5/MT+) more heavily — the right
    V5/MT+ is the dominant motion hemisphere.
[ ] Any downstream code assigning left hemispatial neglect must
    note that **right BA 19 is a contributor**, not a sole
    cause.
[ ] Any downstream code assigning global visual processing must
    weight the **right** BA 19 (LOC + V5/MT+) more heavily.
[ ] Any downstream code assigning the **felt / phenomenal aspect
    of color experience** must weight the **right** BA 19 (V4)
    more heavily; any downstream code assigning **color-form-
    language integration** must weight the **left** BA 19 (V4)
    more heavily.
"""