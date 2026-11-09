"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal
==========================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal              <-- THIS MODULE

**Primary synonym:** Temporal lobe (right); Lobus temporalis.
**Organizing principle:** **Lobar aggregator** — the top-level container for
the right temporal lobe's four organizing partitions.
**Structural boundaries:** Lateral sulcus / Sylvian fissure (superiorly),
parieto-occipital sulcus (posteriorly), the inferior temporal sulcus
(laterally), and the inferior (tentorial) surface (inferiorly).
**Lateralization profile:** **Right-loaded for prosody, music, faces,
non-verbal auditory processing, spatial memory, and self-motion
perception**. The **left** temporal lobe is the language and semantic
hub; the **right** temporal lobe is the **complementary prosody, music,
face, and spatial hub** — anatomically symmetric, functionally distinct.

Overview
--------
The **right temporal lobe** is the **non-verbal, prosodic, musical, and
spatial temporal lobe** — the anatomical counterpart to the left
language hub. It is **structurally identical** to the left temporal lobe
(same four partitions, same twelve Brodmann areas, same six functional
cortex regions, same seven gyri, same two sulci, same standalone MST
node, same nested BA22 cross-listing), but its **functional weightings
are inverted**:

*   **The left temporal lobe is the language hub:** speech comprehension
    (Wernicke's area, BA22), semantic memory (ATL, BA38), the visual word
    form area (left BA37), phonological processing (STG, MTG), verbal
    declarative memory (MTL), and sentence comprehension (left BA21).

*   **The right temporal lobe is the complementary non-verbal hub:**
    **prosody and emotional intonation** (right STG/STS), **music
    perception** (right auditory cortex), **face recognition** (fusiform
    face area, right BA37), **non-verbal auditory processing** (right A2
    and higher), **spatial declarative memory** (right MTL), and
    **self-motion perception** (right MST).

**The temporal lobe is the second lobe in the brainparts tree (after
parietal) to be documented across four organizing principles.** Its
internal structure is **identical to the left hemisphere's**:

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

**Two architectural quirks — identical to the left hemisphere — distinguish
the temporal lobe from the parietal lobe:**

1. **`medial_superior_temporal_area` is a functional region node at the
   lobe level**, not under `cortex/`. It is a sibling of the four
   partitions — the **first standalone functional node in the tree**.

2. **`superior_temporal_gyrus/wernickes_area/brodmann_area_22`** is the
   **nested cross-listing** — BA22 lives under **both**
   `brodmann_areas/` **and** a gyral path. On the **right** side, the
   **Wernicke's-area framing is preserved structurally** even though the
   **functional content** is different (the right BA22 is **not** the
   speech-comprehension hub; it is the **right superior temporal
   auditory/prosodic cortex**). See "The Wernicke's-area naming on the
   right side" below.

The Four Partitions
-------------------
Identical to the left temporal lobe:

*   **`cortex/`** — **functional regions**: anterior temporal lobe,
    inferior temporal cortex, MT, posterior inferior temporal cortex,
    primary auditory cortex, secondary auditory cortex.

*   **`brodmann_areas/`** — **cytoarchitectonic fields**: BA15, BA20,
    BA21, BA22, BA27, BA28, BA34, BA35, BA36, BA37, BA38,
    BA48_retrosubicular.

*   **`gyri/`** — **structural convolutions**: entorhinal cortex, fusiform
    gyrus, inferior temporal gyrus, middle temporal gyrus, parahippocampal
    gyrus, perirhinal cortex, superior temporal gyrus.

*   **`sulci/`** — **structural fissures**: inferior temporal sulcus,
    superior temporal sulcus.

**The four partitions are complementary, non-nesting, and coordinate** —
exactly as in the left temporal lobe. A consumer that asks "what does the
right superior temporal gyrus do?" must query **all four partitions** plus
the nested Wernicke's-area leaf (which on the right carries prosodic and
non-verbal auditory content, not speech comprehension).

The `medial_superior_temporal_area` Anomaly
-------------------------------------------
**`medial_superior_temporal_area`** (MST) is a **functional region node at
the lobe level** — a sibling of the four partitions, not a child of any of
them. It is the **first such node in the brainparts tree**, and it appears
on **both** sides.

**On the right side, MST carries a right-lateralized weighting for
self-motion perception** — the perception of one's own movement through
space (optic flow). The **right MST is the dominant substrate for
egomotion**; the left MST contributes but is not dominant. This is a
**right-lateralized functional addition** that is not mirrored on the
left.

**Resolution contract for consumers:**

*   If you need **MST as a functional node**, use
    `temporal.medial_superior_temporal_area`.
*   If you need **MST's cytoarchitectonic correlate**, it is **not a
    single Brodmann field** — it is adjacent to BA19/MT in most atlases
    and is usually mapped as a subfield of the MT/MST complex.
*   **Do not** assume that every functional node lives under `cortex/`.
    MST is the counterexample on both sides.

The Nested Cross-Listing
------------------------
**`superior_temporal_gyrus/wernickes_area/brodmann_area_22`** is the
**nested cross-listing** — a Brodmann-area leaf that lives under both
`brodmann_areas/` **and** under `gyri/`:

::

    brodmann_areas/
    └── brodmann_area_22      <-- the top-level Brodmann leaf

    gyri/
    └── superior_temporal_gyrus/
        └── wernickes_area/
            └── brodmann_area_22   <-- the nested Wernicke's-area leaf

**On the right side, the Wernicke's-area naming is a structural inheritance
rather than a functional claim.** The right BA22 sits in the right
posterior superior temporal gyrus, but it is **not** the substrate for
speech comprehension. It carries:

*   **Prosodic processing** — emotional intonation, sentence-level melody.
*   **Non-verbal auditory processing** — environmental sounds, voice
    timbre, music-adjacent features.
*   **Speech-adjacent auditory analysis** — the right STG responds to
    speech but with a **right-lateralized weighting for the non-semantic
    (prosodic and paralinguistic) features**.

**The left BA22 is Wernicke's area** — the classical speech-comprehension
hub. **The right BA22 is the right superior temporal auditory/prosodic
cortex** — the structural twin with a different functional overlay. Both
are called "BA22"; the **naming is symmetric, the function is not**.

**Resolution contract for consumers:**

*   If you need **BA22 as a Brodmann field on the right**, use
    `brodmann_areas/brodmann_area_22`.
*   If you need **the right superior temporal auditory/prosodic cortex**
    framed as a named region, use
    `gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22`.
    Be aware: the name "Wernicke's area" is **inherited**, not
    functionally accurate on the right.
*   **Both paths return the same cytoarchitectonic territory.** Only the
    functional framing differs.

Child Modules
-------------
The right temporal lobe contains **22 leaf modules** across its four
partitions plus MST — **structurally identical to the left**:

**Brodmann areas (12):**
*   `brodmann_area_15` — boundary case (shared with cingulate)
*   `brodmann_area_20` — inferior temporal (visual semantic; right
    contributes to non-verbal visual semantics)
*   `brodmann_area_21` — middle temporal (semantic; right contributes to
    non-verbal semantic and prosodic comprehension)
*   `brodmann_area_22` — **right superior temporal auditory/prosodic
    cortex** (inherits the "Wernicke's" name; **not** the speech-
    comprehension hub)
*   `brodmann_area_27` — presubicular / piriform (olfactory)
*   `brodmann_area_28` — entorhinal (medial temporal memory gateway)
*   `brodmann_area_34` — dorsal entorhinal
*   `brodmann_area_35` — perirhinal (memory)
*   `brodmann_area_36` — perirhinal / parahippocampal (memory)
*   `brodmann_area_37` — fusiform (**FFA right-dominant**; VWFA left)
*   `brodmann_area_38` — temporal pole (semantic left; **social/emotional
    right**)
*   `brodmann_area_48_retrosubicular` — boundary case (retrosplenial)

**Functional cortex (6):**
*   `anterior_temporal_lobe` — semantic hub (left); **social/emotional
    hub (right)**
*   `inferior_temporal_cortex` — visual object recognition
*   `mt` — middle temporal visual area (motion)
*   `posterior_inferior_temporal_cortex` — visual association
*   `primary_auditory_cortex` — A1 (Heschl's gyrus; bilateral)
*   `secondary_auditory_cortex` — A2 (auditory association; **right-
    dominant for music and non-verbal auditory**)

**Gyri (7):**
*   `entorhinal_cortex` — memory gateway (hybrid)
*   `fusiform_gyrus` — **FFA right**; VWFA left
*   `inferior_temporal_gyrus` — visual object recognition
*   `middle_temporal_gyrus` — semantic and **prosodic** processing
*   `parahippocampal_gyrus` — spatial and memory (**right-dominant for
    spatial**)
*   `perirhinal_cortex` — object memory (hybrid)
*   `superior_temporal_gyrus` — auditory and **prosodic** processing
    (contains `wernickes_area` as a nested child)

**Sulci (2):**
*   `inferior_temporal_sulcus`
*   `superior_temporal_sulcus` (**right-dominant for voice and prosody**)

**Standalone functional node (1):**
*   `medial_superior_temporal_area` — **right-dominant for self-motion
    perception**

Function in the Human Brain
---------------------------
The right temporal lobe is the **prosodic, musical, face, and spatial
hub** of the brain — the complementary hemisphere to the left language
and semantic hub. Its best-supported functions cluster into seven
domains:

*   **Prosody and Emotional Intonation (Right STG/STS):** The **right
    superior temporal gyrus and superior temporal sulcus** are the
    dominant substrate for **speech prosody** — the emotional and
    paralinguistic melody of speech. Lesions produce **aprosodia**
    (affective and/or linguistic prosody deficits) far more often than
    left-sided lesions.

*   **Music Perception (Right Auditory Cortex):** The **right secondary
    auditory cortex** and adjacent areas are **right-dominant for music
    perception** — pitch, melody, harmony, and rhythm. Lesions produce
    **amusia** more reliably on the right than on the left.

*   **Face Recognition (FFA — Right Fusiform, BA37):** The **right
    fusiform gyrus** contains the **fusiform face area (FFA)** — the
    **right-dominant substrate for face recognition**. Prosopagnosia (the
    inability to recognize familiar faces) follows **right fusiform**
    lesions far more often than left; bilateral lesions produce the most
    severe cases.

*   **Non-Verbal Auditory Processing (Right A2 and Higher):** The
    **right secondary auditory cortex** and adjacent regions are
    **dominant for non-verbal auditory processing** — environmental
    sounds, voice timbre, music, and paralinguistic features. Speech is
    **bilateral** at A1; the **left carries semantics** and the **right
    carries prosody and voice identity**.

*   **Spatial Declarative Memory (Right MTL):** The **right medial
    temporal lobe** — entorhinal (BA28/34), perirhinal (BA35/36),
    parahippocampal — is the **dominant substrate for spatial and
    non-verbal declarative memory**. Left-sided lesions impair verbal
    memory; **right-sided lesions impair spatial and visual memory**.

*   **Self-Motion Perception (Right MST):** The **right medial superior
    temporal area (MST)** is **dominant for egomotion** — the perception
    of one's own movement through space (optic flow). Lesions and
    stimulation studies implicate the right MST more strongly than the
    left.

*   **Social and Emotional Processing (Right Temporal Pole, BA38):** The
    **right temporal pole** participates in **social and emotional
    semantics** — person knowledge, social scripts, and emotional
    associations. Left BA38 is the verbal semantic hub; **right BA38** is
    the social/emotional hub.

Associated Disorders
--------------------
Damage to or dysfunction of the right temporal lobe is associated with:

*   **Aprosodia (Right STG/STS):** Loss of **emotional prosody** (affective
    aprosodia) and/or **linguistic prosody** — the right-hemisphere
    analogue of aphasia.

*   **Amusia (Right Auditory Cortex):** Loss of **music perception** —
    pitch, melody, and rhythm. **Right-lateralized** in most individuals.

*   **Prosopagnosia (Right FFA, BA37):** Inability to recognize **familiar
    faces**, following **right fusiform** lesions (bilateral for severe
    cases).

*   **Spatial Memory Impairment (Right MTL):** Impaired **spatial and
    non-verbal declarative memory** following **right entorhinal/
    perirhinal/hippocampal** damage. Verbal memory follows left-sided
    damage.

*   **Egomotion and Optic Flow Deficits (Right MST):** Impaired
    **self-motion perception** and **visually guided locomotion**,
    following right MST/posterior temporal lesions.

*   **Social-Emotional Semantic Deficits (Right Temporal Pole, BA38):**
    Impaired **person knowledge, social scripts, and emotional
    associations**, following right temporal pole damage.

*   **Right Temporal Lobe Epilepsy (RTLE):** The right temporal lobe is a
    common site of focal epilepsy. **RTLE** is associated with **non-
    verbal/spatial memory deficits**, **emotional and behavioral
    changes**, and **right temporal functional reorganization**.

**What is NOT here:** **Wernicke's aphasia** (left BA22), **semantic
dementia** (left ATL), **pure alexia** (left VWFA), **verbal memory
impairment** (left MTL), and **pure word deafness** (left/bilateral A1)
are **left-lateralized** functions of the left temporal lobe. They are
**absent** from right temporal lesions. They are documented in the left
temporal lobe module and are **explicitly not claimed here**.

Lateralization Notes
--------------------
This is the **right** temporal lobe. The lateralization landscape is
**strongly right-loaded for prosody, music, faces, non-verbal auditory
processing, spatial memory, and self-motion perception** — the **complement
of the left language hub**:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Prosody and emotional intonation** — right STG/STS; aprosodia
      follows right lesions.
    - **Music perception** — right auditory cortex; amusia follows right
      lesions.
    - **Face recognition (FFA, BA37)** — right fusiform; prosopagnosia
      follows right lesions.
    - **Non-verbal auditory processing** — right A2 and higher.
    - **Spatial declarative memory (right MTL)** — right entorhinal/
      perirhinal/hippocampal.
    - **Self-motion perception (MST)** — right-dominant.
    - **Social/emotional semantics (right BA38)** — right temporal pole.

*   **Left-Lateralized Functions (contrast — absent here):**
    - **Speech comprehension (Wernicke's area, BA22)** — left.
    - **Semantic memory (ATL, BA38)** — left-dominant for verbal concepts.
    - **Visual word form area (VWFA, BA37)** — left.
    - **Phonological processing (STG, MTG)** — left.
    - **Verbal declarative memory (left MTL)** — left.
    - **Sentence comprehension (left MTG, BA21)** — left.

*   **Symmetric Functions (bilateral properties of the temporal lobe,
    copied verbatim from the left twin):**
    - Primary auditory cortex (A1) — basic acoustic features.
    - Middle temporal visual area (MT) — motion processing.
    - Medial temporal lobe memory structures — gateway to hippocampus
      (with verbal/spatial split).
    - Piriform/olfactory cortex (BA27).
    - Temporal pole's basic structural organization.

**The temporal lobe pair is the strongest left-loaded pair in the brain.**
The right temporal lobe is **not** the mirror image of the left — it is
the **complementary hemisphere** for prosody, music, faces, and spatial
memory. A consumer that assumes "right temporal = left temporal" will
be **wrong for the majority of its highest-value functions**.

**A note on the "strongest left-loaded" framing.** The **temporal lobe
pair is weighted left** at the lobe level, because the left temporal lobe
carries the language hub (Wernicke's, semantic memory, VWFA, phonological
processing, verbal memory, sentence comprehension). The **right
temporal lobe carries complementary functions**, but they are **not
equally weighted in magnitude** — the language hub is functionally more
prominent and more clinically visible than the prosody/music/face hub.
This is the **"strongly left-loaded with right complement"** pattern —
distinct from the parietal lobe's **"parallel-laden"** pattern (BA39/
BA40/PPC), where both hemispheres carry roughly equal magnitude.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe (Broca's area, BA44/45) or the parietal lobe (angular
    gyrus, BA39). Those are **sibling lobes**.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Lobar aggregator, not a partition.** This module does **not**
    enumerate children directly; it is a **container** for the four
    partitions plus the standalone MST node.
*   **The `medial_superior_temporal_area` anomaly is documented, not
    resolved.** MST sits at the lobe level because it does not fit
    cleanly into any partition. **This is identical to the left.**
*   **The nested cross-listing is documented, not resolved.** BA22 lives
    under both `brodmann_areas/` and `gyri/superior_temporal_gyrus/
    wernickes_area/`. **The "Wernicke's area" name is inherited on the
    right, not functionally accurate** — the right BA22 is the right
    superior temporal auditory/prosodic cortex, not the speech-
    comprehension hub.
*   **Structural parity with left temporal lobe.** Left and right
    temporal lobe aggregators are **structurally identical** in their
    partition list, Brodmann area inventory, cortex region inventory,
    gyral inventory, sulcal inventory, standalone node, and nested
    cross-listing. Only the **lateralization prose** differs.

Usage
-----
Resolve partitions by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal import (
        PARTITIONS, BRODMANN_AREAS, CORTEX_REGIONS, GYRI, SULCI,
        STANDALONE_NODES, NESTED_CROSS_LISTINGS,
    )

    for partition in PARTITIONS:
        # partition is "brodmann_areas", "cortex", "gyri", or "sulci"
        ...

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.gyri.superior_temporal_gyrus.wernickes_area"
    )

For the nested cross-listing (BA22 as the right superior temporal
auditory/prosodic cortex — named "Wernicke's area" by inheritance)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 is the right BA22 (prosodic, not
    # speech-comprehension)

For the top-level Brodmann leaf::

    from ...temporal.brodmann_areas import brodmann_area_22
    # structurally identical cytoarchitectonic constants

For the standalone functional node::

    from ...temporal import medial_superior_temporal_area
    # MST — sibling of partitions, right-dominant for self-motion

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
*   **Prosody — right hemisphere dominance:** Ross, E.D. (1981). "The
    aprosodias: functional-anatomic organization of the affective
    components of language in the right hemisphere." *Arch Neurol*,
    38(9), 561–569.
*   **Music perception — right auditory cortex:** Zatorre, R.J., Belin, P.,
    & Penhune, V.B. (2002). "Structure and function of auditory cortex:
    music and speech." *Trends Cogn Sci*, 6(1), 37–46.
*   **Face recognition — FFA (right dominant):** Kanwisher, N., McDermott,
    J., & Chun, M.M. (1997). "The fusiform face area: a module in human
    extrastriate cortex specialized for face perception." *J Neurosci*,
    17(11), 4302–4311. Also: De Renzi, E., et al. (1994). "Prosopagnosia
    in a patient with an unremarkable brain." *Neuropsychologia* — right
    fusiform lesion cases.
*   **Spatial memory — right MTL:** Burgess, N., Maguire, E.A., &
    O'Keefe, J. (2002). "The human hippocampus and spatial and episodic
    memory." *Neuron*, 35(4), 625–641.
*   **Self-motion — right MST:** Cardin, V., et al. (2012). "Sensitivity
    of human visual area MT and MST to egomotion." *NeuroImage*, 63(4),
    1933–1943.
*   **Social/emotional semantics — right temporal pole:** Zahn, R., et al.
    (2007). "Social concepts are represented in the superior anterior
    temporal cortex." *PNAS*, 104(15), 6430–6435.
*   **Right temporal lobe epilepsy:** Vlooswijk, M.C.G., et al. (2011).
    "Memory processes and prefrontal network dysfunction in cryptogenic
    epilepsy." *Epilepsia*, 52(3), 497–506.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed.
*   NeuroNames — Temporal lobe (right); FMA — right temporal lobe
    partonomy.
"""