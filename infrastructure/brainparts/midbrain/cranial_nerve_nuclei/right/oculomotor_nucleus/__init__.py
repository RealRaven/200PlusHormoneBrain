"""
infrastructure.brainparts.midbrain.cranial_nerve_nuclei.right.oculomotor_nucleus
===============================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── cranial_nerve_nuclei
    │   ├── left
    │   │   └── ...
    │   └── right
    │       ├── oculomotor_nucleus               <-- THIS MODULE
    │       │                                       (leaf — FUNCTIONAL
    │       │                                       parent)
    │       ├── trochlear_nucleus
    │       ├── mesencephalic_trigeminal_nucleus
    │       └── edinger_westphal_nucleus
    └── tegmentum
        ├── left
        │   └── ...
        └── right
            ├── oculomotor_nucleus               (SAME LEAF —
            │                                       TOPOGRAPHIC
            │                                       parent)
            ├── trochlear_nucleus
            ├── mesencephalic_trigeminal_nucleus
            ├── edinger_westphal_nucleus
            ├── substantia_nigra
            └── ...

**Primary synonym:** Right oculomotor nucleus; right CN III nucleus
(somatic motor component); right somatic oculomotor nucleus; right
nucleus of CN III; **the right CN III somatic motor nucleus** — as
distinct from the **right Edinger-Westphal nucleus** (CN IIIp), which
is the **preganglionic parasympathetic** component of the same nerve.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **somatic motor nucleus** in the **rostral midbrain
tegmentum**, at the **level of the superior colliculus**, **ventral
to the periaqueductal gray** and **dorsal to the medial longitudinal
fasciculus (MLF)**. It is a **paired** nucleus (right and left),
with a **complex subnuclear organization** — five somatic motor
subnuclei (superior rectus, inferior rectus, medial rectus, inferior
oblique, levator palpebrae superioris) — and one **distinct
sibling nucleus** (Edinger-Westphal, CN IIIp) that is **dorsomedial**
to it. See *Subnuclear Organization* and *Oculomotor vs
Edinger-Westphal* below.
**Part of:** The **cranial_nerve_nuclei** functional grouping
container → **right** side container (functional parent), **and** the
**tegmentum** topographic container → **right** side container
(topographic parent). **Dual-parent leaf — see *Structural parent*
below and *Cross-Listing Statement*.**
**Structural parent (FUNCTIONAL):** ``.../cranial_nerve_nuclei/right/``
→ **direct child** of the **right side container** of the
cranial_nerve_nuclei functional grouping container.
**Structural parent (TOPOGRAPHIC):** ``.../tegmentum/right/`` →
**direct child** of the **right side container** of the tegmentum
topographic container.
**Structural children:** **None.** This is a **leaf** module. The
**five somatic motor subnuclei** (superior rectus, inferior rectus,
medial rectus, inferior oblique, levator palpebrae superioris) are
documented as **prose**, not as structural children — see *Subnuclear
Organization*.
**Boundary status (DUAL-PARENT LEAF — CROSS-LISTED between
``cranial_nerve_nuclei/right/`` and ``tegmentum/right/``):** **Boundary
case — the right oculomotor nucleus is a DUAL-PARENT LEAF.** It is
reachable by **two** structural paths:
*   **Functional path** —
    ``.../cranial_nerve_nuclei/right/oculomotor_nucleus/``
*   **Topographic path** —
    ``.../tegmentum/right/oculomotor_nucleus/``
**Both resolve to the SAME leaf** — this module. Consumers resolving
the leaf by **either** path get **the same module**. Consumers must
**not** assume the two paths lead to different structures — they lead
to **one leaf**, dual-parented. See *Cross-Listing Statement*.
**Boundary status (SOMATIC MOTOR NUCLEUS — NOT a preganglionic
parasympathetic nucleus):** **Boundary case — the right oculomotor
nucleus is the **SOMATIC MOTOR** nucleus of CN III — NOT the
preganglionic parasympathetic nucleus.** CN III has **two distinct
nuclei**:
*   **Oculomotor nucleus (somatic motor)** — **THIS LEAF** —
    innervates the **five extraocular muscles + levator palpebrae
    superioris** (skeletal muscle).
*   **Edinger-Westphal nucleus (preganglionic parasympathetic)** —
    **NOT this leaf** (see
    ``.../cranial_nerve_nuclei/right/edinger_westphal_nucleus/`` and
    ``.../tegmentum/right/edinger_westphal_nucleus/``) — innervates
    the **ciliary ganglion** → **sphincter pupillae** and **ciliary
    muscle** (smooth muscle).
**They are DIFFERENT NUCLEI in close proximity** — EW is
**dorsomedial** to the oculomotor nucleus. **The CN III fascicles
carry BOTH sets of axons**, but the **nuclei are distinct**. Consumers
must **not** conflate the oculomotor nucleus with the EW nucleus, and
must **not** attribute **pupil constriction** or **lens
accommodation** function to this leaf — those are the **EW leaf**.
**Boundary status (NOT the Edinger-Westphal nucleus — the EW nucleus
is the SIBLING nucleus of the same nerve):** **Boundary case — the
right oculomotor nucleus is NOT the right Edinger-Westphal nucleus.**
They are **sibling CN III nuclei** — the **somatic motor** nucleus
(this leaf) and the **preganglionic parasympathetic** nucleus (the
EW leaf). **They are DIFFERENT NUCLEI** in close proximity; the
**EW** is **dorsomedial** to the oculomotor nucleus. Consumers must
**not** conflate the two, and must **not** resolve the EW leaf
through the oculomotor path (or vice versa). See
*Oculomotor vs Edinger-Westphal* below.
**Boundary status (CONTRALATERAL SUPERIOR RECTUS SUBNUCLEUS — the
ONLY CN III subnucleus innervating the CONTRALATERAL muscle):**
**Boundary case — the right oculomotor nucleus's **superior rectus
subnucleus** innervates the **LEFT superior rectus** — the
**contralateral** muscle.** This is **THE DEFINING CLINICAL FACT**
of the oculomotor nucleus's subnuclear organization:
*   **Medial rectus subnucleus** — **ipsilateral** (right medial
    rectus).
*   **Inferior rectus subnucleus** — **ipsilateral** (right inferior
    rectus).
*   **Inferior oblique subnucleus** — **ipsilateral** (right inferior
    oblique).
*   **Superior rectus subnucleus** — **CONTRALATERAL** (LEFT
    superior rectus) — **THE ONLY ONE**.
*   **Levator palpebrae superioris (central caudal nucleus)** —
    **BILATERAL** (both right and left levator palpebrae) — **a
    single midline subnucleus**.
**A consumer that assumes "right oculomotor nucleus → right eye only"
is WRONG** — the **right superior rectus subnucleus** innervates the
**LEFT superior rectus**, and the **central caudal nucleus**
innervates **BOTH** levator palpebrae. **This is the key anatomical
fact that distinguishes a nuclear CN III lesion from a fascicular or
nerve lesion** — see *Associated Disorders*.
**Boundary status (CENTRAL CAUDAL NUCLEUS — the SINGLE MIDLINE
LEVATOR SUBNUCLEUS):** **Boundary case — the right oculomotor
nucleus's **levator palpebrae superioris** subnucleus is the
**central caudal nucleus** — a **single midline subnucleus** that
innervates **BOTH right and left** levator palpebrae superioris.**
This is **NOT a paired subnucleus** — it is a **midline
structure** shared between the two sides. **A nuclear CN III lesion
that involves the central caudal nucleus produces BILATERAL ptosis**
— not just ipsilateral ptosis. **A fascicular or nerve CN III lesion
that spares the central caudal nucleus produces UNILATERAL ptosis.**
**Bilateral ptosis suggests a NUCLEAR lesion; unilateral ptosis
suggests a FASCICULAR or NERVE lesion.** This is the **second key
clinical fact** of the oculomotor nucleus. See *Associated
Disorders*.
**Boundary status (NOT the right trochlear nucleus — the trochlear
nucleus is CN IV):** **Boundary case — the right oculomotor nucleus
is NOT the right trochlear nucleus.** The **right trochlear nucleus
(CN IV)**
(``.../cranial_nerve_nuclei/right/trochlear_nucleus/`` **and**
``.../tegmentum/right/trochlear_nucleus/``) is the **somatic motor**
nucleus for the **superior oblique** — a **different cranial nerve**
(CN IV, not CN III). **They are DIFFERENT NUCLEI** — the
**oculomotor** is **CN III**; the **trochlear** is **CN IV**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right mesencephalic trigeminal nucleus —
the mesV is a SENSORY nucleus):** **Boundary case — the right
oculomotor nucleus is NOT the right mesencephalic trigeminal nucleus
(mesV).** The **right mesV**
(``.../cranial_nerve_nuclei/right/mesencephalic_trigeminal_nucleus/``
**and** ``.../tegmentum/right/mesencephalic_trigeminal_nucleus/``) is
the **primary sensory (proprioceptive)** nucleus of the trigeminal
system. **They are DIFFERENT NUCLEI** — the **oculomotor** is
**somatic motor (CN III)**; the **mesV** is **primary sensory
(CN V)**. Consumers must **not** conflate the two.
**Boundary status (NOT the MLF — the MLF is a CONDUCTION PATHWAY):**
**Boundary case — the right oculomotor nucleus is NOT the right MLF.**
The **medial longitudinal fasciculus (MLF)** is a **longitudinal
fiber tract** — a **conduction pathway** — that **coordinates** the
**CN III**, **CN IV**, and **CN VI** nuclei for **conjugate gaze**.
It is **wired elsewhere** (as a brainstem longitudinal tract). The
**right oculomotor nucleus** is a **nucleus** — grey matter.
**A right MLF lesion produces RIGHT INTERNUCLEAR OPHTHALMOPLEGIA
(INO)** — **adduction weakness of the right eye with abducting
nystagmus of the left eye** — **NOT a right CN III nuclear palsy**
and **NOT a right CN III palsy at all**. **These are DIFFERENT
SYNDROMES.** Consumers must **not** conflate the oculomotor nucleus
with the MLF, and must **not** resolve the MLF through the
oculomotor path. See *Associated Disorders*.
**Boundary status (NOT the right CN III nerve or the right CN III
fascicles — the NERVE is peripheral, the FASCICLES are the
conduction pathway):** **Boundary case — the right oculomotor nucleus
is NOT the right oculomotor nerve and NOT the right CN III
fascicles.** The **right CN III nerve** is the **peripheral axon
bundle** — it is **wired elsewhere** (peripheral nervous system).
The **right CN III fascicles** traverse the **right cerebral
peduncle** (a conduction-pathway module) **en route** to the
interpeduncular fossa. **The oculomotor axons travel IN the CN III
nerve and IN the CN III fascicles**, but the **nerve** and the
**fascicles** are **not the nucleus**. **They are DIFFERENT
STRUCTURES** — the **oculomotor nucleus** is **grey matter**; the
**CN III fascicles** are **fibers traversing the crus cerebri**; the
**CN III nerve** is **peripheral**. Consumers must **not** conflate
the oculomotor nucleus with the CN III nerve or with the CN III
fascicles, and must **not** forget that **the fascicular lesion site
is the crus cerebri**, not the nucleus — see **Weber syndrome**
below. See *Associated Disorders*.
**Boundary status (NOT the pretectal nucleus — the pretectal nucleus
is DIENCEPHALON, and it is the AFFERENT relay of the pupillary light
reflex, NOT the somatic motor nucleus):** **Boundary case — the
right oculomotor nucleus is NOT the pretectal nucleus.** The
**pretectal nuclei** — the **olivary pretectal nucleus** and the
**nucleus of the optic tract** — are **diencephalon** structures
(``.../forebrain/diencephalon/pretectal_nuclei/``). They are the
**afferent relay** of the **pupillary light reflex**, and they
project to the **Edinger-Westphal nucleus** — **NOT** the oculomotor
nucleus. **They are DIFFERENT STRUCTURES across a lobe boundary** —
the **pretectal nucleus** is **diencephalon**; the **oculomotor
nucleus** is **midbrain**. Consumers must **not** conflate the two,
and must **not** resolve the pretectal nucleus through the
oculomotor path.
**Boundary status (NOT the right superior colliculus — the superior
colliculus is a TECTUM structure that DRIVES the oculomotor nucleus
but is not the oculomotor nucleus):** **Boundary case — the right
oculomotor nucleus is NOT the right superior colliculus.** The **right
superior colliculus**
(``.../tectum/right/superior_colliculus/``) is the
**visual/oculomotor orienting** structure — it **projects to** the
oculomotor nucleus via the **tectobulbar tract** to drive
**saccades** and the **visual grasp reflex**. **They are DIFFERENT
STRUCTURES** — the **superior colliculus** is **tectum**; the
**oculomotor nucleus** is **tegmentum**. The superior colliculus
**drives** the oculomotor nucleus, but **connectivity is not
identity**. Consumers must **not** conflate the two, and must **not**
resolve the superior colliculus through the oculomotor path.
**Boundary status (NOT the right riMLF or the right interstitial
nucleus of Cajal — those are GAZE CENTERS, not CN nuclei):**
**Boundary case — the right oculomotor nucleus is NOT the right riMLF
and NOT the right interstitial nucleus of Cajal.** The **riMLF** and
the **interstitial nucleus of Cajal** are **vertical gaze centers**
in the rostral midbrain tegmentum — **premotor saccade generators**,
not **CN nuclei**. They are **tegmentum** structures but are **NOT**
cross-listed under ``cranial_nerve_nuclei/``. The **right oculomotor
nucleus** (here) is a **CN III somatic motor** nucleus. Consumers
must **not** conflate the oculomotor nucleus with the gaze centers,
and must **not** resolve the riMLF or interstitial nucleus of Cajal
through the oculomotor path.
**Boundary status (NOT the right PPRF — the PPRF is a PREMOTOR SACCADE
GENERATOR, not a CN nucleus):** **Boundary case — the right oculomotor
nucleus is NOT the right paramedian pontine reticular formation
(PPRF).** The **right PPRF**
(``.../hindbrain/metencephalon/pons/pprf/``) is the **horizontal
saccade generator** — a **pontine premotor** structure that
**projects to** the **right abducens nucleus** and, via the MLF, to
the **left oculomotor nucleus's medial rectus subnucleus** for
**conjugate horizontal gaze**. **They are DIFFERENT STRUCTURES** —
the **PPRF** is a **pontine premotor saccade generator**; the
**oculomotor nucleus** is a **midbrain CN III somatic motor
nucleus**. The PPRF **drives** the oculomotor nucleus, but
**connectivity is not identity**. Consumers must **not** conflate
the two, and must **not** resolve the PPRF through the oculomotor
path.
**Boundary status (NOT the left oculomotor nucleus — the SIDE
boundary; the SUPERIOR RECTUS subnucleus is CONTRALATERAL and the
LEVATOR subnucleus is BILATERAL — these are the two ASYMMETRIC facts
of the pair):** **Boundary case — the right oculomotor nucleus is NOT
the left oculomotor nucleus, and the two are NOT a strict mirror
pair in all their subnuclear projections.** The **left oculomotor
nucleus**
(``.../cranial_nerve_nuclei/left/oculomotor_nucleus/`` **and**
``.../tegmentum/left/oculomotor_nucleus/``) is the **left**
oculomotor nucleus. The two are **paired structures** that are
**bilaterally symmetric in their cell-body locations** but
**produce a set of ASYMMETRIC clinical patterns**:
*   **Superior rectus subnucleus** — the **right** subnucleus
    innervates the **LEFT** superior rectus; the **left**
    subnucleus innervates the **RIGHT** superior rectus.
    **CONTRALATERAL** — the only CN III subnucleus that decussates.
*   **Central caudal (levator) nucleus** — **single midline** —
    innervates **BOTH** right and left levator palpebrae.
    **BILATERAL**.
**A consumer that assumes "right oculomotor nucleus = left oculomotor
nucleus" will be structurally correct** (the two are paired and
symmetric in location), but a consumer that assumes their
**subnuclear projections** are strict mirrors is **WRONG** — the
**superior rectus subnucleus is contralateral** (not ipsilateral),
and the **levator subnucleus is bilateral** (not unilateral). These
are the **two asymmetric facts** of the oculomotor nuclear pair.
Consumers must **not** conflate the right oculomotor nucleus with the
left, and must **not** assume their clinical syndromes are mirror
images — see *Associated Disorders* and *Lateralization Notes*.
**Boundary status (SOMATIC MOTOR NUCLEUS — NOT a sensory nucleus, NOT
a preganglionic parasympathetic nucleus, NOT an oscillator, NOT a
premotor pool, NOT a conduction pathway):** **Boundary case — the
right oculomotor nucleus is a SOMATIC MOTOR NUCLEUS.** In the
family's **structure-class taxonomy**, it is a **motor nucleus** —
the **same class** as the CN IV somatic motor nucleus and the
Edinger-Westphal preganglionic parasympathetic nucleus — **not** a
sensory nucleus (CN Vm), **not** an oscillator, **not** a premotor
pool, **not** a conduction pathway, and **not** a grey-matter
processing nucleus (substantia nigra, red nucleus). **Motor nuclei
carry NO coupling warning** — same rule as premotor pools, sensor
nuclei, conduction pathways, and the EW and CN IV nuclei. Its
coordination with the **left oculomotor nucleus** is via
**descending pathways** (the **MLF**, the **posterior commissure**,
the **PPRF** for horizontal gaze, the **riMLF** for vertical gaze)
— **not** intrinsic nucleus-to-nucleus coupling. It is a **paired
mirror with NO coupling warning**, **but with the two asymmetric
subnuclear projections noted above** (contralateral superior rectus,
bilateral levator) — see *Lateralization Notes* and *Design
Contract*.

Overview
--------
The right oculomotor nucleus is the **right CN III somatic motor
nucleus** — the **somatic motor component of CN III** — in the
**right rostral midbrain tegmentum**, at the **level of the superior
colliculus**, **ventral to the periaqueductal gray** and **dorsal
to the MLF**. It innervates the **five extraocular muscles** and
the **levator palpebrae superioris** on the **right** side (for the
medial rectus, inferior rectus, and inferior oblique), on the
**left** side (for the superior rectus — the **contralateral
subnucleus**), and on **both** sides (for the levator palpebrae —
the **central caudal nucleus**). It is a **dual-parent leaf** —
reachable by **both** the functional path
(``.../cranial_nerve_nuclei/right/oculomotor_nucleus/``) and the
topographic path
(``.../tegmentum/right/oculomotor_nucleus/``).

**The right oculomotor nucleus is the SOMATIC MOTOR nucleus of CN III —
NOT the preganglionic parasympathetic nucleus.** CN III has **two
distinct nuclei** — the **oculomotor nucleus** (here, somatic motor,
skeletal muscle) and the **Edinger-Westphal nucleus** (the sibling
leaf, preganglionic parasympathetic, smooth muscle). **The CN III
fascicles carry BOTH sets of axons** — but the **nuclei are
distinct**.

**The right oculomotor nucleus has FIVE SOMATIC MOTOR SUBNUCLEI, and
they are NOT all ipsilateral.** The **medial rectus**, **inferior
rectus**, and **inferior oblique** subnuclei innervate the
**ipsilateral** muscles. The **superior rectus subnucleus**
innervates the **CONTRALATERAL** muscle — the **only CN III
subnucleus that decussates**. The **central caudal nucleus**
(**levator palpebrae superioris**) is a **single midline subnucleus**
that innervates **BILATERAL** levator palpebrae. **These are the
two asymmetric facts of the oculomotor nuclear pair** — see
*Subnuclear Organization*.

**The right oculomotor nucleus is a MOTOR NUCLEUS in the family's
taxonomy.** It carries **NO coupling warning** — same rule as CN IV,
EW, premotor pools, sensor nuclei, and conduction pathways.
Coordination with the **left oculomotor nucleus** is via
**descending pathways** (MLF, posterior commissure, PPRF, riMLF) —
**not** intrinsic nucleus-to-nucleus coupling.

**The right oculomotor nucleus is a dual-parent leaf.** Both
structural parents are named together — the **functional parent**
(``.../cranial_nerve_nuclei/right/``) and the **topographic parent**
(``.../tegmentum/right/``). Consumers resolving the leaf by **either**
path get **this module**.

Subnuclear Organization (the two asymmetric facts)
-------------------------------------------------
The right oculomotor nucleus has **five somatic motor subnuclei** —
documented as **prose**, not as structural children:

*   **Medial rectus subnucleus** — **ipsilateral** — innervates the
    **right medial rectus**. **Adduction of the right eye.** The
    **most ventrolateral** subnucleus — most commonly affected in
    **CN III palsy**.

*   **Inferior rectus subnucleus** — **ipsilateral** — innervates
    the **right inferior rectus**. **Depression of the right eye**
    (especially in adduction).

*   **Inferior oblique subnucleus** — **ipsilateral** — innervates
    the **right inferior oblique**. **Elevation of the right eye**
    (especially in adduction).

*   **Superior rectus subnucleus** — **CONTRALATERAL** — innervates
    the **LEFT superior rectus**. **Elevation of the left eye**
    (especially in adduction). **THE ONLY CN III SUBNUCLEUS THAT
    DECUSSATES** — the single most distinctive subnuclear fact.

*   **Levator palpebrae superioris (central caudal nucleus)** —
    **BILATERAL** — innervates **BOTH right and left** levator
    palpebrae. **Elevation of both upper eyelids.** A **single
    midline subnucleus** — **NOT paired**. The **second most
    distinctive subnuclear fact**.

**These subnuclei are prose, not structural children.** The tree
wires the **right oculomotor nucleus** as a **single leaf** under the
right tegmentum and right cranial_nerve_nuclei. Consumers must **not**
resolve ``.../right/oculomotor_nucleus/medial_rectus_subnucleus`` —
no such path exists.

**The clinical significance of the two asymmetric facts:**
*   **Superior rectus subnucleus (contralateral):** A **right
    oculomotor nucleus lesion** produces **weakness of the LEFT
    superior rectus** (impaired elevation of the left eye,
    especially in adduction) — **in addition to** the **right** eye
    findings. **A right CN III palsy with LEFT superior rectus
    weakness is a NUCLEAR lesion pattern** — not a fascicular or
    nerve pattern.
*   **Central caudal nucleus (bilateral):** A **right oculomotor
    nucleus lesion** that involves the central caudal nucleus
    produces **BILATERAL ptosis** — **not just right ptosis**. **A
    CN III palsy with BILATERAL ptosis is a NUCLEAR lesion pattern**
    — not a fascicular or nerve pattern.

**These two facts together — contralateral superior rectus weakness
and bilateral ptosis — are the diagnostic signature of a NUCLEAR
CN III lesion, distinguishing it from a FASCICULAR or NERVE lesion.**
See *Associated Disorders*.

Oculomotor vs Edinger-Westphal (the CN III nuclear split)
--------------------------------------------------------
CN III has **two distinct nuclei**, and this leaf and the EW leaf
are their respective homes:

*   **Oculomotor nucleus** — **THIS LEAF** — **somatic motor** —
    innervates the **five extraocular muscles** and the **levator
    palpebrae superioris** (skeletal muscle).
*   **Edinger-Westphal nucleus** — **the sibling leaf** —
    **preganglionic parasympathetic** — innervates the **ciliary
    ganglion** → **sphincter pupillae** and **ciliary muscle**
    (smooth muscle).

**They are DIFFERENT NUCLEI in close proximity** — EW is
**dorsomedial** to the oculomotor nucleus. **The CN III fascicles
carry BOTH sets of axons** — somatic motor and preganglionic
parasympathetic. A **CN III palsy** may involve **one or both**
components — a **pupil-sparing** palsy spares EW fibers; a
**pupil-involving** palsy involves EW fibers.

**The structural rule:** consumers must **not** conflate the
oculomotor nucleus with the EW nucleus, and must **not** attribute
**pupil constriction** or **lens accommodation** function to this
leaf — those are the **EW leaf**. A consumer who says "right
oculomotor nucleus lesion → right dilated pupil" is **wrong** — the
**pupil** function is **EW**, not oculomotor, and a **nuclear**
oculomotor lesion may **spare** the pupil (if EW is spared) or
**involve** it (if EW is also involved — see *Associated
Disorders*).

The Right Oculomotor Nucleus / Right Edinger-Westphal Nucleus Boundary
---------------------------------------------------------------------
This is the **somatic motor / preganglionic parasympathetic** boundary
in the CN III nuclear complex:

*   **Right oculomotor nucleus** (this module) — **somatic motor** —
    extraocular muscles, levator palpebrae superioris.

*   **Right Edinger-Westphal nucleus**
    (``.../cranial_nerve_nuclei/right/edinger_westphal_nucleus/``
    **and** ``.../tegmentum/right/edinger_westphal_nucleus/``) —
    **preganglionic parasympathetic** — ciliary ganglion → sphincter
    pupillae, ciliary muscle.

**They are DIFFERENT NUCLEI in close proximity** — EW is
**dorsomedial** to the oculomotor nucleus. **Consumers must not
conflate the two** — the **oculomotor** is **somatic motor**; the
**EW** is **preganglionic parasympathetic**. **The CN III fascicles
carry BOTH sets of axons** — but the **nuclei are distinct**.

The Right Oculomotor Nucleus / Right Trochlear Nucleus Boundary
---------------------------------------------------------------
This is the **CN III / CN IV** boundary:

*   **Right oculomotor nucleus** (this module) — **CN III somatic
    motor** — five muscles (via the subnuclei).

*   **Right trochlear nucleus**
    (``.../cranial_nerve_nuclei/right/trochlear_nucleus/`` **and**
    ``.../tegmentum/right/trochlear_nucleus/``) — **CN IV somatic
    motor** — superior oblique (the **LEFT** superior oblique —
    the right trochlear decussates).

**They are DIFFERENT NUCLEI for DIFFERENT CRANIAL NERVES.**
Consumers must **not** conflate the two.

The Right Oculomotor Nucleus / Right Mesencephalic Trigeminal Nucleus Boundary
-----------------------------------------------------------------------------
This is the **somatic motor / sensory** boundary:

*   **Right oculomotor nucleus** (this module) — **CN III somatic
    motor**.

*   **Right mesencephalic trigeminal nucleus (mesV)**
    (``.../cranial_nerve_nuclei/right/mesencephalic_trigeminal_nucleus/``
    **and** ``.../tegmentum/right/mesencephalic_trigeminal_nucleus/``)
    — **CN V primary sensory** (proprioceptive).

**They are DIFFERENT NUCLEI in DIFFERENT functional systems.**
Consumers must **not** conflate the two.

The Right Oculomotor Nucleus / MLF Boundary
-------------------------------------------
This is the **nucleus / conduction pathway** boundary — and the
**INO-vs-CN-III** distinction:

*   **Right oculomotor nucleus** (this module) — the **CN III somatic
    motor nucleus**.

*   **Right MLF** — the **medial longitudinal fasciculus** — a
    **longitudinal fiber tract** — **conduction pathway** — wired
    elsewhere (as a brainstem tract).

**A right MLF lesion produces RIGHT INTERNUCLEAR OPHTHALMOPLEGIA
(INO)** — **adduction weakness of the right eye with abducting
nystagmus of the left eye** — **NOT a right CN III nuclear palsy**
and **NOT a right CN III palsy at all**. **The pupils are typically
spared in INO** (though some MS patients may have both — the
distinction is anatomical, not absolute). **These are DIFFERENT
SYNDROMES.** Consumers must **not** conflate the oculomotor nucleus
with the MLF, and must **not** resolve the MLF through the
oculomotor path.

The Right Oculomotor Nucleus / CN III Nerve and CN III Fascicles Boundary
-------------------------------------------------------------------------
This is the **nucleus / nerve / fascicle** boundary — and the
**Weber syndrome** cross-reference:

*   **Right oculomotor nucleus** (this module) — the **nucleus** —
    grey matter.

*   **Right CN III fascicles** — the **axons** traversing the **right
    cerebral peduncle** — white matter.

*   **Right CN III nerve** — the **peripheral** axon bundle —
    peripheral nervous system.

**The oculomotor axons travel IN the CN III fascicles and IN the CN
III nerve** — but the **nucleus** is **not** the **fascicle** and
**not** the **nerve**. **A CN III fascicular lesion** (e.g., **Weber
syndrome** — see ``.../cerebral_peduncle/right/crus_cerebri/``)
produces a **CN III palsy** — **including mydriasis** (because EW
fibers also travel in the fascicle) — **plus** a **contralateral
hemiplegia** (because the **corticospinal fibers** are in the same
crus cerebri). **A NUCLEAR CN III lesion does NOT produce
contralateral hemiplegia** — the **corticospinal fibers are not in
the nucleus**. Consumers must **not** conflate the three, and must
**not** attribute **contralateral hemiplegia** to a **nuclear CN III
lesion**.

The Right Oculomotor Nucleus / Right Superior Colliculus Boundary
-----------------------------------------------------------------
This is the **saccade-driver / CN III somatic motor** boundary:

*   **Right oculomotor nucleus** (this module) — the **CN III somatic
    motor nucleus**.

*   **Right superior colliculus**
    (``.../tectum/right/superior_colliculus/``) — the **visual and
    oculomotor orienting** structure — drives **saccades** via the
    **tectobulbar tract** to the CN III nuclei.

**The superior colliculus DRIVES the oculomotor nucleus; it is not
the oculomotor nucleus.** They are **different structures in
different midbrain compartments**. Consumers must **not** conflate
the two.

The Right Oculomotor Nucleus / riMLF and Interstitial Nucleus of Cajal Boundary
------------------------------------------------------------------------------
This is the **CN III nucleus / gaze center** boundary:

*   **Right oculomotor nucleus** (this module) — the **CN III somatic
    motor nucleus**.

*   **Right riMLF** and **right interstitial nucleus of Cajal** —
    **vertical gaze centers** — **premotor saccade generators** —
    tegmentum leaves but **NOT** cross-listed under
    `cranial_nerve_nuclei/`.

**They are DIFFERENT STRUCTURES** — the **oculomotor nucleus** is a
**CN III motor nucleus**; the **riMLF** and **interstitial nucleus
of Cajal** are **premotor gaze centers**. Consumers must **not**
conflate the two.

The Right Oculomotor Nucleus / PPRF Boundary
--------------------------------------------
This is the **CN III nucleus / horizontal saccade generator**
boundary:

*   **Right oculomotor nucleus** (this module) — the **CN III somatic
    motor nucleus**.

*   **Right PPRF**
    (``.../hindbrain/metencephalon/pons/pprf/``) — the **horizontal
    saccade generator** — a **pontine premotor** structure that
    **projects to** the **right abducens nucleus** and, via the MLF,
    to the **left oculomotor nucleus's medial rectus subnucleus**
    for **conjugate horizontal gaze**.

**The PPRF DRIVES the oculomotor nucleus; it is not the oculomotor
nucleus.** They are **different structures in different brainstem
compartments** (pons vs. midbrain). Consumers must **not** conflate
the two.

The Right Oculomotor Nucleus / Pretectal Nucleus Boundary
---------------------------------------------------------
This is the **somatic motor / preganglionic parasympathetic
AFFERENT relay** boundary — **across a lobe boundary**:

*   **Right oculomotor nucleus** (this module) — the **CN III somatic
    motor nucleus**.

*   **Pretectal nuclei** — the **olivary pretectal nucleus** and the
    **nucleus of the optic tract** —
    (``.../forebrain/diencephalon/pretectal_nuclei/``) — the
    **afferent** relay of the **pupillary light reflex** —
    **diencephalon**.

**The pretectal nucleus PROJECTS TO the Edinger-Westphal nucleus —
NOT to the oculomotor nucleus.** They are **different structures
in different functional systems** (somatic motor vs.
preganglionic parasympathetic). Consumers must **not** conflate the
two, and must **not** resolve the pretectal nucleus through the
oculomotor path.

The Right Oculomotor Nucleus / Left Oculomotor Nucleus Boundary
---------------------------------------------------------------
This is the **side** boundary — and the **two asymmetric facts of
the pair**:

*   **Right oculomotor nucleus** (this module) — the **right** CN III
    somatic motor nucleus.

*   **Left oculomotor nucleus**
    (``.../cranial_nerve_nuclei/left/oculomotor_nucleus/`` **and**
    ``.../tegmentum/left/oculomotor_nucleus/``) — the **left** CN
    III somatic motor nucleus.

**They are BILATERALLY SYMMETRIC in their cell-body locations** —
each is a **paired CN III somatic motor nucleus** on its side.
**But their subnuclear PROJECTIONS are NOT strict mirrors**:
*   **Superior rectus subnucleus** — the **right** subnucleus
    innervates the **LEFT** superior rectus; the **left**
    subnucleus innervates the **RIGHT** superior rectus.
    **CONTRALATERAL** — the only CN III subnucleus that decussates.
*   **Central caudal (levator) nucleus** — **single midline** —
    innervates **BOTH** right and left levator palpebrae.
    **BILATERAL**.
**A consumer that assumes "right oculomotor nucleus = left
oculomotor nucleus" will be structurally correct** (the two are
paired and symmetric in location), but a consumer that assumes their
**subnuclear projections** are strict mirrors is **WRONG** — the
**superior rectus subnucleus is contralateral**, and the **levator
subnucleus is bilateral**. Consumers must **not** conflate the right
oculomotor nucleus with the left, and must **not** assume their
clinical syndromes are mirror images.

Function in the Human Brain
---------------------------
The right oculomotor nucleus's function is **somatic motor control of
the right and left extraocular muscles and both upper eyelids** —
**NOT** parasympathetic control of the pupil or lens, **NOT** gaze
generation, **NOT** the pupillary light reflex:

*   **Medial Rectus (ipsilateral):** The right medial rectus subnucleus
    innervates the **right medial rectus** — **adduction of the right
    eye**.

*   **Inferior Rectus (ipsilateral):** The right inferior rectus
    subnucleus innervates the **right inferior rectus** —
    **depression of the right eye** (especially in adduction).

*   **Inferior Oblique (ipsilateral):** The right inferior oblique
    subnucleus innervates the **right inferior oblique** —
    **elevation of the right eye** (especially in adduction).

*   **Superior Rectus (CONTRALATERAL):** The right superior rectus
    subnucleus innervates the **LEFT superior rectus** —
    **elevation of the left eye** (especially in adduction). **The
    only CN III subnucleus that decussates.**

*   **Levator Palpebrae Superioris (BILATERAL):** The central caudal
    nucleus innervates **both right and left** levator palpebrae —
    **elevation of both upper eyelids**.

*   **NOT parasympathetic.** The right oculomotor nucleus does **not**
    innervate the **sphincter pupillae** or the **ciliary muscle**
    — those are the **right Edinger-Westphal nucleus** (the sibling
    leaf).

*   **NOT a gaze center.** The right oculomotor nucleus is a **motor
    nucleus** — it **fires in response to upstream drive** (from the
    PPRF, the riMLF, the superior colliculus, the vestibular nuclei,
    the frontal eye fields). It does **not** generate a saccade
    plan. Its **coordination with the left oculomotor nucleus and
    the abducens nuclei** is via **descending pathways** (MLF,
    posterior commissure, PPRF) — **not** intrinsic
    nucleus-to-nucleus coupling.

*   **NOT an oscillator.** The right oculomotor nucleus is a **motor
    nucleus** — it does **not** generate a rhythm. **Motor nuclei
    carry NO coupling warning** — same rule as CN IV, EW, premotor
    pools, sensor nuclei, and conduction pathways.

**The unifying theme:** the right oculomotor nucleus is the **right
CN III somatic motor nucleus** — the **somatic motor component of
CN III**. It is **somatic motor** (**NOT parasympathetic** — the EW
leaf), **NOT a gaze center** (the PPRF, riMLF), and **NOT an
oscillator** (a motor nucleus — **NO coupling warning**). It has
**two asymmetric subnuclear facts**: the **contralateral superior
rectus subnucleus** and the **bilateral levator subnucleus** — these
are the diagnostic signature of a **nuclear CN III lesion**.

Associated Disorders
--------------------
The right oculomotor nucleus has **no named syndrome of its own** —
the CN III palsy syndromes are **fascicular** (Weber, Benedikt,
Claude, Nothnagel) or **nerve** (PCom aneurysm, microvascular). An
**isolated nuclear CN III lesion** is **rare** — but its clinical
pattern is **distinctive** and its associations are **direct**:

*   **Right Nuclear CN III Palsy (DIRECT — rare, nuclear):** A
    **lesion of the right oculomotor nucleus** — from **small
    infarction**, **demyelination** (e.g., **multiple sclerosis**),
    or **tumor** — produces a **distinctive pattern**:
    *   **Right eye:** ptosis, "down and out" (unopposed lateral
        rectus and superior oblique), impaired adduction (medial
        rectus), impaired depression (inferior rectus), impaired
        elevation in adduction (inferior oblique).
    *   **Left eye:** impaired **elevation in adduction** —
        weakness of the **LEFT superior rectus** — from the
        **contralateral superior rectus subnucleus**.
    *   **Bilateral ptosis** — if the **central caudal nucleus** is
        involved — from the **bilateral levator subnucleus**.
    *   **Pupil:** may be **spared** (if EW is spared) or **involved**
        (if EW is also involved) — the **EW is in close proximity**
        but is a **separate nucleus**.
    **Two features distinguish a nuclear lesion from a fascicular or
    nerve lesion: (1) contralateral superior rectus weakness;
    (2) bilateral ptosis.** **A nuclear CN III lesion does NOT
    produce contralateral hemiplegia** — the **corticospinal fibers
    are not in the nucleus**.

*   **Right Fascicular CN III Palsy (Weber, Benedikt, Claude,
    Nothnagel — DIRECT but FASCICULAR, NOT nuclear):**
    *   **Weber syndrome** — **right CN III palsy** (including
        **mydriasis** from EW fiber involvement) **+ left
        hemiplegia** — **right crus cerebri** lesion. See
        ``.../cerebral_peduncle/right/crus_cerebri/``. **NOT a
        nuclear lesion** — the fascicle is in the crus cerebri.
    *   **Benedikt syndrome** — **right CN III palsy** + **left
        ataxia / tremor** (red nucleus + superior cerebellar
        peduncle involvement) — **right tegmentum** lesion. **NOT a
        nuclear lesion** — the fascicle + red nucleus, not the
        oculomotor nucleus alone.
    *   **Claude syndrome** — **right CN III palsy** + **left
        ataxia** (red nucleus + superior cerebellar peduncle) —
        **right tegmentum** lesion — **a less complete Benedikt**.
        **NOT a nuclear lesion.**
    *   **Nothnagel syndrome** — **right CN III palsy** +
        **ipsilateral cerebellar signs** — **tectum / superior
        cerebellar peduncle** involvement. **NOT a nuclear lesion.**

*   **Right Nerve CN III Palsy (PCom aneurysm / microvascular —
    DIRECT but NERVE, NOT nuclear):**
    *   **Pupil-involving CN III palsy** — **right mydriasis** —
        from **posterior communicating artery aneurysm** compression
        of the **superficial pupillomotor fibers** (EW fibers) on
        the CN III nerve. **NOT a nuclear lesion** — the **nerve**
        is compressed.
    *   **Pupil-sparing CN III palsy** — **right ptosis, "down and
        out"** — from **microvascular ischemia** (diabetes,
        hypertension) affecting the **core** of the nerve and
        **sparing** the **superficially-located pupillomotor
        fibers**. **NOT a nuclear lesion** — the **nerve** is
        ischemic.

*   **Right Internuclear Ophthalmoplegia (INO — MLF, NOT a CN III
    nuclear lesion):** A **right MLF lesion** produces **right INO**
    — **adduction weakness of the right eye with abducting nystagmus
    of the left eye** — **NOT a right CN III nuclear palsy** and
    **NOT a right CN III palsy at all**. **The pupils are typically
    spared** in INO (though some MS patients may have both). **This
    is the key differential for a medial rectus palsy** — a
    **right CN III medial rectus palsy** is a **nuclear or
    fascicular or nerve lesion**; a **right INO** is an **MLF
    lesion**. The **MLF is a conduction pathway**, not a nucleus.

*   **Myasthenia Gravis (NOT a CN III Nuclear Lesion — NMJ):**
    **Myasthenia gravis** produces **fatigable ptosis and
    diplopia** — **pupil-sparing** — **NOT a CN III nuclear, or
    fascicular, or nerve lesion**. The lesion is at the
    **neuromuscular junction** — **outside the brainstem**.

*   **Right PPRF Lesion (NOT a CN III Nuclear Lesion — horizontal
    gaze center):** A **right PPRF lesion** produces **right
    horizontal gaze palsy** — **neither eye can look right** —
    **NOT a right CN III nuclear palsy**. The **PPRF is a pontine
    premotor saccade generator** — a **different structure**. **A
    right CN III nuclear lesion** affects the **right eye and the
    left superior rectus**; a **right PPRF lesion** affects
    **conjugate right gaze** with both eyes.

*   **No Named "Oculomotor Nucleus Syndrome" (apart from "nuclear
    CN III palsy"):** The right oculomotor nucleus is a **somatic
    motor nucleus** — its **isolated lesion** produces a **nuclear
    CN III palsy**, which is **rare** in practice. Most clinical CN
    III palsies are **fascicular** (Weber, Benedikt, Claude,
    Nothnagel) or **nerve** (PCom aneurysm, microvascular). The
    **clinical relevance** of the nucleus is **direct** — via the
    **nuclear CN III palsy** pattern — and **diagnostic** — the
    **contralateral superior rectus weakness + bilateral ptosis**
    distinguishes a **nuclear** from a **fascicular** or **nerve**
    lesion.

**What is NOT here:** The right oculomotor nucleus is **not** the
substrate for **Weber syndrome** (crus cerebri — fascicular — **NOT**
nuclear; cross-reference, **NOT** claim), **Benedikt syndrome**
(tegmentum — fascicular + red nucleus — **NOT** nuclear),
**Claude syndrome** (tegmentum — fascicular + red nucleus — **NOT**
nuclear), **Nothnagel syndrome** (tectum / superior cerebellar
peduncle — **NOT** nuclear), **PCom aneurysm CN III palsy** (nerve —
**NOT** nuclear), **microvascular CN III palsy** (nerve — **NOT**
nuclear), **INO** (MLF — **NOT** CN III), **horizontal gaze palsy**
(PPRF — **NOT** CN III), **vertical gaze palsy** (riMLF — **NOT**
CN III), **Parinaud syndrome** (dorsal midbrain — tectum /
pretectum — **NOT** CN III), **myasthenia gravis** (NMJ — **NOT**
CN III), **pupillary light reflex deficits** (EW — **sibling leaf,
NOT this leaf**), **Argyll Robertson pupil** (upstream / downstream
— **NOT** this leaf), **Adie's tonic pupil** (ciliary ganglion —
**NOT** this leaf), **CCHS** (RTN), **OIRD** (pre-Bötzinger
complex — NK1R neurons), **Rett syndrome** (pre-Bötzinger complex),
**SIDS** (proposed — pre-Bötzinger complex + arcuate nucleus),
**essential hypertension / sympathetic overactivity** (C1 group /
RVLM), **Parkinson's disease** (substantia nigra — tegmentum),
**Huntington's disease** (striatum — telencephalon), or
**Kluver-Bucy syndrome** (amygdala). Its clinical relevance is
**direct** — via the **nuclear CN III palsy** pattern — and
**diagnostic** — the **contralateral superior rectus weakness +
bilateral ptosis** distinguishes a **nuclear** from a **fascicular**
or **nerve** lesion.

Lateralization Notes
--------------------
This is the **right** oculomotor nucleus leaf. The right and left
oculomotor nuclei are **bilaterally symmetric in their cell-body
locations** — but their **subnuclear projections are NOT strict
mirrors**:

*   **Bilateral Paired Motor Nuclei:** Each side has its own
    oculomotor nucleus — each is a **paired CN III somatic motor
    nucleus** with five subnuclei.

*   **THE TWO ASYMMETRIC SUBNUCLEAR FACTS (the key to the leaf):**
    *   **Superior rectus subnucleus — CONTRALATERAL.** The **right**
        subnucleus innervates the **LEFT** superior rectus; the
        **left** subnucleus innervates the **RIGHT** superior
        rectus. **The only CN III subnucleus that decussates.**
    *   **Levator palpebrae superioris subnucleus — BILATERAL.** The
        **central caudal nucleus** is a **single midline subnucleus**
        — it innervates **BOTH** right and left levator palpebrae.
        **Not paired.**
    **These two asymmetric projections are what make a nuclear CN III
    lesion distinctive** — **contralateral superior rectus
    weakness** + **bilateral ptosis** — and distinguish it from a
    fascicular or nerve lesion.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to MOTOR NUCLEI):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **right oculomotor nucleus** is a **motor
    nucleus** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. Its **right**
    and **left** sides are **independent nuclei** — there is
    **no** oculomotor-oculomotor coupling. **Coordination with the
    left oculomotor nucleus** is via **descending pathways** — the
    **MLF** (for horizontal conjugate gaze), the **posterior
    commissure** (for vertical conjugate gaze), the **PPRF** (for
    horizontal saccades), the **riMLF** (for vertical saccades) —
    **not** intrinsic nucleus-to-nucleus coupling. **Motor nuclei
    carry NO coupling warning** — same rule as CN IV, EW, premotor
    pools, sensor nuclei, and conduction pathways.

*   **Clinical Laterality — nuclear vs. fascicular vs. nerve:**
    *   A **right nuclear CN III lesion** → **right eye findings**
        (ptosis, down and out, impaired adduction/depression/elevation
        in adduction) **+ LEFT superior rectus weakness** (from the
        contralateral subnucleus) **+ bilateral ptosis** (if the
        central caudal nucleus is involved). **Pupil may be spared
        or involved.** **NOT a fascicular or nerve pattern.**
    *   A **right fascicular CN III lesion** (Weber syndrome) →
        **right CN III palsy** (including mydriasis from EW fiber
        involvement) **+ left hemiplegia**. **The lesion site is
        the crus cerebri, not the nucleus.** **No contralateral
        superior rectus weakness from a nuclear source; no bilateral
        ptosis from a nuclear source** — though both can be present
        from fascicular involvement of the respective fibers.
    *   A **right nerve CN III lesion** (PCom aneurysm /
        microvascular) → **right CN III palsy** — **pupil-involving**
        (PCom) or **pupil-sparing** (microvascular). **NOT a nuclear
        pattern.**
    *   A **right INO (MLF lesion)** → **right adduction weakness with
        left abducting nystagmus** — **NOT a CN III palsy**. **A
        common differential** for a **right medial rectus palsy** —
        the **right CN III medial rectus palsy** is a **nuclear/
        fascicular/nerve lesion**; the **right INO** is an **MLF
        lesion**.
    *   A **right PPRF lesion** → **right horizontal gaze palsy** —
        **neither eye can look right** — **NOT a CN III palsy**.
    *   **A consumer that assumes "right oculomotor nucleus = right
        eye only" will be WRONG** — the **superior rectus subnucleus
        is contralateral** and the **levator subnucleus is bilateral**.
    *   **A consumer that assumes "nuclear CN III lesion = fascicular
        CN III lesion" will be WRONG** — the **nuclear** pattern
        has **contralateral superior rectus weakness + bilateral
        ptosis** and **no contralateral hemiplegia**; the
        **fascicular** pattern has **no nuclear-source contralateral
        findings** and (in Weber) **contralateral hemiplegia**; the
        **nerve** pattern is **pupil-involving or pupil-sparing**
        with **no brainstem signs at all**.

**The right oculomotor nucleus is a strict mirror of the left
oculomotor nucleus in its cell-body locations** — **no coupling
warning, no SLEA warning, no amygdala-lateralization warning, and no
rhinencephalon-exclusion flag** — **but with two crucial caveats**:
(1) the **superior rectus subnucleus is contralateral** — the
**only** asymmetric subnuclear projection; (2) the **levator
subnucleus is bilateral** — a **single midline subnucleus**. These
two facts make the **clinical syndromes of the two oculomotor nuclei
NOT mirror images in their subnuclear content** — the "strict
mirror" is structural in location but **not** in **subnuclear
projection**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only — **no** import
    from ``.../left/oculomotor_nucleus/``.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cerebral_peduncle/right/crus_cerebri/``,
    ``.../tectum/right/superior_colliculus/``, the **MLF**, the
    **PPRF**, the **riMLF**, the **interstitial nucleus of Cajal**,
    the **CN III nerve**, the **pretectal nuclei**, or any other
    container. The right oculomotor nucleus's relationships to the
    right Edinger-Westphal nucleus, the right trochlear nucleus, the
    right mesV, the right MLF, the right PPRF, the right riMLF, the
    right interstitial nucleus of Cajal, the right superior colliculus,
    the pretectal nuclei, the CN III nerve and fascicles, the left
    oculomotor nucleus, the left abducens nucleus, and the
    myasthenia gravis NMJ are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **EW
    cholinergic phenotype** is a ``chemicals_hormones``-layer fact
    — documented as **prose** in the EW leaf, **not** here. The
    **oculomotor nucleus is not cholinergic** in the sense that
    Edinger-Westphal is — it is a **somatic motor nucleus** whose
    phenotype (nicotinic ACh at the neuromuscular junction) is a
    **different chemicals-layer fact** — documented as **prose**,
    **never imported**.
*   **DUAL-PARENT LEAF — CROSS-LISTED between
    ``cranial_nerve_nuclei/right/`` and ``tegmentum/right/``.** Both
    paths resolve to **this module**.
*   **CROSS-LISTING via ``AREA_PATHS``.** The leaf is cross-listed
    between the functional container (``cranial_nerve_nuclei/``) and
    the topographic container (``tegmentum/``). Consumers resolving
    by **either** path get **this module**.
*   **CONSISTENT with the ``cranial_nerve_nuclei/``,
    ``cranial_nerve_nuclei/right/``, and ``midbrain`` container child
    lists.** The CN nuclei are placed under ``tegmentum/``
    (topographic home) **and** cross-listed under
    ``cranial_nerve_nuclei/`` (functional grouping). This leaf is
    the **right-side oculomotor** slice of that cross-listing.
*   **SOMATIC MOTOR NUCLEUS — NOT a preganglionic parasympathetic
    nucleus.** CN III has **two distinct nuclei** — the
    **oculomotor** (this leaf) and the **Edinger-Westphal** (the
    sibling leaf). The **CN III fascicles carry BOTH sets of
    axons** — but the **nuclei are distinct**.
*   **FIVE SOMATIC MOTOR SUBNUCLEI — with TWO asymmetric facts:**
    *   **Superior rectus subnucleus — CONTRALATERAL.** The **only**
        CN III subnucleus that decussates. **Right subnucleus →
        LEFT superior rectus.**
    *   **Levator palpebrae superioris subnucleus — BILATERAL.** The
        **single midline** central caudal nucleus.
    **These two asymmetric facts are the diagnostic signature of a
    NUCLEAR CN III lesion** — **contralateral superior rectus
    weakness + bilateral ptosis** — distinguishing it from a
    FASCICULAR or NERVE lesion.
*   **NOT a nuclear CN III lesion = fascicular CN III lesion.** The
    **nuclear** pattern has **contralateral superior rectus
    weakness + bilateral ptosis** and **no contralateral hemiplegia**;
    the **fascicular** pattern (Weber, Benedikt, Claude, Nothnagel)
    has **no nuclear-source contralateral findings** and (in Weber)
    **contralateral hemiplegia**; the **nerve** pattern (PCom
    aneurysm, microvascular) is **pupil-involving or pupil-sparing**
    with **no brainstem signs at all**.
*   **NOT the MLF — that is a CONDUCTION PATHWAY.** A **right MLF
    lesion** produces **right INO** — **NOT a right CN III palsy**.
*   **NOT the PPRF — that is a PREMOTOR SACCADE GENERATOR.** A
    **right PPRF lesion** produces **right horizontal gaze palsy** —
    **NOT a right CN III palsy**.
*   **NOT the riMLF or the interstitial nucleus of Cajal — those are
    GAZE CENTERS.**
*   **NOT the superior colliculus — that is a TECTUM structure** that
    **drives** the oculomotor nucleus.
*   **NOT the pretectal nucleus — that is DIENCEPHALON**, the
    **afferent relay** of the pupillary light reflex, projecting to
    the **EW nucleus**, not the oculomotor nucleus.
*   **NOT the CN III nerve or the CN III fascicles.** The **nerve**
    is peripheral; the **fascicles** are fibers traversing the crus
    cerebri. **A CN III fascicular lesion** (Weber syndrome) is a
    **fascicular** lesion — **NOT a nuclear lesion** — and produces
    **contralateral hemiplegia**, which a **nuclear CN III lesion
    does not**.
*   **NOT myasthenia gravis — that is a NEUROMUSCULAR JUNCTION
    disorder**, not a CN III nuclear lesion.
*   **NO coupling warning — motor nuclei carry NO coupling warning.**
    Same rule as CN IV, EW, premotor pools, sensor nuclei, and
    conduction pathways. Coordination with the left oculomotor
    nucleus is via **descending pathways** (MLF, posterior
    commissure, PPRF, riMLF) — **not** intrinsic nucleus-to-nucleus
    coupling.
*   **CHEMICALS-LAYER DISCIPLINE.** The **EW cholinergic phenotype**
    is a ``chemicals_hormones``-layer fact — documented in the EW
    leaf, **never imported here**. The **oculomotor neuromuscular
    junction** phenotype (nicotinic ACh) is a **different
    chemicals-layer fact** — documented as **prose**, **never
    imported**.
*   **CN NUCLEUS — NOT a CN nerve, NOT a CN fascicle, NOT a
    conduction pathway, NOT a gaze center.**
*   **SIDE-CONSISTENT — this leaf is the RIGHT oculomotor nucleus.**
*   **MIRROR PARITY with ``.../left/oculomotor_nucleus/`` — paired
    and symmetric in cell-body location, with NO coupling warning**
    — **but with TWO ASYMMETRIC SUBNUCLEAR FACTS**: (1)
    **contralateral superior rectus subnucleus**; (2) **bilateral
    levator subnucleus**. The "strict mirror" is **structural in
    location** but **not** in **subnuclear projection**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum/right`` ↔
    ``cranial_nerve_nuclei/right``) — not into the forebrain,
    hindbrain, or periphery. The **MLF**, **PPRF**, **riMLF**, and
    **interstitial nucleus of Cajal** are **separate structures**
    referenced as **prose**, not as cross-listed parents. The
    **crus cerebri**, **superior colliculus**, **CN III nerve**, and
    **pretectal nuclei** are also **separate structures** referenced
    as **prose**.
*   **No nested cross-listing.** This is a **single dual-parent
    leaf**. It is **not** a container.
*   **The on-disk tree is authoritative.**

Usage
-----
Resolve the leaf by **either** path (they are equivalent — **this is
a dual-parent anchor**)::

    # Functional path (clinician framing):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei.right import oculomotor_nucleus

    # Topographic path (anatomist framing):
    from infrastructure.brainparts.midbrain.tegmentum.right import oculomotor_nucleus

Or by fully-qualified path string::

    functional_path = (
        "midbrain.cranial_nerve_nuclei.right.oculomotor_nucleus"
    )
    topographic_path = (
        "midbrain.tegmentum.right.oculomotor_nucleus"
    )
    # Both resolve to THIS module.

**Do not** assume the two paths lead to **different structures** —
they lead to **one leaf**, **dual-parented**.

**Do not** assume the right oculomotor nucleus is the **right
Edinger-Westphal nucleus**. The **EW** is the **preganglionic
parasympathetic** nucleus (pupil, lens); the **oculomotor** is the
**somatic motor** nucleus (extraocular muscles, levator). They are
**distinct nuclei** in close proximity — the **CN III fascicles
carry BOTH sets of axons**, but the **nuclei are distinct**.

**Do not** assume the right oculomotor nucleus is the **right
trochlear nucleus** (CN IV) or the **right mesencephalic trigeminal
nucleus** (CN Vm). Those are **different nuclei** for **different
cranial nerves**.

**Do not** assume the right oculomotor nucleus **only affects the
right eye**. The **superior rectus subnucleus is CONTRALATERAL**
(right subnucleus → **LEFT** superior rectus) and the **levator
subnucleus is BILATERAL** (central caudal nucleus → both levators).
**These are the two asymmetric subnuclear facts** — **contralateral
superior rectus weakness + bilateral ptosis** — that distinguish a
**nuclear** from a **fascicular** or **nerve** lesion.

**Do not** assume a **nuclear CN III lesion** is the same as a
**fascicular** or **nerve** CN III lesion. The **nuclear** pattern
has **contralateral superior rectus weakness + bilateral ptosis** and
**no contralateral hemiplegia**. The **fascicular** pattern (Weber,
Benedikt, Claude, Nothnagel) has **no nuclear-source contralateral
findings** and (in Weber) **contralateral hemiplegia**. The **nerve**
pattern (PCom aneurysm, microvascular) is **pupil-involving or
pupil-sparing** with **no brainstem signs at all**.

**Do not** conflate the right oculomotor nucleus with the **right
MLF**. The **MLF** is a **conduction pathway**. A **right MLF
lesion** produces **right internuclear ophthalmoplegia (INO)** — **NOT
a right CN III palsy**. **INO is a common differential for a right
medial rectus palsy** — a **right CN III medial rectus palsy** is a
**nuclear/fascicular/nerve lesion**; a **right INO** is an **MLF
lesion**.

**Do not** conflate the right oculomotor nucleus with the **right
PPRF**. The **PPRF** is a **pontine premotor saccade generator**.
A **right PPRF lesion** produces **right horizontal gaze palsy** —
**NOT a right CN III palsy**.

**Do not** conflate the right oculomotor nucleus with the **right
riMLF** or the **right interstitial nucleus of Cajal**. Those are
**vertical gaze centers** — **premotor saccade generators** — not
CN nuclei.

**Do not** conflate the right oculomotor nucleus with the **right
superior colliculus** (tectum — drives the oculomotor nucleus for
saccades) or with the **pretectal nuclei** (diencephalon —
afferent relay of the pupillary light reflex, projecting to the EW
nucleus, not the oculomotor nucleus).

**Do not** conflate the right oculomotor nucleus with the **CN III
nerve** or the **CN III fascicles**. The **nerve** is peripheral;
the **fascicles** are fibers traversing the crus cerebri. **A CN III
fascicular lesion** (Weber syndrome) is a **fascicular** lesion —
**NOT a nuclear lesion**.

**Do not** conflate the right oculomotor nucleus with **myasthenia
gravis** — MG is a **neuromuscular junction** disorder, **not a CN
III nuclear lesion**. MG is **fatigable**, **pupil-sparing**, and
**outside the brainstem**.

**Do not** attribute **pupil constriction** or **lens
accommodation** to the right oculomotor nucleus. Those are the **EW
leaf**. **The oculomotor nucleus is somatic motor.**

**Do not** import the **EW cholinergic phenotype** or the
**oculomotor NMJ nicotinic phenotype** into the midbrain structural
layer. Both are **``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the right oculomotor
nucleus. **Motor nuclei carry NO coupling warning** — same rule as
CN IV, EW, premotor pools, sensor nuclei, and conduction pathways.
**Coordination with the left oculomotor nucleus is via descending
pathways (MLF, posterior commissure, PPRF, riMLF) — not by intrinsic
nucleus-to-nucleus coupling.**

Iterating the right oculomotor nucleus's (empty) children (recommended
consumer pattern)::

    OCULOMOTOR_NUCLEUS_RIGHT_CHILDREN = ()
    # The right oculomotor nucleus is a leaf. The five somatic motor
    # subnuclei (medial rectus, inferior rectus, inferior oblique,
    # superior rectus — CONTRALATERAL (LEFT superior rectus), and
    # central caudal / levator palpebrae — BILATERAL) are prose, not
    # modules.

Reaching the **functional parent** (``cranial_nerve_nuclei/right/``)::

    # The functional parent is the right side container of the
    # cranial_nerve_nuclei functional grouping:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right
    #
    # The right oculomotor nucleus is a child of BOTH the functional
    # parent and the topographic parent (see below).

Reaching the **topographic parent** (``tegmentum/right/``)::

    # The topographic parent is the right side container of the
    # tegmentum topographic container — the SUPERSET:
    #
    #   brainparts.midbrain.tegmentum.right
    #
    # The right oculomotor nucleus is a child of BOTH the topographic
    # parent and the functional parent (see above).

Reaching the right Edinger-Westphal nucleus (recommended consumer
pattern — the SIBLING CN III NUCLEUS)::

    # The right Edinger-Westphal nucleus is the CN III PREGANGLIONIC
    # PARASYMPATHETIC nucleus — pupil and lens:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right.edinger_westphal_nucleus
    #   OR: brainparts.midbrain.tegmentum.right.edinger_westphal_nucleus
    #
    # The right EW is PREGANGLIONIC PARASYMPATHETIC; the right
    # oculomotor nucleus is SOMATIC MOTOR. They are DIFFERENT NUCLEI
    # of the SAME NERVE (CN III), in close proximity. The CN III
    # fascicles carry BOTH sets of axons.

Reaching the right trochlear nucleus (recommended consumer pattern —
the CN IV nucleus)::

    # The right trochlear nucleus is the CN IV SOMATIC MOTOR nucleus
    # — superior oblique (the LEFT superior oblique, because the
    # right trochlear decussates):
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right.trochlear_nucleus
    #   OR: brainparts.midbrain.tegmentum.right.trochlear_nucleus
    #
    # The right trochlear nucleus is a DIFFERENT CRANIAL NERVE
    # (CN IV) than the right oculomotor nucleus (CN III).

Reaching the right mesV (recommended consumer pattern — the CN Vm
SENSORY nucleus)::

    # The right mesencephalic trigeminal nucleus (mesV) is the CN V
    # PRIMARY SENSORY (proprioceptive) nucleus:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right.mesencephalic_trigeminal_nucleus
    #   OR: brainparts.midbrain.tegmentum.right.mesencephalic_trigeminal_nucleus
    #
    # The right mesV is PRIMARY SENSORY (CN V); the right oculomotor
    # nucleus is SOMATIC MOTOR (CN III). They are DIFFERENT NUCLEI
    # in DIFFERENT functional systems.

Reaching the right MLF (recommended consumer pattern — the CONDUCTION
PATHWAY, NOT a CN nucleus)::

    # The MLF is a CONDUCTION PATHWAY — a longitudinal fiber tract —
    # that coordinates the CN III, CN IV, and CN VI nuclei for
    # conjugate gaze:
    #
    #   brainparts.hindbrain.myelencephalon.medulla_oblongata...
    #   medial_longitudinal_fasciculus
    #
    # A right MLF lesion produces RIGHT INTERNUCLEAR OPHTHALMOPLEGIA
    # (INO) — NOT a right CN III palsy. The medial rectus is the
    # ADDUCTING muscle — a right medial rectus palsy is a NUCLEAR/
    # FASCICULAR/NERVE CN III lesion; a right INO is an MLF lesion.

Reaching the right PPRF (recommended consumer pattern — the
HORIZONTAL SACCADE GENERATOR, NOT a CN nucleus)::

    # The right PPRF is the HORIZONTAL SACCADE GENERATOR — a pontine
    # premotor structure that projects to the right abducens nucleus
    # and, via the MLF, to the left oculomotor nucleus's medial
    # rectus subnucleus for conjugate horizontal gaze:
    #
    #   brainparts.hindbrain.metencephalon.pons.pprf
    #
    # A right PPRF lesion produces RIGHT HORIZONTAL GAZE PALSY —
    # NOT a right CN III palsy.

Reaching the right riMLF and the right interstitial nucleus of Cajal
(recommended consumer pattern — the VERTICAL GAZE CENTERS, NOT CN
nuclei)::

    # The right riMLF and the right interstitial nucleus of Cajal are
    # VERTICAL GAZE CENTERS — premotor saccade generators — NOT CN
    # nuclei:
    #
    #   brainparts.midbrain.tegmentum.right.riMLF
    #   brainparts.midbrain.tegmentum.right.interstitial_nucleus_of_cajal
    #
    # They are tegmentum leaves but are NOT cross-listed under
    # cranial_nerve_nuclei.

Reaching the right superior colliculus (recommended consumer pattern —
the SACCADE DRIVER, NOT the oculomotor nucleus)::

    # The right superior colliculus is a TECTUM structure — the
    # visual/oculomotor orienting structure that drives the CN III
    # nuclei for SACCADES (via the tectobulbar tract):
    #
    #   brainparts.midbrain.tectum.right.superior_colliculus
    #
    # The superior colliculus DRIVES the oculomotor nucleus; it is
    # NOT the oculomotor nucleus.

Reaching the right CN III fascicles (recommended consumer pattern —
the FIBERS traversing the crus cerebri)::

    # The right CN III fascicles traverse the right crus cerebri (the
    # right cerebral peduncle) en route to the interpeduncular fossa.
    # A lesion here (e.g., WEBER SYNDROME) produces right CN III
    # palsy + left hemiplegia — a FASCICULAR lesion, NOT a nuclear
    # lesion:
    #
    #   brainparts.midbrain.cerebral_peduncle.right.crus_cerebri
    #
    # The oculomotor nucleus and the CN III fascicles are DIFFERENT
    # STRUCTURES — nucleus vs. fibers.

Reaching the CN III nerve (recommended consumer pattern — the
PERIPHERAL bundle)::

    # The CN III nerve is the PERIPHERAL axon bundle — NOT a midbrain
    # structure:
    #
    #   peripheral.cranial_nerves.oculomotor
    #
    # The right oculomotor axons travel IN the CN III nerve, but the
    # nerve is NOT the nucleus. A PCom aneurysm compresses the
    # SUPERFICIAL pupillomotor (EW) fibers on the nerve — a NERVE
    # lesion, NOT a nuclear lesion.

Reaching the pretectal nuclei (recommended consumer pattern — the
DIENCEPHALON, NOT the oculomotor nucleus)::

    # The pretectal nuclei — the olivary pretectal nucleus and the
    # nucleus of the optic tract — are DIENCEPHALON. They are the
    # AFFERENT relay of the pupillary light reflex and they project
    # to the EDINGER-WESTPHAL nucleus — NOT to the oculomotor
    # nucleus:
    #
    #   brainparts.forebrain.diencephalon.pretectal_nuclei
    #
    # The pretectal nuclei are DIFFERENT STRUCTURES in a DIFFERENT
    # functional system (preganglionic parasympathetic) than the
    # oculomotor nucleus (somatic motor).

Reaching the left oculomotor nucleus (recommended consumer pattern —
the SIDE mirror, with the TWO ASYMMETRIC SUBNUCLEAR FACTS)::

    # The left oculomotor nucleus is the LEFT CN III somatic motor
    # nucleus:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #
    # The two oculomotor nuclei are PAIRED and SYMMETRIC in their
    # cell-body locations. BUT their SUBNUCLEAR PROJECTIONS are NOT
    # strict mirrors:
    #   - SUPERIOR RECTUS subnucleus — CONTRALATERAL (right subnucleus
    #     -> LEFT superior rectus; left subnucleus -> RIGHT superior
    #     rectus) — the only CN III subnucleus that decussates.
    #   - LEVATOR subnucleus — BILATERAL (central caudal nucleus —
    #     single midline subnucleus — innervates both levator
    #     palpebrae).
    #
    # These two asymmetric facts are the diagnostic signature of a
    # NUCLEAR CN III lesion — contralateral superior rectus weakness
    # + bilateral ptosis.

Reaching myasthenia gravis (recommended consumer pattern — the NMJ,
NOT a CN III nuclear lesion)::

    # Myasthenia gravis is a NEUROMUSCULAR JUNCTION disorder —
    # fatigable ptosis and diplopia — NOT a CN III nuclear lesion:
    #
    #   peripheral.neuromuscular_junction.myasthenia_gravis
    #
    # The lesion is at the NMJ — OUTSIDE the brainstem. MG is
    # pupil-sparing.

Bilateral iteration (recommended consumer pattern — NOTE the
no-coupling-warning rule and the TWO ASYMMETRIC SUBNUCLEAR FACTS)::

    for side in ("left", "right"):
        for nucleus in (
            "oculomotor_nucleus",
            "trochlear_nucleus",
            "mesencephalic_trigeminal_nucleus",
            "edinger_westphal_nucleus",
        ):
            # Either path resolves to the same leaf — use ONE:
            path = (
                f"midbrain.cranial_nerve_nuclei.{side}.{nucleus}"
            )
            # OR:
            # path = f"midbrain.tegmentum.{side}.{nucleus}"
            #
            # resolve path through the memory/recall layer
            #
            # NOTE: the CN nuclei are MOTOR NUCLEI (CN III, CN IV),
            # a SENSORY NUCLEUS (CN Vm), and a PREGANGLIONIC
            # PARASYMPATHETIC NUCLEUS (Edinger-Westphal). NONE
            # carries a coupling warning. Coordination with the
            # contralateral side is via descending pathways (MLF,
            # posterior commissure, PPRF, riMLF) or via upstream
            # bilateral projections (pretectal for the pupillary
            # light reflex), not intrinsic nucleus-to-nucleus
            # coupling.
            #
            # NOTE: for the OCULOMOTOR nucleus specifically, the
            # SUBNUCLEAR PROJECTIONS are NOT strict mirrors — the
            # superior rectus subnucleus is CONTRALATERAL and the
            # levator subnucleus is BILATERAL. A NUCLEAR CN III
            # lesion produces CONTRALATERAL superior rectus weakness
            # + BILATERAL ptosis — the diagnostic signature of a
            # nuclear (vs. fascicular or nerve) lesion.

Subnuclear-organization detail (not wired — consult references)::

    # The right oculomotor nucleus has five SOMATIC MOTOR subnuclei:
    #
    #   medial rectus subnucleus    -> IPSILATERAL (right medial
    #                                   rectus) — adduction of the
    #                                   right eye; MOST
    #                                   VENTROLATERAL subnucleus —
    #                                   most commonly affected in
    #                                   CN III palsy
    #   inferior rectus subnucleus  -> IPSILATERAL (right inferior
    #                                   rectus) — depression of the
    #                                   right eye
    #   inferior oblique subnucleus -> IPSILATERAL (right inferior
    #                                   oblique) — elevation of the
    #                                   right eye (in adduction)
    #   superior rectus subnucleus  -> CONTRALATERAL (LEFT superior
    #                                   rectus) — elevation of the
    #                                   LEFT eye (in adduction) —
    #                                   THE ONLY CN III SUBNUCLEUS
    #                                   THAT DECUSSATES
    #   central caudal nucleus      -> BILATERAL (both right and
    #                                   left levator palpebrae) —
    #                                   elevation of BOTH upper
    #                                   eyelids — SINGLE MIDLINE
    #                                   SUBNUCLEUS
    #
    # The two asymmetric facts — CONTRALATERAL superior rectus and
    # BILATERAL levator — are the diagnostic signature of a NUCLEAR
    # CN III lesion. For the RIGHT nucleus specifically:
    #   - RIGHT superior rectus subnucleus -> LEFT superior rectus
    #   - RIGHT central caudal nucleus -> BOTH levators
    #   - A RIGHT nuclear CN III lesion -> RIGHT eye findings + LEFT
    #     superior rectus weakness + bilateral ptosis.
    #
    # Do not attempt to resolve these subnuclei as sub-paths of the
    # oculomotor nucleus — they are PROSE, not modules.

Clinical-pattern detail (not wired — consult references)::

    # The right oculomotor nucleus is the RIGHT CN III SOMATIC MOTOR
    # nucleus. The CLINICAL PATTERNS of the related lesions are
    # DISTINCT:
    #
    #   right NUCLEAR CN III lesion -> right eye findings (ptosis,
    #                                   down and out, impaired
    #                                   adduction/depression/
    #                                   elevation-in-adduction) +
    #                                   LEFT superior rectus
    #                                   weakness (CONTRALATERAL
    #                                   subnucleus) + BILATERAL
    #                                   ptosis (if central caudal
    #                                   nucleus involved) —
    #                                   RARE in practice
    #   right FASCICULAR CN III     -> right CN III palsy INCLUDING
    #     lesion (Weber syndrome)       mydriasis (EW fibers
    #                                   involved) PLUS left
    #                                   hemiplegia; lesion SITE is
    #                                   the crus cerebri, not the
    #                                   nucleus
    #   right FASCICULAR CN III     -> right CN III palsy + left
    #     lesion (Benedikt)             ataxia / tremor (red nucleus
    #                                   + superior cerebellar
    #                                   peduncle involvement)
    #   right FASCICULAR CN III     -> right CN III palsy + left
    #     lesion (Claude)               ataxia (less complete
    #                                   Benedikt)
    #   right FASCICULAR CN III     -> right CN III palsy +
    #     lesion (Nothnagel)            ipsilateral cerebellar signs
    #   right NERVE CN III lesion   -> right CN III palsy —
    #     (PCom aneurysm)               PUPIL-INVOLVING (mydriasis)
    #                                   from compression of
    #                                   SUPERFICIAL pupillomotor
    #                                   fibers
    #   right NERVE CN III lesion   -> right CN III palsy —
    #     (microvascular)               PUPIL-SPARING (ischemia
    #                                   affects the core of the
    #                                   nerve, sparing the
    #                                   superficial pupillomotor
    #                                   fibers)
    #   right MLF lesion (INO)      -> right adduction weakness with
    #                                   left abducting nystagmus —
    #                                   NOT a CN III palsy; PUPILS
    #                                   TYPICALLY SPARED
    #   right PPRF lesion           -> right horizontal gaze palsy —
    #                                   NOT a CN III palsy
    #   myasthenia gravis           -> fatigable ptosis and diplopia
    #                                   — PUPIL-SPARING — NOT a
    #                                   brainstem lesion
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # STRUCTURES.

References
----------
*   **Canonical oculomotor nucleus anatomy:** Büttner-Ennever,
    J.A. (2006). *Neuroanatomy of the Oculomotor System*. (The
    oculomotor nucleus — its subnuclear organization, the
    contralateral superior rectus subnucleus, the central caudal
    levator subnucleus; the oculomotor / Edinger-Westphal split.)
*   **Oculomotor nucleus — subnuclear organization:** Warwick, R.
    (1953). "Representation of the extraocular muscles in the
    oculomotor nuclei of the monkey." *Journal of Comparative
    Neurology* 98:449–503. (The classic subnuclear mapping of the
    oculomotor nucleus — the five somatic motor subnuclei, the
    contralateral superior rectus subnucleus, the central caudal
    levator subnucleus.)
*   **Contralateral superior rectus subnucleus:** Miyazaki, S.
    (1985). "Location of motoneurons innervating the superior
    rectus muscle in the oculomotor nucleus of the cat."
    *Neuroscience Letters* 55:227–231. (The contralateral
    projection of the superior rectus subnucleus — the only CN III
    subnucleus that decussates.)
*   **Central caudal nucleus (levator subnucleus):** Spencer, R.F.,
    Porter, J.D. (1981). "Innervation and structure of extraocular
    muscles in the monkey in comparison to those of the cat."
    *Journal of Comparative Neurology* 198:649–665. (The central
    caudal nucleus — the single midline levator subnucleus,
    innervating both levator palpebrae superioris.)
*   **Nuclear CN III palsy — clinical:** Brazis, P.W., Masdeu,
    J.C., Biller, J. (2007). *Localization in Clinical
    Neurology*, 5th ed. (The nuclear CN III palsy pattern —
    contralateral superior rectus weakness, bilateral ptosis,
    distinction from fascicular and nerve patterns.)
*   **Weber syndrome (cross-reference — NOT this leaf):** Weber,
    H.D. (1856). "A contribution to the pathology of the crura
    cerebri." *Medico-Chirurgical Transactions* 39:121–140. (The
    original description of alternating oculomotor hemiplegia —
    the CN III fascicular lesion in the crus cerebri; the lesion
    site is the crus, NOT the oculomotor nucleus.)
*   **Benedikt syndrome (contrast — fascicular + red nucleus):**
    Benedikt, M. (1889). "Krankenvorstellung." *Wiener
    Medicinische Presse* 30:1–4. (Benedikt syndrome — CN III
    fascicles + red nucleus — FASCICULAR, NOT nuclear.)
*   **Claude syndrome (contrast — fascicular + red nucleus):**
    Claude, H., Loyez, M. (1912). "Ramollissement du noyau rouge."
    *Revue Neurologique* 23:49–51. (Claude syndrome — CN III
    fascicles + red nucleus — FASCICULAR, NOT nuclear.)
*   **Nothnagel syndrome (contrast — tectum / superior cerebellar
    peduncle):** Nothnagel, C.W.H. (1879). "Ein Fall von
    Ophthalmoplegie mit Kleinhirnsymptomen." *Deutsche
    Medicinische Wochenschrift* 5:429–430. (Nothnagel syndrome —
    CN III + ipsilateral cerebellar signs — TECTUM, NOT nuclear.)
*   **PCom aneurysm CN III palsy (contrast — nerve):** Trobe, J.D.
    (2012). *The Neurology of Vision*, 5th ed. (The pupil-involving
    CN III palsy — compression of the SUPERFICIAL pupillomotor
    (EW) fibers on the CN III nerve by a posterior communicating
    artery aneurysm — NERVE lesion, NOT nuclear.)
*   **Microvascular CN III palsy (contrast — nerve):** Jacobson,
    D.M., Trobe, J.D. (1999). "The emerging role of magnetic
    resonance angiography in the management of patients with third
    cranial nerve palsy." *Journal of Neuro-Ophthalmology*
    19:147–151. (The pupil-sparing CN III palsy — microvascular
    ischemia affecting the core of the nerve and sparing the
    SUPERFICIAL pupillomotor fibers — NERVE lesion, NOT nuclear.)
*   **INO and the MLF (contrast — conduction pathway):** Frohman,
    T.C., Galetta, S.L., Fox, R.J., Solomon, D., Straumann, D.,
    Filippi, M., Zee, D.S., Frohman, E.M. (2008). "Pearls &
    Oy-sters: The medial longitudinal fasciculus in ocular motor
    physiology." *Neurology* 70:e57–e67. (The MLF as the
    internuclear pathway coordinating CN III, IV, VI for conjugate
    gaze; INO as the MLF lesion syndrome — distinct from CN III
    nuclear or fascicular palsy.)
*   **PPRF and horizontal gaze (contrast — pontine premotor
    saccade generator):** Cohen, B., Komatsuzaki, A. (1972). "Eye
    movements induced by stimulation of the pontine reticular
    formation: evidence for integration in oculomotor pathways."
    *Experimental Neurology* 36:101–117. (The PPRF as the
    horizontal saccade generator — a premotor structure that
    DRIVES the oculomotor nucleus, but is NOT the oculomotor
    nucleus.)
*   **riMLF and vertical gaze (contrast — vertical gaze center):**
    Büttner-Ennever, J.A., Büttner, U. (1988). "The reticular
    formation." In *Neuroanatomy of the Oculomotor System*
    (Büttner-Ennever, ed.). (The riMLF and the interstitial
    nucleus of Cajal as vertical gaze centers — premotor saccade
    generators, NOT CN nuclei.)
*   **Superior colliculus (contrast — tectum):** Sparks, D.L.
    (2002). "The brainstem control of saccadic eye movements."
    *Nature Reviews Neuroscience* 3:952–964. (The superior
    colliculus driving the CN III nuclei for saccades — DRIVES the
    oculomotor nucleus, but is NOT the oculomotor nucleus.)
*   **Pretectal nuclei (contrast — diencephalon):** Gamlin, P.D.R.
    (2002). "The pupillary light reflex and its brainstem
    pathways." In *Neuro-Ophthalmology* (Miller et al., eds.).
    (The pretectal nucleus as the afferent relay of the pupillary
    light reflex, projecting to the EDINGER-WESTPHAL nucleus —
    NOT the oculomotor nucleus.)
*   **Edinger-Westphal nucleus (sibling — CN IIIp):** Kozicz, T.,
    Bittencourt, J.C., May, P.J., Reiner, A., Gamlin, P.D.R.,
    Palkovits, M., Horn, A.K.E. (2011). "The Edinger-Westphal
    nucleus: a historical, structural, and functional appraisal
    of the urocortin-1 containing centrally projecting neuron
    population, and its comparison to the parasympathetic and
    preganglionic neurons of the oculomotor nucleus." *Brain
    Structure and Function* 216:1–19. (The EWpg / EWcp
    distinction — the EWpg is the preganglionic parasympathetic
    nucleus of CN III, the SIBLING of the somatic motor oculomotor
    nucleus.)
*   **Myasthenia gravis (contrast — NMJ):** Drachman, D.B. (1994).
    "Myasthenia gravis." *New England Journal of Medicine*
    330:1797–1810. (Myasthenia gravis as a neuromuscular junction
    disorder — fatigable ptosis, pupil-sparing, NOT a brainstem
    lesion.)
*   **SLEA (contrast — the right oculomotor nucleus is not SLEA):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the oculomotor nucleus.)
*   NeuroNames — Oculomotor nucleus (right); FMA — Oculomotor
    nucleus (right member).
"""