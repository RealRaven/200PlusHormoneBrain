"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri.parahippocampal_gyrus
======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── gyri
                        └── parahippocampal_gyrus   <-- THIS MODULE

**Primary synonym:** Parahippocampal gyrus (PHG), right; Right PHG;
Gyrus parahippocampalis; Hippocampal gyrus (older nomenclature, when
including the subiculum).
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the **medial (tentorial) surface** of the temporal
lobe.
**Structural boundaries:** **Collateral sulcus** (laterally, separating
the PHG from the fusiform gyrus) and the **hippocampal fissure / medial
temporal surface** (medially, at the transition to the hippocampal
formation). Its anterior end is the **uncus**; its posterior end is the
**isthmus of the cingulate gyrus**.
**Lobe membership:** **Temporal** — the PHG is entirely within the
temporal lobe, forming its **medial wall**.
**Functional contents:** **BA27** (presubiculum), **BA28** (ventral
entorhinal), **BA34** (dorsal entorhinal), **BA35** (medial perirhinal),
**BA36** (lateral perirhinal/parahippocampal), **BA37** (posterior
boundary), plus the **parahippocampal place area (PPA)** and the
**parahippocampal cortex** (PHC).
**Cytoarchitectonic type:** **Allocortical / periallocortical /
proisocortical** — the PHG is the **most allocortical gyrus in the
tree**, containing **no true neocortical fields** except at its extreme
posterior boundary (BA37).

Overview
--------
The **right parahippocampal gyrus (PHG)** is the **right-hemisphere
medial temporal convolution** — the **principal cortical interface
between the neocortex and the hippocampal formation**, with a
**rightward weighting for spatial-context memory and scene processing**.
It is the **most allocortical gyrus in the entire brainparts tree** and
the **only gyrus whose contents are almost entirely allocortical,
periallocortical, or proisocortical fields** (BA27, BA28, BA34, BA35,
BA36), with only the **extreme posterior boundary (BA37)** representing
true neocortex.

**This is the right-hemisphere twin of the left PHG, and the pair
instantiates the "asymmetric-by-function" pattern at the structural
level** — a **process-specific division of labor** within the medial
temporal memory system:

*   **The left PHG is the left-lateralized pole** for **verbal
    declarative memory**, **object recognition and familiarity**, and
    **verbal context memory**. It carries the **left-hemisphere
    weighting** for object-identity and verbal memory.

*   **The right PHG is the right-lateralized pole** for **spatial-
    context memory**, **scene recognition (PPA)**, and **non-verbal
    declarative memory**. It carries the **right-hemisphere weighting**
    for spatial-context and scene-based memory.

**The PHG is the gyral home of the medial temporal lobe memory system.**
It contains **five of the six transitional Brodmann fields** documented
in the temporal Brodmann partition:

*   **BA27 (presubiculum)** — allocortical spatial-mnemonic relay.
*   **BA28 (ventral entorhinal)** — periallocortical memory gateway.
*   **BA34 (dorsal entorhinal)** — periallocortical memory gateway.
*   **BA35 (medial perirhinal)** — periallocortical object-recognition
    hub.
*   **BA36 (lateral perirhinal / parahippocampal)** — proisocortical
    familiarity and contextual-memory hub.

**The PHG is the gyral anchor for the parahippocampal place area
(PPA).** The **PPA** is a functionally defined region in the posterior
PHG that is **selectively responsive to scenes and places** — it is one
of the **most-studied category-selective regions** in the human brain.
The **parahippocampal cortex (PHC)** is the broader functionally defined
region that contains the PPA and supports **scene recognition, spatial
context, and episodic memory**. On the **right** side, the PPA and PHC
are **right-weighted** — the right PHG is the **dominant hemisphere for
scene processing**.

**The PHG is the only gyrus in the tree that is primarily an
allocortical surface.** Unlike the fusiform gyrus (BA37 + FG1 + FG2,
all neocortical), the ITG (BA20, neocortical), the MTG (BA20/BA21/BA37,
neocortical), and the STG (BA22 + insular BA41/BA42, neocortical), the
PHG is the **parent structural container** for the hybrid-name
allocortical regions — the **entorhinal cortex** and the **perirhinal
cortex** are **co-extensive with the medial aspect of the PHG**. The PHG
is therefore the **structural home of the allocortical memory system**
at the gyral level.

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. It is
**not** a functional region and **not** a cytoarchitectonic field. Its
contents span **both** of those partitions:

::

    Structural leaf (this module)        Functional / cytoarchitectonic contents
    ─────────────────────────────        ────────────────────────────────────────
    parahippocampal_gyrus (right)   ──▶  entorhinal_cortex (nested child)
                                    ──▶  perirhinal_cortex (nested child)
                                    ──▶  brodmann_area_27  (presubiculum)
                                    ──▶  brodmann_area_28  (ventral entorhinal)
                                    ──▶  brodmann_area_34  (dorsal entorhinal)
                                    ──▶  brodmann_area_35  (medial perirhinal)
                                    ──▶  brodmann_area_36  (lateral perirhinal)
                                    ──▶  brodmann_area_37  (posterior boundary)
                                    ──▶  parahippocampal_place_area (PPA)
                                    ──▶  parahippocampal_cortex (PHC)

**The PHG is the first gyrus in the tree that contains TWO hybrid-name
"gyri" as nested children.** The **entorhinal cortex** and the
**perirhinal cortex** are both wired as **structural leaves** under
``gyri/``, and they are **co-extensive with the medial aspect of the
PHG**. This makes the PHG the **structural parent** of both hybrid-name
regions — a **two-level structural hierarchy** that has no counterpart
in the parietal or other temporal gyri.

**The PHG is also the first gyrus in the tree whose contents are almost
entirely allocortical.** The only true neocortical field in the PHG is
BA37 at its extreme posterior boundary. The rest of the gyrus —
BA27, BA28, BA34, BA35, BA36 — is **allocortical, periallocortical, or
proisocortical**. A consumer that assumes all gyri contain neocortical
fields will be **wrong for the PHG** — and this is equally true on the
right side.

**The PHG is the gyral anchor for the PPA and the PHC.** On the
**right**, the PPA is **right-weighted** and is the **dominant
hemisphere for scene processing**. The PHC is the broader functional
region that contains the PPA and supports **spatial context, scene
recognition, and episodic memory retrieval**.

Cytoarchitecture: The Allocortical Series
-----------------------------------------
The PHG is the **structural home of the allocortical series** — the
six transitional Brodmann fields (BA27, BA28, BA34, BA35, BA36, plus
BA37 at the posterior boundary) that constitute the **medial temporal
lobe memory system**. Each field has a **distinct allocortical
cytoarchitectonic type**, **identical to the left twin**:

*   **BA27 (presubiculum)** — **allocortical** (three-layered) spatial-
    mnemonic relay. Contains **head-direction cells** in its dorsal
    part.
*   **BA28 (ventral entorhinal)** — **periallocortical** memory gateway.
    Contains a **lamina dissecans** and **layer II cell islands**.
*   **BA34 (dorsal entorhinal)** — **periallocortical** memory gateway.
    Agranular six-layered structure with **cell-dense islands in
    layer II**.
*   **BA35 (medial perirhinal)** — **periallocortical / proisocortical**
    object-recognition hub. **Agranular (35a) or dysgranular (35b)**
    lamination.
*   **BA36 (lateral perirhinal)** — **proisocortical / isocortical**
    familiarity and contextual-memory hub. **Rudimentary but present
    granular layer IV**.
*   **BA37 (posterior boundary)** — **mixed neocortical/transitional**
    higher-order visual processing. The only true neocortical field in
    the PHG.

**This is the first gyrus in the tree that contains a complete
allocortical-to-neocortical transition.** The PHG spans the **full
gradient** from allocortex (BA27) → periallocortex (BA28, BA34, BA35)
→ proisocortex (BA36) → neocortex (BA37). This is a **unique
architectural fact** — no other gyrus in the tree contains the **full
transitional series** from allocortex to neocortex.

**The PHG is the gyral counterpart of the Brodmann partition's
allocortical series.** The temporal Brodmann aggregator flagged
BA27/28/34/35/36 as the **allocortical/transitional series**; the
perirhinal and entorhinal cortex leaves documented them as **hybrid-name
regions**; and the PHG is the **gyral container** that holds them all.

Function in the Human Brain
---------------------------
The right PHG is the **right-lateralized medial temporal spatial-context
and scene-processing hub**. Its best-supported functions cluster into
six domains — **five symmetric with the left twin and one
right-lateralized emphasis**:

*   **Scene Recognition and the Parahippocampal Place Area (PPA —
    Right-Lateralized, the defining right-PHG function):** The
    **parahippocampal place area (PPA)** is a functionally defined
    region in the **posterior PHG** that is **selectively responsive to
    scenes and places**. It is **activated when participants view
    scenes** — landscapes, rooms, and spatial layouts — and it
    **responds more strongly to scenes than to other object categories**
    (faces, bodies, objects). The **right PPA is dominant for scene
    processing** in most individuals. This is a **right-lateralized**
    function.

*   **Spatial Context Memory (Right-Lateralized):** The PHG / PHC
    supports **spatial context memory** — memory for **where an event
    happened** and the **spatial layout in which it occurred**. This
    function is **right-weighted** in most individuals.
    This is a **right-lateralized** function.

*   **Non-Verbal Declarative Memory (Right-Lateralized):** The right
    PHG — via its entorhinal and perirhinal contents — supports
    **non-verbal declarative memory** (spatial, visual, and
    non-verbalizable material). This function is
    **right-weighted** in most individuals.

*   **Declarative Memory (the defining bilateral function):** The PHG
    — via its entorhinal and perirhinal contents — is a **critical
    component of the medial temporal lobe declarative memory system**.
    It supports **memory encoding, consolidation, and retrieval** via
    its bidirectional connections with the hippocampus and the
    neocortex.

*   **Object Recognition Memory and Familiarity (bilateral, with left
    weighting):** The **perirhinal cortex** — which is co-extensive
    with the medial PHG — is the **principal cortical substrate for
    object recognition memory and familiarity discrimination**. This
    function is **left-weighted** for verbal/object-identity memory.

*   **Gateway to the Hippocampus (the defining structural function):**
    The PHG — via its entorhinal and perirhinal contents — is the
    **cortical gateway to the hippocampal formation**. It receives
    **convergent multimodal input** from association cortices and
    relays it to the hippocampus via the **perforant pathway**.

Associated Disorders
--------------------
Damage to or dysfunction of the right PHG is associated with:

*   **Impaired Scene Recognition and Spatial Context Memory
    (Right-Lateralized — the signature right-PHG syndrome):** **Impaired
    recognition of scenes** and **impaired spatial-context memory**
    following **right PHG damage**, consistent with the right PPA's role
    in scene processing.

*   **Impaired Non-Verbal Declarative Memory (Right-Lateralized):**
    Impaired **spatial, visual, and non-verbalizable memory** following
    **right PHG damage**, consistent with the right-hemisphere weighting
    for non-verbal memory.

*   **Alzheimer's Disease (Earliest Pathology — Bilateral):** The PHG
    is a **site of earliest pathology in Alzheimer's disease**. **PHG
    atrophy** is a **core biomarker of AD progression**, and its
    degeneration is a **core substrate of the early memory impairment**.
    This is a **bilaterally devastating** finding, but the **spatial
    and scene-memory components** of the early deficit are
    **right-weighted**.

*   **Temporal Lobe Epilepsy (Bilateral):** The PHG — via its
    entorhinal and perirhinal contents — is a **critical substrate for
    seizure generation and propagation** in temporal lobe epilepsy.
    **Patients with unilateral TLE show bilateral reduction in EC
    volume**.

*   **Findings Reported in Schizophrenia:** The PHG has been implicated
    in schizophrenia, though this is a **finding reported** rather than
    an established syndrome attribution.

**What is NOT here:** **Verbal declarative memory deficits**,
**verbal context memory deficits**, and **object-recognition memory
deficits** are **left PHG** functions. They are **absent** from right
PHG lesions. They are documented in the left PHG module and are
**explicitly not claimed here**. The right PHG is the **spatial/scene**
pole; the left PHG is the **verbal/object** pole.

Lateralization Notes
--------------------
This is the **right** PHG module. The lateralization landscape is
**asymmetric-by-function with left-verbal/right-spatial specialization**
— a **process-specific division of labor** within the medial temporal
memory system:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Scene recognition (PPA)** — right-weighted scene processing.
    - **Spatial context memory** — memory for where events happened.
    - **Non-verbal declarative memory** — spatial, visual, and
      non-verbalizable material.

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Verbal declarative memory** — left PHG damage preferentially
      impairs verbal memory.
    - **Object recognition and familiarity** — left perirhinal-weighted.
    - **Verbal context memory** — left-weighted.

*   **Symmetric Functions (bilateral properties of the PHG, copied
    verbatim from the left twin):**
    - Gateway to the hippocampus (perforant pathway).
    - Declarative memory (episodic and semantic) — core bilateral.
    - Alzheimer's disease vulnerability (earliest pathology).
    - Temporal lobe epilepsy seizure substrate.

**This is the "asymmetric-by-function" pattern at the structural level**
— the gyral leaf mirrors the EC and perirhinal cortex leaves' division
of labor. The left PHG carries **verbal-memory and object-recognition**
work; the right PHG carries **spatial-context and scene-recognition**
work. Neither hemisphere is the "dominant" one; they are **different
functional fields** that share the same structural convolution.

**A consumer that assumes "right PHG = left PHG" will miss the
right-lateralized spatial-context and scene-recognition weightings** —
but the right twin is not merely "denying" the left's verbal-memory
functions; it is **carrying different functions**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from the
    hippocampus, the occipital lobe, or the insular lobe. Those are
    **downstream/upstream targets**, not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural leaf, not a functional region or Brodmann field.**
    ``__all__`` lists the **gyrus itself**, not the hybrid-name regions
    (EC, perirhinal cortex), Brodmann fields (BA27–BA37), or functional
    regions (PPA, PHC) it contains.
*   **Parent of two hybrid-name "gyri" — flagged in data.** The
    **entorhinal cortex** and **perirhinal cortex** are **co-extensive
    with the medial aspect of the PHG**. The ``CONTAINED_HYBRID_GYRI``
    constant documents this two-level structural hierarchy.
*   **Allocortical series span — flagged in data.** The PHG contains
    **five of the six allocortical/transitional Brodmann fields**
    (BA27, BA28, BA34, BA35, BA36) plus the posterior BA37.
*   **Asymmetric-by-function — flagged in data.** The right PHG carries
    **spatial-context and scene-recognition** functions; the left PHG
    carries **verbal-memory and object-recognition** functions.
*   **Structural parity with left PHG.** Left and right PHG modules are
    **structurally identical** in their Brodmann field span,
    hybrid-name children, and functional regions; only the
    **lateralization prose** differs (spatial/scene vs.
    verbal/object).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri import parahippocampal_gyrus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.gyri.parahippocampal_gyrus"
    )

For the two hybrid-name "gyri" that are co-extensive with the PHG::

    from ...temporal.gyri import entorhinal_cortex, perirhinal_cortex

For the Brodmann fields the PHG contains::

    from ...temporal.brodmann_areas import (
        brodmann_area_27, brodmann_area_28, brodmann_area_34,
        brodmann_area_35, brodmann_area_36, brodmann_area_37,
    )

For the allocortical-to-neocortical transition::

    from ...temporal.gyri.parahippocampal_gyrus import (
        BRODMANN_FIELDS, CONTAINED_HYBRID_GYRI,
    )

For the right-lateralized functions::

    from ...temporal.gyri.parahippocampal_gyrus import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("spatial_context_memory",
    #                      "scene_recognition_PPA",
    #                      "nonverbal_declarative_memory")

For the left-lateralized functions explicitly denied here::

    from ...temporal.gyri.parahippocampal_gyrus import DENIED_LEFT_LATERALIZED
    # DENIED_LEFT_LATERALIZED = ("verbal_declarative_memory",
    #                            "object_recognition_and_familiarity",
    #                            "verbal_context_memory")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        phg_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.parahippocampal_gyrus"
        )
        # resolve phg_path through the memory/recall layer

References
----------
*   **PHG anatomy and boundaries:** *Parahippocampal Gyrus — an overview*
    (ScienceDirect). The PHG is bounded laterally by the **collateral
    sulcus** and medially by the **hippocampal fissure**; its anterior
    end is the **uncus**; its posterior end is the **isthmus of the
    cingulate gyrus**.
*   **PHG and medial temporal memory:** Squire, L.R., & Zola-Morgan, S.
    (1991). "The medial temporal lobe memory system." *Science*,
    253(5026), 1380–1386. The PHG, EC, and perirhinal cortex are the
    **cortical interface** between the neocortex and the hippocampus
    for **declarative memory**.
*   **PPA and scene processing:** Epstein, R., & Kanwisher, N. (1998).
    "A cortical representation of the local visual environment."
    *Nature*, 392(6676), 598–601. The **parahippocampal place area
    (PPA)** is a functionally defined region in the posterior PHG
    that is **selectively responsive to scenes and places**.
*   **PPA right-hemisphere weighting:** *Scene-selective cortex*
    (NeuroImage). The PPA is **bilaterally active** but with a
    **right-hemisphere weighting** for scene processing.
*   **PHG and spatial-context memory:** *The role of the parahippocampal
    cortex in episodic memory* (2017), *Cortex*. The **PHC** supports
    **spatial context memory** for events, with a **right-hemisphere
    weighting**.
*   **Right PHG and non-verbal memory:** *Lateralized spatial and object
    memory encoding in entorhinal and perirhinal cortices* (2005),
    *Learn Mem*, 16(7), 433–438. **Object encoding is biased to the
    left hemisphere, whereas spatial encoding is biased to the right**;
    the right PHG is preferentially involved in **non-verbal memory**.
*   **PHG and object recognition memory (contrast — left):** *Perirhinal
    Cortex — an overview* (ScienceDirect). The perirhinal cortex,
    co-extensive with the medial PHG, is the **principal cortical
    substrate for object recognition memory and familiarity**.
*   **EC and earliest AD pathology:** *Entorhinal cortex dysfunction in
    Alzheimer's disease* (2023), *Trends Neurosci*, 46(2), 124–136.
    The EC is the **site of earliest histological alterations in AD**
    — neurofibrillary tangles and cell death — with **PHG atrophy**
    being a **core biomarker** of AD progression.
*   **EC and TLE seizure substrate:** *Entorhinal cortex in temporal
    lobe epilepsy* (1999), *Neurology*, 52(9), 1870. The EC is a
    **distinct anatomic and functional region** of the anterior PHG
    that plays a role in **seizure generation and propagation** in TLE.
*   **PHG and schizophrenia:** *Hippocampal and parahippocampal
    abnormalities in schizophrenia* (2007), *Arch Gen Psychiatry*. The
    PHG has been implicated in schizophrenia, though this is a
    **finding reported** rather than an established syndrome
    attribution.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Medial temporal and hippocampal-formation anatomy.)
*   NeuroNames — Parahippocampal gyrus (right); FMA — right
    parahippocampal gyrus partonomy.
"""