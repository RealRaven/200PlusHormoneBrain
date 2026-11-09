"""
Paracentral Sulcus (PaCS) — Right Hemisphere
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
                                    └── paracentral_sulcus   ← THIS PACKAGE

This is a **leaf sulcus** package on the **medial surface** of the
hemisphere. Unlike every other sulcus in ``..sulci``, which lives on the
lateral or orbital convexity, the paracentral sulcus is visible only in
midsagittal section. It is the **anterior margin of the paracentral
lobule** — the vertical groove that separates the medial frontal gyrus
(the medial continuation of the superior frontal gyrus) from the
paracentral lobule.

Parent: ``..sulci`` — sibling to ``inferior_frontal_sulcus``,
``olfactory_sulcus``, ``orbital_sulcus``, ``precentral_sulcus``, and
``superior_frontal_sulcus``.

This package is the **structural mirror** of
``../../left/cortex/frontal/sulci/paracentral_sulcus``. Structural
fields (SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT,
SUBDIVISIONS) are identical by contract; geometric and clinical fields
(VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) diverge by design.

--------------------------------------------------------------------------------
WHAT THE PaCS IS
--------------------------------------------------------------------------------

The paracentral sulcus is a **short vertical sulcus on the medial
surface** of the hemisphere, running dorsoventrally just **rostral to
the paracentral lobule**. It is the medial continuation of the
**precentral sulcus**: the precentral sulcus on the lateral convexity
turns over the dorsal edge of the hemisphere and continues onto the
medial wall as the paracentral sulcus. Its caudal
counterpart is the **marginal sulcus** (the upturned posterior end of
the cingulate sulcus), which forms the posterior boundary of the
paracentral lobule.

The sulcus is therefore the **rostral boundary of the paracentral
lobule** and the **caudal boundary of the medial frontal gyrus**. It is
one of the three sulci that frame the paracentral lobule (the others
being the marginal sulcus caudally and the cingulate sulcus ventrally).

Two anatomical cautions are load-bearing:

1. **The paracentral fossa is not the paracentral sulcus.** A shallow
   dimple within the paracentral lobule — the *paracentral fossa
   (pacf)* — is sometimes mistaken for the sulcus on imaging. The
   fossa is a dimple; the sulcus is the anterior border of the
   lobule.

2. **The paracentral sulcus is not the marginal sulcus.** The marginal
   sulcus is the *posterior* boundary of the paracentral lobule; the
   paracentral sulcus is the *anterior* boundary. Confusing the two
   reverses the rostrocaudal orientation of the entire medial
   sensorimotor strip.

**Right-hemisphere specificity**: the right paracentral lobule is
**reliably smaller than the left**. Extrasulcal surface area is
approximately **5.35 cm² on the right vs 6.51 cm² on the left**
across a 42-brain series, and **8.36 cm² vs 10.22 cm²** in a separate
series using a different delineation protocol. In sex-stratified
data, males show **5.76 cm² (right) vs 6.79 cm² (left)** and females
show **5.16 cm² (right) vs 6.05 cm² (left)**. The right PCL also
carries the **left** leg, foot, and perineum representation — the
contralateral counterpart of the left PCL's right-sided
representation.

The right PCL is not merely a smaller mirror of the left. It shows
**rightward-lateralized resting-state variability** in ADHD cohorts,
**reduced cortical thickness** in at-risk mental-state individuals
with poor 1-year functional outcomes, and a slightly **greater
distance from the inferior PCL to the corpus callosum** than the left
(11.37 mm vs 11.09 mm in males; 11.67 mm vs 11.20 mm in females).
These asymmetries are the right-hemisphere's clinical signature.

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction   Gyrus(es) bounded
    ---------   --------------------------------------------------------
    rostral     medial_frontal_gyrus   (medial continuation of the
                                        superior frontal gyrus; BA 6)
    caudal      paracentral_lobule     (medial continuation of the
                                        precentral and postcentral gyri;
                                        BA 4 + BA 3/1/2 + BA 5)

**This field is byte-identical to the left-hemisphere sibling.** The
topology of which gyrus lies rostral and which caudal to the PaCS is
hemisphere-invariant. Both sides use the same two bounding gyri.

The paracentral sulcus is a **two-sided sulcus**, but both sides are on
the **medial wall** — a configuration unique among the frontal sulci.
The rostral bank is the medial frontal gyrus (BA 6, SMA/pre-SMA); the
caudal bank is the paracentral lobule (BA 4 anteriorly, BA 3/1/2
posteriorly, BA 5 inferiorly).

**Both bounding gyri are forward references.** Neither
``medial_frontal_gyrus`` nor ``paracentral_lobule`` exists as a package
under ``..gyri`` today. The parent ``..sulci`` duality contract cannot
resolve this sulcus until the medial-wall gyrus packages are built out.
See the FORWARD-DECLARATION CAVEAT below.

Note that the **paracentral lobule is not a "gyrus" in the classical
sense** — it is a *lobule*, a composite of the medial precentral and
postcentral strips. When it becomes a package under ``..gyri``, its own
``BRODMANN_AREAS`` will span BA 4, 3, 1, 2, and 5, and it will declare
the paracentral sulcus as its **rostral** boundary.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side      Brodmann areas abutting the sulcus
    ------    --------------------------------------------------------
    rostral   BA 6
    caudal    BA 4, BA 3, BA 1, BA 2, BA 5

Interpretation (right-hemisphere functional annotations):

    rostral (medial frontal gyrus side)
        BA 6   medial aspect of the superior frontal gyrus —
               supplementary motor area (SMA) and pre-supplementary
               motor area (pre-SMA). Self-initiated movement,
               motor-sequence planning, and action readiness. On the
               right, the SMA contributes to **left-hand** motor
               planning and bimanual coordination support.

    caudal (paracentral lobule side)
        BA 4   anterior portion of the PCL — medial primary motor
               cortex for the **contralateral (left) leg, foot, and
               perineum**. The cortical centre of micturition
               and defecation control.
        BA 3   postcentral strip — primary somatosensory cortex for
               the left leg and foot.
        BA 1   postcentral strip — somatosensory association.
        BA 2   postcentral strip — deep-tissue sensation.
        BA 5   inferior portion of the PCL — somatosensory
               association and goal-oriented limb movement.

**This field is byte-identical to the left-hemisphere sibling.** The
Brodmann-area adjacency is numerically symmetric across hemispheres;
the functional annotations above differ (right BA 6/4 carry the left
limb representation rather than the left's right limb representation)
but the BA numbers do not.

The paracentral sulcus separates the **medial premotor / supplementary
motor** cortex (BA 6) from the **medial primary sensorimotor strip**
(BA 4 + BA 3/1/2) and its inferior association extension (BA 5). On the
right, this boundary separates the right SMA (left-hand motor planning)
from the right medial M1/S1 strip (left leg, foot, perineum).

The **central sulcus** — the boundary between BA 4 and BA 3 — is often
**not visible on the medial surface**, so the paracentral sulcus is
one of the few reliable surface guides to the cytoarchitectonic
transition from motor to sensory cortex in the medial wall.

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    dorsal end
        Reaches the **superior hemispheric border**, where the
        paracentral sulcus is continuous with the **precentral
        sulcus** on the lateral convexity. The precentral sulcus
        turns medially over the dorsal edge and becomes the
        paracentral sulcus.

    ventral end
        Approaches the **cingulate sulcus** (or the medial
        frontal gyrus's inferior limit). The paracentral sulcus
        does not always reach the cingulate sulcus; in many
        hemispheres it fades before doing so, leaving the medial
        frontal gyrus and the paracentral lobule in continuity
        ventrally.

**This field is byte-identical to the left-hemisphere sibling.** The
dorsal continuity with the precentral sulcus and the variable ventral
approach to the cingulate sulcus are hemisphere-invariant.

The paracentral sulcus is therefore a **short sulcus with one fixed
end (dorsal) and one variable end (ventral)**. Its dorsal continuity
with the precentral sulcus is the reliable landmark; its ventral
extent is variable.

--------------------------------------------------------------------------------
VARIANTS (right-hemisphere specific)
--------------------------------------------------------------------------------

The paracentral sulcus is one of the **less consistently present**
frontal sulci. Its principal variant is presence/absence, followed by
continuity and the morphology of the paracentral lobule it borders.
The presence/absence rate is **hemisphere-invariant (~50 %)**, but the
**surface area** and **segmentation pattern** carry right-specific
values.

    present_as_a_distinct_sulcus      ~50 %
        The paracentral sulcus was identified as a distinct sulcus
        in **50 % of examined hemispheres**. In the other half, the
        boundary between the medial frontal gyrus and the
        paracentral lobule is not marked by a distinct sulcus.
        **This rate is the same on the right as on the left** —
        the sulcus is equally likely to be absent in either
        hemisphere.

    absent_or_indistinct              ~50 %
        When absent, the medial frontal gyrus and the paracentral
        lobule are in continuity, and the boundary must be
        inferred from the intercommissural line or from
        cytoarchitectonic criteria.

    right_pcl_smaller                  consistent finding
        The right PCL's extrasulcal surface is **significantly
        smaller** than the left's. Right-hemisphere means across
        studies: **5.35 cm²** (range 2.41–9.08), **8.36 cm²**,
        **5.76 cm² in males / 5.16 cm² in females**. The
        right PCL also shows **greater coefficient of variation**
        (25.0 % vs 19.2 % on the left), i.e. the right PCL is not
        only smaller but **more variable across individuals**.

    partially_segmented_pcl_type      ~91 %
        The right PCL is partially segmented by an upturned branch
        of the cingulate sulcus, but the constituent gyri remain in
        continuity for most of the lobule's extent. This is the
        **dominant morphology** on both sides.

    completely_segmented_pcl_type     ~7 %
        The right PCL may be completely segmented, often with a
        short **transitional lobulo-limbic gyrus (LLTG)**
        interposed between the PCL proper and the cingulate gyrus.
        The LLTG is present in **13–37 % of hemispheres** depending
        on the series.

    right_pcl_cortical_thickness      context-dependent
        **Right PCL cortical thickness is the more sensitive
        asymmetry in several clinical populations.** Reduced
        right PCL thickness is observed in **at-risk mental-state
        individuals with poor 1-year functional outcomes** and in
        **ADHD**, where the right PCL shows increased
        right-lateralization of resting-state variability. In
        healthy controls, cortical-thickness asymmetry in the PCL
        is **leftward** (left thicker than right: 2.40 mm vs
        2.35 mm in one series), but the right PCL is the side that
        **changes most in disease**.

    right_pcl_corpus_callosum_distance slightly larger
        The distance from the inferior PCL to the corpus callosum
        is slightly **larger on the right** than on the left:
        **11.37 mm vs 11.09 mm** in males, **11.67 mm vs 11.20 mm**
        in females. The difference is small but
        consistent, and may reflect the right PCL's slightly more
        inferior position relative to the callosal body.

These variants are **geometric, presence/absence, and morphometric**.
When the sulcus is present, BOUNDING_GYRI and BRODMANN_ADJACENCY hold
as declared. When absent, the boundary exists cytoarchitectonically but
not as a visible groove — downstream code must therefore treat
``SULCUS_PRESENT_FRACTION ≈ 0.50`` as a first-class field on **both**
sides.

The right-specific entries are the **smaller surface area**, the
**greater coefficient of variation**, the **rightward-lateralized
resting-state variability in ADHD**, the **reduced cortical thickness
in at-risk mental states**, and the **slightly greater PCL-to-callosum
distance**.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    left_leg_foot_perineum_motor_representation
        **This is the right-PaCS anchor par excellence.** The **right**
        paracentral lobule contains the medial primary motor
        representation of the **contralateral (left) leg, foot, and
        perineum**. An isolated **left lower limb weakness** can be
        caused by a lesion involving the anterior (motor) part of
        the **right paracentral lobule**; such a lesion interrupts
        the origin of the corticospinal fibres to the left lower
        limb. MRI-documented cases include **left toe paralysis**
        from a right PCL infarct. Right PCL damage produces
        **left leg weakness**, left foot drop, and — when the
        perineal representation is involved — **urinary and faecal
        incontinence**.

    micturition_and_defecation_control
        The paracentral lobule is the **cortical centre of
        micturition and defecation** on both sides. On the
        right, the PCL's connections to the brainstem and
        periaqueductal grey support voluntary control of the
        bladder and anal sphincters. Right PCL lesions can produce
        urgency, incontinence, or retention, though the effect is
        not as strongly lateralized as the leg motor deficit.

    central_region_epilepsy_left_leg
        The right PCL is part of the **central region** from which
        central-region epilepsy arises. Seizures beginning in the
        right PCL produce **focal motor seizures of the left leg**,
        often with a Jacksonian march from foot to leg to face.
        Notably, **seizures involving the paracentral lobule may
        produce tonic movements of the ipsilateral (right) foot
        in addition to the expected contralateral (left) leg
        movements** — a right-PCL-specific semiological feature
        that reflects the PCL's bilateral callosal connections.

    paracentral_cavernomas_transsulcal_approach
        Cavernomas in the paracentral area present most often with
        **epileptic seizures**. The **transsulcal approach**
        through the paracentral sulcus — supported by
        navigation-guided neurophysiological monitoring — is the
        surgical strategy for resecting right paracentral
        cavernomas while preserving the left leg motor cortex.
        The sulcus is the corridor, not just the landmark.

    focal_cortical_dysplasia_type_2
        Focal cortical dysplasia type 2 in the central region —
        including the right paracentral lobule — can be resected
        with **excellent seizure outcome and low rates of major
        permanent disability**. The right PCL's smaller surface
        area makes the resection margin tighter, and the
        paracentral sulcus is the anterior limit of the resection.

    presurgical_depth_electrode_planning
        Identification of the central region on MRI and angiography
        is necessary before **stereotactic biopsies, depth electrode
        recordings, and resection of centrally located tumours**.
        The right paracentral sulcus is one of the two medial
        landmarks (with the marginal sulcus) for the right PCL in
        these procedures, and the slightly greater PCL-to-callosum
        distance (11.37 mm) must be accounted for in trajectory
        planning.

    adhd_right_lateralization
        **This is a right-only anchor.** The right PCL shows
        **increased right-lateralization of resting-state fMRI
        variability** in ADHD patients, and paracentral cortical
        asymmetry differs significantly between ADHD-C and
        typically developing groups. This finding has no
        left-hemisphere counterpart in the current literature and
        belongs to the right PaCS package alone.

    at_risk_mental_state_cortical_thinning
        **This is a right-only anchor.** Reduced cortical thickness
        of the paracentral lobule — with right-PCL emphasis — is
        observed in **at-risk mental-state individuals with poor
        1-year functional outcomes**. The right PCL is the side
        whose thickness is most informative about functional
        prognosis.

These anchors are **right-hemisphere-specific** in two senses: (a) the
right PCL carries the **left** leg/foot/perineum representation, so
right PCL lesions produce **left-sided** deficits; (b) the ADHD
right-lateralization and at-risk-mental-state cortical-thinning
findings are reported with right-PCL emphasis and are documented here
as right-only anchors. The left sibling's docstring carries the right
leg/foot representation and the left-sided surgical emphases.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath and around the sulcus)
--------------------------------------------------------------------------------

    paracentral_lobule_tract (intrinsic U-fibres)
        → connects_medial_frontal_gyrus_to_paracentral_lobule
        → connects_anterior_pcl_to_posterior_pcl
        Short-range U-fibres run beneath the paracentral sulcus,
        coupling the medial frontal gyrus (BA 6 / SMA) to the
        anterior PCL (BA 4) and coupling the anterior and
        posterior portions of the PCL to each other. On the right,
        these fibres support the **right SMA → right medial M1**
        interaction for left-leg self-initiated movement.

    corticospinal_tract (via right medial BA 4)
        → descends_through_posterior_limb_of_internal_capsule
        → cerebral_peduncle
        → spinal_cord (contralateral, **left** leg / foot / perineal
          motor neurons)
        The right medial BA 4 component of the PCL contributes to
        the corticospinal tract that controls the **left** leg and
        foot. The fibres descend through the posterior limb of the
        internal capsule and the cerebral peduncle. The right PCL's
        smaller surface area means its corticospinal contribution
        is **proportionally smaller** than the left's, but it is
        the sole cortical origin of the left leg's voluntary motor
        control.

    thalamocortical_projections
        → right_ventral_posterior_lateral_nucleus (VPL)
        → right_ventral_lateral_nucleus (VL)
        Thalamocortical tracts run medial to the pyramidal
        projections and enter the thalamus. The right VPL relays
        left leg/foot somatosensory input to the postcentral PCL;
        the right VL relays cerebellar and basal-ganglia input to
        the precentral PCL.

    corpus_callosum (body)
        → left_paracentral_lobule
        Contralateral connections course through the **body of the
        corpus callosum** to the homotopic left PCL; the callosal
        body explicitly connects the left and right paracentral
        lobules. These fibres coordinate the two legs in
        bipedal tasks and in axial/truncal control. The right
        PCL's slightly **greater distance to the callosum**
        (11.37 mm vs 11.09 mm in males) means its callosal
        trajectory is marginally longer than the left's.

    cingulate_connections
        → right_anterior_cingulate
        → right_posterior_cingulate
        Local short association fibres connect the right PCL to
        the right cingulate cortex. These fibres support the
        affective–motor interface (urgency of micturition) and the
        cingulate's role in pain affect and error monitoring
        adjacent to the left-leg motor area.

    superior_longitudinal_fasciculus (medial components)
        → right_superior_parietal_lobule
        → right_precuneus
        Medial SLF components connect the right PCL to the right
        superior parietal lobule and precuneus, supporting the
        sensorimotor–spatial interface for left lower-limb
        navigation and postural control.

    medial_forebrain_bundle / septal connections
        → traverses_beneath_ventral_paracentral_sulcus
        → septal_nuclei
        Ventral continuations of the medial frontal pathways pass
        beneath the inferior limit of the paracentral sulcus
        toward the septal region. These are minor but relevant to
        the right PCL's autonomic (micturition) role.

Note the **absence of a single large dorsal association bundle**
directly beneath the paracentral sulcus: like the orbital and
olfactory sulci, the PaCS is not the surface landmark for one dominant
fasciculus. Its white-matter relationships are **distributed** —
intrinsic U-fibres across the sulcus, corticospinal and
thalamocortical fibres descending beneath the PCL, callosal fibres
crossing in the body of the corpus callosum, and cingulate and SLF
connections laterally.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri  (FORWARD REFERENCES — see the caveat below)
    The medial frontal gyrus (``medial_frontal_gyrus``) and the
    paracentral lobule (``paracentral_lobule``) are **not yet
    packages** under ``..gyri``. When they are created, each must
    declare the paracentral sulcus as a boundary, and the duality
    contract will then apply fully.

..gyri.superior_frontal_gyrus
    The medial frontal gyrus is the **medial continuation** of the
    right superior frontal gyrus. The right SFG package already
    exists and carries BA 6 (SMA / pre-SMA) in its
    ``BRODMANN_AREAS``. When the medial frontal gyrus is promoted
    to its own package, it should be cross-referenced from the SFG
    package as the medial BA 6 extension.

..sulci.precentral_sulcus
    The paracentral sulcus is the **medial continuation** of the
    right precentral sulcus. The two sulci are continuous over the
    dorsal edge of the hemisphere. The right precentral sulcus
    package must declare this continuity.

..sulci.olfactory_sulcus  — no direct relationship
    Recorded here only to pre-empt a false cross-reference. The
    olfactory sulcus is on the orbital surface; the paracentral
    sulcus is on the medial surface. They are not neighbours.

..brodmann_areas.brodmann_area_6
..brodmann_areas.brodmann_area_4
..brodmann_areas.brodmann_area_3
..brodmann_areas.brodmann_area_1
..brodmann_areas.brodmann_area_2
..brodmann_areas.brodmann_area_5
    The six BAs abutting the PaCS. Each must declare the PaCS as a
    boundary once the BA packages exist.

..cortex.supplementary_motor_cortex
    The rostral bank of the right paracentral sulcus is the medial
    BA 6 territory — the **right SMA / pre-SMA**. The
    supplementary_motor_cortex package must declare the paracentral
    sulcus as the **caudal boundary** of the right SMA's medial
    extent, and must note the right SMA's role in left-hand motor
    planning.

..cortex.primary_motor_cortex
    The caudal bank of the right paracentral sulcus is the **medial
    BA 4** territory — the **left leg / foot / perineum**
    representation of the right primary motor cortex. The
    primary_motor_cortex package must declare the paracentral
    sulcus as the **rostral boundary** of the right medial M1
    strip, and must note the contralateral (left) limb
    representation.

..cortex.primary_somatosensory_cortex (if/when created)
    The posterior portion of the right paracentral lobule contains
    BA 3, 1, and 2 — the medial primary somatosensory
    representation of the **left** leg and foot. The somatosensory
    package must declare the paracentral sulcus as the **rostral
    boundary** of the right medial S1 strip.

../../subcortical/basal_ganglia  — indirect
    The corticospinal fibres from right medial BA 4 descend through
    the posterior limb of the internal capsule, adjacent to the
    basal ganglia. No direct basal-ganglia projection originates in
    the PCL; the relationship is via the corticospinal tract.

../../subcortical/medial_temporal_lobe/hippocampus
    The cingulate connections from the right PCL run adjacent to
    the parahippocampal gyrus but do not terminate there. No direct
    hippocampal projection originates in the PCL. Recorded here
    only to pre-empt a false cross-reference.

../../left/cortex/frontal/sulci/paracentral_sulcus
    The left-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
    MUST be byte-identical to this package. Geometric and clinical
    fields (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED
    to differ — the right PCL is smaller and more variable, carries
    the **left** leg/foot representation, and has the ADHD
    right-lateralization and at-risk-mental-state cortical-thinning
    anchors that the left does not.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "paracentral_sulcus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to left
                              "rostral": ("medial_frontal_gyrus",),
                              "caudal":  ("paracentral_lobule",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "rostral": (6,),
                              "caudal":  (4, 3, 1, 2, 5),
                          }

    EXTENT              = {                          # identical to left
                              "dorsal":  ("superior_hemispheric_border",
                                          "precentral_sulcus"),
                              "ventral": ("cingulate_sulcus",
                                          "medial_frontal_gyrus"),
                          }

    VARIANTS            = (                          # DIFFERS from left
                              "present_as_distinct_sulcus_~50%",
                              "absent_or_indistinct_~50%",
                              "right_pcl_smaller_5_35_vs_6_51_cm2",
                              "right_pcl_greater_cv_25_0_vs_19_2_pct",
                              "partially_segmented_pcl_type_~91%",
                              "completely_segmented_pcl_type_~7%",
                              "right_pcl_cortical_thickness_reduced_in_"
                              "at_risk_mental_state",
                              "right_pcl_corpus_callosum_distance_"
                              "11_37_mm_vs_11_09_mm",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from left
                              "left_leg_foot_perineum_motor_"
                              "representation",
                              "micturition_and_defecation_control",
                              "central_region_epilepsy_left_leg_"
                              "ipsilateral_foot_tonic_movements",
                              "paracentral_cavernomas_transsulcal_"
                              "approach",
                              "focal_cortical_dysplasia_type_2",
                              "presurgical_depth_electrode_planning",
                              "adhd_right_lateralization",
                              "at_risk_mental_state_cortical_thinning",
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

Note: ``SUBDIVISIONS`` is an empty tuple — the PaCS is a leaf sulcus.
The field is kept for uniformity with the parent ``..sulci`` contract
and must NOT be deleted; downstream code iterates ``SUBDIVISIONS``
unconditionally.

No behaviour. This package is a declarative descriptor; all computation
that references the PaCS lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT (unique to this sulcus)
--------------------------------------------------------------------------------

The parent ``..sulci`` duality contract states: *every gyrus named in
any BOUNDING_GYRI MUST exist in ``..gyri.GYRI``.* **The paracentral
sulcus is one of the sulci for which this cannot yet hold.**

Of the two gyrus names in this package's BOUNDING_GYRI:

    medial_frontal_gyrus   → forward reference
    paracentral_lobule     → forward reference

**Both bounding gyri are unresolvable.** The parent inversion function
must be explicitly parameterised to tolerate unresolvable gyrus names
for the ``paracentral_sulcus`` entry, alongside the ``olfactory_sulcus``
and ``orbital_sulcus`` entries.

**This caveat text is byte-identical to the left sibling's.** Both
hemispheres carry it until the medial-wall gyrus packages are created;
the right side must not silently drop it or implement a different
tolerance policy.

The **paracentral lobule is the more consequential of the two forward
references** — it is the target of the sulcus's entire clinical
rationale. The PCL package should be built out **before** the
right-hemisphere paracentral sulcus is written, so that the right side
can be authored without the same unresolved-reference burden. If the
right side is written first, it must carry the identical caveat text.

--------------------------------------------------------------------------------
PROMOTION RULE (when a sulcus segment becomes a package)
--------------------------------------------------------------------------------

A sulcus is an **edge**, not a **node**, so the standard promotion rule
does not directly apply. For the paracentral sulcus, two segmentation
schemes are conceivable:

    dorsal / ventral split
        A ``pars_dorsalis`` (the segment continuous with the
        precentral sulcus at the superior border) and a
        ``pars_ventralis`` (the variable segment approaching the
        cingulate sulcus). This is anatomically natural because the
        dorsal end is a fixed landmark and the ventral end is
        variable.

    absent_sulcus placeholder
        When the sulcus is absent (~50 % of hemispheres), there is
        no groove to split. A placeholder package would not be
        useful; the absence should be recorded as a boolean field
        rather than as a sub-package.

If the dorsal / ventral split is adopted:

  1. Add "pars_dorsalis" and "pars_ventralis" to ``SUBDIVISIONS``.
  2. Keep ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and ``EXTENT``
     at the parent level as the union of the segments.
  3. Each segment declares its own restricted versions.
  4. Mirror the split on the left side in the same commit.

**Duality caveat**: the medial frontal gyrus and the paracentral
lobule declare the paracentral sulcus *as a whole* as their boundary.
A segment split does not create new gyri-facing partners — the parent
remains canonical.

**No split should be performed while the FORWARD-DECLARATION CAVEAT is
in force.** Splitting a sulcus whose two bounding gyri do not yet exist
multiplies unresolved references and makes the eventual duality
reconciliation harder.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../paracentral_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME          "paracentral_sulcus"
        LOBE                 "frontal"
        BOUNDING_GYRI        the same medial frontal gyrus ↔
                             paracentral lobule boundary
        BRODMANN_ADJACENCY   the same BA 6 ↔ BA 4/3/1/2/5 adjacency
        EXTENT               the same superior-border /
                             cingulate-sulcus landmarks
        SUBDIVISIONS         both empty (or both non-empty in the same
                             way, if a segment split is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "right" vs "left"
        VARIANTS             right: PCL smaller (5.35 vs 6.51 cm²;
                             8.36 vs 10.22 cm² in another series),
                             greater CV (25.0 % vs 19.2 %),
                             slightly greater PCL-to-callosum distance
                             (11.37 vs 11.09 mm in males); left: PCL
                             larger and less variable.
        CLINICAL_ANCHORS     right: **left** leg/foot/perineum
                             representation; right PCL lesions
                             produce **left-sided** deficits; ADHD
                             right-lateralization; at-risk-mental-
                             state cortical thinning; ipsilateral
                             (right) foot tonic movements during
                             seizures; left: **right** leg/foot
                             representation; left PCL lesions produce
                             right-sided deficits; no ADHD or at-
                             risk-mental-state anchor.
        CONNECTIVITY         same bundle names; the right corticospinal
                             contribution from medial BA 4 controls
                             the **left** leg; the callosal body
                             connects the right PCL to the left PCL
                             across a slightly longer trajectory.

**The smaller right PCL surface area is the single most important
entry in this contract.** The right PCL is reliably smaller
(5.35–8.36 cm² vs 6.51–10.22 cm²), more variable across individuals
(CV 25.0 % vs 19.2 %), and carries the left leg/foot representation.
Any downstream code that computes "PCL volume" or "leg motor
representation size" must specify hemisphere — averaging left and right
PCL would erase the asymmetry that is the anatomical signature of
right-hemisphere motor control for the left lower limb.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "paracentral_sulcus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BOUNDING_GYRI is byte-identical to the left sibling:
    rostral (medial_frontal_gyrus,), caudal (paracentral_lobule,).
[ ] Both bounding gyri are documented as forward references under
    ``..gyri``.
[ ] BRODMANN_ADJACENCY is byte-identical to the left sibling:
    rostral (6,), caudal (4, 3, 1, 2, 5).
[ ] EXTENT is byte-identical to the left sibling: dorsal continuity
    with the precentral sulcus, ventral approach to the cingulate
    sulcus.
[ ] The paracentral fossa (pacf) is explicitly distinguished from the
    paracentral sulcus (pacs).
[ ] The marginal sulcus is explicitly distinguished from the
    paracentral sulcus (posterior vs anterior boundary of the PCL).
[ ] SUBDIVISIONS is empty and byte-identical to the left sibling.
[ ] VARIANTS documents the **~50 % presence rate** of the sulcus on
    both sides.
[ ] VARIANTS documents the **right PCL smaller** finding (5.35 vs
    6.51 cm²; 8.36 vs 10.22 cm²; 5.76/5.16 vs 6.79/6.05 cm² by sex)
    and the **greater coefficient of variation** (25.0 % vs 19.2 %).
[ ] VARIANTS documents the **right PCL cortical thickness** findings
    (leftward asymmetry in healthy controls; right-PCL reduction in
    at-risk mental states; right-lateralized resting-state
    variability in ADHD).
[ ] VARIANTS documents the **slightly greater PCL-to-callosum
    distance** on the right (11.37 mm vs 11.09 mm in males).
[ ] CLINICAL_ANCHORS contains the eight right-specific anchors:
    left leg/foot/perineum representation, micturition/defecation
    control, central-region epilepsy with **ipsilateral foot tonic
    movements**, paracentral cavernomas transsulcal approach, focal
    cortical dysplasia type 2, presurgical depth-electrode planning,
    **ADHD right-lateralization**, **at-risk-mental-state cortical
    thinning**.
[ ] CONNECTIVITY separates the **intrinsic U-fibres** from the
    **descending** (corticospinal to the **left** leg, thalamocortical),
    **crossing** (corpus callosum body to the left PCL), and
    **adjacent** (cingulate, SLF) bundles.
[ ] The corticospinal entry explicitly names the **left** leg / foot /
    perineal motor neurons as the contralateral target.
[ ] The callosal entry explicitly names the **left** paracentral
    lobule as the contralateral target, and notes the slightly longer
    trajectory on the right.
[ ] The absence of a single dominant dorsal association bundle is
    documented — the PaCS is a distributed white-matter landmark.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] The FORWARD-DECLARATION CAVEAT is present and is byte-identical to
    the left sibling's — both bounding gyri are unresolvable.
[ ] The recommendation to build out the paracentral lobule package
    before the right-hemisphere PaCS is recorded.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    left sibling; the smaller right PCL, the left-leg laterality, the
    ADHD and at-risk-mental-state anchors, and the slightly longer
    callosal trajectory deliberately differ.
[ ] Any downstream code computing "PCL volume" or "leg motor
    representation size" is required to specify hemisphere — averaging
    left and right would erase the anatomical signature of right
    motor control for the left lower limb.
"""