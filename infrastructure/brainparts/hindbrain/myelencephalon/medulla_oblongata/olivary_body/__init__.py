"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.olivary_body
=================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── olivary_body   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Olivary body; olive; oliva; inferior olivary
complex; inferior olive; olivary eminence; oliva medullae
oblongatae.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**grey-matter nuclear complex** — the **inferior olivary nuclear
complex** of the **medulla oblongata** — comprising the **principal
inferior olivary nucleus** and its associated **accessory olivary
nuclei** (medial accessory olivary nucleus, dorsal accessory
olivary nucleus). It is the **sole source of climbing fibers** to
the **cerebellar cortex**. It is **NOT** the **superior olivary
complex** — which is a **pontine auditory** structure (superior
olive, medial superior olive, lateral superior olive) wired under
``.../metencephalon/pons/superior_olivary_complex/``.
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each a
**leaf** representing the **left** or **right** inferior olivary
complex. The bilateral olivary bodies are the **structural
children** of this **bilateral container**; the container itself
is **unpaired**.
**Boundary status (NOT the superior olivary complex — a
DIFFERENT structure with a SIMILAR name):** **Boundary case — the
inferior olivary complex is NOT the superior olivary complex.**
The **superior olivary complex** (superior olive, medial superior
olive, lateral superior olive) is a **pontine auditory** structure
— part of the **ascending auditory pathway** — wired under
``.../metencephalon/pons/superior_olivary_complex/``. The
**inferior olivary complex** (here) is a **medullary
cerebellar-climbing-fiber** structure. **They share the name
"olive" but are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**
Consumers must **not** conflate the **inferior olivary complex**
with the **superior olivary complex** — resolve the superior
olivary complex via the **pons** container.
**Boundary status (NOT the medullary pyramid — the pyramid is the
ADJACENT white-matter tract):** **Boundary case — the inferior
olivary complex is NOT the medullary pyramid.** The **medullary
pyramid** (``.../medullary_pyramid/``) is the **ventral
white-matter** column of the **corticospinal / corticobulbar
tract**. The **inferior olivary complex** (here) is a
**grey-matter** cerebellar-climbing-fiber relay. **They are
DIFFERENT STRUCTURES** — the **pyramid** is **white matter**
(descending motor fibers); the **olivary body** is **grey matter**
(neurons). They are **adjacent** in the **ventral medulla** (the
pyramid is **medial**, the olivary body is **lateral**), but they
are **functionally and structurally distinct**. Consumers must
**not** conflate the two.
**Boundary status (NOT the RVLM / CVLM — ventrolateral
autonomic grey matter):** **Boundary case — the inferior olivary
complex is NOT the RVLM or CVLM.** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor** center; the **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay. The **inferior olivary complex**
(here) is a **cerebellar climbing-fiber** relay — a **somatic
sensorimotor** structure. **They are DIFFERENT STRUCTURES** —
the **RVLM** and **CVLM** are **autonomic** nuclei; the
**olivary body** is a **cerebellar relay**. They are **adjacent**
in the **ventrolateral medulla**, but they are **functionally
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the arcuate nucleus — a ventral-surface
chemosensory nucleus):** **Boundary case — the inferior olivary
complex is NOT the arcuate nucleus.** The **arcuate nucleus**
(``.../arcuate_nucleus/``) is a **ventral-surface grey-matter**
chemosensory and hypothalamic-projecting nucleus, adjacent to the
**anterior median fissure**. The **inferior olivary complex**
(here) is a **cerebellar climbing-fiber** relay, **dorsolateral**
to the pyramid. **They are DIFFERENT STRUCTURES** — the
**arcuate nucleus** is **ventral-surface chemosensory**; the
**olivary body** is **cerebellar relay**. Consumers must **not**
conflate the two.
**Boundary status (NOT the cranial nerve nuclei — dorsal /
ventrolateral motor nuclei):** **Boundary case — the inferior
olivary complex is NOT the cranial nerve nuclei.** The **cranial
nerve nuclei** (``.../cranial_nerve_nuclei/``) are the **dorsal
and ventrolateral grey-matter motor** nuclei (hypoglossal, dorsal
motor vagus, inferior salivatory, nucleus ambiguus). The
**inferior olivary complex** (here) is a **cerebellar
climbing-fiber** relay. **They are DIFFERENT STRUCTURES** — the
**cranial nerve nuclei** are **motor**; the **olivary body** is
a **cerebellar relay**. Consumers must **not** conflate the two.
**Boundary status (NOT the solitary nucleus — a visceral
afferent relay):** **Boundary case — the inferior olivary complex
is NOT the solitary nucleus.** The **solitary nucleus** (NTS)
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
it receives **taste**, **baroreceptor**, **chemoreceptor**, and
**gastrointestinal** afferents. It is a **sensory** nucleus. The
**inferior olivary complex** (here) is a **cerebellar
climbing-fiber** relay — **NOT** a visceral afferent nucleus.
Consumers must **not** conflate the two.
**Boundary status (NOT the respiratory centers — a different
grey-matter functional system):** **Boundary case — the inferior
olivary complex is NOT the respiratory centers.** The
**respiratory centers** (``.../respiratory_center/`` and
``.../ventral_respiratory_group/``) are the **medullary
respiratory rhythm** and **pattern** generators. The **inferior
olivary complex** (here) is a **cerebellar climbing-fiber**
relay. **They are DIFFERENT STRUCTURES** — the **respiratory
centers** are **autonomic respiratory**; the **olivary body** is
a **cerebellar sensorimotor** relay. Consumers must **not**
conflate the two.
**Boundary status (NOT the inferior cerebellar peduncle — the
adjacent white-matter tract):** **Boundary case — the inferior
olivary complex is NOT the inferior cerebellar peduncle.** The
**inferior cerebellar peduncle** (restiform body +
juxtarestiform body) is a **white-matter tract** that carries
**olivocerebellar** (climbing) fibers and **spinocerebellar**
(dorsal) fibers to the cerebellum. The **inferior olivary
complex** (here) is the **grey-matter** nucleus of origin of the
**climbing fibers** — the **olivocerebellar fibers** **travel
through** the inferior cerebellar peduncle, but the **nucleus**
and the **peduncle** are **different structures**. Consumers must
**not** conflate the **nucleus** with the **white-matter
peduncle**.
**Boundary status (NOT the cerebellum — a separate structure in
the metencephalon):** **Boundary case — the inferior olivary
complex is NOT the cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is a **separate structure**
in the **metencephalon**. The **inferior olivary complex** (here)
**projects** to the cerebellum via **climbing fibers**, but it is
**NOT** the cerebellum itself. Consumers must **not** conflate the
two.
**Boundary status (NOT the red nucleus — a midbrain
olivocerebellar-triangle structure):** **Boundary case — the
inferior olivary complex is NOT the red nucleus.** The **red
nucleus** (``.../midbrain/tegmentum/red_nucleus/``) is a
**midbrain** motor structure. It is part of the **Guillain–
Mollaret triangle** (red nucleus → inferior olive → cerebellar
dentate nucleus → red nucleus), but the **red nucleus** and the
**inferior olivary complex** are **different structures** in
**different containers**. Consumers must **not** conflate the
two.
**Boundary status (NOT the dentate nucleus — a cerebellar
nucleus):** **Boundary case — the inferior olivary complex is
NOT the dentate nucleus.** The **dentate nucleus**
(``.../metencephalon/cerebellum/nuclei/dentate_nucleus/``) is a
**cerebellar output** nucleus. It is part of the **Guillain–
Mollaret triangle**, but the **dentate nucleus** and the
**inferior olivary complex** are **different structures** in
**different containers**. Consumers must **not** conflate the
two.
**Boundary status (NOT the whole medulla oblongata — a
relatively large grey-matter structure within it):** **Boundary
case — the inferior olivary complex is NOT the whole medulla
oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the cranial nerve nuclei, the autonomic nuclei, the
respiratory centers, the olivary body (here), the medullary
pyramid, the arcuate nucleus, and other structures. The
**inferior olivary complex** is **one relatively large
grey-matter structure** within the medulla. Consumers must **not**
conflate the **olivary body** with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
structural children):** **Boundary case — the inferior olivary
complex is a BILATERAL container with ``left`` and ``right``
structural children.** The **olivary_body** module (here) is an
**unpaired container**; its **structural children** are ``left``
and ``right`` — each a **leaf** representing the **left** or
**right** inferior olivary complex. Consumers must **not** look
for a single unpaired inferior olivary complex — the **left** and
**right** olivary complexes are **separate modules** under this
container. Resolve them via ``olivary_body.left`` and
``olivary_body.right``.

Overview
--------
The **olivary body** (inferior olivary complex) is a **grey-matter
nuclear complex** in the **ventrolateral medulla oblongata** — the
**sole source of climbing fibers** to the **cerebellar cortex**.
It lies **dorsolateral** to the **medullary pyramid** and
**medial** to the **inferior cerebellar peduncle**, and it is
visible as a **paired prominent bulge** (the **olive**) on the
**ventrolateral medullary surface**.

**The olivary body is the INFERIOR olivary complex, NOT the
superior olivary complex.** The **superior olivary complex** is a
**pontine auditory** structure — **NOT** a medullary cerebellar
relay. **They share the name "olive" but are DIFFERENT
STRUCTURES in DIFFERENT CONTAINERS.** The **inferior olivary
complex** is the **cerebellar climbing-fiber source**; the
**superior olivary complex** is an **auditory brainstem relay**.

**The olivary body is a GREY-MATTER structure, NOT a white-matter
tract.** It is the **source of the olivocerebellar fibers** — the
**climbing fibers** that **travel through** the **inferior
cerebellar peduncle** to the **contralateral cerebellar cortex**.
It is **NOT** the **inferior cerebellar peduncle** (the
white-matter tract that carries the fibers), **NOT** the
**medullary pyramid** (the adjacent corticospinal tract), and
**NOT** the **RVLM** / **CVLM** (the adjacent autonomic nuclei).

**The olivary body is a BILATERAL container.** Its structural
children are ``left`` and ``right`` — each a leaf representing the
left or right inferior olivary complex. The **container itself**
is **unpaired**.

**The olivary body is a CEREBELLAR RELAY, NOT a motor nucleus and
NOT an autonomic nucleus.** It **does not** send motor axons to
muscles and **does not** regulate autonomic function. It
**projects** to the cerebellum via climbing fibers and
**participates** in **cerebellar motor learning** and
**timing** — particularly for **eyeblink conditioning**,
**vestibulo-ocular reflex adaptation**, and **sensorimotor
synchronization**.

**The olivary body is part of the Guillain–Mollaret triangle.**
The **Guillain–Mollaret triangle** is a **three-structure
circuit** — the **red nucleus** (midbrain) → the **inferior
olivary complex** (medulla) → the **contralateral cerebellar
dentate nucleus** → the **contralateral red nucleus**. This
triangle is **clinically relevant** — lesions in **any of its
three nodes** cause **hypertrophic olivary degeneration** and
**palatal tremor** (see *Associated Disorders*).

Bilateral Structure
-------------------
The olivary body is a **bilateral container** with **two
structural children**:

*   ``left`` — the **left** inferior olivary complex (a leaf
    module).
*   ``right`` — the **right** inferior olivary complex (a leaf
    module).

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left** and
**right** inferior olivary complexes as **single structures**, not
as further sub-containers. Consumers that need **side-specific**
resolution should descend into ``left`` or ``right``; consumers
that need **bilateral** resolution should iterate over both.

**The container itself is unpaired.** There is **no**
``olivary_body/left/.../`` structural hierarchy beyond the single
leaf level — the ``left`` and ``right`` modules are the
**terminal modules** for this structure.

The Olivary Body / Superior Olivary Complex Boundary
----------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Inferior olivary complex** (this module) — the **medullary
    cerebellar climbing-fiber** relay.

*   **Superior olivary complex** (superior olive, medial superior
    olive, lateral superior olive)
    (``.../metencephalon/pons/superior_olivary_complex/``) — the
    **pontine auditory** relay.

**They share the name "olive" but are DIFFERENT STRUCTURES in
DIFFERENT CONTAINERS.** Consumers must **not** conflate the
**inferior olivary complex** with the **superior olivary
complex** — resolve the superior olivary complex via the **pons**
container.

The Olivary Body / Medullary Pyramid Boundary
---------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Inferior olivary complex** (this module) — the **grey-matter
    cerebellar climbing-fiber** relay.

*   **Medullary pyramid** (``.../medullary_pyramid/``) — the
    **ventral white-matter** corticospinal / corticobulbar tract.

**They are DIFFERENT STRUCTURES** — the **pyramid** is **white
matter**; the **olivary body** is **grey matter**. They are
**adjacent** in the **ventral medulla** (the pyramid is
**medial**, the olivary body is **lateral**), but they are
**functionally and structurally distinct**. Consumers must **not**
conflate the two.

The Olivary Body / RVLM and CVLM Boundary
-----------------------------------------
This is the **cerebellar-relay / autonomic** boundary:

*   **Inferior olivary complex** (this module) — the **cerebellar
    climbing-fiber** relay.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) and
    **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **ventrolateral autonomic** nuclei.

**They are DIFFERENT STRUCTURES** — the **RVLM** and **CVLM** are
**autonomic** nuclei; the **olivary body** is a **cerebellar
relay**. They are **adjacent** in the **ventrolateral medulla**,
but they are **functionally distinct**. Consumers must **not**
conflate the two.

The Olivary Body / Arcuate Nucleus Boundary
-------------------------------------------
This is the **cerebellar-relay / chemosensory** boundary:

*   **Inferior olivary complex** (this module) — the **cerebellar
    climbing-fiber** relay.

*   **Arcuate nucleus** (``.../arcuate_nucleus/``) — the
    **ventral-surface chemosensory** nucleus.

**They are DIFFERENT STRUCTURES** — the **arcuate nucleus** is
**ventral-surface chemosensory**; the **olivary body** is
**cerebellar relay**. Consumers must **not** conflate the two.

The Olivary Body / Cranial Nerve Nuclei Boundary
------------------------------------------------
This is the **cerebellar-relay / motor** boundary:

*   **Inferior olivary complex** (this module) — the **cerebellar
    climbing-fiber** relay.

*   **Cranial nerve nuclei** (``.../cranial_nerve_nuclei/``) — the
    **dorsal / ventrolateral motor** nuclei.

**They are DIFFERENT STRUCTURES** — the **cranial nerve nuclei**
are **motor**; the **olivary body** is a **cerebellar relay**.
Consumers must **not** conflate the two.

The Olivary Body / Solitary Nucleus Boundary
--------------------------------------------
This is the **cerebellar-relay / visceral-sensory** boundary:

*   **Inferior olivary complex** (this module) — the **cerebellar
    climbing-fiber** relay.

*   **Solitary nucleus** (``.../solitary_nucleus/``) — the
    **visceral afferent sensory** relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Olivary Body / Respiratory Centers Boundary
-----------------------------------------------
This is the **cerebellar-relay / respiratory** boundary:

*   **Inferior olivary complex** (this module) — the **cerebellar
    climbing-fiber** relay.

*   **Respiratory centers** (``.../respiratory_center/`` and
    ``.../ventral_respiratory_group/``) — the **medullary
    respiratory rhythm** and **pattern** generators.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Olivary Body / Inferior Cerebellar Peduncle Boundary
--------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Inferior olivary complex** (this module) — the **grey-matter
    nucleus** of origin of the **climbing fibers**.

*   **Inferior cerebellar peduncle** — the **white-matter tract**
    that carries the **olivocerebellar** (climbing) fibers and
    **spinocerebellar** (dorsal) fibers to the cerebellum.

**The olivocerebellar fibers travel THROUGH the inferior
cerebellar peduncle — but the nucleus and the peduncle are
DIFFERENT STRUCTURES.** Consumers must **not** conflate the
**nucleus** with the **white-matter peduncle**.

The Olivary Body / Cerebellum Boundary
--------------------------------------
This is the **relay / target** boundary:

*   **Inferior olivary complex** (this module) — the **climbing
    fiber** source.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the
    **target** of the climbing fibers.

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.**
Consumers must **not** conflate the **olivary body** with the
**cerebellum** — the olivary body **projects** to the cerebellum,
but it is **NOT** the cerebellum itself.

The Olivary Body / Red Nucleus and Dentate Nucleus Boundary
-----------------------------------------------------------
This is the **Guillain–Mollaret triangle** boundary:

*   **Inferior olivary complex** (this module) — one of the **three
    nodes** of the **Guillain–Mollaret triangle**.

*   **Red nucleus** (``.../midbrain/tegmentum/red_nucleus/``) — a
    **midbrain** node of the triangle.

*   **Dentate nucleus**
    (``.../metencephalon/cerebellum/nuclei/dentate_nucleus/``) —
    a **cerebellar** node of the triangle.

**They are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** The
**Guillain–Mollaret triangle** (red nucleus → inferior olivary
complex → contralateral dentate nucleus → contralateral red
nucleus) **connects** them, but each is a **separate structure**.
Consumers must **not** conflate the three.

Function in the Human Brain
---------------------------
The olivary body's function is **cerebellar climbing-fiber
relay** — **NOT motor conduction**, **NOT autonomic regulation**,
and **NOT sensory relay**:

*   **Climbing-fiber output to the cerebellum:** The **inferior
    olivary complex** is the **sole source** of **climbing
    fibers** to the **cerebellar cortex** — the **olivocerebellar
    pathway** projects to the **contralateral cerebellar
    hemisphere** (via the **inferior cerebellar peduncle**). Each
    Purkinje cell receives **exactly one** climbing fiber — a
    **powerful, low-frequency** input that triggers **complex
    spikes** in the Purkinje cell.

*   **Cerebellar motor learning:** The **climbing-fiber**
    **error signal** is **critical** for **cerebellar motor
    learning** — especially **eyeblink conditioning**,
    **vestibulo-ocular reflex adaptation**, and **sensorimotor
    synchronization**. The **climbing fiber** is the **teaching
    signal** that drives **long-term depression** (LTD) at the
    **parallel fiber → Purkinje cell** synapse.

*   **Timing and synchrony:** The **inferior olivary complex**
    neurons are **electrically coupled** via **gap junctions** —
    producing **synchronous, rhythmic** climbing-fiber
    activation that contributes to **cerebellar timing** and
    **sensorimotor synchronization**.

*   **NOT motor conduction:** The **inferior olivary complex**
    does **not** send motor axons to muscles — the **motor
    conduction** is the **corticospinal tract** (via the
    **medullary pyramid**).

*   **NOT autonomic regulation:** The **inferior olivary
    complex** does **not** regulate autonomic function — the
    **autonomic regulation** is the **RVLM**, **CVLM**, and
    **NTS**.

*   **NOT sensory relay:** The **inferior olivary complex**
    does **not** relay **somatic** or **visceral** sensation —
    the **sensory relays** are the **medial lemniscus**,
    **spinothalamic tract**, and **solitary nucleus**.

**The unifying theme:** the olivary body is the **sole source of
climbing fibers** to the **cerebellar cortex** — the **climbing
fiber** is the **error signal** for **cerebellar motor learning**
and **timing**, delivered via the **olivocerebellar pathway**
through the **inferior cerebellar peduncle** to the
**contralateral cerebellar hemisphere**.

Associated Disorders
--------------------
The olivary body is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct**, via
**climbing-fiber dysfunction** and **Guillain–Mollaret triangle**
lesions:

*   **Hypertrophic olivary degeneration (HOD — via Guillain–
    Mollaret triangle lesions):** **Transsynaptic degeneration**
    of the **inferior olivary complex** after a lesion in the
    **Guillain–Mollaret triangle** — the **dentato-rubro-olivary
    pathway** (red nucleus → inferior olive → contralateral
    dentate nucleus → contralateral red nucleus). **Any lesion**
    in the triangle — **dentate nucleus** (e.g., **cerebellar
    hemorrhage**, **infarction**, **tumor**), **red nucleus**
    (e.g., **midbrain stroke**), or the **central tegmental
    tract** (e.g., **pontine stroke**) — causes **hypertrophic
    olivary degeneration** over **weeks to months**. **Imaging**
    shows **T2 hyperintensity** and **enlargement** of the
    inferior olivary complex — **counterintuitive** because
    **most** degenerations cause **atrophy**, but **HOD** causes
    **hypertrophy** (the **neurons** undergo **swelling** and
    **hypertrophy** of the **neuropil** before eventual atrophy).

*   **Palatal tremor / palatal myoclonus (via Guillain–Mollaret
    triangle lesions):** **Rhythmic, involuntary** contraction of
    the **soft palate** — **frequently** accompanies
    **hypertrophic olivary degeneration** after a **Guillain–
    Mollaret triangle** lesion. The **inferior olivary complex**
    is the **direct substrate** of **palatal tremor** —
    **disinhibition** of the **inferior olive** after
    **triangle** lesions produces **rhythmic**, **synchronous**
    olivary **oscillations** that **drive** the **palatal
    tremor** via **brainstem** and **cerebellar** circuits.
    Some patients also have **ocular myoclonus**, **tremor of
    the extremities**, or **cerebellar ataxia**.

*   **Cerebellar motor-learning deficits (via climbing-fiber
    dysfunction):** **Impaired eyeblink conditioning**,
    **impaired vestibulo-ocular reflex adaptation**, and
    **impaired sensorimotor timing** — from **climbing-fiber**
    loss or **olivary** dysfunction. The **inferior olivary
    complex** is the **direct substrate** of these **cerebellar
    motor-learning** findings.

*   **Brainstem stroke (via olivary involvement):** **Medial
    medullary syndrome** or **lateral medullary syndrome** can
    **involve** the **inferior olivary complex** (or its
    **connections**), causing **cerebellar ataxia**,
    **tremor**, or **palatal tremor**. The **olivary body** is
    an **indirect** contributor to these **brainstem stroke**
    syndromes.

*   **Neurodegenerative diseases (via olivary involvement):**
    **Multiple system atrophy (MSA)** can involve the **inferior
    olivary complex** — contributing to **cerebellar ataxia** in
    **MSA-C**. **Spinocerebellar ataxias (SCAs)** may involve
    the **inferior olivary complex** (e.g., **SCA1**, **SCA2**,
    **SCA3**) — contributing to **ataxia** and **oculomotor**
    findings.

*   **No Named "Olivary Body Syndrome":** The olivary body is a
    **cerebellar relay** — its clinical relevance is **direct**
    via the **hypertrophic olivary degeneration / palatal tremor**
    syndrome (Guillain–Mollaret triangle) and **indirect** via
    **cerebellar** and **brainstem** disorders.

**What is NOT here:** The olivary body is **not** the substrate
for **motor weakness** (corticospinal tract — **NOT** in this
container), **sensory loss** (medial lemniscus, spinothalamic
tract — **NOT** in this container), **autonomic dysfunction**
(RVLM, CVLM, NTS — **NOT** in this container), or **respiratory
rhythm** (VRG, DRG — **NOT** in this container). Its clinical
relevance is the **cerebellar motor-learning** and **Guillain–
Mollaret triangle** functions listed above.

Lateralization Notes
--------------------
The olivary body is a **bilateral container** with ``left`` and
``right`` structural children. There is **no**
``olivary_body/left/.../`` structural hierarchy beyond the single
leaf level.

*   **Bilateral structural children:** ``left`` and ``right`` are
    **leaf modules** — each represents the **left** or **right**
    inferior olivary complex as a **single structure**. Consumers
    resolve the **left** inferior olivary complex via
    ``olivary_body.left`` and the **right** via
    ``olivary_body.right``.

*   **Bilateral symmetry:** The **left** and **right** inferior
    olivary complexes are **structurally symmetric** — they are
    **mirror pairs** with the **same** cytoarchitecture, **same**
    projections (contralateral to the cerebellum), and **same**
    functions.

*   **Contralateral projection to the cerebellum:** Each
    **inferior olivary complex** projects **contralaterally** to
    its **ipsilateral** cerebellar hemisphere — **left inferior
    olivary complex → right cerebellar hemisphere** and **right
    inferior olivary complex → left cerebellar hemisphere**. This
    is a **functionally** contralateral projection.

*   **NO lateralization warning:** The olivary body has **no
    known functional lateralization** at the **tract level**.
    Consumers must **not** import a **lateralization warning**
    into the olivary body — the **left** and **right** olivary
    complexes are **functionally symmetric**.

*   **NO extended-amygdala / fear-output / SLEA warnings:** The
    olivary body is **not** part of the amygdala,
    extended-amygdala, or SLEA continuum. It carries **no SLEA
    warning** and **no fear-output warning**.

**A consumer that assumes "left inferior olivary complex = right
inferior olivary complex" will be structurally correct** — the
two sides are **symmetric** and **functionally equivalent** at
the **tract level**. The olivary body is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no fear-output
warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The olivary body is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../metencephalon/pons/superior_olivary_complex/``,
    ``.../medullary_pyramid/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../arcuate_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../solitary_nucleus/``, ``.../respiratory_center/``,
    ``.../ventral_respiratory_group/``,
    ``.../metencephalon/cerebellum/``, ``.../midbrain/``, or any
    other container. The olivary body's relationships to the
    superior olivary complex, medullary pyramid, RVLM, CVLM,
    arcuate nucleus, cranial nerve nuclei, solitary nucleus,
    respiratory centers, inferior cerebellar peduncle, cerebellum,
    red nucleus, and dentate nucleus are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children.** The structural
    children are ``left`` and ``right``, each a **leaf**. The
    container itself is **unpaired**.
*   **NOT the superior olivary complex.** The superior olivary
    complex is a **pontine auditory** structure — **NOT** a
    medullary cerebellar relay. Consumers must **not** conflate
    the two.
*   **NOT the medullary pyramid or the RVLM / CVLM.** Those are
    **white-matter motor tract** and **autonomic nuclei**
    respectively — **NOT** a cerebellar relay.
*   **NOT the arcuate nucleus, cranial nerve nuclei, solitary
    nucleus, or respiratory centers.** Those are
    **chemosensory**, **motor**, **visceral-sensory**, and
    **respiratory** structures respectively.
*   **NOT the inferior cerebellar peduncle or the cerebellum.**
    The **peduncle** is the **white-matter tract** that carries
    the olivocerebellar fibers; the **cerebellum** is the
    **target** of the climbing fibers. The **nucleus** is the
    **grey-matter source** — **different structures**.
*   **NOT the red nucleus or the dentate nucleus.** Those are
    the **other two nodes** of the Guillain–Mollaret triangle —
    **different structures** in **different containers**.
*   **No ``AREA_PATHS`` hop.** The olivary body is a **local
    container** — it is not cross-listed under another brainparts
    path.
*   **No nested cross-listing.** The olivary body has no nested
    dual-framing module. It is a **bilateral container** with
    **two leaf children**.
*   **Structural parity with the right side — strict mirror.** The
    ``left`` and ``right`` leaves are **structurally identical**
    — same leaf status, same **cerebellar climbing-fiber relay**
    framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import olivary_body

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.olivary_body"
    )

**Do not** assume the olivary body is the **superior olivary
complex**. The **superior olivary complex** is a **pontine
auditory** structure — **NOT** a medullary cerebellar relay.

**Do not** assume the olivary body is the **medullary pyramid**
or the **RVLM** / **CVLM**. Those are **white-matter motor
tract** and **autonomic nuclei** respectively.

**Do not** assume the olivary body is the **inferior cerebellar
peduncle** or the **cerebellum**. The **peduncle** is the
**white-matter tract** that carries the olivocerebellar fibers;
the **cerebellum** is the **target** of the climbing fibers.
The **nucleus** is the **grey-matter source** — **different
structures**.

**Do not** look for a single unpaired inferior olivary complex.
The **left** and **right** olivary complexes are **separate leaf
modules** under this container.

Iterating the olivary body's structural children (recommended
consumer pattern)::

    OLIVARY_BODY_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # inferior olivary complex.

Reaching the left and right inferior olivary complexes
(recommended consumer pattern)::

    # The left and right inferior olivary complexes are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.left
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.right
    #
    # Each is a leaf module representing the inferior olivary
    # complex of that side.

Reaching the superior olivary complex (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The superior olivary complex is a PONTINE AUDITORY
    # structure, NOT a medullary cerebellar relay:
    #
    #   hindbrain.metencephalon.pons.superior_olivary_complex
    #
    # The superior olivary complex is part of the ascending
    # auditory pathway — DIFFERENT from the inferior olivary
    # complex (cerebellar climbing-fiber relay).

Reaching the medullary pyramid and RVLM/CVLM (recommended
consumer pattern — NOTE the DIFFERENT structures)::

    # The medullary pyramid and the RVLM/CVLM are DIFFERENT from
    # the olivary body:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #
    # The pyramid is the ventral white-matter corticospinal /
    # corticobulbar tract; the RVLM and CVLM are ventrolateral
    # autonomic nuclei. The olivary body is DORSOLATERAL to the
    # pyramid — a cerebellar climbing-fiber relay.

Reaching the cerebellum and inferior cerebellar peduncle
(recommended consumer pattern — NOTE the DIFFERENT structures)::

    # The cerebellum and the inferior cerebellar peduncle are
    # DIFFERENT from the olivary body:
    #
    #   hindbrain.metencephalon.cerebellum
    #   (the inferior cerebellar peduncle is a white-matter tract
    #    that carries the olivocerebellar fibers)
    #
    # The olivary body PROJECTS to the cerebellum via climbing
    # fibers, but it is NOT the cerebellum itself.

Reaching the Guillain-Mollaret triangle nodes (recommended
consumer pattern — NOTE the DIFFERENT structures)::

    # The red nucleus and dentate nucleus are the OTHER TWO
    # nodes of the Guillain-Mollaret triangle:
    #
    #   hindbrain.midbrain.tegmentum.red_nucleus
    #   hindbrain.metencephalon.cerebellum.nuclei.dentate_nucleus
    #
    # The triangle connects: red nucleus -> inferior olivary
    # complex -> contralateral dentate nucleus -> contralateral
    # red nucleus. Lesions in ANY of the three nodes cause
    # hypertrophic olivary degeneration and palatal tremor.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"olivary_body.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Inferior olivary complex; olivocerebellar pathway;
    climbing fibers; Guillain-Mollaret triangle.)
*   **Inferior olive — microcircuitry and function:** De Zeeuw,
    C.I., et al. (1998). "Microcircuitry and function of the
    inferior olive." *Trends in Neurosciences* 21:391–400.
    (Inferior olivary complex; gap junctions; climbing fibers;
    complex spikes; olivocerebellar pathway.)
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
*   **Guillain-Mollaret triangle:** Guillain, G., Mollaret, P.
    (1931). "Deux cas de myoclonies synchrones et rythmées
    vélo-pharyngo-laryngo-oculo-diaphragmatiques." *Revue
    Neurologique* 2:545–566. (Guillain-Mollaret triangle; red
    nucleus → inferior olive → dentate nucleus → red nucleus;
    palatal tremor.)
*   **Hypertrophic olivary degeneration:** Goto, N., Kaneko, M.
    (1981). "Olivary enlargement: chronological and
    morphometric studies." *Acta Neuropathologica* 54:275–282.
    (Hypertrophic olivary degeneration; transsynaptic
    degeneration; Guillain-Mollaret triangle lesions.)
*   **Palatal tremor:** Deuschl, G., et al. (1990). "Symptomatic
    and essential palatal tremor: clinical and
    polysomnographic differences." *Brain* 113:1645–1660.
    (Palatal tremor; essential vs. symptomatic; Guillain-
    Mollaret triangle; hypertrophic olivary degeneration.)
*   **Olivary hypertrophy imaging:** Kitajima, M., et al. (2018).
    "Hypertrophic olivary degeneration: a comprehensive review."
    *Japanese Journal of Radiology* 36:151–160. (HOD imaging
    findings; T2 hyperintensity; olivary enlargement; Guillain-
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
    olive — DIFFERENT from the inferior olivary complex.)
*   **Medial medullary syndrome (contrast — includes medial
    lemniscus and pyramid, not olivary body):** Bassetti, C., et
    al. (1996). "Medial medullary stroke: clinical and MRI
    findings." *Neurology* 46:106–110. (Dejerine syndrome;
    medullary pyramid and medial lemniscus — NOT the olivary
    body.)
*   **Lateral medullary syndrome (contrast — includes lateral
    medulla, not olivary body):** Sacco, R.L., et al. (1993).
    "Lateral medullary infarction: clinical and MRI correlation."
    *Stroke* 24:1981–1987. (Wallenberg syndrome; lateral medulla
    — NOT the olivary body.)
*   NeuroNames — Inferior olivary complex; FMA — Inferior
    olivary complex.
"""