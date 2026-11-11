"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia
======================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_ganglia   <-- THIS MODULE
                    ├── globus_pallidus
                    │   └── ventral_pallidum
                    └── striatum
                        ├── dorsal_striatum
                        │   ├── caudate_nucleus
                        │   └── putamen
                        └── ventral_striatum
                            ├── nucleus_accumbens
                            └── olfactory_tubercle

**Primary synonym:** Basal ganglia; basal nuclei (the preferred
clinical term — "ganglia" is a misnomer, since these are **nuclei**,
not peripheral ganglia); corpus striatum (classical — partial).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container node** — the parent of two basal ganglia children
(``globus_pallidus``, ``striatum``) and **five** grandchildren and
great-grandchildren.
**Part of:** The **telencephalic subcortical grey matter** — the
**dorsal/lateral** component of the subcortical container.
**Structural parent:** ``.../right/subcortical/`` → **direct child** of
the subcortical container.
**Structural children (two, closed set):**
``globus_pallidus`` (with child ``ventral_pallidum``) and ``striatum``
(with children ``dorsal_striatum`` → ``caudate_nucleus``,
``putamen``; ``ventral_striatum`` → ``nucleus_accumbens``,
``olfactory_tubercle``).
**Boundary status (not basal forebrain):** **Boundary case — the
basal ganglia is the dorsal/lateral complement of the basal forebrain,
not a part of it.** The **basal forebrain** (``basal_forebrain/``)
is the **medial/ventral** grey-matter region: nucleus basalis,
diagonal band, septal nuclei, substantia innominata, anterior
perforated substance, lamina terminalis. The **basal ganglia** is
the **dorsal/lateral** grey-matter group: striatum (caudate,
putamen, nucleus accumbens, olfactory tubercle) and globus pallidus
(with ventral pallidum). They are **siblings** under
``subcortical/``, **not** parent/child. Classical anatomy sometimes
conflates them as "basal ganglia" broadly, but the tree **splits**
them. Consumers that need the **medial/ventral** region must resolve
the basal forebrain; consumers that need the **dorsal/lateral**
region must resolve the basal ganglia.
**Boundary status (not diencephalon):** **Boundary case — the basal
ganglia is telencephalic, but the globus pallidus has diencephalic
embryology in some classifications.** Classical embryology treats the
**globus pallidus** (especially the **external segment**) as
**diencephalic** in origin, while the **striatum** is **telencephalic**.
The tree groups them under the **basal ganglia** (a **clinical and
functional** grouping), not by **embryological origin**. This is a
**deliberate boundary choice** — consumers must not treat the basal
ganglia as a **single embryological** entity. The **globus pallidus**
is a **basal ganglia** child, not a diencephalic child, despite its
embryology.
**Boundary status (not extended amygdala — classificatory overlap via
ventral pallidum/nucleus accumbens):** **Boundary case — the
extended amygdala shares the nucleus accumbens (ventral striatum) and
ventral pallidum with the basal ganglia, but the tree wires them
under the basal ganglia, not the extended amygdala.** The
**extended amygdala** (``.../extended_amygdala/``) is a **limbic
continuum** including the **bed nucleus of the stria terminalis
(BNST)**, the **central amygdaloid nucleus**, and (in the **SLEA
classification**) the **sublenticular extended amygdala (SLEA)**, which
includes the **ventral pallidum** and parts of the **nucleus
accumbens**. The tree **splits** these: the **nucleus accumbens**
is under ``ventral_striatum/``, and the **ventral pallidum** is under
``globus_pallidus/`` — **not** under the extended amygdala. This is a
**deliberate boundary choice**. Consumers that need the **extended
amygdala** as a unit must **union** ``.../extended_amygdala/`` with
the **ventral striatum** and **ventral pallidum** (among others).
**Boundary status (not a single functional system):** **Boundary
case — the basal ganglia is a structural grouping of functionally
distinct nuclei, not a single functional system.** The two children
have **different functions**:
*   ``striatum`` — the **input** structure of the basal ganglia.
    The **dorsal striatum** (caudate, putamen) is involved in
    **motor control, action selection, and habit learning**; the
    **ventral striatum** (nucleus accumbens, olfactory tubercle) is
    involved in **reward, motivation, and addiction**.
*   ``globus_pallidus`` — the **output** structure of the basal
    ganglia. The **dorsal** globus pallidus is involved in **motor
    output**; the **ventral pallidum** is involved in **reward and
    motivation** (with the ventral striatum).
Consumers must not treat "basal ganglia" as a single functional
system — it is a **structural grouping** of input and output nuclei,
dorsal and ventral subsystems.
**Boundary status (the olfactory tubercle is HERE — the fifth
rhinencephalon-excluded structure):** **Boundary case — the
olfactory tubercle is a CHILD of `striatum/ventral_striatum/`, not of
the rhinencephalon or the basal forebrain.** The **olfactory
tubercle** — a **primary olfactory cortical target** on the **anterior
perforated substance** — is classically rhinencephalic. The tree
**excludes** it from the rhinencephalon and places it **here**, under
the **ventral striatum** (because of its **striatal-like
cytoarchitecture**). This is the **fifth and final** rhinencephalon-
excluded structure. Consumers reconstructing the **classical full
rhinencephalon** must **union** the rhinencephalon with the **basal
ganglia** (specifically, the olfactory tubercle).
**Boundary status (the nucleus accumbens is HERE):** **Boundary case
— the nucleus accumbens is a CHILD of `striatum/ventral_striatum/`,
not of the basal forebrain.** The **nucleus accumbens** — the
**ventral striatum's primary reward nucleus** — is classically grouped
with the basal forebrain in some literature. The tree places it
**here**, under the **ventral striatum**. Consumers that need the
nucleus accumbens must resolve it through the basal ganglia, not
through the basal forebrain.
**Boundary status (not the midbrain — substantia nigra is a
midbrain sibling):** **Boundary case — the substantia nigra is
FUNCTIONALLY related to the basal ganglia (dopaminergic input to the
striatum) but STRUCTURALLY separate (midbrain).** The **substantia
nigra** — the **dopaminergic nucleus** that projects to the striatum
— is under ``.../midbrain/tegmentum/substantia_nigra/``, **not**
under the basal ganglia. The **striatum** receives **dopaminergic
input** from the substantia nigra (pars compacta), but the substantia
nigra itself is a **midbrain** structure, not a **basal ganglia**
child. Consumers must not resolve the substantia nigra through the
basal ganglia, and must not treat the basal ganglia's dopaminergic
input as intrinsic to the basal ganglia.
**Boundary status (deep, multi-level container):** **Boundary case —
a deep, multi-level container, up to FOUR levels deep.** The basal
ganglia's deepest branch is
``basal_ganglia/striatum/dorsal_striatum/caudate_nucleus/`` (four
levels from the subcortical container). Consumers iterating the basal
ganglia must be prepared to **recurse**, not just iterate one level.

Overview
--------
The basal ganglia is the **dorsal/lateral complement of the basal
forebrain** — a **structural grouping** of deep grey-matter nuclei
that are involved in **motor control, action selection, habit
learning, reward, and motivation**. It contains **two children**
(``globus_pallidus`` and ``striatum``), which together form the
**input-output circuit** of the basal ganglia:

*   **``striatum``** — the **input** structure. It receives
    **cortical**, **thalamic**, and **dopaminergic** (substantia
    nigra) input, and it projects to the globus pallidus and
    substantia nigra. Its **dorsal** component (caudate, putamen) is
    **motor/cognitive/associative**; its **ventral** component
    (nucleus accumbens, olfactory tubercle) is **limbic/reward/
    olfactory**.

*   **``globus_pallidus``** — the **output** structure. It receives
    striatal input and projects to the **thalamus** (via the
    **ansa lenticularis** and **lenticular fasciculus**) and the
    **subthalamic nucleus**. Its **dorsal** component is
    **motor**; its **ventral** component (ventral pallidum) is
    **limbic/reward**.

**The basal ganglia is the "action selection" system.** Its
**cortico-striato-pallido-thalamo-cortical** loop is the substrate
for **action selection, motor learning, and habit formation**. Its
**dysfunction** produces the **hypokinetic** (Parkinson's) and
**hyperkinetic** (Huntington's, dystonia) movement disorders that are
the **signature clinical associations** of the basal ganglia.

**The basal ganglia is NOT a single functional system.** Its
**dorsal** (motor) and **ventral** (limbic) subsystems have
**different functions** and **different clinical associations**:
*   **Dorsal striatum and globus pallidus** — **motor and cognitive**
    (Parkinson's, Huntington's, dystonia).
*   **Ventral striatum and ventral pallidum** — **reward, motivation,
    and addiction** (addiction, depression, OCD).

Consumers must **not** treat "basal ganglia" as a single functional
system — it is a **structural grouping** of **dorsal and ventral**
subsystems.

**The basal ganglia contains the olfactory tubercle and the nucleus
accumbens.** The **olfactory tubercle** — the **fifth and final
rhinencephalon-excluded structure** — and the **nucleus accumbens** —
the **primary reward nucleus of the ventral striatum** — are **both**
under ``striatum/ventral_striatum/``. They are **classically grouped**
with the rhinencephalon (tubercle) and the basal forebrain (accumbens),
but the tree places them **here**, under the **basal ganglia**.
Consumers reconstructing the **classical full rhinencephalon** must
**union** the rhinencephalon with the **basal ganglia** (specifically,
the olfactory tubercle); consumers reconstructing the **basal
forebrain** must **union** it with the **basal ganglia** (for the
nucleus accumbens, if needed).

**The basal ganglia is a paired structure.** Each hemisphere has its
own basal ganglia, with **ipsilateral** cortical and thalamic
connections. The two sides are **bilaterally symmetric** and
**largely non-lateralized** — the dorsal striatum's motor functions
and the ventral striatum's reward functions are **bilateral**. Some
**subtle lateralization** has been reported (left caudate for
language, right caudate for spatial), but it is **weak** and **not a
strong classification basis**. See *Lateralization Notes*.

Container Contents (two children, closed set)
----------------------------------------------
The basal ganglia container has **exactly two children**:

*   **``globus_pallidus``** — the **output** structure of the basal
    ganglia. **Children:** ``ventral_pallidum``. **Depth: two
    levels.** The **dorsal** globus pallidus (external + internal
    segments) is **motor**; the **ventral pallidum** is
    **limbic/reward**. Note: the tree dump shows ``ventral_pallidum``
    under ``globus_pallidus/``, but the **dorsal** segments (external
    and internal globus pallidus) are **not wired** as separate
    children — a **documented structural gap** at this level.

*   **``striatum``** — the **input** structure of the basal ganglia.
    **Children:** ``dorsal_striatum`` (→ ``caudate_nucleus``,
    ``putamen``) and ``ventral_striatum`` (→ ``nucleus_accumbens``,
    ``olfactory_tubercle``). **Depth: four levels** (deepest branch
    in the subcortical tree: ``basal_ganglia/striatum/dorsal_striatum/
    caudate_nucleus/``). The **dorsal** striatum is **motor/
    cognitive**; the **ventral** striatum is **limbic/reward/
    olfactory**.

**Not children (deliberately excluded):**
*   **Substantia nigra** — under ``.../midbrain/tegmentum/substantia_nigra/``
    (**midbrain**, not basal ganglia). Functionally related
    (dopaminergic input to striatum) but structurally separate.
*   **Subthalamic nucleus** — under
    ``.../diencephalon/subthalamus/subthalamic_nucleus/``
    (**diencephalon**, not basal ganglia). Functionally related
    (part of the basal ganglia circuit) but structurally separate.
*   **Ventral tegmental area (VTA)** — under
    ``.../midbrain/tegmentum/ventral_tegmental_area/`` (**midbrain**,
    not basal ganglia). Functionally related (dopaminergic input to
    ventral striatum) but structurally separate.
*   **Extended amygdala** — under ``.../extended_amygdala/``
    (**sibling** of the basal forebrain, not a child of the basal
    ganglia). The ventral pallidum and nucleus accumbens are
    **classificatory overlaps** with the extended amygdala, but the
    tree **splits** them.

The Basal Ganglia / Basal Forebrain Boundary
--------------------------------------------
This is the **most consequential boundary** for consumers building a
"subcortical" registry:

*   **Basal ganglia** (this module) — **dorsal/lateral** grey matter:
    striatum (caudate, putamen, nucleus accumbens, olfactory tubercle)
    and globus pallidus (dorsal segments + ventral pallidum).

*   **Basal forebrain** (``basal_forebrain/``) — **medial/ventral**
    grey matter: nucleus basalis, diagonal band, septal nuclei,
    substantia innominata, anterior perforated substance, lamina
    terminalis.

**They are siblings under `subcortical/`.** Consumers that need the
**medial/ventral** region must resolve the **basal forebrain**;
consumers that need the **dorsal/lateral** region must resolve the
**basal ganglia**. The **olfactory tubercle** and **nucleus
accumbens** are the **two structures** that are **classically
grouped** with the **basal forebrain** but are **wired here** under
the **basal ganglia** — a deliberate boundary choice reflecting their
**striatal-like cytoarchitecture**.

The Basal Ganglia / Rhinencephalon Boundary
-------------------------------------------
The basal ganglia contains the **fifth and final rhinencephalon-
excluded structure** — the **olfactory tubercle**:

| Rhinencephalon-excluded structure | Tree location |
|---|---|
| Amygdala | `subcortical/medial_temporal_lobe/amygdala/` |
| Hippocampus | `subcortical/medial_temporal_lobe/hippocampus/` |
| Septal nuclei | `subcortical/basal_forebrain/septal_nuclei/` |
| Anterior perforated substance | `subcortical/basal_forebrain/anterior_perforated_substance/` |
| **Olfactory tubercle** | **`subcortical/basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/`** |

**Consumers reconstructing the classical full rhinencephalon** must
union the rhinencephalon with **all five** excluded structures — four
of which are documented in the basal forebrain or medial temporal
lobe, and **one** of which is **here**, in the basal ganglia.

The Basal Ganglia / Extended Amygdala Boundary
----------------------------------------------
This is the **most contested classification** for consumers:

*   **Extended amygdala** (``.../extended_amygdala/``) — the **BNST**,
    the **central amygdaloid nucleus**, and (in the SLEA
    classification) the **ventral pallidum** and parts of the
    **nucleus accumbens**.

*   **Basal ganglia** (this module) — the **ventral striatum** and
    **ventral pallidum** are **wired here**, not under the extended
    amygdala.

**The tree splits them.** The **nucleus accumbens** is under
``ventral_striatum/``, and the **ventral pallidum** is under
``globus_pallidus/`` — **not** under the extended amygdala. This is
a **deliberate boundary choice**. Consumers that need the **extended
amygdala** as a unit (per the SLEA classification) must **union**
``.../extended_amygdala/`` with the **ventral striatum** and
**ventral pallidum** — the tree does **not** provide this union as a
single path.

The Basal Ganglia / Diencephalon Boundary
-----------------------------------------
The basal ganglia is **telencephalic**, but the **globus pallidus**
has **diencephalic embryology** in some classifications:

*   **Striatum** — **telencephalic** embryology (classical).
*   **Globus pallidus** — **diencephalic** embryology (classical;
    especially the external segment).

**The tree groups them under the basal ganglia** (a **clinical and
functional** grouping), not by **embryological origin**. This is a
**deliberate boundary choice**. Consumers must not treat the basal
ganglia as a **single embryological** entity — the globus pallidus is
**diencephalic** in origin but **basal ganglia** in the tree.

The Basal Ganglia / Midbrain Boundary
-------------------------------------
The substantia nigra is **functionally related** to the basal ganglia
(dopaminergic input to the striatum) but **structurally separate**:

*   **Substantia nigra** — under ``.../midbrain/tegmentum/substantia_nigra/``
    (**midbrain**, not basal ganglia).
*   **Ventral tegmental area (VTA)** — under
    ``.../midbrain/tegmentum/ventral_tegmental_area/`` (**midbrain**,
    not basal ganglia).

**Consumers must not resolve the substantia nigra or VTA through the
basal ganglia.** They are **dopaminergic inputs** to the basal
ganglia, not **children** of it. The basal ganglia's
**cortico-striato-pallido-thalamo-cortical** loop is **modulated** by
the substantia nigra and VTA, but those are **midbrain** structures,
not **basal ganglia** components.

Function in the Human Brain
---------------------------
The basal ganglia container has **no single function** — it is a
**structural grouping** of functionally distinct children:

*   **``striatum``** — **motor control, action selection, habit
    learning** (dorsal); **reward, motivation, addiction** (ventral).
*   **``globus_pallidus``** — **motor output** (dorsal); **reward
    and motivation** (ventral).

**The unifying theme:** the basal ganglia is the **action selection
system** — a **cortico-striato-pallido-thalamo-cortical** loop that
**selects and invigorates actions** and **learns habits**. Its
**dorsal** subsystem is **motor**, its **ventral** subsystem is
**limbic/reward**. Consumers must read each child's own module for
detailed functions.

Associated Disorders
--------------------
The basal ganglia container has **no single syndrome** — its children's
disorders are documented in their own modules:

*   **Dorsal striatum and globus pallidus** — **Parkinson's disease**
    (substantia nigra → dorsal striatum dopaminergic loss),
    **Huntington's disease** (dorsal striatum degeneration),
    **dystonia** (basal ganglia dysfunction), **hemiballismus**
    (subthalamic nucleus), **chorea** (dorsal striatum).
*   **Ventral striatum and ventral pallidum** — **addiction**
    (nucleus accumbens), **depression** (ventral pallidum/nucleus
    accumbens), **OCD** (ventral striatum), **Kluver-Bucy syndrome**
    (amygdala — not basal ganglia, contrast), **olfactory dysfunction**
    (olfactory tubercle).
*   **Container-level** — **no single syndrome** — the basal ganglia
    container is a **structural grouping**, and its disorders are the
    **aggregate** of its children's disorders.

**What is NOT here:** The basal ganglia is **not** the substrate for
**Alzheimer's disease** (nucleus basalis — basal forebrain), **basal
forebrain amnesia** (septum/DBB), **Kluver-Bucy syndrome** (amygdala
— medial temporal lobe), or **temporal lobe epilepsy** (hippocampus).
Its clinical footprint is **motor** (dorsal) and **reward/addiction**
(ventral) — a **distinct category** from the basal forebrain's
**cholinergic-cognitive** footprint.

Lateralization Notes
--------------------
This is the **right** basal ganglia container. Its **two children**
are **not uniformly lateralized**:

*   **Bilateral (presumed):** ``globus_pallidus``,
    ``ventral_pallidum``, ``nucleus_accumbens``, ``olfactory_tubercle``
    — structurally symmetric, no strong functional lateralization
    established.

*   **Weak lateralization (contested):** The **dorsal striatum**
    (caudate, putamen) has been reported to show **subtle**
    lateralization — **left caudate** for **language** (via the
    cortico-striatal loop), **right caudate** for **spatial
    navigation**. This is **weak** and **contested**, and it is
    documented in the **striatum** module (if written separately),
    not in this container. **On the right side**, the **right
    caudate's spatial-memory association** is the weaker of the two
    lateralization claims — it is **not** a strong basis for
    container-level classification.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the basal ganglia container has **no documented
    strong left-lateralized or right-lateralized function**.
    **Parkinson's** dorsal striatal dopaminergic loss is
    **bilateral** (though often **asymmetric** in presentation);
    **Huntington's** is **bilateral**; **addiction** is
    **bilateral** in the ventral striatum.

*   **Extended Amygdala Overlap (Deferred Warning):** The **ventral
    pallidum** and **nucleus accumbens** have **classificatory
    overlap** with the extended amygdala (SLEA), but this is a
    **grandchild-level** concern, not a **container-level** one.
    **Any amygdala-lateralization warning belongs to the ventral
    pallidum or nucleus accumbens modules** (if written separately),
    **not** to the basal ganglia container. **This is especially
    important for this right-side module** — the right ventral
    pallidum and right nucleus accumbens are **downstream of** the
    container, and the right amygdala's fear association belongs to
    the **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module**, **not** to the container that contains the
    right ventral pallidum and right nucleus accumbens. The container
    itself carries **no warning**.

**A consumer that assumes "right basal ganglia = left basal ganglia"
will be broadly correct** — the two sides are **largely symmetric**,
no **strong** lateralized syndrome has been demonstrated, and the
**weak** lateralization reported for the dorsal striatum is
**contested**, not a strong classification basis. The basal ganglia
container is a **strict-mirror pair with no warning** — matching the
**basal forebrain container**, because the container itself has **no
direct amygdala connection** (the amygdala is under
``medial_temporal_lobe/``, a sibling) and **no extended-amygdala
overlap at the container level** (the overlap is via grandchildren).
**The right-side module keeps the warning deferred to the child
modules**, matching the deferred-warning pattern — no dedicated Usage
block, no emphatic contrast reference, only a **deferral note** in the
Lateralization section.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../diencephalon/``, ``.../extended_amygdala/``,
    or any other container. The basal ganglia's relationships to the
    substantia nigra, subthalamic nucleus, VTA, and extended amygdala
    are documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — two children, closed set.** The basal ganglia
    container has exactly two children: ``globus_pallidus`` and
    ``striatum``. Consumers may iterate them, but should not assume
    any others exist.
*   **Deep, multi-level container — prepared to recurse.** The basal
    ganglia's deepest branch is
    ``basal_ganglia/striatum/dorsal_striatum/caudate_nucleus/`` (four
    levels from the subcortical container). Consumers must be prepared
    to **recurse**, not just iterate one level.
*   **Dorsal/lateral complement of the basal forebrain.** The basal
    ganglia is the **dorsal/lateral** grey matter; the basal forebrain
    is the **medial/ventral** grey matter. They are **siblings** under
    ``subcortical/``, **not** parent/child.
*   **The olfactory tubercle is HERE — the fifth rhinencephalon-
    excluded structure.** Consumers reconstructing the **classical
    full rhinencephalon** must **union** the rhinencephalon with the
    basal ganglia (specifically, the olfactory tubercle).
*   **The nucleus accumbens is HERE.** Consumers that need the
    nucleus accumbens must resolve it through the basal ganglia, not
    through the basal forebrain.
*   **Globus pallidus has diencephalic embryology in some
    classifications.** The tree groups it under the basal ganglia (a
    clinical/functional grouping), not by embryological origin.
    Consumers must not treat the basal ganglia as a single
    embryological entity.
*   **Extended amygdala overlap via ventral pallidum/nucleus
    accumbens — deferred to child modules.** The SLEA classification
    groups the ventral pallidum and parts of the nucleus accumbens
    with the extended amygdala, but the tree **splits** them. Any
    amygdala-lateralization warning belongs to the **ventral
    pallidum or nucleus accumbens modules**, not to this container.
    **The right-side module keeps the warning deferred** — no
    container-level warning, only a **deferral note** in the
    Lateralization section, matching the deferred-warning pattern.
*   **Not a single functional system.** The dorsal (motor) and
    ventral (limbic/reward) subsystems are functionally distinct.
    Consumers must not treat "basal ganglia" as a single functional
    system.
*   **Not the substantia nigra — midbrain sibling.** The substantia
    nigra is functionally related (dopaminergic input to striatum) but
    structurally separate (midbrain). Do not resolve it through the
    basal ganglia.
*   **No ``AREA_PATHS`` hop.** The basal ganglia is a local container
    under the subcortical container, not a cross-listed leaf.
*   **No nested cross-listing.** The basal ganglia has no nested
    dual-framing module. It is a single container.
*   **Structural parity with left basal ganglia — strict mirror
    with no warning.** Right and left basal ganglia modules are
    **structurally identical** — same two children, same deep
    recursion, same olfactory-tubercle redirect, same
    extended-amygdala classificatory-overlap note, same
    substantia-nigra boundary. **The container has no direct amygdala
    connection**, so the warning is **deferred to child modules**.
    **The right-side module keeps the deferral note** — no dedicated
    Usage block, no contrast reference — matching the deferred-warning
    pattern established by this pair.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical import basal_ganglia

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_ganglia"
    )

**Do not** assume the basal ganglia is under ``basal_forebrain/``. It
is a **sibling** under ``subcortical/``. A consumer that iterates the
basal forebrain and expects to find the striatum or globus pallidus
there will **miss them**.

**Do not** assume the basal ganglia is a **flat container**. It is a
**deep, multi-level tree** (up to four levels). Consumers must be
prepared to **recurse**.

**Do not** assume the basal ganglia **contains** the substantia
nigra, subthalamic nucleus, or VTA. Those are **midbrain or
diencephalic** structures, not basal ganglia children.

**Do not** assume the basal ganglia **contains** the extended amygdala.
The ventral pallidum and nucleus accumbens are **classificatory
overlaps** with the extended amygdala (SLEA), but the tree **splits**
them.

**Do not** assume the basal ganglia is a **single functional system**.
Its **dorsal** (motor) and **ventral** (limbic/reward) subsystems are
functionally distinct.

**Do not** import **amygdala-lateralization claims** into the basal
ganglia container. The container has **no direct amygdala connection**
— the amygdala is under ``medial_temporal_lobe/``, a sibling — and the
extended-amygdala overlap is **deferred to the ventral pallidum and
nucleus accumbens modules**. **This is especially important for this
right-side module** — the right ventral pallidum and right nucleus
accumbens are **downstream of** the container, and the right amygdala's
fear association belongs to the **amygdala module** and (weakly via
SLEA) to the **extended amygdala module**, **not** to the container.

Iterating the basal ganglia's two children (recommended consumer
pattern)::

    BASAL_GANGLIA_CHILDREN = (
        "globus_pallidus",
        "striatum",
    )
    # Closed set. Do not assume additional children.

Recursive iteration over the basal ganglia tree (recommended
consumer pattern)::

    # The basal ganglia is up to four levels deep. Recurse over it
    # rather than iterating one level.
    #
    #   subcortical.basal_ganglia.striatum.dorsal_striatum.caudate_nucleus
    #
    # is a valid leaf; so is
    #
    #   subcortical.basal_ganglia.striatum.ventral_striatum.olfactory_tubercle
    #
    # Do not stop at the first level.

Reconstructing the classical full rhinencephalon (recommended
consumer pattern — the olfactory tubercle is the fifth and final
excluded structure)::

    # The rhinencephalon's narrow definition excludes five
    # structures that classical anatomy includes. The full union:
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",  # THIS MODULE
        ),
    }
    # The olfactory tubercle is the ONLY rhinencephalon-excluded
    # structure wired under the basal ganglia (not the basal forebrain
    # or the medial temporal lobe).

Reconstructing the classical "basal ganglia + basal forebrain"
(recommended consumer pattern)::

    # Classical anatomy sometimes treats "basal ganglia" broadly as
    # including both the dorsal/lateral and medial/ventral regions.
    # The tree splits them. Consumers that want the broad grouping
    # must union:
    BROAD_BASAL_GANGLIA_PLUS_FOREBRAIN = {
        "subcortical.basal_ganglia": (
            "globus_pallidus",
            "striatum",
        ),
        "subcortical.basal_forebrain": (
            "anterior_perforated_substance",
            "diagonal_band_of_broca",
            "lamina_terminalis",
            "nucleus_basalis",
            "septal_nuclei",
            "substantia_innominata",
        ),
    }

Reaching the extended amygdala's ventral-pallidum/nucleus-accumbens
components (recommended consumer pattern)::

    # The extended amygdala's SLEA classification includes the
    # ventral pallidum and parts of the nucleus accumbens. The tree
    # splits them. Consumers that need the SLEA grouping must union:
    #
    #   subcortical.extended_amygdala
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The tree does not provide this union as a single path.

Reaching the substantia nigra (recommended consumer pattern — NOTE
the midbrain boundary)::

    # The substantia nigra is FUNCTIONALLY related to the basal
    # ganglia (dopaminergic input to the striatum) but STRUCTURALLY
    # separate (midbrain):
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # Do NOT resolve substantia nigra through the basal ganglia.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        bg_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia"
        )
        # resolve bg_path through the memory/recall layer

References
----------
*   **Canonical basal ganglia anatomy:** Graybiel, A.M. (2008).
    "Habits, rituals, and the evaluative brain." *Annual Review of
    Neuroscience* 31:359–387. (Definitive functional overview;
    cortico-striato-pallido-thalamo-cortical loop.)
*   **Basal ganglia (textbook):** Standaert, D.G., Young, A.B.
    (2015). "Treatment of central nervous system degenerative
    disorders." In *Goodman & Gilman's Pharmacological Basis of
    Therapeutics*, 12th ed. (Basal ganglia disorders; Parkinson's,
    Huntington's.)
*   **Striatal anatomy:** Haber, S.N. (2011). "Neuroanatomy of
    reward: the ventral striatum and the extended amygdala." In
    *Neurobiology of Sensation and Reward* (Gottfried, J.A., ed.).
    (Ventral striatum; nucleus accumbens; extended amygdala overlap.)
*   **Dorsal vs ventral striatum:** Voorn, P., Vanderschuren, L.J.,
    Groenewegen, H.J., Robbins, T.W., Pennartz, C.M. (2004). "Putting
    a spin on the dorsal-ventral divide of the striatum." *Trends in
    Neurosciences* 27:468–474. (Dorsal/ventral functional distinction.)
*   **Olfactory tubercle:** Heimer, L., Wilson, R.D. (1975). "The
    subcortical projections of the allocortex: similarities in the
    neural associations of the hippocampus, the piriform cortex, and
    the neocortex." In *Golgi Centennial Symposium* (Santini, M.,
    ed.). (Olfactory tubercle as a ventral striatum structure.)
*   **Nucleus accumbens:** Mogenson, G.J., Jones, D.L., Yim, C.Y.
    (1980). "From motivation to action: functional interface between
    the limbic system and the motor system." *Progress in
    Neurobiology* 14:69–97. (Nucleus accumbens as limbic-motor
    interface; ventral striatum.)
*   **Substantia nigra (contrast):** Braak, H., et al. (2003).
    "Staging of brain pathology related to sporadic Parkinson's
    disease." *Neurobiology of Aging* 24:197–211. (Substantia nigra
    pathology in Parkinson's; the substantia nigra is a **midbrain**
    structure, not a basal ganglia child.)
*   **Globus pallidus embryology:** Alvarez-Bolado, G., Paul, F.A.,
    Blaess, S. (2018). "Sonic hedgehog lineage in the mouse
    hypothalamus." *Frontiers in Neuroanatomy* 12:83. (Globus
    pallidus diencephalic origin; striatum telencephalic origin.)
*   **Extended amygdala / SLEA:** Alheid, G.F., Heimer, L. (1988).
    "New perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA; ventral pallidum; extended amygdala continuum.)
*   **Dorsal striatum lateralization:** Ullman, M.T. (2004).
    "Contributions of memory circuits to language: the
    declarative/procedural model." *Cognition* 92:231–270. (Left
    caudate in language; procedural memory.)
*   **Right caudate spatial memory (contrast):** Postle, B.R.,
    D'Esposito, M. (1999). "Dissociation of human caudate nucleus
    activity during spatial and verbal working memory." *Cognitive
    Brain Research* 7:571–580. (Right caudate and spatial working
    memory; weak, contested lateralization — contrast reference,
    **not** a strong basis for container-level classification.)
*   **Addiction:** Koob, G.F., Volkow, N.D. (2010). "Neurocircuitry
    of addiction." *Neuropsychopharmacology* 35:217–238. (Ventral
    striatum and ventral pallidum in addiction.)
*   **Huntington's disease:** Vonsattel, J.P., DiFiglia, M. (1998).
    "Huntington disease." *Journal of Neuropathology and Experimental
    Neurology* 57:369–384. (Dorsal striatum degeneration.)
*   **Parkinson's disease:** Dauer, W., Przedborski, S. (2003).
    "Parkinson's disease: mechanisms and models." *Neuron*
    39:889–909. (Substantia nigra → dorsal striatum dopaminergic
    loss.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this container):** Morris, J.S., Öhman, A., Dolan, R.J. (1998).
    "A subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the basal ganglia container —
    the container has **no direct amygdala connection**, and the
    extended-amygdala overlap is **deferred to the ventral pallidum
    and nucleus accumbens modules**.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Basal ganglia in overview.)
*   NeuroNames — Basal ganglia (right); FMA — Basal ganglia (right
    member).
"""