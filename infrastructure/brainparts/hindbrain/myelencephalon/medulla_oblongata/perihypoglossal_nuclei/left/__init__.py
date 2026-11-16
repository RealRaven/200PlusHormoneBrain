"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left
===============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── perihypoglossal_nuclei
                └── left   <-- THIS MODULE
                    ├── intercalated_nucleus
                    └── prepositus_nucleus

**Primary synonym:** Left perihypoglossal nuclei; left
perihypoglossal nuclear complex; left PHN; left nuclei
perihipoglossi.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter container** — the **left-side** small
nuclei surrounding the **left hypoglossal nucleus** in the
**left dorsal medulla oblongata**, comprising the **left
intercalated nucleus** (nucleus intercalatus / Staderini's
nucleus) and the **left prepositus nucleus** (nucleus prepositus
hypoglossi / left NPH). It is **NOT** the **left hypoglossal
nucleus** itself — the left perihypoglossal nuclei **surround**
the left hypoglossal nucleus ("peri-" = "around") and are
involved in **oculomotor control** and **gaze holding**, **NOT**
tongue motor control.
**Part of:** The **perihypoglossal_nuclei** bilateral container —
which is part of the **medulla oblongata** — the **caudal
brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../perihypoglossal_nuclei/`` →
**direct child** of the perihypoglossal_nuclei container. The
**left** perihypoglossal nuclei container is one of the **two**
structural children of the container (the other is ``right``).
**Structural children:** **Two —** each a **leaf** representing
the **left** side of one of the two nuclei:
1. ``intercalated_nucleus`` — the **left intercalated nucleus of
   Staderini** — an **oculomotor** nucleus involved in
   **vertical gaze**.
2. ``prepositus_nucleus`` — the **left prepositus nucleus
   (NPH)** — the **neural integrator** for **horizontal gaze
   holding**.
**Boundary status (NOT the right perihypoglossal nuclei
container — the contralateral container):** **Boundary case —
the left perihypoglossal nuclei container is NOT the right
perihypoglossal nuclei container.** The **right perihypoglossal
nuclei container**
(``.../perihypoglossal_nuclei/right/``) is the **contralateral
container** — the perihypoglossal nuclei of the **right**
medulla. **They are DIFFERENT CONTAINERS** — the ``left`` and
``right`` modules are the two sides of the **bilateral parent
container**. Consumers must **not** conflate the **left**
container with the **right** — resolve the right side via
``perihypoglossal_nuclei.right``.
**Boundary status (NOT the parent perihypoglossal_nuclei
container — a SIDE of it):** **Boundary case — the left
perihypoglossal nuclei container is NOT the parent
perihypoglossal_nuclei container.** The **parent**
(``.../perihypoglossal_nuclei/``) is the **unpaired bilateral
container** — it contains **both** the ``left`` and ``right``
sides. The **left** container (here) is **one side** of that
parent. Consumers must **not** conflate the **left container**
with the **parent container** — the parent contains **both
sides**; the left container contains **only the left side**.
**Boundary status (NOT a single nucleus — a CONTAINER of two
nuclei):** **Boundary case — the left perihypoglossal nuclei
container is a CONTAINER, not a single nucleus.** It contains
**two distinct leaf nuclei** — the **left intercalated
nucleus** and the **left prepositus nucleus**. Each is a
**separate structure** with **different functions** (vertical
gaze vs. horizontal gaze holding). Consumers must **not** treat
the **left** container as a single uniform nucleus — it is a
**container** of **two functionally distinct nuclei**.
**Boundary status (NOT the left hypoglossal nucleus — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the left perihypoglossal nuclei container is NOT the left
hypoglossal nucleus.** The **left hypoglossal nucleus**
(``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) is the
**left somatic motor** nucleus for the **tongue** — it is
**NOT** part of the left perihypoglossal complex. The **left
perihypoglossal nuclei** (here) **surround** the left
hypoglossal nucleus ("peri-" = "around" + "hypoglossal") but
are **anatomically adjacent** and **functionally distinct**.
Consumers must **not** conflate the two — resolve the left
hypoglossal nucleus via ``cranial_nerve_nuclei.left``.
**Boundary status (NOT the left nucleus of Roller — sometimes
grouped but NOT in this tree):** **Boundary case — the left
perihypoglossal nuclei container is NOT the left nucleus of
Roller.** The **nucleus of Roller** is **sometimes grouped**
with the PHN in the literature but is **NOT wired** in this
tree — only the **left intercalated nucleus** and the **left
prepositus nucleus** are.
**Boundary status (NOT the left abducens nucleus or left PPRF —
PONTINE structures):** **Boundary case — the left
perihypoglossal nuclei container is NOT the left abducens
nucleus or left PPRF.** The **left abducens nucleus**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``)
and **left PPRF**
(``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/left/``)
are **pontine** horizontal **saccade generators**. The **left
perihypoglossal nuclei** (here) are **medullary oculomotor**
nuclei — they are **functionally coupled** but **anatomically
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the left vestibular nuclei or the MLF —
different structures):** **Boundary case — the left
perihypoglossal nuclei container is NOT the left vestibular
nuclei or the MLF.** The **left vestibular nuclei**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
are **pontomedullary** VOR relays; the **MLF** is a
**white-matter tract**. The **left perihypoglossal nuclei**
(here) are **medullary oculomotor** nuclei — they are
**functionally coupled** but **anatomically distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left nucleus ambiguus, left solitary
nucleus, left dorsal motor nucleus of the vagus, left medullary
pyramid, left olivary body, left arcuate nucleus, left
parafacial zone, left paramedian reticular nucleus, or left
respiratory centers — DIFFERENT structures):** **Boundary case
— the left perihypoglossal nuclei container is NOT these other
left medullary structures.** Each is a **different structure**
— see the respective modules. Consumers must **not** conflate
the **left perihypoglossal nuclei** with any of these.

Overview
--------
The **left perihypoglossal nuclei container** is the
**left-side** group of small medullary grey-matter nuclei that
**surround the left hypoglossal nucleus** in the **left dorsal
medulla** — the **left intercalated nucleus** and the **left
prepositus nucleus**. It is the **left** side of the
**perihypoglossal_nuclei** bilateral container, and it is a
**container** (not a leaf) with **two leaf children** (the two
nuclei).

**The left perihypoglossal nuclei container is a CONTAINER of
two nuclei, NOT a single nucleus.** The two **left** nuclei are:

*   **Left intercalated nucleus** (nucleus intercalatus /
    Staderini's nucleus) — an **oculomotor** nucleus involved in
    **vertical gaze** and **vestibulo-ocular** integration.

*   **Left prepositus nucleus** (NPH) — the **neural
    integrator** for **horizontal gaze holding**.

**The left perihypoglossal nuclei container is OCULOMOTOR, NOT
motor, NOT visceral, and NOT autonomic.** The **left hypoglossal
nucleus** is **NOT** in this container — it is **motor**
(tongue); the **left perihypoglossal nuclei** are **oculomotor**
(gaze).

**The left perihypoglossal nuclei container is one side of the
bilateral parent container.** The **parent**
(``.../perihypoglossal_nuclei/``) contains **both** the ``left``
and ``right`` sides; the **left** container (here) contains
**only the left side**.

Structural Children (Two Leaves)
--------------------------------
The left perihypoglossal nuclei container has **two structural
children**, each a **leaf**:

*   ``intercalated_nucleus`` — **left intercalated nucleus of
    Staderini** — an **oculomotor** nucleus involved in
    **vertical gaze**.

*   ``prepositus_nucleus`` — **left prepositus nucleus (NPH)** —
    the **neural integrator** for **horizontal gaze holding**.

**Each child is a leaf.** The two nucleus modules are **single
structures** — they have **no structural children** of their
own. Consumers that need **nucleus-level** resolution descend
into one of the two leaves; consumers that need **side-level**
resolution use this container as a whole; consumers that need
**bilateral** resolution iterate over both ``left`` and
``right``.

The Left Perihypoglossal Nuclei / Right Perihypoglossal Nuclei Boundary
-----------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left perihypoglossal nuclei container** (this module) — the
    perihypoglossal nuclei of the **left** medulla.

*   **Right perihypoglossal nuclei container**
    (``.../perihypoglossal_nuclei/right/``) — the
    perihypoglossal nuclei of the **right** medulla.

**The two are the SIDES of the bilateral
perihypoglossal_nuclei container.** They are **structurally
symmetric mirror pairs** — same two leaf nuclei, same
cytoarchitecture, same projections (with some crossed
components), same functions. Consumers must **not** conflate the
left container with the right — resolve the right side via
``perihypoglossal_nuclei.right``.

The Left Perihypoglossal Nuclei / Left Hypoglossal Nucleus Boundary
-------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Left perihypoglossal nuclei container** (this module) — the
    **left oculomotor** nuclei that **surround** the left
    hypoglossal nucleus.

*   **Left hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) —
    the **left somatic motor** nucleus for the **tongue**.

**They share the name "hypoglossal" but are DIFFERENT STRUCTURES
in DIFFERENT CONTAINERS with DIFFERENT FUNCTIONS** — the **left
hypoglossal nucleus** is **motor** (tongue); the **left
perihypoglossal nuclei** are **oculomotor** (gaze). Consumers
must **not** conflate the two.

The Left Perihypoglossal Nuclei / Left Nucleus of Roller Boundary
-----------------------------------------------------------------
This is the **sometimes-grouped** boundary:

*   **Left perihypoglossal nuclei container** (this module) — the
    **left intercalated nucleus** and **left prepositus
    nucleus**.

*   **Left nucleus of Roller** — a **small medullary nucleus**
    sometimes grouped with the PHN in the literature, **NOT**
    wired in this tree.

**The left nucleus of Roller is NOT wired** as a structural child
of the left perihypoglossal nuclei container. Consumers must
**not** expect to find it here — resolve it via the references.

The Left Perihypoglossal Nuclei / Left Abducens Nucleus and Left PPRF Boundary
-----------------------------------------------------------------------------
This is the **gaze-holding / gaze-generating** boundary:

*   **Left perihypoglossal nuclei container** (this module) — the
    **left medullary** oculomotor nuclei.

*   **Left abducens nucleus**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``)
    and **left PPRF**
    (``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/left/``)
    — the **left pontine** horizontal **saccade generators**.

**They are functionally coupled** but **anatomically distinct**.
Consumers must **not** conflate the two.

The Left Perihypoglossal Nuclei / Left Vestibular Nuclei and MLF Boundary
-------------------------------------------------------------------------
This is the **gaze-holding / VOR-and-MLF** boundary:

*   **Left perihypoglossal nuclei container** (this module) — the
    **left medullary** oculomotor nuclei.

*   **Left vestibular nuclei**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **left VOR relay**.

*   **MLF** — the **white-matter tract** that **connects**
    oculomotor structures.

**They are functionally coupled** but **anatomically distinct**.
Consumers must **not** conflate the two.

The Left Perihypoglossal Nuclei / Other Left Medullary Structures Boundary
--------------------------------------------------------------------------
This is the **oculomotor / non-oculomotor** boundary:

*   **Left perihypoglossal nuclei container** (this module) — the
    **left medullary oculomotor** nuclei.

*   **Left nucleus ambiguus, left solitary nucleus, left dorsal
    motor nucleus of the vagus, left medullary pyramid, left
    olivary body, left arcuate nucleus, left parafacial zone,
    left paramedian reticular nucleus, left respiratory
    centers** — **other left medullary structures**.

**Each is a DIFFERENT STRUCTURE.** Consumers must **not** conflate
the **left perihypoglossal nuclei** with any of these.

Function in the Human Brain
---------------------------
The left perihypoglossal nuclei container's function is
**oculomotor** — **gaze holding** (left prepositus nucleus) and
**vertical gaze integration** (left intercalated nucleus) —
**NOT motor conduction**, **NOT tongue motor control**, and
**NOT autonomic regulation**:

*   **Horizontal gaze holding (left prepositus nucleus):** The
    **left prepositus nucleus** is the **left neural
    integrator** for **horizontal gaze** — it **holds** the
    **left-side horizontal gaze** position after a **saccade**.

*   **Vertical gaze integration (left intercalated nucleus):**
    The **left intercalated nucleus** is involved in **vertical
    gaze** integration and **vertical vestibulo-ocular reflex**
    processing.

*   **Vestibulo-ocular integration (left side):** Both the
    **left prepositus nucleus** and the **left intercalated
    nucleus** **integrate** **vestibular** signals with
    **oculomotor** commands.

*   **NOT motor conduction:** The **left perihypoglossal
    nuclei** do **not** send motor axons to muscles.

*   **NOT tongue motor control:** The **tongue motor control**
    is the **left hypoglossal nucleus** — **NOT** the left
    perihypoglossal nuclei.

*   **NOT autonomic regulation:** The **left perihypoglossal
    nuclei** do **not** regulate autonomic function.

**The unifying theme:** the left perihypoglossal nuclei are the
**left medullary oculomotor nuclei** that **surround** the left
hypoglossal nucleus — they **hold gaze** (left prepositus
nucleus) and **integrate vertical gaze** (left intercalated
nucleus), and they **participate** in the **horizontal and
vertical VOR**.

Associated Disorders
--------------------
The left perihypoglossal nuclei container is the **substrate**
for **well-defined clinical syndromes** — its clinical relevance
is **direct**, via **gaze-holding** and **vestibulo-ocular**
dysfunction:

*   **Gaze-evoked nystagmus (via left prepositus nucleus
    dysfunction):** **Impaired** horizontal **gaze holding** on
    the **left side** — the **left prepositus nucleus** is the
    **left neural integrator**; its **dysfunction** causes
    **gaze-evoked nystagmus**. This is a **cardinal**
    brainstem/cerebellar sign.

*   **Vertical gaze palsy / vertical gaze-evoked nystagmus (via
    left intercalated nucleus dysfunction):** **Impaired**
    vertical **gaze holding** or **vertical saccades** — from
    **left intercalated nucleus** dysfunction. This is **less
    well characterized** than horizontal gaze-holding failure.

*   **Wernicke encephalopathy (via left PHN involvement):**
    **Wernicke encephalopathy** (thiamine deficiency)
    **typically** involves the **medial vestibular nuclei** and
    the **left perihypoglossal nuclei** — producing **nystagmus**,
    **gaze-evoked nystagmus**, and **gaze palsy** in addition to
    the **classic triad** (ophthalmoplegia, ataxia, confusion).
    The **left perihypoglossal nuclei** are a **direct
    substrate** of the **oculomotor** findings in Wernicke
    encephalopathy.

*   **Brainstem stroke (via left PHN involvement):** **Left
    medullary** **stroke** can **involve** the **left
    perihypoglossal nuclei** or their **connections** —
    contributing to **nystagmus** and **gaze-holding**
    abnormalities.

*   **No Named "Left Perihypoglossal Nuclei Syndrome":** The left
    perihypoglossal nuclei are a **small nuclear complex** —
    their clinical syndromes are **named for the broader
    brainstem/cerebellar lesion** or the **oculomotor sign**,
    **not** for the nuclei themselves.

**What is NOT here:** The left perihypoglossal nuclei are **not**
the substrate for **tongue weakness** (left hypoglossal
nucleus), **motor weakness** (left corticospinal tract — **NOT**
in this container), **sensory loss** (left medial lemniscus,
left spinothalamic tract — **NOT** in this container),
**autonomic dysfunction** (left RVLM, left CVLM, left NTS —
**NOT** in this container), or **respiratory rhythm** (left
VRG, left DRG — **NOT** in this container). Their clinical
relevance is the **gaze-holding** and **VOR** functions listed
above.

Lateralization Notes
--------------------
This is the **left** perihypoglossal nuclei container. The
perihypoglossal nuclei are a **bilateral container** whose two
sides are **structurally symmetric mirror pairs** — and it
carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right**
    perihypoglossal nuclei are **structurally symmetric** — they
    are **mirror pairs** with the **same** two leaf nuclei,
    **same** cytoarchitecture, **same** projections, and **same**
    functions.

*   **Partly Crossed Projections:** Some **PHN** projections are
    **ipsilateral** (e.g., **left prepositus → left
    abducens/vestibular nuclei**) and some are **crossed** (via
    the **MLF** and **other** commissural pathways). The **PHN**
    functions **bilaterally** in **gaze holding** — a
    **unilateral** lesion can cause **bilateral** **gaze-evoked
    nystagmus**.

*   **NO Lateralization Warning:** The perihypoglossal nuclei
    have **no known functional lateralization** in humans.
    Consumers must **not** import a **lateralization warning**
    into the left perihypoglossal nuclei — the **left** and
    **right** sides are **functionally symmetric** at the
    **nucleus level**.

*   **NO Extended-Amygdala / SLEA Warning:** The left
    perihypoglossal nuclei are **SLEA-free** — they are **not**
    an extended-amygdala component. Consumers must **not** import
    the SLEA warning into the left perihypoglossal nuclei.

*   **NO Fear-Output Warning:** The left perihypoglossal nuclei
    are **not** a fear-output structure — they are **left
    medullary oculomotor** nuclei. Consumers must **not**
    conflate them with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "left perihypoglossal nuclei = right
perihypoglossal nuclei" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**nucleus level**. The perihypoglossal nuclei are a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left perihypoglossal
    nuclei container is a **container** — it does **not** import
    from ``.../right/`` or any other right-side module.
    Bilateral relationships are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../cranial_nerve_nuclei/``,
    ``.../metencephalon/pons/cranial_nerve_nuclei/``,
    ``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``,
    ``.../solitary_nucleus/``,
    ``.../medullary_pyramid/``, ``.../olivary_body/``,
    ``.../arcuate_nucleus/``, ``.../parafacial_zone/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../respiratory_center/``,
    ``.../ventral_respiratory_group/``, or any other container.
    The left perihypoglossal nuclei's relationships to the left
    hypoglossal nucleus, left nucleus of Roller, left abducens
    nucleus, left PPRF, left vestibular nuclei, MLF, left
    nucleus ambiguus, left solitary nucleus, left cranial nerve
    nuclei, left medullary pyramid, left olivary body, left
    arcuate nucleus, left parafacial zone, left paramedian
    reticular nucleus, and left respiratory centers are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with two leaf children.** The structural
    children are the two nuclei — each a **leaf**. Consumers
    **should** descend into them for **nucleus-level**
    resolution.
*   **NOT the right perihypoglossal nuclei container.** The right
    container is a **separate module** under
    ``.../perihypoglossal_nuclei/right/``. Consumers must **not**
    conflate the left container with the right.
*   **NOT the parent perihypoglossal_nuclei container.** The
    parent is the **unpaired bilateral container**; the **left**
    module is **one side** of it.
*   **OCULOMOTOR, NOT motor.** The **left hypoglossal nucleus**
    is **NOT** in this container. The left perihypoglossal
    nuclei are **oculomotor** — **NOT** tongue motor.
*   **NOT the left nucleus of Roller.** The nucleus of Roller is
    **sometimes grouped** with the PHN in the literature but is
    **NOT wired** in this tree.
*   **NOT the left abducens nucleus, left PPRF, left vestibular
    nuclei, or MLF.** Those are **different structures**.
*   **NOT the left nucleus ambiguus, left solitary nucleus, left
    dorsal motor nucleus of the vagus, left medullary pyramid,
    left olivary body, left arcuate nucleus, left parafacial
    zone, left paramedian reticular nucleus, or left respiratory
    centers.** Each is a **different structure**.
*   **No ``AREA_PATHS`` hop.** The left perihypoglossal nuclei
    container is a **local container** — it is not cross-listed
    under another brainparts path.
*   **No nested cross-listing.** The left perihypoglossal nuclei
    container has no nested dual-framing module. It is a
    **container** with **two leaf children**.
*   **Structural parity with the right perihypoglossal nuclei
    container — strict mirror with NO warning.** The left and
    right containers are **structurally identical** — same two
    leaf children, same **oculomotor** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "perihypoglossal_nuclei.left"
    )

**Do not** expect the two nuclei to be wired directly under
``perihypoglossal_nuclei``. The **left** and **right** containers
are **intermediate** — the two nuclei are leaf children of those
containers. Resolve them via
``perihypoglossal_nuclei.left.<nucleus>``.

**Do not** assume the left perihypoglossal nuclei container is
the **right perihypoglossal nuclei container**. The right
container is the **separate module** at
``.../perihypoglossal_nuclei/right/``.

**Do not** assume the left perihypoglossal nuclei container is
the **left hypoglossal nucleus**. They **surround** the left
hypoglossal nucleus ("peri-" = "around") but are **separate
structures** — the left hypoglossal nucleus is **motor**
(tongue); the left perihypoglossal nuclei are **oculomotor**
(gaze).

**Do not** assume the left perihypoglossal nuclei container is
the **left nucleus of Roller**. The nucleus of Roller is
**sometimes grouped** with the PHN in the literature but is
**NOT wired** in this tree.

**Do not** assume the left perihypoglossal nuclei container is
the **left abducens nucleus**, **left PPRF**, **left vestibular
nuclei**, or **MLF**. Those are **different structures**.

**Do not** assume the left perihypoglossal nuclei container is
the **left nucleus ambiguus**, **left solitary nucleus**,
**left dorsal motor nucleus of the vagus**, **left medullary
pyramid**, **left olivary body**, **left arcuate nucleus**,
**left parafacial zone**, **left paramedian reticular nucleus**,
or **left respiratory centers**. Each is a **different
structure**.

Iterating the left perihypoglossal nuclei container's structural
children (recommended consumer pattern)::

    LEFT_PERIHYPOGLOSSAL_NUCLEI_CHILDREN = (
        "intercalated_nucleus",
        "prepositus_nucleus",
    )
    # Each child is a leaf module representing the left side of
    # one of the two perihypoglossal nuclei.

Reaching the two left nuclei (recommended consumer pattern)::

    # The two left nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left.intercalated_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left.prepositus_nucleus
    #
    # Each is a leaf module representing the LEFT side of that
    # nucleus.

Reaching the right perihypoglossal nuclei container (recommended
consumer pattern — the contralateral container)::

    # The right perihypoglossal nuclei container is the
    # CONTRALATERAL container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right
    #
    # The left and right containers are structurally symmetric
    # mirror pairs with the same two leaf nuclei.

Reaching the left hypoglossal nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The left hypoglossal nucleus is a MOTOR nucleus, NOT part
    # of the left perihypoglossal nuclei:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.hypoglossal_nucleus
    #
    # The left perihypoglossal nuclei SURROUND the left
    # hypoglossal nucleus ("peri-" = "around") but are SEPARATE
    # structures with DIFFERENT functions.

Reaching the left abducens nucleus and left PPRF (recommended
consumer pattern — NOTE the DIFFERENT containers)::

    # The left abducens nucleus and left PPRF are PONTINE
    # structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.abducens_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.paramedian_pontine_reticular_formation.left
    #
    # They are functionally coupled with the left prepositus
    # nucleus (left PPRF drives the saccade; left prepositus
    # holds gaze) but are anatomically distinct.

Reaching the left vestibular nuclei (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The left vestibular nuclei are PONTOMEDULLARY structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei.vestibular_nuclei
    #
    # They are functionally coupled with the left perihypoglossal
    # nuclei in the VOR — but they are DIFFERENT structures.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        for nucleus in LEFT_PERIHYPOGLOSSAL_NUCLEI_CHILDREN:
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"perihypoglossal_nuclei.{side}.{nucleus}"
            )
            # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Perihypoglossal nuclei; intercalated nucleus; prepositus
    nucleus; oculomotor system.)
*   **Prepositus nucleus — neural integrator:** Cannon, S.C.,
    Robinson, D.A. (1987). "Loss of the neural integrator of
    the oculomotor system from brain stem lesions in monkey."
    *Journal of Neurophysiology* 57:1383–1409. (Prepositus
    nucleus; neural integrator; horizontal gaze holding.)
*   **Prepositus nucleus — anatomy and connections:** McCrea,
    R.A., Baker, R. (1985). "Anatomical connections of the
    nucleus prepositus of the cat." *Journal of Comparative
    Neurology* 237:377–407. (Prepositus nucleus; connections
    to abducens, vestibular nuclei, and cerebellum.)
*   **Prepositus nucleus — vertical and horizontal gaze:** Baker,
    R., et al. (1975). "Postsynaptic potentials in abducens
    motoneurons induced by vestibular stimulation." *Brain
    Research* 94:467–488. (Prepositus nucleus; VOR; gaze
    holding.)
*   **Intercalated nucleus — oculomotor functions:** Langer,
    T., et al. (1986). "The nucleus intercalatus and the
    nucleus prepositus hypoglossi: their involvement in
    vertical and horizontal eye movements." *Experimental
    Brain Research* 64:325–334. (Intercalated nucleus;
    vertical gaze; vertical VOR.)
*   **Perihypoglossal nuclei — overview:** Leigh, R.J., Zee,
    D.S. (2015). *The Neurology of Eye Movements*, 5th ed.
    (Perihypoglossal nuclei; intercalated nucleus; prepositus
    nucleus; neural integrator; gaze-evoked nystagmus.)
*   **Gaze-evoked nystagmus — clinical:** Leigh, R.J., Zee,
    D.S. (2015). *The Neurology of Eye Movements*, 5th ed.
    (Gaze-evoked nystagmus; neural integrator; prepositus
    nucleus.)
*   **Wernicke encephalopathy — oculomotor findings:** Victor,
    M., et al. (1989). *The Wernicke-Korsakoff Syndrome and
    Related Neurologic Disorders Due to Alcoholism and
    Malnutrition*, 2nd ed. (Wernicke encephalopathy; medial
    vestibular nuclei; perihypoglossal nuclei; nystagmus.)
*   **Hypoglossal nucleus (contrast — motor):** Lowe, A.A.
    (1980). "The neural regulation of tongue movement."
    *Progress in Neurobiology* 14:273–349. (Hypoglossal
    nucleus; tongue motor — DIFFERENT from the perihypoglossal
    nuclei.)
*   **Abducens nucleus and PPRF (contrast — pontine horizontal
    gaze):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of
    Eye Movements*, 5th ed. (Abducens nucleus; PPRF; horizontal
    saccades — DIFFERENT from the perihypoglossal nuclei.)
*   **Vestibular nuclei (contrast — VOR relay):** Wilson, V.J.,
    Melvill Jones, G. (1979). *Mammalian Vestibular
    Physiology.* (Vestibular nuclei; VOR — DIFFERENT from the
    perihypoglossal nuclei.)
*   NeuroNames — Perihypoglossal nuclei; FMA — Perihypoglossal
    nuclei.
"""