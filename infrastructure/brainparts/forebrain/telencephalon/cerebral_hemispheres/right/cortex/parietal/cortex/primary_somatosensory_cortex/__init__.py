"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex.primary_somatosensory_cortex
=============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── cortex
                        └── primary_somatosensory_cortex   <-- THIS MODULE

**Primary synonym:** Primary Somatosensory Cortex (S1), right; Right S1;
Somatosensory Area I; SI.
**Organizing principle:** **Functional–anatomical region** — the first
cortical stage of somatosensory processing.
**Brodmann constitution:** **BA3a + BA3b + BA1 + BA2** (four
cytoarchitectonically distinct fields arranged rostral-to-caudal along the
postcentral gyrus).
**Part of:** The **functional partition** of the right parietal lobe
(``.../parietal/cortex``), alongside S2 and PPC.
**Cytoarchitectonic siblings:** ``.../parietal/brodmann_areas/brodmann_area_1``,
``.../parietal/brodmann_areas/brodmann_area_2``, and the **cross-listed**
``.../parietal/gyri/postcentral_gyrus/brodmann_area_3`` — the same
territory, partitioned differently. See "Two-Partition Context" below.

Overview
--------
The **right primary somatosensory cortex (S1)** is the first cortical stage
of somatosensory processing and the thalamic gateway for discriminative
touch, proprioception, and nociception in the right hemisphere. It occupies
the **postcentral gyrus**, immediately posterior to the central sulcus, and
is constituted by **four cytoarchitectonically distinct Brodmann fields** —
**3a, 3b, 1, and 2** — arranged along a rostral-to-caudal axis. Each field
contains a complete **somatotopic representation of the contralateral body
surface**, and the four fields together form a **hierarchical processing
cascade** in which information flows from the thalamic gateway (BA3b)
through successive higher-order stages (BA1 → BA2).

**This module is the structural mirror of the left S1, but not its
functional twin.** The cytoarchitectonic organization and the intrinsic
hierarchical processing of S1 are hemisphere-symmetric; however, the
**lateralized functional weightings are not**. Unlike the PPC and BA39/BA40
pairs (which are **parallel-laden**), the S1 pair is **left-loaded**:

*   **The left S1** carries the left-lateralized **stereognosis dominance**
    (bilateral astereognosis from a small left BA1 infarct) and **complex
    finger movement dominance**.
*   **The right S1** carries a distinct **right-lateralized weighting for
    the non-dominant (left) hand**: stronger cortical facilitation during
    left-hand stimulation, and a **contralateral-only** astereognosis
    phenotype.

**Critical lateralization note:** The **bilateral astereognosis** syndrome
described for the left S1 is **left-lateralized** and is **absent** from
the right S1. A right S1 lesion produces **left-hand astereognosis only**
— a purely contralateral deficit. See `Lateralization Notes` for the full
asymmetry.

**This is the canonical boundary case of the two-partition architecture.**
S1 is the only functional region in the tree whose constituent Brodmann
fields live under **two different parents**: BA1 and BA2 are wired under
``.../parietal/brodmann_areas/``, while **BA3 is cross-listed** and lives
under ``.../parietal/gyri/postcentral_gyrus/brodmann_area_3``. The
``BRODMANN_FIELDS`` constant below makes this scattered membership
explicit and programmatically enumerable.

Two-Partition Context
---------------------
This module is the **functional-region node** for the right S1. It is
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
``BRODMANN_FIELDS`` constant (below) encodes the correct resolution for the
**right** hemisphere.

Hierarchical Processing within S1
---------------------------------
The four S1 fields are **not co-equal**; they form a **serial hierarchy**
along the anterior-to-posterior axis. The division of labour is
**hemisphere-symmetric** and is copied verbatim from the left S1 twin:

*   **BA3b (rostral bank of postcentral gyrus)** — the **thalamic gateway**
    and **first cortical stage of tactile processing**. BA3b receives the
    **densest thalamic input** from VPL/VPM and shows specific responsivity
    to FA1, SA1, and SA2 afferents, making it key for **discriminative
    touch**. The earliest cortical components of
    somatosensory evoked potentials originate in BA3b.

*   **BA3a (anterior to BA3b, adjacent to BA4)** — a **proprioceptive and
    nociceptive** field. BA3a contains neurons that respond primarily to
    **joint movements** and is more related to proprioception
    and nociception than to cutaneous touch.

*   **BA1 (crown of postcentral gyrus)** — the **texture** stage. BA1
    receives input from FA1 afferents and from BA3b, and it is specifically
    implicated in **texture perception**. The BA3b → BA1 boundary is a
    **functional boundary** in the S1 hierarchy.

*   **BA2 (caudal bank of postcentral gyrus)** — the **size/shape and
    proprioceptive** stage. BA2 receives reciprocal input from BA3b (for
    size/shape) and is more sensitive to **proprioceptive inputs** than
    BA1. BA2 has **larger receptive fields** than BA3b/BA1,
    consistent with a higher-order role.

**The hierarchy in one line:** BA3b (touch gateway) → BA1 (texture) →
BA2 (size/shape, proprioception); BA3a (proprioception/nociception) runs in
parallel at the anterior edge.

Function in the Human Brain
---------------------------
The right S1 is the **right-lateralized somatosensory gateway with a
specific weighting for the non-dominant (left) hand**. Its best-supported
functions cluster into six domains:

*   **Discriminative Touch (BA3b → BA1):** BA3b is the first cortical
    recipient of cutaneous afferents and the substrate for **detecting**
    tactile stimuli; BA1 refines this into **texture discrimination**
    . Together they support the fine-grained
    analysis of tactile surfaces — a **symmetric** function copied verbatim
    from the left twin.

*   **Proprioception and Limb Posture (BA3a + BA2):** BA3a processes
    **joint movement** signals from muscle spindles and joint receptors;
    BA2 integrates these with cutaneous signals into a coherent
    representation of **limb posture and size/shape**
    . This is a **symmetric** function.

*   **Nociception (Sensory-Discriminative Aspect):** S1 — particularly
    BA1 — is a key node in the **sensory-discriminative** dimension of
    pain, encoding the **location, intensity, and quality** of a
    nociceptive stimulus. Nociceptive S1 responses are generated in
    **area 1**, spatially corresponding to the later tactile S1
    response. This is a **symmetric** function.

*   **Right-Lateralized Facilitation for the Non-Dominant (Left) Hand
    (unique to this twin):** The right S1 shows **stronger cortical
    facilitation during left-hand stimulation** than during right-hand
    stimulation. In an fNIRS study of 31 right-handed participants,
    stronger cortical facilitation was found in the right S1 and right
    somatosensory association area during **left-hand** stimulation but
    not right-hand stimulation[reference:0]. This asymmetric
    activation for the less-preferred (left) hand is thought to
    "considerably reinforce [the] sensorimotor network just with passive
    vibrotactile cutaneous stimulation"[reference:1]. The right S1 therefore
    carries a **right-lateralized weighting for the non-dominant hand** that
    the left S1 does not have.

*   **Somatotopic Representation of the Left Hemibody:** Each S1 field
    contains a complete **mirror-image somatotopic map** of the **left**
    hemibody (face represented bilaterally). BA3b and BA1 are
    **mirror representations** of the body relative to each other
    . This is a **symmetric** function with the
    hemibody flipped.

*   **Sensorimotor Coupling and Hand Movement (Symmetric but not
    left-dominant):** The right S1 provides **afferent regulation of the
    motor hand area**, and it is engaged during **hand shaping and
    hand-object interactions**. However, unlike the left S1, the right S1
    does **not** carry the dominant role in **complex finger movements** —
    that is a left-S1 function (see `Lateralization Notes`).

Associated Disorders
--------------------
Damage to or dysfunction of the right S1 is associated with:

*   **Left-Hand Astereognosis (Contralateral-Only — the right-S1
    phenotype):** Inability to recognize objects by touch with the **left
    hand** following a right S1 lesion. Astereognosis from a right parietal
    lesion presents **contralaterally** — left-hand only[reference:2]. This is
    **not** the bilateral astereognosis phenotype of the left S1; the right
    S1 does **not** produce bilateral loss.

*   **Impaired Texture Discrimination (BA1 lesion, left hand):**
    Selective deficit in discriminating surface texture on the left hand,
    with relatively preserved detection thresholds.

*   **Impaired Size/Shape and Proprioceptive Discrimination (BA2 lesion,
    left hand):** Difficulty with tactile size/shape judgments and
    limb-position sense on the left side.

*   **Contralateral (Left) Hemihypesthesia:** Reduced sensitivity to
    somatosensory stimuli on the **left** side of the body (face excepted,
    which is bilaterally represented).

**What is NOT here:** **Bilateral astereognosis**, **left-lateralized
complex finger movement dominance**, and **left-S1 afferent regulation of
the motor hand area for grasping** are **left-lateralized** functions of the
left S1. They do **not** occur with right S1 lesions. They are documented
in the left S1 module and are **explicitly denied here** (see
`Lateralization Notes`). A right S1 lesion does **not** produce bilateral
astereognosis.

Lateralization Notes
--------------------
This is the **right** S1 module. The lateralization landscape is
**left-loaded**, in contrast to the parallel-laden PPC and BA39/BA40 pairs:

*   **Right-Lateralized Functions in the Right S1 (unique to this twin):**
    - **Stronger cortical facilitation during left-hand (non-dominant)
      stimulation** — right S1 and right SA show stronger activation for
      left-hand than right-hand passive vibrotactile stimulation
      [reference:3].
    - **Contralateral-only astereognosis** — a right S1 lesion produces
      **left-hand** astereognosis only; it does not produce bilateral
      loss[reference:4].

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Bilateral astereognosis** — a small left BA1 infarct produces
      bilateral loss (left-S1 dominance); the right S1 does **not**.
    - **Complex finger movement dominance** — the left S1 plays a dominant
      role in complex finger movements; the right S1 does **not**.
    - **Afferent regulation of the motor hand area for grasping** — a
      left-S1 function; the right S1 contributes but is not dominant.

*   **Symmetric Functions (bilateral properties of S1, copied verbatim
    from the left twin):**
    - BA3b thalamic gateway and first cortical stage of tactile processing.
    - BA3b → BA1 → BA2 hierarchical processing (texture → size/shape).
    - BA3a proprioceptive and nociceptive processing.
    - Somatotopic mirror representations (BA3b ↔ BA1), with hemibody
      flipped (right S1 → **left** hemibody; left S1 → right hemibody).
    - Nociceptive sensory-discriminative processing (area 1).

**A consumer that assumes "right S1 = symmetric" will miss the
right-lateralized left-hand facilitation and will incorrectly import the
left S1's bilateral-astereognosis and complex-finger-movement dominance.**
The S1 pair is **left-loaded**: the left twin carries the lateralized
syndromes, and this right twin must **explicitly deny** them while
documenting its own left-hand facilitation and contralateral-only phenotype.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional region node, not a Brodmann aggregator.** This module
    represents **S1 as a functional unit** (BA3a + BA3b + BA1 + BA2). It
    documents the hierarchical division of labour among the four fields and
    cross-references their Brodmann leaves; it does **not** duplicate their
    per-area content.
*   **BA3 is cross-listed and lives under a non-standard path.** The
    ``BRODMANN_FIELDS`` constant below resolves all four fields, including
    the BA3 hop, for the **right** hemisphere. Consumers must not assume
    that all S1 fields live under ``brodmann_areas/``.
*   **Structural parity with left S1.** Left and right S1 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. **However** — as for BA1/BA2/BA5 — the left
    twin carries the lateralized syndromes (bilateral astereognosis,
    complex finger movement dominance), and this right twin must
    **explicitly deny** them while adding its own left-hand facilitation.
    The two modules are structurally parallel but **content-divergent by
    design** in the left-loaded direction.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex import primary_somatosensory_cortex

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.cortex.primary_somatosensory_cortex"
    )

For Brodmann subfields (a **different** partition of the same territory),
use the ``BRODMANN_FIELDS`` resolver below — **not** a raw
``brodmann_areas.LOCAL_AREAS`` iteration, which would silently miss BA3::

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
*   **Right S1 left-hand facilitation:** Jin, S.H., Lee, S.H., Yang, S.T., &
    An, J. (2020). “Hemispheric asymmetry in hand preference of right-handers
    for passive vibrotactile perception: an fNIRS study.” *Scientific
    Reports*, 10, 13423. “Stronger cortical facilitation was found in the
    right primary somatosensory cortex (S1) and right somatosensory
    association area (SA) during left-hand stimulation but not right-hand
    stimulation”[reference:5].
*   **Contralateral-only astereognosis:** StatPearls — *Astereognosis*
    (2025); GPnotebook — *Astereognosis* (2018). A lesion in the right
    parietal lobe causes astereognosis in the **left hand** (contralateral);
    the syndrome does **not** produce bilateral loss from a right-sided
    lesion[reference:6].
*   **Four-field S1 and hierarchy:** *Differential Organization of Touch and
    Pain in Human Primary Somatosensory Cortex* (2000), *J Neurophysiol*,
    83(3), 1770 — SI consists of four cytoarchitectonically distinct fields
    (3a, 3b, 1, 2); area 3b represents the first cortical stage of tactile
    processing.
*   **Mesoscale S1 hierarchy:** *Mesoscale hierarchical organization of
    primary somatosensory cortex captured by resting-state-fMRI in humans*
    (2021), *NeuroImage* — S1 divides into two functional parcels (3a & 3b,
    1 & 2); functional boundary between 3b and 1; thalamocortical
    connectivity reflects Brodmann areas.
*   **BA3a / BA3b functional differentiation:** *S1 subareas* (J Neurosci;
    biorxiv) — BA3a related to proprioception and nociception; BA3b
    considered S1 ‘proper’; BA1 and BA2 higher-order subdivisions.
*   **Thalamic input and hierarchy:** Ackerley & Kavounoudias (2015),
    *Neuropsychologia* postprint — BA3b receives the densest thalamic input
    and is key for discriminative touch; BA1 → texture; BA2 → size/shape and
    proprioception; BA3b and BA1 are mirror representations.
*   **Left S1 stereognosis dominance (contrast case):** Moll, J., et al.
    (2017). *Cogn Behav Neurol*, 30(3), 102–115. “Hemispheric Dominance for
    Stereognosis in a Patient With an Infarct of the Left Postcentral Sensory
    Hand Area” — cited here only to mark that the **right** S1 does **not**
    share the bilateral-loss phenotype.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Brodmann areas 1, 2, 3a, 3b (right); FMA — right postcentral
    gyrus (S1 partonomy).
"""