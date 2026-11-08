"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri.postcentral_gyrus
===============================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── gyri
                        └── postcentral_gyrus   <-- THIS MODULE

**Primary synonym:** Postcentral gyrus (left); Gyrus postcentralis;
Postcentral convolution; Posterior central gyrus.
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the lateral surface of the hemisphere.
**Structural boundaries:** Central sulcus (anteriorly), postcentral sulcus
(posteriorly), lateral sulcus / Sylvian fissure (inferiorly), and the
superior border of the hemisphere (superiorly).
**Lobe membership:** **Parietal** — the anterior-most gyrus of the parietal
lobe, often described as the "anterior parietal lobe"[reference:0].
**Functional contents:** Primary somatosensory cortex (**S1**);
**Brodmann areas 3a, 3b, 1, and 2**[reference:1][reference:2].
**Cross-partition role:** The **only gyrus in the tree that contains a
Brodmann-area leaf** (BA3) as a child. The resolution target for
``brodmann_areas.AREA_PATHS["brodmann_area_3"]``.

Overview
--------
The **left postcentral gyrus** is the most prominent and most functionally
significant gyrus of the parietal lobe. It is a vertically oriented
convolution on the lateral surface of the left hemisphere, bounded
anteriorly by the **central sulcus** (which separates it from the precentral
gyrus / primary motor cortex) and posteriorly by the **postcentral sulcus**
(which separates it from the superior and inferior parietal lobules)[reference:3].

It is the **structural home of the primary somatosensory cortex (S1)** —
the principal cortical recipient of somatosensory afferents for the
**contralateral (right) hemibody**[reference:4]. It perceives "various
somatic sensations from the body, including touch, pressure, temperature,
and pain"[reference:5], and it contains the **sensory homunculus**, the
topographic map in which "regions of the homunculus that require high
sensory acuity and resolution take up a larger area on the somatosensory
map" (e.g., hands, face, lips)[reference:6].

**This is the canonical gyral anchor for S1, and it is the only gyrus that
contains a cross-listed Brodmann field (BA3).** Every earlier docstring in
the parietal subtree that promised a BA3 cross-listing points here. The
postcentral gyrus is where the three organizing principles —
**structural (gyrus)**, **functional (S1)**, and **cytoarchitectonic
(BA3/1/2)** — converge on a single anatomical entity.

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. It is the
**only gyrus in the parietal ``gyri/`` container that contains a
Brodmann-area leaf as a direct child**:

::

    Structural leaf (this module)        Functional / cytoarchitectonic contents
    ─────────────────────────────        ────────────────────────────────────────
    postcentral_gyrus               ──▶  primary_somatosensory_cortex (S1)
                                    ──▶  brodmann_area_3   **CROSS-LISTED**
                                           (BA3a + BA3b; rostral bank and
                                           posterior wall of central sulcus)
                                    ──▶  brodmann_area_1   (crown of gyrus)
                                    ──▶  brodmann_area_2   (caudal bank;
                                           anterior wall of postcentral sulcus)

**BA3 is the only Brodmann-area leaf that lives under a gyral container
rather than under ``brodmann_areas/``.** It is the resolution target for
``brodmann_areas.AREA_PATHS["brodmann_area_3"]``. A consumer that iterates
``brodmann_areas.LOCAL_AREAS`` will see BA1 and BA2 but **not** BA3; they
must use ``ITERABLE_AREAS`` and resolve BA3 through this gyrus.

**The postcentral gyrus is the structural anchor for S1.** S1 is a
functional region node under ``.../parietal/cortex/primary_somatosensory_cortex/``;
the postcentral gyrus is the **macroscopic surface convolution** that
contains it. The two modules are structurally linked but semantically
distinct: S1 answers "what does this region do?"; the postcentral gyrus
answers "where is it on the cortical surface?".

Cytoarchitecture
----------------
The postcentral gyrus contains **four cytoarchitectonically distinct
fields**, arranged along a rostral-to-caudal axis from the depth of the
central sulcus to the anterior wall of the postcentral sulcus:

*   **Area 3a** — a **hybrid** field at the bottom of the central sulcus,
    adjacent to the agranular primary motor area 4. It has "an overall low
    cell packing density, with few larger pyramidal cells in deep layer
    III, and an incipient layer IV"[reference:7]. It exhibits "characteristics
    of both the primary motor agranular area 4 and the koniocortical area
    3b"[reference:8], and is more related to **proprioception and
    nociception** than to cutaneous touch.

*   **Area 3b** — the **thalamic gateway** and the **first cortical stage
    of tactile processing**. It is "typical koniocortex" with "small
    granular neurons and small pyramidal neurons" that give it "an overall
    'dusty' appearance" under low-power microscopy[reference:9]. It has
    "a very high cell packing density in the supragranular layers,
    particularly layer IV"[reference:10], and receives the densest
    thalamocortical input from VPL/VPM.

*   **Area 1** — the **texture stage**, on the **crown** of the postcentral
    gyrus. It is "characterized by a well-recognizable layer IV, a
    pronounced columnar arrangement of the typically large and numerous
    pyramidal cells in layers III and V, with a marked superficial to deep
    increase in cell size in layer III"[reference:11]. It is specifically
    implicated in **texture perception**[reference:12].

*   **Area 2** — the **size/shape and proprioceptive stage**, on the
    **caudal part of the postcentral gyrus and both banks of the
    postcentral sulcus**[reference:13]. It has "a well-recognizable layer
    IV, fewer pyramidal cells in layer III, with only large pyramids
    appearing in deep layer III, and a sharp layer VI–white-matter
    border"[reference:14]. It responds preferentially to **deep body tissue**
    stimulation and has **larger receptive fields** than BA3b/BA1
    [reference:15].

**The hierarchy in one line:** BA3b (touch gateway) → BA1 (texture) →
BA2 (size/shape, proprioception); BA3a (proprioception/nociception) runs
in parallel at the anterior edge.

Function in the Human Brain
---------------------------
The left postcentral gyrus is the **structural home of left S1** and the
**left-lateralized stereognosis and complex-finger-movement hub**. Its
best-supported functions cluster into six domains:

*   **Discriminative Touch and Texture (BA3b → BA1):** BA3b is the first
    cortical recipient of cutaneous afferents; BA1 refines this into
    **texture discrimination**[reference:16]. Together they support fine-grained
    tactile analysis of surfaces.

*   **Proprioception and Limb Posture (BA3a + BA2):** BA3a processes
    **joint movement** signals; BA2 integrates these with cutaneous
    signals into a coherent representation of **limb posture and
    size/shape**[reference:17]. A small, confined lesion of the hand area in
    the postcentral gyrus can produce a **proprioceptive deficit without
    any concomitant primary motor impairment**[reference:18].

*   **Nociception (Sensory-Discriminative Aspect):** S1 is a key node in
    the **sensory-discriminative** dimension of pain, encoding the
    **location, intensity, and quality** of a nociceptive stimulus.

*   **Stereognosis (Tactile Object Recognition — Left-Lateralized):** The
    left postcentral gyrus is the **dominant cortical substrate for
    stereognosis** in some individuals. A small infarct in the **crown of
    the left postcentral gyrus (BA1)** can produce **bilateral
    astereognosis** — the inability to recognize objects by touch with
    **either** hand[reference:19]. The lesion is strategically positioned to
    "interrupt both the processing of afferent tactile information issuing
    from the primary somatosensory cortex (areas 3a and 3b) and the forward
    higher-order processing in area 2, the secondary sensory cortex, and
    the contralateral area 1"[reference:20]. This supports Oppenheim's 1906
    proposal that "the left postcentral gyrus of some individuals is
    dominant for stereognosis"[reference:21].

*   **Complex Finger Movement and Sensorimotor Integration
    (Left-Lateralized):** The left postcentral gyrus plays a **dominant
    role in sensorimotor integration for complex finger movements**.
    Patients with left-hemisphere damage in the postcentral gyrus show
    **bilateral clumsy hands, predominating on the right side**, while
    right-hemisphere damage produces only a left clumsy hand
    . This indicates a left-lateralized role in "sensory
    information processing necessary to guide the movements" of the fingers
    .

*   **Somatotopic Representation of the Right Hemibody:** The postcentral
    gyrus contains a complete **mirror-image somatotopic map** of the
    **right** hemibody (face represented bilaterally). The medial aspect
    is responsible for **lower extremity** sensation, the dorsolateral
    aspect for the **upper extremity**, and the most lateral aspect for
    the **face, lips, and tongue**[reference:24]. The gyrus also reaches the
    **medial surface**, forming the posterior part of the **paracentral
    lobule**[reference:25].

Associated Disorders
--------------------
Damage to or dysfunction of the left postcentral gyrus is associated with:

*   **Bilateral Astereognosis (Left-Lateralized — the signature left
    postcentral syndrome):** Inability to recognize objects by touch with
    **either** hand, following a **unilateral left** postcentral lesion,
    typically in BA1[reference:26]. The patient may retain the ability to
    localize stimuli on the ipsilesional hand but cannot recognize objects
    with either hand[reference:27]. This is a **left-lateralized** syndrome
    and does **not** occur with right postcentral lesions.

*   **Bilateral Clumsy Hands, Predominating on the Right
    (Left-Lateralized):** Left-hemisphere damage in the postcentral gyrus
    produces **bilateral clumsiness of complex finger movements**,
    predominating on the **right** side. Right-hemisphere damage produces
    only a **left** clumsy hand. This is a left-lateralized
    sensorimotor integration deficit.

*   **Contralateral Hemihypesthesia:** Reduced sensitivity to somatosensory
    stimuli on the **right** side of the body (face excepted, which has
    bilateral representation). A complete parietal lesion produces
    **contralateral hemianaesthesia without upper motor neuron
    signs**.

*   **Impaired Proprioception Without Motor Impairment:** A small,
    confined lesion of the hand area can produce an **isolated
    proprioceptive deficit**[reference:30].

*   **Afferent Paresis:** Lesions on the postcentral gyrus may cause
    **afferent paresis** — significant sensory deficits in the
    contralesional upper extremity with "slowness or inability to perform
    motor tasks only in the absence of visual guidance"[reference:31].

*   **Tactile Extinction and Somatosensory Disturbances:** Simple
    somatosensory disturbances including **tactile extinction**,
    contralateral pain, and paresthesias[reference:32].

*   **Vascular Syndromes (ACA vs. MCA):** The postcentral gyrus is
    supplied by **both the anterior and middle cerebral arteries**. The
    **ACA** perfuses the **medial third** (lower limb representation); the
    **MCA** perfuses the **lateral two-thirds** (upper limb and face
    representation)[reference:33]. An **MCA stroke** produces sensory loss
    in the **upper limbs**; an **ACA stroke** produces sensory loss in the
    **lower limbs**[reference:34].

**What is NOT here:** The **right-hemibody** representation, the
**right-lateralized spatial-attention** functions, and the
**contralateral-only** astereognosis phenotype are properties of the
**right** postcentral gyrus module. They are **not** part of this left
module and must not be imported from the right twin.

Lateralization Notes
--------------------
This is the **left** postcentral gyrus module. The lateralization landscape
is **left-loaded** at the functional level, mirroring the left-loaded
pattern of the S1 pair and the BA1/BA2/BA5 Brodmann leaves:

*   **Left-Lateralized Functions (unique to this twin):**
    - **Bilateral astereognosis** — a small left BA1 infarct produces
      bilateral loss; right lesions produce contralateral-only loss
      [reference:35].
    - **Bilateral clumsy hands predominating on the right** — left
      postcentral lesions impair complex finger movements bilaterally;
      right lesions impair only the left hand.
    - **Dominant sensorimotor integration for complex finger
      movements**.

*   **Right-Lateralized Functions (contrast — absent here):**
    - **Spatial-attention weighting** — the right S1 (in the right
      postcentral gyrus) shows stronger cortical facilitation during
      **left-hand** stimulation (see right postcentral gyrus module).
    - **Contralateral-only astereognosis** — a right postcentral lesion
      produces left-hand astereognosis **only**; it does not produce
      bilateral loss.

*   **Symmetric Functions (bilateral properties of the postcentral
    gyrus):**
    - BA3b thalamic gateway and first cortical stage of tactile processing.
    - BA3b → BA1 → BA2 hierarchical processing (texture → size/shape).
    - BA3a proprioceptive and nociceptive processing.
    - Somatotopic mirror representations (BA3b ↔ BA1), with hemibody
      flipped (left postcentral → right hemibody).
    - Nociceptive sensory-discriminative processing (area 1).
    - The medial extension into the paracentral lobule (posterior part)
      [reference:38].

**A consumer that assumes "left postcentral gyrus = symmetric" will miss
the two left-lateralized syndromes (bilateral astereognosis, bilateral
clumsy hands) that define the left twin.** The postcentral gyrus pair is
**left-loaded**, exactly like the S1 pair and the BA1/BA2/BA5 leaves.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../frontal/gyri/precentral_gyrus`` or
    ``.../frontal/gyri/paracentral_lobule``. The precentral gyrus is a
    separate structural entity in the frontal lobe; the paracentral lobule's
    frontal half is documented under the frontal lobe.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural leaf with a cross-partition child (BA3).** This is the
    **only** gyrus that contains a Brodmann-area leaf. The
    ``brodmann_area_3`` child is the resolution target for
    ``brodmann_areas.AREA_PATHS["brodmann_area_3"]``. Consumers must
    **not** assume that all Brodmann leaves live under
    ``brodmann_areas/``.
*   **Structural parity with right postcentral gyrus.** Left and right
    postcentral gyrus modules must be structurally interchangeable so
    bilateral consumers can iterate hemispheres generically. The
    cytoarchitectonic contents (BA3/1/2) and the hierarchical processing
    are **symmetric**; only the lateralization prose (bilateral
    astereognosis, bilateral clumsy hands) and the contralateral target
    differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri import postcentral_gyrus

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.gyri.postcentral_gyrus"
    )

For the cross-listed BA3 (the only Brodmann-area leaf under a gyrus)::

    from ...parietal.gyri.postcentral_gyrus import brodmann_area_3

**Do not** attempt to resolve BA3 via ``brodmann_areas.brodmann_area_3`` —
there is no such module. Use ``brodmann_areas.AREA_PATHS["brodmann_area_3"]``
or import directly from this gyrus.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pcg_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.gyri.postcentral_gyrus"
        )
        # resolve pcg_path through the memory/recall layer

References
----------
*   **Postcentral gyrus overview:** *Neuroanatomy, Postcentral Gyrus*
    (StatPearls, 2023), NCBI Bookshelf NBK549825[reference:39]. The postcentral
    gyrus lies between the central and postcentral sulci, contains the
    primary somatosensory cortex (BA3b, 1, 2), perceives contralateral
    somatic sensations, contains the sensory homunculus, and is supplied by
    the ACA (medial third) and MCA (lateral two-thirds).
*   **Cytoarchitecture:** *Intraparietal Sulcus* (ScienceDirect)[reference:40].
    Detailed cytoarchitectonic descriptions of areas 3a, 3b, 1, and 2;
    confirmation of the parcelation by von Economo and Koskinas (1925),
    Bailey and von Bonin (1951), Sarkissov et al. (1949), Braak (1980), and
    White et al. (1997). *Postcentral Gyrus* (ScienceDirect)[reference:41].
    Area 3b as koniocortex; area 3a as hybrid cortex; area 1 on the crown;
    area 2 on the caudal bank.
*   **Left S1 stereognosis dominance:** Moll, J., et al. (2017). *Cogn
    Behav Neurol*, 30(3), 102–115. "Hemispheric Dominance for Stereognosis
    in a Patient With an Infarct of the Left Postcentral Sensory Hand
    Area"[reference:42]. A small infarct in the crown of the left postcentral
    gyrus (BA1) produced **bilateral astereognosis**, supporting Oppenheim's
    1906 proposal.
*   **Left S1 complex finger movement dominance:** Okuda, B., et al.
    (1995). *Exp Brain Res*, 106(3), 493–498. "The role of the left
    somatosensory cortex in human hand movement". Left-hemisphere
    damage produced **bilateral clumsy hands predominating on the right**;
    right-hemisphere damage produced only a left clumsy hand. Suggests a
    dominant role of the left somatosensory cortex in sensorimotor
    integration for complex finger movements.
*   **Proprioceptive deficit without motor impairment:** *Bilateral hand
    representations in human primary proprioceptive areas* (2011),
    *Neuropsychologia*, 49(12), 3383–3391[reference:44].
*   **Afferent paresis:** *Desempenho sensório-motor na paresia aferente*
    (2015), *Periodicos UNINOVE*[reference:45].
*   **Vascular territory and clinical syndromes:** *Giro pós-central*
    (IMAIOS e-Anatomy)[reference:46]. ACA stroke → lower-limb sensory loss;
    MCA stroke → upper-limb sensory loss.
*   **Somatosensory evoked potentials and lesion localization:**
    Mauguière, F., Desmedt, J.E., & Courjon, J. (1983). *Brain*, 106(2),
    271–311. Small postcentral lesions produced astereognosis
    and reduced/eliminated N20 and P27 SEP components.
*   **Face area lesion effects:** *Effects of lesions invading the
    postcentral gyrus on somatosensory thresholds on the face* (1997),
    *Neuropsychologia*, 35(7), 953–961[reference:48].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   Terminologia Anatomica (FIPAT, 2019) — gyrus postcentralis.
*   NeuroNames — Postcentral gyrus (left); FMA — left postcentral gyrus.
"""