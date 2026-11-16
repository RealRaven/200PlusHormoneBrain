"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left.prepositus_nucleus
====================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── perihypoglossal_nuclei
                └── left
                    └── prepositus_nucleus   <-- THIS MODULE

**Primary synonym:** Left prepositus nucleus; left nucleus
prepositus hypoglossi; left NPH; left nucleus praepositus
hypoglossi; left prepositus hypoglossal nucleus.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** in the **left dorsal medulla
oblongata** — the **neural integrator** for **horizontal gaze
holding**. It lies in the **left perihypoglossal region**, near
the **left hypoglossal nucleus** and the **left medial
longitudinal fasciculus (MLF)**, and it **extends** from the
**left abducens nucleus** level (caudally) to the **left
hypoglossal nucleus** level (rostrally). It is **NOT** the
**left hypoglossal nucleus** — the hypoglossal nucleus is the
**somatic motor** nucleus for the **tongue**; the **left
prepositus nucleus** is an **oculomotor** structure. It is
**NOT** the **left intercalated nucleus** — which is more
involved in **vertical gaze**; the **prepositus nucleus** is the
**horizontal gaze integrator**. It is **NOT** the **left
nucleus of Roller** — a **small medullary nucleus** sometimes
grouped with the perihypoglossal complex but **NOT wired** in
this tree.
**Part of:** The **left perihypoglossal nuclei container**
(``.../perihypoglossal_nuclei/left/``) — which is part of the
**perihypoglossal_nuclei** bilateral container — which is part
of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../perihypoglossal_nuclei/left/`` →
**direct child** of the left perihypoglossal nuclei container.
**Structural children:** **None.** This is a **leaf** module. The
left prepositus nucleus is represented as a **single structure**
— it has **no structural children** of its own.
**Boundary status (NOT the right prepositus nucleus — the
contralateral leaf):** **Boundary case — the left prepositus
nucleus is NOT the right prepositus nucleus.** The **right
prepositus nucleus**
(``.../perihypoglossal_nuclei/right/prepositus_nucleus/``) is
the **contralateral leaf** — the prepositus nucleus of the
**right** medulla. **They are DIFFERENT LEAVES** — the ``left``
and ``right`` modules are the two sides of the **bilateral
parent container**. Consumers must **not** conflate the **left**
prepositus nucleus with the **right** — resolve the right side
via
``perihypoglossal_nuclei.right.prepositus_nucleus``.
**Boundary status (NOT the left intercalated nucleus — a SIBLING
within the same left perihypoglossal complex):** **Boundary
case — the left prepositus nucleus is NOT the left intercalated
nucleus.** The **left intercalated nucleus**
(``.../perihypoglossal_nuclei/left/intercalated_nucleus/``) is
a **sibling leaf** in the left perihypoglossal complex — it is
more involved in **vertical gaze** and **vertical
vestibulo-ocular** integration. The **left prepositus nucleus**
(here) is the **horizontal gaze neural integrator** — a
**separate structure** with a **different function**. **They
are DIFFERENT NUCLEI** — both are members of the **left
perihypoglossal complex**, but they are **not interchangeable**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left hypoglossal nucleus — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the left prepositus nucleus is NOT the left hypoglossal
nucleus.** The **left hypoglossal nucleus**
(``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) is the
**left somatic motor** nucleus for the **tongue** — it is
**adjacent** to the left prepositus nucleus (the prepositus
nucleus lies **dorsal and lateral** to the hypoglossal nucleus,
and the **name "prepositus hypoglossi"** reflects its
**position "in front of" (prepositus) the hypoglossal
nucleus**). But they are **DIFFERENT STRUCTURES** with
**DIFFERENT functions** — the **hypoglossal nucleus** is
**motor** (tongue); the **prepositus nucleus** is
**oculomotor** (horizontal gaze holding). Consumers must **not**
conflate the two.
**Boundary status (NOT the left nucleus of Roller — sometimes
grouped but NOT in this tree):** **Boundary case — the left
prepositus nucleus is NOT the left nucleus of Roller.** The
**nucleus of Roller** is **sometimes grouped** with the
perihypoglossal complex in the literature — it lies **ventral
and lateral** to the **hypoglossal nucleus**. In **this tree**,
the nucleus of Roller is **NOT wired** — only the
**intercalated nucleus** and the **prepositus nucleus** are.
Consumers must **not** expect to find the nucleus of Roller
under ``prepositus_nucleus`` — resolve it via the references.
**Boundary status (NOT the left abducens nucleus — a PONTINE
structure with a CRITICAL functional relationship):** **Boundary
case — the left prepositus nucleus is NOT the left abducens
nucleus.** The **left abducens nucleus**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``)
is a **pontine branchial motor** nucleus — it supplies the
**left lateral rectus muscle** and contains the **abducens
internuclear neurons** that **drive** the **right medial
rectus** during **horizontal saccades**. The **left prepositus
nucleus** (here) is a **medullary oculomotor** nucleus — it is
the **neural integrator** that **holds** the **horizontal gaze
position** after the **abducens/PPRF** drives the **saccade**.
**They are DIFFERENT STRUCTURES** in **DIFFERENT CONTAINERS** —
the **abducens nucleus** is **pontine**; the **prepositus
nucleus** is **medullary**. They are **functionally coupled** in
the **horizontal gaze** system — the **prepositus nucleus**
**projects** to the **abducens nucleus** to **hold** the
**gaze** — but they are **not interchangeable**. Consumers must
**not** conflate the two.
**Boundary status (NOT the left PPRF — a PONTINE structure with a
CRITICAL functional relationship):** **Boundary case — the left
prepositus nucleus is NOT the left PPRF.** The **left PPRF**
(``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/left/``)
is the **left pontine horizontal saccade generator** — it
**drives** the **left abducens nucleus** for **horizontal
saccades**. The **left prepositus nucleus** (here) is a
**medullary oculomotor** nucleus — the **neural integrator**
that **holds** the **horizontal gaze position** after the
**saccade**. **They are functionally coupled** but
**anatomically distinct** — the **PPRF** is **pontine**; the
**prepositus nucleus** is **medullary**. Consumers must **not**
conflate the two.
**Boundary status (NOT the left vestibular nuclei — a DIFFERENT
medullary region):** **Boundary case — the left prepositus
nucleus is NOT the left vestibular nuclei.** The **left
vestibular nuclei**
(``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
are **pontomedullary** structures that **receive** vestibular
afferents. The **left prepositus nucleus** (here) is a
**medullary oculomotor** nucleus that **receives** vestibular
input and **participates** in the **horizontal vestibulo-ocular
reflex** — it is **functionally coupled** with the vestibular
nuclei but **anatomically distinct**. Consumers must **not**
conflate the two.
**Boundary status (NOT the MLF — a white-matter tract):**
**Boundary case — the left prepositus nucleus is NOT the medial
longitudinal fasciculus (MLF).** The **MLF** is a
**white-matter tract** that **connects** the **abducens nucleus**
to the **contralateral oculomotor nucleus** (for **horizontal
gaze**) and **connects** the **vestibular nuclei** to the
**oculomotor/trochlear nuclei** (for the **VOR**). The **left
prepositus nucleus** (here) is a **grey-matter nucleus** — it
**projects** to the **abducens nucleus** and **other
oculomotor** structures **via** the **MLF** and **other
pathways**, but it is **NOT** the MLF. Consumers must **not**
conflate the **nucleus** with the **white-matter tract**.
**Boundary status (NOT the left dorsal motor nucleus of the
vagus, left area postrema, or left solitary nucleus — different
structures):** **Boundary case — the left prepositus nucleus is
NOT these other left dorsal medullary structures.** The **left
dorsal motor nucleus of the vagus**
(``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``)
is a **parasympathetic** nucleus; the **left area postrema**
and **left chemoreceptor trigger zone** are **circumventricular
organs**; the **left solitary nucleus**
(``.../solitary_nucleus/left/``) is the **visceral afferent
relay**. **Each is a DIFFERENT STRUCTURE** with a **DIFFERENT
function**. Consumers must **not** conflate the **left
prepositus nucleus** with any of these.
**Boundary status (NOT the left nucleus ambiguus — a
branchial-motor structure):** **Boundary case — the left
prepositus nucleus is NOT the left nucleus ambiguus.** The
**left nucleus ambiguus**
(``.../cranial_nerve_nuclei/left/nucleus_ambiguus/``) is a
**left branchial motor** nucleus in the **ventrolateral
medulla** — it supplies the **striated muscles of the pharynx
and larynx**. The **left prepositus nucleus** (here) is a
**left oculomotor** nucleus in the **dorsal medulla**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left intercalated nucleus, left
medullary pyramid, left olivary body, left arcuate nucleus,
left parafacial zone, left paramedian reticular nucleus, left
RVLM, left CVLM, or left respiratory centers — DIFFERENT
structures):** **Boundary case — the left prepositus nucleus is
NOT these other left medullary structures.** Each is a
**different structure** — see the respective modules.
Consumers must **not** conflate the **left prepositus nucleus**
with any of these.
**Boundary status (NOT the whole left perihypoglossal complex —
a COMPONENT of it):** **Boundary case — the left prepositus
nucleus is NOT the whole left perihypoglossal complex.** The
**left perihypoglossal complex**
(``.../perihypoglossal_nuclei/left/``) is a **container** that
**contains** the left prepositus nucleus (here) **plus** the
left intercalated nucleus. The **left prepositus nucleus** is
**one component** — the **horizontal gaze** component — of the
left perihypoglossal complex. Consumers must **not** conflate
the **component** with the **whole left perihypoglossal
complex**.

Overview
--------
The **left prepositus nucleus** (NPH) is a **grey-matter
nucleus** in the **left dorsal medulla oblongata** — it is the
**neural integrator** for **horizontal gaze holding**. It lies
in the **left perihypoglossal region**, **dorsal and lateral**
to the **left hypoglossal nucleus** (the name "prepositus
hypoglossi" = "in front of the hypoglossal nucleus"), and
**adjacent** to the **left abducens nucleus** (caudally) and
the **left hypoglossal nucleus** (rostrally). It is the
**primary horizontal gaze integrator** — the **neural substrate**
that **converts** the **velocity command** from the **PPRF** and
**abducens nucleus** into a **position command** that **holds**
the **eyes** at the **new eccentric position** after a
**horizontal saccade**.

**This is a LEAF module.** The **left prepositus nucleus** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **nucleus-level** resolution of
the left prepositus nucleus use this module; consumers that need
the **left intercalated nucleus** use
``.../perihypoglossal_nuclei/left/intercalated_nucleus/``;
consumers that need the **whole left perihypoglossal container**
use ``.../perihypoglossal_nuclei/left/``.

**The left prepositus nucleus is the HORIZONTAL GAZE
INTEGRATOR, NOT the vertical gaze contributor.** The **vertical
gaze contributor** is the **left intercalated nucleus** — the
**sibling leaf** in the left perihypoglossal complex. The
**left prepositus nucleus** is the **primary horizontal gaze
integrator** — it is one of the **best-characterized**
**neural integrators** in the **brainstem**. **The prepositus
nucleus** and the **intercalated nucleus** are **functionally
distinct** — the **prepositus nucleus** is **horizontal gaze**;
the **intercalated nucleus** is **vertical gaze**.

**The left prepositus nucleus is the PRIMARY horizontal gaze
integrator.** Unlike the **intercalated nucleus** — which
**contributes** to a **distributed** vertical gaze integrator
(alongside the **interstitial nucleus of Cajal** (INC) in the
midbrain) — the **prepositus nucleus** is the **predominant**
horizontal gaze integrator. **Unilateral** or **bilateral**
**lesions** of the **prepositus nucleus** produce **marked**
**horizontal gaze-evoked nystagmus** — a **cardinal** clinical
sign.

**The left prepositus nucleus is functionally coupled to the
left abducens nucleus, the left PPRF, the left vestibular
nuclei, the cerebellum, and the oculomotor/trochlear nuclei.**
It **participates** in the **horizontal vestibulo-ocular
reflex** and **horizontal gaze holding** — but it is **NOT**
the **abducens nucleus** itself, **NOT** the **PPRF**, **NOT**
the **vestibular nuclei**, and **NOT** the **MLF**.

The Left Prepositus Nucleus / Right Prepositus Nucleus Boundary
---------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left prepositus nucleus** (this module) — the prepositus
    nucleus of the **left** medulla.

*   **Right prepositus nucleus**
    (``.../perihypoglossal_nuclei/right/prepositus_nucleus/``) —
    the prepositus nucleus of the **right** medulla.

**The two are the SIDES of the bilateral perihypoglossal
complex.** They are **structurally symmetric mirror pairs** —
same cytoarchitecture, same projections (with some crossed
components), same **no warning**. Consumers must **not** conflate
the left with the right — resolve the right side via
``perihypoglossal_nuclei.right.prepositus_nucleus``.

The Left Prepositus Nucleus / Left Intercalated Nucleus Boundary
----------------------------------------------------------------
This is the **horizontal gaze / vertical gaze** boundary
(within the same perihypoglossal complex):

*   **Left prepositus nucleus** (this module) — the **left
    horizontal gaze** neural integrator.

*   **Left intercalated nucleus**
    (``.../perihypoglossal_nuclei/left/intercalated_nucleus/``) —
    the **left vertical gaze** nucleus.

**They are DIFFERENT NUCLEI** — both are members of the **left
perihypoglossal complex**, but they are **functionally distinct**
— the **prepositus nucleus** is **horizontal gaze holding**; the
**intercalated nucleus** is **vertical gaze**. Consumers must
**not** conflate the two.

The Left Prepositus Nucleus / Left Hypoglossal Nucleus Boundary
---------------------------------------------------------------
This is the **oculomotor / motor** boundary:

*   **Left prepositus nucleus** (this module) — the **left
    oculomotor** nucleus.

*   **Left hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) —
    the **left somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES** — the **hypoglossal nucleus**
is **motor** (tongue); the **prepositus nucleus** is
**oculomotor** (gaze). They are **adjacent** in the **left
dorsal medulla** (the prepositus nucleus is **dorsal and
lateral** to the hypoglossal nucleus, and the name "prepositus
hypoglossi" reflects its **position**), but they are
**functionally distinct**. Consumers must **not** conflate the
two.

The Left Prepositus Nucleus / Left Nucleus of Roller Boundary
-------------------------------------------------------------
This is the **sometimes-grouped** boundary:

*   **Left prepositus nucleus** (this module) — the **left
    prepositus nucleus**.

*   **Left nucleus of Roller** — a **small medullary nucleus**
    sometimes grouped with the perihypoglossal complex in the
    literature, **NOT** wired in this tree.

**The left nucleus of Roller is NOT wired** as a separate module
in this tree — only the **intercalated nucleus** and the
**prepositus nucleus** are. Consumers must **not** expect to find
the nucleus of Roller under ``prepositus_nucleus`` — resolve it
via the references.

The Left Prepositus Nucleus / Left Abducens Nucleus and Left PPRF Boundary
--------------------------------------------------------------------------
This is the **horizontal gaze-holding / horizontal
gaze-generating** boundary:

*   **Left prepositus nucleus** (this module) — the **left
    horizontal gaze** neural integrator.

*   **Left abducens nucleus**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/abducens_nucleus/``)
    and **left PPRF**
    (``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/left/``)
    — the **left pontine horizontal saccade generators**.

**They are FUNCTIONALLY COUPLED but ANATOMICALLY DISTINCT** —
the **left PPRF** **drives** the **left abducens nucleus** for
the **saccade velocity**; the **left prepositus nucleus**
**holds** the **horizontal gaze position** after the **saccade**
(converting the **velocity command** into a **position
command**). They are in **DIFFERENT CONTAINERS** — the
**abducens nucleus** and **PPRF** are **pontine**; the
**prepositus nucleus** is **medullary**. Consumers must **not**
conflate the two.

The Left Prepositus Nucleus / Left Vestibular Nuclei and MLF Boundary
---------------------------------------------------------------------
This is the **horizontal gaze-holding / VOR-and-MLF** boundary:

*   **Left prepositus nucleus** (this module) — the **left
    horizontal gaze** neural integrator.

*   **Left vestibular nuclei**
    (``.../metencephalon/pons/cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **left VOR relay**.

*   **MLF** — the **white-matter tract** that **connects**
    oculomotor structures.

**They are functionally coupled** but **anatomically distinct**.
The **prepositus nucleus** **integrates** **vestibular** signals
into **gaze-holding** commands — it is **part of** the
**horizontal VOR integrator circuitry**. Consumers must **not**
conflate the **prepositus nucleus** with the **vestibular
nuclei** or with the **MLF**.

The Left Prepositus Nucleus / Other Left Medullary Structures Boundary
----------------------------------------------------------------------
This is the **oculomotor / non-oculomotor** boundary:

*   **Left prepositus nucleus** (this module) — the **left
    medullary oculomotor** nucleus.

*   **Left dorsal motor nucleus of the vagus, left area
    postrema, left chemoreceptor trigger zone, left solitary
    nucleus, left nucleus ambiguus, left medullary pyramid,
    left olivary body, left arcuate nucleus, left parafacial
    zone, left paramedian reticular nucleus, left RVLM, left
    CVLM, left respiratory centers** — **other left medullary
    structures**.

**Each is a DIFFERENT STRUCTURE** with a **DIFFERENT function**.
Consumers must **not** conflate the **left prepositus nucleus**
with any of these.

Function in the Human Brain
---------------------------
The left prepositus nucleus's function is **horizontal gaze
holding** (neural integration) and **horizontal
vestibulo-ocular integration** — **NOT vertical gaze**,
**NOT motor conduction**, and **NOT autonomic regulation**:

*   **Horizontal gaze holding (left prepositus nucleus):** The
    **left prepositus nucleus** is the **primary neural
    integrator** for **horizontal gaze** — it **converts** the
    **velocity command** from the **left PPRF** and **left
    abducens nucleus** into a **position command** that
    **holds** the **eyes** at the **new eccentric position**
    after a **horizontal saccade**. Without a functional **left
    prepositus nucleus**, the **left-sided horizontal gaze
    holding** fails — the **eyes** **drift back** to the
    **primary position** after a **saccade** (**horizontal
    gaze-evoked nystagmus**).

*   **Horizontal vestibulo-ocular integration:** The **left
    prepositus nucleus** **integrates** the **vestibular**
    signals from the **horizontal semicircular canals** into
    the **horizontal VOR** — it **participates** in the
    **velocity storage** mechanism of the **horizontal VOR**.

*   **Saccadic pulse-step matching:** The **left prepositus
    nucleus** **contributes** to the **pulse-step matching** of
    **horizontal saccades** — it **holds** the **step**
    component of the **saccadic command** that **maintains**
    the **new eye position**.

*   **Participation in the neural integrator circuitry:** The
    **prepositus nucleus** is the **primary horizontal gaze
    integrator** — **NOT** a **contributor** to a
    **distributed** integrator (unlike the **intercalated
    nucleus**, which **contributes** to the **distributed**
    vertical gaze integrator). **Lesions** of the **prepositus
    nucleus** produce **marked** **horizontal gaze-evoked
    nystagmus** — the **cardinal** clinical sign.

*   **NOT vertical gaze:** The **vertical gaze integration** is
    the **left intercalated nucleus** (and the **INC** in the
    midbrain) — **NOT** the left prepositus nucleus.

*   **NOT motor conduction:** The **left prepositus nucleus**
    does **not** send motor axons to muscles.

*   **NOT autonomic regulation:** The **left prepositus nucleus**
    does **not** regulate autonomic function.

**The unifying theme:** the left prepositus nucleus is the
**left medullary horizontal gaze integrator** — it **holds** the
**horizontal gaze position** after a **saccade** and
**participates** in the **horizontal VOR** — **NOT** in
**vertical gaze** (that is the left intercalated nucleus) and
**NOT** in **motor** or **autonomic** function.

Associated Disorders
--------------------
The left prepositus nucleus is the **substrate** for
**well-defined clinical syndromes** — its clinical relevance is
**direct**, via **horizontal gaze-holding** dysfunction:

*   **Horizontal gaze-evoked nystagmus (via left prepositus
    nucleus dysfunction):** **Impaired** horizontal **gaze
    holding** on the **left side** — the **eyes** **drift
    back** to the **primary position** after a **saccade**,
    producing **horizontal gaze-evoked nystagmus**. The **left
    prepositus nucleus** is the **primary neural integrator**;
    its **dysfunction** (from **stroke**, **demyelination**,
    **Wernicke encephalopathy**, **drugs** like
    **benzodiazepines**, **cerebellar** disease, or
    **degenerative** conditions) causes **horizontal
    gaze-evoked nystagmus**. This is a **cardinal**
    brainstem/cerebellar sign — one of the **most useful**
    **localizing** oculomotor findings.

*   **Horizontal gaze palsy / saccadic palsy (via severe left
    prepositus nucleus dysfunction):** **Severe** bilateral
    **prepositus nucleus** dysfunction can produce **marked**
    horizontal **gaze palsy** — but the **more common**
    finding is **gaze-evoked nystagmus**.

*   **Wernicke encephalopathy (via left prepositus nucleus
    involvement):** **Wernicke encephalopathy** (thiamine
    deficiency) **typically** involves the **medial vestibular
    nuclei** and the **perihypoglossal nuclei** — including the
    **prepositus nucleus**. The **left prepositus nucleus** is a
    **direct substrate** of the **gaze-evoked nystagmus** and
    **oculomotor** findings in Wernicke encephalopathy.

*   **Brainstem stroke (via left prepositus nucleus
    involvement):** **Left medullary** **stroke** can
    **involve** the **left prepositus nucleus** — contributing
    to **horizontal gaze-evoked nystagmus** and **horizontal
    gaze** abnormalities.

*   **Drug-induced gaze-evoked nystagmus (via prepositus
    nucleus dysfunction):** **Benzodiazepines**,
    **barbiturates**, **alcohol**, and **other** drugs that
    **enhance GABA-A** receptor function **impair** the
    **prepositus nucleus**'s **neural integrator** —
    producing **horizontal gaze-evoked nystagmus**. The **left
    prepositus nucleus** is a **direct substrate** of this
    **drug-induced** nystagmus.

*   **Cerebellar disease (via prepositus nucleus
    dysfunction):** **Cerebellar** lesions — especially those
    **involving** the **flocculus/paraflocculus** (which
    **project** to the **prepositus nucleus**) — impair the
    **integrator** and cause **gaze-evoked nystagmus**.

*   **No Named "Left Prepositus Nucleus Syndrome":** The left
    prepositus nucleus is a **small but functionally critical**
    nucleus — its clinical syndromes are **named for the
    broader brainstem/cerebellar lesion** (Wernicke
    encephalopathy, brainstem stroke, cerebellar disease) or
    the **oculomotor sign** (horizontal gaze-evoked nystagmus),
    **not** for the nucleus itself. Its clinical relevance is
    **direct**, via the **horizontal gaze-holding** function.

**What is NOT here:** The left prepositus nucleus is **not** the
substrate for **vertical gaze-evoked nystagmus** (left
intercalated nucleus, INC), **tongue weakness** (left
hypoglossal nucleus), **motor weakness** (left corticospinal
tract — **NOT** in this container), **sensory loss** (left
medial lemniscus, left spinothalamic tract — **NOT** in this
container), or **autonomic dysfunction** (left RVLM, left CVLM,
left NTS — **NOT** in this container). Its clinical relevance is
the **horizontal gaze-holding** and **horizontal VOR** functions
listed above.

Lateralization Notes
--------------------
This is the **left** prepositus nucleus module. The
perihypoglossal nuclei are a **bilateral container** whose two
sides are **structurally symmetric mirror pairs** — and it
carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right**
    prepositus nuclei are **structurally symmetric** — they are
    **mirror pairs** with the **same** cytoarchitecture,
    **same** projections, and **same** functions.

*   **Bilateral Distribution of the Horizontal Integrator:**
    The **horizontal gaze integrator** is **distributed
    bilaterally** between the **left** and **right prepositus
    nuclei** — **unilateral** lesions may **not** cause
    **dramatic** deficits because the **contralateral**
    prepositus nucleus can **partially** **compensate**.
    **Bilateral** lesions produce **marked** bilateral
    **gaze-evoked nystagmus**.

*   **Crossed Projections:** Some **prepositus nucleus**
    projections are **crossed** — the **left prepositus
    nucleus** projects to the **right abducens nucleus** and
    the **right vestibular nuclei** via the **crossed**
    **pathways**, in addition to **ipsilateral** projections.
    This **functional bilateralism** contributes to the
    **integrator's stability**.

*   **NO Lateralization Warning:** The prepositus nucleus has
    **no known functional lateralization** in humans.
    Consumers must **not** import a **lateralization warning**
    into the left prepositus nucleus — the **left** and
    **right** nuclei are **functionally symmetric** at the
    **nucleus level**.

*   **NO Extended-Amygdala / SLEA Warning:** The left
    prepositus nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the left prepositus nucleus.

*   **NO Fear-Output Warning:** The left prepositus nucleus is
    **not** a fear-output structure — it is a **left medullary
    oculomotor** nucleus. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left prepositus nucleus = right
prepositus nucleus" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**nucleus level**. The prepositus nucleus is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left prepositus nucleus
    is a **leaf** — it does **not** import from ``.../right/``
    or any other right-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
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
    The left prepositus nucleus's relationships to the left
    intercalated nucleus, left hypoglossal nucleus, left
    nucleus of Roller, left abducens nucleus, left PPRF, left
    vestibular nuclei, MLF, left dorsal motor nucleus of the
    vagus, left area postrema, left chemoreceptor trigger zone,
    left solitary nucleus, left nucleus ambiguus, left
    medullary pyramid, left olivary body, left arcuate nucleus,
    left parafacial zone, left paramedian reticular nucleus,
    left RVLM, left CVLM, and left respiratory centers are
    documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left
    prepositus nucleus is a **single structure** — it has **no
    structural children**. Consumers must **not** expect
    further sub-paths under ``.../prepositus_nucleus/``.
*   **NOT the right prepositus nucleus.** The right prepositus
    nucleus is a **separate leaf** under
    ``.../perihypoglossal_nuclei/right/``. Consumers must **not**
    conflate the left with the right.
*   **NOT the left intercalated nucleus.** The left intercalated
    nucleus is a **sibling leaf** in the left perihypoglossal
    complex — it is the **vertical gaze** nucleus, **NOT** the
    horizontal gaze integrator.
*   **NOT the left hypoglossal nucleus.** The left hypoglossal
    nucleus is a **somatic motor** nucleus (tongue) — **NOT**
    the left prepositus nucleus.
*   **NOT the left nucleus of Roller.** The nucleus of Roller is
    **sometimes grouped** with the perihypoglossal complex in
    the literature but is **NOT wired** in this tree.
*   **NOT the left abducens nucleus or left PPRF.** Those are
    **pontine horizontal saccade generators** — **functionally
    coupled** but **anatomically distinct**.
*   **NOT the left vestibular nuclei or the MLF.** Those are
    **different structures** in **different containers** (MLF
    is a white-matter tract).
*   **NOT the left dorsal motor nucleus of the vagus, left area
    postrema, left chemoreceptor trigger zone, or left solitary
    nucleus.** Each is a **different structure**.
*   **NOT the left nucleus ambiguus, left medullary pyramid,
    left olivary body, left arcuate nucleus, left parafacial
    zone, left paramedian reticular nucleus, left RVLM, left
    CVLM, or left respiratory centers.** Each is a **different
    structure**.
*   **NOT the whole left perihypoglossal complex.** The **left
    perihypoglossal complex**
    (``.../perihypoglossal_nuclei/left/``) contains this nucleus
    **plus** the left intercalated nucleus. Consumers must **not**
    conflate the **component** with the **whole complex**.
*   **No ``AREA_PATHS`` hop.** The left prepositus nucleus is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The left prepositus nucleus
    has no nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the right prepositus nucleus —
    strict mirror with NO warning.** The left and right modules
    are **structurally identical** — same leaf status, same
    **horizontal gaze integrator** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left import prepositus_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "perihypoglossal_nuclei.left.prepositus_nucleus"
    )

**Do not** assume the left prepositus nucleus is the **right
prepositus nucleus**. The right prepositus nucleus is the
**separate leaf** at
``.../perihypoglossal_nuclei/right/prepositus_nucleus/``.

**Do not** assume the left prepositus nucleus is the **left
intercalated nucleus**. The left intercalated nucleus is the
**sibling leaf** — the **vertical gaze** nucleus — **NOT** the
horizontal gaze integrator.

**Do not** assume the left prepositus nucleus is the **left
hypoglossal nucleus**. The left hypoglossal nucleus is a
**somatic motor** nucleus (tongue) — **NOT** the left
prepositus nucleus.

**Do not** assume the left prepositus nucleus is the **left
nucleus of Roller**. The nucleus of Roller is **sometimes
grouped** with the perihypoglossal complex in the literature but
is **NOT wired** in this tree.

**Do not** assume the left prepositus nucleus is the **left
abducens nucleus** or **left PPRF**. Those are **pontine
horizontal saccade generators** — **functionally coupled** but
**anatomically distinct**.

**Do not** assume the left prepositus nucleus is the **left
vestibular nuclei** or **MLF**. Those are **different
structures**.

**Do not** assume the left prepositus nucleus is the **left
dorsal motor nucleus of the vagus**, **left area postrema**,
**left chemoreceptor trigger zone**, or **left solitary
nucleus**. Each is a **different structure**.

**Do not** assume the left prepositus nucleus has **structural
children**. It is a **leaf** — it represents the left
prepositus nucleus as a **single structure**.

Iterating the left prepositus nucleus's (empty) children
(recommended consumer pattern)::

    LEFT_PREPOSITUS_NUCLEUS_CHILDREN = ()
    # The left prepositus nucleus is a leaf. It has no
    # structural children.

Reaching the right prepositus nucleus (recommended consumer
pattern — the contralateral leaf)::

    # The right prepositus nucleus is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.right.prepositus_nucleus
    #
    # The left and right prepositus nuclei are structurally
    # symmetric mirror pairs and together form the bilateral
    # horizontal gaze integrator.

Reaching the left intercalated nucleus (recommended consumer
pattern — the SIBLING leaf)::

    # The left intercalated nucleus is the SIBLING leaf in the
    # left perihypoglossal complex — the vertical gaze nucleus,
    # NOT the horizontal gaze integrator:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei.left.intercalated_nucleus
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
    # The left prepositus nucleus is named for its position
    # "in front of" (prepositus) the hypoglossal nucleus — but
    # it is a SEPARATE structure with a DIFFERENT function.

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
    # They are functionally coupled with the left prepositus
    # nucleus in the horizontal gaze and VOR systems — but they
    # are DIFFERENT structures.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"perihypoglossal_nuclei.{side}.prepositus_nucleus"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Perihypoglossal nuclei; prepositus nucleus; neural
    integrator; oculomotor system.)
*   **Prepositus nucleus — neural integrator:** Cannon, S.C.,
    Robinson, D.A. (1987). "Loss of the neural integrator of
    the oculomotor system from brain stem lesions in monkey."
    *Journal of Neurophysiology* 57:1383–1409. (Prepositus
    nucleus; neural integrator; horizontal gaze holding;
    gaze-evoked nystagmus after lesions.)
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
*   **Prepositus nucleus — velocity storage:** Raphan, T., Cohen,
    B. (1978). "Brainstem mechanisms for rapid and slow eye
    movements." *Annual Review of Physiology* 40:527–552.
    (Prepositus nucleus; velocity storage; horizontal VOR.)
*   **Prepositus nucleus — overview:** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed.
    (Perihypoglossal nuclei; prepositus nucleus; neural
    integrator; horizontal gaze-evoked nystagmus.)
*   **Gaze-evoked nystagmus — clinical:** Leigh, R.J., Zee,
    D.S. (2015). *The Neurology of Eye Movements*, 5th ed.
    (Gaze-evoked nystagmus; neural integrator; prepositus
    nucleus; drug-induced gaze-evoked nystagmus.)
*   **Wernicke encephalopathy — oculomotor findings:** Victor,
    M., et al. (1989). *The Wernicke-Korsakoff Syndrome and
    Related Neurologic Disorders Due to Alcoholism and
    Malnutrition*, 2nd ed. (Wernicke encephalopathy; medial
    vestibular nuclei; perihypoglossal nuclei — including the
    prepositus nucleus; nystagmus.)
*   **Hypoglossal nucleus (contrast — motor):** Lowe, A.A.
    (1980). "The neural regulation of tongue movement."
    *Progress in Neurobiology* 14:273–349. (Hypoglossal
    nucleus; tongue motor — DIFFERENT from the prepositus
    nucleus.)
*   **Intercalated nucleus (contrast — vertical gaze):** Langer,
    T., et al. (1986). "The nucleus intercalatus and the
    nucleus prepositus hypoglossi: their involvement in
    vertical and horizontal eye movements." *Experimental
    Brain Research* 64:325–334. (Intercalated nucleus;
    vertical gaze; vertical VOR — DIFFERENT from the prepositus
    nucleus.)
*   **Abducens nucleus and PPRF (contrast — pontine horizontal
    gaze):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of
    Eye Movements*, 5th ed. (Abducens nucleus; PPRF; horizontal
    saccades — functionally coupled but DIFFERENT from the
    prepositus nucleus.)
*   **Vestibular nuclei (contrast — VOR relay):** Wilson, V.J.,
    Melvill Jones, G. (1979). *Mammalian Vestibular
    Physiology.* (Vestibular nuclei; VOR — DIFFERENT from the
    prepositus nucleus.)
*   NeuroNames — Nucleus prepositus hypoglossi; FMA — Nucleus
    prepositus hypoglossi.
"""