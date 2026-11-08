"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.gyri.paracentral_lobule
=================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── gyri
                        └── paracentral_lobule   <-- THIS MODULE

**Primary synonym:** Paracentral lobule (right); Lobulus paracentralis;
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
The **right paracentral lobule (PaCL)** is a U-shaped gyrus on the
**medial surface** of the right cerebral hemisphere. It is the **medial
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
    perineal representations** of the sensory homunculus[reference:0].

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

**Consumers must not assume that ``paracentral_lobule`` (parietal) is the
whole paracentral lobule.** It is the **posterior (parietal) half**. The
anterior (frontal) half is a separate module under ``frontal/gyri/``.

Function in the Human Brain
---------------------------
The **parietal half** of the right paracentral lobule is the **medial
somatosensory representation of the contralateral (left) lower limb and
perineum**. Its best-supported functions cluster into four domains:

*   **Somatosensory Representation of the Contralateral (Left) Leg and
    Foot (medial S1):** The posterior part of the paracentral lobule
    contains the **leg and foot representations** of the primary
    somatosensory cortex[reference:1]. It is the medial continuation of
    the postcentral gyrus, and the foot sensory area occupies the
    **posterior paracentral lobule**[reference:2]. On the **right** side,
    this representation is of the **left** leg and foot.

*   **Somatosensory Representation of the Perineum:** The paracentral
    lobule contains the **perineal representations** of the sensory
    homunculus[reference:3]. This is the cortical territory most directly
    concerned with **sensation from the perineum and lower pelvic floor**.

*   **Proprioception and Sensorimotor Integration of the Lower Limb:** The
    parietal half contributes to **proprioceptive processing and
    sensorimotor integration** for the lower limb, consistent with the
    broader role of S1 in discriminative touch, proprioception, and
    nociception.

*   **Cortical Control of Micturition and Defecation (Bilateral
    Contribution):** The paracentral lobule as a whole — **both halves,
    both hemispheres** — contributes to the **cortical control of
    micturition and defecation**[reference:4]. The **parietal half**
    provides the sensory representation of bladder and bowel fullness;
    the **frontal half** provides the motor/executive control. The
    paracentral lobule is sometimes described as the **"cortical center
    of defecation and micturition"**, and it exerts an **inhibitory
    influence** on the sacral micturition center[reference:5].

Associated Disorders
--------------------
Damage to or dysfunction of the **right** paracentral lobule (parietal
half, and often the frontal half as well, given the shared vascular
territory) is associated with:

*   **Contralateral (Left) Lower-Limb Sensory Disturbance:** Numbness,
    paresthesia, or impaired proprioception in the **left** leg and foot.
    Lesions in this parasagittal territory often present with altered
    proprioception and gait disturbance rather than face or hand
    findings[reference:6].

*   **Contralateral (Left) Lower-Limb Weakness (when frontal half is also
    involved):** Leg-predominant weakness, often with relative sparing of
    the face and upper limb — the signature of an **anterior cerebral
    artery (ACA)** territory infarct[reference:7].

*   **Urinary Urgency and Incontinence:** Disruption of the paracentral
    lobule's inhibitory control over micturition can produce **urinary
    urgency, frequency, and urge incontinence**[reference:8][reference:9].
    Lesions may not produce incontinence unless **both** lobules are
    involved, consistent with bilateral cortical control.

*   **Gait Disturbance:** Difficulty with gait initiation and
    leg-predominant motor impairment, often accompanying the sensory and
    sphincter deficits[reference:10].

**What is NOT here:** The **motor** (frontal-half) deficits are
documented under ``.../frontal/gyri/paracentral_lobule`` (if wired), not
here. The **parietal half** is the **sensory** half; the **frontal half**
is the **motor** half. A complete lesion through the whole lobule (e.g.,
ACA infarct) produces **both** — but this module documents the **sensory**
component only.

Lateralization Notes
--------------------
This is the **right** paracentral lobule (parietal half). The
lateralization landscape is **weakly left-weighted at the structural
level**, with **functional laterality remaining largely symmetric**:

*   **Structural Asymmetry (left > right in surface area):** The **left
    paracentral lobule has a larger mean extrasulcal surface area than the
    right** in both sexes. Morphometric studies report left PCL ≈ 10.67
    cm² vs. right ≈ 8.80 cm² in males, and left ≈ 8.80 cm² vs. right ≈
    6.99 cm² in females[reference:11][reference:12]. A separate study
    reports left ≈ 6.79 cm² vs. right ≈ 5.76 cm² in males and left ≈ 6.05
    cm² vs. right ≈ 5.16 cm² in females[reference:13]. The leftward
    asymmetry is consistent across studies, regardless of absolute
    measurements.

*   **A Note on Sensory-Area Width:** One morphometric study reports that
    the **maximum width of the sensory area was significantly higher in
    the right paracentral lobule** in both males and females[reference:14].
    This suggests that while the **overall** PCL surface is left-larger,
    the **sensory subdivision** may be relatively wider on the right —
    a subtle structural dissociation that consumers should note but not
    over-interpret.

*   **Functional Symmetry (contralateral representation):** The **sensory
    representation** is **contralateral** and **symmetric** at the
    functional level:
    - **Right parietal half** → sensory representation of the **left**
      leg, foot, and perineum.
    - **Left parietal half** → sensory representation of the **right**
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
*   **No cross-hemisphere imports.** Right side only.
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
*   **Structural parity with left paracentral lobule.** Left and right
    parietal-half modules must be structurally interchangeable so
    bilateral consumers can iterate hemispheres generically. The
    functional contents (medial S1 for the contralateral leg/foot/perineum)
    are **symmetric**; only the structural-size prose (right < left) and
    the contralateral target differ.

Usage
-----
Resolve by path (parietal half only)::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.gyri import paracentral_lobule

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
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
*   **Paracentral lobule overview and somatotopy:** *Dorsomedial Motor
    Region: Paracentral Lobule and the Supplementary Motor Region*
    (ScienceDirect); *Epilepsy Syndrome Seizure Ontology — Paracentral
    Lobule* (BioPortal, 2015). The paracentral lobule includes the primary
    motor and somatosensory areas for the **leg and foot**; foot sensory
    area occupies the **posterior paracentral lobule**[reference:15][reference:16].
*   **Morphometry — left > right surface area:** *Morphology and
    Morphometry of Human Paracentral Lobule: An Anatomical Study with its
    Application in Neurosurgery* (2021), *Asian J Neurosurg*, 16(2),
    349–354. Left PCL significantly larger (males: left 10.67 cm² vs.
    right 8.80 cm²; females: left 8.80 cm² vs. right 6.99 cm²)[reference:17].
    Also: *Morphology and digitally aided morphometry of the human
    paracentral lobule* (2013), *Folia Morphol*, 72(1). Left ≈ 6.79 cm²
    vs. right ≈ 5.76 cm² in males; left ≈ 6.05 cm² vs. right ≈ 5.16 cm²
    in females[reference:18].
*   **Right sensory-area width:** *Morphometric Variation of Paracentral
    Lobule in Relation to the Hemisphere of Human Brain* (Bangladesh
    Journal of Anatomy). Maximum width of sensory area significantly higher
    in **right** paracentral lobule in both sexes[reference:19].
*   **Clinical syndrome:** *A Medial View Of The Paracentral Lobule Of The
    Brain* (SciePro). Lesions in this parasagittal territory often present
    with **contralateral lower-limb weakness, altered proprioception, and
    gait disturbance**; **ACA infarction**, parasagittal meningioma, or
    cortical venous thrombosis along the superior sagittal sinus can
    involve this cortex, with **urinary urgency or incontinence**
    [reference:20]. Also: *Connection between Diseases and Neuroimaging of
    the Nervous System* (IntechOpen, 2025) — damage to the paracentral
    lobule can lead to contralateral lower limb paralysis and difficulty
    urinating and defecating[reference:21].
*   **Micturition control:** *Management of Neurogenic Bladder* — the
    paracentral lobule is **inhibitory to the pontine micturition center**
    [reference:22]; incontinence may not appear unless **both lobules are
    invaded**[reference:23].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed. (Medial-surface gyral anatomy.)
*   Terminologia Anatomica (FIPAT, 2019) — lobulus paracentralis.
*   NeuroNames — Paracentral lobule (right); FMA — right paracentral lobule
    (parietal part).
"""