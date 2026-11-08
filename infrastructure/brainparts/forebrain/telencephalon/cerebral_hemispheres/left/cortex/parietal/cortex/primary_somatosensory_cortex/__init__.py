"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex.primary_somatosensory_cortex
============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── cortex
                        └── primary_somatosensory_cortex   <-- THIS MODULE

**Primary synonym:** Primary Somatosensory Cortex (S1), left; Left S1;
Somatosensory Area I; SI.
**Organizing principle:** **Functional–anatomical region** — the first
cortical stage of somatosensory processing.
**Brodmann constitution:** **BA3a + BA3b + BA1 + BA2** (four
cytoarchitectonically distinct fields arranged rostral-to-caudal along the
postcentral gyrus)[reference:0].
**Part of:** The **functional partition** of the left parietal lobe
(``.../parietal/cortex``), alongside S2 and PPC.
**Cytoarchitectonic siblings:** ``.../parietal/brodmann_areas/brodmann_area_1``,
``.../parietal/brodmann_areas/brodmann_area_2``, and the **cross-listed**
``.../parietal/gyri/postcentral_gyrus/brodmann_area_3`` — the same
territory, partitioned differently. See "Two-Partition Context" below.

Overview
--------
The **left primary somatosensory cortex (S1)** is the first cortical stage of
somatosensory processing and the thalamic gateway for discriminative touch,
proprioception, and nociception. It occupies the **postcentral gyrus**,
immediately posterior to the central sulcus, and is constituted by **four
cytoarchitectonically distinct Brodmann fields** — **3a, 3b, 1, and 2** —
arranged along a rostral-to-caudal axis[reference:1]. Each field contains a
complete **somatotopic representation of the contralateral body surface**,
and the four fields together form a **hierarchical processing cascade** in
which information flows from the thalamic gateway (BA3b) through successive
higher-order stages (BA1 → BA2)[reference:2][reference:3].

**This is the canonical boundary case of the two-partition architecture.**
S1 is the only functional region in the tree whose constituent Brodmann
fields live under **two different parents**: BA1 and BA2 are wired under
``.../parietal/brodmann_areas/``, while **BA3 is cross-listed** and lives
under ``.../parietal/gyri/postcentral_gyrus/brodmann_area_3``. The
``REGION_TO_BRODMANN`` mapping in the parent ``cortex`` aggregator makes
this scattered membership explicit and programmatically enumerable.

**Left-lateralization note:** The left S1 is the **dominant substrate for
stereognosis** (tactile object recognition) in many right-handers. A small
infarct in the **left postcentral gyrus (BA1)** can produce **bilateral
astereognosis** — the inability to recognize objects by touch with **either**
hand — a syndrome first proposed by Oppenheim in 1906 and confirmed by
modern case reports[reference:4]. This left-lateralized, bilateral-loss
phenotype is **absent** from the right S1 twin (see `Lateralization Notes`).

Two-Partition Context
---------------------
This module is the **functional-region node** for the left S1. It is
**constituted by** Brodmann-area leaves that are wired under the sibling
cytoarchitectonic partition — with one leaf at a non-standard path:

::

    Functional partition (this module)     Cytoarchitectonic partition
    ──────────────────────────────────     ────────────────────────────
    primary_somatosensory_cortex    ──┐
                                     ├──▶  brodmann_area_1   (BA1; crown)
                                     ├──▶  brodmann_area_2   (BA2; caudal
                                     │      bank)
                                     └──▶  brodmann_area_3   **CROSS-LISTED**
                                            lives under
                                            gyri/postcentral_gyrus/
                                            brodmann_area_3
                                            (BA3a + BA3b; rostral bank)

**BA3 is the only constituent that does not live under
``brodmann_areas/``.** Consumers that iterate
``brodmann_areas.LOCAL_AREAS`` will see BA1 and BA2 but **not** BA3; they
must use ``brodmann_areas.ITERABLE_AREAS`` and resolve BA3 via
``brodmann_areas.AREA_PATHS["brodmann_area_3"]``. This module's
``BRODMANN_FIELDS`` constant (below) encodes the correct resolution.

Hierarchical Processing within S1
---------------------------------
The four S1 fields are **not co-equal**; they form a **serial hierarchy**
along the anterior-to-posterior axis. The division of labour is:

*   **BA3b (rostral bank of postcentral gyrus)** — the **thalamic gateway**
    and **first cortical stage of tactile processing**. BA3b receives the
    **densest thalamic input** from VPL/VPM and shows specific responsivity
    to FA1, SA1, and SA2 afferents, making it key for **discriminative
    touch**[reference:5][reference:6]. The earliest cortical components of
    somatosensory evoked potentials originate in BA3b[reference:7].

*   **BA3a (anterior to BA3b, adjacent to BA4)** — a **proprioceptive and
    nociceptive** field. BA3a contains neurons that respond primarily to
    **joint movements**[reference:8] and is more related to proprioception
    and nociception than to cutaneous touch[reference:9].

*   **BA1 (crown of postcentral gyrus)** — the **texture** stage. BA1
    receives input from FA1 afferents and from BA3b, and it is specifically
    implicated in **texture perception**. The BA3b → BA1 boundary is a
    **functional boundary** in the S1 hierarchy[reference:10].

*   **BA2 (caudal bank of postcentral gyrus)** — the **size/shape and
    proprioceptive** stage. BA2 receives reciprocal input from BA3b (for
    size/shape) and is more sensitive to **proprioceptive inputs** than
    BA1[reference:11]. BA2 has **larger receptive fields** than BA3b/BA1,
    consistent with a higher-order role.

**The hierarchy in one line:** BA3b (touch gateway) → BA1 (texture) →
BA2 (size/shape, proprioception); BA3a (proprioception/nociception) runs in
parallel at the anterior edge.

Function in the Human Brain
---------------------------
The left S1 is the **left-lateralized somatosensory gateway and
stereognosis hub**. Its best-supported functions cluster into six domains:

*   **Discriminative Touch (BA3b → BA1):** BA3b is the first cortical
    recipient of cutaneous afferents and the substrate for **detecting**
    tactile stimuli; BA1 refines this into **texture discrimination**
    [reference:12][reference:13]. Together they support the fine-grained
    analysis of tactile surfaces.

*   **Proprioception and Limb Posture (BA3a + BA2):** BA3a processes
    **joint movement** signals from muscle spindles and joint receptors;
    BA2 integrates these with cutaneous signals into a coherent
    representation of **limb posture and size/shape**[reference:14]
    [reference:15].

*   **Nociception (Sensory-Discriminative Aspect):** S1 — particularly
    BA1 — is a key node in the **sensory-discriminative** dimension of
    pain, encoding the **location, intensity, and quality** of a
    nociceptive stimulus. Nociceptive S1 responses are generated in
    **area 1**, spatially corresponding to the later tactile S1
    response[reference:16].

*   **Stereognosis (Tactile Object Recognition):** The left S1 is the
    **dominant cortical substrate for stereognosis** — the ability to
    recognize objects by feeling their form, size, and texture. A small
    infarct in the **left postcentral gyrus (BA1)** can produce
    **bilateral astereognosis**, with the lesion interrupting afferent
    input from BA3a/BA3b and forward processing to BA2, S2, and the
    contralateral BA1[reference:17].

*   **Somatotopic Representation of the Right Hemibody:** Each S1 field
    contains a complete **mirror-image somatotopic map** of the
    **right** hemibody (face represented bilaterally). BA3b and BA1 are
    **mirror representations** of the body relative to each other
    [reference:18].

*   **Sensorimotor Coupling and Hand Movement:** The left S1 provides
    **afferent regulation of the motor hand area** for grasping, and it
    plays a role in **complex finger movements**. Patients with left S1
    lesions present with **asymmetric clumsiness of complex finger
    movements** in association with stereognosis impairment, suggesting a
    dominant role of the left somatosensory cortex in complex hand
    function[reference:19].

Associated Disorders
--------------------
Damage to or dysfunction of the left S1 is associated with:

*   **Bilateral Astereognosis (Left-Lateralized — the signature left-S1
    syndrome):** Inability to recognize objects by touch with **either**
    hand, following a **unilateral left** postcentral lesion. The lesion
    is strategically positioned to interrupt BA3a/BA3b afferents, forward
    processing to BA2/S2/contralateral BA1, and afferent regulation of the
    motor hand area[reference:20]. This is a **left-lateralized**
    syndrome and does **not** occur with right S1 lesions.

*   **Impaired Texture Discrimination (BA1 lesion):** Selective deficit
    in discriminating surface texture, with relatively preserved detection
    thresholds.

*   **Impaired Size/Shape and Proprioceptive Discrimination (BA2 lesion):**
    Difficulty with tactile size/shape judgments and limb-position sense.

*   **Asymmetric Clumsiness of Complex Finger Movements:** Impairment of
    skilled hand movements, particularly for complex finger sequences,
    associated with left S1 lesions and stereognosis deficits
    [reference:21].

*   **Contralateral Hemihypesthesia:** Reduced sensitivity to somatosensory
    stimuli on the **right** side of the body (face excepted, which is
    bilaterally represented).

**What is NOT here:** The **right-hemibody** representation, the
**right-lateralized spatial-attention** functions, and the **right-S1
contralateral-only** astereognosis phenotype are properties of the **right**
S1 module. They are **not** part of this left module and must not be
imported from the right twin.

Lateralization Notes
--------------------
This is the **left** S1 module. The lateralization landscape is
**left-loaded** at the functional-region level (not parallel-laden, as for
PPC and BA39/BA40):

*   **Left-Lateralized Functions (unique to this twin):**
    - **Stereognosis dominance** — the left S1 (BA1–BA2 complex) is the
      dominant substrate for bilateral tactile object recognition. A
      small left BA1 infarct produces **bilateral** astereognosis
      [reference:22].
    - **Complex finger movement dominance** — the left S1 plays a
      dominant role in complex finger movements and hand function
      [reference:23].
    - **Afferent regulation of the motor hand area for grasping** — the
      left S1 → left motor hand area pathway is part of the
      left-lateralized praxis/grasping system.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Spatial-attention weighting** — the right S1 shows stronger
      cortical facilitation during **left-hand** stimulation, consistent
      with a right-hemisphere weighting for contralateral somatosensory
      processing (see right S1 module).
    - **Contralateral-only astereognosis** — a right S1 lesion produces
      left-hand astereognosis **only**; it does not produce bilateral
      loss.

*   **Symmetric Functions (bilateral properties of S1):**
    - BA3b thalamic gateway and first cortical stage of tactile processing.
    - BA3b → BA1 → BA2 hierarchical processing (texture → size/shape).
    - BA3a proprioceptive and nociceptive processing.
    - Somatotopic mirror representations (BA3b ↔ BA1), with hemibody
      flipped (left S1 → right hemibody; right S1 → left hemibody).
    - Nociceptive sensory-discriminative processing (area 1).

**A consumer that assumes "left S1 = symmetric" will miss the two
left-lateralized functions (stereognosis dominance, complex finger movement
dominance) that define the left twin.** Unlike the PPC and BA39/BA40 pairs
(which are parallel-laden), the S1 pair is **left-loaded**: the left twin
carries the lateralized syndromes, and the right twin must **explicitly
deny** them while documenting its own contralateral-only phenotype and
left-hand facilitation.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional region node, not a Brodmann aggregator.** This module
    represents **S1 as a functional unit** (BA3a + BA3b + BA1 + BA2). It
    documents the hierarchical division of labour among the four fields and
    cross-references their Brodmann leaves; it does **not** duplicate their
    per-area content.
*   **BA3 is cross-listed and lives under a non-standard path.** The
    ``BRODMANN_FIELDS`` constant below resolves all four fields, including
    the BA3 hop. Consumers must not assume that all S1 fields live under
    ``brodmann_areas/``.
*   **Structural parity with right S1.** Left and right S1 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. **However** — as for BA1/BA2/BA5 — the left
    twin carries the lateralized syndromes (stereognosis dominance, complex
    finger movement dominance), and the right twin must **explicitly deny**
    them. The two modules are structurally parallel but **content-divergent
    by design** in the left-loaded direction.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex import primary_somatosensory_cortex

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.cortex.primary_somatosensory_cortex"
    )

For Brodmann subfields (a **different** partition of the same territory),
use the ``BRODMANN_FIELDS`` resolver below — **not** a raw
``brodmann_areas.LOCAL_AREAS`` iteration, which would silently miss BA3::

    from ...parietal.brodmann_areas import AREA_PATHS
    for field, path in primary_somatosensory_cortex.BRODMANN_FIELDS.items():
        # path is already resolved; BA3 points at gyri/postcentral_gyrus
        ...

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        s1_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.cortex.primary_somatosensory_cortex"
        )
        # resolve s1_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
    (BA3a, BA3b, BA1, BA2 — the four cytoarchitectonic fields of S1.)
*   **Four-field S1 and hierarchy:** *Differential Organization of Touch and
    Pain in Human Primary Somatosensory Cortex* (2000), *J Neurophysiol*,
    83(3), 1770 — SI consists of four cytoarchitectonically distinct fields
    (3a, 3b, 1, 2); area 3b represents the first cortical stage of tactile
    processing[reference:24].
*   **Mesoscale S1 hierarchy:** *Mesoscale hierarchical organization of
    primary somatosensory cortex captured by resting-state-fMRI in humans*
    (2021), *NeuroImage* — S1 divides into two functional parcels (3a & 3b,
    1 & 2); functional boundary between 3b and 1; thalamocortical
    connectivity reflects Brodmann areas[reference:25].
*   **BA3a / BA3b functional differentiation:** *S1 subareas* (J Neurosci;
    biorxiv) — BA3a related to proprioception and nociception; BA3b
    considered S1 ‘proper’; BA1 and BA2 higher-order subdivisions
    [reference:26].
*   **Thalamic input and hierarchy:** Ackerley & Kavounoudias (2015),
    *Neuropsychologia* postprint — BA3b receives the densest thalamic input
    and is key for discriminative touch; BA1 → texture; BA2 → size/shape and
    proprioception; BA3b and BA1 are mirror representations[reference:27].
*   **Stereognosis and left dominance:** Moll, J., et al. (2017). *Cogn
    Behav Neurol*, 30(3), 102–115. “Hemispheric Dominance for Stereognosis
    in a Patient With an Infarct of the Left Postcentral Sensory Hand Area”
    — a small left BA1 infarct produced **bilateral astereognosis**,
    supporting Oppenheim's 1906 proposal of left-hemisphere dominance for
    stereognosis[reference:28].
*   **Left S1 and complex finger movements:** *The role of the left
    somatosensory cortex in human hand movement* (PubMed) — left S1 lesions
    produce asymmetric clumsiness of complex finger movements and
    stereognosis impairment, suggesting a dominant role of left S1 in
    complex hand function[reference:29].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Brodmann areas 1, 2, 3a, 3b (left); FMA — left postcentral
    gyrus (S1 partonomy).
"""