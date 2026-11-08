"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex
================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── cortex            <-- THIS MODULE

**Primary synonym:** Temporal neocortex (left); Temporal functional cortex.
**Organizing principle:** **Functional–anatomical partition**, NOT
cytoarchitectonic.
**Laterality:** left hemisphere.
**Sibling aggregators:** ``.../temporal/brodmann_areas`` (cytoarchitectonic),
``.../temporal/gyri`` (structural), ``.../temporal/sulci`` (sulcal). See
"The Two Partitions" below.
**Note on `medial_superior_temporal_area`:** MST is a **standalone functional
node at the lobe level**, **NOT** a child of this `cortex/` aggregator. See
"The MST exception" below.

Overview
--------
This module groups the **functional regions** of the left temporal lobe:
the primary and secondary auditory cortices, the visual association areas
of the inferior temporal cortex, and the anterior temporal semantic hub.
It is the **functional twin** of the cytoarchitectonic partition at
``.../temporal/brodmann_areas``.

**The two partitions are complementary, not redundant, and — unlike the
parietal cortex aggregator — they cross into other lobes.** Several
functional regions in this module map to **Brodmann areas that live in
other partitions** (insular, occipital), not just to the temporal
Brodmann areas. Consumers must not assume that "the temporal cortex
functional partition" is confined to the "temporal Brodmann partition".

The two organizing principles are **complementary, non-nesting, and
coordinate** — each is a different slice through the same anatomical
territory:

*   **``brodmann_areas``** answers *"which cytoarchitectonic field is
    this?"* — Brodmann (1909) nomenclature, used by neuroimaging atlases
    and by the FMA.
*   **``cortex``** (this module) answers *"which functional region is
    this?"* — the classical auditory / visual / semantic grouping, used by
    systems neuroscience and by clinical topology.

Both are valid, but they are **not interchangeable**. A consumer that
asks "which Brodmann areas constitute the left primary auditory cortex?"
and only queries ``brodmann_areas`` will **miss the answer** — the answer
is **BA41 and BA42**, which live under the **insular** partition, not the
temporal one. A consumer that asks "what does the left superior temporal
gyrus do?" and only queries ``cortex`` will miss that the **posterior STG
is BA22** (Wernicke's area) and has a **nested cross-listing** under the
superior temporal gyrus.

Child Modules
-------------
Six functional regions are wired under this package — all **structurally
identical to the right twin**:

*   ``primary_auditory_cortex`` (**A1**) — the **core auditory
    processing area** on Heschl's gyrus (transverse temporal gyri) in the
    superior temporal plane. **Bilateral** for basic acoustic features,
    with a **leftward bias for speech sounds** and a **rightward bias for
    tonal/musical stimuli**. **Brodmann mapping:** **BA41 and BA42** — which
    live under the **insular partition**
    (``.../insular/brodmann_areas/brodmann_area_41_posterior_insula`` and
    ``.../insular/brodmann_areas/brodmann_area_42_posterior_insula``),
    **not** under the temporal partition.

*   ``secondary_auditory_cortex`` (**A2**) — the **auditory association
    cortex** surrounding A1. Supports **complex auditory pattern
    analysis, phoneme discrimination, and higher-order auditory
    cognition**. **Left-lateralized for speech; right-lateralized for
    music and prosody**. **Brodmann mapping:** **BA22** (the **top-level
    Brodmann leaf** in the temporal partition) **and** the **nested
    Wernicke's-area leaf** at
    ``.../temporal/gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22``.

*   ``anterior_temporal_lobe`` (**ATL**) — the **anterior temporal
    semantic hub**. The left ATL is the **core substrate for verbal
    semantic memory** (word meanings, person knowledge, conceptual
    knowledge). The right ATL is the **social/emotional semantic hub**.
    **Brodmann mapping:** **BA38** (temporal pole) plus parts of **BA20,
    BA21** — all in the temporal partition.

*   ``inferior_temporal_cortex`` (**ITC**) — the **anterior portion of
    the inferior temporal visual association cortex**. Supports **visual
    object recognition and visual semantic processing**. The left ITC
    contains the **visual-semantic interface** for verbal labels. **Brodmann
    mapping:** **BA20** (inferior temporal area) — in the temporal
    partition.

*   ``posterior_inferior_temporal_cortex`` (**pITC**) — the **posterior
    portion of the inferior temporal visual association cortex**, including
    the **fusiform gyrus** and adjacent areas. The left pITC contains the
    **visual word form area (VWFA)** — the substrate for reading. **Brodmann
    mapping:** **BA37** (fusiform) plus parts of **BA21, BA20** — all in
    the temporal partition.

*   ``mt`` — the **middle temporal visual area** (V5), the **motion-
    processing hub** of the dorsal visual stream. **Bilateral**, with
    **right-hemisphere dominance for motion processing**. **Brodmann
    mapping:** **BA19** — which lives under the **occipital partition**
    (``.../occipital/brodmann_areas/brodmann_area_19``), **not** under the
    temporal partition. (Note: the tree's `brodmann_areas` partition
    wires BA19 under occipital, not temporal; this is the correct
    anatomical assignment.)

**Areas *not* covered by this functional partition:**

*   **Medial temporal lobe memory structures** (entorhinal, perirhinal,
    parahippocampal, presubiculum) are wired as **gyri** and **Brodmann
    leaves**, not as `cortex/` functional regions. The functional
    partition covers the **neocortical** temporal surface, not the
    allocortical/transitional medial temporal lobe.
*   **`medial_superior_temporal_area` (MST)** is a **standalone functional
    node at the lobe level**, **not** a child of this aggregator. See "The
    MST exception" below.
*   **Temporal pole (BA38)** is part of the `anterior_temporal_lobe`
    functional region, but it does not have a separate `cortex/` child.

The Two Partitions — Cross-Lobe Boundaries
-----------------------------------------
The temporal functional partition is **the first partition in the tree
whose functional regions map to Brodmann areas in *other lobes'*
partitions**. This is the **defining architectural feature** of this
module:

::

    Functional region (this module)     Primary Brodmann mapping       Brodmann partition
    ───────────────────────────────     ────────────────────────       ──────────────────
    primary_auditory_cortex (A1)    ──▶ BA41, BA42                  **insular** (not temporal)
    secondary_auditory_cortex (A2)  ──▶ BA22                        temporal
    anterior_temporal_lobe (ATL)    ──▶ BA38 (+ parts of BA20, 21)  temporal
    inferior_temporal_cortex (ITC)  ──▶ BA20                        temporal
    posterior_inferior_temporal_cortex (pITC) ──▶ BA37 (+ BA20, 21) temporal
    mt                              ──▶ BA19                        **occipital** (not temporal)

**Two of the six regions map outside the temporal Brodmann partition:**

*   **A1 → BA41, BA42 (insular partition).** The primary auditory cortex
    is **anatomically on Heschl's gyrus** (a temporal structure), but its
    cytoarchitectonic designation in the tree is **under the insular
    partition**, because Brodmann classed BA41/BA42 as part of the
    posterior insula. A consumer querying "which Brodmann areas are in
    the temporal lobe?" will **not** see BA41/BA42 — they must query the
    insular partition separately.

*   **MT → BA19 (occipital partition).** The middle temporal visual area
    is **anatomically on the lateral temporal-occipital border**, but its
    Brodmann designation (BA19) is **under the occipital partition**.
    A consumer querying the temporal Brodmann partition will **not** see
    BA19.

**Consumers must not assume that the temporal functional partition maps
1:1 onto the temporal Brodmann partition.** The mapping is
**many-to-many** and **cross-lobe**:

*   Some temporal Brodmann areas (BA27, BA28, BA34, BA35, BA36 — the
    medial temporal allocortical fields) have **no** `cortex/`
    functional child in this partition.
*   Some `cortex/` functional regions (A1, MT) map to Brodmann areas in
    **other lobes'** partitions.
*   Some functional regions (ATL, pITC) map to **multiple** Brodmann
    areas within the temporal partition.

The MST Exception
-----------------
**`medial_superior_temporal_area` (MST) is NOT a child of this `cortex/`
aggregator.** It is a **standalone functional node at the lobe level**,
sibling to ``brodmann_areas``, ``cortex``, ``gyri``, and ``sulci``:

::

    temporal/
    ├── brodmann_areas/
    ├── cortex/                          <-- THIS MODULE (6 regions)
    ├── gyri/
    ├── medial_superior_temporal_area/   <-- STANDALONE (not under cortex/)
    └── sulci/

**Why is MST excluded from this aggregator?** MST is **functionally
adjacent to MT** (it sits in the superior temporal sulcus, not on the
temporal convexity), and it is **too functionally specific** to fit
comfortably into the `cortex/` partition (which groups large
functional regions). The tree's authors placed it at the **lobe level**
as a **standalone functional node** — a legitimate architectural
admission that some structures do not fit cleanly into any partition.

**Consumers that need MST must query
``temporal.medial_superior_temporal_area``, not
``temporal.cortex.medial_superior_temporal_area``.** The two paths do
not exist — the `cortex/` aggregator deliberately excludes MST.

Function in the Human Brain
---------------------------
The six functional regions collectively cover the **auditory,
visual-association, and semantic** functions of the left temporal lobe —
with a **strong left-lateralization for language**:

*   **Primary auditory cortex (A1):** Basic acoustic features
    (frequency, intensity, duration). **Bilateral**, with a **leftward
    bias for speech** and a **rightward bias for music**.
*   **Secondary auditory cortex (A2):** Complex auditory patterns,
    phonemes, voice. **Left-lateralized for speech; right-lateralized
    for music and prosody.**
*   **Anterior temporal lobe (ATL):** Verbal semantic memory, person
    knowledge, conceptual knowledge. **Left-lateralized** for verbal
    semantics.
*   **Inferior temporal cortex (ITC):** Visual object recognition,
    visual-semantic interface. **Left-lateralized** for verbal visual
    semantics.
*   **Posterior inferior temporal cortex (pITC):** VWFA (reading),
    visual object processing. **Left-lateralized** for reading.
*   **MT:** Motion processing. **Bilateral**, with **right-hemisphere
    dominance** for motion.

**Functions *not* covered by this functional partition** (they belong to
the allocortical/transitional `gyri` and `brodmann_areas`):

*   Medial temporal lobe memory functions (declarative memory, spatial
    navigation, object recognition familiarity).
*   Hippocampal formation (presubiculum, entorhinal, perirhinal
    complex).
*   MST motion-in-depth and egomotion (standalone at lobe level).

Lateralization Notes
--------------------
This is the **left** temporal functional-cortex module. The
lateralization landscape is **strongly left-loaded for language and
semantic functions**, with **symmetric auditory and motion functions**:

*   **Strongly Left-Lateralized Functions (dominant in this twin):**
    - **Speech-sound processing** (A2 left).
    - **Verbal semantic memory** (ATL left).
    - **Visual-semantic naming** (ITC left).
    - **Visual word form area / reading** (pITC left, BA37 VWFA).

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Music and prosody** (A2 right).
    - **Face recognition** (pITC right, BA37 FFA).
    - **Motion-dominance** (MT right).
    - **Social/emotional semantics** (ATL right).

*   **Symmetric Functions (bilateral properties):**
    - Basic acoustic feature analysis (A1).
    - Visual object processing (ITC, pITC).
    - Motion processing (MT, with right weighting).

**A consumer that assumes "left temporal cortex = symmetric" will be
wrong for the majority of its highest-value functions** — the left
carries the **language and reading hub** (A2 left, ATL left, pITC left).
The right twin carries the **music, prosody, face, and social hub**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    insular partition (for BA41/BA42) or the occipital partition (for
    BA19/MT). Those **cross-partition mappings** are documented as
    **data** (``REGION_TO_BRODMANN``), not as structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional partition, not cytoarchitectonic.** ``__all__`` lists
    the six **regions**, not the Brodmann areas. Consumers that need
    Brodmann fields must query the relevant Brodmann partition (which
    may be temporal, insular, or occipital).
*   **Region-to-Brodmann mapping is data, not code.** The
    ``REGION_TO_BRODMANN`` constant documents the **cross-lobe** mapping.
    The ``CROSS_PARTITION_AREAS`` constant documents the **two regions
    that map outside the temporal partition** (A1 → insular; MT →
    occipital).
*   **MST is NOT a child of this aggregator.** Consumers that need MST
    must query ``temporal.medial_superior_temporal_area``, not
    ``temporal.cortex.medial_superior_temporal_area``.
*   **Structural parity with right temporal cortex.** Left and right
    ``cortex`` aggregators are **structurally identical** in their region
    list and mapping constants; only the **lateralization prose**
    differs.

Usage
-----
Resolve functional regions by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex import (
        REGIONS, REGION_TO_BRODMANN, CROSS_PARTITION_AREAS,
    )

    for region in REGIONS:
        # region is a functional module name, not a Brodmann area
        ...

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.cortex.primary_auditory_cortex"
    )

Cross-partition query (which Brodmann areas, including other lobes)::

    # "Which Brodmann areas constitute the left primary auditory cortex?"
    REGION_TO_BRODMANN["primary_auditory_cortex"]
    # -> ("brodmann_area_41", "brodmann_area_42")  -- in INSULAR partition
    # Note: these live at .../insular/brodmann_areas/, not .../temporal/

For the two regions that map outside the temporal partition::

    from ...temporal.cortex import CROSS_PARTITION_AREAS
    # CROSS_PARTITION_AREAS["primary_auditory_cortex"] = "insular"
    # CROSS_PARTITION_AREAS["mt"] = "occipital"

**For MST (which is NOT a child of this aggregator):**

    from ...temporal import medial_superior_temporal_area
    # MST lives at lobe level, not under cortex/

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        temporal_cortex = importlib.import_module(
            f"infrastructure.brainparts.forebrain.telencephalon."
            f"cerebral_hemispheres.{side}.cortex.temporal.cortex"
        )
        for region in temporal_cortex.REGIONS:
            # query the right- or left-hemisphere region
            ...

References
----------
*   **Primary auditory cortex (A1, BA41/BA42):** Moerel, M., De Martino,
    F., & Formisano, E. (2014). "An anatomical and functional topography
    of acoustic and auditory dimensions in human auditory cortex."
    *NeuroImage*, 83, 1002–1017. A1 on Heschl's gyrus; tonotopic
    organization; left/right asymmetries for speech/music.
*   **Secondary auditory cortex (A2, BA22):** Binder, J.R., et al.
    (2009). "Where is the semantic system? A critical review and
    meta-analysis of 120 functional neuroimaging studies." *Cereb
    Cortex*, 19(12), 2767–2796. BA22 (posterior STG) as the core
    language-comprehension area.
*   **Anterior temporal lobe semantic hub (ATL, BA38 + BA20/21):**
    Patterson, K., Nestor, P.J., & Rogers, T.T. (2007). "Where do you
    know what you know? The representation of semantic knowledge in the
    human brain." *Nat Rev Neurosci*, 8(12), 976–987. The ATL as the
    semantic hub, with left-dominant verbal semantics and right-dominant
    social/affective semantics.
*   **Inferior temporal cortex (ITC, BA20):** Ardila, A., Bernal, B., &
    Rosselli, M. (2015). "Language and Visual Perception Associations:
    Meta-Analytic Connectivity Modeling of Brodmann Area 37."
    *Behavioural Neurology*, 2015, 565871. BA20 as visual-semantic
    association cortex.
*   **Posterior inferior temporal cortex / VWFA (pITC, BA37):** Cohen,
    L., et al. (2000). "The visual word form area: spatial and temporal
    characterization of an initial stage of reading." *Brain*, 123(2),
    291–307. The VWFA in the left mid-fusiform gyrus (BA37).
*   **MT / V5 (BA19):** Zeki, S. (1974). "Functional organization of a
    visual area in the posterior bank of the superior temporal sulcus of
    the rhesus monkey." *J Physiol*, 236(3), 549–573. MT as the motion-
    processing area; right-hemisphere dominance for motion in humans.
*   **Cross-lobe mapping of A1 and MT:** Brodmann, K. (1909).
    *Vergleichende Lokalisationslehre der Grosshirnrinde*. BA41/BA42
    grouped with posterior insula; BA19 grouped with occipital
    association cortex. This cross-lobe grouping is preserved in the FMA
    and in the tree's partition assignments.
*   **MST standalone node:** Tanaka, K., & Saito, H. (1989). "Analysis
    of motion of the visual field by direction, expansion/contraction,
    and rotation cells clustered in the dorsal part of the medial
    superior temporal area of the macaque monkey." *J Neurophysiol*,
    62(3), 626–641. MST as a motion-in-depth and egomotion area,
    functionally adjacent to MT but distinct from MT.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Temporal neocortical anatomy.)
*   NeuroNames — Temporal lobe (left), functional regions; FMA — left
    temporal lobe partonomy.
"""