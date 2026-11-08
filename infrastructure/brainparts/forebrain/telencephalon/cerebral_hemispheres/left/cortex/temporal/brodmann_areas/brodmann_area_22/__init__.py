"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.brodmann_areas.brodmann_area_22
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── brodmann_areas
                        └── brodmann_area_22   <-- THIS MODULE

**Primary synonym:** Brodmann Area 22 (BA22); **Wernicke's area**;
Wernicke's speech area; Sensory speech area; Area temporalis superior.
**Cytoarchitectonic designation:** Area 22 of Brodmann (1909).
**Part of:** **Core Wernicke's area** — the language auditory processing
area in the left hemisphere, alongside **BA21, BA41, and BA42**
.
**Location:** The **posterior segment of the superior temporal gyrus**
(STG) in the dominant (left) hemisphere, encompassing the auditory
cortex on the lateral sulcus . BA22
extends over the **posterior two-thirds of the STG** up to the beginning
of the vertical branch of the lateral fissure
.
**Structural parent:** This is a **Brodmann leaf** under
`.../temporal/brodmann_areas/`, **and** it has a **nested cross-listing**
under `.../gyri/superior_temporal_gyrus/wernickes_area/`.
**Lateralization status:** **The most strongly left-lateralized cortical
area in the human brain** for language comprehension; the right BA22 is
the **right superior temporal auditory/prosodic cortex**, not the
speech-comprehension hub.

Overview
--------
Brodmann Area 22 (BA22) is **Wernicke's area** — the **posterior
superior temporal gyrus** and the **core substrate for speech
comprehension** in the left hemisphere. It was first described by Carl
Wernicke in 1874, who identified it as one of the two cortical areas
that manage speech (the other being Broca's area)
. BA22 encompasses the **auditory association cortex**
on the lateral sulcus and is responsible for the **comprehension of
written and spoken language** .

**This is the single most important leaf module in the entire temporal
lobe.** BA22 is the **definitional Wernicke's area** — the clinical,
anatomical, and functional anchor for the left-hemisphere language
network. Its lesion produces the classical **Wernicke's aphasia**
(fluent but meaningless speech, impaired comprehension, poor repetition,
and unawareness of deficit) . It is the
**auditory-phonological end of the arcuate fasciculus**, receiving
input from primary auditory cortex (BA41/42) and projecting to Broca's
area (BA44/45) for speech production .

**BA22 is the first module in the entire tree with a NESTED CROSS-LISTING
— a dual-framing architecture.** It lives under **both**:

1. `brodmann_areas/brodmann_area_22` (this module) — the
   **cytoarchitectonic framing**: BA22 as a Brodmann field, with its
   laminar organization, boundaries, and connectivity.
2. `gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22` — the
   **functional framing**: BA22 as **Wernicke's area**, the speech-
   comprehension hub, used by consumers that need the aphasia syndrome
   and the language network.

**Both are BA22.** They are the **same cortical territory** with
**different framings**. This is **not** the same as the BA3 cross-listing
in the parietal lobe, where BA3 lives **only** under the postcentral
gyrus and is resolved via `AREA_PATHS`. **BA22 has two modules** because
the tree's authors recognized that **different consumers ask different
questions**: cytoarchitectonic vs. functional.

**On the right hemisphere, the same nested structure exists**, but the
**functional content differs**: the right BA22 is the right superior
temporal auditory/prosodic cortex, not the speech-comprehension hub. The
"Wernicke's area" name is inherited structurally on the right, not
functionally. A consumer that assumes right BA22 lesions produce
Wernicke's aphasia will be **wrong** — Wernicke's aphasia is **left-
lateralized**.

Nested BA22 Cross-Listing
-------------------------
**BA22 is the first area in the tree with a nested cross-listing** — a
Brodmann field that lives under **both** `brodmann_areas/` **and** a
gyral path:

::

    brodmann_areas/
    └── brodmann_area_22      <-- the top-level Brodmann leaf (this module)

    gyri/
    └── superior_temporal_gyrus/
        └── wernickes_area/
            └── brodmann_area_22   <-- the nested Wernicke's-area leaf

**Resolution contract for consumers:**

*   If you need **BA22 as a cytoarchitectonic field**, use this module
    (`brodmann_areas/brodmann_area_22`). It documents the **laminar
    organization, boundaries, and connectivity** of BA22 as a Brodmann
    field.
*   If you need **Wernicke's area as a functionally named region**, use
    the nested module (`gyri/superior_temporal_gyrus/wernickes_area/
    brodmann_area_22`). It documents the **speech-comprehension syndrome,
    the arcuate fasciculus connectivity, and the aphasia literature**.
*   **Both are correct.** The two modules are **structurally identical**
    in their cytoarchitectonic constants; only the **functional framing**
    differs.
*   **Do not** assume that the top-level and nested modules are different
    cortical territories. They are the **same territory** with **two
    framings**.

**The nested cross-listing is documented as data, not as a structural
parent.** The `NESTED_CROSS_LISTINGS` constant below makes the dual-
framing explicit and greppable.

Core Wernicke's Area Context
----------------------------
Ardila et al. (2016) distinguished between **core Wernicke's area**
(BA21, BA22, BA41, BA42) and **extended Wernicke's area** (BA20, BA37,
BA38, BA39, BA40) . **BA22 is a core
Wernicke's field** — the auditory language comprehension zone that the
classical model places at the center of speech comprehension.

**Historical context:** Wernicke (1874) first described the sensory
speech area in the posterior superior temporal gyrus. Since then, the
auditory language processing area has been generally equated with the
**first temporal gyrus** of the left hemisphere, and most authors included
in the temporal segment of the language area the **first and sometimes
also the second temporal gyrus** — in general corresponding to **BA21
and BA22** . BA22 is therefore part of
the **classical Wernicke's area** by both historical and modern
connectivity-based criteria.

Function in the Human Brain
---------------------------
The left BA22 is the **core auditory-semantic and speech-comprehension
hub**. Its best-supported functions cluster into six domains:

*   **Speech Comprehension (Left-Lateralized — the principal left-BA22
    function):** BA22 is responsible for the **comprehension of written
    and spoken language** . It is the **auditory-
    phonological end of the language network**, linking spoken words to
    their meanings . Chronic lesion studies
    have long pointed to an essential role of left BA22 in **linking
    spoken words to their meanings** .

*   **Lexical-Semantic Processing (Left-Lateralized):** BA22 is involved
    in **lexical semantics** — the computation of the representation of
    the meaning of a word . Focal lesions in the
    posterior STG (BA22) produce **lexical-semantic deficits** (semantic
    errors in production and comprehension) . Both acute
    and chronic lesions of left BA22 often result in **Wernicke's
    aphasia** .

*   **Phonological Processing (Left-Lateralized):** BA22 is involved in
    **phonological processing** — the analysis of speech sounds as
    linguistic units . It is the **auditory/phonological
    end of the arcuate fasciculus**, receiving input from primary
    auditory cortex and projecting to Broca's area for speech
    production .

*   **Naming and Word Retrieval (Left-Lateralized):** BA22 is
    **highly involved in word comprehension and production**
    . Posterior BA22 is the area where
    activation is **most reliably correlated with both naming and
    comprehension** . Reperfusion of BA22 is
    significantly associated with improvement in **spoken word
    comprehension** .

*   **Auditory Short-Term Memory and Repetition (Left-Lateralized):**
    BA22 supports **auditory short-term memory** and **repetition** —
    the phonological loop component of language. Its damage produces
    the **poor repetition** that is a hallmark of Wernicke's aphasia
    .

*   **Reading and Writing (Left-Lateralized):** BA22 contributes to
    **reading** and **writing**, consistent with its role in linking
    phonological and semantic representations. Lesions impair
    **reading comprehension** alongside spoken language comprehension
    .

Associated Disorders
--------------------
Damage to or dysfunction of the left BA22 is associated with:

*   **Wernicke's Aphasia (Left-Lateralized — the signature left-BA22
    syndrome):** The classical syndrome of **fluent but meaningless
    speech**, **impaired comprehension** of spoken and written language,
    **poor repetition**, and **unawareness of deficit**
    . The patient's words lack meaning, and they
    cannot understand what is being said to them . This is the **most
    important clinical syndrome in the temporal lobe**.

*   **Lexical-Semantic Deficits (Left-Lateralized):** **Semantic errors**
    in production and comprehension, following focal lesions in the
    posterior STG (BA22) . These deficits are
    **left-lateralized** and are a component of the Wernicke's aphasia
    spectrum.

*   **Pure Word Deafness (Bilateral or Left-Lateralized):** Impaired
    **auditory comprehension of words** with preserved reading and
    writing, following **bilateral** or **left** lesions of BA22 and
    adjacent auditory cortex.

*   **Conduction Aphasia (with Arcuate Fasciculus Involvement):**
    **Impaired repetition** with relatively preserved comprehension,
    when BA22 damage extends to the arcuate fasciculus. This is a
    **left-perisylvian** syndrome.

*   **Alexia (with Visual Word Form Area Involvement):** **Reading
    impairment** when BA22 damage extends to the left fusiform gyrus
    (BA37). This is a **left-lateralized** syndrome.

**What is NOT here:** **Prosody and emotional intonation** are **right
BA22** functions, not left BA22 functions. **Semantic aphasia** and
**impaired sentence comprehension** are **left BA21** functions (though
they can co-occur with BA22 damage). **Gerstmann syndrome** is a **left
BA39** syndrome. The left BA22 is the **speech-comprehension hub**, not
the prosodic, semantic, or praxic hub.

Lateralization Notes
--------------------
This is the **left** BA22 module. The lateralization landscape is **the
most strongly left-lateralized in the human brain** — the left BA22 is
the **definitional Wernicke's area**, while the right BA22 is the
**prosodic and non-verbal auditory cortex**:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Speech comprehension** — the definitional Wernicke's area
      function .
    - **Lexical-semantic processing** — linking spoken words to meanings
      .
    - **Phonological processing** — analysis of speech sounds
      .
    - **Naming and word retrieval** .
    - **Auditory short-term memory and repetition** .
    - **Reading and writing** .

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Emotional prosody** (affective prosody) — the right posterior
      STG/STS (BA22) is part of the right-hemisphere pattern for
      **comprehension of affective prosody**
      .
    - **Discrimination of emotional vs. neutral prosodies** — the right
      posterior STG (BA22) is primarily responsible for this
      .
    - **Processing of negative emotions** (fear, anger) — right
      hemisphere is related to negative emotions
      .

*   **Symmetric Functions (bilateral properties of BA22, copied verbatim
    to the right twin):**
    - **Auditory processing** of complex sounds (with left dominance for
      speech, right dominance for prosody).
    - **Basic acoustic feature analysis** (shared with BA41/42).
    - **Auditory memory** (bilateral component).

**This is the "left-loaded" pattern at its most extreme.** The left BA22
is the **core speech-comprehension hub**; the right BA22 is the **prosodic
and emotional-intonation cortex**. The asymmetry is **not** a division of
equal labor (like BA20's lexical vs. metaphor split) and **not** a
left-dominance-with-right-complement (like BA21's semantic vs. prosody
split). **The left BA22 is the functionally dominant language area; the
right BA22 is the functionally dominant prosody area.** Each hemisphere
has a **dominant specialization**, but they are **different
specializations**, and the left's is the one that defines the clinical
syndrome.

**A consumer that assumes "left BA22 = right BA22" will be wrong for the
entire speech-comprehension domain** — the left BA22 is Wernicke's area;
the right BA22 is not. Wernicke's aphasia is **left-lateralized**; right
BA22 lesions produce **aprosodia**, not aphasia.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe (Broca's area, BA44/45) or the parietal lobe (angular
    gyrus, BA39). Those are **sibling lobes**.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Core Wernicke's area — flagged in prose.** BA22 is part of **core
    Wernicke's area** (BA21, BA22, BA41, BA42), not the extended
    Wernicke's system .
*   **Brodmann leaf under the temporal partition — with a nested
    cross-listing.** BA22 is a local leaf under
    `.../temporal/brodmann_areas/`, **and** it has a nested dual-framing
    module under `.../gyri/superior_temporal_gyrus/wernickes_area/
    brodmann_area_22/`.
*   **`NESTED_CROSS_LISTINGS` is data, not code.** The constant documents
    BA22's dual framing, **and explicitly notes that the right nested
    leaf is prosodic, not speech-comprehension**.
*   **No `AREA_PATHS` hop.** Unlike BA3 (which must be resolved through
    the postcentral gyrus), BA22 has a top-level leaf right here. The
    nested Wernicke's-area leaf is a **dual-framing module**, not a
    resolution target.
*   **Left-loaded at its most extreme.** The left BA22 is Wernicke's
    area; the right BA22 is prosodic cortex. This module documents the
    left-lateralized functions; the right module documents the right-
    lateralized prosodic functions.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.brodmann_areas import brodmann_area_22

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.brodmann_areas.brodmann_area_22"
    )

For the nested Wernicke's-area framing (functionally named)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 — same territory, functional framing

**Both paths return the same cortical territory.** The top-level path is
the **cytoarchitectonic framing**; the nested path is the **Wernicke's-
area framing**. Use the nested path when you need the aphasia syndrome or
the language network; use the top-level path when you need the Brodmann
field.

For the left-lateralized functions::

    from ...temporal.brodmann_areas.brodmann_area_22 import LEFT_LATERALIZED
    # LEFT_LATERALIZED = ("speech_comprehension",
    #                     "lexical_semantic_processing",
    #                     "phonological_processing",
    #                     "naming_and_word_retrieval",
    #                     "auditory_short_term_memory_and_repetition",
    #                     "reading_and_writing")

For the nested cross-listing::

    from ...temporal.brodmann_areas.brodmann_area_22 import NESTED_CROSS_LISTINGS
    # NESTED_CROSS_LISTINGS["brodmann_area_22"] documents both paths

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba22_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.brodmann_areas.brodmann_area_22"
        )
        # resolve ba22_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der
    Grosshirnrinde*. (BA22 defined as the superior temporal area.)
*   **Wernicke's area overview:** *Neuroanatomy, Wernicke Area* (2023),
    StatPearls, NCBI Bookshelf NBK549825. Wernicke area is located in
    BA22, the posterior segment of the superior temporal gyrus in the
    dominant hemisphere; responsible for comprehension of written and
    spoken language; damage produces fluent but receptive aphasia
    .
*   **Lexical semantics and Wernicke's aphasia:** *Lexical Semantics — an
    overview* (ScienceDirect). Focal lesions in the posterior STG (BA22)
    produce lexical-semantic deficits; both acute and chronic lesions
    often result in Wernicke's aphasia; restoration of blood flow in
    left BA22 improves comprehension and naming; left BA22 is highly
    involved in word comprehension and production .
*   **Core vs extended Wernicke's area:** Ardila, A., et al. (2016).
    "How Extended Is Wernicke's Area? Meta-Analytic Connectivity Study
    of BA20 and Integrative Proposal." *Neurosci J*, 2016, 4962562.
    Core Wernicke's area ≈ BA21, BA22, BA41, BA42; extended Wernicke's
    area ≈ BA20, BA37, BA38, BA39, BA40 .
*   **Right-hemisphere prosody (contrast):** Wildgruber, D., et al.
    (2005). "Identification of emotional intonation evaluated by fMRI."
    *NeuroImage*, 24(4), 1233–1241. Comprehension of affective prosody
    is bound to a right-hemisphere pattern including posterior superior
    temporal sulcus (BA22), dorsolateral (BA44/45), and orbitobasal
    (BA47) frontal areas .
*   **Right STG (BA22) and emotional prosody:** *Speech Prosodies of
    Different Emotional Categories Activate Different Brain Regions in
    Adult Cortex: an fNIRS Study* (2018), *Sci Rep*, 8, 607. The right
    posterior STG (BA22) and right primary/secondary AC (BA42) are
    enhanced for emotional vs. neutral prosodies; emotional prosodies
    activate the right STG (BA22/42) .
*   **Cytoarchitecture and connectivity:** *Interhemispheric Asymmetries
    of the Modular Structure in Human Temporal Cortex* (2000), *Science*.
    Language-relevant processing of auditory signals is lateralized and
    involves the posterior part of Brodmann area 22; functional
    lateralization is accompanied by interhemispheric differences in
    intrinsic microcircuitry .
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed.
*   NeuroNames — Brodmann area 22 (left); FMA — Brodmann area 22 (left
    member).
"""