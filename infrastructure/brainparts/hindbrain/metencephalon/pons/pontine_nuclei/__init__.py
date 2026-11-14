"""
infrastructure.brainparts.hindbrain.metencephalon.pons.pontine_nuclei
====================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── pontine_nuclei   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Pontine nuclei; pontine nuclear complex; nuclei
pontis; grey matter of the basilar pons; "the cortico-ponto-cerebellar
relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem grey-matter nuclear complex** — a **bilateral collection of
anatomically delimited grey-matter nuclei** in the **basilar pons**,
interspersed among the **corticospinal** and **corticobulbar tracts**
and continuous with the **transverse pontine fibers** that form the
**middle cerebellar peduncle**. It is the **principal pontine relay** for
the **cortico-ponto-cerebellar pathway** — the **major cerebrocerebellar
projection** in the mammalian brain.
**Part of:** The **pons** container — specifically, the **basilar pons**
(the **ventral** portion of the pons, as opposed to the **dorsal
tegmentum**). The **pons** is the **metencephalic** brainstem segment.
**Structural parent:** ``.../pons/`` → **direct child** of the pons
container.
**Structural children:** **Two sub-containers** — ``left`` and ``right``
— the **bilateral halves** of the pontine nuclear complex. Each of
``left`` and ``right`` is a **sub-container** whose **sub-nuclei**
(median, paramedian, peduncular, ventral, dorsal, lateral pontine
nuclei — **prose subdivisions**) are documented as **prose**, not as
structural children.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
pontine nuclei are a CONTAINER, not a leaf.** They have **two
structural children** (``left`` and ``right``), each of which is a
**bilateral sub-container** whose **sub-nuclei** are **prose
subdivisions**. Consumers must **not** treat the pontine nuclei as a
leaf, and must **not** assume the left and right halves are absent —
they are the **direct structural children** of the pontine nuclei.
**Boundary status (BILATERAL CONTAINER — left and right are STRUCTURALLY
SYMMETRIC):** **Boundary case — the pontine nuclei are a BILATERAL
container.** The **left** and **right** sub-containers are
**structurally symmetric** — same prose subdivisions under each, same
functional system (cortico-ponto-cerebellar relay), same bilateral
framing. The bilateral symmetry is **strict**. Consumers must **not**
assume a left/right asymmetry at the container level — the container is
a **strict mirror pair**. Any lateralization is documented **inside the
left and right sub-containers** and in the **Lateralization Notes**
below, not imported from elsewhere.
**Boundary status (GREY-MATTER NUCLEI — NOT the corticopontine or
pontocerebellar fibers):** **Boundary case — the pontine nuclei are the
GREY-MATTER NUCLEI, NOT the corticopontine or pontocerebellar fibers.**
The **corticopontine fibers** are the **white-matter descending axons**
from the **cerebral cortex** to the **pontine nuclei** — the
**afferent limb** of the cortico-ponto-cerebellar pathway. The
**pontocerebellar fibers** are the **white-matter crossing axons** from
the **pontine nuclei** to the **contralateral cerebellar cortex** —
the **efferent limb** of the cortico-ponto-cerebellar pathway. The
**pontine nuclei** (here) are the **grey-matter neuron clusters** that
**receive** the corticopontine fibers and **give rise to** the
pontocerebellar fibers. They are **DIFFERENT STRUCTURES** — the
**nuclei** are grey matter; the **fibers** are white matter. **This
distinction is clinically load-bearing** — a **pontine nuclei lesion**
causes **cerebrocerebellar dysfunction** (cerebellar ataxia, dysmetria,
dysarthria, cognitive-affective cerebellar syndrome); a **corticopontine
fiber lesion** causes **the same clinical syndrome** (the pontine nuclei
are cut off from their cortical input); a **pontocerebellar fiber
lesion** causes **the same clinical syndrome** (the pontine nuclei are
cut off from their cerebellar output). Consumers must **not** conflate
the pontine nuclei with the corticopontine fibers or the pontocerebellar
fibers.
**Boundary status (NOT the middle cerebellar peduncle — that is the
WHITE-MATTER TRACT the pontocerebellar fibers form):** **Boundary case —
the pontine nuclei are NOT the middle cerebellar peduncle.** The
**middle cerebellar peduncle** (brachium pontis) is the **white-matter
tract** that **carries** the **pontocerebellar fibers** from the
**contralateral pontine nuclei** to the **contralateral cerebellar
cortex** — it is the **largest** of the **three cerebellar peduncles**.
The **pontine nuclei** (here) are the **grey-matter neuron clusters**
that **give rise to** the pontocerebellar fibers that **form** the
middle cerebellar peduncle. They are **DIFFERENT STRUCTURES** — the
**nuclei** are grey matter; the **peduncle** is white matter. **This
distinction is clinically load-bearing** — a **middle cerebellar
peduncle lesion** causes **cerebellar ataxia** and **dysmetria** (the
cerebellar input is disrupted); a **pontine nuclei lesion** causes
**cerebellar ataxia** as well (the pontine nuclei are the source of the
peduncle's fibers) — the **distinction** is often made by **associated
brainstem signs** (a pontine nuclei lesion may accompany **corticospinal
tract** involvement — **hemiparesis** — or **cranial nerve** involvement;
a pure middle cerebellar peduncle lesion is usually isolated cerebellar
ataxia). Consumers must **not** conflate the pontine nuclei with the
middle cerebellar peduncle.
**Boundary status (NOT the corticospinal and corticobulbar tracts — those
are the WHITE-MATTER TRACTS the nuclei are INTERSPERSED among):**
**Boundary case — the pontine nuclei are NOT the corticospinal and
corticobulbar tracts.** The **corticospinal tract** and the
**corticobulbar tract** are the **white-matter descending tracts** that
**descend** through the **basilar pons** (they are the **long
descending tracts** that **run through** the **basilar pons** alongside
the pontine nuclei) — they **carry** the **upper motor neuron** axons
from the **motor cortex** to the **spinal cord** and the **cranial nerve
motor nuclei**. The **pontine nuclei** (here) are the **grey-matter
neuron clusters** that are **interspersed** among the corticospinal and
corticobulbar tracts in the **basilar pons**. They are **DIFFERENT
STRUCTURES** — the **nuclei** are grey matter; the **tracts** are white
matter. **This anatomical juxtaposition is a classic source of
confusion** — the pontine nuclei are **anatomically intermingled** with
the corticospinal and corticobulbar tracts (the tracts run **through**
the basilar pons, and the pontine nuclei are **scattered among** them),
and consumers must **not** conflate the pontine nuclei with the
corticospinal and corticobulbar tracts. **This distinction is clinically
load-bearing** — a **pontine nuclei lesion** causes **cerebrocerebellar
dysfunction**; a **corticospinal/corticobulbar tract lesion** causes
**upper motor neuron weakness** (hemiparesis, pseudobulbar palsy). The
**two can coexist** in a **pontine stroke** — producing **combined
cerebellar ataxia and hemiparesis** — but they are **different
structures**.
**Boundary status (NOT the pontine reticular formation — that is the
DORSAL PONTINE TEGMENTUM):** **Boundary case — the pontine nuclei are
NOT the pontine reticular formation.** The **pontine reticular
formation** — the **paramedian pontine reticular formation (PPRF)**, the
**parvocellular reticular nucleus**, the **caudal pontine reticular
nucleus**, the **oral pontine reticular nucleus**, and other reticular
nuclei — is the **grey-matter region** in the **dorsal pontine
tegmentum** (the **dorsal** portion of the pons, as opposed to the
**basilar** portion). The **pontine nuclei** (here) are the **grey-matter
neuron clusters** in the **basilar pons** (the **ventral** portion).
They are **DIFFERENT STRUCTURES** — **different anatomical locations**
(basilar pons vs. dorsal tegmentum), **different functional systems**
(cortico-ponto-cerebellar relay vs. horizontal saccades, orofacial motor,
autonomic regulation, respiratory rhythm). **This anatomical distinction
is a classic source of confusion** — the "pontine reticular formation"
and the "pontine nuclei" are **both** in the pons, but they are in
**different anatomical regions** (dorsal tegmentum vs. basilar pons) and
**different functional systems**. Consumers must **not** conflate the
pontine nuclei with the pontine reticular formation or any of its
components (the PPRF, the parvocellular reticular nucleus, the caudal
pontine reticular nucleus, the oral pontine reticular nucleus).
**Boundary status (NOT the parabrachial area, the superior olivary
complex, the cranial nerve nuclei, or the locus coeruleus — those are
DORSAL PONTINE TEGMENTUM structures):** **Boundary case — the pontine
nuclei are NOT the parabrachial area, the superior olivary complex, the
cranial nerve nuclei, or the locus coeruleus.** Those are **dorsal
pontine tegmentum structures** — the **parabrachial area** is the
**visceral-sensory and respiratory-relay complex**; the **superior
olivary complex** is the **auditory brainstem relay**; the **cranial
nerve nuclei** are the **CN V, VI, VII, VIII nuclei**; the **locus
coeruleus** is the **noradrenergic nucleus**. The **pontine nuclei**
(here) are the **basilar pons grey-matter neuron clusters** — the
**cortico-ponto-cerebellar relay**. They are **DIFFERENT STRUCTURES** —
different anatomical locations (basilar pons vs. dorsal tegmentum),
different functional systems (cortico-ponto-cerebellar vs.
visceral-sensory/respiratory/auditory/cranial nerve motor/sensory/
noradrenergic). Consumers must **not** conflate the pontine nuclei with
any of the **dorsal pontine tegmentum** structures.
**Boundary status (NOT the cerebellum — that is the METENCEPHALIC SIBLING
the pontocerebellar fibers project to):** **Boundary case — the pontine
nuclei are NOT the cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/hemispheres/left/`` and ``.../right/``)
is the **metencephalic cerebellar half** — it has its **own nuclei**
(dentate, fastigial, interposed) and its **own cortex**. The **pontine
nuclei** (here) are the **basilar pons grey-matter neuron clusters** that
**project to** the **contralateral cerebellar cortex** via the
**pontocerebellar fibers** and the **middle cerebellar peduncle**.
They are **DIFFERENT STRUCTURES** — the **pontine nuclei** are
**pontine**; the **cerebellum** is **cerebellar**. **The pontine nuclei
are the major source of cerebellar cortical afferents** — but they are
**not** the cerebellum itself. Consumers must **not** conflate the
pontine nuclei with the cerebellum.
**Boundary status (NOT a single uniform nucleus — MULTIPLE sub-nuclei
with different cortical inputs):** **Boundary case — the pontine nuclei
are NOT a single uniform nucleus; they contain MULTIPLE sub-nuclei with
different cortical inputs and different cerebellar targets.** The
**sub-nuclei** of the pontine nuclei include the **median (paramedian)
pontine nucleus** (which receives input from the **cingulate motor
areas** and the **supplementary motor area** and projects to the
**vermis** and the **medial cerebellar hemisphere** — the
**spinocerebellar** and **vestibulocerebellar** functional zones), the
**peduncular (ventral) pontine nucleus** (which receives input from the
**primary motor cortex** and the **premotor cortex** and projects to
the **intermediate cerebellar hemisphere** — the **cerebrocerebellar**
functional zone), and the **dorsal (superior) and lateral pontine
nuclei** (which receive input from the **prefrontal cortex**, the
**posterior parietal cortex**, and the **superior temporal cortex** and
project to the **lateral cerebellar hemisphere** — the
**cognitive-affective cerebrocerebellar** functional zone). **These
sub-nuclei are prose subdivisions**, not structural children. Consumers
must **not** treat the pontine nuclei as a single uniform nucleus — they
are a **functionally heterogeneous complex** with **topographically
organized** sub-nuclei.
**Boundary status (TOPOGRAPHICALLY ORGANIZED — the sub-nuclei are
organized by cortical input and cerebellar target):** **Boundary case —
the pontine nuclei are TOPOGRAPHICALLY ORGANIZED.** The **rostrocaudal**
and **mediolateral** organization of the **pontine nuclei** reflects the
**topography** of the **cerebral cortex** (the source of the
corticopontine fibers) and the **cerebellar cortex** (the target of the
pontocerebellar fibers) — **each cortical region projects to a specific
pontine sub-region**, and **each pontine sub-region projects to a
specific cerebellar region**. **This topographic organization** is the
**neural substrate** of the **cerebrocerebellar functional topography**
— the **motor cortex** → **peduncular pontine nucleus** → **intermediate
cerebellar hemisphere** (motor control); the **prefrontal cortex** →
**dorsal/lateral pontine nucleus** → **lateral cerebellar hemisphere**
(cognitive-affective control). **This topographic organization** is
**prose**, not structural children. Consumers must **not** assume the
pontine nuclei are a **single uniform relay** — they are a
**topographically organized complex**.
**Boundary status (SLEA-FREE — the pontine nuclei are NOT an
extended-amygdala component):** **Boundary case — the pontine nuclei are
SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus** (the
**only SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere). The **pontine
nuclei** are a **basilar pons cortico-ponto-cerebellar relay** — they are
**NOT** an extended-amygdala component, and they carry **NO SLEA
warning**. Consumers must **not** import the SLEA warning into the
pontine nuclei — they are **SLEA-free**.

Overview
--------
The pontine nuclei are the **cortico-ponto-cerebellar relay** of the
**basilar pons** — a **bilateral collection** of **anatomically
delimited grey-matter nuclei** interspersed among the **corticospinal**
and **corticobulbar tracts** and continuous with the **transverse
pontine fibers** that form the **middle cerebellar peduncle**. They are
a **container** under the pons container, with **two structural
children** (``left`` and ``right``) — the **bilateral halves** of the
pontine nuclear complex — and each of ``left`` and ``right`` is a
**sub-container** whose **sub-nuclei** (median, paramedian, peduncular,
ventral, dorsal, lateral pontine nuclei) are **prose subdivisions**.

**The pontine nuclei are a CONTAINER, NOT a leaf.** Their structural
children are ``left`` and ``right`` — the **bilateral sub-containers**.

**The pontine nuclei are a BILATERAL CONTAINER.** The ``left`` and
``right`` sub-containers are **structurally symmetric** — same prose
subdivisions under each, same functional system (cortico-ponto-cerebellar
relay), same bilateral framing. The bilateral symmetry is **strict**.

**The pontine nuclei are GREY-MATTER NUCLEI, NOT the corticopontine or
pontocerebellar fibers.** The **corticopontine fibers** are the
**afferent white-matter tract** from the cortex to the pontine nuclei;
the **pontocerebellar fibers** are the **efferent white-matter tract**
from the pontine nuclei to the contralateral cerebellar cortex. The
**pontine nuclei** are the **grey-matter neuron clusters** that
**receive** the corticopontine fibers and **give rise to** the
pontocerebellar fibers.

**The pontine nuclei are NOT the middle cerebellar peduncle.** The
**middle cerebellar peduncle** is the **white-matter tract** that
**carries** the pontocerebellar fibers from the contralateral pontine
nuclei to the contralateral cerebellar cortex. The **pontine nuclei**
are the **grey-matter source** of those fibers.

**The pontine nuclei are NOT the corticospinal and corticobulbar
tracts.** The **corticospinal** and **corticobulbar tracts** are the
**white-matter descending tracts** that **run through** the basilar
pons; the **pontine nuclei** are **interspersed among** them. **This
anatomical juxtaposition is a classic source of confusion** — the
nuclei and the tracts are **anatomically intermingled** in the basilar
pons, but they are **different structures** with **different clinical
correlates** (cerebellar ataxia vs. upper motor neuron weakness).

**The pontine nuclei are NOT the pontine reticular formation.** The
**pontine reticular formation** is the **dorsal pontine tegmentum**
(PPRF, parvocellular reticular nucleus, caudal/oral pontine reticular
nuclei, etc.); the **pontine nuclei** are the **basilar pons**. They are
**different anatomical regions** with **different functional systems**
(cortico-ponto-cerebellar vs. horizontal saccades, orofacial motor,
autonomic regulation, respiratory rhythm).

**The pontine nuclei are TOPOGRAPHICALLY ORGANIZED.** The **sub-nuclei**
receive **topographically organized** cortical inputs and project to
**topographically organized** cerebellar targets — the **motor cortex**
→ **peduncular pontine nucleus** → **intermediate cerebellar hemisphere**
(motor control); the **prefrontal cortex** → **dorsal/lateral pontine
nucleus** → **lateral cerebellar hemisphere** (cognitive-affective
control).

**The pontine nuclei are SLEA-FREE.** They are **not** an
extended-amygdala component, and they carry **no SLEA warning**.

Sub-Container and Sub-Nucleus Composition (prose subdivisions, not
structural children)
------------------------------------------------------------------------
The pontine nuclei contain **two structural children** — the ``left``
and ``right`` **sub-containers** — each of which is a **bilateral half**
of the pontine nuclear complex with **prose subdivisions** (the
**sub-nuclei**):

*   **Median (paramedian) pontine nucleus** — the **most medial** sub-
    nucleus, adjacent to the **midline** and the **raphe**. It
    **receives** inputs from the **cingulate motor areas**, the
    **supplementary motor area**, and the **limbic cortex** and
    **projects** to the **vermis** and the **medial cerebellar
    hemisphere** — the **spinocerebellar** and **vestibulocerebellar**
    functional zones. **Spinocerebellar and limbic-cerebellar relay**
    is the functional system subserved primarily by the median pontine
    nucleus.

*   **Peduncular (ventral) pontine nucleus** — the **lateral** sub-
    nucleus, adjacent to the **cerebral peduncle** (the
    **corticospinal** and **corticobulbar** tracts) — the **largest**
    of the pontine sub-nuclei. It **receives** inputs from the
    **primary motor cortex** (M1) and the **premotor cortex** (PMC) and
    **projects** to the **intermediate cerebellar hemisphere** — the
    **cerebrocerebellar** functional zone. **Motor cerebrocerebellar
    relay** is the functional system subserved primarily by the
    peduncular pontine nucleus.

*   **Dorsal (superior) pontine nucleus** — the **dorsal** sub-nucleus,
    adjacent to the **pontine tegmentum**. It **receives** inputs from
    the **prefrontal cortex** (especially the **dorsolateral prefrontal
    cortex**) and the **posterior parietal cortex** and **projects** to
    the **lateral cerebellar hemisphere** — the **cognitive-affective
    cerebrocerebellar** functional zone. **Cognitive-affective
    cerebrocerebellar relay** is the functional system subserved
    primarily by the dorsal pontine nucleus.

*   **Lateral pontine nucleus** — the **far-lateral** sub-nucleus. It
    **receives** inputs from the **superior temporal cortex** (auditory
    association), the **posterior parietal cortex**, and the
    **prefrontal cortex** and **projects** to the **lateral cerebellar
    hemisphere** — the **cognitive-affective cerebrocerebellar**
    functional zone. **Cognitive-affective cerebrocerebellar relay**
    is the functional system subserved primarily by the lateral pontine
    nucleus.

*   **Nucleus reticularis tegmenti pontis (NRTP)** — the **dorsal**
    sub-nucleus that is **sometimes treated** as a separate structure
    (see the *NRTP Boundary* below). It **receives** inputs from the
    **cerebral cortex** (including the **frontal eye fields** and the
    **somatosensory cortex**) and **projects** to the **oculomotor
    vermis** and the **fastigial nucleus** — it **contributes** to
    **saccade adaptation** and **cerebellar control of eye movements**.
    **Saccade adaptation and oculomotor cerebellar relay** is the
    functional system subserved primarily by the NRTP.

**These sub-nuclei are prose subdivisions** — the tree does **not** wire
them as structural children of ``left`` or ``right`` (the ``left`` and
``right`` sub-containers have **no structural children** at the tree
level). Consumers resolving **sub-nucleus-level** detail go **through**
the ``left`` or ``right`` sub-container (which are **leaf modules** at
the tree level with **prose subdivisions**), and should consult the
references for **sub-nucleus-level** detail.

The Pontine Nuclei / Corticopontine Fibers Boundary
---------------------------------------------------
This is the **grey-matter vs. white-matter AFFERENT** boundary:

*   **Pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that **receive** the corticopontine fibers.

*   **Corticopontine fibers** — the **white-matter descending axons**
    from the **cerebral cortex** to the **pontine nuclei** — the
    **afferent limb** of the cortico-ponto-cerebellar pathway.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**fibers** are white matter. **This distinction is clinically
load-bearing** — a **pontine nuclei lesion** causes **cerebrocerebellar
dysfunction**; a **corticopontine fiber lesion** causes **the same
clinical syndrome** (the pontine nuclei are cut off from their cortical
input). Consumers must **not** conflate the pontine nuclei with the
corticopontine fibers.

The Pontine Nuclei / Pontocerebellar Fibers Boundary
----------------------------------------------------
This is the **grey-matter vs. white-matter EFFERENT** boundary:

*   **Pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the pontocerebellar fibers.

*   **Pontocerebellar fibers** — the **white-matter crossing axons**
    from the pontine nuclei to the **contralateral cerebellar cortex**
    — the **efferent limb** of the cortico-ponto-cerebellar pathway.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**fibers** are white matter. **This distinction is clinically
load-bearing** — a **pontine nuclei lesion** causes **cerebrocerebellar
dysfunction**; a **pontocerebellar fiber lesion** causes **the same
clinical syndrome** (the pontine nuclei are cut off from their
cerebellar output). Consumers must **not** conflate the pontine nuclei
with the pontocerebellar fibers.

The Pontine Nuclei / Middle Cerebellar Peduncle Boundary
--------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tract the
pontocerebellar fibers FORM**:

*   **Pontine nuclei** (this module) — the **grey-matter neuron
    clusters**.

*   **Middle cerebellar peduncle** (brachium pontis) — the **white-matter
    tract** that **carries** the pontocerebellar fibers from the
    contralateral pontine nuclei to the contralateral cerebellar cortex
    — it is the **largest** of the **three cerebellar peduncles**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**peduncle** is white matter. **This distinction is clinically
load-bearing** — a **middle cerebellar peduncle lesion** causes
**cerebellar ataxia** and **dysmetria**; a **pontine nuclei lesion**
causes **cerebellar ataxia** as well, but the **associated signs**
differ (a pontine nuclei lesion may accompany **corticospinal tract**
involvement — **hemiparesis** — or **cranial nerve** involvement; a pure
middle cerebellar peduncle lesion is usually isolated cerebellar
ataxia). Consumers must **not** conflate the pontine nuclei with the
middle cerebellar peduncle.

The Pontine Nuclei / Corticospinal and Corticobulbar Tracts Boundary
--------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tracts the
nuclei are INTERSPERSED among**:

*   **Pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that are **interspersed** among the corticospinal and
    corticobulbar tracts.

*   **Corticospinal tract** and **corticobulbar tract** — the
    **white-matter descending tracts** that **run through** the
    **basilar pons** alongside the pontine nuclei — they **carry** the
    **upper motor neuron** axons from the **motor cortex** to the
    **spinal cord** and the **cranial nerve motor nuclei**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**tracts** are white matter. **This anatomical juxtaposition is a
classic source of confusion** — the pontine nuclei are **anatomically
intermingled** with the corticospinal and corticobulbar tracts (the
tracts run **through** the basilar pons, and the pontine nuclei are
**scattered among** them). Consumers must **not** conflate the pontine
nuclei with the corticospinal and corticobulbar tracts. **This
distinction is clinically load-bearing** — a **pontine nuclei lesion**
causes **cerebrocerebellar dysfunction**; a **corticospinal/corticobulbar
tract lesion** causes **upper motor neuron weakness** (hemiparesis,
pseudobulbar palsy). The **two can coexist** in a **pontine stroke** —
producing **combined cerebellar ataxia and hemiparesis** — but they are
**different structures**.

The Pontine Nuclei / Pontine Reticular Formation Boundary
---------------------------------------------------------
This is the **basilar pons vs. dorsal tegmentum** boundary:

*   **Pontine nuclei** (this module) — the **basilar pons grey-matter
    neuron clusters** — the **cortico-ponto-cerebellar relay**.

*   **Pontine reticular formation** — the **dorsal pontine tegmentum
    grey-matter region** — including the **PPRF**
    (``.../pons/paramedian_pontine_reticular_formation/``), the
    **parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``), the **caudal
    pontine reticular nucleus**, the **oral pontine reticular nucleus**,
    and other reticular nuclei.

**They are DIFFERENT STRUCTURES** — **different anatomical locations**
(basilar pons vs. dorsal tegmentum), **different functional systems**
(cortico-ponto-cerebellar vs. horizontal saccades, orofacial motor,
autonomic regulation, respiratory rhythm). **This anatomical
distinction is a classic source of confusion** — the "pontine reticular
formation" and the "pontine nuclei" are **both** in the pons, but they
are in **different anatomical regions** (dorsal tegmentum vs. basilar
pons) and **different functional systems**. Consumers must **not**
conflate the pontine nuclei with the pontine reticular formation or any
of its components.

The Pontine Nuclei / Dorsal Pontine Tegmentum Structures Boundary
-----------------------------------------------------------------
This is the **basilar pons vs. dorsal tegmentum** boundary — with the
**parabrachial area**, the **superior olivary complex**, the **cranial
nerve nuclei**, and the **locus coeruleus**:

*   **Pontine nuclei** (this module) — the **basilar pons grey-matter
    neuron clusters** — the **cortico-ponto-cerebellar relay**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``), **superior
    olivary complex** (``.../pons/superior_olivary_complex/left/`` and
    ``.../right/``), **cranial nerve nuclei**
    (``.../pons/cranial_nerve_nuclei/``), **locus coeruleus**
    (``.../pons/tegmentum/locus_coeruleus/``) — the **dorsal pontine
    tegmentum structures** — the **visceral-sensory and respiratory
    relay**, the **auditory brainstem relay**, the **CN V, VI, VII,
    VIII nuclei**, and the **noradrenergic nucleus**, respectively.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. visceral-sensory/respiratory/auditory/
cranial nerve motor/sensory/noradrenergic). Consumers must **not**
conflate the pontine nuclei with any of the **dorsal pontine tegmentum**
structures.

The Pontine Nuclei / Cerebellum Boundary
----------------------------------------
This is the **pontine source vs. cerebellar target** boundary:

*   **Pontine nuclei** (this module) — the **basilar pons grey-matter
    neuron clusters** that **project to** the contralateral cerebellar
    cortex via the pontocerebellar fibers and the middle cerebellar
    peduncle.

*   **Cerebellum** (``.../metencephalon/cerebellum/hemispheres/left/``
    and ``.../right/``) — the **metencephalic cerebellar half** — it
    has its **own nuclei** (dentate, fastigial, interposed) and its
    **own cortex**.

**They are DIFFERENT STRUCTURES** — the **pontine nuclei** are
**pontine**; the **cerebellum** is **cerebellar**. **The pontine nuclei
are the major source of cerebellar cortical afferents** — but they are
**not** the cerebellum itself. Consumers must **not** conflate the
pontine nuclei with the cerebellum.

The Pontine Nuclei / Nucleus Reticularis Tegmenti Pontis Boundary
-----------------------------------------------------------------
This is the **pontine nuclei vs. NRTP** boundary — a **prose-location
note**:

*   **Pontine nuclei** (this module) — the **basilar pons grey-matter
    neuron clusters** — the **cortico-ponto-cerebellar relay**.

*   **Nucleus reticularis tegmenti pontis (NRTP)** — the **dorsal
    pontine sub-nucleus** that is **sometimes treated** as a **separate
    structure** — it is a **cortico-ponto-cerebellar relay** (specifically
    for **saccade adaptation** and **cerebellar control of eye
    movements**).

**The NRTP is not wired as a structural child of the pontine nuclei in
the tree** — it is a **prose location** in the **pons**, not a
structural child. **Functionally**, the NRTP is **part of the pontine
nuclei complex** (it is a **dorsal pontine sub-nucleus**); **structurally**,
the tree does **not** wire it as a child of the pontine nuclei. Consumers
must **not** assume the NRTP is a **structural child** of the pontine
nuclei — it is a **prose location** and a **functional component**.

The Pontine Nuclei / SLEA Boundary
----------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Pontine nuclei** (this module) — **SLEA-FREE**. They are **not**
    an extended-amygdala component, and they carry **no SLEA warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The pontine nuclei are NOT part of the SLEA continuum.** They are a
**basilar pons cortico-ponto-cerebellar relay**, and they carry **no
SLEA warning**. Consumers must **not** import the SLEA warning into the
pontine nuclei.

Function in the Human Brain
---------------------------
The pontine nuclei's functions are **the relay of cortical input to the
contralateral cerebellar cortex** — the **cortico-ponto-cerebellar
pathway** — **NOT a single unified function**:

*   **Motor Cerebrocerebellar Relay (Peduncular Pontine Nucleus):** The
    **peduncular (ventral) pontine nucleus** **receives** inputs from
    the **primary motor cortex** (M1) and the **premotor cortex** (PMC)
    and **projects** to the **intermediate cerebellar hemisphere** — it
    **relays** the **motor cortical command** to the **cerebellar motor
    control circuit** (the **cerebrocerebellar** functional zone). The
    **cerebellum** then **modulates** the **motor command** (timing,
    coordination, error-based learning) and **projects back** to the
    **motor cortex** (via the **dentate nucleus** and the **thalamus**).
    **Motor cerebrocerebellar relay** is the functional system subserved
    primarily by the peduncular pontine nucleus.

*   **Cognitive-Affective Cerebrocerebellar Relay (Dorsal and Lateral
    Pontine Nuclei):** The **dorsal (superior) pontine nucleus** and the
    **lateral pontine nucleus** **receive** inputs from the
    **prefrontal cortex** (especially the **dorsolateral prefrontal
    cortex**), the **posterior parietal cortex**, and the **superior
    temporal cortex** and **project** to the **lateral cerebellar
    hemisphere** — they **relay** the **cognitive-affective cortical
    command** to the **cerebellar cognitive-affective control circuit**
    (the **cognitive-affective cerebrocerebellar** functional zone). The
    **cerebellum** then **modulates** the **cognitive-affective
    processing** (working memory, attention, language, social cognition,
    emotion regulation) and **projects back** to the **prefrontal** and
    **parietal** cortices (via the **dentate nucleus** and the
    **thalamus**). **Cognitive-affective cerebrocerebellar relay** is
    the functional system subserved primarily by the dorsal and lateral
    pontine nuclei.

*   **Spinocerebellar and Limbic-Cerebellar Relay (Median Pontine
    Nucleus):** The **median (paramedian) pontine nucleus** **receives**
    inputs from the **cingulate motor areas**, the **supplementary motor
    area**, and the **limbic cortex** and **projects** to the **vermis**
    and the **medial cerebellar hemisphere** — it **relays** the
    **limbic and cingulate cortical command** to the **cerebellar
    spinocerebellar and limbic-cerebellar circuits**. **Spinocerebellar
    and limbic-cerebellar relay** is the functional system subserved
    primarily by the median pontine nucleus.

*   **Saccade Adaptation and Oculomotor Cerebellar Relay (NRTP):** The
    **NRTP** **receives** inputs from the **cerebral cortex** (including
    the **frontal eye fields** and the **somatosensory cortex**) and
    **projects** to the **oculomotor vermis** and the **fastigial
    nucleus** — it **contributes** to **saccade adaptation** and
    **cerebellar control of eye movements**. **Saccade adaptation and
    oculomotor cerebellar relay** is the functional system subserved
    primarily by the NRTP.

*   **Topographic Organization:** The **pontine nuclei** are
    **topographically organized** — the **rostrocaudal** and
    **mediolateral** organization of the pontine nuclei reflects the
    **topography** of the cerebral cortex (source of corticopontine
    fibers) and the cerebellar cortex (target of pontocerebellar
    fibers). **This topographic organization** is the **neural
    substrate** of the **cerebrocerebellar functional topography** —
    each cortical region projects to a specific pontine sub-region, and
    each pontine sub-region projects to a specific cerebellar region.

*   **NOT a neural processor in the classical sense.** The pontine
    nuclei are a **relay** — they **receive** the corticopontine fibers
    from the cerebral cortex and **project** the pontocerebellar fibers
    to the contralateral cerebellar cortex. The **processing** of the
    cortical command happens in the **cerebral cortex** (the source) and
    the **cerebellum** (the target). The pontine nuclei are the
    **brainstem relay** — the **pontine node** that **relays** the
    **cortical command** to the **cerebellum**.

**The unifying theme:** the pontine nuclei are the **cortico-ponto-
cerebellar relay** — the **basilar pons grey-matter neuron clusters**
that **receive** the corticopontine fibers from the cerebral cortex and
**project** the pontocerebellar fibers to the contralateral cerebellar
cortex. They are a **bilateral container** (left and right sub-containers),
**topographically organized** (motor cerebrocerebellar relay; cognitive-
affective cerebrocerebellar relay; spinocerebellar and limbic-cerebellar
relay; saccade adaptation), **SLEA-free**, and **NOT the corticopontine
or pontocerebellar fibers** — the **fibers** are the white-matter tracts
that the nuclei **receive from** and **project to**.

Associated Disorders
--------------------
The pontine nuclei have **no named "pontine nuclei syndrome"** — their
clinical associations are **nucleus-specific** and **sub-nucleus-specific**:

*   **Pontine Nuclei Lesion — Cerebrocerebellar Dysfunction:** A lesion
    of the **pontine nuclei** (e.g. **pontine stroke**, **tumor**,
    **demyelination**) causes **cerebrocerebellar dysfunction** —
    **cerebellar ataxia**, **dysmetria** (overshoot or undershoot of
    voluntary movements), **dysarthria** (articulatory speech
    impairment), **intention tremor**, and — for lesions involving the
    **dorsal/lateral pontine nuclei** — the **cerebellar cognitive-
    affective syndrome** (CCAS: executive dysfunction, visuospatial
    deficits, language deficits, affective dysregulation). **The
    pan-modal cerebrocerebellar pattern** is the **substrate** of the
    **pontine nuclei** functions.

*   **Pontine Stroke — Combined Cerebellar Ataxia and Hemiparesis:** A
    **pontine stroke** (e.g. **basilar artery** perforator territory)
    involving the **pontine nuclei** and the **corticospinal tract**
    causes **combined cerebellar ataxia and hemiparesis** — the
    **pontine nuclei** are the **substrate** of the **cerebellar
    ataxia** component, and the **corticospinal tract** is the
    **substrate** of the **hemiparesis** component. **This combined
    pattern is the classic "pontine stroke" presentation** — and it is
    the **key clinical distinction** from a pure **cerebellar stroke**
    (cerebellar ataxia without hemiparesis) or a pure **corticospinal
    tract stroke** (hemiparesis without cerebellar ataxia).

*   **Cerebellar Cognitive-Affective Syndrome (CCAS) — Dorsal and
    Lateral Pontine Nuclei Involvement:** **CCAS** (also called
    **Schmahmann syndrome**) is a **cerebellar cognitive-affective
    syndrome** characterized by **executive dysfunction**,
    **visuospatial deficits**, **language deficits** (agrammatism,
    anomia), and **affective dysregulation** (anxiety, depression,
    impulsivity). **The dorsal and lateral pontine nuclei** — which
    **relay** the **prefrontal** and **posterior parietal** cortical
    input to the **lateral cerebellar hemisphere** — are **one of the
    neural substrates** of the **cerebellar cognitive-affective
    circuit**, and their dysfunction may **contribute** to **CCAS**.

*   **Cerebellar Motor Syndrome — Peduncular Pontine Nucleus
    Involvement:** **Cerebellar motor syndrome** is characterized by
    **ataxia**, **dysmetria**, **dysarthria**, **intention tremor**, and
    **oculomotor abnormalities**. **The peduncular pontine nucleus** —
    which **relays** the **motor cortical input** to the **intermediate
    cerebellar hemisphere** — is **one of the neural substrates** of the
    **cerebellar motor circuit**, and its dysfunction may **contribute**
    to the **cerebellar motor syndrome**.

*   **Saccade Adaptation Deficit — NRTP Involvement:** **Saccade
    adaptation** is the **cerebellar recalibration** of **saccade
    amplitude** in response to **visual errors** (e.g. **inaccuracy** in
    reaching a visual target). **The NRTP** — which **relays** the
    **cortical** (including **frontal eye fields**) and **somatosensory**
    input to the **oculomotor vermis** and the **fastigial nucleus** —
    is **one of the neural substrates** of **saccade adaptation**, and
    its dysfunction may **contribute** to **saccade adaptation
    deficits** (e.g. **dysmetric saccades** that do not correct over
    time).

*   **Cerebellar Mutism Syndrome (Posterior Fossa Syndrome) — Pontine
    Nuclei Involvement:** **Cerebellar mutism syndrome** (also called
    **posterior fossa syndrome**) is a **complication** of **posterior
    fossa surgery** (especially **medulloblastoma resection**) —
    characterized by **transient mutism**, **emotional lability**, and
    **cerebellar motor deficits**. **The pontine nuclei** — which
    **relay** the **cerebrocerebellar** projections — are **one of the
    neural substrates** of the **cerebrocerebellar** circuit, and their
    **dysfunction** (e.g. from **surgical retraction** or **edema**) may
    **contribute** to the **mutism** and **affective** components of
    **cerebellar mutism syndrome**.

*   **No Named "Pontine Nuclei Syndrome":** The pontine nuclei are a
    **bilateral container** of **topographically organized sub-nuclei** —
    they have **no named clinical syndrome** of their own. Their
    clinical relevance is **cerebrocerebellar-specific** —
    **cerebellar ataxia**, **dysmetria**, **dysarthria**, **intention
    tremor**, **cerebellar cognitive-affective syndrome**, and **saccade
    adaptation deficits**.

**What is NOT here:** The pontine nuclei are **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **trigeminal neuralgia** (trigeminal nerve root), **Bell's palsy**
(facial nerve), **Wallenberg syndrome** (lateral medulla), **locked-in
syndrome** (bilateral ventral pons — but **sparing the dorsal
tegmentum**), or **internuclear ophthalmoplegia** (MLF). Its clinical
relevance is **cerebrocerebellar-specific**, via the **topographically
organized pontine sub-nuclei** it subserves. **No named pontine nuclei
syndrome exists.**

Lateralization Notes
--------------------
This is the **bilateral** pontine nuclei container. The pontine nuclei
are **bilaterally symmetric** with the **right** and **left**
sub-containers **strictly mirrored** — and they carry **NO warning at
the container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right**
    sub-containers are **structurally identical** — same prose
    subdivisions (median, peduncular, dorsal, lateral, NRTP) under each,
    same functional system (cortico-ponto-cerebellar relay), same
    bilateral framing. The bilateral symmetry is **strict**.

*   **Contralateral Cerebellar Projection (Structural Fact, NOT a
    Lateralization Warning):** The **left pontine nuclei** **project**
    to the **right cerebellar cortex** via the **right pontocerebellar
    fibers** and the **right middle cerebellar peduncle**; the **right
    pontine nuclei** **project** to the **left cerebellar cortex** via
    the **left pontocerebellar fibers** and the **left middle
    cerebellar peduncle**. **This crossed projection** is a **structural
    fact** of the **cortico-ponto-cerebellar pathway** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **cerebellar control of the ipsilateral body** (the cerebellum
    controls the **ipsilateral** side of the body, and the **crossed
    pontocerebellar projection** is the **first decussation** in the
    cerebrocerebellar pathway).

*   **Ipsilateral Corticopontine Input (Structural Fact, NOT a
    Lateralization Warning):** The **left pontine nuclei** **receive**
    corticopontine fibers from the **left cerebral cortex** (primarily
    **ipsilateral**); the **right pontine nuclei** receive
    corticopontine fibers from the **right cerebral cortex** (primarily
    **ipsilateral**). **This ipsilateral input** is a **structural
    fact** of the **cortico-ponto-cerebellar pathway** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **ipsilateral cortical command** that is then **crossed** to the
    **contralateral cerebellum**.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The pontine
    nuclei are **SLEA-free** — they are **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the pontine nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the pontine
    nuclei are CORTICO-PONTO-CEREBELLAR RELAY, not the fear-output):**
    The **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The pontine nuclei are a
    **basilar pons cortico-ponto-cerebellar relay** — consumers must
    **not** conflate them with the **amygdala** or with the **fear
    circuit**.

**A consumer that assumes "left pontine nuclei = right pontine nuclei"
will be structurally correct** — the two sides are **strictly
symmetric** (the contralateral cerebellar projection and the ipsilateral
corticopontine input are structural facts, not lateralizations). The
pontine nuclei are a **strict-mirror pair with NO warning at the
container level** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The container is **bilateral**, but
    it does **not** import ``left`` or ``right`` at module level — it
    exposes them as **structural children** and lets consumers resolve
    them through the memory/recall layer.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../pons/tegmentum/``, ``.../pons/parabrachial_area/``,
    ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``, ``.../pons/paramedian_pontine_
    reticular_formation/``, ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../metencephalon/cerebellum/``, or any other container. The
    pontine nuclei's relationships to the **corticopontine fibers**, the
    **pontocerebellar fibers**, the **middle cerebellar peduncle**, the
    **corticospinal** and **corticobulbar tracts**, the **pontine
    reticular formation**, the **dorsal pontine tegmentum structures**,
    the **cerebellum**, the **NRTP**, and the **SLEA continuum** are
    documented as **prose and boundary data**, not as structural parents
    or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children `left` and `right`.** The
    ``left`` and ``right`` sub-containers are **bilateral sub-containers**
    whose **sub-nuclei** (median, peduncular, dorsal, lateral, NRTP) are
    **prose subdivisions**, not structural children.
*   **BILATERAL CONTAINER — left and right are STRUCTURALLY SYMMETRIC.**
    The ``left`` and ``right`` sub-containers are a **strict-mirror
    pair** with **no warning at the container level**. Any lateralization
    is documented **inside the left and right sub-containers** and in the
    **Lateralization Notes**.
*   **GREY-MATTER NUCLEI — NOT the corticopontine or pontocerebellar
    fibers.** The **pontine nuclei** are the **grey-matter neuron
    clusters**; the **corticopontine fibers** and **pontocerebellar
    fibers** are the **white-matter tracts** that the nuclei receive
    from and project to. Consumers must **not** conflate the two.
*   **NOT the middle cerebellar peduncle — that is the WHITE-MATTER TRACT
    the pontocerebellar fibers form.** The **middle cerebellar peduncle**
    is white matter; the **pontine nuclei** are grey matter. Consumers
    must **not** conflate the two.
*   **NOT the corticospinal and corticobulbar tracts — those are the
    WHITE-MATTER TRACTS the nuclei are INTERSPERSED among.** The
    corticospinal and corticobulbar tracts run **through** the basilar
    pons; the pontine nuclei are **scattered among** them. **This
    anatomical juxtaposition is a classic source of confusion** —
    consumers must **not** conflate the two.
*   **NOT the pontine reticular formation — that is the DORSAL PONTINE
    TEGMENTUM.** The **pontine reticular formation** is the **dorsal
    pontine tegmentum**; the **pontine nuclei** are the **basilar
    pons**. Consumers must **not** conflate the two.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, or the locus coeruleus — those are DORSAL
    PONTINE TEGMENTUM structures.** Consumers must **not** conflate the
    pontine nuclei with any of the **dorsal pontine tegmentum**
    structures.
*   **NOT the cerebellum — that is the METENCEPHALIC SIBLING the
    pontocerebellar fibers project to.** The **cerebellum** and the
    **pontine nuclei** are **different structures**. Consumers must
    **not** conflate the two.
*   **TOPOGRAPHICALLY ORGANIZED — MULTIPLE sub-nuclei with different
    cortical inputs and different cerebellar targets.** The **sub-nuclei**
    (median, peduncular, dorsal, lateral, NRTP) are **prose
    subdivisions**, not structural children. Consumers must **not** treat
    the pontine nuclei as a single uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The pontine nuclei
    are **not** an extended-amygdala component, and they carry **no SLEA
    warning**.
*   **NOT the fear-output — the pontine nuclei are CORTICO-PONTO-
    CEREBELLAR RELAY.** The **fear-output** structure is the **central
    nucleus**; the **fear-learning** structures are the **basolateral
    nuclei**; the **fear-modulatory / extinction** structures are the
    **basomedial nuclei**. The **pontine nuclei** are a **basilar pons
    cortico-ponto-cerebellar relay** — they are **not** part of the fear
    circuit.
*   **No ``AREA_PATHS`` hop.** The pontine nuclei are a local container
    under the pons container, not a cross-listed container.
*   **No nested cross-listing.** The pontine nuclei have no nested
    dual-framing module. They are a single bilateral container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import pontine_nuclei

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.pontine_nuclei"
    )

**Do not** assume the pontine nuclei are a **leaf**. They are a
**container** — their structural children are ``left`` and ``right``, the
**bilateral sub-containers** of the pontine nuclear complex.

**Do not** assume the **sub-nuclei** (median, peduncular, dorsal,
lateral, NRTP) are **direct structural children** of the pontine nuclei.
They are **prose subdivisions** under ``left`` and ``right``.

**Do not** assume the pontine nuclei are the **corticopontine fibers**
or the **pontocerebellar fibers**. The **corticopontine fibers** are the
**afferent white-matter tract**; the **pontocerebellar fibers** are the
**efferent white-matter tract**. The **pontine nuclei** are the
**grey-matter neuron clusters** that receive and give rise to them.

**Do not** assume the pontine nuclei are the **middle cerebellar
peduncle**. The **middle cerebellar peduncle** is the **white-matter
tract** that carries the pontocerebellar fibers; the **pontine nuclei**
are the **grey-matter source** of those fibers.

**Do not** assume the pontine nuclei are the **corticospinal** or
**corticobulbar tracts**. Those are the **white-matter descending
tracts** that run **through** the basilar pons; the **pontine nuclei**
are **interspersed among** them.

**Do not** assume the pontine nuclei are the **pontine reticular
formation**, the **parabrachial area**, the **superior olivary
complex**, the **cranial nerve nuclei**, or the **locus coeruleus**.
Those are **dorsal pontine tegmentum structures**; the **pontine
nuclei** are the **basilar pons**.

**Do not** assume the pontine nuclei are the **cerebellum**. The
**cerebellum** is the **metencephalic sibling** that the **pontocerebellar
fibers** project to; the **pontine nuclei** are the **pontine source**
of those fibers.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the pontine nuclei. **The pontine nuclei are SLEA-FREE** —
they are **not** an extended-amygdala component, and they are **NOT part
of the fear circuit**.

Iterating the pontine nuclei's structural children (recommended consumer
pattern)::

    PONTINE_NUCLEI_CHILDREN = ("left", "right")
    # The container is bilateral. The sub-nuclei (median, peduncular,
    # dorsal, lateral, NRTP) are prose subdivisions under left and right
    # — not structural children.

Iterating the pontine nuclei's sub-nuclei (recommended consumer pattern
— through `left` or `right`)::

    for side in ("left", "right"):
        for sub in (
            "median_pontine_nucleus",
            "peduncular_pontine_nucleus",
            "dorsal_pontine_nucleus",
            "lateral_pontine_nucleus",
            "nucleus_reticularis_tegmenti_pontis",
        ):
            sub_path = (
                f"hindbrain.metencephalon.pons.pontine_nuclei."
                f"{side}.{sub}"
            )
            # resolve sub_path through the memory/recall layer

Reaching the corticopontine fibers (recommended consumer pattern — the
AFFERENT white-matter tract)::

    # The corticopontine fibers are the AFFERENT white-matter tract from
    # the cerebral cortex to the pontine nuclei:
    #
    #   .../white_matter/.../corticopontine_fibers/  (or equivalent path)
    #
    # The pontine nuclei RECEIVE the corticopontine fibers; the
    # corticopontine fibers are the AFFERENT limb of the
    # cortico-ponto-cerebellar pathway.

Reaching the pontocerebellar fibers (recommended consumer pattern — the
EFFERENT white-matter tract)::

    # The pontocerebellar fibers are the EFFERENT white-matter tract from
    # the pontine nuclei to the CONTRALATERAL cerebellar cortex:
    #
    #   .../white_matter/.../pontocerebellar_fibers/  (or equivalent path)
    #
    # The pontine nuclei GIVE RISE TO the pontocerebellar fibers; the
    # pontocerebellar fibers are the EFFERENT limb of the
    # cortico-ponto-cerebellar pathway.

Reaching the middle cerebellar peduncle (recommended consumer pattern —
the WHITE-MATTER TRACT the pontocerebellar fibers form)::

    # The middle cerebellar peduncle is the WHITE-MATTER tract that
    # carries the pontocerebellar fibers from the CONTRALATERAL pontine
    # nuclei to the CONTRALATERAL cerebellar cortex:
    #
    #   .../white_matter/.../middle_cerebellar_peduncle/  (or equivalent path)
    #
    # The pontine nuclei GIVE RISE TO the pontocerebellar fibers that FORM
    # the middle cerebellar peduncle.

Reaching the corticospinal and corticobulbar tracts (recommended
consumer pattern — the WHITE-MATTER DESCENDING TRACTS the nuclei are
INTERSPERSED among)::

    # The corticospinal and corticobulbar tracts are the WHITE-MATTER
    # descending tracts that run THROUGH the basilar pons:
    #
    #   .../white_matter/.../corticospinal_tract/  (and corticobulbar_tract)
    #
    # The pontine nuclei are INTERSPERSED among the corticospinal and
    # corticobulbar tracts — this anatomical juxtaposition is a classic
    # source of confusion.

Reaching the pontine reticular formation (recommended consumer pattern —
the DORSAL PONTINE TEGMENTUM)::

    # The pontine reticular formation is the DORSAL PONTINE TEGMENTUM
    # grey-matter region:
    #
    #   .../pons/paramedian_pontine_reticular_formation/
    #   .../pons/parvocellular_reticular_nucleus/
    #   .../pons/caudal_pontine_reticular_nucleus/  (and other reticular nuclei)
    #
    # The pontine nuclei are the BASILAR PONS grey-matter neuron clusters
    # — different anatomical location, different functional system.

Reaching the cerebellum (recommended consumer pattern — the
METENCEPHALIC SIBLING the pontocerebellar fibers project to)::

    # The cerebellum is the METENCEPHALIC SIBLING that the pontocerebellar
    # fibers project to (via the middle cerebellar peduncle):
    #
    #   .../metencephalon/cerebellum/hemispheres/left/  (and right/)
    #
    # The pontine nuclei are the PONTINE SOURCE of the cerebellar cortical
    # afferents; the cerebellum is the CEREBELLAR TARGET.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pn_path = (
            f"hindbrain.metencephalon.pons.pontine_nuclei.{side}"
        )
        # resolve pn_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The pontine nuclei's sub-nuclei are prose subdivisions, not
    # structural children:
    #   median (paramedian) pontine nucleus -> cingulate motor areas,
    #                                         supplementary motor area,
    #                                         limbic cortex -> vermis and
    #                                         medial cerebellar hemisphere;
    #                                         spinocerebellar and limbic-
    #                                         cerebellar relay
    #   peduncular (ventral) pontine nucleus -> primary motor cortex,
    #                                         premotor cortex -> intermediate
    #                                         cerebellar hemisphere;
    #                                         motor cerebrocerebellar relay
    #   dorsal (superior) pontine nucleus -> prefrontal cortex,
    #                                         posterior parietal cortex ->
    #                                         lateral cerebellar hemisphere;
    #                                         cognitive-affective
    #                                         cerebrocerebellar relay
    #   lateral pontine nucleus -> superior temporal cortex, posterior
    #                              parietal cortex, prefrontal cortex ->
    #                              lateral cerebellar hemisphere;
    #                              cognitive-affective cerebrocerebellar
    #                              relay
    #   nucleus reticularis tegmenti pontis (NRTP) -> cerebral cortex
    #                                         (including frontal eye fields),
    #                                         somatosensory cortex ->
    #                                         oculomotor vermis, fastigial
    #                                         nucleus; saccade adaptation
    #                                         and oculomotor cerebellar relay
    #
    # Do not attempt to resolve these as sub-paths of the pontine nuclei
    # — resolve them at the sub-nucleus level through the references.

References
----------
*   **Canonical pontine nuclei anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Pontine nuclei —
    cortico-ponto-cerebellar relay.)
*   **Cortico-ponto-cerebellar pathway — review:** Brodal, P. (1978).
    "The corticopontine projection in the rhesus monkey: origin and
    principles of organization." *Brain* 101:251–282. (Corticopontine
    projection — the afferent limb of the cortico-ponto-cerebellar
    pathway.)
*   **Cortico-ponto-cerebellar pathway — review:** Brodal, P., Bjaalie,
    J.G. (1992). "Organization of the pontine nuclei." *Neuroscience
    Research* 13:83–118. (Pontine nuclei — topographic organization;
    cortico-ponto-cerebellar relay.)
*   **Cerebrocerebellar functional topography:** Schmahmann, J.D.
    (1996). "From movement to thought: anatomic substrates of the
    cerebellar contribution to cognitive processing." *Human Brain
    Mapping* 4:174–198. (Cerebrocerebellar functional topography —
    motor, cognitive, and affective zones.)
*   **Cerebellar cognitive-affective syndrome:** Schmahmann, J.D.,
    Sherman, J.C. (1998). "The cerebellar cognitive affective syndrome."
    *Brain* 121:561–579. (Cerebellar cognitive-affective syndrome —
    executive dysfunction, visuospatial deficits, language deficits,
    affective dysregulation.)
*   **Cerebellar motor syndrome:** Holmes, G. (1939). "The cerebellum of
    man." *Brain* 62:1–30. (Cerebellar motor syndrome — ataxia,
    dysmetria, dysarthria, intention tremor.)
*   **Pontine stroke — combined cerebellar ataxia and hemiparesis:**
    Bassetti, C., Bogousslavsky, J., Barth, A., Regli, F. (1996). "Isolated
    infarcts of the pontine nuclei: a clinical and neuroimaging study."
    *Brain* 119:1237–1253. (Pontine nuclei infarction — cerebellar ataxia,
    dysarthria, and (when the corticospinal tract is involved)
    hemiparesis.)
*   **Cerebellar mutism syndrome (posterior fossa syndrome):** Pollack,
    I.F. (1997). "Cerebellar mutism and pseudobulbar palsy after
    resection of a cerebellar tumor." *Pediatric Neurosurgery*
    27:269–277. (Cerebellar mutism syndrome — transient mutism, emotional
    lability, cerebellar motor deficits; pontine nuclei involvement
    proposed.)
*   **NRTP — saccade adaptation:** Thier, P., Möck, M. (2006). "The
    oculomotor role of the pontine nuclei and the nucleus reticularis
    tegmenti pontis." *Progress in Brain Research* 151:293–320. (NRTP
    — saccade adaptation and oculomotor cerebellar relay.)
*   **Middle cerebellar peduncle (contrast — the white-matter tract the
    pontocerebellar fibers form):** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Middle cerebellar
    peduncle — brachium pontis; the white-matter tract that carries the
    pontocerebellar fibers.)
*   **Corticospinal and corticobulbar tracts (contrast — the white-matter
    descending tracts the nuclei are interspersed among):** Brodal, A.
    (2010). *The Central Nervous System: Structure and Function*, 4th ed.
    (Corticospinal and corticobulbar tracts — descending through the
    basilar pons alongside the pontine nuclei.)
*   **Pontine reticular formation (contrast — the dorsal pontine
    tegmentum):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Pontine reticular formation —
    dorsal pontine tegmentum; distinct from the pontine nuclei in the
    basilar pons.)
*   **Parabrachial area (contrast — the visceral-sensory and respiratory
    relay):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Parabrachial area —
    visceral-sensory and respiratory relay; distinct from the pontine
    nuclei.)
*   **Superior olivary complex (contrast — the auditory brainstem
    relay):** Grothe, B., Pecka, M., McAlpine, D. (2010). "Mechanisms of
    sound localization and coding in mammals." *Physiological Reviews*
    90:983–1012. (Superior olivary complex — auditory brainstem relay;
    distinct from the pontine nuclei.)
*   **Cerebellum (contrast — the metencephalic sibling the pontocerebellar
    fibers project to):** Manto, M., Gruol, D.L., Schmahmann, J.D.,
    Koibuchi, N., Rossi, F. (eds.) (2013). *Handbook of the Cerebellum
    and Cerebellar Disorders*. (Cerebellum — cerebellar target of the
    pontocerebellar fibers.)
*   **SLEA (contrast — the pontine nuclei are not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the pontine nuclei.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the pontine nuclei.)
*   NeuroNames — Pontine nuclei; FMA — Pontine nuclei.
"""
