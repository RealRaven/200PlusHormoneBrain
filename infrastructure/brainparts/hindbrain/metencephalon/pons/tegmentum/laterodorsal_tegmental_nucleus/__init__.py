"""
infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum.laterodorsal_tegmental_nucleus
=============================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── tegmentum
                └── laterodorsal_tegmental_nucleus   <-- THIS MODULE

**Primary synonym:** Laterodorsal tegmental nucleus; LDT; LDTg; "the
pontine cholinergic REM-sleep and arousal nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nucleus** — an **anatomically delimited
cholinergic (with glutamatergic and GABAergic components) nucleus** in
the **dorsal pontine tegmentum**, near the **midline** and just
**ventral to the fourth ventricle**. It is the **pontine cholinergic
REM-sleep and arousal nucleus** — the **principal cholinergic source**
for the **thalamus** and a **major cholinergic source** for the
**basal forebrain** — and the **neural substrate** of the
**cholinergic component** of **REM sleep** and **arousal**.
**Part of:** The **tegmentum** container — specifically, the
**neuromodulatory (cholinergic)** component. The **tegmentum** is the
**dorsal pontine grey-matter region** — the **tree-wired container** for
the six neuromodulatory and autonomic nuclei of the dorsal pons.
**Structural parent:** ``.../tegmentum/`` → **direct child** of the
tegmentum container.
**Structural children:** **None.** This is a **leaf** module. The
**cholinergic principal neurons**, the **glutamatergic neurons**, and
the **GABAergic neurons** are documented as **prose**, not as structural
children — they are the **functionally distinct neuron populations**
within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
laterodorsal tegmental nucleus is a LEAF, not a container.** It has **no
structural children**. The **cholinergic**, **glutamatergic**, and
**GABAergic** neuron populations are **prose** populations, not
structural children. Consumers must **not** treat the laterodorsal
tegmental nucleus as a container, and must **not** assume the neuron
populations exist as sub-modules.
**Boundary status (SINGLE MODULE — NOT bilateralized at the tree level):**
**Boundary case — the laterodorsal tegmental nucleus is a SINGLE module
at the tree level, even though the LDT is BILATERAL in real anatomy.**
Unlike the **cranial_nerve_nuclei** module (which has explicit ``left``
and ``right`` structural children) or the **superior_olivary_complex**
module (which has ``left`` and ``right`` sub-containers), the
**laterodorsal_tegmental_nucleus** module (here) is a **single module**
that represents the **bilateral LDT** (the left and right LDT). The tree
does **not** split them into left/right. Consumers must **not** assume a
left/right split exists at the tree level — the module is a **single,
bilateral representation**. Any lateralization is documented **here, in
the Lateralization Notes**, not imported from elsewhere.
**Boundary status (CHOLINERGIC NEUROMODULATORY NUCLEUS — NOT a motor or
sensory relay):** **Boundary case — the laterodorsal tegmental nucleus
is a CHOLINERGIC NEUROMODULATORY nucleus, NOT a motor or sensory relay.**
Unlike the **cranial nerve motor nuclei** (branchial or somatic motor
relays) or the **sensory nuclei** (e.g., the cochlear nuclei,
trigeminal nuclei), the **laterodorsal tegmental nucleus** (here) is a
**neuromodulatory nucleus** — its **cholinergic (with glutamatergic and
GABAergic components)** neurons **project diffusely** to the
**thalamus**, the **hypothalamus**, the **basal forebrain**, and the
**brainstem** to **modulate** the **excitability** of their targets —
they **do not** directly **relay** motor commands or **transmit**
sensory information. **This distinction is functionally load-bearing**
— the laterodorsal tegmental nucleus is a **state-setting** nucleus,
not a **throughput** nucleus. Consumers must **not** conflate the
laterodorsal tegmental nucleus with a motor or sensory relay.
**Boundary status (NOT the locus coeruleus — that is the NORADRENERGIC
neuromodulatory nucleus):** **Boundary case — the laterodorsal
tegmental nucleus is NOT the locus coeruleus.** The **locus coeruleus**
(``.../tegmentum/locus_coeruleus/``) is the **noradrenergic** nucleus —
the **principal source of norepinephrine** in the brain. The
**laterodorsal tegmental nucleus** (here) is the **cholinergic** nucleus
— the **principal pontine cholinergic source** for the **thalamus**.
They are **DIFFERENT STRUCTURES** — different neurotransmitters
(noradrenaline vs. acetylcholine), different functional systems
(noradrenergic arousal/attention/stress vs. cholinergic REM-sleep/
arousal/motivation), different projection targets (diffuse noradrenergic
vs. thalamic and basal-forebrain cholinergic). They are **anatomically
adjacent** (both are in the **dorsal pontine tegmentum**) — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the laterodorsal tegmental nucleus with the locus coeruleus.
**Boundary status (NOT the pedunculopontine nucleus — that is the
CHOLINERGIC LOCOMOTION nucleus):** **Boundary case — the laterodorsal
tegmental nucleus is NOT the pedunculopontine nucleus (PPN).** The
**pedunculopontine nucleus** (``.../tegmentum/pedunculopontine_nucleus/``)
is the **cholinergic** (with glutamatergic and GABAergic components)
nucleus — it is the **mesencephalic locomotor region** (with the
**cuneiform nucleus**) and is involved in **locomotion**, **REM sleep**,
**arousal**, and **reward**. The **laterodorsal tegmental nucleus**
(here) is the **pontine cholinergic REM-sleep and arousal nucleus** —
it is **primarily** involved in **REM sleep** and **arousal** (via the
**thalamus** and the **basal forebrain**). They are **DIFFERENT
STRUCTURES** — different functional emphases (locomotion/REM/reward for
the PPN vs. REM/arousal for the LDT) and different **anatomical
locations** (the LDT is **dorsomedial** in the pontine tegmentum; the
PPN is **ventrolateral** at the **pontomesencephalic junction**). **They
are both cholinergic** — this shared neurotransmitter is a **classic
source of confusion** — consumers must **not** conflate the laterodorsal
tegmental nucleus with the pedunculopontine nucleus. They are
**functionally coupled** — the LDT and the PPN are **both cholinergic
REM-sleep and arousal nuclei** — but they are **different structures**
with **different anatomical locations** and **different functional
emphases**.
**Boundary status (NOT the nucleus incertus — that is the RELAXIN-3
nucleus):** **Boundary case — the laterodorsal tegmental nucleus is NOT
the nucleus incertus.** The **nucleus incertus**
(``.../tegmentum/nucleus_incertus/``) is the **relaxin-3-expressing
nucleus** — it is involved in **stress**, **arousal**, **feeding**, and
**neuroendocrine regulation**. The **laterodorsal tegmental nucleus**
(here) is the **cholinergic** nucleus — it is involved in **REM sleep**,
**arousal**, and **motivation**. They are **DIFFERENT STRUCTURES** —
different neurotransmitters (relaxin-3 vs. acetylcholine), different
functional systems (stress/arousal/feeding vs. REM-sleep/arousal/
motivation), different projection targets (septum/hippocampus/medial
prefrontal cortex/amygdala/hypothalamus vs. thalamus/basal forebrain/
hypothalamus/brainstem). Consumers must **not** conflate the
laterodorsal tegmental nucleus with the nucleus incertus.
**Boundary status (NOT the pontine micturition center — that is the
MICTURITION nucleus):** **Boundary case — the laterodorsal tegmental
nucleus is NOT the pontine micturition center (Barrington's nucleus).**
The **pontine micturition center**
(``.../tegmentum/pontine_micturition_center/``) is the **micturition
control center** — it **coordinates** the **micturition reflex** (bladder
contraction and sphincter relaxation). The **laterodorsal tegmental
nucleus** (here) is the **cholinergic REM-sleep and arousal nucleus** —
it is involved in **REM sleep** and **arousal**. They are **DIFFERENT
STRUCTURES** — different functional systems (micturition vs.
REM-sleep/arousal), different projection targets (sacral spinal cord vs.
thalamus/basal forebrain/hypothalamus/brainstem). Consumers must **not**
conflate the laterodorsal tegmental nucleus with the pontine micturition
center.
**Boundary status (NOT the tegmental pontine reticular nucleus — that is
the MOTOR RELAY nucleus):** **Boundary case — the laterodorsal
tegmental nucleus is NOT the tegmental pontine reticular nucleus.** The
**tegmental pontine reticular nucleus**
(``.../tegmentum/tegmental_pontine_reticular_nucleus/``) is a **motor
relay** — it **projects** to the **spinal cord** (via the
**reticulospinal tract**) and to the **cerebellum** (via the
**pontocerebellar fibers**) — it is involved in **locomotion**,
**posture**, and **motor pattern generation**. The **laterodorsal
tegmental nucleus** (here) is the **cholinergic REM-sleep and arousal
nucleus** — it is involved in **REM sleep** and **arousal**. They are
**DIFFERENT STRUCTURES** — different functional systems (motor relay vs.
REM-sleep/arousal), different projection targets (spinal cord/cerebellum
vs. thalamus/basal forebrain/hypothalamus/brainstem). Consumers must
**not** conflate the laterodorsal tegmental nucleus with the tegmental
pontine reticular nucleus.
**Boundary status (NOT the parabrachial area — that is a SEPARATE
structural child of the pons):** **Boundary case — the laterodorsal
tegmental nucleus is NOT the parabrachial area.** The **parabrachial
area** (``.../pons/parabrachial_area/``) is the **visceral-sensory and
respiratory-relay complex** — it is a **separate structural child of the
pons**, **not** a structural child of the pontine tegmentum, **even
though** it is **anatomically located** in the **pontine tegmentum**.
The **laterodorsal tegmental nucleus** (here) is a **cholinergic
neuromodulatory nucleus** — a **structural child of the pontine
tegmentum container**. Consumers must **not** conflate the laterodorsal
tegmental nucleus with the parabrachial area.
**Boundary status (NOT the superior olivary complex, the cranial nerve
nuclei, the PPRF, or the parvocellular reticular nucleus — those are
SEPARATE structural children of the pons):** **Boundary case — the
laterodorsal tegmental nucleus is NOT the superior olivary complex, the
cranial nerve nuclei, the PPRF, or the parvocellular reticular
nucleus.** Those are **separate structural children of the pons** — the
**superior olivary complex** (binaural sound-localization relay), the
**cranial nerve nuclei** (CN V, VI, VII, VIII nuclei), the **PPRF**
(horizontal saccadic burst generator), and the **parvocellular
reticular nucleus** (orofacial premotor and autonomic relay). The
**laterodorsal tegmental nucleus** (here) is a **cholinergic
neuromodulatory nucleus** — a **structural child of the pontine
tegmentum container**. Consumers must **not** conflate the laterodorsal
tegmental nucleus with any of them.
**Boundary status (NOT the pontine nuclei — those are in the BASILAR
pons):** **Boundary case — the laterodorsal tegmental nucleus is NOT
the pontine nuclei.** The **pontine nuclei**
(``.../pons/pontine_nuclei/``) are the **cortico-ponto-cerebellar relay**
in the **basilar pons** — the **ventral** portion of the pons. The
**laterodorsal tegmental nucleus** (here) is a **cholinergic
neuromodulatory nucleus** in the **dorsal pontine tegmentum**. They are
**DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not** conflate the
laterodorsal tegmental nucleus with the pontine nuclei.
**Boundary status (NOT the whole tegmentum container — that is the
PARENT):** **Boundary case — the laterodorsal tegmental nucleus is NOT
the whole tegmentum container; the tegmentum container is the PARENT.**
The **tegmentum** container (``.../pons/tegmentum/``) is the **dorsal
pontine grey-matter region** — the **tree-wired container** for the
**six neuromodulatory and autonomic nuclei** (locus coeruleus,
laterodorsal tegmental nucleus, nucleus incertus, pedunculopontine
nucleus, pontine micturition center, tegmental pontine reticular
nucleus). The **laterodorsal tegmental nucleus** (here) is **one of the
six structural children** of the tegmentum container. Consumers must
**not** conflate the laterodorsal tegmental nucleus with the **whole
tegmentum**.
**Boundary status (NOT the whole pons — the pons is the GRANDPARENT):**
**Boundary case — the laterodorsal tegmental nucleus is NOT the whole
pons; the pons is the GRANDPARENT.** The **pons** (``.../pons/``) is the
**whole metencephalic brainstem segment** — it contains the **basilar
pons**, the **pontine tegmentum**, the **parabrachial area**, the
**superior olivary complex**, the **cranial nerve nuclei**, the **PPRF**,
the **parvocellular reticular nucleus**, the **pontine nuclei**, and the
**six neuromodulatory and autonomic nuclei** of the tegmentum container.
The **laterodorsal tegmental nucleus** (here) is **one of the six
neuromodulatory and autonomic nuclei** only. Consumers must **not**
conflate the laterodorsal tegmental nucleus with the **whole pons**.
**Boundary status (NOT the fourth ventricle — that is a CSF SPACE):**
**Boundary case — the laterodorsal tegmental nucleus is NOT the fourth
ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the **CSF-filled space**
**dorsal to** the pons and **ventral to** the cerebellum. The
**laterodorsal tegmental nucleus** (here) is a **grey-matter nucleus**
that sits **just ventral to** the fourth ventricle. They are **DIFFERENT
STRUCTURES** — the **fourth ventricle** is a **fluid space**; the
**laterodorsal tegmental nucleus** is **neural tissue**. Consumers must
**not** conflate the laterodorsal tegmental nucleus with the fourth
ventricle.
**Boundary status (NOT the midbrain tegmentum or the medullary
tegmentum — those are DIFFERENT BRAINSTEM LEVELS):** **Boundary case —
the laterodorsal tegmental nucleus is NOT the midbrain tegmentum or the
medullary tegmentum.** The **midbrain tegmentum**
(``.../midbrain/tegmentum/``) is the **dorsal portion of the midbrain**;
the **medullary tegmentum** is the **dorsal portion of the medulla
oblongata**. The **laterodorsal tegmental nucleus** (here) is a
**specific nucleus** in the **dorsal portion of the pons**. They are
**DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate the
laterodorsal tegmental nucleus with the midbrain tegmentum or the
medullary tegmentum.
**Boundary status (MULTIPLE FUNCTIONALLY DISTINCT NEURON POPULATIONS —
cholinergic, glutamatergic, and GABAergic):** **Boundary case — the
laterodorsal tegmental nucleus is NOT a single uniform neuron
population; it contains MULTIPLE functionally distinct populations.**
The **cholinergic principal neurons** — the **cholinergic** neurons
that **project** to the **thalamus**, the **hypothalamus**, the **basal
forebrain**, and the **brainstem** — they are the **principal output**
of the LDT and the **cholinergic component** of **REM sleep** and
**arousal**. The **glutamatergic neurons** and the **GABAergic
neurons** — the **non-cholinergic** neurons of the LDT — they
**modulate** the **local circuit** and the **cholinergic output**, and
they **contribute** to the **REM-sleep and arousal functions** of the
LDT. **These populations are prose, not structural children.** Consumers
must **not** treat the laterodorsal tegmental nucleus as a single
uniform population — it is a **neurochemically heterogeneous nucleus**
with **distinct** sub-circuits.
**Boundary status (SLEA-FREE — the laterodorsal tegmental nucleus is NOT
an extended-amygdala component):** **Boundary case — the laterodorsal
tegmental nucleus is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala) and to
the **BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **laterodorsal tegmental nucleus** is a **cholinergic
neuromodulatory nucleus** — it is **NOT** an extended-amygdala
component, and it carries **NO SLEA warning**. Consumers must **not**
import the SLEA warning into the laterodorsal tegmental nucleus — it is
**SLEA-free**.

Overview
--------
The laterodorsal tegmental nucleus is the **pontine cholinergic
REM-sleep and arousal nucleus** of the **pontine tegmentum** — a
**neurochemically heterogeneous** grey-matter nucleus in the **dorsal
pontine tegmentum**, near the **midline** and just **ventral to the
fourth ventricle**. It is a **leaf** module under the tegmentum
container, and it is the **principal cholinergic source** for the
**thalamus** and a **major cholinergic source** for the **basal
forebrain** — the **neural substrate** of the **cholinergic component**
of **REM sleep** and **arousal**.

**The laterodorsal tegmental nucleus is a LEAF, not a container.** It
has **no structural children**. The **cholinergic**, **glutamatergic**,
and **GABAergic** neuron populations are **prose populations**, not
structural children.

**The laterodorsal tegmental nucleus is a SINGLE module at the tree
level.** The tree does **not** split the LDT into left/right — the
module is a **single, bilateral representation**.

**The laterodorsal tegmental nucleus is a CHOLINERGIC NEUROMODULATORY
NUCLEUS, NOT a motor or sensory relay.** It **projects diffusely** to
the **thalamus**, the **hypothalamus**, the **basal forebrain**, and the
**brainstem** to **modulate** the **excitability** of its targets — it
does **not** directly **relay** motor commands or **transmit** sensory
information.

**The laterodorsal tegmental nucleus is NOT the locus coeruleus.** The
**locus coeruleus** is the **noradrenergic** nucleus. They are
**anatomically adjacent** and **both** are **neuromodulatory** — but
they use **different neurotransmitters** and **subserve different
functional systems**.

**The laterodorsal tegmental nucleus is NOT the pedunculopontine
nucleus.** Both are **cholinergic** and **both** are **REM-sleep and
arousal nuclei** — but they are **different structures** with
**different anatomical locations** (LDT is **dorsomedial**; PPN is
**ventrolateral**) and **different functional emphases** (LDT is
**primarily** REM-sleep and arousal; PPN is **primarily** locomotion,
REM-sleep, and reward).

**The laterodorsal tegmental nucleus is NOT the nucleus incertus, the
pontine micturition center, or the tegmental pontine reticular
nucleus.** Those are **different structures** — the **nucleus incertus**
(relaxin-3 stress/arousal), the **pontine micturition center**
(micturition), and the **tegmental pontine reticular nucleus** (motor
relay).

**The laterodorsal tegmental nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Prose Population Composition (prose, not structural children)
-------------------------------------------------------------
The laterodorsal tegmental nucleus contains **multiple functionally
distinct neuron populations** — documented as **prose**, not as
structural children:

*   **Cholinergic principal neurons** — the **cholinergic** neurons that
    **project** to the **thalamus**, the **hypothalamus**, the **basal
    forebrain**, and the **brainstem** — they are the **principal
    output** of the LDT and the **cholinergic component** of **REM
    sleep** and **arousal**. **Cholinergic REM-sleep and arousal
    modulation are the functional systems** subserved primarily by the
    cholinergic principal neurons — they **activate** the **thalamus**
    (especially the **intralaminar nuclei** and the **reticular
    nucleus**) during **REM sleep**, they **activate** the **basal
    forebrain** (the **cholinergic basal forebrain** — the **medial
    septal nucleus**, the **diagonal band of Broca**, the **nucleus
    basalis**) during **arousal**, and they **modulate** the
    **hypothalamus** and the **brainstem** to **promote** the
    **arousal** and **REM-sleep** states.

*   **Glutamatergic neurons** — the **glutamatergic** neurons of the LDT
    — they **project** to the **thalamus**, the **hypothalamus**, the
    **basal forebrain**, and the **brainstem** (in some cases
    **co-releasing** glutamate with acetylcholine, or projecting
    independently). They **contribute** to the **REM-sleep and
    arousal functions** of the LDT — the **glutamatergic component** of
    the LDT's **neuromodulatory output**. **Glutamatergic REM-sleep and
    arousal modulation are the functional systems** subserved primarily
    by the glutamatergic neurons.

*   **GABAergic neurons** — the **GABAergic** neurons of the LDT — they
    **modulate** the **local circuit** within the LDT and the
    **cholinergic and glutamatergic output** (in some cases projecting
    to the **thalamus** or the **brainstem**). They **contribute** to
    the **regulation** of the LDT's **REM-sleep and arousal
    functions** — the **GABAergic component** of the LDT's
    **neuromodulatory output**. **GABAergic REM-sleep and arousal
    modulation are the functional systems** subserved primarily by the
    GABAergic neurons.

**These populations are prose, not structural children.** The tree
wires the **laterodorsal tegmental nucleus** as a **single leaf** under
the tegmentum container — the **cholinergic principal neurons**, the
**glutamatergic neurons**, and the **GABAergic neurons** are **prose**,
not structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Laterodorsal Tegmental Nucleus / Locus Coeruleus Boundary
--------------------------------------------------------------
This is the **sibling** boundary — **cholinergic vs. noradrenergic
neuromodulatory nucleus**:

*   **Laterodorsal tegmental nucleus** (this module) — the **cholinergic**
    REM-sleep and arousal nucleus.

*   **Locus coeruleus** (``.../tegmentum/locus_coeruleus/``) — the
    **noradrenergic** nucleus — the **principal source of
    norepinephrine** in the brain.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(acetylcholine vs. noradrenaline), different functional systems
(cholinergic REM-sleep/arousal/motivation vs. noradrenergic
arousal/attention/stress), different projection targets (thalamus and
basal forebrain vs. diffuse noradrenergic). They are **anatomically
adjacent** (both are in the **dorsal pontine tegmentum**) — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the laterodorsal tegmental nucleus with the locus coeruleus.

The Laterodorsal Tegmental Nucleus / Pedunculopontine Nucleus Boundary
---------------------------------------------------------------------
This is the **sibling** boundary — **REM-sleep/arousal cholinergic vs.
locomotion/REM/reward cholinergic**:

*   **Laterodorsal tegmental nucleus** (this module) — the
    **pontine** cholinergic REM-sleep and arousal nucleus —
    **dorsomedial** in the pontine tegmentum.

*   **Pedunculopontine nucleus**
    (``.../tegmentum/pedunculopontine_nucleus/``) — the **cholinergic**
    (with glutamatergic and GABAergic components) nucleus — the
    **mesencephalic locomotor region** — **ventrolateral** at the
    **pontomesencephalic junction**.

**They are DIFFERENT STRUCTURES** — different functional emphases
(locomotion/REM/reward for the PPN vs. REM/arousal for the LDT) and
different **anatomical locations** (the LDT is **dorsomedial**; the PPN
is **ventrolateral**). **They are both cholinergic** — this shared
neurotransmitter is a **classic source of confusion** — consumers must
**not** conflate the laterodorsal tegmental nucleus with the
pedunculopontine nucleus. They are **functionally coupled** — the LDT
and the PPN are **both cholinergic REM-sleep and arousal nuclei** — but
they are **different structures** with **different anatomical
locations** and **different functional emphases**.

The Laterodorsal Tegmental Nucleus / Nucleus Incertus Boundary
-------------------------------------------------------------
This is the **sibling** boundary — **cholinergic vs. relaxin-3**:

*   **Laterodorsal tegmental nucleus** (this module) — the **cholinergic**
    REM-sleep and arousal nucleus.

*   **Nucleus incertus** (``.../tegmentum/nucleus_incertus/``) — the
    **relaxin-3-expressing** nucleus — involved in **stress**,
    **arousal**, **feeding**, and **neuroendocrine regulation**.

**They are DIFFERENT STRUCTURES** — different neurotransmitters
(acetylcholine vs. relaxin-3), different functional systems
(REM-sleep/arousal/motivation vs. stress/arousal/feeding), different
projection targets (thalamus/basal forebrain/hypothalamus/brainstem vs.
septum/hippocampus/medial prefrontal cortex/amygdala/hypothalamus).
Consumers must **not** conflate the laterodorsal tegmental nucleus with
the nucleus incertus.

The Laterodorsal Tegmental Nucleus / Pontine Micturition Center Boundary
-----------------------------------------------------------------------
This is the **sibling** boundary — **REM-sleep/arousal vs.
micturition**:

*   **Laterodorsal tegmental nucleus** (this module) — the **cholinergic**
    REM-sleep and arousal nucleus.

*   **Pontine micturition center**
    (``.../tegmentum/pontine_micturition_center/``) — the **micturition
    control center** — it **coordinates** the **micturition reflex**.

**They are DIFFERENT STRUCTURES** — different functional systems
(REM-sleep/arousal vs. micturition), different projection targets
(thalamus/basal forebrain/hypothalamus/brainstem vs. sacral spinal
cord). Consumers must **not** conflate the laterodorsal tegmental
nucleus with the pontine micturition center.

The Laterodorsal Tegmental Nucleus / Tegmental Pontine Reticular Nucleus Boundary
--------------------------------------------------------------------------------
This is the **sibling** boundary — **REM-sleep/arousal vs. motor relay**:

*   **Laterodorsal tegmental nucleus** (this module) — the **cholinergic**
    REM-sleep and arousal nucleus.

*   **Tegmental pontine reticular nucleus**
    (``.../tegmentum/tegmental_pontine_reticular_nucleus/``) — the
    **motor relay** — it **projects** to the **spinal cord** and the
    **cerebellum** — it is involved in **locomotion**, **posture**, and
    **motor pattern generation**.

**They are DIFFERENT STRUCTURES** — different functional systems
(REM-sleep/arousal vs. motor relay), different projection targets
(thalamus/basal forebrain/hypothalamus/brainstem vs. spinal
cord/cerebellum). Consumers must **not** conflate the laterodorsal
tegmental nucleus with the tegmental pontine reticular nucleus.

The Laterodorsal Tegmental Nucleus / Parabrachial Area Boundary
---------------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Laterodorsal tegmental nucleus** (this module) — a **cholinergic
    neuromodulatory nucleus** — a **structural child of the pontine
    tegmentum container**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex** — a **separate
    structural child of the pons**.

**They are DIFFERENT STRUCTURES** — the parabrachial area is **not** a
structural child of the pontine tegmentum (in the tree), even though it
is **anatomically located** in the pontine tegmentum. Consumers must
**not** conflate the laterodorsal tegmental nucleus with the parabrachial
area.

The Laterodorsal Tegmental Nucleus / Superior Olivary Complex, Cranial Nerve Nuclei, PPRF, and Parvocellular Reticular Nucleus Boundary
------------------------------------------------------------------------------------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Laterodorsal tegmental nucleus** (this module) — a **cholinergic
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
must **not** conflate the laterodorsal tegmental nucleus with any of
them.

The Laterodorsal Tegmental Nucleus / Pontine Nuclei Boundary
------------------------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Laterodorsal tegmental nucleus** (this module) — a **cholinergic
    neuromodulatory nucleus** in the **dorsal pontine tegmentum**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not**
conflate the laterodorsal tegmental nucleus with the pontine nuclei.

The Laterodorsal Tegmental Nucleus / Whole Tegmentum Container Boundary
-----------------------------------------------------------------------
This is the **sub-nucleus vs. parent** boundary:

*   **Laterodorsal tegmental nucleus** (this module) — one of the **six
    neuromodulatory and autonomic nuclei** of the pontine tegmentum.

*   **Tegmentum container** (``.../pons/tegmentum/``) — the **dorsal
    pontine grey-matter region** — the **tree-wired container** for the
    **six neuromodulatory and autonomic nuclei**.

**The laterodorsal tegmental nucleus is a child of the tegmentum
container.** Consumers must **not** conflate the laterodorsal tegmental
nucleus with the **whole tegmentum**.

The Laterodorsal Tegmental Nucleus / Whole Pons Boundary
--------------------------------------------------------
This is the **nucleus vs. grandparent** boundary:

*   **Laterodorsal tegmental nucleus** (this module) — one of the **six
    neuromodulatory and autonomic nuclei** of the pontine tegmentum.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**.

**The laterodorsal tegmental nucleus is a grandchild of the pons** (via
the tegmentum container). Consumers must **not** conflate the
laterodorsal tegmental nucleus with the **whole pons**.

The Laterodorsal Tegmental Nucleus / Fourth Ventricle Boundary
--------------------------------------------------------------
This is the **neural tissue vs. CSF space** boundary:

*   **Laterodorsal tegmental nucleus** (this module) — a **grey-matter
    nucleus** that sits **just ventral to** the fourth ventricle.

*   **Fourth ventricle** (``.../metencephalon/fourth_ventricle/``) — the
    **CSF-filled space** **dorsal to** the pons.

**They are DIFFERENT STRUCTURES** — the **fourth ventricle** is a
**fluid space**; the **laterodorsal tegmental nucleus** is **neural
tissue**. Consumers must **not** conflate the laterodorsal tegmental
nucleus with the fourth ventricle.

The Laterodorsal Tegmental Nucleus / Midbrain Tegmentum and Medullary Tegmentum Boundary
---------------------------------------------------------------------------------------
This is the **pons vs. midbrain/medulla** boundary:

*   **Laterodorsal tegmental nucleus** (this module) — a **specific
    nucleus** in the **dorsal portion of the pons**.

*   **Midbrain tegmentum** (``.../midbrain/tegmentum/``) and **medullary
    tegmentum** — the **dorsal portions** of the **midbrain** and the
    **medulla oblongata**.

**They are DIFFERENT BRAINSTEM LEVELS** — consumers must **not** conflate
the laterodorsal tegmental nucleus with the midbrain tegmentum or the
medullary tegmentum.

The Laterodorsal Tegmental Nucleus / SLEA Boundary
--------------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Laterodorsal tegmental nucleus** (this module) — **SLEA-FREE**. It
    is **not** an extended-amygdala component, and it carries **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The laterodorsal tegmental nucleus is NOT part of the SLEA
continuum.** It is a **cholinergic neuromodulatory nucleus**, and it
carries **no SLEA warning**. Consumers must **not** import the SLEA
warning into the laterodorsal tegmental nucleus.

Function in the Human Brain
---------------------------
The laterodorsal tegmental nucleus's functions are **the cholinergic
(and glutamatergic and GABAergic) modulation of REM sleep and arousal** —
**NOT a single unified function**:

*   **REM Sleep (Cholinergic Thalamic Activation):** The **cholinergic
    principal neurons** of the LDT **project** to the **thalamus** —
    especially the **intralaminar nuclei** and the **reticular
    nucleus** — they **activate** the **thalamus** during **REM
    sleep**, **promoting** the **thalamocortical activation** that
    **underlies** the **desynchronized EEG** of **REM sleep**. The
    **LDT** is a **major cholinergic REM-sleep nucleus** — **along with
    the pedunculopontine nucleus**.

*   **Arousal (Cholinergic Basal-Forebrain Activation):** The
    **cholinergic principal neurons** of the LDT **project** to the
    **basal forebrain** — the **medial septal nucleus**, the **diagonal
    band of Broca**, and the **nucleus basalis** — they **activate** the
    **cholinergic basal forebrain** during **arousal**, **promoting**
    the **cortical activation** that **underlies** the **awake** and
    **alert** states.

*   **Motivation and Reward (Cholinergic and Glutamatergic Modulation):**
    The **LDT** (with the **pedunculopontine nucleus**) **projects** to
    the **ventral tegmental area** and the **substantia nigra** — it
    **modulates** the **dopaminergic** systems that **underlie**
    **motivation** and **reward**. The **LDT's glutamatergic** and
    **cholinergic** neurons **contribute** to the **reward-related**
    and **motivational** functions of the **pontomesencephalic
    cholinergic system**.

*   **Descending Modulation (Cholinergic and GABAergic Brainstem
    Projections):** The **LDT** **projects** to the **brainstem** —
    including the **medulla** and the **spinal cord** (via the
    **reticulospinal** and **descending autonomic** pathways) — it
    **modulates** the **autonomic** and **motor** functions of the
    **brainstem** and the **spinal cord**, and it **contributes** to
    the **REM-sleep atonia** via its **projections** to the
    **medullary** and **spinal** motor systems.

*   **NOT a neural processor in the classical sense.** The LDT is a
    **neuromodulatory nucleus** — it **receives** afferent inputs (from
    the **hypothalamus**, the **brainstem**, the **limbic system**, and
    the **cortex**) and **projects diffusely** to the **thalamus**, the
    **basal forebrain**, the **hypothalamus**, the **brainstem**, and
    the **spinal cord**. The **processing** of REM sleep and arousal
    happens in a **distributed** manner across the **LDT**, the
    **pedunculopontine nucleus**, the **thalamus**, the **basal
    forebrain**, the **hypothalamus**, and the **brainstem**.

**The unifying theme:** the laterodorsal tegmental nucleus is the
**pontine cholinergic REM-sleep and arousal nucleus** — the **principal
pontine cholinergic source** for the **thalamus** and a **major
cholinergic source** for the **basal forebrain**. It is
**neurochemically heterogeneous** (cholinergic, glutamatergic, and
GABAergic neurons), **SLEA-free**, and **NOT the locus coeruleus** — the
**locus coeruleus** is the **noradrenergic** neuromodulatory nucleus.

Associated Disorders
--------------------
The laterodorsal tegmental nucleus has **no named "laterodorsal
tegmental nucleus syndrome"** — its clinical associations are
**function-specific**:

*   **REM Sleep Behavior Disorder (RBD) — LDT Involvement:** **REM sleep
    behavior disorder** is a **parasomnia** characterized by **loss of
    REM-sleep atonia** and **acting out of dreams** — it has been
    **associated** with **dysfunction** of the **pontine REM-sleep
    nuclei**, including the **laterodorsal tegmental nucleus** (and the
    **pedunculopontine nucleus**, the **sublaterodorsal nucleus**, and
    the **medullary REM-sleep circuits**). The **LDT** is **one of the
    neural substrates** of **REM-sleep control**, and its dysfunction
    may **contribute** to **RBD**.

*   **Narcolepsy — LDT Involvement:** **Narcolepsy** is a **sleep
    disorder** characterized by **excessive daytime sleepiness**,
    **cataplexy**, **hypnagogic hallucinations**, and **sleep
    paralysis** — it is caused by **loss of orexin (hypocretin)
    neurons** in the **hypothalamus**, but the **cholinergic REM-sleep
    nuclei** (including the **LDT**) are **involved** in the
    **downstream** effects of **orexin loss** — the **LDT's
    cholinergic** neurons **contribute** to the **REM-sleep
    dysregulation** in **narcolepsy**.

*   **Parkinson's Disease — LDT Involvement:** **Parkinson's disease** is
    a **neurodegenerative disorder** characterized by **dopaminergic
    neuron loss** in the **substantia nigra**, but it is **also**
    associated with **degeneration** of the **cholinergic pontine
    nuclei** — including the **laterodorsal tegmental nucleus** and the
    **pedunculopontine nucleus** — this **cholinergic degeneration**
    **contributes** to the **gait**, **postural**, **sleep**, and
    **cognitive** symptoms of **Parkinson's disease**.

*   **Schizophrenia — LDT Involvement:** **Schizophrenia** has been
    **associated** with **cholinergic dysfunction** — including
    **dysregulation** of the **cholinergic pontine nuclei** (the
    **LDT** and the **PPN**) — the **LDT's cholinergic** projections to
    the **thalamus** and the **basal forebrain** **contribute** to the
    **arousal**, **attention**, and **cognitive** functions that are
    **impaired** in **schizophrenia**.

*   **Alzheimer's Disease — LDT Involvement:** **Alzheimer's disease** is
    characterized by **loss of cholinergic basal forebrain neurons** and
    **loss of cholinergic pontine neurons** — including the
    **laterodorsal tegmental nucleus** and the **pedunculopontine
    nucleus** — this **cholinergic degeneration** **contributes** to the
    **cognitive** and **sleep** symptoms of **Alzheimer's disease**.

*   **Pontine Stroke — LDT Involvement:** A **pontine stroke** (e.g.
    **basilar artery** perforator territory) involving the **LDT**
    causes **REM-sleep dysregulation** (impaired REM-sleep
    **cholinergic** activation) and **arousal dysfunction** —
    often accompanied by **other pontine signs** (**hemiparesis**,
    **facial palsy**, **abducens palsy**, **cerebellar ataxia**).

*   **No Named "LDT Syndrome":** The laterodorsal tegmental nucleus is a
    **neurochemically heterogeneous neuromodulatory nucleus** — it has
    **no named clinical syndrome** of its own. Its clinical relevance is
    **REM-sleep and arousal specific** — **REM sleep behavior
    disorder**, **narcolepsy**, **Parkinson's disease**, **schizophrenia**,
    **Alzheimer's disease**, and **pontine stroke** are all
    **LDT-involved** conditions.

**What is NOT here:** The laterodorsal tegmental nucleus is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **acoustic neuroma** (CN VIII nerve), **vestibular neuritis**
(vestibular nerve), **labyrinthitis** (inner ear), **auditory neuropathy
spectrum disorder** (cochlear nerve or hair cell), **Wallenberg
syndrome** (lateral medulla), **internuclear ophthalmoplegia** (MLF), or
**horizontal gaze palsy** (PPRF or abducens nucleus). Its clinical
relevance is **REM-sleep and arousal specific**, via the
**cholinergic (and glutamatergic and GABAergic) modulation** it
subserves. **No named LDT syndrome exists.**

Lateralization Notes
--------------------
This is the **single** laterodorsal tegmental nucleus module. The LDT is
**bilateral in real anatomy** (left LDT and right LDT), but the tree
wires it as a **single module** — and the module carries **NO warning
at the module level**:

*   **Single Module at Tree Level — Bilateral in Real Anatomy:** The
    **laterodorsal_tegmental_nucleus** module (here) is a **single
    module** that represents the **bilateral LDT** (the left LDT and the
    right LDT). The tree does **not** split them into left/right.
    Consumers must **not** assume a left/right split exists at the tree
    level — the module is a **single, bilateral representation**.

*   **Bilateral Projections (Structural Fact, NOT a Lateralization
    Warning):** The **LDT** **projects bilaterally** to the
    **thalamus**, the **hypothalamus**, the **basal forebrain**, and the
    **brainstem** — each LDT projects to **both** left and right
    targets. **This bilateral projection** is a **structural fact** of
    the **cholinergic neuromodulatory system** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **bilateral cholinergic modulation** of REM sleep and arousal.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The LDT is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the LDT.

*   **NO Amygdala-Lateralization Warning of their own (the LDT is
    CHOLINERGIC NEUROMODULATORY, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The LDT is a
    **cholinergic neuromodulatory nucleus** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**.

**A consumer that sees "laterodorsal_tegmental_nucleus" must understand
that the module is a SINGLE, BILATERAL representation** — it is **not** a
left/right split at the tree level. The **bilateral projections** are
**structural facts**, not lateralizations. The LDT is a
**strict-single module with NO warning at the module level** — **no SLEA
warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The module represents the
    **bilateral** LDT as a **single module** — it does **not** import
    left/right containers (there are none).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/locus_coeruleus/``,
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
    ``.../medulla_oblongata/``, or any other container. The LDT's
    relationships to the **locus coeruleus**, the **nucleus incertus**,
    the **pedunculopontine nucleus**, the **pontine micturition
    center**, the **tegmental pontine reticular nucleus**, the
    **parabrachial area**, the **superior olivary complex**, the
    **cranial nerve nuclei**, the **PPRF**, the **parvocellular
    reticular nucleus**, the **pontine nuclei**, the **fourth
    ventricle**, the **midbrain tegmentum**, the **medullary
    tegmentum**, the **whole tegmentum container**, the **whole pons**,
    and the **SLEA continuum** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **cholinergic
    principal neurons**, the **glutamatergic neurons**, and the
    **GABAergic neurons** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **SINGLE MODULE — NOT bilateralized at the tree level.** The **LDT**
    is a **single module** that represents the **bilateral LDT** — the
    tree does **not** split it into left/right. Consumers must **not**
    assume a left/right split exists at the tree level.
*   **CHOLINERGIC NEUROMODULATORY NUCLEUS — NOT a motor or sensory
    relay.** The **LDT** is a **neuromodulatory nucleus** —
    **projecting diffusely** to the thalamus, the hypothalamus, the
    basal forebrain, and the brainstem. Consumers must **not** conflate
    the LDT with a motor or sensory relay.
*   **NOT the locus coeruleus — that is the NORADRENERGIC neuromodulatory
    nucleus.** The **locus coeruleus** is **noradrenergic**. Consumers
    must **not** conflate the LDT with the locus coeruleus.
*   **NOT the pedunculopontine nucleus — that is the CHOLINERGIC
    LOCOMOTION nucleus.** The **PPN** is **primarily** involved in
    **locomotion**, **REM sleep**, **arousal**, and **reward**. The
    **LDT** is **primarily** involved in **REM sleep** and **arousal**.
    **They are both cholinergic** — consumers must **not** conflate the
    LDT with the PPN.
*   **NOT the nucleus incertus, the pontine micturition center, or the
    tegmental pontine reticular nucleus — those are DIFFERENT
    neuromodulatory and autonomic nuclei.** Consumers must **not**
    conflate the LDT with any of them.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, the PPRF, or the parvocellular reticular
    nucleus — those are SEPARATE structural children of the pons.**
    Consumers must **not** conflate the LDT with any of them.
*   **NOT the pontine nuclei — those are in the BASILAR pons.**
    Consumers must **not** conflate the LDT with the pontine nuclei.
*   **NOT the whole tegmentum container — that is the PARENT.**
    Consumers must **not** conflate the LDT with the whole tegmentum.
*   **NOT the whole pons — that is the GRANDPARENT.** Consumers must
    **not** conflate the LDT with the whole pons.
*   **NOT the fourth ventricle — that is a CSF SPACE.** Consumers must
    **not** conflate the LDT with the fourth ventricle.
*   **NOT the midbrain tegmentum or the medullary tegmentum — those are
    DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate the
    LDT with the midbrain tegmentum or the medullary tegmentum.
*   **MULTIPLE FUNCTIONALLY DISTINCT NEURON POPULATIONS — cholinergic,
    glutamatergic, and GABAergic.** The **cholinergic principal
    neurons**, the **glutamatergic neurons**, and the **GABAergic
    neurons** are **prose**, not structural children. Consumers must
    **not** treat the LDT as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The LDT is **not**
    an extended-amygdala component, and it carries **no SLEA warning**.
*   **NOT the fear-output — the LDT is CHOLINERGIC NEUROMODULATORY.**
    The **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **LDT** is a **cholinergic neuromodulatory nucleus** —
    it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The LDT is a local leaf under the
    tegmentum container, not a cross-listed leaf.
*   **No nested cross-listing.** The LDT has no nested dual-framing
    module. It is a single leaf.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum import laterodorsal_tegmental_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.tegmentum."
        "laterodorsal_tegmental_nucleus"
    )

**Do not** assume the LDT is a **container**. It is a **leaf** — the
**cholinergic principal neurons**, the **glutamatergic neurons**, and the
**GABAergic neurons** are **prose**, not structural children.

**Do not** assume the LDT is **bilateralized at the tree level**. The LDT
is **bilateral in real anatomy**, but the tree wires it as a **single
module** — there is **no left/right split at the module level**.

**Do not** assume the LDT is the **locus coeruleus**. The **locus
coeruleus** is the **noradrenergic** nucleus. The **LDT** is the
**cholinergic** nucleus. They are **different structures** — different
neurotransmitters and different functional systems.

**Do not** assume the LDT is the **pedunculopontine nucleus**. Both are
**cholinergic** and **both** are **REM-sleep and arousal nuclei** — but
they are **different structures** with **different anatomical
locations** (LDT is **dorsomedial**; PPN is **ventrolateral**) and
**different functional emphases** (LDT is **primarily** REM-sleep and
arousal; PPN is **primarily** locomotion, REM-sleep, and reward).

**Do not** assume the LDT is the **nucleus incertus**, the **pontine
micturition center**, or the **tegmental pontine reticular nucleus**.
Those are **different structures** — the **nucleus incertus**
(relaxin-3 stress/arousal), the **pontine micturition center**
(micturition), and the **tegmental pontine reticular nucleus** (motor
relay).

**Do not** assume the LDT is the **parabrachial area**, the **superior
olivary complex**, the **cranial nerve nuclei**, the **PPRF**, or the
**parvocellular reticular nucleus**. Those are **separate structural
children of the pons** — even though they are anatomically located in
the pontine tegmentum.

**Do not** assume the LDT is the **pontine nuclei**. The **pontine
nuclei** are in the **basilar pons** — the LDT is in the **dorsal
pontine tegmentum**.

**Do not** assume the LDT is the **whole tegmentum** or the **whole
pons**. The **tegmentum** is the **parent**; the **pons** is the
**grandparent**.

**Do not** assume the LDT is the **fourth ventricle**. The **fourth
ventricle** is a **CSF space**; the **LDT** is **neural tissue**.

**Do not** assume the LDT is the **midbrain tegmentum** or the **medullary
tegmentum**. Those are **different brainstem levels**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the LDT. **The LDT is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT part of the fear circuit**.

Iterating the LDT's (empty) children (recommended consumer pattern)::

    LATERODORSAL_TEGMENTAL_NUCLEUS_CHILDREN = ()
    # The LDT is a leaf. The cholinergic principal neurons, the
    # glutamatergic neurons, and the GABAergic neurons are prose, not
    # modules.

Reaching the locus coeruleus (recommended consumer pattern — the
noradrenergic sibling)::

    # The locus coeruleus is the NORADRENERGIC sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/locus_coeruleus/
    #
    # The locus coeruleus is noradrenergic; the LDT is cholinergic. They
    # are ANATOMICALLY ADJACENT but FUNCTIONALLY DISTINCT.

Reaching the pedunculopontine nucleus (recommended consumer pattern —
the cholinergic locomotion sibling)::

    # The pedunculopontine nucleus is the CHOLINERGIC LOCOMOTION sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pedunculopontine_nucleus/
    #
    # The PPN is primarily involved in locomotion, REM sleep, arousal,
    # and reward; the LDT is primarily involved in REM sleep and arousal.
    # They are BOTH cholinergic — but DIFFERENT STRUCTURES with
    # DIFFERENT anatomical locations and functional emphases.

Reaching the nucleus incertus (recommended consumer pattern — the
relaxin-3 sibling)::

    # The nucleus incertus is the RELAXIN-3-EXPRESSING sibling under the
    # tegmentum container:
    #
    #   .../pons/tegmentum/nucleus_incertus/
    #
    # The nucleus incertus is involved in stress, arousal, feeding, and
    # neuroendocrine regulation; the LDT is involved in REM sleep and
    # arousal.

Reaching the pontine micturition center (recommended consumer pattern —
the micturition sibling)::

    # The pontine micturition center is the MICTURITION CONTROL sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/pontine_micturition_center/
    #
    # The pontine micturition center coordinates the micturition reflex;
    # the LDT is involved in REM sleep and arousal.

Reaching the tegmental pontine reticular nucleus (recommended consumer
pattern — the motor relay sibling)::

    # The tegmental pontine reticular nucleus is the MOTOR RELAY sibling
    # under the tegmentum container:
    #
    #   .../pons/tegmentum/tegmental_pontine_reticular_nucleus/
    #
    # The tegmental pontine reticular nucleus is involved in locomotion,
    # posture, and motor pattern generation; the LDT is involved in REM
    # sleep and arousal.

Reaching the parabrachial area (recommended consumer pattern — a
SEPARATE pons child)::

    # The parabrachial area is a SEPARATE STRUCTURAL CHILD of the pons:
    #
    #   .../pons/parabrachial_area/
    #
    # The parabrachial area is the visceral-sensory and respiratory-relay
    # complex; the LDT is a cholinergic neuromodulatory nucleus.

Reaching the whole tegmentum container (recommended consumer pattern —
the PARENT)::

    # The tegmentum container is the DORSAL PONTINE GREY-MATTER REGION
    # that CONTAINS the LDT as one of its six structural children:
    #
    #   .../pons/tegmentum/
    #
    # The LDT is a CHILD of the tegmentum container.

Reaching the whole pons (recommended consumer pattern — the
GRANDPARENT)::

    # The pons is the WHOLE METENCEPHALIC BRAINSTEM SEGMENT that CONTAINS
    # the tegmentum container:
    #
    #   .../pons/
    #
    # The LDT is a GRANDCHILD of the pons.

Bilateral iteration (recommended consumer pattern)::

    # The LDT is a SINGLE module (not bilateralized at the tree level).
    # The module represents the BILATERAL LDT.
    ldt_path = (
        "hindbrain.metencephalon.pons.tegmentum."
        "laterodorsal_tegmental_nucleus"
    )
    # resolve ldt_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The LDT's neuron populations are prose, not modules:
    #   cholinergic principal neurons -> project to the thalamus,
    #       hypothalamus, basal forebrain, and brainstem; the cholinergic
    #       component of REM sleep and arousal
    #   glutamatergic neurons -> project to the thalamus, hypothalamus,
    #       basal forebrain, and brainstem (in some cases co-releasing
    #       glutamate with acetylcholine, or projecting independently);
    #       the glutamatergic component of REM sleep and arousal
    #   GABAergic neurons -> modulate the local circuit and the
    #       cholinergic/glutamatergic output; the GABAergic component of
    #       REM-sleep and arousal regulation
    #
    # Do not attempt to resolve these as sub-paths of the LDT — resolve
    # them at the neuron-population level through the references.

References
----------
*   **Canonical LDT anatomy:** Mesulam, M.M., Mufson, E.J., Wainer,
    B.H., Levey, A.I. (1983). "Central cholinergic pathways in the rat:
    an overview based on an alternative nomenclature (Ch1-Ch6)."
    *Neuroscience* 10:1185–1201. (Laterodorsal tegmental nucleus —
    cholinergic brainstem nucleus.)
*   **Laterodorsal tegmental nucleus — modern review:** Woolf, N.J.,
    Butcher, L.L. (2011). "Cholinergic systems mediate action from
    movement to consciousness." *Behavioural Brain Research*
    221:488–498. (LDT — cholinergic REM-sleep and arousal functions.)
*   **REM sleep — cholinergic mechanisms:** Steriade, M., McCarley,
    R.W. (2005). *Brain Control of Wakefulness and Sleep*, 2nd ed.
    (Cholinergic REM-sleep mechanisms — the LDT and PPN.)
*   **Pedunculopontine nucleus and LDT — cholinergic arousal:**
    Garcia-Rill, E. (1991). "The pedunculopontine nucleus." *Progress
    in Neurobiology* 36:363–389. (Pedunculopontine nucleus and
    laterodorsal tegmental nucleus — cholinergic arousal, locomotion,
    and REM sleep.)
*   **Cholinergic basal forebrain arousal:** Jones, B.E. (2008).
    "Modulation of cortical activation and behavioral arousal by
    cholinergic and orexinergic systems." *Annals of the New York
    Academy of Sciences* 1129:26–34. (Cholinergic basal forebrain
    arousal — the LDT's projection to the basal forebrain.)
*   **REM sleep behavior disorder:** Boeve, B.F., Silber, M.H., Ferman,
    T.J., et al. (2001). "Association of REM sleep behavior disorder and
    neurodegenerative disease may reflect an underlying
    synucleinopathy." *Movement Disorders* 16:622–630. (REM sleep
    behavior disorder — pontine REM-sleep nuclei involvement, including
    the LDT.)
*   **Narcolepsy — cholinergic dysregulation:** Nishino, S., Ripley,
    B., Overeem, S., Lammers, G.J., Mignot, E. (2000). "Hypocretin
    (orexin) deficiency in human narcolepsy." *Lancet* 355:39–40.
    (Narcolepsy — orexin deficiency; cholinergic REM-sleep
    dysregulation.)
*   **Parkinson's disease — cholinergic pontine degeneration:** Hirsch,
    E.C., Graybiel, A.M., Duyckaerts, C., Javoy-Agid, F. (1987).
    "Neuronal loss in the pedunculopontine tegmental nucleus in
    Parkinson disease and in progressive supranuclear palsy."
    *Proceedings of the National Academy of Sciences* 84:5976–5980.
    (Parkinson's disease — cholinergic pontine nuclei degeneration,
    including the LDT and PPN.)
*   **Schizophrenia — cholinergic dysfunction:** Raedler, T.J., Knable,
    M.B., Jones, D.W., et al. (2003). "In vivo determination of
    muscarinic receptor availability in schizophrenia." *American
    Journal of Psychiatry* 160:118–125. (Schizophrenia — cholinergic
    dysfunction; the LDT's projections to the thalamus and the basal
    forebrain.)
*   **Alzheimer's disease — cholinergic pontine degeneration:** Mufson,
    E.J., Ginsberg, S.D., Ikonomovic, M.D., DeKosky, S.T. (2003).
    "Human cholinergic basal forebrain: chemoanatomy and neurologic
    dysfunction." *Journal of Chemical Neuroanatomy* 26:233–242.
    (Alzheimer's disease — cholinergic basal forebrain and pontine
    degeneration, including the LDT.)
*   **Pontine stroke — LDT involvement:** Bassetti, C., Bogousslavsky,
    J., Barth, A., Regli, F. (1996). "Isolated infarcts of the pontine
    nuclei: a clinical and neuroimaging study." *Brain*
    119:1237–1253. (Pontine stroke — pontine tegmentum involvement,
    including the LDT.)
*   **Locus coeruleus (contrast — the NORADRENERGIC neuromodulatory
    sibling):** Aston-Jones, G., Cohen, J.D. (2005). "An integrative
    theory of locus coeruleus-norepinephrine function: adaptive gain and
    optimal performance." *Annual Review of Neuroscience* 28:403–450.
    (Locus coeruleus — noradrenergic neuromodulatory nucleus; sibling of
    the LDT.)
*   **Pedunculopontine nucleus (contrast — the CHOLINERGIC LOCOMOTION
    sibling):** Garcia-Rill, E. (1991). "The pedunculopontine nucleus."
    *Progress in Neurobiology* 36:363–389. (PPN — cholinergic locomotion
    and REM-sleep nucleus; sibling of the LDT.)
*   **Nucleus incertus (contrast — the RELAXIN-3 sibling):** Ryan, P.J.,
    Ma, S., Olucha-Bordonau, F.E., Gundlach, A.L. (2011). "Nucleus
    incertus — an emerging role in the behavioural actions of
    relaxin-3." *British Journal of Pharmacology* 162:1115–1126.
    (Nucleus incertus — relaxin-3 stress, arousal, and feeding; sibling
    of the LDT.)
*   **Pontine micturition center (contrast — the MICTURITION sibling):**
    Barrington, F.J.F. (1925). "The effect of lesions of the hind- and
    mid-brain on micturition in the cat." *Quarterly Journal of
    Experimental Physiology* 15:81–102. (Pontine micturition center —
    micturition control; sibling of the LDT.)
*   **Tegmental pontine reticular nucleus (contrast — the MOTOR RELAY
    sibling):** Brodal, A. (2010). *The Central Nervous System: Structure
    and Function*, 4th ed. (Tegmental pontine reticular nucleus — motor
    relay; sibling of the LDT.)
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
    pons; distinct from the LDT.)
*   **Fourth ventricle (contrast — a CSF space):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Fourth ventricle — CSF space dorsal to the pons; distinct from the
    LDT.)
*   **Midbrain tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Midbrain tegmentum — dorsal midbrain; distinct
    from the pontine tegmentum.)
*   **Medullary tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary tegmentum — dorsal medulla; distinct
    from the pontine tegmentum.)
*   **SLEA (contrast — the LDT is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the LDT.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the LDT.)
*   NeuroNames — Laterodorsal tegmental nucleus; FMA — Laterodorsal
    tegmental nucleus.
"""
