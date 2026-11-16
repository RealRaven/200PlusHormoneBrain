"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei
==========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── cranial_nerve_nuclei   <-- THIS MODULE
                ├── left
                │   ├── dorsal_motor_nucleus_vagus
                │   ├── hypoglossal_nucleus
                │   ├── inferior_salivatory_nucleus
                │   └── nucleus_ambiguus
                └── right
                    ├── dorsal_motor_nucleus_vagus
                    ├── hypoglossal_nucleus
                    ├── inferior_salivatory_nucleus
                    └── nucleus_ambiguus

**Primary synonym:** Medullary cranial nerve nuclei; cranial nerve
nuclei IX–XII; bulbar motor nuclei; medullary motor column; caudal
cranial nerve nuclear column.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter container** — a group of **motor cranial
nerve nuclei** in the **medulla oblongata**, comprising the
**general somatic efferent** (hypoglossal — XII), **general
visceral efferent / parasympathetic** (dorsal motor nucleus of
vagus — X; inferior salivatory nucleus — IX), and **special
visceral efferent / branchial motor** (nucleus ambiguus —
IX/X/XI) columns.
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each a
**container** (not a leaf) with **four leaf children**:
1. ``dorsal_motor_nucleus_vagus`` — **CN X** — general visceral
   efferent (parasympathetic).
2. ``hypoglossal_nucleus`` — **CN XII** — general somatic efferent
   (tongue motor).
3. ``inferior_salivatory_nucleus`` — **CN IX** — general visceral
   efferent (parasympathetic to parotid).
4. ``nucleus_ambiguus`` — **CN IX/X/XI** — special visceral
   efferent (branchial motor to pharynx/larynx).
**Boundary status (NOT the whole medulla oblongata — a subset of
its nuclei):** **Boundary case — the cranial_nerve_nuclei is NOT
the whole medulla oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the cranial nerve nuclei (here) **and** the **autonomic
nuclei** (NTS, RVLM, CVLM), the **respiratory centers** (VRG,
DRG, RTN), the **olivary body**, the **medullary pyramid**, the
**arcuate nucleus**, and other structures. The
**cranial_nerve_nuclei** (here) is **one subset** — the **motor
cranial nerve nuclei IX–XII** — not the whole medulla. Consumers
must **not** conflate the **cranial_nerve_nuclei** container with
the **whole medulla oblongata**.
**Boundary status (NOT the solitary nucleus — the NTS is the
VISCERAL AFFERENT relay, not a motor nucleus):** **Boundary case
— the cranial_nerve_nuclei is NOT the solitary nucleus.** The
**solitary nucleus** (NTS) (``.../solitary_nucleus/``) is the
**visceral afferent relay** — it receives **taste**,
**baroreceptor**, **chemoreceptor**, and **gastrointestinal**
afferents from **CN VII, IX, and X**. It is **NOT a motor
nucleus** — it is a **sensory** nucleus. The
**cranial_nerve_nuclei** container (here) contains the **MOTOR**
cranial nerve nuclei of the medulla — the **dorsal motor nucleus
of vagus**, the **hypoglossal nucleus**, the **inferior
salivatory nucleus**, and the **nucleus ambiguus**. The **NTS**
is **anatomically adjacent** but is **NOT** in this container.
Consumers must **not** expect to find the **solitary nucleus**
under ``cranial_nerve_nuclei`` — resolve it via
``.../solitary_nucleus/``.
**Boundary status (NOT the spinal trigeminal nucleus — a sensory
nucleus, not a motor nucleus):** **Boundary case — the
cranial_nerve_nuclei is NOT the spinal trigeminal nucleus.** The
**spinal trigeminal nucleus** (and its tract) is the **facial
pain/temperature** sensory relay — it receives **CN V**
afferents from the face and is **NOT** a motor nucleus. It is
**not** wired under ``cranial_nerve_nuclei`` in this tree.
Consumers must **not** expect to find the **spinal trigeminal
nucleus** here.
**Boundary status (NOT the reticular formation — a cross-container
system):** **Boundary case — the cranial_nerve_nuclei is NOT the
reticular formation.** The **reticular formation** is a
**cross-container system** spanning the **midbrain tegmentum**,
the **pontine tegmentum**, and the **medullary reticular
nuclei** (``paramedian_reticular_nucleus``,
``respiratory_center/gigantocellular_reticular_nucleus``). The
**cranial_nerve_nuclei** (here) are **motor cranial nerve
nuclei** — **not** the reticular formation. Consumers must
**not** conflate the two.
**Boundary status (NOT the pons cranial nerve nuclei — those are
in the metencephalon):** **Boundary case — the
cranial_nerve_nuclei is NOT the pontine cranial nerve nuclei.**
The **pons** (``.../metencephalon/pons/``) contains its own
cranial nerve nuclei — the **motor trigeminal nucleus** (V),
**chief sensory trigeminal nucleus** (V), **abducens nucleus**
(VI), **facial nerve nucleus** (VII), **superior salivatory
nucleus** (VII), and the **vestibulocochlear nuclei** (VIII).
These are **NOT** in the medulla. The **cranial_nerve_nuclei**
(here) contains **only** the **medullary** cranial nerve nuclei
(IX–XII motor components). Consumers must **not** conflate the
**medullary** cranial nerve nuclei with the **pontine** cranial
nerve nuclei.
**Boundary status (NOT the midbrain cranial nerve nuclei — those
are in the midbrain):** **Boundary case — the
cranial_nerve_nuclei is NOT the midbrain cranial nerve nuclei.**
The **midbrain** (``.../midbrain/``) contains its own cranial
nerve nuclei — the **oculomotor nucleus** (III),
**Edinger-Westphal nucleus** (III), **trochlear nucleus** (IV),
and the **mesencephalic trigeminal nucleus** (V). These are
**NOT** in the medulla. Consumers must **not** conflate the
**medullary** cranial nerve nuclei with the **midbrain** cranial
nerve nuclei.
**Boundary status (NOT the RVLM / CVLM / arcuate nucleus — those
are autonomic / chemosensory, not cranial nerve motor):**
**Boundary case — the cranial_nerve_nuclei is NOT the
ventrolateral medullary structures.** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor** center; the **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay; the **arcuate nucleus**
(``.../arcuate_nucleus/``) is a **ventral-surface chemosensory**
nucleus. These are **NOT cranial nerve motor nuclei** — they are
**autonomic / chemosensory** structures. Consumers must **not**
conflate the **cranial_nerve_nuclei** with the **ventrolateral
medullary structures**.
**Boundary status (NOT the olivary body or the medullary pyramid —
those are different structures):** **Boundary case — the
cranial_nerve_nuclei is NOT the olivary body or the medullary
pyramid.** The **olivary body** (``.../olivary_body/``) contains
the **inferior olivary nucleus** (cerebellar climbing fibers);
the **medullary pyramid** (``.../medullary_pyramid/``) is the
**corticospinal / corticobulbar tract**. These are **NOT**
cranial nerve nuclei — they are a **cerebellar relay** and a
**white-matter tract**. Consumers must **not** conflate the
**cranial_nerve_nuclei** with these structures.
**Boundary status (NOT the spinal cord — that begins at the
foramen magnum):** **Boundary case — the cranial_nerve_nuclei is
NOT the spinal cord.** The **spinal cord**
(``.../spinal_cord/``) is a **separate container** beginning at
the **foramen magnum**. The **cranial_nerve_nuclei** (here) are
**medullary** structures. The **spinal accessory nucleus** (CN
XI, spinal part) is in the **cervical spinal cord**, **not** in
the medulla — only the **cranial part** of CN XI is associated
with the **nucleus ambiguus**. Consumers must **not** conflate
the **medullary** cranial nerve nuclei with the **spinal cord**.
**Boundary status (NOT a single nucleus — a CONTAINER of four
nuclei):** **Boundary case — the cranial_nerve_nuclei is a
CONTAINER, not a single nucleus.** It contains **four distinct
nuclei per side** — the **dorsal motor nucleus of vagus**, the
**hypoglossal nucleus**, the **inferior salivatory nucleus**, and
the **nucleus ambiguus**. Each is a **separate structure** with
**different functions** (parasympathetic, somatic motor,
parasympathetic, branchial motor). Consumers must **not** treat
the **cranial_nerve_nuclei** as a single uniform nucleus — it is
a **container** of **four functionally distinct nuclei**.
**Boundary status (BILATERAL container — left and right are
structural children):** **Boundary case — the
cranial_nerve_nuclei is a BILATERAL container with ``left`` and
``right`` structural children.** The **cranial_nerve_nuclei**
module (here) is an **unpaired container**; its **structural
children** are ``left`` and ``right`` — each a **container** (not
a leaf) with **four leaf children** (the four nuclei).
Consumers must **not** look for a single unpaired cranial nerve
nucleus — the **left** and **right** nuclei are **separate
containers** under this container. Resolve them via
``cranial_nerve_nuclei.left`` and ``cranial_nerve_nuclei.right``.

Overview
--------
The **cranial_nerve_nuclei** container is the **medullary motor
cranial nerve nuclear column** — the **CN IX–XII motor nuclei** of
the **medulla oblongata**. It is a **bilateral container** whose
``left`` and ``right`` children are **themselves containers** with
**four leaf children each** (the four motor nuclei).

**The cranial_nerve_nuclei is a CONTAINER of four nuclei, NOT a
single nucleus.** The four nuclei are:

*   **Dorsal motor nucleus of vagus** (CN X) — **general visceral
    efferent** (parasympathetic) — supplies the **thoracic and
    abdominal viscera** (heart, lungs, GI tract).

*   **Hypoglossal nucleus** (CN XII) — **general somatic efferent**
    (tongue motor) — supplies the **intrinsic and extrinsic
    tongue muscles**.

*   **Inferior salivatory nucleus** (CN IX) — **general visceral
    efferent** (parasympathetic) — supplies the **parotid gland**.

*   **Nucleus ambiguus** (CN IX/X/XI) — **special visceral
    efferent** (branchial motor) — supplies the **pharynx**,
    **larynx**, and **upper esophagus** (striated muscle).

**The cranial_nerve_nuclei is a BILATERAL container.** Its
structural children are ``left`` and ``right`` — each a
**container** with the four nuclei as leaf children. The
**container itself** is **unpaired**.

**The cranial_nerve_nuclei is MOTOR, NOT sensory.** The **sensory**
cranial nerve nuclei of the medulla — the **solitary nucleus**
(visceral afferent) and the **spinal trigeminal nucleus** (facial
pain/temperature) — are **NOT** in this container. The
**solitary nucleus** is wired under ``.../solitary_nucleus/``; the
**spinal trigeminal nucleus** is not wired under
``cranial_nerve_nuclei``.

**The cranial_nerve_nuclei is MEDULLARY, NOT pontine or midbrain.**
The **pontine** cranial nerve nuclei (V, VI, VII, VIII) and the
**midbrain** cranial nerve nuclei (III, IV) are wired under their
respective containers. The **cranial_nerve_nuclei** (here)
contains **only** the **medullary** cranial nerve nuclei.

Bilateral Structure
-------------------
The cranial_nerve_nuclei is a **bilateral container** with **two
structural children**:

*   ``left`` — the **left** medullary cranial nerve nuclei (a
    **container** with four leaf children).
*   ``right`` — the **right** medullary cranial nerve nuclei (a
    **container** with four leaf children).

**Each side is itself a container.** The ``left`` and ``right``
modules each have **four leaf children**:

*   ``dorsal_motor_nucleus_vagus`` — CN X — parasympathetic.
*   ``hypoglossal_nucleus`` — CN XII — tongue motor.
*   ``inferior_salivatory_nucleus`` — CN IX — parasympathetic to
    parotid.
*   ``nucleus_ambiguus`` — CN IX/X/XI — branchial motor.

**The container itself is unpaired.** There is **no**
``cranial_nerve_nuclei/left/.../left/`` — the ``left`` and
``right`` modules are **containers** with the four nuclei as their
**leaf children**.

**Two-level container structure:** ``cranial_nerve_nuclei`` →
``left`` / ``right`` → ``{four nuclei}``. Consumers that need
**side-specific** resolution descend into ``left`` or ``right``
and then into one of the four nuclei; consumers that need
**bilateral** resolution iterate over both sides and both the
four nuclei.

The Cranial Nerve Nuclei / Solitary Nucleus Boundary
----------------------------------------------------
This is the **motor / sensory** boundary:

*   **Cranial nerve nuclei** (this module) — the **MOTOR** CN IX–XII
    nuclei (dorsal motor vagus, hypoglossal, inferior salivatory,
    nucleus ambiguus).

*   **Solitary nucleus** (``.../solitary_nucleus/``) — the
    **VISCERAL AFFERENT** relay (taste, baroreceptor,
    chemoreceptor, gastrointestinal).

**The solitary nucleus is NOT in this container.** It is the
**sensory** counterpart to the **motor** cranial nerve nuclei.
Consumers must **not** conflate the **cranial_nerve_nuclei** with
the **solitary nucleus** — the **cranial_nerve_nuclei** is
**motor**; the **solitary nucleus** is **sensory**.

The Cranial Nerve Nuclei / Spinal Trigeminal Nucleus Boundary
-------------------------------------------------------------
This is the **facial-pain / motor** boundary:

*   **Cranial nerve nuclei** (this module) — the **MOTOR** CN IX–XII
    nuclei.

*   **Spinal trigeminal nucleus** — the **FACIAL PAIN/TEMPERATURE**
    sensory relay (CN V).

**The spinal trigeminal nucleus is NOT in this container.** It is
a **sensory** nucleus, not a **motor** nucleus.

The Cranial Nerve Nuclei / RVLM, CVLM, Arcuate Nucleus Boundary
--------------------------------------------------------------
This is the **motor / autonomic** boundary:

*   **Cranial nerve nuclei** (this module) — the **MOTOR** CN IX–XII
    nuclei.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) — the
    **sympathetic premotor** center.

*   **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **sympathoinhibitory** relay.

*   **Arcuate nucleus** (``.../arcuate_nucleus/``) — a
    **ventral-surface chemosensory** nucleus.

**The RVLM, CVLM, and arcuate nucleus are NOT in this container.**
They are **autonomic / chemosensory** structures, not **cranial
nerve motor nuclei**.

The Cranial Nerve Nuclei / Pons and Midbrain Cranial Nerve Nuclei Boundary
-------------------------------------------------------------------------
This is the **rostrocaudal** boundary:

*   **Cranial nerve nuclei** (this module) — the **MEDULLARY**
    cranial nerve nuclei (IX–XII motor components).

*   **Pons** (``.../metencephalon/pons/``) — the **PONTINE**
    cranial nerve nuclei (motor trigeminal, chief sensory
    trigeminal, abducens, facial, superior salivatory,
    vestibulocochlear).

*   **Midbrain** (``.../midbrain/``) — the **MIDBRAIN** cranial
    nerve nuclei (oculomotor, Edinger-Westphal, trochlear,
    mesencephalic trigeminal).

**The cranial_nerve_nuclei is MEDULLARY, NOT pontine or midbrain.**
Consumers must **not** conflate the **medullary** cranial nerve
nuclei with the **pontine** or **midbrain** cranial nerve nuclei
— each is wired under its respective container.

The Cranial Nerve Nuclei / Olivary Body and Medullary Pyramid Boundary
----------------------------------------------------------------------
This is the **nucleus / relay-and-tract** boundary:

*   **Cranial nerve nuclei** (this module) — the **MOTOR** CN IX–XII
    nuclei.

*   **Olivary body** (``.../olivary_body/``) — the **inferior
    olivary nucleus** (cerebellar climbing fibers).

*   **Medullary pyramid** (``.../medullary_pyramid/``) — the
    **corticospinal / corticobulbar tract**.

**The olivary body and medullary pyramid are NOT in this
container.** They are a **cerebellar relay** and a **white-matter
tract**, not **cranial nerve motor nuclei**.

The Cranial Nerve Nuclei / Spinal Cord Boundary
-----------------------------------------------
This is the **medulla / spinal cord** boundary:

*   **Cranial nerve nuclei** (this module) — the **MEDULLARY**
    cranial nerve nuclei.

*   **Spinal cord** (``.../spinal_cord/``) — a **separate
    container** beginning at the **foramen magnum**.

**The cranial_nerve_nuclei are MEDULLARY, NOT spinal.** The
**spinal accessory nucleus** (CN XI, spinal part) is in the
**cervical spinal cord**, not in the medulla — only the **cranial
part** of CN XI is associated with the **nucleus ambiguus**.

Function in the Human Brain
---------------------------
The cranial_nerve_nuclei's functions are the **CN IX–XII motor
functions** — **NOT autonomic premotor** and **NOT respiratory
rhythm**:

*   **Parasympathetic outflow (dorsal motor nucleus of vagus,
    inferior salivatory nucleus):** The **dorsal motor nucleus of
    vagus** (CN X) supplies **parasympathetic** fibers to the
    **heart**, **lungs**, and **gastrointestinal tract**; the
    **inferior salivatory nucleus** (CN IX) supplies
    **parasympathetic** fibers to the **parotid gland**.

*   **Tongue motor (hypoglossal nucleus):** The **hypoglossal
    nucleus** (CN XII) supplies the **intrinsic and extrinsic
    tongue muscles** — critical for **speech**, **swallowing**,
    and **mastication**.

*   **Branchial motor (nucleus ambiguus):** The **nucleus
    ambiguus** (CN IX/X/XI) supplies the **striated muscles** of
    the **pharynx**, **larynx**, and **upper esophagus** —
    critical for **swallowing**, **vocalization**, and **airway
    protection**.

*   **NOT autonomic premotor:** The **autonomic premotor**
    function is the **RVLM** (sympathetic) and the **NTS** /
    **dorsal motor nucleus of vagus** circuit (parasympathetic) —
    **NOT** the cranial_nerve_nuclei as a whole. The **dorsal
    motor nucleus of vagus** is a **parasympathetic preganglionic**
    nucleus, but the **sympathetic premotor** center is the
    **RVLM**.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the cranial_nerve_nuclei. The **nucleus ambiguus**
    and **nucleus para-ambiguus** (VRG) are **adjacent** and
    **interconnected**, but the **rhythm generator** is the VRG,
    not the nucleus ambiguus.

**The unifying theme:** the cranial_nerve_nuclei is the **medullary
motor cranial nerve column** — the **CN IX–XII motor nuclei**
(parasympathetic, tongue motor, branchial motor) wired as a
**bilateral container** with **four leaf nuclei per side**.

Associated Disorders
--------------------
The cranial_nerve_nuclei container is the **substrate** for a set
of **well-defined clinical syndromes** — its clinical relevance is
**direct**, via the four nuclei it contains:

*   **Bulbar palsy (via the four nuclei):** Dysfunction of the
    **cranial nerve nuclei IX–XII** — **dysphagia**, **dysarthria**,
    **tongue weakness** (hypoglossal), **palatal weakness**
    (nucleus ambiguus), **hoarseness** (nucleus ambiguus), and
    **parotid dryness** (inferior salivatory). The **cranial nerve
    nuclei** are the **direct substrate** of bulbar palsy.

*   **Wallenberg syndrome (Lateral Medullary Syndrome / PICA
    syndrome — via the nucleus ambiguus):** Infarction of the
    **lateral medulla** — **dysphagia / dysarthria / hoarseness**
    (nucleus ambiguus), **ipsilateral facial thermoalgesic loss**
    (spinal trigeminal nucleus/tract — **NOT** in this container),
    **contralateral body thermoalgesic loss** (spinothalamic
    tract — **NOT** in this container). The **nucleus ambiguus**
    (in this container) is the **cranial nerve motor** component
    of Wallenberg syndrome.

*   **Hypoglossal nerve palsy (via the hypoglossal nucleus):**
    **Tongue weakness** and **deviation** — from lesions in the
    **hypoglossal nucleus** or its **nerve**. The **hypoglossal
    nucleus** is the **direct substrate**.

*   **Vagal nerve dysfunction (via the dorsal motor nucleus of
    vagus):** **Autonomic** symptoms — **bradycardia**,
    **gastrointestinal dysmotility**, **nausea** — from lesions
    in the **dorsal motor nucleus of vagus** or its **nerve**.
    The **dorsal motor nucleus of vagus** is the **direct
    substrate**.

*   **Parotid dryness (via the inferior salivatory nucleus):**
    **Reduced parotid salivation** — from lesions in the
    **inferior salivatory nucleus** or its **nerve** (CN IX).
    The **inferior salivatory nucleus** is the **direct
    substrate**.

*   **Bulbar-onset ALS (via the four nuclei):** **Amyotrophic
    lateral sclerosis** with **bulbar onset** — **dysarthria**,
    **dysphagia**, **tongue atrophy/fasciculations** — from
    **degeneration** of the **cranial nerve motor nuclei**
    (especially **hypoglossal nucleus** and **nucleus
    ambiguus**). The **cranial_nerve_nuclei** are the **direct
    substrate**.

*   **Progressive bulbar palsy (via the four nuclei):** A
    **lower motor neuron** disorder of the **cranial nerve motor
    nuclei** — **dysarthria**, **dysphagia**, **tongue
    fasciculations** — from **degeneration** of the **cranial
    nerve nuclei**.

**What is NOT here:** The cranial_nerve_nuclei is **not** the
substrate for **central hypoventilation** (VRG / pre-Bötzinger
complex), **neurogenic hypertension** (RVLM / NTS / CVLM), or
**Wallenberg syndrome's sensory deficits** (spinal trigeminal
nucleus, spinothalamic tract — **NOT** in this container). Its
clinical relevance is the **cranial nerve motor** functions
listed above.

Lateralization Notes
--------------------
The cranial_nerve_nuclei is a **bilateral container** with
``left`` and ``right`` structural children — each a **container**
with **four leaf children**.

*   **Bilateral structural children:** ``left`` and ``right`` are
    **containers** — each has **four leaf children**
    (``dorsal_motor_nucleus_vagus``, ``hypoglossal_nucleus``,
    ``inferior_salivatory_nucleus``, ``nucleus_ambiguus``).
    Consumers resolve the **left** nuclei via
    ``cranial_nerve_nuclei.left.<nucleus>`` and the **right**
    nuclei via ``cranial_nerve_nuclei.right.<nucleus>``.

*   **Bilateral symmetry:** The **left** and **right** cranial
    nerve nuclei are **structurally symmetric** — they are
    **mirror pairs** with the **same** cytoarchitecture, **same**
    projections, and **same** functions. The **left** nuclei
    innervate the **left** side of the body; the **right**
    nuclei innervate the **right** side.

*   **Ipsilateral innervation (with exceptions):** The
    **hypoglossal nucleus** innervates the **ipsilateral** tongue
    (except **genioglossus**, which has **contralateral**
    corticobulbar input); the **nucleus ambiguus** innervates the
    **ipsilateral** pharynx/larynx; the **dorsal motor nucleus of
    vagus** and **inferior salivatory nucleus** project
    **ipsilaterally** to their peripheral targets.

*   **NO lateralization warning:** The cranial_nerve_nuclei has
    **no known functional lateralization** in humans beyond the
    **ipsilateral** innervation pattern. Consumers must **not**
    import a **lateralization warning** into the
    cranial_nerve_nuclei — the **left** and **right** sides are
    **functionally symmetric**.

*   **NO extended-amygdala / fear-output / SLEA warnings:** The
    cranial_nerve_nuclei is **not** part of the amygdala,
    extended-amygdala, or SLEA continuum. It carries **no SLEA
    warning** and **no fear-output warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The cranial_nerve_nuclei is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` containers are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../solitary_nucleus/``, ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``, ``.../arcuate_nucleus/``,
    ``.../olivary_body/``, ``.../medullary_pyramid/``,
    ``.../ventral_respiratory_group/``, ``.../metencephalon/``,
    ``.../midbrain/``, or ``.../spinal_cord/``. The
    cranial_nerve_nuclei's relationships to the solitary nucleus,
    RVLM, CVLM, arcuate nucleus, olivary body, medullary pyramid,
    pons, midbrain, and spinal cord are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two container children.** The
    structural children are ``left`` and ``right`` — each a
    **container** with four leaf children. The container itself
    is **unpaired**.
*   **Two-level container structure.** ``cranial_nerve_nuclei`` →
    ``left`` / ``right`` → **four leaf nuclei**. Consumers must
    **not** expect the four nuclei to be wired directly under
    ``cranial_nerve_nuclei`` — they are under ``left/`` and
    ``right/``.
*   **MOTOR, NOT sensory.** The **solitary nucleus** (visceral
    afferent) and the **spinal trigeminal nucleus** (facial
    pain/temperature) are **NOT** in this container. Consumers
    must **not** expect to find them here.
*   **MEDULLARY, NOT pontine or midbrain.** The **pontine** and
    **midbrain** cranial nerve nuclei are wired under their
    respective containers.
*   **NOT the RVLM / CVLM / arcuate nucleus.** Those are
    **autonomic / chemosensory** structures, not **cranial nerve
    motor nuclei**.
*   **NOT the olivary body or medullary pyramid.** Those are a
    **cerebellar relay** and a **white-matter tract**.
*   **No ``AREA_PATHS`` hop.** The cranial_nerve_nuclei is a
    **local container** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The cranial_nerve_nuclei has no
    nested dual-framing module. It is a **bilateral container**
    with **two container children**, each with **four leaf
    children**.
*   **Structural parity with the right side — strict mirror.** The
    ``left`` and ``right`` containers are **structurally
    identical** — same four leaf children, same
    **parasympathetic / tongue-motor / branchial-motor** framing,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import cranial_nerve_nuclei

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "cranial_nerve_nuclei"
    )

**Do not** expect the four nuclei to be wired directly under
``cranial_nerve_nuclei``. The **left** and **right** containers
are **intermediate** — the four nuclei are leaf children of those
containers. Resolve them via
``cranial_nerve_nuclei.{left,right}.<nucleus>``.

**Do not** assume the cranial_nerve_nuclei is the **solitary
nucleus** or the **spinal trigeminal nucleus**. Those are
**sensory** nuclei — **NOT** in this container.

**Do not** assume the cranial_nerve_nuclei is the **whole medulla
oblongata**. The medulla is the **parent container** — the
cranial_nerve_nuclei is one subset of its nuclei.

**Do not** assume the cranial_nerve_nuclei is the **RVLM**, the
**CVLM**, or the **arcuate nucleus**. Those are **autonomic /
chemosensory** structures.

**Do not** assume the cranial_nerve_nuclei is the **olivary body**
or the **medullary pyramid**. Those are a **cerebellar relay** and
a **white-matter tract**.

**Do not** assume the cranial_nerve_nuclei is the **pons** or
**midbrain** cranial nerve nuclei. Those are wired under their
respective containers.

Iterating the cranial_nerve_nuclei's structural children
(recommended consumer pattern)::

    CRANIAL_NERVE_NUCLEI_CHILDREN = ("left", "right")
    # Each child is a CONTAINER with four leaf nuclei.

Iterating the four nuclei per side (recommended consumer pattern)::

    CRANIAL_NERVE_NUCLEI_LEAVES = (
        "dorsal_motor_nucleus_vagus",
        "hypoglossal_nucleus",
        "inferior_salivatory_nucleus",
        "nucleus_ambiguus",
    )
    # Each is a leaf child of the left/ and right/ containers.

Reaching the left and right cranial nerve nuclei (recommended
consumer pattern)::

    # The left and right containers are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right
    #
    # Each is a CONTAINER with the four nuclei as leaf children.

Reaching the four nuclei (recommended consumer pattern)::

    # The four nuclei under the left container are:
    #
    #   ...cranial_nerve_nuclei.left.dorsal_motor_nucleus_vagus
    #   ...cranial_nerve_nuclei.left.hypoglossal_nucleus
    #   ...cranial_nerve_nuclei.left.inferior_salivatory_nucleus
    #   ...cranial_nerve_nuclei.left.nucleus_ambiguus
    #
    # The four nuclei under the right container are the mirror.

Reaching the solitary nucleus (recommended consumer pattern —
NOTE the DIFFERENT structure)::

    # The solitary nucleus (NTS) is a SENSORY nucleus, NOT a
    # motor cranial nerve nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # The NTS is the VISCERAL AFFERENT relay — it is NOT in the
    # cranial_nerve_nuclei container.

Reaching the RVLM, CVLM, and arcuate nucleus (recommended
consumer pattern — NOTE the DIFFERENT structures)::

    # The RVLM, CVLM, and arcuate nucleus are AUTONOMIC /
    # CHEMOSENSORY structures, NOT cranial nerve motor nuclei:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus
    #
    # These are NOT in the cranial_nerve_nuclei container.

Reaching the pontine and midbrain cranial nerve nuclei
(recommended consumer pattern — NOTE the DIFFERENT containers)::

    # The pontine and midbrain cranial nerve nuclei are wired
    # under their respective containers:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei
    #   hindbrain.midbrain.cranial_nerve_nuclei
    #
    # The cranial_nerve_nuclei container (here) is MEDULLARY —
    # it contains ONLY the medullary cranial nerve nuclei (IX–XII).

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        for nucleus in CRANIAL_NERVE_NUCLEI_LEAVES:
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
    corticobulbar input.)
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