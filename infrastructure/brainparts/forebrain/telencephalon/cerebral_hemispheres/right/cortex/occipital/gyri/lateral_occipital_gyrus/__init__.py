"""
Lateral Occipital Gyrus — Right Hemisphere
===========================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── gyri
                                    └── lateral_occipital_gyrus   ← THIS PACKAGE

This is a **leaf gyral package** describing the right hemisphere's
**lateral occipital gyrus** — the **lateral-surface gyral fold** of
the occipital lobe, on the **lateral occipital convexity** between
the **parieto-occipital sulcus** (rostrally) and the **occipital
pole** (caudally). It is the **only lateral-surface gyrus of the
occipital lobe** that is modelled as a gyrus rather than as a V area,
and it is the **only child of the ``..gyri`` parent** in the current
tree.

Parent: ``..gyri`` (right occipital gyral registry) — the
**single-child parent**. Sibling to no other occipital gyral child
(the cuneus is a **parent-level sibling** of ``..gyri``, not a
child of it; the lingual gyrus is a forward reference).

This package is the **structural mirror** of
``../../left/cortex/occipital/gyri/lateral_occipital_gyrus``. The
gyrus name, the bounding sulci (parieto-occipital, transverse
occipital, lateral occipitotemporal), the functional overlays (V3d,
V4d, LOC, MT/V5), and the lateral-surface placement are identical on
both sides; the **functional emphasis** and **clinical
significance** diverge — on the right, the gyrus's **LOC territory
feeds the right FFA (face)** endpoint, and right
lateral-occipital-gyrus lesions produce **prosopagnosia**,
**visuospatial deficits**, and **left hemispatial neglect** (via the
LOC → right FFA and LOC → right IPS pathways). **The right lateral
occipital gyrus's V3d territory is the dominant motion-boundary and
depth-from-motion substrate** in the human brain. The left lateral
occipital gyrus's LOC feeds the **left VWFA (reading)** endpoint,
and left lateral-occipital-gyrus lesions produce **visual object
agnosia** (bilateral), **reading-related deficits**, and
**color-form processing deficits** via the LOC → left VWFA pathway.

**The lateral occipital gyrus is a gyral fold first and a functional
overlay second** — unlike the cuneus, which is a **surface landmark
for primary sensory cortex** first and a gyral fold second. This is
the structural reason the two gyri sit at different levels of the
tree (parent-level cuneus vs `..gyri` child lateral occipital
gyrus), and the two packages cross-reference each other with this
rationale. **This structural rationale is byte-identical to the left
sibling's** — it is a property of the occipital lobe's anatomy, not
of the hemisphere.

--------------------------------------------------------------------------------
WHAT THE LATERAL OCCIPITAL GYRUS IS
--------------------------------------------------------------------------------

The lateral occipital gyrus is the **lateral-surface gyral fold** of
the occipital lobe, on the **lateral occipital convexity**. It
occupies the full anteroposterior extent of the lateral surface,
from the **parieto-occipital sulcus** (rostrally) to the **occipital
pole** (caudally), and from the **temporal lobe** (ventrolaterally)
to the **parietal lobe** (dorsolaterally). It is bounded:

    rostrally   by the **parieto-occipital sulcus** (medially) /
                an imaginary line from the parieto-occipital sulcus
                to the **preoccipital notch** (laterally)
    caudally    by the **occipital pole** — the caudal convergence
                of the lateral occipital gyrus and the cuneus /
                lingual gyrus
    dorsally    by the **transverse occipital sulcus** — the dorsal
                boundary separating the lateral occipital gyri
                from the parietal lobe's angular gyrus
    ventrally   by the **lateral occipitotemporal sulcus** — the
                ventral boundary separating the lateral occipital
                gyri from the **fusiform gyrus**

**The lateral occipital gyri are sometimes subdivided** into
**superior**, **middle**, and **inferior** lateral occipital gyri
in some parcellations, but the current tree keeps them as a
**single gyrus package** because the **functional overlays are
continuous** across the three subdivisions.

**The lateral occipital gyrus is continuous with the fusiform
gyrus ventrally** — the gyrus transitions into the fusiform gyrus at
the **lateral occipitotemporal sulcus**. **On the right, the
fusiform gyrus is where the right FFA lives** (downstream of the
right LOC); the lateral occipital gyrus is the **upstream LOC
territory** that feeds the FFA. **The two together form the right
face-recognition pathway's lateral / ventral territory.**

**The lateral occipital gyrus's functional identity is defined by
its overlays**: V3d at the caudal / dorsal extent, V4d at the
mid / lateral extent, the LOC at the rostral extent, and MT/V5 at
the caudal margin. **It does NOT contain V1, V2, or the primary
sensory cortex** — those live on the medial surface (calcarine
banks, cuneus, lingual gyrus). **The lateral occipital gyrus is
purely extrastriate and association cortex.**

**Right-hemisphere specificity**: the right lateral occipital gyrus
represents the **left visual hemifield** via its V3d, V4d, and LOC
overlays. Its **LOC territory feeds the right FFA (face) pathway**
— the LOC → fusiform → right FFA chain is the right face-recognition
pathway, and the lateral occipital gyrus is its **upstream input
stage**. **Right lateral-occipital-gyrus lesions that extend into
the fusiform gyrus or the downstream right FFA produce
prosopagnosia** (impaired face recognition), **visuospatial
deficits**, and — via the right V3d → right MT/V5 → right IPS
pathway — **left hemispatial neglect** when the lesion extends into
the right parietal and right frontal territories. **The right lateral
occipital gyrus also carries the dominant motion-boundary and
depth-from-motion substrate** via its V3d territory, and right
lateral-occipital-gyrus lesions that extend into V3d produce **more
severe motion-boundary and depth-from-motion deficits** than the
left equivalent. **The right lateral occipital gyrus does NOT
produce reading-related deficits or visual object agnosia at the
same weighting** — those are the left lateral occipital gyrus's
contribution via the left LOC → left VWFA pathway.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Bounding sulci
        rostrally             **parieto-occipital sulcus** (medial)
                              / imaginary line to the preoccipital
                              notch (lateral)
        caudally              **occipital pole** — the caudal
                              convergence of the lateral occipital
                              gyrus and the cuneus / lingual gyrus
        dorsally              **transverse occipital sulcus** —
                              the dorsal boundary with the
                              parietal lobe's angular gyrus
        ventrally             **lateral occipitotemporal sulcus** —
                              the ventral boundary with the
                              fusiform gyrus

    Functional overlays
        tertiary_visual_cortex_v3d (V3d)          (CAUDAL / DORSAL)
            The **motion-boundary and motion-in-depth** area at
            the caudal / dorsal extent of the lateral occipital
            gyrus. **On the right, V3d is the DOMINANT motion
            substrate** — the right V3d → right MT/V5 → right
            IPS pathway is the dominant motion-boundary and
            dorsal-attention substrate, and the right lateral
            occipital gyrus's V3d territory is the more strongly
            engaged side.

        quaternary_visual_cortex_v4d (V4d)          (MID / LATERAL)
            The **color-form and surface-segmentation** area at
            the mid / lateral extent. **On the right, V4d feeds
            the right LOC → right FFA face pathway via its
            color-form output.**

        lateral_occipital_complex (LOC)              (ROSTRAL)
            The **object-recognition complex** at the rostral
            extent. **LOC is a forward reference** — not yet a
            package under ``..cortex``. **On the right, LOC
            feeds the right FFA (faces).** **LOC overlaps the
            lateral occipital gyrus** and extends into the
            fusiform gyrus.

        motion_area_v5_mt_plus (MT/V5)               (CAUDAL MARGIN)
            The **motion area** at the occipito-temporal junction
            near the caudal lateral occipital gyrus. **MT/V5 is a
            forward reference** — not yet a package. **On the
            right, MT/V5 is the DOMINANT motion hemisphere** —
            the right MT/V5 is more strongly engaged during
            coherent motion, motion-in-depth, and optic-flow
            processing than the left's.

**This field is structurally identical to the left sibling's** — the
bounding sulci and the four functional overlays (V3d, V4d, LOC,
MT/V5) are the same on both sides. What differs is the **visual
hemifield** — the right lateral occipital gyrus's overlays carry the
**left** hemifield — and the **downstream clinical emphasis** —
the right LOC → right FFA face pathway vs the left LOC → left VWFA
reading pathway.

--------------------------------------------------------------------------------
GYRUS-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    angular gyrus (parietal lobe)          **dorsal neighbour** via the
                                           **transverse occipital
                                           sulcus**.
    fusiform gyrus (temporal lobe;         **ventral neighbour** via the
    forward reference in ..gyri)           **lateral occipitotemporal
                                           sulcus**. **On the right,
                                           the fusiform gyrus is
                                           where the right FFA
                                           lives** (downstream of
                                           the right LOC).
    cuneus (medial surface)                **distant medial neighbour**
                                           via the occipital pole. The
                                           cuneus is a parent-level
                                           sibling of ``..gyri``, not
                                           a neighbour here.
    lingual gyrus (medial surface;         **distant medial neighbour**
    forward reference in ..gyri)           via the occipital pole.
    parieto-occipital sulcus               **rostral boundary**.
    transverse occipital sulcus            **dorsal boundary**.
    lateral occipitotemporal sulcus        **ventral boundary**.
    occipital pole                         **caudal boundary**.

**This field is byte-identical to the left sibling's** at the level of
sulcal and gyral neighbours. The adjacency relationships are
topological, not lateralized. The "right FFA" downstream note in the
fusiform gyrus entry is updated for the right hemisphere.

--------------------------------------------------------------------------------
FUNCTIONAL OVERLAYS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

The lateral occipital gyrus's functional identity is defined by its
**three principal overlays** plus the **MT/V5** at its caudal margin.
The right-side emphasis is:

    tertiary_visual_cortex_v3d (V3d)          (CAUDAL / DORSAL — DOMINANT)
        **The right lateral occipital gyrus's dominant overlay.**
        V3d is the **motion-boundary and motion-in-depth** area at
        the caudal / dorsal extent. **On the right, V3d is the
        DOMINANT motion substrate** — the right V3d → right MT/V5
        → right IPS pathway is the dominant motion-boundary and
        dorsal-attention substrate in the human brain. **Right
        lateral-occipital-gyrus lesions that extend into V3d
        produce more severe motion-boundary and depth-from-motion
        deficits** than the left equivalent.

    quaternary_visual_cortex_v4d (V4d)        (MID / LATERAL)
        **The right lateral occipital gyrus's mid / lateral
        overlay.** V4d is the **color-form and surface-
        segmentation** area at the mid / lateral extent. **On
        the right, V4d feeds the right LOC → right FFA face
        pathway via its color-form output.** The right lateral
        occipital gyrus's V4d contribution to **color-form
        integration** is part of the right hemisphere's
        **affective / face-linked color processing** — the
        right V4d → right LOC → right FFA chain contributes to
        **face-color integration** (the use of color in face
        recognition), and right lateral-occipital-gyrus lesions
        that extend into V4d can produce **color-form processing
        deficits** that contribute to prosopagnosia when the
        downstream right FFA is also affected.

    lateral_occipital_complex (LOC)           (ROSTRAL — PRIMARY)
        **The right lateral occipital gyrus's most clinically
        consequential overlay.** LOC is the **object-recognition
        complex** at the rostral extent. **LOC is a forward
        reference** — not yet a package under ``..cortex``. **On
        the right, LOC feeds the right FFA (faces) via the LOC
        → fusiform → right FFA pathway.** The right lateral
        occipital gyrus's LOC territory is the **upstream input**
        to the right face-recognition pathway, and right
        lateral-occipital-gyrus lesions that extend into the LOC
        territory can **contribute to prosopagnosia** (when the
        downstream fusiform gyrus and right FFA are also
        affected).

    motion_area_v5_mt_plus (MT/V5)            (CAUDAL MARGIN — DOMINANT)
        **The right lateral occipital gyrus's caudal margin.**
        MT/V5 is the **motion area** at the occipito-temporal
        junction. **MT/V5 is a forward reference** — not yet a
        package. **On the right, MT/V5 is the DOMINANT motion
        hemisphere** — the right MT/V5 is more strongly engaged
        during coherent motion, motion-in-depth, and optic-flow
        processing than the left's.

**Right-specific caveat on the face pathway.** The right lateral
occipital gyrus's **LOC → fusiform → right FFA pathway** is the
**right face-recognition pathway's upstream input stage**. **The
right lateral occipital gyrus is NOT the right FFA** — the FFA is
downstream in the fusiform gyrus. **The right lateral occipital
gyrus is the "what is this object?" object-recognition complex
that feeds the "whose face is this?" FFA.**

**Right-specific caveat on the reading pathway.** The right lateral
occipital gyrus does **not** carry a reading-processing overlay —
that is the left lateral occipital gyrus's contribution via the
left LOC → left VWFA pathway. **The right lateral occipital gyrus's
LOC feeds the right FFA (faces), not the left VWFA (reading).**

**Right-specific caveat on color-form-face integration.** The
right lateral occipital gyrus's V4d → right LOC → right FFA
pathway is part of the **face-color integration** substrate — the
use of color information in the right hemisphere's face-
recognition network. **Right lateral-occipital-gyrus lesions that
extend into V4d can produce color-form processing deficits** that
contribute to prosopagnosia when the downstream right FFA is
affected.

**Summary**: The lateral occipital gyrus's functional identity is
**dominated by the LOC** (the object-recognition complex at its
rostral extent), with **V4d** and **V3d** as mid and caudal
overlays, and **MT/V5** at the caudal margin. **The overlay set is
identical across hemispheres** — both lateral occipital gyri carry
V3d, V4d, LOC, and MT/V5. The right-left differences are:
(a) the **represented visual field** (right = left hemifield,
left = right hemifield);
(b) the **downstream network** (right LOC → right FFA faces;
left LOC → left VWFA reading);
(c) the **V3d weighting** (right V3d is dominant, left V3d is
weaker);
(d) the **LOC downstream target** (right FFA vs left VWFA).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_lateral_occipital_prosopagnosia_contribution
        **The right lateral occipital gyrus's most distinctive
        clinical anchor — and the mirror of the left's visual
        object agnosia anchor.** **Prosopagnosia** — impaired
        face recognition despite intact visual perception —
        typically results from **right occipito-temporal
        lesions** that involve the **right FFA** (in the right
        fusiform gyrus) or its **upstream input pathway** (the
        right lateral occipital gyrus's LOC). **Right lateral-
        occipital-gyrus lesions that extend into the LOC
        territory contribute to the apperceptive component**
        of prosopagnosia (the failure to form a coherent face
        percept from visual features). **Isolated right lateral
        occipital gyrus lesions that spare the downstream right
        FFA produce a milder face-recognition deficit**, because
        the right FFA itself is intact and can process the
        degraded input. **Prosopagnosia is the canonical
        right-lateralized visual-recognition deficit**, and
        right lateral-occipital-gyrus lesions are its upstream
        contributor. **This anchor has no symmetric counterpart
        on the left** — the left lateral occipital gyrus feeds
        the left VWFA reading pathway, not a face pathway.

    right_lateral_occipital_visuospatial_deficit
        **The right lateral occipital gyrus's visuospatial
        anchor.** The right lateral occipital gyrus's V3d and
        LOC territories contribute to visuospatial processing
        via their V3d → right MT/V5 → right IPS and LOC → right
        FFA pathways. **Right lateral-occipital-gyrus lesions
        can produce visuospatial deficits** — impaired spatial
        localization, impaired spatial attention, and impaired
        visuospatial working memory — **that are more severe
        than the left equivalent** because the right hemisphere
        is the dominant visuospatial hemisphere. **This anchor
        has no symmetric counterpart on the left at the same
        weighting** — the left lateral occipital gyrus's
        visuospatial contribution is subordinate to the left's
        language-linked object-recognition contribution.

    right_lateral_occipital_left_hemifield_neglect_contribution
        **Right-emphasized.** Right lateral-occipital-gyrus
        lesions that extend into the adjacent right V3d / right
        MT/V5 territory contribute to **left hemispatial
        neglect** when the lesion extends further into the
        right parietal and right frontal territories. **The
        right V3d → right MT/V5 → right IPS pathway is part of
        the right-lateralized dorsal attention network** that
        contributes to the neglect syndrome. **Isolated right
        lateral occipital gyrus lesions do not produce full
        neglect** — the patient has a left field defect or a
        left hemifield motion deficit but can attend to the
        left field cognitively — but the right lateral
        occipital gyrus's V3d territory is part of the
        neglect substrate. **This anchor has no symmetric
        counterpart on the left.**

    right_lateral_occipital_motion_boundary_deficit_more_severe
        **The right lateral occipital gyrus's dominant motion-
        overlay anchor.** The right lateral occipital gyrus's
        V3d territory contributes to **left-hemifield motion-
        boundary and depth-from-motion perception**. **Right
        lateral-occipital-gyrus lesions that extend into V3d
        produce more severe motion-boundary and depth-from-
        motion deficits** than the left equivalent — the right
        V3d is the dominant motion substrate.

    right_lateral_occipital_color_form_processing_deficit
        **The right lateral occipital gyrus's V4d-overlay
        anchor.** The right V4d → right LOC → right FFA pathway
        carries the **face-color integration** signal. **Right
        lateral-occipital-gyrus lesions that extend into V4d
        can produce color-form processing deficits** — the
        patient may still perceive colors and faces separately
        but cannot integrate them in a face-recognition
        context. **This anchor is a right-lateralized
        contributor** to the broader **right V4 face-color
        integration deficit** that is the right V4's most
        distinctive clinical syndrome.

    right_lateral_occipital_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including the **lateral occipital gyrus's V4d
        and LOC territory**. **The lateral occipital gyrus
        contribution is the propagation of the aura into
        color-defined and object-form features** — colored
        fortifications, chromatic scotomata, and **formed object
        hallucinations** in the left hemifield. **This anchor
        is hemisphere-invariant**, but the field involvement is
        contralateral (left field on the right side).

    right_lateral_occipital_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from the lateral occipital gyrus's V4d and LOC
        territory. **Lateral-occipital-gyrus auras** are
        typically **more complex than V1 / V2 / V3 auras** —
        the patient may see **formed objects, colored scenes,
        or recognizable shapes** in the left visual field.

    right_lateral_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct** can
        involve the lateral occipital gyrus and produce a
        **left hemianopia or quadrantic defect** (from V1 /
        V2 / V3 involvement) **plus** a **left hemiachromatopsia**
        (from V4d involvement) **plus** a **prosopagnosia
        contribution** (from LOC → right FFA involvement) when
        the lesion extends sufficiently. **Isolated right PCA
        infarcts do not produce alexia without agraphia** —
        that syndrome is left-lateralized. **The lateral
        occipital gyrus's contribution is the downstream face-
        recognition component** on top of the primary field
        defect.

    right_lateral_occipital_posterior_cortical_atrophy_benson_syndrome
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves the **lateral occipital gyrus's
        V4d and LOC territory** in early-stage PCA. **Right
        lateral occipital gyrus** is part of the substrate of
        the **progressive dorsal / ventral stream dysfunction**
        that produces **Benson syndrome** — progressive
        prosopagnosia, visuospatial deficits, optic ataxia,
        simultanagnosia. **On the right, PCA presents with the
        visuospatial / prosopagnosic syndrome**; on the left,
        with the progressive reading deficits.

    right_lateral_occipital_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — can involve the
        lateral occipital gyrus and produce **cortical blindness,
        visual hallucinations, and quadrantic field defects**
        from **bilateral occipital involvement**. **The lateral
        occipital gyrus contribution** is the **object-form
        and color hallucinations** (LOC and V4d hyperexcitability)
        beyond the elementary features of V1 / V2. **The
        syndrome is reversible** in most cases.

**The lateral-occipital-gyrus-specific clinical anchors** —
`right_lateral_occipital_prosopagnosia_contribution`,
`right_lateral_occipital_visuospatial_deficit`,
`right_lateral_occipital_left_hemifield_neglect_contribution`,
`right_lateral_occipital_motion_boundary_deficit_more_severe`,
and `right_lateral_occipital_color_form_processing_deficit` — are
the **right-emphasized mirror** of the left lateral occipital gyrus
anchors. **The prosopagnosia contribution and the visuospatial
deficit are right-lateralized** (the right lateral occipital gyrus
feeds the right face pathway and the right visuospatial network);
the **motion-boundary deficit is more severe on the right** (the
right V3d is dominant); the **neglect contribution is right-only**
(via the right V3d → MT/V5 → right IPS pathway); the **color-form
processing deficit is a right-lateralized contributor** to the
broader right V4 face-color syndrome.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**, with the side-appropriate field label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri  (parent)
    The right occipital gyral registry — the **single-child
    parent**. The lateral occipital gyrus is its **only child**
    in the current tree.

..occipital
    The **parent-level sibling** of ``..gyri``. The occipital
    lobe parent.

..brodmann_areas.brodmann_area_19
    The **cytoarchitectonic sibling** of the lateral occipital
    gyrus. The lateral occipital gyrus overlaps **BA 19**. The
    BA 19 package must declare the right lateral occipital
    gyrus as its primary **lateral-surface anatomical
    substrate**.

...cortex.v3  (V3d)
    The **functional sibling** of the lateral occipital
    gyrus's caudal / dorsal overlay. **On the right, V3d is the
    DOMINANT motion substrate.** The V3 package must declare the
    right lateral occipital gyrus as one of its **lateral-
    surface anatomical substrates**.

...cortex.v4  (V4d)
    The **functional sibling** of the lateral occipital
    gyrus's mid / lateral overlay. **On the right, V4d feeds
    the right LOC → right FFA face pathway.**

...cortex.loc  (forward reference)
    The **functional sibling** of the lateral occipital
    gyrus's rostral overlay. **LOC is a forward reference** —
    not yet a package under ``..cortex``. **On the right, LOC
    feeds the right FFA (faces).**

...cortex.v5_mt_plus  (forward reference)
    The **functional sibling** of the lateral occipital
    gyrus's caudal margin. **MT/V5 is a forward reference** —
    not yet a package. **On the right, MT/V5 is the DOMINANT
    motion hemisphere.**

..cuneus
    The **medial-surface sibling** (parent-level sibling of
    ``..gyri``, not a child of the lateral occipital gyrus).
    The cuneus is the **upper bank of the calcarine sulcus**;
    the lateral occipital gyrus is the **lateral surface of
    the occipital lobe**. The two gyri sit at different levels
    of the tree.

..gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus is a **forward reference** in ``..gyri``.
    When it is created, its placement must **preserve the
    cuneus / lingual gyrus symmetry**.

..sulci.calcarine_sulcus
    The **calcarine sulcus is NOT a boundary of the lateral
    occipital gyrus** — it is the boundary of the cuneus and
    lingual gyrus.

..sulci.transverse_occipital_sulcus
    The **dorsal boundary** of the lateral occipital gyri,
    separating them from the parietal lobe's angular gyrus.

..sulci.parieto_occipital_sulcus
    The **rostral boundary** of the lateral occipital gyrus.

..sulci.lateral_occipitotemporal_sulcus  (forward reference, if
    not yet a package)
    The **ventral boundary** of the lateral occipital gyrus,
    separating it from the fusiform gyrus. **On the right, the
    fusiform gyrus is downstream of the lateral occipital
    gyrus's LOC territory** (right FFA).

..cortex.temporal
    The **ventral stream** continues from the lateral occipital
    gyrus's LOC territory into the temporal lobe (fusiform
    gyrus, right FFA). **On the right, the lateral occipital
    gyrus's LOC → fusiform → right FFA pathway is the face
    pathway.** **Right occipito-temporal lesions produce
    prosopagnosia** — the canonical right-lateralized
    visual-recognition deficit. The temporal package must
    declare the right lateral occipital gyrus as a **source
    of upstream LOC input** to its right fusiform gyrus
    children, and must note the **right-lateralized FFA
    specialization**.

..cortex.parietal
    The **dorsal stream** continues from the lateral occipital
    gyrus's V3d territory (via MT/V5 → IPS) into the parietal
    lobe. **On the right, the lateral occipital gyrus's V3d
    contribution is the DOMINANT dorsal-attention substrate.**
    The parietal package must declare the right lateral
    occipital gyrus as a **source of upstream V3d input** to
    its dorsal attention network children.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral
    prefrontal cortex** (BA 9 / BA 46) send top-down visual
    attentional signals to the lateral occipital gyrus's V3d /
    V4d territory. **On the right, the right FEF is the
    dominant node of the ventral attention network**, and right
    frontal lesions contribute to left hemispatial neglect.

..cortex.cingulate  — indirect
    No direct cingulate → lateral occipital gyrus projection.

..cortex.insular  — indirect
    No direct insular → lateral occipital gyrus projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the **indirect** source of the lateral
    occipital gyrus's V3d / V4d input via the V1 → V2 → V3 → V4
    relay.

../../subcortical/diencephalon/thalamus/pulvinar
    The pulvinar sends a **strong modulatory projection** to the
    lateral occipital gyrus's V3d / V4d territory.

../../subcortical/medial_temporal_lobe/hippocampus
    The lateral occipital gyrus's LOC output reaches the
    hippocampus via the ventral stream (LOC → fusiform →
    perirhinal → hippocampus). **On the right, the
    parahippocampal place area (PPA) and the retrosplenial
    complex receive visual input supporting scene and spatial
    memory**, which are more strongly right-lateralized.

../../left/cortex/occipital/gyri/lateral_occipital_gyrus
    The left-hemisphere homologue. Structural fields (gyrus
    name, bounding sulci, V3d / V4d / LOC / MT/V5 overlays,
    lateral-surface placement, cuneus-sibling note) MUST be
    byte-identical. Functional emphasis and clinical
    significance diverge — the left lateral occipital gyrus's
    LOC feeds the **left VWFA (reading)** endpoint, and left
    lateral-occipital-gyrus lesions produce **visual object
    agnosia** (bilateral), **reading-related deficits**, and
    **color-form processing deficits** via the LOC → left VWFA
    pathway.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "lateral_occipital_gyrus"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    ALTERNATE_NAMES     = ("lateral_occipital_gyri",
                           "lateral_occipital_convexity",
                           "gyrus_occipitalis_lateralis")
        # **Byte-identical to the left sibling's.**

    BOUNDING_SULCI      = {
                              "rostral":   ("parieto_occipital_"
                                            "sulcus",),
                              "caudal":    ("occipital_pole",),
                              "dorsal":    ("transverse_occipital_"
                                            "sulcus",),
                              "ventral":   ("lateral_occipito_"
                                            "temporal_sulcus",),
                          }
        # **Byte-identical to the left sibling's.**

    FUNCTIONAL_OVERLAYS = (
                              "tertiary_visual_cortex_v3d",
                              "quaternary_visual_cortex_v4d",
                              "lateral_occipital_complex",
                              "motion_area_v5_mt_plus",
                          )
        # **Byte-identical to the left sibling's.**

    PRIMARY_OVERLAY     = "lateral_occipital_complex"
        # **Byte-identical to the left sibling's.** The LOC is
        # the lateral occipital gyrus's defining functional
        # contribution at its rostral extent.

    REPRESENTED_FIELD   = "contralateral"
        # **On the right, the lateral occipital gyrus carries
        # the LEFT visual hemifield.**

    VISUAL_HEMIFIELD    = "left"
        # **The represented visual hemifield** — right lateral
        # occipital gyrus carries the left hemifield.

    RIGHT_LATERALIZED_FUNCTIONS = (
        "left_hemifield_loc_to_right_ffa",
    )
        # The right lateral occipital gyrus's LOC feeds the
        # right FFA face pathway. **This is the mirror of the
        # left's `LEFT_LATERALIZED_FUNCTIONS`
        # `right_hemifield_loc_to_left_vwfa`.**

    LEFT_ONLY_DOMAINS   = (
        "right_hemifield_loc_to_left_vwfa",
    )
        # The left-only function that the right lateral
        # occipital gyrus does **not** carry. **This is the
        # mirror of the left's `RIGHT_ONLY_DOMAINS`
        # `face_processing`.**

    LATERALIZATION_NOTE = "lateral_surface_gyral_fold_with_LOC_object_recognition_overlay"
        # **Byte-identical to the left sibling's.**

    CUNEUS_SIBLING_NOTE = (
        "The cuneus is a parent-level sibling of this package's "
        "parent (..gyri), not a sibling of this package. The "
        "cuneus sits at the ..occipital parent level because "
        "its primary functional identity is the V1 upper-bank "
        "surface landmark. See ..cuneus and ..gyri."
    )
        # **Byte-identical to the left sibling's.**

    __all__ = [
        "GYRUS_NAME",
        "HEMISPHERE",
        "LOBE",
        "ALTERNATE_NAMES",
        "BOUNDING_SULCI",
        "FUNCTIONAL_OVERLAYS",
        "PRIMARY_OVERLAY",
        "REPRESENTED_FIELD",
        "VISUAL_HEMIFIELD",
        "RIGHT_LATERALIZED_FUNCTIONS",
        "LEFT_ONLY_DOMAINS",
        "LATERALIZATION_NOTE",
        "CUNEUS_SIBLING_NOTE",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references the lateral occipital gyrus lives in
``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There are four forward references for this package**, and they
are the **V-area overlays** that live in ``..cortex``:

1. **V3d** — motion-boundary and motion-in-depth area at the
   caudal / dorsal extent. **On the right, V3d is the DOMINANT
   motion substrate.**
2. **V4d** — color-form and surface-segmentation area at the
   mid / lateral extent. **On the right, V4d feeds the right
   LOC → right FFA face pathway.**
3. **LOC** — object-recognition complex at the rostral extent.
   **On the right, LOC feeds the right FFA (faces).**
4. **MT/V5** — motion area at the caudal margin. **On the right,
   MT/V5 is the DOMINANT motion hemisphere.**

**When they are created under ``..cortex``, they must
cross-reference the right lateral occipital gyrus as one of their
lateral-surface anatomical substrates**, in the same commit, in
both hemispheres.

**On the right, resolving MT/V5 and V3d is the most urgent future
V-area work** — they are the dominant motion and dorsal-attention
substrates in the human brain, and the right lateral occipital
gyrus's V3d contribution is only fully characterised when those
areas are modelled. **Resolving LOC is required for the right face-
recognition pathway's occipital input to be fully characterised**,
because the right LOC → right FFA pathway is the substrate of the
prosopagnosia contribution anchor.

**All forward references are byte-identical to the left sibling's.**
**The right's emphasis note on V3d and MT/V5 dominance is
byte-identical to the right `..gyri` parent's forward-reference
caveat.**

--------------------------------------------------------------------------------
PROMOTION RULE (when a lateral occipital sub-region becomes a
package)
--------------------------------------------------------------------------------

The lateral occipital gyrus is **architectonically continuous**
across its anteroposterior extent. **The one natural split is the
superior / middle / inferior lateral occipital gyrus triad.**

**If a future parcellation promotes the three-way split**, the
promotion takes this form:

    lateral_occipital_gyrus/
        __init__.py
        superior_lateral_occipital_gyrus/    # V3d
            __init__.py
        middle_lateral_occipital_gyrus/      # V4d
            __init__.py
        inferior_lateral_occipital_gyrus/    # LOC
            __init__.py

Then:

  1. Add the three component names to this package's
     ``SUBDIVISIONS``.
  2. Update this package's ``FUNCTIONAL_OVERLAYS`` to reflect the
     per-subdivision overlays (superior → V3d, middle → V4d,
     inferior → LOC).
  3. Update the parent ``..gyri``'s ``GYRI_TO_V_OVERLAYS`` index
     accordingly.
  4. Mirror the promotion on the left side in the same commit.

**On the right, the V3d subdivision is the dominant motion
substrate**, and the LOC subdivision is the upstream input to the
right FFA face pathway. **The right V3d subdivision carries the more
severe motion-boundary deficit anchor**, and the right LOC
subdivision carries the prosopagnosia contribution anchor. The right
V4d subdivision carries the face-color integration deficit anchor.

**The split is BLOCKED while LOC and MT/V5 are unresolved** — the
two most clinically consequential overlays on the right are not yet
packages under ``..cortex``.

**The split preserves the cuneus / lateral occipital gyrus
distinction** — the cuneus remains a parent-level sibling, not a
subdivision of the lateral occipital gyrus.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../lateral_occipital_gyrus``:

    MUST be identical (byte-for-byte):
        GYRUS_NAME                   "lateral_occipital_gyrus"
        LOBE                         "occipital"
        ALTERNATE_NAMES              ("lateral_occipital_gyri",
                                     "lateral_occipital_
                                     convexity",
                                     "gyrus_occipitalis_
                                     lateralis")
        BOUNDING_SULCI               parieto-occipital (rostral),
                                     occipital pole (caudal),
                                     transverse occipital
                                     (dorsal), lateral
                                     occipitotemporal (ventral)
        FUNCTIONAL_OVERLAYS          V3d, V4d, LOC, MT/V5
        PRIMARY_OVERLAY              "lateral_occipital_complex"
        REPRESENTED_FIELD            "contralateral"
        LATERALIZATION_NOTE          "lateral_surface_gyral_fold_
                                     with_LOC_object_recognition_
                                     overlay"
        CUNEUS_SIBLING_NOTE          byte-identical
        The lateral-surface placement (child of ``..gyri``)
        The bounding sulci

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        RIGHT_LATERALIZED_FUNCTIONS
                               right: ("left_hemifield_loc_to_
                               right_ffa",) — the right LOC
                               feeds the right FFA face
                               pathway.
                               left: () — the left LOC does not
                               contribute to the right face
                               pathway.
        LEFT_ONLY_DOMAINS      right: ("right_hemifield_loc_to_
                               left_vwfa",) — the left-only
                               function the right LOC does not
                               carry.
                               left: () — the left LOC uses
                               RIGHT_ONLY_DOMAINS instead.
        CLINICAL_ANCHORS       right: **prosopagnosia
                               contribution**, **visuospatial
                               deficit**, **left hemispatial
                               neglect contribution** (via
                               LOC → right IPS), **more severe
                               motion-boundary deficit** (V3d
                               dominant), color-form processing
                               deficit (V4d), migraine aura,
                               occipital epilepsy, occipital
                               infarct, PCA (Benson syndrome),
                               PRES.
                               left: visual object agnosia
                               (bilateral), reading-related
                               deficit, color-form processing
                               deficit (V4d), motion-boundary
                               deficit (milder), migraine aura,
                               occipital epilepsy, occipital
                               infarct, PCA, PRES.

**The visual-hemifield asymmetry is the sharpest single entry.**
The right lateral occipital gyrus's overlays represent the **left**
hemifield; the left's represent the **right** hemifield.

**The reading-vs-face downstream asymmetry is the second sharpest
entry.** The right lateral occipital gyrus's LOC feeds the **right
FFA face** endpoint; the left's feeds the **left VWFA reading**
endpoint. The `RIGHT_LATERALIZED_FUNCTIONS` / `LEFT_ONLY_DOMAINS`
tuples make this explicit, and the two contributions are
mirror-opposite.

**The right-specific clinical anchors are the third sharpest
entry.** The right lateral occipital gyrus carries three anchors
that the left does not carry at the same weighting:
`right_lateral_occipital_prosopagnosia_contribution`,
`right_lateral_occipital_visuospatial_deficit`, and
`right_lateral_occipital_left_hemifield_neglect_contribution`. The
right also carries the **more severe** motion-boundary deficit (the
right V3d is the dominant motion substrate). The left carries the
mirror `left_lateral_occipital_reading_related_deficit` and
`left_lateral_occipital_visual_object_agnosia` anchors.

**The complementarity invariant is verified across schemes.** The
left's `LEFT_LATERALIZED_FUNCTIONS` (mirror) equals the right's
`RIGHT_LATERALIZED_FUNCTIONS`, and the left's `RIGHT_ONLY_DOMAINS`
(mirror) equals the right's `LEFT_ONLY_DOMAINS`.

**The overlay set (V3d, V4d, LOC, MT/V5), the bounding sulci, the
PRIMARY_OVERLAY, the LATERALIZATION_NOTE, the CUNEUS_SIBLING_NOTE,
and the lateral-surface placement are byte-identical on both
sides.**

**The cuneus-sibling note is byte-identical on both sides** and
must not be allowed to drift.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "lateral_occipital_gyrus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's.
[ ] BOUNDING_SULCI is byte-identical to the left sibling's.
[ ] FUNCTIONAL_OVERLAYS is byte-identical to the left sibling's
    (V3d, V4d, LOC, MT/V5).
[ ] PRIMARY_OVERLAY is "lateral_occipital_complex".
[ ] REPRESENTED_FIELD is "contralateral" — **on the right, the
    lateral occipital gyrus carries the LEFT visual hemifield**.
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class
    field.
[ ] **The lateral-surface placement is documented** — child of
    ``..gyri``, **not** a parent-level sibling like the cuneus.
[ ] **The cuneus-sibling note is documented** — the cuneus is a
    **parent-level sibling of ``..gyri``**, and the reason is
    byte-identical to the left sibling's.
[ ] **The lateral occipital gyrus is a gyral fold first, not a
    surface landmark for primary sensory cortex** — the
    docstring explicitly contrasts it with the cuneus.
[ ] **RIGHT_LATERALIZED_FUNCTIONS** contains
    "left_hemifield_loc_to_right_ffa" — the right lateral
    occipital gyrus's LOC feeds the right FFA face pathway.
[ ] **LEFT_ONLY_DOMAINS** contains
    "right_hemifield_loc_to_left_vwfa" — the left-only function
    the right lateral occipital gyrus does **not** carry.
[ ] **The complementarity invariant is verified**: left's
    `LEFT_LATERALIZED_FUNCTIONS` (mirror) equals right's
    `RIGHT_LATERALIZED_FUNCTIONS`; left's `RIGHT_ONLY_DOMAINS`
    (mirror) equals right's `LEFT_ONLY_DOMAINS`.
[ ] LATERALIZATION_NOTE is
    "lateral_surface_gyral_fold_with_LOC_object_recognition_
    overlay" — byte-identical to the left sibling's.
[ ] CUNEUS_SIBLING_NOTE is present and byte-identical to the
    left sibling's.
[ ] CLINICAL_ANCHORS contains the right-specific anchors:
    - **right_lateral_occipital_prosopagnosia_contribution**
    - **right_lateral_occipital_visuospatial_deficit**
    - **right_lateral_occipital_left_hemifield_neglect_
      contribution**
    - **right_lateral_occipital_motion_boundary_deficit_more_
      severe**
    - right_lateral_occipital_color_form_processing_deficit
    - right_lateral_occipital_migraine_visual_aura
    - right_lateral_occipital_occipital_epilepsy_visual_auras
    - right_lateral_occipital_infarct_pca_territory
    - right_lateral_occipital_posterior_cortical_atrophy_benson_
      syndrome
    - right_lateral_occipital_pres_visual_symptoms
[ ] The **prosopagnosia contribution** is documented as the
    primary right lateral occipital gyrus anchor — the mirror of
    the left's visual object agnosia anchor.
[ ] The **visuospatial deficit** is documented as a
    right-lateralized anchor — the right is the dominant
    visuospatial hemisphere.
[ ] The **left hemifield neglect contribution** is documented as
    a right-emphasized anchor (via the right V3d → MT/V5 → right
    IPS dorsal attention pathway).
[ ] The **more severe motion-boundary deficit** is documented
    (right V3d is dominant).
[ ] The **color-form processing deficit** is documented as a
    V4d-overlay anchor and a **right-lateralized contributor**
    to the broader right V4 face-color integration syndrome.
[ ] **The lateral occipital gyrus is explicitly NOT the right
    FFA** — the FFA is downstream in the fusiform gyrus. The
    lateral occipital gyrus's LOC is the "what is this object?"
    stage; the FFA is the "whose face is this?" stage.
[ ] **The lateral occipital gyrus does NOT produce
    reading-related deficits or visual object agnosia at the
    same weighting** — those are the left lateral occipital
    gyrus's contribution via the left LOC → left VWFA pathway.
[ ] **The lateral occipital gyrus → fusiform gyrus continuity**
    is documented — **on the right, the fusiform gyrus's FFA is
    downstream of the lateral occipital gyrus's LOC.**
[ ] **The transverse occipital sulcus** is documented as the
    dorsal boundary.
[ ] **The lateral occipitotemporal sulcus** is documented as
    the ventral boundary.
[ ] **The parieto-occipital sulcus** is documented as the
    rostral boundary.
[ ] **The calcarine sulcus is explicitly NOT a boundary of the
    lateral occipital gyrus.**
[ ] **The LOC and MT/V5 forward references are documented** —
    they live in ``..cortex`` as V-area forward references.
    **When they are created, they must cross-reference the
    right lateral occipital gyrus as one of their
    lateral-surface anatomical substrates.**
[ ] No forward-declaration caveat is needed for the lateral
    occipital gyrus's structural fields. The **lingual gyrus
    forward reference** and the **cuneus parent-level sibling**
    are documented via the CUNEUS_SIBLING_NOTE and the parent
    package's caveat.
[ ] No SUBDIVISIONS promotion is performed while LOC and MT/V5
    are unresolved.
[ ] The **promotion rule for the three-way lateral occipital
    gyrus split** is documented, with the joint ``..cortex``
    update requirement, the right-specific anchor allocation
    (V3d → more severe motion deficit, LOC → prosopagnosia,
    V4d → face-color integration), and the downstream LOC /
    MT/V5 prerequisites.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (GYRUS_NAME, LOBE, ALTERNATE_NAMES, BOUNDING_SULCI,
    FUNCTIONAL_OVERLAYS, PRIMARY_OVERLAY, REPRESENTED_FIELD,
    LATERALIZATION_NOTE, CUNEUS_SIBLING_NOTE, lateral-surface
    placement) match the left sibling; VISUAL_HEMIFIELD,
    RIGHT_LATERALIZED_FUNCTIONS, LEFT_ONLY_DOMAINS, and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    lateral occipital gyrus carries "left_hemifield"; the left
    carries "right_hemifield."
[ ] **The reading-vs-face downstream asymmetry is verified**:
    the right lateral occipital gyrus carries "left_hemifield_
    loc_to_right_ffa" and the left carries "right_hemifield_
    loc_to_left_vwfa" — the two are mirror-opposite.
[ ] **The right-specific clinical anchors are verified**:
    `right_lateral_occipital_prosopagnosia_contribution`,
    `right_lateral_occipital_visuospatial_deficit`,
    `right_lateral_occipital_left_hemifield_neglect_
    contribution`, and the **more severe** motion-boundary
    deficit are present on the right and absent on the left.
    The left-only
    `left_lateral_occipital_reading_related_deficit` and
    `left_lateral_occipital_visual_object_agnosia` are absent
    on the right.
[ ] Any downstream code querying "what does the right lateral
    occipital gyrus see?" must receive "the LEFT visual
    hemifield."
[ ] Any downstream code querying "what is the lateral
    occipital gyrus?" must receive "the lateral-surface gyral
    fold of the occipital lobe, overlapping V3d, V4d, LOC, and
    MT/V5 — the upstream object-recognition input to the right
    FFA (faces) or left VWFA (reading)."
[ ] Any downstream code querying "is the lateral occipital
    gyrus a primary-sensory surface landmark like the cuneus?"
    must receive "**no** — the cuneus is a V1 upper-bank
    surface landmark (parent-level sibling of ``..gyri``);
    the lateral occipital gyrus is a gyral fold with
    extrastriate and association overlays (a child of
    ``..gyri``)."
[ ] Any downstream code assigning the right face pathway must
    route through the right lateral occipital gyrus's LOC →
    right fusiform gyrus → right FFA chain — the lateral
    occipital gyrus is the upstream LOC input.
[ ] Any downstream code assigning the left reading pathway
    must route through the left lateral occipital gyrus's LOC
    → left fusiform gyrus → left VWFA chain (documented in
    the left sibling).
[ ] Any downstream code assigning prosopagnosia must route
    through the **right** lateral occipital gyrus's LOC →
    right FFA pathway.
[ ] Any downstream code assigning visuospatial deficits must
    weight the **right** lateral occipital gyrus more heavily
    — the right is the dominant visuospatial hemisphere.
[ ] Any downstream code assigning left hemispatial neglect
    must note that **the right lateral occipital gyrus's LOC
    → right IPS pathway is a contributor**, not a sole cause.
[ ] Any downstream code assigning motion-boundary or
    depth-from-motion processing must weight the **right
    lateral occipital gyrus's V3d territory more heavily**
    than the left's — the right V3d is the dominant motion
    substrate.
[ ] **The cuneus-sibling note is byte-identical to the left
    sibling's** — it is a property of the occipital lobe's
    anatomy, not of the hemisphere.
"""