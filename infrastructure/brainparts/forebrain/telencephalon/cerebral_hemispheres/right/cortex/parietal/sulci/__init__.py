"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.sulci
=================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── cortex
                └── parietal
                    └── sulci                <-- THIS MODULE

**Primary synonym:** Parietal sulci (right); Parietal fissures.
**Organizing principle:** **Sulcal partition** — the **fourth** organizing
principle in the right parietal lobe, alongside the functional partition
(``.../parietal/cortex``), the cytoarchitectonic partition
(``.../parietal/brodmann_areas``), and the structural partition
(``.../parietal/gyri``).
**Laterality:** right hemisphere.
**Sibling aggregators:** ``.../parietal/cortex`` (functional),
``.../parietal/brodmann_areas`` (cytoarchitectonic), ``.../parietal/gyri``
(structural). See "The Four Partitions" below.

Overview
--------
This module groups the **sulci** of the **right** parietal lobe — the
macroscopic **fissures** that form the visible boundaries of the gyral
surface. It is the **fourth organizing principle** in the right parietal
lobe and the structural mirror of the left sulcal aggregator at
``.../left/cortex/parietal/sulci``.

**The sulcal partition is the inverse view of the gyral partition.** Where
``gyri`` documents the raised folds, ``sulci`` documents the fissures that
separate them. The two partitions are **complementary and non-redundant**:
a gyrus is defined by the sulci that bound it, and a sulcus is defined by
the gyri it separates. Consumers that need "what is the boundary of X
gyrus?" should query ``sulci``; consumers that need "what is the surface
entity here?" should query ``gyri``.

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
Three sulci are wired under this package, **identical in name and position
to the left hemisphere**:

*   ``intraparietal_sulcus`` (**IPS**) — the **major** sulcus of the
    parietal lobe. It runs anteroposteriorly through the lateral parietal
    surface, separating the **superior parietal lobule** (BA5 + BA7) from
    the **inferior parietal lobule** (BA39 + BA40). On the **right** side,
    the IPS is the **core node of the right-lateralized spatial-attention
    network** and is causally implicated in **street-crossing decisions**
    and **time-to-collision / distance estimation** . It contains the
    functionally defined subregions (LIP, VIP, AIP, MIP, CIP, PIP) that
    support **visually guided reaching, grasping, saccades, and spatial
    attention**.

*   ``postcentral_sulcus`` — the **posterior boundary of the postcentral
    gyrus** and the **anterior boundary of the superior parietal lobule**.
    It separates BA1/BA2 (the caudal S1 fields) from BA5 (the first
    association field). On the **right** side, the trajectory of the
    postcentral sulcus **shifts more anteriorly** than on the left, and
    the central sulcus (its anterior neighbour) is **generally deeper and
    larger** in the right hemisphere .

*   ``marginal_sulcus`` — the **marginal branch of the cingulate sulcus**
    on the medial surface. It forms the **anterior boundary of the
    precuneus** and the **posterior boundary of the paracentral lobule**.
    On the **right** side, the marginal sulcus is **more frequently a
    single continuous sulcus (69%)** than on the left (31%), where a
    double pattern is more common (68%) .

**Sulci that are NOT wired in this package** — the sulcal partition of the
parietal lobe is **incomplete** in this tree, and consumers must know which
sulci are missing. **This omission is identical to the left hemisphere:**

*   **Central sulcus** — the **anterior boundary of the parietal lobe** and
    the boundary between the precentral and postcentral gyri. It is
    **shared with the frontal lobe** and is not wired under the parietal
    ``sulci/`` container.
*   **Parieto-occipital sulcus** — the **posterior boundary of the parietal
    lobe** and the boundary between the precuneus and the cuneus. It is
    **shared with the occipital lobe** and is not wired here.
*   **Subparietal sulcus** — the **inferior boundary of the precuneus** on
    the medial surface. It is a **parietal-only sulcus** that is
    **structurally omitted** from this tree.
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
The right parietal lobe is the **second region in the brainparts tree**
(after the left) with **all four** organizing principles wired:

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
    lobule) from BA39/BA40 (inferior parietal lobule). On the **right**,
    it is the principal node of the **right-lateralized spatial-attention
    network**.
*   ``postcentral_sulcus`` **separates** BA1/BA2 (postcentral gyrus) from
    BA5 (superior parietal lobule). It is the **structural landmark** for
    the S1 → PPC transition.
*   ``marginal_sulcus`` **separates** the paracentral lobule (medial S1/M1)
    from the precuneus (medial BA7). It is the **medial-surface landmark**
    for the sensory-to-DMN transition.

**The sulcal partition is the "negative space" of the gyral partition.**
Every gyrus in ``gyri/`` is bounded by one or more of the sulci in
``sulci/`` (or by sulci not wired here). The two partitions are best
consumed together.

Function in the Human Brain
---------------------------
The sulcal partition is **structural, not functional**, so it does not have
a "function" in the sense that S1, S2, and PPC do. However, each sulcus in
this package is a **functional landmark** for a distinct set of processes,
and on the **right** side the functional relevance of these landmarks is
**amplified by the right-lateralization of spatial attention**:

*   **``intraparietal_sulcus``** — the principal anatomical landmark for the
    **dorsal attention network**, which is **bilaterally organized but
    right-dominant for spatial reorienting and target detection**
    . The **right IPS** is causally involved in **street-crossing
    decisions** and **time-to-collision / distance estimation**
    , and it is a core node of the **right-lateralized ventral attention
    system** alongside the right temporoparietal junction (TPJ)
    . It supports **visually guided reaching, grasping, saccades, spatial
    attention, and multisensory spatial integration**.
*   **``postcentral_sulcus``** — the structural landmark for the **S1 →
    PPC transition**. Marks the boundary between the **unimodal
    somatosensory** postcentral gyrus and the **unimodal-to-polymodal**
    association cortex of the superior parietal lobule. On the **right**,
    the anterior shift of the postcentral sulcus and the greater depth of
    the central sulcus contribute to the **structural asymmetry of the
    sensorimotor strip** that parallels the **leftward asymmetry of the
    primary motor cortex** .
*   **``marginal_sulcus``** — the medial-surface landmark for the
    **sensory-to-DMN transition**. Separates the **medial S1/M1** of the
    paracentral lobule (sensorimotor) from the **medial BA7** of the
    precuneus (default mode network). On the **right**, the more frequent
    **single continuous** marginal sulcus may produce a slightly different
    cortical folding pattern in the precuneus, though its functional
    significance is not established .

Lateralization Notes
--------------------
This is the **right** sulcal aggregator. The sulcal partition is **symmetric
by name** — both left and right parietal lobes have an intraparietal sulcus,
a postcentral sulcus, and a marginal sulcus — but the **morphological
properties** of these sulci are **asymmetric**, and the right-specific
asymmetries are documented here:

*   **``intraparietal_sulcus``** — the **right** IPS is typically **deeper
    and more continuous** than the left. Quantitative morphometry shows
    the **posterior intraparietal sulcus is deeper on the right (6.1 mm)
    than on the left (5.0 mm)**, and the **anterior intraparietal sulcus
    is also slightly deeper on the right (5.6 mm vs. 5.4 mm)**
    . The right IPS is a core node of the **right-lateralized ventral
    attention network** and is **causally involved in spatial decisions**
    (street-crossing, time-to-collision estimation)
    .

*   **``postcentral_sulcus``** — the postcentral sulcus **shifts more
    anteriorly in the right hemisphere** than in the left, and its
    trajectory is structurally asymmetric in the majority of individuals
    . This asymmetry is associated with **Sylvian fissure and parietal
    operculum asymmetries** that complement the planum temporale
    asymmetry in right-handers . The **central sulcus** (its anterior
    neighbour) is generally **deeper and larger** in the right hemisphere
    , though this finding interacts with handedness
    .

*   **``marginal_sulcus``** — the marginal sulcus is **more frequently a
    single continuous sulcus on the right (69%)** than on the left (31%),
    whereas the **double pattern is more frequent on the left (68%)** than
    on the right (32%) . The functional significance of this
    morphological asymmetry is not established, but it contributes to the
    **individual variability of precuneus folding**.

**These morphological asymmetries are structural, not syndromic.** They
contribute to the functional lateralization of the parietal lobe (right
dominance for spatial attention; left dominance for language and praxis) but
they are not themselves syndromes. A consumer that needs the **functional**
lateralization claims should query the BA7, BA39, BA40, and PPC modules;
the sulcal partition documents **where the boundaries are** and **how they
differ morphologically between hemispheres**, not **what they do**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
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
    makes the omission explicit and greppable. **This omission is
    identical to the left hemisphere.**
*   **Structural parity with left sulci.** Left and right ``sulci``
    aggregators are **structurally identical** (same 3 sulci, same
    `MISSING_SULCI`, same `BOUNDARY_FOR_GYRUS` mapping). Only the
    **morphological asymmetry prose** differs — the right side documents
    the right IPS deeper, the right postcentral sulcus more anterior, and
    the right marginal sulcus more often single.

Usage
-----
Resolve sulci by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.cortex.parietal.sulci import (
        SULCI, MISSING_SULCI, BOUNDARY_FOR_GYRUS,
    )

    for sulcus in SULCI:
        # sulcus is a structural boundary module, not a functional region
        ...

Resolve by fully-qualified path string (used by the memory/recall layer)::

    path = (
        "telencephalon.cerebral_hemispheres.right.cortex."
        "parietal.sulci.intraparietal_sulcus"
    )

Boundary query (which sulci bound a gyrus)::

    # "What are the boundaries of the right postcentral gyrus?"
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
*   **Intraparietal sulcus depth asymmetry:** Table 1, *PMC6675292*. The
    **posterior intraparietal sulcus is deeper on the right (6.1 mm) than
    on the left (5.0 mm)**; the **anterior intraparietal sulcus is also
    deeper on the right (5.6 mm vs. 5.4 mm)** .
*   **Right IPS causal role in spatial decisions:** *The results showed
    that the right intraparietal sulcus was causally involved in the
    street-crossing decision* (hal.science). The right IPS plays a role in
    time-to-collision and distance estimation .
*   **Right-lateralized ventral attention network:** *Processing of
    bilateral versus unilateral conditions: Evidence for the functional
    contribution of the ventral attention network* (2015), *ScienceDirect*.
    The **right-lateralized ventral attention system** includes the
    **temporoparietal junction (TPJ)** and ventral frontal cortex
    .
*   **Right hemisphere dominance for spatial attention:** *Right hemisphere
    dominance during spatial selective attention and target detection
    occurs outside the dorsal fronto-parietal network* (2010), *PMC*.
    Right-lateralized activity for shifts of attention to unattended
    targets .
*   **Postcentral sulcus anterior shift in right hemisphere:** *Postcentral
    Gyrus* (ScienceDirect). The trajectory of the postcentral sulcus
    **shifts more anteriorly in the right hemisphere** than in the left;
    the central sulcus is generally **deeper and larger** in the right
    hemisphere .
*   **Marginal sulcus single vs. double pattern:** *(1999) found a single
    sulcus more frequently on the right (69%) than on the left (31%)
    hemispheres, whereas the double pattern was more frequent on the left
    (68%) than right (32%)* (Frontiers). This documents the right-specific
    morphological pattern of the marginal sulcus .
*   Mai, J.K., Majtanik, M., Paxinos, G. (2016). *Atlas of the Human Brain*,
    4th ed. (Sulcal and gyral landmarks.)
*   NeuroNames — Parietal sulci (right); FMA — right parietal lobe
    partonomy.
"""