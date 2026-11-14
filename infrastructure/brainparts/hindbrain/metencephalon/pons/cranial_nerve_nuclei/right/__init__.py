"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.right
=================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── right   <-- THIS MODULE
                    ├── abducens_nucleus
                    ├── chief_sensory_trigeminal_nucleus
                    ├── facial_nerve_nucleus
                    ├── motor_trigeminal_nucleus
                    ├── superior_salivatory_nucleus
                    └── vestibulocochlear_nuclei
                        ├── cochlear_nuclei
                        └── vestibular_nuclei

**Primary synonym:** Right pontine cranial-nerve nuclei; right cranial-nerve
nuclei of the pons; right metencephalic cranial-nerve nuclei; "the right
pontine CN V–VIII subset."
**Cytoarchitectonic designation:** **Not a Brodmann area** — a **bilateral
sub-container** of **brainstem grey-matter nuclei**. A **heterogeneous
collection** of **six right-side cranial-nerve nuclei** in the **right
pontine tegmentum** — **motor** (`abducens_nucleus`,
`facial_nerve_nucleus`, `motor_trigeminal_nucleus`), **general sensory**
(`chief_sensory_trigeminal_nucleus`), **parasympathetic**
(`superior_salivatory_nucleus`), and **special sensory**
(`vestibulocochlear_nuclei`, comprising `cochlear_nuclei` and
`vestibular_nuclei`).
**Part of:** The **cranial_nerve_nuclei** container — specifically, the
**right bilateral half** of the pontine cranial-nerve nuclear collection.
The **cranial_nerve_nuclei** container is the **pontine** cranial-nerve
nuclear collection; the **right** container is its **right-side structural
child**.
**Structural parent:** ``.../cranial_nerve_nuclei/`` → **direct child** of
the cranial_nerve_nuclei container.
**Structural children:** **Six right-side cranial-nerve nuclei**:
``abducens_nucleus``, ``chief_sensory_trigeminal_nucleus``,
``facial_nerve_nucleus``, ``motor_trigeminal_nucleus``,
``superior_salivatory_nucleus``, and ``vestibulocochlear_nuclei`` (itself
a **sub-container** with ``cochlear_nuclei`` and ``vestibular_nuclei``).
**Boundary status (RIGHT HALF — NOT the whole cranial_nerve_nuclei
container):** **Boundary case — the right container is the RIGHT HALF of
the cranial_nerve_nuclei, NOT the whole container.** The
**cranial_nerve_nuclei** container (``.../cranial_nerve_nuclei/``) has
**two structural children** — ``left`` and ``right``. The **right**
container (here) is the **right-side** half only. Consumers must **not**
conflate the right container with the **whole cranial_nerve_nuclei
collection** — the left side is a **separate structural sibling**.
**Boundary status (NOT the left container — strict mirror, no warning):**
**Boundary case — the right container is NOT the left container; the two
are a STRICT MIRROR PAIR with NO warning at the container level.** The
**left** container (``.../cranial_nerve_nuclei/left/``) is the
**structurally identical** left-side counterpart — same six nuclei, same
leaf status for each nucleus, same bilateral framing. The two sides are
**strictly mirrored** — any lateralization is documented **inside the
individual nucleus modules**, not at the container level. Consumers must
**not** import a lateralization warning into the right container — there
is **none at the container level**.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the right
container is a CONTAINER, not a leaf.** It has **six structural
children** (the six right-side cranial-nerve nuclei). The
**vestibulocochlear_nuclei** is itself a **sub-container** with
**cochlear_nuclei** and **vestibular_nuclei** as its children. Consumers
must **not** treat the right container as a leaf, and must **not** assume
the six nuclei are absent — they are its **direct structural children**.
**Boundary status (GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS):**
**Boundary case — the right container holds the GREY-MATTER NUCLEI, NOT
the cranial-nerve FIBERS (axons).** The **cranial nerves** (right CN V,
VI, VII, VIII) are the **white-matter axon bundles** that **leave** the
right pontine tegmentum and **travel** to the periphery. The **right
container** (here) holds the **grey-matter neuron clusters** that **give
rise to** (motor, parasympathetic) or **receive** (sensory, special
sensory) those axons. They are **DIFFERENT STRUCTURES** — the **nuclei**
are grey matter; the **nerves** are white matter. Consumers must **not**
conflate the **right nuclei** with the **right cranial nerves**.
**Boundary status (NOT the whole pons — the pons is the grandparent):**
**Boundary case — the right container is NOT the pons; the pons is the
grandparent.** The **pons** (``.../pons/``) is the **whole metencephalic
brainstem segment** — it contains the **basilar pons**, the **pontine
tegmentum**, the **pontine nuclei**, the **corticospinal/corticobulbar
tracts**, the **middle cerebellar peduncle**, and the
**cranial_nerve_nuclei** (both left and right). The **right container**
(here) is the **right-side cranial-nerve nuclei only**. Consumers must
**not** conflate the right container with the **whole pons**.
**Boundary status (NOT midbrain or medullary cranial-nerve nuclei — those
are DIFFERENT BRAINSTEM LEVELS):** **Boundary case — the right container
is NOT the midbrain or medullary cranial-nerve nuclei.** The **midbrain**
(``.../midbrain/cranial_nerve_nuclei/``) hosts **CN III, IV,
mesencephalic V, Edinger-Westphal**; the **medulla oblongata**
(``.../medulla_oblongata/cranial_nerve_nuclei/``) hosts **CN IX, X, XI,
XII, inferior salivatory, nucleus ambiguus, hypoglossal, dorsal motor
vagus, solitary**. The **right container** (here) is the **right pontine
subset only** — **CN V (chief sensory + motor), CN VI, CN VII (facial +
superior salivatory), CN VIII (cochlear + vestibular)**. Consumers must
**not** conflate the right pontine nuclei with the midbrain or medullary
cranial-nerve nuclei.
**Boundary status (NOT the whole trigeminal complex — the trigeminal
system spans levels):** **Boundary case — the right container does NOT
contain the whole right trigeminal nuclear complex.** The **right
trigeminal system** has **three** brainstem nuclei: the **right
mesencephalic trigeminal nucleus** (midbrain — proprioception), the
**right chief sensory trigeminal nucleus** (pons — discriminative touch,
**in this container**), and the **right spinal trigeminal nucleus**
(medulla/pons junction — pain/temperature). The **right container**
(here) contains **only the right chief sensory trigeminal nucleus** and
the **right motor trigeminal nucleus** — it does **not** contain the
right mesencephalic or spinal trigeminal nuclei. Consumers must **not**
conflate the right pontine trigeminal nuclei with the **whole right
trigeminal complex**.
**Boundary status (NOT the trigeminal ganglion or any sensory ganglion —
those are PERIPHERAL):** **Boundary case — the right container is NOT the
right trigeminal ganglion (or any right sensory ganglion).** The **right
trigeminal ganglion** (right semilunar / Gasserian ganglion) is a
**peripheral sensory ganglion** outside the brainstem containing the
**right primary sensory neuron cell bodies** for the right trigeminal
nerve. The **right container** (here) holds the **right central
grey-matter nuclei** inside the right pontine tegmentum. They are
**DIFFERENT STRUCTURES** — the **ganglion** is peripheral; the **nuclei**
are central. Consumers must **not** conflate the **right central nuclei**
with the **right peripheral ganglion**.
**Boundary status (NOT the cerebellum — that is the metencephalic
sibling):** **Boundary case — the right container is NOT the right
cerebellum.** The **right cerebellum**
(``.../metencephalon/cerebellum/hemispheres/right/``) is the **right
metencephalic cerebellar half**, with its **own nuclei** (right dentate,
right fastigial, right interposed: right emboliform + right globose) and
its **own cortex**. The **right container** (here) holds the **right
pontine cranial-nerve nuclei**, not the right cerebellar nuclei.
Consumers must **not** conflate the **right pontine cranial-nerve
nuclei** with the **right cerebellar nuclei**.
**Boundary status (NOT locus coeruleus, parabrachial area, pontine
nuclei, or other right pontine structures):** **Boundary case — the
right container is NOT the right locus coeruleus, the right parabrachial
area, the right pontine nuclei, or other right pontine structures.** The
**right locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) is
the **noradrenergic** nucleus; the **right parabrachial area**
(``.../pons/parabrachial_area/``) is the **visceral/autonomic relay**;
the **right pontine nuclei** (``.../pons/pontine_nuclei/right/``) are the
**cortico-ponto-cerebellar relay** in the **right basilar pons**. None of
these are **right cranial-nerve nuclei**. The **right container** (here)
is **only** the right nuclei that **give rise to or receive** the
**right cranial nerves V, VI, VII, VIII**. Consumers must **not**
conflate the right cranial-nerve nuclei with **other right pontine
nuclei**.
**Boundary status (NOT the solitary nucleus — that is the medullary
visceral-afferent hub):** **Boundary case — the right container is NOT
the right solitary nucleus.** The **right solitary nucleus** (right
nucleus tractus solitarius,
``.../medulla_oblongata/solitary_nucleus/right/``) is the **right
medullary visceral-afferent hub** for **right CN VII, IX, X** (taste,
visceral sensation, baroreception, respiratory chemoreception). The
**right container** (here) contains the **right superior salivatory
nucleus** (right CN VII parasympathetic), but it does **not** contain the
**right solitary nucleus**. Consumers must **not** conflate the right
pontine nuclei with the **right solitary nucleus**.
**Boundary status (NOT a single functional system — MULTIPLE nuclei with
DIFFERENT functions):** **Boundary case — the right container is a
HETEROGENEOUS collection of six right-side nuclei with DIFFERENT
functions, not a single uniform system.** The collection includes:
*   **Right abducens nucleus (CN VI)** — **somatic motor**; controls the
    **right lateral rectus** muscle (right eye abduction).
*   **Right facial nerve nucleus (CN VII)** — **branchial motor**;
    controls the **right muscles of facial expression**.
*   **Right motor trigeminal nucleus (CN V)** — **branchial motor**;
    controls the **right muscles of mastication**.
*   **Right chief sensory trigeminal nucleus (CN V)** — **general
    sensory**; **discriminative touch** from the **right face**.
*   **Right superior salivatory nucleus (CN VII)** — **parasympathetic**;
    controls the **right lacrimal** and **right salivary** glands.
*   **Right vestibulocochlear nuclei (CN VIII)** — **special sensory**;
    **right cochlear nuclei** subserve **right hearing**; **right
    vestibular nuclei** subserve **right balance and spatial
    orientation**.
**Each nucleus is functionally distinct** — the tree wires them as
**separate structural children under the right container**. Consumers
must **not** treat the right container as a single uniform nucleus — it
is a **distributed collection** of functionally distinct right-side
nuclei.

Overview
--------
The right container is the **right-side half** of the pontine
cranial-nerve nuclear collection — the **six grey-matter nuclei** in the
**right pontine tegmentum** that **give rise to** (motor,
parasympathetic) or **receive** (sensory, special sensory) the **right
cranial nerves V, VI, VII, and VIII**. It is a **container** under the
cranial_nerve_nuclei container, with **six structural children** (six
right-side nuclei), one of which (the **vestibulocochlear_nuclei**) is
itself a **sub-container**.

**The right container is a CONTAINER, NOT a leaf.** Its structural
children are the **six right-side nuclei**. The **right
vestibulocochlear_nuclei** is itself a **sub-container** with **right
cochlear_nuclei** and **right vestibular_nuclei** as its children.

**The right container is the RIGHT HALF of the cranial_nerve_nuclei, NOT
the whole container.** The **cranial_nerve_nuclei** container has **two
structural children** — ``left`` and ``right``. The **right** container
(here) is the **right-side** half only. The left side is a **separate
structural sibling**.

**The right container and the left container are a STRICT MIRROR PAIR
with NO warning at the container level.** The two sides are
**structurally identical** — same six nuclei, same leaf status for each
nucleus, same bilateral framing. Any lateralization is documented
**inside the individual nucleus modules**, not at the container level.

**The right container holds the GREY-MATTER NUCLEI, NOT the cranial-nerve
FIBERS.** The **right cranial nerves V, VI, VII, VIII** are the
**white-matter axon bundles** that **travel** to and from the periphery.
The **right container** (here) holds the **grey-matter neuron clusters**
inside the right pontine tegmentum. They are **DIFFERENT STRUCTURES** —
the **nuclei** are grey matter; the **nerves** are white matter.

**The right container is NOT the whole right trigeminal complex.** The
**right trigeminal system** spans three brainstem levels — the **right
mesencephalic trigeminal nucleus** (midbrain), the **right chief sensory
trigeminal nucleus** (pons, **in this container**), and the **right
spinal trigeminal nucleus** (medulla/pons junction). The **right
container** contains **only the pontine trigeminal components** (chief
sensory + motor).

**The right container is HETEROGENEOUS.** The six right-side nuclei are
**functionally distinct** — **motor** (right abducens, right facial,
right motor trigeminal), **general sensory** (right chief sensory
trigeminal), **parasympathetic** (right superior salivatory), and
**special sensory** (right vestibulocochlear). The tree wires them as
**separate structural children under the right container**.

Nucleus Composition (structural children, prose)
------------------------------------------------
The right container contains **six right-side nuclei**, documented as
**structural children** (not as leaves of the container):

*   **Right abducens nucleus**
    (``.../cranial_nerve_nuclei/right/abducens_nucleus/``) — **somatic
    motor**; controls the **right lateral rectus** muscle (right eye
    abduction). CN VI.

*   **Right chief sensory trigeminal nucleus**
    (``.../cranial_nerve_nuclei/right/chief_sensory_trigeminal_nucleus/``)
    — **general sensory**; **discriminative touch** from the **right
    face**. CN V (principal sensory nucleus).

*   **Right facial nerve nucleus**
    (``.../cranial_nerve_nuclei/right/facial_nerve_nucleus/``) —
    **branchial motor**; controls the **right muscles of facial
    expression**. CN VII.

*   **Right motor trigeminal nucleus**
    (``.../cranial_nerve_nuclei/right/motor_trigeminal_nucleus/``) —
    **branchial motor**; controls the **right muscles of mastication**.
    CN V.

*   **Right superior salivatory nucleus**
    (``.../cranial_nerve_nuclei/right/superior_salivatory_nucleus/``) —
    **parasympathetic**; controls the **right lacrimal** and **right
    salivary** glands. CN VII.

*   **Right vestibulocochlear nuclei**
    (``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/``) —
    **special sensory**; a **sub-container** with two children:
    *   **Right cochlear nuclei** — **right hearing** (right CN VIII
        cochlear division).
    *   **Right vestibular nuclei** — **right balance and spatial
        orientation** (right CN VIII vestibular division).

**These nuclei are structural children of the right container.** The
right container's **structural children** are the **six right-side
nuclei**; the **right vestibulocochlear nuclei** is a **sub-container**
with two of its own children. Consumers resolving nucleus-level detail
go **through** the right container, and resolving cochlear/vestibular
detail goes **through** the right vestibulocochlear nuclei.

The Right / Left Boundary
-------------------------
This is the **strict-mirror** boundary:

*   **Right container** (this module) — the **right-side** pontine
    cranial-nerve nuclei.

*   **Left container** (``.../cranial_nerve_nuclei/left/``) — the
    **structurally identical** left-side pontine cranial-nerve nuclei.

**They are a STRICT MIRROR PAIR with NO warning at the container level.**
The two sides are **structurally identical** — same six nuclei, same leaf
status for each nucleus, same bilateral framing. Any lateralization is
documented **inside the individual nucleus modules**, not at the container
level. Consumers must **not** import a lateralization warning into the
right container.

The Right Container / Cranial Nerve Nuclei Container Boundary
-------------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Right container** (this module) — the **right-side** half of the
    pontine cranial-nerve nuclear collection.

*   **Cranial_nerve_nuclei container** (``.../cranial_nerve_nuclei/``)
    — the **whole pontine collection**, with **two structural children**
    (``left`` and ``right``).

**The right container is a child of the cranial_nerve_nuclei container.**
Consumers must **not** conflate the right half with the **whole pontine
collection** — the left side is a **separate structural sibling**.

The Right Container / Cranial Nerves Boundary
---------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Right container** (this module) — the **right-side grey-matter
    neuron clusters** in the right pontine tegmentum.

*   **Right cranial nerves V, VI, VII, VIII** — the **right white-matter
    axon bundles** that travel to and from the periphery.

**They are DIFFERENT STRUCTURES.** The **right nuclei** are the **right
central neuronal sources/targets**; the **right nerves** are the **right
peripheral conduction infrastructure**. Consumers must **not** conflate
the two.

The Right Container / Pons Boundary
-----------------------------------
This is the **great-grandchild vs. grandparent** boundary:

*   **Right container** (this module) — the **right-side tegmental
    grey-matter nuclei** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal/
    corticobulbar tracts**, the **middle cerebellar peduncle**, and the
    **cranial-nerve nuclei** (both left and right).

**The right container is a great-grandchild of the pons** (via
cranial_nerve_nuclei). Consumers must **not** conflate the right
cranial-nerve nuclei with the **whole pons**.

The Right Container / Midbrain and Medullary Cranial-Nerve Nuclei Boundary
--------------------------------------------------------------------------
This is the **brainstem-level** boundary:

*   **Right container** (this module) — the **right pontine** nuclei only
    — **right CN V (chief sensory + motor)**, **right CN VI**, **right
    CN VII (facial + superior salivatory)**, **right CN VIII (cochlear +
    vestibular)**.

*   **Right midbrain cranial-nerve nuclei**
    (``.../midbrain/cranial_nerve_nuclei/right/``) — **right CN III
    (oculomotor)**, **right CN IV (trochlear)**, **right mesencephalic
    trigeminal nucleus (right CN V proprioceptive)**, **right
    Edinger-Westphal nucleus (right CN III parasympathetic)**.

*   **Right medullary cranial-nerve nuclei**
    (``.../medulla_oblongata/cranial_nerve_nuclei/right/``) — **right CN
    IX (glossopharyngeal)**, **right CN X (vagus)**, **right CN XI
    (accessory)**, **right CN XII (hypoglossal)**, **right inferior
    salivatory nucleus**, **right nucleus ambiguus**, **right
    hypoglossal nucleus**, **right dorsal motor nucleus of the vagus**,
    **right solitary nucleus**.

**They are DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate
the **right pontine** cranial-nerve nuclei with the **right midbrain** or
**right medullary** cranial-nerve nuclei.

The Right Container / Trigeminal Complex Boundary
-------------------------------------------------
This is the **partial-complex** boundary:

*   **Right container** (this module) — contains **only** the **right
    chief sensory trigeminal nucleus** (discriminative touch) and the
    **right motor trigeminal nucleus** (mastication).

*   **Right mesencephalic trigeminal nucleus**
    (``.../midbrain/tegmentum/mesencephalic_trigeminal_nucleus/right/``)
    — **right proprioception** (right CN V mesencephalic division).

*   **Right spinal trigeminal nucleus**
    (``.../medulla_oblongata/spinal_trigeminal_nucleus/right/``) —
    **right pain and temperature** (right CN V spinal division).

**The right trigeminal nuclear complex spans three brainstem levels.**
The **right container** contains **only the right pontine components**.
Consumers must **not** conflate the right pontine trigeminal nuclei with
the **whole right trigeminal complex**.

The Right Container / Right Cerebellum Boundary
-----------------------------------------------
This is the **metencephalic-sibling** boundary:

*   **Right container** (this module) — the **right pontine**
    cranial-nerve nuclei.

*   **Right cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/right/``) — the **right
    metencephalic cerebellar half**, with its **own nuclei** (right
    dentate, right fastigial, right interposed: right emboliform + right
    globose) and its **own cortex**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
**right pontine cranial-nerve nuclei** with the **right cerebellar
nuclei**.

The Right Container / Other Right Pontine Structures Boundary
-------------------------------------------------------------
This is the **non-cranial-nerve right pontine** boundary:

*   **Right container** (this module) — **only** the right nuclei that
    **give rise to or receive** the **right cranial nerves V, VI, VII,
    VIII**.

*   **Right locus coeruleus**
    (``.../pons/tegmentum/locus_coeruleus/``) — the **right
    noradrenergic** nucleus.

*   **Right parabrachial area** (``.../pons/parabrachial_area/``) — the
    **right visceral/autonomic relay**.

*   **Right pontine nuclei** (``.../pons/pontine_nuclei/right/``) — the
    **right cortico-ponto-cerebellar relay** in the **right basilar
    pons**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
right cranial-nerve nuclei with **other right pontine nuclei**.

The Right Container / Right Solitary Nucleus Boundary
-----------------------------------------------------
This is the **visceral-afferent** boundary:

*   **Right container** (this module) — contains the **right superior
    salivatory nucleus** (right CN VII parasympathetic), but **not** the
    **right solitary nucleus**.

*   **Right solitary nucleus**
    (``.../medulla_oblongata/solitary_nucleus/right/``) — the **right
    medullary visceral-afferent hub** for **right CN VII, IX, X** (taste,
    visceral sensation, baroreception, respiratory chemoreception).

**The right solitary nucleus is medullary, not pontine.** Consumers must
**not** conflate the right pontine nuclei with the **right solitary
nucleus**.

Function in the Human Brain
---------------------------
The right container's functions are **the right cranial-nerve
sensorimotor and parasympathetic relay** — **NOT a single unified
function**:

*   **Somatic Motor (Right Abducens Nucleus, right CN VI):** Controls the
    **right lateral rectus** muscle — **right eye abduction**. The right
    abducens nucleus is the **sole source** of the right lateral rectus
    motor innervation.

*   **Branchial Motor (Right Facial Nerve Nucleus, right CN VII):**
    Controls the **right muscles of facial expression** — the right
    facial nerve is the **principal right motor nerve of the face**.

*   **Branchial Motor (Right Motor Trigeminal Nucleus, right CN V):**
    Controls the **right muscles of mastication** — the right motor
    trigeminal nucleus is the **sole source** of the right motor
    trigeminal innervation.

*   **General Sensory (Right Chief Sensory Trigeminal Nucleus, right CN
    V):** **Discriminative touch** from the **right face** — the right
    principal sensory nucleus is the **right pontine** component of the
    right trigeminal nuclear complex.

*   **Parasympathetic (Right Superior Salivatory Nucleus, right CN VII):**
    Controls the **right lacrimal** and **right salivary** glands — the
    right superior salivatory nucleus is the **right preganglionic
    parasympathetic** source for the right facial nerve's autonomic
    component.

*   **Special Sensory (Right Vestibulocochlear Nuclei, right CN VIII):**
    The **right cochlear nuclei** subserve **right hearing**; the
    **right vestibular nuclei** subserve **right balance and spatial
    orientation**. The right vestibulocochlear nuclei are the **right
    brainstem relay** for the right auditory and vestibular senses.

**The unifying theme:** the right container is the **right pontine
cranial-nerve nuclear collection** — the **right grey-matter nuclei**
that **give rise to or receive** the **right cranial nerves V, VI, VII,
VIII**. It is **heterogeneous** and **strictly mirrored** — the six
right-side nuclei are **functionally distinct**, and they are
**structural children** of the right container.

Associated Disorders
--------------------
The right container has **no single named clinical syndrome as a
collection** — its clinical associations are **right-nucleus-specific**:

*   **Right Abducens Nucleus (right CN VI) — Right Sixth Nerve Palsy:**
    Lesions cause **right lateral rectus palsy** — **inability to abduct
    the right eye**, **diplopia** on right lateral gaze.

*   **Right Facial Nerve Nucleus (right CN VII) — Right Facial Nerve
    Palsy (right Bell's Palsy, right Supranuclear Palsy):** Lesions
    cause **ipsilateral (right) facial weakness** — **inability to close
    the right eye**, **right facial droop**, **loss of right forehead
    wrinkling** (peripheral lesions) versus **right forehead sparing**
    (supranuclear lesions).

*   **Right Motor Trigeminal Nucleus (right CN V) — Right Trigeminal
    Motor Palsy:** Lesions cause **weakness of right mastication** —
    **jaw deviation** toward the **right** side.

*   **Right Chief Sensory Trigeminal Nucleus (right CN V) — Right
    Trigeminal Sensory Loss:** Lesions cause **right facial sensory
    loss** — **discriminative touch** impairment on the **right face**.

*   **Right Superior Salivatory Nucleus (right CN VII) — Right Autonomic
    Facial Palsy:** Lesions cause **reduced right lacrimation** and
    **reduced right salivation**.

*   **Right Vestibulocochlear Nuclei (right CN VIII) — Right
    Vestibulocochlear Disorders:** Lesions cause **right hearing loss**
    (right cochlear nuclei) and **right vertigo / right nystagmus /
    right imbalance** (right vestibular nuclei).

*   **No Named "Right Cranial Nerve Nuclei Syndrome":** The right
    container is a **heterogeneous collection**, not a **single
    structure** — it has **no named clinical syndrome as a collection**.
    Its clinical relevance is **right-nucleus-specific**, via the
    **individual right cranial-nerve nuclei** and the **right cranial
    nerves** they subserve.

**What is NOT here:** The right container is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala), **fear conditioning** (amygdala —
central nucleus + basolateral nuclei), **Urbach-Wiethe disease**
(amygdala — basolateral nuclei), **Alzheimer's disease** (hippocampus,
nucleus basalis), or **Parkinson's disease** (substantia nigra). Its
clinical relevance is **right-cranial-nerve-specific**, via the
**individual right nuclei** and the **right cranial nerves** they
subserve. **No named right cranial_nerve_nuclei syndrome exists as a
collection.**

Lateralization Notes
--------------------
This is the **right** container of the cranial_nerve_nuclei. The right
container is **bilaterally symmetric** with the left container and
**strictly mirrored** — and it carries **NO warning at the container
level**:

*   **Strict Bilateral Symmetry:** The **right** and **left**
    containers are **structurally identical** — same six nuclei under
    each, same leaf status for each nucleus, same bilateral framing. The
    bilateral symmetry is **strict**.

*   **Lateralization is Nucleus-Specific (Contested, Documented in the
    Nucleus Modules):** Any functional lateralization (e.g. right facial
    motor control, right vestibular asymmetry, right auditory
    lateralization) is documented **inside the individual right nucleus
    modules**, not at the container level. Consumers must **not** assume
    a container-level lateralization — the right container is a
    **strict-mirror right half**.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The right
    container is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the right container.

*   **NO Amygdala-Lateralization Warning of their own (the right
    container is MODULATORY-AGNOSTIC, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The right container is a
    **right cranial-nerve nuclear collection** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**. The
    **right container** is **SLEA-free** and **amygdala-agnostic**.

**A consumer that assumes "right container = left container" will be
structurally correct** — the two sides are **strictly symmetric** (any
lateralization is documented in the nucleus modules). The right container
is a **strict-mirror pair with NO warning at the container level** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right container is the **right
    half**; it does **not** import the left container at module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../medulla_oblongata/``,
    ``.../metencephalon/cerebellum/``, or any other container. The right
    container's relationships to the **right midbrain** and **right
    medullary** cranial-nerve nuclei, the **right cerebellum**, the
    **right locus coeruleus**, the **right parabrachial area**, and the
    **right pontine nuclei** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children are the SIX right-side
    nuclei.** The **right vestibulocochlear nuclei** is itself a
    **sub-container** with **right cochlear nuclei** and **right
    vestibular nuclei** as its children.
*   **RIGHT HALF — NOT the whole cranial_nerve_nuclei container.** The
    **cranial_nerve_nuclei** container has **two structural children** —
    ``left`` and ``right``. The **right** container (here) is the
    **right-side** half only.
*   **STRICT MIRROR with the left container — NO warning at the
    container level.** The **right** and **left** containers are
    **structurally identical**. Any lateralization is documented **inside
    the individual nucleus modules**.
*   **GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS.** The **right
    nuclei** are the **grey-matter neuron clusters**; the **right cranial
    nerves V, VI, VII, VIII** are the **white-matter axon bundles**.
    Consumers must **not** conflate the two.
*   **NOT the whole brainstem or the whole right cranial-nerve system —
    only the RIGHT PONTINE subset.** The **right midbrain** and **right
    medullary** cranial-nerve nuclei are **wired elsewhere**.
*   **NOT a single functional system — MULTIPLE right-side nuclei.** The
    **right abducens nucleus**, **right facial nerve nucleus**, **right
    motor trigeminal nucleus**, **right chief sensory trigeminal
    nucleus**, **right superior salivatory nucleus**, and **right
    vestibulocochlear nuclei** are **functionally distinct**.
*   **NOT the right mesencephalic or right spinal trigeminal nucleus —
    the right trigeminal system spans levels.** The **right container**
    contains **only the right pontine trigeminal components** (chief
    sensory + motor).
*   **NOT the right trigeminal ganglion or any right sensory ganglion —
    those are PERIPHERAL.** The **right nuclei** are **central**; the
    **right ganglia** are **peripheral**.
*   **NOT the right cerebellum — that is the metencephalic sibling.** The
    **right cerebellar nuclei** (right dentate, right fastigial, right
    interposed) are **wired elsewhere**.
*   **NOT the right solitary nucleus — that is the right medullary
    visceral-afferent hub.** The **right superior salivatory nucleus** is
    here, but the **right solitary nucleus** is not.
*   **SLEA-FREE — no extended-amygdala relationship.** The right
    container is **not** an extended-amygdala component, and it carries
    **no SLEA warning**.
*   **No ``AREA_PATHS`` hop.** The right container is a local
    sub-container under cranial_nerve_nuclei, not a cross-listed
    container.
*   **No nested cross-listing.** The right container has no nested
    dual-framing module. It is a single bilateral sub-container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei import right

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.right"
    )

**Do not** assume the right container is a **leaf**. It is a
**container** — its structural children are the **six right-side
nuclei**.

**Do not** assume the right container is the **whole cranial_nerve_nuclei
container**. It is the **right-side half only** — the left side is a
**separate structural sibling**.

**Do not** assume the right container is the **left container**. The two
are a **strict mirror pair with NO warning at the container level** — any
lateralization is documented **inside the individual nucleus modules**.

**Do not** assume the right container is the **right cranial nerves V,
VI, VII, VIII**. The **nerves** are the **white-matter axon bundles**;
the **nuclei** are the **grey-matter neuron clusters**. They are
**different structures**.

**Do not** assume the right container is the **whole right brainstem** or
the **whole right cranial-nerve system**. It is **only the right pontine
subset** — the **right midbrain** and **right medullary** cranial-nerve
nuclei are **wired elsewhere**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the right container. **The right container is SLEA-FREE**
and **amygdala-agnostic**.

Iterating the right container's structural children (recommended
consumer pattern)::

    RIGHT_CRANIAL_NERVE_NUCLEI_CHILDREN = (
        "abducens_nucleus",
        "chief_sensory_trigeminal_nucleus",
        "facial_nerve_nucleus",
        "motor_trigeminal_nucleus",
        "superior_salivatory_nucleus",
        "vestibulocochlear_nuclei",
    )
    # The right container is the RIGHT HALF of the cranial_nerve_nuclei.
    # The right vestibulocochlear nuclei is itself a sub-container with
    # right cochlear nuclei and right vestibular nuclei as its children.

Iterating the right container's nuclei (recommended consumer pattern)::

    for nucleus in RIGHT_CRANIAL_NERVE_NUCLEI_CHILDREN:
        nucleus_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.right."
            f"{nucleus}"
        )
        # resolve nucleus_path through the memory/recall layer

Reaching the right vestibulocochlear nuclei's sub-children (recommended
consumer pattern — the sub-container)::

    for sub in ("cochlear_nuclei", "vestibular_nuclei"):
        sub_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.right."
            f"vestibulocochlear_nuclei.{sub}"
        )
        # resolve sub_path through the memory/recall layer

Reaching the left container (recommended consumer pattern — the strict
mirror)::

    # The left container is the structurally identical LEFT half:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left
    #
    # The right and left containers are a STRICT MIRROR PAIR with NO
    # warning at the container level.

Reaching the right midbrain cranial-nerve nuclei (recommended consumer
pattern — NOTE the brainstem-level boundary)::

    # The right midbrain hosts right CN III, IV, mesencephalic V,
    # Edinger-Westphal:
    #
    #   hindbrain.midbrain.cranial_nerve_nuclei.right
    #
    # The right container is only the RIGHT PONTINE subset.

Reaching the right medullary cranial-nerve nuclei (recommended consumer
pattern — NOTE the brainstem-level boundary)::

    # The right medulla hosts right CN IX, X, XI, XII, inferior
    # salivatory, nucleus ambiguus, hypoglossal, dorsal motor vagus,
    # solitary:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right
    #
    # The right container is only the RIGHT PONTINE subset.

Reaching the right cerebellum (recommended consumer pattern — NOTE the
metencephalic-sibling boundary)::

    # The right cerebellum is the right metencephalic cerebellar half —
    # it has its own nuclei (right dentate, right fastigial, right
    # interposed):
    #
    #   hindbrain.metencephalon.cerebellum.hemispheres.right
    #
    # The right container is the RIGHT PONTINE nuclear collection, not
    # the right cerebellum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cnn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.{side}"
        )
        # resolve cnn_path through the memory/recall layer

Right cranial-nerve-specific detail (not wired — consult references)::

    # The six right-side nuclei and their functions:
    #   right abducens_nucleus           -> right CN VI, right lateral rectus
    #   right facial_nerve_nucleus       -> right CN VII, right facial expression
    #   right motor_trigeminal_nucleus   -> right CN V, right mastication
    #   right chief_sensory_trigeminal_nucleus -> right CN V, right discriminative touch
    #   right superior_salivatory_nucleus -> right CN VII, right lacrimal/salivary glands
    #   right vestibulocochlear_nuclei   -> right CN VIII, right hearing (cochlear) + right balance (vestibular)
    #
    # Do not attempt to resolve these as anything other than structural
    # children of the right container.

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Right pontine
    cranial-nerve nuclei in overview.)
*   **Cranial nerve nuclei — general:** Haines, D.E. (2012).
    *Neuroanatomy: An Atlas of Structures, Sections, and Systems*, 8th
    ed. (Right cranial-nerve nuclei of the pons.)
*   **Trigeminal system:** Usunoff, K.G., Marani, E., Schoen, J.H.R.
    (2006). "The trigeminal system." *Advances in Anatomy, Embryology,
    and Cell Biology* 184:1–146. (Right chief sensory trigeminal nucleus
    and the right trigeminal nuclear complex across brainstem levels.)
*   **Facial nerve and nucleus:** May, M., Schaitkin, B.M. (2000). *The
    Facial Nerve*, 2nd ed. (Right facial nerve nucleus and the right
    facial motor system.)
*   **Abducens nucleus and sixth nerve palsy:** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (Right abducens
    nucleus and right lateral rectus control.)
*   **Vestibulocochlear system:** Kandel, E.R., Schwartz, J.H., Jessell,
    T.M., Siegelbaum, S.A., Hudspeth, A.J. (2013). *Principles of Neural
    Science*, 5th ed. (Right cochlear and right vestibular nuclei —
    right hearing and right balance.)
*   **Superior salivatory nucleus:** Loewy, A.D., Spyer, K.M. (1990).
    *Central Regulation of Autonomic Functions*. (Right superior
    salivatory nucleus and the right parasympathetic outflow of right
    CN VII.)
*   **Cranial-nerve nuclei across brainstem levels (contrast — the right
    midbrain and right medullary nuclei are wired elsewhere):**
    Nieuwenhuys, R., Voogd, J., van Huijzen, C. (2008). *The Human
    Central Nervous System: A Synopsis and Atlas*, 4th ed. (Right
    cranial-nerve nuclei of the midbrain, pons, and medulla.)
*   **Trigeminal ganglion (contrast — the right peripheral ganglion):**
    Standring, S. (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Right trigeminal ganglion and the
    right peripheral trigeminal system.)
*   **Cerebellar nuclei (contrast — the right metencephalic sibling):**
    Manto, M., Gruol, D.L., Schmahmann, J.D., Koibuchi, N., Rossi, F.
    (eds.) (2013). *Handbook of the Cerebellum and Cerebellar
    Disorders*. (Right cerebellar nuclei — right dentate, right
    fastigial, right interposed.)
*   **Solitary nucleus (contrast — the right medullary visceral-afferent
    hub):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Right solitary nucleus and the
    right medullary visceral-afferent system.)
*   **SLEA (contrast — the right container is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the right container.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the right container. Note: the "right-amygdala" lateralization
    is about the **amygdala**, not about this right pontine
    cranial-nerve nuclear collection.)
*   NeuroNames — Cranial nerve nuclei (pons, right); FMA — Right cranial
    nerve nuclei of the pons.
""""""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.right
=================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── right   <-- THIS MODULE
                    ├── abducens_nucleus
                    ├── chief_sensory_trigeminal_nucleus
                    ├── facial_nerve_nucleus
                    ├── motor_trigeminal_nucleus
                    ├── superior_salivatory_nucleus
                    └── vestibulocochlear_nuclei
                        ├── cochlear_nuclei
                        └── vestibular_nuclei

**Primary synonym:** Right pontine cranial-nerve nuclei; right cranial-nerve
nuclei of the pons; right metencephalic cranial-nerve nuclei; "the right
pontine CN V–VIII subset."
**Cytoarchitectonic designation:** **Not a Brodmann area** — a **bilateral
sub-container** of **brainstem grey-matter nuclei**. A **heterogeneous
collection** of **six right-side cranial-nerve nuclei** in the **right
pontine tegmentum** — **motor** (`abducens_nucleus`,
`facial_nerve_nucleus`, `motor_trigeminal_nucleus`), **general sensory**
(`chief_sensory_trigeminal_nucleus`), **parasympathetic**
(`superior_salivatory_nucleus`), and **special sensory**
(`vestibulocochlear_nuclei`, comprising `cochlear_nuclei` and
`vestibular_nuclei`).
**Part of:** The **cranial_nerve_nuclei** container — specifically, the
**right bilateral half** of the pontine cranial-nerve nuclear collection.
The **cranial_nerve_nuclei** container is the **pontine** cranial-nerve
nuclear collection; the **right** container is its **right-side structural
child**.
**Structural parent:** ``.../cranial_nerve_nuclei/`` → **direct child** of
the cranial_nerve_nuclei container.
**Structural children:** **Six right-side cranial-nerve nuclei**:
``abducens_nucleus``, ``chief_sensory_trigeminal_nucleus``,
``facial_nerve_nucleus``, ``motor_trigeminal_nucleus``,
``superior_salivatory_nucleus``, and ``vestibulocochlear_nuclei`` (itself
a **sub-container** with ``cochlear_nuclei`` and ``vestibular_nuclei``).
**Boundary status (RIGHT HALF — NOT the whole cranial_nerve_nuclei
container):** **Boundary case — the right container is the RIGHT HALF of
the cranial_nerve_nuclei, NOT the whole container.** The
**cranial_nerve_nuclei** container (``.../cranial_nerve_nuclei/``) has
**two structural children** — ``left`` and ``right``. The **right**
container (here) is the **right-side** half only. Consumers must **not**
conflate the right container with the **whole cranial_nerve_nuclei
collection** — the left side is a **separate structural sibling**.
**Boundary status (NOT the left container — strict mirror, no warning):**
**Boundary case — the right container is NOT the left container; the two
are a STRICT MIRROR PAIR with NO warning at the container level.** The
**left** container (``.../cranial_nerve_nuclei/left/``) is the
**structurally identical** left-side counterpart — same six nuclei, same
leaf status for each nucleus, same bilateral framing. The two sides are
**strictly mirrored** — any lateralization is documented **inside the
individual nucleus modules**, not at the container level. Consumers must
**not** import a lateralization warning into the right container — there
is **none at the container level**.
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the right
container is a CONTAINER, not a leaf.** It has **six structural
children** (the six right-side cranial-nerve nuclei). The
**vestibulocochlear_nuclei** is itself a **sub-container** with
**cochlear_nuclei** and **vestibular_nuclei** as its children. Consumers
must **not** treat the right container as a leaf, and must **not** assume
the six nuclei are absent — they are its **direct structural children**.
**Boundary status (GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS):**
**Boundary case — the right container holds the GREY-MATTER NUCLEI, NOT
the cranial-nerve FIBERS (axons).** The **cranial nerves** (right CN V,
VI, VII, VIII) are the **white-matter axon bundles** that **leave** the
right pontine tegmentum and **travel** to the periphery. The **right
container** (here) holds the **grey-matter neuron clusters** that **give
rise to** (motor, parasympathetic) or **receive** (sensory, special
sensory) those axons. They are **DIFFERENT STRUCTURES** — the **nuclei**
are grey matter; the **nerves** are white matter. Consumers must **not**
conflate the **right nuclei** with the **right cranial nerves**.
**Boundary status (NOT the whole pons — the pons is the grandparent):**
**Boundary case — the right container is NOT the pons; the pons is the
grandparent.** The **pons** (``.../pons/``) is the **whole metencephalic
brainstem segment** — it contains the **basilar pons**, the **pontine
tegmentum**, the **pontine nuclei**, the **corticospinal/corticobulbar
tracts**, the **middle cerebellar peduncle**, and the
**cranial_nerve_nuclei** (both left and right). The **right container**
(here) is the **right-side cranial-nerve nuclei only**. Consumers must
**not** conflate the right container with the **whole pons**.
**Boundary status (NOT midbrain or medullary cranial-nerve nuclei — those
are DIFFERENT BRAINSTEM LEVELS):** **Boundary case — the right container
is NOT the midbrain or medullary cranial-nerve nuclei.** The **midbrain**
(``.../midbrain/cranial_nerve_nuclei/``) hosts **CN III, IV,
mesencephalic V, Edinger-Westphal**; the **medulla oblongata**
(``.../medulla_oblongata/cranial_nerve_nuclei/``) hosts **CN IX, X, XI,
XII, inferior salivatory, nucleus ambiguus, hypoglossal, dorsal motor
vagus, solitary**. The **right container** (here) is the **right pontine
subset only** — **CN V (chief sensory + motor), CN VI, CN VII (facial +
superior salivatory), CN VIII (cochlear + vestibular)**. Consumers must
**not** conflate the right pontine nuclei with the midbrain or medullary
cranial-nerve nuclei.
**Boundary status (NOT the whole trigeminal complex — the trigeminal
system spans levels):** **Boundary case — the right container does NOT
contain the whole right trigeminal nuclear complex.** The **right
trigeminal system** has **three** brainstem nuclei: the **right
mesencephalic trigeminal nucleus** (midbrain — proprioception), the
**right chief sensory trigeminal nucleus** (pons — discriminative touch,
**in this container**), and the **right spinal trigeminal nucleus**
(medulla/pons junction — pain/temperature). The **right container**
(here) contains **only the right chief sensory trigeminal nucleus** and
the **right motor trigeminal nucleus** — it does **not** contain the
right mesencephalic or spinal trigeminal nuclei. Consumers must **not**
conflate the right pontine trigeminal nuclei with the **whole right
trigeminal complex**.
**Boundary status (NOT the trigeminal ganglion or any sensory ganglion —
those are PERIPHERAL):** **Boundary case — the right container is NOT the
right trigeminal ganglion (or any right sensory ganglion).** The **right
trigeminal ganglion** (right semilunar / Gasserian ganglion) is a
**peripheral sensory ganglion** outside the brainstem containing the
**right primary sensory neuron cell bodies** for the right trigeminal
nerve. The **right container** (here) holds the **right central
grey-matter nuclei** inside the right pontine tegmentum. They are
**DIFFERENT STRUCTURES** — the **ganglion** is peripheral; the **nuclei**
are central. Consumers must **not** conflate the **right central nuclei**
with the **right peripheral ganglion**.
**Boundary status (NOT the cerebellum — that is the metencephalic
sibling):** **Boundary case — the right container is NOT the right
cerebellum.** The **right cerebellum**
(``.../metencephalon/cerebellum/hemispheres/right/``) is the **right
metencephalic cerebellar half**, with its **own nuclei** (right dentate,
right fastigial, right interposed: right emboliform + right globose) and
its **own cortex**. The **right container** (here) holds the **right
pontine cranial-nerve nuclei**, not the right cerebellar nuclei.
Consumers must **not** conflate the **right pontine cranial-nerve
nuclei** with the **right cerebellar nuclei**.
**Boundary status (NOT locus coeruleus, parabrachial area, pontine
nuclei, or other right pontine structures):** **Boundary case — the
right container is NOT the right locus coeruleus, the right parabrachial
area, the right pontine nuclei, or other right pontine structures.** The
**right locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) is
the **noradrenergic** nucleus; the **right parabrachial area**
(``.../pons/parabrachial_area/``) is the **visceral/autonomic relay**;
the **right pontine nuclei** (``.../pons/pontine_nuclei/right/``) are the
**cortico-ponto-cerebellar relay** in the **right basilar pons**. None of
these are **right cranial-nerve nuclei**. The **right container** (here)
is **only** the right nuclei that **give rise to or receive** the
**right cranial nerves V, VI, VII, VIII**. Consumers must **not**
conflate the right cranial-nerve nuclei with **other right pontine
nuclei**.
**Boundary status (NOT the solitary nucleus — that is the medullary
visceral-afferent hub):** **Boundary case — the right container is NOT
the right solitary nucleus.** The **right solitary nucleus** (right
nucleus tractus solitarius,
``.../medulla_oblongata/solitary_nucleus/right/``) is the **right
medullary visceral-afferent hub** for **right CN VII, IX, X** (taste,
visceral sensation, baroreception, respiratory chemoreception). The
**right container** (here) contains the **right superior salivatory
nucleus** (right CN VII parasympathetic), but it does **not** contain the
**right solitary nucleus**. Consumers must **not** conflate the right
pontine nuclei with the **right solitary nucleus**.
**Boundary status (NOT a single functional system — MULTIPLE nuclei with
DIFFERENT functions):** **Boundary case — the right container is a
HETEROGENEOUS collection of six right-side nuclei with DIFFERENT
functions, not a single uniform system.** The collection includes:
*   **Right abducens nucleus (CN VI)** — **somatic motor**; controls the
    **right lateral rectus** muscle (right eye abduction).
*   **Right facial nerve nucleus (CN VII)** — **branchial motor**;
    controls the **right muscles of facial expression**.
*   **Right motor trigeminal nucleus (CN V)** — **branchial motor**;
    controls the **right muscles of mastication**.
*   **Right chief sensory trigeminal nucleus (CN V)** — **general
    sensory**; **discriminative touch** from the **right face**.
*   **Right superior salivatory nucleus (CN VII)** — **parasympathetic**;
    controls the **right lacrimal** and **right salivary** glands.
*   **Right vestibulocochlear nuclei (CN VIII)** — **special sensory**;
    **right cochlear nuclei** subserve **right hearing**; **right
    vestibular nuclei** subserve **right balance and spatial
    orientation**.
**Each nucleus is functionally distinct** — the tree wires them as
**separate structural children under the right container**. Consumers
must **not** treat the right container as a single uniform nucleus — it
is a **distributed collection** of functionally distinct right-side
nuclei.

Overview
--------
The right container is the **right-side half** of the pontine
cranial-nerve nuclear collection — the **six grey-matter nuclei** in the
**right pontine tegmentum** that **give rise to** (motor,
parasympathetic) or **receive** (sensory, special sensory) the **right
cranial nerves V, VI, VII, and VIII**. It is a **container** under the
cranial_nerve_nuclei container, with **six structural children** (six
right-side nuclei), one of which (the **vestibulocochlear_nuclei**) is
itself a **sub-container**.

**The right container is a CONTAINER, NOT a leaf.** Its structural
children are the **six right-side nuclei**. The **right
vestibulocochlear_nuclei** is itself a **sub-container** with **right
cochlear_nuclei** and **right vestibular_nuclei** as its children.

**The right container is the RIGHT HALF of the cranial_nerve_nuclei, NOT
the whole container.** The **cranial_nerve_nuclei** container has **two
structural children** — ``left`` and ``right``. The **right** container
(here) is the **right-side** half only. The left side is a **separate
structural sibling**.

**The right container and the left container are a STRICT MIRROR PAIR
with NO warning at the container level.** The two sides are
**structurally identical** — same six nuclei, same leaf status for each
nucleus, same bilateral framing. Any lateralization is documented
**inside the individual nucleus modules**, not at the container level.

**The right container holds the GREY-MATTER NUCLEI, NOT the cranial-nerve
FIBERS.** The **right cranial nerves V, VI, VII, VIII** are the
**white-matter axon bundles** that **travel** to and from the periphery.
The **right container** (here) holds the **grey-matter neuron clusters**
inside the right pontine tegmentum. They are **DIFFERENT STRUCTURES** —
the **nuclei** are grey matter; the **nerves** are white matter.

**The right container is NOT the whole right trigeminal complex.** The
**right trigeminal system** spans three brainstem levels — the **right
mesencephalic trigeminal nucleus** (midbrain), the **right chief sensory
trigeminal nucleus** (pons, **in this container**), and the **right
spinal trigeminal nucleus** (medulla/pons junction). The **right
container** contains **only the pontine trigeminal components** (chief
sensory + motor).

**The right container is HETEROGENEOUS.** The six right-side nuclei are
**functionally distinct** — **motor** (right abducens, right facial,
right motor trigeminal), **general sensory** (right chief sensory
trigeminal), **parasympathetic** (right superior salivatory), and
**special sensory** (right vestibulocochlear). The tree wires them as
**separate structural children under the right container**.

Nucleus Composition (structural children, prose)
------------------------------------------------
The right container contains **six right-side nuclei**, documented as
**structural children** (not as leaves of the container):

*   **Right abducens nucleus**
    (``.../cranial_nerve_nuclei/right/abducens_nucleus/``) — **somatic
    motor**; controls the **right lateral rectus** muscle (right eye
    abduction). CN VI.

*   **Right chief sensory trigeminal nucleus**
    (``.../cranial_nerve_nuclei/right/chief_sensory_trigeminal_nucleus/``)
    — **general sensory**; **discriminative touch** from the **right
    face**. CN V (principal sensory nucleus).

*   **Right facial nerve nucleus**
    (``.../cranial_nerve_nuclei/right/facial_nerve_nucleus/``) —
    **branchial motor**; controls the **right muscles of facial
    expression**. CN VII.

*   **Right motor trigeminal nucleus**
    (``.../cranial_nerve_nuclei/right/motor_trigeminal_nucleus/``) —
    **branchial motor**; controls the **right muscles of mastication**.
    CN V.

*   **Right superior salivatory nucleus**
    (``.../cranial_nerve_nuclei/right/superior_salivatory_nucleus/``) —
    **parasympathetic**; controls the **right lacrimal** and **right
    salivary** glands. CN VII.

*   **Right vestibulocochlear nuclei**
    (``.../cranial_nerve_nuclei/right/vestibulocochlear_nuclei/``) —
    **special sensory**; a **sub-container** with two children:
    *   **Right cochlear nuclei** — **right hearing** (right CN VIII
        cochlear division).
    *   **Right vestibular nuclei** — **right balance and spatial
        orientation** (right CN VIII vestibular division).

**These nuclei are structural children of the right container.** The
right container's **structural children** are the **six right-side
nuclei**; the **right vestibulocochlear nuclei** is a **sub-container**
with two of its own children. Consumers resolving nucleus-level detail
go **through** the right container, and resolving cochlear/vestibular
detail goes **through** the right vestibulocochlear nuclei.

The Right / Left Boundary
-------------------------
This is the **strict-mirror** boundary:

*   **Right container** (this module) — the **right-side** pontine
    cranial-nerve nuclei.

*   **Left container** (``.../cranial_nerve_nuclei/left/``) — the
    **structurally identical** left-side pontine cranial-nerve nuclei.

**They are a STRICT MIRROR PAIR with NO warning at the container level.**
The two sides are **structurally identical** — same six nuclei, same leaf
status for each nucleus, same bilateral framing. Any lateralization is
documented **inside the individual nucleus modules**, not at the container
level. Consumers must **not** import a lateralization warning into the
right container.

The Right Container / Cranial Nerve Nuclei Container Boundary
-------------------------------------------------------------
This is the **half vs. whole** boundary:

*   **Right container** (this module) — the **right-side** half of the
    pontine cranial-nerve nuclear collection.

*   **Cranial_nerve_nuclei container** (``.../cranial_nerve_nuclei/``)
    — the **whole pontine collection**, with **two structural children**
    (``left`` and ``right``).

**The right container is a child of the cranial_nerve_nuclei container.**
Consumers must **not** conflate the right half with the **whole pontine
collection** — the left side is a **separate structural sibling**.

The Right Container / Cranial Nerves Boundary
---------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Right container** (this module) — the **right-side grey-matter
    neuron clusters** in the right pontine tegmentum.

*   **Right cranial nerves V, VI, VII, VIII** — the **right white-matter
    axon bundles** that travel to and from the periphery.

**They are DIFFERENT STRUCTURES.** The **right nuclei** are the **right
central neuronal sources/targets**; the **right nerves** are the **right
peripheral conduction infrastructure**. Consumers must **not** conflate
the two.

The Right Container / Pons Boundary
-----------------------------------
This is the **great-grandchild vs. grandparent** boundary:

*   **Right container** (this module) — the **right-side tegmental
    grey-matter nuclei** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine
    tegmentum**, the **pontine nuclei**, the **corticospinal/
    corticobulbar tracts**, the **middle cerebellar peduncle**, and the
    **cranial-nerve nuclei** (both left and right).

**The right container is a great-grandchild of the pons** (via
cranial_nerve_nuclei). Consumers must **not** conflate the right
cranial-nerve nuclei with the **whole pons**.

The Right Container / Midbrain and Medullary Cranial-Nerve Nuclei Boundary
--------------------------------------------------------------------------
This is the **brainstem-level** boundary:

*   **Right container** (this module) — the **right pontine** nuclei only
    — **right CN V (chief sensory + motor)**, **right CN VI**, **right
    CN VII (facial + superior salivatory)**, **right CN VIII (cochlear +
    vestibular)**.

*   **Right midbrain cranial-nerve nuclei**
    (``.../midbrain/cranial_nerve_nuclei/right/``) — **right CN III
    (oculomotor)**, **right CN IV (trochlear)**, **right mesencephalic
    trigeminal nucleus (right CN V proprioceptive)**, **right
    Edinger-Westphal nucleus (right CN III parasympathetic)**.

*   **Right medullary cranial-nerve nuclei**
    (``.../medulla_oblongata/cranial_nerve_nuclei/right/``) — **right CN
    IX (glossopharyngeal)**, **right CN X (vagus)**, **right CN XI
    (accessory)**, **right CN XII (hypoglossal)**, **right inferior
    salivatory nucleus**, **right nucleus ambiguus**, **right
    hypoglossal nucleus**, **right dorsal motor nucleus of the vagus**,
    **right solitary nucleus**.

**They are DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate
the **right pontine** cranial-nerve nuclei with the **right midbrain** or
**right medullary** cranial-nerve nuclei.

The Right Container / Trigeminal Complex Boundary
-------------------------------------------------
This is the **partial-complex** boundary:

*   **Right container** (this module) — contains **only** the **right
    chief sensory trigeminal nucleus** (discriminative touch) and the
    **right motor trigeminal nucleus** (mastication).

*   **Right mesencephalic trigeminal nucleus**
    (``.../midbrain/tegmentum/mesencephalic_trigeminal_nucleus/right/``)
    — **right proprioception** (right CN V mesencephalic division).

*   **Right spinal trigeminal nucleus**
    (``.../medulla_oblongata/spinal_trigeminal_nucleus/right/``) —
    **right pain and temperature** (right CN V spinal division).

**The right trigeminal nuclear complex spans three brainstem levels.**
The **right container** contains **only the right pontine components**.
Consumers must **not** conflate the right pontine trigeminal nuclei with
the **whole right trigeminal complex**.

The Right Container / Right Cerebellum Boundary
-----------------------------------------------
This is the **metencephalic-sibling** boundary:

*   **Right container** (this module) — the **right pontine**
    cranial-nerve nuclei.

*   **Right cerebellum**
    (``.../metencephalon/cerebellum/hemispheres/right/``) — the **right
    metencephalic cerebellar half**, with its **own nuclei** (right
    dentate, right fastigial, right interposed: right emboliform + right
    globose) and its **own cortex**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
**right pontine cranial-nerve nuclei** with the **right cerebellar
nuclei**.

The Right Container / Other Right Pontine Structures Boundary
-------------------------------------------------------------
This is the **non-cranial-nerve right pontine** boundary:

*   **Right container** (this module) — **only** the right nuclei that
    **give rise to or receive** the **right cranial nerves V, VI, VII,
    VIII**.

*   **Right locus coeruleus**
    (``.../pons/tegmentum/locus_coeruleus/``) — the **right
    noradrenergic** nucleus.

*   **Right parabrachial area** (``.../pons/parabrachial_area/``) — the
    **right visceral/autonomic relay**.

*   **Right pontine nuclei** (``.../pons/pontine_nuclei/right/``) — the
    **right cortico-ponto-cerebellar relay** in the **right basilar
    pons**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
right cranial-nerve nuclei with **other right pontine nuclei**.

The Right Container / Right Solitary Nucleus Boundary
-----------------------------------------------------
This is the **visceral-afferent** boundary:

*   **Right container** (this module) — contains the **right superior
    salivatory nucleus** (right CN VII parasympathetic), but **not** the
    **right solitary nucleus**.

*   **Right solitary nucleus**
    (``.../medulla_oblongata/solitary_nucleus/right/``) — the **right
    medullary visceral-afferent hub** for **right CN VII, IX, X** (taste,
    visceral sensation, baroreception, respiratory chemoreception).

**The right solitary nucleus is medullary, not pontine.** Consumers must
**not** conflate the right pontine nuclei with the **right solitary
nucleus**.

Function in the Human Brain
---------------------------
The right container's functions are **the right cranial-nerve
sensorimotor and parasympathetic relay** — **NOT a single unified
function**:

*   **Somatic Motor (Right Abducens Nucleus, right CN VI):** Controls the
    **right lateral rectus** muscle — **right eye abduction**. The right
    abducens nucleus is the **sole source** of the right lateral rectus
    motor innervation.

*   **Branchial Motor (Right Facial Nerve Nucleus, right CN VII):**
    Controls the **right muscles of facial expression** — the right
    facial nerve is the **principal right motor nerve of the face**.

*   **Branchial Motor (Right Motor Trigeminal Nucleus, right CN V):**
    Controls the **right muscles of mastication** — the right motor
    trigeminal nucleus is the **sole source** of the right motor
    trigeminal innervation.

*   **General Sensory (Right Chief Sensory Trigeminal Nucleus, right CN
    V):** **Discriminative touch** from the **right face** — the right
    principal sensory nucleus is the **right pontine** component of the
    right trigeminal nuclear complex.

*   **Parasympathetic (Right Superior Salivatory Nucleus, right CN VII):**
    Controls the **right lacrimal** and **right salivary** glands — the
    right superior salivatory nucleus is the **right preganglionic
    parasympathetic** source for the right facial nerve's autonomic
    component.

*   **Special Sensory (Right Vestibulocochlear Nuclei, right CN VIII):**
    The **right cochlear nuclei** subserve **right hearing**; the
    **right vestibular nuclei** subserve **right balance and spatial
    orientation**. The right vestibulocochlear nuclei are the **right
    brainstem relay** for the right auditory and vestibular senses.

**The unifying theme:** the right container is the **right pontine
cranial-nerve nuclear collection** — the **right grey-matter nuclei**
that **give rise to or receive** the **right cranial nerves V, VI, VII,
VIII**. It is **heterogeneous** and **strictly mirrored** — the six
right-side nuclei are **functionally distinct**, and they are
**structural children** of the right container.

Associated Disorders
--------------------
The right container has **no single named clinical syndrome as a
collection** — its clinical associations are **right-nucleus-specific**:

*   **Right Abducens Nucleus (right CN VI) — Right Sixth Nerve Palsy:**
    Lesions cause **right lateral rectus palsy** — **inability to abduct
    the right eye**, **diplopia** on right lateral gaze.

*   **Right Facial Nerve Nucleus (right CN VII) — Right Facial Nerve
    Palsy (right Bell's Palsy, right Supranuclear Palsy):** Lesions
    cause **ipsilateral (right) facial weakness** — **inability to close
    the right eye**, **right facial droop**, **loss of right forehead
    wrinkling** (peripheral lesions) versus **right forehead sparing**
    (supranuclear lesions).

*   **Right Motor Trigeminal Nucleus (right CN V) — Right Trigeminal
    Motor Palsy:** Lesions cause **weakness of right mastication** —
    **jaw deviation** toward the **right** side.

*   **Right Chief Sensory Trigeminal Nucleus (right CN V) — Right
    Trigeminal Sensory Loss:** Lesions cause **right facial sensory
    loss** — **discriminative touch** impairment on the **right face**.

*   **Right Superior Salivatory Nucleus (right CN VII) — Right Autonomic
    Facial Palsy:** Lesions cause **reduced right lacrimation** and
    **reduced right salivation**.

*   **Right Vestibulocochlear Nuclei (right CN VIII) — Right
    Vestibulocochlear Disorders:** Lesions cause **right hearing loss**
    (right cochlear nuclei) and **right vertigo / right nystagmus /
    right imbalance** (right vestibular nuclei).

*   **No Named "Right Cranial Nerve Nuclei Syndrome":** The right
    container is a **heterogeneous collection**, not a **single
    structure** — it has **no named clinical syndrome as a collection**.
    Its clinical relevance is **right-nucleus-specific**, via the
    **individual right cranial-nerve nuclei** and the **right cranial
    nerves** they subserve.

**What is NOT here:** The right container is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala), **fear conditioning** (amygdala —
central nucleus + basolateral nuclei), **Urbach-Wiethe disease**
(amygdala — basolateral nuclei), **Alzheimer's disease** (hippocampus,
nucleus basalis), or **Parkinson's disease** (substantia nigra). Its
clinical relevance is **right-cranial-nerve-specific**, via the
**individual right nuclei** and the **right cranial nerves** they
subserve. **No named right cranial_nerve_nuclei syndrome exists as a
collection.**

Lateralization Notes
--------------------
This is the **right** container of the cranial_nerve_nuclei. The right
container is **bilaterally symmetric** with the left container and
**strictly mirrored** — and it carries **NO warning at the container
level**:

*   **Strict Bilateral Symmetry:** The **right** and **left**
    containers are **structurally identical** — same six nuclei under
    each, same leaf status for each nucleus, same bilateral framing. The
    bilateral symmetry is **strict**.

*   **Lateralization is Nucleus-Specific (Contested, Documented in the
    Nucleus Modules):** Any functional lateralization (e.g. right facial
    motor control, right vestibular asymmetry, right auditory
    lateralization) is documented **inside the individual right nucleus
    modules**, not at the container level. Consumers must **not** assume
    a container-level lateralization — the right container is a
    **strict-mirror right half**.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The right
    container is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the right container.

*   **NO Amygdala-Lateralization Warning of their own (the right
    container is MODULATORY-AGNOSTIC, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The right container is a
    **right cranial-nerve nuclear collection** — consumers must **not**
    conflate it with the **amygdala** or with the **fear circuit**. The
    **right container** is **SLEA-free** and **amygdala-agnostic**.

**A consumer that assumes "right container = left container" will be
structurally correct** — the two sides are **strictly symmetric** (any
lateralization is documented in the nucleus modules). The right container
is a **strict-mirror pair with NO warning at the container level** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right container is the **right
    half**; it does **not** import the left container at module level.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../medulla_oblongata/``,
    ``.../metencephalon/cerebellum/``, or any other container. The right
    container's relationships to the **right midbrain** and **right
    medullary** cranial-nerve nuclei, the **right cerebellum**, the
    **right locus coeruleus**, the **right parabrachial area**, and the
    **right pontine nuclei** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children are the SIX right-side
    nuclei.** The **right vestibulocochlear nuclei** is itself a
    **sub-container** with **right cochlear nuclei** and **right
    vestibular nuclei** as its children.
*   **RIGHT HALF — NOT the whole cranial_nerve_nuclei container.** The
    **cranial_nerve_nuclei** container has **two structural children** —
    ``left`` and ``right``. The **right** container (here) is the
    **right-side** half only.
*   **STRICT MIRROR with the left container — NO warning at the
    container level.** The **right** and **left** containers are
    **structurally identical**. Any lateralization is documented **inside
    the individual nucleus modules**.
*   **GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS.** The **right
    nuclei** are the **grey-matter neuron clusters**; the **right cranial
    nerves V, VI, VII, VIII** are the **white-matter axon bundles**.
    Consumers must **not** conflate the two.
*   **NOT the whole brainstem or the whole right cranial-nerve system —
    only the RIGHT PONTINE subset.** The **right midbrain** and **right
    medullary** cranial-nerve nuclei are **wired elsewhere**.
*   **NOT a single functional system — MULTIPLE right-side nuclei.** The
    **right abducens nucleus**, **right facial nerve nucleus**, **right
    motor trigeminal nucleus**, **right chief sensory trigeminal
    nucleus**, **right superior salivatory nucleus**, and **right
    vestibulocochlear nuclei** are **functionally distinct**.
*   **NOT the right mesencephalic or right spinal trigeminal nucleus —
    the right trigeminal system spans levels.** The **right container**
    contains **only the right pontine trigeminal components** (chief
    sensory + motor).
*   **NOT the right trigeminal ganglion or any right sensory ganglion —
    those are PERIPHERAL.** The **right nuclei** are **central**; the
    **right ganglia** are **peripheral**.
*   **NOT the right cerebellum — that is the metencephalic sibling.** The
    **right cerebellar nuclei** (right dentate, right fastigial, right
    interposed) are **wired elsewhere**.
*   **NOT the right solitary nucleus — that is the right medullary
    visceral-afferent hub.** The **right superior salivatory nucleus** is
    here, but the **right solitary nucleus** is not.
*   **SLEA-FREE — no extended-amygdala relationship.** The right
    container is **not** an extended-amygdala component, and it carries
    **no SLEA warning**.
*   **No ``AREA_PATHS`` hop.** The right container is a local
    sub-container under cranial_nerve_nuclei, not a cross-listed
    container.
*   **No nested cross-listing.** The right container has no nested
    dual-framing module. It is a single bilateral sub-container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei import right

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.right"
    )

**Do not** assume the right container is a **leaf**. It is a
**container** — its structural children are the **six right-side
nuclei**.

**Do not** assume the right container is the **whole cranial_nerve_nuclei
container**. It is the **right-side half only** — the left side is a
**separate structural sibling**.

**Do not** assume the right container is the **left container**. The two
are a **strict mirror pair with NO warning at the container level** — any
lateralization is documented **inside the individual nucleus modules**.

**Do not** assume the right container is the **right cranial nerves V,
VI, VII, VIII**. The **nerves** are the **white-matter axon bundles**;
the **nuclei** are the **grey-matter neuron clusters**. They are
**different structures**.

**Do not** assume the right container is the **whole right brainstem** or
the **whole right cranial-nerve system**. It is **only the right pontine
subset** — the **right midbrain** and **right medullary** cranial-nerve
nuclei are **wired elsewhere**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the right container. **The right container is SLEA-FREE**
and **amygdala-agnostic**.

Iterating the right container's structural children (recommended
consumer pattern)::

    RIGHT_CRANIAL_NERVE_NUCLEI_CHILDREN = (
        "abducens_nucleus",
        "chief_sensory_trigeminal_nucleus",
        "facial_nerve_nucleus",
        "motor_trigeminal_nucleus",
        "superior_salivatory_nucleus",
        "vestibulocochlear_nuclei",
    )
    # The right container is the RIGHT HALF of the cranial_nerve_nuclei.
    # The right vestibulocochlear nuclei is itself a sub-container with
    # right cochlear nuclei and right vestibular nuclei as its children.

Iterating the right container's nuclei (recommended consumer pattern)::

    for nucleus in RIGHT_CRANIAL_NERVE_NUCLEI_CHILDREN:
        nucleus_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.right."
            f"{nucleus}"
        )
        # resolve nucleus_path through the memory/recall layer

Reaching the right vestibulocochlear nuclei's sub-children (recommended
consumer pattern — the sub-container)::

    for sub in ("cochlear_nuclei", "vestibular_nuclei"):
        sub_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.right."
            f"vestibulocochlear_nuclei.{sub}"
        )
        # resolve sub_path through the memory/recall layer

Reaching the left container (recommended consumer pattern — the strict
mirror)::

    # The left container is the structurally identical LEFT half:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.left
    #
    # The right and left containers are a STRICT MIRROR PAIR with NO
    # warning at the container level.

Reaching the right midbrain cranial-nerve nuclei (recommended consumer
pattern — NOTE the brainstem-level boundary)::

    # The right midbrain hosts right CN III, IV, mesencephalic V,
    # Edinger-Westphal:
    #
    #   hindbrain.midbrain.cranial_nerve_nuclei.right
    #
    # The right container is only the RIGHT PONTINE subset.

Reaching the right medullary cranial-nerve nuclei (recommended consumer
pattern — NOTE the brainstem-level boundary)::

    # The right medulla hosts right CN IX, X, XI, XII, inferior
    # salivatory, nucleus ambiguus, hypoglossal, dorsal motor vagus,
    # solitary:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right
    #
    # The right container is only the RIGHT PONTINE subset.

Reaching the right cerebellum (recommended consumer pattern — NOTE the
metencephalic-sibling boundary)::

    # The right cerebellum is the right metencephalic cerebellar half —
    # it has its own nuclei (right dentate, right fastigial, right
    # interposed):
    #
    #   hindbrain.metencephalon.cerebellum.hemispheres.right
    #
    # The right container is the RIGHT PONTINE nuclear collection, not
    # the right cerebellum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cnn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.{side}"
        )
        # resolve cnn_path through the memory/recall layer

Right cranial-nerve-specific detail (not wired — consult references)::

    # The six right-side nuclei and their functions:
    #   right abducens_nucleus           -> right CN VI, right lateral rectus
    #   right facial_nerve_nucleus       -> right CN VII, right facial expression
    #   right motor_trigeminal_nucleus   -> right CN V, right mastication
    #   right chief_sensory_trigeminal_nucleus -> right CN V, right discriminative touch
    #   right superior_salivatory_nucleus -> right CN VII, right lacrimal/salivary glands
    #   right vestibulocochlear_nuclei   -> right CN VIII, right hearing (cochlear) + right balance (vestibular)
    #
    # Do not attempt to resolve these as anything other than structural
    # children of the right container.

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Right pontine
    cranial-nerve nuclei in overview.)
*   **Cranial nerve nuclei — general:** Haines, D.E. (2012).
    *Neuroanatomy: An Atlas of Structures, Sections, and Systems*, 8th
    ed. (Right cranial-nerve nuclei of the pons.)
*   **Trigeminal system:** Usunoff, K.G., Marani, E., Schoen, J.H.R.
    (2006). "The trigeminal system." *Advances in Anatomy, Embryology,
    and Cell Biology* 184:1–146. (Right chief sensory trigeminal nucleus
    and the right trigeminal nuclear complex across brainstem levels.)
*   **Facial nerve and nucleus:** May, M., Schaitkin, B.M. (2000). *The
    Facial Nerve*, 2nd ed. (Right facial nerve nucleus and the right
    facial motor system.)
*   **Abducens nucleus and sixth nerve palsy:** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (Right abducens
    nucleus and right lateral rectus control.)
*   **Vestibulocochlear system:** Kandel, E.R., Schwartz, J.H., Jessell,
    T.M., Siegelbaum, S.A., Hudspeth, A.J. (2013). *Principles of Neural
    Science*, 5th ed. (Right cochlear and right vestibular nuclei —
    right hearing and right balance.)
*   **Superior salivatory nucleus:** Loewy, A.D., Spyer, K.M. (1990).
    *Central Regulation of Autonomic Functions*. (Right superior
    salivatory nucleus and the right parasympathetic outflow of right
    CN VII.)
*   **Cranial-nerve nuclei across brainstem levels (contrast — the right
    midbrain and right medullary nuclei are wired elsewhere):**
    Nieuwenhuys, R., Voogd, J., van Huijzen, C. (2008). *The Human
    Central Nervous System: A Synopsis and Atlas*, 4th ed. (Right
    cranial-nerve nuclei of the midbrain, pons, and medulla.)
*   **Trigeminal ganglion (contrast — the right peripheral ganglion):**
    Standring, S. (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Right trigeminal ganglion and the
    right peripheral trigeminal system.)
*   **Cerebellar nuclei (contrast — the right metencephalic sibling):**
    Manto, M., Gruol, D.L., Schmahmann, J.D., Koibuchi, N., Rossi, F.
    (eds.) (2013). *Handbook of the Cerebellum and Cerebellar
    Disorders*. (Right cerebellar nuclei — right dentate, right
    fastigial, right interposed.)
*   **Solitary nucleus (contrast — the right medullary visceral-afferent
    hub):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Right solitary nucleus and the
    right medullary visceral-afferent system.)
*   **SLEA (contrast — the right container is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the right container.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the right container. Note: the "right-amygdala" lateralization
    is about the **amygdala**, not about this right pontine
    cranial-nerve nuclear collection.)
*   NeuroNames — Cranial nerve nuclei (pons, right); FMA — Right cranial
    nerve nuclei of the pons.
"""