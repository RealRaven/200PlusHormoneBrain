"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex
=================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── cortex            <-- THIS MODULE

**Primary synonym:** Temporal neocortex (right); Temporal functional cortex.
**Organizing principle:** **Functional–anatomical partition**, NOT
cytoarchitectonic.
**Laterality:** right hemisphere.
**Sibling aggregators:** ``.../temporal/brodmann_areas`` (cytoarchitectonic),
``.../temporal/gyri`` (structural), ``.../temporal/sulci`` (sulcal). See
"The Two Partitions" below.
**Note on `medial_superior_temporal_area`:** MST is a **standalone functional
node at the lobe level**, **NOT** a child of this `cortex/` aggregator. See
"The MST exception" below.

Overview
--------
This module groups the **functional regions** of the right temporal lobe:
the primary and secondary auditory cortices, the visual association areas
of the inferior temporal cortex, and the anterior temporal social/emotional
hub. It is the **functional twin** of the cytoarchitectonic partition at
``.../temporal/brodmann_areas`` and the **structural mirror** of the left
``cortex`` aggregator at ``.../left/cortex/temporal/cortex``.

**This is the right-hemisphere functional aggregator, and its regions
carry the right-lateralized complement of the left's language functions**
— music, prosody, face recognition, motion processing, and social/emotional
semantics. The **region inventory is identical** to the left; only the
**lateralization prose** differs.

**The two partitions are complementary, not redundant, and — unlike the
parietal cortex aggregator — they cross into other lobes.** Several
functional regions in this module map to **Brodmann areas that live in
other partitions** (insular, occipital), not just to the temporal Brodmann
areas. Consumers must not assume that "the right temporal cortex functional
partition" is confined to the "right temporal Brodmann partition".

The two organizing principles are **complementary, non-nesting, and
coordinate** — each is a different slice through the same anatomical
territory:

*   **``brodmann_areas``** answers *"which cytoarchitectonic field is
    this?"* — Brodmann (1909) nomenclature.
*   **``cortex``** (this module) answers *"which functional region is
    this?"* — the classical auditory / visual / social-semantic grouping.

Both are valid, but they are **not interchangeable**. A consumer that
asks "which Brodmann areas constitute the right primary auditory cortex?"
and only queries ``brodmann_areas`` will **miss the answer** — the answer
is **BA41 and BA42**, which live under the **insular** partition, not the
temporal one.

Child Modules
-------------
Six functional regions are wired under this package — **structurally
identical to the left twin**:

*   ``primary_auditory_cortex`` (**A1**) — the **core auditory
    processing area** on Heschl's gyrus. **Bilateral** for basic acoustic
    features, with a **rightward bias for tonal/musical stimuli** and a
    **leftward bias for speech sounds**. **Brodmann mapping:** **BA41 and
    BA42** — which live under the **insular partition**
    (``.../insular/brodmann_areas/``), **not** under the temporal
    partition.

*   ``secondary_auditory_cortex`` (**A2**) — the **auditory association
    cortex** surrounding A1. On the **right**, A2 is
    **right-lateralized for music and prosody** — pitch, melody, and
    emotional intonation. **Brodmann mapping:** **BA22** (the top-level
    Brodmann leaf in the temporal partition) **and** the **nested
    "Wernicke's-area" leaf** at
    ``.../temporal/gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22``
    — but on the right, the "Wernicke's" name is **inherited structurally**,
    not functionally; the right BA22 is the right superior temporal
    auditory/prosodic cortex.

*   ``anterior_temporal_lobe`` (**ATL**) — on the **right**, the ATL is
    the **social/emotional semantic hub** (person knowledge, social
    scripts, emotional associations, social concepts). The left ATL is
    the **verbal semantic hub**. **Brodmann mapping:** **BA38** (temporal
    pole) plus parts of **BA20, BA21** — all in the temporal partition.

*   ``inferior_temporal_cortex`` (**ITC**) — on the **right**, the ITC
    supports **non-verbal visual-semantic processing** and **affective
    visual semantics** (metaphor processing, face-adjacent structural
    judgments). **Brodmann mapping:** **BA20** (inferior temporal area).

*   ``posterior_inferior_temporal_cortex`` (**pITC**) — on the **right**,
    the pITC contains the **fusiform face area (FFA)** — the substrate
    for **face recognition**. **Brodmann mapping:** **BA37** (fusiform)
    plus parts of **BA21, BA20**.

*   ``mt`` — the **middle temporal visual area** (V5), the **motion-
    processing hub** of the dorsal visual stream. **Bilateral**, with
    **right-hemisphere dominance for motion processing**. **Brodmann
    mapping:** **BA19** — which lives under the **occipital partition**
    (``.../occipital/brodmann_areas/``), **not** under the temporal
    partition.

**Areas *not* covered by this functional partition:**

*   **Medial temporal lobe memory structures** (entorhinal, perirhinal,
    parahippocampal, presubiculum) are wired as **gyri** and **Brodmann
    leaves**, not as `cortex/` functional regions.
*   **`medial_superior_temporal_area` (MST)** is a **standalone functional
    node at the lobe level**, **not** a child of this aggregator.

The Two Partitions — Cross-Lobe Boundaries
-----------------------------------------
The right temporal functional partition is **one of two partitions in the
tree (the other being the left) whose functional regions map to Brodmann
areas in *other lobes'* partitions**. This is the **defining
architectural feature** of this module:

::

    Functional region (this module)     Primary Brodmann mapping       Brodmann partition
    ───────────────────────────────     ────────────────────────       ──────────────────
    primary_auditory_cortex (A1)    ──▶ BA41, BA42                  **insular** (not temporal)
    secondary_auditory_cortex (A2)  ──▶ BA22                        temporal (prosodic on right)
    anterior_temporal_lobe (ATL)    ──▶ BA38 (+ parts of BA20, 21)  temporal
    inferior_temporal_cortex (ITC)  ──▶ BA20                        temporal
    posterior_inferior_temporal_cortex (pITC) ──▶ BA37 (+ BA20, 21) temporal
    mt                              ──▶ BA19                        **occipital** (not temporal)

**Two of the six regions map outside the temporal Brodmann partition:**

*   **A1 → BA41, BA42 (insular partition).** A consumer querying "which
    Brodmann areas are in the right temporal lobe?" will **not** see
    BA41/BA42 — they must query the insular partition separately.

*   **MT → BA19 (occipital partition).** The middle temporal visual area
    is **anatomically on the lateral temporal-occipital border**, but its
    Brodmann designation (BA19) is **under the occipital partition**.

**Consumers must not assume that the right temporal functional partition
maps 1:1 onto the right temporal Brodmann partition.** The mapping is
**many-to-many** and **cross-lobe**.

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
comfortably into the `cortex/` partition. The tree's authors placed it at
the **lobe level** as a **standalone functional node**.

**Consumers that need MST must query
``temporal.medial_superior_temporal_area``, not
``temporal.cortex.medial_superior_temporal_area``.**

Function in the Human Brain
---------------------------
The six functional regions collectively cover the **auditory,
visual-association, and social/emotional-semantic** functions of the right
temporal lobe — with a **strong right-lateralization for music, prosody,
and faces**:

*   **Primary auditory cortex (A1):** Basic acoustic features. **Bilateral**,
    with a **rightward bias for music** and a **leftward bias for speech**.
*   **Secondary auditory cortex (A2):** Complex auditory patterns,
    music, prosody. **Right-lateralized for music and prosody.**
*   **Anterior temporal lobe (ATL):** Social/emotional semantics, person
    knowledge, social scripts. **Right-lateralized** for social/emotional
    semantics.
*   **Inferior temporal cortex (ITC):** Non-verbal visual semantics,
    metaphor processing, affective visual semantics. **Right-lateralized**
    for metaphor and affect.
*   **Posterior inferior temporal cortex (pITC):** FFA (face recognition),
    visual object processing. **Right-lateralized** for faces.
*   **MT:** Motion processing. **Bilateral**, with **right-hemisphere
    dominance** for motion.

**Functions *not* covered by this functional partition** (they belong to
the allocortical/transitional `gyri` and `brodmann_areas`):

*   Medial temporal lobe memory functions (declarative memory, spatial
    navigation, object recognition familiarity).
*   Hippocampal formation (presubiculum, entorhinal, perirhinal complex).
*   MST motion-in-depth and egomotion (standalone at lobe level).

Lateralization Notes
--------------------
This is the **right** temporal functional-cortex module. The
lateralization landscape is **strongly right-loaded for music, prosody,
faces, and social/emotional functions**, with **symmetric auditory and
motion foundations**:

*   **Strongly Right-Lateralized Functions (dominant in this twin):**
    - **Music and prosody** (A2 right).
    - **Face recognition (FFA)** (pITC right, BA37 FFA).
    - **Motion-dominance** (MT right).
    - **Social/emotional semantics** (ATL right).
    - **Metaphor and affective visual semantics** (ITC right).

*   **Left-Lateralized Functions (contrast — absent here):**
    - **Speech-sound processing** (A2 left).
    - **Verbal semantic memory** (ATL left).
    - **Visual-semantic naming** (ITC left).
    - **Visual word form area / reading** (pITC left, BA37 VWFA).

*   **Symmetric Functions (bilateral properties):**
    - Basic acoustic feature analysis (A1).
    - Visual object processing (ITC, pITC).
    - Motion processing (MT, with right weighting).

**A consumer that assumes "right temporal cortex = symmetric" will be
wrong for the majority of its highest-value functions** — the right
carries the **music, prosody, face, and social hub** (A2 right, pITC
right FFA, MT right, ATL right). The left twin carries the **language and
reading hub**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    insular partition (for BA41/BA42) or the occipital partition (for
    BA19/MT). Those **cross-partition mappings** are documented as
    **data** (``REGION_TO_BRODMANN``), not as structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional partition, not cytoarchitectonic.** ``__all__`` lists
    the six **regions**, not the Brodmann areas.
*   **Region-to-Brodmann mapping is data, not code.** The
    ``REGION_TO_BRODMANN`` constant documents the **cross-lobe** mapping.
    The ``CROSS_PARTITION_AREAS`` constant documents the **two regions
    that map outside the temporal partition** (A1 → insular; MT →
    occipital).
*   **MST is NOT a child of this aggregator.** Consumers that need MST
    must query ``temporal.medial_superior_temporal_area``.
*   **Structural parity with left temporal cortex.** Left and right
    ``cortex`` aggregators are **structurally identical** in their region
    list and mapping constants; only the **lateralization prose** differs.

Usage
-----
Resolve functional regions by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex import (
        REGIONS, REGION_TO_BRODMANN, CROSS_PARTITION_AREAS,
    )

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.cortex.primary_auditory_cortex"
    )

Cross-partition query (which Brodmann areas, including other lobes)::

    # "Which Brodmann areas constitute the right primary auditory cortex?"
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
    *NeuroImage*, 83, 1002–1017.
*   **Right A2 and music:** Zatorre, R.J., Belin, P., & Penhune, V.B.
    (2002). "Structure and function of auditory cortex: music and speech."
    *Trends Cogn Sci*, 6(1), 37–46. Right auditory cortex dominant for
    music and pitch.
*   **Right A2 and prosody:** Ross, E.D. (1981). "The aprosodias:
    functional-anatomic organization of the affective components of
    language in the right hemisphere." *Arch Neurol*, 38(9), 561–569.
*   **Right ATL and social semantics:** Zahn, R., et al. (2007). "Social
    concepts are represented in the superior anterior temporal cortex."
    *PNAS*, 104(15), 6430–6435.
*   **Right ITC and metaphor/affect:** Bambini, V., et al. (2016).
    "Disentangling Metaphor from Context: An ERP Study." *Front Psychol*,
    7, 559. Right BA20/BA21 as metaphor/affect substrate.
*   **Right pITC and FFA:** Kanwisher, N., McDermott, J., & Chun, M.M.
    (1997). "The fusiform face area: a module in human extrastriate
    cortex specialized for face perception." *J Neurosci*, 17(11),
    4302–4311.
*   **MT / V5 (BA19):** Zeki, S. (1974). "Functional organization of a
    visual area in the posterior bank of the superior temporal sulcus of
    the rhesus monkey." *J Physiol*, 236(3), 549–573.
*   **Cross-lobe mapping of A1 and MT:** Brodmann, K. (1909).
    *Vergleichende Lokalisationslehre der Grosshirnrinde*. BA41/BA42
    grouped with posterior insula; BA19 grouped with occipital
    association cortex.
*   **MST standalone node:** Tanaka, K., & Saito, H. (1989). "Analysis of
    motion of the visual field by direction, expansion/contraction, and
    rotation cells clustered in the dorsal part of the medial superior
    temporal area of the macaque monkey." *J Neurophysiol*, 62(3),
    626–641.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed.
*   NeuroNames — Temporal lobe (right), functional regions; FMA — right
    temporal lobe partonomy.
"""