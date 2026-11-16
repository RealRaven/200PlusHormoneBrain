"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left.retrotrapezoid_nucleus
=========================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── ventral_respiratory_group
                └── left
                    └── retrotrapezoid_nucleus   <-- THIS MODULE

**Primary synonym:** Retrotrapezoid nucleus (left); RTN; retrotrapezoid
nucleus / parafacial region; the ventral medullary CO2 chemoreceptor;
the central respiratory chemoreceptor.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). **Not a classical Nissl-defined nucleus** — the RTN is a
**molecularly and developmentally defined population**: **VGlut2+,
Phox2b+, NK1R+, TH-negative, non-aminergic, non-cholinergic,
non-serotonergic, non-GABAergic** glutamatergic neurons[reference:0].
Its borders are defined by **transcription-factor expression
(Phox2b) and lineage (Egr2, Lbx1, Atoh1)**, not by a sharp Nissl
border[reference:1]. This is the **same class of structure** as the
pre-Bötzinger complex (**functionally/molecularly defined, not
cytoarchitectonic**) — and the **opposite** of the nucleus
retrofacialis (**classically Nissl-defined**).
**Part of:** The **ventral respiratory group (VRG)** container —
specifically, the **left** side, **rostral** division. The **VRG** is
the **ventrolateral medullary respiratory column** — the **Bötzinger
complex**, the **pre-Bötzinger complex**, the **nucleus
retrofacialis**, the **retrotrapezoid nucleus**, the **nucleus
ambiguus**, the **nucleus retroambiguus**, and the **para-ambigual**
region.
**Structural parent:** ``.../ventral_respiratory_group/left/`` →
**direct child** of the left VRG container.
**Structural children:** **None.** This is a **leaf** module. The
**molecularly defined RTN subpopulations** and the **parafacial
expiratory oscillator** are documented as **prose**, not as structural
children.
**Boundary status (NOT the parafacial respiratory group — the pFRG is
the ACTIVE-EXPIRATION OSCILLATOR):** **Boundary case — the
retrotrapezoid_nucleus is NOT the parafacial respiratory group
(pFRG).** This is the **most consequential sibling boundary** in the
module, and it is **contested and overlapping in the literature**:
the **pFRG** is often described as **overlapping the RTN**, and the
compound term **"RTN/pFRG"** is used in the field[reference:2][reference:3].
The **RTN** (here) is the **chemoreceptor population** — the
**Phox2b⁺/TH⁻** neurons that **sense CO2/H+** and **drive** the
respiratory pattern generator. The **pFRG** (wired elsewhere) is the
**expiratory oscillator** — the **late-expiratory (late-E)**
population that **generates** **active expiration**.
**They are DIFFERENT FUNCTIONAL POPULATIONS that OVERLAP
topographically** — the **major pFRG population is lateral to the
RTN**, and the **medial pFRG may overlap the RTN**[reference:5].
Consumers must **not** conflate the two, and must **not** assume
they are mutually exclusive — they **overlap**. **The RTN is the
CHEMORECEPTOR; the pFRG is the OSCILLATOR.**
**Boundary status (NOT the pre-Bötzinger complex — the pre-Bötzinger
complex is the INSPIRATORY RHYTHM GENERATOR):** **Boundary case — the
retrotrapezoid_nucleus is NOT the pre-Bötzinger complex.** The
**pre-Bötzinger complex** (``.../left/pre_botzinger_complex/``) is
the **inspiratory rhythm kernel** — it **generates** the
inspiratory rhythm. The **retrotrapezoid_nucleus** (here) is the
**chemoreceptor** — it **senses** CO2/H+ and **sends excitatory
glutamatergic drive** to the pre-Bötzinger complex and the Bötzinger
complex[reference:6]. **The RTN is UPSTREAM of the pre-Bötzinger
complex** in the respiratory control hierarchy — the RTN **modulates**
the rhythm; the pre-Bötzinger complex **generates** it. Consumers must
**not** conflate the two — the **pre-Bötzinger complex** is the
**oscillator**; the **RTN** is the **sensor / driver**.
**Boundary status (NOT the Bötzinger complex — the Bötzinger complex
is the EXPIRATORY OSCILLATOR):** **Boundary case — the
retrotrapezoid_nucleus is NOT the Bötzinger complex.** The
**Bötzinger complex** (``.../left/botzinger_complex/``) is the
**expiratory oscillator** — it **generates** the expiratory rhythm.
The **retrotrapezoid_nucleus** (here) **sends excitatory drive** to
the Bötzinger complex — it does **not** generate the expiratory
rhythm. **The RTN is UPSTREAM of the Bötzinger complex.** Consumers
must **not** conflate the two — the **Bötzinger complex** is the
**oscillator**; the **RTN** is the **sensor / driver**.
**Boundary status (NOT the C1 adrenergic group / RVLM — the C1 group
is the SYMPATHETIC PREMOTOR population):** **Boundary case — the
retrotrapezoid_nucleus is NOT the C1 adrenergic group and NOT the
rostral ventrolateral medulla (RVLM) cardiovascular premotor
population.** The **C1 group** — **TH-positive, PNMT-expressing,
adrenergic** neurons of the RVLM — is the **sympathetic premotor**
population. **C1 neurons PARTIALLY OVERLAP the RTN and extend
caudally from it**[reference:7][reference:8]. The **RTN** (here) is
**TH-negative, non-aminergic, Phox2b⁺** — the **respiratory
chemoreceptor** population. **They are DIFFERENT FUNCTIONAL
POPULATIONS that OVERLAP topographically** — this is a **real,
documented boundary hazard**. Consumers must **not** conflate the
two, and must **not** attribute **sympathetic / vasomotor /
blood-pressure** function to this module. *(The C1 adrenergic
phenotype is a ``chemicals_hormones``-layer fact — the TH and PNMT
enzymes and catecholamine synthesis belong to that layer. See Design
Contract: no hormone imports.)*
**Boundary status (NOT the facial nucleus — the facial nucleus is the
BRANCHIOMOTOR neighbor):** **Boundary case — the
retrotrapezoid_nucleus is NOT the facial nucleus (nucleus VII).** The
**facial nucleus** (``.../metencephalon/pons/facial_nucleus/``,
wired elsewhere) is the **branchiomotor** nucleus for the **facial
musculature**. The **RTN is located VENTRAL and MEDIAL to the facial
motor nucleus**[reference:9][reference:10] — the facial nucleus is the
**topographic landmark**, **not the parent**. The RTN is a **VRG**
child. Consumers must **not** conflate the two, and must **not**
resolve the RTN as a child of the facial nucleus.
**Boundary status (NOT a classical Nissl nucleus — a MOLECULARLY
DEFINED population):** **Boundary case — the retrotrapezoid_nucleus
is NOT a classical Nissl-defined nucleus.** It is defined by
**transcription-factor expression (Phox2b)**, **lineage (Egr2, Lbx1,
Atoh1)**, and **neurotransmitter phenotype (VGlut2, NK1R, TH⁻)** —
not by a sharp cytoarchitectonic border[reference:11][reference:12].
Consumers must **not** treat it as a **sharply-bounded Nissl nucleus**
— it is a **molecularly defined population**.
**Boundary status (NOT an oscillator — a CHEMORECEPTOR / DRIVE
NUCLEUS):** **Boundary case — the retrotrapezoid_nucleus is NOT an
oscillator.** The **oscillators** are the **pre-Bötzinger complex**
(inspiratory), the **Bötzinger complex** (expiratory), and the
**pFRG** (active expiration). The **RTN** **senses** CO2/H+ and
**drives** the oscillators — it does **not** generate a rhythm
intrinsically[reference:13]. Consumers must **not** attribute rhythm
generation to this module.
**Boundary status (NOT a motoneuron or premotor pool — a SENSOR /
DRIVER):** **Boundary case — the retrotrapezoid_nucleus is NOT a
motoneuron pool and NOT a premotor pool.** The **motoneuron pools**
(phrenic, intercostal, hypoglossal) **execute** the motor output; the
**premotor pools** (nucleus retroambiguus, nucleus retrofacialis)
**distribute** it. The **RTN** **senses and drives** — it is
**upstream** of both. Consumers must **not** conflate the RTN with a
motoneuron or premotor pool.
**Boundary status (NOT the whole VRG — a SUB-REGION):** **Boundary
case — the retrotrapezoid_nucleus is NOT the whole ventral
respiratory group (VRG); the VRG is the COLUMN.** The **VRG**
**contains** the Bötzinger complex, the pre-Bötzinger complex, the
nucleus retrofacialis, the RTN, the nucleus ambiguus, the nucleus
retroambiguus, and the para-ambigual region. The **RTN** is **one
sub-region** of that column — the **chemoreceptor kernel**.
Consumers must **not** conflate the RTN with the whole VRG.
**Boundary status (NOT the right retrotrapezoid nucleus — a leaf child
of the left VRG):** **Boundary case — the retrotrapezoid_nucleus is a
LEAF child of the left VRG, not the right retrotrapezoid nucleus.**
Consumers must **not** conflate the left RTN with its right-hemisphere
counterpart.
**Boundary status (NOT a single uniform population — MULTIPLE RTN
subpopulations and a heterogeneous phenotype):** **Boundary case —
the retrotrapezoid_nucleus is a HETEROGENEOUS molecularly defined
population, not a single uniform neuron type.** It contains:
*   **Phox2b⁺/VGlut2⁺/NK1R⁺/TH⁻ chemoreceptor neurons** — the
    **core RTN population**, intrinsically pH-sensitive (TASK-2,
    GPR4)[reference:14].
*   **Atoh1-lineage subpopulation** — developmentally distinct,
    required for **normal chemoresponsiveness** and **postnatal
    breathing**[reference:15].
*   **Putative subpopulations with different connectomes** — the RTN
    is **phenotypically heterogeneous** and may contain neurons with
    **different projection targets and functions**[reference:16].
**Each subpopulation is functionally distinct** — the tree wires the
**retrotrapezoid_nucleus** as a **single leaf**; the
**subpopulations** are **prose**, not structural children. Consumers
must **not** treat the RTN as a single uniform population.
**Boundary status (NO coupling warning — the coupling warning attaches
to the OSCILLATORS, not to the SENSOR / DRIVER):** **Boundary case —
the retrotrapezoid_nucleus carries NO coupling warning of its own.**
The **pre-Bötzinger complex** carries a **coupling warning** because
it is an **oscillator** whose two sides must synchronize to produce a
single rhythm. The **RTN** is a **sensor / driver** — it does **not**
generate the rhythm, so it does **not** carry the **oscillator
coupling warning**. Its left and right sides are **bilaterally
symmetric chemoreceptor clusters** whose outputs are **coordinated
downstream** (at the pattern level, via the oscillators), **not** by
direct **RTN–RTN** coupling. **This extends the propagatable rule:**
**coupling warnings attach to oscillators — not to premotor pools, and
not to sensory / chemoreceptor nuclei.**

Overview
--------
The retrotrapezoid nucleus is the **central respiratory
chemoreceptor** of the **ventral respiratory group (VRG)** — the
**molecularly defined population** of **Phox2b⁺/VGlut2⁺/TH⁻**
glutamatergic neurons that **senses** CO2/H+ and **drives** the
respiratory pattern generator. It is a **leaf** module under the
**left** VRG container, and it is the **CO2 sensor / breathing
automaticity kernel**[reference:17].

**The RTN is the CHEMORECEPTOR, NOT an oscillator.** The
**oscillators** are the **pre-Bötzinger complex** (inspiratory), the
**Bötzinger complex** (expiratory), and the **pFRG** (active
expiration). The **RTN** **senses** CO2/H+ and **sends excitatory
glutamatergic drive** to those oscillators[reference:18][reference:19].
This is the **most important distinction** in the module.

**The RTN is a MOLECULARLY DEFINED population, NOT a classical Nissl
nucleus.** It is defined by **Phox2b**, **VGlut2**, **NK1R**, and
**TH-negativity** — the **same class** as the pre-Bötzinger complex
(**functionally/molecularly defined**), and the **opposite** of the
nucleus retrofacialis (**Nissl-defined**).

**The RTN OVERLAPS the pFRG and the C1 group.** **pFRG** is the
**expiratory oscillator** (the major pFRG population is **lateral** to
the RTN)[reference:20]. **C1** is the **sympathetic premotor**
population (C1 neurons **partially overlap** the RTN and extend
**caudally**)[reference:21][reference:22]. Consumers must **not** conflate
the RTN with either, and must **not** assume the overlaps make them
the same structure.

**The RTN is a paired structure, and each side is a chemoreceptor
cluster.** Each hemisphere has its own RTN. The two sides are
**bilaterally symmetric** and carry **NO coupling warning of their
own** — the **coupling warning attaches to the oscillators**, **not
to the sensor / driver**. See *Lateralization Notes*.

Molecularly Defined Subpopulations (prose, not structural children)
-------------------------------------------------------------------
The RTN is a **heterogeneous molecularly defined population** —
documented as **prose**, not as structural children:

*   **Phox2b⁺/VGlut2⁺/NK1R⁺/TH⁻ chemoreceptor neurons** — the **core
    RTN population**; **intrinsically pH-sensitive** via **TASK-2**
    (two-pore-domain K+ channel) and **GPR4** (G-protein-coupled
    receptor)[reference:23]; **glutamatergic** output to the
    respiratory pattern generator.

*   **Atoh1-lineage subpopulation** — **developmentally distinct**;
    required for **normal chemoresponsiveness** and **postnatal
    breathing**[reference:24]; part of the **Egr2/Phox2b/Lbx1/Atoh1**
    developmental program[reference:25].

*   **Putative subpopulations with different connectomes** — the RTN
    is **phenotypically heterogeneous** and may contain neurons with
    **different projection targets and functions**[reference:26].

**These subpopulations are prose, not structural children.** The
tree wires the **retrotrapezoid_nucleus** as a **single leaf** under
the left VRG. Consumers that need **subpopulation-level** resolution
should consult the references, not the tree.

The Retrotrapezoid Nucleus / Parafacial Respiratory Group Boundary
------------------------------------------------------------------
This is the **most consequential sibling** boundary, and it is
**contested and overlapping in the literature** — **chemoreceptor vs.
expiratory oscillator**, with **topographic overlap** and the
compound term **"RTN/pFRG"** in use:

*   **Retrotrapezoid_nucleus** (this module) — the **chemoreceptor
    population** — **Phox2b⁺/VGlut2⁺/TH⁻** — the **CO2/H+ sensor**.

*   **Parafacial respiratory group (pFRG)** (wired elsewhere) — the
    **expiratory oscillator** — the **late-expiratory (late-E)**
    population that **generates active expiration**.

**They OVERLAP topographically** — the **major pFRG population is
lateral to the RTN**, and the **medial pFRG may overlap the
RTN**[reference:28]. **This tree wires them as DISTINCT SIBLINGS**
because the tree separates **chemoreception from oscillation**: the
**RTN** is the **sensor / driver**; the **pFRG** is the
**oscillator**. **Consumers must not conflate the two, and must not
assume they are mutually exclusive** — they **overlap**. This is
**analogous** to the nucleus retrofacialis / Bötzinger complex
overlap (two different kinds of structure), but the distinction here
is **sensor vs. oscillator**, not **cytoarchitecture vs. function**.

The Retrotrapezoid Nucleus / Pre-Bötzinger Complex Boundary
-----------------------------------------------------------
This is the **sensor / driver vs. inspiratory oscillator** boundary:

*   **Retrotrapezoid_nucleus** (this module) — the **chemoreceptor**.

*   **Pre-Bötzinger complex** (``.../left/pre_botzinger_complex/``)
    — the **inspiratory rhythm kernel**.

**The RTN is UPSTREAM of the pre-Bötzinger complex** — it **sends
excitatory glutamatergic drive** to the pre-Bötzinger complex and the
Bötzinger complex[reference:29]. Consumers must **not** conflate the
two — the **RTN** is the **sensor / driver**; the **pre-Bötzinger
complex** is the **oscillator**.

The Retrotrapezoid Nucleus / Bötzinger Complex Boundary
-------------------------------------------------------
This is the **sensor / driver vs. expiratory oscillator** boundary:

*   **Retrotrapezoid_nucleus** (this module) — the **chemoreceptor**.

*   **Bötzinger complex** (``.../left/botzinger_complex/``) — the
    **expiratory oscillator**.

**The RTN is UPSTREAM of the Bötzinger complex** — it **sends
excitatory drive** to it. Consumers must **not** conflate the two.

The Retrotrapezoid Nucleus / C1 Group and RVLM Boundary
-------------------------------------------------------
This is the **respiratory chemoreceptor vs. cardiovascular sympathetic
premotor** boundary, and it is a **real topographic overlap**:

*   **Retrotrapezoid_nucleus** (this module) — the **respiratory
    chemoreceptor** population — **Phox2b⁺, TH⁻**.

*   **C1 adrenergic group / RVLM** (wired elsewhere) — the
    **sympathetic premotor** population — **TH⁺, PNMT⁺, adrenergic**.

**C1 neurons PARTIALLY OVERLAP the RTN and extend caudally from
it**[reference:30][reference:31]. They are **DIFFERENT FUNCTIONAL
POPULATIONS** that **share a neighborhood**. Consumers must **not**
conflate the two, and must **not** attribute **sympathetic /
vasomotor / blood-pressure** function to this module. *(The C1
**adrenergic phenotype** is a ``chemicals_hormones``-layer fact — see
Design Contract: no hormone imports.)*

The Retrotrapezoid Nucleus / Facial Nucleus Boundary
----------------------------------------------------
This is the **topographic landmark** boundary:

*   **Retrotrapezoid_nucleus** (this module) — the **respiratory
    chemoreceptor**.

*   **Facial nucleus (nucleus VII)**
    (``.../metencephalon/pons/facial_nucleus/``, wired elsewhere) —
    the **branchiomotor** nucleus for the **facial musculature**.

**The RTN is located VENTRAL and MEDIAL to the facial motor
nucleus**[reference:32][reference:33] — the facial nucleus is the
**topographic landmark**, **not the parent**. Consumers must **not**
conflate the two, and must **not** resolve the RTN as a child of the
facial nucleus.

The Retrotrapezoid Nucleus / Respiratory Pattern Generator Boundary
-------------------------------------------------------------------
This is the **sensor / driver vs. pattern generator** boundary:

*   **Retrotrapezoid_nucleus** (this module) — the **chemoreceptor**.

*   **Respiratory pattern generator (RPG)** — the **pre-Bötzinger
    complex**, the **Bötzinger complex**, and the **pFRG** — the
    **oscillators**.

**The RTN EXCLUSIVELY innervates the regions of the brainstem that
contain the respiratory pattern generator**[reference:34] — it is the
**sensor / driver**; the RPG is the **oscillator / pattern
generator**. Consumers must **not** conflate the two.

The Retrotrapezoid Nucleus / Carotid Bodies Boundary
----------------------------------------------------
This is the **central vs. peripheral chemoreceptor** boundary:

*   **Retrotrapezoid_nucleus** (this module) — the **CENTRAL
    chemoreceptor** (CO2/H+ in the brain).

*   **Carotid bodies** (wired elsewhere) — the **PERIPHERAL
    chemoreceptor** (hypoxia, with CO2/H+ modulation).

**The RTN and the carotid bodies are COMPLEMENTARY** — the RTN
**regulates breathing automaticity** and **CO2 homeostasis**, while
the carotid bodies **regulate the hypoxic response**[reference:35]
[reference:36]. Consumers must **not** conflate the two — the **RTN**
is **central**; the **carotid bodies** are **peripheral**.

Function in the Human Brain
---------------------------
The retrotrapezoid nucleus's functions are **central chemoreception**
and **breathing automaticity** — **NOT rhythm generation** and
**NOT motor output**:

*   **Central Chemoreception (CO2/H+ sensing):** The RTN **senses**
    increases in **brain PCO2 / decreases in pH** and **drives**
    breathing in **proportion to blood acidity or PCO2**[reference:37].
    The sensing involves **cell-autonomous pH sensitivity** (via
    **TASK-2** and **GPR4**), **astrocyte-dependent paracrine
    effects of pH**, and **synaptic input from other CO2-responsive
    neurons**[reference:38].

*   **Breathing Automaticity (sleep and wake):** The RTN **maintains
    breathing automaticity during slow-wave sleep**[reference:39] — it
    is the **nodal point** through which **breathing automaticity**
    is regulated to maintain a constant CO2[reference:40].

*   **Drive to the Respiratory Pattern Generator (glutamatergic
    output):** The RTN **sends excitatory glutamatergic projections**
    to the **Bötzinger complex** and the **pre-Bötzinger complex**,
    **regulating respiratory frequency, inspiratory amplitude, and
    active expiration**[reference:41][reference:42]. This is the
    **premotor-to-oscillator drive** — the RTN **modulates** the
    rhythm; the oscillators **generate** it.

*   **Active Expiration Recruitment (with the pFRG):** The RTN
    **drives the pFRG late-E neurons** during hypercapnia — the
    **activation of the pFRG late-E neurons requires glutamatergic
    inputs from the RTN**. The RTN is the **sensor**;
    the pFRG is the **oscillator**.

*   **Complementary Control with the Carotid Bodies:** The RTN and the
    carotid bodies **complement each other** — the RTN **regulates
    CO2 homeostasis** and **breathing automaticity**; the carotid
    bodies **regulate the hypoxic response**[reference:44][reference:45].

*   **NOT an oscillator.** The **oscillators** are the **pre-Bötzinger
    complex** (inspiratory), the **Bötzinger complex** (expiratory),
    and the **pFRG** (active expiration). The RTN **senses and
    drives** — it does **not** generate a rhythm.

*   **NOT the C1 group.** The RTN is the **respiratory chemoreceptor**
    population; the **C1 group** is the **cardiovascular (sympathetic
    premotor)** population. They **overlap topographically** but are
    **functionally and molecularly distinct**.

*   **NOT a motoneuron or premotor pool.** The **motoneuron pools**
    **execute** the motor output; the **premotor pools** **distribute**
    it. The RTN **senses and drives** — it is **upstream** of both.

**The unifying theme:** the retrotrapezoid nucleus is the **central
respiratory chemoreceptor** of the **ventral respiratory group** —
the **molecularly defined Phox2b⁺/VGlut2⁺ population** that
**senses** CO2/H+ and **drives** the respiratory pattern generator.
It is a **sensor / driver**, **NOT** an oscillator (**pre-Bötzinger
complex**, **Bötzinger complex**, **pFRG**), **NOT** the
cardiovascular **C1 group**, and **NOT** a motoneuron or premotor
pool.

Associated Disorders
--------------------
The retrotrapezoid nucleus has a **direct clinical association** with
**congenital central hypoventilation syndrome (CCHS)** — its clinical
relevance is **direct**, via the **PHOX2B** gene and the **central
CO2 chemoreflex**:

*   **Congenital Central Hypoventilation Syndrome (CCHS — DIRECT, via
    PHOX2B):** **CCHS** is caused by **PHOX2B** mutations (most
    commonly **polyalanine repeat expansions**, with ~10%
    **non-polyalanine** mutations associated with **more severe
    phenotypes**). **Phox2b mutations prevent RTN
    development in mice** and cause **hypoventilation** and **near
    absence of the hypercapnic ventilatory response**[reference:47]
    . The **RTN may be the major defect in CCHS, where
    central and peripheral inputs converge**[reference:49]. This is the
    **headline disorder** of the module — **direct**, not indirect.

*   **Sudden Infant Death Syndrome (SIDS — PROPOSED, not
    established):** The **RTN** is **thought to be involved** in
    **SIDS** via **arousal failure** and **respiratory rhythm
    instability** during sleep[reference:50]. This is **proposed**,
    not established.

*   **Sleep-Disordered Breathing / Central Sleep Apnea (via impaired
    CO2 chemoreflex):** The RTN is the **CO2 chemoreceptor** — its
    **dysfunction** contributes to **central sleep apnea** and to
    **hypoventilation during sleep**. This is **direct**, via the
    **central chemoreflex**.

*   **Rett Syndrome (INDIRECT — via the pre-Bötzinger complex, not the
    RTN):** **MECP2** mutations disrupt the **pre-Bötzinger complex**
    — the **RTN** is **not** the primary substrate. This is
    **indirect**, via the **oscillator** the RTN drives.

*   **No Named "Retrotrapezoid Nucleus Syndrome":** The RTN is a
    **molecularly defined population**, not a **single
    sharply-bounded structure** — it has **no named syndrome of its
    own** apart from **CCHS** (which is defined by the **PHOX2B**
    gene, not by the RTN alone). Its clinical relevance is
    **direct**, via the **central CO2 chemoreflex**.

**What is NOT here:** The RTN is **not** the substrate for
**OIRD** (pre-Bötzinger complex — NK1R neurons), **Wallenberg
syndrome** (lateral medulla — nucleus ambiguus, spinothalamic tract),
**locked-in syndrome** (basis pontis), **essential hypertension /
sympathetic overactivity** (**C1 group / RVLM** — **NOT this
module**), or **Kluver-Bucy syndrome** (amygdala). Its clinical
relevance is **direct**, via the **central CO2 chemoreflex** and
**PHOX2B**. **CCHS is the named disorder.**

Lateralization Notes
--------------------
This is the **left** retrotrapezoid_nucleus module. The
retrotrapezoid_nucleus is **bilaterally symmetric** and carries **NO
coupling warning of its own** — and it **inherits no warning from the
oscillators**:

*   **Bilateral Chemoreceptor Clusters:** Each hemisphere has its own
    RTN — each is a **chemoreceptor cluster** driving the
    **respiratory pattern generator**.

*   **NO Coupling Warning (the coupling warning attaches to the
    OSCILLATORS, not to the SENSOR / DRIVER):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **RTN** is a **sensor / driver** — it does
    **not** generate the rhythm, so it does **not** carry the
    **oscillator coupling warning**. Its **left** and **right** sides
    are **coordinated downstream** (at the pattern level, via the
    oscillators), **not** by direct **RTN–RTN** coupling. **This
    extends the propagatable rule:** **coupling warnings attach to
    oscillators — not to premotor pools, and not to sensory /
    chemoreceptor nuclei.**

*   **NO SLEA Warning:** The RTN is **SLEA-free** — it is **not** an
    extended-amygdala component.

*   **NO Amygdala-Lateralization Warning:** The RTN is **not** part of
    the amygdala — it does **not** inherit the amygdala-lateralization
    warning.

*   **NO Rhinencephalon-Exclusion Flag:** The RTN is **not** a
    rhinencephalon structure — it carries **no** rhinencephalon-
    exclusion flag.

**A consumer that assumes "left retrotrapezoid_nucleus = right
retrotrapezoid_nucleus" will be structurally correct** — the two
sides are **symmetric** and **functionally independent as
chemoreceptor clusters**. The retrotrapezoid_nucleus is a
**strict-mirror pair with NO warning** — **no coupling warning**,
**no SLEA warning**, **no amygdala-lateralization warning**, and
**no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../pre_botzinger_complex/``, ``.../botzinger_complex/``, the
    **pFRG**, the **C1 group / RVLM**, the **facial nucleus**, the
    **carotid bodies**, or any other container. The RTN's
    relationships to the pFRG, the pre-Bötzinger complex, the
    Bötzinger complex, the C1 group, the facial nucleus, the
    respiratory pattern generator, and the carotid bodies are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. **The C1 adrenergic
    phenotype (TH, PNMT, catecholamine synthesis) is a
    ``chemicals_hormones``-layer fact** — it is documented as
    **prose**, never imported.
*   **Leaf module — no structural children.** The **Phox2b⁺/VGlut2⁺**
    chemoreceptor neurons, the **Atoh1-lineage** subpopulation, and
    the **putative connectome subpopulations** are documented as
    **prose**, not as sub-modules. Consumers must not assume any exist
    as children; resolve **subpopulation-level** detail through the
    references.
*   **CHEMORECEPTOR / DRIVER — NOT an oscillator.** The
    **oscillators** are the **pre-Bötzinger complex** (inspiratory),
    the **Bötzinger complex** (expiratory), and the **pFRG** (active
    expiration). The RTN **senses and drives** — it does **not**
    generate. Consumers must **not** attribute rhythm generation to
    this module.
*   **MOLECULARLY DEFINED population — NOT a classical Nissl
    nucleus.** Defined by **Phox2b, VGlut2, NK1R, TH-negativity** and
    **Egr2/Lbx1/Atoh1 lineage** — not by a sharp cytoarchitectonic
    border. Consumers must **not** treat it as a **sharply-bounded
    nucleus**.
*   **OVERLAPS the pFRG — the two are DIFFERENT FUNCTIONAL
    POPULATIONS.** The **pFRG** is the **expiratory oscillator**; the
    **RTN** is the **chemoreceptor**. They **overlap
    topographically** — consumers must **not** assume they are
    mutually exclusive, and must **not** collapse one into the
    other.
*   **NOT the pre-Bötzinger complex — that is the INSPIRATORY
    oscillator.** The RTN is **upstream** of it.
*   **NOT the Bötzinger complex — that is the EXPIRATORY oscillator.**
    The RTN is **upstream** of it.
*   **NOT the C1 group / RVLM — that is the SYMPATHETIC PREMOTOR
    population.** **C1 partially overlaps the RTN** — a **real
    boundary hazard**. Consumers must **not** attribute
    **sympathetic / vasomotor / blood-pressure** function to this
    module.
*   **NOT the facial nucleus — that is the BRANCHIOMOTOR neighbor.**
    The RTN is **ventral and medial** to the facial motor nucleus.
*   **NOT a motoneuron or premotor pool — a SENSOR / DRIVER.**
*   **NOT a single uniform population — MULTIPLE subpopulations.**
*   **NO coupling warning — the coupling warning attaches to the
    OSCILLATORS, not to the SENSOR / DRIVER.** The RTN is a **strict
    mirror with NO warning**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop.** The retrotrapezoid_nucleus is a local
    leaf under the left VRG, not a cross-listed leaf.
*   **No nested cross-listing.** The retrotrapezoid_nucleus has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with right retrotrapezoid_nucleus — strict
    mirror with NO warning.** Left and right RTN modules are
    **structurally identical** — same leaf status, same
    **chemoreceptor** framing, same **molecularly defined** framing,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left import retrotrapezoid_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "ventral_respiratory_group.left.retrotrapezoid_nucleus"
    )

**Do not** assume the retrotrapezoid_nucleus is the **parafacial
respiratory group (pFRG)**. The **pFRG** is the **active-expiration
oscillator**; the **RTN** is the **chemoreceptor**. They **overlap**
topographically but are **functionally distinct**.

**Do not** assume the retrotrapezoid_nucleus is an **oscillator**.
It is a **sensor / driver**. The oscillators are the **pre-Bötzinger
complex**, the **Bötzinger complex**, and the **pFRG**.

**Do not** assume the retrotrapezoid_nucleus is the **pre-Bötzinger
complex** or the **Bötzinger complex**. Those are the **rhythm
generators**; the **RTN** is **upstream** of them.

**Do not** assume the retrotrapezoid_nucleus is the **C1 group /
RVLM**. **C1 neurons partially overlap the RTN** — they are the
**sympathetic premotor** population. The RTN is the **respiratory
chemoreceptor** population.

**Do not** assume the retrotrapezoid_nucleus is the **facial
nucleus**. The RTN is **ventral and medial** to the facial motor
nucleus.

**Do not** import the **oscillator coupling warning** into the
retrotrapezoid_nucleus. **The RTN is a SENSOR / DRIVER** — it
carries **NO coupling warning**.

Iterating the retrotrapezoid_nucleus's (empty) children (recommended
consumer pattern)::

    RETROTRAPEZOID_NUCLEUS_CHILDREN = ()
    # The retrotrapezoid_nucleus is a leaf. The Phox2b+/VGlut2+
    # chemoreceptor neurons, the Atoh1-lineage subpopulation, and the
    # putative connectome subpopulations are prose, not modules.

Reaching the parafacial respiratory group (recommended consumer
pattern — NOTE the topographic overlap)::

    # The parafacial respiratory group (pFRG) is the
    # ACTIVE-EXPIRATION oscillator — it OVERLAPS the RTN
    # topographically:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   parafacial_respiratory_group
    #
    # The RTN is the CHEMORECEPTOR; the pFRG is the OSCILLATOR.
    # They OVERLAP — they are not mutually exclusive.

Reaching the pre-Bötzinger complex (recommended consumer pattern —
the inspiratory oscillator, downstream of the RTN)::

    # The pre-Bötzinger complex is the INSPIRATORY rhythm kernel — the
    # RTN sends excitatory glutamatergic drive to it:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   ventral_respiratory_group.left.pre_botzinger_complex
    #
    # The RTN SENSES CO2/H+; the pre-Bötzinger complex GENERATES the
    # inspiratory rhythm.

Reaching the Bötzinger complex (recommended consumer pattern — the
expiratory oscillator, downstream of the RTN)::

    # The Bötzinger complex is the EXPIRATORY oscillator — the RTN
    # sends excitatory drive to it:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   ventral_respiratory_group.left.botzinger_complex
    #
    # The RTN SENSES CO2/H+; the Bötzinger complex GENERATES the
    # expiratory rhythm.

Reaching the C1 group / RVLM (recommended consumer pattern — NOTE
the topographic overlap)::

    # The C1 adrenergic group of the rostral ventrolateral medulla
    # (RVLM) is the SYMPATHETIC PREMOTOR population. C1 neurons
    # PARTIALLY OVERLAP the RTN and extend caudally from it:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.
    #   rostral_ventrolateral_medulla.c1_group
    #
    # The C1 group is CARDIOVASCULAR; the RTN is RESPIRATORY. They
    # OVERLAP topographically but are functionally and molecularly
    # distinct. Do not attribute sympathetic / vasomotor /
    # blood-pressure function to the RTN.

Reaching the facial nucleus (recommended consumer pattern — NOTE the
topographic landmark)::

    # The facial nucleus (nucleus VII) is the BRANCHIOMOTOR nucleus
    # for the facial musculature — the RTN is located VENTRAL and
    # MEDIAL to it:
    #
    #   hindbrain.metencephalon.pons.facial_nucleus
    #
    # The facial nucleus is the TOPOGRAPHIC LANDMARK, not the parent.

Reaching the carotid bodies (recommended consumer pattern — the
peripheral chemoreceptor)::

    # The carotid bodies are the PERIPHERAL chemoreceptor (hypoxia,
    # with CO2/H+ modulation). The RTN and the carotid bodies are
    # COMPLEMENTARY:
    #
    #   peripheral.carotid_bodies
    #
    # The RTN is the CENTRAL chemoreceptor; the carotid bodies are the
    # PERIPHERAL chemoreceptor.

Bilateral iteration (recommended consumer pattern — NOTE the
sensor/driver rule)::

    for side in ("left", "right"):
        rtn_path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"ventral_respiratory_group.{side}."
            f"retrotrapezoid_nucleus"
        )
        # resolve rtn_path through the memory/recall layer
        #
        # NOTE: the two sides are SENSOR / DRIVER clusters. There is
        # NO coupling warning here. The coupling warning attaches to
        # the OSCILLATORS (pre-Bötzinger complex, Bötzinger complex),
        # not to the sensory / chemoreceptor nuclei.

Subpopulation-level detail (not wired — consult references)::

    # The retrotrapezoid_nucleus's subpopulations are prose, not
    # modules:
    #   Phox2b+/VGlut2+/NK1R+/TH- -> core chemoreceptor; TASK-2,
    #                                GPR4 pH sensors
    #   Atoh1-lineage             -> normal chemoresponsiveness;
    #                                postnatal breathing
    #   putative connectome subs  -> heterogeneous projections and
    #                                functions
    #
    # Do not attempt to resolve these as sub-paths of the
    # retrotrapezoid_nucleus.

References
----------
*   **Definitive RTN review:** Guyenet, P.G., Bayliss, D.A., Stornetta,
    R.L., Ludwig, M.G., Kumar, N.N., Shi, Y., Bayliss, D.A. (2019).
    "The Retrotrapezoid Nucleus: Central Chemoreceptor and Regulator
    of Breathing Automaticity." *Trends in Neurosciences* 42:807–824.
    (The most complete characterization of the RTN — transcriptome,
    lineage, projections, CO2 homeostasis, and mechanisms of pH
    sensitivity.)
*   **RTN and breathing (review):** Guyenet, P.G., Stornetta, R.L.,
    Bayliss, D.A. (2012). "The retrotrapezoid nucleus and breathing."
    *Advances in Experimental Medicine and Biology* 758:115–122.
    (The RTN as a bilateral cluster of Phox2b⁺ glutamatergic neurons;
    the respiratory chemoreflex and CCHS.)
*   **RTN definition and markers:** Guyenet, P.G. (2008). "The 2008
    Carl Ludwig Lecture: retrotrapezoid nucleus, CO2 homeostasis, and
    breathing automaticity." *Journal of Applied Physiology*
    105:404–416. (The RTN as ~2,000 glutamatergic neurons innervating
    the respiratory centers; the definition of the RTN population.)
*   **RTN development:** Gordis, C., Dubreuil, V., Thoby-Brisson, M.,
    Fortin, G., Champagnat, J. (2010). "Phox2b, congenital central
    hypoventilation syndrome and the control of respiration."
    *Seminars in Cell & Developmental Biology* 21:814–822. (The
    **Egr2, Phox2b, Lbx1, Atoh1** developmental program and CCHS.)
*   **Atoh1-lineage RTN subpopulation:** Huang, W.H., Tupal, S.,
    Huang, T.W., et al. (2012). "Atoh1 governs the migration of
    postmitotic neurons that shape respiratory effectiveness at birth
    and chemoresponsiveness in adulthood." *Neuron* 75:799–809.
    (The Atoh1-lineage subpopulation required for normal
    chemoresponsiveness.)
*   **RTN pH sensitivity (TASK-2, GPR4):** Kumar, N.N., Velic, A.,
    Soliz, J., Shi, Y., Li, K., Wang, S., Weaver, J.L., Sen, J.,
    Abbott, S.B.G., Lazarenko, R.M., Ludwig, M.-G., Perez-Reyes, E.,
    Mohebbi, N., Bettoni, C., Gassmann, M., Suply, T., Seuwen, K.,
    Guyenet, P.G., Wagner, C.A., Bayliss, D.A. (2015). "Regulation of
    breathing by CO2 requires the proton-activated receptor GPR4 in
    retrotrapezoid nucleus neurons." *Science* 348:1255–1260. (The
    **GPR4** proton sensor in RTN neurons.)
*   **RTN TASK-2:** Gestreau, C., Heitzmann, D., Thomas, J., Dubreuil,
    V., Forster, I.C., Barhanin, J. (2010). "Task-2 potassium channel
    is required for normal breathing." *Current Biology* 20:1233–1238.
    (The **TASK-2** pH sensor in RTN neurons.)
*   **RTN and the pFRG (overlap and distinction):** Smith, J.C.,
    Abdala, A.P.L., Koizumi, H., Rybak, I.A., Paton, J.F.R. (2007).
    "Spatial and functional architecture of the mammalian brainstem
    respiratory network: a hierarchy of three oscillatory mechanisms."
    *Journal of Neurophysiology* 98:3370–3387. (The pFRG as the
    expiratory oscillator; the RTN/pFRG region as a heterogeneous
    group surrounding the facial nucleus.)
*   **RTN drives the pFRG late-E neurons:** Silva, J.N., Lucena,
    E.V., Silva, T.M., et al. (2016). "Neuroanatomical and
    physiological evidence that the retrotrapezoid nucleus/parafacial
    region regulates expiration in adult rats." *Respiratory
    Physiology & Neurobiology* 224:22–30. (The RTN → pFRG late-E
    glutamatergic drive during hypercapnia.)
*   **pFRG overlap with the RTN:** Feldman, J.L., Del Negro, C.A.
    (2006). "Looking for inspiration: new perspectives on respiratory
    rhythm." *Nature Reviews Neuroscience* 7:232–242. (The RTN/pFRG
    region and the pFRG–preBötC debate.)
*   **RTN and C1 overlap:** Stornetta, R.L., Moreau, J.M., Takakura,
    A.C., et al. (2006). "Expression of Phox2b by brainstem neurons
    involved in chemosensory integration in the adult rat." *Journal
    of Neuroscience* 26:10305–10314. (The Phox2b⁺ RTN neurons are
    **not** catecholaminergic and are clustered **ventrolateral to the
    C1 neurons** and **below the facial motor nucleus**.)
*   **C1 group and RVLM (contrast — the sympathetic premotor
    population, partially overlapping):** Guyenet, P.G. (2006). "The
    sympathetic control of blood pressure." *Nature Reviews
    Neuroscience* 7:335–346. (The C1 adrenergic group and the RVLM as
    the sympathetic premotor population — contrast with the
    respiratory RTN.)
*   **CCHS and PHOX2B:** Amiel, J., Laudier, B., Attié-Bitach, T.,
    et al. (2003). "Polyalanine expansion and frameshift mutations of
    the paired-like homeobox gene PHOX2B in congenital central
    hypoventilation syndrome." *Nature Genetics* 33:459–461. (The
    original PHOX2B–CCHS link.)
*   **CCHS beyond the RTN:** (2022). "Beyond the Retrotrapezoid
    Nucleus in Congenital Central Hypoventilation Syndrome."
    *American Journal of Respiratory and Critical Care Medicine*
    205:271–272. (CCHS as a PHOX2B disorder with effects beyond the
    RTN — autonomic and cerebral consequences.)
*   **RTN and SIDS (proposed):** Kinney, H.C., Richerson, G.B.,
    Dymecki, S.M., Darnall, R.A., Nattie, E.E. (2009). "The brainstem
    and serotonin in the sudden infant death syndrome." *Annual Review
    of Pathology* 4:517–550. (The RTN and medullary respiratory
    network in SIDS — a proposed link.)
*   **Pontine respiratory group (contrast — the pontine modulator):**
    Dutschmann, M., Dick, T.E. (2012). "Pontine mechanisms of
    respiratory control." *Comprehensive Physiology* 2:2443–2469.
    (The pontine respiratory group as the pontine modulator —
    contrast with the medullary RTN.)
*   **SLEA (contrast — the RTN is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; **NOT** the RTN.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary respiratory groups in overview.)
*   Paxinos, G., Franklin, K.B.J. (2019). *Paxinos and Franklin's the
    Mouse Brain in Stereotaxic Coordinates*, 5th ed. (Atlas placement
    of the RTN relative to the facial nucleus and C1.)
*   NeuroNames — Retrotrapezoid nucleus (left); FMA — Retrotrapezoid
    nucleus (left member).
"""