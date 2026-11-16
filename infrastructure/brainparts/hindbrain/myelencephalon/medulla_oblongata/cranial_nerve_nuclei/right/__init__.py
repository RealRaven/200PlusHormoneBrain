"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right
================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── cranial_nerve_nuclei
                └── right   <-- THIS MODULE
                    ├── dorsal_motor_nucleus_vagus
                    ├── hypoglossal_nucleus
                    ├── inferior_salivatory_nucleus
                    └── nucleus_ambiguus

**Primary synonym:** Right medullary cranial nerve nuclei; right
cranial nerve nuclei IX–XII; right bulbar motor nuclei; right
medullary motor column.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter container** — the **right-side motor
cranial nerve nuclei** of the **medulla oblongata**, comprising
the **right general somatic efferent** (hypoglossal — XII),
**right general visceral efferent / parasympathetic** (dorsal
motor nucleus of vagus — X; inferior salivatory nucleus — IX), and
**right special visceral efferent / branchial motor** (nucleus
ambiguus — IX/X/XI) columns.
**Part of:** The **cranial_nerve_nuclei** bilateral container —
which is part of the **medulla oblongata** — the **caudal
brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../cranial_nerve_nuclei/`` → **direct
child** of the cranial_nerve_nuclei container. The **right**
cranial nerve nuclei container is one of the **two** structural
children of the container (the other is ``left``).
**Structural children:** **Four —** each a **leaf** representing
the **right** side of one of the four motor nuclei:
1. ``dorsal_motor_nucleus_vagus`` — **CN X** — general visceral
   efferent (parasympathetic).
2. ``hypoglossal_nucleus`` — **CN XII** — general somatic efferent
   (tongue motor).
3. ``inferior_salivatory_nucleus`` — **CN IX** — general visceral
   efferent (parasympathetic to parotid).
4. ``nucleus_ambiguus`` — **CN IX/X/XI** — special visceral
   efferent (branchial motor to pharynx/larynx).
**Boundary status (NOT the left cranial nerve nuclei container —
the contralateral container):** **Boundary case — the right
cranial nerve nuclei container is NOT the left cranial nerve
nuclei container.** The **left cranial nerve nuclei container**
(``.../cranial_nerve_nuclei/left/``) is the **contralateral
container** — the cranial nerve nuclei of the **left** medulla.
**They are DIFFERENT CONTAINERS** — the ``left`` and ``right``
modules are the two sides of the **bilateral parent container**.
Consumers must **not** conflate the **right** container with the
**left** container — resolve the left side via
``cranial_nerve_nuclei.left``.
**Boundary status (NOT the parent cranial_nerve_nuclei container
— a SIDE of it):** **Boundary case — the right cranial nerve
nuclei container is NOT the parent cranial_nerve_nuclei
container.** The **parent** (``.../cranial_nerve_nuclei/``) is
the **unpaired bilateral container** — it contains **both** the
``left`` and ``right`` sides. The **right** container (here) is
**one side** of that parent. Consumers must **not** conflate the
**right container** with the **parent container** — the parent
contains **both sides**; the right container contains **only the
right side**.
**Boundary status (NOT a single nucleus — a CONTAINER of four
nuclei):** **Boundary case — the right cranial nerve nuclei
container is a CONTAINER, not a single nucleus.** It contains
**four distinct leaf nuclei** — the **right dorsal motor nucleus
of vagus**, the **right hypoglossal nucleus**, the **right
inferior salivatory nucleus**, and the **right nucleus ambiguus**.
Each is a **separate structure** with **different functions**
(parasympathetic, somatic motor, parasympathetic, branchial
motor). Consumers must **not** treat the **right** container as a
single uniform nucleus — it is a **container** of **four
functionally distinct nuclei**.
**Boundary status (NOT the right solitary nucleus — the NTS is
the VISCERAL AFFERENT relay, not a motor nucleus):** **Boundary
case — the right cranial nerve nuclei container is NOT the right
solitary nucleus.** The **right solitary nucleus** (NTS)
(``.../solitary_nucleus/right/``) is the **right visceral
afferent relay** — it receives **taste**, **baroreceptor**,
**chemoreceptor**, and **gastrointestinal** afferents from **CN
VII, IX, and X**. It is **NOT a motor nucleus** — it is a
**sensory** nucleus. The **right cranial nerve nuclei container**
(here) contains the **MOTOR** cranial nerve nuclei of the right
medulla. The **right NTS** is **anatomically adjacent** but is
**NOT** in this container. Consumers must **not** expect to find
the **right solitary nucleus** under
``cranial_nerve_nuclei.right`` — resolve it via
``.../solitary_nucleus/right/``.
**Boundary status (NOT the right spinal trigeminal nucleus — a
sensory nucleus, not a motor nucleus):** **Boundary case — the
right cranial nerve nuclei container is NOT the right spinal
trigeminal nucleus.** The **right spinal trigeminal nucleus** (and
its tract) is the **right facial pain/temperature** sensory relay
— it receives **CN V** afferents from the **right** face and is
**NOT** a motor nucleus. It is **not** wired under
``cranial_nerve_nuclei.right`` in this tree. Consumers must **not**
expect to find the **right spinal trigeminal nucleus** here.
**Boundary status (NOT the right reticular formation — a
cross-container system):** **Boundary case — the right cranial
nerve nuclei container is NOT the right reticular formation.** The
**reticular formation** is a **cross-container system** — its
medullary components are wired under
``.../paramedian_reticular_nucleus/`` and
``.../respiratory_center/gigantocellular_reticular_nucleus/``,
**not** under ``cranial_nerve_nuclei``. The **right cranial nerve
nuclei container** (here) contains **motor cranial nerve nuclei**
— **not** the reticular formation. Consumers must **not**
conflate the two.
**Boundary status (NOT the right RVLM / right CVLM / right
arcuate nucleus — those are autonomic / chemosensory):**
**Boundary case — the right cranial nerve nuclei container is NOT
the right ventrolateral medullary structures.** The **right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) is the **right
sympathetic premotor** center; the **right CVLM**
(``.../caudal_ventrolateral_medulla/right/``) is the **right
sympathoinhibitory** relay; the **right arcuate nucleus**
(``.../arcuate_nucleus/right/``) is a **right ventral-surface
chemosensory** nucleus. These are **NOT cranial nerve motor
nuclei** — they are **autonomic / chemosensory** structures.
Consumers must **not** conflate the **right cranial nerve nuclei
container** with the **right ventrolateral medullary structures**.
**Boundary status (NOT the right olivary body or the right
medullary pyramid — those are different structures):** **Boundary
case — the right cranial nerve nuclei container is NOT the right
olivary body or the right medullary pyramid.** The **right olivary
body** (``.../olivary_body/right/``) contains the **right
inferior olivary nucleus** (right cerebellar climbing fibers); the
**right medullary pyramid** (``.../medullary_pyramid/right/``) is
the **right corticospinal / corticobulbar tract**. These are
**NOT** cranial nerve nuclei. Consumers must **not** conflate the
**right cranial nerve nuclei container** with these structures.
**Boundary status (NOT the right pontine or right midbrain
cranial nerve nuclei — those are in different containers):**
**Boundary case — the right cranial nerve nuclei container is NOT
the right pontine or right midbrain cranial nerve nuclei.** The
**right pontine** cranial nerve nuclei (V, VI, VII, VIII) are
wired under ``.../metencephalon/pons/cranial_nerve_nuclei/right/``;
the **right midbrain** cranial nerve nuclei (III, IV, V
mesencephalic) are wired under
``.../midbrain/cranial_nerve_nuclei/right/``. The **right cranial
nerve nuclei container** (here) is **MEDULLARY** — it contains
**only** the **right medullary** cranial nerve nuclei (IX–XII
motor components). Consumers must **not** conflate the **right
medullary** cranial nerve nuclei with the **right pontine** or
**right midbrain** cranial nerve nuclei.
**Boundary status (NOT the right spinal cord — that is a
separate container):** **Boundary case — the right cranial nerve
nuclei container is NOT the right spinal cord.** The **spinal
cord** (``.../spinal_cord/``) is a **separate container**
beginning at the **foramen magnum**. The **right cranial nerve
nuclei container** (here) contains **medullary** structures. The
**right spinal accessory nucleus** (CN XI, spinal part) is in the
**right cervical spinal cord**, **not** in the medulla — only the
**cranial part** of CN XI is associated with the **right nucleus
ambiguus**. Consumers must **not** conflate the **right
medullary** cranial nerve nuclei with the **right spinal cord**.

Overview
--------
The **right cranial nerve nuclei container** is the **right
medullary motor cranial nerve nuclear column** — the **CN IX–XII
motor nuclei** of the **right medulla oblongata**. It is the
**right** side of the **cranial_nerve_nuclei** bilateral
container, and it is a **container** (not a leaf) with **four leaf
children** (the four motor nuclei).

**The right cranial nerve nuclei container is a CONTAINER of four
nuclei, NOT a single nucleus.** The four **right** nuclei are:

*   **Right dorsal motor nucleus of vagus** (CN X) — **general
    visceral efferent** (parasympathetic) — supplies the **right
    thoracic and abdominal viscera** (heart, lungs, GI tract).

*   **Right hypoglossal nucleus** (CN XII) — **general somatic
    efferent** (tongue motor) — supplies the **right intrinsic and
    extrinsic tongue muscles**.

*   **Right inferior salivatory nucleus** (CN IX) — **general
    visceral efferent** (parasympathetic) — supplies the **right
    parotid gland**.

*   **Right nucleus ambiguus** (CN IX/X/XI) — **special visceral
    efferent** (branchial motor) — supplies the **right pharynx**,
    **larynx**, and **upper esophagus** (striated muscle).

**The right cranial nerve nuclei container is MOTOR, NOT
sensory.** The **right sensory** cranial nerve nuclei of the
medulla — the **right solitary nucleus** (visceral afferent) and
the **right spinal trigeminal nucleus** (facial pain/temperature)
— are **NOT** in this container. The **right solitary nucleus** is
wired under ``.../solitary_nucleus/right/``; the **right spinal
trigeminal nucleus** is not wired under
``cranial_nerve_nuclei.right``.

**The right cranial nerve nuclei container is MEDULLARY, NOT
pontine or midbrain.** The **right pontine** cranial nerve nuclei
(V, VI, VII, VIII) and the **right midbrain** cranial nerve
nuclei (III, IV) are wired under their respective containers. The
**right cranial nerve nuclei container** (here) contains **only**
the **right medullary** cranial nerve nuclei.

**The right cranial nerve nuclei container is one side of the
bilateral parent container.** The **parent**
(``.../cranial_nerve_nuclei/``) contains **both** the ``left``
and ``right`` sides; the **right** container (here) contains
**only the right side**.

Structural Children (Four Leaves)
---------------------------------
The right cranial nerve nuclei container has **four structural
children**, each a **leaf**:

*   ``dorsal_motor_nucleus_vagus`` — **right dorsal motor nucleus
    of vagus** (CN X) — general visceral efferent
    (parasympathetic).

*   ``hypoglossal_nucleus`` — **right hypoglossal nucleus** (CN
    XII) — general somatic efferent (tongue motor).

*   ``inferior_salivatory_nucleus`` — **right inferior salivatory
    nucleus** (CN IX) — general visceral efferent
    (parasympathetic to parotid).

*   ``nucleus_ambiguus`` — **right nucleus ambiguus** (CN IX/X/XI)
    — special visceral efferent (branchial motor).

**Each child is a leaf.** The four nucleus modules are **single
structures** — they have **no structural children** of their own.
Consumers that need **nucleus-level** resolution descend into one
of the four leaves; consumers that need **side-level** resolution
use this container as a whole; consumers that need **bilateral**
resolution iterate over both ``left`` and ``right``.

The Right Cranial Nerve Nuclei / Left Cranial Nerve Nuclei Boundary
-------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right cranial nerve nuclei container** (this module) — the
    cranial nerve nuclei of the **right** medulla.

*   **Left cranial nerve nuclei container**
    (``.../cranial_nerve_nuclei/left/``) — the cranial nerve
    nuclei of the **left** medulla.

**The two are the SIDES of the bilateral cranial_nerve_nuclei
container.** They are **structurally symmetric mirror pairs** —
same four leaf nuclei, same cytoarchitecture, same projections
(ipsilateral to their peripheral targets), same functions.
Consumers must **not** conflate the right container with the left
— resolve the left side via ``cranial_nerve_nuclei.left``.

The Right Cranial Nerve Nuclei / Right Solitary Nucleus Boundary
----------------------------------------------------------------
This is the **motor / sensory** boundary:

*   **Right cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei (right dorsal motor vagus, right
    hypoglossal, right inferior salivatory, right nucleus
    ambiguus).

*   **Right solitary nucleus** (``.../solitary_nucleus/right/``) —
    the **VISCERAL AFFERENT** relay (taste, baroreceptor,
    chemoreceptor, gastrointestinal).

**The right solitary nucleus is NOT in this container.** It is the
**sensory** counterpart to the **motor** right cranial nerve
nuclei. Consumers must **not** conflate the **right cranial nerve
nuclei container** with the **right solitary nucleus** — the
**container** is **motor**; the **solitary nucleus** is
**sensory**.

The Right Cranial Nerve Nuclei / Right Spinal Trigeminal Nucleus Boundary
-------------------------------------------------------------------------
This is the **facial-pain / motor** boundary:

*   **Right cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei.

*   **Right spinal trigeminal nucleus** — the **FACIAL
    PAIN/TEMPERATURE** sensory relay (CN V).

**The right spinal trigeminal nucleus is NOT in this container.**
It is a **sensory** nucleus, not a **motor** nucleus.

The Right Cranial Nerve Nuclei / Right RVLM, Right CVLM, Right Arcuate Nucleus Boundary
---------------------------------------------------------------------------------------
This is the **motor / autonomic** boundary:

*   **Right cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``) —
    the **right sympathetic premotor** center.

*   **Right CVLM** (``.../caudal_ventrolateral_medulla/right/``) —
    the **right sympathoinhibitory** relay.

*   **Right arcuate nucleus** (``.../arcuate_nucleus/right/``) — a
    **right ventral-surface chemosensory** nucleus.

**The right RVLM, right CVLM, and right arcuate nucleus are NOT in
this container.** They are **autonomic / chemosensory**
structures, not **cranial nerve motor nuclei**.

The Right Cranial Nerve Nuclei / Right Pontine and Right Midbrain Cranial Nerve Nuclei Boundary
----------------------------------------------------------------------------------------------
This is the **rostrocaudal** boundary:

*   **Right cranial nerve nuclei container** (this module) — the
    **MEDULLARY** cranial nerve nuclei (IX–XII motor components).

*   **Right pontine** cranial nerve nuclei
    (``.../metencephalon/pons/cranial_nerve_nuclei/right/``) — the
    **right pontine** cranial nerve nuclei (V, VI, VII, VIII).

*   **Right midbrain** cranial nerve nuclei
    (``.../midbrain/cranial_nerve_nuclei/right/``) — the **right
    midbrain** cranial nerve nuclei (III, IV, V mesencephalic).

**The right cranial nerve nuclei container is MEDULLARY, NOT
pontine or midbrain.** Consumers must **not** conflate the
**right medullary** cranial nerve nuclei with the **right
pontine** or **right midbrain** cranial nerve nuclei.

The Right Cranial Nerve Nuclei / Right Olivary Body and Right Medullary Pyramid Boundary
---------------------------------------------------------------------------------------
This is the **nucleus / relay-and-tract** boundary:

*   **Right cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei.

*   **Right olivary body** (``.../olivary_body/right/``) — the
    **right inferior olivary nucleus** (right cerebellar climbing
    fibers).

*   **Right medullary pyramid** (``.../medullary_pyramid/right/``)
    — the **right corticospinal / corticobulbar tract**.

**The right olivary body and right medullary pyramid are NOT in
this container.** They are a **cerebellar relay** and a
**white-matter tract**, not **cranial nerve motor nuclei**.

The Right Cranial Nerve Nuclei / Right Spinal Cord Boundary
-----------------------------------------------------------
This is the **medulla / spinal cord** boundary:

*   **Right cranial nerve nuclei container** (this module) — the
    **MEDULLARY** cranial nerve nuclei.

*   **Spinal cord** (``.../spinal_cord/``) — a **separate
    container** beginning at the **foramen magnum**.

**The right cranial nerve nuclei are MEDULLARY, NOT spinal.** The
**right spinal accessory nucleus** (CN XI, spinal part) is in the
**right cervical spinal cord**, not in the medulla — only the
**cranial part** of CN XI is associated with the **right nucleus
ambiguus**.

Function in the Human Brain
---------------------------
The right cranial nerve nuclei container's functions are the
**right CN IX–XII motor functions** — **NOT autonomic premotor**
and **NOT respiratory rhythm**:

*   **Right parasympathetic outflow (right dorsal motor nucleus of
    vagus, right inferior salivatory nucleus):** The **right
    dorsal motor nucleus of vagus** (CN X) supplies
    **parasympathetic** fibers to the **right heart**, **right
    lungs**, and **gastrointestinal tract**; the **right inferior
    salivatory nucleus** (CN IX) supplies **parasympathetic**
    fibers to the **right parotid gland**.

*   **Right tongue motor (right hypoglossal nucleus):** The
    **right hypoglossal nucleus** (CN XII) supplies the **right
    intrinsic and extrinsic tongue muscles** — critical for
    **speech**, **swallowing**, and **mastication**.

*   **Right branchial motor (right nucleus ambiguus):** The
    **right nucleus ambiguus** (CN IX/X/XI) supplies the
    **striated muscles** of the **right pharynx**, **right
    larynx**, and **right upper esophagus** — critical for
    **swallowing**, **vocalization**, and **airway protection**.

*   **NOT autonomic premotor:** The **autonomic premotor**
    function is the **right RVLM** (sympathetic) and the **right
    NTS** / **right dorsal motor nucleus of vagus** circuit
    (parasympathetic) — **NOT** the right cranial nerve nuclei
    container as a whole. The **right dorsal motor nucleus of
    vagus** is a **parasympathetic preganglionic** nucleus, but
    the **right sympathetic premotor** center is the **right
    RVLM**.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the right cranial nerve nuclei container.

**The unifying theme:** the right cranial nerve nuclei container
is the **right medullary motor cranial nerve column** — the
**right CN IX–XII motor nuclei** (parasympathetic, tongue motor,
branchial motor) wired as a **container** with **four leaf
nuclei**.

Associated Disorders
--------------------
The right cranial nerve nuclei container is the **substrate** for
a set of **well-defined clinical syndromes** — its clinical
relevance is **direct**, via the four right nuclei it contains:

*   **Right bulbar palsy (via the four nuclei):** Dysfunction of
    the **right cranial nerve nuclei IX–XII** — **dysphagia**,
    **dysarthria**, **right tongue weakness** (right hypoglossal),
    **right palatal weakness** (right nucleus ambiguus), **right
    hoarseness** (right nucleus ambiguus), and **right parotid
    dryness** (right inferior salivatory). The **right cranial
    nerve nuclei** are the **direct substrate** of right bulbar
    palsy.

*   **Right Wallenberg syndrome (Lateral Medullary Syndrome / PICA
    syndrome — via the right nucleus ambiguus):** Infarction of
    the **right lateral medulla** — **right dysphagia /
    dysarthria / hoarseness** (right nucleus ambiguus), **right
    ipsilateral facial thermoalgesic loss** (right spinal
    trigeminal nucleus/tract — **NOT** in this container), **left
    contralateral body thermoalgesic loss** (right spinothalamic
    tract — **NOT** in this container). The **right nucleus
    ambiguus** (in this container) is the **right cranial nerve
    motor** component of right Wallenberg syndrome.

*   **Right hypoglossal nerve palsy (via the right hypoglossal
    nucleus):** **Right tongue weakness** and **rightward
    deviation** — from lesions in the **right hypoglossal
    nucleus** or its **nerve**. The **right hypoglossal nucleus**
    is the **direct substrate**.

*   **Right vagal nerve dysfunction (via the right dorsal motor
    nucleus of vagus):** **Right autonomic** symptoms —
    **bradycardia**, **gastrointestinal dysmotility**, **nausea**
    — from lesions in the **right dorsal motor nucleus of vagus**
    or its **nerve**.

*   **Right parotid dryness (via the right inferior salivatory
    nucleus):** **Reduced right parotid salivation** — from
    lesions in the **right inferior salivatory nucleus** or its
    **nerve** (CN IX).

*   **Bulbar-onset ALS (via the four nuclei):** **Amyotrophic
    lateral sclerosis** with **bulbar onset** — **dysarthria**,
    **dysphagia**, **tongue atrophy/fasciculations** — from
    **degeneration** of the **right cranial nerve motor nuclei**
    (especially **right hypoglossal nucleus** and **right nucleus
    ambiguus**). The **right cranial nerve nuclei container** is
    the **direct substrate**.

*   **Progressive bulbar palsy (via the four nuclei):** A
    **lower motor neuron** disorder of the **right cranial nerve
    motor nuclei** — **dysarthria**, **dysphagia**, **tongue
    fasciculations**.

**What is NOT here:** The right cranial nerve nuclei container is
**not** the substrate for **central hypoventilation** (VRG /
pre-Bötzinger complex), **neurogenic hypertension** (right RVLM /
right NTS / right CVLM), or **right Wallenberg syndrome's sensory
deficits** (right spinal trigeminal nucleus, right spinothalamic
tract — **NOT** in this container). Its clinical relevance is the
**right cranial nerve motor** functions listed above.

Lateralization Notes
--------------------
This is the **right** cranial nerve nuclei container. The
cranial_nerve_nuclei is a **bilateral container** whose two sides
are **structurally symmetric mirror pairs** — and it carries
**NO warning**:

*   **Bilateral Symmetry:** The **right** and **left** cranial
    nerve nuclei are **structurally symmetric** — they are
    **mirror pairs** with the **same** four leaf nuclei, **same**
    cytoarchitecture, **same** projections, and **same**
    functions. The **right** nuclei innervate the **right** side
    of the body; the **left** nuclei innervate the **left** side.

*   **Ipsilateral Innervation (with exceptions):** The **right
    hypoglossal nucleus** innervates the **right** tongue (except
    **genioglossus**, which has **contralateral corticobulbar
    input**); the **right nucleus ambiguus** innervates the
    **right** pharynx/larynx; the **right dorsal motor nucleus of
    vagus** and **right inferior salivatory nucleus** project
    **ipsilaterally** to their peripheral targets.

*   **NO Lateralization Warning:** The cranial_nerve_nuclei has
    **no known functional lateralization** in humans beyond the
    **ipsilateral** innervation pattern. Consumers must **not**
    import a **lateralization warning** into the right cranial
    nerve nuclei container — the **right** and **left** sides are
    **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right cranial
    nerve nuclei container is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the right cranial nerve nuclei container.

*   **NO Fear-Output Warning:** The right cranial nerve nuclei
    container is **not** a fear-output structure — it is a
    **right medullary motor cranial nerve column**. Consumers
    must **not** conflate it with the **central nucleus** or with
    the **amygdala**.

**A consumer that assumes "right cranial nerve nuclei = left
cranial nerve nuclei" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent**. The
cranial_nerve_nuclei is a **strict-mirror pair with NO warning** —
**no SLEA warning**, **no fear-output warning**, and **no
lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right cranial nerve nuclei
    container is a **container** — it does **not** import from
    ``.../left/`` or any other left-side module. Bilateral
    relationships are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../solitary_nucleus/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../arcuate_nucleus/``, ``.../olivary_body/``,
    ``.../medullary_pyramid/``, ``.../ventral_respiratory_group/``,
    ``.../metencephalon/``, ``.../midbrain/``, or
    ``.../spinal_cord/``. The right cranial nerve nuclei
    container's relationships to the right solitary nucleus,
    right RVLM, right CVLM, right arcuate nucleus, right olivary
    body, right medullary pyramid, right pontine cranial nerve
    nuclei, right midbrain cranial nerve nuclei, and spinal cord
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with four leaf children.** The structural
    children are the four nuclei — each a **leaf**. Consumers
    **should** descend into them for **nucleus-level** resolution.
*   **NOT the left cranial nerve nuclei container.** The left
    container is a **separate module** under
    ``.../cranial_nerve_nuclei/left/``. Consumers must **not**
    conflate the right container with the left.
*   **NOT the parent cranial_nerve_nuclei container.** The parent
    is the **unpaired bilateral container**; the **right** module
    is **one side** of it.
*   **MOTOR, NOT sensory.** The **right solitary nucleus** and the
    **right spinal trigeminal nucleus** are **NOT** in this
    container.
*   **MEDULLARY, NOT pontine or midbrain.** The **right pontine**
    and **right midbrain** cranial nerve nuclei are wired under
    their respective containers.
*   **NOT the right RVLM / right CVLM / right arcuate nucleus.**
    Those are **autonomic / chemosensory** structures.
*   **NOT the right olivary body or right medullary pyramid.**
    Those are a **cerebellar relay** and a **white-matter
    tract**.
*   **No ``AREA_PATHS`` hop.** The right cranial nerve nuclei
    container is a **local container** — it is not cross-listed
    under another brainparts path.
*   **No nested cross-listing.** The right cranial nerve nuclei
    container has no nested dual-framing module. It is a
    **container** with **four leaf children**.
*   **Structural parity with the left cranial nerve nuclei
    container — strict mirror with NO warning.** The right and
    left containers are **structurally identical** — same four
    leaf children, same **parasympathetic / tongue-motor /
    branchial-motor** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "cranial_nerve_nuclei.right"
    )

**Do not** expect the four nuclei to be wired directly under
``cranial_nerve_nuclei``. The **left** and **right** containers
are **intermediate** — the four nuclei are leaf children of those
containers. Resolve them via
``cranial_nerve_nuclei.right.<nucleus>``.

**Do not** assume the right cranial nerve nuclei container is the
**left cranial nerve nuclei container**. The left container is
the **separate module** at ``.../cranial_nerve_nuclei/left/``.

**Do not** assume the right cranial nerve nuclei container is the
**right solitary nucleus** or the **right spinal trigeminal
nucleus**. Those are **sensory** nuclei — **NOT** in this
container.

**Do not** assume the right cranial nerve nuclei container is the
**right RVLM**, the **right CVLM**, or the **right arcuate
nucleus**. Those are **autonomic / chemosensory** structures.

**Do not** assume the right cranial nerve nuclei container is the
**right olivary body** or the **right medullary pyramid**. Those
are a **cerebellar relay** and a **white-matter tract**.

**Do not** assume the right cranial nerve nuclei container is the
**right pontine** or **right midbrain** cranial nerve nuclei.
Those are wired under their respective containers.

Iterating the right cranial nerve nuclei container's structural
children (recommended consumer pattern)::

    RIGHT_CRANIAL_NERVE_NUCLEI_CHILDREN = (
        "dorsal_motor_nucleus_vagus",
        "hypoglossal_nucleus",
        "inferior_salivatory_nucleus",
        "nucleus_ambiguus",
    )
    # Each child is a leaf module representing the right side of
    # one of the four motor cranial nerve nuclei.

Reaching the four right nuclei (recommended consumer pattern)::

    # The four right nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.dorsal_motor_nucleus_vagus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.hypoglossal_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.inferior_salivatory_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.nucleus_ambiguus
    #
    # Each is a leaf module representing the RIGHT side of that
    # nucleus.

Reaching the left cranial nerve nuclei container (recommended
consumer pattern — the contralateral container)::

    # The left cranial nerve nuclei container is the
    # CONTRALATERAL container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left
    #
    # The right and left containers are structurally symmetric
    # mirror pairs with the same four leaf nuclei.

Reaching the right solitary nucleus (recommended consumer pattern
— NOTE the DIFFERENT structure)::

    # The right solitary nucleus (NTS) is a SENSORY nucleus, NOT
    # a motor cranial nerve nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
    #
    # The right NTS is the VISCERAL AFFERENT relay — it is NOT in
    # the cranial_nerve_nuclei.right container.

Reaching the right RVLM, right CVLM, and right arcuate nucleus
(recommended consumer pattern — NOTE the DIFFERENT structures)::

    # The right RVLM, right CVLM, and right arcuate nucleus are
    # AUTONOMIC / CHEMOSENSORY structures, NOT cranial nerve motor
    # nuclei:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.right
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.right
    #
    # These are NOT in the cranial_nerve_nuclei.right container.

Reaching the right pontine and right midbrain cranial nerve
nuclei (recommended consumer pattern — NOTE the DIFFERENT
containers)::

    # The right pontine and right midbrain cranial nerve nuclei
    # are wired under their respective containers:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right
    #   hindbrain.midbrain.cranial_nerve_nuclei.right
    #
    # The cranial_nerve_nuclei.right container (here) is
    # MEDULLARY — it contains ONLY the right medullary cranial
    # nerve nuclei (IX–XII).

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        for nucleus in RIGHT_CRANIAL_NERVE_NUCLEI_CHILDREN:
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"cranial_nerve_nuclei.{side}.{nucleus}"
            )
            # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Medullary cranial nerve nuclei IX–XII; hypoglossal, dorsal
    motor vagus, inferior salivatory, nucleus ambiguus.)
*   **Cranial nerve nuclei cytoarchitecture:** Paxinos, G.,
    Huang, X.-F. (2013). *The Behaving Human Brain: A
    Cytoarchitectural Atlas.* (Medullary cranial nerve nuclei;
    motor columns.)
*   **Hypoglossal nucleus:** Lowe, A.A. (1980). "The neural
    regulation of tongue movement." *Progress in Neurobiology*
    14:273–349. (Hypoglossal nucleus; tongue motor control;
    corticobulbar input; genioglossus contralateral
    corticobulbar innervation.)
*   **Dorsal motor nucleus of vagus:** Hopkins, D.A., Armour,
    J.A. (1984). "Localization of sympathetic postganglionic and
    parasympathetic preganglionic neurons which innervate
    different regions of the heart." *Journal of Comparative
    Neurology* 240:65–77. (Dorsal motor nucleus of vagus;
    cardiac parasympathetic outflow.)
*   **Nucleus ambiguus:** Bieger, D., Hopkins, D.A. (1987).
    "Viscerotopic representation of the upper alimentary tract in
    the medulla oblongata and nucleus ambiguus." *Journal of
    Comparative Neurology* 262:546–562. (Nucleus ambiguus;
    branchial motor column; pharynx/larynx.)
*   **Inferior salivatory nucleus:** Contreras, R.J., Gomez, M.M.,
    Norgren, R. (1980). "Central origins of cranial nerve
    parasympathetic neurons in the rat." *Journal of Comparative
    Neurology* 190:373–394. (Inferior salivatory nucleus; parotid
    parasympathetic outflow.)
*   **Bulbar palsy:** Hughes, T.A.T., Wiles, C.M. (1996).
    "Neurogenic dysphagia: the role of clinical and investigative
    methods." *Journal of Neurology, Neurosurgery, and Psychiatry*
    60:475–479. (Bulbar palsy; cranial nerve IX–XII dysfunction.)
*   **Wallenberg syndrome:** Sacco, R.L., et al. (1993). "Lateral
    medullary infarction: clinical and MRI correlation." *Stroke*
    24:1981–1987. (Wallenberg syndrome; nucleus ambiguus
    involvement — the motor component of the syndrome.)
*   **Bulbar-onset ALS:** Kiernan, M.C., et al. (2011).
    "Amyotrophic lateral sclerosis." *The Lancet* 377:942–955.
    (Bulbar-onset ALS; cranial nerve motor nucleus degeneration.)
*   **Progressive bulbar palsy:** Norris, F.H., et al. (1993).
    "Onset, natural history and outcome in idiopathic adult motor
    neuron disease." *Journal of the Neurological Sciences*
    118:48–55. (Progressive bulbar palsy; lower motor neuron
    degeneration of the cranial nerve nuclei.)
*   **Solitary nucleus (contrast — NOT in this container):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS as the
    visceral afferent relay — SENSORY, not motor.)
*   **Spinal trigeminal nucleus (contrast — NOT in this
    container):** Usunoff, K.G., et al. (1997). "The trigeminal
    system." *Advances in Anatomy, Embryology, and Cell Biology*
    137:1–112. (Spinal trigeminal nucleus — SENSORY, not motor.)
*   **Pontine cranial nerve nuclei (contrast — in the
    metencephalon):** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Trigeminal motor,
    abducens, facial, superior salivatory, vestibulocochlear
    nuclei — PONTINE, not medullary.)
*   **Midbrain cranial nerve nuclei (contrast — in the
    midbrain):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Oculomotor,
    Edinger-Westphal, trochlear, mesencephalic trigeminal nuclei
    — MIDBRAIN, not medullary.)
*   NeuroNames — Cranial nerve nuclei (medulla); FMA — Cranial
    nerve nuclei of medulla oblongata.
"""