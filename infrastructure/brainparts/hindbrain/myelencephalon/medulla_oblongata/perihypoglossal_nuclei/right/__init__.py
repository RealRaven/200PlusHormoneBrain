"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right
================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── perihypoglossal_nuclei
                └── right   <-- THIS MODULE
                    ├── intercalated_nucleus
                    └── prepositus_nucleus

**Primary synonym:** Right perihypoglossal nuclei; right
perihypoglossal nuclear complex; right PHN; right nuclei
perihipoglossi.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter container** — the **right-side** small
nuclei surrounding the **right hypoglossal nucleus** in the
**right dorsal medulla oblongata**, comprising the **right
intercalated nucleus** (nucleus intercalatus / Staderini's
nucleus) and the **right prepositus nucleus** (nucleus prepositus
hypoglossi / right NPH). It is **NOT** the **right hypoglossal
nucleus** itself — the right perihypoglossal nuclei **surround**
the right hypoglossal nucleus ("peri-" = "around") and are
involved in **oculomotor control** and **gaze holding**, **NOT**
tongue motor control.
**Part of:** The **perihypoglossal_nuclei** bilateral container —
which is part of the **medulla oblongata** — the **caudal
brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../perihypoglossal_nuclei/`` →
**direct child** of the perihypoglossal_nuclei container. The
**right** perihypoglossal nuclei container is one of the **two**
structural children of the container (the other is ``left``).
**Structural children:** **Two —** each a **leaf** representing
the **right** side of one of the two nuclei:
1. ``intercalated_nucleus`` — the **right intercalated nucleus
   of Staderini** — an **oculomotor** nucleus involved in
   **vertical gaze**.
2. ``prepositus_nucleus`` — the **right prepositus nucleus
   (NPH)** — the **neural integrator** for **horizontal gaze
   holding**.
**Boundary status (NOT the left perihypoglossal nuclei
container — the contralateral container):** **Boundary case —
the right perihypoglossal nuclei container is NOT the left
perihypoglossal nuclei container.** The **left perihypoglossal
nuclei container**
(``.../perihypoglossal_nuclei/left/``) is the **contralateral
container** — the perihypoglossal nuclei of the **left**
medulla. **They are DIFFERENT CONTAINERS** — the ``left`` and
``right`` modules are the two sides of the **bilateral parent
container**. Consumers must **not** conflate the **right**
container with the **left** — resolve the left side via
``perihypoglossal_nuclei.left``.
**Boundary status (NOT the parent perihypoglossal_nuclei
container — a SIDE of it):** **Boundary case — the right
perihypoglossal nuclei container is NOT the parent
perihypoglossal_nuclei container.** The **parent**
(``.../perihypoglossal_nuclei/``) is the **unpaired bilateral
container** — it contains **both** the ``left`` and ``right``
sides. The **right** container (here) is **one side** of that
parent. Consumers must **not** conflate the **right container**
with the **parent container** — the parent contains **both
sides**; the right container contains **only the right side**.
**Boundary status (NOT a single nucleus — a CONTAINER of two
nuclei):** **Boundary case — the right perihypoglossal nuclei
container is a CONTAINER, not a single nucleus.** It contains
**two distinct leaf nuclei** — the **right intercalated
nucleus** and the **right prepositus nucleus**. Each is a
**separate structure** with **different functions** (vertical
gaze vs. horizontal gaze holding). Consumers must **not** treat
the **right** container as a single uniform nucleus — it is a
**container** of **two functionally distinct nuclei**.
**Boundary status (NOT the right hypoglossal nucleus — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the right perihypoglossal nuclei container is NOT the right
hypoglossal nucleus.** The **right hypoglossal nucleus**
(``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is the
**right somatic motor** nucleus for the **tongue** — it is
**NOT** part of the right perihypoglossal complex. The **right
perihypoglossal nuclei** (here) **surround** the right
hypoglossal nucleus ("peri-" = "around" + "hypoglossal") but
are **anatomically adjacent** and **functionally distinct**.
Consumers must **not** conflate the two — resolve the right
hypoglossal nucleus via ``cranial_nerve_nuclei.right``.
**Boundary status (NOT the right nucleus of Roller — sometimes
grouped but NOT in this tree):** **Boundary case — the right
perihypoglossal nuclei container is NOT the right nucleus of
Roller.** The **nucleus of Roller** is **sometimes grouped**
with the PHN in the literature but is **NOT wired** in this
tree — only the **right intercalated nucleus** and the **right
prepositus nucleus** are.
**Boundary status (NOT the right abducens nucleus or right
PPRF — PONTINE structures):** **Boundary case — the right
perihypoglossal nuclei container is NOT the right abducens
nucleus or right PPRF.** The **right abducens nucleus**
(``.../metencephalon/pons/cranial_nerve_nuclei/right/abducens_nucleus/``)
and **right PPRF**
(``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/right/``)
are **pontine** horizontal **saccade generators**. The **right
perihypoglossal nuclei** (here) are **medullary oculomotor**
nuclei — they are **functionally coupled** but **anatomically
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the right vestibular nuclei or the MLF —
different structures):** **Boundary case — the right
perihypoglossal nuclei container is NOT the right vestibular
nuclei or the MLF.** The **right vestibular nuclei**
(``.../metencephalon/pons/cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
are **pontomedullary** VOR relays; the **MLF** is a
**white-matter tract**. The **right perihypoglossal nuclei**
(here) are **medullary oculomotor** nuclei — they are
**functionally coupled** but **anatomically distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right nucleus ambiguus, right
solitary nucleus, right dorsal motor nucleus of the vagus,
right medullary pyramid, right olivary body, right arcuate
nucleus, right parafacial zone, right paramedian reticular
nucleus, or right respiratory centers — DIFFERENT structures):**
**Boundary case — the right perihypoglossal nuclei container is
NOT these other right medullary structures.** Each is a
**different structure** — see the respective modules. Consumers
must **not** conflate the **right perihypoglossal nuclei** with
any of these.

Overview
--------
The **right perihypoglossal nuclei container** is the
**right-side** group of small medullary grey-matter nuclei that
**surround the right hypoglossal nucleus** in the **right dorsal
medulla** — the **right intercalated nucleus** and the **right
prepositus nucleus**. It is the **right** side of the
**perihypoglossal_nuclei** bilateral container, and it is a
**container** (not a leaf) with **two leaf children** (the two
nuclei).

**The right perihypoglossal nuclei container is a CONTAINER of
two nuclei, NOT a single nucleus.** The two **right** nuclei
are:

*   **Right intercalated nucleus** (nucleus intercalatus /
    Staderini's nucleus) — an **oculomotor** nucleus involved in
    **vertical gaze** and **vestibulo-ocular** integration.

*   **Right prepositus nucleus** (NPH) — the **neural
    integrator** for **horizontal gaze holding**.

**The right perihypoglossal nuclei container is OCULOMOTOR, NOT
motor, NOT visceral, and NOT autonomic.** The **right
hypoglossal nucleus** is **NOT** in this container — it is
**motor** (tongue); the **right perihypoglossal nuclei** are
**oculomotor** (gaze).

**The right perihypoglossal nuclei container is one side of the
bilateral parent container.** The **parent**
(``.../perihypoglossal_nuclei/``) contains **both** the ``left``
and ``right`` sides; the **right** container (here) contains
**only the right side**.

Structural Children (Two Leaves)
--------------------------------
The right perihypoglossal nuclei container has **two structural
children**, each a **leaf**:

*   ``intercalated_nucleus`` — **right intercalated nucleus of
    Staderini** — an **oculomotor** nucleus involved in
    **vertical gaze**.

*   ``prepositus_nucleus`` — **right prepositus nucleus (NPH)** —
    the **neural integrator** for **horizontal gaze holding**.

**Each child is a leaf.** The two nucleus modules are **single
structures** — they have **no structural children** of their
own. Consumers that need **nucleus-level** resolution descend
into one of the two leaves; consumers that need **side-level**
resolution use this container as a whole; consumers that need
**bilateral** resolution iterate over both ``left`` and
``right``.

The Right Perihypoglossal Nuclei / Left Perihypoglossal Nuclei Boundary
-----------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right perihypoglossal nuclei container** (this module) — the
    perihypoglossal nuclei of the **right** medulla.

*   **Left perihypoglossal nuclei container**
    (``.../perihypoglossal_nuclei/left/``) — the
    perihypoglossal nuclei of the **left** medulla.

**The two are the SIDES of the bilateral
perihypoglossal_nuclei container.** They are **structurally
symmetric mirror pairs** — same two leaf nuclei, same
cytoarchitecture, same projections (with some crossed
components), same functions. Consumers must **not** conflate the
right container with the left — resolve the left side via
``perihypoglossal_nuclei.left``.

The Right Perihypoglossal Nuclei / Right Hypoglossal Nucleus Boundary
---------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Right perihypoglossal nuclei container** (this module) — the
    **right oculomotor** nuclei that **surround** the right
    hypoglossal nucleus.

*   **Right hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **right somatic motor** nucleus for the **tongue**.

**They share the name "hypoglossal" but are DIFFERENT STRUCTURES
in DIFFERENT CONTAINERS with DIFFERENT FUNCTIONS** — the **right
hypoglossal nucleus** is **motor** (tongue); the **right
perihypoglossal nuclei** are **oculomotor** (gaze). Consumers
must **not** conflate the two.

The Right Perihypoglossal Nuclei / Right Nucleus of Roller Boundary
-------------------------------------------------------------------
This is the **sometimes-grouped** boundary:

*   **Right perihypoglossal nuclei container** (this module) — the
    **right intercalated nucleus** and **right prepositus
    nucleus**.

*   **Right nucleus of Roller** — a **small medullary nucleus**
    sometimes grouped with the PHN in the literature, **NOT**
    wired in this tree.

**The right nucleus of Roller is NOT wired** as a structural
child of the right perihypoglossal nuclei container. Consumers
must **not** expect to find it here — resolve it via the
references.

The Right Perihypoglossal Nuclei / Right Abducens Nucleus and Right PPRF Boundary
--------------------------------------------------------------------------------
This is the **gaze-holding / gaze-generating** boundary:

*   **Right perihypoglossal nuclei container** (this module) — the
    **right medullary** oculomotor nuclei.

*   **Right abducens nucleus**
    (``.../metencephalon/pons/cranial_nerve_nuclei/right/abducens_nucleus/``)
    and **right PPRF**
    (``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/right/``)
    — the **right pontine** horizontal **saccade generators**.

**They are functionally coupled** but **anatomically distinct**.
Consumers must **not** conflate the two.

The Right Perihypoglossal Nuclei / Right Vestibular Nuclei and MLF Boundary
---------------------------------------------------------------------------
This is the **gaze-holding / VOR-and-MLF** boundary:

*   **Right perihypoglossal nuclei container** (this module) — the
    **right medullary** oculomotor nuclei.

*   **Right vestibular nuclei**
    (``.../metencephalon/pons/cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **right VOR relay**.

*   **MLF** — the **white-matter tract** that **connects**
    oculomotor structures.

**They are functionally coupled** but **anatomically distinct**.
Consumers must **not** conflate the two.

The Right Perihypoglossal Nuclei / Other Right Medullary Structures Boundary
----------------------------------------------------------------------------
This is the **oculomotor / non-oculomotor** boundary:

*   **Right perihypoglossal nuclei container** (this module) — the
    **right medullary oculomotor** nuclei.

*   **Right nucleus ambiguus, right solitary nucleus, right
    dorsal motor nucleus of the vagus, right medullary pyramid,
    right olivary body, right arcuate nucleus, right parafacial
    zone, right paramedian reticular nucleus, right respiratory
    centers** — **other right medullary structures**.

**Each is a DIFFERENT STRUCTURE.** Consumers must **not** conflate
the **right perihypoglossal nuclei** with any of these.

Function in the Human Brain
---------------------------
The right perihypoglossal nuclei container's function is
**oculomotor** — **gaze holding** (right prepositus nucleus) and
**vertical gaze integration** (right intercalated nucleus) —
**NOT motor conduction**, **NOT tongue motor control**, and
**NOT autonomic regulation**:

*   **Horizontal gaze holding (right prepositus nucleus):** The
    **right prepositus nucleus** is the **right neural
    integrator** for **horizontal gaze** — it **holds** the
    **right-side horizontal gaze** position after a **saccade**.

*   **Vertical gaze integration (right intercalated nucleus):**
    The **right intercalated nucleus** is involved in **vertical
    gaze** integration and **vertical vestibulo-ocular reflex**
    processing.

*   **Vestibulo-ocular integration (right side):** Both the
    **right prepositus nucleus** and the **right intercalated
    nucleus** **integrate** **vestibular** signals with
    **oculomotor** commands.

*   **NOT motor conduction:** The **right perihypoglossal
    nuclei** do **not** send motor axons to muscles.

*   **NOT tongue motor control:** The **tongue motor control**
    is the **right hypoglossal nucleus** — **NOT** the right
    perihypoglossal nuclei.

*   **NOT autonomic regulation:** The **right perihypoglossal
    nuclei** do **not** regulate autonomic function.

**The unifying theme:** the right perihypoglossal nuclei are the
**right medullary oculomotor nuclei** that **surround** the right
hypoglossal nucleus — they **hold gaze** (right prepositus
nucleus) and **integrate vertical gaze** (right intercalated
nucleus), and they **participate** in the **horizontal and
vertical VOR**.

Associated Disorders
--------------------
The right perihypoglossal nuclei container is the **substrate**
for **well-defined clinical syndromes** — its clinical relevance
is **direct**, via **gaze-holding** and **vestibulo-ocular**
dysfunction:

*   **Gaze-evoked nystagmus (via right prepositus nucleus
    dysfunction):** **Impaired** horizontal **gaze holding** on
    the **right side** — the **right prepositus nucleus** is
    the **right neural integrator**; its **dysfunction** causes
    **gaze-evoked nystagmus**. This is a **cardinal**
    brainstem/cerebellar sign.

*   **Vertical gaze palsy / vertical gaze-evoked nystagmus (via
    right intercalated nucleus dysfunction):** **Impaired**
    vertical **gaze holding** or **vertical saccades** — from
    **right intercalated nucleus** dysfunction. This is **less
    well characterized** than horizontal gaze-holding failure.

*   **Wernicke encephalopathy (via right PHN involvement):**
    **Wernicke encephalopathy** (thiamine deficiency)
    **typically** involves the **medial vestibular nuclei** and
    the **right perihypoglossal nuclei** — producing
    **nystagmus**, **gaze-evoked nystagmus**, and **gaze palsy**
    in addition to the **classic triad** (ophthalmoplegia,
    ataxia, confusion). The **right perihypoglossal nuclei** are
    a **direct substrate** of the **oculomotor** findings in
    Wernicke encephalopathy.

*   **Brainstem stroke (via right PHN involvement):** **Right
    medullary** **stroke** can **involve** the **right
    perihypoglossal nuclei** or their **connections** —
    contributing to **nystagmus** and **gaze-holding**
    abnormalities.

*   **No Named "Right Perihypoglossal Nuclei Syndrome":** The
    right perihypoglossal nuclei are a **small nuclear complex**
    — their clinical syndromes are **named for the broader
    brainstem/cerebellar lesion** or the **oculomotor sign**,
    **not** for the nuclei themselves.

**What is NOT here:** The right perihypoglossal nuclei are **not**
the substrate for **tongue weakness** (right hypoglossal
nucleus), **motor weakness** (right corticospinal tract — **NOT**
in this container), **sensory loss** (right medial lemniscus,
right spinothalamic tract — **NOT** in this container),
**autonomic dysfunction** (right RVLM, right CVLM, right NTS —
**NOT** in this container), or **respiratory rhythm** (right
VRG, right DRG — **NOT** in this container). Their clinical
relevance is the **gaze-holding** and **VOR** functions listed
above.

Lateralization Notes
--------------------
This is the **right** perihypoglossal nuclei container. The
perihypoglossal nuclei are a **bilateral container** whose two
sides are **structurally symmetric mirror pairs** — and it
carries **NO warning**:

*   **Bilateral Symmetry:** The **right** and **left**
    perihypoglossal nuclei are **structurally symmetric** — they
    are **mirror pairs** with the **same** two leaf nuclei,
    **same** cytoarchitecture, **same** projections, and **same**
    functions.

*   **Partly Crossed Projections:** Some **PHN** projections are
    **ipsilateral** (e.g., **right prepositus → right
    abducens/vestibular nuclei**) and some are **crossed** (via
    the **MLF** and **other** commissural pathways). The **PHN**
    functions **bilaterally** in **gaze holding** — a
    **unilateral** lesion can cause **bilateral**
    **gaze-evoked nystagmus**.

*   **NO Lateralization Warning:** The perihypoglossal nuclei
    have **no known functional lateralization** in humans.
    Consumers must **not** import a **lateralization warning**
    into the right perihypoglossal nuclei — the **right** and
    **left** sides are **functionally symmetric** at the
    **nucleus level**.

*   **NO Extended-Amygdala / SLEA Warning:** The right
    perihypoglossal nuclei are **SLEA-free** — they are **not**
    an extended-amygdala component. Consumers must **not** import
    the SLEA warning into the right perihypoglossal nuclei.

*   **NO Fear-Output Warning:** The right perihypoglossal nuclei
    are **not** a fear-output structure — they are **right
    medullary oculomotor** nuclei. Consumers must **not**
    conflate them with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "right perihypoglossal nuclei = left
perihypoglossal nuclei" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**nucleus level**. The perihypoglossal nuclei are a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right perihypoglossal
    nuclei container is a **container** — it does **not** import
    from ``.../left/`` or any other left-side module.
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
    The right perihypoglossal nuclei's relationships to the
    right hypoglossal nucleus, right nucleus of Roller, right
    abducens nucleus, right PPRF, right vestibular nuclei, MLF,
    right nucleus ambiguus, right solitary nucleus, right
    cranial nerve nuclei, right medullary pyramid, right
    olivary body, right arcuate nucleus, right parafacial zone,
    right paramedian reticular nucleus, and right respiratory
    centers are documented as **prose and boundary data**, not
    as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with two leaf children.** The structural
    children are the two nuclei — each a **leaf**. Consumers
    **should** descend into them for **nucleus-level**
    resolution.
*   **NOT the left perihypoglossal nuclei container.** The left
    container is a **separate module** under
    ``.../perihypoglossal_nuclei/left/``. Consumers must **not**
    conflate the right container with the left.
*   **NOT the parent perihypoglossal_nuclei container.** The
    parent is the **unpaired bilateral container**; the **right**
    module is **one side** of it.
*   **OCULOMOTOR, NOT motor.** The **right hypoglossal nucleus**
    is **NOT** in this container. The right perihypoglossal
    nuclei are **oculomotor** — **NOT** tongue motor.
*   **NOT the right nucleus of Roller.** The nucleus of Roller is
    **sometimes grouped** with the PHN in the literature but is
    **NOT wired** in this tree.
*   **NOT the right abducens nucleus, right PPRF, right
    vestibular nuclei, or MLF.** Those are **different
    structures**.
*   **NOT the right nucleus ambiguus, right solitary nucleus,
    right dorsal motor nucleus of the vagus, right medullary
    pyramid, right olivary body, right arcuate nucleus, right
    parafacial zone, right paramedian reticular nucleus, or
    right respiratory centers.** Each is a **different
    structure**.
*   **No ``AREA_PATHS`` hop.** The right perihypoglossal nuclei
    container is a **local container** — it is not cross-listed
    under another brainparts path.
*   **No nested cross-listing.** The right perihypoglossal
    nuclei container has no nested dual-framing module. It is a
    **container** with **two leaf children**.
*   **Structural parity with the left perihypoglossal nuclei
    container — strict mirror with NO warning.** The right and
    left containers are **structurally identical** — same two
    leaf children, same **oculomotor** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "perihypoglossal_nuclei.right"
    )

**Do not** expect the two nuclei to be wired directly under
``perihypoglossal_nuclei``. The **left** and **right** containers
are **intermediate** — the two nuclei are leaf children of those
containers. Resolve them via
``perihypoglossal_nuclei.right.<nucleus>``.

**Do not** assume the right perihypoglossal nuclei container is
the **left perihypoglossal nuclei container**. The left container
is the **separate module** at
``.../perihypoglossal_nuclei/left/``.

**Do not** assume the right perihypoglossal nuclei container is
the **right hypoglossal nucleus**. They **surround** the right
hypoglossal nucleus ("peri-" = "around") but are **separate
structures** — the right hypoglossal nucleus is **motor**
(tongue); the right perihypoglossal nuclei are **oculomotor**
(gaze).

**Do not** assume the right perihypoglossal nuclei container is
the **right nucleus of Roller**. The nucleus of Roller is
**sometimes grouped** with the PHN in the literature but is
**NOT wired** in this tree.

**Do not** assume the right perihypoglossal nuclei container is
the **right abducens nucleus**, **right PPRF**, **right
vestibular nuclei**, or **MLF**. Those are **different
structures**.

**Do not** assume the right perihypoglossal nuclei container is
the **right nucleus ambiguus**, **right solitary nucleus**,
**right dorsal motor nucleus of the vagus**, **right medullary
pyramid**, **right olivary body**, **right arcuate nucleus**,
**right parafacial zone**, **right paramedian reticular
nucleus**, or **right respiratory centers**. Each is a
**different structure**.

Iterating the right perihypoglossal nuclei container's structural
children (recommended consumer pattern)::

    RIGHT_PERIHYPOGLOSSAL_NUCLEI_CHILDREN = (
        "intercalated_nucleus",
        "prepositus_nucleus",
    )
    # Each child is a leaf module representing the right side of
    # one of the two perihypoglossal nuclei.

Reaching the two right nuclei (recommended consumer pattern)::

    # The two right nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right.intercalated_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right.prepositus_nucleus
    #
    # Each is a leaf module representing the RIGHT side of that
    # nucleus.

Reaching the left perihypoglossal nuclei container (recommended
consumer pattern — the contralateral container)::

    # The left perihypoglossal nuclei container is the
    # CONTRALATERAL container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left
    #
    # The right and left containers are structurally symmetric
    # mirror pairs with the same two leaf nuclei.

Reaching the right hypoglossal nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The right hypoglossal nucleus is a MOTOR nucleus, NOT part
    # of the right perihypoglossal nuclei:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.hypoglossal_nucleus
    #
    # The right perihypoglossal nuclei SURROUND the right
    # hypoglossal nucleus ("peri-" = "around") but are SEPARATE
    # structures with DIFFERENT functions.

Reaching the right abducens nucleus and right PPRF (recommended
consumer pattern — NOTE the DIFFERENT containers)::

    # The right abducens nucleus and right PPRF are PONTINE
    # structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.abducens_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.paramedian_pontine_reticular_formation.right
    #
    # They are functionally coupled with the right prepositus
    # nucleus (right PPRF drives the saccade; right prepositus
    # holds gaze) but are anatomically distinct.

Reaching the right vestibular nuclei (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The right vestibular nuclei are PONTOMEDULLARY structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.vestibulocochlear_nuclei.vestibular_nuclei
    #
    # They are functionally coupled with the right
    # perihypoglossal nuclei in the VOR — but they are DIFFERENT
    # structures.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        for nucleus in RIGHT_PERIHYPOGLOSSAL_NUCLEI_CHILDREN:
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