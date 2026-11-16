"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left
===============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── cranial_nerve_nuclei
                └── left   <-- THIS MODULE
                    ├── dorsal_motor_nucleus_vagus
                    ├── hypoglossal_nucleus
                    ├── inferior_salivatory_nucleus
                    └── nucleus_ambiguus

**Primary synonym:** Left medullary cranial nerve nuclei; left
cranial nerve nuclei IX–XII; left bulbar motor nuclei; left
medullary motor column.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter container** — the **left-side motor
cranial nerve nuclei** of the **medulla oblongata**, comprising
the **left general somatic efferent** (hypoglossal — XII), **left
general visceral efferent / parasympathetic** (dorsal motor
nucleus of vagus — X; inferior salivatory nucleus — IX), and
**left special visceral efferent / branchial motor** (nucleus
ambiguus — IX/X/XI) columns.
**Part of:** The **cranial_nerve_nuclei** bilateral container —
which is part of the **medulla oblongata** — the **caudal
brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../cranial_nerve_nuclei/`` → **direct
child** of the cranial_nerve_nuclei container. The **left** cranial
nerve nuclei container is one of the **two** structural children
of the container (the other is ``right``).
**Structural children:** **Four —** each a **leaf** representing
the **left** side of one of the four motor nuclei:
1. ``dorsal_motor_nucleus_vagus`` — **CN X** — general visceral
   efferent (parasympathetic).
2. ``hypoglossal_nucleus`` — **CN XII** — general somatic efferent
   (tongue motor).
3. ``inferior_salivatory_nucleus`` — **CN IX** — general visceral
   efferent (parasympathetic to parotid).
4. ``nucleus_ambiguus`` — **CN IX/X/XI** — special visceral
   efferent (branchial motor to pharynx/larynx).
**Boundary status (NOT the right cranial nerve nuclei container —
the contralateral container):** **Boundary case — the left
cranial nerve nuclei container is NOT the right cranial nerve
nuclei container.** The **right cranial nerve nuclei container**
(``.../cranial_nerve_nuclei/right/``) is the **contralateral
container** — the cranial nerve nuclei of the **right** medulla.
**They are DIFFERENT CONTAINERS** — the ``left`` and ``right``
modules are the two sides of the **bilateral parent container**.
Consumers must **not** conflate the **left** container with the
**right** container — resolve the right side via
``cranial_nerve_nuclei.right``.
**Boundary status (NOT the parent cranial_nerve_nuclei container
— a SIDE of it):** **Boundary case — the left cranial nerve
nuclei container is NOT the parent cranial_nerve_nuclei
container.** The **parent** (``.../cranial_nerve_nuclei/``) is
the **unpaired bilateral container** — it contains **both** the
``left`` and ``right`` sides. The **left** container (here) is
**one side** of that parent. Consumers must **not** conflate the
**left container** with the **parent container** — the parent
contains **both sides**; the left container contains **only the
left side**.
**Boundary status (NOT a single nucleus — a CONTAINER of four
nuclei):** **Boundary case — the left cranial nerve nuclei
container is a CONTAINER, not a single nucleus.** It contains
**four distinct leaf nuclei** — the **left dorsal motor nucleus
of vagus**, the **left hypoglossal nucleus**, the **left inferior
salivatory nucleus**, and the **left nucleus ambiguus**. Each is
a **separate structure** with **different functions**
(parasympathetic, somatic motor, parasympathetic, branchial
motor). Consumers must **not** treat the **left** container as a
single uniform nucleus — it is a **container** of **four
functionally distinct nuclei**.
**Boundary status (NOT the left solitary nucleus — the NTS is
the VISCERAL AFFERENT relay, not a motor nucleus):** **Boundary
case — the left cranial nerve nuclei container is NOT the left
solitary nucleus.** The **left solitary nucleus** (NTS)
(``.../solitary_nucleus/left/``) is the **left visceral afferent
relay** — it receives **taste**, **baroreceptor**,
**chemoreceptor**, and **gastrointestinal** afferents from **CN
VII, IX, and X**. It is **NOT a motor nucleus** — it is a
**sensory** nucleus. The **left cranial nerve nuclei container**
(here) contains the **MOTOR** cranial nerve nuclei of the left
medulla. The **left NTS** is **anatomically adjacent** but is
**NOT** in this container. Consumers must **not** expect to find
the **left solitary nucleus** under ``cranial_nerve_nuclei.left``
— resolve it via ``.../solitary_nucleus/left/``.
**Boundary status (NOT the left spinal trigeminal nucleus — a
sensory nucleus, not a motor nucleus):** **Boundary case — the
left cranial nerve nuclei container is NOT the left spinal
trigeminal nucleus.** The **left spinal trigeminal nucleus** (and
its tract) is the **left facial pain/temperature** sensory relay
— it receives **CN V** afferents from the **left** face and is
**NOT** a motor nucleus. It is **not** wired under
``cranial_nerve_nuclei.left`` in this tree. Consumers must **not**
expect to find the **left spinal trigeminal nucleus** here.
**Boundary status (NOT the left reticular formation — a
cross-container system):** **Boundary case — the left cranial
nerve nuclei container is NOT the left reticular formation.** The
**reticular formation** is a **cross-container system** — its
medullary components are wired under
``.../paramedian_reticular_nucleus/`` and
``.../respiratory_center/gigantocellular_reticular_nucleus/``,
**not** under ``cranial_nerve_nuclei``. The **left cranial nerve
nuclei container** (here) contains **motor cranial nerve nuclei**
— **not** the reticular formation. Consumers must **not**
conflate the two.
**Boundary status (NOT the left RVLM / left CVLM / left arcuate
nucleus — those are autonomic / chemosensory):** **Boundary case
— the left cranial nerve nuclei container is NOT the left
ventrolateral medullary structures.** The **left RVLM**
(``.../rostral_ventrolateral_medulla/left/``) is the **left
sympathetic premotor** center; the **left CVLM**
(``.../caudal_ventrolateral_medulla/left/``) is the **left
sympathoinhibitory** relay; the **left arcuate nucleus**
(``.../arcuate_nucleus/left/``) is a **left ventral-surface
chemosensory** nucleus. These are **NOT cranial nerve motor
nuclei** — they are **autonomic / chemosensory** structures.
Consumers must **not** conflate the **left cranial nerve nuclei
container** with the **left ventrolateral medullary structures**.
**Boundary status (NOT the left olivary body or the left
medullary pyramid — those are different structures):** **Boundary
case — the left cranial nerve nuclei container is NOT the left
olivary body or the left medullary pyramid.** The **left olivary
body** (``.../olivary_body/left/``) contains the **left inferior
olivary nucleus** (left cerebellar climbing fibers); the **left
medullary pyramid** (``.../medullary_pyramid/left/``) is the
**left corticospinal / corticobulbar tract**. These are **NOT**
cranial nerve nuclei. Consumers must **not** conflate the **left
cranial nerve nuclei container** with these structures.
**Boundary status (NOT the left pontine or left midbrain cranial
nerve nuclei — those are in different containers):** **Boundary
case — the left cranial nerve nuclei container is NOT the left
pontine or left midbrain cranial nerve nuclei.** The **left
pontine** cranial nerve nuclei (V, VI, VII, VIII) are wired under
``.../metencephalon/pons/cranial_nerve_nuclei/left/``; the **left
midbrain** cranial nerve nuclei (III, IV, V mesencephalic) are
wired under ``.../midbrain/cranial_nerve_nuclei/left/``. The
**left cranial nerve nuclei container** (here) is **MEDULLARY** —
it contains **only** the **left medullary** cranial nerve nuclei
(IX–XII motor components). Consumers must **not** conflate the
**left medullary** cranial nerve nuclei with the **left pontine**
or **left midbrain** cranial nerve nuclei.
**Boundary status (NOT the left spinal cord — that is a separate
container):** **Boundary case — the left cranial nerve nuclei
container is NOT the left spinal cord.** The **spinal cord**
(``.../spinal_cord/``) is a **separate container** beginning at
the **foramen magnum**. The **left cranial nerve nuclei
container** (here) contains **medullary** structures. The **left
spinal accessory nucleus** (CN XI, spinal part) is in the **left
cervical spinal cord**, **not** in the medulla — only the
**cranial part** of CN XI is associated with the **left nucleus
ambiguus**. Consumers must **not** conflate the **left medullary**
cranial nerve nuclei with the **left spinal cord**.

Overview
--------
The **left cranial nerve nuclei container** is the **left medullary
motor cranial nerve nuclear column** — the **CN IX–XII motor
nuclei** of the **left medulla oblongata**. It is the **left**
side of the **cranial_nerve_nuclei** bilateral container, and it
is a **container** (not a leaf) with **four leaf children** (the
four motor nuclei).

**The left cranial nerve nuclei container is a CONTAINER of four
nuclei, NOT a single nucleus.** The four **left** nuclei are:

*   **Left dorsal motor nucleus of vagus** (CN X) — **general
    visceral efferent** (parasympathetic) — supplies the **left
    thoracic and abdominal viscera** (heart, lungs, GI tract).

*   **Left hypoglossal nucleus** (CN XII) — **general somatic
    efferent** (tongue motor) — supplies the **left intrinsic and
    extrinsic tongue muscles**.

*   **Left inferior salivatory nucleus** (CN IX) — **general
    visceral efferent** (parasympathetic) — supplies the **left
    parotid gland**.

*   **Left nucleus ambiguus** (CN IX/X/XI) — **special visceral
    efferent** (branchial motor) — supplies the **left pharynx**,
    **larynx**, and **upper esophagus** (striated muscle).

**The left cranial nerve nuclei container is MOTOR, NOT
sensory.** The **left sensory** cranial nerve nuclei of the
medulla — the **left solitary nucleus** (visceral afferent) and
the **left spinal trigeminal nucleus** (facial pain/temperature)
— are **NOT** in this container. The **left solitary nucleus** is
wired under ``.../solitary_nucleus/left/``; the **left spinal
trigeminal nucleus** is not wired under
``cranial_nerve_nuclei.left``.

**The left cranial nerve nuclei container is MEDULLARY, NOT
pontine or midbrain.** The **left pontine** cranial nerve nuclei
(V, VI, VII, VIII) and the **left midbrain** cranial nerve nuclei
(III, IV) are wired under their respective containers. The
**left cranial nerve nuclei container** (here) contains **only**
the **left medullary** cranial nerve nuclei.

**The left cranial nerve nuclei container is one side of the
bilateral parent container.** The **parent**
(``.../cranial_nerve_nuclei/``) contains **both** the ``left``
and ``right`` sides; the **left** container (here) contains
**only the left side**.

Structural Children (Four Leaves)
---------------------------------
The left cranial nerve nuclei container has **four structural
children**, each a **leaf**:

*   ``dorsal_motor_nucleus_vagus`` — **left dorsal motor nucleus
    of vagus** (CN X) — general visceral efferent
    (parasympathetic).

*   ``hypoglossal_nucleus`` — **left hypoglossal nucleus** (CN
    XII) — general somatic efferent (tongue motor).

*   ``inferior_salivatory_nucleus`` — **left inferior salivatory
    nucleus** (CN IX) — general visceral efferent
    (parasympathetic to parotid).

*   ``nucleus_ambiguus`` — **left nucleus ambiguus** (CN IX/X/XI)
    — special visceral efferent (branchial motor).

**Each child is a leaf.** The four nucleus modules are **single
structures** — they have **no structural children** of their own.
Consumers that need **nucleus-level** resolution descend into one
of the four leaves; consumers that need **side-level** resolution
use this container as a whole; consumers that need **bilateral**
resolution iterate over both ``left`` and ``right``.

The Left Cranial Nerve Nuclei / Right Cranial Nerve Nuclei Boundary
-------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left cranial nerve nuclei container** (this module) — the
    cranial nerve nuclei of the **left** medulla.

*   **Right cranial nerve nuclei container**
    (``.../cranial_nerve_nuclei/right/``) — the cranial nerve
    nuclei of the **right** medulla.

**The two are the SIDES of the bilateral cranial_nerve_nuclei
container.** They are **structurally symmetric mirror pairs** —
same four leaf nuclei, same cytoarchitecture, same projections
(ipsilateral to their peripheral targets), same functions.
Consumers must **not** conflate the left container with the right
— resolve the right side via ``cranial_nerve_nuclei.right``.

The Left Cranial Nerve Nuclei / Left Solitary Nucleus Boundary
--------------------------------------------------------------
This is the **motor / sensory** boundary:

*   **Left cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei (left dorsal motor vagus, left
    hypoglossal, left inferior salivatory, left nucleus
    ambiguus).

*   **Left solitary nucleus** (``.../solitary_nucleus/left/``) —
    the **VISCERAL AFFERENT** relay (taste, baroreceptor,
    chemoreceptor, gastrointestinal).

**The left solitary nucleus is NOT in this container.** It is the
**sensory** counterpart to the **motor** left cranial nerve
nuclei. Consumers must **not** conflate the **left cranial nerve
nuclei container** with the **left solitary nucleus** — the
**container** is **motor**; the **solitary nucleus** is
**sensory**.

The Left Cranial Nerve Nuclei / Left Spinal Trigeminal Nucleus Boundary
-----------------------------------------------------------------------
This is the **facial-pain / motor** boundary:

*   **Left cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei.

*   **Left spinal trigeminal nucleus** — the **FACIAL
    PAIN/TEMPERATURE** sensory relay (CN V).

**The left spinal trigeminal nucleus is NOT in this container.**
It is a **sensory** nucleus, not a **motor** nucleus.

The Left Cranial Nerve Nuclei / Left RVLM, Left CVLM, Left Arcuate Nucleus Boundary
-----------------------------------------------------------------------------------
This is the **motor / autonomic** boundary:

*   **Left cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``) —
    the **left sympathetic premotor** center.

*   **Left CVLM** (``.../caudal_ventrolateral_medulla/left/``) —
    the **left sympathoinhibitory** relay.

*   **Left arcuate nucleus** (``.../arcuate_nucleus/left/``) — a
    **left ventral-surface chemosensory** nucleus.

**The left RVLM, left CVLM, and left arcuate nucleus are NOT in
this container.** They are **autonomic / chemosensory**
structures, not **cranial nerve motor nuclei**.

The Left Cranial Nerve Nuclei / Left Pontine and Left Midbrain Cranial Nerve Nuclei Boundary
-------------------------------------------------------------------------------------------
This is the **rostrocaudal** boundary:

*   **Left cranial nerve nuclei container** (this module) — the
    **MEDULLARY** cranial nerve nuclei (IX–XII motor components).

*   **Left pontine** cranial nerve nuclei
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/``) — the
    **left pontine** cranial nerve nuclei (V, VI, VII, VIII).

*   **Left midbrain** cranial nerve nuclei
    (``.../midbrain/cranial_nerve_nuclei/left/``) — the **left
    midbrain** cranial nerve nuclei (III, IV, V mesencephalic).

**The left cranial nerve nuclei container is MEDULLARY, NOT
pontine or midbrain.** Consumers must **not** conflate the **left
medullary** cranial nerve nuclei with the **left pontine** or
**left midbrain** cranial nerve nuclei.

The Left Cranial Nerve Nuclei / Left Olivary Body and Left Medullary Pyramid Boundary
-------------------------------------------------------------------------------------
This is the **nucleus / relay-and-tract** boundary:

*   **Left cranial nerve nuclei container** (this module) — the
    **MOTOR** CN IX–XII nuclei.

*   **Left olivary body** (``.../olivary_body/left/``) — the
    **left inferior olivary nucleus** (left cerebellar climbing
    fibers).

*   **Left medullary pyramid** (``.../medullary_pyramid/left/``) —
    the **left corticospinal / corticobulbar tract**.

**The left olivary body and left medullary pyramid are NOT in
this container.** They are a **cerebellar relay** and a
**white-matter tract**, not **cranial nerve motor nuclei**.

The Left Cranial Nerve Nuclei / Left Spinal Cord Boundary
---------------------------------------------------------
This is the **medulla / spinal cord** boundary:

*   **Left cranial nerve nuclei container** (this module) — the
    **MEDULLARY** cranial nerve nuclei.

*   **Spinal cord** (``.../spinal_cord/``) — a **separate
    container** beginning at the **foramen magnum**.

**The left cranial nerve nuclei are MEDULLARY, NOT spinal.** The
**left spinal accessory nucleus** (CN XI, spinal part) is in the
**left cervical spinal cord**, not in the medulla — only the
**cranial part** of CN XI is associated with the **left nucleus
ambiguus**.

Function in the Human Brain
---------------------------
The left cranial nerve nuclei container's functions are the
**left CN IX–XII motor functions** — **NOT autonomic premotor**
and **NOT respiratory rhythm**:

*   **Left parasympathetic outflow (left dorsal motor nucleus of
    vagus, left inferior salivatory nucleus):** The **left
    dorsal motor nucleus of vagus** (CN X) supplies
    **parasympathetic** fibers to the **left heart**, **left
    lungs**, and **gastrointestinal tract**; the **left inferior
    salivatory nucleus** (CN IX) supplies **parasympathetic**
    fibers to the **left parotid gland**.

*   **Left tongue motor (left hypoglossal nucleus):** The **left
    hypoglossal nucleus** (CN XII) supplies the **left intrinsic
    and extrinsic tongue muscles** — critical for **speech**,
    **swallowing**, and **mastication**.

*   **Left branchial motor (left nucleus ambiguus):** The **left
    nucleus ambiguus** (CN IX/X/XI) supplies the **striated
    muscles** of the **left pharynx**, **left larynx**, and
    **left upper esophagus** — critical for **swallowing**,
    **vocalization**, and **airway protection**.

*   **NOT autonomic premotor:** The **autonomic premotor**
    function is the **left RVLM** (sympathetic) and the **left
    NTS** / **left dorsal motor nucleus of vagus** circuit
    (parasympathetic) — **NOT** the left cranial nerve nuclei
    container as a whole. The **left dorsal motor nucleus of
    vagus** is a **parasympathetic preganglionic** nucleus, but
    the **left sympathetic premotor** center is the **left
    RVLM**.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the left cranial nerve nuclei container.

**The unifying theme:** the left cranial nerve nuclei container is
the **left medullary motor cranial nerve column** — the **left CN
IX–XII motor nuclei** (parasympathetic, tongue motor, branchial
motor) wired as a **container** with **four leaf nuclei**.

Associated Disorders
--------------------
The left cranial nerve nuclei container is the **substrate** for a
set of **well-defined clinical syndromes** — its clinical
relevance is **direct**, via the four left nuclei it contains:

*   **Left bulbar palsy (via the four nuclei):** Dysfunction of
    the **left cranial nerve nuclei IX–XII** — **dysphagia**,
    **dysarthria**, **left tongue weakness** (left hypoglossal),
    **left palatal weakness** (left nucleus ambiguus), **left
    hoarseness** (left nucleus ambiguus), and **left parotid
    dryness** (left inferior salivatory). The **left cranial
    nerve nuclei** are the **direct substrate** of left bulbar
    palsy.

*   **Left Wallenberg syndrome (Lateral Medullary Syndrome / PICA
    syndrome — via the left nucleus ambiguus):** Infarction of the
    **left lateral medulla** — **left dysphagia / dysarthria /
    hoarseness** (left nucleus ambiguus), **left ipsilateral
    facial thermoalgesic loss** (left spinal trigeminal
    nucleus/tract — **NOT** in this container), **right
    contralateral body thermoalgesic loss** (left spinothalamic
    tract — **NOT** in this container). The **left nucleus
    ambiguus** (in this container) is the **left cranial nerve
    motor** component of left Wallenberg syndrome.

*   **Left hypoglossal nerve palsy (via the left hypoglossal
    nucleus):** **Left tongue weakness** and **leftward
    deviation** — from lesions in the **left hypoglossal
    nucleus** or its **nerve**. The **left hypoglossal nucleus**
    is the **direct substrate**.

*   **Left vagal nerve dysfunction (via the left dorsal motor
    nucleus of vagus):** **Left autonomic** symptoms —
    **bradycardia**, **gastrointestinal dysmotility**, **nausea**
    — from lesions in the **left dorsal motor nucleus of vagus**
    or its **nerve**.

*   **Left parotid dryness (via the left inferior salivatory
    nucleus):** **Reduced left parotid salivation** — from
    lesions in the **left inferior salivatory nucleus** or its
    **nerve** (CN IX).

*   **Bulbar-onset ALS (via the four nuclei):** **Amyotrophic
    lateral sclerosis** with **bulbar onset** — **dysarthria**,
    **dysphagia**, **tongue atrophy/fasciculations** — from
    **degeneration** of the **left cranial nerve motor nuclei**
    (especially **left hypoglossal nucleus** and **left nucleus
    ambiguus**). The **left cranial nerve nuclei container** is
    the **direct substrate**.

*   **Progressive bulbar palsy (via the four nuclei):** A
    **lower motor neuron** disorder of the **left cranial nerve
    motor nuclei** — **dysarthria**, **dysphagia**, **tongue
    fasciculations**.

**What is NOT here:** The left cranial nerve nuclei container is
**not** the substrate for **central hypoventilation** (VRG /
pre-Bötzinger complex), **neurogenic hypertension** (left RVLM /
left NTS / left CVLM), or **left Wallenberg syndrome's sensory
deficits** (left spinal trigeminal nucleus, left spinothalamic
tract — **NOT** in this container). Its clinical relevance is
the **left cranial nerve motor** functions listed above.

Lateralization Notes
--------------------
This is the **left** cranial nerve nuclei container. The
cranial_nerve_nuclei is a **bilateral container** whose two sides
are **structurally symmetric mirror pairs** — and it carries
**NO warning**:

*   **Bilateral Symmetry:** The **left** and **right** cranial
    nerve nuclei are **structurally symmetric** — they are
    **mirror pairs** with the **same** four leaf nuclei, **same**
    cytoarchitecture, **same** projections, and **same**
    functions. The **left** nuclei innervate the **left** side
    of the body; the **right** nuclei innervate the **right**
    side.

*   **Ipsilateral Innervation (with exceptions):** The **left
    hypoglossal nucleus** innervates the **left** tongue (except
    **genioglossus**, which has **contralateral corticobulbar
    input**); the **left nucleus ambiguus** innervates the
    **left** pharynx/larynx; the **left dorsal motor nucleus of
    vagus** and **left inferior salivatory nucleus** project
    **ipsilaterally** to their peripheral targets.

*   **NO Lateralization Warning:** The cranial_nerve_nuclei has
    **no known functional lateralization** in humans beyond the
    **ipsilateral** innervation pattern. Consumers must **not**
    import a **lateralization warning** into the left cranial
    nerve nuclei container — the **left** and **right** sides
    are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left cranial
    nerve nuclei container is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the left cranial nerve nuclei
    container.

*   **NO Fear-Output Warning:** The left cranial nerve nuclei
    container is **not** a fear-output structure — it is a
    **left medullary motor cranial nerve column**. Consumers must
    **not** conflate it with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "left cranial nerve nuclei = right
cranial nerve nuclei" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent**. The
cranial_nerve_nuclei is a **strict-mirror pair with NO warning** —
**no SLEA warning**, **no fear-output warning**, and **no
lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left cranial nerve nuclei
    container is a **container** — it does **not** import from
    ``.../right/`` or any other right-side module. Bilateral
    relationships are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../solitary_nucleus/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../arcuate_nucleus/``, ``.../olivary_body/``,
    ``.../medullary_pyramid/``, ``.../ventral_respiratory_group/``,
    ``.../metencephalon/``, ``.../midbrain/``, or
    ``.../spinal_cord/``. The left cranial nerve nuclei
    container's relationships to the left solitary nucleus, left
    RVLM, left CVLM, left arcuate nucleus, left olivary body, left
    medullary pyramid, left pontine cranial nerve nuclei, left
    midbrain cranial nerve nuclei, and spinal cord are documented
    as **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with four leaf children.** The structural
    children are the four nuclei — each a **leaf**. Consumers
    **should** descend into them for **nucleus-level** resolution.
*   **NOT the right cranial nerve nuclei container.** The right
    container is a **separate module** under
    ``.../cranial_nerve_nuclei/right/``. Consumers must **not**
    conflate the left container with the right.
*   **NOT the parent cranial_nerve_nuclei container.** The parent
    is the **unpaired bilateral container**; the **left** module
    is **one side** of it.
*   **MOTOR, NOT sensory.** The **left solitary nucleus** and the
    **left spinal trigeminal nucleus** are **NOT** in this
    container.
*   **MEDULLARY, NOT pontine or midbrain.** The **left pontine**
    and **left midbrain** cranial nerve nuclei are wired under
    their respective containers.
*   **NOT the left RVLM / left CVLM / left arcuate nucleus.**
    Those are **autonomic / chemosensory** structures.
*   **NOT the left olivary body or left medullary pyramid.**
    Those are a **cerebellar relay** and a **white-matter
    tract**.
*   **No ``AREA_PATHS`` hop.** The left cranial nerve nuclei
    container is a **local container** — it is not cross-listed
    under another brainparts path.
*   **No nested cross-listing.** The left cranial nerve nuclei
    container has no nested dual-framing module. It is a
    **container** with **four leaf children**.
*   **Structural parity with the right cranial nerve nuclei
    container — strict mirror with NO warning.** The left and
    right containers are **structurally identical** — same four
    leaf children, same **parasympathetic / tongue-motor /
    branchial-motor** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "cranial_nerve_nuclei.left"
    )

**Do not** expect the four nuclei to be wired directly under
``cranial_nerve_nuclei``. The **left** and **right** containers
are **intermediate** — the four nuclei are leaf children of those
containers. Resolve them via
``cranial_nerve_nuclei.left.<nucleus>``.

**Do not** assume the left cranial nerve nuclei container is the
**right cranial nerve nuclei container**. The right container is
the **separate module** at ``.../cranial_nerve_nuclei/right/``.

**Do not** assume the left cranial nerve nuclei container is the
**left solitary nucleus** or the **left spinal trigeminal
nucleus**. Those are **sensory** nuclei — **NOT** in this
container.

**Do not** assume the left cranial nerve nuclei container is the
**left RVLM**, the **left CVLM**, or the **left arcuate
nucleus**. Those are **autonomic / chemosensory** structures.

**Do not** assume the left cranial nerve nuclei container is the
**left olivary body** or the **left medullary pyramid**. Those
are a **cerebellar relay** and a **white-matter tract**.

**Do not** assume the left cranial nerve nuclei container is the
**left pontine** or **left midbrain** cranial nerve nuclei.
Those are wired under their respective containers.

Iterating the left cranial nerve nuclei container's structural
children (recommended consumer pattern)::

    LEFT_CRANIAL_NERVE_NUCLEI_CHILDREN = (
        "dorsal_motor_nucleus_vagus",
        "hypoglossal_nucleus",
        "inferior_salivatory_nucleus",
        "nucleus_ambiguus",
    )
    # Each child is a leaf module representing the left side of
    # one of the four motor cranial nerve nuclei.

Reaching the four left nuclei (recommended consumer pattern)::

    # The four left nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.dorsal_motor_nucleus_vagus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.hypoglossal_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.inferior_salivatory_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.nucleus_ambiguus
    #
    # Each is a leaf module representing the LEFT side of that
    # nucleus.

Reaching the right cranial nerve nuclei container (recommended
consumer pattern — the contralateral container)::

    # The right cranial nerve nuclei container is the
    # CONTRALATERAL container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right
    #
    # The left and right containers are structurally symmetric
    # mirror pairs with the same four leaf nuclei.

Reaching the left solitary nucleus (recommended consumer pattern
— NOTE the DIFFERENT structure)::

    # The left solitary nucleus (NTS) is a SENSORY nucleus, NOT a
    # motor cranial nerve nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
    #
    # The left NTS is the VISCERAL AFFERENT relay — it is NOT in
    # the cranial_nerve_nuclei.left container.

Reaching the left RVLM, left CVLM, and left arcuate nucleus
(recommended consumer pattern — NOTE the DIFFERENT structures)::

    # The left RVLM, left CVLM, and left arcuate nucleus are
    # AUTONOMIC / CHEMOSENSORY structures, NOT cranial nerve motor
    # nuclei:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.left
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.left
    #
    # These are NOT in the cranial_nerve_nuclei.left container.

Reaching the left pontine and left midbrain cranial nerve nuclei
(recommended consumer pattern — NOTE the DIFFERENT containers)::

    # The left pontine and left midbrain cranial nerve nuclei are
    # wired under their respective containers:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left
    #   hindbrain.midbrain.cranial_nerve_nuclei.left
    #
    # The cranial_nerve_nuclei.left container (here) is
    # MEDULLARY — it contains ONLY the left medullary cranial
    # nerve nuclei (IX–XII).

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        for nucleus in LEFT_CRANIAL_NERVE_NUCLEI_CHILDREN:
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