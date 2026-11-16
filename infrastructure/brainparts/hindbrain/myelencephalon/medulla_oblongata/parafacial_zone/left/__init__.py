"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.parafacial_zone.left
==========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── parafacial_zone
                └── left   <-- THIS MODULE

**Primary synonym:** Left parafacial zone; left PZ; left parafacial
zone of the medulla; left parafacial sleep-promoting zone; left
GABAergic parafacial zone.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** at the **ponto-medullary
junction** — the **left** GABAergic / glycinergic neuronal
population **ventral and lateral** to the **left facial nucleus
(VII)** and **adjacent** to the **left rostral ventrolateral
medulla**. It is a **sleep-promoting center**, **NOT** a
respiratory rhythm generator, **NOT** an autonomic premotor
center, and **NOT** the **left parafacial respiratory group
(pFRG)** — though the two are **anatomically adjacent** and are
**frequently conflated** in the older literature.
**Part of:** The **parafacial_zone** bilateral container — which
is part of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../parafacial_zone/`` → **direct child**
of the parafacial_zone container. The **left** parafacial zone is
one of the **two** structural children of the container (the
other is ``right``).
**Structural children:** **None.** This is a **leaf** module. The
left parafacial zone is represented as a **single structure** —
it has **no structural children** of its own.
**Boundary status (NOT the right parafacial zone — the
contralateral leaf):** **Boundary case — the left parafacial
zone is NOT the right parafacial zone.** The **right parafacial
zone** (``.../parafacial_zone/right/``) is the **contralateral
leaf** — the parafacial zone of the **right** medulla. **They
are DIFFERENT LEAVES** — the ``left`` and ``right`` modules are
the two sides of the **bilateral container**. Consumers must
**not** conflate the **left** parafacial zone with the **right**
— resolve the right side via ``parafacial_zone.right``.
**Boundary status (NOT the left parafacial respiratory group — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the left parafacial zone (PZ) is NOT the left parafacial
respiratory group (pFRG).** The **left parafacial respiratory
group (pFRG)** is a **respiratory** structure in the **left
rostral ventrolateral medulla** — it contains
**pre-inspiratory** and **expiratory-modulating** neurons that
are **active during high metabolic demand** (exercise,
hypercapnia), and it is **often grouped** with the **left
retrotrapezoid nucleus (RTN)** as the **left RTN/pFRG** **central
chemoreceptor** complex. The **left parafacial zone (PZ)** (here)
is a **left GABAergic / glycinergic sleep-promoting** region — it
is **active during NREM sleep** and **promotes slow-wave sleep**.
**They share the name "parafacial" but are DIFFERENT STRUCTURES
with DIFFERENT FUNCTIONS** — the **left pFRG** is
**respiratory**; the **left PZ** is **sleep-promoting**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left retrotrapezoid nucleus — a
DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the left parafacial zone is NOT the left retrotrapezoid
nucleus.** The **left retrotrapezoid nucleus (RTN)**
(``.../ventral_respiratory_group/retrotrapezoid_nucleus/left/``)
is a **left respiratory chemoreceptor** at the **left ventral
medullary surface** — it senses **CO₂/H⁺** and **drives
breathing**. The **left parafacial zone** (here) is a **left
sleep-promoting** region — it is **NOT** a respiratory
chemoreceptor. They are **anatomically adjacent** in the **left
rostral ventrolateral medulla**, but they are **functionally
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the left RVLM — a DIFFERENT structure with
a DIFFERENT function):** **Boundary case — the left parafacial
zone is NOT the left rostral ventrolateral medulla (RVLM).** The
**left RVLM** (``.../rostral_ventrolateral_medulla/left/``) is
the **left sympathetic premotor / vasomotor** center — it
provides **tonic excitatory drive** to the **left
intermediolateral cell column**. The **left parafacial zone**
(here) is a **left sleep-promoting** region — it is **NOT** an
autonomic premotor center. They are **anatomically adjacent** in
the **left rostral ventrolateral medulla**, but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the left CVLM — a DIFFERENT structure with
a DIFFERENT function):** **Boundary case — the left parafacial
zone is NOT the left caudal ventrolateral medulla (CVLM).** The
**left CVLM** (``.../caudal_ventrolateral_medulla/left/``) is
the **left sympathoinhibitory** relay. The **left parafacial
zone** (here) is a **left sleep-promoting** region. Consumers
must **not** conflate the two — they are at **different
rostrocaudal levels** and have **different functions**.
**Boundary status (NOT the left facial nucleus — a DIFFERENT
structure in the PONS):** **Boundary case — the left parafacial
zone is NOT the left facial nucleus.** The **left facial nucleus
(VII)**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/facial_nerve_nucleus/``)
is a **left branchial motor** nucleus in the **pons** — it
supplies the **left muscles of facial expression**. The **left
parafacial zone** (here) is **ventral and lateral** to the left
facial nucleus — it is **named after** its **position beside**
the facial nucleus ("parafacial" = "beside the facial nucleus").
But it is a **DIFFERENT STRUCTURE** with a **DIFFERENT function**
— the facial nucleus is **motor**; the parafacial zone is
**sleep-promoting**. Consumers must **not** conflate the two.
**Boundary status (NOT the left ventral respiratory group — a
DIFFERENT respiratory structure):** **Boundary case — the left
parafacial zone is NOT the left ventral respiratory group
(VRG).** The **left VRG**
(``.../ventral_respiratory_group/left/``) contains the **left
Bötzinger complex**, **left pre-Bötzinger complex**, **left
nucleus para-ambiguus**, **left nucleus retroambiguus**, **left
nucleus retrofacialis**, and **left retrotrapezoid nucleus** —
the **left respiratory rhythm** and **pattern** generators. The
**left parafacial zone** (here) is a **left sleep-promoting**
region — **NOT** a respiratory rhythm generator. Consumers must
**not** conflate the two.
**Boundary status (NOT the left respiratory_center structures —
a DIFFERENT structure):** **Boundary case — the left parafacial
zone is NOT the left respiratory_center structures.** The
**left respiratory_center**
(``.../respiratory_center/left/``) contains the **left dorsal
respiratory group**, **left area postrema**, **left
chemoreceptor trigger zone**, **left gracile nucleus**, **left
cuneate nucleus**, and **left gigantocellular reticular
nucleus** — the **left dorsal respiratory** and
**chemosensory** structures. The **left parafacial zone** (here)
is a **left sleep-promoting** region — **NOT** a respiratory or
chemosensory structure. Consumers must **not** conflate the
two.
**Boundary status (NOT the left solitary nucleus — a DIFFERENT
structure):** **Boundary case — the left parafacial zone is NOT
the left solitary nucleus.** The **left solitary nucleus (NTS)**
(``.../solitary_nucleus/left/``) is the **left visceral afferent
relay** — it receives **taste**, **baroreceptor**,
**chemoreceptor**, and **gastrointestinal** afferents. The
**left parafacial zone** (here) is a **left sleep-promoting**
region — **NOT** a visceral afferent relay. Consumers must **not**
conflate the two.
**Boundary status (NOT the left medullary pyramid — a DIFFERENT
structure):** **Boundary case — the left parafacial zone is NOT
the left medullary pyramid.** The **left medullary pyramid**
(``.../medullary_pyramid/left/``) is the **left ventral
white-matter** corticospinal / corticobulbar tract. The **left
parafacial zone** (here) is a **left grey-matter**
sleep-promoting region. Consumers must **not** conflate the two.
**Boundary status (NOT the left olivary body — a DIFFERENT
structure):** **Boundary case — the left parafacial zone is NOT
the left olivary body.** The **left olivary body**
(``.../olivary_body/left/``) is the **left cerebellar
climbing-fiber relay**. The **left parafacial zone** (here) is
a **left sleep-promoting** region. Consumers must **not**
conflate the two.
**Boundary status (NOT the left arcuate nucleus — a DIFFERENT
structure):** **Boundary case — the left parafacial zone is NOT
the left arcuate nucleus.** The **left arcuate nucleus**
(``.../arcuate_nucleus/left/``) is a **left ventral-surface
chemosensory and hypothalamic-projecting** nucleus. The **left
parafacial zone** (here) is a **left sleep-promoting** region.
Consumers must **not** conflate the two.
**Boundary status (NOT the left cranial nerve nuclei — DIFFERENT
structures):** **Boundary case — the left parafacial zone is NOT
the left cranial nerve nuclei.** The **left cranial nerve
nuclei** (``.../cranial_nerve_nuclei/left/``) are the **left
medullary motor** nuclei (hypoglossal, dorsal motor vagus,
inferior salivatory, nucleus ambiguus). The **left parafacial
zone** (here) is a **left sleep-promoting** region — **NOT** a
cranial nerve motor nucleus. Consumers must **not** conflate the
two.
**Boundary status (NOT the whole left medulla oblongata — a
small grey-matter region within it):** **Boundary case — the
left parafacial zone is NOT the whole left medulla oblongata.**
The **medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the left cranial nerve
nuclei, the left autonomic nuclei, the left respiratory centers,
the left olivary body, the left medullary pyramid, the left
arcuate nucleus, the left parafacial zone (here), and other
structures. The **left parafacial zone** is **one small
grey-matter region** within the left medulla. Consumers must
**not** conflate the **left parafacial zone** with the **whole
left medulla**.

Overview
--------
The **left parafacial zone (PZ)** is a **left GABAergic /
glycinergic** grey-matter region at the **ponto-medullary
junction** — **ventral and lateral** to the **left facial
nucleus (VII)** and **adjacent** to the **left rostral
ventrolateral medulla (RVLM)**. It is a **sleep-promoting
center** — it is **active during NREM sleep**, and it
**promotes slow-wave sleep (SWS)** by **inhibiting** the
**wake-promoting** systems of the **basal forebrain**, **lateral
hypothalamus**, and **brainstem**.

**This is a LEAF module.** The **left parafacial zone** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **side-specific** resolution of
the left parafacial zone use this module; consumers that need
the **right-side** resolution use
``.../parafacial_zone/right/``; consumers that need the **whole
parafacial_zone container** use ``.../parafacial_zone/``.

**The left parafacial zone is the SLEEP-PROMOTING left
parafacial zone, NOT the left parafacial respiratory group.**
The **left parafacial respiratory group (pFRG)** is a
**respiratory** structure — part of the **left RTN/pFRG**
**central chemoreceptor** complex — **NOT** a sleep-promoting
center. **They share the name "parafacial" but are DIFFERENT
STRUCTURES with DIFFERENT FUNCTIONS** — the **left pFRG** is
**respiratory**; the **left PZ** is **sleep-promoting**. In
older literature, the two are **frequently conflated**; modern
work (Anaclet et al., 2012) has **dissociated** them.

**The left parafacial zone is a GREY-MATTER sleep-promoting
region, NOT a respiratory rhythm generator, NOT an autonomic
premotor center, and NOT a cranial nerve motor nucleus.** It
**contains** a **GABAergic / glycinergic** neuronal population
that **projects** to the **left and right basal forebrain**,
the **left and right lateral hypothalamus** (including **MCH
neurons**), and other **wake-promoting** centers, and it
**promotes NREM sleep**.

**The left parafacial zone is a NAME-COLLISION HAZARD.** The
name "parafacial" appears in **two different structures** — the
**left parafacial zone (PZ)** and the **left parafacial
respiratory group (pFRG)** — and the two are **often conflated**
in the literature. Consumers must **not** import the
**respiratory** function of the **left pFRG** into the **left
parafacial zone** — the left parafacial zone is a
**sleep-promoting** center.

The Left Parafacial Zone / Right Parafacial Zone Boundary
---------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left parafacial zone** (this module) — the parafacial zone
    of the **left** medulla.

*   **Right parafacial zone** (``.../parafacial_zone/right/``) —
    the parafacial zone of the **right** medulla.

**The two are the SIDES of the bilateral parafacial_zone
container.** They are **structurally symmetric mirror pairs** —
same cytoarchitecture, same projections, same **no warning**.
Consumers must **not** conflate the left with the right — resolve
the right side via ``parafacial_zone.right``.

The Left Parafacial Zone / Left Parafacial Respiratory Group Boundary
---------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Left parafacial zone (PZ)** (this module) — the **left
    sleep-promoting** GABAergic region.

*   **Left parafacial respiratory group (pFRG)** — the **left
    respiratory** structure in the **left rostral ventrolateral
    medulla** (often grouped with the **left RTN** as the **left
    RTN/pFRG** complex).

**They share the name "parafacial" but are DIFFERENT STRUCTURES
with DIFFERENT FUNCTIONS.** The **left pFRG** is **respiratory**
(active expiration, pre-inspiratory neurons); the **left PZ** is
**sleep-promoting**. Consumers must **not** conflate the two.

The Left Parafacial Zone / Left Retrotrapezoid Nucleus Boundary
---------------------------------------------------------------
This is the **sleep / respiratory-chemoreceptor** boundary:

*   **Left parafacial zone** (this module) — the **left
    sleep-promoting** region.

*   **Left retrotrapezoid nucleus (RTN)**
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/left/``)
    — the **left respiratory chemoreceptor**.

**They are anatomically adjacent** in the **left rostral
ventrolateral medulla**, but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Left Parafacial Zone / Left RVLM Boundary
---------------------------------------------
This is the **sleep / autonomic-premotor** boundary:

*   **Left parafacial zone** (this module) — the **left
    sleep-promoting** region.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``) —
    the **left sympathetic premotor / vasomotor** center.

**They are anatomically adjacent** in the **left rostral
ventrolateral medulla**, but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Left Parafacial Zone / Left Facial Nucleus Boundary
-------------------------------------------------------
This is the **medulla / pons** and **sleep / motor** boundary:

*   **Left parafacial zone** (this module) — the **left
    sleep-promoting** region.

*   **Left facial nucleus (VII)**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/facial_nerve_nucleus/``)
    — the **left branchial motor** nucleus for the **left muscles
    of facial expression**.

**They are anatomically adjacent** — the left parafacial zone is
**named after** its position **beside** the left facial nucleus.
But they are **DIFFERENT STRUCTURES** — the **left facial
nucleus** is **motor**; the **left parafacial zone** is
**sleep-promoting**. Consumers must **not** conflate the two.

The Left Parafacial Zone / Left Ventral Respiratory Group Boundary
------------------------------------------------------------------
This is the **sleep / respiratory-rhythm** boundary:

*   **Left parafacial zone** (this module) — the **left
    sleep-promoting** region.

*   **Left ventral respiratory group (VRG)**
    (``.../ventral_respiratory_group/left/``) — the **left
    respiratory rhythm and pattern** generators.

**They are functionally distinct.** Consumers must **not**
conflate the two.

The Left Parafacial Zone / Left Respiratory Center Boundary
-----------------------------------------------------------
This is the **sleep / dorsal-respiratory** boundary:

*   **Left parafacial zone** (this module) — the **left
    sleep-promoting** region.

*   **Left respiratory center** (``.../respiratory_center/left/``)
    — the **left dorsal respiratory** and **chemosensory**
    structures.

**They are functionally distinct.** Consumers must **not**
conflate the two.

The Left Parafacial Zone / Left Solitary Nucleus Boundary
---------------------------------------------------------
This is the **sleep / visceral-sensory** boundary:

*   **Left parafacial zone** (this module) — the **left
    sleep-promoting** region.

*   **Left solitary nucleus** (``.../solitary_nucleus/left/``) —
    the **left visceral afferent sensory** relay.

**They are functionally distinct.** Consumers must **not**
conflate the two.

The Left Parafacial Zone / Left Medullary Pyramid, Left Olivary Body, Left Arcuate Nucleus, and Left Cranial Nerve Nuclei Boundary
--------------------------------------------------------------------------------------------------------------------------------
This is the **sleep / white-matter, cerebellar-relay,
chemosensory, and motor** boundary:

*   **Left parafacial zone** (this module) — the **left
    sleep-promoting** region.

*   **Left medullary pyramid** (``.../medullary_pyramid/left/``)
    — the **left white-matter** corticospinal / corticobulbar
    tract.

*   **Left olivary body** (``.../olivary_body/left/``) — the
    **left cerebellar climbing-fiber relay**.

*   **Left arcuate nucleus** (``.../arcuate_nucleus/left/``) —
    the **left ventral-surface chemosensory** nucleus.

*   **Left cranial nerve nuclei**
    (``.../cranial_nerve_nuclei/left/``) — the **left medullary
    motor** nuclei.

**They are functionally distinct** from the **left parafacial
zone**. Consumers must **not** conflate the left parafacial zone
with any of these structures.

Function in the Human Brain
---------------------------
The left parafacial zone's function is **sleep promotion** —
**NOT respiratory rhythm**, **NOT autonomic regulation**, and
**NOT motor control**:

*   **Left NREM sleep promotion:** The **left parafacial zone**
    is **active during NREM sleep** (especially **slow-wave
    sleep**) and **promotes** NREM sleep onset and maintenance.

*   **Inhibition of wake-promoting systems (left side):** The
    **left parafacial zone** **projects** to the **left and
    right basal forebrain**, the **left and right lateral
    hypothalamus** (including **MCH neurons**), and other
    **wake-promoting** centers, and it **inhibits** them —
    thereby **promoting sleep**.

*   **Slow-wave sleep (SWS) generation (left side):** The
    **left parafacial zone** contributes to the **cortical
    slow-wave activity** that characterizes **NREM sleep** —
    its **GABAergic output** **modulates** the **cortical** and
    **thalamocortical** circuits that generate **slow waves**.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** (VRG) — **NOT**
    the left parafacial zone.

*   **NOT autonomic regulation:** The **autonomic regulation**
    is the **RVLM**, **CVLM**, and **NTS** — **NOT** the left
    parafacial zone.

*   **NOT motor control:** The **motor control** is the
    **corticospinal tract** (via the **medullary pyramid**) and
    the **cranial nerve motor nuclei** — **NOT** the left
    parafacial zone.

**The unifying theme:** the left parafacial zone is a **left
GABAergic / glycinergic sleep-promoting region** at the
**ponto-medullary junction** — it **promotes NREM sleep** and
**slow-wave sleep** by **inhibiting wake-promoting systems**.

Associated Disorders
--------------------
The left parafacial zone has **no named clinical syndrome** of
its own — its clinical associations are **indirect**, via
**sleep regulation**:

*   **Insomnia (via left parafacial zone dysfunction —
    hypothesized):** **Reduced** left parafacial zone
    **GABAergic** output — or **impaired** left parafacial zone
    **inhibition** of **wake-promoting** systems — could
    contribute to **insomnia**. This is **speculative** and
    **not** a well-established clinical entity.

*   **Sleep-wake disorders (via left parafacial zone dysfunction
    — hypothesized):** **Abnormal** left parafacial zone
    **activity** — or **altered** left parafacial zone
    **connectivity** with the **basal forebrain** and **lateral
    hypothalamus** — could contribute to **sleep-wake
    dysregulation**. This is **speculative**.

*   **Sudden infant death syndrome (SIDS — via adjacent
    structures):** **SIDS** has been associated with
    **abnormalities** in the **medullary** **serotonergic**
    system — **including** regions **adjacent** to the **left
    parafacial zone**. The **left parafacial zone** itself is
    **not** a primary SIDS substrate, but it is **anatomically
    adjacent** to the **ventral medullary** regions implicated
    in **SIDS**.

*   **No Named "Left Parafacial Zone Syndrome":** The left
    parafacial zone is a **functionally defined region** — it
    has **no named clinical syndrome** of its own.

**What is NOT here:** The left parafacial zone is **not** the
substrate for **respiratory rhythm** (pre-Bötzinger complex,
VRG), **central hypoventilation** (RTN, VRG), **autonomic
dysfunction** (RVLM, CVLM, NTS), or **cranial nerve motor
deficits** (cranial nerve nuclei). Its clinical relevance is
the **sleep-regulation** functions listed above.

Lateralization Notes
--------------------
This is the **left** parafacial zone module. The parafacial
zone is a **bilateral container** whose two sides are
**structurally symmetric mirror pairs** — and it carries **NO
warning**:

*   **Bilateral Symmetry:** The **left** and **right**
    parafacial zones are **structurally symmetric** — they are
    **mirror pairs** with the **same** cytoarchitecture, **same**
    projections, and **same** functions. The **left** parafacial
    zone **promotes NREM sleep** via **bilateral** projections
    to the **basal forebrain** and **lateral hypothalamus**;
    the **right** parafacial zone does the same.

*   **NO Lateralization Warning:** The parafacial zone has **no
    known functional lateralization** in humans. Consumers must
    **not** import a **lateralization warning** into the left
    parafacial zone — the **left** and **right** sides are
    **functionally equivalent**.

*   **NO Extended-Amygdala / SLEA Warning:** The left parafacial
    zone is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the left parafacial zone.

*   **NO Fear-Output Warning:** The left parafacial zone is
    **not** a fear-output structure — it is a **left
    sleep-promoting** region. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left parafacial zone = right
parafacial zone" will be structurally correct** — the two sides
are **symmetric** and **functionally equivalent** at the
**region level**. The parafacial zone is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no fear-output
warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left parafacial zone is
    a **leaf** — it does **not** import from ``.../right/`` or
    any other right-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../ventral_respiratory_group/``,
    ``.../respiratory_center/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../solitary_nucleus/``, ``.../medullary_pyramid/``,
    ``.../olivary_body/``, ``.../arcuate_nucleus/``,
    ``.../cranial_nerve_nuclei/``, ``.../metencephalon/``, or
    any other container. The left parafacial zone's
    relationships to the left parafacial respiratory group
    (pFRG), left retrotrapezoid nucleus, left RVLM, left CVLM,
    left facial nucleus, left VRG, left respiratory_center,
    left solitary nucleus, left medullary pyramid, left olivary
    body, left arcuate nucleus, and left cranial nerve nuclei
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left
    parafacial zone is a **single structure** — it has **no
    structural children**. Consumers must **not** expect further
    sub-paths under ``.../left/``.
*   **NOT the right parafacial zone.** The right parafacial zone
    is a **separate leaf** under ``.../parafacial_zone/right/``.
    Consumers must **not** conflate the left with the right.
*   **NOT the left parafacial respiratory group (pFRG).** The
    pFRG is a **respiratory** structure — **NOT** a
    sleep-promoting center.
*   **NOT the left retrotrapezoid nucleus.** The RTN is a
    **respiratory chemoreceptor** — **NOT** a sleep-promoting
    center.
*   **NOT the left RVLM or left CVLM.** Those are **autonomic**
    structures.
*   **NOT the left facial nucleus.** The facial nucleus is a
    **branchial motor** nucleus in the **pons** — **NOT** a
    sleep-promoting medullary region.
*   **NOT the left ventral respiratory group or left
    respiratory_center.** Those are **respiratory** structures.
*   **NOT the left solitary nucleus.** The solitary nucleus is
    the **visceral afferent sensory** relay.
*   **NOT the left medullary pyramid, left olivary body, left
    arcuate nucleus, or left cranial nerve nuclei.** Those are
    **white-matter motor tract**, **cerebellar relay**,
    **chemosensory nucleus**, and **motor nuclei** respectively.
*   **No ``AREA_PATHS`` hop.** The left parafacial zone is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The left parafacial zone has
    no nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the right parafacial zone — strict
    mirror with NO warning.** The left and right modules are
    **structurally identical** — same leaf status, same
    **sleep-promoting** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.parafacial_zone import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "parafacial_zone.left"
    )

**Do not** assume the left parafacial zone is the **right
parafacial zone**. The right parafacial zone is the **separate
leaf** at ``.../parafacial_zone/right/``.

**Do not** assume the left parafacial zone is the **left
parafacial respiratory group (pFRG)**. The **pFRG** is a
**respiratory** structure — **NOT** a sleep-promoting center.

**Do not** assume the left parafacial zone is the **left
retrotrapezoid nucleus**. The **RTN** is a **respiratory
chemoreceptor** — **NOT** a sleep-promoting center.

**Do not** assume the left parafacial zone is the **left RVLM**
or **left CVLM**. Those are **autonomic** structures.

**Do not** assume the left parafacial zone is the **left facial
nucleus**. The facial nucleus is a **branchial motor** nucleus
in the **pons** — **NOT** a sleep-promoting medullary region.

**Do not** assume the left parafacial zone is the **left
ventral respiratory group** or **left respiratory_center**.
Those are **respiratory** structures.

**Do not** assume the left parafacial zone is the **left
solitary nucleus**, **left medullary pyramid**, **left olivary
body**, **left arcuate nucleus**, or **left cranial nerve
nuclei**. Each is a **different structure**.

**Do not** assume the left parafacial zone has **structural
children**. It is a **leaf** — it represents the left parafacial
zone as a **single structure**.

Iterating the left parafacial zone's (empty) children
(recommended consumer pattern)::

    LEFT_PARAFACIAL_ZONE_CHILDREN = ()
    # The left parafacial zone is a leaf. It has no structural
    # children.

Reaching the right parafacial zone (recommended consumer
pattern — the contralateral leaf)::

    # The right parafacial zone is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone.right
    #
    # The left and right parafacial zones are structurally
    # symmetric mirror pairs with bilateral projections to the
    # basal forebrain and lateral hypothalamus.

Reaching the left retrotrapezoid nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The left retrotrapezoid nucleus is a respiratory
    # chemoreceptor, NOT the sleep-promoting left parafacial
    # zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.left
    #
    # The RTN and the parafacial zone are anatomically adjacent
    # in the left rostral ventrolateral medulla — but they are
    # functionally distinct.

Reaching the left RVLM (recommended consumer pattern — NOTE the
DIFFERENT structure)::

    # The left RVLM is a sympathetic premotor / vasomotor center,
    # NOT the sleep-promoting left parafacial zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #
    # The left RVLM and the left parafacial zone are anatomically
    # adjacent in the left rostral ventrolateral medulla — but
    # they are functionally distinct.

Reaching the left facial nucleus (recommended consumer pattern
— NOTE the DIFFERENT container)::

    # The left facial nucleus is a branchial motor nucleus in
    # the PONS, NOT the sleep-promoting left parafacial zone:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.facial_nerve_nucleus
    #
    # The left parafacial zone is named after its position BESIDE
    # the left facial nucleus ("parafacial" = "beside the facial
    # nucleus") — but it is a DIFFERENT structure with a
    # DIFFERENT function.

Reaching the left ventral respiratory group and left
respiratory_center (recommended consumer pattern — NOTE the
DIFFERENT structures)::

    # The left ventral respiratory group and the left
    # respiratory_center are RESPIRATORY structures, NOT the
    # sleep-promoting left parafacial zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.left
    #
    # The left parafacial zone is a SLEEP-PROMOTING region — it
    # is NOT a respiratory structure.

Reaching the left parafacial respiratory group (pFRG) — NOTE
the NAME COLLISION::

    # The left parafacial respiratory group (pFRG) is a
    # RESPIRATORY structure — often grouped with the left
    # retrotrapezoid nucleus as the left RTN/pFRG complex. It is
    # NOT wired as a separate module in this tree — it is
    # documented as part of the left RTN/pFRG complex under:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.left
    #
    # Consumers must NOT conflate the left parafacial zone
    # (sleep-promoting) with the left parafacial respiratory
    # group (respiratory).

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"parafacial_zone.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Parafacial zone — sleep-promoting center:** Anaclet, C.,
    et al. (2012). "The GABAergic parafacial zone is a medullary
    slow wave sleep-promoting center." *Nature Neuroscience*
    15:747–753. (Parafacial zone; GABAergic / glycinergic
    neurons; NREM sleep promotion; cortical slow-wave activity;
    projections to basal forebrain and lateral hypothalamus.)
*   **Parafacial zone — sleep-wake control:** Anaclet, C., et
    al. (2014). "Identification and characterization of a
    sleep-active region in the medullary parafacial zone."
    *Journal of Neurophysiology* 111:1897–1907. (Parafacial
    zone; sleep-active neurons; wake-promoting systems.)
*   **Parafacial zone — cortico-hypothalamic projections:**
    Anaclet, C., Fuller, P.M. (2017). "Brainstem regulation of
    slow-wave sleep." *Current Opinion in Neurobiology*
    44:131–138. (Parafacial zone; slow-wave sleep; projections
    to basal forebrain and lateral hypothalamus.)
*   **Parafacial respiratory group (contrast — respiratory):**
    Janczewski, W.A., Feldman, J.L. (2006). "Distinct rhythm
    generators for inspiration and expiration in the neonatal
    rat." *Journal of Physiology* 570:407–420. (Parafacial
    respiratory group; pre-inspiratory neurons; active
    expiration; RTN/pFRG complex.)
*   **RTN/pFRG complex (contrast — respiratory chemoreceptor):**
    Guyenet, P.G., et al. (2010). "The retrotrapezoid nucleus,
    central chemoreception and arterial pressure regulation."
    *Journal of Physiology* 588:47–58. (RTN/pFRG complex;
    central chemoreception; active expiration — DIFFERENT from
    the parafacial zone.)
*   **Retrotrapezoid nucleus (contrast — respiratory
    chemoreceptor):** Guyenet, P.G., Stornetta, R.L., Bayliss,
    D.A. (2008). "Central respiratory chemoreception: the
    retrotrapezoid nucleus." *Trends in Neurosciences*
    31:565–573. (RTN; CO₂/H⁺ chemoreception — DIFFERENT from
    the parafacial zone.)
*   **RVLM (contrast — sympathetic premotor):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure."
    *Nature Reviews Neuroscience* 7:335–346. (RVLM; sympathetic
    premotor neurons — DIFFERENT from the parafacial zone.)
*   **Facial nucleus (contrast — branchial motor):** Brodal, A.
    (2010). *The Central Nervous System: Structure and Function*,
    4th ed. (Facial nucleus; branchial motor column — DIFFERENT
    from the parafacial zone.)
*   **Ventral respiratory group (contrast — respiratory
    rhythm):** Feldman, J.L., Del Negro, C.A. (2006). "Looking
    for inspiration: new perspectives on respiratory rhythm."
    *Nature Reviews Neuroscience* 7:232–242. (Ventral
    respiratory group; pre-Bötzinger complex — DIFFERENT from
    the parafacial zone.)
*   **Solitary nucleus (contrast — visceral afferent):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS as the
    visceral afferent relay — DIFFERENT from the parafacial
    zone.)
*   **Sleep-wake circuits:** Saper, C.B., Fuller, P.M. (2017).
    "Wake-sleep circuitry: an overview." *Current Opinion in
    Neurobiology* 44:186–195. (Sleep-wake circuits; wake-
    promoting systems; parafacial zone as sleep-promoting
    center.)
*   NeuroNames — Parafacial zone; FMA — Parafacial zone.
"""