"""
Precentral Sulcus (PreCS) — Right Hemisphere
=============================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
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
``../../left/cortex/frontal/sulci/precentral_sulcus``. Structural fields
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
of brains it is a **segmented complex** with two principal parts:

    superior precentral sulcus (SP)
        The dorsal segment, caudal to the superior frontal sulcus
        (SFS). The SP is usually a single connected structure,
        consisting of two separate folds in only ~24 % of cases.
        Its **ventral limb (SPSv)** is the surface landmark for the
        **frontal eye fields (FEF)**.

    inferior precentral sulcus (IP)
        The ventral segment, caudal to the inferior frontal sulcus
        (IFS). The IP separates the **ventral orofacial part of the
        precentral gyrus** from the **pars opercularis of the
        inferior frontal gyrus**. It is composed of a dorsal branch,
        a ventral branch, and a short horizontal extension. **On the
        right, the IP is the surface landmark for the prosody and
        response-inhibition operculum** (see below).

In addition to the SP and IP, **two or three small sulci** can be
identified between the SP and the midline: the **medial precentral
sulcus**, the **marginal precentral sulcus**, and a **paramidline
sulcus**.

The precentral sulcus is the surface landmark for several critical
functional zones:

  * **Frontal eye fields (FEF)** — located in the **ventral limb of the
    superior precentral sulcus (SPSv)** in humans, in more than 90 % of
    individuals the SP connects with the superior frontal sulcus.
    **On the right, the FEF is the dominant node of the ventral
    attention network** — the stimulus-driven “circuit breaker” that
    reorients attention to salient events[reference:0].

  * **Hand knob / omega sign** — the **precentral knob** corresponding
    to the hand area of the primary motor cortex is located just
    posterior to the junction of the superior frontal sulcus with the
    precentral sulcus, approximately **23 mm from the midline** and
    **19 mm from the lateral surface**[reference:1]. The knob is shaped
    like an **omega or epsilon in axial section** and like a **hook in
    sagittal section**[reference:2]. **On the right, the knob
    represents the left hand**; the right M1 hand area is the
    contralateral substrate of left-hand skilled movement.

  * **Brodmann area 6 (premotor cortex)** — the anterior limit of BA 6
    is at an **individually variable distance anterior to the precentral
    sulcus** and does not correspond to a specific anatomical landmark.
    The border between premotor areas 6v1 and 6v2 is not marked by any
    sulcus and varies across hemispheres.

The precentral sulcus is the **surgical landmark par excellence** for
the primary motor cortex: in tumor resection, epilepsy surgery, and
perirolandic arteriovenous malformation work, confusing the precentral
sulcus with the central sulcus is a recognized hazard[reference:3].

**Right-hemisphere specificity**: the right precentral sulcus is the
surface landmark for the **right primary motor cortex** representing the
**left hand and left lower limb**, and for the **right FEF** driving
**leftward saccades** and **stimulus-driven reorienting**. The right IP
is the posterior boundary of the **right Broca homologue** — the
prosody-and-inhibition operculum, not the speech-production operculum.
The right FEF’s functional dominance for reorienting is a
**right-lateralized network property** that has no symmetric
counterpart on the left[reference:4].

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
                                    the “precentral” gyrus, the most-
                                    posterior frontal-lobe fold)

**This field is byte-identical to the left-hemisphere sibling.** The
topology of which gyrus lies on which side of which component is
hemisphere-invariant. The right precentral sulcus separates the same
three frontal gyri from the same precentral gyrus.

**Both ``superior_frontal_gyrus`` and ``middle_frontal_gyrus`` already
exist as packages under ``..gyri``** (on the right) and declare the
precentral sulcus as their **caudal boundary**. The ``inferior_frontal_gyrus``
package declares the **olfactory sulcus** as a boundary but should also
declare the **inferior precentral sulcus** as its **caudal boundary**
(via pars opercularis) — this cross-reference is currently missing on
both sides and must be added.

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

Interpretation (right-hemisphere functional annotations):

    rostral (frontal gyri side)
        BA 6   premotor cortex — spatial action preparation and
               motor-sequence learning. On the right, the SMA/pre-SMA
               contributes to **left-hand** motor planning and
               bimanual coordination support.
        BA 8   frontal eye fields (FEF) — located in the ventral limb
               of the superior precentral sulcus (SPSv). **On the
               right, the FEF is the dominant node of the ventral
               attention network**, driving reflexive saccades toward
               salient stimuli and reorienting after invalid cueing
               [reference:5].
        BA 9   dorsal prefrontal cortex — spatial task-set maintenance
               (dorsal MFG).
        BA 44  pars opercularis of the IFG — **prosodic-motor output
               and response inhibition** (ventral IP, right hemisphere)
               [reference:6].
        BA 46  mid-DLPFC — visuospatial working-memory register
               (mid-MFG).

    caudal (precentral gyrus side)
        BA 4   primary motor cortex — the **precentral gyrus** proper,
               housing the hand knob (omega sign) and the motor
               representation of the **contralateral (left)** limbs
               and face.

**This field is byte-identical to the left-hemisphere sibling.** The
Brodmann-area adjacency is numerically symmetric across hemispheres;
the functional annotations above differ (right BA 44 carries prosody /
inhibition rather than speech production; right BA 8 carries the
ventral-attention reorienting function) but the BA numbers do not.

**A caution about BA 6 boundaries.** Unlike the crisp BA 4 boundary
(which is marked by the central sulcus), the **anterior limit of BA 6**
is **not a sulcal landmark** — it is at an individually variable
distance anterior to the precentral sulcus. The border between premotor
areas 6v1 and 6v2 is **not marked by any sulcus** and varies across
hemispheres. The ``BRODMANN_ADJACENCY`` dict must therefore be read as
“which areas may abut the sulcus somewhere along its length,” not as a
precise one-to-one mapping for BA 6.

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    dorsal end (superior precentral sulcus, SP)
        Reaches the **superior hemispheric border** in ~12 % of
        brains, **reaches but does not cut** the border in ~14 %,
        and **fails to reach** the border in ~74 %.
        When it reaches the border, it may continue onto the medial
        surface as the **paracentral sulcus**.

    ventral end (inferior precentral sulcus, IP)
        Approaches the **lateral (Sylvian) fissure**, separating the
        pars opercularis (BA 44) from the ventral precentral gyrus.
        **On the right, the IP is the posterior boundary of the
        prosody-inhibition operculum**, and its ventral end is the
        surface landmark for the right frontal operculum.

    rostral connections
        The **inferior frontal sulcus (IFS)** intersects the IP in
        roughly **70 % of specimens**.
        The **superior frontal sulcus (SFS)** intersects the SP in
        roughly **80 % of specimens**.
        In **more than 90 % of individuals** the SP connects with the
        SFS.

    medial components
        Between the SP and the midline, **two or three small sulci**
        can be identified: the **medial precentral sulcus**, the
        **marginal precentral sulcus**, and a **paramidline
        sulcus**.

**This field is byte-identical to the left-hemisphere sibling.** The
dorsal reach of the SP and the ventral approach of the IP are
hemisphere-invariant.

The precentral sulcus is therefore a **segmented sulcal complex** with
a **dorsal segment (SP)** that usually does not reach the midline, a
**ventral segment (IP)** that approaches the Sylvian fissure, and
**medial components** that fill the space between the SP and the
midline.

--------------------------------------------------------------------------------
VARIANTS (right-hemisphere specific)
--------------------------------------------------------------------------------

The precentral sulcus is the **most morphologically complex sulcus in
the frontal lobe**. Unlike the IFS or the olfactory sulcus, whose
variants are deviations from a canonical form, the PreCS has **multiple
canonical configurations** (two-part, three-part, continuous) and
**multiple inferior precentral sulcus morphological patterns** (arcuate,
ramified, bayonet, Y-form, tiny form).

The **segmentation taxonomy is hemisphere-invariant**, but the
**frequencies** and **sex-stratified distributions** carry
right-specific values.

    two_part_configuration        most common
        The precentral sulcus is divided into a **superior precentral
        sulcus (SP)** and an **inferior precentral sulcus (IP)**.
        This is the **majority configuration** in humans on both
        sides.

    three_part_configuration      ~17 %
        The precentral sulcus is divided into **three parts**:
        precentral inferior, precentral medius, and precentral
        superior. The **precentral medius** is most frequently derived
        from the upper part of the IP or the posterior part of the
        horizontal ramus.

    continuous_single_sulcus      minority
        The precentral sulcus may form **one continuous sulcus**
        without segmentation. In about **17 % of brains** the
        precentral sulcus does not show discontinuity into separate
        parts.

    superior_precentral_sulcus_connects_with_SFS  >90 %
        In more than 90 % of individuals the **SP connects with the
        superior frontal sulcus (SFS)**.

    IP_single_segment             96 % (right)
        The right inferior precentral sulcus is a **single segment**
        in **96 %** of right hemispheres — identical to the left
        .

    IP_bifid                       4 % (right)
        The right inferior precentral sulcus is **bifid** in **4 %**
        of right hemispheres — identical to the left.

    IP_no_connection_with_SFS      78 % (right)
        The right inferior precentral sulcus has **no connection with
        the superior frontal sulcus** in **78 %** of right
        hemispheres (left: 84 %; total: 81 %). The right IP
        is therefore **slightly more likely to connect with the SFS**
        than the left IP (22 % vs 16 %).

    IP_morphological_patterns      sex-dependent frequencies (right)
        Five morphological patterns are described for the inferior
        precentral sulcus. Right-hemisphere frequencies (male /
        female):

            arcuate form     right male 16, right female 9
            ramified form    right male 7, right female 3
            bayonet form     right male 19, right female 19
            Y form           right male 2, right female 1
            tiny form        right male 3, right female 3

    left_right_asymmetry           marked individual differences
        The precentral sulcus pattern differs **between hemispheres**
        within the same brain as well as between individuals. The
        left and right PreCS are not mirror images; pattern type and
        segment counts can differ across hemispheres. **Importantly,
        the rightward functional asymmetries in the FEF / ventral
        attention network are NOT explained by differences in sulcal
        position or grey-matter density between hemispheres**
        [reference:12] — the functional laterality is a property of the
        network, not of the sulcal geometry.

These variants are **geometric and topological**, not merely metric.
Unlike the depth variants of the olfactory sulcus, the PreCS variants
change the **number and connectivity of the grooves** — a two-part
sulcus has one topology, a three-part sulcus has another, and a
continuous sulcus has a third. The ``BOUNDING_GYRI`` and
``BRODMANN_ADJACENCY`` fields must therefore be read as the
**canonical** boundary set, with the understanding that in atypical
patterns one or more boundaries may be absent or fused.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    left_hand_knob_localization
        **This is the right-PreCS anchor par excellence.** The
        **precentral knob** (omega sign) corresponding to the hand
        area of the **right** primary motor cortex represents the
        **left hand** and is located just posterior to the junction
        of the superior frontal sulcus with the precentral sulcus,
        approximately **23 mm from the midline** and **19 mm from the
        lateral surface**[reference:13]. The knob is shaped like an
        **omega or epsilon in axial section** and like a **hook in
        sagittal section**[reference:14]. Identifying the omega sulcus is
        a **reliable landmark demarcating eloquent motor cortex**,
        critically important in planning surgical removal of right
        frontal tumours and in resecting right perirolandic
        lesions while preserving left-hand function.

    right_fef_ventral_attention_reorienting
        **This is the right-only functional anchor.** The right FEF,
        in the ventral limb of the right superior precentral sulcus
        (SPSv), is the **dominant node of the right-lateralized
        ventral attention network** — the stimulus-driven “circuit
        breaker” that reorients attention to salient events and
        maintains arousal for target detection[reference:15]. Right FEF
        damage contributes to **left hemispatial neglect**, and the
        right FEF is the cortical target of choice for
        attention-modulating interventions. This function has no
        symmetric left-hemisphere counterpart of comparable
        dominance[reference:16].

    right_broca_homologue_prosody_and_inhibition
        The **right inferior precentral sulcus** is the posterior
        boundary of the **right Broca homologue** — the
        prosody-and-inhibition operculum. The right IP is engaged
        during **sentence-level linguistic prosody** processing and
        during **effortful top-down prosodic analysis** when normal
        linguistic cues are degraded[reference:17]. The right IP is also
        part of the **response-inhibition network** (stop-signal and
        go/no-go tasks under high conflict). Its clinical signature is
        **affective aprosodia and disinhibition**, not speech
        production failure.

    surgical_corridor_for_right_precentral_lesions
        The right precentral sulcus is a **surgical corridor** for
        reaching right precentral gyrus lesions (tumours, cavernomas,
        focal cortical dysplasia) while preserving the **left-hand**
        primary motor cortex[reference:18]. Confusing the precentral
        sulcus with the central sulcus is a recognized hazard in
        tumour resection, epilepsy surgery, and perirolandic AVM work.

    epilepsy_surgery_landmark
        In **frontal lobe decortication** for epilepsy, the precentral
        sulcus is the landmark for the posterior limit of the
        paramedian subpial resection — **3 cm ahead of the precentral
        sulcus** — to reach the genu of the corpus callosum. This
        preserves the motor cortex while achieving adequate
        disconnection. On the right, the resection must also preserve
        the prosody-inhibition operculum.

    tumour_resection_left_hand_eloquent_cortex
        In **tumour resection**, the right precentral sulcus and the
        omega sign are the surface landmarks for the **eloquent motor
        cortex representing the left hand**. The precentral gyrus is
        roughly **50 % thicker in width** than the postcentral gyrus,
        and axial localization using the precentral knob has the
        **highest inter-rater consistency**[reference:19].

    central_sulcus_confusion_hazard
        **Confusing the precentral sulcus with the central sulcus is a
        recognized surgical hazard** in tumour resection, epilepsy
        surgery, and perirolandic AVM work. The precentral sulcus is
        frequently bisected into the IP and SP, while the central
        sulcus does not connect to any other sulcus and is easily
        identifiable. The precentral sulcus can be visualized on MRI
        by observing its connection with the SFS on high axial images
        and the IFS on lateral sagittal images[reference:20].

These anchors are **right-hemisphere-specific** in two senses: (a) the
right FEF’s dominance for **reorienting to salience** is a
right-lateralized network property, not a general FEF property; (b) the
right IP is the posterior boundary of the **prosody-inhibition
operculum**, not Broca’s speech-production area. The left sibling’s
docstring carries the left IP’s Broca’s-area boundary and the left FEF’s
rightward-saccade / reading emphasis.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus complex)
--------------------------------------------------------------------------------

    corticospinal_tract (via right precentral gyrus, BA 4)
        → descends_through_posterior_limb_of_internal_capsule
        → cerebral_peduncle
        → spinal_cord (contralateral, **left** hand / left leg motor
          neurons)
        The corticospinal fibres originate in the right precentral
        gyrus **caudal to the precentral sulcus** and descend through
        the posterior limb of the internal capsule. The right
        precentral sulcus is the surface landmark for the **origin**
        of the left-hand component of this tract.

    frontal_aslant_tract (right)
        → traverses_beneath_caudal_right_PreCS
        → right_pre_supplementary_motor_area
        → right_pars_opercularis_of_ifg
        The right frontal aslant tract crosses beneath the caudal
        right precentral sulcus, connecting the right pre-SMA to the
        right pars opercularis. On the right, it is a core component
        of the **prosody-initiation and response-inhibition
        circuitry** — not the speech-production circuitry of the
        left.

    arcuate_fasciculus (right)
        → caps_right_operculum
        → right_posterior_superior_temporal_gyrus
        The right arcuate fasciculus caps the right operculum beneath
        the right inferior precentral sulcus. **The right arcuate is,
        on average, thinner and less continuous than the left’s**,
        consistent with the right hemisphere’s non-dominant role in
        language; it carries acoustic-to-prosodic mapping rather than
        sound-to-articulation mapping.

    superior_longitudinal_fasciculus (SLF, right)
        → traverses_beneath_superior_precentral_sulcus
        → right_superior_parietal_lobule
        → right_intraparietal_sulcus
        The SLF components run beneath the right SP, connecting the
        right premotor / prefrontal cortex to the right parietal
        cortex. The SLF II component supports the **right dorsal
        attention network** and the **right FEF ↔ right IPS circuit**
        [reference:21].

    uncinate_fasciculus (right)
        → traverses_beneath_ventral_right_PreCS
        → right_anterior_temporal_lobe
        The right uncinate’s frontal segment passes beneath the
        ventral right precentral sulcus (near the right pars
        opercularis / pars triangularis junction), connecting the
        right ventral affective-pragmatic network to the right
        anterior temporal lobe. On the right it carries **affective /
        socio-emotional** content rather than semantic content.

    extreme_capsule (right)
        → traverses_beneath_right_PreCS
        → right_insula (anterior)
        The right extreme capsule runs from the right opercular cortex
        across the right insula; its frontal origin lies beneath the
        right precentral sulcus.

    short-range U-fibres
        → connects_right_precentral_gyrus_to_caudal_right_frontal_gyri
        Short U-fibres cross beneath the right precentral sulcus,
        coupling the right premotor cortex (BA 6) to the right
        primary motor cortex (BA 4). These fibres support the
        **premotor → M1** interaction for left-hand action
        preparation and execution.

Note the **presence of multiple large association bundles** beneath
the right precentral sulcus (aslant tract, arcuate, SLF, uncinate,
extreme capsule) — this is a **corridor-rich** sulcus. On the right,
the **SLF component and the aslant tract carry the prosody-inhibition
and ventral-attention functions**, whereas on the left the same
bundles carry the language and speech-production functions.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri.superior_frontal_gyrus
    The dorsal bounding gyrus (right). The right SFG package already
    declares the precentral sulcus as its **caudal boundary**. The
    duality contract holds for this link.

..gyri.middle_frontal_gyrus
    The intermediate bounding gyrus (right). The right MFG package
    already declares the precentral sulcus as its **caudal boundary**.
    The duality contract holds for this link.

..gyri.inferior_frontal_gyrus
    The ventral bounding gyrus (right, via pars opercularis, BA 44).
    The right IFG package declares the **olfactory sulcus** as a
    boundary but **should also declare the inferior precentral
    sulcus** as its **caudal boundary**. This cross-reference is
    currently missing and must be added when the IFG package is
    updated — in both hemispheres in the same commit.

..gyri  (FORWARD REFERENCE)
    The **precentral gyrus** (BA 4) is **not yet a package** under
    ``..gyri``. When it is created, it must declare the precentral
    sulcus as its **rostral boundary**. See the FORWARD-DECLARATION
    CAVEAT below.

..sulci.paracentral_sulcus
    The precentral sulcus is the **lateral continuation** of the
    paracentral sulcus. The two sulci are continuous over the dorsal
    edge of the hemisphere: the right precentral sulcus turns medially
    and becomes the right paracentral sulcus. Both packages must
    declare this continuity.

..sulci.inferior_frontal_sulcus
    The IFS intersects the **inferior precentral sulcus** in roughly
    **70 % of specimens**. On the right, the IFS-IP junction is the
    surface landmark for the **inferior frontal junction (IFJ)** — a
    core node of task-switching and cognitive control[reference:22].
    The two sulci share a T-junction at the ventral frontal convexity.

..sulci.superior_frontal_sulcus
    The SFS intersects the **superior precentral sulcus** in roughly
    **80 % of specimens**, and the SP connects with the SFS in
    **more than 90 % of individuals**. The two sulci share a
    T-junction at the dorsal frontal convexity.

..brodmann_areas.brodmann_area_4
..brodmann_areas.brodmann_area_6
..brodmann_areas.brodmann_area_8
..brodmann_areas.brodmann_area_9
..brodmann_areas.brodmann_area_44
..brodmann_areas.brodmann_area_46
    The six BAs abutting the PreCS. Each must declare the PreCS as a
    boundary once the BA packages exist.

..cortex.premotor_cortex
    The rostral bank of the right precentral sulcus is the **right
    premotor cortex (BA 6)**. The premotor_cortex package must
    declare the right precentral sulcus as its **caudal boundary**,
    noting that the anterior limit of BA 6 is **variable and not
    sulcus-defined**.

..cortex.primary_motor_cortex
    The caudal bank of the right precentral sulcus is the **right
    primary motor cortex (BA 4)** — the right precentral gyrus. The
    primary_motor_cortex package must declare the right precentral
    sulcus as its **rostral boundary**, and must note the **hand
    knob / omega sign** as the surface landmark for the **left hand
    area**.

..cortex.supplementary_motor_cortex
    The medial continuation of the right precentral sulcus is the
    right paracentral sulcus, which borders the right SMA/pre-SMA.
    The supplementary_motor_cortex package must declare this
    continuity, and must note the right SMA’s role in left-hand
    motor planning.

../../subcortical/basal_ganglia/striatum/dorsal_striatum
    The corticostriatal projections from the right premotor and
    prefrontal cortex pass beneath the right precentral sulcus en
    route to the right caudate and putamen. The striatum package must
    declare the PreCS as a landmark for the **corticostriatal
    corridor**.

../../subcortical/medial_temporal_lobe/amygdala  — indirect
    No direct amygdala projection originates in the right precentral
    sulcus. Recorded here only to pre-empt a false cross-reference.

../../left/cortex/frontal/sulci/precentral_sulcus
    The left-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
    MUST be byte-identical to this package. Geometric and clinical
    fields (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED
    to differ — the right IP is the posterior boundary of the
    prosody-inhibition operculum; the right FEF is the dominant node
    of the ventral attention network; the right hand knob represents
    the left hand.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "precentral_sulcus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to left
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

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "rostral": (6, 8, 9, 44, 46),
                              "caudal":  (4,),
                          }

    EXTENT              = {                          # identical to left
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

    VARIANTS            = (                          # DIFFERS from left
                              "two_part_configuration_most_common",
                              "three_part_configuration_~17%",
                              "continuous_single_sulcus_minority",
                              "superior_precentral_sulcus_connects_"
                              "with_SFS_>90%",
                              "IP_single_segment_96%",
                              "IP_bifid_4%",
                              "IP_no_connection_with_SFS_78%",
                              "IP_morphological_patterns_arcuate_"
                              "ramified_bayonet_Y_tiny",
                              "left_right_asymmetry_pattern_type_"
                              "may_differ_across_hemispheres",
                              "rightward_functional_asymmetry_not_"
                              "explained_by_sulcal_geometry",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from left
                              "left_hand_knob_localization",
                              "right_fef_ventral_attention_reorienting",
                              "right_broca_homologue_prosody_and_"
                              "inhibition",
                              "surgical_corridor_for_right_precentral_"
                              "lesions",
                              "epilepsy_surgery_landmark",
                              "tumour_resection_left_hand_eloquent_"
                              "cortex",
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

    superior_frontal_gyrus    → resolves today (the right SFG package
                                exists and declares the PreCS as its
                                caudal boundary)
    middle_frontal_gyrus      → resolves today (the right MFG package
                                exists and declares the PreCS as its
                                caudal boundary)
    inferior_frontal_gyrus    → **partially resolves** — the right IFG
                                package exists but does **not yet
                                declare the inferior precentral
                                sulcus** as its caudal boundary. This
                                cross-reference must be added.
    precentral_gyrus          → forward reference

**The precentral gyrus is the forward reference**, and it is the
anatomical substrate of BA 4 — the primary motor cortex. The precentral
gyrus package should be built out **before** the right-hemisphere
precentral sulcus is finalised, so that the right side can be authored
without the same unresolved-reference burden. If the right side is
written first, it must carry the identical caveat text — the two
hemispheres must not diverge in their handling of unresolved
references.

**The IFG cross-reference is a separate issue**: the right IFG package
must be updated to declare the **inferior precentral sulcus** as its
**caudal boundary** (via pars opercularis, BA 44). This is a one-line
addition to the IFG package’s boundary cross-references and should be
made in both hemispheres in the same commit.

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
  4. Mirror the promotion on the left side in the same commit.

**Duality caveat**: the frontal gyri and the precentral gyrus declare
the precentral sulcus *as a whole* as their boundary. A component
split does not break the duality contract as long as the parent
remains the canonical answer to “what does the precentral sulcus
bound?” and the components refine *which part* bounds what.

**No split should be performed while the FORWARD-DECLARATION CAVEAT is
in force.** Splitting a sulcus whose precentral gyrus does not yet
exist as a package multiplies unresolved references and makes the
eventual duality reconciliation harder.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../precentral_sulcus``:

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
        HEMISPHERE           "right" vs "left"
        VARIANTS             same two-part / three-part / continuous
                             taxonomy; **right IP no-connection-with-
                             SFS is 78 % vs left 84 %**; IP
                             morphological-pattern frequencies differ
                             by sex and side; the entry
                             "rightward_functional_asymmetry_not_
                             explained_by_sulcal_geometry" is
                             right-only.
        CLINICAL_ANCHORS     right: **left hand** knob, right FEF
                             ventral-attention reorienting, right IP
                             prosody/inhibition boundary, left-hand
                             eloquent-cortex tumour resection; left:
                             **right hand** knob, left IP Broca’s-
                             area boundary, left FEF rightward /
                             reading saccades.
        CONNECTIVITY         same bundle names; right arcuate and SLF
                             III are thinner; right aslant carries
                             prosody/inhibition content; right
                             uncinate carries affective content.

**The right FEF’s ventral-attention dominance is the single most
important entry in this contract.** The rightward functional asymmetry
of the saccadic/attentional system is a **network property, not a
sulcal-geometry property** — it is not explained by differences in
grey-matter density or sulcal position between hemispheres
[reference:23]. Any downstream code that assigns FEF function must
therefore weight the right FEF toward **reorienting to salience** and
the left FEF toward **volitional / reading-related saccades**, and must
not assume symmetry from the identical sulcal geometry.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "precentral_sulcus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BOUNDING_GYRI is **compound** — a per-component dict with keys
    "superior_precentral_sulcus" and "inferior_precentral_sulcus" —
    and is byte-identical to the left sibling’s BOUNDING_GYRI.
[ ] BOUNDING_GYRI names superior_frontal_gyrus,
    middle_frontal_gyrus, and inferior_frontal_gyrus on the rostral
    side, and precentral_gyrus on the caudal side.
[ ] BRODMANN_ADJACENCY is compound, per-component, set-valued, and
    byte-identical to the left sibling’s: rostral (6, 8, 9, 44, 46),
    caudal (4,).
[ ] The BA 6 boundary caution is documented: the anterior limit of
    BA 6 is **variable and not sulcus-defined**.
[ ] EXTENT is byte-identical to the left sibling: SP superior-border
    reach (~12 / ~14 / ~74 %) and IP Sylvian-fissure approach.
[ ] SUBDIVISIONS is empty and byte-identical to the left sibling.
[ ] VARIANTS documents the two-part (most common), three-part
    (~17 %), and continuous (minority) configurations.
[ ] VARIANTS documents the **right IP single-segment rate (96 %)**,
    **bifid rate (4 %)**, and **IP-SFS no-connection rate (78 % vs
    left 84 %)**.
[ ] VARIANTS documents the right IP morphological-pattern frequencies
    by sex (arcuate 16/9, ramified 7/3, bayonet 19/19, Y 2/1,
    tiny 3/3).
[ ] VARIANTS includes the right-only entry
    "rightward_functional_asymmetry_not_explained_by_sulcal_geometry"
    [reference:26].
[ ] CLINICAL_ANCHORS contains the seven right-specific anchors:
    left_hand_knob_localization, right_fef_ventral_attention_
    reorienting, right_broca_homologue_prosody_and_inhibition,
    surgical_corridor_for_right_precentral_lesions,
    epilepsy_surgery_landmark, tumour_resection_left_hand_eloquent_
    cortex, central_sulcus_confusion_hazard.
[ ] CONNECTIVITY contains the seven entries (corticospinal to **left**
    hand/leg, right aslant, right arcuate, right SLF, right uncinate,
    right extreme capsule, short U-fibres), with right-side
    prosody/inhibition and affective emphasis.
[ ] The corticospinal entry explicitly names the **left** hand / leg
    motor neurons as the contralateral target.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.superior_frontal_gyrus`` and
    ``..gyri.middle_frontal_gyrus`` (right) both declare the PreCS as
    their caudal boundary — the duality contract holds for these links.
[ ] The right IFG package is flagged for the **missing** inferior
    precentral sulcus cross-reference — it must be added in both
    hemispheres in the same commit.
[ ] The FORWARD-DECLARATION CAVEAT is present and specifies that
    **precentral_gyrus** is the unresolvable gyrus name.
[ ] The recommendation to build out the precentral gyrus package
    before finalising the right-hemisphere PreCS is recorded.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields
    (compound BOUNDING_GYRI, compound BRODMANN_ADJACENCY, EXTENT,
    SUBDIVISIONS) match the left sibling; VARIANTS (right IP
    no-connection rate, right-only geometry-independence entry),
    CLINICAL_ANCHORS (left-hand knob, FEF reorienting, prosody /
    inhibition), and CONNECTIVITY (thinner right arcuate, affective
    uncinate) deliberately differ.
[ ] Any downstream code assigning FEF function is required to weight
    the right FEF toward **reorienting to salience** and the left FEF
    toward **volitional / reading-related saccades** — the rightward
    functional asymmetry is a network property, not a sulcal-geometry
    property, and must not be averaged away[reference:27].
"""