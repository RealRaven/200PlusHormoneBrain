"""
infrastructure.brainparts.midbrain.tectum
=========================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── tectum                      <-- THIS MODULE (region container)
    │   ├── left
    │   │   ├── superior_colliculus
    │   │   └── inferior_colliculus
    │   └── right
    │       ├── superior_colliculus
    │       └── inferior_colliculus
    ├── tegmentum
    ├── pretectum
    ├── cerebral_aqueduct
    ├── cerebral_peduncle
    └── cranial_nerve_nuclei

**Primary synonym:** Tectum; tectum mesencephali; tectal region;
tectal plate; **the colliculi**; **the corpora quadrigemina** (the
four colliculi together — superior + inferior, left + right — an
older term still used clinically).
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). The tectum is a **region** of the **dorsal midbrain**
— it is the **"roof" (tectum)** of the **midbrain**, lying **dorsal
to the cerebral aqueduct** and **dorsal to the tegmentum**. It
contains the **superior colliculus** (rostral, visual/oculomotor
orienting, saccade command generation) and the **inferior
colliculus** (caudal, auditory relay) — **each paired** (left/right).
Together the four colliculi form the **corpora quadrigemina** (four
bodies) — the older term for the entire tectal plate.
**Container status:** **This module is a REGION CONTAINER, not a
leaf.** It holds the **two colliculi** — each **paired** (a `left/`
leaf and a `right/` leaf). The container imposes **aggregation
rules** on the colliculi but does **not** itself carry a single
anatomical function — every functional claim belongs to a **child**
(the **superior colliculus** for saccade command generation and
visual orienting; the **inferior colliculus** for auditory relay).
See *Expected Structural Children*.
**Developmental designation:** **Mesencephalic** — the tectum is
**unambiguously** part of the **mesencephalon**, unlike the pretectum
(which is at the diencephalon-midbrain junction) and unlike the
tegmentum (which is mesencephalic but ventral). The tectum is
**one of the cleanest midbrain regions** in the tree — no contested
placement, no junction ambiguity.
**Structural parent:** ``.../midbrain/`` → **direct child** of the
midbrain container, as a **region container** peer to
``tegmentum/``, ``pretectum/``, ``cerebral_aqueduct/``,
``cerebral_peduncle/``, and ``cranial_nerve_nuclei/``.
**Structural children (expected — the tree is authoritative):**
*   ``left/`` — the **left colliculi** — a side-scoped container
    holding the **left superior colliculus** and the **left inferior
    colliculus**.
*   ``right/`` — the **right colliculi** — a side-scoped container
    holding the **right superior colliculus** and the **right
    inferior colliculus**.
Each of the two side containers is expected to hold:
*   ``superior_colliculus/`` — the **saccade command generator** and
    **visual/oculomotor orienting** structure — **rostral** colliculus
    — at the level of the **oculomotor nucleus (CN III)**. **Paired**
    (left/right).
*   ``inferior_colliculus/`` — the **auditory relay** — **caudal**
    colliculus — at the level of the **trochlear nucleus (CN IV)**.
    **Paired** (left/right).
**Boundary status (DORSAL MIDBRAIN — the tectum is the "ROOF" of the
midbrain, DORSAL to the cerebral aqueduct):** **Boundary case — the
tectum is the DORSAL MIDBRAIN — the "roof" (tectum) of the midbrain,
**dorsal to the cerebral aqueduct** and **dorsal to the
tegmentum**.** The midbrain has two principal longitudinal
compartments — the **tectum** (dorsal) and the **tegmentum**
(ventral) — separated by the **cerebral aqueduct**. The tectum
contains the **colliculi**; the tegmentum contains the **substantia
nigra**, the **ventral tegmental area**, the **red nucleus**, the
**periaqueductal gray**, the **CN III, IV, Vm, and EW nuclei**, the
**riMLF**, the **interstitial nucleus of Cajal**, and the **midbrain
reticular formation**. **They are DIFFERENT COMPARTMENTS of the
midbrain** — the **tectum** is **dorsal**; the **tegmentum** is
**ventral**. Consumers must **not** conflate the tectum with the
tegmentum, and must **not** resolve a tegmentum structure through
the tectum path (or vice versa).
**Boundary status (NOT the pretectum — the pretectum is ROSTRAL to
the superior colliculus, at the DIENCEPHALON-MIDBRAIN JUNCTION):**
**Boundary case — the tectum is NOT the pretectum.** The
**pretectum** (``.../midbrain/pretectum/``) is a **separate
region** at the **diencephalon-midbrain junction** — **rostral** to
the superior colliculus — containing the **olivary pretectal
nucleus**, the **nucleus of the optic tract**, the **anterior,
posterior, and medial pretectal nuclei**. **They are DIFFERENT
REGIONS in DIFFERENT functional systems** — the **tectum** is
**saccadic and auditory** (via the SC and IC); the **pretectum** is
**pupillary and optokinetic** (via the olivary pretectal nucleus and
the nucleus of the optic tract). **The superior colliculus drives
saccades; the pretectum drives the pupillary light reflex.** These
are **different functional systems**. Consumers must **not** conflate
the tectum with the pretectum, and must **not** resolve the
pretectal nuclei through the tectum path. See
``.../midbrain/pretectum/`` for the pretectum container and its
contested-placement reconciliation.
**Boundary status (NOT the thalamic relays — the LGN and MGN are
DIENCEPHALON, and the colliculi project to them but are not them):**
**Boundary case — the tectum is NOT the lateral geniculate body
(LGN) or the medial geniculate body (MGN).** The **LGN**
(``.../forebrain/diencephalon/thalamus/lateral_geniculate_body/``)
is the **thalamic visual relay** to **V1** — it receives input from
the **retinal ganglion cells** (via the optic tract) and from the
**visual cortex** (corticothalamic feedback), and it projects to
**V1** for **conscious visual perception**. The **MGN**
(``.../forebrain/diencephalon/thalamus/medial_geniculate_body/``)
is the **thalamic auditory relay** to **A1** — it receives input
from the **inferior colliculus** (via the **brachium of the inferior
colliculus**) and projects to **A1** for **conscious auditory
perception**. **The colliculi are UPSTREAM of the thalamic relays**
— the **SC** projects to the **pulvinar** and to the **saccade
generators** (PPRF, riMLF, CN III/IV nuclei) — **not** to the
LGN; the **IC** projects to the **MGN** — **not** the other way
around. **They are DIFFERENT STRUCTURES in DIFFERENT functional
systems** — the **LGN** and **MGN** are **thalamic relays to
cortex** for **conscious perception**; the **SC** and **IC** are
**midbrain orienting and relay structures**. Consumers must **not**
conflate the colliculi with the thalamic relays, and must **not**
resolve the LGN or MGN through the tectum path.
**Boundary status (NOT the CN nuclei — the CN III, IV, Vm, and EW
nuclei are TEGMENTUM structures at the COLLICULAR LEVELS):**
**Boundary case — the tectum is NOT the cranial nerve nuclei.** The
**oculomotor nucleus** (CN III), the **Edinger-Westphal nucleus**
(CN IIIp), the **mesencephalic trigeminal nucleus** (CN Vm), and
the **trochlear nucleus** (CN IV) are **tegmentum** structures
(``.../cranial_nerve_nuclei/`` and ``.../tegmentum/``), **not**
tectum structures. **They sit at the SAME rostrocaudal levels as
the colliculi** — the **oculomotor/EW/mesV nuclei** are at the
**superior colliculus** level; the **trochlear nucleus** is at the
**inferior colliculus** level — but they are in the **tegmentum**,
**ventral to the cerebral aqueduct**, while the colliculi are in
the **tectum**, **dorsal to the aqueduct**. **They are DIFFERENT
STRUCTURES in DIFFERENT midbrain compartments** — the **colliculi**
are **tectum**; the **CN nuclei** are **tegmentum**. The
**superior colliculus DRIVES the CN III/IV nuclei** (via the
**tectobulbar tract** to the PPRF, riMLF, and the CN nuclei) — but
**the colliculus is not the nucleus**. Consumers must **not**
conflate the colliculi with the CN nuclei, and must **not** resolve
the CN nuclei through the tectum path. See *Collicular Levels and
the Rostrocaudal Ordering* below.
**Boundary status (NOT the PPRF, riMLF, or interstitial nucleus of
Cajal — those are PREMOTOR SACCADE GENERATORS, DOWNSTREAM of the
superior colliculus):** **Boundary case — the tectum is NOT the
PPRF, the riMLF, or the interstitial nucleus of Cajal.** The
**paramedian pontine reticular formation (PPRF)**
(``.../hindbrain/metencephalon/pons/pprf/``) is the **horizontal
saccade generator**; the **rostral interstitial nucleus of the MLF
(riMLF)** and the **interstitial nucleus of Cajal**
(``.../tegmentum/left/`` and ``.../tegmentum/right/``) are the
**vertical gaze centers**. **They are PREMOTOR SACCADE
GENERATORS** — they **transform** the **saccade command** from the
**superior colliculus** into the **premotor saccade signal** that
drives the **CN III, IV, and VI nuclei**. **They are DOWNSTREAM of
the superior colliculus** in the saccade hierarchy. **They are
DIFFERENT STRUCTURES in DIFFERENT midbrain/brainstem
compartments** — the **SC** is the **saccade command generator**;
the **PPRF/riMLF** are the **premotor saccade generators**.
Consumers must **not** conflate the tectum with the premotor
saccade generators, and must **not** resolve the PPRF/riMLF through
the tectum path.
**Boundary status (NOT the lateral lemniscus — the LL is an
AUDITORY CONDUCTION PATHWAY that projects TO the inferior
colliculus):** **Boundary case — the tectum is NOT the lateral
lemniscus.** The **lateral lemniscus**
(``.../hindbrain/metencephalon/pons/lateral_lemniscus/``) is the
**ascending auditory fiber tract** — a **conduction pathway** —
that carries auditory signals from the **cochlear nuclei** and the
**superior olivary complex** to the **inferior colliculus**. **It
is a CONDUCTION PATHWAY** — **white matter** — that **projects TO**
the IC. **The IC is a NUCLEUS** — **grey matter**. **They are
DIFFERENT STRUCTURES** — the **LL** is **auditory conduction**;
the **IC** is **auditory relay**. Consumers must **not** conflate
the tectum with the lateral lemniscus, and must **not** resolve the
LL through the tectum path.
**Boundary status (NOT the brachium of the superior colliculus or
the brachium of the inferior colliculus — those are CONDUCTION
PATHWAYS):** **Boundary case — the tectum is NOT the brachium of
the superior colliculus (BSC) or the brachium of the inferior
colliculus (BIC).** The **BSC** is a **conduction pathway** — it
carries **retinal input** from the **optic tract** to the
**superior colliculus** (and to the pretectum and the LGN via the
optic tract proper). The **BIC** is a **conduction pathway** — it
carries **auditory output** from the **inferior colliculus** to the
**medial geniculate body** (thalamic auditory relay). **They are
CONDUCTION PATHWAYS** — **white matter** — that **connect** the
colliculi to their upstream and downstream targets. **The colliculi
are NUCLEI** — **grey matter**. **They are DIFFERENT STRUCTURES** —
the **BSC** and **BIC** are **conduction pathways**; the **SC** and
**IC** are **nuclei**. Consumers must **not** conflate the tectum
with the brachia, and must **not** resolve the brachia through the
tectum path.
**Boundary status (PAIRED STRUCTURE — a CONTAINER for left/right,
each holding TWO colliculi):** **Boundary case — the tectum is a
PAIRED structure, wired as a CONTAINER.** The **left colliculi**
(superior + inferior) and the **right colliculi** (superior +
inferior) are the **side-scoped containers** under this region
container. Each side container holds **two leaves**: the
**superior colliculus** and the **inferior colliculus**. Consumers
must **not** resolve the tectum as a single midline leaf — the
four colliculi (the **corpora quadrigemina**) are the **paired
leaves** under the two side containers.
**Boundary status (STRUCTURE-CLASS TAXONOMY — the two colliculi are
in DIFFERENT classes, and NEITHER carries a coupling warning):**
**Boundary case — the two colliculi are in DIFFERENT functional
classes, and NEITHER carries a coupling warning.**
*   **Superior colliculus** — a **sensorimotor integration / saccade
    command generator** — it receives **visual, auditory, and
    somatosensory** input and generates **saccade commands** to the
    **PPRF** (horizontal saccades) and the **riMLF** (vertical
    saccades). **No coupling warning** — it is **not an oscillator**;
    it is a **sensorimotor integration** structure that **generates
    motor commands**.
*   **Inferior colliculus** — an **auditory relay** — it receives
    **auditory input** from the **cochlear nuclei**, the **superior
    olivary complex**, and the **lateral lemniscus**, and projects
    to the **medial geniculate body** (thalamic auditory relay) and
    to the **superior colliculus** (for auditory orienting and
    audiovisual integration). **No coupling warning** — it is **not
    an oscillator**; it is a **sensory relay**.
**Both carry NO coupling warning** — same rule as motor nuclei,
premotor pools, sensor nuclei, relay nuclei, and conduction
pathways. **The superior colliculus is a sensorimotor INTEGRATION
structure** — a **new class** in the family's taxonomy, distinct
from the **sensory relay** class (pretectum, IC) and the **premotor
saccade generator** class (PPRF, riMLF) — but **carrying the same
NO-coupling-warning rule**. See *The Saccade Hierarchy* and
*Lateralization Notes*.

Overview
--------
The tectum is the **dorsal midbrain** — the **"roof" (tectum)** of
the midbrain, **dorsal to the cerebral aqueduct** and **dorsal to
the tegmentum**. It contains the **superior colliculus** (rostral,
visual/oculomotor orienting and **saccade command generation**) and
the **inferior colliculus** (caudal, **auditory relay**), **each
paired** (left/right). Together, the four colliculi form the
**corpora quadrigemina** (four bodies) — the older term for the
entire tectal plate. The tectum is a **region container** under the
midbrain — its children are the **two colliculi per side**, wired
as **left** and **right** side containers, each holding a
**superior colliculus** leaf and an **inferior colliculus** leaf.

**The tectum is UNAMBIGUOUSLY MIDBRAIN.** Unlike the pretectum
(which is at the diencephalon-midbrain junction, with contested
placement), the tectum is **mesencephalic** — it is one of the
**cleanest midbrain regions** in the tree, with **no contested
placement** and **no junction ambiguity**. The only boundary issues
are against the **tegmentum** (separated by the **cerebral
aqueduct**), the **pretectum** (separate region, **rostral** to the
superior colliculus), and the **thalamic relays** (the LGN and MGN,
which the colliculi project to but are **not**).

**The tectum is the CONTAINER, NOT a functional leaf.** Every
functional claim belongs to a **child** — the **superior
colliculus** for saccade command generation and visual orienting;
the **inferior colliculus** for auditory relay. Consumers must
resolve the **child** that carries the function.

**The tectum is a PAIRED-STRUCTURE region.** Each of the **two
colliculi** is **paired** (a `left/` leaf and a `right/` leaf). The
four colliculi together are the **corpora quadrigemina**.

**The tectum's two colliculi are in DIFFERENT structure classes.**
The **superior colliculus** is a **sensorimotor integration /
saccade command generator** — **not** a pure sensory relay, and
**not** an oscillator. The **inferior colliculus** is an
**auditory relay** — a **sensory relay**, same class as the
pretectum. **Both carry NO coupling warning** — same rule as motor
nuclei, premotor pools, sensor nuclei, relay nuclei, and conduction
pathways.

**The superior colliculus is the COMMAND level of the saccade
hierarchy.** The saccade hierarchy is: **SC (command) → PPRF /
riMLF (premotor) → CN III / IV / VI nuclei (motor) → extraocular
muscles (effector)**. The **SC is at the TOP** of this hierarchy —
it is the **sensorimotor integration** structure that **decides
where to look**; the **PPRF and riMLF** are the **premotor** stages
that **execute** the command; the **CN nuclei** are the **motor**
stage; the **extraocular muscles** are the **effector**.

Collicular Levels and the Rostrocaudal Ordering
----------------------------------------------
**The two colliculi sit at DIFFERENT rostrocaudal levels, and each
level aligns with a distinct set of CN nuclei.** This is one of the
**most useful anatomical landmarks** of the midbrain — it lets you
localize any midbrain section by its level relative to the colliculi.

*   **Superior colliculus level (rostral)** — the **superior
    colliculus** is at the level of the **oculomotor nucleus**
    (CN III), the **Edinger-Westphal nucleus** (CN IIIp), and the
    **mesencephalic trigeminal nucleus** (mesV). **Also at this
    level:** the **substantia nigra pars reticulata** (ventral),
    the **red nucleus** (rostral part), the **pretectum** (just
    rostral), and the **posterior commissure** (just rostral).

*   **Inferior colliculus level (caudal)** — the **inferior
    colliculus** is at the level of the **trochlear nucleus**
    (CN IV). **Also at this level:** the **decussation of the
    trochlear nerve** (in the **superior medullary velum** — just
    caudal), the **decussation of the superior cerebellar
    peduncle** (just caudal), and the **caudal end of the
    periaqueductal gray**.

**The pretectum is ROSTRAL to the superior colliculus** — at the
**diencephalon-midbrain junction**. **The trochlear nucleus is
CAUDAL to the oculomotor nucleus** — at the **inferior colliculus**
level, **not** the superior colliculus level. **The two colliculi
are landmarks for these levels** — the superior colliculus is the
"CN III / EW / mesV" landmark; the inferior colliculus is the
"CN IV" landmark.

**This rostrocaudal ordering is preserved in the leaf modules** —
the `oculomotor_nucleus`, `edinger_westphal_nucleus`, and
`mesencephalic_trigeminal_nucleus` leaves all state that they are
at the **superior colliculus** level; the `trochlear_nucleus` leaf
states that it is at the **inferior colliculus** level. **The
colliculi are the anchors for those statements** — and the tectum
container is the place where the anchor is made explicit.

The Saccade Hierarchy (the superior colliculus's function)
---------------------------------------------------------
The **superior colliculus** is the **command level** of the
**saccade hierarchy** — the **sensorimotor integration** structure
that **decides where to look** and **commands the saccade**. The
hierarchy is:

*   **SC (command level)** — the **superior colliculus** —
    **sensorimotor integration** — receives **visual, auditory, and
    somatosensory** input and generates **saccade commands** in a
    **retinotopic / motor map** of saccade vectors. **The SC is at
    the TOP of the saccade hierarchy.**

*   **PPRF / riMLF (premotor level)** — the **paramedian pontine
    reticular formation** (horizontal saccades) and the **rostral
    interstitial nucleus of the MLF** (vertical saccades) —
    **premotor saccade generators** — they **transform** the SC's
    saccade command into the **premotor saccade signal** that
    drives the CN nuclei. **The PPRF and riMLF are DOWNSTREAM of
    the SC.**

*   **CN III / IV / VI nuclei (motor level)** — the **oculomotor
    nucleus** (CN III), the **trochlear nucleus** (CN IV), and the
    **abducens nucleus** (CN VI) — **motor nuclei** — they
    **execute** the saccade by driving the **extraocular muscles**.
    **The CN nuclei are DOWNSTREAM of the PPRF / riMLF.**

*   **Extraocular muscles (effector level)** — the **six
    extraocular muscles** per eye — **the effectors** of the
    saccade. **The muscles are DOWNSTREAM of the CN nuclei.**

**The superior colliculus is NOT the PPRF, the riMLF, or the CN
nuclei** — it is **UPSTREAM of them** in the saccade hierarchy.
**The SC decides; the PPRF/riMLF execute; the CN nuclei drive; the
muscles move.** **Each level is a different structure** — the SC is
a **sensorimotor integration** structure; the PPRF/riMLF are
**premotor saccade generators**; the CN nuclei are **motor
nuclei**; the muscles are **effectors**. **All four levels carry
NO coupling warning** — same rule, different structures.

Expected Structural Children (prose — the tree is authoritative)
----------------------------------------------------------------
The tectum container is expected to hold **two side containers**
(``left/`` and ``right/``), each holding **two colliculi**:

*   **``superior_colliculus/``** — the **saccade command generator**
    and **visual/oculomotor orienting** structure — **rostral**
    colliculus — at the level of the **oculomotor nucleus (CN III)**,
    the **Edinger-Westphal nucleus** (CN IIIp), and the
    **mesencephalic trigeminal nucleus** (CN Vm). **Receives**
    visual input (from the retina via the **brachium of the superior
    colliculus**, and from the **visual cortex** via the
    **corticotectal pathway**), auditory input (from the **inferior
    colliculus** via the **brachium of the inferior colliculus**),
    and somatosensory input (from the **spinal cord** and the
    **trigeminal system**). **Projects** to the **PPRF**
    (horizontal saccades), the **riMLF** (vertical saccades), the
    **CN III/IV/VI nuclei** (via the **tectobulbar tract**), and
    the **pulvinar** (thalamic visual attention). **The
    retinotopic-to-motor map** — the superficial layers contain a
    **retinotopic map**; the deeper layers contain a **motor map**
    of saccade vectors, aligned with the retinotopic map.
    **Paired** (left/right).

*   **``inferior_colliculus/``** — the **auditory relay** — **caudal**
    colliculus — at the level of the **trochlear nucleus (CN IV)**.
    **Receives** auditory input from the **cochlear nuclei** (via
    the **lateral lemniscus**), from the **superior olivary
    complex** (via the **lateral lemniscus**), and from the
    **auditory cortex** (corticofugal feedback). **Projects** to
    the **medial geniculate body** (thalamic auditory relay to
    **A1**) via the **brachium of the inferior colliculus**, and
    to the **superior colliculus** (for **auditory orienting** and
    **audiovisual integration**). **The tonotopic map** — the
    **central nucleus of the inferior colliculus** is
    **tonotopically organized** and processes **frequency and
    temporal features** of sound. The **external nucleus** contains
    a **map of auditory space** (for orienting). **Paired**
    (left/right).

**These are the expected children — the on-disk tree is the
authoritative source.** The container imposes the **aggregation
rules** below; the leaves impose the leaf-level contract (boundary
stacks, function, disorders, lateralization, references) documented
in the existing leaf modules.

Aggregation Rules (the container's contract on its children)
------------------------------------------------------------
The tectum container **imposes the following rules** on every leaf
under it. These are **inherited** from the midbrain container and
**specialized** for the tectum's role as a **paired region
container** with **two functional classes**:

*   **PAIRED-LEAF DISCIPLINE.** Each colliculus is a **paired
    structure** — a `left/` leaf and a `right/` leaf. **The four
    colliculi together** are the **corpora quadrigemina**. There is
    **no midline colliculus** — both the superior colliculus and the
    inferior colliculus are **paired**.
*   **TWO-CLASS DISCIPLINE.** The **superior colliculus** is a
    **sensorimotor integration / saccade command generator**; the
    **inferior colliculus** is an **auditory relay**. **They are
    DIFFERENT functional classes** — and each carries **NO coupling
    warning** for **different reasons** (the SC is not an oscillator;
    the IC is not an oscillator). **Both are no-coupling-warning.**
    Consumers must **not** treat the two colliculi as a **single
    class** — the SC and the IC are **functionally distinct** (the
    SC is **sensorimotor integration**; the IC is **sensory relay**).
*   **SACCADE-HIERARCHY DISCIPLINE.** The **superior colliculus** is
    the **COMMAND level** of the saccade hierarchy — **UPSTREAM** of
    the **PPRF / riMLF** (premotor saccade generators) and the
    **CN III/IV/VI nuclei** (motor nuclei). **The SC is not the
    PPRF, not the riMLF, not the CN nuclei, not the extraocular
    muscles** — it is the **command level** of the hierarchy.
    Consumers must **not** conflate the SC with the downstream
    structures, and must **not** resolve the PPRF/riMLF/CN nuclei
    through the SC path.
*   **AUDITORY-RELAY DISCIPLINE.** The **inferior colliculus** is an
    **auditory relay** — **UPSTREAM** of the **medial geniculate
    body** (thalamic auditory relay to **A1**) and **UPSTREAM** of
    the **superior colliculus** (for **auditory orienting** and
    **audiovisual integration**). **The IC is not the MGN, not the
    lateral lemniscus, not the auditory cortex** — it is a
    **midbrain auditory relay**. Consumers must **not** conflate
    the IC with the downstream auditory structures, and must **not**
    resolve the MGN or the lateral lemniscus through the IC path.
*   **CHEMICALS-LAYER DISCIPLINE.** The **transmitter phenotypes** of
    the collicular neurons (glutamatergic, GABAergic, cholinergic,
    dopaminergic subpopulations) are **``chemicals_hormones``-layer
    facts** — documented as **prose** in the leaves, **never
    imported**. Dependency DAG unchanged: ``chemicals_hormones →
    memory → brainparts``.
*   **ROSTROCAUDAL-ANCHOR DISCIPLINE.** The **superior colliculus**
    is the **rostral** colliculus — at the level of **CN III, EW,
    and mesV**. The **inferior colliculus** is the **caudal**
    colliculus — at the level of **CN IV**. **The colliculi are the
    anatomical anchors** for these levels — consumers localizing a
    midbrain section by its rostrocaudal level should use the
    **colliculi** as the primary landmark.
*   **JUNCTION-FREE — the tectum is UNAMBIGUOUSLY MIDBRAIN.** Unlike
    the pretectum (contested placement), the tectum is **cleanly
    mesencephalic** — no reconciliation needed. The only boundary
    issues are against the **tegmentum** (separated by the
    **cerebral aqueduct**), the **pretectum** (separate region,
    **rostral**), and the **thalamic relays** (LGN, MGN — the
    colliculi project to **different** structures, not to the LGN).

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-lobe imports.** The tectum container does **not**
    import from ``../forebrain/`` or ``../hindbrain/``. The tectum's
    relationships to the **pretectum**, the **tegmentum**, the
    **thalamic relays** (LGN, MGN), the **CN nuclei** (III, IV, Vm,
    EW), the **PPRF**, the **riMLF**, the **interstitial nucleus of
    Cajal**, the **lateral lemniscus**, the **brachia of the
    colliculi**, and the **extraocular muscles** are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **transmitter
    phenotypes** of the collicular neurons are
    ``chemicals_hormones``-layer facts — documented as **prose**,
    **never imported**.
*   **CONTAINER — paired colliculi.** The left and right colliculi
    are the **structural children**. The **two colliculi per side**
    are **sub-container children** (`left/superior_colliculus/`,
    `left/inferior_colliculus/`, `right/superior_colliculus/`,
    `right/inferior_colliculus/`).
*   **UNAMBIGUOUSLY MESENCEPHALIC — NO CONTESTED PLACEMENT.** The
    tectum is **cleanly midbrain**. Unlike the pretectum (which
    required a contested-placement reconciliation), the tectum has
    **no junction ambiguity**. Consumers can resolve the tectum
    under the midbrain path with **no caveat**.
*   **TWO-CLASS DISCIPLINE — SC and IC are DIFFERENT classes.** The
    **SC** is a **sensorimotor integration / saccade command
    generator**; the **IC** is an **auditory relay**. **Both carry
    NO coupling warning** — but for **different reasons** (neither
    is an oscillator). Consumers must **not** treat them as a
    single class.
*   **SACCADE HIERARCHY — SC is the COMMAND level.** SC (command) →
    PPRF / riMLF (premotor) → CN III/IV/VI nuclei (motor) →
    extraocular muscles (effector). **The SC is UPSTREAM of the
    PPRF, riMLF, and CN nuclei.** Consumers must **not** conflate
    the SC with the downstream structures.
*   **AUDITORY RELAY — IC is UPSTREAM of the MGN.** IC (midbrain
    relay) → MGN (thalamic relay) → A1 (auditory cortex).
    **The IC is UPSTREAM of the MGN.** Consumers must **not**
    conflate the IC with the MGN.
*   **ROSTROCAUDAL ANCHORS — SC is at CN III level; IC is at CN IV
    level.** The **colliculi are the anatomical anchors** for these
    levels. Consumers localizing a midbrain section should use the
    **colliculi** as the primary landmark.
*   **NOT the pretectum — the pretectum is a SEPARATE REGION,
    ROSTRAL to the SC.** The pretectum is **pupillary and
    optokinetic**; the tectum is **saccadic and auditory**.
    Consumers must **not** conflate the two regions.
*   **NOT the tegmentum — the tegmentum is VENTRAL to the cerebral
    aqueduct.** The tectum is **dorsal** to the aqueduct.
*   **NOT the CN nuclei — the CN III, IV, Vm, and EW nuclei are
    TEGMENTUM structures** at the collicular levels. The SC drives
    the CN nuclei via the tectobulbar tract — but **connectivity is
    not identity**.
*   **NOT the PPRF, riMLF, or interstitial nucleus of Cajal — those
    are PREMOTOR SACCADE GENERATORS**, **downstream** of the SC.
*   **NOT the lateral lemniscus — that is an AUDITORY CONDUCTION
    PATHWAY**, **upstream** of the IC.
*   **NOT the brachia of the colliculi — those are CONDUCTION
    PATHWAYS.** The brachium of the SC carries retinal input to the
    SC; the brachium of the IC carries auditory output from the IC
    to the MGN.
*   **NOT the thalamic relays (LGN, MGN) — those are DIENCEPHALON.**
    The SC does **not** project to the LGN; the IC **does** project
    to the MGN. Different structures, different functional systems.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The tectum is a
    **local region container** under the midbrain — no cross-listing.
*   **The on-disk tree is authoritative.**

Usage
-----
Resolve the container by path::

    from infrastructure.brainparts.midbrain import tectum

Resolve a colliculus leaf by path::

    from infrastructure.brainparts.midbrain.tectum.left import superior_colliculus
    from infrastructure.brainparts.midbrain.tectum.left import inferior_colliculus
    from infrastructure.brainparts.midbrain.tectum.right import superior_colliculus
    from infrastructure.brainparts.midbrain.tectum.right import inferior_colliculus

Or by fully-qualified path string (leaves, not the container)::

    left_sc_path = "midbrain.tectum.left.superior_colliculus"
    left_ic_path = "midbrain.tectum.left.inferior_colliculus"
    right_sc_path = "midbrain.tectum.right.superior_colliculus"
    right_ic_path = "midbrain.tectum.right.inferior_colliculus"

**Do not** assume the tectum is the **pretectum**. The **pretectum**
is a **separate region** at the **diencephalon-midbrain junction**,
**rostral** to the superior colliculus. The **tectum** is the
**dorsal midbrain** — the **colliculi**. **They are DIFFERENT
REGIONS in DIFFERENT functional systems** — the **pretectum** is
**pupillary and optokinetic**; the **tectum** is **saccadic and
auditory**. Consumers must **not** conflate the two, and must
**not** resolve the pretectal nuclei through the tectum path.

**Do not** assume the tectum is the **tegmentum**. The **tegmentum**
is the **ventral midbrain** — it contains the **substantia nigra**,
the **VTA**, the **red nucleus**, the **PAG**, the **CN nuclei**
(III, IV, Vm, EW), the **riMLF**, the **interstitial nucleus of
Cajal**, and the **midbrain reticular formation**. **The tectum is
dorsal to the cerebral aqueduct**; the **tegmentum is ventral to the
cerebral aqueduct**. **They are DIFFERENT COMPARTMENTS of the
midbrain** — the **tectum** is **dorsal**; the **tegmentum** is
**ventral**. Consumers must **not** conflate the two.

**Do not** assume the tectum is the **CN nuclei**. The **CN III, IV,
Vm, and EW nuclei** are **tegmentum** structures — they sit at the
**same rostrocaudal levels** as the colliculi but are in the
**ventral (tegmental) compartment**, **below the cerebral aqueduct**.
**The SC drives the CN III/IV nuclei** via the **tectobulbar tract**
to the PPRF, riMLF, and CN nuclei — but **the colliculus is not the
nucleus**.

**Do not** assume the tectum is the **PPRF, the riMLF, or the
interstitial nucleus of Cajal**. Those are **premotor saccade
generators** — **downstream** of the SC in the saccade hierarchy.
The **SC decides**; the **PPRF/riMLF execute**.

**Do not** assume the tectum is the **lateral lemniscus**. The
**lateral lemniscus** is an **auditory conduction pathway** —
**upstream** of the IC. **The IC receives from it**; **the IC is
not it**.

**Do not** assume the tectum is the **brachia of the colliculi**.
The **brachium of the superior colliculus** and the **brachium of
the inferior colliculus** are **conduction pathways** — **white
matter** — that connect the colliculi to their upstream and
downstream targets. **The colliculi are nuclei** — **grey matter**.

**Do not** assume the tectum is the **thalamic relays (LGN, MGN)**.
The **LGN** is the **visual relay to V1** — the **SC does not
project to it**. The **MGN** is the **auditory relay to A1** — the
**IC does project to it**, but the **IC is not the MGN**. **They
are DIFFERENT STRUCTURES in DIFFERENT functional systems** — the
**LGN and MGN** are **thalamic relays to cortex** for **conscious
perception**; the **SC and IC** are **midbrain orienting and relay
structures**.

**Do not** assume the **superior colliculus** is the **inferior
colliculus**. They are **DIFFERENT functional classes** — the
**SC** is a **sensorimotor integration / saccade command generator**;
the **IC** is an **auditory relay**. **Both carry NO coupling
warning** — but for **different reasons**. Consumers must **not**
treat them as a **single class**.

**Do not** import the **transmitter phenotypes** of the collicular
neurons into the midbrain structural layer. Those are
**``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the tectum.
**NEITHER colliculus is an oscillator** — the **SC** is a
**sensorimotor integration** structure; the **IC** is a **sensory
relay**. **Both carry NO coupling warning** — same rule as motor
nuclei, premotor pools, sensor nuclei, relay nuclei, and conduction
pathways.

Iterating the tectum's children (recommended consumer pattern)::

    import pkgutil
    import infrastructure.brainparts.midbrain.tectum as tectum_pkg

    TECTUM_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(tectum_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("left", "right")
    #
    # Each side container holds the two colliculi:
    # ("superior_colliculus", "inferior_colliculus")

Reaching the pretectum (recommended consumer pattern — NOTE the
pretectum is a SEPARATE REGION, ROSTRAL to the SC)::

    # The pretectum is a SEPARATE REGION at the diencephalon-midbrain
    # junction — ROSTRAL to the superior colliculus:
    #
    #   brainparts.midbrain.pretectum
    #
    # The pretectum is PUPILLARY AND OPTOKINETIC; the tectum is
    # SACCADIC AND AUDITORY. Different regions, different functional
    # systems.

Reaching the tegmentum (recommended consumer pattern — NOTE the
tegmentum is VENTRAL to the cerebral aqueduct)::

    # The tegmentum is the VENTRAL MIDBRAIN — substantia nigra, VTA,
    # red nucleus, PAG, CN III/IV/Vm/EW nuclei, riMLF, interstitial
    # nucleus of Cajal, midbrain reticular formation:
    #
    #   brainparts.midbrain.tegmentum
    #
    # The tectum is DORSAL to the cerebral aqueduct; the tegmentum
    # is VENTRAL. Different midbrain compartments.

Reaching the CN nuclei (recommended consumer pattern — NOTE the CN
nuclei are TEGMENTUM structures at the COLLICULAR LEVELS)::

    # The CN III, EW, mesV nuclei are at the SUPERIOR COLLICULUS
    # level; the CN IV nucleus is at the INFERIOR COLLICULUS level.
    # But they are TEGMENTUM structures, NOT tectum structures:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #
    # The SC drives the CN nuclei via the tectobulbar tract to the
    # PPRF, riMLF, and CN nuclei — but the colliculus is not the
    # nucleus.

Reaching the PPRF (recommended consumer pattern — the HORIZONTAL
SACCADE GENERATOR, DOWNSTREAM of the SC)::

    # The PPRF is the HORIZONTAL SACCADE GENERATOR — a pontine
    # premotor structure, DOWNSTREAM of the superior colliculus in
    # the saccade hierarchy:
    #
    #   brainparts.hindbrain.metencephalon.pons.pprf
    #
    # The SC decides; the PPRF executes. Different structures.

Reaching the riMLF and the interstitial nucleus of Cajal
(recommended consumer pattern — the VERTICAL SACCADE GENERATORS,
DOWNSTREAM of the SC)::

    # The riMLF and the interstitial nucleus of Cajal are VERTICAL
    # SACCADE GENERATORS — premotor structures, DOWNSTREAM of the
    # superior colliculus:
    #
    #   brainparts.midbrain.tegmentum.left.riMLF
    #   brainparts.midbrain.tegmentum.left.interstitial_nucleus_of_cajal
    #
    # The SC decides; the riMLF / interstitial nucleus of Cajal
    # execute. Different structures.

Reaching the lateral lemniscus (recommended consumer pattern — the
AUDITORY CONDUCTION PATHWAY, UPSTREAM of the IC)::

    # The lateral lemniscus is an AUDITORY CONDUCTION PATHWAY —
    # carries auditory input from the cochlear nuclei and superior
    # olive TO the inferior colliculus:
    #
    #   brainparts.hindbrain.metencephalon.pons.lateral_lemniscus
    #
    # The IC receives from the LL; the IC is NOT the LL.

Reaching the brachium of the superior colliculus and the brachium
of the inferior colliculus (recommended consumer pattern — the
CONDUCTION PATHWAYS)::

    # The brachium of the superior colliculus (BSC) carries RETINAL
    # input to the SC; the brachium of the inferior colliculus (BIC)
    # carries AUDITORY output from the IC to the medial geniculate
    # body:
    #
    #   brainparts.midbrain.tectum.left.brachium_of_the_superior_colliculus
    #   brainparts.midbrain.tectum.left.brachium_of_the_inferior_colliculus
    #
    # The brachia are CONDUCTION PATHWAYS; the SC and IC are NUCLEI.
    # Different structures.

Reaching the medial geniculate body (recommended consumer pattern —
the AUDITORY THALAMIC RELAY, DOWNSTREAM of the IC)::

    # The medial geniculate body (MGN) is the THALAMIC AUDITORY RELAY
    # to A1 — DOWNSTREAM of the inferior colliculus:
    #
    #   brainparts.forebrain.diencephalon.thalamus.medial_geniculate_body
    #
    # The IC projects to the MGN; the IC is NOT the MGN. Different
    # structures in different functional systems (IC: midbrain
    # auditory relay; MGN: thalamic auditory relay to cortex).

Reaching the lateral geniculate body (recommended consumer pattern —
the VISUAL THALAMIC RELAY, NOT a target of the SC)::

    # The lateral geniculate body (LGN) is the THALAMIC VISUAL RELAY
    # to V1 — CONSCIOUS VISION. The SC does NOT project to the LGN;
    # the SC projects to the pulvinar (visual attention) and to the
    # PPRF / riMLF / CN nuclei (saccades):
    #
    #   brainparts.forebrain.diencephalon.thalamus.lateral_geniculate_body
    #
    # The SC and the LGN are DIFFERENT STRUCTURES in DIFFERENT
    # functional systems (SC: midbrain orienting and saccade command;
    # LGN: thalamic visual relay to cortex).

The Saccade Hierarchy — detail (not wired — consult references)::

    # The saccade hierarchy — the SC is the COMMAND level:
    #
    #   SUPERIOR COLLICULUS (command level) — sensorimotor
    #     integration; receives visual, auditory, somatosensory
    #     input; generates saccade commands in a motor map
    #         |
    #         v
    #   PPRF / riMLF (premotor level) — premotor saccade
    #     generators; transform the SC's saccade command into the
    #     premotor saccade signal
    #         |
    #         v
    #   CN III / IV / VI nuclei (motor level) — motor nuclei;
    #     execute the saccade by driving the extraocular muscles
    #         |
    #         v
    #   Extraocular muscles (effector level) — the effectors of the
    #     saccade
    #
    # The SC is UPSTREAM of the PPRF/riMLF and the CN nuclei. The
    # SC decides; the PPRF/riMLF execute; the CN nuclei drive; the
    # muscles move. Each level is a DIFFERENT STRUCTURE. All four
    # levels carry NO coupling warning.
    #
    # Do not attempt to resolve the PPRF, riMLF, or CN nuclei as
    # sub-paths of the SC — they are DIFFERENT structures at
    # DIFFERENT levels of the hierarchy.

Collicular-levels detail (not wired — consult references)::

    # The two colliculi sit at DIFFERENT rostrocaudal levels, and
    # each level anchors a distinct set of structures:
    #
    #   SUPERIOR COLLICULUS level (rostral):
    #     - superior colliculus (tectum)
    #     - oculomotor nucleus (CN III) (tegmentum)
    #     - Edinger-Westphal nucleus (CN IIIp) (tegmentum)
    #     - mesencephalic trigeminal nucleus (CN Vm) (tegmentum)
    #     - substantia nigra pars reticulata (tegmentum, ventral)
    #     - red nucleus (rostral part) (tegmentum)
    #     - pretectum (just rostral)
    #     - posterior commissure (just rostral)
    #
    #   INFERIOR COLLICULUS level (caudal):
    #     - inferior colliculus (tectum)
    #     - trochlear nucleus (CN IV) (tegmentum)
    #     - decussation of the trochlear nerve (superior medullary
    #       velum — just caudal)
    #     - decussation of the superior cerebellar peduncle (just
    #       caudal)
    #     - caudal end of the periaqueductal gray
    #
    # The PRETECTUM is ROSTRAL to the SC. The TROCHLEAR NUCLEUS is
    # CAUDAL to the OCULOMOTOR NUCLEUS — at the inferior colliculus
    # level, not the superior colliculus level.
    #
    # Do not attempt to resolve the CN nuclei as sub-paths of the
    # colliculi — they are TEGMENTUM structures at the collicular
    # levels, not TECTUM structures.

References
----------
*   **Canonical tectum anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (The tectum as
    the dorsal midbrain — the superior and inferior colliculi, the
    corpora quadrigemina, the rostrocaudal ordering of the colliculi
    with the CN nuclei.)
*   **Superior colliculus — saccade command:** Sparks, D.L. (2002).
    "The brainstem control of saccadic eye movements." *Nature
    Reviews Neuroscience* 3:952–964. (The superior colliculus as the
    saccade command generator — its retinotopic and motor maps, its
    projections to the PPRF, riMLF, and CN nuclei via the
    tectobulbar tract.)
*   **Superior colliculus — sensorimotor integration:** Stein, B.E.,
    Stanford, T.R. (2008). "Multisensory integration: current issues
    from the perspective of the single neuron." *Nature Reviews
    Neuroscience* 9:255–266. (The superior colliculus as a
    sensorimotor integration structure — multisensory visual,
    auditory, and somatosensory integration in its deeper layers.)
*   **Superior colliculus — corticotectal pathway:** Wurtz, R.H.,
    Albano, J.E. (1980). "Visual-motor function of the primate
    superior colliculus." *Annual Review of Neuroscience* 3:189–226.
    (The visual input to the superior colliculus from the visual
    cortex — the corticotectal pathway; the visual orienting and
    saccade command functions.)
*   **Inferior colliculus — auditory relay:** Ehret, G., Romand, R.
    (eds.) (1997). *The Central Auditory System*. Oxford University
    Press. (The inferior colliculus — its ascending auditory inputs,
    its tonotopic organization, its projections to the medial
    geniculate body and the superior colliculus.)
*   **Inferior colliculus — auditory space map:** King, A.J.,
    Palmer, A.R. (1983). "Cells responsive to free-field auditory
    stimuli in guinea-pig superior colliculus: distribution and
    response properties." *Journal of Physiology* 342:361–381. (The
    auditory space map in the external nucleus of the inferior
    colliculus — the superior colliculus's auditory orienting
    function.)
*   **Corpora quadrigemina:** Kahle, W., Frotscher, M. (2003).
    *Color Atlas of Human Anatomy, Vol. 3: Nervous System and
    Sensory Organs*, 5th ed. (The corpora quadrigemina — the four
    colliculi — as the older term for the tectal plate; the
    rostrocaudal ordering of the colliculi.)
*   **Brachia of the colliculi:** Nieuwenhuys, R., Voogd, J., van
    Huijzen, C. (2008). *The Human Central Nervous System: A
    Synopsis and Atlas*, 4th ed. (The brachium of the superior
    colliculus and the brachium of the inferior colliculus —
    conduction pathways connecting the colliculi to their upstream
    and downstream targets.)
*   **PPRF and horizontal saccades (contrast — premotor saccade
    generator):** Cohen, B., Komatsuzaki, A. (1972). "Eye movements
    induced by stimulation of the pontine reticular formation:
    evidence for integration in oculomotor pathways." *Experimental
    Neurology* 36:101–117. (The PPRF as the horizontal saccade
    generator — a premotor structure DOWNSTREAM of the superior
    colliculus.)
*   **riMLF and vertical saccades (contrast — premotor saccade
    generator):** Büttner-Ennever, J.A., Büttner, U. (1988). "The
    reticular formation." In *Neuroanatomy of the Oculomotor System*
    (Büttner-Ennever, ed.). (The riMLF and the interstitial nucleus
    of Cajal as vertical gaze centers — premotor structures
    DOWNSTREAM of the superior colliculus.)
*   **Pretectum (contrast — separate region, rostral):** Gamlin,
    P.D.R. (2002). "The pupillary light reflex and its brainstem
    pathways." In *Neuro-Ophthalmology* (Miller et al., eds.). (The
    pretectum — pupillary and optokinetic — a SEPARATE REGION
    rostral to the superior colliculus.)
*   **Thalamic relays (contrast — diencephalon):** Casagrande,
    V.A., Xu, X. (2004). "The lateral geniculate nucleus." In
    *The Visual Neurosciences* (Chalupa & Werner, eds.); and
    Winer, J.A., Schreiner, C.E. (eds.) (2005). *The Inferior
    Colliculus: A Window to the Brain*. (The LGN as the visual
    relay to V1; the MGN as the auditory relay to A1 — the thalamic
    relays that the colliculi project to (MGN) or do not project to
    (LGN).)
*   **SLEA (contrast — the tectum is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the tectum.)
*   NeuroNames — Tectum; Superior colliculus; Inferior colliculus;
    FMA — Tectum; Superior colliculus; Inferior colliculus.
"""