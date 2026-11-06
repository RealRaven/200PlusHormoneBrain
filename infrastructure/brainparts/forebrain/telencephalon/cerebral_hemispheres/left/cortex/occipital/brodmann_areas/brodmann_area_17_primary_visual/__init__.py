"""
Brodmann Area 17 (Primary Visual Cortex / Striate Cortex) — Left Hemisphere
============================================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── brodmann_areas
                                    └── brodmann_area_17_primary_visual   ← THIS PACKAGE

This is a **leaf cytoarchitectonic package** describing the left
hemisphere's **BA 17** — the **primary visual cortex (V1)**, also
called the **striate cortex** because of the architectonically visible
**stria of Gennari**. It is the **first and tightest** BA↔V
correspondence in the human cortex: **BA 17 is V1**, one-to-one, with
no residual. It is also the **first area Brodmann ever delineated**
(1909) — the stria of Gennari made it visible to the naked eye, and BA
17 became the model for the entire Brodmann scheme.

Parent: ``..brodmann_areas`` (left occipital BA registry) — sibling to
BA 18 and BA 19.

This package is the **structural mirror** of
``../../right/cortex/occipital/brodmann_areas/brodmann_area_17_primary_visual``.
The BA number, the V-area correlate (V1), the architectonic signature
(stria of Gennari), the calcarine-sulcus surface landmark, and the
retinotopic map are identical on both sides; the **functional
emphasis** and **clinical significance** diverge — on the left, BA 17
processes the **right** visual hemifield, and its ventral-stream
output feeds the left visual word form area (VWFA) via V2/V3/V4.

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
        **caudomedially** on the banks of the calcarine sulcus.

    Horizontal meridian → base of the calcarine sulcus
        The horizontal meridian is represented at the **fundus**
        (deepest part) of the calcarine sulcus.

**Left-hemisphere specificity**: the left BA 17 processes the **RIGHT**
visual hemifield of both eyes (contralateral processing). The
**right homonymous hemianopia** that follows a left V1 lesion is the
canonical left-lateralized visual-field deficit. On the left, BA 17 is
also the **input stage of the ventral stream that feeds the left
VWFA** — the reading pathway begins in the left V1 and terminates in
the left fusiform gyrus; this is why left V1 lesions can contribute to
reading deficits when the splenium is also involved (see the clinical
section).

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
            visual field. **On the left, the lower RIGHT field.**
        lingual gyrus — lower-bank V1
            The lingual gyrus (lower bank of the calcarine sulcus)
            carries the ventral V1 representation of the **upper**
            contralateral visual field. **On the left, the upper
            RIGHT field.** (Note: the lingual gyrus is a **forward
            reference** in ``..gyri`` — it is not yet a package.)
        calcarine sulcus — defining surface landmark
            The calcarine sulcus is the **defining sulcus** of BA 17
            and the surface landmark for V1's representation. The
            ``..sulci/calcarine_sulcus`` package declares BA 17 as
            its primary functional overlay.

**This field is structurally identical to the right sibling's** — the
architectonic neighbours and the cuneus / lingual-gyrus / calcarine
overlays are the same on both sides. What differs is the **visual
hemifield** — the left BA 17 processes the RIGHT hemifield, and the
cuneus / lingual gyrus representations carry the upper / lower RIGHT
field on the left.

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
    lingual gyrus (medial-surface          ventral bank of the calcarine
    gyrus; forward reference in ..gyri)    sulcus; the lower-bank V1
                                           representation of the
                                           **upper** visual field
    calcarine sulcus (defining sulcus)     the fundus of the sulcus
                                           represents the horizontal
                                           meridian; the banks
                                           represent the upper /
                                           lower fields

**This field is byte-identical to the left sibling's.** The adjacency
relationships are topological, not lateralized — the same BA 18 border,
the same cuneus / lingual-gyrus relationship, the same calcarine-sulcus
anatomy, on both sides.

--------------------------------------------------------------------------------
FUNCTIONAL DOMAINS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

BA 17 (= V1) participates in **three** canonical occipital functional
domains. The emphasis is as follows:

    primary_visual_processing                      (left emphasis — PRIMARY)
        **This is BA 17's defining contribution.** The first
        cortical stage of vision: orientation selectivity,
        ocular-dominance columns, spatial-frequency tuning, contrast
        sensitivity, edge detection, and retinotopic mapping. On the
        left, BA 17 processes the **RIGHT visual hemifield**;
        right homonymous hemianopia follows left V1 lesions.

    retinotopic_organization                       (left emphasis — PRIMARY)
        **This is BA 17's second primary contribution.** The
        topographic mapping of the **RIGHT visual hemifield** onto
        the left calcarine banks, with the fovea at the occipital
        pole and the periphery at the anterior calcarine banks. The
        left BA 17's retinotopic map is essentially a mirror image
        of the right BA 17's, with the field label flipped.

    binocular_vision                               (left emphasis — PRIMARY)
        Ocular-dominance columns and their convergence onto
        binocular cells support depth perception, stereopsis, and
        binocular fusion. On the left, binocular vision combines
        the right-eye and left-eye inputs to the **RIGHT visual
        hemifield**.

**Left-specific caveat on `color_vision`.** BA 17 is **not** the
color-vision area — that is V4, in BA 19. BA 17 has some wavelength
selectivity (via the koniocellular pathway from the LGN), but the
**conscious perception of color** emerges in V4 and the ventral
stream. `color_vision` is **omitted** from the BA 17
`FUNCTIONAL_DOMAINS` tuple; it appears in BA 19 (V4) instead.

**Left-specific caveat on `motion_perception`.** BA 17 is **not** the
motion area — that is V5/MT+, in BA 19. BA 17 has some direction
selectivity, but **conscious motion perception** emerges in MT/V5 and
the dorsal stream. `motion_perception` is **omitted** from the BA 17
`FUNCTIONAL_DOMAINS` tuple; it appears in BA 19 (MT/V5) instead.

**Left-specific caveat on `form_and_object_perception`.** BA 17
contributes to the **early stages** of form processing (edge
detection, contour integration), but **object recognition** emerges in
V4, the LOC, and the ventral stream. `form_and_object_perception` is
**omitted** from the BA 17 `FUNCTIONAL_DOMAINS` tuple; it appears in
BA 18 and BA 19 instead.

**Left-specific caveat on `visual_attention`.** BA 17 is a **target**
of top-down attentional modulation from the frontal eye fields (BA 8)
and the dorsolateral prefrontal cortex, but it is **not** itself an
attentional control area. The attentional contribution of BA 17 is
**modulatory** (gain control on V1 responses), not **generative**
(V1 does not direct attention). `visual_attention` is **omitted**
from the BA 17 `FUNCTIONAL_DOMAINS` tuple as a primary domain; the
attentional modulation of BA 17 is captured under the connectivity
section (feedback from FEF and DLPFC).

**Left-specific caveat on `visual_word_processing`.** BA 17 is the
**input stage** of the left ventral stream that feeds the left VWFA,
but BA 17 itself does **not** perform word processing. The VWFA is in
the left fusiform gyrus, several synapses downstream. `visual_word_
processing` is **omitted** from the BA 17 `FUNCTIONAL_DOMAINS` tuple;
the left BA 17 contributes to the pathway but is not the pathway's
operation.

**Left-specific caveat on `face_processing` and `global_visual_
processing`.** These are **right-lateralized** domains that the left
BA 17 does **not** carry. `face_processing` is instantiated in the
right FFA (fed by the right BA 17 ventral stream); `global_visual_
processing` is a distributed right-hemisphere property beginning at
right BA 18 (V2 / V3). Neither appears in the left BA 17
`FUNCTIONAL_DOMAINS` tuple.

**Summary**: BA 17 carries **exactly three** functional domains —
`primary_visual_processing`, `retinotopic_organization`, and
`binocular_vision`. It is the **most functionally specific** of the
occipital BA packages, in contrast to BA 18 (which adds form and
spatial localization) and BA 19 (which adds color, motion, form /
object, spatial, attention, and — on the left — the input to the
verbal-visual pathway). This is the architectural signature of the
**1:1 BA 17 ↔ V1 correspondence**: BA 17 is not a heterogeneous
territory spanning multiple functional areas, unlike BA 18 and BA 19.

--------------------------------------------------------------------------------
CONNECTIVITY
--------------------------------------------------------------------------------

    thalamic afferents
        → lateral geniculate nucleus (LGN), left
            **BA 17's primary and dominant thalamic afferent.**
            The LGN relays the visual signal from the left
            hemiretinas of both eyes (via the optic chiasm and the
            left optic tract). The LGN → V1 projection terminates
            in layer IV of the striate cortex — **layer IV is where
            the stria of Gennari runs**, and the LGN input is
            segregated into ocular-dominance columns that alternate
            between the left-eye and right-eye inputs. This is the
            anatomical substrate of the first cortical stage of
            vision.
        → pulvinar (secondary, modulatory)
            The pulvinar sends a weaker modulatory projection to
            BA 17 (and stronger projections to V2, V4, and MT),
            participating in the cortico-thalamo-cortical loops
            that support visual attention and visual short-term
            memory.
        → LGN feedback from layer VI
            BA 17 layer VI projects **back** to the LGN, forming
            the cortico-geniculate feedback loop that modulates
            the thalamic relay. This is a **top-down** modulation
            of the incoming visual signal, not a forward projection.

    cortical efferents
        → BA 18 (V2 and V3), left
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
            On the left, this pathway supports **right-hemifield**
            motion perception.
        → V4 (via BA 18 / V2, ventral stream)
            The color / form pathway (V1 → V2 → V4) carries the
            low-level form and wavelength signal from BA 17 to
            the color area. On the left, this pathway supports the
            **right-hemifield** color and form perception, and
            continues to the left VWFA for reading.

    callosal connections
        → right BA 17
            The callosal fibers connect the left BA 17 to the
            right BA 17 at the **vertical meridian** (the V1/V2
            border), where the two hemispheres' visual fields meet.
            This callosal connection is essential for the
            **fusion of the two hemifields** and for the
            **continuity of vision across the vertical midline**.
            Interruption of the callosal connections produces a
            **split-field** visual experience (the two hemifields
            become independently experienced, as in split-brain
            patients).

    attentional feedback
        → frontal eye fields (BA 8), left
            The FEF sends **top-down attentional gain** to BA 17,
            modulating the responsiveness of V1 neurons to
            behaviourally relevant stimuli.
        → dorsolateral prefrontal cortex (BA 9 / BA 46), left
            The DLPFC sends top-down attentional and working-memory
            signals to BA 17, supporting **visual working memory**
            and **visual imagery**.
        → intraparietal sulcus, left
            The IPS sends dorsal-attention-network signals to
            BA 17, supporting **spatial attention** in the RIGHT
            visual hemifield.

**This field is broadly conserved across hemispheres**, but the
**emphasis** differs on the left in two respects:
(a) the BA 17 → BA 18 → V4 → VWFA pathway is the **verbal-visual
pathway** that the left hemisphere dominates (reading);
(b) the callosal vertical-meridian connection carries the
**right-hemifield / left-hemifield fusion** signal, which on the left
is the **left half of the fused visual field**.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_ba17_right_homonymous_hemianopia
        **This is the left BA 17 anchor par excellence.** A lesion
        of the left BA 17 (or the left optic radiation, or the
        left LGN) produces a **right homonymous hemianopia** —
        loss of the right half of the visual field in both eyes.
        The deficit is **homonymous** (both eyes lose the same
        side), **hemianopic** (half the field is lost), and
        **contralateral** (right side from a left lesion). This is
        the single most common and most clinically consequential
        effect of a left V1 lesion.

    macular_sparing
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
        lesions** and is **less common** in optic-tract or
        chiasmal lesions (where the macular fibers travel with the
        peripheral fibers).

    cortical_blindness_bilateral
        **Bilateral BA 17 lesions** produce **cortical blindness** —
        complete loss of vision despite intact eyes, optic nerves,
        and LGN. The patient has no visual perception but may
        retain pupillary light reflexes (because the reflex arc
        goes through the pretectum and the Edinger-Westphal
        nucleus, not V1). Bilateral lesions can result from
        **bilateral PCA infarcts**, **hypoxic-ischemic
        encephalopathy**, **PRES (posterior reversible
        encephalopathy syndrome)**, or **trauma**.

    anton_syndrome
        **Anton syndrome** — **cortical blindness with denial of
        blindness** — is a rare complication of bilateral BA 17
        lesions. The patient is cortically blind but **insists that
        they can see**, and may confabulate visual experiences.
        The syndrome is thought to reflect a **disconnection
        between the visual cortex and the language / awareness
        networks**, and is more common with **bilateral occipital
        lesions involving the association cortex** in addition to
        BA 17 proper.

    blindsight
        **Blindsight** — residual visual function (detection,
        localization, and sometimes discrimination of stimuli) in
        the absence of conscious visual perception — is a
        well-documented phenomenon after **V1 lesions**. The
        residual function is mediated by **subcortical visual
        pathways** (the superior colliculus and the pulvinar, which
        project to MT/V5 and to the extrastriate cortex bypassing
        V1). **Blindsight is a direct demonstration that V1 is
        necessary for conscious vision but not for all visual
        processing.**

    hemianopic_alexia_right
        **Hemianopic alexia** — acquired reading impairment
        resulting from a **right homonymous hemianopia** (from a
        left BA 17 lesion) — is a recognized clinical entity. The
        patient's reading is slowed or impaired because they must
        make large **rightward saccades** to compensate for the
        missing right hemifield, and the **left-hemisphere reading
        network** (the left VWFA) cannot function efficiently
        without the full right-hemifield input. This is the
        **mildest form of alexia** and is often clinically
        under-recognized compared to the more severe alexia
        without agraphia.

    alexia_without_agraphia_left_occipital_plus_splenium
        **Alexia without agraphia** (Dejerine 1892) — the patient
        can **write** but cannot **read what they have written** —
        results from a **left occipital lesion that disconnects
        the intact right occipital cortex from the left language
        areas**. The classic lesion is **left PCA infarct
        (involving left BA 17 and the left splenium of the corpus
        callosum)**. The mechanism is: the right hemisphere can
        still see, but its visual signal cannot reach the left
        VWFA because the splenium is destroyed; the left VWFA has
        no visual input. The patient can write (because writing is
        a left-hemisphere motor program) but cannot read (because
        the left VWFA is disconnected from vision). **This is the
        canonical clinical demonstration that the left BA 17's
        contribution to reading is via the left VWFA, and that the
        callosal pathway is essential for the intact reading
        circuit.**

    migraine_visual_aura
        **Migraine visual aura** — the transient, typically
        bilateral, scintillating scotomata and fortification
        spectra that precede a migraine headache — reflects
        **cortical spreading depression** spreading across the
        **occipital cortex**, including BA 17. The phenomenon is
        not a lesion, but it is a **functional disturbance of
        BA 17**, and it is one of the most common clinical
        phenomena involving the primary visual cortex. On the
        left, the aura's visual field involvement is
        **contralateral (right)**, although the classic "fortification
        spectrum" is usually bilateral because the spreading
        depression is bilateral.

    occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** — elementary
        visual hallucinations (flashing lights, colored shapes,
        geometric patterns) in the **contralateral visual field** —
        is a well-characterized epilepsy syndrome. The auras arise
        from **epileptiform discharge in BA 17 (or BA 18)** and
        project to the **right visual field** when they arise from
        the left occipital cortex. The visual auras are typically
        **brief, stereotyped, and elementary** — not the complex,
        formed hallucinations of temporal lobe epilepsy.

    posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves **BA 17 and BA 18** bilaterally in
        later stages. Early stages affect the **dorsal (occipito-
        parietal) and ventral (occipito-temporal) association
        cortices** more than BA 17 proper, but the disease
        eventually involves the striate cortex and produces
        **cortical blindness**. PCA is a right-lateralized
        syndrome in its early stages (prosopagnosia, visuospatial
        deficits), but the left hemisphere's contributions to
        reading and object naming are affected as the disease
        progresses.

    pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — produces **cortical
        blindness, visual hallucinations, and hemianopia** from
        bilateral occipital involvement. The syndrome is
        **reversible** in most cases. Common triggers include
        hypertensive encephalopathy, eclampsia, and
        immunosuppressive therapy.

    occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** involving
        the left BA 17 produces **right homonymous hemianopia**,
        often with **macular sparing** (as described above), and
        can also produce the **alexia without agraphia** syndrome
        if the left splenium is involved. The left PCA territory
        includes the left calcarine cortex, the left lingual gyrus,
        and (via the posterior pericallosal artery) the left
        splenium. This is the most common single-lesion syndrome
        involving the left BA 17.

These anchors are **left-hemisphere-specific** in two senses:
(a) the left BA 17 processes the **RIGHT visual hemifield**, so left
BA 17 lesions produce **right-sided** visual deficits; (b) the left
BA 17 is the **input stage of the left reading pathway**, so left
BA 17 lesions can contribute to reading deficits (hemianopic alexia,
alexia without agraphia) that have no symmetric counterpart on the
right. The right sibling's docstring carries the corresponding
right-sided anchors (left homonymous hemianopia, prosopagnosia from
right occipito-temporal lesions, left hemispatial neglect from right
parietal + frontal lesions).

**The `macular_sparing`, `blindsight`, `Anton syndrome`, and
`cortical blindness` anchors are hemisphere-invariant** — they appear
on both sides and are documented identically in both siblings.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..brodmann_areas  (parent)
    The left occipital BA registry. This package's parent, source of
    the ``FUNCTIONAL_DOMAIN_EMPHASIS`` entry for BA 17 (which on the
    left is ``("primary_visual_processing",
    "retinotopic_organization", "binocular_vision")``), and enforcer
    of the **V1 ↔ BA 17 1:1 correspondence**.

..brodmann_area_18
    **Rostral neighbour** via the V1/V2 border. The BA 17 → BA 18
    projection is the first step of the V1 → V2 → V3 → V4 / MT+
    hierarchy. **The vertical meridian of the visual field is
    represented at the BA 17 / BA 18 border**, and the callosal
    connections between the left and right V1 meet at this border
    (in the BA 18 territory, not BA 17 proper, but the border is the
    functional landmark).

..brodmann_area_19
    Distant rostral / lateral neighbour; no direct adjacency (BA 18
    intervenes). BA 19 contains the color (V4) and motion (V5/MT+)
    areas; BA 17 does **not** claim those functions directly.

...cortex.primary_visual_cortex
    **The functional V1 package — the 1:1 counterpart of this BA
    package.** BA 17 and V1 are the **same cortical territory**
    described from two angles (cytoarchitectonic and
    functional-retinotopic). Downstream code should treat them as
    interchangeable identifiers and query either package for the
    same set of functional domains.

...cuneus
    The medial-surface gyral landmark. The cuneus's lower margin
    (the upper bank of the calcarine sulcus) carries the **dorsal
    V1 representation of the lower** contralateral visual field.
    **On the left, the lower RIGHT field.** The cuneus package
    cross-references BA 17 as its primary functional overlay.

...gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus (lower bank of the calcarine sulcus) carries
    the **ventral V1 representation of the upper** contralateral
    visual field. **On the left, the upper RIGHT field.** When the
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
    FFA). **On the left, the ventral stream terminates in the left
    VWFA** (the reading area), and the left BA 17 is the **input
    stage** of this pathway. The temporal package must declare the
    left BA 17 as the source of its visual input via the ventral
    stream, and must note the **left-lateralized VWFA
    specialization**.

..cortex.parietal
    The **dorsal stream** continues from BA 18 / BA 19 into the
    parietal lobe (intraparietal sulcus, area 7). **On the left,
    the dorsal stream supports right-hemifield spatial attention**
    via the left intraparietal sulcus. The parietal package must
    declare the left BA 17 as the source of its visual input for
    the dorsal stream via the BA 18 / BA 19 relay.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral prefrontal
    cortex** (BA 9 / BA 46) send top-down visual attentional
    signals to BA 17 via the BA 18 relay. The frontal package must
    declare the left BA 17 as a target of its attentional
    projections.

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
    primary visual thalamic relay to the left BA 17, and must note
    the LGN → V1 projection's role in the first cortical stage of
    vision.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a secondary, modulatory projection to BA
    17 (stronger to V2, V4, and MT), participating in the
    cortico-thalamo-cortical loops that support visual attention
    and visual short-term memory.

../../subcortical/medial_temporal_lobe/hippocampus
    The ventral stream terminates in the perirhinal, entorhinal,
    and parahippocampal cortices. **The left BA 17 is the input
    stage** of the occipito-temporal-hippocampal pathway that
    supports visual object recognition and visual memory. The
    hippocampus package must declare the left BA 17 as the source
    of its visual input via the BA 18 / BA 19 relay.

../../right/cortex/occipital/brodmann_areas/brodmann_area_17_primary_visual
    The right-hemisphere homologue. Structural fields (BA number,
    V-area correlate, architectonic signature, calcarine-sulcus
    surface landmark, retinotopic map, cuneus / lingual-gyrus
    relationship) MUST be byte-identical. Functional emphasis and
    clinical significance diverge — the right BA 17 processes the
    **LEFT** visual hemifield, and right BA 17 lesions produce
    **left** homonymous hemianopia. The right BA 17 is the input
    stage of the right ventral stream that feeds the right FFA,
    not the left VWFA.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    AREA_NAME           = "brodmann_area_17_primary_visual"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    BRODMANN_NUMBER     = 17
    ALTERNATE_NAMES     = ("striate_cortex",
                           "primary_visual_cortex_V1",
                           "V1")
        # **The 1:1 V-area correspondence is recorded in the
        # ALTERNATE_NAMES field** — BA 17 is V1, and downstream
        # code may refer to the territory by either name.

    ARCHITECTONIC_SIGNATURE = "stria_of_gennari"
        # The **only BA in the cortex tree where the architectonic
        # boundary is visible to the naked eye**. The stria of
        # Gennari is a band of myelinated axons through layer IV
        # and is the reason BA 17 was Brodmann's first area.

    V_AREA_CORRELATE    = ("primary_visual_cortex",)
        # **Exactly one** V area — the tightest BA↔V
        # correspondence in the cortex. Unlike BA 18 (V2 + V3) and
        # BA 19 (V3A + V4 + V5/MT+), BA 17 has no residual.

    NAMING_COLLISION_WITH = ()
        # **No naming collision.** BA 17 is unique to the occipital
        # lobe — it does not collide with any temporal, insular, or
        # frontal BA label.

    RETINOTOPIC_MAP     = "fovea_at_pole_contralateral_hemifield"
        # The fovea is at the occipital pole; the periphery is at
        # the anterior calcarine banks; the vertical meridian is at
        # the V1/V2 border; the horizontal meridian is at the
        # fundus of the calcarine sulcus. **On the left, the
        # represented hemifield is the RIGHT hemifield.**

    FUNCTIONAL_DOMAINS  = (
                              "primary_visual_processing",
                              "retinotopic_organization",
                              "binocular_vision",
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
                              # EXCLUDED as a primary domain (BA
                              # 17 is a *target* of attention, not
                              # a *generator*).
                              # NOTE: visual_word_processing is
                              # EXCLUDED (BA 17 is the input
                              # stage of the left reading pathway,
                              # not the reading operation).
                              # NOTE: face_processing and
                              # global_visual_processing are
                              # EXCLUDED (right-lateralized; not
                              # instantiated on the left BA 17).
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
                              "left_ba17_right_homonymous_"
                              "hemianopia",
                              "macular_sparing",
                              "cortical_blindness_bilateral",
                              "anton_syndrome",
                              "blindsight",
                              "hemianopic_alexia_right",
                              "alexia_without_agraphia_left_"
                              "occipital_plus_splenium",
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
this caveat should be updated.

--------------------------------------------------------------------------------
PROMOTION RULE (when a BA sub-field becomes a package)
--------------------------------------------------------------------------------

BA 17 is **architectonically homogeneous** — the stria of Gennari runs
continuously across the entire territory — and there is no natural
architectonic subdivision. The **one conceivable split** is the
**foveal (macular) representation vs the peripheral representation**,
since the fovea is enormously over-represented (cortical magnification
is roughly 100× in the fovea vs the periphery). If a future
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
  4. Mirror the promotion on the right side in the same commit.

**The foveal / peripheral split is a FUNCTIONAL subdivision, not an
architectonic one.** The stria of Gennari does not distinguish foveal
from peripheral V1 — the split reflects cortical magnification, not
cytoarchitecture. Any split must be documented as a *functional*
refinement of the parent BA 17, not as a new architectonic entity.
The parent remains the canonical answer to "what is BA 17?"; the
components refine *which part of BA 17* supports which retinal
eccentricity.

**No split should be performed while the V1 functional counterpart
under ``..cortex/primary_visual_cortex`` is not yet split.** The
BA 17 ↔ V1 1:1 correspondence means that any BA 17 split must be
mirrored by a corresponding V1 split, in the same commit, in both
hemispheres. Splitting BA 17 while V1 remains a single package would
break the 1:1 correspondence that is the defining structural feature
of this BA.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../brodmann_area_17_primary_visual``:

    MUST be identical (byte-for-byte):
        AREA_NAME                    "brodmann_area_17_primary_visual"
        LOBE                         "occipital"
        BRODMANN_NUMBER              17
        ALTERNATE_NAMES              ("striate_cortex",
                                     "primary_visual_cortex_V1",
                                     "V1")
        ARCHITECTONIC_SIGNATURE      "stria_of_gennari"
        V_AREA_CORRELATE             ("primary_visual_cortex",) —
                                     the 1:1 BA 17 ↔ V1
                                     correspondence is
                                     hemisphere-invariant
        NAMING_COLLISION_WITH        () — empty on both sides
        RETINOTOPIC_MAP              the same fovea-at-pole /
                                     eccentricity-gradient /
                                     vertical-meridian /
                                     horizontal-meridian structure
        Bounding / overlapping territories
        BA-to-neighbour adjacency
        CONNECTIVITY                 same bundle names; the LGN →
                                     V1 projection is the same; the
                                     callosal V1/V2-border
                                     connection is the same; the
                                     attentional feedback is the
                                     same
        FUNCTIONAL_DOMAINS set       the same three domains
                                     (primary_visual_processing,
                                     retinotopic_organization,
                                     binocular_vision), with the
                                     same exclusions

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        RETINOTOPIC_MAP        the **represented hemifield**
                               differs — left BA 17 processes
                               the RIGHT hemifield; right BA 17
                               processes the LEFT hemifield. The
                               map's *structure* is the same
                               (fovea at pole, eccentricity
                               gradient, etc.), but the *label*
                               of the represented hemifield is
                               flipped.
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
        CLINICAL_ANCHORS       left: right homonymous hemianopia;
                               hemianopic alexia; alexia without
                               agraphia (left BA 17 + splenium);
                               macular sparing (both sides, but
                               the left-lesion equivalent is
                               right macular sparing); plus the
                               hemisphere-invariant anchors
                               (cortical blindness, Anton
                               syndrome, blindsight, migraine
                               aura, occipital epilepsy,
                               posterior cortical atrophy,
                               PRES, occipital infarct).
                               right: left homonymous hemianopia;
                               prosopagnosia from right
                               occipito-temporal lesions; left
                               hemispatial neglect from right
                               parietal + frontal lesions;
                               left macular sparing; plus the
                               hemisphere-invariant anchors.

**The visual hemifield asymmetry is the sharpest single entry in this
contract.** Both hemispheres have the same BA 17, the same
architectonic signature, the same LGN input, and the same V1 → BA 18
hierarchy — but the *represented hemifield* is **flipped**. Left
BA 17 → right hemifield; right BA 17 → left hemifield. Any downstream
code that queries "what does the left BA 17 see?" must receive "the
right hemifield," and any downstream code that queries "what does the
right BA 17 see?" must receive "the left hemifield." Averaging the two
would erase the fundamental contralateral-visual-field organization.

**The macular-sparing asymmetry is subtle.** Macular sparing is a
hemisphere-invariant phenomenon (it follows occipital lesions on both
sides, because of the dual blood supply to the occipital pole), but
the *side of the spared macula* is determined by the side of the
lesion: a **left V1 lesion** produces a **right hemianopia with right
macular sparing**; a **right V1 lesion** produces a **left hemianopia
with left macular sparing**. The `CLINICAL_ANCHORS` entry on each
sibling names the side-appropriate sparing.

**The other hemisphere-invariant anchors** — cortical blindness
(bilateral), Anton syndrome (bilateral), blindsight (either side),
migraine aura, occipital epilepsy, posterior cortical atrophy, PRES,
and occipital infarct (the last with the side-appropriate field
label) — are **documented identically in both siblings** and must
not be allowed to drift.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] AREA_NAME is exactly "brodmann_area_17_primary_visual".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] BRODMANN_NUMBER is 17.
[ ] ALTERNATE_NAMES includes "striate_cortex",
    "primary_visual_cortex_V1", and "V1" — **the 1:1 V-area
    correspondence must be recorded** so downstream code can refer
    to the territory by either name.
[ ] ARCHITECTONIC_SIGNATURE is "stria_of_gennari" — the **only BA
    in the cortex tree where the architectonic boundary is visible
    to the naked eye**.
[ ] V_AREA_CORRELATE is exactly ``("primary_visual_cortex",)`` —
    the 1:1 correspondence, no residual.
[ ] NAMING_COLLISION_WITH is an empty tuple — BA 17 has no naming
    collision with any other lobe's BA numbers.
[ ] RETINOTOPIC_MAP is "fovea_at_pole_contralateral_hemifield" and
    the docstring documents the four sub-features:
    - fovea at the occipital pole
    - eccentricity gradient (fovea → anterior calcarine)
    - vertical meridian at the V1/V2 border
    - horizontal meridian at the fundus of the calcarine sulcus
    - **the represented hemifield is the RIGHT hemifield on the
      left side**
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
    domain (BA 17 is a *target*, not a *generator*).
[ ] FUNCTIONAL_DOMAINS **excludes** visual_word_processing (BA 17
    is the *input stage*, not the *operation*).
[ ] FUNCTIONAL_DOMAINS **excludes** face_processing and global_
    visual_processing (right-lateralized; not instantiated on the
    left BA 17).
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
    - BA 17 → BA 18 principal cortical target (the obligate
      relay through which V1 reaches V2, V3, V4, and MT/V5)
    - **no direct BA 17 → BA 19 projections** (the BA 18 relay is
      obligate)
    - callosal connections to the right BA 17 at the vertical
      meridian (V1/V2 border) — supporting fusion of the two
      hemifields
    - attentional feedback from the left FEF (BA 8), left DLPFC
      (BA 9 / BA 46), and left intraparietal sulcus
[ ] CLINICAL_ANCHORS contains the twelve left-specific anchors:
    - left_ba17_right_homonymous_hemianopia
    - macular_sparing
    - cortical_blindness_bilateral
    - anton_syndrome
    - blindsight
    - hemianopic_alexia_right
    - alexia_without_agraphia_left_occipital_plus_splenium
    - migraine_visual_aura
    - occipital_epilepsy_visual_auras
    - posterior_cortical_atrophy
    - pres_visual_symptoms
    - occipital_infarct_pca_territory
[ ] The **right homonymous hemianopia** is documented as the
    primary left BA 17 anchor — the canonical left-lateralized
    visual-field deficit.
[ ] **Macular sparing** is documented with its dual-blood-supply
    mechanism and the side-appropriate sparing (right macular
    sparing from a left lesion).
[ ] **Cortical blindness, Anton syndrome, and blindsight** are
    documented as the hemisphere-invariant bilateral-lesion
    syndromes, with the residual subcortical pathway (colliculus →
    pulvinar → MT/V5) as the blindsight substrate.
[ ] **Hemianopic alexia** and **alexia without agraphia** are
    documented as the left-lateralized reading deficits that arise
    because the left BA 17 is the input stage of the left reading
    pathway (left V1 → BA 18 → BA 19 → V4 → VWFA), and because the
    left splenium is the callosal relay for the intact right-
    hemifield visual signal.
[ ] The **BA 17 ↔ V1 1:1 correspondence** is documented explicitly
    in the ALTERNATE_NAMES field and in the cross-references to
    ``..cortex.primary_visual_cortex`` — BA 17 and V1 are the
    **same cortical territory** described from two angles.
[ ] The **stria of Gennari** is documented as the architectonic
    signature and the reason BA 17 was Brodmann's first area and
    the only BA visible to the naked eye.
[ ] The **calcarine sulcus** is documented as the defining sulcus
    and the surface landmark for V1, with the horizontal meridian
    at the fundus and the upper / lower fields on the two banks.
[ ] The **cuneus and lingual gyrus** are documented as the upper
    and lower banks of the calcarine sulcus, carrying the lower
    and upper contralateral field representations respectively
    (**lower RIGHT and upper RIGHT on the left side**).
[ ] The **BA 17 ↔ BA 18 vertical meridian** is documented as the
    representation of the vertical midline of the visual field,
    with the callosal connections to the right V1 meeting at this
    border.
[ ] No forward-declaration caveat is needed for the BA-side
    neighbours (BA 18, cuneus, calcarine sulcus, V1 all exist).
    The **lingual gyrus** is noted as a forward reference in
    ``..gyri`` and the placement question is documented.
[ ] No SUBDIVISIONS promotion is performed while the V1 functional
    counterpart under ``..cortex/primary_visual_cortex`` is not
    yet split — the 1:1 BA 17 ↔ V1 correspondence must be
    preserved.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (BA number, ALTERNATE_NAMES, ARCHITECTONIC_SIGNATURE,
    V_AREA_CORRELATE, NAMING_COLLISION_WITH, RETINOTOPIC_MAP
    structure, FUNCTIONAL_DOMAINS set) match the right sibling;
    the RETINOTOPIC_MAP's represented hemifield, DOMAIN_EMPHASIS,
    and CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    BA 17 carries "right_hemifield" in its DOMAIN_EMPHASIS entries
    and RETINOTOPIC_MAP; the right BA 17 carries "left_hemifield."
    Neither has been copied verbatim from the other.
[ ] **The macular-sparing asymmetry is verified**: the left BA 17
    carries a **right** macular sparing anchor (right hemianopia
    with right macular sparing); the right BA 17 carries a **left**
    macular sparing anchor (left hemianopia with left macular
    sparing).
[ ] Any downstream code querying "what does the left BA 17 see?"
    must receive "the RIGHT visual hemifield" — the
    contralateral-visual-field rule is enforced.
[ ] Any downstream code querying "what is BA 17?" must receive
    "V1 / primary visual cortex / striate cortex" — the 1:1
    BA 17 ↔ V1 correspondence is enforced through the
    ALTERNATE_NAMES and V_AREA_CORRELATE fields.
[ ] Any downstream code assigning the reading pathway must route
    through the **left** BA 17 → BA 18 → BA 19 → V4 → VWFA chain
    — the left BA 17 is the input stage, but it is **not** the
    reading operation, and no single BA claims `visual_word_
    processing` as a primary contribution.
[ ] Any downstream code assigning face processing must route
    through the **right** BA 17 → BA 18 → BA 19 → LOC → FFA chain
    — the right BA 17 is the input stage of the right face
    pathway, but it is **not** the face operation, and no
    occipital BA claims `face_processing` as a primary
    contribution.
"""