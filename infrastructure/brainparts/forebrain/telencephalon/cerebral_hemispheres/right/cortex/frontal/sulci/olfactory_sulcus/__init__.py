"""
Olfactory Sulcus (OS) — Right Hemisphere
=========================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
                  └── cortex
                        └── frontal
                              └── sulci
                                    └── olfactory_sulcus   ← THIS PACKAGE

This is a **leaf sulcus** package: it has no child packages. It is also
the only **container sulcus** in the frontal lobe — the olfactory bulb,
the olfactory tract, and the olfactory artery physically lie *within*
it, rather than merely bordering the gyri on either side. Every other
frontal sulcus is a groove between two gyri; the olfactory sulcus is a
groove that *houses an organ*. That structural difference drives most of
the special cases documented below.

Parent: ``..sulci`` — sibling to ``inferior_frontal_sulcus``,
``orbital_sulcus``, ``paracentral_sulcus``, ``precentral_sulcus``, and
``superior_frontal_sulcus``.

This package is the **structural mirror** of
``../../left/cortex/frontal/sulci/olfactory_sulcus``. Structural fields
(SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
are identical by contract; geometric and clinical fields (VARIANTS,
CLINICAL_ANCHORS, CONNECTIVITY) diverge by design.

--------------------------------------------------------------------------------
WHAT THE OS IS
--------------------------------------------------------------------------------

The olfactory sulcus is a **rostrocaudally directed sulcus on the orbital
(ventral) surface** of the frontal lobe, running in a paramedian
position from the frontal pole caudally toward the posterior orbital
region. It is the most medial of the orbital sulci and the anatomical
divider between the **medial** and **lateral** compartments of the
orbital surface:

    medial to the OS   → gyrus rectus (straight gyrus) and, caudally,
                         the medial aspect of the posterior orbital region
    lateral to the OS  → medial orbital gyrus, and further laterally the
                         anterior / lateral / posterior orbital gyri,
                         terminating caudolaterally in the pars orbitalis
                         of the inferior frontal gyrus

The olfactory bulb rests in the rostral portion of the sulcus; the
olfactory tract continues caudally within it; the olfactory artery runs
alongside them. The sulcus is therefore both a **gyral
boundary** and an **osseous-soft-tissue corridor** — a dual role no
other frontal sulcus has.

A geometric detail that matters for both imaging and surgery: the
**posterior end of the olfactory sulcus lies more lateral than its
anterior end** (Chiavaras & Petrides, 2000). The sulcus is
therefore not perfectly parasagittal — it diverges laterally as it runs
caudally, tracking the lateral drift of the gyrus rectus.

**Right-hemisphere specificity**: the right OS is **reliably deeper than
the left across all age groups** — normative minimum depth 8.78 mm on
the right vs 7.55 mm on the left at 18–35 years[reference:0]. This is one
of the most robust left–right asymmetries in the human orbitofrontal
surface, and it is the opposite of what one might expect if the left
were the "dominant" hemisphere for olfaction. The functional
consequence is counter-intuitive and is the single most important thing
to get right in this package: **the deeper right OS is NOT the one
whose depth tracks olfactory function.** The left OS is the
functionally informative side; the right OS is the structurally larger
side[reference:1].

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction   Gyrus(es) bounded
    ---------   --------------------------------------------------------
    medial      gyrus_rectus   (rostral and mid-portion)
                posterior_orbital_region_medial_aspect   (caudal portion)
    lateral     medial_orbital_gyrus   (rostral and mid-portion)
                pars_orbitalis_of_inferior_frontal_gyrus   (caudolateral
                                                            portion)

**This field is byte-identical to the left-hemisphere sibling.** The
topology of which gyrus lies on which side of the OS is
hemisphere-invariant.

Two important corrections relative to the parent ``..sulci`` docstring:

1. The parent docstring's shorthand ``olfactory_sulcus [IFG ↔ orbital
   surface]`` is **imprecise**. The IFG's pars orbitalis touches the
   olfactory sulcus only at its far caudolateral end; along most of its
   length the sulcus separates the **gyrus rectus** (medial) from the
   **medial orbital gyrus** (lateral). The parent docstring should be
   corrected to ``olfactory_sulcus [gyrus_rectus ↔ medial_orbital_gyrus
   (+ pars_orbitalis caudolaterally)]``.

2. The gyrus rectus and the medial orbital gyrus are **not yet modelled
   as gyrus packages** in ``..gyri``. Only IFG, MFG, and SFG exist
   there. This package therefore contains **forward references** to
   gyrus names that will exist once the orbital gyri are built out. See
   the FORWARD-DECLARATION CAVEAT below.

The gyrus rectus is worth flagging in its own right: it is generally
regarded as **the most anatomically constant of the cerebral gyri**
 — it is present in essentially every brain, with little
variation in its extent. The olfactory sulcus, as its lateral boundary,
inherits some of that constancy: it is one of the more reliably
identifiable orbital landmarks, which is why it is used as the reference
structure in volumetric MRI studies of olfactory dysfunction.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side      Brodmann areas abutting the sulcus
    ------    --------------------------------------------------------
    medial    BA 11, BA 12
    lateral   BA 11, BA 13, BA 14, BA 47

Interpretation (right-hemisphere functional annotations):

    medial (gyrus rectus side)
        BA 11  rostral / lateral gyrus rectus — medial orbitofrontal
               cortex, reward valuation and affective encoding
        BA 12  caudal / medial gyrus rectus — anterior cingulate
               -adjacent medial OFC, visceral / autonomic integration

    lateral (medial orbital gyrus → pars orbitalis)
        BA 11  rostral medial orbital gyrus — reward valuation
        BA 13  caudal medial orbital gyrus / posterior orbital region
               — visceral and olfactory integration
        BA 14  caudomedial orbital cortex (inconstant in humans; present
               in some parcellations) — interoceptive integration
        BA 47  caudolateral transition to pars orbitalis of the IFG —
               affective valuation / emotion regulation

**This field is byte-identical to the left-hemisphere sibling.** The
Brodmann-area adjacency is numerically symmetric across hemispheres;
the functional annotations above differ (right BA 47 carries affective
valuation rather than the left's semantic retrieval) but the BA numbers
do not.

**A caution about orbital Brodmann boundaries.** On the lateral
convexity, Brodmann boundaries are reasonably crisp and the sulci are
reliable guides to them. On the **orbital surface** they are not: the
BA 11 / 12 / 13 / 14 boundaries are architectonically subtle, vary
across individuals, and do not always coincide with the visible sulci.
The olfactory sulcus is a better guide to the **medial vs lateral
compartment** distinction than to any specific BA boundary within a
compartment. The ``BRODMANN_ADJACENCY`` dict should therefore be read
as "which areas may abut the sulcus somewhere along its length," not as
"which area is on which side at every point."

This is the main reason the olfactory sulcus's BA adjacency is written
as a **set-valued** per-side tuple rather than a single-valued map, and
the reason downstream code must not assume BA 11 is coextensive with the
whole medial bank.

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    rostral end
        Begins at or just behind the **frontal pole**, on the orbital
        surface, where the gyrus rectus and the medial orbital gyrus
        first become distinguishable. The **olfactory bulb** sits in
        this rostral portion of the sulcus; the sulcus is shallowest
        here.

    caudal end
        Terminates in the **posterior orbital region**, near the
        **olfactory trigone** — the point at which the olfactory tract
        divides into the medial and lateral olfactory striae. The
        posterior end lies **more lateral than the rostral end**
        . Caudolaterally, the sulcus's lateral bank transitions
        into the pars orbitalis of the IFG.

**This field is byte-identical to the left-hemisphere sibling.** The
landmarks at each end are hemisphere-invariant.

**A note on the "medial olfactory stria" as a sulcal artefact.** What
has often been called the medial olfactory tract in the human is, in
part, a **gyrus produced by the medial deviation of the olfactory
sulcus** — it separates the neocortex of the gyrus rectus from medially
located tissue in the posterior orbital region. In other
words, the caudal medial bank of the OS is not simply "gyrus rectus
continuing"; it is a distinct transitional fold. This is one of the
reasons the caudal end of the OS is anatomically messier than the
rostral end, and it is why the EXTENT entry names the olfactory trigone
rather than a single gyrus.

--------------------------------------------------------------------------------
VARIANTS (right-hemisphere specific)
--------------------------------------------------------------------------------

Unlike the other frontal sulci, the olfactory sulcus's principal
variation is **depth**, not continuity — it is almost never interrupted
by a bridging gyrus, but it varies substantially in how deep it cuts.
Depth is the clinically load-bearing measurement, and the right OS is
**reliably deeper than the left** in every age band[reference:2].

    standard_depth                majority
        A continuous, smoothly deepening sulcus from the frontal pole
        to the olfactory trigone. Depth increases caudally, reaching
        its maximum in the posterior third.

    normative_depth_18_35         minimum 8.78 mm (right)
        Normative minimum OS depth for the right side in the 18–35 y
        cohort is **8.78 mm**, compared with 7.55 mm on the left
        . This is the largest left–right gap across
        the lifespan; the asymmetry narrows with age.

    normative_depth_36_55         minimum 6.99 mm (right)
        Right-OS normative minimum falls to 6.99 mm at 36–55 y
        (left: 6.47 mm)[reference:3].

    normative_depth_55_plus       minimum 6.19 mm (right)
        Right-OS normative minimum is 6.19 mm above 55 y (left:
        5.28 mm)[reference:4].

    shallow_os                    associated with olfactory dysfunction
        Reduced depth, especially in the posterior third. Shallow OS is
        the morphological signature of **congenital anosmia** and is
        also seen in post-infectious, post-traumatic, and idiopathic
        olfactory loss. **Critically, on the right side, OS depth does
        NOT correlate with measured olfactory function** — the
        functional depth–function relationship is left-lateralized
        . A shallow right OS is therefore a structural
        abnormality that must be interpreted alongside the left OS, not
        in isolation.

    sulcus_fragmentosus           small dimple, inconstant
        A small accessory dimple located **between the olfactory sulcus
        and the medial orbital sulcus**, i.e. within the medial orbital
        gyrus. It is not a variant of the OS itself but a
        neighbouring landmark that must not be mistaken for it on
        imaging.

    sex_difference_in_symmetry    women more symmetric
        Women show a **higher degree of left–right symmetry** in OS
        depth than men, and on the left side women have deeper OS than
        men; the right OS remains the deeper side in both sexes
        . Handedness has no major effect
        (right-handed mean right OS = 11.3 mm, left = 10.6 mm)
        .

These variants are **geometric**, not topological. BOUNDING_GYRI and
BRODMANN_ADJACENCY do not change across them. Depth is recorded in
``VARIANTS`` because it is the variable that downstream olfactory-system
code will actually query — and the right-side depth values are
systematically larger than the left's, which must be encoded rather than
averaged away.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    schizophrenia_right_medial_orbital_sulcus_thinning
        **This is the right-OS anchor par excellence.** Significant
        reductions in cortical thickness of the **right medial orbital
        sulcus (olfactory sulcus)** are observed in schizophrenia
        patients with persistent auditory verbal hallucinations (pAVH)
        compared with both non-AVH patients and healthy controls
        (P < .003, Bonferroni-corrected)[reference:5]. Thinner right OS
        cortex correlates with **more severe olfactory identification
        impairment** (positive correlation with OSIT-J scores)
        [reference:6][reference:7]. The left medial orbital sulcus does
        *not* show this effect at the same significance. This anchor is
        right-only; it has no left-hemisphere counterpart in the
        current literature.

    olfactory_groove_meningioma
        Olfactory groove meningiomas account for roughly **8–13 % of all
        intracranial meningiomas** and about **12 % of basal
        meningiomas**[reference:8][reference:9]. They are usually midline
        but grow asymmetrically; when lateralized, roughly **five are
        left and three are right** in reported surgical series
        [reference:10]. Anosmia is more common on the side of the tumour
        (14/20 in one series), with contralateral normosmia preserved in
        smaller tumours (<3 cm)[reference:11]. The right OS is the
        surgical landmark for the plane between tumour and right gyrus
        rectus.

    congenital_anosmia_and_kallmann_syndrome
        Isolated congenital anosmia is reliably predicted by **shallow
        OS depth**, with no overlap between patients and controls
        . Kallmann syndrome shows the same OS/bulb
        hypoplasia. **On the right, because normative depth is larger
        (8.78 mm vs 7.55 mm), a right OS depth that would be borderline
        on the left is definitively abnormal on the right** — the
        diagnostic threshold must be hemisphere-specific.

    post_infectious_and_post_traumatic_loss
        OS depth is reduced, and olfactory bulb volume falls, in
        post-viral, post-traumatic, and idiopathic olfactory loss.
        The combination of OB volumetry and OS depth provides
        synergistic diagnostic accuracy. Right-OS depth is a
        *structural* rather than *functional* correlate in these
        conditions.

    post_covid_olfactory_loss
        Olfactory bulb atrophy is observed in post-COVID patients, and
        OS depth shows high sensitivity and specificity for
        COVID-associated olfactory disorder. The right OS
        is measured alongside the left in the standard MRI workup, but
        the left remains the functionally informative side.

    chronic_rhinosinusitis_and_migraine
        Both conditions show OB atrophy and reduced OS depth relative to
        controls, alongside post-COVID and idiopathic groups
        . OS depth is a **transdiagnostic**
        structural marker; the right OS contributes the larger
        normative baseline against which pathology is judged.

    epilepsy_associated_olfactory_impairment
        Both temporal and frontal lobe epilepsy are associated with
        decreased OB volume and OS depth, and with measurable olfactory
        impairment. The right OS is a useful secondary measure
        in presurgical epilepsy imaging.

    olfactory_artery_corridor
        The olfactory artery runs within the OS, supplying the tract and
        bulb. Subfrontal approaches that retract the orbital
        surface risk avulsing this artery and devascularizing the
        ipsilateral olfactory tract — a mechanism of **surgical**
        anosmia distinct from direct tract transection. On the right
        side the deeper sulcus provides slightly more working space but
        the same vascular risk.

These anchors are **right-hemisphere-specific**: the schizophrenia
medial-orbital-sulcus finding is right-only; the meningioma laterality
numbers are drawn from series where right-sided tumours are the minority
(3 of 8 lateralized cases); and the diagnostic depth thresholds must use
the right normative values (8.78 / 6.99 / 6.19 mm), not the left's. The
left sibling's docstring carries the left-OS functional-correlation
anchor (r ≈ 0.33) and the left-dominant congenital-anosmia threshold.

--------------------------------------------------------------------------------
CONNECTIVITY (structures within and beneath the sulcus)
--------------------------------------------------------------------------------

The OS is unique among frontal sulci in that its primary "connectivity"
is **physical occupancy**, not sub-sulcal white matter. Both categories
are recorded.

Structures physically within the sulcus:

    olfactory_bulb
        → sits in the rostral portion of the OS
        The bulb receives olfactory receptor neuron axons from the
        olfactory epithelium and is the first central relay. Its volume
        is the single most sensitive MRI marker of olfactory function.
        Right and left bulb volumes are on average equal, even though
        the right OS is deeper[reference:12].

    olfactory_tract
        → runs caudally within the OS
        The tract carries mitral/tufted cell axons from the bulb to the
        olfactory trigone, where it divides into the lateral, medial,
        and intermediate olfactory striae.

    olfactory_artery
        → runs within the OS alongside the tract
        Supplies the tract and bulb. Its intra-sulcal course
        is the reason subfrontal retraction can cause vascular anosmia.

White-matter bundles running beneath the sulcus:

    olfactory_striae (lateral, medial, intermediate)
        → lateral_olfactory_stria:   primary olfactory cortex
                                     (piriform cortex, periamygdaloid
                                     cortex, entorhinal cortex)
        → medial_olfactory_stria:    septal region / medial OFC
        → intermediate_olfactory_stria: olfactory tubercle / ventral
                                     striatum
        These are the principal output pathways of the olfactory system,
        and they pass beneath the caudal OS at the olfactory trigone.

    uncinate_fasciculus (right)
        → traverses_beneath_caudal_os
        → right_anterior_temporal_lobe
        The right uncinate's orbital origin lies beneath the caudal OS,
        connecting the orbital surface to the right anterior temporal
        lobe. On the right it carries **affective and socio-emotional**
        OFC content (rather than the left's semantic / verbal content).

    fronto_orbital_tract / short orbitofrontal U-fibres
        → connects_gyrus_rectus_to_medial_orbital_gyrus
        Short-range fibres cross beneath the OS, coupling the medial
        and lateral orbital compartments. These are the anatomical
        substrate of the OS's role as a *functional* boundary rather
        than an absolute one — the two compartments are coupled, not
        isolated.

    olfactory_radiation (medial forebrain bundle contributions)
        → traverses_beneath_posterior_os
        → hypothalamus / septal nuclei
        Caudal continuations of the olfactory pathway that pass beneath
        the posterior OS en route to limbic and hypothalamic targets.

    amygdala projections (right, via caudal OS / olfactory trigone)
        → right_periamygdaloid_cortex
        → right_corticomedial_amygdala
        The lateral olfactory stria terminates in the right
        periamygdaloid cortex and corticomedial amygdala, passing
        beneath the caudal right OS. The right OFC's coupling to the
        amygdala is denser than the left's, consistent with the
        right-hemisphere's role in affective valuation and emotion
        regulation.

Note the absence of a large dorsal association bundle: unlike the IFS
(arcuate, SLF III) or the precentral sulcus (corticospinal), the OS is
not a landmark for a major intrahemispheric fasciculus. Its
"connectivity" is dominated by the **olfactory pathway itself**, which
is why the OS is best understood as a container rather than a corridor.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri  (FORWARD REFERENCES — see the caveat below)
    The medial bounding gyrus ``gyrus_rectus`` and the lateral bounding
    gyrus ``medial_orbital_gyrus`` are **not yet packages** under
    ``..gyri``. When they are created, each must declare the olfactory
    sulcus as its boundary, and the duality contract will then apply
    fully. Until then, this package's BOUNDING_GYRI names are
    forward-declared strings and the parent ``..sulci`` inversion
    function must tolerate unresolvable gyrus names for this one sulcus
    (see the FORWARD-DECLARATION CAVEAT).

..gyri.inferior_frontal_gyrus
    The pars orbitalis (BA 47) touches the caudolateral end of the OS.
    The right IFG package already declares the **olfactory sulcus** as
    one of its boundaries — this is the one BOUNDING_GYRI entry that
    resolves against an existing package today.

..sulci.orbital_sulcus
    The medial orbital sulcus (a component of the compound
    ``orbital_sulcus``) is the OS's lateral neighbour, with the medial
    orbital gyrus lying between them. The OS and the medial
    orbital sulcus must not be conflated on imaging: the OS is the
    more medial, more constant, and deeper of the two, and it contains
    the olfactory tract.

..sulci.inferior_frontal_sulcus
    The IFS's rostral end often fuses with the lateral orbital sulcus,
    and via that fusion the IFS's rostral terminus lies in the same
    orbital region as the OS's caudolateral terminus. They are distinct
    sulci but share a neighbourhood.

..brodmann_areas.brodmann_area_11
..brodmann_areas.brodmann_area_12
..brodmann_areas.brodmann_area_13
..brodmann_areas.brodmann_area_14
..brodmann_areas.brodmann_area_47
    The five BAs abutting the OS. Each must declare the OS as a
    boundary once the BA packages exist. (Note: these packages are not
    yet modelled in ``frontal/brodmann_areas/``; the forward references
    are reserved so they can be wired up when the BA packages are
    created.)

..cortex.prefrontal_cortex
    The OS separates the medial orbitofrontal cortex (gyrus rectus,
    BA 11/12) from the more lateral orbitofrontal cortex (medial
    orbital gyrus → pars orbitalis, BA 11/13/14/47). On the right,
    the lateral compartment's BA 47 carries **affective valuation and
    emotion regulation** rather than the left's semantic retrieval.
    The prefrontal_cortex package must declare the OS as the **surface
    boundary** between the medial and lateral OFC compartments.

..cortex.primary_motor_cortex  — no relationship
    Unlike the precentral sulcus, the OS is not a motor landmark.
    Recorded here only to pre-empt a false cross-reference.

../../subcortical/medial_temporal_lobe/amygdala
    The lateral olfactory stria terminates in the periamygdaloid cortex
    and the corticomedial amygdala, passing beneath the caudal OS. On
    the right, this projection is **denser** and is the substrate of
    right-OFC-mediated affective valuation and emotion regulation. The
    amygdala package must declare the olfactory trigone / caudal OS as
    one of its afferent corridors, with right-lateralized emphasis.

../../subcortical/medial_temporal_lobe/hippocampus
    The entorhinal cortex (a hippocampal formation structure) receives
    direct olfactory input via the lateral olfactory stria, beneath the
    caudal OS. The hippocampus package must declare this route, and
    must note that it is the shortest cortico-cortical path from a
    sensory organ to the hippocampal formation.

../../brainparts/forebrain/telencephalon/cerebral_hemispheres/right/cortex/frontal/gyri/rhinencephalon (if/when created)
    The rhinencephalon package (olfactory bulb, tract, piriform cortex,
    periamygdaloid cortex, uncus) is the functional home of the
    structures that lie *within* this sulcus. When the rhinencephalon
    package is built out under ``..gyri``, it must cross-reference the
    OS as the anatomical groove that houses its most rostral
    components.

../../left/cortex/frontal/sulci/olfactory_sulcus
    The left-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS) MUST
    be byte-identical to this package. Geometric and clinical fields
    (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED to differ —
    the right OS is deeper (8.78 mm vs 7.55 mm at 18–35 y), right-OS
    depth does *not* correlate with olfactory function, and the right
    medial orbital sulcus carries the schizophrenia
    olfactory-identification finding.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "olfactory_sulcus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to left
                              "medial":  ("gyrus_rectus",
                                          "posterior_orbital_region_"
                                          "medial_aspect"),
                              "lateral": ("medial_orbital_gyrus",
                                          "pars_orbitalis_of_inferior_"
                                          "frontal_gyrus"),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "medial":  (11, 12),
                              "lateral": (11, 13, 14, 47),
                          }

    EXTENT              = {                          # identical to left
                              "rostral": ("frontal_pole",
                                          "olfactory_bulb"),
                              "caudal":  ("olfactory_trigone",
                                          "posterior_orbital_region"),
                          }

    VARIANTS            = (                          # DIFFERS from left
                              "standard_depth_majority",
                              "normative_depth_18_35_minimum_8_78_mm",
                              "normative_depth_36_55_minimum_6_99_mm",
                              "normative_depth_55_plus_minimum_6_19_mm",
                              "shallow_os_structural_marker_not_"
                              "functional_correlate_on_right",
                              "sulcus_fragmentosus_inconstant",
                              "sex_difference_in_symmetry_women_more_"
                              "symmetric",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from left
                              "schizophrenia_right_medial_orbital_"
                              "sulcus_thinning",
                              "olfactory_groove_meningioma",
                              "congenital_anosmia_and_kallmann_syndrome_"
                              "right_specific_threshold",
                              "post_infectious_and_post_traumatic_loss",
                              "post_covid_olfactory_loss",
                              "chronic_rhinosinusitis_and_migraine",
                              "epilepsy_associated_olfactory_impairment",
                              "olfactory_artery_corridor",
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

Note: ``SUBDIVISIONS`` is an empty tuple — the OS is a leaf sulcus. The
field is kept for uniformity with the parent ``..sulci`` contract and
must NOT be deleted; downstream code iterates ``SUBDIVISIONS``
unconditionally.

No behaviour. This package is a declarative descriptor; all computation
that references the OS lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT (unique to this sulcus)
--------------------------------------------------------------------------------

The parent ``..sulci`` docstring states the duality contract as: *every
gyrus named in any BOUNDING_GYRI MUST exist in ``..gyri.GYRI``.* **The
olfactory sulcus is the one sulcus for which this cannot yet hold.**

Of the four gyrus names in this package's BOUNDING_GYRI:

    pars_orbitalis_of_inferior_frontal_gyrus   → resolves today (the
                                                 right IFG package
                                                 exists and declares
                                                 the OS)
    gyrus_rectus                               → forward reference
    posterior_orbital_region_medial_aspect     → forward reference
    medial_orbital_gyrus                       → forward reference

The parent inversion function must therefore be **explicitly
parameterised** to allow unresolvable gyrus names for the
``olfactory_sulcus`` entry, rather than failing loudly. This is a
narrow, documented exception — not a relaxation of the duality
contract for the other five sulci, all of which resolve fully.

**This caveat text is byte-identical to the left sibling's.** Both
hemispheres carry it until the orbital gyri packages are created; the
right side must not silently drop it or implement a different
tolerance policy.

Once the orbital gyri packages (``gyrus_rectus``,
``medial_orbital_gyrus``, and the anterior / lateral / posterior
orbital gyri) are created under ``..gyri``, this caveat must be
removed **from both hemispheres in the same commit** and the duality
test tightened to apply uniformly.

--------------------------------------------------------------------------------
PROMOTION RULE (when a sulcus segment becomes a package)
--------------------------------------------------------------------------------

A sulcus is an **edge**, not a **node**, so the standard promotion rule
does not directly apply. For the olfactory sulcus, two segmentation
schemes are conceivable:

    rostral / caudal split
        A ``pars_rostralis`` (bulbar portion, containing the bulb) and a
        ``pars_caudalis`` (trigonal portion, containing the tract and
        the olfactory trigone). This is the more anatomically natural
        split, because the two portions differ in content (bulb vs
        tract) and in depth profile.

    medial / lateral bank split
        Not recommended. The two banks differ in gyrus (rectus vs
        medial orbital) but splitting a sulcus by *bank* rather than by
        *segment* would create two packages that each describe half a
        groove, which has no anatomical precedent in this tree.

If the rostral / caudal split is adopted:

  1. Add "pars_rostralis" and "pars_caudalis" to ``SUBDIVISIONS``.
  2. Keep ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and ``EXTENT`` at
     the parent level as the union of the segments.
  3. Each segment declares its own restricted versions.
  4. Mirror the split on the left side in the same commit.

**Duality caveat**: the IFG's pars orbitalis declares the OS *as a
whole* as its boundary. A segment split does not create new
gyri-facing partners — the parent remains canonical. This is the same
constraint documented for the inferior frontal sulcus.

**No split should be performed while the FORWARD-DECLARATION CAVEAT is
still in force.** Splitting a sulcus whose bounding gyri do not yet
exist multiplies unresolved references from four to eight and makes the
eventual duality reconciliation substantially harder.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../olfactory_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME          "olfactory_sulcus"
        LOBE                 "frontal"
        BOUNDING_GYRI        the same medial (gyrus rectus) ↔ lateral
                             (medial orbital gyrus / pars orbitalis)
                             boundary
        BRODMANN_ADJACENCY   the same BA 11/12 ↔ BA 11/13/14/47
        EXTENT               the same frontal-pole / olfactory-trigone
                             landmarks
        SUBDIVISIONS         both empty (or both non-empty in the same
                             way, if a segment split is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "right" vs "left"
        VARIANTS             right: deeper in every age band;
                             normative minimum 8.78 mm (18–35 y),
                             6.99 mm (36–55 y), 6.19 mm (>55 y);
                             right-OS depth does NOT correlate with
                             olfactory function; left: shallower;
                             normative minimum 7.55 / 6.47 / 5.28 mm;
                             left-OS depth correlates with function
                             (r ≈ 0.33).
        CLINICAL_ANCHORS     right: **right medial orbital sulcus
                             cortical thinning in schizophrenia with
                             pAVH** (right-only anchor), right-specific
                             congenital-anosmia depth threshold,
                             meningioma laterality (minority of
                             lateralized cases); left: left-OS depth as
                             the functional correlate, left-dominant
                             congenital-anosmia threshold.
        CONNECTIVITY         same bundle and structure names; the right
                             uncinate carries affective /
                             socio-emotional OFC content, the left
                             carries semantic / verbal OFC content;
                             the right amygdala projection from the
                             caudal OS is denser than the left's.

**The depth asymmetry is the single most important entry in this
contract.** The right OS is reliably deeper, but the left OS is the one
whose depth tracks function. Any code that computes "OS depth" must
specify hemisphere, and any diagnostic threshold must use the
hemisphere-specific normative values — averaging left and right OS
depth destroys both the structural asymmetry and the functional signal
[reference:13][reference:14].

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "olfactory_sulcus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BOUNDING_GYRI is byte-identical to the left sibling: medial
    (gyrus_rectus, posterior_orbital_region_medial_aspect), lateral
    (medial_orbital_gyrus, pars_orbitalis_of_inferior_frontal_gyrus).
[ ] BOUNDING_GYRI names gyrus_rectus and medial_orbital_gyrus as the
    primary pair, with pars_orbitalis named only as the caudolateral
    transition.
[ ] BRODMANN_ADJACENCY is byte-identical to the left sibling:
    medial (11, 12), lateral (11, 13, 14, 47).
[ ] EXTENT is byte-identical to the left sibling.
[ ] SUBDIVISIONS is empty and byte-identical to the left sibling.
[ ] VARIANTS documents the RIGHT-hemisphere depth values: 8.78 mm
    (18–35 y), 6.99 mm (36–55 y), 6.19 mm (>55 y), and the absence of
    a right-OS depth–function correlation.
[ ] CLINICAL_ANCHORS contains the right-only anchor
    **schizophrenia_right_medial_orbital_sulcus_thinning**, citing the
    right medial orbital sulcus (olfactory sulcus) cortical thinning in
    pAVH patients and its correlation with OSIT-J impairment
    [reference:15].
[ ] CONNECTIVITY separates the **structures within the sulcus** (bulb,
    tract, artery) from the **bundles beneath it** (olfactory striae,
    right uncinate, short orbitofrontal U-fibres, olfactory radiation,
    right amygdala projection).
[ ] The right uncinate's affective / socio-emotional content is
    documented (contrast with the left's semantic / verbal content).
[ ] The right amygdala projection from the caudal OS is documented as
    denser than the left's.
[ ] The absence of a major dorsal association bundle is documented —
    the OS is a container, not a corridor.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.inferior_frontal_gyrus`` (right) declares the OS as one of
    its boundaries — the one duality link that resolves today.
[ ] The FORWARD-DECLARATION CAVEAT is present and is byte-identical to
    the left sibling's.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    left sibling; depth values, the schizophrenia anchor, the right
    uncinate's content, and the amygdala density deliberately differ.
[ ] Any downstream code computing "OS depth" is required to specify
    hemisphere, and any diagnostic threshold uses the right normative
    values (8.78 / 6.99 / 6.19 mm), not the left's.
"""