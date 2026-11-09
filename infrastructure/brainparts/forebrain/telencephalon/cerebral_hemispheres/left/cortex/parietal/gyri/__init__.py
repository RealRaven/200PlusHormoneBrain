"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri
===============================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── gyri                <-- THIS MODULE

**Primary synonym:** Parietal gyri (left); Parietal convolutions.
**Organizing principle:** **Structural / gyral partition** — the third
organizing principle in the parietal lobe, alongside the functional
partition (``.../parietal/cortex``) and the cytoarchitectonic partition
(``.../parietal/brodmann_areas``).
**Laterality:** left hemisphere.
**Sibling aggregators:** ``.../parietal/cortex`` (functional) and
``.../parietal/brodmann_areas`` (cytoarchitectonic). See "The Three
Partitions" below.

Overview
--------
This module groups the **gyri** of the left parietal lobe — the macroscopic
surface convolutions that are the **structural** partition of the parietal
territory. It is the **third organizing principle** in the parietal lobe,
after the functional partition (S1 / S2 / PPC) and the cytoarchitectonic
partition (Brodmann areas).

The three organizing principles are **complementary, non-nesting, and
coordinate** — each is a different slice through the same anatomical
territory, and each answers a different question:

*   **``cortex``** answers *"which functional region is this?"* — S1, S2,
    PPC. Used by systems neuroscience and clinical topology.
*   **``brodmann_areas``** answers *"which cytoarchitectonic field is
    this?"* — Brodmann (1909) fields. Used by neuroimaging atlases and by
    the FMA.
*   **``gyri``** (this module) answers *"which macroscopic surface
    convolution is this?"* — the gyral landmarks that are visible on
    every MRI, CT, and gross specimen. Used by clinical radiology,
    surgical planning, and any consumer that works from structural
    imaging.

**A gyral partition does not respect functional or cytoarchitectonic
boundaries — and the boundaries of the three partitions do not align.**
Three examples from the parietal lobe make this concrete:

1.  **The postcentral gyrus is the structural home of S1 — but S1 is a
    *functional* region, and BA3 (a *cytoarchitectonic* field) lives
    under the postcentral gyrus's subtree.** The gyrus is the anatomical
    container; S1 is the functional node; BA3 is the cytoarchitectonic
    node. All three exist, and none is redundant with the others.

2.  **The paracentral lobule straddles the frontal–parietal boundary.**
    Its anterior half belongs to the frontal lobe (BA4, primary motor);
    its posterior half belongs to the parietal lobe (BA3/1/2, primary
    somatosensory). The gyrus is a single structural entity that spans
    two lobes and two functional regions.

3.  **The precuneus is the medial extent of BA7 — but BA7 is a *single*
    cytoarchitectonic field that spans both the lateral superior parietal
    lobule and the medial precuneus.** The precuneus is a structural
    subdivision of BA7, not a separate field.

**Consumers must not assume the three partitions nest.** They are three
independent slices through the same territory, and the right way to query
them is to choose the slice that answers the question being asked.

Child Modules
-------------
Three gyri are wired under this package:

*   ``postcentral_gyrus`` — the **structural home of S1**. Contains
    **BA3** (cross-listed; the thalamic gateway of S1) as a child.
    Bounded anteriorly by the central sulcus, posteriorly by the
    postcentral sulcus. The principal cortical surface visible on every
    MRI in the parietal lobe.

*   ``precuneus`` — the **medial extent of BA7**. A medial-surface gyrus
    bounded by the marginal sulcus (anteriorly), the parieto-occipital
    sulcus (posteriorly), and the cingulate sulcus (inferiorly).
    Contributes to the default mode network, episodic memory retrieval,
    and self-referential processing — a **functional** role that is
    documented in the BA7 leaf and in the PPC leaf, not here.

*   ``paracentral_lobule`` — a **single structural gyrus straddling the
    frontal–parietal boundary**. Its anterior half is BA4 (frontal;
    primary motor); its posterior half is BA3/1/2 (parietal; primary
    somatosensory). The **parietal half** is documented here; the
    **frontal half** is documented under
    ``.../frontal/gyri/paracentral_lobule`` (if wired). Consumers that
    need the full paracentral lobule must query **both lobes**.

**Structural anomalies and cross-listings in this package:**

*   **``postcentral_gyrus/brodmann_area_3``** — this is the **cross-listed
    BA3** that the ``brodmann_areas`` aggregator promises to resolve via
    ``AREA_PATHS["brodmann_area_3"]``. It is the **only** Brodmann-area
    leaf that lives under a gyral container rather than under the
    ``brodmann_areas`` aggregator.

*   **``paracentral_lobule``** — the **only** gyrus in this package that
    is **shared with another lobe**. Its frontal half is not documented
    here; a full structural query for the paracentral lobule requires
    iterating both the frontal and parietal gyral containers.

The Three Partitions
--------------------
The parietal lobe is the **first region in the brainparts tree** with all
**three** organizing principles fully wired:

::

    Functional partition     Cytoarchitectonic partition    Structural partition
    ────────────────────     ──────────────────────────     ────────────────────
    cortex/                  brodmann_areas/                gyri/   <-- THIS
    ├── S1                   ├── BA1                        ├── postcentral_gyrus
    ├── S2                   ├── BA2                        │   └── BA3 (cross-
    └── PPC                  ├── BA5                        │       listed)
                             ├── BA7                        ├── precuneus
                             ├── BA26 (boundary; also       └── paracentral_lobule
                             │   under cingulate)               (shared with
                             ├── BA39                           frontal lobe)
                             └── BA40

**The three partitions are related, but not by nesting:**

*   **S1 (functional) → postcentral_gyrus (structural) → BA1, BA2, BA3
    (cytoarchitectonic)** — a clean three-way correspondence, with BA3
    living under the gyrus.
*   **S2 (functional) → parietal operculum (structural; not a gyrus) →
    OP1–OP4 (cytoarchitectonic; not Brodmann)** — a clean three-way
    correspondence, but the structural and cytoarchitectonic anchors are
    **not** in this module. S2 lives on the upper bank of the lateral
    sulcus, which is not a gyrus in the classical sense.
*   **PPC (functional) → superior parietal lobule + precuneus
    (structural) → BA5 + BA7 (cytoarchitectonic)** — a many-to-many
    correspondence. PPC spans two structural regions and two
    cytoarchitectonic fields.
*   **BA39 (cytoarchitectonic) → angular gyrus (structural)** — the
    angular gyrus is not wired as a separate module in this tree; it
    lives only as the BA39 leaf under ``brodmann_areas``. This is a
    **structural omission**: the angular gyrus is a gyrus, but it is not
    in ``gyri/``.
*   **BA40 (cytoarchitectonic) → supramarginal gyrus (structural)** —
    same situation: not wired under ``gyri/``.

**This is the most important consumer-facing fact about this module:**
the ``gyri`` partition does not cover the **entire** parietal lobe. The
inferior parietal lobule's gyri (angular gyrus, supramarginal gyrus) are
**not** wired here. Consumers that need a complete structural partition of
the parietal lobe must query ``gyri`` **plus** the BA39 and BA40 leaves
for the missing gyral names.

Function in the Human Brain
---------------------------
The gyral partition is **structural, not functional**, so it does not have
a "function" in the sense that S1, S2, and PPC do. However, each gyrus
in this package **contains** functional and cytoarchitectonic content:

*   **``postcentral_gyrus``** contains **S1** (functional) and **BA3,
    BA1, BA2** (cytoarchitectonic). Its functions are those of S1:
    discriminative touch, texture, shape/size, proprioception,
    nociception, and somatotopy of the right hemibody.
*   **``precuneus``** contains the **medial extent of BA7** and is a core
    node of the **default mode network** — episodic memory retrieval,
    self-referential processing, visuospatial imagery.
*   **``paracentral_lobule``** (parietal half) contains the **medial
    extent of S1** (leg/foot representation) and is part of the
    sensorimotor strip.

Consumers that need the **function** of a gyrus should query its
corresponding functional-region module (S1, PPC) or its cytoarchitectonic
leaf (BA3, BA7), not this structural aggregator. This module documents
**where** the gyri are and **what they contain**; the functional and
cytoarchitectonic children document **what they do**.

Lateralization Notes
--------------------
This is the **left** gyral aggregator. The gyral partition is **symmetric**
between hemispheres at the level of **gyral names** — both left and right
parietal lobes have a postcentral gyrus, a precuneus, and a paracentral
lobule — but the **contents** of each gyrus are lateralized at the
functional and cytoarchitectonic levels:

*   **``postcentral_gyrus``** — the left postcentral gyrus contains the
    **left S1** and **left BA1/BA2/BA3**, which are **left-loaded** for
    stereognosis dominance and complex finger movement dominance. The
    right postcentral gyrus contains the right S1, which carries a
    left-hand facilitation weighting and a contralateral-only
    astereognosis phenotype.
*   **``precuneus``** — the precuneus is a **mostly symmetric** DMN node,
    with some evidence for right-lateralized activity during episodic
    retrieval and spatial imagery. The left precuneus contributes more
    to semantic and verbal aspects of memory; the right precuneus
    contributes more to spatial and visual aspects.
*   **``paracentral_lobule``** — the parietal half is **symmetric** at the
    functional level (medial S1 for the contralateral leg/foot).
    Lateralization is not a structural property of the gyrus; it is
    encoded in the functional and cytoarchitectonic contents.

**A consumer that iterates the gyral partition will get a symmetric list
of names, but the functional content of each gyrus is asymmetric.** The
gyral partition itself does not carry lateralization claims; those belong
to the functional and cytoarchitectonic partitions.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Structural partition, not functional or cytoarchitectonic.**
    ``__all__`` lists the three **gyri**, not the functional regions or
    Brodmann fields they contain.
*   **BA3 is cross-listed here.** The ``postcentral_gyrus/brodmann_area_3``
    leaf is the resolution target for
    ``brodmann_areas.AREA_PATHS["brodmann_area_3"]``. Consumers that
    iterate ``brodmann_areas.ITERABLE_AREAS`` will resolve BA3 through
    this subtree.
*   **The paracentral lobule is shared with the frontal lobe.** Its
    parietal half is documented here; its frontal half is documented
    under ``.../frontal/gyri/paracentral_lobule`` (if wired). Consumers
    that need the full paracentral lobule must query both lobes.
*   **The inferior parietal gyri are NOT wired here.** The angular gyrus
    and supramarginal gyrus are not children of ``gyri/`` — they exist
    only as BA39 and BA40 leaves under ``brodmann_areas``. This is a
    **structural omission**, documented here so consumers do not assume
    the gyral partition is complete.
*   **Structural parity with right gyri.** Left and right ``gyri``
    aggregators must be structurally interchangeable so bilateral
    consumers can iterate hemispheres generically. The three gyri are
    identical between hemispheres; only the functional and
    cytoarchitectonic **contents** of each gyrus differ.

Usage
-----
Resolve gyri by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.gyri import (
        GYRI, CONTAINED_REGIONS, CONTAINED_BRODMANN_AREAS,
    )

    for gyrus in GYRI:
        # gyrus is a structural module name, not a functional region
        ...

Resolve by fully-qualified path string (used by the memory/recall layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.gyri.postcentral_gyrus"
    )

For the cross-listed BA3 (the only Brodmann-area leaf under a gyrus)::

    from ...parietal.gyri.postcentral_gyrus import brodmann_area_3

Cross-partition query (which functional regions and Brodmann areas are
contained in a gyrus)::

    # "Which functional regions are in the left postcentral gyrus?"
    regions = CONTAINED_REGIONS["postcentral_gyrus"]
    # -> ("primary_somatosensory_cortex",)

    # "Which Brodmann areas are in the left postcentral gyrus?"
    bas = CONTAINED_BRODMANN_AREAS["postcentral_gyrus"]
    # -> ("brodmann_area_3", "brodmann_area_1", "brodmann_area_2")

References
----------
*   Terminologia Anatomica (FIPAT, 2019) — gyrus postcentralis, precuneus,
    lobulus paracentralis.
*   Ono, M., Kubik, S., & Abernathey, C.D. (1990). *Atlas of the Cerebral
    Sulci*. (Gyral and sulcal anatomy; the structural partition's primary
    atlas.)
*   Duvernoy, H.M. (1999). *The Human Brain: Surface, Three-Dimensional
    Sectional Anatomy with MRI, and Blood Supply*. (Gyral landmarks on
    MRI.)
*   Brodmann, K. (1909). *Vergleichende Lokalisationslehre der Grosshirnrinde*.
    (Cytoarchitectonic partition — the sibling partition, not this one.)
*   Penfield, W., & Boldrey, E. (1937). *Brain*, 60(4), 389–443. (Functional
    partition — the sibling partition, not this one.)
*   Cavanna, A.E., & Trimble, M.R. (2006). *Brain*, 129(3), 564–583.
    (Precuneus: medial extent of BA7; DMN and episodic memory.)
*   Eickhoff, S.B., et al. (2006). *NeuroImage*, 30(1), 174–185. (S2 /
    OP1–OP4 — the functional region on the parietal operculum, which is
    not a gyrus in this module.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed. (Gyral and sulcal landmarks.)
*   NeuroNames — Parietal gyri (left); FMA — left parietal lobe partonomy.
"""