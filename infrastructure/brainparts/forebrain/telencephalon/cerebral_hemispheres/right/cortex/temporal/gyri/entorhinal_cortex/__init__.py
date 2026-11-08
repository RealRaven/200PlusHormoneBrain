"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri.entorhinal_cortex
================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── gyri
                        └── entorhinal_cortex   <-- THIS MODULE

**Primary synonym:** Entorhinal cortex (EC), right; Right EC; Brodmann
areas 28 and 34; Area entorhinalis.
**Organizing principle:** **Hybrid structural-functional node** — the
entorhinal cortex is **not a classical gyral convolution**. It is a
**cytoarchitectonically defined periallocortical region** that sits
**within the parahippocampal gyrus** and is wired under ``gyri/`` as a
**structurally addressable memory unit**. See "Hybrid-Name Status"
below.
**Brodmann constitution:** **BA28** (ventral/posterior entorhinal) and
**BA34** (dorsal/anterior entorhinal). Both are **periallocortical**
fields with a **lamina dissecans** and **layer II cell islands**.
**Location:** The **medial aspect of the parahippocampal gyrus** in the
right temporal lobe, **immediately caudal to the olfactory cortex of the
uncus** and **medial to the rhinal fissure**.
**Structural parent:** Child of ``.../temporal/gyri`` (the structural
partition of the temporal lobe).
**Cytoarchitectonic type:** **Periallocortical** — a transitional cortex
between the allocortex of the hippocampal formation and the neocortex of
the parahippocampal gyrus.

Overview
--------
The **right entorhinal cortex (EC)** is the **principal gateway between
the hippocampal formation and the neocortex** in the right hemisphere —
the **cortical entry point for declarative memory and spatial
navigation**. It receives **highly processed multimodal information**
from the perirhinal and parahippocampal cortices and from unimodal and
polymodal association areas, and it relays this information to the
hippocampus via the **perforant pathway**. It also receives
**hippocampal output** and projects it **back to the neocortex**,
completing the **cortico-hippocampal loop** that supports **memory
encoding, consolidation, and retrieval**.

**The EC is the first hybrid-name "gyrus" documented in this tree.** It
is **not a classical surface convolution** — it is a
**cytoarchitectonically defined periallocortical region** that sits
**within the parahippocampal gyrus**. Its presence under ``gyri/``
reflects the tree's choice to treat it as a **structurally addressable
memory unit**, not as a surface convolution. **Consumers must not assume
that ``entorhinal_cortex`` is a gyrus in the same sense as
``superior_temporal_gyrus``** — it is a **hybrid name**, and its
cytoarchitectonic identity is defined by **Brodmann areas 28 and 34**,
not by a gyral boundary.

**This is the right-hemisphere twin of the left EC, and the pair
instantiates the "asymmetric-by-function" pattern** — a **process-
specific division of labor** within the medial temporal memory system:

*   **The left EC is the left-lateralized pole** for **object encoding,
    abstract processing, and verbal learning** — it carries the **left-
    hemisphere weighting** for **object identity memory** and **abstract
    spatial reasoning**.

*   **The right EC is the right-lateralized pole** for **spatial
    encoding, sensory-driven processing, self-referential navigation,
    and real-time spatial data integration** — it carries the **right-
    hemisphere weighting** for **spatial location memory** and
    **sensory-driven spatial processing**.

**The EC is the most clinically important "gyrus" in the temporal lobe.**
It is the **site of earliest pathology in Alzheimer's disease** — the
formation of **neurofibrillary tangles and cell death** begins in the EC
**before clinical symptoms emerge**. It is also a **key substrate for
temporal lobe epilepsy seizure generation and propagation**. These
clinical facts make the EC one of the **highest-value modules in the
entire brainparts tree** — and the right EC is **equally affected** in
both diseases.

Hybrid-Name Status
------------------
The EC is **not a gyral convolution**. It is a **periallocortical region**
that is **co-extensive with the medial aspect of the parahippocampal
gyrus** and is **reachable via the ``gyri/`` partition** as a
**structurally addressable memory unit**. This is the **first hybrid-name
"gyrus" in the tree** — a **cytoarchitectonically defined region** that
is presented as a "gyrus" for **structural addressability**, not because
it is a surface convolution.

**Consumers must not assume that ``entorhinal_cortex`` is a classical
gyrus.** It is a **hybrid name** whose cytoarchitectonic identity is
defined by **Brodmann areas 28 and 34**, not by a gyral boundary. The
``HYBRID_NAME`` constant below makes this explicit and greppable.

**The EC is also a cross-partition node.** Its Brodmann constitution
(BA28 and BA34) lives under the **temporal Brodmann partition**, but the
EC itself is a **structural node** under ``gyri/``. Consumers that need
the full EC must query **both** the structural path and the Brodmann
leaves.

Cytoarchitecture: Periallocortical Features
-------------------------------------------
The EC is **periallocortical** — a transitional cortex between the
allocortex of the hippocampal formation and the neocortex of the
parahippocampal gyrus. Its defining cytoarchitectonic features are
**identical to the left twin**:

*   **Lamina dissecans (layer IV)** — a **cell-free zone between the
    supragranular and infragranular layers**. It is the **most
    distinctive feature of the EC** and is absent from neocortex.

*   **Layer II cell islands** — **neatly arranged islands of pyramidal
    and stellate cells** in layer II. These islands are the **main
    cytoarchitectonic characteristic of the EC** and are the **principal
    output neurons** to the hippocampus via the perforant pathway.

*   **Columnar layer III** — layer III presents a **very columnar
    appearance**, with **radial columns of medium pyramids**. The outer
    part of layer III is adjacent to a **cell-free band** that separates
    it from layer II.

*   **Absent or fused layer IV** — in some EC subfields, the lamina
    dissecans is **absent**, and **layers III and V fuse together**.
    This variability is a **hallmark of the periallocortical transition**.

**This periallocortical architecture is the defining structural fact
about the EC.** It is **more primitive than neocortex** but **more
differentiated than allocortex** — a **transitional tissue type** that
supports the EC's **gateway function** between the hippocampal formation
and the neocortex.

Function in the Human Brain
---------------------------
The right EC is a **memory and spatial navigation gateway** with a
**rightward weighting for spatial and sensory-driven processes**. Its
best-supported functions cluster into six domains:

*   **Gateway Between Hippocampus and Neocortex (the defining function,
    bilateral):** The EC is the **origin of the major neural fiber
    system afferent to the hippocampal formation** — the **perforant
    pathway**. It receives **convergent multimodal input**
    from the perirhinal and parahippocampal cortices and from association
    areas, and it relays this information to the hippocampus. It also
    receives **hippocampal output** and projects it **back to the
    neocortex**.

*   **Spatial Encoding (Right-Lateralized — the principal right-EC
    function):** **Spatial encoding is biased to the right hemisphere**
    in both the entorhinal and perirhinal cortices. The
    right EC therefore makes a **larger contribution** to **spatial
    location memory** — where an object or event occurred — than the left
    EC.

*   **Sensory-Driven Processing (Right-Lateralized):** **Right EC
    modulation enhances sensory-driven processing** in path integration
    tasks. This is a **right-lateralized** function
    that complements the left EC's **abstract processing**.

*   **Self-Referential Navigation and Real-Time Spatial Data Integration
    (Right-Lateralized):** The **right EC is preferentially associated
    with self-referential navigation and real-time spatial data
    integration** in prior studies. This is a
    **right-lateralized** function that supports **egocentric spatial
    processing** and **online updating of spatial position**.

*   **Declarative Memory (Episodic and Semantic, bilateral):** The EC is
    a **critical component of the medial temporal lobe declarative
    memory system**. It supports **memory encoding,
    consolidation, and retrieval** via its bidirectional connections with
    the hippocampus and the neocortex.

*   **Grid Cell Spatial Representation and Path Integration (bilateral,
    with right sensory-driven weighting):** The **medial entorhinal
    cortex (MEC)** contains **grid cells** — neurons that fire in a
    **regular hexagonal spatial pattern** and provide the brain with a
    **spatial metric system** for navigation. Grid cells
    encode information about the **current location** and relay it to
    **place cells** in the hippocampus, supporting **path integration**
    and the **cognitive map**. The EC is **critical for path
    integration** — the fundamental cognitive process that
    enables individuals to **navigate by continuously integrating sensory
    information** about their movements and surroundings. On the right,
    this function is **weighted toward sensory-driven and real-time**
    processing.

Associated Disorders
--------------------
Damage to or dysfunction of the right EC is associated with:

*   **Alzheimer's Disease (Earliest Pathology — the signature EC
    syndrome, bilateral):** The EC is the **site of earliest
    histological alterations in AD**, including **neurofibrillary
    tangles and cell death**. **Impaired neuronal activity in the
    EC precedes neurodegeneration**, and **memory impairments and spatial
    navigation deficits at the initial stage of AD** are likely caused by
    **activity dysfunction rather than cell death**. **Weak metabolism in
    the lateral EC (LEC)** is the **earliest sign of dysfunction**.
    This is a **bilaterally devastating** finding.

*   **Temporal Lobe Epilepsy (Seizure Generation and Propagation,
    bilateral):** The EC is a **distinct anatomic and functional region**
    that plays a **role in seizure generation and propagation in
    temporal lobe epilepsy (TLE)**. **Patients with unilateral TLE show
    bilateral reduction in EC volume**, with the **reduction being more
    severe ipsilateral to the epileptic focus**. **Layer II neurons**
    form the major excitatory input into the hippocampus and are
    involved in seizure propagation.

*   **Spatial Memory Impairment (Right-Lateralized):** **Impaired spatial
    location memory** following **right EC damage**, consistent with the
    right-hemisphere bias for spatial encoding.

*   **Sensory-Driven Path Integration Deficits (Right-Lateralized):**
    **Impaired sensory-driven path integration** following **right EC
    damage**, consistent with the right EC's role in **sensory-driven
    processing**.

*   **Memory Impairment and Spatial Navigation Deficits (bilateral):**
    **Deficits of memory and spatial navigation** related to **EC
    dysfunction** are being elucidated, with **path integration deficits**
    having potential as **early behavioral biomarkers** for AD detection.

**What is NOT here:** **Verbal learning deficits** and **abstract
processing deficits** are **left EC** functions. They are **absent** from
right EC lesions. They are documented in the left EC module and are
**explicitly not claimed here**. The right EC is the **spatial/sensory**
pole; the left EC is the **object/abstract** pole.

Lateralization Notes
--------------------
This is the **right** EC module. The lateralization landscape is
**asymmetric-by-function with left-object/right-spatial specialization**
— a **process-specific division of labor** within the medial temporal
memory system:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Spatial encoding** — spatial location memory is **biased to the
      right hemisphere**.
    - **Sensory-driven processing** — right EC modulation enhances
      **sensory-driven processing** in path integration tasks.
    - **Self-referential navigation** — the right EC is preferentially
      associated with **self-referential navigation**.
    - **Real-time spatial data integration** — the right EC is
      preferentially associated with **real-time spatial data
      integration**.

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Object encoding** — object identity memory is **biased to the
      left hemisphere**.
    - **Abstract processing** — left EC modulation enhances **abstract
      processing** in path integration tasks.
    - **Verbal learning** — the left EC is more involved in **verbal
      learning**.
    - **Grid-like spatial coding** — the left EC shows **grid-like
      spatial coding** in some studies.

*   **Symmetric Functions (bilateral properties of the EC, copied verbatim
    from the left twin):**
    - Gateway between hippocampus and neocortex (perforant pathway).
    - Declarative memory (episodic and semantic).
    - Grid cell spatial representation and path integration.
    - Alzheimer's disease vulnerability (earliest pathology).

**This is the "asymmetric-by-function" pattern** — a division of
cognitive labor, not a denial-based lateralization. The left EC does
**object/abstract** work; the right EC does **spatial/sensory** work.
Neither hemisphere is the "dominant" one; they are **different
functional fields** that share the same cytoarchitectonic territory.

**A consumer that assumes "right EC = left EC" will miss the
right-spatial and right-sensory-driven weightings** — but the two
hemispheres are **not interchangeable** for memory encoding. They are
**specialized for different memory processes** within the same gateway
structure.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    hippocampus or the neocortex. Those are **downstream/upstream
    targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Hybrid-name status — flagged in prose and data.** The EC is **not a
    classical gyrus**. It is a **periallocortical region** wired under
    ``gyri/`` as a **structurally addressable memory unit**. The
    ``HYBRID_NAME`` constant makes this explicit.
*   **Periallocortical type — flagged in data.** The EC is
    **periallocortical**, not neocortical or allocortical. The
    ``CYTOARCHITECTONIC_TYPE`` constant is **"periallocortical"**.
*   **Brodmann constitution — flagged in data.** The EC is constituted by
    **BA28 and BA34**, both in the **temporal Brodmann partition**. The
    ``REGION_TO_BRODMANN`` constant documents the mapping.
*   **Asymmetric-by-function — flagged in data.** The right EC carries
    **spatial/sensory** functions; the left EC carries **object/abstract**
    functions. The ``RIGHT_LATERALIZED`` constant documents the
    right-lateralized functions; the ``DENIED_LEFT_LATERALIZED`` constant
    documents the left-lateralized functions that are **not claimed**
    here.
*   **Structural parity with left EC.** Left and right EC modules are
    **structurally identical** in their cytoarchitectonic constants and
    Brodmann constitution; only the **lateralization prose** differs
    (spatial/sensory vs. object/abstract).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri import entorhinal_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.gyri.entorhinal_cortex"
    )

**The EC is a hybrid-name "gyrus" — not a classical convolution.** Use the
`HYBRID_NAME` constant to check::

    from ...temporal.gyri.entorhinal_cortex import HYBRID_NAME
    # HYBRID_NAME = True

For the Brodmann constitution::

    from ...temporal.gyri.entorhinal_cortex import REGION_TO_BRODMANN
    # REGION_TO_BRODMANN["entorhinal_cortex"] = (
    #     "brodmann_area_28", "brodmann_area_34"
    # )

For the right-lateralized functions::

    from ...temporal.gyri.entorhinal_cortex import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("spatial_encoding",
    #                      "sensory_driven_processing",
    #                      "self_referential_navigation",
    #                      "real_time_spatial_data_integration")

For the left-lateralized functions explicitly denied here::

    from ...temporal.gyri.entorhinal_cortex import DENIED_LEFT_LATERALIZED
    # DENIED_LEFT_LATERALIZED = ("object_encoding",
    #                            "abstract_processing",
    #                            "verbal_learning")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ec_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.entorhinal_cortex"
        )
        # resolve ec_path through the memory/recall layer

References
----------
*   **EC anatomy and gateway function:** *Parahippocampal Gyrus — Chapters
    and Articles* (ScienceDirect). The EC (**Brodmann's areas 28 and
    34**) is located in the **anterior and medial portion of the temporal
    lobe (medial to the rhinal fissure)** and **serves as the principal
    source of input into the hippocampus, via the perforant path**.
*   **EC MeSH descriptor:** *Entorhinal Cortex MeSH Descriptor Data*.
    Cerebral cortex region on the **medial aspect of the parahippocampal
    gyrus**, **immediately caudal to the olfactory cortex of the uncus**;
    the EC is the **origin of the major neural fiber system afferent to
    the hippocampal formation** (perforant pathway).
*   **EC lateralization — path integration:** *Distinctive roles of left
    and right entorhinal cortex in path integration via a non-invasive
    stimulation study* (2025), *Nat Commun*, 16, 10214. **Left EC
    modulation enhanced abstract processing**; **right EC modulation
    enhanced sensory-driven processing**; prior studies report **left EC
    involvement in object encoding, verbal learning, and grid-like
    spatial coding**, and **right EC involvement in spatial encoding,
    self-referential navigation, and real-time spatial data
    integration**.
*   **EC lateralization — object vs. spatial encoding:** Bellgowan, P.S.,
    et al. (2009). "Lateralized spatial and object memory encoding in
    entorhinal and perirhinal cortices." *Learn Mem*, 16(7), 433–438.
    PMC2704107. **Object encoding is biased to the left hemisphere,
    whereas spatial encoding is biased to the right**; this process-
    specific distinction is expressed as a **hemispheric division of
    labor**.
*   **EC and Alzheimer's disease:** *Entorhinal cortex dysfunction in
    Alzheimer's disease* (2023), *Trends Neurosci*, 46(2), 124–136.
    The EC is the **brain region that often exhibits the earliest
    histological alterations in AD**, including **neurofibrillary
    tangles and cell death**; **impaired neuronal activity precedes
    neurodegeneration**; **layer 2 neurons** are a candidate neuron type
    causing EC dysfunction.
*   **EC and grid cells:** *Parahippocampal Place Area* (ScienceDirect).
    The EC **contains grid cells** (Hafting et al., 2005); grid cells
    **encode information about the current location** and relay it to
    **place cells in the hippocampus**; grid cells facilitate **path
    integration**.
*   **EC cytoarchitecture — lamina dissecans and cell islands:** *The
    Human Periallocortex: Layer Pattern in Presubiculum, Parasubiculum
    and Entorhinal Cortex* (2017), PMC5632821. **Layer II is made up of
    neat cell islands**; **layer IV, lamina dissecans, is absent** in
    some subfields so that **layers III and V fuse together**; the EC is
    **periallocortical**.
*   **EC and temporal lobe epilepsy:** *Entorhinal cortex in temporal
    lobe epilepsy* (1999), *Neurology*, 52(9), 1870. The EC is a
    **distinct anatomic and functional region** of the anterior
    parahippocampal gyrus that plays a role in **seizure generation and
    propagation in TLE**; **patients with unilateral TLE show bilateral
    reduction in EC volume**, with the reduction being **more severe
    ipsilateral to the epileptic focus**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial temporal and hippocampal-formation anatomy.)
*   NeuroNames — Entorhinal cortex (right); FMA — right entorhinal cortex
    partonomy.
"""