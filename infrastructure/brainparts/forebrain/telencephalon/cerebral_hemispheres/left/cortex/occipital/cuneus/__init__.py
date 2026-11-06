"""
Cuneus — Left Hemisphere
=========================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── occipital
                              └── cuneus   ← THIS PACKAGE

This is a **leaf gyral package** describing the left hemisphere's
**cuneus** — the **wedge-shaped medial-surface gyrus** between the
**parieto-occipital sulcus** (rostrally) and the **calcarine sulcus**
(caudally). It is **not** a child of ``..gyri`` — it sits at the
**``..occipital`` parent level**, alongside ``brodmann_areas``,
``cortex``, ``gyri``, and ``sulci``.

Parent: ``..occipital`` — the left occipital lobe. Sibling to
``..brodmann_areas``, ``..cortex``, ``..gyri``, and ``..sulci``.

**The parent-level placement is deliberate and reflects the cuneus's
dual identity.** The cuneus is simultaneously:

  (a) a **gyral territory** — a wedge-shaped fold of cortex on the
      medial surface of the occipital lobe, with the same kind of
      structural decomposition as any other gyrus; AND

  (b) a **surface landmark for V1** — the **upper bank of the
      calcarine sulcus**, which is the **lower margin of the
      cuneus**, is the seat of the **dorsal V1 representation of
      the lower contralateral visual field**.

Every other gyrus in the frontal lobe, the temporal lobe, and the
parietal lobe is modelled as a child of ``..gyri`` because its
primary role is **structural** (it is a fold of cortex). The cuneus
is the **first gyrus in the cortex tree whose primary role is
functional-landmark** — its cortical territory is **mostly V1**
(and partly V2 / V3), and its existence as an anatomical fold is
inseparable from its role as the upper-bank V1 surface.

**The cuneus's counterpart on the frontal lobe is the paracentral
lobule.** Both are **medial-surface gyral / lobular territories**
that function as **surface landmarks for primary sensory cortex**:
the paracentral lobule for leg somatosensory / motor, the cuneus for
upper-bank V1. **Both are placed at the parent level** for the same
reason, and both are cross-referenced from the medial-surface
sulcal packages (the paracentral sulcus and the calcarine sulcus,
respectively).

This package is the **structural mirror** of
``../../right/cortex/occipital/cuneus``. The gyrus name, the bounding
sulci (parieto-occipital and calcarine), the V1 upper-bank overlay,
and the medial-surface placement are identical on both sides; the
**functional emphasis** and **clinical significance** diverge — on
the left, the cuneus's V1 upper-bank representation carries the
**lower RIGHT visual field**, and left cuneus lesions produce
**right upper-quadrantic visual field defects** that can contribute
to **hemianopic alexia** and to the **left-lateralized reading
network's** upper-field deficit. The right cuneus carries the mirror
arrangement (lower LEFT field, left upper-quadrantic defects,
prosopagnosia contribution).

--------------------------------------------------------------------------------
WHAT THE CUNEUS IS
--------------------------------------------------------------------------------

The cuneus is the **wedge-shaped medial-surface gyrus** of the
occipital lobe, bounded:

    rostrally   by the **parieto-occipital sulcus** (which separates
                the cuneus from the precuneus of the parietal lobe)
    caudally    by the **calcarine sulcus** (which separates the
                cuneus from the lingual gyrus, and whose upper bank
                carries the **dorsal V1 representation**)
    medially    by the **interhemispheric fissure** (the dorsal
                medial margin of the hemisphere)
    laterally   by the **lateral occipital gyrus** (the lateral
                surface of the occipital lobe)

The name **cuneus** is Latin for **"wedge"** — the gyrus is
wedge-shaped in midsagittal section, with its point at the occipital
pole and its base along the parieto-occipital sulcus. The wedge
narrows caudally toward the occipital pole, where the cuneus meets
the lingual gyrus at the convergence of the calcarine sulcus.

**The cuneus's primary functional identity is its role as the
surface landmark for V1's upper bank.** The **lower margin of the
cuneus** is the **upper bank of the calcarine sulcus**, and this is
where the **dorsal V1 representation** lives:

    Upper bank of the calcarine sulcus    → dorsal V1 representation
                                          → lower contralateral visual
                                            field
    Lower bank of the calcarine sulcus    → ventral V1 representation
                                          → upper contralateral
                                            visual field

**On the left, the cuneus's V1 upper bank represents the lower RIGHT
visual field** — the dorsal V1 neurons that respond to stimuli in the
lower half of the right hemifield.

**The cuneus also extends beyond V1** — its rostral and dorsal
portions are partially V2 (and V3) territory, and its lateral aspect
is V3d territory. **The cuneus's V1 territory is the lower margin**
(the banks of the calcarine sulcus); the more dorsal portions are
extrastriate. **This is why the cuneus's functional overlays are
listed as `primary_visual_cortex_dorsal_bank` (V1), plus
`secondary_visual_cortex_dorsal_bank` (V2), plus
`tertiary_visual_cortex_v3d`** — the cuneus contains portions of
V1, V2, and V3d, with **V1 at its lower margin** (the calcarine
upper bank), **V2 / V3d at its more dorsal extent**.

**The cuneus does not contain the fovea.** The fovea is at the
**occipital pole** — the **caudal convergence** of the cuneus and
lingual gyrus. The cuneus proper (the wedge) represents the **lower
contralateral peripheral field** more than the foveal field. **This
is why cuneus lesions typically produce peripheral field defects**
(macular sparing is common, because the fovea is at the pole).

**Left-hemisphere specificity**: the left cuneus's V1 upper-bank
representation carries the **lower RIGHT visual field**, and its
V2 / V3d extensions contribute to the **right hemifield's V2 / V3d
processing** (motion boundaries, depth from motion, kinetic form).
**Left cuneus lesions produce right upper-quadrantic field defects**
— the dorsal V1 upper-bank damage removes the lower-right-field
representation, producing a defect in the right field's lower half,
which in a completed hemianopia presents as the **upper-quadrantic
defect**. **Left cuneus / V1 upper-bank damage can contribute to
hemianopic alexia** (via loss of right-hemifield input to the
reading network) and to the **left-lateralized reading deficits**
that depend on the full right hemifield.

--------------------------------------------------------------------------------
BOUNDING / OVERLAPPING TERRITORIES
--------------------------------------------------------------------------------

    Bounding sulci
        rostrally   **parieto-occipital sulcus** — separates the
                    cuneus from the precuneus (parietal lobe)
        caudally    **calcarine sulcus** — separates the cuneus
                    from the lingual gyrus; the **upper bank of
                    the calcarine sulcus** is the **lower margin
                    of the cuneus**
        laterally   **lateral occipital sulcus / lateral margin**
                    (where the cuneus transitions to the lateral
                    occipital gyrus)

    Overlapping V areas (functional overlays)
        primary_visual_cortex_dorsal_bank (V1)
            The **lower margin** of the cuneus — the upper bank
            of the calcarine sulcus — carries the **dorsal V1
            representation of the lower contralateral visual
            field**. **On the left, the lower RIGHT field.**
        secondary_visual_cortex_dorsal_bank (V2)
            The **more dorsal** portion of the cuneus carries the
            **V2 upper-bank representation of the lower
            contralateral visual field**. **On the left, the
            lower RIGHT field.** Note: V2's upper-field
            representation is on the **upper bank** (the cuneus
            side), while V1's upper field is on the **lower
            bank** — the **V1 / V2 mirror-flip**.
        tertiary_visual_cortex_v3d (V3d)
            The **lateral and dorsal** portion of the cuneus
            overlaps V3d — the **motion-boundary and
            motion-in-depth** area that projects to MT/V5.
            **On the left, V3d's contribution is present but
            weaker than the right's.**

**This field is structurally identical to the right sibling's** — the
bounding sulci (parieto-occipital and calcarine) and the three V
overlays (V1, V2, V3d) are the same on both sides. What differs is
the **visual hemifield** — the left cuneus carries the lower RIGHT
field — and the **downstream clinical emphasis** — the left cuneus
contributes to the left-lateralized reading network, while the right
cuneus contributes to the right-lateralized face-processing network.

--------------------------------------------------------------------------------
GYRUS-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    precuneus (parietal lobe)              **rostral neighbour** via the
                                           **parieto-occipital sulcus**.
                                           The precuneus is in the
                                           parietal lobe, not the
                                           occipital lobe — the
                                           parieto-occipital sulcus
                                           is the boundary between
                                           the two lobes on the
                                           medial surface.
    lingual gyrus (medial-surface          **caudal neighbour** via the
    gyrus; forward reference in ..gyri)    **calcarine sulcus**. The
                                           lingual gyrus is the lower
                                           bank of the calcarine
                                           sulcus, the cuneus is the
                                           upper bank. **The V1
                                           representation is split
                                           between them**: the upper
                                           bank (cuneus) carries
                                           the lower field, the
                                           lower bank (lingual
                                           gyrus) carries the upper
                                           field.
    lateral occipital gyrus                **lateral neighbour** via
                                           the **lateral occipital
                                           sulcus / lateral margin**.
                                           The cuneus's lateral
                                           portion overlaps with
                                           V3d territory.
    calcarine sulcus (defining sulcus)     **the cuneus's most
                                           consequential sulcal
                                           boundary** — the upper
                                           bank of the calcarine
                                           sulcus is the **lower
                                           margin of the cuneus**,
                                           and it carries the dorsal
                                           V1 representation. **On
                                           the left, the lower RIGHT
                                           visual field.**
    parieto-occipital sulcus               **the cuneus's rostral
                                           boundary** — separates
                                           the cuneus from the
                                           precuneus, and marks the
                                           occipital / parietal
                                           boundary on the medial
                                           surface.

**This field is byte-identical to the left sibling's** at the level of
sulcal and gyral neighbours. The adjacency relationships are
topological, not lateralized.

--------------------------------------------------------------------------------
FUNCTIONAL OVERLAYS (left-hemisphere emphasis)
--------------------------------------------------------------------------------

The cuneus's functional identity is dominated by **one primary
overlay** (V1) plus **two secondary overlays** (V2 and V3d). The
left-side emphasis is:

    primary_visual_cortex_dorsal_bank (V1)         (PRIMARY overlay)
        **The cuneus's defining functional overlay.** The **lower
        margin of the cuneus** — the upper bank of the calcarine
        sulcus — is the **seat of the dorsal V1 representation
        of the lower contralateral visual field**. **On the left,
        the lower RIGHT field.** The V1 upper bank is continuous
        with the V1 lower bank (the lingual gyrus) at the **fundus
        of the calcarine sulcus** (the horizontal meridian), and
        the two banks together represent the full contralateral
        hemifield. **The cuneus's V1 upper bank is the upper half
        of V1's retinotopic map on the medial surface.**

    secondary_visual_cortex_dorsal_bank (V2)       (SECONDARY overlay)
        **The more dorsal portion of the cuneus** overlaps V2's
        upper bank. Note the **V1 / V2 mirror-flip**: V1's upper
        field is on the **lower bank** (lingual gyrus), while V2's
        upper field is on the **upper bank** (cuneus). This is why
        the cuneus contains **both** V1's **lower-field**
        representation (at its lower margin) **and** V2's
        **upper-field** representation (at its more dorsal
        extent) — the two maps are reversed relative to each
        other, and the cuneus spans **both banks of the mirror**.
        **On the left, V2's upper-bank representation carries the
        lower RIGHT field** (which, because of the mirror-flip, is
        also V1's upper-bank representation of the same field).

    tertiary_visual_cortex_v3d (V3d)               (SECONDARY overlay)
        **The lateral and dorsal** portion of the cuneus overlaps
        V3d — the **motion-boundary** and **motion-in-depth** area
        that projects to MT/V5. **On the left, V3d's contribution
        is present but weaker than the right's** — the right V3d
        is the dominant motion substrate. **The cuneus's V3d
        territory feeds the left's contribution to right-
        hemifield motion-boundary perception at a lower weighting
        than the right's.**

**Left-specific caveat on the reading pathway.** The cuneus's V1
upper-bank representation is the **lower-right-field input** to the
**left reading network**. **On the left, the cuneus's V1 upper
bank is part of the input stage of the left V4v → LOC → left VWFA
pathway** — the reading pathway that processes written words in the
right hemifield. **A left cuneus lesion that removes the lower-
right-field representation can disrupt reading** in the same way a
complete left hemianopia does, but the deficit is **more restricted
to the upper-quadrantic portion of the right field** and is often
**milder**.

**Left-specific caveat on the face pathway.** The cuneus's V1
upper-bank representation is **not** part of the right FFA face
pathway — that is the right cuneus's contribution. **The left
cuneus does not carry a face-processing overlay** — its upper-bank
V1 representation feeds the left reading pathway, not a face
pathway.

**Summary**: The cuneus's functional identity is **dominated by
V1** (the lower margin's upper-bank representation), with **V2 and
V3d as secondary overlays** (the more dorsal extent). **The
functional overlay set is identical across hemispheres** — both
cunei carry V1, V2, and V3d. The left-right differences are:
(a) the **represented visual field** (left = lower RIGHT, right =
lower LEFT);
(b) the **downstream network** (left cuneus → left reading pathway;
right cuneus → right face pathway).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    left_cuneus_right_upper_quadrantic_visual_field_defect
        **This is the left cuneus anchor par excellence.** A
        lesion of the left cuneus — specifically, the **lower
        margin** of the cuneus (the upper bank of the calcarine
        sulcus) — produces a **right upper-quadrantic** visual
        field defect: loss of the **upper** portion of the
        **right** visual field. **The mechanism** is that the
        upper bank of the calcarine sulcus represents the **lower
        contralateral field**, so damage to the upper bank
        removes the **lower** right field representation; but a
        partial lesion affecting only the **dorsal** portion of
        the cuneus can produce a defect in the **upper**
        quadrant depending on the exact retinotopic geometry.
        **The typical cuneus lesion produces a right quadrantic
        defect** — either upper or lower depending on the exact
        bank involvement — **often with macular sparing** (the
        fovea is at the occipital pole, away from the cuneus
        proper).

    left_cuneus_right_hemifield_reading_deficit
        **The left cuneus's role in the left reading pathway.**
        The cuneus's V1 upper-bank representation is part of the
        **lower-right-field input** to the **left reading
        network**. **Left cuneus lesions can produce hemianopic
        alexia** (impaired reading from the partial right field
        defect) **and can contribute to the reading-specific
        component** of the left-hemisphere's visual processing.
        **The deficit is milder than a complete left V1
        hemianopia** (the cuneus lesion affects only a portion
        of the right field), but it is more reading-specific
        than a V2 or V3 lesion because the cuneus's V1 input is
        the **primary visual** input to the reading pathway.

    left_cuneus_motion_boundary_deficit
        **The cuneus's V3d territory.** The lateral and dorsal
        portion of the cuneus overlaps V3d — the **motion-
        boundary** and **motion-in-depth** area. **Left cuneus
        lesions that extend into V3d can produce motion-boundary
        and depth-from-motion deficits** in the right
        hemifield. **The deficit is milder than the right
        cuneus's equivalent** (the right V3d is the dominant
        motion substrate) but is present and can be
        clinically detectable on careful testing.

    left_cuneus_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including the **cuneus's V1 upper bank** and
        its V2 and V3d territories. **The cuneus contribution
        is the propagation of the aura into the lower-right-
        field features** (lower-field fortifications, lower-
        field scotomata) — the upper-field features are the
        **lingual gyrus**'s contribution. **This anchor is
        hemisphere-invariant**, but the field involvement is
        contralateral (lower-right field on the left side).

    left_cuneus_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from the **cuneus's V1 upper bank** — the auras
        project to the **lower right visual field** on the
        left side. **The cuneus's auras are typically
        elementary** (flashes, shapes, scotomata) because the
        cuneus's territory is primarily V1 (primary visual
        cortex), not the more complex V4 or MT/V5 areas.

    left_cuneus_occipital_infarct_pca_territory
        **Left posterior cerebral artery (PCA) infarct** can
        involve the cuneus and produce a **right upper-quadrantic
        defect** — often with macular sparing. **The cuneus's
        contribution to the infarct's clinical signature** is
        the **quadrantic specificity** of the field defect (V1
        only would produce a hemianopia; the cuneus-only
        involvement produces the quadrantic defect).

    left_cuneus_posterior_cortical_atrophy
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves the **cuneus** (and the
        surrounding occipital cortex) in later stages. **Left
        cuneus** is part of the substrate of the progressive
        reading deficits in later-stage PCA.

    left_cuneus_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — can involve the cuneus
        and produce **cortical blindness, quadrantic field
        defects, or visual hallucinations**. **The syndrome is
        reversible** in most cases.

**The cuneus-specific clinical anchors** — `left_cuneus_right_
upper_quadrantic_visual_field_defect`,
`left_cuneus_right_hemifield_reading_deficit`, and
`left_cuneus_motion_boundary_deficit` — are the **left-emphasized
mirror** of the right cuneus anchors. **The right upper-quadrantic
defect is the primary anchor**, and the **reading deficit is
left-specific** (the left cuneus contributes to the left reading
network; the right cuneus does not).

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA, PRES, and occipital infarct — are **documented
identically in both siblings**, with the side-appropriate field
label.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..occipital  (parent)
    The left occipital lobe. This package's parent (the cuneus is
    **one of five direct children** of ``..occipital``, not a
    child of ``..gyri``).

..brodmann_areas
    The **cytoarchitectonic sibling**. **The cuneus's V1 territory
    is BA 17, its V2 territory is BA 18, and its V3d territory is
    BA 18 / BA 19.** The BA packages cross-reference the cuneus as
    the surface landmark for their medial-surface upper-bank
    representations.

..cortex
    The **functional sibling**. **The cuneus's V1 territory is
    `primary_visual_cortex`, its V2 territory is `v2`, and its
    V3d territory is `v3`.** The V packages cross-reference the
    cuneus as the surface landmark for their medial-surface
    upper-bank representations.

..gyri
    The **lateral-surface gyral sibling**. The cuneus is the
    **medial-surface** counterpart of the lateral occipital gyrus
    — the two gyri together form the occipital lobe's dorsal
    surface (medial + lateral). **The cuneus is not a child of
    ``..gyri``** because its primary functional identity is the
    V1 upper-bank surface landmark, not a generic gyral fold.

..sulci.calcarine_sulcus
    **The cuneus's defining sulcus.** The upper bank of the
    calcarine sulcus is the **lower margin of the cuneus**, and
    it carries the dorsal V1 representation. **On the left, the
    lower RIGHT visual field.**

..sulci.parieto_occipital_sulcus (a frontal / parietal / occipital
    boundary; the sulcus package may live under ``..parietal``
    or ``..sulci`` depending on the tree's decomposition)
    **The cuneus's rostral boundary.** Separates the cuneus from
    the precuneus, and marks the occipital / parietal boundary
    on the medial surface.

..sulci.lunate_sulcus
    The inconstant lateral-surface sulcus marking the V1 / V2
    border. **Not a cuneus boundary** — the cuneus's boundaries
    are the parieto-occipital and calcarine sulci.

..sulci.transverse_occipital_sulcus
    The dorsal-surface landmark for the V3A / V3B territory.
    **Not a cuneus boundary.**

..cortex.temporal
    The **ventral stream** continues from the cuneus's V1 / V2 /
    V3d territory (via the left V4v → LOC → left VWFA pathway)
    into the temporal lobe. **On the left, the cuneus's upper-
    bank V1 representation is part of the right-hemifield input
    to the left VWFA (reading)** — the lower-right-field signal
    that the left reading network depends on. The temporal
    package must declare the left cuneus as a **source of upper-
    bank V1 input** to the ventral stream, and must note the
    **left-lateralized VWFA specialization**.

..cortex.parietal
    The **dorsal stream** continues from the cuneus's V3d
    territory (via MT/V5 → right IPS) into the parietal lobe.
    **On the left, the cuneus's V3d contribution is present but
    weaker than the right's.** The parietal package should note
    the **cuneus → V3d → MT/V5** relationship.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral
    prefrontal cortex** (BA 9 / BA 46) send top-down visual
    attentional signals to the cuneus's V1 and V2 territory
    via the V1 / V2 relays.

..cortex.cingulate  — indirect
    No direct cingulate → cuneus projection. **The parieto-
    occipital sulcus** separates the cuneus from the precuneus
    (parietal), which is the cingulate's neighbour — but the
    cuneus does not directly border the cingulate.

..cortex.insular  — indirect
    No direct insular → cuneus projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the **indirect** source of the cuneus's V1
    input via the V1 relay. **The cuneus has no direct LGN
    projection** — the LGN → V1 pathway terminates in the
    calcarine cortex, which is the cuneus's lower margin.

../../subcortical/medial_temporal_lobe/hippocampus
    The cuneus's V1 / V2 output reaches the hippocampus via the
    ventral stream (V4v → LOC → inferotemporal → perirhinal →
    hippocampus). **The cuneus's upper-bank V1 representation
    is part of the lower-right-field input to the left
    reading-related memory pathway.**

../../right/cortex/occipital/cuneus
    The right-hemisphere homologue. Structural fields (gyrus
    name, bounding sulci, V1 / V2 / V3d overlays, medial-surface
    placement, parent-level position) MUST be byte-identical.
    Functional emphasis and clinical significance diverge — the
    right cuneus carries the **lower LEFT visual field**, and
    right cuneus lesions produce **left upper-quadrantic visual
    field defects** that can contribute to **prosopagnosia**
    (via the right face pathway) rather than to reading.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "cuneus"
    HEMISPHERE          = "left"
    LOBE                = "occipital"

    ALTERNATE_NAMES     = ("cuneus_gyrus",
                           "medial_occipital_wedge",
                           "cuneate_lobule")
        # **"Cuneate lobule"** is an older term; **"cuneus
        # gyrus"** and **"medial occipital wedge"** are modern
        # anatomical alternatives.

    BOUNDING_SULCI      = {
                              "rostral":    ("parieto_occipital_"
                                             "sulcus",),
                              "caudal":     ("calcarine_sulcus",),
                              "lateral":    ("lateral_occipital_"
                                             "sulcus_or_margin",),
                          }

    FUNCTIONAL_OVERLAYS = (
                              "primary_visual_cortex_dorsal_bank",
                              "secondary_visual_cortex_dorsal_bank",
                              "tertiary_visual_cortex_v3d",
                          )
        # **V1 primary, V2 / V3d secondary.** **Identical
        # overlay set on both hemispheres.**

    PRIMARY_OVERLAY     = "primary_visual_cortex_dorsal_bank"
        # The cuneus's defining functional identity is its V1
        # upper-bank representation. **This is why the cuneus is
        # at the parent level, not under ``..gyri``.**

    V1_BANK_SIDE        = "upper"
        # The cuneus's lower margin is the **upper bank of the
        # calcarine sulcus**, carrying the **dorsal V1
        # representation of the lower contralateral field**.

    REPRESENTED_FIELD   = "lower_contralateral"
        # **On the left, the lower RIGHT visual field.**

    VISUAL_HEMIFIELD    = "right"
        # **The represented visual hemifield** — left cuneus
        # processes the lower RIGHT field (via its V1 upper-bank
        # representation).

    LEFT_LATERALIZED_FUNCTIONS = (
        "right_hemifield_lower_field_reading_input",
    )
        # The left cuneus's V1 upper-bank representation is
        # part of the **lower-right-field input to the left
        # reading network** (left V4v → LOC → left VWFA).
        # **This is a right-hemisphere-specific absence on the
        # right side** (the right cuneus does not contribute to
        # the reading network).

    RIGHT_ONLY_DOMAINS  = (
        "face_processing",
    )
        # The right cuneus's V1 upper-bank representation is
        # part of the **lower-left-field input to the right
        # face-recognition network** (right V4v → LOC → right
        # FFA). **This is a left-hemisphere-specific absence on
        # the left side** (the left cuneus does not contribute
        # to the face network).

    LATERALIZATION_NOTE = "medial_surface_landmark_for_V1_upper_bank"
        # The cuneus's lateralization role is **not** a verbal /
        # spatial asymmetry — it is the **contralateral visual
        # field rule**, applied to the upper bank of the
        # calcarine sulcus.

    __all__ = [
        "GYRUS_NAME",
        "HEMISPHERE",
        "LOBE",
        "ALTERNATE_NAMES",
        "BOUNDING_SULCI",
        "FUNCTIONAL_OVERLAYS",
        "PRIMARY_OVERLAY",
        "V1_BANK_SIDE",
        "REPRESENTED_FIELD",
        "VISUAL_HEMIFIELD",
        "LEFT_LATERALIZED_FUNCTIONS",
        "RIGHT_ONLY_DOMAINS",
        "LATERALIZATION_NOTE",
    ]

No behaviour. This package is a declarative descriptor; all
computation that references the cuneus lives in ``cortex/`` or
``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this package's own
structural fields.** The cuneus's structural neighbours — the
calcarine sulcus, the parieto-occipital sulcus, the lateral occipital
gyrus, the lingual gyrus, and the V1 / V2 / V3 functional areas —
all exist as packages or as documented forward references in the
tree. The **lingual gyrus** is a forward reference in ``..gyri``, but
the cuneus package does not depend on it — the lingual gyrus is a
surface landmark for the lower bank of the calcarine sulcus, and the
cuneus's own structural fields resolve fully.

**The one open question is the placement of the lingual gyrus.**
When the lingual gyrus is added to the tree, it should be placed
**either** at the ``..occipital`` parent level (**like the cuneus**,
because it is the lower-bank V1 surface landmark) **or** under
``..gyri`` (**as a lateral-surface gyral child**). **The placement
decision must be made in the same commit as the lingual gyrus's
creation, in both hemispheres**, and it must preserve the **cuneus /
lingual gyrus symmetry** — the two gyri are the upper and lower
banks of the calcarine sulcus, and their placements should be
symmetric.

**This caveat is byte-identical to the left sibling's** — the
lingual gyrus placement question is a property of the occipital
lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a cuneus sub-region becomes a package)
--------------------------------------------------------------------------------

The cuneus is **architectonically homogeneous as a gyrus** (it is
a single fold of cortex), but its **functional overlays are
distinct**: V1 at the lower margin, V2 at the more dorsal extent,
V3d at the lateral and dorsal extent. **The cuneus is NOT
recommended to be split by functional overlay** — the overlays are
already modelled in ``..cortex`` (the V areas), and splitting the
cuneus by V area would duplicate the V-area decomposition.

**The one natural split is the cuneus's dorsal / ventral
division** — some parcellations distinguish a **dorsal cuneus**
and a **ventral cuneus** by the exact position along the
parieto-occipital-to-occipital-pole axis. **This split is not
recommended** — the cuneus is a single gyral fold, and its dorsal /
ventral extent is continuous.

**No SUBDIVISIONS promotion is recommended in the current tree.**
The cuneus is best kept as a single gyral package that
cross-references the V1 / V2 / V3d overlays via
``FUNCTIONAL_OVERLAYS``.

**If a future parcellation nevertheless splits the cuneus by
functional overlay** (e.g., a separate ``v1_upper_bank_cuneus`` and
``v2_dorsal_cuneus``), the promotion must **mirror the V-area
decomposition** — the ``cortex`` parent's V1, V2, V3 packages would
need to declare the corresponding cuneus sub-packages as their
anatomical substrates. **The promotion must be mirrored on the
right side in the same commit**, and it must preserve the
**cuneus / lingual gyrus symmetry** — the lingual gyrus's lower-
bank V1 / V2 territory would need a corresponding split.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../cuneus``:

    MUST be identical (byte-for-byte):
        GYRUS_NAME                   "cuneus"
        LOBE                         "occipital"
        ALTERNATE_NAMES              ("cuneus_gyrus",
                                     "medial_occipital_wedge",
                                     "cuneate_lobule")
        BOUNDING_SULCI               parieto-occipital (rostral),
                                     calcarine (caudal), lateral
                                     occipital sulcus / margin
        FUNCTIONAL_OVERLAYS          V1 dorsal bank, V2 dorsal
                                     bank, V3d — the same
                                     three overlays
        PRIMARY_OVERLAY              "primary_visual_cortex_
                                     dorsal_bank"
        V1_BANK_SIDE                 "upper" — the cuneus's
                                     lower margin is the upper
                                     bank of the calcarine sulcus
        REPRESENTED_FIELD            "lower_contralateral"
        The medial-surface placement (parent-level position)
        The lingual-gyrus symmetry note
        The lingual-gyrus placement caveat text (byte-
                                     identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "right" (left) vs "left" (right)
        LEFT_LATERALIZED_FUNCTIONS
                               left: ("right_hemifield_lower_
                               field_reading_input",) — the
                               left cuneus contributes to the
                               left reading network.
                               right: () — the right cuneus
                               does not contribute to the
                               reading network.
        RIGHT_ONLY_DOMAINS     left: () — the left cuneus does
                               not contribute to the face
                               network.
                               right: ("face_processing",) —
                               the right cuneus contributes to
                               the right face network.
        LATERALIZATION_NOTE    same value (medial_surface_
                               landmark_for_V1_upper_bank), but
                               the downstream network emphasis
                               differs as noted above.
        CLINICAL_ANCHORS       left: right upper-quadrantic
                               visual field defect, right-
                               hemifield reading deficit,
                               motion-boundary deficit
                               (milder than right), migraine
                               aura, occipital epilepsy,
                               occipital infarct, PCA, PRES.
                               right: left upper-quadrantic
                               visual field defect, left-
                               hemifield face-processing
                               contribution (via prosopagnosia),
                               motion-boundary deficit (more
                               severe), migraine aura,
                               occipital epilepsy, occipital
                               infarct, PCA (Benson syndrome),
                               PRES.

**The visual-hemifield asymmetry is the sharpest single entry in this
contract.** The left cuneus's V1 upper bank represents the **lower
RIGHT** field; the right cuneus's V1 upper bank represents the
**lower LEFT** field. This is the same contralateral rule that
applies throughout the occipital lobe, applied to the cuneus
specifically.

**The `LEFT_LATERALIZED_FUNCTIONS` / `RIGHT_ONLY_DOMAINS` pair is the
second sharpest entry.** The left cuneus contributes to the **left
reading network** (its V1 upper-bank representation is part of the
lower-right-field input to the left VWFA); the right cuneus
contributes to the **right face network** (its V1 upper-bank
representation is part of the lower-left-field input to the right
FFA). **The two contributions are mirror-opposite**, and they
reflect the different downstream endpoints of the left and right
ventral streams.

**The three V overlays (V1, V2, V3d), the bounding sulci, the
V1_BANK_SIDE, the REPRESENTED_FIELD, and the parent-level placement
are byte-identical on both sides.** They are properties of the
cuneus's anatomy, not of the hemisphere.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "cuneus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "occipital".
[ ] ALTERNATE_NAMES includes "cuneus_gyrus",
    "medial_occipital_wedge", and "cuneate_lobule".
[ ] BOUNDING_SULCI documents the three boundaries:
    - rostral: parieto-occipital sulcus
    - caudal: calcarine sulcus
    - lateral: lateral occipital sulcus / margin
[ ] FUNCTIONAL_OVERLAYS is byte-identical to the right sibling's:
    V1 dorsal bank, V2 dorsal bank, V3d.
[ ] PRIMARY_OVERLAY is "primary_visual_cortex_dorsal_bank" —
    **V1 is the cuneus's defining functional overlay**.
[ ] V1_BANK_SIDE is "upper" — **the cuneus's lower margin is the
    upper bank of the calcarine sulcus**.
[ ] REPRESENTED_FIELD is "lower_contralateral" — **on the left,
    the lower RIGHT field**.
[ ] **VISUAL_HEMIFIELD = "right"** is present as a first-class
    field.
[ ] **The parent-level placement is documented** — the cuneus is
    a direct child of ``..occipital``, **not** of ``..gyri`` —
    because its primary functional identity is the V1 upper-bank
    surface landmark.
[ ] **The cuneus / paracentral lobule symmetry is documented** —
    both are medial-surface gyral / lobular territories that
    function as surface landmarks for primary sensory cortex,
    and both are placed at the parent level for the same reason.
[ ] LEFT_LATERALIZED_FUNCTIONS contains
    "right_hemifield_lower_field_reading_input" — the left
    cuneus contributes to the left reading network.
[ ] RIGHT_ONLY_DOMAINS contains "face_processing" — **this is a
    left-side absence anchor**, documenting that the left cuneus
    does **not** contribute to the right face network at the
    same weighting as the right cuneus does.
[ ] LATERALIZATION_NOTE is
    "medial_surface_landmark_for_V1_upper_bank" — the cuneus's
    lateralization role is the contralateral visual field rule,
    **not** a verbal / spatial asymmetry.
[ ] CLINICAL_ANCHORS contains the left-specific anchors:
    - left_cuneus_right_upper_quadrantic_visual_field_defect
    - left_cuneus_right_hemifield_reading_deficit
    - left_cuneus_motion_boundary_deficit
    - left_cuneus_migraine_visual_aura
    - left_cuneus_occipital_epilepsy_visual_auras
    - left_cuneus_occipital_infarct_pca_territory
    - left_cuneus_posterior_cortical_atrophy
    - left_cuneus_pres_visual_symptoms
[ ] The **right upper-quadrantic visual field defect** is
    documented as the primary left cuneus anchor.
[ ] The **right-hemifield reading deficit** is documented as the
    left-lateralized downstream anchor — the cuneus's V1 upper
    bank is part of the lower-right-field input to the left
    reading network.
[ ] The **motion-boundary deficit** is documented as a
    secondary V3d-overlay anchor (milder than the right's).
[ ] The **fusiform gyrus (V4v)** and **lateral occipital gyrus
    (V4d)** are **not** cuneus territory — the cuneus is
    V1 / V2 / V3d, not V4. The docstring correctly lists the
    cuneus's overlays as V1 / V2 / V3d, **not** V4.
[ ] The **V1 / V2 mirror-flip** is documented — **V1's upper
    field is on the lower bank (lingual gyrus), V2's upper field
    is on the upper bank (cuneus)** — and the cuneus spans both
    banks of the mirror.
[ ] The **cuneus's lower margin is the upper bank of the
    calcarine sulcus** is documented as the V1 dorsal
    representation of the lower contralateral field.
[ ] The **lingual gyrus** is documented as the cuneus's caudal
    neighbour via the calcarine sulcus, with the same
    caveats about the lingual gyrus's forward-reference status.
[ ] The **parieto-occipital sulcus** is documented as the
    cuneus's rostral boundary, separating it from the precuneus.
[ ] No forward-declaration caveat is needed for the cuneus's
    structural fields. The **lingual gyrus placement caveat** is
    byte-identical to the right sibling's.
[ ] No SUBDIVISIONS promotion is recommended — the cuneus is a
    single gyral fold, and the V-area decomposition already
    lives in ``..cortex``.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (GYRUS_NAME, LOBE, ALTERNATE_NAMES, BOUNDING_SULCI,
    FUNCTIONAL_OVERLAYS, PRIMARY_OVERLAY, V1_BANK_SIDE,
    REPRESENTED_FIELD, parent-level placement, lingual gyrus
    caveat text) match the right sibling; VISUAL_HEMIFIELD,
    LEFT_LATERALIZED_FUNCTIONS, RIGHT_ONLY_DOMAINS, and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the left
    cuneus carries "right_hemifield" (via "lower_
    contralateral" and "lower RIGHT"), and the right cuneus
    carries "left_hemifield."
[ ] **The reading-vs-face downstream asymmetry is verified**:
    the left cuneus carries "right_hemifield_lower_field_
    reading_input" and the right cuneus carries "face_
    processing" — the two are mirror-opposite.
[ ] **The V1 / V2 mirror-flip is verified** — V1's upper field
    is on the lower bank (lingual gyrus), V2's upper field is
    on the upper bank (cuneus). **This is a fundamental
    structural fact about the cuneus**, and it is byte-
    identical on both sides.
[ ] Any downstream code querying "what does the left cuneus
    see?" must receive "the lower RIGHT visual field" (via the
    V1 upper-bank representation) **and** the cuneus's V2 /
    V3d overlays carry the lower RIGHT field as well.
[ ] Any downstream code querying "what is the cuneus?" must
    receive "the medial-surface wedge gyrus of the occipital
    lobe, whose lower margin is the upper bank of the
    calcarine sulcus (V1 dorsal representation) and whose more
    dorsal extent overlaps V2 and V3d."
[ ] Any downstream code querying "is the cuneus a child of
    ``..gyri``?" must receive "**no** — it is a direct child
    of ``..occipital``, because its primary functional identity
    is the V1 upper-bank surface landmark, not a generic gyral
    fold."
[ ] Any downstream code assigning the left reading pathway must
    note that **the left cuneus's V1 upper-bank representation
    is part of the lower-right-field input** to the left V4v →
    LOC → left VWFA pathway.
[ ] Any downstream code assigning the right face pathway must
    note that **the right cuneus's V1 upper-bank representation
    is part of the lower-left-field input** to the right V4v →
    LOC → right FFA pathway (documented in the right sibling).
"""