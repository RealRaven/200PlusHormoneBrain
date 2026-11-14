"""
infrastructure.brainparts.hindbrain.metencephalon.pons.pontine_nuclei.left
==========================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── pontine_nuclei
                └── left   <-- THIS MODULE

**Primary synonym:** Left pontine nuclei; left pontine nuclear complex;
left nuclei pontis; left grey matter of the basilar pons; "the left
cortico-ponto-cerebellar relay."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**bilateral sub-container** of **brainstem grey-matter nuclei** — the
**left half** of the pontine nuclear complex, in the **left basilar
pons**, interspersed among the **left corticospinal** and **left
corticobulbar tracts** and continuous with the **left transverse pontine
fibers** that contribute to the **right middle cerebellar peduncle** (via
the **decussation of the pontocerebellar fibers**). It is the **left
pontine relay** for the **left cortico-ponto-cerebellar pathway** — the
**left cerebral cortex** to the **right cerebellar cortex**.
**Part of:** The **pontine_nuclei** container — specifically, the **left
half** of the **bilateral pontine nuclear complex**. The
**pontine_nuclei** container is the **cortico-ponto-cerebellar relay** of
the **basilar pons**; the **left** sub-container is its **left-side
structural child**.
**Structural parent:** ``.../pontine_nuclei/`` → **direct child** of the
pontine_nuclei container.
**Structural children:** **None.** This is a **leaf** module at the
**tree level** — but it is a **conceptual sub-container** of the **left
sub-nuclei** (left median/paramedian pontine nucleus, left peduncular
pontine nucleus, left dorsal pontine nucleus, left lateral pontine
nucleus, and left nucleus reticularis tegmenti pontis). The **sub-nuclei**
are documented as **prose subdivisions**, not as structural children.
**Boundary status (LEAF at tree level — CONCEPTUAL SUB-CONTAINER of
PROSE SUBDIVISIONS):** **Boundary case — the left pontine nuclei are a
LEAF at the TREE level, but a CONCEPTUAL SUB-CONTAINER of the left
sub-nuclei.** The tree wires the **left pontine nuclei** as a **single
`__init__.py`** — they have **no structural children**. The **left
median (paramedian) pontine nucleus**, **left peduncular (ventral)
pontine nucleus**, **left dorsal (superior) pontine nucleus**, **left
lateral pontine nucleus**, and **left nucleus reticularis tegmenti
pontis (NRTP)** are **prose subdivisions**, not structural children.
Consumers must **not** assume these sub-nuclei exist as structural
sub-modules — they must resolve sub-nucleus detail through the
references, not the tree.
**Boundary status (LEFT HALF — NOT the whole pontine_nuclei container):**
**Boundary case — the left pontine nuclei are the LEFT HALF of the
pontine_nuclei container, NOT the whole container.** The
**pontine_nuclei** container (``.../pontine_nuclei/``) has **two
structural children** — ``left`` and ``right``. The **left**
sub-container (here) is the **left-side** half only. Consumers must
**not** conflate the left pontine nuclei with the **whole pontine
nuclear complex** — the right side is a **separate structural
sibling**.
**Boundary status (NOT the right pontine nuclei — strict mirror, no
warning):** **Boundary case — the left pontine nuclei are NOT the right
pontine nuclei; the two are a STRICT MIRROR PAIR with NO warning at the
sub-container level.** The **right pontine nuclei**
(``.../pontine_nuclei/right/``) are the **structurally identical**
right-side counterpart — same prose subdivisions (median, peduncular,
dorsal, lateral, NRTP), same functional system
(cortico-ponto-cerebellar relay), same bilateral framing. The two sides
are **strictly mirrored** — any lateralization is documented **here, in
the Lateralization Notes**, not imported from elsewhere. Consumers must
**not** import a lateralization warning into the left pontine nuclei —
there is **none at the sub-container level** beyond the **crossed
cerebellar projection** documented below.
**Boundary status (GREY-MATTER NUCLEI — NOT the left corticopontine or
left pontocerebellar fibers):** **Boundary case — the left pontine
nuclei are the GREY-MATTER NUCLEI, NOT the left corticopontine or left
pontocerebellar fibers.** The **left corticopontine fibers** are the
**white-matter descending axons** from the **left cerebral cortex** to
the **left pontine nuclei** — the **afferent limb** of the **left
cortico-ponto-cerebellar pathway**. The **left pontocerebellar fibers**
are the **white-matter crossing axons** from the **left pontine
nuclei** to the **right cerebellar cortex** (via the **right middle
cerebellar peduncle**) — the **efferent limb** of the **left
cortico-ponto-cerebellar pathway**. The **left pontine nuclei** (here)
are the **grey-matter neuron clusters** that **receive** the left
corticopontine fibers and **give rise to** the left pontocerebellar
fibers. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey
matter; the **fibers** are white matter. **This distinction is
clinically load-bearing** — a **left pontine nuclei lesion** causes
**right cerebrocerebellar dysfunction** (the cerebellum controls the
**right** side of the body); a **left corticopontine fiber lesion**
causes **the same clinical syndrome** (the left pontine nuclei are cut
off from their left cortical input); a **left pontocerebellar fiber
lesion** causes **the same clinical syndrome** (the left pontine nuclei
are cut off from their right cerebellar output). Consumers must **not**
conflate the left pontine nuclei with the left corticopontine or left
pontocerebellar fibers.
**Boundary status (NOT the right middle cerebellar peduncle — that is
the WHITE-MATTER TRACT the left pontocerebellar fibers form):**
**Boundary case — the left pontine nuclei are NOT the right middle
cerebellar peduncle.** The **right middle cerebellar peduncle** (right
brachium pontis) is the **white-matter tract** that **carries** the
**left pontocerebellar fibers** from the **left pontine nuclei** to the
**right cerebellar cortex** — it is the **largest** of the **three
right cerebellar peduncles** and it carries the **left-sided** input to
the **right cerebellum**. The **left pontine nuclei** (here) are the
**grey-matter neuron clusters** that **give rise to** the left
pontocerebellar fibers that **form** the right middle cerebellar
peduncle. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey
matter; the **peduncle** is white matter. **This distinction is
clinically load-bearing** — a **right middle cerebellar peduncle
lesion** causes **right cerebellar ataxia** and **right dysmetria** (the
right cerebellar input from the left pontine nuclei is disrupted); a
**left pontine nuclei lesion** causes **right cerebellar ataxia** as
well (the left pontine nuclei are the source of the right middle
cerebellar peduncle's fibers) — the **distinction** is often made by
**associated brainstem signs** (a left pontine nuclei lesion may
accompany **left corticospinal tract** involvement — **right
hemiparesis** — or **left cranial nerve** involvement; a pure right
middle cerebellar peduncle lesion is usually isolated right cerebellar
ataxia). Consumers must **not** conflate the left pontine nuclei with
the right middle cerebellar peduncle.
**Boundary status (NOT the left corticospinal and left corticobulbar
tracts — those are the WHITE-MATTER TRACTS the nuclei are INTERSPERSED
among):** **Boundary case — the left pontine nuclei are NOT the left
corticospinal and left corticobulbar tracts.** The **left corticospinal
tract** and the **left corticobulbar tract** are the **white-matter
descending tracts** that **descend** through the **left basilar pons**
— they **carry** the **left upper motor neuron** axons from the **left
motor cortex** to the **right spinal cord** (via the **pyramidal
decussation** in the **medulla**) and the **cranial nerve motor
nuclei** (bilateral). The **left pontine nuclei** (here) are the
**grey-matter neuron clusters** that are **interspersed** among the
left corticospinal and left corticobulbar tracts in the **left basilar
pons**. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey
matter; the **tracts** are white matter. **This anatomical
juxtaposition is a classic source of confusion** — the left pontine
nuclei are **anatomically intermingled** with the left corticospinal
and left corticobulbar tracts (the tracts run **through** the left
basilar pons, and the left pontine nuclei are **scattered among** them),
and consumers must **not** conflate the left pontine nuclei with the
left corticospinal and left corticobulbar tracts. **This distinction is
clinically load-bearing** — a **left pontine nuclei lesion** causes
**right cerebrocerebellar dysfunction**; a **left corticospinal tract
lesion** causes **right upper motor neuron weakness** (right
hemiparesis); a **left corticobulbar tract lesion** causes
**contralateral** (or bilateral) **upper motor neuron weakness** of the
**facial** and **bulbar** muscles. The **two can coexist** in a **left
pontine stroke** — producing **combined right cerebellar ataxia and
right hemiparesis** — but they are **different structures**.
**Boundary status (NOT the pontine reticular formation — that is the
DORSAL PONTINE TEGMENTUM):** **Boundary case — the left pontine nuclei
are NOT the pontine reticular formation.** The **pontine reticular
formation** — the **paramedian pontine reticular formation (PPRF)**, the
**parvocellular reticular nucleus**, the **caudal pontine reticular
nucleus**, the **oral pontine reticular nucleus**, and other reticular
nuclei — is the **grey-matter region** in the **dorsal pontine
tegmentum** (the **dorsal** portion of the pons, as opposed to the
**basilar** portion). The **left pontine nuclei** (here) are the
**grey-matter neuron clusters** in the **left basilar pons** (the
**ventral** portion). They are **DIFFERENT STRUCTURES** — **different
anatomical locations** (left basilar pons vs. left dorsal tegmentum),
**different functional systems** (cortico-ponto-cerebellar relay vs.
horizontal saccades, orofacial motor, autonomic regulation, respiratory
rhythm). **This anatomical distinction is a classic source of
confusion** — the "pontine reticular formation" and the "pontine nuclei"
are **both** in the pons, but they are in **different anatomical
regions** (left dorsal tegmentum vs. left basilar pons) and **different
functional systems**. Consumers must **not** conflate the left pontine
nuclei with the pontine reticular formation or any of its components
(the PPRF, the parvocellular reticular nucleus, the caudal pontine
reticular nucleus, the oral pontine reticular nucleus).
**Boundary status (NOT the parabrachial area, the superior olivary
complex, the cranial nerve nuclei, or the locus coeruleus — those are
DORSAL PONTINE TEGMENTUM structures):** **Boundary case — the left
pontine nuclei are NOT the parabrachial area, the superior olivary
complex, the cranial nerve nuclei, or the locus coeruleus.** Those are
**dorsal pontine tegmentum structures** — the **parabrachial area** is
the **visceral-sensory and respiratory-relay complex**; the **superior
olivary complex** is the **auditory brainstem relay**; the **cranial
nerve nuclei** are the **CN V, VI, VII, VIII nuclei**; the **locus
coeruleus** is the **noradrenergic nucleus**. The **left pontine
nuclei** (here) are the **left basilar pons grey-matter neuron
clusters** — the **left cortico-ponto-cerebellar relay**. They are
**DIFFERENT STRUCTURES** — different anatomical locations (left basilar
pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. visceral-sensory/respiratory/auditory/
cranial nerve motor/sensory/noradrenergic). Consumers must **not**
conflate the left pontine nuclei with any of the **dorsal pontine
tegmentum** structures.
**Boundary status (NOT the cerebellum — that is the METENCEPHALIC
SIBLING the left pontocerebellar fibers project to):** **Boundary case
— the left pontine nuclei are NOT the cerebellum.** The **right
cerebellum** (``.../metencephalon/cerebellum/hemispheres/right/``) is
the **right metencephalic cerebellar half** — it has its **own nuclei**
(right dentate, right fastigial, right interposed) and its **own
cortex**. The **left pontine nuclei** (here) are the **left basilar pons
grey-matter neuron clusters** that **project to** the **right cerebellar
cortex** via the **left pontocerebellar fibers** and the **right middle
cerebellar peduncle**. They are **DIFFERENT STRUCTURES** — the **left
pontine nuclei** are **pontine**; the **cerebellum** is **cerebellar**.
**The left pontine nuclei are the major source of right cerebellar
cortical afferents** — but they are **not** the cerebellum itself.
Consumers must **not** conflate the left pontine nuclei with the
cerebellum.
**Boundary status (NOT a single uniform nucleus — MULTIPLE sub-nuclei
with different cortical inputs):** **Boundary case — the left pontine
nuclei are NOT a single uniform nucleus; they contain MULTIPLE sub-nuclei
with different cortical inputs and different cerebellar targets.** The
**left sub-nuclei** of the pontine nuclei include the **left median
(paramedian) pontine nucleus** (which receives input from the **left
cingulate motor areas** and the **left supplementary motor area** and
projects to the **right vermis** and the **right medial cerebellar
hemisphere** — the **spinocerebellar** and **limbic-cerebellar**
functional zones), the **left peduncular (ventral) pontine nucleus**
(which receives input from the **left primary motor cortex** and the
**left premotor cortex** and projects to the **right intermediate
cerebellar hemisphere** — the **motor cerebrocerebellar** functional
zone), the **left dorsal (superior) pontine nucleus** (which receives
input from the **left prefrontal cortex** and the **left posterior
parietal cortex** and projects to the **right lateral cerebellar
hemisphere** — the **cognitive-affective cerebrocerebellar** functional
zone), the **left lateral pontine nucleus** (which receives input from
the **left superior temporal cortex** and the **left posterior parietal
cortex** and projects to the **right lateral cerebellar hemisphere** —
the **cognitive-affective cerebrocerebellar** functional zone), and the
**left nucleus reticularis tegmenti pontis (NRTP)** (which receives
input from the **left cerebral cortex** and projects to the **right
oculomotor vermis** and the **right fastigial nucleus** —
**saccade adaptation** and **oculomotor cerebellar relay**). **These
sub-nuclei are prose subdivisions**, not structural children. Consumers
must **not** treat the left pontine nuclei as a single uniform nucleus
— they are a **functionally heterogeneous complex** with
**topographically organized** sub-nuclei.
**Boundary status (TOPOGRAPHICALLY ORGANIZED — the sub-nuclei are
organized by left cortical input and right cerebellar target):**
**Boundary case — the left pontine nuclei are TOPOGRAPHICALLY
ORGANIZED.** The **rostrocaudal** and **mediolateral** organization of
the **left pontine nuclei** reflects the **topography** of the **left
cerebral cortex** (the source of the left corticopontine fibers) and
the **right cerebellar cortex** (the target of the left pontocerebellar
fibers) — **each left cortical region projects to a specific left
pontine sub-region**, and **each left pontine sub-region projects to a
specific right cerebellar region**. **This topographic organization**
is the **neural substrate** of the **left-to-right cerebrocerebellar
functional topography** — the **left motor cortex** → **left peduncular
pontine nucleus** → **right intermediate cerebellar hemisphere** (motor
control); the **left prefrontal cortex** → **left dorsal/lateral
pontine nucleus** → **right lateral cerebellar hemisphere**
(cognitive-affective control). **This topographic organization** is
**prose**, not structural children. Consumers must **not** assume the
left pontine nuclei are a **single uniform relay** — they are a
**topographically organized complex**.
**Boundary status (SLEA-FREE — the left pontine nuclei are NOT an
extended-amygdala component):** **Boundary case — the left pontine
nuclei are SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **left pontine nuclei** are a **basilar pons
cortico-ponto-cerebellar relay** — they are **NOT** an
extended-amygdala component, and they carry **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the left pontine
nuclei — they are **SLEA-free**.

Overview
--------
The left pontine nuclei are the **left half** of the **cortico-ponto-
cerebellar relay** of the **basilar pons** — the **left grey-matter
neuron clusters** in the **left basilar pons**, interspersed among the
**left corticospinal** and **left corticobulbar tracts** and continuous
with the **left transverse pontine fibers** that contribute to the
**right middle cerebellar peduncle** (via the **decussation of the
pontocerebellar fibers**). They are a **leaf** module at the **tree
level** under the ``left`` sub-container of the pontine_nuclei
container, but they are a **conceptual sub-container** of the **left
sub-nuclei** (left median, left peduncular, left dorsal, left lateral,
left NRTP) — **prose subdivisions**, not structural children.

**The left pontine nuclei are a LEAF at the TREE level, but a CONCEPTUAL
SUB-CONTAINER of the left sub-nuclei.** The tree wires the **left
pontine nuclei** as a **single `__init__.py`** — they have **no
structural children**. The **left median (paramedian) pontine
nucleus**, **left peduncular (ventral) pontine nucleus**, **left dorsal
(superior) pontine nucleus**, **left lateral pontine nucleus**, and
**left nucleus reticularis tegmenti pontis (NRTP)** are **prose
subdivisions**, not structural children.

**The left pontine nuclei are the LEFT HALF of the pontine_nuclei
container, NOT the whole container.** The **pontine_nuclei** container
has **two structural children** — ``left`` and ``right``. The **left**
sub-container (here) is the **left-side** half only. The right side is a
**separate structural sibling**.

**The left pontine nuclei and the right pontine nuclei are a STRICT
MIRROR PAIR with NO warning at the sub-container level.** The two sides
are **structurally identical** — same prose subdivisions, same
functional system, same bilateral framing. Any lateralization is
documented **here, in the Lateralization Notes**, not imported from
elsewhere.

**The left pontine nuclei are GREY-MATTER NUCLEI, NOT the left
corticopontine or left pontocerebellar fibers.** The **left
corticopontine fibers** are the **afferent white-matter tract** from the
left cortex to the left pontine nuclei; the **left pontocerebellar
fibers** are the **efferent white-matter tract** from the left pontine
nuclei to the **right cerebellar cortex**. The **left pontine nuclei**
are the **grey-matter neuron clusters** that **receive** the left
corticopontine fibers and **give rise to** the left pontocerebellar
fibers.

**The left pontine nuclei are NOT the right middle cerebellar peduncle.**
The **right middle cerebellar peduncle** is the **white-matter tract**
that **carries** the left pontocerebellar fibers from the left pontine
nuclei to the right cerebellar cortex. The **left pontine nuclei** are
the **grey-matter source** of those fibers.

**The left pontine nuclei are NOT the left corticospinal and left
corticobulbar tracts.** Those are the **white-matter descending
tracts** that **run through** the left basilar pons; the **left pontine
nuclei** are **interspersed among** them. **This anatomical
juxtaposition is a classic source of confusion** — the nuclei and the
tracts are **anatomically intermingled** in the left basilar pons, but
they are **different structures** with **different clinical correlates**
(right cerebellar ataxia vs. right upper motor neuron weakness).

**The left pontine nuclei are NOT the pontine reticular formation.** The
**pontine reticular formation** is the **dorsal pontine tegmentum**; the
**left pontine nuclei** are the **left basilar pons**. They are
**different anatomical regions** with **different functional systems**.

**The left pontine nuclei are TOPOGRAPHICALLY ORGANIZED.** The **left
sub-nuclei** receive **topographically organized** left cortical inputs
and project to **topographically organized** right cerebellar targets.

**The left pontine nuclei are SLEA-FREE.** They are **not** an
extended-amygdala component, and they carry **no SLEA warning**.

Sub-Nucleus Composition (prose subdivisions, not structural children)
--------------------------------------------------------------------
The left pontine nuclei contain **five prose subdivisions** — documented
as **prose**, not as structural children:

*   **Left median (paramedian) pontine nucleus** — the **most medial**
    left sub-nucleus, adjacent to the **midline** and the **left
    raphe**. It **receives** inputs from the **left cingulate motor
    areas**, the **left supplementary motor area**, and the **left
    limbic cortex** and **projects** to the **right vermis** and the
    **right medial cerebellar hemisphere** — the **spinocerebellar**
    and **limbic-cerebellar** functional zones. **Spinocerebellar and
    limbic-cerebellar relay** is the functional system subserved
    primarily by the left median pontine nucleus.

*   **Left peduncular (ventral) pontine nucleus** — the **lateral** left
    sub-nucleus, adjacent to the **left cerebral peduncle** (the **left
    corticospinal** and **left corticobulbar** tracts) — the **largest**
    of the left pontine sub-nuclei. It **receives** inputs from the
    **left primary motor cortex** (M1) and the **left premotor cortex**
    (PMC) and **projects** to the **right intermediate cerebellar
    hemisphere** — the **motor cerebrocerebellar** functional zone.
    **Motor cerebrocerebellar relay** is the functional system subserved
    primarily by the left peduncular pontine nucleus.

*   **Left dorsal (superior) pontine nucleus** — the **dorsal** left
    sub-nucleus, adjacent to the **left pontine tegmentum**. It
    **receives** inputs from the **left prefrontal cortex** (especially
    the **left dorsolateral prefrontal cortex**) and the **left
    posterior parietal cortex** and **projects** to the **right lateral
    cerebellar hemisphere** — the **cognitive-affective
    cerebrocerebellar** functional zone. **Cognitive-affective
    cerebrocerebellar relay** is the functional system subserved
    primarily by the left dorsal pontine nucleus.

*   **Left lateral pontine nucleus** — the **far-lateral** left
    sub-nucleus. It **receives** inputs from the **left superior
    temporal cortex** (auditory association), the **left posterior
    parietal cortex**, and the **left prefrontal cortex** and
    **projects** to the **right lateral cerebellar hemisphere** — the
    **cognitive-affective cerebrocerebellar** functional zone.
    **Cognitive-affective cerebrocerebellar relay** is the functional
    system subserved primarily by the left lateral pontine nucleus.

*   **Left nucleus reticularis tegmenti pontis (NRTP)** — the **dorsal**
    left sub-nucleus that is **sometimes treated** as a separate
    structure (see the *NRTP Boundary* below). It **receives** inputs
    from the **left cerebral cortex** (including the **left frontal eye
    fields** and the **left somatosensory cortex**) and **projects** to
    the **right oculomotor vermis** and the **right fastigial nucleus**
    — it **contributes** to **saccade adaptation** and **cerebellar
    control of eye movements**. **Saccade adaptation and oculomotor
    cerebellar relay** is the functional system subserved primarily by
    the left NRTP.

**These sub-nuclei are prose subdivisions** — the tree does **not** wire
them as structural children of the **left pontine nuclei** (the **left
pontine nuclei** have **no structural children** at the tree level).
Consumers resolving **sub-nucleus-level** detail should consult the
references, not the tree.

The Left Pontine Nuclei / Right Pontine Nuclei Boundary
-------------------------------------------------------
This is the **strict-mirror** boundary:

*   **Left pontine nuclei** (this module) — the **left-side** pontine
    nuclear complex — the **left basilar pons cortico-ponto-cerebellar
    relay**.

*   **Right pontine nuclei** (``.../pontine_nuclei/right/``) — the
    **structurally identical** right-side pontine nuclear complex — the
    **right basilar pons cortico-ponto-cerebellar relay**.

**They are a STRICT MIRROR PAIR with NO warning at the sub-container
level.** The two sides are **structurally identical** — same prose
subdivisions, same functional system (cortico-ponto-cerebellar relay),
same bilateral framing. Any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere. Consumers must
**not** import a lateralization warning into the left pontine nuclei —
there is **none at the sub-container level** beyond the **crossed
cerebellar projection** documented below.

The Left Pontine Nuclei / Pontine Nuclei Container Boundary
-----------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Left pontine nuclei** (this module) — the **left-side** half of
    the pontine nuclear complex.

*   **Pontine nuclei container** (``.../pontine_nuclei/``) — the **whole
    pontine nuclear complex**, with **two structural children** (``left``
    and ``right``).

**The left pontine nuclei are a child of the pontine nuclei container.**
Consumers must **not** conflate the left half with the **whole pontine
nuclear complex** — the right side is a **separate structural sibling**.

The Left Pontine Nuclei / Corticopontine Fibers Boundary
--------------------------------------------------------
This is the **grey-matter vs. white-matter AFFERENT** boundary:

*   **Left pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that **receive** the left corticopontine fibers.

*   **Left corticopontine fibers** — the **white-matter descending
    axons** from the **left cerebral cortex** to the **left pontine
    nuclei** — the **afferent limb** of the **left cortico-ponto-
    cerebellar pathway**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**fibers** are white matter. **This distinction is clinically
load-bearing** — a **left pontine nuclei lesion** causes **right
cerebrocerebellar dysfunction**; a **left corticopontine fiber lesion**
causes **the same clinical syndrome** (the left pontine nuclei are cut
off from their left cortical input). Consumers must **not** conflate the
left pontine nuclei with the left corticopontine fibers.

The Left Pontine Nuclei / Pontocerebellar Fibers Boundary
---------------------------------------------------------
This is the **grey-matter vs. white-matter EFFERENT** boundary:

*   **Left pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that **give rise to** the left pontocerebellar fibers.

*   **Left pontocerebellar fibers** — the **white-matter crossing axons**
    from the **left pontine nuclei** to the **right cerebellar cortex**
    — the **efferent limb** of the **left cortico-ponto-cerebellar
    pathway**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**fibers** are white matter. **This distinction is clinically
load-bearing** — a **left pontine nuclei lesion** causes **right
cerebrocerebellar dysfunction**; a **left pontocerebellar fiber lesion**
causes **the same clinical syndrome** (the left pontine nuclei are cut
off from their right cerebellar output). Consumers must **not** conflate
the left pontine nuclei with the left pontocerebellar fibers.

The Left Pontine Nuclei / Right Middle Cerebellar Peduncle Boundary
-------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tract the
left pontocerebellar fibers FORM**:

*   **Left pontine nuclei** (this module) — the **grey-matter neuron
    clusters**.

*   **Right middle cerebellar peduncle** (right brachium pontis) — the
    **white-matter tract** that **carries** the left pontocerebellar
    fibers from the left pontine nuclei to the **right cerebellar
    cortex** — it is the **largest** of the **three right cerebellar
    peduncles**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**peduncle** is white matter. **This distinction is clinically
load-bearing** — a **right middle cerebellar peduncle lesion** causes
**right cerebellar ataxia** and **right dysmetria**; a **left pontine
nuclei lesion** causes **right cerebellar ataxia** as well, but the
**associated signs** differ (a left pontine nuclei lesion may accompany
**left corticospinal tract** involvement — **right hemiparesis** — or
**left cranial nerve** involvement; a pure right middle cerebellar
peduncle lesion is usually isolated right cerebellar ataxia). Consumers
must **not** conflate the left pontine nuclei with the right middle
cerebellar peduncle.

The Left Pontine Nuclei / Left Corticospinal and Left Corticobulbar Tracts Boundary
----------------------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **tracts the
nuclei are INTERSPERSED among**:

*   **Left pontine nuclei** (this module) — the **grey-matter neuron
    clusters** that are **interspersed** among the left corticospinal
    and left corticobulbar tracts.

*   **Left corticospinal tract** and **left corticobulbar tract** — the
    **white-matter descending tracts** that **run through** the **left
    basilar pons** alongside the left pontine nuclei — they **carry**
    the **left upper motor neuron** axons from the **left motor cortex**
    to the **right spinal cord** (via the **pyramidal decussation**) and
    the **cranial nerve motor nuclei**.

**They are DIFFERENT STRUCTURES.** The **nuclei** are grey matter; the
**tracts** are white matter. **This anatomical juxtaposition is a
classic source of confusion** — the left pontine nuclei are
**anatomically intermingled** with the left corticospinal and left
corticobulbar tracts (the tracts run **through** the left basilar pons,
and the left pontine nuclei are **scattered among** them). Consumers
must **not** conflate the left pontine nuclei with the left corticospinal
and left corticobulbar tracts. **This distinction is clinically
load-bearing** — a **left pontine nuclei lesion** causes **right
cerebrocerebellar dysfunction**; a **left corticospinal tract lesion**
causes **right upper motor neuron weakness** (right hemiparesis); a
**left corticobulbar tract lesion** causes **contralateral** (or
bilateral) **upper motor neuron weakness** of the **facial** and
**bulbar** muscles. The **two can coexist** in a **left pontine stroke**
— producing **combined right cerebellar ataxia and right hemiparesis** —
but they are **different structures**.

The Left Pontine Nuclei / Pontine Reticular Formation Boundary
--------------------------------------------------------------
This is the **basilar pons vs. dorsal tegmentum** boundary:

*   **Left pontine nuclei** (this module) — the **left basilar pons
    grey-matter neuron clusters** — the **left cortico-ponto-cerebellar
    relay**.

*   **Pontine reticular formation** — the **dorsal pontine tegmentum
    grey-matter region** — including the **PPRF**
    (``.../pons/paramedian_pontine_reticular_formation/``), the
    **parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``), the **caudal
    pontine reticular nucleus**, the **oral pontine reticular nucleus**,
    and other reticular nuclei.

**They are DIFFERENT STRUCTURES** — **different anatomical locations**
(left basilar pons vs. dorsal tegmentum), **different functional
systems** (cortico-ponto-cerebellar vs. horizontal saccades, orofacial
motor, autonomic regulation, respiratory rhythm). **This anatomical
distinction is a classic source of confusion** — the "pontine reticular
formation" and the "pontine nuclei" are **both** in the pons, but they
are in **different anatomical regions** (dorsal tegmentum vs. basilar
pons) and **different functional systems**. Consumers must **not**
conflate the left pontine nuclei with the pontine reticular formation or
any of its components.

The Left Pontine Nuclei / Dorsal Pontine Tegmentum Structures Boundary
----------------------------------------------------------------------
This is the **basilar pons vs. dorsal tegmentum** boundary — with the
**parabrachial area**, the **superior olivary complex**, the **cranial
nerve nuclei**, and the **locus coeruleus**:

*   **Left pontine nuclei** (this module) — the **left basilar pons
    grey-matter neuron clusters** — the **left cortico-ponto-cerebellar
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
(left basilar pons vs. dorsal tegmentum), different functional systems
(cortico-ponto-cerebellar vs. visceral-sensory/respiratory/auditory/
cranial nerve motor/sensory/noradrenergic). Consumers must **not**
conflate the left pontine nuclei with any of the **dorsal pontine
tegmentum** structures.

The Left Pontine Nuclei / Cerebellum Boundary
---------------------------------------------
This is the **pontine source vs. cerebellar target** boundary:

*   **Left pontine nuclei** (this module) — the **left basilar pons
    grey-matter neuron clusters** that **project to** the **right
    cerebellar cortex** via the **left pontocerebellar fibers** and the
    **right middle cerebellar peduncle**.

*   **Right cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/right/``) — the **right
    metencephalic cerebellar half** — it has its **own nuclei** (right
    dentate, right fastigial, right interposed) and its **own cortex**.

**They are DIFFERENT STRUCTURES** — the **left pontine nuclei** are
**pontine**; the **right cerebellum** is **cerebellar**. **The left
pontine nuclei are the major source of right cerebellar cortical
afferents** — but they are **not** the right cerebellum itself.
Consumers must **not** conflate the left pontine nuclei with the
cerebellum.

The Left Pontine Nuclei / Left Nucleus Reticularis Tegmenti Pontis Boundary
---------------------------------------------------------------------------
This is the **prose-location note** boundary:

*   **Left pontine nuclei** (this module) — the **left basilar pons
    grey-matter neuron clusters** — the **left cortico-ponto-cerebellar
    relay**.

*   **Left nucleus reticularis tegmenti pontis (NRTP)** — the **dorsal
    pontine sub-nucleus** that is **sometimes treated** as a **separate
    structure** — it is a **left cortico-ponto-cerebellar relay**
    (specifically for **saccade adaptation** and **cerebellar control of
    eye movements**).

**The left NRTP is not wired as a structural child of the left pontine
nuclei in the tree** — it is a **prose subdivision** of the left pontine
nuclei, not a structural child. **Functionally**, the left NRTP is
**part of the left pontine nuclei complex** (it is a **left dorsal
pontine sub-nucleus**); **structurally**, the tree does **not** wire it
as a child of the left pontine nuclei. Consumers must **not** assume the
left NRTP is a **structural child** of the left pontine nuclei — it is a
**prose subdivision**.

The Left Pontine Nuclei / SLEA Boundary
---------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Left pontine nuclei** (this module) — **SLEA-FREE**. They are
    **not** an extended-amygdala component, and they carry **no SLEA
    warning**.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The left pontine nuclei are NOT part of the SLEA continuum.** They are
a **basilar pons cortico-ponto-cerebellar relay**, and they carry **no
SLEA warning**. Consumers must **not** import the SLEA warning into the
left pontine nuclei.

Function in the Human Brain
---------------------------
The left pontine nuclei's functions are **the relay of left cortical
input to the right cerebellar cortex** — the **left cortico-ponto-
cerebellar pathway** — **NOT a single unified function**:

*   **Motor Cerebrocerebellar Relay (Left Peduncular Pontine Nucleus):**
    The **left peduncular (ventral) pontine nucleus** **receives** inputs
    from the **left primary motor cortex** (M1) and the **left premotor
    cortex** (PMC) and **projects** to the **right intermediate
    cerebellar hemisphere** — it **relays** the **left motor cortical
    command** to the **right cerebellar motor control circuit** (the
    **motor cerebrocerebellar** functional zone). The **right
    cerebellum** then **modulates** the **right-side motor command**
    (timing, coordination, error-based learning) and **projects back** to
    the **left motor cortex** (via the **right dentate nucleus** and the
    **thalamus**). **Motor cerebrocerebellar relay** is the functional
    system subserved primarily by the left peduncular pontine nucleus.

*   **Cognitive-Affective Cerebrocerebellar Relay (Left Dorsal and Left
    Lateral Pontine Nuclei):** The **left dorsal (superior) pontine
    nucleus** and the **left lateral pontine nucleus** **receive** inputs
    from the **left prefrontal cortex** (especially the **left
    dorsolateral prefrontal cortex**), the **left posterior parietal
    cortex**, and the **left superior temporal cortex** and **project**
    to the **right lateral cerebellar hemisphere** — they **relay** the
    **left cognitive-affective cortical command** to the **right
    cerebellar cognitive-affective control circuit** (the
    **cognitive-affective cerebrocerebellar** functional zone). The
    **right cerebellum** then **modulates** the **cognitive-affective
    processing** (working memory, attention, language, social cognition,
    emotion regulation) and **projects back** to the **left prefrontal**
    and **left parietal** cortices (via the **right dentate nucleus** and
    the **thalamus**). **Cognitive-affective cerebrocerebellar relay**
    is the functional system subserved primarily by the left dorsal and
    left lateral pontine nuclei.

*   **Spinocerebellar and Limbic-Cerebellar Relay (Left Median Pontine
    Nucleus):** The **left median (paramedian) pontine nucleus**
    **receives** inputs from the **left cingulate motor areas**, the
    **left supplementary motor area**, and the **left limbic cortex** and
    **projects** to the **right vermis** and the **right medial
    cerebellar hemisphere** — it **relays** the **left limbic and
    cingulate cortical command** to the **right cerebellar
    spinocerebellar and limbic-cerebellar circuits**. **Spinocerebellar
    and limbic-cerebellar relay** is the functional system subserved
    primarily by the left median pontine nucleus.

*   **Saccade Adaptation and Oculomotor Cerebellar Relay (Left NRTP):**
    The **left NRTP** **receives** inputs from the **left cerebral
    cortex** (including the **left frontal eye fields** and the **left
    somatosensory cortex**) and **projects** to the **right oculomotor
    vermis** and the **right fastigial nucleus** — it **contributes** to
    **saccade adaptation** and **cerebellar control of eye movements**.
    **Saccade adaptation and oculomotor cerebellar relay** is the
    functional system subserved primarily by the left NRTP.

*   **Topographic Organization:** The **left pontine nuclei** are
    **topographically organized** — the **rostrocaudal** and
    **mediolateral** organization reflects the **topography** of the
    **left cerebral cortex** (source of left corticopontine fibers) and
    the **right cerebellar cortex** (target of left pontocerebellar
    fibers). **This topographic organization** is the **neural
    substrate** of the **left-to-right cerebrocerebellar functional
    topography** — each left cortical region projects to a specific left
    pontine sub-region, and each left pontine sub-region projects to a
    specific right cerebellar region.

*   **NOT a neural processor in the classical sense.** The left pontine
    nuclei are a **relay** — they **receive** the left corticopontine
    fibers from the left cerebral cortex and **project** the left
    pontocerebellar fibers to the right cerebellar cortex. The
    **processing** of the left cortical command happens in the **left
    cerebral cortex** (the source) and the **right cerebellum** (the
    target). The left pontine nuclei are the **left brainstem relay** —
    the **left pontine node** that **relays** the **left cortical
    command** to the **right cerebellum**.

**The unifying theme:** the left pontine nuclei are the **left half of
the cortico-ponto-cerebellar relay** — the **left basilar pons
grey-matter neuron clusters** that **receive** the left corticopontine
fibers from the left cerebral cortex and **project** the left
pontocerebellar fibers to the right cerebellar cortex. They are a
**conceptual sub-container** (five prose sub-nuclei),
**topographically organized** (motor cerebrocerebellar relay;
cognitive-affective cerebrocerebellar relay; spinocerebellar and
limbic-cerebellar relay; saccade adaptation), **SLEA-free**, and **NOT
the left corticopontine or left pontocerebellar fibers** — the **fibers**
are the white-matter tracts that the nuclei **receive from** and
**project to**.

Associated Disorders
--------------------
The left pontine nuclei have **no named "left pontine nuclei syndrome"**
— their clinical associations are **sub-nucleus-specific** and
**topographic**:

*   **Left Pontine Nuclei Lesion — Right Cerebrocerebellar
    Dysfunction:** A lesion of the **left pontine nuclei** (e.g. **left
    pontine stroke**, **left pontine tumor**, **left pontine
    demyelination**) causes **right cerebrocerebellar dysfunction** —
    **right cerebellar ataxia**, **right dysmetria** (overshoot or
    undershoot of right-sided voluntary movements), **right dysarthria**
    (articulatory speech impairment — usually bilateral but may be
    asymmetric), **right intention tremor**, and — for lesions involving
    the **left dorsal/left lateral pontine nuclei** — the **cerebellar
    cognitive-affective syndrome** (CCAS: executive dysfunction,
    visuospatial deficits, language deficits, affective dysregulation).
    **The right pan-modal cerebrocerebellar pattern** is the **substrate**
    of the **left pontine nuclei** functions.

*   **Left Pontine Stroke — Combined Right Cerebellar Ataxia and Right
    Hemiparesis:** A **left pontine stroke** (e.g. **basilar artery**
    perforator territory) involving the **left pontine nuclei** and the
    **left corticospinal tract** causes **combined right cerebellar
    ataxia and right hemiparesis** — the **left pontine nuclei** are the
    **substrate** of the **right cerebellar ataxia** component, and the
    **left corticospinal tract** is the **substrate** of the **right
    hemiparesis** component. **This combined pattern is the classic "left
    pontine stroke" presentation** — and it is the **key clinical
    distinction** from a pure **right cerebellar stroke** (right
    cerebellar ataxia without right hemiparesis) or a pure **left
    corticospinal tract stroke** (right hemiparesis without right
    cerebellar ataxia).

*   **Cerebellar Cognitive-Affective Syndrome (CCAS) — Left Dorsal and
    Left Lateral Pontine Nuclei Involvement:** **CCAS** (also called
    **Schmahmann syndrome**) is a **cerebellar cognitive-affective
    syndrome** characterized by **executive dysfunction**,
    **visuospatial deficits**, **language deficits** (agrammatism,
    anomia), and **affective dysregulation** (anxiety, depression,
    impulsivity). **The left dorsal and left lateral pontine nuclei** —
    which **relay** the **left prefrontal** and **left posterior
    parietal** cortical input to the **right lateral cerebellar
    hemisphere** — are **one of the neural substrates** of the **right
    cerebellar cognitive-affective circuit**, and their dysfunction may
    **contribute** to **CCAS**.

*   **Cerebellar Motor Syndrome — Left Peduncular Pontine Nucleus
    Involvement:** **Cerebellar motor syndrome** is characterized by
    **right ataxia**, **right dysmetria**, **dysarthria**, **right
    intention tremor**, and **oculomotor abnormalities**. **The left
    peduncular pontine nucleus** — which **relays** the **left motor
    cortical input** to the **right intermediate cerebellar hemisphere**
    — is **one of the neural substrates** of the **right cerebellar
    motor circuit**, and its dysfunction may **contribute** to the
    **right cerebellar motor syndrome**.

*   **Saccade Adaptation Deficit — Left NRTP Involvement:** **Saccade
    adaptation** is the **cerebellar recalibration** of **saccade
    amplitude** in response to **visual errors**. **The left NRTP** —
    which **relays** the **left cortical** (including **left frontal eye
    fields**) and **left somatosensory** input to the **right oculomotor
    vermis** and the **right fastigial nucleus** — is **one of the
    neural substrates** of **saccade adaptation**, and its dysfunction
    may **contribute** to **saccade adaptation deficits** (e.g.
    **dysmetric saccades** that do not correct over time).

*   **Cerebellar Mutism Syndrome (Posterior Fossa Syndrome) — Left
    Pontine Nuclei Involvement:** **Cerebellar mutism syndrome** (also
    called **posterior fossa syndrome**) is a **complication** of
    **posterior fossa surgery** (especially **medulloblastoma
    resection**) — characterized by **transient mutism**, **emotional
    lability**, and **cerebellar motor deficits**. **The left pontine
    nuclei** — which **relay** the **left cerebrocerebellar** projections
    — are **one of the neural substrates** of the **cerebrocerebellar**
    circuit, and their **dysfunction** (e.g. from **surgical retraction**
    or **edema**) may **contribute** to the **mutism** and **affective**
    components of **cerebellar mutism syndrome**.

*   **No Named "Left Pontine Nuclei Syndrome":** The left pontine nuclei
    are a **conceptual sub-container** of **topographically organized
    sub-nuclei** — they have **no named clinical syndrome** of their
    own. Their clinical relevance is **right-cerebrocerebellar-specific**
    — **right cerebellar ataxia**, **right dysmetria**, **dysarthria**,
    **right intention tremor**, **cerebellar cognitive-affective
    syndrome**, and **saccade adaptation deficits**.

**What is NOT here:** The left pontine nuclei are **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **acoustic neuroma** (CN VIII
nerve), **trigeminal neuralgia** (trigeminal nerve root), **Bell's palsy**
(facial nerve), **Wallenberg syndrome** (lateral medulla), or
**internuclear ophthalmoplegia** (MLF). Their clinical relevance is
**right-cerebrocerebellar-specific**, via the **topographically
organized left pontine sub-nuclei** they subserve. **No named left
pontine nuclei syndrome exists.**

Lateralization Notes
--------------------
This is the **left** sub-container of the pontine nuclei. The left
pontine nuclei are **bilaterally symmetric** with the right pontine
nuclei and **strictly mirrored** — and they carry **NO warning at the
sub-container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right** pontine
    nuclei are **structurally identical** — same prose subdivisions
    (median, peduncular, dorsal, lateral, NRTP), same functional system
    (cortico-ponto-cerebellar relay), same bilateral framing. The
    bilateral symmetry is **strict**.

*   **Contralateral Cerebellar Projection (Structural Fact, NOT a
    Lateralization Warning):** The **left pontine nuclei** **project**
    to the **right cerebellar cortex** via the **left pontocerebellar
    fibers** and the **right middle cerebellar peduncle**. **This
    crossed projection** is a **structural fact** of the
    **cortico-ponto-cerebellar pathway** — it is **not** a functional
    lateralization. It is the **neural substrate** of the **cerebellar
    control of the ipsilateral body** (the right cerebellum controls
    the **right** side of the body, and the **left pontine nuclei
    project** to the right cerebellum — the **crossed pontocerebellar
    projection** is the **first decussation** in the cerebrocerebellar
    pathway). **This is the neural substrate** of the **right cerebellar
    ataxia** in **left pontine nuclei lesions**.

*   **Ipsilateral Corticopontine Input (Structural Fact, NOT a
    Lateralization Warning):** The **left pontine nuclei** **receive**
    corticopontine fibers from the **left cerebral cortex** (primarily
    **ipsilateral**). **This ipsilateral input** is a **structural
    fact** of the **cortico-ponto-cerebellar pathway** — it is **not**
    a functional lateralization. It is the **neural substrate** of the
    **left cortical command** that is then **crossed** to the **right
    cerebellum**.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The left pontine
    nuclei are **SLEA-free** — they are **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the left pontine nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the left pontine
    nuclei are CORTICO-PONTO-CEREBELLAR RELAY, not the fear-output):**
    The **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The left pontine nuclei
    are a **basilar pons cortico-ponto-cerebellar relay** — consumers
    must **not** conflate them with the **amygdala** or with the **fear
    circuit**.

**A consumer that assumes "left pontine nuclei = right pontine nuclei"
will be structurally correct** — the two sides are **strictly
symmetric** (the contralateral cerebellar projection and the ipsilateral
corticopontine input are structural facts, not lateralizations). The
left pontine nuclei are a **strict-mirror pair with NO warning at the
sub-container level** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left sub-container is the
    **left half**; it does **not** import the right sub-container at
    module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../pontine_nuclei/right/``, ``.../pons/tegmentum/``,
    ``.../pons/parabrachial_area/``, ``.../pons/superior_olivary_complex/``,
    ``.../pons/cranial_nerve_nuclei/``,
    ``.../pons/paramedian_pontine_reticular_formation/``,
    ``.../pons/parvocellular_reticular_nucleus/``,
    ``.../metencephalon/cerebellum/``, or any other container. The left
    pontine nuclei's relationships to the **left corticopontine
    fibers**, the **left pontocerebellar fibers**, the **right middle
    cerebellar peduncle**, the **left corticospinal** and **left
    corticobulbar tracts**, the **pontine reticular formation**, the
    **dorsal pontine tegmentum structures**, the **right cerebellum**,
    the **left NRTP**, and the **SLEA continuum** are documented as
    **prose and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf at tree level — conceptual sub-container of five prose
    subdivisions.** The **left median (paramedian) pontine nucleus**,
    **left peduncular (ventral) pontine nucleus**, **left dorsal
    (superior) pontine nucleus**, **left lateral pontine nucleus**, and
    **left nucleus reticularis tegmenti pontis (NRTP)** are documented
    as **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve sub-nucleus-level detail through the
    references.
*   **LEFT HALF — NOT the whole pontine_nuclei container.** The
    **pontine_nuclei** container has **two structural children** —
    ``left`` and ``right``. The **left** sub-container (here) is the
    **left-side** half only.
*   **STRICT MIRROR with the right pontine nuclei — NO warning at the
    sub-container level.** The **left** and **right** pontine nuclei are
    **structurally identical**. Any lateralization is documented **inside
    the left and right sub-containers** and in the **Lateralization
    Notes**.
*   **GREY-MATTER NUCLEI — NOT the left corticopontine or left
    pontocerebellar fibers.** The **left pontine nuclei** are the
    **grey-matter neuron clusters**; the **left corticopontine fibers**
    and **left pontocerebellar fibers** are the **white-matter tracts**
    that the nuclei receive from and project to. Consumers must **not**
    conflate the two.
*   **NOT the right middle cerebellar peduncle — that is the WHITE-MATTER
    TRACT the left pontocerebellar fibers form.** Consumers must **not**
    conflate the two.
*   **NOT the left corticospinal and left corticobulbar tracts — those
    are the WHITE-MATTER TRACTS the nuclei are INTERSPERSED among.**
    **This anatomical juxtaposition is a classic source of confusion** —
    consumers must **not** conflate the two.
*   **NOT the pontine reticular formation — that is the DORSAL PONTINE
    TEGMENTUM.** Consumers must **not** conflate the left pontine nuclei
    with the pontine reticular formation or any of its components.
*   **NOT the parabrachial area, the superior olivary complex, the
    cranial nerve nuclei, or the locus coeruleus — those are DORSAL
    PONTINE TEGMENTUM structures.** Consumers must **not** conflate the
    left pontine nuclei with any of them.
*   **NOT the cerebellum — that is the METENCEPHALIC SIBLING the left
    pontocerebellar fibers project to.** Consumers must **not** conflate
    the two.
*   **TOPOGRAPHICALLY ORGANIZED — MULTIPLE sub-nuclei with different
    cortical inputs and different cerebellar targets.** The **left
    sub-nuclei** are **prose subdivisions**, not structural children.
    Consumers must **not** treat the left pontine nuclei as a single
    uniform nucleus.
*   **SLEA-FREE — no extended-amygdala relationship.** The left pontine
    nuclei are **not** an extended-amygdala component, and they carry
    **no SLEA warning**.
*   **NOT the fear-output — the left pontine nuclei are CORTICO-PONTO-
    CEREBELLAR RELAY.** Consumers must **not** conflate the left pontine
    nuclei with the fear circuit.
*   **No ``AREA_PATHS`` hop.** The left pontine nuclei are a local
    sub-container under the pontine_nuclei container, not a
    cross-listed sub-container.
*   **No nested cross-listing.** The left pontine nuclei have no nested
    dual-framing module. They are a single sub-container with five
    prose subdivisions.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.pontine_nuclei import left

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.pontine_nuclei.left"
    )

**Do not** assume the left pontine nuclei are a **structural container**.
They are a **leaf at the tree level** — with **five conceptual prose
subdivisions** (left median, left peduncular, left dorsal, left lateral,
left NRTP) that are **not** structural children.

**Do not** assume the left pontine nuclei are the **whole pontine_nuclei
container**. They are the **left-side half only** — the right side is a
**separate structural sibling**.

**Do not** assume the left pontine nuclei are the **right pontine
nuclei**. The two are a **strict mirror pair with NO warning at the
sub-container level** — any lateralization is documented **here, in the
Lateralization Notes**.

**Do not** assume the left pontine nuclei are the **left corticopontine
fibers** or the **left pontocerebellar fibers**. The **left
corticopontine fibers** are the **afferent white-matter tract**; the
**left pontocerebellar fibers** are the **efferent white-matter tract**.
The **left pontine nuclei** are the **grey-matter neuron clusters** that
receive and give rise to them.

**Do not** assume the left pontine nuclei are the **right middle
cerebellar peduncle**. The **right middle cerebellar peduncle** is the
**white-matter tract** that carries the left pontocerebellar fibers; the
**left pontine nuclei** are the **grey-matter source** of those fibers.

**Do not** assume the left pontine nuclei are the **left corticospinal**
or **left corticobulbar tracts**. Those are the **white-matter
descending tracts** that run **through** the left basilar pons; the
**left pontine nuclei** are **interspersed among** them.

**Do not** assume the left pontine nuclei are the **pontine reticular
formation**, the **parabrachial area**, the **superior olivary
complex**, the **cranial nerve nuclei**, or the **locus coeruleus**.
Those are **dorsal pontine tegmentum structures**; the **left pontine
nuclei** are the **left basilar pons**.

**Do not** assume the left pontine nuclei are the **right cerebellum**.
The **right cerebellum** is the **metencephalic sibling** that the
**left pontocerebellar fibers** project to; the **left pontine nuclei**
are the **pontine source** of those fibers.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the left pontine nuclei. **The left pontine nuclei are
SLEA-FREE** — they are **not** an extended-amygdala component, and they
are **NOT part of the fear circuit**.

Iterating the left pontine nuclei's (empty) structural children
(recommended consumer pattern)::

    LEFT_PONTINE_NUCLEI_CHILDREN = ()
    # The left pontine nuclei are a leaf at the tree level. The left
    # median, left peduncular, left dorsal, left lateral pontine nuclei,
    # and left NRTP are prose subdivisions, not structural children.

Reaching the left sub-nuclei (recommended consumer pattern — through
prose subdivision resolution)::

    for sub in (
        "median_pontine_nucleus",
        "peduncular_pontine_nucleus",
        "dorsal_pontine_nucleus",
        "lateral_pontine_nucleus",
        "nucleus_reticularis_tegmenti_pontis",
    ):
        sub_path = (
            f"hindbrain.metencephalon.pons.pontine_nuclei.left.{sub}"
        )
        # resolve sub_path through the memory/recall layer
        # (NOTE: this is a PROSE SUBDIVISION resolution, not a
        # structural child resolution — the left pontine nuclei
        # sub-nuclei are not wired as structural children.)

Reaching the left corticopontine fibers (recommended consumer pattern —
the AFFERENT white-matter tract)::

    # The left corticopontine fibers are the AFFERENT white-matter tract
    # from the left cerebral cortex to the left pontine nuclei:
    #
    #   .../white_matter/.../left_corticopontine_fibers/  (or equivalent path)
    #
    # The left pontine nuclei RECEIVE the left corticopontine fibers; the
    # left corticopontine fibers are the AFFERENT limb of the left
    # cortico-ponto-cerebellar pathway.

Reaching the left pontocerebellar fibers (recommended consumer pattern —
the EFFERENT white-matter tract)::

    # The left pontocerebellar fibers are the EFFERENT white-matter tract
    # from the left pontine nuclei to the RIGHT cerebellar cortex:
    #
    #   .../white_matter/.../left_pontocerebellar_fibers/  (or equivalent path)
    #
    # The left pontine nuclei GIVE RISE TO the left pontocerebellar
    # fibers; the left pontocerebellar fibers are the EFFERENT limb of
    # the left cortico-ponto-cerebellar pathway.

Reaching the right middle cerebellar peduncle (recommended consumer
pattern — the WHITE-MATTER TRACT the left pontocerebellar fibers form)::

    # The right middle cerebellar peduncle is the WHITE-MATTER tract that
    # carries the left pontocerebellar fibers from the left pontine
    # nuclei to the RIGHT cerebellar cortex:
    #
    #   .../white_matter/.../right_middle_cerebellar_peduncle/  (or equivalent path)
    #
    # The left pontine nuclei GIVE RISE TO the left pontocerebellar
    # fibers that FORM the right middle cerebellar peduncle.

Reaching the left corticospinal and left corticobulbar tracts
(recommended consumer pattern — the WHITE-MATTER DESCENDING TRACTS the
nuclei are INTERSPERSED among)::

    # The left corticospinal and left corticobulbar tracts are the
    # WHITE-MATTER descending tracts that run THROUGH the left basilar
    # pons:
    #
    #   .../white_matter/.../left_corticospinal_tract/  (and left_corticobulbar_tract)
    #
    # The left pontine nuclei are INTERSPERSED among the left
    # corticospinal and left corticobulbar tracts — this anatomical
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
    # The left pontine nuclei are the LEFT BASILAR PONS grey-matter neuron
    # clusters — different anatomical location, different functional
    # system.

Reaching the right cerebellum (recommended consumer pattern — the
METENCEPHALIC SIBLING the left pontocerebellar fibers project to)::

    # The right cerebellum is the METENCEPHALIC SIBLING that the left
    # pontocerebellar fibers project to (via the right middle cerebellar
    # peduncle):
    #
    #   .../metencephalon/cerebellum/hemispheres/right/
    #
    # The left pontine nuclei are the LEFT PONTINE SOURCE of the right
    # cerebellar cortical afferents; the right cerebellum is the
    # CEREBELLAR TARGET.

Reaching the right pontine nuclei (recommended consumer pattern — the
strict mirror)::

    # The right pontine nuclei are the structurally identical RIGHT half
    # of the pontine nuclear complex:
    #
    #   .../pons/pontine_nuclei/right/
    #
    # The left and right pontine nuclei are a STRICT MIRROR PAIR with NO
    # warning at the sub-container level.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pn_path = (
            f"hindbrain.metencephalon.pons.pontine_nuclei.{side}"
        )
        # resolve pn_path through the memory/recall layer

Sub-nucleus-level detail (not wired — consult references)::

    # The left pontine nuclei's sub-nuclei are prose subdivisions, not
    # structural children:
    #   left median (paramedian) pontine nucleus -> left cingulate motor
    #                                         areas, left supplementary
    #                                         motor area, left limbic
    #                                         cortex -> right vermis,
    #                                         right medial cerebellar
    #                                         hemisphere;
    #                                         spinocerebellar and limbic-
    #                                         cerebellar relay
    #   left peduncular (ventral) pontine nucleus -> left primary motor
    #                                         cortex, left premotor
    #                                         cortex -> right intermediate
    #                                         cerebellar hemisphere; motor
    #                                         cerebrocerebellar relay
    #   left dorsal (superior) pontine nucleus -> left prefrontal cortex,
    #                                         left posterior parietal
    #                                         cortex -> right lateral
    #                                         cerebellar hemisphere;
    #                                         cognitive-affective
    #                                         cerebrocerebellar relay
    #   left lateral pontine nucleus -> left superior temporal cortex,
    #                              left posterior parietal cortex, left
    #                              prefrontal cortex -> right lateral
    #                              cerebellar hemisphere; cognitive-
    #                              affective cerebrocerebellar relay
    #   left nucleus reticularis tegmenti pontis (NRTP) -> left cerebral
    #                                         cortex (including left
    #                                         frontal eye fields), left
    #                                         somatosensory cortex ->
    #                                         right oculomotor vermis,
    #                                         right fastigial nucleus;
    #                                         saccade adaptation and
    #                                         oculomotor cerebellar relay
    #
    # Do not attempt to resolve these as sub-paths of the left pontine
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
*   **Right middle cerebellar peduncle (contrast — the white-matter tract
    the left pontocerebellar fibers form):** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed. (Right
    middle cerebellar peduncle — brachium pontis; the white-matter tract
    that carries the left pontocerebellar fibers.)
*   **Left corticospinal and left corticobulbar tracts (contrast — the
    white-matter descending tracts the nuclei are interspersed among):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Left corticospinal and left corticobulbar tracts
    — descending through the left basilar pons alongside the left
    pontine nuclei.)
*   **Pontine reticular formation (contrast — the dorsal pontine
    tegmentum):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Pontine reticular formation —
    dorsal pontine tegmentum; distinct from the left pontine nuclei in
    the left basilar pons.)
*   **Parabrachial area (contrast — the visceral-sensory and respiratory
    relay):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Parabrachial area —
    visceral-sensory and respiratory relay; distinct from the left
    pontine nuclei.)
*   **Superior olivary complex (contrast — the auditory brainstem
    relay):** Grothe, B., Pecka, M., McAlpine, D. (2010). "Mechanisms of
    sound localization and coding in mammals." *Physiological Reviews*
    90:983–1012. (Superior olivary complex — auditory brainstem relay;
    distinct from the left pontine nuclei.)
*   **Right cerebellum (contrast — the metencephalic sibling the left
    pontocerebellar fibers project to):** Manto, M., Gruol, D.L.,
    Schmahmann, J.D., Koibuchi, N., Rossi, F. (eds.) (2013). *Handbook
    of the Cerebellum and Cerebellar Disorders*. (Right cerebellum —
    cerebellar target of the left pontocerebellar fibers.)
*   **SLEA (contrast — the left pontine nuclei are not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the left pontine
    nuclei.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the left pontine nuclei.)
*   NeuroNames — Pontine nuclei (left); FMA — Pontine nuclei (left
    member).
"""