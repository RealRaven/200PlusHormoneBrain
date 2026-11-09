"""
Cuneus — Right Hemisphere
==========================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── occipital
                              └── cuneus   ← THIS PACKAGE

This is a **leaf gyral package** describing the right hemisphere's
**cuneus** — the **wedge-shaped medial-surface gyrus** between the
**parieto-occipital sulcus** (rostrally) and the **calcarine sulcus**
(caudally). It is **not** a child of ``..gyri`` — it sits at the
**``..occipital`` parent level**, alongside ``brodmann_areas``,
``cortex``, ``gyri``, and ``sulci``.

Parent: ``..occipital`` — the right occipital lobe. Sibling to
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
reason.

This package is the **structural mirror** of
``../../left/cortex/occipital/cuneus``. The gyrus name, the bounding
sulci (parieto-occipital and calcarine), the V1 upper-bank overlay,
and the medial-surface placement are identical on both sides; the
**functional emphasis** and **clinical significance** diverge — on
the right, the cuneus's V1 upper-bank representation carries the
**lower LEFT visual field**, and right cuneus lesions produce
**left upper-quadrantic visual field defects** that can contribute
to **prosopagnosia** (via the right face pathway) and to the
**right-lateralized face-recognition network's** upper-field
deficit. **The right cuneus's V3d territory contributes to the
right-lateralized motion-boundary and depth-from-motion substrate
more strongly than the left's.** The left cuneus carries the mirror
arrangement (lower RIGHT field, right upper-quadrantic defects,
hemianopic alexia and left-lateralized reading-network
contributions).

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
pole and its base along the parieto-occipital sulcus.

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

**On the right, the cuneus's V1 upper bank represents the lower LEFT
visual field** — the dorsal V1 neurons that respond to stimuli in the
lower half of the left hemifield.

**The cuneus also extends beyond V1** — its rostral and dorsal
portions are partially V2 (and V3) territory, and its lateral aspect
is V3d territory. **The cuneus's V1 territory is the lower margin**
(the banks of the calcarine sulcus); the more dorsal portions are
extrastriate. **This is why the cuneus's functional overlays are
listed as `primary_visual_cortex_dorsal_bank` (V1), plus
`secondary_visual_cortex_dorsal_bank` (V2), plus
`tertiary_visual_cortex_v3d`** — the cuneus contains portions of
V1, V2, and V3d, with **V1 at its lower margin**, **V2 / V3d at its
more dorsal extent**.

**The cuneus does not contain the fovea.** The fovea is at the
**occipital pole** — the **caudal convergence** of the cuneus and
lingual gyrus. The cuneus proper (the wedge) represents the **lower
contralateral peripheral field** more than the foveal field. **This
is why cuneus lesions typically produce peripheral field defects**
(macular sparing is common, because the fovea is at the pole).

**Right-hemisphere specificity**: the right cuneus's V1 upper-bank
representation carries the **lower LEFT visual field**, and its
V2 / V3d extensions contribute to the **left hemifield's V2 / V3d
processing** (motion boundaries, depth from motion, kinetic form).
**Right cuneus lesions produce left upper-quadrantic field defects**
— the dorsal V1 upper-bank damage removes the lower-left-field
representation, producing a defect in the left field's lower half,
which in a completed hemianopia presents as the **upper-quadrantic
defect**. **Right cuneus / V1 upper-bank damage can contribute to
prosopagnosia** (via loss of left-hemifield input to the right
face-recognition network) and to the **right-lateralized face-
recognition deficits** that depend on the full left hemifield.

**The right cuneus's V3d territory is more strongly engaged than the
left's** — the right V3d is the dominant motion-boundary and motion-
in-depth substrate, and the cuneus's V3d portion feeds the right
MT/V5 and the right dorsal attention network. **Right cuneus lesions
that extend into V3d produce more severe motion-boundary and depth-
from-motion deficits** than the left equivalent.

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
            field**. **On the right, the lower LEFT field.**
        secondary_visual_cortex_dorsal_bank (V2)
            The **more dorsal** portion of the cuneus carries the
            **V2 upper-bank representation of the lower
            contralateral visual field**. **On the right, the
            lower LEFT field.** Note the **V1 / V2 mirror-flip**:
            V1's upper field is on the **lower bank** (lingual
            gyrus), while V2's upper field is on the **upper
            bank** (cuneus).
        tertiary_visual_cortex_v3d (V3d)
            The **lateral and dorsal** portion of the cuneus
            overlaps V3d — the **motion-boundary and
            motion-in-depth** area that projects to MT/V5.
            **On the right, V3d is the DOMINANT motion
            substrate** — the right V3d → right MT/V5 → right
            IPS pathway is the dominant dorsal-attention
            substrate, and the right cuneus's V3d territory is
            more strongly engaged than the left's.

**This field is structurally identical to the left sibling's** — the
bounding sulci and the three V overlays are the same on both sides.
What differs is the **visual hemifield** — the right cuneus carries
the lower LEFT field — the **V3d weighting** — the right's V3d is
the dominant motion substrate — and the **downstream clinical
emphasis** — the right cuneus contributes to the right-lateralized
face-recognition network, while the left cuneus contributes to the
left-lateralized reading network.

--------------------------------------------------------------------------------
GYRUS-TO-NEIGHBOUR ADJACENCY
--------------------------------------------------------------------------------

    Neighbour                              Relationship
    -------------------------------------  ------------------------------
    precuneus (parietal lobe)              **rostral neighbour** via the
                                           **parieto-occipital sulcus**.
                                           The precuneus is in the
                                           parietal lobe, not the
                                           occipital lobe.
    lingual gyrus (medial-surface          **caudal neighbour** via the
    gyrus; forward reference in ..gyri)    **calcarine sulcus**. **The
                                           V1 representation is split
                                           between them**: the upper
                                           bank (cuneus) carries
                                           the lower field (**lower
                                           LEFT on the right**),
                                           the lower bank (lingual
                                           gyrus) carries the upper
                                           field (**upper LEFT on
                                           the right**).
    lateral occipital gyrus                **lateral neighbour** via
                                           the **lateral occipital
                                           sulcus / lateral margin**.
                                           **On the right, feeds the
                                           right V4d / LOC.**
    calcarine sulcus (defining sulcus)     **the cuneus's most
                                           consequential sulcal
                                           boundary** — the upper
                                           bank of the calcarine
                                           sulcus is the **lower
                                           margin of the cuneus**,
                                           and it carries the dorsal
                                           V1 representation. **On
                                           the right, the lower LEFT
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
topological, not lateralized. The field labels (LEFT vs RIGHT) in the
lingual and lateral occipital gyrus entries are updated for the right
hemisphere.

--------------------------------------------------------------------------------
FUNCTIONAL OVERLAYS (right-hemisphere emphasis)
--------------------------------------------------------------------------------

The cuneus's functional identity is dominated by **one primary
overlay** (V1) plus **two secondary overlays** (V2 and V3d). The
right-side emphasis is:

    primary_visual_cortex_dorsal_bank (V1)         (PRIMARY overlay)
        **The cuneus's defining functional overlay.** The **lower
        margin of the cuneus** — the upper bank of the calcarine
        sulcus — is the **seat of the dorsal V1 representation
        of the lower contralateral visual field**. **On the
        right, the lower LEFT field.** The V1 upper bank is
        continuous with the V1 lower bank (the lingual gyrus) at
        the **fundus of the calcarine sulcus** (the horizontal
        meridian).

    secondary_visual_cortex_dorsal_bank (V2)       (SECONDARY overlay)
        **The more dorsal portion of the cuneus** overlaps V2's
        upper bank. **On the right, V2's upper-bank
        representation carries the lower LEFT field** (which,
        because of the V1 / V2 mirror-flip, is also V1's upper-
        bank representation of the same field).

    tertiary_visual_cortex_v3d (V3d)               (SECONDARY overlay)
        **The lateral and dorsal** portion of the cuneus overlaps
        V3d. **On the right, V3d is the DOMINANT motion
        substrate** — the right V3d → right MT/V5 → right IPS
        pathway is the dominant dorsal-attention substrate, and
        the right cuneus's V3d territory is the more strongly
        engaged side.

**Right-specific caveat on the face pathway.** The cuneus's V1
upper-bank representation is the **lower-left-field input** to the
**right face-recognition network**. **On the right, the cuneus's V1
upper bank is part of the input stage of the right V4v → LOC →
right FFA pathway** — the face-recognition pathway that processes
faces in the left hemifield. **A right cuneus lesion that removes
the lower-left-field representation can contribute to
prosopagnosia** when the downstream right FFA is also affected.

**Right-specific caveat on the reading pathway.** The cuneus's V1
upper-bank representation is **not** part of the left reading
network — that is the left cuneus's contribution. **The right
cuneus does not carry a reading-pathway overlay** — its upper-bank
V1 representation feeds the right face pathway, not the left reading
pathway.

**Right-specific caveat on motion-boundary processing.** The right
cuneus's V3d territory is **the dominant motion-boundary and depth-
from-motion substrate**. **Right cuneus lesions that extend into V3d
produce more severe motion-boundary and depth-from-motion deficits
than the left equivalent** — this is the mirror of the left's
milder V3d contribution.

**Summary**: The cuneus's functional identity is **dominated by V1**
(the lower margin's upper-bank representation), with **V2 and V3d as
secondary overlays**. **The functional overlay set is identical
across hemispheres** — both cunei carry V1, V2, and V3d. The right-
left differences are:
(a) the **represented visual field** (right = lower LEFT, left =
lower RIGHT);
(b) the **downstream network** (right cuneus → right face pathway;
left cuneus → left reading pathway);
(c) the **V3d weighting** (right V3d is dominant, left V3d is
weaker).

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_cuneus_left_upper_quadrantic_visual_field_defect
        **This is the right cuneus anchor par excellence.** A
        lesion of the right cuneus — specifically, the **lower
        margin** of the cuneus (the upper bank of the calcarine
        sulcus) — produces a **left upper-quadrantic** visual
        field defect: loss of the **upper** portion of the
        **left** visual field. **The mechanism** is the mirror
        of the left cuneus's: the upper bank of the calcarine
        sulcus represents the **lower contralateral field**, so
        a partial lesion affecting only the dorsal portion of the
        cuneus produces a quadrantic defect in the left field.
        **Often with macular sparing** (the fovea is at the
        occipital pole, away from the cuneus proper).

    right_cuneus_left_hemifield_face_processing_deficit
        **The right cuneus's role in the right face pathway.**
        The cuneus's V1 upper-bank representation is part of the
        **lower-left-field input** to the **right face-
        recognition network**. **Right cuneus lesions can
        contribute to prosopagnosia** when the downstream right
        FFA is also affected. **The deficit is more face-specific
        than a V2 or V3 lesion** because the cuneus's V1 input
        is the **primary visual** input to the right face
        pathway. **This anchor has no symmetric counterpart on
        the left** — the left cuneus feeds the left reading
        pathway, not a face pathway.

    right_cuneus_motion_boundary_deficit_more_severe
        **The cuneus's V3d territory — the dominant motion
        substrate on the right.** The lateral and dorsal portion
        of the cuneus overlaps V3d. **Right cuneus lesions that
        extend into V3d produce more severe motion-boundary and
        depth-from-motion deficits** in the left hemifield than
        the left equivalent. **This anchor is more severe than
        the left cuneus's motion-boundary deficit** — the right
        V3d is the dominant motion-boundary substrate.

    right_cuneus_left_hemifield_neglect_contribution
        **Right-emphasized.** Right cuneus lesions that extend
        into the adjacent right V3d / right MT/V5 territory
        contribute to **left hemispatial neglect** when the
        lesion extends further into the right parietal and
        right frontal territories. **Isolated right cuneus
        lesions do not produce neglect** — the patient has a
        left quadrantic field defect but can attend to the left
        field cognitively — but the right cuneus's V3d territory
        is part of the right dorsal attention network substrate.
        **This anchor has no symmetric counterpart on the left.**

    right_cuneus_migraine_visual_aura
        **Migraine visual aura** — the transient, bilateral,
        scintillating scotomata and fortification spectra that
        precede a migraine headache — reflects **cortical
        spreading depression** spreading across the **occipital
        cortex**, including the **cuneus's V1 upper bank** and
        its V2 and V3d territories. **The cuneus contribution
        is the propagation of the aura into the lower-left-field
        features** (lower-field fortifications, lower-field
        scotomata). **This anchor is hemisphere-invariant**, but
        the field involvement is contralateral (lower-left field
        on the right side).

    right_cuneus_occipital_epilepsy_visual_auras
        **Occipital lobe epilepsy** with **visual auras** can
        arise from the **cuneus's V1 upper bank** — the auras
        project to the **lower left visual field** on the right
        side. **The cuneus's auras are typically elementary**
        (flashes, shapes, scotomata) because the cuneus's
        territory is primarily V1.

    right_cuneus_occipital_infarct_pca_territory
        **Right posterior cerebral artery (PCA) infarct** can
        involve the cuneus and produce a **left upper-quadrantic
        defect** — often with macular sparing. **The cuneus's
        contribution to the infarct's clinical signature** is
        the **quadrantic specificity** of the field defect.
        **Isolated right PCA infarcts do not produce alexia
        without agraphia** — that syndrome is left-lateralized.

    right_cuneus_posterior_cortical_atrophy_benson_syndrome
        **Posterior cortical atrophy (PCA)** — a variant of
        Alzheimer's disease presenting with progressive visual
        dysfunction — involves the **cuneus** in later stages.
        **Right cuneus** is part of the substrate of the
        **progressive dorsal-stream dysfunction** that produces
        **Benson syndrome** — progressive prosopagnosia,
        visuospatial deficits, optic ataxia, simultanagnosia.
        **On the right, PCA presents with the visuospatial /
        prosopagnosic syndrome**; on the left, with the
        progressive reading deficits.

    right_cuneus_pres_visual_symptoms
        **PRES (posterior reversible encephalopathy syndrome)** —
        a clinicoradiological syndrome of vasogenic edema in the
        posterior cerebral circulation — can involve the cuneus
        and produce **cortical blindness, quadrantic field
        defects, or visual hallucinations**. **The syndrome is
        reversible** in most cases.

**The cuneus-specific clinical anchors** — `right_cuneus_left_
upper_quadrantic_visual_field_defect`,
`right_cuneus_left_hemifield_face_processing_deficit`,
`right_cuneus_motion_boundary_deficit_more_severe`, and
`right_cuneus_left_hemifield_neglect_contribution` — are the
**right-emphasized mirror** of the left cuneus anchors. **The left
upper-quadrantic defect is the primary anchor**, the **face-
processing deficit is right-specific** (the right cuneus contributes
to the right face pathway; the left cuneus does not), the **motion-
boundary deficit is more severe on the right** (the right V3d is
dominant), and the **neglect contribution is right-only** (via the
right V3d → MT/V5 → right IPS dorsal attention pathway).

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..occipital  (parent)
    The right occipital lobe. This package's parent.

..brodmann_areas
    The **cytoarchitectonic sibling**. **The cuneus's V1 territory
    is BA 17, its V2 territory is BA 18, and its V3d territory is
    BA 18 / BA 19.**

..cortex
    The **functional sibling**. **The cuneus's V1 territory is
    `primary_visual_cortex`, its V2 territory is `v2`, and its
    V3d territory is `v3`.** **On the right, the cuneus's V3d
    territory is more strongly engaged than the left's.**

..gyri
    The **lateral-surface gyral sibling**. The cuneus is the
    **medial-surface** counterpart of the lateral occipital gyrus.
    **The cuneus is not a child of ``..gyri``** because its
    primary functional identity is the V1 upper-bank surface
    landmark.

..sulci.calcarine_sulcus
    **The cuneus's defining sulcus.** The upper bank of the
    calcarine sulcus is the **lower margin of the cuneus**, and
    it carries the dorsal V1 representation. **On the right, the
    lower LEFT visual field.**

..sulci.parieto_occipital_sulcus
    **The cuneus's rostral boundary.** Separates the cuneus from
    the precuneus.

..sulci.lunate_sulcus
    The inconstant lateral-surface sulcus marking the V1 / V2
    border. **Not a cuneus boundary.**

..sulci.transverse_occipital_sulcus
    The dorsal-surface landmark for the V3A / V3B territory. **Not
    a cuneus boundary.**

..cortex.temporal
    The **ventral stream** continues from the cuneus's V1 / V2 /
    V3d territory (via the right V4v → LOC → right FFA pathway)
    into the temporal lobe. **On the right, the cuneus's upper-
    bank V1 representation is part of the left-hemifield input
    to the right FFA (faces).** **Right occipito-temporal
    lesions produce prosopagnosia** — the canonical right-
    lateralized visual-recognition deficit.

..cortex.parietal
    The **dorsal stream** continues from the cuneus's V3d
    territory (via MT/V5 → right IPS) into the parietal lobe.
    **On the right, the cuneus's V3d contribution is the
    DOMINANT dorsal-stream substrate** — the right V3d → right
    MT/V5 → right IPS pathway is the dominant motion-boundary
    and spatial-attention substrate.

..cortex.frontal
    The **frontal eye fields** (BA 8) and **dorsolateral
    prefrontal cortex** (BA 9 / BA 46) send top-down visual
    attentional signals to the cuneus's V1 and V2 territory.
    **On the right, the right FEF is the dominant node of the
    ventral attention network**, and right frontal lesions
    contribute to left hemispatial neglect.

..cortex.cingulate  — indirect
    No direct cingulate → cuneus projection.

..cortex.insular  — indirect
    No direct insular → cuneus projection.

../../subcortical/diencephalon/thalamus/lateral_geniculate_body
    The **LGN** is the **indirect** source of the cuneus's V1
    input via the V1 relay.

../../subcortical/medial_temporal_lobe/hippocampus
    The cuneus's V1 / V2 output reaches the hippocampus via the
    ventral stream (V4v → LOC → inferotemporal → perirhinal →
    hippocampus). **On the right, the parahippocampal place
    area (PPA) and the retrosplenial complex receive visual
    input supporting scene and spatial memory**, which are more
    strongly right-lateralized.

../../left/cortex/occipital/cuneus
    The left-hemisphere homologue. Structural fields (gyrus
    name, bounding sulci, V1 / V2 / V3d overlays, medial-surface
    placement, parent-level position, lingual-gyrus caveat
    text) MUST be byte-identical. Functional emphasis and
    clinical significance diverge — the left cuneus carries
    the **lower RIGHT visual field**, and left cuneus lesions
    produce **right upper-quadrantic visual field defects**
    that can contribute to **hemianopic alexia** and to the
    **left-lateralized reading network's** upper-field deficit.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    GYRUS_NAME          = "cuneus"
    HEMISPHERE          = "right"
    LOBE                = "occipital"

    ALTERNATE_NAMES     = ("cuneus_gyrus",
                           "medial_occipital_wedge",
                           "cuneate_lobule")
        # **Byte-identical to the left sibling's.**

    BOUNDING_SULCI      = {
                              "rostral":    ("parieto_occipital_"
                                             "sulcus",),
                              "caudal":     ("calcarine_sulcus",),
                              "lateral":    ("lateral_occipital_"
                                             "sulcus_or_margin",),
                          }
        # **Byte-identical to the left sibling's.**

    FUNCTIONAL_OVERLAYS = (
                              "primary_visual_cortex_dorsal_bank",
                              "secondary_visual_cortex_dorsal_bank",
                              "tertiary_visual_cortex_v3d",
                          )
        # **Byte-identical to the left sibling's.**

    PRIMARY_OVERLAY     = "primary_visual_cortex_dorsal_bank"
        # **Byte-identical to the left sibling's.** The cuneus's
        # defining functional identity is its V1 upper-bank
        # representation.

    V1_BANK_SIDE        = "upper"
        # **Byte-identical to the left sibling's.** The cuneus's
        # lower margin is the upper bank of the calcarine sulcus.

    REPRESENTED_FIELD   = "lower_contralateral"
        # **On the right, the lower LEFT visual field.**

    VISUAL_HEMIFIELD    = "left"
        # **The represented visual hemifield** — right cuneus
        # processes the lower LEFT field.

    RIGHT_LATERALIZED_FUNCTIONS = (
        "left_hemifield_lower_field_face_input",
    )
        # The right cuneus's V1 upper-bank representation is
        # part of the **lower-left-field input to the right
        # face-recognition network** (right V4v → LOC → right
        # FFA). **This is the mirror of the left cuneus's
        # `LEFT_LATERALIZED_FUNCTIONS` "right_hemifield_lower_
        # field_reading_input".**

    LEFT_ONLY_DOMAINS   = (
        "right_hemifield_lower_field_reading_input",
    )
        # The left-only function that the right cuneus does
        # **not** carry. **This is the mirror of the left
        # cuneus's `RIGHT_ONLY_DOMAINS` "face_processing".**

    LATERALIZATION_NOTE = "medial_surface_landmark_for_V1_upper_bank"
        # **Byte-identical to the left sibling's.**

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
        "RIGHT_LATERALIZED_FUNCTIONS",
        "LEFT_ONLY_DOMAINS",
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
the cuneus package does not depend on it.

**The one open question is the placement of the lingual gyrus.**
When the lingual gyrus is added to the tree, it should be placed
**either** at the ``..occipital`` parent level (**like the cuneus**)
**or** under ``..gyri`` (**as a lateral-surface gyral child**).
**The placement decision must be made in the same commit as the
lingual gyrus's creation, in both hemispheres**, and it must
preserve the **cuneus / lingual gyrus symmetry**.

**This caveat is byte-identical to the right sibling's** — the
lingual gyrus placement question is a property of the occipital
lobe, not of the hemisphere.

--------------------------------------------------------------------------------
PROMOTION RULE (when a cuneus sub-region becomes a package)
--------------------------------------------------------------------------------

The cuneus is **architectonically homogeneous as a gyrus**, but its
**functional overlays are distinct** (V1 at the lower margin, V2 at
the more dorsal extent, V3d at the lateral and dorsal extent). **The
cuneus is NOT recommended to be split by functional overlay** — the
overlays are already modelled in ``..cortex``.

**No SUBDIVISIONS promotion is recommended in the current tree.**

**If a future parcellation nevertheless splits the cuneus by
functional overlay**, the promotion must **mirror the V-area
decomposition** — the ``cortex`` parent's V1, V2, V3 packages would
need to declare the corresponding cuneus sub-packages as their
anatomical substrates. **The promotion must be mirrored on the left
side in the same commit**, and it must preserve the **cuneus /
lingual gyrus symmetry**.

**On the right, the V3d sub-package is the more consequential** —
the right V3d is the dominant motion-boundary and depth-from-motion
substrate, and its clinical anchors (the more severe motion-boundary
and depth-from-motion deficits) would need to be declared on the
right V3d sub-package, not on the parent cuneus.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../cuneus``:

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
                                     bank, V3d
        PRIMARY_OVERLAY              "primary_visual_cortex_
                                     dorsal_bank"
        V1_BANK_SIDE                 "upper"
        REPRESENTED_FIELD            "lower_contralateral"
        LATERALIZATION_NOTE          "medial_surface_landmark_for_
                                     V1_upper_bank"
        The medial-surface placement (parent-level position)
        The lingual-gyrus caveat text (byte-identical)

    MUST differ (and the difference must be documented here):
        HEMISPHERE             "left" vs "right"
        VISUAL_HEMIFIELD       "left" (right) vs "right" (left)
        RIGHT_LATERALIZED_FUNCTIONS
                               right: ("left_hemifield_lower_
                               field_face_input",) — the right
                               cuneus contributes to the right
                               face network.
                               left: () — the left cuneus does
                               not carry RIGHT_LATERALIZED_
                               FUNCTIONS (it uses LEFT_
                               LATERALIZED_FUNCTIONS instead).
        LEFT_ONLY_DOMAINS      right: ("right_hemifield_lower_
                               field_reading_input",) — the
                               left-only function the right
                               cuneus does not carry.
                               left: () — the left cuneus uses
                               RIGHT_ONLY_DOMAINS instead.
        The complementary mapping of the two lateralized-domain
                               tuples:
                                   left.LEFT_LATERALIZED_
                                     FUNCTIONS
                                   ≡ (mirror) right.RIGHT_
                                     LATERALIZED_FUNCTIONS
                                   left.RIGHT_ONLY_DOMAINS
                                   ≡ (mirror) right.LEFT_ONLY_
                                     DOMAINS
        CLINICAL_ANCHORS       right: left upper-quadrantic
                               visual field defect, left-
                               hemifield face-processing
                               contribution (prosopagnosia via
                               right FFA input), **motion-boundary
                               deficit more severe**, **left
                               hemifield neglect contribution**,
                               migraine aura, occipital epilepsy,
                               occipital infarct, PCA (Benson
                               syndrome), PRES.
                               left: right upper-quadrantic
                               visual field defect, right-
                               hemifield reading deficit,
                               motion-boundary deficit
                               (milder), migraine aura,
                               occipital epilepsy, occipital
                               infarct, PCA, PRES.

**The visual-hemifield asymmetry is the sharpest single entry.** The
right cuneus's V1 upper bank represents the **lower LEFT** field.
This is the same contralateral rule applied to the cuneus, with the
hemisphere flipped.

**The reading-vs-face downstream asymmetry is the second sharpest
entry.** `RIGHT_LATERALIZED_FUNCTIONS` on the right
(`("left_hemifield_lower_field_face_input",)`) mirrors
`LEFT_LATERALIZED_FUNCTIONS` on the left
(`("right_hemifield_lower_field_reading_input",)`). `LEFT_ONLY_
DOMAINS` on the right (`("right_hemifield_lower_field_reading_
input",)`) mirrors `RIGHT_ONLY_DOMAINS` on the left
(`("face_processing",)`). **The two contributions are
mirror-opposite**, and they reflect the different downstream
endpoints of the right and left ventral streams.

**The right-specific clinical anchors are the third sharpest entry.**
The right cuneus carries **two additional anchors** that the left
does not carry at the same weighting: `right_cuneus_left_hemifield_
neglect_contribution` (via the right V3d → MT/V5 → right IPS dorsal
attention pathway) and the **more severe** motion-boundary deficit
(the right V3d is dominant). The **left-hemifield face-processing
deficit** is the right cuneus's mirror of the left's
`right-hemifield reading deficit`.

**The three V overlays, the bounding sulci, the V1_BANK_SIDE, the
REPRESENTED_FIELD, and the parent-level placement are byte-identical
on both sides.** They are properties of the cuneus's anatomy, not
of the hemisphere.

**The hemisphere-invariant anchors** — migraine aura, occipital
epilepsy, PCA (with the right's Benson subtype emphasis), PRES, and
occipital infarct — are **documented identically in both
siblings**.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] GYRUS_NAME is exactly "cuneus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "occipital".
[ ] ALTERNATE_NAMES is byte-identical to the left sibling's.
[ ] BOUNDING_SULCI is byte-identical to the left sibling's.
[ ] FUNCTIONAL_OVERLAYS is byte-identical to the left sibling's
    (V1 dorsal bank, V2 dorsal bank, V3d).
[ ] PRIMARY_OVERLAY is "primary_visual_cortex_dorsal_bank".
[ ] V1_BANK_SIDE is "upper".
[ ] REPRESENTED_FIELD is "lower_contralateral" — **on the right,
    the lower LEFT field**.
[ ] **VISUAL_HEMIFIELD = "left"** is present as a first-class
    field.
[ ] **The parent-level placement is documented** — the cuneus is
    a direct child of ``..occipital``, **not** of ``..gyri``.
[ ] **The cuneus / paracentral lobule symmetry is documented** —
    both are medial-surface gyral / lobular territories that
    function as surface landmarks for primary sensory cortex.
[ ] **RIGHT_LATERALIZED_FUNCTIONS** contains
    "left_hemifield_lower_field_face_input" — the right cuneus
    contributes to the right face network.
[ ] **LEFT_ONLY_DOMAINS** contains
    "right_hemifield_lower_field_reading_input" — the left-only
    function that the right cuneus does **not** carry.
[ ] **The complementarity invariant is verified across schemes**:
    - left's LEFT_LATERALIZED_FUNCTIONS (mirror) = right's
      RIGHT_LATERALIZED_FUNCTIONS
    - left's RIGHT_ONLY_DOMAINS (mirror) = right's LEFT_ONLY_
      DOMAINS
[ ] LATERALIZATION_NOTE is
    "medial_surface_landmark_for_V1_upper_bank".
[ ] CLINICAL_ANCHORS contains the right-specific anchors:
    - right_cuneus_left_upper_quadrantic_visual_field_defect
    - **right_cuneus_left_hemifield_face_processing_deficit**
    - **right_cuneus_motion_boundary_deficit_more_severe**
    - **right_cuneus_left_hemifield_neglect_contribution**
    - right_cuneus_migraine_visual_aura
    - right_cuneus_occipital_epilepsy_visual_auras
    - right_cuneus_occipital_infarct_pca_territory
    - right_cuneus_posterior_cortical_atrophy_benson_syndrome
    - right_cuneus_pres_visual_symptoms
[ ] The **left upper-quadrantic visual field defect** is
    documented as the primary right cuneus anchor.
[ ] The **left-hemifield face-processing deficit** is documented
    as the right-lateralized downstream anchor — the cuneus's
    V1 upper bank is part of the lower-left-field input to the
    right face network.
[ ] The **more severe motion-boundary deficit** is documented as
    a right-specific V3d-overlay anchor.
[ ] The **left hemifield neglect contribution** is documented as
    a right-emphasized anchor (via the right V3d → MT/V5 → right
    IPS dorsal attention pathway).
[ ] The **V1 / V2 mirror-flip** is documented — **V1's upper
    field is on the lower bank (lingual gyrus), V2's upper field
    is on the upper bank (cuneus)**.
[ ] The **cuneus's lower margin is the upper bank of the
    calcarine sulcus** is documented as the V1 dorsal
    representation of the lower contralateral field (**lower
    LEFT** on the right).
[ ] The **lingual gyrus** is documented as the cuneus's caudal
    neighbour via the calcarine sulcus.
[ ] The **parieto-occipital sulcus** is documented as the
    cuneus's rostral boundary.
[ ] No forward-declaration caveat is needed for the cuneus's
    structural fields. The **lingual gyrus placement caveat** is
    byte-identical to the left sibling's.
[ ] No SUBDIVISIONS promotion is recommended — the cuneus is a
    single gyral fold, and the V-area decomposition already
    lives in ``..cortex``.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (GYRUS_NAME, LOBE, ALTERNATE_NAMES, BOUNDING_SULCI,
    FUNCTIONAL_OVERLAYS, PRIMARY_OVERLAY, V1_BANK_SIDE,
    REPRESENTED_FIELD, parent-level placement, lingual gyrus
    caveat text) match the left sibling; VISUAL_HEMIFIELD,
    RIGHT_LATERALIZED_FUNCTIONS, LEFT_ONLY_DOMAINS, and
    CLINICAL_ANCHORS deliberately differ.
[ ] **The visual-hemifield asymmetry is verified**: the right
    cuneus carries "left_hemifield" (via "lower_contralateral"
    and "lower LEFT"), and the left cuneus carries
    "right_hemifield."
[ ] **The reading-vs-face downstream asymmetry is verified**:
    the right cuneus carries "left_hemifield_lower_field_
    face_input" and the left cuneus carries "right_hemifield_
    lower_field_reading_input" — the two are mirror-opposite.
[ ] **The right-specific clinical anchors are verified**:
    `right_cuneus_left_hemifield_face_processing_deficit`,
    `right_cuneus_motion_boundary_deficit_more_severe`, and
    `right_cuneus_left_hemifield_neglect_contribution` are
    present on the right and absent on the left. The left-only
    `left_cuneus_right_hemifield_reading_deficit` is absent on
    the right.
[ ] **The V1 / V2 mirror-flip is verified** — V1's upper field
    is on the lower bank (lingual gyrus), V2's upper field is
    on the upper bank (cuneus). **Byte-identical structural
    fact on both sides.**
[ ] Any downstream code querying "what does the right cuneus
    see?" must receive "the lower LEFT visual field" (via the
    V1 upper-bank representation) **and** the cuneus's V2 /
    V3d overlays carry the lower LEFT field as well.
[ ] Any downstream code querying "what is the cuneus?" must
    receive "the medial-surface wedge gyrus of the occipital
    lobe, whose lower margin is the upper bank of the
    calcarine sulcus (V1 dorsal representation) and whose more
    dorsal extent overlaps V2 and V3d."
[ ] Any downstream code querying "is the cuneus a child of
    ``..gyri``?" must receive "**no** — it is a direct child
    of ``..occipital``."
[ ] Any downstream code assigning the right face pathway must
    note that **the right cuneus's V1 upper-bank representation
    is part of the lower-left-field input** to the right V4v →
    LOC → right FFA pathway.
[ ] Any downstream code assigning the left reading pathway must
    note that **the left cuneus's V1 upper-bank representation
    is part of the lower-right-field input** to the left V4v →
    LOC → left VWFA pathway (documented in the left sibling).
[ ] Any downstream code assigning left hemispatial neglect must
    note that **the right cuneus's V3d territory is a
    contributor** via the right V3d → MT/V5 → right IPS dorsal
    attention pathway.
[ ] Any downstream code assigning **motion-boundary or
    depth-from-motion processing** must weight the **right
    cuneus's V3d territory more heavily** than the left's —
    the right V3d is the dominant motion substrate.
"""