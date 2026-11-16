"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left.intercalated_nucleus
======================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── perihypoglossal_nuclei
                └── left
                    └── intercalated_nucleus   <-- THIS MODULE

**Primary synonym:** Left intercalated nucleus; left nucleus
intercalatus; left nucleus intercalatus of Staderini; left
Staderini's nucleus; left nucleus of Staderini.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** in the **left dorsal medulla
oblongata** — a **small oculomotor nucleus** that lies
**between** the **left hypoglossal nucleus** (medial) and the
**left dorsal motor nucleus of the vagus** (lateral), **ventral**
to the **left area postrema** and the **floor of the fourth
ventricle**. It is involved in **vertical gaze** and
**vestibulo-ocular** integration. It is **NOT** the **left
hypoglossal nucleus** — the hypoglossal nucleus is the
**somatic motor** nucleus for the **tongue**; the **left
intercalated nucleus** is an **oculomotor** structure. It is
**NOT** the **left prepositus nucleus** — which is the **neural
integrator** for **horizontal gaze holding**; the **intercalated
nucleus** is more involved in **vertical gaze**. It is **NOT**
the **left nucleus of Roller** — a **small medullary nucleus**
sometimes grouped with the perihypoglossal complex but **NOT
wired** in this tree.
**Part of:** The **left perihypoglossal nuclei container**
(``.../perihypoglossal_nuclei/left/``) — which is part of the
**perihypoglossal_nuclei** bilateral container — which is part
of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../perihypoglossal_nuclei/left/`` →
**direct child** of the left perihypoglossal nuclei container.
**Structural children:** **None.** This is a **leaf** module. The
left intercalated nucleus is represented as a **single
structure** — it has **no structural children** of its own.
**Boundary status (NOT the right intercalated nucleus — the
contralateral leaf):** **Boundary case — the left intercalated
nucleus is NOT the right intercalated nucleus.** The **right
intercalated nucleus**
(``.../perihypoglossal_nuclei/right/intercalated_nucleus/``) is
the **contralateral leaf** — the intercalated nucleus of the
**right** medulla. **They are DIFFERENT LEAVES** — the ``left``
and ``right`` modules are the two sides of the **bilateral
parent container**. Consumers must **not** conflate the **left**
intercalated nucleus with the **right** — resolve the right side
via
``perihypoglossal_nuclei.right.intercalated_nucleus``.
**Boundary status (NOT the left prepositus nucleus — a SIBLING
within the same left perihypoglossal complex):** **Boundary
case — the left intercalated nucleus is NOT the left prepositus
nucleus.** The **left prepositus nucleus**
(``.../perihypoglossal_nuclei/left/prepositus_nucleus/``) is a
**sibling leaf** in the left perihypoglossal complex — it is the
**neural integrator** for **horizontal gaze holding**, and it
is a **separate structure** with a **different function**. The
**left intercalated nucleus** (here) is more involved in
**vertical gaze** and **vertical vestibulo-ocular**
integration. **They are DIFFERENT NUCLEI** — both are members of
the **left perihypoglossal complex**, but they are **not
interchangeable**. Consumers must **not** conflate the two.
**Boundary status (NOT the left hypoglossal nucleus — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the left intercalated nucleus is NOT the left hypoglossal
nucleus.** The **left hypoglossal nucleus**
(``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) is the
**left somatic motor** nucleus for the **tongue** — it is
**medial** to the left intercalated nucleus. The **left
intercalated nucleus** (here) is a **left oculomotor** nucleus
— it is **lateral** to the left hypoglossal nucleus and
**involved in vertical gaze**. **They are DIFFERENT STRUCTURES**
— the **hypoglossal nucleus** is **motor** (tongue); the
**intercalated nucleus** is **oculomotor** (gaze). Consumers
must **not** conflate the two.
**Boundary status (NOT the left nucleus of Roller — sometimes
grouped but NOT in this tree):** **Boundary case — the left
intercalated nucleus is NOT the left nucleus of Roller.** The
**nucleus of Roller** is **sometimes grouped** with the
perihypoglossal complex in the literature — it lies **ventral
and lateral** to the **hypoglossal nucleus** and is **sometimes
considered adjacent** to the intercalated nucleus. In **this
tree**, the nucleus of Roller is **NOT wired** — only the
**intercalated nucleus** and the **prepositus nucleus** are.
Consumers must **not** expect to find the nucleus of Roller
under ``intercalated_nucleus`` — resolve it via the references.
**Boundary status (NOT the left dorsal motor nucleus of the
vagus — a DIFFERENT structure):** **Boundary case — the left
intercalated nucleus is NOT the left dorsal motor nucleus of
the vagus.** The **left dorsal motor nucleus of the vagus**
(``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``)
is the **left parasympathetic** nucleus for the **thoracic and
abdominal viscera** — it is **lateral** to the left
intercalated nucleus. The **left intercalated nucleus** (here)
is a **left oculomotor** nucleus. **They are DIFFERENT
STRUCTURES** — the **dorsal motor nucleus of the vagus** is
**parasympathetic**; the **intercalated nucleus** is
**oculomotor**. Consumers must **not** conflate the two.
**Boundary status (NOT the left area postrema or left
chemoreceptor trigger zone — circumventricular structures):**
**Boundary case — the left intercalated nucleus is NOT the left
area postrema or the left chemoreceptor trigger zone.** The
**left area postrema** and **left chemoreceptor trigger zone**
are **circumventricular organs** at the **caudal floor of the
fourth ventricle** — they are **sensory / chemosensory**
structures that trigger **vomiting**. They are **dorsal** to
the left intercalated nucleus. The **left intercalated nucleus**
(here) is an **oculomotor** nucleus — **NOT** a
circumventricular organ. Consumers must **not** conflate the
two.
**Boundary status (NOT the left solitary nucleus — a visceral
afferent relay):** **Boundary case — the left intercalated
nucleus is NOT the left solitary nucleus.** The **left solitary
nucleus (NTS)** (``.../solitary_nucleus/left/``) is the **left
visceral afferent relay** — it is a **sensory** nucleus,
**lateral and ventral** to the left intercalated nucleus. The
**left intercalated nucleus** (here) is an **oculomotor**
nucleus. Consumers must **not** conflate the two.
**Boundary status (NOT the left abducens nucleus or left PPRF —
PONTINE structures):** **Boundary case — the left intercalated
nucleus is NOT the left abducens nucleus or left PPRF.** The
**left abducens nucleus**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``)
and **left PPRF**
(``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/left/``)
are **pontine horizontal saccade generators**. The **left
intercalated nucleus** (here) is a **medullary oculomotor**
nucleus — more involved in **vertical gaze**. **They are
anatomically distinct** — the **abducens nucleus** and **PPRF**
are **pontine**; the **intercalated nucleus** is **medullary**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left vestibular nuclei — a
DIFFERENT medullary region):** **Boundary case — the left
intercalated nucleus is NOT the left vestibular nuclei.** The
**left vestibular nuclei**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
are **pontomedullary** structures that **receive** vestibular
afferents. The **left intercalated nucleus** (here) is a
**medullary oculomotor** nucleus that **participates** in
**vestibulo-ocular** integration — it is **functionally
coupled** with the vestibular nuclei but **anatomically
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the MLF — a white-matter tract):**
**Boundary case — the left intercalated nucleus is NOT the
medial longitudinal fasciculus (MLF).** The **MLF** is a
**white-matter tract** that **connects** the **abducens
nucleus** to the **contralateral oculomotor nucleus** (for
**horizontal gaze**) and **connects** the **vestibular nuclei**
to the **oculomotor/trochlear nuclei** (for the **VOR**). The
**left intercalated nucleus** (here) is a **grey-matter
nucleus** — it **projects** to the **oculomotor** structures
**via** the **MLF** and **other pathways**, but it is **NOT**
the MLF. Consumers must **not** conflate the **nucleus** with
the **white-matter tract**.
**Boundary status (NOT the left nucleus ambiguus — a
branchial-motor structure):** **Boundary case — the left
intercalated nucleus is NOT the left nucleus ambiguus.** The
**left nucleus ambiguus**
(``.../cranial_nerve_nuclei/left/nucleus_ambiguus/``) is a
**left branchial motor** nucleus in the **ventrolateral
medulla** — it supplies the **striated muscles of the pharynx
and larynx**. The **left intercalated nucleus** (here) is a
**left oculomotor** nucleus in the **dorsal medulla**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left prepositus nucleus, left
medullary pyramid, left olivary body, left arcuate nucleus,
left parafacial zone, left paramedian reticular nucleus, left
RVLM, left CVLM, or left respiratory centers — DIFFERENT
structures):** **Boundary case — the left intercalated nucleus
is NOT these other left medullary structures.** Each is a
**different structure** — see the respective modules.
Consumers must **not** conflate the **left intercalated
nucleus** with any of these.
**Boundary status (NOT the whole left perihypoglossal complex —
a COMPONENT of it):** **Boundary case — the left intercalated
nucleus is NOT the whole left perihypoglossal complex.** The
**left perihypoglossal complex**
(``.../perihypoglossal_nuclei/left/``) is a **container** that
**contains** the left intercalated nucleus (here) **plus** the
left prepositus nucleus. The **left intercalated nucleus** is
**one component** — the **vertical gaze** component — of the
left perihypoglossal complex. Consumers must **not** conflate
the **component** with the **whole left perihypoglossal
complex**.

Overview
--------
The **left intercalated nucleus** (nucleus intercalatus of
Staderini) is a **small grey-matter nucleus** in the **left
dorsal medulla oblongata** — it lies **between** the **left
hypoglossal nucleus** (medial) and the **left dorsal motor
nucleus of the vagus** (lateral), **ventral** to the **left area
postrema** and the **floor of the fourth ventricle**. It is
involved in **vertical gaze** and **vertical vestibulo-ocular**
integration.

**This is a LEAF module.** The **left intercalated nucleus** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **nucleus-level** resolution of
the left intercalated nucleus use this module; consumers that
need the **left prepositus nucleus** use
``.../perihypoglossal_nuclei/left/prepositus_nucleus/``;
consumers that need the **whole left perihypoglossal
container** use ``.../perihypoglossal_nuclei/left/``.

**The left intercalated nucleus is a VERTICAL GAZE /
VESTIBULO-OCULAR nucleus, NOT the horizontal gaze integrator.**
The **horizontal gaze integrator** is the **left prepositus
nucleus** — the **sibling leaf** in the left perihypoglossal
complex. The **left intercalated nucleus** is more involved in
**vertical gaze** and **vertical vestibulo-ocular**
integration. **They are functionally distinct** — the
**prepositus nucleus** is the **"horizontal"** part of the
complex; the **intercalated nucleus** is the **"vertical"** part.

**The left intercalated nucleus is a DORSAL MEDULLARY nucleus,
NOT a ventrolateral or ventral nucleus.** It is **NOT** the
**left hypoglossal nucleus** (medial), **NOT** the **left
dorsal motor nucleus of the vagus** (lateral), **NOT** the
**left solitary nucleus** (lateral and ventral), **NOT** the
**left nucleus ambiguus** (ventrolateral), **NOT** the **left
prepositus nucleus** (adjacent within the same complex), and
**NOT** the **left nucleus of Roller** (sometimes grouped but
**NOT wired** in this tree).

**The left intercalated nucleus is functionally coupled to the
left vestibular nuclei, the left abducens nucleus, the left
PPRF, and the oculomotor/trochlear nuclei.** It **participates**
in the **vertical vestibulo-ocular reflex** and **vertical
gaze** integration — but it is **NOT** the **vestibular
nuclei** themselves, **NOT** the **abducens nucleus**, **NOT**
the **PPRF**, and **NOT** the **MLF**.

The Left Intercalated Nucleus / Right Intercalated Nucleus Boundary
-------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left intercalated nucleus** (this module) — the
    intercalated nucleus of the **left** medulla.

*   **Right intercalated nucleus**
    (``.../perihypoglossal_nuclei/right/intercalated_nucleus/``) —
    the intercalated nucleus of the **right** medulla.

**The two are the SIDES of the bilateral perihypoglossal
complex.** They are **structurally symmetric mirror pairs** —
same cytoarchitecture, same projections (with some crossed
components), same **no warning**. Consumers must **not** conflate
the left with the right — resolve the right side via
``perihypoglossal_nuclei.right.intercalated_nucleus``.

The Left Intercalated Nucleus / Left Prepositus Nucleus Boundary
----------------------------------------------------------------
This is the **vertical gaze / horizontal gaze** boundary
(within the same perihypoglossal complex):

*   **Left intercalated nucleus** (this module) — the **left
    vertical gaze** nucleus.

*   **Left prepositus nucleus**
    (``.../perihypoglossal_nuclei/left/prepositus_nucleus/``) —
    the **left horizontal gaze** neural integrator.

**They are DIFFERENT NUCLEI** — both are members of the **left
perihypoglossal complex**, but they are **functionally distinct**
— the **intercalated nucleus** is **vertical gaze**; the
**prepositus nucleus** is **horizontal gaze holding**.
Consumers must **not** conflate the two.

The Left Intercalated Nucleus / Left Hypoglossal Nucleus Boundary
-----------------------------------------------------------------
This is the **oculomotor / motor** boundary:

*   **Left intercalated nucleus** (this module) — the **left
    oculomotor** nucleus.

*   **Left hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) —
    the **left somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES** — the **hypoglossal nucleus**
is **motor** (tongue); the **intercalated nucleus** is
**oculomotor** (gaze). They are **adjacent** in the **left
dorsal medulla** (the hypoglossal nucleus is **medial** to the
intercalated nucleus), but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Left Intercalated Nucleus / Left Nucleus of Roller Boundary
---------------------------------------------------------------
This is the **sometimes-grouped** boundary:

*   **Left intercalated nucleus** (this module) — the **left
    intercalated nucleus of Staderini**.

*   **Left nucleus of Roller** — a **small medullary nucleus**
    sometimes grouped with the perihypoglossal complex in the
    literature, **NOT** wired in this tree.

**The left nucleus of Roller is NOT wired** as a separate module
in this tree — only the **intercalated nucleus** and the
**prepositus nucleus** are. Consumers must **not** expect to find
the nucleus of Roller under ``intercalated_nucleus`` — resolve it
via the references.

The Left Intercalated Nucleus / Left Dorsal Motor Nucleus of the Vagus, Left Area Postrema, Left Solitary Nucleus Boundary
--------------------------------------------------------------------------------------------------------------------------
This is the **oculomotor / parasympathetic-and-sensory** boundary:

*   **Left intercalated nucleus** (this module) — the **left
    oculomotor** nucleus.

*   **Left dorsal motor nucleus of the vagus**
    (``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``)
    — the **left parasympathetic** nucleus.

*   **Left area postrema** and **left chemoreceptor trigger
    zone** — **circumventricular organs**.

*   **Left solitary nucleus** (``.../solitary_nucleus/left/``) —
    the **left visceral afferent relay**.

**Each is a DIFFERENT STRUCTURE** with a **DIFFERENT function**.
Consumers must **not** conflate the **left intercalated nucleus**
with any of these.

The Left Intercalated Nucleus / Left Abducens Nucleus, Left PPRF, Left Vestibular Nuclei, and MLF Boundary
----------------------------------------------------------------------------------------------------------
This is the **medullary-vertical-gaze / pontine-horizontal-gaze-and-VOR** boundary:

*   **Left intercalated nucleus** (this module) — the **left
    medullary vertical gaze** nucleus.

*   **Left abducens nucleus**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``)
    and **left PPRF**
    (``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/left/``)
    — the **left pontine horizontal saccade generators**.

*   **Left vestibular nuclei**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **left VOR relay**.

*   **MLF** — the **white-matter tract** that **connects**
    oculomotor structures.

**Each is a DIFFERENT STRUCTURE** in a **DIFFERENT container**.
They are **functionally coupled** in the **gaze** and **VOR**
systems, but the **left intercalated nucleus** is **medullary**
and **vertical-gaze-oriented**, while the **abducens nucleus**
and **PPRF** are **pontine** and **horizontal-gaze-oriented**,
and the **vestibular nuclei** are **pontomedullary** and
**VOR-oriented**. Consumers must **not** conflate the left
intercalated nucleus with any of these.

Function in the Human Brain
---------------------------
The left intercalated nucleus's function is **vertical gaze
integration** and **vertical vestibulo-ocular integration** —
**NOT horizontal gaze holding**, **NOT motor conduction**, and
**NOT autonomic regulation**:

*   **Vertical gaze integration (left side):** The **left
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

*   **Vertical vestibulo-ocular integration:** The **left
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
    holding** is the **left prepositus nucleus** — **NOT** the
    left intercalated nucleus.

*   **NOT motor conduction:** The **left intercalated nucleus**
    does **not** send motor axons to muscles.

*   **NOT autonomic regulation:** The **left intercalated
    nucleus** does **not** regulate autonomic function.

**The unifying theme:** the left intercalated nucleus is a
**left medullary oculomotor nucleus** — it **participates** in
**vertical gaze** integration and **vertical vestibulo-ocular**
integration, **NOT** in **horizontal gaze holding** (that is the
left prepositus nucleus) and **NOT** in **motor** or
**autonomic** function.

Associated Disorders
--------------------
The left intercalated nucleus has **no named clinical syndrome**
of its own — its clinical associations are **indirect**, via
**vertical gaze** and **vestibulo-ocular** dysfunction:

*   **Vertical gaze-evoked nystagmus (via left intercalated
    nucleus dysfunction):** **Impaired** vertical **gaze
    holding** on the **left side** — the **left intercalated
    nucleus** **participates** in **vertical gaze**
    integration; its **dysfunction** **contributes** to
    **vertical gaze-evoked nystagmus**. This is **less well
    characterized** than **horizontal gaze-evoked nystagmus** —
    the **vertical gaze integrator** is **more distributed**
    (involving the **INC** in the midbrain, which is the
    **primary** vertical gaze integrator).

*   **Vertical gaze palsy (via left intercalated nucleus
    dysfunction — partial):** **Impaired** vertical **saccades**
    or **vertical gaze** — from **left intercalated nucleus**
    dysfunction. This is **usually** part of a **broader**
    midbrain/medullary **lesion** — the **INC** in the midbrain
    is the **primary** vertical gaze integrator, and the
    **intercalated nucleus** **contributes** rather than
    **drives** the **vertical gaze** function.

*   **Wernicke encephalopathy (via left intercalated nucleus
    involvement):** **Wernicke encephalopathy** (thiamine
    deficiency) **typically** involves the **medial vestibular
    nuclei** and the **perihypoglossal nuclei** — including the
    **intercalated nucleus**. The **left intercalated nucleus**
    is a **contributing substrate** of the **oculomotor**
    findings in Wernicke encephalopathy, though the **primary**
    findings are usually **nystagmus** and **gaze palsy** (not
    specifically **vertical** gaze palsy).

*   **Brainstem stroke (via left intercalated nucleus
    involvement):** **Left medullary** **stroke** can
    **involve** the **left intercalated nucleus** —
    contributing to **vertical gaze** abnormalities. This is
    **usually** part of a **broader** brainstem syndrome (e.g.,
    Wallenberg syndrome), not an isolated finding.

*   **No Named "Left Intercalated Nucleus Syndrome":** The left
    intercalated nucleus is a **small, functionally subtle**
    nucleus — it has **no named clinical syndrome** of its own.
    Its clinical relevance is **indirect**, via the **vertical
    gaze** and **vestibulo-ocular** functions listed above.

**What is NOT here:** The left intercalated nucleus is **not** the
substrate for **horizontal gaze-evoked nystagmus** (left
prepositus nucleus), **tongue weakness** (left hypoglossal
nucleus), **motor weakness** (left corticospinal tract — **NOT**
in this container), **sensory loss** (left medial lemniscus,
left spinothalamic tract — **NOT** in this container), or
**autonomic dysfunction** (left RVLM, left CVLM, left NTS —
**NOT** in this container). Its clinical relevance is the
**vertical gaze** and **vertical VOR** functions listed above.

Lateralization Notes
--------------------
This is the **left** intercalated nucleus module. The
perihypoglossal nuclei are a **bilateral container** whose two
sides are **structurally symmetric mirror pairs** — and it
carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right**
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
    left intercalated nucleus — the **left** and **right**
    nuclei are **functionally symmetric** at the **nucleus
    level**.

*   **NO Extended-Amygdala / SLEA Warning:** The left
    intercalated nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the left intercalated nucleus.

*   **NO Fear-Output Warning:** The left intercalated nucleus is
    **not** a fear-output structure — it is a **left medullary
    oculomotor** nucleus. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left intercalated nucleus = right
intercalated nucleus" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**nucleus level**. The intercalated nucleus is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left intercalated
    nucleus is a **leaf** — it does **not** import from
    ``.../right/`` or any other right-side module. Bilateral
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
    The left intercalated nucleus's relationships to the left
    prepositus nucleus, left hypoglossal nucleus, left nucleus
    of Roller, left dorsal motor nucleus of the vagus, left
    area postrema, left chemoreceptor trigger zone, left
    solitary nucleus, left abducens nucleus, left PPRF, left
    vestibular nuclei, MLF, left nucleus ambiguus, left
    medullary pyramid, left olivary body, left arcuate nucleus,
    left parafacial zone, left paramedian reticular nucleus,
    left RVLM, left CVLM, and left respiratory centers are
    documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left
    intercalated nucleus is a **single structure** — it has
    **no structural children**. Consumers must **not** expect
    further sub-paths under ``.../intercalated_nucleus/``.
*   **NOT the right intercalated nucleus.** The right
    intercalated nucleus is a **separate leaf** under
    ``.../perihypoglossal_nuclei/right/``. Consumers must **not**
    conflate the left with the right.
*   **NOT the left prepositus nucleus.** The left prepositus
    nucleus is a **sibling leaf** in the left perihypoglossal
    complex — it is the **horizontal gaze** integrator, **NOT**
    the vertical gaze nucleus.
*   **NOT the left hypoglossal nucleus.** The left hypoglossal
    nucleus is a **somatic motor** nucleus (tongue) — **NOT**
    the left intercalated nucleus.
*   **NOT the left nucleus of Roller.** The nucleus of Roller is
    **sometimes grouped** with the perihypoglossal complex in
    the literature but is **NOT wired** in this tree.
*   **NOT the left dorsal motor nucleus of the vagus, left area
    postrema, left chemoreceptor trigger zone, or left solitary
    nucleus.** Each is a **different structure**.
*   **NOT the left abducens nucleus, left PPRF, left vestibular
    nuclei, or MLF.** Those are **different structures** in
    **different containers**.
*   **NOT the left nucleus ambiguus, left medullary pyramid,
    left olivary body, left arcuate nucleus, left parafacial
    zone, left paramedian reticular nucleus, left RVLM, left
    CVLM, or left respiratory centers.** Each is a **different
    structure**.
*   **NOT the whole left perihypoglossal complex.** The **left
    perihypoglossal complex** (``.../perihypoglossal_nuclei/left/``)
    contains this nucleus **plus** the left prepositus nucleus.
    Consumers must **not** conflate the **component** with the
    **whole complex**.
*   **No ``AREA_PATHS`` hop.** The left intercalated nucleus is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The left intercalated nucleus
    has no nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the right intercalated nucleus —
    strict mirror with NO warning.** The left and right modules
    are **structurally identical** — same leaf status, same
    **vertical gaze / VOR** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left import intercalated_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "perihypoglossal_nuclei.left.intercalated_nucleus"
    )

**Do not** assume the left intercalated nucleus is the **right
intercalated nucleus**. The right intercalated nucleus is the
**separate leaf** at
``.../perihypoglossal_nuclei/right/intercalated_nucleus/``.

**Do not** assume the left intercalated nucleus is the **left
prepositus nucleus**. The left prepositus nucleus is the
**sibling leaf** — the **horizontal gaze** integrator — **NOT**
the vertical gaze nucleus.

**Do not** assume the left intercalated nucleus is the **left
hypoglossal nucleus**. The left hypoglossal nucleus is a
**somatic motor** nucleus (tongue) — **NOT** the left
intercalated nucleus.

**Do not** assume the left intercalated nucleus is the **left
nucleus of Roller**. The nucleus of Roller is **sometimes
grouped** with the perihypoglossal complex in the literature but
is **NOT wired** in this tree.

**Do not** assume the left intercalated nucleus is the **left
dorsal motor nucleus of the vagus**, **left area postrema**,
**left chemoreceptor trigger zone**, or **left solitary
nucleus**. Each is a **different structure**.

**Do not** assume the left intercalated nucleus is the **left
abducens nucleus**, **left PPRF**, **left vestibular nuclei**,
or **MLF**. Those are **different structures** in **different
containers**.

**Do not** assume the left intercalated nucleus has **structural
children**. It is a **leaf** — it represents the left
intercalated nucleus as a **single structure**.

Iterating the left intercalated nucleus's (empty) children
(recommended consumer pattern)::

    LEFT_INTERCALATED_NUCLEUS_CHILDREN = ()
    # The left intercalated nucleus is a leaf. It has no
    # structural children.

Reaching the right intercalated nucleus (recommended consumer
pattern — the contralateral leaf)::

    # The right intercalated nucleus is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right.intercalated_nucleus
    #
    # The left and right intercalated nuclei are structurally
    # symmetric mirror pairs.

Reaching the left prepositus nucleus (recommended consumer
pattern — the SIBLING leaf)::

    # The left prepositus nucleus is the SIBLING leaf in the
    # left perihypoglossal complex — the horizontal gaze
    # integrator, NOT the vertical gaze nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left.prepositus_nucleus
    #
    # Both the intercalated nucleus and the prepositus nucleus
    # are members of the left perihypoglossal complex — but they
    # are functionally distinct (vertical vs. horizontal gaze).

Reaching the left hypoglossal nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The left hypoglossal nucleus is a MOTOR nucleus, NOT part
    # of the perihypoglossal complex:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.hypoglossal_nucleus
    #
    # The left intercalated nucleus SURROUNDS the left hypoglossal
    # nucleus ("peri-" = "around") but is a SEPARATE structure
    # with a DIFFERENT function.

Reaching the left abducens nucleus, left PPRF, and left
vestibular nuclei (recommended consumer pattern — NOTE the
DIFFERENT containers)::

    # The left abducens nucleus, left PPRF, and left vestibular
    # nuclei are PONTINE / PONTOMEDULLARY structures:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.abducens_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.paramedian_pontine_reticular_formation.left
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.vestibulocochlear_nuclei.vestibular_nuclei
    #
    # They are functionally coupled with the left intercalated
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