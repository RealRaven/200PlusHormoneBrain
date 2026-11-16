"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.left
=======================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── caudal_ventrolateral_medulla
                └── left   <-- THIS MODULE

**Primary synonym:** Left caudal ventrolateral medulla; left CVLM;
left caudal ventrolateral medullary region; left caudal
ventrolateral medullary depressor area.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** — a group of **functionally
defined neurons** in the **left caudal ventrolateral medulla**,
**ventral and lateral** to the **left nucleus ambiguus** and the
**left lateral reticular nucleus**, **caudal** to the **left
RVLM** and **rostral** to the **spinomedullary junction**. It is
the **left sympathoinhibitory relay** — the left **CVLM** of the
**medullary autonomic circuit**.
**Part of:** The **caudal_ventrolateral_medulla** bilateral
container — which is part of the **medulla oblongata** — the
**caudal brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../caudal_ventrolateral_medulla/`` →
**direct child** of the caudal_ventrolateral_medulla container.
The **left** CVLM is one of the **two** structural children of the
container (the other is ``right``).
**Structural children:** **None.** This is a **leaf** module. The
left CVLM is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the right CVLM — the contralateral leaf):**
**Boundary case — the left CVLM is NOT the right CVLM.** The
**right CVLM** (``.../caudal_ventrolateral_medulla/right/``) is
the **contralateral leaf** — the CVLM of the **right** medulla.
**They are DIFFERENT LEAVES** — the ``left`` and ``right`` modules
are the two sides of the **bilateral container**. Consumers must
**not** conflate the **left** CVLM with the **right** CVLM —
resolve the right side via
``caudal_ventrolateral_medulla.right``.
**Boundary status (NOT the left RVLM — the RVLM is the ROSTRAL
ventrolateral medulla):** **Boundary case — the left CVLM is NOT
the left RVLM.** The **left RVLM**
(``.../rostral_ventrolateral_medulla/left/``) is the **left
rostral** ventrolateral medulla — the **left sympathetic premotor
/ vasomotor center** that provides **tonic excitatory drive** to
the **left intermediolateral cell column**. The **left CVLM**
(here) is the **left caudal** ventrolateral medulla — the **left
sympathoinhibitory relay** that **inhibits the left RVLM**.
**They are DIFFERENT STRUCTURES at DIFFERENT rostrocaudal
levels** — the **left RVLM** is **rostral**; the **left CVLM** is
**caudal**. Consumers must **not** conflate the two — the **left
RVLM** **drives** sympathetic outflow; the **left CVLM**
**inhibits** it.
**Boundary status (NOT the left arcuate nucleus — a
ventral-surface nucleus):** **Boundary case — the left CVLM is
NOT the left arcuate nucleus.** The **left arcuate nucleus**
(``.../arcuate_nucleus/left/``) is a **ventral-surface
chemosensory and hypothalamic-projecting** nucleus at the **left
ventral medullary surface**, adjacent to the **anterior median
fissure**. The **left CVLM** (here) is a **more lateral** left
ventrolateral medullary region — it is **NOT** the left arcuate
nucleus. **They are DIFFERENT STRUCTURES** — the **left arcuate
nucleus** is a **ventral-surface** nucleus; the **left CVLM** is
a **ventrolateral** region. Consumers must **not** conflate the
two.
**Boundary status (NOT the left solitary nucleus — the NTS is
the visceral afferent relay):** **Boundary case — the left CVLM
is NOT the left solitary nucleus.** The **left solitary nucleus**
(NTS) (``.../solitary_nucleus/left/``) is the **left visceral
afferent relay** — it receives **baroreceptor**,
**chemoreceptor**, and **gastrointestinal** afferents. The
**left CVLM** (here) is the **left sympathoinhibitory relay** —
it **receives left NTS input** and **inhibits the left RVLM**.
**They are DIFFERENT STRUCTURES** — the **left NTS** is the
**afferent** relay; the **left CVLM** is the
**sympathoinhibitory** relay. Consumers must **not** conflate the
two.
**Boundary status (NOT the left retrotrapezoid nucleus — that is
a respiratory chemoreceptor):** **Boundary case — the left CVLM
is NOT the left retrotrapezoid nucleus.** The **left
retrotrapezoid nucleus** (RTN) is a **more rostral**
ventral-surface **respiratory chemoreceptor** — it is wired under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/left/``.
The **left CVLM** (here) is a **left caudal ventrolateral**
**sympathoinhibitory relay**. **They are DIFFERENT STRUCTURES** —
the **left RTN** is a **respiratory chemoreceptor**; the **left
CVLM** is a **sympathoinhibitory** relay. Consumers must **not**
conflate the two.
**Boundary status (NOT the left ventrolateral medulla as a whole
— a specific rostrocaudal subdivision):** **Boundary case — the
left CVLM is NOT the whole left ventrolateral medulla (VLM).**
The **left ventrolateral medulla** is a **region** containing
the **left RVLM**, the **left CVLM**, and the **left arcuate
nucleus**. The **left CVLM** (here) is the **left caudal**
subdivision — it is **NOT** the whole **left VLM**, and it is
**NOT** the **left RVLM** or the **left arcuate nucleus**.
Consumers must **not** conflate the **left CVLM** with the
**whole left ventrolateral medulla**.
**Boundary status (NOT the left medullary pyramid — adjacent but
distinct):** **Boundary case — the left CVLM is NOT the left
medullary pyramid.** The **left medullary pyramid**
(``.../medullary_pyramid/left/``) is the **left corticospinal /
corticobulbar tract** — a **white-matter** structure at the
**left ventral medulla**. The **left CVLM** (here) is a
**grey-matter** region in the **left caudal ventrolateral
medulla**. **They are DIFFERENT STRUCTURES** — the pyramid is
**white matter** (descending motor fibers); the **left CVLM** is
**grey matter** (neurons). Consumers must **not** conflate the
two.
**Boundary status (NOT the left olivary body — adjacent but
distinct):** **Boundary case — the left CVLM is NOT the left
olivary body.** The **left olivary body**
(``.../olivary_body/left/``) contains the **left inferior
olivary nucleus** — the **sole source of climbing fibers** to
the **left cerebellar hemisphere**. The **left CVLM** (here) is
a **left ventrolateral medullary sympathoinhibitory** region.
**They are DIFFERENT STRUCTURES** — the left olivary body is a
**cerebellar relay**; the **left CVLM** is a
**sympathoinhibitory** relay. Consumers must **not** conflate the
two.
**Boundary status (NOT the left nucleus ambiguus — adjacent but
distinct):** **Boundary case — the left CVLM is NOT the left
nucleus ambiguus.** The **left nucleus ambiguus**
(``.../cranial_nerve_nuclei/left/nucleus_ambiguus/``) is a
**left branchial motor** nucleus (CN IX/X/XI) **dorsal** to the
left CVLM. The **left CVLM** (here) is a **left ventrolateral
sympathoinhibitory** region. **They are DIFFERENT STRUCTURES** —
the left nucleus ambiguus is a **motor nucleus**; the **left
CVLM** is a **sympathoinhibitory** region. Consumers must **not**
conflate the two.
**Boundary status (NOT the spinal cord — that begins at the
foramen magnum):** **Boundary case — the left CVLM is NOT the
spinal cord.** The **spinal cord** (``.../spinal_cord/``) is a
**separate container** beginning at the **foramen magnum**. The
**left CVLM** (here) is a **medullary** region — its **caudal
boundary** is the **spinomedullary junction** (the **pyramidal
decussation**). Consumers must **not** conflate the **left
CVLM** with the **spinal cord**.

Overview
--------
The **left CVLM** is the **left caudal ventrolateral medulla** —
the **left sympathoinhibitory relay** of the **left medullary
autonomic circuit**. It lies **ventrolateral** in the **left
caudal medulla**, **caudal** to the **left RVLM** and **rostral**
to the **spinomedullary junction**, and it **inhibits the left
RVLM** in response to **baroreceptor** and **visceral** input
relayed by the **left NTS**.

**This is a LEAF module.** The **left CVLM** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution of the left side
use this module; consumers that need **right-side** resolution
use ``.../caudal_ventrolateral_medulla/right/``; consumers that
need **bilateral** resolution iterate over both.

**The left CVLM is the LEFT caudal ventrolateral medulla, NOT the
left rostral one.** The **left RVLM** is **rostral**; the **left
CVLM** is **caudal**. **They are DIFFERENT STRUCTURES at
DIFFERENT rostrocaudal levels** — the **left RVLM** **drives**
sympathetic outflow; the **left CVLM** **inhibits** it.

**The left CVLM is functionally coupled to the left NTS and left
RVLM in the left medullary baroreflex circuit.** The **left NTS**
receives **baroreceptor** afferents; the **left CVLM** receives
**left NTS** input and **inhibits the left RVLM**; the **left
RVLM** drives **left sympathetic outflow**. This is the **left
medullary baroreflex arc** — a **three-structure circuit**
(left NTS → left CVLM → left RVLM).

**The left CVLM is NOT the left arcuate nucleus, the left RTN,
the left nucleus ambiguus, the left medullary pyramid, or the
left olivary body.** Each is a **different structure** in the
**left caudal ventrolateral medulla region**.

The Left CVLM / Right CVLM Boundary
-----------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left CVLM** (this module) — the CVLM of the **left** medulla.

*   **Right CVLM** (``.../caudal_ventrolateral_medulla/right/``) —
    the CVLM of the **right** medulla.

**The two are the SIDES of the bilateral CVLM container.** They
are **structurally symmetric mirror pairs** — same
cytoarchitecture, same ipsilateral projections, same functions.
Consumers must **not** conflate the left with the right — resolve
the right side via ``caudal_ventrolateral_medulla.right``.

The Left CVLM / Left RVLM Boundary
----------------------------------
This is the **most consequential** rostrocaudal boundary:

*   **Left CVLM** (this module) — the **left caudal**
    ventrolateral medulla — the **left sympathoinhibitory
    relay**.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``) —
    the **left rostral** ventrolateral medulla — the **left
    sympathetic premotor / vasomotor center**.

**The two are ROSTROCAUDAL SIBLINGS of the left ventrolateral
medulla.** The **left RVLM** **drives** sympathetic outflow; the
**left CVLM** **inhibits** it. Consumers must **not** conflate
the two — the **left RVLM** is **rostral**; the **left CVLM** is
**caudal**.

The Left CVLM / Left NTS Boundary
---------------------------------
This is the **autonomic-circuit** boundary:

*   **Left CVLM** (this module) — the **left sympathoinhibitory
    relay**.

*   **Left NTS** (``.../solitary_nucleus/left/``) — the **left
    visceral afferent relay**.

**The left NTS is UPSTREAM of the left CVLM in the left medullary
baroreflex arc.** The **left NTS** receives **baroreceptor**
afferents and **projects** to the **left CVLM**; the **left
CVLM** **inhibits the left RVLM**. Consumers must **not**
conflate the **left NTS** with the **left CVLM** — the **left
NTS** is the **afferent** relay; the **left CVLM** is the
**sympathoinhibitory** relay.

The Left CVLM / Left Arcuate Nucleus Boundary
---------------------------------------------
This is the **ventral-surface** boundary:

*   **Left CVLM** (this module) — the **left caudal ventrolateral
    medulla** (more **lateral**).

*   **Left arcuate nucleus** (``.../arcuate_nucleus/left/``) — a
    **ventral-surface chemosensory and hypothalamic-projecting**
    nucleus (more **medial**, at the **left ventral surface**).

**They are DIFFERENT STRUCTURES in the left ventrolateral
medullary region.** Consumers must **not** conflate the **left
CVLM** with the **left arcuate nucleus**.

The Left CVLM / Left Retrotrapezoid Nucleus Boundary
----------------------------------------------------
This is the **respiratory-chemoreceptor** boundary:

*   **Left CVLM** (this module) — the **left caudal
    ventrolateral sympathoinhibitory** relay.

*   **Left RTN**
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/left/``)
    — a **more rostral** left ventral-surface **respiratory
    chemoreceptor**.

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate them.

The Left CVLM / Left Medullary Pyramid and Left Olivary Body
Boundary
--------
This is the **grey-matter / white-matter and cerebellar-relay**
boundary:

*   **Left CVLM** (this module) — **grey-matter** region in the
    **left caudal ventrolateral medulla**.

*   **Left medullary pyramid**
    (``.../medullary_pyramid/left/``) — **white-matter** left
    corticospinal / corticobulbar tract.

*   **Left olivary body** (``.../olivary_body/left/``) — contains
    the **left inferior olivary nucleus** (left cerebellar
    climbing fibers).

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the **left CVLM** with the **left medullary pyramid** or
the **left olivary body**.

The Left CVLM / Left Nucleus Ambiguus Boundary
----------------------------------------------
This is the **motor-nucleus** boundary:

*   **Left CVLM** (this module) — a **left ventrolateral
    sympathoinhibitory** region.

*   **Left nucleus ambiguus**
    (``.../cranial_nerve_nuclei/left/nucleus_ambiguus/``) — a
    **left branchial motor** nucleus (CN IX/X/XI) **dorsal** to
    the left CVLM.

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate them.

Function in the Human Brain
---------------------------
The left CVLM's function is **left sympathoinhibition** in the
**left medullary baroreflex circuit** — **NOT sympathetic
premotor** and **NOT respiratory rhythm**:

*   **Sympathoinhibition (left medullary baroreflex):** The
    **left CVLM** receives **glutamatergic** input from the
    **left NTS** and **projects GABAergic inhibitory** fibers to
    the **left RVLM** — **inhibiting** the **left sympathetic
    premotor** neurons. This is the **left medullary baroreflex
    arc** (left NTS → left CVLM → left RVLM) that **buffers**
    blood pressure **fluctuations** on the left side.

*   **Baroreflex buffering (left side):** The **left CVLM** is
    the **key left sympathoinhibitory** node in the
    **baroreflex** — it **reduces left sympathetic outflow**
    when **blood pressure rises**, and it **withdraws**
    inhibition when **blood pressure falls**. This is a
    **critical** homeostatic mechanism, integrated with the
    right CVLM via **bilateral** coordination.

*   **Visceral reflex integration (left side):** The **left
    CVLM** integrates **visceral** input from the **left NTS**
    (baroreceptor, chemoreceptor, gastrointestinal) and
    **modulates** the **left RVLM** sympathetic drive
    accordingly.

*   **NOT left sympathetic premotor:** The **left sympathetic
    premotor** function is the **left RVLM** — **NOT** the left
    CVLM.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the left CVLM.

*   **NOT chemosensory:** The **central chemoreception**
    function is the **left ventral medullary surface** (left
    arcuate nucleus, left RTN) — **NOT** the left CVLM.

**The unifying theme:** the left CVLM is the **left caudal
ventrolateral medulla** — the **left sympathoinhibitory relay**
that **buffers** left sympathetic outflow via the **left
medullary baroreflex arc** (left NTS → left CVLM → left RVLM).
It is **NOT** the left RVLM, **NOT** the left NTS, **NOT** the
left arcuate nucleus, **NOT** the left RTN, and **NOT** the
left nucleus ambiguus.

Associated Disorders
--------------------
The left CVLM has **no named clinical syndrome** of its own —
its clinical associations are **indirect**:

*   **Neurogenic hypertension (via left CVLM dysfunction):**
    Impaired **left CVLM** sympathoinhibition — or impaired
    **left NTS → left CVLM** signaling — contributes to **left
    sympathetic overactivity** and **neurogenic hypertension**.
    The **left CVLM** is the **left sympathoinhibitory** node;
    its dysfunction **reduces** baroreflex **buffering**.

*   **Baroreflex failure (via left CVLM / left NTS / left RVLM
    circuit dysfunction):** Disruption of the **left medullary
    baroreflex arc** — including the **left CVLM** — causes
    **baroreflex failure** — **labile blood pressure**,
    **orthostatic hypotension**, and **hypertensive crises**.
    The **bilateral** integration of left and right CVLM means
    unilateral lesions may be **compensated** by the
    **contralateral** side.

*   **Brainstem stroke (via left ventrolateral medullary
    infarction):** Infarction of the **left caudal ventrolateral
    medulla** — adjacent to the **left CVLM** — can cause
    **autonomic** and **cardiovascular** instability. The
    **left CVLM** contributes to the **autonomic** component of
    **Wallenberg syndrome** (lateral medullary syndrome), though
    the **primary** lesion is in the **left lateral medulla**
    structures (left NTS, left spinothalamic tract, left nucleus
    ambiguus, left inferior cerebellar peduncle).

*   **No Named "Left CVLM Syndrome":** The left CVLM is a
    **functionally defined region** (not a sharply demarcated
    nucleus) — it has **no named clinical syndrome**. Its
    clinical relevance is **indirect**, via the **left medullary
    baroreflex** circuit.

**What is NOT here:** The left CVLM is **not** the substrate for
**central hypoventilation** (ventral medullary surface /
pre-Bötzinger complex), **Wallenberg syndrome** (lateral medulla
— left NTS, left nucleus ambiguus, left spinothalamic tract), or
**neurogenic hypertension of the RVLM type** (left RVLM). Its
clinical relevance is the **left sympathoinhibitory** and
**baroreflex** functions listed above.

Lateralization Notes
--------------------
This is the **left** CVLM module. The CVLM is a **bilateral
container** whose two sides are **structurally symmetric mirror
pairs** — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right** CVLM
    regions are **structurally symmetric** — they are **mirror
    pairs** with the **same** cytoarchitecture, **same**
    ipsilateral projections, and **same** functions. The **left**
    CVLM projects **ipsilaterally** to the **left** RVLM; the
    **right** CVLM projects **ipsilaterally** to the **right**
    RVLM.

*   **Ipsilateral Projection:** Each **CVLM** projects
    **ipsilaterally** to its **ipsilateral RVLM** —
    **left CVLM → left RVLM** and **right CVLM → right RVLM**.
    This is **functionally** an **ipsilateral** circuit; the
    bilateral **sympathoinhibition** is the **sum** of the two
    sides. **Unilateral left CVLM lesion** may be **compensated**
    by the **right** side (and vice versa).

*   **NO Lateralization Warning:** The CVLM has **no known
    functional lateralization** in humans. Consumers must **not**
    import a **lateralization warning** into the left CVLM — the
    **left** and **right** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left CVLM is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into the left
    CVLM.

*   **NO Fear-Output Warning:** The left CVLM is **not** a
    fear-output structure — it is a **left sympathoinhibitory**
    region. Consumers must **not** conflate it with the **central
    nucleus** or with the **amygdala**.

**A consumer that assumes "left CVLM = right CVLM" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent**. The CVLM is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no fear-output
warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left CVLM is a **leaf** —
    it does **not** import from ``.../right/`` or any other
    right-side module. Bilateral relationships are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../rostral_ventrolateral_medulla/``,
    ``.../arcuate_nucleus/``, ``.../solitary_nucleus/``,
    ``.../ventral_respiratory_group/``,
    ``.../medullary_pyramid/``, ``.../olivary_body/``,
    ``.../cranial_nerve_nuclei/``, or any other container. The
    left CVLM's relationships to the left RVLM, left NTS, left
    arcuate nucleus, left RTN, left medullary pyramid, left
    olivary body, and left nucleus ambiguus are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left CVLM is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../left/``.
*   **NOT the right CVLM.** The right CVLM is a **separate leaf**
    under ``.../caudal_ventrolateral_medulla/right/``. Consumers
    must **not** conflate the left with the right.
*   **NOT the left RVLM.** The left RVLM is the **left rostral**
    ventrolateral medulla — the **left sympathetic premotor**
    center. The **left CVLM** is the **left caudal** ventrolateral
    medulla — the **left sympathoinhibitory** relay. Consumers
    must **not** conflate the two.
*   **NOT the left NTS.** The left NTS is the **left visceral
    afferent** relay; the **left CVLM** is the **left
    sympathoinhibitory** relay.
*   **NOT the left arcuate nucleus.** The left arcuate nucleus is
    a **left ventral-surface chemosensory** nucleus; the **left
    CVLM** is a **left ventrolateral sympathoinhibitory** region.
*   **NOT the left retrotrapezoid nucleus.** The left RTN is a
    **respiratory chemoreceptor**; the **left CVLM** is a
    **sympathoinhibitory** relay.
*   **NOT the left medullary pyramid or the left olivary body.**
    The left pyramid is white-matter corticospinal /
    corticobulbar tract; the left olivary body is a cerebellar
    relay. The **left CVLM** is grey-matter left ventrolateral
    medulla.
*   **NOT the left nucleus ambiguus.** The left nucleus ambiguus
    is a branchial motor nucleus; the **left CVLM** is a
    sympathoinhibitory region.
*   **No ``AREA_PATHS`` hop.** The left CVLM is a **local leaf** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The left CVLM has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the right CVLM — strict mirror with
    NO warning.** The left and right CVLM modules are
    **structurally identical** — same leaf status, same
    **sympathoinhibitory** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "caudal_ventrolateral_medulla.left"
    )

**Do not** assume the left CVLM is the **right CVLM**. The right
CVLM is the **separate leaf** at
``.../caudal_ventrolateral_medulla/right/``.

**Do not** assume the left CVLM is the **left RVLM**. The **left
RVLM** (``.../rostral_ventrolateral_medulla/left/``) is the
**left rostral** ventrolateral medulla — the **left sympathetic
premotor** center. The **left CVLM** is the **left caudal**
ventrolateral medulla — the **left sympathoinhibitory** relay.
They are **DIFFERENT STRUCTURES at DIFFERENT rostrocaudal
levels**.

**Do not** assume the left CVLM is the **left NTS**, the **left
arcuate nucleus**, the **left retrotrapezoid nucleus**, the
**left medullary pyramid**, the **left olivary body**, or the
**left nucleus ambiguus**. Each is a **different structure**.

**Do not** assume the left CVLM has **structural children**. It
is a **leaf** — it represents the left CVLM as a **single
structure**.

Iterating the left CVLM's (empty) children (recommended consumer
pattern)::

    LEFT_CAUDAL_VENTROLATERAL_MEDULLA_CHILDREN = ()
    # The left CVLM is a leaf. It has no structural children.

Reaching the right CVLM (recommended consumer pattern — the
contralateral leaf)::

    # The right CVLM is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.right
    #
    # The left and right CVLMs are structurally symmetric mirror
    # pairs with ipsilateral projections to their respective
    # RVLMs.

Reaching the left RVLM (recommended consumer pattern — the
ROSTRAL sibling)::

    # The left RVLM is the LEFT ROSTRAL ventrolateral medulla —
    # the left sympathetic premotor / vasomotor center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #
    # The left CVLM INHIBITS the left RVLM via a GABAergic
    # ipsilateral projection. They are DIFFERENT STRUCTURES at
    # DIFFERENT rostrocaudal levels.

Reaching the left NTS (recommended consumer pattern — the
UPSTREAM afferent)::

    # The left NTS is the LEFT visceral afferent relay UPSTREAM
    # of the left CVLM in the left medullary baroreflex arc:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
    #
    # Circuit: left NTS -> left CVLM -> left RVLM -> left
    # intermediolateral cell column. The left CVLM is the LEFT
    # SYMPATHOINHIBITORY node.

Reaching the left arcuate nucleus (recommended consumer pattern
— NOTE the ventral-surface distinction)::

    # The left arcuate nucleus is a LEFT VENTRAL-SURFACE
    # chemosensory and hypothalamic-projecting nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.left
    #
    # The left CVLM is more LATERAL in the left caudal
    # ventrolateral medulla. They are DIFFERENT STRUCTURES.

Reaching the left retrotrapezoid nucleus (recommended consumer
pattern — NOTE the respiratory-chemoreceptor distinction)::

    # The left retrotrapezoid nucleus is a respiratory
    # chemoreceptor:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.left
    #
    # The left CVLM is a sympathoinhibitory relay. They are
    # DIFFERENT STRUCTURES.

Reaching the left nucleus ambiguus (recommended consumer
pattern — NOTE the motor-nucleus distinction)::

    # The left nucleus ambiguus is a branchial motor nucleus (CN
    # IX/X/XI):
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.nucleus_ambiguus
    #
    # The left CVLM is a sympathoinhibitory region. They are
    # DIFFERENT STRUCTURES.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"caudal_ventrolateral_medulla.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical medullary autonomic anatomy:** Blessing, W.W.
    (1997). *The Lower Brain Stem and Bodily Homeostasis.*
    (CVLM; RVLM; NTS; medullary baroreflex circuit; autonomic
    premotor organization.)
*   **CVLM and sympathoinhibition:** Schreihofer, A.M., Guyenet,
    P.G. (2000). "Role of the ventrolateral medulla in
    sympathoinhibition." *American Journal of Physiology*
    279:R1701–R1711. (CVLM as the sympathoinhibitory relay;
    GABAergic projection to RVLM.)
*   **RVLM and sympathetic premotor (contrast):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure." *Nature
    Reviews Neuroscience* 7:335–346. (RVLM; sympathetic premotor
    neurons — DIFFERENT from the CVLM.)
*   **NTS and visceral afferents (contrast — UPSTREAM of CVLM):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS as the
    visceral afferent relay — UPSTREAM of CVLM.)
*   **Medullary baroreflex circuit:** Dampney, R.A.L. (1994).
    "Functional organization of central pathways regulating the
    cardiovascular system." *Physiological Reviews* 74:323–364.
    (NTS → CVLM → RVLM baroreflex arc.)
*   **CVLM and baroreflex buffering:** Jeske, I., et al. (1995).
    "Contribution of the caudal ventrolateral medulla to the
    baroreflex." *American Journal of Physiology*
    269:R1003–R1010. (CVLM as the sympathoinhibitory node in the
    baroreflex.)
*   **Neurogenic hypertension (via CVLM dysfunction):** Guyenet,
    P.G. (2006). "The sympathetic control of blood pressure."
    *Nature Reviews Neuroscience* 7:335–346. (CVLM dysfunction
    and sympathetic overactivity.)
*   **Baroreflex failure:** Robertson, D., et al. (1993).
    "Baroreflex failure: a new syndrome of hypertension and
    hypotension." *Hypertension* 21:496–501. (Baroreflex failure
    — autonomic instability.)
*   **Brainstem stroke (contrast — Wallenberg syndrome):** Sacco,
    R.L., et al. (1993). "Lateral medullary infarction: clinical
    and MRI correlation." *Stroke* 24:1981–1987. (Wallenberg
    syndrome; lateral medullary lesion — CVLM-adjacent.)
*   **Medullary cytoarchitecture:** Paxinos, G., Huang, X.-F.
    (2013). *The Behaving Human Brain: A Cytoarchitectural
    Atlas.* (Medullary nuclei; ventrolateral medullary regions.)
*   **CVLM functional anatomy:** Dampney, R.A.L., et al. (2002).
    "Medullary and supramedullary mechanisms regulating
    sympathetic vasomotor tone." *Clinical and Experimental
    Pharmacology and Physiology* 30:6–12. (CVLM; RVLM; NTS;
    autonomic circuit.)
*   NeuroNames — Caudal ventrolateral medulla; FMA — Caudal
    ventrolateral medulla.
"""