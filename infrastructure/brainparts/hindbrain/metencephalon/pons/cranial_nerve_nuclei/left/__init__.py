"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left
================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── left   <-- THIS MODULE
                    ├── abducens_nucleus
                    ├── chief_sensory_trigeminal_nucleus
                    ├── facial_nerve_nucleus
                    ├── motor_trigeminal_nucleus
                    ├── superior_salivatory_nucleus
                    └── vestibulocochlear_nuclei
                        ├── cochlear_nuclei
                        └── vestibular_nuclei

**Primary synonym:** Left pontine cranial-nerve nuclei; left cranial-nerve
nuclei of the pons; left metencephalic cranial-nerve nuclei; "the left
pontine CN V–VIII subset."
**Cytoarchitectonic designation:** **Not a Brodmann area** — a **bilateral
sub-container** of **brainstem grey-matter nuclei**. A **heterogeneous
collection** of **six left-side cranial-nerve nuclei** in the **left
pontine tegmentum** — **motor** (`abducens_nucleus`,
`facial_nerve_nucleus`, `motor_trigeminal_nucleus`), **general sensory**
(`chief_sensory_trigeminal_nucleus`), **parasympathetic**
(`superior_salivatory_nucleus`), and **special sensory**
(`vestibulocochlear_nuclei`, comprising `cochlear_nuclei` and
`vestibular_nuclei`).
**Part of:** The **cranial_nerve_nuclei** container — specifically, the
**left bilateral half** of the pontine cranial-nerve nuclear collection.
The **cranial_nerve_nuclei** container is the **pontine** cranial-nerve
nuclear collection; the **left** container is its **left-side structural
child**.
**Structural parent:** ``.../cranial_nerve_nuclei/`` → **direct child** of
the cranial_nerve_nuclei container.
**Structural children:** **Six left-side cranial-nerve nuclei**:
``abducens_nucleus``, ``chief_sensory_trigeminal_nucleus``,
``facial_nerve_nucleus``, ``motor_trigeminal_nucleus``,
``superior_salivatory_nucleus``, and ``vestibulocochlear_nuclei`` (itself
a **sub-container** with ``cochlear_nuclei`` and ``vestibular_nuclei``).
**Boundary status (LEFT HALF — NOT the whole cranial_nerve_nuclei
container):** **Boundary case — the left container is the LEFT HALF of the
cranial_nerve_nuclei, NOT the whole container.** The
**cranial_nerve_nuclei** container (``.../cranial_nerve_nuclei/``) has
**two structural children** — ``left`` and ``right``. The **left**
container (here) is the **left-side** half only. Consumers must **not**
conflate the left container with the **whole cranial_nerve_nuclei
collection** — the right side is a **separate structural sibling**.
**Boundary status (NOT the right container — strict mirror, no warning):**
**Boundary case — the left container is NOT the right container; the two
are a STRICT MIRROR PAIR with NO warning at the container level.** The
**right** container (``.../cranial_nerve_nuclei/right/``) is the
**structurally identical** right-side counterpart — same six nuclei, same
leaf status for each nucleus, same bilateral framing. The two sides are
**strictly mirrored** — any lateralization is documented **inside the
individual nucleus modules**, not at the container level. Consumers must
**not** import a lateralization warning into the left container — there
is **none at the container level**.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the left
container is a CONTAINER, not a leaf.** It has **six structural
children** (the six left-side cranial-nerve nuclei). The
**vestibulocochlear_nuclei** is itself a **sub-container** with
**cochlear_nuclei** and **vestibular_nuclei** as its children. Consumers
must **not** treat the left container as a leaf, and must **not** assume
the six nuclei are absent — they are its **direct structural children**.
**Boundary status (GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS):**
**Boundary case — the left container holds the GREY-MATTER NUCLEI, NOT the
cranial-nerve FIBERS (axons).** The **cranial nerves** (left CN V, VI,
VII, VIII) are the **white-matter axon bundles** that **leave** the left
pontine tegmentum and **travel** to the periphery. The **left container**
(here) holds the **grey-matter neuron clusters** that **give rise to**
(motor, parasympathetic) or **receive** (sensory, special sensory) those
axons. They are **DIFFERENT STRUCTURES** — the **nuclei** are grey matter;
the **nerves** are white matter. Consumers must **not** conflate the
**left nuclei** with the **left cranial nerves**.
**Boundary status (NOT the whole pons — the pons is the grandparent):**
**Boundary case — the left container is NOT the pons; the pons is the
grandparent.** The **pons** (``.../pons/``) is the **whole metencephalic
brainstem segment** — it contains the **basilar pons**, the **pontine
tegmentum**, the **pontine nuclei**, the **corticospinal/corticobulbar
tracts**, the **middle cerebellar peduncle**, and the
**cranial_nerve_nuclei** (both left and right). The **left container**
(here) is the **left-side cranial-nerve nuclei only**. Consumers must
**not** conflate the left container with the **whole pons**.
**Boundary status (NOT midbrain or medullary cranial-nerve nuclei — those
are DIFFERENT BRAINSTEM LEVELS):** **Boundary case — the left container
is NOT the midbrain or medullary cranial-nerve nuclei.** The **midbrain**
(``.../midbrain/cranial_nerve_nuclei/``) hosts **CN III, IV,
mesencephalic V, Edinger-Westphal**; the **medulla oblongata**
(``.../medulla_oblongata/cranial_nerve_nuclei/``) hosts **CN IX, X, XI,
XII, inferior salivatory, nucleus ambiguus, hypoglossal, dorsal motor
vagus, solitary**. The **left container** (here) is the **left pontine
subset only** — **CN V (chief sensory + motor), CN VI, CN VII (facial +
superior salivatory), CN VIII (cochlear + vestibular)**. Consumers must
**not** conflate the left pontine nuclei with the midbrain or medullary
cranial-nerve nuclei.
**Boundary status (NOT the whole trigeminal complex — the trigeminal
system spans levels):** **Boundary case — the left container does NOT
contain the whole left trigeminal nuclear complex.** The **left trigeminal
system** has **three** brainstem nuclei: the **left mesencephalic
trigeminal nucleus** (midbrain — proprioception), the **left chief sensory
trigeminal nucleus** (pons — discriminative touch, **in this container**),
and the **left spinal trigeminal nucleus** (medulla/pons junction —
pain/temperature). The **left container** (here) contains **only the
left chief sensory trigeminal nucleus** and the **left motor trigeminal
nucleus** — it does **not** contain the left mesencephalic or spinal
trigeminal nuclei. Consumers must **not** conflate the left pontine
trigeminal nuclei with the **whole left trigeminal complex**.
**Boundary status (NOT the trigeminal ganglion or any sensory ganglion —
those are PERIPHERAL):** **Boundary case — the left container is NOT the
left trigeminal ganglion (or any left sensory ganglion).** The **left
trigeminal ganglion** (left semilunar / Gasserian ganglion) is a
**peripheral sensory ganglion** outside the brainstem containing the
**left primary sensory neuron cell bodies** for the left trigeminal
nerve. The **left container** (here) holds the **left central grey-matter
nuclei** inside the left pontine tegmentum. They are **DIFFERENT
STRUCTURES** — the **ganglion** is peripheral; the **nuclei** are central.
Consumers must **not** conflate the **left central nuclei** with the
**left peripheral ganglion**.
**Boundary status (NOT the cerebellum — that is the metencephalic
sibling):** **Boundary case — the left container is NOT the left
cerebellum.** The **left cerebellum**
(``.../metencephalon/cerebellum/hemispheres/left/``) is the **left
metencephalic cerebellar half**, with its **own nuclei** (left dentate,
left fastigial, left interposed: left emboliform + left globose) and its
**own cortex**. The **left container** (here) holds the **left pontine
cranial-nerve nuclei**, not the left cerebellar nuclei. Consumers must
**not** conflate the **left pontine cranial-nerve nuclei** with the
**left cerebellar nuclei**.
**Boundary status (NOT locus coeruleus, parabrachial area, pontine
nuclei, or other left pontine structures):** **Boundary case — the left
container is NOT the left locus coeruleus, the left parabrachial area,
the left pontine nuclei, or other left pontine structures.** The **left
locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) is the
**noradrenergic** nucleus; the **left parabrachial area**
(``.../pons/parabrachial_area/``) is the **visceral/autonomic relay**;
the **left pontine nuclei** (``.../pons/pontine_nuclei/left/``) are the
**cortico-ponto-cerebellar relay** in the **left basilar pons**. None of
these are **left cranial-nerve nuclei**. The **left container** (here)
is **only** the left nuclei that **give rise to or receive** the **left
cranial nerves V, VI, VII, VIII**. Consumers must **not** conflate the
left cranial-nerve nuclei with **other left pontine nuclei**.
**Boundary status (NOT the solitary nucleus — that is the medullary
visceral-afferent hub):** **Boundary case — the left container is NOT the
left solitary nucleus.** The **left solitary nucleus** (left nucleus
tractus solitarius,
``.../medulla_oblongata/solitary_nucleus/left/``) is the **left medullary
visceral-afferent hub** for **left CN VII, IX, X** (taste, visceral
sensation, baroreception, respiratory chemoreception). The **left
container** (here) contains the **left superior salivatory nucleus** (left
CN VII parasympathetic), but it does **not** contain the **left solitary
nucleus**. Consumers must **not** conflate the left pontine nuclei with
the **left solitary nucleus**.
**Boundary status (NOT a single functional system — MULTIPLE nuclei with
DIFFERENT functions):** **Boundary case — the left container is a
HETEROGENEOUS collection of six left-side nuclei with DIFFERENT
functions, not a single uniform system.** The collection includes:
*   **Left abducens nucleus (CN VI)** — **somatic motor**; controls the
    **left lateral rectus** muscle (left eye abduction).
*   **Left facial nerve nucleus (CN VII)** — **branchial motor**;
    controls the **left muscles of facial expression**.
*   **Left motor trigeminal nucleus (CN V)** — **branchial motor**;
    controls the **left muscles of mastication**.
*   **Left chief sensory trigeminal nucleus (CN V)** — **general
    sensory**; **discriminative touch** from the **left face**.
*   **Left superior salivatory nucleus (CN VII)** — **parasympathetic**;
    controls the **left lacrimal** and **left salivary** glands.
*   **Left vestibulocochlear nuclei (CN VIII)** — **special sensory**;
    **left cochlear nuclei** subserve **left hearing**; **left vestibular
    nuclei** subserve **left balance and spatial orientation**.
**Each nucleus is functionally distinct** — the tree wires them as
**separate structural children under the left container**. Consumers must
**not** treat the left container as a single uniform nucleus — it is a
**distributed collection** of functionally distinct left-side nuclei.

Overview
--------
The left container is the **left-side half** of the pontine cranial-nerve
nuclear collection — the **six grey-matter nuclei** in the **left pontine
tegmentum** that **give rise to** (motor, parasympathetic) or **receive**
(sensory, special sensory) the **left cranial nerves V, VI, VII, and
VIII**. It is a **container** under the cranial_nerve_nuclei container,
with **six structural children** (six left-side nuclei), one of which
(the **vestibulocochlear_nuclei**) is itself a **sub-container**.

**The left container is a CONTAINER, NOT a leaf.** Its structural
children are the **six left-side nuclei**. The **left
vestibulocochlear_nuclei** is itself a **sub-container** with **left
cochlear_nuclei** and **left vestibular_nuclei** as its children.

**The left container is the LEFT HALF of the cranial_nerve_nuclei, NOT
the whole container.** The **cranial_nerve_nuclei** container has **two
structural children** — ``left`` and ``right``. The **left** container
(here) is the **left-side** half only. The right side is a **separate
structural sibling**.

**The left container and the right container are a STRICT MIRROR PAIR
with NO warning at the container level.** The two sides are
**structurally identical** — same six nuclei, same leaf status for each
nucleus, same bilateral framing. Any lateralization is documented
**inside the individual nucleus modules**, not at the container level.

**The left container holds the GREY-MATTER NUCLEI, NOT the cranial-nerve
FIBERS.** The **left cranial nerves V, VI, VII, VIII** are the
**white-matter axon bundles** that **travel** to and from the periphery.
The **left container** (here) holds the **grey-matter neuron clusters**
inside the left pontine tegmentum. They are **DIFFERENT STRUCTURES** —
the **nuclei** are grey matter; the **nerves** are white matter.

**The left container is NOT the whole left trigeminal complex.** The
**left trigeminal system** spans three brainstem levels — the **left
mesencephalic trigeminal nucleus** (midbrain), the **left chief sensory
trigeminal nucleus** (pons, **in this container**), and the **left spinal
trigeminal nucleus** (medulla/pons junction). The **left container**
contains **only the pontine trigeminal components** (chief sensory +
motor).

**The left container is HETEROGENEOUS.** The six left-side nuclei are
**functionally distinct** — **motor** (left abducens, left facial, left
motor trigeminal), **general sensory** (left chief sensory trigeminal),
**parasympathetic** (left superior salivatory), and **special sensory**
(left vestibulocochlear). The tree wires them as **separate structural
children under the left container**.

Nucleus Composition (structural children, prose)
------------------------------------------------
The left container contains **six left-side nuclei**, documented as
**structural children** (not as leaves of the container):

*   **Left abducens nucleus**
    (``.../cranial_nerve_nuclei/left/abducens_nucleus/``) — **somatic
    motor**; controls the **left lateral rectus** muscle (left eye
    abduction). CN VI.

*   **Left chief sensory trigeminal nucleus**
    (``.../cranial_nerve_nuclei/left/chief_sensory_trigeminal_nucleus/``)
    — **general sensory**; **discriminative touch** from the **left
    face**. CN V (principal sensory nucleus).

*   **Left facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) —
    **branchial motor**; controls the **left muscles of facial
    expression**. CN VII.

*   **Left motor trigeminal nucleus**
    (``.../cranial_nerve_nuclei/left/motor_trigeminal_nucleus/``) —
    **branchial motor**; controls the **left muscles of mastication**.
    CN V.

*   **Left superior salivatory nucleus**
    (``.../cranial_nerve_nuclei/left/superior_salivatory_nucleus/``) —
    **parasympathetic**; controls the **left lacrimal** and **left
    salivary** glands. CN VII.

*   **Left vestibulocochlear nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/``) —
    **special sensory**; a **sub-container** with two children:
    *   **Left cochlear nuclei** — **left hearing** (left CN VIII
        cochlear division).
    *   **Left vestibular nuclei** — **left balance and spatial
        orientation** (left CN VIII vestibular division).

**These nuclei are structural children of the left container.** The
left container's **structural children** are the **six left-side
nuclei**; the **left vestibulocochlear nuclei** is a **sub-container**
with two of its own children. Consumers resolving nucleus-level detail
go **through** the left container, and resolving cochlear/vestibular
detail goes **through** the left vestibulocochlear nuclei.

The Left / Right Boundary
-------------------------
This is the **strict-mirror** boundary:

*   **Left container** (this module) — the **left-side** pontine
    cranial-nerve nuclei.

*   **Right container** (``.../cranial_nerve_nuclei/right/``) — the
    **structurally identical** right-side pontine cranial-nerve nuclei.

**They are a STRICT MIRROR PAIR with NO warning at the container level.**
The two sides are **structurally identical** — same six nuclei, same leaf
status for each nucleus, same bilateral framing. Any lateralization is
documented **inside the individual nucleus modules**, not at the container
level. Consumers must **not** import a lateralization warning into the
left container.

The Left Container / Cranial Nerve Nuclei Container Boundary
------------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Left container** (this module) — the **left-side** half of the
    pontine cranial-nerve nuclear collection.

*   **Cranial_nerve_nuclei container** (``.../cranial_nerve_nuclei/``)
    — the **whole pontine collection**, with **two structural children**
    (``left`` and ``right``).

**The left container is a child of the cranial_nerve_nuclei container.**
Consumers must **not** conflate the left half with the **whole pontine
collection** — the right side is a **separate structural sibling**.

The Left Container / Cranial Nerves Boundary
--------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Left container** (this module) — the **left-side grey-matter
    neuron clusters** in the left pontine tegmentum.

*   **Left cranial nerves V, VI, VII, VIII** — the **left white-matter
    axon bundles** that travel to and from the periphery.

**They are DIFFERENT STRUCTURES.** The **left nuclei** are the **left
central neuronal sources/targets**; the **left nerves** are the **left
peripheral conduction infrastructure**. Consumers must **not** conflate
the two.

The Left Container / Pons Boundary
----------------------------------
This is the **great-grandchild vs. grandparent** boundary:

*   **Left container** (this module) — the **left-side tegmental
    grey-matter nuclei** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal/
    corticobulbar tracts**, the **middle cerebellar peduncle**, and the
    **cranial-nerve nuclei** (both left and right).

**The left container is a great-grandchild of the pons** (via
cranial_nerve_nuclei). Consumers must **not** conflate the left
cranial-nerve nuclei with the **whole pons**.

The Left Container / Midbrain and Medullary Cranial-Nerve Nuclei Boundary
-------------------------------------------------------------------------
This is the **brainstem-level** boundary:

*   **Left container** (this module) — the **left pontine** nuclei only —
    **left CN V (chief sensory + motor)**, **left CN VI**, **left CN
    VII (facial + superior salivatory)**, **left CN VIII (cochlear +
    vestibular)**.

*   **Left midbrain cranial-nerve nuclei**
    (``.../midbrain/cranial_nerve_nuclei/left/``) — **left CN III
    (oculomotor)**, **left CN IV (trochlear)**, **left mesencephalic
    trigeminal nucleus (left CN V proprioceptive)**, **left
    Edinger-Westphal nucleus (left CN III parasympathetic)**.

*   **Left medullary cranial-nerve nuclei**
    (``.../medulla_oblongata/cranial_nerve_nuclei/left/``) — **left CN
    IX (glossopharyngeal)**, **left CN X (vagus)**, **left CN XI
    (accessory)**, **left CN XII (hypoglossal)**, **left inferior
    salivatory nucleus**, **left nucleus ambiguus**, **left hypoglossal
    nucleus**, **left dorsal motor nucleus of the vagus**, **left
    solitary nucleus**.

**They are DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate
the **left pontine** cranial-nerve nuclei with the **left midbrain** or
**left medullary** cranial-nerve nuclei.

The Left Container / Trigeminal Complex Boundary
------------------------------------------------
This is the **partial-complex** boundary:

*   **Left container** (this module) — contains **only** the **left
    chief sensory trigeminal nucleus** (discriminative touch) and the
    **left motor trigeminal nucleus** (mastication).

*   **Left mesencephalic trigeminal nucleus**
    (``.../midbrain/tegmentum/mesencephalic_trigeminal_nucleus/left/``)
    — **left proprioception** (left CN V mesencephalic division).

*   **Left spinal trigeminal nucleus**
    (``.../medulla_oblongata/spinal_trigeminal_nucleus/left/``) — **left
    pain and temperature** (left CN V spinal division).

**The left trigeminal nuclear complex spans three brainstem levels.** The
**left container** contains **only the left pontine components**.
Consumers must **not** conflate the left pontine trigeminal nuclei with
the **whole left trigeminal complex**.

The Left Container / Left Cerebellum Boundary
---------------------------------------------
This is the **metencephalic-sibling** boundary:

*   **Left container** (this module) — the **left pontine** cranial-nerve
    nuclei.

*   **Left cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/left/``) — the **left
    metencephalic cerebellar half**, with its **own nuclei** (left
    dentate, left fastigial, left interposed: left emboliform + left
    globose) and its **own cortex**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
**left pontine cranial-nerve nuclei** with the **left cerebellar
nuclei**.

The Left Container / Other Left Pontine Structures Boundary
-----------------------------------------------------------
This is the **non-cranial-nerve left pontine** boundary:

*   **Left container** (this module) — **only** the left nuclei that
    **give rise to or receive** the **left cranial nerves V, VI, VII,
    VIII**.

*   **Left locus coeruleus**
    (``.../pons/tegmentum/locus_coeruleus/``) — the **left
    noradrenergic** nucleus.

*   **Left parabrachial area** (``.../pons/parabrachial_area/``) — the
    **left visceral/autonomic relay**.

*   **Left pontine nuclei** (``.../pons/pontine_nuclei/left/``) — the
    **left cortico-ponto-cerebellar relay** in the **left basilar
    pons**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
left cranial-nerve nuclei with **other left pontine nuclei**.

The Left Container / Left Solitary Nucleus Boundary
---------------------------------------------------
This is the **visceral-afferent** boundary:

*   **Left container** (this module) — contains the **left superior
    salivatory nucleus** (left CN VII parasympathetic), but **not** the
    **left solitary nucleus**.

*   **Left solitary nucleus**
    (``.../medulla_oblongata/solitary_nucleus/left/``) — the **left
    medullary visceral-afferent hub** for **left CN VII, IX, X** (taste,
    visceral sensation, baroreception, respiratory chemoreception).

**The left solitary nucleus is medullary, not pontine.** Consumers must
**not** conflate the left pontine nuclei with the **left solitary
nucleus**.

Function in the Human Brain
---------------------------
The left container's functions are **the left cranial-nerve sensorimotor
and parasympathetic relay** — **NOT a single unified function**:

*   **Somatic Motor (Left Abducens Nucleus, left CN VI):** Controls the
    **left lateral rectus** muscle — **left eye abduction**. The left
    abducens nucleus is the **sole source** of the left lateral rectus
    motor innervation.

*   **Branchial Motor (Left Facial Nerve Nucleus, left CN VII):**
    Controls the **left muscles of facial expression** — the left
    facial nerve is the **principal left motor nerve of the face**.

*   **Branchial Motor (Left Motor Trigeminal Nucleus, left CN V):**
    Controls the **left muscles of mastication** — the left motor
    trigeminal nucleus is the **sole source** of the left motor
    trigeminal innervation.

*   **General Sensory (Left Chief Sensory Trigeminal Nucleus, left CN
    V):** **Discriminative touch** from the **left face** — the left
    principal sensory nucleus is the **left pontine** component of the
    left trigeminal nuclear complex.

*   **Parasympathetic (Left Superior Salivatory Nucleus, left CN VII):**
    Controls the **left lacrimal** and **left salivary** glands — the
    left superior salivatory nucleus is the **left preganglionic
    parasympathetic** source for the left facial nerve's autonomic
    component.

*   **Special Sensory (Left Vestibulocochlear Nuclei, left CN VIII):**
    The **left cochlear nuclei** subserve **left hearing**; the **left
    vestibular nuclei** subserve **left balance and spatial
    orientation**. The left vestibulocochlear nuclei are the **left
    brainstem relay** for the left auditory and vestibular senses.

**The unifying theme:** the left container is the **left pontine
cranial-nerve nuclear collection** — the **left grey-matter nuclei**
that **give rise to or receive** the **left cranial nerves V, VI, VII,
VIII**. It is **heterogeneous** and **strictly mirrored** — the six
left-side nuclei are **functionally distinct**, and they are **structural
children** of the left container.

Associated Disorders
--------------------
The left container has **no single named clinical syndrome as a
collection** — its clinical associations are **left-nucleus-specific**:

*   **Left Abducens Nucleus (left CN VI) — Left Sixth Nerve Palsy:**
    Lesions cause **left lateral rectus palsy** — **inability to abduct
    the left eye**, **diplopia** on left lateral gaze.

*   **Left Facial Nerve Nucleus (left CN VII) — Left Facial Nerve Palsy
    (left Bell's Palsy, left Supranuclear Palsy):** Lesions cause
    **ipsilateral (left) facial weakness** — **inability to close the
    left eye**, **left facial droop**, **loss of left forehead
    wrinkling** (peripheral lesions) versus **left forehead sparing**
    (supranuclear lesions).

*   **Left Motor Trigeminal Nucleus (left CN V) — Left Trigeminal Motor
    Palsy:** Lesions cause **weakness of left mastication** — **jaw
    deviation** toward the **left** side.

*   **Left Chief Sensory Trigeminal Nucleus (left CN V) — Left Trigeminal
    Sensory Loss:** Lesions cause **left facial sensory loss** —
    **discriminative touch** impairment on the **left face**.

*   **Left Superior Salivatory Nucleus (left CN VII) — Left Autonomic
    Facial Palsy:** Lesions cause **reduced left lacrimation** and
    **reduced left salivation**.

*   **Left Vestibulocochlear Nuclei (left CN VIII) — Left
    Vestibulocochlear Disorders:** Lesions cause **left hearing loss**
    (left cochlear nuclei) and **left vertigo / left nystagmus / left
    imbalance** (left vestibular nuclei).

*   **No Named "Left Cranial Nerve Nuclei Syndrome":** The left
    container is a **heterogeneous collection**, not a **single
    structure** — it has **no named clinical syndrome as a collection**.
    Its clinical relevance is **left-nucleus-specific**, via the
    **individual left cranial-nerve nuclei** and the **left cranial
    nerves** they subserve.

**What is NOT here:** The left container is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala), **fear conditioning** (amygdala —
central nucleus + basolateral nuclei), **Urbach-Wiethe disease**
(amygdala — basolateral nuclei), **Alzheimer's disease** (hippocampus,
nucleus basalis), or **Parkinson's disease** (substantia nigra). Its
clinical relevance is **left-cranial-nerve-specific**, via the
**individual left nuclei** and the **left cranial nerves** they subserve.
**No named left cranial_nerve_nuclei syndrome exists as a collection.**

Lateralization Notes
--------------------
This is the **left** container of the cranial_nerve_nuclei. The left
container is **bilaterally symmetric** with the right container and
**strictly mirrored** — and it carries **NO warning at the container
level**:

*   **Strict Bilateral Symmetry:** The **left** and **right**
    containers are **structurally identical** — same six nuclei under
    each, same leaf status for each nucleus, same bilateral framing. The
    bilateral symmetry is **strict**.

*   **Lateralization is Nucleus-Specific (Contested, Documented in the
    Nucleus Modules):** Any functional lateralization (e.g. left facial
    motor control, left vestibular asymmetry, left auditory
    lateralization) is documented **inside the individual left nucleus
    modules**, not at the container level. Consumers must **not** assume
    a container-level lateralization — the left container is a
    **strict-mirror left half**.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The left
    container is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the left container.

*   **NO Amygdala-Lateralization Warning of their own (the left
    container is MODULATORY-AGNOSTIC, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The left container is a
    **left cranial-nerve nuclear collection** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**. The
    **left container** is **SLEA-free** and **amygdala-agnostic**.

**A consumer that assumes "left container = right container" will be
structurally correct** — the two sides are **strictly symmetric** (any
lateralization is documented in the nucleus modules). The left container
is a **strict-mirror pair with NO warning at the container level** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left container is the **left
    half**; it does **not** import the right container at module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../medulla_oblongata/``,
    ``.../metencephalon/cerebellum/``, or any other container. The left
    container's relationships to the **left midbrain** and **left
    medullary** cranial-nerve nuclei, the **left cerebellum**, the
    **left locus coeruleus**, the **left parabrachial area**, and the
    **left pontine nuclei** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children are the SIX left-side
    nuclei.** The **left vestibulocochlear nuclei** is itself a
    **sub-container** with **left cochlear nuclei** and **left
    vestibular nuclei** as its children.
*   **LEFT HALF — NOT the whole cranial_nerve_nuclei container.** The
    **cranial_nerve_nuclei** container has **two structural children** —
    ``left`` and ``right``. The **left** container (here) is the
    **left-side** half only.
*   **STRICT MIRROR with the right container — NO warning at the
    container level.** The **left** and **right** containers are
    **structurally identical**. Any lateralization is documented **inside
    the individual nucleus modules**.
*   **GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS.** The **left
    nuclei** are the **grey-matter neuron clusters**; the **left cranial
    nerves V, VI, VII, VIII** are the **white-matter axon bundles**.
    Consumers must **not** conflate the two.
*   **NOT the whole brainstem or the whole left cranial-nerve system —
    only the LEFT PONTINE subset.** The **left midbrain** and **left
    medullary** cranial-nerve nuclei are **wired elsewhere**.
*   **NOT a single functional system — MULTIPLE left-side nuclei.** The
    **left abducens nucleus**, **left facial nerve nucleus**, **left
    motor trigeminal nucleus**, **left chief sensory trigeminal
    nucleus**, **left superior salivatory nucleus**, and **left
    vestibulocochlear nuclei** are **functionally distinct**.
*   **NOT the left mesencephalic or left spinal trigeminal nucleus — the
    left trigeminal system spans levels.** The **left container**
    contains **only the left pontine trigeminal components** (chief
    sensory + motor).
*   **NOT the left trigeminal ganglion or any left sensory ganglion —
    those are PERIPHERAL.** The **left nuclei** are **central**; the
    **left ganglia** are **peripheral**.
*   **NOT the left cerebellum — that is the metencephalic sibling.** The
    **left cerebellar nuclei** (left dentate, left fastigial, left
    interposed) are **wired elsewhere**.
*   **NOT the left solitary nucleus — that is the left medullary
    visceral-afferent hub.** The **left superior salivatory nucleus** is
    here, but the **left solitary nucleus** is not.
*   **SLEA-FREE — no extended-amygdala relationship.** The left container
    is **not** an extended-amygdala component, and it carries **no SLEA
    warning**.
*   **No ``AREA_PATHS`` hop.** The left container is a local sub-container
    under cranial_nerve_nuclei, not a cross-listed container.
*   **No nested cross-listing.** The left container has no nested
    dual-framing module. It is a single bilateral sub-container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei import left

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.left"
    )

**Do not** assume the left container is a **leaf**. It is a
**container** — its structural children are the **six left-side nuclei**.

**Do not** assume the left container is the **whole cranial_nerve_nuclei
container**. It is the **left-side half only** — the right side is a
**separate structural sibling**.

**Do not** assume the left container is the **right container**. The two
are a **strict mirror pair with NO warning at the container level** — any
lateralization is documented **inside the individual nucleus modules**.

**Do not** assume the left container is the **left cranial nerves V, VI,
VII, VIII**. The **nerves** are the **white-matter axon bundles**; the
**nuclei** are the **grey-matter neuron clusters**. They are **different
structures**.

**Do not** assume the left container is the **whole left brainstem** or
the **whole left cranial-nerve system**. It is **only the left pontine
subset** — the **left midbrain** and **left medullary** cranial-nerve
nuclei are **wired elsewhere**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the left container. **The left container is SLEA-FREE**
and **amygdala-agnostic**.

Iterating the left container's structural children (recommended consumer
pattern)::

    LEFT_CRANIAL_NERVE_NUCLEI_CHILDREN = (
        "abducens_nucleus",
        "chief_sensory_trigeminal_nucleus",
        "facial_nerve_nucleus",
        "motor_trigeminal_nucleus",
        "superior_salivatory_nucleus",
        "vestibulocochlear_nuclei",
    )
    # The left container is the LEFT HALF of the cranial_nerve_nuclei.
    # The left vestibulocochlear nuclei is itself a sub-container with
    # left cochlear nuclei and left vestibular nuclei as its children.

Iterating the left container's nuclei (recommended consumer pattern)::

    for nucleus in LEFT_CRANIAL_NERVE_NUCLEI_CHILDREN:
        nucleus_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.left."
            f"{nucleus}"
        )
        # resolve nucleus_path through the memory/recall layer

Reaching the left vestibulocochlear nuclei's sub-children (recommended
consumer pattern — the sub-container)::

    for sub in ("cochlear_nuclei", "vestibular_nuclei"):
        sub_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.left."
            f"vestibulocochlear_nuclei.{sub}"
        )
        # resolve sub_path through the memory/recall layer

Reaching the right container (recommended consumer pattern — the strict
mirror)::

    # The right container is the structurally identical RIGHT half:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.right
    #
    # The left and right containers are a STRICT MIRROR PAIR with NO
    # warning at the container level.

Reaching the left midbrain cranial-nerve nuclei (recommended consumer
pattern — NOTE the brainstem-level boundary)::

    # The left midbrain hosts left CN III, IV, mesencephalic V,
    # Edinger-Westphal:
    #
    #   hindbrain.midbrain.cranial_nerve_nuclei.left
    #
    # The left container is only the LEFT PONTINE subset.

Reaching the left medullary cranial-nerve nuclei (recommended consumer
pattern — NOTE the brainstem-level boundary)::

    # The left medulla hosts left CN IX, X, XI, XII, inferior salivatory,
    # nucleus ambiguus, hypoglossal, dorsal motor vagus, solitary:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left
    #
    # The left container is only the LEFT PONTINE subset.

Reaching the left cerebellum (recommended consumer pattern — NOTE the
metencephalic-sibling boundary)::

    # The left cerebellum is the left metencephalic cerebellar half — it
    # has its own nuclei (left dentate, left fastigial, left interposed):
    #
    #   hindbrain.metencephalon.cerebellum.hemispheres.left
    #
    # The left container is the LEFT PONTINE nuclear collection, not the
    # left cerebellum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cnn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.{side}"
        )
        # resolve cnn_path through the memory/recall layer

Left cranial-nerve-specific detail (not wired — consult references)::

    # The six left-side nuclei and their functions:
    #   left abducens_nucleus           -> left CN VI, left lateral rectus
    #   left facial_nerve_nucleus       -> left CN VII, left facial expression
    #   left motor_trigeminal_nucleus   -> left CN V, left mastication
    #   left chief_sensory_trigeminal_nucleus -> left CN V, left discriminative touch
    #   left superior_salivatory_nucleus -> left CN VII, left lacrimal/salivary glands
    #   left vestibulocochlear_nuclei   -> left CN VIII, left hearing (cochlear) + left balance (vestibular)
    #
    # Do not attempt to resolve these as anything other than structural
    # children of the left container.

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Left pontine
    cranial-nerve nuclei in overview.)
*   **Cranial nerve nuclei — general:** Haines, D.E. (2012).
    *Neuroanatomy: An Atlas of Structures, Sections, and Systems*, 8th
    ed. (Left cranial-nerve nuclei of the pons.)
*   **Trigeminal system:** Usunoff, K.G., Marani, E., Schoen, J.H.R.
    (2006). "The trigeminal system." *Advances in Anatomy, Embryology,
    and Cell Biology* 184:1–146. (Left chief sensory trigeminal nucleus
    and the left trigeminal nuclear complex across brainstem levels.)
*   **Facial nerve and nucleus:** May, M., Schaitkin, B.M. (2000). *The
    Facial Nerve*, 2nd ed. (Left facial nerve nucleus and the left
    facial motor system.)
*   **Abducens nucleus and sixth nerve palsy:** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (Left abducens
    nucleus and left lateral rectus control.)
*   **Vestibulocochlear system:** Kandel, E.R., Schwartz, J.H., Jessell,
    T.M., Siegelbaum, S.A., Hudspeth, A.J. (2013). *Principles of Neural
    Science*, 5th ed. (Left cochlear and left vestibular nuclei —
    left hearing and left balance.)
*   **Superior salivatory nucleus:** Loewy, A.D., Spyer, K.M. (1990).
    *Central Regulation of Autonomic Functions*. (Left superior
    salivatory nucleus and the left parasympathetic outflow of left
    CN VII.)
*   **Cranial-nerve nuclei across brainstem levels (contrast — the left
    midbrain and left medullary nuclei are wired elsewhere):**
    Nieuwenhuys, R., Voogd, J., van Huijzen, C. (2008). *The Human
    Central Nervous System: A Synopsis and Atlas*, 4th ed. (Left
    cranial-nerve nuclei of the midbrain, pons, and medulla.)
*   **Trigeminal ganglion (contrast — the left peripheral ganglion):**
    Standring, S. (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Left trigeminal ganglion and the left
    peripheral trigeminal system.)
*   **Cerebellar nuclei (contrast — the left metencephalic sibling):**
    Manto, M., Gruol, D.L., Schmahmann, J.D., Koibuchi, N., Rossi, F.
    (eds.) (2013). *Handbook of the Cerebellum and Cerebellar
    Disorders*. (Left cerebellar nuclei — left dentate, left fastigial,
    left interposed.)
*   **Solitary nucleus (contrast — the left medullary visceral-afferent
    hub):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Left solitary nucleus and the
    left medullary visceral-afferent system.)
*   **SLEA (contrast — the left container is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the left container.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the left container.)
*   NeuroNames — Cranial nerve nuclei (pons, left); FMA — Left cranial
    nerve nuclei of the pons.
"""