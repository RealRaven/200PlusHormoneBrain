"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.gyri.postcentral_gyrus.brodmann_area_3
===============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── gyri
                        └── postcentral_gyrus
                            └── brodmann_area_3   <-- THIS MODULE

**Primary synonym:** Brodmann Area 3 (BA3); Area 3 of Brodmann (1909).
**Subdivisions:** **BA3a** and **BA3b** — two cytoarchitectonically and
functionally distinct fields conventionally grouped under the single
Brodmann label "area 3" but increasingly recognized as separate entities.
**Part of:** Primary somatosensory cortex (**S1**), alongside BA1 and BA2.
**Structural parent:** ``.../parietal/gyri/postcentral_gyrus`` — **not**
``.../parietal/brodmann_areas``.
**Cross-listing status:** The **only** Brodmann-area leaf in the tree that
lives under a gyral container. Resolution target for the **right**
``brodmann_areas.AREA_PATHS["brodmann_area_3"]``.
**Location:** The **posterior bank of the central sulcus** (BA3b) and the
**fundus** of the central sulcus (BA3a), at the transition between the
primary somatosensory and primary motor cortices.

Overview
--------
Brodmann Area 3 (BA3) is the **rostral-most component of the primary
somatosensory cortex (S1)** and the **first cortical stage of the
somatosensory processing cascade** in the **right** hemisphere. It occupies
the **posterior bank of the central sulcus** (BA3b) and the **fundus of the
central sulcus** (BA3a), adjacent to the agranular primary motor cortex
(BA4) on the anterior bank. It is the **thalamic gateway** for
discriminative touch, proprioception, and nociception from the
**contralateral (left) hemibody**.

**BA3 is not a single homogeneous field.** Modern cytoarchitectonic and
electrophysiological work distinguishes **two functionally dissociable
subfields**:

*   **BA3b** — the **thalamic gateway** and the **first cortical stage of
    tactile processing**. It is **"S1 proper"** (Kaas, 1983) and receives
    the **densest thalamocortical input** from the ventroposterior lateral
    (VPL) and ventroposterior medial (VPM) nuclei of the thalamus
    [reference:0]. It is a **koniocortex** with a very high cell-packing
    density in layer IV and is the **principal cortical target of the
    lemniscal pathway** for discriminative touch. BA3b and BA1 neurons are
    **unimodal**, encoding only the tactile modality in both firing rate
    and variability, and BA3b carries **more information about periodic
    stimulus structure** than BA1, with **lower response and coding
    latencies** and a **lower intrinsic time scale** — direct evidence of a
    **processing-based hierarchy** .

*   **BA3a** — a **hybrid field** at the fundus of the central sulcus,
    adjacent to area 4. It has a **blend of motor and sensory features** —
    low cell-packing density, few larger pyramidal cells in deep layer III,
    and an **incipient layer IV**. It receives **proprioceptive signals**
    from deep receptors via the **ventroposterior oral nucleus (VPO)** and
    the **ventroposterior superior nucleus (VPS)** [reference:2][reference:3],
    and it is also **nociresponsive** — particularly to
    **C-fiber-mediated slow/burning pain** (second pain) — via a distinct
    region at the S1–M1 border that some authors propose to call **"BA3c"**
    [reference:4].

**This module is the right-hemisphere twin of the left BA3, and it is
structurally identical but functionally inverted in its lateralization.**
The cytoarchitecture, thalamic input, and hierarchical position are
**hemisphere-symmetric**. The **left** BA3 carries the left-lateralized
**bilateral astereognosis** and **stereognosis dominance** claims; the
**right** BA3 carries a **contralateral-only astereognosis** phenotype and
a **right-lateralized proprioceptive weighting** — documented in detail
below.

**This module is the cross-listing resolution target.** Every earlier
docstring in the right parietal subtree — from the ``brodmann_areas``
aggregator through BA1, BA2, the S1 functional-region node, and the gyri
aggregator — has pointed at this path as the place where BA3 actually
lives. A consumer that iterates ``brodmann_areas.LOCAL_AREAS`` will see
BA1 and BA2 but **not** BA3; they must use ``ITERABLE_AREAS`` and resolve
BA3 through this gyrus.

Two-Partition Context
---------------------
This module is a **cytoarchitectonic leaf** under a **structural
container** (the right postcentral gyrus). It is the **only** such module
in the tree:

::

    Structural container (gyrus)         Cytoarchitectonic leaf (this module)
    ────────────────────────────         ────────────────────────────────────
    postcentral_gyrus               ──▶  brodmann_area_3   **CROSS-LISTED**
                                           ├── BA3a (fundus; proprioception /
                                           │   nociception)
                                           └── BA3b (posterior bank; thalamic
                                               gateway for discriminative touch)

**Resolution contract for consumers:**

*   If you need **BA3 by name**, use
    ``brodmann_areas.ITERABLE_AREAS`` and resolve it via
    ``AREA_PATHS["brodmann_area_3"]``, which points here.
*   If you need **BA3a or BA3b separately**, use the ``SUBFIELDS`` constant
    below. They are **not** wired as separate child packages.
*   If you iterate ``brodmann_areas.LOCAL_AREAS``, you will **miss BA3**.
    This is documented, not a bug.

Cytoarchitecture
----------------
The two BA3 subfields are cytoarchitectonically distinct and are
increasingly recognized as separate entities. The cytoarchitecture is
**hemisphere-symmetric** and is copied verbatim from the left BA3 twin:

*   **BA3b (S1 proper)** — **koniocortex** with a very high cell-packing
    density in the supragranular layers, particularly layer IV. Small
    granular neurons and small pyramidal neurons give it an overall
    "dusty" appearance under low-power microscopy. It has the
    **narrowest fingertip tuning** in the S1 hierarchy (2.6 fingertips
    FWHM), widening to 4.0 in BA1 and 9.3 in BA2. It is the
    **principal thalamocortical recipient** of the lemniscal pathway from
    **VPL/VPM** [reference:5].

*   **BA3a** — a **transitional/hybrid** cortex at the fundus of the
    central sulcus, with **fewer granule cells and larger pyramidal cells**
    than BA3b. It has an **incipient layer IV** and a **blend of motor and
    sensory features**. It receives **muscle spindle** input via **VPO**
    [reference:6] and **deep-receptor** input via **VPS** [reference:7]. It
    contains a **nociresponsive region** at the S1–M1 border that is
    **C-fiber-dominated** and is associated with **slow/second/burning
    pain** — a functionally distinct zone that some authors propose to call
    **"BA3c"** [reference:8].

**Thalamic input summary (hemisphere-symmetric):**

*   **BA3b** ← **VPL/VPM** (cutaneous, lemniscal; the densest input); also
    sparse VPS and VPI [reference:9].
*   **BA3a** ← **VPO** (muscle spindle) [reference:10]; **VPS** (deep
    receptors) [reference:11].

Function in the Human Brain
---------------------------
The right BA3 is the **right-lateralized thalamic gateway and first
cortical stage of somatosensory processing** for the **left hemibody**. Its
best-supported functions cluster into five domains:

*   **Discriminative Touch — First Cortical Stage (BA3b):** BA3b is the
    **first cortical stage of the tactile processing cascade** and receives
    the **densest thalamic input** from **VPL/VPM** [reference:12]. It is
    the principal cortical target of the lemniscal pathway for fine
    discriminative touch, with specific responsivity to **FA1, SA1, and
    SA2** cutaneous afferents. It is the substrate for **elementary tactile
    feature detection**, including **two-point discrimination**.
    Neurons in BA3b carry **more information about periodic stimulus
    structure** than BA1, with **lower response latencies** — a
    processing-based hierarchy .

*   **Proprioception — Deep Receptor Input (BA3a):** BA3a receives
    **muscle spindle** signals via **VPO** [reference:14] and
    **deep-receptor** signals via **VPS** [reference:15]. It is the
    **proprioceptive gateway** of right S1 — the first cortical stage of
    the processing cascade that leads to limb-position sense and
    kinaesthesia for the **left** limbs.

*   **Nociception — Slow/Burning Pain (BA3a, "BA3c"):** A distinct
    nociresponsive region at the **S1–M1 border** within BA3a responds
    preferentially to **C-fiber-mediated slow/burning pain** (second
    pain), in contrast to the **Aδ-mediated fast/discriminative pain**
    (first pain) generated in **BA3b–BA1** [reference:16]. This region is
    most likely engaged in **interoception and autonomic control** and
    contributes to the **sympathetic response to noxious stimulation**.
    Ablation of this region has been shown to **reduce pain sensibility**
    [reference:17].

*   **Somatotopic Representation of the Left Hemibody:** BA3b contains a
    complete **mirror-image somatotopic map** of the **left** hemibody,
    which is a **mirror image of the BA1 map** [reference:18]. The **foot**
    is represented **posteriorly**, and the **genitalia** are represented
    **anterior** to the foot sensory area. The **lips** have an
    **ipsilateral** representation in **BA3b/BA1** in addition to the
    contralateral one — a rare exception to the strictly contralateral
    organization of S1.

*   **Hierarchical Cascade Initiation (BA3b → BA1 → BA2):** BA3b initiates
    the **serial hierarchy** of S1: BA3b (elementary features, two-point
    discrimination) → BA1 (texture) → BA2 (size/shape, proprioception).
    Fingertip tuning widths widen progressively from **2.6** (BA3b) to
    **4.0** (BA1) and **9.3** (BA2) fingertips FWHM, providing direct
    evidence for the hierarchical cascade. BA3b and BA1 neurons are
    **unimodal**, encoding only the tactile modality .

Associated Disorders
--------------------
Damage to or dysfunction of the **right** BA3 is associated with:

*   **Contralateral (Left) Astereognosis (Contralateral-Only — the
    right-BA3 phenotype):** Lesions to the right postcentral gyrus produce
    **astereognosis** — the inability to recognize objects by touch despite
    intact elementary sensation — in the **left hand** [reference:20]. "The
    resulting astereognosis typically presents **contralaterally**, meaning
    a lesion in the right parietal lobe will cause astereognosis in the
    left hand" [reference:21]. Only **direct damage to or undercutting of
    the anterior part of the middle third of the postcentral gyrus** causes
    impairment of size and shape discrimination **contralateral to the
    lesion** . This is **not** the bilateral astereognosis
    phenotype of the left BA3; a right-sided lesion does **not** produce
    bilateral loss.

*   **Impaired Two-Point Discrimination (BA3b lesion, left hand):**
    Selective deficit in elementary tactile feature detection on the
    **left** hand.

*   **Impaired Proprioception (BA3a lesion, left hand):** Deficits in
    limb-position sense and kinaesthesia for the **left** limbs.

*   **Altered Slow/Burning Pain Perception (BA3a/"BA3c" lesion or
    ablation):** Ablation of the nociresponsive region in the depth of
    the central sulcus **reduces pain sensibility** [reference:23].

**What is NOT here:** **Bilateral astereognosis**, **stereognosis
dominance**, **bilateral clumsy hands**, and **left-lateralized complex
finger movement dominance** are **left-lateralized** functions of the left
BA3. They do **not** occur with right BA3 lesions. They are documented in
the left BA3 module and are **explicitly denied here** (see
`Lateralization Notes`). A right BA3 lesion does **not** produce bilateral
astereognosis.

Lateralization Notes
--------------------
This is the **right** BA3 module. The lateralization landscape is
**right-loaded for proprioception** and **left-loaded for stereognosis**
— a **mixed pattern** that is qualitatively different from the left BA3
twin:

*   **Right-Lateralized Functions (unique to this twin):**
    - **Bilateral hand proprioception** — a unilateral right postcentral
      lesion affects proprioceptive processing for **both hands**,
      suggesting integration of contralateral and ipsilateral
      proprioceptive information at this early stage, possibly via callosal
      connections (see the right postcentral gyrus module for the case
      evidence).
    - **Right-hemisphere lateralization for lower-limb proprioception** —
      a general right-hemisphere weighting for proprioception regardless
      of which limb is active (see the right postcentral gyrus module).
    - **Contralateral-only astereognosis** — a right BA3 lesion produces
      **left-hand** astereognosis only [reference:24][reference:25].

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Bilateral astereognosis** — a small left BA1/BA3 lesion produces
      bilateral loss; a right lesion produces **contralateral-only** loss.
    - **Stereognosis dominance** — the left BA3/BA1 complex is the
      dominant substrate for tactile object recognition in some
      individuals (Oppenheim, 1906; Moll et al., 2017).
    - **Bilateral clumsy hands** — left postcentral lesions impair complex
      finger movements bilaterally; right lesions impair only the left
      hand.

*   **Symmetric Functions (bilateral properties of BA3, copied verbatim
    from the left twin):**
    - BA3b thalamic gateway and first cortical stage of tactile processing
      [reference:26].
    - BA3b → BA1 → BA2 hierarchical cascade .
    - BA3a proprioceptive and nociresponsive processing (muscle spindle,
      C-fiber slow pain) [reference:28][reference:29].
    - Somatotopic mirror representations (BA3b ↔ BA1), with hemibody
      flipped (right BA3 → **left** hemibody) [reference:30].
    - Ipsilateral lip representation in BA3b/BA1.

**A consumer that assumes "right BA3 = symmetric" will miss the
right-lateralized bilateral proprioception and contralateral-only
astereognosis weightings.** A consumer that assumes "right BA3 = left BA3"
will incorrectly import the left-lateralized bilateral astereognosis and
stereognosis dominance claims, which are **absent** here.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../frontal/gyri/precentral_gyrus`` or
    ``.../frontal/brodmann_areas/brodmann_area_4``. The motor counterpart
    (BA4) is a separate module in the frontal lobe.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cross-listed leaf — the ONLY Brodmann-area leaf under a gyrus.**
    This module lives under ``.../gyri/postcentral_gyrus/``, **not** under
    ``.../brodmann_areas/``. It is the resolution target for the **right**
    ``brodmann_areas.AREA_PATHS["brodmann_area_3"]``.
*   **BA3a and BA3b are subfields, not separate modules.** They are
    documented within this single module via the ``SUBFIELDS`` constant.
*   **Structural parity with left BA3.** Left and right BA3 modules must
    be structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. The cytoarchitecture, thalamic input, and
    hierarchical position are **symmetric**; only the lateralization prose
    and the contralateral target differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.gyri.postcentral_gyrus import brodmann_area_3

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.gyri.postcentral_gyrus.brodmann_area_3"
    )

For BA3 via the ``brodmann_areas`` aggregator (the **only** correct way
to reach it from that partition)::

    from ...parietal.brodmann_areas import ITERABLE_AREAS, AREA_PATHS
    # AREA_PATHS["brodmann_area_3"] points at this module

For BA3a and BA3b separately::

    from ...parietal.gyri.postcentral_gyrus.brodmann_area_3 import SUBFIELDS
    # SUBFIELDS["brodmann_area_3a"], SUBFIELDS["brodmann_area_3b"]

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba3_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.gyri.postcentral_gyrus.brodmann_area_3"
        )
        # resolve ba3_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
*   **Thalamic input — VPL/VPM to BA3b:** *Anterior (ant.) parietal cortex*
    (Semmelweis repository) [reference:31]; *Thalamocortical connections*
    (theses.hal.science, tel-01186557) — **VPL/VPM** → BA3b (densest
    input); **VPO** → BA3a (muscle spindle); **VPS** → BA3a and BA2 (deep
    receptors) [reference:32][reference:33].
*   **Hierarchical unimodal processing:** *Hierarchical unimodal processing
    within the primary somatosensory cortex during a bimodal detection
    task* (2022), *PNAS*, 119(52), e2213847119 . BA3b and BA1
    neurons are **unimodal**; BA3b carries **more information about
    periodic stimulus structure**, with **lower response and coding
    latencies** and a **lower intrinsic time scale** — a processing-based
    hierarchy.
*   **BA3a nociresponsive region / "BA3c":** *A nociresponsive specific area
    of human somatosensory cortex within BA3a: BA3c?* (2020),
    *NeuroImage*, 221, 117187 [reference:35]. The depth of the central
    sulcus contains a **C-fiber-dominated** nociresponsive region
    associated with **slow/burning pain**; ablation reduces pain
    sensibility.
*   **Right BA3 somatotopy — left hemibody:** *ipsilateral clusters* (theses
    .hal.science, tel-01186557) — the right-D2 and right-lip
    representations are within **right BA3b** and **right BA3a**; the
    somatotopic map is of the **contralateral (left) hemibody**
    [reference:36].
*   **Contralateral-only astereognosis from right lesions:** *Astereognosis*
    (arabpsychology.com, 2025) — "a lesion in the right parietal lobe
    will cause astereognosis in the **left hand**" [reference:37].
    *Astereognosis. Tactile discrimination after localized hemispheric
    lesions in man* (OvidDS) — only direct damage to the anterior part of
    the middle third of the postcentral gyrus caused impairment
    **contralateral to the lesion** .
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Brodmann area 3 (right); FMA — right postcentral gyrus
    (BA3 partonomy).
"""