"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.right.motor_trigeminal_nucleus
========================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── right
                    └── motor_trigeminal_nucleus   <-- THIS MODULE

**Primary synonym:** Right motor trigeminal nucleus; right masticatory
nucleus; right motor nucleus of the trigeminal nerve; right CN V motor
nucleus; right trigeminal motor nucleus; "the right mastication motor
nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem branchial motor nucleus** — a **grey-matter neuron cluster**
in the **right mid-pontine tegmentum**, **medial** to the **right chief
sensory trigeminal nucleus** and **lateral** to the **right abducens
nucleus** and **right facial colliculus**. It is the **sole source** of
the **right motor trigeminal root** (the **motor division** of right
CN V) — the **motor innervation of the right muscles of mastication** and
the **right tensor tympani** and **right tensor veli palatini**.
**Part of:** The **right** container of the **cranial_nerve_nuclei**
container — specifically, the **branchial motor** component. The
**right** container is the **right-side half** of the pontine
cranial-nerve nuclear collection.
**Structural parent:** ``.../cranial_nerve_nuclei/right/`` → **direct
child** of the right container.
**Structural children:** **None.** This is a **leaf** module. The
**masticatory motoneurons** (masseter, temporalis, medial pterygoid,
lateral pterygoid) and the **accessory motoneurons** (mylohyoid,
anterior belly of the digastric, tensor tympani, tensor veli palatini)
are documented as **prose**, not as structural children — they are the
**two functionally distinct populations** within the nucleus.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
motor trigeminal nucleus is a LEAF, not a container.** It has **no
structural children**. The **masticatory motoneurons** and **accessory
motoneurons** are **prose** populations, not structural children.
Consumers must **not** treat the motor trigeminal nucleus as a container,
and must **not** assume the masticatory or accessory populations exist as
sub-modules.
**Boundary status (GREY-MATTER NUCLEUS — NOT the motor trigeminal NERVE
ROOT):** **Boundary case — the motor trigeminal nucleus is the
GREY-MATTER NUCLEUS, NOT the motor trigeminal nerve root (the motor
division of right CN V).** The **right motor trigeminal root** is the
**white-matter axon bundle** that **leaves** the right motor trigeminal
nucleus and **travels** — **alongside but separate from** the **right
chief sensory trigeminal root** — to the **right muscles of mastication**
via the **mandibular division (V3)** of the right trigeminal nerve. The
**motor trigeminal nucleus** (here) is the **grey-matter neuron cluster**
that **gives rise to** those axons. They are **DIFFERENT STRUCTURES** —
the **nucleus** is grey matter; the **root** is white matter. Consumers
must **not** conflate the **nucleus** with the **motor root** — the
nucleus is the **central neuronal source**; the root is the **peripheral
conduction infrastructure**.
**Boundary status (NOT the chief sensory trigeminal nucleus — that is a
SIBLING, and it is SENSORY):** **Boundary case — the motor trigeminal
nucleus is NOT the chief sensory trigeminal nucleus; the chief sensory
trigeminal nucleus is a SIBLING under the right container, and it is
SENSORY.** The **right chief sensory trigeminal nucleus**
(``.../cranial_nerve_nuclei/right/chief_sensory_trigeminal_nucleus/``) is
the **general sensory** nucleus for **discriminative touch** from the
**right face**. The **right motor trigeminal nucleus** (here) is the
**branchial motor** nucleus for the **right muscles of mastication**.
They are **DIFFERENT STRUCTURES** — one is **motor**, the other is
**sensory**; they subserve **different functional systems** and
**different peripheral targets**. They are **adjacent** in the pontine
tegmentum and **both** belong to the **trigeminal system (CN V)** — this
anatomical and functional proximity is a **classic source of confusion**
— consumers must **not** conflate the **motor trigeminal nucleus** with
the **chief sensory trigeminal nucleus**.
**Boundary status (NOT the mesencephalic trigeminal nucleus — that is
MIDBRAIN, and it is the PROPRIOCEPTIVE AFFERENT for the jaw jerk):**
**Boundary case — the motor trigeminal nucleus is NOT the mesencephalic
trigeminal nucleus.** The **right mesencephalic trigeminal nucleus**
(``.../midbrain/tegmentum/mesencephalic_trigeminal_nucleus/right/``) is
the **midbrain** component of the right trigeminal nuclear complex — it
contains the **primary proprioceptive afferent cell bodies** from the
**right jaw** and **right periodontal mechanoreceptors**. **These
mesencephalic afferents project to the motor trigeminal nucleus to
complete the monosynaptic jaw jerk reflex** — but the **mesencephalic
nucleus** and the **motor trigeminal nucleus** are **DIFFERENT
STRUCTURES**. **This distinction is functionally load-bearing** — the
**afferent limb** of the jaw jerk is the **mesencephalic trigeminal
nucleus**; the **efferent limb** is the **motor trigeminal nucleus**.
Consumers must **not** conflate the **motor trigeminal nucleus** with the
**mesencephalic trigeminal nucleus**.
**Boundary status (NOT the spinal trigeminal nucleus — that is
MEDULLARY, and it is PAIN/TEMPERATURE):** **Boundary case — the motor
trigeminal nucleus is NOT the spinal trigeminal nucleus.** The **right
spinal trigeminal nucleus**
(``.../medulla_oblongata/spinal_trigeminal_nucleus/right/``) is the
**medullary** component of the right trigeminal nuclear complex — it
subserves **pain and temperature** from the **right face**. The **right
motor trigeminal nucleus** (here) is the **pontine branchial motor**
nucleus for the **right muscles of mastication**. They are **DIFFERENT
STRUCTURES** — different brainstem levels, **different functional
modalities** (motor vs. sensory), different peripheral targets. Consumers
must **not** conflate the **motor trigeminal nucleus** with the **spinal
trigeminal nucleus**.
**Boundary status (NOT the trigeminal ganglion — that is PERIPHERAL and
SENSORY):** **Boundary case — the motor trigeminal nucleus is NOT the
trigeminal ganglion (or any sensory ganglion).** The **right trigeminal
ganglion** (right semilunar / Gasserian ganglion) is a **peripheral
sensory ganglion** outside the brainstem that contains the **right
primary sensory neuron cell bodies** for the right trigeminal nerve. The
**motor trigeminal nucleus** (here) is the **right central grey-matter
branchial motor nucleus**. They are **DIFFERENT STRUCTURES** — the
**ganglion** is peripheral and sensory; the **nucleus** is central and
motor. Consumers must **not** conflate the **central motor nucleus**
with the **peripheral sensory ganglion**.
**Boundary status (NOT the muscles of mastication — those are PERIPHERAL
TARGETS):** **Boundary case — the motor trigeminal nucleus is NOT the
muscles of mastication.** The **right muscles of mastication** — the
**right masseter**, **right temporalis**, **right medial pterygoid**,
**right lateral pterygoid**, **right mylohyoid**, **right anterior belly
of the digastric**, **right tensor tympani**, and **right tensor veli
palatini** — are the **peripheral effector muscles** that **move the
jaw** and **tension the tympanic membrane and soft palate**, and they
are the **targets** of the right motor trigeminal axons. The **motor
trigeminal nucleus** (here) is the **central grey-matter neuron cluster**
that **innervates** them. They are **DIFFERENT STRUCTURES** — the
**nucleus** is central nervous system; the **muscles** are peripheral
effectors. Consumers must **not** conflate the **nucleus** with the
**muscles**.
**Boundary status (NOT the corticobulbar tract — that is the WHITE-MATTER
UPPER-MOTOR INPUT):** **Boundary case — the motor trigeminal nucleus is
NOT the corticobulbar tract.** The **right (and left) corticobulbar
tract** is the **white-matter upper-motor-neuron pathway** that
**projects** from the **motor cortex** to the **motor trigeminal
nucleus** — it carries the **upper-motor-neuron input** that **drives**
the masticatory motor neurons. The **motor trigeminal nucleus** (here) is
the **grey-matter lower-motor-neuron cluster** that **gives rise to** the
**motor trigeminal root**. They are **DIFFERENT STRUCTURES** — the
**corticobulbar tract** is white matter; the **nucleus** is grey matter.
**This distinction is clinically load-bearing** — a **corticobulbar**
(upper-motor-neuron) lesion usually causes **minimal masticatory
weakness** (because the motor trigeminal nucleus receives **bilateral
corticobulbar input**), whereas a **motor trigeminal nucleus** (or motor
root) lesion causes **ipsilateral masticatory weakness** with **jaw
deviation toward the weak side**.
**Boundary status (NOT the trigeminal motor root fibers within V3 — those
are the WHITE-MATTER AXONS):** **Boundary case — the motor trigeminal
nucleus is NOT the trigeminal motor root fibers.** The **right
trigeminal motor root** — the motor division of right CN V — is the
**white-matter axon bundle** that **joins the mandibular division (V3)**
of the right trigeminal nerve and **travels** to the right masticatory
muscles. The **motor trigeminal nucleus** (here) is the **grey-matter
neuron cluster** that **gives rise to** those axons. They are
**DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the **root
fibers** are white matter. Consumers must **not** conflate the
**nucleus** with the **motor root fibers**.
**Boundary status (NOT the jaw jerk reflex — that is a CIRCUIT, not a
structure):** **Boundary case — the motor trigeminal nucleus is NOT the
jaw jerk reflex; the jaw jerk reflex is a CIRCUIT.** The **jaw jerk
reflex** (masseter reflex, mandibular reflex) is a **monosynaptic
stretch reflex** whose **afferent limb** is the **right mesencephalic
trigeminal nucleus** (via the **right masseteric nerve**) and whose
**efferent limb** is the **right motor trigeminal nucleus** (via the
**right masseteric nerve** to the **right masseter**). The **motor
trigeminal nucleus** (here) is **one node** in this circuit — the
**efferent limb** — not the circuit itself. Consumers must **not**
conflate the **motor trigeminal nucleus** with the **jaw jerk reflex**.
**Boundary status (NOT the facial nerve nucleus — that is a SIBLING, and
it is FACIAL EXPRESSION, CN VII):** **Boundary case — the motor
trigeminal nucleus is NOT the facial nerve nucleus.** The **right facial
nerve nucleus**
(``.../cranial_nerve_nuclei/right/facial_nerve_nucleus/``) is the
**branchial motor** nucleus for the **right muscles of facial
expression** (CN VII, **2nd branchial arch**). The **right motor
trigeminal nucleus** (here) is the **branchial motor** nucleus for the
**right muscles of mastication** (CN V, **1st branchial arch**). They
are **DIFFERENT STRUCTURES** — different cranial nerves (CN V vs.
CN VII), different branchial-arch origins (arch 1 vs. arch 2), different
peripheral targets (mastication vs. facial expression). Consumers must
**not** conflate the **motor trigeminal nucleus** with the **facial
nerve nucleus**.
**Boundary status (NOT the hypoglossal nucleus — that is MEDULLARY, and
it is TONGUE, CN XII):** **Boundary case — the motor trigeminal nucleus
is NOT the hypoglossal nucleus.** The **right hypoglossal nucleus**
(``.../medulla_oblongata/cranial_nerve_nuclei/right/hypoglossal_nucleus/``)
is the **somatic motor** nucleus for the **right tongue muscles** (right
CN XII). The **right motor trigeminal nucleus** (here) is the **branchial
motor** nucleus for the **right muscles of mastication** (right CN V).
They are **DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different cranial nerves (V vs. XII), different peripheral
targets (mastication vs. tongue movement). Consumers must **not**
conflate the **motor trigeminal nucleus** with the **hypoglossal
nucleus**.
**Boundary status (NOT the nucleus ambiguus — that is MEDULLARY, and it
is PHARYNX/LARYNX, CN IX/X):** **Boundary case — the motor trigeminal
nucleus is NOT the nucleus ambiguus.** The **right nucleus ambiguus**
(``.../medulla_oblongata/cranial_nerve_nuclei/right/nucleus_ambiguus/``)
is the **branchial motor** nucleus for the **right pharynx** and **right
larynx** (right CN IX and right CN X). The **right motor trigeminal
nucleus** (here) is the **branchial motor** nucleus for the **right
muscles of mastication** (right CN V). They are **DIFFERENT STRUCTURES**
— different brainstem levels (pons vs. medulla), different cranial
nerves (V vs. IX/X), different peripheral targets (mastication vs.
swallowing and phonation). Consumers must **not** conflate the **motor
trigeminal nucleus** with the **nucleus ambiguus**.
**Boundary status (NOT the abducens nucleus — that is a SIBLING, and it
is SOMATIC MOTOR):** **Boundary case — the motor trigeminal nucleus is
NOT the abducens nucleus.** The **right abducens nucleus**
(``.../cranial_nerve_nuclei/right/abducens_nucleus/``) is the **somatic
motor** nucleus for the **right lateral rectus**. The **right motor
trigeminal nucleus** (here) is the **branchial motor** nucleus for the
**right muscles of mastication**. They are **DIFFERENT STRUCTURES** —
different functional systems (somatic motor vs. branchial motor),
different peripheral targets (eye abduction vs. jaw movement). They are
**both CN V–adjacent structures in the pontine tegmentum**, but they are
**functionally distinct** — consumers must **not** conflate the **motor
trigeminal nucleus** with the **abducens nucleus**.
**Boundary status (NOT a single uniform neuron population —
SOMATOTOPICALLY ORGANIZED into MASTICATORY and ACCESSORY populations):**
**Boundary case — the motor trigeminal nucleus is NOT a single uniform
neuron population; it contains TWO functionally distinct populations
organized SOMATOTOPICALLY along the dorsomedial-to-ventrolateral axis.**
The **accessory motoneurons** — the **mylohyoid**, **anterior belly of
the digastric**, **tensor tympani**, and **tensor veli palatini** — lie
**dorsomedially**. The **masticatory motoneurons** — the **masseter**,
**temporalis**, **medial pterygoid**, and **lateral pterygoid** — lie
**ventrolaterally**. This **somatotopic organization** is **prose**, not
structural children. Consumers must **not** treat the motor trigeminal
nucleus as a single uniform population — it is a **two-population,
somatotopically organized nucleus**.
**Boundary status (NOT the whole cranial_nerve_nuclei container — a leaf
child of the right container):** **Boundary case — the motor trigeminal
nucleus is a LEAF child of the right container, not the container itself,
and not the whole cranial_nerve_nuclei container.** The **right**
container contains the **motor trigeminal nucleus** and **five other
children**. The **cranial_nerve_nuclei** container contains **two
structural children** (``left`` and ``right``). Consumers must **not**
conflate the motor trigeminal nucleus with the **right** container or the
**cranial_nerve_nuclei** container.
**Boundary status (NOT the left motor trigeminal nucleus — strict
mirror, no warning):** **Boundary case — the right motor trigeminal
nucleus is NOT the left motor trigeminal nucleus; the two are a STRICT
MIRROR PAIR with NO warning at the nucleus level.** The **left motor
trigeminal nucleus**
(``.../cranial_nerve_nuclei/left/motor_trigeminal_nucleus/``) is the
**structurally identical** left-side counterpart — same branchial motor
function, same masticatory/accessory populations, same leaf status, same
bilateral framing. The two sides are **strictly mirrored** — any
lateralization is documented **here, in the Lateralization Notes**, not
imported from elsewhere. Consumers must **not** import a lateralization
warning into the right motor trigeminal nucleus — there is **none at the
nucleus level** beyond the **bilateral corticobulbar input** documented
below.
**Boundary status (SLEA-FREE — the motor trigeminal nucleus is NOT an
extended-amygdala component):** **Boundary case — the motor trigeminal
nucleus is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **motor trigeminal nucleus** is a **branchial motor
brainstem nucleus** — it is **NOT** an extended-amygdala component, and
it carries **NO SLEA warning**. Consumers must **not** import the SLEA
warning into the motor trigeminal nucleus — it is **SLEA-free**.

Overview
--------
The motor trigeminal nucleus is the **branchial motor** nucleus for the
**right muscles of mastication** — the **sole source** of the **right
motor trigeminal root** (the **motor division** of right CN V). It is a
**leaf** module under the right container of the cranial_nerve_nuclei
container, and it contains **two functionally distinct populations**
organized somatotopically: the **accessory motoneurons** (mylohyoid,
anterior digastric, tensor tympani, tensor veli palatini; dorsomedial)
and the **masticatory motoneurons** (masseter, temporalis, medial
pterygoid, lateral pterygoid; ventrolateral).

**The motor trigeminal nucleus is the GREY-MATTER NUCLEUS, NOT the motor
trigeminal NERVE ROOT.** The **motor trigeminal root** (the motor
division of right CN V) is the **white-matter axon bundle** that **joins
V3** and **travels** to the right masticatory muscles. The **motor
trigeminal nucleus** (here) is the **grey-matter neuron cluster** that
**gives rise to** those axons. They are **DIFFERENT STRUCTURES** — the
**nucleus** is grey matter; the **root** is white matter.

**The motor trigeminal nucleus is NOT the chief sensory trigeminal
nucleus.** The **chief sensory trigeminal nucleus** is a **sibling**
under the right container — the **general sensory** nucleus for
**discriminative touch** from the right face. They are **adjacent** in
the pontine tegmentum and **both** belong to the **trigeminal system
(CN V)** — this proximity is a **classic source of confusion** —
consumers must **not** conflate the **motor trigeminal nucleus** with the
**chief sensory trigeminal nucleus**.

**The motor trigeminal nucleus is the EFFERENT LIMB of the jaw jerk
reflex.** The **afferent limb** is the **mesencephalic trigeminal
nucleus** (which contains the primary proprioceptive afferent cell
bodies). The **motor trigeminal nucleus** is **one node** in the
**monosynaptic jaw jerk circuit** — the **efferent limb** — not the
circuit itself. Consumers must **not** conflate the **motor trigeminal
nucleus** with the **jaw jerk reflex** or with the **mesencephalic
trigeminal nucleus**.

**The motor trigeminal nucleus is a TWO-POPULATION nucleus organized
SOMATOTOPICALLY.** The **accessory motoneurons** (mylohyoid, anterior
digastric, tensor tympani, tensor veli palatini) lie **dorsomedially**;
the **masticatory motoneurons** (masseter, temporalis, medial pterygoid,
lateral pterygoid) lie **ventrolaterally**. This somatotopic organization
is **prose**, not structural children — the motor trigeminal nucleus is a
**leaf** with **no structural children**.

**The motor trigeminal nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Neuron Population Composition (prose, not structural children)
---------------------------------------------------------------
The motor trigeminal nucleus is a **two-population nucleus** organized
**somatotopically** along the **dorsomedial-to-ventrolateral axis** —
documented as **prose**, not as structural children:

*   **Accessory motoneurons (dorsomedial)** — the **branchial motor**
    neurons that innervate the **accessory masticatory muscles** — the
    **right mylohyoid** (elevates the hyoid and floor of the mouth
    during swallowing), the **right anterior belly of the digastric**
    (depresses the mandible), the **right tensor tympani** (dampens the
    ossicular chain in response to loud sounds — the **tympanic
    reflex**), and the **right tensor veli palatini** (tenses the soft
    palate during swallowing and yawning). These are **not** the
    principal jaw-closing muscles — they are **accessory branchial-
    arch-1 muscles**.

*   **Masticatory motoneurons (ventrolateral)** — the **branchial
    motor** neurons that innervate the **principal muscles of
    mastication** — the **right masseter** (elevates the mandible), the
    **right temporalis** (elevates and retracts the mandible), the
    **right medial pterygoid** (elevates and protrudes the mandible),
    and the **right lateral pterygoid** (protrudes the mandible and
    opens the jaw — **the only jaw-opening muscle innervated by CN V**).
    These are the **principal jaw-closing and jaw-opening muscles**.

**These populations are prose, not structural children.** The tree wires
the **motor trigeminal nucleus** as a **single leaf** under the right
container — the **accessory motoneurons** and **masticatory motoneurons**
are **prose**, not structural children. Consumers that need
**neuron-population-level** resolution should consult the references, not
the tree.

The Motor Trigeminal Nucleus / Motor Trigeminal Nerve Root Boundary
-------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Motor trigeminal nucleus** (this module) — the **grey-matter
    neuron cluster** in the right pontine tegmentum.

*   **Motor trigeminal nerve root** — the **white-matter axon bundle**
    (the motor division of right CN V) that **joins V3** and travels to
    the right masticatory muscles.

**They are DIFFERENT STRUCTURES.** The **nucleus** is the **central
neuronal source**; the **root** is the **peripheral conduction
infrastructure**. Consumers must **not** conflate the two — the **motor
trigeminal nucleus** is the **nucleus**; the **motor trigeminal root**
is the **nerve**.

The Motor Trigeminal Nucleus / Chief Sensory Trigeminal Nucleus Boundary
-----------------------------------------------------------------------
This is the **trigeminal sibling** boundary — **branchial motor vs.
general sensory**:

*   **Motor trigeminal nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of mastication**.

*   **Chief sensory trigeminal nucleus**
    (``.../cranial_nerve_nuclei/right/chief_sensory_trigeminal_nucleus/``)
    — the **general sensory** nucleus for **discriminative touch** from
    the **right face**.

**They are DIFFERENT STRUCTURES** — one is **motor**, the other is
**sensory**; they subserve **different functional systems** and
**different peripheral targets**. They are **adjacent** in the pontine
tegmentum and **both** belong to the **trigeminal system (CN V)** — this
proximity is a **classic source of confusion** — consumers must **not**
conflate the **motor trigeminal nucleus** with the **chief sensory
trigeminal nucleus**.

The Motor Trigeminal Nucleus / Mesencephalic Trigeminal Nucleus Boundary
------------------------------------------------------------------------
This is the **jaw jerk reflex** boundary — **efferent vs. afferent**:

*   **Motor trigeminal nucleus** (this module) — the **EFFERENT limb**
    of the jaw jerk reflex — the **branchial motor** nucleus that
    **closes the jaw** in response to stretch of the masseter.

*   **Mesencephalic trigeminal nucleus**
    (``.../midbrain/tegmentum/mesencephalic_trigeminal_nucleus/right/``)
    — the **AFFERENT limb** of the jaw jerk reflex — the **midbrain**
    nucleus containing the **primary proprioceptive afferent cell
    bodies** from the right jaw and right periodontal mechanoreceptors.

**They are DIFFERENT STRUCTURES** — the **mesencephalic trigeminal
nucleus** is the **afferent limb**; the **motor trigeminal nucleus** is
the **efferent limb**. **This distinction is functionally load-bearing**
— a **mesencephalic trigeminal** lesion **abolishes the jaw jerk reflex**
(afferent limb lost); a **motor trigeminal** lesion **abolishes the jaw
jerk reflex AND causes masticatory weakness** (efferent limb lost).
Consumers must **not** conflate the **motor trigeminal nucleus** with the
**mesencephalic trigeminal nucleus**.

The Motor Trigeminal Nucleus / Spinal Trigeminal Nucleus Boundary
-----------------------------------------------------------------
This is the **brainstem-level** boundary — **pons vs. medulla**, and
**motor vs. pain/temperature**:

*   **Motor trigeminal nucleus** (this module) — the **pontine branchial
    motor** nucleus for the **right muscles of mastication**.

*   **Spinal trigeminal nucleus**
    (``.../medulla_oblongata/spinal_trigeminal_nucleus/right/``) — the
    **medullary** (and caudal pontine) component; **pain and
    temperature** from the **right face**.

**They are DIFFERENT STRUCTURES** — different brainstem levels,
**different functional modalities** (motor vs. sensory), different
peripheral targets. Consumers must **not** conflate the **motor
trigeminal nucleus** with the **spinal trigeminal nucleus**.

The Motor Trigeminal Nucleus / Trigeminal Ganglion Boundary
-----------------------------------------------------------
This is the **central vs. peripheral** boundary — **motor vs. sensory**:

*   **Motor trigeminal nucleus** (this module) — the **central
    grey-matter branchial motor nucleus**.

*   **Trigeminal ganglion** (right semilunar / Gasserian ganglion) — the
    **peripheral sensory ganglion** containing the **right primary
    sensory neuron cell bodies** for the right trigeminal nerve.

**They are DIFFERENT STRUCTURES** — the **ganglion** is peripheral and
sensory; the **nucleus** is central and motor. Consumers must **not**
conflate the **central motor nucleus** with the **peripheral sensory
ganglion**.

The Motor Trigeminal Nucleus / Muscles of Mastication Boundary
--------------------------------------------------------------
This is the **central vs. peripheral** boundary:

*   **Motor trigeminal nucleus** (this module) — the **central
    grey-matter neuron cluster**.

*   **Muscles of mastication** — the **peripheral effector muscles** —
    the **masseter**, **temporalis**, **medial pterygoid**, **lateral
    pterygoid**, **mylohyoid**, **anterior belly of the digastric**,
    **tensor tympani**, and **tensor veli palatini** — the **targets**
    of the right motor trigeminal axons.

**They are DIFFERENT STRUCTURES** — the **nucleus** is central nervous
system; the **muscles** are peripheral effectors. Consumers must **not**
conflate the **nucleus** with the **muscles**.

The Motor Trigeminal Nucleus / Corticobulbar Tract Boundary
-----------------------------------------------------------
This is the **grey-matter vs. white-matter UPPER-MOTOR-NEURON** boundary:

*   **Motor trigeminal nucleus** (this module) — the **grey-matter
    lower-motor-neuron cluster** that **gives rise to** the **motor
    trigeminal root**.

*   **Corticobulbar tract** — the **white-matter upper-motor-neuron
    pathway** that **projects** from the **motor cortex** to the
    **motor trigeminal nucleus**.

**They are DIFFERENT STRUCTURES** — the **corticobulbar tract** is white
matter; the **nucleus** is grey matter. **This distinction is clinically
load-bearing** — the motor trigeminal nucleus receives **bilateral
corticobulbar input**, so a **corticobulbar** (upper-motor-neuron)
lesion usually causes **minimal masticatory weakness** (the intact
contralateral projection is sufficient), whereas a **motor trigeminal
nucleus** (or motor root) lesion causes **ipsilateral masticatory
weakness** with **jaw deviation toward the weak side**. Consumers must
**not** conflate the **motor trigeminal nucleus** with the
**corticobulbar tract**.

The Motor Trigeminal Nucleus / Trigeminal Motor Root Fibers in V3 Boundary
--------------------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the motor root
**travels within V3**:

*   **Motor trigeminal nucleus** (this module) — the **grey-matter neuron
    cluster** that **gives rise to** the motor trigeminal axons.

*   **Trigeminal motor root fibers in V3** — the **white-matter axons**
    that **travel within the mandibular division (V3)** of the right
    trigeminal nerve to reach the right masticatory muscles.

**They are DIFFERENT STRUCTURES** — the **nucleus** is grey matter; the
**root fibers in V3** are white matter. Consumers must **not** conflate
the **nucleus** with the **motor root fibers**.

The Motor Trigeminal Nucleus / Jaw Jerk Reflex Boundary
-------------------------------------------------------
This is the **structure vs. circuit** boundary:

*   **Motor trigeminal nucleus** (this module) — **one node** in the jaw
    jerk circuit — the **efferent limb**.

*   **Jaw jerk reflex** — the **monosynaptic stretch reflex** whose
    **afferent limb** is the **mesencephalic trigeminal nucleus** (via
    the right masseteric nerve) and whose **efferent limb** is the
    **motor trigeminal nucleus** (via the right masseteric nerve to the
    right masseter).

**They are DIFFERENT CONCEPTS** — the **motor trigeminal nucleus** is a
**structure**; the **jaw jerk reflex** is a **circuit**. Consumers must
**not** conflate the **motor trigeminal nucleus** with the **jaw jerk
reflex**.

The Motor Trigeminal Nucleus / Facial Nerve Nucleus Boundary
------------------------------------------------------------
This is the **branchial motor sibling** boundary — **CN V vs. CN VII**:

*   **Motor trigeminal nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of mastication** (right CN V, **1st
    branchial arch**).

*   **Facial nerve nucleus**
    (``.../cranial_nerve_nuclei/right/facial_nerve_nucleus/``) — the
    **branchial motor** nucleus for the **right muscles of facial
    expression** (right CN VII, **2nd branchial arch**).

**They are DIFFERENT STRUCTURES** — different cranial nerves (CN V vs.
CN VII), different branchial-arch origins (arch 1 vs. arch 2), different
peripheral targets (mastication vs. facial expression). Consumers must
**not** conflate the **motor trigeminal nucleus** with the **facial
nerve nucleus**.

The Motor Trigeminal Nucleus / Hypoglossal Nucleus Boundary
-----------------------------------------------------------
This is the **brainstem-level** boundary — **pons vs. medulla**, and
**mastication vs. tongue**:

*   **Motor trigeminal nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of mastication** (right CN V).

*   **Hypoglossal nucleus**
    (``.../medulla_oblongata/cranial_nerve_nuclei/right/hypoglossal_nucleus/``)
    — the **somatic motor** nucleus for the **right tongue muscles**
    (right CN XII).

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different cranial nerves (V vs. XII), different peripheral
targets (mastication vs. tongue movement). Consumers must **not**
conflate the **motor trigeminal nucleus** with the **hypoglossal
nucleus**.

The Motor Trigeminal Nucleus / Nucleus Ambiguus Boundary
--------------------------------------------------------
This is the **branchial motor sibling** boundary — **CN V vs. CN IX/X**,
and **pons vs. medulla**:

*   **Motor trigeminal nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of mastication** (right CN V).

*   **Nucleus ambiguus**
    (``.../medulla_oblongata/cranial_nerve_nuclei/right/nucleus_ambiguus/``)
    — the **branchial motor** nucleus for the **right pharynx** and
    **right larynx** (right CN IX and right CN X).

**They are DIFFERENT STRUCTURES** — different brainstem levels (pons vs.
medulla), different cranial nerves (V vs. IX/X), different peripheral
targets (mastication vs. swallowing and phonation). Consumers must **not**
conflate the **motor trigeminal nucleus** with the **nucleus ambiguus**.

The Motor Trigeminal Nucleus / Abducens Nucleus Boundary
--------------------------------------------------------
This is the **sibling** boundary — **branchial motor vs. somatic motor**:

*   **Motor trigeminal nucleus** (this module) — the **branchial motor**
    nucleus for the **right muscles of mastication**.

*   **Abducens nucleus**
    (``.../cranial_nerve_nuclei/right/abducens_nucleus/``) — the
    **somatic motor** nucleus for the **right lateral rectus**.

**They are DIFFERENT STRUCTURES** — different functional systems
(branchial motor vs. somatic motor), different peripheral targets (jaw
movement vs. eye abduction). Consumers must **not** conflate the **motor
trigeminal nucleus** with the **abducens nucleus**.

The Motor Trigeminal Nucleus / Left Motor Trigeminal Nucleus Boundary
---------------------------------------------------------------------
This is the **strict-mirror** boundary:

*   **Right motor trigeminal nucleus** (this module) — the **right-side**
    branchial motor nucleus for the **right muscles of mastication**.

*   **Left motor trigeminal nucleus**
    (``.../cranial_nerve_nuclei/left/motor_trigeminal_nucleus/``) — the
    **structurally identical** left-side branchial motor nucleus for the
    **left muscles of mastication**.

**They are a STRICT MIRROR PAIR with NO warning at the nucleus level.**
The two sides are **structurally identical** — same branchial motor
function, same masticatory/accessory populations, same leaf status, same
bilateral framing. **The bilateral corticobulbar input is a connectivity
fact, not a lateralization warning** — the right motor trigeminal nucleus
receives input from **both** motor cortices, and the left motor
trigeminal nucleus also receives input from **both** motor cortices.
This is **structural**, not a functional lateralization. Consumers must
**not** import a lateralization warning into the right motor trigeminal
nucleus — there is **none at the nucleus level**.

The Motor Trigeminal Nucleus / Cranial Nerve Nuclei Container Boundary
----------------------------------------------------------------------
This is the **leaf vs. container** boundary:

*   **Motor trigeminal nucleus** (this module) — a **leaf** child of the
    **right** container.

*   **Right container** (``.../cranial_nerve_nuclei/right/``) — the
    **right-side half** of the pontine cranial-nerve nuclear collection,
    with **six structural children** (including the motor trigeminal
    nucleus).

*   **Cranial_nerve_nuclei container** (``.../cranial_nerve_nuclei/``) —
    the **whole pontine collection**, with **two structural children**
    (``left`` and ``right``).

**The motor trigeminal nucleus is a leaf child of the right container.**
Consumers must **not** conflate the motor trigeminal nucleus with the
**right** container or the **cranial_nerve_nuclei** container.

The Motor Trigeminal Nucleus / SLEA Boundary
--------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Motor trigeminal nucleus** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The motor trigeminal nucleus is NOT part of the SLEA continuum.** It is
a **branchial motor brainstem nucleus**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the motor
trigeminal nucleus.

Function in the Human Brain
---------------------------
The motor trigeminal nucleus's functions are **the branchial motor
control of the right muscles of mastication** and **the efferent limb of
the jaw jerk reflex** — **NOT a single unified function**:

*   **Masticatory Motor (Masseter, Temporalis, Medial Pterygoid, Lateral
    Pterygoid):** The **masticatory motoneurons** innervate the
    **principal jaw muscles** — the **right masseter** and **right
    temporalis** (jaw elevation), the **right medial pterygoid** (jaw
    elevation and protrusion), and the **right lateral pterygoid** (jaw
    protrusion and opening). Together, these muscles produce **chewing,
    biting, and jaw clenching**.

*   **Accessory Motor (Mylohyoid, Anterior Digastric, Tensor Tympani,
    Tensor Veli Palatini):** The **accessory motoneurons** innervate the
    **accessory masticatory muscles** — the **right mylohyoid** and
    **right anterior belly of the digastric** (hyoid elevation and jaw
    depression during swallowing and speech), the **right tensor
    tympani** (the **tympanic reflex** — dampens the ossicular chain in
    response to loud sounds), and the **right tensor veli palatini**
    (tenses the soft palate during swallowing and yawning).

*   **Efferent Limb of Jaw Jerk Reflex:** The **motor trigeminal
    nucleus** is the **efferent limb** of the **monosynaptic jaw jerk
    reflex** (masseter reflex) — it **receives** the primary
    proprioceptive afferents from the **right mesencephalic trigeminal
    nucleus** and **discharges** the **right masseter motoneurons** to
    **close the jaw** in response to stretch of the masseter.

*   **NOT a neural processor in the classical sense.** The motor
    trigeminal nucleus is a **motor output nucleus** — it **executes**
    the **corticobulbar commands** generated upstream (in the **motor
    cortex**) and the **reflex commands** generated by the **jaw jerk
    circuit** (via the mesencephalic trigeminal nucleus). The
    **processing** of mastication and jaw reflexes happens in the
    **motor cortex**, the **mesencephalic trigeminal nucleus**, and the
    **brainstem central pattern generators**. The motor trigeminal
    nucleus is the **final common pathway** for **jaw movement**.

**The unifying theme:** the motor trigeminal nucleus is the **branchial
motor output nucleus** for the **right muscles of mastication** — the
**final common pathway** for **voluntary jaw movement** and the
**efferent limb** of the **jaw jerk reflex**. It is **two-population**
(masticatory ventrolateral; accessory dorsomedial), **SLEA-free**, and
**NOT the motor trigeminal nerve root** — the **root** is the
**white-matter axon bundle**; the **nucleus** is the **grey-matter
neuron cluster** that **gives rise to** it.

Associated Disorders
--------------------
The motor trigeminal nucleus has **no named "motor trigeminal nucleus
syndrome"** — its clinical associations are **nucleus-specific**, and
they are **distinguishable from upper-motor-neuron (corticobulbar),
nerve-level, and other brainstem-level lesions**:

*   **Motor Trigeminal Nucleus Lesion — Ipsilateral Masticatory
    Weakness with Jaw Deviation:** A lesion of the **right motor
    trigeminal nucleus** causes **right masticatory weakness** — the
    **right masseter**, **right temporalis**, and **right medial
    pterygoid** are weak, and the **right lateral pterygoid** is weak.
    The **clinically salient sign** is **jaw deviation toward the weak
    (right) side** on **mouth opening** — because the **left lateral
    pterygoid** (jaw opening and protrusion) is **unopposed**. The
    **jaw jerk reflex is abolished** (efferent limb lost). **The muscles
    of facial expression are spared** (facial nerve nucleus is intact).

*   **Corticobulbar (Upper-Motor-Neuron) Lesion — Minimal Masticatory
    Weakness, Enhanced Jaw Jerk:** A lesion of the **left motor cortex**
    or **left corticobulbar tract** causes **minimal or no masticatory
    weakness** — the **motor trigeminal nucleus** receives **bilateral
    corticobulbar input**, so the intact ipsilateral projection is
    sufficient. **The jaw jerk reflex is ENHANCED** (the
    **corticobulbar tract** normally **inhibits** the jaw jerk; loss of
    this inhibition causes **hyperreflexia**). **This pattern is the
    hallmark of pseudobulbar palsy** — enhanced jaw jerk with minimal
    masticatory weakness.

*   **Motor Trigeminal Nerve Root Lesion — Ipsilateral Masticatory
    Weakness with Jaw Deviation:** A lesion of the **right motor
    trigeminal root** (the motor division of right CN V) causes
    **clinically identical** masticatory weakness to a nucleus lesion —
    **right masticatory weakness** with **jaw deviation toward the right
    on mouth opening** — because the **final common pathway** is lost at
    the nerve level. **The distinction from a nucleus lesion** is often
    made by **associated brainstem signs** — a **nucleus** lesion may be
    accompanied by **ipsilateral facial sensory loss** (chief sensory
    trigeminal nucleus involvement) or **ipsilateral abducens palsy**
    (abducens nucleus involvement); a **nerve root** lesion is usually
    **isolated**.

*   **Trigeminal Motor Neuropathy (Rare) — Isolated Masticatory
    Weakness:** **Isolated trigeminal motor neuropathy** is a **rare**
    condition causing **unilateral masticatory weakness** without
    sensory loss — it is a **nerve-level** disorder, not a
    **nucleus-level** disorder. Causes include **focal demyelination**,
    **compression**, and **inflammatory neuropathies**.

*   **Lateral Pontine Syndrome (Marie-Foix) — Motor Trigeminal Nucleus
    Involvement:** A lesion of the **right lateral pontine tegmentum**
    involving the **right motor trigeminal nucleus**, the **right chief
    sensory trigeminal nucleus**, the **right spinal trigeminal nucleus**
    (caudal pontine part), the **right facial nerve fibers**, and the
    **right middle cerebellar peduncle** causes **Marie-Foix syndrome**
    — **ipsilateral (right) facial sensory loss** (touch, pain,
    temperature), **ipsilateral (right) masticatory weakness**,
    **ipsilateral (right) facial palsy**, **ipsilateral (right) ataxia**,
    and **contralateral (left) hemiparesis**. The **motor trigeminal
    nucleus** is the **substrate** of the **ipsilateral masticatory
    weakness** component.

*   **Foville Syndrome — Motor Trigeminal Nucleus Sparing:** **Foville
    syndrome** (pontine tegmentum lesion involving the **abducens
    nucleus**/PPRF, **facial nerve fibers**, and **corticospinal
    tract**) **typically spares the motor trigeminal nucleus** — the
    classic Foville lesion is **ventromedial** and does not reach the
    **more lateral** motor trigeminal nucleus. **This is a useful
    anatomical distinction** — **masticatory weakness** suggests a
    **more lateral** pontine lesion (Marie-Foix) than the classic
    **Foville** pattern.

*   **No Named "Motor Trigeminal Nucleus Syndrome":** The motor
    trigeminal nucleus is a **single branchial motor nucleus** — it has
    **no named clinical syndrome of its own**. Its clinical relevance is
    **nucleus-specific**, via the **right muscles of mastication** it
    subserves. **The most important clinical distinction is
    upper-motor-neuron (corticobulbar) vs. lower-motor-neuron (nucleus
    or motor root)** — the **enhanced jaw jerk** of a central lesion
    vs. the **ipsilateral masticatory weakness with jaw deviation and
    abolished jaw jerk** of a peripheral lesion.

**What is NOT here:** The motor trigeminal nucleus is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), **trigeminal neuralgia**
(trigeminal nerve root — sensory, not motor), or **Bell's palsy** (facial
nerve, not trigeminal). Its clinical relevance is
**masticatory-motor-specific**, via the **right muscles of mastication**
it subserves. **No named motor trigeminal nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **right** motor trigeminal nucleus module. The motor
trigeminal nucleus is **bilaterally symmetric** with the left motor
trigeminal nucleus and **strictly mirrored** — and it carries **NO
warning at the nucleus level**:

*   **Strict Bilateral Symmetry:** The **right** and **left** motor
    trigeminal nuclei are **structurally identical** — same branchial
    motor function, same masticatory/accessory populations, same leaf
    status, same bilateral framing. The bilateral symmetry is
    **strict**.

*   **Bilateral Corticobulbar Input (Connectivity Fact, NOT a
    Lateralization Warning):** The **right motor trigeminal nucleus**
    receives **bilateral corticobulbar input** from **both the right and
    left motor cortices**. This is a **structural fact** of the
    **masticatory motor system** — it is the **neural substrate** of
    **minimal masticatory weakness** in **upper-motor-neuron lesions**
    and of the **enhanced jaw jerk** (loss of corticobulbar inhibition).
    It is **not** a functional lateralization.

*   **Unilateral Jaw Deviation Is a Structural Fact, NOT a
    Lateralization Warning:** The **lateral pterygoid** — the **jaw-
    opening and protruding muscle** — is innervated **ipsilaterally** by
    the **motor trigeminal nucleus**. On **mouth opening**, the
    **contralateral lateral pterygoid** (in a unilateral lesion) is
    **unopposed**, causing **jaw deviation toward the weak side**. This
    is a **structural fact** of the **masticatory motor system** — it is
    the **neural substrate** of the **classic clinical sign** of
    masticatory weakness — and it is **not** a functional lateralization.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The motor
    trigeminal nucleus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the SLEA
    warning or the amygdala-lateralization warning into the motor
    trigeminal nucleus.

*   **NO Amygdala-Lateralization Warning of their own (the motor
    trigeminal nucleus is BRANCHIAL MOTOR, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output) and
    the **basolateral nuclei** (fear-learning). The motor trigeminal
    nucleus is a **branchial motor brainstem nucleus** — consumers must
    **not** conflate it with the **amygdala** or with the **fear
    circuit**. **Note**: the "right-amygdala" lateralization is about
    the **amygdala**, not about this right pontine motor nucleus — do
    not import it.

**A consumer that assumes "right motor trigeminal nucleus = left motor
trigeminal nucleus" will be structurally correct** — the two sides are
**strictly symmetric** (the bilateral corticobulbar input and the
unilateral jaw deviation are structural facts, not lateralizations). The
motor trigeminal nucleus is a **strict-mirror pair with NO warning at the
nucleus level** — **no SLEA warning**, **no amygdala-lateralization
warning**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cranial_nerve_nuclei/left/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../cortex/``, or any other container.
    The motor trigeminal nucleus's relationships to the **motor
    trigeminal nerve root**, the **chief sensory trigeminal nucleus**,
    the **mesencephalic trigeminal nucleus**, the **spinal trigeminal
    nucleus**, the **trigeminal ganglion**, the **muscles of
    mastication**, the **corticobulbar tract**, the **trigeminal motor
    root fibers in V3**, the **jaw jerk reflex**, the **facial nerve
    nucleus**, the **hypoglossal nucleus**, the **nucleus ambiguus**,
    and the **abducens nucleus** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **masticatory
    motoneurons** and **accessory motoneurons** are documented as
    **prose**, not as sub-modules. Consumers must not assume any exist
    as children; resolve neuron-population-level detail through the
    references.
*   **GREY-MATTER NUCLEUS — NOT the motor trigeminal NERVE ROOT.** The
    **motor trigeminal nucleus** is the **grey-matter neuron cluster**;
    the **motor trigeminal root** (the motor division of right CN V) is
    the **white-matter axon bundle**. Consumers must **not** conflate
    the two.
*   **NOT the chief sensory trigeminal nucleus — that is a SIBLING and
    it is SENSORY.** The **chief sensory trigeminal nucleus** is the
    **general sensory** CN V sibling; the **motor trigeminal nucleus** is
    the **branchial motor** CN V component. Consumers must **not**
    conflate the two.
*   **NOT the mesencephalic trigeminal nucleus — that is MIDBRAIN and it
    is the AFFERENT limb of the jaw jerk.** The **mesencephalic
    trigeminal nucleus** is the **afferent limb**; the **motor
    trigeminal nucleus** is the **efferent limb**. **This distinction is
    functionally load-bearing** — mesencephalic lesion = abolished jaw
    jerk alone; motor trigeminal lesion = abolished jaw jerk PLUS
    masticatory weakness.
*   **NOT the spinal trigeminal nucleus — that is MEDULLARY and it is
    PAIN/TEMPERATURE.** The **spinal trigeminal nucleus** is the
    medullary sensory component; the **motor trigeminal nucleus** is the
    pontine motor component. Consumers must **not** conflate the two.
*   **NOT the trigeminal ganglion — that is PERIPHERAL and SENSORY.**
    The **ganglion** is peripheral and sensory; the **nucleus** is
    central and motor. Consumers must **not** conflate the two.
*   **NOT the muscles of mastication — those are PERIPHERAL TARGETS.**
    The **nucleus** is central; the **muscles** are peripheral
    effectors. Consumers must **not** conflate the two.
*   **NOT the corticobulbar tract — that is the WHITE-MATTER
    UPPER-MOTOR-NEURON INPUT.** The **corticobulbar tract** is white
    matter; the **nucleus** is grey matter. **This distinction is
    clinically load-bearing** — corticobulbar lesion = minimal
    masticatory weakness with enhanced jaw jerk; motor trigeminal nucleus
    lesion = ipsilateral masticatory weakness with jaw deviation and
    abolished jaw jerk.
*   **NOT the trigeminal motor root fibers in V3 — those are the
    WHITE-MATTER AXONS.** The **motor root fibers in V3** are white
    matter; the **nucleus** is grey matter. Consumers must **not**
    conflate the two.
*   **NOT the jaw jerk reflex — that is a CIRCUIT, not a structure.**
    The **motor trigeminal nucleus** is **one node** in the jaw jerk
    circuit — the **efferent limb** — not the circuit itself. Consumers
    must **not** conflate the two.
*   **NOT the facial nerve nucleus — that is a SIBLING and it is FACIAL
    EXPRESSION (CN VII).** The **facial nerve nucleus** is the
    **branchial motor** nucleus for facial expression (CN VII, arch 2);
    the **motor trigeminal nucleus** is the **branchial motor** nucleus
    for mastication (CN V, arch 1). Consumers must **not** conflate the
    two.
*   **NOT the hypoglossal nucleus — that is MEDULLARY and it is TONGUE
    (CN XII).** The **hypoglossal nucleus** is the **somatic motor**
    nucleus for the tongue; the **motor trigeminal nucleus** is the
    **branchial motor** nucleus for mastication. Consumers must **not**
    conflate the two.
*   **NOT the nucleus ambiguus — that is MEDULLARY and it is
    PHARYNX/LARYNX (CN IX/X).** The **nucleus ambiguus** is the
    **branchial motor** nucleus for the pharynx and larynx; the **motor
    trigeminal nucleus** is the **branchial motor** nucleus for
    mastication. Consumers must **not** conflate the two.
*   **NOT the abducens nucleus — that is a SIBLING and it is SOMATIC
    MOTOR.** The **abducens nucleus** is the **somatic motor** nucleus
    for the lateral rectus; the **motor trigeminal nucleus** is the
    **branchial motor** nucleus for mastication. Consumers must **not**
    conflate the two.
*   **TWO FUNCTIONALLY DISTINCT POPULATIONS — MASTICATORY vs.
    ACCESSORY.** The **masticatory motoneurons** (masseter, temporalis,
    medial pterygoid, lateral pterygoid; ventrolateral) and the
    **accessory motoneurons** (mylohyoid, anterior digastric, tensor
    tympani, tensor veli palatini; dorsomedial) are **prose**, not
    structural children. Consumers must **not** treat the motor
    trigeminal nucleus as a single uniform population.
*   **SLEA-FREE — no extended-amygdala relationship.** The motor
    trigeminal nucleus is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output — the motor trigeminal nucleus is BRANCHIAL
    MOTOR.** The **fear-output** structure is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **motor trigeminal nucleus** is a **branchial motor
    brainstem nucleus** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The motor trigeminal nucleus is a local
    leaf under the right container, not a cross-listed leaf.
*   **No nested cross-listing.** The motor trigeminal nucleus has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left motor trigeminal nucleus — strict
    mirror with NO warning.** Right and left motor trigeminal nucleus
    modules are **structurally identical** — same leaf status, same
    **branchial motor** framing, same **masticatory/accessory
    populations**, same **SLEA-free** status, same **no warning** at the
    nucleus level.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.right import motor_trigeminal_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.right."
        "motor_trigeminal_nucleus"
    )

**Do not** assume the motor trigeminal nucleus is the **motor trigeminal
nerve root**. The **motor trigeminal root** (the motor division of right
CN V) is the **white-matter axon bundle**; the **motor trigeminal
nucleus** is the **grey-matter neuron cluster**. They are **different
structures**.

**Do not** assume the motor trigeminal nucleus is the **chief sensory
trigeminal nucleus**. The **chief sensory trigeminal nucleus** is a
**sibling** under the right container; the **motor trigeminal nucleus** is
the **branchial motor** CN V component; the **chief sensory trigeminal
nucleus** is the **general sensory** CN V component.

**Do not** assume the motor trigeminal nucleus is the **mesencephalic
trigeminal nucleus** or the **jaw jerk reflex**. The **mesencephalic
trigeminal nucleus** is the **afferent limb** of the jaw jerk (in the
midbrain); the **motor trigeminal nucleus** is the **efferent limb** (in
the pons); the **jaw jerk reflex** is the **circuit** that connects them.

**Do not** assume the motor trigeminal nucleus is the **spinal trigeminal
nucleus**, the **trigeminal ganglion**, or the **muscles of
mastication**. Those are **different structures** — the **spinal
trigeminal nucleus** is medullary and sensory (pain/temperature); the
**trigeminal ganglion** is peripheral and sensory; the **muscles** are
peripheral effectors.

**Do not** assume the motor trigeminal nucleus is the **corticobulbar
tract** or the **motor root fibers in V3**. The **corticobulbar tract**
is the **white-matter upper-motor-neuron input**; the **motor root fibers
in V3** are the **white-matter axons** — both are white matter; the
**nucleus** is the **grey-matter lower-motor-neuron cluster**. **This
distinction is clinically load-bearing** — corticobulbar lesion =
minimal masticatory weakness with enhanced jaw jerk; motor trigeminal
nucleus lesion = ipsilateral masticatory weakness with jaw deviation and
abolished jaw jerk.

**Do not** assume the motor trigeminal nucleus is the **facial nerve
nucleus**, the **hypoglossal nucleus**, the **nucleus ambiguus**, or the
**abducens nucleus**. Those are **different motor nuclei** for
**different cranial nerves and different peripheral targets** — facial
expression (CN VII), tongue (CN XII), pharynx/larynx (CN IX/X), and eye
abduction (CN VI), respectively.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the motor trigeminal nucleus. **The motor trigeminal
nucleus is SLEA-FREE** — it is **not** an extended-amygdala component,
and it is **NOT part of the fear circuit**. **Note**: the
"right-amygdala" lateralization is about the **amygdala**, not about this
right pontine motor nucleus — do not import it.

Iterating the motor trigeminal nucleus's (empty) children (recommended
consumer pattern)::

    MOTOR_TRIGEMINAL_NUCLEUS_CHILDREN = ()
    # The motor trigeminal nucleus is a leaf. The masticatory motoneurons
    # and accessory motoneurons are prose, not modules.

Reaching the motor trigeminal nerve root (recommended consumer pattern —
the white-matter axon bundle)::

    # The motor trigeminal root (the motor division of right CN V) is the
    # WHITE-MATTER axon bundle:
    #
    #   peripheral: right motor CN V -> V3 -> right masticatory muscles
    #
    # The nucleus is the CENTRAL neuronal source; the motor root is the
    # PERIPHERAL conduction infrastructure.

Reaching the chief sensory trigeminal nucleus (recommended consumer
pattern — the CN V general sensory sibling)::

    # The chief sensory trigeminal nucleus is the GENERAL SENSORY
    # sibling under the right container:
    #
    #   .../cranial_nerve_nuclei/right/chief_sensory_trigeminal_nucleus/
    #
    # The motor trigeminal nucleus is the BRANCHIAL MOTOR sibling — both
    # are CN V, but different functional components.

Reaching the mesencephalic trigeminal nucleus (recommended consumer
pattern — the AFFERENT limb of the jaw jerk)::

    # The mesencephalic trigeminal nucleus is the MIDBRAIN proprioceptive
    # component of the trigeminal complex:
    #
    #   .../midbrain/tegmentum/mesencephalic_trigeminal_nucleus/right/
    #
    # The mesencephalic trigeminal nucleus is the AFFERENT limb of the
    # jaw jerk; the motor trigeminal nucleus is the EFFERENT limb.

Reaching the jaw jerk reflex circuit (recommended consumer pattern — the
monosynaptic reflex arc)::

    # The jaw jerk reflex is a CIRCUIT, not a structure:
    #
    #   afferent: right masseteric nerve -> right mesencephalic trigeminal
    #             nucleus (primary proprioceptive cell bodies)
    #   efferent: right motor trigeminal nucleus -> right masseteric nerve
    #             -> right masseter
    #
    # The motor trigeminal nucleus is the EFFERENT limb, not the circuit
    # itself.

Reaching the corticobulbar tract (recommended consumer pattern — the
upper-motor-neuron input)::

    # The corticobulbar tract is the WHITE-MATTER upper-motor-neuron
    # pathway:
    #
    #   .../white_matter/.../corticobulbar_tract/  (or equivalent path)
    #
    # The corticobulbar tract PROVIDES INPUT TO the motor trigeminal
    # nucleus; the motor trigeminal nucleus is the LOWER-MOTOR-NEURON
    # OUTPUT.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mtn_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
            f"{side}.motor_trigeminal_nucleus"
        )
        # resolve mtn_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The motor trigeminal nucleus's neuron populations are prose, not
    # modules:
    #   masticatory motoneurons (ventrolateral) -> masseter, temporalis,
    #                                             medial pterygoid,
    #                                             lateral pterygoid
    #   accessory motoneurons (dorsomedial)     -> mylohyoid, anterior
    #                                             belly of digastric,
    #                                             tensor tympani,
    #                                             tensor veli palatini
    #
    # Do not attempt to resolve these as sub-paths of the motor
    # trigeminal nucleus.

References
----------
*   **Canonical trigeminal anatomy:** Usunoff, K.G., Marani, E., Schoen,
    J.H.R. (2006). "The trigeminal system." *Advances in Anatomy,
    Embryology, and Cell Biology* 184:1–146. (Motor trigeminal nucleus
    and the trigeminal nuclear complex — definitive.)
*   **Trigeminal motor system — review:** Lund, J.P., Kolta, A. (2006).
    "Brainstem circuits that control mastication: do they have anything
    to say about communication?" *Journal of Communication Disorders*
    39:285–300. (Motor trigeminal nucleus and the masticatory central
    pattern generator.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Motor trigeminal nucleus
    in overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An Atlas
    of Structures, Sections, and Systems*, 8th ed. (Motor trigeminal
    nucleus and the pontine trigeminal nuclei.)
*   **Masticatory system:** Dubner, R., Sessle, B.J., Storey, A.T.
    (1978). *The Neural Basis of Oral and Facial Function*. (Motor
    trigeminal nucleus and the muscles of mastication.)
*   **Trigeminal motor somatotopy:** Mizuno, N., Konishi, A., Sato, M.
    (1975). "Localization of masticatory motoneurons in the cat and rat
    by means of retrograde axonal transport of horseradish peroxidase."
    *Journal of Comparative Neurology* 164:105–115. (Somatotopic
    organization of the motor trigeminal nucleus — masticatory
    ventrolateral, accessory dorsomedial.)
*   **Jaw jerk reflex:** Godaux, E., Desmedt, J.E. (1975). "Excitatory
    and inhibitory effects of the masseteric nerve on the masseteric
    motor nucleus of the cat." *Experimental Brain Research* 23:411–424.
    (Monosynaptic jaw jerk reflex — afferent from the mesencephalic
    trigeminal nucleus, efferent from the motor trigeminal nucleus.)
*   **Corticobulbar tract:** Kuypers, H.G.J.M. (1958). "Corticobulbar
    connexions to the pons and lower brain-stem in man: an anatomical
    study." *Brain* 81:364–388. (Bilateral corticobulbar input to the
    motor trigeminal nucleus — minimal masticatory weakness in UMN
    lesions.)
*   **Pseudobulbar palsy (contrast — the enhanced jaw jerk of UMN
    lesions):** Lieberman, A., Drake, M. (1996). "Pseudobulbar palsy."
    In *Neuroanatomy and Neuropathology*. (Enhanced jaw jerk as the
    hallmark of pseudobulbar palsy from bilateral corticobulbar lesions.)
*   **Lateral pontine syndrome (contrast — Marie-Foix):** Marie, P.,
    Foix, C. (1913). "Les lésions des artères du cervelet." *Revue
    Neurologique* 25:177–190. (Lateral pontine syndrome — motor
    trigeminal nucleus involvement in the ipsilateral masticatory
    weakness.)
*   **Foville syndrome (contrast — motor trigeminal nucleus typically
    spared):** Foville, A.L.F. (1858). "Note sur une paralysie peu
    connue des six derniers nerfs crâniens." *Bulletin de la Société
    Anatomique de Paris* 33:289–302. (Foville syndrome — ventromedial
    pontine tegmentum lesion; motor trigeminal nucleus typically
    spared.)
*   **Chief sensory trigeminal nucleus (contrast — the CN V general
    sensory sibling):** Usunoff, K.G., et al. (2006). "The trigeminal
    system." (Chief sensory trigeminal nucleus — general sensory CN V
    sibling; distinct from the motor trigeminal nucleus.)
*   **Mesencephalic trigeminal nucleus (contrast — the AFFERENT limb of
    the jaw jerk):** Usunoff, K.G., et al. (2006). "The trigeminal
    system." (Mesencephalic trigeminal nucleus — proprioceptive afferent
    cell bodies; distinct from the motor trigeminal nucleus.)
*   **Spinal trigeminal nucleus (contrast — the medullary
    pain/temperature component):** Usunoff, K.G., et al. (2006). "The
    trigeminal system." (Spinal trigeminal nucleus — pain/temperature;
    distinct from the motor trigeminal nucleus.)
*   **Trigeminal ganglion (contrast — the peripheral sensory
    ganglion):** Standring, S. (ed.) (2020). *Gray's Anatomy: The
    Anatomical Basis of Clinical Practice*, 42nd ed. (Trigeminal
    ganglion — peripheral sensory ganglion; distinct from the motor
    trigeminal nucleus.)
*   **Facial nerve nucleus (contrast — the CN VII branchial motor
    sibling):** May, M., Schaitkin, B.M. (2000). *The Facial Nerve*, 2nd
    ed. (Facial nerve nucleus — facial expression, CN VII, arch 2;
    distinct from the motor trigeminal nucleus.)
*   **Hypoglossal nucleus (contrast — the medullary tongue motor
    nucleus):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Hypoglossal nucleus — tongue motor
    nucleus; distinct from the motor trigeminal nucleus.)
*   **Nucleus ambiguus (contrast — the medullary branchial motor
    nucleus):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (Nucleus ambiguus — pharynx/larynx
    motor nucleus; distinct from the motor trigeminal nucleus.)
*   **Abducens nucleus (contrast — the CN VI somatic motor sibling):**
    Leigh, R.J., Zee, D.S. (2015). *The Neurology of Eye Movements*, 5th
    ed. (Abducens nucleus — lateral rectus, CN VI; distinct from the
    motor trigeminal nucleus.)
*   **SLEA (contrast — the motor trigeminal nucleus is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the motor
    trigeminal nucleus.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the right motor trigeminal nucleus. **Note**: the
    "right-amygdala" lateralization is about the **amygdala**, not about
    this right pontine motor nucleus.)
*   NeuroNames — Motor nucleus of trigeminal nerve (right); FMA — Motor
    nucleus of trigeminal nerve (right member).
"""