"""
Superior Frontal Sulcus (SFS) — Right Hemisphere
=================================================

Hierarchical location
---------------------
::

    telencephalon
      └── cerebral_hemispheres
            └── right
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
``../../left/cortex/frontal/sulci/superior_frontal_sulcus``. Structural
fields (SULCUS_NAME, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT,
SUBDIVISIONS) are identical by contract; geometric and clinical fields
(VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) diverge by design.

--------------------------------------------------------------------------------
WHAT THE SFS IS
--------------------------------------------------------------------------------

The superior frontal sulcus is a **dorsal, horizontally directed sulcus**
of the frontal lobe. It begins **caudally near the superior precentral
sulcus (SPRS)** and terminates **rostrally near the frontal pole**
. It is therefore the groove that defines the **lateral
limit of the superior frontal gyrus** and the **dorsal limit of the
middle frontal gyrus** on the dorsolateral convexity.

The SFS is **not a reliably continuous sulcus**. In the largest modern
MRI series (100 hemispheres), it was a **continuous sulcus (Type I) in
42 % of hemispheres** and a **discontinuous sulcal complex (Type II) in
58 %**[reference:1]. When discontinuous, it comprises two segments — an
**anterior ramus (SFS-a)** and a **posterior ramus (SFS-p)** — separated
by a pli de passage or a submerged gyral bridge. It also **merges with
neighbouring frontal sulci in the vast majority of cases (92 % of
hemispheres)**, most often the superior precentral sulcus caudally and
the accessory superior frontal sulcus near the frontal pole
[reference:2].

The SFS is the surface landmark for the **dorsomedial / dorsolateral
prefrontal boundary** and for the **superior frontal trans-sulcal
corridor** to the lateral ventricle and foramen of Monro
[reference:3]. It is explicitly described in the surgical literature as a
**"non-eloquent corridor"** for deep lesions — a route that reaches the
ventricles and internal capsule without traversing primary motor or
language cortex [reference:4].

**Right-hemisphere specificity**: the **anterior ramus (SFS-a) extends
more posteriorly in the right hemisphere**, whereas the posterior ramus
(SFS-p) extends more caudally in the left [reference:5][reference:6].
This asymmetry is thought to reflect **Yakovlevian anti-clockwise
torque** — the expansion of left-hemisphere language cortex along the
Sylvian fissure pushes right-hemisphere structures rightward and
anteriorly [reference:7]. The right SFS is therefore the surface landmark
for the **right superior frontal trans-sulcal corridor**, and its
anterior ramus is the segment that most reliably reaches the precentral
region on this side.

--------------------------------------------------------------------------------
BOUNDING GYRI
--------------------------------------------------------------------------------

    Direction   Gyrus(es) bounded
    ---------   --------------------------------------------------------
    dorsal      superior_frontal_gyrus
    ventral     middle_frontal_gyrus

**This field is byte-identical to the left-hemisphere sibling.** The
topology of which gyrus lies dorsal and which ventral to the SFS is
hemisphere-invariant.

**Both bounding gyri already exist as packages under ``..gyri``** —
``superior_frontal_gyrus`` (right) and ``middle_frontal_gyrus`` (right).
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

Interpretation (right-hemisphere functional annotations):

    dorsal (superior frontal gyrus side)
        BA 6   medial / dorsal SFG — supplementary motor area (SMA)
               and pre-SMA on the medial aspect. On the right, the
               SMA contributes to **left-hand** motor planning and
               bimanual coordination support.
        BA 8   **area 8B** — the **dysgranular** part of area 8 that
               lies above the SFS on the SFG .
        BA 9   dorsal SFG — executive control and task-set
               maintenance.

    ventral (middle frontal gyrus side)
        BA 6   premotor strip (caudal MFG) — spatial action
               preparation.
        BA 8   **area 8A** — the **granular** part of area 8 that lies
               below the SFS on the MFG . On the right,
               area 8A is the cortical substrate of the **ventral
               attention network's reorienting function** — the
               stimulus-driven "circuit breaker" that shifts attention
               to salient events.
        BA 9   dorsal MFG — spatial task-set maintenance.

**This field is byte-identical to the left-hemisphere sibling.** The
Brodmann-area adjacency is numerically symmetric; the **8A / 8B
distinction** applies on both sides [reference:10]. What differs is the
**functional emphasis** of 8A: on the right, 8A is the granular node of
the **right-lateralized ventral attention network**, more strongly
engaged in reorienting to salience than its left counterpart.

**The SFS is the cytoarchitectonic boundary *within* areas 6, 8, and 9,
not between them.** In Brodmann's classic map, the SFS separates the
parts of areas 6, 8, and 9 that lie on the superior frontal gyrus from
those that lie on the middle frontal gyrus. The most consequential of
these internal splits is **area 8A (granular, MFG side) vs area 8B
(dysgranular, SFG side)** — 8A is the attentional-selection cortex, 8B
is not the FEF proper [reference:11].

--------------------------------------------------------------------------------
EXTENT (landmarks at each end)
--------------------------------------------------------------------------------

    caudal end
        Begins near the **superior precentral sulcus (SPRS)**. The SFS
        **merges with the SPRS in the vast majority of hemispheres**
        — reported at 92 % in one large series [reference:13]. The
        SFS-SPRS junction is one of the **seven reliable signs for
        identifying the central sulcus** on MRI.

    rostral end
        Terminates near the **frontal pole**, but **does not reach it**
        in most brains — it is interrupted by the **transverse
        frontopolar gyri and sulci**. It merges with the **accessory
        superior frontal sulcus (ASFS)** near the frontal pole
        .

**This field is byte-identical to the left-hemisphere sibling.** The
caudal SPRS junction and the rostral frontopolar interruption are
hemisphere-invariant.

The SFS therefore runs the full anteroposterior extent of the
dorsolateral frontal convexity's dorsal strip — from the SPRS caudally
to the frontopolar region rostrally — but it is a **merging sulcus at
both ends**, not a free-standing groove.

--------------------------------------------------------------------------------
VARIANTS (right-hemisphere specific)
--------------------------------------------------------------------------------

The SFS is one of the **most morphologically variable** sulci in the
frontal lobe. Its principal variants are continuity (Type I vs Type II),
merging behaviour (Subtype a vs b), and the **left-right asymmetry in
segment extent**. The **right hemisphere is more often discontinuous**
than the left.

    Type_I_continuous             18 % of right hemispheres
        The SFS is a **single continuous sulcus** from the SPRS to the
        frontopolar region. **On the right this pattern is LESS common
        than on the left** (18 % vs 24 %) [reference:15].

    Type_II_discontinuous         32 % of right hemispheres
        The SFS is a **discontinuous sulcal complex** comprising an
        **anterior ramus (SFS-a)** and a **posterior ramus (SFS-p)**
        [reference:16]. **On the right this pattern is MORE common than on
        the left** (32 % vs 26 %) — the right SFS is the more often
        discontinuous hemisphere.

    Subtype_a_does_not_merge        2 % of right hemispheres
        The SFS (or SFS complex) is a **distinct sulcus that does not
        merge** with any surrounding frontal sulcus
        [reference:17]. Extremely rare on the right (2 % vs 4 % on the
        left).

    Subtype_b_merges                92 % of hemispheres
        The SFS **merges with at least one neighbouring frontal
        sulcus**. This is the overwhelming majority pattern on both
        sides [reference:18].

    SFS_a_extends_more_posteriorly_right   right-specific
        The **anterior ramus (SFS-a) extends more posteriorly in the
        right hemisphere** than in the left [reference:19][reference:20].
        This is the single most important left-right geometric
        asymmetry of the SFS, and it means the right SFS-a is the more
        reliable surface guide to the precentral region on the right.
        The asymmetry is attributed to **Yakovlevian torque**
        [reference:21].

    SFS_p_extends_more_caudally_left   left-specific
        The **posterior ramus (SFS-p) extends more caudally in the left
        hemisphere**[reference:22]. The mirror of the above asymmetry.

    three_segment_configuration     8 % of right hemispheres
        A three-segment SFS complex is **much less common on the right**
        (8 % vs 28 % on the left) [reference:23].

    four_segment_configuration     0 % of right hemispheres
        A four-segment complex is **absent on the right** (0 % vs 4 %
        on the left) [reference:24].

    hemispheric_congruence         60 % of brains
        In **60 % of brains**, both hemispheres show the **same primary
        morphological pattern** (both Type I or both Type II). In the
        remaining 40 %, the pattern differs across hemispheres — which
        is why the left and right SFS packages each carry their own
        VARIANTS list .

These variants are **geometric and topological**, not merely metric.
The Type I / Type II distinction changes the **number of grooves**, and
the Subtype a / b distinction changes the **merging relationships**. The
``BOUNDING_GYRI`` and ``BRODMANN_ADJACENCY`` fields must therefore be
read as the **canonical** boundary set, with the understanding that in
atypical patterns one or more boundaries may be absent or fused.

--------------------------------------------------------------------------------
CLINICAL SIGNIFICANCE (right-hemisphere specific)
--------------------------------------------------------------------------------

    right_superior_frontal_trans_sulcal_corridor
        **This is the right-SFS anchor par excellence.** The SFS is a
        **"non-eloquent corridor"** for reaching the **lateral
        ventricle, foramen of Monro, and internal capsule** without
        traversing primary motor or language cortex [reference:26]. The
        **superior frontal trans-sulcal transventricular approach**
        dissects through the SFS as an intrinsic microsurgical corridor
        to the lateral ventricle, minimizing brain retraction and
        transgression [reference:27]. On the right, the corridor is the
        approach of choice for **right-sided anterior ventricular and
        internal capsule lesions**.

    right_internal_capsule_cavernoma_corridor
        **Internal capsule cavernomas** — deep, eloquent-area lesions —
        can be approached via right frontal craniotomy **through the
        SFS** with curative resection and low morbidity
        [reference:28]. The corridor is safe because the SFS
        separates the SFG from the MFG without crossing primary motor
        or language cortex. The right SFS is the surface landmark for
        this corridor on the right.

    right_superior_frontal_sulcus_fcd_epilepsy
        **Focal cortical dysplasia (FCD) related to the SFS** is a
        surgically remediable syndrome of frontal lobe epilepsy with a
        **favorable postoperative seizure outcome** . The SFS
        is the surface landmark for the epileptogenic zone, and
        resective strategies guided by the SFS achieve high rates of
        seizure freedom. Right-sided SFS-FCD is documented in
        lesional epilepsy implantation strategies [reference:31].

    central_sulcus_identification_sign
        The **junction of the SFS with the precentral sulcus** is one of
        the **seven reliable signs for identifying the central sulcus**
        on MRI. The SFS is united with the precentral sulcus in the
        vast majority of cases, making this junction a dependable
        landmark for distinguishing the precentral from the central
        sulcus.

    tumour_and_fcd_resection_landmark
        Sulci and gyri are the **primary neuroanatomical landmarks used
        during neurosurgical interventions** such as tumour and FCD
        resections. The SFS is a **dependable landmark for dividing
        dorsomedial and dorsolateral prefrontal regions** and for
        guiding gyral entry points while avoiding unintended extension
        toward the precentral region where even small cortical injuries
        can produce motor deficits.

These anchors are **right-hemisphere-specific** in emphasis: the right
SFS-a extends more posteriorly, making it the more reliable guide to
the precentral region on the right; and the right SFS is the corridor
of choice for right-sided ventricular and internal capsule lesions. The
left sibling's docstring carries the left SFS-p caudal extent and the
left-sided surgical emphases.

--------------------------------------------------------------------------------
CONNECTIVITY (bundles running beneath the sulcus)
--------------------------------------------------------------------------------

The SFS is a **corridor-rich** sulcus. Cadaveric dissection and DTI
tractography have divided the SFS corridor into **medial, lateral, and
intervening white-matter segments**:

    medial to SFS
        → U-fibres (short-range cortico-cortical)
        → frontal_aslant_tract (FAT)
        → superior_longitudinal_fasciculus_I (SLF-I)
        → cingulum_bundle
        The medial segment carries the FAT (connecting SFG to the
        inferior frontal gyrus), SLF-I (adjacent to the cingulum and
        often indistinguishable from it) [reference:33], and the
        cingulum (default-mode and memory circuits).

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
        and crossing FAT and CCF fibres.

**Right-hemisphere-specific connectivity emphasis**: on the right,
**SLF-II connects the angular gyrus and superior parietal lobe with
the caudal and rostral middle frontal gyrus**, a pattern congruent with
**regulating the focus of attention in spatial orientation**
[reference:34]. On the left, by contrast, SLF-II connects the
supramarginal gyrus with the dorsal precentral gyrus and caudal MFG,
supporting **motor planning of language and/or syntactic processing**
[reference:35]. The right FAT carries **prosody / inhibition** content
rather than the left's speech-initiation content.

Additional SFG-level connections documented by DSI-based tractography:

    frontal_aslant_tract (FAT)
        → inferior_frontal_gyrus
        Connects the SFG (especially pre-SMA) to the pars opercularis
        of the IFG. On the right, this is the **prosody-inhibition**
        corridor.

    inferior_fronto_occipital_fasciculus (IFOF)
        → cuneus
        → lingual_gyrus
        → superior_parietal_lobule
        Connects the SFG to posterior visual and parietal association
        cortex.

    cingulum_bundle
        → precuneus
        → parahippocampal_gyrus / uncus
        Connects the SFG to the default-mode network and to medial
        temporal memory structures.

    callosal_fibres
        → contralateral SFG
        Bilateral callosal fibres connect the right and left SFG,
        supporting interhemispheric coordination of executive and
        motor functions.

The SFS is therefore the surface landmark for a **layered white-matter
corridor** — medial, lateral, and intervening segments — rather than for
a single dominant fasciculus. This layered organization is what makes
the SFS a **surgical corridor of choice**: the surgeon can choose the
medial, lateral, or intervening trajectory depending on the target and
the tracts to be avoided.

--------------------------------------------------------------------------------
CROSS-REFERENCES
--------------------------------------------------------------------------------

..gyri.superior_frontal_gyrus
    The dorsal bounding gyrus (right). The right SFG package **already
    declares the SFS as its ventral boundary**. The duality contract
    resolves fully for this link — no forward reference.

..gyri.middle_frontal_gyrus
    The ventral bounding gyrus (right). The right MFG package **already
    declares the SFS as its dorsal boundary**. The duality contract
    resolves fully for this link — no forward reference.

..sulci.precentral_sulcus
    The caudal neighbour. The SFS **merges with the superior precentral
    sulcus (SPRS) in the vast majority of hemispheres**
    [reference:36]. The SFS-SPRS junction is a reliable landmark for the
    central sulcus.

..sulci.inferior_frontal_sulcus
    The parallel sulcus one gyrus ventrally. The IFS separates MFG from
    IFG; the SFS separates SFG from MFG.

..brodmann_areas.brodmann_area_6
..brodmann_areas.brodmann_area_8
..brodmann_areas.brodmann_area_9
    The three BAs abutting the SFS. **Special note for BA 8**: the SFS
    separates **area 8A (granular, below the SFS)** from **area 8B
    (dysgranular, above the SFS)** . On the right, area 8A
    is the granular node of the ventral attention network's reorienting
    function.

..cortex.premotor_cortex
    The caudal bank of the SFS includes BA 6 (premotor strip). The
    premotor_cortex package must declare the SFS as a **surface
    landmark** for its dorsal margin, noting the right SMA's role in
    left-hand motor planning.

..cortex.supplementary_motor_cortex
    The medial continuation of the SFG carries the SMA / pre-SMA (BA
    6). The supplementary_motor_cortex package must declare the SFS as
    the **lateral boundary** of the medial BA 6 territory on the
    right.

..cortex.prefrontal_cortex
    The SFS separates the dorsal SFG (BA 9) from the dorsal MFG (BA 9),
    and the dorsal SFG (BA 8B) from the dorsal MFG (BA 8A). The
    prefrontal_cortex package must declare the SFS as the **surface
    boundary** within the DLPFC, and must note the rightward emphasis
    of area 8A for reorienting.

../../subcortical/basal_ganglia  — indirect
    The corona radiata descends beneath the SFS, adjacent to the basal
    ganglia.

../../subcortical/medial_temporal_lobe/hippocampus
    The cingulum bundle, which runs beneath the SFS, connects to the
    parahippocampal gyrus and uncus.

../../left/cortex/frontal/sulci/superior_frontal_sulcus
    The left-hemisphere homologue. Structural fields (SULCUS_NAME,
    LOBE, BOUNDING_GYRI, BRODMANN_ADJACENCY, EXTENT, SUBDIVISIONS) MUST
    be byte-identical to this package. Geometric and clinical fields
    (VARIANTS, CLINICAL_ANCHORS, CONNECTIVITY) are EXPECTED to differ —
    the right SFS-a extends more posteriorly, the left SFS-p extends
    more caudally, the right SFS is more often Type II (32 % vs 26 %),
    and the right SLF-II carries spatial-attention rather than
    language content.

--------------------------------------------------------------------------------
IMPLEMENTATION CONTRACT (this package)
--------------------------------------------------------------------------------

Module-level constants required:

    SULCUS_NAME         = "superior_frontal_sulcus"
    HEMISPHERE          = "right"
    LOBE                = "frontal"

    BOUNDING_GYRI       = {                          # identical to left
                              "dorsal":  ("superior_frontal_gyrus",),
                              "ventral": ("middle_frontal_gyrus",),
                          }

    BRODMANN_ADJACENCY  = {                          # identical to left
                              "dorsal":  (6, 8, 9),
                              "ventral": (6, 8, 9),
                          }

    EXTENT              = {                          # identical to left
                              "caudal":  ("superior_precentral_sulcus",
                                          "precentral_sulcus"),
                              "rostral": ("frontal_pole",
                                          "accessory_superior_frontal_"
                                          "sulcus"),
                          }

    VARIANTS            = (                          # DIFFERS from left
                              "Type_I_continuous_18%_right",
                              "Type_II_discontinuous_32%_right",
                              "Subtype_a_does_not_merge_2%_right",
                              "Subtype_b_merges_92%_overall",
                              "SFS_a_extends_more_posteriorly_right",
                              "three_segment_configuration_8%_right",
                              "four_segment_configuration_0%_right",
                              "hemispheric_congruence_60%_of_brains",
                              "yakovlevian_torque_anti_clockwise",
                          )

    CLINICAL_ANCHORS    = (                          # DIFFERS from left
                              "right_superior_frontal_trans_sulcal_"
                              "corridor",
                              "right_internal_capsule_cavernoma_"
                              "corridor",
                              "right_superior_frontal_sulcus_fcd_"
                              "epilepsy",
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
  4. Mirror the promotion on the left side in the same commit.

**Duality caveat**: the superior and middle frontal gyri declare the
SFS *as a whole* as their boundary. A ramus split does not create new
gyri-facing partners — the parent remains canonical.

**The Type I / Type II distinction must be respected**: in Type I
(continuous) hemispheres, there is only one groove and no ramus split
is anatomically meaningful. A ramus split should therefore be applied
only to Type II hemispheres, or the package must carry an explicit
``RAMUS_SPLIT_APPLICABLE = "Type_II_only"`` flag. **On the right this
matters more than on the left**, because the right SFS is more often
Type II (32 % vs 26 %).

--------------------------------------------------------------------------------
HEMISPHERIC-SYMMETRY CONTRACT
--------------------------------------------------------------------------------

Compared to ``../../left/.../superior_frontal_sulcus``:

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
        HEMISPHERE           "right" vs "left"
        VARIANTS             right: Type I 18 %, Type II 32 %,
                             SFS-a extends more posteriorly, three-
                             segment 8 %, four-segment 0 %, Subtype a
                             2 %; left: Type I 24 %, Type II 26 %,
                             SFS-p extends more caudally, three-
                             segment 28 %, four-segment 4 %, Subtype a
                             4 %. The right-only entry is
                             "yakovlevian_torque_anti_clockwise".
        CLINICAL_ANCHORS     right: right superior frontal trans-sulcal
                             corridor, right internal capsule
                             cavernoma corridor, right SFS-FCD
                             epilepsy; left: left trans-sulcal
                             corridor, left cavernoma corridor, left
                             FCD epilepsy.
        CONNECTIVITY         same bundle names; **right SLF-II connects
                             angular gyrus and superior parietal lobe
                             with caudal and rostral MFG, supporting
                             spatial-attention regulation**; the right
                             FAT carries prosody / inhibition content
                             rather than speech-initiation content.

**The SFS-a posterior extent asymmetry is the single most important
entry in this contract.** The right anterior ramus extends more
posteriorly than the left's [reference:38]. Any downstream code that uses
the SFS-a as a surface guide to the precentral region must specify
hemisphere — the right SFS-a reaches further posteriorly and is the
more reliable landmark on that side. The asymmetry is attributed to
**Yakovlevian torque** [reference:39], and the right-only VARIANT entry
records this explicitly.

--------------------------------------------------------------------------------
CHECKLIST
--------------------------------------------------------------------------------

[ ] SULCUS_NAME is exactly "superior_frontal_sulcus" (same as left).
[ ] HEMISPHERE is "right".
[ ] LOBE is "frontal" (same as left).
[ ] BOUNDING_GYRI is **simple two-sided**: dorsal
    (superior_frontal_gyrus,), ventral (middle_frontal_gyrus,), and
    byte-identical to the left sibling's BOUNDING_GYRI.
[ ] Both bounding gyri already exist as packages under ``..gyri``
    (right) and declare the SFS as a boundary — **no forward
    reference**.
[ ] BRODMANN_ADJACENCY is set-valued per side and includes the
    **8A / 8B distinction**: the SFS separates granular 8A (below,
    MFG) from dysgranular 8B (above, SFG) .
[ ] EXTENT is byte-identical to the left sibling: caudal **SPRS
    junction (92 % merge rate)** and rostral **frontopolar
    interruption / ASFS merge** [reference:41].
[ ] SUBDIVISIONS is empty and byte-identical to the left sibling.
[ ] VARIANTS documents **Type I 18 % right** and **Type II 32 %
    right** — the right SFS is **more often discontinuous** than the
    left (32 % vs 26 %) [reference:43].
[ ] VARIANTS documents Subtype a **2 % right** (vs 4 % left) and
    Subtype b (92 % merge) [reference:44].
[ ] VARIANTS documents the **right-specific** entries: SFS-a extends
    more posteriorly, three-segment 8 %, four-segment 0 %, and the
    **yakovlevian_torque_anti_clockwise** explanation [reference:45].
[ ] VARIANTS documents hemispheric congruence (60 % of brains)
    .
[ ] CLINICAL_ANCHORS contains the five right-specific anchors:
    right_superior_frontal_trans_sulcal_corridor, right_internal_
    capsule_cavernoma_corridor, right_superior_frontal_sulcus_fcd_
    epilepsy, central_sulcus_identification_sign,
    tumour_and_fcd_resection_landmark.
[ ] CONNECTIVITY separates the **medial** (U-fibres, FAT, SLF-I,
    cingulum), **lateral** (U-fibres, SLF-II, CCF, IFOF), and
    **intervening** (FAT, corona radiata, CCF) segments
    .
[ ] CONNECTIVITY documents the **right-specific SLF-II connectivity**:
    angular gyrus + superior parietal lobe → caudal and rostral MFG,
    supporting **spatial-attention regulation** (contrast with the
    left's language-motor role) [reference:48].
[ ] Every CONNECTIVITY target is either a real package or a documented
    forward reference.
[ ] ``..gyri.superior_frontal_gyrus`` and
    ``..gyri.middle_frontal_gyrus`` (right) both declare the SFS as a
    boundary — the duality contract passes fully.
[ ] No SUBDIVISIONS promotion is performed without mirroring on the
    left and without a Type I / Type II applicability flag.
[ ] Cross-hemisphere symmetry test passes: structural fields match the
    left sibling; the SFS-a posterior extent, Type I/II frequencies,
    segment counts, Yakovlevian-torque entry, and right SLF-II
    spatial-attention content deliberately differ.
[ ] Any downstream code using the SFS-a as a precentral landmark is
    required to specify hemisphere — the right SFS-a extends further
    posteriorly [reference:49].
"""