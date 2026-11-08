"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.precuneus
===================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── precuneus                <-- THIS MODULE

**Primary synonym:** Precuneus (right); Praecuneus; Quadrate lobule of
Foville.
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the **medial surface** of the right hemisphere.
**Structural boundaries:** Marginal branch of the cingulate sulcus
(anteriorly), parieto-occipital sulcus (posteriorly), subparietal sulcus
(inferiorly).
**Lobe membership:** **Parietal** — the posteromedial gyrus of the right
parietal lobe, entirely on the medial surface.
**Functional contents:** **Medial extent of BA7** (and dorsal BA31);
default mode network (DMN) core node; episodic memory, self-referential
processing, and visuospatial imagery hub; **right-lateralized
spatial-attention / neglect contribution**.
**Cytoarchitectonic anchor:** **BA7** (medial continuation), with
subdivisions **7Am / 7Pm / 7m** and the precuneus visual area (PCV).

Overview
--------
The **right precuneus** is the posteromedial gyrus of the right parietal
lobe. It is a **hidden cortical element**, folded in the midsagittal
plane and buried in the depths of the longitudinal fissure, encased by
the sagittal sinus and bridging veins. Its concealment is why it
was historically "one of the less accurately mapped areas of the whole
cortical surface".

It is bounded by three sulci: the **marginal branch of the cingulate
sulcus** anteriorly, the **parieto-occipital sulcus** posteriorly, and
the **subparietal sulcus** inferiorly. It is anatomically co-extensive
with the **medial extent of Brodmann area 7 (BA7)**, and the modern
observer-independent partition subdivides it into **7Am (anteromedial)**,
**7Pm (posteromedial)**, and **7m (medial)** — with an additional
**precuneus visual area (PCV)** mapped in some atlases. Dorsal BA31 also
contributes to its territory.

**The precuneus is not a homogeneous structure.** Modern resting-state
connectivity confirms **three functionally dissociable subregions** —
dorsal-anterior, dorsal-posterior, and ventral — each with distinct
connectivity and cognitive roles. The **ventral precuneus** is the core
**default mode network (DMN)** node; the **dorsal-anterior** precuneus
is connected with sensorimotor and attention areas; the
**dorsal-posterior** precuneus is connected with visual imagery and
middle frontal regions.

**This is the right-hemisphere twin of the left precuneus, and its
lateralization profile differs in one crucial respect:** the **right**
precuneus is part of the **right-lateralized spatial-attention / neglect
network**, whereas the **left** precuneus is **not**. The DMN, memory,
imagery, and theory-of-mind functions are **largely symmetric** across
the two hemispheres; the **neglect and spatial-awareness** functions are
**right-lateralized** and are documented in full here (and **explicitly
denied** in the left module).

**Critical twin note:** The precuneus is one of the **most functionally
symmetric regions** in the parietal lobe for its core DMN/imagery/ToM
functions, **but not** for its spatial-attention contribution. The
**right precuneus** carries a **right-lateralized spatial-awareness
function** (neglect vulnerability, line-bisection contribution,
spatial-attention reorienting) that the left precuneus does **not**.
This is the **"weakly lateralized / structurally asymmetric + one
right-lateralized spatial function"** pattern.

Two-Partition Context
---------------------
This module is a **structural leaf** under the parietal lobe. Unlike the
postcentral gyrus, it does **not** contain a cross-listed Brodmann-area
child. Its cytoarchitectonic identity (**BA7 medial extent**) is
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
                                    ──▶  right-lateralized spatial awareness /
                                          neglect contribution

**Resolution contract for consumers:**

*   If you need **the precuneus as a structural entity**, use this module.
*   If you need **BA7 as a cytoarchitectonic field**, query
    ``brodmann_areas.brodmann_area_7``.
*   If you need **both**, use them together: this module for the medial
    surface location, DMN role, and **right-lateralized spatial-attention
    contribution**; the BA7 leaf for the lateral extent and the polymodal
    association functions.
*   **Do not** assume the precuneus is a Brodmann area. It is a **gyrus**
    whose territory is **co-extensive with the medial BA7**.

Connectivity
------------
The right precuneus is a **widespread connectivity hub**. Its major
connections include:

*   **Cingulum bundle** — connects the precuneus with the cingulate
    gyrus, parahippocampal cortices, and anterior thalamic nuclei (the
    posterior segment of the Papez circuit).
*   **Parahippocampal and hippocampal regions** — functional connectivity
    with the parahippocampal gyrus and hippocampus, supporting episodic
    memory.
*   **Thalamus** — functional connectivity with the medial thalamus,
    particularly in women.
*   **Posterior parietal cortex and occipital cortex** — dorsal precuneus
    shows greater connectivity with these regions than ventral precuneus
    .
*   **Medial superior frontal and orbitofrontal gyri, anterior cingulate,
    and parahippocampus** — stronger connectivity with the **ventral**
    precuneus.
*   **Somatomotor cortex, insula, supramarginal gyrus, and superior
    temporal gyrus** — stronger connectivity with the **dorsal-anterior**
    precuneus.
*   **Middle frontal gyrus** — stronger connectivity with the
    **dorsal-posterior** precuneus.
*   **Negative connectivity with the amygdala and lateral/inferior
    orbitofrontal gyri** — a distinctive feature of the precuneus as a
    whole.
*   **Right-lateralized dorsal-attention-network coupling** — the right
    precuneus is coupled with the right intraparietal sulcus and right
    temporoparietal junction as part of the **right ventral/dorsal
    attention networks**, contributing to the right-hemisphere dominance
    for spatial attention and neglect.

**The connectivity profile is the anatomical basis for the three
functional subregions AND for the right-lateralized spatial-attention
role.** The ventral precuneus is the DMN node; the dorsal-anterior is
sensorimotor/attentional; the dorsal-posterior is visual-imagery-related.
On the **right** side, the dorsal-anterior and dorsal-posterior
subregions additionally couple with the **right-lateralized attention
networks** — the anatomical substrate for the right-precuneus
contribution to spatial awareness and neglect.

Function in the Human Brain
---------------------------
The right precuneus is a **multidomain hub at the intersection of memory,
self, space, social cognition, and spatial attention**. Its
best-supported functions cluster into seven domains — six **symmetric**
with the left precuneus and **one right-lateralized**:

*   **Default Mode Network (DMN) Core Node:** The **ventral precuneus**
    is a core node of the DMN. The precuneus and surrounding
    posteromedial areas show the **highest resting metabolic rates** in
    the brain and are deactivated during non-self-referential
    goal-directed actions. **Symmetric function.**

*   **Episodic and Autobiographical Memory:** The precuneus is a hub
    within the DMN implicated in **episodic memory retrieval** and
    **metacognitive ability for memory retrieval**. It supports
    **vivid autobiographical reminiscence** through **subjective content
    representations**. **Symmetric function.**

*   **Self-Referential Processing and Self-Awareness:** The precuneus is
    involved in **self-referential processes** and **self-awareness**
    . A novel **"para-cingulate" network** — a subnetwork
    of the central executive network — supports self-referential processes
    and related psychiatric symptoms. **Symmetric function.**

*   **Visuospatial Imagery and Mental Rotation:** The precuneus is
    engaged in **visuospatial mental imagery**, **mental rotation**, and
    **action imagery**. A **medial network including the precuneus and
    hippocampus** is selectively recruited in **imagined viewer rotation**
    (perspective-taking). **Symmetric function.**

*   **Theory of Mind and Social Cognition:** The precuneus is part of the
    **mentalizing system** — with the temporoparietal junction and medial
    prefrontal cortex — activated when inferring the goals and intentions
    of others. **Verbal theory-of-mind reasoning** is
    supported by the cortical surface area and thickness of the precuneus
    and temporoparietal junction. **Symmetric function.**

*   **Visuospatial Integration and Sensorimotor Guidance:** The
    **dorsal-anterior** precuneus is connected with **somatomotor cortex,
    insula, and supramarginal gyrus**, and it participates in
    **spatially guided behaviors** and **motor execution/attention**.
    **Symmetric function.**

*   **Right-Lateralized Spatial Awareness / Neglect Contribution
    (unique to this twin):** The **right precuneus** is part of the
    **right-lateralized spatial-attention network** and is one of the
    regions whose hypoperfusion or lesion is associated with
    **hemispatial neglect**. Severe hypoperfusion in the
    right parieto-temporo-occipital cortex, **including the precuneus**,
    is associated with neglect. The right precuneus
    contributes to **symmetrical processing of the visual scene** and
    **line bisection** — the classical neglect-relevant functions of the
    right parietal lobe. It has also been associated with
    **freezing of gait** in Parkinson's disease in some studies,
    consistent with its role in **visuospatial integration for
    movement**.

Associated Disorders
--------------------
Damage to or dysfunction of the **right** precuneus is associated with:

*   **Hemispatial Neglect (Right-Lateralized — the principal
    right-precuneus syndrome):** Severe hypoperfusion in the right
    parieto-temporo-occipital cortex, **including the precuneus**, is
    associated with left hemispatial neglect. The right
    precuneus contributes to the **right-lateralized spatial-attention
    network** whose disruption produces neglect. **Left
    precuneus lesions do not produce neglect** (see left precuneus
    module).

*   **Alzheimer's Disease (Hypometabolism and Atrophy):** The precuneus
    is affected by atrophy and hypometabolism in the early stages of
    Alzheimer's disease (AD). Meta-analyses confirm
    **significant hypoperfusion in the precuneus** of AD patients,
    consistent with hypometabolic patterns. The precuneus
    shows disrupted functional connectivity and decreased glucose
    metabolism in AD, and it is one of the regions whose hypometabolism
    most reliably predicts progression from amnestic mild cognitive
    impairment to AD. This is a **bilateral** finding, not
    right-lateralized.

*   **Bálint Syndrome (Bilateral Lesions):** **Bilateral** lesions of
    the parieto-occipital junction, often including the precuneus,
    produce **Bálint syndrome** — the triad of **simultanagnosia**,
    **optic ataxia**, and **ocular apraxia**.
    The **right** precuneus contributes to the neglect-adjacent
    components of the syndrome.

*   **Freezing of Gait in Parkinson's Disease (Right-Lateralized
    Association):** The **right** precuneus has been
    associated with **freezing of gait** in Parkinson's disease,
    consistent with its role in visuospatial integration for movement.

*   **Psychiatric and Neurodegenerative Conditions:** The precuneus has
    been implicated in depression, social anxiety disorder, and other
    psychiatric conditions through its DMN connectivity.
    Disrupted precuneus connectivity is a convergent finding across
    schizophrenia and depression. These are largely **bilateral**
    findings.

**What is NOT here:** The **left-lateralized language syndromes** of
BA39/BA40 (Gerstmann, alexia, conduction aphasia) are **not** precuneus
syndromes and are absent from both precuneus modules. **Bilateral
astereognosis** and **stereognosis dominance** belong to the left S1
modules, not the precuneus. The right precuneus is a **medial
DMN/spatial-attention hub**, not an inferior parietal language/praxis
hub.

Lateralization Notes
--------------------
This is the **right** precuneus module. The lateralization landscape is
**weakly asymmetric at the structural level**, **largely symmetric at
the functional level**, and **right-lateralized for spatial awareness /
neglect** — a mixed pattern that is qualitatively different from every
other module in the parietal subtree:

*   **Right-Lateralized Function (unique to this twin):**
    - **Spatial-awareness dominance / neglect contribution** — the right
      precuneus is part of the right-lateralized spatial-attention
      network, and its hypoperfusion/lesion is associated with
      **left hemispatial neglect**. It also contributes to
      **line bisection** and **symmetrical processing of the visual
      scene**.
    - **Freezing of gait** in Parkinson's disease has been associated
      with the right precuneus.

*   **No Left-Lateralized Function Denied.** Unlike the S1/BA1/BA2/BA3
    pairs (left-loaded), the precuneus pair carries **no left-lateralized
    syndrome** that needs to be denied on the right. The DMN, memory,
    imagery, and theory-of-mind functions are **symmetric**, and the
    spatial-attention function is **right-lateralized**. The precuneus
    pair is therefore **not a mirror of a left-loaded module** — it is a
    **weakly-lateralized module with one right-lateralized
    spatial-attention addition**.

*   **Structural Asymmetry (right > left in size, left > right in
    thickness):** Morphometric studies report that the **right precuneus
    is thinner and larger than the left**, with marked individual
    variation and fluctuating asymmetries. Average
    total surface area is ≈16.07 cm² on the right and ≈15.44 cm² on the
    left. The **subparietal sulcus is generally wider on the right
    hemisphere**.

*   **Symmetric Functions (bilateral properties of the precuneus, copied
    verbatim from the left twin):**
    - DMN core node (ventral precuneus).
    - Episodic and autobiographical memory.
    - Self-referential processing and self-awareness.
    - Visuospatial imagery and mental rotation (viewer rotation).
    - Theory of mind and social cognition.
    - Visuospatial integration and sensorimotor guidance (dorsal-anterior
      precuneus).
    - Connectivity with cingulum, parahippocampus, and thalamus.
    - Alzheimer's disease hypometabolism / atrophy.

**A consumer that assumes "right precuneus = left precuneus" will miss
the right-lateralized spatial-awareness / neglect contribution** — the
single function that distinguishes the two twins. A consumer that
assumes "right precuneus is left-loaded like S1" will be **wrong** —
there are no left-lateralized syndromes to deny here. The precuneus pair
is the **"weakly lateralized / structurally asymmetric + one
right-lateralized spatial function"** pattern.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../occipital/cuneus`` or ``.../cingulate``. The cuneus is a
    separate structural entity in the occipital lobe; the cingulate is a
    separate lobar system.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural leaf with a shared cytoarchitectonic identity (BA7).**
    The precuneus is co-extensive with the medial BA7, but it does
    **not** contain a cross-listed Brodmann child (unlike the postcentral
    gyrus and BA3). Consumers that need BA7 should query
    ``brodmann_areas.brodmann_area_7``.
*   **Three functional subregions within one gyrus.** The ventral
    precuneus (DMN), dorsal-anterior (sensorimotor/attention), and
    dorsal-posterior (visual imagery) are functionally dissociable but
    structurally unified. On the **right** side, the dorsal subregions
    additionally couple with the **right-lateralized attention
    networks**. Consumers that need subregion-level resolution should use
    the ``SUBREGIONS`` constant below.
*   **Structural parity with left precuneus.** Left and right precuneus
    modules must be structurally interchangeable so bilateral consumers
    can iterate hemispheres generically. The functional contents are
    **largely symmetric**; the **right** twin **adds** the
    right-lateralized spatial-awareness / neglect contribution, and the
    structural-asymmetry prose is inverted (right > left in size; left >
    right in thickness).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal import precuneus

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
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
    S0940960216300905.
*   **BA7 medial extent:** *Chapter 3.7 The role of the precuneus in
    episodic memory* (2008), *ScienceDirect*.
*   **Three subregions:** *Functional connectivity mapping of the human
    precuneus by resting state fMRI* (2011), *NeuroImage*,
    S1053811911013048.
*   **DMN core node and metabolic hot spot:** *The precuneus: a review of
    its functional anatomy and behavioural correlates* (2006), *Brain*,
    PMID 37254.
*   **Functional role and para-cingulate network:** Dadario, N.B., et al.
    (2023). *Brain*, 146(9), 3598–3607, PMID 37254740.
*   **Episodic memory and metacognition:** *The experience of vivid
    autobiographical reminiscence is supported by subjective content
    representations in the precuneus* (2018), *Sci Rep*.
*   **Visuospatial imagery and mental rotation:** *Nayouki Sato — Brain
    mechanisms for the generation and transformations of visuospatial
    mental imagery*; *Differential effect of double-pulse TMS applied to
    dorsal premotor cortex and precuneus during internal operation of
    visuospatial information* (2009), *ScienceDirect*.
*   **Theory of mind:** *Two systems for thinking about others' thoughts
    in the developing brain* (2020), *PNAS*, 117(12), 6928–6935, PMID
    32152117; *The intentional network: How the brain reads varieties of
    intentions* (2007), *ScienceDirect*.
*   **Connectivity:** *Supplementary Material: Hubs and Interaction: The
    Brain's Meta-loop* (PMC); *Functional connectivity mapping* (2011).
*   **Right precuneus and neglect:** *is clinically characterized by
    variable degrees of Balint and Gerstmann syndromes...* (2025),
    *Alzheimers Dement*. Severe hypoperfusion in the right
    parieto-temporo-occipital cortex in the subgroup with neglect.
    *The anatomy of a disorder: a model of hemispatial
    neglect* (PMC, 2011). Right precuneus is part of the network whose
    damage produces neglect.
*   **Right precuneus and freezing of gait:** *Freezing of gait in
    Parkinson's disease is associated with altered precuneus connectivity*
    and related studies. The right precuneus contributes to visuospatial
    integration for movement.
*   **Structural asymmetry:** *Cortical surface area and cortical
    thickness in the precuneus of adult humans* (2015), *Neuroscience*,
    286, 345–352. The right precuneus is thinner and larger than the left,
    with marked individual variation.
*   **Alzheimer's disease:** *Cerebral blood flow alterations in the
    precuneus of Alzheimer's disease using arterial spin labeling: A
    systematic review and meta-analysis* (2025), *ScienceDirect*;
    *Morphological variations and cortical atrophy of the precuneus in
    normal aging and Alzheimer's disease* (2025), *J Anat*, PMID 40874415;
    *Neural correlates of Alzheimer's disease and mild cognitive
    impairment* (2009), *ScienceDirect*.
*   **Bálint syndrome:** *Neurobiology of the Balint-Holmes syndrome*
    (2017), *Actas Esp Psiquiatr*; *Anatomical Presentation Of The
    Superior Parietal Lobule* (2026), *SciePro*.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed.
*   Terminologia Anatomica (FIPAT, 2019) — precuneus.
*   NeuroNames — Precuneus (right); FMA — right precuneus.
"""