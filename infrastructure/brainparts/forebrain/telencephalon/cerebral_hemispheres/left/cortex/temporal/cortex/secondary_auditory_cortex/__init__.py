"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex.secondary_auditory_cortex
=========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── cortex
                        └── secondary_auditory_cortex   <-- THIS MODULE

**Primary synonym:** Secondary auditory cortex (A2), left; Left A2;
Auditory association cortex; Auditory belt/parabelt; Wernicke's area
region (BA22).
**Organizing principle:** **Functional–anatomical region** — the
auditory association cortex surrounding the primary auditory core.
**Brodmann constitution:** **BA22** (the posterior superior temporal
gyrus, containing Wernicke's area) **plus BA42** (the lateral belt/
parakoniocortex). BA42 is wired under the **insular partition** in the
tree's `brodmann_areas`; BA22 is wired under the **temporal partition**
with a **nested cross-listing**.
**Location:** The **superior temporal gyrus (STG)** and **superior
temporal sulcus (STS)** , lateral and posterior to the primary auditory
cortex (Heschl's gyrus) on the superior temporal plane.
**Structural parent:** Child of ``.../temporal/cortex`` (the functional
partition of the temporal lobe).
**Cytoarchitectonic type:** **Neocortical (parakoniocortical /
dysgranular)** — A2 is a **higher-order auditory association area** with
a **less prominent layer IV** than the koniocortical A1, and a **more
developed layer III** for cortico-cortical output.

Overview
--------
The **left secondary auditory cortex (A2)** is the **left-hemisphere
auditory association cortex** — the **principal cortical substrate for
the transformation of acoustic features into meaningful auditory
objects**, including **speech, music, and environmental sounds**. It sits
in the **belt and parabelt** of the auditory cortical hierarchy, lateral
and posterior to the primary auditory core (A1), and it is the
**anatomical and functional bridge** between basic acoustic analysis
(A1) and higher-order language comprehension (Wernicke's area, BA22).

**A2 is the left-hemisphere pole of a functionally asymmetric pair.**
The **left A2** is specialized for **fast temporal processing and
speech** — it decodes the **rapid temporal perturbations** that
distinguish phonemes and syllables. The **right A2** is specialized for
**spectral processing and music/pitch** — it analyzes the **frequency
content** of complex sounds. This is a **"temporal/spectral
dichotomy"** — the **first auditory-domain lateralization**
documented in the tree, and the **auditory foundation of the
left-hemisphere language dominance**.

**A2 is the first functional region in the tree whose primary Brodmann
anchor (BA22) has a nested cross-listing.** The top-level Brodmann leaf
``temporal.brodmann_areas.brodmann_area_22`` and the nested Wernicke's-
area leaf ``temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22``
both represent the same cortical territory — BA22. This module documents
the **functional region** that contains the left BA22 (Wernicke's area)
and the **left BA42** (lateral belt/parakoniocortex).

**A2 is the cortical substrate of Wernicke's aphasia.** Damage to the
left posterior STG (BA22) — the core of the left A2 — produces
**Wernicke's aphasia** (fluent but meaningless speech, impaired
comprehension, poor repetition, and unawareness of deficit). This is the
**most important clinical syndrome in the temporal lobe**, and it is the
**left-lateralized signature** of A2 pathology.

Cross-Lobe Mapping
------------------
A2's Brodmann constitution **spans two partitions**:

::

    Functional region (this module)     Brodmann mapping      Brodmann partition
    ───────────────────────────────     ─────────────────      ──────────────────
    secondary_auditory_cortex       ──▶  BA42 (lateral belt)   **insular** (not temporal)
                                    ──▶  BA22 (parabelt;      temporal (nested
                                         Wernicke's area)     cross-listing)

**Consumers must not assume that a temporal Brodmann query returns the
full A2 constitution.** BA42 lives under the **insular** partition; BA22
lives under the **temporal** partition with a nested cross-listing.

**Resolution contract for consumers:**

*   If you need **A2 as a functional region**, use this module.
*   If you need **BA42 (lateral belt)**, query
    ``insular.brodmann_areas.brodmann_area_42_posterior_insula``.
*   If you need **BA22 (Wernicke's area)**, query
    ``temporal.brodmann_areas.brodmann_area_22`` or the nested
    ``temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22``.

Hierarchical Organization: Belt and Parabelt
--------------------------------------------
A2 corresponds to the **belt** and **parabelt** levels of the auditory
cortical hierarchy — the **second and third levels** of the
**core-belt-parabelt** cascade:

*   **Belt (BA42)** — a **surrounding ring of non-primary auditory areas**
    that receive input from the core (A1) and from the thalamus. The belt
    performs **higher-order auditory processing** — **spectral
    integration, temporal integration, and the analysis of complex
    acoustic patterns**.

*   **Parabelt (BA22)** — a **third set of auditory areas** lateral to the
    belt, receiving input from the belt. The parabelt performs
    **auditory object recognition and auditory scene analysis** — the
    **integration of acoustic features into meaningful auditory objects**
    (speech, music, environmental sounds). The **posterior parabelt**
    overlaps with **Wernicke's area (BA22)** and the **language
    network**.

**This belt-parabelt architecture is the defining structural fact about
A2.** A1 is the **entry point**; A2 is the **transformation stage** where
**acoustic features become auditory objects**.

Function in the Human Brain
---------------------------
The left A2 is the **left-lateralized speech and fast-temporal
processing hub**. Its best-supported functions cluster into six domains:

*   **Speech Sound Processing (Left-Lateralized — the defining left-A2
    function):** The **left auditory cortex is best at processing fast
    temporal cues**, especially critical for speech.
    **Speech comprehension is a strikingly bilateral process**,
    but the **left hemisphere is dominant for higher-level speech
    processing** — the transformation of **phonological
    sequences** into **meaningful words and sentences**.

*   **Wernicke's Area and Language Comprehension (Left-Lateralized):**
    The **posterior STG (BA22)** is **Wernicke's area** — the
    **core substrate for the comprehension of written and spoken
    language**. Its neurons respond preferentially to **specific
    phonetic parameters** rather than to pure tones, and it is
    **active during exposition to meaningful speech**.

*   **Phonological and Lexical-Semantic Processing (Left-Lateralized):**
    The left A2 supports **phonological processing** (the analysis of
    speech sounds as linguistic units) and **lexical-semantic
    processing** (the mapping of word forms to meanings).
    **Both acute and chronic lesions of left BA22 often result in
    Wernicke's aphasia**, characterized by **impaired comprehension**
    and **fluent but meaningless speech**.

*   **Processing of Complex Acoustic Patterns (Bilateral Foundation):**
    A2 processes **complex acoustic patterns** — **harmonies, timbre,
    sequential acoustic analysis, and auditory working memory**.
    This is a **bilateral** foundation that supports the left-
    lateralized speech function.

*   **Auditory Working Memory and Pattern Recognition (Bilateral):** A2
    supports **auditory working memory** and **pattern recognition in
    the auditory domain** — the ability to hold and manipulate acoustic
    information over short periods.

*   **Integration with Visual Information (Bilateral):** A2 contributes
    to **integration with visual information** — e.g., **lip reading**
    and **audiovisual speech perception** — via connections to the
    posterior STS and the visual word form area.

Associated Disorders
--------------------
Damage to or dysfunction of the left A2 is associated with:

*   **Wernicke's Aphasia (Left-Lateralized — the signature left-A2
    syndrome):** **Fluent but receptive aphasia** — the patient
    **cannot comprehend written or spoken language**, produces **fluent
    speech that lacks meaning**, and is **unaware of their lack of
    comprehension**. **Both acute and chronic lesions of left BA22 often
    result in Wernicke's aphasia**.

*   **Auditory Agnosia (Bilateral or Left-Lateralized):** **Impaired
    recognition of sounds** despite intact hearing — including
    **nonverbal auditory agnosia** (inability to recognize environmental
    sounds) and **verbal auditory agnosia** (pure word deafness).
    **Auditory agnosia is thought to result from unilateral or bilateral
    lesions of the unimodal (secondary) auditory association cortex**.

*   **Impaired Speech Recognition in Noise (Left-Lateralized):**
    **Difficulty understanding speech in noisy environments**, consistent
    with the left A2's role in **spectral and temporal integration** for
    speech.

*   **Impaired Music Perception (Amusia — Right-Lateralized
    Contrast):** **Impaired music perception** is associated with
    **right A2** damage, not left. It is **absent** from left A2 lesions.

**What is NOT here:** **Amusia**, **pitch processing deficits**, and
**spectral processing deficits** are **right A2** functions. They are
**absent** from left A2 lesions. They are documented in the right A2
module and are **explicitly not claimed here**. The left A2 is the
**speech/fast-temporal** pole; the right A2 is the **music/spectral**
pole.

Lateralization Notes
--------------------
This is the **left** A2 module. The lateralization landscape is the
**temporal/spectral dichotomy** — a **sensory-domain weighting** for
fast temporal processing and speech:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Fast temporal processing** — rapid acoustic perturbations.
    - **Speech sound processing** — phoneme and syllable decoding.
    - **Wernicke's area** — language comprehension.
    - **Phonological and lexical-semantic processing**.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Spectral processing** — frequency content of complex sounds.
    - **Music perception** — pitch, melody, harmony.
    - **Pitch processing** — fine-grained tonal discrimination.
    - **Amusia** — the right-A2 signature syndrome.

*   **Symmetric Functions (bilateral properties of A2):**
    - Processing of complex acoustic patterns.
    - Auditory working memory and pattern recognition.
    - Integration with visual information (lip reading).
    - Timbre processing.

**This is the "temporal/spectral dichotomy" pattern** — the **first
auditory-domain lateralization** documented in the tree. Unlike MT
(right-dominant motion) or the olfactory cortex (ipsilateral
representation), A2's lateralization is a **leftward weighting for
speech and fast temporal processing** and a **rightward weighting for
music and spectral processing**. The **left hemisphere is the dominant
speech processor**; the right hemisphere is the **dominant music
processor**.

**A consumer that assumes "left A2 = right A2" will miss the leftward
speech weighting and the rightward spectral/music weighting** — but the
left twin is **not** merely "denying" a right-hemisphere claim; it is
**carrying a speech-specialized subset** of the auditory-association
function.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    insular lobe (BA42) or the occipital lobe. Those are **cross-lobe
    Brodmann anchors**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cross-lobe Brodmann mapping — flagged in prose and data.** A2's
    lateral belt anchor (BA42) lives under the **insular** partition;
    its parabelt anchor (BA22) lives under the **temporal** partition
    with a nested cross-listing. The ``BRODMANN_MAPPING`` constant
    documents the mapping.
*   **Neocortical parakoniocortical type — flagged in data.** A2 is
    **neocortical and parakoniocortical/dysgranular**, not koniocortical
    like A1. The ``CYTOARCHITECTONIC_TYPE`` constant is
    **"neocortical_parakoniocortical"**.
*   **Hierarchical organization — flagged in data.** A2 corresponds to
    the **belt and parabelt** levels. The ``HIERARCHICAL_LEVEL`` constant
    is **("belt", "parabelt")**.
*   **Temporal/spectral dichotomy — flagged in data.** The
    ``LEFTWARD_ASYMMETRY`` constant documents the leftward functional
    asymmetry for fast temporal and speech processing.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex import secondary_auditory_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.cortex.secondary_auditory_cortex"
    )

For the Brodmann constitution::

    from ...temporal.cortex.secondary_auditory_cortex import BRODMANN_MAPPING
    # BRODMANN_MAPPING = {
    #     "brodmann_area_42": "insular",   # lateral belt
    #     "brodmann_area_22": "temporal",  # parabelt (nested Wernicke's)
    # }

For the leftward asymmetry::

    from ...temporal.cortex.secondary_auditory_cortex import LEFTWARD_ASYMMETRY
    # LEFTWARD_ASYMMETRY = True

For the hierarchical organization::

    from ...temporal.cortex.secondary_auditory_cortex import HIERARCHICAL_LEVEL
    # HIERARCHICAL_LEVEL = ("belt", "parabelt")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        a2_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.cortex.secondary_auditory_cortex"
        )
        # resolve a2_path through the memory/recall layer

References
----------
*   **A2 and Wernicke's area:** *Neuroanatomy, Wernicke Area* (2023),
    StatPearls, NCBI Bookshelf NBK533001. Wernicke area is located in
    **Brodmann area 22**, the posterior segment of the superior temporal
    gyrus in the dominant hemisphere; **95% of people have a left
    dominant hemisphere**; damage produces **fluent but receptive
    aphasia** .
*   **Temporal/spectral dichotomy:** Zatorre, R.J., & Belin, P. (2001).
    "Spectral and temporal processing in human auditory cortex." *Cereb
    Cortex*, 11(10), 946–953. The **left auditory cortex is best at
    processing fast temporal cues**, especially critical for speech; the
    **right auditory cortex is best for processing tonal or spectral
    information** .
*   **Left-hemisphere dominance for higher-level speech:** *Speech
    processing: from peripheral to hemispheric asymmetry of the auditory
    system* (2011), *PubMed*. Language processing from the cochlea to
    auditory association cortices shows **side-dependent specificities
    with an apparent left hemispheric dominance**; a **left-hemispheric
    dominance exists for higher-level processing** .
*   **A2 functions and disorders:** *Brodmann Area 42 — Secondary Auditory
    Cortex* (Neurofeedback Academy). Processing of complex acoustic
    patterns, harmonies, music, auditory working memory, pattern
    recognition, timbre, speech recognition, sequential acoustic
    analysis, integration with visual information (lip reading);
    associated with **auditory agnosia**, **impaired music perception**,
    problems processing complex sounds, altered auditory memory, impaired
    speech recognition in noise .
*   **Belt/parabelt hierarchy:** *Activation lateralization in human
    core, belt, and parabelt auditory fields* (2012), *PMC3403813*. The
    **belt** and **parabelt** are higher levels of the auditory
    hierarchy; **speech comprehension is a strikingly bilateral
    process**, but the **left hemisphere is dominant for higher-level
    speech processing** .
*   **Left A2 and speech in mice:** *PNAS* 2023, 120(30), e2219340120.
    The **secondary auditory cortex (A2) in the left hemisphere** shows
    **larger responses than right to high-frequency tones and adult
    vocalizations**; A2 shows **lateralized functional activation**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Superior temporal gyrus and sulcus anatomy.)
*   NeuroNames — Secondary auditory cortex (left); FMA — left superior
    temporal gyrus partonomy.
"""