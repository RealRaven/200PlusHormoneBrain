"""
Olfactory Sulcus (OS) — Left Hemisphere
========================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
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
``../../right/cortex/frontal/sulci/olfactory_sulcus``. Structural fields
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
alongside them[reference:0]. The sulcus is therefore both a **gyral
boundary** and an **osseous-soft-tissue corridor** — a dual role no
other frontal sulcus has.

A geometric detail that matters for both imaging and surgery: the
**posterior end of the olfactory sulcus lies more lateral than its
anterior end** (Chiavaras & Petrides, 2000)[reference:1]. The sulcus is
therefore not perfectly parasagittal — it diverges laterally as it runs
caudally, tracking the lateral drift of the gyrus rectus.

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

**Two important corrections relative to the parent ``..sulci`` docstring.**

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
[reference:2] — it is present in essentially every brain, with little
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

Interpretation:

    medial (gyrus rectus side)
        BA 11  rostral / lateral gyrus rectus — medial orbitofrontal
               cortex, reward valuation
        BA 12  caudal / medial gyrus rectus — anterior cingulate
               -adjacent medial OFC, visceral / autonomic integration

    lateral (medial orbital gyrus → pars orbitalis)
        BA 11  rostral medial orbital gyrus — reward valuation
        BA 13  caudal medial orbital gyrus / posterior orbital region
               — visceral and olfactory integration
        BA 14  caudomedial orbital cortex (inconstant in humans; present
               in some parcellations) — interoceptive integration
        BA 47  caudolateral transition to pars orbitalis of the IFG —
               semantic retrieval / affective valuation

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
        [reference:3]. Caudolaterally, the sulcus's lateral bank transitions
        into the pars orbitalis of the IFG.

**A note on the "medial olfactory stria" as a sulcal artefact.** What
has often been called the medial olfactory tract in the human is, in
part, a **gyrus produced by the medial deviation of the olfactory
sulcus** — it separates the neocortex of the gyrus rectus from medially
located tissue in the posterior orbital region[reference:4]. In other
words, the caudal medial bank of the OS is not simply "gyrus rectus
continuing"; it is a distinct transitional fold. This is one of the
reasons the caudal end of the OS is anatomically messier than the
rostral end, and it is why the EXTENT entry names the olfactory trigone
rather than a single gyrus.

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

Unlike the other frontal sulci, the olfactory sulcus's principal
variation is **depth**, not continuity — it is almost never interrupted
by a bridging gyrus, but it varies substantially in how deep it cuts.
Depth is the clinically load-bearing measurement.

    standard_depth              majority
        A continuous, smoothly deepening sulcus from the frontal pole
        to the olfactory trigone. Depth increases caudally, reaching
        its maximum in the posterior third.

    shallow_os                  associated with olfactory dysfunction
        Reduced depth, especially in the posterior third. Shallow OS is
        the morphological signature of **congenital anosmia** and is
        also seen in post-infectious, post-traumatic, and idiopathic
        olfactory loss[reference:5][reference:6]. Normative minimum depths
        (18–35 y) are **7.55 mm on the left** and 8.78 mm on the right;
        these minima fall with age (6.47 mm left at 36–55 y; 5.28 mm
        left above 55 y)[reference:7].

    asymmetrically_shallow        more common on the left
        The left OS is, on average, **shallower than the right** across
        all age groups[reference:8][reference:9][reference:10]. Left-OS depth
        is also the side that correlates with measured olfactory
        function (r ≈ 0.33 in healthy males), whereas right-OS depth
        does not[reference:11]. This is one of the few frontal-sulcus
        asymmetries where the **left** is the functionally informative
        side.

    sulcus_fragmentosus         small dimple, inconstant
        A small accessory dimple located **between the olfactory sulcus
        and the medial orbital sulcus**, i.e. within the medial orbital
        gyrus[reference:12]. It is not a variant of the OS itself but a
        neighbouring landmark that must not be mistaken for it on
        imaging.

    deviated_course             rare, usually pathological or
                                maldevelopmental
        Atypical courses have been described in which the OS deviates
        laterally, deviates superiorly into the interhemispheric
        fissure, or is **hypoplastic**[reference:13]. These are reported in
        the context of congenital olfactory disorders and midline
        malformations rather than as normal variants.

    sex_difference_in_symmetry  women more symmetric
        Women show a **higher degree of left–right symmetry** in OS
        depth than men, and on the left side women have deeper OS than
        men[reference:14]. Handedness has no major effect on OS depth
        [reference:15].

These variants are **geometric**, not topological. BOUNDING_GYRI and
BRODMANN_ADJACENCY do not change across them. Depth is recorded in
``VARIANTS`` because it is the variable that downstream olfactory-system
code will actually query.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    olfactory_groove_meningioma
        Olfactory groove meningiomas account for roughly **10 % of all
        intracranial meningiomas** and arise from the cribriform plate
        or the frontosphenoid suture; they are **usually midline** but
        grow asymmetrically and compress the orbital surface on one
        side[reference:16][reference:17]. Because growth is insidious, they are
        often large at presentation, with marked frontal-lobe edema and
        frontal dysfunction[reference:18][reference:19]. The olfactory
        sulcus is the key surface landmark for their dural attachment
        and for the plane between tumour and gyrus rectus.

    congenital_anosmia_and_kallmann_syndrome
        Isolated congenital anosmia is reliably predicted by **shallow
        OS depth** in the plane of the posterior tangent through the
        eyeballs (PPTE), with no overlap in OS depth between patients
        with and without olfactory bulbs/tracts[reference:20]. Kallmann
        syndrome — congenital hypogonadotropic hypogonadism with
        anosmia — shows the same OS/bulb hypoplasia. The OS is
        therefore a **primary radiological criterion** for congenital
        smell loss, not an incidental finding[reference:21].

    post_infectious_and_post_traumatic_loss
        OS depth is reduced, and olfactory bulb volume falls, in
        post-viral, post-traumatic, and idiopathic olfactory loss
        [reference:22]. The combination of OB volumetry and OS depth
        provides "synergistic contributions to the accurate radiological
        diagnosis of smell dysfunction"[reference:23].

    post_covid_olfactory_loss
        Olfactory bulb atrophy is observed in post-COVID patients, and
        OS depth shows high sensitivity and specificity for
        COVID-associated olfactory disorder[reference:24][reference:25]. The
        OS is now part of the standard MRI workup for persistent
        post-COVID anosmia.

    chronic_rhinosinusitis_and_migraine
        Both conditions show OB atrophy and reduced OS depth relative to
        controls, alongside post-COVID and idiopathic groups
        [reference:26][reference:27]. OS depth is thus a **transdiagnostic**
        morphological marker of olfactory system compromise, not a
        disease-specific one.

    epilepsy_associated_olfactory_impairment
        Both temporal and frontal lobe epilepsy are associated with
        decreased OB volume and OS depth, and with measurable olfactory
        impairment[reference:28]. The OS is a useful secondary measure in
        presurgical epilepsy imaging.

    schizophrenia_olfactory_identification
        Thinner cortex at the **right medial orbital sulcus (olfactory
        sulcus)** is associated with more severe olfactory
        identification impairment in schizophrenia patients with
        persistent auditory verbal hallucinations[reference:29]. Note that
        this finding is right-lateralized — it is documented here for
        cross-reference but is *not* a left-OS anchor.

    olfactory_artery_corridor
        The olfactory artery runs within the OS, supplying the tract and
        bulb[reference:30]. Subfrontal approaches that retract the orbital
        surface risk avulsing this artery and devascularizing the
        ipsilateral olfactory tract — a mechanism of **surgical**
        anosmia distinct from direct tract transection.

These anchors are **left-hemisphere-specific** only in the sense that
left-OS depth is the functionally informative measure and left-sided
meningiomas present with the left-hemisphere symptom profile. The
pathology itself is bilateral or midline; the right sibling's docstring
carries the right-lateralized anchors (right-OS depth as the larger
measure, right medial orbital sulcus in schizophrenia).

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

    olfactory_tract
        → runs caudally within the OS
        The tract carries mitral/tufted cell axons from the bulb to the
        olfactory trigone, where it divides into the lateral, medial,
        and intermediate olfactory striae.

    olfactory_artery
        → runs within the OS alongside the tract
        Supplies the tract and bulb[reference:31]. Its intra-sulcal course
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

    uncinate_fasciculus (left)
        → traverses_beneath_caudal_os
        → anterior_temporal_lobe
        The uncinate's orbital origin lies beneath the caudal OS,
        connecting the orbital surface to the anterior temporal lobe.
        On the left it carries the semantic / verbal contribution of
        the OFC.

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
    The IFG package already declares the **olfactory sulcus** as one of
    its boundaries — this is the one BOUNDING_GYRI entry that resolves
    against an existing package today.

..sulci.orbital_sulcus
    The medial orbital sulcus (a component of the compound
    ``orbital_sulcus``) is the OS's lateral neighbour, with the medial
    orbital gyrus lying between them[reference:32]. The OS and the medial
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
    orbital gyrus → pars orbitalis, BA 11/13/14/47). The
    prefrontal_cortex package must declare the OS as the **surface
    boundary** between the medial and lateral OFC compartments.

..cortex.primary_motor_cortex  — no relationship
    Unlike the precentral sulcus, the OS is not a motor landmark.
    Recorded here only to pre-empt a false cross-reference.

../../subcortical/medial_temporal_lobe/amygdala
    The lateral olfactory stria terminates in the periamygdaloid cortex
    and the corticomedial amygdala, passing beneath the caudal OS. The
    amygdala package must declare the olfactory trigone / caudal OS as
    one of its afferent corridors.

../../subcortical/medial_temporal_lobe/hippocampus
    The entorhinal cortex (a hippocampal formation structure) receives
    direct olfactory input via the lateral olfactory stria, beneath the
    caudal OS. The hippocampus package must declare this route, and
    must note that it is the shortest cortico-cortical path from a
    sensory organ to the hippocampal formation.

../../brainparts/forebrain/telencephalon/cerebral_hemispheres/left/cortex/frontal/gyri/rhinencephalon (if/when created)
    The rhinencephalon package (olfactory bulb, tract, piriform cortex,
    periamygdaloid cortex, uncus) is the functional home of the
    structures that lie *within* this sulcus. When the rhinencephalon
    package is built out under ``..gyri``, it must cross-reference the
    OS as the anatomical groove that houses its most rostral
    components.

../../right/cortex/frontal/sulci/olfactory_sulcus
    The right-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS) MUST
    be byte-identical to this package. Geometric and clinical fields
    (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED to differ —
    the right OS is deeper, right-OS depth does *not* correlate with
    olfactory function, and the right medial orbital sulcus carries the
    schizophrenia olfactory-identification finding.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "olfactory_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to right
                              "medial":  ("gyrus_rectus",
                                          "posterior_orbital_region_"
                                          "medial_aspect"),
                              "lateral": ("medial_orbital_gyrus",
                                          "pars_orbitalis_of_inferior_"
                                          "frontal_gyrus"),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "medial":  (11, 12),
                              "lateral": (11, 13, 14, 47),
                          }

    EXTENT              = {                          # identical to right
                              "rostral": ("frontal_pole",
                                          "olfactory_bulb"),
                              "caudal":  ("olfactory_trigone",
                                          "posterior_orbital_region"),
                          }

    VARIANTS            = (                          # DIFFERS from right
                              "standard_depth_majority",
                              "shallow_os_associated_with_olfactory_"
                              "dysfunction",
                              "asymmetrically_shallow_left_more_common",
                              "sulcus_fragmentosus_inconstant",
                              "deviated_course_rare",
                              "sex_difference_in_symmetry_women_more_"
                              "symmetric",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "olfactory_groove_meningioma",
                              "congenital_anosmia_and_kallmann_syndrome",
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
                                                 IFG package exists and
                                                 declares the OS)
    gyrus_rectus                               → forward reference
    posterior_orbital_region_medial_aspect     → forward reference
    medial_orbital_gyrus                       → forward reference

The parent inversion function must therefore be **explicitly
parameterised** to allow unresolvable gyrus names for the
``olfactory_sulcus`` entry, rather than failing loudly. This is a
narrow, documented exception — not a relaxation of the duality
contract for the other five sulci, all of which resolve fully.

Once the orbital gyri packages (``gyrus_rectus``,
``medial_orbital_gyrus``, and the anterior / lateral / posterior
orbital gyri) are created under ``..gyri``, this caveat must be
removed and the duality test tightened to apply uniformly.

**Recommended sequencing**: build out the orbital gyri packages
*before* the right-hemisphere olfactory sulcus, so the right side can be
written without the caveat. If the right side is written first, it must
carry the identical caveat text so the two hemispheres do not diverge in
their handling of unresolved references.

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
  4. Mirror the split on the right side in the same commit.

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

Compared to ``../../right/.../olfactory_sulcus``:

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
        HEMISPHERE           "left" vs "right"
        VARIANTS             left: shallower on average; left-OS depth
                             correlates with olfactory function;
                             women more symmetric with deeper left OS;
                             normative minimum depth 7.55 mm (18–35 y);
                             right: deeper on average; right-OS depth
                             does not correlate with olfactory function;
                             normative minimum depth 8.78 mm (18–35 y).
        CLINICAL_ANCHORS     left: left-OS depth as the functionally
                             informative measure; left-sided olfactory
                             groove meningioma symptom profile;
                             right: right-OS depth as the larger
                             normative measure; **right medial orbital
                             sulcus cortical thickness in
                             schizophrenia** (a right-only anchor).
        CONNECTIVITY         same bundle and structure names; the left
                             uncinate carries semantic / verbal OFC
                             content, the right carries affective /
                             socio-emotional OFC content.

The **depth asymmetry** is the single most important entry in the
symmetry contract for this sulcus: the right OS is reliably deeper, the
left OS is the one whose depth tracks function, and any code that
computes "OS depth" must be explicit about which hemisphere it is
measuring. A downstream function that silently averages left and right
OS depth would destroy the one signal this structure is known to carry.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "olfactory_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BOUNDING_GYRI names gyrus_rectus (medial) and medial_orbital_gyrus
    (lateral) as the primary pair, with pars_orbitalis named only as
    the caudolateral transition — NOT as the primary lateral gyrus.
[ ] The parent ``..sulci`` docstring's ``[IFG ↔ orbital surface]``
    shorthand is corrected to reflect gyrus rectus ↔ medial orbital
    gyrus.
[ ] BRODMANN_ADJACENCY is byte-identical to the right sibling:
    medial (11, 12), lateral (11, 13, 14, 47).
[ ] The BA-boundary caution is documented: orbital BA boundaries are
    architectonically subtle and do not always coincide with visible
    sulci.
[ ] EXTENT records the frontal pole / olfactory bulb rostrally and the
    olfactory trigone / posterior orbital region caudally, and notes
    that the posterior end is more lateral than the anterior end.
[ ] SUBDIVISIONS is empty and byte-identical to the right sibling.
[ ] VARIANTS documents the LEFT-hemisphere depth profile (shallower on
    average; left-OS depth correlates with function; women more
    symmetric; normative minimum 7.55 mm at 18–35 y), and these differ
    from the right sibling's.
[ ] CLINICAL_ANCHORS contains the seven left-specific anchors
    (meningioma, congenital anosmia/Kallmann, post-infectious/traumatic,
    post-COVID, CRS/migraine, epilepsy, olfactory artery corridor).
[ ] CONNECTIVITY separates the **structures within the sulcus** (bulb,
    tract, artery) from the **bundles beneath it** (olfactory striae,
    uncinate, short orbitofrontal U-fibres, olfactory radiation).
[ ] The absence of a major dorsal association bundle is documented —
    the OS is a container, not a corridor.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.inferior_frontal_gyrus`` declares the OS as one of its
    boundaries — the one duality link that resolves today.
[ ] The FORWARD-DECLARATION CAVEAT is present and specifies that the
    parent inversion function must tolerate four unresolvable gyrus
    names for this sulcus only.
[ ] The recommendation to build out the orbital gyri packages before
    the right-hemisphere OS is recorded.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    right sibling; depth profile, clinical anchors, and uncinate content
    deliberately differ.
[ ] Any downstream code computing "OS depth" is required to specify
    hemisphere — averaging left and right would destroy the functional
    signal.
"""