"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal
=========================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal              <-- THIS MODULE

**Primary synonym:** Temporal lobe (left); Lobus temporalis.
**Organizing principle:** **Lobar aggregator** — the top-level container for
the left temporal lobe's four organizing partitions.
**Structural boundaries:** Lateral sulcus / Sylvian fissure (superiorly),
parieto-occipital sulcus (posteriorly), the inferior temporal sulcus
(laterally), and the inferior (tentorial) surface (inferiorly).
**Lateralization profile:** **Strongly left-loaded for language** —
**Wernicke's area (BA22)**, the **temporal pole (BA38)**, and the
**visual word form area (BA37)** are **left-dominant**. The **right**
temporal lobe carries **prosody, music, and face processing** in the
symmetric counterparts.

Overview
--------
The **left temporal lobe** is the **language-dominant temporal lobe** and
one of the most functionally asymmetric regions in the human brain. It is
the **primary auditory and language cortex**, the **semantic memory hub**,
and a **critical interface between the auditory, visual, and limbic
systems**. It contains the **classical Wernicke's area (BA22)** — the
posterior superior temporal gyrus that is the core substrate for **speech
comprehension** — and it is the **left-lateralized pole of the language
network** that pairs with **Broca's area (BA44/BA45)** in the frontal lobe.

**The temporal lobe is the second lobe in the brainparts tree (after
parietal) to be documented across four organizing principles.** Its
internal structure follows the same four-partition architecture:

::

    Functional         Cytoarchitectonic      Structural           Sulcal
    ──────────         ────────────────       ──────────           ──────
    cortex/            brodmann_areas/        gyri/                sulci/
    ├── anterior TL    ├── BA15 (boundary)    ├── entorhinal_cx    ├── inferior
    ├── inferior TC    ├── BA20               ├── fusiform_gyrus   │   temporal
    ├── MT             ├── BA21               ├── inferior_temporal├── superior
    ├── posterior ITC  ├── BA22 (Wernicke)    ├── middle_temporal  │   temporal
    ├── primary AC     ├── BA27 (piriform)    ├── parahippocampal
    └── secondary AC   ├── BA28               ├── perirhinal_cx
                       ├── BA34               └── superior_temporal
                       ├── BA35                   └── wernickes_area
                       ├── BA36                       └── BA22 (cross)
                       ├── BA37
                       ├── BA38
                       └── BA48_retrosubicular

**Two architectural quirks distinguish the temporal lobe from the parietal
lobe:**

1. **`medial_superior_temporal_area` is a functional region node at the
   lobe level**, not under `cortex/`. This is the **first non-partition,
   non-aggregator functional node** in the tree — it sits directly under
   `temporal/` as a sibling of the four partitions. See
   "The medial_superior_temporal_area anomaly" below.

2. **`superior_temporal_gyrus/wernickes_area/brodmann_area_22`** is the
   **first nested cross-listing** in the tree — BA22 is both a top-level
   Brodmann leaf under `brodmann_areas/` and a **nested child** of
   `wernickes_area/` under the superior temporal gyrus. Unlike BA3 (which
   lives *only* under the gyrus), BA22 lives in **both** places. See "The
   nested cross-listing" below.

The Four Partitions
-------------------
The temporal lobe has **four organizing principles**, wired as follows:

*   **`cortex/`** — **functional regions**: anterior temporal lobe,
    inferior temporal cortex, MT (middle temporal visual area),
    posterior inferior temporal cortex, primary auditory cortex,
    secondary auditory cortex. Answers *"which functional region is
    this?"*.

*   **`brodmann_areas/`** — **cytoarchitectonic fields**: BA15, BA20,
    BA21, BA22, BA27, BA28, BA34, BA35, BA36, BA37, BA38, BA48_retro-
    subicular. Answers *"which Brodmann field is this?"*.

*   **`gyri/`** — **structural convolutions**: entorhinal cortex, fusiform
    gyrus, inferior temporal gyrus, middle temporal gyrus, parahippocampal
    gyrus, perirhinal cortex, superior temporal gyrus. Answers *"which
    macroscopic surface convolution is this?"*. Note that **`entorhinal_cortex`,
    `perirhinal_cortex`, and `fusiform_gyrus`** are **cytoarchitectonically
    defined names** that sit under `gyri/` — a structural-functional hybrid
    that recurs throughout the temporal lobe.

*   **`sulci/`** — **structural fissures**: inferior temporal sulcus,
    superior temporal sulcus. Answers *"which macroscopic surface fissure
    is this?"*.

**The four partitions are complementary, non-nesting, and coordinate** —
exactly as in the parietal lobe. A consumer that asks "what does the
superior temporal gyrus do?" must query `gyri/superior_temporal_gyrus`
(structural) **and** `cortex/primary_auditory_cortex` (functional) **and**
`brodmann_areas/brodmann_area_22` (cytoarchitectonic) **and**
`gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22` (the nested
cross-listing). No single partition answers the full question.

The `medial_superior_temporal_area` Anomaly
-------------------------------------------
**`medial_superior_temporal_area`** is a **functional region node at the
lobe level** — a sibling of the four partitions, not a child of any of them.
It is the **first such node in the brainparts tree**. Its architecture:

::

    temporal/
    ├── brodmann_areas/
    ├── cortex/
    ├── gyri/
    ├── medial_superior_temporal_area   <-- sibling of partitions
    └── sulci/

**Why is it here?** The medial superior temporal area (MST) is a
**motion-processing area adjacent to MT** — functionally distinct from
both the primary auditory cortex (which sits in the superior temporal
gyrus) and the inferior temporal visual areas. It is too functionally
specific to be a partition, and too functionally general to be a single
Brodmann field (the macaque MST is often grouped with MT but has distinct
connectivity and function). The tree's authors placed it at the lobe
level as a **standalone functional node**, acknowledging that it does not
fit cleanly into any of the four partitions.

**Resolution contract for consumers:**

*   If you need **MST as a functional node**, use
    `temporal.medial_superior_temporal_area`.
*   If you need **MST's cytoarchitectonic correlate**, it is **not a single
    Brodmann field** — it is adjacent to BA19/MT in most atlases and is
    usually mapped as a subfield of the MT/MST complex, which the tree does
    not have as a separate cytoarchitectonic leaf.
*   **Do not** assume that every functional node lives under `cortex/`. MST
    is the counterexample.

The Nested Cross-Listing
------------------------
**`superior_temporal_gyrus/wernickes_area/brodmann_area_22`** is the
**first nested cross-listing in the tree** — a Brodmann-area leaf that
lives under both `brodmann_areas/` **and** under `gyri/`:

::

    brodmann_areas/
    └── brodmann_area_22      <-- the top-level Brodmann leaf

    gyri/
    └── superior_temporal_gyrus/
        └── wernickes_area/
            └── brodmann_area_22   <-- the nested Wernicke's-area leaf

**Both are BA22.** The tree uses **two paths** to reach the same
cytoarchitectonic field:

*   **`brodmann_areas/brodmann_area_22`** — the canonical Brodmann leaf,
    used by consumers that iterate `brodmann_areas.ITERABLE_AREAS`.
*   **`gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22`** —
    the **functionally named** leaf, used by consumers that need the
    Wernicke's-area framing (language comprehension, conduction aphasia,
    aphasia recovery).

**This is different from the BA3 cross-listing in the parietal lobe.**
BA3 lives **only** under `gyri/postcentral_gyrus/` and is resolved via
`brodmann_areas.AREA_PATHS`. BA22 lives **in both places** as two separate
modules. The two modules should be **structurally identical** in their
cytoarchitectonic constants; only the **functional framing** differs.

**Resolution contract for consumers:**

*   If you need **BA22 as a Brodmann field**, use
    `brodmann_areas/brodmann_area_22`.
*   If you need **Wernicke's area (BA22) as a functionally named module**,
    use `gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22`.
*   Both are the same cortical territory. The two paths exist because
    **different consumers ask different questions** — cytoarchitectonic vs.
    functional.

Child Modules
-------------
The temporal lobe contains **22 leaf modules** across its four partitions
plus MST:

**Brodmann areas (12):**
*   `brodmann_area_15` — boundary case (subgenual; shared with cingulate)
*   `brodmann_area_20` — inferior temporal (visual semantic)
*   `brodmann_area_21` — middle temporal (semantic, language)
*   `brodmann_area_22` — **Wernicke's area** (left-lateralized speech
    comprehension)
*   `brodmann_area_27` — presubicular / piriform (olfactory)
*   `brodmann_area_28` — entorhinal (medial temporal memory gateway)
*   `brodmann_area_34` — dorsal entorhinal
*   `brodmann_area_35` — perirhinal (memory)
*   `brodmann_area_36` — perirhinal / parahippocampal (memory)
*   `brodmann_area_37` — fusiform (VWFA left; FFA right)
*   `brodmann_area_38` — temporal pole (semantic left; social right)
*   `brodmann_area_48_retrosubicular` — boundary case (retrosplenial)

**Functional cortex (6):**
*   `anterior_temporal_lobe` — semantic hub (left)
*   `inferior_temporal_cortex` — visual object recognition
*   `mt` — middle temporal visual area (motion)
*   `posterior_inferior_temporal_cortex` — visual association
*   `primary_auditory_cortex` — A1 (Heschl's gyrus; bilateral)
*   `secondary_auditory_cortex` — A2 (auditory association; bilateral)

**Gyri (7):**
*   `entorhinal_cortex` — memory gateway (hybrid structural-functional)
*   `fusiform_gyrus` — face (right) and word (left) processing
*   `inferior_temporal_gyrus` — visual object recognition
*   `middle_temporal_gyrus` — semantic and language processing
*   `parahippocampal_gyrus` — spatial and memory
*   `perirhinal_cortex` — object memory (hybrid)
*   `superior_temporal_gyrus` — auditory and language (contains
    `wernickes_area` as a nested child)

**Sulci (2):**
*   `inferior_temporal_sulcus` — separates ITG from fusiform
*   `superior_temporal_sulcus` — separates STG from MTG

**Standalone functional node (1):**
*   `medial_superior_temporal_area` — motion processing adjacent to MT

Function in the Human Brain
---------------------------
The left temporal lobe is the **language and semantic hub** of the brain.
Its best-supported functions cluster into seven domains:

*   **Speech Comprehension (Wernicke's Area — BA22):** The **posterior
    superior temporal gyrus (BA22)** is the classical **Wernicke's area** —
    the core substrate for **speech comprehension**. Lesions produce
    **Wernicke's aphasia** (fluent but nonsensical speech, impaired
    comprehension, poor repetition). This is the **most strongly left-
    lateralized function in the human brain**.

*   **Auditory Processing (Primary and Secondary Auditory Cortex):** A1
    (Heschl's gyrus, BA41/42 in older numbering, often mapped to BA22 in
    the tree's Brodmann partition) processes **basic acoustic features**
    (frequency, intensity, duration). A2 processes **complex auditory
    patterns** (phonemes, prosody, music). **A1 is largely symmetric**;
    **A2 and higher auditory areas are left-lateralized for speech and
    right-lateralized for music/prosody**.

*   **Semantic Memory and Language (Anterior Temporal Lobe, MTG, ITG):**
    The **left anterior temporal lobe** is the **semantic hub** for verbal
    concepts. The **left middle temporal gyrus (BA21)** supports **word
    meaning, sentence comprehension, and semantic retrieval**. The **left
    inferior temporal gyrus (BA20)** supports **visual semantic
    processing** (reading, object naming).

*   **Visual Word Form Area (VWFA — Left Fusiform, BA37):** The **left
    fusiform gyrus** contains the **visual word form area (VWFA)** — the
    **left-lateralized substrate for reading**. It responds to **written
    words** regardless of font, size, or case, and its disruption causes
    **pure alexia** (the inability to read).

*   **Face Processing (FFA — Right Fusiform, BA37):** The **right fusiform
    gyrus** contains the **fusiform face area (FFA)** — the **right-
    lateralized substrate for face recognition**. Prosopagnosia (the
    inability to recognize faces) follows **right fusiform** lesions far
    more often than left.

*   **Medial Temporal Memory (Entorhinal, Perirhinal, Parahippocampal):**
    The **medial temporal lobe (MTL) memory system** — **entorhinal cortex
    (BA28/34)**, **perirhinal cortex (BA35/36)**, and **parahippocampal
    gyrus** — is the **gateway to the hippocampus** for declarative memory.
    **Left-lateralized for verbal memory**, **right-lateralized for
    spatial memory**.

*   **Motion Processing (MT and MST):** The **middle temporal visual area
    (MT, BA19-equivalent)** and **medial superior temporal area (MST)**
    process **visual motion** and **optic flow**. **MT is bilateral**;
    **MST is right-dominant for self-motion perception**.

Associated Disorders
--------------------
Damage to or dysfunction of the left temporal lobe is associated with:

*   **Wernicke's Aphasia (BA22):** Fluent but nonsensical speech, impaired
    comprehension, poor repetition — the classical left temporal language
    syndrome.

*   **Pure Word Deafness:** Impaired **auditory comprehension of words**
    with preserved reading and writing, following **bilateral** or **left**
    lesions of primary auditory cortex.

*   **Semantic Dementia (Anterior Temporal Lobe):** Progressive loss of
    **word and object meaning**, with **left-predominant** anterior
    temporal atrophy.

*   **Pure Alexia (VWFA, BA37):** Inability to read **without agraphia**,
    following **left fusiform** lesions.

*   **Prosopagnosia (Right FFA, BA37):** Inability to recognize **familiar
    faces**, following **right fusiform** lesions (bilateral for severe
    cases).

*   **Verbal Memory Impairment (Left MTL):** Impaired **verbal declarative
    memory** following **left entorhinal/perirhinal/hippocampal** damage;
    **non-verbal/spatial memory** follows right-sided damage.

*   **Epilepsy (Temporal Lobe Epilepsy):** The temporal lobe is the **most
    common site of focal epilepsy**. **Left temporal lobe epilepsy (LTLE)**
    is associated with **verbal memory deficits**, **language-related
    functional reorganization**, and **Wernicke's area involvement**.

*   **Prosody and Music Deficits (Right Temporal):** **Aprosodia** (loss of
    emotional prosody) and **amusia** (loss of music perception) follow
    **right temporal** lesions.

**What is NOT here:** **Broca's aphasia** (left inferior frontal),
**conduction aphasia** (left arcuate fasciculus + BA40), and **Gerstmann
syndrome** (left angular gyrus) are syndromes of the **frontal and parietal
lobes**, not the temporal lobe. **Neglect** and **spatial-awareness** are
**right parietal** syndromes. The left temporal lobe is the **language
comprehension and semantic hub**, not the motor or spatial hub.

Lateralization Notes
--------------------
This is the **left** temporal lobe. The lateralization landscape is
**strongly left-loaded for language, with right-lateralized counterparts
for prosody, music, and faces** — the **most asymmetric lobe in the human
brain**:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Speech comprehension (Wernicke's area, BA22)** — the most
      left-lateralized language function.
    - **Semantic memory (anterior temporal lobe, BA38)** — left-dominant
      for verbal concepts.
    - **Visual word form area (VWFA, BA37)** — left fusiform; pure alexia
      follows left lesions.
    - **Phonological processing (STG, MTG)** — left-dominant for speech
      sounds.
    - **Verbal declarative memory (left MTL)** — left entorhinal/
      perirhinal/hippocampal.
    - **Sentence and narrative comprehension (left MTG, BA21)** —
      left-dominant.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Prosody and emotional intonation** — right STG/STS.
    - **Music perception (amusia)** — right auditory cortex.
    - **Face recognition (FFA, right fusiform, BA37)** — right-dominant.
    - **Non-verbal auditory processing** — right A2 and higher.
    - **Spatial declarative memory (right MTL)** — right entorhinal/
      perirhinal/hippocampal.
    - **Self-motion perception (MST)** — right-dominant.

*   **Symmetric Functions (bilateral properties of the temporal lobe,
    copied verbatim to the right twin):**
    - Primary auditory cortex (A1) — basic acoustic features.
    - Middle temporal visual area (MT) — motion processing.
    - Medial temporal lobe memory structures (entorhinal, perirhinal,
      parahippocampal) — gateway to hippocampus.
    - Piriform/olfactory cortex (BA27).
    - Temporal pole's basic structural organization.

**The left temporal lobe is the strongest left-lateralized lobe in the
human brain.** A consumer that assumes "left temporal = right temporal"
will be **wrong for the majority of its highest-value functions** —
Wernicke's area, the semantic hub, the VWFA, and verbal memory are all
strongly left-dominant.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe (Broca's area, BA44/45) or the parietal lobe (angular
    gyrus, BA39). Those are **sibling lobes**, and cross-lobe queries must
    be made explicitly by the consumer.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Lobar aggregator, not a partition.** This module does **not**
    enumerate children directly; it is a **container** for the four
    partitions (`brodmann_areas`, `cortex`, `gyri`, `sulci`) plus the
    standalone `medial_superior_temporal_area` node. Consumers that need
    leaves must descend into the partitions.
*   **The `medial_superior_temporal_area` anomaly is documented, not
    resolved.** MST sits at the lobe level because it does not fit cleanly
    into any partition. Consumers must not assume that every functional
    node lives under `cortex/`.
*   **The nested cross-listing is documented, not resolved.** BA22 lives
    under both `brodmann_areas/` and `gyri/superior_temporal_gyrus/
    wernickes_area/`. Consumers that need BA22 must be aware of **both**
    paths — the top-level Brodmann path and the nested Wernicke's-area
    path. The two modules should be **structurally identical** in their
    cytoarchitectonic constants; only the functional framing differs.
*   **Structural parity with right temporal lobe.** Left and right
    temporal lobe aggregators must be structurally identical in their
    **partition list** (four partitions plus MST) and **Brodmann area
    inventory** (BA15, 20, 21, 22, 27, 28, 34, 35, 36, 37, 38, 48). Only
    the **lateralization prose** differs.

Usage
-----
Resolve partitions by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal import (
        PARTITIONS, BRODMANN_AREAS, CORTEX_REGIONS, GYRI, SULCI,
        STANDALONE_NODES, NESTED_CROSS_LISTINGS,
    )

    for partition in PARTITIONS:
        # partition is "brodmann_areas", "cortex", "gyri", or "sulci"
        ...

    for ba in BRODMANN_AREAS:
        # iterate the top-level Brodmann leaf inventory
        ...

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.gyri.superior_temporal_gyrus.wernickes_area"
    )

For the nested cross-listing (BA22 as Wernicke's area)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 is the functionally framed BA22

For the top-level Brodmann leaf (BA22 as a cytoarchitectonic field)::

    from ...temporal.brodmann_areas import brodmann_area_22
    # structurally identical cytoarchitectonic constants;
    # only the functional framing differs

For the standalone functional node::

    from ...temporal import medial_superior_temporal_area
    # MST — sibling of partitions, not a child of cortex/

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        temporal_pkg = importlib.import_module(
            f"infrastructure.brainparts.forebrain.telencephalon."
            f"cerebral_hemispheres.{side}.cortex.temporal"
        )
        for ba in temporal_pkg.BRODMANN_AREAS:
            # resolve ba through the temporal lobe's brodmann_areas partition
            ...

References
----------
*   Terminologia Anatomica (FIPAT, 2019) — lobus temporalis; gyrus
    temporalis superior, medius, inferior; sulcus temporalis superior,
    inferior.
*   **Wernicke's area and aphasia:** Wernicke, C. (1874). *Der aphasische
    Symptomencomplex*. (Classical description of sensory aphasia and its
    localization to the posterior superior temporal gyrus.)
*   **Language network:** Binder, J.R., et al. (2009). "Where is the
    semantic system? A critical review and meta-analysis of 120 functional
    neuroimaging studies." *Cereb Cortex*, 19(12), 2767–2796.
*   **Visual word form area (VWFA):** Cohen, L., et al. (2000). "The visual
    word form area: spatial and temporal characterization of an initial
    stage of reading in normal subjects and posterior split-brain
    patients." *Brain*, 123(2), 291–307.
*   **Fusiform face area (FFA):** Kanwisher, N., McDermott, J., & Chun,
    M.M. (1997). "The fusiform face area: a module in human extrastriate
    cortex specialized for face perception." *J Neurosci*, 17(11),
    4302–4311.
*   **Medial temporal memory system:** Squire, L.R., & Zola-Morgan, S.
    (1991). "The medial temporal lobe memory system." *Science*,
    253(5026), 1380–1386.
*   **MT / MST motion areas:** Zeki, S. (1974). "Functional organization
    of a visual area in the posterior bank of the superior temporal sulcus
    of the rhesus monkey." *J Physiol*, 236(3), 549–573; Tanaka, K., &
    Saito, H. (1989). "Analysis of motion of the visual field by direction,
    expansion/contraction, and rotation cells clustered in the dorsal part
    of the medial superior temporal area of the macaque monkey."
    *J Neurophysiol*, 62(3), 626–641.
*   **Prosody and music (right temporal):** Zatorre, R.J., Belin, P., &
    Penhune, V.B. (2002). "Structure and function of auditory cortex: music
    and speech." *Trends Cogn Sci*, 6(1), 37–46.
*   **Semantic dementia:** Hodges, J.R., et al. (1992). "Semantic dementia:
    progressive fluent aphasia with temporal lobe atrophy." *Brain*,
    115(6), 1783–1806.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Temporal lobe (left); FMA — left temporal lobe partonomy.
"""