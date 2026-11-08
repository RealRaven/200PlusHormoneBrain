"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex.primary_auditory_cortex
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── cortex
                        └── primary_auditory_cortex   <-- THIS MODULE

**Primary synonym:** Primary auditory cortex (A1), right; Right A1; Core
auditory cortex; Heschl's gyrus (HG); Transverse temporal gyrus.
**Organizing principle:** **Functional–anatomical region** — the first
cortical relay station for auditory information.
**Brodmann constitution:** **BA41 and BA42** — the **first cross-lobe
functional region in the tree** (see "Cross-Lobe Mapping" below). BA41
and BA42 are wired under the **insular partition** in the tree's
`brodmann_areas`, **not** the temporal partition.
**Location:** The **posteromedial two-thirds of the first transverse
temporal gyrus (Heschl's gyrus)**, on the **superior temporal plane**
within the **Sylvian fissure** (temporal operculum).
**Structural parent:** Child of ``.../temporal/cortex`` (the functional
partition of the temporal lobe).
**Cytoarchitectonic type:** **Neocortical (koniocortical)** — A1 is a
**primary sensory koniocortex** with a **prominent, densely packed layer
IV** and a **dense band of cytochrome oxidase activity** in layer IV and
the base of layer III.

Overview
--------
The **right primary auditory cortex (A1)** is the **first cortical relay
station for auditory information** in the right hemisphere — the
**principal cortical recipient of thalamocortical auditory afferents**
from the **medial geniculate body (MGB)** and the **entry point of
auditory information into the cerebral cortex**. It sits on **Heschl's
gyrus** in the superior temporal plane, and it is the **core of a
hierarchical auditory processing cascade** that extends through the
**belt** and **parabelt** to the **auditory association cortices** and
beyond.

**This is the right-hemisphere twin of the left A1, and the pair
instantiates the "rightward spectral/pitch weighting" pattern** — a
**sensory-domain weighting** for spectral and pitch information, not a
semantic-domain split. The two hemispheres carry **different emphases**
within the same auditory-processing cascade:

*   **The left A1 is the left-lateralized pole** for **fast temporal
    processing** — it specializes in the **rapid temporal components of
    speech sounds** and integrates information over **shorter
    timescales**.

*   **The right A1 is the right-lateralized pole** for **spectral and
    pitch processing** — it specializes in **spectrally complex
    stimuli**, **fine-grained tonal processing**, and **musical pitch**,
    and integrates information over **longer timescales**.

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
(higher-order areas)[reference:0]. This hierarchy is the anatomical
substrate for the transformation of **basic acoustic features** (A1)
into **complex auditory patterns** (belt) and **auditory objects**
(parabelt), including **speech, music, and environmental sounds**.

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
**insular** partition.

**Resolution contract for consumers:**

*   If you need **A1 as a functional region**, use this module.
*   If you need **BA41 or BA42 as cytoarchitectonic fields**, query
    ``insular.brodmann_areas.brodmann_area_41_posterior_insula`` and
    ``insular.brodmann_areas.brodmann_area_42_posterior_insula``.
*   If you need **BA22 (Wernicke's area on the left; prosodic cortex on
    the right)**, query ``temporal.brodmann_areas.brodmann_area_22``.
*   **Do not** assume that a temporal Brodmann query will return A1's
    primary cytoarchitectonic anchor. It will not.

Hierarchical Organization: Core, Belt, Parabelt
-----------------------------------------------
The auditory cortex is organized into **three hierarchical levels** —
the **first sensory system in the tree with this explicit tri-level
architecture**:

*   **Core (A1)** — the **primary auditory cortex**, receiving **direct
    thalamocortical input** from the MGB. The core is characterized by
    a **dense granular layer IV** and **multiple tonotopic maps** with
    frequency gradients, comprising isofrequency bands oriented
    medio-laterally[reference:1].

*   **Belt** — a **surrounding ring of non-primary auditory areas** that
    receive input predominantly from the core (with minor thalamic
    contributions). The belt allows a **second level of auditory
    processing** and responds to **more complex sounds** than the
    core[reference:2]. The **antero-lateral auditory belt** is the site
    of **hemispheric asymmetry for spectral and temporal processing**:
    **rightward lateralization for spectrally complex stimuli** and
    **leftward lateralization for rapidly changing stimuli**[reference:3].

*   **Parabelt** — a **third set of auditory areas** lateral to the belt,
    receiving input from the belt and permitting a **third level of
    auditory processing**[reference:4]. The parabelt performs
    **auditory object recognition and auditory scene analysis**.

**This tri-level architecture is the defining structural fact about the
auditory cortex.** A1 is the **entry point**, not the endpoint.

Tonotopy and Cytoarchitecture
-----------------------------
A1 is a **tonotopically organized, koniocortical field**:

*   **Spectrally organized tonotopic maps** — the right hemisphere shows
    **clear spectrally organized tonotopic maps** with **distinct
    separations between different frequency-processing regions**. AEPs
    for **high frequencies are recorded medially**, whereas AEPs for
    **low frequencies are recorded laterally**[reference:5]. In the left
    hemisphere, this tonotopic organization is **less evident**, with
    different regions involved in processing a range of frequencies
    [reference:6]. This is the **clearest tonotopic asymmetry** between
    the hemispheres.

*   **Koniocortex** — A1 is a **primary sensory koniocortex** with a
    **prominent, densely packed layer IV** and a **dense band of
    cytochrome oxidase activity** in layer IV and the base of layer III.

*   **Transverse temporal gyri** — A1 is located on the **posteromedial
    two-thirds of the first transverse temporal gyrus (Heschl's gyrus)**,
    with **BA41** forming the **core** and **BA42** forming the
    **surrounding belt**.

Function in the Human Brain
---------------------------
The right A1 is the **right-lateralized spectral and pitch processing
hub**. Its best-supported functions cluster into six domains — **five
symmetric with the left twin and one right-lateralized emphasis**:

*   **Spectral Processing (Right-Lateralized — the defining right-A1
    function):** The right A1 (and adjacent antero-lateral belt) shows
    **greater activation for spectrally complex stimuli** than the
    left[reference:7][reference:8]. **Harmonic tones** (which have complex
    spectra) produce **more activation than single tones in right
    Heschl's gyrus**[reference:9]. The right auditory cortex is
    **dominant for spectral processing** — the analysis of the
    **frequency content** of sounds.

*   **Pitch Processing (Right-Lateralized):** The **right auditory
    cortex** is **dominant for pitch perception** — the perceptual
    attribute that allows sounds to be ordered on a frequency-related
    scale. **Pitch discrimination tasks** enlarge the **N100m dipole
    distance** between tones **especially in the right auditory
    cortex**, but not during laterality discrimination tasks
    [reference:10]. The **right, but not left, auditory cortex lesions**
    impair **pitch perception of complex tones** and **melody
    discrimination**[reference:11].

*   **Music Perception and Amusia (Right-Lateralized):** The **right
    auditory cortex** plays an important role in **musical pitch
    processing**[reference:12]. **Right temporal lobe-damaged patients**
    show **overall impairment of music perception**, while left
    temporal lobe-damaged patients show more specific deficits in
    melodic and temporal appreciation[reference:13]. **Pure amusia**
    cases involve **right superior and middle temporal gyrus lesions**
    [reference:14]. **Acquired amusia** after stroke is associated with
    damage to the **right auditory cortex** together with other temporal
    and frontal structures[reference:15].

*   **Prosody and Aprosodia (Right-Lateralized):** The **right A1–A2
    region** is **more sensitive to the overall intonational pattern**
    present in a phonemic sequence — the **fundamental frequency (F0)**
    and its variation[reference:16]. **Damage to perisylvian areas in the
    right hemisphere** can interfere with **speech prosody** and lead
    to **aprosodia**[reference:17]. This is the **right-hemisphere
    complement** to the left A1's speech-sound processing.

*   **Slower Temporal Integration (Right-Lateralized):** The **right
    auditory cortex** is believed to specialize in processing **slower
    temporal components** of sounds[reference:18]. It has **longer
    temporal integration windows** than the left[reference:19],
    consistent with the temporal scales of **syllabic and supra-syllabic
    processing**[reference:20]. This is the **right-hemisphere
    complement** to the left A1's fast temporal processing.

*   **Basic Acoustic Feature Analysis and Auditory Learning (Bilateral):**
    A1 performs **frequency, intensity, and duration analysis** of sound
    and is involved in **auditory associative learning and memory**.
    These are **bilateral** foundations.

Associated Disorders
--------------------
Damage to or dysfunction of the right A1 is associated with:

*   **Amusia (Right-Lateralized — the signature right-A1 syndrome):**
    **Acquired amusia** — the loss of music perception — follows
    **right temporal lobe lesions**, particularly involving the **right
    superior and middle temporal gyrus**[reference:21]. **Right auditory
    cortical damage** produces **overall impairment of music
    perception**[reference:22].

*   **Aprosodia (Right-Lateralized):** **Impaired comprehension and/or
    production of speech prosody** — the emotional and intonational
    melody of speech — follows **right perisylvian damage**[reference:23].
    This is the **right-hemisphere analogue of aphasia**.

*   **Pitch Processing Deficits (Right-Lateralized):** **Impaired pitch
    perception** for complex tones, with **preserved** performance on
    simple frequency discrimination, follows **right auditory cortex
    lesions**[reference:24].

*   **Impaired Spectral Processing (Right-Lateralized):** **Difficulty
    analyzing the spectral content** of complex sounds, following
    right A1 damage.

*   **Auditory Agnosia (Bilateral or Right-Lateralized):** Impaired
    **recognition of environmental sounds or music** (as distinct from
    speech) when early perceptual processing is preserved. Auditory
    agnosia for non-speech sounds is associated with **right or bilateral
    auditory association cortex lesions**[reference:25].

**What is NOT here:** **Pure word deafness**, **phoneme discrimination
deficits**, and **fast temporal processing deficits** are **left A1**
functions. They are **absent** from right A1 lesions. They are
documented in the left A1 module and are **explicitly not claimed here**.
The right A1 is the **spectral/pitch/music** pole; the left A1 is the
**speech/fast-temporal** pole.

Lateralization Notes
--------------------
This is the **right** A1 module. The lateralization landscape is
**rightward spectral/pitch weighting** — a **sensory-domain weighting**,
not a semantic-domain split:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Spectral processing** — complex harmonic spectra.
    - **Pitch processing** — fine-grained tonal discrimination.
    - **Music perception** — amusia follows right lesions.
    - **Prosody** — aprosodia follows right lesions.
    - **Slower temporal integration** — longer timescales.

*   **Left-Lateralized Functions (contrast — absent here):**
    - **Fast temporal processing** — rapid acoustic changes.
    - **Speech sound processing** — phoneme recognition.
    - **Pure word deafness** — the signature left-A1 syndrome.

*   **Symmetric Functions (bilateral properties of A1):**
    - Basic acoustic feature analysis (frequency, intensity, duration).
    - Auditory associative learning and memory.
    - Contralateral ear representation (both hemispheres
      represent the contralateral ear more strongly)[reference:26].

**This is the "rightward sensory weighting" pattern** — the **mirror
image of the left A1's leftward speech weighting**. Unlike MT
(right-dominant motion), the A1 pair is a **bilateral sensory system with
complementary hemispheric specializations**: the **left for fast
temporal/speech**, the **right for spectral/pitch/music**. Neither
hemisphere is the "dominant" one; they are **specialized for different
acoustic dimensions**.

**A consumer that assumes "right A1 = left A1" will miss the rightward
spectral, pitch, music, and prosody weighting** — but the right twin is
**not** merely "denying" the left's speech functions; it is **carrying
a spectral/pitch-specialized subset** of the auditory-processing
function.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    insular lobe (BA41/BA42) or the occipital lobe. Those are **cross-lobe
    Brodmann anchors**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cross-lobe Brodmann mapping — flagged in prose and data.** A1's
    primary Brodmann anchors (BA41 and BA42) live under the **insular**
    partition. The ``BRODMANN_PARTITION`` constant is **"insular"**.
*   **Neocortical koniocortical type — flagged in data.** A1 is
    **neocortical and koniocortical**, not paleocortical or transitional.
    The ``CYTOARCHITECTONIC_TYPE`` constant is **"neocortical_koniocortical"**.
*   **Hierarchical organization — flagged in data.** A1 is the **core**
    of a **core-belt-parabelt** hierarchy. The ``HIERARCHICAL_LEVEL``
    constant is **"core"**.
*   **Rightward spectral/pitch weighting — flagged in data.** The
    ``RIGHTWARD_ASYMMETRY`` constant documents the rightward functional
    asymmetry for spectral and pitch processing.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex import primary_auditory_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.cortex.primary_auditory_cortex"
    )

**A1's primary Brodmann anchors (BA41/BA42) live under the insular
partition.** Use the `BRODMANN_PARTITION` constant to check::

    from ...temporal.cortex.primary_auditory_cortex import BRODMANN_PARTITION
    # BRODMANN_PARTITION = "insular"

For BA41/BA42 as cytoarchitectonic fields::

    from ...insular.brodmann_areas import brodmann_area_41_posterior_insula
    from ...insular.brodmann_areas import brodmann_area_42_posterior_insula

For the rightward asymmetry::

    from ...temporal.cortex.primary_auditory_cortex import RIGHTWARD_ASYMMETRY
    # RIGHTWARD_ASYMMETRY = True

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
*   **Rightward spectral tonotopy and pitch asymmetry:** Liégeois-Chauvel,
    C., et al. (2001). "Intracerebral evoked potentials in pitch perception
    reveal a functional asymmetry of the human auditory cortex." *Ann N Y
    Acad Sci*, 930, 117–132. PMID 11458823. In the **right hemisphere**,
    clear spectrally organized tonotopic maps were observed; in the **left
    hemisphere**, this tonotopic organization was **less evident**
    [reference:27].
*   **Pitch discrimination and right auditory cortex:** *Tonotopic maps
    and short-term plasticity in the human auditory cortex* (2004). The
    N100m dipole distance between 400- and 4000-Hz tones was **enlarged
    during pitch discrimination tasks especially in the right auditory
    cortex**[reference:28].
*   **Rightward lateralization for spectral complexity:** Hall, D.A., et
    al. (2002). "Spectral and temporal processing in human auditory
    cortex." *Cereb Cortex*, 12(2), 140–149. **Harmonic tones produced
    more activation than single tones in right Heschl's gyrus (HG)**
    [reference:29].
*   **Antero-lateral belt and spectral/temporal asymmetry:** Schönwiesner,
    M., et al. (2005). "Hemispheric asymmetry for spectral and temporal
    processing in the human antero-lateral auditory belt cortex." *Eur J
    Neurosci*, 22(6), 1521–1528. **BOLD-responses from the left and right
    Heschl's gyrus and part of the right superior temporal gyrus
    covaried with the spectral parameter**, whereas the temporal
    parameter highlighted an area on the **left superior temporal
    gyrus**[reference:30].
*   **Music and amusia (right-lateralized):** *Model of music cognition
    and amusia* (2013), *ScienceDirect*. **Right temporal lobe-damaged
    patients** show **overall impairment of music perception**; **pure
    amusia** cases involve **right superior and middle temporal gyrus
    lesions**[reference:31]. **Acquired amusia** after stroke is
    associated with **right auditory cortex damage**[reference:32].
*   **Prosody and aprosodia (right-lateralized):** *Aprosodia — overview*
    (arabpsychology.com). The **right A1–A2 region** is **more sensitive
    to the overall intonational pattern** (F0)[reference:33]. Damage to
    **right perisylvian areas** can lead to **aprosodia**
    [reference:34].
*   **Slower temporal integration in right auditory cortex:** Neophytou,
    D., et al. (2022). "Differences in temporal processing speeds between
    the right and left auditory cortex reflect the strength of recurrent
    synaptic connectivity." *PLoS Biol*, 20(10), e3001803.
    PMC9629599. The **right auditory cortex** specializes in processing
    **slower temporal components** and has **longer temporal integration
    windows** than the left[reference:35][reference:36].
*   **Contralateral ear representation:** *Native language, gender, and
    functional organization of the auditory cortex* (1999), *PNAS*,
    96(18), 10460–10465. In each hemisphere, the **contralateral ear**
    is represented by a **larger or more synchronized neuronal
    population** than the ipsilateral ear[reference:37].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Superior temporal plane and Heschl's gyrus anatomy.)
*   NeuroNames — Primary auditory cortex (right); FMA — right Heschl's
    gyrus partonomy.
"""