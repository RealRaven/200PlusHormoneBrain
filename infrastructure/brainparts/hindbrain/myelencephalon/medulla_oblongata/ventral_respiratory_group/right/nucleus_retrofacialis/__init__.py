"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right.nucleus_retrofacialis
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── ventral_respiratory_group
                └── right
                    └── nucleus_retrofacialis   <-- THIS MODULE

**Primary synonym:** Nucleus retrofacialis (right); retrofacial
nucleus (RFN); RFR; retrofacial nucleus of the ventrolateral medulla;
the rostral expiratory premotor nucleus.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). Unlike the **pre-Bötzinger complex**, the nucleus
retrofacialis **IS a classical Nissl-defined nucleus** — a
cytoarchitectonically delimited cell group in the **rostral
ventrolateral medulla**, immediately **caudal to the facial nucleus
(nucleus VII)** — hence "retro-facial." Its borders are **Nissl
borders**, not functional or molecular borders. **Nomenclature
contest:** some atlases assign it to the **intermediate reticular
nucleus** of the reticular formation rather than to the VRG column;
this tree follows the **VRG assignment**.
**Part of:** The **ventral respiratory group (VRG)** container —
specifically, the **right** side, **rostral** division. The **VRG**
is the **ventrolateral medullary respiratory column** — the
**Bötzinger complex**, the **pre-Bötzinger complex**, the **nucleus
retrofacialis**, the **nucleus ambiguus**, the **nucleus
retroambiguus**, and the **para-ambigual** region.
**Structural parent:** ``.../ventral_respiratory_group/right/`` →
**direct child** of the right VRG container.
**Structural children:** **None.** This is a **leaf** module. The
**expiratory premotor neuron populations** (bulbospinal E2 neurons,
propriobulbar expiratory neurons) are documented as **prose**, not as
structural children.
**Boundary status (NOT the Bötzinger complex — the Bötzinger complex
is the FUNCTIONALLY-DEFINED expiratory oscillator):** **Boundary case
— the nucleus_retrofacialis is NOT the Bötzinger complex.** This is
the **most consequential sibling boundary** in the module, and it is
**contested in the literature**: the **Bötzinger complex** is often
defined **topographically as the region containing the retrofacial
nucleus**. This tree wires them as **DISTINCT SIBLINGS** because it
separates the **functionally-defined expiratory oscillator**
(**Bötzinger complex**) from the **cytoarchitectonically-defined
nucleus** (**nucleus retrofacialis**) that **overlaps** it. The
**Bötzinger complex** (``.../right/botzinger_complex/``) is the
**expiratory oscillator** — a **functional microcircuit**; the
**nucleus_retrofacialis** (here) is the **Nissl-defined nucleus**
that **houses** expiratory premotor neurons. **They are DIFFERENT
KINDS OF STRUCTURE** — the **Bötzinger complex** is defined by
**function**; the **nucleus retrofacialis** is defined by
**cytoarchitecture**. Consumers must **not** conflate the two, and
must **not** assume the two are mutually exclusive — they
**overlap**.
**Boundary status (NOT the pre-Bötzinger complex — the pre-Bötzinger
complex is the INSPIRATORY oscillator):** **Boundary case — the
nucleus_retrofacialis is NOT the pre-Bötzinger complex.** The
**pre-Bötzinger complex** (``.../right/pre_botzinger_complex/``) is
the **inspiratory** rhythm kernel — it **generates** the
**inspiratory** rhythm. The **nucleus_retrofacialis** (here) is an
**expiratory premotor pool** — it **distributes** the
**expiratory** drive. **They are DIFFERENT STRUCTURES** on
**opposite phases** of the respiratory cycle. Consumers must **not**
conflate the two — the **pre-Bötzinger complex** is **inspiratory
rhythm generation**; the **nucleus retrofacialis** is **expiratory
premotor output**.
**Boundary status (NOT the nucleus ambiguus — the nucleus ambiguus is
the BRANCHIOMOTOR pool):** **Boundary case — the
nucleus_retrofacialis is NOT the nucleus ambiguus.** The **nucleus
ambiguus** (``.../medulla_oblongata/nucleus_ambiguus/``, wired
elsewhere) is the **branchiomotor** pool — **vagal, glossopharyngeal,
laryngeal, pharyngeal, and cardiac** motoneurons — a **somatic
motoneuron** population. The **nucleus_retrofacialis** (here) is an
**expiratory premotor** pool — **bulbospinal** neurons that **drive**
spinal expiratory motoneurons; it contains **no** branchiomotor
motoneurons. **They are DIFFERENT STRUCTURES**: the **nucleus
ambiguus** is a **motoneuron** pool; the **nucleus retrofacialis** is
a **premotor** pool. Consumers must **not** conflate the two.
**Boundary status (NOT the nucleus retroambiguus — the nucleus
retroambiguus is the CAUDAL expiratory premotor pool):** **Boundary
case — the nucleus_retrofacialis is NOT the nucleus retroambiguus.**
The **nucleus retroambiguus** (wired elsewhere, **caudal** VRG) is
the **caudal** expiratory premotor pool — it drives **abdominal and
thoracic** expiratory motoneurons and is the **premotor substrate**
of **cough and sneeze**. The **nucleus_retrofacialis** (here) is the
**rostral** expiratory premotor pool. **They are DIFFERENT
STRUCTURES** at **different rostrocaudal levels** of the same
column. Consumers must **not** conflate the two — both are
**expiratory premotor**, but they are **rostral vs. caudal**
**siblings**, not one structure.
**Boundary status (NOT the parafacial respiratory group — the pFRG
is the ACTIVE-EXPIRATION OSCILLATOR):** **Boundary case — the
nucleus_retrofacialis is NOT the parafacial respiratory group
(pFRG).** The **pFRG** (wired elsewhere) is the **active-expiration
oscillator** — it **generates** the **active expiratory** rhythm
(a functionally-defined oscillator, like the Bötzinger complex). The
**nucleus_retrofacialis** (here) is a **premotor pool** — it
**distributes** expiratory drive; it does **not** generate the
rhythm. **They are DIFFERENT STRUCTURES**: the **pFRG** is an
**oscillator**; the **nucleus retrofacialis** is a **premotor
pool**. Consumers must **not** conflate the two — the **pFRG**
**generates** active expiration; the **nucleus retrofacialis**
**relays** expiratory drive. *(This is the same
oscillator-vs-premotor-pool distinction as the Bötzinger boundary,
and the same distinction as the pre-Bötzinger boundary — see
Design Contract.)*
**Boundary status (NOT the facial nucleus — the facial nucleus is the
BRANCHIOMOTOR neighbor):** **Boundary case — the
nucleus_retrofacialis is NOT the facial nucleus (nucleus VII).** The
**facial nucleus** (``.../metencephalon/pons/facial_nucleus/``,
wired elsewhere) is the **branchiomotor** nucleus for the **facial
musculature** — it is the **rostral neighbor** that gives the
retrofacial nucleus its name ("retro-facial" = **caudal to the
facial nucleus**). The **nucleus_retrofacialis** (here) is an
**expiratory premotor** pool. **They are DIFFERENT STRUCTURES** —
the **facial nucleus** is **branchiomotor**; the **nucleus
retrofacialis** is **respiratory premotor**. Consumers must **not**
conflate the two, and must **not** resolve the nucleus retrofacialis
as a child of the facial nucleus — it is a **VRG** child.
**Boundary status (NOT the C1 adrenergic group / RVLM — the C1 group
is the SYMPATHETIC PREMOTOR population):** **Boundary case — the
nucleus_retrofacialis is NOT the C1 adrenergic group and NOT the
rostral ventrolateral medulla (RVLM) cardiovascular premotor
population.** The **C1 group** — **PNMT-expressing, adrenergic**
neurons of the **RVLM** — is the **sympathetic premotor** population
that **drives** the **vasomotor** outflow. **C1 neurons overlap
topographically with the region of the nucleus retrofacialis** —
this is a **real, documented overlap**, and it is a **boundary
hazard**. The **nucleus_retrofacialis** (here) is the
**respiratory (expiratory premotor)** population; the **C1 group**
is the **cardiovascular (sympathetic premotor)** population.
**They are DIFFERENT FUNCTIONAL POPULATIONS** that **share a
neighborhood**. Consumers must **not** conflate the two, and must
**not** attribute **sympathetic / vasomotor / blood-pressure**
function to this module. *(The C1 adrenergic phenotype is a
**chemicals-side** fact — the PNMT enzyme and epinephrine synthesis
belong to the ``chemicals_hormones`` layer, not to this module. See
Design Contract: no hormone imports.)*
**Boundary status (NOT the whole ventral respiratory group — the VRG
is the COLUMN):** **Boundary case — the nucleus_retrofacialis is NOT
the whole ventral respiratory group (VRG); the VRG is the COLUMN.**
The **VRG** (``.../ventral_respiratory_group/``) **contains** the
Bötzinger complex, the pre-Bötzinger complex, the nucleus
retrofacialis, the nucleus ambiguus, the nucleus retroambiguus, and
the para-ambigual region. The **nucleus_retrofacialis** (here) is
**one sub-region** of that column — the **rostral expiratory
premotor** pool. Consumers must **not** conflate the nucleus
retrofacialis with the whole VRG.
**Boundary status (NOT a motor output — a PREMOTOR pool):**
**Boundary case — the nucleus_retrofacialis is a PREMOTOR pool, NOT
a motoneuron pool.** The **spinal expiratory motoneurons**
(**thoracic** and **abdominal** motoneurons) are the **executors** —
they **fire** the motor output. The **nucleus_retrofacialis**
(here) **drives** them — it is **bulbospinal** and **premotor**.
Consumers must **not** conflate the **premotor pool** with the
**motoneuron pools** — the **nucleus retrofacialis** **distributes**
the expiratory drive; the **spinal motoneurons** **execute** it.
**Boundary status (NOT the medulla oblongata, the VRG, or the left
nucleus retrofacialis — a leaf child of the right VRG):** **Boundary
case — the nucleus_retrofacialis is a LEAF child of the right VRG,
not the medulla oblongata, not the VRG, and not the left nucleus
retrofacialis.** Consumers must **not** conflate the nucleus
retrofacialis with the medulla oblongata, with the VRG column, or
with its left-hemisphere counterpart.
**Boundary status (NOT a single uniform population — MULTIPLE
expiratory premotor neuron classes):** **Boundary case — the
nucleus_retrofacialis is a HETEROGENEOUS premotor nucleus with
MULTIPLE neuron classes, not a single uniform population.** It
contains:
*   **Bulbospinal E2 (late-expiratory) neurons** — the **principal
    output** population, projecting to **thoracic and abdominal**
    expiratory motoneurons via the **ventrolateral funiculus**.
*   **Propriobulbar expiratory neurons** — **local-circuit**
    neurons projecting to the **nucleus retroambiguus**, the
    **pre-Bötzinger complex**, and the **Bötzinger complex** —
    the **intra-column** coordination layer.
*   **E-augmenting and E-decrementing subtypes** — distinguished by
    **firing pattern** within the expiratory phase.
**Each class is functionally distinct** — the tree wires the
**nucleus_retrofacialis** as a **single leaf**; the **neuron
classes** are **prose**, not structural children. Consumers must
**not** treat the nucleus as a single uniform population.

Overview
--------
The nucleus retrofacialis is the **rostral expiratory premotor pool**
of the **ventral respiratory group (VRG)** — the **Nissl-defined
nucleus** that **distributes** the **expiratory** drive to the
**spinal expiratory motoneurons** and to the **intra-column**
respiratory circuits. It is a **leaf** module under the **right** VRG
container.

**The nucleus retrofacialis is a PREMOTOR POOL, NOT an oscillator.**
The **oscillators** are the **Bötzinger complex** (expiratory), the
**pre-Bötzinger complex** (inspiratory), and the **pFRG** (active
expiration). The **nucleus retrofacialis** does **not** generate a
rhythm — it **relays and shapes** the expiratory drive that the
oscillators produce. This is the **most important distinction** in
the module.

**The nucleus retrofacialis is a CLASSICAL NUCLEUS, NOT a
functionally-defined region.** This is the **exact mirror** of the
pre-Bötzinger complex framing: the **pre-Bötzinger complex** is a
**functionally-defined region** that is **not** a classical nucleus;
the **nucleus retrofacialis** is a **classical Nissl-defined
nucleus** that is **not** an oscillator. The **Bötzinger complex**
sits between them — a **functionally-defined region** that
**overlaps** the retrofacial nucleus **topographically**.

**The nucleus retrofacialis is NOT the C1 group and NOT the RVLM.**
**C1 adrenergic neurons overlap** the region — this is a **real
boundary hazard**. The **nucleus retrofacialis** is the
**respiratory** population; the **C1 group** is the
**cardiovascular (sympathetic premotor)** population.

**The nucleus retrofacialis is a paired structure, and each side is
a premotor pool.** Each hemisphere has its own nucleus retrofacialis.
The two sides are **bilaterally symmetric** and carry **NO coupling
warning of their own** — the **coupling warning attaches to the
oscillators** (pre-Bötzinger complex, Bötzinger complex), **not to
the premotor pools**. See *Lateralization Notes*.

Expiratory Premotor Neuron Classes (prose, not structural children)
-------------------------------------------------------------------
The nucleus retrofacialis is a **heterogeneous premotor nucleus** —
documented as **prose**, not as structural children:

*   **Bulbospinal E2 (late-expiratory) neurons** — the **principal
    output** population; project to **thoracic and abdominal**
    expiratory motoneurons via the **ventrolateral funiculus**;
    **bulbospinal**, **premotor**.

*   **Propriobulbar expiratory neurons** — **local-circuit**
    neurons projecting to the **nucleus retroambiguus**, the
    **pre-Bötzinger complex**, and the **Bötzinger complex** — the
    **intra-column coordination layer**.

*   **E-augmenting and E-decrementing subtypes** — distinguished by
    **firing pattern** within the expiratory phase; **prose**, not
    modules.

**These neuron classes are prose, not structural children.** The
tree wires the **nucleus_retrofacialis** as a **single leaf** under
the right VRG. Consumers that need **neuron-class-level** resolution
should consult the references, not the tree.

The Nucleus Retrofacialis / Bötzinger Complex Boundary
------------------------------------------------------
This is the **most consequential sibling** boundary, and it is
**contested in the literature** — **classical nucleus vs.
functional oscillator**, with **topographic overlap**:

*   **Nucleus_retrofacialis** (this module) — the **Nissl-defined
    nucleus** — the **cytoarchitectonic** structure.

*   **Bötzinger complex** (``.../right/botzinger_complex/``) — the
    **functionally-defined expiratory oscillator** — the
    **functional microcircuit**.

**They OVERLAP topographically** — the Bötzinger complex is often
defined as the region **containing** the retrofacial nucleus. **This
tree wires them as DISTINCT SIBLINGS** because the tree separates
**function from cytoarchitecture**: the **Bötzinger complex** is
defined by **oscillation**; the **nucleus retrofacialis** is defined
by **Nissl borders**. **Consumers must not conflate the two, and
must not assume they are mutually exclusive** — they **overlap**.
This is **the exact mirror** of the pre-Bötzinger complex framing
(a **functionally-defined region** that is **not** a classical
nucleus).

The Nucleus Retrofacialis / Pre-Bötzinger Complex Boundary
----------------------------------------------------------
This is the **expiratory vs. inspiratory** boundary:

*   **Nucleus_retrofacialis** (this module) — the **rostral
    expiratory premotor pool**.

*   **Pre-Bötzinger complex** (``.../right/pre_botzinger_complex/``)
    — the **inspiratory rhythm kernel**.

**They are on OPPOSITE PHASES of the respiratory cycle.** The
**pre-Bötzinger complex** is the **inspiratory** oscillator; the
**nucleus retrofacialis** is the **expiratory** premotor pool.
Consumers must **not** conflate the two.

The Nucleus Retrofacialis / Nucleus Ambiguus Boundary
-----------------------------------------------------
This is the **branchiomotor vs. respiratory premotor** boundary:

*   **Nucleus_retrofacialis** (this module) — the **expiratory
    premotor** pool.

*   **Nucleus ambiguus** (``.../medulla_oblongata/nucleus_ambiguus/``,
    wired elsewhere) — the **branchiomotor** pool (vagal,
    glossopharyngeal, laryngeal, pharyngeal, cardiac).

**The nucleus ambiguus is a MOTONEURON pool; the nucleus
retrofacialis is a PREMOTOR pool.** Consumers must **not** conflate
the two.

The Nucleus Retrofacialis / Nucleus Retroambiguus Boundary
----------------------------------------------------------
This is the **rostral vs. caudal expiratory premotor** boundary:

*   **Nucleus_retrofacialis** (this module) — the **rostral**
    expiratory premotor pool.

*   **Nucleus retroambiguus** (wired elsewhere, **caudal** VRG) —
    the **caudal** expiratory premotor pool; the **premotor
    substrate** of **cough and sneeze**.

**They are ROSTRAL vs. CAUDAL siblings of the same column — both
expiratory premotor, but DIFFERENT STRUCTURES.** Consumers must
**not** conflate the two.

The Nucleus Retrofacialis / Parafacial Respiratory Group Boundary
-----------------------------------------------------------------
This is the **premotor pool vs. active-expiration oscillator**
boundary:

*   **Nucleus_retrofacialis** (this module) — the **expiratory
    premotor** pool.

*   **Parafacial respiratory group (pFRG)** (wired elsewhere) — the
    **active-expiration oscillator**.

**The pFRG GENERATES active expiration; the nucleus retrofacialis
RELAYS expiratory drive.** Consumers must **not** conflate the two —
the **pFRG** is an **oscillator**; the **nucleus retrofacialis** is
a **premotor pool**.

The Nucleus Retrofacialis / Facial Nucleus Boundary
---------------------------------------------------
This is the **branchiomotor neighbor** boundary:

*   **Nucleus_retrofacialis** (this module) — the **expiratory
    premotor** pool.

*   **Facial nucleus** (nucleus VII)
    (``.../metencephalon/pons/facial_nucleus/``, wired elsewhere) —
    the **branchiomotor** nucleus for the **facial musculature**.

**"Retrofacial" means CAUDAL TO THE FACIAL NUCLEUS.** The facial
nucleus is the **rostral neighbor** — **not the parent**. Consumers
must **not** conflate the two, and must **not** resolve the nucleus
retrofacialis as a child of the facial nucleus — it is a **VRG**
child.

The Nucleus Retrofacialis / C1 Group and RVLM Boundary
------------------------------------------------------
This is the **respiratory vs. cardiovascular** boundary, and it is a
**real topographic overlap**:

*   **Nucleus_retrofacialis** (this module) — the **respiratory
    (expiratory premotor)** population.

*   **C1 adrenergic group / RVLM** (wired elsewhere) — the
    **sympathetic premotor** population (PNMT-expressing,
    adrenergic).

**C1 neurons OVERLAP the region of the nucleus retrofacialis.** They
are **DIFFERENT FUNCTIONAL POPULATIONS** that **share a
neighborhood**. Consumers must **not** conflate the two, and must
**not** attribute **sympathetic / vasomotor / blood-pressure**
function to this module. *(The C1 **adrenergic phenotype** is a
``chemicals_hormones``-layer fact — see Design Contract: no hormone
imports.)*

The Nucleus Retrofacialis / Spinal Expiratory Motoneurons Boundary
------------------------------------------------------------------
This is the **premotor vs. motoneuron** boundary:

*   **Nucleus_retrofacialis** (this module) — the **premotor** pool.

*   **Thoracic and abdominal expiratory motoneurons** (spinal cord)
    — the **executors**.

**The nucleus retrofacialis DRIVES the motoneurons; the motoneurons
EXECUTE the motor output.** Consumers must **not** conflate the
**premotor pool** with the **motoneuron pools**.

Function in the Human Brain
---------------------------
The nucleus retrofacialis's functions are **expiratory premotor
drive** and **intra-column coordination** — **NOT rhythm generation**
and **NOT motor output**:

*   **Expiratory Premotor Output (bulbospinal E2 neurons):** The
    nucleus retrofacialis **distributes** the **expiratory** drive
    to the **thoracic and abdominal** expiratory motoneurons via
    the **ventrolateral funiculus**. This is the **premotor
    substrate** of **active expiration** — the **forced** expiratory
    phase of **exercise**, **speech**, **cough**, and **sneeze**.

*   **Intra-Column Coordination (propriobulbar neurons):** The
    nucleus retrofacialis **coordinates** the **Bötzinger complex**,
    the **pre-Bötzinger complex**, and the **nucleus
    retroambiguus** — the **propriobulbar** neurons **shape** the
    expiratory pattern within the VRG column.

*   **Pattern Shaping (not generation):** The nucleus retrofacialis
    **shapes** the **expiratory pattern** — the **E-augmenting** and
    **E-decrementing** subtypes **shape** the **firing profile**
    within the expiratory phase. The **rhythm** is generated
    **upstream** (the **Bötzinger complex**, the **pFRG**); the
    nucleus retrofacialis **shapes** it.

*   **Airway Defense (with the nucleus retroambiguus):** The
    **rostral** expiratory premotor pool **contributes** to
    **airway defense** — **cough** and **sneeze** — via the
    **intra-column** and **spinal** projections. This is
    **distributed** with the **nucleus retroambiguus**, and it is
    **contested** in its **rostral/caudal** division of labor.

*   **NOT an oscillator.** The **oscillators** are the **Bötzinger
    complex** (expiratory), the **pre-Bötzinger complex**
    (inspiratory), and the **pFRG** (active expiration). The
    nucleus retrofacialis **relays** — it does **not** generate.

*   **NOT the C1 group.** The nucleus retrofacialis is the
    **respiratory** population; the **C1 group** is the
    **cardiovascular (sympathetic premotor)** population. They
    **overlap topographically** but are **functionally distinct**.

*   **NOT a motoneuron pool.** The **spinal expiratory motoneurons**
    **execute** the motor output. The nucleus retrofacialis
    **drives** them.

**The unifying theme:** the nucleus retrofacialis is the **rostral
expiratory premotor pool** of the **ventral respiratory group** —
the **classical Nissl-defined nucleus** that **distributes** the
expiratory drive. It is a **premotor pool**, **NOT** an oscillator
(**Bötzinger complex**, **pFRG**), **NOT** the cardiovascular **C1
group**, and **NOT** a motoneuron pool (**spinal expiratory
motoneurons**).

Associated Disorders
--------------------
The nucleus retrofacialis has **no named clinical syndrome of its
own** — its clinical associations are **indirect**, via the
expiratory premotor drive it distributes:

*   **Impaired Airway Defense (via the expiratory premotor output):**
    The **expiratory premotor** drive **contributes** to **cough**
    and **sneeze** — its **impairment** (in **stroke**,
    **neurodegeneration**, or **aging**) is **associated** with
    **impaired airway clearance** and **aspiration risk**. This is
    **indirect** and **distributed** with the **nucleus
    retroambiguus**.

*   **Central Sleep Apnea / Expiratory Failure (indirect):** The
    nucleus retrofacialis **distributes** the expiratory drive —
    its **dysfunction** **contributes** to **expiratory** timing
    **abnormalities**, but the **rhythm** abnormality originates
    **upstream** (**pre-Bötzinger complex**, **RTN**). This is
    **indirect**.

*   **No Named "Nucleus Retrofacialis Syndrome":** The nucleus
    retrofacialis is a **premotor pool**, not a **rhythm
    generator** — it has **no named clinical syndrome**. Its
    clinical relevance is **indirect**, via the **expiratory
    premotor** drive it distributes.

**What is NOT here:** The nucleus retrofacialis is **not** the
substrate for **OIRD** (pre-Bötzinger complex — NK1R neurons),
**CCHS / Ondine's curse** (RTN — PHOX2B chemoreceptor), **Rett
syndrome** (pre-Bötzinger complex), **SIDS** (proposed —
pre-Bötzinger complex + arcuate nucleus), **Wallenberg syndrome**
(lateral medulla — nucleus ambiguus, spinothalamic tract),
**essential hypertension / sympathetic overactivity** (**C1 group /
RVLM** — **NOT this module**), or **Kluver-Bucy syndrome**
(amygdala). Its clinical relevance is **indirect**, via the
**expiratory premotor** drive it distributes. **No named nucleus
retrofacialis syndrome exists.**

Lateralization Notes
--------------------
This is the **right** nucleus_retrofacialis module. The
nucleus_retrofacialis is **bilaterally symmetric** and carries **NO
coupling warning of its own** — and it **inherits no warning from
the oscillators**:

*   **Bilateral Premotor Pools:** Each hemisphere has its own
    nucleus retrofacialis — each is a **premotor pool** driving
    **its own** (predominantly **ipsilateral**) spinal expiratory
    motoneurons.

*   **NO Coupling Warning (the coupling warning attaches to the
    OSCILLATORS, not to the PREMOTOR POOLS):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose **two sides must synchronize** to produce a
    **single coherent rhythm**. The **nucleus retrofacialis** is a
    **premotor pool** — it does **not** generate the rhythm, so it
    does **not** carry the **oscillator coupling warning**. Its
    **right** and **left** sides are **coordinated downstream** (at
    the **pattern** level, via the oscillators and the
    **propriobulbar** network), **not** by direct **RFN–RFN**
    coupling. **This is a general rule the tree can propagate:**
    **coupling warnings attach to oscillators, not to premotor
    pools.**

*   **NO SLEA Warning:** The nucleus retrofacialis is **SLEA-free**
    — it is **not** an extended-amygdala component.

*   **NO Amygdala-Lateralization Warning:** The nucleus
    retrofacialis is **not** part of the amygdala — it does **not**
    inherit the amygdala-lateralization warning.

*   **NO Rhinencephalon-Exclusion Flag:** The nucleus retrofacialis
    is **not** a rhinencephalon structure — it carries **no**
    rhinencephalon-exclusion flag.

**A consumer that assumes "right nucleus_retrofacialis = left
nucleus_retrofacialis" will be structurally correct** — the two
sides are **symmetric** and **functionally independent as premotor
pools** (each drives its own motoneurons). The nucleus
retrofacialis is a **strict-mirror pair with NO warning** — **no
coupling warning**, **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../botzinger_complex/``, ``.../pre_botzinger_complex/``,
    ``.../nucleus_ambiguus/``, ``.../nucleus_retroambiguus/``, the
    **pons**, the **spinal cord**, the **C1 group / RVLM**, or any
    other container. The nucleus retrofacialis's relationships to
    the Bötzinger complex, the pre-Bötzinger complex, the nucleus
    ambiguus, the nucleus retroambiguus, the pFRG, the facial
    nucleus, the C1 group, and the spinal expiratory motoneurons are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. **The C1
    adrenergic phenotype (PNMT, epinephrine synthesis) is a
    ``chemicals_hormones``-layer fact** — it is documented as
    **prose**, never imported.
*   **Leaf module — no structural children.** The **bulbospinal E2**,
    **propriobulbar**, and **E-augmenting / E-decrementing** neuron
    classes are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    **neuron-class-level** detail through the references.
*   **PREMOTOR POOL — NOT an oscillator.** The **oscillators** are
    the **Bötzinger complex** (expiratory), the **pre-Bötzinger
    complex** (inspiratory), and the **pFRG** (active expiration).
    The nucleus retrofacialis **relays and shapes** — it does
    **not** generate. Consumers must **not** attribute rhythm
    generation to this module.
*   **CLASSICAL NUCLEUS — NOT a functionally-defined region.** The
    nucleus retrofacialis is **Nissl-defined**. This is the **exact
    mirror** of the pre-Bötzinger complex framing. Consumers must
    **not** treat it as a **functionally-defined oscillator**.
*   **OVERLAPS the Bötzinger complex — the two are DIFFERENT KINDS
    of structure.** The **Bötzinger complex** is a
    **functionally-defined region**; the **nucleus retrofacialis**
    is a **Nissl-defined nucleus**. They **overlap
    topographically** — consumers must **not** assume they are
    mutually exclusive, and must **not** collapse one into the
    other.
*   **NOT the pre-Bötzinger complex — that is the INSPIRATORY
    oscillator.** Opposite phase of the respiratory cycle.
*   **NOT the nucleus ambiguus — that is the BRANCHIOMOTOR pool.**
*   **NOT the nucleus retroambiguus — that is the CAUDAL expiratory
    premotor pool.** Rostral vs. caudal siblings.
*   **NOT the pFRG — that is the ACTIVE-EXPIRATION oscillator.**
*   **NOT the facial nucleus — that is the BRANCHIOMOTOR neighbor.**
    "Retrofacial" = **caudal to** the facial nucleus, **not a child
    of** it.
*   **NOT the C1 group / RVLM — that is the SYMPATHETIC PREMOTOR
    population.** **C1 overlaps topographically** — a **real
    boundary hazard**. Consumers must **not** attribute
    **sympathetic / vasomotor / blood-pressure** function to this
    module.
*   **NOT a motoneuron pool — a PREMOTOR pool.** The **spinal
    expiratory motoneurons** are the **executors**.
*   **NOT a single uniform population — MULTIPLE expiratory premotor
    neuron classes.** The **bulbospinal E2**, **propriobulbar**, and
    **E-augmenting / E-decrementing** classes are **prose**, not
    structural children.
*   **NO coupling warning — the coupling warning attaches to the
    OSCILLATORS, not to the PREMOTOR POOLS.** The nucleus
    retrofacialis is a **strict mirror with NO warning**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop.** The nucleus_retrofacialis is a local
    leaf under the right VRG, not a cross-listed leaf.
*   **No nested cross-listing.** The nucleus_retrofacialis has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left nucleus_retrofacialis — strict
    mirror with NO warning.** Right and left nucleus retrofacialis
    modules are **structurally identical** — same leaf status, same
    **premotor-pool** framing, same **classical-nucleus** framing,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right import nucleus_retrofacialis

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "ventral_respiratory_group.right.nucleus_retrofacialis"
    )

**Do not** assume the nucleus_retrofacialis is the **Bötzinger
complex**. The **Bötzinger complex** is the **functionally-defined
expiratory oscillator**; the **nucleus_retrofacialis** is the
**Nissl-defined nucleus** that **overlaps** it. They are
**different kinds of structure**.

**Do not** assume the nucleus_retrofacialis is an **oscillator**.
It is a **premotor pool**. The oscillators are the **Bötzinger
complex**, the **pre-Bötzinger complex**, and the **pFRG**.

**Do not** assume the nucleus_retrofacialis is the **pre-Bötzinger
complex**. The **pre-Bötzinger complex** is the **inspiratory**
oscillator; the **nucleus_retrofacialis** is the **expiratory**
premotor pool.

**Do not** assume the nucleus_retrofacialis is the **nucleus
ambiguus** or the **nucleus retroambiguus**. The **nucleus
ambiguus** is the **branchiomotor** pool; the **nucleus
retroambiguus** is the **caudal** expiratory premotor pool. The
nucleus retrofacialis is the **rostral** expiratory premotor pool.

**Do not** assume the nucleus_retrofacialis is the **facial
nucleus**. "Retrofacial" means **caudal to** the facial nucleus.

**Do not** assume the nucleus_retrofacialis is the **C1 group /
RVLM**. **C1 neurons overlap the region** — they are the
**sympathetic premotor** population. The nucleus retrofacialis is
the **respiratory (expiratory premotor)** population.

**Do not** import the **oscillator coupling warning** into the
nucleus_retrofacialis. **The nucleus_retrofacialis is a PREMOTOR
POOL** — it carries **NO coupling warning**.

Iterating the nucleus_retrofacialis's (empty) children (recommended
consumer pattern)::

    NUCLEUS_RETROFACIALIS_CHILDREN = ()
    # The nucleus_retrofacialis is a leaf. The bulbospinal E2,
    # propriobulbar, and E-augmenting / E-decrementing neuron
    # classes are prose, not modules.

Reaching the Bötzinger complex (recommended consumer pattern — the
overlapping functional oscillator)::

    # The Bötzinger complex is the FUNCTIONALLY-DEFINED expiratory
    # oscillator that OVERLAPS the nucleus retrofacialis
    # topographically:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   ventral_respiratory_group.right.botzinger_complex
    #
    # The nucleus retrofacialis is the NISSL-DEFINED nucleus; the
    # Bötzinger complex is the FUNCTIONALLY-DEFINED oscillator.
    # They OVERLAP — they are not mutually exclusive.

Reaching the pre-Bötzinger complex (recommended consumer pattern —
the inspiratory oscillator, opposite phase)::

    # The pre-Bötzinger complex is the INSPIRATORY oscillator — the
    # nucleus retrofacialis is on the EXPIRATORY phase:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   ventral_respiratory_group.right.pre_botzinger_complex
    #
    # The pre-Bötzinger complex GENERATES the inspiratory rhythm;
    # the nucleus retrofacialis DISTRIBUTES the expiratory drive.

Reaching the nucleus ambiguus (recommended consumer pattern — the
branchiomotor pool)::

    # The nucleus ambiguus is the BRANCHIOMOTOR pool (vagal,
    # laryngeal, pharyngeal, cardiac motoneurons):
    #
    #   hindbrain.myelencephalon.medulla_oblongata.nucleus_ambiguus
    #
    # The nucleus ambiguus is a MOTONEURON pool; the nucleus
    # retrofacialis is a PREMOTOR pool.

Reaching the nucleus retroambiguus (recommended consumer pattern —
the caudal expiratory premotor pool)::

    # The nucleus retroambiguus is the CAUDAL expiratory premotor
    # pool — the premotor substrate of cough and sneeze:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   ventral_respiratory_group.nucleus_retroambiguus
    #
    # The nucleus retroambiguus is CAUDAL; the nucleus
    # retrofacialis is ROSTRAL. Both are expiratory premotor.

Reaching the parafacial respiratory group (recommended consumer
pattern — the active-expiration oscillator)::

    # The parafacial respiratory group (pFRG) is the
    # ACTIVE-EXPIRATION oscillator:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   parafacial_respiratory_group
    #
    # The pFRG GENERATES active expiration; the nucleus
    # retrofacialis RELAYS expiratory drive.

Reaching the facial nucleus (recommended consumer pattern — NOTE
the "retrofacial" naming)::

    # The facial nucleus (nucleus VII) is the BRANCHIOMOTOR nucleus
    # for the facial musculature — the ROSTRAL NEIGHBOR that gives
    # the retrofacial nucleus its name:
    #
    #   hindbrain.metencephalon.pons.facial_nucleus
    #
    # "Retrofacial" means CAUDAL TO the facial nucleus — the facial
    # nucleus is NOT the parent.

Reaching the C1 group / RVLM (recommended consumer pattern — NOTE
the topographic overlap)::

    # The C1 adrenergic group of the rostral ventrolateral medulla
    # (RVLM) is the SYMPATHETIC PREMOTOR population. C1 neurons
    # OVERLAP the region of the nucleus retrofacialis:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   rostral_ventrolateral_medulla.c1_group
    #
    # The C1 group is CARDIOVASCULAR; the nucleus retrofacialis is
    # RESPIRATORY. They OVERLAP topographically but are
    # functionally distinct. Do not attribute sympathetic /
    # vasomotor / blood-pressure function to the nucleus
    # retrofacialis.

Reaching the spinal expiratory motoneurons (recommended consumer
pattern — the executors)::

    # The thoracic and abdominal expiratory motoneurons (spinal
    # cord) are the EXECUTORS — the nucleus retrofacialis drives
    # them via the ventrolateral funiculus:
    #
    #   spinal_cord.thoracic.intermediate_zone.expiratory_motoneurons
    #
    # The nucleus retrofacialis is PREMOTOR; the spinal motoneurons
    # are MOTOR.

Bilateral iteration (recommended consumer pattern — NOTE the
premotor-pool rule)::

    for side in ("left", "right"):
        rfn_path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"ventral_respiratory_group.{side}."
            f"nucleus_retrofacialis"
        )
        # resolve rfn_path through the memory/recall layer
        #
        # NOTE: the two sides are PREMOTOR POOLS — each drives its
        # own motoneurons. There is NO coupling warning here. The
        # coupling warning attaches to the OSCILLATORS (pre-Bötzinger
        # complex, Bötzinger complex), not to the premotor pools.

Neuron-class-level detail (not wired — consult references)::

    # The nucleus retrofacialis's neuron classes are prose, not
    # modules:
    #   bulbospinal E2 neurons   -> principal output; thoracic and
    #                               abdominal expiratory motoneurons
    #   propriobulbar neurons    -> intra-column coordination
    #   E-augmenting / E-decrementing -> firing-profile shaping
    #
    # Do not attempt to resolve these as sub-paths of the
    # nucleus_retrofacialis.

References
----------
*   **Canonical cytoarchitectonic mapping of the VRG:** Ellenberger,
    H.H., Feldman, J.L. (1990). "Subnuclear organization of the
    lateral tegmental field of the rat. I: Nucleus ambiguus and
    ventral respiratory group." *Journal of Comparative Neurology*
    294:202–211. (The definitive cytoarchitectonic mapping of the
    VRG subdivisions, including the retrofacial nucleus.)
*   **Canonical lateral respiratory neuron mapping:** Merrill, E.G.
    (1970). "The lateral respiratory neurones of the medulla: their
    associations with nucleus ambiguus, nucleus retroambigualis, the
    spinal accessory nucleus and the spinal cord." *Brain Research*
    24:11–28. (The original mapping of lateral respiratory neurons,
    including the rostral expiratory premotor population.)
*   **Bötzinger complex and retrofacial nucleus:** Otake, K.,
    Sasaki, H., Ezure, K., Manabe, M. (1988). "Axonal projections
    from Bötzinger expiratory neurons to contralateral ventral and
    dorsal respiratory groups in the cat." *Experimental Brain
    Research* 72:83–93. (The Bötzinger complex and its overlap with
    the retrofacial region.)
*   **Expiratory neuron classes:** Ezure, K. (1990). "Synaptic
    connections between medullary respiratory neurons and
    considerations on the genesis of respiratory rhythm." *Progress
    in Neurobiology* 35:429–450. (Definitive review of medullary
    respiratory neuron classes — E-augmenting, E-decrementing,
    bulbospinal, propriobulbar.)
*   **Decrementing expiratory neurons:** Ezure, K., Manabe, M.
    (1988). "Decrementing expiratory neurons of the Bötzinger
    complex. II. Direct inhibitory input to the medullary
    respiratory neurons." *Experimental Brain Research* 72:159–166.
    (Decrementing expiratory neurons in the Bötzinger / retrofacial
    region.)
*   **Bilateral coupling and microcircuits:** Smith, J.C., Abdala,
    A.P.L., Borgmann, A., Rybak, I.A., Paton, J.F.R. (2013).
    "Brainstem respiratory networks: building blocks and
    microcircuits." *Trends in Neurosciences* 36:152–162. (The VRG
    microcircuit — the **oscillator** vs. **premotor pool**
    distinction.)
*   **Three-oscillator architecture:** Smith, J.C., Abdala, A.P.L.,
    Koizumi, H., Rybak, I.A., Paton, J.F.R. (2007). "Spatial and
    functional architecture of the mammalian brainstem respiratory
    network: a hierarchy of three oscillatory mechanisms."
    *Journal of Neurophysiology* 98:3370–3387. (The Bötzinger
    complex, pre-Bötzinger complex, and pFRG as the three
    oscillators — contrast with the retrofacial **premotor pool**.)
*   **Pre-Bötzinger complex (contrast — the inspiratory
    oscillator):** Feldman, J.L., Del Negro, C.A. (2006). "Looking
    for inspiration: new perspectives on respiratory rhythm."
    *Nature Reviews Neuroscience* 7:232–242. (The pre-Bötzinger
    complex as the inspiratory rhythm kernel — contrast with the
    retrofacial expiratory premotor pool.)
*   **Nucleus retroambiguus (contrast — the caudal expiratory
    premotor pool):** Bautista, T.G., Sun, Q.-J., Pilowsky, P.M.
    (2012). "The generation of phrenic and sympathetic respiratory
    activities." *Respiratory Physiology & Neurobiology* 184:1–12.
    (The motor and premotor pools — contrast with the rostral
    retrofacial pool.)
*   **Cough and sneeze (contrast — distributed with the nucleus
    retroambiguus):** Bolser, D.C., Davenport, P.W. (2002).
    "Functional organization of the central cough generation
    mechanism." *Pulmonary Pharmacology & Therapeutics* 15:221–225.
    (The central cough generation mechanism — distributed across
    the rostral and caudal expiratory premotor pools.)
*   **C1 group and RVLM (contrast — the sympathetic premotor
    population, topographically overlapping):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure." *Nature
    Reviews Neuroscience* 7:335–346. (The C1 adrenergic group and
    the RVLM as the sympathetic premotor population — contrast with
    the respiratory nucleus retrofacialis.)
*   **Pontine respiratory group (contrast — the pontine modulator):**
    Dutschmann, M., Dick, T.E. (2012). "Pontine mechanisms of
    respiratory control." *Comprehensive Physiology* 2:2443–2469.
    (The pontine respiratory group as the pontine modulator —
    contrast with the medullary premotor pools.)
*   **SLEA (contrast — the nucleus retrofacialis is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the nucleus retrofacialis.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary respiratory groups in overview.)
*   Paxinos, G., Franklin, K.B.J. (2019). *Paxinos and Franklin's
    the Mouse Brain in Stereotaxic Coordinates*, 5th ed.
    (Cytoarchitectonic atlas placement of the retrofacial nucleus.)
*   NeuroNames — Nucleus retrofacialis (right); FMA — Retrofacial
    nucleus (right member).
"""