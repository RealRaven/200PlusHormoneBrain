"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex.secondary_somatosensory_cortex
===============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── cortex
                        └── secondary_somatosensory_cortex   <-- THIS MODULE

**Primary synonym:** Secondary Somatosensory Cortex (S2), right; Right S2;
Somatosensory Area II; SII.
**Organizing principle:** **Functional–anatomical region** — the second
cortical stage of somatosensory processing.
**Brodmann constitution:** **No single Brodmann field.** S2 corresponds to
the **OP1–OP4 cytoarchitectonic complex** of the parietal operculum
(Eickhoff et al., 2006). BA40 and BA43 are sometimes cited loosely, but
neither is a precise anchor.
**Part of:** The **functional partition** of the right parietal lobe
(``.../parietal/cortex``), alongside S1 and PPC.
**Cytoarchitectonic siblings:** **None.** This is the **boundary case** of
the two-partition architecture: a functional region with **no unambiguous
Brodmann anchor** in the current tree. See "Two-Partition Context" below.

Overview
--------
The **right secondary somatosensory cortex (S2)** is the second cortical
stage of somatosensory processing. It lies in the **parietal operculum**,
on the upper bank of the lateral sulcus (Sylvian fissure), posterior to S1
and adjacent to the insula.

Like the left S2, the right S2 is a **bilateral, higher-order, multimodal
integration hub** — not a second somatotopic map. Its receptive fields are
**large and often bilateral**, spanning both hands and multiple body
regions, and it supports **sensorimotor integration, interhemispheric
integration, tactile attention, tactile learning and memory, nociception,
and body schema**.

**This is the right S2, and its lateralization is NOT a mirror of the
left S2's left-dominance claim.** The right S2 carries a **distinctive,
right-lateralized functional profile**:

*   **Right parietal operculum/S2 is commonly activated for both right-
    and left-hand tactile stimulation**, making it the **one area of
    overlap** in a meta-analysis of right- vs. left-hand touch studies —
    suggesting a **lateralized pattern of bilateral somatosensory
    integration** in the right S2 region[reference:0].

*   **Right S2 is functionally connected to the left posterior parietal
    cortex (PPC)** during tactile object recognition — an asymmetric
    connectivity pattern that is **not** mirrored by the left S2's
    connectivity profile[reference:1][reference:2].

*   **Right S2 lesions are associated with left hemianesthesia and body-
    awareness deficits** (anosognosia, somatoparaphrenia, personal neglect)
    when they extend into the right somatosensory parietal cortex
    [reference:3].

**Critical lateralization note:** The **left-hemisphere dominance** claim
documented for the left S2 (Simões et al., 2002; left/right ratio ≈ 1.8)
is **absent** from this right module. The right S2 is **not** the
subordinate twin; it is the **dominant substrate for bilateral integration
across both hands**, and its connectivity to left PPC is a
right-lateralized property. See `Lateralization Notes` for the full
asymmetry and the documented controversy.

**This is the canonical boundary case of the two-partition architecture.**
Like the left S2, the right S2 has **zero** Brodmann fields wired under
``.../parietal/brodmann_areas/``. The OP1–OP4 complex is the modern
cytoarchitectonic correlate; BA40 and BA43 are imprecise conventional
labels.

Two-Partition Context
---------------------
This module is the **functional-region node** for the right S2. It is the
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
    as separate modules. **Do not claim that BA40 or BA43 “is” S2.**
*   If you need **both**, query this module for the functional region and
    the OP1–OP4 literature (Eickhoff et al., 2006) for the cytoarchitectonic
    detail.

Function in the Human Brain
---------------------------
The right S2 is a **right-lateralized higher-order somatosensory
integration hub**. Its best-supported functions cluster into six domains:

*   **Bilateral Integration Across the Two Hands (Right-Lateralized —
    the principal right-S2 function):** The **right parietal operculum/S2
    region is commonly activated for both right- and left-hand tactile
    stimulation**, making it the **one area of overlap** between right-hand
    and left-hand touch studies in a meta-analysis of functional
    neuroimaging[reference:4]. This right-S2-specific bilateral activation
    pattern suggests a **lateralized role in integrating tactile
    information across both body sides**.

*   **Functional Connectivity to Left PPC During Tactile Object Recognition
    (Right-Lateralized):** During a delayed match-to-sample tactile object
    recognition task, the **right SII is functionally connected to the left
    posterior parietal cortex (PPC)**, whereas the left SII connects to
    left SI and right primary/premotor cortex[reference:5][reference:6].
    This asymmetric connectivity suggests that the right S2 is integrated
    into a **left-PPC-dependent sensorimotor transformation network** for
    tactile object recognition.

*   **Sensorimotor Integration:** S2 integrates somatosensory input with
    motor signals to support **manual exploration and object
    discrimination**. This function is **symmetric** across hemispheres
    and copied verbatim from the left S2 twin.

*   **Tactile Attention:** S2 is **activated bilaterally during attentional
    tasks** and plays a role in **tactile attention**, particularly in
    responding to **rare/deviant tactile stimuli**. This is a
    **symmetric** function.

*   **Tactile Learning and Memory:** S2 is involved in **remembering
    differences between tactile shapes and textures**. Unilateral S2
    removals in monkeys impair **tactile learning and retention** whether
    using the hand **contralateral or ipsilateral** to the removal
    [reference:7] — a finding that underscores S2's bilateral integration
    role. This is a **symmetric** function.

*   **Nociception and Body Schema:** S2 responds to **nociceptive
    afferents** and contributes to the **body schema**. Right S2 lesions
    extending into the right somatosensory parietal cortex are associated
    with **left hemianesthesia and body-awareness deficits** — anosognosia,
    somatoparaphrenia, and personal neglect[reference:8]. The nociceptive
    function is **symmetric**; the body-awareness deficit is a
    **right-lateralized** clinical association.

Associated Disorders
--------------------
Damage to or dysfunction of the right S2 is associated with:

*   **Left Hemianesthesia and Body-Awareness Deficits (Right-Lateralized):**
    Right brain lesions involving the somatosensory parietal cortex produce
    **left hemianesthesia** that is frequently associated with
    **anosognosia, somatoparaphrenia, and personal neglect**
    [reference:9]. This is a **right-lateralized** association — the left S2
    module does not carry this syndrome.

*   **Tactile Agnosia and Astereognosis:** Lesions in S2 and the adjacent
    inferior parietal lobule cause **tactile agnosia** and impairment of
    **texture and shape discrimination**[reference:10].

*   **Impaired Tactile Learning and Retention (Bilateral):** Unilateral S2
    removals impair tactile learning and retention **whether using the hand
    contralateral or ipsilateral to the removal**[reference:11]. This is a
    **symmetric** lesion effect, not a lateralized syndrome.

*   **Impaired Pain and Temperature Sense:** Lesions in S2 affect **pain
    and temperature sensation**, consistent with its nociceptive role.

**What is NOT here:** The **left-hemisphere dominance** in S2 activation
after bilateral median nerve stimulation (Simões et al., 2002) is a
**left-S2 claim**. It is **absent** from this right module. The
**bilateral astereognosis** phenotype and **complex finger movement
dominance** are **left-S1** functions, not right-S2 functions.

Lateralization Notes
--------------------
This is the **right** S2 module. The lateralization landscape is
**right-lateralized for bilateral integration and left-PPC connectivity**,
with a **documented controversy** about whether S2 activation is
hemispherically asymmetric at all:

*   **Right-Lateralized Functions (unique to this twin):**
    - **Right parietal operculum/S2 is commonly activated for both
      hands** — the one area of overlap between right- and left-hand touch
      studies, suggesting a right-lateralized pattern of bilateral
      integration[reference:12].
    - **Functional connectivity to left PPC during tactile object
      recognition** — right SII → left PPC, whereas left SII → left SI and
      right primary/premotor cortex[reference:13][reference:14].
    - **Left hemianesthesia with body-awareness deficits** — right
      somatosensory parietal lesions produce anosognosia,
      somatoparaphrenia, and personal neglect for the left side
      [reference:15].

*   **Left-Lateralized Function (contrast — absent here):**
    - **Left-hemisphere dominance in S2 activation after bilateral median
      nerve stimulation** (Simões et al., 2002; left/right ratio ≈ 1.8).
      This is a **left-S2 claim** and is **not** mirrored here.

*   **Controversy (documented, not resolved):**
    - Some studies report **no hemispheric difference** in S2 response
      amplitude, latency, or oddball responses to digit stimulation,
      independent of handedness. This supports a
      **lack of functional asymmetry** in human somatosensory cortex — a
      direct counterpoint to both the left-dominance and right-bilateral-
      integration claims. **Consumers should treat S2 lateralization as
      stimulus-dependent and context-dependent**, not as an absolute rule.

*   **Symmetric Functions (bilateral properties of S2, copied verbatim
    from the left twin):**
    - Sensorimotor integration.
    - Interhemispheric integration of the two body halves.
    - Tactile attention.
    - Tactile learning and memory (with bilateral impairment from unilateral
      lesions[reference:18]).
    - Nociception (sensory-discriminative).
    - Body schema contribution.

**A consumer that assumes “right S2 = symmetric” will miss the
right-lateralized bilateral-integration and left-PPC connectivity
functions.** A consumer that assumes “right S2 = left S2” will incorrectly
import the left-dominance claim, which is absent here. The S2 pair is
**weakly lateralized, with opposite-direction claims and a documented
controversy**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional region node with NO Brodmann anchor.** This module
    represents **S2 as a functional unit** (OP1–OP4 complex). It does
    **not** claim that S2 “is” BA40, BA43, or any other Brodmann field.
*   **Structural parity with left S2.** Left and right S2 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. The six functional domains are **identical**;
    only the lateralization prose differs (left-dominance vs. right-
    bilateral-integration/left-PPC connectivity) and the controversy is
    documented on both sides.
*   **Lateralization is weak and stimulus-dependent.** Unlike S1, PPC,
    BA39, and BA40, S2 is **not a strongly lateralized module**. The
    right-bilateral-integration and left-PPC-connectivity claims are
    documented with their supporting evidence, and the counter-evidence
    (no hemispheric difference) is documented alongside them.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex import secondary_somatosensory_cortex

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.cortex.secondary_somatosensory_cortex"
    )

**Do not** attempt to resolve S2 through ``brodmann_areas`` — there is no
S2 entry in that partition. For cytoarchitectonic detail, use the OP1–OP4
literature (Eickhoff et al., 2006).

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        s2_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.cortex.secondary_somatosensory_cortex"
        )
        # resolve s2_path through the memory/recall layer

References
----------
*   **Right S2 bilateral activation (right-hand vs. left-hand meta-
    analysis):** *Activation of Bilateral Secondary Somatosensory Cortex
    With Right Hand Touch Stimulation: A Meta-Analysis of Functional
    Neuroimaging Studies* (2019), DOAJ — the **right parietal operculum/S2
    region was commonly activated for right and left hand tactile
    stimulation**, suggesting a lateralized pattern of somatosensory
    activation in the right S2 region[reference:19].
*   **Right S2 → left PPC connectivity:** Yu, Y., Yang, J., Ejima, Y.,
    Fukuyama, H., & Wu, J. (2018). “Asymmetric Functional Connectivity of
    the Contra- and Ipsilateral Secondary Somatosensory Cortex during
    Tactile Object Recognition.” *Front Hum Neurosci*, 11, 662. The right
    SII is functionally connected to the **left posterior parietal cortex
    (PPC)** during tactile object recognition[reference:20][reference:21].
*   **Right S2 lesions and body-awareness deficits:** *At the more
    elementary level, lesions of the somatosensory parietal cortex may
    induce an impairment to report tactile stimuli delivered to the
    contralateral side of the body* (University of Turin repository) —
    **left hemianesthesia following right brain lesions is frequently
    associated with anosognosia, somatoparaphrenia, and personal
    neglect**[reference:22].
*   **S2 functions and bilateral properties:** Lin, Y.Y., & Forss, N.
    (2002). *Behav Brain Res*, 135(1–2), 141–145. (S2 responds to tactile
    and nociceptive input; lesions disturb body schema.)
*   **S2 higher-order functions:** *Human secondary somatosensory cortex is
    involved in the processing of somatosensory rare stimuli: an fMRI study*
    (2008), *NeuroImage*, 40(4), 1765–1771. (Bilateral S2 performs
    sensorimotor integration, integration of the two body halves, attention,
    learning and memory.)
*   **S2 as OP1–OP4 complex:** Eickhoff, S.B., Amunts, K., Mohlberg, H., &
    Zilles, K. (2006). *Cereb Cortex*, 16(2), 268–279. (The parietal
    operculum consists of OP1–OP4; SII is **not** a single Brodmann field.)
*   **Bilateral receptive fields:** Iwamura, Y. (2000). *Phil Trans R Soc
    Lond B*, 355(1397), 267–273. (S2 neurons have large, often bilateral
    receptive fields covering multiple body regions.)
*   **No hemispheric difference (counter-evidence):** *Spatiotemporal
    integration of tactile information in human somatosensory cortex*
    (2007), *BMC Neuroscience* — **no hemispheric differences** in response
    amplitude, latency, or oddball responses to digit stimulation,
    independent of handedness; supports a lack of functional
    asymmetry in human somatosensory cortex.
*   **Unilateral S2 removal impairs both hands:** Garcha, H.S., et al.
    (1978). *Cortex*, 14(3), 319–326. “The effects of unilateral or
    bilateral removals of the second somatosensory cortex (area SII)” —
    unilateral removals impaired tactile learning and retention **whether
    using the hand contralateral or ipsilateral to the removal**
    [reference:24].
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Secondary somatosensory cortex (right); FMA — right
    parietal operculum (S2 partonomy).
"""