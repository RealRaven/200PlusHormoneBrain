"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas.brodmann_area_1
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
                        └── brodmann_area_1   <-- THIS MODULE

**Primary synonym:** Brodmann Area 1 (BA1); Primary Somatosensory Cortex,
crown of postcentral gyrus.
**Cytoarchitectonic designation:** Area 1 of Brodmann (1909).
**Part of:** Primary somatosensory cortex (S1), alongside BA3a, BA3b, and BA2.
**Location:** Crown (apex) of the postcentral gyrus, on the lateral surface
of the right parietal lobe.

Overview
--------
Brodmann Area 1 (BA1) is a key cytoarchitectonic field within the **primary
somatosensory cortex (S1)**. It occupies the crown of the postcentral gyrus,
situated just posterior to the central sulcus. While BA3b is the initial
recipient of thalamocortical somatosensory input, BA1 is a crucial downstream
processor that refines and elaborates this information.

This module is structurally identical to the left-hemisphere twin at
``.../left/cortex/parietal/brodmann_areas/brodmann_area_1``. The
**cytoarchitectonic identity and intrinsic processing role of BA1 are the same
in both hemispheres**; what differs is the *contralateral target* of its
somatosensory input, and the lateralized functional weightings noted below.

Function in the Human Brain
---------------------------
The function of BA1 is multifaceted, encompassing low-level sensory processing
and higher-order integrative roles. Key functions include:

*   **Discriminative Touch and Texture Perception:** BA1 is critically
    involved in processing fine tactile details. It is particularly important
    for **discriminating the texture of objects** (e.g., smooth vs. rough) and
    for processing **spatial stimulus patterns** on the skin.

*   **Pain Processing (Nociception):** Contrary to the classical view that
    pain is processed elsewhere, BA1 is now recognized as a key node in the
    **sensory-discriminative** dimension of pain. It is preferentially
    involved in processing nociceptive information, helping to encode the
    location, intensity, and quality of a painful stimulus.

*   **Somatotopic Representation:** BA1 contains a complete, orderly **map of
    the contralateral body surface** (the sensory homunculus). This
    representation is highly organized; for instance, the fingers are
    represented in a precise medial-to-lateral sequence along the crown of the
    gyrus.

*   **Body Ownership and Self-Awareness:** Activity in BA1 has been linked to
    the feeling that our bodies belong to us. Studies show that illusory
    feelings of body ownership (e.g., the "numbness illusion") are associated
    with specific activity patterns in BA1.

*   **Sensorimotor Integration:** BA1 is not a purely sensory area; it
    receives **top-down modulation** from motor and prefrontal areas and
    integrates sensory feedback with motor control, contributing to the
    refinement of tactile discrimination through training and experience.

Associated Disorders
--------------------
Damage to or dysfunction of BA1 is associated with:

*   **Impaired tactile discrimination** and **loss of texture perception**.
*   **Hemihypesthesia** (reduced sensitivity to sensory stimuli on one side of
    the body).
*   Findings reported in **chronic pain syndromes**.

**Note on stereognosis:** The *bilateral* astereognosis syndrome described for
the **left** BA1 is a left-lateralized phenomenon. A comparably small right
BA1 lesion does **not** produce bilateral astereognosis; it produces
contralateral (left-hand) deficits only. Do not carry the bilateral-astereognosis
note into the right module — that would be an over-generalization.

Lateralization Notes
--------------------
This is the **right** hemisphere BA1 module.

*   **Contralateral Representation:** The right BA1 receives and processes
    somatosensory information from the **left side of the body** (with the
    exception of the face, which has bilateral representation).

*   **Right-Hemisphere Functional Weighting (consumer layer, not encoded here):**
    Right-hemisphere somatosensory cortex participates more strongly than the
    left in **spatial attention to the left hemibody** and in **whole-body
    spatial and postural representation**. This is one reason right
    somatosensory/parietal lesions are associated with more severe
    **personal neglect** and **anosognosia for the left side of the body**.

*   **No stereognosis dominance.** The left-hemisphere dominance for
    stereognosis noted in the left twin does **not** apply symmetrically to
    the right side. The right BA1 contributes to tactile object recognition,
    but without the demonstrated left-lateralized, bilateral-loss phenotype.

Design Contract
---------------
*   **No side effects on import.** This `__init__.py` is a pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No hormone imports here.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **BA3 cross-listing.** This module is a sibling to the cross-listed
    ``brodmann_area_3`` (which lives under ``gyri.postcentral_gyrus`` on the
    right side). See the parent ``brodmann_areas`` package for the full
    iteration contract (``ITERABLE_AREAS``).
*   **Structural parity with left.** The left and right BA1 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. Only the path segment (`right` vs `left`) and
    the lateralization prose differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas import brodmann_area_1

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.brodmann_areas.brodmann_area_1"
    )

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba1_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.brodmann_areas.brodmann_area_1"
        )
        # resolve ba1_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
*   NeuroNames — Brodmann area 1 (right).
*   FMA — Brodmann area 1 (right member).
*   Roux, F.-E., et al. (2018). *J Physiol*, 596(5), 941–956. (Somatotopy in BA1).
*   Chen, L.M., et al. (2008). *Acta Physiologica Sinica*, 60(5), 664–668. (Nociception in BA1).
*   Martuzzi, R., et al. (2015). *Soc Cogn Affect Neurosci*, 10(11), 1449–1459. (Body ownership and BA1).
*   Committeri, G., et al. (2007). *Neuropsychologia*, 45(4), 745–755. (Right somatosensory/parietal contribution to personal neglect).
*   Moll, J., et al. (2017). *Cogn Behav Neurol*, 30(3), 102–115. (Left-lateralized stereognosis — cited here only to mark that the right side does not share the bilateral-loss phenotype).
"""