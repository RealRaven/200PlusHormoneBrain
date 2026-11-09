"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.brodmann_areas.brodmann_area_34
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
                        └── brodmann_area_34   <-- THIS MODULE

**Primary synonym:** Brodmann Area 34 (BA34); **Dorsal entorhinal cortex**;
**Anterior entorhinal cortex**; Area entorhinalis dorsalis; Cortex
entorhinalis dorsalis.
**Cytoarchitectonic designation:** Area 34 of Brodmann (1909).
**Part of:** The **entorhinal complex** — together with BA28 (the
ventral/posterior entorhinal cortex). The entorhinal cortex (ERC) in humans
consists of **Brodmann areas 28 and 34** and is situated bilaterally between
the **sulcus semiannularis** and the **sulcus rhinalis** in the rostral
parahippocampal gyrus.
**Location:** The **anterior and dorsal portion of the entorhinal cortex**
along the **parahippocampal gyrus** and **gyrus ambiens** of the right
temporal lobe.
**Structural parent:** This is a **Brodmann leaf**, not a gyral child. It
lives directly under the right temporal Brodmann aggregator.
**Cytoarchitectonic type:** **Periallocortical / allocortical** — BA34 is
**not neocortical**. It is a transitional cortex between the hippocampus
(archicortex) and the neocortical parahippocampal gyrus.

Overview
--------
Brodmann Area 34 (BA34) is the **dorsal (anterior) subdivision of the
entorhinal cortex** — the **major gateway between the hippocampal formation
and the neocortex**. Together with BA28, it forms the **entorhinal complex**,
the nodal point of the cortico-hippocampal circuit that supports
**declarative memory, spatial navigation, and the perception of time**.

**This is the right-hemisphere twin of the left BA34, and the pair is
SYMMETRIC-BY-BILATERAL-ORGANIZATION with a right-lateralized spatial and
olfactory weighting.** Unlike BA20 (asymmetric-by-function), BA21
(left-loaded with right complement), and BA22 (hemispheric dominance by
function), BA34 is **bilaterally organized as part of the entorhinal-
hippocampal system**. The **core gateway and memory functions are
bilaterally represented**, and the only lateralized functions are:

1.  **Spatial memory encoding — biased to the right hemisphere** in both
    the entorhinal and perirhinal cortices, whereas object encoding is
    biased to the left.

2.  **Olfactory processing — the right hemisphere is more activated than
    the left** during olfactory tasks, including in the entorhinal cortex
    (BA34)[reference:1].

3.  **Anosmia — the right BA34 is relatively spared** in some clinical
    populations with anosmia (e.g., Parkinson's disease), whereas the left
    BA34 shows significantly higher Z-scores.

**BA34 is the third allocortical leaf documented in this tree**, following
BA27 (presubiculum) and BA28 (entorhinal cortex). The temporal Brodmann
aggregator flagged BA27, BA28, BA34, and BA35 as **allocortical or
transitional fields** (via the `CYTOARCHITECTONIC_TYPE` constant) — and this
module continues that series. Consumers that assume all Brodmann areas are
neocortical will be **wrong for BA34**: it has **fewer layers**, a
distinctive **lamina dissecans** (a cell-sparse layer IV), and **cell-dense
islands in layer II**.

**BA34 is the dorsal/anterior entorhinal cortex, and it is cytoarchitectonically
distinct from BA28.** BA28 is the **ventral/posterior** entorhinal cortex
(the classical "area entorhinalis"), while BA34 is the **dorsal/anterior**
entorhinal cortex (the "area entorhinalis dorsalis"). The two together
constitute the human entorhinal cortex, but they have **different
cytoarchitectonic signatures and different connectivity profiles**.
Consumers that need the full entorhinal cortex must query **both BA28 and
BA34**.

Periallocortical Cytoarchitecture
--------------------------------
BA34 is **periallocortical / allocortical** — a transitional cortex between
the archicortex of the hippocampus and the neocortex of the parahippocampal
gyrus. Its cytoarchitectonic features are **identical to the left twin**:

*   **Agranular six-layered structure** — BA34 is characterized by an
    **agranular six-layered structure**, including **distinctive cell-dense
    islands in layer II** and a **cell-sparse lamina dissecans as layer IV**,
    distinguishing it from adjacent areas like the perirhinal cortex (BA35).

*   **Paucity of cells in layer IV (lamina dissecans)** — the entorhinal
    cortex (including BA34) has a **striking paucity of cells in layer IV
    (lamina dissecans)**, which separates the **outer cell-rich layers (V
    and VI)** from the **inner cell-rich layers (II and III)**. This is a
    **hallmark of entorhinal cortex** and is absent from neocortex.

*   **Layer III pyramidal projection neurons** — **layer III** consists of
    **pyramidal projection neurons** that target the **hippocampus and other
    regions**. This is the principal output layer of the entorhinal cortex
    to the hippocampus.

*   **Neurochemical signature** — BA34 shows **moderate parvalbumin
    immunoreactivity in layer IIIb** and **lighter calbindin labeling**
    compared to neighboring perirhinal regions, aiding precise delineation
    in histological and neuroimaging studies.

**This periallocortical identity is the defining structural fact about
BA34.** It is **not** a neocortical association area; it is a
**hippocampal-formation gateway** with a different computational
architecture from BA20/21/22/37/38. A consumer that applies neocortical
computational assumptions (columnar organization, six-layer canonical
microcircuit) to BA34 will be **wrong** — and this is equally true on the
right side.

Function in the Human Brain
---------------------------
The right BA34 is a **memory, navigation, time-perception, and olfactory
gateway**. Its best-supported functions cluster into six domains — five
**symmetric** with the left twin and **one right-lateralized addition**:

*   **Gateway Between Hippocampus and Neocortex (the defining function,
    bilateral):** BA34, as part of the entorhinal cortex, is the **major
    interface between the hippocampus and neocortex**. It receives
    **convergent multimodal sensory inputs from neocortical association
    areas** and relays them to the hippocampus via the **perforant
    pathway**, facilitating **declarative memory encoding, consolidation,
    and spatial navigation**. This is a **bilateral** function.

*   **Spatial Memory Encoding (Right-Lateralized — the principal
    right-BA34 function):** In both the entorhinal and perirhinal cortices,
    **spatial encoding is biased to the right hemisphere**, whereas object
    encoding is biased to the left. A similar hemispheric bias
    is evident for **recognition memory**. The right BA34 is
    therefore the **dominant substrate for spatial memory encoding** within
    the entorhinal complex.

*   **Olfactory Processing (Right-Lateralized Activation):** The
    **right hemisphere is more activated than the left** during olfactory
    processing, including in the **entorhinal cortex (BA34)**, the amygdala,
    and orbitofrontal cortex[reference:5]. The right BA34 is part of the
    **olfactory cortex** and is involved in the **perception of smell**;
    **destruction of BA34 results in ipsilateral anosmia**.

*   **Declarative Memory (Episodic and Semantic, bilateral):** BA34 is part
    of the entorhinal-hippocampal system that plays an important role in
    **declarative (autobiographical/episodic/semantic) memories**, including
    **memory formation, memory consolidation, and memory optimization in
    sleep**. This is a **bilateral** function.

*   **Spatial Navigation and the Cognitive Map (bilateral, with right
    weighting):** BA34 contributes to the entorhinal cortex's role in
    **spatial navigation** and the **generation of spatial
    representations**, including contributions to **grid cell activity**.
    The **right-hemisphere spatial bias** makes the right BA34
    particularly important for **path integration** and **spatial-memory
    tasks**.

*   **Perception of Time (bilateral):** The entorhinal area is involved in
    the **perception of time**, a function that has been linked to
    entorhinal grid-cell-like mechanisms. This is a **bilateral** function.

Associated Disorders
--------------------
Damage to or dysfunction of the **right** BA34 is associated with:

*   **Spatial Memory Impairment (Right-Lateralized):** Impaired **spatial
    learning and spatial memory**, consistent with the right-hemisphere
    bias for spatial encoding in the entorhinal cortex.

*   **Ipsilateral Anosmia (Clinical Sign — Right-Sided):** Destruction of
    the **right** BA34 results in **anosmia on the right side**
    . However, in some clinical populations
    (e.g., Parkinson's disease), the **right BA34 may be relatively spared**
    from the pathological changes associated with anosmia, whereas the left
    BA34 shows significantly higher Z-scores.

*   **Olfactory Hallucinations (Cacosmy) in Temporal Lobe Epilepsy
    (Right-Sided):** Lesions in AB34 are related to **epileptic seizures of
    the temporal lobe that course with cacosmy** (olfactory
    hallucinations)[reference:12].

*   **Declarative Memory Impairment (Right-Lateralized for Spatial/
    Non-Verbal Material):** Impaired **spatial and non-verbal declarative
    memory**, consistent with the right-hemisphere bias for spatial
    encoding. This is the complement of the left BA34's **verbal memory**
    impairment.

*   **Alzheimer's Disease (Early and Severe):** BA34 is a **site of early
    pathology in Alzheimer's disease** — tau pathology and volume loss in
    BA34 correlate with **initial memory impairments** and contribute to
    **hippocampal isolation from neocortical inputs**.

*   **Temporal Lobe Epilepsy (Findings Reported):** BA34 has been implicated
    in **temporal lobe epilepsy**, consistent with the entorhinal cortex's
    role as a **critical substrate for seizure propagation**.

**No named "BA34 lesion syndrome" exists.** BA34 is discussed as a
**component of the entorhinal-hippocampal memory system**, not as a
standalone clinical node. Its clinical relevance is as a **contributor** to
spatial memory, olfactory processing, declarative memory, and Alzheimer's
disease pathology.

**What is NOT here:** **Wernicke's aphasia** (BA22), **semantic dementia**
(left anterior temporal), **pure alexia** (left VWFA, BA37), and
**prosopagnosia** (right FFA, BA37) are **not** BA34 syndromes. BA34 is a
**memory, navigation, and olfactory gateway**, not a language or visual-
recognition area. **Object recognition memory** is a **perirhinal (BA35/36)**
function, not a BA34 function.

Lateralization Notes
--------------------
This is the **right** BA34 module. The lateralization landscape is
**symmetric-by-bilateral-organization with a right-lateralized spatial and
olfactory weighting**:

*   **Right-Lateralized Functions (unique to this twin):**
    - **Spatial memory encoding** — biased to the right hemisphere in the
      entorhinal and perirhinal cortices.
    - **Olfactory processing** — the right hemisphere is more activated than
      the left during olfactory tasks, including BA34[reference:14].
    - **Spatial navigation and path integration** — the right-hemisphere
      spatial bias makes the right BA34 particularly important for
      spatial-memory tasks.

*   **Left-Lateralized Functions (contrast — absent here):**
    - **Object memory encoding** — biased to the left hemisphere in the
      entorhinal and perirhinal cortices.
    - **Verbal declarative memory** — the left BA34 preferentially supports
      verbal memory, consistent with the broader left-verbal bias of the
      medial temporal lobe.

*   **Symmetric Functions (bilateral properties of BA34, copied verbatim
    from the left twin):**
    - Gateway between hippocampus and neocortex.
    - Declarative memory (episodic and semantic).
    - Time perception.
    - Alzheimer's disease vulnerability.
    - Core entorhinal cytoarchitecture (lamina dissecans, cell islands,
      layer III projection neurons).

**A consumer that assumes "right BA34 = left BA34" will miss the
right-lateralized spatial-memory and olfactory-processing weightings.**
However, the **core gateway and declarative-memory functions are
bilateral** — the right BA34 is **not** the "complement" of the left in the
BA26 sense, and it is **not** a denial-based lateralization in the S1 sense.
This is the **"symmetric-by-bilateral-organization with a functional
weighting"** pattern — the same pattern as BA27 and BA28, refined for the
right-hemisphere spatial and olfactory emphases.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    hippocampus, the cingulate, or the parietal lobe. Those are
    **downstream/upstream targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Periallocortical leaf — flagged in prose and data.** BA34 is
    **periallocortical / allocortical**, not neocortical. The
    `CYTOARCHITECTONIC_TYPE` constant is **"allocortical"**. Consumers must
    not apply neocortical computational assumptions to BA34.
*   **Brodmann leaf under the temporal partition.** BA34 is a local leaf
    under `.../temporal/brodmann_areas/`, **not** a cross-listed or nested
    leaf. There is **no `AREA_PATHS` hop** and **no nested dual-framing
    module**.
*   **Dorsal entorhinal subdivision of the entorhinal complex.** BA34 is
    the **dorsal/anterior** subdivision of the entorhinal cortex; BA28 is
    the **ventral/posterior** subdivision. The `SUBFIELD` constant below
    makes this explicit. Consumers that need the full entorhinal cortex
    must query **both** modules.
*   **Right-lateralized spatial and olfactory weightings.** The
    `RIGHT_LATERALIZED` constant below documents the right-hemisphere
    spatial-memory and olfactory-processing biases. The left twin documents
    the left-hemisphere object-memory bias.
*   **Structural parity with left BA34.** Left and right BA34 modules are
    **structurally identical** — same periallocortical type, same
    dorsal-entorhinal identity, same gateway and memory functions — but the
    **lateralized weightings are explicitly documented on each side**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.brodmann_areas import brodmann_area_34

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.brodmann_areas.brodmann_area_34"
    )

**Do not** apply neocortical computational assumptions to BA34. It is
**periallocortical** — a hippocampal-formation gateway with a lamina
dissecans and cell islands in layer II. Use the `CYTOARCHITECTONIC_TYPE`
constant to check the type::

    from ...temporal.brodmann_areas.brodmann_area_34 import CYTOARCHITECTONIC_TYPE
    # CYTOARCHITECTONIC_TYPE = "allocortical"

For the right-lateralized functions::

    from ...temporal.brodmann_areas.brodmann_area_34 import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("spatial_memory_encoding",
    #                      "olfactory_processing",
    #                      "spatial_navigation_path_integration")

For the dorsal-entorhinal subfield identity::

    from ...temporal.brodmann_areas.brodmann_area_34 import SUBFIELD
    # SUBFIELD = "dorsal_entorhinal (anterior)"

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba34_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.brodmann_areas.brodmann_area_34"
        )
        # resolve ba34_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der
    Grosshirnrinde*. (BA34 defined as the area entorhinalis dorsalis.)
*   **Entorhinal cortex composition (BA28 + BA34):** Koubeissi, M.Z.
    (2015). "The piriform, perirhinal, and entorhinal cortex in seizure
    generation." *Frontiers in Neurology*. In humans, the entorhinal
    cortex consists of **Brodmann areas 28 and 34**, situated bilaterally
    between the sulcus semiannularis and sulcus rhinalis in the rostral
    parahippocampal gyrus.
*   **BA34 cytoarchitecture and connectivity:** Grokipedia — *Brodmann
    area 34* (2026). BA34 is the **anterior and dorsal portion of the
    entorhinal cortex**; it is characterized by an **agranular six-layered
    structure** with **cell-dense islands in layer II** and a **cell-sparse
    lamina dissecans as layer IV**; it receives **convergent multimodal
    sensory inputs** and relays them to the hippocampus via the **perforant
    pathway**.
*   **Right-lateralized spatial memory encoding:** Bellgowan, P.S.,
    Buffalo, E.A., Bodurka, J., & Martin, A. (2005). "Lateralized spatial
    and object memory encoding in entorhinal and perirhinal cortices."
    *Learning & Memory*, 12(3), 343–351. In both the perirhinal and
    entorhinal cortices, **object encoding was biased to the left
    hemisphere, whereas spatial encoding was biased to the right**
    .
*   **Right-lateralized olfactory processing:** *Right Occipital Cortex
    Activation Correlates with Superior Odor Processing Performance in the
    Early Blind* (2013), *PLoS ONE*, PMC3743806. During olfactory
    processing, the **right hemisphere appeared more activated than the
    left one**, including in the **entorhinal cortex (BA34)**
    [reference:18].
*   **Right BA34 and anosmia:** *[Function and anosmia in patients with
    Parkinson disease and Alzheimer disease]* (CiNii). In patients with
    anosmia, Z-scores were significantly high in all areas **except the
    right Brodmann area 34** in PD patients, suggesting a relative sparing
    of the right BA34 in some anosmia populations.
*   **Ipsilateral anosmia from BA34 destruction:** Wikipedia — *Brodmann
    area 34*. **Destruction of Brodmann area 34 results in ipsilateral
    anosmia**.
*   **Cacosmy and temporal lobe epilepsy:** Thieme Connect — *Cortical
    Brain Functions – The Brodmann Legacy in the 21st Century*. Lesions in
    AB34 are related to **epileptic seizures of the temporal lobe that
    course with cacosmy** (olfactory hallucinations)[reference:21].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial temporal and hippocampal-formation anatomy.)
*   NeuroNames — Brodmann area 34 (right); FMA — Brodmann area 34 (right
    member).
"""