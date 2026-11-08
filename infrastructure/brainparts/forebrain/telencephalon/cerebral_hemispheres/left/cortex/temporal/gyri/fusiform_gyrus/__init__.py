"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri.fusiform_gyrus
============================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── gyri
                        └── fusiform_gyrus   <-- THIS MODULE

**Primary synonym:** Fusiform gyrus (FG), left; Left FG; Lateral
occipitotemporal gyrus; Gyrus fusiformis; Occipitotemporal gyrus.
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the **ventral (inferior) surface** of the temporal
and occipital lobes.
**Structural boundaries:** **Collateral sulcus** (medially, separating
the fusiform gyrus from the parahippocampal gyrus) and **occipitotemporal
sulcus** (laterally, separating it from the inferior temporal gyrus).
**Lobe membership:** **Temporal and occipital** — the fusiform gyrus
spans the temporo-occipital junction; its anterior portion is temporal
and its posterior portion is occipital.
**Functional contents:** **Brodmann area 37** (BA37) — the core
cytoarchitectonic field — plus the **visual word form area (VWFA)** on
the left and the **fusiform face area (FFA)** on the right.
**Cytoarchitectonic type:** **Mixed neocortical/transitional** — the
fusiform gyrus contains **two cytoarchitectonic areas, FG1 and FG2**
(Caspers et al., 2013). **FG1** is a **transitional area** between early
and higher visual cortex; **FG2** is a **higher-order, lateralized
area** associated with **visual word-form processing on the left** and
**face processing on the right**.

Overview
--------
The **left fusiform gyrus** is the **left-hemisphere ventral
occipitotemporal convolution** — the **principal cortical substrate for
visual word recognition and reading** in the human brain. It sits at the
**final stages of the ventral visual "what" pathway**, downstream of the
occipital visual areas and upstream of the anterior temporal semantic
hub, and it contains the **visual word form area (VWFA)** — the
**left-lateralized substrate for reading**.

**The fusiform gyrus is the most functionally lateralized gyrus in the
temporal lobe.** Two areas of the fusiform cortex show a **remarkable
hemispheric lateralization**: **written words activate the VWFA in the
left fusiform gyrus**, and **faces activate a symmetrical site in the
right hemisphere, the FFA**. This is **parallel-laden at its
most extreme** — the left does **words**, the right does **faces**, and
**neither hemisphere is the "complement" or "denial" of the other**. Both
are **substantial, clinically named syndromes** (pure alexia vs.
prosopagnosia), and both are **equally weighted** in magnitude.

**The left fusiform gyrus is the left-hemisphere pole of the VWFA/FFA
pair.** The **left FG** contains the **VWFA** — the substrate for
**reading** — while the **right FG** contains the **FFA** — the
substrate for **face recognition**. This is the **most balanced and
most clinically asymmetric gyrus pair** in the entire temporal lobe.

**The fusiform gyrus is the gyral home of Brodmann area 37 (BA37).**
Unlike the superior temporal gyrus (which contains a **nested Brodmann
cross-listing** under ``wernickes_area``), the fusiform gyrus does **not**
contain a nested Brodmann module — BA37 lives as a **top-level Brodmann
leaf** under ``.../temporal/brodmann_areas/brodmann_area_37``. The
fusiform gyrus and BA37 are **co-extensive at the structural level**:
the gyrus is the surface convolution, and BA37 is its cytoarchitectonic
identity.

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. It is
**not** a functional region and **not** a cytoarchitectonic field. Its
contents span **both** of those partitions:

::

    Structural leaf (this module)        Functional / cytoarchitectonic contents
    ─────────────────────────────        ────────────────────────────────────────
    fusiform_gyrus (left)           ──▶  posterior_inferior_temporal_cortex
                                           (functional region; VWFA)
                                    ──▶  brodmann_area_37  (core field)
                                    ──▶  FG1 (transitional area; peripheral)
                                    ──▶  FG2 (higher-order area; VWFA left)

**The fusiform gyrus is the structural anchor for the VWFA.** The
**functional region** ``posterior_inferior_temporal_cortex`` (pITC) is
the **functional node** that contains the VWFA; the **Brodmann leaf**
``brodmann_area_37`` is the **cytoarchitectonic node**; and the
**fusiform gyrus** is the **structural convolution** that contains both.
The three-partition architecture is **fully instantiated** at the
fusiform gyrus.

**The fusiform gyrus is the first gyrus in the tree whose contents are
entirely defined by a single Brodmann field (BA37) plus its two
cytoarchitectonic subfields (FG1, FG2).** Unlike the STG (which spans
BA22, BA41/BA42 in the insular partition, and the nested Wernicke's-area
module), the fusiform gyrus is **cytoarchitectonically unified** around
BA37. This makes it the **cleanest structural-cytoarchitectonic
correspondence** in the temporal gyral partition.

Cytoarchitecture: FG1 and FG2
-----------------------------
The fusiform gyrus contains **two cytoarchitectonically distinct areas**
in its posterior portion — **FG1** and **FG2** (Caspers et al., 2013):

*   **FG1** — a **transitional area** between early and higher visual
    cortex. It is characterized by a **marked columnar arrangement of
    small pyramidal cells** and a **lower cell density in layer IV** when
    compared to neighboring areas. **Layer II** shows a
    **low density of cells** with a smooth transition into a **layer III
    of low to moderate cell density**. The **pyramidal cells in layer III
    are small** with **no superficial-to-deep increase**, and they are
    arranged in **clearly visible cell columns** — a feature that is
    **unique to FG1** compared to adjacent areas. **Layer IV is thin**,
    but clearly delineable from adjacent layers IIIc and V.
    **Layer V** pyramidal cells are small and show a columnar arrangement.
    The **border between cortex and white matter is blurred**.

*   **FG2** — a **higher-order, lateralized area** associated with
    **visual word-form processing on the left** and **face processing on
    the right**. It shows **large pyramidal cells in lower layer III**
    and a **prominent layer IV** as characteristic features. A **columnar
    arrangement of pyramidal cells is not found**, neither in layer III
    nor in layer V. **Layer II** has a **rather high cell density** with
    a clearly delineable border to the **cell-sparse layer IIIa**. **Large
    pyramidal cells of layer III** are primarily found in sublayers **IIIb
    and IIIc**, with a slight increase of cell sizes in deep sublayer IIIc.
    This sublayer often **merges with the broad and cell-dense layer IV**.
    **Layer V** consists of equally distributed pyramidal cells, which are
    smaller than those in lower layer III but larger than those of FG1.
    **Layer VI** is cell-dense with a distinct border to the white matter.

**The FG1/FG2 subdivision is the defining structural fact about the
fusiform gyrus.** FG1 is a **transitional area** with columnar
organization; FG2 is a **higher-order area** with large pyramidal cells
and a prominent layer IV. **FG2 is the cytoarchitectonic substrate of the
VWFA (left) and FFA (right)** — a **single cytoarchitectonic area**
that is **homogeneously found in both hemispheres** with **no
interhemispheric differences in cytoarchitecture, cortical volume, or
relative stereotaxic location**, yet is **functionally lateralized** into
**word processing (left)** and **face processing (right)**.

**This is a remarkable architectural fact:** the **same cytoarchitectonic
area (FG2)** hosts **two functionally distinct systems** (VWFA and FFA)
in the two hemispheres, and the **lateralization is not driven by
cytoarchitectonic differences** but by **connectivity differences** and
**competitive developmental processes**. This makes the fusiform gyrus the
**cleanest example in the tree of a gyrus whose functional lateralization
is not mirrored in its cytoarchitecture**.

Function in the Human Brain
---------------------------
The left fusiform gyrus is the **left-lateralized visual word and shape
processing hub**. Its best-supported functions cluster into six domains:

*   **Visual Word Form Processing (Left-Lateralized — the defining
    left-FG function):** The **VWFA** in the left mid-fusiform gyrus is
    **especially responsive to visual words** and is **essential to
    rapid reading ability**. **Perception of visual words and
    pseudowords reliably activates the left fusiform gyrus to a greater
    degree than other highly similar control stimuli**.
    The left FG is **more sensitive to orthographic information** than
    the right FG.

*   **Reading (Left-Lateralized):** The left FG supports **reading** via
    the VWFA. **Pure alexia** — a selective acquired impairment of
    visual word recognition — stems from **left fusiform lesions
    affecting the VWFA**. The VWFA acts as a **unique
    bottleneck** for efficient reading.

*   **Higher-Order Visual Shape Processing (Bilateral Foundation):** The
    posterior fusiform gyrus (FG1) is **responsible for combining visual
    features to form representations of complex shapes**. This is
    a **bilateral** foundation that supports the left-lateralized
    word-selective function.

*   **Visual Mental Imagery (Left-Lateralized):** The **Fusiform Imagery
    Node (FIN)** in the **left fusiform gyrus** is a **key hub for
    voluntary visual mental imagery**. **Lesions or disconnection of the
    FIN reliably impair imagery, sparing perception**. The FIN exhibits
    **functional connectivity with both frontoparietal control regions
    and domain-specific areas**, consistent with a role as a
    **semantic integration hub**.

*   **Face Processing — Parts-Based (Left-Lateralized):** The left
    fusiform gyrus is **superior for processing faces based on individual
    features** (parts-based processing). The **left middle fusiform
    gyrus** is more activated when matching **face parts** than whole
    faces — the **reverse of the right FG's whole-face advantage**.

*   **Higher-Order Visual Recognition (Bilateral):** The fusiform gyrus
    is involved in **high-order visual recognition processes**,
    particularly the recognition of **faces, bodies, and stimuli
    characterized by high spatial frequencies**. This is a
    **bilateral** foundation.

Associated Disorders
--------------------
Damage to or dysfunction of the left fusiform gyrus is associated with:

*   **Pure Alexia (Left-Lateralized — the signature left-FG syndrome):**
    **Pure alexia** (alexia without agraphia) is an **acquired reading
    disorder** typically due to a **left fusiform lesion affecting the
    VWFA**. A **surgical lesion close to the region sensitive to visual
    words** can result in **pure alexia**. The patient can write
    but cannot read, often reading **letter-by-letter**.

*   **Impaired Visual Mental Imagery (Left-Lateralized):** **Lesions or
    disconnection of the Fusiform Imagery Node (FIN)** in the left
    fusiform gyrus **reliably impair visual mental imagery**, sparing
    perception.

*   **Mild Face Processing Impairments (Left-Lateralized):** **Left
    fusiform lesions** can produce **mild impairments of face
    processing** alongside pure alexia, consistent with the overlapping
    patterns of face and word activation in the left fusiform cortex
    .

*   **Pure Alexia with Agraphia of Kanji (Left-Lateralized):** The left
    fusiform gyrus is involved in **Kanji (logographic) reading**;
    damage can produce **alexia with agraphia of kanji**.

**What is NOT here:** **Prosopagnosia** is a **right fusiform (FFA)**
syndrome, not a left FG syndrome. It is **absent** from left FG lesions.
It is documented in the right FG module and is **explicitly not claimed
here**. The left FG is the **word** pole; the right FG is the **face**
pole.

Lateralization Notes
--------------------
This is the **left** fusiform gyrus module. The lateralization landscape
is **parallel-laden** — both hemispheres carry **substantial, distinct,
non-overlapping functions of roughly equal magnitude**:

*   **Left-Lateralized Functions (dominant in this twin):**
    - **Visual word form processing (VWFA)** — orthographic analysis.
    - **Reading** — efficient parallel word recognition.
    - **Pure alexia** — the signature left-FG syndrome.
    - **Visual mental imagery (FIN)** — voluntary imagery hub.
    - **Parts-based face processing** — feature-level face analysis.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Fusiform face area (FFA)** — face recognition.
    - **Prosopagnosia** — the signature right-FG syndrome.
    - **Whole-based face processing** — holistic face analysis.

*   **Symmetric Functions (bilateral properties of the FG):**
    - Higher-order visual shape processing (FG1).
    - High-order visual recognition (faces, bodies, objects).
    - Processing of high-spatial-frequency stimuli.

**This is the "parallel-laden" pattern at its most extreme.** **Written
words activate the VWFA in the left fusiform gyrus** and **faces activate
a symmetrical site in the right hemisphere, the FFA**. Both are
**substantial, clinically named syndromes** (pure alexia vs.
prosopagnosia), and both are **equally weighted** in magnitude.

**The FG1/FG2 cytoarchitecture is symmetric; the functional lateralization
is not.** This is the **most remarkable architectural fact** about the
fusiform gyrus: **FG2 is homogeneously found in both hemispheres with no
interhemispheric differences in cytoarchitecture, cortical volume, or
relative stereotaxic location** — yet it hosts **two functionally
distinct systems** (VWFA and FFA). The lateralization is driven by
**connectivity differences** and **competitive developmental processes**,
not by cytoarchitectonic differences.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    occipital lobe (the fusiform's occipital continuation) or the
    insular lobe. Those are **cross-lobe references**, not structural
    parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural leaf, not a functional region or Brodmann field.**
    ``__all__`` lists the **gyrus itself**, not the functional regions
    (pITC) or Brodmann fields (BA37, FG1, FG2) it contains.
*   **Cytoarchitectonic symmetry vs. functional asymmetry — flagged in
    data.** The **FG2 area is cytoarchitectonically symmetric** between
    hemispheres but **functionally lateralized** (VWFA left, FFA right).
    The ``CYTOARCHITECTONIC_SYMMETRY`` constant documents this.
*   **Parallel-laden at its most extreme — flagged in data.** The left FG
    is the **VWFA**; the right FG is the **FFA**. Both are **equally
    weighted** named syndromes. This module documents the left-
    lateralized functions; the right module documents the right-
    lateralized functions.
*   **No nested cross-listing.** Unlike the STG (which contains the
    nested Wernicke's-area module), the fusiform gyrus does **not**
    contain a nested Brodmann leaf. BA37 lives as a top-level Brodmann
    leaf under ``.../temporal/brodmann_areas/brodmann_area_37``.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.gyri import fusiform_gyrus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.gyri.fusiform_gyrus"
    )

For the functional region (pITC) that contains the VWFA::

    from ...temporal.cortex import posterior_inferior_temporal_cortex

For the cytoarchitectonic field (BA37)::

    from ...temporal.brodmann_areas import brodmann_area_37

For the cytoarchitectonic symmetry vs. functional asymmetry::

    from ...temporal.gyri.fusiform_gyrus import CYTOARCHITECTONIC_SYMMETRY
    # CYTOARCHITECTONIC_SYMMETRY = True

For the left-lateralized functions::

    from ...temporal.gyri.fusiform_gyrus import LEFT_LATERALIZED
    # LEFT_LATERALIZED = ("visual_word_form_processing",
    #                     "reading",
    #                     "visual_mental_imagery",
    #                     "parts_based_face_processing")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        fg_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.gyri.fusiform_gyrus"
        )
        # resolve fg_path through the memory/recall layer

References
----------
*   **Fusiform gyrus overview and VWFA/FFA parallel-laden:** *Genetic and
    Environmental Influences on the Visual Word Form and Fusiform Face
    Areas* (2015), *Cereb Cortex*, 25(9), 2478–2493. **Written words
    activate the VWFA in the left fusiform gyrus** and **faces activate a
    symmetrical site in the right hemisphere, the FFA**.
*   **VWFA and reading:** McCandliss, B.D., et al. (2003). "The visual
    word form area: expertise for reading in the fusiform gyrus."
    *Trends Cogn Sci*, 7(7), 293–299. **Perception of visual words and
    pseudowords reliably activates the left fusiform gyrus** to a greater
    degree than other highly similar control stimuli.
*   **FG1 and FG2 cytoarchitecture:** Caspers, S., et al. (2013).
    "Cytoarchitectonical analysis and probabilistic mapping of two
    extrastriate areas of the human posterior fusiform gyrus." *Brain
    Struct Funct*, 218(2), 511–526. PMC3580145. **FG1** has a **marked
    columnar arrangement of small pyramidal cells** and a **lower cell
    density in layer IV**; **FG2** has **large pyramidal cells in lower
    layer III** and a **prominent layer IV**.
*   **FG2 functional lateralization with cytoarchitectonic symmetry:**
    *Functional characterization and differential coactivation patterns
    of two cytoarchitectonic visual areas on the human posterior fusiform
    gyrus* (2013), *Hum Brain Mapp*. PMC4791049. **FG2 is homogenously
    found on the lateral bank of the posterior fusiform gyrus in both
    hemispheres with no interhemispheric differences in cytoarchitecture,
    cortical volume, or relative stereotaxic location**; yet it is
    **hemisphere-specifically involved in two distinctive functional
    systems** — visual word processing (left) and face processing (right).
*   **Left FG and visual mental imagery (FIN):** *The Fusiform Imagery
    Node: Where vision meets concepts in the left temporal lobe* (2026),
    *ScienceDirect*. The **FIN in left fusiform is a key hub for
    voluntary visual mental imagery**; **lesions or disconnection of FIN
    reliably impair imagery, sparing perception**.
*   **Left FG and parts-based face processing:** *Hemispheric asymmetries
    for whole-based and part-based face processing in the human fusiform
    gyrus* (2000), *J Cogn Neurosci*, 12(5), 793–802. The **right middle
    fusiform gyrus** is more activated when matching **whole faces**;
    this pattern is **reversed in the left homologous region**, which is
    more activated for **face parts**.
*   **Right FG and whole-based face processing:** *Functional asymmetry
    between the left and right human fusiform gyrus explored through
    electrical brain stimulation* (2016), *Neuropsychologia*, 83, 29–36.
    **Electrical brain stimulation disrupted the conscious perception of
    faces only when it was delivered in the right, but not left, FG**
    .
*   **Pure alexia and left fusiform lesions:** *The neural bases of
    prosopagnosia and pure alexia* (2017), *Curr Opin Neurol*. A
    **surgical lesion close to the region sensitive to visual words can
    result in pure alexia**.
*   **Mild face impairments with pure alexia:** *Face perception in pure
    alexia: Complementary contributions of the left fusiform gyrus to
    facial identity and facial speech processing* (2017),
    *Neuropsychologia*. **Left fusiform lesions** can cause **pure
    alexia** and also lead to **mild impairments of face processing**
    .
*   **Fusiform connectivity:** *Anatomy and white matter connections of
    the fusiform gyrus* (2020), *Sci Rep*, 10, 12594. PMC7417738. The
    fusiform gyrus is **strongly connected to the occipital lobe** and is
    involved in **high-order visual recognition processes**,
    particularly the recognition of **faces** .
*   **Fusiform gyrus connectivity to intraparietal sulcus:** *Identification
    of a distinct association fiber tract "IPS-FG"* (2021). A distinct
    association fiber tract **"IPS-FG"** connects the **intraparietal
    sulcus** and the **fusiform gyrus**, linking a sensorimotor relay to
    a high-level visual area.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Ventral temporal and occipitotemporal anatomy.)
*   NeuroNames — Fusiform gyrus (left); FMA — left fusiform gyrus
    partonomy.
"""