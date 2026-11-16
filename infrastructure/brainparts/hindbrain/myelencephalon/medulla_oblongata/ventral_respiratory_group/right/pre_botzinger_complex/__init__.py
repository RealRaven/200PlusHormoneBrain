"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.pre_botzinger_complex
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── ventral_respiratory_group
                └── right
                    └── pre_botzinger_complex   <-- THIS MODULE

**Primary synonym:** Pre-Bötzinger complex (right); preBötC; PBC;
preinspiratory kernel; the respiratory rhythm kernel; the inspiratory
rhythm generator.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **functionally-defined region** of the **ventrolateral
medulla** — **not a classical Nissl-defined nucleus**. Its boundaries
are defined by **rhythm generation** and by **molecular markers**
(NK1R / substance-P receptor, somatostatin, Dbx1-lineage,
glutamatergic pacemaker neurons), not by a sharp cytoarchitectonic
border.
**Part of:** The **ventral respiratory group (VRG)** container —
specifically, the **right** side. The **VRG** is the **ventrolateral
medullary respiratory column** — the **Bötzinger complex**, the
**pre-Bötzinger complex**, the **nucleus ambiguus**, the **nucleus
retroambiguus**, and the **para-ambigual** region.
**Structural parent:** ``.../ventral_respiratory_group/right/`` →
**direct child** of the right VRG container.
**Structural children:** **None.** This is a **leaf** module. The
**rhythm-generating sub-circuits** (pacemaker neurons, NK1R neurons,
Dbx1-lineage neurons, somatostatin neurons) are documented as
**prose**, not as structural children.
**Boundary status (NOT the Bötzinger complex — the Bötzinger complex
is the EXPIRATORY oscillator):** **Boundary case — the
pre_botzinger_complex is NOT the Bötzinger complex; the Bötzinger
complex is the EXPIRATORY oscillator.** The **Bötzinger complex**
(``.../right/botzinger_complex/``, wired as a sibling under the
right VRG) is the **expiratory** oscillator — it **produces** the
**expiratory** phase of the respiratory cycle. The
**pre_botzinger_complex** (here) is the **inspiratory** oscillator —
it **produces** the **inspiratory** rhythm. **They are DIFFERENT
STRUCTURES**: the **pre-Bötzinger complex** is the **inspiratory
kernel**; the **Bötzinger complex** is the **expiratory oscillator**.
Consumers must **not** conflate the two — the
**pre_botzinger_complex** is the **inspiratory rhythm generator**; the
**Bötzinger complex** is the **expiratory rhythm generator**.
**Boundary status (NOT the whole ventral respiratory group — the VRG
is the COLUMN):** **Boundary case — the pre_botzinger_complex is NOT
the whole ventral respiratory group (VRG); the VRG is the COLUMN.**
The **VRG** (``.../ventral_respiratory_group/``) is the
**ventrolateral medullary respiratory column** — it **contains** the
Bötzinger complex, the pre-Bötzinger complex, the nucleus ambiguus,
the nucleus retroambiguus, and the para-ambigual region. The
**pre_botzinger_complex** (here) is **one sub-region** of that column
— the **inspiratory rhythm kernel**. **They are DIFFERENT
STRUCTURES**: the **VRG** is the **column**; the **pre-Bötzinger
complex** is **one kernel** within it. Consumers must **not**
conflate the pre-Bötzinger complex with the whole VRG — the
**pre_botzinger_complex** is a **sub-region** of the VRG.
**Boundary status (NOT the dorsal respiratory group — the DRG is the
SENSORY RELAY):** **Boundary case — the pre_botzinger_complex is NOT
the dorsal respiratory group (DRG); the DRG is the SENSORY RELAY.**
The **DRG** (``.../medulla_oblongata/dorsal_respiratory_group/``,
wired elsewhere in the medulla) is the **sensory relay** — the
**nucleus tractus solitarius (NTS)** — which receives **peripheral
chemoreceptor and baroreceptor** input and **relays** it to the
respiratory pattern generator. The **pre_botzinger_complex** (here)
is the **rhythm generator** — it **produces** the inspiratory rhythm
and **receives** the DRG drive. **They are DIFFERENT STRUCTURES**:
the **DRG** is the **sensory interface**; the **pre-Bötzinger
complex** is the **rhythm generator**. Consumers must **not** conflate
the two — the **DRG** is **sensory relay**; the
**pre_botzinger_complex** is **rhythm generation**.
**Boundary status (NOT the retrotrapezoid nucleus or the parafacial
respiratory group — those are the CHEMORECEPTOR and the EXPIRATORY
OSCILLATOR):** **Boundary case — the pre_botzinger_complex is NOT
the retrotrapezoid nucleus (RTN) and NOT the parafacial respiratory
group (pFRG).** The **RTN** (``.../medulla_oblongata/retrotrapezoid_
nucleus/``, wired elsewhere) is the **central chemoreceptor** —
it **senses** CO2/H+ and **drives** the respiratory rhythm. The
**pFRG** (wired elsewhere) is the **expiratory oscillator** — it
**produces** the **active expiration** rhythm. The
**pre_botzinger_complex** (here) is the **inspiratory rhythm
generator** — it **receives** the RTN drive and **produces** the
inspiratory rhythm. **They are DIFFERENT STRUCTURES**: the **RTN**
is the **chemoreceptor**; the **pFRG** is the **expiratory
oscillator**; the **pre-Bötzinger complex** is the **inspiratory
rhythm generator**. Consumers must **not** conflate the three.
**Boundary status (NOT the nucleus ambiguus or the nucleus
retroambiguus — those are the MOTOR/PREMOTOR POOLS):** **Boundary
case — the pre_botzinger_complex is NOT the nucleus ambiguus and
NOT the nucleus retroambiguus.** The **nucleus ambiguus**
(``.../medulla_oblongata/nucleus_ambiguus/``, wired elsewhere) is
the **vagal/laryngeal/cardiac motoneuron pool** — it **executes**
the motor output. The **nucleus retroambiguus** (wired elsewhere) is
the **expiratory premotor pool** — it **executes** the expiratory
motor pattern. The **pre_botzinger_complex** (here) is the
**rhythm generator** — it **produces** the rhythm that the **motor**
and **premotor** pools **execute**. **They are DIFFERENT
STRUCTURES**: the **nucleus ambiguus** and the **nucleus
retroambiguus** are **output** pools; the **pre-Bötzinger complex**
is the **rhythm generator**. Consumers must **not** conflate the
two.
**Boundary status (NOT a classical cytoarchitectonic nucleus — a
FUNCTIONALLY-DEFINED region):** **Boundary case — the
pre_botzinger_complex is NOT a classical Nissl-defined nucleus; it is
a FUNCTIONALLY-DEFINED region.** It is defined by **rhythm
generation** and by **molecular markers** (NK1R, somatostatin,
Dbx1-lineage), not by a sharp cytoarchitectonic border. The **VRG**
column **contains** it, and the **pre-Bötzinger complex** is the
**rhythm kernel** within the column. Consumers must **not** treat it
as a **sharply-bounded nucleus** — it is a **functionally-defined
region**.
**Boundary status (NOT the whole medulla oblongata — a sub-region
within it):** **Boundary case — the pre_botzinger_complex is a LEAF
child of the right VRG, not the medulla oblongata, not the VRG, and
not the left pre-Bötzinger complex.** The **medulla oblongata**
container contains the **VRG** (left and right), the **DRG**, the
**RTN**, the **pFRG**, the **nucleus ambiguus**, the **nucleus
retroambiguus**, the **hypoglossal nucleus**, and more. The
**pre_botzinger_complex** (here) is **one leaf** under the **right
VRG**. Consumers must **not** conflate the pre-Bötzinger complex with
the medulla oblongata or with the VRG.
**Boundary status (NOT the respiratory motoneuron pools — the
phrenic, intercostal, and hypoglossal nuclei are the EXECUTORS):**
**Boundary case — the pre_botzinger_complex is NOT a respiratory
motoneuron pool.** The **phrenic nucleus** (spinal cord, C3–C5), the
**intercostal motoneurons** (thoracic spinal cord), and the
**hypoglossal nucleus** (``.../medulla_oblongata/hypoglossal_
nucleus/``, wired elsewhere) are the **executors** — they **fire**
the motor output. The **pre_botzinger_complex** (here) is the
**rhythm generator** — it **produces** the rhythm that the **motor
pools** **execute**. Consumers must **not** conflate the **rhythm
generator** with the **motoneuron pools** — the **pre-Bötzinger
complex** generates the rhythm; the **motoneuron pools** execute it.
**Boundary status (NOT a single uniform neuron population — MULTIPLE
molecularly distinct neuron types):** **Boundary case — the
pre_botzinger_complex is a HETEROGENEOUS region with MULTIPLE
neuron types and MULTIPLE roles, not a single uniform population.**
It contains:
*   **Pacemaker neurons** — a subset with **intrinsic bursting**
    properties (persistent sodium, calcium-activated nonselective
    cation currents) — the **rhythm kernel** proper.
*   **NK1R-expressing neurons** — **substance-P receptor** —
    required for **normal breathing** and the **target of opioid
    respiratory depression**.
*   **Dbx1-lineage neurons** — **glutamatergic** — the **core
    rhythmogenic population**.
*   **Somatostatin-expressing neurons** — a **molecularly distinct
    population** with **distinct** roles in rhythm and pattern.
**Each population is functionally distinct** — the tree wires the
**pre-Bötzinger complex** as a **single leaf** under the right VRG;
the **neuron types** are **prose**, not structural children.
Consumers must **not** treat the region as a single uniform
population — it is a **heterogeneous rhythmogenic kernel**.
**Boundary status (BILATERAL COUPLING — the right and left
pre-Bötzinger complexes are COUPLED, not independent):** **Boundary
case — the pre_botzinger_complex is NOT functionally independent of
the left pre-Bötzinger complex.** The two **inspiratory oscillators**
are **coupled** via **commissural fibers** and **shared input** to
produce a **single coherent respiratory rhythm**. **Unilateral**
pre-Bötzinger complex is **sufficient to generate a rhythm** in many
reduced preparations, but the two sides can **desynchronize** if the
commissural connections are cut. Consumers must **not** assume the
right and left pre-Bötzinger complexes are **strictly independent** —
they are **structurally symmetric** and **functionally coupled**.

Overview
--------
The pre-Bötzinger complex is the **inspiratory rhythm kernel** of the
**ventral respiratory group (VRG)** — the **rhythm generator** that
**produces** the **inspiratory** rhythm of the respiratory cycle. It
is a **leaf** module under the **right** VRG container, and it is the
**respiratory CPG kernel** — the **site** of **inspiratory
rhythmogenesis**.

**The pre-Bötzinger complex is the INSPIRATORY OSCILLATOR, NOT the
expiratory oscillator.** The **expiratory oscillator** is the
**Bötzinger complex** (``.../right/botzinger_complex/``, sibling). The
**pre-Bötzinger complex** (here) **produces** the **inspiratory**
rhythm; the **Bötzinger complex** **produces** the **expiratory**
rhythm. **They are DIFFERENT STRUCTURES** — the **pre-Bötzinger
complex** is **inspiratory**; the **Bötzinger complex** is
**expiratory**.

**The pre-Bötzinger complex is a SUB-REGION of the VRG, NOT the whole
VRG.** The **VRG** (``.../ventral_respiratory_group/``) is the
**ventrolateral medullary respiratory column** — it **contains** the
Bötzinger complex, the pre-Bötzinger complex, the nucleus ambiguus,
the nucleus retroambiguus, and the para-ambigual region. The
**pre-Bötzinger complex** is **one kernel** within the column — the
**inspiratory rhythm generator**.

**The pre-Bötzinger complex is a RHYTHM GENERATOR, NOT a motor
output.** The **motor output** is executed by the **phrenic**,
**intercostal**, and **hypoglossal** motoneuron pools. The
**pre-Bötzinger complex** **generates** the rhythm; the **motoneuron
pools** **execute** it.

**The pre-Bötzinger complex is a paired structure, and the two sides
are COUPLED.** Each hemisphere has its own pre-Bötzinger complex, and
the two are **coupled** via **commissural fibers** and **shared
input** to produce a **single coherent respiratory rhythm**. The two
sides are **structurally symmetric** and **functionally coupled** —
this is a **coupling warning**, NOT a **strict-mirror-with-no-
warning**. See *Lateralization Notes*.

Rhythm-Generating Sub-Circuits (prose, not structural children)
---------------------------------------------------------------
The pre-Bötzinger complex is a **heterogeneous rhythmogenic kernel** —
documented as **prose**, not as structural children:

*   **Pacemaker neurons** — a subset with **intrinsic bursting**
    properties (persistent sodium, calcium-activated nonselective
    cation currents). The **rhythm kernel** proper.

*   **NK1R-expressing neurons** — **substance-P receptor** —
    required for **normal breathing**; the **target of opioid
    respiratory depression**.

*   **Dbx1-lineage neurons** — **glutamatergic** — the **core
    rhythmogenic population**; the **developmental origin** of the
    kernel.

*   **Somatostatin-expressing neurons** — a **molecularly distinct
    population** with **distinct** roles in rhythm and pattern.

**These neuron types are prose, not structural children.** The tree
wires the **pre_botzinger_complex** as a **single leaf** under the
right VRG — the **pacemaker**, **NK1R**, **Dbx1-lineage**, and
**somatostatin** neurons are **prose**, not structural children.
Consumers that need **neuron-type-level** resolution should consult
the references, not the tree.

The Pre-Bötzinger Complex / Bötzinger Complex Boundary
------------------------------------------------------
This is the **most consequential sibling** boundary — **inspiratory
vs. expiratory**:

*   **Pre_botzinger_complex** (this module) — the **inspiratory
    rhythm kernel**.

*   **Bötzinger complex** (``.../right/botzinger_complex/``, wired as
    a sibling under the right VRG) — the **expiratory oscillator**.

**They are siblings under the right VRG.** The **pre-Bötzinger
complex** is the **inspiratory** rhythm generator; the **Bötzinger
complex** is the **expiratory** rhythm generator. **Consumers must
not conflate the two** — the **pre_botzinger_complex** is the
**inspiratory kernel**; the **Bötzinger complex** is the **expiratory
oscillator**.

The Pre-Bötzinger Complex / Whole VRG Boundary
----------------------------------------------
This is the **column** boundary:

*   **Pre_botzinger_complex** (this module) — the **inspiratory
    rhythm kernel**.

*   **Ventral respiratory group (VRG)** (``.../ventral_respiratory_
    group/``) — the **ventrolateral medullary respiratory column**.

**The pre-Bötzinger complex is a SUBSET of the VRG** — it is **one
kernel** within the column. Consumers must **not** conflate the
**pre-Bötzinger complex** with the **whole VRG**.

The Pre-Bötzinger Complex / Dorsal Respiratory Group Boundary
-------------------------------------------------------------
This is the **sensory-relay** boundary:

*   **Pre_botzinger_complex** (this module) — the **inspiratory
    rhythm kernel**.

*   **Dorsal respiratory group (DRG)** (``.../medulla_oblongata/
    dorsal_respiratory_group/``, wired elsewhere) — the **sensory
    relay** (nucleus tractus solitarius).

**The DRG is the SENSORY interface; the pre-Bötzinger complex is the
RHYTHM GENERATOR.** Consumers must **not** conflate the two — the
**DRG** is **sensory relay**; the **pre_botzinger_complex** is
**rhythm generation**.

The Pre-Bötzinger Complex / RTN and pFRG Boundary
-------------------------------------------------
This is the **chemoreceptor / expiratory-oscillator** boundary:

*   **Pre_botzinger_complex** (this module) — the **inspiratory
    rhythm kernel**.

*   **Retrotrapezoid nucleus (RTN)** (``.../medulla_oblongata/
    retrotrapezoid_nucleus/``, wired elsewhere) — the **central
    chemoreceptor** (CO2/H+ sensor).

*   **Parafacial respiratory group (pFRG)** (wired elsewhere) — the
    **expiratory oscillator** (active expiration).

**The RTN is the CHEMORECEPTOR; the pFRG is the EXPIRATORY
OSCILLATOR; the pre-Bötzinger complex is the INSPIRATORY RHYTHM
GENERATOR.** Consumers must **not** conflate the three.

The Pre-Bötzinger Complex / Nucleus Ambiguus and Nucleus Retroambiguus Boundary
------------------------------------------------------------------------------
This is the **motor/premotor output** boundary:

*   **Pre_botzinger_complex** (this module) — the **inspiratory
    rhythm kernel**.

*   **Nucleus ambiguus** (``.../medulla_oblongata/nucleus_ambiguus/``,
    wired elsewhere) — the **vagal/laryngeal/cardiac motoneuron
    pool**.

*   **Nucleus retroambiguus** (wired elsewhere) — the **expiratory
    premotor pool**.

**The pre-Bötzinger complex GENERATES the rhythm; the nucleus
ambiguus and nucleus retroambiguus EXECUTE the motor pattern.**
Consumers must **not** conflate the **rhythm generator** with the
**motor/premotor pools**.

The Pre-Bötzinger Complex / Respiratory Motoneuron Pools Boundary
-----------------------------------------------------------------
This is the **executor** boundary:

*   **Pre_botzinger_complex** (this module) — the **inspiratory
    rhythm kernel**.

*   **Phrenic nucleus** (spinal cord, C3–C5), **intercostal
    motoneurons** (thoracic spinal cord), **hypoglossal nucleus**
    (``.../medulla_oblongata/hypoglossal_nucleus/``, wired elsewhere)
    — the **executors**.

**The pre-Bötzinger complex generates the rhythm; the motoneuron
pools execute it.** Consumers must **not** conflate the **rhythm
generator** with the **motoneuron pools**.

The Pre-Bötzinger Complex / Cytoarchitectonic Nucleus Boundary
--------------------------------------------------------------
This is the **functionally-defined-region** boundary:

*   **Pre_botzinger_complex** (this module) — a **functionally-
    defined region** of the ventrolateral medulla.

*   **Classical Nissl-defined nuclei** — the **nucleus ambiguus**,
    the **hypoglossal nucleus**, the **nucleus tractus solitarius**,
    etc.

**The pre-Bötzinger complex is defined by RHYTHM GENERATION and
MOLECULAR MARKERS, not by a sharp cytoarchitectonic border.**
Consumers must **not** treat it as a **sharply-bounded nucleus**.

Function in the Human Brain
---------------------------
The pre-Bötzinger complex's functions are **respiratory rhythm
generation** and **inspiratory drive** — **NOT the expiratory
oscillator** and **NOT the motor output**:

*   **Inspiratory Rhythmogenesis (the rhythm kernel):** The
    pre-Bötzinger complex **generates** the **inspiratory** rhythm
    — the **kernel** of the respiratory central pattern generator
    (CPG). The rhythm is **produced** by the **pacemaker neurons**
    (intrinsic bursting) and by **network interactions** among the
    **NK1R**, **Dbx1-lineage**, and **somatostatin** populations.
    This is the **neural substrate** of **automatic breathing
    rhythm**.

*   **Rhythm → Pattern (the pre-Bötzinger complex is the kernel, not
    the pattern):** The pre-Bötzinger complex **produces** the
    **rhythm**; the **pattern** is **distributed** to the premotor
    pools (the **nucleus retroambiguus**, the **nucleus ambiguus**,
    the **hypoglossal nucleus**) and to the **motoneuron pools**
    (the **phrenic nucleus**, the **intercostal motoneurons**) which
    **execute** the motor pattern. The pre-Bötzinger complex is the
    **kernel**; the **pattern** is the **downstream** output.

*   **Opioid Sensitivity (μ-opioid receptors on NK1R neurons):** The
    **NK1R-expressing pre-Bötzinger neurons** carry **μ-opioid
    receptors** — **opioids** **depress** the pre-Bötzinger complex
    and **suppress** the respiratory rhythm. This is the **neural
    substrate** of **opioid-induced respiratory depression
    (OIRD)**.

*   **Bilateral Coupling (the two sides must synchronize):** The
    right and left pre-Bötzinger complexes are **coupled** via
    **commissural fibers** and **shared input** — they
    **synchronize** to produce a **single coherent respiratory
    rhythm**. **Unilateral** pre-Bötzinger complex is **sufficient**
    to generate a rhythm in many reduced preparations, but the two
    sides can **desynchronize** if the connections are cut.

*   **NOT the expiratory oscillator.** The **expiratory** rhythm is
    produced by the **Bötzinger complex** and the **pFRG** —
    **separate structures**. The **pre-Bötzinger complex** is the
    **inspiratory** rhythm generator.

*   **NOT the chemoreceptor.** The **RTN** **senses** CO2/H+ — the
    **pre-Bötzinger complex** **receives** the RTN drive and
    **produces** the rhythm. The **pre-Bötzinger complex** is the
    **rhythm generator**; the **RTN** is the **sensor**.

*   **NOT the motor output.** The **motoneuron pools** (phrenic,
    intercostal, hypoglossal) **execute** the motor pattern. The
    **pre-Bötzinger complex** **generates** the rhythm.

**The unifying theme:** the pre-Bötzinger complex is the
**inspiratory rhythm kernel** of the **ventral respiratory group** —
the **functionally-defined region** that **produces** the
**inspiratory** rhythm. It is **the rhythm generator**, **NOT** the
expiratory oscillator (**Bötzinger complex**), **NOT** the
chemoreceptor (**RTN**), and **NOT** the motor output (the
**motoneuron pools**).

Associated Disorders
--------------------
The pre-Bötzinger complex has **no named clinical syndrome of its
own** — its clinical associations are **direct**, via the rhythm it
generates and the receptors it carries:

*   **Opioid-Induced Respiratory Depression (OIRD — via the NK1R
    neurons):** The **NK1R-expressing pre-Bötzinger neurons** carry
    **μ-opioid receptors** — **opioids** **depress** the
    pre-Bötzinger complex and **suppress** the respiratory rhythm.
    **OIRD** is the **direct** clinical consequence of pre-Bötzinger
    complex **opioid sensitivity** — and the **NK1R population** is
    the **therapeutic target** for **opioid-sparing analgesia**.

*   **Central Sleep Apnea (via the rhythm generator):** The
    **pre-Bötzinger complex** is the **rhythm kernel** — its
    **dysfunction** contributes to **central sleep apnea** and to
    the **apneas** of **Rett syndrome** (MECP2) and of **apnea of
    prematurity**.

*   **Rett Syndrome (via pre-Bötzinger dysfunction):** **MECP2**
    mutations **disrupt** the **pre-Bötzinger complex** —
    contributing to the **severe apneas** and **respiratory
    arrhythmias** of **Rett syndrome**.

*   **Sudden Infant Death Syndrome (SIDS — proposed):** The
    **pre-Bötzinger complex** and the **arcuate nucleus** have been
    **proposed** as **sites** of **dysfunction** in **SIDS** — via
    **arousal failure** and **respiratory rhythm instability**.
    This is **proposed**, not established.

*   **Apnea of Prematurity (via pre-Bötzinger immaturity):** The
    **pre-Bötzinger complex** is **immature** in **preterm
    infants** — contributing to the **apneas** of prematurity.

*   **No Named "Pre-Bötzinger Complex Syndrome":** The
    pre-Bötzinger complex is a **functionally-defined region**, not
    a **single sharply-bounded structure** — it has **no named
    clinical syndrome of its own**. Its clinical relevance is
    **direct**, via the **rhythm** it generates and the **μ-opioid
    receptors** it carries.

**What is NOT here:** The pre-Bötzinger complex is **not** the
substrate for **CCHS (Ondine's curse)** (RTN — PHOX2B
chemoreceptor), **Wallenberg syndrome** (lateral medulla — nucleus
ambiguus, spinothalamic tract), **locked-in syndrome** (basis
pontis), or **Kluver-Bucy syndrome** (amygdala). Its clinical
relevance is **direct**, via the **inspiratory rhythm** and the
**μ-opioid receptors** it carries. **No named pre-Bötzinger complex
syndrome exists.**

Lateralization Notes
--------------------
This is the **right** pre_botzinger_complex module. The
pre_botzinger_complex is **bilaterally symmetric** and
**functionally COUPLED** — and it carries a **coupling warning**:

*   **Bilateral Coupling (the two sides must synchronize):** Each
    hemisphere has its own pre-Bötzinger complex, and the two are
    **coupled** via **commissural fibers** and **shared input** to
    produce a **single coherent respiratory rhythm**. **Unilateral**
    pre-Bötzinger complex is **sufficient** to generate a rhythm in
    many reduced preparations, but the two sides can
    **desynchronize** if the connections are cut.

*   **Coupling Warning (NOT a strict-mirror-with-no-warning):** The
    right and left pre-Bötzinger complexes are **structurally
    symmetric** but **functionally coupled**. Consumers must
    **not** assume the two sides are **strictly independent** — a
    **single coherent respiratory rhythm** requires **both sides**.

*   **No Inherited Amygdala-Lateralization Warning:** The
    pre-Bötzinger complex is **not** part of the amygdala — it does
    **not** inherit the amygdala-lateralization warning. It carries
    its **own** **coupling warning** at the **structure level**.

**A consumer that assumes "right pre_botzinger_complex = left
pre_botzinger_complex" will be structurally correct** — the two
sides are **symmetric**. But a consumer that assumes the two sides
are **functionally independent** will be **wrong** — the two sides
are **coupled** and a **single coherent rhythm** requires **both**.
The pre_botzinger_complex is a **strict-mirror pair with a COUPLING
warning** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag**, but **a
coupling warning of its own**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../botzinger_complex/``, ``.../dorsal_respiratory_group/``,
    ``.../retrotrapezoid_nucleus/``, ``.../nucleus_ambiguus/``,
    ``.../hypoglossal_nucleus/``, the **pons**, the **spinal cord**,
    or any other container. The pre-Bötzinger complex's
    relationships to the Bötzinger complex, the DRG, the RTN, the
    pFRG, the nucleus ambiguus, the nucleus retroambiguus, the
    hypoglossal nucleus, and the respiratory motoneuron pools are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **pacemaker**,
    **NK1R**, **Dbx1-lineage**, and **somatostatin** neuron types are
    documented as **prose**, not as sub-modules. Consumers must not
    assume any exist as children; resolve **neuron-type-level**
    detail through the references.
*   **Inspiratory rhythm kernel — NOT the expiratory oscillator.**
    The **Bötzinger complex** (sibling) is the **expiratory
    oscillator**; the **pre_botzinger_complex** is the
    **inspiratory** rhythm generator. Consumers must **not** conflate
    the two.
*   **Sub-region of the VRG — NOT the whole VRG.** The
    pre-Bötzinger complex is **one kernel** within the **ventral
    respiratory group**. Consumers must **not** conflate the
    **pre-Bötzinger complex** with the **whole VRG**.
*   **NOT the dorsal respiratory group — the DRG is the SENSORY
    RELAY.** The pre-Bötzinger complex is the **rhythm generator**;
    the DRG is the **sensory interface**.
*   **NOT the RTN or the pFRG — those are the CHEMORECEPTOR and the
    EXPIRATORY OSCILLATOR.** The pre-Bötzinger complex is the
    **inspiratory rhythm generator**.
*   **NOT the nucleus ambiguus or the nucleus retroambiguus — those
    are the MOTOR/PREMOTOR POOLS.** The pre-Bötzinger complex is the
    **rhythm generator**.
*   **NOT the respiratory motoneuron pools — the phrenic,
    intercostal, and hypoglossal nuclei are the EXECUTORS.** The
    pre-Bötzinger complex **generates** the rhythm; the **motoneuron
    pools** **execute** it.
*   **NOT a classical cytoarchitectonic nucleus — a FUNCTIONALLY-
    DEFINED region.** Defined by **rhythm generation** and
    **molecular markers**, not by a sharp Nissl border.
*   **NOT a single uniform neuron population — MULTIPLE molecularly
    distinct neuron types.** The **pacemaker**, **NK1R**,
    **Dbx1-lineage**, and **somatostatin** populations are **prose**,
    not structural children.
*   **BILATERAL COUPLING WARNING — the right and left pre-Bötzinger
    complexes are COUPLED.** The two sides are **structurally
    symmetric** and **functionally coupled** — a **single coherent
    respiratory rhythm** requires **both**. Consumers must **not**
    assume the two sides are **functionally independent**.
*   **No ``AREA_PATHS`` hop.** The pre_botzinger_complex is a
    local leaf under the right VRG, not a cross-listed leaf.
*   **No nested cross-listing.** The pre_botzinger_complex has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left pre_botzinger_complex — strict
    mirror WITH coupling warning.** Right and left pre-Bötzinger
    complex modules are **structurally identical** — same leaf
    status, same **rhythm-kernel** framing, same **coupling
    warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right import pre_botzinger_complex

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "ventral_respiratory_group.right.pre_botzinger_complex"
    )

**Do not** assume the pre_botzinger_complex is the **Bötzinger
complex**. The **Bötzinger complex** is the **expiratory
oscillator**; the **pre_botzinger_complex** is the **inspiratory
rhythm kernel**.

**Do not** assume the pre_botzinger_complex is the **whole ventral
respiratory group**. It is only the **inspiratory kernel** — one
sub-region of the VRG.

**Do not** assume the pre_botzinger_complex is the **dorsal
respiratory group**. The **DRG** is the **sensory relay**; the
**pre_botzinger_complex** is the **rhythm generator**.

**Do not** assume the pre_botzinger_complex is the **retrotrapezoid
nucleus** or the **parafacial respiratory group**. Those are the
**chemoreceptor** and the **expiratory oscillator**; the
**pre_botzinger_complex** is the **inspiratory rhythm generator**.

**Do not** assume the pre_botzinger_complex is the **nucleus
ambiguus** or the **nucleus retroambiguus**. Those are the
**motor/premotor pools**; the **pre_botzinger_complex** is the
**rhythm generator**.

**Do not** import the **amygdala-lateralization warning** into the
pre_botzinger_complex — it is **not** an amygdala structure.
**The pre_botzinger_complex carries its own COUPLING warning** — the
two sides are **coupled** and a **single coherent rhythm** requires
**both**.

Iterating the pre_botzinger_complex's (empty) children (recommended
consumer pattern)::

    PRE_BOTZINGER_COMPLEX_CHILDREN = ()
    # The pre_botzinger_complex is a leaf. The pacemaker, NK1R,
    # Dbx1-lineage, and somatostatin neuron types are prose, not
    # modules.

Reaching the Bötzinger complex (recommended consumer pattern — the
sibling)::

    # The Bötzinger complex is the EXPIRATORY SIBLING of the
    # pre-Bötzinger complex — the expiratory oscillator:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   ventral_respiratory_group.right.botzinger_complex
    #
    # The pre-Bötzinger complex is the INSPIRATORY oscillator; the
    # Bötzinger complex is the EXPIRATORY oscillator.

Reaching the whole ventral respiratory group (recommended consumer
pattern — NOTE the subset boundary)::

    # The whole ventral respiratory group (VRG) is the ventrolateral
    # medullary respiratory COLUMN — it contains the Bötzinger
    # complex, the pre-Bötzinger complex, the nucleus ambiguus, the
    # nucleus retroambiguus, and the para-ambigual region:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   ventral_respiratory_group
    #
    # The pre-Bötzinger complex is one KERNEL within the VRG.

Reaching the dorsal respiratory group (recommended consumer pattern —
the sensory relay)::

    # The dorsal respiratory group (DRG) is the SENSORY relay
    # (nucleus tractus solitarius) — it receives peripheral
    # chemoreceptor and baroreceptor input:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   dorsal_respiratory_group
    #
    # The pre-Bötzinger complex is the RHYTHM GENERATOR; the DRG is
    # the SENSORY RELAY.

Reaching the RTN and the pFRG (recommended consumer pattern — NOTE
the chemoreceptor / expiratory-oscillator boundary)::

    # The retrotrapezoid nucleus (RTN) is the CENTRAL CHEMORECEPTOR
    # (CO2/H+ sensor); the parafacial respiratory group (pFRG) is
    # the EXPIRATORY OSCILLATOR:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   retrotrapezoid_nucleus
    #
    # The pre-Bötzinger complex is the INSPIRATORY RHYTHM GENERATOR.

Reaching the nucleus ambiguus and the nucleus retroambiguus
(recommended consumer pattern — the motor/premotor pools)::

    # The nucleus ambiguus is the VAGAL/LARYNGEAL/CARDIAC MOTONEURON
    # POOL; the nucleus retroambiguus is the EXPIRATORY PREMOTOR
    # POOL. They EXECUTE the motor pattern:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.nucleus_ambiguus
    #
    # The pre-Bötzinger complex GENERATES the rhythm; the
    # nucleus ambiguus and nucleus retroambiguus EXECUTE it.

Reaching the respiratory motoneuron pools (recommended consumer
pattern — NOTE the executor boundary)::

    # The respiratory motoneuron pools — the phrenic nucleus (spinal
    # cord, C3–C5), the intercostal motoneurons (thoracic spinal
    # cord), and the hypoglossal nucleus (medulla) — EXECUTE the
    # motor pattern:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.hypoglossal_nucleus
    #
    # The pre-Bötzinger complex GENERATES the rhythm; the motoneuron
    # pools EXECUTE it.

Reaching the pontine respiratory group (recommended consumer pattern
— NOTE it is PONTINE, not medullary)::

    # The pontine respiratory group (PRG — the "pneumotaxic center")
    # is PONTINE — it modulates the medullary rhythm but is not part
    # of the medulla:
    #
    #   hindbrain.metencephalon.pons.pontine_respiratory_group
    #
    # The pre-Bötzinger complex is the MEDULLARY rhythm generator;
    # the PRG is the PONTINE modulator.

Bilateral iteration (recommended consumer pattern — NOTE the
coupling warning)::

    for side in ("left", "right"):
        pbc_path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"ventral_respiratory_group.{side}."
            f"pre_botzinger_complex"
        )
        # resolve pbc_path through the memory/recall layer
        #
        # WARNING: the two sides are COUPLED. A single coherent
        # respiratory rhythm requires BOTH sides. Do not treat
        # left and right as functionally independent.

Neuron-type-level detail (not wired — consult references)::

    # The pre-Bötzinger complex's neuron types are prose, not
    # modules:
    #   pacemaker neurons    -> intrinsic bursting (rhythm kernel)
    #   NK1R neurons         -> required for normal breathing;
    #                           μ-opioid target
    #   Dbx1-lineage neurons -> core rhythmogenic population
    #   somatostatin neurons -> molecularly distinct population
    #
    # Do not attempt to resolve these as sub-paths of the
    # pre_botzinger_complex.

References
----------
*   **Canonical pre-Bötzinger complex discovery:** Smith, J.C.,
    Ellenberger, H.H., Ballanyi, K., Richter, D.W., Feldman, J.L.
    (1991). "Pre-Bötzinger complex: a brainstem region that may
    generate respiratory rhythm in mammals." *Science* 254:726–729.
    (The discovery of the pre-Bötzinger complex as the respiratory
    rhythm kernel.)
*   **Pre-Bötzinger complex review:** Feldman, J.L., Del Negro, C.A.
    (2006). "Looking for inspiration: new perspectives on
    respiratory rhythm." *Nature Reviews Neuroscience* 7:232–242.
    (Definitive review of the pre-Bötzinger complex and the
    respiratory CPG.)
*   **NK1R neurons and normal breathing:** Gray, P.A., Janczewski,
    W.A., Mellen, N., McCrimmon, D.R., Feldman, J.L. (2001).
    "Normal breathing requires preBötzinger complex neurokinin-1
    receptor-expressing neurons." *Nature Neuroscience* 4:927–930.
    (NK1R pre-Bötzinger neurons are required for normal breathing.)
*   **Dbx1-lineage and rhythmogenesis:** Bouvier, J., Thoby-Brisson,
    M., Renier, N., et al. (2010). "Hindbrain interneurons and axon
    guidance signaling critical for breathing." *Nature Neuroscience*
    13:1066–1074. (Dbx1-lineage glutamatergic neurons as the core
    rhythmogenic population.)
*   **Bilateral coupling and microcircuits:** Smith, J.C., Abdala,
    A.P.L., Borgmann, A., Rybak, I.A., Paton, J.F.R. (2013).
    "Brainstem respiratory networks: building blocks and
    microcircuits." *Trends in Neurosciences* 36:152–162. (The
    pre-Bötzinger complex microcircuit and the bilateral coupling of
    the two oscillators.)
*   **Pacemaker neurons:** Koshiya, N., Smith, J.C. (1999).
    "Neuronal pacemaker for breathing visualized in vitro."
    *Nature* 400:360–363. (Pacemaker neurons in the pre-Bötzinger
    complex.)
*   **Respiratory rhythm generation review:** Del Negro, C.A., Funk,
    G.D., Feldman, J.L. (2018). "Breathing matters." *Nature
    Reviews Neuroscience* 19:351–367. (Recent review of the
    pre-Bötzinger complex and respiratory rhythm generation.)
*   **In vivo rhythm generation:** Richter, D.W., Smith, J.C.
    (2014). "Respiratory rhythm generation in vivo." *Physiology*
    29:58–71. (In vivo evidence for the pre-Bötzinger complex as
    the rhythm generator.)
*   **Opioid-induced respiratory depression (OIRD):** Montandon, G.,
    Ren, J., Victoria, N.C., Liu, H., Wickman, K., Greer, J.J.,
    Horner, R.L. (2016). "PreBötzinger complex neurokinin-1
    receptor-expressing neurons mediate opioid-induced respiratory
    depression." *Journal of Neuroscience* 36:1292–1301. (The
    NK1R pre-Bötzinger neurons as the target of opioid respiratory
    depression.)
*   **Rett syndrome and pre-Bötzinger dysfunction:** Lioy, D.T.,
    Wu, W.W., Bissonnette, J.M. (2011). "A role for glia in the
    progression of Rett's syndrome." *Nature* 475:497–500. (Glial
    and pre-Bötzinger dysfunction in Rett syndrome.)
*   **SIDS and the medullary respiratory network:** Kinney, H.C.,
    Richerson, G.B., Dymecki, S.M., Darnall, R.A., Nattie, E.E.
    (2009). "The brainstem and serotonin in the sudden infant death
    syndrome." *Annual Review of Pathology* 4:517–550. (The
    pre-Bötzinger complex and the arcuate nucleus in SIDS — a
    proposed link.)
*   **RTN and central chemoreception (contrast — NOT this module):**
    Guyenet, P.G., Stornetta, R.L., Abbott, S.B.G., Depuy, S.D.,
    Fortuna, M.G., Kanbar, R. (2009). "Central CO2 chemoreception
    and integrated neural mechanisms of cardiovascular and
    respiratory control." *Journal of Applied Physiology*
    108:995–1002. (The RTN as the central chemoreceptor — contrast
    with the pre-Bötzinger complex rhythm generator.)
*   **Bötzinger complex (contrast — the expiratory sibling):**
    Smith, J.C., Abdala, A.P.L., Koizumi, H., Rybak, I.A., Paton,
    J.F.R. (2007). "Spatial and functional architecture of the
    mammalian brainstem respiratory network: a hierarchy of three
    oscillatory mechanisms." *Journal of Neurophysiology*
    98:3370–3387. (The Bötzinger complex as the expiratory
    oscillator — contrast with the pre-Bötzinger complex.)
*   **Nucleus ambiguus and nucleus retroambiguus (contrast — the
    motor/premotor pools):** Bautista, T.G., Sun, Q.-J., Pilowsky,
    P.M. (2012). "The generation of phrenic and sympathetic
    respiratory activities." *Respiratory Physiology & Neurobiology*
    184:1–12. (The motor and premotor pools — contrast with the
    rhythm generator.)
*   **Pontine respiratory group (contrast — the pontine modulator):**
    Dutschmann, M., Dick, T.E. (2012). "Pontine mechanisms of
    respiratory control." *Comprehensive Physiology* 2:2443–2469.
    (The pontine respiratory group as the pontine modulator —
    contrast with the medullary rhythm generator.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary respiratory groups in overview.)
*   NeuroNames — Pre-Bötzinger complex (right); FMA — Pre-Bötzinger
    complex (right member).
"""