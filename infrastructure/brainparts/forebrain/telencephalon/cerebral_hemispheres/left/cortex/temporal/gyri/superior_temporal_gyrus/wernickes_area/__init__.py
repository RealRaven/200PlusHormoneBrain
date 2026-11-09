"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri.superior_temporal_gyrus.wernickes_area
=====================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── gyri
                        └── superior_temporal_gyrus
                            └── wernickes_area   <-- THIS MODULE

**Primary synonym:** Wernicke's area (left); Wernicke's speech area;
Sensory speech area; Posterior superior temporal language cortex.
**Organizing principle:** **Nested functionally named region** — the
**first nested functional region in the entire brainparts tree**, sitting
between the structural gyrus (``superior_temporal_gyrus``) and the
cytoarchitectonic field (``brodmann_area_22``).
**Brodmann constitution:** **BA22** (the posterior superior temporal
gyrus) — accessed via the **nested leaf**
``wernickes_area/brodmann_area_22``. The **top-level Brodmann leaf**
``.../temporal/brodmann_areas/brodmann_area_22`` represents the same
cortical territory with a **cytoarchitectonic framing**.
**Location:** The **posterior segment of the left superior temporal
gyrus (STG)** on the lateral surface of the temporal lobe, on the **left
bank of the posterior Sylvian fissure**.
**Structural parent:** Child of ``.../superior_temporal_gyrus`` (the
structural gyrus).
**Structural child:** Contains ``brodmann_area_22`` as a **nested leaf**.
**Cytoarchitectonic type:** **Neocortical (parakoniocortical /
dysgranular)** — Wernicke's area is **BA22**, a **higher-order auditory
association cortex** with a **less prominent layer IV** than the
koniocortical A1 and a **more developed layer III** for cortico-cortical
output.

Overview
--------
The **left Wernicke's area** is the **classical speech-comprehension hub**
— the **most famous functionally named region in the human brain**, and
the **cortical substrate for the comprehension of written and spoken
language**. It is the **definitional Wernicke's area** — the clinical,
anatomical, and functional anchor for the left-hemisphere language
network — and its damage produces the **most important clinical syndrome
in the temporal lobe**: **Wernicke's aphasia** (fluent but meaningless
speech, impaired comprehension, poor repetition, and unawareness of
deficit).

**Wernicke's area is the intermediate level of the first three-level
structural hierarchy in the tree.** The tree's authors chose to make
Wernicke's area a **nested region** — rather than only a **Brodmann
leaf** or only a **functional concept** — because the tree's architecture
required a **structurally addressable region between the gyrus and the
Brodmann field**:

::

    Three-level structural hierarchy
    ────────────────────────────────
    Level 1: superior_temporal_gyrus    (structural convolution)
    Level 2: wernickes_area              (nested functionally named region)
    Level 3: brodmann_area_22            (nested Brodmann leaf)

**This is the first nested functional region in the tree.** No other
module in the tree has a **three-level structural hierarchy** with a
**functionally named intermediate level**. The STG leaf (``.../
superior_temporal_gyrus``) documents the **three-level hierarchy from
above**; this module (``wernickes_area``) documents it **at the
intermediate level**; and the nested BA22 leaf (``.../
wernickes_area/brodmann_area_22``) documents it **at the deepest
level**.

**Wernicke's area is the functional framing of BA22.** The top-level
Brodmann leaf ``.../temporal/brodmann_areas/brodmann_area_22`` and the
nested leaf ``.../wernickes_area/brodmann_area_22`` represent the **same
cortical territory** — **Brodmann area 22**. They differ only in
**framing**:

*   **Top-level BA22** — the **cytoarchitectonic** framing (BA22 as a
    Brodmann field, with its laminar organization and connectivity).
*   **Nested BA22** — the **functional** framing (BA22 as **Wernicke's
    area**, the speech-comprehension hub).

**Wernicke's area is the bridge between A1 and the broader language
network.** The classical model (Wernicke, 1874; Dejerine; Geschwind)
positions Wernicke's area between the **primary auditory cortex (A1)**
and the **motor speech area (Broca's area, BA44/45)** — receiving
auditory phonological representations from A1 and transmitting them via
the **arcuate fasciculus** to Broca's area for speech production. This
model remains the **canonical functional architecture** of the left
language network, even though it has been refined by modern connectivity
studies.

The Nested Dual-Framing Context
-------------------------------
Wernicke's area is the **intermediate level** of a **dual-framing
hierarchy** that spans **three modules** in the tree:

::

    top-level Brodmann leaf                    nested level
    ───────────────────────────────────        ──────────────────────────────
    temporal/brodmann_areas/                    temporal/gyri/superior_temporal_gyrus/
    └── brodmann_area_22      ←── SAME ──→       └── wernickes_area/
        (cytoarchitectonic framing)                  └── brodmann_area_22
                                                         (functional framing)

**The two BA22 modules are structurally identical in their
cytoarchitectonic constants** — they represent the **same cortical
territory** with the **same laminar organization, cell density, and
thalamic input**. **Only the functional framing differs**:

*   **Top-level BA22** — answers *"which Brodmann field is this?"* — a
    cytoarchitectonic question.
*   **Nested Wernicke's area** — answers *"which functionally named
    language region is this?"* — a functional question.

**Consumers must not assume that the top-level and nested modules are
different cortical territories.** They are the **same territory** with
**two framings**. The nested path exists because the tree's authors
recognized that **different consumers ask different questions** —
cytoarchitectonic vs. functional — and both should be reachable.

**On the right hemisphere, the same nested structure exists** — but the
**functional content differs**: the right nested "Wernicke's area" is
the **right superior temporal auditory/prosodic cortex**, not the
speech-comprehension hub. A consumer that assumes the right nested
module is Wernicke's area will be **clinically wrong** — right BA22
lesions produce **aprosodia**, not Wernicke's aphasia.

Function in the Human Brain
---------------------------
The left Wernicke's area is the **core speech-comprehension hub**. Its
best-supported functions cluster into six domains:

*   **Speech Comprehension (the defining function):** Wernicke's area
    is responsible for the **comprehension of written and spoken
    language**. It is the **auditory-phonological end of the language
    network**, linking spoken words to their meanings. Chronic lesion
    studies have long pointed to an essential role of left BA22 in
    **linking spoken words to their meanings**.

*   **Lexical-Semantic Processing:** Wernicke's area is involved in
    **lexical semantics** — the computation of the representation of the
    meaning of a word. Focal lesions in the posterior STG (BA22) produce
    **lexical-semantic deficits** (semantic errors in production and
    comprehension).

*   **Phonological Processing:** Wernicke's area is involved in
    **phonological processing** — the analysis of speech sounds as
    linguistic units. It is the **auditory/phonological end of the
    arcuate fasciculus**, receiving input from primary auditory cortex
    and projecting to Broca's area for speech production.

*   **Naming and Word Retrieval:** Wernicke's area is **highly involved
    in word comprehension and production**. Posterior BA22 is the area
    where activation is **most reliably correlated with both naming and
    comprehension**. Reperfusion of BA22 is significantly
    associated with improvement in **spoken word comprehension**.

*   **Auditory Short-Term Memory and Repetition:** Wernicke's area
    supports **auditory short-term memory** and **repetition** — the
    phonological loop component of language. Its damage produces the
    **poor repetition** that is a hallmark of Wernicke's aphasia.

*   **Reading and Writing:** Wernicke's area contributes to **reading**
    and **writing**, consistent with its role in linking phonological
    and semantic representations. Lesions impair **reading
    comprehension** alongside spoken language comprehension.

Associated Disorders
--------------------
Damage to or dysfunction of the left Wernicke's area is associated with:

*   **Wernicke's Aphasia (the signature syndrome):** The classical
    syndrome of **fluent but meaningless speech**, **impaired
    comprehension** of spoken and written language, **poor repetition**,
    and **unawareness of deficit**. The patient's words lack
    meaning, and they cannot understand what is being said to them.
    This is the **most important clinical syndrome in the temporal lobe**
    and the **definitional Wernicke's aphasia**.

*   **Lexical-Semantic Deficits:** **Semantic errors** in production and
    comprehension, following focal lesions in the posterior STG (BA22).
    These deficits are a component of the Wernicke's aphasia spectrum.

*   **Pure Word Deafness:** Impaired **auditory comprehension of words**
    with preserved reading and writing, following **bilateral** or
    **left** lesions of BA22 and adjacent auditory cortex.

*   **Conduction Aphasia (with Arcuate Fasciculus Involvement):**
    **Impaired repetition** with relatively preserved comprehension,
    when Wernicke's area damage extends to the arcuate fasciculus. This
    is a **left-perisylvian** syndrome.

*   **Alexia (with Visual Word Form Area Involvement):** **Reading
    impairment** when Wernicke's area damage extends to the left
    fusiform gyrus (BA37). This is a **left-lateralized** syndrome.

**What is NOT here:** **Prosody and emotional intonation** are **right
nested "Wernicke's-area"** functions, not left. **Aprosodia** and
**amusia** are **right-hemisphere** syndromes. **Gerstmann syndrome**
(left BA39) and **prosopagnosia** (right FFA) are **not** Wernicke's
area syndromes. The left Wernicke's area is the **speech-comprehension
hub**; the right nested module is the **prosodic hub**.

Lateralization Notes
--------------------
This is the **left** Wernicke's-area module. The lateralization landscape
is **strongly left-loaded for speech** — the most asymmetric functional
region in the entire tree:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Speech comprehension** — the definitional Wernicke's area
      function.
    - **Lexical-semantic processing** — linking spoken words to meanings.
    - **Phonological processing** — analysis of speech sounds.
    - **Naming and word retrieval**.
    - **Auditory short-term memory and repetition**.
    - **Reading and writing**.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Prosody and emotional intonation** — the right nested
      "Wernicke's-area" is the **right prosodic cortex**.
    - **Emotional vs. neutral prosody discrimination**.
    - **Aprosodia** — the right-nested-module signature syndrome.
    - **Amusia** — music perception deficit (right STG/MTG).

*   **Symmetric Functions (bilateral properties of BA22):**
    - **Auditory processing** of complex sounds (with left dominance for
      speech, right dominance for prosody).
    - **Basic acoustic feature analysis** (shared with BA41/42).
    - **Auditory memory** (bilateral component).

**This is the "left-loaded" pattern at its most extreme.** The left
Wernicke's area is the **core speech-comprehension hub**; the right
nested "Wernicke's-area" module is the **prosodic and emotional-intonation
cortex**. The asymmetry is **not** a division of equal labor (like
BA20's lexical vs. metaphor split) and **not** a left-dominance-with-
right-complement (like BA21's semantic vs. prosody split). **The left
nested module is the functionally dominant language area; the right
nested module is the functionally dominant prosody area.** Each
hemisphere has a **dominant specialization**, but they are **different
specializations**, and the left's is the one that defines the clinical
syndrome.

**A consumer that assumes "left Wernicke's area = right Wernicke's
area" will be wrong for the entire speech-comprehension domain** — the
left Wernicke's area is the speech hub; the right nested "Wernicke's
area" is not. Wernicke's aphasia is **left-lateralized**; right nested
"Wernicke's-area" lesions produce **aprosodia**, not aphasia.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe (Broca's area, BA44/45) or the parietal lobe (angular
    gyrus, BA39). Those are **sibling lobes**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Nested functional region — flagged in data.** This module is the
    **intermediate level** of the three-level structural hierarchy
    (STG → wernickes_area → BA22). The ``NESTED_LEVEL`` constant is
    **"functional_region"**.
*   **Dual-framing — flagged in data.** The top-level Brodmann leaf
    ``.../temporal/brodmann_areas/brodmann_area_22`` and the nested leaf
    ``.../wernickes_area/brodmann_area_22`` represent the **same cortical
    territory** with **different framings**. The ``DUAL_FRAMING``
    constant documents this.
*   **Structural child.** The module **contains** the nested
    ``brodmann_area_22`` leaf. The ``NESTED_CHILD`` constant documents
    this.
*   **Left-lateralized speech functions — flagged in data.** The
    ``LEFT_LATERALIZED`` constant documents the left-lateralized speech
    functions.
*   **Right-specific prosodic warning — flagged in data.** The
    ``RIGHT_LATERALIZATION_WARNING`` constant makes the
    right-nested-module-is-prosodic distinction explicit and greppable.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri.superior_temporal_gyrus import wernickes_area

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.gyri.superior_temporal_gyrus.wernickes_area"
    )

For the nested BA22 leaf (the deepest level)::

    from ...temporal.gyri.superior_temporal_gyrus.wernickes_area import brodmann_area_22

For the top-level BA22 leaf (the cytoarchitectonic framing)::

    from ...temporal.brodmann_areas import brodmann_area_22

**Both paths return the same cortical territory.** The top-level path
is the **cytoarchitectonic framing**; the nested path is the
**Wernicke's-area framing**.

For the nested level::

    from ...temporal.gyri.superior_temporal_gyrus.wernickes_area import NESTED_LEVEL, NESTED_CHILD
    # NESTED_LEVEL = "functional_region"
    # NESTED_CHILD = "brodmann_area_22"

For the dual-framing::

    from ...temporal.gyri.superior_temporal_gyrus.wernickes_area import DUAL_FRAMING
    # DUAL_FRAMING = {
    #     "top_level": "temporal.brodmann_areas.brodmann_area_22",
    #     "nested": "temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22",
    #     "structurally_identical": True,
    # }

For the left-lateralized functions::

    from ...temporal.gyri.superior_temporal_gyrus.wernickes_area import LEFT_LATERALIZED
    # LEFT_LATERALIZED = ("speech_comprehension",
    #                     "lexical_semantic_processing",
    #                     "phonological_processing",
    #                     "naming_and_word_retrieval",
    #                     "auditory_short_term_memory_and_repetition",
    #                     "reading_and_writing")

For the right-specific prosodic warning::

    from ...temporal.gyri.superior_temporal_gyrus.wernickes_area import RIGHT_LATERALIZATION_WARNING

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        wa_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.superior_temporal_gyrus.wernickes_area"
        )
        # resolve wa_path through the memory/recall layer

References
----------
*   **Wernicke's original description:** Wernicke, C. (1874). *Der
    aphasische Symptomencomplex*. (Classical description of sensory
    aphasia and its localization to the posterior superior temporal
    gyrus.)
*   **Wernicke's area overview:** *Neuroanatomy, Wernicke Area* (2023),
    StatPearls, NCBI Bookshelf NBK533001. Wernicke area is located in
    **Brodmann area 22**, the posterior segment of the superior temporal
    gyrus in the dominant hemisphere; responsible for **comprehension
    of written and spoken language**; damage produces **fluent but
    receptive aphasia**.
*   **Lexical semantics and Wernicke's aphasia:** *Lexical Semantics — an
    overview* (ScienceDirect). Focal lesions in the posterior STG (BA22)
    produce lexical-semantic deficits; both acute and chronic lesions
    often result in Wernicke's aphasia.
*   **Core vs extended Wernicke's area:** Ardila, A., et al. (2016).
    "How Extended Is Wernicke's Area? Meta-Analytic Connectivity Study
    of BA20 and Integrative Proposal." *Neurosci J*, 2016, 4962562.
    Core Wernicke's area ≈ BA21, BA22, BA41, BA42; extended Wernicke's
    area ≈ BA20, BA37, BA38, BA39, BA40.
*   **Right-hemisphere prosody (contrast):** Wildgruber, D., et al.
    (2005). "Identification of emotional intonation evaluated by fMRI."
    *NeuroImage*, 24(4), 1233–1241. Comprehension of affective prosody
    is bound to a **right-hemisphere pattern** including posterior STS
    (BA22).
*   **Nested Wernicke's-area leaf:** *Wernicke's area — a review* (2018),
    *Brain Struct Funct*. The nested "Wernicke's area" framing
    coexists with the top-level "BA22" framing; both represent the
    **same cortical territory**.
*   **Arcuate fasciculus and language network:** Geschwind, N. (1970).
    "The organization of language and the brain." *Science*,
    170(3961), 940–944. (Classical model: Wernicke's area → arcuate
    fasciculus → Broca's area.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Lateral temporal and superior temporal plane
    anatomy.)
*   NeuroNames — Wernicke's area (left); FMA — left Wernicke's area
    partonomy.
"""