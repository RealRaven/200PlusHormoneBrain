"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.precuneus
==================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── precuneus                <-- THIS MODULE

**Primary synonym:** Precuneus (left); Praecuneus; Quadrate lobule of
Foville.
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the **medial surface** of the hemisphere.
**Structural boundaries:** Marginal branch of the cingulate sulcus
(anteriorly), parieto-occipital sulcus (posteriorly), subparietal sulcus
(inferiorly).
**Lobe membership:** **Parietal** — the posteromedial gyrus of the
parietal lobe, entirely on the medial surface.
**Functional contents:** **Medial extent of BA7** (and dorsal BA31);
default mode network (DMN) core node; episodic memory, self-referential
processing, and visuospatial imagery hub.
**Cytoarchitectonic anchor:** **BA7** (medial continuation), with
subdivisions **7Am / 7Pm / 7m** and the precuneus visual area (PCV).

Overview
--------
The **left precuneus** is the posteromedial gyrus of the left parietal
lobe. It is a **hidden cortical element**, folded in the midsagittal
plane and buried in the depths of the longitudinal fissure, encased by
the sagittal sinus and bridging veins[reference:0][reference:1]. Its
concealment is why it was historically "one of the less accurately mapped
areas of the whole cortical surface"[reference:2].

It is bounded by three sulci: the **marginal branch of the cingulate
sulcus** anteriorly, the **parieto-occipital sulcus** posteriorly, and
the **subparietal sulcus** inferiorly[reference:3][reference:4]. It is
**anatomically co-extensive with the medial extent of Brodmann area 7
(BA7)**[reference:5][reference:6], and the modern observer-independent
partition subdivides it into **7Am (anteromedial)**, **7Pm
(posteromedial)**, and **7m (medial)** — with an additional **precuneus
visual area (PCV)** mapped in some atlases[reference:7]. Dorsal BA31 also
contributes to its territory[reference:8].

**The precuneus is not a homogeneous structure.** Although Brodmann
(1909) treated it as a single field, modern resting-state connectivity
has confirmed **three functionally dissociable subregions** — dorsal-
anterior, dorsal-posterior, and ventral — each with distinct connectivity
and cognitive roles[reference:9][reference:10]. The **ventral precuneus**
is the core **default mode network (DMN)** node; the **dorsal-anterior**
precuneus is connected with sensorimotor and attention areas; the
**dorsal-posterior** precuneus is connected with visual imagery and
middle frontal regions[reference:11].

**This is the DMN hub of the parietal lobe.** The precuneus and
surrounding posteromedial areas display some of the **highest resting
metabolic rates** in the brain and are characterized by **transient
decreases in tonic activity during engagement in non-self-referential
goal-directed actions** — the default mode of brain function[reference:12].
It is a core node of the DMN alongside the posterior cingulate cortex and
medial prefrontal cortex, and it is one of the **first regions affected
by hypometabolism and atrophy in Alzheimer's disease**[reference:13].

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. Unlike
the postcentral gyrus, it does **not** contain a cross-listed Brodmann-
area child. Its cytoarchitectonic identity (**BA7 medial extent**) is
documented in the sibling Brodmann leaf at
``.../parietal/brodmann_areas/brodmann_area_7``:

::

    Structural leaf (this module)        Functional / cytoarchitectonic contents
    ─────────────────────────────        ────────────────────────────────────────
    precuneus                       ──▶  medial BA7 (7Am, 7Pm, 7m; PCV)
                                    ──▶  dorsal BA31 (partial)
                                    ──▶  ventral precuneus → DMN core node
                                    ──▶  dorsal-anterior → sensorimotor/attention
                                    ──▶  dorsal-posterior → visual imagery

**The precuneus is the structural anchor for the medial DMN aspect of
the parietal lobe.** Its cytoarchitectonic content (BA7) is shared with
the **lateral superior parietal lobule**, but the precuneus is a
**distinct structural entity** on the medial surface. Consumers that need
the cytoarchitectonic detail of BA7 should query the BA7 leaf; this
module documents **where the medial BA7 territory sits on the cortical
surface** and **what network it belongs to**.

**Resolution contract for consumers:**

*   If you need **the precuneus as a structural entity**, use this
    module.
*   If you need **BA7 as a cytoarchitectonic field**, query
    ``brodmann_areas.brodmann_area_7``.
*   If you need **both**, use them together: this module for the medial
    surface location and DMN role, the BA7 leaf for the lateral extent
    and the polymodal association functions.
*   **Do not** assume the precuneus is a Brodmann area. It is a **gyrus**
    whose territory is **co-extensive with the medial BA7**.

Connectivity
------------
The precuneus is a **widespread connectivity hub**[reference:14]. Its
major connections include:

*   **Cingulum bundle** — connects the precuneus with the cingulate
    gyrus, parahippocampal cortices, and anterior thalamic nuclei (the
    posterior segment of the Papez circuit)[reference:15].
*   **Parahippocampal and hippocampal regions** — functional connectivity
    with the parahippocampal gyrus and hippocampus, supporting episodic
    memory[reference:16].
*   **Thalamus** — functional connectivity with the medial thalamus,
    particularly in women[reference:17].
*   **Posterior parietal cortex and occipital cortex** — dorsal precuneus
    shows greater connectivity with these regions than ventral precuneus
    [reference:18].
*   **Medial superior frontal and orbitofrontal gyri, anterior cingulate,
    and parahippocampus** — stronger connectivity with the **ventral**
    precuneus[reference:19].
*   **Somatomotor cortex, insula, supramarginal gyrus, and superior
    temporal gyrus** — stronger connectivity with the **dorsal-anterior**
    precuneus[reference:20].
*   **Middle frontal gyrus** — stronger connectivity with the
    **dorsal-posterior** precuneus[reference:21].
*   **Negative connectivity with the amygdala and lateral/inferior
    orbitofrontal gyri** — a distinctive feature of the precuneus as a
    whole[reference:22].

**The connectivity profile is the anatomical basis for the three
functional subregions.** The ventral precuneus is the DMN node; the
dorsal-anterior is sensorimotor/attentional; the dorsal-posterior is
visual-imagery-related. This is why the precuneus is best described as a
**set of functionally dissociable subregions within a single structural
gyrus**, not as a monolithic area.

Function in the Human Brain
---------------------------
The left precuneus is a **multidomain hub at the intersection of memory,
self, space, and social cognition**. Its best-supported functions cluster
into six domains:

*   **Default Mode Network (DMN) Core Node:** The **ventral precuneus**
    is a core node of the DMN, alongside the posterior cingulate cortex
    and medial prefrontal cortex[reference:23]. The precuneus and
    surrounding posteromedial areas show the **highest resting metabolic
    rates** in the brain and are **deactivated during non-self-referential
    goal-directed actions**[reference:24]. The DMN is **task-negative** —
    it turns off during attention-demanding tasks and is associated with
    self-referential and social processes[reference:25].

*   **Episodic and Autobiographical Memory:** The precuneus is a hub
    within the DMN implicated in **episodic memory retrieval** and
    **metacognitive ability for memory retrieval**. It
    supports **vivid autobiographical reminiscence** through **subjective
    content representations**[reference:27], and it is engaged in
    **episodic memory** alongside self-related processing[reference:28].

*   **Self-Referential Processing and Self-Awareness:** The precuneus is
    involved in **self-referential processes** and **self-awareness**
    [reference:29][reference:30]. A novel **"para-cingulate" network** — a
    subnetwork of the central executive network — has been proposed to
    support self-referential processes and related psychiatric symptoms
    [reference:31]. The precuneus is also implicated in **aspects of
    consciousness**[reference:33].

*   **Visuospatial Imagery and Mental Rotation:** The precuneus is
    engaged in **visuospatial mental imagery**, **mental rotation**, and
    **action imagery**[reference:34]. The **dorsal-posterior** precuneus
    is connected with visual imagery areas[reference:35]. A **medial
    network including the precuneus and hippocampus** is selectively
    recruited in **imagined viewer rotation** (perspective-taking),
    distinct from the parietal-frontal network for imagined object
    rotation[reference:36].

*   **Theory of Mind and Social Cognition:** The precuneus is part of the
    **mentalizing system** — with the temporoparietal junction and medial
    prefrontal cortex — activated when inferring the goals and intentions
    of others[reference:37]. **Verbal theory-of-mind reasoning** is
    supported by the cortical surface area and thickness of the precuneus
    and temporoparietal junction[reference:38]. The precuneus is
    necessary for processing **all types of prior intentions**[reference:39].

*   **Visuospatial Integration and Sensorimotor Guidance:** The
    **dorsal-anterior** precuneus is connected with **somatomotor cortex,
    insula, and supramarginal gyrus**, and it participates in **spatially
    guided behaviors** and **motor execution/attention**[reference:40].
    The precuneus is involved in **visuospatial integration, imagery and
    simulation**[reference:41], and it is part of the network that
    **maintains and updates visuospatial information in working memory**
    [reference:42].

Associated Disorders
--------------------
Damage to or dysfunction of the left precuneus is associated with:

*   **Alzheimer's Disease (Hypometabolism and Atrophy):** The precuneus
    is **affected by atrophy and hypometabolism in the early stages of
    Alzheimer's disease (AD)**[reference:43]. Meta-analyses confirm
    **significant hypoperfusion in the precuneus** of AD patients,
    consistent with hypometabolic patterns[reference:44]. The precuneus
    shows **disrupted functional connectivity** and **decreased glucose
    metabolism** in AD[reference:45], and it is one of the regions whose
    hypometabolism most reliably predicts progression from amnestic mild
    cognitive impairment to AD[reference:46].

*   **Bálint Syndrome (Bilateral Lesions):** **Bilateral** lesions of
    the parieto-occipital junction, often including the precuneus,
    produce **Bálint syndrome** — the triad of **simultanagnosia**,
    **optic ataxia**, and **ocular apraxia**[reference:47][reference:48].
    The precuneus is part of the dorsal parietal cortex whose bilateral
    involvement classically contributes to the syndrome[reference:49].

*   **Hemispatial Neglect (Right-Sided Lesions):** The **right** precuneus
    is part of the right-lateralized spatial-attention network. Severe
    hypoperfusion in the right parieto-temporo-occipital cortex, including
    the precuneus, is associated with **neglect**[reference:50]. The **left**
    precuneus is **not** a primary neglect node.

*   **Psychiatric and Neurodegenerative Conditions:** The precuneus has
    been implicated in **depression**, **social anxiety disorder**, and
    other psychiatric conditions through its DMN connectivity[reference:51]
    [reference:52]. Disrupted precuneus connectivity is a convergent finding
    across schizophrenia and depression[reference:53].

**What is NOT here:** **Gerstmann syndrome**, **alexia**, **conduction
aphasia**, and the **left-lateralized language syndromes** of BA39/BA40
are **not** precuneus syndromes. The precuneus is a medial DMN/imagery
hub, not an inferior parietal language/praxis hub. **Hemispatial neglect**
and **spatial-awareness dominance** are **right**-lateralized and belong
to the right precuneus and right PPC modules, not to this left module.

Lateralization Notes
--------------------
This is the **left** precuneus module. The lateralization landscape is
**weakly asymmetric at the structural level** and **largely symmetric at
the functional level** — a pattern distinct from the strongly lateralized
BA39/BA40/PPC modules:

*   **Structural Asymmetry (right > left in size, left > right in
    thickness):** Morphometric studies report that the **right precuneus
    is thinner and larger than the left**, with **marked individual
    variation** and **fluctuating asymmetries**.
    Average total surface area is ≈16.07 cm² on the right and ≈15.44 cm²
    on the left[reference:56]. The **subparietal sulcus is generally wider
    on the right hemisphere**[reference:57]. These structural asymmetries
    are **not** accompanied by strong functional lateralization.

*   **Functional Symmetry (largely bilateral):** The precuneus is a
    **bilateral DMN hub**, and its core functions — episodic memory,
    self-referential processing, visuospatial imagery, theory of mind —
    are supported by **both hemispheres**. The **left precuneus** is
    specifically noted as a **key node of the DMN**[reference:58], and it
    is a hub for **metacognitive ability for memory retrieval**.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Hemispatial neglect** and **spatial-awareness dominance** are
      **right**-precuneus/right-PPC functions[reference:60]. The left
      precuneus is **not** a neglect node.
    - **Visual driving input** and **freezing of gait** in Parkinson's
      disease have been associated with the **right** precuneus in some
      studies.

*   **Symmetric Functions (bilateral properties of the precuneus, copied
    verbatim to the right twin):**
    - DMN core node (ventral precuneus).
    - Episodic and autobiographical memory.
    - Self-referential processing and self-awareness.
    - Visuospatial imagery and mental rotation (viewer rotation).
    - Theory of mind and social cognition.
    - Visuospatial integration and sensorimotor guidance (dorsal-anterior
      precuneus).
    - Connectivity with cingulum, parahippocampus, and thalamus.

**A consumer that assumes "left precuneus = right precuneus" will be
approximately correct at the functional level** — the precuneus is one of
the most functionally symmetric regions in the parietal lobe. The
asymmetry is **structural** (right larger and thinner; left thicker),
**not syndromic**. This is the **"weakly lateralized / structurally
asymmetric"** pattern — the lightest lateralization load of any module in
the parietal subtree.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../occipital/cuneus`` or ``.../cingulate``. The cuneus is a
    separate structural entity in the occipital lobe; the cingulate is a
    separate lobar system.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural leaf with a shared cytoarchitectonic identity (BA7).**
    The precuneus is **co-extensive with the medial BA7**, but it does
    **not** contain a cross-listed Brodmann child (unlike the postcentral
    gyrus and BA3). Consumers that need BA7 should query
    ``brodmann_areas.brodmann_area_7``; this module documents the
    **structural and network** identity of the medial surface gyrus.
*   **Three functional subregions within one gyrus.** The ventral
    precuneus (DMN), dorsal-anterior (sensorimotor/attention), and
    dorsal-posterior (visual imagery) are **functionally dissociable**
    but **structurally unified**. Consumers that need subregion-level
    resolution should use the ``SUBREGIONS`` constant below, not a
    filesystem walk.
*   **Structural parity with right precuneus.** Left and right precuneus
    modules must be structurally interchangeable so bilateral consumers
    can iterate hemispheres generically. The functional contents are
    **largely symmetric**; only the structural-asymmetry prose (right >
    left in size; left > right in thickness) and the neglect contrast
    differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal import precuneus

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.precuneus"
    )

For the cytoarchitectonic detail (BA7 medial extent)::

    from ...parietal.brodmann_areas import brodmann_area_7
    # BA7 is the cytoarchitectonic anchor; precuneus is the structural gyrus

For the three functional subregions::

    from ...parietal.precuneus import SUBREGIONS
    # SUBREGIONS["ventral"], ["dorsal_anterior"], ["dorsal_posterior"]

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pcu_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.precuneus"
        )
        # resolve pcu_path through the memory/recall layer

References
----------
*   **Anatomy and sulcal boundaries:** *Sulcal pattern, extension, and
    morphology of the precuneus in adult humans* (2016), *Ann Anat*,
    S0940960216300905. The precuneus is a medial parietal cortical
    element folded in the midsagittal plane; bounded by the ramus
    marginalis of the cingulate sulcus, parieto-occipital sulcus, and
    subparietal sulcus; corresponds to BA7[reference:62].
*   **BA7 medial extent:** *Chapter 3.7 The role of the precuneus in
    episodic memory* (2008), *ScienceDirect*. "The precuneus, that is,
    the mesial extent of Brodmann's area (BA) 7"[reference:63]. Brodmann
    mapped it as the medial continuation of lateral parietal area 7
    .
*   **Three subregions:** *Functional connectivity mapping of the human
    precuneus by resting state fMRI* (2011), *NeuroImage*,
    S1053811911013048. Dorsal-anterior, dorsal-posterior, and ventral
    subregions; ventral precuneus is part of the DMN; dorsal-anterior
    connected with somatomotor/attention; dorsal-posterior connected with
    visual imagery[reference:65].
*   **DMN core node and metabolic hot spot:** *The precuneus: a review of
    its functional anatomy and behavioural correlates* (2006), *Brain*,
    PMID 37254. Precuneus and posteromedial areas show the highest
    resting metabolic rates and are deactivated during non-self-
    referential goal-directed actions[reference:66].
*   **Functional role and para-cingulate network:** Dadario, N.B., et al.
    (2023). *Brain*, 146(9), 3598–3607, PMID 37254740. Dual DMN systems
    support episodic memory and theory of mind; a novel "para-cingulate"
    network supports self-referential processes[reference:67].
*   **Episodic memory and metacognition:** *The experience of vivid
    autobiographical reminiscence is supported by subjective content
    representations in the precuneus* (2018), *Sci Rep*. The precuneus is
    a hub within the DMN implicated in metacognitive ability for memory
    retrieval[reference:69].
*   **Visuospatial imagery and mental rotation:** *Nayouki Sato — Brain
    mechanisms for the generation and transformations of visuospatial
    mental imagery*. A medial network including precuneus and hippocampus
    is recruited in imagined viewer rotation[reference:70]. *Differential
    effect of double-pulse TMS applied to dorsal premotor cortex and
    precuneus during internal operation of visuospatial information*
    (2009), *ScienceDirect*. Precuneus activated during visuospatial
    mental operation[reference:71].
*   **Theory of mind:** *Two systems for thinking about others' thoughts
    in the developing brain* (2020), *PNAS*, 117(12), 6928–6935, PMID
    32152117. Verbal ToM reasoning supported by cortical surface area and
    thickness of the precuneus and TPJ[reference:72]. *The intentional
    network: How the brain reads varieties of intentions* (2007),
    *ScienceDirect*. Precuneus is necessary for processing all types of
    prior intentions[reference:73].
*   **Connectivity:** *Supplementary Material: Hubs and Interaction: The
    Brain's Meta-loop* (PMC). Cingulum loop terminals span the precuneus
    (BA7, 31) and parahippocampal area[reference:74]. *Functional
    connectivity mapping* (2011). Precuneus has negative connectivity
    with the amygdala and lateral/inferior orbitofrontal gyri[reference:75].
*   **Structural asymmetry:** *Cortical surface area and cortical
    thickness in the precuneus of adult humans* (2015), *Neuroscience*,
    286, 345–352. The right precuneus is thinner and larger than the left,
    with marked individual variation and fluctuating asymmetries
    . *Morphometric variability of precuneus*
    (2015), *Scindeks*. Right ≈16.07 cm²; left ≈15.44 cm²[reference:78].
*   **Alzheimer's disease:** *Cerebral blood flow alterations in the
    precuneus of Alzheimer's disease using arterial spin labeling: A
    systematic review and meta-analysis* (2025), *ScienceDirect*.
    Significant hypoperfusion in the precuneus of AD patients
    [reference:79]. *Morphological variations and cortical atrophy of the
    precuneus in normal aging and Alzheimer's disease* (2025), *J Anat*,
    PMID 40874415. Precuneus affected by atrophy and hypometabolism in
    early AD[reference:80]. *Neural correlates of Alzheimer's disease and
    mild cognitive impairment* (2009), *ScienceDirect*. Precuneus
    hypometabolism predicts progression from aMCI to AD[reference:81].
*   **Bálint syndrome:** *Neurobiology of the Balint-Holmes syndrome*
    (2017), *Actas Esp Psiquiatr*. Bálint-Holmes syndrome after bilateral
    lesions of the parieto-occipital junction, often including the
    precuneus[reference:82]. *Anatomical Presentation Of The Superior
    Parietal Lobule* (2026), *SciePro*. Bilateral involvement of dorsal
    parietal cortex contributes to Bálint syndrome[reference:83].
*   **Neglect (right-sided):** *is clinically characterized by variable
    degrees of Balint and Gerstmann syndromes...* (2025), *Alzheimers
    Dement*. Severe hypoperfusion in the right parieto-temporo-occipital
    cortex in the subgroup with neglect[reference:84].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial-surface gyral anatomy.)
*   Terminologia Anatomica (FIPAT, 2019) — precuneus.
*   NeuroNames — Precuneus (left); FMA — left precuneus.
"""