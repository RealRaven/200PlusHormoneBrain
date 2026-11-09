"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.brodmann_areas.brodmann_area_22
=========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── brodmann_areas
                        └── brodmann_area_22   <-- THIS MODULE

**Primary synonym:** Brodmann Area 22 (BA22); **right superior temporal
auditory/prosodic cortex**; Area temporalis superior.
**Cytoarchitectonic designation:** Area 22 of Brodmann (1909).
**Part of:** **Core Wernicke's area** (structurally), alongside **BA21,
BA41, and BA42** — but on the right side, the functional role is
**prosodic and emotional**, not semantic-linguistic.
**Location:** The **posterior segment of the superior temporal gyrus**
(STG) in the right hemisphere, encompassing the auditory association
cortex on the lateral sulcus. BA22 extends over the posterior two-thirds
of the STG up to the beginning of the vertical branch of the lateral
fissure.
**Structural parent:** This is a **Brodmann leaf** under
`.../temporal/brodmann_areas/`, **and** it has a **nested cross-listing**
under `.../gyri/superior_temporal_gyrus/wernickes_area/`.
**Lateralization status:** **Right-lateralized for emotional prosody,
affective intonation, and non-verbal auditory processing**; the left
counterpart is the **definitional Wernicke's area** and the dominant
speech-comprehension hub.

Overview
--------
Brodmann Area 22 (BA22) on the **right** side is the **superior temporal
auditory association cortex** — the right hemisphere's principal
substrate for **emotional prosody processing, affective intonation, and
non-verbal auditory analysis**. It is **structurally** a core Wernicke's
area field (BA21, BA22, BA41, BA42), but on the **right** side it does
**not** carry the speech-comprehension functions that the left BA22
carries . Instead, the right BA22 is the
**prosodic and emotional complement** to the left's speech-comprehension
hub.

**This is the right-hemisphere twin of the left BA22, and the pair
instantiates the "hemispheric dominance by function" pattern.** The two
hemispheres carry **different functions**, with **each hemisphere dominant
for a distinct domain**:

*   **The left BA22 is the left-lateralized pole** for **speech
    comprehension**, **lexical-semantic processing**, **phonological
    processing**, and **naming** (documented in the left BA22 module). It
    is the **definitional Wernicke's area**, and its lesion produces
    **Wernicke's aphasia**.

*   **The right BA22 is the right-lateralized pole** for **emotional
    prosody comprehension**, **affective intonation**, and **processing
    of negative emotions from vocal cues** . It
    is the **right-hemisphere prosodic hub**, and its lesion produces
    **aprosodia** (not aphasia).

**BA22 is structurally a core Wernicke's area field, but functionally the
right side is not a language-comprehension hub.** A consumer that needs
the speech-comprehension substrate should query the **left BA22**. A
consumer that needs the **prosodic and emotional-intonation interface**
should query the **right BA22**.

**Critical right-lateralization warning:** A right BA22 lesion produces
**aprosodia** — impaired comprehension and production of emotional
prosody — **not Wernicke's aphasia**. Wernicke's aphasia is **left-
lateralized**. The right BA22 is the **right superior temporal auditory/
prosodic cortex**, not the speech-comprehension hub, even though it lives
under the same nested "Wernicke's area" path as its left twin.

Nested BA22 Cross-Listing
-------------------------
**BA22 is the only area in the tree with a nested cross-listing** — a
Brodmann field that lives under **both** `brodmann_areas/` **and** a
gyral path:

::

    brodmann_areas/
    └── brodmann_area_22      <-- the top-level Brodmann leaf (this module)

    gyri/
    └── superior_temporal_gyrus/
        └── wernickes_area/
            └── brodmann_area_22   <-- the nested "Wernicke's-area" leaf

**On the right side, the "Wernicke's area" name is INHERITED
STRUCTURALLY, NOT FUNCTIONALLY ACCURATE.** The right nested leaf exists
because the tree mirrors the left-hemisphere structure, but its functional
content is **prosodic**, not speech-comprehension. The `right_
lateralization_warning` field in `NESTED_CROSS_LISTINGS` makes this
explicit and greppable.

**Resolution contract for consumers:**

*   If you need **right BA22 as a cytoarchitectonic field**, use this
    module (`brodmann_areas/brodmann_area_22`). It documents the laminar
    organization, boundaries, and connectivity of right BA22 as a
    Brodmann field.
*   If you need **the right "Wernicke's-area" framing**, use the nested
    module (`gyri/superior_temporal_gyrus/wernickes_area/
    brodmann_area_22`). It documents the **right prosodic functions**, not
    the speech-comprehension functions.
*   **Both paths are correct.** The two modules are **structurally
    identical** in their cytoarchitectonic constants; only the
    **functional framing** differs — and on the right, the framing is
    **prosodic, not linguistic**.
*   **Do not** assume that right BA22 lesions produce Wernicke's aphasia.
    They produce **aprosodia**.

Core Wernicke's Area Context
----------------------------
Ardila et al. (2016) distinguished between **core Wernicke's area**
(BA21, BA22, BA41, BA42) and **extended Wernicke's area** (BA20, BA37,
BA38, BA39, BA40) . **The right BA22 is
structurally in the core Wernicke's set** — the same Brodmann number as
the left BA22. But the **functional** Wernicke's area is
**left-lateralized** for language comprehension; the right homologue
carries **prosodic and emotional** functions instead
.

**This is a critical architectural point:** BA22's **membership in the
core Wernicke's set is a cytoarchitectonic fact**, not a functional claim
on the right. The right BA22 is **not** the right-hemisphere speech-
comprehension hub. It is the **right-hemisphere prosodic and emotional
hub**.

Function in the Human Brain
---------------------------
The right BA22 is a **right-lateralized prosodic and emotional-intonation
hub**. Its best-supported functions cluster into five domains:

*   **Emotional Prosody Processing (Right-Lateralized — the principal
    right-BA22 function):** The right BA22 (posterior STG/STS) is
    **crucially involved in the comprehension of affective prosody**
    . Lesion evidence shows that the **right
    posterior STG (BA22) is primarily responsible for the discrimination
    of emotional vs. neutral prosodies** , and
    that **comprehension of affective prosody is bound to a right-
    hemisphere pattern** including posterior STS (BA22), dorsolateral
    frontal (BA44/45), and orbitobasal frontal (BA47) areas
    . The **right STG (BA22/42) is activated for emotional
    vs. neutral prosodies** in near-infrared spectroscopy studies
    .

*   **Affective Intonation and Emotional Voice Analysis
    (Right-Lateralized):** The right BA22 is part of the **right
    temporal cortex** that serves as the **input region for affective-
    prosody comprehension** . Dynamic
    causal modeling shows that **right posterior STG (BA22) is the input
    region**, with information transferred to the frontal lobes via
    parallel pathways . The right BA22
    performs **early-stage analysis of affective vocal cues**
    .

*   **Negative Emotion Processing (Right-Lateralized):** The right
    hemisphere is **related to negative emotions** — fear, anger,
    sadness — and the **right STG (BA22) and right primary/secondary
    auditory cortex (BA42)** are enhanced for **negative vs. neutral
    prosodies** . This is a **right-lateralized**
    affective function.

*   **Non-Verbal Auditory Processing (Right-Lateralized):** The right
    BA22 is dominant for **non-verbal auditory processing** —
    environmental sounds, voice timbre, and paralinguistic features. The
    left carries the **semantic** and **phonological** aspects of speech;
    the right carries the **prosodic** and **voice-identity** aspects.

*   **Speech Processing (Bilateral, with Right Emphasis on Prosody):**
    The right BA22 responds to speech but with a **right-lateralized
    weighting for the prosodic and paralinguistic features**. The left
    BA22 carries the **phonological-semantic** features; the right carries
    the **melodic-affective** features.

Associated Disorders
--------------------
Damage to or dysfunction of the right BA22 is associated with:

*   **Aprosodia (Right-Lateralized — the signature right-BA22 syndrome):**
    **Impaired comprehension and/or production of emotional prosody**,
    consistent with the right BA22's role as the input region for
    affective-prosody comprehension . The patient
    has difficulty **identifying the emotional tone** of speech even
    though the words themselves are understood. This is the **right-
    hemisphere analogue of aphasia** — Ross (1981) described the
    **aprosodias** as the affective-prosodic counterpart to the left-
    hemisphere aphasias.

*   **Impaired Discrimination of Emotional vs. Neutral Prosody
    (Right-Lateralized):** Difficulty **discriminating** emotional from
    neutral intonation, consistent with the right posterior STG's
    primary role in this discrimination .

*   **Impaired Recognition of Negative Emotions from Voice
    (Right-Lateralized):** Reduced accuracy in recognizing **fear,
    anger, and sadness** from vocal cues, consistent with the right
    hemisphere's relation to negative emotions .

*   **Impaired Non-Verbal Auditory Processing (Right-Lateralized):**
    Difficulty with **environmental sounds, voice identity, and
    paralinguistic features**, consistent with the right BA22's
    non-verbal auditory role.

**What is NOT here:** **Wernicke's aphasia**, **lexical-semantic
deficits**, **phonological processing deficits**, and **naming deficits**
are **left BA22** functions. They are **absent** from right BA22 lesions.
They are documented in the left BA22 module and are **explicitly not
claimed here**. **Conduction aphasia** is a **left-perisylvian** syndrome
(left arcuate fasciculus + left BA40).

Lateralization Notes
--------------------
This is the **right** BA22 module. The lateralization landscape is
**"hemispheric dominance by function"** — each hemisphere is dominant for
a distinct domain:

*   **Right-Lateralized Functions (unique to this twin):**
    - **Emotional prosody comprehension** — affective intonation
      .
    - **Affective prosody input region** — early-stage analysis of
      affective vocal cues .
    - **Negative emotion processing** — fear, anger, sadness from voice
      .
    - **Non-verbal auditory processing** — environmental sounds, voice
      timbre .

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Speech comprehension** — the definitional Wernicke's area
      function .
    - **Lexical-semantic processing** — linking spoken words to meanings
      .
    - **Phonological processing** — analysis of speech sounds
      .
    - **Naming and word retrieval** .
    - **Auditory short-term memory and repetition** .
    - **Reading and writing** .

*   **Symmetric Functions (bilateral properties of BA22, copied verbatim
    from the left twin):**
    - **Auditory processing** of complex sounds (with left dominance for
      speech, right dominance for prosody).
    - **Basic acoustic feature analysis** (shared with BA41/42).
    - **Auditory memory** (bilateral component).
    - **Speech processing** (with left semantic, right prosodic
      weighting).

**This is the "hemispheric dominance by function" pattern at its most
extreme.** The left BA22 is the **speech-comprehension hub** (Wernicke's
area); the right BA22 is the **prosodic and emotional-intonation hub**.
Each hemisphere has a **dominant specialization**, but they are
**different specializations**, and the left's is the one that defines the
clinical aphasia syndrome.

**A consumer that assumes "right BA22 = left BA22" will be wrong for the
entire speech-comprehension domain** — the right BA22 is not Wernicke's
area. Wernicke's aphasia is **left-lateralized**; right BA22 lesions
produce **aprosodia**, not aphasia. The `right_lateralization_warning`
field makes this explicit.

**The "Wernicke's area" name is inherited structurally on the right.**
The right nested leaf exists under the same path as the left
(`gyri/superior_temporal_gyrus/wernickes_area/brodmann_area_22`), but its
functional content is **prosodic**, not speech-comprehension. A consumer
that queries the right nested leaf and expects Wernicke's area will find
the **right prosodic cortex** — same path, different function.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe (Broca's area, BA44/45) or the parietal lobe (angular
    gyrus, BA39). Those are **sibling lobes**.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Core Wernicke's area — structurally, not functionally.** BA22 is
    structurally in the core Wernicke's set (BA21, BA22, BA41, BA42),
    but the **right** BA22 does **not** carry speech-comprehension
    functions. Consumers must not assume that right BA22 lesions produce
    Wernicke's aphasia.
*   **Brodmann leaf under the temporal partition — with a nested
    cross-listing.** BA22 is a local leaf under
    `.../temporal/brodmann_areas/`, **and** it has a nested dual-framing
    module under `.../gyri/superior_temporal_gyrus/wernickes_area/
    brodmann_area_22/`.
*   **`NESTED_CROSS_LISTINGS` is data, not code.** The constant documents
    BA22's dual framing, **and explicitly notes that the right nested
    leaf is prosodic, not speech-comprehension**.
*   **No `AREA_PATHS` hop.** Unlike BA3, BA22 has a top-level leaf right
    here. The nested Wernicke's-area leaf is a **dual-framing module**,
    not a resolution target.
*   **Hemispheric dominance by function.** The left BA22 is Wernicke's
    area; the right BA22 is prosodic cortex. This module documents the
    right-lateralized functions; the left module documents the
    left-lateralized ones.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.brodmann_areas import brodmann_area_22

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.brodmann_areas.brodmann_area_22"
    )

For the nested right "Wernicke's-area" framing (prosodic cortex)::

    from ...temporal.gyri.superior_temporal_gyrus import wernickes_area
    # wernickes_area.brodmann_area_22 — same territory, PROSODIC framing;
    # NOT the speech-comprehension hub

**Both paths return the same cortical territory.** The top-level path is
the **cytoarchitectonic framing**; the nested path is the **inherited
"Wernicke's-area" framing**, which on the right is **prosodic**, not
linguistic.

For the right-lateralized functions::

    from ...temporal.brodmann_areas.brodmann_area_22 import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("emotional_prosody",
    #                      "affective_intonation",
    #                      "negative_emotion_processing",
    #                      "nonverbal_auditory_processing")

For the nested cross-listing::

    from ...temporal.brodmann_areas.brodmann_area_22 import NESTED_CROSS_LISTINGS
    # NESTED_CROSS_LISTINGS["brodmann_area_22"] documents both paths,
    # with a right_lateralization_warning

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
*   **Right-hemisphere prosody — the aprosodias:** Ross, E.D. (1981).
    "The aprosodias: functional-anatomic organization of the affective
    components of language in the right hemisphere." *Arch Neurol*,
    38(9), 561–569. The right hemisphere carries the **affective-prosodic**
    counterpart of language; right lesions produce **aprosodias**, not
    aphasias.
*   **Right posterior STG (BA22) and emotional vs. neutral prosody
    discrimination:** *The right posterior superior temporal gyrus (BA22)
    is primarily responsible for the discrimination of emotional vs.
    neutral prosodies* (cited from prosody literature).
*   **Right-hemisphere pattern for affective prosody:** Wildgruber, D.,
    et al. (2005). "Identification of emotional intonation evaluated by
    fMRI." *NeuroImage*, 24(4), 1233–1241. Comprehension of affective
    prosody is bound to a **right-hemisphere pattern** including posterior
    STS (BA22), dorsolateral (BA44/45), and orbitobasal (BA47) frontal
    areas .
*   **Right posterior STG as input region for affective prosody:**
    *Cerebral pathways in processing of affective prosody: A dynamic
    causal modeling study* (2005), *NeuroImage*. Activation within the
    **right posterior middle temporal gyrus** during evaluation of
    affective prosody; the **right temporal cortex serves as the input
    region** for affective-prosody comprehension, with information
    transferred to the frontal lobes via parallel pathways
    .
*   **Right STG (BA22/42) and emotional vs. neutral prosody:** *Speech
    Prosodies of Different Emotional Categories Activate Different Brain
    Regions in Adult Cortex: an fNIRS Study* (2018), *Sci Rep*, 8, 607.
    The **right posterior STG (BA22) and right primary/secondary AC
    (BA42)** are enhanced for emotional vs. neutral prosodies
    .
*   **Right hemisphere and negative emotions:** *Speech Prosodies* (2018),
    *Sci Rep*. The **right hemisphere is related to negative emotions**;
    the right STG (BA22) and right primary/secondary AC (BA42) are
    enhanced for **negative vs. neutral prosodies** .
*   **Core vs extended Wernicke's area:** Ardila, A., et al. (2016).
    "How Extended Is Wernicke's Area? Meta-Analytic Connectivity Study
    of BA20 and Integrative Proposal." *Neurosci J*, 2016, 4962562.
    Core Wernicke's area ≈ BA21, BA22, BA41, BA42; extended Wernicke's
    area ≈ BA20, BA37, BA38, BA39, BA40 .
*   **Interhemispheric microcircuitry differences:** *Interhemispheric
    Asymmetries of the Modular Structure in Human Temporal Cortex*
    (2000), *Science*. Language-relevant processing of auditory signals
    is lateralized and involves the posterior part of BA22; functional
    lateralization is accompanied by interhemispheric differences in
    intrinsic microcircuitry .
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed.
*   NeuroNames — Brodmann area 22 (right); FMA — Brodmann area 22 (right
    member).
"""