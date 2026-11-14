"""
infrastructure.brainparts.hindbrain.metencephalon.pons.parvocellular_reticular_nucleus
======================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── parvocellular_reticular_nucleus   <-- THIS MODULE

**Primary synonym:** Parvocellular reticular nucleus; PCRt; PCRtN;
parvocellular reticular formation (pontine portion); "the pontine
orofacial premotor and autonomic relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem reticular formation region** — **not a single anatomically
delimited nucleus**, but a **functionally defined group of small
(parvocellular) neurons** in the **lateral pontine tegmentum**, medial
to the **trigeminal motor nucleus** and the **facial nerve nucleus**,
lateral to the **paramedian pontine reticular formation (PPRF)**. It is
the **pontine orofacial premotor relay** — the **critical node** for
**orofacial motor control** (mastication, swallowing, facial expression,
vocalization) and **autonomic regulation** (cardiorespiratory,
gastrointestinal).
**Part of:** The **pons** container — specifically, the **pontine
tegmentum** (the **lateral zone** of the **pontine reticular
formation**). The **pons** is the **metencephalic** brainstem segment.
**Structural parent:** ``.../pons/`` → **direct child** of the pons
container.
**Structural children:** **None.** This is a **leaf** module. The
**orofacial premotor neurons**, **autonomic relay neurons**, and
**reticulospinal projection neurons** are documented as **prose**, not
as structural children — they are the **functionally distinct neuron
populations** within the region.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
parvocellular reticular nucleus is a LEAF, not a container.** It has
**no structural children**. The **orofacial premotor neurons**,
**autonomic relay neurons**, and **reticulospinal projection neurons**
are **prose** populations, not structural children. Consumers must
**not** treat the parvocellular reticular nucleus as a container, and
must **not** assume the neuron populations exist as sub-modules.
**Boundary status (FUNCTIONALLY DEFINED REGION — NOT a cytologically
distinct nucleus):** **Boundary case — the parvocellular reticular
nucleus is a FUNCTIONALLY DEFINED REGION, NOT a cytologically distinct
nucleus.** Unlike the **trigeminal motor nucleus** (a compact branchial
motor nucleus) or the **facial nerve nucleus** (a compact branchial
motor nucleus), the **parvocellular reticular nucleus** is a
**functionally defined group of small (parvocellular) neurons** in the
**lateral pontine tegmentum** — it is defined by its **axonal
projections** (to the cranial nerve motor nuclei and the spinal cord)
and its **functional role** (orofacial premotor relay and autonomic
regulation), rather than by a **distinct cytoarchitectonic boundary**.
This **diffuse organization** is **prose**, not structural children.
Consumers must **not** expect a compact, cytologically distinct nucleus
— the **parvocellular reticular nucleus** is a **functional population**
defined by its **targets** and its **premotor / autonomic role**.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the parvocellular reticular nucleus is a SINGLE module
at the tree level, even though the parvocellular reticular nucleus is
BILATERAL in real anatomy.** Unlike the **cranial_nerve_nuclei** module
(which has explicit ``left`` and ``right`` structural children), the
**parvocellular_reticular_nucleus** module (here) is a **single module**
that represents the **bilateral parvocellular reticular nucleus** (left
and right lateral pontine tegmentum). The tree does **not** split them
into left/right. Consumers must **not** assume a left/right split
exists at the tree level — the module is a **single, bilateral
representation**.
**Boundary status (PREmotor OROFACIAL RELAY — NOT the motor output
nuclei):** **Boundary case — the parvocellular reticular nucleus is a
PREMOTOR OROFACIAL RELAY, NOT the motor output nuclei.** The
**parvocellular reticular nucleus** (here) is the **premotor relay**
that **provides** the **premotor drive** to the **trigeminal motor
nucleus**, the **facial nerve nucleus**, the **hypoglossal nucleus**,
and the **nucleus ambiguus** — it **coordinates** the **orofacial
motor patterns** (mastication, swallowing, facial expression,
vocalization). The **trigeminal motor nucleus**, the **facial nerve
nucleus**, the **hypoglossal nucleus**, and the **nucleus ambiguus** are
the **motor output nuclei** that **execute** the **orofacial motor
patterns** via the **cranial nerves** (V, VII, XII, IX/X). They are
**DIFFERENT STRUCTURES** — the **parvocellular reticular nucleus** is
**upstream premotor**; the **cranial nerve motor nuclei** are
**downstream motor**. **This distinction is clinically load-bearing** — a
**parvocellular reticular nucleus lesion** causes **orofacial motor
dysfunction** (impaired mastication, swallowing, facial expression,
vocalization) **without** the **full lower-motor-neuron pattern** of a
**cranial nerve motor nucleus lesion** (which would cause **flaccid
paralysis** of the **specific muscles** innervated by that nucleus). The
**parvocellular reticular nucleus** **coordinates** the **orofacial
motor patterns** across **multiple cranial nerve motor nuclei**;
individual **cranial nerve motor nucleus lesions** produce **specific**
muscle weakness. Consumers must **not** conflate the parvocellular
reticular nucleus with the cranial nerve motor nuclei.
**Boundary status (NOT the trigeminal motor nucleus — that is a
DOWNSTREAM MOTOR OUTPUT TARGET):** **Boundary case — the parvocellular
reticular nucleus is NOT the trigeminal motor nucleus; the trigeminal
motor nucleus is a DOWNSTREAM MOTOR OUTPUT TARGET.** The **trigeminal
motor nucleus** (``.../cranial_nerve_nuclei/left/motor_trigeminal_nucleus/``
and ``.../right/``) is the **branchial motor** nucleus for the **muscles
of mastication** (masseter, temporalis, medial pterygoid, lateral
pterygoid, mylohyoid, anterior belly of the digastric, tensor tympani,
tensor veli palatini). The **parvocellular reticular nucleus** (here)
is the **premotor relay** that **provides** the **premotor drive** to
the trigeminal motor nucleus for **mastication**. They are **DIFFERENT
STRUCTURES** — the **parvocellular reticular nucleus** is **upstream
premotor**; the **trigeminal motor nucleus** is **downstream motor**.
Consumers must **not** conflate the parvocellular reticular nucleus with
the trigeminal motor nucleus.
**Boundary status (NOT the facial nerve nucleus — that is a DOWNSTREAM
MOTOR OUTPUT TARGET):** **Boundary case — the parvocellular reticular
nucleus is NOT the facial nerve nucleus; the facial nerve nucleus is a
DOWNSTREAM MOTOR OUTPUT TARGET.** The **facial nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
``.../right/``) is the **branchial motor** nucleus for the **muscles of
facial expression** (frontalis, orbicularis oculi, orbicularis oris,
buccinator, platysma, stapedius, stylohyoid, posterior belly of the
digastric). The **parvocellular reticular nucleus** (here) is the
**premotor relay** that **provides** the **premotor drive** to the
facial nerve nucleus for **facial expression**. They are **DIFFERENT
STRUCTURES** — the **parvocellular reticular nucleus** is **upstream
premotor**; the **facial nerve nucleus** is **downstream motor**.
Consumers must **not** conflate the parvocellular reticular nucleus with
the facial nerve nucleus.
**Boundary status (NOT the hypoglossal nucleus — that is a MEDULLARY
DOWNSTREAM MOTOR OUTPUT TARGET):** **Boundary case — the parvocellular
reticular nucleus is NOT the hypoglossal nucleus; the hypoglossal
nucleus is a MEDULLARY DOWNSTREAM MOTOR OUTPUT TARGET.** The
**hypoglossal nucleus**
(``.../medulla_oblongata/cranial_nerve_nuclei/left/hypoglossal_nucleus/``
and ``.../right/``) is the **somatic motor** nucleus for the **tongue
muscles**. The **parvocellular reticular nucleus** (here) is the
**premotor relay** that **provides** the **premotor drive** to the
hypoglossal nucleus for **tongue movements** during **mastication**,
**swallowing**, and **speech**. They are **DIFFERENT STRUCTURES** —
different brainstem levels (pons vs. medulla), different functional
roles (premotor relay vs. motor output). Consumers must **not** conflate
the parvocellular reticular nucleus with the hypoglossal nucleus.
**Boundary status (NOT the nucleus ambiguus — that is a MEDULLARY
DOWNSTREAM MOTOR OUTPUT TARGET):** **Boundary case — the parvocellular
reticular nucleus is NOT the nucleus ambiguus; the nucleus ambiguus is a
MEDULLARY DOWNSTREAM MOTOR OUTPUT TARGET.** The **nucleus ambiguus**
(``.../medulla_oblongata/cranial_nerve_nuclei/left/nucleus_ambiguus/``
and ``.../right/``) is the **branchial motor** nucleus for the
**pharynx** and **larynx**. The **parvocellular reticular nucleus**
(here) is the **premotor relay** that **provides** the **premotor
drive** to the nucleus ambiguus for **swallowing** and **vocalization**.
They are **DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (premotor relay vs. motor output).
Consumers must **not** conflate the parvocellular reticular nucleus with
the nucleus ambiguus.
**Boundary status (NOT the PPRF — that is a SIBLING under the pons
container):** **Boundary case — the parvocellular reticular nucleus is
NOT the paramedian pontine reticular formation (PPRF); the PPRF is a
SIBLING under the pons container.** The **PPRF**
(``.../pons/paramedian_pontine_reticular_formation/``) is the
**horizontal saccadic burst generator** — it **drives** the abducens
nucleus for **horizontal saccades**. The **parvocellular reticular
nucleus** (here) is the **orofacial premotor and autonomic relay** — it
**drives** the **cranial nerve motor nuclei** for **mastication**,
**swallowing**, **facial expression**, and **vocalization**, and it
**regulates autonomic function**. They are **DIFFERENT STRUCTURES** —
different functional systems (horizontal saccades vs. orofacial
motor/autonomic) and different anatomical locations (**paramedian** PPRF
vs. **lateral** parvocellular reticular nucleus). They are
**anatomically adjacent** (both are in the pontine tegmentum) — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the parvocellular reticular nucleus with the PPRF.
**Boundary status (NOT the gigantocellular reticular nucleus — that is
a MEDULLARY structure):** **Boundary case — the parvocellular reticular
nucleus is NOT the gigantocellular reticular nucleus.** The
**gigantocellular reticular nucleus (Gi)**
(``.../medulla_oblongata/.../gigantocellular_reticular_nucleus/`` —
**prose location** in the **medulla**, not a structural child of the
pons in the tree) is the **large-cell (gigantocellular) component** of
the **medullary reticular formation** — it is involved in **motor
control** (reticulospinal tract), **autonomic regulation**, and
**nociception modulation**. The **parvocellular reticular nucleus**
(here) is the **small-cell (parvocellular) component** of the **pontine
reticular formation**. They are **DIFFERENT STRUCTURES** — different
brainstem levels (pons vs. medulla) and different cytoarchitectonic
characteristics (small-cell vs. large-cell). Consumers must **not**
conflate the parvocellular reticular nucleus with the gigantocellular
reticular nucleus.
**Boundary status (NOT the caudal pontine reticular nucleus or the oral
pontine reticular nucleus — those are RELATED RETICULAR NUCLEI):**
**Boundary case — the parvocellular reticular nucleus is NOT the caudal
pontine reticular nucleus or the oral pontine reticular nucleus; those
are RELATED RETICULAR NUCLEI.** The **caudal pontine reticular nucleus
(PnC)** and the **oral pontine reticular nucleus (PnO)** are **other
components** of the **pontine reticular formation** — they are involved
in **motor control**, **sleep/wake regulation**, and **autonomic
function**. The **parvocellular reticular nucleus** (here) is the
**small-cell component** that is **specifically dedicated** to
**orofacial premotor relay and autonomic regulation**. They are
**DIFFERENT STRUCTURES** — different cytoarchitectonic components of the
pontine reticular formation, different functional emphases. Consumers
must **not** conflate the parvocellular reticular nucleus with the
caudal pontine reticular nucleus or the oral pontine reticular nucleus.
**Boundary status (NOT the pontine nuclei — those are basilar-pons
cortico-ponto-cerebellar relays):** **Boundary case — the parvocellular
reticular nucleus is NOT the pontine nuclei.** The **pontine nuclei**
(``.../pons/pontine_nuclei/left/`` and ``.../right/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons** — they
**receive** corticopontine fibers from the cerebral cortex and
**project** to the **contralateral cerebellar cortex** via the
**middle cerebellar peduncle**. The **parvocellular reticular nucleus**
(here) is the **dorsal tegmental** orofacial premotor and autonomic
relay. They are **DIFFERENT STRUCTURES** — different anatomical
locations (basilar pons vs. dorsal tegmentum), different functional
systems (cortico-ponto-cerebellar vs. orofacial motor/autonomic).
Consumers must **not** conflate the parvocellular reticular nucleus with
the pontine nuclei.
**Boundary status (NOT the locus coeruleus — that is the adjacent
noradrenergic nucleus):** **Boundary case — the parvocellular reticular
nucleus is NOT the locus coeruleus.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``) is the **noradrenergic
nucleus** — the **principal source of norepinephrine** in the brain —
it is in the **pontine tegmentum**, **dorsolateral** to the
parvocellular reticular nucleus. The **parvocellular reticular nucleus**
(here) is the **orofacial premotor and autonomic relay**. They are
**DIFFERENT STRUCTURES** — different neurotransmitters (glutamate,
GABA, etc. vs. norepinephrine), different functional systems
(orofacial motor/autonomic vs. noradrenergic arousal). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the parvocellular
reticular nucleus with the locus coeruleus.
**Boundary status (NOT the parabrachial area — that is the visceral-
sensory and respiratory relay):** **Boundary case — the parvocellular
reticular nucleus is NOT the parabrachial area.** The **parabrachial
area** (``.../pons/parabrachial_area/``) is the **visceral-sensory and
respiratory-relay complex** — the **lateral parabrachial nucleus**
(visceral-sensory and pain/aversion relay), the **medial parabrachial
nucleus** (respiratory and autonomic relay), and the **subparabrachial
nucleus** (pontine respiratory center). The **parvocellular reticular
nucleus** (here) is the **orofacial premotor and autonomic relay**. They
are **DIFFERENT STRUCTURES** — different functional systems (orofacial
motor/autonomic vs. visceral-sensory/respiratory). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the parvocellular
reticular nucleus with the parabrachial area.
**Boundary status (NOT the superior olivary complex — that is an
auditory brainstem relay):** **Boundary case — the parvocellular
reticular nucleus is NOT the superior olivary complex.** The **superior
olivary complex**
(``.../pons/superior_olivary_complex/left/`` and ``.../right/``) is the
**auditory brainstem relay** — it **receives** cochlear nuclei
projections and **processes interaural time and intensity differences**
for **sound localization**. The **parvocellular reticular nucleus**
(here) is the **orofacial premotor and autonomic relay**. They are
**DIFFERENT STRUCTURES** — different functional systems (orofacial
motor/autonomic vs. auditory). Consumers must **not** conflate the
parvocellular reticular nucleus with the superior olivary complex.
**Boundary status (NOT the solitary nucleus — that is the MEDULLARY
visceral-afferent hub):** **Boundary case — the parvocellular reticular
nucleus is NOT the solitary nucleus.** The **solitary nucleus** (nucleus
tractus solitarius,
``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``) is
the **medullary visceral-afferent hub** for **CN VII, IX, and X** —
taste, visceral sensation, baroreception, respiratory chemoreception,
and gastrointestinal afferents. The **parvocellular reticular nucleus**
(here) is the **pontine orofacial premotor and autonomic relay**. They
are **DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (orofacial motor/autonomic relay
vs. visceral-afferent integration). The parvocellular reticular nucleus
**receives** visceral afferents from the solitary nucleus (via the
**medial parabrachial nucleus** and **direct** projections) — but it is
**not** the solitary nucleus. Consumers must **not** conflate the
parvocellular reticular nucleus with the solitary nucleus.
**Boundary status (NOT the superior cerebellar peduncle — that is the
white-matter tract):** **Boundary case — the parvocellular reticular
nucleus is the GREY-MATTER NUCLEI, NOT the superior cerebellar
peduncle.** The **superior cerebellar peduncle** (the "brachium
conjunctivum") is the **white-matter tract** that carries **cerebellar
efferents** from the **dentate nucleus** and the **interposed nucleus**
to the **red nucleus** and the **thalamus**. The **parvocellular
reticular nucleus** (here) is the **grey-matter neuron cluster** in the
**lateral pontine tegmentum**. They are **DIFFERENT STRUCTURES** — the
**nucleus** is grey matter; the **peduncle** is white matter. Consumers
must **not** conflate the parvocellular reticular nucleus with the
superior cerebellar peduncle.
**Boundary status (NOT the whole pons — the pons is the parent):**
**Boundary case — the parvocellular reticular nucleus is NOT the whole
pons; the pons is the PARENT.** The **pons** (``.../pons/``) is the
**whole metencephalic brainstem segment** — it contains the **basilar
pons**, the **pontine tegmentum**, the **pontine nuclei**, the
**corticospinal / corticobulbar tracts**, the **middle cerebellar
peduncle**, the **cranial_nerve_nuclei**, the **parabrachial area**,
the **PPRF**, and the **parvocellular reticular nucleus**. The
**parvocellular reticular nucleus** (here) is the **lateral pontine
tegmental orofacial premotor and autonomic relay** only. Consumers must
**not** conflate the parvocellular reticular nucleus with the **whole
pons**.
**Boundary status (MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS —
orofacial premotor vs. autonomic relay vs. reticulospinal):** **Boundary
case — the parvocellular reticular nucleus is NOT a single uniform
neuron population; it contains MULTIPLE functionally distinct
populations.** The **orofacial premotor neurons** — the **premotor
neurons** that **project to** the **trigeminal motor nucleus**, the
**facial nerve nucleus**, the **hypoglossal nucleus**, and the
**nucleus ambiguus** — they **coordinate** the **orofacial motor
patterns** (mastication, swallowing, facial expression, vocalization).
The **autonomic relay neurons** — the **neurons** that **receive**
visceral afferents (from the solitary nucleus and the medial parabrachial
nucleus) and **project to** the **hypothalamus** and the **brainstem
autonomic centers** (rostral ventrolateral medulla, nucleus ambiguus) —
they **regulate** **cardiovascular**, **respiratory**, and
**gastrointestinal** function. The **reticulospinal projection
neurons** — the **neurons** that **project to** the **spinal cord**
(via the **reticulospinal tract**) — they **modulate** **motor
activity** and **autonomic outflow** at the **spinal level**. **These
populations are prose, not structural children.** Consumers must **not**
treat the parvocellular reticular nucleus as a single uniform population
— it is a **functionally heterogeneous complex** with **distinct**
sub-circuits.
**Boundary status (SLEA-FREE — the parvocellular reticular nucleus is
NOT an extended-amygdala component):** **Boundary case — the
parvocellular reticular nucleus is SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **parvocellular reticular nucleus**
is a **pontine orofacial premotor and autonomic relay** — it is **NOT**
an extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the parvocellular
reticular nucleus — it is **SLEA-free**.

Overview
--------
The parvocellular reticular nucleus is the **orofacial premotor and
autonomic relay** of the **pons** — a **functionally defined region** of
**small (parvocellular) neurons** in the **lateral pontine tegmentum**,
medial to the **trigeminal motor nucleus** and the **facial nerve
nucleus**, lateral to the **PPRF**. It is a **leaf** module under the
pons container, and it is the **premotor relay** that **coordinates**
the **orofacial motor patterns** (mastication, swallowing, facial
expression, vocalization) and the **autonomic regulation**
(cardiorespiratory, gastrointestinal).

**The parvocellular reticular nucleus is a LEAF, not a container.** It
has **no structural children**. The **orofacial premotor neurons**,
**autonomic relay neurons**, and **reticulospinal projection neurons**
are **prose populations**, not structural children.

**The parvocellular reticular nucleus is a FUNCTIONALLY DEFINED REGION,
NOT a cytologically distinct nucleus.** Unlike the trigeminal motor
nucleus (compact branchial motor) or the facial nerve nucleus (compact
branchial motor), the parvocellular reticular nucleus is a **functionally
defined group of small (parvocellular) neurons** in the **lateral
pontine tegmentum** — it is defined by its **axonal projections** (to
the cranial nerve motor nuclei and the spinal cord) and its
**functional role** (orofacial premotor relay and autonomic regulation),
rather than by a **distinct cytoarchitectonic boundary**.

**The parvocellular reticular nucleus is a PREMOTOR OROFACIAL RELAY, NOT
the motor output nuclei.** The parvocellular reticular nucleus is the
**premotor relay** that **coordinates** the **orofacial motor patterns**
across multiple cranial nerve motor nuclei; the **cranial nerve motor
nuclei** are the **motor output nuclei** that **execute** the specific
orofacial movements. **This distinction is clinically load-bearing** — a
**parvocellular reticular nucleus lesion** causes **orofacial motor
dysfunction** (impaired mastication, swallowing, facial expression,
vocalization) **without** the **full lower-motor-neuron pattern** of a
**cranial nerve motor nucleus lesion** (which would cause **flaccid
paralysis** of the specific muscles innervated by that nucleus).

**The parvocellular reticular nucleus is NOT the PPRF, the gigantocellular
reticular nucleus, the pontine nuclei, the locus coeruleus, the
parabrachial area, the superior olivary complex, the solitary nucleus, or
the superior cerebellar peduncle.** Those are **different pontine or
medullary structures** with **different functional systems**. The
parvocellular reticular nucleus is the **orofacial premotor and autonomic
relay** — a **lateral pontine tegmental structure** that **coordinates**
orofacial motor patterns and autonomic function.

**The parvocellular reticular nucleus is a MULTI-POPULATION complex.**
The **orofacial premotor neurons** project to the **cranial nerve motor
nuclei** (trigeminal motor, facial, hypoglossal, nucleus ambiguus); the
**autonomic relay neurons** project to the **hypothalamus** and the
**brainstem autonomic centers**; the **reticulospinal projection
neurons** project to the **spinal cord**. These populations are **prose**,
not structural children.

**The parvocellular reticular nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The parvocellular reticular nucleus contains **three functionally
distinct neuron populations** — documented as **prose**, not as
structural children:

*   **Orofacial premotor neurons** — the **premotor neurons** that
    **project to** the **trigeminal motor nucleus**, the **facial nerve
    nucleus**, the **hypoglossal nucleus**, and the **nucleus
    ambiguus** — they **coordinate** the **orofacial motor patterns**
    (mastication, swallowing, facial expression, vocalization). They are
    the **principal output** of the parvocellular reticular nucleus for
    **orofacial motor control** — the **neural substrate** of the
    **masticatory central pattern generator**, the **swallowing central
    pattern generator**, and the **vocalization central pattern
    generator**. **Orofacial motor coordination is the functional
    system** subserved primarily by the orofacial premotor neurons.

*   **Autonomic relay neurons** — the **neurons** that **receive**
    visceral afferents (from the **solitary nucleus** and the **medial
    parabrachial nucleus**) and **project to** the **hypothalamus** and
    the **brainstem autonomic centers** (rostral ventrolateral medulla,
    nucleus ambiguus) — they **regulate** **cardiovascular**,
    **respiratory**, and **gastrointestinal** function. They are the
    **autonomic relay** component of the parvocellular reticular
    nucleus. **Autonomic regulation is the functional system** subserved
    primarily by the autonomic relay neurons.

*   **Reticulospinal projection neurons** — the **neurons** that
    **project to** the **spinal cord** (via the **reticulospinal
    tract**) — they **modulate** **motor activity** and **autonomic
    outflow** at the **spinal level**. They are the **descending
    projection** component of the parvocellular reticular nucleus.
    **Reticulospinal modulation is the functional system** subserved
    primarily by the reticulospinal projection neurons.

**These populations are prose, not structural children.** The tree wires
the **parvocellular reticular nucleus** as a **single leaf** under the
pons container — the **orofacial premotor neurons**, **autonomic relay
neurons**, and **reticulospinal projection neurons** are **prose**, not
structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Parvocellular Reticular Nucleus / PPRF Boundary
---------------------------------------------------
This is the **sibling** boundary — **orofacial motor/autonomic vs.
horizontal saccades**:

*   **Parvocellular reticular nucleus** (this module) — the **orofacial
    premotor and autonomic relay** in the **lateral pontine tegmentum**.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/paramedian_pontine_reticular_formation/``) — the
    **horizontal saccadic burst generator** in the **paramedian pontine
    tegmentum**.

**They are DIFFERENT STRUCTURES** — different functional systems
(orofacial motor/autonomic vs. horizontal saccades) and different
anatomical locations (**lateral** parvocellular reticular nucleus vs.
**paramedian** PPRF). They are **anatomically adjacent** (both are in
the pontine tegmentum) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the parvocellular reticular
nucleus with the PPRF.

The Parvocellular Reticular Nucleus / Trigeminal Motor Nucleus Boundary
-----------------------------------------------------------------------
This is the **premotor relay vs. motor output** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **premotor
    relay** that provides premotor drive to the trigeminal motor nucleus.

*   **Trigeminal motor nucleus**
    (``.../cranial_nerve_nuclei/left/motor_trigeminal_nucleus/`` and
    ``.../right/``) — the **branchial motor** nucleus for the **muscles
    of mastication**.

**They are DIFFERENT STRUCTURES** — the **parvocellular reticular
nucleus** is **upstream premotor**; the **trigeminal motor nucleus** is
**downstream motor**. Consumers must **not** conflate the parvocellular
reticular nucleus with the trigeminal motor nucleus.

The Parvocellular Reticular Nucleus / Facial Nerve Nucleus Boundary
-------------------------------------------------------------------
This is the **premotor relay vs. motor output** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **premotor
    relay** that provides premotor drive to the facial nerve nucleus.

*   **Facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/`` and
    ``.../right/``) — the **branchial motor** nucleus for the **muscles
    of facial expression**.

**They are DIFFERENT STRUCTURES** — the **parvocellular reticular
nucleus** is **upstream premotor**; the **facial nerve nucleus** is
**downstream motor**. Consumers must **not** conflate the parvocellular
reticular nucleus with the facial nerve nucleus.

The Parvocellular Reticular Nucleus / Hypoglossal Nucleus Boundary
------------------------------------------------------------------
This is the **premotor relay vs. motor output** boundary — **pons vs.
medulla**:

*   **Parvocellular reticular nucleus** (this module) — the **pontine
    premotor relay** that provides premotor drive to the hypoglossal
    nucleus.

*   **Hypoglossal nucleus**
    (``.../medulla_oblongata/cranial_nerve_nuclei/left/hypoglossal_nucleus/``
    and ``.../right/``) — the **somatic motor** nucleus for the **tongue
    muscles**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (premotor relay vs. motor output).
Consumers must **not** conflate the parvocellular reticular nucleus with
the hypoglossal nucleus.

The Parvocellular Reticular Nucleus / Nucleus Ambiguus Boundary
---------------------------------------------------------------
This is the **premotor relay vs. motor output** boundary — **pons vs.
medulla**:

*   **Parvocellular reticular nucleus** (this module) — the **pontine
    premotor relay** that provides premotor drive to the nucleus
    ambiguus.

*   **Nucleus ambiguus**
    (``.../medulla_oblongata/cranial_nerve_nuclei/left/nucleus_ambiguus/``
    and ``.../right/``) — the **branchial motor** nucleus for the
    **pharynx** and **larynx**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different functional roles (premotor relay vs. motor output).
Consumers must **not** conflate the parvocellular reticular nucleus with
the nucleus ambiguus.

The Parvocellular Reticular Nucleus / Gigantocellular Reticular Nucleus Boundary
--------------------------------------------------------------------------------
This is the **pons vs. medulla** boundary — **small-cell vs. large-cell
reticular formation**:

*   **Parvocellular reticular nucleus** (this module) — the
    **small-cell (parvocellular) component** of the **pontine reticular
    formation**.

*   **Gigantocellular reticular nucleus (Gi)** — the **large-cell
    (gigantocellular) component** of the **medullary reticular
    formation**.

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla) and different cytoarchitectonic characteristics (small-cell vs.
large-cell). Consumers must **not** conflate the parvocellular reticular
nucleus with the gigantocellular reticular nucleus.

The Parvocellular Reticular Nucleus / Caudal and Oral Pontine Reticular Nuclei Boundary
---------------------------------------------------------------------------------------
This is the **related reticular nuclei** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **small-cell
    component** of the pontine reticular formation, specifically
    dedicated to **orofacial premotor relay and autonomic regulation**.

*   **Caudal pontine reticular nucleus (PnC)** and **oral pontine
    reticular nucleus (PnO)** — **other components** of the pontine
    reticular formation, involved in **motor control**, **sleep/wake
    regulation**, and **autonomic function**.

**They are DIFFERENT STRUCTURES** — different cytoarchitectonic
components of the pontine reticular formation, different functional
emphases. Consumers must **not** conflate the parvocellular reticular
nucleus with the caudal pontine reticular nucleus or the oral pontine
reticular nucleus.

The Parvocellular Reticular Nucleus / Pontine Nuclei Boundary
-------------------------------------------------------------
This is the **dorsal tegmental vs. basilar pons** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **dorsal
    tegmental** orofacial premotor and autonomic relay.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/left/`` and
    ``.../right/``) — the **cortico-ponto-cerebellar relay** in the
    **basilar pons**.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. orofacial motor/autonomic). Consumers must
**not** conflate the parvocellular reticular nucleus with the pontine
nuclei.

The Parvocellular Reticular Nucleus / Locus Coeruleus Boundary
--------------------------------------------------------------
This is the **anatomically adjacent** boundary — **orofacial
motor/autonomic vs. noradrenergic nucleus**:

*   **Parvocellular reticular nucleus** (this module) — the **orofacial
    premotor and autonomic relay**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic nucleus** — the **principal source of
    norepinephrine** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate, GABA, etc. vs. norepinephrine), different functional systems
(orofacial motor/autonomic vs. noradrenergic arousal). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the parvocellular reticular
nucleus with the locus coeruleus.

The Parvocellular Reticular Nucleus / Parabrachial Area Boundary
----------------------------------------------------------------
This is the **anatomically adjacent** boundary — **orofacial
motor/autonomic vs. visceral-sensory/respiratory**:

*   **Parvocellular reticular nucleus** (this module) — the **orofacial
    premotor and autonomic relay**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex**.

**They are DIFFERENT STRUCTURES** — different functional systems
(orofacial motor/autonomic vs. visceral-sensory/respiratory). They are
**anatomically adjacent** — this proximity is a **classic source of
confusion** — consumers must **not** conflate the parvocellular reticular
nucleus with the parabrachial area.

The Parvocellular Reticular Nucleus / Superior Olivary Complex Boundary
-----------------------------------------------------------------------
This is the **orofacial motor/autonomic vs. auditory** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **orofacial
    premotor and autonomic relay**.

*   **Superior olivary complex**
    (``.../pons/superior_olivary_complex/left/`` and ``.../right/``) —
    the **auditory brainstem relay** for **sound localization**.

**They are DIFFERENT STRUCTURES** — different functional systems
(orofacial motor/autonomic vs. auditory). Consumers must **not** conflate
the parvocellular reticular nucleus with the superior olivary complex.

The Parvocellular Reticular Nucleus / Solitary Nucleus Boundary
---------------------------------------------------------------
This is the **pontine relay vs. medullary upstream source** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **pontine
    orofacial premotor and autonomic relay**.

*   **Solitary nucleus** (nucleus tractus solitarius,
    ``.../medulla_oblongata/solitary_nucleus/left/`` and ``.../right/``)
    — the **medullary visceral-afferent hub** for **CN VII, IX, and X**.

**The solitary nucleus is the upstream source** of visceral afferents
that the parvocellular reticular nucleus **receives** (via the **medial
parabrachial nucleus** and **direct** projections). The **parvocellular
reticular nucleus** (here) is the **pontine autonomic relay** that
**receives** these afferents and **projects** them to the **hypothalamus**
and the **brainstem autonomic centers**. They are **DIFFERENT
STRUCTURES** — the **solitary nucleus** is **medullary** and
**upstream**; the **parvocellular reticular nucleus** is **pontine** and
**downstream**. Consumers must **not** conflate the parvocellular
reticular nucleus with the solitary nucleus.

The Parvocellular Reticular Nucleus / Superior Cerebellar Peduncle Boundary
---------------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **grey-matter
    neuron cluster** in the lateral pontine tegmentum.

*   **Superior cerebellar peduncle** (brachium conjunctivum) — the
    **white-matter tract** that carries cerebellar efferents from the
    dentate and interposed nuclei to the red nucleus and the thalamus.

**They are DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**peduncle** is white matter. Consumers must **not** conflate the
parvocellular reticular nucleus with the superior cerebellar peduncle.

The Parvocellular Reticular Nucleus / Pons Boundary
---------------------------------------------------
This is the **leaf vs. parent** boundary:

*   **Parvocellular reticular nucleus** (this module) — the **lateral
    pontine tegmental orofacial premotor and autonomic relay** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine tegmentum**,
    the **pontine nuclei**, the **corticospinal / corticobulbar
    tracts**, the **middle cerebellar peduncle**, the **cranial-nerve
    nuclei**, the **parabrachial area**, the **PPRF**, and the
    **parvocellular reticular nucleus**.

**The parvocellular reticular nucleus is a child of the pons.**
Consumers must **not** conflate the parvocellular reticular nucleus with
the **whole pons**.

The Parvocellular Reticular Nucleus / SLEA Boundary
---------------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Parvocellular reticular nucleus** (this module) — **SLEA-FREE**. It
    is **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The parvocellular reticular nucleus is NOT part of the SLEA
continuum.** It is a **pontine orofacial premotor and autonomic relay**,
and it carries **no SLEA warning**. Consumers must **not** import the
SLEA warning into the parvocellular reticular nucleus.

Function in the Human Brain
---------------------------
The parvocellular reticular nucleus's functions are **the coordination of
orofacial motor patterns** and **the autonomic regulation** — **NOT a
single unified function**:

*   **Orofacial Motor Coordination (Orofacial Premotor Neurons):** The
    **orofacial premotor neurons** **project to** the **trigeminal motor
    nucleus**, the **facial nerve nucleus**, the **hypoglossal nucleus**,
    and the **nucleus ambiguus** — they **coordinate** the **orofacial
    motor patterns** (mastication, swallowing, facial expression,
    vocalization). They are the **neural substrate** of the **masticatory
    central pattern generator**, the **swallowing central pattern
    generator**, and the **vocalization central pattern generator**. This
    is the **primary function** of the parvocellular reticular nucleus —
    the **premotor coordination** of **orofacial movements**.

*   **Autonomic Regulation (Autonomic Relay Neurons):** The **autonomic
    relay neurons** **receive** visceral afferents (from the **solitary
    nucleus** and the **medial parabrachial nucleus**) and **project to**
    the **hypothalamus** and the **brainstem autonomic centers** (rostral
    ventrolateral medulla, nucleus ambiguus) — they **regulate**
    **cardiovascular**, **respiratory**, and **gastrointestinal**
    function. This is the **autonomic regulation** function of the
    parvocellular reticular nucleus — the **pontine relay** for
    **visceral afferent integration** and **autonomic outflow**.

*   **Reticulospinal Modulation (Reticulospinal Projection Neurons):**
    The **reticulospinal projection neurons** **project to** the **spinal
    cord** (via the **reticulospinal tract**) — they **modulate**
    **motor activity** and **autonomic outflow** at the **spinal level**.
    This is the **reticulospinal modulation** function of the
    parvocellular reticular nucleus — the **descending modulation** of
    **motor and autonomic activity**.

*   **NOT a neural processor in the classical sense.** The parvocellular
    reticular nucleus is a **premotor and autonomic relay** — it
    **receives** the **orofacial motor commands** from the **cortex**
    (via the **corticobulbar** and **corticoreticular** pathways), the
    **basal ganglia**, and the **limbic system** (via the **amygdala**
    and **hypothalamus**), and it **receives** the **visceral
    afferents** from the **solitary nucleus** and the **medial
    parabrachial nucleus** — it **coordinates** the **orofacial motor
    patterns** and **autonomic responses**. The **processing** of
    orofacial motor patterns happens in the **cortex**, the **basal
    ganglia**, the **limbic system**, and the **brainstem central
    pattern generators** (including the parvocellular reticular nucleus).
    The parvocellular reticular nucleus is the **premotor relay** — the
    **pontine node** that **coordinates** the **orofacial motor output**
    and **autonomic regulation**.

**The unifying theme:** the parvocellular reticular nucleus is the
**orofacial premotor and autonomic relay** — the **pontine premotor
node** that **coordinates** the **orofacial motor patterns** (mastication,
swallowing, facial expression, vocalization) and the **autonomic
regulation** (cardiovascular, respiratory, gastrointestinal). It is a
**functionally heterogeneous complex** (orofacial premotor neurons,
autonomic relay neurons, reticulospinal projection neurons),
**SLEA-free**, and **NOT the cranial nerve motor nuclei** — the
**cranial nerve motor nuclei** are the **downstream motor output nodes**;
the **parvocellular reticular nucleus** is the **upstream premotor
relay**.

Associated Disorders
--------------------
The parvocellular reticular nucleus has **no named "parvocellular
reticular nucleus syndrome"** — its clinical associations are
**neuron-population-specific**:

*   **Parvocellular Reticular Nucleus Lesion — Orofacial Motor
    Dysfunction:** A lesion of the **parvocellular reticular nucleus**
    (e.g. **pontine stroke**, **tumor**, **demyelination**) causes
    **orofacial motor dysfunction** — **impaired mastication**,
    **impaired swallowing** (**dysphagia**), **impaired facial
    expression**, and **impaired vocalization** — because the
    **orofacial premotor relay** that **coordinates** the orofacial
    motor patterns is **disrupted**. **The pan-modal orofacial motor
    pattern** is the **substrate** of the **orofacial premotor**
    function of the parvocellular reticular nucleus.

*   **Parvocellular Reticular Nucleus Lesion — Autonomic Dysregulation:**
    A lesion of the **parvocellular reticular nucleus** causes
    **autonomic dysregulation** — **cardiovascular dysregulation**
    (impaired baroreceptor reflex, impaired cardiopulmonary integration),
    **respiratory dysregulation** (impaired respiratory rhythm), and
    **gastrointestinal dysregulation** (impaired gastrointestinal
    motility) — because the **autonomic relay** is **disrupted**.

*   **Dysphagia — Parvocellular Reticular Nucleus Involvement:**
    **Dysphagia** (difficulty swallowing) is a **common symptom** of
    **pontine lesions** involving the parvocellular reticular nucleus —
    the **swallowing central pattern generator** (which includes the
    parvocellular reticular nucleus) is **disrupted**, leading to
    **impaired coordination** of the **pharyngeal** and **laryngeal**
    phases of swallowing.

*   **Dysarthria — Parvocellular Reticular Nucleus Involvement:**
    **Dysarthria** (difficulty articulating speech) can result from
    **pontine lesions** involving the parvocellular reticular nucleus —
    the **orofacial premotor relay** that **coordinates** the
    **articulatory movements** (tongue, lips, jaw, palate) is
    **disrupted**, leading to **impaired speech articulation**.

*   **Bruxism — Parvocellular Reticular Nucleus Involvement:** **Bruxism**
    (involuntary jaw clenching or grinding) is a **movement disorder**
    that involves the **masticatory central pattern generator** — the
    parvocellular reticular nucleus is **one of the neural substrates**
    of the **masticatory central pattern generator**, and its
    **dysregulation** may **contribute** to **bruxism** (especially
    **sleep bruxism**).

*   **Sleep Bruxism — Parvocellular Reticular Nucleus Involvement:**
    **Sleep bruxism** is a **sleep-related movement disorder** that
    involves the **masticatory central pattern generator** — the
    parvocellular reticular nucleus is **one of the neural substrates**
    of the **masticatory central pattern generator**, and its
    **dysregulation** during **sleep** may **contribute** to **sleep
    bruxism** (via **brainstem arousal** and **autonomic activation**
    during **REM** and **NREM** sleep).

*   **Lateral Medullary Syndrome (Wallenberg) — Parvocellular Reticular
    Nucleus Sparing:** **Wallenberg syndrome** (lateral medullary
    lesion) **typically spares the parvocellular reticular nucleus** —
    the parvocellular reticular nucleus is a **pontine** structure,
    above the medullary level of the Wallenberg lesion. **Orofacial
    motor dysfunction** is **not** a classic Wallenberg feature.
    Consumers must **not** conflate the **parvocellular reticular
    nucleus** with the **medullary structures** involved in Wallenberg
    syndrome.

*   **Locked-in Syndrome — Parvocellular Reticular Nucleus Sparing:**
    **Locked-in syndrome** (bilateral ventral pontine lesion, e.g.
    **basilar artery occlusion**) **typically spares the parvocellular
    reticular nucleus** — the parvocellular reticular nucleus is in the
    **dorsal pontine tegmentum**, while the **ventral pons** is affected
    in locked-in syndrome. **Orofacial motor function** (mastication,
    swallowing, facial expression) is **preserved** in locked-in
    syndrome (vertical eye movements and blinking are preserved, but
    **bulbar function** is often impaired due to **corticobulbar tract**
    involvement — the **parvocellular reticular nucleus itself** may be
    spared).

*   **Central Pontine Myelinolysis (Osmotic Demyelination Syndrome) —
    Parvocellular Reticular Nucleus Involvement:** **Central pontine
    myelinolysis** (osmotic demyelination syndrome) is a **demyelinating
    disorder** of the **central pons** (often **ventral pons** but can
    extend to the **tegmentum**) — it causes **quadriparesis**,
    **pseudobulbar palsy**, and **locked-in syndrome**. The
    parvocellular reticular nucleus may be **involved** if the
    demyelination **extends to the tegmentum** — contributing to
    **orofacial motor dysfunction** and **autonomic dysregulation**.

*   **No Named "Parvocellular Reticular Nucleus Syndrome":** The
    parvocellular reticular nucleus is a **functionally defined region**
    — it has **no named clinical syndrome** of its own. Its clinical
    relevance is **orofacial-motor and autonomic-specific** — **impaired
    mastication**, **impaired swallowing**, **impaired facial
    expression**, **impaired vocalization**, **cardiovascular
    dysregulation**, **respiratory dysregulation**, and
    **gastrointestinal dysregulation**.

**What is NOT here:** The parvocellular reticular nucleus is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **trigeminal neuralgia** (trigeminal nerve root), **Bell's palsy**
(facial nerve), **Wallenberg syndrome** (lateral medulla), or
**locked-in syndrome** (bilateral ventral pons). Its clinical relevance
is **orofacial-motor and autonomic-specific**, via the **orofacial
premotor neurons**, **autonomic relay neurons**, and **reticulospinal
projection neurons** it subserves. **No named parvocellular reticular
nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **single** parvocellular reticular nucleus module. The
parvocellular reticular nuclei are **bilateral in real anatomy** (left
and right lateral pontine tegmentum), but the tree wires them as a
**single module** — and the module carries **NO warning at the module
level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **parvocellular_reticular_nucleus** module (here) is a **single
    module** that represents the **bilateral parvocellular reticular
    nucleus** (left and right lateral pontine tegmentum). The tree does
    **not** split them into left/right. Consumers must **not** assume a
    left/right split exists at the tree level — the module is a
    **single, bilateral representation**.

*   **Bilateral Orofacial Premotor and Autonomic Projections (Structural
    Fact, NOT a Lateralization Warning):** The **parvocellular reticular
    nucleus** **projects** to the **cranial nerve motor nuclei**
    (trigeminal motor, facial, hypoglossal, nucleus ambiguus) — the
    projections are **largely bilateral** (each parvocellular reticular
    nucleus projects to both the left and right cranial nerve motor
    nuclei, and the **orofacial motor patterns** require **bilateral
    coordination**). This **bilateral projection** is a **structural
    fact** of the **orofacial motor system** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **bilateral coordination** of orofacial movements (chewing, swallowing,
    speech, facial expression).

*   **Bilateral Autonomic Projections (Structural Fact, NOT a
    Lateralization Warning):** The **parvocellular reticular nucleus**
    **projects** to the **hypothalamus** and the **brainstem autonomic
    centers** — the projections are **largely bilateral**. This
    **bilateral projection** is a **structural fact** of the **autonomic
    relay system** — it is **not** a functional lateralization. It is
    the **neural substrate** of the **bilateral modulation** of
    autonomic function.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The parvocellular
    reticular nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the
    parvocellular reticular nucleus.

*   **NO Amygdala-Lateralization Warning of their own (the parvocellular
    reticular nucleus is OROFACIAL MOTOR/AUTONOMIC, not the fear-output):**
    The **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The parvocellular
    reticular nucleus is a **pontine orofacial premotor and autonomic
    relay** — consumers must **not** conflate it with the **amygdala**
    or with the **fear circuit**.

**A consumer that sees "parvocellular_reticular_nucleus" must understand
that the module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **bilateral orofacial premotor
projections** and the **bilateral autonomic projections** are
**structural facts**, not lateralizations. The parvocellular reticular
nucleus is a **strict-single module with NO warning at the module
level** — **no SLEA warning**, **no amygdala-lateralization warning**,
and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** parvocellular reticular nucleus as a **single module**
    — it does **not** import left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cranial_nerve_nuclei/``, ``.../pons/tegmentum/``,
    ``.../medulla_oblongata/``, ``.../diencephalon/``, or any other
    container. The parvocellular reticular nucleus's relationships to the
    **PPRF**, the **trigeminal motor nucleus**, the **facial nerve
    nucleus**, the **hypoglossal nucleus**, the **nucleus ambiguus**,
    the **gigantocellular reticular nucleus**, the **caudal pontine
    reticular nucleus**, the **oral pontine reticular nucleus**, the
    **pontine nuclei**, the **locus coeruleus**, the **parabrachial
    area**, the **superior olivary complex**, the **solitary nucleus**,
    the **superior cerebellar peduncle**, the **pons**, and the **SLEA
    continuum** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **orofacial premotor
    neurons**, **autonomic relay neurons**, and **reticulospinal
    projection neurons** are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    neuron-population-level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The
    **parvocellular reticular nucleus** is a **single module** that
    represents the **bilateral parvocellular reticular nucleus** — the
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **FUNCTIONALLY DEFINED REGION — NOT a cytologically distinct
    nucleus.** The **parvocellular reticular nucleus** is a
    **functionally defined group of small (parvocellular) neurons** in
    the **lateral pontine tegmentum**, defined by its **axonal
    projections** (to the cranial nerve motor nuclei and the spinal
    cord) and its **functional role** (orofacial premotor relay and
    autonomic regulation) — not by a **distinct cytoarchitectonic
    boundary**. Consumers must **not** expect a **compact, cytologically
    distinct nucleus**.
*   **PREMOTOR OROFACIAL RELAY — NOT the motor output nuclei.** The
    **parvocellular reticular nucleus** is the **premotor relay** that
    **coordinates** the **orofacial motor patterns** across multiple
    cranial nerve motor nuclei. Consumers must **not** conflate the
    parvocellular reticular nucleus with the **cranial nerve motor
    nuclei** (trigeminal motor, facial, hypoglossal, nucleus ambiguus).
*   **MULTIPLE FUNCTIONALLY DISTINCT POPULATIONS — orofacial premotor
    vs. autonomic relay vs. reticulospinal.** The **orofacial premotor
    neurons** (orofacial motor coordination), **autonomic relay
    neurons** (autonomic regulation), and **reticulospinal projection
    neurons** (reticulospinal modulation) are **prose**, not structural
    children. Consumers must **not** treat the parvocellular reticular
    nucleus as a single uniform population.
*   **NOT the PPRF — that is a SIBLING.** The **PPRF** is the
    **horizontal saccadic burst generator**; the **parvocellular
    reticular nucleus** is the **orofacial premotor and autonomic
    relay**. Consumers must **not** conflate the two.
*   **NOT the trigeminal motor nucleus, facial nerve nucleus, hypoglossal
    nucleus, or nucleus ambiguus — those are DOWNSTREAM MOTOR OUTPUT
    TARGETS.** The **parvocellular reticular nucleus** **projects to**
    these motor output nuclei. Consumers must **not** conflate the
    parvocellular reticular nucleus with any of them.
*   **NOT the gigantocellular reticular nucleus — that is a MEDULLARY
    structure.** The **gigantocellular reticular nucleus** is the
    **large-cell component** of the **medullary reticular formation**.
    Consumers must **not** conflate the parvocellular reticular nucleus
    with the gigantocellular reticular nucleus.
*   **NOT the caudal pontine reticular nucleus or the oral pontine
    reticular nucleus — those are RELATED RETICULAR NUCLEI.** They are
    **other components** of the pontine reticular formation. Consumers
    must **not** conflate the parvocellular reticular nucleus with them.
*   **NOT the pontine nuclei — those are basilar-pons
    cortico-ponto-cerebellar relays.** Consumers must **not** conflate
    the parvocellular reticular nucleus with the pontine nuclei.
*   **NOT the locus coeruleus or the parabrachial area — those are
    anatomically adjacent structures.** The **locus coeruleus** is the
    **noradrenergic nucleus**; the **parabrachial area** is the
    **visceral-sensory and respiratory-relay complex**. Consumers must
    **not** conflate the parvocellular reticular nucleus with either.
*   **NOT the superior olivary complex — that is an auditory brainstem
    relay.** Consumers must **not** conflate the parvocellular reticular
    nucleus with the superior olivary complex.
*   **NOT the solitary nucleus — that is the MEDULLARY
    visceral-afferent hub.** The **solitary nucleus** is **upstream**;
    the **parvocellular reticular nucleus** is **downstream**. Consumers
    must **not** conflate the two.
*   **NOT the superior cerebellar peduncle — that is the white-matter
    tract.** The **superior cerebellar peduncle** is white matter; the
    **parvocellular reticular nucleus** is grey matter. Consumers must
    **not** conflate the two.
*   **SLEA-FREE — no extended-amygdala relationship.** The parvocellular
    reticular nucleus is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output — the parvocellular reticular nucleus is
    OROFACIAL MOTOR/AUTONOMIC.** The **fear-output** structure is the
    **central nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**; the **fear-modulatory / extinction**
    structures are the **basomedial nuclei**. The **parvocellular
    reticular nucleus** is a **pontine orofacial premotor and autonomic
    relay** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The parvocellular reticular nucleus is a
    local leaf under the pons container, not a cross-listed leaf.
*   **No nested cross-listing.** The parvocellular reticular nucleus has
    no nested dual-framing module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import parvocellular_reticular_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.parvocellular_reticular_nucleus"
    )

**Do not** assume the parvocellular reticular nucleus is a **container**.
It is a **leaf** — the **orofacial premotor neurons**, **autonomic relay
neurons**, and **reticulospinal projection neurons** are **prose**, not
structural children.

**Do not** assume the parvocellular reticular nucleus is **bilateralized
at the tree level**. The parvocellular reticular nucleus is **bilateral
in real anatomy**, but the tree wires it as a **single module** — there
is **no left/right split**.

**Do not** assume the parvocellular reticular nucleus is a **compact,
cytologically distinct nucleus**. The **parvocellular reticular nucleus**
is a **functionally defined group of small (parvocellular) neurons** in
the **lateral pontine tegmentum** — it is defined by its **axonal
projections** (to the cranial nerve motor nuclei and the spinal cord)
and its **functional role** (orofacial premotor relay and autonomic
regulation), not by a **distinct cytoarchitectonic boundary**.

**Do not** assume the parvocellular reticular nucleus is the **PPRF**.
The **PPRF** is the **horizontal saccadic burst generator**; the
**parvocellular reticular nucleus** is the **orofacial premotor and
autonomic relay**. They are **different structures** — different
functional systems and different anatomical locations (**paramedian**
PPRF vs. **lateral** parvocellular reticular nucleus).

**Do not** assume the parvocellular reticular nucleus is the **trigeminal
motor nucleus**, the **facial nerve nucleus**, the **hypoglossal
nucleus**, or the **nucleus ambiguus**. Those are the **downstream motor
output nuclei** that the parvocellular reticular nucleus **projects to**.
They are **different structures**.

**Do not** assume the parvocellular reticular nucleus is the
**gigantocellular reticular nucleus**, the **caudal pontine reticular
nucleus**, or the **oral pontine reticular nucleus**. Those are
**related reticular nuclei** — the **gigantocellular reticular nucleus**
is a **medullary** structure; the **caudal pontine reticular nucleus**
and the **oral pontine reticular nucleus** are **other components** of
the pontine reticular formation. They are **different structures**.

**Do not** assume the parvocellular reticular nucleus is the **pontine
nuclei**, the **locus coeruleus**, the **parabrachial area**, the
**superior olivary complex**, or the **solitary nucleus**. Those are
**different pontine or medullary structures** — the **pontine nuclei**
are the **cortico-ponto-cerebellar relay**; the **locus coeruleus** is
the **noradrenergic nucleus**; the **parabrachial area** is the
**visceral-sensory and respiratory-relay complex**; the **superior
olivary complex** is the **auditory brainstem relay**; the **solitary
nucleus** is the **medullary visceral-afferent hub**.

**Do not** assume the parvocellular reticular nucleus is the **superior
cerebellar peduncle**. The **superior cerebellar peduncle** is the
**white-matter tract**; the **parvocellular reticular nucleus** is the
**grey-matter neuron cluster**. They are **different structures**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the parvocellular reticular nucleus. **The parvocellular
reticular nucleus is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT part of the fear circuit**.

Iterating the parvocellular reticular nucleus's (empty) children
(recommended consumer pattern)::

    PARVOCELLULAR_RETICULAR_NUCLEUS_CHILDREN = ()
    # The parvocellular reticular nucleus is a leaf. The orofacial
    # premotor neurons, autonomic relay neurons, and reticulospinal
    # projection neurons are prose, not modules.

Reaching the PPRF (recommended consumer pattern — the sibling)::

    # The PPRF is the HORIZONTAL SACCADIC BURST GENERATOR sibling under
    # the pons container:
    #
    #   .../pons/paramedian_pontine_reticular_formation/
    #
    # The parvocellular reticular nucleus is the OROFACIAL PREMOTOR AND
    # AUTONOMIC RELAY sibling — different functional system, different
    # anatomical location (lateral vs. paramedian).

Reaching the trigeminal motor nucleus (recommended consumer pattern — the
DOWNSTREAM MOTOR OUTPUT TARGET)::

    # The trigeminal motor nucleus is the DOWNSTREAM MOTOR OUTPUT NUCLEUS
    # for the muscles of mastication — it is the motor output target of
    # the parvocellular reticular nucleus orofacial premotor neurons:
    #
    #   .../cranial_nerve_nuclei/left/motor_trigeminal_nucleus/  (and right/)
    #
    # The parvocellular reticular nucleus is the PREMOTOR RELAY; the
    # trigeminal motor nucleus is the MOTOR OUTPUT NUCLEUS. They are
    # DIFFERENT STRUCTURES.

Reaching the facial nerve nucleus (recommended consumer pattern — the
DOWNSTREAM MOTOR OUTPUT TARGET)::

    # The facial nerve nucleus is the DOWNSTREAM MOTOR OUTPUT NUCLEUS
    # for the muscles of facial expression — it is the motor output
    # target of the parvocellular reticular nucleus orofacial premotor
    # neurons:
    #
    #   .../cranial_nerve_nuclei/left/facial_nerve_nucleus/  (and right/)
    #
    # The parvocellular reticular nucleus is the PREMOTOR RELAY; the
    # facial nerve nucleus is the MOTOR OUTPUT NUCLEUS. They are
    # DIFFERENT STRUCTURES.

Reaching the hypoglossal nucleus (recommended consumer pattern — the
DOWNSTREAM MOTOR OUTPUT TARGET)::

    # The hypoglossal nucleus is the DOWNSTREAM MOTOR OUTPUT NUCLEUS
    # for the tongue muscles — it is the motor output target of the
    # parvocellular reticular nucleus orofacial premotor neurons:
    #
    #   .../medulla_oblongata/cranial_nerve_nuclei/left/hypoglossal_nucleus/  (and right/)
    #
    # The parvocellular reticular nucleus is the PREMOTOR RELAY; the
    # hypoglossal nucleus is the MOTOR OUTPUT NUCLEUS. They are
    # DIFFERENT STRUCTURES.

Reaching the nucleus ambiguus (recommended consumer pattern — the
DOWNSTREAM MOTOR OUTPUT TARGET)::

    # The nucleus ambiguus is the DOWNSTREAM MOTOR OUTPUT NUCLEUS for the
    # pharynx and larynx — it is the motor output target of the
    # parvocellular reticular nucleus orofacial premotor neurons:
    #
    #   .../medulla_oblongata/cranial_nerve_nuclei/left/nucleus_ambiguus/  (and right/)
    #
    # The parvocellular reticular nucleus is the PREMOTOR RELAY; the
    # nucleus ambiguus is the MOTOR OUTPUT NUCLEUS. They are DIFFERENT
    # STRUCTURES.

Reaching the solitary nucleus (recommended consumer pattern — the
UPSTREAM visceral afferent source)::

    # The solitary nucleus (nucleus tractus solitarius) is the MEDULLARY
    # visceral-afferent hub that PROVIDES visceral afferents to the
    # parvocellular reticular nucleus (via the medial parabrachial
    # nucleus and direct projections):
    #
    #   .../medulla_oblongata/solitary_nucleus/left/  (and right/)
    #
    # The solitary nucleus is UPSTREAM; the parvocellular reticular
    # nucleus is DOWNSTREAM. They are DIFFERENT STRUCTURES.

Reaching the locus coeruleus (recommended consumer pattern — the adjacent
noradrenergic nucleus)::

    # The locus coeruleus is the NORADRENERGIC nucleus in the pontine
    # tegmentum — it is ANATOMICALLY ADJACENT to the parvocellular
    # reticular nucleus, but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic (source of norepinephrine);
    # the parvocellular reticular nucleus is glutamatergic/GABAergic
    # (orofacial motor/autonomic relay). They are ANATOMICALLY ADJACENT
    # but FUNCTIONALLY DISTINCT.

Reaching the parabrachial area (recommended consumer pattern — the
adjacent visceral-sensory and respiratory relay)::

    # The parabrachial area is the VISCERAL-SENSORY AND RESPIRATORY
    # RELAY in the pontine tegmentum — it is ANATOMICALLY ADJACENT to the
    # parvocellular reticular nucleus, but it is a DIFFERENT STRUCTURE:
    #
    #   .../pons/parabrachial_area/
    #
    # The parabrachial area is visceral-sensory and respiratory; the
    # parvocellular reticular nucleus is orofacial motor and autonomic.
    # They are ANATOMICALLY ADJACENT but FUNCTIONALLY DISTINCT.

Bilateral iteration (recommended consumer pattern)::

    # The parvocellular reticular nucleus is a SINGLE module (not
    # bilateralized at the tree level). The module represents the
    # BILATERAL parvocellular reticular nucleus.
    pcrt_path = (
        "hindbrain.metencephalon.pons.parvocellular_reticular_nucleus"
    )
    # resolve pcrt_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The parvocellular reticular nucleus's neuron populations are prose,
    # not modules:
    #   orofacial premotor neurons -> project to the trigeminal motor
    #                                  nucleus, facial nerve nucleus,
    #                                  hypoglossal nucleus, and nucleus
    #                                  ambiguus; coordinate orofacial motor
    #                                  patterns (mastication, swallowing,
    #                                  facial expression, vocalization)
    #   autonomic relay neurons     -> receive visceral afferents (from
    #                                  solitary nucleus and medial
    #                                  parabrachial nucleus); project to
    #                                  hypothalamus and brainstem autonomic
    #                                  centers; regulate cardiovascular,
    #                                  respiratory, and gastrointestinal
    #                                  function
    #   reticulospinal projection   -> project to spinal cord (via
    #   neurons                        reticulospinal tract); modulate
    #                                  motor activity and autonomic outflow
    #                                  at the spinal level
    #
    # Do not attempt to resolve these as sub-paths of the parvocellular
    # reticular nucleus — resolve them at the neuron-population level
    # through the references.

References
----------
*   **Canonical pontine reticular formation anatomy:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Parvocellular reticular nucleus in overview.)
*   **Parvocellular reticular nucleus — review:** Newman, D.B. (1985).
    "Distinguishing rat brainstem reticulospinal nuclei by their neuronal
    morphology." *Journal für Hirnforschung* 26:187–226. (Parvocellular
    reticular nucleus — cytoarchitectonic characterization.)
*   **Orofacial motor control — review:** Lund, J.P., Kolta, A. (2006).
    "Brainstem circuits that control mastication: do they have anything
    to say about communication?" *Journal of Communication Disorders*
    39:285–300. (Parvocellular reticular nucleus — orofacial premotor
    relay; masticatory central pattern generator.)
*   **Swallowing — review:** Jean, A. (2001). "Brain stem control of
    swallowing: neuronal network and cellular mechanisms."
    *Physiological Reviews* 81:929–969. (Parvocellular reticular nucleus
    — swallowing central pattern generator.)
*   **Vocalization — review:** Jürgens, U. (2002). "Neural pathways
    underlying vocal control." *Neuroscience & Biobehavioral Reviews*
    26:235–258. (Parvocellular reticular nucleus — vocalization central
    pattern generator.)
*   **Autonomic regulation — review:** Saper, C.B. (2002). "The central
    autonomic nervous system: conscious visceral perception and autonomic
    function." *Annual Review of Neuroscience* 25:433–469. (Parvocellular
    reticular nucleus — autonomic relay.)
*   **Reticulospinal tract — review:** Peterson, B.W., Maunz, R.A.,
    Pitts, N.G., Mackel, R.G. (1975). "Patterns of projection and
    branching of reticulospinal neurons." *Experimental Neurology*
    45:193–208. (Reticulospinal projection neurons — parvocellular
    reticular nucleus as a source.)
*   **Dysphagia — parvocellular reticular nucleus involvement:** Jean, A.
    (2001). "Brain stem control of swallowing: neuronal network and
    cellular mechanisms." *Physiological Reviews* 81:929–969. (Dysphagia
    — parvocellular reticular nucleus and the swallowing central pattern
    generator.)
*   **Dysarthria — parvocellular reticular nucleus involvement:**
    Jürgens, U. (2002). "Neural pathways underlying vocal control."
    *Neuroscience & Biobehavioral Reviews* 26:235–258. (Dysarthria —
    parvocellular reticular nucleus and the vocalization central pattern
    generator.)
*   **Bruxism — parvocellular reticular nucleus involvement:** Lavigne,
    G.J., Khoury, S., Abe, S., Yamaguchi, T., Raphael, K. (2008).
    "Bruxism physiology and pathology: an overview for clinicians."
    *Journal of Oral Rehabilitation* 35:476–494. (Bruxism — parvocellular
    reticular nucleus and the masticatory central pattern generator.)
*   **Sleep bruxism — parvocellular reticular nucleus involvement:**
    Kato, T., Thie, N.M.R., Montplaisir, J.Y., Lavigne, G.J. (2001).
    "Bruxism and orofacial movements during sleep." *Dental Clinics of
    North America* 45:657–684. (Sleep bruxism — parvocellular reticular
    nucleus and brainstem arousal.)
*   **Locked-in syndrome (contrast — parvocellular reticular nucleus
    typically spared):** Plum, F., Posner, J.B. (1980). *The Diagnosis of
    Stupor and Coma*, 3rd ed. (Locked-in syndrome — bilateral ventral
    pontine lesion; parvocellular reticular nucleus typically spared.)
*   **Wallenberg syndrome (contrast — parvocellular reticular nucleus
    typically spared):** Wallenberg, A. (1901). "Acute bulbar paralysis
    (embolic obstruction of the posterior inferior cerebellar artery)."
    *Archiv für Psychiatrie und Nervenkrankheiten* 34:923–959. (Lateral
    medullary syndrome — parvocellular reticular nucleus typically
    spared, as it is a pontine structure.)
*   **Central pontine myelinolysis (contrast — parvocellular reticular
    nucleus may be involved):** Adams, R.D., Victor, M., Mancall, E.L.
    (1959). "Central pontine myelinolysis: a hitherto undescribed disease
    occurring in alcoholic and malnourished patients." *Archives of
    Neurology and Psychiatry* 81:154–172. (Central pontine myelinolysis —
    parvocellular reticular nucleus may be involved if the demyelination
    extends to the tegmentum.)
*   **PPRF (contrast — the horizontal saccadic burst generator):**
    Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye Movements*, 5th
    ed. (PPRF — horizontal saccadic burst generator; distinct from the
    parvocellular reticular nucleus.)
*   **Gigantocellular reticular nucleus (contrast — the MEDULLARY
    large-cell reticular formation):** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Gigantocellular
    reticular nucleus — medullary large-cell reticular formation; distinct
    from the parvocellular reticular nucleus.)
*   **Pontine nuclei (contrast — the basilar-pons cortico-ponto-
    cerebellar relay):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Pontine nuclei — basilar-pons
    cortico-ponto-cerebellar relay; distinct from the parvocellular
    reticular nucleus.)
*   **Locus coeruleus (contrast — the adjacent noradrenergic nucleus):**
    Aston-Jones, G., Cohen, J.D. (2005). "An integrative theory of locus
    coeruleus-norepinephrine function: adaptive gain and optimal
    performance." *Annual Review of Neuroscience* 28:403–450. (Locus
    coeruleus — noradrenergic nucleus; anatomically adjacent to the
    parvocellular reticular nucleus but functionally distinct.)
*   **Parabrachial area (contrast — the visceral-sensory and respiratory
    relay):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Parabrachial area —
    visceral-sensory and respiratory relay; anatomically adjacent to the
    parvocellular reticular nucleus but functionally distinct.)
*   **Solitary nucleus (contrast — the MEDULLARY upstream source):**
    Saper, C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Solitary nucleus — the medullary
    visceral-afferent hub that provides visceral afferents to the
    parvocellular reticular nucleus.)
*   **Superior cerebellar peduncle (contrast — the white-matter tract):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Superior cerebellar peduncle — brachium
    conjunctivum; distinct from the parvocellular reticular nucleus.)
*   **SLEA (contrast — the parvocellular reticular nucleus is not
    included):** Alheid, G.F., Heimer, L. (1988). "New perspectives in
    basal forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA continuum
    — BNST, central nucleus, ventral pallidum, nucleus accumbens; NOT
    the parvocellular reticular nucleus.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the parvocellular reticular nucleus.)
*   NeuroNames — Parvocellular reticular nucleus; FMA — Parvocellular
    reticular nucleus.
"""