"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22
====================================================================================================================================================

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
                            └── wernickes_area
                                └── brodmann_area_22   <-- THIS MODULE

**Primary synonym:** Brodmann Area 22 (BA22), nested Wernicke's-area
framing; Left Wernicke's area (leaf level); Left superior temporal
speech-comprehension cortex.
**Cytoarchitectonic designation:** Area 22 of Brodmann (1909). **This is
the same cortical territory as the top-level leaf
``.../temporal/brodmann_areas/brodmann_area_22`` — not a separate field.**
**Part of:** The nested **Wernicke's-area** module
(``.../wernickes_area``), which is in turn a child of the
**superior temporal gyrus** (``.../superior_temporal_gyrus``).
**Location:** The **posterior superior temporal gyrus (STG)** of the left
hemisphere — the **left bank of the posterior Sylvian fissure** — on the
lateral temporal surface, extending onto the **superior temporal plane**.
**Structural parent:** ``.../wernickes_area`` (nested functionally named
region).
**Structural grandparent:** ``.../superior_temporal_gyrus`` (structural
convolution).
**Sibling (dual-framing) module:** ``.../temporal/brodmann_areas/brodmann_area_22``
(top-level cytoarchitectonic framing; structurally identical).
**Cytoarchitectonic type:** **Neocortical (parakoniocortical /
dysgranular)** — BA22 is a **higher-order auditory association cortex**
with a **less prominent layer IV** than the koniocortical A1 and a
**more developed layer III** for cortico-cortical output.

Overview
--------
This module is the **deepest level** of the **first three-level
structural hierarchy** in the entire brainparts tree, and it is the
**functional framing** of Brodmann Area 22 (BA22) in the left hemisphere.
It represents the **same cortical territory** as the top-level leaf
``.../temporal/brodmann_areas/brodmann_area_22``, but it accesses that
territory **through the Wernicke's-area nested path** and documents the
territory with a **functional framing** rather than a cytoarchitectonic
one.

**This is the first module in the tree whose identity is defined entirely
by its *position in a hierarchy* rather than by a novel cortical
territory.** The territory itself — Brodmann area 22 on the posterior
left superior temporal gyrus — has already been documented at the
top-level Brodmann leaf. This module documents the **same territory
through the nested Wernicke's-area path**, so that consumers who need
**functionally framed** access to BA22 (rather than cytoarchitectonically
framed access) have a first-class module to query.

**The "Wernicke's area" framing is a functional inheritance.** The
"Wernicke's area" name travels down the path
``superior_temporal_gyrus → wernickes_area → brodmann_area_22`` — the
gyrus is **structural**, the intermediate region is **functionally
named**, and the leaf is **cytoarchitectonic**. This module combines
both framings: the **cytoarchitectonic identity** of BA22 (from the leaf
name) with the **functional identity** of Wernicke's area (from the
parent's name).

**The nested leaf is the final piece of the dual-framing architecture.**
The tree provides **two complete access paths** to the same cortical
territory:

::

    Path A (cytoarchitectonic framing)       Path B (functional framing)
    ─────────────────────────────────        ──────────────────────────────
    temporal/brodmann_areas/                 temporal/gyri/superior_temporal_gyrus/
    └── brodmann_area_22                     └── wernickes_area/
        (top-level leaf)                         └── brodmann_area_22
                                                     (nested leaf; THIS MODULE)

**Both paths return the same cortical territory.** The top-level path
answers *"which cytoarchitectonic field is this?"* — the leaf's
**laminar organization, cell density, and thalamic input** are the
primary constants. The nested path answers *"which functionally named
language region is this?"* — the leaf's **speech-comprehension
functions, clinical syndrome, and language-network participation** are
the primary constants.

**On the right hemisphere, the same nested leaf exists structurally** —
but its functional content is **prosodic**, not speech-comprehension.
The right nested BA22 is the **right superior temporal auditory/prosodic
cortex**, and its damage produces **aprosodia**, not Wernicke's aphasia.

The Nested Dual-Framing Context
-------------------------------
This module is the **deepest level** of the three-level structural
hierarchy that is **bilateral** across the tree:

::

    Three-level structural hierarchy (left hemisphere)
    ──────────────────────────────────────────────────
    Level 1: superior_temporal_gyrus    (structural convolution)
    Level 2: wernickes_area              (nested functionally named region)
    Level 3: brodmann_area_22            (nested Brodmann leaf; THIS MODULE)

    Dual-framing counterpart (top-level)
    ────────────────────────────────────
    temporal/brodmann_areas/brodmann_area_22
    (cytoarchitectonic framing; same cortical territory)

**The two BA22 modules are structurally identical in their
cytoarchitectonic constants.** They represent the **same cortical
territory** with the **same laminar organization, cell density, and
thalamic input**. **Only the framing differs:**

*   **Top-level BA22** (`.../temporal/brodmann_areas/brodmann_area_22`)
    — **cytoarchitectonic framing**: BA22 as a **Brodmann field**,
    documented primarily by its **laminar organization, cell density,
    boundaries, and thalamic input**.
*   **Nested BA22** (this module) — **functional framing**: BA22 as the
    **posterior superior temporal language cortex** (Wernicke's area),
    documented primarily by its **speech-comprehension functions,
    clinical syndrome, and language-network participation**.

**Consumers must not assume that the top-level and nested BA22 modules
are different cortical territories.** They are the **same territory**
with **two framings**. The `DUAL_FRAMING` constant below makes this
explicit and greppable.

**The parent `wernickes_area` module is the intermediate level** of the
hierarchy — it is the **first nested functional region in the tree**,
and its role is to **bridge** the structural gyrus (Level 1) and the
nested Brodmann leaf (Level 3). This module (the nested BA22 leaf) is
the **leaf-level instantiation** of that intermediate region.

Cytoarchitecture
----------------
The nested BA22 leaf shares **all cytoarchitectonic constants** with the
top-level BA22 leaf. The cytoarchitecture is **summarized here for
reference**, but consumers that need **detailed cytoarchitectonic
constants** should query the top-level leaf
(``.../temporal/brodmann_areas/brodmann_area_22``), which documents the
laminar organization, cell density, and thalamic input in full.

*   **Parakoniocortical / dysgranular** — BA22 is a **higher-order
    auditory association cortex**. It has a **less prominent layer IV**
    than the koniocortical A1 (BA41/BA42) and a **more developed layer
    III** for cortico-cortical output.

*   **Laminar profile** — a **granular layer IV** is present but
    **thinner and less sharply delineated** than in A1. **Layer III**
    contains **large pyramidal cells** — the **principal output neurons**
    to the arcuate fasciculus, Broca's area, and the broader language
    network.

*   **Hemispheric asymmetry** — BA22 exhibits **interhemispheric
    microcircuitry differences** that accompany its **functional
    lateralization** (speech on the left, prosody on the right).

**This cytoarchitectonic profile is inherited from the top-level BA22
leaf** and is documented here only at the level of summary. Consumers
that need **detailed laminar constants** should query the top-level
leaf.

Function in the Human Brain
---------------------------
The nested BA22 leaf is the **leaf-level functional framing of
Wernicke's area**. Its best-supported functions cluster into six
domains — **identical to those documented in the parent
`wernickes_area` module**, but **instantiated at the leaf level**:

*   **Speech Comprehension (the defining function):** The nested BA22
    leaf is the **leaf-level substrate for the comprehension of written
    and spoken language**. It links **spoken words to their meanings**
    and is the **auditory-phonological end of the language network**.

*   **Lexical-Semantic Processing:** The nested BA22 leaf supports
    **lexical semantics** — the computation of the representation of the
    meaning of a word. Focal lesions in the posterior STG (BA22) produce
    **lexical-semantic deficits** (semantic errors in production and
    comprehension).

*   **Phonological Processing:** The nested BA22 leaf supports
    **phonological processing** — the analysis of speech sounds as
    linguistic units. It is the **auditory/phonological end of the
    arcuate fasciculus**, receiving input from primary auditory cortex
    and projecting to Broca's area for speech production.

*   **Naming and Word Retrieval:** The nested BA22 leaf is **highly
    involved in word comprehension and production**. Posterior BA22 is
    the area where activation is **most reliably correlated with both
    naming and comprehension**.

*   **Auditory Short-Term Memory and Repetition:** The nested BA22 leaf
    supports **auditory short-term memory** and **repetition** — the
    phonological loop component of language.

*   **Reading and Writing:** The nested BA22 leaf contributes to
    **reading** and **writing**, consistent with its role in linking
    phonological and semantic representations.

**These functions are the leaf-level instantiation of the parent
`wernickes_area` module's functions.** No new functional content is
introduced here — the module's role is to provide **leaf-level access**
to those functions via the nested Wernicke's-area path.

Associated Disorders
--------------------
Damage to or dysfunction of the nested BA22 leaf is associated with the
**same disorders as the parent `wernickes_area` module**:

*   **Wernicke's Aphasia (the signature syndrome):** The classical
    syndrome of **fluent but meaningless speech**, **impaired
    comprehension** of spoken and written language, **poor repetition**,
    and **unawareness of deficit**. This is the **definitional
    Wernicke's aphasia** — the same syndrome documented in the parent
    module and in the top-level BA22 leaf.

*   **Lexical-Semantic Deficits:** **Semantic errors** in production and
    comprehension, following focal lesions in the posterior STG (BA22).

*   **Pure Word Deafness:** Impaired **auditory comprehension of words**
    with preserved reading and writing, following **bilateral** or
    **left** lesions of BA22.

*   **Conduction Aphasia (with Arcuate Fasciculus Involvement):**
    **Impaired repetition** with relatively preserved comprehension,
    when BA22 damage extends to the arcuate fasciculus.

*   **Alexia (with Visual Word Form Area Involvement):** **Reading
    impairment** when BA22 damage extends to the left fusiform gyrus
    (BA37).

**What is NOT here:** **Prosody and emotional intonation** are **right
nested BA22** functions, not left. **Aprosodia** and **amusia** are
**right-hemisphere** syndromes. **Gerstmann syndrome** (left BA39),
**prosopagnosia** (right FFA), and **anomia** (left ITG) are **not**
nested-BA22 syndromes.

Lateralization Notes
--------------------
This is the **left** nested BA22 leaf. The lateralization landscape is
**strongly left-loaded for speech** — identical to the parent
`wernickes_area` module and the top-level BA22 leaf:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Speech comprehension** — the defining Wernicke's area function.
    - **Lexical-semantic processing** — linking spoken words to meanings.
    - **Phonological processing** — analysis of speech sounds.
    - **Naming and word retrieval**.
    - **Auditory short-term memory and repetition**.
    - **Reading and writing**.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Prosody and emotional intonation** — the right nested BA22 is
      the **right prosodic cortex**.
    - **Emotional vs. neutral prosody discrimination**.
    - **Aprosodia** — the right nested BA22 signature syndrome.

*   **Symmetric Functions (bilateral properties of BA22):**
    - **Auditory processing** of complex sounds (with left dominance for
      speech, right dominance for prosody).
    - **Basic acoustic feature analysis** (shared with BA41/42).
    - **Auditory memory** (bilateral component).

**This is the "left-loaded" pattern at its most extreme — the same
pattern already documented in the parent `wernickes_area` module and the
top-level BA22 leaf.** The nested BA22 leaf is the **leaf-level
instantiation** of that pattern, and it carries the **same left-loaded
lateralization** as its parent and its dual-framing sibling.

**A consumer that assumes "left nested BA22 = right nested BA22" will
be wrong for the entire speech-comprehension domain** — the left nested
BA22 is the speech hub; the right nested BA22 is the prosodic hub.
**Wernicke's aphasia is left-lateralized**; aprosodia is
**right-lateralized**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe (Broca's area, BA44/45) or the parietal lobe (angular
    gyrus, BA39). Those are **sibling lobes**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Nested-leaf status — flagged in data.** This module is the
    **deepest level** of the three-level structural hierarchy
    (STG → wernickes_area → BA22). The ``NESTED_LEVEL`` constant is
    **"brodmann_leaf"**.
*   **Dual-framing — flagged in data.** The top-level Brodmann leaf
    ``.../temporal/brodmann_areas/brodmann_area_22`` and this nested
    leaf represent the **same cortical territory** with **different
    framings**. The ``DUAL_FRAMING`` constant documents this.
*   **No novel cytoarchitectonic or functional content.** This module
    inherits its cytoarchitectonic and functional constants from the
    top-level BA22 leaf and the parent `wernickes_area` module. It
    exists to provide **leaf-level access via the nested Wernicke's-area
    path**.
*   **Left-lateralized speech functions — flagged in data.** The
    ``LEFT_LATERALIZED`` constant documents the left-lateralized speech
    functions.
*   **Right-specific prosodic warning — flagged in data.** The
    ``RIGHT_LATERALIZATION_WARNING`` constant makes the
    right-nested-BA22-is-prosodic distinction explicit and greppable.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri.superior_temporal_gyrus.wernickes_area import brodmann_area_22

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.gyri.superior_temporal_gyrus."
        "wernickes_area.brodmann_area_22"
    )

**This is the nested (functional) framing of BA22.** For the top-level
(cytoarchitectonic) framing of the **same cortical territory**::

    from ...temporal.brodmann_areas import brodmann_area_22

**Both paths return the same cortical territory.** Use the nested path
when you need the **Wernicke's-area functional framing**; use the
top-level path when you need the **Brodmann-field cytoarchitectonic
framing**.

For the dual-framing::

    from ...wernickes_area.brodmann_area_22 import DUAL_FRAMING
    # DUAL_FRAMING = {
    #     "top_level": "temporal.brodmann_areas.brodmann_area_22",
    #     "nested": "temporal.gyri.superior_temporal_gyrus."
    #               "wernickes_area.brodmann_area_22",
    #     "structurally_identical": True,
    # }

For the nested level::

    from ...wernickes_area.brodmann_area_22 import NESTED_LEVEL
    # NESTED_LEVEL = "brodmann_leaf"

For the left-lateralized functions::

    from ...wernickes_area.brodmann_area_22 import LEFT_LATERALIZED
    # LEFT_LATERALIZED = ("speech_comprehension",
    #                     "lexical_semantic_processing",
    #                     "phonological_processing",
    #                     "naming_and_word_retrieval",
    #                     "auditory_short_term_memory_and_repetition",
    #                     "reading_and_writing")

For the right-specific prosodic warning::

    from ...wernickes_area.brodmann_area_22 import RIGHT_LATERALIZATION_WARNING

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba22_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.superior_temporal_gyrus."
            f"wernickes_area.brodmann_area_22"
        )
        # resolve ba22_path through the memory/recall layer

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
*   **Lexical semantics and BA22:** *Lexical Semantics — an overview*
    (ScienceDirect). Focal lesions in the posterior STG (BA22) produce
    lexical-semantic deficits; both acute and chronic lesions often
    result in Wernicke's aphasia.
*   **Dual-framing (nested + top-level BA22):** *Wernicke's area — a
    review* (2018), *Brain Struct Funct*. The nested "Wernicke's area"
    framing coexists with the top-level "BA22" framing; both represent
    the **same cortical territory**.
*   **Cytoarchitecture (BA22):** *Interhemispheric Asymmetries of the
    Modular Structure in Human Temporal Cortex* (2000), *Science*.
    Language-relevant processing of auditory signals is lateralized and
    involves the **posterior part of Brodmann area 22**; functional
    lateralization is accompanied by **interhemispheric differences in
    intrinsic microcircuitry**.
*   **Right-hemisphere prosody (contrast):** Wildgruber, D., et al.
    (2005). "Identification of emotional intonation evaluated by fMRI."
    *NeuroImage*, 24(4), 1233–1241. Comprehension of affective prosody
    is bound to a **right-hemisphere pattern** including posterior STS
    (BA22).
*   **Arcuate fasciculus and language network:** Geschwind, N. (1970).
    "The organization of language and the brain." *Science*, 170(3961),
    940–944. (Classical model: Wernicke's area → arcuate fasciculus →
    Broca's area.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Lateral temporal and superior temporal plane
    anatomy.)
*   NeuroNames — Brodmann area 22 (left, nested Wernicke's-area framing);
    FMA — left posterior superior temporal gyrus.
"""