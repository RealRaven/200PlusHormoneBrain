"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.right
=============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── medullary_pyramid
                └── right   <-- THIS MODULE

**Primary synonym:** Right medullary pyramid; right pyramid of the
medulla oblongata; right pyramis medullae oblongatae; right
anterior pyramid; right bulbar pyramid; right medullary pyramidal
tract.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **right medullary segment** of the
**corticospinal** and **corticobulbar** tracts. It is **NOT** a
grey-matter nucleus, **NOT** the whole corticospinal tract, and
**NOT** the whole corticobulbar tract — it is the **right ventral
medullary portion** of those descending motor pathways, visible
as a **right ventral bulge** on the medullary surface.
**Part of:** The **medullary_pyramid** bilateral container — which
is part of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medullary_pyramid/`` → **direct
child** of the medullary_pyramid container. The **right**
medullary pyramid is one of the **two** structural children of
the container (the other is ``left``).
**Structural children:** **None.** This is a **leaf** module. The
right medullary pyramid is represented as a **single structure**
— it has **no structural children** of its own.
**Boundary status (NOT the left medullary pyramid — the
contralateral leaf):** **Boundary case — the right medullary
pyramid is NOT the left medullary pyramid.** The **left
medullary pyramid** (``.../medullary_pyramid/left/``) is the
**contralateral leaf** — the medullary pyramid of the **left**
medulla. **They are DIFFERENT LEAVES** — the ``left`` and
``right`` modules are the two sides of the **bilateral
container**. Consumers must **not** conflate the **right**
medullary pyramid with the **left** — resolve the left side via
``medullary_pyramid.left``.
**Boundary status (NOT the whole right corticospinal tract —
only the medullary segment):** **Boundary case — the right
medullary pyramid is NOT the whole right corticospinal tract.**
The **right corticospinal tract** extends from the **right motor
cortex** (via the **right corona radiata**, **right internal
capsule**, **right cerebral peduncle**, **right pons**) to the
**spinal cord**. The **right medullary pyramid** (here) is the
**right medullary segment** — the portion that **runs on the
ventral surface** of the right medulla. Consumers must **not**
conflate the **right medullary pyramid** with the **whole right
corticospinal tract**.
**Boundary status (NOT the whole right corticobulbar tract —
only the medullary segment):** **Boundary case — the right
medullary pyramid is NOT the whole right corticobulbar tract.**
The **right corticobulbar tract** extends from the **right motor
cortex** to the **right cranial nerve motor nuclei**. The
**right medullary pyramid** (here) carries the **right
corticobulbar fibers** that **travel through** the medullary
segment. Consumers must **not** conflate the two.
**Boundary status (NOT the pyramidal decussation — the
decussation is the CAUDAL END of the right pyramid):**
**Boundary case — the right medullary pyramid is NOT the
pyramidal decussation.** The **pyramidal decussation** is the
**crossing of the corticospinal fibers at the spinomedullary
junction** — the **caudal end** of the right medullary pyramid.
It is **where ~85–90% of right corticospinal fibers cross the
midline** to form the **left lateral corticospinal tract** (and
vice versa). The **right medullary pyramid** (here) is the
**right ventral column** that **leads to** the decussation.
Consumers must **not** conflate the **pyramid** with the
**decussation**.
**Boundary status (NOT the right spinal corticospinal tract —
the spinal segment is in the spinal_cord container):**
**Boundary case — the right medullary pyramid is NOT the right
spinal corticospinal tract.** The **right lateral corticospinal
tract** and the **right anterior corticospinal tract** are
**right spinal cord** structures — wired under
``.../spinal_cord/white_matter/right/corticospinal_tract/``.
The **right medullary pyramid** (here) is the **right medullary
segment** — **rostral** to the **pyramidal decussation** and the
**right spinal cord**. Consumers must **not** conflate the two.
**Boundary status (NOT the right internal capsule or right
cerebral peduncle — supratentorial / midbrain segments):**
**Boundary case — the right medullary pyramid is NOT the right
internal capsule or the right cerebral peduncle.** The **right
internal capsule** is a **supratentorial** white-matter
structure; the **right cerebral peduncle** (right crus cerebri)
is a **midbrain** structure. The **right medullary pyramid**
(here) is the **right medullary segment**. Consumers must **not**
conflate the **right medullary pyramid** with the **right
internal capsule** or the **right cerebral peduncle**.
**Boundary status (NOT the right pontine corticospinal tract —
that is in the metencephalon):** **Boundary case — the right
medullary pyramid is NOT the right pontine corticospinal tract.**
The **right pons** (``.../metencephalon/pons/``) contains the
**right pontine segment** of the corticospinal tract — the
fibers **disperse** among the **right pontine nuclei** and then
**reconverge** at the **right pontomedullary junction** to form
the **right medullary pyramid**. Consumers must **not** conflate
the two.
**Boundary status (NOT the right inferior olivary nucleus —
adjacent but DISTINCT):** **Boundary case — the right medullary
pyramid is NOT the right inferior olivary nucleus.** The **right
inferior olivary nucleus** (``.../olivary_body/right/``) is the
**right cerebellar climbing-fiber relay** — a **grey-matter**
structure **dorsolateral** to the right pyramid. The **right
medullary pyramid** (here) is a **white-matter tract**. **They
are DIFFERENT STRUCTURES** — the **olivary body** is
**grey-matter cerebellar relay**; the **pyramid** is
**white-matter motor tract**. Consumers must **not** conflate the
two.
**Boundary status (NOT the right arcuate nucleus — adjacent but
DISTINCT):** **Boundary case — the right medullary pyramid is
NOT the right arcuate nucleus.** The **right arcuate nucleus**
(``.../arcuate_nucleus/right/``) is a **right ventral-surface
grey-matter** chemosensory / hypothalamic-projecting nucleus,
adjacent to the right pyramid. The **right medullary pyramid**
(here) is a **white-matter tract**. **They are DIFFERENT
STRUCTURES** — the **arcuate nucleus** is **grey matter**; the
**pyramid** is **white matter**. Consumers must **not** conflate
the two.
**Boundary status (NOT the right RVLM / right CVLM —
ventrolateral, not ventral):** **Boundary case — the right
medullary pyramid is NOT the right RVLM or right CVLM.** The
**right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) and **right CVLM**
(``.../caudal_ventrolateral_medulla/right/``) are **ventrolateral
grey-matter autonomic** regions. The **right medullary pyramid**
(here) is a **ventral white-matter tract**. Consumers must **not**
conflate the two.
**Boundary status (NOT the right cranial nerve nuclei — dorsal /
ventrolateral grey matter):** **Boundary case — the right
medullary pyramid is NOT the right cranial nerve nuclei.** The
**right cranial nerve nuclei**
(``.../cranial_nerve_nuclei/right/``) are **dorsal and
ventrolateral grey-matter** nuclei. The **right medullary
pyramid** (here) is a **ventral white-matter tract**. The
**right corticobulbar fibers** that **innervate** the right
cranial nerve nuclei **travel through** the right pyramid region
— but the **tract** and the **nuclei** are **different
structures**. Consumers must **not** conflate the two.
**Boundary status (NOT the right medial lemniscus — a DIFFERENT
white-matter tract):** **Boundary case — the right medullary
pyramid is NOT the right medial lemniscus.** The **right medial
lemniscus** is a **right sensory** white-matter tract (fine
touch, vibration, proprioception) that runs **dorsal** to the
right pyramid. The **right medullary pyramid** (here) is a
**right motor** white-matter tract. Consumers must **not**
conflate the two.
**Boundary status (NOT the whole right medulla oblongata — a
small white-matter tract within it):** **Boundary case — the
right medullary pyramid is NOT the whole right medulla
oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the right cranial nerve nuclei, right autonomic nuclei,
right respiratory centers, right olivary body, right medullary
pyramid (here), right arcuate nucleus, and other structures. The
**right medullary pyramid** is **one white-matter tract** within
the right medulla. Consumers must **not** conflate the
**pyramid** with the **whole medulla**.

Overview
--------
The **right medullary pyramid** is the **right ventral
white-matter column** of the **medulla oblongata** — the **right
medullary segment** of the **right corticospinal** and **right
corticobulbar** tracts. It appears as a **right ventral bulge**
on the medullary surface, **right of the anterior median
fissure**, and it **leads caudally** to the **pyramidal
decussation** at the **spinomedullary junction**.

**This is a LEAF module.** The **right medullary pyramid** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **tract-level** resolution of the
right side use this module; consumers that need **left-side**
resolution use ``.../medullary_pyramid/left/``; consumers that
need the **whole medullary_pyramid container** use
``.../medullary_pyramid/``.

**The right medullary pyramid is a WHITE-MATTER TRACT, NOT a
grey-matter nucleus.** It is the **right descending motor
column** — the **right corticospinal fibers** (to the spinal
cord) and **right corticobulbar fibers** (to the right cranial
nerve motor nuclei) **pass through** it.

**The right medullary pyramid is the MEDULLARY SEGMENT, NOT the
whole right corticospinal or corticobulbar tract.** The **whole
right corticospinal tract** extends from the **right motor
cortex** to the **spinal cord**; the **whole right
corticobulbar tract** extends from the **right motor cortex** to
the **right cranial nerve motor nuclei**. The **right medullary
pyramid** (here) is the **right ventral medullary segment**.

**The right medullary pyramid leads to the PYRAMIDAL DECUSSATION.**
At the **spinomedullary junction**, **~85–90% of right
corticospinal fibers cross the midline** to form the **left
lateral corticospinal tract** in the **left spinal cord** — and
conversely. **The decussation is the caudal landmark** of the
right medullary pyramid — **NOT** a separate module in the tree.

The Right Medullary Pyramid / Left Medullary Pyramid Boundary
-------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right medullary pyramid** (this module) — the medullary
    pyramid of the **right** medulla.

*   **Left medullary pyramid** (``.../medullary_pyramid/left/``)
    — the medullary pyramid of the **left** medulla.

**The two are the SIDES of the bilateral medullary_pyramid
container.** They are **structurally symmetric mirror pairs** —
same white-matter composition, same corticospinal and
corticobulbar fiber content, same **no warning**. Consumers must
**not** conflate the right with the left — resolve the left side
via ``medullary_pyramid.left``.

The Right Medullary Pyramid / Whole Right Corticospinal and Corticobulbar Tracts Boundary
-----------------------------------------------------------------------------------------
This is the **segment** boundary:

*   **Right medullary pyramid** (this module) — the **right
    medullary segment**.

*   **Whole right corticospinal tract** and **whole right
    corticobulbar tract** — the **whole pathways** from the
    **right motor cortex** to their targets.

**The right medullary pyramid is a SPECIFIC SEGMENT.** Consumers
must **not** conflate it with the **whole** tract.

The Right Medullary Pyramid / Pyramidal Decussation Boundary
------------------------------------------------------------
This is the **column / crossing** boundary:

*   **Right medullary pyramid** (this module) — the **right
    ventral column** that **leads to** the decussation.

*   **Pyramidal decussation** — the **crossing** of the
    corticospinal fibers at the **spinomedullary junction** — the
    **caudal landmark** of the right pyramid.

**The decussation is the CAUDAL END of the right pyramid.**
Consumers must **not** conflate the **column** with the
**crossing**.

The Right Medullary Pyramid / Right Spinal Corticospinal Tract Boundary
-----------------------------------------------------------------------
This is the **medullary / spinal** boundary:

*   **Right medullary pyramid** (this module) — the **right
    medullary segment**.

*   **Right spinal corticospinal tract**
    (``.../spinal_cord/white_matter/right/corticospinal_tract/``)
    — the **right spinal segment** after the **pyramidal
    decussation**.

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**
Consumers must **not** descend from the right medullary pyramid
into the spinal cord; resolve the right spinal corticospinal
tract via the **spinal cord** container.

The Right Medullary Pyramid / Right Inferior Olivary Nucleus Boundary
----------------------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Right medullary pyramid** (this module) — the **right
    ventral white-matter** motor tract.

*   **Right inferior olivary nucleus**
    (``.../olivary_body/right/``) — the **right dorsolateral
    grey-matter** cerebellar climbing-fiber relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Medullary Pyramid / Right Arcuate Nucleus Boundary
------------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Right medullary pyramid** (this module) — the **right
    ventral white-matter** motor tract.

*   **Right arcuate nucleus** (``.../arcuate_nucleus/right/``) —
    a **right ventral-surface grey-matter** chemosensory /
    hypothalamic-projecting nucleus, adjacent to the right
    pyramid.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Medullary Pyramid / Right RVLM and Right CVLM Boundary
----------------------------------------------------------------
This is the **ventral / ventrolateral** boundary:

*   **Right medullary pyramid** (this module) — the **right
    ventral** white-matter motor tract.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``)
    and **right CVLM**
    (``.../caudal_ventrolateral_medulla/right/``) — the **right
    ventrolateral** grey-matter autonomic regions.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Medullary Pyramid / Right Cranial Nerve Nuclei Boundary
-----------------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Right medullary pyramid** (this module) — the **right
    ventral** white-matter motor tract.

*   **Right cranial nerve nuclei**
    (``.../cranial_nerve_nuclei/right/``) — the **right dorsal
    and ventrolateral** grey-matter motor nuclei.

**They are DIFFERENT STRUCTURES.** The **right corticobulbar
fibers** that **innervate** the right cranial nerve nuclei
**travel through** the right pyramid region — but the **tract**
and the **nuclei** are **different structures**.

The Right Medullary Pyramid / Right Medial Lemniscus Boundary
-------------------------------------------------------------
This is the **motor / sensory white-matter** boundary:

*   **Right medullary pyramid** (this module) — the **right
    ventral motor** white-matter tract.

*   **Right medial lemniscus** — the **right dorsal sensory**
    white-matter tract.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

Function in the Human Brain
---------------------------
The right medullary pyramid's function is **right motor
conduction** — the **right medullary segment** of the **right
corticospinal and corticobulbar tracts** — **NOT sensory
conduction**, **NOT cerebellar conduction**, and **NOT autonomic
conduction**:

*   **Right corticospinal conduction (medullary segment):** The
    **right medullary pyramid** carries the **right corticospinal
    fibers** from the **right motor cortex** to the **pyramidal
    decussation** and then to the **left spinal cord** (after
    crossing) — the **upper motor neuron** pathway for
    **voluntary movement** of the **left body**.

*   **Right corticobulbar conduction (medullary segment):** The
    **right medullary pyramid** carries the **right corticobulbar
    fibers** from the **right motor cortex** to the **left and
    right medullary cranial nerve motor nuclei** (via crossing at
    or above the decussation). Some fibers **leave the pyramid**
    at the level of their target nuclei.

*   **NOT sensory:** The **right medial lemniscus** (adjacent) is
    the **right sensory** tract — **NOT** the right pyramid.

*   **NOT cerebellar:** The **right inferior cerebellar peduncle**
    and the **right inferior olivary nucleus** (adjacent) are the
    **right cerebellar** pathways — **NOT** the right pyramid.

*   **NOT autonomic:** The **right RVLM** and **right CVLM**
    (ventrolateral) are the **right autonomic** structures —
    **NOT** the right pyramid.

**The unifying theme:** the right medullary pyramid is the
**right ventral white-matter column** of the **right medulla
oblongata** — the **right medullary segment** of the **right
corticospinal and right corticobulbar tracts**, conducting
**upper motor neuron** signals from the **right motor cortex** to
the **left spinal cord** (after decussation) and to the **left
and right medullary cranial nerve motor nuclei**.

Associated Disorders
--------------------
The right medullary pyramid is the **substrate** for
**well-defined clinical syndromes** — its clinical relevance is
**direct**, via **upper motor neuron** dysfunction:

*   **Right medial medullary syndrome (Dejerine syndrome /
    anterior spinal artery syndrome — via the right medullary
    pyramid):** Infarction of the **right medial medulla** —
    **left contralateral hemiparesis** (right pyramid), **left
    contralateral loss of proprioception/vibration** (right
    medial lemniscus — **NOT** in this container), and **right
    ipsilateral tongue weakness** (right hypoglossal
    nucleus/nerve — **NOT** in this container). The **right
    medullary pyramid** is the **direct substrate** of the
    **left hemiparesis** in right medial medullary syndrome.

*   **Pseudobulbar palsy (via right corticobulbar tract in the
    pyramid):** **Bilateral** corticobulbar lesions —
    **dysarthria**, **dysphagia**, **emotional lability** — from
    **right and left corticobulbar fiber** damage. The **right
    medullary pyramid** carries the **right corticobulbar
    fibers** that contribute to the **upper motor neuron**
    component of pseudobulbar palsy.

*   **Amyotrophic lateral sclerosis (via right corticospinal
    degeneration):** **Upper motor neuron** degeneration of the
    **right corticospinal tract** — including the **right
    medullary pyramid** — contributes to **spasticity**,
    **hyperreflexia**, and **Babinski sign** in ALS. The **right
    medullary pyramid** is the **right medullary segment** of the
    degenerating **upper motor neuron** pathway.

*   **Hereditary spastic paraplegia (via right corticospinal
    degeneration):** **Upper motor neuron** degeneration of the
    **right corticospinal tract** — including the **right
    medullary pyramid** — causes **progressive spasticity** and
    **gait impairment**. The **right medullary pyramid** is the
    **right medullary segment** of the degenerating pathway.

*   **Primary lateral sclerosis (via right corticospinal
    degeneration):** A **pure upper motor neuron** disorder —
    **right corticospinal tract** degeneration (including the
    **right medullary pyramid**) — causes **progressive
    spasticity** and **weakness**. The **right medullary
    pyramid** is the **right medullary segment** of the
    degenerating pathway.

*   **No Named "Right Medullary Pyramid Syndrome":** The right
    medullary pyramid is a **white-matter tract** — its clinical
    relevance is **direct**, via the **upper motor neuron**
    findings of the **broader brainstem lesion** (medial
    medullary syndrome) or the **neurological disorder** (ALS,
    HSP, PLS), **not** for the pyramid itself.

**What is NOT here:** The right medullary pyramid is **not** the
substrate for **sensory loss** (right medial lemniscus, right
spinothalamic tract — **NOT** in this container), **cerebellar
ataxia** (right inferior cerebellar peduncle, right inferior
olivary nucleus — **NOT** in this container), or **autonomic
dysfunction** (right RVLM, right CVLM, right NTS — **NOT** in
this container). Its clinical relevance is the **upper motor
neuron** functions listed above.

Lateralization Notes
--------------------
This is the **right** medullary pyramid module. The medullary
pyramid is a **bilateral container** whose two sides are
**structurally symmetric mirror pairs** — and it carries **NO
warning**:

*   **Bilateral Symmetry:** The **right** and **left** medullary
    pyramids are **structurally symmetric** — they are **mirror
    pairs** with the **same** white-matter composition, **same**
    corticospinal and corticobulbar fiber content, and **same**
    no warning. The **right** pyramid carries fibers from the
    **right motor cortex**; the **left** pyramid carries fibers
    from the **left motor cortex**.

*   **Contralateral Motor Control (corticospinal):** The
    **pyramidal decussation** at the **spinomedullary junction**
    crosses **~85–90%** of right corticospinal fibers, so the
    **right medullary pyramid** controls the **left** body. This
    is a **functional** contralaterality — the **pyramid itself**
    is structurally **symmetric**.

*   **NO Lateralization Warning:** The medullary pyramid has **no
    known functional lateralization** at the **tract level**.
    Consumers must **not** import a **lateralization warning**
    into the right medullary pyramid — the **right** and **left**
    pyramids are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right medullary
    pyramid is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the right medullary pyramid.

*   **NO Fear-Output Warning:** The right medullary pyramid is
    **not** a fear-output structure — it is a **ventral
    white-matter motor tract**. Consumers must **not** conflate
    it with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "right medullary pyramid = left
medullary pyramid" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**tract level**. The medullary pyramid is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no fear-output
warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right medullary pyramid
    is a **leaf** — it does **not** import from ``.../left/`` or
    any other left-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../olivary_body/``, ``.../arcuate_nucleus/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../solitary_nucleus/``, ``.../ventral_respiratory_group/``,
    ``.../metencephalon/``, ``.../midbrain/``,
    ``.../spinal_cord/``, or any other container. The right
    medullary pyramid's relationships to the right olivary body,
    right arcuate nucleus, right RVLM, right CVLM, right cranial
    nerve nuclei, right medial lemniscus, and the right spinal
    corticospinal tract are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right medullary
    pyramid is a **single structure** — it has **no structural
    children**. Consumers must **not** expect further sub-paths
    under ``.../right/``.
*   **NOT the left medullary pyramid.** The left medullary pyramid
    is a **separate leaf** under
    ``.../medullary_pyramid/left/``. Consumers must **not**
    conflate the right with the left.
*   **NOT the whole right corticospinal or corticobulbar tract.**
    The right medullary pyramid is the **right medullary
    segment** — **NOT** the whole pathway.
*   **NOT the pyramidal decussation.** The decussation is the
    **caudal end** of the right pyramid — **NOT** a separate
    module.
*   **NOT the right spinal corticospinal tract.** The right
    spinal segment is wired under
    ``.../spinal_cord/white_matter/right/corticospinal_tract/``.
*   **NOT the right internal capsule or right cerebral peduncle.**
    Those are **supratentorial / midbrain** segments of the
    pathway.
*   **NOT the right inferior olivary nucleus or right arcuate
    nucleus.** Those are **right grey-matter** structures
    adjacent to the right pyramid.
*   **NOT the right RVLM or right CVLM.** Those are **right
    ventrolateral grey-matter autonomic** structures.
*   **NOT the right cranial nerve nuclei.** Those are **right
    dorsal / ventrolateral grey-matter motor** nuclei.
*   **NOT the right medial lemniscus.** That is the **right dorsal
    sensory** white-matter tract.
*   **No ``AREA_PATHS`` hop.** The right medullary pyramid is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The right medullary pyramid has
    no nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the left medullary pyramid — strict
    mirror with NO warning.** The right and left modules are
    **structurally identical** — same leaf status, same
    **white-matter motor tract** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "medullary_pyramid.right"
    )

**Do not** assume the right medullary pyramid is the **left
medullary pyramid**. The left medullary pyramid is the
**separate leaf** at ``.../medullary_pyramid/left/``.

**Do not** assume the right medullary pyramid is the **whole
right corticospinal or corticobulbar tract**. It is the **right
medullary segment** — **NOT** the whole pathway.

**Do not** assume the right medullary pyramid is the **pyramidal
decussation**. The decussation is the **caudal end** of the
right pyramid — **NOT** a separate module.

**Do not** assume the right medullary pyramid is the **right
spinal corticospinal tract**. The right spinal segment is wired
under ``.../spinal_cord/white_matter/right/corticospinal_tract/``.

**Do not** assume the right medullary pyramid is the **right
inferior olivary nucleus**, the **right arcuate nucleus**, the
**right RVLM**, the **right CVLM**, or the **right cranial nerve
nuclei**. Those are **right grey-matter** structures — **NOT**
the white-matter pyramid.

**Do not** assume the right medullary pyramid is the **right
medial lemniscus**. The right medial lemniscus is a **right
sensory** white-matter tract — **NOT** the right motor pyramid.

**Do not** assume the right medullary pyramid has **structural
children**. It is a **leaf** — it represents the right
medullary pyramid as a **single structure**.

Iterating the right medullary pyramid's (empty) children
(recommended consumer pattern)::

    RIGHT_MEDULLARY_PYRAMID_CHILDREN = ()
    # The right medullary pyramid is a leaf. It has no structural
    # children.

Reaching the left medullary pyramid (recommended consumer
pattern — the contralateral leaf)::

    # The left medullary pyramid is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.left
    #
    # The right and left medullary pyramids are structurally
    # symmetric mirror pairs of white-matter motor tracts.

Reaching the right spinal corticospinal tract (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The right spinal corticospinal tract is a SEPARATE
    # structure in the SPINAL CORD container:
    #
    #   spinal_cord.white_matter.right.corticospinal_tract
    #
    # The right medullary pyramid is the RIGHT MEDULLARY segment;
    # the right spinal corticospinal tract is the RIGHT SPINAL
    # segment after the pyramidal decussation.

Reaching the right inferior olivary nucleus (recommended
consumer pattern — NOTE the DIFFERENT structure)::

    # The right inferior olivary nucleus is a GREY-MATTER
    # cerebellar relay, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.right
    #
    # The right olivary body is DORSOLATERAL to the right
    # pyramid — adjacent but DISTINCT.

Reaching the right arcuate nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The right arcuate nucleus is a VENTRAL-SURFACE grey-matter
    # chemosensory nucleus, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.right
    #
    # The right arcuate nucleus is ADJACENT to the right pyramid
    # at the ventral medullary surface — but it is grey matter,
    # not white matter.

Reaching the right RVLM and right CVLM (recommended consumer
pattern — NOTE the DIFFERENT structures)::

    # The right RVLM and right CVLM are VENTROLATERAL grey-matter
    # autonomic regions, NOT the ventral white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.right
    #
    # The right pyramid is VENTRAL; the right RVLM and right CVLM
    # are VENTROLATERAL — different locations, different
    # structures.

Reaching the right cranial nerve nuclei (recommended consumer
pattern — NOTE the DIFFERENT structures)::

    # The right cranial nerve nuclei are DORSAL / VENTROLATERAL
    # grey-matter motor nuclei, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right
    #
    # The right corticobulbar fibers from the right pyramid
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