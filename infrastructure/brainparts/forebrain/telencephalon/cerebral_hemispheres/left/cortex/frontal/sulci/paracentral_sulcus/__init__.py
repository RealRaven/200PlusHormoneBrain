"""
Paracentral Sulcus (PaCS) — Left Hemisphere
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
                                    └── paracentral_sulcus   ← THIS PACKAGE

This is a **leaf sulcus** package on the **medial surface** of the
hemisphere. Unlike every other sulcus in ``..sulci``, which lives on the
lateral or orbital convexity, the paracentral sulcus is visible only in
midsagittal section. It is the **anterior margin of the paracentral
lobule** — the vertical groove that separates the medial frontal gyrus
(the medial continuation of the superior frontal gyrus) from the
paracentral lobule[reference:0].

Parent: ``..sulci`` — sibling to ``inferior_frontal_sulcus``,
``olfactory_sulcus``, ``orbital_sulcus``, ``precentral_sulcus``, and
``superior_frontal_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/frontal/sulci/paracentral_sulcus``. Structural
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
medial wall as the paracentral sulcus[reference:1]. Its caudal
counterpart is the **marginal sulcus** (the upturned posterior end of
the cingulate sulcus), which forms the posterior boundary of the
paracentral lobule[reference:2].

The sulcus is therefore the **rostral boundary of the paracentral
lobule** and the **caudal boundary of the medial frontal gyrus**. It is
one of the three sulci that frame the paracentral lobule (the others
being the marginal sulcus caudally and the cingulate sulcus ventrally).

Two anatomical cautions are load-bearing:

1. **The paracentral fossa is not the paracentral sulcus.** A shallow
   dimple within the paracentral lobule — the *paracentral fossa
   (pacf)* — is sometimes mistaken for the sulcus on imaging. The
   fossa is a dimple; the sulcus is the anterior border of the
   lobule[reference:3].

2. **The paracentral sulcus is not the marginal sulcus.** The marginal
   sulcus is the *posterior* boundary of the paracentral lobule; the
   paracentral sulcus is the *anterior* boundary. Confusing the two
   reverses the rostrocaudal orientation of the entire medial
   sensorimotor strip.

**Left-hemisphere specificity**: the left paracentral lobule is
**significantly larger** than the right — extrasulcal surface area
approximately **10.22 cm² on the left vs 8.36 cm² on the right**
[reference:4][reference:5]. The left PCL also shows **greater activation
during knee movement** and during **saccadic eye movements** than the
right[reference:6]. This asymmetry is consistent with left-hemisphere
dominance for skilled motor control in the ~90–95 % right-handed
majority[reference:7].

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

Interpretation:

    rostral (medial frontal gyrus side)
        BA 6   medial aspect of the superior frontal gyrus —
               supplementary motor area (SMA) and pre-supplementary
               motor area (pre-SMA). Self-initiated movement,
               motor-sequence planning, and action readiness.

    caudal (paracentral lobule side)
        BA 4   anterior portion of the PCL — medial primary motor
               cortex for the **contralateral leg, foot, and
               perineum**[reference:8]. The cortical centre of
               micturition and defecation control[reference:9].
        BA 3   postcentral strip — primary somatosensory cortex for
               the contralateral leg and foot[reference:10].
        BA 1   postcentral strip — somatosensory association.
        BA 2   postcentral strip — deep-tissue sensation.
        BA 5   inferior portion of the PCL — somatosensory
               association and goal-oriented limb movement
               [reference:11].

The paracentral sulcus therefore separates the **medial premotor /
supplementary motor** cortex (BA 6) from the **medial primary
sensorimotor strip** (BA 4 + BA 3/1/2) and its inferior association
extension (BA 5). It is the surface landmark for the boundary between
the **SMA / pre-SMA** and the **leg / foot / perineum representation**
of the primary sensorimotor cortex.

The **central sulcus** — the boundary between BA 4 and BA 3 — is often
**not visible on the medial surface**, so the paracentral sulcus is
one of the few reliable surface guides to the cytoarchitectonic
transition from motor to sensory cortex in the medial wall
[reference:12].

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    dorsal end
        Reaches the **superior hemispheric border**, where the
        paracentral sulcus is continuous with the **precentral
        sulcus** on the lateral convexity. The precentral sulcus
        turns medially over the dorsal edge and becomes the
        paracentral sulcus[reference:13].

    ventral end
        Approaches the **cingulate sulcus** (or the medial
        frontal gyrus's inferior limit). The paracentral sulcus
        does not always reach the cingulate sulcus; in many
        hemispheres it fades before doing so, leaving the medial
        frontal gyrus and the paracentral lobule in continuity
        ventrally.

The paracentral sulcus is therefore a **short sulcus with one fixed
end (dorsal) and one variable end (ventral)**. Its dorsal continuity
with the precentral sulcus is the reliable landmark; its ventral
extent is variable.

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

The paracentral sulcus is one of the **less consistently present**
frontal sulci. Its principal variant is presence/absence, followed by
continuity and the morphology of the paracentral lobule it borders.

    present_as_a_distinct_sulcus      ~50 %
        The paracentral sulcus was identified as a distinct sulcus
        in **50 % of examined hemispheres** in the largest
        anatomical series. In the other half, the
        boundary between the medial frontal gyrus and the
        paracentral lobule is not marked by a distinct sulcus.

    absent_or_indistinct              ~50 %
        When absent, the medial frontal gyrus and the paracentral
        lobule are in continuity, and the boundary must be
        inferred from the intercommissural line or from
        cytoarchitectonic criteria[reference:15]. This is the single
        most important variant for imaging and surgery — the
        surgeon cannot assume the sulcus will be present.

    continuous_pcl_type               ~2 %
        The paracentral lobule is a single continuous strip with
        no internal segmentation. The paracentral sulcus is
        present as a clean anterior boundary[reference:16].

    partially_segmented_pcl_type      ~91 %
        The paracentral lobule is partially segmented by an
        upturned branch of the cingulate sulcus, but the
        constituent gyri remain in continuity for most of the
        lobule's extent. This is the **dominant morphology**
        [reference:17].

    completely_segmented_pcl_type     ~7 %
        The paracentral lobule is completely segmented, often with
        a short **transitional lobulo-limbic gyrus (LLTG)**
        interposed between the PCL proper and the cingulate
        gyrus[reference:18]. The LLTG is present in
        13–37 % of hemispheres depending on the series
        [reference:19].

    left_pcl_larger                   ~consistent finding
        The left paracentral lobule's extrasulcal surface is
        significantly larger than the right's — 10.22 cm² vs
        8.36 cm² in one series, 10.67 vs 8.80 cm² in males and
        8.80 vs 6.99 cm² in females in another[reference:20]
        [reference:21]. The left PCL also shows stronger activation
        during knee movement and saccades[reference:22].

These variants are **geometric and presence/absence**, not
topological. When the sulcus is present, BOUNDING_GYRI and
BRODMANN_ADJACENCY hold as declared. When absent, the boundary exists
cytoarchitectonically but not as a visible groove — downstream code
must therefore treat ``SULCUS_PRESENT_FRACTION ≈ 0.50`` as a
first-class field.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    leg_foot_perineum_motor_representation
        The **left** paracentral lobule contains the medial primary
        motor representation of the **contralateral (right) leg,
        foot, and perineum**[reference:23][reference:24]. Damage to
        the left PCL produces **right leg weakness**, right foot
        drop, and — when the perineal representation is involved —
        **urinary and faecal incontinence**. This is the
        left-hemisphere anchor par excellence; the right PCL
        carries the left leg and foot.

    micturition_and_defecation_control
        The paracentral lobule is the **cortical centre of
        micturition and defecation**[reference:25]. Its role in
        bladder and anal sphincter control is well documented, and
        PCL lesions produce urgency, incontinence, or retention.
        The left PCL's larger surface area may give it a
        proportionally larger role in these functions, though this
        has not been definitively lateralized.

    central_region_epilepsy
        The paracentral lobule is part of the **central region**
        (with the precentral and postcentral gyri) from which
        **central region epilepsy** arises[reference:26]. Seizures
        beginning in the left PCL produce focal motor seizures of
        the right leg, often with a **Jacksonian march** from foot
        to leg to face, and sometimes with versive head/eye
        deviation. The paracentral sulcus is the surgical landmark
        for the anterior margin of the epileptogenic zone in
        medial frontal / paracentral epilepsy.

    paracentral_cavernomas
        Cavernomas in the paracentral area present most often with
        **epileptic seizures**[reference:27]. The **transsulcal
        approach** through the paracentral sulcus — supported by
        navigation-guided neurophysiological monitoring — is the
        surgical strategy for resecting these lesions while
        preserving the leg motor cortex[reference:28]. The sulcus
        is the corridor, not just the landmark.

    focal_cortical_dysplasia_type_2
        Focal cortical dysplasia type 2 in the central region —
        including the paracentral lobule — can be resected with
        **excellent seizure outcome and low rates of major
        permanent disability**[reference:29]. The left PCL's larger
        surface makes it a proportionally larger target for
        dysplasia surgery, and the paracentral sulcus is the
        anterior limit of the resection.

    presurgical_depth_electrode_planning
        Identification of the central region (central sulcus,
        paracentral lobule) on MRI and angiography is necessary
        before **stereotactic biopsies, depth electrode recordings,
        and resection of centrally located tumours**[reference:30].
        The paracentral sulcus is one of the two medial landmarks
        (with the marginal sulcus) for the paracentral lobule in
        these procedures.

These anchors are **left-hemisphere-specific** in two respects: (a)
the left PCL carries the **right** leg/foot/perineum representation,
and left PCL lesions produce right-sided deficits; (b) the left PCL's
larger surface area makes it the more prominent surgical target. The
right sibling's docstring carries the left leg/foot representation and
the right-sided surgical emphases.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath and around the sulcus)
--------------------------------------------------------------------------------

    paracentral_lobule_tract (intrinsic U-fibres)
        → connects_medial_frontal_gyrus_to_paracentral_lobule
        → connects_anterior_pcl_to_posterior_pcl
        Short-range U-fibres run beneath the paracentral sulcus,
        coupling the medial frontal gyrus (BA 6 / SMA) to the
        anterior PCL (BA 4) and coupling the anterior and
        posterior portions of the PCL to each other[reference:31].
        These are the anatomical substrate of the SMA–M1
        interaction that supports self-initiated leg movement.

    corticospinal_tract (via medial BA 4)
        → descends_through_posterior_limb_of_internal_capsule
        → cerebral_peduncle
        → spinal_cord (contralateral, leg / foot / perineal motor
          neurons)
        The medial BA 4 component of the paracentral lobule
        contributes to the **corticospinal tract** that controls
        the contralateral leg and foot. The fibres descend through
        the posterior limb of the internal capsule and the
        cerebral peduncle to the brainstem[reference:32]. Damage
        anywhere along this route produces the same leg weakness
        as PCL damage.

    thalamocortical_projections
        → left_ventral_posterior_lateral_nucleus (VPL)
        → left_ventral_lateral_nucleus (VL)
        Thalamocortical tracts run medial to the pyramidal
        projections and enter the thalamus[reference:33]. The VPL
        relays leg/foot somatosensory input to the postcentral
        PCL; the VL relays cerebellar and basal-ganglia input to
        the precentral PCL.

    corpus_callosum (body)
        → right_paracentral_lobule
        Contralateral connections course through the **body of the
        corpus callosum** to the homotopic right PCL
        [reference:34]. These connections coordinate the two legs in
        bimanual (bipedal) tasks and in axial/truncal control.
        The left PCL's larger surface area suggests a
        proportionally larger callosal contribution.

    cingulate_connections
        → left_anterior_cingulate
        → left_posterior_cingulate
        Local short association fibres connect the paracentral
        lobule to the cingulate cortex, and specific PCL
        parcellations have direct cingulate connections
        [reference:35]. These fibres support the affective–motor
        interface (e.g. the urgency of micturition) and the
        cingulate's role in pain affect and error monitoring
        adjacent to the leg motor area.

    superior_longitudinal_fasciculus (medial components)
        → left_superior_parietal_lobule
        → left_precuneus
        Medial SLF components connect the PCL to the superior
        parietal lobule and precuneus, supporting the
        sensorimotor–spatial interface for lower-limb navigation
        and postural control.

    medial_forebrain_bundle / septal connections
        → traverses_beneath_ventral_paracentral_sulcus
        → septal_nuclei
        Ventral continuations of the medial frontal pathways
        pass beneath the inferior limit of the paracentral
        sulcus toward the septal region. These are minor but
        relevant to the PCL's autonomic (micturition) role.

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
    superior frontal gyrus. The left SFG package already exists and
    carries BA 6 (SMA / pre-SMA) in its ``BRODMANN_AREAS``. When the
    medial frontal gyrus is promoted to its own package, it should be
    cross-referenced from the SFG package as the medial BA 6
    extension.

..sulci.precentral_sulcus
    The paracentral sulcus is the **medial continuation** of the
    precentral sulcus. The two sulci are continuous over the dorsal
    edge of the hemisphere: the precentral sulcus turns medially and
    becomes the paracentral sulcus[reference:36]. The precentral
    sulcus package must declare this continuity.

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
    boundary once the BA packages exist. (Note: these packages are
    not yet modelled in ``frontal/brodmann_areas/``; the forward
    references are reserved so they can be wired up when the BA
    packages are created.)

..cortex.supplementary_motor_cortex
    The rostral bank of the paracentral sulcus is the medial BA 6
    territory — the **SMA / pre-SMA**. The supplementary_motor_cortex
    package must declare the paracentral sulcus as the **caudal
    boundary** of the SMA's medial extent.

..cortex.primary_motor_cortex
    The caudal bank of the paracentral sulcus is the **medial BA 4**
    territory — the leg / foot / perineum representation of the
    primary motor cortex. The primary_motor_cortex package must
    declare the paracentral sulcus as the **rostral boundary** of the
    medial M1 strip.

..cortex.primary_somatosensory_cortex (if/when created)
    The posterior portion of the paracentral lobule contains BA 3, 1,
    and 2 — the medial primary somatosensory representation of the
    leg and foot. The somatosensory package must declare the
    paracentral sulcus as the **rostral boundary** of the medial S1
    strip.

../../subcortical/basal_ganglia  — indirect
    The corticospinal fibres from medial BA 4 descend through the
    posterior limb of the internal capsule, adjacent to the basal
    ganglia. No direct basal-ganglia projection originates in the
    PCL; the relationship is via the corticospinal tract.

../../subcortical/medial_temporal_lobe/hippocampus
    The cingulate connections from the PCL run adjacent to the
    parahippocampal gyrus but do not terminate there. No direct
    hippocampal projection originates in the PCL. Recorded here
    only to pre-empt a false cross-reference.

../../right/cortex/frontal/sulci/paracentral_sulcus
    The right-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS)
    MUST be byte-identical to this package. Geometric and clinical
    fields (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED
    to differ — the right PCL is smaller, carries the **left**
    leg/foot representation, and has proportionally less callosal
    and corticospinal volume from the medial BA 4 strip.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "paracentral_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to right
                              "rostral": ("medial_frontal_gyrus",),
                              "caudal":  ("paracentral_lobule",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "rostral": (6,),
                              "caudal":  (4, 3, 1, 2, 5),
                          }

    EXTENT              = {                          # identical to right
                              "dorsal":  ("superior_hemispheric_border",
                                          "precentral_sulcus"),
                              "ventral": ("cingulate_sulcus",
                                          "medial_frontal_gyrus"),
                          }

    VARIANTS            = (                          # DIFFERS from right
                              "present_as_distinct_sulcus_~50%",
                              "absent_or_indistinct_~50%",
                              "continuous_pcl_type_~2%",
                              "partially_segmented_pcl_type_~91%",
                              "completely_segmented_pcl_type_~7%",
                              "left_pcl_larger_10_22_vs_8_36_cm2",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "leg_foot_perineum_motor_"
                              "representation_right_side",
                              "micturition_and_defecation_control",
                              "central_region_epilepsy",
                              "paracentral_cavernomas",
                              "focal_cortical_dysplasia_type_2",
                              "presurgical_depth_electrode_planning",
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

**The paracentral lobule is the more consequential of the two forward
references.** It is the target of the sulcus's entire clinical
rationale — epilepsy surgery, cavernoma resection, dysplasia surgery,
and depth-electrode planning all depend on the PCL. The orbital gyri
and the medial frontal gyrus are important, but the PCL is the
*raison d'être* of this sulcus package. The PCL package should therefore
be built out **before** the right-hemisphere paracentral sulcus is
written, so that the right side can be authored without the same
unresolved-reference burden.

If the right side is written first, it must carry the identical caveat
text — the two hemispheres must not diverge in their handling of
unresolved references.

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
  4. Mirror the split on the right side in the same commit.

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

Compared to ``../../right/.../paracentral_sulcus``:

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
        HEMISPHERE           "left" vs "right"
        VARIANTS             left: PCL larger (10.22 vs 8.36 cm²;
                             greater knee and saccade activation);
                             right: PCL smaller; the same
                             present/absent (~50/50) and PCL
                             morphological type frequencies are
                             expected on both sides but the surface-
                             area asymmetry is left-larger.
        CLINICAL_ANCHORS     left: **right leg/foot/perineum**
                             representation; left PCL lesions
                             produce right-sided deficits; larger
                             surgical target; right: **left**
                             leg/foot/perineum representation;
                             right PCL lesions produce left-sided
                             deficits; smaller surgical target.
        CONNECTIVITY         same bundle names; left corticospinal
                             and callosal contributions from medial
                             BA 4 are proportionally larger,
                             consistent with the larger left PCL
                             surface area.

**The surface-area asymmetry is the single most important entry in this
contract.** The left PCL is reliably larger, carries the right leg/foot
representation, and shows stronger activation during knee movement and
saccades. Any downstream code that computes "PCL volume" or "leg motor
representation size" must specify hemisphere — averaging left and right
PCL would erase the asymmetry that is the anatomical signature of
left-hemisphere motor dominance.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "paracentral_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BOUNDING_GYRI names ``medial_frontal_gyrus`` (rostral) and
    ``paracentral_lobule`` (caudal) as the two bounding gyri.
[ ] Both bounding gyri are documented as forward references under
    ``..gyri``.
[ ] BRODMANN_ADJACENCY is byte-identical to the right sibling:
    rostral (6,), caudal (4, 3, 1, 2, 5).
[ ] EXTENT records the dorsal continuity with the **precentral
    sulcus** at the superior hemispheric border, and the ventral
    approach to the **cingulate sulcus**.
[ ] The paracentral fossa (pacf) is explicitly distinguished from the
    paracentral sulcus (pacs)[reference:37].
[ ] The marginal sulcus is explicitly distinguished from the
    paracentral sulcus (posterior vs anterior boundary of the PCL)
    [reference:38].
[ ] SUBDIVISIONS is empty and byte-identical to the right sibling.
[ ] VARIANTS documents the **~50 % presence rate** of the sulcus
     and the PCL morphological types (continuous ~2 %,
    partially segmented ~91 %, completely segmented ~7 %)
    [reference:40].
[ ] VARIANTS documents the **left PCL larger** finding (10.22 vs
    8.36 cm²) and the greater knee/saccade activation on the left
    [reference:41].
[ ] CLINICAL_ANCHORS contains the six left-specific anchors:
    right-leg/foot/perineum representation, micturition/defecation
    control, central-region epilepsy, paracentral cavernomas, focal
    cortical dysplasia type 2, presurgical depth-electrode planning.
[ ] CONNECTIVITY separates the **intrinsic U-fibres** (paracentral
    lobule tract) from the **descending** (corticospinal,
    thalamocortical), **crossing** (corpus callosum body), and
    **adjacent** (cingulate, SLF) bundles.
[ ] The absence of a single dominant dorsal association bundle is
    documented — the PaCS is a distributed white-matter landmark.
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] The FORWARD-DECLARATION CAVEAT is present and specifies that
    **both** bounding gyri are unresolvable.
[ ] The recommendation to build out the paracentral lobule package
    before the right-hemisphere PaCS is recorded.
[ ] No SUBDIVISIONS promotion is performed while the caveat is in
    force.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    right sibling; the PCL surface-area asymmetry, the leg/foot
    laterality, and the proportionally larger left corticospinal and
    callosal contributions deliberately differ.
[ ] Any downstream code computing "PCL volume" or "leg motor
    representation size" is required to specify hemisphere — averaging
    left and right would erase the anatomical signature of left
    motor dominance.
"""