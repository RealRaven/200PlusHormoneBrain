"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri.superior_temporal_gyrus
=====================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── gyri
                        └── superior_temporal_gyrus   <-- THIS MODULE

**Primary synonym:** Superior temporal gyrus (STG), left; Left STG;
Gyrus temporalis superior; T1 (first temporal convolution); **Wernicke's
area** (its posterior extent).
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the **lateral and superior surface** of the temporal
lobe, forming the **superior wall of the Sylvian fissure**.
**Structural boundaries:** **Lateral sulcus / Sylvian fissure**
(superiorly, separating the STG from the frontal and parietal opercula)
and **superior temporal sulcus** (inferiorly, separating the STG from the
middle temporal gyrus). Its **superior surface** forms the **planum
temporale**, including **Heschl's gyrus** (the transverse temporal gyrus).
**Lobe membership:** **Temporal** — the STG is entirely within the
temporal lobe.
**Functional contents:** **A1** (primary auditory cortex; Heschl's gyrus;
BA41/BA42 in the *insular* partition), **A2** (secondary auditory cortex;
BA22 on the lateral STG), plus the **nested Wernicke's-area module**
(``wernickes_area/brodmann_area_22``). The STG is the **only gyrus in the
tree that contains a nested Brodmann child**.
**Cytoarchitectonic type:** **Neocortical** — koniocortical (A1, BA41)
transitioning to parakoniocortical/dysgranular (A2, BA22) along the
posterior-lateral axis.

Overview
--------
The **left superior temporal gyrus (STG)** is the **left-hemisphere
auditory and language convolution** — the **principal cortical substrate
for speech comprehension, auditory processing, and the early stages of
the language network**. It is the **most structurally complex gyrus in
the tree**, because it is the **only gyrus that contains a nested
Brodmann cross-listing** — the **Wernicke's-area module** at
``.../temporal/gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22``.

**The STG is the first structural leaf in the tree with a nested
Brodmann child.** This is the **defining architectural feature** of the
gyrus — a **three-level structural hierarchy** that no other gyrus in the
tree has:

1. **STG** — the structural convolution.
2. **wernickes_area** — the nested functionally named region.
3. **brodmann_area_22** — the nested Brodmann leaf.

**The nested Wernicke's-area module is the functional framing of BA22.**
The top-level Brodmann leaf ``.../temporal/brodmann_areas/brodmann_area_22``
and the nested leaf
``.../temporal/gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22``
both represent the **same cortical territory** — **Brodmann area 22**
(BA22). They differ only in **framing**:

*   **Top-level** — the **cytoarchitectonic** framing (BA22 as a Brodmann
    field, with its laminar organization and connectivity).
*   **Nested** — the **functional** framing (BA22 as **Wernicke's area**,
    the speech-comprehension hub).

**Consumers must not assume that the top-level and nested BA22 are
different cortical territories.** They are the **same territory** with
**two framings**. The nested path exists because the tree's authors
recognized that **different consumers ask different questions** —
cytoarchitectonic vs. functional — and both should be reachable.

**The STG is the structural home of the auditory and language systems.**
It contains:

*   **A1 (primary auditory cortex)** — on **Heschl's gyrus** (the
    transverse temporal gyrus on the superior surface of the STG).
*   **A2 (secondary auditory cortex)** — on the **lateral STG** (BA22).
*   **Wernicke's area** — the **nested functional framing** of the
    posterior STG (BA22).

**The STG is the first gyrus in the tree whose functional contents span
two functional regions (A1, A2) with a nested cross-listing (Wernicke's
area) embedded in one of them.** This is a **unique structural
configuration** — the auditory system (A1/A2) and the language system
(Wernicke's area) are **both embedded in the same gyrus**, but at
**different structural levels**.

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. It is
**not** a functional region and **not** a cytoarchitectonic field. Its
contents span **both** of those partitions:

::

    Structural leaf (this module)        Functional / cytoarchitectonic contents
    ─────────────────────────────        ────────────────────────────────────────
    superior_temporal_gyrus (left)  ──▶  primary_auditory_cortex
                                           (functional region; A1)
                                    ──▶  secondary_auditory_cortex
                                           (functional region; A2)
                                    ──▶  wernickes_area  (NESTED child)
                                           └── brodmann_area_22 (NESTED leaf)
                                    ──▶  brodmann_area_22  (top-level Brodmann leaf)
                                    ──▶  brodmann_area_41  (Heschl's gyrus; INSULAR)
                                    ──▶  brodmann_area_42  (Heschl's gyrus; INSULAR)

**The STG is the structural anchor for both the auditory system (A1/A2)
and the language system (Wernicke's area).** It is the **first gyrus in
the tree whose functional contents span two functional regions** (A1 and
A2) **with a nested cross-listing** (Wernicke's area) embedded in one of
them.

**The STG is also the first gyrus in the tree whose Brodmann constitution
spans TWO LOBES' partitions.** Its cytoarchitectonic contents include:

*   **BA22** — in the **temporal** partition.
*   **BA41 and BA42** — in the **insular** partition (per the tree's
    `brodmann_areas` assignment, following Brodmann's original grouping
    of BA41/BA42 with the posterior insula).

**Consumers must not assume that the STG's Brodmann fields live under the
temporal partition.** A1's primary cytoarchitectonic anchors (BA41/BA42)
live under the **insular** partition; only BA22 lives under the temporal
partition.

Cytoarchitecture: Koniocortex to Parakoniocortex
------------------------------------------------
The STG spans a **transitional cytoarchitectonic gradient** from the
**primary auditory koniocortex** (A1) to the **secondary auditory
parakoniocortex/dysgranular cortex** (A2):

*   **A1 (Heschl's gyrus; BA41/BA42 in the insular partition)** —
    **koniocortex** with a **prominent, densely packed layer IV** and a
    **dense band of cytochrome oxidase activity** in layer IV and the
    base of layer III. BA41 has a **more densely packed, narrower layer
    IV** than BA42.

*   **A2 (lateral STG; BA22)** — **parakoniocortical/dysgranular**
    cortex with a **less prominent layer IV** and a **more developed
    layer III** for cortico-cortical output.

*   **Wernicke's area (posterior STG; BA22)** — the **functionally
    defined language hub** at the **posterior end of the STG**, with the
    same cytoarchitecture as the rest of BA22 but a **distinct
    connectivity profile** that links it to the language network.

**This koniocortical-to-parakoniocortical gradient is the defining
structural fact about the STG.** The gyrus spans the **transition** from
the primary auditory koniocortex (A1) on its superior surface to the
secondary auditory parakoniocortex (A2) on its lateral surface, with
**Wernicke's area** at the posterior end. A consumer that applies uniform
koniocortical assumptions to the entire STG will be **wrong** — the gyrus
is a **gradient**.

Function in the Human Brain
---------------------------
The left STG is the **left-lateralized auditory and language hub**. Its
best-supported functions cluster into six domains:

*   **Speech Comprehension (Left-Lateralized — the defining left-STG
    function):** The **posterior STG (BA22; Wernicke's area)** is
    responsible for the **comprehension of written and spoken
    language**. Its damage produces **Wernicke's
    aphasia** — fluent but meaningless speech, impaired comprehension,
    poor repetition, and unawareness of deficit.

*   **Phonological and Auditory Speech Processing (Left-Lateralized):**
    The left STG is **best at processing fast temporal cues**,
    especially critical for speech. It supports
    **phonological processing** — the analysis of speech sounds as
    linguistic units — via the left A2 (BA22).

*   **Lexical-Semantic Processing (Left-Lateralized):** The left STG
    (BA22) is involved in **lexical semantics** — the computation of the
    representation of the meaning of a word. Focal lesions in the
    posterior STG (BA22) produce **lexical-semantic deficits**.

*   **Basic Acoustic Feature Analysis (Bilateral Foundation):** The
    **superior surface of the STG (Heschl's gyrus; A1)** performs
    **frequency, intensity, and duration analysis** of sound. This is a
    **bilateral** foundation with a leftward speech bias.

*   **Auditory Working Memory and Pattern Recognition (Bilateral):** The
    STG (A2; BA22) supports **auditory working memory** and **pattern
    recognition in the auditory domain**.

*   **Sentence Comprehension (Left-Lateralized):** The left STG
    contributes to **word sequence processing** and **sentence
    comprehension** via its connections to the adjacent MTG (BA21) and
    the broader language network.

Associated Disorders
--------------------
Damage to or dysfunction of the left STG is associated with:

*   **Wernicke's Aphasia (Left-Lateralized — the signature left-STG
    syndrome):** The classical syndrome of **fluent but meaningless
    speech**, **impaired comprehension** of spoken and written language,
    **poor repetition**, and **unawareness of deficit**. This is the
    **most important clinical syndrome in the STG**.

*   **Pure Word Deafness (Left-Lateralized):** Impaired **auditory
    comprehension of words** with preserved reading and writing,
    following **left or bilateral lesions** of the posterior STG / A1.

*   **Lexical-Semantic Deficits (Left-Lateralized):** **Semantic errors**
    in production and comprehension, following focal lesions in the
    posterior STG.

*   **Impaired Phoneme Discrimination (Left-Lateralized):** **Disordered
    perception of stop consonants** (b, d, g, p, t, k), which contain
    rapidly changing auditory information.

**What is NOT here:** **Prosody and amusia** are **right STG**
functions, not left STG functions. **Alexia** (left VWFA, fusiform
gyrus), **prosopagnosia** (right FFA, fusiform gyrus), and **anomia**
(left ITG) are **not** STG syndromes. The left STG is the **speech and
auditory** pole; the right STG is the **prosody and music** pole.

Lateralization Notes
--------------------
This is the **left** STG module. The lateralization landscape is
**left-loaded with right complement** — a **dominance-based split**
where the left STG is the **core speech-comprehension hub** and the
right STG carries **prosodic and musical** functions:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Speech comprehension (Wernicke's area)**.
    - **Phonological processing** — fast temporal cues for speech.
    - **Lexical-semantic processing** — word meaning.
    - **Sentence comprehension**.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Prosody and emotional intonation** — the right STG is engaged
      in prosodic processing.
    - **Music perception** — the right auditory cortex is dominant for
      music.
    - **Aprosodia** — the right-STG signature syndrome.

*   **Symmetric Functions (bilateral properties of the STG):**
    - Basic acoustic feature analysis (A1).
    - Auditory working memory and pattern recognition.
    - Contralateral ear representation (both hemispheres represent the
      contralateral ear more strongly).

**This is the "left-loaded with right complement" pattern at the
structural level** — the gyral leaf mirrors the BA22 Brodmann leaf's
division of labor. The left STG is the **dominant speech-comprehension
hub**; the right STG carries the **complementary prosodic and musical**
functions.

**The nested Wernicke's-area module is left-lateralized in its
functional framing.** On the left, the nested BA22 is **Wernicke's area**
— the speech-comprehension hub. On the right, the **same nested path**
exists structurally, but the functional content is **prosodic**. A
consumer that assumes right BA22 lesions produce Wernicke's aphasia will
be **wrong** — Wernicke's aphasia is **left-lateralized**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    insular lobe (BA41/BA42) or the parietal lobe. Those are
    **cross-lobe references**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural leaf with a nested Brodmann child — flagged in data.**
    The ``wernickes_area`` module is a **nested functionally named
    region** containing a **nested Brodmann leaf** (BA22). The
    ``NESTED_CROSS_LISTING`` constant documents this three-level
    structural hierarchy.
*   **Cross-lobe Brodmann mapping — flagged in data.** The STG's
    functional contents span **two lobes' partitions**: A1's BA41/BA42
    are in the **insular** partition; A2's BA22 is in the **temporal**
    partition. The ``BRODMANN_PARTITION_SPAN`` constant documents this.
*   **Koniocortical-to-parakoniocortical gradient — flagged in data.**
    The STG spans a **transitional cytoarchitectonic gradient** from
    koniocortex (A1) to parakoniocortex (A2). The
    ``CYTOARCHITECTONIC_GRADIENT`` constant documents this.
*   **Left-loaded with right complement — flagged in data.** The left
    STG is the **speech-comprehension** pole; the right STG is the
    **prosody and music** pole.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri import superior_temporal_gyrus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.gyri.superior_temporal_gyrus"
    )

For the nested Wernicke's-area framing (functionally named)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 — Wernicke's area, functionally framed

For the functional regions the STG contains::

    from ...temporal.cortex import (
        primary_auditory_cortex,      # A1
        secondary_auditory_cortex,    # A2
    )

For the top-level Brodmann leaf (BA22, cytoarchitectonic framing)::

    from ...temporal.brodmann_areas import brodmann_area_22

For the nested cross-listing::

    from ...temporal.gyri.superior_temporal_gyrus import NESTED_CROSS_LISTING
    # NESTED_CROSS_LISTING["wernickes_area"] = {
    #     "top_level": "temporal.brodmann_areas.brodmann_area_22",
    #     "nested": "temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22",
    # }

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        stg_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.superior_temporal_gyrus"
        )
        # resolve stg_path through the memory/recall layer

References
----------
*   **STG anatomy and boundaries:** *Superior Temporal Gyrus — an
    overview* (ScienceDirect). The STG is bounded superiorly by the
    **Sylvian fissure** and inferiorly by the **superior temporal
    sulcus**; its superior surface is the **planum temporale**,
    including **Heschl's gyrus**.
*   **Heschl's gyrus and A1:** *Heschl's gyrus — an overview*
    (ScienceDirect). The primary auditory cortex is located on the
    **posteromedial two-thirds of the first transverse temporal gyrus
    (Heschl's gyrus)**.
*   **Wernicke's area:** Wernicke, C. (1874). *Der aphasische
    Symptomencomplex*. (Wernicke's area on the posterior STG; damage
    produces Wernicke's aphasia.)
*   **Wernicke's area overview:** *Neuroanatomy, Wernicke Area* (2023),
    StatPearls, NCBI Bookshelf NBK533001. Wernicke area is located in
    **Brodmann area 22**, the posterior segment of the superior temporal
    gyrus in the dominant hemisphere; responsible for **comprehension
    of written and spoken language**.
*   **BA22 and lexical semantics:** *Lexical Semantics — an overview*
    (ScienceDirect). Focal lesions in the posterior STG (BA22) produce
    **lexical-semantic deficits**.
*   **Right STG prosody (contrast):** Ross, E.D. (1981). "The
    aprosodias: functional-anatomic organization of the affective
    components of language in the right hemisphere." *Arch Neurol*,
    38(9), 561–569. Right posterior STG damage produces **aprosodia**,
    not aphasia.
*   **Pure word deafness:** *Pure word deafness after bilateral primary
    auditory cortex infarcts* (Neurology). **Pure word deafness** is
    associated with **bilateral infarctions of the primary auditory
    cortex**.
*   **Heschl's gyrus koniocortex:** *Temporal Gyrus — an overview*
    (ScienceDirect). **BA41 and BA42** are the primary auditory cortex
    with **tonotopic representation**; **BA41 has a denser layer IV**
    than BA42.
*   **Nested Wernicke's-area leaf:** *Wernicke's area — a review* (2018),
    *Brain Struct Funct*. The nested "Wernicke's area" framing
    coexists with the top-level "BA22" framing; both represent the
    **same cortical territory**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Lateral temporal and superior temporal plane
    anatomy.)
*   NeuroNames — Superior temporal gyrus (left); FMA — left superior
    temporal gyrus partonomy.
"""