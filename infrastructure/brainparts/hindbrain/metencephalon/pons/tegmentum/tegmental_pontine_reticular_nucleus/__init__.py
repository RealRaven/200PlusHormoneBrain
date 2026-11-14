"""
infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum.tegmental_pontine_reticular_nucleus
=================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── tegmentum
                └── tegmental_pontine_reticular_nucleus   <-- THIS MODULE

**Primary synonym:** Tegmental pontine reticular nucleus; TPRN;
tegmental reticular nucleus; tegmental pontine reticular formation
(rostral portion); "the pontine tegmental motor relay"; "the pontine
reticulospinal and pontocerebellar motor relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — an **anatomically delimited
glutamatergic/GABAergic nucleus** in the **dorsal pontine tegmentum**,
**ventrolateral to the fourth ventricle** and **dorsomedial to the
superior cerebellar peduncle**, **intermingled** with the **ascending
and descending white-matter tracts** that traverse the pontine
tegmentum. It is the **pontine tegmental motor relay** — the
**neural substrate** of the **reticulospinal motor output** and the
**pontocerebellar mossy-fiber input** — and the **neural substrate** of
**locomotion**, **posture**, and **motor pattern generation** at the
**pontine level**.
**Part of:** The **tegmentum** container — specifically, the
**motor relay** component. The **tegmentum** is the **dorsal pontine
grey-matter region** — the **tree-wired container** for the six
neuromodulatory and autonomic nuclei of the dorsal pons.
**Structural parent:** ``.../tegmentum/`` → **direct child** of the
tegmentum container.
**Structural children:** **None.** This is a **leaf** module. The
**glutamatergic projection neurons**, the **GABAergic interneurons**,
and the **reticulospinal and pontocerebellar projection neurons** are
documented as **prose**, not as structural children — they are the
**functionally distinct neuron populations** within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
tegmental pontine reticular nucleus is a LEAF, not a container.** It has
**no structural children**. The **glutamatergic projection neurons**,
the **GABAergic interneurons**, and the **reticulospinal and
pontocerebellar projection neurons** are **prose** populations, not
structural children. Consumers must **not** treat the tegmental pontine
reticular nucleus as a container, and must **not** assume the neuron
populations exist as sub-modules.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the tegmental pontine reticular nucleus is a SINGLE
module at the tree level, even though the TPRN is BILATERAL in real
anatomy.** Unlike the **cranial_nerve_nuclei** module (which has
explicit ``left`` and ``right`` structural children) or the
**superior_olivary_complex** module (which has ``left`` and ``right``
sub-containers), the **tegmental_pontine_reticular_nucleus** module
(here) is a **single module** that represents the **bilateral TPRN**
(the left TPRN and the right TPRN). The tree does **not** split them
into left/right. Consumers must **not** assume a left/right split
exists at the tree level — the module is a **single, bilateral
representation**. Any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere.
**Boundary status (MOTOR RELAY NUCLEUS — NOT a neuromodulatory or
autonomic control nucleus):** **Boundary case — the tegmental pontine
reticular nucleus is a MOTOR RELAY NUCLEUS, NOT a neuromodulatory or
autonomic control nucleus.** Unlike the **locus coeruleus** (the
**noradrenergic neuromodulatory** nucleus), the **laterodorsal
tegmental nucleus** and the **pedunculopontine nucleus** (the
**cholinergic neuromodulatory** nuclei), the **nucleus incertus** (the
**relaxin-3 neuromodulatory** nucleus), and the **pontine micturition
center** (the **glutamatergic/GABAergic autonomic control** nucleus),
the **tegmental pontine reticular nucleus** (here) is a **motor relay
nucleus** — its **glutamatergic (and GABAergic)** neurons **project**
to the **spinal cord** (via the **reticulospinal tract**) and to the
**cerebellum** (via the **pontocerebellar fibers**) to **relay** the
**motor commands** that **underlie** **locomotion**, **posture**, and
**motor pattern generation** — they **do** directly **relay** motor
commands (unlike the neuromodulatory nuclei, which modulate the
excitability of their targets without relaying specific motor
commands). **This distinction is functionally load-bearing** — the TPRN
is a **throughput** nucleus (motor relay), not a **state-setting**
nucleus. Consumers must **not** conflate the tegmental pontine reticular
nucleus with the **neuromodulatory** or **autonomic control** nuclei of
the pontine tegmentum.
**Boundary status (GLUTAMATERGIC AND GABAERGIC — NOT a monoaminergic,
cholinergic, or relaxin-3-expressing nucleus):** **Boundary case — the
tegmental pontine reticular nucleus is GLUTAMATERGIC AND GABAERGIC,
NOT a monoaminergic, cholinergic, or relaxin-3-expressing nucleus.** The
**tegmental pontine reticular nucleus** neurons are **predominantly
glutamatergic** (with **GABAergic** components) — they use **glutamate**
as their **principal excitatory neurotransmitter** and **GABA** as
their **inhibitory neurotransmitter** — and they are **not**
monoaminergic (dopamine, norepinephrine, serotonin, histamine), **not**
cholinergic, and **not** relaxin-3-expressing. **The other pontine
tegmentum nuclei** use **different neurotransmitters** (noradrenaline
for the locus coeruleus; acetylcholine for the LDT and PPN; relaxin-3
for the nucleus incertus; the pontine micturition center is also
glutamatergic/GABAergic with CRF co-expression, but is an **autonomic
control** nucleus, not a **motor relay**). **This distinction is
neurochemically load-bearing** — the TPRN is a **motor relay** nucleus
that **relays** the **reticulospinal** and **pontocerebellar** motor
commands via **glutamate** (excitatory) and **GABA** (inhibitory).
Consumers must **not** conflate the TPRN with the **monoaminergic**
nuclei (the locus coeruleus, the substantia nigra, the ventral tegmental
area, the raphe nuclei), the **cholinergic** nuclei (the LDT and PPN),
the **relaxin-3** nucleus (the nucleus incertus), or the **autonomic
control** nucleus (the pontine micturition center).
**Boundary status (NOT the nucleus reticularis tegmenti pontis (NRTP) —
that is a BASILAR PONS cortico-ponto-cerebellar relay):** **Boundary
case — the tegmental pontine reticular nucleus is NOT the nucleus
reticularis tegmenti pontis (NRTP).** The **NRTP** is a **basilar pons
cortico-ponto-cerebellar relay** — it is **often** listed as a
**sub-nucleus** of the **pontine nuclei** (and it is documented as a
**prose subdivision** under the **pontine_nuclei** container in the
tree) — it **receives** the **corticopontine fibers** from the cerebral
cortex (including the **frontal eye fields** and the **somatosensory
cortex**) and **projects** to the **contralateral cerebellar cortex**
(via the **pontocerebellar fibers** and the **middle cerebellar
peduncle**) — it is **involved** in **saccade adaptation** and
**cerebellar control of eye movements**. The **tegmental pontine
reticular nucleus** (here) is a **tegmental motor relay** — it is a
**separate structural child of the pontine tegmentum container** — it
**projects** to the **spinal cord** (via the **reticulospinal tract**)
and to the **cerebellum** (via the **pontocerebellar fibers**) to
**relay** the **motor commands** that **underlie** **locomotion**,
**posture**, and **motor pattern generation**. They are **DIFFERENT
STRUCTURES** — different anatomical locations (**TPRN** is **tegmental**
— dorsolateral in the pontine tegmentum; **NRTP** is **basilar** — in
the basilar pons), different functional systems (**TPRN** is
**reticulospinal and pontocerebellar motor relay**; **NRTP** is
**cortico-ponto-cerebellar relay** for **saccade adaptation** and
**cerebellar control of eye movements**), different structural wiring
(**TPRN** is a **structural child of the pontine tegmentum container**;
**NRTP** is a **prose subdivision of the pontine nuclei container**).
**The names are similar** — this is a **classic source of confusion** —
consumers must **not** conflate the **tegmental pontine reticular
nucleus** with the **nucleus reticularis tegmenti pontis**.
**Boundary status (NOT the locus coeruleus — that is the NORADRENERGIC
neuromodulatory nucleus):** **Boundary case — the tegmental pontine
reticular nucleus is NOT the locus coeruleus (LC).** The **locus
coeruleus** (``.../tegmentum/locus_coeruleus/``) is the **noradrenergic**
nucleus — the **sole noradrenergic source** for the **forebrain** — it
is involved in **arousal**, **attention**, **stress**, **pain
modulation**, and **memory consolidation**. The **tegmental pontine
reticular nucleus** (here) is the **glutamatergic/GABAergic motor
relay** — it **relays** the **reticulospinal** and **pontocerebellar**
motor commands. They are **DIFFERENT STRUCTURES** — different
neurotransmitters (glutamate/GABA vs. noradrenaline), different
functional systems (motor relay vs. noradrenergic
arousal/attention/stress/pain/memory), different projection targets
(spinal cord and cerebellum vs. diffuse noradrenergic). They are
**anatomically adjacent** (both are in the **dorsal pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the tegmental pontine reticular nucleus
with the locus coeruleus.
**Boundary status (NOT the laterodorsal tegmental nucleus — that is the
CHOLINERGIC neuromodulatory nucleus):** **Boundary case — the
tegmental pontine reticular nucleus is NOT the laterodorsal tegmental
nucleus (LDT).** The **laterodorsal tegmental nucleus**
(``.../tegmentum/laterodorsal_tegmental_nucleus/``) is the **cholinergic**
nucleus — the **principal pontine cholinergic source** for the
**thalamus** — it is involved in **REM sleep**, **arousal**, and
**motivation**. The **tegmental pontine reticular nucleus** (here) is
the **glutamatergic/GABAergic motor relay**. They are **DIFFERENT
STRUCTURES** — different neurotransmitters (glutamate/GABA vs.
acetylcholine), different functional systems (motor relay vs.
cholinergic REM-sleep/arousal/motivation), different projection targets
(spinal cord and cerebellum vs. thalamus/basal forebrain). They are
**anatomically adjacent** (both are in the **dorsal pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the tegmental pontine reticular nucleus
with the laterodorsal tegmental nucleus.
**Boundary status (NOT the pedunculopontine nucleus — that is the
CHOLINERGIC LOCOMOTION nucleus):** **Boundary case — the tegmental
pontine reticular nucleus is NOT the pedunculopontine nucleus (PPN).**
The **pedunculopontine nucleus**
(``.../tegmentum/pedunculopontine_nucleus/``) is the **cholinergic**
(with glutamatergic and GABAergic components) nucleus — the
**mesencephalic locomotor region** (with the **cuneiform nucleus**) —
it is involved in **locomotion**, **REM sleep**, **arousal**, and
**reward** — it is **ventrolateral** at the **pontomesencephalic
junction**. The **tegmental pontine reticular nucleus** (here) is the
**glutamatergic/GABAergic motor relay** — it **relays** the
**reticulospinal** and **pontocerebellar** motor commands. **They are
both involved in locomotion** — but they are **DIFFERENT STRUCTURES** —
the **PPN** is a **cholinergic neuromodulatory nucleus** that
**participates** in the **mesencephalic locomotor region** (with the
**cuneiform nucleus**), while the **TPRN** is a **glutamatergic/
GABAergic motor relay** that **relays** the **reticulospinal** and
**pontocerebellar** motor commands (without the **cholinergic** identity
of the PPN). They are **anatomically adjacent** (both are in the
**pontine tegmentum**) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the tegmental pontine
reticular nucleus with the pedunculopontine nucleus.
**Boundary status (NOT the nucleus incertus — that is the RELAXIN-3
nucleus):** **Boundary case — the tegmental pontine reticular nucleus
is NOT the nucleus incertus.** The **nucleus incertus**
(``.../tegmentum/nucleus_incertus/``) is the **relaxin-3-expressing**
nucleus — it is involved in **stress**, **arousal**, **feeding**, and
**neuroendocrine regulation**. The **tegmental pontine reticular
nucleus** (here) is the **glutamatergic/GABAergic motor relay**. They
are **DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. relaxin-3), different functional systems (motor
relay vs. relaxin-3 stress/arousal/feeding/neuroendocrine), different
projection targets (spinal cord and cerebellum vs.
septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus).
Consumers must **not** conflate the tegmental pontine reticular nucleus
with the nucleus incertus.
**Boundary status (NOT the pontine micturition center — that is the
AUTONOMIC CONTROL nucleus):** **Boundary case — the tegmental pontine
reticular nucleus is NOT the pontine micturition center (PMC).** The
**pontine micturition center**
(``.../tegmentum/pontine_micturition_center/``) is the **autonomic
control nucleus** — it **coordinates** the **micturition reflex** (via
its **CRF-expressing and glutamatergic** projections to the **sacral
spinal cord**). The **tegmental pontine reticular nucleus** (here) is
the **glutamatergic/GABAergic motor relay** — it **relays** the
**reticulospinal** and **pontocerebellar** motor commands. They are
**DIFFERENT STRUCTURES** — different functional systems (motor relay vs.
micturition), different projection targets (spinal cord and cerebellum
vs. sacral spinal cord). **They are both glutamatergic/GABAergic** —
this shared neurotransmitter profile is a **classic source of
confusion** — consumers must **not** conflate the tegmental pontine
reticular nucleus with the pontine micturition center.
**Boundary status (NOT the PPRF — that is the HORIZONTAL SACCADIC BURST
GENERATOR):** **Boundary case — the tegmental pontine reticular nucleus
is NOT the paramedian pontine reticular formation (PPRF).** The **PPRF**
(``.../pons/paramedian_pontine_reticular_formation/``) is the
**horizontal saccadic burst generator** — it **projects** to the
**abducens nucleus** to **drive** the **horizontal saccades** — it is a
**separate structural child of the pons** (not a structural child of
the pontine tegmentum). The **tegmental pontine reticular nucleus**
(here) is the **glutamatergic/GABAergic motor relay** — it **relays**
the **reticulospinal** and **pontocerebellar** motor commands. They are
**DIFFERENT STRUCTURES** — **different functional systems** (horizontal
saccades vs. locomotion/posture/motor pattern generation), **different
structural wiring** (**PPRF** is a **separate structural child of the
pons**; **TPRN** is a **structural child of the pontine tegmentum
container**). Consumers must **not** conflate the tegmental pontine
reticular nucleus with the PPRF.
**Boundary status (NOT the parvocellular reticular nucleus — that is the
OROFACIAL PREMOTOR RELAY):** **Boundary case — the tegmental pontine
reticular nucleus is NOT the parvocellular reticular nucleus.** The
**parvocellular reticular nucleus**
(``.../pons/parvocellular_reticular_nucleus/``) is the **orofacial
premotor relay** — it **projects** to the **cranial nerve motor nuclei**
(trigeminal motor, facial, hypoglossal, nucleus ambiguus) to
**coordinate** the **orofacial motor patterns** (mastication,
swallowing, facial expression, vocalization) — it is a **separate
structural child of the pons** (not a structural child of the pontine
tegmentum). The **tegmental pontine reticular nucleus** (here) is the
**glutamatergic/GABAergic motor relay** — it **relays** the
**reticulospinal** and **pontocerebellar** motor commands. They are
**DIFFERENT STRUCTURES** — **different functional systems** (orofacial
motor vs. locomotion/posture/motor pattern generation), **different
structural wiring** (**parvocellular reticular nucleus** is a
**separate structural child of the pons**; **TPRN** is a **structural
child of the pontine tegmentum container**). Consumers must **not**
conflate the tegmental pontine reticular nucleus with the parvocellular
reticular nucleus.
**Boundary status (NOT the pontine nuclei — those are in the BASILAR
pons):** **Boundary case — the tegmental pontine reticular nucleus is
NOT the pontine nuclei.** The **pontine nuclei**
(``.../pons/pontine_nuclei/``) are the **cortico-ponto-cerebellar
relay** in the **basilar pons** — the **ventral** portion of the pons.
The **tegmental pontine reticular nucleus** (here) is the
**glutamatergic/GABAergic motor relay** in the **dorsal pontine
tegmentum**. They are **DIFFERENT PONTS SUB-DIVISIONS** — consumers must
**not** conflate the tegmental pontine reticular nucleus with the
pontine nuclei.
**Boundary status (NOT the parabrachial area, the superior olivary
complex, or the cranial nerve nuclei — those are SEPARATE structural
children of the pons):** **Boundary case — the tegmental pontine
reticular nucleus is NOT the parabrachial area, the superior olivary
complex, or the cranial nerve nuclei.** Those are **separate structural
children of the pons** — the **parabrachial area** (visceral-sensory
and respiratory relay), the **superior olivary complex** (binaural
sound-localization relay), and the **cranial nerve nuclei** (CN V, VI,
VII, VIII nuclei). The **tegmental pontine reticular nucleus** (here)
is a **glutamatergic/GABAergic motor relay** — a **structural child of
the pontine tegmentum container**. Consumers must **not** conflate the
tegmental pontine reticular nucleus with any of them.
**Boundary status (NOT the whole tegmentum container — that is the
PARENT):** **Boundary case — the tegmental pontine reticular nucleus is
NOT the whole tegmentum container; the tegmentum container is the
PARENT.** The **tegmentum** container (``.../pons/tegmentum/``) is the
**dorsal pontine grey-matter region** — the **tree-wired container**
for the **six neuromodulatory and autonomic nuclei** (locus coeruleus,
laterodorsal tegmental nucleus, nucleus incertus, pedunculopontine
nucleus, pontine micturition center, tegmental pontine reticular
nucleus). The **tegmental pontine reticular nucleus** (here) is **one
of the six structural children** of the tegmentum container. Consumers
must **not** conflate the tegmental pontine reticular nucleus with the
**whole tegmentum**.
**Boundary status (NOT the whole pons — the pons is the GRANDPARENT):**
**Boundary case — the tegmental pontine reticular nucleus is NOT the
whole pons; the pons is the GRANDPARENT.** The **pons** (``.../pons/``)
is the **whole metencephalic brainstem segment** — it contains the
**basilar pons**, the **pontine tegmentum**, the **parabrachial area**,
the **superior olivary complex**, the **cranial nerve nuclei**, the
**PPRF**, the **parvocellular reticular nucleus**, the **pontine
nuclei**, and the **six neuromodulatory and autonomic nuclei** of the
tegmentum container. The **tegmental pontine reticular nucleus** (here)
is **one of the six neuromodulatory and autonomic nuclei** only.
Consumers must **not** conflate the tegmental pontine reticular nucleus
with the **whole pons**.
**Boundary status (NOT the fourth ventricle — that is a CSF SPACE):**
**Boundary case — the tegmental pontine reticular nucleus is NOT the
fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the **CSF-filled space**
**dorsal to** the pons and **ventral to** the cerebellum. The
**tegmental pontine reticular nucleus** (here) is a **grey-matter
nucleus** that sits **ventrolateral to** the fourth ventricle (in the
**dorsal pontine tegmentum**). They are **DIFFERENT STRUCTURES** — the
**fourth ventricle** is a **fluid space**; the **tegmental pontine
reticular nucleus** is **neural tissue**. Consumers must **not**
conflate the tegmental pontine reticular nucleus with the fourth
ventricle.
**Boundary status (NOT the midbrain tegmentum or the medullary
tegmentum — those are DIFFERENT BRAINSTEM LEVELS):** **Boundary case —
the tegmental pontine reticular nucleus is NOT the midbrain tegmentum
or the medullary tegmentum.** The **midbrain tegmentum**
(``.../midbrain/tegmentum/``) is the **dorsal portion of the midbrain**
— it contains the **periaqueductal gray**, the **red nucleus**, the
**substantia nigra**, the **ventral tegmental area**, the **oculomotor
nucleus**, the **trochlear nucleus**, the **mesencephalic trigeminal
nucleus**, the **riMLF**, the **cMRF**, the **cuneiform nucleus**, and
other **midbrain structures**. The **medullary tegmentum** is the
**dorsal portion of the medulla oblongata** — it contains the
**solitary nucleus**, the **dorsal motor nucleus of the vagus**, the
**hypoglossal nucleus**, the **nucleus ambiguus**, the **inferior
olivary nucleus**, the **gigantocellular reticular nucleus**, the
**paramedian reticular nucleus**, and other **medullary structures**.
The **tegmental pontine reticular nucleus** (here) is a **specific
nucleus** in the **dorsal portion of the pons**. They are **DIFFERENT
BRAINSTEM LEVELS** — consumers must **not** conflate the tegmental
pontine reticular nucleus with the midbrain tegmentum or the medullary
tegmentum.
**Boundary status (NOT the spinal cord — that is the DOWNSTREAM EFFECTOR
TARGET):** **Boundary case — the tegmental pontine reticular nucleus is
NOT the spinal cord.** The **spinal cord** — especially the **ventral
horn** and the **intermediate zone** — is the **downstream effector
target** of the tegmental pontine reticular nucleus — it contains the
**lower motor neurons** (ventral horn) and the **spinal interneurons**
(intermediate zone) that **execute** the **motor commands** relayed by
the **reticulospinal tract**. The **tegmental pontine reticular
nucleus** (here) is the **pontine motor relay** that **projects to**
the **spinal cord**. They are **DIFFERENT STRUCTURES** — the **TPRN** is
**pontine** and **upstream**; the **spinal cord** is **spinal** and
**downstream**. Consumers must **not** conflate the tegmental pontine
reticular nucleus with the spinal cord.
**Boundary status (NOT the cerebellum — that is the DOWNSTREAM
PONTOCEREBELLAR TARGET):** **Boundary case — the tegmental pontine
reticular nucleus is NOT the cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is the **metencephalic cerebellar
half** — it is the **downstream pontocerebellar target** of the
tegmental pontine reticular nucleus — it **receives** the
**pontocerebellar mossy-fiber input** from the TPRN (and from the
**pontine nuclei** and the **NRTP**) and **integrates** it into the
**cerebellar motor control** circuits. The **tegmental pontine
reticular nucleus** (here) is the **pontine motor relay** that
**projects to** the **cerebellum**. They are **DIFFERENT STRUCTURES** —
the **TPRN** is **pontine** and **upstream**; the **cerebellum** is
**cerebellar** and **downstream**. Consumers must **not** conflate the
tegmental pontine reticular nucleus with the cerebellum.
**Boundary status (NOT the whole pontine reticular formation — that is a
CONTAINER-LEVEL CONCEPT):** **Boundary case — the tegmental pontine
reticular nucleus is NOT the whole pontine reticular formation.** The
**pontine reticular formation** — the **paramedian pontine reticular
formation (PPRF)**, the **parvocellular reticular nucleus**, the
**tegmental pontine reticular nucleus** (here), and other reticular
nuclei — is a **container-level concept** — it is the **grey-matter
region** of the **dorsal pontine tegmentum** that includes **multiple
reticular nuclei**. The **tegmental pontine reticular nucleus** (here)
is **one of the reticular nuclei** — the **motor relay** component.
Consumers must **not** conflate the tegmental pontine reticular nucleus
with the **whole pontine reticular formation** — it is one of its
constituent nuclei.
**Boundary status (MULTIPLE NEUROCHEMICALLY DISTINCT NEURON
POPULATIONS — glutamatergic, GABAergic, and reticulospinal/pontocerebellar
projection neurons):** **Boundary case — the tegmental pontine reticular
nucleus is NOT a single uniform neuron population; it contains MULTIPLE
neurochemically and projection-wise distinct populations.** The
**glutamatergic projection neurons** — the **majority** of the TPRN
neurons — they **release glutamate** at their **axon terminals** — the
**excitatory** neurotransmitter that **activates** the **spinal cord**
(via the **reticulospinal tract**) and the **cerebellum** (via the
**pontocerebellar fibers**) — they are the **principal output** of the
TPRN and the **excitatory motor relay** to the spinal cord and the
cerebellum. The **GABAergic interneurons** — the **TPRN neurons that
are GABAergic** — they **release GABA** at their **axon terminals** —
the **inhibitory** neurotransmitter that **modulates** the **TPRN's
output** and **contributes** to the **coordination** of the **motor
relay**. The **reticulospinal projection neurons** — the **TPRN neurons
that project to the spinal cord** (via the **reticulospinal tract**) —
they **relay** the **motor commands** that **underlie** **locomotion**
and **posture**. The **pontocerebellar projection neurons** — the
**TPRN neurons that project to the cerebellum** (via the
**pontocerebellar fibers**) — they **relay** the **motor commands** to
the **cerebellar motor control circuits** (via the **mossy-fiber**
input). **These populations are prose, not structural children.**
Consumers must **not** treat the tegmental pontine reticular nucleus as
a single uniform population — it is a **neurochemically and
projection-wise heterogeneous nucleus** with **distinct** sub-circuits.
**Boundary status (SLEA-FREE — the tegmental pontine reticular nucleus
is NOT an extended-amygdala component):** **Boundary case — the
tegmental pontine reticular nucleus is SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **tegmental pontine reticular
nucleus** is a **glutamatergic/GABAergic motor relay** — it is **NOT**
an extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the tegmental
pontine reticular nucleus — it is **SLEA-free**.

Overview
--------
The tegmental pontine reticular nucleus is the **pontine tegmental motor
relay** of the **pontine tegmentum** — a **neurochemically and
projection-wise heterogeneous** grey-matter nucleus in the **dorsal
pontine tegmentum**, **ventrolateral to the fourth ventricle** and
**dorsomedial to the superior cerebellar peduncle**, **intermingled**
with the **ascending and descending white-matter tracts** that traverse
the pontine tegmentum. It is a **leaf** module under the tegmentum
container, and it is the **neural substrate** of the **reticulospinal
motor output** and the **pontocerebellar mossy-fiber input** — and the
**neural substrate** of **locomotion**, **posture**, and **motor
pattern generation** at the **pontine level**.

**The tegmental pontine reticular nucleus is a LEAF, not a container.**
It has **no structural children**. The **glutamatergic projection
neurons**, the **GABAergic interneurons**, and the **reticulospinal and
pontocerebellar projection neurons** are **prose populations**, not
structural children.

**The tegmental pontine reticular nucleus is a SINGLE module at the tree
level.** The tree does **not** split the TPRN into left/right — the
module is a **single, bilateral representation**.

**The tegmental pontine reticular nucleus is a MOTOR RELAY NUCLEUS, NOT
a neuromodulatory or autonomic control nucleus.** It **projects** to the
**spinal cord** (via the **reticulospinal tract**) and to the
**cerebellum** (via the **pontocerebellar fibers**) to **relay** the
**motor commands** that **underlie** **locomotion**, **posture**, and
**motor pattern generation** — it **does** directly **relay** motor
commands (unlike the neuromodulatory nuclei, which modulate the
excitability of their targets without relaying specific motor commands).

**The tegmental pontine reticular nucleus is GLUTAMATERGIC AND
GABAERGIC, NOT a monoaminergic, cholinergic, or relaxin-3-expressing
nucleus.** The **other pontine tegmentum nuclei** use **different
neurotransmitters** (noradrenaline for the locus coeruleus;
acetylcholine for the LDT and PPN; relaxin-3 for the nucleus incertus;
the pontine micturition center is also glutamatergic/GABAergic with CRF
co-expression, but is an **autonomic control** nucleus).

**The tegmental pontine reticular nucleus is NOT the nucleus reticularis
tegmenti pontis (NRTP).** The **NRTP** is a **basilar pons
cortico-ponto-cerebellar relay** — it is **often** listed as a
**sub-nucleus** of the **pontine nuclei** (and it is documented as a
**prose subdivision** under the **pontine_nuclei** container in the
tree) — it is involved in **saccade adaptation** and **cerebellar
control of eye movements**. **The names are similar** — this is a
**classic source of confusion** — consumers must **not** conflate the
**tegmental pontine reticular nucleus** with the **nucleus reticularis
tegmenti pontis**.

**The tegmental pontine reticular nucleus is NOT the locus coeruleus,
the laterodorsal tegmental nucleus, the pedunculopontine nucleus, the
nucleus incertus, or the pontine micturition center.** Those are the
**other five** neuromodulatory and autonomic nuclei of the **pontine
tegmentum container** — different neurotransmitters, different
functional systems, different projection targets.

**The tegmental pontine reticular nucleus is NOT the PPRF, the
parvocellular reticular nucleus, the pontine nuclei, the parabrachial
area, the superior olivary complex, or the cranial nerve nuclei.**
Those are **separate structural children of the pons** — different
functional systems, different structural wiring.

**The tegmental pontine reticular nucleus is SLEA-FREE.** It is **not**
an extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The tegmental pontine reticular nucleus contains **multiple
neurochemically and projection-wise distinct neuron populations** —
documented as **prose**, not as structural children:

*   **Glutamatergic projection neurons** — the **majority** of the TPRN
    neurons — they **release glutamate** at their **axon terminals** —
    the **excitatory** neurotransmitter that **activates** the **spinal
    cord** (via the **reticulospinal tract**) and the **cerebellum**
    (via the **pontocerebellar fibers**). They are the **principal
    output** of the TPRN and the **excitatory motor relay** to the
    spinal cord and the cerebellum. **Glutamatergic motor relay is the
    functional system** subserved primarily by the glutamatergic
    projection neurons.

*   **GABAergic interneurons** — the **TPRN neurons that are
    GABAergic** — they **release GABA** at their **axon terminals** —
    the **inhibitory** neurotransmitter that **modulates** the **TPRN's
    output** and **contributes** to the **coordination** of the
    **motor relay**. **GABAergic motor relay modulation is the
    functional system** subserved primarily by the GABAergic
    interneurons.

*   **Reticulospinal projection neurons** — the **TPRN neurons that
    project to the spinal cord** (via the **reticulospinal tract**) —
    they **relay** the **motor commands** that **underlie**
    **locomotion** and **posture** to the **spinal cord**. **Reticulospinal
    motor relay is the functional system** subserved primarily by the
    reticulospinal projection neurons.

*   **Pontocerebellar projection neurons** — the **TPRN neurons that
    project to the cerebellum** (via the **pontocerebellar fibers**) —
    they **relay** the **motor commands** to the **cerebellar motor
    control circuits** (via the **mossy-fiber** input). **Pontocerebellar
    mossy-fiber relay is the functional system** subserved primarily by
    the pontocerebellar projection neurons.

**These populations are prose, not structural children.** The tree wires
the **tegmental pontine reticular nucleus** as a **single leaf** under
the tegmentum container — the **glutamatergic projection neurons**, the
**GABAergic interneurons**, the **reticulospinal projection neurons**,
and the **pontocerebellar projection neurons** are **prose**, not
structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Tegmental Pontine Reticular Nucleus / Locus Coeruleus Boundary
------------------------------------------------------------------
This is the **sibling** boundary — **motor relay vs. noradrenergic
arousal/attention/stress**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay**.

*   **Locus coeruleus** (``.../tegmentum/locus_coeruleus/``) — the
    **noradrenergic** nucleus — the **principal source of
    norepinephrine** in the brain — it is involved in **arousal**,
    **attention**, **stress**, **pain modulation**, and **memory
    consolidation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. noradrenaline), different functional systems
(motor relay vs. noradrenergic arousal/attention/stress/pain/memory),
different projection targets (spinal cord and cerebellum vs. diffuse
noradrenergic). They are **anatomically adjacent** (both are in the
**dorsal pontine tegmentum**) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the tegmental pontine
reticular nucleus with the locus coeruleus.

The Tegmental Pontine Reticular Nucleus / Laterodorsal Tegmental Nucleus Boundary
---------------------------------------------------------------------------------
This is the **sibling** boundary — **motor relay vs. cholinergic
REM-sleep/arousal**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay**.

*   **Laterodorsal tegmental nucleus**
    (``.../tegmentum/laterodorsal_tegmental_nucleus/``) — the
    **cholinergic** nucleus — the **principal pontine cholinergic
    source** for the **thalamus** — it is involved in **REM sleep**,
    **arousal**, and **motivation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. acetylcholine), different functional systems
(motor relay vs. cholinergic REM-sleep/arousal/motivation), different
projection targets (spinal cord and cerebellum vs. thalamus/basal
forebrain). They are **anatomically adjacent** (both are in the **dorsal
pontine tegmentum**) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the tegmental pontine
reticular nucleus with the laterodorsal tegmental nucleus.

The Tegmental Pontine Reticular Nucleus / Pedunculopontine Nucleus Boundary
---------------------------------------------------------------------------
This is the **sibling** boundary — **motor relay vs. cholinergic
locomotion/REM/reward**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay**.

*   **Pedunculopontine nucleus**
    (``.../tegmentum/pedunculopontine_nucleus/``) — the **cholinergic**
    (with glutamatergic and GABAergic components) nucleus — the
    **mesencephalic locomotor region** — it is involved in
    **locomotion**, **REM sleep**, **arousal**, and **reward** —
    **ventrolateral** at the **pontomesencephalic junction**.

**They are both involved in locomotion** — but they are **DIFFERENT
STRUCTURES** — the **PPN** is a **cholinergic neuromodulatory nucleus**
that **participates** in the **mesencephalic locomotor region** (with
the **cuneiform nucleus**), while the **TPRN** is a
**glutamatergic/GABAergic motor relay** that **relays** the
**reticulospinal** and **pontocerebellar** motor commands (without the
**cholinergic** identity of the PPN). They are **anatomically adjacent**
(both are in the **pontine tegmentum**) — this proximity is a **classic
source of confusion** — consumers must **not** conflate the tegmental
pontine reticular nucleus with the pedunculopontine nucleus.

The Tegmental Pontine Reticular Nucleus / Nucleus Incertus Boundary
-------------------------------------------------------------------
This is the **sibling** boundary — **motor relay vs. relaxin-3
stress/arousal/feeding**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay**.

*   **Nucleus incertus** (``.../tegmentum/nucleus_incertus/``) — the
    **relaxin-3-expressing** nucleus — it is involved in **stress**,
    **arousal**, **feeding**, and **neuroendocrine regulation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. relaxin-3), different functional systems (motor
relay vs. relaxin-3 stress/arousal/feeding/neuroendocrine), different
projection targets (spinal cord and cerebellum vs.
septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus).
Consumers must **not** conflate the tegmental pontine reticular nucleus
with the nucleus incertus.

The Tegmental Pontine Reticular Nucleus / Pontine Micturition Center Boundary
-----------------------------------------------------------------------------
This is the **sibling** boundary — **motor relay vs. autonomic control**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay** — it **relays** the
    **reticulospinal** and **pontocerebellar** motor commands.

*   **Pontine micturition center**
    (``.../tegmentum/pontine_micturition_center/``) — the **autonomic
    control nucleus** — it **coordinates** the **micturition reflex**
    (via its **CRF-expressing and glutamatergic** projections to the
    **sacral spinal cord**).

**They are DIFFERENT STRUCTURES** — different functional systems (motor
relay vs. micturition), different projection targets (spinal cord and
cerebellum vs. sacral spinal cord). **They are both
glutamatergic/GABAergic** — this shared neurotransmitter profile is a
**classic source of confusion** — consumers must **not** conflate the
tegmental pontine reticular nucleus with the pontine micturition center.

The Tegmental Pontine Reticular Nucleus / Nucleus Reticularis Tegmenti Pontis (NRTP) Boundary
--------------------------------------------------------------------------------------------
This is the **CRITICAL** boundary — **tegmental motor relay vs. basilar
pons cortico-ponto-cerebellar relay**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay** — it is a **structural child
    of the pontine tegmentum container**.

*   **Nucleus reticularis tegmenti pontis (NRTP)** — the **basilar pons
    cortico-ponto-cerebellar relay** — it is a **prose subdivision** of
    the **pontine nuclei** (``.../pons/pontine_nuclei/``) — it
    **receives** the **corticopontine fibers** from the cerebral cortex
    (including the **frontal eye fields** and the **somatosensory
    cortex**) and **projects** to the **contralateral cerebellar
    cortex** (via the **pontocerebellar fibers** and the **middle
    cerebellar peduncle**) — it is **involved** in **saccade adaptation**
    and **cerebellar control of eye movements**.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(**TPRN** is **tegmental** — dorsolateral in the pontine tegmentum;
**NRTP** is **basilar** — in the basilar pons), different functional
systems (**TPRN** is **reticulospinal and pontocerebellar motor relay**;
**NRTP** is **cortico-ponto-cerebellar relay** for **saccade adaptation**
and **cerebellar control of eye movements**), different structural
wiring (**TPRN** is a **structural child of the pontine tegmentum
container**; **NRTP** is a **prose subdivision of the pontine nuclei
container**). **The names are similar** — this is a **classic source of
confusion** — consumers must **not** conflate the **tegmental pontine
reticular nucleus** with the **nucleus reticularis tegmenti pontis**.

The Tegmental Pontine Reticular Nucleus / PPRF Boundary
-------------------------------------------------------
This is the **pons-child** boundary — **motor relay vs. horizontal
saccadic burst generator**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay**.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/paramedian_pontine_reticular_formation/``) — the
    **horizontal saccadic burst generator** — it **projects** to the
    **abducens nucleus** to **drive** the **horizontal saccades** — it
    is a **separate structural child of the pons** (not a structural
    child of the pontine tegmentum).

**They are DIFFERENT STRUCTURES** — **different functional systems**
(horizontal saccades vs. locomotion/posture/motor pattern generation),
**different structural wiring** (**PPRF** is a **separate structural
child of the pons**; **TPRN** is a **structural child of the pontine
tegmentum container**). Consumers must **not** conflate the tegmental
pontine reticular nucleus with the PPRF.

The Tegmental Pontine Reticular Nucleus / Parvocellular Reticular Nucleus Boundary
----------------------------------------------------------------------------------
This is the **pons-child** boundary — **motor relay vs. orofacial
premotor relay**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay**.

*   **Parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``) — the **orofacial
    premotor relay** — it **projects** to the **cranial nerve motor
    nuclei** (trigeminal motor, facial, hypoglossal, nucleus ambiguus)
    to **coordinate** the **orofacial motor patterns** (mastication,
    swallowing, facial expression, vocalization) — it is a **separate
    structural child of the pons** (not a structural child of the
    pontine tegmentum).

**They are DIFFERENT STRUCTURES** — **different functional systems**
(orofacial motor vs. locomotion/posture/motor pattern generation),
**different structural wiring** (**parvocellular reticular nucleus** is
a **separate structural child of the pons**; **TPRN** is a
**structural child of the pontine tegmentum container**). Consumers
must **not** conflate the tegmental pontine reticular nucleus with the
parvocellular reticular nucleus.

The Tegmental Pontine Reticular Nucleus / Parabrachial Area, Superior Olivary Complex, and Cranial Nerve Nuclei Boundary
----------------------------------------------------------------------------------------------------------------------
This is the **pons-child** boundary — **motor relay vs. other pontine
structures**:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay** — a **structural child of
    the pontine tegmentum container**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``), **superior
    olivary complex** (``.../pons/superior_olivary_complex/``), and
    **cranial nerve nuclei** (``.../pons/cranial_nerve_nuclei/``) —
    **separate structural children of the pons**.

**They are DIFFERENT STRUCTURES** — the **parabrachial area** is the
**visceral-sensory and respiratory-relay complex**, the **superior
olivary complex** is the **binaural sound-localization relay**, and the
**cranial nerve nuclei** are the **CN V, VI, VII, VIII nuclei**. The
**tegmental pontine reticular nucleus** is the **motor relay**.
Consumers must **not** conflate the tegmental pontine reticular nucleus
with any of them.

The Tegmental Pontine Reticular Nucleus / Pontine Nuclei Boundary
-----------------------------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **glutamatergic/GABAergic motor relay** in the **dorsal pontine
    tegmentum**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not**
conflate the tegmental pontine reticular nucleus with the pontine nuclei.

The Tegmental Pontine Reticular Nucleus / Whole Tegmentum Container Boundary
---------------------------------------------------------------------------
This is the **sub-nucleus vs. parent** boundary:

*   **Tegmental pontine reticular nucleus** (this module) — one of the
    **six neuromodulatory and autonomic nuclei** of the pontine
    tegmentum.

*   **Tegmentum container** (``.../pons/tegmentum/``) — the **dorsal
    pontine grey-matter region** — the **tree-wired container** for the
    **six neuromodulatory and autonomic nuclei**.

**The tegmental pontine reticular nucleus is a child of the tegmentum
container.** Consumers must **not** conflate the tegmental pontine
reticular nucleus with the **whole tegmentum**.

The Tegmental Pontine Reticular Nucleus / Whole Pons Boundary
-------------------------------------------------------------
This is the **nucleus vs. grandparent** boundary:

*   **Tegmental pontine reticular nucleus** (this module) — one of the
    **six neuromodulatory and autonomic nuclei** of the pontine
    tegmentum.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**.

**The tegmental pontine reticular nucleus is a grandchild of the pons**
(via the tegmentum container). Consumers must **not** conflate the
tegmental pontine reticular nucleus with the **whole pons**.

The Tegmental Pontine Reticular Nucleus / Fourth Ventricle Boundary
-------------------------------------------------------------------
This is the **neural tissue vs. CSF space** boundary:

*   **Tegmental pontine reticular nucleus** (this module) — a
    **grey-matter nucleus** ventrolateral to the fourth ventricle.

*   **Fourth ventricle** (``.../metencephalon/fourth_ventricle/``) — the
    **CSF-filled space** **dorsal to** the pons.

**They are DIFFERENT STRUCTURES** — the **fourth ventricle** is a
**fluid space**; the **tegmental pontine reticular nucleus** is
**neural tissue**. Consumers must **not** conflate the tegmental
pontine reticular nucleus with the fourth ventricle.

The Tegmental Pontine Reticular Nucleus / Midbrain Tegmentum and Medullary Tegmentum Boundary
--------------------------------------------------------------------------------------------
This is the **pons vs. midbrain/medulla** boundary:

*   **Tegmental pontine reticular nucleus** (this module) — a **specific
    nucleus** in the **dorsal portion of the pons**.

*   **Midbrain tegmentum** (``.../midbrain/tegmentum/``) and **medullary
    tegmentum** — the **dorsal portions** of the **midbrain** and the
    **medulla oblongata**.

**They are DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate
the tegmental pontine reticular nucleus with the midbrain tegmentum or
the medullary tegmentum.

The Tegmental Pontine Reticular Nucleus / Spinal Cord Boundary
--------------------------------------------------------------
This is the **pontine motor relay vs. spinal effector** boundary:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **pontine motor relay** — it **projects** to the **spinal cord**
    via the **reticulospinal tract**.

*   **Spinal cord** — the **downstream effector target** — it contains
    the **lower motor neurons** (ventral horn) and the **spinal
    interneurons** (intermediate zone) that **execute** the **motor
    commands** relayed by the **reticulospinal tract**.

**They are DIFFERENT STRUCTURES** — the **TPRN** is **pontine** and
**upstream**; the **spinal cord** is **spinal** and **downstream**.
Consumers must **not** conflate the tegmental pontine reticular nucleus
with the spinal cord.

The Tegmental Pontine Reticular Nucleus / Cerebellum Boundary
-------------------------------------------------------------
This is the **pontine motor relay vs. cerebellar target** boundary:

*   **Tegmental pontine reticular nucleus** (this module) — the
    **pontine motor relay** — it **projects** to the **cerebellum** via
    the **pontocerebellar fibers**.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the
    **metencephalic cerebellar half** — it is the **downstream
    pontocerebellar target** of the tegmental pontine reticular nucleus
    — it **receives** the **pontocerebellar mossy-fiber input** from
    the TPRN (and from the **pontine nuclei** and the **NRTP**) and
    **integrates** it into the **cerebellar motor control** circuits.

**They are DIFFERENT STRUCTURES** — the **TPRN** is **pontine** and
**upstream**; the **cerebellum** is **cerebellar** and **downstream**.
Consumers must **not** conflate the tegmental pontine reticular nucleus
with the cerebellum.

The Tegmental Pontine Reticular Nucleus / Whole Pontine Reticular Formation Boundary
-----------------------------------------------------------------------------------
This is the **constituent nucleus vs. whole reticular formation**
boundary:

*   **Tegmental pontine reticular nucleus** (this module) — one of the
    **reticular nuclei** — the **motor relay** component.

*   **Pontine reticular formation** — the **container-level concept** —
    the **grey-matter region** of the **dorsal pontine tegmentum** that
    includes **multiple reticular nuclei** (the **PPRF**, the
    **parvocellular reticular nucleus**, the **tegmental pontine
    reticular nucleus** (here), and other reticular nuclei).

**The tegmental pontine reticular nucleus is one of the constituent
nuclei of the pontine reticular formation.** Consumers must **not**
conflate the tegmental pontine reticular nucleus with the **whole
pontine reticular formation**.

The Tegmental Pontine Reticular Nucleus / SLEA Boundary
-------------------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Tegmental pontine reticular nucleus** (this module) — **SLEA-FREE**.
    It is **not** an extended-amygdala component, and it carries **no
    SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The tegmental pontine reticular nucleus is NOT part of the SLEA
continuum.** It is a **glutamatergic/GABAergic motor relay**, and it
carries **no SLEA warning**. Consumers must **not** import the SLEA
warning into the tegmental pontine reticular nucleus.

Function in the Human Brain
---------------------------
The tegmental pontine reticular nucleus's functions are **the pontine
motor relay for reticulospinal and pontocerebellar commands** —
**NOT a single unified function**:

*   **Reticulospinal Motor Relay (Locomotion and Posture):** The
    **reticulospinal projection neurons** of the TPRN **project** to the
    **spinal cord** (via the **reticulospinal tract**) — they **relay**
    the **motor commands** that **underlie** **locomotion** and
    **posture** to the **spinal cord**. They **activate** the **spinal
    locomotor central pattern generators** and the **spinal postural
    circuits** — they **contribute** to the **initiation**,
    **maintenance**, and **modulation** of **locomotion** and
    **posture**. **Reticulospinal motor relay is the functional system**
    subserved primarily by the reticulospinal projection neurons.

*   **Pontocerebellar Mossy-Fiber Relay (Cerebellar Motor Control):** The
    **pontocerebellar projection neurons** of the TPRN **project** to
    the **cerebellum** (via the **pontocerebellar fibers**) — they
    **relay** the **motor commands** to the **cerebellar motor control
    circuits** (via the **mossy-fiber** input). They **provide** the
    **cerebellum** with the **ongoing motor command** signals that the
    **cerebellar cortex** uses to **modulate** the **descending motor
    commands** (via the **cerebellar nuclei** and the **thalamus**) —
    they **contribute** to the **cerebellar control** of **motor
    coordination**, **timing**, and **error-based learning**.
    **Pontocerebellar mossy-fiber relay is the functional system**
    subserved primarily by the pontocerebellar projection neurons.

*   **Motor Pattern Generation (Glutamatergic and GABAergic Modulation):**
    The **glutamatergic** and **GABAergic** neurons of the TPRN
    **contribute** to the **motor pattern generation** that **underlies**
    **locomotion** — they **modulate** the **excitability** of the
    **spinal cord** and the **cerebellum** (via the **reticulospinal**
    and **pontocerebellar** projections) — they **contribute** to the
    **fine-tuning** and **coordination** of **locomotor patterns**.

*   **NOT a neural processor in the classical sense.** The TPRN is a
    **motor relay** — it **receives** afferent inputs (from the
    **cortex** — the **motor cortex**, the **premotor cortex** — the
    **basal ganglia** — the **substantia nigra pars reticulata**, the
    **globus pallidus internus**, the **subthalamic nucleus** — the
    **cerebellum** — the **fastigial nucleus** — and the **brainstem**
    — the **pontine reticular formation**, the **medullary reticular
    formation**) and **projects** to the **spinal cord** (via the
    **reticulospinal tract**) and the **cerebellum** (via the
    **pontocerebellar fibers**). The **processing** of locomotion,
    posture, and motor pattern generation happens in a **distributed**
    manner across the **TPRN**, the **spinal cord** (the **spinal
    locomotor central pattern generators** and the **spinal postural
    circuits**), the **cerebellum** (the **cerebellar motor control
    circuits**), and the **other motor systems** (the **PPN** and the
    **cuneiform nucleus** — the **mesencephalic locomotor region** —
    the **motor cortex**, the **basal ganglia**, and the **brainstem
    reticular formation**) that **interact** with the **TPRN**.

**The unifying theme:** the tegmental pontine reticular nucleus is the
**pontine tegmental motor relay** — the **neural substrate** of the
**reticulospinal motor output** and the **pontocerebellar mossy-fiber
input**. It is **glutamatergic/GABAergic** (with **reticulospinal** and
**pontocerebellar** projection neurons), **SLEA-free**, and **NOT the
nucleus reticularis tegmenti pontis (NRTP)** — the **NRTP** is the
**basilar pons cortico-ponto-cerebellar relay** (for **saccade
adaptation** and **cerebellar control of eye movements**). The **TPRN**
is the **tegmental motor relay** for **locomotion**, **posture**, and
**motor pattern generation**.

Associated Disorders
--------------------
The tegmental pontine reticular nucleus has **no named "tegmental
pontine reticular nucleus syndrome"** — its clinical associations are
**function-specific**:

*   **Gait and Postural Disorders — TPRN Involvement:** **Gait and
    postural disorders** (e.g., **Parkinson's disease gait impairment**,
    **progressive supranuclear palsy gait impairment**, **vascular
    parkinsonism**, **normal pressure hydrocephalus gait impairment**)
    have been **associated** with **dysfunction** of the **pontine
    reticular formation** (including the **TPRN**) — the **TPRN**
    **relays** the **reticulospinal motor commands** that **underlie**
    **locomotion** and **posture**, and its **dysfunction** may
    **contribute** to the **gait and postural** symptoms of these
    disorders.

*   **Locomotor Dysfunction — TPRN Involvement:** **Locomotor
    dysfunction** (e.g., **freezing of gait** in **Parkinson's
    disease**, **locomotor initiation deficits** in **progressive
    supranuclear palsy**) has been **associated** with **dysfunction**
    of the **mesencephalic locomotor region** (the **PPN** and the
    **cuneiform nucleus**) and the **pontine reticular formation**
    (including the **TPRN**) — the **TPRN** **relays** the
    **reticulospinal motor commands** to the **spinal locomotor central
    pattern generators**, and its **dysfunction** may **contribute** to
    the **locomotor** symptoms of these disorders.

*   **Cerebellar Motor Dysfunction — TPRN Involvement:** **Cerebellar
    motor dysfunction** (e.g., **ataxia**, **dysmetria**, **intention
    tremor**) has been **associated** with **dysfunction** of the
    **pontocerebellar mossy-fiber system** (including the **TPRN**) —
    the **TPRN** **relays** the **motor commands** to the **cerebellum**
    (via the **pontocerebellar fibers**), and its **dysfunction** may
    **contribute** to the **cerebellar motor** symptoms of these
    disorders.

*   **Pontine Stroke — TPRN Involvement:** A **pontine stroke** (e.g.,
    **basilar artery** perforator territory) involving the **TPRN**
    causes **gait and postural dysfunction** and **cerebellar motor
    dysfunction** — often accompanied by **other pontine signs**
    (**hemiparesis**, **facial palsy**, **abducens palsy**, **cerebellar
    ataxia**).

*   **Multiple Sclerosis — TPRN Involvement:** **Multiple sclerosis** can
    affect the **TPRN** (as a **brainstem demyelinating lesion**),
    contributing to **gait and postural dysfunction** and **cerebellar
    motor dysfunction**.

*   **No Named "TPRN Syndrome":** The tegmental pontine reticular nucleus
    is a **neurochemically and projection-wise heterogeneous motor
    relay nucleus** — it has **no named clinical syndrome** of its own.
    Its clinical relevance is **locomotion, posture, and motor pattern
    generation specific** — **gait and postural disorders**,
    **locomotor dysfunction**, **cerebellar motor dysfunction**,
    **pontine stroke**, and **multiple sclerosis** are all
    **TPRN-involved** conditions.

**What is NOT here:** The tegmental pontine reticular nucleus is **not**
the substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **fear conditioning** (amygdala — central
nucleus + basolateral nuclei), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **acoustic neuroma** (CN VIII nerve), **vestibular
neuritis** (vestibular nerve), **labyrinthitis** (inner ear), **auditory
neuropathy spectrum disorder** (cochlear nerve or hair cell),
**Wallenberg syndrome** (lateral medulla), **internuclear
ophthalmoplegia** (MLF), **horizontal gaze palsy** (PPRF or abducens
nucleus), **REM sleep behavior disorder** (REM-sleep nuclei), or
**micturition dysfunction** (PMC). Its clinical relevance is
**locomotion, posture, and motor pattern generation specific**, via the
**reticulospinal** and **pontocerebellar** motor relay it subserves.
**No named TPRN syndrome exists.**

Lateralization Notes
--------------------
This is the **single** tegmental pontine reticular nucleus module. The
TPRN is **bilateral in real anatomy** (left TPRN and right TPRN), but
the tree wires it as a **single module** — and the module carries **NO
warning at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **tegmental_pontine_reticular_nucleus** module (here) is a **single
    module** that represents the **bilateral TPRN** (the left TPRN and
    the right TPRN). The tree does **not** split them into left/right.
    Consumers must **not** assume a left/right split exists at the tree
    level — the module is a **single, bilateral representation**.

*   **Bilateral Projections (Structural Fact, NOT a Lateralization
    Warning):** The **TPRN** **projects bilaterally** to the **spinal
    cord** (via the **reticulospinal tract**) and to the **cerebellum**
    (via the **pontocerebellar fibers**) — each TPRN projects to **both**
    left and right targets. **This bilateral projection** is a
    **structural fact** of the **motor relay system** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **bilateral reticulospinal** and **pontocerebellar** motor relay
    that **underlies** **locomotion**, **posture**, and **motor pattern
    generation**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The TPRN is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the TPRN.

*   **NO Amygdala-Lateralization Warning of their own (the TPRN is
    MOTOR RELAY, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The TPRN is a **glutamatergic/GABAergic motor
    relay** — consumers must **not** conflate it with the **amygdala**
    or with the **fear circuit**.

**A consumer that sees "tegmental_pontine_reticular_nucleus" must
understand that the module is a SINGLE, BILATERAL representation** — it
is **not** a left/right split at the tree level. The **bilateral
projections** are **structural facts**, not lateralizations. The TPRN is
a **strict-single module with NO warning at the module level** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** TPRN as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/locus_coeruleus/``,
    ``.../tegmentum/laterodorsal_tegmental_nucleus/``,
    ``.../tegmentum/nucleus_incertus/``,
    ``.../tegmentum/pedunculopontine_nucleus/``,
    ``.../tegmentum/pontine_micturition_center/``,
    ``.../pons/parabrachial_area/``,
    ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../pons/pontine_nuclei/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../spinal_cord/``,
    ``.../cerebellum/``, or any other container. The TPRN's
    relationships to the **locus coeruleus**, the **laterodorsal
    tegmental nucleus**, the **pedunculopontine nucleus**, the **nucleus
    incertus**, the **pontine micturition center**, the **nucleus
    reticularis tegmenti pontis (NRTP)**, the **PPRF**, the
    **parvocellular reticular nucleus**, the **parabrachial area**, the
    **superior olivary complex**, the **cranial nerve nuclei**, the
    **pontine nuclei**, the **fourth ventricle**, the **midbrain
    tegmentum**, the **medullary tegmentum**, the **spinal cord**, the
    **cerebellum**, the **whole pontine reticular formation**, the
    **whole tegmentum container**, the **whole pons**, and the **SLEA
    continuum** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **glutamatergic
    projection neurons**, the **GABAergic interneurons**, the
    **reticulospinal projection neurons**, and the **pontocerebellar
    projection neurons** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The **TPRN**
    is a **single module** that represents the **bilateral TPRN** — the
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **MOTOR RELAY NUCLEUS — NOT a neuromodulatory or autonomic control
    nucleus.** The **TPRN** is a **motor relay** — it **relays** the
    **reticulospinal** and **pontocerebellar** motor commands. Consumers
    must **not** conflate the TPRN with the **neuromodulatory** or
    **autonomic control** nuclei.
*   **GLUTAMATERGIC AND GABAERGIC — NOT a monoaminergic, cholinergic, or
    relaxin-3-expressing nucleus.** Consumers must **not** conflate the
    TPRN with the **monoaminergic** nuclei (LC, substantia nigra, VTA,
    raphe nuclei), the **cholinergic** nuclei (LDT, PPN), the
    **relaxin-3** nucleus (nucleus incertus), or the **autonomic
    control** nucleus (PMC).
*   **NOT the nucleus reticularis tegmenti pontis (NRTP) — that is a
    BASILAR PONS cortico-ponto-cerebellar relay.** **The names are
    similar** — this is a **classic source of confusion** — consumers
    must **not** conflate the **tegmental pontine reticular nucleus**
    with the **nucleus reticularis tegmenti pontis**.
*   **NOT the locus coeruleus, the laterodorsal tegmental nucleus, the
    pedunculopontine nucleus, the nucleus incertus, or the pontine
    micturition center — those are the OTHER five neuromodulatory and
    autonomic nuclei of the pontine tegmentum.** Consumers must **not**
    conflate the TPRN with any of them.
*   **NOT the PPRF, the parvocellular reticular nucleus, the parabrachial
    area, the superior olivary complex, the cranial nerve nuclei, or the
    pontine nuclei — those are SEPARATE structural children of the
    pons.** Consumers must **not** conflate the TPRN with any of them.
*   **NOT the whole pontine reticular formation.** The **TPRN** is one of
    the **constituent nuclei** of the **pontine reticular formation**.
    Consumers must **not** conflate the TPRN with the **whole pontine
    reticular formation**.
*   **NOT the whole tegmentum container — that is the PARENT.**
    Consumers must **not** conflate the TPRN with the whole tegmentum.
*   **NOT the whole pons — that is the GRANDPARENT.** Consumers must
    **not** conflate the TPRN with the whole pons.
*   **NOT the fourth ventricle — that is a CSF SPACE.** Consumers must
    **not** conflate the TPRN with the fourth ventricle.
*   **NOT the midbrain tegmentum or the medullary tegmentum — those are
    DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate the
    TPRN with the midbrain tegmentum or the medullary tegmentum.
*   **NOT the spinal cord or the cerebellum — those are the DOWNSTREAM
    EFFECTOR TARGETS.** Consumers must **not** conflate the TPRN with
    the spinal cord or the cerebellum.
*   **MULTIPLE NEUROCHEMICALLY AND PROJECTION-WISE DISTINCT NEURON
    POPULATIONS — glutamatergic, GABAergic, reticulospinal, and
    pontocerebellar.** The **glutamatergic projection neurons**, the
    **GABAergic interneurons**, the **reticulospinal projection
    neurons**, and the **pontocerebellar projection neurons** are
    **prose**, not structural children. Consumers must **not** treat the
    TPRN as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The TPRN is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the TPRN is MOTOR RELAY.** The **fear-output**
    structure is the **central nucleus**; the **fear-learning**
    structures are the **basolateral nuclei**; the **fear-modulatory /
    extinction** structures are the **basomedial nuclei**. The **TPRN**
    is a **glutamatergic/GABAergic motor relay** — it is **not** part of
    the fear circuit.
*   **No ``AREA_PATHS`` hop.** The TPRN is a local leaf under the
    tegmentum container, not a cross-listed leaf.
*   **No nested cross-listing.** The TPRN has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum import tegmental_pontine_reticular_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.tegmentum."
        "tegmental_pontine_reticular_nucleus"
    )

**Do not** assume the TPRN is a **container**. It is a **leaf** — the
**glutamatergic projection neurons**, the **GABAergic interneurons**, the
**reticulospinal projection neurons**, and the **pontocerebellar
projection neurons** are **prose**, not structural children.

**Do not** assume the TPRN is **bilateralized at the tree level**. The
TPRN is **bilateral in real anatomy**, but the tree wires it as a
**single module** — there is **no left/right split at the module
level**.

**Do not** assume the TPRN is a **neuromodulatory or autonomic control
nucleus**. The **TPRN** is a **glutamatergic/GABAergic motor relay** —
it **relays** the **reticulospinal** and **pontocerebellar** motor
commands.

**Do not** assume the TPRN is the **nucleus reticularis tegmenti pontis
(NRTP)**. The **NRTP** is a **basilar pons cortico-ponto-cerebellar
relay** — it is involved in **saccade adaptation** and **cerebellar
control of eye movements**. The **TPRN** is a **tegmental motor relay**
— it is involved in **locomotion**, **posture**, and **motor pattern
generation**. **The names are similar** — this is a **classic source of
confusion**.

**Do not** assume the TPRN is the **locus coeruleus**, the
**laterodorsal tegmental nucleus**, the **pedunculopontine nucleus**, the
**nucleus incertus**, or the **pontine micturition center**. Those are
the **other five** neuromodulatory and autonomic nuclei of the **pontine
tegmentum container** — different neurotransmitters, different
functional systems, different projection targets.

**Do not** assume the TPRN is the **PPRF**, the **parvocellular
reticular nucleus**, the **parabrachial area**, the **superior olivary
complex**, the **cranial nerve nuclei**, or the **pontine nuclei**.
Those are **separate structural children of the pons** — different
functional systems, different structural wiring.

**Do not** assume the TPRN is the **whole pontine reticular formation**.
The **TPRN** is one of the **constituent nuclei** of the **pontine
reticular formation**.

**Do not** assume the TPRN is the **whole tegmentum** or the **whole
pons**. The **tegmentum** is the **parent**; the **pons** is the
**grandparent**.

**Do not** assume the TPRN is the **fourth ventricle**. The **fourth
ventricle** is a **CSF space**; the TPRN is **neural tissue**.

**Do not** assume the TPRN is the **midbrain tegmentum** or the
**medullary tegmentum**. Those are **different brainstem levels**.

**Do not** assume the TPRN is the **spinal cord** or the **cerebellum**.
Those are the **downstream effector targets** of the TPRN — the **TPRN**
is the **pontine motor relay**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the TPRN. **The TPRN is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the TPRN's (empty) children (recommended consumer pattern)::

    TEGMENTAL_PONTINE_RETICULAR_NUCLEUS_CHILDREN = ()
    # The TPRN is a leaf. The glutamatergic projection neurons, the
    # GABAergic interneurons, the reticulospinal projection neurons, and
    # the pontocerebellar projection neurons are prose, not modules.

Reaching the locus coeruleus (recommended consumer pattern — the
noradrenergic sibling)::

    # The locus coeruleus is the NORADRENERGIC sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The LC is noradrenergic; the TPRN is glutamatergic/GABAergic. They
    # are ANATOMICALLY ADJACENT but FUNCTIONALLY DISTINCT.

Reaching the laterodorsal tegmental nucleus (recommended consumer
pattern — the cholinergic sibling)::

    # The laterodorsal tegmental nucleus is the CHOLINERGIC sibling under
    # the tegmentum container:
    #
    #   .../pons/tegmentum/laterodorsal_tegmental_nucleus/
    #
    # The LDT is cholinergic; the TPRN is glutamatergic/GABAergic. They
    # are DIFFERENT STRUCTURES.

Reaching the pedunculopontine nucleus (recommended consumer pattern — the
cholinergic locomotion sibling)::

    # The pedunculopontine nucleus is the CHOLINERGIC LOCOMOTION sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pedunculopontine_nucleus/
    #
    # The PPN is cholinergic; the TPRN is glutamatergic/GABAergic. They
    # are DIFFERENT STRUCTURES with DIFFERENT functional systems.

Reaching the nucleus incertus (recommended consumer pattern — the
relaxin-3 sibling)::

    # The nucleus incertus is the RELAXIN-3-EXPRESSING sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/nucleus_incertus/
    #
    # The nucleus incertus is relaxin-3-expressing; the TPRN is
    # glutamatergic/GABAergic. They are DIFFERENT STRUCTURES.

Reaching the pontine micturition center (recommended consumer pattern —
the autonomic control sibling)::

    # The pontine micturition center is the AUTONOMIC CONTROL sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pontine_micturition_center/
    #
    # The PMC is an autonomic control nucleus; the TPRN is a motor relay.
    # They are BOTH glutamatergic/GABAergic — but DIFFERENT STRUCTURES
    # with DIFFERENT functional systems.

Reaching the nucleus reticularis tegmenti pontis (NRTP) (recommended
consumer pattern — the BASILAR PONS cortico-ponto-cerebellar relay,
NOT the TPRN)::

    # The nucleus reticularis tegmenti pontis (NRTP) is the BASILAR
    # PONS cortico-ponto-cerebellar relay:
    #
    #   .../pons/pontine_nuclei/left/nucleus_reticularis_tegmenti_pontis/
    #   .../pons/pontine_nuclei/right/nucleus_reticularis_tegmenti_pontis/
    #
    # The NRTP is a prose subdivision of the PONTINE NUCLEI; the TPRN is
    # a structural child of the PONTINE TEGMENTUM container. They are
    # DIFFERENT STRUCTURES with DIFFERENT anatomical locations,
    # functional systems, and structural wiring. THE NAMES ARE SIMILAR —
    # this is a classic source of confusion.

Reaching the PPRF (recommended consumer pattern — the pons-child
horizontal saccadic burst generator)::

    # The paramedian pontine reticular formation (PPRF) is the PONS-CHILD
    # horizontal saccadic burst generator:
    #
    #   .../pons/paramedian_pontine_reticular_formation/
    #
    # The PPRF is a separate structural child of the pons; the TPRN is a
    # structural child of the pontine tegmentum container. They are
    # DIFFERENT STRUCTURES with DIFFERENT functional systems.

Reaching the parvocellular reticular nucleus (recommended consumer
pattern — the pons-child orofacial premotor relay)::

    # The parvocellular reticular nucleus is the PONS-CHILD orofacial
    # premotor relay:
    #
    #   .../pons/parvocellular_reticular_nucleus/
    #
    # The parvocellular reticular nucleus is a separate structural child
    # of the pons; the TPRN is a structural child of the pontine
    # tegmentum container. They are DIFFERENT STRUCTURES with DIFFERENT
    # functional systems.

Reaching the whole tegmentum container (recommended consumer pattern —
the PARENT)::

    # The tegmentum container is the DORSAL PONTINE GREY-MATTER REGION
    # that CONTAINS the TPRN as one of its six structural children:
    #
    #   .../pons/tegmentum/
    #
    # The TPRN is a CHILD of the tegmentum container.

Reaching the whole pons (recommended consumer pattern — the
GRANDPARENT)::

    # The pons is the WHOLE METENCEPHALIC BRAINSTEM SEGMENT that CONTAINS
    # the tegmentum container:
    #
    #   .../pons/
    #
    # The TPRN is a GRANDCHILD of the pons.

Reaching the spinal cord (recommended consumer pattern — the DOWNSTREAM
EFFECTOR TARGET)::

    # The spinal cord — especially the ventral horn and the intermediate
    # zone — is the DOWNSTREAM EFFECTOR TARGET of the TPRN:
    #
    #   .../spinal_cord/gray_matter/left/ventral_horn/  (and right/)
    #   .../spinal_cord/gray_matter/left/lateral_horn/  (and right/)
    #
    # The TPRN PROJECTS TO the spinal cord via the reticulospinal tract.

Reaching the cerebellum (recommended consumer pattern — the DOWNSTREAM
PONTOCEREBELLAR TARGET)::

    # The cerebellum is the DOWNSTREAM PONTOCEREBELLAR TARGET of the
    # TPRN:
    #
    #   .../metencephalon/cerebellum/
    #
    # The TPRN PROJECTS TO the cerebellum via the pontocerebellar fibers.

Bilateral iteration (recommended consumer pattern)::

    # The TPRN is a SINGLE module (not bilateralized at the tree level).
    # The module represents the BILATERAL TPRN.
    tprn_path = (
        "hindbrain.metencephalon.pons.tegmentum."
        "tegmental_pontine_reticular_nucleus"
    )
    # resolve tprn_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The TPRN's neuron populations are prose, not modules:
    #   glutamatergic projection neurons -> release glutamate at their
    #       axon terminals; activate the spinal cord (via the
    #       reticulospinal tract) and the cerebellum (via the
    #       pontocerebellar fibers); the principal output of the TPRN
    #       and the excitatory motor relay to the spinal cord and the
    #       cerebellum
    #   GABAergic interneurons -> release GABA at their axon terminals;
    #       modulate the TPRN's output and contribute to the coordination
    #       of the motor relay
    #   reticulospinal projection neurons -> project to the spinal cord
    #       (via the reticulospinal tract); relay the motor commands that
    #       underlie locomotion and posture to the spinal cord
    #   pontocerebellar projection neurons -> project to the cerebellum
    #       (via the pontocerebellar fibers); relay the motor commands to
    #       the cerebellar motor control circuits (via the mossy-fiber
    #       input)
    #
    # Do not attempt to resolve these as sub-paths of the TPRN — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical pontine reticular formation anatomy:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Tegmental pontine reticular nucleus in overview.)
*   **Pontine reticular formation — motor relay:** Peterson, B.W.,
    Maunz, R.A., Pitts, N.G., Mackel, R.G. (1975). "Patterns of
    projection and branching of reticulospinal neurons." *Experimental
    Neurology* 45:193–208. (Reticulospinal neurons of the pontine
    reticular formation — the tegmental pontine reticular nucleus as a
    source.)
*   **Reticulospinal tract — motor control:** Lemon, R.N. (2008).
    "Descending pathways in motor control." *Annual Review of
    Neuroscience* 31:195–218. (Reticulospinal tract — motor control;
    the pontine reticular formation and the TPRN.)
*   **Pontocerebellar mossy-fiber system:** Brodal, P., Bjaalie, J.G.
    (1992). "Organization of the pontine nuclei." *Neuroscience
    Research* 13:83–118. (Pontocerebellar mossy-fiber system — the
    pontine nuclei, the NRTP, and the TPRN as sources.)
*   **Locomotion — brainstem control:** Shik, M.L., Severin, F.V.,
    Orlovskii, G.N. (1966). "Control of walking and running by means of
    electrical stimulation of the mid-brain." *Biophysics*
    11:756–765. (Mesencephalic locomotor region — the PPN and the
    cuneiform nucleus; the pontine reticular formation — the TPRN — as
    a downstream relay.)
*   **Posture — brainstem control:** Takakusaki, K., Habaguchi, T.,
    Ohtinata-Sugimoto, J., Saitoh, K., Sakamoto, T. (2003). "Basal
    ganglia efferents to the brainstem centers controlling postural
    muscle tone and locomotion: a new concept for understanding motor
    disorders in basal ganglia dysfunction." *Neuroscience Research*
    47:219–233. (Pontine reticular formation — postural muscle tone and
    locomotion; the TPRN as a relay.)
*   **Gait and postural disorders — TPRN involvement:** Hirsch, E.C.,
    Graybiel, A.M., Duyckaerts, C., Javoy-Agid, F. (1987). "Neuronal
    loss in the pedunculopontine tegmental nucleus in Parkinson disease
    and in progressive supranuclear palsy." *Proceedings of the National
    Academy of Sciences* 84:5976–5980. (Gait and postural disorders —
    pontine reticular formation involvement, including the TPRN.)
*   **Cerebellar motor dysfunction — TPRN involvement:** Manto, M.,
    Gruol, D.L., Schmahmann, J.D., Koibuchi, N., Rossi, F. (eds.)
    (2013). *Handbook of the Cerebellum and Cerebellar Disorders*.
    (Cerebellar motor dysfunction — pontocerebellar mossy-fiber system
    involvement, including the TPRN.)
*   **Pontine stroke — TPRN involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — pontine tegmentum involvement,
    including the TPRN.)
*   **Locus coeruleus (contrast — the NORADRENERGIC neuromodulatory
    sibling):** Aston-Jones, G., Cohen, J.D. (2005). "An integrative
    theory of locus coeruleus-norepinephrine function: adaptive gain
    and optimal performance." *Annual Review of Neuroscience*
    28:403–450. (Locus coeruleus — noradrenergic neuromodulatory
    nucleus; sibling of the TPRN.)
*   **Laterodorsal tegmental nucleus (contrast — the CHOLINERGIC
    neuromodulatory sibling):** Mesulam, M.M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the rat:
    an overview based on an alternative nomenclature (Ch1-Ch6)."
    *Neuroscience* 10:1185–1201. (LDT — cholinergic neuromodulatory
    nucleus; sibling of the TPRN.)
*   **Pedunculopontine nucleus (contrast — the CHOLINERGIC LOCOMOTION
    sibling):** Garcia-Rill, E. (1991). "The pedunculopontine nucleus."
    *Progress in Neurobiology* 36:363–389. (PPN — cholinergic
    locomotion and REM-sleep nucleus; sibling of the TPRN.)
*   **Nucleus incertus (contrast — the RELAXIN-3 sibling):** Ryan, P.J.,
    Ma, S., Olucha-Bordonau, F.E., Gundlach, A.L. (2011). "Nucleus
    incertus — an emerging role in the behavioural actions of
    relaxin-3." *British Journal of Pharmacology* 162:1115–1126.
    (Nucleus incertus — relaxin-3 stress, arousal, and feeding; sibling
    of the TPRN.)
*   **Pontine micturition center (contrast — the AUTONOMIC CONTROL
    sibling):** Barrington, F.J.F. (1925). "The effect of lesions of the
    hind- and mid-brain on micturition in the cat." *Quarterly Journal
    of Experimental Physiology* 15:81–102. (Pontine micturition center —
    micturition control; sibling of the TPRN.)
*   **Nucleus reticularis tegmenti pontis (contrast — the BASILAR PONS
    cortico-ponto-cerebellar relay; NOT the TPRN):** Thier, P., Möck,
    M. (2006). "The oculomotor role of the pontine nuclei and the
    nucleus reticularis tegmenti pontis." *Progress in Brain Research*
    151:293–320. (NRTP — basilar pons cortico-ponto-cerebellar relay;
    distinct from the TPRN.)
*   **PPRF (contrast — a separate pons child):** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (PPRF —
    horizontal saccadic burst generator; distinct from the TPRN.)
*   **Parvocellular reticular nucleus (contrast — a separate pons
    child):** Brodal, A. (2010). *The Central Nervous System: Structure
    and Function*, 4th ed. (Parvocellular reticular nucleus — orofacial
    premotor and autonomic relay; distinct from the TPRN.)
*   **Parabrachial area (contrast — a separate pons child):** Saper,
    C.B. (2002). "The central autonomic nervous system: conscious
    visceral perception and autonomic function." *Annual Review of
    Neuroscience* 25:433–469. (Parabrachial area — visceral-sensory and
    respiratory relay; distinct from the pontine tegmentum container in
    the tree.)
*   **Superior olivary complex (contrast — a separate pons child):**
    Pickles, J.O. (2015). *An Introduction to the Physiology of
    Hearing*, 4th ed. (Superior olivary complex — binaural
    sound-localization relay; distinct from the pontine tegmentum
    container in the tree.)
*   **Cranial nerve nuclei (contrast — a separate pons child):** Haines,
    D.E. (2012). *Neuroanatomy: An Atlas of Structures, Sections, and
    Systems*, 8th ed. (Cranial nerve nuclei of the pons — distinct from
    the pontine tegmentum container in the tree.)
*   **Pontine nuclei (contrast — in the BASILAR pons):** Brodal, A.
    (2010). *The Central Nervous System: Structure and Function*, 4th
    ed. (Pontine nuclei — cortico-ponto-cerebellar relay in the basilar
    pons; distinct from the TPRN.)
*   **Fourth ventricle (contrast — a CSF space):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Fourth ventricle — CSF space dorsal to the pons; distinct from the
    TPRN.)
*   **Midbrain tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Midbrain tegmentum — dorsal midbrain; distinct
    from the pontine tegmentum.)
*   **Medullary tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary tegmentum — dorsal medulla; distinct
    from the pontine tegmentum.)
*   **SLEA (contrast — the TPRN is not included):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain organization
    of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the TPRN.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the TPRN.)
*   NeuroNames — Tegmental reticular nucleus; FMA — Tegmental reticular
    nucleus.
"""