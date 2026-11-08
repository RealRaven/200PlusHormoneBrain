"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex.secondary_auditory_cortex
==========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── cortex
                        └── secondary_auditory_cortex   <-- THIS MODULE

**Primary synonym:** Secondary auditory cortex (A2), right; Right A2;
Auditory association cortex; Auditory belt/parabelt; Right superior
temporal auditory/prosodic cortex.
**Organizing principle:** **Functional–anatomical region** — the
auditory association cortex surrounding the primary auditory core.
**Brodmann constitution:** **BA22** (the posterior superior temporal
gyrus) **plus BA42** (the lateral belt/parakoniocortex). BA42 is wired
under the **insular partition** in the tree's `brodmann_areas`; BA22 is
wired under the **temporal partition** with a **nested cross-listing**
under the superior temporal gyrus.
**Location:** The **superior temporal gyrus (STG)** and **superior
temporal sulcus (STS)** , lateral and posterior to the primary auditory
cortex (Heschl's gyrus) on the superior temporal plane of the **right**
hemisphere.
**Structural parent:** Child of ``.../temporal/cortex`` (the functional
partition of the temporal lobe).
**Cytoarchitectonic type:** **Neocortical (parakoniocortical /
dysgranular)** — A2 is a **higher-order auditory association area** with
a **less prominent layer IV** than the koniocortical A1, and a **more
developed layer III** for cortico-cortical output.

Overview
--------
The **right secondary auditory cortex (A2)** is the **right-hemisphere
auditory association cortex** — the **principal cortical substrate for
the transformation of acoustic features into meaningful auditory
objects**, with a **rightward weighting for spectral processing, pitch,
music, and emotional prosody**. It sits in the **belt and parabelt** of
the auditory cortical hierarchy, lateral and posterior to the primary
auditory core (A1), and it is the **anatomical and functional bridge**
between basic acoustic analysis (A1) and higher-order **spectral and
prosodic** processing.

**This is the right-hemisphere twin of the left A2, and the pair
instantiates the "temporal/spectral dichotomy"** — the **first
auditory-domain lateralization** documented in the tree. The two
hemispheres carry **different emphases** within the same auditory-
association cascade:

*   **The left A2 is the left-lateralized pole** for **fast temporal
    processing and speech** — it decodes the **rapid temporal
    perturbations** that distinguish phonemes and syllables, and it
    contains **Wernicke's area** (BA22).

*   **The right A2 is the right-lateralized pole** for **spectral
    processing, pitch, music, and prosody** — it analyzes the **frequency
    content** of complex sounds, supports **musical pitch and melody
    perception**, and processes the **emotional intonation of speech**.
    Its damage produces **amusia** and **aprosodia**, not aphasia.

**A2 is the first functional region in the tree whose primary Brodmann
anchor (BA22) has a nested cross-listing.** The top-level Brodmann leaf
``temporal.brodmann_areas.brodmann_area_22`` and the nested Wernicke's-
area leaf ``temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22``
both represent the same cortical territory — BA22. On the **right**
side, the "Wernicke's area" name is **inherited structurally, not
functionally accurate**: the right BA22 is the **right superior
temporal auditory/prosodic cortex**, not the speech-comprehension hub.

**The right A2 is the cortical substrate of amusia and aprosodia.**
Damage to the **right posterior STG (BA22)** and adjacent right temporal
areas produces **amusia** (impaired music perception) and **aprosodia**
(impaired comprehension/production of emotional prosody), not
Wernicke's aphasia. This is the **right-lateralized signature** of A2
pathology.

Cross-Lobe Mapping
------------------
A2's Brodmann constitution **spans two partitions**:

::

    Functional region (this module)     Brodmann mapping      Brodmann partition
    ───────────────────────────────     ─────────────────      ──────────────────
    secondary_auditory_cortex       ──▶  BA42 (lateral belt)   **insular** (not temporal)
                                    ──▶  BA22 (parabelt;      temporal (nested
                                         prosodic cortex)     cross-listing)

**Consumers must not assume that a temporal Brodmann query returns the
full A2 constitution.** BA42 lives under the **insular** partition; BA22
lives under the **temporal** partition with a nested cross-listing.

**Resolution contract for consumers:**

*   If you need **A2 as a functional region**, use this module.
*   If you need **BA42 (lateral belt)**, query
    ``insular.brodmann_areas.brodmann_area_42_posterior_insula``.
*   If you need **BA22 (right prosodic cortex)**, query
    ``temporal.brodmann_areas.brodmann_area_22`` or the nested
    ``temporal.gyri.superior_temporal_gyrus.wernickes_area.brodmann_area_22``.
    **Do not** assume that right BA22 lesions produce Wernicke's aphasia.
    They produce **aprosodia**.

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
    **auditory object recognition and auditory scene analysis**. On the
    **right** side, the parabelt's contribution is weighted toward
    **spectral, pitch, and prosodic** dimensions rather than speech
    semantics.

**This belt-parabelt architecture is the defining structural fact about
A2.** A1 is the **entry point**; A2 is the **transformation stage** where
**acoustic features become auditory objects** — with a **rightward
spectral/pitch/prosodic weighting**.

Function in the Human Brain
---------------------------
The right A2 is the **right-lateralized spectral, pitch, music, and
prosodic processing hub**. Its best-supported functions cluster into six
domains — **five symmetric with the left twin and one right-lateralized
emphasis**:

*   **Spectral Processing (Right-Lateralized — the defining right-A2
    function):** The **right-hemisphere belt cortical areas** show
    **complementary specialization for spectral processing** — the
    analysis of the **frequency content** of complex sounds.
    **Responses to spectral features are weighted toward the right**,
    while responses to temporal features are weighted toward the left[reference:0].

*   **Pitch Processing and Melody (Right-Lateralized):** The **right
    secondary auditory cortex is central in various aspects of musical
    pitch processing** — melodic processing, pitch judgments within
    melodies, discrimination of pitch and duration, and timbre
    judgments[reference:1]. The **right superior temporal gyrus recruits
    and evaluates contour information** (pitch direction), while both
    temporal regions evaluate interval information. The
    right anterolateral part of Heschl's gyrus is also concerned with
    **pitch information processing**.

*   **Music Perception and Amusia (Right-Lateralized):** The **right
    hemisphere is dominant for the global analysis of melody and pitch
    contour**, integrating successive tones into a coherent whole.
    **Right-hemisphere lesions, particularly in the superior temporal
    gyrus, frequently result in profound receptive amusia**, leaving
    language relatively intact[reference:4]. **Acquired amusia** is
    associated with lesions comprising the **superior temporal gyrus,
    Heschl's gyrus, insula, and striatum in the right hemisphere**[reference:5].
    The right superior temporal gyrus is the **key node** for amusia[reference:6].

*   **Emotional Prosody (Right-Lateralized):** The **right posterior STG
    (BA22) and right primary/secondary auditory cortex (BA42)** are
    **significantly more activated for emotional vs. neutral prosodies**
    [reference:7]. While the main effect of speech prosody has leftward
    lateralization, the **contrast of emotional vs. neutral prosodies
    within these areas shows rightward lateralization**[reference:8].
    **Comprehension of affective prosody** is bound to a distinct
    **right-hemisphere pattern** encompassing posterior STS (BA22),
    dorsolateral (BA44/45), and orbitobasal (BA47) areas[reference:9].

*   **Auditory Working Memory and Pattern Recognition (Bilateral):** A2
    supports **auditory working memory** and **pattern recognition in
    the auditory domain** — the ability to hold and manipulate acoustic
    information over short periods. This is a **bilateral** foundation.

*   **Integration with Visual Information (Bilateral):** A2 contributes
    to **integration with visual information** — e.g., **lip reading**
    and **audiovisual speech perception** — via connections to the
    posterior STS[reference:10]. This is a **bilateral** function.

Associated Disorders
--------------------
Damage to or dysfunction of the right A2 is associated with:

*   **Amusia (Right-Lateralized — the signature right-A2 syndrome):**
    **Acquired amusia** — the loss of music perception — follows **right
    temporal lobe lesions**, particularly involving the **right superior
    temporal gyrus, Heschl's gyrus, insula, and striatum**[reference:11].
    **Pure amusia** cases involve **right superior and middle temporal
    gyrus lesions**[reference:12]. **Right-hemisphere lesions in the
    superior temporal gyrus frequently result in profound receptive
    amusia**, leaving language relatively intact[reference:13].

*   **Aprosodia (Right-Lateralized):** **Impaired comprehension and/or
    production of emotional prosody** — the emotional and intonational
    melody of speech — follows **right perisylvian damage**.
    **Right BA22 aids in the interpretation of prosody**, and **damage
    causes sensory aprosodia**, with the patient unable to comprehend
    changes in voice and body language.

*   **Impaired Pitch Processing (Right-Lateralized):** **Impaired pitch
    perception** for complex tones and melodies, following **right
    auditory cortex lesions**[reference:15].

*   **Impaired Spectral Processing (Right-Lateralized):** **Difficulty
    analyzing the spectral content** of complex sounds, following right
    A2 damage.

*   **Auditory Agnosia (Bilateral or Right-Lateralized):** Impaired
    **recognition of environmental sounds or music** (as distinct from
    speech) when early perceptual processing is preserved.

**What is NOT here:** **Wernicke's aphasia**, **pure word deafness**,
**phoneme discrimination deficits**, and **fast temporal processing
deficits** are **left A2** functions. They are **absent** from right A2
lesions. They are documented in the left A2 module and are **explicitly
not claimed here**. The right A2 is the **spectral/pitch/music/prosody**
pole; the left A2 is the **speech/fast-temporal** pole.

Lateralization Notes
--------------------
This is the **right** A2 module. The lateralization landscape is the
**temporal/spectral dichotomy** — a **sensory-domain weighting** for
spectral, pitch, music, and prosodic processing:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Spectral processing** — complementary specialization in
      right-hemisphere belt cortical areas[reference:16].
    - **Pitch processing** — musical pitch, melody, contour[reference:17].
    - **Music perception** — amusia follows right temporal lesions
      [reference:18].
    - **Emotional prosody** — rightward lateralization for emotional vs.
      neutral prosodies[reference:19].
    - **Aprosodia** — the right-A2 signature syndrome.

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Fast temporal processing** — rapid acoustic perturbations
      [reference:21].
    - **Speech sound processing** — phoneme and syllable decoding.
    - **Wernicke's area** — language comprehension.
    - **Wernicke's aphasia** — the left-A2 signature syndrome.

*   **Symmetric Functions (bilateral properties of A2):**
    - Processing of complex acoustic patterns.
    - Auditory working memory and pattern recognition.
    - Integration with visual information (lip reading).
    - Timbre processing.

**This is the "rightward sensory weighting" pattern** — the **mirror
image of the left A2's leftward speech weighting**. The **left
hemisphere is the dominant speech/fast-temporal processor**; the **right
hemisphere is the dominant spectral/pitch/music/prosody processor**.
Neither hemisphere is the "dominant" one; they are **specialized for
different acoustic dimensions**.

**A consumer that assumes "right A2 = left A2" will miss the rightward
spectral, pitch, music, and prosody weighting** — but the right twin is
**not** merely "denying" the left's speech functions; it is **carrying
a spectral/pitch-specialized subset** of the auditory-association
function.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
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
    ``RIGHTWARD_ASYMMETRY`` constant documents the rightward functional
    asymmetry for spectral, pitch, music, and prosodic processing.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex import secondary_auditory_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.cortex.secondary_auditory_cortex"
    )

For the Brodmann constitution::

    from ...temporal.cortex.secondary_auditory_cortex import BRODMANN_MAPPING
    # BRODMANN_MAPPING = {
    #     "brodmann_area_42": "insular",   # lateral belt
    #     "brodmann_area_22": "temporal",  # parabelt (nested)
    # }

For the rightward asymmetry::

    from ...temporal.cortex.secondary_auditory_cortex import RIGHTWARD_ASYMMETRY
    # RIGHTWARD_ASYMMETRY = True

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
*   **Temporal/spectral dichotomy:** Zatorre, R.J., & Belin, P. (2001).
    "Spectral and temporal processing in human auditory cortex." *Cereb
    Cortex*, 11(10), 946–953. **Responses to temporal features were
    weighted toward the left, spectral features toward the right**;
    **right-hemisphere belt cortical areas** show **complementary
    specialization for spectral processing**[reference:22].
*   **Right secondary auditory cortex and musical pitch:** *Many findings
    have shown that musical pitch processing preferentially involves
    right auditory cortical structures* (MPG Pure). The **right
    secondary auditory regions are central in musical pitch processing**
    — melodic processing, pitch judgments, timbre judgments
    [reference:23].
*   **Amusia and right superior temporal gyrus:** Sihvonen, A.J., et al.
    (2016). "Neural Basis of Acquired Amusia and Its Recovery after
    Stroke." *J Neurosci*, 36(34), 8872–8881. **Amusia is associated
    with a lesion area comprising the superior temporal gyrus, Heschl's
    gyrus, insula, and striatum in the right hemisphere**[reference:24].
*   **Pure amusia and right STG/MTG:** *[Music Processing in the Brain:
    Neuropsychological Approach Through Findings of Patients with
    Amusia]* (2017), *Brain Nerve*, 69(6), 615–627. **Pure amusia cases
    included right superior and middle temporal gyrus lesion
    involvement**[reference:25].
*   **Right-hemisphere dominance for melody and amusia:** *Amusia*
    (scales.arabpsychology.com). The **right hemisphere is dominant for
    the global analysis of melody and pitch contour**; **right-hemisphere
    lesions, particularly in the superior temporal gyrus, frequently
    result in profound receptive amusia**[reference:26].
*   **Prosody and right STG/BA22/BA42:** *Speech Prosodies of Different
    Emotional Categories Activate Different Brain Regions* (2018), *Sci
    Rep*, 8, 607. **Emotional prosodies activated the right STG (BA22)
    and right primary/secondary AC (BA42)**; the **contrast of emotional
    vs. neutral prosodies showed rightward lateralization**[reference:27].
*   **Affective prosody and right-hemisphere pattern:** Wildgruber, D.,
    et al. (2005). "Identification of emotional intonation evaluated by
    fMRI." *NeuroImage*, 24(4), 1233–1241. **Comprehension of affective
    prosody is bound to a right-hemisphere pattern** encompassing
    posterior STS (BA22), dorsolateral (BA44/45), and orbitobasal (BA47)
    areas[reference:28].
*   **Sensory aprosodia and right BA22:** *Brodmann Area 22 — Superior
    Temporal Gyrus* (Neurofeedback Academy). **Prosody and emotional
    speech processing (right)**; **sensory aprosodia (right)**;
    **right BA22 aids in the interpretation of prosody, and damage
    causes sensory aprosodia**[reference:29].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Superior temporal gyrus and sulcus anatomy.)
*   NeuroNames — Secondary auditory cortex (right); FMA — right superior
    temporal gyrus partonomy.
"""