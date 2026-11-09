"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.brodmann_areas.brodmann_area_34
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
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
along the **parahippocampal gyrus** and **gyrus ambiens**[reference:1]. Its
anterior extent begins approximately **4–7 mm anterior to the limen insula**,
and its posterior border lies near the **tip of the gyrus intralimbicus**
[reference:2].
**Structural parent:** This is a **Brodmann leaf**, not a gyral child. It
lives directly under the left temporal Brodmann aggregator.
**Cytoarchitectonic type:** **Periallocortical / allocortical** — BA34 is
**not neocortical**. It is a transitional cortex between the hippocampus
(archicortex) and the neocortical parahippocampal gyrus.

Overview
--------
Brodmann Area 34 (BA34) is the **dorsal (anterior) subdivision of the
entorhinal cortex** — the **major gateway between the hippocampal formation
and the neocortex**[reference:4]. Together with BA28, it forms
the **entorhinal complex**, the nodal point of the cortico-hippocampal
circuit that supports **declarative memory, spatial navigation, and the
perception of time**[reference:6].

**BA34 is the third allocortical leaf documented in this tree**, following
BA27 (presubiculum) and BA28 (entorhinal cortex). The temporal Brodmann
aggregator flagged BA27, BA28, BA34, and BA35 as **allocortical or
transitional fields** (via the `CYTOARCHITECTONIC_TYPE` constant) — and this
module continues that series. Consumers that assume all Brodmann areas are
neocortical will be **wrong for BA34**: it has **fewer layers**, a
distinctive **lamina dissecans** (a cell-sparse layer IV), and **cell-dense
islands in layer II**[reference:7].

**BA34 is the dorsal/anterior entorhinal cortex, and it is cytoarchitectonically
distinct from BA28.** BA28 is the **ventral/posterior** entorhinal cortex
(the classical "area entorhinalis"), while BA34 is the **dorsal/anterior**
entorhinal cortex (the "area entorhinalis dorsalis")[reference:8][reference:9].
The two together constitute the human entorhinal cortex, but they have
**different cytoarchitectonic signatures and different connectivity
profiles**. Consumers that need the full entorhinal cortex must query **both
BA28 and BA34**.

Periallocortical Cytoarchitecture
--------------------------------
BA34 is **periallocortical / allocortical** — a transitional cortex between
the archicortex of the hippocampus and the neocortex of the parahippocampal
gyrus. Its cytoarchitectonic features include:

*   **Agranular six-layered structure** — BA34 is characterized by an
    **agranular six-layered structure**, including **distinctive cell-dense
    islands in layer II** and a **cell-sparse lamina dissecans as layer IV**
    , distinguishing it from adjacent areas like the perirhinal cortex
    (BA35)[reference:10].

*   **Paucity of cells in layer IV (lamina dissecans)** — the entorhinal
    cortex (including BA34) has a **striking paucity of cells in layer IV
    (lamina dissecans)**, which separates the **outer cell-rich layers (V
    and VI)** from the **inner cell-rich layers (II and III)**
    . This is a **hallmark of entorhinal cortex** and is absent
    from neocortex.

*   **Layer III pyramidal projection neurons** — **layer III** consists of
    **pyramidal projection neurons** that target the **hippocampus and other
    regions** . This is the principal output layer of the
    entorhinal cortex to the hippocampus.

*   **Neurochemical signature** — BA34 shows **moderate parvalbumin
    immunoreactivity in layer IIIb** and **lighter calbindin labeling**
    compared to neighboring perirhinal regions, aiding precise delineation in
    histological and neuroimaging studies[reference:13].

**This periallocortical identity is the defining structural fact about
BA34.** It is **not** a neocortical association area; it is a
**hippocampal-formation gateway** with a different computational
architecture from BA20/21/22/37/38. A consumer that applies neocortical
computational assumptions (columnar organization, six-layer canonical
microcircuit) to BA34 will be **wrong**.

Entorhinal Subfield Context
---------------------------
The entorhinal cortex is divided into two major subfields, and BA34
corresponds to the **dorsal/anterior** component:

*   **Dorsal/anterior entorhinal cortex (BA34)** — the subdivision
    documented here. It is the **anterior and dorsal portion** of the
    entorhinal cortex along the parahippocampal gyrus and gyrus ambiens
    [reference:14].

*   **Ventral/posterior entorhinal cortex (BA28)** — the classical
    "area entorhinalis" (area entorhinalis ventralis), documented in the
    sibling BA28 module.

**The dorsal/ventral (anterior/posterior) distinction is not merely
geometric — it reflects a functional and connectional gradient.** The
entorhinal cortex as a whole is organized into **rostro-caudal bands** that
project to different septo-temporal levels of the dentate gyrus
, and its subregions differ in their **connectivity and
physiology**. BA34, as the dorsal/anterior component, is part
of this **topographic organization** and contributes to the entorhinal
cortex's role as a **topographically organized gateway**.

Function in the Human Brain
---------------------------
The left BA34 is a **memory, navigation, and time-perception gateway**.
Its best-supported functions cluster into six domains:

*   **Gateway Between Hippocampus and Neocortex (the defining function):**
    BA34, as part of the entorhinal cortex, is the **major interface between
    the hippocampus and neocortex**[reference:18]. It receives
    **convergent multimodal sensory inputs from neocortical association
    areas** and relays them to the hippocampus via the **perforant
    pathway**, facilitating **declarative memory encoding, consolidation,
    and spatial navigation**[reference:19].

*   **Declarative Memory (Episodic and Semantic):** BA34 is part of the
    entorhinal-hippocampal system that plays an important role in
    **declarative (autobiographical/episodic/semantic) memories**, including
    **memory formation, memory consolidation, and memory optimization in
    sleep**[reference:20]. The bidirectional connections between BA34 and the
    hippocampal formation support the **formation of episodic memories**
    [reference:21].

*   **Spatial Navigation and the Cognitive Map:** BA34 contributes to the
    entorhinal cortex's role in **spatial navigation** and the **generation
    of spatial representations**, including contributions to **grid cell
    activity** observed in the entorhinal cortex[reference:22]. The entorhinal
    cortex is a **hub in a widespread network for memory and navigation**
    [reference:23].

*   **Perception of Time:** The entorhinal area is involved in the
    **perception of time**, a function that has been linked to
    entorhinal grid-cell-like mechanisms and to the broader hippocampal-
    entorhinal system for temporal cognition.

*   **Olfactory Processing (Conventional / Clinical):** Destruction of
    Brodmann area 34 results in **ipsilateral anosmia**,
    consistent with the entorhinal cortex's historical association with the
    olfactory system and its position adjacent to the rhinal sulcus.

*   **Alzheimer's Disease Vulnerability (Early Pathology):** Early
    degeneration in BA34, marked by **tau pathology and volume loss
    detectable via MRI**, is a **hallmark of Alzheimer's disease
    progression**, correlating with **initial memory impairments** and
    **isolating the hippocampus from neocortical inputs**
    [reference:26].

Associated Disorders
--------------------
Damage to or dysfunction of the left BA34 is associated with:

*   **Declarative Memory Impairment (Left-Lateralized for Verbal
    Material):** Impaired **episodic and semantic memory**, consistent with
    BA34's role as part of the hippocampal-neocortical gateway. Left BA34
    damage preferentially impairs **verbal declarative memory**, mirroring
    the left-verbal / right-spatial bias observed in the broader medial
    temporal lobe.

*   **Spatial Memory and Navigation Deficits:** Impaired **spatial learning
    and memory**, consistent with the entorhinal cortex's role in grid-cell-
    based navigation and spatial representation[reference:28].

*   **Ipsilateral Anosmia (Clinical Sign):** Destruction of BA34 results in
    **ipsilateral anosmia**, a clinically testable sign of
    entorhinal/orbitofrontal damage.

*   **Alzheimer's Disease (Early and Severe):** BA34 is a **site of early
    pathology in Alzheimer's disease** — tau pathology and volume loss in
    BA34 correlate with **initial memory impairments** and contribute to
    **hippocampal isolation from neocortical inputs**[reference:30].

*   **Temporal Lobe Epilepsy (Findings Reported):** BA34 has been implicated
    in **temporal lobe epilepsy**[reference:31], consistent with the
    entorhinal cortex's role as a **critical substrate for seizure
    propagation** via layer III pyramidal projection neurons
    .

*   **Frontotemporal Dementia (Findings Reported):** BA34 has been implicated
    in **frontotemporal dementia**[reference:33], though this is a **finding
    reported** rather than an established syndrome attribution.

**No named "BA34 lesion syndrome" exists.** BA34 is discussed as a
**component of the entorhinal-hippocampal memory system**, not as a
standalone clinical node. Its clinical relevance is as a **contributor** to
declarative memory, spatial navigation, time perception, and Alzheimer's
disease pathology.

**What is NOT here:** **Wernicke's aphasia** (BA22), **semantic dementia**
(left anterior temporal), **pure alexia** (left VWFA, BA37), and
**prosopagnosia** (right FFA, BA37) are **not** BA34 syndromes. BA34 is a
**memory and navigation gateway**, not a language or visual-recognition
area. **Object recognition memory** is a **perirhinal (BA35/36)** function,
not a BA34 function.

Lateralization Notes
--------------------
This is the **left** BA34 module. The lateralization of BA34 is **weakly
established** — the area is part of the **bilateral entorhinal-hippocampal
system**, and no strong left-right functional asymmetry has been
demonstrated for its core gateway or memory functions:

*   **No Established Lateralized Syndrome:** Unlike BA22 (left Wernicke's /
    right prosodic) or BA37 (left VWFA / right FFA), BA34 has **no
    documented left-lateralized or right-lateralized function** for its core
    entorhinal functions. The entorhinal-hippocampal system is **bilaterally
    organized** for declarative memory and spatial cognition.

*   **Hippocampal Lateralization (Contrast):** The medial temporal lobe
    shows a **functional bias** — **object encoding is biased to the left
    hemisphere, whereas spatial encoding is biased to the right**
    . This bias applies to both the perirhinal and
    entorhinal cortices, and therefore to BA34. However, this is a
    **weighting**, not a **dominance** — both hemispheres carry the gateway
    and memory functions, but the **emphasis** differs slightly.

*   **Symmetric Functions (presumed bilateral, copied verbatim to the right
    twin):** Gateway between hippocampus and neocortex, declarative memory,
    spatial navigation (grid cells), time perception, olfactory processing,
    and Alzheimer's disease vulnerability are **presumed bilateral** for
    the entorhinal cortex.

**A consumer that assumes "left BA34 = right BA34" will be approximately
correct** — not because BA34 is perfectly symmetric, but because **no
strong lateralization has been demonstrated** for its core functions beyond
the weak left-object / right-spatial bias inherited from the broader medial
temporal lobe. This is the **"symmetric-by-bilateral-organization"** pattern
— the same pattern as BA27 and BA28, and distinct from the **"symmetric-by-
default"** pattern of BA15.

**The only lateralized function attributable to BA34 is the left-object /
right-spatial bias**, which is inherited from the broader medial temporal
lobe rather than being a BA34-specific asymmetry. The **gateway function**
and the **temporal-perception function** are bilateral.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    hippocampus, the cingulate, or the parietal lobe. Those are
    **downstream/upstream targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Periallocortical leaf — flagged in prose and data.** BA34 is
    **periallocortical / allocortical**, not neocortical. The
    `CYTOARCHITECTONIC_TYPE` constant is **"allocortical"** (per the
    temporal Brodmann aggregator's type map). Consumers must not apply
    neocortical computational assumptions to BA34.
*   **Brodmann leaf under the temporal partition.** BA34 is a local leaf
    under `.../temporal/brodmann_areas/`, **not** a cross-listed or nested
    leaf. There is **no `AREA_PATHS` hop** and **no nested dual-framing
    module**.
*   **Dorsal entorhinal subdivision of the entorhinal complex.** BA34 is
    the **dorsal/anterior** subdivision of the entorhinal cortex; BA28 is
    the **ventral/posterior** subdivision. The `SUBFIELD` constant below
    makes this explicit. Consumers that need the full entorhinal cortex
    must query **both** modules.
*   **Structural parity with right BA34.** Left and right BA34 modules
    are **structurally identical** — same periallocortical type, same
    dorsal-entorhinal identity, same gateway and memory functions, same
    weak lateralization.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.brodmann_areas import brodmann_area_34

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.brodmann_areas.brodmann_area_34"
    )

**Do not** apply neocortical computational assumptions to BA34. It is
**periallocortical** — a hippocampal-formation gateway with a lamina
dissecans and cell islands in layer II. Use the `CYTOARCHITECTONIC_TYPE`
constant to check the type::

    from ...temporal.brodmann_areas.brodmann_area_34 import CYTOARCHITECTONIC_TYPE
    # CYTOARCHITECTONIC_TYPE = "allocortical"

For the dorsal-entorhinal subfield identity::

    from ...temporal.brodmann_areas.brodmann_area_34 import SUBFIELD
    # SUBFIELD = "dorsal_entorhinal (anterior)"

For the gateway and memory functions::

    from ...temporal.brodmann_areas.brodmann_area_34 import SYMMETRIC_FUNCTIONS
    # gateway_hippocampus_neocortex, declarative_memory,
    # spatial_navigation_grid_cells, time_perception,
    # olfactory_processing, alzheimer_disease_vulnerability

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
    generation." *Frontiers in Neurology* / *Scholar*. In humans, the
    entorhinal cortex consists of **Brodmann areas 28 and 34**, situated
    bilaterally between the sulcus semiannularis and sulcus rhinalis in the
    rostral parahippocampal gyrus.
*   **BA34 cytoarchitecture and connectivity:** Grokipedia — *Brodmann
    area 34* (2026). BA34 is the **anterior and dorsal portion of the
    entorhinal cortex**; it is characterized by an **agranular six-layered
    structure** with **cell-dense islands in layer II** and a **cell-sparse
    lamina dissecans as layer IV**; it receives **convergent multimodal
    sensory inputs** and relays them to the hippocampus via the **perforant
    pathway**; its **bidirectional connections** with the hippocampal
    formation support **episodic memory and spatial representation**
    [reference:37].
*   **Entorhinal cortex layers and connectivity:** Koubeissi (2015). The
    entorhinal cortex is an allocortical structure with **six layers**,
    a **striking paucity of cells in layer IV (lamina dissecans)**, and
    **layer III pyramidal projection neurons** that target the hippocampus
    .
*   **Dorsal entorhinal identity:** Wikipedia — *Brodmann area 34*. BA34
    is the **area entorhinalis dorsalis**. It is part of the
    entorhinal area together with BA28.
*   **Function and clinical associations:** Wikipedia — *Brodmann area 34*.
    The entorhinal area is the **main interface between the hippocampus and
    neocortex** and is involved in **memory, navigation, and the perception
    of time**; destruction of BA34 results in **ipsilateral anosmia**
    .
*   **Entorhinal cortex function:** IMAIOS — *Area 34 — Anterior entorhinal
    cortex*. The entorhinal cortex is a **hub in a widespread network for
    memory and navigation**, the **main interface between the hippocampus
    and neocortex**; the entorhinal-hippocampal system is important for
    **declarative memories** (autobiographical/episodic/semantic) and
    **spatial memories**, including memory formation, consolidation, and
    optimization in sleep[reference:42].
*   **Lateralized memory encoding:** *Lateralized spatial and object memory
    encoding in entorhinal and perirhinal cortices* (LearnMem). In both
    the perirhinal and entorhinal cortices, **object encoding is biased to
    the left hemisphere**, whereas **spatial encoding is biased to the
    right**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial temporal and hippocampal-formation anatomy.)
*   NeuroNames — Brodmann area 34 (left); FMA — Brodmann area 34 (left
    member).
"""