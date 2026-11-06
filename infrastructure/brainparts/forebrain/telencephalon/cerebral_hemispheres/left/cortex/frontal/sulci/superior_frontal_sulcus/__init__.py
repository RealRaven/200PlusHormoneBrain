"""
Superior Frontal Sulcus (SFS) — Left Hemisphere
================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── left
                  └── cortex
                        └── frontal
                              └── sulci
                                    └── superior_frontal_sulcus   ← THIS PACKAGE

This is a **leaf sulcus** package on the **dorsolateral convexity** of
the frontal lobe. It is the **lateral limit of the superior frontal
gyrus** — the major horizontally directed groove that separates the
superior frontal gyrus (dorsal) from the middle frontal gyrus (ventral)
along the dorsolateral frontal cortex.

Parent: ``..sulci`` — sibling to ``inferior_frontal_sulcus``,
``olfactory_sulcus``, ``orbital_sulcus``, ``paracentral_sulcus``, and
``precentral_sulcus``.

This package is the **structural mirror** of
``../../right/cortex/frontal/sulci/superior_frontal_sulcus``. Structural
fields (SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT,
SUBDIVISIONS) are identical by contract; geometric and clinical fields
(VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) diverge by design.

--------------------------------------------------------------------------------
WHAT THE SFS IS
--------------------------------------------------------------------------------

The superior frontal sulcus is a **dorsal, horizontally directed sulcus**
of the frontal lobe. It begins **caudally near the superior precentral
sulcus (SPRS)** and terminates **rostrally near the frontal pole**
[reference:0]. It is therefore the groove that defines the **lateral
limit of the superior frontal gyrus** and the **dorsal limit of the
middle frontal gyrus** on the dorsolateral convexity.

The SFS is **not a reliably continuous sulcus**. In the largest modern
MRI series (100 hemispheres), it was a **continuous sulcus (Type I) in
42 % of hemispheres** and a **discontinuous sulcal complex (Type II) in
58 %**[reference:1]. When discontinuous, it comprises two segments — an
**anterior ramus (SFS-a)** and a **posterior ramus (SFS-p)** — separated
by a pli de passage or a submerged gyral bridge. It also **merges with
neighbouring frontal sulci in the vast majority of cases (92 % of
hemispheres)**[reference:2], most often the superior precentral sulcus
caudally and the accessory superior frontal sulcus near the frontal pole
[reference:3].

The SFS is the surface landmark for the **dorsomedial / dorsolateral
prefrontal boundary** and for the **superior frontal trans-sulcal
corridor** to the lateral ventricle and foramen of Monro[reference:4].
It is explicitly described in the surgical literature as a
**"non-eloquent corridor"** for deep lesions — a route that reaches the
ventricles and internal capsule without traversing primary motor or
language cortex[reference:5].

**Left-hemisphere specificity**: the **posterior ramus (SFS-p) extends
more caudally in the left hemisphere**, whereas the anterior segment
(SFS-a) extends more posteriorly in the right hemisphere[reference:6].
The left SFS is therefore the surface landmark for the **left superior
frontal trans-sulcal corridor**, and its posterior ramus is the segment
that most reliably reaches the precentral region.

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction   Gyrus(es) bounded
    ---------   --------------------------------------------------------
    dorsal      superior_frontal_gyrus
    ventral     middle_frontal_gyrus

The SFS is a **simple, two-sided sulcus** — it separates exactly one
pair of gyri along its entire length. This is the same clean two-sided
configuration as the inferior frontal sulcus, and unlike the compound
orbital sulcus or the multi-gyrus precentral sulcus.

**This field is byte-identical to the right-hemisphere sibling.** The
topology of which gyrus lies dorsal and which ventral to the SFS is
hemisphere-invariant.

**Both bounding gyri already exist as packages under ``..gyri``** —
``superior_frontal_gyrus`` (left) and ``middle_frontal_gyrus`` (left).
Both declare the SFS as one of their boundaries in their own docstrings,
and the duality contract resolves fully for this sulcus. **There is no
forward reference in this package's BOUNDING_GYRI** — a rarity among
the frontal sulci.

--------------------------------------------------------------------------------
BRODMANN ADJACENCY
--------------------------------------------------------------------------------

    Side      Brodmann areas abutting the sulcus
    ------    --------------------------------------------------------
    dorsal    BA 6, BA 8, BA 9
    ventral   BA 6, BA 8, BA 9

Interpretation:

    dorsal (superior frontal gyrus side)
        BA 6   medial / dorsal SFG — supplementary motor area (SMA)
               and pre-SMA on the medial aspect; dorsal premotor
               strip laterally
        BA 8   **area 8B** — the **dysgranular** part of area 8 that
               lies above the SFS on the SFG[reference:7]
        BA 9   dorsal SFG — executive control and task-set
               maintenance

    ventral (middle frontal gyrus side)
        BA 6   premotor strip (caudal MFG)
        BA 8   **area 8A** — the **granular** part of area 8 that lies
               below the SFS on the MFG; implicated in the **higher-
               order cognitive allocation of attention** and in the
               **high-level attentional selection of eye movements**
               [reference:8]
        BA 9   dorsal MFG — task-set maintenance and rule
               representation

**The SFS is the cytoarchitectonic boundary *within* areas 6, 8, and 9,
not between them.** In Brodmann's classic map, the SFS separates the
parts of areas 6, 8, and 9 that lie on the superior frontal gyrus from
those that lie on the middle frontal gyrus[reference:9]. The most
consequential of these internal splits is **area 8A vs area 8B**: 8A
(below the SFS, on the MFG) is **granular** and supports attentional
selection; 8B (above the SFS, on the SFG) is **dysgranular** and is not
the FEF proper[reference:10]. This is why the SFS matters functionally
even though it does not separate two *different* Brodmann numbers — it
separates two *architectonically distinct sub-areas* of the same
number.

**This field is byte-identical to the right-hemisphere sibling.** The
Brodmann-area adjacency is numerically symmetric; the 8A/8B distinction
applies on both sides, though the functional emphasis of 8A differs
(right 8A is more strongly engaged in reorienting to salience).

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    caudal end
        Begins near the **superior precentral sulcus (SPRS)**. The SFS
        **merges with the SPRS in the vast majority of hemispheres** —
        reported at 92 % in one large series[reference:11] and as high as
        95 % in a clinical MRI series[reference:12]. The SFS-SPRS junction
        is one of the **seven reliable signs for identifying the central
        sulcus** on MRI[reference:13].

    rostral end
        Terminates near the **frontal pole**, but **does not reach it**
        in most brains — it is interrupted by the **transverse
        frontopolar gyri and sulci**[reference:14]. It merges with the
        **accessory superior frontal sulcus (ASFS)** near the frontal
        pole in **29 % of hemispheres**[reference:15].

**This field is byte-identical to the right-hemisphere sibling.** The
caudal SPRS junction and the rostral frontopolar interruption are
hemisphere-invariant.

The SFS therefore runs the full anteroposterior extent of the
dorsolateral frontal convexity's dorsal strip — from the SPRS caudally
to the frontopolar region rostrally — but it is a **merging sulcus at
both ends**, not a free-standing groove.

--------------------------------------------------------------------------------
VARIANTS (left-hemisphere specific)
--------------------------------------------------------------------------------

The SFS is one of the **most morphologically variable** sulci in the
frontal lobe. Its principal variants are continuity (Type I vs Type II),
merging behaviour (Subtype a vs b), and the **left-right asymmetry in
segment extent**.

    Type_I_continuous             42 % overall; 24 % of left hemispheres
        The SFS is a **single continuous sulcus** from the SPRS to the
        frontopolar region[reference:16]. On the left this pattern is
        **more common than on the right** (24 % vs 18 %).

    Type_II_discontinuous         58 % overall; 26 % of left hemispheres
        The SFS is a **discontinuous sulcal complex** comprising an
        **anterior ramus (SFS-a)** and a **posterior ramus (SFS-p)**
        [reference:17]. On the left this pattern is **less common than on
        the right** (26 % vs 32 %), i.e. the **right SFS is more often
        discontinuous**.

    Subtype_a_does_not_merge        6 % overall; 4 % of left hemispheres
        The SFS (or SFS complex) is a **distinct sulcus that does not
        merge** with any surrounding frontal sulcus[reference:18].
        Extremely rare.

    Subtype_b_merges                92 % of hemispheres
        The SFS **merges with at least one neighbouring frontal
        sulcus**[reference:19]. This is the overwhelming majority
        pattern on both sides.

    SFS_p_extends_more_caudally_left   left-specific
        The **posterior ramus (SFS-p) extends more caudally in the left
        hemisphere** than in the right[reference:20]. This is the
        single most important left-right geometric asymmetry of the
        SFS, and it means the left SFS-p is the more reliable surface
        guide to the precentral region.

    SFS_a_extends_more_posteriorly_right   right-specific
        The **anterior ramus (SFS-a) extends more posteriorly in the
        right hemisphere**[reference:21]. The mirror of the above
        asymmetry.

    three_segment_configuration     8 % of right, 28 % of left
        A three-segment SFS complex is **more common on the left**
        (28 % vs 8 % on the right)[reference:22], while a four-segment
        complex is rare and left-predominant (4 % left, 0 % right)
        [reference:23].

    hemispheric_congruence         60 % of brains
        In **60 % of brains**, both hemispheres show the **same primary
        morphological pattern** (both Type I or both Type II)
        . In the remaining 40 %, the pattern differs across
        hemispheres — which is why the left and right SFS packages each
        carry their own VARIANTS list.

These variants are **geometric and topological**, not merely metric.
The Type I / Type II distinction changes the **number of grooves**, and
the Subtype a / b distinction changes the **merging relationships**. The
``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` fields must therefore be
read as the **canonical** boundary set, with the understanding that in
atypical patterns one or more boundaries may be absent or fused.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (left-hemisphere specific)
--------------------------------------------------------------------------------

    superior_frontal_trans_sulcal_corridor
        **This is the left-SFS anchor par excellence.** The SFS is a
        **"non-eloquent corridor"** for reaching the **lateral
        ventricle, foramen of Monro, and internal capsule** without
        traversing primary motor or language cortex[reference:25]. The
        **superior frontal trans-sulcal trans-ventricular approach**
        dissects through the SFS as an intrinsic microsurgical corridor
        to the lateral ventricle[reference:26]. The preferred entry point
        (Kassam-Monroy) bisects the distance between the midpupillary
        line and the superior sagittal sinus at approximately **x = 2.3
        cm lateral to the SSS, y ≥ 3.5 cm anterior to the coronal
        suture**[reference:27].

    superior_frontal_sulcus_fcd_epilepsy
        **Focal cortical dysplasia (FCD) related to the SFS** is a
        surgically remediable syndrome of frontal lobe epilepsy with a
        **favorable postoperative seizure outcome**[reference:28]
        [reference:29]. The SFS is the surface landmark for the
        epileptogenic zone, and resective strategies guided by the SFS
        achieve high rates of seizure freedom.

    internal_capsule_cavernoma_corridor
        **Internal capsule cavernomas** — deep, eloquent-area lesions —
        can be approached via frontal craniotomy **through the SFS**
        with curative resection and low morbidity[reference:30]. The
        corridor is safe because the SFS separates the SFG from the
        MFG without crossing primary motor or language cortex.

    superior_frontal_trans_sulcal_ventricular_approach
        The SFS provides a **direct trans-sulcal route to the anterior
        ventricular system**[reference:31]. This is used for
        intraventricular tumors, colloid cysts, and other anterior
        ventricular lesions, and it minimizes cortical transgression
        by entering through the sulcal depth rather than the gyral
        surface.

    central_sulcus_identification_sign
        The **junction of the SFS with the precentral sulcus** is one of
        the **seven reliable signs for identifying the central sulcus**
        on MRI[reference:32]. The SFS is united with the precentral
        sulcus in **95 % of cases**[reference:33], making this junction a
        dependable landmark for distinguishing the precentral from the
        central sulcus.

    tumour_and_fcd_resection_landmark
        Sulci and gyri are the **primary neuroanatomical landmarks used
        during neurosurgical interventions** such as tumour and FCD
        resections[reference:34]. The SFS is a **dependable landmark for
        dividing dorsomedial and dorsolateral prefrontal regions** and
        for guiding gyral entry points while avoiding unintended
        extension toward the precentral region where even small
        cortical injuries can produce motor deficits[reference:35].

These anchors are **left-hemisphere-specific** in emphasis: the left
SFS-p extends more caudally, making it the more reliable guide to the
precentral region on the left; and the left SFS is the corridor of
choice for left-sided ventricular and internal capsule lesions. The
right sibling's docstring carries the right SFS-a posterior extent and
the right-sided surgical emphases.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus)
--------------------------------------------------------------------------------

The SFS is a **corridor-rich** sulcus. Cadaveric dissection and DTI
tractography have divided the SFS corridor into **medial, lateral, and
intervening white-matter segments**[reference:36]:

    medial to SFS
        → U-fibres (short-range cortico-cortical)
        → frontal_aslant_tract (FAT)
        → superior_longitudinal_fasciculus_I (SLF-I)
        → cingulum_bundle
        The medial segment carries the FAT (connecting SFG to the
        inferior frontal gyrus), SLF-I (dorsal attention network),
        and the cingulum (default-mode and memory circuits).

    lateral to SFS
        → U-fibres
        → superior_longitudinal_fasciculus_II (SLF-II)
        → claustrocortical_fibres (CCF)
        → inferior_fronto_occipital_fasciculus (IFOF)
        The lateral segment carries SLF-II (working memory and
        attention), the CCF (claustrum-cortical coupling), and the
        IFOF (ventral visual stream to orbitofrontal cortex).

    intervening fibres
        → frontal_aslant_tract (FAT)
        → corona_radiata
        → claustrocortical_fibres (CCF)
        The intervening segment carries the descending corona radiata
        and crossing FAT and CCF fibres[reference:37].

Additional SFG-level connections documented by DSI-based tractography:

    frontal_aslant_tract (FAT)
        → inferior_frontal_gyrus
        Connects the SFG (especially pre-SMA) to the pars opercularis
        of the IFG. On the left, this is the speech-initiation
        corridor.

    inferior_fronto_occipital_fasciculus (IFOF)
        → cuneus
        → lingual_gyrus
        → superior_parietal_lobule
        Connects the SFG to posterior visual and parietal association
        cortex[reference:38].

    cingulum_bundle
        → precuneus
        → parahippocampal_gyrus / uncus
        Connects the SFG to the default-mode network and to medial
        temporal memory structures[reference:39].

    callosal_fibres
        → contralateral SFG
        Bilateral callosal fibres connect the left and right SFG,
        supporting interhemispheric coordination of executive and
        motor functions[reference:40].

The SFS is therefore the surface landmark for a **layered white-matter
corridor** — medial, lateral, and intervening segments — rather than for
a single dominant fasciculus. This layered organization is what makes
the SFS a **surgical corridor of choice**: the surgeon can choose the
medial, lateral, or intervening trajectory depending on the target and
the tracts to be avoided[reference:41].

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri.superior_frontal_gyrus
    The dorsal bounding gyrus. The left SFG package **already declares
    the SFS as its ventral boundary**. The duality contract resolves
    fully for this link — no forward reference.

..gyri.middle_frontal_gyrus
    The ventral bounding gyrus. The left MFG package **already declares
    the SFS as its dorsal boundary**. The duality contract resolves
    fully for this link — no forward reference.

..sulci.precentral_sulcus
    The caudal neighbour. The SFS **merges with the superior precentral
    sulcus (SPRS) in 92–95 % of hemispheres**[reference:42]
    [reference:43]. The SFS-SPRS junction is a reliable landmark for the
    central sulcus[reference:44]. Both packages must declare this
    junction.

..sulci.inferior_frontal_sulcus
    The parallel sulcus one gyrus ventrally. The IFS separates MFG from
    IFG; the SFS separates SFG from MFG. Together they define the three
    frontal gyri on the lateral convexity[reference:45].

..brodmann_areas.brodmann_area_6
..brodmann_areas.brodmann_area_8
..brodmann_areas.brodmann_area_9
    The three BAs abutting the SFS. Each must declare the SFS as a
    boundary once the BA packages exist. **Special note for BA 8**:
    the SFS separates **area 8A (granular, below the SFS)** from **area
    8B (dysgranular, above the SFS)** — this internal subdivision must
    be represented in the BA 8 package[reference:46].

..cortex.premotor_cortex
    The caudal bank of the SFS includes BA 6 (premotor strip). The
    premotor_cortex package must declare the SFS as a **surface
    landmark** for its dorsal margin.

..cortex.supplementary_motor_cortex
    The medial continuation of the SFG carries the SMA / pre-SMA (BA
    6). The supplementary_motor_cortex package must declare the SFS as
    the **lateral boundary** of the medial BA 6 territory.

..cortex.prefrontal_cortex
    The SFS separates the dorsal SFG (BA 9) from the dorsal MFG (BA 9),
    and the dorsal SFG (BA 8B) from the dorsal MFG (BA 8A). The
    prefrontal_cortex package must declare the SFS as the **surface
    boundary** within the DLPFC.

../../subcortical/basal_ganglia  — indirect
    The corona radiata descends beneath the SFS, adjacent to the basal
    ganglia. No direct basal-ganglia projection originates in the SFS;
    the relationship is via the descending corona radiata[reference:47].

../../subcortical/medial_temporal_lobe/hippocampus
    The cingulum bundle, which runs beneath the SFS, connects to the
    parahippocampal gyrus and uncus[reference:48]. The hippocampus
    package must declare this route.

../../right/cortex/frontal/sulci/superior_frontal_sulcus
    The right-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS) MUST
    be byte-identical to this package. Geometric and clinical fields
    (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED to differ —
    the left SFS-p extends more caudally, the right SFS-a extends more
    posteriorly, and the right SFS is more often discontinuous (Type II
    32 % vs 26 %).

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "superior_frontal_sulcus"
    HEMISPHERE          = "left"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to right
                              "dorsal":  ("superior_frontal_gyrus",),
                              "ventral": ("middle_frontal_gyrus",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to right
                              "dorsal":  (6, 8, 9),
                              "ventral": (6, 8, 9),
                          }

    EXTENT              = {                          # identical to right
                              "caudal":  ("superior_precentral_sulcus",
                                          "precentral_sulcus"),
                              "rostral": ("frontal_pole",
                                          "accessory_superior_frontal_"
                                          "sulcus"),
                          }

    VARIANTS            = (                          # DIFFERS from right
                              "Type_I_continuous_24%_left",
                              "Type_II_discontinuous_26%_left",
                              "Subtype_a_does_not_merge_4%_left",
                              "Subtype_b_merges_92%_overall",
                              "SFS_p_extends_more_caudally_left",
                              "three_segment_configuration_28%_left",
                              "four_segment_configuration_4%_left",
                              "hemispheric_congruence_60%_of_brains",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from right
                              "superior_frontal_trans_sulcal_corridor",
                              "superior_frontal_sulcus_fcd_epilepsy",
                              "internal_capsule_cavernoma_corridor",
                              "superior_frontal_trans_sulcal_ventricular_"
                              "approach",
                              "central_sulcus_identification_sign",
                              "tumour_and_fcd_resection_landmark",
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

Note: ``SUBDIVISIONS`` is an empty tuple — the SFS is a leaf sulcus. The
anterior and posterior rami are **not** sub-packages; they are captured
inside ``VARIANTS`` as morphological descriptors. If a future
parcellation promotes them to sub-packages, see the PROMOTION RULE
below.

No behaviour. This package is a declarative descriptor; all computation
that references the SFS lives in ``cortex/`` or ``memory/``.

--------------------------------------------------------------------------------
FORWARD-DECLARATION CAVEAT
--------------------------------------------------------------------------------

**There is no forward-declaration caveat for this sulcus.** Both
bounding gyri — ``superior_frontal_gyrus`` and
``middle_frontal_gyrus`` — already exist as packages under ``..gyri``
and both declare the SFS as a boundary. The duality contract resolves
fully. This makes the SFS one of only two frontal sulci (with the
inferior frontal sulcus) whose bounding gyri are both fully modelled
today.

--------------------------------------------------------------------------------
PROMOTION RULE (when a sulcus segment becomes a package)
--------------------------------------------------------------------------------

A sulcus is an **edge**, not a **node**, so the standard promotion rule
does not directly apply. For the SFS, the most natural promotion is to
split the **two morphological rami** into sub-packages:

    superior_frontal_sulcus/
        __init__.py
        anterior_ramus/
            __init__.py
        posterior_ramus/
            __init__.py

Then:

  1. Add "anterior_ramus" and "posterior_ramus" to ``SUBDIVISIONS``.
  2. Keep ``BOUNDING_GYRI``, ``BRODMANN_ADJACENCY``, and ``EXTENT`` at
     the parent level as the **union** of the rami.
  3. Each ramus package declares its own restricted versions.
  4. Mirror the promotion on the right side in the same commit.

**Duality caveat**: the superior and middle frontal gyri declare the
SFS *as a whole* as their boundary. A ramus split does not create new
gyri-facing partners — the parent remains canonical. This is the same
constraint documented for the inferior frontal sulcus and the orbital
sulcus.

**The Type I / Type II distinction must be respected**: in Type I
(continuous) hemispheres, there is only one groove and no ramus split
is anatomically meaningful. A ramus split should therefore be applied
only to Type II hemispheres, or the package must carry an explicit
``RAMUS_SPLIT_APPLICABLE = "Type_II_only"`` flag.

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../right/.../superior_frontal_sulcus``:

    MUST be identical (byte-for-byte):
        SULCUS_NAME          "superior_frontal_sulcus"
        LOBE                 "frontal"
        BOUNDING_GYRI        the same SFG ↔ MFG boundary
        BRODMANN_ADJACENCY   the same BA 6/8/9 ↔ BA 6/8/9 adjacency,
                             including the 8A/8B distinction
        EXTENT               the same SPRS / frontopolar landmarks
        SUBDIVISIONS         both empty (or both non-empty in the same
                             way, if a ramus split is ever done)

    MUST differ (and the difference must be documented here):
        HEMISPHERE           "left" vs "right"
        VARIANTS             left: Type I 24 %, Type II 26 %,
                             SFS-p extends more caudally, three-
                             segment 28 %, four-segment 4 %;
                             right: Type I 18 %, Type II 32 %, SFS-a
                             extends more posteriorly, three-segment
                             8 %, four-segment 0 %.
        CLINICAL_ANCHORS     left: left superior frontal trans-sulcal
                             corridor, left internal capsule cavernoma
                             corridor, left FCD epilepsy; right: right
                             trans-sulcal corridor, right cavernoma
                             corridor, right FCD epilepsy.
        CONNECTIVITY         same bundle names (FAT, SLF-I, SLF-II,
                             cingulum, IFOF, CCF, callosal); the left
                             FAT carries speech-initiation content,
                             the right carries prosody / inhibition
                             content.

**The SFS-p caudal extent asymmetry is the single most important entry
in this contract.** The left posterior ramus extends more caudally than
the right's[reference:49]. Any downstream code that uses the SFS-p as a
surface guide to the precentral region must specify hemisphere — the
left SFS-p reaches further caudally and is the more reliable landmark
on that side.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "superior_frontal_sulcus".
[ ] HEMISPHERE is "left".
[ ] LOBE is "frontal".
[ ] BOUNDING_GYRI is **simple two-sided**: dorsal
    (superior_frontal_gyrus,), ventral (middle_frontal_gyrus,).
[ ] Both bounding gyri already exist as packages under ``..gyri`` and
    declare the SFS as a boundary — **no forward reference**.
[ ] BRODMANN_ADJACENCY is set-valued per side and includes the
    **8A / 8B distinction**: the SFS separates granular 8A (below,
    MFG) from dysgranular 8B (above, SFG)[reference:50].
[ ] EXTENT records the caudal **SPRS junction (92–95 % merge rate)**
    and the rostral **frontopolar interruption / ASFS merge (29 %)**
    [reference:51][reference:52].
[ ] SUBDIVISIONS is empty and byte-identical to the right sibling.
[ ] VARIANTS documents Type I (42 % overall, 24 % left) and Type II
    (58 % overall, 26 % left)[reference:53], Subtype a (6 % overall,
    4 % left) and Subtype b (92 % merge)[reference:54][reference:55].
[ ] VARIANTS documents the **left-specific** entries: SFS-p extends
    more caudally, three-segment 28 %, four-segment 4 %.
[ ] VARIANTS documents the **right-specific** entries: SFS-a extends
    more posteriorly, Type II 32 %, three-segment 8 %,
    four-segment 0 %[reference:56][reference:57].
[ ] VARIANTS documents hemispheric congruence (60 % of brains)
    .
[ ] CLINICAL_ANCHORS contains the six left-specific anchors:
    superior_frontal_trans_sulcal_corridor, superior_frontal_sulcus_
    fcd_epilepsy, internal_capsule_cavernoma_corridor,
    superior_frontal_trans_sulcal_ventricular_approach,
    central_sulcus_identification_sign, tumour_and_fcd_resection_
    landmark.
[ ] CONNECTIVITY separates the **medial** (U-fibres, FAT, SLF-I,
    cingulum), **lateral** (U-fibres, SLF-II, CCF, IFOF), and
    **intervening** (FAT, corona radiata, CCF) segments
    [reference:59].
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.superior_frontal_gyrus`` and
    ``..gyri.middle_frontal_gyrus`` both declare the SFS as a boundary
    — the duality contract passes fully.
[ ] No SUBDIVISIONS promotion is performed without mirroring on the
    right and without a Type I / Type II applicability flag.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    right sibling; the SFS-p / SFS-a extent asymmetry, Type I/II
    frequencies, segment counts, and surgical emphasis deliberately
    differ.
[ ] Any downstream code using the SFS-p as a precentral landmark is
    required to specify hemisphere — the left SFS-p extends further
    caudally.
"""