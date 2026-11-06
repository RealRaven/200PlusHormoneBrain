"""
Precentral Sulcus (PreCS) — Left Hemisphere
============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── frontal
                              └── sulci
                                    └── precentral_sulcus   ← THIS PACKAGE

This is a **leaf sulcus** package on the **lateral convexity** of the
frontal lobe. Unlike the simple two-sided sulci (inferior frontal,
superior frontal) or the compound orbital sulcus, the precentral sulcus
is a **segmented sulcal complex** — typically divided into a **superior
precentral sulcus (SP)** and an **inferior precentral sulcus (IP)**,
with additional medial and paramedian components. It is the **posterior
boundary of the frontal lobe proper**, separating the frontal gyri from
the precentral gyrus (primary motor cortex, BA 4).

Parent: ``..sulci`` — sibling to ``inferior_frontal_sulcus``,
``olfactory_sulcus``, ``orbital_sulcus``, ``paracentral_sulcus``, and
``superior_frontal_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/frontal/sulci/precentral_sulcus``. Structural fields
(SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
are identical by contract; geometric and clinical fields (VARIANTS,
CLINICAL_ANCHORS, CONNECTIVITY) diverge by design.

--------------------------------------------------------------------------------
WHAT THE PreCS IS
--------------------------------------------------------------------------------

The precentral sulcus is the **anterior boundary of the precentral
gyrus** — the fold of cortex that houses the primary motor cortex
(BA 4) and that immediately precedes the central sulcus. It is the
surface groove that separates the **frontal gyri** (inferior, middle,
and superior) from the **precentral gyrus**.

The precentral sulcus is not a single continuous groove. In the majority
of brains it is a **segmented complex** with two principal parts[reference:0]:

    superior precentral sulcus (SP)
        The dorsal segment, caudal to the superior frontal sulcus
        (SFS). The SP is usually a single connected structure,
        consisting of two separate folds in only ~24 % of cases
        [reference:1]. Its **ventral limb (SPSv)** is the surface
        landmark for the **frontal eye fields (FEF)**[reference:2].

    inferior precentral sulcus (IP)
        The ventral segment, caudal to the inferior frontal sulcus
        (IFS). The IP separates the **ventral orofacial part of the
        precentral gyrus** from the **pars opercularis of the
        inferior frontal gyrus**[reference:3]. It is composed of a
        dorsal branch, a ventral branch, and a short horizontal
        extension[reference:4].

In addition to the SP and IP, **two or three small sulci** can be
identified between the SP and the midline: the **medial precentral
sulcus**, the **marginal precentral sulcus**, and a **paramidline
sulcus**[reference:5].

The precentral sulcus is the surface landmark for several critical
functional zones:

  * **Frontal eye fields (FEF)** — located in the **ventral limb of the
    superior precentral sulcus (SPSv)** in humans, in more than 90 % of
    individuals the SP connects with the superior frontal sulcus
    [reference:6][reference:7].

  * **Hand knob / omega sign** — the **precentral knob** corresponding
    to the hand area of the primary motor cortex is located just
    posterior to the junction of the superior frontal sulcus with the
    precentral sulcus, approximately **23 mm from the midline** and
    **19 mm from the lateral surface**[reference:8]. The knob is shaped
    like an **omega or epsilon in axial section** and like a **hook in
    sagittal section**[reference:9].

  * **Brodmann area 6 (premotor cortex)** — the anterior limit of BA 6
    is at an **individually variable distance anterior to the precentral
    sulcus** and does not correspond to a specific anatomical landmark
    [reference:10]. The border between premotor areas 6v1 and 6v2 is
    not marked by any sulcus and varies across hemispheres
    [reference:11].

The precentral sulcus is the **surgical landmark par excellence** for
the primary motor cortex: in tumor resection, epilepsy surgery, and
perirolandic arteriovenous malformation work, confusing the precentral
sulcus with the central sulcus is a recognized hazard[reference:12].

**Left-hemisphere specificity**: the left precentral sulcus is the
surface landmark for the **left primary motor cortex** representing the
**right hand and right lower limb**, and for the **left FEF** driving
**rightward saccades** and reading-related saccades. The left IP is the
posterior boundary of **Broca's area** (pars opercularis, BA 44), and
its discontinuity (present in ~4 % of hemispheres) has consequences for
quantitative measurement of pars opercularis volume[reference:13].

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction   Gyrus(es) bounded
    ---------   --------------------------------------------------------
    rostral     middle_frontal_gyrus   (dorsal portion of the SP)
                superior_frontal_gyrus (most-dorsal portion of the SP,
                                        where it turns medially)
                inferior_frontal_gyrus  (ventral portion of the IP, via
                                        pars opercularis, BA 44)
    caudal      precentral_gyrus   (BA 4, primary motor cortex; this is
                                    the "precentral" gyrus, the most-
                                    posterior frontal-lobe fold)

The precentral sulcus is a **multi-gyrus boundary** on its rostral side —
it separates **three different frontal gyri** (IFG, MFG, SFG) from the
**precentral gyrus** along its dorsoventral extent. This is more complex
than the simple IFG↔MFG boundary of the inferior frontal sulcus or the
MFG↔SFG boundary of the superior frontal sulcus, and it is why the
precentral sulcus must be treated as a **segmented complex** rather than
as a single groove.

**Both ``superior_frontal_gyrus`` and ``middle_frontal_gyrus`` already
exist as packages under ``..gyri``** and declare the precentral sulcus
as their **caudal boundary**. The ``inferior_frontal_gyrus`` package
declares the **olfactory sulcus** as a boundary but should also declare
the **inferior precentral sulcus** as its **caudal boundary** (via pars
opercularis) — this cross-reference is currently missing and must be
added.

**The precentral gyrus is NOT yet a package** under ``..gyri``. It is
the anatomical substrate of BA 4, and when it becomes a package it must
declare the precentral sulcus as its **rostral boundary**.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side      Brodmann areas abutting the sulcus
    ------    --------------------------------------------------------
    rostral   BA 6, BA 8, BA 9, BA 44, BA 46
    caudal    BA 4

Interpretation:

    rostral (frontal gyri side)
        BA 6   premotor cortex — action preparation, motor-sequence
               learning, and the SMA/pre-SMA on the medial surface.
               The anterior limit of BA 6 is **variable** and does not
               correspond to a fixed sulcal landmark[reference:14].
        BA 8   frontal eye fields (FEF) — located in the ventral limb
               of the superior precentral sulcus (SPSv) in humans
               [reference:15][reference:16].
        BA 9   dorsal prefrontal cortex — task-set maintenance and
               rule representation (dorsal MFG).
        BA 44  pars opercularis of the IFG — Broca's area component
               for speech-motor output (ventral IP, left hemisphere)
               [reference:17].
        BA 46  mid-DLPFC — working-memory register (mid-MFG).

    caudal (precentral gyrus side)
        BA 4   primary motor cortex — the **precentral gyrus** proper,
               housing the hand knob (omega sign) and the motor
               representation of the contralateral limbs and face.

The precentral sulcus therefore separates the **premotor / prefrontal /
language** cortex (BA 6, 8, 9, 44, 46) from the **primary motor
cortex** (BA 4). It is the surface landmark for the transition from
**action planning and cognitive control** to **motor execution**.

**A caution about BA 6 boundaries.** Unlike the crisp BA 4 boundary
(which is marked by the central sulcus), the **anterior limit of BA 6**
is **not a sulcal landmark** — it is at an individually variable
distance anterior to the precentral sulcus[reference:18]. The border
between premotor areas 6v1 and 6v2 is **not marked by any sulcus** and
varies across hemispheres[reference:19]. The ``BRODMANN_ADJACENCY`` dict
must therefore be read as "which areas may abut the sulcus somewhere
along its length," not as a precise one-to-one mapping for BA 6.

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    dorsal end (superior precentral sulcus, SP)
        Reaches the **superior hemispheric border** in ~12 % of
        brains, **reaches but does not cut** the border in ~14 %,
        and **fails to reach** the border in ~74 %[reference:20].
        When it reaches the border, it may continue onto the medial
        surface as the **paracentral sulcus**.

    ventral end (inferior precentral sulcus, IP)
        Approaches the **lateral (Sylvian) fissure**, separating the
        pars opercularis (BA 44) from the ventral precentral gyrus.
        The IP is the **posterior boundary of Broca's area** and is
        used as the landmark for quantitative measurement of pars
        opercularis volume[reference:21].

    rostral connections
        The **inferior frontal sulcus (IFS)** intersects the IP in
        roughly **70 % of specimens**[reference:22].
        The **superior frontal sulcus (SFS)** intersects the SP in
        roughly **80 % of specimens**[reference:23].
        In **more than 90 % of individuals** the SP connects with the
        SFS[reference:24].

    medial components
        Between the SP and the midline, **two or three small sulci**
        can be identified: the **medial precentral sulcus**, the
        **marginal precentral sulcus**, and a **paramidline
        sulcus**[reference:25].

The precentral sulcus is therefore a **segmented sulcal complex** with
a **dorsal segment (SP)** that usually does not reach the midline, a
**ventral segment (IP)** that approaches the Sylvian fissure, and
**medial components** that fill the space between the SP and the
midline.

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

The precentral sulcus is the **most morphologically complex sulcus in
the frontal lobe**. Unlike the IFS or the olfactory sulcus, whose
variants are deviations from a canonical form, the PreCS has **multiple
canonical configurations** (two-part, three-part, continuous) and
**multiple inferior precentral sulcus morphological patterns** (arcuate,
ramified, bayonet, Y-form, tiny form).

    two_part_configuration        most common
        The precentral sulcus is divided into a **superior precentral
        sulcus (SP)** and an **inferior precentral sulcus (IP)**.
        This is the **majority configuration** in humans[reference:26].

    three_part_configuration      ~17 %
        The precentral sulcus is divided into **three parts**:
        precentral inferior, precentral medius, and precentral
        superior. The **precentral medius** is most frequently derived
        from the upper part of the IP or the posterior part of the
        horizontal ramus[reference:27][reference:28].

    continuous_single_sulcus      minority
        The precentral sulcus may form **one continuous sulcus**
        without segmentation[reference:29]. In about **17 % of brains**
        the precentral sulcus does not show discontinuity into
        separate parts[reference:30].

    superior_precentral_sulcus_connects_with_SFS  >90 %
        In more than 90 % of individuals the **SP connects with the
        superior frontal sulcus (SFS)**[reference:31].

    IP_single_segment              96 %
        The inferior precentral sulcus is a **single segment** in
        96 % of hemispheres (left: 96 %, right: 96 %)[reference:32].

    IP_bifid                       4 %
        The inferior precentral sulcus is **bifid** in 4 % of
        hemispheres (left: 4 %, right: 4 %)[reference:33].

    IP_no_connection_with_SFS      81 %
        The inferior precentral sulcus has **no connection with the
        superior frontal sulcus** in 81 % of hemispheres (left: 84 %,
        right: 78 %)[reference:34].

    IP_morphological_patterns      sex-dependent frequencies
        Five morphological patterns are described for the inferior
        precentral sulcus:

            arcuate form    left male 17, left female 16
                            right male 16, right female 9
            ramified form   left male 7, left female 4
                            right male 7, right female 3
            bayonet form    left male 24, left female 13
                            right male 19, right female 19
            Y form          left male 2, left female 2
                            right male 2, right female 1
            tiny form       left male 5, left female 0
                            right male 3, right female 3

    left_right_asymmetry           marked individual differences
        The precentral sulcus pattern differs **between hemispheres**
        within the same brain as well as between individuals. The
        left and right PreCS are not mirror images; pattern type and
        segment counts can differ across hemispheres. This is why the
        left and right PreCS packages each carry their own VARIANTS
        list rather than sharing one.

These variants are **geometric and topological**, not merely metric.
Unlike the depth variants of the olfactory sulcus, the PreCS variants
change the **number and connectivity of the grooves** — a two-part
sulcus has one topology, a three-part sulcus has another, and a
continuous sulcus has a third. The ``BOUNDING_GYRI`` and
``BRODMANN_ADJACENCY`` fields must therefore be read as the
**canonical** boundary set, with the understanding that in atypical
patterns one or more boundaries may be absent or fused.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    precentral_knob_hand_localization
        **This is the left-PreCS anchor par excellence.** The
        **precentral knob** (omega sign) corresponding to the hand
        area of the primary motor cortex is located just posterior
        to the junction of the superior frontal sulcus with the
        precentral sulcus, approximately **23 mm from the midline**
        and **19 mm from the lateral surface**[reference:36].
        The knob is shaped like an **omega or epsilon in axial
        section** and like a **hook in sagittal section**
        [reference:37]. Identifying the omega sulcus is important
        because it is a **reliable landmark demarcating eloquent
        motor cortex**, critically important in planning surgical
        removal of brain tumors[reference:38].

    broca_operculum_posterior_boundary
        The **left inferior precentral sulcus** is the posterior
        boundary of **Broca's area** (pars opercularis, BA 44).
        Discontinuity of the IP (present in ~4 % of hemispheres)
        has been argued to make it an unreliable landmark for
        quantitative measurement of pars opercularis, with the
        anterior subcentral sulcus used instead in some studies
        [reference:39]. Other studies have demonstrated the reliability
        of the IP as the posterior boundary[reference:40].

    frontal_eye_fields_spsv
        The **left FEF** is located in the **ventral limb of the
        superior precentral sulcus (SPSv)**, driving **rightward
        saccades** and reading-related saccades[reference:41].
        The FEF is a core node of the dorsal attention network
        and the oculomotor control system.

    surgical_corridor_for_precentral_lesions
        The precentral sulcus is a **surgical corridor** for
        reaching precentral gyrus lesions (tumors, cavernomas,
        focal cortical dysplasia) while preserving the primary
        motor cortex. Confusing the precentral sulcus with the
        central sulcus is a recognized hazard in tumor resection,
        epilepsy surgery, and perirolandic AVM work[reference:42].
        Staged multimodal intraoperative neurophysiology can guide
        resection of epileptogenic lesions within the precentral
        gyrus[reference:43].

    epilepsy_surgery_landmark
        In **frontal lobe decortication** for epilepsy, the
        precentral sulcus is the landmark for the posterior limit
        of the paramedian subpial resection — **3 cm ahead of the
        precentral sulcus** — to reach the genu of the corpus
        callosum. This preserves the motor cortex while
        achieving adequate disconnection.

    tumor_resection_eloquent_cortex
        In **tumor resection**, the precentral sulcus and the
        omega sign are the surface landmarks for the **eloquent
        motor cortex**[reference:45]. The precentral gyrus is roughly
        **50 % thicker in width** than the postcentral gyrus, and
        the "bracket" sign on sagittal MRI can help localize the
        postcentral gyrus, but axial localization using the
        precentral knob has the **highest inter-rater consistency**
        [reference:46].

    central_sulcus_confusion_hazard
        **Confusing the precentral sulcus with the central sulcus
        is a recognized surgical hazard** in tumor resection,
        epilepsy surgery, and perirolandic AVM work[reference:47].
        The precentral sulcus is frequently bisected into the IP
        and SP[reference:48], while the central sulcus does not
        connect to any other sulcus and is easily identifiable
        [reference:49]. The precentral sulcus can be visualized on
        MRI by observing its connection with the SFS on high axial
        images and the IFS on lateral sagittal images
        [reference:50].

These anchors are **left-hemisphere-specific** in two senses: (a) the
left IP is the posterior boundary of **Broca's area**, a left-dominant
language structure; (b) the left FEF drives **rightward** saccades and
reading-related saccades. The right sibling's docstring carries the
right hand/leg representation and the right FEF's **leftward** saccade
and ventral-attention emphasis.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus complex)
--------------------------------------------------------------------------------

    corticospinal_tract (via precentral gyrus, BA 4)
        → descends_through_posterior_limb_of_internal_capsule
        → cerebral_peduncle
        → spinal_cord (contralateral, right hand / right leg motor
          neurons)
        The corticospinal fibres originate in the precentral gyrus
        **caudal to the precentral sulcus** and descend through the
        posterior limb of the internal capsule. The precentral
        sulcus is the surface landmark for the **origin** of this
        tract, not for the tract itself.

    frontal_aslant_tract (left)
        → traverses_beneath_caudal_left_PreCS
        → left_pre_supplementary_motor_area
        → left_pars_opercularis_of_ifg
        The frontal aslant tract crosses beneath the caudal left
        precentral sulcus, connecting the pre-SMA to the pars
        opercularis. This is the speech-initiation corridor, and
        its interruption produces **apraxia of speech**.

    arcuate_fasciculus (left)
        → caps_left_operculum
        → left_posterior_superior_temporal_gyrus
        The left arcuate fasciculus caps the left operculum
        beneath the inferior precentral sulcus, forming the dorsal
        language pathway.

    superior_longitudinal_fasciculus (SLF)
        → traverses_beneath_superior_precentral_sulcus
        → left_superior_parietal_lobule
        → left_intraparietal_sulcus
        The SLF components run beneath the SP, connecting the
        premotor / prefrontal cortex to the parietal cortex. The
        SLF II component supports the **dorsal attention network**
        and the **FEF ↔ IPS circuit**.

    uncinate_fasciculus (left)
        → traverses_beneath_ventral_left_PreCS
        → left_anterior_temporal_lobe
        The uncinate's frontal segment passes beneath the ventral
        precentral sulcus (near the pars opercularis / pars
        triangularis junction), connecting the ventral language
        network to the anterior temporal lobe.

    extreme_capsule (left)
        → traverses_beneath_left_PreCS
        → left_insula (anterior)
        The extreme capsule runs from the opercular cortex across
        the insula; its frontal origin lies beneath the precentral
        sulcus.

    short-range U-fibres
        → connects_precentral_gyrus_to_caudal_frontal_gyri
        Short U-fibres cross beneath the precentral sulcus,
        coupling the premotor cortex (BA 6) to the primary motor
        cortex (BA 4). These fibres support the **premotor →
        M1** interaction for action preparation and execution.

Note the **presence of multiple large association bundles** beneath
the precentral sulcus (aslant tract, arcuate, SLF, uncinate, extreme
capsule) — this is a **corridor-rich** sulcus, unlike the orbital and
olfactory sulci whose white-matter relationships are distributed. The
precentral sulcus is the surface landmark for the **convergence of the
language, attention, and motor systems** on the posterior frontal
convexity.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri.superior_frontal_gyrus
    The dorsal bounding gyrus. The SFG package already declares the
    precentral sulcus as its **caudal boundary**. The duality
    contract holds for this link.

..gyri.middle_frontal_gyrus
    The intermediate bounding gyrus. The MFG package already declares
    the precentral sulcus as its **caudal boundary**. The duality
    contract holds for this link.

..gyri.inferior_frontal_gyrus
    The ventral bounding gyrus (via pars opercularis, BA 44). The
    IFG package declares the **olfactory sulcus** as a boundary but
    **should also declare the inferior precentral sulcus** as its
    **caudal boundary**. This cross-reference is currently missing
    and must be added when the IFG package is updated.

..gyri  (FORWARD REFERENCE)
    The **precentral gyrus** (BA 4) is **not yet a package** under
    ``..gyri``. When it is created, it must declare the precentral
    sulcus as its **rostral boundary**. See the FORWARD-DECLARATION
    CAVEAT below.

..sulci.paracentral_sulcus
    The precentral sulcus is the **lateral continuation** of the
    paracentral sulcus. The two sulci are continuous over the dorsal
    edge of the hemisphere: the precentral sulcus turns medially and
    becomes the paracentral sulcus. Both packages must declare this
    continuity.

..sulci.inferior_frontal_sulcus
    The IFS intersects the **inferior precentral sulcus** in roughly
    **70 % of specimens**[reference:51]. The two sulci share a
    T-junction at the ventral frontal convexity.

..sulci.superior_frontal_sulcus
    The SFS intersects the **superior precentral sulcus** in roughly
    **80 % of specimens**[reference:52], and the SP connects with the
    SFS in **more than 90 % of individuals**[reference:53]. The two
    sulci share a T-junction at the dorsal frontal convexity.

..brodmann_areas.brodmann_area_4
..brodmann_areas.brodmann_area_6
..brodmann_areas.brodmann_area_8
..brodmann_areas.brodmann_area_9
..brodmann_areas.brodmann_area_44
..brodmann_areas.brodmann_area_46
    The six BAs abutting the PreCS. Each must declare the PreCS as a
    boundary once the BA packages exist.

..cortex.premotor_cortex
    The rostral bank of the precentral sulcus is the **premotor
    cortex (BA 6)**. The premotor_cortex package must declare the
    precentral sulcus as its **caudal boundary**, noting that the
    anterior limit of BA 6 is **variable and not sulcus-defined**
    [reference:54].

..cortex.primary_motor_cortex
    The caudal bank of the precentral sulcus is the **primary motor
    cortex (BA 4)** — the precentral gyrus. The
    primary_motor_cortex package must declare the precentral sulcus
    as its **rostral boundary**, and must note the **hand knob /
    omega sign** as the surface landmark for the hand area[reference:55].

..cortex.supplementary_motor_cortex
    The medial continuation of the precentral sulcus is the
    paracentral sulcus, which borders the SMA/pre-SMA. The
    supplementary_motor_cortex package must declare this
    continuity.

../../subcortical/basal_ganglia/striatum/dorsal_striatum
    The corticostriatal projections from the premotor and prefrontal
    cortex pass beneath the precentral sulcus en route to the
    caudate and putamen. The striatum package must declare the
    PreCS as a landmark for the **corticostriatal corridor**.

../../subcortical/medial_temporal_lobe/amygdala  — indirect
    No direct amygdala projection originates in the precentral
    sulcus. Recorded here only to pre-empt a false cross-reference.

../../right/cortex/frontal/sulci/precentral_sulcus
    The right-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
    MUST be byte-identical to this package. Geometric and clinical
    fields (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED
    to differ — the left IP is the posterior boundary of Broca's
    area; the left FEF drives rightward saccades; the left hand
    knob represents the right hand.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "precentral_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to right
                              "rostral": {
                                  "superior_precentral_sulcus": (
                                      "superior_frontal_gyrus",
                                      "middle_frontal_gyrus",
                                  ),
                                  "inferior_precentral_sulcus": (
                                      "middle_frontal_gyrus",
                                      "inferior_frontal_gyrus",
                                  ),
                              },
                              "caudal":  ("precentral_gyrus",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "rostral": (6, 8, 9, 44, 46),
                              "caudal":  (4,),
                          }

    EXTENT              = {
                              "superior_precentral_sulcus": {
                                  "dorsal":  ("superior_hemispheric_"
                                              "border",
                                              "paracentral_sulcus"),
                                  "ventral": ("superior_frontal_sulcus",),
                              },
                              "inferior_precentral_sulcus": {
                                  "dorsal":  ("inferior_frontal_sulcus",),
                                  "ventral": ("lateral_sylvian_fissure",
                                              "pars_opercularis"),
                              },
                          }

    VARIANTS            = (                          # DIFFERS from right
                              "two_part_configuration_most_common",
                              "three_part_configuration_~17%",
                              "continuous_single_sulcus_minority",
                              "superior_precentral_sulcus_connects_"
                              "with_SFS_>90%",
                              "IP_single_segment_96%",
                              "IP_bifid_4%",
                              "IP_no_connection_with_SFS_81%",
                              "IP_morphological_patterns_arcuate_"
                              "ramified_bayonet_Y_tiny",
                              "left_right_asymmetry_pattern_type_"
                              "may_differ_across_hemispheres",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "precentral_knob_hand_localization",
                              "broca_operculum_posterior_boundary",
                              "frontal_eye_fields_spsv",
                              "surgical_corridor_for_precentral_"
                              "lesions",
                              "epilepsy_surgery_landmark",
                              "tumor_resection_eloquent_cortex",
                              "central_sulcus_confusion_hazard",
                          )

    CONNECTIVITY        = { ... }   # as specified above

    SUBDIVISIONS        = ()        # no nested packages

    __all__ = [
        "SULCUS_NAME",
        "HEMISPHERE",
        "LOBE",
        "BOUNDING_GYRI",
        "BRODMANN_ADJACENCY",
        "EXTENT",
        "VARIANTS",
        "CLINICAL_ANCHORS",
        "CONNECTIVITY",
        "SUBDIVISIONS",
    ]

Note: ``SUBDIVISIONS`` is an empty tuple — the PreCS is a leaf sulcus.
The superior and inferior precentral sulci are **not** sub-packages;
they are captured inside ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and
``EXTENT`` as per-component keys. If a future parcellation promotes
them to sub-packages, see the PROMOTION RULE below.

No behaviour. This package is a declarative descriptor; all computation
that references the PreCS lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT (unique to this sulcus)
--------------------------------------------------------------------------------

The parent ``..sulci`` duality contract states: *every gyrus named in
any BOUNDING_GYRI MUST exist in ``..gyri.GYRI``.* **The precentral
sulcus is the sulcus for which this holds partially.**

Of the four gyrus names in this package's BOUNDING_GYRI:

    superior_frontal_gyrus    → resolves today (the SFG package exists
                                and declares the PreCS as its caudal
                                boundary)
    middle_frontal_gyrus      → resolves today (the MFG package exists
                                and declares the PreCS as its caudal
                                boundary)
    inferior_frontal_gyrus    → **partially resolves** — the IFG
                                package exists but does **not yet
                                declare the inferior precentral
                                sulcus** as its caudal boundary. This
                                cross-reference must be added.
    precentral_gyrus          → forward reference

**The precentral gyrus is the forward reference**, and it is the
anatomical substrate of BA 4 — the primary motor cortex. The PCL
package should be built out **before** the right-hemisphere precentral
sulcus is written, so that the right side can be authored without the
same unresolved-reference burden. If the right side is written first,
it must carry the identical caveat text — the two hemispheres must not
diverge in their handling of unresolved references.

**The IFG cross-reference is a separate issue**: the IFG package must
be updated to declare the **inferior precentral sulcus** as its
**caudal boundary** (via pars opercularis, BA 44). This is a
one-line addition to the IFG package's boundary cross-references and
should be made in both hemispheres in the same commit.

--------------------------------------------------------------------------------
PROMOTION RULE (when a sulcus component becomes a package)
--------------------------------------------------------------------------------

A sulcus is an **edge**, not a **node**, so the standard promotion rule
does not directly apply. For the precentral sulcus, the most natural
promotion is to split the **two principal components** into
sub-packages:

    precentral_sulcus/
        __init__.py
        superior_precentral_sulcus/
            __init__.py
        inferior_precentral_sulcus/
            __init__.py

Then:

  1. Add the two component names to ``SUBDIVISIONS``.
  2. Keep ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and ``EXTENT`` at
     the parent level as the **union** of the components.
  3. Each component package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**Duality caveat**: the frontal gyri and the precentral gyrus declare
the precentral sulcus *as a whole* as their boundary. A component
split does not break the duality contract as long as the parent
remains the canonical answer to "what does the precentral sulcus
bound?" and the components refine *which part* bounds what.

**No split should be performed while the FORWARD-DECLARATION CAVEAT is
in force.** Splitting a sulcus whose precentral gyrus does not yet
exist as a package multiplies unresolved references and makes the
eventual duality reconciliation harder.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../precentral_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME          "precentral_sulcus"
        LOBE                 "frontal"
        BOUNDING_GYRI        the same multi-gyrus boundary set, with
                             the same per-component mapping
        BRODMANN_ADJACENCY   the same BA 6/8/9/44/46 ↔ BA 4 adjacency
        EXTENT               the same superior-border / Sylvian-fissure
                             landmarks
        SUBDIVISIONS         both empty (or both non-empty in the same
                             way, if a component split is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "left" vs "right"
        VARIANTS             same two-part / three-part / continuous
                             taxonomy and same IP morphological
                             patterns; frequencies may differ; left-
                             right asymmetry is itself a variant entry
                             on both sides
        CLINICAL_ANCHORS     left: Broca's-area posterior boundary,
                             left FEF driving rightward saccades,
                             left hand knob representing the right
                             hand; right: prosody-network corridor,
                             right FEF driving leftward saccades and
                             reorienting to salience, right hand knob
                             representing the left hand
        CONNECTIVITY         same bundle names; left aslant tract
                             carries speech-initiation content; left
                             arcuate carries sound-to-articulation
                             mapping

**The segmentation taxonomy is hemisphere-invariant** — two-part,
three-part, and continuous configurations mean the same thing on both
sides. What may differ is the **frequency** of each configuration and
the **functional correlate** of a given segment (Broca's area on the
left, prosody network on the right), and those differences belong in
VARIANTS and CLINICAL_ANCHORS, not in the structural contract.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "precentral_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BOUNDING_GYRI is **compound** — a per-component dict with keys
    "superior_precentral_sulcus" and "inferior_precentral_sulcus",
    not a simple direction→gyrus mapping.
[ ] BOUNDING_GYRI names superior_frontal_gyrus,
    middle_frontal_gyrus, and inferior_frontal_gyrus on the rostral
    side, and precentral_gyrus on the caudal side.
[ ] BRODMANN_ADJACENCY is compound, per-component, and set-valued:
    rostral (6, 8, 9, 44, 46), caudal (4,).
[ ] The BA 6 boundary caution is documented: the anterior limit of
    BA 6 is **variable and not sulcus-defined**[reference:56].
[ ] EXTENT records the superior-border reach of the SP (~12 % cut,
    ~14 % reach, ~74 % fail) and the Sylvian-fissure approach of
    the IP.
[ ] SUBDIVISIONS is empty and byte-identical to the right sibling.
[ ] VARIANTS documents the two-part (most common), three-part
    (~17 %), and continuous (minority) configurations, and the five
    IP morphological patterns (arcuate, ramified, bayonet, Y, tiny)
    with sex-stratified frequencies.
[ ] VARIANTS documents the **IP single-segment rate (96 %)**,
    **IP bifid rate (4 %)**, and **IP-SFS no-connection rate (81 %)**
    [reference:58].
[ ] CLINICAL_ANCHORS contains the seven left-specific anchors:
    precentral_knob_hand_localization, broca_operculum_posterior_
    boundary, frontal_eye_fields_spsv, surgical_corridor_for_
    precentral_lesions, epilepsy_surgery_landmark, tumor_resection_
    eloquent_cortex, central_sulcus_confusion_hazard.
[ ] CONNECTIVITY contains the seven entries (corticospinal, frontal
    aslant, arcuate, SLF, uncinate, extreme capsule, short U-fibres),
    with left-side speech and language emphasis.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.superior_frontal_gyrus`` and
    ``..gyri.middle_frontal_gyrus`` both declare the PreCS as their
    caudal boundary — the duality contract holds for these links.
[ ] The IFG package is flagged for the **missing** inferior
    precentral sulcus cross-reference — it must be added in both
    hemispheres in the same commit.
[ ] The FORWARD-DECLARATION CAVEAT is present and specifies that
    **precentral_gyrus** is the unresolvable gyrus name.
[ ] The recommendation to build out the precentral gyrus package
    before the right-hemisphere PreCS is recorded.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (compound BOUNDING_GYRI, compound BRODMANN_ADJACENCY, EXTENT,
    SUBDIVISIONS) match the right sibling; VARIANTS frequencies,
    CLINICAL_ANCHORS emphasis, and CONNECTIVITY content deliberately
    differ.
"""