"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas.brodmann_area_5
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── brodmann_areas
                        └── brodmann_area_5   <-- THIS MODULE

**Primary synonym:** Brodmann Area 5 (BA5); Somatosensory Association Cortex;
Preparaparietal area.
**Cytoarchitectonic designation:** Area 5 of Brodmann (1909); **Area praeparietalis**
in Terminologia Anatomica.
**Part of:** Superior parietal lobule (SPL) — together with BA7.
**Location:** Anterosuperior portion of the right superior parietal lobule,
immediately posterior to the postcentral sulcus, across from BA2.

Overview
--------
Brodmann Area 5 (BA5) is the **first association cortex** in the parietal
Brodmann sequence. It sits at the junction between primary somatosensory
cortex (S1: BA3/1/2) and the polymodal posterior parietal cortex (BA7), and
it is best characterized as **unimodal somatosensory association cortex**:
it receives its driving input from S1 and from proprioceptive pathways, but
it performs computations that go beyond raw feature registration.

Cytoarchitectonically, BA5 is thicker than S1 fields, with a **less prominent
layer IV** and larger pyramidal cells in layer III — the signature of a
cortico-cortical association area rather than a thalamic recipient zone.
Critically, **direct thalamic input from VPL/VPM stops at the BA2/BA5
border**; BA5 is not a primary sensory area. Its responses to passive touch
are weaker and more context-dependent than those of S1, and a higher fraction
of its neurons are tuned to **joint configuration, limb posture, and
movement-related signals** rather than to cutaneous features alone.

BA5 occupies a **central anatomical position** between primary motor cortex
(BA4) rostrally, primary somatosensory cortex (BA3b/BA2) anteriorly, and the
polymodal association areas of BA7 posteriorly. This position
predicts its functional profile: it is the first parietal field where
somatosensation, proprioception, and motor planning begin to converge.

This module is structurally identical to the left-hemisphere twin at
``.../left/cortex/parietal/brodmann_areas/brodmann_area_5``. The
**cytoarchitectonic identity and intrinsic computational role of BA5 are the
same in both hemispheres**; only the contralateral target of its sensory input
and the lateralized functional weightings (below) differ.

Function in the Human Brain
---------------------------
BA5 converts **somatic features** (BA1/BA2) into **body-centred action-
relevant representations**. Its best-supported functions are:

*   **Stereognosis (Tactile Object Recognition):** BA5 is a core node of the
    network that lets us **identify objects by feel**. Lesions here produce
    **astereognosia** — the inability to recognize objects by touch despite
    preserved elementary sensation. This is the classical
    clinical signature of BA5 damage, contralateral to the lesion on the right
    side (see the lateralization note below).

*   **Proprioceptive Integration and Limb Posture:** BA5 is the **proprioceptive
    analogue of BA2**: it performs complex analysis of **whole joint movements
    and limb postures**, combining cutaneous and joint-angle signals into a
    coherent representation of where the limb is in space. It is
    more posture-weighted than BA2, which is more feature-weighted.

*   **Motor Planning and Preparation:** BA5 is active during the **preparation
    and execution of goal-directed limb movements**. Human fMRI shows a
    **lateral-to-medial gradient** in BA5 for hand vs. foot movement planning,
    and this region is functionally connected with hand and foot motor
    regions. BA5 is best described as **sensorimotor** rather than
    purely sensory.

*   **Tactile Localization:** BA5 contributes to **localizing a touch on the
    body surface**, particularly when the localization requires integrating
    posture information (e.g., localizing a touch on a crossed limb).

*   **Body Ownership and Body Schema:** BA5 participates in the **body schema**
    — the online, action-oriented model of the body's configuration. It
    contributes to the feeling that a limb belongs to oneself and to the
    spatial unity of the body.

*   **Visuo-Somatic Convergence for Reaching:** BA5 receives visual input via
    the parietal reach region (PRR) and adjacent intraparietal areas, and it
    contributes to **visually guided reaching** toward objects. This is the
    beginning of the transition from somatosensation to the polymodal spatial
    representations of BA7.

*   **Pain Localization (Sensory-Discriminative Aspect):** BA5, like BA1,
    participates in the **sensory-discriminative** dimension of pain —
    particularly the localization and intensity encoding of nociceptive
    stimuli — rather than the affective dimension.

Associated Disorders
--------------------
Damage to or dysfunction of the right BA5 is associated with:

*   **Astereognosis (Tactile Agnosia):** Inability to recognize objects by
    touch with the **left hand** despite intact primary sensation. This is
    the **most characteristic BA5 deficit** on the right side.
*   **Impaired Tactile Localization:** Difficulty identifying where on the
    **left** side of the body a touch occurred, especially when posture is
    non-canonical.
*   **Impaired Limb Position Sense:** Proprioceptive deficits of the
    **left** limb, contributing to **sensory ataxia** when severe.
*   **Left-hand Constructional / Manipulation Difficulties** (when the lesion
    extends into adjacent BA7/BA39 territory).

**Important lateralization caveat — what is NOT here:** The **ideomotor
apraxia** and **bilateral astereognosis** syndromes described for the left BA5
are **left-lateralized**. They do **not** apply symmetrically to the right
BA5. A small right BA5 lesion produces contralateral (left-hand) deficits
only; it does not produce bilateral loss or a praxis syndrome. See
`Lateralization Notes` below.

Lateralization Notes
--------------------
This is the **right** hemisphere BA5 module.

*   **Contralateral Somatosensory Representation:** Right BA5 processes
    proprioceptive and tactile information from the **left side of the body**
    (face excepted, which is bilaterally represented).

*   **No Left-Dominant Praxis Role.** Unlike the left BA5, the right BA5 is
    **not** a core node of the praxis network. It contributes to **left-hand**
    skilled movements, but the dominant praxis substrate remains
    left-hemispheric (BA5 + BA39/BA40 + premotor hand area) in most
    right-handers. **Do not** inherit the left BA5's "ideomotor apraxia" claim
    into this module — the right-sided counterpart of a left BA5 lesion is a
    contralateral manipulation deficit, not a praxis syndrome.

*   **No Bilateral-Loss Stereognosis.** The right BA5 contributes to tactile
    object recognition for the **left hand**, but without the
    left-lateralized, bilateral-loss phenotype described for the left BA5
    twin. Right BA5 lesions → left-hand astereognosis only.

*   **No Left-Dominant Movement-Execution Weighting.** The left BA5's
    preferential engagement during *execution* of upper-limb movements (as
    opposed to mere motor imagery) is part of the left-lateralized praxis
    system. Right BA5 shows the same hand/foot gradient in
    motor *planning* (a symmetric property of the SPL), but without the
    left-hemisphere execution-dominance overprint.

*   **Hand/Foot Planning Gradient Is Bilateral and Symmetric.** The
    lateral-to-medial hand/foot gradient in BA5 (Heed et al., 2011) is a
    **general property of human PPC**, not a left-lateralized one. This
    function should be documented verbatim on both sides.

*   **No Right-Lateralized Neglect Role.** Unlike BA7 and the inferior
    parietal lobule (BA39/BA40), BA5 is **not** a primary node of the
    right-lateralized spatial-attention / neglect network. The hemispatial
    neglect syndrome belongs to right BA7/BA39/BA40 territory, not to BA5.
    Do **not** add a neglect claim to this module even though it is on the
    right side — BA5 sits outside that network.

Design Contract
---------------
*   **No side effects on import.** This `__init__.py` is a pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No hormone imports here.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **S1 → BA5 boundary criterion.** Direct thalamic input from VPL/VPM stops
    at the BA2/BA5 border. BA5 is **association** cortex: it does not receive
    first-order thalamic somatosensory input, and it does not respond
    obligatorily to passive touch. This single criterion cleanly separates BA5
    from BA1/BA2 and is hemisphere-symmetric.
*   **BA5/BA7 boundary.** BA5 is **unimodal somatosensory association cortex**;
    BA7 is **polymodal association cortex** (somatosensory + visual +
    oculomotor). The boundary is at the anterior border of BA7 within the
    superior parietal lobule. BA5 is the *last* unimodal parietal
    field; BA7 is the first polymodal one. Hemisphere-symmetric criterion.
*   **Structural parity with left BA5.** Left and right BA5 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. Only the path segment (`right` vs `left`) and the
    lateralization prose differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas import brodmann_area_5

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.brodmann_areas.brodmann_area_5"
    )

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba5_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.brodmann_areas.brodmann_area_5"
        )
        # resolve ba5_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
*   NeuroNames — Brodmann area 5 (right).
*   FMA — Brodmann area 5 (right member); Terminologia Anatomica: area praeparietalis.
*   Scheperjans, F., et al. (2008). *Cereb Cortex*, 18(4), 846–867.
    (Observer-independent cytoarchitectonic mapping of human SPC: BA5 and BA7).
*   Heed, T., et al. (2011). *J Neurosci*, 31(8), 3066–3076. (Hand/foot gradient
    in human PPC — a bilateral, symmetric property of BA5).
*   Bodegàrd, A., et al. (2001). *Neuron*, 31(2), 317–328. (Hierarchical
    processing in somatosensory cortex).
*   Iwamura, Y. (1998). *Curr Opin Neurobiol*, 8(4), 522–528. (Joint and posture
    coding in parietal area 5).
*   Moll, J., et al. (2017). *Cogn Behav Neurol*, 30(3), 102–115. (Left
    superior parietal lesions, astereognosis, and apraxia — cited here only to
    mark that the right BA5 does **not** share the bilateral-loss or praxis
    phenotype).
*   Committeri, G., et al. (2007). *Neuropsychologia*, 45(4), 745–755. (Right
    parietal contribution to personal neglect — contrast case; BA5 itself is
    not the neglect node).
"""