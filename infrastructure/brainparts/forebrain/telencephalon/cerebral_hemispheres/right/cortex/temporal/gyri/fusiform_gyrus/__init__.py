"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri.fusiform_gyrus
=============================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── temporal
                    └── gyri
                        └── fusiform_gyrus   <-- THIS MODULE

**Primary synonym:** Fusiform gyrus (FG), right; Right FG; Lateral
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
cytoarchitectonic field — plus the **fusiform face area (FFA)** on the
right and the **visual word form area (VWFA)** on the left.
**Cytoarchitectonic type:** **Mixed neocortical/transitional** — the
fusiform gyrus contains **two cytoarchitectonic areas, FG1 and FG2**
(Caspers et al., 2013). **FG1** is a **transitional area** between early
and higher visual cortex; **FG2** is a **higher-order, lateralized
area** associated with **face processing on the right** and **visual
word-form processing on the left**.

Overview
--------
The **right fusiform gyrus** is the **right-hemisphere ventral
occipitotemporal convolution** — the **principal cortical substrate for
face recognition** in the human brain. It sits at the **final stages of
the ventral visual "what" pathway**, downstream of the occipital visual
areas and upstream of the anterior temporal semantic hub, and it
contains the **fusiform face area (FFA)** — the **right-lateralized
substrate for face recognition**.

**This is the right-hemisphere twin of the left fusiform gyrus, and the
pair instantiates the "parallel-laden" pattern at its most extreme.**
The two hemispheres carry **different functions**, not the same function
with inverted weightings:

*   **The left fusiform gyrus is the left-lateralized pole** for
    **visual word recognition** — the **visual word form area (VWFA)**.
    Its damage produces **pure alexia** (alexia without agraphia).

*   **The right fusiform gyrus is the right-lateralized pole** for
    **face recognition** — the **fusiform face area (FFA)**. Its damage
    produces **prosopagnosia** (the inability to recognize familiar
    faces).

**The fusiform gyrus is the most functionally lateralized gyrus in the
temporal lobe.** Two areas of the fusiform cortex show a **remarkable
hemispheric lateralization**: **written words activate the VWFA in the
left fusiform gyrus**, and **faces activate a symmetrical site in the
right hemisphere, the FFA**. This is **parallel-laden at its
most extreme** — the left does **words**, the right does **faces**, and
**neither hemisphere is the "complement" or "denial" of the other**. Both
are **substantial, clinically named syndromes** (pure alexia vs.
prosopagnosia), and both are **equally weighted** in magnitude.

**The right fusiform gyrus is the right-hemisphere pole of the VWFA/FFA
pair.** The **right FG** contains the **FFA** — the substrate for
**face recognition** — while the **left FG** contains the **VWFA** — the
substrate for **reading**. This is the **most balanced and
most clinically asymmetric gyrus pair** in the entire temporal lobe.

**The fusiform gyrus is the gyral home of Brodmann area 37 (BA37).**
Unlike the superior temporal gyrus (which contains a **nested Brodmann
cross-listing** under ``wernickes_area``), the fusiform gyrus does **not**
contain a nested Brodmann module — BA37 lives as a **top-level Brodmann
leaf** under ``.../temporal/brodmann_areas/brodmann_area_37``.

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. It is
**not** a functional region and **not** a cytoarchitectonic field. Its
contents span **both** of those partitions:

::

    Structural leaf (this module)        Functional / cytoarchitectonic contents
    ─────────────────────────────        ────────────────────────────────────────
    fusiform_gyrus (right)          ──▶  posterior_inferior_temporal_cortex
                                           (functional region; FFA)
                                    ──▶  brodmann_area_37  (core field)
                                    ──▶  FG1 (transitional area; peripheral)
                                    ──▶  FG2 (higher-order area; FFA right)

**The fusiform gyrus is the structural anchor for the FFA.** The
**functional region** ``posterior_inferior_temporal_cortex`` (pITC) is
the **functional node** that contains the FFA; the **Brodmann leaf**
``brodmann_area_37`` is the **cytoarchitectonic node**; and the
**fusiform gyrus** is the **structural convolution** that contains both.

Cytoarchitecture: FG1 and FG2 — Symmetric
-----------------------------------------
The right fusiform gyrus contains **two cytoarchitectonically distinct
areas** in its posterior portion — **FG1** and **FG2** (Caspers et al.,
2013). The cytoarchitecture is **identical to the left twin**:

*   **FG1** — a **transitional area** between early and higher visual
    cortex. Characterized by a **marked columnar arrangement of small
    pyramidal cells** and a **lower cell density in layer IV**.
    **Layer II** shows a **low density of cells**. **Layer IV is
    thin** but clearly delineable. **Layer V** pyramidal cells are
    small with columnar arrangement. The **border between cortex and
    white matter is blurred**.

*   **FG2** — a **higher-order, lateralized area**. Characterized by
    **large pyramidal cells in lower layer III** and a **prominent
    layer IV**. **Layer II** has a **rather high cell density**.
    **Large pyramidal cells of layer III** are primarily found in
    sublayers **IIIb and IIIc**. **Layer V** has equally distributed
    pyramidal cells. **Layer VI** is cell-dense with a distinct border
    to white matter.

**The FG1/FG2 subdivision is the defining structural fact about the
fusiform gyrus — and it is CYTOARCHITECTONICALLY SYMMETRIC between
hemispheres.** FG2 is **homogenously found on the lateral bank of the
posterior fusiform gyrus in both hemispheres with no interhemispheric
differences in cytoarchitecture, cortical volume, or relative stereotaxic
location** — yet it is **hemisphere-specifically involved in two
distinctive functional systems**: visual word processing (left) and
**face processing (right)**.

**This is a remarkable architectural fact:** the **same cytoarchitectonic
area (FG2)** hosts **two functionally distinct systems** (VWFA and FFA)
in the two hemispheres, and the **lateralization is not driven by
cytoarchitectonic differences** but by **connectivity differences** and
**competitive developmental processes**.

Function in the Human Brain
---------------------------
The right fusiform gyrus is the **right-lateralized face-recognition and
visual-structural hub**. Its best-supported functions cluster into six
domains:

*   **Face Recognition (Right-Lateralized — the defining right-FG
    function):** The **right mid-fusiform gyrus** contains the
    **fusiform face area (FFA)** — the **right-lateralized substrate
    for face recognition**. The FFA is a **region in the fusiform gyrus**
    that shows **greater activation for faces than for other object
    categories**, and it is **crucial for normal face recognition**.
    **Face-selective cortex is right-lateralized in the majority of
    individuals**.

*   **Prosopagnosia (Right-Lateralized — the signature right-FG
    syndrome):** **Acquired prosopagnosia** — the inability to recognize
    familiar faces — is the result of brain pathology involving the
    **right fusiform gyrus (FFA)** or both fusiform gyri.
    **Apperceptive prosopagnosia** is associated with **lesions of the
    right fusiform face area**, and the **right fusiform gyrus is the
    critical lesion site** for the face-recognition deficit.

*   **Whole-Based Face Processing (Right-Lateralized):** The **right
    middle fusiform gyrus** is **more activated when matching whole
    faces** — the **holistic face-processing advantage** that the left
    FG does not have. The **left FG is more activated for face parts**;
    the **right FG is more activated for whole faces**. This is a
    **double dissociation** between parts-based (left) and whole-based
    (right) face processing.

*   **Higher-Order Visual Shape Processing (Bilateral Foundation):** The
    posterior fusiform gyrus (FG1) is **responsible for combining visual
    features to form representations of complex shapes**. This is
    a **bilateral** foundation that supports the right-lateralized
    face-selective function.

*   **Visual Mental Imagery — Right Contribution (Bilateral, with Left
    Dominance):** The **Fusiform Imagery Node (FIN)** is primarily a
    **left fusiform hub**, but the **right fusiform gyrus contributes
    to imagery** via its structural and functional connections. On the
    right, the contribution is more **spatial and structural** than
    **semantic**.

*   **Higher-Order Visual Recognition (Bilateral):** The fusiform gyrus
    is involved in **high-order visual recognition processes**,
    particularly the recognition of **faces, bodies, and stimuli
    characterized by high spatial frequencies**. This is a
    **bilateral** foundation.

Associated Disorders
--------------------
Damage to or dysfunction of the right fusiform gyrus is associated with:

*   **Prosopagnosia (Right-Lateralized — the signature right-FG
    syndrome):** **Acquired inability to recognize familiar faces**,
    following **focal lesions in the right fusiform gyrus (FFA)** or
    bilateral fusiform lesions. **Apperceptive prosopagnosia** is
    specifically associated with **right FFA lesions**, and the
    **right fusiform gyrus is the critical lesion site** for the
    face-recognition deficit.

*   **Impaired Whole-Based Face Processing (Right-Lateralized):**
    Difficulty perceiving faces **holistically** — the right FG's
    distinctive face-processing contribution. **Electrical brain
    stimulation disrupted the conscious perception of faces only when
    it was delivered in the right, but not left, FG**.

*   **Impaired Visual Structural Processing (Right-Lateralized):**
    Difficulty with **high-order visual structural judgments** of faces
    and complex objects, consistent with the right FG's role in
    **whole-based visual processing**.

*   **Associative Visual Agnosia (Bilateral or Right-Lateralized):**
    Impaired **recognition of visual objects** when early perceptual
    processing is preserved. The **right FG** contributes to
    **structural and holistic object recognition** (as distinct from
    the left's semantic naming).

**What is NOT here:** **Pure alexia**, **letter-by-letter reading**, and
**verbal mental imagery deficits** are **left FG** syndromes. They are
**absent** from right FG lesions. They are documented in the left FG
module and are **explicitly not claimed here**. The right FG is the
**face** pole; the left FG is the **word** pole.

Lateralization Notes
--------------------
This is the **right** fusiform gyrus module. The lateralization landscape
is **parallel-laden** — both hemispheres carry **substantial, distinct,
non-overlapping functions of roughly equal magnitude**:

*   **Right-Lateralized Functions (dominant in this twin):**
    - **Fusiform face area (FFA)** — face recognition.
    - **Prosopagnosia** — the signature right-FG syndrome.
    - **Whole-based face processing** — holistic face analysis.
    - **Right FFA functional dominance** — electrical brain stimulation
      disrupts face perception only in the right FG.

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Visual word form processing (VWFA)** — orthographic analysis.
    - **Reading** — efficient parallel word recognition.
    - **Pure alexia** — the signature left-FG syndrome.
    - **Parts-based face processing** — feature-level face analysis.
    - **Verbal mental imagery (FIN)** — left fusiform imagery hub.

*   **Symmetric Functions (bilateral properties of the FG, copied
    verbatim from the left twin):**
    - Higher-order visual shape processing (FG1).
    - High-order visual recognition (faces, bodies, objects).
    - Processing of high-spatial-frequency stimuli.

**This is the "parallel-laden" pattern at its most extreme.** **Written
words activate the VWFA in the left fusiform gyrus** and **faces
activate a symmetrical site in the right hemisphere, the FFA**. Both are
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
*   **No cross-hemisphere imports.** Right side only.
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
*   **Parallel-laden at its most extreme — flagged in data.** The right
    FG is the **FFA**; the left FG is the **VWFA**. Both are **equally
    weighted** named syndromes.
*   **No nested cross-listing.** Unlike the STG, the fusiform gyrus
    does **not** contain a nested Brodmann leaf. BA37 lives as a
    top-level Brodmann leaf under
    ``.../temporal/brodmann_areas/brodmann_area_37``.
*   **Structural parity with left FG.** Left and right FG modules are
    **structurally identical** in their cytoarchitectonic constants and
    subfield definitions; only the **lateralization prose** differs
    (faces vs. words).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.temporal.gyri import fusiform_gyrus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "temporal.gyri.fusiform_gyrus"
    )

For the functional region (pITC) that contains the FFA::

    from ...temporal.cortex import posterior_inferior_temporal_cortex

For the cytoarchitectonic field (BA37)::

    from ...temporal.brodmann_areas import brodmann_area_37

For the cytoarchitectonic symmetry vs. functional asymmetry::

    from ...temporal.gyri.fusiform_gyrus import CYTOARCHITECTONIC_SYMMETRY
    # CYTOARCHITECTONIC_SYMMETRY = True

For the right-lateralized functions::

    from ...temporal.gyri.fusiform_gyrus import RIGHT_LATERALIZED
    # RIGHT_LATERALIZED = ("face_recognition_FFA",
    #                      "prosopagnosia",
    #                      "whole_based_face_processing")

For the left-lateralized functions explicitly denied here::

    from ...temporal.gyri.fusiform_gyrus import DENIED_LEFT_LATERALIZED
    # DENIED_LEFT_LATERALIZED = ("visual_word_form_processing",
    #                            "reading",
    #                            "visual_mental_imagery",
    #                            "parts_based_face_processing")

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
*   **FFA and prosopagnosia (right-lateralized):** Kanwisher, N.,
    McDermott, J., & Chun, M.M. (1997). "The fusiform face area: a
    module in human extrastriate cortex specialized for face perception."
    *J Neurosci*, 17(11), 4302–4311. The FFA is a **region in the
    fusiform gyrus** with **greater activation for faces than for other
    object categories**.
*   **Right FFA lesions and apperceptive prosopagnosia:** *The
    rehabilitation of face processing in acquired prosopagnosia*
    (Taylor & Francis). **Apperceptive prosopagnosia is specifically
    associated with lesions of the right fusiform face area**.
*   **Right fusiform gyrus as critical lesion site:** *Prosopagnosia —
    an overview* (ScienceDirect). **The right fusiform gyrus is the
    critical lesion site** for prosopagnosia.
*   **FG1 and FG2 cytoarchitecture:** Caspers, S., et al. (2013).
    "Cytoarchitectonical analysis and probabilistic mapping of two
    extrastriate areas of the human posterior fusiform gyrus." *Brain
    Struct Funct*, 218(2), 511–526. PMC3580145.
*   **FG2 cytoarchitectonic symmetry with functional lateralization:**
    *Functional characterization and differential coactivation patterns
    of two cytoarchitectonic visual areas on the human posterior fusiform
    gyrus* (2013), *Hum Brain Mapp*. PMC4791049. **FG2 is homogenously
    found on the lateral bank of the posterior fusiform gyrus in both
    hemispheres with no interhemispheric differences in cytoarchitecture,
    cortical volume, or relative stereotaxic location**; yet it is
    **hemisphere-specifically involved in two distinctive functional
    systems** — visual word processing (left) and face processing (right).
*   **Right FG and whole-based face processing:** *Hemispheric asymmetries
    for whole-based and part-based face processing in the human fusiform
    gyrus* (2000), *J Cogn Neurosci*, 12(5), 793–802. The **right middle
    fusiform gyrus** is more activated when matching **whole faces**;
    this pattern is **reversed in the left homologous region**.
*   **Electrical brain stimulation and right FG:** *Functional asymmetry
    between the left and right human fusiform gyrus explored through
    electrical brain stimulation* (2016), *Neuropsychologia*, 83, 29–36.
    **Electrical brain stimulation disrupted the conscious perception of
    faces only when it was delivered in the right, but not left, FG**.
*   **Face-selective right lateralization:** *Face-Specific Activation in
    the Human Brain* (PMC). **Face-selective cortex is right-lateralized
    in the majority of individuals**; the right mid-fusiform gyrus shows
    greater face selectivity than the left.
*   **Fusiform connectivity:** *Anatomy and white matter connections of
    the fusiform gyrus* (2020), *Sci Rep*, 10, 12594. PMC7417738. The
    fusiform gyrus is **strongly connected to the occipital lobe** and is
    involved in **high-order visual recognition processes**, particularly
    the recognition of **faces**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Ventral temporal and occipitotemporal anatomy.)
*   NeuroNames — Fusiform gyrus (right); FMA — right fusiform gyrus
    partonomy.
"""