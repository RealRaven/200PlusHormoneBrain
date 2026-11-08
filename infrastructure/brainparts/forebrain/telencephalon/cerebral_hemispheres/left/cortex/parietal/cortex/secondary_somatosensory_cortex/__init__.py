"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex.secondary_somatosensory_cortex
==============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── cortex
                        └── secondary_somatosensory_cortex   <-- THIS MODULE

**Primary synonym:** Secondary Somatosensory Cortex (S2), left; Left S2;
Somatosensory Area II; SII.
**Organizing principle:** **Functional–anatomical region** — the second
cortical stage of somatosensory processing.
**Brodmann constitution:** **No single Brodmann field.** S2 corresponds to
the **OP1–OP4 cytoarchitectonic complex** of the parietal operculum
(Eickhoff et al., 2006). BA40 and BA43 are sometimes cited loosely, but
neither is a precise anchor — BA40 is the supramarginal gyrus (phonological/
praxic), and BA43 is the subcentral area, which does not capture the full
S2 territory.
**Part of:** The **functional partition** of the left parietal lobe
(``.../parietal/cortex``), alongside S1 and PPC.
**Cytoarchitectonic siblings:** **None.** This is the **boundary case** of
the two-partition architecture: a functional region with **no unambiguous
Brodmann anchor** in the current tree. See "Two-Partition Context" below.

Overview
--------
The **left secondary somatosensory cortex (S2)** is the second cortical
stage of somatosensory processing. It lies in the **parietal operculum**,
on the upper bank of the lateral sulcus (Sylvian fissure), posterior to S1
and adjacent to the insula. It was first described by Adrian (1940) and
confirmed in humans by Penfield and Jasper (1954), who evoked somatosensory
sensations by stimulating the ceiling of the lateral sulcus
.

Unlike S1, which is a **contralateral, topographically precise, unimodal**
somatosensory area, S2 is a **bilateral, higher-order, multimodal
integration hub**:

*   **Bilateral receptive fields.** Individual S2 neurons receive input from
    **wide areas of the body surface on both sides**, and stimulation on one
    side of the body activates S2 in **both hemispheres**.
*   **Large receptive fields.** S2 receptive fields are **larger and less
    topographically precise** than S1 fields, and they often span multiple
    body regions (e.g., hand and face, or hand and foot).
*   **Higher-order functions.** S2 is engaged in **sensorimotor integration,
    integration of information from the two body halves, tactile attention,
    tactile learning and memory, and nociception**.

**The left S2 is not the right S2.** The lateralization of S2 is **subtle
and debated** — far less pronounced than the left-loaded S1 pair or the
parallel-laden PPC/BA39/BA40 pairs. The strongest evidence points to a
**left-hemisphere dominance in S2 activation** after **bilateral** median
nerve stimulation (left/right S2 ratio ≈ 1.8 in right-handers, ≈ 1.6 in
left-handers), independent of handedness. However,
other studies report **no functional asymmetry** in S2 responses to digit
stimulation. This module documents the **left-hemisphere weighting** as
the best-supported lateralized claim, while explicitly noting the
controversy.

Two-Partition Context
---------------------
This module is the **functional-region node** for the left S2. It is the
**complementary boundary case** to S1:

::

    Functional partition (this module)     Cytoarchitectonic partition
    ──────────────────────────────────     ────────────────────────────
    secondary_somatosensory_cortex  ──▶    **NO BRODMANN ANCHOR**
                                           (OP1–OP4 complex in the
                                           parietal operculum is the
                                           modern cytoarchitectonic
                                           correlate; BA40/BA43 are
                                           imprecise conventional labels)

**S1 is scattered membership; S2 is no membership.** S1 has four Brodmann
fields, one of which (BA3) lives at a non-standard path. S2 has **zero**
fields wired under ``.../parietal/brodmann_areas/``. A consumer that
iterates ``brodmann_areas.ITERABLE_AREAS`` will find **no S2 entry**,
because the Brodmann partition does not contain one.

**Resolution contract for consumers:**

*   If you need a **functional S2 node**, use this module.
*   If you need a **cytoarchitectonic S2 anchor**, use the **OP1–OP4
    complex** — but be aware that the current tree does not wire OP1–OP4
    as separate modules. The closest existing anchors are
    ``brodmann_area_40`` (supramarginal gyrus) and ``brodmann_area_43``
    (subcentral area), but neither is a faithful representation of S2.
    **Do not claim that BA40 or BA43 “is” S2.** They are adjacent
    territories that overlap partially with the S2 region.
*   If you need **both**, query this module for the functional region and
    the OP1–OP4 literature (Eickhoff et al., 2006) for the cytoarchitectonic
    detail — but recognize that the tree does not currently provide a
    one-to-one Brodmann mapping for S2.

Function in the Human Brain
---------------------------
The left S2 is a **left-weighted higher-order somatosensory integration
hub**. Its best-supported functions cluster into six domains:

*   **Sensorimotor Integration:** S2 integrates somatosensory input with
    motor signals to support **manual exploration and object
    discrimination**. It is part of the circuit that links tactile
    processing to action, and it is activated during **isometric muscle
    contraction** of various body parts.

*   **Interhemispheric Integration of the Two Body Halves:** S2 is the
    principal cortical substrate for **integrating tactile information
    across the two sides of the body**. The two S2 cortices are
    **densely interconnected**, and S2 neurons have **bilateral receptive
    fields**. In bilateral simultaneous stimulation, the **contralateral
    input arriving first in S2 inhibits the later ipsilateral input**
    , a mechanism for resolving competing bilateral signals.

*   **Tactile Attention:** S2 is **activated bilaterally during attentional
    tasks** and is considered to play a role in **tactile attention**.
    fMRI studies of somatosensory oddball tasks show that S2 — not S1 —
    is the region that responds to **rare/deviant tactile stimuli**,
    consistent with a role in **attentional capture and salience
    detection** in the tactile modality.

*   **Tactile Learning and Memory:** S2 is involved in **remembering
    differences between tactile shapes and textures**. Ablation
    studies in primates indicate that S2 is critical for **tactile learning
    and retention**, and S2 is considered to play a role in **tactile
    memory**.

*   **Nociception (Sensory-Discriminative Aspect):** S2 responds to
    **nociceptive afferents** and is part of the cortical network for
    **pain processing**. Lesions in S2 can affect **pain and temperature
    sense**. S2 receives nociceptive projections from the **VPI thalamic
    nucleus** with mostly large, bilateral receptive fields.

*   **Body Schema and Self-Perception:** S2 contributes to the **body
    schema** — the internal representation of one's own body. Lesions in S2
    may **disturb the self-perception of body scheme**. S2 is a strong
    candidate for encoding body schema, particularly given its role in
    processing proprioceptive input.

Associated Disorders
--------------------
Damage to or dysfunction of the left S2 is associated with:

*   **Tactile Agnosia and Astereognosis:** Lesions in S2 and the adjacent
    inferior parietal lobule cause **severe tactile deficits**, including
    **tactile agnosia** (inability to recognize objects by touch) and
    impairment of **texture and shape discrimination**.
*   **Impaired Pain and Temperature Sense:** Lesions in S2 affect **pain
    and temperature sensation**, consistent with its nociceptive role.
*   **Body Schema Disturbance:** Lesions may **disturb the self-perception
    of body scheme**, contributing to disorders of corporeal awareness.
*   **Superficial Hemisensory Dysfunction (Thalamocortical Disconnection):**
    Disconnection between the thalamus and S2 can cause **superficial
    hemisensory dysfunction**, particularly for pain and temperature.

**What is NOT here:** **Bilateral astereognosis** (left-S1 dominance),
**complex finger movement dominance** (left-S1), and **hemispatial neglect**
(right-PPC/BA39/BA40) are **not** S2 syndromes. They belong to other
modules and must not be imported here.

Lateralization Notes
--------------------
This is the **left** S2 module. The lateralization landscape is **weakly
left-weighted** — far less pronounced than the S1 pair (left-loaded) or
the PPC/BA39/BA40 pairs (parallel-laden):

*   **Left-Lateralized Function (best-supported claim):**
    - **Left-hemisphere dominance in S2 activation after bilateral median
      nerve stimulation.** In 14 healthy adults, S2 responses were
      **significantly stronger in the left than in the right hemisphere**
      (left/right ratio ≈ 1.8 in right-handers, ≈ 1.6 in left-handers),
      independent of handedness. This suggests a
      **handedness-independent functional specialization** of the left S2
      for **bilateral integration**.

*   **Controversy (documented, not resolved):**
    - Some studies report **no hemispheric difference** in S2 responses to
      digit stimulation, supporting **a lack of functional asymmetry** in
      human somatosensory cortex. The left-dominance
      finding may be specific to **bilateral simultaneous stimulation** or
      to **specific stimulus modalities** (e.g., median nerve, penile
      nerve) rather than a general property of S2.
    - **Consumers should treat the left-S2 dominance as a
      stimulus-dependent, best-supported claim, not as an absolute rule.**

*   **Symmetric Functions (bilateral properties of S2):**
    - Sensorimotor integration.
    - Interhemispheric integration of the two body halves.
    - Tactile attention.
    - Tactile learning and memory.
    - Nociception (sensory-discriminative).
    - Body schema contribution.

**A consumer that assumes “left S2 = strongly lateralized” will overstate
the evidence.** The left-S2 dominance is **real but subtle and
stimulus-dependent**. This module documents it as the best-supported
lateralized claim while explicitly flagging the controversy.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional region node with NO Brodmann anchor.** This module
    represents **S2 as a functional unit** (OP1–OP4 complex). It does
    **not** claim that S2 “is” BA40, BA43, or any other Brodmann field.
    Consumers must not assume a one-to-one mapping between S2 and any
    Brodmann leaf in this tree.
*   **Structural parity with right S2.** Left and right S2 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. The functions are largely symmetric; only the
    left-dominance claim and the stimulus-dependent caveat differ.
*   **Lateralization is weak and stimulus-dependent.** Unlike S1, PPC,
    BA39, and BA40, S2 is **not a strongly lateralized module**. The
    left-dominance claim is documented with its supporting evidence and
    its counter-evidence.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex import secondary_somatosensory_cortex

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.cortex.secondary_somatosensory_cortex"
    )

**Do not** attempt to resolve S2 through ``brodmann_areas`` — there is no
S2 entry in that partition. For cytoarchitectonic detail, use the OP1–OP4
literature (Eickhoff et al., 2006), not the Brodmann leaves.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        s2_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.cortex.secondary_somatosensory_cortex"
        )
        # resolve s2_path through the memory/recall layer

References
----------
*   Adrian, E.D. (1940). “Double representation of the feet in the sensory
    cortex of the cat.” *J Physiol*, 98, 16–18. (First description of S2.)
*   Penfield, W., & Jasper, H. (1954). *Epilepsy and Functional Anatomy of
    the Human Brain*. (Human S2 confirmed by stimulation of the lateral
    sulcus ceiling.)
*   **S2 functions and bilateral properties:** Lin, Y.Y., & Forss, N.
    (2002). “Functional characterization of human second somatosensory
    cortex by magnetoencephalography.” *Behav Brain Res*, 135(1–2), 141–145.
    (S2 responds to tactile and nociceptive input; modulated by muscle
    contraction; lesions disturb body schema; S2 receives direct ipsilateral
    peripheral input.)
*   **S2 higher-order functions:** *Human secondary somatosensory cortex is
    involved in the processing of somatosensory rare stimuli: an fMRI study*
    (2008), *NeuroImage*, 40(4), 1765–1771. (Bilateral S2 performs
    sensorimotor integration, integration of the two body halves, attention,
    learning and memory.)
*   **S2 as OP1–OP4 complex:** Eickhoff, S.B., Amunts, K., Mohlberg, H., &
    Zilles, K. (2006). “The human parietal operculum. II. Stereotaxic maps
    and correlation with functional imaging results.” *Cereb Cortex*,
    16(2), 268–279. (The parietal operculum consists of four cytoarchitectonic
    areas OP1–OP4; the functional SII region matches this complex; SII is
    **not** a single Brodmann field.)
*   **Bilateral receptive fields:** Iwamura, Y. (2000). “Bilateral receptive
    field neurons and callosal connections in the somatosensory cortex.”
    *Phil Trans R Soc Lond B*, 355(1397), 267–273. (S2 neurons have large,
    often bilateral receptive fields covering multiple body regions.)
*   **Left-hemisphere dominance:** Simões, C., et al. (2002).
    “Left-hemisphere-dominant SII activation after bilateral median nerve
    stimulation.” *NeuroImage*, 15(3), 686–690. (S2 responses significantly
    stronger in the left than the right hemisphere; left/right ratio ≈ 1.8
    in right-handers, ≈ 1.6 in left-handers; handedness-independent.)
*   **No functional asymmetry (counter-evidence):** *Spatiotemporal
    integration of tactile information in human somatosensory cortex*
    (2007), *BMC Neuroscience*. (Lack of hemispheric difference in responses
    to digit stimulation supports a lack of functional asymmetry in human
    somatosensory cortex.)
*   **Tactile agnosia and astereognosis from S2 lesions:**
    *Secondary Somatosensory Area (S2)* overview. (S2 lesions cause tactile
    agnosia, astereognosis, and impaired texture/shape discrimination.)
*   **Pain and temperature from S2 lesions:** *Parietal Lobe – Exam* (2021).
    (S2 lesions affect pain and temperature sense.)
*   **Thalamocortical disconnection:** *A case of superficial hemisensory
    dysfunction due to operculo-insular infarction* (2012), *ScienceDirect*.
    (Disconnection between thalamus and S2 contributes to superficial
    perception disturbance.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Secondary somatosensory cortex (left); FMA — left parietal
    operculum (S2 partonomy).
"""