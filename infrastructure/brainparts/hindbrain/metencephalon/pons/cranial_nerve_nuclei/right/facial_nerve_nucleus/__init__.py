"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.facial_nerve_nucleus
====================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── right
                    └── facial_nerve_nucleus   <-- THIS MODULE

**Primary synonym:** Right facial nerve nucleus; right facial motor
nucleus; right facial nucleus; right CN VII nucleus; right seventh-nerve
motor nucleus; "the right facial-expression motor nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem branchial motor nucleus** — a **grey-matter neuron cluster**
in the **right ventrolateral pontine tegmentum**, dorsal to the **right
superior olivary complex** and ventrolateral to the **right abducens
nucleus**. It is the **sole source** of the **right facial nerve** (right
CN VII) **branchial motor** output — the **motor innervation of the right
muscles of facial expression**.
**Part of:** The **right** container of the **cranial_nerve_nuclei**
container — specifically, the **branchial motor** component. The
**right** container is the **right-side half** of the pontine
cranial-nerve nuclear collection.
**Structural parent:** ``.../cranial_nerve_nuclei/right/`` → **direct
child** of the right container.
**Structural children:** **None.** This is a **leaf** module. The
**upper-face motoneurons** (bilateral corticobulbar input) and the
**lower-face motoneurons** (contralateral corticobulbar input) are
documented as **prose**, not as structural children — they are the
**two functionally distinct populations** within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
facial nerve nucleus is a LEAF, not a container.** It has **no structural
children**. The **upper-face motoneurons** and **lower-face motoneurons**
are **prose** populations, not structural children. Consumers must
**not** treat the facial nerve nucleus as a container, and must **not**
assume the upper/lower-face populations exist as sub-modules.
**Boundary status (GREY-MATTER NUCLEUS — NOT the facial NERVE):**
**Boundary case — the facial nerve nucleus is the GREY-MATTER NUCLEUS,
NOT the facial nerve (CN VII).** The **right facial nerve** (right CN VII)
is the **white-matter axon bundle** that **leaves** the right facial
nerve nucleus and **travels** to the **right muscles of facial
expression**. The **facial nerve nucleus** (here) is the **grey-matter
neuron cluster** that **gives rise to** those axons. They are
**DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the **nerve**
is white matter. Consumers must **not** conflate the **nucleus** with the
**nerve** — the nucleus is the **central neuronal source**; the nerve is
the **peripheral conduction infrastructure**. **This distinction is
clinically load-bearing** — a **nucleus** lesion causes **ipsilateral
peripheral facial palsy** (whole right face affected, including
forehead); a **nerve** lesion also causes **ipsilateral peripheral facial
palsy**, but at a different anatomical locus along the nerve's course
(e.g. **Bell's palsy** is a nerve-level lesion, not a nucleus-level
lesion).
**Boundary status (NOT the superior salivatory nucleus — that is a
SIBLING, and it is PARASYMPATHETIC):** **Boundary case — the facial nerve
nucleus is NOT the superior salivatory nucleus.** The **right superior
salivatory nucleus**
(``.../cranial_nerve_nuclei/right/superior_salivatory_nucleus/``) is the
**parasympathetic** nucleus for the **right lacrimal** and **right
salivary** glands — also **CN VII**, but a **different functional
component** (autonomic vs. branchial motor). The **right facial nerve
nucleus** (here) is the **branchial motor** nucleus for the **right
muscles of facial expression**. They are **DIFFERENT STRUCTURES** —
different functional systems (branchial motor vs. parasympathetic),
different peripheral targets (facial muscles vs. glands). They are
**both CN VII** — this shared cranial nerve is a **classic source of
confusion** — consumers must **not** conflate the **facial nerve
nucleus** with the **superior salivatory nucleus**.
**Boundary status (NOT the abducens nucleus — that is a SIBLING, and the
facial FIBERS loop around it):** **Boundary case — the facial nerve
nucleus is NOT the abducens nucleus; the abducens nucleus is a SIBLING
under the right container, and the facial nerve FIBERS loop around it.**
The **right abducens nucleus**
(``.../cranial_nerve_nuclei/right/abducens_nucleus/``) is the **somatic
motor** nucleus for the **right lateral rectus**. The **right facial
nerve nucleus** (here) is the **branchial motor** nucleus for the **right
muscles of facial expression**. They are **DIFFERENT STRUCTURES** —
different functional systems, different peripheral targets. **The facial
nerve fibers** (the **internal genu** of right CN VII) **loop around** the
right abducens nucleus in the pontine tegmentum, producing the **facial
colliculus** on the floor of the fourth ventricle. This anatomical
proximity is a **classic source of confusion** — consumers must **not**
conflate the **facial nerve nucleus** with the **abducens nucleus**, and
must **not** assume the facial nerve fibers are part of the abducens
nucleus.
**Boundary status (NOT the motor trigeminal nucleus — that is a SIBLING,
and it is MASTICATION, CN V):** **Boundary case — the facial nerve
nucleus is NOT the motor trigeminal nucleus.** The **right motor
trigeminal nucleus**
(``.../cranial_nerve_nuclei/right/motor_trigeminal_nucleus/``) is the
**branchial motor** nucleus for the **right muscles of mastication**
(CN V). The **right facial nerve nucleus** (here) is the **branchial
motor** nucleus for the **right muscles of facial expression** (CN VII).
They are **DIFFERENT STRUCTURES** — different cranial nerves (CN V vs.
CN VII), different branchial-arch origins (arch 1 vs. arch 2), different
peripheral targets (mastication vs. facial expression). Consumers must
**not** conflate the **facial nerve nucleus** with the **motor
trigeminal nucleus**.
**Boundary status (NOT the hypoglossal nucleus — that is MEDULLARY, and
it is TONGUE, CN XII):** **Boundary case — the facial nerve nucleus is
NOT the hypoglossal nucleus.** The **right hypoglossal nucleus**
(``.../medulla_oblongata/cranial_nerve_nuclei/right/hypoglossal_nucleus/``)
is the **somatic motor** nucleus for the **right tongue muscles** (right
CN XII). The **right facial nerve nucleus** (here) is the **branchial
motor** nucleus for the **right muscles of facial expression** (right
CN VII). They are **DIFFERENT STRUCTURES** — different brainstem levels
(pons vs. medulla), different cranial nerves (VII vs. XII), different
peripheral targets (facial expression vs. tongue movement). Consumers
must **not** conflate the **facial nerve nucleus** with the
**hypoglossal nucleus**.
**Boundary status (NOT the nucleus ambiguus — that is MEDULLARY, and it
is PHARYNX/LARYNX, CN IX/X):** **Boundary case — the facial nerve nucleus
is NOT the nucleus ambiguus.** The **right nucleus ambiguus**
(``.../medulla_oblongata/cranial_nerve_nuclei/right/nucleus_ambiguus/``)
is the **branchial motor** nucleus for the **right pharynx** and **right
larynx** (right CN IX and right CN X). The **right facial nerve nucleus**
(here) is the **branchial motor** nucleus for the **right muscles of
facial expression** (right CN VII). They are **DIFFERENT STRUCTURES** —
different brainstem levels (pons vs. medulla), different cranial nerves
(VII vs. IX/X), different peripheral targets (facial expression vs.
swallowing and phonation). Consumers must **not** conflate the **facial
nerve nucleus** with the **nucleus ambiguus**.
**Boundary status (NOT the extraocular motor nuclei — those are CN III,
IV, VI):** **Boundary case — the facial nerve nucleus is NOT the
oculomotor, trochlear, or abducens nucleus.** The **oculomotor nucleus**
(midbrain — CN III), the **trochlear nucleus** (midbrain — CN IV), and
the **abducens nucleus** (pons — CN VI) are the **somatic motor**
extraocular nuclei. The **facial nerve nucleus** (here) is the
**branchial motor** nucleus for the **facial muscles** — not an
extraocular nucleus. Consumers must **not** conflate the **facial nerve
nucleus** with any of the **extraocular motor nuclei**.
**Boundary status (NOT the facial muscles — those are PERIPHERAL
TARGETS):** **Boundary case — the facial nerve nucleus is NOT the muscles
of facial expression.** The **right muscles of facial expression** — the
**frontalis**, **orbicularis oculi**, **orbicularis oris**,
**buccinator**, **platysma**, **stapedius**, **stylohyoid**, and the
**posterior belly of the digastric** — are the **peripheral effector
muscles** that **express the face** and are the **targets** of the right
facial motor axons. The **facial nerve nucleus** (here) is the **central
grey-matter neuron cluster** that **innervates** them. They are
**DIFFERENT STRUCTURES** — the **nucleus** is central nervous system; the
**muscles** are peripheral effectors. Consumers must **not** conflate
the **nucleus** with the **muscles**.
**Boundary status (NOT the corticobulbar tract — that is the WHITE-MATTER
UPPER-MOTOR INPUT):** **Boundary case — the facial nerve nucleus is NOT
the corticobulbar tract.** The **right (and left) corticobulbar tract**
is the **white-matter upper-motor-neuron pathway** that **projects** from
the **motor cortex** to the **facial nerve nucleus** — it carries the
**upper-motor-neuron input** that **drives** the facial motor neurons.
The **facial nerve nucleus** (here) is the **grey-matter lower-motor-
neuron cluster** that **gives rise to** the **facial nerve**. They are
**DIFFERENT STRUCTURES** — the **corticobulbar tract** is white matter;
the **nucleus** is grey matter. **This distinction is clinically
load-bearing** — a **corticobulbar** (upper-motor-neuron) lesion causes
**central facial palsy** with **forehead sparing**; a **facial nerve
nucleus** (lower-motor-neuron) lesion causes **peripheral facial palsy**
with the **whole face affected** (no forehead sparing). Consumers must
**not** conflate the **facial nerve nucleus** with the **corticobulbar
tract**.
**Boundary status (NOT the facial colliculus — that is the SURFACE
LANDMARK):** **Boundary case — the facial nerve nucleus is NOT the facial
colliculus.** The **facial colliculus** is the **bump on the floor of the
fourth ventricle** produced by the **facial nerve fibers** (the internal
genu of CN VII) **looping around the abducens nucleus** — it is a
**surface landmark**, not the nucleus itself. The **facial nerve
nucleus** (here) is a **deeper grey-matter structure** in the
**ventrolateral pontine tegmentum**, **not** directly beneath the facial
colliculus. The facial colliculus marks the **facial nerve fibers**, not
the **facial nerve nucleus** — they are **anatomically separate**.
Consumers must **not** conflate the **facial nerve nucleus** with the
**facial colliculus**.
**Boundary status (NOT the geniculate ganglion — that is PERIPHERAL):**
**Boundary case — the facial nerve nucleus is NOT the geniculate
ganglion.** The **right geniculate ganglion** is a **peripheral sensory
ganglion** on the right facial nerve that contains the **primary sensory
neuron cell bodies** for the **right CN VII sensory components** (taste
from the anterior two-thirds of the tongue, and sensation from the
external auditory canal). The **facial nerve nucleus** (here) is the
**central grey-matter branchial motor nucleus**. They are **DIFFERENT
STRUCTURES** — the **ganglion** is peripheral and sensory; the **nucleus**
is central and motor. Consumers must **not** conflate the **central
nucleus** with the **peripheral ganglion**.
**Boundary status (NOT the nervus intermedius — that is the CN VII
SENSORY/PARASYMPATHETIC COMPONENT):** **Boundary case — the facial nerve
nucleus is NOT the nervus intermedius.** The **nervus intermedius** (the
**nerve of Wrisberg**) is the **sensory and parasympathetic root** of the
facial nerve — it carries the **taste fibers** (from the anterior
two-thirds of the tongue, via the chorda tympani), the **somatic sensory
fibers** (from the external auditory canal), and the **parasympathetic
preganglionic fibers** (from the superior salivatory nucleus). The
**facial nerve nucleus** (here) is the **branchial motor nucleus** —
the **motor root** of CN VII. The nervus intermedius and the facial
nerve nucleus are **DIFFERENT STRUCTURES** — the **nervus intermedius**
is the **sensory/parasympathetic root**; the **facial nerve nucleus** is
the **motor root**. Consumers must **not** conflate the **branchial
motor nucleus** with the **nervus intermedius**.
**Boundary status (NOT a single uniform neuron population — TWO
functionally distinct UPPER-FACE vs. LOWER-FACE populations):**
**Boundary case — the facial nerve nucleus is NOT a single uniform neuron
population; it contains TWO functionally distinct populations defined by
their CORTICOBULBAR INPUT.** The **upper-face motoneurons** (frontalis,
orbicularis oculi) receive **bilateral corticobulbar input** from **both
the right and left motor cortices** — so a **unilateral** upper-motor-
neuron lesion **spares the upper face** (the intact contralateral
corticobulbar projection is sufficient). The **lower-face motoneurons**
(orbicularis oris, buccinator, platysma, etc.) receive **contralateral
corticobulbar input only** from the **left motor cortex** — so a
**unilateral** upper-motor-neuron lesion **affects the lower face**
contralaterally (the intact ipsilateral corticobulbar projection is
insufficient). This **upper/lower-face distinction** is **prose**, not
structural children. Consumers must **not** treat the facial nerve
nucleus as a single uniform population — it is a **two-population
nucleus** with **different cortical innervation patterns**.
**Boundary status (NOT the whole cranial_nerve_nuclei container — a leaf
child of the right container):** **Boundary case — the facial nerve
nucleus is a LEAF child of the right container, not the container itself,
and not the whole cranial_nerve_nuclei container.** The **right** container
contains the **facial nerve nucleus** and **five other children**. The
**cranial_nerve_nuclei** container contains **two structural children**
(``left`` and ``right``). Consumers must **not** conflate the facial
nerve nucleus with the **right** container or the **cranial_nerve_nuclei**
container.
**Boundary status (NOT the left facial nerve nucleus — strict mirror,
no warning):** **Boundary case — the right facial nerve nucleus is NOT the
left facial nerve nucleus; the two are a STRICT MIRROR PAIR with NO
warning at the nucleus level.** The **left facial nerve nucleus**
(``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) is the
**structurally identical** left-side counterpart — same branchial motor
function, same upper/lower-face populations, same leaf status, same
bilateral framing. The two sides are **strictly mirrored** — any
lateralization is documented **here, in the Lateralization Notes**, not
imported from elsewhere. Consumers must **not** import a lateralization
warning into the right facial nerve nucleus — there is **none at the
nucleus level** beyond the **contralateral corticobulbar input to the
lower-face** documented below.
**Boundary status (SLEA-FREE — the facial nerve nucleus is NOT an
extended-amygdala component):** **Boundary case — the facial nerve
nucleus is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **facial nerve nucleus** is a **branchial motor
brainstem nucleus** — it is **NOT** an extended-amygdala component, and
it carries **NO SLEA warning**. Consumers must **not** import the SLEA
warning into the facial nerve nucleus — it is **SLEA-free**.

Overview
--------
The facial nerve nucleus is the **branchial motor** nucleus for the
**right muscles of facial expression** — the **sole source** of the
**right facial nerve** (right CN VII) **branchial motor** output. It is a
**leaf** module under the right container of the cranial_nerve_nuclei
container, and it contains **two functionally distinct populations**
defined by their **corticobulbar input**: the **upper-face motoneurons**
(bilateral corticobulbar input) and the **lower-face motoneurons**
(contralateral corticobulbar input).

**The facial nerve nucleus is the GREY-MATTER NUCLEUS, NOT the facial
NERVE.** The **facial nerve** (right CN VII) is the **white-matter axon
bundle** that **travels** to the right muscles of facial expression. The
**facial nerve nucleus** (here) is the **grey-matter neuron cluster**
that **gives rise to** those axons. They are **DIFFERENT STRUCTURES** —
the **nucleus** is grey matter; the **nerve** is white matter.

**The facial nerve nucleus is NOT the superior salivatory nucleus.** The
**superior salivatory nucleus** is a **sibling** under the right
container — the **parasympathetic** nucleus for the **right lacrimal**
and **right salivary** glands, **also CN VII**. They are **both CN VII**
— this shared cranial nerve is a **classic source of confusion** —
consumers must **not** conflate the **facial nerve nucleus** with the
**superior salivatory nucleus**.

**The facial nerve nucleus is NOT the abducens nucleus.** The **abducens
nucleus** is a **sibling** under the right container; the **facial nerve
fibers** (the internal genu of right CN VII) **loop around** the abducens
nucleus, producing the **facial colliculus** on the floor of the fourth
ventricle. The facial colliculus marks the **facial nerve fibers**, not
the **facial nerve nucleus** — they are **anatomically separate**. This
anatomical proximity is a **classic source of confusion** — consumers
must **not** conflate the **facial nerve nucleus** with the **abducens
nucleus**.

**The facial nerve nucleus is a TWO-POPULATION nucleus defined by
CORTICOBULBAR INPUT.** The **upper-face motoneurons** receive **bilateral
corticobulbar input**; the **lower-face motoneurons** receive
**contralateral corticobulbar input**. **This distinction is clinically
load-bearing** — a **corticobulbar (upper-motor-neuron)** lesion causes
**central facial palsy with forehead sparing**; a **facial nerve nucleus
(lower-motor-neuron)** lesion causes **peripheral facial palsy with the
whole face affected**. The two populations are **prose**, not structural
children — the facial nerve nucleus is a **leaf** with **no structural
children**.

**The facial nerve nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Neuron Population Composition (prose, not structural children)
---------------------------------------------------------------
The facial nerve nucleus is a **two-population nucleus** — documented as
**prose**, not as structural children:

*   **Upper-face motoneurons** — the **branchial motor** neurons that
    innervate the **upper-face muscles** — the **right frontalis** and
    the **right orbicularis oculi**. They receive **bilateral
    corticobulbar input** from **both the right and left motor
    cortices**. **This bilateral input is the basis of "forehead
    sparing"** in **upper-motor-neuron lesions** — a **unilateral**
    central lesion **spares the upper face** because the intact
    contralateral corticobulbar projection is sufficient. **A
    lower-motor-neuron lesion** (nucleus or nerve) **affects the upper
    face** because the **final common pathway** is lost.

*   **Lower-face motoneurons** — the **branchial motor** neurons that
    innervate the **lower-face muscles** — the **right orbicularis
    oris**, **right buccinator**, **right platysma**, **right
    stapedius**, **right stylohyoid**, and the **right posterior belly
    of the digastric**. They receive **contralateral corticobulbar
    input only** from the **left motor cortex**. **This contralateral
    input is the basis of "lower-face involvement"** in **both central
    and peripheral lesions** — a **unilateral** central lesion **affects
    the lower face** (the intact ipsilateral corticobulbar projection is
    insufficient); a **lower-motor-neuron lesion** (nucleus or nerve)
    **also affects the lower face** (the final common pathway is lost).

**These populations are prose, not structural children.** The tree wires
the **facial nerve nucleus** as a **single leaf** under the right
container — the **upper-face motoneurons** and **lower-face motoneurons**
are **prose**, not structural children. Consumers that need
**neuron-population-level** resolution should consult the references, not
the tree.

The Facial Nerve Nucleus / Facial Nerve Boundary
------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Facial nerve nucleus** (this module) — the **grey-matter neuron
    cluster** in the right pontine tegmentum.

*   **Facial nerve** (right CN VII) — the **white-matter axon bundle**
    that travels to the right muscles of facial expression.

**They are DIFFERENT STRUCTURES.** The **nucleus** is the **central
neuronal source**; the **nerve** is the **peripheral conduction
infrastructure**. Consumers must **not** conflate the two — the **facial
nerve nucleus** is the **nucleus**; the **facial nerve** is the
**nerve**.

The Facial Nerve Nucleus / Superior Salivatory Nucleus Boundary
---------------------------------------------------------------
This is the **CN VII sibling** boundary — **branchial motor vs.
parasympathetic**:

*   **Facial nerve nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of facial expression**.

*   **Superior salivatory nucleus**
    (``.../cranial_nerve_nuclei/right/superior_salivatory_nucleus/``) —
    the **parasympathetic** nucleus for the **right lacrimal** and
    **right salivary** glands, **also CN VII**.

**They are DIFFERENT STRUCTURES** — different functional systems
(branchial motor vs. parasympathetic), different peripheral targets
(facial muscles vs. glands). They are **both CN VII** — this shared
cranial nerve is a **classic source of confusion** — consumers must
**not** conflate the **facial nerve nucleus** with the **superior
salivatory nucleus**.

The Facial Nerve Nucleus / Abducens Nucleus Boundary
----------------------------------------------------
This is the **sibling** boundary — with a **fiber-proximity** twist:

*   **Facial nerve nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of facial expression**.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/right/abducens_nucleus/``) — the
    **somatic motor** nucleus for the **right lateral rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems,
different peripheral targets. **The facial nerve fibers** (the internal
genu of right CN VII) **loop around** the right abducens nucleus in the
pontine tegmentum, producing the **facial colliculus** on the floor of
the fourth ventricle. The facial colliculus marks the **facial nerve
fibers**, not the **facial nerve nucleus** — they are **anatomically
separate**. Consumers must **not** conflate the **facial nerve nucleus**
with the **abducens nucleus**.

The Facial Nerve Nucleus / Motor Trigeminal Nucleus Boundary
------------------------------------------------------------
This is the **branchial motor sibling** boundary — **CN VII vs. CN V**:

*   **Facial nerve nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of facial expression** (right CN VII,
    **2nd branchial arch**).

*   **Motor trigeminal nucleus**
    (``.../cranial_nerve_nuclei/right/motor_trigeminal_nucleus/``) — the
    **branchial motor** nucleus for the **right muscles of mastication**
    (right CN V, **1st branchial arch**).

**They are DIFFERENT STRUCTURES** — different cranial nerves (CN VII vs.
CN V), different branchial-arch origins (arch 2 vs. arch 1), different
peripheral targets (facial expression vs. mastication). Consumers must
**not** conflate the **facial nerve nucleus** with the **motor
trigeminal nucleus**.

The Facial Nerve Nucleus / Hypoglossal Nucleus Boundary
-------------------------------------------------------
This is the **brainstem-level** boundary — **pons vs. medulla**, and
**facial expression vs. tongue**:

*   **Facial nerve nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of facial expression** (right
    CN VII).

*   **Hypoglossal nucleus**
    (``.../medulla_oblongata/cranial_nerve_nuclei/right/hypoglossal_nucleus/``)
    — the **somatic motor** nucleus for the **right tongue muscles**
    (right CN XII).

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different cranial nerves (VII vs. XII), different peripheral
targets (facial expression vs. tongue movement). Consumers must **not**
conflate the **facial nerve nucleus** with the **hypoglossal nucleus**.

The Facial Nerve Nucleus / Nucleus Ambiguus Boundary
----------------------------------------------------
This is the **branchial motor sibling** boundary — **CN VII vs. CN
IX/X**, and **pons vs. medulla**:

*   **Facial nerve nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of facial expression** (right
    CN VII).

*   **Nucleus ambiguus**
    (``.../medulla_oblongata/cranial_nerve_nuclei/right/nucleus_ambiguus/``)
    — the **branchial motor** nucleus for the **right pharynx** and
    **right larynx** (right CN IX and right CN X).

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different cranial nerves (VII vs. IX/X), different peripheral
targets (facial expression vs. swallowing and phonation). Consumers must
**not** conflate the **facial nerve nucleus** with the **nucleus
ambiguus**.

The Facial Nerve Nucleus / Extraocular Motor Nuclei Boundary
------------------------------------------------------------
This is the **somatic motor extraocular** boundary:

*   **Facial nerve nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of facial expression**.

*   **Oculomotor nucleus** (midbrain — CN III), **trochlear nucleus**
    (midbrain — CN IV), **abducens nucleus** (pons — CN VI) — the
    **somatic motor** extraocular nuclei.

**They are DIFFERENT STRUCTURES** — the facial nerve nucleus is
**branchial motor**; the extraocular nuclei are **somatic motor**. They
subserve **different functional systems** and **different peripheral
targets**. Consumers must **not** conflate the **facial nerve nucleus**
with any of the **extraocular motor nuclei**.

The Facial Nerve Nucleus / Facial Muscles Boundary
--------------------------------------------------
This is the **central vs. peripheral** boundary:

*   **Facial nerve nucleus** (this module) — the **central grey-matter
    neuron cluster**.

*   **Facial muscles** — the **peripheral effector muscles** — the
    **frontalis**, **orbicularis oculi**, **orbicularis oris**,
    **buccinator**, **platysma**, **stapedius**, **stylohyoid**, and the
    **posterior belly of the digastric** — the **targets** of the right
    facial motor axons.

**They are DIFFERENT STRUCTURES** — the **nucleus** is central nervous
system; the **muscles** are peripheral effectors. Consumers must **not**
conflate the **nucleus** with the **muscles**.

The Facial Nerve Nucleus / Corticobulbar Tract Boundary
-------------------------------------------------------
This is the **grey-matter vs. white-matter UPPER-MOTOR-NEURON** boundary:

*   **Facial nerve nucleus** (this module) — the **grey-matter
    lower-motor-neuron cluster** that **gives rise to** the **facial
    nerve**.

*   **Corticobulbar tract** — the **white-matter upper-motor-neuron
    pathway** that **projects** from the **motor cortex** to the
    **facial nerve nucleus**.

**They are DIFFERENT STRUCTURES** — the **corticobulbar tract** is white
matter; the **nucleus** is grey matter. **This distinction is clinically
load-bearing** — a **corticobulbar** (upper-motor-neuron) lesion causes
**central facial palsy** with **forehead sparing**; a **facial nerve
nucleus** (lower-motor-neuron) lesion causes **peripheral facial palsy**
with the **whole face affected** (no forehead sparing). Consumers must
**not** conflate the **facial nerve nucleus** with the **corticobulbar
tract**.

The Facial Nerve Nucleus / Facial Colliculus Boundary
-----------------------------------------------------
This is the **surface-landmark** boundary:

*   **Facial nerve nucleus** (this module) — a **deeper grey-matter
    structure** in the **ventrolateral pontine tegmentum**.

*   **Facial colliculus** — the **bump on the floor of the fourth
    ventricle** produced by the **facial nerve fibers** (the internal
    genu of CN VII) **looping around** the abducens nucleus.

**The facial colliculus marks the facial nerve FIBERS, not the facial
nerve NUCLEUS** — they are **anatomically separate**. The nucleus is in
the ventrolateral tegmentum; the fibers loop around the abducens nucleus
more dorsomedially. Consumers must **not** conflate the **facial nerve
nucleus** with the **facial colliculus**.

The Facial Nerve Nucleus / Geniculate Ganglion Boundary
-------------------------------------------------------
This is the **central vs. peripheral** boundary — **motor vs. sensory**:

*   **Facial nerve nucleus** (this module) — the **central grey-matter
    branchial motor nucleus**.

*   **Geniculate ganglion** — the **peripheral sensory ganglion** on the
    right facial nerve that contains the **primary sensory neuron cell
    bodies** for the **right CN VII sensory components** (taste from the
    anterior two-thirds of the tongue, and sensation from the external
    auditory canal).

**They are DIFFERENT STRUCTURES** — the **ganglion** is peripheral and
sensory; the **nucleus** is central and motor. Consumers must **not**
conflate the **central nucleus** with the **peripheral ganglion**.

The Facial Nerve Nucleus / Nervus Intermedius Boundary
------------------------------------------------------
This is the **motor vs. sensory/parasympathetic** boundary:

*   **Facial nerve nucleus** (this module) — the **branchial motor
    nucleus** — the **motor root** of CN VII.

*   **Nervus intermedius** (the **nerve of Wrisberg**) — the **sensory
    and parasympathetic root** of the facial nerve — it carries the
    **taste fibers** (from the anterior two-thirds of the tongue, via
    the chorda tympani), the **somatic sensory fibers** (from the
    external auditory canal), and the **parasympathetic preganglionic
    fibers** (from the superior salivatory nucleus).

**They are DIFFERENT STRUCTURES** — the **nervus intermedius** is the
**sensory/parasympathetic root**; the **facial nerve nucleus** is the
**motor root**. Consumers must **not** conflate the **branchial motor
nucleus** with the **nervus intermedius**.

The Facial Nerve Nucleus / Left Facial Nerve Nucleus Boundary
-------------------------------------------------------------
This is the **strict-mirror** boundary:

*   **Right facial nerve nucleus** (this module) — the **right-side**
    branchial motor nucleus for the **right muscles of facial
    expression**.

*   **Left facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) — the
    **structurally identical** left-side branchial motor nucleus for
    the **left muscles of facial expression**.

**They are a STRICT MIRROR PAIR with NO warning at the nucleus level.**
The two sides are **structurally identical** — same branchial motor
function, same upper/lower-face populations, same leaf status, same
bilateral framing. **The contralateral corticobulbar input to the
lower-face is a connectivity fact, not a lateralization warning** — the
right facial nerve nucleus lower-face motoneurons receive input from the
**left** motor cortex, and the left facial nerve nucleus lower-face
motoneurons receive input from the **right** motor cortex. This is
**structural**, not a functional lateralization. Consumers must **not**
import a lateralization warning into the right facial nerve nucleus —
there is **none at the nucleus level**.

The Facial Nerve Nucleus / Cranial Nerve Nuclei Container Boundary
------------------------------------------------------------------
This is the **leaf vs. container** boundary:

*   **Facial nerve nucleus** (this module) — a **leaf** child of the
    **right** container.

*   **Right container** (``.../cranial_nerve_nuclei/right/``) — the
    **right-side half** of the pontine cranial-nerve nuclear collection,
    with **six structural children** (including the facial nerve
    nucleus).

*   **Cranial_nerve_nuclei container** (``.../cranial_nerve_nuclei/``) —
    the **whole pontine collection**, with **two structural children**
    (``left`` and ``right``).

**The facial nerve nucleus is a leaf child of the right container.**
Consumers must **not** conflate the facial nerve nucleus with the
**right** container or the **cranial_nerve_nuclei** container.

The Facial Nerve Nucleus / SLEA Boundary
----------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Facial nerve nucleus** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The facial nerve nucleus is NOT part of the SLEA continuum.** It is a
**branchial motor brainstem nucleus**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the facial nerve
nucleus.

Function in the Human Brain
---------------------------
The facial nerve nucleus's functions are **the branchial motor control of
the right muscles of facial expression** — **NOT a single unified
function**:

*   **Upper-Face Motor (Frontalis, Orbicularis Oculi):** The **upper-face
    motoneurons** innervate the **right frontalis** (forehead wrinkling)
    and the **right orbicularis oculi** (eye closure). They receive
    **bilateral corticobulbar input**, so a **unilateral** upper-motor-
    neuron lesion **spares the upper face**.

*   **Lower-Face Motor (Orbicularis Oris, Buccinator, Platysma):** The
    **lower-face motoneurons** innervate the **right orbicularis oris**
    (lip closure, pucker), the **right buccinator** (cheek
    tension, keeping food between the teeth), and the **right platysma**
    (neck skin tension). They receive **contralateral corticobulbar
    input only**, so a **unilateral** upper-motor-neuron lesion
    **affects the lower face** contralaterally.

*   **Stapedius Motor (Stapedius Muscle):** The **stapedius motoneurons**
    innervate the **right stapedius** muscle — the **smallest skeletal
    muscle in the human body**, which **dampens the ossicular chain** in
    response to **loud sounds** (the **acoustic reflex**). Loss of
    stapedius innervation causes **hyperacusis** (sound
    hypersensitivity).

*   **Stylohyoid and Posterior Digastric Motor:** The **stylohyoid and
    posterior belly of the digastric motoneurons** innervate the **right
    stylohyoid** (elevates the hyoid) and the **right posterior belly of
    the digastric** (depresses the mandible). These are **accessory
    facial motor functions** — **not** the principal muscles of facial
    expression, but they are **innervated by the same nucleus**.

*   **NOT a neural processor in the classical sense.** The facial nerve
    nucleus is a **motor output nucleus** — it **executes** the
    **corticobulbar commands** generated upstream (in the **motor
    cortex**). The **processing** of facial expression happens in the
    **motor cortex**, the **basal ganglia**, and the **limbic system**
    (which modulate emotional facial expression via separate pathways).
    The facial nerve nucleus is the **final common pathway** for
    **voluntary facial movement**.

**The unifying theme:** the facial nerve nucleus is the **branchial
motor output nucleus** for the **right muscles of facial expression** —
the **final common pathway** for **voluntary facial movement**. It is
**two-population** (upper-face bilateral corticobulbar; lower-face
contralateral corticobulbar), **SLEA-free**, and **NOT the facial
nerve** — the **nerve** is the **white-matter axon bundle**; the
**nucleus** is the **grey-matter neuron cluster** that **gives rise to**
it.

Associated Disorders
--------------------
The facial nerve nucleus has **no named "facial nerve nucleus syndrome"**
— its clinical associations are **nucleus-specific**, and they are
**distinguishable from upper-motor-neuron (corticobulbar), nerve-level,
and other brainstem-level lesions**:

*   **Facial Nerve Nucleus Lesion — Ipsilateral Peripheral Facial
    Palsy:** A lesion of the **right facial nerve nucleus** causes
    **right peripheral facial palsy** — **inability to close the right
    eye** (orbicularis oculi weakness), **loss of right forehead
    wrinkling** (frontalis weakness), **right facial droop** (lower-face
    weakness), **right nasolabial fold flattening**, **drooling** from
    the right corner of the mouth, and **loss of the right acoustic
    reflex** (stapedius weakness → hyperacusis). **The whole right face
    is affected — no forehead sparing** — because the **lower-motor
    neuron** (final common pathway) is lost.

*   **Corticobulbar (Upper-Motor-Neuron) Lesion — Contralateral Central
    Facial Palsy with Forehead Sparing:** A lesion of the **left motor
    cortex** or **left corticobulbar tract** causes **right central
    facial palsy** — **right lower-face weakness** (drooping of the
    right corner of the mouth, flattening of the right nasolabial fold)
    **with SPARING of the right forehead** (frontalis preserved; the
    right orbicularis oculi is also partially preserved). **This is the
    key clinical distinction from a nucleus/nerve lesion** — the
    **upper face is spared** because the **bilateral corticobulbar input
    to the upper-face motoneurons** is sufficient (the intact
    right-hemisphere corticobulbar projection to the right upper-face
    motoneurons preserves forehead movement).

*   **Facial Nerve Lesion — Ipsilateral Peripheral Facial Palsy (Bell's
    Palsy, Ramsay Hunt Syndrome):** A lesion of the **right facial
    nerve** (right CN VII) **along its peripheral course** also causes
    **right peripheral facial palsy** — **clinically identical to a
    nucleus lesion** in its effect on the facial muscles, but at a
    **different anatomical locus**. **Bell's palsy** is an **idiopathic
    peripheral facial nerve palsy** (usually at the **stylomastoid
    foramen** or **geniculate ganglion** level). **Ramsay Hunt
    syndrome** is a **varicella-zoster virus** infection of the
    **geniculate ganglion**, causing **peripheral facial palsy** with
    **vesicles in the external auditory canal** and **taste loss** on
    the anterior two-thirds of the tongue (because the **nervus
    intermedius** is also affected). **The distinction between a
    nucleus and nerve lesion** in the clinical exam is often made by
    **associated brainstem signs** (e.g. **abducens palsy** suggests
    a **pontine nucleus** lesion; **isolated facial palsy** suggests
    a **nerve** lesion).

*   **Facial Colliculus Syndrome (Abducens Nucleus + Facial Nerve
    Fibers) — Foville Syndrome:** A lesion of the **right pontine
    tegmentum** involving the **right abducens nucleus** (or **right
    PPRF**), the **right facial nerve fibers** (which loop around the
    abducens nucleus), and the **right corticospinal tract** causes
    **Foville syndrome** — **rightward horizontal gaze palsy** +
    **right facial palsy** + **left hemiparesis**. **Note**: in
    Foville syndrome, the **facial palsy is due to the facial nerve
    FIBERS being interrupted**, not the **facial nerve NUCLEUS** — but
    the **nucleus may also be involved** if the lesion is large enough.
    **The facial nerve nucleus is the substrate of the facial palsy
    component** when the lesion extends to the ventrolateral tegmentum.

*   **Millard-Gubler Syndrome — Pontine Base Lesion:** A lesion of the
    **right pontine base** involving the **right abducens nerve fibers**
    and the **right facial nerve fibers** (and the **right
    corticospinal tract**) causes **Millard-Gubler syndrome** — **right
    lateral rectus palsy** + **right facial palsy** + **left
    hemiparesis**. **Note**: this is a **nerve-fiber** lesion, not a
    **nucleus** lesion — the **facial nerve nucleus itself may be
    spared**.

*   **Möbius Syndrome — Congenital Facial (and Abducens) Palsy:**
    **Möbius syndrome** is a **congenital** disorder characterized by
    **facial (CN VII)** and **abducens (CN VI)** palsy — the **facial
    nerve nucleus** (and the abducens nucleus) are **hypoplastic or
    absent**.

*   **No Named "Facial Nerve Nucleus Syndrome":** The facial nerve
    nucleus is a **single branchial motor nucleus** — it has **no named
    clinical syndrome of its own**. Its clinical relevance is
    **nucleus-specific**, via the **right muscles of facial expression**
    it subserves. **The most important clinical distinction is
    upper-motor-neuron (corticobulbar) vs. lower-motor-neuron (nucleus
    or nerve)** — the **forehead-sparing** pattern of a central lesion
    vs. the **whole-face** pattern of a peripheral lesion.

**What is NOT here:** The facial nerve nucleus is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), or **Bell's palsy alone**
(facial nerve, not nucleus). Its clinical relevance is
**facial-motor-specific**, via the **right muscles of facial expression**
it subserves. **No named facial nerve nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **right** facial nerve nucleus module. The facial nerve
nucleus is **bilaterally symmetric** with the left facial nerve nucleus
and **strictly mirrored** — and it carries **NO warning at the nucleus
level**:

*   **Strict Bilateral Symmetry:** The **right** and **left** facial
    nerve nuclei are **structurally identical** — same branchial motor
    function, same upper/lower-face populations, same leaf status, same
    bilateral framing. The bilateral symmetry is **strict**.

*   **Bilateral Corticobulbar Input to Upper-Face Motoneurons
    (Connectivity Fact, NOT a Lateralization Warning):** The **right
    upper-face motoneurons** receive **bilateral corticobulbar input**
    from **both the right and left motor cortices**. This is a
    **structural fact** of the **facial motor system** — it is the
    **neural substrate** of **forehead sparing** in **upper-motor-
    neuron lesions**, and it is **not** a functional lateralization.

*   **Contralateral Corticobulbar Input to Lower-Face Motoneurons
    (Connectivity Fact, NOT a Lateralization Warning):** The **right
    lower-face motoneurons** receive **contralateral corticobulbar
    input only** from the **left motor cortex**. This is a
    **structural fact** of the **facial motor system** — it is the
    **neural substrate** of **lower-face involvement** in **upper-
    motor-neuron lesions**, and it is **not** a functional
    lateralization.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The facial nerve
    nucleus is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the facial nerve nucleus.

*   **NO Amygdala-Lateralization Warning of their own (the facial nerve
    nucleus is BRANCHIAL MOTOR, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The facial nerve nucleus
    is a **branchial motor brainstem nucleus** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**.
    **Note**: the "right-amygdala" lateralization is about the
    **amygdala**, not about this right pontine motor nucleus — do not
    import it.

**A consumer that assumes "right facial nerve nucleus = left facial
nerve nucleus" will be structurally correct** — the two sides are
**strictly symmetric** (the bilateral upper-face input and contralateral
lower-face input are structural facts, not lateralizations). The facial
nerve nucleus is a **strict-mirror pair with NO warning at the nucleus
level** — **no SLEA warning**, **no amygdala-lateralization warning**,
and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cranial_nerve_nuclei/left/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../cortex/``, or any other container.
    The facial nerve nucleus's relationships to the **facial nerve**,
    the **superior salivatory nucleus**, the **abducens nucleus**, the
    **motor trigeminal nucleus**, the **hypoglossal nucleus**, the
    **nucleus ambiguus**, the **extraocular motor nuclei**, the
    **facial muscles**, the **corticobulbar tract**, the **facial
    colliculus**, the **geniculate ganglion**, and the **nervus
    intermedius** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **upper-face
    motoneurons** and **lower-face motoneurons** are documented as
    **prose**, not as sub-modules. Consumers must not assume any exist
    as children; resolve neuron-population-level detail through the
    references.
*   **GREY-MATTER NUCLEUS — NOT the facial NERVE.** The **facial nerve
    nucleus** is the **grey-matter neuron cluster**; the **facial nerve**
    (right CN VII) is the **white-matter axon bundle**. Consumers must
    **not** conflate the two.
*   **NOT the superior salivatory nucleus — that is a SIBLING and it is
    PARASYMPATHETIC.** The **superior salivatory nucleus** is the
    **parasympathetic** CN VII sibling; the **facial nerve nucleus** is
    the **branchial motor** CN VII component. Consumers must **not**
    conflate the two.
*   **NOT the abducens nucleus — that is a SIBLING.** The **facial nerve
    fibers** loop around the abducens nucleus (facial colliculus), but
    the **abducens nucleus** is a **different structure**. Consumers
    must **not** conflate the two.
*   **NOT the motor trigeminal nucleus — that is a SIBLING and it is
    MASTICATION (CN V).** The **motor trigeminal nucleus** is the
    **branchial motor** nucleus for **mastication** (CN V, arch 1); the
    **facial nerve nucleus** is the **branchial motor** nucleus for
    **facial expression** (CN VII, arch 2). Consumers must **not**
    conflate the two.
*   **NOT the hypoglossal nucleus — that is MEDULLARY and it is TONGUE
    (CN XII).** The **hypoglossal nucleus** is the **somatic motor**
    nucleus for the tongue; the **facial nerve nucleus** is the
    **branchial motor** nucleus for facial expression. Consumers must
    **not** conflate the two.
*   **NOT the nucleus ambiguus — that is MEDULLARY and it is
    PHARYNX/LARYNX (CN IX/X).** The **nucleus ambiguus** is the
    **branchial motor** nucleus for the pharynx and larynx; the
    **facial nerve nucleus** is the **branchial motor** nucleus for
    facial expression. Consumers must **not** conflate the two.
*   **NOT the extraocular motor nuclei — those are CN III, IV, VI.** The
    **facial nerve nucleus** is **branchial motor** (CN VII); the
    extraocular nuclei are **somatic motor** (CN III, IV, VI). Consumers
    must **not** conflate the two.
*   **NOT the facial muscles — those are PERIPHERAL TARGETS.** The
    **nucleus** is central; the **muscles** are peripheral effectors.
    Consumers must **not** conflate the two.
*   **NOT the corticobulbar tract — that is the WHITE-MATTER
    UPPER-MOTOR-NEURON INPUT.** The **corticobulbar tract** is white
    matter; the **nucleus** is grey matter. **This distinction is
    clinically load-bearing** — corticobulbar lesion = central facial
    palsy with forehead sparing; facial nerve nucleus lesion =
    peripheral facial palsy with the whole face affected.
*   **NOT the facial colliculus — that is the SURFACE LANDMARK.** The
    **facial colliculus** marks the **facial nerve fibers** looping
    around the abducens nucleus; the **facial nerve nucleus** is a
    **separate, deeper structure**. Consumers must **not** conflate the
    two.
*   **NOT the geniculate ganglion — that is PERIPHERAL.** The
    **ganglion** is peripheral and sensory; the **nucleus** is central
    and motor. Consumers must **not** conflate the two.
*   **NOT the nervus intermedius — that is the CN VII
    SENSORY/PARASYMPATHETIC ROOT.** The **nervus intermedius** is the
    sensory/parasympathetic root; the **facial nerve nucleus** is the
    **motor root**. Consumers must **not** conflate the two.
*   **TWO FUNCTIONALLY DISTINCT POPULATIONS — UPPER-FACE vs.
    LOWER-FACE.** The **upper-face motoneurons** (bilateral
    corticobulbar input) and the **lower-face motoneurons**
    (contralateral corticobulbar input) are **prose**, not structural
    children. Consumers must **not** treat the facial nerve nucleus as a
    single uniform population.
*   **SLEA-FREE — no extended-amygdala relationship.** The facial nerve
    nucleus is **not** an extended-amygdala component, and it carries
    **no SLEA warning**.
*   **NOT the fear-output — the facial nerve nucleus is BRANCHIAL
    MOTOR.** The **fear-output** structure is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **facial nerve nucleus** is a **branchial motor
    brainstem nucleus** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The facial nerve nucleus is a local leaf
    under the right container, not a cross-listed leaf.
*   **No nested cross-listing.** The facial nerve nucleus has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with left facial nerve nucleus — strict mirror
    with NO warning.** Right and left facial nerve nucleus modules are
    **structurally identical** — same leaf status, same **branchial
    motor** framing, same **upper/lower-face populations**, same
    **SLEA-free** status, same **no warning** at the nucleus level.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.right import facial_nerve_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.right."
        "facial_nerve_nucleus"
    )

**Do not** assume the facial nerve nucleus is the **facial nerve**. The
**facial nerve** (right CN VII) is the **white-matter axon bundle**; the
**facial nerve nucleus** is the **grey-matter neuron cluster**. They are
**different structures**.

**Do not** assume the facial nerve nucleus is the **superior salivatory
nucleus**. The **superior salivatory nucleus** is a **sibling** under the
right container; **both are CN VII**, but they are **different functional
components** — the **facial nerve nucleus** is **branchial motor**; the
**superior salivatory nucleus** is **parasympathetic**.

**Do not** assume the facial nerve nucleus is the **abducens nucleus**.
The **abducens nucleus** is a **sibling**; the **facial nerve fibers**
loop around it (facial colliculus), but the **facial nerve nucleus**
itself is **anatomically separate**.

**Do not** assume the facial nerve nucleus is the **motor trigeminal
nucleus**, the **hypoglossal nucleus**, or the **nucleus ambiguus**.
Those are **different branchial/somatic motor nuclei** for **different
cranial nerves and different peripheral targets** — mastication (CN V),
tongue (CN XII), and pharynx/larynx (CN IX/X), respectively.

**Do not** assume the facial nerve nucleus is the **corticobulbar
tract**. The **corticobulbar tract** is the **white-matter
upper-motor-neuron input**; the **facial nerve nucleus** is the
**grey-matter lower-motor-neuron cluster**. **This distinction is
clinically load-bearing** — corticobulbar lesion = central facial palsy
with forehead sparing; facial nerve nucleus lesion = peripheral facial
palsy with the whole face affected.

**Do not** assume the facial nerve nucleus is the **facial colliculus**.
The **facial colliculus** marks the **facial nerve fibers**; the
**facial nerve nucleus** is a **separate, deeper structure**.

**Do not** assume the facial nerve nucleus is the **geniculate
ganglion** or the **nervus intermedius**. Those are **peripheral** or
**sensory/parasympathetic** structures; the **facial nerve nucleus** is
the **central branchial motor nucleus**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the facial nerve nucleus. **The facial nerve nucleus is
SLEA-FREE** — it is **not** an extended-amygdala component, and it is
**NOT part of the fear circuit**. **Note**: the "right-amygdala"
lateralization is about the **amygdala**, not about this right pontine
motor nucleus — do not import it.

Iterating the facial nerve nucleus's (empty) children (recommended
consumer pattern)::

    FACIAL_NERVE_NUCLEUS_CHILDREN = ()
    # The facial nerve nucleus is a leaf. The upper-face motoneurons and
    # lower-face motoneurons are prose, not modules.

Reaching the facial nerve (recommended consumer pattern — the
white-matter axon bundle)::

    # The facial nerve (right CN VII) is the WHITE-MATTER axon bundle:
    #
    #   peripheral: right CN VII -> right facial muscles
    #
    # The nucleus is the CENTRAL neuronal source; the nerve is the
    # PERIPHERAL conduction infrastructure.

Reaching the superior salivatory nucleus (recommended consumer pattern —
the CN VII parasympathetic sibling)::

    # The superior salivatory nucleus is the PARASYMPATHETIC sibling
    # under the right container:
    #
    #   .../cranial_nerve_nuclei/right/superior_salivatory_nucleus/
    #
    # The facial nerve nucleus is the BRANCHIAL MOTOR sibling — both are
    # CN VII, but different functional components.

Reaching the abducens nucleus (recommended consumer pattern — the
sibling around which the facial fibers loop)::

    # The abducens nucleus is the SOMATIC MOTOR sibling under the right
    # container:
    #
    #   .../cranial_nerve_nuclei/right/abducens_nucleus/
    #
    # The facial nerve FIBERS loop around the abducens nucleus (facial
    # colliculus), but the FACIAL NERVE NUCLEUS itself is anatomically
    # separate.

Reaching the motor trigeminal nucleus (recommended consumer pattern —
the CN V branchial motor sibling)::

    # The motor trigeminal nucleus is the BRANCHIAL MOTOR sibling under
    # the right container:
    #
    #   .../cranial_nerve_nuclei/right/motor_trigeminal_nucleus/
    #
    # The motor trigeminal nucleus innervates MASTICATION (CN V, arch 1);
    # the facial nerve nucleus innervates FACIAL EXPRESSION (CN VII,
    # arch 2).

Reaching the corticobulbar tract (recommended consumer pattern — the
upper-motor-neuron input)::

    # The corticobulbar tract is the WHITE-MATTER upper-motor-neuron
    # pathway:
    #
    #   .../white_matter/.../corticobulbar_tract/  (or equivalent path)
    #
    # The corticobulbar tract PROVIDES INPUT TO the facial nerve nucleus;
    # the facial nerve nucleus is the LOWER-MOTOR-NEURON OUTPUT.

Reaching the facial colliculus (recommended consumer pattern — the
surface landmark)::

    # The facial colliculus marks the FACIAL NERVE FIBERS looping around
    # the abducens nucleus on the floor of the fourth ventricle:
    #
    #   (surface landmark of the fourth ventricle floor)
    #
    # The facial colliculus is NOT the facial nerve nucleus — it marks
    # the facial nerve FIBERS.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        fnn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
            f"{side}.facial_nerve_nucleus"
        )
        # resolve fnn_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The facial nerve nucleus's neuron populations are prose, not
    # modules:
    #   upper-face motoneurons -> frontalis, orbicularis oculi;
    #                             BILATERAL corticobulbar input
    #                             (forehead sparing in UMN lesions)
    #   lower-face motoneurons -> orbicularis oris, buccinator, platysma,
    #                             stapedius, stylohyoid, posterior belly
    #                             of digastric; CONTRALATERAL
    #                             corticobulbar input (lower-face
    #                             involvement in both UMN and LMN lesions)
    #
    # Do not attempt to resolve these as sub-paths of the facial nerve
    # nucleus.

References
----------
*   **Canonical facial nerve anatomy:** May, M., Schaitkin, B.M. (2000).
    *The Facial Nerve*, 2nd ed. (Facial nerve nucleus and the facial
    motor system — definitive.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Facial nerve nucleus in
    overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An Atlas
    of Structures, Sections, and Systems*, 8th ed. (Facial nerve nucleus
    and the facial colliculus.)
*   **Facial nerve — clinical:** Gilden, D.H. (2004). "Bell's palsy."
    *New England Journal of Medicine* 351:1323–1331. (Peripheral facial
    palsy — Bell's palsy as a nerve-level lesion, not a nucleus lesion.)
*   **Facial palsy — central vs. peripheral:** Jenkins, D.B., Jenkins,
    R.A. (2007). "Facial nerve." In *Neuroanatomy and Neuroscience*.
    (Upper-motor-neuron vs. lower-motor-neuron facial palsy — forehead
    sparing in central lesions.)
*   **Corticobulbar tract:** Kuypers, H.G.J.M. (1958). "Corticobulbar
    connexions to the pons and lower brain-stem in man: an anatomical
    study." *Brain* 81:364–388. (Corticobulbar input to the facial nerve
    nucleus — bilateral upper-face, contralateral lower-face.)
*   **Facial colliculus:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Facial colliculus as the
    surface landmark of the facial nerve fibers looping around the
    abducens nucleus.)
*   **Superior salivatory nucleus (contrast — the CN VII parasympathetic
    sibling):** Loewy, A.D., Spyer, K.M. (1990). *Central Regulation of
    Autonomic Functions*. (Superior salivatory nucleus — the
    parasympathetic CN VII component; distinct from the facial nerve
    nucleus.)
*   **Abducens nucleus (contrast — the sibling around which the facial
    fibers loop):** Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye
    Movements*, 5th ed. (Abducens nucleus and horizontal gaze — distinct
    from the facial nerve nucleus.)
*   **Motor trigeminal nucleus (contrast — the CN V branchial motor
    sibling):** Usunoff, K.G., Marani, E., Schoen, J.H.R. (2006). "The
    trigeminal system." *Advances in Anatomy, Embryology, and Cell
    Biology* 184:1–146. (Motor trigeminal nucleus — mastication, CN V,
    arch 1; distinct from facial nerve nucleus.)
*   **Hypoglossal nucleus (contrast — the medullary tongue motor
    nucleus):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Hypoglossal nucleus — tongue motor
    nucleus; distinct from facial nerve nucleus.)
*   **Nucleus ambiguus (contrast — the medullary branchial motor
    nucleus):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Nucleus ambiguus — pharynx/larynx
    motor nucleus; distinct from facial nerve nucleus.)
*   **Geniculate ganglion (contrast — the peripheral sensory
    ganglion):** Standring, S. (ed.) (2020). *Gray's Anatomy: The
    Anatomical Basis of Clinical Practice*, 42nd ed. (Geniculate
    ganglion — peripheral sensory ganglion on CN VII; distinct from the
    facial nerve nucleus.)
*   **Nervus intermedius (contrast — the CN VII
    sensory/parasympathetic root):** May, M., Schaitkin, B.M. (2000).
    *The Facial Nerve*, 2nd ed. (Nervus intermedius — the
    sensory/parasympathetic root of CN VII; distinct from the facial
    nerve nucleus.)
*   **SLEA (contrast — the facial nerve nucleus is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the facial nerve
    nucleus.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the right facial nerve nucleus. **Note**: the
    "right-amygdala" lateralization is about the **amygdala**, not about
    this right pontine motor nucleus.)
*   NeuroNames — Facial nerve nucleus (right); FMA — Facial motor nucleus
    (right member).
"""