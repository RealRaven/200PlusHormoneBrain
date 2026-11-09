"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.brodmann_areas.brodmann_area_2
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
                        └── brodmann_area_2   <-- THIS MODULE

**Primary synonym:** Brodmann Area 2 (BA2); part of Primary Somatosensory
Cortex (S1).
**Cytoarchitectonic designation:** Area 2 of Brodmann (1909).
**Part of:** Primary somatosensory cortex (S1), alongside BA3a, BA3b, and BA1.
**Location:** Caudal bank of the postcentral gyrus, immediately posterior to
BA1, on the lateral surface of the left parietal lobe.

Overview
--------
Brodmann Area 2 (BA2) is the most **caudal** of the four S1 subfields. It sits
behind BA1 on the posterior bank of the postcentral gyrus, abutting the
anterior border of the superior parietal lobule / BA5. Unlike BA3b (the
thalamic gateway) and BA1 (the texture/proprioception node), BA2 is the first
S1 field dominated by **cortico-cortical** rather than thalamocortical input:
it receives dense projections from BA3b and BA1, and it begins the transition
from raw somatosensation toward **tactile object representation**.

Cytoarchitectonically, BA2 is thicker than BA3 and BA1, with larger pyramidal
cells in layer III and a more prominent layer IV. Its **receptive fields are
larger** than those of BA3b and BA1, and a higher fraction of its neurons are
**bilaterally responsive** or show **complex, multi-digit** receptive fields.

Function in the Human Brain
---------------------------
BA2 is best understood as the S1 subfield that converts **feature
registration** (BA1) into **object-level representation**. Key functions:

*   **Size, Shape, and Curvature Perception:** BA2 is selectively engaged by
    **tactile shape and size** judgments. Human fMRI and primate
    electrophysiology converge on BA2 as the S1 field most strongly modulated
    by the *geometry* of a touched object, as distinct from its *surface
    texture* (BA1) or *vibrotactile frequency* (BA3b).

*   **Stereognosis (Tactile Object Recognition):** BA2, together with BA1 and
    the downstream anterior intraparietal area (AIP), is a core node of the
    network that lets us **identify objects by feel**. Tactile
    object-recognition tasks recruit BA2 more strongly than passive touch
    tasks do.

*   **Proprioception of the Hand and Fingers:** BA2 carries a substantial
    proprioceptive signal — particularly from muscle spindles and joint
    receptors of the fingers and wrist — and is a major contributor to
    **hand posture representation**. It is more proprioception-weighted than
    BA1.

*   **Bimanual and Midline Integration:** BA2 contains a higher proportion of
    neurons with **bilateral receptive fields** and with receptive fields
    straddling the body midline than BA3b or BA1. This makes BA2 a candidate
    substrate for **bimanual coordination** and for representing the body as a
    single coherent object rather than two hemibodies.

*   **Sensorimotor Coupling:** BA2 is reciprocally connected with the primary
    motor cortex (BA4) and premotor cortex (BA6), and it shows
    **movement-related modulation** of tactile responses. It is best described
    as *sensorimotor* rather than purely sensory.

*   **Tactile Working Memory and Decision:** BA2 is active during **delayed
    tactile discrimination** tasks (e.g., decide whether a test stimulus is
    wider than a remembered sample). This is a step beyond S1's classical
    "sensation-only" role and places BA2 at the boundary between perception
    and cognition.

Associated Disorders
--------------------
Damage to or dysfunction of BA2 is associated with:

*   **Astereognosis** — impaired recognition of objects by touch despite
    preserved elementary sensation.
*   **Tactile agnosia** — inability to recognize the *identity* of an object
    by touch, even when its features (size, texture, shape) can be described.
*   **Impaired size and shape discrimination** in psychophysical tasks.
*   **Proprioceptive deficits** of the contralateral hand, sometimes
    contributing to **ideomotor apraxia** for the affected limb when the
    lesion extends into the intraparietal region.

**Note on lateralization:** The left BA1–BA2 complex is the dominant
hemisphere for **stereognosis** in most right-handed individuals; a small
left postcentral lesion (involving BA1 and/or BA2) can produce a syndrome of
**bilateral** astereognosis, with the *contralateral* (right-hand) deficit
being the more severe of the two. See the left BA1 docstring for the
reference. The right BA2 module does **not** carry this bilateral-loss
syndrome.

Lateralization Notes
--------------------
This is the **left** hemisphere BA2 module.

*   **Contralateral Representation:** Left BA2 processes tactile and
    proprioceptive information from the **right side of the body** (face
    excepted, which is bilaterally represented).

*   **Left-Hemisphere Weighting for Stereognosis:** As noted above, the left
    BA1–BA2 complex is the dominant substrate for tactile object recognition
    in most right-handers. Right BA2 contributes, but without the demonstrated
    bilateral-loss phenotype.

*   **Left-Hemisphere Weighting for Praxis:** Because of its tight coupling
    with left-hemisphere parietal praxis areas (BA39/BA40) and with the
    premotor hand area, left BA2 is more strongly engaged than right BA2
    during **skilled tool manipulation** and **imitation of hand postures**.

Design Contract
---------------
*   **No side effects on import.** This `__init__.py` is a pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No hormone imports here.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **S1 subfield siblings.** BA2 is functionally grouped with BA3a, BA3b,
    and BA1 as the four subfields of S1. BA3 lives under
    ``gyri.postcentral_gyrus/brodmann_area_3``; BA1 and BA2 live here. See the
    parent ``brodmann_areas`` package for the full iteration contract
    (``ITERABLE_AREAS``).
*   **Boundary with BA5.** BA2 abuts BA5 at the caudal edge of the postcentral
    gyrus. Do not conflate them: BA2 is still *primary* somatosensory (thalamic
    input via VPL/VPM, obligate response to passive touch), while BA5 is
    *association* cortex (no direct thalamic input from VPL/VPM; requires
    active exploration or attention).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.brodmann_areas import brodmann_area_2

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.brodmann_areas.brodmann_area_2"
    )

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
*   NeuroNames — Brodmann area 2 (left).
*   FMA — Brodmann area 2 (left member).
*   Bodegàrd, A., et al. (2001). *Neuron*, 31(2), 317–328. (Hierarchical
    processing in S1: BA1 vs BA2 vs BA3b).
*   Reed, C.L., et al. (2004). *NeuroImage*, 22(1), 313–320. (BA2 in tactile
    shape and size processing).
*   Kitada, R., et al. (2005). *NeuroImage*, 28(1), 266–275. (BA2 in tactile
    object recognition).
*   Iwamura, Y. (1998). *Curr Opin Neurobiol*, 8(4), 522–528. (Bilateral and
    midline receptive fields in primate BA2).
*   Moll, J., et al. (2017). *Cogn Behav Neurol*, 30(3), 102–115. (Left
    BA1–BA2 complex and bilateral astereognosis).
"""