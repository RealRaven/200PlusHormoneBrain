"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex
================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── cortex            <-- THIS MODULE

**Primary synonym:** Parietal cortex (left); Parietal neocortex.
**Organizing principle:** **Functional–anatomical partition**, NOT
cytoarchitectonic.
**Laterality:** left hemisphere.
**Sibling aggregator:** ``.../parietal/brodmann_areas`` — a *different*
partition of the *same* anatomical territory. See "The Two Partitions"
below; this distinction is the single most important thing a consumer must
know about this module.

Overview
--------
This module groups the **functional regions** of the left parietal lobe:
the two somatosensory cortical areas (primary and secondary) and the
posterior parietal association cortex. It is the **functional twin** of the
cytoarchitectonic partition at ``.../parietal/brodmann_areas``.

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
asks "does the left parietal lobe contain S1?" and only queries
``brodmann_areas`` will get a *partial* answer (BA1, BA2, and a broken
link to BA3); a consumer that asks "which Brodmann areas are in PPC?" and
only queries ``cortex`` will miss that BA5 and BA7 are distinct fields
with distinct thalamic connectivity.

Child Modules
-------------
Three functional regions are wired under this package:

*   ``primary_somatosensory_cortex`` (**S1**) — the thalamic gateway for
    discriminative touch, proprioception, and nociception. Constituted
    functionally by **BA3a/3b + BA1 + BA2**. On the left side, S1
    represents the **right** hemibody.

*   ``secondary_somatosensory_cortex`` (**S2**) — the second
    somatosensory field, located on the upper bank of the lateral sulcus /
    parietal operculum, posterior to S1. S2 receives input from S1 and from
    the thalamus (VPI), has **larger and more bilateral receptive fields**
    than S1, and supports **tactile attention and sensorimotor integration**.
    On the left side, S2 represents primarily the **right** hemibody, with
    a substantial bilateral component.

*   ``posterior_parietal_cortex`` (**PPC**) — the polymodal association
    territory, comprising **BA5 + BA7**. Supports **reaching, grasping,
    spatial attention, and visuomotor integration**. On the left side, PPC
    is **not** the dominant substrate for hemispatial neglect (that role
    belongs to right PPC); it contributes to right-hemispace visuomotor
    guidance and to the praxis network.

**Areas *not* covered by this functional partition:**

*   **BA39 (angular gyrus)** and **BA40 (supramarginal gyrus)** have no
    functional-region parent in this module. They are wired only under
    ``brodmann_areas``. This is a **deliberate omission**: the classical
    S1/S2/PPC functional partition was defined before the inferior parietal
    lobule was recognized as a distinct heteromodal association system.
    Consumers needing BA39/BA40 must query ``brodmann_areas``.
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

The mapping is **many-to-many-ish** in the sense that:

*   **S1 → {BA1, BA2, BA3}** — a clean three-to-one mapping, with the
    caveat that BA3 is cross-listed under the postcentral gyrus.
*   **S2 → ∅** — S2 does **not** map cleanly to any single Brodmann
    field. The conventional label is **BA43** (subcentral area), but the
    tree does not currently wire BA43 anywhere. S2 is therefore a
    **functional region with no cytoarchitectonic anchor** in this
    project, and that is a documented fact, not an oversight.
*   **PPC → {BA5, BA7}** — a clean two-to-one mapping. Both are unimodal
    (BA5) or polymodal (BA7) somatosensory/visuomotor association
    cortex, but they are distinguished by thalamic connectivity (BA5 is
    still S1-adjacent; BA7 is fully polymodal).
*   **{BA39, BA40, BA26} → ∅ (from this module's perspective)** — three
    Brodmann areas with no functional-region parent. See "Child Modules"
    for the rationale.

**Consumers must not assume the two partitions nest.** They are two
independent slices through the same anatomical territory, and the
right way to query them is to choose the slice that answers the question
being asked.

Function in the Human Brain
---------------------------
The three functional regions collectively cover the **somatosensory and
visuomotor** functions of the left parietal lobe:

*   **Primary Somatosensory Cortex (S1):** Discriminative touch, texture
    (BA1), shape/size (BA2), proprioception, nociception, somatotopic
    representation of the **right** hemibody. Thalamic gateway (VPL/VPM).
*   **Secondary Somatosensory Cortex (S2):** Tactile attention, bilateral
    sensory integration, sensorimotor coupling. Receives from S1 and VPI;
    has larger, more bilateral receptive fields than S1.
*   **Posterior Parietal Cortex (PPC):** Visuomotor integration for
    reaching and grasping (BA5 → planning, BA7 → polymodal spatial
    transformation), spatial attention, body schema. On the left, PPC
    contributes to the **praxis network** (with left BA39/BA40) and to
    right-hemispace visuomotor guidance.

**Functions *not* covered by this functional partition** (they belong to
the ``brodmann_areas`` partition only):

*   **Language-semantic** and **number** processing (left BA39).
*   **Phonological loop**, **conduction aphasia**, **praxis storage**
    (left BA40).
*   **Hemispatial neglect** and **spatial-awareness dominance** (right
    BA39/BA40 — the right-side counterparts; not relevant to this left
    module but worth noting for symmetry).

Lateralization Notes
--------------------
This is the **left** functional-parietal module. The lateralization
landscape is **mixed** — some functions in this partition are
left-dominant, some are right-dominant, and the split is **not** aligned
with the S1/S2/PPC functional boundaries:

*   **Left-Lateralized Functions in this Partition:**
    - **Praxis contribution** via PPC (BA5) → left BA39/BA40 — the left
      PPC is part of the left-lateralized praxis network.
    - **Stereognosis dominance** via S1 (BA1–BA2 complex) — the left S1
      is the dominant substrate for bilateral tactile object recognition.
    - **Lexical-semantic and number** functions live in BA39/BA40 (not in
      this partition), so they are **not** carried here.
*   **Right-Lateralized Functions in this Partition (contrast):**
    - **Hemispatial neglect** and **spatial-awareness dominance** belong
      to the **right** PPC (right BA7) and **right** BA39/BA40 — **not**
      to this left module.
    - **Bimanual coordination** and **mental-rotation dominance** belong
      to the **right** BA7.
*   **Symmetric Functions in this Partition (bilateral):**
    - S1 discriminative touch, pain, somatotopy (with hemibody flipped).
    - S2 tactile attention and sensorimotor integration.
    - PPC reaching, grasping, spatial working memory.
    - PPC visuo-proprioceptive convergence for object localisation.

**A consumer that assumes "left parietal = left-lateralized" will be
wrong for half of this partition's contents.** The left S1 and left PPC
each carry **both** left-lateralized (praxis, stereognosis) and
symmetric (touch, reaching) functions, and the neglect/spatial-attention
functions that consumers most strongly associate with "parietal cortex"
belong to the **right** hemisphere, not this one.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Functional partition, not cytoarchitectonic.** ``__all__`` lists
    the three **regions**, not the Brodmann areas. Consumers that need
    Brodmann fields must query ``brodmann_areas`` directly.
*   **Region-to-Brodmann mapping is data, not code.** The
    ``REGION_TO_BRODMANN`` constant makes the mapping explicit and
    greppable; the boundary cases (BA3 cross-listing, S2 ↔ ∅) are
    documented as data values, not as exception logic.
*   **Structural parity with right cortex.** Left and right ``cortex``
    aggregators must be structurally interchangeable so bilateral
    consumers can iterate hemispheres generically. The three regions are
    identical between hemispheres; only the lateralization prose differs.

Usage
-----
Resolve functional regions by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.cortex import (
        REGIONS, REGION_TO_BRODMANN,
    )

    for region in REGIONS:
        # region is a functional module name, not a Brodmann area
        ...

Resolve by fully-qualified path string (used by the memory/recall layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.cortex.primary_somatosensory_cortex"
    )

For Brodmann fields (a **different** partition of the same territory),
query the sibling aggregator::

    from ...parietal.brodmann_areas import ITERABLE_AREAS, AREA_PATHS
    # BA3 lives at a non-default path; use AREA_PATHS to resolve it

Cross-partition query (both functional region and Brodmann field)::

    # "Which Brodmann fields constitute the left S1?"
    fields = REGION_TO_BRODMANN["primary_somatosensory_cortex"]
    # -> ("brodmann_area_1", "brodmann_area_2", "brodmann_area_3")

References
----------
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
    (Cytoarchitectonic partition — the sibling partition, not this one.)
*   Penfield, W., & Boldrey, E. (1937). *Brain*, 60(4), 389–443. (Classical
    S1 somatotopic mapping; the functional partition's empirical origin.)
*   Disbrow, E., et al. (2000). *J Neurophysiol*, 83(5), 2956–2964. (S2
    somatotopy and receptive-field properties.)
*   Eickhoff, S.B., et al. (2006). *NeuroImage*, 30(1), 174–185. (Observer-
    independent cytoarchitectonic mapping of S2 / OP1–OP4 — the modern
    evidence that S2 does not map to a single Brodmann field.)
*   Bodegàrd, A., et al. (2001). *Neuron*, 31(2), 317–328. (Hierarchical
    serial processing within S1: BA3b → BA1 → BA2.)
*   Scheperjans, F., et al. (2008). *Cereb Cortex*, 18(4), 846–867.
    (Observer-independent mapping of SPC: BA5 and BA7 as distinct fields
    within PPC.)
*   Le, A., et al. (2017). *J Neurophysiol*, 117(2), 624–636. (PPC reach /
    grasp / bimanual — right-lateralised bimanual dominance, documented here
    only as a contrast case.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed.
*   NeuroNames — Parietal lobe (left), regions; FMA — Left parietal lobe
    partonomy.
*   Terminologia Anatomica (FIPAT, 2019) — parietal lobe gyri and sulci.
"""