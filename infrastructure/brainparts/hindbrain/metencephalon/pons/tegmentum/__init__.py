"""
infrastructure.brainparts.hindbrain.metencephalon.pons.tegmentum
===============================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── tegmentum   <-- THIS MODULE
                ├── laterodorsal_tegmental_nucleus
                ├── locus_coeruleus
                ├── nucleus_incertus
                ├── pedunculopontine_nucleus
                ├── pontine_micturition_center
                └── tegmental_pontine_reticular_nucleus

**Primary synonym:** Pontine tegmentum; dorsal pons; pontine tegmentum
(tree sub-container); "the pontine neuromodulatory and autonomic
tegmentum."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter region** — the **dorsal pontine tegmentum**, the
**ventral-most portion of the pons** (dorsal to the basilar pons and
ventral to the fourth ventricle), **tree-wired as a container** for six
**neuromodulatory and autonomic nuclei**.
**Part of:** The **pons** container — specifically, the **dorsal
tegmental** component. The **pons** is the **metencephalic** brainstem
segment; the **tegmentum** is its **dorsal grey-matter region**.
**Structural parent:** ``.../pons/`` → **direct child** of the pons
container.
**Structural children:** **Six structural children** — the
``laterodorsal_tegmental_nucleus``, the ``locus_coeruleus``, the
``nucleus_incertus``, the ``pedunculopontine_nucleus``, the
``pontine_micturition_center``, and the
``tegmental_pontine_reticular_nucleus``. Each is itself a **leaf** at
the tree level.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
pontine tegmentum is a CONTAINER, not a leaf.** It has **six structural
children** (the six neuromodulatory and autonomic nuclei). Consumers
must **not** treat the pontine tegmentum as a leaf, and must **not**
assume the six nuclei are absent — they are the **direct structural
children** of the pontine tegmentum.
**Boundary status (TREE-WIRED SUBSET — NOT the whole anatomical pontine
tegmentum):** **Boundary case — the pontine tegmentum is a TREE-WIRED
SUBSET, NOT the whole anatomical pontine tegmentum.** The **anatomical
pontine tegmentum** includes **many more structures** than the six
neuromodulatory and autonomic nuclei wired here — it also includes the
**parabrachial area**
(``.../pons/parabrachial_area/``), the **superior olivary complex**
(``.../pons/superior_olivary_complex/``), the **cranial nerve nuclei**
(``.../pons/cranial_nerve_nuclei/``), the **paramedian pontine reticular
formation (PPRF)**
(``.../pons/paramedian_pontine_reticular_formation/``), the
**parvocellular reticular nucleus**
(``.../pons/parvocellular_reticular_nucleus/``), the **caudal pontine
reticular nucleus**, the **oral pontine reticular nucleus**, the
**mesencephalic trigeminal nucleus** (via the midbrain), the **medial
lemniscus** (white matter), the **central tegmental tract** (white
matter), and the **pontine reticular formation** more broadly. **The
tree splits these into separate containers under the pons** — the
**parabrachial area**, the **superior olivary complex**, the **cranial
nerve nuclei**, the **PPRF**, the **parvocellular reticular nucleus**,
and the **pontine nuclei** are **separate structural children of the
pons** — **not** structural children of the pontine tegmentum. The
**pontine tegmentum** (here) is therefore a **narrower, tree-specific
sub-container** for the six **neuromodulatory and autonomic nuclei**.
Consumers must **not** assume that "pontine tegmentum" (the anatomical
region) equals "tegmentum" (the tree container) — the tree's
**tegmentum** is a **subset** of the anatomical pontine tegmentum.
**Boundary status (NOT the basilar pons — that is the VENTRAL PONS,
TREE-WIRED AS SEPARATE STRUCTURES):** **Boundary case — the pontine
tegmentum is NOT the basilar pons; the basilar pons is the VENTRAL PONS,
TREE-WIRED AS SEPARATE STRUCTURES.** The **basilar pons** is the
**ventral portion of the pons** — it contains the **pontine nuclei**
(``.../pons/pontine_nuclei/``), the **corticospinal tract**
(``.../white_matter/.../corticospinal_tract/``), the **corticobulbar
tract** (``.../white_matter/.../corticobulbar_tract/``), and the
**transverse pontine fibers** that form the **middle cerebellar
peduncle**. The **pontine tegmentum** (here) is the **dorsal portion** —
it contains the **neuromodulatory and autonomic nuclei** wired as
structural children. They are **DIFFERENT PONTS SUB-DIVISIONS** — the
**basilar pons** is **ventral** and **white-matter-rich**; the
**pontine tegmentum** is **dorsal** and **grey-matter-rich**. **This
dorsal/ventral distinction is a classic source of confusion** —
consumers must **not** conflate the pontine tegmentum with the basilar
pons or with the pontine nuclei.
**Boundary status (NOT the parabrachial area — that is a SEPARATE
STRUCTURAL CHILD of the pons, not the pontine tegmentum):** **Boundary
case — the pontine tegmentum is NOT the parabrachial area.** The
**parabrachial area** (``.../pons/parabrachial_area/``) is the
**visceral-sensory and respiratory-relay complex** — it is a **separate
structural child of the pons**, **not** a structural child of the
pontine tegmentum, **even though** it is **anatomically located** in
the **pontine tegmentum**. **The tree splits the parabrachial area from
the pontine tegmentum container** — consumers must **not** conflate the
pontine tegmentum with the parabrachial area.
**Boundary status (NOT the superior olivary complex — that is a
SEPARATE STRUCTURAL CHILD of the pons):** **Boundary case — the pontine
tegmentum is NOT the superior olivary complex.** The **superior olivary
complex** (``.../pons/superior_olivary_complex/``) is the **pontine
binaural sound-localization relay** — it is a **separate structural
child of the pons**, **not** a structural child of the pontine
tegmentum, **even though** it is **anatomically located** in the
**ventral pontine tegmentum**. **The tree splits the superior olivary
complex from the pontine tegmentum container** — consumers must **not**
conflate the pontine tegmentum with the superior olivary complex.
**Boundary status (NOT the cranial nerve nuclei — those are a SEPARATE
STRUCTURAL CHILD of the pons):** **Boundary case — the pontine
tegmentum is NOT the cranial nerve nuclei.** The **cranial nerve
nuclei** (``.../pons/cranial_nerve_nuclei/``) are the **CN V, VI, VII,
VIII nuclei** — they are a **separate structural child of the pons**,
**not** a structural child of the pontine tegmentum, **even though**
they are **anatomically located** in the **pontine tegmentum**. **The
tree splits the cranial nerve nuclei from the pontine tegmentum
container** — consumers must **not** conflate the pontine tegmentum with
the cranial nerve nuclei.
**Boundary status (NOT the PPRF or the parvocellular reticular nucleus —
those are SEPARATE STRUCTURAL CHILDREN of the pons):** **Boundary case —
the pontine tegmentum is NOT the paramedian pontine reticular formation
(PPRF) or the parvocellular reticular nucleus.** The **PPRF**
(``.../pons/paramedian_pontine_reticular_formation/``) is the
**horizontal saccadic burst generator**; the **parvocellular reticular
nucleus** (``.../pons/parvocellular_reticular_nucleus/``) is the
**orofacial premotor and autonomic relay**. Both are **separate
structural children of the pons** — **not** structural children of the
pontine tegmentum — **even though** they are **anatomically located**
in the **pontine tegmentum**. **The tree splits them from the pontine
tegmentum container** — consumers must **not** conflate the pontine
tegmentum with the PPRF or with the parvocellular reticular nucleus.
**Boundary status (NOT the pontine nuclei — those are in the BASILAR
PONS):** **Boundary case — the pontine tegmentum is NOT the pontine
nuclei.** The **pontine nuclei** (``.../pons/pontine_nuclei/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons** — the
**ventral** portion of the pons. The **pontine tegmentum** (here) is
the **dorsal** portion of the pons. They are **DIFFERENT PONTS
SUB-DIVISIONS** — consumers must **not** conflate the pontine tegmentum
with the pontine nuclei.
**Boundary status (NOT the fourth ventricle — that is a CSF SPACE
dorsal to the pons):** **Boundary case — the pontine tegmentum is NOT
the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the **CSF-filled space**
**dorsal to** the pons and **ventral to** the cerebellum. The **pontine
tegmentum** (here) is the **grey-matter region** that **forms the
floor** of the fourth ventricle. They are **DIFFERENT STRUCTURES** — the
**fourth ventricle** is a **fluid space**; the **pontine tegmentum** is
**neural tissue**. Consumers must **not** conflate the pontine tegmentum
with the fourth ventricle.
**Boundary status (NOT the cerebellum — that is the metencephalic
SIBLING):** **Boundary case — the pontine tegmentum is NOT the
cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is the **metencephalic cerebellar
half** — it is **dorsal to** the fourth ventricle, and it is
**functionally distinct** from the pontine tegmentum. The **pontine
tegmentum** (here) is the **dorsal pontine grey-matter region**. They
are **DIFFERENT STRUCTURES** — consumers must **not** conflate the
pontine tegmentum with the cerebellum.
**Boundary status (NOT the midbrain tegmentum — that is a MIDBRAIN
structure):** **Boundary case — the pontine tegmentum is NOT the
midbrain tegmentum.** The **midbrain tegmentum**
(``.../midbrain/tegmentum/``) is the **dorsal portion of the midbrain**
— it contains the **periaqueductal gray**, the **red nucleus**, the
**substantia nigra** (pars compacta and pars reticulata), the **ventral
tegmental area**, the **oculomotor nucleus**, the **trochlear nucleus**,
the **mesencephalic trigeminal nucleus**, the **rostral interstitial
nucleus of the MLF (riMLF)**, the **central mesencephalic reticular
formation (cMRF)**, and other **midbrain structures**. The **pontine
tegmentum** (here) is the **dorsal portion of the pons** — a **different
brainstem level**. They are **DIFFERENT STRUCTURES** — consumers must
**not** conflate the pontine tegmentum with the midbrain tegmentum.
**Boundary status (NOT the medullary tegmentum — that is a MEDULLARY
structure):** **Boundary case — the pontine tegmentum is NOT the
medullary tegmentum.** The **medullary tegmentum** is the **dorsal
portion of the medulla oblongata** — it contains the **solitary
nucleus**, the **dorsal motor nucleus of the vagus**, the **hypoglossal
nucleus**, the **nucleus ambiguus**, the **inferior olivary nucleus**,
the **gigantocellular reticular nucleus**, the **paramedian reticular
nucleus**, and other **medullary structures**. The **pontine tegmentum**
(here) is the **dorsal portion of the pons** — a **different brainstem
level**. They are **DIFFERENT STRUCTURES** — consumers must **not**
conflate the pontine tegmentum with the medullary tegmentum.
**Boundary status (GREY-MATTER REGION — NOT the white-matter tracts that
traverse it):** **Boundary case — the pontine tegmentum is the
GREY-MATTER REGION, NOT the white-matter tracts that traverse it.** The
**pontine tegmentum** contains **grey-matter nuclei** (the six
neuromodulatory and autonomic nuclei) **and** traversing **white-matter
tracts** — including the **medial longitudinal fasciculus (MLF)**, the
**medial lemniscus**, the **central tegmental tract**, the **lateral
lemniscus**, the **descending trigeminal tract**, the **spinothalamic
tract**, the **rubrospinal tract**, and the **tectospinal tract**. **The
tree wires the pontine tegmentum as a container for the GREY-MATTER
NUCLEI** — the traversing **white-matter tracts** are documented as
**prose and boundary data**, not as structural children. Consumers must
**not** conflate the pontine tegmentum with the white-matter tracts that
traverse it.
**Boundary status (NOT a single uniform functional system — MULTIPLE
nuclei with DIFFERENT functions):** **Boundary case — the pontine
tegmentum is a HETEROGENEOUS collection of SIX neuromodulatory and
autonomic nuclei with DIFFERENT functions, not a single uniform
system.** The **locus coeruleus** is **noradrenergic** (arousal,
attention, stress, pain modulation). The **laterodorsal tegmental
nucleus** and the **pedunculopontine nucleus** are **cholinergic**
(REM sleep, arousal, locomotion). The **nucleus incertus** is
**relaxin-3-expressing** (stress, arousal, feeding). The **pontine
micturition center** (Barrington's nucleus) is the **micturition control
center** (bladder contraction). The **tegmental pontine reticular
nucleus** is a **motor relay** (reticulospinal projections, locomotion).
**Each nucleus is functionally distinct** — the tree wires them as
**separate structural children**. Consumers must **not** treat the
pontine tegmentum as a single uniform system — it is a **distributed
collection** of functionally distinct nuclei.
**Boundary status (SLEA-FREE — the pontine tegmentum is NOT an
extended-amygdala component):** **Boundary case — the pontine tegmentum
is SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus**
(the **only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired elsewhere). The
**pontine tegmentum** is the **dorsal pontine grey-matter region** — it
is **NOT** an extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into the
pontine tegmentum — it is **SLEA-free**.

Overview
--------
The pontine tegmentum is the **dorsal pontine grey-matter region** — the
**tree-wired container** for **six neuromodulatory and autonomic
nuclei** in the **dorsal pons**. It is a **container** under the pons
container, with **six structural children** — the **laterodorsal
tegmental nucleus**, the **locus coeruleus**, the **nucleus incertus**,
the **pedunculopontine nucleus**, the **pontine micturition center**,
and the **tegmental pontine reticular nucleus** — each of which is a
**leaf** at the tree level.

**The pontine tegmentum is a CONTAINER, NOT a leaf.** Its structural
children are the **six neuromodulatory and autonomic nuclei**.

**The pontine tegmentum is a TREE-WIRED SUBSET, NOT the whole anatomical
pontine tegmentum.** The **anatomical pontine tegmentum** includes many
more structures (the parabrachial area, the superior olivary complex,
the cranial nerve nuclei, the PPRF, the parvocellular reticular nucleus,
the caudal and oral pontine reticular nuclei, the medial lemniscus, the
MLF, and others). **The tree splits these into separate containers
under the pons** — the **pontine tegmentum** (here) is a **narrower,
tree-specific sub-container** for the six **neuromodulatory and
autonomic nuclei**. Consumers must **not** assume that "pontine
tegmentum" (the anatomical region) equals "tegmentum" (the tree
container) — the tree's **tegmentum** is a **subset** of the anatomical
pontine tegmentum.

**The pontine tegmentum is GREY-MATTER, NOT the white-matter tracts that
traverse it.** The **grey-matter nuclei** are the six structural
children. The traversing **white-matter tracts** (MLF, medial lemniscus,
central tegmental tract, lateral lemniscus, etc.) are documented as
**prose and boundary data**, not as structural children.

**The pontine tegmentum is NOT the basilar pons, the parabrachial area,
the superior olivary complex, the cranial nerve nuclei, the PPRF, the
parvocellular reticular nucleus, the pontine nuclei, the fourth
ventricle, the cerebellum, the midbrain tegmentum, or the medullary
tegmentum.** Those are **different structures** — the **basilar pons**
(ventral pons), the **parabrachial area** (visceral-sensory and
respiratory relay), the **superior olivary complex** (binaural
sound-localization relay), the **cranial nerve nuclei** (CN V, VI, VII,
VIII nuclei), the **PPRF** (horizontal saccadic burst generator), the
**parvocellular reticular nucleus** (orofacial premotor and autonomic
relay), the **pontine nuclei** (cortico-ponto-cerebellar relay in the
basilar pons), the **fourth ventricle** (CSF space), the **cerebellum**
(metencephalic sibling), the **midbrain tegmentum** (midbrain dorsal
region), and the **medullary tegmentum** (medullary dorsal region). The
**pontine tegmentum** (here) is a **specific tree-wired sub-container**
for the **six neuromodulatory and autonomic nuclei**.

**The pontine tegmentum is HETEROGENEOUS.** The six nuclei are
**functionally distinct** — **locus coeruleus** (noradrenergic arousal),
**laterodorsal tegmental nucleus** and **pedunculopontine nucleus**
(cholinergic REM/arousal/locomotion), **nucleus incertus** (relaxin-3
stress/arousal), **pontine micturition center** (micturition), and
**tegmental pontine reticular nucleus** (motor relay). The tree wires
them as **separate structural children**.

**The pontine tegmentum is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Sub-Nucleus Composition (structural children, prose)
----------------------------------------------------
The pontine tegmentum contains **six neuromodulatory and autonomic
nuclei** — documented as **structural children** (not as leaves of the
pontine tegmentum):

*   **Locus coeruleus**
    (``.../tegmentum/locus_coeruleus/``) — the **noradrenergic
    nucleus** — the **principal source of norepinephrine** in the brain.
    It **projects diffusely** to the **entire forebrain**, the
    **brainstem**, and the **spinal cord** — it is involved in
    **arousal**, **attention**, **stress**, **pain modulation**, and
    **memory consolidation**. **Noradrenergic arousal and neuromodulation
    are the functional systems** subserved primarily by the locus
    coeruleus.

*   **Laterodorsal tegmental nucleus**
    (``.../tegmentum/laterodorsal_tegmental_nucleus/``) — the
    **cholinergic nucleus** (with **glutamatergic** and **GABAergic**
    components) — it **projects** to the **thalamus**, the
    **hypothalamus**, the **basal forebrain**, and the **brainstem** —
    it is involved in **REM sleep** (cholinergic activation of the
    thalamus during REM), **arousal**, and **motivation**. **REM sleep
    and cholinergic arousal are the functional systems** subserved
    primarily by the laterodorsal tegmental nucleus.

*   **Nucleus incertus**
    (``.../tegmentum/nucleus_incertus/``) — the **relaxin-3-expressing
    nucleus** — it **projects** to the **septum**, the **hippocampus**,
    the **medial prefrontal cortex**, the **amygdala**, the
    **hypothalamus**, and the **brainstem** — it is involved in
    **stress**, **arousal**, **feeding**, and **neuroendocrine
    regulation**. **Relaxin-3 stress and arousal modulation are the
    functional systems** subserved primarily by the nucleus incertus.

*   **Pedunculopontine nucleus**
    (``.../tegmentum/pedunculopontine_nucleus/``) — the
    **cholinergic** (with **glutamatergic** and **GABAergic** components)
    nucleus — it **projects** to the **basal ganglia**, the
    **thalamus**, the **hypothalamus**, the **brainstem**, and the
    **spinal cord** — it is involved in **locomotion** (the
    **mesencephalic locomotor region** — with the **cuneiform
    nucleus**), **REM sleep**, **arousal**, and **reward**. **Locomotion
    and cholinergic arousal are the functional systems** subserved
    primarily by the pedunculopontine nucleus.

*   **Pontine micturition center** (Barrington's nucleus)
    (``.../tegmentum/pontine_micturition_center/``) — the
    **micturition control center** — it **projects** to the
    **sacral spinal cord** (the **Onuf's nucleus** and the
    **parasympathetic preganglionic neurons** of the **bladder**) —
    it **coordinates** the **micturition reflex** (bladder
    **contraction** and **sphincter relaxation**). **Micturition
    control is the functional system** subserved primarily by the
    pontine micturition center.

*   **Tegmental pontine reticular nucleus**
    (``.../tegmentum/tegmental_pontine_reticular_nucleus/``) — the
    **motor relay** — it **projects** to the **spinal cord** (via the
    **reticulospinal tract**) and to the **cerebellum** (via the
    **pontocerebellar fibers**) — it is involved in **locomotion**,
    **posture**, and **motor pattern generation**. **Reticulospinal
    motor relay is the functional system** subserved primarily by the
    tegmental pontine reticular nucleus.

**These nuclei are structural children of the pontine tegmentum.** The
pontine tegmentum's **structural children** are the **six
neuromodulatory and autonomic nuclei**; each is itself a **leaf** at the
tree level with its own **prose neuron populations and projection
targets**. Consumers resolving sub-nucleus detail go **through** the six
structural children.

The Pontine Tegmentum / Pons Boundary
-------------------------------------
This is the **sub-container vs. parent** boundary:

*   **Pontine tegmentum** (this module) — the **dorsal pontine
    grey-matter region** — the **tree-wired container** for the **six
    neuromodulatory and autonomic nuclei**.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine tegmentum**
    (here), the **parabrachial area**, the **superior olivary complex**,
    the **cranial nerve nuclei**, the **PPRF**, the **parvocellular
    reticular nucleus**, the **pontine nuclei**, and other structures.

**The pontine tegmentum is a child of the pons.** Consumers must **not**
conflate the pontine tegmentum with the **whole pons**.

The Pontine Tegmentum / Basilar Pons Boundary
---------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Pontine tegmentum** (this module) — the **dorsal pontine
    grey-matter region**.

*   **Basilar pons** — the **ventral pontine region** that contains the
    **pontine nuclei**, the **corticospinal tract**, the
    **corticobulbar tract**, and the **transverse pontine fibers** that
    form the **middle cerebellar peduncle**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — the **basilar pons** is
**ventral** and **white-matter-rich**; the **pontine tegmentum** is
**dorsal** and **grey-matter-rich**. **This dorsal/ventral distinction
is a classic source of confusion** — consumers must **not** conflate the
pontine tegmentum with the basilar pons or with the pontine nuclei.

The Pontine Tegmentum / Parabrachial Area Boundary
--------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pontine tegmentum** (this module) — the **tree-wired container**
    for the **six neuromodulatory and autonomic nuclei**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral-sensory and respiratory-relay complex** — it is a
    **separate structural child of the pons**, **not** a structural
    child of the pontine tegmentum, **even though** it is **anatomically
    located** in the **pontine tegmentum**.

**The tree splits the parabrachial area from the pontine tegmentum
container** — consumers must **not** conflate the pontine tegmentum with
the parabrachial area.

The Pontine Tegmentum / Superior Olivary Complex Boundary
---------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pontine tegmentum** (this module) — the **tree-wired container**
    for the **six neuromodulatory and autonomic nuclei**.

*   **Superior olivary complex** (``.../pons/superior_olivary_complex/``)
    — the **pontine binaural sound-localization relay** — it is a
    **separate structural child of the pons**, **not** a structural
    child of the pontine tegmentum, **even though** it is **anatomically
    located** in the **ventral pontine tegmentum**.

**The tree splits the superior olivary complex from the pontine
tegmentum container** — consumers must **not** conflate the pontine
tegmentum with the superior olivary complex.

The Pontine Tegmentum / Cranial Nerve Nuclei Boundary
-----------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pontine tegmentum** (this module) — the **tree-wired container**
    for the **six neuromodulatory and autonomic nuclei**.

*   **Cranial nerve nuclei** (``.../pons/cranial_nerve_nuclei/``) — the
    **CN V, VI, VII, VIII nuclei** — they are a **separate structural
    child of the pons**, **not** a structural child of the pontine
    tegmentum, **even though** they are **anatomically located** in the
    **pontine tegmentum**.

**The tree splits the cranial nerve nuclei from the pontine tegmentum
container** — consumers must **not** conflate the pontine tegmentum with
the cranial nerve nuclei.

The Pontine Tegmentum / PPRF and Parvocellular Reticular Nucleus Boundary
-------------------------------------------------------------------------
This is the **tree-wiring vs. anatomical location** boundary:

*   **Pontine tegmentum** (this module) — the **tree-wired container**
    for the **six neuromodulatory and autonomic nuclei**.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/paramedian_pontine_reticular_formation/``) — the
    **horizontal saccadic burst generator**.

*   **Parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``) — the **orofacial
    premotor and autonomic relay**.

**Both the PPRF and the parvocellular reticular nucleus are separate
structural children of the pons** — **not** structural children of the
pontine tegmentum — **even though** they are **anatomically located** in
the **pontine tegmentum**. **The tree splits them from the pontine
tegmentum container** — consumers must **not** conflate the pontine
tegmentum with the PPRF or with the parvocellular reticular nucleus.

The Pontine Tegmentum / Pontine Nuclei Boundary
-----------------------------------------------
This is the **dorsal vs. ventral pons** boundary:

*   **Pontine tegmentum** (this module) — the **dorsal pontine
    grey-matter region**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT PONTS SUB-DIVISIONS** — consumers must **not**
conflate the pontine tegmentum with the pontine nuclei.

The Pontine Tegmentum / Fourth Ventricle Boundary
-------------------------------------------------
This is the **neural tissue vs. CSF space** boundary:

*   **Pontine tegmentum** (this module) — the **grey-matter region**
    that forms the **floor of the fourth ventricle**.

*   **Fourth ventricle** (``.../metencephalon/fourth_ventricle/``) — the
    **CSF-filled space** **dorsal to** the pons and **ventral to** the
    cerebellum.

**They are DIFFERENT STRUCTURES** — the **fourth ventricle** is a
**fluid space**; the **pontine tegmentum** is **neural tissue**.
Consumers must **not** conflate the pontine tegmentum with the fourth
ventricle.

The Pontine Tegmentum / Cerebellum Boundary
-------------------------------------------
This is the **pons vs. cerebellum** boundary:

*   **Pontine tegmentum** (this module) — the **dorsal pontine
    grey-matter region**.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the
    **metencephalic cerebellar half**.

**They are DIFFERENT STRUCTURES** — consumers must **not** conflate the
pontine tegmentum with the cerebellum.

The Pontine Tegmentum / Midbrain Tegmentum Boundary
---------------------------------------------------
This is the **pons vs. midbrain** boundary:

*   **Pontine tegmentum** (this module) — the **dorsal portion of the
    pons**.

*   **Midbrain tegmentum** (``.../midbrain/tegmentum/``) — the **dorsal
    portion of the midbrain** — it contains the **periaqueductal gray**,
    the **red nucleus**, the **substantia nigra** (pars compacta and
    pars reticulata), the **ventral tegmental area**, the **oculomotor
    nucleus**, the **trochlear nucleus**, the **mesencephalic trigeminal
    nucleus**, the **riMLF**, the **cMRF**, and other **midbrain
    structures**.

**They are DIFFERENT BRAINSTEM LEVELS** — consumers must **not**
conflate the pontine tegmentum with the midbrain tegmentum.

The Pontine Tegmentum / Medullary Tegmentum Boundary
----------------------------------------------------
This is the **pons vs. medulla** boundary:

*   **Pontine tegmentum** (this module) — the **dorsal portion of the
    pons**.

*   **Medullary tegmentum** — the **dorsal portion of the medulla
    oblongata** — it contains the **solitary nucleus**, the **dorsal
    motor nucleus of the vagus**, the **hypoglossal nucleus**, the
    **nucleus ambiguus**, the **inferior olivary nucleus**, the
    **gigantocellular reticular nucleus**, the **paramedian reticular
    nucleus**, and other **medullary structures**.

**They are DIFFERENT BRAINSTEM LEVELS** — consumers must **not**
conflate the pontine tegmentum with the medullary tegmentum.

The Pontine Tegmentum / White-Matter Tracts Boundary
----------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tracts that
traverse the tegmentum**:

*   **Pontine tegmentum** (this module) — the **grey-matter nuclei** (the
    six structural children).

*   **White-matter tracts that traverse the pontine tegmentum** — the
    **medial longitudinal fasciculus (MLF)**, the **medial lemniscus**,
    the **central tegmental tract**, the **lateral lemniscus**, the
    **descending trigeminal tract**, the **spinothalamic tract**, the
    **rubrospinal tract**, and the **tectospinal tract**.

**The tree wires the pontine tegmentum as a container for the GREY-MATTER
NUCLEI** — the traversing **white-matter tracts** are documented as
**prose and boundary data**, not as structural children. Consumers must
**not** conflate the pontine tegmentum with the white-matter tracts that
traverse it.

The Pontine Tegmentum / SLEA Boundary
-------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Pontine tegmentum** (this module) — **SLEA-FREE**. It is **not** an
    extended-amygdala component, and it carries **no SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The pontine tegmentum is NOT part of the SLEA continuum.** It is the
**dorsal pontine grey-matter region**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
pontine tegmentum.

Function in the Human Brain
---------------------------
The pontine tegmentum's functions are **the neuromodulatory and
autonomic functions of the six nuclei** — **NOT a single unified
function**:

*   **Noradrenergic Arousal and Neuromodulation (Locus Coeruleus):** The
    **locus coeruleus** is the **principal source of norepinephrine** in
    the brain — it **projects diffusely** to the **entire forebrain**,
    the **brainstem**, and the **spinal cord**. It is involved in
    **arousal**, **attention**, **stress**, **pain modulation**, and
    **memory consolidation**.

*   **Cholinergic REM Sleep and Arousal (Laterodorsal Tegmental Nucleus
    and Pedunculopontine Nucleus):** The **laterodorsal tegmental
    nucleus** and the **pedunculopontine nucleus** are **cholinergic
    nuclei** that **project** to the **thalamus**, the **hypothalamus**,
    the **basal forebrain**, and the **brainstem** — they are involved
    in **REM sleep** (cholinergic activation of the thalamus during
    REM), **arousal**, **motivation**, and **locomotion**.

*   **Relaxin-3 Stress and Arousal Modulation (Nucleus Incertus):** The
    **nucleus incertus** is the **relaxin-3-expressing nucleus** that
    **projects** to the **septum**, the **hippocampus**, the **medial
    prefrontal cortex**, the **amygdala**, the **hypothalamus**, and the
    **brainstem** — it is involved in **stress**, **arousal**,
    **feeding**, and **neuroendocrine regulation**.

*   **Locomotion and Cholinergic Arousal (Pedunculopontine Nucleus):**
    The **pedunculopontine nucleus** is the **mesencephalic locomotor
    region** (with the **cuneiform nucleus**) — it is involved in
    **locomotion**, **REM sleep**, **arousal**, and **reward**.

*   **Micturition Control (Pontine Micturition Center):** The **pontine
    micturition center** (Barrington's nucleus) **coordinates** the
    **micturition reflex** — it **projects** to the **sacral spinal
    cord** (the **Onuf's nucleus** and the **parasympathetic
    preganglionic neurons** of the bladder) to **coordinate** the
    **bladder contraction** and **sphincter relaxation**.

*   **Reticulospinal Motor Relay (Tegmental Pontine Reticular Nucleus):**
    The **tegmental pontine reticular nucleus** **projects** to the
    **spinal cord** (via the **reticulospinal tract**) and to the
    **cerebellum** (via the **pontocerebellar fibers**) — it is involved
    in **locomotion**, **posture**, and **motor pattern generation**.

*   **NOT a neural processor in the classical sense.** The pontine
    tegmentum is a **neuromodulatory and autonomic relay region** — its
    nuclei **receive** afferent inputs (from the cortex, the limbic
    system, the hypothalamus, and the brainstem) and **project**
    **diffusely** or **specifically** to **wide-spread targets** (the
    forebrain, the brainstem, the spinal cord). The **processing** of
    arousal, REM sleep, stress, micturition, and locomotion happens in a
    **distributed** manner across the **pontine tegmentum nuclei** and
    their **forebrain, brainstem, and spinal targets**.

**The unifying theme:** the pontine tegmentum is the **dorsal pontine
grey-matter region** — the **tree-wired container** for the **six
neuromodulatory and autonomic nuclei**. It is **heterogeneous** (six
functionally distinct nuclei — noradrenergic, cholinergic,
relaxin-3-expressing, micturition, motor relay), **SLEA-free**, and
**NOT the anatomical pontine tegmentum in its entirety** — the tree
**splits** the other pontine tegmentum structures (parabrachial area,
superior olivary complex, cranial nerve nuclei, PPRF, parvocellular
reticular nucleus) into **separate containers**.

Associated Disorders
--------------------
The pontine tegmentum has **no single named "pontine tegmentum
syndrome" as a collection** — its clinical associations are
**nucleus-specific**:

*   **Locus Coeruleus — Noradrenergic Dysfunction:** **Locus coeruleus**
    dysfunction has been implicated in **Alzheimer's disease**
    (early loss of locus coeruleus neurons precedes cortical pathology),
    **Parkinson's disease** (locus coeruleus degeneration), **PTSD**
    (hyperactive noradrenergic signaling), **depression** (noradrenergic
    dysregulation), **ADHD** (noradrenergic dysfunction), and **opioid
    withdrawal** (noradrenergic hyperactivity).

*   **Laterodorsal Tegmental Nucleus and Pedunculopontine Nucleus —
    Cholinergic Dysfunction:** **Laterodorsal tegmental nucleus** and
    **pedunculopontine nucleus** dysfunction has been implicated in
    **REM sleep behavior disorder** (cholinergic dysregulation),
    **Parkinson's disease** (pedunculopontine nucleus degeneration —
    gait and postural impairment), **narcolepsy** (cholinergic
    dysregulation), and **schizophrenia** (cholinergic dysfunction).

*   **Nucleus Incertus — Relaxin-3 Dysfunction:** **Nucleus incertus**
    dysfunction has been implicated in **stress-related disorders**
    (relaxin-3 dysregulation), **depression**, **anxiety**, and
    **feeding disorders**.

*   **Pontine Micturition Center (Barrington's Nucleus) — Micturition
    Dysfunction:** **Pontine micturition center** dysfunction has been
    implicated in **neurogenic bladder** (detrusor-sphincter
    dyssynergia), **incontinence**, **urinary retention**, and
    **multiple sclerosis** (pontine micturition center demyelination).

*   **Tegmental Pontine Reticular Nucleus — Motor Relay Dysfunction:**
    **Tegmental pontine reticular nucleus** dysfunction has been
    implicated in **gait disorders**, **postural instability**, and
    **locomotor dysfunction** — especially in **Parkinson's disease**
    (pedunculopontine nucleus and tegmental pontine reticular nucleus
    degeneration).

*   **Pontine Stroke — Pontine Tegmentum Involvement:** A **pontine
    stroke** (e.g. **basilar artery** perforator territory) involving
    the **pontine tegmentum** can cause **a wide range of deficits** —
    depending on which **nuclei** are involved:
    *   **Locus coeruleus** involvement — **arousal dysfunction**,
        **noradrenergic deficit**.
    *   **Laterodorsal tegmental nucleus** or **pedunculopontine
        nucleus** involvement — **REM sleep dysregulation**, **arousal
        dysfunction**, **gait and postural impairment**.
    *   **Nucleus incertus** involvement — **stress and arousal
        dysregulation**.
    *   **Pontine micturition center** involvement — **micturition
        dysfunction**.
    *   **Tegmental pontine reticular nucleus** involvement —
        **locomotor and postural dysfunction**.
    *   **Plus** — **other pontine stroke signs** (**hemiparesis**,
        **facial palsy**, **abducens palsy**, **cerebellar ataxia**).

*   **Locked-in Syndrome — Pontine Tegmentum Sparing:** **Locked-in
    syndrome** (bilateral ventral pontine lesion, e.g. **basilar artery
    occlusion**) **typically spares the pontine tegmentum** — the
    **ventral pons** is affected, but the **dorsal pontine tegmentum**
    is **spared** (which is why **consciousness** and **vertical eye
    movements** — which depend on the **midbrain tegmentum**, not the
    pontine tegmentum — are **preserved**). The **pontine tegmentum
    nuclei** (locus coeruleus, laterodorsal tegmental nucleus,
    pedunculopontine nucleus, nucleus incertus, pontine micturition
    center, tegmental pontine reticular nucleus) may be **spared** in
    locked-in syndrome.

*   **No Named "Pontine Tegmentum Syndrome":** The pontine tegmentum is a
    **heterogeneous collection** of six neuromodulatory and autonomic
    nuclei — it has **no named clinical syndrome as a collection**. Its
    clinical relevance is **nucleus-specific** — **locus coeruleus**
    (noradrenergic arousal), **laterodorsal tegmental nucleus** and
    **pedunculopontine nucleus** (cholinergic REM/arousal/locomotion),
    **nucleus incertus** (relaxin-3 stress/arousal), **pontine
    micturition center** (micturition), and **tegmental pontine
    reticular nucleus** (motor relay).

**What is NOT here:** The pontine tegmentum is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **acoustic neuroma** (CN VIII nerve), **vestibular neuritis**
(vestibular nerve), **labyrinthitis** (inner ear), **auditory neuropathy
spectrum disorder** (cochlear nerve or hair cell), **Wallenberg
syndrome** (lateral medulla), **internuclear ophthalmoplegia** (MLF), or
**horizontal gaze palsy** (PPRF or abducens nucleus). Its clinical
relevance is **neuromodulatory and autonomic-specific**, via the six
nuclei it subserves. **No named pontine tegmentum syndrome exists as a
collection.**

Lateralization Notes
--------------------
The pontine tegmentum is a **tree-wired container** of six **bilateral
neuromodulatory and autonomic nuclei**. The six nuclei are **bilaterally
symmetric** and **strictly mirrored**, and the container carries **NO
warning at the container level**:

*   **Strict Bilateral Symmetry:** Each of the six nuclei (locus
    coeruleus, laterodorsal tegmental nucleus, nucleus incertus,
    pedunculopontine nucleus, pontine micturition center, tegmental
    pontine reticular nucleus) is **bilaterally symmetric** — same
    neuron populations, same functional system, same bilateral framing.
    The bilateral symmetry is **strict**.

*   **Bilateral Projections (Structural Fact, NOT a Lateralization
    Warning):** Each nucleus **projects bilaterally** — the locus
    coeruleus projects **bilaterally** to the forebrain, the brainstem,
    and the spinal cord; the laterodorsal tegmental nucleus and the
    pedunculopontine nucleus project **bilaterally** to the thalamus, the
    hypothalamus, the basal forebrain, and the brainstem; the nucleus
    incertus projects **bilaterally** to the septum, the hippocampus,
    the medial prefrontal cortex, the amygdala, the hypothalamus, and the
    brainstem; the pontine micturition center projects **bilaterally**
    to the sacral spinal cord; the tegmental pontine reticular nucleus
    projects **bilaterally** to the spinal cord and the cerebellum. **This
    bilateral projection** is a **structural fact** of the **neuromodulatory
    and autonomic systems** — it is **not** a functional lateralization.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The pontine
    tegmentum is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the pontine tegmentum.

*   **NO Amygdala-Lateralization Warning of their own (the pontine
    tegmentum is NEUROMODULATORY/AUTONOMIC, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The pontine tegmentum
    is a **neuromodulatory and autonomic region** — consumers must
    **not** conflate it with the **amygdala** or with the **fear
    circuit**.

**A consumer that assumes "left pontine tegmentum = right pontine
tegmentum" will be structurally correct** — the six nuclei are
**strictly symmetric** (the bilateral projections are structural facts,
not lateralizations). The pontine tegmentum is a **strict-mirror pair
with NO warning at the container level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The container is **bilateral**, but
    it does **not** import left/right containers — each of the six
    nuclei is itself a **single module** (not split into left/right in
    the tree — the module represents the **bilateral nucleus**).
*   **No cross-lobe imports.** This module does **not** import from
    ``.../pons/parabrachial_area/``,
    ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../pons/pontine_nuclei/``,
    ``.../metencephalon/cerebellum/``,
    ``.../metencephalon/fourth_ventricle/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, or any other container. The pontine
    tegmentum's relationships to the **basilar pons**, the **parabrachial
    area**, the **superior olivary complex**, the **cranial nerve
    nuclei**, the **PPRF**, the **parvocellular reticular nucleus**, the
    **pontine nuclei**, the **fourth ventricle**, the **cerebellum**,
    the **midbrain tegmentum**, the **medullary tegmentum**, the
    **white-matter tracts that traverse the tegmentum**, and the **SLEA
    continuum** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children are the SIX
    neuromodulatory and autonomic nuclei.** Each of the six nuclei is
    itself a **leaf** at the tree level (representing its **bilateral**
    real-anatomy counterpart as a **single module**).
*   **TREE-WIRED SUBSET — NOT the whole anatomical pontine tegmentum.**
    The **parabrachial area**, the **superior olivary complex**, the
    **cranial nerve nuclei**, the **PPRF**, the **parvocellular
    reticular nucleus**, the **pontine nuclei**, and the **white-matter
    tracts** are **separate containers** under the pons, **not**
    structural children of the pontine tegmentum. Consumers must **not**
    assume the tree's **tegmentum** equals the anatomical pontine
    tegmentum.
*   **GREY-MATTER NUCLEI — NOT the white-matter tracts that traverse
    the tegmentum.** The **grey-matter nuclei** are the six structural
    children. The traversing **white-matter tracts** (MLF, medial
    lemniscus, central tegmental tract, lateral lemniscus, etc.) are
    **prose**, not structural children. Consumers must **not** conflate
    the pontine tegmentum with the white-matter tracts.
*   **NOT the basilar pons — that is the VENTRAL PONS.** Consumers must
    **not** conflate the pontine tegmentum with the basilar pons or with
    the pontine nuclei.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, the PPRF, or the parvocellular reticular
    nucleus — those are SEPARATE STRUCTURAL CHILDREN of the pons.**
    Consumers must **not** conflate the pontine tegmentum with any of
    them.
*   **NOT the fourth ventricle — that is a CSF SPACE.** Consumers must
    **not** conflate the pontine tegmentum with the fourth ventricle.
*   **NOT the cerebellum — that is the metencephalic SIBLING.**
    Consumers must **not** conflate the pontine tegmentum with the
    cerebellum.
*   **NOT the midbrain tegmentum or the medullary tegmentum — those are
    DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate the
    pontine tegmentum with the midbrain tegmentum or the medullary
    tegmentum.
*   **HETEROGENEOUS — MULTIPLE nuclei with DIFFERENT functions.** The
    **locus coeruleus** (noradrenergic arousal), **laterodorsal
    tegmental nucleus** and **pedunculopontine nucleus** (cholinergic
    REM/arousal/locomotion), **nucleus incertus** (relaxin-3
    stress/arousal), **pontine micturition center** (micturition), and
    **tegmental pontine reticular nucleus** (motor relay) are
    **functionally distinct**. Consumers must **not** treat the pontine
    tegmentum as a single uniform system.
*   **SLEA-FREE — no extended-amygdala relationship.** The pontine
    tegmentum is **not** an extended-amygdala component, and it carries
    **no SLEA warning**.
*   **NOT the fear-output — the pontine tegmentum is
    NEUROMODULATORY/AUTONOMIC.** The **fear-output** structure is the
    **central nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**; the **fear-modulatory / extinction**
    structures are the **basomedial nuclei**. The **pontine tegmentum**
    is a **neuromodulatory and autonomic region** — it is **not** part
    of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The pontine tegmentum is a local container
    under the pons container, not a cross-listed container.
*   **No nested cross-listing.** The pontine tegmentum has no nested
    dual-framing module. It is a single container with six structural
    children.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import tegmentum

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.tegmentum"
    )

**Do not** assume the pontine tegmentum is a **leaf**. It is a
**container** — its structural children are the **six neuromodulatory
and autonomic nuclei** (laterodorsal tegmental nucleus, locus coeruleus,
nucleus incertus, pedunculopontine nucleus, pontine micturition center,
tegmental pontine reticular nucleus).

**Do not** assume the pontine tegmentum is the **whole anatomical
pontine tegmentum**. The tree's **tegmentum** is a **subset** — the
**parabrachial area**, the **superior olivary complex**, the **cranial
nerve nuclei**, the **PPRF**, the **parvocellular reticular nucleus**,
the **pontine nuclei**, and the **white-matter tracts** are **separate
containers** under the pons.

**Do not** assume the pontine tegmentum is the **basilar pons**. The
**basilar pons** is the **ventral** portion of the pons; the **pontine
tegmentum** is the **dorsal** portion.

**Do not** assume the pontine tegmentum is the **parabrachial area**,
the **superior olivary complex**, the **cranial nerve nuclei**, the
**PPRF**, or the **parvocellular reticular nucleus**. Those are
**separate structural children** of the pons.

**Do not** assume the pontine tegmentum is the **fourth ventricle**. The
**fourth ventricle** is a **CSF space**; the **pontine tegmentum** is
**neural tissue**.

**Do not** assume the pontine tegmentum is the **cerebellum**. The
**cerebellum** is the **metencephalic sibling**.

**Do not** assume the pontine tegmentum is the **midbrain tegmentum** or
the **medullary tegmentum**. Those are **different brainstem levels**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the pontine tegmentum. **The pontine tegmentum is
SLEA-FREE** — it is **not** an extended-amygdala component, and it is
**NOT part of the fear circuit**.

Iterating the pontine tegmentum's structural children (recommended
consumer pattern)::

    PONTINE_TEGMENTUM_CHILDREN = (
        "laterodorsal_tegmental_nucleus",
        "locus_coeruleus",
        "nucleus_incertus",
        "pedunculopontine_nucleus",
        "pontine_micturition_center",
        "tegmental_pontine_reticular_nucleus",
    )
    # The six nuclei are the structural children of the pontine
    # tegmentum. Each is itself a leaf at the tree level (representing
    # its bilateral real-anatomy counterpart as a single module).

Iterating the pontine tegmentum's structural children (recommended
consumer pattern)::

    for nucleus in PONTINE_TEGMENTUM_CHILDREN:
        nucleus_path = (
            f"hindbrain.metencephalon.pons.tegmentum.{nucleus}"
        )
        # resolve nucleus_path through the memory/recall layer

Reaching the pons (recommended consumer pattern — the parent)::

    # The pons is the WHOLE METENCEPHALIC BRAINSTEM SEGMENT that
    # CONTAINS the pontine tegmentum as one of its structural children:
    #
    #   .../pons/
    #
    # The pontine tegmentum is a CHILD of the pons.

Reaching the basilar pons (recommended consumer pattern — the VENTRAL
PONS)::

    # The basilar pons is the VENTRAL portion of the pons — it contains
    # the pontine nuclei, the corticospinal tract, the corticobulbar
    # tract, and the transverse pontine fibers that form the middle
    # cerebellar peduncle:
    #
    #   .../pons/pontine_nuclei/  (and the surrounding white matter)
    #
    # The pontine tegmentum is the DORSAL portion of the pons.

Reaching the parabrachial area (recommended consumer pattern — a
SEPARATE pons child)::

    # The parabrachial area is a SEPARATE STRUCTURAL CHILD of the pons —
    # it is the visceral-sensory and respiratory-relay complex:
    #
    #   .../pons/parabrachial_area/
    #
    # The tree splits the parabrachial area from the pontine tegmentum
    # container — even though it is anatomically located in the pontine
    # tegmentum.

Reaching the superior olivary complex (recommended consumer pattern — a
SEPARATE pons child)::

    # The superior olivary complex is a SEPARATE STRUCTURAL CHILD of the
    # pons — it is the pontine binaural sound-localization relay:
    #
    #   .../pons/superior_olivary_complex/
    #
    # The tree splits the superior olivary complex from the pontine
    # tegmentum container — even though it is anatomically located in
    # the ventral pontine tegmentum.

Reaching the cranial nerve nuclei (recommended consumer pattern — a
SEPARATE pons child)::

    # The cranial nerve nuclei are a SEPARATE STRUCTURAL CHILD of the
    # pons — they are the CN V, VI, VII, VIII nuclei:
    #
    #   .../pons/cranial_nerve_nuclei/
    #
    # The tree splits the cranial nerve nuclei from the pontine tegmentum
    # container — even though they are anatomically located in the
    # pontine tegmentum.

Reaching the PPRF (recommended consumer pattern — a SEPARATE pons child)::

    # The paramedian pontine reticular formation (PPRF) is a SEPARATE
    # STRUCTURAL CHILD of the pons — it is the horizontal saccadic burst
    # generator:
    #
    #   .../pons/paramedian_pontine_reticular_formation/
    #
    # The tree splits the PPRF from the pontine tegmentum container —
    # even though it is anatomically located in the pontine tegmentum.

Reaching the parvocellular reticular nucleus (recommended consumer
pattern — a SEPARATE pons child)::

    # The parvocellular reticular nucleus is a SEPARATE STRUCTURAL CHILD
    # of the pons — it is the orofacial premotor and autonomic relay:
    #
    #   .../pons/parvocellular_reticular_nucleus/
    #
    # The tree splits the parvocellular reticular nucleus from the
    # pontine tegmentum container — even though it is anatomically
    # located in the pontine tegmentum.

Reaching the pontine nuclei (recommended consumer pattern — in the
BASILAR PONS)::

    # The pontine nuclei are the CORTICO-PONTO-CEREBELLAR RELAY in the
    # BASILAR PONS — the VENTRAL portion of the pons:
    #
    #   .../pons/pontine_nuclei/
    #
    # The pontine tegmentum is the DORSAL portion of the pons.

Reaching the fourth ventricle (recommended consumer pattern — the CSF
space)::

    # The fourth ventricle is the CSF SPACE dorsal to the pons:
    #
    #   .../metencephalon/fourth_ventricle/
    #
    # The pontine tegmentum forms the FLOOR of the fourth ventricle.

Reaching the midbrain tegmentum (recommended consumer pattern — a
DIFFERENT brainstem level)::

    # The midbrain tegmentum is the DORSAL PORTION of the midbrain:
    #
    #   .../midbrain/tegmentum/
    #
    # The pontine tegmentum is the DORSAL PORTION of the pons — a
    # DIFFERENT BRAINSTEM LEVEL.

Bilateral iteration (recommended consumer pattern)::

    # Each of the six pontine tegmentum nuclei is a SINGLE module (not
    # split into left/right at the tree level). The modules represent
    # the BILATERAL nuclei.
    for nucleus in PONTINE_TEGMENTUM_CHILDREN:
        nucleus_path = (
            f"hindbrain.metencephalon.pons.tegmentum.{nucleus}"
        )
        # resolve nucleus_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The pontine tegmentum's six nuclei are structural children:
    #   locus_coeruleus              -> noradrenergic arousal, attention,
    #                                    stress, pain modulation, memory
    #                                    consolidation; diffuse projections
    #                                    to the entire forebrain, brainstem,
    #                                    and spinal cord
    #   laterodorsal_tegmental_nucleus -> cholinergic REM sleep, arousal,
    #                                    motivation; projections to the
    #                                    thalamus, hypothalamus, basal
    #                                    forebrain, and brainstem
    #   nucleus_incertus             -> relaxin-3 stress, arousal,
    #                                    feeding, neuroendocrine regulation;
    #                                    projections to the septum,
    #                                    hippocampus, medial prefrontal
    #                                    cortex, amygdala, hypothalamus,
    #                                    and brainstem
    #   pedunculopontine_nucleus     -> cholinergic/glutamatergic/GABAergic
    #                                    locomotion (mesencephalic locomotor
    #                                    region), REM sleep, arousal,
    #                                    reward; projections to the basal
    #                                    ganglia, thalamus, hypothalamus,
    #                                    brainstem, and spinal cord
    #   pontine_micturition_center   -> micturition control (Barrington's
    #                                    nucleus); projections to the
    #                                    sacral spinal cord (Onuf's nucleus
    #                                    and parasympathetic preganglionic
    #                                    neurons of the bladder)
    #   tegmental_pontine_reticular  -> motor relay (reticulospinal
    #   nucleus                        projections); locomotion, posture,
    #                                    motor pattern generation;
    #                                    projections to the spinal cord
    #                                    and cerebellum
    #
    # Do not attempt to resolve these as sub-paths of the pontine
    # tegmentum beyond the six structural children — resolve
    # sub-nucleus-level detail through the references.

References
----------
*   **Canonical pontine tegmentum anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed. (Pontine
    tegmentum in overview.)
*   **Locus coeruleus — canonical:** Aston-Jones, G., Cohen, J.D.
    (2005). "An integrative theory of locus coeruleus-norepinephrine
    function: adaptive gain and optimal performance." *Annual Review of
    Neuroscience* 28:403–450. (Locus coeruleus — noradrenergic arousal,
    attention, and stress.)
*   **Laterodorsal tegmental nucleus and pedunculopontine nucleus —
    canonical:** Mesulam, M.M., Mufson, E.J., Wainer, B.H., Levey, A.I.
    (1983). "Central cholinergic pathways in the rat: an overview based
    on an alternative nomenclature (Ch1-Ch6)." *Neuroscience*
    10:1185–1201. (Laterodorsal tegmental nucleus and pedunculopontine
    nucleus — cholinergic brainstem nuclei.)
*   **Pedunculopontine nucleus — modern review:** Garcia-Rill, E.
    (1991). "The pedunculopontine nucleus." *Progress in Neurobiology*
    36:363–389. (Pedunculopontine nucleus — locomotion, REM sleep, and
    arousal.)
*   **Nucleus incertus — canonical:** Ryan, P.J., Ma, S., Olucha-Bordonau,
    F.E., Gundlach, A.L. (2011). "Nucleus incertus — an emerging role in
    the behavioural actions of relaxin-3." *British Journal of
    Pharmacology* 162:1115–1126. (Nucleus incertus — relaxin-3 stress,
    arousal, and feeding.)
*   **Pontine micturition center — canonical:** Barrington, F.J.F.
    (1925). "The effect of lesions of the hind- and mid-brain on
    micturition in the cat." *Quarterly Journal of Experimental
    Physiology* 15:81–102. (Original description of the pontine
    micturition center — Barrington's nucleus.)
*   **Pontine micturition center — modern review:** Fowler, C.J.,
    Griffiths, D., de Groat, W.C. (2008). "The neural control of
    micturition." *Nature Reviews Neuroscience* 9:453–466. (Pontine
    micturition center — micturition reflex control.)
*   **Tegmental pontine reticular nucleus — canonical:** Brodal, A.
    (2010). *The Central Nervous System: Structure and Function*, 4th
    ed. (Tegmental pontine reticular nucleus — motor relay.)
*   **Brainstem anatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An
    Atlas of Structures, Sections, and Systems*, 8th ed. (Pontine
    tegmentum and its nuclei.)
*   **Locked-in syndrome (contrast — pontine tegmentum typically
    spared):** Plum, F., Posner, J.B. (1980). *The Diagnosis of Stupor
    and Coma*, 3rd ed. (Locked-in syndrome — bilateral ventral pontine
    lesion; pontine tegmentum typically spared.)
*   **Basilar pons (contrast — the ventral pons):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Basilar pons — ventral pons; distinct from the pontine tegmentum.)
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
*   **Cranial nerve nuclei (contrast — a separate pons child):**
    Haines, D.E. (2012). *Neuroanatomy: An Atlas of Structures,
    Sections, and Systems*, 8th ed. (Cranial nerve nuclei of the pons —
    distinct from the pontine tegmentum container in the tree.)
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
    pons; distinct from the pontine tegmentum.)
*   **Fourth ventricle (contrast — a CSF space):** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Fourth ventricle — CSF space dorsal to the pons; distinct from the
    pontine tegmentum.)
*   **Cerebellum (contrast — the metencephalic sibling):** Manto, M.,
    Gruol, D.L., Schmahmann, J.D., Koibuchi, N., Rossi, F. (eds.)
    (2013). *Handbook of the Cerebellum and Cerebellar Disorders*.
    (Cerebellum — metencephalic sibling; distinct from the pontine
    tegmentum.)
*   **Midbrain tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Midbrain tegmentum — dorsal midbrain; distinct
    from the pontine tegmentum.)
*   **Medullary tegmentum (contrast — a DIFFERENT brainstem level):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medullary tegmentum — dorsal medulla; distinct
    from the pontine tegmentum.)
*   **SLEA (contrast — the pontine tegmentum is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the pontine tegmentum.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association belongs to
    the **amygdala module** — the **central nucleus** and the
    **basolateral nuclei** — not to the pontine tegmentum.)
*   NeuroNames — Pontine tegmentum; FMA — Pontine tegmentum.
"""
