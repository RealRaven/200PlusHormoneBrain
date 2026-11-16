"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.left
============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── medullary_pyramid
                └── left   <-- THIS MODULE

**Primary synonym:** Left medullary pyramid; left pyramid of the
medulla oblongata; left pyramis medullae oblongatae; left anterior
pyramid; left bulbar pyramid; left medullary pyramidal tract.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **left medullary segment** of the
**corticospinal** and **corticobulbar** tracts. It is **NOT** a
grey-matter nucleus, **NOT** the whole corticospinal tract, and
**NOT** the whole corticobulbar tract — it is the **left ventral
medullary portion** of those descending motor pathways, visible
as a **left ventral bulge** on the medullary surface.
**Part of:** The **medullary_pyramid** bilateral container — which
is part of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medullary_pyramid/`` → **direct
child** of the medullary_pyramid container. The **left** medullary
pyramid is one of the **two** structural children of the container
(the other is ``right``).
**Structural children:** **None.** This is a **leaf** module. The
left medullary pyramid is represented as a **single structure** —
it has **no structural children** of its own.
**Boundary status (NOT the right medullary pyramid — the
contralateral leaf):** **Boundary case — the left medullary
pyramid is NOT the right medullary pyramid.** The **right
medullary pyramid** (``.../medullary_pyramid/right/``) is the
**contralateral leaf** — the medullary pyramid of the **right**
medulla. **They are DIFFERENT LEAVES** — the ``left`` and
``right`` modules are the two sides of the **bilateral container**.
Consumers must **not** conflate the **left** medullary pyramid
with the **right** medullary pyramid — resolve the right side via
``medullary_pyramid.right``.
**Boundary status (NOT the whole left corticospinal tract — only
the medullary segment):** **Boundary case — the left medullary
pyramid is NOT the whole left corticospinal tract.** The **left
corticospinal tract** extends from the **left motor cortex** (via
the **left corona radiata**, **left internal capsule**, **left
cerebral peduncle**, **left pons**) to the **spinal cord**. The
**left medullary pyramid** (here) is the **left medullary
segment** — the portion that **runs on the ventral surface** of
the left medulla. Consumers must **not** conflate the **left
medullary pyramid** with the **whole left corticospinal tract**.
**Boundary status (NOT the whole left corticobulbar tract — only
the medullary segment):** **Boundary case — the left medullary
pyramid is NOT the whole left corticobulbar tract.** The **left
corticobulbar tract** extends from the **left motor cortex** to
the **left cranial nerve motor nuclei**. The **left medullary
pyramid** (here) carries the **left corticobulbar fibers** that
**travel through** the medullary segment. Consumers must **not**
conflate the two.
**Boundary status (NOT the pyramidal decussation — the decussation
is the CAUDAL END of the left pyramid):** **Boundary case — the
left medullary pyramid is NOT the pyramidal decussation.** The
**pyramidal decussation** is the **crossing of the corticospinal
fibers at the spinomedullary junction** — the **caudal end** of
the left medullary pyramid. It is **where ~85–90% of left
corticospinal fibers cross the midline** to form the **right
lateral corticospinal tract** (and vice versa). The **left
medullary pyramid** (here) is the **left ventral column** that
**leads to** the decussation. Consumers must **not** conflate the
**pyramid** with the **decussation**.
**Boundary status (NOT the left spinal corticospinal tract — the
spinal segment is in the spinal_cord container):** **Boundary
case — the left medullary pyramid is NOT the left spinal
corticospinal tract.** The **left lateral corticospinal tract**
and the **left anterior corticospinal tract** are **left spinal
cord** structures — wired under
``.../spinal_cord/white_matter/left/corticospinal_tract/``. The
**left medullary pyramid** (here) is the **left medullary
segment** — **rostral** to the **pyramidal decussation** and the
**left spinal cord**. Consumers must **not** conflate the two.
**Boundary status (NOT the left internal capsule or left cerebral
peduncle — supratentorial / midbrain segments):** **Boundary
case — the left medullary pyramid is NOT the left internal
capsule or the left cerebral peduncle.** The **left internal
capsule** is a **supratentorial** white-matter structure; the
**left cerebral peduncle** (left crus cerebri) is a **midbrain**
structure. The **left medullary pyramid** (here) is the **left
medullary segment**. Consumers must **not** conflate the
**left medullary pyramid** with the **left internal capsule** or
the **left cerebral peduncle**.
**Boundary status (NOT the left pontine corticospinal tract —
that is in the metencephalon):** **Boundary case — the left
medullary pyramid is NOT the left pontine corticospinal tract.**
The **left pons** (``.../metencephalon/pons/``) contains the
**left pontine segment** of the corticospinal tract — the fibers
**disperse** among the **left pontine nuclei** and then
**reconverge** at the **left pontomedullary junction** to form
the **left medullary pyramid**. Consumers must **not** conflate
the two.
**Boundary status (NOT the left inferior olivary nucleus —
adjacent but DISTINCT):** **Boundary case — the left medullary
pyramid is NOT the left inferior olivary nucleus.** The **left
inferior olivary nucleus** (``.../olivary_body/left/``) is the
**left cerebellar climbing-fiber relay** — a **grey-matter**
structure **dorsolateral** to the left pyramid. The **left
medullary pyramid** (here) is a **white-matter tract**. **They
are DIFFERENT STRUCTURES** — the **olivary body** is
**grey-matter cerebellar relay**; the **pyramid** is
**white-matter motor tract**. Consumers must **not** conflate the
two.
**Boundary status (NOT the left arcuate nucleus — adjacent but
DISTINCT):** **Boundary case — the left medullary pyramid is NOT
the left arcuate nucleus.** The **left arcuate nucleus**
(``.../arcuate_nucleus/left/``) is a **left ventral-surface
grey-matter** chemosensory / hypothalamic-projecting nucleus,
adjacent to the left pyramid. The **left medullary pyramid**
(here) is a **white-matter tract**. **They are DIFFERENT
STRUCTURES** — the **arcuate nucleus** is **grey matter**; the
**pyramid** is **white matter**. Consumers must **not** conflate
the two.
**Boundary status (NOT the left RVLM / left CVLM —
ventrolateral, not ventral):** **Boundary case — the left
medullary pyramid is NOT the left RVLM or left CVLM.** The **left
RVLM** (``.../rostral_ventrolateral_medulla/left/``) and **left
CVLM** (``.../caudal_ventrolateral_medulla/left/``) are
**ventrolateral grey-matter autonomic** regions. The **left
medullary pyramid** (here) is a **ventral white-matter tract**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left cranial nerve nuclei — dorsal /
ventrolateral grey matter):** **Boundary case — the left
medullary pyramid is NOT the left cranial nerve nuclei.** The
**left cranial nerve nuclei**
(``.../cranial_nerve_nuclei/left/``) are **dorsal and
ventrolateral grey-matter** nuclei. The **left medullary
pyramid** (here) is a **ventral white-matter tract**. The
**left corticobulbar fibers** that **innervate** the left
cranial nerve nuclei **travel through** the left pyramid region
— but the **tract** and the **nuclei** are **different
structures**. Consumers must **not** conflate the two.
**Boundary status (NOT the left medial lemniscus — a DIFFERENT
white-matter tract):** **Boundary case — the left medullary
pyramid is NOT the left medial lemniscus.** The **left medial
lemniscus** is a **left sensory** white-matter tract (fine
touch, vibration, proprioception) that runs **dorsal** to the
left pyramid. The **left medullary pyramid** (here) is a **left
motor** white-matter tract. Consumers must **not** conflate the
two.
**Boundary status (NOT the whole left medulla oblongata — a
small white-matter tract within it):** **Boundary case — the
left medullary pyramid is NOT the whole left medulla oblongata.**
The **medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the left cranial nerve nuclei,
left autonomic nuclei, left respiratory centers, left olivary
body, left medullary pyramid (here), left arcuate nucleus, and
other structures. The **left medullary pyramid** is **one
white-matter tract** within the left medulla. Consumers must
**not** conflate the **pyramid** with the **whole medulla**.

Overview
--------
The **left medullary pyramid** is the **left ventral white-matter
column** of the **medulla oblongata** — the **left medullary
segment** of the **left corticospinal** and **left
corticobulbar** tracts. It appears as a **left ventral bulge** on
the medullary surface, **left of the anterior median fissure**,
and it **leads caudally** to the **pyramidal decussation** at
the **spinomedullary junction**.

**This is a LEAF module.** The **left medullary pyramid** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **tract-level** resolution of the
left side use this module; consumers that need **right-side**
resolution use ``.../medullary_pyramid/right/``; consumers that
need the **whole medullary_pyramid container** use
``.../medullary_pyramid/``.

**The left medullary pyramid is a WHITE-MATTER TRACT, NOT a
grey-matter nucleus.** It is the **left descending motor
column** — the **left corticospinal fibers** (to the spinal
cord) and **left corticobulbar fibers** (to the left cranial
nerve motor nuclei) **pass through** it.

**The left medullary pyramid is the MEDULLARY SEGMENT, NOT the
whole left corticospinal or corticobulbar tract.** The **whole
left corticospinal tract** extends from the **left motor
cortex** to the **spinal cord**; the **whole left corticobulbar
tract** extends from the **left motor cortex** to the **left
cranial nerve motor nuclei**. The **left medullary pyramid**
(here) is the **left ventral medullary segment**.

**The left medullary pyramid leads to the PYRAMIDAL DECUSSATION.**
At the **spinomedullary junction**, **~85–90% of left
corticospinal fibers cross the midline** to form the **right
lateral corticospinal tract** in the **right spinal cord** — and
conversely. **The decussation is the caudal landmark** of the
left medullary pyramid — **NOT** a separate module in the tree.

The Left Medullary Pyramid / Right Medullary Pyramid Boundary
------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left medullary pyramid** (this module) — the medullary
    pyramid of the **left** medulla.

*   **Right medullary pyramid** (``.../medullary_pyramid/right/``)
    — the medullary pyramid of the **right** medulla.

**The two are the SIDES of the bilateral medullary_pyramid
container.** They are **structurally symmetric mirror pairs** —
same white-matter composition, same corticospinal and
corticobulbar fiber content, same **no warning**. Consumers must
**not** conflate the left with the right — resolve the right side
via ``medullary_pyramid.right``.

The Left Medullary Pyramid / Whole Left Corticospinal and Corticobulbar Tracts Boundary
---------------------------------------------------------------------------------------
This is the **segment** boundary:

*   **Left medullary pyramid** (this module) — the **left
    medullary segment**.

*   **Whole left corticospinal tract** and **whole left
    corticobulbar tract** — the **whole pathways** from the
    **left motor cortex** to their targets.

**The left medullary pyramid is a SPECIFIC SEGMENT.** Consumers
must **not** conflate it with the **whole** tract.

The Left Medullary Pyramid / Pyramidal Decussation Boundary
-----------------------------------------------------------
This is the **column / crossing** boundary:

*   **Left medullary pyramid** (this module) — the **left ventral
    column** that **leads to** the decussation.

*   **Pyramidal decussation** — the **crossing** of the
    corticospinal fibers at the **spinomedullary junction** — the
    **caudal landmark** of the left pyramid.

**The decussation is the CAUDAL END of the left pyramid.**
Consumers must **not** conflate the **column** with the
**crossing**.

The Left Medullary Pyramid / Left Spinal Corticospinal Tract Boundary
---------------------------------------------------------------------
This is the **medullary / spinal** boundary:

*   **Left medullary pyramid** (this module) — the **left
    medullary segment**.

*   **Left spinal corticospinal tract**
    (``.../spinal_cord/white_matter/left/corticospinal_tract/``)
    — the **left spinal segment** after the **pyramidal
    decussation**.

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**
Consumers must **not** descend from the left medullary pyramid
into the spinal cord; resolve the left spinal corticospinal tract
via the **spinal cord** container.

The Left Medullary Pyramid / Left Inferior Olivary Nucleus Boundary
--------------------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Left medullary pyramid** (this module) — the **left
    ventral white-matter** motor tract.

*   **Left inferior olivary nucleus**
    (``.../olivary_body/left/``) — the **left dorsolateral
    grey-matter** cerebellar climbing-fiber relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Medullary Pyramid / Left Arcuate Nucleus Boundary
----------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Left medullary pyramid** (this module) — the **left
    ventral white-matter** motor tract.

*   **Left arcuate nucleus** (``.../arcuate_nucleus/left/``) — a
    **left ventral-surface grey-matter** chemosensory /
    hypothalamic-projecting nucleus, adjacent to the left pyramid.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Medullary Pyramid / Left RVLM and Left CVLM Boundary
-------------------------------------------------------------
This is the **ventral / ventrolateral** boundary:

*   **Left medullary pyramid** (this module) — the **left
    ventral** white-matter motor tract.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``)
    and **left CVLM**
    (``.../caudal_ventrolateral_medulla/left/``) — the **left
    ventrolateral** grey-matter autonomic regions.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Medullary Pyramid / Left Cranial Nerve Nuclei Boundary
---------------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Left medullary pyramid** (this module) — the **left
    ventral** white-matter motor tract.

*   **Left cranial nerve nuclei**
    (``.../cranial_nerve_nuclei/left/``) — the **left dorsal and
    ventrolateral** grey-matter motor nuclei.

**They are DIFFERENT STRUCTURES.** The **left corticobulbar
fibers** that **innervate** the left cranial nerve nuclei
**travel through** the left pyramid region — but the **tract**
and the **nuclei** are **different structures**.

The Left Medullary Pyramid / Left Medial Lemniscus Boundary
-----------------------------------------------------------
This is the **motor / sensory white-matter** boundary:

*   **Left medullary pyramid** (this module) — the **left
    ventral motor** white-matter tract.

*   **Left medial lemniscus** — the **left dorsal sensory**
    white-matter tract.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

Function in the Human Brain
---------------------------
The left medullary pyramid's function is **left motor
conduction** — the **left medullary segment** of the **left
corticospinal and corticobulbar tracts** — **NOT sensory
conduction**, **NOT cerebellar conduction**, and **NOT autonomic
conduction**:

*   **Left corticospinal conduction (medullary segment):** The
    **left medullary pyramid** carries the **left corticospinal
    fibers** from the **left motor cortex** to the **pyramidal
    decussation** and then to the **right spinal cord** (after
    crossing) — the **upper motor neuron** pathway for
    **voluntary movement** of the **right body**.

*   **Left corticobulbar conduction (medullary segment):** The
    **left medullary pyramid** carries the **left corticobulbar
    fibers** from the **left motor cortex** to the **left and
    right medullary cranial nerve motor nuclei** (via crossing
    at or above the decussation). Some fibers **leave the
    pyramid** at the level of their target nuclei.

*   **NOT sensory:** The **left medial lemniscus** (adjacent) is
    the **left sensory** tract — **NOT** the left pyramid.

*   **NOT cerebellar:** The **left inferior cerebellar peduncle**
    and the **left inferior olivary nucleus** (adjacent) are the
    **left cerebellar** pathways — **NOT** the left pyramid.

*   **NOT autonomic:** The **left RVLM** and **left CVLM**
    (ventrolateral) are the **left autonomic** structures —
    **NOT** the left pyramid.

**The unifying theme:** the left medullary pyramid is the **left
ventral white-matter column** of the **left medulla oblongata** —
the **left medullary segment** of the **left corticospinal and
left corticobulbar tracts**, conducting **upper motor neuron**
signals from the **left motor cortex** to the **right spinal
cord** (after decussation) and to the **left and right medullary
cranial nerve motor nuclei**.

Associated Disorders
--------------------
The left medullary pyramid is the **substrate** for **well-defined
clinical syndromes** — its clinical relevance is **direct**, via
**upper motor neuron** dysfunction:

*   **Left medial medullary syndrome (Dejerine syndrome / anterior
    spinal artery syndrome — via the left medullary pyramid):**
    Infarction of the **left medial medulla** — **right
    contralateral hemiparesis** (left pyramid), **right
    contralateral loss of proprioception/vibration** (left medial
    lemniscus — **NOT** in this container), and **left
    ipsilateral tongue weakness** (left hypoglossal nucleus/nerve
    — **NOT** in this container). The **left medullary pyramid**
    is the **direct substrate** of the **right hemiparesis** in
    left medial medullary syndrome.

*   **Pseudobulbar palsy (via left corticobulbar tract in the
    pyramid):** **Bilateral** corticobulbar lesions —
    **dysarthria**, **dysphagia**, **emotional lability** — from
    **left and right corticobulbar fiber** damage. The **left
    medullary pyramid** carries the **left corticobulbar fibers**
    that contribute to the **upper motor neuron** component of
    pseudobulbar palsy.

*   **Amyotrophic lateral sclerosis (via left corticospinal
    degeneration):** **Upper motor neuron** degeneration of the
    **left corticospinal tract** — including the **left medullary
    pyramid** — contributes to **spasticity**, **hyperreflexia**,
    and **Babinski sign** in ALS. The **left medullary pyramid**
    is the **left medullary segment** of the degenerating
    **upper motor neuron** pathway.

*   **Hereditary spastic paraplegia (via left corticospinal
    degeneration):** **Upper motor neuron** degeneration of the
    **left corticospinal tract** — including the **left medullary
    pyramid** — causes **progressive spasticity** and **gait
    impairment**. The **left medullary pyramid** is the **left
    medullary segment** of the degenerating pathway.

*   **Primary lateral sclerosis (via left corticospinal
    degeneration):** A **pure upper motor neuron** disorder —
    **left corticospinal tract** degeneration (including the
    **left medullary pyramid**) — causes **progressive
    spasticity** and **weakness**. The **left medullary pyramid**
    is the **left medullary segment** of the degenerating
    pathway.

*   **No Named "Left Medullary Pyramid Syndrome":** The left
    medullary pyramid is a **white-matter tract** — its clinical
    relevance is **direct**, via the **upper motor neuron**
    findings of the **broader brainstem lesion** (medial medullary
    syndrome) or the **neurological disorder** (ALS, HSP, PLS),
    **not** for the pyramid itself.

**What is NOT here:** The left medullary pyramid is **not** the
substrate for **sensory loss** (left medial lemniscus, left
spinothalamic tract — **NOT** in this container), **cerebellar
ataxia** (left inferior cerebellar peduncle, left inferior
olivary nucleus — **NOT** in this container), or **autonomic
dysfunction** (left RVLM, left CVLM, left NTS — **NOT** in this
container). Its clinical relevance is the **upper motor neuron**
functions listed above.

Lateralization Notes
--------------------
This is the **left** medullary pyramid module. The medullary
pyramid is a **bilateral container** whose two sides are
**structurally symmetric mirror pairs** — and it carries **NO
warning**:

*   **Bilateral Symmetry:** The **left** and **right** medullary
    pyramids are **structurally symmetric** — they are **mirror
    pairs** with the **same** white-matter composition, **same**
    corticospinal and corticobulbar fiber content, and **same**
    no warning. The **left** pyramid carries fibers from the
    **left motor cortex**; the **right** pyramid carries fibers
    from the **right motor cortex**.

*   **Contralateral Motor Control (corticospinal):** The
    **pyramidal decussation** at the **spinomedullary junction**
    crosses **~85–90%** of left corticospinal fibers, so the
    **left medullary pyramid** controls the **right** body. This
    is a **functional** contralaterality — the **pyramid itself**
    is structurally **symmetric**.

*   **NO Lateralization Warning:** The medullary pyramid has **no
    known functional lateralization** at the **tract level**.
    Consumers must **not** import a **lateralization warning**
    into the left medullary pyramid — the **left** and **right**
    pyramids are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left medullary
    pyramid is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the left medullary pyramid.

*   **NO Fear-Output Warning:** The left medullary pyramid is
    **not** a fear-output structure — it is a **ventral
    white-matter motor tract**. Consumers must **not** conflate
    it with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left medullary pyramid = right
medullary pyramid" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**tract level**. The medullary pyramid is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no fear-output
warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left medullary pyramid is
    a **leaf** — it does **not** import from ``.../right/`` or
    any other right-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../olivary_body/``, ``.../arcuate_nucleus/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../solitary_nucleus/``, ``.../ventral_respiratory_group/``,
    ``.../metencephalon/``, ``.../midbrain/``,
    ``.../spinal_cord/``, or any other container. The left
    medullary pyramid's relationships to the left olivary body,
    left arcuate nucleus, left RVLM, left CVLM, left cranial
    nerve nuclei, left medial lemniscus, and the left spinal
    corticospinal tract are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left medullary
    pyramid is a **single structure** — it has **no structural
    children**. Consumers must **not** expect further sub-paths
    under ``.../left/``.
*   **NOT the right medullary pyramid.** The right medullary
    pyramid is a **separate leaf** under
    ``.../medullary_pyramid/right/``. Consumers must **not**
    conflate the left with the right.
*   **NOT the whole left corticospinal or corticobulbar tract.**
    The left medullary pyramid is the **left medullary segment**
    — **NOT** the whole pathway.
*   **NOT the pyramidal decussation.** The decussation is the
    **caudal end** of the left pyramid — **NOT** a separate
    module.
*   **NOT the left spinal corticospinal tract.** The left spinal
    segment is wired under
    ``.../spinal_cord/white_matter/left/corticospinal_tract/``.
*   **NOT the left internal capsule or left cerebral peduncle.**
    Those are **supratentorial / midbrain** segments of the
    pathway.
*   **NOT the left inferior olivary nucleus or left arcuate
    nucleus.** Those are **left grey-matter** structures adjacent
    to the left pyramid.
*   **NOT the left RVLM or left CVLM.** Those are **left
    ventrolateral grey-matter autonomic** structures.
*   **NOT the left cranial nerve nuclei.** Those are **left dorsal
    / ventrolateral grey-matter motor** nuclei.
*   **NOT the left medial lemniscus.** That is the **left dorsal
    sensory** white-matter tract.
*   **No ``AREA_PATHS`` hop.** The left medullary pyramid is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The left medullary pyramid has
    no nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the right medullary pyramid — strict
    mirror with NO warning.** The left and right modules are
    **structurally identical** — same leaf status, same
    **white-matter motor tract** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "medullary_pyramid.left"
    )

**Do not** assume the left medullary pyramid is the **right
medullary pyramid**. The right medullary pyramid is the
**separate leaf** at ``.../medullary_pyramid/right/``.

**Do not** assume the left medullary pyramid is the **whole left
corticospinal or corticobulbar tract**. It is the **left
medullary segment** — **NOT** the whole pathway.

**Do not** assume the left medullary pyramid is the **pyramidal
decussation**. The decussation is the **caudal end** of the
left pyramid — **NOT** a separate module.

**Do not** assume the left medullary pyramid is the **left
spinal corticospinal tract**. The left spinal segment is wired
under ``.../spinal_cord/white_matter/left/corticospinal_tract/``.

**Do not** assume the left medullary pyramid is the **left
inferior olivary nucleus**, the **left arcuate nucleus**, the
**left RVLM**, the **left CVLM**, or the **left cranial nerve
nuclei**. Those are **left grey-matter** structures — **NOT** the
white-matter pyramid.

**Do not** assume the left medullary pyramid is the **left medial
lemniscus**. The left medial lemniscus is a **left sensory**
white-matter tract — **NOT** the left motor pyramid.

**Do not** assume the left medullary pyramid has **structural
children**. It is a **leaf** — it represents the left medullary
pyramid as a **single structure**.

Iterating the left medullary pyramid's (empty) children
(recommended consumer pattern)::

    LEFT_MEDULLARY_PYRAMID_CHILDREN = ()
    # The left medullary pyramid is a leaf. It has no structural
    # children.

Reaching the right medullary pyramid (recommended consumer
pattern — the contralateral leaf)::

    # The right medullary pyramid is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.right
    #
    # The left and right medullary pyramids are structurally
    # symmetric mirror pairs of white-matter motor tracts.

Reaching the left spinal corticospinal tract (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The left spinal corticospinal tract is a SEPARATE structure
    # in the SPINAL CORD container:
    #
    #   spinal_cord.white_matter.left.corticospinal_tract
    #
    # The left medullary pyramid is the LEFT MEDULLARY segment;
    # the left spinal corticospinal tract is the LEFT SPINAL
    # segment after the pyramidal decussation.

Reaching the left inferior olivary nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The left inferior olivary nucleus is a GREY-MATTER
    # cerebellar relay, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.left
    #
    # The left olivary body is DORSOLATERAL to the left pyramid —
    # adjacent but DISTINCT.

Reaching the left arcuate nucleus (recommended consumer pattern
— NOTE the DIFFERENT structure)::

    # The left arcuate nucleus is a VENTRAL-SURFACE grey-matter
    # chemosensory nucleus, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.left
    #
    # The left arcuate nucleus is ADJACENT to the left pyramid at
    # the ventral medullary surface — but it is grey matter, not
    # white matter.

Reaching the left RVLM and left CVLM (recommended consumer
pattern — NOTE the DIFFERENT structures)::

    # The left RVLM and left CVLM are VENTROLATERAL grey-matter
    # autonomic regions, NOT the ventral white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.left
    #
    # The left pyramid is VENTRAL; the left RVLM and left CVLM
    # are VENTROLATERAL — different locations, different
    # structures.

Reaching the left cranial nerve nuclei (recommended consumer
pattern — NOTE the DIFFERENT structures)::

    # The left cranial nerve nuclei are DORSAL / VENTROLATERAL
    # grey-matter motor nuclei, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left
    #
    # The left corticobulbar fibers from the left pyramid
    # innervate these nuclei — but the TRACT and the NUCLEI are
    # different structures.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"medullary_pyramid.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Medullary pyramid; corticospinal and corticobulbar tracts;
    pyramidal decussation; relations to inferior olive and
    medial lemniscus.)
*   **Corticospinal tract — overview:** Nathan, P.W., Smith, M.C.,
    Deacon, P. (1990). "The corticospinal tracts in man: course
    and location of fibres within the spinal cord." *Brain*
    113:303–324. (Corticospinal tract course; medullary pyramid;
    pyramidal decussation; lateral and anterior corticospinal
    tracts.)
*   **Corticobulbar tract — overview:** Kuypers, H.G.J.M. (1958).
    "Corticobulbar connexions to the pons and lower brain-stem in
    man." *Journal of Anatomy* 92:198–218. (Corticobulbar tract;
    medullary pyramid segment; bilateral and contralateral
    projections to cranial nerve motor nuclei.)
*   **Pyramidal decussation:** Yakovlev, P.I., Rakic, P. (1966).
    "Patterns of decussation of bulbar pyramids and distribution
    of pyramidal tracts on two sides of the spinal cord."
    *Transactions of the American Neurological Association*
    91:366–367. (Pyramidal decussation; ~85–90% of corticospinal
    fibers cross; lateral and anterior corticospinal tracts.)
*   **Medial medullary syndrome:** Bassetti, C., et al. (1996).
    "Medial medullary stroke: clinical and MRI findings."
    *Neurology* 46:106–110. (Dejerine syndrome; anterior spinal
    artery territory; medullary pyramid involvement —
    contralateral hemiparesis.)
*   **Pseudobulbar palsy:** Lieberman, A., Benson, D.F. (1977).
    "Pseudobulbar palsy." *Neurology* 27:105–109. (Bilateral
    corticobulbar lesions; dysarthria; dysphagia; emotional
    lability.)
*   **ALS — corticospinal degeneration:** Kiernan, M.C., et al.
    (2011). "Amyotrophic lateral sclerosis." *The Lancet*
    377:942–955. (ALS; upper motor neuron degeneration including
    the corticospinal tract and medullary pyramid.)
*   **Hereditary spastic paraplegia:** Fink, J.K. (2013).
    "Hereditary spastic paraplegia: clinico-pathologic features
    and emerging molecular mechanisms." *Acta Neuropathologica*
    126:307–328. (HSP; corticospinal tract degeneration;
    medullary pyramid involvement.)
*   **Primary lateral sclerosis:** Pringle, C.E., et al. (1992).
    "Primary lateral sclerosis: clinical features, neuropathology
    and diagnostic criteria." *Brain* 115:495–520. (PLS; pure
    upper motor neuron degeneration; corticospinal tract
    involvement.)
*   **Inferior olive (contrast — grey-matter cerebellar relay):**
    De Zeeuw, C.I., et al. (1998). "Microcircuitry and function
    of the inferior olive." *Trends in Neurosciences* 21:391–400.
    (Inferior olivary nucleus; climbing fibers; olivocerebellar
    pathway — DIFFERENT from the white-matter pyramid.)
*   **Medial lemniscus (contrast — sensory white-matter tract):**
    Tracey, D.J. (2004). "Ascending and descending pathways." In:
    Paxinos, G. (ed.), *The Rat Nervous System*, 3rd ed. (Medial
    lemniscus; internal arcuate fibers; dorsal column–medial
    lemniscus pathway — SENSORY, not motor.)
*   **RVLM and CVLM (contrast — grey-matter autonomic regions):**
    Guyenet, P.G. (2006). "The sympathetic control of blood
    pressure." *Nature Reviews Neuroscience* 7:335–346. (RVLM;
    sympathetic premotor neurons — DIFFERENT from the white-matter
    pyramid.)
*   NeuroNames — Pyramis medullae oblongatae; FMA — Pyramid of
    medulla oblongata.
"""