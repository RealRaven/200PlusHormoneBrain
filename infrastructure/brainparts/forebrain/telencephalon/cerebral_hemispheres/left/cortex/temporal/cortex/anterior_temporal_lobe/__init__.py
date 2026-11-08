"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex.anterior_temporal_lobe
======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── cortex
                        └── anterior_temporal_lobe   <-- THIS MODULE

**Primary synonym:** Anterior temporal lobe (ATL), left; Left ATL;
Temporal pole region; Anterior temporal cortex.
**Organizing principle:** **Functional–anatomical region** — the
anterior portion of the temporal lobe, including the temporal pole and
the anterior segments of the temporal gyri.
**Brodmann constitution:** **BA38 (temporal pole)** plus the anterior
portions of **BA20 (inferior temporal)**, **BA21 (middle temporal)**,
and **BA22 (superior temporal)** — a **multi-field functional region**,
not a single cytoarchitectonic area.
**Part of:** The **functional partition** of the left temporal lobe
(``.../temporal/cortex``), alongside A1, A2, ITC, pITC, and MT.
**Cytoarchitectonic siblings:** ``.../temporal/brodmann_areas/brodmann_area_38``,
``.../temporal/brodmann_areas/brodmann_area_20``,
``.../temporal/brodmann_areas/brodmann_area_21`` — the same territory,
partitioned differently. See "Two-Partition Context" below.

Overview
--------
The **left anterior temporal lobe (ATL)** is the **left-hemisphere
semantic hub** — the **principal cortical substrate for verbal semantic
memory** in the human brain. It is a **supramodal convergence zone**
where information from multiple sensory and cognitive modalities
converges to form **amodal conceptual representations** — the meanings
of words, objects, people, and ideas, independent of the sensory
modality through which they were experienced[reference:0][reference:1].

**The ATL is not a single Brodmann area.** It is a **functional region**
that encompasses the **temporal pole (BA38)** and the **anterior
segments of the temporal gyri (BA20, BA21, BA22)**[reference:2]. It is
a **multi-field, multi-cytoarchitectonic territory** whose functions are
defined by **convergent connectivity** and **semantic representation**,
not by a single laminar pattern.

**The left ATL is the left-hemisphere pole of a functionally asymmetric
pair.** The **left ATL** is specialized for **verbal semantics** — word
meanings, verbal concepts, and lexical-semantic processing. The **right
ATL** is specialized for **non-verbal and social/emotional semantics** —
person knowledge, social concepts, and affective associations. This is
a **"left-verbal / right-non-verbal" specialization model**,
supported by recent causal evidence from repetitive transcranial
magnetic stimulation (rTMS)[reference:3][reference:4][reference:5].

**The left ATL is the first functional region in the tree whose
lateralization is defined by a *semantic domain split* rather than by a
sensory, motor, or spatial domain split.** Unlike BA22 (speech vs.
prosody), BA37 (words vs. faces), or BA7 (attention vs. bimanual
control), the ATL pair divides the **conceptual system** into
**verbal (left)** and **non-verbal/social (right)** components — a
distinction that is **representational**, not sensorimotor.

Two-Partition Context
---------------------
This module is the **functional-region node** for the left ATL. It is
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
aspects**[reference:6]:

*   **Superior dorsal ATL** — associated with **auditory sensory,
    language (phonological production), and emotion**[reference:7].
*   **Inferior dorsal ATL** — associated with **auditory sensory and
    language (phonological perception and production)**[reference:8].
*   **Lateral ATL** — associated with **visual sensory, language
    (semantic and episodic), and social processing**[reference:9].
*   **Ventromedial ATL** — associated with **visual sensory, episodic
    memory, and emotion**[reference:10].

**These four subregions are functionally dissociable within a single
structural region.** The ATL is not a homogeneous semantic "blob"; it is
a **topographically organized convergence zone** whose subregions
differentially weight sensory, language, and socioemotional dimensions.

Function in the Human Brain
---------------------------
The left ATL is the **left-lateralized verbal semantic hub**. Its
best-supported functions cluster into six domains:

*   **Verbal Semantic Memory (the defining function):** The left ATL is
    the **core substrate for verbal semantic memory** — the meanings of
    words, the concepts they denote, and the relationships among them
    [reference:11][reference:12]. **rTMS over the left ATL eliminates
    semantic priming for words**, while rTMS over the right ATL does
    not — direct causal evidence that **verbal semantics is
    implemented by the left ATL**[reference:13][reference:14].

*   **Supramodal Semantic Hub (Bilateral Contribution):** The ATL as a
    whole (left and right) is a **supramodal hub** — a convergence zone
    where **multimodal information** from vision, audition, and other
    modalities is integrated into **amodal conceptual representations**
    [reference:15][reference:16]. The left ATL is the **verbal pole** of this
    hub.

*   **Lexical-Semantic Processing (Left-Lateralized):** The left ATL
    supports **lexical-semantic processing** — the mapping of word forms
    to their meanings, and the retrieval of word meanings from semantic
    memory. This is the **left-lateralized** component of the ATL's
    semantic function.

*   **Verbal Label Feedback for Object Processing (Left-Lateralized):**
    The left ATL provides **verbal label feedback** that **guides the
    semantic analysis of visual objects**[reference:17]. This is a
    **twofold mechanism**: object semantics depend on right ATL
    computations **and** on automatic activation of verbal
    representations in the left ATL[reference:18].

*   **Person Knowledge and Social Semantics (Bilateral, with Right
    Emphasis):** The ATL supports **person knowledge** — knowledge about
    specific individuals, their identities, and their attributes. The
    **right ATL** is more strongly associated with **social concepts**
    and **social/emotional semantics**[reference:19], while the left ATL
    contributes to **verbal person knowledge**.

*   **Conceptual Knowledge and Categorization (Bilateral):** The ATL
    supports **conceptual knowledge** — the ability to categorize objects
    and ideas and to reason about their properties. This is a
    **bilateral** function of the ATL hub.

Associated Disorders
--------------------
Damage to or dysfunction of the left ATL is associated with:

*   **Semantic Dementia (Left-Lateralized — the signature left-ATL
    syndrome):** **Semantic dementia (SD)** is a progressive impairment
    of **semantic memory** characterized by **anomia, impaired word
    comprehension, and fluent but empty speech**[reference:20]. The
    **left ATL is the most severely affected region** in the classic
    left-predominant variant of SD, accounting for **about two-thirds of
    focal anterior temporal neurodegeneration cases**[reference:21].
    **Temporopolar and perirhinal cortices** show **>60% atrophy** in SD
    [reference:22].

*   **Anomic Aphasia and Word-Finding Difficulty (Left-Lateralized):**
    **Impaired naming** and **word retrieval** are core features of left
    ATL damage, consistent with the left ATL's role as the verbal
    semantic hub.

*   **Impaired Verbal Comprehension (Left-Lateralized):** **Difficulty
    understanding spoken and written words** follows left ATL damage,
    particularly in the semantic variant of primary progressive aphasia
    (svPPA)[reference:23].

*   **Surface Dyslexia and Dysgraphia (Left-Lateralized):** **Impaired
    reading and writing of irregular words** are associated with left
    ATL damage, consistent with the semantic contributions to reading
    and spelling[reference:24].

*   **Right Temporal Variant of Semantic Dementia (Right-Lateralized —
    contrast):** The **right temporal variant of SD (rSD)** is
    characterized by **right-predominant anterior temporal atrophy** and
    presents with **prosopagnosia, loss of emotional meaning, and
    behavioral changes** rather than verbal semantic deficits
    [reference:25].

**What is NOT here:** **Prosopagnosia**, **loss of emotional meaning**,
and **behavioral changes** are **right ATL** syndromes (right temporal
variant of SD). They are **absent** from left ATL lesions. They are
documented in the right ATL module and are **explicitly not claimed
here**.

Lateralization Notes
--------------------
This is the **left** ATL module. The lateralization landscape is
**left-verbal / right-non-verbal specialization** — a
**representational domain split**, not a sensorimotor or spatial split:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Verbal semantic memory** — word meanings and verbal concepts
      [reference:26][reference:27].
    - **Lexical-semantic processing** — mapping word forms to meanings.
    - **Verbal label feedback** for object processing[reference:28].
    - **Anomic aphasia** and **verbal comprehension deficits** following
      left ATL damage.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Non-verbal semantics** — object knowledge that is not
      verbally mediated[reference:29].
    - **Social/emotional semantics** — social concepts, person
      knowledge, and emotional associations[reference:30].
    - **Prosopagnosia** and **loss of emotional meaning** in the right
      temporal variant of SD[reference:31].

*   **Symmetric Functions (bilateral properties of the ATL hub):**
    - **Supramodal semantic integration** — the convergence of
      multimodal information into amodal concepts[reference:32].
    - **Conceptual knowledge and categorization**.
    - **Person knowledge** (with right emphasis on social semantics).
    - **Object semantics** (requiring both left verbal label feedback
      and right non-verbal computations)[reference:33].

**The "left-verbal / right-non-verbal" pattern is the defining
lateralization of the ATL pair.** Unlike the parallel-laden BA37
(words vs. faces) or the hemispheric-dominance BA22 (speech vs.
prosody), the ATL splits the **conceptual system** into **verbal
(left)** and **non-verbal/social (right)** components. This is a
**representational division of labor**, not a sensorimotor one.

**A consumer that assumes "left ATL = right ATL" will miss the
left-lateralized verbal semantic functions and the right-lateralized
social/emotional semantic functions.** The two hemispheres are **not
interchangeable** for semantic processing — they are **specialized for
different semantic domains**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe or the parietal lobe. Those are **sibling lobes**.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Multi-field functional region — flagged in prose and data.** The
    ATL is **not a single Brodmann area**. It encompasses **BA38** and
    the **anterior segments of BA20, BA21, and BA22**. The
    ``REGION_TO_BRODMANN`` constant below makes the multi-field mapping
    explicit.
*   **Partial-field mapping — flagged in data.** The ATL includes only
    the **anterior segment** of BA22, not the full BA22 (which is
    Wernicke's area). The ``PARTIAL_FIELDS`` constant below documents
    this.
*   **Left-verbal / right-non-verbal specialization — flagged in data.**
    The ``LEFT_LATERALIZED`` constant documents the left-lateralized
    verbal semantic functions.
*   **Four functional subregions — flagged in data.** The
    ``SUBREGIONS`` constant documents the superior dorsal, inferior
    dorsal, lateral, and ventromedial subregions.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex import anterior_temporal_lobe

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
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

For the left-lateralized functions::

    from ...temporal.cortex.anterior_temporal_lobe import LEFT_LATERALIZED
    # LEFT_LATERALIZED = ("verbal_semantic_memory",
    #                     "lexical_semantic_processing",
    #                     "verbal_label_feedback")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        atl_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.cortex.anterior_temporal_lobe"
        )
        # resolve atl_path through the memory/recall layer

References
----------
*   **Left-verbal / right-non-verbal specialization (rTMS evidence):**
    Uno, T., et al. (2026). "The Anterior Temporal Semantic Hub in the
    Left and Right Hemispheres: A Unitary System or Two Separate Systems
    for Meaning?" *J Neurosci*, 46(5), e1715252025.
    PMC12873641. **rTMS over left ATL eliminates semantic priming for
    words, but not right ATL**; both left and right ATL stimulation
    affect object priming[reference:34].
*   **Left ATL and verbal semantics:** *The functional architecture of
    the semantic hub: left and right anterior temporal lobes differently
    contribute to verbal and nonverbal processing* (2025),
    *ScienceDirect*. **Semantic priming in lexical decision was
    eliminated by left ATL stimulation but not right ATL stimulation**
    [reference:35].
*   **ATL functional subregions:** *Functional subdivisions in the
    anterior temporal lobes: a large scale meta-analytic investigation*
    (2020), *Neurosci Biobehav Rev*. **Four functional subregions**:
    superior dorsal, inferior dorsal, lateral, ventromedial[reference:36].
*   **ATL Brodmann constitution:** *Functional subdivisions* (2020).
    The ATL encompasses the **temporal pole (BA38)** and the **anterior
    segments of temporal gyri (BA20, 21, 22)**[reference:37]. MeSH —
    *Anterior Temporal Lobe* (2026) — BA38 is the temporal pole; BA20,
    BA21, BA22 are the anterior temporal gyri[reference:38].
*   **Semantic dementia and left ATL:** *Semantic Dementia — an
    overview* (ScienceDirect). **Classic SD is left-predominant**,
    accounting for **about two-thirds of cases**; left ATL is **most
    severely affected**[reference:39]. *The neural basis of semantic
    memory: Evidence from semantic dementia* (2008). **Temporopolar
    and perirhinal cortices show >60% atrophy** in SD[reference:40].
*   **Right temporal variant of SD:** *Semantic Dementia — an overview*.
    **Right-predominant atrophy** is associated with **prosopagnosia,
    loss of emotional meaning, and behavioral changes**[reference:41].
*   **ATL connectivity:** *Structural connectivity of the medial
    temporal lobe* (2025). The **anterior-temporal (AT) network** is
    supported by the **thalamic radiations and corpus callosum**
    [reference:42]. *Anatomy of the temporal stem* (2026). The **temporal
    stem** connects the **anterior temporal lobe, frontal lobe, and
    diencephalon**[reference:43]. The **uncinate fasciculus** and
    **inferior longitudinal fasciculus** connect the ATL to the frontal
    and posterior temporal regions[reference:44].
*   **ATL and semantic memory:** Patterson, K., Nestor, P.J., & Rogers,
    T.T. (2007). "Where do you know what you know? The representation of
    semantic knowledge in the human brain." *Nat Rev Neurosci*, 8(12),
    976–987. The ATL as the **supramodal semantic hub**.
*   **ATL and social semantics:** Zahn, R., et al. (2007). "Social
    concepts are represented in the superior anterior temporal cortex."
    *PNAS*, 104(15), 6430–6435. The **right anterior temporal cortex**
    represents **social concepts**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Anterior temporal and temporal pole anatomy.)
*   NeuroNames — Anterior temporal lobe (left); FMA — left anterior
    temporal lobe partonomy.
"""