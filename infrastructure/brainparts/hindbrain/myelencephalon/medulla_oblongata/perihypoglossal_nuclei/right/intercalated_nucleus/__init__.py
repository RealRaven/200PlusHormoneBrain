"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right.intercalated_nucleus
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── perihypoglossal_nuclei
                └── right
                    └── intercalated_nucleus   <-- THIS MODULE

**Primary synonym:** Right intercalated nucleus; right nucleus
intercalatus; right nucleus intercalatus of Staderini; right
Staderini's nucleus; right nucleus of Staderini.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** in the **right dorsal medulla
oblongata** — a **small oculomotor nucleus** that lies
**between** the **right hypoglossal nucleus** (medial) and the
**right dorsal motor nucleus of the vagus** (lateral), **ventral**
to the **right area postrema** and the **floor of the fourth
ventricle**. It is involved in **vertical gaze** and
**vestibulo-ocular** integration. It is **NOT** the **right
hypoglossal nucleus** — the hypoglossal nucleus is the
**somatic motor** nucleus for the **tongue**; the **right
intercalated nucleus** is an **oculomotor** structure. It is
**NOT** the **right prepositus nucleus** — which is the **neural
integrator** for **horizontal gaze holding**; the **intercalated
nucleus** is more involved in **vertical gaze**. It is **NOT**
the **right nucleus of Roller** — a **small medullary nucleus**
sometimes grouped with the perihypoglossal complex but **NOT
wired** in this tree.
**Part of:** The **right perihypoglossal nuclei container**
(``.../perihypoglossal_nuclei/right/``) — which is part of the
**perihypoglossal_nuclei** bilateral container — which is part
of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../perihypoglossal_nuclei/right/`` →
**direct child** of the right perihypoglossal nuclei container.
**Structural children:** **None.** This is a **leaf** module. The
right intercalated nucleus is represented as a **single
structure** — it has **no structural children** of its own.
**Boundary status (NOT the left intercalated nucleus — the
contralateral leaf):** **Boundary case — the right intercalated
nucleus is NOT the left intercalated nucleus.** The **left
intercalated nucleus**
(``.../perihypoglossal_nuclei/left/intercalated_nucleus/``) is
the **contralateral leaf** — the intercalated nucleus of the
**left** medulla. **They are DIFFERENT LEAVES** — the ``left``
and ``right`` modules are the two sides of the **bilateral
parent container**. Consumers must **not** conflate the **right**
intercalated nucleus with the **left** — resolve the left side
via
``perihypoglossal_nuclei.left.intercalated_nucleus``.
**Boundary status (NOT the right prepositus nucleus — a SIBLING
within the same right perihypoglossal complex):** **Boundary
case — the right intercalated nucleus is NOT the right
prepositus nucleus.** The **right prepositus nucleus**
(``.../perihypoglossal_nuclei/right/prepositus_nucleus/``) is a
**sibling leaf** in the right perihypoglossal complex — it is
the **neural integrator** for **horizontal gaze holding**, and
it is a **separate structure** with a **different function**.
The **right intercalated nucleus** (here) is more involved in
**vertical gaze** and **vertical vestibulo-ocular**
integration. **They are DIFFERENT NUCLEI** — both are members of
the **right perihypoglossal complex**, but they are **not
interchangeable**. Consumers must **not** conflate the two.
**Boundary status (NOT the right hypoglossal nucleus — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the right intercalated nucleus is NOT the right hypoglossal
nucleus.** The **right hypoglossal nucleus**
(``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is
the **right somatic motor** nucleus for the **tongue** — it is
**medial** to the right intercalated nucleus. The **right
intercalated nucleus** (here) is a **right oculomotor** nucleus
— it is **lateral** to the right hypoglossal nucleus and
**involved in vertical gaze**. **They are DIFFERENT STRUCTURES**
— the **hypoglossal nucleus** is **motor** (tongue); the
**intercalated nucleus** is **oculomotor** (gaze). Consumers
must **not** conflate the two.
**Boundary status (NOT the right nucleus of Roller — sometimes
grouped but NOT in this tree):** **Boundary case — the right
intercalated nucleus is NOT the right nucleus of Roller.** The
**nucleus of Roller** is **sometimes grouped** with the
perihypoglossal complex in the literature — it lies **ventral
and lateral** to the **hypoglossal nucleus** and is **sometimes
considered adjacent** to the intercalated nucleus. In **this
tree**, the nucleus of Roller is **NOT wired** — only the
**intercalated nucleus** and the **prepositus nucleus** are.
Consumers must **not** expect to find the nucleus of Roller
under ``intercalated_nucleus`` — resolve it via the references.
**Boundary status (NOT the right dorsal motor nucleus of the
vagus — a DIFFERENT structure):** **Boundary case — the right
intercalated nucleus is NOT the right dorsal motor nucleus of
the vagus.** The **right dorsal motor nucleus of the vagus**
(``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
is the **right parasympathetic** nucleus for the **thoracic and
abdominal viscera** — it is **lateral** to the right
intercalated nucleus. The **right intercalated nucleus** (here)
is a **right oculomotor** nucleus. **They are DIFFERENT
STRUCTURES** — the **dorsal motor nucleus of the vagus** is
**parasympathetic**; the **intercalated nucleus** is
**oculomotor**. Consumers must **not** conflate the two.
**Boundary status (NOT the right area postrema or right
chemoreceptor trigger zone — circumventricular structures):**
**Boundary case — the right intercalated nucleus is NOT the
right area postrema or the right chemoreceptor trigger zone.**
The **right area postrema** and **right chemoreceptor trigger
zone** are **circumventricular organs** at the **caudal floor of
the fourth ventricle** — they are **sensory / chemosensory**
structures that trigger **vomiting**. They are **dorsal** to
the right intercalated nucleus. The **right intercalated
nucleus** (here) is an **oculomotor** nucleus — **NOT** a
circumventricular organ. Consumers must **not** conflate the
two.
**Boundary status (NOT the right solitary nucleus — a visceral
afferent relay):** **Boundary case — the right intercalated
nucleus is NOT the right solitary nucleus.** The **right
solitary nucleus (NTS)** (``.../solitary_nucleus/right/``) is
the **right visceral afferent relay** — it is a **sensory**
nucleus, **lateral and ventral** to the right intercalated
nucleus. The **right intercalated nucleus** (here) is an
**oculomotor** nucleus. Consumers must **not** conflate the two.
**Boundary status (NOT the right abducens nucleus or right
PPRF — PONTINE structures):** **Boundary case — the right
intercalated nucleus is NOT the right abducens nucleus or right
PPRF.** The **right abducens nucleus**
(``.../metencephalon/pons/cranial_nerve_nuclei/right/abducens_nucleus/``)
and **right PPRF**
(``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/right/``)
are **pontine horizontal saccade generators**. The **right
intercalated nucleus** (here) is a **medullary oculomotor**
nucleus — more involved in **vertical gaze**. **They are
anatomically distinct** — the **abducens nucleus** and **PPRF**
are **pontine**; the **intercalated nucleus** is **medullary**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right vestibular nuclei — a
DIFFERENT medullary region):** **Boundary case — the right
intercalated nucleus is NOT the right vestibular nuclei.** The
**right vestibular nuclei**
(``.../metencephalon/pons/cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
are **pontomedullary** structures that **receive** vestibular
afferents. The **right intercalated nucleus** (here) is a
**medullary oculomotor** nucleus that **participates** in
**vestibulo-ocular** integration — it is **functionally
coupled** with the vestibular nuclei but **anatomically
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the MLF — a white-matter tract):**
**Boundary case — the right intercalated nucleus is NOT the
medial longitudinal fasciculus (MLF).** The **MLF** is a
**white-matter tract** that **connects** the **abducens
nucleus** to the **contralateral oculomotor nucleus** (for
**horizontal gaze**) and **connects** the **vestibular nuclei**
to the **oculomotor/trochlear nuclei** (for the **VOR**). The
**right intercalated nucleus** (here) is a **grey-matter
nucleus** — it **projects** to the **oculomotor** structures
**via** the **MLF** and **other pathways**, but it is **NOT**
the MLF. Consumers must **not** conflate the **nucleus** with
the **white-matter tract**.
**Boundary status (NOT the right nucleus ambiguus — a
branchial-motor structure):** **Boundary case — the right
intercalated nucleus is NOT the right nucleus ambiguus.** The
**right nucleus ambiguus**
(``.../cranial_nerve_nuclei/right/nucleus_ambiguus/``) is a
**right branchial motor** nucleus in the **ventrolateral
medulla** — it supplies the **striated muscles of the pharynx
and larynx**. The **right intercalated nucleus** (here) is a
**right oculomotor** nucleus in the **dorsal medulla**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right prepositus nucleus, right
medullary pyramid, right olivary body, right arcuate nucleus,
right parafacial zone, right paramedian reticular nucleus, right
RVLM, right CVLM, or right respiratory centers — DIFFERENT
structures):** **Boundary case — the right intercalated nucleus
is NOT these other right medullary structures.** Each is a
**different structure** — see the respective modules.
Consumers must **not** conflate the **right intercalated
nucleus** with any of these.
**Boundary status (NOT the whole right perihypoglossal complex —
a COMPONENT of it):** **Boundary case — the right intercalated
nucleus is NOT the whole right perihypoglossal complex.** The
**right perihypoglossal complex**
(``.../perihypoglossal_nuclei/right/``) is a **container** that
**contains** the right intercalated nucleus (here) **plus** the
right prepositus nucleus. The **right intercalated nucleus** is
**one component** — the **vertical gaze** component — of the
right perihypoglossal complex. Consumers must **not** conflate
the **component** with the **whole right perihypoglossal
complex**.

Overview
--------
The **right intercalated nucleus** (nucleus intercalatus of
Staderini) is a **small grey-matter nucleus** in the **right
dorsal medulla oblongata** — it lies **between** the **right
hypoglossal nucleus** (medial) and the **right dorsal motor
nucleus of the vagus** (lateral), **ventral** to the **right
area postrema** and the **floor of the fourth ventricle**. It is
involved in **vertical gaze** and **vertical vestibulo-ocular**
integration.

**This is a LEAF module.** The **right intercalated nucleus** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **nucleus-level** resolution of
the right intercalated nucleus use this module; consumers that
need the **right prepositus nucleus** use
``.../perihypoglossal_nuclei/right/prepositus_nucleus/``;
consumers that need the **whole right perihypoglossal
container** use ``.../perihypoglossal_nuclei/right/``.

**The right intercalated nucleus is a VERTICAL GAZE /
VESTIBULO-OCULAR nucleus, NOT the horizontal gaze integrator.**
The **horizontal gaze integrator** is the **right prepositus
nucleus** — the **sibling leaf** in the right perihypoglossal
complex. The **right intercalated nucleus** is more involved in
**vertical gaze** and **vertical vestibulo-ocular**
integration. **They are functionally distinct** — the
**prepositus nucleus** is the **"horizontal"** part of the
complex; the **intercalated nucleus** is the **"vertical"** part.

**The right intercalated nucleus is a DORSAL MEDULLARY nucleus,
NOT a ventrolateral or ventral nucleus.** It is **NOT** the
**right hypoglossal nucleus** (medial), **NOT** the **right
dorsal motor nucleus of the vagus** (lateral), **NOT** the
**right solitary nucleus** (lateral and ventral), **NOT** the
**right nucleus ambiguus** (ventrolateral), **NOT** the **right
prepositus nucleus** (adjacent within the same complex), and
**NOT** the **right nucleus of Roller** (sometimes grouped but
**NOT wired** in this tree).

**The right intercalated nucleus is functionally coupled to the
right vestibular nuclei, the right abducens nucleus, the right
PPRF, and the oculomotor/trochlear nuclei.** It
**participates** in the **vertical vestibulo-ocular reflex**
and **vertical gaze** integration — but it is **NOT** the
**vestibular nuclei** themselves, **NOT** the **abducens
nucleus**, **NOT** the **PPRF**, and **NOT** the **MLF**.

The Right Intercalated Nucleus / Left Intercalated Nucleus Boundary
-------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right intercalated nucleus** (this module) — the
    intercalated nucleus of the **right** medulla.

*   **Left intercalated nucleus**
    (``.../perihypoglossal_nuclei/left/intercalated_nucleus/``) —
    the intercalated nucleus of the **left** medulla.

**The two are the SIDES of the bilateral perihypoglossal
complex.** They are **structurally symmetric mirror pairs** —
same cytoarchitecture, same projections (with some crossed
components), same **no warning**. Consumers must **not** conflate
the right with the left — resolve the left side via
``perihypoglossal_nuclei.left.intercalated_nucleus``.

The Right Intercalated Nucleus / Right Prepositus Nucleus Boundary
------------------------------------------------------------------
This is the **vertical gaze / horizontal gaze** boundary
(within the same perihypoglossal complex):

*   **Right intercalated nucleus** (this module) — the **right
    vertical gaze** nucleus.

*   **Right prepositus nucleus**
    (``.../perihypoglossal_nuclei/right/prepositus_nucleus/``) —
    the **right horizontal gaze** neural integrator.

**They are DIFFERENT NUCLEI** — both are members of the **right
perihypoglossal complex**, but they are **functionally distinct**
— the **intercalated nucleus** is **vertical gaze**; the
**prepositus nucleus** is **horizontal gaze holding**.
Consumers must **not** conflate the two.

The Right Intercalated Nucleus / Right Hypoglossal Nucleus Boundary
-------------------------------------------------------------------
This is the **oculomotor / motor** boundary:

*   **Right intercalated nucleus** (this module) — the **right
    oculomotor** nucleus.

*   **Right hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **right somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES** — the **hypoglossal nucleus**
is **motor** (tongue); the **intercalated nucleus** is
**oculomotor** (gaze). They are **adjacent** in the **right
dorsal medulla** (the hypoglossal nucleus is **medial** to the
intercalated nucleus), but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Right Intercalated Nucleus / Right Nucleus of Roller Boundary
-----------------------------------------------------------------
This is the **sometimes-grouped** boundary:

*   **Right intercalated nucleus** (this module) — the **right
    intercalated nucleus of Staderini**.

*   **Right nucleus of Roller** — a **small medullary nucleus**
    sometimes grouped with the perihypoglossal complex in the
    literature, **NOT** wired in this tree.

**The right nucleus of Roller is NOT wired** as a separate module
in this tree — only the **intercalated nucleus** and the
**prepositus nucleus** are. Consumers must **not** expect to find
the nucleus of Roller under ``intercalated_nucleus`` — resolve it
via the references.

The Right Intercalated Nucleus / Right Dorsal Motor Nucleus of the Vagus, Right Area Postrema, Right Solitary Nucleus Boundary
-----------------------------------------------------------------------------------------------------------------------------
This is the **oculomotor / parasympathetic-and-sensory** boundary:

*   **Right intercalated nucleus** (this module) — the **right
    oculomotor** nucleus.

*   **Right dorsal motor nucleus of the vagus**
    (``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
    — the **right parasympathetic** nucleus.

*   **Right area postrema** and **right chemoreceptor trigger
    zone** — **circumventricular organs**.

*   **Right solitary nucleus** (``.../solitary_nucleus/right/``) —
    the **right visceral afferent relay**.

**Each is a DIFFERENT STRUCTURE** with a **DIFFERENT function**.
Consumers must **not** conflate the **right intercalated nucleus**
with any of these.

The Right Intercalated Nucleus / Right Abducens Nucleus, Right PPRF, Right Vestibular Nuclei, and MLF Boundary
-------------------------------------------------------------------------------------------------------------
This is the **medullary-vertical-gaze / pontine-horizontal-gaze-and-VOR** boundary:

*   **Right intercalated nucleus** (this module) — the **right
    medullary vertical gaze** nucleus.

*   **Right abducens nucleus**
    (``.../metencephalon/pons/cranial_nerve_nuclei/right/abducens_nucleus/``)
    and **right PPRF**
    (``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/right/``)
    — the **right pontine horizontal saccade generators**.

*   **Right vestibular nuclei**
    (``.../metencephalon/pons/cranial_nerve_nuclei/right/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **right VOR relay**.

*   **MLF** — the **white-matter tract** that **connects**
    oculomotor structures.

**Each is a DIFFERENT STRUCTURE** in a **DIFFERENT container**.
They are **functionally coupled** in the **gaze** and **VOR**
systems, but the **right intercalated nucleus** is **medullary**
and **vertical-gaze-oriented**, while the **abducens nucleus**
and **PPRF** are **pontine** and **horizontal-gaze-oriented**,
and the **vestibular nuclei** are **pontomedullary** and
**VOR-oriented**. Consumers must **not** conflate the right
intercalated nucleus with any of these.

Function in the Human Brain
---------------------------
The right intercalated nucleus's function is **vertical gaze
integration** and **vertical vestibulo-ocular integration** —
**NOT horizontal gaze holding**, **NOT motor conduction**, and
**NOT autonomic regulation**:

*   **Vertical gaze integration (right side):** The **right
    intercalated nucleus** is involved in **vertical gaze**
    integration — it **participates** in **vertical gaze
    holding** and **vertical saccades**, and it
    **contributes** to the **vertical gaze integrator**
    circuitry. Without a functional **intercalated nucleus**, the
    **vertical gaze holding** is impaired — the **eyes** may
    **drift back** to the **primary position** after a
    **vertical saccade** (vertical gaze-evoked nystagmus), though
    the **vertical gaze integrator** is **more distributed**
    than the **horizontal** one (involving the **interstitial
    nucleus of Cajal** (INC) in the **midbrain**).

*   **Vertical vestibulo-ocular integration:** The **right
    intercalated nucleus** **participates** in the **vertical
    vestibulo-ocular reflex** — it **integrates** **vertical**
    **vestibular** signals with **vertical oculomotor** commands.

*   **Participation in the neural integrator circuitry:** The
    **intercalated nucleus** is **part of** the **distributed
    vertical gaze integrator** — alongside the **interstitial
    nucleus of Cajal** (INC) and the **supraspinal nucleus of
    the MLF**. The **intercalated nucleus** is **NOT** the
    **sole** vertical gaze integrator — it **contributes** to
    the **vertical gaze holding** function.

*   **NOT horizontal gaze holding:** The **horizontal gaze
    holding** is the **right prepositus nucleus** — **NOT** the
    right intercalated nucleus.

*   **NOT motor conduction:** The **right intercalated nucleus**
    does **not** send motor axons to muscles.

*   **NOT autonomic regulation:** The **right intercalated
    nucleus** does **not** regulate autonomic function.

**The unifying theme:** the right intercalated nucleus is a
**right medullary oculomotor nucleus** — it **participates** in
**vertical gaze** integration and **vertical vestibulo-ocular**
integration, **NOT** in **horizontal gaze holding** (that is the
right prepositus nucleus) and **NOT** in **motor** or
**autonomic** function.

Associated Disorders
--------------------
The right intercalated nucleus has **no named clinical syndrome**
of its own — its clinical associations are **indirect**, via
**vertical gaze** and **vestibulo-ocular** dysfunction:

*   **Vertical gaze-evoked nystagmus (via right intercalated
    nucleus dysfunction):** **Impaired** vertical **gaze
    holding** on the **right side** — the **right intercalated
    nucleus** **participates** in **vertical gaze**
    integration; its **dysfunction** **contributes** to
    **vertical gaze-evoked nystagmus**. This is **less well
    characterized** than **horizontal gaze-evoked nystagmus** —
    the **vertical gaze integrator** is **more distributed**
    (involving the **INC** in the midbrain, which is the
    **primary** vertical gaze integrator).

*   **Vertical gaze palsy (via right intercalated nucleus
    dysfunction — partial):** **Impaired** vertical **saccades**
    or **vertical gaze** — from **right intercalated nucleus**
    dysfunction. This is **usually** part of a **broader**
    midbrain/medullary **lesion** — the **INC** in the midbrain
    is the **primary** vertical gaze integrator, and the
    **intercalated nucleus** **contributes** rather than
    **drives** the **vertical gaze** function.

*   **Wernicke encephalopathy (via right intercalated nucleus
    involvement):** **Wernicke encephalopathy** (thiamine
    deficiency) **typically** involves the **medial vestibular
    nuclei** and the **perihypoglossal nuclei** — including the
    **intercalated nucleus**. The **right intercalated nucleus**
    is a **contributing substrate** of the **oculomotor**
    findings in Wernicke encephalopathy, though the **primary**
    findings are usually **nystagmus** and **gaze palsy** (not
    specifically **vertical** gaze palsy).

*   **Brainstem stroke (via right intercalated nucleus
    involvement):** **Right medullary** **stroke** can
    **involve** the **right intercalated nucleus** —
    contributing to **vertical gaze** abnormalities. This is
    **usually** part of a **broader** brainstem syndrome (e.g.,
    Wallenberg syndrome), not an isolated finding.

*   **No Named "Right Intercalated Nucleus Syndrome":** The
    right intercalated nucleus is a **small, functionally
    subtle** nucleus — it has **no named clinical syndrome** of
    its own. Its clinical relevance is **indirect**, via the
    **vertical gaze** and **vestibulo-ocular** functions listed
    above.

**What is NOT here:** The right intercalated nucleus is **not**
the substrate for **horizontal gaze-evoked nystagmus** (right
prepositus nucleus), **tongue weakness** (right hypoglossal
nucleus), **motor weakness** (right corticospinal tract — **NOT**
in this container), **sensory loss** (right medial lemniscus,
right spinothalamic tract — **NOT** in this container), or
**autonomic dysfunction** (right RVLM, right CVLM, right NTS —
**NOT** in this container). Its clinical relevance is the
**vertical gaze** and **vertical VOR** functions listed above.

Lateralization Notes
--------------------
This is the **right** intercalated nucleus module. The
perihypoglossal nuclei are a **bilateral container** whose two
sides are **structurally symmetric mirror pairs** — and it
carries **NO warning**:

*   **Bilateral Symmetry:** The **right** and **left**
    intercalated nuclei are **structurally symmetric** — they
    are **mirror pairs** with the **same** cytoarchitecture,
    **same** projections, and **same** functions.

*   **Partly Crossed Projections:** Some **intercalated
    nucleus** projections are **ipsilateral** and some are
    **crossed** (via the **MLF** and **other** commissural
    pathways). The **intercalated nucleus** functions
    **bilaterally** in **vertical gaze** integration — a
    **unilateral** lesion may **not** produce a **dramatic**
    deficit because the **vertical gaze integrator** is
    **distributed** and **bilateral**.

*   **NO Lateralization Warning:** The intercalated nucleus has
    **no known functional lateralization** in humans. Consumers
    must **not** import a **lateralization warning** into the
    right intercalated nucleus — the **right** and **left**
    nuclei are **functionally symmetric** at the **nucleus
    level**.

*   **NO Extended-Amygdala / SLEA Warning:** The right
    intercalated nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the right intercalated nucleus.

*   **NO Fear-Output Warning:** The right intercalated nucleus is
    **not** a fear-output structure — it is a **right medullary
    oculomotor** nucleus. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "right intercalated nucleus = left
intercalated nucleus" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**nucleus level**. The intercalated nucleus is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right intercalated
    nucleus is a **leaf** — it does **not** import from
    ``.../left/`` or any other left-side module. Bilateral
    relationships are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../cranial_nerve_nuclei/``,
    ``.../solitary_nucleus/``,
    ``.../metencephalon/pons/cranial_nerve_nuclei/``,
    ``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``,
    ``.../medullary_pyramid/``, ``.../olivary_body/``,
    ``.../arcuate_nucleus/``, ``.../parafacial_zone/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../respiratory_center/``,
    ``.../ventral_respiratory_group/``, or any other container.
    The right intercalated nucleus's relationships to the right
    prepositus nucleus, right hypoglossal nucleus, right nucleus
    of Roller, right dorsal motor nucleus of the vagus, right
    area postrema, right chemoreceptor trigger zone, right
    solitary nucleus, right abducens nucleus, right PPRF, right
    vestibular nuclei, MLF, right nucleus ambiguus, right
    medullary pyramid, right olivary body, right arcuate
    nucleus, right parafacial zone, right paramedian reticular
    nucleus, right RVLM, right CVLM, and right respiratory
    centers are documented as **prose and boundary data**, not
    as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right
    intercalated nucleus is a **single structure** — it has
    **no structural children**. Consumers must **not** expect
    further sub-paths under ``.../intercalated_nucleus/``.
*   **NOT the left intercalated nucleus.** The left
    intercalated nucleus is a **separate leaf** under
    ``.../perihypoglossal_nuclei/left/``. Consumers must **not**
    conflate the right with the left.
*   **NOT the right prepositus nucleus.** The right prepositus
    nucleus is a **sibling leaf** in the right perihypoglossal
    complex — it is the **horizontal gaze** integrator, **NOT**
    the vertical gaze nucleus.
*   **NOT the right hypoglossal nucleus.** The right hypoglossal
    nucleus is a **somatic motor** nucleus (tongue) — **NOT**
    the right intercalated nucleus.
*   **NOT the right nucleus of Roller.** The nucleus of Roller
    is **sometimes grouped** with the perihypoglossal complex in
    the literature but is **NOT wired** in this tree.
*   **NOT the right dorsal motor nucleus of the vagus, right
    area postrema, right chemoreceptor trigger zone, or right
    solitary nucleus.** Each is a **different structure**.
*   **NOT the right abducens nucleus, right PPRF, right
    vestibular nuclei, or MLF.** Those are **different
    structures** in **different containers**.
*   **NOT the right nucleus ambiguus, right medullary pyramid,
    right olivary body, right arcuate nucleus, right parafacial
    zone, right paramedian reticular nucleus, right RVLM, right
    CVLM, or right respiratory centers.** Each is a **different
    structure**.
*   **NOT the whole right perihypoglossal complex.** The **right
    perihypoglossal complex**
    (``.../perihypoglossal_nuclei/right/``) contains this
    nucleus **plus** the right prepositus nucleus. Consumers
    must **not** conflate the **component** with the **whole
    complex**.
*   **No ``AREA_PATHS`` hop.** The right intercalated nucleus is
    a **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The right intercalated nucleus
    has no nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the left intercalated nucleus —
    strict mirror with NO warning.** The right and left modules
    are **structurally identical** — same leaf status, same
    **vertical gaze / VOR** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right import intercalated_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "perihypoglossal_nuclei.right.intercalated_nucleus"
    )

**Do not** assume the right intercalated nucleus is the **left
intercalated nucleus**. The left intercalated nucleus is the
**separate leaf** at
``.../perihypoglossal_nuclei/left/intercalated_nucleus/``.

**Do not** assume the right intercalated nucleus is the **right
prepositus nucleus**. The right prepositus nucleus is the
**sibling leaf** — the **horizontal gaze** integrator — **NOT**
the vertical gaze nucleus.

**Do not** assume the right intercalated nucleus is the **right
hypoglossal nucleus**. The right hypoglossal nucleus is a
**somatic motor** nucleus (tongue) — **NOT** the right
intercalated nucleus.

**Do not** assume the right intercalated nucleus is the **right
nucleus of Roller**. The nucleus of Roller is **sometimes
grouped** with the perihypoglossal complex in the literature but
is **NOT wired** in this tree.

**Do not** assume the right intercalated nucleus is the **right
dorsal motor nucleus of the vagus**, **right area postrema**,
**right chemoreceptor trigger zone**, or **right solitary
nucleus**. Each is a **different structure**.

**Do not** assume the right intercalated nucleus is the **right
abducens nucleus**, **right PPRF**, **right vestibular nuclei**,
or **MLF**. Those are **different structures** in **different
containers**.

**Do not** assume the right intercalated nucleus has **structural
children**. It is a **leaf** — it represents the right
intercalated nucleus as a **single structure**.

Iterating the right intercalated nucleus's (empty) children
(recommended consumer pattern)::

    RIGHT_INTERCALATED_NUCLEUS_CHILDREN = ()
    # The right intercalated nucleus is a leaf. It has no
    # structural children.

Reaching the left intercalated nucleus (recommended consumer
pattern — the contralateral leaf)::

    # The left intercalated nucleus is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left.intercalated_nucleus
    #
    # The right and left intercalated nuclei are structurally
    # symmetric mirror pairs.

Reaching the right prepositus nucleus (recommended consumer
pattern — the SIBLING leaf)::

    # The right prepositus nucleus is the SIBLING leaf in the
    # right perihypoglossal complex — the horizontal gaze
    # integrator, NOT the vertical gaze nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right.prepositus_nucleus
    #
    # Both the intercalated nucleus and the prepositus nucleus
    # are members of the right perihypoglossal complex — but
    # they are functionally distinct (vertical vs. horizontal
    # gaze).

Reaching the right hypoglossal nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The right hypoglossal nucleus is a MOTOR nucleus, NOT part
    # of the perihypoglossal complex:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.hypoglossal_nucleus
    #
    # The right intercalated nucleus SURROUNDS the right
    # hypoglossal nucleus ("peri-" = "around") but is a SEPARATE
    # structure with a DIFFERENT function.

Reaching the right abducens nucleus, right PPRF, and right
vestibular nuclei (recommended consumer pattern — NOTE the
DIFFERENT containers)::

    # The right abducens nucleus, right PPRF, and right
    # vestibular nuclei are PONTINE / PONTOMEDULLARY structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.abducens_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.paramedian_pontine_reticular_formation.right
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.vestibulocochlear_nuclei.vestibular_nuclei
    #
    # They are functionally coupled with the right intercalated
    # nucleus in the gaze and VOR systems — but they are
    # DIFFERENT structures.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"perihypoglossal_nuclei.{side}.intercalated_nucleus"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Perihypoglossal nuclei; intercalated nucleus; Staderini's
    nucleus; oculomotor system.)
*   **Intercalated nucleus — oculomotor functions:** Langer,
    T., et al. (1986). "The nucleus intercalatus and the
    nucleus prepositus hypoglossi: their involvement in
    vertical and horizontal eye movements." *Experimental
    Brain Research* 64:325–334. (Intercalated nucleus;
    vertical gaze; vertical VOR; Staderini's nucleus.)
*   **Intercalated nucleus — overview:** Leigh, R.J., Zee,
    D.S. (2015). *The Neurology of Eye Movements*, 5th ed.
    (Perihypoglossal nuclei; intercalated nucleus; vertical
    gaze; vestibulo-ocular integration.)
*   **Vertical gaze integrator — interstitial nucleus of
    Cajal:** Fukushima, K. (1987). "The interstitial nucleus of
    Cajal and its role in the control of movements of head and
    eyes." *Progress in Neurobiology* 29:107–192. (Interstitial
    nucleus of Cajal; vertical gaze integrator — the
    intercalated nucleus contributes to the distributed
    vertical gaze integrator.)
*   **Wernicke encephalopathy — oculomotor findings:** Victor,
    M., et al. (1989). *The Wernicke-Korsakoff Syndrome and
    Related Neurologic Disorders Due to Alcoholism and
    Malnutrition*, 2nd ed. (Wernicke encephalopathy; medial
    vestibular nuclei; perihypoglossal nuclei — including the
    intercalated nucleus; nystagmus.)
*   **Hypoglossal nucleus (contrast — motor):** Lowe, A.A.
    (1980). "The neural regulation of tongue movement."
    *Progress in Neurobiology* 14:273–349. (Hypoglossal
    nucleus; tongue motor — DIFFERENT from the intercalated
    nucleus.)
*   **Prepositus nucleus (contrast — horizontal gaze
    integrator):** Cannon, S.C., Robinson, D.A. (1987). "Loss
    of the neural integrator of the oculomotor system from
    brain stem lesions in monkey." *Journal of
    Neurophysiology* 57:1383–1409. (Prepositus nucleus;
    horizontal gaze integrator — DIFFERENT from the
    intercalated nucleus.)
*   **Abducens nucleus and PPRF (contrast — pontine horizontal
    gaze):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of
    Eye Movements*, 5th ed. (Abducens nucleus; PPRF; horizontal
    saccades — DIFFERENT from the intercalated nucleus.)
*   **Vestibular nuclei (contrast — VOR relay):** Wilson, V.J.,
    Melvill Jones, G. (1979). *Mammalian Vestibular
    Physiology.* (Vestibular nuclei; VOR — DIFFERENT from the
    intercalated nucleus.)
*   NeuroNames — Nucleus intercalatus; FMA — Nucleus
    intercalatus.
"""