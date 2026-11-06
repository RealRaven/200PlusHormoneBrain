"""
Lateral Occipital Gyrus — Left Hemisphere
==========================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── gyri
                                    └── lateral_occipital_gyrus   ← THIS PACKAGE

This is a **leaf gyral package** describing the left hemisphere's
**lateral occipital gyrus** — the **lateral-surface gyral fold** of
the occipital lobe, on the **lateral occipital convexity** between
the **parieto-occipital sulcus** (rostrally) and the **occipital
pole** (caudally). It is the **only lateral-surface gyrus of the
occipital lobe** that is modelled as a gyrus rather than as a V area,
and it is the **only child of the ``..gyri`` parent** in the current
tree.

Parent: ``..gyri`` (left occipital gyral registry) — the
**single-child parent**. Sibling to no other occipital gyral child
(the cuneus is a **parent-level sibling** of ``..gyri``, not a
child of it; the lingual gyrus is a forward reference).

This package is the **structural mirror** of
``../../right/cortex/occipital/gyri/lateral_occipital_gyrus``. The
gyrus name, the bounding sulci (parieto-occipital, transverse
occipital, lateral occipitotemporal), the functional overlays (V3d,
V4d, LOC), and the lateral-surface placement are identical on both
sides; the **functional emphasis** and **clinical significance**
diverge — on the left, the gyrus's **LOC territory feeds the left
VWFA (reading)** endpoint, and left lateral-occipital-gyrus lesions
produce **visual object agnosia** (bilateral),
**reading-related deficits**, and **color-form processing deficits**
via the LOC → left VWFA pathway. The right lateral occipital gyrus's
LOC feeds the **right FFA (face)** endpoint, and right
lateral-occipital-gyrus lesions produce **prosopagnosia**,
**visuospatial deficits**, and **left hemispatial neglect** via the
LOC → FFA and LOC → right IPS pathways.

**The lateral occipital gyrus is a gyral fold first and a functional
overlay second** — unlike the cuneus, which is a **surface landmark
for primary sensory cortex** first and a gyral fold second. This is
the structural reason the two gyri sit at different levels of the
tree (parent-level cuneus vs `..gyri` child lateral occipital
gyrus), and the two packages cross-reference each other with this
rationale.

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
in some parcellations (analogous to the frontal lobe's SFG / MFG /
IFG triad), but the current tree keeps them as a **single gyrus
package** because the **functional overlays are continuous** across
the three subdivisions. **The superior / middle / inferior
subdivisions are forward references** — they will be added if a
future parcellation promotes the split.

**The lateral occipital gyrus is continuous with the fusiform
gyrus ventrally** — the gyrus transitions into the fusiform gyrus at
the **lateral occipitotemporal sulcus**. **On the left, the fusiform
gyrus is where the left VWFA lives** (downstream of the left LOC);
the lateral occipital gyrus is the **upstream LOC territory** that
feeds the VWFA. **The two together form the left reading pathway's
lateral / ventral territory.**

**The lateral occipital gyrus's functional identity is defined by
its overlays**: V3d at the caudal / dorsal extent, V4d at the
mid / lateral extent, and the LOC at the rostral extent. **It does
NOT contain V1, V2, or the primary sensory cortex** — those live on
the medial surface (calcarine banks, cuneus, lingual gyrus). **The
lateral occipital gyrus is purely extrastriate and association
cortex.**

**Left-hemisphere specificity**: the left lateral occipital gyrus
represents the **right visual hemifield** via its V3d, V4d, and LOC
overlays. Its **LOC territory feeds the left VWFA (reading)
pathway** — the LOC → fusiform → left VWFA chain is the left
reading pathway, and the lateral occipital gyrus is its **upstream
input stage**. **Left lateral-occipital-gyrus lesions that extend
into the fusiform gyrus or the downstream left VWFA produce
reading-related deficits**, **visual object agnosia** (when
bilateral), and **color-form processing deficits** via the V4d
overlay. **The left lateral occipital gyrus does NOT produce
prosopagnosia** — that is the right lateral occipital gyrus's
contribution via the right LOC → right FFA pathway.

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
            gyrus. **On the left, V3d's contribution to right-
            hemifield motion perception is present but weaker
            than the right's** — the right V3d is the dominant
            motion substrate. **On the left, V3d feeds the left's
            contribution to right-hemifield motion-boundary
            perception at a lower weighting than the right's.**

        quaternary_visual_cortex_v4d (V4d)          (MID / LATERAL)
            The **color-form and surface-segmentation** area at
            the mid / lateral extent. **On the left, V4d feeds
            the left LOC → left VWFA reading pathway via its
            color-form output.**

        lateral_occipital_complex (LOC)              (ROSTRAL)
            The **object-recognition complex** at the rostral
            extent. **LOC is a forward reference** — not yet a
            package under ``..cortex``. **On the left, LOC feeds
            the left VWFA (reading).** **LOC overlaps the
            lateral occipital gyrus** and extends into the
            fusiform gyrus.

        motion_area_v5_mt_plus (MT/V5)               (CAUDAL MARGIN)
            The **motion area** at the occipito-temporal junction
            near the caudal lateral occipital gyrus. **MT/V5 is a
            forward reference** — not yet a package. **On the
            left, MT/V5 is present but weaker than the right's**
            — the right MT/V5 is the dominant motion hemisphere.

**This field is structurally identical to the right sibling's** — the
bounding sulci and the four functional overlays (V3d, V4d, LOC,
MT/V5) are the same on both sides. What differs is the **visual
hemifield** — the left lateral occipital gyrus's overlays carry the
**right** hemifield — and the **downstream clinical emphasis** —
the left LOC → left VWFA reading pathway vs the right LOC → right
FFA face pathway.

--------------------------------------------------------------------------------
GYRUS-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    angular gyrus (parietal lobe)          **dorsal neighbour** via the
                                           **transverse occipital
                                           sulcus**. The angular
                                           gyrus is in the parietal
                                           lobe, not the occipital
                                           lobe.
    fusiform gyrus (temporal lobe;         **ventral neighbour** via the
    forward reference in ..gyri)           **lateral occipitotemporal
                                           sulcus**. **On the left,
                                           the fusiform gyrus is
                                           where the left VWFA
                                           lives** (downstream of
                                           the left LOC). **On the
                                           right, the fusiform
                                           gyrus is where the right
                                           FFA lives.**
    cuneus (medial surface)                **distant medial neighbour**
                                           via the occipital pole. The
                                           cuneus is a parent-level
                                           sibling of ``..gyri``, not
                                           a neighbour here.
    lingual gyrus (medial surface;         **distant medial neighbour**
    forward reference in ..gyri)           via the occipital pole. The
                                           lingual gyrus is a forward
                                           reference in the current
                                           tree.
    parieto-occipital sulcus               **rostral boundary** —
                                           separates the lateral
                                           occipital gyrus from the
                                           precuneus (medial) and
                                           from the angular gyrus
                                           (lateral).
    transverse occipital sulcus            **dorsal boundary** —
                                           separates the lateral
                                           occipital gyri from the
                                           parietal lobe's angular
                                           gyrus.
    lateral occipitotemporal sulcus        **ventral boundary** —
                                           separates the lateral
                                           occipital gyri from the
                                           fusiform gyrus.
    occipital pole                        **caudal boundary** — the
                                           caudal convergence of the
                                           lateral occipital gyrus,
                                           cuneus, and lingual
                                           gyrus.

**This field is byte-identical to the left sibling's** at the level of
sulcal and gyral neighbours. The adjacency relationships are
topological, not lateralized. The "left VWFA / right FFA" downstream
notes are correct as written and are repeated in the right sibling's
adjacency section for symmetry.

--------------------------------------------------------------------------------
FUNCTIONAL OVERLAYS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

The lateral occipital gyrus's functional identity is defined by its
**three principal overlays** plus the **MT/V5** at its caudal margin.
The left-side emphasis is:

    tertiary_visual_cortex_v3d (V3d)          (CAUDAL / DORSAL — PRIMARY)
        **The lateral occipital gyrus's caudal / dorsal overlay.**
        V3d is the **motion-boundary and motion-in-depth** area at
        the caudal / dorsal extent. **On the left, V3d's
        contribution to right-hemifield motion perception is
        present but weaker than the right's** — the right V3d is
        the dominant motion-boundary substrate. **Left lateral-
        occipital-gyrus lesions that extend into V3d produce
        motion-boundary and depth-from-motion deficits** in the
        right hemifield that are **milder than the right lateral
        occipital gyrus's equivalent** but are clinically
        detectable on careful testing.

    quaternary_visual_cortex_v4d (V4d)        (MID / LATERAL — PRIMARY)
        **The lateral occipital gyrus's mid / lateral overlay.**
        V4d is the **color-form and surface-segmentation** area at
        the mid / lateral extent. **On the left, V4d feeds the
        left LOC → left VWFA reading pathway via its color-form
        output.** The left lateral occipital gyrus's V4d
        contribution to **color-form integration** is part of the
        left hemisphere's **language-linked color processing**
        — the left V4d → left LOC → left VWFA → left language
        areas chain is the substrate for **color-form-language
        integration**, and left lateral-occipital-gyrus lesions
        that extend into V4d can produce **color-form processing
        deficits** that contribute to color agnosia and
        color-form-language integration deficits when the
        downstream left VWFA and language areas are also
        affected.

    lateral_occipital_complex (LOC)           (ROSTRAL — PRIMARY)
        **The lateral occipital gyrus's rostral overlay — and its
        most clinically consequential contribution.** LOC is the
        **object-recognition complex** at the rostral extent.
        **LOC is a forward reference** — not yet a package under
        ``..cortex``. **On the left, LOC feeds the left VWFA
        (reading) via the LOC → fusiform → left VWFA pathway.**
        The left lateral occipital gyrus's LOC territory is the
        **upstream input** to the left reading pathway, and left
        lateral-occipital-gyrus lesions that extend into the LOC
        territory can **contribute to reading-related deficits**
        (when the downstream fusiform gyrus and left VWFA are
        also affected) and to **visual object agnosia** (when
        the lesion is **bilateral**).

    motion_area_v5_mt_plus (MT/V5)            (CAUDAL MARGIN — SECONDARY)
        **The lateral occipital gyrus's caudal margin.** MT/V5 is
        the **motion area** at the occipito-temporal junction.
        **MT/V5 is a forward reference** — not yet a package.
        **On the left, MT/V5 is present but weaker than the
        right's** — the right MT/V5 is the dominant motion
        hemisphere. **The left MT/V5's contribution to right-
        hemifield motion perception is part of the left
        lateral occipital gyrus's motion territory** but is
        subordinate to the right hemisphere's dominance.

**Left-specific caveat on the reading pathway.** The left lateral
occipital gyrus's **LOC → fusiform → left VWFA pathway** is the
**left reading pathway's upstream input stage**. **The left
lateral occipital gyrus is NOT the left VWFA** — the VWFA is
downstream in the fusiform gyrus. **The left lateral occipital
gyrus is the "what is this object?" object-recognition complex
that feeds the "what does this written word say?" VWFA.**

**Left-specific caveat on the face pathway.** The left lateral
occipital gyrus does **not** carry a face-processing overlay —
that is the right lateral occipital gyrus's contribution. **The
left lateral occipital gyrus's LOC feeds the left VWFA (reading),
not the right FFA (faces).**

**Left-specific caveat on color-form-language integration.** The
left lateral occipital gyrus's V4d → left LOC → left VWFA
pathway is part of the **color-form-language integration**
substrate — the use of color information in the left hemisphere's
language-linked object-recognition network. **Left lateral-
occipital-gyrus lesions that extend into V4d can produce
color-form processing deficits** that contribute to color-form-
language integration deficits when the downstream left VWFA and
language areas are affected.

**Summary**: The lateral occipital gyrus's functional identity is
**dominated by LOC** (the object-recognition complex at its
rostral extent), with **V4d** and **V3d** as mid and caudal
overlays, and **MT/V5** at the caudal margin. **The overlay set is
identical across hemispheres** — both lateral occipital gyri carry
V3d, V4d, LOC, and MT/V5. The left-right differences are:
(a) the **represented visual field** (left = right hemifield,
right = left hemifield);
(b) the **downstream network** (left LOC → left VWFA reading;
right LOC → right FFA faces);
(c) the **V3d weighting** (right V3d is dominant, left V3d is
weaker);
(d) the **LOC downstream target** (left VWFA vs right FFA).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_lateral_occipital_visual_object_agnosia
        **The left lateral occipital gyrus's most distinctive
        clinical anchor.** **Visual object agnosia** — impaired
        ability to recognize objects despite intact visual
        perception — typically requires **bilateral** lesions of
        the ventral stream. **Left lateral-occipital-gyrus
        lesions that extend into the LOC territory contribute to
        the apperceptive component** of visual object agnosia
        (the failure to form a coherent object percept from
        visual features) more than the associative component
        (the failure to link a percept to semantic knowledge).
        **The bilateral requirement** means that isolated left
        lateral-occipital-gyrus lesions produce a **milder**
        object-recognition deficit than bilateral lesions,
        because the right lateral occipital gyrus's LOC can
        compensate via the callosum.

    left_lateral_occipital_reading_related_deficit
        **The left lateral occipital gyrus's reading-pathway
        anchor.** The left lateral occipital gyrus's **LOC →
        fusiform → left VWFA pathway** is the **upstream input**
        to the left reading pathway. **Left lateral-occipital-
        gyrus lesions that extend into the fusiform gyrus or the
        downstream left VWFA produce reading-related deficits**
        — the patient may still read **familiar** words but
        shows **slowed reading** or **impaired recognition of
        novel words** (because the LOC → VWFA object-recognition
        stage is degraded). **The deficit is milder than alexia
        without agraphia** (which requires V1 + splenium
        disconnection) but is more reading-specific than a V2 or
        V3 lesion because the LOC's object-recognition stage is
        the **immediate upstream** of the left VWFA.

    left_lateral_occipital_color_form_processing_deficit
        **The left lateral occipital gyrus's V4d-overlay anchor.**
        The left V4d → left LOC → left VWFA pathway carries the
        **color-form integration** signal. **Left lateral-
        occipital-gyrus lesions that extend into V4d can produce
        color-form processing deficits** — the patient may
        still perceive colors and objects separately but
        cannot integrate them in a linguistic context. **This
        anchor is a left-lateralized contributor** to the
        broader **color-form-language integration deficit**
        that is the left V4's most distinctive clinical
        syndrome. **The deficit is milder than a pure V4 lesion**
        because the lateral occipital gyrus's V4d is a subset of
        the full V4 territory.

    left_lateral_occipital_motion_boundary_deficit
        **The left lateral occipital gyrus's V3d-overlay
        anchor.** The left lateral occipital gyrus's V3d
        territory contributes to right-hemifield motion-boundary
        and depth-from-motion perception. **Left lateral-
        occipital-gyrus lesions that extend into V3d can produce
        motion-boundary deficits** — the patient cannot perceive
        the boundary defined by motion (e.g., a figure defined
        only by the relative motion of its parts against the
        background). **The deficit is milder than the right
        lateral occipital gyrus's equivalent** — the right V3d
        is the dominant motion substrate.

    left_lateral_occipital_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including the **lateral occipital gyrus's V4d
        and LOC territory**. **The lateral occipital gyrus
        contribution is the propagation of the aura into
        color-defined and object-form features** — colored
        fortifications, chromatic scotomata, and **formed object
        hallucinations** in the right hemifield. **This anchor
        is hemisphere-invariant**, but the field involvement is
        contralateral (right field on the left side).

    left_lateral_occipital_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from the lateral occipital gyrus's V4d and LOC
        territory. **Lateral-occipital-gyrus auras** are
        typically **more complex than V1 / V2 / V3 auras** —
        the patient may see **formed objects, colored scenes,
        or recognizable shapes** in the right visual field.
        **The lateral occipital gyrus's auras are the most
        complex of the occipital auras** because the LOC is the
        object-recognition stage.

    left_lateral_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** can
        involve the lateral occipital gyrus and produce a
        **right hemianopia or quadrantic defect** (from V1 /
        V2 / V3 involvement) **plus** a **right hemiachromatopsia**
        (from V4d involvement) **plus** a **reading-related
        deficit** (from LOC → VWFA involvement) when the
        lesion extends sufficiently. **The lateral occipital
        gyrus's contribution is the downstream object-
        recognition and reading component** on top of the
        primary field defect.

    left_lateral_occipital_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves the **lateral occipital gyrus's
        V4d and LOC territory** in early-stage PCA. **Left
        lateral occipital gyrus** is part of the substrate of
        the **progressive ventral stream dysfunction** that
        produces **progressive reading deficits** and **object
        agnosia** in later-stage PCA on the left.

    left_lateral_occipital_pres_visual_symptoms
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
`left_lateral_occipital_visual_object_agnosia`,
`left_lateral_occipital_reading_related_deficit`,
`left_lateral_occipital_color_form_processing_deficit`, and
`left_lateral_occipital_motion_boundary_deficit` — are the
**left-emphasized mirror** of the right lateral occipital gyrus
anchors. **The visual object agnosia and reading-related deficit
are left-lateralized** (the left lateral occipital gyrus feeds the
left reading pathway); the **motion-boundary deficit is milder on
the left** (the right V3d is dominant); the **color-form
processing deficit is a left-lateralized contributor** to the
broader left V4 color-form-language syndrome.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, PRES, and occipital infarct — are **documented
identically in both siblings**, with the side-appropriate field
label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri  (parent)
    The left occipital gyral registry — the **single-child
    parent** of the left occipital lobe. The lateral occipital
    gyrus is its **only child** in the current tree (the cuneus
    is a parent-level sibling, and the lingual gyrus is a
    forward reference).

..occipital
    The **parent-level sibling** of ``..gyri``. The occipital
    lobe parent, source of the ``..gyri``, ``..cortex``,
    ``..brodmann_areas``, ``..cuneus``, and ``..sulci``
    registries.

..brodmann_areas.brodmann_area_19
    The **cytoarchitectonic sibling** of the lateral occipital
    gyrus. The lateral occipital gyrus overlaps **BA 19** (the
    only occipital BA that contains V3d, V4d, and LOC). The
    BA 19 package must declare the lateral occipital gyrus as
    its primary **lateral-surface anatomical substrate**.

...cortex.v3  (V3d)
    The **functional sibling** of the lateral occipital
    gyrus's caudal / dorsal overlay. **On the left, V3d's
    contribution is present but weaker than the right's.** The
    V3 package must declare the lateral occipital gyrus as one
    of its **lateral-surface anatomical substrates**.

...cortex.v4  (V4d)
    The **functional sibling** of the lateral occipital
    gyrus's mid / lateral overlay. **On the left, V4d feeds
    the left LOC → left VWFA reading pathway.**

...cortex.loc  (forward reference)
    The **functional sibling** of the lateral occipital
    gyrus's rostral overlay. **LOC is a forward reference** —
    not yet a package under ``..cortex``. **On the left, LOC
    feeds the left VWFA (reading).**

...cortex.v5_mt_plus  (forward reference)
    The **functional sibling** of the lateral occipital
    gyrus's caudal margin. **MT/V5 is a forward reference** —
    not yet a package under ``..cortex``. **On the left, MT/V5
    is present but weaker than the right's.**

..cuneus
    The **medial-surface sibling** (parent-level sibling of
    ``..gyri``, not a child of the lateral occipital gyrus).
    The cuneus is the **upper bank of the calcarine sulcus**
    (V1 dorsal bank); the lateral occipital gyrus is the
    **lateral surface of the occipital lobe**. **The two gyri
    sit at different levels of the tree** — the cuneus at the
    parent level (surface landmark for V1), the lateral
    occipital gyrus under ``..gyri`` (gyral fold with
    extrastriate overlays).

..gyri  (forward reference — the lingual gyrus is not yet a
    package)
    The lingual gyrus is a **forward reference** in ``..gyri``.
    When it is created, its placement must **preserve the
    cuneus / lingual gyrus symmetry** (the two medial-surface
    gyri) and must be consistent with the lateral occipital
    gyrus's lateral-surface placement.

..sulci.calcarine_sulcus
    The **calcarine sulcus is NOT a boundary of the lateral
    occipital gyrus** — it is the boundary of the cuneus and
    lingual gyrus. The lateral occipital gyrus is on the
    lateral surface, not the medial surface.

..sulci.transverse_occipital_sulcus
    The **dorsal boundary** of the lateral occipital gyri,
    separating them from the parietal lobe's angular gyrus.

..sulci.parieto_occipital_sulcus
    The **rostral boundary** of the lateral occipital gyrus,
    separating it from the precuneus (medial) and the angular
    gyrus (lateral).

..sulci.lateral_occipitotemporal_sulcus  (forward reference, if
    not yet a package)
    The **ventral boundary** of the lateral occipital gyrus,
    separating it from the fusiform gyrus. **On the left, the
    fusiform gyrus is downstream of the lateral occipital
    gyrus's LOC territory** (left VWFA).

..cortex.temporal
    The **ventral stream** continues from the lateral occipital
    gyrus's LOC territory into the temporal lobe (fusiform
    gyrus, left VWFA / right FFA). **On the left, the lateral
    occipital gyrus's LOC → fusiform → left VWFA pathway is
    the reading pathway.** The temporal package must declare
    the left lateral occipital gyrus as a **source of upstream
    LOC input** to its left fusiform gyrus children, and must
    note the **left-lateralized VWFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from the lateral occipital
    gyrus's V3d territory (via MT/V5 → IPS) into the parietal
    lobe. **On the left, the lateral occipital gyrus's V3d
    contribution is present but weaker than the right's.** The
    parietal package must declare the left lateral occipital
    gyrus as a **source of upstream V3d input** to its dorsal
    attention network children (at a lower weighting than the
    right's).

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral
    prefrontal cortex** (BA 9 / BA 46) send top-down visual
    attentional signals to the lateral occipital gyrus's V3d /
    V4d territory.

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
    perirhinal → hippocampus). **On the left, the lateral
    occipital gyrus's LOC → fusiform → left VWFA pathway is
    part of the reading-related memory pathway.**

../../right/cortex/occipital/gyri/lateral_occipital_gyrus
    The right-hemisphere homologue. Structural fields (gyrus
    name, bounding sulci, V3d / V4d / LOC / MT/V5 overlays,
    lateral-surface placement, cuneus-sibling note) MUST be
    byte-identical. Functional emphasis and clinical
    significance diverge — the right lateral occipital gyrus's
    LOC feeds the **right FFA (face)** endpoint, and right
    lateral-occipital-gyrus lesions produce **prosopagnosia**,
    **visuospatial deficits**, and **left hemispatial neglect**
    (via the LOC → right FFA and LOC → right IPS pathways).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "lateral_occipital_gyrus"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    ALTERNATE_NAMES     = ("lateral_occipital_gyri",
                           "lateral_occipital_convexity",
                           "gyrus_occipitalis_lateralis")
        # **"Lateral occipital gyri"** (plural) is the classical
        # anatomical name when the gyrus is subdivided into
        # superior / middle / inferior; **"lateral occipital
        # convexity"** is the modern surface-landmark name;
        # **"gyrus occipitalis lateralis"** is the Latin form.

    BOUNDING_SULCI      = {
                              "rostral":   ("parieto_occipital_"
                                            "sulcus",),
                              "caudal":    ("occipital_pole",),
                              "dorsal":    ("transverse_occipital_"
                                            "sulcus",),
                              "ventral":   ("lateral_occipito_"
                                            "temporal_sulcus",),
                          }

    FUNCTIONAL_OVERLAYS = (
                              "tertiary_visual_cortex_v3d",
                              "quaternary_visual_cortex_v4d",
                              "lateral_occipital_complex",
                              "motion_area_v5_mt_plus",
                          )
        # **V3d, V4d, LOC, MT/V5.** **Identical overlay set on
        # both hemispheres.**

    PRIMARY_OVERLAY     = "lateral_occipital_complex"
        # The lateral occipital gyrus's defining functional
        # identity is the **LOC object-recognition complex** at
        # its rostral extent — the upstream input to the left
        # VWFA (reading) or right FFA (faces).

    REPRESENTED_FIELD   = "contralateral"

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** — left lateral
        # occipital gyrus carries the right hemifield.

    LEFT_LATERALIZED_FUNCTIONS = (
        "right_hemifield_loc_to_left_vwfa",
    )
        # The left lateral occipital gyrus's LOC feeds the left
        # VWFA reading pathway. **This is a right-hemisphere-
        # specific absence on the right side** (the right
        # lateral occipital gyrus feeds the right FFA).

    RIGHT_ONLY_DOMAINS  = (
        "face_processing",
    )
        # The right lateral occipital gyrus's LOC feeds the
        # right FFA face pathway. **This is a left-hemisphere-
        # specific absence on the left side** (the left
        # lateral occipital gyrus feeds the left VWFA).

    LATERALIZATION_NOTE = "lateral_surface_gyral_fold_with_LOC_object_recognition_overlay"
        # **The lateral occipital gyrus's lateralization role is
        # NOT a primary-sensory surface-landmark role** — that
        # is the cuneus's role. The lateral occipital gyrus's
        # lateralization is the **contralateral visual field
        # rule** applied to its extrastriate / association
        # overlays (V3d, V4d, LOC), with the downstream
        # reading-vs-face asymmetry layered on top.

    CUNEUS_SIBLING_NOTE = (
        "The cuneus is a parent-level sibling of this package's "
        "parent (..gyri), not a sibling of this package. The "
        "cuneus sits at the ..occipital parent level because "
        "its primary functional identity is the V1 upper-bank "
        "surface landmark. See ..cuneus and ..gyri."
    )
        # **Byte-identical to the right sibling's.**

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
        "LEFT_LATERALIZED_FUNCTIONS",
        "RIGHT_ONLY_DOMAINS",
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
are the **V-area overlays** that live in ``..cortex`` (not here):

1. **V3d** — the motion-boundary and motion-in-depth area at the
   caudal / dorsal extent. **On the right, V3d is the dominant
   motion substrate**; on the left, it is present but weaker.
2. **V4d** — the color-form and surface-segmentation area at the
   mid / lateral extent. **On the left, V4d feeds the left LOC
   → left VWFA reading pathway.**
3. **LOC** — the object-recognition complex at the rostral extent.
   **On the left, LOC feeds the left VWFA (reading)**; **on the
   right, LOC feeds the right FFA (faces).**
4. **MT/V5** — the motion area at the caudal margin. **On the
   right, MT/V5 is the dominant motion hemisphere**; on the left,
   it is present but weaker.

**None of these is a forward reference of the *gyral* package** —
they are forward references in ``..cortex``, and the gyral
package references them as its functional overlays. **When they
are created under ``..cortex``, they must cross-reference the
lateral occipital gyrus as one of their lateral-surface anatomical
substrates**, in the same commit, in both hemispheres.

**The lingual gyrus is a forward reference in ``..gyri``** and
**the cuneus is a parent-level sibling** — neither is a child of
``..gyri``, and neither affects the lateral occipital gyrus's
structural fields. **The cuneus-sibling note** in the
implementation contract documents the relationship explicitly.

**All forward references are byte-identical to the right sibling's**
— they are properties of the occipital lobe's anatomy, not of the
hemisphere. **The right's emphasis note on V3d and MT/V5 dominance
is byte-identical to the right `..gyri` parent's forward-reference
caveat.**

--------------------------------------------------------------------------------
PROMOTION RULE (when a lateral occipital sub-region becomes a
package)
--------------------------------------------------------------------------------

The lateral occipital gyrus is **architectonically continuous**
across its anteroposterior extent. **The one natural split is the
superior / middle / inferior lateral occipital gyrus triad** — a
three-way gyral subdivision analogous to the frontal lobe's SFG /
MFG / IFG. **The current tree keeps them together as a single
gyrus** because the V3d / V4d / LOC overlays span the full extent
without clean anatomical breaks.

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
  2. Update this package's ``FUNCTIONAL_OVERLAYS`` to reflect
     the per-subdivision overlays (superior → V3d, middle → V4d,
     inferior → LOC).
  3. Update the parent ``..gyri``'s ``GYRI_TO_V_OVERLAYS`` index
     accordingly.
  4. Mirror the promotion on the right side in the same commit.

**The split is a legitimate three-way gyral subdivision, but it is
BLOCKED while LOC and MT/V5 are unresolved** — the two most
clinically consequential overlays (the LOC upstream of the left
VWFA reading pathway, and the right V3d → MT/V5 motion substrate)
are not yet packages under ``..cortex``.

**The split preserves the cuneus / lateral occipital gyrus
distinction** — the cuneus remains a parent-level sibling, not a
subdivision of the lateral occipital gyrus, and its primary-sensory
role is unchanged by the lateral occipital gyrus's three-way
subdivision.

**No split should be performed while LOC and MT/V5 are unresolved.**

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../lateral_occipital_gyrus``:

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
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        LEFT_LATERALIZED_FUNCTIONS
                               left: ("right_hemifield_loc_to_
                               left_vwfa",) — the left LOC
                               feeds the left VWFA reading
                               pathway.
                               right: () — the right LOC does
                               not contribute to the left
                               reading pathway.
        RIGHT_ONLY_DOMAINS     left: () — the left LOC does not
                               contribute to the right face
                               pathway.
                               right: ("face_processing",) —
                               the right LOC feeds the right
                               FFA face pathway.
        CLINICAL_ANCHORS       left: **visual object agnosia**
                               (bilateral), **reading-related
                               deficit** via the LOC → left
                               VWFA pathway, **color-form
                               processing deficit** (V4d),
                               motion-boundary deficit
                               (milder), migraine aura,
                               occipital epilepsy, occipital
                               infarct, PCA, PRES.
                               right: **prosopagnosia
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

**The visual-hemifield asymmetry is the sharpest single entry.**
The left lateral occipital gyrus's overlays represent the **right**
hemifield; the right's represent the **left** hemifield.

**The reading-vs-face downstream asymmetry is the second sharpest
entry.** The left lateral occipital gyrus's LOC feeds the **left
VWFA reading** endpoint; the right's feeds the **right FFA face**
endpoint. The `LEFT_LATERALIZED_FUNCTIONS` / `RIGHT_ONLY_DOMAINS`
tuples make this explicit, and the two contributions are
mirror-opposite.

**The right-specific clinical anchors are the third sharpest
entry.** The right lateral occipital gyrus carries three anchors
that the left does not carry at the same weighting:
`right_lateral_occipital_prosopagnosia_contribution`,
`right_lateral_occipital_visuospatial_deficit`, and
`right_lateral_occipital_left_hemifield_neglect_contribution`. The
right also carries the **more severe** motion-boundary deficit
(the right V3d is the dominant motion substrate). The left carries
the mirror `left_lateral_occipital_reading_related_deficit` and
`left_lateral_occipital_visual_object_agnosia` anchors.

**The overlay set (V3d, V4d, LOC, MT/V5), the bounding sulci, the
PRIMARY_OVERLAY, the LATERALIZATION_NOTE, the CUNEUS_SIBLING_NOTE,
and the lateral-surface placement are byte-identical on both
sides.** They are properties of the lateral occipital gyrus's
anatomy, not of the hemisphere.

**The cuneus-sibling note is byte-identical on both sides** and
must not be allowed to drift.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "lateral_occipital_gyrus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] ALTERNATE_NAMES includes "lateral_occipital_gyri",
    "lateral_occipital_convexity", and
    "gyrus_occipitalis_lateralis".
[ ] BOUNDING_SULCI documents the four boundaries:
    - rostral: parieto-occipital sulcus
    - caudal: occipital pole
    - dorsal: transverse occipital sulcus
    - ventral: lateral occipitotemporal sulcus
[ ] FUNCTIONAL_OVERLAYS is byte-identical to the right sibling's:
    V3d, V4d, LOC, MT/V5.
[ ] PRIMARY_OVERLAY is "lateral_occipital_complex" — **the LOC
    is the lateral occipital gyrus's defining functional
    contribution** at its rostral extent.
[ ] REPRESENTED_FIELD is "contralateral" — the lateral
    occipital gyrus represents the contralateral hemifield.
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] **The lateral-surface placement is documented** — the
    lateral occipital gyrus is a **child of ``..gyri``**,
    **not** a parent-level sibling like the cuneus.
[ ] **The cuneus-sibling note is documented** — the cuneus is
    a **parent-level sibling of ``..gyri``** (not a sibling of
    the lateral occipital gyrus), and the reason (V1 upper-bank
    surface landmark) is repeated here for clarity.
[ ] **The lateral occipital gyrus is a gyral fold first, not a
    surface landmark for primary sensory cortex** — the
    docstring explicitly contrasts it with the cuneus on this
    point.
[ ] **The cuneus / lateral occipital gyrus symmetry is
    documented** — the two gyri sit at different levels of the
    tree for structural reasons.
[ ] LEFT_LATERALIZED_FUNCTIONS contains
    "right_hemifield_loc_to_left_vwfa" — the left lateral
    occipital gyrus's LOC feeds the left VWFA reading pathway.
[ ] RIGHT_ONLY_DOMAINS contains "face_processing" — **this is a
    left-side absence anchor**, documenting that the left
    lateral occipital gyrus does **not** contribute to the
    right face pathway at the same weighting as the right
    lateral occipital gyrus does.
[ ] LATERALIZATION_NOTE is
    "lateral_surface_gyral_fold_with_LOC_object_recognition_
    overlay" — the lateral occipital gyrus's lateralization
    role is the contralateral visual field rule applied to its
    extrastriate / association overlays, **not** a
    primary-sensory surface-landmark role.
[ ] CUNEUS_SIBLING_NOTE is present and byte-identical to the
    right sibling's.
[ ] CLINICAL_ANCHORS contains the left-specific anchors:
    - left_lateral_occipital_visual_object_agnosia
    - left_lateral_occipital_reading_related_deficit
    - left_lateral_occipital_color_form_processing_deficit
    - left_lateral_occipital_motion_boundary_deficit
    - left_lateral_occipital_migraine_visual_aura
    - left_lateral_occipital_occipital_epilepsy_visual_auras
    - left_lateral_occipital_infarct_pca_territory
    - left_lateral_occipital_posterior_cortical_atrophy
    - left_lateral_occipital_pres_visual_symptoms
[ ] The **visual object agnosia** is documented as the
    primary left lateral occipital gyrus anchor (with the
    **bilateral** requirement noted).
[ ] The **reading-related deficit** is documented as the
    left-lateralized downstream anchor — the left LOC → left
    VWFA pathway is the upstream input to the reading
    pathway.
[ ] The **color-form processing deficit** is documented as a
    V4d-overlay anchor and a **left-lateralized contributor**
    to the broader left V4 color-form-language syndrome.
[ ] The **motion-boundary deficit** is documented as a
    V3d-overlay anchor (milder than the right's).
[ ] **The lateral occipital gyrus is explicitly NOT the left
    VWFA** — the VWFA is downstream in the fusiform gyrus.
    The lateral occipital gyrus's LOC is the "what is this
    object?" stage; the VWFA is the "what does this written
    word say?" stage.
[ ] **The lateral occipital gyrus does NOT produce
    prosopagnosia** — that is the right lateral occipital
    gyrus's contribution via the right LOC → right FFA
    pathway.
[ ] **The lateral occipital gyrus → fusiform gyrus continuity**
    is documented — the lateral occipital gyrus transitions to
    the fusiform gyrus at the lateral occipitotemporal sulcus.
    **On the left, the fusiform gyrus's VWFA is downstream of
    the lateral occipital gyrus's LOC.**
[ ] **The transverse occipital sulcus** is documented as the
    dorsal boundary.
[ ] **The lateral occipitotemporal sulcus** is documented as
    the ventral boundary.
[ ] **The parieto-occipital sulcus** is documented as the
    rostral boundary.
[ ] **The calcarine sulcus is explicitly NOT a boundary of the
    lateral occipital gyrus.**
[ ] **The LOC and MT/V5 forward references are documented** —
    they live in ``..cortex`` as V-area forward references,
    not here as gyral children. **When they are created, they
    must cross-reference the lateral occipital gyrus as one of
    their lateral-surface anatomical substrates.**
[ ] No forward-declaration caveat is needed for the lateral
    occipital gyrus's structural fields. The **lingual gyrus
    forward reference** (in ``..gyri``) and the **cuneus
    parent-level sibling** are documented via the
    CUNEUS_SIBLING_NOTE and the parent package's caveat.
[ ] No SUBDIVISIONS promotion is performed while LOC and MT/V5
    are unresolved.
[ ] The **promotion rule for the three-way lateral occipital
    gyrus split** is documented, with the joint ``..cortex``
    update requirement and the downstream LOC / MT/V5
    prerequisites.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (GYRUS_NAME, LOBE, ALTERNATE_NAMES, BOUNDING_SULCI,
    FUNCTIONAL_OVERLAYS, PRIMARY_OVERLAY, REPRESENTED_FIELD,
    LATERALIZATION_NOTE, CUNEUS_SIBLING_NOTE, lateral-surface
    placement) match the right sibling; VISUAL_HEMIFIELD,
    LEFT_LATERALIZED_FUNCTIONS, RIGHT_ONLY_DOMAINS, and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    lateral occipital gyrus carries "right_hemifield"; the
    right carries "left_hemifield."
[ ] **The reading-vs-face downstream asymmetry is verified**:
    the left lateral occipital gyrus carries "right_hemifield_
    loc_to_left_vwfa" and the right carries "face_processing"
    — the two are mirror-opposite.
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
[ ] Any downstream code querying "what does the left lateral
    occipital gyrus see?" must receive "the RIGHT visual
    hemifield."
[ ] Any downstream code querying "what is the lateral
    occipital gyrus?" must receive "the lateral-surface gyral
    fold of the occipital lobe, overlapping V3d, V4d, LOC, and
    MT/V5 — the upstream object-recognition input to the left
    VWFA (reading) or right FFA (faces)."
[ ] Any downstream code querying "is the lateral occipital
    gyrus a primary-sensory surface landmark like the cuneus?"
    must receive "**no** — the cuneus is a V1 upper-bank
    surface landmark (parent-level sibling of ``..gyri``);
    the lateral occipital gyrus is a gyral fold with
    extrastriate and association overlays (a child of
    ``..gyri``)."
[ ] Any downstream code assigning the left reading pathway
    must route through the left lateral occipital gyrus's LOC
    → left fusiform gyrus → left VWFA chain — the lateral
    occipital gyrus is the upstream LOC input.
[ ] Any downstream code assigning the right face pathway
    must route through the right lateral occipital gyrus's
    LOC → right fusiform gyrus → right FFA chain (documented
    in the right sibling).
[ ] Any downstream code assigning visual object agnosia must
    note that **bilateral lateral occipital gyrus lesions are
    required** — the left lateral occipital gyrus alone does
    not produce full visual object agnosia.
[ ] Any downstream code assigning prosopagnosia must route
    through the **right** lateral occipital gyrus's LOC →
    right FFA pathway.
[ ] Any downstream code assigning motion-boundary or
    depth-from-motion processing must note that the **right
    lateral occipital gyrus's V3d territory is the dominant
    substrate** — the left's contribution is milder.
[ ] **The cuneus-sibling note is byte-identical to the right
    sibling's** — it is a property of the occipital lobe's
    anatomy, not of the hemisphere.
"""