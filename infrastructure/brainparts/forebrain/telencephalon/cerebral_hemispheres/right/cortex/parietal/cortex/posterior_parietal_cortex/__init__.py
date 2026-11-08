"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex.posterior_parietal_cortex
=========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── cortex
                        └── posterior_parietal_cortex   <-- THIS MODULE

**Primary synonym:** Posterior Parietal Cortex (PPC), right; Right PPC.
**Organizing principle:** **Functional–anatomical region**, the polymodal
association territory of the right parietal lobe.
**Brodmann constitution:** **BA5 + BA7** (plus the adjacent intraparietal
sulcus fields, functionally).
**Part of:** The **functional partition** of the right parietal lobe
(``.../parietal/cortex``), alongside S1 and S2.
**Cytoarchitectonic siblings:** ``.../parietal/brodmann_areas/brodmann_area_5``
and ``.../parietal/brodmann_areas/brodmann_area_7`` — the same territory,
partitioned differently. See "Two-Partition Context" below.

Overview
--------
The **right posterior parietal cortex (PPC)** is the polymodal association
territory of the right parietal lobe. It lies **caudal to the postcentral
sulcus**, encompasses **Brodmann areas 5 and 7**, and is the principal
cortical substrate for transforming sensory coordinates into **action-relevant
spatial and motor representations**. It is the first parietal territory where
somatosensation, proprioception, vision, and oculomotor signals converge.

The right PPC is **not** a single homogeneous area. It comprises two
functionally dissociable Brodmann fields with a clean internal boundary:

*   **BA5 (anterior PPC)** — unimodal somatosensory association cortex.
    Receives S1 input, performs proprioceptive and postural integration, and
    contributes to **sensorimotor guidance for reaching and grasping**.
*   **BA7 (posterior PPC)** — polymodal association cortex. Converges visual,
    somatosensory, and oculomotor signals; supports **visuomotor integration
    for reaching and grasping**, spatial transformation, and spatial working
    memory.

**This is the right PPC, and it is not the left PPC.** The right PPC carries
the **dominant substrate for sustained spatial attention and hemispatial
neglect**; the left PPC carries a **distinct, left-lateralized functional
profile** centred on **motor intention, categorical spatial processing,
praxis co-lateralization, and episodic retrieval**. The
left and right PPC are **parallel-laden** at the functional-region level: both
carry substantial, non-overlapping lateralized functions.

**Key right-lateralized characteristics of this module (documented in full
below):** the right PPC is critical for **sustaining attention to spatial
locations over time**; its inhibition produces **neglect-like rightward
visuospatial bias**; it is the dominant substrate for **coordinate spatial
processing** (precise metric distance); it is critical for **body schema and
postural representation**; and it exerts **strong inhibitory control over the
contralateral (left) PPC** via the posterior corpus callosum. These are
**not** mirrored on the left and must **not** be imported from the left twin.

Two-Partition Context
---------------------
This module is the **functional-region node** for the right PPC. It is
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

The **BA5/BA7 boundary** is the key internal distinction within the right PPC
(identical to the left PPC):

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
The right PPC is a **right-lateralized spatial-attention, spatial-processing,
and body-schema hub**. Its best-supported functions cluster into six domains:

*   **Sustaining Attention to Spatial Locations Over Time (Right-Lateralized —
    the principal right-PPC function):** The right PPC is **critical for
    maintaining attention to spatial locations over time**.
    Patients with right PPC lesions show a **vigilance decrement** specifically
    when attention must be maintained on spatial information (not verbal
    material), and lesioned voxels spanning the right intraparietal sulcus
    and inferior parietal lobe are significantly associated with this deficit
    [reference:0]. This function must be incorporated into models of normal
    parietal function and of hemispatial neglect[reference:1].

*   **Visuospatial Attention and Neglect (Right-Lateralized):** The right PPC
    is the dominant cortical substrate for **visuospatial attention**.
    Inhibitory TMS over the right PPC in healthy participants triggers a
    **significant rightward shift in the spatial allocation of visual
    attention**, temporarily mimicking the spatial deficits observed in
    neglect[reference:2]. Hemispatial neglect is predominant after a **right PPC
    stroke**[reference:3]. The right PPC exerts **strong inhibitory activity
    over the contralateral (left) PPC** via a short-latency transcallosal
    connection in the posterior corpus callosum; this interhemispheric
    inhibition asymmetry is a candidate neurophysiological basis for neglect
    [reference:4].

*   **Coordinate Spatial Processing (Right > Left):** The right PPC is
    preferentially engaged in **coordinate spatial processing** — precise
    metric distance and spatial relationships — as distinct from the
    **categorical spatial processing** (above/below, left/right) subserved by
    the left PPC. rTMS over the right PPC interferes with coordinate task
    performance, while left PPC stimulation primarily affects categorical
    tasks[reference:5].

*   **Body Schema and Postural Representation (Right-Lateralized):** The right
    PPC plays an important role in **maintaining an accurate and up-to-date
    representation of the current postural state of the body (the body
    schema)**[reference:6]. The superior parietal cortex, particularly the
    medial aspect (precuneus), shows increased activation during upper-limb
    posture changes and is the most likely location for damage leading to
    errors in visually guided reaching to non-foveated targets[reference:7].
    Right posterior parietal lesions can cause both positive symptoms
    (supernumerary limbs) and negative symptoms (disownership of a body part)
    [reference:8].

*   **Reaching and Grasping — On-Line Control:** The right PPC coordinates
    **reach and grasp behaviours** and provides **on-line control** needed for
    goal-directed hand movements. Beyond a role in movement planning, the PPC
    plays a major role in **on-line control of reach-to-grasp movements** —
    patients with PPC lesions can plan movements accurately but cannot amend
    ongoing movements when a target jumps unexpectedly[reference:9]. Hand
    manipulation neurons in the lateral PPC depend on **motor context**, not
    purely sensory or kinematic properties[reference:10].

*   **Processing Spatial Aspects of Complex Actions (Right-Lateralized):**
    Assessing the **spatial configuration of complex actions** differentially
    increases neural activity in the **right posterior parietal cortex**,
    suggesting a specific role of the right PPC in processing **spatial
    aspects of complex actions**[reference:11]. This is consistent with the
    right PPC's broader role in **visual-spatial judgments and orienting as
    well as reorienting**[reference:12].

Associated Disorders
--------------------
Damage to or dysfunction of the right PPC is associated with:

*   **Hemispatial Neglect (Left Neglect — Right-Lateralized):** Right PPC
    lesions are a classic cause of **left hemispatial neglect**. Inhibitory
    TMS over the right PPC produces neglect-like rightward visuospatial bias
    [reference:13]; right PPC stroke is the predominant cause of clinical neglect
    [reference:14].
*   **Vigilance Decrement for Spatial Information:** Impaired ability to
    sustain attention to spatial locations over time, with preserved
    performance for non-spatial (e.g., verbal) material[reference:15].
*   **Impaired Coordinate Spatial Judgment:** Difficulty with precise metric
    distance and coordinate spatial relationships, with preserved categorical
    spatial processing.
*   **Body Schema Disturbances:** Supernumerary limbs (positive symptoms),
    disownership of a body part (negative symptoms), and impaired postural
    representation[reference:16][reference:17].
*   **Impaired On-Line Movement Control:** Inability to amend ongoing
    reach-to-grasp movements when a target moves unexpectedly, despite intact
    movement planning[reference:18].

**What is NOT here:** **Motor intention** (high-level movement planning),
**categorical spatial processing**, **verbal-strategy mental rotation of
180°-rotated stimuli**, **praxis–language co-lateralization**, and
**left-IPS episodic retrieval** are **left-lateralized** functions of the left
PPC. They do **not** occur with right PPC lesions. They are documented in the
right PPC module and are explicitly denied here (see `Lateralization Notes`).
A right PPC lesion does **not** produce the left PPC's praxis or categorical
spatial deficits.

Lateralization Notes
--------------------
This is the **right** PPC module. The lateralization landscape is **parallel-
laden**: both PPCs carry substantial, non-overlapping lateralized functions
of approximately equal magnitude.

*   **Right-Lateralized Functions in the Right PPC (unique to this twin):**
    - **Sustaining attention to spatial locations over time** — right PPC
      critical[reference:19].
    - **Hemispatial neglect** — right PPC dominant; inhibition produces
      rightward bias[reference:20].
    - **Coordinate spatial processing** — right PPC > left PPC
      [reference:21].
    - **Body schema and postural representation** — right PPC important for
      up-to-date postural state[reference:22].
    - **Processing spatial aspects of complex actions** — right PPC
      differentially activated[reference:23].
    - **Interhemispheric inhibition of the left PPC** — right, but not left,
      PPC exerts strong inhibitory control over the contralateral homologue
      [reference:24].

*   **Left-Lateralized Functions (contrast — absent here):**
    - **Motor intention** — left PPC engaged in high-level movement planning
      (see left PPC module).
    - **Categorical spatial processing** — left PPC > right PPC
      [reference:25].
    - **Verbal-strategy mental rotation (180°)** — left PPC unique.
    - **Praxis–language co-lateralization** — left PPC part of left-
      lateralized praxis network.
    - **Left-IPS episodic retrieval** — left-lateralized.

*   **Symmetric Functions (bilateral properties of PPC):**
    - Reach and grasp sensorimotor transformation, with hemispace flipped
      (right PPC → left hemispace).
    - On-line control of goal-directed hand movements[reference:26].
    - BA5/BA7 boundary criterion (unimodal vs. polymodal).

**A consumer that assumes "right PPC = symmetric" will miss the six
right-lateralized functions and will incorrectly import the left PPC's motor
intention, categorical processing, verbal mental rotation, praxis, and
episodic retrieval claims.** The left and right PPC are **parallel-laden**;
neither is the "complement" of the other.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
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
*   **Structural parity with left PPC.** Left and right PPC modules must
    be structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. **However** — exactly as for BA39/BA40 — both
    twins are heavily lateralized, on **different** functions. This module
    carries the **right-lateralized functions** (sustained attention, neglect,
    coordinate processing, body schema, spatial aspects of complex actions,
    interhemispheric inhibition). The left twin carries the **left-lateralized
    functions** (motor intention, categorical processing, verbal mental
    rotation, praxis co-lateralization, left-IPS retrieval). The two modules
    are structurally parallel but **content-divergent by design**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex import posterior_parietal_cortex

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
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
*   **Sustained spatial attention:** Malhotra, P., et al. (2009). *Brain*,
    132(Pt 3), 645–660. "Role of right posterior parietal cortex in maintaining
    attention to spatial locations over time."[reference:27]
*   **Neglect-like bias from right PPC inhibition:** *Structural Organization
    of the Corpus Callosum Predicts Attentional Shifts after Continuous Theta
    Burst Stimulation* (2015), *J Neurosci* — rTMS over right PPC triggers
    rightward shift in spatial allocation of visual attention[reference:28].
*   **Coordinate spatial processing:** *Categorical and coordinate spatial
    processing in the imagery domain investigated by rTMS* (2006),
    *Neuropsychologia* — right parietal stimulation interferes with coordinate
    task; left with categorical[reference:29].
*   **Body schema:** *Parietal updating of limb posture: an event-related fMRI
    study* (2006), *Neuropsychologia* — PPC maintains up-to-date representation
    of postural state (body schema); superior parietal/precuneus activation
    [reference:30].
*   **On-line reach-to-grasp control:** *HAL TEI export* — PPC plays a major
    role in on-line control of reach-to-grasp movements beyond movement
    planning[reference:31].
*   **Interhemispheric inhibition asymmetry:** Koch, G., et al. (2011).
    *J Neurosci*, 31(24), 8967–8975. "Asymmetry of Parietal Interhemispheric
    Connections in Humans" — right, but not left, PPC exerts strong inhibitory
    activity over contralateral homologue via posterior corpus callosum
    [reference:32].
*   **Spatial aspects of complex actions:** *Processing the spatial
    configuration of complex actions involves right posterior parietal cortex*
    (2006), *Hum Brain Mapp* — right PPC differentially activated[reference:33].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Brodmann areas 5 and 7 (right); FMA — right superior parietal
    lobule (PPC partonomy).
"""