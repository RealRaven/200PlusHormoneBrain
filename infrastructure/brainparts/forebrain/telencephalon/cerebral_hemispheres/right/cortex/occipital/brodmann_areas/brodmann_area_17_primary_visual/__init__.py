"""
Brodmann Area 17 (Primary Visual Cortex / Striate Cortex) — Right Hemisphere
=============================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── brodmann_areas
                                    └── brodmann_area_17_primary_visual   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the right
hemisphere's **BA 17** — the **primary visual cortex (V1)**, also
called the **striate cortex** because of the architectonically visible
**stria of Gennari**. It is the **first and tightest** BA↔V
correspondence in the human cortex: **BA 17 is V1**, one-to-one, with
no residual. It is also the **first area Brodmann ever delineated**
(1909) — the stria of Gennari made it visible to the naked eye, and BA
17 became the model for the entire Brodmann scheme.

Parent: ``..brodmann_areas`` (right occipital BA registry) — sibling to
BA 18 and BA 19.

This package is the **structural mirror** of
``../../left/cortex/occipital/brodmann_areas/brodmann_area_17_primary_visual``.
The BA number, the V-area correlate (V1), the architectonic signature
(stria of Gennari), the calcarine-sulcus surface landmark, and the
retinotopic map are identical on both sides; the **functional
emphasis** and **clinical significance** diverge — on the right, BA 17
processes the **LEFT** visual hemifield, and its ventral-stream output
feeds the right fusiform face area (FFA) via V2/V3/V4/LOC, supporting
the right-lateralized face-recognition pathway.

**This package is the only BA package in the cortex tree whose V-area
correlate is a current package with the same territory.** BA 17 ↔ V1
is a 1:1 correspondence, and ``..cortex/primary_visual_cortex`` is the
functional counterpart of this package. The two packages describe the
**same cortical territory** from two angles — cytoarchitectonic (BA
17) and functional-retinotopic (V1) — and the parent
``..brodmann_areas``'s ``BA_TO_V_CROSSWALK`` and
``V_TO_BA_CROSSWALK`` registers the mapping. Downstream code should
treat BA 17 and V1 as **interchangeable identifiers for the same
thing** and query either package for the same set of functional
domains.

--------------------------------------------------------------------------------
WHAT BA 17 IS
--------------------------------------------------------------------------------

BA 17 occupies the **banks of the calcarine sulcus** — the **upper
bank** (the lower margin of the **cuneus**) and the **lower bank** (the
upper margin of the **lingual gyrus**). It extends from the **occipital
pole** (where the fovea is represented) rostrally along the calcarine
sulcus to the **anterior limit of the striate cortex**, where the
calcarine sulcus meets the parieto-occipital sulcus. The two banks
converge at the occipital pole and diverge caudo-rostrally, forming the
characteristic **wedge shape** of V1 in midsagittal section.

The **architectonic signature** of BA 17 is the **stria of Gennari** —
a band of myelinated axons running through layer IV of the striate
cortex. The stria is **visible to the naked eye** on a gross specimen
and is the reason the occipital cortex can be parcellated without
microscopy. This is why **BA 17 was Brodmann's first area** (1909), and
why the **V1/V2 border (BA 17 / BA 18 border) is architectonically
unambiguous** in a way that no other BA boundary in the cortex is.

**The 1:1 BA 17 ↔ V1 correspondence** is the tightest in the entire
cortex. Unlike BA 18 (which spans V2 + V3) or BA 19 (which spans V3A +
V4 + V5/MT+), BA 17 **is** V1 — the cytoarchitectonic boundary (the
stria of Gennari) and the functional boundary (the V1/V2 retinotopic
border) **coincide**. This is why BA 17 is the **only** occipital BA
package that does not need a `FUNCTIONAL_CORRELATES` field with
multiple entries; its correlate is exactly ``("primary_visual_cortex",)``.

**The retinotopic organization** of BA 17 is the most precise in the
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
        sulcus. The **central 10° of vision** occupies roughly **half**
        of the total V1 surface area; the peripheral visual field is
        represented at the **anterior calcarine banks**, near the
        junction with the parieto-occipital sulcus.

    Upper visual field → lower bank of the calcarine sulcus
        The **lingual gyrus** (the lower bank of the calcarine
        sulcus) represents the **upper** visual field of the
        **contralateral** hemifield. **On the right, the lingual
        gyrus represents the upper LEFT visual field.**

    Lower visual field → upper bank of the calcarine sulcus
        The **cuneus** (the upper bank of the calcarine sulcus)
        represents the **lower** visual field of the **contralateral**
        hemifield. **On the right, the cuneus represents the lower
        LEFT visual field.**

    Vertical meridian → V1/V2 border
        The vertical meridian of the visual field is represented at
        the **V1/V2 border** (the BA 17 / BA 18 border), which lies
        **caudomedially** on the banks of the calcarine sulcus. The
        callosal connections between the left and right V1 meet at
        this border, in the BA 18 territory.

    Horizontal meridian → base of the calcarine sulcus
        The horizontal meridian is represented at the **fundus**
        (deepest part) of the calcarine sulcus.

**Right-hemisphere specificity**: the right BA 17 processes the
**LEFT** visual hemifield of both eyes (contralateral processing). The
**left homonymous hemianopia** that follows a right V1 lesion is the
canonical right-lateralized visual-field deficit. On the right, BA 17
is also the **input stage of the ventral stream that feeds the right
FFA** — the face-recognition pathway begins in the right V1 and
terminates in the right fusiform gyrus; this is why right V1 lesions
can contribute to face-processing deficits when the downstream
occipito-temporal pathway is also involved (see the clinical section).
**The right V1 is also a target of the right ventral attention
network** (with the right temporoparietal junction and right frontal
eye fields) that reorients to salient visual events — a
right-lateralized attentional role that the left V1 does not carry at
the same weighting.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Architectonic neighbours
        rostrally              BA 18 (V2 + V3) via the V1/V2 border
        caudomedially          BA 18 (upper-bank continuation)
        laterally              the cuneus (medial surface) and the
                               lingual gyrus (medial surface); the
                               lateral surface of BA 17 is only
                               visible at the occipital pole
        ventrally              the lingual gyrus
        dorsally               the cuneus

    Functional overlays
        primary_visual_cortex (V1) — 1:1
            BA 17 **is** V1. The functional-retinotopic parent
            ``..cortex/primary_visual_cortex`` is the other angle on
            the same territory. Downstream code should treat BA 17
            and V1 as interchangeable identifiers for the same
            thing.
        cuneus — upper-bank V1
            The cuneus (upper bank of the calcarine sulcus) carries
            the dorsal V1 representation of the **lower** contralateral
            visual field. **On the right, the lower LEFT field.**
        lingual gyrus — lower-bank V1
            The lingual gyrus (lower bank of the calcarine sulcus)
            carries the ventral V1 representation of the **upper**
            contralateral visual field. **On the right, the upper
            LEFT field.** (Note: the lingual gyrus is a **forward
            reference** in ``..gyri`` — it is not yet a package.)
        calcarine sulcus — defining surface landmark
            The calcarine sulcus is the **defining sulcus** of BA 17
            and the surface landmark for V1's representation. The
            ``..sulci/calcarine_sulcus`` package declares BA 17 as
            its primary functional overlay.
        right ventral attention network — target
            **Right-emphasized overlay.** The right V1 is a
            target of the right ventral attention network
            (right TPJ + right FEF), which reorients to salient
            visual events. The left V1 is also a target of the
            left hemisphere's ventral attention network, but the
            right network is the dominant reorienting substrate.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours and the cuneus / lingual-gyrus / calcarine
overlays are the same on both sides. What differs is the **visual
hemifield** — the right BA 17 processes the LEFT hemifield, and the
cuneus / lingual gyrus representations carry the upper / lower LEFT
field on the right. The **right ventral attention network target**
overlay is a right-emphasized functional overlay that the left BA 17
package declares at lower weighting.

--------------------------------------------------------------------------------
BA-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    BA 18 (V2 + V3)                        **rostral neighbour** via the
                                           V1/V2 border; the vertical
                                           meridian of the visual
                                           field is represented at
                                           this border. The
                                           BA 17 → BA 18 projection is
                                           the first step of the
                                           V1 → V2 → V3 → V4 / MT+
                                           hierarchy.
    BA 19 (V3A + V4 + V5/MT+)              distant rostral / lateral
                                           neighbour; no direct
                                           adjacency (BA 18
                                           intervenes)
    cuneus (medial-surface gyrus)          dorsal bank of the calcarine
                                           sulcus; the upper-bank V1
                                           representation of the
                                           **lower** visual field
                                           (**lower LEFT field on the
                                           right**)
    lingual gyrus (medial-surface          ventral bank of the calcarine
    gyrus; forward reference in ..gyri)    sulcus; the lower-bank V1
                                           representation of the
                                           **upper** visual field
                                           (**upper LEFT field on the
                                           right**)
    calcarine sulcus (defining sulcus)     the fundus of the sulcus
                                           represents the horizontal
                                           meridian; the banks
                                           represent the upper /
                                           lower fields

**This field is byte-identical to the left sibling's** at the level of
BA-numbered neighbours and sulcal/gyral landmarks. The adjacency
relationships are topological, not lateralized. The field labels
(LEFT vs RIGHT) in the cuneus and lingual gyrus entries are updated
for the right hemisphere.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 17 (= V1) participates in **four** canonical occipital functional
domains on the right — the same three as the left (`primary_visual_
processing`, `retinotopic_organization`, `binocular_vision`) plus one
**right-emphasized** attentional target role
(`visual_attention_ventral_network_target`). The emphasis is as
follows:

    primary_visual_processing                      (right emphasis — PRIMARY)
        **This is BA 17's defining contribution.** The first
        cortical stage of vision: orientation selectivity,
        ocular-dominance columns, spatial-frequency tuning, contrast
        sensitivity, edge detection, and retinotopic mapping. On the
        right, BA 17 processes the **LEFT visual hemifield**; left
        homonymous hemianopia follows right V1 lesions.

    retinotopic_organization                       (right emphasis — PRIMARY)
        **This is BA 17's second primary contribution.** The
        topographic mapping of the **LEFT visual hemifield** onto
        the right calcarine banks, with the fovea at the occipital
        pole and the periphery at the anterior calcarine banks. The
        right BA 17's retinotopic map is essentially a mirror image
        of the left BA 17's, with the field label flipped.

    binocular_vision                               (right emphasis — PRIMARY)
        Ocular-dominance columns and their convergence onto
        binocular cells support depth perception, stereopsis, and
        binocular fusion. On the right, binocular vision combines
        the right-eye and left-eye inputs to the **LEFT visual
        hemifield**.

    visual_attention_ventral_network_target        (right emphasis — SECONDARY)
        **Right-emphasized.** The right V1 is a target of the
        right ventral attention network (right TPJ + right FEF),
        which reorients to salient visual events. The right
        network is the dominant reorienting substrate in the
        human brain; the left V1 is also a target of the left
        ventral attention network, but the left network's
        reorienting contribution is weaker. The right V1's
        attentional target role is therefore **more strongly
        engaged on the right** and is captured here as a
        right-emphasized functional domain. **The right V1 is
        not a generator of attention** — it is a target of
        top-down and bottom-up attentional gain.

**Right-specific caveat on `color_vision`.** BA 17 is **not** the
color-vision area — that is V4, in BA 19. BA 17 has some wavelength
selectivity (via the koniocellular pathway from the LGN), but the
**conscious perception of color** emerges in V4 and the ventral
stream. `color_vision` is **omitted** from the BA 17
`FUNCTIONAL_DOMAINS` tuple; it appears in BA 19 (V4) instead.

**Right-specific caveat on `motion_perception`.** BA 17 is **not** the
motion area — that is V5/MT+, in BA 19. **On the right, V5/MT+ is
the more strongly engaged side** for visuospatial attention and
motion-in-space processing, but this is a BA 19 property, not a BA 17
property. BA 17 has some direction selectivity, but **conscious motion
perception** emerges in MT/V5 and the dorsal stream. `motion_
perception` is **omitted** from the BA 17 `FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `form_and_object_perception`.** BA 17
contributes to the **early stages** of form processing (edge
detection, contour integration), but **object recognition** emerges in
V4, the LOC, and the ventral stream. `form_and_object_perception` is
**omitted** from the BA 17 `FUNCTIONAL_DOMAINS` tuple; it appears in
BA 18 and BA 19 instead. **The right BA 19 ventral stream terminates
in the right FFA** — the face-processing endpoint of the right
ventral stream is downstream of BA 17, not in BA 17 itself.

**Right-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the
**right BA 17 supports as an input stage** but does **not** carry as
primary functional domains. `face_processing` is instantiated in the
right FFA (fed by the right BA 17 → BA 18 → BA 19 → LOC → FFA
pathway); `global_visual_processing` is a distributed right-hemisphere
property beginning at right BA 18 (V2 / V3). **No single occipital BA
claims `face_processing` or `global_visual_processing` as a primary
contribution** — they are network properties of the right occipital +
right fusiform / right hemisphere pathways. The right BA 17 package
**contributes to** these pathways without carrying the domains.

**Right-specific caveat on `visual_word_processing` and `local_
featural_processing`.** These are **left-lateralized** functions that
the right BA 17 does **not** carry. `visual_word_processing` is
instantiated in the left VWFA (fed by the left BA 17 ventral stream);
`local_featural_processing` is a left-hemisphere advantage beginning
at left BA 18. Neither appears in the right BA 17 `FUNCTIONAL_
DOMAINS` tuple.

**Summary**: BA 17 carries **exactly four** functional domains on the
right — `primary_visual_processing`, `retinotopic_organization`,
`binocular_vision`, and `visual_attention_ventral_network_target`.
The first three are shared with the left; the fourth is a
right-emphasized attentional target role. **The right BA 17 is
functionally identical to the left BA 17 in its primary domains**
(they are the same BA 17, after all) — the difference is that the
represented hemifield is **LEFT** and the attentional target role is
**right-emphasized**, not the domain set itself.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), right
            **BA 17's primary and dominant thalamic afferent.**
            The right LGN relays the visual signal from the right
            hemiretinas of both eyes (via the optic chiasm and the
            right optic tract). The LGN → V1 projection terminates
            in layer IV of the striate cortex — **layer IV is where
            the stria of Gennari runs**, and the LGN input is
            segregated into ocular-dominance columns that alternate
            between the left-eye and right-eye inputs. This is the
            anatomical substrate of the first cortical stage of
            vision. **On the right, this input carries the LEFT
            visual hemifield.**
        → pulvinar (secondary, modulatory)
            The pulvinar sends a weaker modulatory projection to
            BA 17 (and stronger projections to V2, V4, and MT),
            participating in the cortico-thalamo-cortical loops
            that support visual attention and visual short-term
            memory. **On the right, the pulvinar → V1 loop is part
            of the right ventral attention network substrate.**
        → LGN feedback from layer VI
            BA 17 layer VI projects **back** to the LGN, forming
            the cortico-geniculate feedback loop that modulates
            the thalamic relay. This is a **top-down** modulation
            of the incoming visual signal, not a forward projection.

    cortical efferents
        → BA 18 (V2 and V3), right
            **BA 17's principal cortical target.** The BA 17 →
            BA 18 projection carries the V1 output to V2 (the
            first extrastriate stage) and V3 (via V2). This is the
            first step of the V1 → V2 → V3 → V4 / MT+ hierarchy.
        → BA 19 (via BA 18)
            V1's output reaches V3A, V4, and MT/V5 via the BA 18
            relay, not directly. There are **no direct BA 17 → BA
            19 projections** — the relay through BA 18 is obligate.
        → MT/V5 (via BA 18 / V2, dorsal stream)
            The motion pathway (V1 → V2 → MT/V5) carries the
            low-level motion signal from BA 17 to the motion area.
            **On the right, MT/V5 is more strongly engaged during
            visuospatial attention and motion-in-space processing
            than on the left** — the right dorsal stream's motion
            contribution dominates. On the right, this pathway
            supports **LEFT-hemifield** motion perception.
        → V4 and the LOC (via BA 18 / V2, ventral stream)
            The color / form pathway (V1 → V2 → V4 → LOC) carries
            the low-level form and wavelength signal from BA 17 to
            the color area and the object-recognition complex.
            **On the right, the ventral stream terminates in the
            right FFA** — the face-recognition endpoint. The right
            BA 17 → BA 18 → BA 19 → LOC → FFA pathway supports
            **LEFT-hemifield** face perception.

    callosal connections
        → left BA 17
            The callosal fibers connect the right BA 17 to the
            left BA 17 at the **vertical meridian** (the V1/V2
            border), where the two hemispheres' visual fields meet.
            This callosal connection is essential for the
            **fusion of the two hemifields** and for the
            **continuity of vision across the vertical midline**.
            Interruption of the callosal connections produces a
            **split-field** visual experience (the two hemifields
            become independently experienced, as in split-brain
            patients).

    attentional feedback
        → frontal eye fields (BA 8), right
            **Right-emphasized.** The right FEF is the dominant
            node of the right ventral attention network and sends
            strong **top-down and bottom-up attentional gain** to
            right BA 17, modulating the responsiveness of V1
            neurons to behaviourally relevant stimuli. The right
            FEF → right V1 projection is part of the substrate
            for **stimulus-driven reorienting to salient visual
            events**.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), right
            The DLPFC sends top-down attentional and working-memory
            signals to BA 17, supporting **visual working memory**
            and **visual imagery**.
        → intraparietal sulcus, right
            **Right-emphasized.** The right IPS is a core node of
            the right dorsal attention network and sends strong
            top-down spatial-attention signals to right BA 17,
            supporting **spatial attention** in the LEFT visual
            hemifield. The right IPS → right V1 projection is part
            of the substrate for **sustained spatial attention**.
        → temporoparietal junction, right
            **Right-emphasized.** The right TPJ is the other core
            node of the right ventral attention network and sends
            reorienting signals to right BA 17 via the right FEF.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the right BA 17 → BA 18 → LOC → FFA pathway is the **face-
recognition pathway** that the right hemisphere dominates (not the
left's reading pathway);
(b) the right MT/V5 is more strongly engaged during visuospatial
attention and motion-in-space processing, so the right BA 17 → BA 18
→ MT/V5 pathway carries the dominant dorsal-stream motion
contribution;
(c) the right FEF, right IPS, and right TPJ send strong attentional
gain to right BA 17 as part of the **right-lateralized ventral and
dorsal attention networks**.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_ba17_left_homonymous_hemianopia
        **This is the right BA 17 anchor par excellence.** A lesion
        of the right BA 17 (or the right optic radiation, or the
        right LGN) produces a **left homonymous hemianopia** —
        loss of the left half of the visual field in both eyes.
        The deficit is **homonymous** (both eyes lose the same
        side), **hemianopic** (half the field is lost), and
        **contralateral** (left side from a right lesion). This is
        the single most common and most clinically consequential
        effect of a right V1 lesion.

    left_macular_sparing
        **Macular sparing** — preservation of the central 5–10° of
        the visual field within an otherwise complete homonymous
        hemianopia — is a well-known phenomenon in occipital
        lesions. The mechanism is debated but is generally
        attributed to the **dual blood supply** of the occipital
        pole: the occipital pole (where the fovea is
        over-represented) receives blood from **both the posterior
        cerebral artery (PCA) and the middle cerebral artery
        (MCA)**, whereas the anterior calcarine banks receive blood
        from the PCA alone. **An MCA-PCA watershed infarct spares
        the occipital pole, sparing the macula** — and this is
        why macular sparing is a **hallmark of occipital (PCA)
        lesions**. **On the right, a right V1 lesion produces a
        left hemianopia with left macular sparing.**

    cortical_blindness_bilateral
        **Bilateral BA 17 lesions** produce **cortical blindness** —
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
        blindness** — is a rare complication of bilateral BA 17
        lesions. The patient is cortically blind but **insists that
        they can see**, and may confabulate visual experiences.
        **This anchor is hemisphere-invariant** — it appears on
        both sides with the same clinical significance.

    blindsight
        **Blindsight** — residual visual function (detection,
        localization, and sometimes discrimination of stimuli) in
        the absence of conscious visual perception — is a
        well-documented phenomenon after **V1 lesions**. The
        residual function is mediated by **subcortical visual
        pathways** (the superior colliculus and the pulvinar, which
        project to MT/V5 and to the extrastriate cortex bypassing
        V1). **This anchor is hemisphere-invariant** — it appears
        on both sides with the same clinical significance.

    right_ba17_left_hemifield_neglect_contribution
        **Right-emphasized.** Right V1 lesions contribute to
        **left hemispatial neglect** when the lesion extends
        beyond BA 17 into the right parietal and right frontal
        territories. **Isolated right V1 lesions do not produce
        neglect** — the patient has a left homonymous hemianopia
        but can attend to the left field cognitively — but the
        right V1 is part of the **right ventral attention
        network** substrate that, when damaged together with the
        right TPJ and right FEF, contributes to the neglect
        syndrome. **The right V1 is therefore the
        right-lateralized attentional substrate that the left V1
        is not**, and its damage is more consequential for
        hemispatial attention than isolated left V1 damage.

    right_ba17_contribution_to_prosopagnosia
        **Right-emphasized.** Right V1 is the **input stage** of
        the right ventral stream that feeds the right FFA, and
        **right occipito-temporal lesions** that involve the right
        FFA or its input pathway produce **prosopagnosia** —
        impaired face recognition. **Isolated right BA 17 lesions
        do not produce prosopagnosia** — the right FFA is spared
        — but the right BA 17 is the **occipital input stage** of
        the right-lateralized face pathway, and its lesions can
        contribute to face-processing deficits when the downstream
        pathway is also affected. **Prosopagnosia is the
        canonical right-lateralized visual-recognition deficit**,
        and right BA 17 is its first cortical stage.

    hemianopic_alexia_left
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **left homonymous hemianopia** (from a
        right BA 17 lesion) — is a recognized clinical entity,
        but **weaker than the left-side equivalent**. The
        reading deficit in hemianopic alexia arises because the
        patient must make large **leftward saccades** to
        compensate for the missing left hemifield, and the
        **left-hemisphere reading network** cannot function
        efficiently without the full right-hemifield input. **A
        right V1 lesion produces a left hemianopia that impairs
        reading via the loss of the left-hemifield input to the
        reading network**, but the reading network itself (left
        VWFA, left angular gyrus) is intact and the deficit is
        milder than after a left V1 lesion.

    occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct** involving
        the right BA 17 produces **left homonymous hemianopia**,
        often with **left macular sparing** (as described above).
        The right PCA territory includes the right calcarine
        cortex, the right lingual gyrus, and (via the posterior
        pericallosal artery) the right splenium. **Isolated right
        PCA infarcts do not produce alexia without agraphia** —
        that syndrome is left-lateralized (see left sibling) —
        because the right splenium does not connect to a right
        reading network. **The right PCA infarct's clinical
        signature is therefore the left hemianopia (with or
        without macular sparing), not the reading syndrome.**

    right_ventral_attention_network_target
        **Right-emphasized.** Right V1 is a target of the right
        ventral attention network (right TPJ + right FEF), which
        reorients to salient visual events. **Isolated right V1
        lesions do not produce reorienting deficits**, but right
        V1 is part of the network's substrate and its
        participation is part of the right-lateralized
        reorienting substrate that the left V1 does not carry at
        the same weighting.

    the_hemisphere_invariant_syndromes
        The remaining clinical anchors — **cortical blindness,
        Anton syndrome, blindsight, migraine visual aura,
        occipital epilepsy visual auras, posterior cortical
        atrophy, PRES** — are **hemisphere-invariant** and are
        documented identically in both siblings. They are
        repeated here for completeness and cross-reference, and
        any deviation from the left sibling's documentation of
        these anchors is a bug.

These anchors are **right-hemisphere-specific** in two senses:
(a) the right BA 17 processes the **LEFT visual hemifield**, so right
BA 17 lesions produce **left-sided** visual deficits; (b) the right
BA 17 is the **input stage of the right face pathway**, so right
BA 17 lesions can contribute to face-processing deficits
(prosopagnosia) when the downstream occipito-temporal pathway is
also involved, and the right BA 17 is part of the **right-lateralized
ventral attention network** substrate that contributes to left
hemispatial neglect. **The right BA 17 does not produce alexia without
agraphia** — that syndrome is left-lateralized — and the right V1's
reading contribution is limited to the left-hemifield input to the
intact left reading network. The left sibling's docstring carries the
corresponding left-sided anchors (right homonymous hemianopia,
alexia without agraphia from left V1 + splenium).

**The `macular_sparing`, `blindsight`, `Anton syndrome`, and `cortical
blindness` anchors are hemisphere-invariant** — they appear on both
sides and are documented identically in both siblings. The **field
label of the sparing** differs (left macular sparing from a right
lesion vs right macular sparing from a left lesion), but the
phenomenon and its mechanism are the same.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The right occipital BA registry. This package's parent, source
    of the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 17 (which on
    the right is ``("primary_visual_processing",
    "retinotopic_organization", "binocular_vision",
    "visual_attention_ventral_network_target")``), and enforcer of
    the **V1 ↔ BA 17 1:1 correspondence**.

..brodmann_area_18
    **Rostral neighbour** via the V1/V2 border. The BA 17 → BA 18
    projection is the first step of the V1 → V2 → V3 → V4 / MT+
    hierarchy. **The vertical meridian of the visual field is
    represented at the BA 17 / BA 18 border**, and the callosal
    connections between the left and right V1 meet at this border.

..brodmann_area_19
    Distant rostral / lateral neighbour; no direct adjacency (BA 18
    intervenes). BA 19 contains the color (V4) and motion (V5/MT+)
    areas; **on the right, the BA 19 dorsal-stream end (V3A,
    V5/MT+) is more strongly engaged**, and the BA 19 ventral-
    stream end (V4, LOC) feeds the right FFA.

...cortex.primary_visual_cortex
    **The functional V1 package — the 1:1 counterpart of this BA
    package.** BA 17 and V1 are the **same cortical territory**
    described from two angles. Downstream code should treat them
    as interchangeable identifiers and query either package for
    the same set of functional domains.

...cuneus
    The medial-surface gyral landmark. The cuneus's lower margin
    (the upper bank of the calcarine sulcus) carries the **dorsal
    V1 representation of the lower** contralateral visual field.
    **On the right, the lower LEFT field.** The cuneus package
    cross-references BA 17 as its primary functional overlay.

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus (lower bank of the calcarine sulcus) carries
    the **ventral V1 representation of the upper** contralateral
    visual field. **On the right, the upper LEFT field.** When the
    lingual gyrus becomes a package, it must declare BA 17 as its
    primary functional overlay, and the BA 17 package must
    cross-reference the lingual gyrus.

...sulci.calcarine_sulcus
    **The defining sulcus of BA 17.** The banks of the calcarine
    sulcus carry the V1 representation, and the **fundus** of the
    sulcus represents the **horizontal meridian** of the visual
    field. The calcarine sulcus package declares BA 17 as its
    primary functional overlay.

...sulci.lunate_sulcus
    An inconstant lateral-surface sulcus that, when present, marks
    the **anterior boundary of V1 on the lateral surface**. Not a
    primary landmark for BA 17 proper (which is mostly on the
    medial surface), but a secondary landmark for the lateral
    portion of V1 near the occipital pole.

..cortex.temporal
    The **ventral stream** continues from BA 18 / BA 19 into the
    temporal lobe (inferior temporal cortex, fusiform gyrus, VWFA,
    FFA). **On the right, the ventral stream terminates in the
    right FFA** (the face area), and the right BA 17 is the
    **input stage** of this pathway. The temporal package must
    declare the right BA 17 as the source of its visual input via
    the ventral stream, and must note the **right-lateralized FFA
    specialization**. **Right occipito-temporal lesions produce
    prosopagnosia** — the canonical right-lateralized visual-
    recognition deficit.

..cortex.parietal
    The **dorsal stream** continues from BA 18 / BA 19 into the
    parietal lobe (intraparietal sulcus, area 7). **On the right,
    the dorsal stream is more strongly engaged during visuospatial
    attention**, and the right parietal lobe is a core node of
    the right-lateralized dorsal attention network. The parietal
    package must declare the right BA 17 as the source of its
    visual input for the dorsal stream via the BA 18 / BA 19
    relay, and must note the right-lateralized attentional
    emphasis.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to BA 17 via the BA 18 relay. **On the right, the
    right FEF is the dominant node of the ventral attention
    network**, and right frontal lesions contribute to left
    hemispatial neglect. The frontal package must declare the
    right BA 17 as a target of its attentional projections, and
    must note the right-lateralized attentional emphasis.

..cortex.cingulate  — indirect
    No direct cingulate → BA 17 projection. Recorded here to
    pre-empt a false cross-reference.

..cortex.insular  — indirect
    No direct insular → BA 17 projection. Recorded here to
    pre-empt a false cross-reference.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **The LGN is BA 17's primary and dominant thalamic afferent.**
    The LGN → BA 17 projection terminates in layer IV (where the
    stria of Gennari runs) and is segregated into ocular-dominance
    columns. The thalamus package must declare the LGN as the
    primary visual thalamic relay to the right BA 17.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a secondary, modulatory projection to BA
    17 (stronger to V2, V4, and MT), participating in the
    cortico-thalamo-cortical loops that support visual attention
    and visual short-term memory. **On the right, the pulvinar →
    V1 loop is part of the right ventral attention network
    substrate.**

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream terminates in the perirhinal, entorhinal,
    and parahippocampal cortices. **The right BA 17 is the input
    stage** of the occipito-temporal-hippocampal pathway that
    supports visual object recognition and visual memory. **On
    the right, the parahippocampal place area (PPA) and the
    retrosplenial complex receive visual input supporting scene
    and spatial memory**, which are more strongly right-
    lateralized. The hippocampus package must declare the right
    BA 17 as the source of its visual input via the BA 18 / BA 19
    relay, and must note the right-lateralized scene-memory
    emphasis.

../../left/cortex/occipital/brodmann_areas/brodmann_area_17_primary_visual
    The left-hemisphere homologue. Structural fields (BA number,
    V-area correlate, architectonic signature, calcarine-sulcus
    surface landmark, retinotopic map structure, cuneus /
    lingual-gyrus relationship) MUST be byte-identical. Functional
    emphasis and clinical significance diverge — the right BA 17
    processes the **LEFT** visual hemifield, and right BA 17
    lesions produce **left** homonymous hemianopia with **left**
    macular sparing. The right BA 17 is the input stage of the
    right ventral stream that feeds the right FFA, not the left
    VWFA, and it is part of the right-lateralized ventral
    attention network substrate.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_17_primary_visual"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    BRODMANN_NUMBER     = 17
    ALTERNATE_NAMES     = ("striate_cortex",
                           "primary_visual_cortex_V1",
                           "V1")
        # **Byte-identical to the left sibling's.** The 1:1
        # V-area correspondence is a property of BA 17, not of
        # the hemisphere.

    ARCHITECTONIC_SIGNATURE = "stria_of_gennari"
        # **Byte-identical to the left sibling's.**

    V_AREA_CORRELATE    = ("primary_visual_cortex",)
        # **Exactly one** V area — the tightest BA↔V
        # correspondence in the cortex. **Byte-identical to the
        # left sibling's.**

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** Byte-identical to the left
        # sibling's.

    RETINOTOPIC_MAP     = "fovea_at_pole_contralateral_hemifield"
        # The map's *structure* is identical to the left's —
        # fovea at pole, eccentricity gradient, vertical meridian
        # at V1/V2 border, horizontal meridian at fundus of
        # calcarine sulcus. **On the right, the represented
        # hemifield is the LEFT hemifield.**

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing",
                              "retinotopic_organization",
                              "binocular_vision",
                              "visual_attention_ventral_network_"
                              "target",     # right-emphasized
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
                              # EXCLUDED as a *primary* domain
                              # beyond the target role captured in
                              # `visual_attention_ventral_
                              # network_target` (BA 17 is a
                              # target, not a generator).
                              # NOTE: visual_word_processing is
                              # EXCLUDED (left-lateralized;
                              # the right BA 17 does not feed
                              # the left VWFA).
                              # NOTE: local_featural_processing
                              # is EXCLUDED (left-lateralized).
                              # NOTE: face_processing is
                              # EXCLUDED as a *BA 17 domain*
                              # (it is instantiated at the right
                              # FFA, downstream of BA 17; the
                              # right BA 17 is the *input stage*
                              # of the right face pathway).
                              # NOTE: global_visual_processing is
                              # EXCLUDED as a *BA 17 domain*
                              # (it begins at BA 18).
                          )

    DOMAIN_EMPHASIS     = {   # right-side emphasis per domain
                              "primary_visual_processing":
                                  "first_cortical_stage_of_vision_"
                                  "left_hemifield",
                              "retinotopic_organization":
                                  "fovea_at_pole_left_hemifield_"
                                  "eccentricity_gradient",
                              "binocular_vision":
                                  "ocular_dominance_columns_left_"
                                  "hemifield_stereopsis",
                              "visual_attention_ventral_network_"
                              "target":
                                  "right_ventral_attention_"
                                  "network_target_reorienting_"
                                  "substrate",
                          }

    CONNECTIVITY        = { ... }   # as specified above
    CLINICAL_ANCHORS    = (
                              "right_ba17_left_homonymous_"
                              "hemianopia",
                              "left_macular_sparing",
                              "cortical_blindness_bilateral",
                              "anton_syndrome",
                              "blindsight",
                              "right_ba17_left_hemifield_"
                              "neglect_contribution",
                              "right_ba17_contribution_to_"
                              "prosopagnosia",
                              "hemianopic_alexia_left",
                              "occipital_infarct_pca_"
                              "territory",
                              "right_ventral_attention_"
                              "network_target",
                              "migraine_visual_aura",
                              "occipital_epilepsy_visual_"
                              "auras",
                              "posterior_cortical_atrophy",
                              "pres_visual_symptoms",
                          )

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "AREA_NAME",
        "HEMISPHERE",
        "LOBE",
        "BRODMANN_NUMBER",
        "ALTERNATE_NAMES",
        "ARCHITECTONIC_SIGNATURE",
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
computation that references BA 17 lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this package.** BA 17 is
a leaf BA package whose structural neighbours (BA 18, the cuneus, the
calcarine sulcus, and the V1 functional area under ``..cortex``) all
exist as packages in the tree. The **lingual gyrus** (the lower bank
of the calcarine sulcus) is a forward reference in ``..gyri`` — it is
not yet a package — but the BA 17 package does not depend on it: the
lingual gyrus is a *surface landmark* for the ventral V1
representation, and BA 17's own structural fields (the calcarine
sulcus, the cuneus, and the V1 functional area) resolve fully.

**The one open question** is whether the **lingual gyrus** should be
placed under ``..occipital/gyri/`` alongside the lateral occipital
gyrus, or under a separate medial-surface gyral parent (like the
cuneus's parent-level placement). The cuneus is currently at the
``..occipital`` parent level (not under ``..gyri``) because it is a
**medial-surface landmark for V1**. By symmetry, the lingual gyrus
should probably also be at the parent level (for the same reason),
but the current tree has only the cuneus at that level. When the
lingual gyrus is added, the decision about its placement should be
made in the same commit as its creation, in both hemispheres, and
this caveat should be updated. **The caveat text is byte-identical to
the left sibling's** — the placement question is a property of the
occipital lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 17 is **architectonically homogeneous** — the stria of Gennari runs
continuously across the entire territory — and there is no natural
architectonic subdivision. The **one conceivable split** is the
**foveal (macular) representation vs the peripheral representation**,
since the fovea is enormously over-represented. If a future
parcellation decides to split BA 17 into its foveal and peripheral
components, the promotion takes this form:

    brodmann_area_17_primary_visual/
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
  4. Mirror the promotion on the left side in the same commit.

**The foveal / peripheral split is a FUNCTIONAL subdivision, not an
architectonic one.** The parent remains the canonical answer to "what
is BA 17?"; the components refine *which part of BA 17* supports
which retinal eccentricity.

**The foveal component is the macular-sparing substrate.** The
macular-sparing clinical anchor is directly tied to the foveal
component's **dual blood supply** (PCA + MCA at the occipital pole).
If BA 17 is split, the macular-sparing anchor must remain at the
parent level (as a "foveal component + watershed" claim) and must
also be declared on the foveal component, in both hemispheres.

**No split should be performed while the V1 functional counterpart
under ``..cortex/primary_visual_cortex`` is not yet split.** The
BA 17 ↔ V1 1:1 correspondence means that any BA 17 split must be
mirrored by a corresponding V1 split, in the same commit, in both
hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../brodmann_area_17_primary_visual``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "brodmann_area_17_primary_visual"
        LOBE                         "occipital"
        BRODMANN_NUMBER              17
        ALTERNATE_NAMES              ("striate_cortex",
                                     "primary_visual_cortex_V1",
                                     "V1")
        ARCHITECTONIC_SIGNATURE      "stria_of_gennari"
        V_AREA_CORRELATE             ("primary_visual_cortex",)
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same fovea-at-pole /
                                     eccentricity-gradient /
                                     vertical-meridian /
                                     horizontal-meridian structure
        Bounding / overlapping territories
                                     (architectonic neighbours and
                                     sulcal / gyral landmarks)
        BA-to-neighbour adjacency
        The forward-declaration caveat text (byte-identical —
                                     the lingual-gyrus placement
                                     question is a lobe-level
                                     concern, not a hemisphere-
                                     level one)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — right BA 17 processes
                               the LEFT hemifield; left BA 17
                               processes the RIGHT hemifield.
                               The map's *structure* is the same;
                               the *label* of the represented
                               hemifield is flipped.
        FUNCTIONAL_DOMAINS     the right has **four** domains —
                               the left's three PLUS
                               `visual_attention_ventral_network_
                               target`. The right's fourth domain
                               captures the right-emphasized
                               attentional target role that the
                               left package declares at lower
                               weighting.
        DOMAIN_EMPHASIS        right: primary_visual_processing is
                               "first_cortical_stage_of_vision_
                               left_hemifield"; retinotopic_
                               organization is "fovea_at_pole_
                               left_hemifield_eccentricity_
                               gradient"; binocular_vision is
                               "ocular_dominance_columns_left_
                               hemifield_stereopsis"; visual_
                               attention_ventral_network_target
                               is "right_ventral_attention_
                               network_target_reorienting_
                               substrate".
                               left: primary_visual_processing is
                               "first_cortical_stage_of_vision_
                               right_hemifield"; retinotopic_
                               organization is "fovea_at_pole_
                               right_hemifield_eccentricity_
                               gradient"; binocular_vision is
                               "ocular_dominance_columns_right_
                               hemifield_stereopsis"; the left
                               FUNCTIONAL_DOMAINS set does not
                               include
                               visual_attention_ventral_
                               network_target.
        CONNECTIVITY           same bundle names; right: the LGN →
                               V1 projection carries the LEFT
                               hemifield; the BA 17 → BA 18 →
                               MT/V5 pathway carries the dominant
                               dorsal-stream motion contribution;
                               the BA 17 → BA 18 → LOC → FFA
                               pathway carries the right
                               face-recognition input; the right
                               FEF, right IPS, and right TPJ
                               send strong attentional gain to
                               right BA 17.
                               left: the LGN → V1 projection
                               carries the RIGHT hemifield; the
                               BA 17 → BA 18 → V4 → VWFA
                               pathway carries the left reading
                               input; the left FEF, left IPS, and
                               left TPJ send attentional gain to
                               left BA 17 (weaker reorienting
                               contribution).
        CLINICAL_ANCHORS       right: fourteen anchors (left
                               homonymous hemianopia, **left
                               macular sparing**, cortical
                               blindness, Anton syndrome,
                               blindsight, left-hemifield neglect
                               contribution, prosopagnosia
                               contribution, hemianopic alexia
                               (left), occipital infarct, right
                               ventral attention network target,
                               migraine aura, occipital epilepsy,
                               posterior cortical atrophy,
                               PRES).
                               left: twelve anchors (right
                               homonymous hemianopia, **right
                               macular sparing**, cortical
                               blindness, Anton syndrome,
                               blindsight, **hemianopic alexia
                               (right)**, **alexia without
                               agraphia (left V1 + splenium)**,
                               migraine aura, occipital epilepsy,
                               posterior cortical atrophy, PRES,
                               occipital infarct).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same BA 17, the same
architectonic signature, the same LGN input, and the same V1 → BA 18
hierarchy — but the *represented hemifield* is **flipped**. Right
BA 17 → left hemifield; left BA 17 → right hemifield. Any downstream
code that queries "what does the right BA 17 see?" must receive "the
left hemifield," and any downstream code that queries "what does the
left BA 17 see?" must receive "the right hemifield."

**The macular-sparing field label flips.** Macular sparing is a
hemisphere-invariant phenomenon, but the *side of the spared macula*
is determined by the side of the lesion: a **right V1 lesion**
produces a **left hemianopia with left macular sparing**; a **left V1
lesion** produces a **right hemianopia with right macular sparing**.

**The right-sided FUNCTIONAL_DOMAINS addition is the second sharpest
entry.** The right BA 17 adds `visual_attention_ventral_network_
target` as a fourth domain — the right-emphasized attentional target
role that the left BA 17 declares at lower weighting. **This is a
domain-set divergence between the two hemispheres**, not a
weighting-only divergence, and it must be preserved through any
refactor.

**The right-only clinical anchors are the third sharpest entry.** The
right BA 17 carries four anchors that the left does not carry at the
same weighting: `right_ba17_left_hemifield_neglect_contribution`,
`right_ba17_contribution_to_prosopagnosia`,
`right_ventral_attention_network_target`, and the right-side
`hemianopic_alexia_left`. The left BA 17's
`alexia_without_agraphia_left_occipital_plus_splenium` anchor is
**left-only** and has no right-side counterpart. The checklist
verifies these asymmetries.

**The hemisphere-invariant anchors** — cortical blindness, Anton
syndrome, blindsight, migraine aura, occipital epilepsy, posterior
cortical atrophy, PRES — are **documented identically in both
siblings** and must not be allowed to drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_17_primary_visual" (same as
    left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] BRODMANN_NUMBER is 17.
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's
    ("striate_cortex", "primary_visual_cortex_V1", "V1").
[ ] ARCHITECTONIC_SIGNATURE is "stria_of_gennari" — byte-identical
    to the left sibling's.
[ ] V_AREA_CORRELATE is exactly ``("primary_visual_cortex",)`` —
    byte-identical to the left sibling's.
[ ] NAMING_COLLISION_WITH is an empty tuple.
[ ] RETINOTOPIC_MAP is "fovea_at_pole_contralateral_hemifield" and
    the docstring documents the four sub-features with the **LEFT
    hemifield label**:
    - fovea at the occipital pole
    - eccentricity gradient (fovea → anterior calcarine)
    - vertical meridian at the V1/V2 border
    - horizontal meridian at the fundus of the calcarine sulcus
    - **the represented hemifield is the LEFT hemifield on the
      right side**
[ ] FUNCTIONAL_DOMAINS contains **four** domains:
    - primary_visual_processing
    - retinotopic_organization
    - binocular_vision
    - **visual_attention_ventral_network_target** (right-
      emphasized; not present on the left)
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision (V4, BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (V5/MT+, BA
    19 — **even though the right MT/V5 is the more strongly
    engaged side**, this is a BA 19 property, not a BA 17
    property).
[ ] FUNCTIONAL_DOMAINS **excludes** form_and_object_perception
    (V2, V3, V4, LOC — BA 18 and BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** spatial_localization (V3, V3A
    — BA 18 and BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing
    (left-lateralized; the right BA 17 does not feed the left
    VWFA).
[ ] FUNCTIONAL_DOMAINS **excludes** local_featural_processing
    (left-lateralized).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing as **BA 17 domains** — the right BA 17 is
    the *input stage* of the right face pathway and does not
    carry the domain itself.
[ ] DOMAIN_EMPHASIS captures the **right-side emphasis**:
    - primary_visual_processing → first_cortical_stage_of_vision_
      left_hemifield
    - retinotopic_organization → fovea_at_pole_left_hemifield_
      eccentricity_gradient
    - binocular_vision → ocular_dominance_columns_left_hemifield_
      stereopsis
    - visual_attention_ventral_network_target → right_ventral_
      attention_network_target_reorienting_substrate
[ ] CONNECTIVITY documents:
    - LGN thalamic afferent (primary, dominant, terminates in
      layer IV / stria of Gennari, carries the LEFT hemifield)
    - Pulvinar afferent (secondary, modulatory; part of the
      right ventral attention network substrate)
    - BA 17 → BA 18 principal cortical target (the obligate
      relay through which V1 reaches V2, V3, V4, MT/V5, and LOC)
    - **no direct BA 17 → BA 19 projections**
    - **BA 17 → BA 18 → LOC → right FFA pathway** (the right
      face-recognition input)
    - **BA 17 → BA 18 → MT/V5 pathway** (the dominant dorsal-
      stream motion input on the right)
    - callosal connections to the left BA 17 at the vertical
      meridian (V1/V2 border)
    - attentional feedback from the right FEF (BA 8), right
      DLPFC (BA 9 / BA 46), right IPS, and right TPJ (the
      right-lateralized ventral and dorsal attention networks)
[ ] CLINICAL_ANCHORS contains the fourteen right-specific anchors:
    - right_ba17_left_homonymous_hemianopia
    - **left_macular_sparing**
    - cortical_blindness_bilateral
    - anton_syndrome
    - blindsight
    - **right_ba17_left_hemifield_neglect_contribution**
    - **right_ba17_contribution_to_prosopagnosia**
    - **hemianopic_alexia_left**
    - occipital_infarct_pca_territory
    - **right_ventral_attention_network_target**
    - migraine_visual_aura
    - occipital_epilepsy_visual_auras
    - posterior_cortical_atrophy
    - pres_visual_symptoms
[ ] The **left homonymous hemianopia** is documented as the primary
    right BA 17 anchor — the canonical right-lateralized
    visual-field deficit.
[ ] **Left macular sparing** is documented with its dual-blood-
    supply mechanism, with the side-appropriate sparing (left
    macular sparing from a right lesion).
[ ] **Cortical blindness, Anton syndrome, and blindsight** are
    documented as the hemisphere-invariant bilateral-lesion
    syndromes, byte-identically to the left sibling's treatment.
[ ] **Hemianopic alexia (left)** is documented as a right-side
    anchor — the left hemianopia impairs reading by removing the
    left-hemifield input to the **intact left reading network**,
    and the deficit is **milder** than after a left V1 lesion
    (which impairs the reading network directly). **The right
    BA 17 does NOT produce alexia without agraphia** — that
    syndrome is left-only.
[ ] The **left-hemifield neglect contribution** is documented as
    a right-emphasized anchor — **isolated right V1 lesions do
    not produce neglect**, but right V1 is part of the right
    ventral attention network substrate that contributes to left
    hemispatial neglect when the lesion extends to the right TPJ
    and right FEF.
[ ] The **prosopagnosia contribution** is documented as a
    right-emphasized anchor — **isolated right BA 17 lesions do
    not produce prosopagnosia**, but the right BA 17 is the
    occipital input stage of the right face pathway, and right
    occipito-temporal lesions that involve the right FFA or its
    input pathway produce prosopagnosia.
[ ] The **right ventral attention network target** is documented
    as the right-specific attentional role — the right V1 is a
    target of the right TPJ + right FEF reorienting network,
    which is the dominant reorienting substrate in the human
    brain.
[ ] The **BA 17 ↔ V1 1:1 correspondence** is documented
    byte-identically to the left sibling's.
[ ] The **stria of Gennari**, the **four-component retinotopic
    map** (with LEFT hemifield labels), the **cuneus and lingual
    gyrus bank mapping** (lower LEFT / upper LEFT), and the **BA
    17 / BA 18 vertical meridian** are all documented
    byte-identically to the left sibling's (except for the
    hemifield label, which is flipped).
[ ] No forward-declaration caveat is needed for the BA-side
    neighbours. The lingual gyrus forward-reference caveat text
    is byte-identical to the left sibling's.
[ ] No SUBDIVISIONS promotion is performed while the V1 functional
    counterpart under ``..cortex/primary_visual_cortex`` is not
    yet split.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURE,
    V_AREA_CORRELATE, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, forward-declaration caveat text) match the left
    sibling; the RETINOTOPIC_MAP's represented hemifield,
    FUNCTIONAL_DOMAINS set (four on the right, three on the
    left), DOMAIN_EMPHASIS, and CLINICAL_ANCHORS deliberately
    differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    BA 17 carries "left_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP; the left BA 17 carries "right_hemifield."
    Neither has been copied verbatim from the other.
[ ] **The macular-sparing asymmetry is verified**: the right
    BA 17 carries a **left** macular sparing anchor; the left
    BA 17 carries a **right** macular sparing anchor.
[ ] **The right-specific FUNCTIONAL_DOMAINS addition is verified**:
    `visual_attention_ventral_network_target` is present on the
    right and absent on the left. This is a **domain-set
    divergence**, not just a weighting divergence.
[ ] **The right-only clinical anchors are verified**:
    `right_ba17_left_hemifield_neglect_contribution`,
    `right_ba17_contribution_to_prosopagnosia`,
    `right_ventral_attention_network_target`, and
    `hemianopic_alexia_left` are present on the right and absent
    on the left. The left-only `alexia_without_agraphia_left_
    occipital_plus_splenium` anchor is absent on the right.
[ ] Any downstream code querying "what does the right BA 17
    see?" must receive "the LEFT visual hemifield."
[ ] Any downstream code querying "what is BA 17?" must receive
    "V1 / primary visual cortex / striate cortex" — the 1:1
    BA 17 ↔ V1 correspondence is enforced.
[ ] Any downstream code assigning face processing must route
    through the **right** BA 17 → BA 18 → BA 19 → LOC → FFA
    chain — the right BA 17 is the input stage, but it is
    **not** the face operation.
[ ] Any downstream code assigning the reading pathway must
    route through the **left** BA 17 → BA 18 → BA 19 → V4 →
    VWFA chain — the left BA 17 is the input stage, but it is
    **not** the reading operation.
[ ] Any downstream code assigning left hemispatial neglect must
    note that **right V1 is a contributor**, not a sole cause —
    the lesion must extend to the right TPJ and right FEF for
    the full neglect syndrome.
"""