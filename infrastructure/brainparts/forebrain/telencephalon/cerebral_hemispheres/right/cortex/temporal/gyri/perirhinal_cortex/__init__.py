"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri.perirhinal_cortex
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
                        └── perirhinal_cortex   <-- THIS MODULE

**Primary synonym:** Perirhinal cortex (PRC), right; Right PRC; Area
perirhinalis; Brodmann areas 35 and 36; Transentorhinal cortex (BA35's
older name, Braak's term).
**Organizing principle:** **Hybrid structural-functional node** — the
perirhinal cortex is **not a classical gyral convolution**. It is a
**cytoarchitectonically defined periallocortical/proisocortical region**
that sits **within the medial aspect of the parahippocampal gyrus** and
is wired under ``gyri/`` as a **structurally addressable memory unit**.
See "Hybrid-Name Status" below.
**Brodmann constitution:** **BA35** (medial perirhinal) and **BA36**
(lateral perirhinal / ectorhinal). BA35 is **periallocortical** (agranular
35a / dysgranular 35b); BA36 is **proisocortical to isocortical**
(dysgranular to granular, with a rudimentary layer IV).
**Location:** The **medial aspect of the parahippocampal gyrus** and the
**fundus and medial bank of the rhinal sulcus** in the right temporal
lobe, **immediately lateral to the entorhinal cortex (BA28/BA34)** and
**medial to the fusiform gyrus / inferior temporal gyrus**.
**Structural parent:** Child of ``.../temporal/gyri`` (the structural
partition of the temporal lobe).
**Cytoarchitectonic type:** **Periallocortical (BA35) and proisocortical
(BA36)** — a transitional cortex between the allocortex of the entorhinal
region and the neocortex of the inferior temporal / fusiform gyri.

Overview
--------
The **right perirhinal cortex (PRC)** is the **principal cortical
substrate for object recognition memory and familiarity discrimination**
in the right hemisphere, with a **rightward weighting for spatial-
context memory, contextual recall, and discriminative familiarity**.
It sits at the **interface between the neocortical sensory association
areas and the entorhinal-hippocampal memory system**, receiving **highly
processed multimodal sensory information** from unimodal and polymodal
association cortices and relaying it to the entorhinal cortex (and
thence to the hippocampus) for **memory consolidation and retrieval**.
It is the **immediate neighbor** of the entorhinal cortex on the medial
temporal surface, and together with the EC and the parahippocampal gyrus
it forms the **medial temporal lobe memory system**.

**This is the right-hemisphere twin of the left PRC, and the pair
instantiates the "asymmetric-by-function" pattern at the structural
level** — a **process-specific division of labor** within the medial
temporal memory system:

*   **The left PRC is the left-lateralized pole** for **object
    recognition memory** (object-identity memory) and **object mnemonic
    discrimination**. It carries the **left-hemisphere weighting** for
    verbal and object-identity memory.

*   **The right PRC is the right-lateralized pole** for **spatial-
    context memory**, **contextual recall**, and **discriminative
    familiarity**. It carries the **right-hemisphere weighting** for
    spatial and contextual memory. **Right BA36** specifically
    contributes to **familiarity in the discriminative condition**, an
    association that appeared **marginally stronger on the right than on
    the left**.

**The PRC is the second hybrid-name "gyrus" documented in this tree**,
following the **entorhinal cortex**. Like the EC, it is **not a classical
surface convolution** — it is a **cytoarchitectonically defined
periallocortical/proisocortical region** that sits **within the medial
aspect of the parahippocampal gyrus**. Its presence under ``gyri/``
reflects the tree's choice to treat it as a **structurally addressable
memory unit**, not as a surface convolution. **Consumers must not assume
that ``perirhinal_cortex`` is a gyrus in the same sense as
``superior_temporal_gyrus``** — it is a **hybrid name**, and its
cytoarchitectonic identity is defined by **Brodmann areas 35 and 36**,
not by a gyral boundary.

**The PRC is the gyral partner of the EC within the parahippocampal
gyrus.** The PHG (``.../temporal/gyri/parahippocampal_gyrus``) is the
**structural parent** of both the EC and the PRC. The **EC** is the
**medial** component (BA28, BA34); the **PRC** is the **lateral**
component (BA35, BA36). Together they form the **hippocampal-neocortical
gateway** that supports **declarative memory**.

**The PRC is the cortical seat of the earliest Alzheimer's disease
pathology after the EC — and on the right side this is equally true.**
BA35 (the transentorhinal region) is among the **earliest brain regions
to show tau accumulation** — the **Braak staging** of Alzheimer's
disease begins with the **transentorhinal region** (BA35) and
**proceeds to the EC (BA28/BA34) and then to the hippocampus**. This
clinical fact makes the PRC one of the **highest-value modules in the
entire brainparts tree**, and it is **bilaterally devastating**.

Hybrid-Name Status
------------------
The PRC is **not a gyral convolution**. It is a **periallocortical/
proisocortical region** that is **co-extensive with the medial aspect of
the parahippocampal gyrus** and is **reachable via the ``gyri/``
partition** as a **structurally addressable memory unit**. This is the
**second hybrid-name "gyrus" in the tree** (after the EC) — a
**cytoarchitectonically defined region** that is presented as a "gyrus"
for **structural addressability**, not because it is a surface
convolution.

**Consumers must not assume that ``perirhinal_cortex`` is a classical
gyrus.** It is a **hybrid name** whose cytoarchitectonic identity is
defined by **Brodmann areas 35 and 36**, not by a gyral boundary. The
``HYBRID_NAME`` constant below makes this explicit and greppable.

**The PRC is also a cross-partition node.** Its Brodmann constitution
(BA35 and BA36) lives under the **temporal Brodmann partition**, but the
PRC itself is a **structural node** under ``gyri/``. Consumers that need
the full PRC must query **both** the structural path and the Brodmann
leaves.

Cytoarchitecture: Periallocortical (BA35) and Proisocortical (BA36)
-------------------------------------------------------------------
The PRC contains **two cytoarchitectonically distinct areas** that span
the **transitional range** from periallocortex to proisocortex. The
cytoarchitecture is **identical to the left twin**:

*   **BA35 (medial perirhinal / transentorhinal)** — **periallocortical**.
    **BA35a** is **agranular** (layer IV absent); **BA35b** is
    **dysgranular** (layer IV sparse). Contains **large heart-shaped
    pyramidal cells in deep layer V**. BA35 is the **earliest site of
    tau pathology in Alzheimer's disease** (the "transentorhinal
    region" in Braak staging).

*   **BA36 (lateral perirhinal / ectorhinal)** — **proisocortical to
    isocortical**. Has a **rudimentary but present granular layer IV**.
    Contains **all the components that quintessentially define isocortex
    proper** — a **thick layer I**, a **granular layer IV**, and
    **pyramidal neurons in layers III and V** — but is **less laminated
    than true neocortex**. BA36 is the **larger, laterally situated
    division** of the PRC and is the **critical substrate for object
    recognition memory** in macaques.

**This periallocortical-to-proisocortical gradient is the defining
structural fact about the PRC.** The PRC spans the **transition** from
the allocortical entorhinal cortex (medially) to the neocortical
inferior temporal / fusiform gyri (laterally), with **BA35
(periallocortical)** as the **medial pole** and **BA36
(proisocortical)** as the **lateral pole**.

Function in the Human Brain
---------------------------
The right PRC is an **object-recognition and familiarity hub** with a
**rightward weighting for spatial-context and discriminative familiarity**.
Its best-supported functions cluster into six domains — **four symmetric
with the left twin and two right-lateralized emphases**:

*   **Spatial-Context Memory (Right-Lateralized — the principal right-PRC
    function):** The right PRC supports **spatial-context memory** —
    memory for the **spatial, temporal, and situational context** in
    which an object or event was encountered. This function is
    **right-weighted** in most individuals, consistent with the
    **right-hemisphere bias for spatial encoding** in the perirhinal and
    entorhinal cortices.

*   **Discriminative Familiarity (Right-Lateralized):** **Right BA36
    specifically contributes to familiarity in the discriminative
    condition** — the ability to judge whether a stimulus has been
    encountered before **under conditions that require discriminating
    it from similar lures**. This association appeared **marginally
    stronger on the right than on the left**.

*   **Object Recognition Memory (the defining function, bilateral):** The
    PRC is **critical for recognition memory** — the ability to judge
    that a stimulus has been encountered before. The **critical
    substrate for object recognition memory is located in the
    anteromedial perirhinal cortex** (BA35 and the medial portion of
    BA36); blocking glutamatergic transmission in BA35 **significantly
    impairs object recognition memory**.

*   **Familiarity Evaluation (Bilateral):** The PRC supports
    **familiarity evaluation** — the ability to judge whether a stimulus
    has been encountered before, **independent of the retrieval of
    contextual details**. The evidence is **clearest for familiarity
    discrimination for single items**. The **familiarity mechanism
    itself** is bilateral; only the **discriminative-condition
    contribution** is marginally right-weighted.

*   **Connection Between Perception and Memory (Bilateral):** The PRC
    sits at the **interface between perceptual representation and
    mnemonic association**, supporting **visual-mnemonic integration**
    — the transformation of a perceptual representation into a mnemonic
    one.

*   **Mnemonic Discrimination (Pattern Separation for Objects,
    Bilateral):** The PRC (together with the anterior-lateral entorhinal
    cortex) has been implicated in **mnemonic discrimination of objects
    rather than scenes** — the ability to distinguish similar objects in
    memory.

Associated Disorders
--------------------
Damage to or dysfunction of the right PRC is associated with:

*   **Spatial-Context Memory Impairment (Right-Lateralized):** Impaired
    **spatial-context memory** following **right PRC damage**, consistent
    with the right-hemisphere weighting for spatial encoding.

*   **Impaired Discriminative Familiarity (Right-Lateralized):** Reduced
    **familiarity in the discriminative condition** following **right
    BA36 damage**, consistent with the right BA36's marginally stronger
    contribution to this function.

*   **Object Recognition Memory Disorders (Bilateral, with Right-Spatial
    Emphasis):** Impaired **object recognition memory** and **familiarity
    evaluation**, consistent with the PRC's defining role. The
    **right PRC contributes more to spatial-context** aspects of object
    memory.

*   **Alzheimer's Disease (Earliest Pathology — Bilateral):**
    **Neurofibrillary tangle pathology in Alzheimer's disease is first
    observed in Brodmann Area 35 (BA35)** — the medial portion of the
    PRC, known as the **transentorhinal region**. The **Braak staging**
    of Alzheimer's disease begins with **BA35** and proceeds to **the EC
    and hippocampus**. This is **equally true on the right side**.
    **Right BA36 volume also correlates with memory performance in
    MCI**.

*   **Mild Cognitive Impairment (MCI):** PRC atrophy and dysfunction are
    associated with **memory impairment in MCI**, and tasks sensitive to
    PRC atrophy (especially spatial-context memory and discriminative
    familiarity) may help identify early cognitive decline.

*   **Impaired Object Mnemonic Discrimination:** Reduced ability to
    distinguish similar objects in memory, consistent with the PRC's
    role in object pattern separation.

*   **Findings Reported in Schizophrenia and Depression:** The PRC has
    been implicated in schizophrenia (reduced volume) and in depression
    (reduced perirhinal volume in depressed older adults), though these
    are **findings reported** rather than established syndrome
    attributions.

**What is NOT here:** **Verbal object-identity memory deficits** and
**left-lateralized object mnemonic discrimination** are **left PRC**
functions. They are **absent** from right PRC lesions. They are
documented in the left PRC module and are **explicitly not claimed
here**. **Wernicke's aphasia** (BA22), **pure alexia** (left VWFA,
fusiform gyrus), and **prosopagnosia** (right FFA, fusiform gyrus) are
**not** PRC syndromes. The PRC is an **object-recognition and
familiarity hub**, not a language or visual-recognition area.

Lateralization Notes
--------------------
This is the **right** PRC module. The lateralization landscape is
**asymmetric-by-function with left-object/right-spatial specialization**
— a **process-specific division of labor** within the medial temporal
memory system:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Spatial-context memory** — right-weighted.
    - **Contextual recall** — right-weighted.
    - **Discriminative familiarity** — **right BA36** specifically
      contributes to familiarity in the discriminative condition.

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Object-identity memory** — left PRC damage preferentially
      impairs object-identity memory.
    - **Object mnemonic discrimination** — left-weighted.
    - **Semantic memory and conceptual object processing** — left-
      weighted for verbal/object-identity material.

*   **Symmetric Functions (bilateral properties of the PRC, copied
    verbatim from the left twin):**
    - **Familiarity evaluation** — core bilateral function.
    - **Visual-mnemonic integration** — bilateral.
    - **Mnemonic discrimination (core)** — bilateral.
    - **Alzheimer's disease vulnerability (earliest pathology)** —
      bilateral, with **BA35 as the Braak stage I site**.

**This is the "asymmetric-by-function" pattern at the structural level**
— the gyral leaf mirrors the EC's division of labor. The left PRC does
**object-identity and verbal-semantic** work; the right PRC does
**spatial-context and discriminative-familiarity** work. Neither
hemisphere is the "dominant" one; they are **different functional
fields** that share the same structural convolution.

**A consumer that assumes "right PRC = left PRC" will miss the
right-lateralized spatial-context and discriminative-familiarity
weightings** — but the right twin is not merely "denying" the left's
object-memory functions; it is **carrying different functions**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    hippocampus or the neocortex. Those are **downstream/upstream
    targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Hybrid-name status — flagged in prose and data.** The PRC is **not
    a classical gyrus**. It is a **periallocortical/proisocortical
    region** wired under ``gyri/`` as a **structurally addressable
    memory unit**. The ``HYBRID_NAME`` constant makes this explicit.
*   **Periallocortical (BA35) + proisocortical (BA36) type — flagged in
    data.** The PRC spans a **transitional gradient** from
    periallocortex (BA35) to proisocortex (BA36). The
    ``CYTOARCHITECTONIC_TYPE`` constant documents this as
    **"periallocortical_proisocortical"**.
*   **Brodmann constitution — flagged in data.** The PRC is constituted
    by **BA35 and BA36**, both in the **temporal Brodmann partition**.
    The ``REGION_TO_BRODMANN`` constant documents the mapping.
*   **Asymmetric-by-function — flagged in data.** The right PRC carries
    **spatial-context and discriminative-familiarity** functions; the
    left PRC carries **object-identity** functions. The
    ``RIGHT_LATERALIZED`` constant documents the right-lateralized
    functions; the ``DENIED_LEFT_LATERALIZED`` constant documents the
    left-lateralized functions that are **not claimed** here.
*   **AD vulnerability — flagged in data.** BA35 is the **earliest site
    of tau pathology** in Alzheimer's disease (Braak staging begins with
    BA35). The ``EARLIEST_AD_PATHOLOGY`` constant documents this.
*   **Structural parity with left PRC.** Left and right PRC modules are
    **structurally identical** in their cytoarchitectonic constants and
    Brodmann constitution; only the **lateralization prose** differs
    (spatial vs. object).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri import perirhinal_cortex

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.gyri.perirhinal_cortex"
    )

**The PRC is a hybrid-name "gyrus" — not a classical convolution.** Use
the `HYBRID_NAME` constant to check::

    from ...temporal.gyri.perirhinal_cortex import HYBRID_NAME
    # HYBRID_NAME = True

For the Brodmann constitution::

    from ...temporal.gyri.perirhinal_cortex import REGION_TO_BRODMANN
    # REGION_TO_BRODMANN["perirhinal_cortex"] = (
    #     "brodmann_area_35", "brodmann_area_36"
    # )

For the earliest AD pathology::

    from ...temporal.gyri.perirhinal_cortex import EARLIEST_AD_PATHOLOGY
    # EARLIEST_AD_PATHOLOGY = "brodmann_area_35 (transentorhinal region)"

For the right-lateralized functions::

    from ...temporal.gyri.perirhinal_cortex import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("spatial_context_memory",
    #                      "contextual_recall",
    #                      "familiarity_discriminative_condition")

For the left-lateralized functions explicitly denied here::

    from ...temporal.gyri.perirhinal_cortex import DENIED_LEFT_LATERALIZED
    # DENIED_LEFT_LATERALIZED = ("object_identity_memory",
    #                            "object_mnemonic_discrimination",
    #                            "semantic_memory_conceptual_object_processing")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        prc_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.perirhinal_cortex"
        )
        # resolve prc_path through the memory/recall layer

References
----------
*   **PRC anatomy and gateway function:** *Parahippocampal Gyrus — Chapters
    and Articles* (ScienceDirect). The PRC (**Brodmann areas 35 and 36**)
    is located in the **medial temporal lobe** and **serves as an
    interface between the neocortex and the hippocampus**.
*   **PRC MeSH descriptor:** *Perirhinal Cortex MeSH Descriptor Data*.
    Cerebral cortex region on the **medial aspect of the temporal lobe**
    in the **fundus and medial bank of the rhinal sulcus**, **caudal to
    the olfactory cortex** and **medial to the ectorhinal area (BA36)**.
*   **PRC cytoarchitecture — BA35 agranular/dysgranular, BA36
    dysgranular-to-granular:** *Predicting the Location of Human
    Perirhinal Cortex, Brodmann's area 35, from MRI* (2012),
    *PMC3508349*. **BA35a is agranular periallocortex** (layer IV
    absent); **BA35b is dysgranular proisocortex** (sparse layer IV);
    **BA36 has a compact granular layer IV** and is true isocortex.
*   **PRC as critical substrate for object recognition memory:**
    *Blockade of Glutamatergic Transmission in Perirhinal Cortex Impairs
    Object Recognition Memory in Macaques* (2015), *J Neurosci*.
    The **critical substrate for object recognition memory is located in
    the anteromedial perirhinal cortex — Area 35 and the medial portion
    of Area 36**; blocking glutamate transmission in BA35 significantly
    impaired object recognition memory.
*   **PRC functions:** *Perirhinal Cortex — an overview* (ScienceDirect).
    The PRC plays a central role in **recognition memory** (clearest for
    **familiarity discrimination for single items**) and in **perceptual
    functions**; it receives highly processed sensory information and
    provides a route to and from the hippocampus.
*   **PRC and Alzheimer's disease — BA35 as earliest site:** *In
    Alzheimer's disease, neurofibrillary tangle pathology is first
    observed in Brodmann Area 35 (BA35)* — the **transentorhinal
    region** (Braak's term). **Braak staging** begins with **BA35** and
    proceeds to the EC and hippocampus. **Selective atrophy in BA35**
    is associated with early cognitive changes in prodromal AD.
*   **PRC and mnemonic discrimination:** *Mnemonic discrimination, the
    ability to distinguish similar events in memory* (DZNE). The
    **perirhinal-transentorhinal region (area 35)** has been implicated
    in the **mnemonic discrimination of objects rather than scenes**.
*   **Lateralized memory encoding:** Bellgowan, P.S., Buffalo, E.A.,
    Bodurka, J., & Martin, A. (2005). "Lateralized spatial and object
    memory encoding in entorhinal and perirhinal cortices." *Learn Mem*,
    12(3), 343–351. PMC2704107. **Object encoding is biased to the left
    hemisphere, whereas spatial encoding is biased to the right**; this
    process-specific distinction is expressed as a **hemispheric division
    of labor** in both the perirhinal and entorhinal cortices.
*   **Right BA36 and discriminative familiarity:** Besson, G., et al.
    (2020). "Familiarity for entities as a sensitive marker of
    antero-lateral entorhinal atrophy in amnestic mild cognitive
    impairment." *Cortex*. **Right BA36 specifically contributed to
    familiarity in the discriminative condition**, an association that
    appeared **marginally stronger than with familiarity for entities**.
*   **PRC and schizophrenia / depression:** *Hippocampal and
    parahippocampal abnormalities in schizophrenia* (2007),
    *Arch Gen Psychiatry*; *Depressed older individuals have smaller
    perirhinal volumes* (2015). These are **findings reported** rather
    than established syndrome attributions.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial temporal and perirhinal anatomy.)
*   NeuroNames — Perirhinal cortex (right); FMA — right perirhinal cortex
    partonomy.
"""