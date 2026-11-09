"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.sulci
================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── cortex
                └── parietal
                    └── sulci                <-- THIS MODULE

**Primary synonym:** Parietal sulci (left); Parietal fissures.
**Organizing principle:** **Sulcal partition** — the **fourth** organizing
principle in the parietal lobe, alongside the functional partition
(``.../parietal/cortex``), the cytoarchitectonic partition
(``.../parietal/brodmann_areas``), and the structural partition
(``.../parietal/gyri``).
**Laterality:** left hemisphere.
**Sibling aggregators:** ``.../parietal/cortex`` (functional),
``.../parietal/brodmann_areas`` (cytoarchitectonic), ``.../parietal/gyri``
(structural). See "The Four Partitions" below.

Overview
--------
This module groups the **sulci** of the left parietal lobe — the
macroscopic **fissures** that form the visible boundaries of the gyral
surface. It is the **fourth organizing principle** in the parietal lobe,
after the functional, cytoarchitectonic, and structural partitions.

**The sulcal partition is the inverse view of the gyral partition.**
Where ``gyri`` documents the raised folds, ``sulci`` documents the
fissures that separate them. The two partitions are **complementary and
non-redundant**: a gyrus is defined by the sulci that bound it, and a sulcus
is defined by the gyri it separates. Consumers that need "what is the
boundary of X gyrus?" should query ``sulci``; consumers that need "what is
the surface entity here?" should query ``gyri``.

The four organizing principles are **complementary, non-nesting, and
coordinate** — each is a different slice through the same anatomical
territory:

*   **``cortex``** answers *"which functional region is this?"* — S1, S2,
    PPC.
*   **``brodmann_areas``** answers *"which cytoarchitectonic field is
    this?"* — BA1, BA2, BA3, BA5, BA7, BA26, BA39, BA40.
*   **``gyri``** answers *"which macroscopic surface convolution is
    this?"* — postcentral gyrus, precuneus, paracentral lobule.
*   **``sulci``** (this module) answers *"which macroscopic surface
    fissure is this?"* — intraparietal sulcus, postcentral sulcus,
    marginal sulcus.

**A sulcal partition does not respect functional or cytoarchitectonic
boundaries.** A single sulcus can straddle two functional regions (e.g., the
intraparietal sulcus separates BA5/BA7 from BA39/BA40 and is a key
functional landmark for the dorsal attention network). Conversely, a
functional region can span multiple sulci (e.g., PPC spans the
intraparietal sulcus and the parieto-occipital sulcus).

Child Modules
-------------
Three sulci are wired under this package:

*   ``intraparietal_sulcus`` (**IPS**) — the **major** sulcus of the
    parietal lobe. It runs anteroposteriorly through the lateral parietal
    surface, separating the **superior parietal lobule** (BA5 + BA7) from
    the **inferior parietal lobule** (BA39 + BA40). It is the **principal
    anatomical landmark for the dorsal attention network** and contains
    functionally defined subregions (LIP, VIP, AIP, MIP, CIP, PIP) that are
    critical for visually guided reaching, grasping, saccades, and spatial
    attention.

*   ``postcentral_sulcus`` — the **posterior boundary of the postcentral
    gyrus** and the **anterior boundary of the superior parietal lobule**.
    It separates BA1/BA2 (the caudal S1 fields) from BA5 (the first
    association field). It is the structural landmark that the BA5/BA2
    thalamic-input boundary follows.

*   ``marginal_sulcus`` — the **marginal branch of the cingulate sulcus**
    on the medial surface. It forms the **anterior boundary of the
    precuneus** and the **posterior boundary of the paracentral lobule**.
    It is the medial-surface landmark that separates the parietal lobe from
    the frontal lobe (paracentral lobule's anterior half) and from the
    cingulate gyrus.

**Sulci that are NOT wired in this package** — the sulcal partition of the
parietal lobe is **incomplete** in this tree, and consumers must know which
sulci are missing:

*   **Central sulcus** — the **anterior boundary of the parietal lobe** and
    the boundary between the precentral and postcentral gyri. It is
    **shared with the frontal lobe** and is not wired under the parietal
    ``sulci/`` container. A complete structural query for the central sulcus
    must query the frontal lobe's ``sulci/`` container (if wired).
*   **Parieto-occipital sulcus** — the **posterior boundary of the parietal
    lobe** and the boundary between the precuneus and the cuneus. It is
    **shared with the occipital lobe** and is not wired here. A complete
    structural query must query the occipital lobe's ``sulci/`` container
    (if wired).
*   **Subparietal sulcus** — the **inferior boundary of the precuneus** on
    the medial surface. It is a **parietal-only sulcus** that is
    **structurally omitted** from this tree. Consumers that need it must
    fall back on the atlas-level documentation (Ono et al., 1990; Duvernoy,
    1999).
*   **Lateral sulcus / Sylvian fissure** — the **inferior boundary of the
    parietal lobe** and the boundary between the parietal operculum
    (containing S2) and the superior temporal gyrus. It is **shared with
    the temporal lobe** and is not wired here.

**This is the most important consumer-facing fact about this module:** the
``sulci`` partition is **neither complete nor closed**. It covers the
**intraparietal** and **postcentral** sulci on the lateral surface and the
**marginal** sulcus on the medial surface, but it omits the **central**,
**parieto-occipital**, **subparietal**, and **lateral** sulci. A consumer
that iterates ``sulci`` and assumes completeness will be **wrong** for
these four major fissures.

The Four Partitions
-------------------
The left parietal lobe is the **first region in the brainparts tree** with
**all four** organizing principles wired:

::

    Functional         Cytoarchitectonic      Structural           Sulcal
    ──────────         ────────────────       ──────────           ──────
    cortex/            brodmann_areas/        gyri/                sulci/
    ├── S1             ├── BA1                ├── postcentral      ├── intraparietal
    ├── S2             ├── BA2                │   └── BA3 (cross)  ├── postcentral
    └── PPC            ├── BA5                ├── precuneus        └── marginal
                       ├── BA7                └── paracentral
                       ├── BA26 (boundary)        (shared with
                       ├── BA39                    frontal lobe)
                       └── BA40

**The four partitions are related, but not by nesting.** The sulcal
partition is **structurally the inverse** of the gyral partition:

*   ``intraparietal_sulcus`` **separates** BA5/BA7 (superior parietal
    lobule) from BA39/BA40 (inferior parietal lobule). It is the **major**
    functional landmark of the dorsal attention network.
*   ``postcentral_sulcus`` **separates** BA1/BA2 (postcentral gyrus) from
    BA5 (superior parietal lobule). It is the **structural landmark** for
    the S1 → PPC transition.
*   ``marginal_sulcus`` **separates** the paracentral lobule (medial S1/M1)
    from the precuneus (medial BA7). It is the **medial-surface landmark**
    for the sensory-to-DMN transition.

**The sulcal partition is the "negative space" of the gyral partition.**
Every gyrus in ``gyri/`` is bounded by one or more of the sulci in
``sulci/`` (or by sulci not wired here). The two partitions are best
consumed together: a consumer that wants "where is the precuneus?" queries
``gyri.precuneus``; a consumer that wants "what are the boundaries of the
precuneus?" queries ``sulci.marginal_sulcus`` (anteriorly), the
parieto-occipital sulcus (posteriorly; **not wired**), and the subparietal
sulcus (inferiorly; **not wired**).

Function in the Human Brain
---------------------------
The sulcal partition is **structural, not functional**, so it does not have
a "function" in the sense that S1, S2, and PPC do. However, each sulcus in
this package is a **functional landmark** for a distinct set of processes:

*   **``intraparietal_sulcus``** — the principal anatomical landmark for the
    **dorsal attention network** (with functional subregions LIP, VIP, AIP,
    MIP, CIP, PIP). Supports **visually guided reaching, grasping,
    saccades, spatial attention, and multisensory spatial integration**.
    Its depth and continuity are structurally asymmetric (often deeper and
    more continuous on the right), which contributes to the right-hemisphere
    dominance for spatial attention.
*   **``postcentral_sulcus``** — the structural landmark for the **S1 →
    PPC transition**. Marks the boundary between the **unimodal
    somatosensory** postcentral gyrus and the **unimodal-to-polymodal**
    association cortex of the superior parietal lobule.
*   **``marginal_sulcus``** — the medial-surface landmark for the
    **sensory-to-DMN transition**. Separates the **medial S1/M1** of the
    paracentral lobule (sensorimotor) from the **medial BA7** of the
    precuneus (default mode network).

Lateralization Notes
--------------------
This is the **left** sulcal aggregator. The sulcal partition is **symmetric
by name** — both left and right parietal lobes have an intraparietal sulcus,
a postcentral sulcus, and a marginal sulcus — but the **morphological
properties** of these sulci are **asymmetric**, and the asymmetry is
documented here:

*   **``intraparietal_sulcus``** — the **right** IPS is typically **deeper
    and more continuous** than the left, and its **depth asymmetry**
    correlates with the right-hemisphere dominance for spatial attention.
    The left IPS is often more **segmented** and its anterior segment is
    more variable. Sulcal pattern analysis confirms that
    **left-right asymmetries are more common than expected by chance** in
    the intraparietal region.
*   **``postcentral_sulcus``** — the postcentral sulcus shows **moderate
    left-right asymmetry**, with the right side slightly longer and more
    posteriorly extended in many individuals.
*   **``marginal_sulcus``** — the marginal sulcus is **largely symmetric**
    in the gross-anatomical sense, though its **continuity with the
    cingulate sulcus** varies individually.

**These morphological asymmetries are structural, not syndromic.** They
contribute to the functional lateralization of the parietal lobe (right
dominance for spatial attention; left dominance for language and praxis) but
they are not themselves syndromes. A consumer that needs the
**functional** lateralization claims should query the BA7, BA39, BA40, and
PPC modules; the sulcal partition documents **where the boundaries are**,
not **what they do**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from the
    frontal lobe's ``sulci/`` (for the central sulcus) or the occipital
    lobe's ``sulci/`` (for the parieto-occipital sulcus). Those sulci are
    shared boundaries and are **not** wired here.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Sulcal partition, not structural or functional.** ``__all__`` lists
    the three **sulci**, not the gyri they bound or the functional regions
    they separate.
*   **Sulcal partition is incomplete.** The central, parieto-occipital,
    subparietal, and lateral sulci are **not wired here**. Consumers must
    know this and fall back on the corresponding lobes (or the atlas
    literature) for those boundaries. The ``MISSING_SULCI`` constant below
    makes the omission explicit and greppable.
*   **Structural parity with right sulci.** Left and right ``sulci``
    aggregators must be structurally interchangeable so bilateral consumers
    can iterate hemispheres generically. The three sulci are identical
    between hemispheres; only the **morphological asymmetry prose** (right
    IPS deeper; right postcentral longer) differs.

Usage
-----
Resolve sulci by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.cortex.parietal.sulci import (
        SULCI, MISSING_SULCI, BOUNDARY_FOR_GYRUS,
    )

    for sulcus in SULCI:
        # sulcus is a structural boundary module, not a functional region
        ...

Resolve by fully-qualified path string (used by the memory/recall layer)::

    path = (
        "telencephalon.cerebral_hemispheres.left.cortex."
        "parietal.sulci.intraparietal_sulcus"
    )

Boundary query (which sulci bound a gyrus)::

    # "What are the boundaries of the left postcentral gyrus?"
    boundaries = BOUNDARY_FOR_GYRUS["postcentral_gyrus"]
    # -> ("central_sulcus" [not wired], "postcentral_sulcus")

**Do not** assume the sulcal partition is complete. Query ``MISSING_SULCI``
to see which boundaries are not wired.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        sulci_pkg = importlib.import_module(
            f"infrastructure.brainparts.forebrain.telencephalon."
            f"cerebral_hemispheres.{side}.cortex.parietal.sulci"
        )
        for sulcus in sulci_pkg.SULCI:
            # query the right- or left-hemisphere sulcus
            ...

References
----------
*   Terminologia Anatomica (FIPAT, 2019) — sulcus intraparietalis, sulcus
    postcentralis, sulcus marginalis. (Hemisphere-symmetric sulcal names.)
*   Ono, M., Kubik, S., & Abernathey, C.D. (1990). *Atlas of the Cerebral
    Sulci*. (The primary structural atlas for sulcal anatomy; includes the
    intraparietal, postcentral, and marginal sulci as well as the missing
    central, parieto-occipital, subparietal, and lateral sulci.)
*   Duvernoy, H.M. (1999). *The Human Brain: Surface, Three-Dimensional
    Sectional Anatomy with MRI, and Blood Supply*. (Sulcal landmarks on
    MRI.)
*   **Intraparietal sulcus — dorsal attention network:** Corbetta, M., &
    Shulman, G.L. (2011). *Nat Rev Neurosci*, 12(3), 114–122. (The IPS is
    the principal anatomical landmark for the dorsal attention network;
    functional subregions LIP, VIP, AIP, MIP, CIP, PIP.)
*   **Intraparietal sulcus — morphology and asymmetry:** *Left-right
    asymmetry of the intraparietal sulcus* (2021), *Brain Struct Funct*.
    (The right IPS is typically deeper and more continuous than the left;
    sulcal asymmetries are more common than expected by chance.)
*   **Postcentral sulcus — structural landmark:** *Neuroanatomy, Postcentral
    Gyrus* (StatPearls, 2023), NCBI Bookshelf NBK549825. (The postcentral
    sulcus forms the posterior boundary of the postcentral gyrus and the
    anterior boundary of the superior parietal lobule.)
*   **Marginal sulcus — medial surface:** *Dorsomedial Motor Region:
    Paracentral Lobule and the Supplementary Motor Region* (ScienceDirect);
    *Morphology and Morphometry of Human Paracentral Lobule* (2021),
    *Asian J Neurosurg*, 16(2), 349–354. (The marginal sulcus bounds the
    paracentral lobule anteriorly and the precuneus posteriorly.)
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed. (Sulcal and gyral landmarks.)
*   NeuroNames — Parietal sulci (left); FMA — left parietal lobe partonomy.
"""