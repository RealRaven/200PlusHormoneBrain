"""
infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum.pedunculopontine_nucleus
=======================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── tegmentum
                └── pedunculopontine_nucleus   <-- THIS MODULE

**Primary synonym:** Pedunculopontine nucleus; PPN; pedunculopontine
tegmental nucleus; PPTg; PPT; "the pontomesencephalic cholinergic
locomotion nucleus"; "the mesencephalic locomotor region (with the
cuneiform nucleus)."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — an **anatomically delimited
cholinergic (with glutamatergic and GABAergic components) nucleus** at
the **pontomesencephalic junction** (the **caudal midbrain / rostral
pons** transition), **ventrolateral** in the **pontine tegmentum**,
**lateral to the superior cerebellar peduncle** and **medial to the
medial lemniscus**. It is the **pontomesencephalic cholinergic
locomotion nucleus** — the **principal cholinergic source** for the
**basal ganglia** and a **major cholinergic source** for the
**thalamus**, the **brainstem**, and the **spinal cord** — and the
**neural substrate** of the **locomotion**, **REM-sleep**, **arousal**,
and **reward** functions of the **mesencephalic locomotor region**
(with the **cuneiform nucleus**).
**Part of:** The **tegmentum** container — specifically, the
**neuromodulatory (cholinergic and glutamatergic/GABAergic locomotion)**
component. The **tegmentum** is the **dorsal pontine grey-matter
region** — the **tree-wired container** for the six neuromodulatory and
autonomic nuclei of the dorsal pons.
**Structural parent:** ``.../tegmentum/`` → **direct child** of the
tegmentum container.
**Structural children:** **None.** This is a **leaf** module. The
**cholinergic principal neurons**, the **glutamatergic neurons**, and
the **GABAergic neurons** are documented as **prose**, not as structural
children — they are the **functionally distinct neuron populations**
within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
pedunculopontine nucleus is a LEAF, not a container.** It has **no
structural children**. The **cholinergic principal neurons**, the
**glutamatergic neurons**, and the **GABAergic neurons** are **prose**
populations, not structural children. Consumers must **not** treat the
pedunculopontine nucleus as a container, and must **not** assume the
neuron populations exist as sub-modules.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the pedunculopontine nucleus is a SINGLE module at the
tree level, even though the PPN is BILATERAL in real anatomy.** Unlike
the **cranial_nerve_nuclei** module (which has explicit ``left`` and
``right`` structural children) or the **superior_olivary_complex**
module (which has ``left`` and ``right`` sub-containers), the
**pedunculopontine_nucleus** module (here) is a **single module** that
represents the **bilateral PPN** (the left PPN and the right PPN). The
tree does **not** split them into left/right. Consumers must **not**
assume a left/right split exists at the tree level — the module is a
**single, bilateral representation**. Any lateralization is documented
**here, in the Lateralization Notes**, not imported from elsewhere.
**Boundary status (PONTOMESENCEPHALIC JUNCTION — NOT a purely pontine
nucleus):** **Boundary case — the pedunculopontine nucleus is a
PONTOMESENCEPHALIC JUNCTION nucleus, NOT a purely pontine nucleus.** The
**PPN** straddles the **boundary** between the **caudal midbrain** and
the **rostral pons** — its **cholinergic neurons** are **concentrated**
at the **pontomesencephalic junction**, and it is **often** considered
a **"pontine"** nucleus in the **pontine tegmentum container** (here),
but it is **also** often classified as a **"midbrain"** nucleus in the
**midbrain tegmentum** literature. **This pontomesencephalic location**
is a **classic source of confusion** — consumers must **not** assume the
PPN is a **purely pontine** nucleus, and must **not** conflate it with
the **purely pontine** nuclei (the locus coeruleus, the laterodorsal
tegmental nucleus, the nucleus incertus, the pontine micturition center,
and the tegmental pontine reticular nucleus). The **tree** places the
PPN in the **pontine tegmentum container** — but consumers must **not**
assume the tree's container placement overrides the **pontomesencephalic
anatomical reality**.
**Boundary status (CHOLINERGIC NEUROMODULATORY NUCLEUS — NOT a motor or
sensory relay):** **Boundary case — the pedunculopontine nucleus is a
CHOLINERGIC NEUROMODULATORY nucleus, NOT a motor or sensory relay.**
Unlike the **cranial nerve motor nuclei** (branchial or somatic motor
relays) or the **sensory nuclei** (e.g., the cochlear nuclei, the
trigeminal nuclei), the **pedunculopontine nucleus** (here) is a
**neuromodulatory nucleus** — its **cholinergic (with glutamatergic and
GABAergic components)** neurons **project diffusely** to the **basal
ganglia**, the **thalamus**, the **hypothalamus**, the **brainstem**,
and the **spinal cord** to **modulate** the **excitability** of their
targets — they **do not** directly **relay** motor commands or
**transmit** sensory information. **This distinction is functionally
load-bearing** — the PPN is a **state-setting** nucleus (locomotion,
REM sleep, arousal, reward), not a **throughput** nucleus — but its
**locomotion function** is **closer** to a **motor function** than the
**purely neuromodulatory** functions of the **locus coeruleus** or the
**laterodorsal tegmental nucleus**. **The PPN is a "neuromodulatory
nucleus" that ALSO serves as a "motor region"** (the **mesencephalic
locomotor region**). Consumers must **not** conflate the PPN with a
**purely** motor or sensory relay — but they must **also** recognize its
**motor-region** role.
**Boundary status (CHOLINERGIC — NOT noradrenergic, dopaminergic,
serotonergic, or relaxin-3):** **Boundary case — the pedunculopontine
nucleus is CHOLINERGIC, NOT noradrenergic, dopaminergic, serotonergic, or
relaxin-3-expressing.** The **pedunculopontine nucleus** neurons are
**cholinergic** — they synthesize **acetylcholine** (via the **choline
acetyltransferase (ChAT)** pathway) and release it as their **primary
neurotransmitter**. The **cholinergic** identity of the PPN is its
**defining neurochemical signature** — the **other pontine tegmentum
nuclei** use **different neurotransmitters** (noradrenaline for the
locus coeruleus; **also acetylcholine** for the laterodorsal tegmental
nucleus; relaxin-3 for the nucleus incertus; the pontine micturition
center and the tegmental pontine reticular nucleus are
**glutamatergic/GABAergic**). **This distinction is neurochemically
load-bearing** — the PPN is one of the **two principal cholinergic
sources** for the **forebrain** (the **other** being the **laterodorsal
tegmental nucleus**) — and its **cholinergic identity** is the **basis**
of its **locomotion, REM-sleep, arousal, and reward** functions.
Consumers must **not** conflate the PPN with the **noradrenergic**
nucleus (the locus coeruleus), the **dopaminergic** nuclei (the
substantia nigra and the ventral tegmental area), the **serotonergic**
nuclei (the raphe nuclei), or the **relaxin-3** nucleus (the nucleus
incertus).
**Boundary status (NOT the laterodorsal tegmental nucleus — that is the
OTHER cholinergic neuromodulatory nucleus):** **Boundary case — the
pedunculopontine nucleus is NOT the laterodorsal tegmental nucleus
(LDT).** The **laterodorsal tegmental nucleus**
(``.../tegmentum/laterodorsal_tegmental_nucleus/``) is the **cholinergic**
nucleus — the **principal pontine cholinergic source** for the
**thalamus** and a **major cholinergic source** for the **basal
forebrain** — it is involved in **REM sleep**, **arousal**, and
**motivation** — it is **dorsomedial** in the pontine tegmentum. The
**pedunculopontine nucleus** (here) is the **cholinergic** nucleus — the
**principal cholinergic source** for the **basal ganglia** and a
**major cholinergic source** for the **thalamus**, the **brainstem**,
and the **spinal cord** — it is involved in **locomotion**, **REM
sleep**, **arousal**, and **reward** — it is **ventrolateral** at the
**pontomesencephalic junction**. They are **DIFFERENT STRUCTURES** —
different functional emphases (locomotion/REM/reward for the PPN vs.
REM/arousal/motivation for the LDT) and different **anatomical
locations** (the LDT is **dorsomedial**; the PPN is **ventrolateral**).
**They are both cholinergic** — this shared neurotransmitter is a
**classic source of confusion** — consumers must **not** conflate the
pedunculopontine nucleus with the laterodorsal tegmental nucleus. They
are **functionally coupled** — the LDT and the PPN are **both
cholinergic REM-sleep and arousal nuclei** — but they are **different
structures** with **different anatomical locations** and **different
functional emphases**.
**Boundary status (NOT the locus coeruleus — that is the NORADRENERGIC
neuromodulatory nucleus):** **Boundary case — the pedunculopontine
nucleus is NOT the locus coeruleus (LC).** The **locus coeruleus**
(``.../tegmentum/locus_coeruleus/``) is the **noradrenergic** nucleus —
the **sole noradrenergic source** for the **forebrain** — it is
involved in **arousal**, **attention**, **stress**, **pain
modulation**, and **memory consolidation**. The **pedunculopontine
nucleus** (here) is the **cholinergic** nucleus — it is involved in
**locomotion**, **REM sleep**, **arousal**, and **reward**. They are
**DIFFERENT STRUCTURES** — different neurotransmitters (acetylcholine
vs. noradrenaline), different functional systems (cholinergic
locomotion/REM-sleep/arousal/reward vs. noradrenergic
arousal/attention/stress/pain/memory), different anatomical locations
(the LC is **dorsomedial** at the lateral fourth-ventricle wall; the PPN
is **ventrolateral** at the pontomesencephalic junction). Consumers must
**not** conflate the pedunculopontine nucleus with the locus coeruleus.
**Boundary status (NOT the nucleus incertus — that is the RELAXIN-3
nucleus):** **Boundary case — the pedunculopontine nucleus is NOT the
nucleus incertus.** The **nucleus incertus**
(``.../tegmentum/nucleus_incertus/``) is the **relaxin-3-expressing**
nucleus — it is involved in **stress**, **arousal**, **feeding**, and
**neuroendocrine regulation**. The **pedunculopontine nucleus** (here) is
the **cholinergic** nucleus. They are **DIFFERENT STRUCTURES** —
different neurotransmitters (acetylcholine vs. relaxin-3), different
functional systems (cholinergic locomotion/REM-sleep/arousal/reward vs.
relaxin-3 stress/arousal/feeding/neuroendocrine), different projection
targets (basal ganglia/thalamus/brainstem/spinal cord vs.
septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus).
Consumers must **not** conflate the pedunculopontine nucleus with the
nucleus incertus.
**Boundary status (NOT the pontine micturition center — that is the
MICTURITION nucleus):** **Boundary case — the pedunculopontine nucleus
is NOT the pontine micturition center (Barrington's nucleus).** The
**pontine micturition center**
(``.../tegmentum/pontine_micturition_center/``) is the **micturition
control center** — it **coordinates** the **micturition reflex**
(bladder contraction and sphincter relaxation). The
**pedunculopontine nucleus** (here) is the **cholinergic** nucleus.
They are **DIFFERENT STRUCTURES** — different functional systems
(cholinergic locomotion/REM-sleep/arousal/reward vs. micturition),
different projection targets (basal ganglia/thalamus/brainstem/spinal
cord vs. sacral spinal cord). Consumers must **not** conflate the
pedunculopontine nucleus with the pontine micturition center.
**Boundary status (NOT the tegmental pontine reticular nucleus — that is
the MOTOR RELAY nucleus):** **Boundary case — the pedunculopontine
nucleus is NOT the tegmental pontine reticular nucleus.** The
**tegmental pontine reticular nucleus**
(``.../tegmentum/tegmental_pontine_reticular_nucleus/``) is a **motor
relay** — it **projects** to the **spinal cord** (via the
**reticulospinal tract**) and to the **cerebellum** (via the
**pontocerebellar fibers**) — it is involved in **locomotion**,
**posture**, and **motor pattern generation**. The
**pedunculopontine nucleus** (here) is the **cholinergic** nucleus — it
is involved in **locomotion**, **REM sleep**, **arousal**, and
**reward**. **They are both involved in locomotion** — but they are
**DIFFERENT STRUCTURES** — the **tegmental pontine reticular nucleus**
is a **purely motor relay** (reticulospinal and pontocerebellar
projections), while the **pedunculopontine nucleus** is a
**cholinergic neuromodulatory nucleus** that **participates** in the
**mesencephalic locomotor region** (with the **cuneiform nucleus**) and
**also** serves **REM-sleep**, **arousal**, and **reward** functions.
Consumers must **not** conflate the pedunculopontine nucleus with the
tegmental pontine reticular nucleus.
**Boundary status (NOT the cuneiform nucleus — that is the OTHER
mesencephalic locomotor region component):** **Boundary case — the
pedunculopontine nucleus is NOT the cuneiform nucleus.** The **cuneiform
nucleus** (midbrain) is the **other component** of the **mesencephalic
locomotor region** — it is a **glutamatergic** nucleus that **projects**
to the **ventral spinal cord** (via the **reticulospinal tract**) to
**initiate** and **maintain** **locomotion**. The **pedunculopontine
nucleus** (here) is the **cholinergic** nucleus — it is **one of the
two** components of the **mesencephalic locomotor region** (with the
**cuneiform nucleus**), and it is involved in **locomotion**, **REM
sleep**, **arousal**, and **reward**. They are **DIFFERENT STRUCTURES**
— different neurotransmitters (acetylcholine vs. glutamate), different
functional emphases (the cuneiform nucleus is **primarily** locomotion;
the PPN is **locomotion + REM sleep + arousal + reward**), different
anatomical locations (the cuneiform nucleus is **midbrain**; the PPN is
**pontomesencephalic**). Consumers must **not** conflate the
pedunculopontine nucleus with the cuneiform nucleus — but they must
**recognize** that the **two** together constitute the **mesencephalic
locomotor region**.
**Boundary status (NOT the parabrachial area — that is a SEPARATE
structural child of the pons):** **Boundary case — the
pedunculopontine nucleus is NOT the parabrachial area.** The
**parabrachial area** (``.../pons/parabrachial_area/``) is the
**visceral-sensory and respiratory-relay complex** — it is a
**separate structural child of the pons**, **not** a structural child
of the pontine tegmentum, **even though** it is **anatomically
located** in the **pontine tegmentum**. The **pedunculopontine
nucleus** (here) is a **cholinergic neuromodulatory nucleus** — a
**structural child of the pontine tegmentum container**. Consumers must
**not** conflate the pedunculopontine nucleus with the parabrachial
area.
**Boundary status (NOT the superior olivary complex, the cranial nerve
nuclei, the PPRF, or the parvocellular reticular nucleus — those are
SEPARATE structural children of the pons):** **Boundary case — the
pedunculopontine nucleus is NOT the superior olivary complex, the
cranial nerve nuclei, the PPRF, or the parvocellular reticular
nucleus.** Those are **separate structural children of the pons** — the
**superior olivary complex** (binaural sound-localization relay), the
**cranial nerve nuclei** (CN V, VI, VII, VIII nuclei), the **PPRF**
(horizontal saccadic burst generator), and the **parvocellular
reticular nucleus** (orofacial premotor and autonomic relay). The
**pedunculopontine nucleus** (here) is a **cholinergic neuromodulatory
nucleus** — a **structural child of the pontine tegmentum container**.
Consumers must **not** conflate the pedunculopontine nucleus with any of
them.
**Boundary status (NOT the pontine nuclei — those are in the BASILAR
pons):** **Boundary case — the pedunculopontine nucleus is NOT the
pontine nuclei.** The **pontine nuclei** (``.../pons/pontine_nuclei/``)
are the **cortico-ponto-cerebellar relay** in the **basilar pons** —
the **ventral** portion of the pons. The **pedunculopontine nucleus**
(here) is a **cholinergic neuromodulatory nucleus** at the
**pontomesencephalic junction**. They are **DIFFERENT PONTS
SUB-DIVISIONS** — consumers must **not** conflate the pedunculopontine
nucleus with the pontine nuclei.
**Boundary status (NOT the whole tegmentum container — that is the
PARENT):** **Boundary case — the pedunculopontine nucleus is NOT the
whole tegmentum container; the tegmentum container is the PARENT.** The
**tegmentum** container (``.../pons/tegmentum/``) is the **dorsal
pontine grey-matter region** — the **tree-wired container** for the
**six neuromodulatory and autonomic nuclei** (locus coeruleus,
laterodorsal tegmental nucleus, nucleus incertus, pedunculopontine
nucleus, pontine micturition center, tegmental pontine reticular
nucleus). The **pedunculopontine nucleus** (here) is **one of the six
structural children** of the tegmentum container. Consumers must **not**
conflate the pedunculopontine nucleus with the **whole tegmentum**.
**Boundary status (NOT the whole pons — the pons is the GRANDPARENT):**
**Boundary case — the pedunculopontine nucleus is NOT the whole pons;
the pons is the GRANDPARENT.** The **pons** (``.../pons/``) is the
**whole metencephalic brainstem segment** — it contains the **basilar
pons**, the **pontine tegmentum**, the **parabrachial area**, the
**superior olivary complex**, the **cranial nerve nuclei**, the
**PPRF**, the **parvocellular reticular nucleus**, the **pontine
nuclei**, and the **six neuromodulatory and autonomic nuclei** of the
tegmentum container. The **pedunculopontine nucleus** (here) is **one
of the six neuromodulatory and autonomic nuclei** only. Consumers must
**not** conflate the pedunculopontine nucleus with the **whole pons**.
**Boundary status (NOT the midbrain tegmentum — the PPN is
PONTOMESENCEPHALIC and is TREE-WIRED in the pontine tegmentum):**
**Boundary case — the pedunculopontine nucleus is NOT the midbrain
tegmentum; the PPN is PONTOMESENCEPHALIC and is TREE-WIRED in the
pontine tegmentum.** The **midbrain tegmentum**
(``.../midbrain/tegmentum/``) is the **dorsal portion of the midbrain**
— it contains the **periaqueductal gray**, the **red nucleus**, the
**substantia nigra**, the **ventral tegmental area**, the **oculomotor
nucleus**, the **trochlear nucleus**, the **mesencephalic trigeminal
nucleus**, the **riMLF**, the **cMRF**, the **cuneiform nucleus**, and
other **midbrain structures**. The **pedunculopontine nucleus** (here)
is a **pontomesencephalic** nucleus — **straddling** the **caudal
midbrain / rostral pons** boundary — **tree-wired** in the **pontine
tegmentum container**. **The PPN is a boundary case** — it is
**anatomically** at the **pontomesencephalic junction** and is
**sometimes** classified as a **midbrain nucleus** (in the **midbrain
tegmentum** literature). **The tree** places it in the **pontine
tegmentum container** — consumers must **not** assume this **tree
placement** overrides the **pontomesencephalic anatomical reality**, and
must **not** conflate the PPN with the **purely midbrain** structures
(the **cuneiform nucleus**, the **substantia nigra**, the **ventral
tegmental area**, the **red nucleus**, the **periaqueductal gray**).
**Boundary status (NOT the fourth ventricle — that is a CSF SPACE):**
**Boundary case — the pedunculopontine nucleus is NOT the fourth
ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the **CSF-filled space**
**dorsal to** the pons and **ventral to** the cerebellum. The
**pedunculopontine nucleus** (here) is a **grey-matter nucleus** that
sits **ventrolateral** in the **pontine tegmentum** — **not** at the
**fourth-ventricle wall**. They are **DIFFERENT STRUCTURES** — the
**fourth ventricle** is a **fluid space**; the **pedunculopontine
nucleus** is **neural tissue**. Consumers must **not** conflate the
pedunculopontine nucleus with the fourth ventricle.
**Boundary status (MULTIPLE NEUROCHEMICALLY DISTINCT NEURON POPULATIONS —
cholinergic, glutamatergic, and GABAergic):** **Boundary case — the
pedunculopontine nucleus is NOT a single uniform neuron population; it
contains MULTIPLE neurochemically distinct populations.** The
**cholinergic principal neurons** — the **majority** of the PPN neurons
— they are the **cholinergic output** of the PPN, and they are the
**principal source of acetylcholine** for the **basal ganglia** and a
**major source** for the **thalamus**, the **brainstem**, and the
**spinal cord**. The **glutamatergic neurons** — the **PPN neurons that
are glutamatergic** (with or without cholinergic co-expression) — they
**contribute** to the **excitatory modulation** of the PPN's targets,
and they are **particularly important** for the **mesencephalic
locomotor region** function (the **glutamatergic PPN neurons** are
**critical** for **locomotion**). The **GABAergic neurons** — the **PPN
neurons that are GABAergic** (with or without cholinergic co-
expression) — they **contribute** to the **inhibitory modulation** of
the PPN's targets. **These populations are prose, not structural
children.** Consumers must **not** treat the pedunculopontine nucleus
as a single uniform population — it is a **neurochemically
heterogeneous nucleus** with **distinct** sub-circuits, and the
**glutamatergic** and **GABAergic** components are **particularly
important** for the PPN's **locomotion** and **REM-sleep** functions.
**Boundary status (SLEA-FREE — the pedunculopontine nucleus is NOT an
extended-amygdala component):** **Boundary case — the
pedunculopontine nucleus is SLEA-FREE.** The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the amygdala)
and to the **BNST**, **ventral pallidum**, and **nucleus accumbens**
(wired elsewhere). The **pedunculopontine nucleus** is a
**cholinergic neuromodulatory nucleus** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the
pedunculopontine nucleus — it is **SLEA-free**.

Overview
--------
The pedunculopontine nucleus is the **pontomesencephalic cholinergic
locomotion nucleus** of the **pontine tegmentum** — a
**neurochemically heterogeneous** grey-matter nucleus at the
**pontomesencephalic junction**, **ventrolateral** in the **pontine
tegmentum**. It is a **leaf** module under the tegmentum container, and
it is the **principal cholinergic source** for the **basal ganglia**
and a **major cholinergic source** for the **thalamus**, the
**brainstem**, and the **spinal cord** — the **neural substrate** of
the **locomotion**, **REM-sleep**, **arousal**, and **reward**
functions of the **mesencephalic locomotor region** (with the
**cuneiform nucleus**).

**The pedunculopontine nucleus is a LEAF, not a container.** It has **no
structural children**. The **cholinergic principal neurons**, the
**glutamatergic neurons**, and the **GABAergic neurons** are **prose
populations**, not structural children.

**The pedunculopontine nucleus is a SINGLE module at the tree level.**
The tree does **not** split the PPN into left/right — the module is a
**single, bilateral representation**.

**The pedunculopontine nucleus is a PONTOMESENCEPHALIC JUNCTION nucleus,
NOT a purely pontine nucleus.** It **straddles** the **caudal midbrain
/ rostral pons** boundary — **tree-wired** in the **pontine tegmentum
container**, but **anatomically** at the **pontomesencephalic
junction**. **This pontomesencephalic location** is a **classic source
of confusion** — consumers must **not** assume the PPN is a **purely
pontine** nucleus, and must **not** conflate it with the **purely
pontine** nuclei.

**The pedunculopontine nucleus is a CHOLINERGIC NEUROMODULATORY NUCLEUS
that ALSO serves as a MOTOR REGION.** It **projects diffusely** to the
**basal ganglia**, the **thalamus**, the **hypothalamus**, the
**brainstem**, and the **spinal cord** to **modulate** the
**excitability** of its targets — and it is **one of the two**
components of the **mesencephalic locomotor region** (with the
**cuneiform nucleus**). **The PPN is a "neuromodulatory nucleus" that
ALSO serves as a "motor region"** — consumers must **not** conflate the
PPN with a **purely** motor or sensory relay, but they must **also**
recognize its **motor-region** role.

**The pedunculopontine nucleus is CHOLINERGIC, NOT noradrenergic,
dopaminergic, serotonergic, or relaxin-3-expressing.** It is **one of
the two principal cholinergic sources** for the **forebrain** (the
**other** being the **laterodorsal tegmental nucleus**). The
**noradrenergic** nucleus (the locus coeruleus), the **dopaminergic**
nuclei (the substantia nigra and the ventral tegmental area), the
**serotonergic** nuclei (the raphe nuclei), and the **relaxin-3**
nucleus (the nucleus incertus) are **different structures** — different
neurotransmitters and different functional systems.

**The pedunculopontine nucleus is NOT the laterodorsal tegmental
nucleus, the locus coeruleus, the nucleus incertus, the pontine
micturition center, or the tegmental pontine reticular nucleus.** Those
are the **other five** neuromodulatory and autonomic nuclei of the
**pontine tegmentum container** — different neurotransmitters, different
functional systems, different projection targets. **The PPN and the LDT
are BOTH cholinergic** — but they are **different structures** with
**different anatomical locations** (PPN = **ventrolateral**; LDT =
**dorsomedial**) and **different functional emphases** (PPN = **primarily
locomotion/REM/reward**; LDT = **primarily REM/arousal**).

**The pedunculopontine nucleus is NOT the cuneiform nucleus.** The
**cuneiform nucleus** is the **other component** of the
**mesencephalic locomotor region** — it is a **glutamatergic** nucleus
that **primarily** initiates and maintains **locomotion**. The **PPN**
is the **cholinergic** nucleus that **also** contributes to the
**mesencephalic locomotor region** (with the **cuneiform nucleus**) and
**also** serves **REM-sleep**, **arousal**, and **reward** functions.

**The pedunculopontine nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The pedunculopontine nucleus contains **multiple neurochemically
distinct neuron populations** — documented as **prose**, not as
structural children:

*   **Cholinergic principal neurons** — the **majority** of the PPN
    neurons — they **synthesize** and **release acetylcholine** (via the
    **choline acetyltransferase (ChAT)** pathway). They **project** to
    the **basal ganglia** (the **substantia nigra pars compacta**, the
    **substantia nigra pars reticulata**, the **globus pallidus
    internus**, the **globus pallidus externus**, the **subthalamic
    nucleus**, the **striatum**), the **thalamus** (the **intralaminar
    nuclei**, the **reticular nucleus**, the **mediodorsal nucleus**),
    the **hypothalamus** (the **lateral hypothalamic area**, the
    **arcuate nucleus**), the **brainstem** (the **pontine reticular
    formation**, the **medullary reticular formation**, the
    **laterodorsal tegmental nucleus**, the **locus coeruleus**, the
    **dorsal raphe nucleus**, the **parabrachial area**, the **solitary
    nucleus**, the **nucleus ambiguus**), and the **spinal cord** (the
    **ventral horn**). **Cholinergic locomotion, REM-sleep, arousal, and
    reward modulation are the functional systems** subserved primarily
    by the cholinergic principal neurons.

*   **Glutamatergic neurons** — the **PPN neurons that are
    glutamatergic** (with or without cholinergic co-expression). They
    **release glutamate** at their **axon terminals** — the
    **excitatory** neurotransmitter that **modulates** the
    **excitability** of the PPN's targets. They **project** to the
    **ventral spinal cord** (via the **reticulospinal tract**) — they
    are **particularly important** for the **mesencephalic locomotor
    region** function — **glutamatergic PPN neurons** are **critical**
    for **locomotion initiation** and **maintenance**. They **also
    project** to the **basal ganglia**, the **thalamus**, the
    **hypothalamus**, the **brainstem**, and the **spinal cord**.
    **Glutamatergic locomotion and excitatory modulation are the
    functional systems** subserved primarily by the glutamatergic
    neurons.

*   **GABAergic neurons** — the **PPN neurons that are GABAergic** (with
    or without cholinergic co-expression). They **release GABA** at
    their **axon terminals** — the **inhibitory** neurotransmitter that
    **modulates** the **excitability** of the PPN's targets. They
    **project** to the **basal ganglia**, the **thalamus**, the
    **hypothalamus**, the **brainstem**, and the **spinal cord**.
    **GABAergic inhibitory modulation is the functional system**
    subserved primarily by the GABAergic neurons.

**These populations are prose, not structural children.** The tree wires
the **pedunculopontine nucleus** as a **single leaf** under the
tegmentum container — the **cholinergic principal neurons**, the
**glutamatergic neurons**, and the **GABAergic neurons** are **prose**,
not structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Pedunculopontine Nucleus / Laterodorsal Tegmental Nucleus Boundary
----------------------------------------------------------------------
This is the **sibling** boundary — **cholinergic locomotion/REM/reward
vs. cholinergic REM/arousal/motivation**:

*   **Pedunculopontine nucleus** (this module) — the **cholinergic**
    nucleus — the **principal cholinergic source** for the **basal
    ganglia** and a **major cholinergic source** for the **thalamus**,
    the **brainstem**, and the **spinal cord** — involved in
    **locomotion**, **REM sleep**, **arousal**, and **reward** —
    **ventrolateral** at the **pontomesencephalic junction**.

*   **Laterodorsal tegmental nucleus**
    (``.../tegmentum/laterodorsal_tegmental_nucleus/``) — the
    **cholinergic** nucleus — the **principal pontine cholinergic
    source** for the **thalamus** and a **major cholinergic source** for
    the **basal forebrain** — involved in **REM sleep**, **arousal**,
    and **motivation** — **dorsomedial** in the **pontine tegmentum**.

**They are DIFFERENT STRUCTURES** — different functional emphases
(locomotion/REM/reward for the PPN vs. REM/arousal/motivation for the
LDT) and different **anatomical locations** (the PPN is
**ventrolateral**; the LDT is **dorsomedial**). **They are both
cholinergic** — this shared neurotransmitter is a **classic source of
confusion** — consumers must **not** conflate the pedunculopontine
nucleus with the laterodorsal tegmental nucleus. They are
**functionally coupled** — the LDT and the PPN are **both cholinergic
REM-sleep and arousal nuclei** — but they are **different structures**
with **different anatomical locations** and **different functional
emphases**.

The Pedunculopontine Nucleus / Locus Coeruleus Boundary
-------------------------------------------------------
This is the **sibling** boundary — **cholinergic locomotion vs.
noradrenergic arousal/attention/stress**:

*   **Pedunculopontine nucleus** (this module) — the **cholinergic**
    nucleus.

*   **Locus coeruleus** (``.../tegmentum/locus_coeruleus/``) — the
    **noradrenergic** nucleus — the **principal source of
    norepinephrine** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(acetylcholine vs. noradrenaline), different functional systems
(cholinergic locomotion/REM-sleep/arousal/reward vs. noradrenergic
arousal/attention/stress/pain/memory), different anatomical locations
(the PPN is **ventrolateral** at the pontomesencephalic junction; the
LC is **dorsomedial** at the lateral fourth-ventricle wall). Consumers
must **not** conflate the pedunculopontine nucleus with the locus
coeruleus.

The Pedunculopontine Nucleus / Nucleus Incertus Boundary
--------------------------------------------------------
This is the **sibling** boundary — **cholinergic locomotion vs.
relaxin-3 stress/arousal/feeding**:

*   **Pedunculopontine nucleus** (this module) — the **cholinergic**
    nucleus.

*   **Nucleus incertus** (``.../tegmentum/nucleus_incertus/``) — the
    **relaxin-3-expressing** nucleus — involved in **stress**,
    **arousal**, **feeding**, and **neuroendocrine regulation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(acetylcholine vs. relaxin-3), different functional systems (cholinergic
locomotion/REM-sleep/arousal/reward vs. relaxin-3
stress/arousal/feeding/neuroendocrine), different projection targets
(basal ganglia/thalamus/brainstem/spinal cord vs.
septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus).
Consumers must **not** conflate the pedunculopontine nucleus with the
nucleus incertus.

The Pedunculopontine Nucleus / Pontine Micturition Center Boundary
------------------------------------------------------------------
This is the **sibling** boundary — **cholinergic locomotion vs.
micturition**:

*   **Pedunculopontine nucleus** (this module) — the **cholinergic**
    nucleus.

*   **Pontine micturition center**
    (``.../tegmentum/pontine_micturition_center/``) — the **micturition
    control center** — it **coordinates** the **micturition reflex**.

**They are DIFFERENT STRUCTURES** — different functional systems
(cholinergic locomotion/REM-sleep/arousal/reward vs. micturition),
different projection targets (basal ganglia/thalamus/brainstem/spinal
cord vs. sacral spinal cord). Consumers must **not** conflate the
pedunculopontine nucleus with the pontine micturition center.

The Pedunculopontine Nucleus / Tegmental Pontine Reticular Nucleus Boundary
---------------------------------------------------------------------------
This is the **sibling** boundary — **cholinergic locomotion vs. motor
relay**:

*   **Pedunculopontine nucleus** (this module) — the **cholinergic**
    nucleus — **one of the two** components of the **mesencephalic
    locomotor region** (with the **cuneiform nucleus**) — involved in
    **locomotion**, **REM sleep**, **arousal**, and **reward**.

*   **Tegmental pontine reticular nucleus**
    (``.../tegmentum/tegmental_pontine_reticular_nucleus/``) — the
    **motor relay** — it **projects** to the **spinal cord** (via the
    **reticulospinal tract**) and to the **cerebellum** (via the
    **pontocerebellar fibers**) — it is involved in **locomotion**,
    **posture**, and **motor pattern generation**.

**They are both involved in locomotion** — but they are **DIFFERENT
STRUCTURES** — the **tegmental pontine reticular nucleus** is a
**purely motor relay** (reticulospinal and pontocerebellar projections),
while the **pedunculopontine nucleus** is a **cholinergic
neuromodulatory nucleus** that **participates** in the **mesencephalic
locomotor region** (with the **cuneiform nucleus**) and **also** serves
**REM-sleep**, **arousal**, and **reward** functions. Consumers must
**not** conflate the pedunculopontine nucleus with the tegmental pontine
reticular nucleus.

The Pedunculopontine Nucleus / Cuneiform Nucleus Boundary
---------------------------------------------------------
This is the **mesencephalic locomotor region partner** boundary:

*   **Pedunculopontine nucleus** (this module) — the **cholinergic**
    nucleus — **one of the two** components of the **mesencephalic
    locomotor region** (with the **cuneiform nucleus**) — involved in
    **locomotion**, **REM sleep**, **arousal**, and **reward**.

*   **Cuneiform nucleus** (midbrain) — the **other component** of the
    **mesencephalic locomotor region** — a **glutamatergic** nucleus
    that **primarily** initiates and maintains **locomotion**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(acetylcholine vs. glutamate), different functional emphases (the
cuneiform nucleus is **primarily** locomotion; the PPN is **locomotion
+ REM sleep + arousal + reward**), different anatomical locations (the
cuneiform nucleus is **midbrain**; the PPN is **pontomesencephalic**).
Consumers must **not** conflate the pedunculopontine nucleus with the
cuneiform nucleus — but they must **recognize** that the **two**
together constitute the **mesencephalic locomotor region**.

The Pedunculopontine Nucleus / Parabrachial Area Boundary
---------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pedunculopontine nucleus** (this module) — a **cholinergic
    neuromodulatory nucleus** — a **structural child of the pontine
    tegmentum container**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex** — a **separate
    structural child of the pons**.

**They are DIFFERENT STRUCTURES** — the parabrachial area is **not** a
structural child of the pontine tegmentum (in the tree), even though it
is **anatomically located** in the pontine tegmentum. Consumers must
**not** conflate the pedunculopontine nucleus with the parabrachial area.

The Pedunculopontine Nucleus / Superior Olivary Complex, Cranial Nerve Nuclei, PPRF, and Parvocellular Reticular Nucleus Boundary
-------------------------------------------------------------------------------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pedunculopontine nucleus** (this module) — a **cholinergic
    neuromodulatory nucleus** — a **structural child of the pontine
    tegmentum container**.

*   **Superior olivary complex** (``.../pons/superior_olivary_complex/``),
    **cranial nerve nuclei** (``.../pons/cranial_nerve_nuclei/``),
    **PPRF** (``.../pons/paramedian_pontine_reticular_formation/``),
    **parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``) — **separate
    structural children of the pons**.

**They are DIFFERENT STRUCTURES** — those four structures are **not**
structural children of the pontine tegmentum (in the tree), even though
they are **anatomically located** in the pontine tegmentum. Consumers
must **not** conflate the pedunculopontine nucleus with any of them.

The Pedunculopontine Nucleus / Pontine Nuclei Boundary
------------------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Pedunculopontine nucleus** (this module) — a **cholinergic
    neuromodulatory nucleus** at the **pontomesencephalic junction**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not**
conflate the pedunculopontine nucleus with the pontine nuclei.

The Pedunculopontine Nucleus / Whole Tegmentum Container Boundary
-----------------------------------------------------------------
This is the **sub-nucleus vs. parent** boundary:

*   **Pedunculopontine nucleus** (this module) — one of the **six
    neuromodulatory and autonomic nuclei** of the pontine tegmentum.

*   **Tegmentum container** (``.../pons/tegmentum/``) — the **dorsal
    pontine grey-matter region** — the **tree-wired container** for the
    **six neuromodulatory and autonomic nuclei**.

**The pedunculopontine nucleus is a child of the tegmentum container.**
Consumers must **not** conflate the pedunculopontine nucleus with the
**whole tegmentum**.

The Pedunculopontine Nucleus / Whole Pons Boundary
--------------------------------------------------
This is the **nucleus vs. grandparent** boundary:

*   **Pedunculopontine nucleus** (this module) — one of the **six
    neuromodulatory and autonomic nuclei** of the pontine tegmentum.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**.

**The pedunculopontine nucleus is a grandchild of the pons** (via the
tegmentum container). Consumers must **not** conflate the
pedunculopontine nucleus with the **whole pons**.

The Pedunculopontine Nucleus / Midbrain Tegmentum Boundary
----------------------------------------------------------
This is the **pontomesencephalic vs. purely midbrain** boundary:

*   **Pedunculopontine nucleus** (this module) — a **pontomesencephalic**
    nucleus — **tree-wired** in the **pontine tegmentum container**.

*   **Midbrain tegmentum** (``.../midbrain/tegmentum/``) — the **dorsal
    portion of the midbrain** — the **purely midbrain** structures
    (periaqueductal gray, red nucleus, substantia nigra, ventral
    tegmental area, oculomotor nucleus, trochlear nucleus,
    mesencephalic trigeminal nucleus, riMLF, cMRF, **cuneiform
    nucleus**).

**The PPN is a boundary case** — it is **anatomically** at the
**pontomesencephalic junction** and is **sometimes** classified as a
**midbrain nucleus** (in the **midbrain tegmentum** literature). **The
tree** places it in the **pontine tegmentum container** — consumers
must **not** assume this **tree placement** overrides the
**pontomesencephalic anatomical reality**, and must **not** conflate the
PPN with the **purely midbrain** structures (especially the **cuneiform
nucleus**, which is the **other** component of the **mesencephalic
locomotor region**).

The Pedunculopontine Nucleus / Fourth Ventricle Boundary
--------------------------------------------------------
This is the **neural tissue vs. CSF space** boundary:

*   **Pedunculopontine nucleus** (this module) — a **grey-matter
    nucleus** that sits **ventrolateral** in the **pontine tegmentum**.

*   **Fourth ventricle** (``.../metencephalon/fourth_ventricle/``) — the
    **CSF-filled space** **dorsal to** the pons.

**They are DIFFERENT STRUCTURES** — the **fourth ventricle** is a
**fluid space**; the **pedunculopontine nucleus** is **neural tissue**.
Consumers must **not** conflate the pedunculopontine nucleus with the
fourth ventricle.

The Pedunculopontine Nucleus / Substantia Nigra, Ventral Tegmental Area, and Raphe Nuclei Boundary
------------------------------------------------------------------------------------------------
This is the **cholinergic vs. dopaminergic/serotonergic** boundary:

*   **Pedunculopontine nucleus** (this module) — the **cholinergic**
    nucleus — **one of the two** principal cholinergic sources for the
    **forebrain**.

*   **Substantia nigra** (pars compacta, midbrain) and **ventral
    tegmental area** (midbrain) — the **dopaminergic** nuclei — the
    **principal sources of dopamine** in the brain.

*   **Dorsal raphe nucleus** and **median raphe nucleus**
    (midbrain/pons) — the **serotonergic** nuclei — the **principal
    sources of serotonin** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(acetylcholine vs. dopamine vs. serotonin), different anatomical
locations (pontomesencephalic vs. midbrain), different functional
systems (cholinergic locomotion/REM-sleep/arousal/reward vs. dopaminergic
reward/motor control/learning vs. serotonergic
mood/sleep/appetite/pain). Consumers must **not** conflate the
pedunculopontine nucleus with the dopaminergic or serotonergic nuclei.

The Pedunculopontine Nucleus / SLEA Boundary
-------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Pedunculopontine nucleus** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The pedunculopontine nucleus is NOT part of the SLEA continuum.** It
is a **cholinergic neuromodulatory nucleus**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
pedunculopontine nucleus.

Function in the Human Brain
---------------------------
The pedunculopontine nucleus's functions are **the cholinergic (and
glutamatergic and GABAergic) modulation of locomotion, REM sleep,
arousal, and reward** — **NOT a single unified function**:

*   **Locomotion (Mesencephalic Locomotor Region):** The **PPN** — with
    the **cuneiform nucleus** — is the **mesencephalic locomotor
    region** — the **midbrain/pontomesencephalic** region that
    **initiates** and **maintains** **locomotion**. The **glutamatergic
    PPN neurons** (and the **glutamatergic cuneiform neurons**)
    **project** to the **ventral spinal cord** (via the
    **reticulospinal tract**) to **activate** the **spinal locomotor
    central pattern generators** — they **initiate** and **maintain**
    **walking**, **running**, and **other locomotor behaviors**. **The
    cholinergic PPN neurons** **modulate** the **basal ganglia** and the
    **thalamus** to **support** the **locomotor** function. **This
    "locomotion"** function is the **neural substrate** of the **PPN's
    role in movement** — the **PPN** is the **cholinergic and
    glutamatergic** region that **initiates** and **maintains**
    **locomotion**.

*   **REM Sleep (Cholinergic Thalamic Activation):** The **cholinergic
    PPN neurons** — **along with** the **laterodorsal tegmental
    nucleus** — **project** to the **thalamus** (especially the
    **intralaminar nuclei** and the **reticular nucleus**) — they
    **activate** the **thalamus** during **REM sleep**, **promoting**
    the **thalamocortical activation** that **underlies** the
    **desynchronized EEG** of **REM sleep**. The **PPN** is a **major
    cholinergic REM-sleep nucleus** — **along with** the **LDT**.

*   **Arousal (Cholinergic and Glutamatergic Brainstem Activation):** The
    **PPN** **projects** to the **brainstem arousal centers** (the
    **pontine reticular formation**, the **medullary reticular
    formation**, the **locus coeruleus**, the **dorsal raphe
    nucleus**) — it **promotes** the **wakeful** and **alert** states
    by **increasing** the **excitability** of the **brainstem** and
    **thalamic** neurons.

*   **Reward (Cholinergic and Glutamatergic Modulation of the Ventral
    Tegmental Area and the Substantia Nigra):** The **PPN** **projects**
    to the **ventral tegmental area** and the **substantia nigra** — it
    **modulates** the **dopaminergic** systems that **underlie**
    **motivation** and **reward**. The **PPN's cholinergic** and
    **glutamatergic** neurons **contribute** to the **reward-related**
    and **motivational** functions of the **pontomesencephalic
    cholinergic system**.

*   **Posture and Motor Control (Cholinergic and Glutamatergic Modulation
    of the Basal Ganglia and the Spinal Cord):** The **PPN** **projects**
    to the **basal ganglia** (the **substantia nigra**, the **globus
    pallidus**, the **subthalamic nucleus**, the **striatum**) and the
    **spinal cord** — it **modulates** the **basal ganglia** and
    **spinal** motor circuits to **support** **posture** and **motor
    control**. **This "posture and motor control"** function is the
    **neural substrate** of the **PPN's role in motor function** — the
    **PPN** is the **cholinergic and glutamatergic** region that
    **modulates** the **basal ganglia** and **spinal** motor circuits.

*   **NOT a neural processor in the classical sense.** The PPN is a
    **neuromodulatory nucleus** that **also** serves as a **motor
    region** — it **receives** afferent inputs (from the **basal
    ganglia** — the **substantia nigra pars reticulata**, the **globus
    pallidus internus**, the **subthalamic nucleus** — the **cortex**
    — the **motor cortex**, the **prefrontal cortex** — the **limbic
    system** — the **amygdala**, the **hypothalamus** — and the
    **brainstem**) and **projects diffusely** to the **basal ganglia**,
    the **thalamus**, the **hypothalamus**, the **brainstem**, and the
    **spinal cord**. The **processing** of locomotion, REM sleep,
    arousal, and reward happens in a **distributed** manner across the
    **PPN**, the **cuneiform nucleus** (for locomotion), the
    **targets of the PPN** (the **basal ganglia**, the **thalamus**,
    the **hypothalamus**, the **brainstem**, the **spinal cord**), and
    the **other neuromodulatory systems** (the **noradrenergic**,
    **cholinergic**, **dopaminergic**, and **serotonergic** systems)
    that **interact** with the **PPN**.

**The unifying theme:** the pedunculopontine nucleus is the
**pontomesencephalic cholinergic locomotion nucleus** — the **principal
cholinergic source** for the **basal ganglia** and a **major cholinergic
source** for the **thalamus**, the **brainstem**, and the **spinal
cord**. It is **cholinergic** (with **glutamatergic** and **GABAergic**
co-transmission), **SLEA-free**, and **NOT the laterodorsal tegmental
nucleus** — the **LDT** is the **other cholinergic** neuromodulatory
nucleus (**dorsomedial**, **primarily REM/arousal**). The **PPN** is the
**cholinergic** nucleus that **also** serves as a **motor region** (the
**mesencephalic locomotor region**, with the **cuneiform nucleus**) and
**also** serves **REM-sleep**, **arousal**, and **reward** functions.

Associated Disorders
--------------------
The pedunculopontine nucleus has **no named "pedunculopontine nucleus
syndrome"** — its clinical associations are **function-specific**:

*   **Parkinson's Disease — PPN Involvement:** **Parkinson's disease** is
    characterized by **degeneration** of the **cholinergic pontine
    nuclei** (including the **pedunculopontine nucleus** and the
    **laterodorsal tegmental nucleus**) — **PPN degeneration**
    **contributes** to the **gait**, **postural**, **sleep**, and
    **cognitive** symptoms of **Parkinson's disease**. **Deep brain
    stimulation (DBS)** of the **PPN** has been **investigated** as a
    **treatment** for **Parkinson's disease gait and postural
    impairments** — with **mixed results**.

*   **Progressive Supranuclear Palsy (PSP) — PPN Involvement:**
    **Progressive supranuclear palsy** is a **neurodegenerative
    disorder** characterized by **cholinergic pontine nuclei
    degeneration** (including the **pedunculopontine nucleus**) — **PPN
    degeneration** **contributes** to the **gait**, **postural**, and
    **oculomotor** symptoms of **PSP** (especially the **vertical gaze
    palsy** and the **postural instability**).

*   **REM Sleep Behavior Disorder (RBD) — PPN Involvement:** **REM sleep
    behavior disorder** is a **parasomnia** characterized by **loss of
    REM-sleep atonia** and **acting out of dreams** — it has been
    **associated** with **dysfunction** of the **pontine REM-sleep
    nuclei**, including the **pedunculopontine nucleus** (and the
    **laterodorsal tegmental nucleus**, the **sublaterodorsal
    nucleus**, and the **medullary REM-sleep circuits**). The **PPN**
    is **one of the neural substrates** of **REM-sleep control**, and
    its dysfunction may **contribute** to **RBD**.

*   **Narcolepsy — PPN Involvement:** **Narcolepsy** is a **sleep
    disorder** characterized by **excessive daytime sleepiness**,
    **cataplexy**, **hypnagogic hallucinations**, and **sleep
    paralysis** — it is caused by **loss of orexin (hypocretin)
    neurons** in the **hypothalamus**, but the **cholinergic REM-sleep
    nuclei** (including the **PPN**) are **involved** in the
    **downstream** effects of **orexin loss** — the **PPN's
    cholinergic** neurons **contribute** to the **REM-sleep
    dysregulation** in **narcolepsy**.

*   **Schizophrenia — PPN Involvement:** **Schizophrenia** has been
    **associated** with **cholinergic dysfunction** — including
    **dysregulation** of the **cholinergic pontine nuclei** (the **PPN**
    and the **LDT**) — the **PPN's cholinergic** projections to the
    **basal ganglia** and the **thalamus** **contribute** to the
    **arousal**, **attention**, and **cognitive** functions that are
    **impaired** in **schizophrenia**.

*   **Alzheimer's Disease — PPN Involvement:** **Alzheimer's disease** is
    characterized by **loss of cholinergic basal forebrain neurons** and
    **loss of cholinergic pontine neurons** — including the
    **pedunculopontine nucleus** and the **laterodorsal tegmental
    nucleus** — this **cholinergic degeneration** **contributes** to the
    **cognitive** and **sleep** symptoms of **Alzheimer's disease**.

*   **Pontine Stroke or Midbrain Stroke — PPN Involvement:** A **pontine
    stroke** or **midbrain stroke** (e.g., **basilar artery** or
    **posterior cerebral artery** territory) involving the **PPN**
    causes **locomotion dysfunction** (gait and postural impairment),
    **REM-sleep dysregulation**, and **arousal dysfunction** — often
    accompanied by **other pontine or midbrain signs** (**hemiparesis**,
    **facial palsy**, **abducens palsy**, **cerebellar ataxia**,
    **oculomotor palsy**).

*   **No Named "PPN Syndrome":** The pedunculopontine nucleus is a
    **neurochemically heterogeneous neuromodulatory and motor nucleus** —
    it has **no named clinical syndrome** of its own. Its clinical
    relevance is **locomotion, REM-sleep, arousal, and reward specific**
    — **Parkinson's disease**, **progressive supranuclear palsy**,
    **REM sleep behavior disorder**, **narcolepsy**, **schizophrenia**,
    **Alzheimer's disease**, and **pontine or midbrain stroke** are all
    **PPN-involved** conditions.

**What is NOT here:** The pedunculopontine nucleus is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **acoustic neuroma** (CN VIII nerve), **vestibular neuritis**
(vestibular nerve), **labyrinthitis** (inner ear), **auditory neuropathy
spectrum disorder** (cochlear nerve or hair cell), **Wallenberg
syndrome** (lateral medulla), **internuclear ophthalmoplegia** (MLF), or
**horizontal gaze palsy** (PPRF or abducens nucleus). Its clinical
relevance is **locomotion, REM-sleep, arousal, and reward specific**,
via the **cholinergic (and glutamatergic and GABAergic) modulation** it
subserves. **No named PPN syndrome exists.**

Lateralization Notes
--------------------
This is the **single** pedunculopontine nucleus module. The PPN is
**bilateral in real anatomy** (left PPN and right PPN), but the tree
wires it as a **single module** — and the module carries **NO warning at
the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **pedunculopontine_nucleus** module (here) is a **single module**
    that represents the **bilateral PPN** (the left PPN and the right
    PPN). The tree does **not** split them into left/right. Consumers
    must **not** assume a left/right split exists at the tree level —
    the module is a **single, bilateral representation**.

*   **Bilateral Projections (Structural Fact, NOT a Lateralization
    Warning):** The **PPN** **projects bilaterally** to the **basal
    ganglia**, the **thalamus**, the **hypothalamus**, the **brainstem**,
    and the **spinal cord** — each PPN projects to **both** left and
    right targets. **This bilateral projection** is a **structural
    fact** of the **cholinergic neuromodulatory system** — it is **not**
    a functional lateralization. It is the **neural substrate** of the
    **bilateral cholinergic modulation** of locomotion, REM sleep,
    arousal, and reward.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The PPN is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the PPN.

*   **NO Amygdala-Lateralization Warning of their own (the PPN is
    CHOLINERGIC NEUROMODULATORY/MOTOR, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The PPN is a
    **cholinergic neuromodulatory and motor nucleus** — consumers must
    **not** conflate it with the **amygdala** or with the **fear
    circuit**.

**A consumer that sees "pedunculopontine_nucleus" must understand that
the module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **bilateral projections** are
**structural facts**, not lateralizations. The PPN is a **strict-single
module with NO warning at the module level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** PPN as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/locus_coeruleus/``,
    ``.../tegmentum/laterodorsal_tegmental_nucleus/``,
    ``.../tegmentum/nucleus_incertus/``,
    ``.../tegmentum/pontine_micturition_center/``,
    ``.../tegmentum/tegmental_pontine_reticular_nucleus/``,
    ``.../pons/parabrachial_area/``,
    ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../pons/pontine_nuclei/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, or any other container. The PPN's
    relationships to the **laterodorsal tegmental nucleus**, the **locus
    coeruleus**, the **nucleus incertus**, the **pontine micturition
    center**, the **tegmental pontine reticular nucleus**, the
    **cuneiform nucleus**, the **parabrachial area**, the **superior
    olivary complex**, the **cranial nerve nuclei**, the **PPRF**, the
    **parvocellular reticular nucleus**, the **pontine nuclei**, the
    **fourth ventricle**, the **midbrain tegmentum**, the **substantia
    nigra**, the **ventral tegmental area**, the **raphe nuclei**, the
    **whole tegmentum container**, the **whole pons**, and the **SLEA
    continuum** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **cholinergic
    principal neurons**, the **glutamatergic neurons**, and the
    **GABAergic neurons** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The **PPN**
    is a **single module** that represents the **bilateral PPN** — the
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **PONTOMESENCEPHALIC JUNCTION — NOT a purely pontine nucleus.** The
    **PPN** straddles the **caudal midbrain / rostral pons** boundary —
    it is **tree-wired** in the **pontine tegmentum container**, but it
    is **anatomically** at the **pontomesencephalic junction**.
    Consumers must **not** assume the PPN is a **purely pontine**
    nucleus.
*   **CHOLINERGIC NEUROMODULATORY NUCLEUS that ALSO serves as a MOTOR
    REGION.** The **PPN** is a **cholinergic neuromodulatory nucleus**
    that **also** serves as one of the **two components** of the
    **mesencephalic locomotor region** (with the **cuneiform nucleus**).
    Consumers must **not** conflate the PPN with a **purely** motor or
    sensory relay — but they must **also** recognize its **motor-region**
    role.
*   **CHOLINERGIC — NOT noradrenergic, dopaminergic, serotonergic, or
    relaxin-3-expressing.** The **PPN** is **one of the two principal
    cholinergic sources** for the **forebrain** (the other being the
    **LDT**). Consumers must **not** conflate the PPN with the
    **noradrenergic**, **dopaminergic**, **serotonergic**, or
    **relaxin-3** nuclei.
*   **NOT the laterodorsal tegmental nucleus — that is the OTHER
    cholinergic neuromodulatory nucleus.** The **PPN** and the **LDT**
    are **both cholinergic** — but they are **different structures**
    with **different anatomical locations** (PPN = **ventrolateral**;
    LDT = **dorsomedial**) and **different functional emphases**
    (PPN = **primarily locomotion/REM/reward**; LDT = **primarily
    REM/arousal**). Consumers must **not** conflate the PPN with the
    LDT.
*   **NOT the locus coeruleus — that is the NORADRENERGIC
    neuromodulatory nucleus.** Consumers must **not** conflate the PPN
    with the LC.
*   **NOT the nucleus incertus, the pontine micturition center, or the
    tegmental pontine reticular nucleus — those are DIFFERENT
    neuromodulatory and autonomic nuclei.** Consumers must **not**
    conflate the PPN with any of them.
*   **NOT the cuneiform nucleus — that is the OTHER mesencephalic
    locomotor region component.** The **PPN** and the **cuneiform
    nucleus** are **both** components of the **mesencephalic locomotor
    region** — but they are **different structures** with **different
    neurotransmitters** (PPN = **cholinergic + glutamatergic**;
    cuneiform = **glutamatergic**) and **different functional
    emphases** (the cuneiform nucleus is **primarily locomotion**; the
    PPN is **locomotion + REM sleep + arousal + reward**). Consumers
    must **not** conflate the PPN with the cuneiform nucleus — but they
    must **recognize** that the **two** together constitute the
    **mesencephalic locomotor region**.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, the PPRF, or the parvocellular reticular
    nucleus — those are SEPARATE structural children of the pons.**
    Consumers must **not** conflate the PPN with any of them.
*   **NOT the pontine nuclei — those are in the BASILAR pons.**
    Consumers must **not** conflate the PPN with the pontine nuclei.
*   **NOT the whole tegmentum container — that is the PARENT.**
    Consumers must **not** conflate the PPN with the whole tegmentum.
*   **NOT the whole pons — that is the GRANDPARENT.** Consumers must
    **not** conflate the PPN with the whole pons.
*   **NOT the midbrain tegmentum — the PPN is PONTOMESENCEPHALIC and is
    TREE-WIRED in the pontine tegmentum.** Consumers must **not** assume
    the tree placement overrides the **pontomesencephalic anatomical
    reality**, and must **not** conflate the PPN with the **purely
    midbrain** structures.
*   **NOT the fourth ventricle — that is a CSF SPACE.** Consumers must
    **not** conflate the PPN with the fourth ventricle.
*   **NOT the substantia nigra, the ventral tegmental area, or the raphe
    nuclei — those are DOPAMINERGIC or SEROTONERGIC nuclei.** Consumers
    must **not** conflate the PPN with the dopaminergic or serotonergic
    nuclei.
*   **MULTIPLE NEUROCHEMICALLY DISTINCT NEURON POPULATIONS —
    cholinergic, glutamatergic, and GABAergic.** The **cholinergic
    principal neurons** (the majority), the **glutamatergic neurons**,
    and the **GABAergic neurons** are **prose**, not structural
    children. Consumers must **not** treat the PPN as a single uniform
    nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The PPN is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the PPN is CHOLINERGIC
    NEUROMODULATORY/MOTOR.** The **fear-output** structure is the
    **central nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**; the **fear-modulatory / extinction**
    structures are the **basomedial nuclei**. The **PPN** is a
    **cholinergic neuromodulatory and motor nucleus** — it is **not**
    part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The PPN is a local leaf under the
    tegmentum container, not a cross-listed leaf.
*   **No nested cross-listing.** The PPN has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum import pedunculopontine_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.tegmentum."
        "pedunculopontine_nucleus"
    )

**Do not** assume the PPN is a **container**. It is a **leaf** — the
**cholinergic principal neurons**, the **glutamatergic neurons**, and the
**GABAergic neurons** are **prose**, not structural children.

**Do not** assume the PPN is **bilateralized at the tree level**. The
PPN is **bilateral in real anatomy**, but the tree wires it as a
**single module** — there is **no left/right split at the module level**.

**Do not** assume the PPN is a **purely pontine nucleus**. The **PPN**
straddles the **caudal midbrain / rostral pons** boundary — it is
**anatomically** at the **pontomesencephalic junction** — the tree
places it in the **pontine tegmentum container**, but consumers must
**not** assume this placement overrides the **pontomesencephalic
anatomical reality**.

**Do not** assume the PPN is a **purely motor or sensory relay**. The
**PPN** is a **cholinergic neuromodulatory nucleus** that **also**
serves as one of the **two components** of the **mesencephalic
locomotor region** (with the **cuneiform nucleus**).

**Do not** assume the PPN is the **laterodorsal tegmental nucleus**. Both
are **cholinergic** — but they are **different structures** with
**different anatomical locations** (PPN = **ventrolateral**; LDT =
**dorsomedial**) and **different functional emphases** (PPN =
**primarily locomotion/REM/reward**; LDT = **primarily REM/arousal**).

**Do not** assume the PPN is the **locus coeruleus**. The **locus
coeruleus** is the **noradrenergic** nucleus. The **PPN** is the
**cholinergic** nucleus.

**Do not** assume the PPN is the **nucleus incertus**, the **pontine
micturition center**, or the **tegmental pontine reticular nucleus**.
Those are **different structures** — the **nucleus incertus**
(relaxin-3 stress/arousal/feeding/neuroendocrine), the **pontine
micturition center** (micturition), and the **tegmental pontine
reticular nucleus** (motor relay).

**Do not** assume the PPN is the **cuneiform nucleus**. The **cuneiform
nucleus** is the **other component** of the **mesencephalic locomotor
region** — it is **primarily** a **glutamatergic** nucleus that
**initiates** and **maintains** **locomotion**. The **PPN** is the
**cholinergic** nucleus that **also** contributes to the
**mesencephalic locomotor region** and **also** serves **REM-sleep**,
**arousal**, and **reward** functions.

**Do not** assume the PPN is the **parabrachial area**, the **superior
olivary complex**, the **cranial nerve nuclei**, the **PPRF**, or the
**parvocellular reticular nucleus**. Those are **separate structural
children of the pons** — even though they are anatomically located in
the pontine tegmentum.

**Do not** assume the PPN is the **pontine nuclei**. The **pontine
nuclei** are in the **basilar pons** — the PPN is at the
**pontomesencephalic junction**.

**Do not** assume the PPN is the **whole tegmentum** or the **whole
pons**. The **tegmentum** is the **parent**; the **pons** is the
**grandparent**.

**Do not** assume the PPN is the **fourth ventricle**. The **fourth
ventricle** is a **CSF space**; the PPN is **neural tissue**
ventrolateral in the pontine tegmentum.

**Do not** assume the PPN is the **midbrain tegmentum**, the
**substantia nigra**, the **ventral tegmental area**, or the **raphe
nuclei**. The **midbrain tegmentum** is a **purely midbrain** region —
the **PPN** is **pontomesencephalic**. The **substantia nigra** and the
**ventral tegmental area** are **dopaminergic**; the **raphe nuclei**
are **serotonergic**. The **PPN** is the **cholinergic** nucleus.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the PPN. **The PPN is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the PPN's (empty) children (recommended consumer pattern)::

    PEDUNCULOPONTINE_NUCLEUS_CHILDREN = ()
    # The PPN is a leaf. The cholinergic principal neurons, the
    # glutamatergic neurons, and the GABAergic neurons are prose, not
    # modules.

Reaching the laterodorsal tegmental nucleus (recommended consumer
pattern — the OTHER cholinergic sibling)::

    # The laterodorsal tegmental nucleus is the OTHER CHOLINERGIC sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/laterodorsal_tegmental_nucleus/
    #
    # Both the PPN and the LDT are cholinergic REM-sleep and arousal
    # nuclei — but they are DIFFERENT STRUCTURES with DIFFERENT
    # anatomical locations (PPN = ventrolateral; LDT = dorsomedial) and
    # DIFFERENT functional emphases (PPN = primarily locomotion/REM/
    # reward; LDT = primarily REM/arousal).

Reaching the locus coeruleus (recommended consumer pattern — the
noradrenergic sibling)::

    # The locus coeruleus is the NORADRENERGIC sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The LC is noradrenergic; the PPN is cholinergic. They are
    # DIFFERENT STRUCTURES with DIFFERENT neurotransmitters and
    # functional systems.

Reaching the nucleus incertus (recommended consumer pattern — the
relaxin-3 sibling)::

    # The nucleus incertus is the RELAXIN-3-EXPRESSING sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/nucleus_incertus/
    #
    # The nucleus incertus is relaxin-3-expressing; the PPN is
    # cholinergic. They are DIFFERENT STRUCTURES.

Reaching the pontine micturition center (recommended consumer pattern —
the micturition sibling)::

    # The pontine micturition center is the MICTURITION CONTROL sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pontine_micturition_center/
    #
    # The pontine micturition center coordinates the micturition reflex;
    # the PPN is the cholinergic locomotion/REM-sleep/arousal/reward
    # nucleus.

Reaching the tegmental pontine reticular nucleus (recommended consumer
pattern — the motor relay sibling)::

    # The tegmental pontine reticular nucleus is the MOTOR RELAY sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/tegmental_pontine_reticular_nucleus/
    #
    # The tegmental pontine reticular nucleus is a purely motor relay
    # (reticulospinal and pontocerebellar projections); the PPN is a
    # cholinergic neuromodulatory and motor-region nucleus.

Reaching the cuneiform nucleus (recommended consumer pattern — the
MESENCEPHALIC LOCOMOTOR REGION partner)::

    # The cuneiform nucleus (midbrain) is the OTHER COMPONENT of the
    # mesencephalic locomotor region:
    #
    #   .../midbrain/tegmentum/cuneiform_nucleus/
    #
    # The PPN and the cuneiform nucleus together constitute the
    # mesencephalic locomotor region — but they are DIFFERENT STRUCTURES
    # (PPN = cholinergic + glutamatergic; cuneiform = glutamatergic) with
    # DIFFERENT functional emphases (the cuneiform nucleus is primarily
    # locomotion; the PPN is locomotion + REM sleep + arousal + reward).

Reaching the parabrachial area (recommended consumer pattern — a
SEPARATE pons child)::

    # The parabrachial area is a SEPARATE STRUCTURAL CHILD of the pons:
    #
    #   .../pons/parabrachial_area/
    #
    # The parabrachial area is the visceral-sensory and respiratory-relay
    # complex; the PPN is a cholinergic neuromodulatory and motor-region
    # nucleus.

Reaching the whole tegmentum container (recommended consumer pattern —
the PARENT)::

    # The tegmentum container is the DORSAL PONTINE GREY-MATTER REGION
    # that CONTAINS the PPN as one of its six structural children:
    #
    #   .../pons/tegmentum/
    #
    # The PPN is a CHILD of the tegmentum container.

Reaching the whole pons (recommended consumer pattern — the
GRANDPARENT)::

    # The pons is the WHOLE METENCEPHALIC BRAINSTEM SEGMENT that CONTAINS
    # the tegmentum container:
    #
    #   .../pons/
    #
    # The PPN is a GRANDCHILD of the pons.

Bilateral iteration (recommended consumer pattern)::

    # The PPN is a SINGLE module (not bilateralized at the tree level).
    # The module represents the BILATERAL PPN.
    ppn_path = (
        "hindbrain.metencephalon.pons.tegmentum.pedunculopontine_nucleus"
    )
    # resolve ppn_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The PPN's neuron populations are prose, not modules:
    #   cholinergic principal neurons -> synthesize and release
    #       acetylcholine; project to the basal ganglia (substantia nigra
    #       pars compacta and reticulata, globus pallidus internus and
    #       externus, subthalamic nucleus, striatum), thalamus
    #       (intralaminar nuclei, reticular nucleus, mediodorsal nucleus),
    #       hypothalamus (lateral hypothalamic area, arcuate nucleus),
    #       brainstem (pontine reticular formation, medullary reticular
    #       formation, laterodorsal tegmental nucleus, locus coeruleus,
    #       dorsal raphe nucleus, parabrachial area, solitary nucleus,
    #       nucleus ambiguus), and spinal cord (ventral horn); the
    #       cholinergic component of locomotion, REM sleep, arousal,
    #       and reward modulation
    #   glutamatergic neurons -> release glutamate at their axon
    #       terminals; project to the ventral spinal cord (via the
    #       reticulospinal tract) and to the basal ganglia, thalamus,
    #       hypothalamus, brainstem, and spinal cord; particularly
    #       important for the mesencephalic locomotor region function
    #   GABAergic neurons -> release GABA at their axon terminals;
    #       project to the basal ganglia, thalamus, hypothalamus,
    #       brainstem, and spinal cord; contribute to the inhibitory
    #       modulation of the PPN's targets
    #
    # Do not attempt to resolve these as sub-paths of the PPN — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical PPN anatomy:** Mesulam, M.M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the rat:
    an overview based on an alternative nomenclature (Ch1-Ch6)."
    *Neuroscience* 10:1185–1201. (Pedunculopontine nucleus —
    cholinergic brainstem nucleus; Ch5.)
*   **PPN — canonical modern review:** Garcia-Rill, E. (1991). "The
    pedunculopontine nucleus." *Progress in Neurobiology* 36:363–389.
    (Pedunculopontine nucleus — cholinergic locomotion, REM sleep,
    arousal, and reward.)
*   **Mesencephalic locomotor region — canonical:** Shik, M.L., Severin,
    F.V., Orlovskii, G.N. (1966). "Control of walking and running by
    means of electrical stimulation of the mid-brain." *Biophysics*
    11:756–765. (Mesencephalic locomotor region — original discovery;
    the PPN and the cuneiform nucleus as the MLR components.)
*   **PPN and locomotion — modern review:** Takakusaki, K., Habaguchi,
    T., Ohtinata-Sugimoto, J., Saitoh, K., Sakamoto, T. (2003). "Basal
    ganglia efferents to the brainstem centers controlling postural
    muscle tone and locomotion: a new concept for understanding motor
    disorders in basal ganglia dysfunction." *Neuroscience Research*
    47:219–233. (PPN — locomotion and posture; basal ganglia
    projections.)
*   **PPN and REM sleep:** Steriade, M., McCarley, R.W. (2005). *Brain
    Control of Wakefulness and Sleep*, 2nd ed. (Cholinergic REM-sleep
    mechanisms — the LDT and PPN.)
*   **PPN and arousal:** Jones, B.E. (2008). "Modulation of cortical
    activation and behavioral arousal by cholinergic and orexinergic
    systems." *Annals of the New York Academy of Sciences*
    1129:26–34. (Cholinergic arousal — the PPN's projections to the
    brainstem and the thalamus.)
*   **PPN and reward:** Mena-Segovia, J., Bolam, J.P. (2017). "Rethinking
    the pedunculopontine nucleus." *Trends in Neurosciences*
    40:142–150. (PPN — reward, motivation, and the mesencephalic
    locomotor region.)
*   **PPN and Parkinson's disease:** Hirsch, E.C., Graybiel, A.M.,
    Duyckaerts, C., Javoy-Agid, F. (1987). "Neuronal loss in the
    pedunculopontine tegmental nucleus in Parkinson disease and in
    progressive supranuclear palsy." *Proceedings of the National
    Academy of Sciences* 84:5976–5980. (PPN — cholinergic degeneration
    in Parkinson's disease and PSP.)
*   **PPN deep brain stimulation — Parkinson's disease:** Stefani, A.,
    Lozano, A.M., Peppe, A., et al. (2007). "Bilateral deep brain
    stimulation of the pedunculopontine and subthalamic nuclei in severe
    Parkinson's disease." *Brain* 130:1596–1607. (PPN deep brain
    stimulation — gait and postural impairment in Parkinson's disease.)
*   **PPN and progressive supranuclear palsy:** Zweig, R.M., Whitehouse,
    P.J., Casanova, M.F., et al. (1987). "Loss of pedunculopontine
    neurons in progressive supranuclear palsy." *Annals of Neurology*
    22:18–25. (PPN — cholinergic degeneration in progressive
    supranuclear palsy.)
*   **PPN and REM sleep behavior disorder:** Boeve, B.F., Silber, M.H.,
    Ferman, T.J., et al. (2001). "Association of REM sleep behavior
    disorder and neurodegenerative disease may reflect an underlying
    synucleinopathy." *Movement Disorders* 16:622–630. (RBD — pontine
    REM-sleep nuclei involvement, including the PPN.)
*   **PPN and narcolepsy:** Nishino, S., Ripley, B., Overeem, S.,
    Lammers, G.J., Mignot, E. (2000). "Hypocretin (orexin) deficiency in
    human narcolepsy." *Lancet* 355:39–40. (Narcolepsy — orexin
    deficiency; cholinergic REM-sleep dysregulation — the PPN.)
*   **PPN and schizophrenia:** Raedler, T.J., Knable, M.B., Jones,
    D.W., et al. (2003). "In vivo determination of muscarinic receptor
    availability in schizophrenia." *American Journal of Psychiatry*
    160:118–125. (Schizophrenia — cholinergic dysfunction; the PPN's
    projections to the basal ganglia and the thalamus.)
*   **PPN and Alzheimer's disease:** Mufson, E.J., Ginsberg, S.D.,
    Ikonomovic, M.D., DeKosky, S.T. (2003). "Human cholinergic basal
    forebrain: chemoanatomy and neurologic dysfunction." *Journal of
    Chemical Neuroanatomy* 26:233–242. (Alzheimer's disease —
    cholinergic basal forebrain and pontine degeneration, including the
    PPN.)
*   **Pontine/midbrain stroke — PPN involvement:** Bassetti, C.,
    Bogousslavsky, J., Barth, A., Regli, F. (1996). "Isolated infarcts
    of the pontine nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — pontine tegmentum involvement,
    including the PPN.)
*   **Laterodorsal tegmental nucleus (contrast — the OTHER CHOLINERGIC
    neuromodulatory sibling):** Mesulam, M.M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the rat:
    an overview based on an alternative nomenclature (Ch1-Ch6)."
    *Neuroscience* 10:1185–1201. (LDT — cholinergic neuromodulatory
    nucleus; sibling of the PPN.)
*   **Locus coeruleus (contrast — the NORADRENERGIC neuromodulatory
    sibling):** Aston-Jones, G., Cohen, J.D. (2005). "An integrative
    theory of locus coeruleus-norepinephrine function: adaptive gain
    and optimal performance." *Annual Review of Neuroscience*
    28:403–450. (Locus coeruleus — noradrenergic neuromodulatory
    nucleus; sibling of the PPN.)
*   **Nucleus incertus (contrast — the RELAXIN-3 sibling):** Ryan, P.J.,
    Ma, S., Olucha-Bordonau, F.E., Gundlach, A.L. (2011). "Nucleus
    incertus — an emerging role in the behavioural actions of
    relaxin-3." *British Journal of Pharmacology* 162:1115–1126.
    (Nucleus incertus — relaxin-3 stress, arousal, and feeding; sibling
    of the PPN.)
*   **Pontine micturition center (contrast — the MICTURITION sibling):**
    Barrington, F.J.F. (1925). "The effect of lesions of the hind- and
    mid-brain on micturition in the cat." *Quarterly Journal of
    Experimental Physiology* 15:81–102. (Pontine micturition center —
    micturition control; sibling of the PPN.)
*   **Tegmental pontine reticular nucleus (contrast — the MOTOR RELAY
    sibling):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Tegmental pontine reticular
    nucleus — motor relay; sibling of the PPN.)
*   **Cuneiform nucleus (contrast — the OTHER mesencephalic locomotor
    region component):** Shik, M.L., Severin, F.V., Orlovskii, G.N.
    (1966). "Control of walking and running by means of electrical
    stimulation of the mid-brain." *Biophysics* 11:756–765. (Cuneiform
    nucleus — the other component of the mesencephalic locomotor
    region; glutamatergic; distinct from the PPN.)
*   **Substantia nigra and ventral tegmental area (contrast — the
    DOPAMINERGIC nuclei):** Björklund, A., Dunnett, S.B. (2007).
    "Dopamine neuron systems in the brain: an update." *Trends in
    Neurosciences* 30:194–202. (Substantia nigra and VTA —
    dopaminergic nuclei; distinct from the PPN.)
*   **Raphe nuclei (contrast — the SEROTONERGIC nuclei):** Hornung,
    J.P. (2003). "The human raphe nuclei and the serotonergic system."
    *Journal of Chemical Neuroanatomy* 26:331–343. (Raphe nuclei —
    serotonergic nuclei; distinct from the PPN.)
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
*   **PPRF (contrast — a separate pons child):** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (PPRF —
    horizontal saccadic burst generator; distinct from the pontine
    tegmentum container in the tree.)
*   **Parvocellular reticular nucleus (contrast — a separate pons
    child):** Brodal, A. (2010). *The Central Nervous System: Structure
    and Function*, 4th ed. (Parvocellular reticular nucleus — orofacial
    premotor and autonomic relay; distinct from the pontine tegmentum
    container in the tree.)
*   **Pontine nuclei (contrast — in the BASILAR pons):** Brodal, A.
    (2010). *The Central Nervous System: Structure and Function*, 4th
    ed. (Pontine nuclei — cortico-ponto-cerebellar relay in the basilar
    pons; distinct from the PPN.)
*   **Fourth ventricle (contrast — a CSF space):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Fourth ventricle — CSF space dorsal to the pons; distinct from the
    PPN.)
*   **Midbrain tegmentum (contrast — a PONTOMESENCEPHALIC vs. purely
    midbrain boundary):** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Midbrain tegmentum —
    dorsal midbrain; distinct from the pontine tegmentum; the PPN is a
    pontomesencephalic boundary case.)
*   **SLEA (contrast — the PPN is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the PPN.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the PPN.)
*   NeuroNames — Pedunculopontine nucleus; FMA — Pedunculopontine
    nucleus.
"""
