"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.brodmann_areas.brodmann_area_28
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
                        └── brodmann_area_28   <-- THIS MODULE

**Primary synonym:** Brodmann Area 28 (BA28); **Entorhinal cortex (EC)**;
Area entorhinalis.
**Cytoarchitectonic designation:** Area 28 of Brodmann (1909). Brodmann
originally subdivided BA28 into **28a (lateral)** and **28b (medial)**,
corresponding to the modern **lateral entorhinal cortex (LEC)** and
**medial entorhinal cortex (MEC)**.
**Part of:** The **hippocampal-parahippocampal formation** — the
allocortical memory and spatial-cognition system.
**Location:** The **anterior aspect of the parahippocampal gyrus** on the
medial surface of the right temporal lobe. BA28 is partially enclosed by
the **rhinal (olfactory) sulcus** — the feature from which its name is
derived.
**Structural parent:** This is a **Brodmann leaf**, not a gyral child. It
lives directly under the right temporal Brodmann aggregator.
**Cytoarchitectonic type:** **Periallocortical** — BA28 is **not
neocortical**. It is a transitional cortex between the hippocampus
(archicortex) and the neocortical parahippocampal gyrus.

Overview
--------
Brodmann Area 28 (BA28) is the **entorhinal cortex** — the **major
gateway between the hippocampal formation and the neocortex**
. It is the **nodal point of the cortico-hippocampal
circuit**: **superficial layers receive convergent cortical information**
from a variety of multimodal association areas and relay it to the
hippocampus, while **hippocampal output reaches the deep layers** of the
entorhinal cortex and is projected **back to the cortex**
. This **bidirectional gateway** function makes BA28
the **single most important cortical interface** for declarative memory
and spatial cognition.

**This is the right-hemisphere twin of the left BA28, and the pair is
SYMMETRIC-BY-BILATERAL-ORGANIZATION.** Unlike BA20 (asymmetric-by-
function), BA21 (left-loaded with right complement), and BA22
(hemispheric dominance by function), BA28 is **bilaterally organized as
part of the hippocampal formation**. No strong left-right functional
asymmetry has been demonstrated for its core gateway, memory, or
navigation functions. **This module is structurally and functionally
identical to the left BA28** — only the path segment differs.

**BA28 is the second periallocortical leaf documented in this tree**,
following BA27 (presubiculum). The temporal Brodmann aggregator flagged
BA27, BA28, BA34, and BA35 as **allocortical or transitional fields**
(via the `CYTOARCHITECTONIC_TYPE` constant) — and this module continues
that series. Consumers that assume all Brodmann areas are neocortical
will be **wrong for BA28**: it has fewer layers, a distinctive **lamina
disens** (a cell-sparse layer), and **cell islands in layer II** that
are absent from neocortex.

**BA28 is the entorhinal cortex, and it is NOT the perirhinal cortex.**
The perirhinal cortex corresponds to **BA35 and BA36**, which are
adjacent to BA28 laterally. BA28 is the **medial** component of the
parahippocampal region, and its **principal function is spatial and
mnemonic**, not object recognition (which is perirhinal).

Periallocortical Cytoarchitecture
--------------------------------
BA28 is **periallocortical** — a transitional cortex between the
archicortex of the hippocampus and the neocortex of the parahippocampal
gyrus. Its cytoarchitectonic features are **identical to the left twin**:

*   **Six layers, but not the neocortical six** — the entorhinal cortex
    is generally subdivided into **six layers**: four cellular layers
    (**layers II, III, V, and VI**) and two **acellular or plexiform
    layers** (**layer I** and **layer IV, the lamina disens**)
    . The **lamina disens** is a
    **cell-sparse layer** that is a hallmark of entorhinal cortex and is
    absent from neocortex.

*   **Cell islands in layer II** — the most conspicuous feature of the
    human entorhinal cortex is the **cell islands of layer II** (the
    "glomeruli" of the entorhinal cortex), surrounded by myelinated
    fibers . These
    islands are **the defining cytoarchitectonic signature** of BA28.

*   **Subfields: LEC and MEC** — Brodmann's original **28a (lateral)** and
    **28b (medial)** correspond to the modern **lateral entorhinal
    cortex (LEC)** and **medial entorhinal cortex (MEC)**
    . In the rat, the LEC occupies the
    rostrolateral part of EC, and the MEC occupies the remaining
    triangular area with its base caudally and its tip rostromedially
    . The two subfields have
    **different connectivity and different functions**:
    - **LEC** — more strongly connected with **perirhinal, visual,
      auditory, and multimodal association cortices**; associated with
      **item-based memory** (the "what" pathway).
    - **MEC** — more strongly connected with **spatial and navigational
      systems**; associated with **spatial memory** (the "where"
      pathway).

**This periallocortical identity is the defining structural fact about
BA28.** It is **not** a neocortical association area; it is a
**hippocampal-formation gateway** with a different computational
architecture from BA20/21/22/37/38. A consumer that applies neocortical
computational assumptions (columnar organization, six-layer canonical
microcircuit) to BA28 will be **wrong** — and this is equally true on
the right side.

Function in the Human Brain
---------------------------
The right BA28 is a **memory and spatial-navigation gateway**. Its
best-supported functions cluster into six domains — **identical to the
left twin**, because BA28's core functions are bilaterally organized:

*   **Gateway Between Hippocampus and Neocortex (the defining function):**
    BA28 is the **major input and output structure of the hippocampal
    formation** . **Superficial layers** receive
    convergent cortical information from multimodal association areas and
    relay it to the hippocampus; **deep layers** receive hippocampal
    output and project it back to the cortex
    . This **bidirectional gateway** function is the
    **architectural signature** of the entorhinal cortex.

*   **Declarative Memory (Episodic and Semantic):** BA28 is a major
    substrate for **conscious (declarative) memory**
    . It is the **nodal point** of the cortico-hippocampal
    circuits that support **episodic memory** (memory for events and
    their spatiotemporal context) and **semantic memory** (memory for
    facts and concepts).

*   **Spatial Navigation and the Cognitive Map (MEC):** The **medial
    entorhinal cortex (MEC)** contains **grid cells** — neurons that
    fire in a **regular hexagonal spatial pattern** and provide the brain
    with a **spatial metric system** for navigation
    . Grid cells in the MEC provide inputs to
    **place cells** in the hippocampus and are a core component of the
    brain's **cognitive map** . The MEC is a
    **key brain area for spatial learning and memory**
    .

*   **Path Integration and Prospective Coding:** Entorhinal neurons
    exhibit **prospective coding** — activity that represents the
    **future path** of an animal through the environment, in contrast to
    the **retrospective coding** of hippocampal CA1 neurons
    . The entorhinal cortex represents **similarities or
    regularities across different trajectories** (path equivalence), a
    mechanism for **generalization across experiences during navigation**
    .

*   **Olfactory and Multimodal Sensory Integration:** BA28 is
    **partially enclosed by the rhinal (olfactory) sulcus** and
    historically was considered part of the olfactory cortex
    . In modern terms, it receives **convergent
    multimodal sensory inputs** — visual, auditory, somatosensory, and
    olfactory — from association cortices and integrates them into a
    **unified memory trace** .

*   **Alzheimer's Disease Vulnerability (Early Pathology):** BA28 is a
    **site of early pathology in Alzheimer's disease** — the
    entorhinal cortex is one of the **first regions to show
    neurofibrillary tangles and cell loss** in AD, and its degeneration
    is a **core substrate of the early memory impairment** in the
    disease .

Associated Disorders
--------------------
Damage to or dysfunction of the right BA28 is associated with the **same
disorders as the left BA28** — because BA28's core functions are
bilaterally organized:

*   **Declarative Memory Impairment (Right-Lateralized for Spatial/
    Non-Verbal Material):** Impaired **episodic and semantic memory**,
    consistent with BA28's role as the hippocampal-neocortical gateway.
    Right BA28 damage preferentially impairs **spatial and non-verbal
    declarative memory** (the complement of the left's verbal-memory
    impairment).

*   **Spatial Memory and Navigation Deficits (Bilateral, MEC-Dependent):**
    Impaired **spatial learning and memory**, consistent with the MEC's
    role in grid-cell-based navigation . These deficits
    are **bilateral** because the MEC's spatial map is bilaterally
    organized.

*   **Alzheimer's Disease (Early and Severe):** The entorhinal cortex is
    **one of the earliest and most severely affected regions in
    Alzheimer's disease** . Entorhinal atrophy is a
    **core biomarker of AD progression**, and its degeneration is a
    **core substrate of the early memory impairment**.

*   **Temporal Lobe Epilepsy (Findings Reported):** BA28 has been
    implicated in **temporal lobe epilepsy**, though this is a **finding
    reported** rather than an established syndrome attribution.

*   **Schizophrenia (Findings Reported):** Entorhinal cortex
    abnormalities have been reported in schizophrenia, though these are
    **findings reported** rather than established syndrome attributions.

**No named "BA28 lesion syndrome" exists.** BA28 is discussed as a
**component of the hippocampal-parahippocampal memory system**, not as a
standalone clinical node. Its clinical relevance is as a **contributor**
to declarative memory, spatial navigation, and Alzheimer's disease
pathology.

**What is NOT here:** **Wernicke's aphasia** (BA22), **semantic
dementia** (left anterior temporal), **pure alexia** (left VWFA, BA37),
and **prosopagnosia** (right FFA, BA37) are **not** BA28 syndromes.
BA28 is a **memory and spatial-navigation gateway**, not a language or
visual-recognition area. **Object recognition memory** is a **perirhinal
(BA35/36)** function, not a BA28 function — and this is equally true on
the right side.

Lateralization Notes
--------------------
This is the **right** BA28 module. The lateralization landscape is
**symmetric-by-bilateral-organization** — the area is part of the
**bilateral hippocampal-parahippocampal system**, and no strong left-right
functional asymmetry has been demonstrated for its core gateway, memory,
or navigation functions:

*   **No Established Lateralized Syndrome:** Unlike BA22 (left Wernicke's
    / right prosodic) or BA37 (left VWFA / right FFA), BA28 has **no
    documented left-lateralized or right-lateralized function** for its
    core entorhinal functions. The hippocampal formation is **bilaterally
    organized** for spatial cognition and episodic memory.

*   **Hippocampal Lateralization (Contrast):** The hippocampus itself
    shows some lateralization — **left for verbal memory, right for
    spatial memory** — and this lateralization extends to the entorhinal
    cortex to some degree. However, the **core gateway function** of BA28
    is **bilateral**, and the **grid-cell spatial map** is bilaterally
    organized. The right BA28 contributes more to **spatial and non-
    verbal memory**, and the left BA28 contributes more to **verbal
    memory**, but this is a **weighting**, not a **dominance**.

*   **Structural Asymmetry (Weak):** The entorhinal cortex shows
    **left-right volumetric differences** in some studies (left BA28
    volume ≈ 860 mm³, right ≈ 875 mm³ in one study
    ), but these are **small and not consistently
    functionally meaningful**. No strong right-specific structural
    asymmetry has been reported for BA28.

*   **Symmetric Functions (presumed bilateral, copied verbatim from the
    left twin):** Gateway between hippocampus and neocortex,
    declarative memory, spatial navigation (grid cells), path
    integration, multimodal sensory integration, and Alzheimer's disease
    vulnerability are **presumed bilateral** for the entorhinal cortex.

**A consumer that assumes "right BA28 = left BA28" will be approximately
correct** — not because BA28 is perfectly symmetric, but because **no
strong lateralization has been demonstrated** for its core functions.
The area is **bilaterally organized** as part of the hippocampal
formation. This is the **"symmetric-by-bilateral-organization"** pattern
— the same pattern as BA27, and distinct from the **"symmetric-by-
default"** pattern of BA15 (which is symmetric because **no function has
been established**).

**The only lateralized function attributable to BA28 is the left-verbal
/ right-spatial split**, which is inherited from the broader hippocampal
lateralization rather than being a BA28-specific asymmetry. The
**gateway function** and the **grid-cell spatial map** are bilateral.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    hippocampus, the cingulate, or the parietal lobe. Those are
    **downstream/upstream targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Periallocortical leaf — flagged in prose and data.** BA28 is
    **periallocortical**, not neocortical. The `CYTOARCHITECTONIC_TYPE`
    constant is **"allocortical"** (per the temporal Brodmann
    aggregator's type map). Consumers must not apply neocortical
    computational assumptions to BA28.
*   **Brodmann leaf under the temporal partition.** BA28 is a local leaf
    under `.../temporal/brodmann_areas/`, **not** a cross-listed or
    nested leaf. There is **no `AREA_PATHS` hop** and **no nested dual-
    framing module**.
*   **Subfields LEC and MEC documented as data.** Brodmann's 28a/28b
    correspond to the modern LEC/MEC, which have **different connectivity
    and functions** (item-based vs. spatial-based memory). The `SUBFIELDS`
    constant below makes the distinction explicit and greppable.
*   **Not the perirhinal cortex.** BA28 is the **entorhinal cortex**;
    the perirhinal cortex is **BA35/BA36**. Consumers must not conflate
    them — they are adjacent but functionally distinct (spatial-mnemonic
    vs. object-recognition).
*   **Structural parity with left BA28.** Left and right BA28 modules
    are **structurally identical** — same periallocortical type, same
    entorhinal identity, same gateway and memory functions, same weak
    lateralization. **The only difference between the two modules is the
    path segment (`right` vs `left`), plus the flipped verbal/spatial
    weighting in the disorders section.**

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.brodmann_areas import brodmann_area_28

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.brodmann_areas.brodmann_area_28"
    )

**Do not** apply neocortical computational assumptions to BA28. It is
**periallocortical** — a hippocampal-formation gateway with a lamina
disens and cell islands in layer II. Use the `CYTOARCHITECTONIC_TYPE`
constant to check the type::

    from ...temporal.brodmann_areas.brodmann_area_28 import CYTOARCHITECTONIC_TYPE
    # CYTOARCHITECTONIC_TYPE = "allocortical"

For the LEC/MEC subfields::

    from ...temporal.brodmann_areas.brodmann_area_28 import SUBFIELDS
    # SUBFIELDS["LEC"], SUBFIELDS["MEC"]

For the gateway and memory functions::

    from ...temporal.brodmann_areas.brodmann_area_28 import SYMMETRIC_FUNCTIONS
    # gateway_hippocampus_neocortex, declarative_memory,
    # spatial_navigation_grid_cells, path_integration,
    # multimodal_sensory_integration, alzheimer_disease_vulnerability

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba28_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.brodmann_areas.brodmann_area_28"
        )
        # resolve ba28_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der
    Grosshirnrinde*. (BA28 defined as the entorhinal area; subdivided
    into 28a and 28b.)
*   **Entorhinal cortex overview:** Witter, M. (2011). "Entorhinal
    cortex." *Scholarpedia*, 6(10), 4380. The entorhinal cortex
    (Brodmann area 28) constitutes the **major gateway between the
    hippocampal formation and the neocortex**; part of the medial
    temporal lobe memory system; site of early pathology in Alzheimer's
    disease .
*   **Anatomical organization and connectivity:** Witter, M.P., et al.
    (2008). "What Does the Anatomical Organization of the Entorhinal
    Cortex Tell Us?" *Neural Plasticity*, 2008, 381243. PMC2526269.
    Superficial layers receive convergent cortical information;
    hippocampal output reaches deep layers; the entorhinal cortex is the
    nodal point of cortico-hippocampal circuits; it harbors different
    subdivisions that mediate parallel input/output channels
    .
*   **Grid cells and spatial navigation:** Hafting, T., et al. (2005).
    *Nature*. The discovery of **grid cells** in the **medial entorhinal
    cortex (MEC)** put place cells in context; grid cells provide a
    **spatial metric system** for navigation; MEC is a key brain area for
    spatial learning and memory .
*   **Prospective coding and path equivalence:** Frank, L.M., et al.
    (2000). Entorhinal cells exhibit **prospective coding** (future
    path); deep entorhinal cells show **path equivalence** (similarities
    across different trajectories) — a mechanism for generalization
    across experiences during navigation .
*   **Cytoarchitecture and layers:** *Cortex Layer III* (ScienceDirect).
    The entorhinal cortex is considered **periallocortex**; it has
    **six layers** (four cellular, two acellular, including the **lamina
    disens**); Brodmann's 28a and 28b correspond to **LEC and MEC**
    .
*   **Cell islands in layer II:** *Entorhinal cortex modules of the human
    brain* (1996), *PubMed*. The human entorhinal cortex is formed by a
    **mosaic of cellular aggregates** whose most conspicuous elements are
    the **cell islands of layer II** .
*   **Human entorhinal cortex parcellation:** *Parahippocampal Gyrus*
    (ScienceDirect). The human entorhinal cortex can be partitioned into
    **up to eight fields**; the rhinal sulcus is rostral to the
    entorhinal cortex; BA35/36 (perirhinal) is laterally adjacent
    .
*   **Hippocampal lateralization:** *Hippocampal lateralization* — the
    hippocampus is generally left-lateralized for verbal memory and
    right-lateralized for spatial/non-verbal memory, with the entorhinal
    cortex participating in these functional networks.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial temporal and hippocampal-formation anatomy.)
*   NeuroNames — Brodmann area 28 (right); FMA — Brodmann area 28 (right
    member).
"""