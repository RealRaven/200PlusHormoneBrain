"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.olivary_body.right.inferior_olivary_nucleus
=================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── olivary_body
                └── right
                    └── inferior_olivary_nucleus   <-- THIS MODULE

**Primary synonym:** Right inferior olivary nucleus; right principal
inferior olivary nucleus; right nucleus olivaris inferior; right
oliva; right principal olive.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**grey-matter nucleus** — the **principal (main) nucleus of the
right inferior olivary complex** in the **right ventrolateral
medulla oblongata**. It is the **sole source of climbing fibers**
to the **left cerebellar hemisphere**. It is the **principal**
nucleus — the **accessory olivary nuclei** (right medial accessory
olivary nucleus, right dorsal accessory olivary nucleus) are
**associated subdivisions of the right olivary body**, documented
as **prose at the parent level**, **not** as structural children
of this leaf. It is **NOT** the **right superior olivary complex**
— which is a **pontine auditory** structure.
**Part of:** The **right** container of the **olivary_body**
bilateral container — which is part of the **medulla oblongata**
— the **caudal brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../olivary_body/right/`` → **direct
child** of the right olivary body container. It is the **only**
structural child of the right olivary body container.
**Structural children:** **None.** This is a **leaf** module. The
right inferior olivary nucleus is represented as a **single
structure** — it has **no structural children** of its own. The
**right accessory olivary nuclei** (medial accessory, dorsal
accessory) are **prose subdivisions of the parent**
``.../olivary_body/right/`` — **NOT** structural children of this
leaf.
**Boundary status (NOT the left inferior olivary nucleus — the
contralateral leaf):** **Boundary case — the right inferior
olivary nucleus is NOT the left inferior olivary nucleus.** The
**left inferior olivary nucleus**
(``.../olivary_body/left/inferior_olivary_nucleus/``) is the
**contralateral leaf** — the principal inferior olivary nucleus
of the **left** medulla. **They are DIFFERENT LEAVES** — the
``left`` and ``right`` nuclei are the two sides of the
**bilateral olivary_body** container. Consumers must **not**
conflate the **right** inferior olivary nucleus with the **left**
— resolve the left side via
``olivary_body.left.inferior_olivary_nucleus``.
**Boundary status (NOT the right accessory olivary nuclei —
prose subdivisions of the parent):** **Boundary case — the right
inferior olivary nucleus is NOT the right accessory olivary
nuclei.** The **right accessory olivary nuclei** — the **right
medial accessory olivary nucleus** and the **right dorsal
accessory olivary nucleus** — are **associated subdivisions of
the right olivary body**, **NOT** the principal inferior olivary
nucleus. They are documented as **prose at the parent level**
(``.../olivary_body/right/``), **not** as structural children of
this leaf. Consumers must **not** expect to find the accessory
olivary nuclei under ``inferior_olivary_nucleus`` — resolve them
via the parent container's prose.
**Boundary status (NOT the right superior olivary complex — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the right inferior olivary nucleus is NOT the right superior
olivary complex.** The **right superior olivary complex** (right
superior olive, right medial superior olive, right lateral
superior olive)
(``.../metencephalon/pons/superior_olivary_complex/right/``) is
a **right pontine auditory** structure — part of the **ascending
auditory pathway**. The **right inferior olivary nucleus** (here)
is the **right medullary cerebellar-climbing-fiber** source.
**They share the name "olive" but are DIFFERENT STRUCTURES in
DIFFERENT CONTAINERS.** Consumers must **not** conflate the
**right inferior olivary nucleus** with the **right superior
olivary complex**.
**Boundary status (NOT the right medullary pyramid — the pyramid
is the ADJACENT white-matter tract):** **Boundary case — the
right inferior olivary nucleus is NOT the right medullary
pyramid.** The **right medullary pyramid**
(``.../medullary_pyramid/right/``) is the **right ventral
white-matter** column of the **corticospinal / corticobulbar
tract**. The **right inferior olivary nucleus** (here) is a
**right grey-matter** cerebellar-climbing-fiber source. **They
are DIFFERENT STRUCTURES** — the **pyramid** is **white
matter**; the **inferior olivary nucleus** is **grey matter**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right RVLM / right CVLM —
ventrolateral autonomic grey matter):** **Boundary case — the
right inferior olivary nucleus is NOT the right RVLM or right
CVLM.** The **right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) is the **right
sympathetic premotor** center; the **right CVLM**
(``.../caudal_ventrolateral_medulla/right/``) is the **right
sympathoinhibitory** relay. The **right inferior olivary
nucleus** (here) is a **right cerebellar climbing-fiber**
source. **They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the two.
**Boundary status (NOT the right arcuate nucleus — a
ventral-surface chemosensory nucleus):** **Boundary case — the
right inferior olivary nucleus is NOT the right arcuate
nucleus.** The **right arcuate nucleus**
(``.../arcuate_nucleus/right/``) is a **right ventral-surface
grey-matter** chemosensory and hypothalamic-projecting nucleus.
The **right inferior olivary nucleus** (here) is a **right
cerebellar climbing-fiber** source. **They are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the two.
**Boundary status (NOT the right cranial nerve nuclei — dorsal /
ventrolateral motor nuclei):** **Boundary case — the right
inferior olivary nucleus is NOT the right cranial nerve nuclei.**
The **right cranial nerve nuclei**
(``.../cranial_nerve_nuclei/right/``) are the **right dorsal and
ventrolateral grey-matter motor** nuclei. The **right inferior
olivary nucleus** (here) is a **right cerebellar climbing-fiber**
source. **They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the two.
**Boundary status (NOT the right solitary nucleus — a visceral
afferent relay):** **Boundary case — the right inferior olivary
nucleus is NOT the right solitary nucleus.** The **right solitary
nucleus** (NTS) (``.../solitary_nucleus/right/``) is the **right
visceral afferent relay** — a **sensory** nucleus. The **right
inferior olivary nucleus** (here) is a **right cerebellar
climbing-fiber** source — **NOT** a visceral afferent nucleus.
Consumers must **not** conflate the two.
**Boundary status (NOT the right respiratory centers — a
different grey-matter functional system):** **Boundary case —
the right inferior olivary nucleus is NOT the right respiratory
centers.** The **right respiratory centers**
(``.../respiratory_center/right/`` and
``.../ventral_respiratory_group/right/``) are the **right
medullary respiratory rhythm** and **pattern** generators. The
**right inferior olivary nucleus** (here) is a **right cerebellar
climbing-fiber** source. **They are DIFFERENT STRUCTURES.**
Consumers must **not** conflate the two.
**Boundary status (NOT the right inferior cerebellar peduncle —
the white-matter tract that carries the axons):** **Boundary
case — the right inferior olivary nucleus is NOT the right
inferior cerebellar peduncle.** The **right inferior cerebellar
peduncle** (restiform body + juxtarestiform body) is a **right
white-matter tract** that carries the **right olivocerebellar**
(climbing) fibers and **right spinocerebellar** (dorsal) fibers
to the **left cerebellar hemisphere** (crossing first). The
**right inferior olivary nucleus** (here) is the **right
grey-matter nucleus** of origin of the **climbing fibers** — the
**olivocerebellar axons** **travel through** the right inferior
cerebellar peduncle, but the **nucleus** and the **peduncle** are
**different structures**. Consumers must **not** conflate the
**nucleus** with the **white-matter peduncle**.
**Boundary status (NOT the left cerebellar hemisphere — the
target of the right inferior olivary nucleus):** **Boundary
case — the right inferior olivary nucleus is NOT the left
cerebellar hemisphere.** The **left cerebellar hemisphere**
(``.../metencephalon/cerebellum/hemispheres/left/``) is the
**target** of the **right olivocerebellar projection** —
**different structure** in a **different container**. The
**right inferior olivary nucleus** (here) **projects** to the
left cerebellar hemisphere via climbing fibers, but it is **NOT**
the left cerebellar hemisphere itself. Consumers must **not**
conflate the two.
**Boundary status (NOT the right red nucleus — a midbrain
Guillain–Mollaret triangle node that PROJECTS TO this nucleus):**
**Boundary case — the right inferior olivary nucleus is NOT the
right red nucleus.** The **right red nucleus**
(``.../midbrain/tegmentum/red_nucleus/right/``) is a **right
midbrain** motor structure that **projects to** the right
inferior olivary nucleus via the **right central tegmental
tract**. It is **upstream** of this nucleus in the
**Guillain–Mollaret triangle** (right red nucleus → right
inferior olivary nucleus → left dentate nucleus → right red
nucleus). Consumers must **not** conflate the two — the **red
nucleus** is the **input**; the **inferior olivary nucleus** is
the **intermediate node**.
**Boundary status (NOT the left dentate nucleus — a cerebellar
node that RECEIVES from this nucleus):** **Boundary case — the
right inferior olivary nucleus is NOT the left dentate nucleus.**
The **left dentate nucleus**
(``.../metencephalon/cerebellum/nuclei/dentate_nucleus/left/``)
is a **left cerebellar output** nucleus that **receives**
olivocerebellar (climbing) input from the **right inferior
olivary nucleus** and **projects to** the **right red nucleus**
via the **left superior cerebellar peduncle**. It is
**downstream** of this nucleus in the **Guillain–Mollaret
triangle** (right red nucleus → right inferior olivary nucleus →
left dentate nucleus → right red nucleus). Consumers must **not**
conflate the two — the **inferior olivary nucleus** is the
**intermediate node**; the **dentate nucleus** is the
**cerebellar output**.
**Boundary status (NOT the whole right olivary body — a
component of it):** **Boundary case — the right inferior
olivary nucleus is NOT the whole right olivary body.** The
**right olivary body** (``.../olivary_body/right/``) is the
**container** that **contains** the right inferior olivary
nucleus (here) **plus** the right accessory olivary nuclei
(medial accessory, dorsal accessory). The **right inferior
olivary nucleus** is **one component** — the **principal**
nucleus — of the right olivary body. Consumers must **not**
conflate the **principal nucleus** with the **whole right
olivary body**.
**Boundary status (NOT the whole right medulla oblongata — a
relatively large grey-matter structure within it):** **Boundary
case — the right inferior olivary nucleus is NOT the whole right
medulla oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the right cranial nerve nuclei, right autonomic nuclei,
right respiratory centers, right olivary body (here), right
medullary pyramid, right arcuate nucleus, and other structures.
The **right inferior olivary nucleus** is **one relatively
large grey-matter structure** within the right medulla.
Consumers must **not** conflate the **nucleus** with the **whole
medulla**.

Overview
--------
The **right inferior olivary nucleus** (principal inferior
olivary nucleus) is a **grey-matter nucleus** in the **right
ventrolateral medulla oblongata** — the **sole source of
climbing fibers** to the **left cerebellar hemisphere**. It lies
**dorsolateral** to the **right medullary pyramid** and **medial**
to the **right inferior cerebellar peduncle**, and it is the
**main component** of the **right olive** — the **prominent
bulge** on the **right ventrolateral medullary surface**.

**This is a LEAF module.** The **right inferior olivary nucleus**
is represented as a **single structure** — it has **no
structural children**. The **right accessory olivary nuclei**
(right medial accessory, right dorsal accessory) are **prose
subdivisions of the parent** ``.../olivary_body/right/`` —
**NOT** structural children of this leaf.

**The right inferior olivary nucleus is the PRINCIPAL nucleus of
the right olivary body.** The **right accessory olivary nuclei**
— the **right medial accessory olivary nucleus** and the **right
dorsal accessory olivary nucleus** — are **smaller associated
nuclei** within the **right inferior olivary complex**,
documented as **prose at the parent level**. They **also** send
climbing fibers to the **left cerebellar hemisphere**, but to
**different cerebellar zones** than the principal nucleus.

**The right inferior olivary nucleus is the INFERIOR olivary
nucleus, NOT the superior olivary complex.** The **right superior
olivary complex** is a **right pontine auditory** structure —
**NOT** a medullary cerebellar relay. **They share the name
"olive" but are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**

**The right inferior olivary nucleus is a GREY-MATTER structure,
NOT a white-matter tract.** It is the **source of the right
olivocerebellar axons** — the **climbing fibers** that **travel
through** the **right inferior cerebellar peduncle** (crossing
first) to the **left cerebellar hemisphere**. It is **NOT** the
**right inferior cerebellar peduncle** (the white-matter tract
that carries the axons), **NOT** the **right medullary pyramid**
(the adjacent corticospinal tract), and **NOT** the **right
RVLM** / **right CVLM** (the adjacent autonomic nuclei).

**The right inferior olivary nucleus is a CEREBELLAR
CLIMBING-FIBER SOURCE, NOT a motor nucleus and NOT an autonomic
nucleus.** It **does not** send motor axons to muscles and
**does not** regulate autonomic function. It **projects** to the
**left cerebellar hemisphere** via climbing fibers and
**participates** in **cerebellar motor learning** and
**timing**.

**The right inferior olivary nucleus is one of the three nodes of
the Guillain–Mollaret triangle.** The triangle is **right red
nucleus → right inferior olivary nucleus → left dentate nucleus
→ right red nucleus**. The **right red nucleus** projects to the
**right inferior olivary nucleus** via the **right central
tegmental tract** (ipsilateral); the **right inferior olivary
nucleus** projects to the **left dentate nucleus** via the
**right inferior cerebellar peduncle** (contralateral); the
**left dentate nucleus** projects back to the **right red
nucleus** via the **left superior cerebellar peduncle**
(contralateral). **Lesions anywhere in this circuit** cause
**right hypertrophic olivary degeneration** and **palatal
tremor**.

The Right Inferior Olivary Nucleus / Left Inferior Olivary Nucleus Boundary
---------------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    principal inferior olivary nucleus of the **right** medulla.

*   **Left inferior olivary nucleus**
    (``.../olivary_body/left/inferior_olivary_nucleus/``) — the
    principal inferior olivary nucleus of the **left** medulla.

**The two are the SIDES of the bilateral olivary_body container.**
They are **structurally symmetric mirror pairs** — same
cytoarchitecture, same **contralateral** projections, same **no
warning**. Consumers must **not** conflate the right with the
left — resolve the left side via
``olivary_body.left.inferior_olivary_nucleus``.

The Right Inferior Olivary Nucleus / Right Accessory Olivary Nuclei Boundary
---------------------------------------------------------------------------
This is the **principal / accessory** boundary (within the same
olivary body):

*   **Right inferior olivary nucleus** (this module) — the
    **principal** nucleus of the right olivary body.

*   **Right accessory olivary nuclei** — the **right medial
    accessory olivary nucleus** and the **right dorsal accessory
    olivary nucleus** — **prose subdivisions of the parent**
    ``.../olivary_body/right/``.

**The accessory olivary nuclei are NOT structural children of this
leaf.** They are **documented at the parent container level** as
prose. Consumers must **not** expect to find them under
``inferior_olivary_nucleus`` — resolve them via the parent
container.

The Right Inferior Olivary Nucleus / Right Superior Olivary Complex Boundary
---------------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right medullary cerebellar climbing-fiber** source.

*   **Right superior olivary complex**
    (``.../metencephalon/pons/superior_olivary_complex/right/``)
    — the **right pontine auditory** relay.

**They share the name "olive" but are DIFFERENT STRUCTURES in
DIFFERENT CONTAINERS.** Consumers must **not** conflate the
**right inferior olivary nucleus** with the **right superior
olivary complex**.

The Right Inferior Olivary Nucleus / Right Medullary Pyramid Boundary
---------------------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right grey-matter cerebellar climbing-fiber** source.

*   **Right medullary pyramid**
    (``.../medullary_pyramid/right/``) — the **right ventral
    white-matter** corticospinal / corticobulbar tract.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Inferior Olivary Nucleus / Right RVLM and Right CVLM Boundary
-----------------------------------------------------------------------
This is the **cerebellar-relay / autonomic** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right cerebellar climbing-fiber** source.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``)
    and **right CVLM**
    (``.../caudal_ventrolateral_medulla/right/``) — the **right
    ventrolateral autonomic** nuclei.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Inferior Olivary Nucleus / Right Arcuate Nucleus Boundary
-------------------------------------------------------------------
This is the **cerebellar-relay / chemosensory** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right cerebellar climbing-fiber** source.

*   **Right arcuate nucleus** (``.../arcuate_nucleus/right/``) —
    the **right ventral-surface chemosensory** nucleus.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Inferior Olivary Nucleus / Right Cranial Nerve Nuclei Boundary
------------------------------------------------------------------------
This is the **cerebellar-relay / motor** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right cerebellar climbing-fiber** source.

*   **Right cranial nerve nuclei**
    (``.../cranial_nerve_nuclei/right/``) — the **right dorsal /
    ventrolateral motor** nuclei.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Inferior Olivary Nucleus / Right Solitary Nucleus Boundary
--------------------------------------------------------------------
This is the **cerebellar-relay / visceral-sensory** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right cerebellar climbing-fiber** source.

*   **Right solitary nucleus** (``.../solitary_nucleus/right/``) —
    the **right visceral afferent sensory** relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Inferior Olivary Nucleus / Right Respiratory Centers Boundary
-----------------------------------------------------------------------
This is the **cerebellar-relay / respiratory** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right cerebellar climbing-fiber** source.

*   **Right respiratory centers**
    (``.../respiratory_center/right/`` and
    ``.../ventral_respiratory_group/right/``) — the **right
    medullary respiratory rhythm** and **pattern** generators.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Right Inferior Olivary Nucleus / Right Inferior Cerebellar Peduncle Boundary
--------------------------------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right grey-matter nucleus** of origin of the **right
    climbing fibers**.

*   **Right inferior cerebellar peduncle** — the **right
    white-matter tract** that carries the **right
    olivocerebellar** (climbing) fibers and **right
    spinocerebellar** (dorsal) fibers to the cerebellum.

**The right olivocerebellar axons travel THROUGH the right
inferior cerebellar peduncle — but the nucleus and the peduncle
are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
**nucleus** with the **white-matter peduncle**.

The Right Inferior Olivary Nucleus / Left Cerebellar Hemisphere Boundary
------------------------------------------------------------------------
This is the **source / target** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **right climbing fiber** source.

*   **Left cerebellar hemisphere**
    (``.../metencephalon/cerebellum/hemispheres/left/``) — the
    **target** of the right climbing fibers.

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**
Consumers must **not** conflate the **right inferior olivary
nucleus** with the **left cerebellar hemisphere**.

The Right Inferior Olivary Nucleus / Right Red Nucleus Boundary
---------------------------------------------------------------
This is the **Guillain–Mollaret triangle INPUT** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **intermediate node** of the **Guillain–Mollaret triangle**.

*   **Right red nucleus**
    (``.../midbrain/tegmentum/red_nucleus/right/``) — the
    **input node** of the **Guillain–Mollaret triangle** —
    projects to the right inferior olivary nucleus via the
    **right central tegmental tract** (ipsilateral).

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** The
**right red nucleus** is **upstream** of the **right inferior
olivary nucleus** in the **triangle** (right red nucleus → right
inferior olivary nucleus → left dentate nucleus → right red
nucleus). Consumers must **not** conflate the two.

The Right Inferior Olivary Nucleus / Left Dentate Nucleus Boundary
------------------------------------------------------------------
This is the **Guillain–Mollaret triangle OUTPUT** boundary:

*   **Right inferior olivary nucleus** (this module) — the
    **intermediate node** of the **Guillain–Mollaret triangle**.

*   **Left dentate nucleus**
    (``.../metencephalon/cerebellum/nuclei/dentate_nucleus/left/``)
    — the **cerebellar output node** of the **Guillain–Mollaret
    triangle** — receives olivocerebellar (climbing) input from
    the right inferior olivary nucleus and projects back to the
    **right red nucleus** via the **left superior cerebellar
    peduncle** (contralateral).

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** The
**left dentate nucleus** is **downstream** of the **right
inferior olivary nucleus** in the **triangle**. Consumers must
**not** conflate the two.

Function in the Human Brain
---------------------------
The right inferior olivary nucleus's function is **right
cerebellar climbing-fiber output** — **NOT motor conduction**,
**NOT autonomic regulation**, and **NOT sensory relay**:

*   **Climbing-fiber output to the left cerebellar hemisphere:**
    The **right inferior olivary nucleus** is the **sole source**
    of **climbing fibers** to the **left cerebellar hemisphere**
    — the **right olivocerebellar pathway** projects to the
    **left cerebellar hemisphere** via the **right inferior
    cerebellar peduncle** (after crossing). Each **left**
    Purkinje cell receives **exactly one** climbing fiber from
    the **right** inferior olivary nucleus — a **powerful,
    low-frequency** input that triggers **complex spikes** in
    the Purkinje cell.

*   **Left cerebellar motor learning:** The **right
    climbing-fiber** **error signal** is **critical** for
    **left cerebellar motor learning** — especially **eyeblink
    conditioning**, **vestibulo-ocular reflex adaptation**, and
    **sensorimotor synchronization**. The **climbing fiber**
    drives **long-term depression** (LTD) at the **parallel
    fiber → Purkinje cell** synapse — the **cellular basis** of
    cerebellar motor learning.

*   **Timing and synchrony:** The **right inferior olivary
    nucleus** neurons are **electrically coupled** via **gap
    junctions** — producing **synchronous, rhythmic** climbing-
    fiber activation that contributes to **cerebellar timing**
    and **sensorimotor synchronization**.

*   **NOT motor conduction:** The **right inferior olivary
    nucleus** does **not** send motor axons to muscles — the
    **motor conduction** is the **corticospinal tract** (via the
    **right medullary pyramid**).

*   **NOT autonomic regulation:** The **right inferior olivary
    nucleus** does **not** regulate autonomic function — the
    **autonomic regulation** is the **right RVLM**, **right
    CVLM**, and **right NTS**.

*   **NOT sensory relay:** The **right inferior olivary nucleus**
    does **not** relay **somatic** or **visceral** sensation.

**The unifying theme:** the right inferior olivary nucleus is the
**sole source of climbing fibers** to the **left cerebellar
hemisphere** — the **right climbing fiber** is the **error
signal** for **left cerebellar motor learning** and **timing**,
delivered via the **right olivocerebellar pathway** through the
**right inferior cerebellar peduncle** to the **left cerebellar
hemisphere**.

Associated Disorders
--------------------
The right inferior olivary nucleus is the **substrate** for
**well-defined clinical syndromes** — its clinical relevance is
**direct**, via **climbing-fiber dysfunction** and
**Guillain–Mollaret triangle** lesions:

*   **Right hypertrophic olivary degeneration (HOD — via
    Guillain–Mollaret triangle lesions):** **Transsynaptic
    degeneration** of the **right inferior olivary nucleus**
    after a lesion in the **Guillain–Mollaret triangle**. The
    **responsible lesions** are:
    *   **Right red nucleus lesion** (or **right central
        tegmental tract lesion** — the pathway from the right
        red nucleus to the right inferior olivary nucleus) →
        **right HOD**.
    *   **Left dentate nucleus lesion** (or **left superior
        cerebellar peduncle lesion** — the pathway from the
        left dentate to the right red nucleus) → **right HOD**.
    **Imaging** shows **T2 hyperintensity** and **enlargement**
    of the right inferior olivary nucleus over **weeks to
    months** — **counterintuitive** because **most**
    degenerations cause **atrophy**, but **HOD** causes
    **hypertrophy** (the **neurons** undergo **swelling** and
    **hypertrophy** of the **neuropil** before eventual
    atrophy).

*   **Palatal tremor / palatal myoclonus (via Guillain–Mollaret
    triangle lesions):** **Rhythmic, involuntary** contraction
    of the **soft palate** — **frequently** accompanies **right
    hypertrophic olivary degeneration** after a
    **Guillain–Mollaret triangle** lesion. The **right inferior
    olivary nucleus** is the **direct substrate** of **palatal
    tremor** — **disinhibition** of the **inferior olive**
    after **triangle** lesions produces **rhythmic**,
    **synchronous** olivary **oscillations** that **drive** the
    **palatal tremor**. Some patients also have **ocular
    myoclonus**, **tremor of the extremities**, or **cerebellar
    ataxia**.

*   **Cerebellar motor-learning deficits (via right
    climbing-fiber dysfunction):** **Impaired eyeblink
    conditioning**, **impaired vestibulo-ocular reflex
    adaptation**, and **impaired sensorimotor timing** on the
    **left side** — from **right climbing-fiber** loss or
    **right olivary** dysfunction.

*   **Brainstem stroke (via olivary involvement):** **Medial
    medullary syndrome** or **lateral medullary syndrome** can
    **involve** the **right inferior olivary nucleus** (or its
    **connections**), causing **cerebellar ataxia**,
    **tremor**, or **palatal tremor**.

*   **Neurodegenerative diseases (via olivary involvement):**
    **Multiple system atrophy (MSA)** can involve the **right
    inferior olivary nucleus** — contributing to **cerebellar
    ataxia** in **MSA-C**. **Spinocerebellar ataxias (SCAs)**
    may involve the **right inferior olivary nucleus**.

*   **No Named "Right Inferior Olivary Nucleus Syndrome":** The
    right inferior olivary nucleus is a **cerebellar relay** —
    its clinical relevance is **direct** via the **right
    hypertrophic olivary degeneration / palatal tremor**
    syndrome (Guillain–Mollaret triangle) and **indirect** via
    **cerebellar** and **brainstem** disorders.

**What is NOT here:** The right inferior olivary nucleus is
**not** the substrate for **motor weakness** (right
corticospinal tract — **NOT** in this container), **sensory
loss** (right medial lemniscus, right spinothalamic tract —
**NOT** in this container), **autonomic dysfunction** (right
RVLM, right CVLM, right NTS — **NOT** in this container), or
**respiratory rhythm** (right VRG, right DRG — **NOT** in this
container). Its clinical relevance is the **right cerebellar
motor-learning** and **Guillain–Mollaret triangle** functions
listed above.

Lateralization Notes
--------------------
This is the **right** inferior olivary nucleus module. The
olivary body is a **bilateral container** whose two sides are
**structurally symmetric mirror pairs** — and it carries **NO
warning**:

*   **Bilateral Symmetry:** The **right** and **left** inferior
    olivary nuclei are **structurally symmetric** — they are
    **mirror pairs** with the **same** cytoarchitecture, **same**
    contralateral projections, and **same** functions. The
    **right** nucleus projects to the **left** cerebellar
    hemisphere; the **left** nucleus projects to the **right**
    cerebellar hemisphere.

*   **Contralateral Projection to the Cerebellum:** Each
    **inferior olivary nucleus** projects **contralaterally** to
    its **ipsilateral** cerebellar hemisphere — **right
    inferior olivary nucleus → left cerebellar hemisphere** and
    **left inferior olivary nucleus → right cerebellar
    hemisphere**. This is **functionally** a **contralateral**
    circuit.

*   **NO Lateralization Warning:** The inferior olivary nucleus
    has **no known functional lateralization** at the **nucleus
    level**. Consumers must **not** import a **lateralization
    warning** into the right inferior olivary nucleus — the
    **right** and **left** nuclei are **functionally
    symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right inferior
    olivary nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the right inferior olivary nucleus.

*   **NO Fear-Output Warning:** The right inferior olivary
    nucleus is **not** a fear-output structure — it is a **right
    cerebellar climbing-fiber** source. Consumers must **not**
    conflate it with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "right inferior olivary nucleus = left
inferior olivary nucleus" will be structurally correct** — the
two sides are **symmetric** and **functionally equivalent** at
the **nucleus level**. The inferior olivary nucleus is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right inferior olivary
    nucleus is a **leaf** — it does **not** import from
    ``.../left/`` or any other left-side module. Bilateral
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
    any other container. The right inferior olivary nucleus's
    relationships to the right superior olivary complex, right
    medullary pyramid, right RVLM, right CVLM, right arcuate
    nucleus, right cranial nerve nuclei, right solitary nucleus,
    right respiratory centers, right inferior cerebellar
    peduncle, left cerebellar hemisphere, right red nucleus,
    and left dentate nucleus are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right inferior
    olivary nucleus is a **single structure** — it has **no
    structural children**. The **right accessory olivary nuclei**
    (medial accessory, dorsal accessory) are **prose
    subdivisions of the parent** ``.../olivary_body/right/`` —
    **NOT** structural children of this leaf.
*   **NOT the left inferior olivary nucleus.** The left inferior
    olivary nucleus is a **separate leaf** under
    ``.../olivary_body/left/inferior_olivary_nucleus/``.
    Consumers must **not** conflate the right with the left.
*   **NOT the right accessory olivary nuclei.** Those are
    **prose subdivisions of the parent** — **NOT** structural
    children of this leaf.
*   **NOT the right superior olivary complex.** The superior
    olivary complex is a **pontine auditory** structure — **NOT**
    a medullary cerebellar relay.
*   **NOT the right medullary pyramid or the right RVLM / right
    CVLM.** Those are **white-matter motor tract** and
    **autonomic nuclei** respectively.
*   **NOT the right arcuate nucleus, right cranial nerve nuclei,
    right solitary nucleus, or right respiratory centers.**
    Those are **chemosensory**, **motor**, **visceral-sensory**,
    and **respiratory** structures respectively.
*   **NOT the right inferior cerebellar peduncle or the left
    cerebellar hemisphere.** The **peduncle** is the
    **white-matter tract** that carries the olivocerebellar
    axons; the **cerebellum** is the **target** of the climbing
    fibers. The **nucleus** is the **grey-matter source** —
    **different structures**.
*   **NOT the right red nucleus or the left dentate nucleus.**
    Those are the **other two nodes** of the Guillain–Mollaret
    triangle — **different structures** in **different
    containers**. The **right red nucleus** is the **input**;
    the **left dentate nucleus** is the **output**.
*   **NOT the whole right olivary body.** The **right olivary
    body** (``.../olivary_body/right/``) is the **container**
    that contains this nucleus **plus** the right accessory
    olivary nuclei. Consumers must **not** conflate the
    **principal nucleus** with the **whole right olivary body**.
*   **No ``AREA_PATHS`` hop.** The right inferior olivary
    nucleus is a **local leaf** — it is not cross-listed under
    another brainparts path.
*   **No nested cross-listing.** The right inferior olivary
    nucleus has no nested dual-framing module. It is a **single
    leaf**.
*   **Structural parity with the left inferior olivary nucleus —
    strict mirror with NO warning.** The right and left modules
    are **structurally identical** — same leaf status, same
    **cerebellar climbing-fiber** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.olivary_body.right import inferior_olivary_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "olivary_body.right.inferior_olivary_nucleus"
    )

**Do not** assume the right inferior olivary nucleus is the
**left inferior olivary nucleus**. The left inferior olivary
nucleus is the **separate leaf** at
``.../olivary_body/left/inferior_olivary_nucleus/``.

**Do not** assume the right inferior olivary nucleus is the
**right accessory olivary nuclei**. The accessory nuclei are
**prose subdivisions of the parent** ``.../olivary_body/right/``
— **NOT** structural children of this leaf.

**Do not** assume the right inferior olivary nucleus is the
**right superior olivary complex**. The superior olivary complex
is a **pontine auditory** structure — **NOT** a medullary
cerebellar relay.

**Do not** assume the right inferior olivary nucleus is the
**right medullary pyramid**, the **right RVLM**, or the **right
CVLM**. Those are **white-matter motor tract** and **autonomic
nuclei** respectively.

**Do not** assume the right inferior olivary nucleus is the
**right inferior cerebellar peduncle** or the **left cerebellar
hemisphere**. The **peduncle** is the **white-matter tract**
that carries the olivocerebellar axons; the **cerebellum** is
the **target** of the climbing fibers.

**Do not** assume the right inferior olivary nucleus has
**structural children**. It is a **leaf** — it represents the
right inferior olivary nucleus as a **single structure**.

Iterating the right inferior olivary nucleus's (empty) children
(recommended consumer pattern)::

    RIGHT_INFERIOR_OLIVARY_NUCLEUS_CHILDREN = ()
    # The right inferior olivary nucleus is a leaf. It has no
    # structural children.

Reaching the left inferior olivary nucleus (recommended consumer
pattern — the contralateral leaf)::

    # The left inferior olivary nucleus is the CONTRALATERAL
    # leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.left.inferior_olivary_nucleus
    #
    # The right and left inferior olivary nuclei are structurally
    # symmetric mirror pairs with contralateral projections to
    # their respective cerebellar hemispheres.

Reaching the right accessory olivary nuclei (recommended
consumer pattern — NOTE they are prose subdivisions of the
parent)::

    # The right accessory olivary nuclei are PROSE SUBDIVISIONS
    # of the parent right olivary body container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.right
    #
    # They are NOT structural children of the right inferior
    # olivary nucleus — they are documented as prose at the
    # parent level.

Reaching the right superior olivary complex (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The right superior olivary complex is a PONTINE AUDITORY
    # structure, NOT a medullary cerebellar relay:
    #
    #   hindbrain.metencephalon.pons.superior_olivary_complex.right
    #
    # The superior olivary complex is part of the ascending
    # auditory pathway — DIFFERENT from the right inferior
    # olivary nucleus.

Reaching the Guillain-Mollaret triangle input (recommended
consumer pattern — NOTE the DIFFERENT structure)::

    # The RIGHT RED NUCLEUS is the INPUT to the right inferior
    # olivary nucleus via the RIGHT CENTRAL TEGMENTAL TRACT:
    #
    #   hindbrain.midbrain.tegmentum.red_nucleus.right
    #
    # Triangle: RIGHT red nucleus -> RIGHT inferior olivary
    # nucleus -> LEFT dentate nucleus -> RIGHT red nucleus.
    # Lesions in the RIGHT red nucleus or the RIGHT central
    # tegmental tract cause RIGHT hypertrophic olivary
    # degeneration.

Reaching the Guillain-Mollaret triangle output (recommended
consumer pattern — NOTE the DIFFERENT structure)::

    # The LEFT DENTATE NUCLEUS RECEIVES climbing fibers from the
    # right inferior olivary nucleus and projects back to the
    # RIGHT red nucleus via the LEFT SUPERIOR CEREBELLAR
    # PEDUNCLE:
    #
    #   hindbrain.metencephalon.cerebellum.nuclei.dentate_nucleus.left
    #
    # Lesions in the LEFT dentate nucleus or the LEFT superior
    # cerebellar peduncle cause RIGHT hypertrophic olivary
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