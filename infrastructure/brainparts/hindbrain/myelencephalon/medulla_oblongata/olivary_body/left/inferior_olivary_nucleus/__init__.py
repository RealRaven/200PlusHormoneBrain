"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.olivary_body.left.inferior_olivary_nucleus
================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── olivary_body
                └── left
                    └── inferior_olivary_nucleus   <-- THIS MODULE

**Primary synonym:** Left inferior olivary nucleus; left principal
inferior olivary nucleus; left nucleus olivaris inferior; left
oliva; left principal olive.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**grey-matter nucleus** — the **principal (main) nucleus of the
left inferior olivary complex** in the **left ventrolateral
medulla oblongata**. It is the **sole source of climbing fibers**
to the **right cerebellar hemisphere**. It is the **principal**
nucleus — the **accessory olivary nuclei** (left medial accessory
olivary nucleus, left dorsal accessory olivary nucleus) are
**associated subdivisions of the left olivary body**, documented
as **prose at the parent level**, **not** as structural children
of this leaf. It is **NOT** the **left superior olivary complex**
— which is a **pontine auditory** structure.
**Part of:** The **left** container of the **olivary_body**
bilateral container — which is part of the **medulla oblongata**
— the **caudal brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../olivary_body/left/`` → **direct
child** of the left olivary body container. It is the **only**
structural child of the left olivary body container.
**Structural children:** **None.** This is a **leaf** module. The
left inferior olivary nucleus is represented as a **single
structure** — it has **no structural children** of its own. The
**left accessory olivary nuclei** (medial accessory, dorsal
accessory) are **prose subdivisions of the parent**
``.../olivary_body/left/`` — **NOT** structural children of this
leaf.
**Boundary status (NOT the right inferior olivary nucleus — the
contralateral leaf):** **Boundary case — the left inferior
olivary nucleus is NOT the right inferior olivary nucleus.** The
**right inferior olivary nucleus**
(``.../olivary_body/right/inferior_olivary_nucleus/``) is the
**contralateral leaf** — the principal inferior olivary nucleus
of the **right** medulla. **They are DIFFERENT LEAVES** — the
``left`` and ``right`` nuclei are the two sides of the
**bilateral olivary_body** container. Consumers must **not**
conflate the **left** inferior olivary nucleus with the **right**
— resolve the right side via
``olivary_body.right.inferior_olivary_nucleus``.
**Boundary status (NOT the left accessory olivary nuclei — prose
subdivisions of the parent):** **Boundary case — the left
inferior olivary nucleus is NOT the left accessory olivary
nuclei.** The **left accessory olivary nuclei** — the **left
medial accessory olivary nucleus** and the **left dorsal
accessory olivary nucleus** — are **associated subdivisions of
the left olivary body**, **NOT** the principal inferior olivary
nucleus. They are documented as **prose at the parent level**
(``.../olivary_body/left/``), **not** as structural children of
this leaf. Consumers must **not** expect to find the accessory
olivary nuclei under ``inferior_olivary_nucleus`` — resolve them
via the parent container's prose.
**Boundary status (NOT the left superior olivary complex — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the left inferior olivary nucleus is NOT the left superior
olivary complex.** The **left superior olivary complex** (left
superior olive, left medial superior olive, left lateral superior
olive)
(``.../metencephalon/pons/superior_olivary_complex/left/``) is a
**left pontine auditory** structure — part of the **ascending
auditory pathway**. The **left inferior olivary nucleus** (here)
is the **left medullary cerebellar-climbing-fiber** source.
**They share the name "olive" but are DIFFERENT STRUCTURES in
DIFFERENT CONTAINERS.** Consumers must **not** conflate the
**left inferior olivary nucleus** with the **left superior
olivary complex**.
**Boundary status (NOT the left medullary pyramid — the pyramid
is the ADJACENT white-matter tract):** **Boundary case — the
left inferior olivary nucleus is NOT the left medullary pyramid.**
The **left medullary pyramid**
(``.../medullary_pyramid/left/``) is the **left ventral
white-matter** column of the **corticospinal / corticobulbar
tract**. The **left inferior olivary nucleus** (here) is a
**left grey-matter** cerebellar-climbing-fiber source. **They are
DIFFERENT STRUCTURES** — the **pyramid** is **white matter**;
the **inferior olivary nucleus** is **grey matter**. Consumers
must **not** conflate the two.
**Boundary status (NOT the left RVLM / left CVLM —
ventrolateral autonomic grey matter):** **Boundary case — the
left inferior olivary nucleus is NOT the left RVLM or left
CVLM.** The **left RVLM**
(``.../rostral_ventrolateral_medulla/left/``) is the **left
sympathetic premotor** center; the **left CVLM**
(``.../caudal_ventrolateral_medulla/left/``) is the **left
sympathoinhibitory** relay. The **left inferior olivary nucleus**
(here) is a **left cerebellar climbing-fiber** source. **They
are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
two.
**Boundary status (NOT the left arcuate nucleus — a
ventral-surface chemosensory nucleus):** **Boundary case — the
left inferior olivary nucleus is NOT the left arcuate nucleus.**
The **left arcuate nucleus** (``.../arcuate_nucleus/left/``) is
a **left ventral-surface grey-matter** chemosensory and
hypothalamic-projecting nucleus. The **left inferior olivary
nucleus** (here) is a **left cerebellar climbing-fiber** source.
**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.
**Boundary status (NOT the left cranial nerve nuclei — dorsal /
ventrolateral motor nuclei):** **Boundary case — the left
inferior olivary nucleus is NOT the left cranial nerve nuclei.**
The **left cranial nerve nuclei**
(``.../cranial_nerve_nuclei/left/``) are the **left dorsal and
ventrolateral grey-matter motor** nuclei. The **left inferior
olivary nucleus** (here) is a **left cerebellar climbing-fiber**
source. **They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the two.
**Boundary status (NOT the left solitary nucleus — a visceral
afferent relay):** **Boundary case — the left inferior olivary
nucleus is NOT the left solitary nucleus.** The **left solitary
nucleus** (NTS) (``.../solitary_nucleus/left/``) is the **left
visceral afferent relay** — a **sensory** nucleus. The **left
inferior olivary nucleus** (here) is a **left cerebellar
climbing-fiber** source — **NOT** a visceral afferent nucleus.
Consumers must **not** conflate the two.
**Boundary status (NOT the left respiratory centers — a
different grey-matter functional system):** **Boundary case —
the left inferior olivary nucleus is NOT the left respiratory
centers.** The **left respiratory centers**
(``.../respiratory_center/left/`` and
``.../ventral_respiratory_group/left/``) are the **left medullary
respiratory rhythm** and **pattern** generators. The **left
inferior olivary nucleus** (here) is a **left cerebellar
climbing-fiber** source. **They are DIFFERENT STRUCTURES.**
Consumers must **not** conflate the two.
**Boundary status (NOT the left inferior cerebellar peduncle —
the white-matter tract that carries the axons):** **Boundary
case — the left inferior olivary nucleus is NOT the left
inferior cerebellar peduncle.** The **left inferior cerebellar
peduncle** (restiform body + juxtarestiform body) is a **left
white-matter tract** that carries the **left olivocerebellar**
(climbing) fibers and **left spinocerebellar** (dorsal) fibers
to the **right cerebellar hemisphere** (crossing first). The
**left inferior olivary nucleus** (here) is the **left
grey-matter nucleus** of origin of the **climbing fibers** — the
**olivocerebellar axons** **travel through** the left inferior
cerebellar peduncle, but the **nucleus** and the **peduncle** are
**different structures**. Consumers must **not** conflate the
**nucleus** with the **white-matter peduncle**.
**Boundary status (NOT the right cerebellar hemisphere — the
target of the left inferior olivary nucleus):** **Boundary
case — the left inferior olivary nucleus is NOT the right
cerebellar hemisphere.** The **right cerebellar hemisphere**
(``.../metencephalon/cerebellum/hemispheres/right/``) is the
**target** of the **left olivocerebellar projection** —
**different structure** in a **different container**. The **left
inferior olivary nucleus** (here) **projects** to the right
cerebellar hemisphere via climbing fibers, but it is **NOT** the
right cerebellar hemisphere itself. Consumers must **not**
conflate the two.
**Boundary status (NOT the left red nucleus — a midbrain
Guillain-Mollaret triangle node that PROJECTS TO this nucleus):**
**Boundary case — the left inferior olivary nucleus is NOT the
left red nucleus.** The **left red nucleus**
(``.../midbrain/tegmentum/red_nucleus/left/``) is a **left
midbrain** motor structure that **projects to** the left
inferior olivary nucleus via the **left central tegmental
tract**. It is **upstream** of this nucleus in the
**Guillain-Mollaret triangle** (left red nucleus → left inferior
olivary nucleus → right dentate nucleus → left red nucleus).
Consumers must **not** conflate the two — the **red nucleus** is
the **input**; the **inferior olivary nucleus** is the
**intermediate node**.
**Boundary status (NOT the right dentate nucleus — a cerebellar
node that RECEIVES from this nucleus):** **Boundary case — the
left inferior olivary nucleus is NOT the right dentate nucleus.**
The **right dentate nucleus**
(``.../metencephalon/cerebellum/nuclei/dentate_nucleus/right/``)
is a **right cerebellar output** nucleus that **receives**
olivocerebellar (climbing) input from the **left inferior
olivary nucleus** and **projects to** the **left red nucleus**
via the **right superior cerebellar peduncle**. It is
**downstream** of this nucleus in the **Guillain-Mollaret
triangle** (left red nucleus → left inferior olivary nucleus →
right dentate nucleus → left red nucleus). Consumers must **not**
conflate the two — the **inferior olivary nucleus** is the
**intermediate node**; the **dentate nucleus** is the
**cerebellar output**.
**Boundary status (NOT the whole left olivary body — a
component of it):** **Boundary case — the left inferior
olivary nucleus is NOT the whole left olivary body.** The
**left olivary body** (``.../olivary_body/left/``) is the
**container** that **contains** the left inferior olivary
nucleus (here) **plus** the left accessory olivary nuclei
(medial accessory, dorsal accessory). The **left inferior
olivary nucleus** is **one component** — the **principal**
nucleus — of the left olivary body. Consumers must **not**
conflate the **principal nucleus** with the **whole left
olivary body**.
**Boundary status (NOT the whole left medulla oblongata — a
relatively large grey-matter structure within it):** **Boundary
case — the left inferior olivary nucleus is NOT the whole left
medulla oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the left cranial nerve nuclei, left autonomic nuclei,
left respiratory centers, left olivary body (here), left
medullary pyramid, left arcuate nucleus, and other structures.
The **left inferior olivary nucleus** is **one relatively large
grey-matter structure** within the left medulla. Consumers must
**not** conflate the **nucleus** with the **whole medulla**.

Overview
--------
The **left inferior olivary nucleus** (principal inferior olivary
nucleus) is a **grey-matter nucleus** in the **left ventrolateral
medulla oblongata** — the **sole source of climbing fibers** to
the **right cerebellar hemisphere**. It lies **dorsolateral** to
the **left medullary pyramid** and **medial** to the **left
inferior cerebellar peduncle**, and it is the **main component**
of the **left olive** — the **prominent bulge** on the **left
ventrolateral medullary surface**.

**This is a LEAF module.** The **left inferior olivary nucleus**
is represented as a **single structure** — it has **no structural
children**. The **left accessory olivary nuclei** (left medial
accessory, left dorsal accessory) are **prose subdivisions of the
parent** ``.../olivary_body/left/`` — **NOT** structural children
of this leaf.

**The left inferior olivary nucleus is the PRINCIPAL nucleus of
the left olivary body.** The **left accessory olivary nuclei** —
the **left medial accessory olivary nucleus** and the **left
dorsal accessory olivary nucleus** — are **smaller associated
nuclei** within the **left inferior olivary complex**, documented
as **prose at the parent level**. They **also** send climbing
fibers to the **right cerebellar hemisphere**, but to **different
cerebellar zones** than the principal nucleus.

**The left inferior olivary nucleus is the INFERIOR olivary
nucleus, NOT the superior olivary complex.** The **left superior
olivary complex** is a **left pontine auditory** structure — **NOT**
a medullary cerebellar relay. **They share the name "olive" but
are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**

**The left inferior olivary nucleus is a GREY-MATTER structure,
NOT a white-matter tract.** It is the **source of the left
olivocerebellar axons** — the **climbing fibers** that **travel
through** the **left inferior cerebellar peduncle** (crossing
first) to the **right cerebellar hemisphere**. It is **NOT** the
**left inferior cerebellar peduncle** (the white-matter tract
that carries the axons), **NOT** the **left medullary pyramid**
(the adjacent corticospinal tract), and **NOT** the **left
RVLM** / **left CVLM** (the adjacent autonomic nuclei).

**The left inferior olivary nucleus is a CEREBELLAR CLIMBING-FIBER
SOURCE, NOT a motor nucleus and NOT an autonomic nucleus.** It
**does not** send motor axons to muscles and **does not**
regulate autonomic function. It **projects** to the **right
cerebellar hemisphere** via climbing fibers and **participates**
in **cerebellar motor learning** and **timing**.

**The left inferior olivary nucleus is one of the three nodes of
the Guillain–Mollaret triangle.** The triangle is **left red
nucleus → left inferior olivary nucleus → right dentate nucleus
→ left red nucleus**. The **left red nucleus** projects to the
**left inferior olivary nucleus** via the **left central
tegmental tract** (ipsilateral); the **left inferior olivary
nucleus** projects to the **right dentate nucleus** via the
**left inferior cerebellar peduncle** (contralateral); the
**right dentate nucleus** projects back to the **left red
nucleus** via the **right superior cerebellar peduncle**
(contralateral). **Lesions anywhere in this circuit** cause
**left hypertrophic olivary degeneration** and **palatal
tremor**.

The Left Inferior Olivary Nucleus / Right Inferior Olivary Nucleus Boundary
---------------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left inferior olivary nucleus** (this module) — the
    principal inferior olivary nucleus of the **left** medulla.

*   **Right inferior olivary nucleus**
    (``.../olivary_body/right/inferior_olivary_nucleus/``) — the
    principal inferior olivary nucleus of the **right** medulla.

**The two are the SIDES of the bilateral olivary_body container.**
They are **structurally symmetric mirror pairs** — same
cytoarchitecture, same **contralateral** projections, same **no
warning**. Consumers must **not** conflate the left with the
right — resolve the right side via
``olivary_body.right.inferior_olivary_nucleus``.

The Left Inferior Olivary Nucleus / Left Accessory Olivary Nuclei Boundary
--------------------------------------------------------------------------
This is the **principal / accessory** boundary (within the same
olivary body):

*   **Left inferior olivary nucleus** (this module) — the
    **principal** nucleus of the left olivary body.

*   **Left accessory olivary nuclei** — the **left medial
    accessory olivary nucleus** and the **left dorsal accessory
    olivary nucleus** — **prose subdivisions of the parent**
    ``.../olivary_body/left/``.

**The accessory olivary nuclei are NOT structural children of this
leaf.** They are **documented at the parent container level** as
prose. Consumers must **not** expect to find them under
``inferior_olivary_nucleus`` — resolve them via the parent
container.

The Left Inferior Olivary Nucleus / Left Superior Olivary Complex Boundary
--------------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    medullary cerebellar climbing-fiber** source.

*   **Left superior olivary complex**
    (``.../metencephalon/pons/superior_olivary_complex/left/``) —
    the **left pontine auditory** relay.

**They share the name "olive" but are DIFFERENT STRUCTURES in
DIFFERENT CONTAINERS.** Consumers must **not** conflate the
**left inferior olivary nucleus** with the **left superior
olivary complex**.

The Left Inferior Olivary Nucleus / Left Medullary Pyramid Boundary
-------------------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    grey-matter cerebellar climbing-fiber** source.

*   **Left medullary pyramid**
    (``.../medullary_pyramid/left/``) — the **left ventral
    white-matter** corticospinal / corticobulbar tract.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Inferior Olivary Nucleus / Left RVLM and Left CVLM Boundary
--------------------------------------------------------------------
This is the **cerebellar-relay / autonomic** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    cerebellar climbing-fiber** source.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``)
    and **left CVLM**
    (``.../caudal_ventrolateral_medulla/left/``) — the **left
    ventrolateral autonomic** nuclei.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Inferior Olivary Nucleus / Left Arcuate Nucleus Boundary
-----------------------------------------------------------------
This is the **cerebellar-relay / chemosensory** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    cerebellar climbing-fiber** source.

*   **Left arcuate nucleus** (``.../arcuate_nucleus/left/``) — the
    **left ventral-surface chemosensory** nucleus.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Inferior Olivary Nucleus / Left Cranial Nerve Nuclei Boundary
----------------------------------------------------------------------
This is the **cerebellar-relay / motor** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    cerebellar climbing-fiber** source.

*   **Left cranial nerve nuclei**
    (``.../cranial_nerve_nuclei/left/``) — the **left dorsal /
    ventrolateral motor** nuclei.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Inferior Olivary Nucleus / Left Solitary Nucleus Boundary
------------------------------------------------------------------
This is the **cerebellar-relay / visceral-sensory** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    cerebellar climbing-fiber** source.

*   **Left solitary nucleus** (``.../solitary_nucleus/left/``) —
    the **left visceral afferent sensory** relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Inferior Olivary Nucleus / Left Respiratory Centers Boundary
---------------------------------------------------------------------
This is the **cerebellar-relay / respiratory** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    cerebellar climbing-fiber** source.

*   **Left respiratory centers** (``.../respiratory_center/left/``
    and ``.../ventral_respiratory_group/left/``) — the **left
    medullary respiratory rhythm** and **pattern** generators.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Left Inferior Olivary Nucleus / Left Inferior Cerebellar Peduncle Boundary
------------------------------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    grey-matter nucleus** of origin of the **left climbing
    fibers**.

*   **Left inferior cerebellar peduncle** — the **left
    white-matter tract** that carries the **left olivocerebellar**
    (climbing) fibers and **left spinocerebellar** (dorsal)
    fibers to the cerebellum.

**The left olivocerebellar axons travel THROUGH the left inferior
cerebellar peduncle — but the nucleus and the peduncle are
DIFFERENT STRUCTURES.** Consumers must **not** conflate the
**nucleus** with the **white-matter peduncle**.

The Left Inferior Olivary Nucleus / Right Cerebellar Hemisphere Boundary
------------------------------------------------------------------------
This is the **source / target** boundary:

*   **Left inferior olivary nucleus** (this module) — the **left
    climbing fiber** source.

*   **Right cerebellar hemisphere**
    (``.../metencephalon/cerebellum/hemispheres/right/``) — the
    **target** of the left climbing fibers.

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**
Consumers must **not** conflate the **left inferior olivary
nucleus** with the **right cerebellar hemisphere**.

The Left Inferior Olivary Nucleus / Left Red Nucleus Boundary
-------------------------------------------------------------
This is the **Guillain–Mollaret triangle INPUT** boundary:

*   **Left inferior olivary nucleus** (this module) — the
    **intermediate node** of the **Guillain–Mollaret triangle**.

*   **Left red nucleus**
    (``.../midbrain/tegmentum/red_nucleus/left/``) — the **input
    node** of the **Guillain–Mollaret triangle** — projects to
    the left inferior olivary nucleus via the **left central
    tegmental tract** (ipsilateral).

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** The
**left red nucleus** is **upstream** of the **left inferior
olivary nucleus** in the **triangle** (left red nucleus → left
inferior olivary nucleus → right dentate nucleus → left red
nucleus). Consumers must **not** conflate the two.

The Left Inferior Olivary Nucleus / Right Dentate Nucleus Boundary
------------------------------------------------------------------
This is the **Guillain–Mollaret triangle OUTPUT** boundary:

*   **Left inferior olivary nucleus** (this module) — the
    **intermediate node** of the **Guillain–Mollaret triangle**.

*   **Right dentate nucleus**
    (``.../metencephalon/cerebellum/nuclei/dentate_nucleus/right/``)
    — the **cerebellar output node** of the **Guillain–Mollaret
    triangle** — receives olivocerebellar (climbing) input from
    the left inferior olivary nucleus and projects back to the
    **left red nucleus** via the **right superior cerebellar
    peduncle** (contralateral).

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** The
**right dentate nucleus** is **downstream** of the **left
inferior olivary nucleus** in the **triangle**. Consumers must
**not** conflate the two.

Function in the Human Brain
---------------------------
The left inferior olivary nucleus's function is **left
cerebellar climbing-fiber output** — **NOT motor conduction**,
**NOT autonomic regulation**, and **NOT sensory relay**:

*   **Climbing-fiber output to the right cerebellar hemisphere:**
    The **left inferior olivary nucleus** is the **sole source**
    of **climbing fibers** to the **right cerebellar
    hemisphere** — the **left olivocerebellar pathway** projects
    to the **right cerebellar hemisphere** via the **left
    inferior cerebellar peduncle** (after crossing). Each
    **right** Purkinje cell receives **exactly one** climbing
    fiber from the **left** inferior olivary nucleus — a
    **powerful, low-frequency** input that triggers **complex
    spikes** in the Purkinje cell.

*   **Right cerebellar motor learning:** The **left
    climbing-fiber** **error signal** is **critical** for
    **right cerebellar motor learning** — especially **eyeblink
    conditioning**, **vestibulo-ocular reflex adaptation**, and
    **sensorimotor synchronization**. The **climbing fiber**
    drives **long-term depression** (LTD) at the **parallel
    fiber → Purkinje cell** synapse — the **cellular basis** of
    cerebellar motor learning.

*   **Timing and synchrony:** The **left inferior olivary
    nucleus** neurons are **electrically coupled** via **gap
    junctions** — producing **synchronous, rhythmic** climbing-
    fiber activation that contributes to **cerebellar timing**
    and **sensorimotor synchronization**.

*   **NOT motor conduction:** The **left inferior olivary
    nucleus** does **not** send motor axons to muscles — the
    **motor conduction** is the **corticospinal tract** (via the
    **left medullary pyramid**).

*   **NOT autonomic regulation:** The **left inferior olivary
    nucleus** does **not** regulate autonomic function — the
    **autonomic regulation** is the **left RVLM**, **left
    CVLM**, and **left NTS**.

*   **NOT sensory relay:** The **left inferior olivary nucleus**
    does **not** relay **somatic** or **visceral** sensation.

**The unifying theme:** the left inferior olivary nucleus is the
**sole source of climbing fibers** to the **right cerebellar
hemisphere** — the **left climbing fiber** is the **error
signal** for **right cerebellar motor learning** and **timing**,
delivered via the **left olivocerebellar pathway** through the
**left inferior cerebellar peduncle** to the **right cerebellar
hemisphere**.

Associated Disorders
--------------------
The left inferior olivary nucleus is the **substrate** for
**well-defined clinical syndromes** — its clinical relevance is
**direct**, via **climbing-fiber dysfunction** and
**Guillain–Mollaret triangle** lesions:

*   **Left hypertrophic olivary degeneration (HOD — via
    Guillain–Mollaret triangle lesions):** **Transsynaptic
    degeneration** of the **left inferior olivary nucleus**
    after a lesion in the **Guillain–Mollaret triangle**. The
    **responsible lesions** are:
    *   **Left red nucleus lesion** (or **left central tegmental
        tract lesion** — the pathway from the left red nucleus
        to the left inferior olivary nucleus) → **left HOD**.
    *   **Right dentate nucleus lesion** (or **right superior
        cerebellar peduncle lesion** — the pathway from the
        right dentate to the left red nucleus) → **left HOD**.
    **Imaging** shows **T2 hyperintensity** and **enlargement**
    of the left inferior olivary nucleus over **weeks to
    months** — **counterintuitive** because **most**
    degenerations cause **atrophy**, but **HOD** causes
    **hypertrophy** (the **neurons** undergo **swelling** and
    **hypertrophy** of the **neuropil** before eventual
    atrophy).

*   **Palatal tremor / palatal myoclonus (via Guillain–Mollaret
    triangle lesions):** **Rhythmic, involuntary** contraction
    of the **soft palate** — **frequently** accompanies **left
    hypertrophic olivary degeneration** after a
    **Guillain–Mollaret triangle** lesion. The **left inferior
    olivary nucleus** is the **direct substrate** of **palatal
    tremor** — **disinhibition** of the **inferior olive**
    after **triangle** lesions produces **rhythmic**,
    **synchronous** olivary **oscillations** that **drive** the
    **palatal tremor**. Some patients also have **ocular
    myoclonus**, **tremor of the extremities**, or **cerebellar
    ataxia**.

*   **Cerebellar motor-learning deficits (via left climbing-fiber
    dysfunction):** **Impaired eyeblink conditioning**,
    **impaired vestibulo-ocular reflex adaptation**, and
    **impaired sensorimotor timing** on the **right side** —
    from **left climbing-fiber** loss or **left olivary**
    dysfunction.

*   **Brainstem stroke (via olivary involvement):** **Medial
    medullary syndrome** or **lateral medullary syndrome** can
    **involve** the **left inferior olivary nucleus** (or its
    **connections**), causing **cerebellar ataxia**,
    **tremor**, or **palatal tremor**.

*   **Neurodegenerative diseases (via olivary involvement):**
    **Multiple system atrophy (MSA)** can involve the **left
    inferior olivary nucleus** — contributing to **cerebellar
    ataxia** in **MSA-C**. **Spinocerebellar ataxias (SCAs)**
    may involve the **left inferior olivary nucleus**.

*   **No Named "Left Inferior Olivary Nucleus Syndrome":** The
    left inferior olivary nucleus is a **cerebellar relay** —
    its clinical relevance is **direct** via the **left
    hypertrophic olivary degeneration / palatal tremor**
    syndrome (Guillain–Mollaret triangle) and **indirect** via
    **cerebellar** and **brainstem** disorders.

**What is NOT here:** The left inferior olivary nucleus is
**not** the substrate for **motor weakness** (left corticospinal
tract — **NOT** in this container), **sensory loss** (left
medial lemniscus, left spinothalamic tract — **NOT** in this
container), **autonomic dysfunction** (left RVLM, left CVLM,
left NTS — **NOT** in this container), or **respiratory rhythm**
(left VRG, left DRG — **NOT** in this container). Its clinical
relevance is the **left cerebellar motor-learning** and
**Guillain–Mollaret triangle** functions listed above.

Lateralization Notes
--------------------
This is the **left** inferior olivary nucleus module. The
olivary body is a **bilateral container** whose two sides are
**structurally symmetric mirror pairs** — and it carries **NO
warning**:

*   **Bilateral Symmetry:** The **left** and **right** inferior
    olivary nuclei are **structurally symmetric** — they are
    **mirror pairs** with the **same** cytoarchitecture, **same**
    contralateral projections, and **same** functions. The
    **left** nucleus projects to the **right** cerebellar
    hemisphere; the **right** nucleus projects to the **left**
    cerebellar hemisphere.

*   **Contralateral Projection to the Cerebellum:** Each
    **inferior olivary nucleus** projects **contralaterally** to
    its **ipsilateral** cerebellar hemisphere — **left inferior
    olivary nucleus → right cerebellar hemisphere** and **right
    inferior olivary nucleus → left cerebellar hemisphere**.
    This is **functionally** a **contralateral** circuit.

*   **NO Lateralization Warning:** The inferior olivary nucleus
    has **no known functional lateralization** at the **nucleus
    level**. Consumers must **not** import a **lateralization
    warning** into the left inferior olivary nucleus — the
    **left** and **right** nuclei are **functionally
    symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left inferior
    olivary nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the left inferior olivary nucleus.

*   **NO Fear-Output Warning:** The left inferior olivary nucleus
    is **not** a fear-output structure — it is a **left
    cerebellar climbing-fiber** source. Consumers must **not**
    conflate it with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "left inferior olivary nucleus = right
inferior olivary nucleus" will be structurally correct** — the
two sides are **symmetric** and **functionally equivalent** at
the **nucleus level**. The inferior olivary nucleus is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left inferior olivary
    nucleus is a **leaf** — it does **not** import from
    ``.../right/`` or any other right-side module. Bilateral
    relationships are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../metencephalon/pons/superior_olivary_complex/``,
    ``.../medullary_pyramid/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../arcuate_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../solitary_nucleus/``, ``.../respiratory_center/``,
    ``.../ventral_respiratory_group/``,
    ``.../metencephalon/cerebellum/``, ``.../midbrain/``, or
    any other container. The left inferior olivary nucleus's
    relationships to the left superior olivary complex, left
    medullary pyramid, left RVLM, left CVLM, left arcuate
    nucleus, left cranial nerve nuclei, left solitary nucleus,
    left respiratory centers, left inferior cerebellar peduncle,
    right cerebellar hemisphere, left red nucleus, and right
    dentate nucleus are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left inferior
    olivary nucleus is a **single structure** — it has **no
    structural children**. The **left accessory olivary nuclei**
    (medial accessory, dorsal accessory) are **prose
    subdivisions of the parent** ``.../olivary_body/left/`` —
    **NOT** structural children of this leaf.
*   **NOT the right inferior olivary nucleus.** The right
    inferior olivary nucleus is a **separate leaf** under
    ``.../olivary_body/right/inferior_olivary_nucleus/``.
    Consumers must **not** conflate the left with the right.
*   **NOT the left accessory olivary nuclei.** Those are **prose
    subdivisions of the parent** — **NOT** structural children
    of this leaf.
*   **NOT the left superior olivary complex.** The superior
    olivary complex is a **pontine auditory** structure — **NOT**
    a medullary cerebellar relay.
*   **NOT the left medullary pyramid or the left RVLM / left
    CVLM.** Those are **white-matter motor tract** and
    **autonomic nuclei** respectively.
*   **NOT the left arcuate nucleus, left cranial nerve nuclei,
    left solitary nucleus, or left respiratory centers.** Those
    are **chemosensory**, **motor**, **visceral-sensory**, and
    **respiratory** structures respectively.
*   **NOT the left inferior cerebellar peduncle or the right
    cerebellar hemisphere.** The **peduncle** is the
    **white-matter tract** that carries the olivocerebellar
    axons; the **cerebellum** is the **target** of the climbing
    fibers. The **nucleus** is the **grey-matter source** —
    **different structures**.
*   **NOT the left red nucleus or the right dentate nucleus.**
    Those are the **other two nodes** of the Guillain–Mollaret
    triangle — **different structures** in **different
    containers**. The **left red nucleus** is the **input**; the
    **right dentate nucleus** is the **output**.
*   **NOT the whole left olivary body.** The **left olivary
    body** (``.../olivary_body/left/``) is the **container** that
    contains this nucleus **plus** the left accessory olivary
    nuclei. Consumers must **not** conflate the **principal
    nucleus** with the **whole left olivary body**.
*   **No ``AREA_PATHS`` hop.** The left inferior olivary nucleus
    is a **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The left inferior olivary
    nucleus has no nested dual-framing module. It is a **single
    leaf**.
*   **Structural parity with the right inferior olivary nucleus —
    strict mirror with NO warning.** The left and right modules
    are **structurally identical** — same leaf status, same
    **cerebellar climbing-fiber** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.olivary_body.left import inferior_olivary_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "olivary_body.left.inferior_olivary_nucleus"
    )

**Do not** assume the left inferior olivary nucleus is the
**right inferior olivary nucleus**. The right inferior olivary
nucleus is the **separate leaf** at
``.../olivary_body/right/inferior_olivary_nucleus/``.

**Do not** assume the left inferior olivary nucleus is the
**left accessory olivary nuclei**. The accessory nuclei are
**prose subdivisions of the parent** ``.../olivary_body/left/``
— **NOT** structural children of this leaf.

**Do not** assume the left inferior olivary nucleus is the
**left superior olivary complex**. The superior olivary complex
is a **pontine auditory** structure — **NOT** a medullary
cerebellar relay.

**Do not** assume the left inferior olivary nucleus is the
**left medullary pyramid**, the **left RVLM**, or the **left
CVLM**. Those are **white-matter motor tract** and **autonomic
nuclei** respectively.

**Do not** assume the left inferior olivary nucleus is the
**left inferior cerebellar peduncle** or the **right cerebellar
hemisphere**. The **peduncle** is the **white-matter tract**
that carries the olivocerebellar axons; the **cerebellum** is
the **target** of the climbing fibers.

**Do not** assume the left inferior olivary nucleus has
**structural children**. It is a **leaf** — it represents the
left inferior olivary nucleus as a **single structure**.

Iterating the left inferior olivary nucleus's (empty) children
(recommended consumer pattern)::

    LEFT_INFERIOR_OLIVARY_NUCLEUS_CHILDREN = ()
    # The left inferior olivary nucleus is a leaf. It has no
    # structural children.

Reaching the right inferior olivary nucleus (recommended consumer
pattern — the contralateral leaf)::

    # The right inferior olivary nucleus is the CONTRALATERAL
    # leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.right.inferior_olivary_nucleus
    #
    # The left and right inferior olivary nuclei are structurally
    # symmetric mirror pairs with contralateral projections to
    # their respective cerebellar hemispheres.

Reaching the left accessory olivary nuclei (recommended consumer
pattern — NOTE they are prose subdivisions of the parent)::

    # The left accessory olivary nuclei are PROSE SUBDIVISIONS of
    # the parent left olivary body container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.left
    #
    # They are NOT structural children of the left inferior
    # olivary nucleus — they are documented as prose at the parent
    # level.

Reaching the left superior olivary complex (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The left superior olivary complex is a PONTINE AUDITORY
    # structure, NOT a medullary cerebellar relay:
    #
    #   hindbrain.metencephalon.pons.superior_olivary_complex.left
    #
    # The superior olivary complex is part of the ascending
    # auditory pathway — DIFFERENT from the left inferior olivary
    # nucleus.

Reaching the Guillain-Mollaret triangle input (recommended
consumer pattern — NOTE the DIFFERENT structure)::

    # The LEFT RED NUCLEUS is the INPUT to the left inferior
    # olivary nucleus via the LEFT CENTRAL TEGMENTAL TRACT:
    #
    #   hindbrain.midbrain.tegmentum.red_nucleus.left
    #
    # Triangle: LEFT red nucleus -> LEFT inferior olivary
    # nucleus -> RIGHT dentate nucleus -> LEFT red nucleus.
    # Lesions in the LEFT red nucleus or the LEFT central
    # tegmental tract cause LEFT hypertrophic olivary
    # degeneration.

Reaching the Guillain-Mollaret triangle output (recommended
consumer pattern — NOTE the DIFFERENT structure)::

    # The RIGHT DENTATE NUCLEUS RECEIVES climbing fibers from
    # the left inferior olivary nucleus and projects back to the
    # LEFT red nucleus via the RIGHT SUPERIOR CEREBELLAR
    # PEDUNCLE:
    #
    #   hindbrain.metencephalon.cerebellum.nuclei.dentate_nucleus.right
    #
    # Lesions in the RIGHT dentate nucleus or the RIGHT superior
    # cerebellar peduncle cause LEFT hypertrophic olivary
    # degeneration.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"olivary_body.{side}.inferior_olivary_nucleus"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Inferior olivary complex; principal inferior olivary
    nucleus; accessory olivary nuclei; olivocerebellar pathway;
    climbing fibers; Guillain–Mollaret triangle.)
*   **Inferior olive — microcircuitry and function:** De Zeeuw,
    C.I., et al. (1998). "Microcircuitry and function of the
    inferior olive." *Trends in Neurosciences* 21:391–400.
    (Inferior olivary complex; principal nucleus vs. accessory
    nuclei; gap junctions; climbing fibers; complex spikes;
    olivocerebellar pathway.)
*   **Climbing fibers and cerebellar motor learning:** Ito, M.
    (2001). "Cerebellar long-term depression: characterization,
    signal transduction, and functional roles."
    *Physiological Reviews* 81:1143–1195. (Climbing fiber as
    error signal; long-term depression at parallel fiber →
    Purkinje cell synapse; cerebellar motor learning.)
*   **Eyeblink conditioning and inferior olive:** Thompson,
    R.F., Krupa, D.J. (1994). "Organization of memory traces in
    the mammalian brain." *Annual Review of Neuroscience*
    17:519–549. (Eyeblink conditioning; inferior olive; climbing
    fibers.)
*   **Vestibulo-ocular reflex adaptation and inferior olive:**
    Ito, M. (1982). "Cerebellar control of the vestibulo-ocular
    reflex — around the flocculus hypothesis." *Annual Review of
    Neuroscience* 5:275–296. (VOR adaptation; inferior olive;
    climbing fibers.)
*   **Olivocerebellar projection:** Sugihara, I., et al. (2001).
    "The entire trajectories of single olivocerebellar axons in
    the cerebellar cortex and their contribution to cerebellar
    compartmentalization." *Journal of Neuroscience*
    21:7715–7723. (Olivocerebellar axons; climbing fibers;
    contralateral projection.)
*   **Guillain–Mollaret triangle:** Guillain, G., Mollaret, P.
    (1931). "Deux cas de myoclonies synchrones et rythmées
    vélo-pharyngo-laryngo-oculo-diaphragmatiques." *Revue
    Neurologique* 2:545–566. (Guillain–Mollaret triangle;
    ipsilateral red nucleus → inferior olive → contralateral
    dentate nucleus → ipsilateral red nucleus; palatal tremor.)
*   **Hypertrophic olivary degeneration:** Goto, N., Kaneko, M.
    (1981). "Olivary enlargement: chronological and
    morphometric studies." *Acta Neuropathologica* 54:275–282.
    (Hypertrophic olivary degeneration; transsynaptic
    degeneration; Guillain–Mollaret triangle lesions;
    ipsilateral red nucleus / central tegmental tract lesion or
    contralateral dentate nucleus / superior cerebellar peduncle
    lesion.)
*   **Palatal tremor:** Deuschl, G., et al. (1990). "Symptomatic
    and essential palatal tremor: clinical and
    polysomnographic differences." *Brain* 113:1645–1660.
    (Palatal tremor; essential vs. symptomatic; Guillain–
    Mollaret triangle; hypertrophic olivary degeneration.)
*   **Olivary hypertrophy imaging:** Kitajima, M., et al. (2018).
    "Hypertrophic olivary degeneration: a comprehensive review."
    *Japanese Journal of Radiology* 36:151–160. (HOD imaging
    findings; T2 hyperintensity; olivary enlargement; Guillain–
    Mollaret triangle.)
*   **Multiple system atrophy and inferior olive:** Wenning,
    G.K., et al. (2004). "Multiple system atrophy." *The Lancet
    Neurology* 3:93–103. (MSA; inferior olivary complex
    involvement; cerebellar ataxia in MSA-C.)
*   **Spinocerebellar ataxias and inferior olive:** Koeppen,
    A.H. (2005). "The pathogenesis of spinocerebellar ataxia."
    *Cerebellum* 4:62–73. (SCAs; inferior olivary complex
    involvement; cerebellar ataxia.)
*   **Superior olivary complex (contrast — pontine auditory):**
    Grothe, B., et al. (2010). "Mechanisms of sound localization
    in mammals." *Physiological Reviews* 90:983–1012. (Superior
    olivary complex; medial superior olive; lateral superior
    olive — DIFFERENT from the inferior olivary nucleus.)
*   NeuroNames — Inferior olivary nucleus (principal); FMA —
    Inferior olivary nucleus (principal olive).
"""