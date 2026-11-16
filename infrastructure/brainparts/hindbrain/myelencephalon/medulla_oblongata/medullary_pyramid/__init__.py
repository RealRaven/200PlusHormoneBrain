"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid
=======================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── medullary_pyramid   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Medullary pyramid; pyramid of the medulla
oblongata; pyramis medullae oblongatae; anterior pyramid; bulbar
pyramid; medullary pyramidal tract.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **medullary segment** of the
**corticospinal** and **corticobulbar** tracts. It is **NOT** a
grey-matter nucleus, **NOT** the whole corticospinal tract, and
**NOT** the whole corticobulbar tract — it is the **ventral
medullary portion** of those descending motor pathways, visible
as a **paired ventral bulge** on the medullary surface.
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** medullary
pyramid. The bilateral pyramids are the **structural children**
of this **bilateral container**; the container itself is
**unpaired**.
**Boundary status (NOT the whole corticospinal tract — only the
medullary segment):** **Boundary case — the medullary pyramid is
NOT the whole corticospinal tract.** The **corticospinal tract**
is a **long descending pathway** that extends from the **motor
cortex** (via the **corona radiata**, **internal capsule**,
**cerebral peduncle**, **pons**) to the **spinal cord**. The
**medullary pyramid** (here) is the **medullary segment** of that
pathway — the portion that **runs on the ventral surface** of the
medulla, from the **pontomedullary junction** to the
**spinomedullary junction** (where the **pyramidal decussation**
occurs). The **supratentorial**, **capsular**, **peduncular**,
**pontine**, and **spinal** segments are **different structures**
in **different containers**. Consumers must **not** conflate the
**medullary pyramid** with the **whole corticospinal tract** —
the pyramid is a **specific medullary segment**.
**Boundary status (NOT the whole corticobulbar tract — only the
medullary segment):** **Boundary case — the medullary pyramid is
NOT the whole corticobulbar tract.** The **corticobulbar tract**
is a **descending pathway** from the **motor cortex** to the
**cranial nerve motor nuclei** (including those in the **pons**,
**midbrain**, and **medulla**). The **medullary pyramid** (here)
carries **corticobulbar fibers** that **leave the pyramid** at
the level of their **target nuclei** (hypoglossal, nucleus
ambiguus, dorsal motor nucleus of the vagus, inferior salivatory
nucleus) — but the **whole corticobulbar tract** extends from the
**cortex** to those nuclei. The **medullary pyramid** is the
**medullary segment** — **NOT** the whole corticobulbar tract.
Consumers must **not** conflate the two.
**Boundary status (NOT the pyramidal decussation — the decussation
is the CAUDAL END of the pyramid):** **Boundary case — the
medullary pyramid is NOT the pyramidal decussation.** The
**pyramidal decussation** is the **crossing of the corticospinal
fibers at the spinomedullary junction** — the **caudal end** of
the medullary pyramid. It is **where ~85–90% of corticospinal
fibers cross the midline** to form the **lateral corticospinal
tract** in the spinal cord. The **medullary pyramid** (here) is
the **paired ventral column** that **leads to** the decussation.
**The decussation is a landmark at the caudal boundary of the
pyramid**, not a separate structure. Consumers must **not**
conflate the **pyramid** with the **decussation** — the
**decussation** is the **crossing** at the **caudal end**; the
**pyramid** is the **column** leading to it.
**Boundary status (NOT the spinal cord corticospinal tract — the
spinal segment is in the spinal_cord container):** **Boundary
case — the medullary pyramid is NOT the spinal cord corticospinal
tract.** The **lateral corticospinal tract** and the **anterior
corticospinal tract** are **spinal cord** structures — wired
under ``.../spinal_cord/white_matter/{left,right}/corticospinal_tract/``.
The **medullary pyramid** (here) is the **medullary segment** —
**rostral** to the **pyramidal decussation** and the **spinal
cord**. **They are DIFFERENT STRUCTURES in DIFFERENT
CONTAINERS** — the **medullary pyramid** is the **medullary
column**; the **spinal corticospinal tract** is the **spinal
column** after the decussation. Consumers must **not** conflate
the two.
**Boundary status (NOT the internal capsule or cerebral peduncle
— those are supratentorial / midbrain segments):** **Boundary
case — the medullary pyramid is NOT the internal capsule or the
cerebral peduncle.** The **internal capsule** is a
**supratentorial** white-matter structure (telencephalon /
diencephalon); the **cerebral peduncle** (crus cerebri) is a
**midbrain** structure. The **medullary pyramid** (here) is the
**medullary segment** of the corticospinal / corticobulbar
pathway. **They are DIFFERENT STRUCTURES in DIFFERENT
CONTAINERS.** Consumers must **not** conflate the **medullary
pyramid** with the **internal capsule** or the **cerebral
peduncle**.
**Boundary status (NOT the pontine corticospinal tract — that is
in the metencephalon):** **Boundary case — the medullary pyramid
is NOT the pontine corticospinal tract.** The **pons**
(``.../metencephalon/pons/``) contains the **pontine segment** of
the corticospinal tract — the fibers **disperse** among the
**pontine nuclei** and then **reconverge** at the
**pontomedullary junction** to form the **medullary pyramid**.
The **medullary pyramid** (here) is the **medullary segment** —
**caudal** to the pons. Consumers must **not** conflate the
**medullary pyramid** with the **pontine corticospinal tract**.
**Boundary status (NOT the inferior olivary nucleus — adjacent
but DISTINCT):** **Boundary case — the medullary pyramid is NOT
the inferior olivary nucleus.** The **inferior olivary nucleus**
(``.../olivary_body/``) is the **cerebellar climbing-fiber
relay** — a **grey-matter** structure **dorsolateral** to the
pyramid. The **medullary pyramid** (here) is a **white-matter
tract** — the **corticospinal / corticobulbar** column. **They
are DIFFERENT STRUCTURES** — the **olivary body** is
**grey-matter cerebellar relay**; the **pyramid** is
**white-matter motor tract**. They are **adjacent** in the
**ventral medulla** (the pyramid is **medial**, the olivary body
is **lateral**), but they are **functionally and structurally
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the arcuate nucleus — adjacent but
DISTINCT):** **Boundary case — the medullary pyramid is NOT the
arcuate nucleus.** The **arcuate nucleus**
(``.../arcuate_nucleus/``) is a **ventral-surface grey-matter
nucleus** — a **chemosensory / hypothalamic-projecting** structure
at the **ventral medullary surface**, adjacent to the **anterior
median fissure** and the **pyramid**. The **medullary pyramid**
(here) is a **white-matter tract** — the **corticospinal /
corticobulbar** column. **They are DIFFERENT STRUCTURES** — the
**arcuate nucleus** is **grey matter** (neurons); the **pyramid**
is **white matter** (descending motor fibers). They are
**adjacent** at the **ventral medullary surface**, but they are
**functionally and structurally distinct**. Consumers must **not**
conflate the two.
**Boundary status (NOT the RVLM / CVLM — ventrolateral, not
ventral):** **Boundary case — the medullary pyramid is NOT the
RVLM or CVLM.** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) and **CVLM**
(``.../caudal_ventrolateral_medulla/``) are **ventrolateral
grey-matter autonomic** regions — the **sympathetic premotor**
center and the **sympathoinhibitory** relay, respectively. The
**medullary pyramid** (here) is a **ventral white-matter tract**
— the **corticospinal / corticobulbar** column. **They are
DIFFERENT STRUCTURES** — the **RVLM** and **CVLM** are
**grey-matter autonomic** nuclei; the **pyramid** is a
**white-matter motor tract**. Consumers must **not** conflate the
two.
**Boundary status (NOT the cranial nerve nuclei — dorsal /
ventrolateral grey matter):** **Boundary case — the medullary
pyramid is NOT the cranial nerve nuclei.** The **cranial nerve
nuclei** (``.../cranial_nerve_nuclei/``) are **dorsal and
ventrolateral grey-matter** nuclei — the **hypoglossal nucleus**
(dorsal), the **dorsal motor nucleus of the vagus** (dorsal), the
**inferior salivatory nucleus** (ventrolateral), and the
**nucleus ambiguus** (ventrolateral). The **medullary pyramid**
(here) is a **ventral white-matter tract**. **They are DIFFERENT
STRUCTURES** — the **cranial nerve nuclei** are **grey-matter
motor nuclei**; the **pyramid** is a **white-matter motor
tract**. Consumers must **not** conflate the two.
**Boundary status (NOT the medial lemniscus — a DIFFERENT
white-matter tract):** **Boundary case — the medullary pyramid is
NOT the medial lemniscus.** The **medial lemniscus** is a
**dorsal-column–medial-lemniscus** pathway — a **sensory**
white-matter tract that runs **dorsal** to the pyramid and
**decussates** as the **internal arcuate fibers** at the level
of the **gracile and cuneate nuclei**. The **medullary pyramid**
(here) is a **motor** white-matter tract. **They are DIFFERENT
STRUCTURES** — the **medial lemniscus** is **sensory** (fine
touch, vibration, proprioception); the **pyramid** is **motor**
(corticospinal / corticobulbar). They are **adjacent** in the
**medulla**, but they are **functionally distinct**. Consumers
must **not** conflate the two.
**Boundary status (NOT the whole medulla oblongata — a small
white-matter tract within it):** **Boundary case — the medullary
pyramid is NOT the whole medulla oblongata.** The **medulla
oblongata** (``.../medulla_oblongata/``) is the **parent
container** — it contains the cranial nerve nuclei, the autonomic
nuclei, the respiratory centers, the olivary body, the medullary
pyramid (here), the arcuate nucleus, and other structures. The
**medullary pyramid** is **one white-matter tract** within the
medulla. Consumers must **not** conflate the **pyramid** with the
**whole medulla**.
**Boundary status (BILATERAL container — left and right are
structural children):** **Boundary case — the medullary pyramid
is a BILATERAL container with ``left`` and ``right`` structural
children.** The **medullary_pyramid** module (here) is an
**unpaired container**; its **structural children** are ``left``
and ``right`` — each a **leaf** representing the **left** or
**right** medullary pyramid. Consumers must **not** look for a
single unpaired medullary pyramid — the **left** and **right**
pyramids are **separate modules** under this container. Resolve
them via ``medullary_pyramid.left`` and
``medullary_pyramid.right``.

Overview
--------
The medullary pyramid is the **ventral white-matter column** of
the **medulla oblongata** — the **medullary segment** of the
**corticospinal** and **corticobulbar** tracts. It appears as a
**paired ventral bulge** on the medullary surface, flanking the
**anterior median fissure**, and it **leads caudally** to the
**pyramidal decussation** at the **spinomedullary junction**.

**The medullary pyramid is a WHITE-MATTER TRACT, NOT a grey-matter
nucleus.** It is the **descending motor column** — the
**corticospinal fibers** (to the spinal cord) and
**corticobulbar fibers** (to the cranial nerve motor nuclei)
**pass through** it. It is **NOT** the **inferior olivary
nucleus** (adjacent grey matter), **NOT** the **arcuate nucleus**
(adjacent grey matter), and **NOT** the **medial lemniscus**
(adjacent sensory tract).

**The medullary pyramid is the MEDULLARY SEGMENT, NOT the whole
corticospinal or corticobulbar tract.** The **whole
corticospinal tract** extends from the **motor cortex** to the
**spinal cord**; the **whole corticobulbar tract** extends from
the **motor cortex** to the **cranial nerve motor nuclei**. The
**medullary pyramid** (here) is the **ventral medullary
segment** — the portion that **runs on the ventral surface** of
the medulla, between the **pontomedullary junction** and the
**pyramidal decussation**.

**The medullary pyramid is a BILATERAL container.** Its
structural children are ``left`` and ``right`` — each a leaf
representing the left or right medullary pyramid. The **container
itself** is **unpaired**.

**The medullary pyramid leads to the PYRAMIDAL DECUSSATION.** At
the **spinomedullary junction**, **~85–90% of corticospinal
fibers cross the midline** to form the **lateral corticospinal
tract** in the **contralateral spinal cord**; the remaining
**~10–15%** continue **ipsilaterally** as the **anterior
corticospinal tract** (which **decussates segmentally** at the
spinal cord level). **The decussation is the caudal landmark** of
the medullary pyramid — **NOT** a separate module in the tree.

Bilateral Structure
-------------------
The medullary pyramid is a **bilateral container** with **two
structural children**:

*   ``left`` — the **left** medullary pyramid (a leaf module).
*   ``right`` — the **right** medullary pyramid (a leaf module).

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left** and
**right** medullary pyramids as **single structures**, not as
further sub-containers. Consumers that need **side-specific**
resolution should descend into ``left`` or ``right``; consumers
that need **bilateral** resolution should iterate over both.

**The container itself is unpaired.** There is **no**
``medullary_pyramid/left/.../`` structural hierarchy beyond the
single leaf level — the ``left`` and ``right`` modules are the
**terminal modules** for this structure.

The Medullary Pyramid / Whole Corticospinal and Corticobulbar Tracts Boundary
-----------------------------------------------------------------------------
This is the **most consequential** segment boundary:

*   **Medullary pyramid** (this module) — the **medullary segment**
    of the corticospinal and corticobulbar tracts.

*   **Whole corticospinal tract** — **cortex → corona radiata →
    internal capsule → cerebral peduncle → pons → medullary
    pyramid → pyramidal decussation → lateral / anterior
    corticospinal tract in the spinal cord**.

*   **Whole corticobulbar tract** — **cortex → corona radiata →
    internal capsule → cerebral peduncle → pons → medullary
    pyramid → cranial nerve motor nuclei**.

**The medullary pyramid is a SPECIFIC SEGMENT.** Consumers must
**not** conflate it with the **whole** tract — the **supratentorial**,
**capsular**, **peduncular**, **pontine**, and **spinal**
segments are **different structures** in **different containers**.

The Medullary Pyramid / Pyramidal Decussation Boundary
------------------------------------------------------
This is the **column / crossing** boundary:

*   **Medullary pyramid** (this module) — the **ventral column**
    that **leads to** the decussation.

*   **Pyramidal decussation** — the **crossing** of the
    corticospinal fibers at the **spinomedullary junction** — the
    **caudal landmark** of the pyramid.

**The decussation is the CAUDAL END of the pyramid**, not a
separate structure. Consumers must **not** conflate the
**column** with the **crossing**.

The Medullary Pyramid / Spinal Cord Corticospinal Tract Boundary
----------------------------------------------------------------
This is the **medullary / spinal** boundary:

*   **Medullary pyramid** (this module) — the **medullary
    segment** of the corticospinal tract.

*   **Spinal corticospinal tract**
    (``.../spinal_cord/white_matter/{left,right}/corticospinal_tract/``)
    — the **spinal segment** after the **pyramidal decussation**.

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**
Consumers must **not** descend from the medullary pyramid into the
spinal cord; resolve the spinal corticospinal tract via the
**spinal cord** container.

The Medullary Pyramid / Inferior Olivary Nucleus Boundary
---------------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Medullary pyramid** (this module) — the **ventral
    white-matter** motor tract.

*   **Inferior olivary nucleus** (``.../olivary_body/``) — the
    **dorsolateral grey-matter** cerebellar climbing-fiber relay.

**They are DIFFERENT STRUCTURES** — the **olivary body** is
**grey-matter cerebellar relay**; the **pyramid** is
**white-matter motor tract**. They are **adjacent** in the
**ventral medulla** (the pyramid is **medial**, the olivary body
is **lateral**), but they are **functionally and structurally
distinct**. Consumers must **not** conflate the two.

The Medullary Pyramid / Arcuate Nucleus Boundary
------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Medullary pyramid** (this module) — the **ventral
    white-matter** motor tract.

*   **Arcuate nucleus** (``.../arcuate_nucleus/``) — a
    **ventral-surface grey-matter** chemosensory / hypothalamic-
    projecting nucleus, adjacent to the pyramid.

**They are DIFFERENT STRUCTURES** — the **arcuate nucleus** is
**grey matter**; the **pyramid** is **white matter**. They are
**adjacent** at the **ventral medullary surface**, but they are
**functionally and structurally distinct**. Consumers must **not**
conflate the two.

The Medullary Pyramid / RVLM and CVLM Boundary
----------------------------------------------
This is the **ventral / ventrolateral** boundary:

*   **Medullary pyramid** (this module) — the **ventral**
    white-matter motor tract.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) and
    **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **ventrolateral** grey-matter autonomic regions.

**They are DIFFERENT STRUCTURES** — the **RVLM** and **CVLM** are
**grey-matter autonomic** nuclei; the **pyramid** is a
**white-matter motor tract**. Consumers must **not** conflate the
two.

The Medullary Pyramid / Cranial Nerve Nuclei Boundary
-----------------------------------------------------
This is the **white-matter / grey-matter** boundary:

*   **Medullary pyramid** (this module) — the **ventral**
    white-matter motor tract.

*   **Cranial nerve nuclei** (``.../cranial_nerve_nuclei/``) —
    the **dorsal and ventrolateral** grey-matter motor nuclei.

**They are DIFFERENT STRUCTURES** — the **cranial nerve nuclei**
are **grey-matter motor nuclei**; the **pyramid** is a
**white-matter motor tract**. The **corticobulbar fibers** that
**innervate** the cranial nerve nuclei **travel through** the
pyramid region — but the **tract** and the **nuclei** are
**different structures**. Consumers must **not** conflate the
two.

The Medullary Pyramid / Medial Lemniscus Boundary
-------------------------------------------------
This is the **motor / sensory white-matter** boundary:

*   **Medullary pyramid** (this module) — the **ventral motor**
    white-matter tract.

*   **Medial lemniscus** — the **dorsal sensory** white-matter
    tract (fine touch, vibration, proprioception).

**They are DIFFERENT STRUCTURES** — the **medial lemniscus** is
**sensory**; the **pyramid** is **motor**. They are **adjacent**
in the **medulla**, but they are **functionally distinct**.
Consumers must **not** conflate the two.

Function in the Human Brain
---------------------------
The medullary pyramid's function is **motor conduction** — the
**medullary segment** of the **corticospinal and corticobulbar
tracts** — **NOT sensory conduction**, **NOT cerebellar
conduction**, and **NOT autonomic conduction**:

*   **Corticospinal conduction (medullary segment):** The
    **medullary pyramid** carries the **corticospinal fibers**
    from the **motor cortex** to the **pyramidal decussation**
    and then to the **spinal cord** — the **upper motor neuron**
    pathway for **voluntary movement** of the **contralateral
    body**.

*   **Corticobulbar conduction (medullary segment):** The
    **medullary pyramid** carries the **corticobulbar fibers**
    from the **motor cortex** to the **medullary cranial nerve
    motor nuclei** — the **hypoglossal nucleus**, **nucleus
    ambiguus**, **dorsal motor nucleus of the vagus**, and
    **inferior salivatory nucleus**. Some fibers **leave the
    pyramid** at the level of their target nuclei.

*   **NOT sensory:** The **medial lemniscus** (adjacent) is the
    **sensory** tract — **NOT** the pyramid.

*   **NOT cerebellar:** The **inferior cerebellar peduncle** and
    the **inferior olivary nucleus** (adjacent) are the
    **cerebellar** pathways — **NOT** the pyramid.

*   **NOT autonomic:** The **RVLM** and **CVLM** (ventrolateral)
    are the **autonomic** structures — **NOT** the pyramid.

**The unifying theme:** the medullary pyramid is the **ventral
white-matter column** of the **medulla oblongata** — the
**medullary segment** of the **corticospinal and corticobulbar
tracts**, conducting **upper motor neuron** signals from the
**motor cortex** to the **spinal cord** (corticospinal) and the
**cranial nerve motor nuclei** (corticobulbar), and leading to the
**pyramidal decussation** at the **spinomedullary junction**.

Associated Disorders
--------------------
The medullary pyramid is the **substrate** for **well-defined
clinical syndromes** — its clinical relevance is **direct**, via
**upper motor neuron** dysfunction:

*   **Medial medullary syndrome (Dejerine syndrome / anterior
    spinal artery syndrome — via the medullary pyramid):**
    Infarction of the **medial medulla** — **contralateral
    hemiparesis** (pyramid), **contralateral loss of
    proprioception/vibration** (medial lemniscus — **NOT** in this
    container), and **ipsilateral tongue weakness** (hypoglossal
    nucleus/nerve — **NOT** in this container). The **medullary
    pyramid** is the **direct substrate** of the **contralateral
    hemiparesis** in medial medullary syndrome.

*   **Pseudobulbar palsy (via corticobulbar tract in the
    pyramid):** **Bilateral** corticobulbar lesions — **dysarthria**,
    **dysphagia**, **emotional lability** — from **corticobulbar
    fiber** damage. The **medullary pyramid** carries the
    **corticobulbar fibers** that contribute to the **upper motor
    neuron** component of pseudobulbar palsy.

*   **Amyotrophic lateral sclerosis (via corticospinal
    degeneration):** **Upper motor neuron** degeneration of the
    **corticospinal tract** — including the **medullary
    pyramid** — contributes to **spasticity**, **hyperreflexia**,
    and **Babinski sign** in ALS. The **medullary pyramid** is the
    **medullary segment** of the degenerating **upper motor
    neuron** pathway.

*   **Hereditary spastic paraplegia (via corticospinal
    degeneration):** **Upper motor neuron** degeneration of the
    **corticospinal tract** — including the **medullary
    pyramid** — causes **progressive spasticity** and **gait
    impairment**. The **medullary pyramid** is the **medullary
    segment** of the degenerating pathway.

*   **Primary lateral sclerosis (via corticospinal
    degeneration):** A **pure upper motor neuron** disorder —
    **corticospinal tract** degeneration (including the
    **medullary pyramid**) — causes **progressive spasticity**
    and **weakness**. The **medullary pyramid** is the
    **medullary segment** of the degenerating pathway.

*   **No Named "Medullary Pyramid Syndrome":** The medullary
    pyramid is a **white-matter tract** — its clinical relevance
    is **direct**, via the **upper motor neuron** findings of the
    **broader brainstem lesion** (medial medullary syndrome) or
    the **neurological disorder** (ALS, HSP, PLS), **not** for the
    pyramid itself.

**What is NOT here:** The medullary pyramid is **not** the
substrate for **sensory loss** (medial lemniscus, spinothalamic
tract — **NOT** in this container), **cerebellar ataxia**
(inferior cerebellar peduncle, inferior olivary nucleus — **NOT**
in this container), or **autonomic dysfunction** (RVLM, CVLM,
NTS — **NOT** in this container). Its clinical relevance is the
**upper motor neuron** functions listed above.

Lateralization Notes
--------------------
The medullary pyramid is a **bilateral container** with ``left``
and ``right`` structural children. There is **no**
``medullary_pyramid/left/.../`` structural hierarchy beyond the
single leaf level.

*   **Bilateral structural children:** ``left`` and ``right`` are
    **leaf modules** — each represents the **left** or **right**
    medullary pyramid as a **single structure**. Consumers resolve
    the **left** medullary pyramid via
    ``medullary_pyramid.left`` and the **right** via
    ``medullary_pyramid.right``.

*   **Contralateral motor control (corticospinal):** The
    **pyramidal decussation** at the **spinomedullary junction**
    crosses **~85–90%** of corticospinal fibers, so each
    **medullary pyramid** controls the **contralateral** body.
    This is a **functional** contralaterality — the **pyramid
    itself** is structurally **symmetric**.

*   **Bilateral corticobulbar input (with exceptions):** Most
    **corticobulbar fibers** cross the midline (via the
    **pyramidal decussation** or **above** it) and **innervate
    the contralateral** cranial nerve motor nuclei. **Exceptions**
    include the **genioglossus** motor neuron pool (contralateral
    only) and the **lower facial** motor neuron pool (contralateral
    only) — relevant to **upper motor neuron** facial and tongue
    findings. This is a **corticobulbar** asymmetry, **NOT** a
    **pyramidal** lateralization — the **pyramid itself** is
    **symmetric**.

*   **NO Lateralization Warning:** The medullary pyramid has **no
    known functional lateralization** at the **tract level**.
    Consumers must **not** import a **lateralization warning**
    into the medullary pyramid — the **left** and **right**
    pyramids are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The medullary pyramid
    is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the medullary pyramid.

*   **NO Fear-Output Warning:** The medullary pyramid is **not** a
    fear-output structure — it is a **ventral white-matter motor
    tract**. Consumers must **not** conflate it with the
    **central nucleus** or with the **amygdala**.

**A consumer that assumes "left medullary pyramid = right
medullary pyramid" will be structurally correct** — the two sides
are **symmetric** and **functionally equivalent** at the **tract
level**. The medullary pyramid is a **strict-mirror pair with NO
warning** — **no SLEA warning**, **no fear-output warning**, and
**no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The medullary pyramid is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../olivary_body/``, ``.../arcuate_nucleus/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../solitary_nucleus/``, ``.../ventral_respiratory_group/``,
    ``.../metencephalon/``, ``.../midbrain/``,
    ``.../spinal_cord/``, or any other container. The medullary
    pyramid's relationships to the olivary body, arcuate nucleus,
    RVLM, CVLM, cranial nerve nuclei, medial lemniscus, and the
    spinal corticospinal tract are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children.** The structural
    children are ``left`` and ``right``, each a **leaf**. The
    container itself is **unpaired**.
*   **NOT the whole corticospinal or corticobulbar tract.** The
    medullary pyramid is the **medullary segment** — **NOT** the
    whole pathway.
*   **NOT the pyramidal decussation.** The decussation is the
    **caudal end** of the pyramid, **NOT** a separate module.
*   **NOT the spinal corticospinal tract.** The spinal segment is
    wired under ``.../spinal_cord/white_matter/{left,right}/corticospinal_tract/``.
*   **NOT the internal capsule or cerebral peduncle.** Those are
    **supratentorial / midbrain** segments of the pathway.
*   **NOT the inferior olivary nucleus or the arcuate nucleus.**
    Those are **grey-matter** structures adjacent to the pyramid.
*   **NOT the RVLM or CVLM.** Those are **ventrolateral
    grey-matter autonomic** structures.
*   **NOT the cranial nerve nuclei.** Those are **dorsal /
    ventrolateral grey-matter motor** nuclei. The
    **corticobulbar fibers** pass through the pyramid, but the
    **nuclei** and the **tract** are different structures.
*   **NOT the medial lemniscus.** That is the **dorsal sensory**
    white-matter tract.
*   **No ``AREA_PATHS`` hop.** The medullary pyramid is a **local
    container** — it is not cross-listed under another brainparts
    path.
*   **No nested cross-listing.** The medullary pyramid has no
    nested dual-framing module. It is a **bilateral container**
    with **two leaf children**.
*   **Structural parity with the right side — strict mirror.** The
    ``left`` and ``right`` leaves are **structurally identical**
    — same leaf status, same **white-matter motor tract**
    framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import medullary_pyramid

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid"
    )

**Do not** assume the medullary pyramid is the **whole
corticospinal or corticobulbar tract**. It is the **medullary
segment** — the **supratentorial**, **capsular**, **peduncular**,
**pontine**, and **spinal** segments are **different structures**
in **different containers**.

**Do not** assume the medullary pyramid is the **pyramidal
decussation**. The decussation is the **caudal end** of the
pyramid — **NOT** a separate module.

**Do not** assume the medullary pyramid is the **spinal
corticospinal tract**. The spinal segment is wired under
``.../spinal_cord/white_matter/{left,right}/corticospinal_tract/``.

**Do not** assume the medullary pyramid is the **inferior olivary
nucleus**, the **arcuate nucleus**, the **RVLM**, the **CVLM**,
or the **cranial nerve nuclei**. Those are **grey-matter**
structures — **NOT** the white-matter pyramid.

**Do not** assume the medullary pyramid is the **medial
lemniscus**. The medial lemniscus is a **sensory** white-matter
tract — **NOT** the motor pyramid.

**Do not** look for a single unpaired medullary pyramid. The
**left** and **right** pyramids are **separate leaf modules**
under this container.

Iterating the medullary pyramid's structural children (recommended
consumer pattern)::

    MEDULLARY_PYRAMID_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # medullary pyramid.

Reaching the left and right medullary pyramids (recommended
consumer pattern)::

    # The left and right medullary pyramids are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.left
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.right
    #
    # Each is a leaf module representing the medullary pyramid of
    # that side.

Reaching the spinal corticospinal tract (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The spinal corticospinal tract is a SEPARATE structure in
    # the SPINAL CORD container:
    #
    #   spinal_cord.white_matter.left.corticospinal_tract
    #   spinal_cord.white_matter.right.corticospinal_tract
    #
    # The medullary pyramid is the MEDULLARY segment; the spinal
    # corticospinal tract is the SPINAL segment after the
    # pyramidal decussation.

Reaching the inferior olivary nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The inferior olivary nucleus is a GREY-MATTER cerebellar
    # relay, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body
    #
    # The olivary body is DORSOLATERAL to the pyramid — adjacent
    # but DISTINCT.

Reaching the arcuate nucleus (recommended consumer pattern —
NOTE the DIFFERENT structure)::

    # The arcuate nucleus is a VENTRAL-SURFACE grey-matter
    # chemosensory nucleus, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus
    #
    # The arcuate nucleus is ADJACENT to the pyramid at the
    # ventral medullary surface — but it is grey matter, not
    # white matter.

Reaching the RVLM and CVLM (recommended consumer pattern — NOTE
the DIFFERENT structures)::

    # The RVLM and CVLM are VENTROLATERAL grey-matter autonomic
    # regions, NOT the ventral white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #
    # The pyramid is VENTRAL; the RVLM and CVLM are
    # VENTROLATERAL — different locations, different structures.

Reaching the cranial nerve nuclei (recommended consumer pattern
— NOTE the DIFFERENT structures)::

    # The cranial nerve nuclei are DORSAL / VENTROLATERAL
    # grey-matter motor nuclei, NOT the white-matter pyramid:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei
    #
    # The corticobulbar fibers from the pyramid innervate these
    # nuclei — but the TRACT and the NUCLEI are different
    # structures.

Bilateral iteration (recommended consumer pattern)::

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