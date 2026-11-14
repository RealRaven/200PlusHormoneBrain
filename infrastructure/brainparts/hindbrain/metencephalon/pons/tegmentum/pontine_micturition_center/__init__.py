"""
infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum.pontine_micturition_center
=========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── tegmentum
                └── pontine_micturition_center   <-- THIS MODULE

**Primary synonym:** Pontine micturition center; PMC; Barrington's
nucleus; Barrington's nucleus of the pons; "the pontine micturition
control center"; "the pontine bladder control nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — an **anatomically delimited
glutamatergic/GABAergic nucleus** in the **dorsolateral pontine
tegmentum**, **ventromedial to the locus coeruleus** and **dorsolateral
to the superior cerebellar peduncle**, near the **lateral wall of the
fourth ventricle**. It is the **pontine micturition control center** —
the **neural substrate** of the **micturition reflex** — and the
**neural substrate** of the **voluntary control of micturition**.
**Part of:** The **tegmentum** container — specifically, the
**autonomic (micturition)** component. The **tegmentum** is the
**dorsal pontine grey-matter region** — the **tree-wired container** for
the six neuromodulatory and autonomic nuclei of the dorsal pons.
**Structural parent:** ``.../tegmentum/`` → **direct child** of the
tegmentum container.
**Structural children:** **None.** This is a **leaf** module. The
**corticotropin-releasing factor (CRF)-expressing neurons** (the
**principal population**), the **glutamatergic neurons**, and the
**GABAergic neurons** are documented as **prose**, not as structural
children — they are the **functionally distinct neuron populations**
within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
pontine micturition center is a LEAF, not a container.** It has **no
structural children**. The **CRF-expressing neurons**, the
**glutamatergic neurons**, and the **GABAergic neurons** are **prose**
populations, not structural children. Consumers must **not** treat the
pontine micturition center as a container, and must **not** assume the
neuron populations exist as sub-modules.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the pontine micturition center is a SINGLE module at
the tree level, even though the PMC is BILATERAL in real anatomy.**
Unlike the **cranial_nerve_nuclei** module (which has explicit ``left``
and ``right`` structural children) or the **superior_olivary_complex**
module (which has ``left`` and ``right`` sub-containers), the
**pontine_micturition_center** module (here) is a **single module** that
represents the **bilateral PMC** (the left PMC and the right PMC). The
tree does **not** split them into left/right. Consumers must **not**
assume a left/right split exists at the tree level — the module is a
**single, bilateral representation**. Any lateralization is documented
**here, in the Lateralization Notes**, not imported from elsewhere.
**Boundary status (AUTONOMIC CONTROL NUCLEUS — NOT a motor or sensory
relay):** **Boundary case — the pontine micturition center is an
AUTONOMIC CONTROL NUCLEUS, NOT a motor or sensory relay.** Unlike the
**cranial nerve motor nuclei** (branchial or somatic motor relays) or
the **sensory nuclei** (e.g., the cochlear nuclei, the trigeminal
nuclei), the **pontine micturition center** (here) is an **autonomic
control nucleus** — its **CRF-expressing (with glutamatergic and
GABAergic components)** neurons **project** to the **sacral spinal
cord** (the **parasympathetic preganglionic neurons** of the **bladder**
and the **Onuf's nucleus** of the **external urethral sphincter**) to
**coordinate** the **micturition reflex** — they **do not** directly
**relay** motor commands or **transmit** sensory information. **This
distinction is functionally load-bearing** — the PMC is a
**state-setting** nucleus (micturition), not a **throughput** nucleus.
Consumers must **not** conflate the pontine micturition center with a
motor or sensory relay.
**Boundary status (GLUTAMATERGIC AND GABAERGIC — NOT a monoaminergic,
cholinergic, or relaxin-3-expressing nucleus):** **Boundary case — the
pontine micturition center is GLUTAMATERGIC AND GABAERGIC, NOT a
monoaminergic, cholinergic, or relaxin-3-expressing nucleus.** The
**pontine micturition center** neurons are **predominantly
glutamatergic** (with some **GABAergic** components and substantial
**CRF co-expression**) — they use **glutamate** as their **principal
excitatory neurotransmitter** and **GABA** as their **inhibitory
neurotransmitter** — and they are **not** monoaminergic (dopamine,
norepinephrine, serotonin, histamine), **not** cholinergic, and **not**
relaxin-3-expressing. **The other pontine tegmentum nuclei** use
**different neurotransmitters** (noradrenaline for the locus coeruleus;
acetylcholine for the LDT and PPN; relaxin-3 for the nucleus incertus;
the tegmental pontine reticular nucleus is also glutamatergic/GABAergic
but is a **motor relay**, not a micturition control center). **This
distinction is neurochemically load-bearing** — the PMC is **not a
neuromodulatory nucleus** in the classic sense (it does not project
diffusely to the forebrain); it is an **autonomic control nucleus** that
**coordinates** the **micturition reflex** via **specific descending
projections** to the **sacral spinal cord**. Consumers must **not**
conflate the PMC with the **monoaminergic** nuclei (the locus coeruleus,
the substantia nigra, the ventral tegmental area, the raphe nuclei), the
**cholinergic** nuclei (the LDT and PPN), the **relaxin-3** nucleus (the
nucleus incertus), or the **motor relay** nucleus (the tegmental pontine
reticular nucleus).
**Boundary status (NOT the locus coeruleus — that is the NORADRENERGIC
neuromodulatory nucleus):** **Boundary case — the pontine micturition
center is NOT the locus coeruleus (LC).** The **locus coeruleus**
(``.../tegmentum/locus_coeruleus/``) is the **noradrenergic** nucleus —
the **sole noradrenergic source** for the **forebrain** — it is
involved in **arousal**, **attention**, **stress**, **pain modulation**,
and **memory consolidation**. The **pontine micturition center** (here)
is the **glutamatergic/GABAergic autonomic control nucleus** — it
**coordinates** the **micturition reflex**. They are **DIFFERENT
STRUCTURES** — different neurotransmitters (glutamate/GABA vs.
noradrenaline), different functional systems (micturition vs.
noradrenergic arousal/attention/stress/pain/memory), different
projection targets (sacral spinal cord vs. diffuse noradrenergic). They
are **anatomically adjacent** (the PMC is **ventromedial to** the LC) —
this proximity is a **classic source of confusion** — consumers must
**not** conflate the pontine micturition center with the locus
coeruleus.
**Boundary status (NOT the laterodorsal tegmental nucleus — that is the
CHOLINERGIC neuromodulatory nucleus):** **Boundary case — the pontine
micturition center is NOT the laterodorsal tegmental nucleus (LDT).**
The **laterodorsal tegmental nucleus**
(``.../tegmentum/laterodorsal_tegmental_nucleus/``) is the **cholinergic**
nucleus — the **principal pontine cholinergic source** for the
**thalamus** — it is involved in **REM sleep**, **arousal**, and
**motivation**. The **pontine micturition center** (here) is the
**glutamatergic/GABAergic autonomic control nucleus** — it
**coordinates** the **micturition reflex**. They are **DIFFERENT
STRUCTURES** — different neurotransmitters (glutamate/GABA vs.
acetylcholine), different functional systems (micturition vs.
cholinergic REM-sleep/arousal/motivation), different projection targets
(sacral spinal cord vs. thalamus/basal forebrain). They are
**anatomically adjacent** (both are in the **dorsolateral pontine
tegmentum**) — this proximity is a **classic source of confusion** —
consumers must **not** conflate the pontine micturition center with the
laterodorsal tegmental nucleus.
**Boundary status (NOT the pedunculopontine nucleus — that is the
CHOLINERGIC LOCOMOTION nucleus):** **Boundary case — the pontine
micturition center is NOT the pedunculopontine nucleus (PPN).** The
**pedunculopontine nucleus**
(``.../tegmentum/pedunculopontine_nucleus/``) is the **cholinergic**
(with glutamatergic and GABAergic components) nucleus — the
**mesencephalic locomotor region** (with the **cuneiform nucleus**) — it
is involved in **locomotion**, **REM sleep**, **arousal**, and
**reward** — it is **ventrolateral** at the **pontomesencephalic
junction**. The **pontine micturition center** (here) is the
**glutamatergic/GABAergic autonomic control nucleus** — it
**coordinates** the **micturition reflex** — it is **dorsomedial** in
the **pontine tegmentum**, **near the locus coeruleus**. They are
**DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. acetylcholine), different functional systems
(micturition vs. cholinergic locomotion/REM-sleep/arousal/reward),
different anatomical locations (the PMC is **dorsomedial** near the
fourth ventricle; the PPN is **ventrolateral** at the pontomesencephalic
junction). Consumers must **not** conflate the pontine micturition center
with the pedunculopontine nucleus.
**Boundary status (NOT the nucleus incertus — that is the RELAXIN-3
nucleus):** **Boundary case — the pontine micturition center is NOT the
nucleus incertus.** The **nucleus incertus**
(``.../tegmentum/nucleus_incertus/``) is the **relaxin-3-expressing**
nucleus — it is involved in **stress**, **arousal**, **feeding**, and
**neuroendocrine regulation**. The **pontine micturition center** (here)
is the **glutamatergic/GABAergic autonomic control nucleus**. They are
**DIFFERENT STRUCTURES** — different neurotransmitters (glutamate/GABA
vs. relaxin-3), different functional systems (micturition vs. relaxin-3
stress/arousal/feeding/neuroendocrine), different projection targets
(sacral spinal cord vs. septum/hippocampus/medial prefrontal cortex/
amygdala/hypothalamus). Consumers must **not** conflate the pontine
micturition center with the nucleus incertus.
**Boundary status (NOT the tegmental pontine reticular nucleus — that is
the MOTOR RELAY nucleus):** **Boundary case — the pontine micturition
center is NOT the tegmental pontine reticular nucleus.** The
**tegmental pontine reticular nucleus**
(``.../tegmentum/tegmental_pontine_reticular_nucleus/``) is a **motor
relay** — it **projects** to the **spinal cord** (via the
**reticulospinal tract**) and to the **cerebellum** (via the
**pontocerebellar fibers**) — it is involved in **locomotion**,
**posture**, and **motor pattern generation**. The **pontine
micturition center** (here) is the **glutamatergic/GABAergic autonomic
control nucleus** — it **coordinates** the **micturition reflex**. They
are **DIFFERENT STRUCTURES** — different functional systems
(micturition vs. motor relay), different projection targets (sacral
spinal cord vs. spinal cord/cerebellum). **They are both
glutamatergic/GABAergic** — this shared neurotransmitter profile is a
**classic source of confusion** — consumers must **not** conflate the
pontine micturition center with the tegmental pontine reticular nucleus.
**Boundary status (NOT the parabrachial area — that is a SEPARATE
structural child of the pons):** **Boundary case — the pontine
micturition center is NOT the parabrachial area.** The **parabrachial
area** (``.../pons/parabrachial_area/``) is the **visceral-sensory and
respiratory-relay complex** — it is a **separate structural child of the
pons**, **not** a structural child of the pontine tegmentum, **even
though** it is **anatomically located** in the **pontine tegmentum**.
The **pontine micturition center** (here) is a **glutamatergic/GABAergic
autonomic control nucleus** — a **structural child of the pontine
tegmentum container**. Consumers must **not** conflate the pontine
micturition center with the parabrachial area.
**Boundary status (NOT the superior olivary complex, the cranial nerve
nuclei, the PPRF, or the parvocellular reticular nucleus — those are
SEPARATE structural children of the pons):** **Boundary case — the
pontine micturition center is NOT the superior olivary complex, the
cranial nerve nuclei, the PPRF, or the parvocellular reticular
nucleus.** Those are **separate structural children of the pons** — the
**superior olivary complex** (binaural sound-localization relay), the
**cranial nerve nuclei** (CN V, VI, VII, VIII nuclei), the **PPRF**
(horizontal saccadic burst generator), and the **parvocellular
reticular nucleus** (orofacial premotor and autonomic relay). The
**pontine micturition center** (here) is a **glutamatergic/GABAergic
autonomic control nucleus** — a **structural child of the pontine
tegmentum container**. Consumers must **not** conflate the pontine
micturition center with any of them.
**Boundary status (NOT the pontine nuclei — those are in the BASILAR
pons):** **Boundary case — the pontine micturition center is NOT the
pontine nuclei.** The **pontine nuclei** (``.../pons/pontine_nuclei/``)
are the **cortico-ponto-cerebellar relay** in the **basilar pons** —
the **ventral** portion of the pons. The **pontine micturition center**
(here) is a **glutamatergic/GABAergic autonomic control nucleus** in the
**dorsal pontine tegmentum**. They are **DIFFERENT PONTS
SUB-DIVISIONS** — consumers must **not** conflate the pontine
micturition center with the pontine nuclei.
**Boundary status (NOT the whole tegmentum container — that is the
PARENT):** **Boundary case — the pontine micturition center is NOT the
whole tegmentum container; the tegmentum container is the PARENT.** The
**tegmentum** container (``.../pons/tegmentum/``) is the **dorsal
pontine grey-matter region** — the **tree-wired container** for the
**six neuromodulatory and autonomic nuclei** (locus coeruleus,
laterodorsal tegmental nucleus, nucleus incertus, pedunculopontine
nucleus, pontine micturition center, tegmental pontine reticular
nucleus). The **pontine micturition center** (here) is **one of the six
structural children** of the tegmentum container. Consumers must **not**
conflate the pontine micturition center with the **whole tegmentum**.
**Boundary status (NOT the whole pons — the pons is the GRANDPARENT):**
**Boundary case — the pontine micturition center is NOT the whole pons;
the pons is the GRANDPARENT.** The **pons** (``.../pons/``) is the
**whole metencephalic brainstem segment** — it contains the **basilar
pons**, the **pontine tegmentum**, the **parabrachial area**, the
**superior olivary complex**, the **cranial nerve nuclei**, the
**PPRF**, the **parvocellular reticular nucleus**, the **pontine
nuclei**, and the **six neuromodulatory and autonomic nuclei** of the
tegmentum container. The **pontine micturition center** (here) is **one
of the six neuromodulatory and autonomic nuclei** only. Consumers must
**not** conflate the pontine micturition center with the **whole pons**.
**Boundary status (NOT the fourth ventricle — that is a CSF SPACE):**
**Boundary case — the pontine micturition center is NOT the fourth
ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the **CSF-filled space**
**dorsal to** the pons and **ventral to** the cerebellum. The
**pontine micturition center** (here) is a **grey-matter nucleus** that
sits **near the lateral wall** of the fourth ventricle (in the
**dorsolateral pontine tegmentum**). They are **DIFFERENT STRUCTURES**
— the **fourth ventricle** is a **fluid space**; the **pontine
micturition center** is **neural tissue**. Consumers must **not**
conflate the pontine micturition center with the fourth ventricle.
**Boundary status (NOT the midbrain tegmentum or the medullary
tegmentum — those are DIFFERENT BRAINSTEM LEVELS):** **Boundary case —
the pontine micturition center is NOT the midbrain tegmentum or the
medullary tegmentum.** The **midbrain tegmentum**
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
The **pontine micturition center** (here) is a **specific nucleus** in
the **dorsal portion of the pons**. They are **DIFFERENT BRAINSTEM
LEVELS** — consumers must **not** conflate the pontine micturition
center with the midbrain tegmentum or the medullary tegmentum.
**Boundary status (NOT the sacral spinal cord — that is the DOWNSTREAM
EFFECTOR TARGET):** **Boundary case — the pontine micturition center is
NOT the sacral spinal cord.** The **sacral spinal cord** (the **S2–S4
segments**) is the **downstream effector target** of the pontine
micturition center — it contains the **parasympathetic preganglionic
neurons** of the **bladder** (which **contract** the **detrusor
muscle**) and the **Onuf's nucleus** (which **innervates** the
**external urethral sphincter**). The **pontine micturition center**
(here) is the **pontine autonomic control nucleus** that **projects to**
the **sacral spinal cord**. They are **DIFFERENT STRUCTURES** — the
**PMC** is **pontine** and **upstream**; the **sacral spinal cord** is
**spinal** and **downstream**. Consumers must **not** conflate the
pontine micturition center with the sacral spinal cord.
**Boundary status (NOT the periaqueductal gray — that is the MIDBRAIN
UPSTREAM MICTURITION REGION):** **Boundary case — the pontine
micturition center is NOT the periaqueductal gray (PAG).** The **PAG**
(``.../midbrain/tegmentum/periaqueductal_gray/``) is the **midbrain
micturition region** — it **receives** the **bladder afferents** from
the **solitary nucleus** (via the **sacral spinal cord** and the
**spinothalamic** and **spinoparabrachial** pathways) and **projects**
to the **pontine micturition center** to **initiate** the **micturition
reflex**. The **pontine micturition center** (here) is the **pontine
micturition control center** — it **receives** the **PAG projections**
and **projects** to the **sacral spinal cord** to **coordinate** the
**micturition reflex**. They are **DIFFERENT STRUCTURES** — the **PAG**
is **midbrain** and **upstream**; the **PMC** is **pontine** and
**downstream** of the **PAG**. Consumers must **not** conflate the
pontine micturition center with the periaqueductal gray.
**Boundary status (NOT the hypothalamus — that is the FOREBRAIN
UPSTREAM MICTURITION REGION):** **Boundary case — the pontine
micturition center is NOT the hypothalamus.** The **hypothalamus**
(``.../diencephalon/hypothalamus/``) — especially the **medial preoptic
area** and the **lateral hypothalamic area** — is the **forebrain
micturition region** — it **receives** the **PAG projections** (and
**bladder afferents**) and **projects** to the **pontine micturition
center** to **modulate** the **micturition reflex** (via **descending
forebrain control** of **micturition**). The **pontine micturition
center** (here) is the **pontine micturition control center** — it
**receives** the **hypothalamic** and **PAG** projections and
**projects** to the **sacral spinal cord**. They are **DIFFERENT
STRUCTURES** — the **hypothalamus** is **diencephalic** and
**upstream**; the **PMC** is **pontine** and **downstream** of the
**hypothalamus**. Consumers must **not** conflate the pontine
micturition center with the hypothalamus.
**Boundary status (NOT the prefrontal cortex — that is the CORTICAL
UPSTREAM MICTURITION REGION):** **Boundary case — the pontine
micturition center is NOT the prefrontal cortex.** The **medial
prefrontal cortex** (mPFC) — especially the **anterior cingulate
cortex** and the **medial frontal gyrus** — is the **cortical
micturition region** — it **modulates** the **pontine micturition
center** via the **hypothalamus** and the **periaqueductal gray** to
**enable voluntary control** of **micturition** (the **"social
continence"** of **micturition**). The **pontine micturition center**
(here) is the **pontine micturition control center** — it **receives**
the **cortical** (via the **hypothalamus** and **PAG**) projections and
**projects** to the **sacral spinal cord**. They are **DIFFERENT
STRUCTURES** — the **mPFC** is **cortical** and **upstream**; the
**PMC** is **pontine** and **downstream** of the **mPFC**. Consumers
must **not** conflate the pontine micturition center with the
prefrontal cortex.
**Boundary status (MULTIPLE NEUROCHEMICALLY DISTINCT NEURON
POPULATIONS — CRF-expressing, glutamatergic, and GABAergic):**
**Boundary case — the pontine micturition center is NOT a single
uniform neuron population; it contains MULTIPLE neurochemically
distinct populations.** The **CRF-expressing neurons** — the
**principal population** of the PMC — they **co-express** CRF with
**glutamate** — they are the **principal output** of the PMC to the
**sacral spinal cord**. The **glutamatergic neurons** — the **PMC
neurons that are glutamatergic** — they **release glutamate** at their
**axon terminals** — the **excitatory** neurotransmitter that
**activates** the **sacral parasympathetic preganglionic neurons** (for
**bladder contraction**) and **inhibits** the **Onuf's nucleus** (for
**sphincter relaxation**). The **GABAergic neurons** — the **PMC
neurons that are GABAergic** — they **release GABA** at their **axon
terminals** — the **inhibitory** neurotransmitter that **modulates** the
**PMC's output** and **contributes** to the **coordination** of the
**micturition reflex**. **These populations are prose, not structural
children.** Consumers must **not** treat the pontine micturition center
as a single uniform population — it is a **neurochemically
heterogeneous nucleus** with **distinct** sub-circuits.
**Boundary status (SLEA-FREE — the pontine micturition center is NOT an
extended-amygdala component):** **Boundary case — the pontine
micturition center is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala) and to
the **BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **pontine micturition center** is a
**glutamatergic/GABAergic autonomic control nucleus** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the pontine
micturition center — it is **SLEA-free**.

Overview
--------
The pontine micturition center is the **pontine micturition control
center** of the **pontine tegmentum** — a **neurochemically
heterogeneous** grey-matter nucleus in the **dorsolateral pontine
tegmentum**, **ventromedial to the locus coeruleus** and **dorsolateral
to the superior cerebellar peduncle**, near the **lateral wall of the
fourth ventricle**. It is a **leaf** module under the tegmentum
container, and it is the **neural substrate** of the **micturition
reflex** and the **neural substrate** of the **voluntary control of
micturition**.

**The pontine micturition center is a LEAF, not a container.** It has
**no structural children**. The **CRF-expressing neurons**, the
**glutamatergic neurons**, and the **GABAergic neurons** are **prose
populations**, not structural children.

**The pontine micturition center is a SINGLE module at the tree level.**
The tree does **not** split the PMC into left/right — the module is a
**single, bilateral representation**.

**The pontine micturition center is an AUTONOMIC CONTROL NUCLEUS, NOT a
motor or sensory relay.** It **projects** to the **sacral spinal cord**
to **coordinate** the **micturition reflex** — it does **not** directly
**relay** motor commands or **transmit** sensory information.

**The pontine micturition center is GLUTAMATERGIC AND GABAERGIC, NOT a
monoaminergic, cholinergic, or relaxin-3-expressing nucleus.** It is the
**pontine micturition control center** — a **glutamatergic/GABAergic**
autonomic control nucleus with **CRF co-expression**.

**The pontine micturition center is NOT the locus coeruleus, the
laterodorsal tegmental nucleus, the pedunculopontine nucleus, the nucleus
incertus, or the tegmental pontine reticular nucleus.** Those are the
**other five** neuromodulatory and autonomic nuclei of the **pontine
tegmentum container** — different neurotransmitters, different
functional systems, different projection targets. **The PMC is adjacent
to the LC** — and the **close anatomical proximity** (PMC is
**ventromedial to** the LC) is a **classic source of confusion** —
consumers must **not** conflate the PMC with the LC.

**The pontine micturition center is part of the SUPRASPINAL MICTURITION
CIRCUIT.** The **micturition reflex** is a **complex circuit** that
involves:
*   The **sacral spinal cord** — the **parasympathetic preganglionic
    neurons** (for **bladder contraction**) and **Onuf's nucleus** (for
    **sphincter relaxation**) — the **effector** of the micturition
    reflex.
*   The **periaqueductal gray (PAG)** (midbrain) — the **micturition
    region** that **receives** bladder afferents and **projects** to the
    **PMC** to **initiate** micturition.
*   The **pontine micturition center (PMC)** (pons) — the **pontine
    micturition control center** that **coordinates** the **bladder
    contraction** and **sphincter relaxation** via its **projections** to
    the **sacral spinal cord**.
*   The **hypothalamus** (diencephalon) — the **forebrain micturition
    region** that **modulates** the **PMC** via the **PAG**.
*   The **medial prefrontal cortex** (cortex) — the **cortical
    micturition region** that **enables voluntary control** of
    micturition (the **"social continence"** of micturition) via the
    **hypothalamus** and the **PAG**.

**The pontine micturition center is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The pontine micturition center contains **multiple neurochemically
distinct neuron populations** — documented as **prose**, not as
structural children:

*   **CRF-expressing neurons** — the **principal population** of the PMC
    — they **co-express** CRF with **glutamate**. They **project** to
    the **sacral spinal cord** — the **parasympathetic preganglionic
    neurons** of the **bladder** (which **contract** the **detrusor
    muscle**) and the **Onuf's nucleus** (which **innervates** the
    **external urethral sphincter** — they **inhibit** the
    **sphincter** to **relax** it). They are the **principal output**
    of the PMC and the **neural substrate** of the **micturition
    reflex**. **CRF-expressing micturition control is the functional
    system** subserved primarily by the CRF-expressing neurons.

*   **Glutamatergic neurons** — the **PMC neurons that are
    glutamatergic** (including the **CRF-expressing neurons**) — they
    **release glutamate** at their **axon terminals** — the
    **excitatory** neurotransmitter that **activates** the **sacral
    parasympathetic preganglionic neurons** (for **bladder
    contraction**) and **inhibits** the **Onuf's nucleus** (for
    **sphincter relaxation**). **Glutamatergic micturition control is
    the functional system** subserved primarily by the glutamatergic
    neurons.

*   **GABAergic neurons** — the **PMC neurons that are GABAergic** —
    they **release GABA** at their **axon terminals** — the
    **inhibitory** neurotransmitter that **modulates** the **PMC's
    output** and **contributes** to the **coordination** of the
    **micturition reflex**. **GABAergic micturition modulation is the
    functional system** subserved primarily by the GABAergic neurons.

**These populations are prose, not structural children.** The tree wires
the **pontine micturition center** as a **single leaf** under the
tegmentum container — the **CRF-expressing neurons**, the
**glutamatergic neurons**, and the **GABAergic neurons** are **prose**,
not structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Pontine Micturition Center / Locus Coeruleus Boundary
---------------------------------------------------------
This is the **sibling** boundary — **micturition vs. noradrenergic
arousal/attention/stress**:

*   **Pontine micturition center** (this module) — the
    **glutamatergic/GABAergic** autonomic control nucleus — it
    **coordinates** the **micturition reflex**.

*   **Locus coeruleus** (``.../tegmentum/locus_coeruleus/``) — the
    **noradrenergic** nucleus — the **principal source of
    norepinephrine** in the brain — it is involved in **arousal**,
    **attention**, **stress**, **pain modulation**, and **memory
    consolidation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. noradrenaline), different functional systems
(micturition vs. noradrenergic arousal/attention/stress/pain/memory),
different projection targets (sacral spinal cord vs. diffuse
noradrenergic). They are **anatomically adjacent** (the PMC is
**ventromedial to** the LC) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the pontine micturition
center with the locus coeruleus.

The Pontine Micturition Center / Laterodorsal Tegmental Nucleus Boundary
-----------------------------------------------------------------------
This is the **sibling** boundary — **micturition vs. cholinergic
REM-sleep/arousal**:

*   **Pontine micturition center** (this module) — the
    **glutamatergic/GABAergic** autonomic control nucleus — it
    **coordinates** the **micturition reflex**.

*   **Laterodorsal tegmental nucleus**
    (``.../tegmentum/laterodorsal_tegmental_nucleus/``) — the
    **cholinergic** nucleus — the **principal pontine cholinergic
    source** for the **thalamus** — it is involved in **REM sleep**,
    **arousal**, and **motivation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. acetylcholine), different functional systems
(micturition vs. cholinergic REM-sleep/arousal/motivation), different
projection targets (sacral spinal cord vs. thalamus/basal forebrain).
They are **anatomically adjacent** (both are in the **dorsolateral
pontine tegmentum**) — this proximity is a **classic source of
confusion** — consumers must **not** conflate the pontine micturition
center with the laterodorsal tegmental nucleus.

The Pontine Micturition Center / Pedunculopontine Nucleus Boundary
------------------------------------------------------------------
This is the **sibling** boundary — **micturition vs. cholinergic
locomotion/REM/reward**:

*   **Pontine micturition center** (this module) — the
    **glutamatergic/GABAergic** autonomic control nucleus — it
    **coordinates** the **micturition reflex** — **dorsomedial** in the
    pontine tegmentum, **near the locus coeruleus**.

*   **Pedunculopontine nucleus**
    (``.../tegmentum/pedunculopontine_nucleus/``) — the **cholinergic**
    (with glutamatergic and GABAergic components) nucleus — the
    **mesencephalic locomotor region** — it is involved in
    **locomotion**, **REM sleep**, **arousal**, and **reward** —
    **ventrolateral** at the **pontomesencephalic junction**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. acetylcholine), different functional systems
(micturition vs. cholinergic locomotion/REM-sleep/arousal/reward),
different anatomical locations (the PMC is **dorsomedial** near the
fourth ventricle; the PPN is **ventrolateral** at the pontomesencephalic
junction). Consumers must **not** conflate the pontine micturition
center with the pedunculopontine nucleus.

The Pontine Micturition Center / Nucleus Incertus Boundary
----------------------------------------------------------
This is the **sibling** boundary — **micturition vs. relaxin-3
stress/arousal/feeding**:

*   **Pontine micturition center** (this module) — the
    **glutamatergic/GABAergic** autonomic control nucleus.

*   **Nucleus incertus** (``.../tegmentum/nucleus_incertus/``) — the
    **relaxin-3-expressing** nucleus — it is involved in **stress**,
    **arousal**, **feeding**, and **neuroendocrine regulation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(glutamate/GABA vs. relaxin-3), different functional systems
(micturition vs. relaxin-3 stress/arousal/feeding/neuroendocrine),
different projection targets (sacral spinal cord vs.
septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus).
Consumers must **not** conflate the pontine micturition center with the
nucleus incertus.

The Pontine Micturition Center / Tegmental Pontine Reticular Nucleus Boundary
-----------------------------------------------------------------------------
This is the **sibling** boundary — **micturition vs. motor relay**:

*   **Pontine micturition center** (this module) — the
    **glutamatergic/GABAergic** autonomic control nucleus — it
    **coordinates** the **micturition reflex**.

*   **Tegmental pontine reticular nucleus**
    (``.../tegmentum/tegmental_pontine_reticular_nucleus/``) — the
    **motor relay** — it **projects** to the **spinal cord** (via the
    **reticulospinal tract**) and to the **cerebellum** (via the
    **pontocerebellar fibers**) — it is involved in **locomotion**,
    **posture**, and **motor pattern generation**.

**They are DIFFERENT STRUCTURES** — different functional systems
(micturition vs. motor relay), different projection targets (sacral
spinal cord vs. spinal cord/cerebellum). **They are both
glutamatergic/GABAergic** — this shared neurotransmitter profile is a
**classic source of confusion** — consumers must **not** conflate the
pontine micturition center with the tegmental pontine reticular
nucleus.

The Pontine Micturition Center / Parabrachial Area Boundary
-----------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pontine micturition center** (this module) — a
    **glutamatergic/GABAergic autonomic control nucleus** — a
    **structural child of the pontine tegmentum container**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex** — a **separate
    structural child of the pons**.

**They are DIFFERENT STRUCTURES** — the parabrachial area is **not** a
structural child of the pontine tegmentum (in the tree), even though it
is **anatomically located** in the pontine tegmentum. Consumers must
**not** conflate the pontine micturition center with the parabrachial
area.

The Pontine Micturition Center / Superior Olivary Complex, Cranial Nerve Nuclei, PPRF, and Parvocellular Reticular Nucleus Boundary
--------------------------------------------------------------------------------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pontine micturition center** (this module) — a
    **glutamatergic/GABAergic autonomic control nucleus** — a
    **structural child of the pontine tegmentum container**.

*   **Superior olivary complex** (``.../pons/superior_olivary_complex/``),
    **cranial nerve nuclei** (``.../pons/cranial_nerve_nuclei/``),
    **PPRF** (``.../pons/paramedian_pontine_reticular_formation/``),
    **parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``) — **separate
    structural children of the pons**.

**They are DIFFERENT STRUCTURES** — those four structures are **not**
structural children of the pontine tegmentum (in the tree), even though
they are **anatomically located** in the pontine tegmentum. Consumers
must **not** conflate the pontine micturition center with any of them.

The Pontine Micturition Center / Pontine Nuclei Boundary
--------------------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Pontine micturition center** (this module) — a
    **glutamatergic/GABAergic autonomic control nucleus** in the
    **dorsolateral pontine tegmentum**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not**
conflate the pontine micturition center with the pontine nuclei.

The Pontine Micturition Center / Whole Tegmentum Container Boundary
-------------------------------------------------------------------
This is the **sub-nucleus vs. parent** boundary:

*   **Pontine micturition center** (this module) — one of the **six
    neuromodulatory and autonomic nuclei** of the pontine tegmentum.

*   **Tegmentum container** (``.../pons/tegmentum/``) — the **dorsal
    pontine grey-matter region** — the **tree-wired container** for the
    **six neuromodulatory and autonomic nuclei**.

**The pontine micturition center is a child of the tegmentum container.**
Consumers must **not** conflate the pontine micturition center with the
**whole tegmentum**.

The Pontine Micturition Center / Whole Pons Boundary
----------------------------------------------------
This is the **nucleus vs. grandparent** boundary:

*   **Pontine micturition center** (this module) — one of the **six
    neuromodulatory and autonomic nuclei** of the pontine tegmentum.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**.

**The pontine micturition center is a grandchild of the pons** (via the
tegmentum container). Consumers must **not** conflate the pontine
micturition center with the **whole pons**.

The Pontine Micturition Center / Fourth Ventricle Boundary
----------------------------------------------------------
This is the **neural tissue vs. CSF space** boundary:

*   **Pontine micturition center** (this module) — a **grey-matter
    nucleus** near the **lateral wall** of the fourth ventricle.

*   **Fourth ventricle** (``.../metencephalon/fourth_ventricle/``) — the
    **CSF-filled space** **dorsal to** the pons.

**They are DIFFERENT STRUCTURES** — the **fourth ventricle** is a
**fluid space**; the **pontine micturition center** is **neural tissue**.
Consumers must **not** conflate the pontine micturition center with the
fourth ventricle.

The Pontine Micturition Center / Midbrain Tegmentum and Medullary Tegmentum Boundary
------------------------------------------------------------------------------------
This is the **pons vs. midbrain/medulla** boundary:

*   **Pontine micturition center** (this module) — a **specific nucleus**
    in the **dorsal portion of the pons**.

*   **Midbrain tegmentum** (``.../midbrain/tegmentum/``) and **medullary
    tegmentum** — the **dorsal portions** of the **midbrain** and the
    **medulla oblongata**.

**They are DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate
the pontine micturition center with the midbrain tegmentum or the
medullary tegmentum.

The Pontine Micturition Center / Sacral Spinal Cord Boundary
------------------------------------------------------------
This is the **pontine control vs. spinal effector** boundary:

*   **Pontine micturition center** (this module) — the **pontine
    micturition control center** — it **coordinates** the **micturition
    reflex** via its **projections** to the **sacral spinal cord**.

*   **Sacral spinal cord** — the **downstream effector target** — it
    contains the **parasympathetic preganglionic neurons** of the
    **bladder** (which **contract** the **detrusor muscle**) and the
    **Onuf's nucleus** (which **innervates** the **external urethral
    sphincter**).

**They are DIFFERENT STRUCTURES** — the **PMC** is **pontine** and
**upstream**; the **sacral spinal cord** is **spinal** and
**downstream**. Consumers must **not** conflate the pontine micturition
center with the sacral spinal cord.

The Pontine Micturition Center / Periaqueductal Gray Boundary
-------------------------------------------------------------
This is the **pontine control vs. midbrain upstream micturition region**
boundary:

*   **Pontine micturition center** (this module) — the **pontine
    micturition control center** — it **receives** the **PAG
    projections** and **projects** to the **sacral spinal cord**.

*   **Periaqueductal gray (PAG)**
    (``.../midbrain/tegmentum/periaqueductal_gray/``) — the **midbrain
    micturition region** — it **receives** the **bladder afferents**
    (from the **solitary nucleus**) and **projects** to the **PMC** to
    **initiate** the **micturition reflex**.

**They are DIFFERENT STRUCTURES** — the **PAG** is **midbrain** and
**upstream**; the **PMC** is **pontine** and **downstream** of the
**PAG**. Consumers must **not** conflate the pontine micturition center
with the periaqueductal gray.

The Pontine Micturition Center / Hypothalamus Boundary
------------------------------------------------------
This is the **pontine control vs. forebrain upstream micturition
region** boundary:

*   **Pontine micturition center** (this module) — the **pontine
    micturition control center**.

*   **Hypothalamus** (``.../diencephalon/hypothalamus/``) — the
    **forebrain micturition region** — it **modulates** the **PMC** via
    the **PAG** (and **bladder afferents**) to **modulate** the
    **micturition reflex**.

**They are DIFFERENT STRUCTURES** — the **hypothalamus** is
**diencephalic** and **upstream**; the **PMC** is **pontine** and
**downstream** of the **hypothalamus**. Consumers must **not** conflate
the pontine micturition center with the hypothalamus.

The Pontine Micturition Center / Prefrontal Cortex Boundary
-----------------------------------------------------------
This is the **pontine control vs. cortical upstream micturition
region** boundary:

*   **Pontine micturition center** (this module) — the **pontine
    micturition control center**.

*   **Medial prefrontal cortex** (mPFC) — the **cortical micturition
    region** — it **enables voluntary control** of **micturition** (the
    **"social continence"** of micturition) via the **hypothalamus** and
    the **PAG**.

**They are DIFFERENT STRUCTURES** — the **mPFC** is **cortical** and
**upstream**; the **PMC** is **pontine** and **downstream** of the
**mPFC**. Consumers must **not** conflate the pontine micturition center
with the prefrontal cortex.

The Pontine Micturition Center / SLEA Boundary
----------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Pontine micturition center** (this module) — **SLEA-FREE**. It is
    **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The pontine micturition center is NOT part of the SLEA continuum.** It
is a **glutamatergic/GABAergic autonomic control nucleus**, and it
carries **no SLEA warning**. Consumers must **not** import the SLEA
warning into the pontine micturition center.

Function in the Human Brain
---------------------------
The pontine micturition center's functions are **the pontine control of
micturition** — **NOT a single unified function**:

*   **Micturition Reflex Coordination (CRF-expressing and Glutamatergic
    Neurons):** The **CRF-expressing** and **glutamatergic** neurons of
    the PMC **project** to the **sacral spinal cord** — they
    **activate** the **parasympathetic preganglionic neurons** of the
    **bladder** (which **contract** the **detrusor muscle**) and
    **inhibit** the **Onuf's nucleus** (which **innervates** the
    **external urethral sphincter** — they **relax** the **sphincter**).
    **This coordinated activation** — **bladder contraction** and
    **sphincter relaxation** — is the **neural substrate** of the
    **micturition reflex** — the **PMC** is the **pontine micturition
    control center** that **coordinates** the **micturition reflex**.

*   **Voluntary Control of Micturition (Supraspinal Modulation):** The
    **PMC** **receives** the **supraspinal inputs** from the
    **periaqueductal gray** (which **receives** the **bladder
    afferents** from the **solitary nucleus** and the **sacral spinal
    cord**), the **hypothalamus** (which **receives** the **cortical
    inputs** from the **medial prefrontal cortex**), and the **medial
    prefrontal cortex** (which **enables voluntary control** of
    micturition — the **"social continence"** of micturition). **The
    PMC** **integrates** these **supraspinal inputs** to **modulate**
    the **micturition reflex** — **initiating** micturition when
    **appropriate** and **suppressing** it when **inappropriate**.

*   **Micturition Suppression (GABAergic Neurons):** The **GABAergic**
    neurons of the PMC (and the **GABAergic inputs** from the **PAG**
    and the **hypothalamus**) **inhibit** the **micturition reflex** —
    they **suppress** the **bladder contraction** and **maintain** the
    **sphincter tone** until **micturition is appropriate**. **This
    "micturition suppression"** function is the **neural substrate** of
    the **continence** of micturition — the **PMC** is the **pontine
    micturition control center** that **suppresses** micturition when
    **inappropriate**.

*   **Bladder Sensation (PAG and Thalamic Projections):** The **PMC**
    (and the **PAG**) **receives** the **bladder afferents** from the
    **sacral spinal cord** — the **bladder distension** signals that
    **underlie** the **conscious sensation of bladder fullness** — and
    **projects** them to the **thalamus** and the **cortex** (via the
    **spinothalamic** and **spinoparabrachial** pathways). **This
    "bladder sensation"** function is the **neural substrate** of the
    **conscious perception of bladder fullness** — the **PMC** (and the
    **PAG**) **relays** the **bladder afferents** to the **forebrain**.

*   **NOT a neural processor in the classical sense.** The PMC is an
    **autonomic control nucleus** — it **receives** afferent inputs
    (from the **PAG**, the **hypothalamus**, the **medial prefrontal
    cortex**, and the **sacral spinal cord**) and **projects** to the
    **sacral spinal cord** (for the **micturition reflex**). The
    **processing** of micturition happens in a **distributed** manner
    across the **PMC**, the **PAG**, the **hypothalamus**, the **medial
    prefrontal cortex**, and the **sacral spinal cord**.

**The unifying theme:** the pontine micturition center is the **pontine
micturition control center** — the **neural substrate** of the
**micturition reflex** and the **neural substrate** of the **voluntary
control of micturition**. It is **CRF-expressing** (with
**glutamatergic** and **GABAergic** co-transmission), **SLEA-free**, and
**NOT the locus coeruleus** — the **LC** is the **noradrenergic**
neuromodulatory nucleus. The **PMC** is the **glutamatergic/GABAergic**
autonomic control nucleus that **coordinates** the **micturition
reflex**.

Associated Disorders
--------------------
The pontine micturition center has **no named "pontine micturition
center syndrome"** — its clinical associations are **function-specific**:

*   **Neurogenic Bladder — PMC Involvement:** **Neurogenic bladder** is a
    **dysfunction** of the **bladder** caused by **neurological
    disease** — it can be caused by **PMC dysfunction** (e.g., **pontine
    stroke**, **multiple sclerosis**, **Parkinson's disease**,
    **dementia**, **spinal cord injury** above the **sacral level**).
    The **most common PMC-related pattern** is **detrusor-sphincter
    dyssynergia** — the **bladder contraction** (detrusor) is
    **dyssynergic** with the **sphincter relaxation** — because the
    **PMC's coordinated output** is **disrupted** — leading to
    **urinary retention**, **incontinence**, and **recurrent urinary
    tract infections**.

*   **Urinary Incontinence — PMC Involvement:** **Urinary
    incontinence** — especially **urge incontinence** — is a **common
    symptom** of **PMC dysfunction** — the **PMC** **fails** to
    **suppress** the **micturition reflex** when **inappropriate**,
    leading to **involuntary bladder contractions** and **urine
    leakage**. This is particularly **common** in **older adults** with
    **pontine** or **forebrain** **lesions**.

*   **Urinary Retention — PMC Involvement:** **Urinary retention** is a
    **failure** to **empty** the **bladder** — it can be caused by
    **PMC dysfunction** — the **PMC** **fails** to **initiate** the
    **micturition reflex** when **appropriate**, leading to **bladder
    overdistension** and **urine retention**. This is particularly
    **common** in **pontine** or **sacral spinal cord** **lesions**.

*   **Multiple Sclerosis — PMC Involvement:** **Multiple sclerosis** can
    affect the **pontine micturition center** (as a **brainstem
    demyelinating lesion**), contributing to **neurogenic bladder**
    (detrusor-sphincter dyssynergia, urge incontinence, urinary
    retention).

*   **Parkinson's Disease — PMC Involvement:** **Parkinson's disease** is
    associated with **lower urinary tract symptoms** (urinary urgency,
    frequency, and urge incontinence) — the **PMC** is **involved** in
    these symptoms, and **dopaminergic** **medications** may
    **exacerbate** or **improve** them depending on the **dose** and the
    **specific dopaminergic** pathway affected.

*   **Pontine Stroke — PMC Involvement:** A **pontine stroke** (e.g.,
    **basilar artery** perforator territory) involving the **PMC**
    causes **neurogenic bladder** — **detrusor-sphincter dyssynergia**,
    **urge incontinence**, or **urinary retention** — often accompanied
    by **other pontine signs** (**hemiparesis**, **facial palsy**,
    **abducens palsy**, **cerebellar ataxia**).

*   **Normal Pressure Hydrocephalus (NPH) — PMC Involvement:** **Normal
    pressure hydrocephalus** is a **triad** of **gait disturbance**,
    **cognitive impairment**, and **urinary incontinence** — the
    **PMC** may be **involved** in the **urinary incontinence**
    component — the **ventricular enlargement** and the **periventricular
    white matter changes** may **disrupt** the **PMC's** **supraspinal
    inputs** (from the **medial prefrontal cortex** and the
    **hypothalamus**), leading to **urinary incontinence**.

*   **No Named "PMC Syndrome":** The pontine micturition center is a
    **neurochemically heterogeneous autonomic control nucleus** — it has
    **no named clinical syndrome** of its own. Its clinical relevance is
    **micturition-specific** — **neurogenic bladder**, **urinary
    incontinence**, **urinary retention**, **multiple sclerosis**,
    **Parkinson's disease**, **pontine stroke**, and **normal pressure
    hydrocephalus** are all **PMC-involved** conditions.

**What is NOT here:** The pontine micturition center is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **acoustic neuroma** (CN VIII nerve), **vestibular neuritis**
(vestibular nerve), **labyrinthitis** (inner ear), **auditory neuropathy
spectrum disorder** (cochlear nerve or hair cell), **Wallenberg
syndrome** (lateral medulla), **internuclear ophthalmoplegia** (MLF),
**horizontal gaze palsy** (PPRF or abducens nucleus), or **REM sleep
behavior disorder** (REM-sleep nuclei). Its clinical relevance is
**micturition-specific**, via the **micturition reflex** it subserves.
**No named PMC syndrome exists.**

Lateralization Notes
--------------------
This is the **single** pontine micturition center module. The PMC is
**bilateral in real anatomy** (left PMC and right PMC), but the tree
wires it as a **single module** — and the module carries **NO warning at
the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **pontine_micturition_center** module (here) is a **single module**
    that represents the **bilateral PMC** (the left PMC and the right
    PMC). The tree does **not** split them into left/right. Consumers
    must **not** assume a left/right split exists at the tree level —
    the module is a **single, bilateral representation**.

*   **Bilateral Projections to the Sacral Spinal Cord (Structural Fact,
    NOT a Lateralization Warning):** The **PMC** **projects bilaterally**
    to the **sacral spinal cord** (both left and right sacral
    parasympathetic preganglionic neurons and Onuf's nucleus) — it
    **coordinates** the **micturition reflex** bilaterally. **This
    bilateral projection** is a **structural fact** of the **micturition
    control system** — it is **not** a functional lateralization. It is
    the **neural substrate** of the **bilateral coordination** of
    **bladder contraction** and **sphincter relaxation**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The PMC is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the PMC.

*   **NO Amygdala-Lateralization Warning of their own (the PMC is
    AUTONOMIC CONTROL, not the fear-output):** The **right-amygdala fear
    association** belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The PMC is a **glutamatergic/GABAergic autonomic
    control nucleus** — consumers must **not** conflate it with the
    **amygdala** or with the **fear circuit**.

**A consumer that sees "pontine_micturition_center" must understand that
the module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **bilateral projections** are
**structural facts**, not lateralizations. The PMC is a **strict-single
module with NO warning at the module level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** PMC as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/locus_coeruleus/``,
    ``.../tegmentum/laterodorsal_tegmental_nucleus/``,
    ``.../tegmentum/nucleus_incertus/``,
    ``.../tegmentum/pedunculopontine_nucleus/``,
    ``.../tegmentum/tegmental_pontine_reticular_nucleus/``,
    ``.../pons/parabrachial_area/``,
    ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../pons/pontine_nuclei/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../diencephalon/hypothalamus/``,
    ``.../cortex/``, or any other container. The PMC's relationships to
    the **locus coeruleus**, the **laterodorsal tegmental nucleus**, the
    **pedunculopontine nucleus**, the **nucleus incertus**, the
    **tegmental pontine reticular nucleus**, the **parabrachial area**,
    the **superior olivary complex**, the **cranial nerve nuclei**, the
    **PPRF**, the **parvocellular reticular nucleus**, the **pontine
    nuclei**, the **fourth ventricle**, the **midbrain tegmentum**, the
    **medullary tegmentum**, the **sacral spinal cord**, the
    **periaqueductal gray**, the **hypothalamus**, the **medial
    prefrontal cortex**, the **whole tegmentum container**, the **whole
    pons**, and the **SLEA continuum** are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **CRF-expressing
    neurons**, the **glutamatergic neurons**, and the **GABAergic
    neurons** are documented as **prose**, not as sub-modules. Consumers
    must not assume any exist as children; resolve neuron-population-
    level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The **PMC**
    is a **single module** that represents the **bilateral PMC** — the
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **AUTONOMIC CONTROL NUCLEUS — NOT a motor or sensory relay.** The
    **PMC** is an **autonomic control nucleus** — **projecting to** the
    **sacral spinal cord** to **coordinate** the **micturition reflex**.
    Consumers must **not** conflate the PMC with a motor or sensory
    relay.
*   **GLUTAMATERGIC AND GABAERGIC — NOT a monoaminergic, cholinergic, or
    relaxin-3-expressing nucleus.** The **PMC** is a
    **glutamatergic/GABAergic** autonomic control nucleus with **CRF
    co-expression**. Consumers must **not** conflate the PMC with the
    **monoaminergic** nuclei (LC, substantia nigra, VTA, raphe nuclei),
    the **cholinergic** nuclei (LDT, PPN), the **relaxin-3** nucleus
    (nucleus incertus), or the **motor relay** nucleus (tegmental
    pontine reticular nucleus).
*   **NOT the locus coeruleus — that is the NORADRENERGIC neuromodulatory
    nucleus.** The **LC** is **anatomically adjacent** to the PMC
    (ventromedial) — consumers must **not** conflate the PMC with the
    LC.
*   **NOT the laterodorsal tegmental nucleus — that is the CHOLINERGIC
    neuromodulatory nucleus.** Consumers must **not** conflate the PMC
    with the LDT.
*   **NOT the pedunculopontine nucleus — that is the CHOLINERGIC
    LOCOMOTION nucleus.** Consumers must **not** conflate the PMC with
    the PPN.
*   **NOT the nucleus incertus or the tegmental pontine reticular
    nucleus — those are DIFFERENT neuromodulatory and motor nuclei.**
    Consumers must **not** conflate the PMC with either of them.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, the PPRF, or the parvocellular reticular
    nucleus — those are SEPARATE structural children of the pons.**
    Consumers must **not** conflate the PMC with any of them.
*   **NOT the pontine nuclei — those are in the BASILAR pons.**
    Consumers must **not** conflate the PMC with the pontine nuclei.
*   **NOT the whole tegmentum container — that is the PARENT.**
    Consumers must **not** conflate the PMC with the whole tegmentum.
*   **NOT the whole pons — that is the GRANDPARENT.** Consumers must
    **not** conflate the PMC with the whole pons.
*   **NOT the fourth ventricle — that is a CSF SPACE.** Consumers must
    **not** conflate the PMC with the fourth ventricle.
*   **NOT the midbrain tegmentum or the medullary tegmentum — those are
    DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate the PMC
    with the midbrain tegmentum or the medullary tegmentum.
*   **NOT the sacral spinal cord — that is the DOWNSTREAM EFFECTOR
    TARGET.** Consumers must **not** conflate the PMC with the sacral
    spinal cord.
*   **NOT the periaqueductal gray — that is the MIDBRAIN UPSTREAM
    MICTURITION REGION.** Consumers must **not** conflate the PMC with
    the PAG.
*   **NOT the hypothalamus or the prefrontal cortex — those are FOREBRAIN
    and CORTICAL UPSTREAM MICTURITION REGIONS.** Consumers must **not**
    conflate the PMC with the hypothalamus or the prefrontal cortex.
*   **MULTIPLE NEUROCHEMICALLY DISTINCT NEURON POPULATIONS —
    CRF-expressing, glutamatergic, and GABAergic.** The
    **CRF-expressing neurons** (the principal population), the
    **glutamatergic neurons**, and the **GABAergic neurons** are
    **prose**, not structural children. Consumers must **not** treat the
    PMC as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The PMC is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the PMC is AUTONOMIC CONTROL.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **PMC** is a **glutamatergic/GABAergic autonomic
    control nucleus** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The PMC is a local leaf under the
    tegmentum container, not a cross-listed leaf.
*   **No nested cross-listing.** The PMC has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum import pontine_micturition_center

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.tegmentum."
        "pontine_micturition_center"
    )

**Do not** assume the PMC is a **container**. It is a **leaf** — the
**CRF-expressing neurons**, the **glutamatergic neurons**, and the
**GABAergic neurons** are **prose**, not structural children.

**Do not** assume the PMC is **bilateralized at the tree level**. The PMC
is **bilateral in real anatomy**, but the tree wires it as a **single
module** — there is **no left/right split at the module level**.

**Do not** assume the PMC is a **purely motor or sensory relay**. The
**PMC** is an **autonomic control nucleus** — it **coordinates** the
**micturition reflex** via its **projections** to the **sacral spinal
cord**.

**Do not** assume the PMC is the **locus coeruleus**. The **locus
coeruleus** is the **noradrenergic** nucleus. The **PMC** is the
**glutamatergic/GABAergic** autonomic control nucleus. They are
**anatomically adjacent** (the PMC is ventromedial to the LC) — but
they are **different structures**.

**Do not** assume the PMC is the **laterodorsal tegmental nucleus**, the
**pedunculopontine nucleus**, the **nucleus incertus**, or the
**tegmental pontine reticular nucleus**. Those are **different
structures** — the **LDT** and **PPN** are **cholinergic**; the
**nucleus incertus** is **relaxin-3-expressing**; the **tegmental
pontine reticular nucleus** is a **motor relay**.

**Do not** assume the PMC is the **parabrachial area**, the **superior
olivary complex**, the **cranial nerve nuclei**, the **PPRF**, or the
**parvocellular reticular nucleus**. Those are **separate structural
children of the pons** — even though they are anatomically located in
the pontine tegmentum.

**Do not** assume the PMC is the **pontine nuclei**. The **pontine
nuclei** are in the **basilar pons** — the PMC is in the **dorsolateral
pontine tegmentum**.

**Do not** assume the PMC is the **whole tegmentum** or the **whole
pons**. The **tegmentum** is the **parent**; the **pons** is the
**grandparent**.

**Do not** assume the PMC is the **fourth ventricle**. The **fourth
ventricle** is a **CSF space**; the PMC is **neural tissue**.

**Do not** assume the PMC is the **midbrain tegmentum** or the **medullary
tegmentum**. Those are **different brainstem levels**.

**Do not** assume the PMC is the **sacral spinal cord**, the
**periaqueductal gray**, the **hypothalamus**, or the **prefrontal
cortex**. Those are **downstream effector** or **upstream regulatory**
structures — the **PMC** is the **pontine micturition control center**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the PMC. **The PMC is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the PMC's (empty) children (recommended consumer pattern)::

    PONTINE_MICTURITION_CENTER_CHILDREN = ()
    # The PMC is a leaf. The CRF-expressing neurons, the glutamatergic
    # neurons, and the GABAergic neurons are prose, not modules.

Reaching the locus coeruleus (recommended consumer pattern — the
noradrenergic sibling)::

    # The locus coeruleus is the NORADRENERGIC sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The LC is noradrenergic; the PMC is glutamatergic/GABAergic. They
    # are ANATOMICALLY ADJACENT (the PMC is ventromedial to the LC) but
    # FUNCTIONALLY DISTINCT.

Reaching the laterodorsal tegmental nucleus (recommended consumer
pattern — the cholinergic sibling)::

    # The laterodorsal tegmental nucleus is the CHOLINERGIC sibling under
    # the tegmentum container:
    #
    #   .../pons/tegmentum/laterodorsal_tegmental_nucleus/
    #
    # The LDT is cholinergic; the PMC is glutamatergic/GABAergic. They
    # are DIFFERENT STRUCTURES.

Reaching the pedunculopontine nucleus (recommended consumer pattern — the
cholinergic locomotion sibling)::

    # The pedunculopontine nucleus is the CHOLINERGIC LOCOMOTION sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pedunculopontine_nucleus/
    #
    # The PPN is cholinergic; the PMC is glutamatergic/GABAergic. They
    # are DIFFERENT STRUCTURES with DIFFERENT functional systems.

Reaching the nucleus incertus (recommended consumer pattern — the
relaxin-3 sibling)::

    # The nucleus incertus is the RELAXIN-3-EXPRESSING sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/nucleus_incertus/
    #
    # The nucleus incertus is relaxin-3-expressing; the PMC is
    # glutamatergic/GABAergic. They are DIFFERENT STRUCTURES.

Reaching the tegmental pontine reticular nucleus (recommended consumer
pattern — the motor relay sibling)::

    # The tegmental pontine reticular nucleus is the MOTOR RELAY sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/tegmental_pontine_reticular_nucleus/
    #
    # The tegmental pontine reticular nucleus is a motor relay; the PMC
    # is an autonomic control nucleus. They are BOTH glutamatergic/
    # GABAergic — but DIFFERENT STRUCTURES with DIFFERENT functional
    # systems.

Reaching the parabrachial area (recommended consumer pattern — a
SEPARATE pons child)::

    # The parabrachial area is a SEPARATE STRUCTURAL CHILD of the pons:
    #
    #   .../pons/parabrachial_area/
    #
    # The parabrachial area is the visceral-sensory and respiratory-relay
    # complex; the PMC is a glutamatergic/GABAergic autonomic control
    # nucleus.

Reaching the whole tegmentum container (recommended consumer pattern —
the PARENT)::

    # The tegmentum container is the DORSAL PONTINE GREY-MATTER REGION
    # that CONTAINS the PMC as one of its six structural children:
    #
    #   .../pons/tegmentum/
    #
    # The PMC is a CHILD of the tegmentum container.

Reaching the whole pons (recommended consumer pattern — the
GRANDPARENT)::

    # The pons is the WHOLE METENCEPHALIC BRAINSTEM SEGMENT that CONTAINS
    # the tegmentum container:
    #
    #   .../pons/
    #
    # The PMC is a GRANDCHILD of the pons.

Reaching the sacral spinal cord (recommended consumer pattern — the
DOWNSTREAM EFFECTOR TARGET)::

    # The sacral spinal cord is the DOWNSTREAM EFFECTOR TARGET of the
    # PMC:
    #
    #   .../spinal_cord/gray_matter/left/sacral_segments/  (and right/)
    #
    # The PMC PROJECTS TO the sacral spinal cord to coordinate the
    # micturition reflex.

Reaching the periaqueductal gray (recommended consumer pattern — the
MIDBRAIN UPSTREAM MICTURITION REGION)::

    # The periaqueductal gray (PAG) is the MIDBRAIN UPSTREAM MICTURITION
    # REGION that PROJECTS TO the PMC:
    #
    #   .../midbrain/tegmentum/periaqueductal_gray/
    #
    # The PAG is UPSTREAM of the PMC; the PMC is DOWNSTREAM of the PAG.

Bilateral iteration (recommended consumer pattern)::

    # The PMC is a SINGLE module (not bilateralized at the tree level).
    # The module represents the BILATERAL PMC.
    pmc_path = (
        "hindbrain.metencephalon.pons.tegmentum.pontine_micturition_center"
    )
    # resolve pmc_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The PMC's neuron populations are prose, not modules:
    #   CRF-expressing neurons -> the principal population of the PMC;
    #       co-express CRF with glutamate; project to the sacral spinal
    #       cord (parasympathetic preganglionic neurons of the bladder;
    #       Onuf's nucleus of the external urethral sphincter); the
    #       principal output of the PMC and the neural substrate of the
    #       micturition reflex
    #   glutamatergic neurons -> release glutamate at their axon
    #       terminals; activate the sacral parasympathetic preganglionic
    #       neurons (for bladder contraction) and inhibit the Onuf's
    #       nucleus (for sphincter relaxation)
    #   GABAergic neurons -> release GABA at their axon terminals;
    #       modulate the PMC's output and contribute to the coordination
    #       of the micturition reflex
    #
    # Do not attempt to resolve these as sub-paths of the PMC — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical PMC anatomy:** Barrington, F.J.F. (1925). "The effect
    of lesions of the hind- and mid-brain on micturition in the cat."
    *Quarterly Journal of Experimental Physiology* 15:81–102. (Original
    description of the pontine micturition center — Barrington's
    nucleus.)
*   **PMC — canonical modern review:** Fowler, C.J., Griffiths, D., de
    Groat, W.C. (2008). "The neural control of micturition." *Nature
    Reviews Neuroscience* 9:453–466. (Pontine micturition center —
    micturition reflex control; comprehensive review.)
*   **PMC — anatomy and connectivity:** Holstege, G., Griffiths, D., de
    Wall, H., Dalm, E. (1996). "Anatomical and physiological
    observations on supraspinal control of bladder and urethral
    sphincter muscles in the cat." *Journal of Comparative Neurology*
    250:449–461. (Pontine micturition center — anatomy and connectivity;
    the descending projections to the sacral spinal cord.)
*   **PMC — CRF expression:** Vincent, S.R., Satoh, K., Armstrong, D.M.,
    Fibiger, H.C. (1983). "Substance P in the ascending cholinergic
    reticular system." *Nature* 306:688–691. (Pontine micturition
    center — CRF co-expression; the CRF-expressing neurons.)
*   **Micturition reflex — neural control:** de Groat, W.C., Griffiths,
    D., Yoshimura, N. (2015). "Neural control of the lower urinary
    tract." *Comprehensive Physiology* 5:327–396. (Micturition reflex —
    neural control; the PMC's role in the micturition reflex.)
*   **Supraspinal micturition control — review:** Blok, B.F.M.,
    Holstege, G. (1994). "Direct projections from the periaqueductal
    gray to the pontine micturition center (M-region): an anterograde
    and retrograde tracing study in the cat." *Neuroscience Letters*
    166:93–96. (Periaqueductal gray — the midbrain upstream micturition
    region that projects to the PMC.)
*   **Forebrain micturition control:** Holstege, G. (2005). "The central
    nervous system control of micturition." *Advances in Anatomy,
    Embryology, and Cell Biology* 178:1–118. (Hypothalamus and medial
    prefrontal cortex — the forebrain and cortical upstream micturition
    regions.)
*   **Neurogenic bladder — PMC involvement:** Fowler, C.J., Griffiths,
    D., de Groat, W.C. (2008). "The neural control of micturition."
    *Nature Reviews Neuroscience* 9:453–466. (Neurogenic bladder —
    detrusor-sphincter dyssynergia; PMC dysfunction.)
*   **Multiple sclerosis — PMC involvement:** Litwiller, S.E., Frohman,
    E.M., Zimmern, P.E. (1999). "Multiple sclerosis and the
    urologist." *Journal of Urology* 162:2069–2076. (Multiple sclerosis
    — neurogenic bladder; PMC involvement.)
*   **Parkinson's disease — PMC involvement:** Sakakibara, R., Uchiyama,
    T., Yamanishi, T., Shirai, K., Hattori, T. (2008). "Bladder and
    bowel dysfunction in Parkinson's disease." *Journal of Neural
    Transmission* 115:443–459. (Parkinson's disease — lower urinary
    tract symptoms; PMC involvement.)
*   **Pontine stroke — PMC involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — pontine tegmentum involvement,
    including the PMC.)
*   **Normal pressure hydrocephalus — PMC involvement:** Klinge, P.,
    Berding, G., Brinker, T., et al. (2005). "A positron emission
    tomography study of cortical glucose metabolism in normal pressure
    hydrocephalus." *Journal of Neurosurgery* 103:437–447. (Normal
    pressure hydrocephalus — urinary incontinence; PMC involvement.)
*   **Locus coeruleus (contrast — the NORADRENERGIC neuromodulatory
    sibling):** Aston-Jones, G., Cohen, J.D. (2005). "An integrative
    theory of locus coeruleus-norepinephrine function: adaptive gain
    and optimal performance." *Annual Review of Neuroscience*
    28:403–450. (Locus coeruleus — noradrenergic neuromodulatory
    nucleus; sibling of the PMC.)
*   **Laterodorsal tegmental nucleus (contrast — the CHOLINERGIC
    neuromodulatory sibling):** Mesulam, M.M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the rat:
    an overview based on an alternative nomenclature (Ch1-Ch6)."
    *Neuroscience* 10:1185–1201. (LDT — cholinergic neuromodulatory
    nucleus; sibling of the PMC.)
*   **Pedunculopontine nucleus (contrast — the CHOLINERGIC LOCOMOTION
    sibling):** Garcia-Rill, E. (1991). "The pedunculopontine nucleus."
    *Progress in Neurobiology* 36:363–389. (PPN — cholinergic
    locomotion and REM-sleep nucleus; sibling of the PMC.)
*   **Nucleus incertus (contrast — the RELAXIN-3 sibling):** Ryan, P.J.,
    Ma, S., Olucha-Bordonau, F.E., Gundlach, A.L. (2011). "Nucleus
    incertus — an emerging role in the behavioural actions of
    relaxin-3." *British Journal of Pharmacology* 162:1115–1126.
    (Nucleus incertus — relaxin-3 stress, arousal, and feeding; sibling
    of the PMC.)
*   **Tegmental pontine reticular nucleus (contrast — the MOTOR RELAY
    sibling):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Tegmental pontine reticular
    nucleus — motor relay; sibling of the PMC.)
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
    pons; distinct from the PMC.)
*   **Fourth ventricle (contrast — a CSF space):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Fourth ventricle — CSF space dorsal to the pons; distinct from the
    PMC.)
*   **Midbrain tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Midbrain tegmentum — dorsal midbrain; distinct
    from the pontine tegmentum.)
*   **Medullary tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary tegmentum — dorsal medulla; distinct
    from the pontine tegmentum.)
*   **SLEA (contrast — the PMC is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the PMC.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the PMC.)
*   NeuroNames — Barrington's nucleus; FMA — Barrington's nucleus.
"""