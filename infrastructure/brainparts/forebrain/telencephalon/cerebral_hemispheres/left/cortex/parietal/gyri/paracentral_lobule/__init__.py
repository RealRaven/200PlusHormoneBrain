"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri.paracentral_lobule
================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── gyri
                        └── paracentral_lobule   <-- THIS MODULE

**Primary synonym:** Paracentral lobule (left); Lobulus paracentralis;
PaCL; PCL.
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the medial surface of the hemisphere.
**Lobe membership:** **Frontal + parietal** — the only gyrus in the
parietal ``gyri/`` container that is **shared with another lobe**.
**Structural parent:** ``.../parietal/gyri/`` (parietal half only).
**Frontal twin:** ``.../frontal/gyri/paracentral_lobule/`` (if wired;
**not** documented here).

Overview
--------
The **left paracentral lobule (PaCL)** is a U-shaped gyrus on the
**medial surface** of the cerebral hemisphere. It is the **medial
continuation of the precentral and postcentral gyri**, bridging them
across the medial extension of the central sulcus. The central sulcus
continues onto the medial surface and divides the lobule into two
functionally distinct halves:

*   **Anterior half (anterior two-thirds)** — the **medial extension of
    the precentral gyrus**, corresponding to **Brodmann area 4 (BA4)**,
    the primary motor cortex. Contains the **leg, foot, and perineal
    representations** of the motor homunculus.
*   **Posterior half (posterior third)** — the **medial extension of the
    postcentral gyrus**, corresponding to **Brodmann areas 3, 1, and 2**
    (and, most inferiorly, part of BA5). Contains the **leg, foot, and
    perineal representations** of the sensory homunculus.

**The paracentral lobule is the only gyrus in the parietal ``gyri/``
container that belongs to two lobes.** Its anterior half is **frontal**
(BA4); its posterior half is **parietal** (BA3/1/2). This module documents
the **parietal half** only. A complete structural query for the
paracentral lobule must iterate **both** this module and
``.../frontal/gyri/paracentral_lobule``.

**This is the definitive "shared gyrus" case in the brainparts tree.**
The gyral partition is structural, and the structural boundary of the
paracentral lobule does **not** align with the lobar boundary between the
frontal and parietal lobes. The gyrus is a single macroscopic entity; the
lobar boundary runs through it.

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. It is
**not** a functional region and **not** a cytoarchitectonic field. Its
contents span **both** of those partitions:

::

    Structural leaf (this module)        Functional / cytoarchitectonic contents
    ─────────────────────────────        ────────────────────────────────────────
    paracentral_lobule (parietal half) ──▶  medial S1 (leg/foot/perineum)
                                        ──▶  BA3, BA1, BA2 (posterior third)
                                        ──▶  BA5 (most inferior part)

    paracentral_lobule (frontal half)  ──▶  medial M1 (leg/foot/perineum)
    [NOT this module]                   ──▶  BA4 (anterior two-thirds)
                                        ──▶  SMA-adjacent cortex (rostrally)

**Consumers must not assume that ``paracentral_lobule`` (parietal) is the
whole paracentral lobule.** It is the **posterior (parietal) half**. The
anterior (frontal) half is a separate module under ``frontal/gyri/``.

Function in the Human Brain
---------------------------
The **parietal half** of the left paracentral lobule is the **medial
somatosensory representation of the contralateral lower limb and
perineum**. Its best-supported functions cluster into four domains:

*   **Somatosensory Representation of the Contralateral Leg and Foot
    (medial S1):** The posterior part of the paracentral lobule contains
    the **leg and foot representations** of the primary somatosensory
    cortex. It is the medial continuation of the postcentral
    gyrus, and the foot sensory area occupies the **posterior
    paracentral lobule**. Somatotopically, the **foot** is
    represented posteriorly, and the **genitalia** are represented
    **anterior** to the foot sensory area.

*   **Somatosensory Representation of the Perineum:** The paracentral
    lobule contains the **perineal representations** of both the motor
    and sensory homunculi. This is the
    cortical territory most directly concerned with **sensation from the
    perineum and lower pelvic floor**.

*   **Proprioception and Sensorimotor Integration of the Lower Limb:** The
    parietal half contributes to **proprioceptive processing and
    sensorimotor integration** for the lower limb, consistent with the
    broader role of S1 in discriminative touch, proprioception, and
    nociception (documented in the S1 functional-region module).

*   **Cortical Control of Micturition and Defecation (Bilateral
    Contribution):** The paracentral lobule as a whole — **both halves,
    both hemispheres** — contributes to the **cortical control of
    micturition and defecation**. The **parietal half** provides the
    sensory representation of bladder and bowel fullness; the
    **frontal half** provides the motor/executive control. The
    paracentral lobule is sometimes described as the
    **"cortical center of defecation and micturition"**, and it exerts an
    **inhibitory influence** on the sacral micturition center
    .

Associated Disorders
--------------------
Damage to or dysfunction of the **left** paracentral lobule (parietal
half, and often the frontal half as well, given the shared vascular
territory) is associated with:

*   **Contralateral Lower-Limb Sensory Disturbance:** Numbness,
    paresthesia, or impaired proprioception in the **right** leg and foot.
    The paracentral lobule is the cortical representation for
    contralateral lower-limb motor and sensory function.
*   **Contralateral Lower-Limb Weakness (Monoparesis / Paraparesis,
    when frontal half is also involved):** Leg-predominant weakness,
    often with relative sparing of the face and upper limb — the
    signature of an **anterior cerebral artery (ACA)** territory
    infarct.
*   **Urinary Urgency and Incontinence:** Disruption of the paracentral
    lobule's inhibitory control over micturition can produce **urinary
    urgency, frequency, and urge incontinence**. Lesions may
    not produce incontinence unless **both** lobules are involved
    , consistent with bilateral cortical control.
*   **Gait Disturbance:** Difficulty with gait initiation and
    leg-predominant motor impairment, often accompanying the
    sensory and sphincter deficits.

**What is NOT here:** The **motor** (frontal-half) deficits are
documented under ``.../frontal/gyri/paracentral_lobule`` (if wired), not
here. The **parietal half** is the **sensory** half; the **frontal half**
is the **motor** half. A complete lesion through the whole lobule (e.g.,
ACA infarct) produces **both** — but this module documents the **sensory**
component only.

Lateralization Notes
--------------------
This is the **left** paracentral lobule (parietal half). The lateralization
landscape is **weakly left-weighted at the structural level**, with
**functional laterality remaining largely symmetric**:

*   **Structural Asymmetry (left > right):** The **left paracentral
    lobule has a larger mean surface area than the right** in both males
    and females. Morphometric studies report left PCL ≈ 10.67 cm² vs.
    right ≈ 8.80 cm² in males, and left ≈ 8.80 cm² vs. right ≈ 6.99 cm²
    in females. The paracentral lobule is also described as
    **"remarkably asymmetric"** in cortical grey-matter analyses.
    This structural asymmetry corresponds to the predominance of
    right-handedness (90–95% of the population).

*   **Functional Symmetry (contralateral representation):** The **sensory
    representation** is **contralateral** and **symmetric** at the
    functional level:
    - **Left parietal half** → sensory representation of the **right**
      leg, foot, and perineum.
    - **Right parietal half** → sensory representation of the **left**
      leg, foot, and perineum.

*   **Bilateral Control of Micturition/Defecation:** The cortical control
    of bladder and bowel function is **bilateral** — both paracentral
    lobules contribute. Unilateral lesions may produce urgency but
    **incontinence may require bilateral involvement**.

*   **No Neglect, No Praxis, No Language Role:** The paracentral lobule is
    **not** part of the spatial-attention/neglect network, the praxis
    network, or the language network. Do not import claims from BA39,
    BA40, PPC, or S1/BA1–BA2 that belong to those modules.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../frontal/gyri/paracentral_lobule``. The frontal half is a
    **separate module**, and consumers that need the whole gyrus must
    query both lobes explicitly.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Parietal half only.** This module documents the **posterior
    (sensory) half** of the paracentral lobule. The **anterior (motor)
    half** is documented under the frontal lobe. **Do not** document BA4
    or motor functions here.
*   **Shared-gyrus caveat is the defining contract.** The paracentral
    lobule is the **only gyrus in the parietal ``gyri/`` container that is
    shared with another lobe**. Consumers must not assume that
    ``parietal.gyri.paracentral_lobule`` covers the whole gyrus.
*   **Structural parity with right paracentral lobule.** Left and right
    parietal-half modules must be structurally interchangeable so
    bilateral consumers can iterate hemispheres generically. The
    functional contents (medial S1 for the contralateral leg/foot/perineum)
    are **symmetric**; only the structural-size prose (left > right) and
    the contralateral target differ.

Usage
-----
Resolve by path (parietal half only)::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri import paracentral_lobule

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.gyri.paracentral_lobule"
    )

**For the full paracentral lobule, query both lobes:** ::

    from ...parietal.gyri import paracentral_lobule as parietal_half
    from ...frontal.gyri import paracentral_lobule as frontal_half
    # parietal_half = sensory; frontal_half = motor

Bilateral iteration (parietal halves only)::

    for side in ("left", "right"):
        pcl_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.gyri.paracentral_lobule"
        )
        # resolve pcl_path through the memory/recall layer

References
----------
*   **Paracentral lobule overview:** *Dorsomedial Motor Region: Paracentral
    Lobule and the Supplementary Motor Region* (ScienceDirect). The
    paracentral lobule is the medial extension of the precentral motor
    region and the postcentral somatosensory region; it consists of the
    medial extensions of the precentral and postcentral gyri where the leg
    region is represented[reference:0].
*   **Somatotopy:** *Epilepsy Syndrome Seizure Ontology — Paracentral
    Lobule* (BioPortal, 2015). The paracentral lobule includes the primary
    motor and somatosensory areas for the **leg and foot** and is important
    in the control of voluntary movements and the localization and
    perception of somatosensory stimuli in the leg and foot[reference:1].
    Foot sensory area occupies the **posterior paracentral lobule**; the
    genitalia are represented **anterior** to the foot sensory area
    [reference:2].
*   **Cytoarchitecture:** *Structural Morphology Of The Brodmann Areas In
    Medial View* (SciePro). Area 4 lies **anterior** to the central sulcus
    and areas **3, 1, and 2** lie posteriorly[reference:3]. Also: *Anatomy
    Master* — anterior portion = BA4 (primary motor); posterior portion =
    BA3/1/2 (primary somatosensory)[reference:4].
*   **Morphometry and morphology:** *Morphology and Morphometry of Human
    Paracentral Lobule: An Anatomical Study with its Application in
    Neurosurgery* (2021), *Asian J Neurosurg*, 16(2), 349–354. Three
    morphological types (continuous 2%, partially segmented 91%, completely
    segmented 7%). **Left PCL significantly larger than right** (males:
    left 10.67 cm² vs. right 8.80 cm²; females: left 8.80 cm² vs. right
    6.99 cm²). Motor area significantly larger than sensory area
    [reference:5].
*   **Vascular territory and clinical syndrome:** *A Medial View Of The
    Paracentral Lobule Of The Brain* (SciePro). Lesions in this
    parasagittal territory often present with **contralateral lower-limb
    weakness, altered proprioception, and gait disturbance** rather than
    face or hand findings. **Anterior cerebral artery** infarction,
    parasagittal meningioma, or cortical venous thrombosis along the
    superior sagittal sinus can involve this cortex; associated **urinary
    urgency or incontinence**[reference:6]. Also: *The Anatomy Of The
    Paracentral Lobule Of The Human Brain* (SciePro) — medial location
    tracks closely with the **ACA territory**, where infarcts present with
    **leg-predominant weakness and sensory loss**[reference:7].
*   **Micturition control:** *Disturbances of Micturition Observed in Some
    Patients with Brain Tumor* (2007). The paracentral lobule seems to have
    an **inhibitory function** on the sacral micturition center;
    incontinence may not appear unless **both lobules are invaded**
    [reference:8]. Also: *White matter of paracentral lobule* (Ontosight) —
    lesions can result in **urinary incontinence** due to disruption of
    nerve pathways controlling these functions[reference:9].
*   **Radiopaedia:** *Paracentral lobule* (2024), rID 39075. Located on the
    **medial surface**, includes parts of **both frontal and parietal
    lobes**; medial continuation of precentral and postcentral gyri; motor
    and sensory functions related to the **lower limb**[reference:10].
*   **Structural asymmetry:** *Hemispheric asymmetries in cortical grey
    matter of gyri and sulci* (2024), *Am J Biol Anthropol*. The
    paracentral lobule was **remarkably asymmetric**[reference:11].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed. (Medial-surface gyral anatomy.)
*   Terminologia Anatomica (FIPAT, 2019) — lobulus paracentralis.
*   NeuroNames — Paracentral lobule (left); FMA — left paracentral lobule
    (parietal part).
"""