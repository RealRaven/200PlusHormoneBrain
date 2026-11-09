"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex.anterior_temporal_lobe
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── cortex
                        └── anterior_temporal_lobe   <-- THIS MODULE

**Primary synonym:** Anterior temporal lobe (ATL), right; Right ATL;
Temporal pole region; Anterior temporal cortex.
**Organizing principle:** **Functional–anatomical region** — the
anterior portion of the temporal lobe, including the temporal pole and
the anterior segments of the temporal gyri.
**Brodmann constitution:** **BA38 (temporal pole)** plus the anterior
portions of **BA20 (inferior temporal)**, **BA21 (middle temporal)**,
and **BA22 (superior temporal)** — a **multi-field functional region**,
not a single cytoarchitectonic area.
**Part of:** The **functional partition** of the right temporal lobe
(``.../temporal/cortex``), alongside A1, A2, ITC, pITC, and MT.
**Cytoarchitectonic siblings:** ``.../temporal/brodmann_areas/brodmann_area_38``,
``.../temporal/brodmann_areas/brodmann_area_20``,
``.../temporal/brodmann_areas/brodmann_area_21`` — the same territory,
partitioned differently. See "Two-Partition Context" below.

Overview
--------
The **right anterior temporal lobe (ATL)** is the **right-hemisphere
non-verbal and social/emotional semantic hub** — the **principal
cortical substrate for person knowledge, social concepts, and affective
semantics** in the human brain. It is a **supramodal convergence zone**
where information from multiple sensory and cognitive modalities
converges to form **amodal conceptual representations**, but on the
**right** side the representational emphasis falls on **non-verbal,
social, and emotional** content rather than on verbal semantics.

**This is the right-hemisphere twin of the left ATL, and the pair
instantiates the "left-verbal / right-non-verbal" specialization
model.** The two hemispheres carry **different semantic specializations**,
with causal evidence from repetitive transcranial magnetic stimulation
(rTMS) showing that:

- **Left ATL stimulation, but not right ATL stimulation, eliminates
  semantic priming for words** — verbal semantics is represented in the
  left ATL[reference:0].
- **rTMS over either ATL eliminates semantic priming for objects** —
  non-verbal object semantics relies on **both** left and right ATL
  computations, with the right ATL contributing the **non-verbal semantic
  computations** and the left ATL providing **"verbal label" feedback**
  [reference:1].

**The right ATL is the right-hemisphere pole of a functionally
asymmetric pair.** The **right ATL** is specialized for **non-verbal
semantics** — person knowledge, social concepts, emotional meaning, and
face-related semantic information. The **left ATL** is specialized for
**verbal semantics** — word meanings, verbal concepts, and lexical-
semantic processing. This is a **"left-verbal / right-non-verbal"
specialization model**, supported by rTMS, neuroimaging, and clinical
evidence.

**The right ATL is the first functional region in the tree whose
lateralization is defined by a *semantic domain split* rather than by a
sensory, motor, or spatial domain split.** Unlike BA22 (speech vs.
prosody), BA37 (words vs. faces), or BA7 (attention vs. bimanual
control), the ATL pair divides the **conceptual system** into
**verbal (left)** and **non-verbal/social (right)** components — a
distinction that is **representational**, not sensorimotor.

Two-Partition Context
---------------------
This module is the **functional-region node** for the right ATL. It is
**constituted by** Brodmann-area leaves that are wired under the sibling
cytoarchitectonic partition:

::

    Functional partition (this module)     Cytoarchitectonic partition
    ──────────────────────────────────     ────────────────────────────
    anterior_temporal_lobe          ──┐
                                     ├──▶  brodmann_area_38  (temporal
                                     │      pole; core ATL field)
                                     ├──▶  brodmann_area_20  (anterior
                                     │      inferior temporal)
                                     ├──▶  brodmann_area_21  (anterior
                                     │      middle temporal)
                                     └──▶  brodmann_area_22  (anterior
                                            superior temporal; partially)

**The ATL is a multi-field functional region, not a single Brodmann
area.** Unlike S1 (which maps cleanly to BA3/BA1/BA2) or MT (which maps
to BA19), the ATL **spans multiple Brodmann fields** and **partial
territories** of those fields. Consumers that need the full ATL must
query **all four Brodmann leaves** — or, more practically, use this
functional region node as the **supramodal semantic hub**.

**The ATL is also the first functional region in the tree whose
Brodmann constitution includes a partially shared field (BA22).**
BA22 is **fully** the superior temporal language area on the left, but
only its **anterior segment** contributes to the ATL. The posterior
BA22 (Wernicke's area) is **not** part of the ATL. This makes the ATL's
Brodmann mapping **territorially partial**, not whole-field.

Functional Subregions
---------------------
A large-scale meta-analytic investigation identified **four functional
subregions** within the ATL, organized along **dorsal and ventral
aspects**[reference:2]:

- **Superior dorsal ATL** — associated with **auditory sensory,
  language (phonological production), and emotion**[reference:3].
- **Inferior dorsal ATL** — associated with **auditory sensory and
  language (phonological perception and production)**[reference:4].
- **Lateral ATL** — associated with **visual sensory, language
  (semantic and episodic), and social processing**[reference:5].
- **Ventromedial ATL** — associated with **visual sensory, episodic
  memory, and emotion**[reference:6].

**These four subregions are functionally dissociable within a single
structural region.** On the **right** side, the **lateral** subregion's
social-processing dimension and the **ventromedial** subregion's
emotion dimension are **more heavily weighted** than on the left, in
keeping with the right ATL's specialization for social/emotional
semantics.

Function in the Human Brain
---------------------------
The right ATL is the **right-lateralized non-verbal and social/emotional
semantic hub**. Its best-supported functions cluster into six domains:

- **Non-Verbal Object Semantics (Bilateral, with Right Computation
  Emphasis):** rTMS over the **right ATL** eliminates semantic priming
  for objects, and the finding that **either-side ATL stimulation**
  disrupts object priming suggests that **non-verbal object semantics
  depends on semantic computations in the right ATL** combined with
  verbal-label feedback from the left ATL[reference:7][reference:8].

- **Person Knowledge and Social Semantics (Right-Lateralized —
  the principal right-ATL function):** The right ATL is associated with
  **person-related semantic information** — **familiar faces** and
  **social concepts**. Laterality effects show the **left ATL is
  associated with processing names** and the **right ATL with familiar
  faces**[reference:9]. Right ATL activity reflects recall of **faces and
  person-related semantic information**[reference:10].

- **Social Concept Representation (Right-Emphasis):** Socially related
  words (e.g., "polite") versus nonsocial words (e.g., "nutritious")
  localize to the **right anterior superior temporal gyrus** in
  neurologically intact participants, with the **right > left** pattern
  being most consistent for the social-concept dimension[reference:11].

- **Affective and Emotional Semantics (Right-Lateralized):** The right
  ATL supports **emotional meaning** — the affective significance of
  concepts and the **loss of emotional meaning** is a hallmark of
  right-predominant semantic dementia[reference:12].

- **Supramodal Semantic Integration (Bilateral Contribution):** The ATL
  as a whole is a **supramodal hub** for verbal and nonverbal semantic
  information[reference:13]. The **right ATL** is the **non-verbal pole**
  of this hub, integrating **visual, auditory, and affective**
  information into amodal representations.

- **Verbal Label Feedback Integration (Bilateral):** Semantic processing
  of visual objects depends on **right ATL semantic computations** and on
  **left ATL verbal-label feedback**[reference:14]. The right ATL is the
  **non-verbal semantic partner** in this twofold mechanism.

Associated Disorders
--------------------
Damage to or dysfunction of the right ATL is associated with:

- **Right Temporal Variant of Semantic Dementia (Right-Lateralized — the
  signature right-ATL syndrome):** The **right temporal variant of
  semantic dementia (rSD)** is characterized by **right-predominant
  anterior temporal atrophy** and presents with **prosopagnosia, loss of
  emotional meaning, and behavioral changes** rather than verbal
  semantic deficits[reference:15][reference:16]. **About one-third of focal
  anterior temporal neurodegeneration cases** present with this
  right-predominant pattern[reference:17].

- **Prosopagnosia (Right-Lateralized):** **Impaired recognition of
  familiar faces** is a core feature of the right temporal variant of
  semantic dementia[reference:18].

- **Loss of Emotional Meaning (Right-Lateralized):** Impaired
  **emotional semantic knowledge** — the affective significance of
  concepts — is a hallmark of the right temporal variant[reference:19].

- **Behavioral Changes and Loss of Empathy (Right-Lateralized):** The
  right temporal variant is associated with **behavioral disturbances**
  and **loss of empathy**, often preceding language deficits
  [reference:20][reference:21].

- **Impaired Social Cognition (Right-Lateralized):** Difficulty with
  **social concept processing** and **emotional recognition** follows
  right ATL damage[reference:22].

**What is NOT here:** **Anomia**, **verbal semantic loss**, and
**surface dyslexia/dysgraphia** are **left ATL** syndromes. They are
**absent** from right ATL lesions. They are documented in the left ATL
module and are **explicitly not claimed here**.

Lateralization Notes
--------------------
This is the **right** ATL module. The lateralization landscape is
**left-verbal / right-non-verbal specialization** — a
**representational domain split**, not a sensorimotor or spatial split:

- **Right-Lateralized Functions (dominant in this twin):**
  - **Non-verbal object semantics** — semantic computations in the right
    ATL[reference:23].
  - **Person knowledge and familiar faces**[reference:24].
  - **Social concepts** — right anterior STG/ATL[reference:25].
  - **Emotional meaning** — affective semantics[reference:26].

- **Left-Lateralized Functions (contrast — absent here):**
  - **Verbal semantic memory** — word meanings and verbal concepts.
  - **Lexical-semantic processing** — mapping word forms to meanings.
  - **Verbal label feedback** — left ATL's guiding role in object
    semantics[reference:27].
  - **Anomic aphasia** and **verbal comprehension deficits** following
    left ATL damage.

- **Symmetric Functions (bilateral properties of the ATL hub):**
  - **Supramodal semantic integration**[reference:28].
  - **Conceptual knowledge and categorization**.
  - **Object semantics** (requiring both right computations and left
    verbal feedback).

**The "left-verbal / right-non-verbal" pattern is the defining
lateralization of the ATL pair.** Unlike the parallel-laden BA37
(words vs. faces) or the hemispheric-dominance BA22 (speech vs.
prosody), the ATL splits the **conceptual system** into **verbal
(left)** and **non-verbal/social (right)** components. This is a
**representational division of labor**, not a sensorimotor one.

**A consumer that assumes "right ATL = left ATL" will miss the
right-lateralized non-verbal, social, and emotional semantic functions.**
The two hemispheres are **not interchangeable** for semantic processing
— they are **specialized for different semantic domains**.

Design Contract
---------------
- **No side effects on import.** Pure namespace.
- **No cross-hemisphere imports.** Right side only.
- **No cross-lobe imports.** This module does **not** import from the
  frontal lobe or the parietal lobe. Those are **sibling lobes**.
- **No hormone imports.** Dependency DAG unchanged:
  ``chemicals_hormones → memory → brainparts``.
- **Multi-field functional region — flagged in prose and data.** The
  ATL is **not a single Brodmann area**. It encompasses **BA38** and the
  **anterior segments of BA20, BA21, and BA22**. The
  ``REGION_TO_BRODMANN`` constant below makes the multi-field mapping
  explicit.
- **Partial-field mapping — flagged in data.** The ATL includes only the
  **anterior segment** of BA22, not the full BA22 (which is Wernicke's
  area). The ``PARTIAL_FIELDS`` constant below documents this.
- **Left-verbal / right-non-verbal specialization — flagged in data.**
  The ``RIGHT_LATERALIZED`` constant documents the right-lateralized
  non-verbal/social semantic functions.
- **Four functional subregions — flagged in data.** The ``SUBREGIONS``
  constant documents the superior dorsal, inferior dorsal, lateral, and
  ventromedial subregions.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.cortex import anterior_temporal_lobe

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.cortex.anterior_temporal_lobe"
    )

For the Brodmann constitution::

    from ...temporal.cortex.anterior_temporal_lobe import (
        REGION_TO_BRODMANN, PARTIAL_FIELDS,
    )
    # REGION_TO_BRODMANN["anterior_temporal_lobe"] = (
    #     "brodmann_area_38", "brodmann_area_20",
    #     "brodmann_area_21", "brodmann_area_22"
    # )
    # PARTIAL_FIELDS = ("brodmann_area_22",)  # only anterior segment

For the functional subregions::

    from ...temporal.cortex.anterior_temporal_lobe import SUBREGIONS
    # SUBREGIONS["superior_dorsal"], ["inferior_dorsal"],
    # SUBREGIONS["lateral"], ["ventromedial"]

For the right-lateralized functions::

    from ...temporal.cortex.anterior_temporal_lobe import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("non_verbal_object_semantics",
    #                      "person_knowledge_familiar_faces",
    #                      "social_concepts", "emotional_meaning")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        atl_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.cortex.anterior_temporal_lobe"
        )
        # resolve atl_path through the memory/recall layer

References
----------
* **Left-verbal / right-non-verbal specialization (rTMS evidence):**
  Uno, T., Teichmann, M., Takano, K., & Nakamura, K. (2026). “The
  Anterior Temporal Semantic Hub in the Left and Right Hemispheres: A
  Unitary System or Two Separate Systems for Meaning?” *J Neurosci*,
  46(5), e1715252025. Left ATL stimulation, but not right ATL
  stimulation, eliminated semantic priming for words; rTMS over either
  ATL eliminated semantic priming for objects[reference:29].
* **Right ATL and non-verbal semantics:** *The functional architecture
  of the semantic hub* (2025), *ScienceDirect*. Semantic priming in the
  object-decision task was altered by both left and right ATL
  stimulation, suggesting non-verbal semantic information relies on
  functional coordination of the left and right ATL[reference:30].
* **Right ATL and person knowledge:** *The Selectivity and Functional
  Connectivity of the Anterior Temporal Lobes* (2009), *PMC*. Right
  anterior temporal activity reflects recall of **faces and person-
  related semantic information**[reference:31].
* **Right ATL and social concepts:** Zahn, R., et al. (2007). “Social
  concepts are represented in the superior anterior temporal cortex.”
  *PNAS*, 104(15), 6430–6435. Socially related words versus nonsocial
  words localized to the **right anterior STG** in neurologically intact
  participants[reference:32].
* **Laterality of names vs. faces:** *Graded specialization within and
  between the anterior temporal lobes* (2015), *PMC*. The **left ATL is
  associated with processing names** and the **right ATL with familiar
  faces**[reference:33].
* **ATL functional subregions:** *Functional subdivisions in the
  anterior temporal lobes: a large scale meta-analytic investigation*
  (2020), *Neurosci Biobehav Rev*, 115, 134–145. Four subregions:
  superior dorsal, inferior dorsal, lateral, ventromedial
  [reference:34].
* **ATL Brodmann constitution:** *Functional subdivisions* (2020). The
  ATL encompasses the **temporal pole (BA38)** and the **anterior
  segments of temporal gyri (BA20, 21, 22)**[reference:35].
* **Right temporal variant of semantic dementia:** *Semantic Dementia —
  an overview* (ScienceDirect). Right-predominant atrophy is associated
  with **prosopagnosia, loss of emotional meaning, and behavioral
  changes**[reference:36]. About **one-third** of focal anterior temporal
  neurodegeneration cases present with right-predominant atrophy
  [reference:37].
* **ATL connectivity:** Uno et al. (2026). The left and right ATLs have
  **different patterns of functional/structural connectivity** with
  domain-specific areas; fiber tract connections between the **right ATL
  and right posterior temporal cortex** correlate with **nonverbal
  semantics**[reference:38].
* Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
  Brain*, 4th ed. (Anterior temporal and temporal pole anatomy.)
* NeuroNames — Anterior temporal lobe (right); FMA — right anterior
  temporal lobe partonomy.
"""