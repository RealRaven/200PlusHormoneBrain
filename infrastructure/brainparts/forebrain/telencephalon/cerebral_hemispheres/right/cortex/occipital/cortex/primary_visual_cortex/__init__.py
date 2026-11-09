"""
Primary Visual Cortex (V1) — Right Hemisphere
==============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── cortex
                                    └── primary_visual_cortex   ← THIS PACKAGE

This is a **leaf functional / retinotopic package** describing the
right hemisphere's **V1** — the **primary visual cortex**, also called
the **striate cortex** because of the architectonically visible
**stria of Gennari**. It is the **first and tightest** V↔BA
correspondence in the human cortex: **V1 is BA 17**, one-to-one, with
no residual. It is the first cortical stage of the visual hierarchy,
the input point for the visual radiation from the lateral geniculate
nucleus (LGN), and the anatomical substrate of **conscious visual
perception**.

Parent: ``..cortex`` (right occipital functional / V-numbered parent)
— sibling to V2, V3, V4. **Sibling — not parent —** of
``...brodmann_areas/brodmann_area_17_primary_visual``, which sits at
the ``..brodmann_areas`` parent level. The V1 / BA 17 relationship is
**1:1 correspondence, not nesting** — both packages describe the same
cortical territory from different angles (functional-retinotopic vs
cytoarchitectonic), and downstream code should treat them as
interchangeable identifiers for the same thing.

This package is the **structural mirror** of
``../../left/cortex/occipital/cortex/primary_visual_cortex``. The
V-number, the BA correlate (17), the architectonic signature (stria
of Gennari), the calcarine-sulcus surface landmark, and the retinotopic
map structure are identical on both sides; the **functional emphasis**
and **clinical significance** diverge — on the right, V1 processes the
**left** visual hemifield, and its ventral-stream output feeds the
right fusiform face area (FFA) via V2 / V3 / V4 / LOC. The right V1 is
also a **target of the right ventral attention network** — a
right-lateralized attentional role that the left V1 does not carry at
the same weighting.

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
        callosal connections between the right and left V1 meet at
        this border, in the V2 territory.

    Horizontal meridian → base of the calcarine sulcus
        The horizontal meridian is represented at the **fundus**
        (deepest part) of the calcarine sulcus.

**Right-hemisphere specificity**: the right V1 processes the **LEFT**
visual hemifield of both eyes (contralateral processing). The
**left homonymous hemianopia** that follows a right V1 lesion is the
canonical right-lateralized visual-field deficit. On the right, V1 is
also the **input stage of the ventral stream that feeds the right
FFA** — the face-recognition pathway begins in the right V1 and
terminates in the right fusiform gyrus; this is why right V1 lesions
can contribute to face-processing deficits when the downstream
occipito-temporal pathway is also involved. **The right V1 is also a
target of the right ventral attention network** (with the right
temporoparietal junction and right frontal eye fields) that reorients
to salient visual events — a right-lateralized attentional role that
the left V1 does not carry at the same weighting.

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
            visual field. **On the right, the lower LEFT field.**
        lingual gyrus — lower-bank V1
            The lingual gyrus (lower bank of the calcarine sulcus)
            carries the ventral V1 representation of the **upper**
            contralateral visual field. **On the right, the upper
            LEFT field.** (Note: the lingual gyrus is a **forward
            reference** in ``..gyri`` — it is not yet a package.)
        calcarine sulcus — defining surface landmark
            The calcarine sulcus is the **defining sulcus** of V1
            and the surface landmark for V1's representation. The
            ``..sulci/calcarine_sulcus`` package declares V1 (and
            BA 17) as its primary functional overlay.
        right fusiform face area (FFA) — downstream ventral-
        stream target
            **Right-specific overlay.** The right V1's ventral-stream
            output — via V2, V3, V4, and the LOC — terminates in
            the **right FFA** in the right fusiform gyrus. The
            V1 → V2 → V3 → V4 → LOC → FFA pathway is the **right
            face-recognition pathway**, and right V1 is its
            **input stage**.
        right ventral attention network — target
            **Right-emphasized overlay.** The right V1 is a target
            of the **right ventral attention network** (right TPJ
            + right FEF), which reorients to salient visual
            events. The left V1 is also a target of the left
            ventral attention network, but the right network is
            the dominant reorienting substrate in the human
            brain.

**This field is structurally identical to the left sibling's** — the
architectonic neighbours and the cuneus / lingual-gyrus / calcarine
overlays are the same on both sides. What differs is the **visual
hemifield** — the right V1 processes the LEFT hemifield, and the
cuneus / lingual gyrus representations carry the upper / lower LEFT
field on the right. The **right FFA downstream target** is a
right-specific functional overlay that the left V1 package declares
as the **left VWFA** (the reading endpoint) instead, and the **right
ventral attention network target** is a right-emphasized overlay
that the left V1 package does not carry at the same weighting.

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
                                           right and left V1 meet at
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
                                           (**lower LEFT field on
                                           the right**)
    lingual gyrus (medial-surface          ventral bank of the calcarine
    gyrus; forward reference in ..gyri)    sulcus; the lower-bank V1
                                           representation of the
                                           **upper** visual field
                                           (**upper LEFT field on
                                           the right**)
    calcarine sulcus (defining sulcus)     the fundus of the sulcus
                                           represents the horizontal
                                           meridian; the banks
                                           represent the upper /
                                           lower fields

**This field is byte-identical to the left sibling's** at the level of
V-numbered and BA-numbered neighbours. The adjacency relationships are
topological, not lateralized. The field labels (LEFT vs RIGHT) in the
cuneus and lingual gyrus entries are updated for the right hemisphere.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

V1 participates in **four** canonical occipital functional domains on
the right — the same three as the left (`primary_visual_processing`,
`retinotopic_organization`, `binocular_vision`) plus one
**right-emphasized** attentional target role
(`visual_attention_ventral_network_target`). This matches the right
BA 17 package's four-domain set exactly, preserving the 1:1
correspondence. The emphasis is as follows:

    primary_visual_processing                      (right emphasis — PRIMARY)
        **This is V1's defining contribution.** The first
        cortical stage of vision: orientation selectivity,
        ocular-dominance columns, spatial-frequency tuning, contrast
        sensitivity, edge detection, and retinotopic mapping. On
        the right, V1 processes the **LEFT visual hemifield**; left
        homonymous hemianopia follows right V1 lesions.

    retinotopic_organization                       (right emphasis — PRIMARY)
        **This is V1's second primary contribution.** The
        topographic mapping of the **LEFT visual hemifield** onto
        the right calcarine banks, with the fovea at the occipital
        pole and the periphery at the anterior calcarine banks. The
        right V1's retinotopic map is essentially a mirror image of
        the left V1's, with the field label flipped.

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
        reorienting contribution is weaker. **This domain is
        present on the right and absent on the left** — a
        domain-set divergence from the left sibling, consistent
        with the right BA 17 package's treatment.

**Right-specific caveat on `color_vision`.** V1 is **not** the
color-vision area — that is V4, in BA 19. `color_vision` is
**omitted** from the V1 `FUNCTIONAL_DOMAINS` tuple; it appears in V4
instead.

**Right-specific caveat on `motion_perception`.** V1 is **not** the
motion area — that is V5/MT+, a forward reference in BA 19. **On the
right, V5/MT+ is the dominant motion hemisphere**, but this is a
V5/MT+ property, not a V1 property. `motion_perception` is **omitted**
from the V1 `FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `form_and_object_perception`.** V1
contributes to the **early stages** of form processing (edge
detection, contour integration), but **object recognition** emerges in
V4, the LOC, and the ventral stream. `form_and_object_perception` is
**omitted** from the V1 `FUNCTIONAL_DOMAINS` tuple. **The right V4 →
LOC → right FFA pathway terminates in the right face endpoint**, but
this is downstream of V1, not in V1 itself.

**Right-specific caveat on `spatial_localization`.** V1 contributes
to the **early stages** of spatial localization (retinotopic
position), but **full spatial localization** emerges in V3, V3A, and
V5/MT+. **On the right, V3A and V5/MT+ are the dominant spatial
areas.** `spatial_localization` is **omitted** from the V1
`FUNCTIONAL_DOMAINS` tuple.

**Right-specific caveat on `visual_attention`.** V1 is a **target**
of top-down attentional modulation from the frontal eye fields (BA
8) and the dorsolateral prefrontal cortex, and the **right V1 is a
target of the right ventral attention network** for reorienting to
salient visual events. But V1 is **not itself an attentional control
area** — it is a *target*, not a *generator*. The right-emphasized
attentional target role is captured under
`visual_attention_ventral_network_target` above; `visual_attention`
as a general primary domain is **omitted**.

**Right-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the
**right V1 supports as an input stage** but does **not** carry as
primary functional domains. `face_processing` is instantiated in the
right FFA (fed by the right V1 → V2 → V3 → V4 → LOC → FFA pathway);
`global_visual_processing` begins at right V2 (the BA 18 emphasis).
**No single V area claims `face_processing` or `global_visual_
processing` as a primary contribution** — they are network properties
of the right occipital + right fusiform / right hemisphere pathways.

**Right-specific caveat on `visual_word_processing` and `local_
featural_processing`.** These are **left-lateralized** functions that
the right V1 does **not** carry. `visual_word_processing` is
instantiated in the left VWFA (fed by the left V1 ventral stream);
`local_featural_processing` is a left-hemisphere advantage beginning
at left V2. Neither appears in the right V1 `FUNCTIONAL_DOMAINS`
tuple.

**Summary**: V1 carries **exactly four** functional domains on the
right — `primary_visual_processing`, `retinotopic_organization`,
`binocular_vision`, and `visual_attention_ventral_network_target`.
The first three are shared with the left and with BA 17; the fourth
is a right-emphasized attentional target role, consistent with the
right BA 17 package. **The right V1's FUNCTIONAL_DOMAINS set matches
the right BA 17's exactly** — the 1:1 correspondence between V1 and
BA 17 extends to the functional domains, on both hemispheres.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), right
            **V1's primary and dominant thalamic afferent.** The
            right LGN relays the visual signal from the right
            hemiretinas of both eyes (via the optic chiasm and the
            right optic tract). The LGN → V1 projection terminates
            in layer IV of the striate cortex — **layer IV is where
            the stria of Gennari runs** — and the LGN input is
            segregated into ocular-dominance columns that alternate
            between the left-eye and right-eye inputs. **On the
            right, this input carries the LEFT visual hemifield.**
        → pulvinar (secondary, modulatory)
            The pulvinar sends a weaker modulatory projection to
            V1 (and stronger projections to V2, V3, and V4),
            participating in the cortico-thalamo-cortical loops
            that support visual attention and visual short-term
            memory. **On the right, the pulvinar → V1 loop is part
            of the right ventral attention network substrate.**
        → LGN feedback from layer VI
            V1 layer VI projects **back** to the LGN, forming the
            cortico-geniculate feedback loop that modulates the
            thalamic relay.

    cortical efferents
        → V2, right
            **V1's principal cortical target.** The V1 → V2
            projection carries V1's output to V2 (the first
            extrastriate stage). This is the first step of the
            V1 → V2 → V3 → V4 hierarchy.
        → V3 and V4 (via the V2 relay)
            V1's output reaches V3 and V4 via the **V2 relay**,
            not directly. There are **no direct V1 → V3 or V1 →
            V4 projections**.
        → MT/V5 (via V2, dorsal stream — forward reference)
            The motion pathway (V1 → V2 → MT/V5) carries the
            low-level motion signal from V1 to the motion area.
            **On the right, MT/V5 is more strongly engaged during
            visuospatial attention and motion-in-space processing
            than on the left** — the right dorsal stream's motion
            contribution dominates. On the right, this pathway
            supports **LEFT-hemifield** motion perception.
        → LOC (via V2, V3, V4, ventral stream — forward reference)
            The color/form/object pathway (V1 → V2 → V3 → V4 →
            LOC) carries the low-level object signal from V1 to
            the LOC. **On the right, the LOC → right FFA pathway
            carries the object-form signal forward to the face-
            recognition endpoint.**

    callosal connections
        → left V1
            The callosal fibers connect the right V1 to the left
            V1 at the **vertical meridian** (the V1/V2 border),
            where the two hemispheres' visual fields meet. This
            callosal connection is essential for the **fusion of
            the two hemifields** and for the **continuity of
            vision across the vertical midline**.

    attentional feedback
        → frontal eye fields (BA 8), right
            **Right-emphasized.** The right FEF is the dominant
            node of the right ventral attention network and sends
            strong **top-down and bottom-up attentional gain** to
            right V1, modulating the responsiveness of V1 neurons
            to behaviourally relevant stimuli.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), right
            The right DLPFC sends top-down attentional and
            working-memory signals to V1, supporting **visual
            working memory** and **visual imagery**.
        → intraparietal sulcus, right
            **Right-emphasized.** The right IPS is a core node of
            the right dorsal attention network and sends strong
            top-down spatial-attention signals to right V1,
            supporting **spatial attention** in the LEFT visual
            hemifield.
        → temporoparietal junction, right
            **Right-emphasized.** The right TPJ is the other core
            node of the right ventral attention network and sends
            reorienting signals to right V1 via the right FEF.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the right in three respects:
(a) the V1 → V2 → V4 → LOC → right FFA pathway is the **right face-
recognition pathway**, not the left reading pathway;
(b) the right MT/V5 is more strongly engaged during visuospatial
attention, so the right V1 → V2 → MT/V5 pathway carries the dominant
dorsal-stream motion contribution;
(c) the right FEF, right IPS, and right TPJ send strong attentional
gain to right V1 as part of the **right-lateralized ventral and dorsal
attention networks**.

**Note: the connectivity is identical in structure to BA 17's.** The
1:1 correspondence between V1 and BA 17 extends to connectivity —
they describe the same territory.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_v1_left_homonymous_hemianopia
        **This is the right V1 anchor par excellence.** A lesion of
        the right V1 (or the right optic radiation, or the right
        LGN) produces a **left homonymous hemianopia** — loss of
        the left half of the visual field in both eyes. The deficit
        is **homonymous** (both eyes lose the same side),
        **hemianopic** (half the field is lost), and
        **contralateral** (left side from a right lesion). This is
        the single most common and most clinically consequential
        effect of a right V1 lesion.

    macular_sparing_left
        **Macular sparing** — preservation of the central 5–10° of
        the visual field within an otherwise complete homonymous
        hemianopia — is a well-known phenomenon in V1 lesions.
        The mechanism is the **dual blood supply** of the
        occipital pole (PCA + MCA), whereas the anterior calcarine
        banks receive blood from the PCA alone. **An MCA-PCA
        watershed infarct spares the occipital pole, sparing the
        macula.** **On the right, a right V1 lesion produces a
        left hemianopia with left macular sparing.**

    cortical_blindness_bilateral
        **Bilateral V1 lesions** produce **cortical blindness** —
        complete loss of vision despite intact eyes, optic nerves,
        and LGN. The patient has no visual perception but may
        retain pupillary light reflexes. **This anchor is
        hemisphere-invariant** — it appears on both sides with
        the same clinical significance.

    anton_syndrome
        **Anton syndrome** — **cortical blindness with denial of
        blindness** — is a rare complication of bilateral V1
        lesions. **This anchor is hemisphere-invariant.**

    blindsight
        **Blindsight** — residual visual function in the absence
        of conscious visual perception — is a well-documented
        phenomenon after **V1 lesions**. The residual function is
        mediated by **subcortical visual pathways** (the superior
        colliculus and the pulvinar). **This anchor is
        hemisphere-invariant.**

    right_v1_left_hemifield_neglect_contribution
        **Right-emphasized.** Right V1 lesions contribute to
        **left hemispatial neglect** when the lesion extends
        beyond V1 into the right parietal and right frontal
        territories. **Isolated right V1 lesions do not produce
        neglect** — the patient has a left homonymous hemianopia
        but can attend to the left field cognitively — but the
        right V1 is part of the **right ventral attention
        network** substrate that, when damaged together with the
        right TPJ and right FEF, contributes to the neglect
        syndrome. **The right V1 is therefore the
        right-lateralized attentional substrate that the left V1
        is not.** This anchor has no symmetric counterpart on the
        left.

    right_v1_contribution_to_prosopagnosia
        **Right-emphasized.** Right V1 is the **input stage** of
        the right ventral stream that feeds the right FFA, and
        **right occipito-temporal lesions** that involve the right
        FFA or its input pathway produce **prosopagnosia**.
        **Isolated right V1 lesions do not produce prosopagnosia**
        — the right FFA is spared — but the right V1 is the
        **occipital input stage** of the right-lateralized face
        pathway. **Prosopagnosia is the canonical right-
        lateralized visual-recognition deficit**, and right V1 is
        its first cortical stage.

    hemianopic_alexia_left
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **left homonymous hemianopia** (from a
        right V1 lesion) — is a recognized clinical entity, but
        **weaker than the left-side equivalent**. The reading
        deficit arises because the patient must make large
        **leftward saccades** to compensate for the missing left
        hemifield, and the **left-hemisphere reading network**
        cannot function efficiently without the full right-
        hemifield input. **A right V1 lesion produces a left
        hemianopia that impairs reading via the loss of the
        left-hemifield input to the reading network**, but the
        reading network itself (left VWFA, left angular gyrus)
        is intact and the deficit is milder than after a left V1
        lesion.

    occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct** involving
        the right V1 produces **left homonymous hemianopia**,
        often with **left macular sparing**. **Isolated right PCA
        infarcts do not produce alexia without agraphia** — that
        syndrome is left-lateralized — because the right splenium
        does not connect to a right reading network.

    right_ventral_attention_network_target
        **Right-emphasized.** Right V1 is a target of the right
        ventral attention network (right TPJ + right FEF), which
        reorients to salient visual events. **Isolated right V1
        lesions do not produce reorienting deficits**, but right
        V1 is part of the network's substrate and its
        participation is part of the right-lateralized
        reorienting substrate that the left V1 does not carry at
        the same weighting.

    migraine_visual_aura
        **Migraine visual aura** — the transient, typically
        bilateral, scintillating scotomata and fortification
        spectra that precede a migraine headache — reflects
        **cortical spreading depression** spreading across the
        **occipital cortex**, including V1. **This anchor is
        hemisphere-invariant.**

    occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** —
        elementary visual hallucinations in the **contralateral
        visual field** — is a well-characterized epilepsy
        syndrome. **Right V1 auras project to the left visual
        field.**

    posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **V1 and V2** bilaterally in later
        stages. **On the right, PCA presents with the visuospatial
        / prosopagnosic syndrome (Benson syndrome)** — progressive
        prosopagnosia, visuospatial deficits, optic ataxia, and
        simultanagnosia.

    pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia** from
        bilateral occipital involvement. **The syndrome is
        reversible** in most cases.

These anchors are **right-hemisphere-specific** in two senses:
(a) the right V1 processes the **LEFT visual hemifield**, so right
V1 lesions produce **left-sided** visual deficits; (b) the right V1
is the **input stage of the right face pathway** and is part of the
**right-lateralized ventral attention network** substrate, so right
V1 lesions can contribute to face-processing deficits (prosopagnosia)
and left hemispatial neglect. **The right V1 does not produce alexia
without agraphia** — that syndrome is left-lateralized — and the
right V1's reading contribution is limited to the milder left-side
hemianopic alexia. The left sibling's docstring carries the
corresponding left-sided anchors (right homonymous hemianopia,
right macular sparing, alexia without agraphia from left V1 +
splenium).

**The clinical anchors match BA 17's right-side anchors exactly** —
the 1:1 correspondence between V1 and BA 17 extends to the clinical
syndromes. Downstream code that queries V1 for a clinical anchor
receives the same result as querying BA 17.

**The `macular_sparing`, `blindsight`, `Anton syndrome`, and
`cortical blindness` anchors are hemisphere-invariant** — they appear
on both sides and are documented identically in both siblings. The
**field label of the sparing** differs (left macular sparing from a
right lesion vs right macular sparing from a left lesion), but the
phenomenon and its mechanism are the same.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..cortex  (parent)
    The right occipital functional / V-numbered parent. This
    package's parent, source of the ``BA_TO_V_CROSSWALK``,
    ``V_TO_BA_CROSSWALK``, ``FORWARD_REFERENCE_V_AREAS``, and
    ``DOMAIN_COVERAGE`` registries, and enforcer of the **V1 ↔ BA
    17 1:1 correspondence**.

..v2
    **Rostral neighbour** via the V1/V2 border. The V1 → V2
    projection is the first step of the V1 → V2 → V3 → V4
    hierarchy. **The vertical meridian of the visual field is
    represented at the V1/V2 border**.

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
    **On the right, the lower LEFT field.**

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus (lower bank of the calcarine sulcus) carries
    the **ventral V1 representation of the upper** contralateral
    visual field. **On the right, the upper LEFT field.**

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
    the temporal lobe. **On the right, the ventral stream
    terminates in the right FFA** (the face area), and the right
    V1 is the **input stage** of this pathway. **Right
    occipito-temporal lesions produce prosopagnosia** — the
    canonical right-lateralized visual-recognition deficit. The
    temporal package must declare the right V1 as the source of
    its visual input via the ventral stream, and must note the
    **right-lateralized FFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from V2 / V3 / V4 into the
    parietal lobe. **On the right, the dorsal stream is more
    strongly engaged during visuospatial attention**, and the
    right parietal lobe is a core node of the right-lateralized
    dorsal attention network. The parietal package must declare
    the right V1 as the source of its visual input for the
    dorsal stream, and must note the **right-lateralized
    attentional emphasis**.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to V1 via the V2 relay. **On the right, the right FEF
    is the dominant node of the ventral attention network**, and
    right frontal lesions contribute to left hemispatial neglect.
    The frontal package must declare the right V1 as a target of
    its attentional projections.

..cortex.cingulate  — indirect
    No direct cingulate → V1 projection.

..cortex.insular  — indirect
    No direct insular → V1 projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    **The LGN is V1's primary and dominant thalamic afferent.**
    The LGN → V1 projection terminates in layer IV (where the
    stria of Gennari runs) and is segregated into ocular-dominance
    columns. **On the right, this input carries the LEFT visual
    hemifield.**

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a secondary, modulatory projection to V1
    (stronger to V2, V3, and V4). **On the right, the pulvinar →
    V1 loop is part of the right ventral attention network
    substrate.**

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream terminates in the perirhinal, entorhinal,
    and parahippocampal cortices. **The right V1 is the input
    stage** of the occipito-temporal-hippocampal pathway. **On
    the right, the parahippocampal place area (PPA) and the
    retrosplenial complex receive visual input supporting scene
    and spatial memory**, which are more strongly right-
    lateralized.

../../left/cortex/occipital/cortex/primary_visual_cortex
    The left-hemisphere homologue. Structural fields (V-number,
    BA correlate, architectonic signature, calcarine-sulcus
    surface landmark, retinotopic map structure, cuneus /
    lingual-gyrus relationship, FUNCTIONAL_DOMAINS set,
    forward-declaration caveat text) MUST be byte-identical.
    Functional emphasis and clinical significance diverge — the
    right V1 processes the **LEFT** visual hemifield, and right
    V1 lesions produce **left** homonymous hemianopia with
    **left** macular sparing. The right V1 is the input stage of
    the right ventral stream that feeds the right FFA, not the
    left VWFA, and it is part of the right-lateralized ventral
    attention network substrate.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "primary_visual_cortex"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    V_NUMBER            = "V1"
    ALTERNATE_NAMES     = ("striate_cortex",
                           "V1",
                           "brodmann_area_17_primary_visual")
        # **Byte-identical to the left sibling's.** The 1:1 BA
        # correspondence is a property of V1, not of the
        # hemisphere.

    ARCHITECTONIC_SIGNATURE = "stria_of_gennari"
        # **Byte-identical to the left sibling's.**

    BRODMANN_CORRELATES = (17,)
        # **Exactly one** BA — the tightest V↔BA correspondence
        # in the cortex. **Byte-identical to the left sibling's.**

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** Byte-identical to the left
        # sibling's.

    RETINOTOPIC_MAP     = "fovea_at_pole_contralateral_hemifield"
        # The map's *structure* is identical to the left's.
        # **On the right, the represented hemifield is the LEFT
        # hemifield.**

    VISUAL_HEMIFIELD    = "left"
        # **The represented visual hemifield** — the most
        # important single fact about the right V1.

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing",
                              "retinotopic_organization",
                              "binocular_vision",
                              "visual_attention_ventral_network_"
                              "target",     # right-emphasized
                              # **Identical to the right BA 17's
                              # domain set** — the 1:1
                              # correspondence extends to the
                              # functional domains, on both
                              # hemispheres.
                              # NOTE: color_vision is EXCLUDED (V4,
                              # BA 19 territory).
                              # NOTE: motion_perception is EXCLUDED
                              # (V5/MT+, BA 19 territory).
                              # NOTE: form_and_object_perception is
                              # EXCLUDED (V2, V3, V4, LOC).
                              # NOTE: spatial_localization is
                              # EXCLUDED (V3, V3A).
                              # NOTE: visual_attention is
                              # EXCLUDED as a *primary* domain
                              # beyond the target role captured in
                              # `visual_attention_ventral_
                              # network_target`.
                              # NOTE: visual_word_processing is
                              # EXCLUDED (left-lateralized).
                              # NOTE: face_processing and global_
                              # visual_processing are EXCLUDED as
                              # *V1 domains* (they live downstream
                              # in the right FFA / right BA 18
                              # emphasis).
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
                              "right_v1_left_homonymous_"
                              "hemianopia",
                              "macular_sparing_left",
                              "cortical_blindness_bilateral",
                              "anton_syndrome",
                              "blindsight",
                              "right_v1_left_hemifield_neglect_"
                              "contribution",
                              "right_v1_contribution_to_"
                              "prosopagnosia",
                              "hemianopic_alexia_left",
                              "occipital_infarct_pca_territory",
                              "right_ventral_attention_network_"
                              "target",
                              "migraine_visual_aura",
                              "occipital_epilepsy_visual_auras",
                              "posterior_cortical_atrophy",
                              "pres_visual_symptoms",
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
sulcus) is a forward reference in ``..gyri``, but the V1 package does
not depend on it.

**The one open question** — the lingual gyrus placement — is
byte-identical to the left sibling's. It is a property of the
occipital lobe, not of the hemisphere.

**All forward-declaration caveat text is byte-identical to the left
sibling's.**

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
  4. Mirror the promotion on the left side in the same commit.

**The foveal / peripheral split is a FUNCTIONAL subdivision, not an
architectonic one.**

**The foveal component is the macular-sparing substrate** — the
dual blood supply (PCA + MCA at the occipital pole). **On the right,
the macular sparing is left macular sparing.**

**No split should be performed while the BA 17 functional counterpart
under ``..brodmann_areas/brodmann_area_17_primary_visual`` is not yet
split.** The V1 ↔ BA 17 1:1 correspondence means that any V1 split
must be mirrored by a corresponding BA 17 split, in the same commit,
in both hemispheres.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../primary_visual_cortex``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "primary_visual_cortex"
        LOBE                         "occipital"
        V_NUMBER                     "V1"
        ALTERNATE_NAMES              ("striate_cortex", "V1",
                                     "brodmann_area_17_primary_
                                     visual")
        ARCHITECTONIC_SIGNATURE      "stria_of_gennari"
        BRODMANN_CORRELATES          (17,)
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same fovea-at-pole /
                                     eccentricity-gradient /
                                     vertical-meridian /
                                     horizontal-meridian structure
        Bounding / overlapping territories
        V-to-neighbour adjacency (with the LEFT / RIGHT
                                     field labels updated for the
                                     cuneus and lingual gyrus)
        CONNECTIVITY                 same bundle names
        The forward-declaration caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — right V1 processes
                               the LEFT hemifield; left V1
                               processes the RIGHT hemifield.
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        FUNCTIONAL_DOMAINS     the right has **four** domains —
                               the left's three PLUS
                               `visual_attention_ventral_
                               network_target`. **The right's
                               set matches the right BA 17's
                               exactly** — the 1:1 correspondence
                               extends to the domains on both
                               hemispheres.
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
                               right_hemifield"; etc.; the left
                               FUNCTIONAL_DOMAINS set does not
                               include visual_attention_ventral_
                               network_target.
        CONNECTIVITY           same bundle names; right: the V1 →
                               V2 → V4 → LOC → right FFA pathway
                               is the right face-recognition
                               pathway; the right MT/V5 is more
                               strongly engaged; the right FEF,
                               right IPS, and right TPJ send
                               strong attentional gain.
                               left: the V1 → V2 → V4 → LOC →
                               left VWFA pathway is the left
                               reading pathway.
        CLINICAL_ANCHORS       right: fourteen anchors (left
                               homonymous hemianopia, **left
                               macular sparing**, cortical
                               blindness, Anton syndrome,
                               blindsight, **left hemifield
                               neglect contribution**,
                               **prosopagnosia contribution**,
                               hemianopic alexia (left, milder),
                               occipital infarct, **right
                               ventral attention network
                               target**, migraine aura,
                               occipital epilepsy, PCA (Benson
                               syndrome), PRES).
                               left: twelve anchors (right
                               homonymous hemianopia, **right
                               macular sparing**, cortical
                               blindness, Anton syndrome,
                               blindsight, **hemianopic alexia
                               (right)**, **alexia without
                               agraphia (left V1 + splenium)**,
                               migraine aura, occipital epilepsy,
                               PCA, PRES, occipital infarct).

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same V1, the same architectonic
signature, the same LGN input, and the same V1 → V2 hierarchy — but
the *represented hemifield* is **flipped**.

**The macular-sparing field label flips.** A **right V1 lesion**
produces a **left hemianopia with left macular sparing**.

**The right-specific FUNCTIONAL_DOMAINS addition is the second
sharpest entry.** The right V1 adds
`visual_attention_ventral_network_target` as a fourth domain — the
right-emphasized attentional target role. **The left V1 does not have
this domain.** This is a domain-set divergence, not a weighting-only
divergence, and it matches the right BA 17's domain set exactly.

**The right-only clinical anchors are the third sharpest entry.** The
right V1 carries four anchors that the left does not carry at the
same weighting: `right_v1_left_hemifield_neglect_contribution`,
`right_v1_contribution_to_prosopagnosia`,
`right_ventral_attention_network_target`, and
`hemianopic_alexia_left` (which is left-specific but milder, and its
mirror on the left is `hemianopic_alexia_right`). The left V1's
`alexia_without_agraphia_left_v1_plus_splenium` anchor is
**left-only** and has no right-side counterpart.

**The FUNCTIONAL_DOMAINS set matches BA 17's on both hemispheres** —
the 1:1 correspondence extends to the domains, and the right-side
four-domain set is the mirror of the right BA 17's four-domain set.

**The hemisphere-invariant anchors** — cortical blindness, Anton
syndrome, blindsight, migraine aura, occipital epilepsy, PCA, PRES,
and occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "primary_visual_cortex" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] V_NUMBER is "V1".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's.
[ ] ARCHITECTONIC_SIGNATURE is "stria_of_gennari" — byte-identical
    to the left sibling's.
[ ] BRODMANN_CORRELATES is exactly ``(17,)`` — byte-identical to
    the left sibling's.
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
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class,
    queryable field.
[ ] FUNCTIONAL_DOMAINS contains **four** domains:
    - primary_visual_processing
    - retinotopic_organization
    - binocular_vision
    - **visual_attention_ventral_network_target** (right-
      emphasized; not present on the left)
[ ] FUNCTIONAL_DOMAINS **excludes** color_vision (V4, BA 19).
[ ] FUNCTIONAL_DOMAINS **excludes** motion_perception (V5/MT+, BA
    19).
[ ] FUNCTIONAL_DOMAINS **excludes** form_and_object_perception
    (V2, V3, V4, LOC).
[ ] FUNCTIONAL_DOMAINS **excludes** spatial_localization (V3,
    V3A).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_attention as a
    primary domain beyond the target role captured in
    `visual_attention_ventral_network_target`.
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing and
    local_featural_processing (left-lateralized).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing as **V1 domains** (they live downstream).
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical to
    the right BA 17's** — the 1:1 correspondence extends to the
    functional domains on the right hemisphere.
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
    - LGN thalamic afferent (primary, dominant, carries the LEFT
      hemifield)
    - Pulvinar afferent (secondary, modulatory; part of the
      right ventral attention network substrate)
    - V1 → V2 principal cortical target (the obligate relay)
    - **no direct V1 → V3 or V1 → V4 projections**
    - **V1 → V2 → V4 → LOC → right FFA pathway** (the right
      face-recognition pathway)
    - **V1 → V2 → MT/V5 pathway** (the dominant dorsal-stream
      motion input on the right)
    - callosal connections to the left V1 at the vertical
      meridian (V1/V2 border)
    - attentional feedback from the right FEF, right DLPFC,
      right IPS, right TPJ
[ ] CLINICAL_ANCHORS contains the fourteen right-specific anchors:
    - right_v1_left_homonymous_hemianopia
    - **macular_sparing_left**
    - cortical_blindness_bilateral
    - anton_syndrome
    - blindsight
    - **right_v1_left_hemifield_neglect_contribution**
    - **right_v1_contribution_to_prosopagnosia**
    - **hemianopic_alexia_left**
    - occipital_infarct_pca_territory
    - **right_ventral_attention_network_target**
    - migraine_visual_aura
    - occipital_epilepsy_visual_auras
    - posterior_cortical_atrophy
    - pres_visual_symptoms
[ ] The **left homonymous hemianopia** is documented as the
    primary right V1 anchor.
[ ] **Left macular sparing** is documented with its dual-blood-
    supply mechanism.
[ ] **Cortical blindness, Anton syndrome, and blindsight** are
    documented as the hemisphere-invariant bilateral-lesion
    syndromes.
[ ] **Left-hemifield neglect contribution** and **prosopagnosia
    contribution** are documented as **right-emphasized anchors**
    — **isolated right V1 lesions do not produce either**, but
    right V1 is part of the right ventral attention network
    substrate and the right face-pathway input stage respectively.
[ ] **Hemianopic alexia (left)** is documented as a right-side
    anchor that is **milder** than the left-side equivalent —
    the reading network itself (left VWFA) is intact.
[ ] **The right V1 does NOT produce alexia without agraphia** —
    that syndrome is left-only.
[ ] **The V1 ↔ BA 17 1:1 correspondence** is documented in
    ALTERNATE_NAMES and the cross-references to the right
    `..brodmann_areas.brodmann_area_17_primary_visual` — V1 and
    BA 17 are the same cortical territory described from two
    angles.
[ ] **The FUNCTIONAL_DOMAINS set is verified to be identical to
    the right BA 17's** — the 1:1 correspondence extends to the
    domains.
[ ] **The clinical anchors are verified to be the mirror of the
    left V1's** — left homonymous hemianopia, left macular
    sparing, left hemifield neglect contribution, prosopagnosia
    contribution, right ventral attention network target, and
    hemianopic alexia (left, milder) replace the left V1's
    right-sided equivalents and the left-only alexia without
    agraphia.
[ ] The **stria of Gennari**, the **four-component retinotopic
    map** (with LEFT hemifield labels), the **cuneus and lingual
    gyrus bank mapping** (lower LEFT / upper LEFT), and the **V1
    / V2 vertical meridian** are documented byte-identically to
    the left sibling's (except for the field label flip).
[ ] No forward-declaration caveat is needed. The lingual gyrus
    forward-reference caveat text is byte-identical to the left
    sibling's.
[ ] No SUBDIVISIONS promotion is performed while the BA 17
    functional counterpart under the right
    `...brodmann_areas/brodmann_area_17_primary_visual` is not
    yet split.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (V number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURE,
    BRODMANN_CORRELATES, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, forward-declaration caveat text) match the left
    sibling; VISUAL_HEMIFIELD, FUNCTIONAL_DOMAINS set (four on
    the right, three on the left), DOMAIN_EMPHASIS, CONNECTIVITY
    emphasis, and CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    V1 carries "left_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP; the left V1 carries "right_hemifield."
[ ] **The macular-sparing asymmetry is verified**: the right V1
    carries a **left** macular sparing anchor.
[ ] **The right-specific FUNCTIONAL_DOMAINS addition is verified**:
    `visual_attention_ventral_network_target` is present on the
    right and absent on the left. This is a **domain-set
    divergence**, not just a weighting divergence.
[ ] **The FUNCTIONAL_DOMAINS set is verified to match the right
    BA 17's** — the 1:1 correspondence extends to the domains on
    the right hemisphere.
[ ] **The right-only clinical anchors are verified**:
    `right_v1_left_hemifield_neglect_contribution`,
    `right_v1_contribution_to_prosopagnosia`,
    `right_ventral_attention_network_target`, and
    `hemianopic_alexia_left` are present on the right and absent
    on the left. The left-only
    `alexia_without_agraphia_left_v1_plus_splenium` anchor is
    absent on the right.
[ ] Any downstream code querying "what does the right V1 see?"
    must receive "the LEFT visual hemifield."
[ ] Any downstream code querying "what is V1?" must receive
    "the striate cortex / primary visual cortex / BA 17" — the
    1:1 V1 ↔ BA 17 correspondence is enforced.
[ ] Any downstream code assigning the right face pathway must
    route through the **right** V1 → V2 → V3 → V4 → LOC → right
    FFA chain — the right V1 is the input stage of the right
    face pathway, but it is **not** the face operation.
[ ] Any downstream code assigning the left reading pathway must
    route through the **left** V1 → V2 → V3 → V4 → LOC → left
    VWFA chain.
[ ] Any downstream code assigning left hemispatial neglect must
    note that **right V1 is a contributor**, not a sole cause —
    the lesion must extend to the right TPJ and right FEF for
    the full neglect syndrome.
[ ] **Any change to V1 must be mirrored to BA 17 in the same
    commit, in both hemispheres** — the 1:1 V1 ↔ BA 17
    correspondence requires the two packages to stay in lockstep.
"""