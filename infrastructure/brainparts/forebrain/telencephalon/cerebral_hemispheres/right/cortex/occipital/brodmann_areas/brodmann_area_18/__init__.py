"""
Brodmann Area 18 (Secondary Visual Cortex) — Right Hemisphere
==============================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── brodmann_areas
                                    └── brodmann_area_18   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the right
hemisphere's **BA 18** — the **secondary visual cortex**, the
extrastriate territory that **surrounds BA 17 (V1)** on the medial and
lateral surfaces of the occipital lobe. Unlike BA 17, whose 1:1 V-area
correspondence makes it the cleanest leaf in the cortex tree, **BA 18
spans two** modern functional areas — **V2** and **V3** — and its
`V_AREA_CORRELATE` field is a **two-element tuple**, not a single-element
one.

Parent: ``..brodmann_areas`` (right occipital BA registry) — sibling to
BA 17 and BA 19.

This package is the **structural mirror** of
``../../left/cortex/occipital/brodmann_areas/brodmann_area_18``. The BA
number, the two V-area correlates (V2 + V3), the architectonic
signatures, the retinotopic mirror-flip, and the V1/V2 and V2/V3
borders are identical on both sides; the **functional emphasis** and
**clinical significance** diverge — on the right, BA 18 is weighted
toward the **global / holistic** aspect of visual processing, its V2
and V3 outputs feed the **right ventral stream** through V4 toward the
right fusiform face area (FFA), and the right BA 18 lesions produce
**left quadrantic visual field defects** with a distinct
**prosopagnosia contribution** and **left hemispatial neglect
contribution**.

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
**unambiguous** V2 + V3 assignment. **On the right, V3A is the more
strongly engaged side** for motion-in-depth and visuospatial attention —
but this is a BA 19 property (V3A is not a BA 18 property), so the
right-sided emphasis is not carried in this package's domain set.

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

**Right-hemisphere specificity**: the right BA 18 processes the **LEFT**
visual hemifield of both eyes (contralateral processing). The
**left homonymous hemianopia or quadrantic defect** that follows a
right BA 18 lesion is the canonical right-lateralized visual-field
deficit for this territory. **On the right, BA 18's V2 and V3 outputs
feed the right ventral stream through V4 toward the right FFA**, and
the right BA 18 is therefore the **second stage of the right face-
recognition pathway** after BA 17. The right BA 18 is also weighted
toward the **global / holistic aspect** of visual processing (Navon's
global-precedence asymmetry), in contrast to the left BA 18's
**local / featural** emphasis. **On the right, the V2 and V3 → MT/V5
pathway is the dominant dorsal-stream contribution**, and the right
BA 18 is part of the **right ventral attention network** substrate
that reorients to salient visual events.

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
            **On the right, V2's outputs feed the right ventral
            stream via V4 and the right dorsal stream via MT/V5**,
            and the right's contribution is weighted toward the
            **global / holistic** form processing.
        V3 — tertiary visual cortex (part of BA 18)
            The second extrastriate area, immediately surrounding
            V2. Processes dynamic form, motion boundaries, coherent
            motion, and depth from motion. **On the right, V3's
            outputs feed the right dorsal stream via MT/V5 and the
            right ventral stream via V4. The right V3 is more
            strongly engaged during visuospatial attention and
            motion-in-space processing than the left.**
        V3A / V3B — forward references
            Sub-areas of the V3 complex, assigned to BA 18 in some
            parcellations and to BA 19 in others. **Not yet
            packages under ``..cortex``** — recorded as forward
            references. **On the right, V3A is the more strongly
            engaged side** for motion-in-depth and visuospatial
            attention.
        cuneus — upper-bank territory
            The cuneus's lower margin carries the **V2 and V3
            upper-bank representations of the lower** contralateral
            visual field. **On the right, the lower LEFT field.**
            (Note the mirror-flip: **V1's upper field is on the
            lower bank, but V2 and V3's upper fields are on the
            upper bank** — the exact opposite physical location
            for the same field label.)
        lingual gyrus — lower-bank territory
            The lingual gyrus carries the **V2 and V3 lower-bank
            representations of the upper** contralateral visual
            field. **On the right, the upper LEFT field.**
        lateral occipital gyrus — lateral territory
            The lateral occipital gyrus is overlapped by BA 18 on
            its lateral aspect (V3 on the lateral surface). **On
            the right, the lateral V3 representation is part of the
            right dorsal stream's dominant contribution to left-
            hemifield motion processing** — the right V3 is more
            strongly engaged for visuospatial motion than the left
            V3.
        calcarine sulcus — landmark
            The calcarine sulcus is the **fundus** of the V1
            representation; BA 18 lies on both banks of the
            calcarine sulcus and extends beyond it caudally and
            laterally. The calcarine sulcus is **not** the primary
            landmark for BA 18 (it is the landmark for BA 17), but
            it is the reference point for the **V1/V2 border**
            which is the caudomedial boundary of BA 18.
        right ventral attention network — target
            **Right-emphasized overlay.** The right BA 18 is part
            of the substrate of the **right ventral attention
            network** (right TPJ + right FEF), which reorients to
            salient visual events. The left BA 18 is also a target
            of the left ventral attention network, but the right
            network is the dominant reorienting substrate in the
            human brain, and the right BA 18's participation is
            part of that dominance.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours and the V2 / V3 / cuneus / lingual-gyrus /
lateral-occipital-gyrus / calcarine overlays are the same on both
sides. What differs is the **visual hemifield** — the right BA 18
processes the LEFT hemifield, and the cuneus / lingual gyrus
representations carry the upper / lower LEFT field on the right. The
**global-vs-local processing asymmetry** and the **right ventral
attention network overlay** are the two right-emphasized functional
axes of divergence.

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
                                           V4. **On the right, the
                                           V3A and MT/V5 ends are
                                           more strongly engaged**,
                                           so the BA 18 → BA 19
                                           dorsal-stream projection
                                           is the dominant one on
                                           the right.
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
                                           field (**lower LEFT field
                                           on the right**)
    lingual gyrus (medial-surface          carries the **V2 / V3
    gyrus; forward reference in ..gyri)    lower-bank** representation
                                           of the **upper** visual
                                           field (**upper LEFT field
                                           on the right**)
    lateral occipital gyrus                carries the **lateral V3**
                                           representation; **on the
                                           right, this is the more
                                           strongly engaged dorsal-
                                           stream substrate** for
                                           left-hemifield motion
                                           processing
    calcarine sulcus                       the **fundus** of the V1
                                           representation; the
                                           V1/V2 border (the
                                           caudomedial boundary of
                                           BA 18) is adjacent to
                                           the calcarine sulcus

**This field is byte-identical to the left sibling's** at the level of
BA-numbered neighbours and sulcal/gyral landmarks. The adjacency
relationships are topological, not lateralized. The field labels
(LEFT vs RIGHT) in the cuneus and lingual gyrus entries are updated
for the right hemisphere, and the right's **dominant dorsal-stream
emphasis** is noted in the BA 19 and lateral-occipital-gyrus entries.

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
available. **This caveat is byte-identical to the left sibling's.**

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 18 (= V2 + V3) participates in **four** canonical occipital
functional domains. The set is **identical on both hemispheres**
(unlike BA 17's four-vs-three divergence); the **emphasis** differs.
On the right, the emphasis is as follows:

    primary_visual_processing (secondary)          (right emphasis — PRIMARY)
        **This is BA 18's first defining contribution.** The
        **second** cortical stage of vision, after BA 17 (V1). V2
        adds **border ownership, texture, illusory contours,
        surface filling-in, and stereoscopic depth** to the
        low-level features extracted by V1. V3 adds **dynamic
        form, motion boundaries, and depth from motion**. On the
        right, BA 18 processes the **LEFT visual hemifield**.

    binocular_vision                               (right emphasis — PRIMARY)
        V2's binocular disparity neurons — which are **more
        numerous and more selective than in V1** — support
        **fine stereoscopic depth perception** and **binocular
        fusion**. V3 adds depth from motion. On the right,
        binocular vision in V2 / V3 combines the right-eye and
        left-eye inputs to the **LEFT visual hemifield**.

    form_and_object_perception                     (right emphasis — SECONDARY)
        **This is BA 18's most right-lateralized contribution.**
        V2's **thin stripes** and V3's **dynamic-form**
        representations contribute to the **early stages of form
        and object processing** that continue in V4 and the LOC.
        **On the right, the form-and-object contribution is
        weighted toward the GLOBAL / HOLISTIC aspect** — the right
        hemisphere's documented advantage in global processing
        (Navon's global-precedence asymmetry is the mirror of the
        left's local-precedence). The right's **global / holistic
        processing** is captured here as the right-specific
        emphasis within `form_and_object_perception`; it is not a
        separate domain. **On the right, the V2 / V3 → V4 → LOC
        pathway terminates in the right FFA** (the face area),
        and the right BA 18 is the **second stage** of the right
        face-recognition pathway.

    spatial_localization                           (right emphasis — SECONDARY)
        V3's **motion-boundary** and **depth-from-motion**
        representations contribute to the **early stages of
        spatial localization** that continue in V3A and MT/V5.
        **On the right, the spatial-localization contribution is
        stronger than on the left** — the right V3 is more
        strongly engaged during visuospatial attention and
        motion-in-space processing, and the right's contribution
        is to the **dorsal stream** (motion, spatial attention)
        as well as the ventral stream. **The right V3A and right
        MT/V5 are core nodes of the right-lateralized dorsal
        attention network.**

**Right-specific caveat on `primary_visual_processing` (BA 17's
domain).** The label is shared with BA 17, but the **emphasis**
differs. BA 17's `primary_visual_processing` is the **first**
cortical stage — orientation, contrast, spatial frequency. BA 18's
`primary_visual_processing (secondary)` is the **second** stage —
border ownership, texture, filling-in, motion boundaries. The
parent ``..brodmann_areas`` registers BA 17's and BA 18's
`primary_visual_processing` entries as **distinct emphases**, not
duplicates; downstream code must not conflate them.

**Right-specific caveat on `color_vision`.** BA 18 is **not** the
color-vision area — that is V4, in BA 19. BA 18's **thin stripes**
(V2) and **V3** project **to** V4, but the conscious perception of
color emerges in V4. `color_vision` is **omitted** from the BA 18
`FUNCTIONAL_DOMAINS` tuple; it appears in BA 19 (V4) instead.

**Right-specific caveat on `motion_perception`.** BA 18 is **not** the
motion area — that is V5/MT+, in BA 19. **On the right, V5/MT+ is
the more strongly engaged side**, and the right V3 has strong
motion-boundary sensitivity, but **conscious motion perception**
emerges in MT/V5. `motion_perception` is **omitted** from the BA 18
`FUNCTIONAL_DOMAINS` tuple; it appears in BA 19 (MT/V5) instead.

**Right-specific caveat on `visual_attention`.** BA 18 is a **target**
of top-down attentional modulation from the frontal eye fields (BA 8)
and the dorsolateral prefrontal cortex, and the **right BA 18 is part
of the right ventral attention network substrate** for reorienting to
salient visual events. But BA 18 is **not itself an attentional
control area** — it is a *target*, not a *generator*. `visual_
attention` is **omitted** from the BA 18 `FUNCTIONAL_DOMAINS` tuple as
a primary domain; the right-emphasized attentional target role is
captured in the **right ventral attention network overlay** and in
the `CONNECTIVITY` section, not as a domain.

**Right-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the
**right BA 18 supports as an input stage** but does **not** carry as
primary functional domains. `face_processing` is instantiated in the
right FFA (fed by the right BA 17 → BA 18 → BA 19 → LOC → FFA
pathway); `global_visual_processing` **begins at right BA 18** (V2 /
V3) and is the right-hemisphere's documented advantage. **No single
occipital BA claims `face_processing` or `global_visual_processing`
as a primary contribution** — they are network properties of the
right occipital + right fusiform / right hemisphere pathways. The
right BA 18 package **contributes to** these pathways via its
`form_and_object_perception` and `spatial_localization` domains, but
does not carry the downstream domains themselves. **This is the same
structural relationship as BA 17's: the BA is the input stage, the
domain lives downstream.**

**Right-specific caveat on `visual_word_processing` and `local_
featural_processing`.** These are **left-lateralized** functions that
the right BA 18 does **not** carry. `visual_word_processing` is
instantiated in the left VWFA (fed by the left BA 17 ventral stream);
`local_featural_processing` is a left-hemisphere advantage beginning
at left BA 18. Neither appears in the right BA 18 `FUNCTIONAL_
DOMAINS` tuple.

**Summary**: BA 18 carries **exactly four** functional domains —
`primary_visual_processing (secondary)`, `binocular_vision`,
`form_and_object_perception`, and `spatial_localization`. The first
two are shared with BA 17; the last two are BA 18-specific additions
that reflect V2's and V3's contributions to the ventral and dorsal
streams. **The FUNCTIONAL_DOMAINS set is identical across
hemispheres** — both sides carry the same four domains. **The
emphasis differs**: the left emphasizes local / featural form
processing; the right emphasizes global / holistic form processing and
the dominant dorsal-stream spatial localization. **This is a
weighting-only divergence, not a domain-set divergence** — a
distinction from BA 17, whose right side adds a fourth domain
(`visual_attention_ventral_network_target`).

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), right — via V1 relay
            **BA 18's dominant input is from V1, not directly
            from the LGN.** The LGN → V1 → BA 18 pathway is the
            **obligate relay** for V2's and V3's visual input.
            Direct LGN → V2 projections exist (the **koniocellular
            pathway**) but are weaker and modulatory.
        → pulvinar (secondary, modulatory)
            The pulvinar sends a **stronger modulatory projection
            to V2 and V3 than to V1**, participating in the
            cortico-thalamo-cortical loops that support visual
            attention and visual short-term memory. **On the
            right, the pulvinar → V2 / V3 loop is part of the
            right ventral attention network substrate.**

    cortical afferents
        → BA 17 (V1), right
            **BA 18's principal cortical afferent.** The V1 →
            V2 projection is the first step of the V1 → V2 → V3
            hierarchy, and it carries the low-level features that
            V2 transforms into border ownership, texture, and
            surface representations. **On the right, this input
            carries the LEFT visual hemifield.**
        → V2 → V3 (intra-BA 18)
            V2's outputs project to V3 within BA 18, forming the
            **V2 → V3 relay** that carries the surface and border
            representations forward to the dynamic-form and
            motion-boundary processing.

    cortical efferents
        → V4 (via V2 thin stripes), right
            The **V2 thin stripes** carry the color and form
            signal forward to V4. This is the **ventral stream**
            (the "what" pathway) originating in V2's thin stripes
            and continuing through V4 to the LOC and the right
            FFA. **On the right, the V2 → V4 pathway feeds the
            right face-recognition endpoint.**
        → MT/V5 (via V2 thick stripes and V3), right
            The **V2 thick stripes** and **V3** carry the motion
            and motion-boundary signal forward to MT/V5. This is
            the **dorsal stream** (the "where" pathway)
            originating in V2's thick stripes and V3, continuing
            through MT/V5 to the parietal cortex. **On the right,
            this dorsal-stream pathway is the dominant one** —
            the right V3 and MT/V5 are more strongly engaged
            during visuospatial attention and motion-in-space
            processing than the left's.
        → inferotemporal cortex (via V2 pale stripes), right
            The **V2 pale stripes** carry the object-form signal
            forward to the inferotemporal cortex, contributing to
            the ventral stream's object-recognition hierarchy.
            On the right, this pathway feeds the right FFA (via
            V4 and the LOC) — the face-recognition endpoint.
        → BA 19 (V3A, V4, V5/MT+), right
            V2 and V3 project forward to BA 19's functional areas
            via the three-stripe pattern described above. The
            **BA 18 → BA 19** projection is the second step of
            the occipital hierarchy. **On the right, the V3A and
            MT/V5 ends are more strongly engaged**, making the
            right BA 18 → BA 19 dorsal-stream projection the
            dominant one.

    callosal connections
        → left BA 18
            The callosal fibers connect the right BA 18 to the
            left BA 18 at the **vertical meridian** (the V1/V2
            border) and across the upper and lower banks of the
            calcarine region. This callosal connection supports
            **the fusion of the two hemifields** at the V2 and V3
            stage, and it is essential for the **continuity of
            visual perception across the vertical midline** at the
            extrastriate level.

    attentional feedback
        → frontal eye fields (BA 8), right
            **Right-emphasized.** The right FEF is the dominant
            node of the right ventral attention network and sends
            strong **top-down and bottom-up attentional gain** to
            right BA 18, modulating the responsiveness of V2 and
            V3 neurons to behaviourally relevant stimuli. The
            right FEF → right BA 18 projection is part of the
            substrate for **stimulus-driven reorienting to
            salient visual events**.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), right
            The DLPFC sends top-down attentional and working-memory
            signals to BA 18, supporting **visual working memory**
            and **visual imagery**.
        → intraparietal sulcus, right
            **Right-emphasized.** The right IPS is a core node of
            the right dorsal attention network and sends strong
            top-down spatial-attention signals to right BA 18,
            supporting **spatial attention** in the LEFT visual
            hemifield. The right IPS → right BA 18 projection is
            part of the substrate for **sustained spatial
            attention**.
        → temporoparietal junction, right
            **Right-emphasized.** The right TPJ is the other core
            node of the right ventral attention network and sends
            reorienting signals to right BA 18 via the right FEF.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the BA 18 → V4 → LOC → right FFA pathway is the **right face-
recognition pathway**, and the right BA 18 is the second stage of it;
(b) the BA 18 → MT/V5 pathway is the **dominant dorsal-stream
contribution** on the right, and the right V3 / MT/V5 are more
strongly engaged during visuospatial attention than the left's;
(c) the right FEF, right IPS, and right TPJ send strong attentional
gain to right BA 18 as part of the **right-lateralized ventral and
dorsal attention networks**.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ba18_left_quadrantic_visual_field_defect
        **This is the right BA 18 anchor par excellence.** Unlike
        BA 17, whose lesions produce a **complete** left homonymous
        hemianopia (because V1 represents the entire contralateral
        hemifield), BA 18's lesions produce **partial** field
        defects — most characteristically a **left quadrantic** or
        **sectoranopic** defect. The classic BA 18-lesion field
        defect is a **left inferior quadrantic** field loss
        (from an upper-bank BA 18 lesion) or a **left superior
        quadrantic** field loss (from a lower-bank BA 18 lesion),
        **often with macular sparing** because the foveal
        representation at the occipital pole is fed by the
        dual-blood-supply V1 territory rather than BA 18 proper.

    right_ba18_left_hemifield_neglect_contribution
        **Right-emphasized.** Right BA 18 lesions contribute to
        **left hemispatial neglect** when the lesion extends
        beyond BA 18 into the right parietal and right frontal
        territories. **Isolated right BA 18 lesions do not
        produce neglect** — the patient has a left quadrantic
        field defect but can attend to the left field cognitively
        — but the right BA 18 is part of the **right ventral
        attention network** substrate that, when damaged together
        with the right TPJ and right FEF, contributes to the
        neglect syndrome. **The right BA 18 is therefore the
        right-lateralized attentional substrate that the left
        BA 18 is not**, and its damage is more consequential for
        hemispatial attention than isolated left BA 18 damage.
        **This anchor has no symmetric counterpart on the left.**

    right_ba18_global_holistic_form_processing_deficit
        **On the right, BA 18's V2 / V3 contribution to form and
        object processing is weighted toward the global / holistic
        aspect.** Right BA 18 lesions can produce **global-level
        form processing deficits** — the patient may still
        perceive local features but cannot integrate them into a
        coherent global shape (Navon's global-precedence asymmetry
        is the framework). **This is a right-weighted anchor**;
        the left BA 18 lesion produces the complementary
        **local-level form processing deficit**.

    right_ba18_contribution_to_prosopagnosia
        **Right-emphasized.** Right BA 18 is the **second stage**
        of the right ventral stream that feeds the right FFA, and
        **right occipito-temporal lesions** that involve the right
        FFA or its input pathway produce **prosopagnosia** —
        impaired face recognition. **Isolated right BA 18 lesions
        do not produce prosopagnosia** — the right FFA is spared
        — but the right BA 18 is the **occipital input stage** of
        the right-lateralized face pathway, and its lesions can
        contribute to face-processing deficits when the downstream
        pathway is also affected. **Prosopagnosia is the
        canonical right-lateralized visual-recognition deficit**,
        and right BA 18 is its second cortical stage. **This
        anchor has no symmetric counterpart on the left** — the
        left BA 18 feeds the left VWFA (reading), not a
        prosopagnosia pathway.

    right_ba18_color_and_motion_indirect_deficits
        BA 18's thin and thick stripes project to V4 and MT/V5,
        respectively. **Right BA 18 lesions can produce indirect
        color or motion processing deficits** — the V4 and MT/V5
        areas themselves are intact, but their input from BA 18
        is degraded. **On the right, the motion deficit is more
        likely to be clinically apparent than on the left**,
        because the right MT/V5 is the dominant motion area. The
        color deficit in a BA 18 lesion is typically **milder**
        than in a V4 lesion, and the motion deficit in a BA 18
        lesion is typically **milder** than in a V5/MT+ lesion.
        **Isolated achromatopsia (V4) or akinetopsia (V5/MT+)
        from a BA 18 lesion would be unexpected.**

    right_ba18_hemianopic_alexia_left
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **left homonymous hemianopia or
        quadrantic defect** (from a right BA 18 lesion extending
        into BA 17) — is a recognized clinical entity, but
        **weaker than the left-side equivalent**. The reading
        deficit in hemianopic alexia arises because the patient
        must make large **leftward saccades** to compensate for
        the missing left hemifield, and the **left-hemisphere
        reading network** cannot function efficiently without the
        full right-hemifield input. **A right BA 18 lesion
        produces a milder hemianopic alexia than a left BA 18
        lesion** — the right-side lesion is in the non-dominant
        hemisphere for reading, and the reading network itself
        (left VWFA, left angular gyrus) is intact and its
        contralateral-field input (right hemifield) is preserved.

    right_ba18_ventral_attention_network_target
        **Right-emphasized.** Right BA 18 is part of the substrate
        of the **right ventral attention network** (right TPJ +
        right FEF), which reorients to salient visual events.
        **Isolated right BA 18 lesions do not produce reorienting
        deficits** in the same way that right TPJ lesions do, but
        right BA 18 is part of the network's substrate and its
        participation is part of the right-lateralized reorienting
        substrate that the left BA 18 does not carry at the same
        weighting.

    right_ba18_migraine_visual_aura
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
        is contralateral (left field on the right side).

    right_ba18_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** —
        elementary visual hallucinations (flashing lights, colored
        shapes, geometric patterns) in the **contralateral visual
        field** — can arise from **BA 17 OR BA 18**. **BA 18
        auras** are typically **more complex** than BA 17 auras —
        the patient may see **formed objects, recognizable
        scenes, or specific colors** in addition to elementary
        shapes. **Right BA 18 auras** project to the **left
        visual field** and can be preceded or accompanied by
        **visual field defects** that persist after the seizure.

    right_ba18_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **BA 17 AND BA 18 bilaterally** in
        later stages, but early PCA affects the **dorsal and
        ventral association cortices** (V3A, V4, V5/MT+, and the
        LOC) more than BA 18 proper. **Right BA 18** is part of
        the substrate of the **progressive dorsal-stream
        dysfunction** that produces **progressive prosopagnosia
        and visuospatial deficits** in the early stages of PCA.
        **On the right, PCA presents with the visuospatial /
        prosopagnosic syndrome**; on the left, with the
        progressive reading deficits (the "visual variant" of
        progressive aphasia).

    right_ba18_pres_visual_symptoms
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

    right_ba18_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct**
        involving **BA 17 AND BA 18** produces a **left homonymous
        hemianopia** (from BA 17) **plus** a **left quadrantic
        or sectoranopic defect** (from BA 18) and, in some cases,
        **cortical blindness in the affected field** with
        **macular sparing**. **Isolated right PCA infarcts do
        not produce alexia without agraphia** — that syndrome is
        left-lateralized — because the right splenium does not
        connect to a right reading network. **The right PCA
        infarct's clinical signature is therefore the left
        hemianopia plus left quadrantic defect, with or without
        macular sparing.**

    the_hemisphere_invariant_syndromes
        The remaining clinical anchors — **migraine aura,
        occipital epilepsy, PCA, PRES, and occipital infarct** —
        are **hemisphere-invariant** in their mechanism, though
        the side of the field label differs. They are documented
        identically in both siblings, and any deviation from the
        left sibling's documentation of these anchors is a bug.

These anchors are **right-hemisphere-specific** in two senses:
(a) the right BA 18 processes the **LEFT visual hemifield**, so right
BA 18 lesions produce **left-sided** visual deficits; (b) the right
BA 18 is the **second stage of the right face pathway**, so right
BA 18 lesions can contribute to face-processing deficits
(prosopagnosia) when the downstream occipito-temporal pathway is
also involved, and the right BA 18 is part of the **right-lateralized
ventral attention network** substrate that contributes to left
hemispatial neglect. **The global / holistic emphasis** is a third
right-specific feature — the right BA 18 is weighted toward global
processing, and right BA 18 lesions produce global-level form
deficits that have no symmetric counterpart on the left. **The right
BA 18 does not produce alexia without agraphia** — that syndrome is
left-lateralized — and the right's reading contribution is limited
to the milder left-side hemianopic alexia (from the partial left
field defect). The left sibling's docstring carries the corresponding
left-sided anchors (right homonymous hemianopia or quadrantic defect,
local / featural form processing deficit, right hemianopic alexia
(milder), alexia without agraphia if the lesion extends to the
splenium).

**The `migraine_aura`, `occipital_epilepsy`, `PCA`, `PRES`, and
`occipital_infarct` anchors are hemisphere-invariant** — they appear
on both sides and are documented identically in both siblings, with
the side-appropriate field label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The right occipital BA registry. This package's parent, source
    of the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 18 (which on
    the right is ``("primary_visual_processing_secondary",
    "binocular_vision",
    "form_and_object_perception_global_holistic",
    "spatial_localization_v3_dominant")``), and enforcer of the
    **two-element V_AREA_CORRELATE (V2 + V3)** — a departure from
    BA 17's single-element correlate.

..brodmann_area_17_primary_visual
    **Caudal neighbour** via the V1/V2 border. The BA 17 → BA 18
    projection is the first step of the V1 → V2 → V3 → V4 / MT+
    hierarchy. **The vertical meridian of the visual field is
    represented at the V1/V2 border**, and the callosal connections
    between the right and left hemispheres meet at this border.
    **The retinotopic mirror-flip** between V1 and V2 is the
    defining feature of the V1/V2 border, and it is why BA 18's
    upper-field / lower-field bank assignments are **reversed**
    relative to BA 17's.

..brodmann_area_19
    **Rostral neighbour** via the BA 18 / BA 19 border. BA 18's
    V2 and V3 outputs reach BA 19's V4 (via the thin stripes)
    and V5/MT+ (via the thick stripes), completing the
    V1 → V2 → V3 → V4 / MT+ hierarchy. **On the right, the V3A
    and MT/V5 ends are more strongly engaged**, making the right
    BA 18 → BA 19 dorsal-stream projection the dominant one.

...cortex.v2
    The **functional V2 package under ``..cortex``** — the direct
    counterpart of the V2 half of this BA package. Where this
    package describes the **cytoarchitectonic** BA 18, the V2
    package describes the **functional-retinotopic** V2.

...cortex.v3
    The **functional V3 package under ``..cortex``** — the direct
    counterpart of the V3 half of this BA package. **V3 is one of
    the two V areas that BA 18 spans** (the other is V2). **On
    the right, the V3 motion-boundary and depth-from-motion
    contributions are the more strongly engaged ones**, and the
    right V3 is the second stage of the right dorsal-stream
    substrate for left-hemifield motion processing.

...cortex.v4
    V2's **thin stripes** project forward to V4, and V4 is where
    the conscious perception of color and the ventral stream's
    form-and-object hierarchy begin. **On the right, the
    V2 → V4 pathway feeds the right FFA** (via the LOC), and the
    right BA 18 is the **second stage** of the right face-
    recognition pathway.

...cortex.primary_visual_cortex  (V1)
    **Not a direct target of BA 18** — V1 is the **source** of
    BA 18's input. But V1 and V2 / V3 together form the **core
    occipital hierarchy**, and the parent ``..brodmann_areas``'s
    crosswalk records the V1 → V2 → V3 sequence.

...cuneus
    The medial-surface gyral landmark. The cuneus's lower margin
    (the upper bank of the calcarine region) carries the **V2 /
    V3 upper-bank representations of the lower** contralateral
    visual field. **On the right, the lower LEFT field.** Note the
    mirror-flip: **V1's upper field is on the LOWER bank, but V2
    and V3's upper fields are on the UPPER bank.**

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus carries the **V2 / V3 lower-bank**
    representations of the upper contralateral visual field.
    **On the right, the upper LEFT field.** The same mirror-flip
    applies.

...gyri.lateral_occipital_gyrus
    The lateral-surface gyral territory. BA 18's **lateral V3**
    representation overlays the lateral occipital gyrus, and
    **on the right, the lateral V3 representation is part of the
    dominant dorsal-stream contribution to left-hemifield motion
    processing** (the right V3 is more strongly engaged than the
    left).

...sulci.calcarine_sulcus
    The **fundus of the V1 representation**; the V1/V2 border (the
    caudomedial boundary of BA 18) is adjacent to the calcarine
    sulcus.

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
    LOC) into the temporal lobe. **On the right, the ventral
    stream terminates in the right FFA** (the face area), and
    the right BA 18 is the **second stage** of this pathway.
    **Right occipito-temporal lesions produce prosopagnosia** —
    the canonical right-lateralized visual-recognition deficit.
    The temporal package must declare the right BA 18 as a
    source of its visual input via the ventral stream, and must
    note the **right-lateralized FFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from BA 18 (via V3 and MT/V5)
    into the parietal lobe. **On the right, the dorsal stream is
    more strongly engaged during visuospatial attention**, and
    the right parietal lobe is a core node of the right-
    lateralized dorsal attention network. The parietal package
    must declare the right BA 18 as a source of its visual input
    for the dorsal stream, and must note the right-lateralized
    attentional emphasis.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to BA 18. **On the right, the right FEF is the
    dominant node of the ventral attention network**, and right
    frontal lesions contribute to left hemispatial neglect. The
    frontal package must declare the right BA 18 as a target of
    its attentional projections, and must note the right-
    lateralized attentional emphasis.

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
    its LGN input **indirectly via V1**.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **stronger modulatory projection to V2
    and V3 than to V1**, participating in the cortico-thalamo-
    cortical loops that support visual attention and visual
    short-term memory. **On the right, the pulvinar → V2 / V3
    loop is part of the right ventral attention network
    substrate.**

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream continues from BA 18 (via V4 and the LOC)
    to the perirhinal, entorhinal, and parahippocampal cortices.
    **The right BA 18 is the second stage** of the occipito-
    temporal-hippocampal pathway that supports visual object
    recognition and visual memory. **On the right, the
    parahippocampal place area (PPA) and the retrosplenial
    complex receive visual input supporting scene and spatial
    memory**, which are more strongly right-lateralized.

../../left/cortex/occipital/brodmann_areas/brodmann_area_18
    The left-hemisphere homologue. Structural fields (BA number,
    V-area correlates V2 + V3, architectonic signatures, V1/V2
    and V2/V3 borders, retinotopic mirror-flip, three-stripe
    V2 organization, cuneus / lingual-gyrus / lateral-occipital-
    gyrus relationships, V_AREA_CORRELATE, ARCHITECTONIC_
    SIGNATURES, forward-declaration caveat text) MUST be
    byte-identical. Functional emphasis and clinical significance
    diverge — the right BA 18 processes the **LEFT** visual
    hemifield, is weighted toward the **global / holistic**
    aspect of form processing, and its V2 / V3 outputs feed the
    right ventral stream toward the right FFA (for faces) rather
    than the left VWFA (for reading).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_18"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    BRODMANN_NUMBER     = 18
    ALTERNATE_NAMES     = ("secondary_visual_cortex",
                           "extrastriate_cortex_belt",
                           "V2_V3_complex")
        # **Byte-identical to the left sibling's.** BA 18's
        # multi-V-area identity is a property of the territory,
        # not of the hemisphere.

    ARCHITECTONIC_SIGNATURES = (
        "cytochrome_oxidase_stripes_in_V2",
        "dysgranular_extrastriate_cortex",
        "variable_BA18_BA19_border",
    )
        # **Byte-identical to the left sibling's.**

    V_AREA_CORRELATE    = ("v2", "v3")
        # **Two elements, not one** — the departure from BA 17's
        # single-element correlate. **Byte-identical to the left
        # sibling's.** V3A and V3B are NOT included — they are
        # scheme-dependent forward references.

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** Byte-identical to the left
        # sibling's.

    RETINOTOPIC_MAP     = "mirror_flip_of_V1_across_V1_V2_border"
        # The map's *structure* is identical to the left's —
        # V2 mirror-flip of V1, V3 mirror-flip of V2. **On the
        # right, the represented hemifield is the LEFT
        # hemifield.**

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing_secondary",
                              "binocular_vision",
                              "form_and_object_perception",
                              "spatial_localization",
                              # **Identical set to the left
                              # sibling's** — the four domains are
                              # the same on both hemispheres.
                              # The emphasis differs, not the set.
                              # NOTE: color_vision is EXCLUDED (V4,
                              # BA 19 territory).
                              # NOTE: motion_perception is EXCLUDED
                              # (V5/MT+, BA 19 territory).
                              # NOTE: visual_attention is EXCLUDED
                              # as a primary domain (BA 18 is a
                              # *target*, not a *generator*).
                              # NOTE: visual_word_processing and
                              # local_featural_processing are
                              # EXCLUDED (left-lateralized; not
                              # instantiated on the right BA 18).
                              # NOTE: face_processing and
                              # global_visual_processing are
                              # EXCLUDED as *BA 18 domains*
                              # (the right BA 18 is the *input
                              # stage*, not the operation).
                              # NOTE: global_visual_processing is
                              # a *right-specific emphasis* within
                              # `form_and_object_perception`, not
                              # a separate domain.
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
                              "spatial_localization":
                                  "v3_motion_boundary_and_depth_"
                                  "from_motion_left_hemifield_"
                                  "dominant",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_ba18_left_quadrantic_visual_"
                              "field_defect",
                              "right_ba18_left_hemifield_neglect_"
                              "contribution",
                              "right_ba18_global_holistic_form_"
                              "processing_deficit",
                              "right_ba18_contribution_to_"
                              "prosopagnosia",
                              "right_ba18_color_and_motion_"
                              "indirect_deficits",
                              "right_ba18_hemianopic_alexia_left",
                              "right_ba18_ventral_attention_"
                              "network_target",
                              "right_ba18_migraine_visual_aura",
                              "right_ba18_occipital_epilepsy_"
                              "visual_auras",
                              "right_ba18_posterior_cortical_"
                              "atrophy",
                              "right_ba18_pres_visual_symptoms",
                              "right_ba18_occipital_infarct_pca_"
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
reference in ``..gyri``, but the BA 18 package does not depend on it.

**The two open questions are**:

1. **The V3A / V3B assignment.** V3A and V3B are sub-areas of the V3
   complex that some parcellations assign to BA 18 and some to BA 19.
   **BA 18's `V_AREA_CORRELATE` field records only V2 and V3** — the
   unambiguous correlates. V3A and V3B are recorded as **forward
   references** in the parent registry and must be resolved to either
   BA 18 or BA 19 in the same commit as their creation. **The
   resolution must be hemisphere-invariant** — the same assignment on
   both sides.

2. **The lingual gyrus placement.** As with the right BA 17 sibling,
   the lingual gyrus (the lower bank of the calcarine sulcus) is not
   yet a package. Its placement (parent level, like the cuneus, or
   under ``..gyri``) is an open question that must be resolved in
   the same commit as its creation.

**Both caveats are byte-identical to the left sibling's** — they are
properties of the occipital lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 18 is **not architectonically homogeneous** — V2 and V3 have
different cytoarchitectures. The **natural split** is into its two V
areas:

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
  4. Mirror the promotion on the left side in the same commit.

**The V2 / V3 split is a legitimate architectonic subdivision.**
V2 and V3 have different CO-stripe organizations, different layer IV
prominence, and different functional domains. If the split is
performed, the **parent remains the canonical answer to "what is
BA 18?"** and the components refine *which V area* is which.

**The V2 / V3 split must be mirrored by a corresponding split of the
``..cortex/v2`` and ``..cortex/v3`` packages** — the BA 18 → V2 / V3
correspondence means that any BA 18 split must be matched by a V2 / V3
split in ``..cortex``, in the same commit, in both hemispheres.

**On the right, the V3 component is the dominant dorsal-stream
contributor.** If BA 18 is split, the right V3 component must carry
the right-emphasized motion-boundary, spatial-localization, and
dorsal-attention contributions, and the right V2 component must
carry the right-emphasized global / holistic form-processing
contribution. **The left V3 and V2 components must carry the
complementary local / featural and weaker-dorsal-stream emphases.**

**V3A and V3B must be resolved before the V2 / V3 split.** If V3A and
V3B are assigned to BA 18, they become additional components of BA 18;
if they are assigned to BA 19, they become components of BA 19. **On
the right, V3A is the more strongly engaged side** for motion-in-depth
and visuospatial attention, so any resolution that places V3A in BA 19
must be reflected in the right BA 19 package, not in this BA 18
package.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../brodmann_area_18``:

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
        FUNCTIONAL_DOMAINS set       the same four domains
                                     (primary_visual_processing_
                                     secondary, binocular_vision,
                                     form_and_object_perception,
                                     spatial_localization)
        Bounding / overlapping territories
        BA-to-neighbour adjacency (with the LEFT / RIGHT
                                     field labels updated for the
                                     cuneus and lingual gyrus)
        CONNECTIVITY                 same bundle names (the
                                     three-stripe V2 → V4 / MT/V5
                                     / IT pattern is hemisphere-
                                     invariant)
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — right BA 18 processes
                               the LEFT hemifield; left BA 18
                               processes the RIGHT hemifield.
                               The map's *structure* (V2 mirror-
                               flip, V3 mirror-flip) is the same;
                               the *label* is flipped.
        DOMAIN_EMPHASIS        right: form_and_object_perception is
                               "global_holistic_form_processing_
                               left_hemifield_ventral_stream_to_
                               right_ffa"; spatial_localization is
                               "v3_motion_boundary_and_depth_from_
                               motion_left_hemifield_dominant".
                               left: form_and_object_perception is
                               "local_featural_form_processing_
                               right_hemifield_ventral_stream_to_
                               left_vwfa"; spatial_localization is
                               "v3_motion_boundary_and_depth_from_
                               motion_right_hemifield_weaker_than_
                               right".
        CONNECTIVITY           same bundle names; right: the
                               V2 → V4 pathway feeds the right
                               FFA via the LOC; the
                               V2 / V3 → MT/V5 pathway is the
                               dominant dorsal-stream contribution;
                               the right FEF, right IPS, and right
                               TPJ send strong attentional gain to
                               right BA 18.
                               left: the V2 → V4 pathway feeds the
                               left VWFA via the LOC; the
                               V2 / V3 → MT/V5 pathway is present
                               but weaker than the right's; the
                               left FEF, left IPS, and left TPJ
                               send attentional gain to left BA 18
                               (weaker reorienting contribution).
        CLINICAL_ANCHORS       right: twelve anchors (left
                               quadrantic visual field defect,
                               **left hemifield neglect
                               contribution**, **global / holistic
                               form processing deficit**,
                               **prosopagnosia contribution**,
                               color / motion indirect deficits,
                               hemianopic alexia (left, milder),
                               **right ventral attention network
                               target**, migraine aura, occipital
                               epilepsy, PCA, PRES, occipital
                               infarct).
                               left: eleven anchors (right
                               quadrantic visual field defect,
                               quadrantic defect with reading
                               field shift, visual form processing
                               deficit (local), color / motion
                               indirect deficits, hemianopic alexia
                               (right), alexia without agraphia
                               (left V1 + splenium if lesion
                               extends), migraine aura, occipital
                               epilepsy, PCA, PRES, occipital
                               infarct).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same BA 18, the same V2 + V3
correlates, the same three-stripe V2 organization, and the same
mirror-flip retinotopy — but the *represented hemifield* is
**flipped**.

**The local-vs-global emphasis is the second sharpest entry.** Both
hemispheres carry `form_and_object_perception` as a functional
domain, and the **FUNCTIONAL_DOMAINS set is identical** — but the
**left** BA 18's emphasis is on **local / featural** form processing,
and the **right** BA 18's emphasis is on **global / holistic** form
processing. **Neither emphasis is a separate domain** — the domain
set is identical — but the emphasis determines which **clinical
deficit pattern** a lesion produces.

**The right-specific clinical anchors are the third sharpest entry.**
The right BA 18 carries **four anchors** that the left does not carry
at the same weighting: `right_ba18_left_hemifield_neglect_
contribution`, `right_ba18_global_holistic_form_processing_deficit`,
`right_ba18_contribution_to_prosopagnosia`, and
`right_ba18_ventral_attention_network_target`. The left BA 18's
`left_ba18_alexia_without_agraphia_left_occipital_plus_splenium`
anchor is **left-only**. The checklist verifies these asymmetries.

**The V2 / V3 correlates, the three-stripe V2 organization, the
mirror-flip retinotopy, and the FUNCTIONAL_DOMAINS set are
byte-identical on both sides.** They are properties of the
extrastriate cortex itself, not of the hemisphere.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, PRES, and occipital infarct — are **documented
identically in both siblings** and must not be allowed to drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_18" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] BRODMANN_NUMBER is 18.
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's.
[ ] ARCHITECTONIC_SIGNATURES is byte-identical to the left
    sibling's (CO stripes, dysgranular, variable BA 18 / BA 19
    border).
[ ] V_AREA_CORRELATE is **exactly** ``("v2", "v3")`` —
    byte-identical to the left sibling's.
[ ] V3A and V3B are **NOT** included in V_AREA_CORRELATE — they
    are scheme-dependent forward references. **On the right, V3A
    is the more strongly engaged side** for motion-in-depth and
    visuospatial attention.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP documents the **mirror-flip** structure with
    the **LEFT hemifield label**:
    - V2 upper field on the **upper** bank
    - V2 lower field on the **lower** bank
    - V1/V2 border = vertical meridian
    - V2/V3 border = horizontal meridian
    - V3 is a second mirror-flip of V2
    - **represented hemifield = LEFT hemifield on the right side**
[ ] FUNCTIONAL_DOMAINS contains **four** domains, **identical set
    to the left sibling's**:
    - primary_visual_processing_secondary
    - binocular_vision
    - form_and_object_perception
    - spatial_localization
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical
    across hemispheres** — both carry the same four domains.
    There is **no right-only fifth domain** (unlike BA 17's
    `visual_attention_ventral_network_target`). **The right
    BA 18's attentional target role is captured in the
    CONNECTIVITY section and in the `right_ba18_ventral_
    attention_network_target` clinical anchor**, not as a
    fifth functional domain.
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision (V4, BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (V5/MT+,
    BA 19 — even though the right MT/V5 is the more strongly
    engaged side).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a primary
    domain.
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing and
    local_featural_processing (left-lateralized).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing as **BA 18 domains** — the right BA 18 is
    the *input stage* of the right face pathway and the
    *beginning* of the right global-processing advantage, but
    the domains live downstream.
[ ] **`global_visual_processing` is a right-specific emphasis
    within `form_and_object_perception`**, not a separate domain.
[ ] **`local_featural_processing` is a left-specific emphasis
    within `form_and_object_perception`**, not a separate domain.
    The left sibling carries the `local_featural` emphasis; this
    package carries the `global_holistic` emphasis.
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis**:
    - primary_visual_processing_secondary → second_cortical_stage_
      of_vision_left_hemifield_border_ownership_texture_filling_in
    - binocular_vision → stereoscopic_depth_from_disparity_left_
      hemifield_fusion
    - form_and_object_perception → **global_holistic_form_
      processing_left_hemifield_ventral_stream_to_right_ffa**
    - spatial_localization → v3_motion_boundary_and_depth_from_
      motion_left_hemifield_dominant
[ ] CONNECTIVITY documents:
    - V1 → BA 18 principal cortical afferent (the obligate relay,
      carrying the LEFT hemifield)
    - Direct LGN → V2 koniocellular projection (weaker,
      modulatory)
    - Pulvinar afferent (stronger to V2 / V3 than to V1; part of
      the right ventral attention network substrate)
    - **Three-stripe V2 output pattern** (thin → V4, thick →
      MT/V5, pale → IT)
    - **V2 → V3 intra-BA 18 relay**
    - **BA 18 → BA 19** projection (with the right's dominant
      dorsal-stream emphasis on V3A and MT/V5)
    - **V2 → V4 → LOC → right FFA pathway** (the right face-
      recognition input)
    - **V2 / V3 → MT/V5 pathway** (the dominant dorsal-stream
      contribution on the right)
    - Callosal connections to the left BA 18 at the vertical
      meridian (V1/V2 border)
    - Attentional feedback from the right FEF, right DLPFC,
      right IPS, and right TPJ (the right-lateralized ventral
      and dorsal attention networks)
[ ] CLINICAL_ANCHORS contains the twelve right-specific anchors:
    - right_ba18_left_quadrantic_visual_field_defect
    - **right_ba18_left_hemifield_neglect_contribution**
    - **right_ba18_global_holistic_form_processing_deficit**
    - **right_ba18_contribution_to_prosopagnosia**
    - right_ba18_color_and_motion_indirect_deficits
    - **right_ba18_hemianopic_alexia_left**
    - **right_ba18_ventral_attention_network_target**
    - right_ba18_migraine_visual_aura
    - right_ba18_occipital_epilepsy_visual_auras
    - right_ba18_posterior_cortical_atrophy
    - right_ba18_pres_visual_symptoms
    - right_ba18_occipital_infarct_pca_territory
[ ] The **left quadrantic visual field defect** is documented as
    the primary right BA 18 anchor.
[ ] **Left hemifield neglect contribution** is documented as a
    right-emphasized anchor — **isolated right BA 18 lesions do
    not produce neglect**, but right BA 18 is part of the right
    ventral attention network substrate that contributes to left
    hemispatial neglect when the lesion extends to the right TPJ
    and right FEF.
[ ] The **global / holistic form processing deficit** is
    documented as the right-lateralized form anchor — the mirror
    of the left's local / featural deficit.
[ ] The **prosopagnosia contribution** is documented as a
    right-emphasized anchor — **isolated right BA 18 lesions do
    not produce prosopagnosia**, but the right BA 18 is the
    second stage of the right face pathway, and right occipito-
    temporal lesions that involve the right FFA or its input
    pathway produce prosopagnosia.
[ ] **Hemianopic alexia (left)** is documented as a right-side
    anchor that is **milder** than the left-side equivalent —
    the partial left field defect impairs reading by removing
    the left-hemifield input to the **intact left reading
    network**, but the reading network itself is preserved, and
    the deficit is milder than after a left BA 18 or BA 17
    lesion. **The right BA 18 does NOT produce alexia without
    agraphia** — that syndrome is left-only.
[ ] The **right ventral attention network target** is documented
    as the right-specific attentional substrate.
[ ] The **color / motion indirect deficits** are documented as
    *processing* impairments (BA 18 feeds V4 and MT/V5), not
    *perceptual absences*. **On the right, the motion deficit is
    more likely to be clinically apparent** because the right
    MT/V5 is the dominant motion area.
[ ] **Migraine aura and occipital epilepsy** are documented with
    the **V2 / V3 contributions** (fortification spectra, formed
    objects) beyond V1's elementary features, byte-identically
    to the left sibling's treatment.
[ ] The **retinotopic mirror-flip** is documented explicitly, with
    the upper-field / lower-field bank assignments **reversed**
    relative to V1, byte-identically to the left sibling's.
[ ] The **three-stripe V2 output pattern** is documented as the
    anatomical basis for the V2 → three-stream output.
[ ] The **BA 18 / BA 19 border variability** is documented as a
    caveat, byte-identically to the left sibling's.
[ ] No forward-declaration caveat is needed for the BA-side
    neighbours. The lingual gyrus forward-reference caveat is
    byte-identical to the left sibling's.
[ ] No SUBDIVISIONS promotion is performed while the V2 / V3 split
    has not been matched by a corresponding split of the
    ``..cortex/v2`` and ``..cortex/v3`` packages.
[ ] **V3A and V3B are not yet resolved** — the assignment to BA 18
    or BA 19 is an open question that must be resolved before the
    V2 / V3 split, and the resolution must be hemisphere-invariant.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURES,
    V_AREA_CORRELATE, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, **FUNCTIONAL_DOMAINS set**, forward-declaration
    caveat text) match the left sibling; the RETINOTOPIC_MAP's
    represented hemifield, DOMAIN_EMPHASIS (global vs local
    emphasis), CONNECTIVITY emphasis, and CLINICAL_ANCHORS
    deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    BA 18 carries "left_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP; the left BA 18 carries "right_hemifield."
[ ] **The local-vs-global emphasis is verified**: the right
    BA 18 carries "global_holistic" in its `form_and_object_
    perception` emphasis; the left BA 18 carries
    "local_featural."
[ ] **The right-only clinical anchors are verified**:
    `right_ba18_left_hemifield_neglect_contribution`,
    `right_ba18_global_holistic_form_processing_deficit`,
    `right_ba18_contribution_to_prosopagnosia`, and
    `right_ba18_ventral_attention_network_target` are present on
    the right and absent on the left. The left-only
    `left_ba18_alexia_without_agraphia_left_occipital_plus_
    splenium` anchor is absent on the right.
[ ] Any downstream code querying "what does the right BA 18
    see?" must receive "the LEFT visual hemifield."
[ ] Any downstream code querying "what is BA 18?" must receive
    "V2 + V3 / secondary visual cortex / extrastriate cortex
    belt" — the two-element correspondence is enforced.
[ ] Any downstream code assigning the right face pathway must
    route through the **right** BA 18 → V4 → LOC → FFA chain.
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** BA 18 → V4 → LOC → VWFA chain.
[ ] Any downstream code assigning global / holistic processing
    must weight the right BA 18 more heavily; any downstream
    code assigning local / featural processing must weight the
    left BA 18 more heavily.
[ ] Any downstream code assigning left hemispatial neglect must
    note that **right BA 18 is a contributor**, not a sole
    cause — the lesion must extend to the right TPJ and right
    FEF for the full neglect syndrome.
"""