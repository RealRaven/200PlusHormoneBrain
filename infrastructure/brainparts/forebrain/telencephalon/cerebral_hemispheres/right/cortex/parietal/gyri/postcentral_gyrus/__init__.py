"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.gyri.postcentral_gyrus
================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── gyri
                        └── postcentral_gyrus   <-- THIS MODULE

**Primary synonym:** Postcentral gyrus (right); Gyrus postcentralis;
Postcentral convolution; Posterior central gyrus.
**Organizing principle:** **Structural / gyral partition** — a single
macroscopic gyrus on the lateral surface of the hemisphere.
**Structural boundaries:** Central sulcus (anteriorly), postcentral sulcus
(posteriorly), lateral sulcus / Sylvian fissure (inferiorly), and the
superior border of the hemisphere (superiorly).
**Lobe membership:** **Parietal** — the anterior-most gyrus of the right
parietal lobe, often described as the "anterior parietal lobe".
**Functional contents:** Primary somatosensory cortex (**S1**);
**Brodmann areas 3a, 3b, 1, and 2**.
**Cross-partition role:** The **only gyrus in the tree that contains a
Brodmann-area leaf** (BA3) as a child. The resolution target for
``brodmann_areas.AREA_PATHS["brodmann_area_3"]``.

Overview
--------
The **right postcentral gyrus** is the most prominent and most functionally
significant gyrus of the right parietal lobe. It is a vertically oriented
convolution on the lateral surface of the right hemisphere, bounded
anteriorly by the **central sulcus** (which separates it from the precentral
gyrus / primary motor cortex) and posteriorly by the **postcentral sulcus**
(which separates it from the superior and inferior parietal lobules).

It is the **structural home of the primary somatosensory cortex (S1)** —
the principal cortical recipient of somatosensory afferents for the
**contralateral (left) hemibody**. It perceives "various
somatic sensations from the body, including touch, pressure, temperature,
and pain", and it contains the **sensory homunculus**, the
topographic map in which "regions of the homunculus that require high
sensory acuity and resolution take up a larger area on the somatosensory
map" (e.g., hands, face, lips).

**This is the canonical gyral anchor for right S1, and it is the only gyrus
that contains a cross-listed Brodmann field (BA3).** Every earlier docstring
in the right parietal subtree that promised a BA3 cross-listing points here.
The postcentral gyrus is where the three organizing principles —
**structural (gyrus)**, **functional (S1)**, and **cytoarchitectonic
(BA3/1/2)** — converge on a single anatomical entity.

**This is the right-hemisphere twin of the left postcentral gyrus, and its
lateralization profile is not a simple mirror.** The cytoarchitectonic
organization and the hierarchical processing of S1 are **hemisphere-
symmetric**; however, the lateralized functional weightings are **right-
loaded in specific domains**. The **left** postcentral gyrus carries the
two classic left-lateralized syndromes (**bilateral astereognosis** and
**bilateral clumsy hands**); the **right** postcentral gyrus carries a
distinct **right-lateralized weighting for proprioception** (both
contralateral and ipsilateral) and a **right-lateralized facilitation for
the non-dominant (left) hand** — documented in detail below.

Two-Partition Context
---------------------
This module is a **structural leaf** under the gyral aggregator. It is the
**only gyrus in the right parietal ``gyri/`` container that contains a
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
``brodmann_areas.AREA_PATHS["brodmann_area_3"]`` on the **right** side.

**The postcentral gyrus is the structural anchor for right S1.** S1 is a
functional region node under ``.../parietal/cortex/primary_somatosensory_cortex/``;
the postcentral gyrus is the **macroscopic surface convolution** that
contains it.

Cytoarchitecture
----------------
The right postcentral gyrus contains **four cytoarchitectonically distinct
fields**, arranged along a rostral-to-caudal axis from the depth of the
central sulcus to the anterior wall of the postcentral sulcus. The
cytoarchitecture is **hemisphere-symmetric** and is copied verbatim from
the left postcentral gyrus twin:

*   **Area 3a** — a **hybrid** field at the bottom of the central sulcus,
    adjacent to the agranular primary motor area 4. More related to
    **proprioception and nociception** than to cutaneous touch.

*   **Area 3b** — the **thalamic gateway** and the **first cortical stage
    of tactile processing**. Typical koniocortex with a very high cell
    packing density in the supragranular layers, particularly layer IV;
    receives the densest thalamocortical input from VPL/VPM.
    BA3b has the **narrowest fingertip tuning** (2.6 fingertips FWHM),
    increasing posteriorly to **4.0 in BA1 and 9.3 in BA2** — direct
    evidence for the hierarchical processing cascade[reference:0].

*   **Area 1** — the **texture stage**, on the **crown** of the postcentral
    gyrus. Well-recognizable layer IV, pronounced columnar arrangement of
    large pyramidal cells in layers III and V. Specifically
    implicated in **texture perception**.

*   **Area 2** — the **size/shape and proprioceptive stage**, on the
    **caudal part of the postcentral gyrus and both banks of the
    postcentral sulcus**. Responds preferentially to **deep body tissue**
    stimulation and has **larger receptive fields** than BA3b/BA1.
    BA2 contains neurons with **bilateral receptive fields** that extend
    into BA5[reference:1].

**The hierarchy in one line:** BA3b (touch gateway) → BA1 (texture) →
BA2 (size/shape, proprioception); BA3a (proprioception/nociception) runs
in parallel at the anterior edge.

Function in the Human Brain
---------------------------
The right postcentral gyrus is the **structural home of right S1** and the
**right-lateralized proprioceptive and non-dominant-hand facilitation hub**.
Its best-supported functions cluster into six domains:

*   **Discriminative Touch and Texture (BA3b → BA1):** BA3b is the first
    cortical recipient of cutaneous afferents from the **left** hand and
    body; BA1 refines this into **texture discrimination**. Right S1
    neurons are tuned primarily to somatosensory inputs from the
    **contralateral (left) hand** during hand shaping and hand-object
    interactions[reference:2].

*   **Proprioception and Limb Posture (BA3a + BA2 — Right-Lateralized):**
    BA3a processes **joint movement** signals; BA2 integrates these with
    cutaneous signals into a coherent representation of **limb posture and
    size/shape**. The right hemisphere carries a **general lateralization
    for proprioception**, regardless of which limb is active. In a knee
    joint position sense (JPS) study, **significantly greater responses**
    were observed in the right hemisphere (including the right precentral
    gyrus and right rolandic operculum) for both legs.
    Furthermore, a **unilateral lesion in the right postcentral gyrus
    affects bilateral hand proprioception** — a patient with a small,
    confined right postcentral lesion showed a **significant leftward shift
    of perceived locations when reaching with the ipsilesional right hand
    to the contralesional left hand**, and an opposite rightward shift when
    reaching with the left hand to the right hand's position
    [reference:3]. This suggests **integration of contralateral and
    ipsilateral proprioceptive information already at this early processing
    stage**, possibly mediated by callosal connections[reference:4].

*   **Nociception (Sensory-Discriminative Aspect):** S1 is a key node in
    the **sensory-discriminative** dimension of pain, encoding the
    **location, intensity, and quality** of a nociceptive stimulus. This
    function is **symmetric**.

*   **Somatotopic Representation of the Left Hemibody:** The postcentral
    gyrus contains a complete **mirror-image somatotopic map** of the
    **left** hemibody (face represented bilaterally). The medial aspect is
    responsible for **lower extremity** sensation, the dorsolateral aspect
    for the **upper extremity**, and the most lateral aspect for the
    **face, lips, and tongue**. The gyrus also reaches the **medial
    surface**, forming the posterior part of the **paracentral lobule**.

*   **Right-Lateralized Facilitation for the Non-Dominant (Left) Hand
    (unique to this twin):** The **right S1 and right somatosensory
    association area (SA) show stronger cortical facilitation during
    left-hand stimulation but not right-hand stimulation**. In an fNIRS study of 31 right-handed participants, "stronger cortical facilitation
    was found in the right primary somatosensory cortex (S1) and right
    somatosensory association area (SA) during left-hand stimulation but
    not right-hand stimulation"[reference:5]. This
    asymmetric activation for the less-preferred (left) hand "might
    contribute to considerably reinforce [the] sensorimotor network just
    with passive vibrotactile cutaneous stimulation". The
    right postcentral gyrus therefore carries a **right-lateralized
    weighting for the non-dominant hand** that the left postcentral gyrus
    does not have.

*   **Sensorimotor Integration for Hand Shaping (Right-Lateralized
    Emphasis):** Right S1 neurons are **tuned primarily to somatosensory
    inputs from the contralateral (left) hand** during hand shaping and
    hand-object interactions[reference:8]. S1 neurons in the right
    hemisphere respond primarily to actions of the contralateral hand
    during reach (hand shaping), contact, grasp, and pull, and also to
    object release from the hand — providing tactile and proprioceptive
    information about object acquisition for the **contralateral (left)
    hand**[reference:9]. This is a **contralateral** function that is
    symmetric with the left hemisphere, but the right S1 additionally
    carries the non-dominant-hand facilitation weighting described above.

Associated Disorders
--------------------
Damage to or dysfunction of the right postcentral gyrus is associated with:

*   **Contralateral (Left) Astereognosis (Contralateral-Only — the
    right-postcentral phenotype):** Lesions to the postcentral gyrus of
    the parietal lobe produce **astereognosis** — the inability to
    recognize objects by touch despite intact elementary sensation
    . The damage is "usually being expressed **contralaterally**" — on
    the **left hand** for a right-hemisphere lesion[reference:10]. Only
    **direct damage to or an undercutting of the anterior part of the
    middle third of the postcentral gyrus** causes impairment of size and
    shape discrimination (astereognosis) **contralateral to the lesion**
    [reference:11]. This is **not** the bilateral astereognosis phenotype
    of the left postcentral gyrus; a right-sided lesion does **not**
    produce bilateral loss.

*   **Bilateral Hand Proprioceptive Deficit (Right-Lateralized):** A small,
    confined lesion of the hand area in the right postcentral gyrus
    produces a **proprioceptive deficit without any concomitant primary
    motor impairment**. Unilateral right postcentral lesion affects
    **bilateral hand proprioception**: the patient showed a significant
    leftward shift of perceived locations when reaching with the
    ipsilesional right hand to the contralesional left hand, and an
    opposite rightward shift when reaching with the left hand to the right
    hand's position[reference:12]. This is a **right-lateralized** effect
    — the left postcentral gyrus does not carry the same bilateral
    proprioceptive weighting.

*   **Impaired Proprioception Without Motor Impairment:** A small,
    confined lesion of the hand area can produce an **isolated
    proprioceptive deficit**[reference:13].

*   **Contralateral (Left) Hemihypesthesia:** Reduced sensitivity to
    somatosensory stimuli on the **left** side of the body (face excepted,
    which has bilateral representation).

*   **Afferent Paresis:** Lesions on the postcentral gyrus may cause
    **afferent paresis** — significant sensory deficits in the
    contralesional upper extremity with slowness or inability to perform
    motor tasks only in the absence of visual guidance. This is a
    **contralateral** syndrome, symmetric with the left side.

*   **Tactile Extinction and Somatosensory Disturbances:** Simple
    somatosensory disturbances including **tactile extinction**,
    contralateral pain, and paresthesias.

*   **Vascular Syndromes (ACA vs. MCA):** The postcentral gyrus is
    supplied by **both the anterior and middle cerebral arteries**. The
    **ACA** perfuses the **medial third** (lower limb representation); the
    **MCA** perfuses the **lateral two-thirds** (upper limb and face
    representation). An **MCA stroke** produces sensory loss in the
    **upper limbs**; an **ACA stroke** produces sensory loss in the
    **lower limbs**. This vascular organization is hemisphere-symmetric.

**What is NOT here:** **Bilateral astereognosis**, **bilateral clumsy
hands predominating on the right**, and **left-lateralized complex finger
movement dominance** are **left-lateralized** functions of the left
postcentral gyrus. They do **not** occur with right postcentral lesions.
They are documented in the left postcentral gyrus module and are
**explicitly denied here** (see `Lateralization Notes`). A right
postcentral lesion does **not** produce bilateral astereognosis or
bilateral clumsy hands.

Lateralization Notes
--------------------
This is the **right** postcentral gyrus module. The lateralization
landscape is **right-loaded in proprioception and non-dominant-hand
facilitation**, and **left-loaded in stereognosis and complex finger
movement** — a **mixed pattern** that is qualitatively different from the
purely left-loaded S1 pair at the functional-region level:

*   **Right-Lateralized Functions (unique to this twin):**
    - **Bilateral hand proprioception** — a unilateral right postcentral
      lesion affects proprioceptive processing for **both hands**[reference:14].
    - **General right-hemisphere lateralization for proprioception** of
      the lower limbs, regardless of which limb is active[reference:15].
    - **Stronger cortical facilitation in right S1 and right SA during
      left-hand (non-dominant) stimulation**[reference:16].

*   **Left-Lateralized Functions (contrast — absent here, explicitly
    denied):**
    - **Bilateral astereognosis** — a small left BA1 infarct produces
      bilateral loss; a right lesion produces **contralateral-only** loss
      [reference:18].
    - **Bilateral clumsy hands predominating on the right** — left
      postcentral lesions impair complex finger movements bilaterally;
      right lesions impair only the left hand.
    - **Dominant sensorimotor integration for complex finger movements**.

*   **Symmetric Functions (bilateral properties of the postcentral gyrus,
    copied verbatim from the left twin):**
    - BA3b thalamic gateway and first cortical stage of tactile processing.
    - BA3b → BA1 → BA2 hierarchical processing (texture → size/shape),
      with fingertip tuning widths of 2.6 (BA3b), 4.0 (BA1), and 9.3
      (BA2) fingertips FWHM[reference:19].
    - BA3a proprioceptive and nociceptive processing.
    - Somatotopic mirror representations (BA3b ↔ BA1), with hemibody
      flipped (right postcentral → **left** hemibody).
    - Nociceptive sensory-discriminative processing (area 1).
    - The medial extension into the paracentral lobule (posterior part).
    - Vascular territory (ACA medial third; MCA lateral two-thirds).

**A consumer that assumes "right postcentral gyrus = symmetric" will miss
the right-lateralized bilateral proprioception and left-hand facilitation
weightings.** A consumer that assumes "right postcentral gyrus = left
postcentral gyrus" will incorrectly import the left-lateralized bilateral
astereognosis and bilateral clumsy hands claims, which are **absent**
here. The postcentral gyrus pair is **mixed-loaded**: the left twin is
left-loaded for stereognosis and complex finger movement; the right twin is
right-loaded for proprioception and non-dominant-hand facilitation.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../frontal/gyri/precentral_gyrus`` or
    ``.../frontal/gyri/paracentral_lobule``. The precentral gyrus is a
    separate structural entity in the frontal lobe; the paracentral lobule's
    frontal half is documented under the frontal lobe.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural leaf with a cross-partition child (BA3).** This is the
    **only** gyrus that contains a Brodmann-area leaf. The
    ``brodmann_area_3`` child is the resolution target for the **right**
    ``brodmann_areas.AREA_PATHS["brodmann_area_3"]``. Consumers must
    **not** assume that all Brodmann leaves live under
    ``brodmann_areas/``.
*   **Structural parity with left postcentral gyrus.** Left and right
    postcentral gyrus modules must be structurally interchangeable so
    bilateral consumers can iterate hemispheres generically. The
    cytoarchitectonic contents (BA3/1/2) and the hierarchical processing
    are **symmetric**; only the lateralization prose (bilateral
    proprioception, non-dominant-hand facilitation vs. bilateral
    astereognosis, bilateral clumsy hands) and the contralateral target
    differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.gyri import postcentral_gyrus

Resolve by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.gyri.postcentral_gyrus"
    )

For the cross-listed BA3 (the only Brodmann-area leaf under a gyrus)::

    from ...parietal.gyri.postcentral_gyrus import brodmann_area_3

**Do not** attempt to resolve BA3 via ``brodmann_areas.brodmann_area_3`` —
there is no such module. Use
``brodmann_areas.AREA_PATHS["brodmann_area_3"]`` or import directly from
this gyrus.

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
    (StatPearls, 2023), NCBI Bookshelf NBK549825. The postcentral
    gyrus lies between the central and postcentral sulci, contains the
    primary somatosensory cortex (BA3b, 1, 2), perceives contralateral
    somatic sensations, contains the sensory homunculus, and is supplied by
    the ACA (medial third) and MCA (lateral two-thirds).
*   **Cytoarchitecture and hierarchical processing:** *Intraparietal Sulcus*
    (ScienceDirect); *Postcentral Gyrus* (ScienceDirect). BA3b as
    koniocortex; BA3a as hybrid cortex; BA1 on the crown; BA2 on the
    caudal bank. **Fingertip tuning widths:** BA3b (2.6), BA1 (4.0), BA2
    (9.3) fingertips FWHM — direct evidence for the hierarchical cascade
    [reference:20]. **Bilateral receptive fields in BA2** extending into BA5
    [reference:21].
*   **Right S1 contralateral (left) hand tuning:** *Rasters and PSTHs for a
    primary somatosensory cortex (S1) neuron in area 2* (J Neurophysiol).
    S1 neurons of the right hemisphere are **tuned primarily to
    somatosensory inputs from the contralateral (left) hand** during hand
    shaping and hand-object interactions[reference:22].
*   **Right postcentral gyrus bilateral proprioception:** *Bilateral hand
    representations in human primary proprioceptive areas* (2011),
    *Neuropsychologia*, 49(12), 3383–3391. A small, confined lesion of the
    hand area in the right postcentral gyrus produced a proprioceptive
    deficit without motor impairment; the patient showed a **significant
    leftward shift of perceived locations when reaching with the
    ipsilesional right hand to the contralesional left hand**, and an
    opposite rightward shift for the reverse condition — demonstrating
    **bilateral proprioceptive processing** at this early stage, possibly
    via callosal connections[reference:23].
*   **Right hemisphere lateralization for proprioception:** *Right
    hemisphere brain lateralization for knee proprioception among
    right-limb dominant individuals* (2023), *Europe PMC*. Significantly
    greater responses were observed mainly in the **right hemisphere**
    (precentral gyrus, insula, rolandic operculum) for knee joint position
    sense, **regardless of which limb was active**, supporting a general
    right-hemisphere lateralization for proprioception[reference:24].
*   **Right S1 left-hand facilitation:** Jin, S.H., Lee, S.H., Yang, S.T.,
    & An, J. (2020). "Hemispheric asymmetry in hand preference of
    right-handers for passive vibrotactile perception: an fNIRS study."
    *Scientific Reports*, 10, 13423. **Stronger cortical facilitation was
    found in the right primary somatosensory cortex (S1) and right
    somatosensory association area (SA) during left-hand stimulation but
    not right-hand stimulation**[reference:25]. The asymmetric
    activation "might contribute to considerably reinforce [the]
    sensorimotor network just with passive vibrotactile cutaneous
    stimulation".
*   **Right postcentral lesion — contralateral-only astereognosis:**
    *Stereognosis* (Springer); *Astereognosis* (JAMA Neurology, 1976;
    PubMed 1976; *Arch Neurol*, 33(8), 543–550). Lesions to the postcentral
    gyrus are implicated in astereognosis, with damage "usually being
    expressed **contralaterally**"[reference:28]. Only direct damage to or
    undercutting of the anterior part of the middle third of the
    postcentral gyrus caused impairment of size and shape discrimination
    (astereognosis) **contralateral to the lesion**[reference:29].
*   **Proprioceptive deficit without motor impairment:** *Bilateral hand
    representations in human primary proprioceptive areas* (2011),
    *Neuropsychologia*, 49(12), 3383–3391.
*   **Vascular territory and clinical syndromes:** *Giro pós-central*
    (IMAIOS e-Anatomy). ACA stroke → lower-limb sensory loss;
    MCA stroke → upper-limb sensory loss.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   Terminologia Anatomica (FIPAT, 2019) — gyrus postcentralis.
*   NeuroNames — Postcentral gyrus (right); FMA — right postcentral gyrus.
"""