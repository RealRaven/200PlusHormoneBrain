"""
infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left.trochlear_nucleus
=============================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── cranial_nerve_nuclei
    │   ├── left
    │   │   ├── oculomotor_nucleus
    │   │   ├── trochlear_nucleus               <-- THIS MODULE
    │   │   │                                       (leaf — FUNCTIONAL
    │   │   │                                       parent)
    │   │   ├── mesencephalic_trigeminal_nucleus
    │   │   └── edinger_westphal_nucleus
    │   └── right
    │       └── ...
    └── tegmentum
        ├── left
        │   ├── oculomotor_nucleus
        │   ├── trochlear_nucleus               (SAME LEAF —
        │   │                                       TOPOGRAPHIC
        │   │                                       parent)
        │   ├── mesencephalic_trigeminal_nucleus
        │   ├── edinger_westphal_nucleus
        │   ├── substantia_nigra
        │   └── ...
        └── right
            └── ...

**Primary synonym:** Left trochlear nucleus; left CN IV nucleus; left
nucleus of the trochlear nerve; left nucleus of the fourth cranial
nerve; **the left CN IV somatic motor nucleus**.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **somatic motor nucleus** in the **caudal midbrain
tegmentum**, at the **level of the inferior colliculus** — **caudal
to the oculomotor nucleus** (which is at the level of the
**superior colliculus**). It is the **smallest** of the cranial nerve
motor nuclei — a compact cluster of **~1,700 motoneurons** in the
human. It is a **paired** nucleus (left and right), with a
**single motor pool** — the **superior oblique** motoneurons — and
**no distinct subnuclei** (unlike the oculomotor nucleus). See
*The Two Defining Facts of the Trochlear Nucleus* below.
**Part of:** The **cranial_nerve_nuclei** functional grouping
container → **left** side container (functional parent), **and** the
**tegmentum** topographic container → **left** side container
(topographic parent). **Dual-parent leaf — see *Structural parent*
below and *Cross-Listing Statement*.**
**Structural parent (FUNCTIONAL):** ``.../cranial_nerve_nuclei/left/``
→ **direct child** of the **left side container** of the
cranial_nerve_nuclei functional grouping container.
**Structural parent (TOPOGRAPHIC):** ``.../tegmentum/left/`` →
**direct child** of the **left side container** of the tegmentum
topographic container.
**Structural children:** **None.** This is a **leaf** module. The
**single motor pool** — the **superior oblique** motoneurons — is
**the whole nucleus**, not a structural child. The **only CN IV
target muscle** is documented as **prose**, not as a structural
child.
**Boundary status (DUAL-PARENT LEAF — CROSS-LISTED between
``cranial_nerve_nuclei/left/`` and ``tegmentum/left/``):** **Boundary
case — the left trochlear nucleus is a DUAL-PARENT LEAF.** It is
reachable by **two** structural paths:
*   **Functional path** —
    ``.../cranial_nerve_nuclei/left/trochlear_nucleus/``
*   **Topographic path** —
    ``.../tegmentum/left/trochlear_nucleus/``
**Both resolve to the SAME leaf** — this module. Consumers resolving
the leaf by **either** path get **the same module**. Consumers must
**not** assume the two paths lead to different structures — they lead
to **one leaf**, dual-parented. See *Cross-Listing Statement*.
**Boundary status (THE DEFINING FACT OF THE TROCHLEAR NUCLEUS —
DECUSSATION BEFORE EXIT):** **Boundary case — the left trochlear
nucleus innervates the **RIGHT** superior oblique — the
**CONTRALATERAL** muscle.** The **left trochlear nucleus's axons
DECUSSATE** within the **superior medullary velum** — the thin roof
of the **fourth ventricle** — **before exiting the brainstem** and
**before** the nerve proper is formed. **This is the ONLY cranial
nerve whose fibers cross BEFORE exiting the brainstem.** Every other
CN — including **CN III** — either **does not decussate** or
**decussates at the level of the target muscle** (e.g.,
**oculomotor's superior rectus subnucleus** — the one exception
inside CN III). **The trochlear is the only entire cranial nerve
with this pre-exit decussation.** **A consumer that assumes "left
trochlear nucleus → left superior oblique" is WRONG.** **A LEFT
trochlear nucleus lesion produces a RIGHT superior oblique palsy.**
**A RIGHT trochlear nucleus lesion produces a LEFT superior oblique
palsy.** **This is the single most consequential fact about the
leaf** — see *The Two Defining Facts* and *Associated Disorders*.
**Boundary status (THE SECOND DEFINING FACT — DORSAL EXIT):**
**Boundary case — the left trochlear nerve EXITS THE BRAINSTEM
DORSALLY — the only CN to do so.** Every other cranial nerve exits
**ventrally** or **laterally** (CN III ventrally at the
interpeduncular fossa; CN VI ventrally at the pontomedullary
junction; CN IX, X, XI, XII ventrally or laterally at the medulla;
CN VII, VIII laterally at the cerebellopontine angle; CN V
laterally at the pons; CN I through the cribriform plate; CN II as
a CNS tract). **The trochlear nerve alone exits DORSALLY** — it
**emerges from the dorsal midbrain** (the only CN whose nerve fibers
**do not cross the ventral surface of the brainstem**), **curves
around the cerebral peduncle**, and continues **ventrally** to the
**superior oblique** in the orbit. This dorsal exit is **the reason
the nerve is vulnerable to head trauma** — the long course around
the brainstem (see *The Trochlear Nerve's Long Peripheral Course*
below) makes it the **most commonly injured cranial nerve in head
trauma**. **A consumer that assumes the trochlear exits ventrally
like the others is WRONG.** See *The Two Defining Facts* and
*Associated Disorders*.
**Boundary status (SOMATIC MOTOR NUCLEUS — NOT a preganglionic
parasympathetic nucleus, NOT a sensory nucleus):** **Boundary case —
the left trochlear nucleus is a **SOMATIC MOTOR** nucleus.** It
innervates the **superior oblique** — a **skeletal muscle** — via
**nicotinic ACh** at the **neuromuscular junction**. It has **no
preganglionic parasympathetic component** (unlike CN III, which has
the Edinger-Westphal nucleus as its parasympathetic sibling), **no
sensory component** (unlike CN V, which has the mesencephalic
trigeminal nucleus), and **no branchiomotor component** (unlike
CN V, VII, IX, X, XI, which are branchiomotor). **CN IV is a pure
somatic motor nerve — the only such CN that innervates a single
muscle.** Consumers must **not** attribute **pupil**, **lens**,
**sensory**, or **branchiomotor** function to this leaf — the
trochlear nucleus is **somatic motor only**.
**Boundary status (NOT the left oculomotor nucleus — the oculomotor
nucleus is CN III):** **Boundary case — the left trochlear nucleus
is NOT the left oculomotor nucleus.** The **left oculomotor nucleus
(CN III)**
(``.../cranial_nerve_nuclei/left/oculomotor_nucleus/`` **and**
``.../tegmentum/left/oculomotor_nucleus/``) is the **CN III somatic
motor** nucleus — it innervates the **five extraocular muscles**
(superior rectus, inferior rectus, medial rectus, inferior oblique)
and the **levator palpebrae superioris**. **They are DIFFERENT
NUCLEI for DIFFERENT CRANIAL NERVES** — the **oculomotor** is
**CN III**; the **trochlear** is **CN IV**. **They are also at
different rostrocaudal levels** — the oculomotor nucleus is at the
**superior colliculus**; the trochlear nucleus is at the **inferior
colliculus** (caudal to the oculomotor). Consumers must **not**
conflate the two.
**Boundary status (NOT the left Edinger-Westphal nucleus — the EW
nucleus is CN IIIp):** **Boundary case — the left trochlear nucleus
is NOT the left Edinger-Westphal nucleus.** The **left EW nucleus**
(``.../cranial_nerve_nuclei/left/edinger_westphal_nucleus/`` **and**
``.../tegmentum/left/edinger_westphal_nucleus/``) is the **CN III
preganglionic parasympathetic** nucleus — pupil and lens. **They are
DIFFERENT NUCLEI for DIFFERENT CRANIAL NERVES** — the **trochlear**
is **CN IV somatic motor**; the **EW** is **CN III preganglionic
parasympathetic**. **The trochlear has NO parasympathetic component**
— it is a pure somatic motor nerve. Consumers must **not** conflate
the two, and must **not** attribute **pupil** or **lens** function
to the trochlear.
**Boundary status (NOT the left mesencephalic trigeminal nucleus —
the mesV is a SENSORY nucleus):** **Boundary case — the left
trochlear nucleus is NOT the left mesencephalic trigeminal nucleus
(mesV).** The **left mesV**
(``.../cranial_nerve_nuclei/left/mesencephalic_trigeminal_nucleus/``
**and** ``.../tegmentum/left/mesencephalic_trigeminal_nucleus/``) is
the **CN V primary sensory (proprioceptive)** nucleus. **They are
DIFFERENT NUCLEI in DIFFERENT functional systems** — the **trochlear**
is **CN IV somatic motor**; the **mesV** is **CN V primary sensory**.
Consumers must **not** conflate the two.
**Boundary status (NOT the MLF — the MLF is a CONDUCTION PATHWAY):**
**Boundary case — the left trochlear nucleus is NOT the left MLF.**
The **medial longitudinal fasciculus (MLF)** is a **longitudinal
fiber tract** — a **conduction pathway** — that **coordinates** the
**CN III**, **CN IV**, and **CN VI** nuclei for **conjugate gaze**.
It is **wired elsewhere** (as a brainstem longitudinal tract). The
**left trochlear nucleus** is a **nucleus** — grey matter. **A left
MLF lesion produces LEFT INTERNUCLEAR OPHTHALMOPLEGIA (INO)** —
**adduction weakness of the left eye with abducting nystagmus of the
right eye** — **NOT a left CN IV nuclear palsy** and **NOT a left
CN IV palsy at all**. **These are DIFFERENT SYNDROMES.** Note that
the **superior oblique** (CN IV) is **not** the **medial rectus**
(which the MLF coordinates) — the INO and the CN IV palsy are
**mechanistically different**: INO is a **conduction pathway**
deficit; CN IV palsy is a **nuclear / fascicular / nerve** deficit.
Consumers must **not** conflate the trochlear nucleus with the MLF,
and must **not** resolve the MLF through the trochlear path. See
*Associated Disorders*.
**Boundary status (NOT the left CN IV nerve — the nerve is
PERIPHERAL, and it has a unique long course):** **Boundary case —
the left trochlear nucleus is NOT the left trochlear nerve.** The
**left trochlear nerve** is the **peripheral axon bundle** — it is
**wired elsewhere** (peripheral nervous system). **The trochlear
nerve has the longest intracranial course of any CN** — it exits
**dorsally** from the midbrain, **curves around the cerebral
peduncle**, passes **between the posterior cerebral artery and the
superior cerebellar artery**, runs along the **free edge of the
tentorium cerebelli**, enters the **cavernous sinus**, and passes
through the **superior orbital fissure** to reach the **superior
oblique**. **The nerve's long course and its dorsal exit make it
the MOST VULNERABLE cranial nerve to head trauma.** **They are
DIFFERENT STRUCTURES** — the **trochlear nucleus** is **grey
matter** in the midbrain; the **trochlear nerve** is **peripheral**
white matter. Consumers must **not** conflate the two, and must
**not** attribute **traumatic CN IV palsy** to a **nuclear** lesion
— the **lesion site in trauma is typically the NERVE**, not the
nucleus. See *Associated Disorders*.
**Boundary status (NOT the left superior oblique — the superior
oblique is the TARGET MUSCLE, and it is CONTRALATERAL):** **Boundary
case — the left trochlear nucleus is NOT the left superior oblique.**
The **superior oblique** is the **target muscle** — it is **NOT a
brainstem structure**, and it is **innervated by the CONTRALATERAL
trochlear nucleus** (the **RIGHT trochlear nucleus** innervates the
**LEFT** superior oblique; the **LEFT trochlear nucleus** innervates
the **RIGHT** superior oblique). **This is the direct consequence of
the pre-exit decussation.** **They are DIFFERENT STRUCTURES across
the CNS-muscle boundary** — and **the side inversion is the defining
fact.** Consumers must **not** conflate the trochlear nucleus with
the superior oblique, and must **not** assume the **left** nucleus
innervates the **left** muscle — it innervates the **right** muscle.
See *The Two Defining Facts*.
**Boundary status (NOT the left inferior oblique or any other
extraocular muscle — the superior oblique is the ONLY target):**
**Boundary case — the left trochlear nucleus innervates **only one
muscle** — the **RIGHT superior oblique**.** The **left inferior
oblique** (innervated by the **left oculomotor nucleus**, CN III),
the **left medial rectus** (CN III), the **left inferior rectus**
(CN III), the **left superior rectus** (CN III, **contralateral**
from the left superior rectus subnucleus — wait, the **left**
superior rectus subnucleus innervates the **RIGHT** superior
rectus), the **left lateral rectus** (CN VI, **ipsilateral**), and
the **left levator palpebrae superioris** (CN III, **bilateral**
from the central caudal nucleus) are **all innervated by OTHER
nuclei**. **The trochlear nucleus is the ONLY source of innervation
to the superior oblique — on the contralateral side.** This is the
**narrowest target of any CN motor nucleus** — a single muscle on
the contralateral side. Consumers must **not** assume the trochlear
nucleus innervates "the extraocular muscles" generally — it
innervates **exactly one muscle, on the contralateral side**.
**Boundary status (NOT the left PPRF, riMLF, or interstitial nucleus
of Cajal — those are GAZE CENTERS, not CN nuclei):** **Boundary
case — the left trochlear nucleus is NOT the left PPRF, the left
riMLF, or the left interstitial nucleus of Cajal.** The **PPRF**
(``.../hindbrain/metencephalon/pons/pprf/``) is the **horizontal
saccade generator**; the **riMLF** and the **interstitial nucleus
of Cajal** (``.../tegmentum/left/``) are the **vertical gaze
centers**. They are **premotor saccade generators**, not **CN
nuclei**. **They are DIFFERENT STRUCTURES in DIFFERENT functional
systems** — the **gaze centers** are **premotor**; the **trochlear
nucleus** is a **CN motor nucleus**. Consumers must **not** conflate
the trochlear nucleus with the gaze centers.
**Boundary status (NOT the left superior colliculus or the left
inferior colliculus — those are TECTUM structures that DRIVE the
CN nuclei but are not the CN nuclei):** **Boundary case — the left
trochlear nucleus is NOT the left superior colliculus, and NOT the
left inferior colliculus.** The **left superior colliculus**
(``.../tectum/left/superior_colliculus/``) is the **visual and
oculomotor orienting** structure; the **left inferior colliculus**
(``.../tectum/left/inferior_colliculus/``) is the **auditory relay**.
**Neither is a CN nucleus.** They are **tectum** structures **at the
same rostrocaudal level** as the trochlear nucleus (the trochlear
nucleus is at the **inferior colliculus** level). The **superior
colliculus DRIVES the oculomotor and trochlear nuclei for saccades
and orienting** via the tectobulbar tract — but **the colliculi
themselves are not CN nuclei**. Consumers must **not** conflate the
trochlear nucleus with the colliculi, even though they are at
**overlapping rostrocaudal levels**.
**Boundary status (NOT the right trochlear nucleus — the SIDE
boundary; the DECUSSATION is the ASYMMETRY):** **Boundary case — the
left trochlear nucleus is NOT the right trochlear nucleus, and the
two are NOT a strict mirror in their **target muscles**.** The
**right trochlear nucleus**
(``.../cranial_nerve_nuclei/right/trochlear_nucleus/`` **and**
``.../tegmentum/right/trochlear_nucleus/``) is the **right** CN IV
somatic motor nucleus. The two are **paired structures** that are
**bilaterally symmetric in their cell-body locations** but
**innervate the CONTRALATERAL superior oblique each**:
*   **Left trochlear nucleus** — **LEFT** nucleus — innervates the
    **RIGHT** superior oblique.
*   **Right trochlear nucleus** — **RIGHT** nucleus — innervates
    the **LEFT** superior oblique.
**A consumer that assumes "left trochlear nucleus = left superior
oblique" will be WRONG** — the **left nucleus innervates the right
muscle**, and the **right nucleus innervates the left muscle**.
**This is the defining asymmetric fact of the pair** — and it is
**the same fact on both sides**, just with the muscle flipped. The
two nuclei are **strict mirrors in their locations** but
**innervate opposite muscles** — the "strict mirror" is structural
in location but **not** in **target**. See *Lateralization Notes*
and *Design Contract*.
**Boundary status (SOMATIC MOTOR NUCLEUS — NOT a sensory nucleus, NOT
a preganglionic parasympathetic nucleus, NOT an oscillator, NOT a
premotor pool, NOT a conduction pathway):** **Boundary case — the
left trochlear nucleus is a SOMATIC MOTOR NUCLEUS.** In the family's
**structure-class taxonomy**, it is a **motor nucleus** — the **same
class** as the oculomotor nucleus (CN III somatic) and the EW
nucleus (CN IIIp) — **not** a sensory nucleus (CN Vm), **not** an
oscillator, **not** a premotor pool, **not** a conduction pathway,
and **not** a grey-matter processing nucleus (substantia nigra, red
nucleus). **Motor nuclei carry NO coupling warning** — same rule as
premotor pools, sensor nuclei, conduction pathways, and the EW and
oculomotor nuclei. Its coordination with the **right trochlear
nucleus** (via the **MLF** for conjugate gaze) and with the other
extraocular motor nuclei is via **descending pathways** — **not**
intrinsic nucleus-to-nucleus coupling. It is a **paired mirror with
NO coupling warning** — **but with the pre-exit decussation as its
defining asymmetry** (see *Lateralization Notes* and *Design
Contract*).

Overview
--------
The left trochlear nucleus is the **left CN IV somatic motor
nucleus** — the **somatic motor component of CN IV** — in the
**left caudal midbrain tegmentum**, at the **level of the inferior
colliculus**, **ventral to the periaqueductal gray** and **dorsal
to the MLF**. It innervates the **RIGHT superior oblique** (the
**contralateral** muscle — because the trochlear fibers
**decussate before exiting**), and it is the **only CN whose
nucleus has a single target muscle on a single side**. It is a
**dual-parent leaf** — reachable by **both** the functional path
(``.../cranial_nerve_nuclei/left/trochlear_nucleus/``) and the
topographic path
(``.../tegmentum/left/trochlear_nucleus/``).

**The left trochlear nucleus innervates the RIGHT superior
oblique.** This is the **defining fact** — the trochlear is the
**only CN whose fibers decussate before exiting the brainstem**.
**A consumer that reasons "left nucleus → left muscle" is WRONG.**
A **left trochlear nucleus lesion** produces a **RIGHT** superior
oblique palsy. A **right trochlear nucleus lesion** produces a
**LEFT** superior oblique palsy. **This inversion is the
characteristic consumer-facing hazard of the leaf.**

**The left trochlear nucleus is at the level of the INFERIOR
COLLICULUS — CAUDAL to the oculomotor nucleus** (which is at the
**superior colliculus**). The two CN III-related nuclei (oculomotor
and EW) and the CN IV nucleus (trochlear) are **in a rostrocaudal
sequence** in the midbrain tegmentum — oculomotor + EW at the
superior colliculus level; trochlear at the inferior colliculus
level. **This rostrocaudal ordering is a useful landmark** — and it
is why CN IV is the **caudal-most midbrain CN nucleus**.

**The left trochlear nucleus is a MOTOR NUCLEUS in the family's
taxonomy.** It carries **NO coupling warning** — same rule as CN III
(oculomotor, EW), premotor pools, sensor nuclei, and conduction
pathways. Coordination with the **right trochlear nucleus** is via
the **MLF** and **descending pathways** — **not** intrinsic
nucleus-to-nucleus coupling.

**The left trochlear nucleus is a dual-parent leaf.** Both
structural parents are named together — the **functional parent**
(``.../cranial_nerve_nuclei/left/``) and the **topographic parent**
(``.../tegmentum/left/``). Consumers resolving the leaf by **either**
path get **this module**.

The Two Defining Facts of the Trochlear Nucleus
----------------------------------------------
**Two facts define the trochlear nucleus and make it unlike any
other CN motor nucleus.** A consumer who reads the rest of the leaf
without absorbing these two is likely to make both of the classic
errors described below.

**Fact 1 — Decussation before exit (the ONLY CN with this
property).** The **left trochlear nucleus's axons DECUSSATE** within
the **superior medullary velum** — the thin roof of the **fourth
ventricle** — **before exiting the brainstem** and **before the
nerve proper is formed**. **Every other CN — including CN III —
either does not decussate, or decussates at the level of the target
muscle (the oculomotor's superior rectus subnucleus is the one
exception inside CN III).** The **trochlear is the only entire CN
with a pre-exit decussation.** **Consequence:** the **left
trochlear nucleus innervates the RIGHT superior oblique**, and the
**right trochlear nucleus innervates the LEFT superior oblique**.
**A left trochlear nucleus lesion produces a RIGHT superior oblique
palsy; a right trochlear nucleus lesion produces a LEFT superior
oblique palsy.**

**Fact 2 — Dorsal exit (the ONLY CN with this property).** The
**left trochlear nerve EXITS THE BRAINSTEM DORSALLY** — from the
**dorsal midbrain** — and **curves around the cerebral peduncle**
and the **midbrain** to reach the **ventral surface** and the
**orbit**. **No other CN exits dorsally.** CN III exits ventrally
at the interpeduncular fossa; CN VI ventrally at the
pontomedullary junction; CN V laterally at the pons; CN VII and
VIII laterally at the cerebellopontine angle; CN IX, X, XI, XII
ventrally or laterally at the medulla; CN I through the cribriform
plate; CN II as a CNS tract. **The trochlear is the only CN that
does not cross the ventral surface of the brainstem as a nerve.**
**Consequence:** the **trochlear nerve has a unique, long, and
vulnerable peripheral course** — it is the **longest intracranial
course of any CN**, and it passes **between the posterior cerebral
artery and the superior cerebellar artery**, along the **free edge
of the tentorium cerebelli**, through the **cavernous sinus**, and
through the **superior orbital fissure**. **This is why the
trochlear is the MOST VULNERABLE cranial nerve to head trauma.**

**These two facts — decussation and dorsal exit — are the two things
that distinguish the trochlear nucleus from every other CN motor
nucleus.** Everything else in the leaf is downstream of them.

The Trochlear Nerve's Long Peripheral Course (the trauma
vulnerability)
----------------------------------------------------------------
The **trochlear nerve's peripheral course** is the **longest
intracranial course of any CN** — and it is why CN IV palsy is the
**most common CN palsy after head trauma**. The path (from the
**left trochlear nucleus** to the **RIGHT superior oblique**):

*   **Origin** — the **left trochlear nucleus** (caudal midbrain
    tegmentum, at the level of the inferior colliculus).
*   **Decussation** — **within the superior medullary velum** — the
    left nucleus's axons **cross to the right** before exiting.
*   **Dorsal exit** — the **right trochlear nerve** emerges from
    the **dorsal midbrain**, **curving around the right cerebral
    peduncle**.
*   **Subarachnoid course** — between the **posterior cerebral
    artery** and the **superior cerebellar artery** — the **nerve is
    vulnerable to compression by aneurysms or masses** here.
*   **Tentorial edge** — along the **free edge of the tentorium
    cerebelli** — vulnerable to **tentorial herniation**.
*   **Cavernous sinus** — along the **lateral wall** of the
    cavernous sinus (along with CN III, V1, V2, VI).
*   **Superior orbital fissure** — entering the **orbit**.
*   **Target** — the **RIGHT superior oblique**.

**This long course makes the trochlear nerve vulnerable to trauma,
compression, and ischemia along its entire peripheral path.** The
**nucleus** (this leaf) is only **one** of the many potential
lesion sites — and in **head trauma**, the lesion is almost always
in the **nerve**, not the **nucleus**.

The Left Trochlear Nucleus / Left Oculomotor Nucleus Boundary
-------------------------------------------------------------
This is the **CN IV / CN III** boundary — and the **rostrocaudal
ordering**:

*   **Left trochlear nucleus** (this module) — **CN IV somatic
    motor** — **superior oblique** — **inferior colliculus level**.

*   **Left oculomotor nucleus**
    (``.../cranial_nerve_nuclei/left/oculomotor_nucleus/`` **and**
    ``.../tegmentum/left/oculomotor_nucleus/``) — **CN III somatic
    motor** — five extraocular muscles and levator palpebrae
    superioris — **superior colliculus level**.

**They are DIFFERENT NUCLEI for DIFFERENT CRANIAL NERVES, at
DIFFERENT rostrocaudal levels** — the **oculomotor** is **rostral**
(superior colliculus); the **trochlear** is **caudal** (inferior
colliculus). Consumers must **not** conflate the two.

The Left Trochlear Nucleus / Left Edinger-Westphal Nucleus Boundary
-------------------------------------------------------------------
This is the **CN IV / CN IIIp** boundary:

*   **Left trochlear nucleus** (this module) — **CN IV somatic
    motor**.

*   **Left Edinger-Westphal nucleus**
    (``.../cranial_nerve_nuclei/left/edinger_westphal_nucleus/``
    **and** ``.../tegmentum/left/edinger_westphal_nucleus/``) —
    **CN III preganglionic parasympathetic**.

**They are DIFFERENT NUCLEI for DIFFERENT CRANIAL NERVES.**
Consumers must **not** conflate the two, and must **not** attribute
**pupil** or **lens** function to the trochlear.

The Left Trochlear Nucleus / Left Mesencephalic Trigeminal Nucleus Boundary
---------------------------------------------------------------------------
This is the **somatic motor / sensory** boundary:

*   **Left trochlear nucleus** (this module) — **CN IV somatic
    motor**.

*   **Left mesencephalic trigeminal nucleus (mesV)**
    (``.../cranial_nerve_nuclei/left/mesencephalic_trigeminal_nucleus/``
    **and** ``.../tegmentum/left/mesencephalic_trigeminal_nucleus/``)
    — **CN V primary sensory (proprioceptive)**.

**They are DIFFERENT NUCLEI in DIFFERENT functional systems.**
Consumers must **not** conflate the two.

The Left Trochlear Nucleus / MLF Boundary
-----------------------------------------
This is the **nucleus / conduction pathway** boundary:

*   **Left trochlear nucleus** (this module) — the **CN IV somatic
    motor nucleus**.

*   **Left MLF** — the **medial longitudinal fasciculus** — a
    **longitudinal fiber tract** — **conduction pathway** — wired
    elsewhere (as a brainstem tract).

**A left MLF lesion produces LEFT INTERNUCLEAR OPHTHALMOPLEGIA
(INO)** — **adduction weakness of the left eye with abducting
nystagmus of the right eye** — **NOT a left CN IV nuclear palsy**
and **NOT a left CN IV palsy at all**. **The superior oblique is not
the medial rectus** — the **INO** and the **CN IV palsy** are
**mechanistically different**: INO is a **conduction pathway**
deficit; CN IV palsy is a **nuclear / fascicular / nerve** deficit.
Consumers must **not** conflate the two.

The Left Trochlear Nucleus / Left Superior Oblique Boundary
-----------------------------------------------------------
This is the **nucleus / target muscle** boundary — and the **side
inversion**:

*   **Left trochlear nucleus** (this module) — the **left** CN IV
    somatic motor nucleus.

*   **Right superior oblique** — the **target muscle** — the
    **CONTRALATERAL** superior oblique.

**The left trochlear nucleus innervates the RIGHT superior
oblique** — the direct consequence of the **pre-exit decussation**.
**They are DIFFERENT STRUCTURES across the CNS-muscle boundary** —
and the **side inversion is the defining fact**. Consumers must
**not** assume the **left** nucleus innervates the **left** muscle
— it innervates the **right** muscle.

The Left Trochlear Nucleus / Left Trochlear Nerve Boundary
----------------------------------------------------------
This is the **nucleus / peripheral nerve** boundary — and the
**trauma vulnerability**:

*   **Left trochlear nucleus** (this module) — the **nucleus** —
    grey matter in the midbrain.

*   **Left trochlear nerve** — the **peripheral axon bundle** —
    PNS.

**The left trochlear nerve's axons** — after **decussating in the
superior medullary velum** — travel through the **left trochlear
nerve** (the **right** nucleus's decussated axons form the
**left** nerve, and vice versa) — but the **nerve** is **not the
nucleus**. **The nerve has the longest intracranial course of any
CN**, and it is the **most vulnerable cranial nerve to head
trauma**. **In head trauma, the lesion is almost always in the
NERVE, not the nucleus.** Consumers must **not** conflate the
trochlear nucleus with the trochlear nerve, and must **not**
attribute **traumatic CN IV palsy** to a **nuclear** lesion.

The Left Trochlear Nucleus / Left Superior Colliculus and Left Inferior Colliculus Boundary
------------------------------------------------------------------------------------------
This is the **CN nucleus / tectum** boundary:

*   **Left trochlear nucleus** (this module) — the **CN IV somatic
    motor nucleus**.

*   **Left superior colliculus** and **left inferior colliculus**
    (``.../tectum/left/superior_colliculus/`` and
    ``.../tectum/left/inferior_colliculus/``) — **tectum**
    structures — the **superior colliculus** drives **saccades**
    and **visual orienting**; the **inferior colliculus** is the
    **auditory relay**.

**The trochlear nucleus is at the level of the INFERIOR
COLLICULUS.** The colliculi **DRIVE** the CN nuclei for saccades
(via the tectobulbar tract), but they are **not CN nuclei**.
**They are DIFFERENT STRUCTURES in DIFFERENT midbrain
compartments** — the **colliculi** are **tectum**; the **trochlear
nucleus** is **tegmentum**. Consumers must **not** conflate the
two.

The Left Trochlear Nucleus / PPRF, riMLF, and Interstitial Nucleus of Cajal Boundary
-----------------------------------------------------------------------------------
This is the **CN IV nucleus / gaze center** boundary:

*   **Left trochlear nucleus** (this module) — the **CN IV somatic
    motor nucleus**.

*   **PPRF** (``.../hindbrain/metencephalon/pons/pprf/``), **riMLF**,
    and **interstitial nucleus of Cajal**
    (``.../tegmentum/left/``) — **premotor saccade generators** —
    **gaze centers**, not CN nuclei.

**They are DIFFERENT STRUCTURES in DIFFERENT functional systems** —
the **gaze centers** are **premotor**; the **trochlear nucleus** is
a **CN motor nucleus**. Consumers must **not** conflate the
trochlear nucleus with the gaze centers.

The Left Trochlear Nucleus / Right Trochlear Nucleus Boundary
-------------------------------------------------------------
This is the **side** boundary — and the **decussation is the
asymmetry**:

*   **Left trochlear nucleus** (this module) — the **left** CN IV
    somatic motor nucleus.

*   **Right trochlear nucleus**
    (``.../cranial_nerve_nuclei/right/trochlear_nucleus/`` **and**
    ``.../tegmentum/right/trochlear_nucleus/``) — the **right** CN
    IV somatic motor nucleus.

**They are BILATERALLY SYMMETRIC in their cell-body locations** —
each is a **paired CN IV somatic motor nucleus** on its side.
**But their TARGET MUSCLES are CONTRALATERAL**:
*   **Left trochlear nucleus** — innervates the **RIGHT** superior
    oblique.
*   **Right trochlear nucleus** — innervates the **LEFT** superior
    oblique.
**A consumer that assumes "left trochlear nucleus = left superior
oblique" will be WRONG** — the **left nucleus innervates the right
muscle**, and the **right nucleus innervates the left muscle**.
**This is the defining asymmetric fact of the pair** — and it is
**the same fact on both sides**, just with the muscle flipped. The
two nuclei are **strict mirrors in their locations** but
**innervate opposite muscles**. Consumers must **not** conflate
the left trochlear nucleus with the right, and must **not** assume
their target muscles are mirror images — **they are contralateral
each**.

Function in the Human Brain
---------------------------
The left trochlear nucleus's function is **somatic motor control of
the RIGHT superior oblique** — **NOT** control of any other
extraocular muscle, **NOT** the left superior oblique, **NOT**
pupil or lens, **NOT** gaze generation:

*   **Superior Oblique (CONTRALATERAL — RIGHT):** The left trochlear
    nucleus innervates the **RIGHT superior oblique** — the
    **only target** of the left CN IV. The superior oblique's
    actions (from the primary position of the eye) are:
    *   **Depression** (especially in **adduction** — when the eye
        is turned inward).
    *   **Intorsion** (internal rotation of the eye around its
        visual axis — the top of the eye rotates toward the nose).
    *   **Abduction** (slight outward movement of the eye).
    The **right superior oblique** is tested clinically by asking
    the patient to **look down and to the LEFT** (the **right eye's
    adduction** position) — a **right superior oblique palsy**
    produces **impaired depression of the right eye in left gaze**
    (worse than in other directions).

*   **NOT the left superior oblique.** The **left superior oblique**
    is innervated by the **RIGHT trochlear nucleus** (the
    **contralateral** one). A consumer who says "left trochlear
    nucleus → left superior oblique" is **wrong** — the side
    inversion is the defining fact.

*   **NOT a gaze center.** The left trochlear nucleus is a **motor
    nucleus** — it **fires in response to upstream drive** (from
    the PPRF for horizontal conjugate gaze, the riMLF for vertical
    conjugate gaze, the vestibular nuclei for the vestibulo-ocular
    reflex, the superior colliculus for saccades). It does **not**
    generate a saccade plan. Its **coordination with the right
    trochlear nucleus and the other extraocular motor nuclei** is
    via **descending pathways** (MLF, posterior commissure) — **not**
    intrinsic nucleus-to-nucleus coupling.

*   **NOT an oscillator.** The left trochlear nucleus is a **motor
    nucleus** — it does **not** generate a rhythm. **Motor nuclei
    carry NO coupling warning** — same rule as CN III, EW, premotor
    pools, sensor nuclei, and conduction pathways.

**The unifying theme:** the left trochlear nucleus is the **left
CN IV somatic motor nucleus** — the **somatic motor component of
CN IV**. It is **somatic motor** (**pure** — no parasympathetic,
no sensory, no branchiomotor component), **NOT a gaze center**
(the PPRF, riMLF, interstitial nucleus of Cajal), and **NOT an
oscillator** (a motor nucleus — **NO coupling warning**). It has
**two defining facts**: **pre-exit decussation** (left nucleus →
**RIGHT** superior oblique) and **dorsal exit** (the trochlear is
the **only CN that exits dorsally**, with the **longest
intracranial course** and the **highest trauma vulnerability**).

Associated Disorders
--------------------
The left trochlear nucleus has **no named syndrome of its own** —
and unlike CN III (which has Weber, Benedikt, Claude, Nothnagel,
and PCom-aneurysm signatures), **CN IV palsy has no eponymous
nuclear syndrome**. Its clinical associations are **direct** but
usually **not nuclear-localizing** — the vast majority of CN IV
palsies are **nerve** lesions (trauma, microvascular,
decompensated congenital), not **nuclear** lesions:

*   **Congenital Trochlear Nerve Palsy (MOST COMMON — NERVE, NOT
    nuclear):** **Congenital CN IV palsy** is the **most common
    cause of CN IV palsy overall**, and the **most common
    congenital cranial dysinnervation disorder**. It is caused by
    **agenesis or dysgenesis of the trochlear nerve** (not the
    nucleus in most cases — some forms are nuclear, but the
    characteristic finding is **nerve absence** on MRI). It
    typically **decompensates in adulthood** — patients who have
    compensated with a head tilt since childhood may develop
    **diplopia** and a **new-onset head tilt** when the
    compensation fails. **The classic finding** is a **large
    vertical deviation** (often **15–20 prism diopters**) with a
    **positive Bielschowsky head-tilt test** — **worse on
    ipsilateral head tilt** (e.g., a **right** superior oblique
    palsy worsens the hypertropia on **right** head tilt). **NOT a
    nuclear lesion** in most cases — the nerve is missing.

*   **Traumatic Trochlear Nerve Palsy (NERVE, NOT nuclear — the
    MOST VULNERABLE CN):** **Head trauma** is a **leading cause of
    acquired CN IV palsy**, because the **trochlear nerve has the
    longest intracranial course of any CN** and passes along the
    **free edge of the tentorium cerebelli** — vulnerable to
    **tentorial herniation**, **shear injury**, and **direct
    compression**. **The lesion is almost always in the NERVE,
    not the nucleus.** **Bilateral CN IV palsy** can occur with
    **severe head trauma** or **dorsal midbrain lesions**
    (especially **pineal region tumors**, which can compress **both
    trochlear nerves** at the **superior medullary velum** — the
    decussation site — producing **bilateral CN IV palsy**).

*   **Microvascular Trochlear Nerve Palsy (NERVE, NOT nuclear —
    DIABETES, HYPERTENSION):** **Microvascular ischemia** can
    affect the trochlear nerve — most commonly in **diabetes** and
    **hypertension** — producing an **isolated CN IV palsy** that
    **spontaneously resolves** over weeks to months. **The lesion
    is in the NERVE**, not the nucleus.

*   **Trochlear Nerve Palsy from Mass Lesion or Aneurysm (NERVE,
    NOT nuclear):** **Compression by a mass or aneurysm** — e.g., a
    **posterior cerebral artery** or **superior cerebellar artery**
    aneurysm — can compress the **trochlear nerve** in the
    subarachnoid space. **The lesion is in the NERVE**, not the
    nucleus.

*   **Dorsal Midbrain Syndrome (TECTUM — NOT trochlear nucleus):**
    **Dorsal midbrain lesions** — **pineal region tumors**
    (pinealoma, germinoma), **tectal gliomas**, **hydrocephalus**
    — produce **Parinaud syndrome** — **upgaze palsy,
    convergence-retraction nystagmus, light-near dissociation,
    eyelid retraction (Collier sign)** — **not isolated CN IV
    palsy** (though **bilateral CN IV palsy** can occur from
    compression of the **trochlear decussation** at the **superior
    medullary velum**). **The lesion is in the TECTUM** or the
    **decussation**, not the **trochlear nucleus itself**.

*   **Myasthenia Gravis (NOT a CN IV Nuclear Lesion — NMJ):**
    **Myasthenia gravis** produces **fatigable diplopia** — which
    may **mimic** a CN IV palsy (and can affect the superior
    oblique) — **NOT a CN IV nuclear, or fascicular, or nerve
    lesion**. The lesion is at the **neuromuscular junction** —
    **outside the brainstem**.

*   **Thyroid Eye Disease (NOT a CN IV Nuclear Lesion — ORBIT):**
    **Thyroid eye disease** (Graves' orbitopathy) can produce
    **restrictive strabismus** — which may **mimic** a CN IV palsy
    (especially **inferior rectus restriction** mimicking **superior
    oblique palsy**) — **NOT a CN IV nuclear lesion**. The lesion is
    in the **orbit**, not the brainstem.

*   **Brown Syndrome (NOT a CN IV Nuclear Lesion — TENDON
    RESTRICTION):** **Brown syndrome** — **impaired elevation in
    adduction** — is a **superior oblique tendon restriction** at
    the **trochlea** — **NOT a CN IV palsy**. The lesion is in the
    **orbit**, not the brainstem. It can be **congenital** or
    **acquired** (inflammatory, traumatic, surgical).

*   **Isolated Nuclear CN IV Lesion (RARE — NO NAMED SYNDROME):** A
    **focal lesion** of the **left trochlear nucleus** — from
    **small infarction**, **demyelination** (e.g., **multiple
    sclerosis**), or **tumor** — would produce a **RIGHT superior
    oblique palsy** (the **contralateral** muscle, because of the
    **pre-exit decussation**). **This is rare in practice** — most
    CN IV palsies are **nerve** lesions (congenital, traumatic,
    microvascular, compressive), not **nuclear** lesions. **No
    named nuclear CN IV syndrome exists.**

*   **MS Plaques (INDIRECT — the trochlear nucleus and the MLF can
    both be involved):** **Multiple sclerosis** plaques can occur
    **anywhere in the CNS**, including the **trochlear nucleus** or
    the **MLF** — producing **CN IV palsy**, **INO**, or both, as
    part of a **broader MS presentation**. This is **indirect**.

*   **No Named "Trochlear Nucleus Syndrome":** The left trochlear
    nucleus is a **somatic motor nucleus** — its **isolated lesion**
    produces a **contralateral superior oblique palsy**, which is
    **rare** in practice. Most clinical CN IV palsies are **nerve**
    lesions (congenital, traumatic, microvascular, compressive). The
    **clinical relevance** of the nucleus is **direct** — via the
    **contralateral superior oblique palsy** — but **most CN IV
    palsies are NOT nuclear**, and the **therapeutic and diagnostic
    approach** is usually **directed at the nerve or at
    non-compressive causes**.

**What is NOT here:** The left trochlear nucleus is **not** the
substrate for **Weber syndrome** (crus cerebri — CN III fascicular
— **NOT** CN IV), **Benedikt syndrome** (tegmentum — CN III +
red nucleus — **NOT** CN IV), **Claude syndrome** (tegmentum —
CN III + red nucleus — **NOT** CN IV), **Nothnagel syndrome**
(tectum — CN III + cerebellar signs — **NOT** CN IV),
**Parinaud syndrome** (dorsal midbrain — tectum — **NOT** the
trochlear nucleus; bilateral CN IV palsy can occur from
compression of the decussation, not the nucleus), **PCom aneurysm**
(CN III — **NOT** CN IV), **myasthenia gravis** (NMJ — **NOT**
CN IV), **thyroid eye disease** (orbit — **NOT** CN IV),
**Brown syndrome** (superior oblique tendon — **NOT** CN IV),
**INO** (MLF — **NOT** CN IV), **horizontal gaze palsy** (PPRF —
**NOT** CN IV), **vertical gaze palsy** (riMLF — **NOT** CN IV),
**pupillary light reflex deficits** (EW — **NOT** CN IV),
**Argyll Robertson pupil** (upstream / downstream — **NOT** CN IV),
**Adie's tonic pupil** (ciliary ganglion — **NOT** CN IV),
**CCHS** (RTN), **OIRD** (pre-Bötzinger complex — NK1R neurons),
**Rett syndrome** (pre-Bötzinger complex), **SIDS** (proposed —
pre-Bötzinger complex + arcuate nucleus), **essential hypertension /
sympathetic overactivity** (C1 group / RVLM), **Parkinson's
disease** (substantia nigra — tegmentum), **Huntington's disease**
(striatum — telencephalon), or **Kluver-Bucy syndrome** (amygdala).
Its clinical relevance is **direct** — via the **contralateral
superior oblique palsy** — but **most CN IV palsies are NOT
nuclear**, and the **therapeutic and diagnostic approach** is
usually **directed at the nerve or at non-compressive causes**.
**No named nuclear CN IV syndrome exists.**

Lateralization Notes
--------------------
This is the **left** trochlear nucleus leaf. The left and right
trochlear nuclei are **bilaterally symmetric in their cell-body
locations** — but their **target muscles are CONTRALATERAL**:

*   **Bilateral Paired Motor Nuclei:** Each side has its own
    trochlear nucleus — each is a **paired CN IV somatic motor
    nucleus** with a **single target muscle on the contralateral
    side**.

*   **THE DEFINING ASYMMETRIC FACT (the key to the leaf):**
    *   **Left trochlear nucleus** — **left** nucleus — innervates
        the **RIGHT** superior oblique.
    *   **Right trochlear nucleus** — **right** nucleus —
        innervates the **LEFT** superior oblique.
    **The pre-exit decussation in the superior medullary velum is
    what flips the target.** A consumer that assumes "left nucleus
    → left muscle" is **WRONG** — the **left nucleus innervates the
    right muscle**, and the **right nucleus innervates the left
    muscle**. **This is the defining asymmetric fact of the pair** —
    and it is **the same fact on both sides**, just with the muscle
    flipped.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to MOTOR NUCLEI):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **left trochlear nucleus** is a **motor
    nucleus** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. Its **left**
    and **right** sides are **independent nuclei** — there is
    **no** trochlear-trochlear coupling. **Coordination with the
    right trochlear nucleus and the other extraocular motor nuclei**
    is via **descending pathways** — the **MLF** (for conjugate
    gaze), the **posterior commissure** (for vertical conjugate
    gaze), the **PPRF** (for horizontal saccades), the **riMLF**
    (for vertical saccades) — **not** intrinsic nucleus-to-nucleus
    coupling. **Motor nuclei carry NO coupling warning** — same
    rule as CN III, EW, premotor pools, sensor nuclei, and
    conduction pathways.

*   **Clinical Laterality — the classic Bielschowsky head-tilt test:**
    *   A **left nuclear CN IV lesion** → **RIGHT superior oblique
        palsy** — **right hypertropia** (right eye higher than
        left), **worse on LEFT head tilt** (the **Bielschowsky
        head-tilt test** — **worse on contralateral head tilt** for
        a **nuclear** CN IV lesion, because the **right superior
        oblique** normally **depresses the right eye in right head
        tilt**; if the **right superior oblique** is weak, the
        **right eye does not depress** on **right** head tilt, and
        the **right hypertropia worsens on RIGHT head tilt** —
        **wait** — I need to state this carefully: **the
        Bielschowsky head-tilt test is positive (hypertropia
        worsens) on the side of the PAREtic superior oblique** —
        i.e., a **right superior oblique palsy worsens the
        right hypertropia on RIGHT head tilt**. **A left nuclear
        CN IV lesion produces a RIGHT superior oblique palsy, so
        the right hypertropia worsens on RIGHT head tilt.** **The
        lesion is on the LEFT (nucleus), the paretic muscle is on
        the RIGHT (superior oblique), and the Bielschowsky is
        positive on the RIGHT (head tilt toward the paretic
        muscle).** This is the **classic inversion that catches
        consumers** — the **side of the lesion (LEFT nucleus)** and
        the **side of the clinical sign (RIGHT head tilt)** are
        **opposite**.
    *   A **left nerve CN IV lesion** → **LEFT superior oblique
        palsy** — **left hypertropia**, **worse on LEFT head tilt**.
        **The lesion is on the LEFT (nerve), the paretic muscle is
        on the LEFT (superior oblique), and the Bielschowsky is
        positive on the LEFT (head tilt toward the paretic
        muscle).** **The side of the lesion (LEFT nerve)** and the
        **side of the clinical sign (LEFT head tilt)** are the
        **same** — this is the **usual, non-inverting pattern** for
        CN IV nerve palsy.
    *   **The contrast between nuclear and nerve CN IV palsy is
        the diagnostic signature of the leaf** — a **left nuclear
        CN IV lesion** produces a **right** superior oblique palsy
        (inversion); a **left nerve CN IV lesion** produces a
        **left** superior oblique palsy (no inversion). **The
        decussation is the mechanism** — and the leaf is the place
        to encode it.
    *   **A consumer that assumes "left CN IV lesion = left superior
        oblique palsy" will be WRONG for NUCLEAR lesions** — the
        **left** nucleus innervates the **right** superior oblique,
        so a **left nuclear** lesion is a **right** superior
        oblique palsy. The **left nerve** lesion is a **left**
        superior oblique palsy (usual pattern). **This distinction
        is the leaf's key consumer-facing hazard.**

**The left trochlear nucleus is a strict mirror of the right
trochlear nucleus in its cell-body location** — **no coupling
warning, no SLEA warning, no amygdala-lateralization warning, and
no rhinencephalon-exclusion flag** — **but with a crucial caveat**:
the **pre-exit decussation inverts the target muscle**, so the
**left** nucleus innervates the **right** superior oblique and the
**right** nucleus innervates the **left** superior oblique. The
"strict mirror" is **structural in location** but **contralateral
in target** — the two nuclei are **exact mirrors with the muscle
flipped**. See *Design Contract*.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only — **no** import
    from ``.../right/trochlear_nucleus/``.
*   **No cross-lobe imports.** This module does **not** import from
    the **superior oblique**, the **trochlear nerve**, the **MLF**,
    the **PPRF**, the **riMLF**, the **interstitial nucleus of
    Cajal**, the **superior colliculus**, the **inferior
    colliculus**, or any other container. The left trochlear
    nucleus's relationships to the right superior oblique, the left
    trochlear nerve, the right trochlear nucleus, the MLF, the
    PPRF, the riMLF, the interstitial nucleus of Cajal, the superior
    and inferior colliculi, the other extraocular motor nuclei, and
    the neuromuscular junction are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **nicotinic
    ACh phenotype** at the **neuromuscular junction** is a
    ``chemicals_hormones``-layer fact — documented as **prose**,
    **never imported**.
*   **DUAL-PARENT LEAF — CROSS-LISTED between
    ``cranial_nerve_nuclei/left/`` and ``tegmentum/left/``.** Both
    paths resolve to **this module**.
*   **CROSS-LISTING via ``AREA_PATHS``.** The leaf is cross-listed
    between the functional container (``cranial_nerve_nuclei/``) and
    the topographic container (``tegmentum/``). Consumers resolving
    by **either** path get **this module**.
*   **CONSISTENT with the ``cranial_nerve_nuclei/``,
    ``cranial_nerve_nuclei/left/``, and ``midbrain`` container child
    lists.** The CN nuclei are placed under ``tegmentum/``
    (topographic home) **and** cross-listed under
    ``cranial_nerve_nuclei/`` (functional grouping). This leaf is
    the **left-side trochlear** slice of that cross-listing.
*   **SOMATIC MOTOR NUCLEUS — pure somatic motor.** **No
    parasympathetic component** (unlike CN III, which has the EW
    nucleus as its preganglionic parasympathetic sibling), **no
    sensory component** (unlike CN V), **no branchiomotor component**
    (unlike CN V, VII, IX, X, XI). **CN IV is the only CN that
    innervates a single muscle.**
*   **THE DEFINING FACT — DECUSSATION BEFORE EXIT.** The **left
    trochlear nucleus innervates the RIGHT superior oblique** — the
    **only CN with a pre-exit decussation**. The **left nucleus
    → right muscle** and the **right nucleus → left muscle**.
    **A consumer that reasons "left nucleus → left muscle" is
    WRONG** — the **side inversion is the defining fact**.
*   **THE SECOND DEFINING FACT — DORSAL EXIT.** The **trochlear
    nerve exits the brainstem DORSALLY** — the **only CN to do so**.
    It has the **longest intracranial course of any CN** and is the
    **most vulnerable cranial nerve to head trauma**.
*   **NOT the oculomotor nucleus — that is CN III.** The trochlear
    is CN IV, at the **inferior colliculus level** (caudal to the
    oculomotor).
*   **NOT the Edinger-Westphal nucleus — that is CN IIIp.** The
    trochlear has **no parasympathetic component**.
*   **NOT the mesV — that is CN V sensory.**
*   **NOT the MLF — that is a CONDUCTION PATHWAY.** A **left MLF
    lesion** produces **left INO** — **NOT a left CN IV palsy**.
*   **NOT the superior oblique — that is the TARGET MUSCLE**, and
    the **left nucleus innervates the RIGHT superior oblique** (the
    **contralateral** one).
*   **NOT the trochlear nerve — the NERVE is peripheral**, with the
    **longest intracranial course of any CN**, and is the
    **most vulnerable cranial nerve to head trauma**. **In head
    trauma, the lesion is almost always in the NERVE, not the
    nucleus.**
*   **NOT the colliculi — those are TECTUM structures** that
    **drive** the CN nuclei for saccades.
*   **NOT the PPRF, riMLF, or interstitial nucleus of Cajal — those
    are GAZE CENTERS.** They are **premotor saccade generators**,
    not CN nuclei.
*   **NO coupling warning — motor nuclei carry NO coupling warning.**
    Same rule as CN III, EW, premotor pools, sensor nuclei, and
    conduction pathways. Coordination with the right trochlear
    nucleus is via **descending pathways** (MLF, posterior
    commissure, PPRF, riMLF) — **not** intrinsic nucleus-to-nucleus
    coupling.
*   **CHEMICALS-LAYER DISCIPLINE.** The **nicotinic ACh phenotype**
    at the neuromuscular junction is a ``chemicals_hormones``-layer
    fact — documented as **prose**, **never imported**.
*   **CN NUCLEUS — NOT a CN nerve, NOT a conduction pathway, NOT a
    gaze center, NOT a colliculus, NOT a target muscle.**
*   **SIDE-CONSISTENT — this leaf is the LEFT trochlear nucleus.**
*   **MIRROR PARITY with ``.../right/trochlear_nucleus/`` — paired
    and symmetric in cell-body location, with NO coupling warning**
    — **but with the DECUSSATION as the DEFINING ASYMMETRY**: the
    **left nucleus innervates the RIGHT superior oblique**, and the
    **right nucleus innervates the LEFT superior oblique**. The
    "strict mirror" is **structural in location** but
    **contralateral in target** — the two nuclei are **exact
    mirrors with the muscle flipped**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum/left`` ↔
    ``cranial_nerve_nuclei/left``) — not into the forebrain,
    hindbrain, or periphery. The **MLF**, **PPRF**, **riMLF**,
    **interstitial nucleus of Cajal**, **colliculi**, **trochlear
    nerve**, and **superior oblique** are **separate structures**
    referenced as **prose**, not as cross-listed parents.
*   **No nested cross-listing.** This is a **single dual-parent
    leaf**. It is **not** a container.
*   **The on-disk tree is authoritative.**

Usage
-----
Resolve the leaf by **either** path (they are equivalent — **this is
a dual-parent anchor**)::

    # Functional path (clinician framing):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left import trochlear_nucleus

    # Topographic path (anatomist framing):
    from infrastructure.brainparts.midbrain.tegmentum.left import trochlear_nucleus

Or by fully-qualified path string::

    functional_path = (
        "midbrain.cranial_nerve_nuclei.left.trochlear_nucleus"
    )
    topographic_path = (
        "midbrain.tegmentum.left.trochlear_nucleus"
    )
    # Both resolve to THIS module.

**Do not** assume the two paths lead to **different structures** —
they lead to **one leaf**, **dual-parented**.

**Do not** assume the left trochlear nucleus **innervates the left
superior oblique**. The **trochlear is the ONLY CN whose fibers
DECUSSATE BEFORE EXITING** — the **left trochlear nucleus
innervates the RIGHT superior oblique**, and the **right trochlear
nucleus innervates the LEFT superior oblique**. **A LEFT nuclear
CN IV lesion produces a RIGHT superior oblique palsy.** This is the
**defining fact** of the leaf.

**Do not** assume the left trochlear nucleus is the **left
oculomotor nucleus** (CN III) or the **left Edinger-Westphal
nucleus** (CN IIIp). The **trochlear** is **CN IV** — a **different
cranial nerve** — at the **inferior colliculus level** (caudal to
the oculomotor, which is at the superior colliculus level). The
trochlear has **no parasympathetic component**.

**Do not** assume the left trochlear nucleus is the **left mesV**
(CN V sensory). The **trochlear** is **somatic motor**; the
**mesV** is **primary sensory**. Different nuclei for different
cranial nerves.

**Do not** conflate the left trochlear nucleus with the **left
MLF**. The **MLF** is a **conduction pathway**. A **left MLF
lesion** produces **left internuclear ophthalmoplegia (INO)** —
**NOT a left CN IV palsy**. **The superior oblique is not the
medial rectus** — the INO and the CN IV palsy are
**mechanistically different**.

**Do not** conflate the left trochlear nucleus with the **left
superior oblique**. The **superior oblique** is the **target
muscle** — the **left nucleus innervates the RIGHT superior
oblique** (the **contralateral** muscle). **The left superior
oblique** is innervated by the **right trochlear nucleus**.

**Do not** conflate the left trochlear nucleus with the **left
trochlear nerve**. The **nerve** is peripheral — it has the
**longest intracranial course of any CN** and is the **most
vulnerable cranial nerve to head trauma**. **In head trauma, the
lesion is almost always in the NERVE, not the nucleus.** The
**left nuclear** CN IV palsy is a **rare** pattern; the **left
nerve** CN IV palsy is **common**.

**Do not** conflate the left trochlear nucleus with the **superior
or inferior colliculus** — those are **tectum** structures that
**drive** the CN nuclei for saccades. The trochlear is at the
**inferior colliculus level**, but the **colliculus is not the
trochlear nucleus**.

**Do not** conflate the left trochlear nucleus with the **PPRF**,
the **riMLF**, or the **interstitial nucleus of Cajal**. Those are
**gaze centers** — **premotor saccade generators** — not CN nuclei.

**Do not** conflate the left trochlear nucleus with the
**congenital**, **traumatic**, **microvascular**, or **compressive**
CN IV palsies — those are **NERVE** lesions, not **nuclear**
lesions. The **nuclear** CN IV palsy is **rare**; the **nerve**
CN IV palsy is **common**.

**Do not** conflate the left trochlear nucleus with **myasthenia
gravis** (NMJ), **thyroid eye disease** (orbit), or **Brown
syndrome** (superior oblique tendon restriction) — those are
**outside the brainstem** and are **common CN IV-palsy mimics**.

**Do not** import the **nicotinic ACh phenotype** into the midbrain
structural layer. It is a **``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the left trochlear
nucleus. **Motor nuclei carry NO coupling warning** — same rule as
CN III, EW, premotor pools, sensor nuclei, and conduction pathways.
**Coordination with the right trochlear nucleus is via descending
pathways (MLF, posterior commissure, PPRF, riMLF) — not by
intrinsic nucleus-to-nucleus coupling.**

Iterating the left trochlear nucleus's (empty) children (recommended
consumer pattern)::

    TROCHLEAR_NUCLEUS_LEFT_CHILDREN = ()
    # The left trochlear nucleus is a leaf. It has ONE target
    # muscle — the RIGHT superior oblique (CONTRALATERAL, because
    # the trochlear fibers DECUSSATE BEFORE EXITING). There are no
    # structural children — the single motor pool IS the nucleus.

Reaching the **functional parent** (``cranial_nerve_nuclei/left/``)::

    # The functional parent is the left side container of the
    # cranial_nerve_nuclei functional grouping:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left
    #
    # The left trochlear nucleus is a child of BOTH the functional
    # parent and the topographic parent (see below).

Reaching the **topographic parent** (``tegmentum/left/``)::

    # The topographic parent is the left side container of the
    # tegmentum topographic container — the SUPERSET:
    #
    #   brainparts.midbrain.tegmentum.left
    #
    # The left trochlear nucleus is a child of BOTH the topographic
    # parent and the functional parent (see above).

Reaching the left oculomotor nucleus (recommended consumer pattern —
the CN III SOMATIC nucleus, sibling)::

    # The left oculomotor nucleus is the CN III SOMATIC MOTOR
    # nucleus — five extraocular muscles and levator palpebrae
    # superioris — at the SUPERIOR COLLICULUS level:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #
    # The left oculomotor nucleus is CN III, at the SUPERIOR
    # COLLICULUS level. The left trochlear nucleus is CN IV, at the
    # INFERIOR COLLICULUS level — CAUDAL to the oculomotor. They are
    # DIFFERENT NUCLEI for DIFFERENT CRANIAL NERVES.

Reaching the left Edinger-Westphal nucleus (recommended consumer
pattern — the CN IIIp PARASYMPATHETIC nucleus, sibling)::

    # The left Edinger-Westphal nucleus is the CN III PREGANGLIONIC
    # PARASYMPATHETIC nucleus — pupil and lens:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.edinger_westphal_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.edinger_westphal_nucleus
    #
    # The left Edinger-Westphal is CN IIIp; the left trochlear is
    # CN IV somatic motor. The trochlear has NO parasympathetic
    # component.

Reaching the left mesV (recommended consumer pattern — the CN Vm
SENSORY nucleus, sibling)::

    # The left mesencephalic trigeminal nucleus (mesV) is the CN V
    # PRIMARY SENSORY (proprioceptive) nucleus:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.mesencephalic_trigeminal_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.mesencephalic_trigeminal_nucleus
    #
    # The left mesV is PRIMARY SENSORY (CN V); the left trochlear
    # nucleus is SOMATIC MOTOR (CN IV). They are DIFFERENT NUCLEI
    # in DIFFERENT functional systems.

Reaching the MLF (recommended consumer pattern — the CONDUCTION
PATHWAY, NOT a CN nucleus)::

    # The MLF is a CONDUCTION PATHWAY — a longitudinal fiber tract —
    # that coordinates the CN III, CN IV, and CN VI nuclei for
    # conjugate gaze:
    #
    #   brainparts.hindbrain.myelencephalon.medulla_oblongata...
    #   medial_longitudinal_fasciculus
    #
    # A left MLF lesion produces LEFT INTERNUCLEAR OPHTHALMOPLEGIA
    # (INO) — NOT a left CN IV palsy. The medial rectus is the
    # ADDUCTING muscle coordinated by the MLF; the superior oblique
    # is the CN IV target. INO and CN IV palsy are MECHANISTICALLY
    # DIFFERENT.

Reaching the left superior oblique (recommended consumer pattern —
the TARGET MUSCLE, CONTRALATERAL)::

    # The left trochlear nucleus innervates the RIGHT superior
    # oblique — the CONTRALATERAL muscle — because the trochlear
    # fibers DECUSSATE BEFORE EXITING:
    #
    #   peripheral.extraocular_muscles.superior_oblique.right
    #
    # The left nucleus -> right muscle. The right nucleus -> left
    # muscle. THIS IS THE DEFINING ASYMMETRY of the trochlear
    # nucleus. A consumer that reasons "left nucleus -> left muscle"
    # is WRONG.

Reaching the left trochlear nerve (recommended consumer pattern —
the PERIPHERAL bundle, with the LONGEST INTRACRANIAL COURSE)::

    # The left trochlear nerve is the PERIPHERAL axon bundle —
    # formed by the decussated axons of the RIGHT trochlear nucleus
    # (the right nucleus's axons cross in the superior medullary
    # velum and emerge as the LEFT trochlear nerve):
    #
    #   peripheral.cranial_nerves.trochlear.left
    #
    # The trochlear nerve has the LONGEST INTRACRANIAL COURSE of
    # any CN and is the MOST VULNERABLE to head trauma. In head
    # trauma, the lesion is almost always in the NERVE, not the
    # nucleus.

Reaching the left superior colliculus and the left inferior
colliculus (recommended consumer pattern — the TECTUM structures,
NOT the trochlear nucleus)::

    # The left superior colliculus and the left inferior colliculus
    # are TECTUM structures — the superior colliculus is the
    # visual/oculomotor orienting structure; the inferior colliculus
    # is the auditory relay:
    #
    #   brainparts.midbrain.tectum.left.superior_colliculus
    #   brainparts.midbrain.tectum.left.inferior_colliculus
    #
    # The left trochlear nucleus is at the level of the INFERIOR
    # COLLICULUS, but the colliculus is NOT the trochlear nucleus.

Reaching the left PPRF, riMLF, and interstitial nucleus of Cajal
(recommended consumer pattern — the GAZE CENTERS, NOT CN nuclei)::

    # The PPRF, riMLF, and interstitial nucleus of Cajal are GAZE
    # CENTERS — premotor saccade generators — NOT CN nuclei:
    #
    #   brainparts.hindbrain.metencephalon.pons.pprf
    #   brainparts.midbrain.tegmentum.left.riMLF
    #   brainparts.midbrain.tegmentum.left.interstitial_nucleus_of_cajal
    #
    # They are tegmentum (or pontine) leaves but are NOT
    # cross-listed under cranial_nerve_nuclei.

Reaching the right trochlear nucleus (recommended consumer pattern —
the SIDE mirror, with the DECUSSATION as the asymmetry)::

    # The right trochlear nucleus is the RIGHT CN IV somatic motor
    # nucleus:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right.trochlear_nucleus
    #   OR: brainparts.midbrain.tegmentum.right.trochlear_nucleus
    #
    # The two trochlear nuclei are PAIRED and SYMMETRIC in their
    # cell-body locations. BUT their TARGET MUSCLES are
    # CONTRALATERAL:
    #   - LEFT trochlear nucleus -> RIGHT superior oblique
    #   - RIGHT trochlear nucleus -> LEFT superior oblique
    #
    # The DECUSSATION is the DEFINING ASYMMETRY of the pair — the
    # left nucleus innervates the right muscle, and the right
    # nucleus innervates the left muscle. This is the same fact on
    # both sides, just with the muscle flipped.

Reaching myasthenia gravis, thyroid eye disease, and Brown syndrome
(recommended consumer pattern — the NON-BRAINSTEM mimics of CN IV
palsy)::

    # Myasthenia gravis (NMJ), thyroid eye disease (orbit), and
    # Brown syndrome (superior oblique tendon restriction) are
    # NON-BRAINSTEM mimics of CN IV palsy:
    #
    #   peripheral.neuromuscular_junction.myasthenia_gravis
    #   peripheral.orbit.thyroid_eye_disease
    #   peripheral.orbit.brown_syndrome
    #
    # They are NOT CN IV nuclear (or fascicular, or nerve) lesions.
    # They are COMMON CN IV-palsy mimics and must be excluded
    # clinically.

Bilateral iteration (recommended consumer pattern — NOTE the
no-coupling-warning rule and the DECUSSATION ASYMMETRY)::

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
            # NOTE: for the TROCHLEAR nucleus specifically, the
            # TARGET MUSCLES are CONTRALATERAL — the left nucleus
            # innervates the RIGHT superior oblique, and the right
            # nucleus innervates the LEFT superior oblique. The
            # decussation is the DEFINING ASYMMETRY of the pair.

Clinical-pattern detail (not wired — consult references)::

    # The left trochlear nucleus is the LEFT CN IV SOMATIC MOTOR
    # nucleus. It innervates the RIGHT superior oblique
    # (CONTRALATERAL). The CLINICAL PATTERNS of the related lesions
    # are DISTINCT:
    #
    #   LEFT NUCLEAR CN IV lesion  -> RIGHT superior oblique palsy:
    #                                   right hypertropia, worse
    #                                   on RIGHT head tilt
    #                                   (Bielschowsky positive on
    #                                   the RIGHT — the PARETIC
    #                                   muscle side); excyclotorsion
    #                                   of the right eye; RARE in
    #                                   practice
    #   LEFT NERVE CN IV lesion    -> LEFT superior oblique palsy:
    #     (congenital, traumatic,         left hypertropia, worse
    #      microvascular, compressive)    on LEFT head tilt
    #                                   (Bielschowsky positive on
    #                                   the LEFT — the PARETIC
    #                                   muscle side); excyclotorsion
    #                                   of the left eye; COMMON in
    #                                   practice
    #   Parinaud syndrome          -> dorsal midbrain — upgaze
    #                                   palsy, convergence-
    #                                   retraction nystagmus,
    #                                   light-near dissociation,
    #                                   Collier sign — NOT an
    #                                   isolated CN IV palsy
    #   Bilateral CN IV palsy      -> dorsal midbrain lesion
    #                                   (e.g., pineal region tumor)
    #                                   compressing BOTH trochlear
    #                                   nerves at the superior
    #                                   medullary velum
    #                                   (DECUSSATION SITE) —
    #                                   bilateral superior oblique
    #                                   palsy
    #   myasthenia gravis          -> fatigable diplopia — MIMICS
    #                                   CN IV palsy — NOT a brainstem
    #                                   lesion
    #   thyroid eye disease        -> restrictive strabismus —
    #                                   MIMICS CN IV palsy — NOT a
    #                                   brainstem lesion
    #   Brown syndrome             -> superior oblique tendon
    #                                   restriction — MIMICS CN IV
    #                                   palsy — NOT a brainstem
    #                                   lesion
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # STRUCTURES.

The Bielschowsky head-tilt test — detail (not wired — consult
references)::

    # The Bielschowsky head-tilt test identifies the paretic
    # superior oblique. When the head tilts to one side, the
    # ipsilateral superior oblique and the contralateral inferior
    # rectus are the two muscles that must contract to keep the
    # eyes level. If the ipsilateral superior oblique is weak, the
    # ipsilateral eye rises (hypertropia) on that head tilt.
    #
    # The Bielschowsky test is POSITIVE (hypertropia worsens) on
    # the side of the PARETIC superior oblique:
    #
    #   - RIGHT superior oblique palsy -> right hypertropia, worse
    #     on RIGHT head tilt (Bielschowsky positive on the RIGHT)
    #   - LEFT superior oblique palsy -> left hypertropia, worse on
    #     LEFT head tilt (Bielschowsky positive on the LEFT)
    #
    # For a LEFT NUCLEAR CN IV lesion: the paretic muscle is the
    # RIGHT superior oblique (contralateral, because of the
    # decussation), so the RIGHT hypertropia worsens on RIGHT head
    # tilt (Bielschowsky positive on the RIGHT).
    #
    # For a LEFT NERVE CN IV lesion: the paretic muscle is the LEFT
    # superior oblique (ipsilateral, because the nerve is already
    # decussated), so the LEFT hypertropia worsens on LEFT head
    # tilt (Bielschowsky positive on the LEFT).
    #
    # THE INVERSION: a LEFT NUCLEAR lesion gives a RIGHT
    # Bielschowsky; a LEFT NERVE lesion gives a LEFT Bielschowsky.
    # This is the diagnostic signature of the decussation — and the
    # classic inversion that catches consumers.

References
----------
*   **Canonical trochlear nucleus anatomy:** Büttner-Ennever, J.A.
    (2006). *Neuroanatomy of the Oculomotor System*. (The trochlear
    nucleus — its location at the inferior colliculus level, its
    single motor pool, the pre-exit decussation in the superior
    medullary velum, the dorsal exit of the trochlear nerve.)
*   **Trochlear decussation:** Porter, J.D., Guthrie, B.L., Sparks,
    D.L. (1983). "Innervation of monkey extraocular muscles:
    localization of sensory and motor neurons by retrograde
    transport of horseradish peroxidase." *Journal of Comparative
    Neurology* 218:208–219. (The trochlear nucleus's single motor
    pool and its contralateral projection — the anatomical basis of
    the pre-exit decussation.)
*   **Trochlear nerve — dorsal exit and course:** Brazis, P.W.,
    Masdeu, J.C., Biller, J. (2007). *Localization in Clinical
    Neurology*, 5th ed. (The trochlear nerve's dorsal exit, its
    long intracranial course around the cerebral peduncle, its
    vulnerability to head trauma.)
*   **Congenital CN IV palsy:** Brodsky, M.C. (2004). "Pediatric
    neuro-ophthalmology." In *Pediatric Ophthalmology and
    Strabismus* (Hoyt & Taylor, eds.). (Congenital CN IV palsy —
    the most common cause of CN IV palsy, often from nerve
    agenesis, decompensating in adulthood.)
*   **Bielschowsky head-tilt test:** Bielschowsky, A. (1935).
    "Lectures on motor anomalies of the eyes: II. Paralysis of
    individual ocular muscles." *Archives of Ophthalmology*
    13:33–59. (The classic description of the head-tilt test for
    superior oblique palsy.)
*   **Trochlear nucleus vs. nerve — the decussation inversion:**
    Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye
    Movements*, 6th ed. (The clinical distinction between nuclear
    and nerve CN IV palsy — the decussation inversion, the
    Bielschowsky test, and the localizing value of the findings.)
*   **Traumatic CN IV palsy:** Rush, J.A., Younge, B.R. (1981).
    " Paralysis of cranial nerves III, IV, and VI: cause and
    prognosis in 1,000 cases." *Archives of Ophthalmology*
    99:76–79. (Traumatic CN IV palsy — the trochlear is the most
    vulnerable CN to head trauma, because of its long intracranial
    course and tentorial course.)
*   **Microvascular CN IV palsy:** Jacobson, D.M., Trobe, J.D.
    (1999). "The emerging role of magnetic resonance angiography
    in the management of patients with third cranial nerve palsy."
    *Journal of Neuro-Ophthalmology* 19:147–151. (Microvascular
    trochlear neuropathy — diabetes, hypertension — with
    spontaneous resolution.)
*   **Parinaud syndrome (contrast — dorsal midbrain, NOT trochlear
    nucleus):** Parinaud, H. (1883). "Paralysie des mouvements
    associés des yeux." *Annales d'Oculistique* 90:1–21. (Parinaud
    syndrome — superior colliculus / pretectum — NOT an isolated
    CN IV palsy; bilateral CN IV palsy can occur from compression
    of the decussation at the superior medullary velum.)
*   **Pineal region tumors and bilateral CN IV palsy:** Keane, J.R.
    (1993). "Fourth nerve palsy: historical review and study of
    215 patients." *Neurology* 43:2439–2443. (Bilateral CN IV palsy
    from pineal region tumors compressing the superior medullary
    velum — the decussation site.)
*   **Superior oblique muscle actions:** von Noorden, G.K., Campos,
    E.C. (2002). *Binocular Vision and Ocular Motility*, 6th ed.
    (The superior oblique's three actions — depression in
    adduction, intorsion, abduction — and their clinical testing.)
*   **Myasthenia gravis (mimic — NMJ):** Drachman, D.B. (1994).
    "Myasthenia gravis." *New England Journal of Medicine*
    330:1797–1810. (Myasthenia gravis — fatigable diplopia,
    pupil-sparing, mimicking CN IV palsy — NOT a brainstem lesion.)
*   **Thyroid eye disease (mimic — orbit):** Bahn, R.S. (2010).
    "Graves' ophthalmopathy." *New England Journal of Medicine*
    362:726–738. (Thyroid eye disease — restrictive strabismus,
    mimicking CN IV palsy — NOT a brainstem lesion.)
*   **Brown syndrome (mimic — superior oblique tendon):** Brown,
    H.W. (1950). "Congenital structural muscle anomalies." In
    *Strabismus Ophthalmic Symposium* (Allen, ed.). (Brown
    syndrome — superior oblique tendon restriction, mimicking
    CN IV palsy — NOT a brainstem lesion.)
*   **MLF and INO (contrast — conduction pathway):** Frohman,
    T.C., Galetta, S.L., Fox, R.J., Solomon, D., Straumann, D.,
    Filippi, M., Zee, D.S., Frohman, E.M. (2008). "Pearls &
    Oy-sters: The medial longitudinal fasciculus in ocular motor
    physiology." *Neurology* 70:e57–e67. (The MLF as the
    internuclear pathway coordinating CN III, IV, VI for conjugate
    gaze; INO as the MLF lesion syndrome — distinct from CN IV
    palsy.)
*   **SLEA (contrast — the left trochlear nucleus is not SLEA):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the trochlear nucleus.)
*   NeuroNames — Trochlear nucleus (left); FMA — Trochlear nucleus
    (left member).
"""