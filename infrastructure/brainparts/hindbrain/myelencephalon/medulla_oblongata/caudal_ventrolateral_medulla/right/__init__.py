"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.right
========================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── caudal_ventrolateral_medulla
                └── right   <-- THIS MODULE

**Primary synonym:** Right caudal ventrolateral medulla; right CVLM;
right caudal ventrolateral medullary region; right caudal
ventrolateral medullary depressor area.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** — a group of **functionally
defined neurons** in the **right caudal ventrolateral medulla**,
**ventral and lateral** to the **right nucleus ambiguus** and the
**right lateral reticular nucleus**, **caudal** to the **right
RVLM** and **rostral** to the **spinomedullary junction**. It is
the **right sympathoinhibitory relay** — the right **CVLM** of the
**medullary autonomic circuit**.
**Part of:** The **caudal_ventrolateral_medulla** bilateral
container — which is part of the **medulla oblongata** — the
**caudal brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../caudal_ventrolateral_medulla/`` →
**direct child** of the caudal_ventrolateral_medulla container.
The **right** CVLM is one of the **two** structural children of the
container (the other is ``left``).
**Structural children:** **None.** This is a **leaf** module. The
right CVLM is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the left CVLM — the contralateral leaf):**
**Boundary case — the right CVLM is NOT the left CVLM.** The
**left CVLM** (``.../caudal_ventrolateral_medulla/left/``) is the
**contralateral leaf** — the CVLM of the **left** medulla. **They
are DIFFERENT LEAVES** — the ``left`` and ``right`` modules are
the two sides of the **bilateral container**. Consumers must
**not** conflate the **right** CVLM with the **left** CVLM —
resolve the left side via ``caudal_ventrolateral_medulla.left``.
**Boundary status (NOT the right RVLM — the RVLM is the ROSTRAL
ventrolateral medulla):** **Boundary case — the right CVLM is NOT
the right RVLM.** The **right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) is the **right
rostral** ventrolateral medulla — the **right sympathetic
premotor / vasomotor center** that provides **tonic excitatory
drive** to the **right intermediolateral cell column**. The
**right CVLM** (here) is the **right caudal** ventrolateral
medulla — the **right sympathoinhibitory relay** that **inhibits
the right RVLM**. **They are DIFFERENT STRUCTURES at DIFFERENT
rostrocaudal levels** — the **right RVLM** is **rostral**; the
**right CVLM** is **caudal**. Consumers must **not** conflate the
two — the **right RVLM** **drives** sympathetic outflow; the
**right CVLM** **inhibits** it.
**Boundary status (NOT the right arcuate nucleus — a
ventral-surface nucleus):** **Boundary case — the right CVLM is
NOT the right arcuate nucleus.** The **right arcuate nucleus**
(``.../arcuate_nucleus/right/``) is a **ventral-surface
chemosensory and hypothalamic-projecting** nucleus at the **right
ventral medullary surface**, adjacent to the **anterior median
fissure**. The **right CVLM** (here) is a **more lateral** right
ventrolateral medullary region — it is **NOT** the right arcuate
nucleus. **They are DIFFERENT STRUCTURES** — the **right arcuate
nucleus** is a **ventral-surface** nucleus; the **right CVLM** is
a **ventrolateral** region. Consumers must **not** conflate the
two.
**Boundary status (NOT the right solitary nucleus — the NTS is
the visceral afferent relay):** **Boundary case — the right CVLM
is NOT the right solitary nucleus.** The **right solitary
nucleus** (NTS) (``.../solitary_nucleus/right/``) is the **right
visceral afferent relay** — it receives **baroreceptor**,
**chemoreceptor**, and **gastrointestinal** afferents. The
**right CVLM** (here) is the **right sympathoinhibitory relay**
— it **receives right NTS input** and **inhibits the right
RVLM**. **They are DIFFERENT STRUCTURES** — the **right NTS** is
the **afferent** relay; the **right CVLM** is the
**sympathoinhibitory** relay. Consumers must **not** conflate
the two.
**Boundary status (NOT the right retrotrapezoid nucleus — that
is a respiratory chemoreceptor):** **Boundary case — the right
CVLM is NOT the right retrotrapezoid nucleus.** The **right
retrotrapezoid nucleus** (RTN) is a **more rostral**
ventral-surface **respiratory chemoreceptor** — it is wired under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/right/``.
The **right CVLM** (here) is a **right caudal ventrolateral**
**sympathoinhibitory relay**. **They are DIFFERENT STRUCTURES** —
the **right RTN** is a **respiratory chemoreceptor**; the
**right CVLM** is a **sympathoinhibitory** relay. Consumers must
**not** conflate the two.
**Boundary status (NOT the right ventrolateral medulla as a
whole — a specific rostrocaudal subdivision):** **Boundary case —
the right CVLM is NOT the whole right ventrolateral medulla
(VLM).** The **right ventrolateral medulla** is a **region**
containing the **right RVLM**, the **right CVLM**, and the
**right arcuate nucleus**. The **right CVLM** (here) is the
**right caudal** subdivision — it is **NOT** the whole **right
VLM**, and it is **NOT** the **right RVLM** or the **right
arcuate nucleus**. Consumers must **not** conflate the **right
CVLM** with the **whole right ventrolateral medulla**.
**Boundary status (NOT the right medullary pyramid — adjacent but
distinct):** **Boundary case — the right CVLM is NOT the right
medullary pyramid.** The **right medullary pyramid**
(``.../medullary_pyramid/right/``) is the **right corticospinal
/ corticobulbar tract** — a **white-matter** structure at the
**right ventral medulla**. The **right CVLM** (here) is a
**grey-matter** region in the **right caudal ventrolateral
medulla**. **They are DIFFERENT STRUCTURES** — the pyramid is
**white matter** (descending motor fibers); the **right CVLM**
is **grey matter** (neurons). Consumers must **not** conflate
the two.
**Boundary status (NOT the right olivary body — adjacent but
distinct):** **Boundary case — the right CVLM is NOT the right
olivary body.** The **right olivary body**
(``.../olivary_body/right/``) contains the **right inferior
olivary nucleus** — the **sole source of climbing fibers** to
the **right cerebellar hemisphere**. The **right CVLM** (here)
is a **right ventrolateral medullary sympathoinhibitory**
region. **They are DIFFERENT STRUCTURES** — the right olivary
body is a **cerebellar relay**; the **right CVLM** is a
**sympathoinhibitory** relay. Consumers must **not** conflate
the two.
**Boundary status (NOT the right nucleus ambiguus — adjacent but
distinct):** **Boundary case — the right CVLM is NOT the right
nucleus ambiguus.** The **right nucleus ambiguus**
(``.../cranial_nerve_nuclei/right/nucleus_ambiguus/``) is a
**right branchial motor** nucleus (CN IX/X/XI) **dorsal** to
the right CVLM. The **right CVLM** (here) is a **right
ventrolateral sympathoinhibitory** region. **They are DIFFERENT
STRUCTURES** — the right nucleus ambiguus is a **motor nucleus**;
the **right CVLM** is a **sympathoinhibitory** region.
Consumers must **not** conflate the two.
**Boundary status (NOT the spinal cord — that begins at the
foramen magnum):** **Boundary case — the right CVLM is NOT the
spinal cord.** The **spinal cord** (``.../spinal_cord/``) is a
**separate container** beginning at the **foramen magnum**. The
**right CVLM** (here) is a **medullary** region — its **caudal
boundary** is the **spinomedullary junction** (the **pyramidal
decussation**). Consumers must **not** conflate the **right
CVLM** with the **spinal cord**.

Overview
--------
The **right CVLM** is the **right caudal ventrolateral medulla**
— the **right sympathoinhibitory relay** of the **right
medullary autonomic circuit**. It lies **ventrolateral** in the
**right caudal medulla**, **caudal** to the **right RVLM** and
**rostral** to the **spinomedullary junction**, and it **inhibits
the right RVLM** in response to **baroreceptor** and **visceral**
input relayed by the **right NTS**.

**This is a LEAF module.** The **right CVLM** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution of the right
side use this module; consumers that need **left-side** resolution
use ``.../caudal_ventrolateral_medulla/left/``; consumers that
need **bilateral** resolution iterate over both.

**The right CVLM is the RIGHT caudal ventrolateral medulla, NOT
the right rostral one.** The **right RVLM** is **rostral**; the
**right CVLM** is **caudal**. **They are DIFFERENT STRUCTURES at
DIFFERENT rostrocaudal levels** — the **right RVLM** **drives**
sympathetic outflow; the **right CVLM** **inhibits** it.

**The right CVLM is functionally coupled to the right NTS and
right RVLM in the right medullary baroreflex circuit.** The
**right NTS** receives **baroreceptor** afferents; the **right
CVLM** receives **right NTS** input and **inhibits the right
RVLM**; the **right RVLM** drives **right sympathetic outflow**.
This is the **right medullary baroreflex arc** — a
**three-structure circuit** (right NTS → right CVLM → right
RVLM).

**The right CVLM is NOT the right arcuate nucleus, the right RTN,
the right nucleus ambiguus, the right medullary pyramid, or the
right olivary body.** Each is a **different structure** in the
**right caudal ventrolateral medulla region**.

The Right CVLM / Left CVLM Boundary
-----------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right CVLM** (this module) — the CVLM of the **right**
    medulla.

*   **Left CVLM** (``.../caudal_ventrolateral_medulla/left/``) —
    the CVLM of the **left** medulla.

**The two are the SIDES of the bilateral CVLM container.** They
are **structurally symmetric mirror pairs** — same
cytoarchitecture, same ipsilateral projections, same functions.
Consumers must **not** conflate the right with the left —
resolve the left side via ``caudal_ventrolateral_medulla.left``.

The Right CVLM / Right RVLM Boundary
------------------------------------
This is the **most consequential** rostrocaudal boundary:

*   **Right CVLM** (this module) — the **right caudal**
    ventrolateral medulla — the **right sympathoinhibitory
    relay**.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``)
    — the **right rostral** ventrolateral medulla — the **right
    sympathetic premotor / vasomotor center**.

**The two are ROSTROCAUDAL SIBLINGS of the right ventrolateral
medulla.** The **right RVLM** **drives** sympathetic outflow; the
**right CVLM** **inhibits** it. Consumers must **not** conflate
the two — the **right RVLM** is **rostral**; the **right CVLM**
is **caudal**.

The Right CVLM / Right NTS Boundary
-----------------------------------
This is the **autonomic-circuit** boundary:

*   **Right CVLM** (this module) — the **right sympathoinhibitory
    relay**.

*   **Right NTS** (``.../solitary_nucleus/right/``) — the **right
    visceral afferent relay**.

**The right NTS is UPSTREAM of the right CVLM in the right
medullary baroreflex arc.** The **right NTS** receives
**baroreceptor** afferents and **projects** to the **right
CVLM**; the **right CVLM** **inhibits the right RVLM**.
Consumers must **not** conflate the **right NTS** with the
**right CVLM** — the **right NTS** is the **afferent** relay;
the **right CVLM** is the **sympathoinhibitory** relay.

The Right CVLM / Right Arcuate Nucleus Boundary
-----------------------------------------------
This is the **ventral-surface** boundary:

*   **Right CVLM** (this module) — the **right caudal
    ventrolateral medulla** (more **lateral**).

*   **Right arcuate nucleus** (``.../arcuate_nucleus/right/``) —
    a **ventral-surface chemosensory and hypothalamic-projecting**
    nucleus (more **medial**, at the **right ventral surface**).

**They are DIFFERENT STRUCTURES in the right ventrolateral
medullary region.** Consumers must **not** conflate the **right
CVLM** with the **right arcuate nucleus**.

The Right CVLM / Right Retrotrapezoid Nucleus Boundary
------------------------------------------------------
This is the **respiratory-chemoreceptor** boundary:

*   **Right CVLM** (this module) — the **right caudal
    ventrolateral sympathoinhibitory** relay.

*   **Right RTN**
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/right/``)
    — a **more rostral** right ventral-surface **respiratory
    chemoreceptor**.

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate them.

The Right CVLM / Right Medullary Pyramid and Right Olivary Body
Boundary
--------
This is the **grey-matter / white-matter and cerebellar-relay**
boundary:

*   **Right CVLM** (this module) — **grey-matter** region in the
    **right caudal ventrolateral medulla**.

*   **Right medullary pyramid**
    (``.../medullary_pyramid/right/``) — **white-matter** right
    corticospinal / corticobulbar tract.

*   **Right olivary body** (``.../olivary_body/right/``) —
    contains the **right inferior olivary nucleus** (right
    cerebellar climbing fibers).

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the **right CVLM** with the **right medullary pyramid**
or the **right olivary body**.

The Right CVLM / Right Nucleus Ambiguus Boundary
------------------------------------------------
This is the **motor-nucleus** boundary:

*   **Right CVLM** (this module) — a **right ventrolateral
    sympathoinhibitory** region.

*   **Right nucleus ambiguus**
    (``.../cranial_nerve_nuclei/right/nucleus_ambiguus/``) — a
    **right branchial motor** nucleus (CN IX/X/XI) **dorsal** to
    the right CVLM.

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate them.

Function in the Human Brain
---------------------------
The right CVLM's function is **right sympathoinhibition** in the
**right medullary baroreflex circuit** — **NOT sympathetic
premotor** and **NOT respiratory rhythm**:

*   **Sympathoinhibition (right medullary baroreflex):** The
    **right CVLM** receives **glutamatergic** input from the
    **right NTS** and **projects GABAergic inhibitory** fibers to
    the **right RVLM** — **inhibiting** the **right sympathetic
    premotor** neurons. This is the **right medullary baroreflex
    arc** (right NTS → right CVLM → right RVLM) that **buffers**
    blood pressure **fluctuations** on the right side.

*   **Baroreflex buffering (right side):** The **right CVLM** is
    the **key right sympathoinhibitory** node in the
    **baroreflex** — it **reduces right sympathetic outflow**
    when **blood pressure rises**, and it **withdraws**
    inhibition when **blood pressure falls**. This is a
    **critical** homeostatic mechanism, integrated with the left
    CVLM via **bilateral** coordination.

*   **Visceral reflex integration (right side):** The **right
    CVLM** integrates **visceral** input from the **right NTS**
    (baroreceptor, chemoreceptor, gastrointestinal) and
    **modulates** the **right RVLM** sympathetic drive
    accordingly.

*   **NOT right sympathetic premotor:** The **right sympathetic
    premotor** function is the **right RVLM** — **NOT** the
    right CVLM.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the right CVLM.

*   **NOT chemosensory:** The **central chemoreception**
    function is the **right ventral medullary surface** (right
    arcuate nucleus, right RTN) — **NOT** the right CVLM.

**The unifying theme:** the right CVLM is the **right caudal
ventrolateral medulla** — the **right sympathoinhibitory relay**
that **buffers** right sympathetic outflow via the **right
medullary baroreflex arc** (right NTS → right CVLM → right RVLM).
It is **NOT** the right RVLM, **NOT** the right NTS, **NOT** the
right arcuate nucleus, **NOT** the right RTN, and **NOT** the
right nucleus ambiguus.

Associated Disorders
--------------------
The right CVLM has **no named clinical syndrome** of its own —
its clinical associations are **indirect**:

*   **Neurogenic hypertension (via right CVLM dysfunction):**
    Impaired **right CVLM** sympathoinhibition — or impaired
    **right NTS → right CVLM** signaling — contributes to
    **right sympathetic overactivity** and **neurogenic
    hypertension**. The **right CVLM** is the **right
    sympathoinhibitory** node; its dysfunction **reduces**
    baroreflex **buffering**.

*   **Baroreflex failure (via right CVLM / right NTS / right
    RVLM circuit dysfunction):** Disruption of the **right
    medullary baroreflex arc** — including the **right CVLM** —
    causes **baroreflex failure** — **labile blood pressure**,
    **orthostatic hypotension**, and **hypertensive crises**.
    The **bilateral** integration of right and left CVLM means
    unilateral lesions may be **compensated** by the
    **contralateral** side.

*   **Brainstem stroke (via right ventrolateral medullary
    infarction):** Infarction of the **right caudal
    ventrolateral medulla** — adjacent to the **right CVLM** —
    can cause **autonomic** and **cardiovascular** instability.
    The **right CVLM** contributes to the **autonomic**
    component of **Wallenberg syndrome** (lateral medullary
    syndrome), though the **primary** lesion is in the **right
    lateral medulla** structures (right NTS, right spinothalamic
    tract, right nucleus ambiguus, right inferior cerebellar
    peduncle).

*   **No Named "Right CVLM Syndrome":** The right CVLM is a
    **functionally defined region** (not a sharply demarcated
    nucleus) — it has **no named clinical syndrome**. Its
    clinical relevance is **indirect**, via the **right medullary
    baroreflex** circuit.

**What is NOT here:** The right CVLM is **not** the substrate for
**central hypoventilation** (ventral medullary surface /
pre-Bötzinger complex), **Wallenberg syndrome** (lateral medulla
— right NTS, right nucleus ambiguus, right spinothalamic tract),
or **neurogenic hypertension of the RVLM type** (right RVLM). Its
clinical relevance is the **right sympathoinhibitory** and
**baroreflex** functions listed above.

Lateralization Notes
--------------------
This is the **right** CVLM module. The CVLM is a **bilateral
container** whose two sides are **structurally symmetric mirror
pairs** — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **right** and **left** CVLM
    regions are **structurally symmetric** — they are **mirror
    pairs** with the **same** cytoarchitecture, **same**
    ipsilateral projections, and **same** functions. The
    **right** CVLM projects **ipsilaterally** to the **right**
    RVLM; the **left** CVLM projects **ipsilaterally** to the
    **left** RVLM.

*   **Ipsilateral Projection:** Each **CVLM** projects
    **ipsilaterally** to its **ipsilateral RVLM** —
    **right CVLM → right RVLM** and **left CVLM → left RVLM**.
    This is **functionally** an **ipsilateral** circuit; the
    bilateral **sympathoinhibition** is the **sum** of the two
    sides. **Unilateral right CVLM lesion** may be
    **compensated** by the **left** side (and vice versa).

*   **NO Lateralization Warning:** The CVLM has **no known
    functional lateralization** in humans. Consumers must **not**
    import a **lateralization warning** into the right CVLM —
    the **right** and **left** sides are **functionally
    symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right CVLM is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into the right
    CVLM.

*   **NO Fear-Output Warning:** The right CVLM is **not** a
    fear-output structure — it is a **right sympathoinhibitory**
    region. Consumers must **not** conflate it with the
    **central nucleus** or with the **amygdala**.

**A consumer that assumes "right CVLM = left CVLM" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent**. The CVLM is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no fear-output
warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right CVLM is a
    **leaf** — it does **not** import from ``.../left/`` or any
    other left-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../rostral_ventrolateral_medulla/``,
    ``.../arcuate_nucleus/``, ``.../solitary_nucleus/``,
    ``.../ventral_respiratory_group/``,
    ``.../medullary_pyramid/``, ``.../olivary_body/``,
    ``.../cranial_nerve_nuclei/``, or any other container. The
    right CVLM's relationships to the right RVLM, right NTS,
    right arcuate nucleus, right RTN, right medullary pyramid,
    right olivary body, and right nucleus ambiguus are documented
    as **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right CVLM is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../right/``.
*   **NOT the left CVLM.** The left CVLM is a **separate leaf**
    under ``.../caudal_ventrolateral_medulla/left/``. Consumers
    must **not** conflate the right with the left.
*   **NOT the right RVLM.** The right RVLM is the **right
    rostral** ventrolateral medulla — the **right sympathetic
    premotor** center. The **right CVLM** is the **right
    caudal** ventrolateral medulla — the **right
    sympathoinhibitory** relay. Consumers must **not** conflate
    the two.
*   **NOT the right NTS.** The right NTS is the **right visceral
    afferent** relay; the **right CVLM** is the **right
    sympathoinhibitory** relay.
*   **NOT the right arcuate nucleus.** The right arcuate nucleus
    is a **right ventral-surface chemosensory** nucleus; the
    **right CVLM** is a **right ventrolateral
    sympathoinhibitory** region.
*   **NOT the right retrotrapezoid nucleus.** The right RTN is a
    **respiratory chemoreceptor**; the **right CVLM** is a
    **sympathoinhibitory** relay.
*   **NOT the right medullary pyramid or the right olivary
    body.** The right pyramid is white-matter corticospinal /
    corticobulbar tract; the right olivary body is a cerebellar
    relay. The **right CVLM** is grey-matter right ventrolateral
    medulla.
*   **NOT the right nucleus ambiguus.** The right nucleus
    ambiguus is a branchial motor nucleus; the **right CVLM** is
    a sympathoinhibitory region.
*   **No ``AREA_PATHS`` hop.** The right CVLM is a **local leaf**
    — it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The right CVLM has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the left CVLM — strict mirror with
    NO warning.** The right and left CVLM modules are
    **structurally identical** — same leaf status, same
    **sympathoinhibitory** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "caudal_ventrolateral_medulla.right"
    )

**Do not** assume the right CVLM is the **left CVLM**. The left
CVLM is the **separate leaf** at
``.../caudal_ventrolateral_medulla/left/``.

**Do not** assume the right CVLM is the **right RVLM**. The
**right RVLM** (``.../rostral_ventrolateral_medulla/right/``) is
the **right rostral** ventrolateral medulla — the **right
sympathetic premotor** center. The **right CVLM** is the **right
caudal** ventrolateral medulla — the **right sympathoinhibitory**
relay. They are **DIFFERENT STRUCTURES at DIFFERENT rostrocaudal
levels**.

**Do not** assume the right CVLM is the **right NTS**, the
**right arcuate nucleus**, the **right retrotrapezoid nucleus**,
the **right medullary pyramid**, the **right olivary body**, or
the **right nucleus ambiguus**. Each is a **different
structure**.

**Do not** assume the right CVLM has **structural children**. It
is a **leaf** — it represents the right CVLM as a **single
structure**.

Iterating the right CVLM's (empty) children (recommended consumer
pattern)::

    RIGHT_CAUDAL_VENTROLATERAL_MEDULLA_CHILDREN = ()
    # The right CVLM is a leaf. It has no structural children.

Reaching the left CVLM (recommended consumer pattern — the
contralateral leaf)::

    # The left CVLM is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.left
    #
    # The right and left CVLMs are structurally symmetric mirror
    # pairs with ipsilateral projections to their respective
    # RVLMs.

Reaching the right RVLM (recommended consumer pattern — the
ROSTRAL sibling)::

    # The right RVLM is the RIGHT ROSTRAL ventrolateral medulla —
    # the right sympathetic premotor / vasomotor center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #
    # The right CVLM INHIBITS the right RVLM via a GABAergic
    # ipsilateral projection. They are DIFFERENT STRUCTURES at
    # DIFFERENT rostrocaudal levels.

Reaching the right NTS (recommended consumer pattern — the
UPSTREAM afferent)::

    # The right NTS is the RIGHT visceral afferent relay UPSTREAM
    # of the right CVLM in the right medullary baroreflex arc:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
    #
    # Circuit: right NTS -> right CVLM -> right RVLM -> right
    # intermediolateral cell column. The right CVLM is the RIGHT
    # SYMPATHOINHIBITORY node.

Reaching the right arcuate nucleus (recommended consumer
pattern — NOTE the ventral-surface distinction)::

    # The right arcuate nucleus is a RIGHT VENTRAL-SURFACE
    # chemosensory and hypothalamic-projecting nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.right
    #
    # The right CVLM is more LATERAL in the right caudal
    # ventrolateral medulla. They are DIFFERENT STRUCTURES.

Reaching the right retrotrapezoid nucleus (recommended consumer
pattern — NOTE the respiratory-chemoreceptor distinction)::

    # The right retrotrapezoid nucleus is a respiratory
    # chemoreceptor:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.right
    #
    # The right CVLM is a sympathoinhibitory relay. They are
    # DIFFERENT STRUCTURES.

Reaching the right nucleus ambiguus (recommended consumer
pattern — NOTE the motor-nucleus distinction)::

    # The right nucleus ambiguus is a branchial motor nucleus (CN
    # IX/X/XI):
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.nucleus_ambiguus
    #
    # The right CVLM is a sympathoinhibitory region. They are
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