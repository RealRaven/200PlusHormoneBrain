"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left.abducens_nucleus
=================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── metencephalon
        └── pons
            └── cranial_nerve_nuclei
                └── left
                    └── abducens_nucleus   <-- THIS MODULE

**Primary synonym:** Left abducens nucleus; left abducens motor nucleus;
left CN VI nucleus; left sixth-nerve nucleus; "the left lateral rectus
motor nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem somatic motor nucleus** — a **grey-matter neuron cluster**
in the **left pontine tegmentum**, near the midline, in the floor of the
**fourth ventricle** (the **facial colliculus**). It is the **sole
source** of the **left lateral rectus** motor innervation and the
**leftward horizontal conjugate gaze** output node.
**Part of:** The **left** container of the **cranial_nerve_nuclei**
container — specifically, the **somatic motor** component. The **left**
container is the **left-side half** of the pontine cranial-nerve nuclear
collection.
**Structural parent:** ``.../cranial_nerve_nuclei/left/`` → **direct
child** of the left container.
**Structural children:** **None.** This is a **leaf** module. The
**motoneurons** (to the left lateral rectus) and the **internuclear
neurons** (to the right medial rectus subnucleus via the MLF) are
documented as **prose**, not as structural children.
**Boundary status (LEAF — NOT a container):** **Boundary case — the
abducens nucleus is a LEAF, not a container.** It has **no structural
children**. The **motoneurons** and **internuclear neurons** are **prose**
neuron populations, not structural children. Consumers must **not** treat
the abducens nucleus as a container, and must **not** assume the
motoneurons or internuclear neurons exist as sub-modules.
**Boundary status (GREY-MATTER NUCLEUS — NOT the abducens NERVE):**
**Boundary case — the abducens nucleus is the GREY-MATTER NUCLEUS, NOT
the abducens NERVE (CN VI).** The **abducens nerve** (left CN VI) is the
**white-matter axon bundle** that **leaves** the left abducens nucleus
and **travels** to the **left lateral rectus** muscle. The **abducens
nucleus** (here) is the **grey-matter neuron cluster** that **gives rise
to** those axons. They are **DIFFERENT STRUCTURES** — the **nucleus** is
grey matter; the **nerve** is white matter. Consumers must **not**
conflate the **nucleus** with the **nerve** — the nucleus is the
**central neuronal source**; the nerve is the **peripheral conduction
infrastructure**. **This distinction is clinically load-bearing**: a
**nucleus** lesion causes **ipsilateral horizontal gaze palsy** (both
eyes cannot look toward the lesion side, because the internuclear
neurons are also lost), whereas a **nerve** lesion causes **ipsilateral
lateral rectus palsy only** (the eye cannot abduct, but conjugate gaze
is partially preserved because the internuclear neurons are intact).
**Boundary status (NOT the facial nerve nucleus — that is a SIBLING, and
the facial FIBERS loop around the abducens nucleus):** **Boundary case —
the abducens nucleus is NOT the facial nerve nucleus (CN VII); the facial
nerve nucleus is a SIBLING under the left container, and the facial nerve
FIBERS loop around the abducens nucleus.** The **left facial nerve
nucleus** (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``) is the
**branchial motor** nucleus for the **left muscles of facial
expression**. The **left abducens nucleus** (here) is the **somatic
motor** nucleus for the **left lateral rectus**. They are **DIFFERENT
STRUCTURES** — different functional systems, different peripheral
targets. **The facial nerve fibers** (the **internal genu** of CN VII)
**loop around the abducens nucleus** in the pontine tegmentum, producing
the **facial colliculus** on the floor of the fourth ventricle. This
anatomical proximity is a **classic source of confusion** — consumers
must **not** conflate the **abducens nucleus** with the **facial nerve
nucleus**, and must **not** assume the facial nerve fibers are part of
the abducens nucleus.
**Boundary status (NOT the oculomotor nucleus — that is MIDBRAIN, and it
controls the MEDIAL rectus):** **Boundary case — the abducens nucleus is
NOT the oculomotor nucleus (CN III).** The **oculomotor nucleus**
(``.../midbrain/cranial_nerve_nuclei/left/oculomotor_nucleus/``) is the
**midbrain somatic motor** nucleus for the **left medial rectus**, **left
superior rectus**, **left inferior rectus**, and **left inferior
oblique** (via the left CN III). The **abducens nucleus** (here) is the
**pontine somatic motor** nucleus for the **left lateral rectus**. They
are **DIFFERENT STRUCTURES** — different brainstem levels, different
extraocular muscles. **The abducens internuclear neurons project to the
CONTRALATERAL (right) medial rectus subnucleus of the oculomotor
nucleus** via the **MLF** — this is a **crossed projection**, not an
identity. Consumers must **not** conflate the **abducens nucleus** with
the **oculomotor nucleus**.
**Boundary status (NOT the trochlear nucleus — that is MIDBRAIN, and it
controls the SUPERIOR oblique):** **Boundary case — the abducens nucleus
is NOT the trochlear nucleus (CN IV).** The **trochlear nucleus**
(``.../midbrain/cranial_nerve_nuclei/left/trochlear_nucleus/``) is the
**midbrain somatic motor** nucleus for the **left superior oblique**. The
**abducens nucleus** (here) is the **pontine somatic motor** nucleus for
the **left lateral rectus**. They are **DIFFERENT STRUCTURES** — different
brainstem levels, different extraocular muscles. Consumers must **not**
conflate the **abducens nucleus** with the **trochlear nucleus**.
**Boundary status (NOT the lateral rectus muscle — that is the PERIPHERAL
TARGET):** **Boundary case — the abducens nucleus is NOT the lateral
rectus muscle.** The **left lateral rectus** is the **peripheral
extraocular muscle** that **abducts the left eye** — it is the **target**
of the left abducens motor axons. The **abducens nucleus** (here) is the
**central grey-matter neuron cluster** that **innervates** the left
lateral rectus. They are **DIFFERENT STRUCTURES** — the **nucleus** is
central nervous system; the **muscle** is peripheral effector. Consumers
must **not** conflate the **nucleus** with the **muscle**.
**Boundary status (NOT the medial longitudinal fasciculus — that is the
WHITE-MATTER TRACT carrying the internuclear axons):** **Boundary case —
the abducens nucleus is NOT the medial longitudinal fasciculus (MLF).**
The **MLF** is the **white-matter tract** that carries the **internuclear
neuron axons** from the abducens nucleus to the **contralateral medial
rectus subnucleus** of the oculomotor nucleus. The **abducens nucleus**
(here) is the **grey-matter neuron cluster** that **gives rise to** those
internuclear axons. They are **DIFFERENT STRUCTURES** — the **nucleus** is
grey matter; the **MLF** is white matter. **This distinction is
clinically load-bearing**: an **MLF** lesion causes **internuclear
ophthalmoplegia (INO)** — impaired adduction of the ipsilateral eye with
dissociated nystagmus of the abducting eye — whereas an **abducens
nucleus** lesion causes **ipsilateral horizontal gaze palsy**. Consumers
must **not** conflate the **abducens nucleus** with the **MLF**.
**Boundary status (NOT the paramedian pontine reticular formation — that
is the HORIZONTAL GAZE CENTER upstream):** **Boundary case — the abducens
nucleus is NOT the paramedian pontine reticular formation (PPRF).** The
**PPRF** (``.../pons/tegmentum/paramedian_pontine_reticular_formation/``)
is the **horizontal saccadic burst generator** — it contains **excitatory
burst neurons** that **drive** the abducens nucleus for **horizontal
saccades**. The **abducens nucleus** (here) is the **motor output
nucleus** — it contains the **motoneurons** (to the lateral rectus) and
the **internuclear neurons** (to the contralateral medial rectus
subnucleus). They are **DIFFERENT STRUCTURES** — the **PPRF** is
**upstream** of the abducens nucleus in the horizontal gaze circuit; the
**abducens nucleus** is the **final common pathway**. **This distinction
is clinically load-bearing**: a **PPRF** lesion causes **ipsilateral
horizontal gaze palsy** (similar to an abducens nucleus lesion), but the
**abducens nucleus itself is spared**. Consumers must **not** conflate
the **abducens nucleus** with the **PPRF**.
**Boundary status (NOT the nucleus prepositus hypoglossi — that is the
NEURAL INTEGRATOR):** **Boundary case — the abducens nucleus is NOT the
nucleus prepositus hypoglossi (NPH).** The **NPH**
(``.../medulla_oblongata/perihypoglossal_nuclei/prepositus_nucleus/``) is
the **horizontal gaze neural integrator** — it **converts** the
**velocity** command from the PPRF into a **position** command that
**holds** the eyes in eccentric gaze. The **abducens nucleus** (here) is
the **motor output nucleus**. They are **DIFFERENT STRUCTURES** — the
**NPH** is the **integrator**; the **abducens nucleus** is the **output**.
Consumers must **not** conflate the **abducens nucleus** with the **NPH**.
**Boundary status (NOT the vestibular nuclei — those are the VOR INPUT):**
**Boundary case — the abducens nucleus is NOT the vestibular nuclei.**
The **left vestibular nuclei**
(``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
are the **special sensory** nuclei for **balance and spatial
orientation** — they **project** to the abducens nucleus to **drive** the
**vestibulo-ocular reflex (VOR)**. The **abducens nucleus** (here) is the
**somatic motor** nucleus for the **left lateral rectus**. They are
**DIFFERENT STRUCTURES** — the **vestibular nuclei** are **upstream
sensory** structures; the **abducens nucleus** is the **downstream motor**
structure. Consumers must **not** conflate the **abducens nucleus** with
the **vestibular nuclei**.
**Boundary status (NOT the facial colliculus — that is the SURFACE
LANDMARK):** **Boundary case — the abducens nucleus is NOT the facial
colliculus.** The **facial colliculus** is the **bump on the floor of the
fourth ventricle** produced by the **facial nerve fibers** (the internal
genu of CN VII) **looping around** the abducens nucleus. It is a
**surface landmark**, not the nucleus itself. The **abducens nucleus**
(here) is the **grey-matter structure beneath** the facial colliculus.
Consumers must **not** conflate the **abducens nucleus** with the
**facial colliculus** — the colliculus is a **surface feature**; the
nucleus is the **underlying grey-matter structure**.
**Boundary status (NOT the whole cranial_nerve_nuclei container — a leaf
child of the left container):** **Boundary case — the abducens nucleus is
a LEAF child of the left container, not the container itself, and not the
whole cranial_nerve_nuclei container.** The **left** container contains
the **abducens nucleus** and **five other children**. The
**cranial_nerve_nuclei** container contains **two structural children**
(``left`` and ``right``). Consumers must **not** conflate the abducens
nucleus with the **left** container or the **cranial_nerve_nuclei**
container.
**Boundary status (NOT the right abducens nucleus — strict mirror, no
warning):** **Boundary case — the left abducens nucleus is NOT the right
abducens nucleus; the two are a STRICT MIRROR PAIR with NO warning at the
nucleus level.** The **right abducens nucleus**
(``.../cranial_nerve_nuclei/right/abducens_nucleus/``) is the
**structurally identical** right-side counterpart — same somatic motor
function, same leaf status, same bilateral framing. The two sides are
**strictly mirrored** — any lateralization is documented **here, in the
Lateralization Notes**, not imported from elsewhere. Consumers must
**not** import a lateralization warning into the left abducens nucleus —
there is **none at the nucleus level** beyond the **crossed internuclear
projection** documented below.
**Boundary status (NOT a single neuron population — TWO populations with
DIFFERENT projections):** **Boundary case — the abducens nucleus is NOT a
single uniform neuron population; it contains TWO functionally distinct
populations.** The **motoneurons** project to the **ipsilateral (left)
lateral rectus** — they **abduct the left eye**. The **internuclear
neurons** project to the **contralateral (right) medial rectus
subnucleus** of the oculomotor nucleus via the **MLF** — they **adduct
the right eye**. Together, these two populations produce **leftward
conjugate horizontal gaze** (left eye abducts, right eye adducts).
Consumers must **not** treat the abducens nucleus as a single uniform
population — it is a **two-population output node** for **conjugate
horizontal gaze**.
**Boundary status (SLEA-FREE — the abducens nucleus is NOT an
extended-amygdala component):** **Boundary case — the abducens nucleus is
SLEA-FREE.** The **SLEA overlap** belongs to the **central nucleus** (the
**only SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere). The **abducens
nucleus** is a **somatic motor brainstem nucleus** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the abducens nucleus
— it is **SLEA-free**.

Overview
--------
The abducens nucleus is the **somatic motor** nucleus for the **left
lateral rectus** — the **sole source** of the left lateral rectus motor
innervation and the **leftward horizontal conjugate gaze** output node.
It is a **leaf** module under the left container of the
cranial_nerve_nuclei container, and it contains **two functionally
distinct neuron populations**: the **motoneurons** (to the left lateral
rectus) and the **internuclear neurons** (to the right medial rectus
subnucleus via the MLF).

**The abducens nucleus is the GREY-MATTER NUCLEUS, NOT the abducens
NERVE.** The **abducens nerve** (left CN VI) is the **white-matter axon
bundle** that **travels** to the left lateral rectus. The **abducens
nucleus** (here) is the **grey-matter neuron cluster** that **gives rise
to** those axons. They are **DIFFERENT STRUCTURES** — the **nucleus** is
grey matter; the **nerve** is white matter. **This distinction is
clinically load-bearing**: a **nucleus** lesion causes **ipsilateral
horizontal gaze palsy** (both eyes cannot look toward the lesion side),
whereas a **nerve** lesion causes **ipsilateral lateral rectus palsy
only** (the eye cannot abduct, but conjugate gaze is partially
preserved).

**The abducens nucleus is NOT the facial nerve nucleus.** The **facial
nerve nucleus** (CN VII) is a **sibling** under the left container — the
**branchial motor** nucleus for the **left muscles of facial
expression**. The **facial nerve fibers** (the internal genu of CN VII)
**loop around** the abducens nucleus in the pontine tegmentum, producing
the **facial colliculus** on the floor of the fourth ventricle. This
anatomical proximity is a **classic source of confusion** — consumers
must **not** conflate the **abducens nucleus** with the **facial nerve
nucleus**, and must **not** assume the facial nerve fibers are part of
the abducens nucleus.

**The abducens nucleus is a TWO-POPULATION output node.** The
**motoneurons** project to the **ipsilateral (left) lateral rectus**;
the **internuclear neurons** project to the **contralateral (right)
medial rectus subnucleus** via the **MLF**. Together, they produce
**leftward conjugate horizontal gaze**. The two populations are **prose**,
not structural children — the abducens nucleus is a **leaf** with **no
structural children**.

**The abducens nucleus is NOT the PPRF, the MLF, the NPH, or the
vestibular nuclei.** The **PPRF** is the **horizontal saccadic burst
generator** upstream; the **MLF** is the **white-matter tract** carrying
the internuclear axons; the **NPH** is the **horizontal gaze neural
integrator**; the **vestibular nuclei** are the **VOR input**. The
abducens nucleus is the **final common pathway** — the **motor output
nucleus** that the PPRF drives, that the NPH integrates, and that the
vestibular nuclei modulate. **Each distinction is clinically
load-bearing** — a lesion at each level produces a **different clinical
syndrome**.

**The abducens nucleus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

Neuron Population Composition (prose, not structural children)
---------------------------------------------------------------
The abducens nucleus is a **two-population output node** — documented as
**prose**, not as structural children:

*   **Motoneurons** — the **somatic motor** neurons whose axons form the
    **left abducens nerve** (left CN VI) and innervate the **left
    lateral rectus** muscle. They **abduct the left eye**. They are the
    **sole source** of the left lateral rectus motor innervation.

*   **Internuclear neurons** — the **internuclear** neurons whose axons
    **cross the midline** and travel in the **contralateral (right)
    MLF** to synapse on the **right medial rectus subnucleus** of the
    **right oculomotor nucleus**. They **adduct the right eye**. They
    are the **neural substrate** of **conjugate horizontal gaze** — the
    left abducens nucleus drives **both** the left eye's abduction (via
    motoneurons) **and** the right eye's adduction (via internuclear
    neurons), producing **leftward conjugate horizontal gaze**.

**These populations are prose, not structural children.** The tree wires
the **abducens nucleus** as a **single leaf** under the left container —
the **motoneurons** and **internuclear neurons** are **prose**, not
structural children. Consumers that need **neuron-population-level**
resolution should consult the references, not the tree.

The Abducens Nucleus / Abducens Nerve Boundary
----------------------------------------------
This is the **grey-matter vs. white-matter** boundary:

*   **Abducens nucleus** (this module) — the **grey-matter neuron
    cluster** in the left pontine tegmentum.

*   **Abducens nerve** (left CN VI) — the **white-matter axon bundle**
    that travels to the left lateral rectus.

**They are DIFFERENT STRUCTURES.** The **nucleus** is the **central
neuronal source**; the **nerve** is the **peripheral conduction
infrastructure**. **This distinction is clinically load-bearing**: a
**nucleus** lesion causes **ipsilateral horizontal gaze palsy** (both
eyes cannot look toward the lesion side, because the internuclear neurons
are also lost), whereas a **nerve** lesion causes **ipsilateral lateral
rectus palsy only** (the eye cannot abduct, but conjugate gaze is
partially preserved because the internuclear neurons are intact).
Consumers must **not** conflate the two — the **abducens nucleus** is the
**nucleus**; the **abducens nerve** is the **nerve**.

The Abducens Nucleus / Facial Nerve Nucleus Boundary
----------------------------------------------------
This is the **sibling** boundary — with a **fiber-proximity** twist:

*   **Abducens nucleus** (this module) — the **somatic motor** nucleus
    for the **left lateral rectus**.

*   **Facial nerve nucleus** (``.../cranial_nerve_nuclei/left/facial_nerve_nucleus/``)
    — the **branchial motor** nucleus for the **left muscles of facial
    expression**.

**They are DIFFERENT STRUCTURES** — different functional systems,
different peripheral targets. **The facial nerve fibers** (the internal
genu of CN VII) **loop around** the abducens nucleus in the pontine
tegmentum, producing the **facial colliculus** on the floor of the fourth
ventricle. This anatomical proximity is a **classic source of
confusion** — consumers must **not** conflate the **abducens nucleus**
with the **facial nerve nucleus**, and must **not** assume the facial
nerve fibers are part of the abducens nucleus.

The Abducens Nucleus / Oculomotor and Trochlear Nuclei Boundary
---------------------------------------------------------------
This is the **extraocular motor nucleus** boundary:

*   **Abducens nucleus** (this module) — the **pontine somatic motor**
    nucleus for the **left lateral rectus** (left eye abduction).

*   **Oculomotor nucleus** (``.../midbrain/cranial_nerve_nuclei/left/oculomotor_nucleus/``)
    — the **midbrain somatic motor** nucleus for the **left medial
    rectus**, **left superior rectus**, **left inferior rectus**, and
    **left inferior oblique** (left eye adduction, elevation, depression,
    intorsion).

*   **Trochlear nucleus** (``.../midbrain/cranial_nerve_nuclei/left/trochlear_nucleus/``)
    — the **midbrain somatic motor** nucleus for the **left superior
    oblique** (left eye intorsion and depression).

**They are DIFFERENT STRUCTURES** — different brainstem levels, different
extraocular muscles. **The abducens internuclear neurons project to the
CONTRALATERAL (right) medial rectus subnucleus of the oculomotor nucleus**
via the **MLF** — this is a **crossed projection**, not an identity.
Consumers must **not** conflate the **abducens nucleus** with the
**oculomotor nucleus** or the **trochlear nucleus**.

The Abducens Nucleus / Medial Longitudinal Fasciculus Boundary
--------------------------------------------------------------
This is the **grey-matter vs. white-matter** boundary — the **MLF** is the
**tract** carrying the internuclear axons:

*   **Abducens nucleus** (this module) — the **grey-matter neuron
    cluster** that **gives rise to** the internuclear axons.

*   **Medial longitudinal fasciculus (MLF)** — the **white-matter tract**
    that **carries** the internuclear axons from the abducens nucleus to
    the **contralateral medial rectus subnucleus** of the oculomotor
    nucleus.

**They are DIFFERENT STRUCTURES.** The **nucleus** is grey matter; the
**MLF** is white matter. **This distinction is clinically load-bearing**:
an **MLF** lesion causes **internuclear ophthalmoplegia (INO)** — impaired
adduction of the ipsilateral eye with dissociated nystagmus of the
abducting eye — whereas an **abducens nucleus** lesion causes
**ipsilateral horizontal gaze palsy**. Consumers must **not** conflate
the **abducens nucleus** with the **MLF**.

The Abducens Nucleus / Paramedian Pontine Reticular Formation Boundary
----------------------------------------------------------------------
This is the **gaze-center upstream** boundary:

*   **Abducens nucleus** (this module) — the **motor output nucleus** —
    the **final common pathway** for horizontal gaze.

*   **Paramedian pontine reticular formation (PPRF)**
    (``.../pons/tegmentum/paramedian_pontine_reticular_formation/``) —
    the **horizontal saccadic burst generator** — the **excitatory burst
    neurons** that **drive** the abducens nucleus for **horizontal
    saccades**.

**The PPRF is upstream of the abducens nucleus** in the horizontal gaze
circuit. **This distinction is clinically load-bearing**: a **PPRF**
lesion causes **ipsilateral horizontal gaze palsy** (similar to an
abducens nucleus lesion), but the **abducens nucleus itself is spared**.
Consumers must **not** conflate the **abducens nucleus** with the
**PPRF**.

The Abducens Nucleus / Nucleus Prepositus Hypoglossi Boundary
-------------------------------------------------------------
This is the **neural integrator** boundary:

*   **Abducens nucleus** (this module) — the **motor output nucleus**.

*   **Nucleus prepositus hypoglossi (NPH)**
    (``.../medulla_oblongata/perihypoglossal_nuclei/prepositus_nucleus/``)
    — the **horizontal gaze neural integrator** — it **converts** the
    **velocity** command from the PPRF into a **position** command that
    **holds** the eyes in eccentric gaze.

**They are DIFFERENT STRUCTURES** — the **NPH** is the **integrator**;
the **abducens nucleus** is the **output**. Consumers must **not**
conflate the **abducens nucleus** with the **NPH**.

The Abducens Nucleus / Vestibular Nuclei Boundary
-------------------------------------------------
This is the **VOR input** boundary:

*   **Abducens nucleus** (this module) — the **somatic motor** nucleus for
    the **left lateral rectus**.

*   **Vestibular nuclei**
    (``.../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/``)
    — the **special sensory** nuclei for **balance and spatial
    orientation**; they **project** to the abducens nucleus to **drive**
    the **vestibulo-ocular reflex (VOR)**.

**They are DIFFERENT STRUCTURES** — the **vestibular nuclei** are
**upstream sensory** structures; the **abducens nucleus** is the
**downstream motor** structure. Consumers must **not** conflate the
**abducens nucleus** with the **vestibular nuclei**.

The Abducens Nucleus / Facial Colliculus Boundary
-------------------------------------------------
This is the **surface-landmark** boundary:

*   **Abducens nucleus** (this module) — the **grey-matter structure
    beneath** the facial colliculus.

*   **Facial colliculus** — the **bump on the floor of the fourth
    ventricle** produced by the **facial nerve fibers** (the internal
    genu of CN VII) **looping around** the abducens nucleus.

**The facial colliculus is a surface landmark, not the nucleus itself.**
Consumers must **not** conflate the **abducens nucleus** with the
**facial colliculus** — the colliculus is a **surface feature**; the
nucleus is the **underlying grey-matter structure**.

The Abducens Nucleus / Lateral Rectus Muscle Boundary
-----------------------------------------------------
This is the **central vs. peripheral** boundary:

*   **Abducens nucleus** (this module) — the **central grey-matter neuron
    cluster**.

*   **Lateral rectus muscle** — the **peripheral extraocular muscle**
    that **abducts the left eye** — the **target** of the left abducens
    motor axons.

**They are DIFFERENT STRUCTURES** — the **nucleus** is central nervous
system; the **muscle** is peripheral effector. Consumers must **not**
conflate the **nucleus** with the **muscle**.

The Abducens Nucleus / Right Abducens Nucleus Boundary
------------------------------------------------------
This is the **strict-mirror** boundary:

*   **Left abducens nucleus** (this module) — the **left-side** somatic
    motor nucleus for the **left lateral rectus**.

*   **Right abducens nucleus**
    (``.../cranial_nerve_nuclei/right/abducens_nucleus/``) — the
    **structurally identical** right-side somatic motor nucleus for the
    **right lateral rectus**.

**They are a STRICT MIRROR PAIR with NO warning at the nucleus level.**
The two sides are **structurally identical** — same somatic motor
function, same leaf status, same bilateral framing. **The crossed
internuclear projection is a connectivity fact, not a lateralization
warning** — the left abducens internuclear neurons project to the
**right** medial rectus subnucleus, and the right abducens internuclear
neurons project to the **left** medial rectus subnucleus. This is
**structural**, not a functional lateralization. Consumers must **not**
import a lateralization warning into the left abducens nucleus — there is
**none at the nucleus level**.

The Abducens Nucleus / Cranial Nerve Nuclei Container Boundary
--------------------------------------------------------------
This is the **leaf vs. container** boundary:

*   **Abducens nucleus** (this module) — a **leaf** child of the **left**
    container.

*   **Left container** (``.../cranial_nerve_nuclei/left/``) — the
    **left-side half** of the pontine cranial-nerve nuclear collection,
    with **six structural children** (including the abducens nucleus).

*   **Cranial_nerve_nuclei container** (``.../cranial_nerve_nuclei/``) —
    the **whole pontine collection**, with **two structural children**
    (``left`` and ``right``).

**The abducens nucleus is a leaf child of the left container.**
Consumers must **not** conflate the abducens nucleus with the **left**
container or the **cranial_nerve_nuclei** container.

The Abducens Nucleus / SLEA Boundary
------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Abducens nucleus** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral pallidum**,
    and **nucleus accumbens** (wired elsewhere).

**The abducens nucleus is NOT part of the SLEA continuum.** It is a
**somatic motor brainstem nucleus**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the abducens nucleus.

Function in the Human Brain
---------------------------
The abducens nucleus's functions are **the somatic motor control of the
left lateral rectus** and **the leftward horizontal conjugate gaze
output** — **NOT a single unified function**:

*   **Somatic Motor (Left Lateral Rectus):** The **motoneurons** innervate
    the **left lateral rectus** — they **abduct the left eye**. The
    abducens nucleus is the **sole source** of the left lateral rectus
    motor innervation.

*   **Conjugate Horizontal Gaze (Leftward):** The **internuclear
    neurons** project to the **right medial rectus subnucleus** of the
    **right oculomotor nucleus** via the **right MLF** — they **adduct
    the right eye**. Together with the motoneurons, they produce
    **leftward conjugate horizontal gaze** (left eye abducts, right eye
    adducts).

*   **Final Common Pathway for Horizontal Gaze:** The abducens nucleus is
    the **motor output node** for horizontal gaze — it **receives** the
    **saccadic velocity command** from the **PPRF**, the **integrated
    position command** from the **NPH**, and the **VOR drive** from the
    **vestibular nuclei**. It is the **final common pathway** that
    **converts** these signals into **left lateral rectus contraction**
    and **right medial rectus contraction**.

*   **NOT a neural processor in the classical sense.** The abducens
    nucleus is a **motor output nucleus** — it **executes** the
    horizontal gaze commands generated upstream (PPRF, NPH, vestibular
    nuclei). The **processing** happens in the **PPRF** (burst
    generation), the **NPH** (integration), and the **vestibular nuclei**
    (VOR). The abducens nucleus is the **output**.

**The unifying theme:** the abducens nucleus is the **somatic motor
output nucleus** for the **left lateral rectus** and the **leftward
horizontal conjugate gaze** — the **final common pathway** for
horizontal eye movements. It is **SLEA-free**, **somatic motor**, and
**NOT the abducens nerve** — the **nerve** is the **white-matter axon
bundle**; the **nucleus** is the **grey-matter neuron cluster** that
**gives rise to** it.

Associated Disorders
--------------------
The abducens nucleus has **no named "abducens nucleus syndrome"** — its
clinical associations are **nucleus-specific**, and they are
**distinguishable from nerve-level, MLF-level, and PPRF-level lesions**:

*   **Abducens Nucleus Lesion — Ipsilateral Horizontal Gaze Palsy:** A
    lesion of the **left abducens nucleus** causes **leftward horizontal
    gaze palsy** — **both eyes cannot look left** (the left eye cannot
    abduct because the motoneurons are lost; the right eye cannot adduct
    because the internuclear neurons are lost). This is **distinct from**
    a **left abducens nerve** lesion, which causes **left lateral rectus
    palsy only** (the left eye cannot abduct, but the right eye can still
    adduct via convergence and the intact internuclear neurons).

*   **Abducens Nerve Lesion — Ipsilateral Lateral Rectus Palsy (Sixth
    Nerve Palsy):** A lesion of the **left abducens nerve** causes
    **left lateral rectus palsy** — **inability to abduct the left eye**,
    **esotropia** (the left eye deviates inward at rest),
    **diplopia** on left lateral gaze. This is **distinct from** a
    **nucleus** lesion because the **internuclear neurons are spared** —
    the right eye can still adduct.

*   **Internuclear Ophthalmoplegia (INO) — MLF Lesion:** A lesion of the
    **left MLF** causes **left INO** — **impaired adduction of the left
    eye** with **dissociated nystagmus of the right (abducting) eye**.
    This is **distinct from** an **abducens nucleus** lesion — the
    **abducens nucleus itself is spared**, and the **left eye can still
    abduct** (the left abducens motoneurons are intact).

*   **One-and-a-Half Syndrome — Abducens Nucleus/PPRF + Adjacent MLF
    Lesion:** A lesion of the **left abducens nucleus** (or **left
    PPRF**) **plus** the **adjacent left MLF** causes **one-and-a-half
    syndrome** — **leftward horizontal gaze palsy** (the "one") **plus**
    **left INO** (the "half"). The only preserved horizontal movement is
    **rightward abduction of the right eye**. **The abducens nucleus is
    the substrate of the "one" component** — the "half" component is the
    MLF.

*   **Foville Syndrome — Pontine Tegmentum Lesion:** A lesion of the
    **left pontine tegmentum** involving the **left abducens nucleus**,
    the **left facial nerve fibers** (which loop around the nucleus), and
    the **left corticospinal tract** causes **Foville syndrome** —
    **leftward horizontal gaze palsy** + **left facial palsy** +
    **right hemiparesis**.

*   **Millard-Gubler Syndrome — Pontine Base Lesion:** A lesion of the
    **left pontine base** involving the **left abducens nerve fibers**
    and the **left facial nerve fibers** (and the **left corticospinal
    tract**) causes **Millard-Gubler syndrome** — **left lateral rectus
    palsy** + **left facial palsy** + **right hemiparesis**. **Note**:
    this is a **nerve-fiber** lesion, not a **nucleus** lesion — the
    abducens nucleus itself may be spared.

*   **Wernicke's Encephalopathy — Abducens Nucleus Involvement:** **Wernicke's
    encephalopathy** (thiamine deficiency) can affect the **abducens
    nucleus** (among other brainstem and diencephalic structures),
    contributing to **abducens palsy** and **horizontal gaze
    abnormalities**.

*   **Möbius Syndrome — Congenital Abducens (and Facial) Palsy:**
    **Möbius syndrome** is a **congenital** disorder characterized by
    **abducens (CN VI)** and **facial (CN VII)** palsy — the **abducens
    nucleus** (and the facial nucleus) are **hypoplastic or absent**.

*   **No Named "Abducens Nucleus Syndrome":** The abducens nucleus is a
    **single somatic motor nucleus** — it has **no named clinical
    syndrome of its own**. Its clinical relevance is **nucleus-specific**,
    via the **left lateral rectus** and the **leftward horizontal
    conjugate gaze** it subserves. **The most important clinical
    distinction is nucleus vs. nerve vs. MLF vs. PPRF** — each produces a
    **different syndrome**, and the abducens nucleus is **only one node**
    in the horizontal gaze circuit.

**What is NOT here:** The abducens nucleus is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **fear conditioning** (amygdala — central nucleus +
basolateral nuclei), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **Alzheimer's disease** (hippocampus, nucleus basalis),
**Parkinson's disease** (substantia nigra), or **internuclear
ophthalmoplegia alone** (MLF). Its clinical relevance is
**horizontal-gaze-specific**, via the **left lateral rectus** and the
**leftward conjugate gaze** it subserves. **No named abducens nucleus
syndrome exists.**

Lateralization Notes
--------------------
This is the **left** abducens nucleus module. The abducens nucleus is
**bilaterally symmetric** with the right abducens nucleus and **strictly
mirrored** — and it carries **NO warning at the nucleus level**:

*   **Strict Bilateral Symmetry:** The **left** and **right** abducens
    nuclei are **structurally identical** — same somatic motor function,
    same leaf status, same bilateral framing. The bilateral symmetry is
    **strict**.

*   **Crossed Internuclear Projection (Connectivity Fact, NOT a
    Lateralization Warning):** The **left abducens internuclear neurons**
    project to the **right medial rectus subnucleus** via the **right
    MLF**; the **right abducens internuclear neurons** project to the
    **left medial rectus subnucleus** via the **left MLF**. This is a
    **structural connectivity fact** — it is **not** a functional
    lateralization, and it is **not** a warning. It is the **neural
    substrate** of **conjugate horizontal gaze** — the left abducens
    nucleus drives **both** the left eye's abduction (via motoneurons)
    **and** the right eye's adduction (via internuclear neurons).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The abducens
    nucleus is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning or the
    amygdala-lateralization warning into the abducens nucleus.

*   **NO Amygdala-Lateralization Warning of their own (the abducens
    nucleus is SOMATIC MOTOR, not the fear-output):** The **right-amygdala
    fear association** belongs to the **amygdala module** — specifically
    the **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning). The abducens nucleus is a **somatic motor brainstem
    nucleus** — consumers must **not** conflate it with the **amygdala**
    or with the **fear circuit**.

**A consumer that assumes "left abducens nucleus = right abducens
nucleus" will be structurally correct** — the two sides are **strictly
symmetric** (the crossed internuclear projection is a connectivity fact,
not a lateralization). The abducens nucleus is a **strict-mirror pair
with NO warning at the nucleus level** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no rhinencephalon-exclusion
flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cranial_nerve_nuclei/right/``, ``.../midbrain/``,
    ``.../medulla_oblongata/``, ``.../pons/tegmentum/``, or any other
    container. The abducens nucleus's relationships to the **abducens
    nerve**, the **facial nerve nucleus**, the **oculomotor nucleus**,
    the **trochlear nucleus**, the **MLF**, the **PPRF**, the **NPH**,
    the **vestibular nuclei**, the **facial colliculus**, and the
    **lateral rectus muscle** are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **motoneurons** and
    **internuclear neurons** are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve neuron-population-level detail through the references.
*   **GREY-MATTER NUCLEUS — NOT the abducens NERVE.** The **abducens
    nucleus** is the **grey-matter neuron cluster**; the **abducens
    nerve** (left CN VI) is the **white-matter axon bundle**. Consumers
    must **not** conflate the two. **This distinction is clinically
    load-bearing** — nucleus lesion = ipsilateral horizontal gaze palsy;
    nerve lesion = ipsilateral lateral rectus palsy only.
*   **NOT the facial nerve nucleus — that is a SIBLING.** The **facial
    nerve fibers** loop around the abducens nucleus, but the **facial
    nerve nucleus** is a **different structure**. Consumers must **not**
    conflate the two.
*   **NOT the oculomotor nucleus or the trochlear nucleus — those are
    MIDBRAIN.** The abducens nucleus is the **pontine** somatic motor
    nucleus for the **lateral rectus**. The **oculomotor** and
    **trochlear** nuclei are the **midbrain** somatic motor nuclei for
    the **medial rectus / superior rectus / inferior rectus / inferior
    oblique** and the **superior oblique**, respectively.
*   **NOT the MLF — that is the WHITE-MATTER TRACT carrying the
    internuclear axons.** The **MLF** is white matter; the **abducens
    nucleus** is grey matter. **This distinction is clinically
    load-bearing** — MLF lesion = INO; abducens nucleus lesion =
    ipsilateral horizontal gaze palsy.
*   **NOT the PPRF — that is the HORIZONTAL GAZE CENTER upstream.** The
    **PPRF** drives the abducens nucleus; the **abducens nucleus** is
    the **final common pathway**. Consumers must **not** conflate the
    two.
*   **NOT the NPH — that is the NEURAL INTEGRATOR.** The **NPH**
    integrates the horizontal gaze command; the **abducens nucleus** is
    the **output**. Consumers must **not** conflate the two.
*   **NOT the vestibular nuclei — those are the VOR INPUT.** The
    **vestibular nuclei** project to the abducens nucleus; the
    **abducens nucleus** is the **output**. Consumers must **not**
    conflate the two.
*   **NOT the facial colliculus — that is the SURFACE LANDMARK.** The
    **facial colliculus** is the **bump on the floor of the fourth
    ventricle**; the **abducens nucleus** is the **underlying grey-matter
    structure**. Consumers must **not** conflate the two.
*   **NOT a single neuron population — TWO populations.** The
    **motoneurons** (to the left lateral rectus) and the **internuclear
    neurons** (to the right medial rectus subnucleus via the MLF) are
    **functionally distinct**. Consumers must **not** treat the abducens
    nucleus as a single uniform population.
*   **SLEA-FREE — no extended-amygdala relationship.** The abducens
    nucleus is **not** an extended-amygdala component, and it carries
    **no SLEA warning**.
*   **NOT the fear-output — the abducens nucleus is SOMATIC MOTOR.** The
    **fear-output** structure is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**; the
    **fear-modulatory / extinction** structures are the **basomedial
    nuclei**. The **abducens nucleus** is a **somatic motor brainstem
    nucleus** — it is **not** part of the fear circuit.
*   **No ``AREA_PATHS`` hop.** The abducens nucleus is a local leaf under
    the left container, not a cross-listed leaf.
*   **No nested cross-listing.** The abducens nucleus has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with right abducens nucleus — strict mirror with
    NO warning.** Left and right abducens nucleus modules are
    **structurally identical** — same leaf status, same **somatic motor**
    framing, same **SLEA-free** status, same **no warning** at the
    nucleus level (the crossed internuclear projection is a connectivity
    fact, not a warning).

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei.left import abducens_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei.left."
        "abducens_nucleus"
    )

**Do not** assume the abducens nucleus is the **abducens nerve**. The
**abducens nerve** (left CN VI) is the **white-matter axon bundle**; the
**abducens nucleus** is the **grey-matter neuron cluster**. They are
**different structures**. **This distinction is clinically
load-bearing** — a **nucleus** lesion causes **ipsilateral horizontal
gaze palsy**; a **nerve** lesion causes **ipsilateral lateral rectus
palsy only**.

**Do not** assume the abducens nucleus is the **facial nerve nucleus**.
The **facial nerve nucleus** is a **sibling** under the left container;
the **facial nerve fibers** loop around the abducens nucleus, but the
**nucleus itself** is a **different structure**.

**Do not** assume the abducens nucleus is the **oculomotor nucleus** or
the **trochlear nucleus**. Those are **midbrain** somatic motor nuclei;
the abducens nucleus is a **pontine** somatic motor nucleus.

**Do not** assume the abducens nucleus is the **MLF**, the **PPRF**, the
**NPH**, or the **vestibular nuclei**. Those are **different structures**
in the horizontal gaze circuit — the **MLF** is the **white-matter
tract**; the **PPRF** is the **upstream burst generator**; the **NPH** is
the **neural integrator**; the **vestibular nuclei** are the **VOR
input**. **Each distinction is clinically load-bearing** — a lesion at
each level produces a **different clinical syndrome**.

**Do not** assume the abducens nucleus is the **facial colliculus**. The
**facial colliculus** is a **surface landmark**; the **abducens nucleus**
is the **underlying grey-matter structure**.

**Do not** assume the abducens nucleus is the **lateral rectus muscle**.
The **lateral rectus** is the **peripheral target**; the **abducens
nucleus** is the **central source**.

**Do not** import the **SLEA warning** or the **amygdala-lateralization
warning** into the abducens nucleus. **The abducens nucleus is
SLEA-FREE** — it is **not** an extended-amygdala component, and it is
**NOT part of the fear circuit**.

Iterating the abducens nucleus's (empty) children (recommended consumer
pattern)::

    ABDUCENS_NUCLEUS_CHILDREN = ()
    # The abducens nucleus is a leaf. The motoneurons and internuclear
    # neurons are prose, not modules.

Reaching the abducens nerve (recommended consumer pattern — the
white-matter axon bundle)::

    # The abducens nerve (left CN VI) is the WHITE-MATTER axon bundle:
    #
    #   peripheral: left CN VI -> left lateral rectus
    #
    # The nucleus is the CENTRAL neuronal source; the nerve is the
    # PERIPHERAL conduction infrastructure.

Reaching the facial nerve nucleus (recommended consumer pattern — the
sibling)::

    # The facial nerve nucleus is the BRANCHIAL MOTOR sibling under the
    # left container:
    #
    #   .../cranial_nerve_nuclei/left/facial_nerve_nucleus/
    #
    # The facial nerve FIBERS loop around the abducens nucleus
    # (facial colliculus), but the NUCLEUS is a different structure.

Reaching the MLF (recommended consumer pattern — the white-matter
tract)::

    # The MLF is the WHITE-MATTER tract carrying the internuclear axons:
    #
    #   .../white_matter/medial_forebrain_bundle/  (or MLF-specific path)
    #
    # The abducens nucleus GIVES RISE TO the internuclear axons; the MLF
    # CARRIES them.

Reaching the PPRF (recommended consumer pattern — the upstream burst
generator)::

    # The PPRF is the HORIZONTAL SACCADIC BURST GENERATOR:
    #
    #   .../pons/tegmentum/paramedian_pontine_reticular_formation/
    #
    # The PPRF DRIVES the abducens nucleus; the abducens nucleus is the
    # FINAL COMMON PATHWAY.

Reaching the NPH (recommended consumer pattern — the neural
integrator)::

    # The NPH is the HORIZONTAL GAZE NEURAL INTEGRATOR:
    #
    #   .../medulla_oblongata/perihypoglossal_nuclei/prepositus_nucleus/
    #
    # The NPH INTEGRATES the horizontal gaze command; the abducens
    # nucleus is the OUTPUT.

Reaching the vestibular nuclei (recommended consumer pattern — the VOR
input)::

    # The vestibular nuclei are the VOR INPUT:
    #
    #   .../cranial_nerve_nuclei/left/vestibulocochlear_nuclei/vestibular_nuclei/
    #
    # The vestibular nuclei PROJECT TO the abducens nucleus; the abducens
    # nucleus is the OUTPUT.

Reaching the oculomotor nucleus (recommended consumer pattern — the
midbrain medial rectus nucleus)::

    # The oculomotor nucleus is the MIDBRAIN somatic motor nucleus:
    #
    #   .../midbrain/cranial_nerve_nuclei/left/oculomotor_nucleus/
    #
    # The abducens internuclear neurons PROJECT TO the CONTRALATERAL
    # (right) medial rectus subnucleus of the oculomotor nucleus via the
    # MLF — this is a CROSSED projection, not an identity.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        abducens_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
            f"{side}.abducens_nucleus"
        )
        # resolve abducens_path through the memory/recall layer

Neuron-population-level detail (not wired — consult references)::

    # The abducens nucleus's neuron populations are prose, not modules:
    #   motoneurons          -> left lateral rectus (left eye abduction)
    #   internuclear neurons -> right medial rectus subnucleus via right
    #                           MLF (right eye adduction, conjugate gaze)
    #
    # Do not attempt to resolve these as sub-paths of the abducens
    # nucleus.

References
----------
*   **Canonical oculomotor anatomy:** Leigh, R.J., Zee, D.S. (2015).
    *The Neurology of Eye Movements*, 5th ed. (Abducens nucleus and
    horizontal gaze — definitive.)
*   **Neuroanatomy of the oculomotor system:** Büttner-Ennever, J.A.
    (ed.) (1988). *Neuroanatomy of the Oculomotor System*. (Abducens
    nucleus motoneurons and internuclear neurons.)
*   **Brainstem anatomy:** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (Abducens nucleus in
    overview.)
*   **Neuroanatomy atlas:** Haines, D.E. (2012). *Neuroanatomy: An Atlas
    of Structures, Sections, and Systems*, 8th ed. (Abducens nucleus and
    the facial colliculus.)
*   **Eye movement disorders:** Pierrot-Deseilligny, C., Milea, D.,
    Müri, R.M. (2019). *Eye Movement Disorders: A Practical Guide*.
    (Abducens nucleus vs. abducens nerve vs. MLF vs. PPRF lesions.)
*   **Clinical neuro-ophthalmology:** Miller, N.R., Subramanian, P.S.,
    Patel, V.R. (eds.) (2022). *Walsh and Hoyt's Clinical
    Neuro-Ophthalmology*, 6th ed. (Sixth nerve palsy, horizontal gaze
    palsy, INO, one-and-a-half syndrome.)
*   **Facial nerve and nucleus (contrast — the sibling):** May, M.,
    Schaitkin, B.M. (2000). *The Facial Nerve*, 2nd ed. (Facial nerve
    nucleus and the internal genu of CN VII that loops around the
    abducens nucleus.)
*   **MLF and INO (contrast — the white-matter tract):**
    Pierrot-Deseilligny, C., et al. (2019). *Eye Movement Disorders*.
    (MLF and internuclear ophthalmoplegia — distinct from abducens
    nucleus lesions.)
*   **PPRF (contrast — the upstream burst generator):** Leigh, R.J.,
    Zee, D.S. (2015). *The Neurology of Eye Movements*, 5th ed. (PPRF
    and horizontal saccadic burst generation — upstream of the abducens
    nucleus.)
*   **NPH (contrast — the neural integrator):** Cannon, S.C., Robinson,
    D.A. (1987). "Loss of the neural integrator of the oculomotor system
    from brain stem lesions in monkey." *Journal of Neurophysiology*
    57:1383–1409. (NPH as the horizontal gaze neural integrator.)
*   **Vestibular nuclei (contrast — the VOR input):** Kandel, E.R.,
    Schwartz, J.H., Jessell, T.M., Siegelbaum, S.A., Hudspeth, A.J.
    (2013). *Principles of Neural Science*, 5th ed. (Vestibular nuclei
    and the vestibulo-ocular reflex — upstream of the abducens nucleus.)
*   **SLEA (contrast — the abducens nucleus is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT the abducens nucleus.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical pathway
    to the right amygdala mediating 'unseen' fear." *PNAS* 96:1680–1685.
    (Right amygdala and fear; the association belongs to the **amygdala
    module** — the **central nucleus** and the **basolateral nuclei** —
    not to the abducens nucleus.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Abducens nucleus in overview.)
*   NeuroNames — Abducens nucleus (left); FMA — Abducens nucleus (left
    member).
"""