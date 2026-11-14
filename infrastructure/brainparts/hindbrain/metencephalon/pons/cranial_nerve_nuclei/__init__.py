"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei
===========================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei   <-- THIS MODULE
                ├── left
                │   ├── abducens_nucleus
                │   ├── chief_sensory_trigeminal_nucleus
                │   ├── facial_nerve_nucleus
                │   ├── motor_trigeminal_nucleus
                │   ├── superior_salivatory_nucleus
                │   └── vestibulocochlear_nuclei
                │       ├── cochlear_nuclei
                │       └── vestibular_nuclei
                └── right
                    └── (mirror of left)

**Primary synonym:** Pontine cranial-nerve nuclei; cranial-nerve nuclei of
the pons; metencephalic cranial-nerve nuclei; "the pontine CN III–XII
subset" (specifically **CN V**, **CN VI**, **CN VII**, **CN VIII**).
**Cytoarchitectonic designation:** **Not a Brodmann area** — these are
**brainstem grey-matter nuclei**, not cortical areas. A **heterogeneous
collection** of **six cranial-nerve nuclei** in the **pontine tegmentum**
— **motor** (`abducens_nucleus`, `facial_nerve_nucleus`,
`motor_trigeminal_nucleus`), **general sensory**
(`chief_sensory_trigeminal_nucleus`), **parasympathetic**
(`superior_salivatory_nucleus`), and **special sensory**
(`vestibulocochlear_nuclei`, comprising `cochlear_nuclei` and
`vestibular_nuclei`).
**Part of:** The **pons** container — specifically, the **tegmental**
(dorsal) component that hosts the cranial-nerve nuclei. The **pons** is
the **metencephalic** brainstem segment.
**Structural parent:** ``.../pons/`` → **direct child** of the pons
container.
**Structural children:** **left** and **right** — the **bilateral
containers**. Each side contains **six cranial-nerve nuclei**:
``abducens_nucleus``, ``chief_sensory_trigeminal_nucleus``,
``facial_nerve_nucleus``, ``motor_trigeminal_nucleus``,
``superior_salivatory_nucleus``, and ``vestibulocochlear_nuclei`` (itself
a **sub-container** with ``cochlear_nuclei`` and ``vestibular_nuclei``).
**Boundary status (CONTAINER — NOT a leaf):** **Boundary case — the
cranial_nerve_nuclei is a CONTAINER, not a leaf.** It has **two structural
children** (``left`` and ``right``), each of which is itself a **container**
for six nuclei. The six nuclei are **structural grandchildren**, not
structural children. Consumers must **not** treat the
cranial_nerve_nuclei as a leaf, and must **not** assume the nuclei are
direct structural children of the container — they are children of the
``left`` and ``right`` containers.
**Boundary status (NOT the pons — the pons is the PARENT):** **Boundary
case — the cranial_nerve_nuclei is NOT the pons; the pons is the PARENT.**
The **pons** (``.../pons/``) is the **whole metencephalic brainstem
segment** — it contains the **basilar pons**, the **pontine tegmentum**,
the **pontine nuclei**, the **corticospinal/corticobulbar tracts**, the
**middle cerebellar peduncle**, and the **cranial_nerve_nuclei**. The
**cranial_nerve_nuclei** (here) are the **tegmental grey-matter nuclei**
only. Consumers must **not** conflate the nuclei collection with the
**whole pons** — the pons is much larger, and it hosts many structures
that are **not** cranial-nerve nuclei.
**Boundary status (NOT the whole brainstem, metencephalon, or hindbrain):**
**Boundary case — the cranial_nerve_nuclei is NOT the whole brainstem,
metencephalon, or hindbrain.** The **hindbrain** contains the
**metencephalon** (pons + cerebellum) and the **myelencephalon** (medulla
oblongata). The **metencephalon** contains the **pons** and the
**cerebellum**. The **cranial_nerve_nuclei** (here) are the **pontine
cranial-nerve nuclei only** — they do **not** include the **midbrain**
(CN III, IV, mesencephalic V) or **medullary** (CN IX, X, XI, XII,
inferior salivatory, nucleus ambiguus, hypoglossal, dorsal motor vagus,
solitary) cranial-nerve nuclei, and they do **not** include the
**cerebellum** (which is a separate metencephalic structure). Consumers
must **not** conflate the pontine nuclei with the **whole brainstem** or
with **cranial-nerve nuclei of other brainstem levels**.
**Boundary status (GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS):**
**Boundary case — the cranial_nerve_nuclei are the GREY-MATTER NUCLEI, NOT
the cranial-nerve FIBERS (axons).** The **cranial nerves** (CN V, VI, VII,
VIII) are the **white-matter axon bundles** that **leave** the brainstem
and **travel** to the periphery. The **cranial_nerve_nuclei** (here) are
the **grey-matter neuron clusters** inside the pontine tegmentum that
**give rise to** (motor) or **receive** (sensory) those axons. They are
**DIFFERENT STRUCTURES** — the **nuclei** are grey matter; the **nerves**
are white matter. Consumers must **not** conflate the **nuclei** with the
**nerves** — the nuclei are the **central neuronal sources/targets**; the
nerves are the **peripheral conduction infrastructure**.
**Boundary status (NOT the midbrain cranial-nerve nuclei — CN III, IV,
mesencephalic V, Edinger-Westphal):** **Boundary case — the
cranial_nerve_nuclei is NOT the midbrain cranial-nerve nuclei.** The
**midbrain** (``.../midbrain/cranial_nerve_nuclei/``) hosts the
**oculomotor nucleus (CN III)**, the **trochlear nucleus (CN IV)**, the
**mesencephalic trigeminal nucleus (CN V proprioceptive)**, and the
**Edinger-Westphal nucleus (CN III parasympathetic)**. The
**cranial_nerve_nuclei** (here) are the **pontine** nuclei — **CN V, VI,
VII, VIII** — and they do **not** include the midbrain nuclei. Consumers
must **not** conflate the pontine nuclei with the **midbrain nuclei** —
they are **different brainstem levels** with **different cranial nerves**.
**Boundary status (NOT the medullary cranial-nerve nuclei — CN IX, X, XI,
XII, inferior salivatory, nucleus ambiguus, hypoglossal, dorsal motor
vagus, solitary):** **Boundary case — the cranial_nerve_nuclei is NOT the
medullary cranial-nerve nuclei.** The **medulla oblongata**
(``.../medulla_oblongata/cranial_nerve_nuclei/``) hosts the
**glossopharyngeal (IX)**, **vagus (X)**, **accessory (XI)**, and
**hypoglossal (XII)** nuclei — including the **inferior salivatory
nucleus**, the **nucleus ambiguus**, the **hypoglossal nucleus**, the
**dorsal motor nucleus of the vagus**, and the **solitary nucleus**. The
**cranial_nerve_nuclei** (here) are the **pontine** nuclei only. Consumers
must **not** conflate the pontine nuclei with the **medullary nuclei** —
they are **different brainstem levels** with **different cranial nerves**.
**Boundary status (NOT the mesencephalic or spinal trigeminal nucleus —
the trigeminal system spans levels):** **Boundary case — the
cranial_nerve_nuclei does NOT contain the whole trigeminal nuclear
complex.** The **trigeminal system** has **three** brainstem nuclei: the
**mesencephalic trigeminal nucleus** (midbrain — proprioception), the
**chief sensory trigeminal nucleus** (pons — discriminative touch, **in
this module**), and the **spinal trigeminal nucleus** (medulla/pons
junction — pain/temperature). The **cranial_nerve_nuclei** (here) contains
**only the chief sensory trigeminal nucleus** and the **motor trigeminal
nucleus** — it does **not** contain the **mesencephalic** or **spinal**
trigeminal nuclei. Consumers must **not** conflate the pontine trigeminal
nuclei with the **whole trigeminal complex**.
**Boundary status (NOT the trigeminal ganglion or sensory ganglia — those
are PERIPHERAL):** **Boundary case — the cranial_nerve_nuclei is NOT the
trigeminal ganglion (or any sensory ganglion).** The **trigeminal
ganglion** (semilunar ganglion, Gasserian ganglion) is a **peripheral
sensory ganglion** outside the brainstem that contains the **primary
sensory neuron cell bodies** for the trigeminal nerve. The
**cranial_nerve_nuclei** (here) are the **central grey-matter nuclei**
inside the pontine tegmentum. They are **DIFFERENT STRUCTURES** — the
**ganglion** is peripheral; the **nuclei** are central. Consumers must
**not** conflate the **central nuclei** with the **peripheral ganglion**.
**Boundary status (NOT the cerebellum — that is the metencephalic
sibling):** **Boundary case — the cranial_nerve_nuclei is NOT the
cerebellum.** The **cerebellum** (``.../metencephalon/cerebellum/``) is
the **other metencephalic structure** — it has its **own nuclei**
(dentate, fastigial, interposed: emboliform + globose) and its **own
cortex**. The **cranial_nerve_nuclei** (here) are the **pontine** nuclei,
not the cerebellar nuclei. Consumers must **not** conflate the **pontine
cranial-nerve nuclei** with the **cerebellar nuclei** — they are
**different structures** in **different metencephalic sub-regions**.
**Boundary status (NOT the locus coeruleus, parabrachial area, pontine
nuclei, or other pontine structures):** **Boundary case — the
cranial_nerve_nuclei is NOT the locus coeruleus, the parabrachial area,
the pontine nuclei, or other pontine structures.** The **locus
coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) is the
**noradrenergic** nucleus; the **parabrachial area**
(``.../pons/parabrachial_area/``) is the **visceral/autonomic relay**;
the **pontine nuclei** (``.../pons/pontine_nuclei/``) are the
**cortico-ponto-cerebellar relay** in the **basilar pons**. None of these
are **cranial-nerve nuclei**. The **cranial_nerve_nuclei** (here) are
**only** the nuclei that **give rise to or receive** the **cranial nerves
V, VI, VII, VIII**. Consumers must **not** conflate the cranial-nerve
nuclei with **other pontine nuclei** — they are **different structures**.
**Boundary status (NOT a single functional system — MULTIPLE nuclei with
DIFFERENT functions):** **Boundary case — the cranial_nerve_nuclei is a
HETEROGENEOUS collection of six nuclei with DIFFERENT functions, not a
single uniform system.** The collection includes:
*   **Abducens nucleus (CN VI)** — **somatic motor**; controls the
    **lateral rectus** muscle (eye abduction).
*   **Facial nerve nucleus (CN VII)** — **branchial motor**; controls the
    **muscles of facial expression**.
*   **Motor trigeminal nucleus (CN V)** — **branchial motor**; controls
    the **muscles of mastication**.
*   **Chief sensory trigeminal nucleus (CN V)** — **general sensory**;
    **discriminative touch** from the face.
*   **Superior salivatory nucleus (CN VII)** — **parasympathetic**;
    controls the **lacrimal** and **salivary** glands.
*   **Vestibulocochlear nuclei (CN VIII)** — **special sensory**;
    **cochlear nuclei** subserve **hearing**; **vestibular nuclei**
    subserve **balance and spatial orientation**.
**Each nucleus is functionally distinct** — the tree wires them as
**separate structural children under `left` and `right`**, not as a single
uniform module. Consumers must **not** treat the collection as a single
uniform nucleus — it is a **distributed collection** of functionally
distinct nuclei.
**Boundary status (NOT the whole cranial-nerve system — only the PONTINE
subset):** **Boundary case — the cranial_nerve_nuclei is only the PONTINE
cranial-nerve nuclei, not the whole cranial-nerve system.** The **twelve
cranial nerves** have nuclei distributed across the **midbrain**, the
**pons**, and the **medulla**. The **cranial_nerve_nuclei** (here) are the
**pontine** nuclei only — **CN V (chief sensory + motor)**, **CN VI**,
**CN VII (facial + superior salivatory)**, and **CN VIII (cochlear +
vestibular)**. Consumers must **not** conflate the pontine nuclei with the
**whole cranial-nerve system** — the midbrain and medullary nuclei are
**wired elsewhere**.
**Boundary status (NOT the solitary nucleus — that is the medullary
visceral-afferent hub):** **Boundary case — the cranial_nerve_nuclei is
NOT the solitary nucleus.** The **solitary nucleus** (nucleus tractus
solitarius, ``.../medulla_oblongata/solitary_nucleus/``) is the
**medullary visceral-afferent hub** for **CN VII, IX, and X** (taste,
visceral sensation, baroreception, respiratory chemoreception). The
**cranial_nerve_nuclei** (here) contains the **superior salivatory
nucleus** (CN VII parasympathetic), but it does **not** contain the
**solitary nucleus** — that is **medullary**. Consumers must **not**
conflate the pontine nuclei with the **solitary nucleus**.
**Boundary status (BILATERAL CONTAINER — left and right are STRUCTURALLY
SYMMETRIC):** **Boundary case — the cranial_nerve_nuclei is a BILATERAL
container.** The **left** and **right** containers are **structurally
symmetric** — same six nuclei under each, same leaf status for each
nucleus, same bilateral framing. The bilateral symmetry is **strict**.
Consumers must **not** assume a left/right asymmetry at the
container level — the container is a **strict mirror pair**. Any
lateralization is documented **inside the individual nucleus modules**,
not at the container level.

Overview
--------
The cranial_nerve_nuclei is the **pontine cranial-nerve nuclear
collection** — the **six grey-matter nuclei** in the **pontine tegmentum**
that **give rise to** (motor, parasympathetic) or **receive** (sensory,
special sensory) the **cranial nerves V, VI, VII, and VIII**. It is a
**bilateral container** under the pons, with **left** and **right**
sub-containers, each holding the same six nuclei.

**The cranial_nerve_nuclei is a CONTAINER, NOT a leaf.** Its structural
children are the **left** and **right** containers. The six nuclei are
**structural grandchildren** under each side. The
**vestibulocochlear_nuclei** is itself a **sub-container** with
**cochlear_nuclei** and **vestibular_nuclei** as its children.

**The cranial_nerve_nuclei are the GREY-MATTER NUCLEI, NOT the
cranial-nerve FIBERS.** The **cranial nerves** (CN V, VI, VII, VIII) are
the **white-matter axon bundles** that **travel** to and from the
periphery. The **cranial_nerve_nuclei** (here) are the **grey-matter
neuron clusters** inside the pontine tegmentum. They are **DIFFERENT
STRUCTURES** — the **nuclei** are grey matter; the **nerves** are white
matter.

**The cranial_nerve_nuclei is NOT the whole brainstem or the whole
cranial-nerve system.** It is **only the pontine subset** — **CN V (chief
sensory + motor)**, **CN VI**, **CN VII (facial + superior salivatory)**,
and **CN VIII (cochlear + vestibular)**. The **midbrain** cranial-nerve
nuclei (CN III, IV, mesencephalic V, Edinger-Westphal) and the **medullary**
cranial-nerve nuclei (CN IX, X, XI, XII, inferior salivatory, nucleus
ambiguus, hypoglossal, dorsal motor vagus, solitary) are **wired
elsewhere**.

**The cranial_nerve_nuclei is HETEROGENEOUS.** The six nuclei are
**functionally distinct** — **motor** (abducens, facial, motor trigeminal),
**general sensory** (chief sensory trigeminal), **parasympathetic**
(superior salivatory), and **special sensory** (vestibulocochlear). The
tree wires them as **separate children under `left` and `right`**, not as
a single uniform module.

**The cranial_nerve_nuclei is a strict-mirror bilateral container.** The
**left** and **right** containers are **structurally identical** — same
six nuclei under each, same leaf status for each nucleus, same bilateral
framing. Any lateralization is documented **inside the individual nucleus
modules**, not at the container level.

Nucleus Composition (structural grandchildren, prose)
-----------------------------------------------------
The cranial_nerve_nuclei contains **six nuclei per side**, documented as
**structural grandchildren** under ``left`` and ``right`` (not as direct
structural children of the container):

*   **Abducens nucleus** (``.../cranial_nerve_nuclei/left/abducens_nucleus/``)
    — **somatic motor**; controls the **lateral rectus** muscle (eye
    abduction). CN VI.

*   **Chief sensory trigeminal nucleus**
    (``.../cranial_nerve_nuclei/left/chief_sensory_trigeminal_nucleus/``)
    — **general sensory**; **discriminative touch** from the face. CN V
    (principal sensory nucleus).

*   **Facial nerve nucleus**
    (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) —
    **branchial motor**; controls the **muscles of facial expression**.
    CN VII.

*   **Motor trigeminal nucleus**
    (``.../cranial_nerve_nuclei/left/motor_trigeminal_nucleus/``) —
    **branchial motor**; controls the **muscles of mastication**. CN V.

*   **Superior salivatory nucleus**
    (``.../cranial_nerve_nuclei/left/superior_salivatory_nucleus/``) —
    **parasympathetic**; controls the **lacrimal** and **salivary**
    glands. CN VII.

*   **Vestibulocochlear nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/``) —
    **special sensory**; a **sub-container** with two children:
    *   **Cochlear nuclei** — **hearing** (CN VIII cochlear division).
    *   **Vestibular nuclei** — **balance and spatial orientation** (CN
        VIII vestibular division).

**These nuclei are structural grandchildren, not direct children of the
container.** The container's **direct structural children** are ``left``
and ``right``; the nuclei are children of those bilateral containers.
Consumers resolving nucleus-level detail must go **through** ``left`` or
``right``, not assume the nuclei are direct children of
``cranial_nerve_nuclei``.

The Cranial_Nerve_Nuclei / Cranial Nerves Boundary
--------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Cranial_nerve_nuclei** (this module) — the **grey-matter neuron
    clusters** in the pontine tegmentum.

*   **Cranial nerves V, VI, VII, VIII** — the **white-matter axon
    bundles** that travel to and from the periphery.

**They are DIFFERENT STRUCTURES.** The **nuclei** are the **central
neuronal sources/targets**; the **nerves** are the **peripheral
conduction infrastructure**. Consumers must **not** conflate the two —
the **cranial_nerve_nuclei** are the **nuclei**; the **cranial nerves**
are the **fibers**.

The Cranial_Nerve_Nuclei / Pons Boundary
----------------------------------------
This is the **container vs. parent** boundary:

*   **Cranial_nerve_nuclei** (this module) — the **tegmental grey-matter
    nuclei** only.

*   **Pons** (``.../pons/``) — the **whole metencephalic brainstem
    segment**, including the **basilar pons**, the **pontine tegmentum**,
    the **pontine nuclei**, the **corticospinal/corticobulbar tracts**,
    the **middle cerebellar peduncle**, and the **cranial-nerve nuclei**.

**The cranial_nerve_nuclei is a child of the pons.** Consumers must
**not** conflate the nuclei collection with the **whole pons** — the pons
is much larger, and it hosts many structures that are **not**
cranial-nerve nuclei.

The Cranial_Nerve_Nuclei / Midbrain and Medullary Cranial-Nerve Nuclei Boundary
------------------------------------------------------------------------------
This is the **brainstem-level** boundary:

*   **Cranial_nerve_nuclei** (this module) — the **pontine** nuclei only
    — **CN V (chief sensory + motor)**, **CN VI**, **CN VII (facial +
    superior salivatory)**, **CN VIII (cochlear + vestibular)**.

*   **Midbrain cranial-nerve nuclei** (``.../midbrain/cranial_nerve_nuclei/``)
    — **CN III (oculomotor)**, **CN IV (trochlear)**, **mesencephalic
    trigeminal nucleus (CN V proprioceptive)**, **Edinger-Westphal
    nucleus (CN III parasympathetic)**.

*   **Medullary cranial-nerve nuclei**
    (``.../medulla_oblongata/cranial_nerve_nuclei/``) — **CN IX
    (glossopharyngeal)**, **CN X (vagus)**, **CN XI (accessory)**, **CN
    XII (hypoglossal)**, **inferior salivatory nucleus**, **nucleus
    ambiguus**, **hypoglossal nucleus**, **dorsal motor nucleus of the
    vagus**, **solitary nucleus**.

**They are DIFFERENT BRAINSTEM LEVELS.** Consumers must **not** conflate
the **pontine** cranial-nerve nuclei with the **midbrain** or
**medullary** cranial-nerve nuclei.

The Cranial_Nerve_Nuclei / Trigeminal Complex Boundary
------------------------------------------------------
This is the **partial-complex** boundary:

*   **Cranial_nerve_nuclei** (this module) — contains **only** the
    **chief sensory trigeminal nucleus** (discriminative touch) and the
    **motor trigeminal nucleus** (mastication).

*   **Mesencephalic trigeminal nucleus** (``.../midbrain/...``) —
    **proprioception** (CN V mesencephalic division).

*   **Spinal trigeminal nucleus** (``.../medulla_oblongata/...``) —
    **pain and temperature** (CN V spinal division).

**The trigeminal nuclear complex spans three brainstem levels.** The
**cranial_nerve_nuclei** contains **only the pontine components**.
Consumers must **not** conflate the pontine trigeminal nuclei with the
**whole trigeminal complex** — the mesencephalic and spinal components
are **wired elsewhere**.

The Cranial_Nerve_Nuclei / Cerebellum Boundary
----------------------------------------------
This is the **metencephalic-sibling** boundary:

*   **Cranial_nerve_nuclei** (this module) — the **pontine** cranial-nerve
    nuclei.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the **other
    metencephalic structure**, with its **own nuclei** (dentate,
    fastigial, interposed: emboliform + globose) and its **own cortex**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
**pontine cranial-nerve nuclei** with the **cerebellar nuclei** — they
are **different structures** in **different metencephalic sub-regions**.

The Cranial_Nerve_Nuclei / Other Pontine Structures Boundary
-----------------------------------------------------------
This is the **non-cranial-nerve pontine** boundary:

*   **Cranial_nerve_nuclei** (this module) — **only** the nuclei that
    **give rise to or receive** the **cranial nerves V, VI, VII, VIII**.

*   **Locus coeruleus** (``.../pons/tegmentum/locus_coeruleus/``) — the
    **noradrenergic** nucleus.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) — the
    **visceral/autonomic relay**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **cortico-ponto-cerebellar relay** in the **basilar pons**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate the
cranial-nerve nuclei with **other pontine nuclei** — the locus coeruleus,
the parabrachial area, and the pontine nuclei are **not** cranial-nerve
nuclei, and they are **wired elsewhere**.

The Cranial_Nerve_Nuclei / Solitary Nucleus Boundary
----------------------------------------------------
This is the **visceral-afferent** boundary:

*   **Cranial_nerve_nuclei** (this module) — contains the **superior
    salivatory nucleus** (CN VII parasympathetic), but **not** the
    **solitary nucleus**.

*   **Solitary nucleus** (``.../medulla_oblongata/solitary_nucleus/``) —
    the **medullary visceral-afferent hub** for **CN VII, IX, X** (taste,
    visceral sensation, baroreception, respiratory chemoreception).

**The solitary nucleus is medullary, not pontine.** Consumers must **not**
conflate the pontine nuclei with the **solitary nucleus**.

Function in the Human Brain
---------------------------
The cranial_nerve_nuclei's functions are **the cranial-nerve
sensorimotor and parasympathetic relay** — **NOT a single unified
function**:

*   **Somatic Motor (Abducens Nucleus, CN VI):** Controls the **lateral
    rectus** muscle — **eye abduction**. The abducens nucleus is the
    **sole source** of the lateral rectus motor innervation.

*   **Branchial Motor (Facial Nerve Nucleus, CN VII):** Controls the
    **muscles of facial expression** — the **facial nerve** is the
    **principal motor nerve of the face**.

*   **Branchial Motor (Motor Trigeminal Nucleus, CN V):** Controls the
    **muscles of mastication** — the **motor trigeminal nucleus** is the
    **sole source** of the motor trigeminal innervation.

*   **General Sensory (Chief Sensory Trigeminal Nucleus, CN V):**
    **Discriminative touch** from the face — the **principal sensory
    nucleus** is the **pontine** component of the trigeminal nuclear
    complex.

*   **Parasympathetic (Superior Salivatory Nucleus, CN VII):** Controls
    the **lacrimal** and **salivary** glands — the **superior salivatory
    nucleus** is the **preganglionic parasympathetic** source for the
    facial nerve's autonomic component.

*   **Special Sensory (Vestibulocochlear Nuclei, CN VIII):** The
    **cochlear nuclei** subserve **hearing**; the **vestibular nuclei**
    subserve **balance and spatial orientation**. The
    **vestibulocochlear nuclei** are the **brainstem relay** for the
    **auditory and vestibular** senses.

**The unifying theme:** the cranial_nerve_nuclei is the **pontine
cranial-nerve nuclear collection** — the **grey-matter nuclei** that
**give rise to or receive** the **cranial nerves V, VI, VII, VIII**. It is
**heterogeneous**, **bilateral**, and **strictly mirrored** — the six
nuclei are **functionally distinct**, and they are **structural
grandchildren** under the ``left`` and ``right`` containers.

Associated Disorders
--------------------
The cranial_nerve_nuclei have **no single named clinical syndrome as a
collection** — their clinical associations are **nucleus-specific**:

*   **Abducens Nucleus (CN VI) — Sixth Nerve Palsy:** Lesions cause
    **lateral rectus palsy** — **inability to abduct the eye**,
    **diplopia** on ipsilateral gaze.

*   **Facial Nerve Nucleus (CN VII) — Facial Nerve Palsy (Bell's Palsy,
    Supranuclear Palsy):** Lesions cause **ipsilateral facial weakness**
    — **inability to close the eye**, **facial droop**, **loss of
    forehead wrinkling** (peripheral lesions) versus **forehead sparing**
    (supranuclear lesions).

*   **Motor Trigeminal Nucleus (CN V) — Trigeminal Motor Palsy:**
    Lesions cause **weakness of mastication** — **jaw deviation** toward
    the side of the lesion.

*   **Chief Sensory Trigeminal Nucleus (CN V) — Trigeminal Sensory
    Loss:** Lesions cause **facial sensory loss** — **discriminative
    touch** impairment on the ipsilateral face.

*   **Superior Salivatory Nucleus (CN VII) — Autonomic Facial Palsy:**
    Lesions cause **reduced lacrimation** and **reduced salivation** on
    the ipsilateral side.

*   **Vestibulocochlear Nuclei (CN VIII) — Vestibulocochlear Disorders:**
    Lesions cause **hearing loss** (cochlear nuclei) and
    **vertigo/nystagmus/imbalance** (vestibular nuclei).

*   **No Named "Cranial Nerve Nuclei Syndrome":** The
    cranial_nerve_nuclei is a **heterogeneous collection**, not a
    **single structure** — it has **no named clinical syndrome as a
    collection**. Its clinical relevance is **nucleus-specific**, via the
    **individual cranial-nerve nuclei** and the **cranial nerves** they
    subserve.

**What is NOT here:** The cranial_nerve_nuclei is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala), **fear conditioning** (amygdala
— central nucleus + basolateral nuclei), **Urbach-Wiethe disease**
(amygdala — basolateral nuclei), **Alzheimer's disease** (hippocampus,
nucleus basalis), or **Parkinson's disease** (substantia nigra). Its
clinical relevance is **cranial-nerve-specific**, via the **individual
nuclei** and the **cranial nerves** they subserve. **No named
cranial_nerve_nuclei syndrome exists as a collection.**

Lateralization Notes
--------------------
This is the **bilateral** cranial_nerve_nuclei container. The
cranial_nerve_nuclei is **bilaterally symmetric** and **strictly
mirrored** — and it carries **NO warning at the container level**:

*   **Strict Bilateral Symmetry:** The **left** and **right** containers
    are **structurally identical** — same six nuclei under each, same
    leaf status for each nucleus, same bilateral framing. The bilateral
    symmetry is **strict**.

*   **Lateralization is Nucleus-Specific (Contested, Documented in the
    Nucleus Modules):** Any functional lateralization (e.g. facial motor
    control, vestibular asymmetry, auditory lateralization) is
    documented **inside the individual nucleus modules**, not at the
    container level. Consumers must **not** assume a container-level
    lateralization — the container is a **strict mirror pair**.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The
    cranial_nerve_nuclei is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the
    cranial_nerve_nuclei.

*   **NO Amygdala-Lateralization Warning of their own (the
    cranial_nerve_nuclei is MODULATORY-AGNOSTIC, not the fear-output):**
    The **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). The cranial_nerve_nuclei is a
    **cranial-nerve nuclear collection** — consumers must **not** conflate
    it with the **amygdala** or with the **fear circuit**. The
    **cranial_nerve_nuclei** is **SLEA-free** and **amygdala-agnostic**.

**A consumer that assumes "left cranial_nerve_nuclei = right
cranial_nerve_nuclei" will be structurally correct** — the two sides are
**strictly symmetric** (any lateralization is documented in the nucleus
modules). The cranial_nerve_nuclei is a **strict-mirror pair with NO
warning at the container level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The container is **bilateral**, but
    it does **not** import `left` or `right` at module level — it exposes
    them as **structural children** and lets consumers resolve them
    through the memory/recall layer.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../medulla_oblongata/``,
    ``.../metencephalon/cerebellum/``, or any other container. The
    cranial_nerve_nuclei's relationships to the **midbrain** and
    **medullary** cranial-nerve nuclei, the **cerebellum**, the
    **locus coeruleus**, the **parabrachial area**, and the **pontine
    nuclei** are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — structural children `left` and `right`.** The
    six nuclei are **structural grandchildren** under each side. The
    **vestibulocochlear_nuclei** is itself a **sub-container** with
    **cochlear_nuclei** and **vestibular_nuclei** as its children.
*   **GREY-MATTER NUCLEI — NOT the cranial-nerve FIBERS.** The
    **cranial_nerve_nuclei** are the **grey-matter neuron clusters**; the
    **cranial nerves V, VI, VII, VIII** are the **white-matter axon
    bundles**. Consumers must **not** conflate the two.
*   **NOT the whole brainstem or the whole cranial-nerve system — only
    the PONTINE subset.** The **midbrain** and **medullary**
    cranial-nerve nuclei are **wired elsewhere**.
*   **NOT a single functional system — MULTIPLE nuclei.** The **abducens
    nucleus**, **facial nerve nucleus**, **motor trigeminal nucleus**,
    **chief sensory trigeminal nucleus**, **superior salivatory
    nucleus**, and **vestibulocochlear nuclei** are **functionally
    distinct**.
*   **NOT the mesencephalic or spinal trigeminal nucleus — the trigeminal
    system spans levels.** The **cranial_nerve_nuclei** contains **only
    the pontine trigeminal components** (chief sensory + motor).
*   **NOT the trigeminal ganglion or any sensory ganglion — those are
    PERIPHERAL.** The **nuclei** are **central**; the **ganglia** are
    **peripheral**.
*   **NOT the cerebellum — that is the metencephalic sibling.** The
    **cerebellar nuclei** (dentate, fastigial, interposed) are **wired
    elsewhere**.
*   **NOT the solitary nucleus — that is the medullary visceral-afferent
    hub.** The **superior salivatory nucleus** is here, but the
    **solitary nucleus** is not.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    cranial_nerve_nuclei is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **BILATERAL CONTAINER — left and right are STRUCTURALLY SYMMETRIC.**
    The **left** and **right** containers are a **strict-mirror pair**
    with **no warning at the container level**. Any lateralization is
    documented **inside the individual nucleus modules**.
*   **No ``AREA_PATHS`` hop.** The cranial_nerve_nuclei is a local
    container under the pons, not a cross-listed container.
*   **No nested cross-listing.** The cranial_nerve_nuclei has no nested
    dual-framing module. It is a single bilateral container.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import cranial_nerve_nuclei

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei"
    )

**Do not** assume the cranial_nerve_nuclei is a **leaf**. It is a
**container** — its structural children are ``left`` and ``right``, each
of which is a **container** for six nuclei.

**Do not** assume the six nuclei are **direct structural children** of
``cranial_nerve_nuclei``. They are **structural grandchildren** under
``left`` and ``right``.

**Do not** assume the cranial_nerve_nuclei is the **cranial nerves V, VI,
VII, VIII**. The **nerves** are the **white-matter axon bundles**; the
**nuclei** are the **grey-matter neuron clusters**. They are **different
structures**.

**Do not** assume the cranial_nerve_nuclei is the **whole brainstem** or
the **whole cranial-nerve system**. It is **only the pontine subset** —
the **midbrain** and **medullary** cranial-nerve nuclei are **wired
elsewhere**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the cranial_nerve_nuclei. **The cranial_nerve_nuclei is
SLEA-FREE** and **amygdala-agnostic**.

Iterating the cranial_nerve_nuclei's structural children (recommended
consumer pattern)::

    CRANIAL_NERVE_NUCLEI_CHILDREN = ("left", "right")
    # The container is bilateral. The six nuclei are structural
    # grandchildren under each side.

Iterating the cranial_nerve_nuclei's nuclei (recommended consumer
pattern — through `left` or `right`)::

    for side in ("left", "right"):
        for nucleus in (
            "abducens_nucleus",
            "chief_sensory_trigeminal_nucleus",
            "facial_nerve_nucleus",
            "motor_trigeminal_nucleus",
            "superior_salivatory_nucleus",
            "vestibulocochlear_nuclei",
        ):
            nucleus_path = (
                f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
                f"{side}.{nucleus}"
            )
            # resolve nucleus_path through the memory/recall layer

Reaching the vestibulocochlear_nuclei's sub-children (recommended
consumer pattern — the sub-container)::

    for side in ("left", "right"):
        for sub in ("cochlear_nuclei", "vestibular_nuclei"):
            sub_path = (
                f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
                f"{side}.vestibulocochlear_nuclei.{sub}"
            )
            # resolve sub_path through the memory/recall layer

Reaching the midbrain cranial-nerve nuclei (recommended consumer pattern
— NOTE the brainstem-level boundary)::

    # The midbrain hosts CN III, IV, mesencephalic V, Edinger-Westphal:
    #
    #   hindbrain.midbrain.cranial_nerve_nuclei
    #
    # The cranial_nerve_nuclei is only the PONTINE subset.

Reaching the medullary cranial-nerve nuclei (recommended consumer pattern
— NOTE the brainstem-level boundary)::

    # The medulla hosts CN IX, X, XI, XII, inferior salivatory, nucleus
    # ambiguus, hypoglossal, dorsal motor vagus, solitary:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei
    #
    # The cranial_nerve_nuclei is only the PONTINE subset.

Reaching the cerebellum (recommended consumer pattern — NOTE the
metencephalic-sibling boundary)::

    # The cerebellum is the other metencephalic structure — it has its
    # own nuclei (dentate, fastigial, interposed):
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cranial_nerve_nuclei is the PONTINE nuclear collection, not the
    # cerebellum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cnn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei.{side}"
        )
        # resolve cnn_path through the memory/recall layer

Cranial-nerve-specific detail (not wired — consult references)::

    # The six nuclei and their functions:
    #   abducens_nucleus           -> CN VI, lateral rectus (eye abduction)
    #   facial_nerve_nucleus       -> CN VII, facial expression
    #   motor_trigeminal_nucleus   -> CN V, mastication
    #   chief_sensory_trigeminal_nucleus -> CN V, discriminative touch
    #   superior_salivatory_nucleus -> CN VII, lacrimal/salivary glands
    #   vestibulocochlear_nuclei   -> CN VIII, hearing (cochlear) + balance (vestibular)
    #
    # Do not attempt to resolve these as direct children of
    # cranial_nerve_nuclei — they are children of `left` or `right`.

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Pontine
    cranial-nerve nuclei in overview.)
*   **Cranial nerve nuclei — general:** Haines, D.E. (2012).
    *Neuroanatomy: An Atlas of Structures, Sections, and Systems*, 8th
    ed. (Cranial-nerve nuclei of the pons.)
*   **Trigeminal system:** Usunoff, K.G., Marani, E., Schoen, J.H.R.
    (2006). "The trigeminal system." *Advances in Anatomy, Embryology,
    and Cell Biology* 184:1–146. (Chief sensory trigeminal nucleus and
    the trigeminal nuclear complex across brainstem levels.)
*   **Facial nerve and nucleus:** May, M., Schaitkin, B.M. (2000). *The
    Facial Nerve*, 2nd ed. (Facial nerve nucleus and the facial motor
    system.)
*   **Abducens nucleus and sixth nerve palsy:** Leigh, R.J., Zee, D.S.
    (2015). *The Neurology of Eye Movements*, 5th ed. (Abducens nucleus
    and lateral rectus control.)
*   **Vestibulocochlear system:** Kandel, E.R., Schwartz, J.H., Jessell,
    T.M., Siegelbaum, S.A., Hudspeth, A.J. (2013). *Principles of Neural
    Science*, 5th ed. (Cochlear and vestibular nuclei — hearing and
    balance.)
*   **Superior salivatory nucleus:** Loewy, A.D., Spyer, K.M. (1990).
    *Central Regulation of Autonomic Functions*. (Superior salivatory
    nucleus and the parasympathetic outflow of CN VII.)
*   **Cranial-nerve nuclei across brainstem levels (contrast — the
    midbrain and medullary nuclei are wired elsewhere):** Nieuwenhuys,
    R., Voogd, J., van Huijzen, C. (2008). *The Human Central Nervous
    System: A Synopsis and Atlas*, 4th ed. (Cranial-nerve nuclei of the
    midbrain, pons, and medulla.)
*   **Trigeminal ganglion (contrast — the peripheral ganglion):**
    Standring, S. (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Trigeminal ganglion and the peripheral
    trigeminal system.)
*   **Cerebellar nuclei (contrast — the metencephalic sibling):**
    Manto, M., Gruol, D.L., Schmahmann, J.D., Koibuchi, N., Rossi, F.
    (eds.) (2013). *Handbook of the Cerebellum and Cerebellar
    Disorders*. (Cerebellar nuclei — dentate, fastigial, interposed.)
*   **Solitary nucleus (contrast — the medullary visceral-afferent
    hub):** Saper, C.B. (2002). "The central autonomic nervous system:
    conscious visceral perception and autonomic function." *Annual
    Review of Neuroscience* 25:433–469. (Solitary nucleus and the
    medullary visceral-afferent system.)
*   **SLEA (contrast — the cranial_nerve_nuclei is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the
    cranial_nerve_nuclei.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the cranial_nerve_nuclei.)
*   NeuroNames — Cranial nerve nuclei (pons); FMA — Cranial nerve
    nuclei of the pons.
"""
