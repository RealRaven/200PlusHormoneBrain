"""
Brodmann Area 18 (Secondary Visual Cortex) — Left Hemisphere
=============================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── brodmann_areas
                                    └── brodmann_area_18   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 18** — the **secondary visual cortex**, the
extrastriate territory that **surrounds BA 17 (V1)** on the medial and
lateral surfaces of the occipital lobe. Unlike BA 17, whose 1:1 V-area
correspondence makes it the cleanest leaf in the cortex tree, **BA 18
spans two** modern functional areas — **V2** and **V3** — and its
`V_AREA_CORRELATE` field is a **two-element tuple**, not a single-element
one.

Parent: ``..brodmann_areas`` (left occipital BA registry) — sibling to
BA 17 and BA 19.

This package is the **structural mirror** of
``../../right/cortex/occipital/brodmann_areas/brodmann_area_18``. The
BA number, the two V-area correlates (V2 + V3), the architectonic
signatures, the retinotopic mirror-flip, and the V1/V2 and V2/V3
borders are identical on both sides; the **functional emphasis** and
**clinical significance** diverge — on the left, BA 18 is weighted
toward the **local / featural** aspect of visual processing, its V2 and
V3 outputs feed the **left ventral stream** through V4 toward the left
visual word form area (VWFA), and the left BA 18 lesions produce **right
quadrantic visual field defects** more often than the right produces
left ones.

**The most consequential structural fact about BA 18** is its
**retinotopic mirror-flip relative to V1**. Each subsequent visual area
(V2, V3, V4, V3A, etc.) is a **mirror reflection** of the preceding one
across the field-sign boundary between them:

    V1 → V2:  mirror-flip across the V1/V2 border
              (vertical meridian)
    V2 → V3:  mirror-flip across the V2/V3 border
              (horizontal meridian)
    V3 → V3A: mirror-flip across the V3/V3A border

This means that **V1 upper field and V2 upper field are not on the same
bank of the calcarine sulcus** — they are on **adjacent** banks that
happen to be near the calcarine sulcus, and the same for lower fields.
The mirror-flip is why the retinotopic organization of the occipital
lobe is described as **alternating mirror images**, and it is one of the
most important architectural facts for interpreting visual field
defects: a lesion in V2 or V3 can produce a visual field defect that
**does not coincide with the field defect from a V1 lesion at the same
cortical location**.

--------------------------------------------------------------------------------
WHAT BA 18 IS
--------------------------------------------------------------------------------

BA 18 is the **secondary visual cortex** — the belt of cortex that
**surrounds BA 17** on the medial and lateral surfaces of the occipital
lobe. In Brodmann's original map, BA 18 is a **single cytoarchitectonic
area** that lies caudal to the V1/V2 border and rostral to the BA 18 /
BA 19 border. In modern retinotopic parcellations, BA 18 contains **two
distinct functional areas**:

    V2    The secondary visual cortex, immediately surrounding V1.
          Processes **border ownership, texture, illusory contours,
          surface filling-in, and stereoscopic depth from
          binocular disparity**. V2 has a **mirror-image
          retinotopic map** relative to V1 — the upper field is
          on the upper bank of the calcarine region and the lower
          field on the lower bank, **reversed relative to V1**.

    V3    The tertiary visual cortex, immediately surrounding V2.
          Processes **dynamic form, motion boundaries, coherent
          motion detection, and depth from motion** (via its
          relay to MT/V5). V3 has a **mirror-image retinotopic
          map** relative to V2 — the upper field is on the upper
          bank and the lower field on the lower bank, **reversed
          relative to V2**, which restores the same physical bank
          relationship as V1 but with the field labels flipped
          again. The **V2/V3 border** is the representation of
          the **horizontal meridian**.

**A note on V3A and V3B**. Some parcellation schemes subdivide BA 18
further into V3A (ventrolateral V3, motion and motion-in-depth) and V3B
(ventrolateral V3, kinetic contours). **These are forward references in
the tree** — V3A and V3B are not yet packages under ``..cortex`` — and
they are recorded in the parent ``..brodmann_areas``'s
``FORWARD_REFERENCE_V_AREAS`` tuple. BA 18's primary correlates are V2
and V3; V3A and V3B are nearby territories that some schemes assign to
BA 18 and some to BA 19, and their assignment is **scheme-dependent**.
The BA 18 package's `V_AREA_CORRELATE` field records only the
**unambiguous** V2 + V3 assignment.

**The architectonic signatures of BA 18** are:

    V2 (part of BA 18)   The **dysgranular** extrastriate cortex,
                         with a **distinct layer IV** that is
                         present but less prominent than in V1.
                         Contains **cytochrome-oxidase stripes**
                         (the "V2 stripes") that are visible on
                         histochemical staining — the **thin
                         stripes** project to V4 (color and form),
                         the **thick stripes** project to MT/V5
                         (motion), and the **pale stripes** project
                         to the inferotemporal cortex. The stripes
                         are the anatomical basis for the **V2
                         → three-stream output** (ventral, dorsal,
                         and IT).

    V3 (part of BA 18)   The **dysgranular** extrastriate cortex
                         with a **more prominent layer IV** than V2
                         and a **weaker layer V**. V3 is
                         architectonically intermediate between V2
                         and V4.

**The retinotopic organization of BA 18** is the **most clinically
consequential** aspect of the territory, because the **mirror-flip**
between V1, V2, and V3 creates the **alternating visual field
representation** that produces the classic **quadrantic and sectoranopic
field defects** from BA 18 lesions:

    V2 upper field → upper bank of the calcarine region
        **V2's upper field is on the upper bank** — the **opposite**
        bank from V1's upper field, which is on the lower bank. The
        V2 map is a **mirror image** of the V1 map across the
        V1/V2 border (which is the vertical meridian).

    V2 lower field → lower bank of the calcarine region
        **V2's lower field is on the lower bank** — the opposite
        bank from V1's lower field.

    V2 vertical meridian → V1/V2 border
        The **V1/V2 border** represents the **vertical meridian**
        in both V1 and V2, and is the **mirror-flip axis** between
        them.

    V2 horizontal meridian → V2/V3 border
        The **V2/V3 border** represents the **horizontal meridian**
        in V2 and V3, and is the **mirror-flip axis** between V2
        and V3.

    V3 upper field → upper bank of the calcarine region (again)
        **V3's upper field is on the upper bank** — the **same**
        bank as V2's upper field, but on the **far side** of the
        V2/V3 border. The V3 map is a **mirror image** of the V2
        map across the V2/V3 border (horizontal meridian).

    V3 lower field → lower bank of the calcarine region (again)
        **V3's lower field is on the lower bank** — the same bank
        as V2's lower field, on the far side of the V2/V3 border.

**Left-hemisphere specificity**: the left BA 18 processes the **RIGHT**
visual hemifield of both eyes (contralateral processing). The
**right homonymous hemianopia or quadrantic defect** that follows a
left BA 18 lesion is the canonical left-lateralized visual-field
deficit for this territory. **On the left, BA 18's V2 and V3 outputs
feed the left ventral stream through V4 toward the left VWFA**, and the
left BA 18 is therefore the **second stage of the left reading
pathway** after BA 17. The left BA 18 is also weighted toward the
**local / featural aspect** of visual processing (Navon's
local-precedence asymmetry), in contrast to the right BA 18's **global /
holistic** emphasis.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours
        caudally               BA 17 (V1) via the V1/V2 border
        rostrally              BA 19 (V3A, V4, V5/MT+) via the
                               BA 18 / BA 19 border
        laterally              the lateral occipital gyri
                               (overlapping BA 18 on the lateral
                               surface)
        medially               the cuneus and lingual gyrus
                               (overlapping BA 18 on the medial
                               surface, adjacent to BA 17)
        ventrally              the lingual gyrus / parahippocampal
                               region (BA 18's inferior edge)

    Functional overlays
        V2 — secondary visual cortex (part of BA 18)
            The first extrastriate area, immediately surrounding
            V1. Processes border ownership, texture, illusory
            contours, surface filling-in, and stereoscopic depth.
            **On the left, V2's outputs feed the left ventral
            stream via V4 and the dorsal stream via MT/V5.**
        V3 — tertiary visual cortex (part of BA 18)
            The second extrastriate area, immediately surrounding
            V2. Processes dynamic form, motion boundaries, coherent
            motion, and depth from motion. **On the left, V3's
            outputs feed the left dorsal stream via MT/V5 and the
            left ventral stream via V4.**
        V3A / V3B — forward references
            Sub-areas of the V3 complex, assigned to BA 18 in some
            parcellations and to BA 19 in others. **Not yet
            packages under ``..cortex``** — recorded as forward
            references.
        cuneus — upper-bank territory
            The cuneus's lower margin carries the **V2 and V3
            upper-bank representations of the lower** contralateral
            visual field. **On the left, the lower RIGHT field.**
            (Note the mirror-flip: **V1's upper field is on the
            lower bank, but V2 and V3's upper fields are on the
            upper bank** — the exact opposite physical location
            for the same field label.)
        lingual gyrus — lower-bank territory
            The lingual gyrus carries the **V2 and V3 lower-bank
            representations of the upper** contralateral visual
            field. **On the left, the upper RIGHT field.**
        lateral occipital gyrus — lateral territory
            The lateral occipital gyrus is overlapped by BA 18 on
            its lateral aspect (V3 on the lateral surface). **On
            the left, the lateral V3 representation is part of the
            left dorsal stream's contribution to the right-
            hemifield motion processing.**
        calcarine sulcus — landmark
            The calcarine sulcus is the **fundus** of the V1
            representation; BA 18 lies on both banks of the
            calcarine sulcus and extends beyond it caudally and
            laterally. The calcarine sulcus is **not** the primary
            landmark for BA 18 (it is the landmark for BA 17), but
            it is the reference point for the **V1/V2 border**
            which is the caudomedial boundary of BA 18.

**This field is structurally identical to the right sibling's** — the
architectonic neighbours and the V2 / V3 / cuneus / lingual-gyrus /
lateral-occipital-gyrus / calcarine overlays are the same on both
sides. What differs is the **visual hemifield** — the left BA 18
processes the RIGHT hemifield, and the cuneus / lingual gyrus
representations carry the upper / lower RIGHT field on the left. The
**local-vs-global processing asymmetry** is the second axis of
divergence.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 17 (V1)                             **caudal neighbour** via the
                                           V1/V2 border; the vertical
                                           meridian of the visual
                                           field is represented at
                                           this border. The BA 17 →
                                           BA 18 projection is the
                                           first step of the
                                           V1 → V2 → V3 → V4 / MT+
                                           hierarchy.
    BA 19 (V3A + V4 + V5/MT+)              **rostral neighbour** via the
                                           BA 18 / BA 19 border.
                                           V2's outputs reach V4
                                           (via the thin stripes)
                                           and MT/V5 (via the thick
                                           stripes); V3's outputs
                                           reach MT/V5, V3A, and
                                           V4.
    BA 41 / BA 42 (temporal, auditory)     **distant neighbour** across
                                           the occipito-temporal
                                           junction; no naming
                                           collision with the
                                           occipital BA 18 (the
                                           temporal BA 41 / BA 42
                                           are auditory cortex, a
                                           different territory)
    cuneus (medial-surface gyrus)          carries the **V2 / V3
                                           upper-bank** representation
                                           of the **lower** visual
                                           field (**lower RIGHT field
                                           on the left**)
    lingual gyrus (medial-surface          carries the **V2 / V3
    gyrus; forward reference in ..gyri)    lower-bank** representation
                                           of the **upper** visual
                                           field (**upper RIGHT field
                                           on the left**)
    lateral occipital gyrus                carries the **lateral V3**
                                           representation; part of
                                           the left dorsal stream's
                                           contribution to right-
                                           hemifield motion
                                           processing
    calcarine sulcus                       the **fundus** of the V1
                                           representation; the
                                           V1/V2 border (the
                                           caudomedial boundary of
                                           BA 18) is adjacent to
                                           the calcarine sulcus

**This field is byte-identical to the left sibling's.** The adjacency
relationships are topological, not lateralized.

**A note on the BA 18 / BA 19 border.** Unlike the V1/V2 border, which
is architectonically unambiguous (the stria of Gennari's abrupt
disappearance), the **BA 18 / BA 19 border is more variable** across
individuals. The border roughly coincides with the **lunate sulcus**
(when present) on the lateral surface and with the **transverse
occipital sulcus** region on the medial surface, but neither sulcus is
a perfectly reliable landmark. Modern parcellations (HCP 180-area,
Öngür-Price, Petrides-Pandya) subdivide the BA 18 / BA 19 transition
under different labels, and downstream code that needs a specific
boundary should use the **retinotopic** border (the horizontal
meridian at the V2/V3 border) rather than the architectonic one when
available. **This caveat is byte-identical to the right sibling's.**

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 18 (= V2 + V3) participates in **four** canonical occipital
functional domains. On the left, the emphasis is as follows:

    primary_visual_processing (secondary)          (left emphasis — PRIMARY)
        **This is BA 18's first defining contribution.** The
        **second** cortical stage of vision, after BA 17 (V1). V2
        adds **border ownership, texture, illusory contours,
        surface filling-in, and stereoscopic depth** to the
        low-level features extracted by V1. V3 adds **dynamic
        form, motion boundaries, and depth from motion**. On the
        left, BA 18 processes the **RIGHT visual hemifield**.

    binocular_vision                               (left emphasis — PRIMARY)
        V2's binocular disparity neurons — which are **more
        numerous and more selective than in V1** — support
        **fine stereoscopic depth perception** and **binocular
        fusion**. V3 adds depth from motion. On the left,
        binocular vision in V2 / V3 combines the right-eye and
        left-eye inputs to the **RIGHT visual hemifield**.

    form_and_object_perception                     (left emphasis — SECONDARY)
        **This is BA 18's most left-lateralized contribution.**
        V2's **thin stripes** and V3's **dynamic-form**
        representations contribute to the **early stages of form
        and object processing** that continue in V4 and the LOC.
        **On the left, the form-and-object contribution is
        weighted toward the LOCAL / FEATURAL aspect** — the left
        hemisphere's documented advantage in local processing
        (Navon's local-precedence asymmetry is the mirror of the
        right's global-precedence). The left's **local / featural
        processing** is captured here as the left-specific
        emphasis within `form_and_object_perception`; it is not a
        separate domain.

    spatial_localization                           (left emphasis — SECONDARY)
        V3's **motion-boundary** and **depth-from-motion**
        representations contribute to the **early stages of
        spatial localization** that continue in V3A and MT/V5.
        **On the left, the spatial-localization contribution is
        present but weaker than on the right** — the right V3 is
        more strongly engaged during visuospatial attention and
        motion-in-space processing, and the left's contribution
        is predominantly to the **ventral stream** (form, color,
        reading) rather than the dorsal stream.

**Left-specific caveat on `primary_visual_processing` (BA 17's
domain).** The label is shared with BA 17, but the **emphasis**
differs. BA 17's `primary_visual_processing` is the **first**
cortical stage — orientation, contrast, spatial frequency. BA 18's
`primary_visual_processing (secondary)` is the **second** stage —
border ownership, texture, filling-in, motion boundaries. The
parent ``..brodmann_areas`` registers BA 17's and BA 18's
`primary_visual_processing` entries as **distinct emphases**, not
duplicates; downstream code must not conflate them.

**Left-specific caveat on `color_vision`.** BA 18 is **not** the
color-vision area — that is V4, in BA 19. BA 18's **thin stripes**
(V2) and **V3** project **to** V4, but the conscious perception of
color emerges in V4. `color_vision` is **omitted** from the BA 18
`FUNCTIONAL_DOMAINS` tuple; it appears in BA 19 (V4) instead.

**Left-specific caveat on `motion_perception`.** BA 18 is **not** the
motion area — that is V5/MT+, in BA 19. BA 18's **thick stripes** (V2)
and **V3** project **to** MT/V5, and V3 itself has **motion-boundary**
sensitivity, but **conscious motion perception** emerges in MT/V5.
`motion_perception` is **omitted** from the BA 18 `FUNCTIONAL_DOMAINS`
tuple; it appears in BA 19 (MT/V5) instead. **On the right, V3 is more
strongly engaged during motion-boundary processing than on the left**,
but the right BA 18 still does not carry `motion_perception` as a
primary domain — that is MT/V5's territory.

**Left-specific caveat on `visual_attention`.** BA 18 is a **target**
of top-down attentional modulation from the frontal eye fields (BA 8)
and the dorsolateral prefrontal cortex, but it is **not** itself an
attentional control area. `visual_attention` is **omitted** from the
BA 18 `FUNCTIONAL_DOMAINS` tuple as a primary domain.

**Left-specific caveat on `visual_word_processing`.** BA 18 is the
**second stage** of the left ventral stream that feeds the left VWFA,
but BA 18 itself does **not** perform word processing. The VWFA is in
the left fusiform gyrus, several synapses downstream (via V4 and the
LOC). `visual_word_processing` is **omitted** from the BA 18
`FUNCTIONAL_DOMAINS` tuple.

**Left-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the left
BA 18 does **not** carry. `face_processing` is instantiated in the
right FFA (fed by the right BA 17 → BA 18 → BA 19 → LOC → FFA
pathway); `global_visual_processing` **begins at right BA 18** (V2 /
V3) and is the right-hemisphere's documented advantage. Neither
appears in the left BA 18 `FUNCTIONAL_DOMAINS` tuple.

**Summary**: BA 18 carries **exactly four** functional domains —
`primary_visual_processing (secondary)`, `binocular_vision`,
`form_and_object_perception`, and `spatial_localization`. The first
two are shared with BA 17; the last two are BA 18-specific additions
that reflect V2's and V3's contributions to the ventral and dorsal
streams. **The left emphasis is on `form_and_object_perception`
(local / featural) and a secondary `spatial_localization`** — the
right's emphasis is on `form_and_object_perception` (global /
holistic) and a dominant `spatial_localization` and
`global_visual_processing`.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), left — via V1 relay
            **BA 18's dominant input is from V1, not directly
            from the LGN.** The LGN → V1 → BA 18 pathway is the
            **obligate relay** for V2's and V3's visual input.
            Direct LGN → V2 projections exist (the **koniocellular
            pathway**) but are weaker and modulatory.
        → pulvinar (secondary, modulatory)
            The pulvinar sends a **stronger modulatory projection
            to V2 and V3 than to V1**, participating in the
            cortico-thalamo-cortical loops that support visual
            attention and visual short-term memory.

    cortical afferents
        → BA 17 (V1), left
            **BA 18's principal cortical afferent.** The V1 →
            V2 projection is the first step of the V1 → V2 → V3
            hierarchy, and it carries the low-level features that
            V2 transforms into border ownership, texture, and
            surface representations.
        → V2 → V3 (intra-BA 18)
            V2's outputs project to V3 within BA 18, forming the
            **V2 → V3 relay** that carries the surface and border
            representations forward to the dynamic-form and
            motion-boundary processing.

    cortical efferents
        → V4 (via V2 thin stripes), left
            The **V2 thin stripes** carry the color and form
            signal forward to V4. This is the **ventral stream**
            (the "what" pathway) originating in V2's thin stripes
            and continuing through V4 to the LOC and the left VWFA.
        → MT/V5 (via V2 thick stripes and V3), left
            The **V2 thick stripes** and **V3** carry the motion
            and motion-boundary signal forward to MT/V5. This is
            the **dorsal stream** (the "where" pathway)
            originating in V2's thick stripes and V3, continuing
            through MT/V5 to the parietal cortex.
        → inferotemporal cortex (via V2 pale stripes), left
            The **V2 pale stripes** carry the object-form signal
            forward to the inferotemporal cortex, contributing to
            the ventral stream's object-recognition hierarchy.
            On the left, this pathway feeds the left VWFA (via
            V4 and the LOC) — the reading endpoint.
        → BA 19 (V3A, V4, V5/MT+), left
            V2 and V3 project forward to BA 19's functional areas
            via the three-stripe pattern described above. The
            **BA 18 → BA 19** projection is the second step of
            the occipital hierarchy.

    callosal connections
        → right BA 18
            The callosal fibers connect the left BA 18 to the
            right BA 18 at the **vertical meridian** (the V1/V2
            border) and across the upper and lower banks of the
            calcarine region. This callosal connection supports
            **the fusion of the two hemifields** at the V2 and V3
            stage, and it is essential for the **continuity of
            visual perception across the vertical midline** at the
            extrastriate level.

    attentional feedback
        → frontal eye fields (BA 8), left
            The FEF sends **top-down attentional gain** to BA 18,
            modulating the responsiveness of V2 and V3 neurons to
            behaviourally relevant stimuli. **On the left, the
            FEF → BA 18 projection is part of the left dorsal
            attention network's contribution to right-hemifield
            spatial attention**; it is present but weaker than the
            right FEF → right BA 18 projection.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), left
            The DLPFC sends top-down attentional and working-memory
            signals to BA 18, supporting **visual working memory**
            and **visual imagery**.
        → intraparietal sulcus, left
            The IPS sends dorsal-attention-network signals to
            BA 18, supporting **spatial attention** in the RIGHT
            visual hemifield. **On the left, the IPS → BA 18
            projection is present but weaker than on the right.**

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in three respects:
(a) the BA 18 → V4 pathway is the **left ventral stream** that feeds
the left VWFA for reading; the right's BA 18 → V4 pathway feeds the
right LOC for face processing;
(b) the BA 18 → MT/V5 pathway is present on both sides, but the
**right's is more strongly engaged** during visuospatial attention and
motion-in-space processing;
(c) the callosal connections carry the **right-hemifield / left-
hemifield fusion** signal at the V2 / V3 level, which on the left is
the **left half of the fused extrastriate visual field**.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_ba18_right_quadrantic_visual_field_defect
        **This is the left BA 18 anchor par excellence.** Unlike
        BA 17, whose lesions produce a **complete** right homonymous
        hemianopia (because V1 represents the entire contralateral
        hemifield), BA 18's lesions produce **partial** field
        defects — most characteristically a **right quadrantic** or
        **sectoranopic** defect. The classic BA 18-lesion field
        defect is a **right inferior quadrantic** field loss
        (from an upper-bank BA 18 lesion) or a **right superior
        quadrantic** field loss (from a lower-bank BA 18 lesion),
        **often with macular sparing** because the foveal
        representation at the occipital pole is fed by the
        dual-blood-supply V1 territory rather than BA 18 proper.

    left_ba18_quadrantic_defect_with_reading_field_shift
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **right homonymous field defect** — is a
        recognized clinical entity after left BA 18 lesions that
        produce a partial right field defect. The patient's
        reading is slowed because they must make **large rightward
        saccades** to compensate for the missing right hemifield,
        and the **left-hemisphere reading network** cannot
        function efficiently without the full right-hemifield
        input. **The left BA 18 lesion produces a milder alexia
        than a complete left BA 17 lesion** — the partial field
        defect is less disruptive than the complete hemianopia,
        and the reading network itself (left VWFA, left angular
        gyrus) is intact.

    left_ba18_visual_form_processing_deficit
        **On the left, BA 18's V2 / V3 contribution to form and
        object processing is weighted toward the local / featural
        aspect.** Left BA 18 lesions can produce **local-level
        form processing deficits** — the patient may still
        perceive global shape but cannot resolve fine local
        features. **This is a left-weighted anchor**; the right
        BA 18 lesion produces the complementary **global-level
        form processing deficit** (Navon's global-precedence
        asymmetry is the framework).

    left_ba18_color_and_motion_indirect_deficits
        BA 18's thin and thick stripes project to V4 and MT/V5,
        respectively. **Left BA 18 lesions can produce indirect
        color or motion processing deficits** — the V4 and MT/V5
        areas themselves are intact, but their input from BA 18
        is degraded. The color deficit in a BA 18 lesion is
        typically **milder** than in a V4 lesion, and the motion
        deficit in a BA 18 lesion is typically **milder** than in
        a V5/MT+ lesion. **Isolated achromatopsia (V4) or
        akinetopsia (V5/MT+) from a BA 18 lesion would be
        unexpected** — the deficit is a *processing* impairment,
        not a *perceptual absence*.

    left_ba18_hemianopic_alexia_right
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **right homonymous hemianopia or
        quadrantic defect** (from a left BA 18 lesion extending
        into BA 17) — is the most common reading deficit after
        an occipital lesion, and it is often clinically
        under-recognized compared to alexia without agraphia.
        The deficit is **mild** (the patient can still read, but
        more slowly and with more effort), **recoverable** (many
        patients compensate within weeks), and **left-lateralized**
        (the left reading network is disconnected from the full
        right hemifield).

    left_ba18_alexia_without_agraphia_left_occipital_plus_splenium
        **If the left BA 18 lesion is large enough to involve the
        left splenium** in addition to the BA 17 / BA 18 territory,
        the patient may develop **alexia without agraphia** (as
        described in the left BA 17 sibling). **Isolated BA 18
        lesions do NOT produce alexia without agraphia** — the
        syndrome requires the splenium disconnection, which is
        outside BA 18 proper. The BA 18 lesion's contribution is
        to the **right-hemifield field defect**, not to the
        splenium disconnection.

    left_ba18_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including **BA 17 AND BA 18**. The spread
        typically begins in V1 and moves into V2 / V3, producing
        the **fortification spectrum** as the wave passes through
        the retinotopic maps. **The BA 18 contribution** is the
        propagation of the visual aura from V1's simple features
        (flashes) to V2 / V3's more complex features (the
        zigzag fortification lines). This anchor is
        hemisphere-invariant, but the aura's field involvement
        is contralateral (right field on the left side).

    left_ba18_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** —
        elementary visual hallucinations (flashing lights, colored
        shapes, geometric patterns) in the **contralateral visual
        field** — can arise from **BA 17 OR BA 18**. **BA 18
        auras** are typically **more complex** than BA 17 auras —
        the patient may see **formed objects, recognizable
        scenes, or specific colors** in addition to elementary
        shapes — because V2 and V3 process more complex features
        than V1. **Left BA 18 auras** project to the **right
        visual field** and can be preceded or accompanied by
        **visual field defects** that persist after the seizure.

    left_ba18_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **BA 17 AND BA 18 bilaterally** in
        later stages, but early PCA affects the **dorsal and
        ventral association cortices** (V3A, V4, V5/MT+, and the
        LOC) more than BA 18 proper. **Left BA 18** is part of
        the substrate of the **progressive ventral stream
        dysfunction** that affects the left VWFA and reading in
        the later stages of PCA. **On the left, PCA can produce
        progressive reading deficits** (the "visual variant" of
        progressive aphasia), while on the right it produces
        progressive prosopagnosia and visuospatial deficits.

    left_ba18_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia or
        quadrantic defects** from **bilateral occipital
        involvement**. **The BA 18 contribution** is the
        **extrastriate involvement** that produces **visual
        hallucinations** (V2 / V3 hyperexcitability) and
        **quadrantic defects** (V2 / V3 partial loss). **The
        syndrome is reversible** in most cases.

    left_ba18_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** involving
        **BA 17 AND BA 18** produces a **right homonymous
        hemianopia** (from BA 17) **plus** a **right quadrantic
        or sectoranopic defect** (from BA 18) and, in some cases,
        **cortical blindness in the affected field** with
        **macular sparing**. The PCA territory includes the left
        calcarine cortex, the left lingual gyrus, the left cuneus,
        and (via the posterior pericallosal artery) the left
        splenium. **The BA 18-specific contribution** is the
        **quadrantic** extension of the field defect beyond the
        V1-only hemianopia.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 18 processes the **RIGHT visual hemifield**, so left
BA 18 lesions produce **right-sided** visual deficits; (b) the left
BA 18 is the **second stage of the left reading pathway**, so left
BA 18 lesions can produce **hemianopic alexia** and contribute to the
left-lateralized reading deficits. **The local / featural emphasis**
is a third left-specific feature — the left BA 18 is weighted toward
local processing, and left BA 18 lesions produce local-level form
deficits that have no symmetric counterpart on the right. The right
sibling's docstring carries the corresponding right-sided anchors
(left homonymous hemianopia or quadrantic defect, left-hemifield
hemianopic alexia (milder), global-level form processing deficit,
prosopagnosia contribution, and the right-lateralized global
processing emphasis).

**The `migraine_visual_aura`, `PRES`, and `cortical blindness`
anchors are hemisphere-invariant** — they appear on both sides and are
documented identically in both siblings, with the side-appropriate
field label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left occipital BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 18 (which on the
    left is ``("primary_visual_processing_secondary",
    "binocular_vision",
    "form_and_object_perception_local_featural",
    "spatial_localization_v3")``), and enforcer of the **two-element
    V_AREA_CORRELATE (V2 + V3)** — a departure from BA 17's
    single-element correlate.

..brodmann_area_17_primary_visual
    **Caudal neighbour** via the V1/V2 border. The BA 17 → BA 18
    projection is the first step of the V1 → V2 → V3 → V4 / MT+
    hierarchy. **The vertical meridian of the visual field is
    represented at the V1/V2 border**, and the callosal connections
    between the left and right hemispheres meet at this border
    (in the BA 18 territory, not BA 17 proper). **The
    retinotopic mirror-flip** between V1 and V2 is the defining
    feature of the V1/V2 border, and it is why BA 18's upper-
    field / lower-field bank assignments are **reversed** relative
    to BA 17's.

..brodmann_area_19
    **Rostral neighbour** via the BA 18 / BA 19 border. BA 18's
    V2 and V3 outputs reach BA 19's V4 (via the thin stripes)
    and V5/MT+ (via the thick stripes), completing the
    V1 → V2 → V3 → V4 / MT+ hierarchy. **The BA 18 / BA 19
    border is more variable than the V1/V2 border** — the
    horizontal meridian at the V2/V3 border is the more reliable
    retinotopic landmark, and downstream code should prefer the
    retinotopic landmark over the architectonic one when
    available.

...cortex.v2
    The **functional V2 package under ``..cortex``** — the direct
    counterpart of the V2 half of this BA package. Where this
    package describes the **cytoarchitectonic** BA 18, the V2
    package describes the **functional-retinotopic** V2. The two
    packages overlap on the same territory and cross-reference
    each other via the parent's ``BA_TO_V_CROSSWALK``.

...cortex.v3
    The **functional V3 package under ``..cortex``** — the direct
    counterpart of the V3 half of this BA package. **V3 is one of
    the two V areas that BA 18 spans** (the other is V2), and
    its inclusion is what makes BA 18's `V_AREA_CORRELATE` a
    two-element tuple.

...cortex.v4  (forward reference in the sense that V4 is a child
    of BA 19, but the V4 package exists)
    V2's **thin stripes** project forward to V4, and V4 is where
    the conscious perception of color and the ventral stream's
    form-and-object hierarchy begin. **On the left, the
    V2 → V4 pathway feeds the left VWFA** (via the LOC), and the
    left BA 18 is the **second stage** of the left reading
    pathway.

...cortex.primary_visual_cortex  (V1)
    **Not a direct target of BA 18** — V1 is the **source** of
    BA 18's input, not its output. But V1 and V2 / V3 together
    form the **core occipital hierarchy**, and the parent
    ``..brodmann_areas``'s crosswalk records the V1 → V2 → V3
    sequence.

...cuneus
    The medial-surface gyral landmark. The cuneus's lower margin
    (the upper bank of the calcarine region) carries the **V2 /
    V3 upper-bank representations of the lower** contralateral
    visual field. **On the left, the lower RIGHT field.** Note the
    mirror-flip: **V1's upper field is on the LOWER bank, but V2
    and V3's upper fields are on the UPPER bank** — the exact
    opposite physical location for the same field label.

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus carries the **V2 / V3 lower-bank**
    representations of the upper contralateral visual field.
    **On the left, the upper RIGHT field.** The same mirror-flip
    applies: **V1's lower field is on the UPPER bank, but V2 and
    V3's lower fields are on the LOWER bank**.

...gyri.lateral_occipital_gyrus
    The lateral-surface gyral territory. BA 18's **lateral V3**
    representation overlays the lateral occipital gyrus, and the
    left lateral V3 is part of the left dorsal stream's
    contribution to right-hemifield motion processing.

...sulci.calcarine_sulcus
    The **fundus of the V1 representation**; the V1/V2 border (the
    caudomedial boundary of BA 18) is adjacent to the calcarine
    sulcus. **Not the primary landmark for BA 18** (that is the
    lunate sulcus when present, or the transverse occipital
    sulcus), but the reference point for the V1/V2 mirror-flip.

...sulci.lunate_sulcus
    The **lateral-surface landmark** for the BA 18 / BA 19 border,
    **when present** (the lunate sulcus is inconstant in humans).
    When absent, the BA 18 / BA 19 border must be inferred from
    the retinotopic V2/V3 border rather than the architectonic
    one.

...sulci.transverse_occipital_sulcus
    The **medial-surface landmark** for the posterior boundary of
    the lateral occipital gyri; the BA 18 / BA 19 border on the
    medial surface is roughly adjacent to the transverse occipital
    sulcus.

..cortex.temporal
    The **ventral stream** continues from BA 18 (via V4 and the
    LOC) into the temporal lobe. **On the left, the ventral
    stream terminates in the left VWFA** (the reading area), and
    the left BA 18 is the **second stage** of this pathway. The
    temporal package must declare the left BA 18 as a source of
    its visual input via the ventral stream, and must note the
    **left-lateralized VWFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from BA 18 (via V3 and MT/V5)
    into the parietal lobe. **On the left, the dorsal stream
    supports right-hemifield spatial attention** via the left
    intraparietal sulcus, but the left's contribution is weaker
    than the right's. The parietal package must declare the left
    BA 18 as a source of its visual input for the dorsal stream
    via the BA 19 / MT/V5 relay.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to BA 18. The frontal package must declare the left
    BA 18 as a target of its attentional projections.

..cortex.cingulate  — indirect
    No direct cingulate → BA 18 projection. Recorded here to
    pre-empt a false cross-reference.

..cortex.insular  — indirect
    No direct insular → BA 18 projection. Recorded here to
    pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the **indirect** source of BA 18's input via
    the V1 relay. **Direct LGN → V2 projections exist via the
    koniocellular pathway but are weaker and modulatory.** The
    thalamus package must declare the LGN as the primary visual
    thalamic relay to BA 17, and must note that BA 18 receives
    its LGN input **indirectly via V1** (plus a weaker direct
    koniocellular projection).

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V2
    and V3 than to V1**, participating in the cortico-thalamo-
    cortical loops that support visual attention and visual
    short-term memory.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from BA 18 (via V4 and the LOC)
    to the perirhinal, entorhinal, and parahippocampal cortices.
    **The left BA 18 is the second stage** of the occipito-
    temporal-hippocampal pathway that supports visual object
    recognition and visual memory.

../../right/cortex/occipital/brodmann_areas/brodmann_area_18
    The right-hemisphere homologue. Structural fields (BA number,
    V-area correlates V2 + V3, architectonic signatures, V1/V2
    and V2/V3 borders, retinotopic mirror-flip, three-stripe
    V2 organization, cuneus / lingual-gyrus / lateral-occipital-
    gyrus relationships) MUST be byte-identical. Functional
    emphasis and clinical significance diverge — the right BA 18
    processes the **LEFT** visual hemifield, is weighted toward
    the **global / holistic** aspect of form processing, and its
    V2 / V3 outputs feed the right ventral stream toward the
    right FFA (for faces) rather than the left VWFA (for reading).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_18"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    BRODMANN_NUMBER     = 18
    ALTERNATE_NAMES     = ("secondary_visual_cortex",
                           "extrastriate_cortex_belt",
                           "V2_V3_complex")
        # **Note the plural**: BA 18 is not a single V area.
        # Unlike BA 17 ("V1"), BA 18 is the joint cytoarchitectonic
        # parent of V2 and V3.

    ARCHITECTONIC_SIGNATURES = (
        "cytochrome_oxidase_stripes_in_V2",
        "dysgranular_extrastriate_cortex",
        "variable_BA18_BA19_border",
    )
        # **Three signatures**: the V2 CO stripes (thin / thick /
        # pale — the basis of the V2 → three-stream output), the
        # dysgranular cytoarchitecture, and the variable BA 18 /
        # BA 19 border (the only BA border in the occipital lobe
        # that is not architectonically unambiguous).

    V_AREA_CORRELATE    = ("v2", "v3")
        # **Two elements, not one** — the departure from BA 17's
        # single-element (`primary_visual_cortex`) correlate.
        # **V3A and V3B are NOT included** — their assignment to
        # BA 18 vs BA 19 is scheme-dependent, and they are
        # recorded as forward references in the parent registry.

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** BA 18 is unique to the occipital
        # lobe.

    RETINOTOPIC_MAP     = "mirror_flip_of_V1_across_V1_V2_border"
        # The map's structure: V2's upper field is on the UPPER
        # bank (opposite V1's lower-bank upper field), V2's lower
        # field is on the LOWER bank (opposite V1's upper-bank
        # lower field), the V1/V2 border is the vertical meridian,
        # and the V2/V3 border is the horizontal meridian. V3 is
        # a second mirror-flip of V2 across the V2/V3 border.
        # **On the left, the represented hemifield is the RIGHT
        # hemifield.**

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing_secondary",
                              "binocular_vision",
                              "form_and_object_perception",
                              "spatial_localization",
                              # NOTE: color_vision is EXCLUDED (V4,
                              # BA 19 territory; BA 18 feeds it via
                              # V2 thin stripes but does not
                              # perform it).
                              # NOTE: motion_perception is EXCLUDED
                              # (V5/MT+, BA 19 territory; BA 18
                              # feeds it via V2 thick stripes and
                              # V3 but does not perform it).
                              # NOTE: visual_attention is EXCLUDED
                              # as a primary domain (BA 18 is a
                              # *target* of attention, not a
                              # *generator*).
                              # NOTE: visual_word_processing is
                              # EXCLUDED (BA 18 is the *second
                              # stage* of the left reading
                              # pathway, not the reading
                              # operation).
                              # NOTE: local_featural_processing is
                              # a *left-specific emphasis* within
                              # `form_and_object_perception`, not
                              # a separate domain.
                              # NOTE: global_visual_processing is
                              # a *right-specific emphasis* within
                              # `form_and_object_perception`, not
                              # a separate domain.
                              # NOTE: face_processing is EXCLUDED
                              # (right-lateralized; not
                              # instantiated on the left BA 18).
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
                              "spatial_localization":
                                  "v3_motion_boundary_and_depth_"
                                  "from_motion_right_hemifield_"
                                  "weaker_than_right",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "left_ba18_right_quadrantic_visual_"
                              "field_defect",
                              "left_ba18_quadrantic_defect_with_"
                              "reading_field_shift",
                              "left_ba18_visual_form_processing_"
                              "deficit",
                              "left_ba18_color_and_motion_"
                              "indirect_deficits",
                              "left_ba18_hemianopic_alexia_right",
                              "left_ba18_alexia_without_agraphia_"
                              "left_occipital_plus_splenium",
                              "left_ba18_migraine_visual_aura",
                              "left_ba18_occipital_epilepsy_"
                              "visual_auras",
                              "left_ba18_posterior_cortical_"
                              "atrophy",
                              "left_ba18_pres_visual_symptoms",
                              "left_ba18_occipital_infarct_pca_"
                              "territory",
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
computation that references BA 18 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this package's own
structural fields.** BA 18 is a leaf BA package whose structural
neighbours (BA 17, BA 19, the cuneus, the calcarine sulcus, the lateral
occipital gyrus, and the V2 / V3 functional areas under ``..cortex``)
all exist as packages in the tree. The **lingual gyrus** is a forward
reference in ``..gyri``, but the BA 18 package does not depend on it —
the lingual gyrus is a surface landmark for the lower-bank
representation, and BA 18's own structural fields resolve fully.

**The two open questions are**:

1. **The V3A / V3B assignment.** V3A and V3B are sub-areas of the V3
   complex that some parcellations assign to BA 18 and some to BA 19.
   **BA 18's `V_AREA_CORRELATE` field records only V2 and V3** — the
   unambiguous correlates. V3A and V3B are recorded as **forward
   references** in the parent registry and must be resolved to either
   BA 18 or BA 19 in the same commit as their creation. **The
   resolution must be hemisphere-invariant** — the same assignment on
   both sides.

2. **The lingual gyrus placement.** As with the left BA 17 sibling,
   the lingual gyrus (the lower bank of the calcarine sulcus) is not
   yet a package. Its placement (parent level, like the cuneus, or
   under ``..gyri``) is an open question that must be resolved in
   the same commit as its creation.

**Both caveats are byte-identical to the right sibling's** — they are
properties of the occipital lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 18 is **not architectonically homogeneous** — V2 and V3 have
different cytoarchitectures (V2 is more dysgranular, V3 is more
intermediate). The **natural split** is into its two V areas:

    brodmann_area_18/
        __init__.py
        v2_component/
            __init__.py
        v3_component/
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``FUNCTIONAL_DOMAINS``, ``DOMAIN_EMPHASIS``,
     ``CONNECTIVITY``, and ``CLINICAL_ANCHORS`` at the parent level
     as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**The V2 / V3 split is a legitimate architectonic subdivision** (unlike
BA 17's foveal / peripheral split, which is functional). V2 and V3 are
**genuinely different architectonic entities** — they have different
CO-stripe organizations, different layer IV prominence, and different
functional domains. If the split is performed, the **parent remains
the canonical answer to "what is BA 18?"** and the components refine
*which V area* is which.

**The V2 / V3 split must be mirrored by a corresponding split of the
``..cortex/v2`` and ``..cortex/v3`` packages** — the BA 18 → V2 / V3
correspondence means that any BA 18 split must be matched by a V2 / V3
split in ``..cortex``, in the same commit, in both hemispheres.

**V3A and V3B must be resolved before the V2 / V3 split.** If V3A and
V3B are assigned to BA 18, they become additional components of BA 18;
if they are assigned to BA 19, they become components of BA 19. **The
assignment decision must be made in the same commit as the V2 / V3
split**, and the ``FORWARD_REFERENCE_V_AREAS`` tuple in the parent
registry must be updated accordingly.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_18``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "brodmann_area_18"
        LOBE                         "occipital"
        BRODMANN_NUMBER              18
        ALTERNATE_NAMES              ("secondary_visual_cortex",
                                     "extrastriate_cortex_belt",
                                     "V2_V3_complex")
        ARCHITECTONIC_SIGNATURES     (three signatures —
                                     CO stripes, dysgranular,
                                     variable BA 18 / BA 19
                                     border)
        V_AREA_CORRELATE             ("v2", "v3") — two
                                     elements, not one
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same V2 mirror-flip of
                                     V1 across the V1/V2 border,
                                     V3 mirror-flip of V2 across
                                     the V2/V3 border
        Bounding / overlapping territories
        BA-to-neighbour adjacency
        CONNECTIVITY                 same bundle names (the
                                     three-stripe V2 → V4 / MT/V5
                                     / IT pattern is hemisphere-
                                     invariant)
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — left BA 18 processes
                               the RIGHT hemifield; right BA 18
                               processes the LEFT hemifield. The
                               map's *structure* (V2 mirror-flip,
                               V3 mirror-flip) is the same; the
                               *label* is flipped.
        FUNCTIONAL_DOMAINS     **identical set on both sides** —
                               both carry the same four domains
                               (primary_visual_processing_
                               secondary, binocular_vision,
                               form_and_object_perception,
                               spatial_localization). The
                               *emphasis* differs, not the set.
        DOMAIN_EMPHASIS        left: form_and_object_perception
                               is "local_featural_form_processing_
                               right_hemifield_ventral_stream_to_
                               left_vwfa"; spatial_localization
                               is "v3_motion_boundary_and_depth_
                               from_motion_right_hemifield_weaker_
                               than_right".
                               right: form_and_object_perception
                               is "global_holistic_form_
                               processing_left_hemifield_ventral_
                               stream_to_right_ffa"; spatial_
                               localization is "v3_motion_
                               boundary_and_depth_from_motion_
                               left_hemifield_dominant"; the
                               right BA 18 also emphasizes
                               `global_visual_processing` as
                               part of the `form_and_object_
                               perception` domain.
        CONNECTIVITY           same bundle names; left: the
                               V2 → V4 pathway feeds the left
                               VWFA via the LOC; the
                               V2 / V3 → MT/V5 pathway is
                               present but weaker than the
                               right's.
                               right: the V2 → V4 pathway feeds
                               the right FFA via the LOC; the
                               V2 / V3 → MT/V5 pathway is the
                               dominant dorsal-stream
                               contribution.
        CLINICAL_ANCHORS       left: eleven anchors (right
                               quadrantic visual field defect,
                               quadrantic defect with reading
                               field shift, visual form
                               processing deficit (local),
                               color / motion indirect
                               deficits, hemianopic alexia
                               (right), alexia without agraphia
                               (left V1 + splenium if lesion
                               extends), migraine aura,
                               occipital epilepsy, PCA, PRES,
                               occipital infarct).
                               right: eleven anchors (left
                               quadrantic visual field defect,
                               left-hemifield neglect
                               contribution, global-level form
                               processing deficit, prosopagnosia
                               contribution, color / motion
                               indirect deficits, left
                               hemianopic alexia (milder),
                               right ventral attention
                               network target, migraine aura,
                               occipital epilepsy, PCA, PRES,
                               occipital infarct).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same BA 18, the same V2 + V3
correlates, the same three-stripe V2 organization, and the same
mirror-flip retinotopy — but the *represented hemifield* is **flipped**.

**The local-vs-global emphasis is the second sharpest entry.** Both
hemispheres carry `form_and_object_perception` as a functional
domain, but the **left** BA 18's emphasis is on **local / featural**
form processing (the left hemisphere's documented advantage), and the
**right** BA 18's emphasis is on **global / holistic** form
processing (the right hemisphere's documented advantage). **Neither
emphasis is a separate domain** — the domain set is identical — but
the emphasis determines which **clinical deficit pattern** a lesion
produces.

**The V2 / V3 correlates, the three-stripe V2 organization, and the
mirror-flip retinotopy are byte-identical on both sides.** They are
properties of the extrastriate cortex itself, not of the hemisphere.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, PRES, and occipital infarct — are **documented
identically in both siblings** and must not be allowed to drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_18".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] BRODMANN_NUMBER is 18.
[ ] ALTERNATE_NAMES includes "secondary_visual_cortex",
    "extrastriate_cortex_belt", and "V2_V3_complex".
[ ] ARCHITECTONIC_SIGNATURES includes the **three** signatures:
    CO stripes in V2, dysgranular extrastriate cortex, and the
    **variable BA 18 / BA 19 border** (the only BA border in the
    occipital lobe that is not architectonically unambiguous).
[ ] V_AREA_CORRELATE is **exactly** ``("v2", "v3")`` — a
    **two-element tuple**, not one. This is a **structural
    departure from BA 17** and must be preserved.
[ ] V3A and V3B are **NOT** included in V_AREA_CORRELATE — they
    are scheme-dependent forward references.
[ ] NAMING_COLLISION_WITH is an empty tuple — BA 18 has no naming
    collision.
[ ] RETINOTOPIC_MAP documents the **mirror-flip** structure:
    - V2 upper field on the **upper** bank (opposite V1's lower-
      bank upper field)
    - V2 lower field on the **lower** bank (opposite V1's upper-
      bank lower field)
    - V1/V2 border = vertical meridian
    - V2/V3 border = horizontal meridian
    - V3 is a second mirror-flip of V2
    - **represented hemifield = RIGHT hemifield on the left side**
[ ] FUNCTIONAL_DOMAINS contains **four** domains:
    - primary_visual_processing_secondary
    - binocular_vision
    - form_and_object_perception
    - spatial_localization
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision (V4, BA 19 —
    BA 18 feeds it via V2 thin stripes but does not perform it).
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (V5/MT+,
    BA 19 — BA 18 feeds it via V2 thick stripes and V3 but does
    not perform it).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a primary
    domain (BA 18 is a *target*, not a *generator*).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing (BA 18
    is the *second stage* of the left reading pathway, not the
    operation).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing (right-
    lateralized; not instantiated on the left BA 18).
[ ] **`local_featural_processing` and `global_visual_processing`
    are NOT separate domains** — they are **hemisphere-specific
    emphases within `form_and_object_perception`**. The domain
    set is identical on both hemispheres.
[ ] DOMAIN_EMPHASIS captures the **left-side emphasis**:
    - primary_visual_processing_secondary → second_cortical_stage_
      of_vision_right_hemifield_border_ownership_texture_
      filling_in
    - binocular_vision → stereoscopic_depth_from_disparity_right_
      hemifield_fusion
    - form_and_object_perception → **local_featural_form_
      processing_right_hemifield_ventral_stream_to_left_vwfa**
    - spatial_localization → v3_motion_boundary_and_depth_from_
      motion_right_hemifield_weaker_than_right
[ ] CONNECTIVITY documents:
    - V1 → BA 18 principal cortical afferent (the obligate relay)
    - Direct LGN → V2 koniocellular projection (weaker,
      modulatory)
    - Pulvinar afferent (stronger to V2 / V3 than to V1)
    - **Three-stripe V2 output pattern**:
        - thin stripes → V4 (color / form, ventral stream)
        - thick stripes → MT/V5 (motion, dorsal stream)
        - pale stripes → inferotemporal cortex (object form)
    - **V2 → V3 intra-BA 18 relay**
    - **BA 18 → BA 19** projection (second step of the occipital
      hierarchy)
    - Callosal connections to the right BA 18 at the vertical
      meridian (V1/V2 border)
    - Attentional feedback from the left FEF, left DLPFC, and
      left IPS (weaker than the right's)
[ ] CLINICAL_ANCHORS contains the eleven left-specific anchors:
    - left_ba18_right_quadrantic_visual_field_defect
    - left_ba18_quadrantic_defect_with_reading_field_shift
    - left_ba18_visual_form_processing_deficit
    - left_ba18_color_and_motion_indirect_deficits
    - left_ba18_hemianopic_alexia_right
    - left_ba18_alexia_without_agraphia_left_occipital_plus_
      splenium
    - left_ba18_migraine_visual_aura
    - left_ba18_occipital_epilepsy_visual_auras
    - left_ba18_posterior_cortical_atrophy
    - left_ba18_pres_visual_symptoms
    - left_ba18_occipital_infarct_pca_territory
[ ] The **right quadrantic visual field defect** is documented as
    the primary left BA 18 anchor — the canonical partial field
    defect that distinguishes BA 18 lesions from BA 17's complete
    hemianopia.
[ ] The **local / featural form processing deficit** is documented
    as the left-lateralized form anchor — the mirror of the right's
    global / holistic deficit.
[ ] **Hemianopic alexia (right)** is documented as a left-
    lateralized reading deficit from the partial right field
    defect, and it is described as **milder than a complete left
    BA 17 hemianopia**.
[ ] The **color / motion indirect deficits** are documented as
    *processing* impairments (BA 18 feeds V4 and MT/V5), not
    *perceptual absences* (which would require direct V4 or
    MT/V5 lesions).
[ ] **Migraine aura and occipital epilepsy** are documented with
    the **V2 / V3 contributions** to the aura's complexity
    (fortification spectra, formed objects) beyond V1's
    elementary features.
[ ] The **retinotopic mirror-flip** is documented explicitly, with
    the upper-field / lower-field bank assignments **reversed**
    relative to V1.
[ ] The **three-stripe V2 output pattern** is documented as the
    anatomical basis for the V2 → three-stream output (ventral,
    dorsal, IT).
[ ] The **BA 18 / BA 19 border variability** is documented as a
    caveat — the border is more variable than the V1/V2 border,
    and the retinotopic horizontal meridian is the more reliable
    landmark when available.
[ ] No forward-declaration caveat is needed for the BA-side
    neighbours. The lingual gyrus forward-reference caveat is
    byte-identical to the right sibling's.
[ ] No SUBDIVISIONS promotion is performed while the V2 / V3 split
    has not been matched by a corresponding split of the
    ``..cortex/v2`` and ``..cortex/v3`` packages.
[ ] **V3A and V3B are not yet resolved** — the assignment to BA 18
    or BA 19 is an open question that must be resolved before the
    V2 / V3 split, and the resolution must be hemisphere-invariant.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    V_AREA_CORRELATE, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, FUNCTIONAL_DOMAINS set, forward-declaration caveat
    text) match the right sibling; the RETINOTOPIC_MAP's
    represented hemifield, DOMAIN_EMPHASIS (local vs global
    emphasis), CONNECTIVITY emphasis, and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left BA 18
    carries "right_hemifield" in its DOMAIN_EMPHASIS entries and
    RETINOTOPIC_MAP; the right BA 18 carries "left_hemifield."
[ ] **The local-vs-global emphasis is verified**: the left BA 18
    carries "local_featural" in its `form_and_object_perception`
    emphasis; the right BA 18 carries "global_holistic."
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — both carry the same four domains. The
    `local_featural_processing` and `global_visual_processing`
    domains are **not** in the set; they are emphases within
    `form_and_object_perception`.
[ ] Any downstream code querying "what does the left BA 18 see?"
    must receive "the RIGHT visual hemifield."
[ ] Any downstream code querying "what is BA 18?" must receive
    "V2 + V3 / secondary visual cortex / extrastriate cortex
    belt" — the two-element correspondence is enforced.
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** BA 18 → V4 → LOC → VWFA chain —
    the left BA 18 is the **second stage**, not the reading
    operation.
[ ] Any downstream code assigning the right face pathway must
    route through the **right** BA 18 → V4 → LOC → FFA chain.
[ ] Any downstream code assigning local / featural processing
    must weight the left BA 18 more heavily; any downstream code
    assigning global / holistic processing must weight the right
    BA 18 more heavily. Averaging left and right would erase the
    lateralized emphasis.
"""