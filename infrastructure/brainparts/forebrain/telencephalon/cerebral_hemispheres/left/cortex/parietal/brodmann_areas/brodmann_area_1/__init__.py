"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.brodmann_areas.brodmann_area_1
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── brodmann_areas
                        └── brodmann_area_1   <-- THIS MODULE

**Primary synonym:** Brodmann Area 1 (BA1); Primary Somatosensory Cortex,
crown of postcentral gyrus.
**Cytoarchitectonic designation:** Area 1 of Brodmann (1909).
**Part of:** Primary somatosensory cortex (S1), alongside BA3a, BA3b, and BA2.
**Location:** Crown (apex) of the postcentral gyrus, on the lateral surface
of the left parietal lobe.

Overview
--------
Brodmann Area 1 (BA1) is a key cytoarchitectonic field within the **primary
somatosensory cortex (S1)**. It occupies the crown of the postcentral gyrus,
situated just posterior to the central sulcus. While BA3b is the initial
recipient of thalamocortical somatosensory input, BA1 is a crucial downstream
processor that refines and elaborates this information.

Function in the Human Brain
---------------------------
The function of BA1 is multifaceted, encompassing low-level sensory processing
and higher-order integrative roles. Key functions include:

*   **Discriminative Touch and Texture Perception:** BA1 is critically
    involved in processing fine tactile details. It is particularly important
    for **discriminating the texture of objects** (e.g., smooth vs. rough) and
    for processing **spatial stimulus patterns** on the skin[reference:0][reference:1].

*   **Pain Processing (Nociception):** Contrary to the classical view that
    pain is processed elsewhere, BA1 is now recognized as a key node in the
    **sensory-discriminative** dimension of pain. It is preferentially
    involved in processing nociceptive information, helping to encode the
    location, intensity, and quality of a painful stimulus[reference:2][reference:3].

*   **Somatotopic Representation:** BA1 contains a complete, orderly **map of
    the contralateral body surface** (the sensory homunculus). This
    representation is highly organized; for instance, the fingers are
    represented in a precise medial-to-lateral sequence along the crown of the
    gyrus[reference:4][reference:5].

*   **Body Ownership and Self-Awareness:** Activity in BA1 has been linked to
    the feeling that our bodies belong to us. Studies show that illusory
    feelings of body ownership (e.g., the "numbness illusion") are associated
    with specific activity patterns in BA1.

*   **Stereognosis (Tactile Object Recognition):** The left BA1, in
    particular, appears to play a dominant role in **stereognosis**—the
    ability to recognize objects by feeling their form and texture. A small
    lesion in the left BA1 can cause **bilateral astereognosis**, where a
    person cannot recognize objects by touch with either hand, despite intact
    basic sensation[reference:8].

*   **Sensorimotor Integration:** BA1 is not a purely sensory area; it
    receives **top-down modulation** from motor and prefrontal areas and
    integrates sensory feedback with motor control, contributing to the
    refinement of tactile discrimination through training and experience
    [reference:9].

Associated Disorders
--------------------
Damage to or dysfunction of BA1 is associated with:

*   **Astereognosis** (inability to recognize objects by touch)[reference:10].
*   **Impaired tactile discrimination** and **loss of texture perception**
    [reference:11].
*   **Hemihypesthesia** (reduced sensitivity to sensory stimuli on one side of
    the body)[reference:12].
*   Findings reported in **chronic pain syndromes**[reference:13].

Lateralization Notes
--------------------
This is the **left** hemisphere BA1 module.

*   **Contralateral Representation:** The left BA1 receives and processes
    somatosensory information from the **right side of the body** (with the
    exception of the face, which has bilateral representation)[reference:14].
*   **Left-Hemisphere Dominance for Stereognosis:** As noted above, the left
    BA1 (and the broader left postcentral gyrus) is dominant for the complex
    tactile recognition of objects (stereognosis) in many individuals
    [reference:15].

Design Contract
---------------
*   **No side effects on import.** This `__init__.py` is a pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No hormone imports here.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **BA3 cross-listing.** This module is a sibling to the cross-listed
    ``brodmann_area_3`` (which lives under ``gyri.postcentral_gyrus``). See the
    parent ``brodmann_areas`` package for the full iteration contract
    (``ITERABLE_AREAS``).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.brodmann_areas import brodmann_area_1

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.brodmann_areas.brodmann_area_1"
    )

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
*   NeuroNames — Brodmann area 1 (left).
*   FMA — Brodmann area 1 (left member).
*   Roux, F.-E., et al. (2018). *J Physiol*, 596(5), 941–956. (Somatotopy in BA1)[reference:16].
*   Chen, L.M., et al. (2008). *Acta Physiologica Sinica*, 60(5), 664–668. (Nociception in BA1)[reference:17].
*   Martuzzi, R., et al. (2015). *Soc Cogn Affect Neurosci*, 10(11), 1449–1459. (Body ownership and BA1).
*   Moll, J., et al. (2017). *Cogn Behav Neurol*, 30(3), 102–115. (Left BA1 and stereognosis)[reference:19].
"""