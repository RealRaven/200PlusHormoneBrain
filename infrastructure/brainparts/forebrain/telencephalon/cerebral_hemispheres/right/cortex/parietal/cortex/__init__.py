"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex
=================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── cortex            <-- THIS MODULE

**Primary synonym:** Parietal cortex (right); Parietal neocortex.
**Organizing principle:** **Functional–anatomical partition**, NOT
cytoarchitectonic.
**Laterality:** right hemisphere.
**Sibling aggregator:** ``.../parietal/brodmann_areas`` — a *different*
partition of the *same* anatomical territory. See "The Two Partitions"
below.

Overview
--------
This module groups the **functional regions** of the right parietal lobe:
the two somatosensory cortical areas (primary and secondary) and the
posterior parietal association cortex. It is the **functional twin** of the
cytoarchitectonic partition at ``.../parietal/brodmann_areas`` and the
structural mirror of the left ``cortex`` aggregator at
``.../left/cortex/parietal/cortex``.

**The two partitions are complementary, not redundant, and they do not
nest cleanly.** A region may be constituted by several Brodmann areas; a
Brodmann area may contribute to several functional networks; and one
region (S2) has no unambiguous single Brodmann label. Consumers must know
which partition they are querying:

*   **``brodmann_areas``** answers *"which cytoarchitectonic field is
    this?"* — Brodmann (1909) nomenclature, used by neuroimaging atlases
    and by the FMA.
*   **``cortex``** (this module) answers *"which functional region is
    this?"* — the classical S1 / S2 / PPC grouping, used by systems
    neuroscience and by clinical topology.

Both are valid, but they are **not interchangeable**. A consumer that
asks "does the right parietal lobe contain PPC?" and only queries
``brodmann_areas`` will get a *partial* answer (BA5 and BA7, but not the
functional region they jointly constitute); a consumer that asks "which
functional region supports spatial attention?" and only queries
``cortex`` will miss that the answer is specifically **right PPC**
(BA5 + BA7), not the entire cortical territory[reference:0].

Child Modules
-------------
Three functional regions are wired under this package:

*   ``primary_somatosensory_cortex`` (**S1**) — the thalamic gateway for
    discriminative touch, proprioception, and nociception. Constituted
    functionally by **BA3a/3b + BA1 + BA2**. On the right side, S1
    represents the **left** hemibody. Right S1 shows **stronger cortical
    facilitation during left-hand stimulation** than during right-hand
    stimulation, a right-lateralized weighting of contralateral
    somatosensory processing[reference:1].

*   ``secondary_somatosensory_cortex`` (**S2**) — the second
    somatosensory field, located on the upper bank of the lateral sulcus /
    parietal operculum. S2 receives input from S1 and from the thalamus
    (VPI), has **larger and more bilateral receptive fields** than S1, and
    supports **tactile attention, sensorimotor integration, and tactile
    object recognition**. On the right side, S2 is **commonly activated
    for both right- and left-hand tactile stimulation**, suggesting a
    lateralized pattern of bilateral somatosensory integration in the
    right S2 region[reference:2]. Right S2 is functionally connected to the
    **left posterior parietal cortex**, an asymmetric connectivity pattern
    implicated in tactile object recognition[reference:3].

*   ``posterior_parietal_cortex`` (**PPC**) — the polymodal association
    territory, comprising **BA5 + BA7**. Supports **reaching, grasping,
    spatial attention, and visuomotor integration**. On the **right** side,
    PPC carries the **dominant spatial-attention function**: it is critical
    for **sustaining attention to spatial locations over time** and is the
    principal cortical substrate for the spatial component of
    **hemispatial neglect**[reference:4][reference:5].

**Areas *not* covered by this functional partition:**

*   **BA39 (angular gyrus)** and **BA40 (supramarginal gyrus)** have no
    functional-region parent in this module. They are wired only under
    ``brodmann_areas``. This is a **deliberate omission**: the classical
    S1/S2/PPC functional partition was defined before the inferior parietal
    lobule was recognized as a distinct heteromodal association system.
    On the right side, BA39 and BA40 are **critical nodes of the
    right-lateralized spatial-awareness / neglect network** (documented in
    their respective leaf modules), but they are **not** part of the
    S1/S2/PPC functional partition.
*   **BA26 (ectosplenial area)** is a boundary case shared with the
    cingulate; it has no functional-region parent here either.

The Two Partitions
------------------
The **S1-vs-Brodmann** relationship is the canonical example of why both
partitions exist and why neither subsumes the other:

::

    Functional partition (this package)     Cytoarchitectonic partition
    ─────────────────────────────────────   ────────────────────────────
    primary_somatosensory_cortex   ──┐
                                     ├──▶  brodmann_area_1
                                     ├──▶  brodmann_area_2
                                     └──▶  brodmann_area_3   (cross-listed;
                                                              lives under
                                                              gyri/postcentral_gyrus/)

    secondary_somatosensory_cortex ──▶    (no single Brodmann field;
                                           BA43 is conventional but is not
                                           wired in this tree)

    posterior_parietal_cortex      ──┐
                                     ├──▶  brodmann_area_5
                                     └──▶  brodmann_area_7

The mapping is **hemisphere-symmetric** (identical to the left ``cortex``
aggregator):

*   **S1 → {BA1, BA2, BA3}** — a clean three-to-one mapping, with the
    caveat that BA3 is cross-listed under the postcentral gyrus.
*   **S2 → ∅** — S2 does **not** map cleanly to any single Brodmann
    field. The conventional label is **BA43** (subcentral area), but the
    tree does not currently wire BA43 anywhere. S2 is therefore a
    **functional region with no cytoarchitectonic anchor** in this
    project, and that is a documented fact, not an oversight.
*   **PPC → {BA5, BA7}** — a clean two-to-one mapping. BA5 is unimodal
    somatosensory association cortex; BA7 is fully polymodal
    (somatosensory + visual + oculomotor)[reference:6][reference:7].
*   **{BA39, BA40, BA26} → ∅ (from this module's perspective)** — three
    Brodmann areas with no functional-region parent here. On the right
    side, BA39 and BA40 carry the **spatial-awareness / neglect syndromes**
    that are *not* captured by the S1/S2/PPC partition.

**Consumers must not assume the two partitions nest.** They are two
independent slices through the same anatomical territory, and the
right way to query them is to choose the slice that answers the question
being asked.

Function in the Human Brain
---------------------------
The three functional regions collectively cover the **somatosensory and
visuomotor** functions of the right parietal lobe, with a **right-lateralized
emphasis on spatial attention and body schema**:

*   **Primary Somatosensory Cortex (S1):** Discriminative touch, texture
    (BA1), shape/size (BA2), proprioception, nociception, somatotopic
    representation of the **left** hemibody. Thalamic gateway (VPL/VPM).
    Right S1 shows **stronger facilitation during left-hand stimulation**,
    consistent with a right-hemisphere weighting for contralateral
    somatosensory processing[reference:8].

*   **Secondary Somatosensory Cortex (S2):** Tactile attention, bilateral
    sensory integration, tactile object recognition, sensorimotor coupling.
    The **right S2 is commonly activated for both right- and left-hand
    tactile stimulation**, suggesting a lateralized pattern of bilateral
    integration in the right S2 region[reference:9]. Right S2 is
    functionally connected to the **left PPC**, an asymmetric connectivity
    pattern implicated in tactile object recognition[reference:10].

*   **Posterior Parietal Cortex (PPC):** **Sustaining attention to spatial
    locations over time** is a critical function of the human right PPC[reference:11]. Right PPC is the **dominant cortical substrate for the
    spatial component of hemispatial neglect** — lesions to right, but not
    left, posterior parietal cortex produce a unilateral tactile neglect
    syndrome[reference:12]. Right PPC also carries the **dominant role in body
    schema and the internal representation of one's own body**: lesions of
    the right parietal lobe are largely responsible for severe
    perturbations of the internal representation of one's own body[reference:13]. Right PPC contributes to visuomotor integration for reaching and
    grasping, spatial working memory, and spatial cognition.

**Functions *not* covered by this functional partition** (they belong to
the ``brodmann_areas`` partition only):

*   **Gerstmann syndrome**, **alexia**, **semantic aphasia**, and the
    **semantic hub** role (left BA39 — **absent** on the right).
*   **Phonological loop**, **conduction aphasia**, **praxis storage**
    (left BA40 — **absent** on the right).
*   **Hemispatial neglect** and **spatial-awareness dominance** belong to
    the **right** BA39/BA40 *in addition to* right PPC. Consumers needing
    the full neglect network must query ``brodmann_areas`` for BA39/BA40
    as well as this module for PPC.

Lateralization Notes
--------------------
This is the **right** functional-parietal module. The lateralization
landscape is **strongly right-weighted** — the opposite of the left
``cortex`` aggregator, which carries the left-lateralized praxis and
stereognosis functions:

*   **Right-Lateralized Functions in this Partition:**
    - **Sustaining spatial attention over time** via PPC — a critical,
      right-dominant function[reference:14].
    - **Hemispatial neglect** via PPC (and BA39/BA40) — lesions to right,
      but not left, PPC produce tactile neglect[reference:15].
    - **Body schema and internal body representation** via PPC — right
      parietal lesions are largely responsible for severe perturbations of
      the body schema[reference:16].
    - **Right S2 bilateral integration** — right S2 is commonly activated
      for both hands, a lateralized pattern[reference:17].
*   **Left-Lateralized Functions (contrast — absent here):**
    - **Praxis contribution** via left PPC (BA5) → left BA39/BA40.
    - **Stereognosis dominance** via left S1 (BA1–BA2 complex) — the left
      S1 is the dominant substrate for bilateral tactile object
      recognition. The right S1 contributes to left-hand stereognosis but
      without the bilateral-loss phenotype.
*   **Symmetric Functions in this Partition (bilateral):**
    - S1 discriminative touch, pain, somatotopy (with hemibody flipped:
      right S1 → left hemibody).
    - S2 tactile attention and sensorimotor integration.
    - PPC reaching, grasping, spatial working memory.
    - PPC visuo-proprioceptive convergence for object localisation.

**A consumer that assumes "right parietal = symmetric" will be wrong for
the most clinically important content of this partition.** The right PPC
carries the **dominant** spatial-attention, neglect, and body-schema
functions — none of which are mirrored on the left. The left ``cortex``
aggregator's praxis and stereognosis dominance are equally absent here.
This is a **parallel-laden** pair at the functional-region level, just as
BA39 and BA40 are at the cytoarchitectonic level.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional partition, not cytoarchitectonic.** ``__all__`` lists
    the three **regions**, not the Brodmann areas. Consumers that need
    Brodmann fields must query ``brodmann_areas`` directly.
*   **Region-to-Brodmann mapping is data, not code.** The
    ``REGION_TO_BRODMANN`` constant makes the mapping explicit and
    greppable; the boundary cases (BA3 cross-listing, S2 ↔ ∅) are
    documented as data values, not as exception logic. The mapping is
    **identical to the left hemisphere**.
*   **Structural parity with left cortex.** Left and right ``cortex``
    aggregators must be structurally interchangeable so bilateral
    consumers can iterate hemispheres generically. The three regions and
    the ``REGION_TO_BRODMANN`` mapping are identical between hemispheres;
    only the lateralization prose attached to each region differs.

Usage
-----
Resolve functional regions by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.cortex import (
        REGIONS, REGION_TO_BRODMANN,
    )

    for region in REGIONS:
        # region is a functional module name, not a Brodmann area
        ...

Resolve by fully-qualified path string (used by the memory/recall layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.cortex.posterior_parietal_cortex"
    )

For Brodmann fields (a **different** partition of the same territory),
query the sibling aggregator::

    from ...parietal.brodmann_areas import ITERABLE_AREAS, AREA_PATHS
    # BA3 lives at a non-default path; use AREA_PATHS to resolve it

Cross-partition query (both functional region and Brodmann field)::

    # "Which Brodmann fields constitute the right PPC?"
    fields = REGION_TO_BRODMANN["posterior_parietal_cortex"]
    # -> ("brodmann_area_5", "brodmann_area_7")

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
    (Cytoarchitectonic partition — the sibling partition, not this one.)
*   Penfield, W., & Boldrey, E. (1937). *Brain*, 60(4), 389–443. (Classical
    S1 somatotopic mapping.)
*   Coghill, R.C., Gilron, I., & Iadarola, M.J. (2001). *J Neurophysiol*,
    85(6), 2602–2612. (Right-lateralized somatosensory processing; lesions
    to right, but not left, PPC produce tactile neglect; right PPC critical
    for spatial somatosensory processing.)[reference:18]
*   Malhotra, P., et al. (2009). *Brain*, 132(3), 645–660. (Right PPC
    critical for sustaining attention to spatial locations over time;
    right PPC lesions associated with vigilance decrement in neglect.)[reference:19]
*   Blankenburg, F., et al. (2003). *NeuroImage* / *J Neurophysiol* studies
    of S1 somatotopy. (BA3b, BA1, BA2 mirror-image somatotopic organization;
    applicable to both hemispheres.)[reference:20]
*   Eickhoff, S.B., et al. (2006). *NeuroImage*, 30(1), 174–185. (Observer-
    independent cytoarchitectonic mapping of S2 / OP1–OP4 — evidence that S2
    does not map to a single Brodmann field.)
*   Singh, A.K., et al. (2019). *Front Neurol*, 9, 1129. (Meta-analysis:
    bilateral S2 activation with unilateral tactile stimulation; right
    parietal operculum/S2 commonly activated for both hands, suggesting a
    lateralized pattern of bilateral integration.)[reference:21]
*   Fujiwara, T., et al. (2018). *Front Hum Neurosci* / Europe PMC. (Right
    S2 functionally connected to left PPC during tactile object
    recognition; asymmetric contra-/ipsilateral S2 connectivity.)[reference:22]
*   Berlucchi, G., & Aglioti, S.M. (2010). *Neuropsychologia*, 48(6),
    1583–1592. (Right parietal lobe largely responsible for severe
    perturbations of the internal representation of one's own body; body
    schema and self-recognition.)[reference:23]
*   Scheperjans, F., et al. (2008). *Cereb Cortex*, 18(4), 846–867.
    (Observer-independent mapping of SPC: BA5 and BA7 as distinct fields
    within PPC.)[reference:24]
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Parietal lobe (right), regions; FMA — Right parietal lobe
    partonomy.
*   Terminologia Anatomica (FIPAT, 2019) — parietal lobe gyri and sulci.
"""