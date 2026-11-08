"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex.posterior_parietal_cortex
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── cortex
                        └── posterior_parietal_cortex   <-- THIS MODULE

**Primary synonym:** Posterior Parietal Cortex (PPC), left; Left PPC.
**Organizing principle:** **Functional–anatomical region**, the polymodal
association territory of the left parietal lobe.
**Brodmann constitution:** **BA5 + BA7** (plus the adjacent intraparietal
sulcus fields, functionally).
**Part of:** The **functional partition** of the left parietal lobe
(``.../parietal/cortex``), alongside S1 and S2.
**Cytoarchitectonic siblings:** ``.../parietal/brodmann_areas/brodmann_area_5``
and ``.../parietal/brodmann_areas/brodmann_area_7`` — the same territory,
partitioned differently. See "Two-Partition Context" below.

Overview
--------
The **left posterior parietal cortex (PPC)** is the polymodal association
territory of the left parietal lobe. It lies **caudal to the postcentral
sulcus**, encompasses **Brodmann areas 5 and 7**, and is the principal
cortical substrate for transforming sensory coordinates into **action-relevant
spatial and motor representations**[reference:0][reference:1]. It is the first
parietal territory where somatosensation, proprioception, vision, and
oculomotor signals converge.

The left PPC is **not** a single homogeneous area. It comprises two
functionally dissociable Brodmann fields with a clean internal boundary:

*   **BA5 (anterior PPC)** — unimodal somatosensory association cortex.
    Receives S1 input, performs proprioceptive and postural integration, and
    provides **somesthetic information to grasping circuits** linking the
    anterior intraparietal area (AIP) and frontal motor areas[reference:2].
*   **BA7 (posterior PPC)** — polymodal association cortex. Converges visual,
    somatosensory, and oculomotor signals; supports **visuomotor integration
    for reaching and grasping**, spatial transformation, and spatial working
    memory[reference:3].

**The left PPC is not the right PPC.** The right PPC carries the dominant
substrate for **sustained spatial attention and hemispatial neglect**; the
left PPC carries a **distinct, left-lateralized functional profile** centred
on **sensorimotor intention, categorical spatial processing, praxis
co-lateralization, and episodic retrieval**[reference:4][reference:5]. The
left and right PPC are **parallel-laden** at the functional-region level: both
carry substantial, non-overlapping lateralized functions.

Two-Partition Context
---------------------
This module is the **functional-region node** for the left PPC. It is
**constituted by** two Brodmann-area leaves that are wired under the sibling
cytoarchitectonic partition:

::

    Functional partition (this module)     Cytoarchitectonic partition
    ──────────────────────────────────     ────────────────────────────
    posterior_parietal_cortex       ──┐
                                     ├──▶  brodmann_area_5  (anterior PPC;
                                     │      unimodal somatosensory
                                     │      association)
                                     └──▶  brodmann_area_7  (posterior PPC;
                                            polymodal association)

The **BA5/BA7 boundary** is the key internal distinction within the left PPC:

*   **BA5** is the **last unimodal** parietal field. Direct thalamic input
    from VPL/VPM stops at the BA2/BA5 border; BA5 is association cortex but
    remains **somatosensory-dominant**.
*   **BA7** is the **first polymodal** parietal field. It receives visual and
    oculomotor input in addition to somatosensory input, and it does not
    obligatorily respond to passive touch.

Consumers that need the cytoarchitectonic detail of either subfield should
query the corresponding Brodmann leaf. This module documents the **PPC as a
functional unit** and the **division of labour between BA5 and BA7**; it does
not duplicate the per-area documentation.

Function in the Human Brain
---------------------------
The left PPC is a **left-lateralized sensorimotor-intentional and
categorical-spatial hub**. Its best-supported functions cluster into six
domains:

*   **Motor Intention and High-Level Movement Planning:** The left PPC is
    engaged in **forming motor intentions** — high-level cognitive plans for
    movements, distinct from the low-level execution signals of motor cortex
    [reference:6]. It bridges sensory representation and action planning.

*   **Reaching and Grasping — Sensorimotor Transformation:** The left PPC
    coordinates **reach and grasp behaviours** and provides **on-line
    feedback needed for goal-directed hand movements**[reference:7]. Area 5
    supplies **somesthetic information** to the AIP/7b-to-frontal grasping
    circuit, while area 7b/AIP supports **visually guided grasping**[reference:8]
    [reference:9]. Hand-manipulation neurons in the PPC are active during the
    **planning of grasp** as the hand is preshaped to acquire objects during
    reach[reference:10].

*   **Categorical Spatial Processing:** The left PPC is preferentially
    engaged in **categorical spatial processing** (e.g., "above/below",
    "left/right" relationships), as distinct from the **coordinate spatial
    processing** (precise metric distance) subserved by the right PPC
    [reference:11]. The left PPC appears to be activated **earlier** in
    visuospatial mental imagery than parts of the right PPC[reference:12].

*   **Mental Rotation and Spatial Transformation:** The left PPC is
    specifically engaged when stimuli to be compared are **rotated through
    180°**, a task that engages **verbal strategies** due to the special
    nature of enantiomorphs[reference:13]. This is a distinct left-PPC
    contribution to spatial cognition, complementary to the right PPC's
    general spatial-transformation dominance.

*   **Spatio-Temporal Monitoring of Limb Position:** The left PPC is
    **critically involved in monitoring limb position and in spatio-temporal
    binding** when serial events are delivered to the limbs[reference:14]
    [reference:15]. It is activated during **crossed-hands postures**, a task
    that demands remapping of limb position into external space
    [reference:16].

*   **Praxis Co-Lateralization with Language:** The left PPC is part of the
    **left-lateralized praxis network**, which is **co-lateralized with the
    language network** in prefrontal, premotor, and posterior parietal
    regions[reference:17][reference:18]. Tool-use pantomiming produces left
    hemisphere changes in the PPC, and the praxis and language networks
    overlap in the left PPC regardless of handedness.

*   **Episodic Retrieval (Left IPS):** The left intraparietal sulcus (IPS),
    within the left PPC, shows **strong left-lateralization of retrieval
    success effects** and performs operations common to both **task
    preparation and episodic memory retrieval**[reference:20].

Associated Disorders
--------------------
Damage to or dysfunction of the left PPC is associated with:

*   **Ideomotor Apraxia:** Impaired performance of learned, purposeful
    movements on command or imitation. Left inferior parietal and superior
    parietal lesions are specifically associated with apraxic deficits
    . The left PPC's praxis co-lateralization with language
    makes it a core node of the left-lateralized praxis system.
*   **Optic Ataxia (Contralateral):** Inaccurate visually guided reaching
    for the **right** hemifield / right hand, with worse performance when
    visual feedback of the limb is unavailable. This is a **contralateral**
    syndrome that occurs with lesions on either side (see the left BA7
    module).
*   **Impaired Categorical Spatial Judgment:** Difficulty with categorical
    spatial relationships (above/below, left/right), with preserved
    coordinate spatial processing.
*   **Impaired Limb-Position Monitoring:** Deficits in spatio-temporal
    binding and limb-position awareness, particularly in non-canonical
    postures.
*   **Impaired Mental Rotation of 180°-Rotated Stimuli:** Selective deficit
    in the verbal-strategy-dependent rotation task, with preserved
    performance on other rotation angles.

**What is NOT here:** **Hemispatial neglect**, **sustained spatial-attention
dominance**, and **body-schema dominance** are **right-lateralized**
functions of the right PPC. They do **not** occur with left PPC lesions. They
are documented in the right PPC module and are explicitly denied here (see
`Lateralization Notes`). A left PPC lesion does **not** produce neglect.

Lateralization Notes
--------------------
This is the **left** PPC module. The lateralization landscape is **parallel-
laden**: both PPCs carry substantial, non-overlapping lateralized functions
of approximately equal magnitude.

*   **Left-Lateralized Functions in the Left PPC:**
    - **Motor intention** — high-level movement planning[reference:22].
    - **Categorical spatial processing** — left PPC > right PPC
      [reference:23].
    - **Verbal-strategy mental rotation (180°)** — left-unique
      [reference:24].
    - **Praxis co-lateralization with language** — left PPC is part of the
      left-lateralized praxis network[reference:25].
    - **Episodic retrieval success effects (left IPS)** — strongly
      left-lateralized[reference:26].

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Sustained spatial attention over time** — right PPC dominant
      (see right PPC module).
    - **Hemispatial neglect** — right PPC dominant; left PPC lesions do not
      produce neglect.
    - **Body schema and internal body representation** — right PPC dominant
      (see right PPC module).
    - **Coordinate spatial processing** — right PPC > left PPC
      [reference:27].

*   **Symmetric Functions (bilateral properties of PPC):**
    - Reach and grasp sensorimotor transformation, with hemispace flipped
      (left PPC → right hemispace).
    - On-line feedback for goal-directed hand movements.
    - Spatio-temporal binding of limb events (bilateral, with left PPC
      emphasis on monitoring).
    - BA5/BA7 boundary criterion (unimodal vs. polymodal).

**A consumer that assumes "left PPC = symmetric" will miss the five
left-lateralized functions and will incorrectly import the right PPC's
neglect and spatial-attention claims.** The left and right PPC are
**parallel-laden**; neither is the "complement" of the other.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional region node, not a Brodmann aggregator.** This module
    represents the **PPC as a functional unit** (BA5 + BA7). It documents
    the division of labour between the two subfields and cross-references
    their Brodmann leaves; it does **not** duplicate their per-area content.
*   **BA5/BA7 boundary is the internal contract.** BA5 is **unimodal**
    somatosensory association cortex (VPL/VPM input stops at BA2/BA5; BA5
    remains somatosensory-dominant). BA7 is **polymodal** association
    cortex (visual + somatosensory + oculomotor; no obligate response to
    passive touch). Consumers that need subfield-level resolution should
    query the Brodmann leaves directly.
*   **Structural parity with right PPC.** Left and right PPC modules must
    be structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. **However** — exactly as for BA39/BA40 — both
    twins are heavily lateralized, on **different** functions. This module
    carries the **left-lateralized functions** (motor intention, categorical
    processing, verbal mental rotation, praxis co-lateralization, left-IPS
    retrieval). The right twin will carry the **right-lateralized
    functions** (sustained attention, neglect, body schema, coordinate
    processing). The two modules are structurally parallel but
    **content-divergent by design**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex import posterior_parietal_cortex

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.cortex.posterior_parietal_cortex"
    )

For Brodmann subfields (a **different** partition of the same territory),
query the sibling aggregator::

    from ...parietal.brodmann_areas import brodmann_area_5, brodmann_area_7
    # BA5 = anterior (unimodal); BA7 = posterior (polymodal)

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ppc_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.cortex.posterior_parietal_cortex"
        )
        # resolve ppc_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
    (BA5 and BA7 — the cytoarchitectonic subfields of PPC.)
*   **Motor intention:** Desmurget, M., et al. (2009). *Science*, 324(5928),
    811–813; event-related fMRI study of left parietal cortex and motor
    intention[reference:28].
*   **Categorical vs. coordinate spatial processing:** Kosslyn, S.M., et al.
    (1989). *J Cogn Neurosci*; parametric brain mapping study dissecting
    hemisphere-specific contributions to visual spatial imagery
    [reference:29].
*   **Mental rotation (180°):** *Differential effects of TMS of left and right
    PPC on mental rotation tasks* (2008), *ScienceDirect* — left PPC
    stimulation affected 180° rotation[reference:30].
*   **Spatio-temporal limb monitoring:** Ikegami, S., et al. — *Spatio-temporal
    updating in the left posterior parietal cortex*; left PPC activation
    during crossed-hands posture[reference:31].
*   **Episodic retrieval / left IPS:** *Left posterior parietal cortex
    participates in both task preparation and episodic retrieval* (2009),
    *NeuroImage* — left-lateralization of retrieval success effects
    [reference:32].
*   **Praxis–language co-lateralization:** Vingerhoets, G., et al. (2013).
    *Praxis and language are linked: evidence from co-lateralization in
    individuals with atypical language dominance*; left hemisphere changes
    during tool-use pantomiming in prefrontal, premotor, and posterior
    parietal regions[reference:33].
*   **Reaching and grasping:** *Neurophysiology of prehension. I. Posterior
    parietal cortex and object-oriented hand behaviors* (2007), *J
    Neurophysiol* — area 5 provides somesthetic information to AIP/7b-to-
    frontal grasping circuits; area 5 coordinates reach and grasp and
    provides on-line feedback[reference:35][reference:36].
*   **PPC as BA5 + BA7:** *Posterior Parietal Cortex* overview,
    *ScienceDirect* — PPC encompasses areas 5 and 7; AIP cells respond during
    visually guided grasping[reference:37].
*   **Apraxia and left parietal lesions:** *Search UW-Madison Libraries*
    (2025) — inferior parietal lobe associated with apraxic deficits
    .
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Brodmann areas 5 and 7 (left); FMA — left superior parietal
    lobule (PPC partonomy).
"""