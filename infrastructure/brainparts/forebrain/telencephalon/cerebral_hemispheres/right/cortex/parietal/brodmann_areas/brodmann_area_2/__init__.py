"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas.brodmann_area_2
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
                        └── brodmann_area_2   <-- THIS MODULE

**Primary synonym:** Brodmann Area 2 (BA2); part of Primary Somatosensory
Cortex (S1).
**Cytoarchitectonic designation:** Area 2 of Brodmann (1909).
**Part of:** Primary somatosensory cortex (S1), alongside BA3a, BA3b, and BA1.
**Location:** Caudal bank of the postcentral gyrus, immediately posterior to
BA1, on the lateral surface of the right parietal lobe.

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

This module is structurally identical to the left-hemisphere twin at
``.../left/cortex/parietal/brodmann_areas/brodmann_area_2``. The
**cytoarchitectonic identity and intrinsic computational role of BA2 are the
same in both hemispheres**; only the contralateral target of its sensory input
and the lateralized functional weightings (below) differ.

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
    preserved elementary sensation (contralateral to the lesion on the right
    side; see the lateralization note below).
*   **Tactile agnosia** — inability to recognize the *identity* of an object
    by touch, even when its features (size, texture, shape) can be described.
*   **Impaired size and shape discrimination** in psychophysical tasks.
*   **Proprioceptive deficits** of the contralateral hand, sometimes
    contributing to **ideomotor apraxia** for the affected limb when the
    lesion extends into the intraparietal region.

**Note on lateralization:** The **bilateral-astereognosis** syndrome described
for the left BA1–BA2 complex is a left-lateralized phenomenon. A small right
BA2 lesion produces a **contralateral (left-hand) astereognosis** only; it
does **not** produce bilateral loss. Do not carry the left-hemisphere
bilateral-loss claim into this module.

Lateralization Notes
--------------------
This is the **right** hemisphere BA2 module.

*   **Contralateral Representation:** Right BA2 processes tactile and
    proprioceptive information from the **left side of the body** (face
    excepted, which is bilaterally represented).

*   **Right-Hemisphere Weighting for Spatial and Postural Aspects of Touch:**
    Right BA2 participates more strongly than left BA2 in **tactile spatial
    attention to the left hemibody**, in **postural / limb-position
    representation**, and in **whole-body tactile integration**. This is
    consistent with the broader right-hemisphere dominance for spatial
    attention and body schema, and it is one reason right somatosensory and
    parietal lesions are associated with more severe **personal neglect** and
    **anosognosia** for the left side of the body.

*   **No Stereognosis Dominance.** The left-hemisphere dominance for
    stereognosis described in the left BA2 twin does **not** apply
    symmetrically to the right side. Right BA2 contributes to tactile object
    recognition — for example, the **left hand's** contribution to bimanual
    object exploration — but without the demonstrated left-lateralized,
    bilateral-loss phenotype.

*   **No Praxis Dominance.** The left-hemisphere praxis weighting described in
    the left BA2 twin does **not** apply symmetrically to the right side.
    Right BA2 contributes to skilled manipulation with the **left** hand, but
    the dominant praxis substrate remains left-hemispheric (BA39/BA40 and
    premotor hand area) in most right-handers.

Design Contract
---------------
*   **No side effects on import.** This `__init__.py` is a pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No hormone imports here.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **S1 subfield siblings.** BA2 is functionally grouped with BA3a, BA3b,
    and BA1 as the four subfields of S1. BA3 lives under
    ``gyri.postcentral_gyrus/brodmann_area_3`` on the right side; BA1 and BA2
    live here. See the parent ``brodmann_areas`` package for the full
    iteration contract (``ITERABLE_AREAS``).
*   **Boundary with BA5.** BA2 abuts BA5 at the caudal edge of the postcentral
    gyrus. BA2 is still *primary* somatosensory (thalamic input via VPL/VPM,
    obligate response to passive touch), while BA5 is *association* cortex (no
    direct VPL/VPM input; requires active exploration or attention). This
    boundary criterion is hemisphere-symmetric and applies verbatim here.
*   **Structural parity with left.** Left and right BA2 modules must be
    structurally interchangeable so bilateral consumers can iterate
    hemispheres generically. Only the path segment (`right` vs `left`) and the
    lateralization prose differ.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.brodmann_areas import brodmann_area_2

Or by fully-qualified path string (used by the hormone/memory gating layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.brodmann_areas.brodmann_area_2"
    )

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ba2_path = (
            f"telencephalon.cerebral_hemispheres.{side}.cortex."
            f"parietal.brodmann_areas.brodmann_area_2"
        )
        # resolve ba2_path through the memory/recall layer

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*, 4th ed.
*   NeuroNames — Brodmann area 2 (right).
*   FMA — Brodmann area 2 (right member).
*   Bodegàrd, A., et al. (2001). *Neuron*, 31(2), 317–328. (Hierarchical
    processing in S1: BA1 vs BA2 vs BA3b).
*   Reed, C.L., et al. (2004). *NeuroImage*, 22(1), 313–320. (BA2 in tactile
    shape and size processing).
*   Kitada, R., et al. (2005). *NeuroImage*, 28(1), 266–275. (BA2 in tactile
    object recognition).
*   Iwamura, Y. (1998). *Curr Opin Neurobiol*, 8(4), 522–528. (Bilateral and
    midline receptive fields in primate BA2).
*   Committeri, G., et al. (2007). *Neuropsychologia*, 45(4), 745–755.
    (Right somatosensory/parietal contribution to personal neglect).
*   Moll, J., et al. (2017). *Cogn Behav Neurol*, 30(3), 102–115. (Left
    BA1–BA2 complex and bilateral astereognosis — cited here only to mark
    that the right side does **not** share the bilateral-loss phenotype).
"""