"""
infrastructure.brainparts.hindbrain.metencephalon.pons.pontine_nuclei.right
===========================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── pontine_nuclei
                └── right   <-- THIS MODULE

**Primary synonym:** Right pontine nuclei; right pontine nuclear complex;
right nuclei pontis; right grey matter of the basilar pons; "the right
cortico-ponto-cerebellar relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**bilateral sub-container** of **brainstem grey-matter nuclei** — the
**right half** of the pontine nuclear complex, in the **right basilar
pons**, interspersed among the **right corticospinal** and **right
corticobulbar tracts** and continuous with the **right transverse pontine
fibers** that contribute to the **left middle cerebellar peduncle** (via
the **decussation of the pontocerebellar fibers**). It is the **right
pontine relay** for the **right cortico-ponto-cerebellar pathway** — the
**right cerebral cortex** to the **left cerebellar cortex**.
**Part of:** The **pontine_nuclei** container — specifically, the
**right half** of the **bilateral pontine nuclear complex**. The
**pontine_nuclei** container is the **cortico-ponto-cerebellar relay** of
the **basilar pons**; the **right** sub-container is its **right-side
structural child**.
**Structural parent:** ``.../pontine_nuclei/`` → **direct child** of the
pontine_nuclei container.
**Structural children:** **None.** This is a **leaf** module at the
**tree level** — but it is a **conceptual sub-container** of the **right
sub-nuclei** (right median/paramedian pontine nucleus, right peduncular
pontine nucleus, right dorsal pontine nucleus, right lateral pontine
nucleus, and right nucleus reticularis tegmenti pontis). The **sub-nuclei**
are documented as **prose subdivisions**, not as structural children.
**Boundary status (LEAF at tree level — CONCEPTUAL SUB-CONTAINER of
PROSE SUBDIVISIONS):** **Boundary case — the right pontine nuclei are a
LEAF at the TREE level, but a CONCEPTUAL SUB-CONTAINER of the right
sub-nuclei.** The tree wires the **right pontine nuclei** as a **single
`__init__.py`** — they have **no structural children**. The **right
median (paramedian) pontine nucleus**, **right peduncular (ventral)
pontine nucleus**, **right dorsal (superior) pontine nucleus**, **right
lateral pontine nucleus**, and **right nucleus reticularis tegmenti
pontis (NRTP)** are **prose subdivisions**, not structural children.
Consumers must **not** assume these sub-nuclei exist as structural
sub-modules — they must resolve sub-nucleus detail through the
references, not the tree.
**Boundary status (RIGHT HALF — NOT the whole pontine_nuclei container):**
**Boundary case — the right pontine nuclei are the RIGHT HALF of the
pontine_nuclei container, NOT the whole container.** The
**pontine_nuclei** container (``.../pontine_nuclei/``) has **two
structural children** — ``left`` and ``right``. The **right**
sub-container (here) is the **right-side** half only. Consumers must
**not** conflate the right pontine nuclei with the **whole pontine
nuclear complex** — the left side is a **separate structural
sibling**.
**Boundary status (NOT the left pontine nuclei — strict mirror, no
warning):** **Boundary case — the right pontine nuclei are NOT the left
pontine nuclei; the two are a STRICT MIRROR PAIR with NO warning at the
sub-container level.** The **left pontine nuclei**
(``.../pontine_nuclei/left/``) are the **structurally identical**
left-side counterpart — same prose subdivisions (median, peduncular,
dorsal, lateral, NRTP), same functional system
(cortico-ponto-cerebellar relay), same bilateral framing. The two sides
are **strictly mirrored** — any lateralization is documented **here, in
the Lateralization Notes**, not imported from elsewhere. Consumers must
**not** import a lateralization warning into the right pontine nuclei —
there is **none at the sub-container level** beyond the **crossed
cerebellar projection** documented below.
**Boundary status (GREY-MATTER NUCLEI — NOT the right corticopontine or
right pontocerebellar fibers):** **Boundary case — the right pontine
nuclei are the GREY-MATTER NUCLEI, NOT the right corticopontine or right
pontocerebellar fibers.** The **right corticopontine fibers** are the
**white-matter descending axons** from the **right cerebral cortex** to
the **right pontine nuclei** — the **afferent limb** of the **right
cortico-ponto-cerebellar pathway**. The **right pontocerebellar fibers**
are the **white-matter crossing axons** from the **right pontine
nuclei** to the **left cerebellar cortex** (via the **left middle
cerebellar peduncle**) — the **efferent limb** of the **right
cortico-ponto-cerebellar pathway**. The **right pontine nuclei** (here)
are the **grey-matter neuron clusters** that **receive** the right
corticopontine fibers and **give rise to** the right pontocerebellar
fibers. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey
matter; the **fibers** are white matter. **This distinction is
clinically load-bearing** — a **right pontine nuclei lesion** causes
**left cerebrocerebellar dysfunction** (the cerebellum controls the
**left** side of the body); a **right corticopontine fiber lesion**
causes **the same clinical syndrome** (the right pontine nuclei are cut
off from their right cortical input); a **right pontocerebellar fiber
lesion** causes **the same clinical syndrome** (the right pontine nuclei
are cut off from their left cerebellar output). Consumers must **not**
conflate the right pontine nuclei with the right corticopontine or right
pontocerebellar fibers.
**Boundary status (NOT the left middle cerebellar peduncle — that is
the WHITE-MATTER TRACT the right pontocerebellar fibers form):**
**Boundary case — the right pontine nuclei are NOT the left middle
cerebellar peduncle.** The **left middle cerebellar peduncle** (left
brachium pontis) is the **white-matter tract** that **carries** the
**right pontocerebellar fibers** from the **right pontine nuclei** to the
**left cerebellar cortex** — it is the **largest** of the **three left
cerebellar peduncles** and it carries the **right-sided** input to
the **left cerebellum**. The **right pontine nuclei** (here) are the
**grey-matter neuron clusters** that **give rise to** the right
pontocerebellar fibers that **form** the left middle cerebellar
peduncle. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey
matter; the **peduncle** is white matter. **This distinction is
clinically load-bearing** — a **left middle cerebellar peduncle
lesion** causes **left cerebellar ataxia** and **left dysmetria** (the
left cerebellar input from the right pontine nuclei is disrupted); a
**right pontine nuclei lesion** causes **left cerebellar ataxia** as
well (the right pontine nuclei are the source of the left middle
cerebellar peduncle's fibers) — the **distinction** is often made by
**associated brainstem signs** (a right pontine nuclei lesion may
accompany **right corticospinal tract** involvement — **left
hemiparesis** — or **right cranial nerve** involvement; a pure left
middle cerebellar peduncle lesion is usually isolated left cerebellar
ataxia). Consumers must **not** conflate the right pontine nuclei with
the left middle cerebellar peduncle.
**Boundary status (NOT the right corticospinal and right corticobulbar
tracts — those are the WHITE-MATTER TRACTS the nuclei are INTERSPERSED
among):** **Boundary case — the right pontine nuclei are NOT the right
corticospinal and right corticobulbar tracts.** The **right corticospinal
tract** and the **right corticobulbar tract** are the **white-matter
descending tracts** that **descend** through the **right basilar pons**
— they **carry** the **right upper motor neuron** axons from the **right
motor cortex** to the **left spinal cord** (via the **pyramidal
decussation** in the **medulla**) and the **cranial nerve motor
nuclei** (bilateral). The **right pontine nuclei** (here) are the
**grey-matter neuron clusters** that are **interspersed** among the
right corticospinal and right corticobulbar tracts in the **right basilar
pons**. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey
matter; the **tracts** are white matter. **This anatomical
juxtaposition is a classic source of confusion** — the right pontine
nuclei are **anatomically intermingled** with the right corticospinal
and right corticobulbar tracts (the tracts run **through** the right
basilar pons, and the right pontine nuclei are **scattered among** them),
and consumers must **not** conflate the right pontine nuclei with the
right corticospinal and right corticobulbar tracts. **This distinction is
clinically load-bearing** — a **right pontine nuclei lesion** causes
**left cerebrocerebellar dysfunction**; a **right corticospinal tract
lesion** causes **left upper motor neuron weakness** (left
hemiparesis); a **right corticobulbar tract lesion** causes
**contralateral** (or bilateral) **upper motor neuron weakness** of the
**facial** and **bulbar** muscles. The **two can coexist** in a **right
pontine stroke** — producing **combined left cerebellar ataxia and left
hemiparesis** — but they are **different structures**.
**Boundary status (NOT the pontine reticular formation — that is the
DORSAL PONTINE TEGMENTUM):** **Boundary case — the right pontine nuclei
are NOT the pontine reticular formation.** The **pontine reticular
formation** — the **paramedian pontine reticular formation (PPRF)**, the
**parvocellular reticular nucleus**, the **caudal pontine reticular
nucleus**, the **oral pontine reticular nucleus**, and other reticular
nuclei — is the **grey-matter region** in the **dorsal pontine
tegmentum** (the **dorsal** portion of the pons, as opposed to the
**basilar** portion). The **right pontine nuclei** (here) are the
**grey-matter neuron clusters** in the **right basilar pons** (the
**ventral** portion). They are **DIFFERENT STRUCTURES** — **different
anatomical locations** (right basilar pons vs. right dorsal tegmentum),
**different functional systems** (cortico-ponto-cerebellar relay vs.
horizontal saccades, orofacial motor, autonomic regulation, respiratory
rhythm). **This anatomical distinction is a classic source of
confusion** — the "pontine reticular formation" and the "pontine nuclei"
are **both** in the pons, but they are in **different anatomical
regions** (right dorsal tegmentum vs. right basilar pons) and **different
functional systems**. Consumers must **not** conflate the right pontine
nuclei with the pontine reticular formation or any of its components
(the PPRF, the parvocellular reticular nucleus, the caudal pontine
reticular nucleus, the oral pontine reticular nucleus).
**Boundary status (NOT the parabrachial area, the superior olivary
complex, the cranial nerve nuclei, or the locus coeruleus — those are
DORSAL PONTINE TEGMENTUM structures):** **Boundary case — the right
pontine nuclei are NOT the parabrachial area, the superior olivary
complex, the cranial nerve nuclei, or the locus coeruleus.** Those are
**dorsal pontine tegmentum structures** — the **parabrachial area** is
the **visceral-sensory and respiratory-relay complex**; the **superior
olivary complex** is the **auditory brainstem relay**; the **cranial
nerve nuclei** are the **CN V, VI, VII, VIII nuclei**; the **locus
coeruleus** is the **noradrenergic nucleus**. The **right pontine
nuclei** (here) are the **right basilar pons grey-matter neuron
clusters** — the **right cortico-ponto-cerebellar relay**. They are
**DIFFERENT STRUCTURES** — different anatomical locations (right basilar
pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. visceral-sensory/respiratory/auditory/
cranial nerve motor/sensory/noradrenergic). Consumers must **not**
conflate the right pontine nuclei with any of the **dorsal pontine
tegmentum** structures.
**Boundary status (NOT the cerebellum — that is the METENCEPHALIC
SIBLING the right pontocerebellar fibers project to):** **Boundary case
— the right pontine nuclei are NOT the cerebellum.** The **left
cerebellum** (``.../metencephalon/cerebellum/hemispheres/left/``) is
the **left metencephalic cerebellar half** — it has its **own nuclei**
(left dentate, left fastigial, left interposed) and its **own
cortex**. The **right pontine nuclei** (here) are the **right basilar
pons grey-matter neuron clusters** that **project to** the **left
cerebellar cortex** via the **right pontocerebellar fibers** and the
**left middle cerebellar peduncle**. They are **DIFFERENT STRUCTURES** —
the **right pontine nuclei** are **pontine**; the **cerebellum** is
**cerebellar**. **The right pontine nuclei are the major source of left
cerebellar cortical afferents** — but they are **not** the cerebellum
itself. Consumers must **not** conflate the right pontine nuclei with
the cerebellum.
**Boundary status (NOT a single uniform nucleus — MULTIPLE sub-nuclei
with different cortical inputs):** **Boundary case — the right pontine
nuclei are NOT a single uniform nucleus; they contain MULTIPLE sub-nuclei
with different cortical inputs and different cerebellar targets.** The
**right sub-nuclei** of the pontine nuclei include the **right median
(paramedian) pontine nucleus** (which receives input from the **right
cingulate motor areas** and the **right supplementary motor area** and
projects to the **left vermis** and the **left medial cerebellar
hemisphere** — the **spinocerebellar** and **limbic-cerebellar**
functional zones), the **right peduncular (ventral) pontine nucleus**
(which receives input from the **right primary motor cortex** and the
**right premotor cortex** and projects to the **left intermediate
cerebellar hemisphere** — the **motor cerebrocerebellar** functional
zone), the **right dorsal (superior) pontine nucleus** (which receives
input from the **right prefrontal cortex** and the **right posterior
parietal cortex** and projects to the **left lateral cerebellar
hemisphere** — the **cognitive-affective cerebrocerebellar** functional
zone), the **right lateral pontine nucleus** (which receives input from
the **right superior temporal cortex** and the **right posterior
parietal cortex** and projects to the **left lateral cerebellar
hemisphere** — the **cognitive-affective cerebrocerebellar** functional
zone), and the **right nucleus reticularis tegmenti pontis (NRTP)**
(which receives input from the **right cerebral cortex** and projects to
the **left oculomotor vermis** and the **left fastigial nucleus** —
**saccade adaptation** and **oculomotor cerebellar relay**). **These
sub-nuclei are prose subdivisions**, not structural children. Consumers
must **not** treat the right pontine nuclei as a single uniform nucleus
— they are a **functionally heterogeneous complex** with
**topographically organized** sub-nuclei.
**Boundary status (TOPOGRAPHICALLY ORGANIZED — the sub-nuclei are
organized by right cortical input and left cerebellar target):**
**Boundary case — the right pontine nuclei are TOPOGRAPHICALLY
ORGANIZED.** The **rostrocaudal** and **mediolateral** organization of
the **right pontine nuclei** reflects the **topography** of the **right
cerebral cortex** (the source of the right corticopontine fibers) and
the **left cerebellar cortex** (the target of the right pontocerebellar
fibers) — **each right cortical region projects to a specific right
pontine sub-region**, and **each right pontine sub-region projects to a
specific left cerebellar region**. **This topographic organization**
is the **neural substrate** of the **right-to-left cerebrocerebellar
functional topography** — the **right motor cortex** → **right peduncular
pontine nucleus** → **left intermediate cerebellar hemisphere** (motor
control); the **right prefrontal cortex** → **right dorsal/right lateral
pontine nucleus** → **left lateral cerebellar hemisphere**
(cognitive-affective control). **This topographic organization** is
**prose**, not structural children. Consumers must **not** assume the
right pontine nuclei are a **single uniform relay** — they are a
**topographically organized complex**.
**Boundary status (SLEA-FREE — the right pontine nuclei are NOT an
extended-amygdala component):** **Boundary case — the right pontine
nuclei are SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **right pontine nuclei** are a **basilar pons
cortico-ponto-cerebellar relay** — they are **NOT** an
extended-amygdala component, and they carry **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the right pontine
nuclei — they are **SLEA-free**.

Overview
--------
The right pontine nuclei are the **right half** of the **cortico-ponto-
cerebellar relay** of the **basilar pons** — the **right grey-matter
neuron clusters** in the **right basilar pons**, interspersed among the
**right corticospinal** and **right corticobulbar tracts** and continuous
with the **right transverse pontine fibers** that contribute to the
**left middle cerebellar peduncle** (via the **decussation of the
pontocerebellar fibers**). They are a **leaf** module at the **tree
level** under the ``right`` sub-container of the pontine_nuclei
container, but they are a **conceptual sub-container** of the **right
sub-nuclei** (right median, right peduncular, right dorsal, right lateral,
right NRTP) — **prose subdivisions**, not structural children.

**The right pontine nuclei are a LEAF at the TREE level, but a CONCEPTUAL
SUB-CONTAINER of the right sub-nuclei.** The tree wires the **right
pontine nuclei** as a **single `__init__.py`** — they have **no
structural children**. The **right median (paramedian) pontine
nucleus**, **right peduncular (ventral) pontine nucleus**, **right dorsal
(superior) pontine nucleus**, **right lateral pontine nucleus**, and
**right nucleus reticularis tegmenti pontis (NRTP)** are **prose
subdivisions**, not structural children.

**The right pontine nuclei are the RIGHT HALF of the pontine_nuclei
container, NOT the whole container.** The **pontine_nuclei** container
has **two structural children** — ``left`` and ``right``. The **right**
sub-container (here) is the **right-side** half only. The left side is a
**separate structural sibling**.

**The right pontine nuclei and the left pontine nuclei are a STRICT
MIRROR PAIR with NO warning at the sub-container level.** The two sides
are **structurally identical** — same prose subdivisions, same
functional system, same bilateral framing. Any lateralization is
documented **here, in the Lateralization Notes**, not imported from
elsewhere.

**The right pontine nuclei are GREY-MATTER NUCLEI, NOT the right
corticopontine or right pontocerebellar fibers.** The **right
corticopontine fibers** are the **afferent white-matter tract** from the
right cortex to the right pontine nuclei; the **right pontocerebellar
fibers** are the **efferent white-matter tract** from the right pontine
nuclei to the **left cerebellar cortex**. The **right pontine nuclei**
are the **grey-matter neuron clusters** that **receive** the right
corticopontine fibers and **give rise to** the right pontocerebellar
fibers.

**The right pontine nuclei are NOT the left middle cerebellar peduncle.**
The **left middle cerebellar peduncle** is the **white-matter tract**
that **carries** the right pontocerebellar fibers from the right pontine
nuclei to the left cerebellar cortex. The **right pontine nuclei** are
the **grey-matter source** of those fibers.

**The right pontine nuclei are NOT the right corticospinal and right
corticobulbar tracts.** Those are the **white-matter descending
tracts** that **run through** the right basilar pons; the **right pontine
nuclei** are **interspersed among** them. **This anatomical
juxtaposition is a classic source of confusion** — the nuclei and the
tracts are **anatomically intermingled** in the right basilar pons, but
they are **different structures** with **different clinical correlates**
(left cerebellar ataxia vs. left upper motor neuron weakness).

**The right pontine nuclei are NOT the pontine reticular formation.** The
**pontine reticular formation** is the **dorsal pontine tegmentum**; the
**right pontine nuclei** are the **right basilar pons**. They are
**different anatomical regions** with **different functional systems**.

**The right pontine nuclei are TOPOGRAPHICALLY ORGANIZED.** The **right
sub-nuclei** receive **topographically organized** right cortical inputs
and project to **topographically organized** left cerebellar targets.

**The right pontine nuclei are SLEA-FREE.** They are **not** an
extended-amygdala component, and they carry **no SLEA warning**.

Sub-Nucleus Composition (prose subdivisions, not structural children)
--------------------------------------------------------------------
The right pontine nuclei contain **five prose subdivisions** — documented
as **prose**, not as structural children:

*   **Right median (paramedian) pontine nucleus** — the **most medial**
    right sub-nucleus, adjacent to the **midline** and the **right
    raphe**. It **receives** inputs from the **right cingulate motor
    areas**, the **right supplementary motor area**, and the **right
    limbic cortex** and **projects** to the **left vermis** and the
    **left medial cerebellar hemisphere** — the **spinocerebellar**
    and **limbic-cerebellar** functional zones. **Spinocerebellar and
    limbic-cerebellar relay** is the functional system subserved
    primarily by the right median pontine nucleus.

*   **Right peduncular (ventral) pontine nucleus** — the **lateral** right
    sub-nucleus, adjacent to the **right cerebral peduncle** (the **right
    corticospinal** and **right corticobulbar** tracts) — the **largest**
    of the right pontine sub-nuclei. It **receives** inputs from the
    **right primary motor cortex** (M1) and the **right premotor cortex**
    (PMC) and **projects** to the **left intermediate cerebellar
    hemisphere** — the **motor cerebrocerebellar** functional zone.
    **Motor cerebrocerebellar relay** is the functional system subserved
    primarily by the right peduncular pontine nucleus.

*   **Right dorsal (superior) pontine nucleus** — the **dorsal** right
    sub-nucleus, adjacent to the **right pontine tegmentum**. It
    **receives** inputs from the **right prefrontal cortex** (especially
    the **right dorsolateral prefrontal cortex**) and the **right
    posterior parietal cortex** and **projects** to the **left lateral
    cerebellar hemisphere** — the **cognitive-affective
    cerebrocerebellar** functional zone. **Cognitive-affective
    cerebrocerebellar relay** is the functional system subserved
    primarily by the right dorsal pontine nucleus.

*   **Right lateral pontine nucleus** — the **far-lateral** right
    sub-nucleus. It **receives** inputs from the **right superior
    temporal cortex** (auditory association), the **right posterior
    parietal cortex**, and the **right prefrontal cortex** and
    **projects** to the **left lateral cerebellar hemisphere** — the
    **cognitive-affective cerebrocerebellar** functional zone.
    **Cognitive-affective cerebrocerebellar relay** is the functional
    system subserved primarily by the right lateral pontine nucleus.

*   **Right nucleus reticularis tegmenti pontis (NRTP)** — the **dorsal**
    right sub-nucleus that is **sometimes treated** as a separate
    structure (see the *NRTP Boundary* below). It **receives** inputs
    from the **right cerebral cortex** (including the **right frontal eye
    fields** and the **right somatosensory cortex**) and **projects** to
    the **left oculomotor vermis** and the **left fastigial nucleus**
    — it **contributes** to **saccade adaptation** and **cerebellar
    control of eye movements**. **Saccade adaptation and oculomotor
    cerebellar relay** is the functional system subserved primarily by
    the right NRTP.

**These sub-nuclei are prose subdivisions** — the tree does **not** wire
them as structural children of the **right pontine nuclei** (the **right
pontine nuclei** have **no structural children** at the tree level).
Consumers resolving **sub-nucleus-level** detail should consult the
references, not the tree.

The Right Pontine Nuclei / Left Pontine Nuclei Boundary
-------------------------------------------------------
This is the **strict-mirror** boundary:

*   **Right pontine nuclei** (this module) — the **right-side** pontine
    nuclear complex — the **right basilar pons cortico-ponto-cerebellar
    relay**.

*   **Left pontine nuclei** (``.../pontine_nuclei/left/``) — the
    **structurally identical** left-side pontine nuclear complex — the
    **left basilar pons cortico-ponto-cerebellar relay**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same prose
subdivisions, same functional system (cortico-ponto-cerebellar relay),
same bilateral framing. Any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere. Consumers must
**not** import a lateralization warning into the right pontine nuclei —
there is **none at the sub-container level** beyond the **crossed
cerebellar projection** documented below.

The Right Pontine Nuclei / Pontine Nuclei Container Boundary
------------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Right pontine nuclei** (this module) — the **right-side** half of
    the pontine nuclear complex.

*   **Pontine nuclei container** (``.../pontine_nuclei/``) — the **whole
    pontine nuclear complex**, with **two structural children** (``left``
    and ``right``).

**The right pontine nuclei are a child of the pontine nuclei container.**
Consumers must **not** conflate the right half with the **whole pontine
nuclear complex** — the left side is a **separate structural sibling**.

The Right Pontine Nuclei / Corticopontine Fibers Boundary
---------------------------------------------------------
This is the **grey-matter vs. white-matter AFFERENT** boundary:

*   **Right pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that **receive** the right corticopontine fibers.

*   **Right corticopontine fibers** — the **white-matter descending
    axons** from the **right cerebral cortex** to the **right pontine
    nuclei** — the **afferent limb** of the **right cortico-ponto-
    cerebellar pathway**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**fibers** are white matter. **This distinction is clinically
load-bearing** — a **right pontine nuclei lesion** causes **left
cerebrocerebellar dysfunction**; a **right corticopontine fiber lesion**
causes **the same clinical syndrome** (the right pontine nuclei are cut
off from their right cortical input). Consumers must **not** conflate
the right pontine nuclei with the right corticopontine fibers.

The Right Pontine Nuclei / Pontocerebellar Fibers Boundary
----------------------------------------------------------
This is the **grey-matter vs. white-matter EFFERENT** boundary:

*   **Right pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the right pontocerebellar fibers.

*   **Right pontocerebellar fibers** — the **white-matter crossing axons**
    from the **right pontine nuclei** to the **left cerebellar cortex**
    — the **efferent limb** of the **right cortico-ponto-cerebellar
    pathway**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**fibers** are white matter. **This distinction is clinically
load-bearing** — a **right pontine nuclei lesion** causes **left
cerebrocerebellar dysfunction**; a **right pontocerebellar fiber lesion**
causes **the same clinical syndrome** (the right pontine nuclei are cut
off from their left cerebellar output). Consumers must **not** conflate
the right pontine nuclei with the right pontocerebellar fibers.

The Right Pontine Nuclei / Left Middle Cerebellar Peduncle Boundary
-------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tract the
right pontocerebellar fibers FORM**:

*   **Right pontine nuclei** (this module) — the **grey-matter neuron
    clusters**.

*   **Left middle cerebellar peduncle** (left brachium pontis) — the
    **white-matter tract** that **carries** the right pontocerebellar
    fibers from the right pontine nuclei to the **left cerebellar
    cortex** — it is the **largest** of the **three left cerebellar
    peduncles**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**peduncle** is white matter. **This distinction is clinically
load-bearing** — a **left middle cerebellar peduncle lesion** causes
**left cerebellar ataxia** and **left dysmetria**; a **right pontine
nuclei lesion** causes **left cerebellar ataxia** as well, but the
**associated signs** differ (a right pontine nuclei lesion may accompany
**right corticospinal tract** involvement — **left hemiparesis** — or
**right cranial nerve** involvement; a pure left middle cerebellar
peduncle lesion is usually isolated left cerebellar ataxia). Consumers
must **not** conflate the right pontine nuclei with the left middle
cerebellar peduncle.

The Right Pontine Nuclei / Right Corticospinal and Right Corticobulbar Tracts Boundary
------------------------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tracts the
nuclei are INTERSPERSED among**:

*   **Right pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that are **interspersed** among the right corticospinal
    and right corticobulbar tracts.

*   **Right corticospinal tract** and **right corticobulbar tract** — the
    **white-matter descending tracts** that **run through** the **right
    basilar pons** alongside the right pontine nuclei — they **carry**
    the **right upper motor neuron** axons from the **right motor
    cortex** to the **left spinal cord** (via the **pyramidal
    decussation**) and the **cranial nerve motor nuclei**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**tracts** are white matter. **This anatomical juxtaposition is a
classic source of confusion** — the right pontine nuclei are
**anatomically intermingled** with the right corticospinal and right
corticobulbar tracts (the tracts run **through** the right basilar pons,
and the right pontine nuclei are **scattered among** them). Consumers
must **not** conflate the right pontine nuclei with the right
corticospinal and right corticobulbar tracts. **This distinction is
clinically load-bearing** — a **right pontine nuclei lesion** causes
**left cerebrocerebellar dysfunction**; a **right corticospinal tract
lesion** causes **left upper motor neuron weakness** (left
hemiparesis); a **right corticobulbar tract lesion** causes
**contralateral** (or bilateral) **upper motor neuron weakness** of the
**facial** and **bulbar** muscles. The **two can coexist** in a **right
pontine stroke** — producing **combined left cerebellar ataxia and left
hemiparesis** — but they are **different structures**.

The Right Pontine Nuclei / Pontine Reticular Formation Boundary
---------------------------------------------------------------
This is the **basilar pons vs. dorsal tegmentum** boundary:

*   **Right pontine nuclei** (this module) — the **right basilar pons
    grey-matter neuron clusters** — the **right cortico-ponto-cerebellar
    relay**.

*   **Pontine reticular formation** — the **dorsal pontine tegmentum
    grey-matter region** — including the **PPRF**
    (``.../pons/paramedian_pontine_reticular_formation/``), the
    **parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``), the **caudal
    pontine reticular nucleus**, the **oral pontine reticular nucleus**,
    and other reticular nuclei.

**They are DIFFERENT STRUCTURES** — **different anatomical locations**
(right basilar pons vs. dorsal tegmentum), **different functional
systems** (cortico-ponto-cerebellar vs. horizontal saccades, orofacial
motor, autonomic regulation, respiratory rhythm). **This anatomical
distinction is a classic source of confusion** — the "pontine reticular
formation" and the "pontine nuclei" are **both** in the pons, but they
are in **different anatomical regions** (dorsal tegmentum vs. basilar
pons) and **different functional systems**. Consumers must **not**
conflate the right pontine nuclei with the pontine reticular formation or
any of its components.

The Right Pontine Nuclei / Dorsal Pontine Tegmentum Structures Boundary
-----------------------------------------------------------------------
This is the **basilar pons vs. dorsal tegmentum** boundary — with the
**parabrachial area**, the **superior olivary complex**, the **cranial
nerve nuclei**, and the **locus coeruleus**:

*   **Right pontine nuclei** (this module) — the **right basilar pons
    grey-matter neuron clusters** — the **right cortico-ponto-cerebellar
    relay**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``), **superior
    olivary complex** (``.../pons/superior_olivary_complex/left/`` and
    ``.../right/``), **cranial nerve nuclei**
    (``.../pons/cranial_nerve_nuclei/``), **locus coeruleus**
    (``.../pons/tegmentum/locus_coeruleus/``) — the **dorsal pontine
    tegmentum structures** — the **visceral-sensory and respiratory
    relay**, the **auditory brainstem relay**, the **CN V, VI, VII,
    VIII nuclei**, and the **noradrenergic nucleus**, respectively.

**They are DIFFERENT STRUCTURES** — different anatomical locations
(right basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. visceral-sensory/respiratory/auditory/
cranial nerve motor/sensory/noradrenergic). Consumers must **not**
conflate the right pontine nuclei with any of the **dorsal pontine
tegmentum** structures.

The Right Pontine Nuclei / Cerebellum Boundary
----------------------------------------------
This is the **pontine source vs. cerebellar target** boundary:

*   **Right pontine nuclei** (this module) — the **right basilar pons
    grey-matter neuron clusters** that **project to** the **left
    cerebellar cortex** via the **right pontocerebellar fibers** and the
    **left middle cerebellar peduncle**.

*   **Left cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/left/``) — the **left
    metencephalic cerebellar half** — it has its **own nuclei** (left
    dentate, left fastigial, left interposed) and its **own cortex**.

**They are DIFFERENT STRUCTURES** — the **right pontine nuclei** are
**pontine**; the **left cerebellum** is **cerebellar**. **The right
pontine nuclei are the major source of left cerebellar cortical
afferents** — but they are **not** the left cerebellum itself.
Consumers must **not** conflate the right pontine nuclei with the
cerebellum.

The Right Pontine Nuclei / Right Nucleus Reticularis Tegmenti Pontis Boundary
----------------------------------------------------------------------------
This is the **prose-location note** boundary:

*   **Right pontine nuclei** (this module) — the **right basilar pons
    grey-matter neuron clusters** — the **right cortico-ponto-cerebellar
    relay**.

*   **Right nucleus reticularis tegmenti pontis (NRTP)** — the **dorsal
    pontine sub-nucleus** that is **sometimes treated** as a **separate
    structure** — it is a **right cortico-ponto-cerebellar relay**
    (specifically for **saccade adaptation** and **cerebellar control of
    eye movements**).

**The right NRTP is not wired as a structural child of the right pontine
nuclei in the tree** — it is a **prose subdivision** of the right pontine
nuclei, not a structural child. **Functionally**, the right NRTP is
**part of the right pontine nuclei complex** (it is a **right dorsal
pontine sub-nucleus**); **structurally**, the tree does **not** wire it
as a child of the right pontine nuclei. Consumers must **not** assume the
right NRTP is a **structural child** of the right pontine nuclei — it is
a **prose subdivision**.

The Right Pontine Nuclei / SLEA Boundary
----------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Right pontine nuclei** (this module) — **SLEA-FREE**. They are
    **not** an extended-amygdala component, and they carry **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The right pontine nuclei are NOT part of the SLEA continuum.** They are
a **basilar pons cortico-ponto-cerebellar relay**, and they carry **no
SLEA warning**. Consumers must **not** import the SLEA warning into the
right pontine nuclei.

Function in the Human Brain
---------------------------
The right pontine nuclei's functions are **the relay of right cortical
input to the left cerebellar cortex** — the **right cortico-ponto-
cerebellar pathway** — **NOT a single unified function**:

*   **Motor Cerebrocerebellar Relay (Right Peduncular Pontine Nucleus):**
    The **right peduncular (ventral) pontine nucleus** **receives**
    inputs from the **right primary motor cortex** (M1) and the **right
    premotor cortex** (PMC) and **projects** to the **left intermediate
    cerebellar hemisphere** — it **relays** the **right motor cortical
    command** to the **left cerebellar motor control circuit** (the
    **motor cerebrocerebellar** functional zone). The **left
    cerebellum** then **modulates** the **left-side motor command**
    (timing, coordination, error-based learning) and **projects back** to
    the **right motor cortex** (via the **left dentate nucleus** and the
    **thalamus**). **Motor cerebrocerebellar relay** is the functional
    system subserved primarily by the right peduncular pontine nucleus.

*   **Cognitive-Affective Cerebrocerebellar Relay (Right Dorsal and Right
    Lateral Pontine Nuclei):** The **right dorsal (superior) pontine
    nucleus** and the **right lateral pontine nucleus** **receive**
    inputs from the **right prefrontal cortex** (especially the **right
    dorsolateral prefrontal cortex**), the **right posterior parietal
    cortex**, and the **right superior temporal cortex** and **project**
    to the **left lateral cerebellar hemisphere** — they **relay** the
    **right cognitive-affective cortical command** to the **left
    cerebellar cognitive-affective control circuit** (the
    **cognitive-affective cerebrocerebellar** functional zone). The
    **left cerebellum** then **modulates** the **cognitive-affective
    processing** (working memory, attention, language, social cognition,
    emotion regulation) and **projects back** to the **right prefrontal**
    and **right parietal** cortices (via the **left dentate nucleus** and
    the **thalamus**). **Cognitive-affective cerebrocerebellar relay**
    is the functional system subserved primarily by the right dorsal and
    right lateral pontine nuclei.

*   **Spinocerebellar and Limbic-Cerebellar Relay (Right Median Pontine
    Nucleus):** The **right median (paramedian) pontine nucleus**
    **receives** inputs from the **right cingulate motor areas**, the
    **right supplementary motor area**, and the **right limbic cortex**
    and **projects** to the **left vermis** and the **left medial
    cerebellar hemisphere** — it **relays** the **right limbic and
    cingulate cortical command** to the **left cerebellar
    spinocerebellar and limbic-cerebellar circuits**. **Spinocerebellar
    and limbic-cerebellar relay** is the functional system subserved
    primarily by the right median pontine nucleus.

*   **Saccade Adaptation and Oculomotor Cerebellar Relay (Right NRTP):**
    The **right NRTP** **receives** inputs from the **right cerebral
    cortex** (including the **right frontal eye fields** and the **right
    somatosensory cortex**) and **projects** to the **left oculomotor
    vermis** and the **left fastigial nucleus** — it **contributes** to
    **saccade adaptation** and **cerebellar control of eye movements**.
    **Saccade adaptation and oculomotor cerebellar relay** is the
    functional system subserved primarily by the right NRTP.

*   **Topographic Organization:** The **right pontine nuclei** are
    **topographically organized** — the **rostrocaudal** and
    **mediolateral** organization reflects the **topography** of the
    **right cerebral cortex** (source of right corticopontine fibers) and
    the **left cerebellar cortex** (target of right pontocerebellar
    fibers). **This topographic organization** is the **neural
    substrate** of the **right-to-left cerebrocerebellar functional
    topography** — each right cortical region projects to a specific
    right pontine sub-region, and each right pontine sub-region projects
    to a specific left cerebellar region.

*   **NOT a neural processor in the classical sense.** The right pontine
    nuclei are a **relay** — they **receive** the right corticopontine
    fibers from the right cerebral cortex and **project** the right
    pontocerebellar fibers to the left cerebellar cortex. The
    **processing** of the right cortical command happens in the **right
    cerebral cortex** (the source) and the **left cerebellum** (the
    target). The right pontine nuclei are the **right brainstem relay**
    — the **right pontine node** that **relays** the **right cortical
    command** to the **left cerebellum**.

**The unifying theme:** the right pontine nuclei are the **right half of
the cortico-ponto-cerebellar relay** — the **right basilar pons
grey-matter neuron clusters** that **receive** the right corticopontine
fibers from the right cerebral cortex and **project** the right
pontocerebellar fibers to the left cerebellar cortex. They are a
**conceptual sub-container** (five prose sub-nuclei),
**topographically organized** (motor cerebrocerebellar relay;
cognitive-affective cerebrocerebellar relay; spinocerebellar and
limbic-cerebellar relay; saccade adaptation), **SLEA-free**, and **NOT
the right corticopontine or right pontocerebellar fibers** — the
**fibers** are the white-matter tracts that the nuclei **receive from**
and **project to**.

Associated Disorders
--------------------
The right pontine nuclei have **no named "right pontine nuclei
syndrome"** — their clinical associations are **sub-nucleus-specific**
and **topographic**:

*   **Right Pontine Nuclei Lesion — Left Cerebrocerebellar
    Dysfunction:** A lesion of the **right pontine nuclei** (e.g.
    **right pontine stroke**, **right pontine tumor**, **right pontine
    demyelination**) causes **left cerebrocerebellar dysfunction** —
    **left cerebellar ataxia**, **left dysmetria** (overshoot or
    undershoot of left-sided voluntary movements), **left dysarthria**
    (articulatory speech impairment — usually bilateral but may be
    asymmetric), **left intention tremor**, and — for lesions involving
    the **right dorsal/right lateral pontine nuclei** — the **cerebellar
    cognitive-affective syndrome** (CCAS: executive dysfunction,
    visuospatial deficits, language deficits, affective dysregulation).
    **The left pan-modal cerebrocerebellar pattern** is the **substrate**
    of the **right pontine nuclei** functions.

*   **Right Pontine Stroke — Combined Left Cerebellar Ataxia and Left
    Hemiparesis:** A **right pontine stroke** (e.g. **basilar artery**
    perforator territory) involving the **right pontine nuclei** and the
    **right corticospinal tract** causes **combined left cerebellar
    ataxia and left hemiparesis** — the **right pontine nuclei** are the
    **substrate** of the **left cerebellar ataxia** component, and the
    **right corticospinal tract** is the **substrate** of the **left
    hemiparesis** component. **This combined pattern is the classic
    "right pontine stroke" presentation** — and it is the **key clinical
    distinction** from a pure **left cerebellar stroke** (left cerebellar
    ataxia without left hemiparesis) or a pure **right corticospinal
    tract stroke** (left hemiparesis without left cerebellar ataxia).

*   **Cerebellar Cognitive-Affective Syndrome (CCAS) — Right Dorsal and
    Right Lateral Pontine Nuclei Involvement:** **CCAS** (also called
    **Schmahmann syndrome**) is a **cerebellar cognitive-affective
    syndrome** characterized by **executive dysfunction**,
    **visuospatial deficits**, **language deficits** (agrammatism,
    anomia), and **affective dysregulation** (anxiety, depression,
    impulsivity). **The right dorsal and right lateral pontine nuclei**
    — which **relay** the **right prefrontal** and **right posterior
    parietal** cortical input to the **left lateral cerebellar
    hemisphere** — are **one of the neural substrates** of the **left
    cerebellar cognitive-affective circuit**, and their dysfunction may
    **contribute** to **CCAS**.

*   **Cerebellar Motor Syndrome — Right Peduncular Pontine Nucleus
    Involvement:** **Cerebellar motor syndrome** is characterized by
    **left ataxia**, **left dysmetria**, **dysarthria**, **left
    intention tremor**, and **oculomotor abnormalities**. **The right
    peduncular pontine nucleus** — which **relays** the **right motor
    cortical input** to the **left intermediate cerebellar hemisphere**
    — is **one of the neural substrates** of the **left cerebellar
    motor circuit**, and its dysfunction may **contribute** to the
    **left cerebellar motor syndrome**.

*   **Saccade Adaptation Deficit — Right NRTP Involvement:** **Saccade
    adaptation** is the **cerebellar recalibration** of **saccade
    amplitude** in response to **visual errors**. **The right NRTP** —
    which **relays** the **right cortical** (including **right frontal
    eye fields**) and **right somatosensory** input to the **left
    oculomotor vermis** and the **left fastigial nucleus** — is **one of
    the neural substrates** of **saccade adaptation**, and its
    dysfunction may **contribute** to **saccade adaptation deficits**
    (e.g. **dysmetric saccades** that do not correct over time).

*   **Cerebellar Mutism Syndrome (Posterior Fossa Syndrome) — Right
    Pontine Nuclei Involvement:** **Cerebellar mutism syndrome** (also
    called **posterior fossa syndrome**) is a **complication** of
    **posterior fossa surgery** (especially **medulloblastoma
    resection**) — characterized by **transient mutism**, **emotional
    lability**, and **cerebellar motor deficits**. **The right pontine
    nuclei** — which **relay** the **right cerebrocerebellar**
    projections — are **one of the neural substrates** of the
    **cerebrocerebellar** circuit, and their **dysfunction** (e.g. from
    **surgical retraction** or **edema**) may **contribute** to the
    **mutism** and **affective** components of **cerebellar mutism
    syndrome**.

*   **No Named "Right Pontine Nuclei Syndrome":** The right pontine
    nuclei are a **conceptual sub-container** of **topographically
    organized sub-nuclei** — they have **no named clinical syndrome** of
    their own. Their clinical relevance is
    **left-cerebrocerebellar-specific** — **left cerebellar ataxia**,
    **left dysmetria**, **dysarthria**, **left intention tremor**,
    **cerebellar cognitive-affective syndrome**, and **saccade
    adaptation deficits**.

**What is NOT here:** The right pontine nuclei are **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **trigeminal neuralgia** (trigeminal nerve root), **Bell's palsy**
(facial nerve), **Wallenberg syndrome** (lateral medulla), or
**internuclear ophthalmoplegia** (MLF). Their clinical relevance is
**left-cerebrocerebellar-specific**, via the **topographically
organized right pontine sub-nuclei** they subserve. **No named right
pontine nuclei syndrome exists.**

Lateralization Notes
--------------------
This is the **right** sub-container of the pontine nuclei. The right
pontine nuclei are **bilaterally symmetric** with the left pontine
nuclei and **strictly mirrored** — and they carry **NO warning at the
sub-container level**:

*   **Strict Bilateral Symmetry:** The **right** and **left** pontine
    nuclei are **structurally identical** — same prose subdivisions
    (median, peduncular, dorsal, lateral, NRTP), same functional system
    (cortico-ponto-cerebellar relay), same bilateral framing. The
    bilateral symmetry is **strict**.

*   **Contralateral Cerebellar Projection (Structural Fact, NOT a
    Lateralization Warning):** The **right pontine nuclei** **project**
    to the **left cerebellar cortex** via the **right pontocerebellar
    fibers** and the **left middle cerebellar peduncle**. **This
    crossed projection** is a **structural fact** of the
    **cortico-ponto-cerebellar pathway** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **cerebellar
    control of the ipsilateral body** (the left cerebellum controls the
    **left** side of the body, and the **right pontine nuclei project**
    to the left cerebellum — the **crossed pontocerebellar projection**
    is the **first decussation** in the cerebrocerebellar pathway).
    **This is the neural substrate** of the **left cerebellar ataxia**
    in **right pontine nuclei lesions**.

*   **Ipsilateral Corticopontine Input (Structural Fact, NOT a
    Lateralization Warning):** The **right pontine nuclei** **receive**
    corticopontine fibers from the **right cerebral cortex** (primarily
    **ipsilateral**). **This ipsilateral input** is a **structural
    fact** of the **cortico-ponto-cerebellar pathway** — it is **not** a
    functional lateralization. It is the **neural substrate** of the
    **right cortical command** that is then **crossed** to the **left
    cerebellum**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The right pontine
    nuclei are **SLEA-free** — they are **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the right pontine nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the right pontine
    nuclei are CORTICO-PONTO-CEREBELLAR RELAY, not the fear-output):**
    The **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The right pontine nuclei are
    a **basilar pons cortico-ponto-cerebellar relay** — consumers must
    **not** conflate them with the **amygdala** or with the **fear
    circuit**. **Note**: the "right-amygdala" lateralization is about
    the **amygdala**, not about this right basilar pons relay — do not
    import it.

**A consumer that assumes "right pontine nuclei = left pontine nuclei"
will be structurally correct** — the two sides are **strictly
symmetric** (the contralateral cerebellar projection and the ipsilateral
corticopontine input are structural facts, not lateralizations). The
right pontine nuclei are a **strict-mirror pair with NO warning at the
sub-container level** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right sub-container is the
    **right half**; it does **not** import the left sub-container at
    module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../pontine_nuclei/left/``, ``.../pons/tegmentum/``,
    ``.../pons/parabrachial_area/``, ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../metencephalon/cerebellum/``, or any other container. The right
    pontine nuclei's relationships to the **right corticopontine
    fibers**, the **right pontocerebellar fibers**, the **left middle
    cerebellar peduncle**, the **right corticospinal** and **right
    corticobulbar tracts**, the **pontine reticular formation**, the
    **dorsal pontine tegmentum structures**, the **left cerebellum**,
    the **right NRTP**, and the **SLEA continuum** are documented as
    **prose and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf at tree level — conceptual sub-container of five prose
    subdivisions.** The **right median (paramedian) pontine nucleus**,
    **right peduncular (ventral) pontine nucleus**, **right dorsal
    (superior) pontine nucleus**, **right lateral pontine nucleus**, and
    **right nucleus reticularis tegmenti pontis (NRTP)** are documented
    as **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve sub-nucleus-level detail through the
    references.
*   **RIGHT HALF — NOT the whole pontine_nuclei container.** The
    **pontine_nuclei** container has **two structural children** —
    ``left`` and ``right``. The **right** sub-container (here) is the
    **right-side** half only.
*   **STRICT MIRROR with the left pontine nuclei — NO warning at the
    sub-container level.** The **right** and **left** pontine nuclei are
    **structurally identical**. Any lateralization is documented **inside
    the left and right sub-containers** and in the **Lateralization
    Notes**.
*   **GREY-MATTER NUCLEI — NOT the right corticopontine or right
    pontocerebellar fibers.** The **right pontine nuclei** are the
    **grey-matter neuron clusters**; the **right corticopontine fibers**
    and **right pontocerebellar fibers** are the **white-matter tracts**
    that the nuclei receive from and project to. Consumers must **not**
    conflate the two.
*   **NOT the left middle cerebellar peduncle — that is the WHITE-MATTER
    TRACT the right pontocerebellar fibers form.** Consumers must **not**
    conflate the two.
*   **NOT the right corticospinal and right corticobulbar tracts — those
    are the WHITE-MATTER TRACTS the nuclei are INTERSPERSED among.**
    **This anatomical juxtaposition is a classic source of confusion** —
    consumers must **not** conflate the two.
*   **NOT the pontine reticular formation — that is the DORSAL PONTINE
    TEGMENTUM.** Consumers must **not** conflate the right pontine nuclei
    with the pontine reticular formation or any of its components.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, or the locus coeruleus — those are DORSAL
    PONTINE TEGMENTUM structures.** Consumers must **not** conflate the
    right pontine nuclei with any of them.
*   **NOT the cerebellum — that is the METENCEPHALIC SIBLING the right
    pontocerebellar fibers project to.** Consumers must **not** conflate
    the two.
*   **TOPOGRAPHICALLY ORGANIZED — MULTIPLE sub-nuclei with different
    cortical inputs and different cerebellar targets.** The **right
    sub-nuclei** are **prose subdivisions**, not structural children.
    Consumers must **not** treat the right pontine nuclei as a single
    uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The right pontine
    nuclei are **not** an extended-amygdala component, and they carry
    **no SLEA warning**.
*   **NOT the fear-output — the right pontine nuclei are CORTICO-PONTO-
    CEREBELLAR RELAY.** Consumers must **not** conflate the right pontine
    nuclei with the fear circuit.
*   **No ``AREA_PATHS`` hop.** The right pontine nuclei are a local
    sub-container under the pontine_nuclei container, not a
    cross-listed sub-container.
*   **No nested cross-listing.** The right pontine nuclei have no nested
    dual-framing module. They are a single sub-container with five
    prose subdivisions.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.pontine_nuclei import right

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.pontine_nuclei.right"
    )

**Do not** assume the right pontine nuclei are a **structural container**.
They are a **leaf at the tree level** — with **five conceptual prose
subdivisions** (right median, right peduncular, right dorsal, right
lateral, right NRTP) that are **not** structural children.

**Do not** assume the right pontine nuclei are the **whole pontine_nuclei
container**. They are the **right-side half only** — the left side is a
**separate structural sibling**.

**Do not** assume the right pontine nuclei are the **left pontine
nuclei**. The two are a **strict mirror pair with NO warning at the
sub-container level** — any lateralization is documented **here, in the
Lateralization Notes**.

**Do not** assume the right pontine nuclei are the **right corticopontine
fibers** or the **right pontocerebellar fibers**. The **right
corticopontine fibers** are the **afferent white-matter tract**; the
**right pontocerebellar fibers** are the **efferent white-matter tract**.
The **right pontine nuclei** are the **grey-matter neuron clusters** that
receive and give rise to them.

**Do not** assume the right pontine nuclei are the **left middle
cerebellar peduncle**. The **left middle cerebellar peduncle** is the
**white-matter tract** that carries the right pontocerebellar fibers; the
**right pontine nuclei** are the **grey-matter source** of those fibers.

**Do not** assume the right pontine nuclei are the **right corticospinal**
or **right corticobulbar tracts**. Those are the **white-matter
descending tracts** that run **through** the right basilar pons; the
**right pontine nuclei** are **interspersed among** them.

**Do not** assume the right pontine nuclei are the **pontine reticular
formation**, the **parabrachial area**, the **superior olivary
complex**, the **cranial nerve nuclei**, or the **locus coeruleus**.
Those are **dorsal pontine tegmentum structures**; the **right pontine
nuclei** are the **right basilar pons**.

**Do not** assume the right pontine nuclei are the **left cerebellum**.
The **left cerebellum** is the **metencephalic sibling** that the
**right pontocerebellar fibers** project to; the **right pontine nuclei**
are the **pontine source** of those fibers.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the right pontine nuclei. **The right pontine nuclei are
SLEA-FREE** — they are **not** an extended-amygdala component, and they
are **NOT part of the fear circuit**. **Note**: the "right-amygdala"
lateralization is about the **amygdala**, not about this right basilar
pons relay — do not import it.

Iterating the right pontine nuclei's (empty) structural children
(recommended consumer pattern)::

    RIGHT_PONTINE_NUCLEI_CHILDREN = ()
    # The right pontine nuclei are a leaf at the tree level. The right
    # median, right peduncular, right dorsal, right lateral pontine nuclei,
    # and right NRTP are prose subdivisions, not structural children.

Reaching the right sub-nuclei (recommended consumer pattern — through
prose subdivision resolution)::

    for sub in (
        "median_pontine_nucleus",
        "peduncular_pontine_nucleus",
        "dorsal_pontine_nucleus",
        "lateral_pontine_nucleus",
        "nucleus_reticularis_tegmenti_pontis",
    ):
        sub_path = (
            f"hindbrain.metencephalon.pons.pontine_nuclei.right.{sub}"
        )
        # resolve sub_path through the memory/recall layer
        # (NOTE: this is a PROSE SUBDIVISION resolution, not a
        # structural child resolution — the right pontine nuclei
        # sub-nuclei are not wired as structural children.)

Reaching the right corticopontine fibers (recommended consumer pattern —
the AFFERENT white-matter tract)::

    # The right corticopontine fibers are the AFFERENT white-matter tract
    # from the right cerebral cortex to the right pontine nuclei:
    #
    #   .../white_matter/.../right_corticopontine_fibers/  (or equivalent path)
    #
    # The right pontine nuclei RECEIVE the right corticopontine fibers;
    # the right corticopontine fibers are the AFFERENT limb of the right
    # cortico-ponto-cerebellar pathway.

Reaching the right pontocerebellar fibers (recommended consumer pattern —
the EFFERENT white-matter tract)::

    # The right pontocerebellar fibers are the EFFERENT white-matter tract
    # from the right pontine nuclei to the LEFT cerebellar cortex:
    #
    #   .../white_matter/.../right_pontocerebellar_fibers/  (or equivalent path)
    #
    # The right pontine nuclei GIVE RISE TO the right pontocerebellar
    # fibers; the right pontocerebellar fibers are the EFFERENT limb of
    # the right cortico-ponto-cerebellar pathway.

Reaching the left middle cerebellar peduncle (recommended consumer
pattern — the WHITE-MATTER TRACT the right pontocerebellar fibers form)::

    # The left middle cerebellar peduncle is the WHITE-MATTER tract that
    # carries the right pontocerebellar fibers from the right pontine
    # nuclei to the LEFT cerebellar cortex:
    #
    #   .../white_matter/.../left_middle_cerebellar_peduncle/  (or equivalent path)
    #
    # The right pontine nuclei GIVE RISE TO the right pontocerebellar
    # fibers that FORM the left middle cerebellar peduncle.

Reaching the right corticospinal and right corticobulbar tracts
(recommended consumer pattern — the WHITE-MATTER DESCENDING TRACTS the
nuclei are INTERSPERSED among)::

    # The right corticospinal and right corticobulbar tracts are the
    # WHITE-MATTER descending tracts that run THROUGH the right basilar
    # pons:
    #
    #   .../white_matter/.../right_corticospinal_tract/  (and right_corticobulbar_tract)
    #
    # The right pontine nuclei are INTERSPERSED among the right
    # corticospinal and right corticobulbar tracts — this anatomical
    # juxtaposition is a classic source of confusion.

Reaching the pontine reticular formation (recommended consumer pattern —
the DORSAL PONTINE TEGMENTUM)::

    # The pontine reticular formation is the DORSAL PONTINE TEGMENTUM
    # grey-matter region:
    #
    #   .../pons/paramedian_pontine_reticular_formation/
    #   .../pons/parvocellular_reticular_nucleus/
    #   .../pons/caudal_pontine_reticular_nucleus/  (and other reticular nuclei)
    #
    # The right pontine nuclei are the RIGHT BASILAR PONS grey-matter
    # neuron clusters — different anatomical location, different
    # functional system.

Reaching the left cerebellum (recommended consumer pattern — the
METENCEPHALIC SIBLING the right pontocerebellar fibers project to)::

    # The left cerebellum is the METENCEPHALIC SIBLING that the right
    # pontocerebellar fibers project to (via the left middle cerebellar
    # peduncle):
    #
    #   .../metencephalon/cerebellum/hemispheres/left/
    #
    # The right pontine nuclei are the RIGHT PONTINE SOURCE of the left
    # cerebellar cortical afferents; the left cerebellum is the
    # CEREBELLAR TARGET.

Reaching the left pontine nuclei (recommended consumer pattern — the
strict mirror)::

    # The left pontine nuclei are the structurally identical LEFT half
    # of the pontine nuclear complex:
    #
    #   .../pons/pontine_nuclei/left/
    #
    # The right and left pontine nuclei are a STRICT MIRROR PAIR with NO
    # warning at the sub-container level.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pn_path = (
            f"hindbrain.metencephalon.pons.pontine_nuclei.{side}"
        )
        # resolve pn_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The right pontine nuclei's sub-nuclei are prose subdivisions, not
    # structural children:
    #   right median (paramedian) pontine nucleus -> right cingulate motor
    #                                         areas, right supplementary
    #                                         motor area, right limbic
    #                                         cortex -> left vermis, left
    #                                         medial cerebellar
    #                                         hemisphere; spinocerebellar
    #                                         and limbic-cerebellar relay
    #   right peduncular (ventral) pontine nucleus -> right primary motor
    #                                         cortex, right premotor
    #                                         cortex -> left intermediate
    #                                         cerebellar hemisphere; motor
    #                                         cerebrocerebellar relay
    #   right dorsal (superior) pontine nucleus -> right prefrontal cortex,
    #                                         right posterior parietal
    #                                         cortex -> left lateral
    #                                         cerebellar hemisphere;
    #                                         cognitive-affective
    #                                         cerebrocerebellar relay
    #   right lateral pontine nucleus -> right superior temporal cortex,
    #                              right posterior parietal cortex, right
    #                              prefrontal cortex -> left lateral
    #                              cerebellar hemisphere; cognitive-
    #                              affective cerebrocerebellar relay
    #   right nucleus reticularis tegmenti pontis (NRTP) -> right cerebral
    #                                         cortex (including right
    #                                         frontal eye fields), right
    #                                         somatosensory cortex ->
    #                                         left oculomotor vermis, left
    #                                         fastigial nucleus; saccade
    #                                         adaptation and oculomotor
    #                                         cerebellar relay
    #
    # Do not attempt to resolve these as sub-paths of the right pontine
    # nuclei — resolve them at the sub-nucleus level through the
    # references.

References
----------
*   **Canonical pontine nuclei anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Pontine nuclei —
    cortico-ponto-cerebellar relay; left and right halves.)
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
    Bassetti, C., Bogousslavsky, J., Barth, A., Regli, F. (1996).
    "Isolated infarcts of the pontine nuclei: a clinical and neuroimaging
    study." *Brain* 119:1237–1253. (Pontine nuclei infarction —
    cerebellar ataxia, dysarthria, and (when the corticospinal tract is
    involved) hemiparesis.)
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
*   **Left middle cerebellar peduncle (contrast — the white-matter tract
    the right pontocerebellar fibers form):** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed. (Left
    middle cerebellar peduncle — brachium pontis; the white-matter tract
    that carries the right pontocerebellar fibers.)
*   **Right corticospinal and right corticobulbar tracts (contrast — the
    white-matter descending tracts the nuclei are interspersed among):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Right corticospinal and right corticobulbar tracts
    — descending through the right basilar pons alongside the right
    pontine nuclei.)
*   **Pontine reticular formation (contrast — the dorsal pontine
    tegmentum):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Pontine reticular formation —
    dorsal pontine tegmentum; distinct from the right pontine nuclei in
    the right basilar pons.)
*   **Parabrachial area (contrast — the visceral-sensory and respiratory
    relay):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Parabrachial area —
    visceral-sensory and respiratory relay; distinct from the right
    pontine nuclei.)
*   **Superior olivary complex (contrast — the auditory brainstem
    relay):** Grothe, B., Pecka, M., McAlpine, D. (2010). "Mechanisms of
    sound localization and coding in mammals." *Physiological Reviews*
    90:983–1012. (Superior olivary complex — auditory brainstem relay;
    distinct from the right pontine nuclei.)
*   **Left cerebellum (contrast — the metencephalic sibling the right
    pontocerebellar fibers project to):** Manto, M., Gruol, D.L.,
    Schmahmann, J.D., Koibuchi, N., Rossi, F. (eds.) (2013). *Handbook
    of the Cerebellum and Cerebellar Disorders*. (Left cerebellum —
    cerebellar target of the right pontocerebellar fibers.)
*   **SLEA (contrast — the right pontine nuclei are not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the right pontine
    nuclei.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the right pontine nuclei. **Note**: the "right-amygdala"
    lateralization is about the **amygdala**, not about this right
    basilar pons relay.)
*   NeuroNames — Pontine nuclei (right); FMA — Pontine nuclei (right
    member).
"""
