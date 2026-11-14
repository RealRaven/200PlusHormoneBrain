"""
infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum.locus_coeruleus
================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── tegmentum
                └── locus_coeruleus   <-- THIS MODULE

**Primary synonym:** Locus coeruleus; LC; nucleus coeruleus; nucleus
pigmentosus pontis; "the pontine noradrenergic nucleus"; "the brain's
principal noradrenergic nucleus"; "the blue spot" (from the neuromelanin
pigmentation that gives the nucleus its blue appearance in fresh tissue).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — an **anatomically delimited
noradrenergic nucleus** in the **dorsal pontine tegmentum**, near the
**lateral wall of the fourth ventricle** in the **rostral pons**. It is
the **principal source of norepinephrine** in the brain — the **sole
noradrenergic source** for the **cerebral cortex**, the **hippocampus**,
the **amygdala**, the **thalamus**, the **hypothalamus**, the
**cerebellum**, the **brainstem**, and the **spinal cord**.
**Part of:** The **tegmentum** container — specifically, the
**neuromodulatory (noradrenergic)** component. The **tegmentum** is the
**dorsal pontine grey-matter region** — the **tree-wired container** for
the six neuromodulatory and autonomic nuclei of the dorsal pons.
**Structural parent:** ``.../tegmentum/`` → **direct child** of the
tegmentum container.
**Structural children:** **None.** This is a **leaf** module. The
**noradrenergic principal neurons** (the **vast majority** of the
nucleus) and the **neuropeptide-coexpressing neurons** (galanin,
neuropeptide Y, and other peptide co-transmitters) are documented as
**prose**, not as structural children — they are the **functionally
distinct neuron populations** within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
locus coeruleus is a LEAF, not a container.** It has **no structural
children**. The **noradrenergic principal neurons** and the
**neuropeptide-coexpressing neurons** are **prose** populations, not
structural children. Consumers must **not** treat the locus coeruleus as
a container, and must **not** assume the neuron populations exist as
sub-modules.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the locus coeruleus is a SINGLE module at the tree
level, even though the LC is BILATERAL in real anatomy.** Unlike the
**cranial_nerve_nuclei** module (which has explicit ``left`` and
``right`` structural children) or the **superior_olivary_complex**
module (which has ``left`` and ``right`` sub-containers), the
**locus_coeruleus** module (here) is a **single module** that represents
the **bilateral LC** (the left LC and the right LC). The tree does
**not** split them into left/right. Consumers must **not** assume a
left/right split exists at the tree level — the module is a **single,
bilateral representation**. Any lateralization is documented **here, in
the Lateralization Notes**, not imported from elsewhere.
**Boundary status (NORADRENERGIC NEUROMODULATORY NUCLEUS — NOT a motor
or sensory relay):** **Boundary case — the locus coeruleus is a
NORADRENERGIC NEUROMODULATORY nucleus, NOT a motor or sensory relay.**
Unlike the **cranial nerve motor nuclei** (branchial or somatic motor
relays) or the **sensory nuclei** (e.g., the cochlear nuclei, the
trigeminal nuclei), the **locus coeruleus** (here) is a
**neuromodulatory nucleus** — its **noradrenergic neurons** **project
diffusely** to the **entire forebrain**, the **brainstem**, and the
**spinal cord** to **modulate** the **excitability** of their targets —
they **do not** directly **relay** motor commands or **transmit**
sensory information. **This distinction is functionally load-bearing**
— the locus coeruleus is a **state-setting** nucleus, not a
**throughput** nucleus — it **adjusts the gain** of the entire
nervous system. Consumers must **not** conflate the locus coeruleus
with a motor or sensory relay.
**Boundary status (NORADRENERGIC — NOT a cholinergic, dopaminergic,
serotonergic, or other monoaminergic nucleus):** **Boundary case — the
locus coeruleus is NORADRENERGIC, NOT a cholinergic, dopaminergic,
serotonergic, or other monoaminergic nucleus.** The **locus coeruleus**
neurons are **noradrenergic** — they synthesize **norepinephrine**
(via the **tyrosine hydroxylase** → **DOPA** → **dopamine** →
**dopamine β-hydroxylase** → **norepinephrine** pathway) and release it
as their **primary neurotransmitter**. The **noradrenergic** identity of
the locus coeruleus is its **defining neurochemical signature** — the
other pontine tegmentum nuclei use **different neurotransmitters**
(acetylcholine for the LDT and PPN; relaxin-3 for the nucleus incertus;
the pontine micturition center and the tegmental pontine reticular
nucleus are **glutamatergic/GABAergic**). **This distinction is
neurochemically load-bearing** — the locus coeruleus is the **sole
noradrenergic source** for the **forebrain** and the **sole
noradrenergic source** for the **cortex** — and its **noradrenergic
identity** is the **basis** of its **arousal, attention, stress, pain
modulation, and memory consolidation** functions. Consumers must **not**
conflate the locus coeruleus with the **cholinergic** nuclei (the LDT
and the PPN) or with the **dopaminergic** nuclei (the **substantia
nigra** and the **ventral tegmental area** in the midbrain) or with the
**serotonergic** nuclei (the **dorsal raphe nucleus** and the
**median raphe nucleus** in the midbrain/pons) or with the
**relaxin-3** nucleus (the nucleus incertus).
**Boundary status (NOT the laterodorsal tegmental nucleus — that is the
CHOLINERGIC neuromodulatory nucleus):** **Boundary case — the locus
coeruleus is NOT the laterodorsal tegmental nucleus (LDT).** The
**laterodorsal tegmental nucleus**
(``.../tegmentum/laterodorsal_tegmental_nucleus/``) is the **cholinergic**
nucleus — the **principal pontine cholinergic source** for the
**thalamus** and a **major cholinergic source** for the **basal
forebrain** — it is involved in **REM sleep**, **arousal**, and
**motivation**. The **locus coeruleus** (here) is the **noradrenergic**
nucleus — the **sole noradrenergic source** for the **forebrain** — it
is involved in **arousal**, **attention**, **stress**, **pain
modulation**, and **memory consolidation**. They are **DIFFERENT
STRUCTURES** — different neurotransmitters (noradrenaline vs.
acetylcholine), different functional systems (noradrenergic
arousal/attention/stress vs. cholinergic REM-sleep/arousal/motivation),
different projection targets (diffuse noradrenergic vs. thalamic and
basal-forebrain cholinergic). They are **anatomically adjacent** (both
are in the **dorsal pontine tegmentum**) — this proximity is a
**classic source of confusion** — consumers must **not** conflate the
locus coeruleus with the laterodorsal tegmental nucleus.
**Boundary status (NOT the pedunculopontine nucleus — that is the
CHOLINERGIC LOCOMOTION nucleus):** **Boundary case — the locus
coeruleus is NOT the pedunculopontine nucleus (PPN).** The
**pedunculopontine nucleus**
(``.../tegmentum/pedunculopontine_nucleus/``) is the **cholinergic**
(with glutamatergic and GABAergic components) nucleus — the
**mesencephalic locomotor region** — it is involved in **locomotion**,
**REM sleep**, **arousal**, and **reward**. The **locus coeruleus**
(here) is the **noradrenergic** nucleus. They are **DIFFERENT
STRUCTURES** — different neurotransmitters (noradrenaline vs.
acetylcholine), different functional systems (noradrenergic
arousal/attention/stress vs. cholinergic locomotion/REM-sleep/
arousal/reward), different anatomical locations (LC is **dorsomedial**
at the **lateral fourth-ventricle wall**; PPN is **ventrolateral** at
the **pontomesencephalic junction**). Consumers must **not** conflate
the locus coeruleus with the pedunculopontine nucleus.
**Boundary status (NOT the nucleus incertus — that is the RELAXIN-3
nucleus):** **Boundary case — the locus coeruleus is NOT the nucleus
incertus.** The **nucleus incertus**
(``.../tegmentum/nucleus_incertus/``) is the **relaxin-3-expressing**
nucleus — it is involved in **stress**, **arousal**, **feeding**, and
**neuroendocrine regulation**. The **locus coeruleus** (here) is the
**noradrenergic** nucleus. They are **DIFFERENT STRUCTURES** — different
neurotransmitters (noradrenaline vs. relaxin-3), different functional
systems (noradrenergic arousal/attention/stress/pain/memory vs.
relaxin-3 stress/arousal/feeding/neuroendocrine), different projection
targets (diffuse noradrenergic vs. septum/hippocampus/medial prefrontal
cortex/amygdala/hypothalamus). Consumers must **not** conflate the locus
coeruleus with the nucleus incertus.
**Boundary status (NOT the pontine micturition center — that is the
MICTURITION nucleus):** **Boundary case — the locus coeruleus is NOT the
pontine micturition center (Barrington's nucleus).** The **pontine
micturition center**
(``.../tegmentum/pontine_micturition_center/``) is the **micturition
control center** — it **coordinates** the **micturition reflex**
(bladder contraction and sphincter relaxation). The **locus coeruleus**
(here) is the **noradrenergic** nucleus. They are **DIFFERENT
STRUCTURES** — different functional systems (noradrenergic
arousal/attention/stress/pain/memory vs. micturition), different
projection targets (diffuse noradrenergic vs. sacral spinal cord).
Consumers must **not** conflate the locus coeruleus with the pontine
micturition center.
**Boundary status (NOT the tegmental pontine reticular nucleus — that is
the MOTOR RELAY nucleus):** **Boundary case — the locus coeruleus is
NOT the tegmental pontine reticular nucleus.** The **tegmental pontine
reticular nucleus**
(``.../tegmentum/tegmental_pontine_reticular_nucleus/``) is a **motor
relay** — it **projects** to the **spinal cord** (via the
**reticulospinal tract**) and to the **cerebellum** (via the
**pontocerebellar fibers**) — it is involved in **locomotion**,
**posture**, and **motor pattern generation**. The **locus coeruleus**
(here) is the **noradrenergic** nucleus. They are **DIFFERENT
STRUCTURES** — different functional systems (noradrenergic
arousal/attention/stress/pain/memory vs. motor relay), different
projection targets (diffuse noradrenergic vs. spinal cord/cerebellum).
Consumers must **not** conflate the locus coeruleus with the tegmental
pontine reticular nucleus.
**Boundary status (NOT the parabrachial area — that is a SEPARATE
structural child of the pons):** **Boundary case — the locus coeruleus
is NOT the parabrachial area.** The **parabrachial area**
(``.../pons/parabrachial_area/``) is the **visceral-sensory and
respiratory-relay complex** — it is a **separate structural child of the
pons**, **not** a structural child of the pontine tegmentum, **even
though** it is **anatomically located** in the **pontine tegmentum**.
The **locus coeruleus** (here) is a **noradrenergic neuromodulatory
nucleus** — a **structural child of the pontine tegmentum container**.
Consumers must **not** conflate the locus coeruleus with the parabrachial
area.
**Boundary status (NOT the superior olivary complex, the cranial nerve
nuclei, the PPRF, or the parvocellular reticular nucleus — those are
SEPARATE structural children of the pons):** **Boundary case — the
locus coeruleus is NOT the superior olivary complex, the cranial nerve
nuclei, the PPRF, or the parvocellular reticular nucleus.** Those are
**separate structural children of the pons** — the **superior olivary
complex** (binaural sound-localization relay), the **cranial nerve
nuclei** (CN V, VI, VII, VIII nuclei), the **PPRF** (horizontal
saccadic burst generator), and the **parvocellular reticular nucleus**
(orofacial premotor and autonomic relay). The **locus coeruleus** (here)
is a **noradrenergic neuromodulatory nucleus** — a **structural child of
the pontine tegmentum container**. Consumers must **not** conflate the
locus coeruleus with any of them.
**Boundary status (NOT the pontine nuclei — those are in the BASILAR
pons):** **Boundary case — the locus coeruleus is NOT the pontine
nuclei.** The **pontine nuclei** (``.../pons/pontine_nuclei/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons** — the
**ventral** portion of the pons. The **locus coeruleus** (here) is a
**noradrenergic neuromodulatory nucleus** in the **dorsal pontine
tegmentum**. They are **DIFFERENT PONTS SUB-DIVISIONS** — consumers must
**not** conflate the locus coeruleus with the pontine nuclei.
**Boundary status (NOT the whole tegmentum container — that is the
PARENT):** **Boundary case — the locus coeruleus is NOT the whole
tegmentum container; the tegmentum container is the PARENT.** The
**tegmentum** container (``.../pons/tegmentum/``) is the **dorsal
pontine grey-matter region** — the **tree-wired container** for the
**six neuromodulatory and autonomic nuclei** (locus coeruleus,
laterodorsal tegmental nucleus, nucleus incertus, pedunculopontine
nucleus, pontine micturition center, tegmental pontine reticular
nucleus). The **locus coeruleus** (here) is **one of the six structural
children** of the tegmentum container. Consumers must **not** conflate
the locus coeruleus with the **whole tegmentum**.
**Boundary status (NOT the whole pons — the pons is the GRANDPARENT):**
**Boundary case — the locus coeruleus is NOT the whole pons; the pons
is the GRANDPARENT.** The **pons** (``.../pons/``) is the **whole
metencephalic brainstem segment** — it contains the **basilar pons**,
the **pontine tegmentum**, the **parabrachial area**, the **superior
olivary complex**, the **cranial nerve nuclei**, the **PPRF**, the
**parvocellular reticular nucleus**, the **pontine nuclei**, and the
**six neuromodulatory and autonomic nuclei** of the tegmentum container.
The **locus coeruleus** (here) is **one of the six neuromodulatory and
autonomic nuclei** only. Consumers must **not** conflate the locus
coeruleus with the **whole pons**.
**Boundary status (NOT the fourth ventricle — that is a CSF SPACE):**
**Boundary case — the locus coeruleus is NOT the fourth ventricle.** The
**fourth ventricle** (``.../metencephalon/fourth_ventricle/``) is the
**CSF-filled space** **dorsal to** the pons and **ventral to** the
cerebellum. The **locus coeruleus** (here) is a **grey-matter nucleus**
that sits **at the lateral wall of** the fourth ventricle (in the
**pontine tegmentum**). They are **DIFFERENT STRUCTURES** — the
**fourth ventricle** is a **fluid space**; the **locus coeruleus** is
**neural tissue**. Consumers must **not** conflate the locus coeruleus
with the fourth ventricle.
**Boundary status (NOT the midbrain tegmentum or the medullary
tegmentum — those are DIFFERENT BRAINSTEM LEVELS):** **Boundary case —
the locus coeruleus is NOT the midbrain tegmentum or the medullary
tegmentum.** The **midbrain tegmentum** (``.../midbrain/tegmentum/``)
is the **dorsal portion of the midbrain** — it contains the **substantia
nigra** and the **ventral tegmental area** (the **dopaminergic**
nuclei), the **red nucleus**, the **periaqueductal gray**, the
**oculomotor nucleus**, the **trochlear nucleus**, the **mesencephalic
trigeminal nucleus**, the **riMLF**, the **cMRF**, and other **midbrain
structures**. The **medullary tegmentum** is the **dorsal portion of the
medulla oblongata** — it contains the **solitary nucleus**, the
**dorsal motor nucleus of the vagus**, the **hypoglossal nucleus**, the
**nucleus ambiguus**, the **inferior olivary nucleus**, the
**gigantocellular reticular nucleus**, the **paramedian reticular
nucleus**, and other **medullary structures**. The **locus coeruleus**
(here) is a **specific nucleus** in the **dorsal portion of the pons**.
They are **DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate
the locus coeruleus with the midbrain tegmentum or the medullary
tegmentum.
**Boundary status (NORADRENERGIC IDENTITY — NOT the dopaminergic
substantia nigra/ventral tegmental area or the serotonergic raphe
nuclei):** **Boundary case — the locus coeruleus is NORADRENERGIC, NOT
the dopaminergic substantia nigra/ventral tegmental area or the
serotonergic raphe nuclei.** The **substantia nigra** (pars compacta)
and the **ventral tegmental area** (midbrain) are the **dopaminergic**
nuclei — the **principal sources of dopamine** in the brain. The
**dorsal raphe nucleus** and the **median raphe nucleus**
(midbrain/pons) are the **serotonergic** nuclei — the **principal
sources of serotonin** in the brain. The **locus coeruleus** (here) is
the **noradrenergic** nucleus — the **principal source of
norepinephrine** in the brain. **These three monoaminergic systems are
distinct** — different neurotransmitters (noradrenaline vs. dopamine vs.
serotonin), different anatomical locations (pons vs. midbrain), different
functional systems (noradrenergic arousal/attention/stress/pain/memory
vs. dopaminergic reward/motor control/learning vs. serotonergic
mood/sleep/appetite/pain). **This distinction is neurochemically
load-bearing** — consumers must **not** conflate the locus coeruleus
with the **dopaminergic** or **serotonergic** nuclei.
**Boundary status (MULTIPLE NEUROCHEMICALLY DISTINCT NEURON
POPULATIONS — noradrenergic principal neurons and neuropeptide-
coexpressing neurons):** **Boundary case — the locus coeruleus is NOT a
single uniform neuron population; it contains MULTIPLE neurochemically
distinct populations.** The **noradrenergic principal neurons** — the
**vast majority** of the LC neurons — they are the **noradrenergic
output** of the LC, and they are the **principal source of
norepinephrine** in the brain. The **neuropeptide-coexpressing
neurons** — the **minority** population of LC neurons that **co-express
norepinephrine** with **neuropeptides** (galanin, neuropeptide Y,
somatostatin, and other peptides) — they **co-release** the
neuropeptide with norepinephrine and **modulate** the **norepinephrine
signal** (different peptides have different effects on different
targets). **These populations are prose, not structural children.**
Consumers must **not** treat the locus coeruleus as a single uniform
population — it is a **neurochemically heterogeneous nucleus** with
**distinct** sub-circuits, even though the **vast majority** of its
neurons are **noradrenergic**.
**Boundary status (SLEA-FREE — the locus coeruleus is NOT an
extended-amygdala component):** **Boundary case — the locus coeruleus is
SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus**
(the **only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired elsewhere). The
**locus coeruleus** is a **noradrenergic neuromodulatory nucleus** — it
is **NOT** an extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into the locus
coeruleus — it is **SLEA-free**.

Overview
--------
The locus coeruleus is the **pontine noradrenergic nucleus** of the
**pontine tegmentum** — an **anatomically delimited noradrenergic**
grey-matter nucleus in the **dorsal pontine tegmentum**, at the **lateral
wall of the fourth ventricle** in the **rostral pons**. It is a **leaf**
module under the tegmentum container, and it is the **sole noradrenergic
source** for the **forebrain** — the **sole noradrenergic source** for
the **cortex** — the **neural substrate** of **noradrenergic arousal**,
**attention**, **stress**, **pain modulation**, and **memory
consolidation**.

**The locus coeruleus is a LEAF, not a container.** It has **no
structural children**. The **noradrenergic principal neurons** and the
**neuropeptide-coexpressing neurons** are **prose populations**, not
structural children.

**The locus coeruleus is a SINGLE module at the tree level.** The tree
does **not** split the LC into left/right — the module is a **single,
bilateral representation**.

**The locus coeruleus is a NORADRENERGIC NEUROMODULATORY NUCLEUS, NOT a
motor or sensory relay.** It **projects diffusely** to the **entire
forebrain**, the **brainstem**, and the **spinal cord** to **modulate**
the **excitability** of its targets — it does **not** directly **relay**
motor commands or **transmit** sensory information. **It adjusts the
gain of the entire nervous system** — the **"blue spot"** that colors
the brain's arousal, attention, and stress responses.

**The locus coeruleus is NORADRENERGIC, NOT cholinergic, dopaminergic, or
serotonergic.** It is the **sole noradrenergic source** for the
**forebrain** and the **sole noradrenergic source** for the **cortex**.
The **cholinergic** nuclei (the LDT and the PPN), the **dopaminergic**
nuclei (the substantia nigra and the ventral tegmental area), and the
**serotonergic** nuclei (the raphe nuclei) are **different structures**
— different neurotransmitters and different functional systems.

**The locus coeruleus is NOT the laterodorsal tegmental nucleus, the
pedunculopontine nucleus, the nucleus incertus, the pontine micturition
center, or the tegmental pontine reticular nucleus.** Those are the
**other five** neuromodulatory and autonomic nuclei of the **pontine
tegmentum container** — different neurotransmitters, different
functional systems, different projection targets.

**The locus coeruleus is SLEA-FREE.** It is **not** an extended-amygdala
component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The locus coeruleus contains **multiple neurochemically distinct neuron
populations** — documented as **prose**, not as structural children:

*   **Noradrenergic principal neurons** — the **vast majority** of the
    LC neurons — they **synthesize** and **release norepinephrine** (via
    the **tyrosine hydroxylase** → **DOPA** → **dopamine** → **dopamine
    β-hydroxylase** → **norepinephrine** pathway). They **project
    diffusely** to the **entire forebrain** (the **cortex**, the
    **hippocampus**, the **amygdala**, the **thalamus**, the
    **hypothalamus**, the **septum**, the **basal forebrain**), the
    **brainstem** (the **parabrachial area**, the **solitary nucleus**,
    the **vagal nuclei**, the **raphe nuclei**, the **cerebellum**),
    and the **spinal cord** (the **dorsal horn** — for **pain
    modulation** — and the **ventral horn** — for **motor
    modulation**). They are the **principal output** of the LC and the
    **sole noradrenergic source** for the **forebrain** and the
    **cortex**. **Noradrenergic arousal, attention, stress, pain
    modulation, and memory consolidation are the functional systems**
    subserved primarily by the noradrenergic principal neurons.

*   **Neuropeptide-coexpressing neurons** — the **minority** population
    of LC neurons that **co-express norepinephrine** with
    **neuropeptides** — including **galanin**, **neuropeptide Y**,
    **somatostatin**, and other peptides. They **co-release** the
    **neuropeptide** with **norepinephrine** at their **axon
    terminals** — the **neuropeptide** **modulates** the
    **norepinephrine signal** at the **target** (different peptides have
    different effects on different targets — e.g., **galanin** may
    **inhibit** some targets while norepinephrine **excites** them).
    They **contribute** to the **nuanced** and **target-specific**
    **noradrenergic modulation** of the LC's targets. **Neuropeptide
    co-modulation of the noradrenergic signal is the functional system**
    subserved primarily by the neuropeptide-coexpressing neurons.

**These populations are prose, not structural children.** The tree
wires the **locus coeruleus** as a **single leaf** under the tegmentum
container — the **noradrenergic principal neurons** and the
**neuropeptide-coexpressing neurons** are **prose**, not structural
children. Consumers that need **neuron-population-level** resolution
should consult the references, not the tree.

The Locus Coeruleus / Laterodorsal Tegmental Nucleus Boundary
-------------------------------------------------------------
This is the **sibling** boundary — **noradrenergic vs. cholinergic
neuromodulatory nucleus**:

*   **Locus coeruleus** (this module) — the **noradrenergic** nucleus —
    the **principal source of norepinephrine** in the brain — involved
    in **arousal**, **attention**, **stress**, **pain modulation**, and
    **memory consolidation**.

*   **Laterodorsal tegmental nucleus**
    (``.../tegmentum/laterodorsal_tegmental_nucleus/``) — the
    **cholinergic** nucleus — the **principal pontine cholinergic
    source** for the **thalamus** — involved in **REM sleep**,
    **arousal**, and **motivation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(noradrenaline vs. acetylcholine), different functional systems
(noradrenergic arousal/attention/stress/pain/memory vs. cholinergic
REM-sleep/arousal/motivation), different projection targets (diffuse
noradrenergic vs. thalamic and basal-forebrain cholinergic). They are
**anatomically adjacent** (both are in the **dorsal pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the locus coeruleus with the
laterodorsal tegmental nucleus.

The Locus Coeruleus / Pedunculopontine Nucleus Boundary
-------------------------------------------------------
This is the **sibling** boundary — **noradrenergic vs. cholinergic
locomotion nucleus**:

*   **Locus coeruleus** (this module) — the **noradrenergic** nucleus.

*   **Pedunculopontine nucleus**
    (``.../tegmentum/pedunculopontine_nucleus/``) — the **cholinergic**
    (with glutamatergic and GABAergic components) nucleus — the
    **mesencephalic locomotor region** — involved in **locomotion**,
    **REM sleep**, **arousal**, and **reward**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(noradrenaline vs. acetylcholine), different functional systems
(noradrenergic arousal/attention/stress/pain/memory vs. cholinergic
locomotion/REM-sleep/arousal/reward), different anatomical locations
(the LC is **dorsomedial** at the **lateral fourth-ventricle wall**;
the PPN is **ventrolateral** at the **pontomesencephalic junction**).
Consumers must **not** conflate the locus coeruleus with the
pedunculopontine nucleus.

The Locus Coeruleus / Nucleus Incertus Boundary
-----------------------------------------------
This is the **sibling** boundary — **noradrenergic vs. relaxin-3**:

*   **Locus coeruleus** (this module) — the **noradrenergic** nucleus.

*   **Nucleus incertus** (``.../tegmentum/nucleus_incertus/``) — the
    **relaxin-3-expressing** nucleus — involved in **stress**,
    **arousal**, **feeding**, and **neuroendocrine regulation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(noradrenaline vs. relaxin-3), different functional systems
(noradrenergic arousal/attention/stress/pain/memory vs. relaxin-3
stress/arousal/feeding/neuroendocrine), different projection targets
(diffuse noradrenergic vs. septum/hippocampus/medial prefrontal
cortex/amygdala/hypothalamus). Consumers must **not** conflate the locus
coeruleus with the nucleus incertus.

The Locus Coeruleus / Pontine Micturition Center Boundary
---------------------------------------------------------
This is the **sibling** boundary — **noradrenergic vs. micturition**:

*   **Locus coeruleus** (this module) — the **noradrenergic** nucleus.

*   **Pontine micturition center**
    (``.../tegmentum/pontine_micturition_center/``) — the **micturition
    control center** — it **coordinates** the **micturition reflex**.

**They are DIFFERENT STRUCTURES** — different functional systems
(noradrenergic arousal/attention/stress/pain/memory vs. micturition),
different projection targets (diffuse noradrenergic vs. sacral spinal
cord). Consumers must **not** conflate the locus coeruleus with the
pontine micturition center.

The Locus Coeruleus / Tegmental Pontine Reticular Nucleus Boundary
------------------------------------------------------------------
This is the **sibling** boundary — **noradrenergic vs. motor relay**:

*   **Locus coeruleus** (this module) — the **noradrenergic** nucleus.

*   **Tegmental pontine reticular nucleus**
    (``.../tegmentum/tegmental_pontine_reticular_nucleus/``) — the
    **motor relay** — it **projects** to the **spinal cord** and the
    **cerebellum** — it is involved in **locomotion**, **posture**, and
    **motor pattern generation**.

**They are DIFFERENT STRUCTURES** — different functional systems
(noradrenergic arousal/attention/stress/pain/memory vs. motor relay),
different projection targets (diffuse noradrenergic vs. spinal
cord/cerebellum). Consumers must **not** conflate the locus coeruleus
with the tegmental pontine reticular nucleus.

The Locus Coeruleus / Parabrachial Area Boundary
------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Locus coeruleus** (this module) — a **noradrenergic neuromodulatory
    nucleus** — a **structural child of the pontine tegmentum
    container**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex** — a **separate
    structural child of the pons**.

**They are DIFFERENT STRUCTURES** — the parabrachial area is **not** a
structural child of the pontine tegmentum (in the tree), even though it
is **anatomically located** in the pontine tegmentum. Consumers must
**not** conflate the locus coeruleus with the parabrachial area.

The Locus Coeruleus / Superior Olivary Complex, Cranial Nerve Nuclei, PPRF, and Parvocellular Reticular Nucleus Boundary
----------------------------------------------------------------------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Locus coeruleus** (this module) — a **noradrenergic neuromodulatory
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
must **not** conflate the locus coeruleus with any of them.

The Locus Coeruleus / Pontine Nuclei Boundary
---------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Locus coeruleus** (this module) — a **noradrenergic neuromodulatory
    nucleus** in the **dorsal pontine tegmentum**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not**
conflate the locus coeruleus with the pontine nuclei.

The Locus Coeruleus / Whole Tegmentum Container Boundary
--------------------------------------------------------
This is the **sub-nucleus vs. parent** boundary:

*   **Locus coeruleus** (this module) — one of the **six neuromodulatory
    and autonomic nuclei** of the pontine tegmentum.

*   **Tegmentum container** (``.../pons/tegmentum/``) — the **dorsal
    pontine grey-matter region** — the **tree-wired container** for the
    **six neuromodulatory and autonomic nuclei**.

**The locus coeruleus is a child of the tegmentum container.** Consumers
must **not** conflate the locus coeruleus with the **whole tegmentum**.

The Locus Coeruleus / Whole Pons Boundary
-----------------------------------------
This is the **nucleus vs. grandparent** boundary:

*   **Locus coeruleus** (this module) — one of the **six neuromodulatory
    and autonomic nuclei** of the pontine tegmentum.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**.

**The locus coeruleus is a grandchild of the pons** (via the tegmentum
container). Consumers must **not** conflate the locus coeruleus with the
**whole pons**.

The Locus Coeruleus / Fourth Ventricle Boundary
-----------------------------------------------
This is the **neural tissue vs. CSF space** boundary:

*   **Locus coeruleus** (this module) — a **grey-matter nucleus** at the
    **lateral wall of** the fourth ventricle.

*   **Fourth ventricle** (``.../metencephalon/fourth_ventricle/``) — the
    **CSF-filled space** **dorsal to** the pons.

**They are DIFFERENT STRUCTURES** — the **fourth ventricle** is a
**fluid space**; the **locus coeruleus** is **neural tissue**. Consumers
must **not** conflate the locus coeruleus with the fourth ventricle.

The Locus Coeruleus / Midbrain Tegmentum and Medullary Tegmentum Boundary
-------------------------------------------------------------------------
This is the **pons vs. midbrain/medulla** boundary:

*   **Locus coeruleus** (this module) — a **specific nucleus** in the
    **dorsal portion of the pons**.

*   **Midbrain tegmentum** (``.../midbrain/tegmentum/``) and **medullary
    tegmentum** — the **dorsal portions** of the **midbrain** and the
    **medulla oblongata**.

**They are DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate
the locus coeruleus with the midbrain tegmentum or the medullary
tegmentum.

The Locus Coeruleus / Substantia Nigra, Ventral Tegmental Area, and Raphe Nuclei Boundary
-----------------------------------------------------------------------------------------
This is the **noradrenergic vs. dopaminergic/serotonergic** boundary:

*   **Locus coeruleus** (this module) — the **noradrenergic** nucleus —
    the **principal source of norepinephrine** in the brain.

*   **Substantia nigra** (pars compacta, midbrain) and **ventral
    tegmental area** (midbrain) — the **dopaminergic** nuclei — the
    **principal sources of dopamine** in the brain.

*   **Dorsal raphe nucleus** and **median raphe nucleus**
    (midbrain/pons) — the **serotonergic** nuclei — the **principal
    sources of serotonin** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(noradrenaline vs. dopamine vs. serotonin), different anatomical
locations (pons vs. midbrain), different functional systems
(noradrenergic arousal/attention/stress/pain/memory vs. dopaminergic
reward/motor control/learning vs. serotonergic mood/sleep/appetite/
pain). **This distinction is neurochemically load-bearing** — consumers
must **not** conflate the locus coeruleus with the dopaminergic or
serotonergic nuclei.

The Locus Coeruleus / SLEA Boundary
-----------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Locus coeruleus** (this module) — **SLEA-FREE**. It is **not** an
    extended-amygdala component, and it carries **no SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The locus coeruleus is NOT part of the SLEA continuum.** It is a
**noradrenergic neuromodulatory nucleus**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the locus
coeruleus.

Function in the Human Brain
---------------------------
The locus coeruleus's functions are **the noradrenergic modulation of
arousal, attention, stress, pain, and memory** — **NOT a single unified
function**:

*   **Arousal and Wakefulness:** The **noradrenergic principal neurons**
    of the LC **project diffusely** to the **entire forebrain** (the
    **cortex**, the **thalamus**, the **hypothalamus**, the **basal
    forebrain**) and to the **brainstem arousal centers** — they
    **promote** the **wakeful** and **alert** states by **increasing**
    the **excitability** of the **cortical** and **thalamic** neurons.
    **Loss of LC noradrenergic neurons** is associated with **reduced
    arousal** and **cognitive slowing** (as in **Alzheimer's disease**
    and **Parkinson's disease**).

*   **Attention and Adaptive Gain:** The **LC noradrenergic** neurons
    **modulate** the **signal-to-noise ratio** of **cortical
    processing** — they **increase** the **gain** of **task-relevant**
    neural responses and **decrease** the **gain** of **task-
    irrelevant** responses. **This "adaptive gain"** function is the
    **neural substrate** of **attention** — the **LC** is the
    **noradrenergic** system that **focuses** the brain on **behaviorally
    relevant** stimuli. **Phasic LC activation** is associated with
    **focused attention**; **tonic LC activation** is associated with
    **exploration** and **distractibility**.

*   **Stress Response:** The **LC noradrenergic** neurons **respond** to
    **stressful stimuli** — they **increase** their **firing rate** and
    **norepinephrine release** in response to **threats**,
    **pain**, **hypoglycemia**, **hypotension**, and **other
    stressors** — they **activate** the **sympathetic nervous system**
    (via the **hypothalamus** and the **brainstem autonomic centers**)
    and **the HPA axis** (via the **hypothalamus**). **This "stress
    response"** function is the **neural substrate** of the **body's
    alarm system** — the **LC** is the **noradrenergic** system that
    **mobilizes** the body **to cope with stressors**.

*   **Pain Modulation (Descending Noradrenergic Inhibition):** The **LC
    noradrenergic** neurons **project** to the **spinal cord dorsal
    horn** — they **inhibit** the **nociceptive** (pain) transmission
    via **α2-adrenergic receptors** on the **dorsal horn** neurons —
    they **suppress** the **pain signal** at the **spinal level**.
    **This "descending noradrenergic inhibition"** function is the
    **neural substrate** of **endogenous pain modulation** — the **LC**
    is the **noradrenergic** system that **suppresses** pain via the
    **descending inhibitory pathway**.

*   **Memory Consolidation (Noradrenergic Modulation of the
    Hippocampus and the Amygdala):** The **LC noradrenergic** neurons
    **project** to the **hippocampus** (for **episodic** and **spatial**
    memory) and to the **amygdala** (for **emotional** memory) — they
    **modulate** the **synaptic plasticity** (the **long-term
    potentiation** and **long-term depression**) that **underlies**
    **memory consolidation**. **This "emotional memory enhancement"**
    function is the **neural substrate** of the **noradrenergic
    modulation of memory** — the **LC** is the **noradrenergic**
    system that **prioritizes** the **memory** of **emotionally
    salient** events.

*   **Autonomic Regulation (Brainstem and Spinal Cord Noradrenergic
    Modulation):** The **LC noradrenergic** neurons **project** to the
    **brainstem autonomic centers** (the **solitary nucleus**, the
    **dorsal motor nucleus of the vagus**, the **nucleus ambiguus**, the
    **rostral ventrolateral medulla**) and to the **spinal cord
    intermediolateral cell column** — they **modulate** the
    **cardiovascular**, **respiratory**, and **gastrointestinal**
    functions via their **noradrenergic** projections. **This
    "autonomic regulation"** function is the **neural substrate** of the
    **noradrenergic modulation of autonomic outflow** — the **LC** is
    the **noradrenergic** system that **adjusts** the **autonomic
    state** to the **behavioral state**.

*   **Neuroplasticity and the Noradrenergic "Gain" of the Brain:** The
    **LC noradrenergic** system **modulates** the **entire brain's
    excitability** — it **adjusts** the **"gain"** of the **nervous
    system** to the **organism's behavioral state** (wakefulness,
    attention, stress, exploration, sleep). **This "gain
    modulation"** function is the **neural substrate** of the **LC's
    role as a global neuromodulatory system** — the **LC** is the
    **noradrenergic** system that **sets the stage** for **all other
    neural processing**.

*   **NOT a neural processor in the classical sense.** The LC is a
    **neuromodulatory nucleus** — it **receives** afferent inputs (from
    the **hypothalamus**, the **brainstem**, the **limbic system**, and
    the **cortex**) and **projects diffusely** to the **entire
    forebrain**, the **brainstem**, and the **spinal cord**. The
    **processing** of arousal, attention, stress, pain, and memory
    happens in a **distributed** manner across the **LC**, the
    **targets of the LC** (the **cortex**, the **hippocampus**, the
    **amygdala**, the **thalamus**, the **hypothalamus**, the
    **brainstem**, the **spinal cord**), and the **other
    neuromodulatory systems** (the **cholinergic**, **dopaminergic**,
    and **serotonergic** systems) that **interact** with the **LC**.

**The unifying theme:** the locus coeruleus is the **pontine
noradrenergic nucleus** — the **sole noradrenergic source** for the
**forebrain** and the **sole noradrenergic source** for the **cortex**.
It is **noradrenergic** (with **neuropeptide co-transmitters**),
**SLEA-free**, and **NOT the laterodorsal tegmental nucleus** — the
**LDT** is the **cholinergic** neuromodulatory nucleus. The **LC** is
the **noradrenergic** neuromodulatory nucleus — the **"blue spot"** that
colors the brain's arousal, attention, and stress responses.

Associated Disorders
--------------------
The locus coeruleus has **no named "locus coeruleus syndrome"** — its
clinical associations are **function-specific**:

*   **Alzheimer's Disease — LC Involvement:** **Alzheimer's disease** is
    characterized by **early loss** of **locus coeruleus noradrenergic
    neurons** — the **LC neuronal loss** **precedes** the **cortical
    pathology** in some cases, and it **contributes** to the **cognitive
    decline**, the **sleep disturbances**, and the **behavioral
    symptoms** of **Alzheimer's disease**. The **LC** is **one of the
    earliest** brain regions affected by **Alzheimer's disease
    pathology** (tau pathology).

*   **Parkinson's Disease — LC Involvement:** **Parkinson's disease** is
    characterized by **loss** of **locus coeruleus noradrenergic
    neurons** (in addition to the **substantia nigra dopaminergic**
    loss) — the **LC neuronal loss** **contributes** to the
    **non-motor symptoms** of **Parkinson's disease** (depression,
    anxiety, sleep disturbances, cognitive decline, autonomic
    dysfunction).

*   **PTSD — LC Hyperactivity:** **Post-traumatic stress disorder**
    (PTSD) has been **associated** with **hyperactive noradrenergic
    signaling** — the **LC** is **hyperactive** in **PTSD**, and this
    **contributes** to the **hyperarousal**, **hypervigilance**, and
    **intrusive memories** that are **hallmark** features of **PTSD**.
    **α1-adrenergic antagonists** (e.g., **prazosin**) are used to
    **reduce** the **LC-mediated hyperarousal** in **PTSD**.

*   **Depression — LC Dysregulation:** **Major depressive disorder** has
    been **associated** with **noradrenergic dysregulation** — the
    **LC** may be **hypoactive** in some forms of **depression**, and
    **noradrenergic** antidepressants (e.g., **tricyclic
    antidepressants**, **SNRIs**) **increase** the **noradrenergic
    signaling** to **alleviate** the **depressive symptoms**.

*   **ADHD — LC Dysregulation:** **Attention-deficit/hyperactivity
    disorder** (ADHD) has been **associated** with **noradrenergic
    dysregulation** — the **LC's attention-related "adaptive gain"**
    function may be **impaired** in **ADHD**, and **noradrenergic**
    medications (e.g., **atomoxetine**, **guanfacine**) are used to
    **improve** the **attention** and **impulse control** in **ADHD**.

*   **Opioid Withdrawal — LC Hyperactivity:** **Opioid withdrawal** is
    associated with **locus coeruleus hyperactivity** — the **LC** is
    **tonically inhibited** by **opioids** (via **μ-opioid receptors**),
    and **opioid withdrawal** **removes** this **inhibition** — the
    **LC** becomes **hyperactive**, and this **contributes** to the
    **autonomic symptoms** of **opioid withdrawal** (tachycardia,
    hypertension, sweating, diarrhea, anxiety). **α2-adrenergic
    agonists** (e.g., **clonidine**, **lofexidine**) are used to
    **suppress** the **LC hyperactivity** during **opioid withdrawal**.

*   **REM Sleep Behavior Disorder (RBD) — LC Involvement:** **REM sleep
    behavior disorder** (RBD) has been **associated** with
    **dysfunction** of the **pontine REM-sleep nuclei** — the **LC**
    **interacts** with the **cholinergic REM-sleep nuclei** (the **LDT**
    and the **PPN**) and with the **sublaterodorsal nucleus** — the
    **LC's noradrenergic** and **cholinergic** balance is **altered**
    in **RBD** — the **LC** **contributes** to the **REM-sleep
    dysregulation** in **RBD**.

*   **Pontine Stroke — LC Involvement:** A **pontine stroke** (e.g.,
    **basilar artery** perforator territory) involving the **LC** causes
    **arousal dysfunction**, **attention dysfunction**, **autonomic
    dysregulation**, and **pain modulation deficits** — often accompanied
    by **other pontine signs** (**hemiparesis**, **facial palsy**,
    **abducens palsy**, **cerebellar ataxia**).

*   **No Named "LC Syndrome":** The locus coeruleus is a
    **neurochemically distinct neuromodulatory nucleus** — it has **no
    named clinical syndrome** of its own. Its clinical relevance is
    **noradrenergic arousal, attention, stress, pain, and memory
    specific** — **Alzheimer's disease**, **Parkinson's disease**,
    **PTSD**, **depression**, **ADHD**, **opioid withdrawal**, **RBD**,
    and **pontine stroke** are all **LC-involved** conditions.

**What is NOT here:** The locus coeruleus is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **acoustic neuroma** (CN VIII nerve), **vestibular neuritis**
(vestibular nerve), **labyrinthitis** (inner ear), **auditory neuropathy
spectrum disorder** (cochlear nerve or hair cell), **Wallenberg
syndrome** (lateral medulla), **internuclear ophthalmoplegia** (MLF), or
**horizontal gaze palsy** (PPRF or abducens nucleus). Its clinical
relevance is **noradrenergic arousal, attention, stress, pain, and
memory specific**, via the **noradrenergic principal neurons** it
subserves. **No named LC syndrome exists.**

Lateralization Notes
--------------------
This is the **single** locus coeruleus module. The LC is **bilateral in
real anatomy** (left LC and right LC), but the tree wires it as a
**single module** — and the module carries **NO warning at the module
level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **locus_coeruleus** module (here) is a **single module** that
    represents the **bilateral LC** (the left LC and the right LC). The
    tree does **not** split them into left/right. Consumers must **not**
    assume a left/right split exists at the tree level — the module is a
    **single, bilateral representation**.

*   **Bilateral Diffuse Projections (Structural Fact, NOT a
    Lateralization Warning):** The **LC** **projects bilaterally** to
    the **entire forebrain**, the **brainstem**, and the **spinal
    cord** — each LC projects to **both** left and right targets. **This
    bilateral diffuse projection** is a **structural fact** of the
    **noradrenergic neuromodulatory system** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **global noradrenergic modulation** of arousal, attention, stress,
    pain, and memory.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The LC is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the LC.

*   **NO Amygdala-Lateralization Warning of their own (the LC is
    NORADRENERGIC NEUROMODULATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The LC is a
    **noradrenergic neuromodulatory nucleus** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**. The
    LC **projects to** the **amygdala** (modulating emotional memory) —
    but the **LC itself** is **not a fear-output structure**.

**A consumer that sees "locus_coeruleus" must understand that the module
is a SINGLE, BILATERAL representation** — it is **not** a left/right
split at the tree level. The **bilateral diffuse projections** are
**structural facts**, not lateralizations. The LC is a **strict-single
module with NO warning at the module level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** LC as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/laterodorsal_tegmental_nucleus/``,
    ``.../tegmentum/nucleus_incertus/``,
    ``.../tegmentum/pedunculopontine_nucleus/``,
    ``.../tegmentum/pontine_micturition_center/``,
    ``.../tegmentum/tegmental_pontine_reticular_nucleus/``,
    ``.../pons/parabrachial_area/``,
    ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../pons/pontine_nuclei/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, or any other container. The LC's
    relationships to the **laterodorsal tegmental nucleus**, the
    **nucleus incertus**, the **pedunculopontine nucleus**, the
    **pontine micturition center**, the **tegmental pontine reticular
    nucleus**, the **parabrachial area**, the **superior olivary
    complex**, the **cranial nerve nuclei**, the **PPRF**, the
    **parvocellular reticular nucleus**, the **pontine nuclei**, the
    **fourth ventricle**, the **midbrain tegmentum**, the **medullary
    tegmentum**, the **substantia nigra**, the **ventral tegmental
    area**, the **raphe nuclei**, the **whole tegmentum container**, the
    **whole pons**, and the **SLEA continuum** are documented as
    **prose and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **noradrenergic
    principal neurons** and the **neuropeptide-coexpressing neurons** are
    documented as **prose**, not as sub-modules. Consumers must not
    assume any exist as children; resolve neuron-population-level
    detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The **LC**
    is a **single module** that represents the **bilateral LC** — the
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **NORADRENERGIC NEUROMODULATORY NUCLEUS — NOT a motor or sensory
    relay.** The **LC** is a **neuromodulatory nucleus** —
    **projecting diffusely** to the entire forebrain, the brainstem, and
    the spinal cord. Consumers must **not** conflate the LC with a motor
    or sensory relay.
*   **NORADRENERGIC — NOT cholinergic, dopaminergic, or serotonergic.**
    The **LC** is the **sole noradrenergic source** for the forebrain
    and the cortex. The **cholinergic** nuclei (LDT and PPN), the
    **dopaminergic** nuclei (substantia nigra and VTA), and the
    **serotonergic** nuclei (raphe nuclei) are **different structures**.
    Consumers must **not** conflate the LC with any of them.
*   **NOT the laterodorsal tegmental nucleus — that is the CHOLINERGIC
    neuromodulatory nucleus.** Consumers must **not** conflate the LC
    with the LDT.
*   **NOT the pedunculopontine nucleus — that is the CHOLINERGIC
    LOCOMOTION nucleus.** Consumers must **not** conflate the LC with
    the PPN.
*   **NOT the nucleus incertus, the pontine micturition center, or the
    tegmental pontine reticular nucleus — those are DIFFERENT
    neuromodulatory and autonomic nuclei.** Consumers must **not**
    conflate the LC with any of them.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, the PPRF, or the parvocellular reticular
    nucleus — those are SEPARATE structural children of the pons.**
    Consumers must **not** conflate the LC with any of them.
*   **NOT the pontine nuclei — those are in the BASILAR pons.**
    Consumers must **not** conflate the LC with the pontine nuclei.
*   **NOT the whole tegmentum container — that is the PARENT.**
    Consumers must **not** conflate the LC with the whole tegmentum.
*   **NOT the whole pons — that is the GRANDPARENT.** Consumers must
    **not** conflate the LC with the whole pons.
*   **NOT the fourth ventricle — that is a CSF SPACE.** Consumers must
    **not** conflate the LC with the fourth ventricle.
*   **NOT the midbrain tegmentum or the medullary tegmentum — those are
    DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate the LC
    with the midbrain tegmentum or the medullary tegmentum.
*   **NOT the substantia nigra, the ventral tegmental area, or the raphe
    nuclei — those are DOPAMINERGIC or SEROTONERGIC nuclei.** Consumers
    must **not** conflate the LC with the dopaminergic or serotonergic
    nuclei.
*   **MULTIPLE NEUROCHEMICALLY DISTINCT NEURON POPULATIONS —
    noradrenergic principal neurons and neuropeptide-coexpressing
    neurons.** The **noradrenergic principal neurons** (the vast
    majority) and the **neuropeptide-coexpressing neurons** (the
    minority) are **prose**, not structural children. Consumers must
    **not** treat the LC as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The LC is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the LC is NORADRENERGIC NEUROMODULATORY.**
    The **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **LC** is a **noradrenergic neuromodulatory nucleus**
    — it is **not** part of the fear circuit. **The LC projects to** the
    amygdala (modulating emotional memory) — but the **LC itself** is
    **not a fear-output structure**.
*   **No ``AREA_PATHS`` hop.** The LC is a local leaf under the
    tegmentum container, not a cross-listed leaf.
*   **No nested cross-listing.** The LC has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum import locus_coeruleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.tegmentum.locus_coeruleus"
    )

**Do not** assume the LC is a **container**. It is a **leaf** — the
**noradrenergic principal neurons** and the **neuropeptide-coexpressing
neurons** are **prose**, not structural children.

**Do not** assume the LC is **bilateralized at the tree level**. The LC
is **bilateral in real anatomy**, but the tree wires it as a **single
module** — there is **no left/right split at the module level**.

**Do not** assume the LC is the **laterodorsal tegmental nucleus** or
the **pedunculopontine nucleus**. The **LDT** and the **PPN** are
**cholinergic** nuclei — the **LC** is the **noradrenergic** nucleus.
They are **different structures** — different neurotransmitters and
different functional systems.

**Do not** assume the LC is the **nucleus incertus**, the **pontine
micturition center**, or the **tegmental pontine reticular nucleus**.
Those are **different structures** — the **nucleus incertus**
(relaxin-3 stress/arousal), the **pontine micturition center**
(micturition), and the **tegmental pontine reticular nucleus** (motor
relay).

**Do not** assume the LC is the **substantia nigra**, the **ventral
tegmental area**, or the **raphe nuclei**. Those are **different
structures** — the **substantia nigra** and the **ventral tegmental
area** are **dopaminergic** (midbrain); the **raphe nuclei** are
**serotonergic** (midbrain/pons). The **LC** is the **noradrenergic**
nucleus (pons).

**Do not** assume the LC is the **parabrachial area**, the **superior
olivary complex**, the **cranial nerve nuclei**, the **PPRF**, or the
**parvocellular reticular nucleus**. Those are **separate structural
children of the pons** — even though they are anatomically located in
the pontine tegmentum.

**Do not** assume the LC is the **pontine nuclei**. The **pontine
nuclei** are in the **basilar pons** — the LC is in the **dorsal
pontine tegmentum**.

**Do not** assume the LC is the **whole tegmentum** or the **whole
pons**. The **tegmentum** is the **parent**; the **pons** is the
**grandparent**.

**Do not** assume the LC is the **fourth ventricle**. The **fourth
ventricle** is a **CSF space**; the LC is **neural tissue** at the
**lateral wall of the fourth ventricle**.

**Do not** assume the LC is the **midbrain tegmentum** or the **medullary
tegmentum**. Those are **different brainstem levels**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the LC. **The LC is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the LC's (empty) children (recommended consumer pattern)::

    LOCUS_COERULEUS_CHILDREN = ()
    # The LC is a leaf. The noradrenergic principal neurons and the
    # neuropeptide-coexpressing neurons are prose, not modules.

Reaching the laterodorsal tegmental nucleus (recommended consumer
pattern — the cholinergic sibling)::

    # The laterodorsal tegmental nucleus is the CHOLINERGIC sibling under
    # the tegmentum container:
    #
    #   .../pons/tegmentum/laterodorsal_tegmental_nucleus/
    #
    # The LDT is cholinergic; the LC is noradrenergic. They are
    # ANATOMICALLY ADJACENT but FUNCTIONALLY DISTINCT.

Reaching the pedunculopontine nucleus (recommended consumer pattern — the
cholinergic locomotion sibling)::

    # The pedunculopontine nucleus is the CHOLINERGIC LOCOMOTION sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pedunculopontine_nucleus/
    #
    # The PPN is cholinergic; the LC is noradrenergic. They are
    # DIFFERENT STRUCTURES with DIFFERENT neurotransmitters and
    # functional systems.

Reaching the nucleus incertus (recommended consumer pattern — the
relaxin-3 sibling)::

    # The nucleus incertus is the RELAXIN-3-EXPRESSING sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/nucleus_incertus/
    #
    # The nucleus incertus is relaxin-3-expressing; the LC is
    # noradrenergic. They are DIFFERENT STRUCTURES.

Reaching the pontine micturition center (recommended consumer pattern —
the micturition sibling)::

    # The pontine micturition center is the MICTURITION CONTROL sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pontine_micturition_center/
    #
    # The pontine micturition center coordinates the micturition reflex;
    # the LC is the noradrenergic neuromodulatory nucleus.

Reaching the tegmental pontine reticular nucleus (recommended consumer
pattern — the motor relay sibling)::

    # The tegmental pontine reticular nucleus is the MOTOR RELAY sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/tegmental_pontine_reticular_nucleus/
    #
    # The tegmental pontine reticular nucleus is involved in locomotion,
    # posture, and motor pattern generation; the LC is the noradrenergic
    # neuromodulatory nucleus.

Reaching the parabrachial area (recommended consumer pattern — a
SEPARATE pons child)::

    # The parabrachial area is a SEPARATE STRUCTURAL CHILD of the pons:
    #
    #   .../pons/parabrachial_area/
    #
    # The parabrachial area is the visceral-sensory and respiratory-relay
    # complex; the LC is a noradrenergic neuromodulatory nucleus.

Reaching the whole tegmentum container (recommended consumer pattern —
the PARENT)::

    # The tegmentum container is the DORSAL PONTINE GREY-MATTER REGION
    # that CONTAINS the LC as one of its six structural children:
    #
    #   .../pons/tegmentum/
    #
    # The LC is a CHILD of the tegmentum container.

Reaching the whole pons (recommended consumer pattern — the
GRANDPARENT)::

    # The pons is the WHOLE METENCEPHALIC BRAINSTEM SEGMENT that CONTAINS
    # the tegmentum container:
    #
    #   .../pons/
    #
    # The LC is a GRANDCHILD of the pons.

Bilateral iteration (recommended consumer pattern)::

    # The LC is a SINGLE module (not bilateralized at the tree level).
    # The module represents the BILATERAL LC.
    lc_path = (
        "hindbrain.metencephalon.pons.tegmentum.locus_coeruleus"
    )
    # resolve lc_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The LC's neuron populations are prose, not modules:
    #   noradrenergic principal neurons -> synthesize and release
    #       norepinephrine; project diffusely to the entire forebrain
    #       (cortex, hippocampus, amygdala, thalamus, hypothalamus,
    #       septum, basal forebrain), the brainstem (parabrachial area,
    #       solitary nucleus, vagal nuclei, raphe nuclei, cerebellum),
    #       and the spinal cord (dorsal horn for pain modulation;
    #       ventral horn for motor modulation); the noradrenergic arousal,
    #       attention, stress, pain modulation, and memory consolidation
    #   neuropeptide-coexpressing neurons -> co-express norepinephrine
    #       with neuropeptides (galanin, neuropeptide Y, somatostatin,
    #       etc.); co-release the neuropeptide with norepinephrine;
    #       modulate the norepinephrine signal at the target
    #
    # Do not attempt to resolve these as sub-paths of the LC — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical LC anatomy:** Dahlström, A., Fuxe, K. (1964). "Evidence
    for the existence of monoamine-containing neurons in the central
    nervous system. I. Demonstration of monoamines in the cell bodies of
    brain stem neurons." *Acta Physiologica Scandinavica* 62:1–55.
    (Original demonstration of the noradrenergic locus coeruleus
    neurons.)
*   **LC — canonical modern review:** Aston-Jones, G., Cohen, J.D.
    (2005). "An integrative theory of locus coeruleus-norepinephrine
    function: adaptive gain and optimal performance." *Annual Review
    of Neuroscience* 28:403–450. (LC — noradrenergic arousal,
    attention, and adaptive gain.)
*   **LC — comprehensive review:** Sara, S.J. (2009). "The locus
    coeruleus and noradrenergic modulation of cognition." *Nature
    Reviews Neuroscience* 10:211–223. (LC — noradrenergic modulation of
    cognition, attention, and memory.)
*   **LC — arousal and wakefulness:** Berridge, C.W., Waterhouse, B.D.
    (2003). "The locus coeruleus-noradrenergic system: modulation of
    behavioral state and state-dependent cognitive processes." *Brain
    Research Reviews* 42:33–84. (LC — arousal and wakefulness.)
*   **LC — stress response:** Valentino, R.J., Van Bockstaele, E.
    (2008). "Convergent regulation of locus coeruleus activity as an
    adaptive response to stress." *European Journal of Pharmacology*
    583:194–203. (LC — stress response and CRF regulation.)
*   **LC — pain modulation:** Pertovaara, A. (2006). "Noradrenergic
    pain modulation — a review." *Progress in Neurobiology*
    80:53–83. (LC — descending noradrenergic pain modulation.)
*   **LC — memory consolidation:** McGaugh, J.L. (2004). "The amygdala
    modulates the consolidation of memories of emotionally arousing
    experiences." *Annual Review of Neuroscience* 27:1–28. (LC —
    noradrenergic modulation of emotional memory consolidation.)
*   **Alzheimer's disease — LC involvement:** Braak, H., Del Tredici,
    K. (2011). "The pathological process underlying Alzheimer's disease
    in individuals under thirty." *Acta Neuropathologica* 121:171–181.
    (Alzheimer's disease — early LC involvement; tau pathology.)
*   **Parkinson's disease — LC involvement:** Hirsch, E.C., Graybiel,
    A.M., Duyckaerts, C., Javoy-Agid, F. (1987). "Neuronal loss in the
    pedunculopontine tegmental nucleus in Parkinson disease and in
    progressive supranuclear palsy." *Proceedings of the National
    Academy of Sciences* 84:5976–5980. (Parkinson's disease — LC
    degeneration contributes to non-motor symptoms.)
*   **PTSD — LC hyperactivity:** Southwick, S.M., Bremner, J.D.,
    Rasmusson, A., et al. (1999). "Role of norepinephrine in the
    pathophysiology and treatment of posttraumatic stress disorder."
    *Biological Psychiatry* 46:1192–1204. (PTSD — LC hyperactivity;
    α1-adrenergic antagonists for treatment.)
*   **Depression — LC dysregulation:** Anand, A., Charney, D.S. (2000).
    "Norepinephrine dysfunction in depression." *Journal of Clinical
    Psychiatry* 61:16–24. (Depression — noradrenergic dysregulation; LC
    involvement.)
*   **ADHD — LC dysregulation:** Arnsten, A.F.T., Pliszka, S.R. (2011).
    "Catecholamine influences on prefrontal cortical function: relevance
    to treatment of attention deficit/hyperactivity disorder and related
    disorders." *Pharmacology Biochemistry and Behavior* 99:211–216.
    (ADHD — noradrenergic modulation; LC involvement.)
*   **Opioid withdrawal — LC hyperactivity:** Aghajanian, G.K. (1978).
    "Tolerance of locus coeruleus neurones to morphine and suppression
    of withdrawal response by clonidine." *Nature* 276:186–188. (Opioid
    withdrawal — LC hyperactivity; clonidine for treatment.)
*   **REM sleep behavior disorder — LC involvement:** Boeve, B.F.,
    Silber, M.H., Ferman, T.J., et al. (2001). "Association of REM
    sleep behavior disorder and neurodegenerative disease may reflect an
    underlying synucleinopathy." *Movement Disorders* 16:622–630. (RBD —
    pontine REM-sleep nuclei involvement, including the LC.)
*   **Pontine stroke — LC involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — pontine tegmentum involvement,
    including the LC.)
*   **Laterodorsal tegmental nucleus (contrast — the CHOLINERGIC
    neuromodulatory sibling):** Mesulam, M.M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the rat:
    an overview based on an alternative nomenclature (Ch1-Ch6)."
    *Neuroscience* 10:1185–1201. (LDT — cholinergic neuromodulatory
    nucleus; sibling of the LC.)
*   **Pedunculopontine nucleus (contrast — the CHOLINERGIC LOCOMOTION
    sibling):** Garcia-Rill, E. (1991). "The pedunculopontine nucleus."
    *Progress in Neurobiology* 36:363–389. (PPN — cholinergic
    locomotion and REM-sleep nucleus; sibling of the LC.)
*   **Nucleus incertus (contrast — the RELAXIN-3 sibling):** Ryan, P.J.,
    Ma, S., Olucha-Bordonau, F.E., Gundlach, A.L. (2011). "Nucleus
    incertus — an emerging role in the behavioural actions of
    relaxin-3." *British Journal of Pharmacology* 162:1115–1126.
    (Nucleus incertus — relaxin-3 stress, arousal, and feeding; sibling
    of the LC.)
*   **Pontine micturition center (contrast — the MICTURITION sibling):**
    Barrington, F.J.F. (1925). "The effect of lesions of the hind- and
    mid-brain on micturition in the cat." *Quarterly Journal of
    Experimental Physiology* 15:81–102. (Pontine micturition center —
    micturition control; sibling of the LC.)
*   **Tegmental pontine reticular nucleus (contrast — the MOTOR RELAY
    sibling):** Brodal, A. (2010). *The Central Nervous System: Structure
    and Function*, 4th ed. (Tegmental pontine reticular nucleus — motor
    relay; sibling of the LC.)
*   **Substantia nigra and ventral tegmental area (contrast — the
    DOPAMINERGIC nuclei):** Björklund, A., Dunnett, S.B. (2007).
    "Dopamine neuron systems in the brain: an update." *Trends in
    Neurosciences* 30:194–202. (Substantia nigra and VTA — dopaminergic
    nuclei; distinct from the LC.)
*   **Raphe nuclei (contrast — the SEROTONERGIC nuclei):** Hornung,
    J.P. (2003). "The human raphe nuclei and the serotonergic system."
    *Journal of Chemical Neuroanatomy* 26:331–343. (Raphe nuclei —
    serotonergic nuclei; distinct from the LC.)
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
    pons; distinct from the LC.)
*   **Fourth ventricle (contrast — a CSF space):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Fourth ventricle — CSF space dorsal to the pons; distinct from the
    LC.)
*   **Midbrain tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Midbrain tegmentum — dorsal midbrain; distinct
    from the pontine tegmentum.)
*   **Medullary tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary tegmentum — dorsal medulla; distinct
    from the pontine tegmentum.)
*   **SLEA (contrast — the LC is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the LC.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the LC.)
*   NeuroNames — Locus coeruleus; FMA — Locus coeruleus.
"""