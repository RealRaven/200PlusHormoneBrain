"""
infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum.nucleus_incertus
================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── tegmentum
                └── nucleus_incertus   <-- THIS MODULE

**Primary synonym:** Nucleus incertus; NI; nucleus incertus of the pons;
"the pontine relaxin-3 nucleus"; "the pontine stress and arousal
relaxin-3 nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — an **anatomically delimited
relaxin-3-expressing (with GABAergic and glutamatergic components)
nucleus** in the **dorsal pontine tegmentum**, near the **midline** and
just **ventral to the fourth ventricle**, **ventrolateral to the
laterodorsal tegmental nucleus** and **ventromedial to the locus
coeruleus**. It is the **pontine relaxin-3 nucleus** — the **principal
source of relaxin-3** in the **brain** — and the **neural substrate** of
**relaxin-3 stress, arousal, feeding, and neuroendocrine regulation**.
**Part of:** The **tegmentum** container — specifically, the
**neuromodulatory (relaxin-3)** component. The **tegmentum** is the
**dorsal pontine grey-matter region** — the **tree-wired container** for
the six neuromodulatory and autonomic nuclei of the dorsal pons.
**Structural parent:** ``.../tegmentum/`` → **direct child** of the
tegmentum container.
**Structural children:** **None.** This is a **leaf** module. The
**relaxin-3-expressing principal neurons**, the **GABAergic neurons**,
and the **glutamatergic neurons** are documented as **prose**, not as
structural children — they are the **functionally distinct neuron
populations** within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
nucleus incertus is a LEAF, not a container.** It has **no structural
children**. The **relaxin-3-expressing principal neurons**, the
**GABAergic neurons**, and the **glutamatergic neurons** are **prose**
populations, not structural children. Consumers must **not** treat the
nucleus incertus as a container, and must **not** assume the neuron
populations exist as sub-modules.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the nucleus incertus is a SINGLE module at the tree
level, even though the NI is BILATERAL in real anatomy.** Unlike the
**cranial_nerve_nuclei** module (which has explicit ``left`` and
``right`` structural children) or the **superior_olivary_complex**
module (which has ``left`` and ``right`` sub-containers), the
**nucleus_incertus** module (here) is a **single module** that
represents the **bilateral NI** (the left NI and the right NI). The tree
does **not** split them into left/right. Consumers must **not** assume a
left/right split exists at the tree level — the module is a **single,
bilateral representation**. Any lateralization is documented **here, in
the Lateralization Notes**, not imported from elsewhere.
**Boundary status (RELAXIN-3 NEUROMODULATORY NUCLEUS — NOT a motor or
sensory relay):** **Boundary case — the nucleus incertus is a RELAXIN-3
NEUROMODULATORY nucleus, NOT a motor or sensory relay.** Unlike the
**cranial nerve motor nuclei** (branchial or somatic motor relays) or the
**sensory nuclei** (e.g., the cochlear nuclei, the trigeminal nuclei),
the **nucleus incertus** (here) is a **neuromodulatory nucleus** — its
**relaxin-3-expressing (with GABAergic and glutamatergic components)**
neurons **project diffusely** to the **septum**, the **hippocampus**, the
**medial prefrontal cortex**, the **amygdala**, the **hypothalamus**, and
the **brainstem** to **modulate** the **excitability** of their targets
— they **do not** directly **relay** motor commands or **transmit**
sensory information. **This distinction is functionally load-bearing** —
the nucleus incertus is a **state-setting** nucleus (stress, arousal,
feeding, neuroendocrine), not a **throughput** nucleus. Consumers must
**not** conflate the nucleus incertus with a motor or sensory relay.
**Boundary status (RELAXIN-3 — NOT a cholinergic, noradrenergic,
dopaminergic, or serotonergic nucleus):** **Boundary case — the nucleus
incertus is RELAXIN-3-EXPRESSING, NOT a cholinergic, noradrenergic,
dopaminergic, or serotonergic nucleus.** The **nucleus incertus**
neurons are **relaxin-3-expressing** — they synthesize **relaxin-3**
(a member of the **insulin/relaxin superfamily** of peptides) and
release it as their **principal neuromodulator**. The **relaxin-3**
identity of the nucleus incertus is its **defining neurochemical
signature** — the **other pontine tegmentum nuclei** use **different
neurotransmitters** (noradrenaline for the locus coeruleus;
acetylcholine for the LDT and PPN; the pontine micturition center and
the tegmental pontine reticular nucleus are **glutamatergic/GABAergic**).
**This distinction is neurochemically load-bearing** — the nucleus
incertus is the **sole brainstem relaxin-3 nucleus** (the **other
relaxin-3 source** is the **periventricular nucleus of the
hypothalamus**, but the **nucleus incertus is the primary source of
relaxin-3 projections to the forebrain**) — and its **relaxin-3
identity** is the **basis** of its **stress, arousal, feeding, and
neuroendocrine** functions. Consumers must **not** conflate the nucleus
incertus with the **cholinergic** nuclei (the LDT and the PPN), the
**noradrenergic** nucleus (the locus coeruleus), the **dopaminergic**
nuclei (the substantia nigra and the ventral tegmental area), or the
**serotonergic** nuclei (the raphe nuclei).
**Boundary status (NOT the locus coeruleus — that is the NORADRENERGIC
neuromodulatory nucleus):** **Boundary case — the nucleus incertus is
NOT the locus coeruleus (LC).** The **locus coeruleus**
(``.../tegmentum/locus_coeruleus/``) is the **noradrenergic** nucleus —
the **sole noradrenergic source** for the **forebrain** — it is
involved in **arousal**, **attention**, **stress**, **pain
modulation**, and **memory consolidation**. The **nucleus incertus**
(here) is the **relaxin-3** nucleus — it is involved in **stress**,
**arousal**, **feeding**, and **neuroendocrine regulation**. They are
**DIFFERENT STRUCTURES** — different neurotransmitters (relaxin-3 vs.
noradrenaline), different functional systems (relaxin-3
stress/arousal/feeding/neuroendocrine vs. noradrenergic
arousal/attention/stress/pain/memory), different projection targets
(septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus vs.
diffuse noradrenergic). They are **anatomically adjacent** (both are in
the **dorsal pontine tegmentum**) — this proximity is a **classic source
of confusion** — consumers must **not** conflate the nucleus incertus
with the locus coeruleus.
**Boundary status (NOT the laterodorsal tegmental nucleus — that is the
CHOLINERGIC neuromodulatory nucleus):** **Boundary case — the nucleus
incertus is NOT the laterodorsal tegmental nucleus (LDT).** The
**laterodorsal tegmental nucleus**
(``.../tegmentum/laterodorsal_tegmental_nucleus/``) is the **cholinergic**
nucleus — the **principal pontine cholinergic source** for the
**thalamus** — it is involved in **REM sleep**, **arousal**, and
**motivation**. The **nucleus incertus** (here) is the **relaxin-3**
nucleus. They are **DIFFERENT STRUCTURES** — different neurotransmitters
(relaxin-3 vs. acetylcholine), different functional systems (relaxin-3
stress/arousal/feeding/neuroendocrine vs. cholinergic
REM-sleep/arousal/motivation), different projection targets
(septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus vs.
thalamus/basal forebrain). They are **anatomically adjacent** (both are
in the **dorsal pontine tegmentum**) — this proximity is a **classic
source of confusion** — consumers must **not** conflate the nucleus
incertus with the laterodorsal tegmental nucleus.
**Boundary status (NOT the pedunculopontine nucleus — that is the
CHOLINERGIC LOCOMOTION nucleus):** **Boundary case — the nucleus
incertus is NOT the pedunculopontine nucleus (PPN).** The
**pedunculopontine nucleus**
(``.../tegmentum/pedunculopontine_nucleus/``) is the **cholinergic**
(with glutamatergic and GABAergic components) nucleus — the
**mesencephalic locomotor region** — it is involved in **locomotion**,
**REM sleep**, **arousal**, and **reward**. The **nucleus incertus**
(here) is the **relaxin-3** nucleus. They are **DIFFERENT STRUCTURES** —
different neurotransmitters (relaxin-3 vs. acetylcholine), different
functional systems (relaxin-3 stress/arousal/feeding/neuroendocrine vs.
cholinergic locomotion/REM-sleep/arousal/reward), different anatomical
locations (the NI is **dorsomedial** near the fourth ventricle; the PPN
is **ventrolateral** at the pontomesencephalic junction). Consumers must
**not** conflate the nucleus incertus with the pedunculopontine nucleus.
**Boundary status (NOT the pontine micturition center — that is the
MICTURITION nucleus):** **Boundary case — the nucleus incertus is NOT
the pontine micturition center (Barrington's nucleus).** The **pontine
micturition center**
(``.../tegmentum/pontine_micturition_center/``) is the **micturition
control center** — it **coordinates** the **micturition reflex**
(bladder contraction and sphincter relaxation). The **nucleus incertus**
(here) is the **relaxin-3** nucleus. They are **DIFFERENT STRUCTURES** —
different functional systems (relaxin-3 stress/arousal/feeding/
neuroendocrine vs. micturition), different projection targets
(septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus vs.
sacral spinal cord). Consumers must **not** conflate the nucleus incertus
with the pontine micturition center.
**Boundary status (NOT the tegmental pontine reticular nucleus — that is
the MOTOR RELAY nucleus):** **Boundary case — the nucleus incertus is
NOT the tegmental pontine reticular nucleus.** The **tegmental pontine
reticular nucleus**
(``.../tegmentum/tegmental_pontine_reticular_nucleus/``) is a **motor
relay** — it **projects** to the **spinal cord** (via the
**reticulospinal tract**) and to the **cerebellum** (via the
**pontocerebellar fibers**) — it is involved in **locomotion**,
**posture**, and **motor pattern generation**. The **nucleus incertus**
(here) is the **relaxin-3** nucleus. They are **DIFFERENT STRUCTURES** —
different functional systems (relaxin-3 stress/arousal/feeding/
neuroendocrine vs. motor relay), different projection targets
(septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus vs.
spinal cord/cerebellum). Consumers must **not** conflate the nucleus
incertus with the tegmental pontine reticular nucleus.
**Boundary status (NOT the parabrachial area — that is a SEPARATE
structural child of the pons):** **Boundary case — the nucleus incertus
is NOT the parabrachial area.** The **parabrachial area**
(``.../pons/parabrachial_area/``) is the **visceral-sensory and
respiratory-relay complex** — it is a **separate structural child of the
pons**, **not** a structural child of the pontine tegmentum, **even
though** it is **anatomically located** in the **pontine tegmentum**.
The **nucleus incertus** (here) is a **relaxin-3 neuromodulatory
nucleus** — a **structural child of the pontine tegmentum container**.
Consumers must **not** conflate the nucleus incertus with the
parabrachial area.
**Boundary status (NOT the superior olivary complex, the cranial nerve
nuclei, the PPRF, or the parvocellular reticular nucleus — those are
SEPARATE structural children of the pons):** **Boundary case — the
nucleus incertus is NOT the superior olivary complex, the cranial nerve
nuclei, the PPRF, or the parvocellular reticular nucleus.** Those are
**separate structural children of the pons** — the **superior olivary
complex** (binaural sound-localization relay), the **cranial nerve
nuclei** (CN V, VI, VII, VIII nuclei), the **PPRF** (horizontal
saccadic burst generator), and the **parvocellular reticular nucleus**
(orofacial premotor and autonomic relay). The **nucleus incertus**
(here) is a **relaxin-3 neuromodulatory nucleus** — a **structural
child of the pontine tegmentum container**. Consumers must **not**
conflate the nucleus incertus with any of them.
**Boundary status (NOT the pontine nuclei — those are in the BASILAR
pons):** **Boundary case — the nucleus incertus is NOT the pontine
nuclei.** The **pontine nuclei** (``.../pons/pontine_nuclei/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons** — the
**ventral** portion of the pons. The **nucleus incertus** (here) is a
**relaxin-3 neuromodulatory nucleus** in the **dorsal pontine
tegmentum**. They are **DIFFERENT PONTS SUB-DIVISIONS** — consumers must
**not** conflate the nucleus incertus with the pontine nuclei.
**Boundary status (NOT the whole tegmentum container — that is the
PARENT):** **Boundary case — the nucleus incertus is NOT the whole
tegmentum container; the tegmentum container is the PARENT.** The
**tegmentum** container (``.../pons/tegmentum/``) is the **dorsal
pontine grey-matter region** — the **tree-wired container** for the
**six neuromodulatory and autonomic nuclei** (locus coeruleus,
laterodorsal tegmental nucleus, nucleus incertus, pedunculopontine
nucleus, pontine micturition center, tegmental pontine reticular
nucleus). The **nucleus incertus** (here) is **one of the six structural
children** of the tegmentum container. Consumers must **not** conflate
the nucleus incertus with the **whole tegmentum**.
**Boundary status (NOT the whole pons — the pons is the GRANDPARENT):**
**Boundary case — the nucleus incertus is NOT the whole pons; the pons
is the GRANDPARENT.** The **pons** (``.../pons/``) is the **whole
metencephalic brainstem segment** — it contains the **basilar pons**,
the **pontine tegmentum**, the **parabrachial area**, the **superior
olivary complex**, the **cranial nerve nuclei**, the **PPRF**, the
**parvocellular reticular nucleus**, the **pontine nuclei**, and the
**six neuromodulatory and autonomic nuclei** of the tegmentum container.
The **nucleus incertus** (here) is **one of the six neuromodulatory and
autonomic nuclei** only. Consumers must **not** conflate the nucleus
incertus with the **whole pons**.
**Boundary status (NOT the fourth ventricle — that is a CSF SPACE):**
**Boundary case — the nucleus incertus is NOT the fourth ventricle.** The
**fourth ventricle** (``.../metencephalon/fourth_ventricle/``) is the
**CSF-filled space** **dorsal to** the pons and **ventral to** the
cerebellum. The **nucleus incertus** (here) is a **grey-matter nucleus**
that sits **just ventral to** the fourth ventricle (in the **pontine
tegmentum**). They are **DIFFERENT STRUCTURES** — the **fourth
ventricle** is a **fluid space**; the **nucleus incertus** is **neural
tissue**. Consumers must **not** conflate the nucleus incertus with the
fourth ventricle.
**Boundary status (NOT the midbrain tegmentum or the medullary
tegmentum — those are DIFFERENT BRAINSTEM LEVELS):** **Boundary case —
the nucleus incertus is NOT the midbrain tegmentum or the medullary
tegmentum.** The **midbrain tegmentum** (``.../midbrain/tegmentum/``)
is the **dorsal portion of the midbrain** — it contains the **substantia
nigra** and the **ventral tegmental area** (the **dopaminergic**
nuclei), the **red nucleus**, the **periaqueductal gray**, the
**oculomotor nucleus**, the **trochlear nucleus**, the **mesencephalic
trigeminal nucleus**, the **riMLF**, the **cMRF**, and other **midbrain
structures**. The **medullary tegmentum** is the **dorsal portion of
the medulla oblongata** — it contains the **solitary nucleus**, the
**dorsal motor nucleus of the vagus**, the **hypoglossal nucleus**, the
**nucleus ambiguus**, the **inferior olivary nucleus**, the
**gigantocellular reticular nucleus**, the **paramedian reticular
nucleus**, and other **medullary structures**. The **nucleus incertus**
(here) is a **specific nucleus** in the **dorsal portion of the pons**.
They are **DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate
the nucleus incertus with the midbrain tegmentum or the medullary
tegmentum.
**Boundary status (RELAXIN-3 — NOT the hypothalamic periventricular
nucleus, which is the OTHER relaxin-3 source):** **Boundary case — the
nucleus incertus is RELAXIN-3-EXPRESSING, but it is NOT the hypothalamic
periventricular nucleus (the other relaxin-3 source).** The **hypothalamic
periventricular nucleus** is the **other relaxin-3-expressing nucleus**
in the brain — it is located in the **hypothalamus** (the
**periventricular region**, the **anterior hypothalamic area**, and the
**medial preoptic area**). The **nucleus incertus** (here) is the
**pontine relaxin-3 nucleus** — the **principal source of relaxin-3
projections to the forebrain**. They are **DIFFERENT STRUCTURES** —
different anatomical locations (pons vs. hypothalamus), different
functional emphases (the nucleus incertus is the **principal pontine
relaxin-3 nucleus**; the hypothalamic periventricular nucleus is the
**hypothalamic relaxin-3 source**). **They are both relaxin-3** — this
shared neurotransmitter is a **classic source of confusion** — consumers
must **not** conflate the nucleus incertus with the hypothalamic
periventricular nucleus. **The nucleus incertus is the primary source**
of relaxin-3 projections to the **septum**, the **hippocampus**, the
**medial prefrontal cortex**, the **amygdala**, and the **brainstem**
(the hypothalamic periventricular nucleus is the **primary source** of
relaxin-3 projections to the **hypothalamus** itself).
**Boundary status (MULTIPLE NEUROCHEMICALLY DISTINCT NEURON
POPULATIONS — relaxin-3, GABAergic, and glutamatergic):** **Boundary
case — the nucleus incertus is NOT a single uniform neuron population;
it contains MULTIPLE neurochemically distinct populations.** The
**relaxin-3-expressing principal neurons** — the **majority** of the NI
neurons that **co-express relaxin-3** with **GABA** or **glutamate**
(or both) — they are the **relaxin-3 output** of the NI, and they are
the **principal source of relaxin-3** in the brain. The **GABAergic
neurons** — the **NI neurons that are GABAergic** (with or without
relaxin-3 co-expression) — they **contribute** to the **inhibitory
modulation** of the NI's targets. The **glutamatergic neurons** — the
**NI neurons that are glutamatergic** (with or without relaxin-3
co-expression) — they **contribute** to the **excitatory modulation**
of the NI's targets. **These populations are prose, not structural
children.** Consumers must **not** treat the nucleus incertus as a
single uniform population — it is a **neurochemically heterogeneous
nucleus** with **distinct** sub-circuits, and the **relaxin-3
co-expression** with **GABA** or **glutamate** is an **important
functional feature** of the nucleus.
**Boundary status (SLEA-FREE — the nucleus incertus is NOT an
extended-amygdala component):** **Boundary case — the nucleus incertus
is SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus**
(the **only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired elsewhere). The
**nucleus incertus** is a **relaxin-3 neuromodulatory nucleus** — it is
**NOT** an extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into the
nucleus incertus — it is **SLEA-free**.

Overview
--------
The nucleus incertus is the **pontine relaxin-3 nucleus** of the
**pontine tegmentum** — a **neurochemically heterogeneous**
grey-matter nucleus in the **dorsal pontine tegmentum**, near the
**midline** and just **ventral to the fourth ventricle**. It is a
**leaf** module under the tegmentum container, and it is the **principal
source of relaxin-3** in the **brain** — the **neural substrate** of
**relaxin-3 stress, arousal, feeding, and neuroendocrine regulation**.

**The nucleus incertus is a LEAF, not a container.** It has **no
structural children**. The **relaxin-3-expressing principal neurons**,
the **GABAergic neurons**, and the **glutamatergic neurons** are **prose
populations**, not structural children.

**The nucleus incertus is a SINGLE module at the tree level.** The tree
does **not** split the NI into left/right — the module is a **single,
bilateral representation**.

**The nucleus incertus is a RELAXIN-3 NEUROMODULATORY NUCLEUS, NOT a
motor or sensory relay.** It **projects diffusely** to the **septum**,
the **hippocampus**, the **medial prefrontal cortex**, the **amygdala**,
the **hypothalamus**, and the **brainstem** to **modulate** the
**excitability** of its targets — it does **not** directly **relay**
motor commands or **transmit** sensory information.

**The nucleus incertus is RELAXIN-3-EXPRESSING, NOT cholinergic,
noradrenergic, dopaminergic, or serotonergic.** It is the **principal
source of relaxin-3** in the brain. The **cholinergic** nuclei (the LDT
and the PPN), the **noradrenergic** nucleus (the locus coeruleus), the
**dopaminergic** nuclei (the substantia nigra and the ventral tegmental
area), and the **serotonergic** nuclei (the raphe nuclei) are
**different structures** — different neurotransmitters and different
functional systems.

**The nucleus incertus is NOT the locus coeruleus, the laterodorsal
tegmental nucleus, the pedunculopontine nucleus, the pontine micturition
center, or the tegmental pontine reticular nucleus.** Those are the
**other five** neuromodulatory and autonomic nuclei of the **pontine
tegmentum container** — different neurotransmitters, different
functional systems, different projection targets.

**The nucleus incertus is NOT the hypothalamic periventricular
nucleus.** The **hypothalamic periventricular nucleus** is the **other
relaxin-3-expressing nucleus** in the brain — it is located in the
**hypothalamus**, and it is the **primary source** of relaxin-3
projections to the **hypothalamus** itself. The **nucleus incertus** is
the **pontine relaxin-3 nucleus** — the **principal source** of
relaxin-3 projections to the **forebrain** (the **septum**, the
**hippocampus**, the **medial prefrontal cortex**, the **amygdala**, and
the **brainstem**).

**The nucleus incertus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The nucleus incertus contains **multiple neurochemically distinct
neuron populations** — documented as **prose**, not as structural
children:

*   **Relaxin-3-expressing principal neurons** — the **majority** of the
    NI neurons — they **synthesize** and **release relaxin-3** (a member
    of the **insulin/relaxin superfamily** of peptides). They
    **co-express** relaxin-3 with **GABA** or **glutamate** (or both) —
    the **co-transmitter** (GABA or glutamate) **modulates** the
    **relaxin-3 signal** at the **target** (GABA is **inhibitory**;
    glutamate is **excitatory**). They **project** to the **medial
    septum**, the **diagonal band of Broca**, the **hippocampus**, the
    **medial prefrontal cortex**, the **amygdala**, the **hypothalamus**
    (the **paraventricular nucleus**, the **lateral hypothalamic area**,
    the **arcuate nucleus**, the **dorsomedial hypothalamic nucleus**),
    and the **brainstem** (the **dorsal raphe nucleus**, the
    **laterodorsal tegmental nucleus**, the **locus coeruleus**, the
    **parabrachial area**, the **solitary nucleus**, the **nucleus
    ambiguus**, the **ventral respiratory group**). **Relaxin-3 stress,
    arousal, feeding, and neuroendocrine modulation are the functional
    systems** subserved primarily by the relaxin-3-expressing principal
    neurons.

*   **GABAergic neurons** — the **NI neurons that are GABAergic** (with
    or without relaxin-3 co-expression). They **release GABA** at their
    **axon terminals** — the **inhibitory** neurotransmitter that
    **modulates** the **excitability** of the NI's targets. They
    **contribute** to the **inhibitory modulation** of the NI's targets
    — including the **septum**, the **hippocampus**, the **medial
    prefrontal cortex**, and the **hypothalamus**. **GABAergic
    modulation is the functional system** subserved primarily by the
    GABAergic neurons.

*   **Glutamatergic neurons** — the **NI neurons that are
    glutamatergic** (with or without relaxin-3 co-expression). They
    **release glutamate** at their **axon terminals** — the
    **excitatory** neurotransmitter that **modulates** the
    **excitability** of the NI's targets. They **contribute** to the
    **excitatory modulation** of the NI's targets — including the
    **septum**, the **hippocampus**, the **medial prefrontal cortex**,
    and the **hypothalamus**. **Glutamatergic modulation is the
    functional system** subserved primarily by the glutamatergic
    neurons.

**These populations are prose, not structural children.** The tree
wires the **nucleus incertus** as a **single leaf** under the tegmentum
container — the **relaxin-3-expressing principal neurons**, the
**GABAergic neurons**, and the **glutamatergic neurons** are **prose**,
not structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Nucleus Incertus / Locus Coeruleus Boundary
-----------------------------------------------
This is the **sibling** boundary — **relaxin-3 vs. noradrenergic
neuromodulatory nucleus**:

*   **Nucleus incertus** (this module) — the **relaxin-3** nucleus —
    involved in **stress**, **arousal**, **feeding**, and
    **neuroendocrine regulation**.

*   **Locus coeruleus** (``.../tegmentum/locus_coeruleus/``) — the
    **noradrenergic** nucleus — the **principal source of
    norepinephrine** in the brain — involved in **arousal**,
    **attention**, **stress**, **pain modulation**, and **memory
    consolidation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(relaxin-3 vs. noradrenaline), different functional systems (relaxin-3
stress/arousal/feeding/neuroendocrine vs. noradrenergic
arousal/attention/stress/pain/memory), different projection targets
(septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus vs.
diffuse noradrenergic). They are **anatomically adjacent** (both are in
the **dorsal pontine tegmentum**) — this proximity is a **classic
source of confusion** — consumers must **not** conflate the nucleus
incertus with the locus coeruleus.

The Nucleus Incertus / Laterodorsal Tegmental Nucleus Boundary
--------------------------------------------------------------
This is the **sibling** boundary — **relaxin-3 vs. cholinergic
neuromodulatory nucleus**:

*   **Nucleus incertus** (this module) — the **relaxin-3** nucleus.

*   **Laterodorsal tegmental nucleus**
    (``.../tegmentum/laterodorsal_tegmental_nucleus/``) — the
    **cholinergic** nucleus — the **principal pontine cholinergic
    source** for the **thalamus** — involved in **REM sleep**,
    **arousal**, and **motivation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(relaxin-3 vs. acetylcholine), different functional systems (relaxin-3
stress/arousal/feeding/neuroendocrine vs. cholinergic
REM-sleep/arousal/motivation), different projection targets
(septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus vs.
thalamus/basal forebrain). They are **anatomically adjacent** (both are
in the **dorsal pontine tegmentum**) — this proximity is a **classic
source of confusion** — consumers must **not** conflate the nucleus
incertus with the laterodorsal tegmental nucleus.

The Nucleus Incertus / Pedunculopontine Nucleus Boundary
--------------------------------------------------------
This is the **sibling** boundary — **relaxin-3 vs. cholinergic
locomotion nucleus**:

*   **Nucleus incertus** (this module) — the **relaxin-3** nucleus.

*   **Pedunculopontine nucleus**
    (``.../tegmentum/pedunculopontine_nucleus/``) — the **cholinergic**
    (with glutamatergic and GABAergic components) nucleus — the
    **mesencephalic locomotor region** — involved in **locomotion**,
    **REM sleep**, **arousal**, and **reward**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(relaxin-3 vs. acetylcholine), different functional systems (relaxin-3
stress/arousal/feeding/neuroendocrine vs. cholinergic
locomotion/REM-sleep/arousal/reward), different anatomical locations
(the NI is **dorsomedial** near the fourth ventricle; the PPN is
**ventrolateral** at the pontomesencephalic junction). Consumers must
**not** conflate the nucleus incertus with the pedunculopontine nucleus.

The Nucleus Incertus / Pontine Micturition Center Boundary
----------------------------------------------------------
This is the **sibling** boundary — **relaxin-3 vs. micturition**:

*   **Nucleus incertus** (this module) — the **relaxin-3** nucleus.

*   **Pontine micturition center**
    (``.../tegmentum/pontine_micturition_center/``) — the **micturition
    control center** — it **coordinates** the **micturition reflex**.

**They are DIFFERENT STRUCTURES** — different functional systems
(relaxin-3 stress/arousal/feeding/neuroendocrine vs. micturition),
different projection targets (septum/hippocampus/medial prefrontal
cortex/amygdala/hypothalamus vs. sacral spinal cord). Consumers must
**not** conflate the nucleus incertus with the pontine micturition
center.

The Nucleus Incertus / Tegmental Pontine Reticular Nucleus Boundary
-------------------------------------------------------------------
This is the **sibling** boundary — **relaxin-3 vs. motor relay**:

*   **Nucleus incertus** (this module) — the **relaxin-3** nucleus.

*   **Tegmental pontine reticular nucleus**
    (``.../tegmentum/tegmental_pontine_reticular_nucleus/``) — the
    **motor relay** — it **projects** to the **spinal cord** and the
    **cerebellum** — it is involved in **locomotion**, **posture**, and
    **motor pattern generation**.

**They are DIFFERENT STRUCTURES** — different functional systems
(relaxin-3 stress/arousal/feeding/neuroendocrine vs. motor relay),
different projection targets (septum/hippocampus/medial prefrontal
cortex/amygdala/hypothalamus vs. spinal cord/cerebellum). Consumers must
**not** conflate the nucleus incertus with the tegmental pontine
reticular nucleus.

The Nucleus Incertus / Parabrachial Area Boundary
-------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Nucleus incertus** (this module) — a **relaxin-3 neuromodulatory
    nucleus** — a **structural child of the pontine tegmentum
    container**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex** — a **separate
    structural child of the pons**.

**They are DIFFERENT STRUCTURES** — the parabrachial area is **not** a
structural child of the pontine tegmentum (in the tree), even though it
is **anatomically located** in the pontine tegmentum. Consumers must
**not** conflate the nucleus incertus with the parabrachial area.

The Nucleus Incertus / Superior Olivary Complex, Cranial Nerve Nuclei, PPRF, and Parvocellular Reticular Nucleus Boundary
------------------------------------------------------------------------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Nucleus incertus** (this module) — a **relaxin-3 neuromodulatory
    nucleus** — a **structural child of the pontine tegmentum
    container**.

*   **Superior olivary complex** (``.../pons/superior_olivary_complex/``),
    **cranial nerve nuclei** (``.../pons/cranial_nerve_nuclei/``),
    **PPRF** (``.../pons/paramedian_pontine_reticular_formation/``),
    **parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``) — **separate
    structural children of the pons**.

**They are DIFFERENT STRUCTURES** — those four structures are **not**
structural children of the pontine tegmentum (in the tree), even though
they are **anatomically located** in the pontine tegmentum. Consumers
must **not** conflate the nucleus incertus with any of them.

The Nucleus Incertus / Pontine Nuclei Boundary
----------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Nucleus incertus** (this module) — a **relaxin-3 neuromodulatory
    nucleus** in the **dorsal pontine tegmentum**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not**
conflate the nucleus incertus with the pontine nuclei.

The Nucleus Incertus / Whole Tegmentum Container Boundary
---------------------------------------------------------
This is the **sub-nucleus vs. parent** boundary:

*   **Nucleus incertus** (this module) — one of the **six neuromodulatory
    and autonomic nuclei** of the pontine tegmentum.

*   **Tegmentum container** (``.../pons/tegmentum/``) — the **dorsal
    pontine grey-matter region** — the **tree-wired container** for the
    **six neuromodulatory and autonomic nuclei**.

**The nucleus incertus is a child of the tegmentum container.**
Consumers must **not** conflate the nucleus incertus with the **whole
tegmentum**.

The Nucleus Incertus / Whole Pons Boundary
------------------------------------------
This is the **nucleus vs. grandparent** boundary:

*   **Nucleus incertus** (this module) — one of the **six neuromodulatory
    and autonomic nuclei** of the pontine tegmentum.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**.

**The nucleus incertus is a grandchild of the pons** (via the tegmentum
container). Consumers must **not** conflate the nucleus incertus with the
**whole pons**.

The Nucleus Incertus / Fourth Ventricle Boundary
------------------------------------------------
This is the **neural tissue vs. CSF space** boundary:

*   **Nucleus incertus** (this module) — a **grey-matter nucleus** that
    sits **just ventral to** the fourth ventricle.

*   **Fourth ventricle** (``.../metencephalon/fourth_ventricle/``) — the
    **CSF-filled space** **dorsal to** the pons.

**They are DIFFERENT STRUCTURES** — the **fourth ventricle** is a
**fluid space**; the **nucleus incertus** is **neural tissue**. Consumers
must **not** conflate the nucleus incertus with the fourth ventricle.

The Nucleus Incertus / Midbrain Tegmentum and Medullary Tegmentum Boundary
--------------------------------------------------------------------------
This is the **pons vs. midbrain/medulla** boundary:

*   **Nucleus incertus** (this module) — a **specific nucleus** in the
    **dorsal portion of the pons**.

*   **Midbrain tegmentum** (``.../midbrain/tegmentum/``) and **medullary
    tegmentum** — the **dorsal portions** of the **midbrain** and the
    **medulla oblongata**.

**They are DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate
the nucleus incertus with the midbrain tegmentum or the medullary
tegmentum.

The Nucleus Incertus / Hypothalamic Periventricular Nucleus Boundary
--------------------------------------------------------------------
This is the **pontine relaxin-3 vs. hypothalamic relaxin-3** boundary:

*   **Nucleus incertus** (this module) — the **pontine relaxin-3
    nucleus** — the **principal source of relaxin-3 projections to the
    forebrain** (the **septum**, the **hippocampus**, the **medial
    prefrontal cortex**, the **amygdala**, and the **brainstem**).

*   **Hypothalamic periventricular nucleus** — the **other
    relaxin-3-expressing nucleus** in the brain — the **primary source
    of relaxin-3 projections to the hypothalamus** itself.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(pons vs. hypothalamus), different functional emphases (the nucleus
incertus is the **principal pontine relaxin-3 nucleus**; the
hypothalamic periventricular nucleus is the **hypothalamic relaxin-3
source**). **They are both relaxin-3** — this shared neurotransmitter is
a **classic source of confusion** — consumers must **not** conflate the
nucleus incertus with the hypothalamic periventricular nucleus.

The Nucleus Incertus / Substantia Nigra, Ventral Tegmental Area, and Raphe Nuclei Boundary
------------------------------------------------------------------------------------------
This is the **relaxin-3 vs. dopaminergic/serotonergic** boundary:

*   **Nucleus incertus** (this module) — the **relaxin-3** nucleus.

*   **Substantia nigra** (pars compacta, midbrain) and **ventral
    tegmental area** (midbrain) — the **dopaminergic** nuclei — the
    **principal sources of dopamine** in the brain.

*   **Dorsal raphe nucleus** and **median raphe nucleus**
    (midbrain/pons) — the **serotonergic** nuclei — the **principal
    sources of serotonin** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(relaxin-3 vs. dopamine vs. serotonin), different anatomical locations
(pons vs. midbrain), different functional systems (relaxin-3
stress/arousal/feeding/neuroendocrine vs. dopaminergic
reward/motor control/learning vs. serotonergic mood/sleep/appetite/
pain). Consumers must **not** conflate the nucleus incertus with the
dopaminergic or serotonergic nuclei.

The Nucleus Incertus / SLEA Boundary
------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Nucleus incertus** (this module) — **SLEA-FREE**. It is **not** an
    extended-amygdala component, and it carries **no SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The nucleus incertus is NOT part of the SLEA continuum.** It is a
**relaxin-3 neuromodulatory nucleus**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
nucleus incertus.

Function in the Human Brain
---------------------------
The nucleus incertus's functions are **the relaxin-3 modulation of
stress, arousal, feeding, and neuroendocrine regulation** — **NOT a
single unified function**:

*   **Stress Response (Relaxin-3 Activation):** The **relaxin-3-
    expressing principal neurons** of the NI **respond** to **stressful
    stimuli** — they **increase** their **firing rate** and
    **relaxin-3 release** in response to **psychological stressors**
    (e.g., **restraint stress**, **social defeat**, **predator
    exposure**) and **physiological stressors** (e.g., **hypoglycemia**,
    **hypotension**, **immune challenge**) — they **activate** the
    **hypothalamic-pituitary-adrenal (HPA) axis** (via the
    **paraventricular nucleus** of the hypothalamus) and the
    **sympathetic nervous system** (via the **brainstem autonomic
    centers**). **This "relaxin-3 stress response"** function is the
    **neural substrate** of the **NI's role in the stress response** —
    the **NI** is the **pontine relaxin-3** system that **mobilizes**
    the body **to cope with stressors**, in **concert** with the
    **locus coeruleus noradrenergic** and the **CRF hypothalamic**
    stress systems.

*   **Arousal and Theta Rhythm (Relaxin-3 Modulation of the Septum and
    Hippocampus):** The **relaxin-3-expressing principal neurons** of
    the NI **project** to the **medial septum**, the **diagonal band of
    Broca**, and the **hippocampus** — they **modulate** the
    **septohippocampal system** and the **theta rhythm** (the
    **hippocampal theta oscillation** that **underlies**
    **spatial navigation**, **memory encoding**, and **REM sleep**).
    **This "relaxin-3 arousal and theta modulation"** function is the
    **neural substrate** of the **NI's role in arousal and memory** —
    the **NI** is the **pontine relaxin-3** system that **promotes**
    the **theta rhythm** and the **arousal states** that **support**
    **spatial cognition** and **memory**.

*   **Feeding and Energy Balance (Relaxin-3 Modulation of the
    Hypothalamus):** The **relaxin-3-expressing principal neurons** of
    the NI **project** to the **arcuate nucleus**, the **paraventricular
    nucleus**, the **lateral hypothalamic area**, and the **dorsomedial
    hypothalamic nucleus** — they **modulate** the **hypothalamic
    feeding circuits** (the **NPY/AgRP** and **POMC** neurons of the
    arcuate nucleus, the **orexin** and **MCH** neurons of the lateral
    hypothalamic area) — they **promote** **food intake** and
    **regulate** **energy balance**. **This "relaxin-3 feeding and
    energy balance"** function is the **neural substrate** of the
    **NI's role in feeding** — the **NI** is the **pontine relaxin-3**
    system that **modulates** the **hypothalamic feeding circuits**.

*   **Neuroendocrine Regulation (Relaxin-3 Modulation of the
    Hypothalamus):** The **relaxin-3-expressing principal neurons** of
    the NI **project** to the **paraventricular nucleus** and the
    **arcuate nucleus** — they **modulate** the **hypothalamic-
    pituitary** axes (the **HPA axis**, the **HPT axis**, the **HPG
    axis**) and the **neuroendocrine** responses to **stress**,
    **feeding**, and **reproduction**. **This "relaxin-3 neuroendocrine
    regulation"** function is the **neural substrate** of the **NI's
    role in neuroendocrine control** — the **NI** is the **pontine
    relaxin-3** system that **modulates** the **hypothalamic-
    pituitary** axes.

*   **Autonomic Regulation (Relaxin-3 Modulation of the Brainstem):**
    The **relaxin-3-expressing principal neurons** of the NI **project**
    to the **brainstem autonomic centers** (the **dorsal raphe
    nucleus**, the **laterodorsal tegmental nucleus**, the **locus
    coeruleus**, the **parabrachial area**, the **solitary nucleus**,
    the **nucleus ambiguus**, the **ventral respiratory group**) — they
    **modulate** the **cardiovascular**, **respiratory**, and
    **gastrointestinal** functions via their **relaxin-3** and
    **GABAergic/glutamatergic** projections. **This "relaxin-3
    autonomic modulation"** function is the **neural substrate** of the
    **NI's role in autonomic regulation** — the **NI** is the
    **pontine relaxin-3** system that **adjusts** the **autonomic
    state** to the **behavioral state**.

*   **NOT a neural processor in the classical sense.** The NI is a
    **neuromodulatory nucleus** — it **receives** afferent inputs (from
    the **hypothalamus**, the **brainstem**, the **limbic system**, and
    the **cortex**) and **projects diffusely** to the **septum**, the
    **hippocampus**, the **medial prefrontal cortex**, the **amygdala**,
    the **hypothalamus**, and the **brainstem**. The **processing** of
    stress, arousal, feeding, and neuroendocrine regulation happens in a
    **distributed** manner across the **NI**, the **targets of the NI**
    (the **septum**, the **hippocampus**, the **medial prefrontal
    cortex**, the **amygdala**, the **hypothalamus**, the **brainstem**),
    and the **other neuromodulatory systems** (the **noradrenergic**,
    **cholinergic**, **dopaminergic**, and **serotonergic** systems)
    that **interact** with the **NI**.

**The unifying theme:** the nucleus incertus is the **pontine
relaxin-3 nucleus** — the **principal source of relaxin-3** in the
**brain**. It is **relaxin-3-expressing** (with **GABAergic** and
**glutamatergic** co-transmission), **SLEA-free**, and **NOT the
hypothalamic periventricular nucleus** — the **hypothalamic
periventricular nucleus** is the **other relaxin-3-expressing nucleus**
in the brain (the **hypothalamic relaxin-3 source** for the
**hypothalamus** itself). The **NI** is the **pontine relaxin-3**
nucleus — the **forebrain-projecting relaxin-3 system** that
**modulates** **stress**, **arousal**, **feeding**, and
**neuroendocrine** function.

Associated Disorders
--------------------
The nucleus incertus has **no named "nucleus incertus syndrome"** — its
clinical associations are **function-specific**:

*   **Stress-Related Disorders (PTSD, Anxiety, Depression) — NI
    Involvement:** **Post-traumatic stress disorder**, **generalized
    anxiety disorder**, and **major depressive disorder** have been
    **associated** with **dysregulation** of the **relaxin-3 system** —
    the **nucleus incertus** is the **principal source of relaxin-3** in
    the brain, and its **dysfunction** may **contribute** to the
    **stress-related symptoms** of these disorders. **Relaxin-3** is a
    **potential therapeutic target** for **stress-related disorders** —
    **relaxin-3 receptor (RXFP3) agonists** and **antagonists** are
    being **investigated** as **novel treatments** for **stress**,
    **anxiety**, and **depression**.

*   **Feeding and Eating Disorders — NI Involvement:** **Feeding and
    eating disorders** (e.g., **anorexia nervosa**, **binge-eating
    disorder**, **obesity**) have been **associated** with
    **dysregulation** of the **hypothalamic feeding circuits** — the
    **nucleus incertus** **modulates** the **hypothalamic feeding
    circuits** via its **relaxin-3** projections, and its **dysfunction**
    may **contribute** to the **feeding-related symptoms** of these
    disorders. **Relaxin-3** is a **potential therapeutic target** for
    **feeding and eating disorders** — **relaxin-3 receptor (RXFP3)
    agonists** and **antagonists** are being **investigated** as
    **novel treatments** for **obesity** and **eating disorders**.

*   **Neuroendocrine Disorders — NI Involvement:** **Neuroendocrine
    disorders** (e.g., **hypothalamic-pituitary-adrenal (HPA) axis
    dysregulation**, **hypothalamic-pituitary-thyroid (HPT) axis
    dysregulation**, **hypothalamic-pituitary-gonadal (HPG) axis
    dysregulation**) have been **associated** with **dysregulation** of
    the **NI** — the **nucleus incertus** **modulates** the
    **hypothalamic-pituitary** axes via its **relaxin-3** projections,
    and its **dysfunction** may **contribute** to the
    **neuroendocrine** symptoms of these disorders.

*   **Sleep and Arousal Disorders — NI Involvement:** **Sleep and
    arousal disorders** (e.g., **insomnia**, **REM sleep behavior
    disorder**, **narcolepsy**) have been **associated** with
    **dysregulation** of the **NI** — the **nucleus incertus**
    **modulates** the **septohippocampal system** and the **theta
    rhythm** via its **relaxin-3** projections, and its **dysfunction**
    may **contribute** to the **sleep and arousal** symptoms of these
    disorders.

*   **Alzheimer's Disease — NI Involvement:** **Alzheimer's disease** has
    been **associated** with **loss** of **nucleus incertus
    relaxin-3** neurons — the **NI's relaxin-3** projections to the
    **septum** and the **hippocampus** are **important** for **spatial
    memory** and **theta rhythm** — the **NI's degeneration** may
    **contribute** to the **cognitive decline** and the **sleep
    disturbances** of **Alzheimer's disease**.

*   **Pontine Stroke — NI Involvement:** A **pontine stroke** (e.g.,
    **basilar artery** perforator territory) involving the **NI** causes
    **stress-response dysregulation**, **arousal dysfunction**,
    **feeding dysfunction**, and **neuroendocrine dysregulation** —
    often accompanied by **other pontine signs** (**hemiparesis**,
    **facial palsy**, **abducens palsy**, **cerebellar ataxia**).

*   **No Named "NI Syndrome":** The nucleus incertus is a
    **neurochemically heterogeneous neuromodulatory nucleus** — it has
    **no named clinical syndrome** of its own. Its clinical relevance is
    **relaxin-3 stress, arousal, feeding, and neuroendocrine specific** —
    **PTSD**, **anxiety**, **depression**, **feeding and eating
    disorders**, **neuroendocrine disorders**, **sleep and arousal
    disorders**, **Alzheimer's disease**, and **pontine stroke** are all
    **NI-involved** conditions.

**What is NOT here:** The nucleus incertus is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **acoustic neuroma** (CN VIII nerve), **vestibular neuritis**
(vestibular nerve), **labyrinthitis** (inner ear), **auditory neuropathy
spectrum disorder** (cochlear nerve or hair cell), **Wallenberg
syndrome** (lateral medulla), **internuclear ophthalmoplegia** (MLF), or
**horizontal gaze palsy** (PPRF or abducens nucleus). Its clinical
relevance is **relaxin-3 stress, arousal, feeding, and neuroendocrine
specific**, via the **relaxin-3-expressing principal neurons** it
subserves. **No named NI syndrome exists.**

Lateralization Notes
--------------------
This is the **single** nucleus incertus module. The NI is **bilateral in
real anatomy** (left NI and right NI), but the tree wires it as a
**single module** — and the module carries **NO warning at the module
level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **nucleus_incertus** module (here) is a **single module** that
    represents the **bilateral NI** (the left NI and the right NI). The
    tree does **not** split them into left/right. Consumers must **not**
    assume a left/right split exists at the tree level — the module is a
    **single, bilateral representation**.

*   **Bilateral Projections (Structural Fact, NOT a Lateralization
    Warning):** The **NI** **projects bilaterally** to the **septum**,
    the **hippocampus**, the **medial prefrontal cortex**, the
    **amygdala**, the **hypothalamus**, and the **brainstem** — each NI
    projects to **both** left and right targets. **This bilateral
    projection** is a **structural fact** of the **relaxin-3
    neuromodulatory system** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **bilateral
    relaxin-3 modulation** of stress, arousal, feeding, and
    neuroendocrine function.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The NI is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the NI.

*   **NO Amygdala-Lateralization Warning of their own (the NI is
    RELAXIN-3 NEUROMODULATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The NI is a
    **relaxin-3 neuromodulatory nucleus** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**. The
    NI **projects to** the **amygdala** (modulating stress-related
    emotional processing) — but the **NI itself** is **not a
    fear-output structure**.

**A consumer that sees "nucleus_incertus" must understand that the
module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **bilateral projections** are
**structural facts**, not lateralizations. The NI is a **strict-single
module with NO warning at the module level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** NI as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/locus_coeruleus/``,
    ``.../tegmentum/laterodorsal_tegmental_nucleus/``,
    ``.../tegmentum/pedunculopontine_nucleus/``,
    ``.../tegmentum/pontine_micturition_center/``,
    ``.../tegmentum/tegmental_pontine_reticular_nucleus/``,
    ``.../pons/parabrachial_area/``,
    ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../pons/pontine_nuclei/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../diencephalon/hypothalamus/``, or
    any other container. The NI's relationships to the **locus
    coeruleus**, the **laterodorsal tegmental nucleus**, the
    **pedunculopontine nucleus**, the **pontine micturition center**,
    the **tegmental pontine reticular nucleus**, the **parabrachial
    area**, the **superior olivary complex**, the **cranial nerve
    nuclei**, the **PPRF**, the **parvocellular reticular nucleus**, the
    **pontine nuclei**, the **fourth ventricle**, the **midbrain
    tegmentum**, the **medullary tegmentum**, the **hypothalamic
    periventricular nucleus**, the **substantia nigra**, the **ventral
    tegmental area**, the **raphe nuclei**, the **whole tegmentum
    container**, the **whole pons**, and the **SLEA continuum** are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **relaxin-3-expressing
    principal neurons**, the **GABAergic neurons**, and the
    **glutamatergic neurons** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The **NI**
    is a **single module** that represents the **bilateral NI** — the
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **RELAXIN-3 NEUROMODULATORY NUCLEUS — NOT a motor or sensory
    relay.** The **NI** is a **neuromodulatory nucleus** —
    **projecting diffusely** to the septum, hippocampus, medial
    prefrontal cortex, amygdala, hypothalamus, and brainstem. Consumers
    must **not** conflate the NI with a motor or sensory relay.
*   **RELAXIN-3-EXPRESSING — NOT cholinergic, noradrenergic, dopaminergic,
    or serotonergic.** The **NI** is the **sole pontine relaxin-3
    nucleus** (with the **hypothalamic periventricular nucleus** as the
    other relaxin-3 source). The **cholinergic** nuclei (LDT and PPN),
    the **noradrenergic** nucleus (LC), the **dopaminergic** nuclei
    (substantia nigra and VTA), and the **serotonergic** nuclei (raphe
    nuclei) are **different structures**. Consumers must **not** conflate
    the NI with any of them.
*   **NOT the locus coeruleus — that is the NORADRENERGIC neuromodulatory
    nucleus.** Consumers must **not** conflate the NI with the LC.
*   **NOT the laterodorsal tegmental nucleus — that is the CHOLINERGIC
    neuromodulatory nucleus.** Consumers must **not** conflate the NI
    with the LDT.
*   **NOT the pedunculopontine nucleus — that is the CHOLINERGIC
    LOCOMOTION nucleus.** Consumers must **not** conflate the NI with
    the PPN.
*   **NOT the pontine micturition center or the tegmental pontine
    reticular nucleus — those are DIFFERENT autonomic and motor
    nuclei.** Consumers must **not** conflate the NI with either of
    them.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, the PPRF, or the parvocellular reticular
    nucleus — those are SEPARATE structural children of the pons.**
    Consumers must **not** conflate the NI with any of them.
*   **NOT the pontine nuclei — those are in the BASILAR pons.**
    Consumers must **not** conflate the NI with the pontine nuclei.
*   **NOT the whole tegmentum container — that is the PARENT.**
    Consumers must **not** conflate the NI with the whole tegmentum.
*   **NOT the whole pons — that is the GRANDPARENT.** Consumers must
    **not** conflate the NI with the whole pons.
*   **NOT the fourth ventricle — that is a CSF SPACE.** Consumers must
    **not** conflate the NI with the fourth ventricle.
*   **NOT the midbrain tegmentum or the medullary tegmentum — those are
    DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate the NI
    with the midbrain tegmentum or the medullary tegmentum.
*   **NOT the hypothalamic periventricular nucleus — that is the OTHER
    RELAXIN-3 source (the hypothalamic relaxin-3 nucleus).** Consumers
    must **not** conflate the NI with the hypothalamic periventricular
    nucleus.
*   **NOT the substantia nigra, the ventral tegmental area, or the raphe
    nuclei — those are DOPAMINERGIC or SEROTONERGIC nuclei.** Consumers
    must **not** conflate the NI with the dopaminergic or serotonergic
    nuclei.
*   **MULTIPLE NEUROCHEMICALLY DISTINCT NEURON POPULATIONS —
    relaxin-3-expressing principal neurons, GABAergic neurons, and
    glutamatergic neurons.** The **relaxin-3-expressing principal
    neurons** (the majority), the **GABAergic neurons**, and the
    **glutamatergic neurons** are **prose**, not structural children.
    Consumers must **not** treat the NI as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The NI is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the NI is RELAXIN-3 NEUROMODULATORY.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **NI** is a **relaxin-3 neuromodulatory nucleus** —
    it is **not** part of the fear circuit. **The NI projects to** the
    amygdala (modulating stress-related emotional processing) — but the
    **NI itself** is **not a fear-output structure**.
*   **No ``AREA_PATHS`` hop.** The NI is a local leaf under the tegmentum
    container, not a cross-listed leaf.
*   **No nested cross-listing.** The NI has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum import nucleus_incertus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.tegmentum.nucleus_incertus"
    )

**Do not** assume the NI is a **container**. It is a **leaf** — the
**relaxin-3-expressing principal neurons**, the **GABAergic neurons**,
and the **glutamatergic neurons** are **prose**, not structural
children.

**Do not** assume the NI is **bilateralized at the tree level**. The NI
is **bilateral in real anatomy**, but the tree wires it as a **single
module** — there is **no left/right split at the module level**.

**Do not** assume the NI is the **locus coeruleus**. The **locus
coeruleus** is the **noradrenergic** nucleus. The **NI** is the
**relaxin-3** nucleus. They are **different structures** — different
neurotransmitters and different functional systems.

**Do not** assume the NI is the **laterodorsal tegmental nucleus** or
the **pedunculopontine nucleus**. The **LDT** and the **PPN** are
**cholinergic** nuclei — the **NI** is the **relaxin-3** nucleus. They
are **different structures** — different neurotransmitters and
different functional systems.

**Do not** assume the NI is the **pontine micturition center** or the
**tegmental pontine reticular nucleus**. The **pontine micturition
center** is the **micturition control center** — the **tegmental
pontine reticular nucleus** is the **motor relay**. The **NI** is the
**relaxin-3** nucleus.

**Do not** assume the NI is the **hypothalamic periventricular
nucleus**. The **hypothalamic periventricular nucleus** is the **other
relaxin-3-expressing nucleus** in the brain — the **hypothalamic
relaxin-3 source** for the **hypothalamus** itself. The **NI** is the
**pontine relaxin-3 nucleus** — the **forebrain-projecting relaxin-3
system**.

**Do not** assume the NI is the **substantia nigra**, the **ventral
tegmental area**, or the **raphe nuclei**. Those are **different
structures** — the **substantia nigra** and the **ventral tegmental
area** are **dopaminergic** (midbrain); the **raphe nuclei** are
**serotonergic** (midbrain/pons). The **NI** is the **relaxin-3**
nucleus (pons).

**Do not** assume the NI is the **parabrachial area**, the **superior
olivary complex**, the **cranial nerve nuclei**, the **PPRF**, or the
**parvocellular reticular nucleus**. Those are **separate structural
children of the pons** — even though they are anatomically located in
the pontine tegmentum.

**Do not** assume the NI is the **pontine nuclei**. The **pontine
nuclei** are in the **basilar pons** — the NI is in the **dorsal
pontine tegmentum**.

**Do not** assume the NI is the **whole tegmentum** or the **whole
pons**. The **tegmentum** is the **parent**; the **pons** is the
**grandparent**.

**Do not** assume the NI is the **fourth ventricle**. The **fourth
ventricle** is a **CSF space**; the NI is **neural tissue** just
ventral to the fourth ventricle.

**Do not** assume the NI is the **midbrain tegmentum** or the **medullary
tegmentum**. Those are **different brainstem levels**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the NI. **The NI is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the NI's (empty) children (recommended consumer pattern)::

    NUCLEUS_INCERTUS_CHILDREN = ()
    # The NI is a leaf. The relaxin-3-expressing principal neurons, the
    # GABAergic neurons, and the glutamatergic neurons are prose, not
    # modules.

Reaching the locus coeruleus (recommended consumer pattern — the
noradrenergic sibling)::

    # The locus coeruleus is the NORADRENERGIC sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The LC is noradrenergic; the NI is relaxin-3-expressing. They are
    # ANATOMICALLY ADJACENT but FUNCTIONALLY DISTINCT.

Reaching the laterodorsal tegmental nucleus (recommended consumer
pattern — the cholinergic sibling)::

    # The laterodorsal tegmental nucleus is the CHOLINERGIC sibling under
    # the tegmentum container:
    #
    #   .../pons/tegmentum/laterodorsal_tegmental_nucleus/
    #
    # The LDT is cholinergic; the NI is relaxin-3-expressing. They are
    # DIFFERENT STRUCTURES with DIFFERENT neurotransmitters and
    # functional systems.

Reaching the pedunculopontine nucleus (recommended consumer pattern — the
cholinergic locomotion sibling)::

    # The pedunculopontine nucleus is the CHOLINERGIC LOCOMOTION sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pedunculopontine_nucleus/
    #
    # The PPN is cholinergic; the NI is relaxin-3-expressing. They are
    # DIFFERENT STRUCTURES.

Reaching the pontine micturition center (recommended consumer pattern —
the micturition sibling)::

    # The pontine micturition center is the MICTURITION CONTROL sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pontine_micturition_center/
    #
    # The pontine micturition center coordinates the micturition reflex;
    # the NI is the relaxin-3 neuromodulatory nucleus.

Reaching the tegmental pontine reticular nucleus (recommended consumer
pattern — the motor relay sibling)::

    # The tegmental pontine reticular nucleus is the MOTOR RELAY sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/tegmental_pontine_reticular_nucleus/
    #
    # The tegmental pontine reticular nucleus is involved in locomotion,
    # posture, and motor pattern generation; the NI is the relaxin-3
    # neuromodulatory nucleus.

Reaching the parabrachial area (recommended consumer pattern — a
SEPARATE pons child)::

    # The parabrachial area is a SEPARATE STRUCTURAL CHILD of the pons:
    #
    #   .../pons/parabrachial_area/
    #
    # The parabrachial area is the visceral-sensory and respiratory-relay
    # complex; the NI is a relaxin-3 neuromodulatory nucleus.

Reaching the whole tegmentum container (recommended consumer pattern —
the PARENT)::

    # The tegmentum container is the DORSAL PONTINE GREY-MATTER REGION
    # that CONTAINS the NI as one of its six structural children:
    #
    #   .../pons/tegmentum/
    #
    # The NI is a CHILD of the tegmentum container.

Reaching the whole pons (recommended consumer pattern — the
GRANDPARENT)::

    # The pons is the WHOLE METENCEPHALIC BRAINSTEM SEGMENT that CONTAINS
    # the tegmentum container:
    #
    #   .../pons/
    #
    # The NI is a GRANDCHILD of the pons.

Bilateral iteration (recommended consumer pattern)::

    # The NI is a SINGLE module (not bilateralized at the tree level).
    # The module represents the BILATERAL NI.
    ni_path = (
        "hindbrain.metencephalon.pons.tegmentum.nucleus_incertus"
    )
    # resolve ni_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The NI's neuron populations are prose, not modules:
    #   relaxin-3-expressing principal neurons -> synthesize and release
    #       relaxin-3; co-express relaxin-3 with GABA or glutamate;
    #       project to the medial septum, diagonal band of Broca,
    #       hippocampus, medial prefrontal cortex, amygdala, hypothalamus
    #       (paraventricular nucleus, lateral hypothalamic area, arcuate
    #       nucleus, dorsomedial hypothalamic nucleus), and brainstem
    #       (dorsal raphe nucleus, laterodorsal tegmental nucleus, locus
    #       coeruleus, parabrachial area, solitary nucleus, nucleus
    #       ambiguus, ventral respiratory group); relaxin-3 stress,
    #       arousal, feeding, and neuroendocrine modulation
    #   GABAergic neurons -> release GABA at their axon terminals;
    #       contribute to the inhibitory modulation of the NI's targets
    #   glutamatergic neurons -> release glutamate at their axon
    #       terminals; contribute to the excitatory modulation of the
    #       NI's targets
    #
    # Do not attempt to resolve these as sub-paths of the NI — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical NI anatomy:** Ryan, P.J., Ma, S., Olucha-Bordonau, F.E.,
    Gundlach, A.L. (2011). "Nucleus incertus — an emerging role in the
    behavioural actions of relaxin-3." *British Journal of
    Pharmacology* 162:1115–1126. (Nucleus incertus — relaxin-3
    neuromodulatory nucleus; canonical review.)
*   **Relaxin-3 — discovery and distribution:** Bathgate, R.A.D.,
    Samuel, C.S., Burazin, T.C.D., et al. (2002). "Human relaxin gene 3
    (H3) and the equivalent mouse relaxin (M3) gene: novel
    relaxin-like peptides and their receptors." *Journal of Biological
    Chemistry* 277:1148–1157. (Relaxin-3 — discovery; distribution in
    the nucleus incertus and the hypothalamic periventricular nucleus.)
*   **Nucleus incertus — anatomy and connectivity:** Ma, S., Bonaventure,
    P., Ferraro, T., et al. (2007). "Modulation of the
    corticotropin-releasing factor system by relaxin-3." *Neuroscience*
    144:845–857. (Nucleus incertus — anatomy and connectivity;
    relaxin-3 and CRF interactions.)
*   **Nucleus incertus — stress and arousal:** Tanaka, M., Iijima, N.,
    Miyamoto, Y., et al. (2005). "Neurons expressing relaxin 3/INSL 7 in
    the nucleus incertus respond to stress." *European Journal of
    Neuroscience* 22:1659–1670. (Nucleus incertus — relaxin-3 neurons
    respond to stress.)
*   **Nucleus incertus — feeding:** Lenglos, C., Calvez, J., Timofeeva,
    E. (2013). "Relaxin-3/I5 neurons in the nucleus incertus are
    activated by food restriction and cold exposure in rats."
    *Neuroscience* 250:200–210. (Nucleus incertus — feeding and energy
    balance.)
*   **Nucleus incertus — theta rhythm and arousal:** Olucha-Bordonau,
    F.E., Otero-García, M., Sánchez-Pérez, A.M., et al. (2012).
    "Distribution and targets of the relaxin-3 innervation of the
    septal area in the rat." *Journal of Comparative Neurology*
    520:2233–2268. (Nucleus incertus — relaxin-3 innervation of the
    septal area; theta rhythm and arousal.)
*   **Nucleus incertus — neuroendocrine regulation:** Watanabe, Y.,
    Miyamoto, Y., Matsuda, T., Tanaka, M. (2011). "Relaxin-3/INSL7
    regulates the stress response via the
    hypothalamic-pituitary-adrenal axis." *Molecular and Cellular
    Endocrinology* 331:183–190. (Nucleus incertus — relaxin-3 and the
    HPA axis.)
*   **Relaxin-3 receptor (RXFP3) — therapeutic target:** Smith, C.M.,
    Walker, A.W., Hosken, I.T., et al. (2012). "Relaxin-3/RXFP3
    systems modulate feeding and stress-driven anxiety-like behavior in
    mice." *Neuropsychopharmacology* 37:2108–2120. (Relaxin-3/RXFP3
    system — potential therapeutic target for feeding and stress-related
    disorders.)
*   **Nucleus incertus — Alzheimer's disease:** Ryan, P.J., Büchler, E.,
    De Souza, R.L., et al. (2013). "Nucleus incertus — an emerging role
    in the behavioural actions of relaxin-3." *British Journal of
    Pharmacology* 162:1115–1126. (Nucleus incertus — relaxin-3
    projections to the septum and hippocampus; potential involvement in
    Alzheimer's disease.)
*   **Pontine stroke — NI involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — pontine tegmentum involvement,
    including the NI.)
*   **Locus coeruleus (contrast — the NORADRENERGIC neuromodulatory
    sibling):** Aston-Jones, G., Cohen, J.D. (2005). "An integrative
    theory of locus coeruleus-norepinephrine function: adaptive gain
    and optimal performance." *Annual Review of Neuroscience*
    28:403–450. (Locus coeruleus — noradrenergic neuromodulatory
    nucleus; sibling of the NI.)
*   **Laterodorsal tegmental nucleus (contrast — the CHOLINERGIC
    neuromodulatory sibling):** Mesulam, M.M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the rat:
    an overview based on an alternative nomenclature (Ch1-Ch6)."
    *Neuroscience* 10:1185–1201. (LDT — cholinergic neuromodulatory
    nucleus; sibling of the NI.)
*   **Pedunculopontine nucleus (contrast — the CHOLINERGIC LOCOMOTION
    sibling):** Garcia-Rill, E. (1991). "The pedunculopontine nucleus."
    *Progress in Neurobiology* 36:363–389. (PPN — cholinergic
    locomotion and REM-sleep nucleus; sibling of the NI.)
*   **Pontine micturition center (contrast — the MICTURITION sibling):**
    Barrington, F.J.F. (1925). "The effect of lesions of the hind- and
    mid-brain on micturition in the cat." *Quarterly Journal of
    Experimental Physiology* 15:81–102. (Pontine micturition center —
    micturition control; sibling of the NI.)
*   **Tegmental pontine reticular nucleus (contrast — the MOTOR RELAY
    sibling):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Tegmental pontine reticular
    nucleus — motor relay; sibling of the NI.)
*   **Hypothalamic periventricular nucleus (contrast — the OTHER
    relaxin-3 source):** Bathgate, R.A.D., Samuel, C.S., Burazin,
    T.C.D., et al. (2002). "Human relaxin gene 3 (H3) and the equivalent
    mouse relaxin (M3) gene." *Journal of Biological Chemistry*
    277:1148–1157. (Hypothalamic periventricular nucleus — the other
    relaxin-3-expressing nucleus; distinct from the NI.)
*   **Substantia nigra and ventral tegmental area (contrast — the
    DOPAMINERGIC nuclei):** Björklund, A., Dunnett, S.B. (2007).
    "Dopamine neuron systems in the brain: an update." *Trends in
    Neurosciences* 30:194–202. (Substantia nigra and VTA —
    dopaminergic nuclei; distinct from the NI.)
*   **Raphe nuclei (contrast — the SEROTONERGIC nuclei):** Hornung,
    J.P. (2003). "The human raphe nuclei and the serotonergic system."
    *Journal of Chemical Neuroanatomy* 26:331–343. (Raphe nuclei —
    serotonergic nuclei; distinct from the NI.)
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
    pons; distinct from the NI.)
*   **Fourth ventricle (contrast — a CSF space):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Fourth ventricle — CSF space dorsal to the pons; distinct from the
    NI.)
*   **Midbrain tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Midbrain tegmentum — dorsal midbrain; distinct
    from the pontine tegmentum.)
*   **Medullary tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary tegmentum — dorsal medulla; distinct
    from the pontine tegmentum.)
*   **SLEA (contrast — the NI is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the NI.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the NI.)
*   NeuroNames — Nucleus incertus; FMA — Nucleus incertus.
"""
