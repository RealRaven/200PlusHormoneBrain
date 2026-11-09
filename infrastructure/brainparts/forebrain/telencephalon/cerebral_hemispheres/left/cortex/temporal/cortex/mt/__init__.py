"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex.mt
====================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── temporal
                    └── cortex
                        └── mt                   <-- THIS MODULE

**Primary synonym:** Middle temporal visual area (MT), left; **V5**;
Human MT/V5 (hMT/V5); Middle temporal area.
**Organizing principle:** **Functional–anatomical region** — the
motion-processing hub of the dorsal visual stream.
**Brodmann constitution:** **BA19** — the **occipital** association
area. MT/V5 occupies the **temporo-parieto-occipital pit** at the
boundaries of **Brodmann areas 19 and 37** (and, in some atlases, the
posterior bank of the superior temporal sulcus). The tree's
`brodmann_areas` partition wires **BA19 under the occipital partition**,
**not** the temporal partition. See "Cross-Lobe Mapping" below.
**Location:** The **lateral occipitotemporal cortex**, at the junction
of the **temporal, parietal, and occipital lobes**, typically in the
**posterior bank of the inferior temporal sulcus / superior temporal
sulcus**.
**Structural parent:** Child of ``.../temporal/cortex`` (the functional
partition of the temporal lobe). **MT is the first functional region in
the temporal cortex partition whose primary Brodmann anchor lives in a
different lobe's Brodmann partition.**
**Cytoarchitectonic type:** **Neocortical (granular)** — MT is a
**heavily myelinated, granular koniocortex-like field**, with a
distinctly **dense layer IV** and **large layer III pyramidal cells**.

Overview
--------
The **left middle temporal visual area (MT, or V5)** is the **principal
cortical substrate for visual motion processing** in the human brain.
It is the **first extrastriate area with predominantly motion-selective
responses**, and its neurons are **selective for both the direction and
the speed of moving stimuli**. It sits at the **heart of the dorsal
visual "where/how" pathway**, receiving input from V1 and projecting
forward to MST and the posterior parietal cortex to support **motion
perception, motion-in-depth, structure-from-motion, and visually guided
action**.

**MT is the first functional region in the tree whose primary Brodmann
anchor lives in a different lobe's Brodmann partition.** The tree's
`brodmann_areas` partition wires **BA19 under the occipital lobe**, not
the temporal lobe. A consumer that iterates
``temporal.brodmann_areas.ITERABLE_AREAS`` will **not** see BA19 — they
must query ``occipital.brodmann_areas`` separately. This makes MT the
**first "cross-lobe functional region" in the temporal cortex partition**
— the temporal cortex aggregator flagged the cross-lobe mapping, and
this module **instantiates it**.

**MT is strongly right-lateralized for motion processing.** Unlike the
ATL (left-verbal / right-non-verbal) or the ITC (left-verbal / right-
affective), MT's lateralization is a **sensory-domain weighting**, not a
**semantic-domain split**. The **right MT/V5+** is the dominant
hemisphere for **translational motion across the full visual field**:
TMS over **right MT** disrupts motion perception in **both contra- and
ipsi-lateral hemifields**, whereas TMS over **left MT** disrupts motion
perception only in the **contra-lateral hemifield**. This is
the **clearest sensory-domain lateralization** in the tree so far.

Cross-Lobe Mapping
------------------
MT is the **first functional region in the tree whose primary Brodmann
anchor is in a different lobe's partition**:

::

    Functional region (this module)     Brodmann mapping      Brodmann partition
    ───────────────────────────────     ─────────────────      ──────────────────
    mt                              ──▶  BA19 (V5/MT)       **occipital** (not temporal)
                                    ──▶  BA37 (boundary)    temporal (partially)

**Consumers must not assume that the temporal functional partition maps
1:1 onto the temporal Brodmann partition.** MT is the **counterexample**:
its primary cytoarchitectonic anchor (BA19) lives under the **occipital**
partition, and its secondary anchor (BA37) lives under the **temporal**
partition. This is **not a bug** — it is a faithful reflection of the
fact that **MT sits at the junction of the temporal, parietal, and
occipital lobes**, and Brodmann grouped it with the occipital
association cortex.

**Resolution contract for consumers:**

*   If you need **MT as a functional region**, use this module.
*   If you need **BA19 as a cytoarchitectonic field**, query
    ``occipital.brodmann_areas.brodmann_area_19``.
*   If you need **BA37 as a cytoarchitectonic field** (the temporal
    boundary of MT), query
    ``temporal.brodmann_areas.brodmann_area_37``.
*   **Do not** assume that a temporal Brodmann query will return MT's
    primary cytoarchitectonic anchor. It will not.

Cytoarchitecture
----------------
MT is **neocortical and granular** — a **heavily myelinated** field
with a **distinctly dense layer IV** and **large layer III pyramidal
cells**:

*   **Heavily myelinated** — a **very heavily myelinated region stands
    out in the lateral part of area 19, near the occipito-temporal
    junction** — this is MT/V5. Myeloarchitecture is
    the **most reliable marker** for MT in histological and (increasingly)
    in vivo neuroimaging studies.

*   **Dense layer IV (granular)** — MT is a **granular koniocortex-like
    field**, with a **prominent layer IV** and a **high cell-packing
    density**, consistent with its role as a **primary-like motion
    processor** receiving direct V1 input.

*   **Large layer III pyramidal cells** — the **output neurons** to MST
    and the posterior parietal cortex are **large layer III pyramidal
    cells**, characteristic of a **feed-forward extrastriate area**.

*   **Columnar organization** — MT neurons are **organized in columns or
    clusters** by **direction preference and binocular disparity**,
    the **first extrastriate area** where columnar organization for
    motion is clearly demonstrated.

**This granular, heavily myelinated architecture is the defining
structural fact about MT.** Unlike the paleocortical olfactory cortex
(3 layers) or the transitional perirhinal/entorhinal fields (4–6 layers
with variable IV), MT is a **fully neocortical, granular sensory area**
— the **first such area documented in the temporal functional
partition**.

Function in the Human Brain
---------------------------
The left MT is a **left-hemisphere motion-processing hub**, with a
**right-hemisphere-dominant partner**. Its best-supported functions
cluster into six domains:

*   **Visual Motion Processing (the defining function, bilateral with
    right dominance):** MT is the **main extrastriate region with
    predominantly motion-selective responses**. Its neurons are
    **selective for both the direction and the speed** of moving
    signals. This is the **bilateral foundation** of motion
    perception.

*   **Direction Selectivity and Motion Integration (bilateral):** MT
    neurons show **strong direction selectivity** and play a
    **critical role in suppressing ambiguous motion information**
    (e.g., the aperture problem). MT integrates **local motion
    signals** from V1 into **coherent global motion percepts**.

*   **Structure-from-Motion and Motion-in-Depth (right-dominant):** The
    **human MT/V5+ is part of a network with right hemisphere dominance
    involved in extracting depth from motion**. MT/V5 is
    **significantly more active when subjects view 3D (as opposed to
    2D) displays**, supporting **structure-from-motion** and
    **motion-in-depth**.

*   **Full-Field Translational Motion (right-dominant):** TMS over
    **right MT** disrupts translational motion perception in **both
    contra- and ipsi-lateral visual fields**, whereas TMS over **left
    MT** disrupts motion perception only in the **contra-lateral
    field**. This suggests an **enhanced role for the right
    hemisphere in processing translational motion across the full visual
    field**.

*   **Multisensory Motion Processing (bilateral):** MT/V5 is
    **motion-selective across the senses** — it responds not only to
    **visual motion** but also to **tactile and auditory motion
    information**. This makes MT a **multisensory motion hub**,
    not a purely visual area.

*   **Visually Guided Action (bilateral, with right dominance):** MT
    projects to **MST** (optic flow, heading perception) and to the
    **posterior parietal cortex** (visually guided action). The
    **right-hemisphere dominance** for full-field motion supports
    **heading perception** and **visually guided locomotion**.

Associated Disorders
--------------------
Damage to or dysfunction of the left MT is associated with:

*   **Akinetopsia (Bilateral Lesions — the signature MT syndrome):**
    **Cerebral akinetopsia** is the **inability to perceive visual
    motion** — a moving object appears to "jump" from one stationary
    position to another. It follows **bilateral lesions of the V5/V5A
    complex**. The **landmark case of patient LM** had
    **bilateral extrastriate lesions** from venous infarcts and was
    unable to see objects in motion.

*   **Hemiakinetopsia (Unilateral Lesions):** **Unilateral MT/V5
    lesions** are **more common but cause milder, asymptomatic
    deficits**; **hemiakinetopsia** (motion blindness in one hemifield)
    can occur when damage is confined to specific parts of the MT/V5
    complex. **Lesions of MT (V5) produce a relatively selective
    deficit for motion perception in the contralateral visual
    hemifield**, which **recovers within a few weeks** depending on the
    extent of the lesion and white matter involvement.

*   **Impaired Structure-from-Motion and Kinetic Depth (Bilateral):**
    **Defective smooth pursuit eye movements** and **impaired
    identification of objects defined by movement cues** (structure-
    from-motion or kinetic depth) follow MT/MST lesions.

*   **Motion Perception Auras in Epilepsy (Right-Emphasis):**
    **Epileptic activity in MT/V5** can elicit **motion perception
    auras** — e.g., a percept of **colorless fog moving from peripheral
    vision** and stopping abruptly in the midline. **Akinetopsia
    can also occur as an epileptic seizure**, arising from
    **hyperexcitability of the right temporal and parietal cortices,
    including area MT/V5**.

**What is NOT here:** **Akinetopsia** is a **bilateral MT/V5** syndrome,
not a **left-hemisphere-specific** syndrome. The **left MT alone** does
not produce clinical akinetopsia — the **right MT** and **bilateral
MT/V5** are the critical substrates. **Anomia**, **semantic dementia**,
and **prosopagnosia** are **not** MT syndromes — they belong to the
ATL, ITC, and pITC modules.

Lateralization Notes
--------------------
This is the **left** MT module. The lateralization landscape is
**right-dominant for full-field motion** — a **sensory-domain
weighting**, not a semantic-domain split:

*   **Right-Lateralized Functions (dominant in the right twin):**
    - **Full-field translational motion** — right MT TMS disrupts motion
      in **both hemifields**.
    - **Structure-from-motion and motion-in-depth** — right MT/V5+ is
      part of a **right-dominant network** for depth-from-motion.

*   **Left-Lateralized Functions (present in this twin, but not
    dominant):**
    - **Contra-lateral motion processing** — left MT TMS disrupts motion
      only in the **right visual field**.
    - **Local motion integration** — left MT contributes to the **local
      sensory input** that is integrated into global motion by the
      right-hemisphere network.

*   **Symmetric Functions (bilateral properties of MT):**
    - Direction selectivity and speed tuning.
    - Motion integration and aperture-problem solving.
    - Multisensory motion processing (visual, tactile, auditory).
    - Visually guided action (via MST and PPC).

**This is the "right-dominant sensory weighting" pattern** — the
**first sensory-domain lateralization** in the temporal functional
partition. Unlike the ATL (left-verbal / right-non-verbal) and the ITC
(left-verbal / right-affective), MT's lateralization is **not a division
of cognitive labor** but a **hemispheric weighting for a single sensory
domain** (motion). The **right hemisphere is the dominant motion
processor**; the left hemisphere is the **contra-lateral specialist**.

**A consumer that assumes "left MT = right MT" will miss the right-
lateralized full-field motion and structure-from-motion functions** —
but the left twin is **not** merely "denying" a right-hemisphere claim;
it is **carrying a contra-lateral subset** of the motion-processing
function. This is qualitatively different from the denial-based patterns
of S1 and from the parallel-laden pattern of BA37.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    occipital lobe (BA19, V1) or the parietal lobe (MST, PPC). Those are
    **downstream/upstream targets** and **cross-lobe Brodmann anchors**,
    not structural parents.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cross-lobe Brodmann mapping — flagged in prose and data.** MT's
    primary Brodmann anchor (BA19) lives under the **occipital**
    partition. The ``BRODMANN_PARTITION`` constant is **"occipital"**;
    the ``CROSS_PARTITION_AREAS`` constant in the parent temporal cortex
    aggregator records MT → occipital.
*   **Neocortical granular type — flagged in data.** MT is **neocortical
    and granular**, not paleocortical or transitional. The
    ``CYTOARCHITECTONIC_TYPE`` constant is **"neocortical_granular"**.
*   **Right-dominant sensory weighting — flagged in data.** The
    ``RIGHT_DOMINANT`` constant documents the right-hemisphere
    dominance for full-field motion.
*   **Functional-region leaf, not a Brodmann leaf.** MT is a
    **functional region** that maps to BA19 (occipital) and BA37
    (temporal). It is **not** a Brodmann leaf — the Brodmann leaves are
    under ``occipital.brodmann_areas`` and ``temporal.brodmann_areas``.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.temporal.cortex import mt

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "temporal.cortex.mt"
    )

**MT's primary Brodmann anchor (BA19) lives under the occipital
partition.** Use the `BRODMANN_PARTITION` constant to check::

    from ...temporal.cortex.mt import BRODMANN_PARTITION
    # BRODMANN_PARTITION = "occipital"

For BA19 as a cytoarchitectonic field::

    from ...occipital.brodmann_areas import brodmann_area_19

For the right-dominant motion functions::

    from ...temporal.cortex.mt import RIGHT_DOMINANT
    # RIGHT_DOMINANT = ("full_field_translational_motion",
    #                   "structure_from_motion",
    #                   "motion_in_depth")

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mt_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"temporal.cortex.mt"
        )
        # resolve mt_path through the memory/recall layer

References
----------
*   **MT/V5 as the motion-processing hub:** *Motion Perception — an
    overview* (ScienceDirect). V5, also known as MT, is the **main
    extrastriate region with predominantly motion-selective
    responses**; its neurons are selective for both the **direction and
    the speed** of moving signals; adjacent to MT is **MST/V5a**, which
    has more complex motion responses.
*   **MT cytoarchitecture and myeloarchitecture:** *Occipital cortex in
    man: organization of callosal connections, related myelo- and
    cytoarchitecture* (1990), *J Comp Neurol*, 298(2), 188–214. A
    **very heavily myelinated region stands out in the lateral part of
    area 19, near the occipito-temporal junction** — this is MT/V5
    .
*   **MT/V5 location at BA19/BA37 boundary:** *The contribution of LM to
    the neuroscience of movement vision* (2015), PMC. Area V5/MT and its
    surroundings occupy the **temporo-parieto-occipital pit at the
    boundaries of Brodmann areas 19 and 37**.
*   **Right-hemisphere dominance for full-field motion:** *An enhanced
    role for right hV5/MT+ in the analysis of motion in the contra- and
    ipsi-lateral visual hemi-fields* (2019), *Behav Brain Res*,
    S0166432819302062. TMS over **right MT** disrupts translational
    motion in **both contra- and ipsi-lateral visual fields**; TMS over
    **left MT** disrupts motion only in the **contra-lateral field**
    .
*   **Right-hemisphere dominance for depth-from-motion:** Orban, G.A.,
    et al. (1999). "Human cortical regions involved in extracting depth
    from motion." *Neuron*, 24(4), 929–940. PMID 10624956. Human MT/V5+
    is part of a network with **right hemisphere dominance** involved in
    extracting **depth from motion**.
*   **Akinetopsia and bilateral MT/V5 lesions:** *Akinetopsia — an
    overview* (ScienceDirect). Akinetopsia is the **inability to detect
    motion** following **bilateral cortical lesions outside the striate
    cortex**; **unilateral MT/V5 lesions** cause **milder asymptomatic
    deficits**; **lesions of MT (V5) produce a relatively selective
    deficit for motion perception in the contralateral visual
    hemifield** that **recovers within a few weeks**.
*   **Akinetopsia as epileptic seizure (right MT/V5):** *Akinetopsia as
    epileptic seizure* (2013), *Epilepsy Behav Case Rep*. Akinetopsia
    can occur as an **epileptic seizure** arising from
    **hyperexcitability of the right temporal and parietal cortices,
    including area MT/V5**.
*   **MT multisensory motion processing:** *Aligned motion-direction
    information for touch and vision in the human brain* (2015),
    *hal.science*. In addition to processing **visual motion signals**,
    **hMT+/V5 selectively responds to tactile as well as auditory motion
    information**; hMT/V5 is **tactile motion selective**
    .
*   **MT retinotopy:** *The Retinotopic Organization of the Human Middle
    Temporal Area MT/V5 and Its Cortical Neighbors* (2010), *J Neurosci*.
    MT/V5 has a **coarse retinotopic organization** and is bordered by
    **pMSTv, pFST, and pV4t**; the **MT/V5 cluster forms a complete
    retinotopic circle**.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human
    Brain*, 4th ed. (Lateral occipitotemporal anatomy.)
*   NeuroNames — Middle temporal area (left); FMA — left MT/V5 partonomy.
"""