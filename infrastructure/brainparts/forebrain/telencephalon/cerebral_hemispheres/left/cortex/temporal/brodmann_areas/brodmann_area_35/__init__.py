"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.brodmann_areas.brodmann_area_35
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
                        └── brodmann_area_35   <-- THIS MODULE

**Primary synonym:** Brodmann Area 35 (BA35); **Perirhinal cortex (PRC),
medial division**; **Transentorhinal cortex** (Braak's term).
**Cytoarchitectonic designation:** Area 35 of Brodmann (1909). The
perirhinal cortex comprises **BA35 and BA36**; BA35 is the **medial
component**, situated in the **fundus and medial bank of the rhinal
sulcus**.
**Part of:** The **perirhinal cortex** — the object-recognition and
familiarity hub of the medial temporal lobe memory system.
**Location:** The **medial aspect of the anterior parahippocampal
gyrus**, in the **depth and medial bank of the rhinal (collateral)
sulcus**, immediately lateral to the entorhinal cortex (BA28/BA34) and
medial to the ectorhinal cortex (BA36).
**Structural parent:** This is a **Brodmann leaf**, not a gyral child. It
lives directly under the left temporal Brodmann aggregator.
**Cytoarchitectonic type:** **Periallocortical / proisocortical** — BA35
is a **transitional cortex** between the allocortex of the entorhinal
region and the isocortex of BA36.

Overview
--------
Brodmann Area 35 (BA35) is the **medial division of the perirhinal
cortex** — the **principal cortical substrate for object recognition
memory and familiarity discrimination** in the human brain. It sits at
the **interface between the entorhinal-hippocampal memory system and the
neocortical sensory association areas**, receiving **highly processed
multimodal sensory information** and relaying it to the hippocampus via
the entorhinal cortex[reference:0]. Its position at the **top of the
sensory processing hierarchy and at the gateway to the limbic system**
makes it ideally placed to support **the transformation of perceptual
representations into mnemonic ones**[reference:1].

**BA35 is the fourth allocortical / transitional leaf documented in this
tree**, following BA27 (presubiculum), BA28 (entorhinal cortex), and BA34
(dorsal entorhinal cortex). The temporal Brodmann aggregator flagged
BA27, BA28, BA34, and BA35 as **allocortical or transitional fields**
(via the `CYTOARCHITECTONIC_TYPE` constant). BA35 is **not fully
neocortical** — it is **agranular (35a) or dysgranular (35b)**, lacking a
proper layer IV[reference:2]. Consumers that assume all Brodmann areas are
neocortical will be **wrong for BA35**.

**BA35 is the perirhinal cortex, and it is NOT the entorhinal cortex.**
The entorhinal cortex is **BA28 and BA34**; the perirhinal cortex is
**BA35 and BA36**. BA35 is the **medial** component of the perirhinal
cortex, adjacent to the entorhinal cortex, and its **principal function
is object recognition and familiarity**, not spatial navigation or grid-
cell coding (which are entorhinal functions).

Periallocortical / Proisocortical Cytoarchitecture
--------------------------------------------------
BA35 is a **transitional cortex** with a **dual lamination pattern**
that distinguishes it from both the allocortex of the entorhinal region
and the isocortex of BA36[reference:3]:

*   **BA35a — agranular periallocortex** — **layer IV is absent**; a
    "placeholder" layer occurs spatially but **with no cells present**
    [reference:4]. BA35a shares the **modular organization** (clustering
    of neurons in layers II–III, forming "perirhinal columns") that is a
    classic attribute of periallocortex[reference:5].

*   **BA35b — dysgranular proisocortex** — **layer IV has a few cells
    but is not completely organized**[reference:6]. **Layer V** is more
    organized and uniform than in BA35a, beginning to resemble the
    internal pyramidal layer of isocortex but is **not as thick**
    [reference:7].

*   **Signature feature: large heart-shaped cells in deep layer V** —
    present in **both BA35 and BA36**, these are a hallmark of perirhinal
    cortex in rodents and primates[reference:8].

*   **Broad layer I** — a distinguishing feature of BA35 relative to
    adjacent areas[reference:9].

**The agranular/dysgranular lamination of BA35 is the defining structural
fact.** Unlike BA36, which has a **compact and granular layer IV** and is
therefore **true isocortex**, BA35 is **periallocortex and proisocortex**
— a **transitional tissue type**[reference:10]. A consumer that applies
neocortical computational assumptions (columnar organization, four-layer
canonical microcircuit) to BA35 will be **wrong**.

Function in the Human Brain
---------------------------
The left BA35 is an **object-recognition and familiarity hub**. Its
best-supported functions cluster into six domains:

*   **Object Recognition Memory (the defining function):** BA35 is
    **critically involved in recognition memory for objects**
    [reference:11]. In macaques, the **critical substrate for object
    recognition memory is located in the anteromedial perirhinal cortex,
    specifically Area 35 and the medial portion of Area 36**; only
    infusions aimed at this site impaired performance[reference:12]. Blocking
    glutamatergic transmission in BA35 **significantly impairs object
    recognition memory**[reference:13].

*   **Familiarity Discrimination:** BA35 supports **familiarity
    evaluation** — the ability to judge whether a stimulus has been
    encountered before, independent of the retrieval of contextual
    details[reference:14][reference:15]. The evidence is **clearest for
    familiarity discrimination for single items**[reference:16].

*   **Connection Between Perception and Memory:** BA35 sits at the
    **interface between perceptual representation and mnemonic
    association**, supporting **visual-mnemonic integration** — the
    transformation of a perceptual representation into a mnemonic one
    [reference:17][reference:18].

*   **Processing of Complex Visual Configurations:** BA35 represents
    **complex object-level feature configurations** and participates in
    **the discrimination of novel versus familiar configurations**
    .

*   **Semantic Memory and Conceptual Object Processing:** BA35 is
    involved in **semantic memory** and **conceptual object processing**
    [reference:20]. The importance of the perirhinal cortex for semantic memory
    may explain **early impairments of semantics in preclinical
    Alzheimer's disease**[reference:21].

*   **Mnemonic Discrimination (Pattern Separation for Objects):** BA35
    (together with the anterior-lateral entorhinal cortex) has been
    implicated in **mnemonic discrimination of objects rather than
    scenes** — the ability to distinguish similar objects in memory
    [reference:22].

Associated Disorders
--------------------
Damage to or dysfunction of the left BA35 is associated with:

*   **Recognition Memory Disorders:** Impaired **object recognition
    memory** and **familiarity evaluation**, consistent with BA35's
    defining role[reference:23].

*   **Alzheimer's Disease (Earliest Pathology):** **Neurofibrillary
    tangle pathology in Alzheimer's disease is first observed in
    Brodmann Area 35 (BA35)** — the medial portion of the perirhinal
    cortex[reference:24]. BA35 is also referred to as the
    **transentorhinal region** (Braak's term) and is among the **earliest
    brain regions to show tau accumulation**[reference:25]. **Selective
    atrophy in BA35** is associated with early cognitive changes in
    prodromal AD[reference:26].

*   **Mild Cognitive Impairment (MCI):** BA35 atrophy and dysfunction are
    associated with **memory impairment in MCI**, and tasks sensitive to
    BA35 atrophy may help identify early cognitive decline
    [reference:27].

*   **Impaired Object Mnemonic Discrimination:** Reduced ability to
    distinguish similar objects in memory, consistent with BA35's role
    in object pattern separation[reference:28].

*   **Findings Reported in Schizophrenia:** The perirhinal cortex (BA35
    and BA36) has been assessed in schizophrenia, though this is a
    **finding reported** rather than an established syndrome attribution
    [reference:29].

**No named "BA35 lesion syndrome" exists.** BA35 is discussed as a
**component of the perirhinal memory system**, not as a standalone
clinical node. Its clinical relevance is as a **contributor** to object
recognition, familiarity, semantic memory, and **the earliest stages of
Alzheimer's disease pathology**.

**What is NOT here:** **Wernicke's aphasia** (BA22), **semantic dementia**
(left anterior temporal), **pure alexia** (left VWFA, BA37), and
**prosopagnosia** (right FFA, BA37) are **not** BA35 syndromes. BA35 is
an **object-recognition memory hub**, not a language or face-recognition
area. **Spatial memory and navigation** are **entorhinal (BA28/BA34)**
and **hippocampal** functions, not BA35 functions.

Lateralization Notes
--------------------
This is the **left** BA35 module. The lateralization of BA35 is **weakly
established** — the area is part of the **bilateral perirhinal memory
system**, and no strong left-right functional asymmetry has been
demonstrated for its core object-recognition functions:

*   **No Established Lateralized Syndrome:** Unlike BA22 (left Wernicke's
    / right prosodic) or BA37 (left VWFA / right FFA), BA35 has **no
    documented left-lateralized or right-lateralized function** for its
    core object-recognition and familiarity functions.

*   **Weak Left-Object / Right-Spatial Bias (Inherited from MTL):** The
    medial temporal lobe shows a **functional bias** — **object encoding
    is biased to the left hemisphere, whereas spatial encoding is biased
    to the right**. This bias applies to the perirhinal
    cortex (BA35/BA36) and gives the **left BA35 a slight advantage for
    object memory**, but it is a **weighting**, not a **dominance**.

*   **Bilateral Activation in Object Memory Tasks:** BOLD responses
    during object-recognition tasks reveal **significant activation in
    bilateral BA35**, indicating that both hemispheres contribute to the
    function.

*   **Symmetric Functions (presumed bilateral, copied verbatim to the
    right twin):** Object recognition memory, familiarity discrimination,
    visual-mnemonic integration, complex visual configuration processing,
    semantic memory, and mnemonic discrimination are **presumed bilateral**
    for the perirhinal cortex.

**A consumer that assumes "left BA35 = right BA35" will be approximately
correct** — not because BA35 is perfectly symmetric, but because **no
strong lateralization has been demonstrated** for its core functions
beyond the weak left-object / right-spatial bias inherited from the
broader medial temporal lobe. This is the **"symmetric-by-bilateral-
organization"** pattern — the same pattern as BA27, BA28, and BA34, and
distinct from the **"symmetric-by-default"** pattern of BA15.

**The only lateralized function attributable to BA35 is the left-object
bias**, which is inherited from the broader medial temporal lobe rather
than being a BA35-specific asymmetry. The **familiarity function** and the
**object-recognition function** are bilateral.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    hippocampus, the entorhinal cortex, or the amygdala. Those are
    **downstream/upstream targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Periallocortical / proisocortical leaf — flagged in prose and
    data.** BA35 is **not fully neocortical** — it is **agranular (35a)
    or dysgranular (35b)**. The `CYTOARCHITECTONIC_TYPE` constant is
    **"periallocortical_transitional"** (per the temporal Brodmann
    aggregator's type map). Consumers must not apply neocortical
    computational assumptions to BA35.
*   **Brodmann leaf under the temporal partition.** BA35 is a local leaf
    under `.../temporal/brodmann_areas/`, **not** a cross-listed or nested
    leaf.
*   **Medial perirhinal division of the perirhinal complex.** BA35 is the
    **medial** division of the perirhinal cortex; BA36 is the **lateral**
    division. The `SUBFIELD` constant below makes this explicit.
    Consumers that need the full perirhinal cortex must query **both**
    modules.
*   **Not the entorhinal cortex.** BA35 is **perirhinal**; the entorhinal
    cortex is **BA28 and BA34**. Consumers must not conflate them — they
    are adjacent but functionally distinct (object memory vs. spatial/
    declarative memory gateway).
*   **Structural parity with right BA35.** Left and right BA35 modules
    are **structurally identical** — same periallocortical type, same
    medial-perirhinal identity, same object-recognition functions, same
    weak lateralization.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.brodmann_areas import brodmann_area_35

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.brodmann_areas.brodmann_area_35"
    )

**Do not** apply neocortical computational assumptions to BA35. It is
**periallocortical / proisocortical** — agranular or dysgranular, lacking
a proper layer IV. Use the `CYTOARCHITECTONIC_TYPE` constant to check the
type::

    from ...temporal.brodmann_areas.brodmann_area_35 import CYTOARCHITECTONIC_TYPE
    # CYTOARCHITECTONIC_TYPE = "periallocortical_transitional"

For the medial-perirhinal subfield identity::

    from ...temporal.brodmann_areas.brodmann_area_35 import SUBFIELD
    # SUBFIELD = "medial_perirhinal (BA35)"

For the object-recognition functions::

    from ...temporal.brodmann_areas.brodmann_area_35 import SYMMETRIC_FUNCTIONS
    # object_recognition_memory, familiarity_discrimination,
    # visual_mnemonic_integration, complex_visual_configuration_processing,
    # semantic_memory, mnemonic_discrimination_objects

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba35_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.brodmann_areas.brodmann_area_35"
        )
        # resolve ba35_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der
    Grosshirnrinde*. (BA35 defined as the perirhinal area; described as
    "transitional cortex between archipallium and neopallium".)
*   **Perirhinal cortex overview and functions:** *Perirhinal Cortex — an
    overview* (ScienceDirect). The perirhinal cortex comprises BA35 and
    BA36; it receives highly processed sensory information and provides a
    route to and from the hippocampus; its position at the top of the
    sensory processing hierarchy and at the gateway to the limbic system
    supports sensory perception and memory; it plays a central role in
    **recognition memory** (clearest for **familiarity discrimination
    for single items**) and in **perceptual functions**[reference:32].
*   **BA35 as critical substrate for object recognition memory:**
    *Blockade of Glutamatergic Transmission in Perirhinal Cortex Impairs
    Object Recognition Memory in Macaques* (2015), *J Neurosci*. The
    **critical substrate for object recognition memory is located in the
    anteromedial perirhinal cortex — Area 35 and the medial portion of
    Area 36**; only infusions aimed at this site impaired performance;
    blocking glutamate transmission in BA35 significantly impaired
    object recognition memory[reference:33].
*   **Cytoarchitecture — agranular/dysgranular lamination:** *Predicting
    the Location of Human Perirhinal Cortex, Brodmann's area 35, from MRI*
    (2012), *PMC3508349*. BA35a is **agranular periallocortex** (layer
    IV absent); BA35b is **dysgranular proisocortex** (sparse layer IV);
    BA36 has a **compact granular layer IV** and is true isocortex;
    BA35 is **periallocortex and proisocortex**[reference:34].
*   **Signature large heart-shaped cells in layer V:** *Rhinal Sulcus —
    an overview* (ScienceDirect). A signature feature of perirhinal
    cortex is the presence of **large heart-shaped cells in deep layer V**
    that appear in **both BA36 and BA35**; BA35 has a **broad layer I**,
    and layers II and III tend to blend together[reference:35].
*   **Functions and clinical associations:** Neurofeedback Academy —
    *Brodmann Area 35 — Perirhinal Cortex*. Object recognition
    (recognition memory), familiarity evaluation, connection between
    perception and memory, visual-mnemonic integration, processing of
    complex visual configurations, involvement in semantic memory,
    conceptual object processing, early changes in Alzheimer's disease;
    associated with recognition memory disorders, impaired familiarity
    evaluation, findings reported in Alzheimer's disease and MCI,
    impaired object recognition, altered theta-gamma coupling
    [reference:36].
*   **Alzheimer's disease — earliest pathology in BA35:** *Sensitive
    Measures of Cognition in Mild Cognitive Impairment* (2018). In
    Alzheimer's disease, **neurofibrillary tangle pathology is first
    observed in Brodmann Area 35 (BA35)** — the medial portion of the
    perirhinal cortex[reference:37]. BA35 (the **transentorhinal region**)
    is among the **earliest brain regions to show tau accumulation**
    [reference:38]. **Selective atrophy in BA35** is associated with early
    cognitive changes in prodromal AD[reference:39].
*   **Mnemonic discrimination of objects:** *Mnemonic discrimination, the
    ability to distinguish similar events in memory* (DZNE). The
    perirhinal-transentorhinal region (area 35) and the anterior-lateral
    entorhinal cortex have been implicated in the **mnemonic
    discrimination of objects rather than scenes**[reference:40].
*   **Bilateral activation in object memory tasks:** *Functional
    Lateralization of Face, Hand, and Trunk Representation* (FZ
    Jülich). BOLD responses revealed a **significant linear trend in
    bilateral BA35** during object-recognition tasks (highest activation
    for familiar configurations).
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial temporal and perirhinal anatomy.)
*   NeuroNames — Brodmann area 35 (left); FMA — Brodmann area 35 (left
    member).
"""