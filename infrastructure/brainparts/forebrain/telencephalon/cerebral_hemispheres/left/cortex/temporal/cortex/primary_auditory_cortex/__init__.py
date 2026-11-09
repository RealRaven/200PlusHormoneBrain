"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex.primary_auditory_cortex
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── cortex
                        └── primary_auditory_cortex   <-- THIS MODULE

**Primary synonym:** Primary auditory cortex (A1), left; Left A1; Core
auditory cortex; Heschl's gyrus (HG); Transverse temporal gyrus.
**Organizing principle:** **Functional–anatomical region** — the first
cortical relay station for auditory information.
**Brodmann constitution:** **BA41 and BA42** — the **first cross-lobe
functional region in the tree** (see "Cross-Lobe Mapping" below). BA41
and BA42 are wired under the **insular partition** in the tree's
`brodmann_areas`, **not** the temporal partition.
**Location:** The **posteromedial two-thirds of the first transverse
temporal gyrus (Heschl's gyrus)**, on the **superior temporal plane**
within the **Sylvian fissure** (temporal operculum)[reference:0][reference:1].
**Structural parent:** Child of ``.../temporal/cortex`` (the functional
partition of the temporal lobe).
**Cytoarchitectonic type:** **Neocortical (koniocortical)** — A1 is a
**primary sensory koniocortex** with a **prominent, densely packed layer
IV** and a **dense band of cytochrome oxidase activity** in layer IV and
the base of layer III[reference:2].

Overview
--------
The **left primary auditory cortex (A1)** is the **first cortical relay
station for auditory information** — the **principal cortical recipient
of thalamocortical auditory afferents** from the **medial geniculate
body (MGB)** and the **entry point of auditory information into the
cerebral cortex**[reference:3][reference:4]. It sits on **Heschl's gyrus**
in the superior temporal plane, and it is the **core of a hierarchical
auditory processing cascade** that extends through the **belt** and
**parabelt** to the **auditory association cortices** (including
Wernicke's area, BA22) and beyond[reference:5][reference:6].

**A1 is the first functional region in the tree whose primary Brodmann
anchor lives in a different lobe's partition.** The tree's
`brodmann_areas` partition wires **BA41 and BA42 under the insular
lobe**, **not** the temporal lobe. A consumer that iterates
``temporal.brodmann_areas.ITERABLE_AREAS`` will **not** see BA41/BA42 —
they must query ``insular.brodmann_areas`` separately. This makes A1 the
**first "cross-lobe functional region" in the temporal cortex partition**,
alongside MT (which maps to BA19 in the occipital partition).

**A1 is the core of a three-level hierarchical auditory system.** The
auditory cortex is organized into a **core** (primary area, A1), a
**belt** (non-primary areas surrounding the core), and a **parabelt**
(higher-order areas)[reference:7][reference:8]. This hierarchy is the
anatomical substrate for the transformation of **basic acoustic
features** (A1) into **complex auditory patterns** (belt) and
**auditory objects** (parabelt), including **speech, music, and
environmental sounds**.

**A1 is the first sensory cortex in the tree with a clearly documented
leftward functional asymmetry.** Unlike the olfactory cortex (ipsilateral
representation) or MT (right-dominant motion), A1 exhibits a **leftward
functional asymmetry** during both **linguistic and non-linguistic sound
stimulation** — the **first sensory-domain lateralization** with a
**leftward** direction[reference:9]. This asymmetry is the **auditory
foundation of the left-hemisphere language dominance**.

Cross-Lobe Mapping
------------------
A1 is the **first functional region in the tree whose primary Brodmann
anchor is in a different lobe's partition**:

::

    Functional region (this module)     Brodmann mapping      Brodmann partition
    ───────────────────────────────     ─────────────────      ──────────────────
    primary_auditory_cortex         ──▶  BA41 (core A1)       **insular** (not temporal)
                                    ──▶  BA42 (belt/boundary)  **insular** (not temporal)
                                    ──▶  BA22 (belt/parabelt)  temporal (nested)

**Consumers must not assume that the temporal functional partition maps
1:1 onto the temporal Brodmann partition.** A1 is the **counterexample**:
its primary cytoarchitectonic anchors (BA41 and BA42) live under the
**insular** partition, and its tertiary association area (BA22) lives
under the **temporal** partition with a **nested cross-listing**.

**Resolution contract for consumers:**

*   If you need **A1 as a functional region**, use this module.
*   If you need **BA41 or BA42 as cytoarchitectonic fields**, query
    ``insular.brodmann_areas.brodmann_area_41_posterior_insula`` and
    ``insular.brodmann_areas.brodmann_area_42_posterior_insula``.
*   If you need **BA22 (Wernicke's area)**, query
    ``temporal.brodmann_areas.brodmann_area_22`` (or the nested
    ``temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22``).
*   **Do not** assume that a temporal Brodmann query will return A1's
    primary cytoarchitectonic anchor. It will not.

Hierarchical Organization: Core, Belt, Parabelt
-----------------------------------------------
The auditory cortex is organized into **three hierarchical levels** — the
**first sensory system in the tree with this explicit tri-level
architecture**[reference:10][reference:11]:

*   **Core (A1)** — the **primary auditory cortex**, receiving **direct
    thalamocortical input** from the MGB. It contains **tonotopic maps**
    of sound frequency and performs **basic acoustic feature analysis**
    (frequency, intensity, duration). This is the **first cortical stage
    of auditory processing**.

*   **Belt** — a **surrounding ring of non-primary auditory areas** that
    receive input from the core and from the thalamus. The belt performs
    **higher-order auditory processing** — **spectral integration,
    temporal integration, and the analysis of complex acoustic patterns**
    [reference:12][reference:13]. The **antero-lateral belt** is the site of
    **hemispheric asymmetry for spectral and temporal processing**[reference:14].

*   **Parabelt** — a **third set of auditory areas** lateral to the belt,
    receiving input from the belt. The parabelt performs **auditory object
    recognition and auditory scene analysis** — the **integration of
    acoustic features into meaningful auditory objects** (speech, music,
    environmental sounds)[reference:15]. The **posterior parabelt** overlaps
    with **Wernicke's area (BA22)** and the **language network**[reference:16].

**This tri-level architecture is the defining structural fact about the
auditory cortex.** A1 is the **entry point**, not the endpoint — the
auditory system transforms **acoustic features** into **meaningful
sounds** through this **hierarchical cascade**.

Tonotopy and Cytoarchitecture
-----------------------------
A1 is a **tonotopically organized, koniocortical field**:

*   **Tonotopic organization** — A1 contains a **tonotopic map** of sound
    frequency, with **different frequencies represented in different
    cortical locations**[reference:17][reference:18]. This is the **auditory
    analogue of retinotopy in V1** and **somatotopy in S1**.

*   **Koniocortex** — A1 is a **primary sensory koniocortex** with a
    **prominent, densely packed layer IV** and a **dense band of
    cytochrome oxidase activity** in layer IV and the base of layer III
    [reference:19]. **BA41** has a **more densely packed, narrower layer
    IV** than BA42[reference:20].

*   **Transverse temporal gyri** — A1 is located on the **posteromedial
    two-thirds of the first transverse temporal gyrus (Heschl's gyrus)**,
    with **BA41** forming the **core** and **BA42** forming the
    **surrounding belt**[reference:21][reference:22].

Function in the Human Brain
---------------------------
The left A1 is the **left-lateralized core auditory processing hub**. Its
best-supported functions cluster into six domains:

*   **Basic Acoustic Feature Analysis (the defining function, bilateral
    with leftward asymmetry):** A1 is the **first cortical stage of
    auditory processing**, performing **frequency, intensity, and duration
    analysis** of sound[reference:23]. This is a **bilateral** foundation,
    but it exhibits a **leftward functional asymmetry** during both
    linguistic and non-linguistic stimulation[reference:24].

*   **Speech Sound Processing (Left-Lateralized):** The **left auditory
    cortex has a higher temporal resolution** than the right and is
    **more sensitive to the high-speed temporal changes needed for
    speech**[reference:25]. A1 (BA41, and to a lesser extent BA42) is
    involved in **early stages of phonological processing (phoneme
    recognition)**[reference:26].

*   **Phoneme Recognition and Word Deafness (Left-Lateralized):** **Damage
    to the left A1** (or bilateral damage) produces **pure word deafness**
    (“auditory verbal agnosia”) — a **severe comprehension deficit for
    spoken words** with **relatively intact abilities in other areas of
    language**[reference:27][reference:28]. **Word-deaf patients** show
    **disordered perception of stop consonants** (which change rapidly
    over time) but **relatively intact processing of vowels** (which are
    steady over time)[reference:29].

*   **Temporal Resolution and Gap Detection (Bilateral):** A1 supports the
    **resolution of acoustic events of a fine temporal grain**. Patients
    with auditory cortical damage require **longer silent durations** to
    detect a **gap between two noise bursts** or to perceive **two
    discrete click events** instead of a fused single one[reference:30].

*   **Auditory Associative Learning and Memory (Bilateral):** A1 can no
    longer be considered **only a sensory analyzer** — it is **deeply
    involved in associative learning and memory**, and in the
    **attribution of meaning to sound**[reference:31].

*   **Pitch Processing (Right-Lateralized Contrast):** **Right, but not
    left, auditory cortex lesions** impair **pitch perception of complex
    tones** when the fundamental frequency is absent, and impair
    **timbre identification** and **melody discrimination**[reference:32].
    This is a **right-lateralized** function that is **not claimed for
    the left A1**.

Associated Disorders
--------------------
Damage to or dysfunction of the left A1 is associated with:

*   **Pure Word Deafness (Left-Lateralized — the signature left-A1
    syndrome):** **Impaired comprehension of spoken words** with
    **relatively intact reading, writing, and environmental sound
    recognition**, following **left or bilateral lesions** of the primary
    auditory cortex[reference:33][reference:34]. The patient can hear but
    cannot **decode speech sounds**.

*   **Auditory Verbal Agnosia (Left-Lateralized):** A broader term for
    the **inability to recognize speech sounds** despite intact hearing,
    following **left auditory cortical damage**[reference:35].

*   **Impaired Phoneme Discrimination (Left-Lateralized):** **Disordered
    perception and discrimination of stop consonants** (b, d, g, p, t,
    k), which contain **rapidly changing auditory information**, with
    **relatively intact vowel processing**[reference:36].

*   **Impaired Temporal Resolution (Bilateral):** **Difficulty detecting
    brief gaps** in noise or **discriminating two closely spaced click
    events**, following auditory cortical damage[reference:37].

*   **Generalized Auditory Agnosia (Bilateral Lesions):** **Bilateral
    destruction** of the primary auditory cortex or acoustic radiation
    can produce **generalized auditory agnosia** — the **inability to
    recognize any sound**, including environmental sounds
    [reference:38].

**What is NOT here:** **Pitch processing deficits** and **amusia**
(music perception deficits) are **right auditory cortex** functions.
They are **absent** from left A1 lesions. They are documented in the
right A1 module and are **explicitly not claimed here**. The left A1 is
the **speech** pole; the right A1 is the **music/pitch** pole.

Lateralization Notes
--------------------
This is the **left** A1 module. The lateralization landscape is
**leftward functional asymmetry** — a **sensory-domain weighting** for
speech, not a semantic-domain split:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Speech sound processing** — higher temporal resolution, sensitivity
      to rapid temporal changes[reference:39].
    - **Phoneme recognition** — early phonological processing
      [reference:40].
    - **Pure word deafness** — the signature left-A1 syndrome
      [reference:41].
    - **Leftward functional asymmetry** during linguistic and
      non-linguistic stimulation[reference:42].

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Pitch processing** — complex tone pitch, timbre, melody
      discrimination[reference:43].
    - **Spectral processing** — higher resolution of spectral information
      for music[reference:44].

*   **Symmetric Functions (bilateral properties of A1):**
    - Basic acoustic feature analysis (frequency, intensity, duration).
    - Temporal resolution and gap detection.
    - Auditory associative learning and memory.

**This is the "leftward sensory weighting" pattern** — the **first
sensory-domain lateralization with a leftward direction** in the tree.
Unlike MT (right-dominant motion) or the olfactory cortex (ipsilateral
representation), A1's lateralization is a **leftward weighting for
speech** and a **rightward weighting for music/pitch**. The **left
hemisphere is the dominant speech processor**; the right hemisphere is
the **dominant music/pitch processor**.

**A consumer that assumes "left A1 = right A1" will miss the leftward
speech weighting and the rightward pitch/music weighting** — but the
left twin is **not** merely "denying" a right-hemisphere claim; it is
**carrying a speech-specialized subset** of the auditory-processing
function.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    insular lobe (BA41/BA42) or the occipital lobe. Those are **cross-lobe
    Brodmann anchors**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cross-lobe Brodmann mapping — flagged in prose and data.** A1's
    primary Brodmann anchors (BA41 and BA42) live under the **insular**
    partition. The ``BRODMANN_PARTITION`` constant is **"insular"**; the
    ``CROSS_PARTITION_AREAS`` constant in the parent temporal cortex
    aggregator records A1 → insular.
*   **Neocortical koniocortical type — flagged in data.** A1 is
    **neocortical and koniocortical**, not paleocortical or transitional.
    The ``CYTOARCHITECTONIC_TYPE`` constant is **"neocortical_koniocortical"**.
*   **Hierarchical organization — flagged in data.** A1 is the **core**
    of a **core-belt-parabelt** hierarchy. The ``HIERARCHICAL_LEVEL``
    constant is **"core"**.
*   **Leftward functional asymmetry — flagged in data.** The
    ``LEFTWARD_ASYMMETRY`` constant documents the leftward functional
    asymmetry during linguistic and non-linguistic stimulation.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex import primary_auditory_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.cortex.primary_auditory_cortex"
    )

**A1's primary Brodmann anchors (BA41/BA42) live under the insular
partition.** Use the `BRODMANN_PARTITION` constant to check::

    from ...temporal.cortex.primary_auditory_cortex import BRODMANN_PARTITION
    # BRODMANN_PARTITION = "insular"

For BA41/BA42 as cytoarchitectonic fields::

    from ...insular.brodmann_areas import brodmann_area_41_posterior_insula
    from ...insular.brodmann_areas import brodmann_area_42_posterior_insula

For the leftward asymmetry::

    from ...temporal.cortex.primary_auditory_cortex import LEFTWARD_ASYMMETRY
    # LEFTWARD_ASYMMETRY = True

For the hierarchical organization::

    from ...temporal.cortex.primary_auditory_cortex import HIERARCHICAL_LEVEL
    # HIERARCHICAL_LEVEL = "core"

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        a1_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.cortex.primary_auditory_cortex"
        )
        # resolve a1_path through the memory/recall layer

References
----------
*   **A1 overview and hierarchical organization:** *Primary Auditory Cortex
    — Chapters and Articles* (ScienceDirect). A1 is the **first relay
    station for auditory information in the cortex**; it projects to a
    **belt** and **parabelt**; damage produces **word deafness**
    [reference:45].
*   **Core-belt-parabelt hierarchy:** *The auditory brain consists of
    three different parts: the core, the belt and the parabelt*
    (dspace.uba.uva.nl). The **core** is on the dorsal STG, surrounded
    by the **belt** and **parabelt**; the **left auditory cortex** has
    higher temporal resolution for speech, the **right** higher spectral
    resolution for music[reference:46].
*   **Leftward functional asymmetry:** *Functional asymmetry in human
    primary auditory cortex: Identified from longitudinal fMRI study*
    (2005), *Neuroscience Letters*. **Predominant and consistent leftward
    functional asymmetry in PAC** during both linguistic and
    non-linguistic sound stimulations[reference:47].
*   **Hemispheric asymmetry for spectral and temporal processing:**
    *Hemispheric asymmetry for spectral and temporal processing in the
    human antero-lateral auditory belt cortex* (2005), *Eur J Neurosci*.
    The **antero-lateral auditory belt** is the site of hemispheric
    asymmetry for speech and music processing[reference:48].
*   **Tonotopy and koniocortex:** *Temporal Gyrus — an overview*
    (ScienceDirect). A1 is on the **transverse temporal gyri (Heschl's
    gyrus)**; **BA41 and BA42** are the primary auditory cortex with
    **tonotopic representation**[reference:49]. *Histochemical
    identification of cortical areas* (2002), *Europe PMC*. A1 has a
    **dense band of cytochrome oxidase activity** in layer IV and the
    base of layer III[reference:50].
*   **Pure word deafness and A1 lesions:** *Pure word deafness after
    bilateral primary auditory cortex infarcts* (Neurology). **Pure word
    deafness** is associated with **bilateral infarctions of the primary
    auditory cortex**; the PAC seems to be **essential for comprehending
    speech**[reference:51].
*   **Wernicke's area relationship:** *Interpretation of Wernicke's area
    in action* (University of Michigan). **Primary auditory cortex
    (41/42) → Wernicke's A. (22) → semantic networks**[reference:52].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Superior temporal plane and Heschl's gyrus anatomy.)
*   NeuroNames — Primary auditory cortex (left); FMA — left Heschl's gyrus
    partonomy.
"""