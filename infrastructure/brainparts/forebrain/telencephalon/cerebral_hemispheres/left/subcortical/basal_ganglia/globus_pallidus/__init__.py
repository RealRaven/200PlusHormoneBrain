"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_ganglia.globus_pallidus
=====================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── basal_ganglia
                    └── globus_pallidus   <-- THIS MODULE
                        └── ventral_pallidum

**Primary synonym:** Globus pallidus (GP); pallidum; paleostriatum
(classical); globus pallidus (dorsal + ventral); "the pallidum."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**GABAergic output nucleus** of the basal ganglia — the **output**
structure of the cortico-striato-pallido-thalamo-cortical loop.
**Part of:** The **basal ganglia** container — specifically, the
**output side** of the basal ganglia (with the **striatum** as the
input side).
**Structural parent:** ``.../left/subcortical/basal_ganglia/`` →
**direct child** of the basal ganglia container.
**Structural children (one wired child, closed set):**
``ventral_pallidum``.
**Boundary status (DORSAL SEGMENT GAP — the canonical GPe/GPi are NOT
wired):** **Boundary case — the tree wires only `ventral_pallidum`;
the DORSAL segments (GPe, GPi) are a DOCUMENTED GAP, not children.**
This is the **third documented structural gap** in the subcortical
tree (after the **lateral septal nucleus** gap in `septal_nuclei/`
and the **magnocellular preoptic nucleus** gap in
`substantia_innominata/`). The **globus pallidus** classically has
**three segments**:
*   **External globus pallidus (GPe)** — the **lateral** segment (also
    called the **lateral globus pallidus** in older terminology) — part
    of the **indirect pathway**, receiving striatal input and
    projecting to the **subthalamic nucleus**. **NOT wired** in the
    tree.
*   **Internal globus pallidus (GPi)** — the **medial** segment (also
    called the **medial globus pallidus** in older terminology) — the
    **main output** of the basal ganglia, projecting to the
    **thalamus** (via the **ansa lenticularis** and **lenticular
    fasciculus**) and to the **pedunculopontine nucleus**. **The
    target of pallidotomy and DBS** for Parkinson's disease and
    dystonia. **NOT wired** in the tree.
*   **Ventral pallidum (VP)** — the **ventral** segment — the
    **limbic/reward output** of the ventral striatum. **Wired** as the
    **only child** of this container.

**The dorsal segments are the CANONICAL globus pallidus** — the GPe
and GPi that are the target of **pallidotomy** and **deep brain
stimulation** for Parkinson's and dystonia. Their absence is a
**major structural gap**, not a minor omission. Consumers that need
the **dorsal globus pallidus** must resolve its functions as
**prose** in this module (see *The Globus Pallidus / Dorsal Segment
Gap*), not as structural children. Consumers that need the **ventral
pallidum** resolve the **one wired child**.
**Boundary status (not the striatum — sibling):** **Boundary case —
the striatum is a SIBLING under the basal ganglia, not a parent or
child.** The **striatum** is the **input** structure of the basal
ganglia; the **globus pallidus** is the **output** structure. They
are **structurally separate** and **functionally complementary**.
The tree wires them as **siblings** under ``.../basal_ganglia/``.
Consumers that need the **input** structure must resolve
``.../striatum/``; consumers that need the **output** structure must
resolve this module. They are **not** parent and child — they are
**two halves** of the basal ganglia circuit.
**Boundary status (not the subthalamic nucleus — diencephalic
sibling):** **Boundary case — the subthalamic nucleus (STN) is
FUNCTIONALLY related to the globus pallidus (part of the indirect
pathway) but STRUCTURALLY separate (diencephalon).** The **STN** is
under ``.../diencephalon/subthalamus/subthalamic_nucleus/`` — **not**
under the globus pallidus. The **STN** projects to the **GPi** (and
the **GPe**), and the **GPi** projects back to the **STN** via the
**subthalamic fasciculus** — they are **part of the same
cortico-striato-pallido-subthalamo-pallido-thalamo-cortical loop** —
but the **STN is a diencephalic structure**, not a globus pallidus
child. Consumers must not resolve the STN through the globus pallidus,
and must not treat the STN as intrinsic to the basal ganglia (it is
**diencephalic**, not **telencephalic**).
**Boundary status (not the substantia nigra — midbrain sibling):**
**Boundary case — the substantia nigra is FUNCTIONALLY related to the
striatum (dopaminergic input) but STRUCTURALLY separate (midbrain),
and it is NOT a globus pallidus child.** The **substantia nigra** is
under ``.../midbrain/tegmentum/substantia_nigra/`` — **not** under
the globus pallidus, and **not** under the striatum either. Its
**pars compacta** provides **dopaminergic input to the striatum**;
its **pars reticulata** is a **GABAergic output** comparable to the
**GPi**. The **globus pallidus** does **not** receive dopaminergic
input from the substantia nigra directly (the striatum does). The two
structures are **functionally related** (both are basal ganglia
outputs) but **structurally separate** (globus pallidus is
telencephalic; substantia nigra is mesencephalic).
**Boundary status (extended amygdala overlap via the ventral
pallidum — DEFERRED WARNING FROM THE BASAL GANGLIA CONTAINER):**
**Boundary case — the VENTRAL PALLIDUM (the one wired child) is part
of the sublingual extended amygdala (SLEA) in some classifications.**
The **basal ganglia container** flagged this overlap and **deferred**
the amygdala-lateralization warning to this level. The **globus
pallidus container** now carries the **light warning**: the
**ventral pallidum is a direct child** with **classificatory overlap**
with the extended amygdala (SLEA), so the warning is **less deferred**
than at the basal ganglia container level, but it is still **not
container-wide** — the **dorsal segments** (the canonical GPe/GPi,
which are **not wired**) have **no amygdala relationship**. The
**full warning** belongs to the **ventral pallidum module**, which
carries the **SLEA** relationship directly. See *The Globus Pallidus
/ Extended Amygdala Boundary* and *Lateralization Notes*.
**Boundary status (diencephalic embryology of the GPe — grouped under
the basal ganglia for clinical/functional reasons):** **Boundary
case — the EXTERNAL globus pallidus (GPe) has DIENCEPHALIC embryology
in classical classifications, but the tree groups it under the basal
ganglia.** Classical embryology treats the **GPe** as
**diencephalic** in origin (along with the hypothalamus), while the
**striatum** and **GPi** are **telencephalic**. The tree groups the
**entire globus pallidus** (dorsal + ventral) under the **basal
ganglia** — a **clinical and functional** grouping, not an
**embryological** one. This is a **deliberate boundary choice**.
Consumers must not treat the globus pallidus as a **single
embryological** entity — the **GPe** is **diencephalic** in origin,
the **GPi** is **telencephalic**, and the **ventral pallidum** is
**telencephalic** (part of the ventral striatopallidal system).
**Boundary status (the internal capsule separates the segments — white
matter, not a GP child):** **Boundary case — the internal capsule
SEPARATES the globus pallidus segments from the putamen and from each
other, but it is WHITE MATTER, not a globus pallidus child.** The
**internal capsule** (specifically, the **lateral part** — the
**external capsule** and **internal capsule** together) separates:
*   The **putamen** from the **GPe** (the **external medullary
    lamina**).
*   The **GPe** from the **GPi** (the **internal medullary lamina**).
*   The **globus pallidus** from the **thalamus** (the **internal
    capsule** proper).
The **internal capsule** is under ``.../left/white_matter/`` — **not**
a globus pallidus child. The **medullary laminae** (external and
internal) are **white-matter sheets** within the globus pallidus;
they are **prose**, not structural children.
**Boundary status (not the substantia innominata — basal forebrain
sibling, blends laterally):** **Boundary case — the substantia
innominata is a BASAL FOREBRAIN sibling, not a globus pallidus
child.** The **substantia innominata** (``.../basal_forebrain/substantia_innominata/``)
**blends laterally** into the globus pallidus (especially the **GPe**),
and the **ventral pallidum** is **embedded** in the substantia
innominata's territory. But the tree wires them as **siblings**
(globus pallidus under basal ganglia; substantia innominata under
basal forebrain). This is a **deliberate boundary choice** — the
**substantia innominata** is a **basal forebrain grey-matter region**
that **overlaps** the globus pallidus territory, but it is **not a
globus pallidus child** and the globus pallidus is **not a substantia
innominata child**.
**Boundary status (deep, output-side container):** **Boundary case —
a deep, output-side container with a DORSAL GAP and a VENTRAL CHILD.**
The globus pallidus is the **output** structure of the basal ganglia
(the striatum is the input). Its **dorsal** component is **motor
output** (not wired — a documented gap); its **ventral** component is
**limbic/reward output** (wired — the one child). The **dorsal/ventral
split** is the **functional** organizing principle of the globus
pallidus — the dorsal and ventral components have **different
functions**, **different connections**, and **different clinical
associations**.

Overview
--------
The globus pallidus is the **output** structure of the basal ganglia
— the **GABAergic** nucleus that receives striatal input and
projects to the **thalamus** (via the **ansa lenticularis** and
**lenticular fasciculus**) and the **subthalamic nucleus**. It is
the **GABAergic counterpart** to the **dopaminergic** substantia nigra
in the midbrain, and together with the striatum it forms the
**input-output circuit** of the basal ganglia:

*   **``striatum``** — the **input** structure (sibling).
*   **``globus_pallidus``** — the **output** structure (this module).

**The globus pallidus has TWO functional subsystems.** This is its
**defining structural fact**:
*   **Dorsal globus pallidus** (GPe + GPi) — **motor output**. The
    **GPe** is part of the **indirect pathway** (striatum → GPe →
    STN → GPi); the **GPi** is the **main output** of the basal
    ganglia (striatum → GPi → thalamus). **NOT wired** in the tree —
    a **documented gap**.
*   **Ventral pallidum** — **limbic/reward output**. The ventral
    pallidum receives input from the **ventral striatum** (nucleus
    accumbens, olfactory tubercle) and projects to the **mediodorsal
    thalamus**, the **lateral habenula**, and the **brainstem**.
    **Wired** as the **one child**.

**The dorsal globus pallidus is the CANONICAL globus pallidus.** The
**GPe** and **GPi** are the structures that clinicians mean when they
say "globus pallidus" — they are the targets of **pallidotomy** and
**deep brain stimulation** for **Parkinson's disease** and
**dystonia**. Their absence from the tree is a **major structural
gap**, and this module documents it as **prose**, not as a structural
child.

**The ventral pallidum is the LIMBIC globus pallidus.** It is the
**reward/motivation output** of the ventral striatum, and it is part
of the **extended amygdala** (SLEA) in some classifications. It is the
**one wired child** of this container, and it carries the
**extended-amygdala SLEA overlap** that the **basal ganglia container
deferred** to this level.

**The globus pallidus is NOT a single functional system.** The
**dorsal** (motor) and **ventral** (limbic/reward) subsystems have
**different functions**, **different connections**, and **different
clinical associations**:
*   **Dorsal** — **motor output** (Parkinson's, Huntington's,
    dystonia, hemiballismus — the **movement disorders**).
*   **Ventral** — **reward, motivation, addiction** (addiction,
    depression, OCD).

Consumers must **not** treat "globus pallidus" as a single functional
system — it is a **structural grouping** of **dorsal and ventral**
subsystems with **different roles**.

**The globus pallidus is a paired structure.** Each hemisphere has its
own globus pallidus, with **ipsilateral** striatal input and
**ipsilateral** thalamic output. The two sides are **bilaterally
symmetric** and **largely non-lateralized** — the dorsal (motor) and
ventral (limbic/reward) functions are **bilateral**. Some **subtle
lateralization** has been reported for the **striatum** (not the
globus pallidus), but it is **weak** and **not a strong classification
basis**. See *Lateralization Notes*.

Container Contents (one wired child + a documented gap)
--------------------------------------------------------
The globus pallidus container has **exactly one wired child**:

*   **``ventral_pallidum``** — the **limbic/reward output** of the
    ventral striatum. **Depth: leaf (no children).** Part of the
    **extended amygdala** (SLEA) in some classifications — the
    **full extended-amygdala warning** is in the **ventral pallidum
    module**.

**Documented gap (deliberately NOT wired):**

*   **External globus pallidus (GPe)** — the **lateral** segment (also
    called the **lateral globus pallidus**); part of the **indirect
    pathway** (striatum → GPe → STN → GPi). **NOT wired** in the tree.
    Its functions (indirect pathway, movement suppression, action
    inhibition) are documented as **prose** below.

*   **Internal globus pallidus (GPi)** — the **medial** segment (also
    called the **medial globus pallidus**); the **main output** of
    the basal ganglia (striatum → GPi → thalamus); the **target of
    pallidotomy and DBS** for Parkinson's and dystonia. **NOT wired**
    in the tree. Its functions (direct pathway output, movement
    facilitation) are documented as **prose** below.

*   **Medullary laminae (external and internal)** — white-matter
    sheets **within** the globus pallidus, separating the segments.
    **Prose**, not structural children (and white matter, not grey).

**Not children (deliberately excluded):**
*   **Striatum** — ``.../basal_ganglia/striatum/`` — **sibling**
    (input structure).
*   **Subthalamic nucleus** — ``.../diencephalon/subthalamus/subthalamic_nucleus/``
    — **diencephalic** (functionally related, structurally separate).
*   **Substantia nigra** — ``.../midbrain/tegmentum/substantia_nigra/``
    — **midbrain** (functionally related to the striatum, not the
    globus pallidus).
*   **Substantia innominata** — ``.../basal_forebrain/substantia_innominata/``
    — **basal forebrain sibling** (blends laterally).

The Globus Pallidus / Dorsal Segment Gap
----------------------------------------
This is the **most consequential structural gap** in the globus
pallidus container, and the **third documented gap** in the subcortical
tree. The **dorsal segments** (GPe, GPi) are the **canonical** globus
pallidus — the structures that clinicians mean when they say "globus
pallidus," and the **targets of pallidotomy and DBS** for Parkinson's
and dystonia. They are **NOT wired** as children. Their functions are
documented as **prose**:

*   **External globus pallidus (GPe)** — the **lateral** segment
    (also called the **lateral globus pallidus**). **GABAergic**.
    Receives **striatal** input (from the **indirect pathway
    striatal neurons**), and projects to the **subthalamic nucleus
    (STN)** and the **GPi**. Its function is to **inhibit** the STN
    and the GPi, contributing to the **indirect pathway's suppression
    of unwanted movements**. **Lesions of the GPe** produce
    **hyperkinetic** movement disorders (chorea, ballism) by
    disinhibiting the STN and GPi.

*   **Internal globus pallidus (GPi)** — the **medial** segment (also
    called the **medial globus pallidus**). **GABAergic**. The
    **main output** of the basal ganglia. Receives **striatal** input
    (from the **direct pathway** and the **indirect pathway**,
    via the STN) and projects to the **thalamus** (via the **ansa
    lenticularis** and **lenticular fasciculus**) and the
    **pedunculopontine nucleus (PPN)**. Its function is to
    **inhibit** the thalamus, **gating** movement. **GPi
    pallidotomy** or **DBS** reduces the **excessive GPi inhibition**
    of the thalamus in **Parkinson's disease**, improving
    **bradykinesia and rigidity**. **GPi DBS** is also used for
    **dystonia** and **Huntington's chorea**.

**The dorsal segments are the CANONICAL globus pallidus.** Consumers
that need the **GPe or GPi** must be aware that:
*   They are **not** in the tree dump.
*   Their **functions** are documented as **prose** in this module.
*   Their **surgical targets** (pallidotomy, DBS) are the
  **signature clinical associations** of the globus pallidus.
*   Resolving a "gpe" or "gpi" path is **not possible** — they are a
  **documented gap**, like the **lateral septal nucleus** and the
  **magnocellular preoptic nucleus**.

The Globus Pallidus / Ventral Pallidum Boundary
-----------------------------------------------
This is the **one wired boundary** in the globus pallidus container:

*   **Globus pallidus** (this module) — the **container** for the
    dorsal (motor) + ventral (limbic) segments. The **dorsal
    segments** are a **documented gap**; the **ventral pallidum** is
    the **one wired child**.

*   **Ventral pallidum** (``.../globus_pallidus/ventral_pallidum/``)
    — the **limbic/reward output** of the ventral striatum. **Wired**
    as the **only child**. Part of the **extended amygdala** (SLEA) in
    some classifications — the **full extended-amygdala warning** is
    in the **ventral pallidum module**.

**The ventral pallidum is the LIMBIC globus pallidus.** Consumers
that need the **limbic/reward** component resolve the **ventral
pallidum**; consumers that need the **motor** component must resolve
it as **prose** in **this module** (the **dorsal segment gap**).

The Globus Pallidus / Striatum Boundary
---------------------------------------
This is the **input-output** boundary of the basal ganglia:

*   **Striatum** (``.../basal_ganglia/striatum/``) — the **input**
    structure (dorsal: caudate, putamen; ventral: nucleus accumbens,
    olfactory tubercle). **Sibling**.

*   **Globus pallidus** (this module) — the **output** structure
    (dorsal: GPe, GPi; ventral: ventral pallidum). **Sibling**.

**They are siblings under the basal ganglia container.** The
**cortico-striato-pallido-thalamo-cortical loop** connects them: the
**striatum** is the **first** relay (cortical input), and the
**globus pallidus** is the **second** relay (thalamic output).
Consumers that need the **input** structure must resolve the
**striatum**; consumers that need the **output** structure must resolve
**this module**.

The Globus Pallidus / Subthalamic Nucleus Boundary
--------------------------------------------------
This is the **indirect-pathway** boundary:

*   **Subthalamic nucleus (STN)** —
    ``.../diencephalon/subthalamus/subthalamic_nucleus/`` — the
    **diencephalic** relay of the **indirect pathway**. **Glutamatergic**
    (excitatory). Receives **GPe** input and projects to the **GPi**.
    **Functionally related** to the globus pallidus but **structurally
    separate** (diencephalon, not telencephalon).

*   **Globus pallidus** (this module) — the **GABAergic** output of
    the **direct** and **indirect** pathways. **Telencephalic**.

**The STN is NOT a globus pallidus child.** It is a **diencephalic
sibling** — functionally related (part of the same
cortico-striato-pallido-subthalamo-pallido-thalamo-cortical loop) but
structurally separate. **STN DBS** (deep brain stimulation) is a
**different surgical target** from **GPi pallidotomy/DBS** — the STN
is used for **Parkinson's disease**, and the GPi is used for
**Parkinson's, dystonia, and Huntington's chorea**. Consumers must
not conflate them.

The Globus Pallidus / Substantia Nigra Boundary
-----------------------------------------------
This is the **dopaminergic** boundary:

*   **Substantia nigra** —
    ``.../midbrain/tegmentum/substantia_nigra/`` — the
    **dopaminergic** (pars compacta) and **GABAergic** (pars
    reticulata) **midbrain** nucleus. Its **pars compacta** provides
    **dopaminergic input to the striatum** (the **nigrostriatal
    pathway**); its **pars reticulata** is a **GABAergic output**
    comparable to the **GPi**. **Functionally related** to the basal
    ganglia but **structurally separate** (midbrain).

*   **Globus pallidus** (this module) — the **GABAergic** output of
    the **telencephalic** basal ganglia.

**The substantia nigra is NOT a globus pallidus child.** Its
**pars compacta** projects to the **striatum** (not the globus
pallidus); its **pars reticulata** is a **parallel output** to the
GPi (both project to the thalamus). Consumers that need the
**dopaminergic** or **GABAergic** midbrain component must resolve
the **substantia nigra**; consumers that need the **telencephalic**
GABAergic output must resolve **this module**.

The Globus Pallidus / Extended Amygdala Boundary
------------------------------------------------
This is the **SLEA** boundary — the **deferred warning** from the
basal ganglia container:

*   **Extended amygdala** (``.../extended_amygdala/``) — the **BNST**,
    the **central amygdaloid nucleus**, and (in the **SLEA
    classification**) the **ventral pallidum** and parts of the
    **nucleus accumbens**.

*   **Globus pallidus** (this module) — the **ventral pallidum** (the
    **one wired child**) is part of the **SLEA classification**.

**The tree splits them.** The **ventral pallidum** is under
``.../globus_pallidus/ventral_pallidum/``, and the **nucleus
accumbens** is under ``.../striatum/ventral_striatum/nucleus_accumbens/``
— **not** under the extended amygdala. This is a **deliberate
boundary choice**. Consumers that need the **extended amygdala** as a
unit (per the SLEA classification) must **union**
``.../extended_amygdala/`` with the **ventral pallidum** and **nucleus
accumbens** — the tree does **not** provide this union as a single
path.

**The globus pallidus container carries the LIGHT warning**: the
**ventral pallidum is a direct child** with **classificatory overlap**
with the extended amygdala (SLEA), so the warning is **less deferred**
than at the basal ganglia container level. But the **dorsal segments**
(the canonical GPe/GPi, **not wired**) have **no amygdala
relationship**, so the warning is **not container-wide** — it applies
**specifically to the ventral pallidum**, and the **full warning**
belongs to the **ventral pallidum module**.

The Globus Pallidus / Diencephalon Boundary
-------------------------------------------
This is the **embryological** boundary:

*   **Striatum** — **telencephalic** embryology.
*   **GPi** — **telencephalic** embryology.
*   **Ventral pallidum** — **telencephalic** embryology.
*   **GPe** — **DIENCEPHALIC** embryology (classical classification).

**The tree groups the GPe under the basal ganglia** — a **clinical and
functional** grouping, not an **embryological** one. This is a
**deliberate boundary choice**. Consumers must not treat the globus
pallidus as a **single embryological** entity — the **GPe** is
**diencephalic** in origin, and the **GPi** and **ventral pallidum**
are **telencephalic**.

The Globus Pallidus / Substantia Innominata Boundary
----------------------------------------------------
This is the **basal forebrain** boundary:

*   **Substantia innominata** —
    ``.../basal_forebrain/substantia_innominata/`` — a **basal
    forebrain grey-matter region** that **blends laterally** into the
    globus pallidus (especially the **GPe**).

*   **Globus pallidus** (this module) — the **basal ganglia output**
    structure. The **ventral pallidum** is **embedded** in the
    substantia innominata's territory.

**They are siblings under `subcortical/`.** The **substantia
innominata** is a **basal forebrain** structure; the **globus
pallidus** is a **basal ganglia** structure. They **blend** laterally
(the GPe/ventral pallidum overlap with the substantia innominata
territory), but they are **structurally separate**. Consumers must
not resolve the substantia innominata through the globus pallidus, or
vice versa.

Function in the Human Brain
---------------------------
The globus pallidus has **two functionally distinct subsystems**, and
**only one is wired**:

**Dorsal globus pallidus (GPe + GPi — DOCUMENTED GAP, prose only):**

*   **Indirect Pathway (GPe Function):** The **GPe** is part of the
    **indirect pathway** (striatum → GPe → STN → GPi → thalamus),
    which **suppresses unwanted movements**. Its **GABAergic
    inhibition** of the STN and GPi is part of the **action
    inhibition** circuit. **Lesions** produce **hyperkinetic**
    disorders (chorea, ballism).

*   **Direct/Indirect Output (GPi Function):** The **GPi** is the
    **main output** of the basal ganglia (striatum → GPi → thalamus;
    striatum → GPe → STN → GPi → thalamus). Its **GABAergic
    inhibition** of the thalamus **gates** movement — it **inhibits**
    the thalamus and **suppresses** movement when the basal ganglia
    **do not select** an action, and it **disinhibits** the thalamus
    when the basal ganglia **select** an action. **GPi pallidotomy**
    or **DBS** reduces excessive GPi inhibition in **Parkinson's
    disease**, improving **bradykinesia and rigidity**.

*   **NOT in the tree.** The dorsal segments are a **documented gap**.
    Consumers that need the **motor output** of the basal ganglia must
    resolve its functions as **prose** in this module.

**Ventral pallidum (the one wired child):**

*   **Reward and Motivation (Ventral Pallidum Function):** The
    **ventral pallidum** is the **limbic/reward output** of the
    ventral striatum (nucleus accumbens, olfactory tubercle). It
    projects to the **mediodorsal thalamus**, the **lateral
    habenula**, and the **brainstem**, and it is involved in
    **reward, motivation, and addiction**. **Lesions** impair
    **reward-seeking** and **motivation**.

*   **Extended Amygdala Continuity (Contested — SLEA Classification):**
    The **ventral pallidum** is part of the **SLEA** (sublenticular
    extended amygdala) in some classifications, giving it a role in
    **stress, anxiety, and reward** — but the tree **splits** it from
    the extended amygdala, and the SLEA classification is
    **contested**.

*   **NOT a neural processor in the classical sense.** The ventral
    pallidum is a **GABAergic output** — it **inhibits** its targets
    and **gates** reward-related behavior, but the **full function**
    is documented in the **ventral pallidum module**.

**The unifying theme:** the globus pallidus is the **GABAergic output**
of the basal ganglia — the **dorsal** segments are the **motor
output** (GPe and GPi, **not wired** — a documented gap), and the
**ventral pallidum** is the **limbic/reward output** (**wired** as
the one child). Consumers must not treat "globus pallidus" as a
single functional system — the **dorsal** and **ventral** subsystems
have **different functions**.

Associated Disorders
--------------------
Globus pallidus disorders are **motor** (dorsal) and **limbic/reward**
(ventral) — the **two subsystems** are clinically distinct:

*   **Parkinson's Disease (GPi Function):** The **GPi** is **overactive**
    in Parkinson's disease (due to **dopaminergic loss** in the
    striatum), **over-inhibiting** the thalamus and producing
    **bradykinesia, rigidity, and tremor**. **GPi pallidotomy** and
    **GPi DBS** reduce the **overactive GPi** and **improve motor
    symptoms**. This is the **signature surgical association** of
    the globus pallidus.

*   **Dystonia (GPi Function):** The **GPi** is **overactive** in
    **primary dystonia** (and in some secondary dystonias).
    **GPi DBS** is the **treatment of choice** for **medically
    refractory dystonia** — it has a **high response rate** and is
    **FDA-approved** for this indication.

*   **Huntington's Disease (Dorsal Striatum/GPe Function):** In
    **Huntington's disease**, the **dorsal striatum** (especially the
    **indirect pathway** striatal neurons) degenerates first, causing
    **GPe disinhibition**, **STN overactivity**, and **GPi
    overinhibition** — but the **clinical picture** is
    **hyperkinetic** (chorea), because the **direct pathway** also
    degenerates. **GPi DBS** has been used for **medication-refractory
    chorea**. The **globus pallidus** (GPe) is the **first affected**
    structure in HD after the striatum.

*   **Hemiballismus (STN Function — NOT GP):** **Hemiballismus** —
    violent, involuntary **proximal limb movements** — is caused by
    a **lesion of the subthalamic nucleus (STN)**, **not** the globus
    pallidus. But the **GPi** is the **downstream target** of the STN
    (STN → GPi → thalamus), so **GPi pallidotomy** can **reduce
    hemiballismus**. The STN is **diencephalic** (not a globus
    pallidus child), and this is a **contrast** disorder.

*   **Addiction (Ventral Pallidum Function):** The **ventral pallidum**
    is a key node in the **reward circuit** (with the nucleus
    accumbens and VTA). Its **dysfunction** contributes to
    **addiction**, **craving**, and **relapse**. The **ventral
    pallidum** is a **therapeutic target** in experimental
    **DBS for addiction**.

*   **Depression (Ventral Pallidum Function):** The **ventral pallidum**
    is **overactive** in **depression** in some models. **Ventral
    pallidum DBS** has been investigated for
    **treatment-resistant depression** — results are **mixed** but the
    target is **clinically relevant**.

*   **OCD (Ventral Striatum/Ventral Pallidum Function):** The **ventral
    striatum** and **ventral pallidum** are part of the **OCD
    circuit**. **Ventral pallidum DBS** is an **experimental
    treatment** for **treatment-resistant OCD**.

**What is NOT here:** The globus pallidus is **not** the substrate for
**Alzheimer's disease** (nucleus basalis), **basal forebrain amnesia**
(septum/DBB), **Kluver-Bucy syndrome** (amygdala), or **temporal
lobe epilepsy** (hippocampus). Its clinical footprint is **motor**
(dorsal — Parkinson's, dystonia, Huntington's) and **limbic/reward**
(ventral — addiction, depression, OCD) — a **distinct category** from
the basal forebrain's **cholinergic-cognitive** footprint.

Lateralization Notes
--------------------
This is the **left** globus pallidus container. The globus pallidus is
**bilaterally symmetric** and **largely non-lateralized** — but the
**light warning** from the deferred extended-amygdala overlap applies
at this level:

*   **Bilateral Motor Output (Dorsal):** Each globus pallidus projects
    **ipsilaterally** to the thalamus. The two sides are **functionally
    symmetric** for motor output. **GPi DBS** is **bilateral** in
    **Parkinson's disease** and **dystonia** (both hemispheres
    stimulated).

*   **Bilateral Limbic/Reward Output (Ventral):** Each ventral pallidum
    projects **ipsilaterally** to the mediodorsal thalamus. The two
    sides are **functionally symmetric** for reward and motivation.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the globus pallidus has **no documented strong
    left-lateralized or right-lateralized function**. **Parkinson's**
    and **dystonia** are **bilateral**; **addiction** and
    **depression** are **bilateral** in the ventral pallidum.

*   **Extended Amygdala Overlap (LIGHT WARNING — at container level):**
    The **ventral pallidum** (the one wired child) is part of the
    **SLEA** in some classifications. The **basal ganglia container**
    **deferred** the amygdala-lateralization warning to this level;
    the **globus pallidus container** now carries the **light
    warning**, because the **ventral pallidum is a direct child** with
    **classificatory overlap** with the extended amygdala. But the
    **dorsal segments** (GPe/GPi, **not wired**) have **no amygdala
    relationship**, so the warning is **not container-wide** — it
    applies **specifically to the ventral pallidum**, and the **full
    warning** belongs to the **ventral pallidum module**.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the **amygdala
    module** and (weakly via SLEA) to the **extended amygdala
    module** — **not** to the globus pallidus container, **not** to
    the dorsal segments, and **not** to the ventral pallidum (which
    is **downstream** of the container). Consumers must **not** import
    the right-amygdala fear association into this container.

**A consumer that assumes "left globus pallidus = right globus
pallidus" will be structurally and functionally correct** — the two
sides are symmetric, no lateralized function has been demonstrated,
and the **light warning** at this level **defers the full warning**
to the **ventral pallidum module**. This is a **strict-mirror pair
with a light warning** — **one level less deferred** than the basal
ganglia container, because the ventral pallidum is a **direct child**
(not a grandchild). The warning **tracks the anatomy** — it is
**light** at the globus pallidus container level, **full** at the
ventral pallidum module level.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../diencephalon/``, ``.../midbrain/``, ``.../extended_amygdala/``,
    or any other container. The globus pallidus's relationships to
    the STN, substantia nigra, and extended amygdala are documented
    as **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — one wired child + a documented gap.** The
    globus pallidus container has **exactly one wired child**:
    ``ventral_pallidum``. The **dorsal segments** (GPe, GPi) are a
    **documented structural gap** — they are **classically expected**
    but **not wired**, like the **lateral septal nucleus** in
    ``septal_nuclei/`` and the **magnocellular preoptic nucleus** in
    ``substantia_innominata/``. Their functions are **prose**.
*   **DORSAL GAP — the canonical GPe/GPi are NOT wired.** The
    **external globus pallidus (GPe)** and **internal globus pallidus
    (GPi)** are the **canonical** globus pallidus — the **targets of
    pallidotomy and DBS**. They are **not** in the tree dump. Their
    functions (indirect pathway, direct pathway output, movement
    gating) are documented as **prose**. Consumers must be aware that
    **resolving a "gpe" or "gpi" path is not possible**.
*   **Not a single functional system.** The **dorsal** (motor) and
    **ventral** (limbic/reward) subsystems are functionally distinct.
    Consumers must not treat "globus pallidus" as a single functional
    system.
*   **Not the striatum — sibling.** The striatum is the **input**
    structure; the globus pallidus is the **output** structure. They
    are **siblings** under the basal ganglia.
*   **Not the subthalamic nucleus — diencephalic sibling.** The STN
    is functionally related (indirect pathway) but structurally
    separate (diencephalon). Do not resolve it through the globus
    pallidus.
*   **Not the substantia nigra — midbrain sibling.** The substantia
    nigra is functionally related (dopaminergic input to the
    striatum) but structurally separate (midbrain). Do not resolve it
    through the globus pallidus.
*   **Extended amygdala overlap via ventral pallidum — light warning
    at this level, full warning in the ventral pallidum module.** The
    ventral pallidum is a **direct child** with **classificatory
    overlap** with the extended amygdala (SLEA). The **globus pallidus
    container** carries the **light warning**; the **full warning**
    belongs to the **ventral pallidum module**.
*   **Diencephalic embryology of the GPe.** The **external globus
    pallidus** has **diencephalic** embryology in classical
    classifications, but the tree groups it under the basal ganglia
    (a clinical/functional grouping). Consumers must not treat the
    globus pallidus as a single embryological entity.
*   **Internal capsule separates the segments — white matter, not a
    GP child.** The internal capsule and the medullary laminae are
    **white matter**, not globus pallidus children. Do not resolve
    them through this module.
*   **Not the substantia innominata — basal forebrain sibling.**
    The substantia innominata blends laterally into the globus
    pallidus, but it is a **basal forebrain** structure, not a globus
    pallidus child.
*   **No ``AREA_PATHS`` hop.** The globus pallidus is a local
    container under the basal ganglia, not a cross-listed leaf.
*   **No nested cross-listing.** The globus pallidus has no nested
    dual-framing module. It is a single container.
*   **Structural parity with right globus pallidus — strict mirror
    with a light warning.** Left and right globus pallidus modules
    are **structurally identical** — same one wired child, same
    dorsal-segment gap, same extended-amygdala classificatory-overlap
    note (light warning), same diencephalic-embryology flag, same
    striatum/STN/substantia-nigra/substantia-innominata boundaries.
    **The warning is light at this level** — the full warning is in
    the ventral pallidum module.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_ganglia import globus_pallidus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "basal_ganglia.globus_pallidus"
    )

**Do not** assume the globus pallidus container has **GPe** or **GPi**
children. They are a **documented structural gap** — the **canonical**
globus pallidus segments are **not wired**. Their functions are
documented as **prose** in this module. **Resolving a "gpe" or "gpi"
path is not possible.**

**Do not** assume the globus pallidus container has **more than one
wired child**. It has **exactly one**: ``ventral_pallidum``.

**Do not** assume the globus pallidus is the **striatum**. The
striatum is the **input** structure (sibling); the globus pallidus is
the **output** structure.

**Do not** assume the globus pallidus **contains** the subthalamic
nucleus, substantia nigra, or substantia innominata. Those are
**diencephalic, midbrain, or basal forebrain** siblings, not globus
pallidus children.

**Do not** assume the globus pallidus is a **single functional
system**. Its **dorsal** (motor) and **ventral** (limbic/reward)
subsystems are functionally distinct.

**Do not** import **amygdala-lateralization claims** into the globus
pallidus container. The **ventral pallidum** (the one wired child) has
**classificatory overlap** with the extended amygdala (SLEA), but the
warning is **light at this container level** and the **full warning**
belongs to the **ventral pallidum module**. The **dorsal segments**
(the canonical GPe/GPi, **not wired**) have **no amygdala
relationship**.

Iterating the globus pallidus's one wired child (recommended consumer
pattern)::

    GLOBUS_PALLIDUS_CHILDREN = (
        "ventral_pallidum",
    )
    # Closed set. The dorsal segments (GPe, GPi) are a DOCUMENTED GAP.

Reaching the dorsal segment functions (recommended consumer pattern —
note the GAP)::

    # The external globus pallidus (GPe) and internal globus pallidus
    # (GPi) are NOT in the tree. Their functions are documented as
    # PROSE in this module. If you need a path for them, you must:
    #
    #   1. Note the gap in your registry.
    #   2. Optionally, document them as "virtual" or "prose-only"
    #      nodes under globus_pallidus, with a clear "NOT IN TREE"
    #      marker.
    #
    # Do NOT attempt to resolve a "gpe" or "gpi" path — they do not
    # exist in the tree.

Reaching the extended amygdala's ventral-pallidum component
(recommended consumer pattern — the SLEA union)::

    # The extended amygdala's SLEA classification includes the
    # ventral pallidum. The tree splits them. Consumers that need
    # the SLEA grouping must union:
    #
    #   subcortical.extended_amygdala
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #
    # The tree does not provide this union as a single path.

Reaching the subthalamic nucleus (recommended consumer pattern — NOTE
the diencephalon boundary)::

    # The subthalamic nucleus is FUNCTIONALLY related to the globus
    # pallidus (indirect pathway) but STRUCTURALLY separate
    # (diencephalon):
    #
    #   diencephalon.subthalamus.subthalamic_nucleus
    #
    # Do NOT resolve STN through the globus pallidus.

Reaching the substantia nigra (recommended consumer pattern — NOTE
the midbrain boundary)::

    # The substantia nigra is FUNCTIONALLY related to the striatum
    # (dopaminergic input), but it is STRUCTURALLY separate (midbrain)
    # and it is NOT a globus pallidus child:
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # Do NOT resolve substantia nigra through the globus pallidus.

Reconstructing the classical "basal ganglia + basal forebrain"
(recommended consumer pattern — inherited from the parent)::

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

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        gp_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.globus_pallidus"
        )
        # resolve gp_path through the memory/recall layer

References
----------
*   **Canonical globus pallidus anatomy:** DeLong, M.R., Wichmann, T.
    (2007). "Circuits and circuit disorders of the basal ganglia."
    *Archives of Neurology* 64:20–24. (Definitive review; direct and
    indirect pathways; GPe/GPi; ventral pallidum.)
*   **Basal ganglia (textbook):** Standaert, D.G., Young, A.B.
    (2015). "Treatment of central nervous system degenerative
    disorders." In *Goodman & Gilman's Pharmacological Basis of
    Therapeutics*, 12th ed. (Basal ganglia disorders; pallidotomy;
    GPi DBS.)
*   **GPe/GPi functional anatomy:** Bolam, J.P., Hanley, J.J., Booth,
    P.A., Bevan, M.D. (2000). "Synaptic organisation of the basal
    ganglia." *Journal of Anatomy* 196:527–542. (GPe/GPi synaptic
    organization.)
*   **Direct/indirect pathways:** Albin, R.L., Young, A.B., Penney,
    J.B. (1989). "The functional anatomy of basal ganglia disorders."
    *Trends in Neurosciences* 12:366–375. (Direct/indirect pathway
    model.)
*   **GPi DBS for Parkinson's:** Deep-Brain Stimulation for
    Parkinson's Disease Study Group (2001). "Deep-brain stimulation
    of the subthalamic nucleus or the pars interna of the globus
    pallidus in Parkinson's disease." *New England Journal of
    Medicine* 345:956–963. (GPi DBS for Parkinson's.)
*   **GPi DBS for dystonia:** Kupsch, A., et al. (2006). "Pallidal
    deep-brain stimulation in primary generalised dystonia."
    *Lancet Neurology* 5:529–534. (GPi DBS for dystonia.)
*   **Huntington's disease:** Vonsattel, J.P., DiFiglia, M. (1998).
    "Huntington disease." *Journal of Neuropathology and Experimental
    Neurology* 57:369–384. (Dorsal striatum and GPe degeneration in
    HD.)
*   **Ventral pallidum reward:** Smith, K.S., Tindell, A.J., Aldridge,
    J.W., Berridge, K.C. (2009). "Ventral pallidum roles in reward
    and motivation." *Behavioural Brain Research* 196:155–167.
    (Ventral pallidum in reward and motivation.)
*   **Ventral pallidum extended amygdala:** Alheid, G.F., Heimer, L.
    (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA; ventral pallidum in the extended
    amygdala continuum.)
*   **Ventral pallidum DBS for depression:** Malone, D.A., et al.
    (2009). "Deep brain stimulation of the ventral capsule/ventral
    striatum for treatment-resistant depression." *Biological
    Psychiatry* 65:267–275. (Ventral pallidum DBS for depression.)
*   **Ventral pallidum DBS for OCD:** Greenberg, B.D., et al. (2010).
    "Deep brain stimulation of the ventral internal capsule/ventral
    striatum for obsessive-compulsive disorder." *Molecular
    Psychiatry* 15:64–79. (Ventral pallidum DBS for OCD.)
*   **Subthalamic nucleus (contrast):** Bergman, H., Wichmann, T.,
    DeLong, M.R. (1990). "Reversal of experimental parkinsonism by
    lesions of the subthalamic nucleus." *Science* 249:1436–1438.
    (STN lesion and Parkinson's; the STN is diencephalic, not a GP
    child.)
*   **Substantia nigra (contrast):** Braak, H., et al. (2003).
    "Staging of brain pathology related to sporadic Parkinson's
    disease." *Neurobiology of Aging* 24:197–211. (Substantia nigra
    pathology; the substantia nigra is midbrain, not a GP child.)
*   **GPe diencephalic embryology:** Alvarez-Bolado, G., Paul, F.A.,
    Blaess, S. (2018). "Sonic hedgehog lineage in the mouse
    hypothalamus." *Frontiers in Neuroanatomy* 12:83. (GPe
    diencephalic origin; GPi telencephalic origin.)
*   **Substantia innominata (contrast):** Heimer, L., de Olmos, J.,
    Alheid, G.F., Záborszky, L. (1999). "The human basal forebrain:
    an overview." In *The Human Nervous System* (Paxinos, G., ed.),
    2nd ed. (Substantia innominata as a basal forebrain grey-matter
    region; blends into the globus pallidus laterally.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the globus pallidus container
    — the container's only amygdala-adjacent structure is the ventral
    pallidum, and the full warning is in the ventral pallidum
    module.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Globus pallidus in overview.)
*   NeuroNames — Globus pallidus (left); FMA — Globus pallidus (left
    member).
"""