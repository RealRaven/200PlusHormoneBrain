"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.parafacial_zone.right
===========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── parafacial_zone
                └── right   <-- THIS MODULE

**Primary synonym:** Right parafacial zone; right PZ; right
parafacial zone of the medulla; right parafacial sleep-promoting
zone; right GABAergic parafacial zone.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** at the **ponto-medullary
junction** — the **right** GABAergic / glycinergic neuronal
population **ventral and lateral** to the **right facial nucleus
(VII)** and **adjacent** to the **right rostral ventrolateral
medulla**. It is a **sleep-promoting center**, **NOT** a
respiratory rhythm generator, **NOT** an autonomic premotor
center, and **NOT** the **right parafacial respiratory group
(pFRG)** — though the two are **anatomically adjacent** and are
**frequently conflated** in the older literature.
**Part of:** The **parafacial_zone** bilateral container — which
is part of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../parafacial_zone/`` → **direct child**
of the parafacial_zone container. The **right** parafacial zone
is one of the **two** structural children of the container (the
other is ``left``).
**Structural children:** **None.** This is a **leaf** module. The
right parafacial zone is represented as a **single structure** —
it has **no structural children** of its own.
**Boundary status (NOT the left parafacial zone — the
contralateral leaf):** **Boundary case — the right parafacial
zone is NOT the left parafacial zone.** The **left parafacial
zone** (``.../parafacial_zone/left/``) is the **contralateral
leaf** — the parafacial zone of the **left** medulla. **They are
DIFFERENT LEAVES** — the ``left`` and ``right`` modules are the
two sides of the **bilateral container**. Consumers must **not**
conflate the **right** parafacial zone with the **left** —
resolve the left side via ``parafacial_zone.left``.
**Boundary status (NOT the right parafacial respiratory group — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the right parafacial zone (PZ) is NOT the right parafacial
respiratory group (pFRG).** The **right parafacial respiratory
group (pFRG)** is a **respiratory** structure in the **right
rostral ventrolateral medulla** — it contains
**pre-inspiratory** and **expiratory-modulating** neurons that
are **active during high metabolic demand** (exercise,
hypercapnia), and it is **often grouped** with the **right
retrotrapezoid nucleus (RTN)** as the **right RTN/pFRG** **central
chemoreceptor** complex. The **right parafacial zone (PZ)** (here)
is a **right GABAergic / glycinergic sleep-promoting** region — it
is **active during NREM sleep** and **promotes slow-wave sleep**.
**They share the name "parafacial" but are DIFFERENT STRUCTURES
with DIFFERENT FUNCTIONS** — the **right pFRG** is
**respiratory**; the **right PZ** is **sleep-promoting**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right retrotrapezoid nucleus — a
DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the right parafacial zone is NOT the right retrotrapezoid
nucleus.** The **right retrotrapezoid nucleus (RTN)**
(``.../ventral_respiratory_group/retrotrapezoid_nucleus/right/``)
is a **right respiratory chemoreceptor** at the **right ventral
medullary surface** — it senses **CO₂/H⁺** and **drives
breathing**. The **right parafacial zone** (here) is a **right
sleep-promoting** region — it is **NOT** a respiratory
chemoreceptor. They are **anatomically adjacent** in the **right
rostral ventrolateral medulla**, but they are **functionally
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the right RVLM — a DIFFERENT structure with
a DIFFERENT function):** **Boundary case — the right parafacial
zone is NOT the right rostral ventrolateral medulla (RVLM).** The
**right RVLM** (``.../rostral_ventrolateral_medulla/right/``) is
the **right sympathetic premotor / vasomotor** center — it
provides **tonic excitatory drive** to the **right
intermediolateral cell column**. The **right parafacial zone**
(here) is a **right sleep-promoting** region — it is **NOT** an
autonomic premotor center. They are **anatomically adjacent** in
the **right rostral ventrolateral medulla**, but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the right CVLM — a DIFFERENT structure with
a DIFFERENT function):** **Boundary case — the right parafacial
zone is NOT the right caudal ventrolateral medulla (CVLM).** The
**right CVLM** (``.../caudal_ventrolateral_medulla/right/``) is
the **right sympathoinhibitory** relay. The **right parafacial
zone** (here) is a **right sleep-promoting** region. Consumers
must **not** conflate the two — they are at **different
rostrocaudal levels** and have **different functions**.
**Boundary status (NOT the right facial nucleus — a DIFFERENT
structure in the PONS):** **Boundary case — the right parafacial
zone is NOT the right facial nucleus.** The **right facial nucleus
(VII)**
(``.../metencephalon/pons/cranial_nerve_nuclei/right/facial_nerve_nucleus/``)
is a **right branchial motor** nucleus in the **pons** — it
supplies the **right muscles of facial expression**. The **right
parafacial zone** (here) is **ventral and lateral** to the right
facial nucleus — it is **named after** its **position beside**
the facial nucleus ("parafacial" = "beside the facial nucleus").
But it is a **DIFFERENT STRUCTURE** with a **DIFFERENT function**
— the facial nucleus is **motor**; the parafacial zone is
**sleep-promoting**. Consumers must **not** conflate the two.
**Boundary status (NOT the right ventral respiratory group — a
DIFFERENT respiratory structure):** **Boundary case — the right
parafacial zone is NOT the right ventral respiratory group
(VRG).** The **right VRG**
(``.../ventral_respiratory_group/right/``) contains the **right
Bötzinger complex**, **right pre-Bötzinger complex**, **right
nucleus para-ambiguus**, **right nucleus retroambiguus**, **right
nucleus retrofacialis**, and **right retrotrapezoid nucleus** —
the **right respiratory rhythm** and **pattern** generators. The
**right parafacial zone** (here) is a **right sleep-promoting**
region — **NOT** a respiratory rhythm generator. Consumers must
**not** conflate the two.
**Boundary status (NOT the right respiratory_center structures —
a DIFFERENT structure):** **Boundary case — the right parafacial
zone is NOT the right respiratory_center structures.** The
**right respiratory_center**
(``.../respiratory_center/right/``) contains the **right dorsal
respiratory group**, **right area postrema**, **right
chemoreceptor trigger zone**, **right gracile nucleus**, **right
cuneate nucleus**, and **right gigantocellular reticular
nucleus** — the **right dorsal respiratory** and
**chemosensory** structures. The **right parafacial zone** (here)
is a **right sleep-promoting** region — **NOT** a respiratory or
chemosensory structure. Consumers must **not** conflate the
two.
**Boundary status (NOT the right solitary nucleus — a DIFFERENT
structure):** **Boundary case — the right parafacial zone is NOT
the right solitary nucleus.** The **right solitary nucleus (NTS)**
(``.../solitary_nucleus/right/``) is the **right visceral afferent
relay** — it receives **taste**, **baroreceptor**,
**chemoreceptor**, and **gastrointestinal** afferents. The
**right parafacial zone** (here) is a **right sleep-promoting**
region — **NOT** a visceral afferent relay. Consumers must **not**
conflate the two.
**Boundary status (NOT the right medullary pyramid — a DIFFERENT
structure):** **Boundary case — the right parafacial zone is NOT
the right medullary pyramid.** The **right medullary pyramid**
(``.../medullary_pyramid/right/``) is the **right ventral
white-matter** corticospinal / corticobulbar tract. The **right
parafacial zone** (here) is a **right grey-matter**
sleep-promoting region. Consumers must **not** conflate the two.
**Boundary status (NOT the right olivary body — a DIFFERENT
structure):** **Boundary case — the right parafacial zone is NOT
the right olivary body.** The **right olivary body**
(``.../olivary_body/right/``) is the **right cerebellar
climbing-fiber relay**. The **right parafacial zone** (here) is
a **right sleep-promoting** region. Consumers must **not**
conflate the two.
**Boundary status (NOT the right arcuate nucleus — a DIFFERENT
structure):** **Boundary case — the right parafacial zone is NOT
the right arcuate nucleus.** The **right arcuate nucleus**
(``.../arcuate_nucleus/right/``) is a **right ventral-surface
chemosensory and hypothalamic-projecting** nucleus. The **right
parafacial zone** (here) is a **right sleep-promoting** region.
Consumers must **not** conflate the two.
**Boundary status (NOT the right cranial nerve nuclei — DIFFERENT
structures):** **Boundary case — the right parafacial zone is NOT
the right cranial nerve nuclei.** The **right cranial nerve
nuclei** (``.../cranial_nerve_nuclei/right/``) are the **right
medullary motor** nuclei (hypoglossal, dorsal motor vagus,
inferior salivatory, nucleus ambiguus). The **right parafacial
zone** (here) is a **right sleep-promoting** region — **NOT** a
cranial nerve motor nucleus. Consumers must **not** conflate the
two.
**Boundary status (NOT the whole right medulla oblongata — a
small grey-matter region within it):** **Boundary case — the
right parafacial zone is NOT the whole right medulla oblongata.**
The **medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the right cranial nerve
nuclei, the right autonomic nuclei, the right respiratory centers,
the right olivary body, the right medullary pyramid, the right
arcuate nucleus, the right parafacial zone (here), and other
structures. The **right parafacial zone** is **one small
grey-matter region** within the right medulla. Consumers must
**not** conflate the **right parafacial zone** with the **whole
right medulla**.

Overview
--------
The **right parafacial zone (PZ)** is a **right GABAergic /
glycinergic** grey-matter region at the **ponto-medullary
junction** — **ventral and lateral** to the **right facial
nucleus (VII)** and **adjacent** to the **right rostral
ventrolateral medulla (RVLM)**. It is a **sleep-promoting
center** — it is **active during NREM sleep**, and it
**promotes slow-wave sleep (SWS)** by **inhibiting** the
**wake-promoting** systems of the **basal forebrain**, **lateral
hypothalamus**, and **brainstem**.

**This is a LEAF module.** The **right parafacial zone** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **side-specific** resolution of
the right parafacial zone use this module; consumers that need
the **left-side** resolution use
``.../parafacial_zone/left/``; consumers that need the **whole
parafacial_zone container** use ``.../parafacial_zone/``.

**The right parafacial zone is the SLEEP-PROMOTING right
parafacial zone, NOT the right parafacial respiratory group.**
The **right parafacial respiratory group (pFRG)** is a
**respiratory** structure — part of the **right RTN/pFRG**
**central chemoreceptor** complex — **NOT** a sleep-promoting
center. **They share the name "parafacial" but are DIFFERENT
STRUCTURES with DIFFERENT FUNCTIONS** — the **right pFRG** is
**respiratory**; the **right PZ** is **sleep-promoting**. In
older literature, the two are **frequently conflated**; modern
work (Anaclet et al., 2012) has **dissociated** them.

**The right parafacial zone is a GREY-MATTER sleep-promoting
region, NOT a respiratory rhythm generator, NOT an autonomic
premotor center, and NOT a cranial nerve motor nucleus.** It
**contains** a **GABAergic / glycinergic** neuronal population
that **projects** to the **right and left basal forebrain**,
the **right and left lateral hypothalamus** (including **MCH
neurons**), and other **wake-promoting** centers, and it
**promotes NREM sleep**.

**The right parafacial zone is a NAME-COLLISION HAZARD.** The
name "parafacial" appears in **two different structures** — the
**right parafacial zone (PZ)** and the **right parafacial
respiratory group (pFRG)** — and the two are **often conflated**
in the literature. Consumers must **not** import the
**respiratory** function of the **right pFRG** into the **right
parafacial zone** — the right parafacial zone is a
**sleep-promoting** center.

The Right Parafacial Zone / Left Parafacial Zone Boundary
---------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right parafacial zone** (this module) — the parafacial zone
    of the **right** medulla.

*   **Left parafacial zone** (``.../parafacial_zone/left/``) —
    the parafacial zone of the **left** medulla.

**The two are the SIDES of the bilateral parafacial_zone
container.** They are **structurally symmetric mirror pairs** —
same cytoarchitecture, same projections, same **no warning**.
Consumers must **not** conflate the right with the left — resolve
the left side via ``parafacial_zone.left``.

The Right Parafacial Zone / Right Parafacial Respiratory Group Boundary
-----------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Right parafacial zone (PZ)** (this module) — the **right
    sleep-promoting** GABAergic region.

*   **Right parafacial respiratory group (pFRG)** — the **right
    respiratory** structure in the **right rostral ventrolateral
    medulla** (often grouped with the **right RTN** as the
    **right RTN/pFRG** complex).

**They share the name "parafacial" but are DIFFERENT STRUCTURES
with DIFFERENT FUNCTIONS.** The **right pFRG** is **respiratory**
(active expiration, pre-inspiratory neurons); the **right PZ** is
**sleep-promoting**. Consumers must **not** conflate the two.

The Right Parafacial Zone / Right Retrotrapezoid Nucleus Boundary
-----------------------------------------------------------------
This is the **sleep / respiratory-chemoreceptor** boundary:

*   **Right parafacial zone** (this module) — the **right
    sleep-promoting** region.

*   **Right retrotrapezoid nucleus (RTN)**
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/right/``)
    — the **right respiratory chemoreceptor**.

**They are anatomically adjacent** in the **right rostral
ventrolateral medulla**, but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Right Parafacial Zone / Right RVLM Boundary
-----------------------------------------------
This is the **sleep / autonomic-premotor** boundary:

*   **Right parafacial zone** (this module) — the **right
    sleep-promoting** region.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``)
    — the **right sympathetic premotor / vasomotor** center.

**They are anatomically adjacent** in the **right rostral
ventrolateral medulla**, but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Right Parafacial Zone / Right Facial Nucleus Boundary
---------------------------------------------------------
This is the **medulla / pons** and **sleep / motor** boundary:

*   **Right parafacial zone** (this module) — the **right
    sleep-promoting** region.

*   **Right facial nucleus (VII)**
    (``.../metencephalon/pons/cranial_nerve_nuclei/right/facial_nerve_nucleus/``)
    — the **right branchial motor** nucleus for the **right
    muscles of facial expression**.

**They are anatomically adjacent** — the right parafacial zone is
**named after** its position **beside** the right facial nucleus.
But they are **DIFFERENT STRUCTURES** — the **right facial
nucleus** is **motor**; the **right parafacial zone** is
**sleep-promoting**. Consumers must **not** conflate the two.

The Right Parafacial Zone / Right Ventral Respiratory Group Boundary
--------------------------------------------------------------------
This is the **sleep / respiratory-rhythm** boundary:

*   **Right parafacial zone** (this module) — the **right
    sleep-promoting** region.

*   **Right ventral respiratory group (VRG)**
    (``.../ventral_respiratory_group/right/``) — the **right
    respiratory rhythm and pattern** generators.

**They are functionally distinct.** Consumers must **not**
conflate the two.

The Right Parafacial Zone / Right Respiratory Center Boundary
-------------------------------------------------------------
This is the **sleep / dorsal-respiratory** boundary:

*   **Right parafacial zone** (this module) — the **right
    sleep-promoting** region.

*   **Right respiratory center**
    (``.../respiratory_center/right/``) — the **right dorsal
    respiratory** and **chemosensory** structures.

**They are functionally distinct.** Consumers must **not**
conflate the two.

The Right Parafacial Zone / Right Solitary Nucleus Boundary
-----------------------------------------------------------
This is the **sleep / visceral-sensory** boundary:

*   **Right parafacial zone** (this module) — the **right
    sleep-promoting** region.

*   **Right solitary nucleus** (``.../solitary_nucleus/right/``) —
    the **right visceral afferent sensory** relay.

**They are functionally distinct.** Consumers must **not**
conflate the two.

The Right Parafacial Zone / Right Medullary Pyramid, Right Olivary Body, Right Arcuate Nucleus, and Right Cranial Nerve Nuclei Boundary
--------------------------------------------------------------------------------------------------------------------------------------
This is the **sleep / white-matter, cerebellar-relay,
chemosensory, and motor** boundary:

*   **Right parafacial zone** (this module) — the **right
    sleep-promoting** region.

*   **Right medullary pyramid**
    (``.../medullary_pyramid/right/``) — the **right
    white-matter** corticospinal / corticobulbar tract.

*   **Right olivary body** (``.../olivary_body/right/``) — the
    **right cerebellar climbing-fiber relay**.

*   **Right arcuate nucleus** (``.../arcuate_nucleus/right/``) —
    the **right ventral-surface chemosensory** nucleus.

*   **Right cranial nerve nuclei**
    (``.../cranial_nerve_nuclei/right/``) — the **right medullary
    motor** nuclei.

**They are functionally distinct** from the **right parafacial
zone**. Consumers must **not** conflate the right parafacial zone
with any of these structures.

Function in the Human Brain
---------------------------
The right parafacial zone's function is **sleep promotion** —
**NOT respiratory rhythm**, **NOT autonomic regulation**, and
**NOT motor control**:

*   **Right NREM sleep promotion:** The **right parafacial zone**
    is **active during NREM sleep** (especially **slow-wave
    sleep**) and **promotes** NREM sleep onset and maintenance.

*   **Inhibition of wake-promoting systems (right side):** The
    **right parafacial zone** **projects** to the **right and
    left basal forebrain**, the **right and left lateral
    hypothalamus** (including **MCH neurons**), and other
    **wake-promoting** centers, and it **inhibits** them —
    thereby **promoting sleep**.

*   **Slow-wave sleep (SWS) generation (right side):** The
    **right parafacial zone** contributes to the **cortical
    slow-wave activity** that characterizes **NREM sleep** —
    its **GABAergic output** **modulates** the **cortical** and
    **thalamocortical** circuits that generate **slow waves**.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** (VRG) — **NOT**
    the right parafacial zone.

*   **NOT autonomic regulation:** The **autonomic regulation**
    is the **RVLM**, **CVLM**, and **NTS** — **NOT** the right
    parafacial zone.

*   **NOT motor control:** The **motor control** is the
    **corticospinal tract** (via the **medullary pyramid**) and
    the **cranial nerve motor nuclei** — **NOT** the right
    parafacial zone.

**The unifying theme:** the right parafacial zone is a **right
GABAergic / glycinergic sleep-promoting region** at the
**ponto-medullary junction** — it **promotes NREM sleep** and
**slow-wave sleep** by **inhibiting wake-promoting systems**.

Associated Disorders
--------------------
The right parafacial zone has **no named clinical syndrome** of
its own — its clinical associations are **indirect**, via
**sleep regulation**:

*   **Insomnia (via right parafacial zone dysfunction —
    hypothesized):** **Reduced** right parafacial zone
    **GABAergic** output — or **impaired** right parafacial zone
    **inhibition** of **wake-promoting** systems — could
    contribute to **insomnia**. This is **speculative** and
    **not** a well-established clinical entity.

*   **Sleep-wake disorders (via right parafacial zone
    dysfunction — hypothesized):** **Abnormal** right parafacial
    zone **activity** — or **altered** right parafacial zone
    **connectivity** with the **basal forebrain** and **lateral
    hypothalamus** — could contribute to **sleep-wake
    dysregulation**. This is **speculative**.

*   **Sudden infant death syndrome (SIDS — via adjacent
    structures):** **SIDS** has been associated with
    **abnormalities** in the **medullary** **serotonergic**
    system — **including** regions **adjacent** to the **right
    parafacial zone**. The **right parafacial zone** itself is
    **not** a primary SIDS substrate, but it is **anatomically
    adjacent** to the **ventral medullary** regions implicated
    in **SIDS**.

*   **No Named "Right Parafacial Zone Syndrome":** The right
    parafacial zone is a **functionally defined region** — it
    has **no named clinical syndrome** of its own.

**What is NOT here:** The right parafacial zone is **not** the
substrate for **respiratory rhythm** (pre-Bötzinger complex,
VRG), **central hypoventilation** (RTN, VRG), **autonomic
dysfunction** (RVLM, CVLM, NTS), or **cranial nerve motor
deficits** (cranial nerve nuclei). Its clinical relevance is
the **sleep-regulation** functions listed above.

Lateralization Notes
--------------------
This is the **right** parafacial zone module. The parafacial
zone is a **bilateral container** whose two sides are
**structurally symmetric mirror pairs** — and it carries **NO
warning**:

*   **Bilateral Symmetry:** The **right** and **left**
    parafacial zones are **structurally symmetric** — they are
    **mirror pairs** with the **same** cytoarchitecture, **same**
    projections, and **same** functions. The **right** parafacial
    zone **promotes NREM sleep** via **bilateral** projections
    to the **basal forebrain** and **lateral hypothalamus**;
    the **left** parafacial zone does the same.

*   **NO Lateralization Warning:** The parafacial zone has **no
    known functional lateralization** in humans. Consumers must
    **not** import a **lateralization warning** into the right
    parafacial zone — the **right** and **left** sides are
    **functionally equivalent**.

*   **NO Extended-Amygdala / SLEA Warning:** The right parafacial
    zone is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the right parafacial zone.

*   **NO Fear-Output Warning:** The right parafacial zone is
    **not** a fear-output structure — it is a **right
    sleep-promoting** region. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "right parafacial zone = left
parafacial zone" will be structurally correct** — the two sides
are **symmetric** and **functionally equivalent** at the
**region level**. The parafacial zone is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no fear-output
warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right parafacial zone is
    a **leaf** — it does **not** import from ``.../left/`` or
    any other left-side module. Bilateral relationships are
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
    any other container. The right parafacial zone's
    relationships to the right parafacial respiratory group
    (pFRG), right retrotrapezoid nucleus, right RVLM, right
    CVLM, right facial nucleus, right VRG, right
    respiratory_center, right solitary nucleus, right medullary
    pyramid, right olivary body, right arcuate nucleus, and right
    cranial nerve nuclei are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right
    parafacial zone is a **single structure** — it has **no
    structural children**. Consumers must **not** expect further
    sub-paths under ``.../right/``.
*   **NOT the left parafacial zone.** The left parafacial zone
    is a **separate leaf** under ``.../parafacial_zone/left/``.
    Consumers must **not** conflate the right with the left.
*   **NOT the right parafacial respiratory group (pFRG).** The
    pFRG is a **respiratory** structure — **NOT** a
    sleep-promoting center.
*   **NOT the right retrotrapezoid nucleus.** The RTN is a
    **respiratory chemoreceptor** — **NOT** a sleep-promoting
    center.
*   **NOT the right RVLM or right CVLM.** Those are **autonomic**
    structures.
*   **NOT the right facial nucleus.** The facial nucleus is a
    **branchial motor** nucleus in the **pons** — **NOT** a
    sleep-promoting medullary region.
*   **NOT the right ventral respiratory group or right
    respiratory_center.** Those are **respiratory** structures.
*   **NOT the right solitary nucleus.** The solitary nucleus is
    the **visceral afferent sensory** relay.
*   **NOT the right medullary pyramid, right olivary body, right
    arcuate nucleus, or right cranial nerve nuclei.** Those are
    **white-matter motor tract**, **cerebellar relay**,
    **chemosensory nucleus**, and **motor nuclei** respectively.
*   **No ``AREA_PATHS`` hop.** The right parafacial zone is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The right parafacial zone has
    no nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the left parafacial zone — strict
    mirror with NO warning.** The right and left modules are
    **structurally identical** — same leaf status, same
    **sleep-promoting** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.parafacial_zone import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "parafacial_zone.right"
    )

**Do not** assume the right parafacial zone is the **left
parafacial zone**. The left parafacial zone is the **separate
leaf** at ``.../parafacial_zone/left/``.

**Do not** assume the right parafacial zone is the **right
parafacial respiratory group (pFRG)**. The **pFRG** is a
**respiratory** structure — **NOT** a sleep-promoting center.

**Do not** assume the right parafacial zone is the **right
retrotrapezoid nucleus**. The **RTN** is a **respiratory
chemoreceptor** — **NOT** a sleep-promoting center.

**Do not** assume the right parafacial zone is the **right RVLM**
or **right CVLM**. Those are **autonomic** structures.

**Do not** assume the right parafacial zone is the **right facial
nucleus**. The facial nucleus is a **branchial motor** nucleus
in the **pons** — **NOT** a sleep-promoting medullary region.

**Do not** assume the right parafacial zone is the **right
ventral respiratory group** or **right respiratory_center**.
Those are **respiratory** structures.

**Do not** assume the right parafacial zone is the **right
solitary nucleus**, **right medullary pyramid**, **right olivary
body**, **right arcuate nucleus**, or **right cranial nerve
nuclei**. Each is a **different structure**.

**Do not** assume the right parafacial zone has **structural
children**. It is a **leaf** — it represents the right parafacial
zone as a **single structure**.

Iterating the right parafacial zone's (empty) children
(recommended consumer pattern)::

    RIGHT_PARAFACIAL_ZONE_CHILDREN = ()
    # The right parafacial zone is a leaf. It has no structural
    # children.

Reaching the left parafacial zone (recommended consumer
pattern — the contralateral leaf)::

    # The left parafacial zone is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone.left
    #
    # The right and left parafacial zones are structurally
    # symmetric mirror pairs with bilateral projections to the
    # basal forebrain and lateral hypothalamus.

Reaching the right retrotrapezoid nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The right retrotrapezoid nucleus is a respiratory
    # chemoreceptor, NOT the sleep-promoting right parafacial
    # zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.right
    #
    # The RTN and the parafacial zone are anatomically adjacent
    # in the right rostral ventrolateral medulla — but they are
    # functionally distinct.

Reaching the right RVLM (recommended consumer pattern — NOTE the
DIFFERENT structure)::

    # The right RVLM is a sympathetic premotor / vasomotor center,
    # NOT the sleep-promoting right parafacial zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #
    # The right RVLM and the right parafacial zone are anatomically
    # adjacent in the right rostral ventrolateral medulla — but
    # they are functionally distinct.

Reaching the right facial nucleus (recommended consumer pattern
— NOTE the DIFFERENT container)::

    # The right facial nucleus is a branchial motor nucleus in
    # the PONS, NOT the sleep-promoting right parafacial zone:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.facial_nerve_nucleus
    #
    # The right parafacial zone is named after its position BESIDE
    # the right facial nucleus ("parafacial" = "beside the facial
    # nucleus") — but it is a DIFFERENT structure with a
    # DIFFERENT function.

Reaching the right ventral respiratory group and right
respiratory_center (recommended consumer pattern — NOTE the
DIFFERENT structures)::

    # The right ventral respiratory group and the right
    # respiratory_center are RESPIRATORY structures, NOT the
    # sleep-promoting right parafacial zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.right
    #
    # The right parafacial zone is a SLEEP-PROMOTING region — it
    # is NOT a respiratory structure.

Reaching the right parafacial respiratory group (pFRG) — NOTE
the NAME COLLISION::

    # The right parafacial respiratory group (pFRG) is a
    # RESPIRATORY structure — often grouped with the right
    # retrotrapezoid nucleus as the right RTN/pFRG complex. It is
    # NOT wired as a separate module in this tree — it is
    # documented as part of the right RTN/pFRG complex under:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.right
    #
    # Consumers must NOT conflate the right parafacial zone
    # (sleep-promoting) with the right parafacial respiratory
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