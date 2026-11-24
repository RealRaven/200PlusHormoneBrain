"""
infrastructure.brainparts.midbrain.cranial_nerve_nuclei
=======================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── tectum
    ├── tegmentum
    │   ├── oculomotor_nucleus            (CN III — topographic home)
    │   ├── trochlear_nucleus             (CN IV  — topographic home)
    │   ├── mesencephalic_trigeminal_nucleus  (CN Vm — topographic home)
    │   └── edinger_westphal_nucleus      (CN IIIp — topographic home)
    ├── cerebral_aqueduct
    ├── cerebral_peduncle
    └── cranial_nerve_nuclei              <-- THIS MODULE (functional
                                              cross-listing container)

**Primary synonym:** Midbrain cranial nerve nuclei; mesencephalic
cranial nerve nuclei; the mesencephalic CN nuclear column; CN III / CN
IV / CN Vm nuclear group.
**Container status:** **This module is a FUNCTIONAL GROUPING
CONTAINER, not a topographic parent.** It **cross-lists** four leaf
nuclei that are wired **topographically** under ``.../tegmentum/`` —
it does **not** duplicate their structural homes. Consumers may
resolve each leaf by **either** path (see *Cross-Listing Statement*
below). Consumers must **not** treat this container as a
**sub-topographic parent** — the CN nuclei are **in the tegmentum**;
this container re-frames them **by cranial-nerve function**, the way
a clinician frames them.
**Developmental designation:** **Mesencephalic** — the CN nuclei
cross-listed here are the **cranial-nerve nuclei whose cell bodies
lie within the midbrain (mesencephalon)**. This container holds **only
the midbrain CN nuclei** — it does **not** hold pontine or medullary
CN nuclei.
**Structural parent:** ``.../midbrain/`` → **direct child** of the
midbrain container, as a **functional grouping** peer to
``tectum/``, ``tegmentum/``, ``cerebral_aqueduct/``, and
``cerebral_peduncle/``.
**Structural children (expected — the tree is authoritative; each is
a CROSS-LISTED leaf whose topographic home is ``.../tegmentum/``):**
*   ``oculomotor_nucleus/`` — **CN III** — **somatic motor**;
    innervates the **superior rectus**, **inferior rectus**,
    **medial rectus**, **inferior oblique**, and **levator
    palpebrae superioris**; paired (left/right).
    Topographic home: ``.../tegmentum/oculomotor_nucleus/``.
*   ``trochlear_nucleus/`` — **CN IV** — **somatic motor**;
    innervates the **superior oblique**; paired (left/right);
    **the only CN that exits dorsally** and **the only CN whose
    fibers decussate before exiting** (left trochlear nucleus →
    right superior oblique).
    Topographic home: ``.../tegmentum/trochlear_nucleus/``.
*   ``mesencephalic_trigeminal_nucleus/`` — **CN V mesencephalic
    (CN Vm)** — **sensory** (proprioceptive); the **only primary
    sensory nucleus in the CNS** whose **cell bodies lie within the
    CNS** (all other primary sensory neurons have cell bodies in
    peripheral ganglia); paired (left/right).
    Topographic home: ``.../tegmentum/mesencephalic_trigeminal_nucleus/``.
*   ``edinger_westphal_nucleus/`` — **CN III parasympathetic
    (CN IIIp)** — **preganglionic parasympathetic**; projects to the
    **ciliary ganglion** → **sphincter pupillae** and **ciliary
    muscle**; the **efferent limb of the pupillary light reflex** and
    of the **near triad**; paired (left/right).
    Topographic home: ``.../tegmentum/edinger_westphal_nucleus/``.

**Boundary status (FUNCTIONAL CONTAINER — NOT a topographic
parent):** **Boundary case — the cranial_nerve_nuclei is a
FUNCTIONAL GROUPING CONTAINER, NOT a topographic parent.** The four
leaves it holds are **topographically in the tegmentum** — their
**structural (topographic) home** is ``.../tegmentum/``. This
container **cross-lists** them **by cranial-nerve identity** via the
``AREA_PATHS`` mechanism. Consumers must **not** treat this container
as a **second structural parent** in the topographic sense — it is a
**re-framing parent**, and the two paths (**tegmentum** and
**cranial_nerve_nuclei**) are **equivalent** for the leaf content
they point at. See *Cross-Listing Statement*.
**Boundary status (NOT the tegmentum — the tegmentum is the
TOPOGRAPHIC parent):** **Boundary case — the cranial_nerve_nuclei is
NOT the tegmentum.** The **tegmentum**
(``.../midbrain/tegmentum/``) is the **topographic container** — it
holds the CN nuclei **plus** the substantia nigra, the ventral
tegmental area, the red nucleus, the periaqueductal gray, and the
midbrain reticular formation. This container (**here**) is a
**functional grouping** that holds **only** the four CN nuclei,
**cross-listed** from the tegmentum. **They are DIFFERENT KINDS of
container** — the **tegmentum** is a **topographic** container; the
**cranial_nerve_nuclei** is a **functional** container. Consumers
must **not** conflate the two, and must **not** assume the CN nuclei
are **structurally children of this container only** — they are
**also** children of the tegmentum.
**Boundary status (CN NUCLEI — NOT the CN NERVES):** **Boundary case
— the cranial_nerve_nuclei are the **NUCLEI (grey matter, CNS)**,
NOT the **NERVES (peripheral)**.** The **nuclei** cross-listed here
are **CNS grey-matter structures** — they contain **motoneuron cell
bodies** (CN III, CN IV) or **sensory neuron cell bodies** (CN Vm)
or **preganglionic parasympathetic cell bodies** (Edinger-Westphal).
The **nerves** themselves — the **peripheral axon bundles** of
CN III, CN IV, and CN V — are **NOT midbrain structures**; they are
**peripheral nervous system** structures **wired elsewhere**. The
**CN III fascicles traverse the cerebral peduncle** (see
``.../cerebral_peduncle/``), but the **nerve** is not the **nucleus**
and is not **here**. Consumers must **not** conflate the CN **nuclei**
with the CN **nerves**.
**Boundary status (MIDBRAIN CN NUCLEI — NOT the pontine or medullary
CN nuclei):** **Boundary case — the cranial_nerve_nuclei holds **ONLY
the midbrain CN nuclei**.** The **pontine CN nuclei** — the **main
sensory and motor trigeminal nuclei** (CN V), the **abducens
nucleus** (CN VI), the **facial nucleus** (CN VII), the **superior
salivatory nucleus** (CN VIIp), the **vestibular nuclei** (CN VIII),
and the **cochlear nuclei** (CN VIII) — are **pons** structures
(``.../hindbrain/metencephalon/pons/``). The **medullary CN nuclei** —
the **nucleus ambiguus** (CN IX/X/XI), the **solitary nucleus** (CN
VII/IX/X), the **spinal trigeminal nucleus** (CN V), the **hypoglossal
nucleus** (CN XII), the **inferior salivatory nucleus** (CN IXp), and
the **dorsal motor nucleus of the vagus** (CN Xp) — are **medulla**
structures (``.../hindbrain/myencephalon/medulla_oblongata/``).
**This container holds ONLY the mesencephalic subset.** Consumers
must **not** assume this container holds **all** CN nuclei, and must
**not** resolve a pontine or medullary CN nucleus through the midbrain
path.
**Boundary status (NOT the MLF — the MLF is the INTERNUCLEAR
PATHWAY):** **Boundary case — the cranial_nerve_nuclei does NOT
include the medial longitudinal fasciculus (MLF).** The **MLF** is
a **longitudinal fiber pathway** — a **white-matter tract** — that
**coordinates** the CN III, CN IV, and CN VI nuclei for **conjugate
gaze**. The **MLF** is a **conduction pathway**, **not a nucleus**.
It is **wired elsewhere** (as a brainstem longitudinal tract, not as
a midbrain CN nucleus). Consumers must **not** conflate the CN
**nuclei** with the **MLF**, and must **not** resolve the MLF through
the cranial_nerve_nuclei path. **A lesion of the MLF produces
internuclear ophthalmoplegia (INO), which is NOT a CN III or CN IV
nuclear palsy** — this is a **clinical** distinction, not just an
anatomical one. See *Associated Disorders*.
**Boundary status (NOT the pretectal nuclei — the pretectal nuclei
are DIENCEPHALON):** **Boundary case — the cranial_nerve_nuclei does
NOT include the pretectal nuclei.** The **pretectal nuclei** — the
**olivary pretectal nucleus** and the **nucleus of the optic tract**
— are **diencephalon** structures (``.../forebrain/diencephalon/``),
at the **diencephalon–midbrain junction**. They are the **afferent
relay** of the **pupillary light reflex** — they receive retinal
input and **project to** the Edinger-Westphal nucleus. **They are
NOT midbrain structures**, and they are **NOT CN nuclei**. Consumers
must **not** conflate the pretectal nuclei with the
Edinger-Westphal nucleus, and must **not** resolve the pretectal
nuclei through the midbrain path. **The pupillary light reflex
spans diencephalon → midbrain** — the pretectal nuclei (diencephalon)
project to Edinger-Westphal (midbrain), which projects to the ciliary
ganglion (peripheral).
**Boundary status (NOT the superior colliculus or the lateral
geniculate body — those are VISUAL structures, not CN nuclei):**
**Boundary case — the cranial_nerve_nuclei does NOT include the
superior colliculus (tectum) or the lateral geniculate body
(diencephalon/thalamus).** The **superior colliculus** is a **tectum**
structure (``.../tectum/superior_colliculus/``) — it is the
**visual/oculomotor orienting** structure, and it **projects to** the
CN III/IV nuclei via the **tectobulbar tract** to drive **saccades**
and **visual grasp reflexes**. The **lateral geniculate body** is a
**diencephalon/thalamus** structure
(``.../forebrain/diencephalon/thalamus/.../lateral_geniculate_body/``)
— it is the **visual relay** to the cortex. **Neither is a CN
nucleus.** Consumers must **not** conflate the CN nuclei with the
superior colliculus or the lateral geniculate body, even though the
superior colliculus **drives** the CN nuclei.
**Boundary status (NOT the riMLF or the interstitial nucleus of
Cajal — those are GAZE CENTERS, not CN nuclei):** **Boundary case —
the cranial_nerve_nuclei does NOT include the rostral interstitial
nucleus of the MLF (riMLF) or the interstitial nucleus of Cajal.**
The **riMLF** and the **interstitial nucleus of Cajal** are
**vertical gaze** centers in the **rostral midbrain tegmentum** —
they are **premotor saccade generators**, not **CN nuclei**. They
are **tegmentum** structures (``.../tegmentum/``) but are **not**
cross-listed here. Consumers must **not** conflate the CN nuclei
with the gaze centers, and must **not** resolve the riMLF or
interstitial nucleus of Cajal through the cranial_nerve_nuclei path.
**Boundary status (PAIRED NUCLEI — each leaf here is a PAIRED
structure, wired as ``left/`` and ``right/``):** **Boundary case —
each cross-listed CN nucleus is a PAIRED structure.** The **left**
and **right** versions of the oculomotor nucleus, the trochlear
nucleus, the mesencephalic trigeminal nucleus, and the
Edinger-Westphal nucleus are **separate leaves** (side containers
holding one leaf each). Consumers must **not** resolve a single
midline "oculomotor nucleus" — the left and right are **distinct
leaves** with **distinct clinical laterality** (a left CN III nuclear
lesion produces a **left** CN III palsy; a left MLF lesion produces a
**left** internuclear ophthalmoplegia — different syndromes).
**Boundary status (STRUCTURE-CLASS TAXONOMY — motor nuclei,
sensory nuclei, and parasympathetic nuclei carry NO coupling
warning):** **Boundary case — the cranial_nerve_nuclei are
**motor nuclei (CN III, CN IV)**, a **sensory nucleus (CN Vm)**, and
a **preganglionic parasympathetic nucleus (Edinger-Westphal)** — and
**none carries a coupling warning**.** In the family's taxonomy,
**coupling warnings attach to oscillators only** — not to premotor
pools, not to sensor nuclei, not to conduction pathways, and **not to
motor nuclei**. The CN III and CN IV nuclei **fire in response to
upstream drive** (from the frontal eye fields via the PPRF, from the
superior colliculus via the tectobulbar tract, from the vestibular
nuclei, and from the riMLF) — they do **not** generate a rhythm
intrinsically. Their **coordination with the contralateral side** is
via **descending pathways** (the **MLF**, the **posterior
commissure**) — **not** via intrinsic nucleus-to-nucleus coupling.
**Motor nuclei carry NO coupling warning** — this is a **new
structure class** in the family, and it is the **same rule** that
applies to premotor pools: **coordination is downstream, not
intrinsic**.
**Boundary status (CHEMICALS-LAYER DISCIPLINE — the cholinergic
phenotype of Edinger-Westphal is a chemicals-layer fact):**
**Boundary case — the Edinger-Westphal nucleus is
**cholinergic**, and the **cholinergic phenotype** is a
``chemicals_hormones``-layer fact.** Edinger-Westphal is the
**preganglionic parasympathetic** nucleus — its neurons **synthesize
acetylcholine** (via **choline acetyltransferase, ChAT**) and
**release ACh** onto the **ciliary ganglion** (which is
**nicotinic**), and the **postganglionic** fibers **release ACh** onto
the **sphincter pupillae** (which is **muscarinic**). The
**cholinergic phenotype** — ChAT, ACh synthesis, nicotinic and
muscarinic receptors — is a **``chemicals_hormones``-layer fact**, not
a midbrain structural fact. Consumers must **not** import the
cholinergic phenotype into the cranial_nerve_nuclei container; the
**structural** module documents the **anatomy**, and **references**
the chemicals layer as prose. *(This is the same discipline the
midbrain container imposes on the dopaminergic phenotype of the
substantia nigra and the ventral tegmental area — see the midbrain
container's Design Contract.)*

Overview
--------
The midbrain cranial nerve nuclei are the **four CN nuclei whose cell
bodies lie within the mesencephalon** — the **oculomotor nucleus**
(CN III), the **trochlear nucleus** (CN IV), the **mesencephalic
trigeminal nucleus** (CN V mesencephalic), and the
**Edinger-Westphal nucleus** (CN III parasympathetic). They are
**functionally distinct** — **somatic motor** (CN III, CN IV),
**sensory** (CN Vm), and **preganglionic parasympathetic**
(Edinger-Westphal) — but they share a **common topographic home in
the midbrain tegmentum** and a **common functional identity as
cranial-nerve nuclei**.

**This container is a FUNCTIONAL GROUPING, not a topographic
parent.** The four leaves are **topographically in
``.../tegmentum/``** — this container **cross-lists** them by
cranial-nerve function via the ``AREA_PATHS`` mechanism. Both paths
resolve to the same leaf. See *Cross-Listing Statement*.

**The cranial_nerve_nuclei are NUCLEI, NOT NERVES.** The **nuclei**
are CNS grey-matter structures; the **nerves** are peripheral axon
bundles. The **CN III fascicles** traverse the cerebral peduncle (a
conduction-pathway module), but the **nerve** is **not** the
**nucleus**.

**The cranial_nerve_nuclei are MOTOR NUCLEI, a SENSORY NUCLEUS, and
a PARASYMPATHETIC NUCLEUS — and NONE carries a coupling warning.**
Coupling warnings attach to **oscillators only**. Coordination with
the contralateral side is via **descending pathways** (MLF,
posterior commissure), not intrinsic nucleus-to-nucleus coupling.
**Motor nuclei carry no coupling warning** — this is a **new
structure class** in the family.

**The cranial_nerve_nuclei are PAIRED NUCLEI.** Each is wired as a
**left** and a **right** leaf (side-scoped container each holding one
leaf). The left and right are **distinct leaves** with **distinct
clinical laterality** — a **left** CN III nuclear lesion is a
**left** CN III palsy; a **left** MLF lesion is a **left** internuclear
ophthalmoplegia. They are **different syndromes**, not mirror-image
deficits.

Expected Structural Children (prose — the tree is authoritative)
----------------------------------------------------------------
This container is expected to hold **four cross-listed leaves** —
each also a ``.../tegmentum/`` leaf:

*   **``oculomotor_nucleus/``** — **CN III** — **somatic motor** —
    superior rectus, inferior rectus, medial rectus, inferior
    oblique, levator palpebrae superioris. **Paired** (left/right).
    Topographic home: ``.../tegmentum/oculomotor_nucleus/``.

*   **``trochlear_nucleus/``** — **CN IV** — **somatic motor** —
    superior oblique. **Paired** (left/right). The **only CN that
    exits dorsally**; the **only CN whose fibers decussate before
    exiting** (left trochlear nucleus → right superior oblique).
    Topographic home: ``.../tegmentum/trochlear_nucleus/``.

*   **``mesencephalic_trigeminal_nucleus/``** — **CN V mesencephalic**
    — **sensory** (proprioceptive from jaw muscles and periodontal
    mechanoreceptors); the **only primary sensory nucleus in the CNS**
    whose **cell bodies lie within the CNS**. **Paired** (left/right).
    Topographic home:
    ``.../tegmentum/mesencephalic_trigeminal_nucleus/``.

*   **``edinger_westphal_nucleus/``** — **CN III parasympathetic** —
    **preganglionic parasympathetic** — ciliary ganglion →
    sphincter pupillae and ciliary muscle; **efferent limb of the
    pupillary light reflex** and of the **near triad**. **Paired**
    (left/right). Topographic home:
    ``.../tegmentum/edinger_westphal_nucleus/``.

**These are the expected children — the on-disk tree is the
authoritative source.** The container imposes the **cross-listing**
and **aggregation rules** below; the leaves impose the leaf-level
contract (boundary stacks, function, disorders, lateralization,
references) documented in the existing leaf modules.

Cross-Listing Statement (the container's core structural innovation)
--------------------------------------------------------------------
Each leaf under this container is **CROSS-LISTED** with
``.../tegmentum/`` — the same leaf is reachable by **two** structural
paths:

*   **Topographic path** — ``midbrain.tegmentum.<cn_nucleus>``
*   **Functional path** — ``midbrain.cranial_nerve_nuclei.<cn_nucleus>``

**Both paths resolve to the SAME leaf.** The **topographic home** is
``.../tegmentum/`` — that is the leaf's **structural parent** in the
topographic sense. The **functional home** is ``.../cranial_nerve_nuclei/``
— that is the leaf's **functional grouping parent**. The two are
**equivalent** for the leaf content they point at.

**Mechanism:** cross-listing is implemented via the ``AREA_PATHS``
mechanism the family already supports. Consumers that enumerate
**``.../cranial_nerve_nuclei/``** will see the four CN nuclei;
consumers that enumerate **``.../tegmentum/``** will see the **same
four** CN nuclei **plus** the substantia nigra, the ventral tegmental
area, the red nucleus, the periaqueductal gray, the riMLF, the
interstitial nucleus of Cajal, and the midbrain reticular formation.
**Neither enumeration is exhaustive in the other's sense** — the
**tegmentum is larger**; the **cranial_nerve_nuclei is smaller**.

**The midbrain container's child list places the CN nuclei under
``tegmentum/``** (their topographic home) — this container **does
not contradict that placement**; it **adds** a functional grouping.
Consumers reading the midbrain container's docstring and this
container's docstring should find them **consistent** — both
describe the CN nuclei as **topographically in the tegmentum**, and
this container describes them **functionally grouped here**.

**A consumer that resolves the CN nuclei by EITHER path will be
structurally correct** — but a consumer that assumes ``tegmentum/``
and ``cranial_nerve_nuclei/`` contain **disjoint** leaf sets will be
**wrong** — the four CN nuclei are **shared**, and the **tegmentum
is the superset**.

Aggregation Rules (the container's contract on its children)
------------------------------------------------------------
The cranial_nerve_nuclei container **imposes the following rules**
on every leaf under it. These are **inherited** from the midbrain
container and **extended** for the CN-nuclei-specific framing:

*   **FUNCTIONAL, NOT TOPOGRAPHIC, GROUPING.** The container groups
    by **cranial-nerve identity**, not by **topographic location**.
    A leaf belongs here **if and only if** it is a **cranial-nerve
    nucleus** whose cell bodies lie in the **midbrain**. A structure
    that is **in the tegmentum but is NOT a CN nucleus** (substantia
    nigra, VTA, red nucleus, PAG, riMLF, interstitial nucleus of
    Cajal, midbrain reticular formation) **does NOT belong here**.
*   **CROSS-LISTING DISCIPLINE.** Every leaf here is **ALSO** a
    ``.../tegmentum/`` leaf. The leaf's **content** is identical
    under both paths. Consumers should **resolve by one path** — not
    by both — for a single lookup. Enumerating **both** paths will
    yield **duplicates** for the four CN nuclei.
*   **CN-NUCLEI-ONLY — NOT NERVES, NOT PATHWAYS, NOT GAZE CENTERS.**
    The container holds CN **nuclei** — not the **nerves** (peripheral
    structures), not the **MLF** (a conduction pathway), not the
    **pretectal nuclei** (diencephalon), not the **superior
    colliculus** (tectum), not the **lateral geniculate body**
    (diencephalon/thalamus), and not the **riMLF** or the
    **interstitial nucleus of Cajal** (gaze centers).
*   **PAIRED-LEAF DISCIPLINE.** Each CN nucleus is a **paired
    structure** wired as a **left** leaf and a **right** leaf (a
    side-scoped container each holding one leaf). There is **no**
    midline CN nucleus in the midbrain.
*   **NO COUPLING WARNING (motor nuclei).** The CN III and CN IV
    nuclei are **motor nuclei**; the CN Vm is a **sensory nucleus**;
    the Edinger-Westphal is a **preganglionic parasympathetic
    nucleus**. **None carries a coupling warning.** Coupling warnings
    attach to **oscillators only** — the CN nuclei are **not**
    oscillators, and their **coordination with the contralateral
    side** is via **descending pathways** (MLF, posterior
    commissure), **not** via intrinsic nucleus-to-nucleus coupling.
    **This establishes the "motor nucleus" structure class** in the
    family — **same rule as premotor pools and sensor nuclei: no
    coupling warning**.
*   **CHEMICALS-LAYER DISCIPLINE.** The **cholinergic phenotype** of
    Edinger-Westphal (ChAT, ACh synthesis, nicotinic and muscarinic
    receptors) is a **``chemicals_hormones``-layer fact** —
    documented as **prose** in the leaf, **never imported**.
    Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **SENSORY-vs-MOTOR-vs-PARASYMPATHETIC DISCIPLINE.** The container
    holds a **mixed functional set** — two **somatic motor**
    (CN III, CN IV), one **sensory** (CN Vm), one **preganglionic
    parasympathetic** (Edinger-Westphal). Consumers must **not**
    assume a uniform functional type; the four leaves classify
    themselves.
*   **LATERALIZATION-WARNING DISCIPLINE.** The CN nuclei are
    **strict-mirror pairs with NO coupling warning** — same rule as
    the medullary premotor pools and the cerebral peduncle conduction
    pathways. The **left and right CN nuclei** are **functionally
    independent** at the **nucleus** level; their **coordination** is
    via **descending pathways** (MLF, posterior commissure), not
    intrinsic coupling.

Design Contract
---------------
*   **No side effects on import.** Pure namespace. The container
    ``__init__.py`` may be empty; re-exports are **optional** and
    **not** required.
*   **No cross-lobe imports.** This container does **not** import
    from ``../forebrain/`` or ``../hindbrain/``. The CN nuclei's
    relationships to the **pretectal nuclei** (diencephalon), the
    **superior colliculus** (tectum), the **lateral geniculate body**
    (diencephalon/thalamus), the **MLF** (conduction pathway), the
    **riMLF** and the **interstitial nucleus of Cajal** (gaze
    centers), the **pontine CN nuclei** (CN V main, VI, VII, VIII),
    the **medullary CN nuclei** (CN IX, X, XI, XII), the **ciliary
    ganglion** (peripheral), and the **CN nerves** (peripheral) are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **cholinergic
    phenotype** of Edinger-Westphal is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the leaf, **never imported**.
*   **FUNCTIONAL GROUPING CONTAINER — NOT a topographic parent.**
    The container cross-lists four leaves whose **topographic home**
    is ``.../tegmentum/``. The two paths are **equivalent** for the
    leaf content they point at. Consumers must **not** treat this
    container as a **second structural parent** in the topographic
    sense.
*   **CROSS-LISTING via ``AREA_PATHS``.** The four CN nuclei are
    cross-listed between ``.../tegmentum/`` and
    ``.../cranial_nerve_nuclei/``. The **tegmentum is the superset**;
    this container is a **functional subset** (four of the tegmentum's
    many leaves).
*   **CONSISTENT with the midbrain container's child list.** The
    midbrain container places the CN nuclei under ``tegmentum/``
    (their topographic home). This container **does not contradict
    that placement** — it **adds** a functional grouping. Consumers
    reading both docstrings should find them **consistent**.
*   **CN NUCLEI — NOT CN NERVES, NOT PATHWAYS, NOT GAZE CENTERS.**
    The **nerves** are peripheral; the **MLF** is a conduction
    pathway; the **riMLF** and the **interstitial nucleus of Cajal**
    are gaze centers; the **pretectal nuclei** are diencephalon; the
    **superior colliculus** is tectum; the **lateral geniculate
    body** is diencephalon/thalamus. None is in this container.
*   **PAIRED LEAVES — each is a left leaf and a right leaf.** The
    left and right are **distinct leaves** with **distinct clinical
    laterality**. There is **no** midline CN nucleus.
*   **MOTOR NUCLEI CARRY NO COUPLING WARNING.** The CN III and CN IV
    nuclei are motor nuclei; the CN Vm is a sensory nucleus; the
    Edinger-Westphal is a preganglionic parasympathetic nucleus.
    **None carries a coupling warning** — same rule as premotor
    pools and sensor nuclei. This establishes the **motor nucleus**
    structure class in the family.
*   **CHEMICALS-LAYER DISCIPLINE.** The **cholinergic phenotype** of
    Edinger-Westphal is a ``chemicals_hormones``-layer fact —
    documented as **prose**, **never imported**.
*   **SENSORY-vs-MOTOR-vs-PARASYMPATHETIC DISCIPLINE.** The container
    holds a **mixed functional set** — consumers must **not** assume
    a uniform type.
*   **"Brainstem" is federated, not structural.** Consistent with
    the midbrain container — there is **no** ``brainparts/brainstem/``
    container.
*   **The on-disk tree is authoritative.** The expected children
    listed above are **the standard midbrain CN nuclei**; the actual
    children are **whatever exists on disk**. The container **must
    not** invent children that are not present, and **must not**
    silently drop children that are present.
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum`` ↔
    ``cranial_nerve_nuclei``) — not into the forebrain, hindbrain, or
    periphery.
*   **No nested cross-listing.** The four CN nuclei are single-level
    cross-listed leaves. They are not themselves containers.

Usage
-----
Resolve the container by path::

    from infrastructure.brainparts.midbrain import cranial_nerve_nuclei

Resolve a cross-listed leaf by **either** path (they are
equivalent)::

    # Functional path (clinician framing):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei import oculomotor_nucleus

    # Topographic path (anatomist framing):
    from infrastructure.brainparts.midbrain.tegmentum import oculomotor_nucleus

Or by fully-qualified path string (leaves, not the container)::

    oculomotor_functional_path = (
        "midbrain.cranial_nerve_nuclei.oculomotor_nucleus"
    )
    oculomotor_topographic_path = (
        "midbrain.tegmentum.oculomotor_nucleus"
    )
    # Both resolve to the same leaf.

**Do not** assume the cranial_nerve_nuclei is a **topographic
parent**. The four CN nuclei are **topographically in
``.../tegmentum/``** — this container **cross-lists** them by
cranial-nerve function.

**Do not** assume the cranial_nerve_nuclei and the tegmentum contain
**disjoint** leaf sets. The four CN nuclei are **shared**, and the
**tegmentum is the superset** — it also holds the substantia nigra,
the ventral tegmental area, the red nucleus, the periaqueductal gray,
the riMLF, the interstitial nucleus of Cajal, and the midbrain
reticular formation.

**Do not** assume the cranial_nerve_nuclei contains **all** CN
nuclei. It contains **only the midbrain CN nuclei** — the **pontine**
CN nuclei (CN V main, VI, VII, VIII) and the **medullary** CN nuclei
(CN IX, X, XI, XII) are **elsewhere**.

**Do not** conflate the CN **nuclei** with the CN **nerves**. The
**nerves** are peripheral; the **nuclei** are here. The **CN III
fascicles traverse the cerebral peduncle**, but the **nerve** is not
the **nucleus**.

**Do not** conflate the CN **nuclei** with the **MLF**. The **MLF**
is a **conduction pathway** — a **longitudinal fiber tract** — not
a CN nucleus. **An MLF lesion produces internuclear ophthalmoplegia
(INO), NOT a CN III or CN IV nuclear palsy.** These are **different
syndromes**.

**Do not** conflate the CN **nuclei** with the **pretectal nuclei**.
The **pretectal nuclei** are **diencephalon** — the **afferent
relay** of the **pupillary light reflex** — and they **project to**
the **Edinger-Westphal nucleus** (midbrain). The two are **different
structures** across a lobe boundary.

**Do not** conflate the CN **nuclei** with the **superior colliculus**
(tectum) or the **lateral geniculate body** (diencephalon/thalamus).
The **superior colliculus** **drives** the CN nuclei for saccades;
it is **not** a CN nucleus.

**Do not** conflate the CN **nuclei** with the **riMLF** or the
**interstitial nucleus of Cajal**. Those are **premotor saccade
generators** — **gaze centers** — not CN nuclei.

**Do not** import the **cholinergic phenotype** of Edinger-Westphal
into the midbrain structural layer. The **cholinergic phenotype** is
a **``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the CN nuclei. **Motor
nuclei, sensory nuclei, and preganglionic parasympathetic nuclei
carry NO coupling warning** — same rule as premotor pools and sensor
nuclei. Coordination with the contralateral side is via **descending
pathways** (MLF, posterior commissure), **not** intrinsic
nucleus-to-nucleus coupling.

Iterating the cranial_nerve_nuclei's children (recommended consumer
pattern — NOTE cross-listing)::

    import pkgutil
    import infrastructure.brainparts.midbrain.cranial_nerve_nuclei as cnn_pkg

    CRANIAL_NERVE_NUCLEI_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(cnn_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("oculomotor_nucleus", "trochlear_nucleus",
    #            "mesencephalic_trigeminal_nucleus",
    #            "edinger_westphal_nucleus")
    #
    # Each of these is ALSO a .../tegmentum/ child. Enumerating
    # .../tegmentum/ will yield these four PLUS substantia_nigra,
    # ventral_tegmental_area, red_nucleus, periaqueductal_gray,
    # riMLF, interstitial_nucleus_of_cajal, and
    # midbrain_reticular_formation.
    #
    # Do NOT assume the two enumerations are disjoint — they are
    # NOT. The tegmentum is the SUPERSET.

Reaching the topographic home (recommended consumer pattern — the
tegmentum is the structural parent)::

    # The tegmentum is the TOPOGRAPHIC parent of the CN nuclei —
    # it also holds substantia nigra, VTA, red nucleus, PAG,
    # riMLF, interstitial nucleus of Cajal, and midbrain reticular
    # formation:
    #
    #   brainparts.midbrain.tegmentum
    #
    # The cranial_nerve_nuclei is a FUNCTIONAL subset — the four
    # CN nuclei cross-listed from the tegmentum.

Reaching the CN nerves (recommended consumer pattern — NOTE the
nerves are PERIPHERAL)::

    # The CN nerves (III, IV, V) are PERIPHERAL axon bundles —
    # NOT midbrain structures. They are wired elsewhere.
    #
    #   peripheral.cranial_nerves.oculomotor
    #   peripheral.cranial_nerves.trochlear
    #   peripheral.cranial_nerves.trigeminal
    #
    # The CN NUCLEI are here; the CN NERVES are NOT.

Reaching the MLF (recommended consumer pattern — NOTE the MLF is a
CONDUCTION PATHWAY, NOT a CN nucleus)::

    # The medial longitudinal fasciculus (MLF) is a CONDUCTION
    # PATHWAY — a longitudinal fiber tract — that COORDINATES the
    # CN III, IV, and VI nuclei for conjugate gaze:
    #
    #   brainparts.hindbrain.myelencephalon.medulla_oblongata...
    #   medial_longitudinal_fasciculus
    #
    # The MLF is a FIBER TRACT; the CN nuclei are GREY-MATTER
    # NUCLEI. An MLF lesion produces INTERNUCLEAR
    # OPHTHALMOPLEGIA (INO), NOT a CN III or CN IV nuclear palsy.

Reaching the pretectal nuclei (recommended consumer pattern — NOTE
the pretectal nuclei are DIENCEPHALON)::

    # The pretectal nuclei — the olivary pretectal nucleus and the
    # nucleus of the optic tract — are DIENCEPHALON structures at
    # the diencephalon-midbrain junction. They are the AFFERENT
    # relay of the pupillary light reflex, and they PROJECT TO the
    # Edinger-Westphal nucleus:
    #
    #   brainparts.forebrain.diencephalon.pretectal_nuclei
    #
    # The pretectal nuclei are DIENCEPHALON; the Edinger-Westphal
    # nucleus is MIDBRAIN. The pupillary light reflex SPANS
    # diencephalon -> midbrain -> peripheral.

Reaching the superior colliculus (recommended consumer pattern —
NOTE the superior colliculus DRIVES the CN nuclei but is NOT a CN
nucleus)::

    # The superior colliculus is a TECTUM structure — the
    # visual/oculomotor orienting structure. It PROJECTS TO the
    # CN III/IV nuclei via the tectobulbar tract to drive saccades
    # and visual grasp reflexes:
    #
    #   brainparts.midbrain.tectum.superior_colliculus
    #
    # The superior colliculus DRIVES the CN nuclei; it is NOT a
    # CN nucleus.

Reaching the riMLF and the interstitial nucleus of Cajal
(recommended consumer pattern — NOTE they are GAZE CENTERS, NOT CN
nuclei)::

    # The rostral interstitial nucleus of the MLF (riMLF) and the
    # interstitial nucleus of Cajal are VERTICAL GAZE CENTERS in
    # the rostral midbrain tegmentum — PREMOTOR SACCADE
    # GENERATORS, NOT CN nuclei:
    #
    #   brainparts.midbrain.tegmentum.riMLF
    #   brainparts.midbrain.tegmentum.interstitial_nucleus_of_cajal
    #
    # The gaze centers are TEgmentum leaves but are NOT
    # cross-listed under cranial_nerve_nuclei.

Reaching the pontine CN nuclei (recommended consumer pattern — NOTE
they are HINDBRAIN, NOT midbrain)::

    # The pontine CN nuclei — CN V main sensory and motor, CN VI,
    # CN VII, CN VIIp (superior salivatory), CN VIII vestibular
    # and cochlear — are PONS structures:
    #
    #   brainparts.hindbrain.metencephalon.pons.cranial_nerve_nuclei
    #
    # The midbrain cranial_nerve_nuclei holds ONLY the mesencephalic
    # subset — CN III, CN IV, CN Vm, and Edinger-Westphal.

Reaching the medullary CN nuclei (recommended consumer pattern —
NOTE they are HINDBRAIN, NOT midbrain)::

    # The medullary CN nuclei — CN IX, CN X, CN XI, CN XII, CN VII
    # (nucleus ambiguus component), CN IXp (inferior salivatory),
    # CN Xp (dorsal motor nucleus of the vagus), the solitary
    # nucleus, and the spinal trigeminal nucleus — are MEDULLA
    # structures:
    #
    #   brainparts.hindbrain.myelencephalon.medulla_oblongata.
    #   cranial_nerve_nuclei
    #
    # The midbrain cranial_nerve_nuclei holds ONLY the mesencephalic
    # subset.

Bilateral iteration (recommended consumer pattern — NOTE the
no-coupling-warning rule)::

    for side in ("left", "right"):
        for nucleus in (
            "oculomotor_nucleus",
            "trochlear_nucleus",
            "mesencephalic_trigeminal_nucleus",
            "edinger_westphal_nucleus",
        ):
            path = (
                f"midbrain.cranial_nerve_nuclei.{nucleus}.{side}"
            )
            # resolve path through the memory/recall layer
            #
            # NOTE: the CN nuclei are MOTOR NUCLEI (CN III, CN IV),
            # a SENSORY NUCLEUS (CN Vm), and a PREGANGLIONIC
            # PARASYMPATHETIC NUCLEUS (Edinger-Westphal). NONE
            # carries a coupling warning. Coordination with the
            # contralateral side is via descending pathways (MLF,
            # posterior commissure), not intrinsic
            # nucleus-to-nucleus coupling.

CN-nuclei-level detail (not wired — consult references)::

    # The midbrain CN nuclei are four functionally distinct
    # nuclei:
    #   oculomotor_nucleus (CN III)  -> somatic motor;
    #                                    superior rectus, inferior
    #                                    rectus, medial rectus,
    #                                    inferior oblique, levator
    #                                    palpebrae superioris
    #   trochlear_nucleus (CN IV)    -> somatic motor; superior
    #                                    oblique; only CN that
    #                                    exits dorsally; only CN
    #                                    whose fibers decussate
    #   mesencephalic_trigeminal_nucleus (CN Vm) -> sensory
    #                                    (proprioceptive); only
    #                                    primary sensory nucleus
    #                                    in the CNS
    #   edinger_westphal_nucleus (CN IIIp) -> preganglionic
    #                                    parasympathetic; ciliary
    #                                    ganglion; sphincter
    #                                    pupillae; ciliary muscle
    #
    # Do not attempt to resolve these as sub-paths of the
    # cranial_nerve_nuclei container beyond their named children.

References
----------
*   **Canonical midbrain CN nuclei anatomy:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (The midbrain CN nuclei — oculomotor, trochlear, mesencephalic
    trigeminal, Edinger-Westphal; their topographic locations in
    the tegmentum and their functional identities.)
*   **Oculomotor nucleus and CN III:** Büttner-Ennever, J.A. (2006).
    *Neuroanatomy of the Oculomotor System*. (The oculomotor nucleus
    — somatic motor subnuclei for the extraocular muscles and the
    levator palpebrae superioris; the Edinger-Westphal nucleus as
    the preganglionic parasympathetic subnucleus.)
*   **Trochlear nucleus and CN IV:** Büttner-Ennever, J.A., Horn,
    A.K.E. (2014). "Oculomotor system." In *The Human Nervous
    System* (Paxinos, ed.). (The trochlear nucleus — the only CN
    that exits dorsally and decussates before exiting; the left
    trochlear nucleus innervates the right superior oblique.)
*   **Mesencephalic trigeminal nucleus:** Lazarov, N.E. (2007). "The
    mesencephalic trigeminal nucleus in the mouse." *Annals of
    Anatomy* 189:349–360. (The mesencephalic trigeminal nucleus as
    the only primary sensory nucleus in the CNS; its role in jaw
    proprioception.)
*   **Edinger-Westphal nucleus and the pupillary light reflex:**
    Gamlin, P.D.R. (2002). "The pupillary light reflex and its
    brainstem pathways." In *Neuro-Ophthalmology* (Miller et al.,
    eds.). (The Edinger-Westphal nucleus as the preganglionic
    parasympathetic source for the pupillary light reflex and the
    near triad; the pretectal relay.)
*   **Pupillary light reflex — modern review:** Wilhelm, H. (2011).
    "Disorders of the pupil." *Handbook of Clinical Neurology*
    102:427–466. (The pupillary light reflex pathway — retina →
    optic nerve → pretectal nucleus → Edinger-Westphal → ciliary
    ganglion → sphincter pupillae; the clinical syndromes.)
*   **MLF and internuclear ophthalmoplegia:** Frohman, T.C.,
    Galetta, S.L., Fox, R.J., Solomon, D., Straumann, D., Filippi,
    M., Zee, D.S., Frohman, E.M. (2008). "Pearls & Oy-sters: The
    medial longitudinal fasciculus in ocular motor physiology."
    *Neurology* 70:e57–e67. (The MLF as the internuclear pathway
    coordinating CN III, IV, VI for conjugate gaze; INO as the MLF
    lesion syndrome — distinct from CN III or IV nuclear palsy.)
*   **riMLF and vertical gaze:** Büttner-Ennever, J.A., Büttner, U.
    (1988). "The reticular formation." In *Neuroanatomy of the
    Oculomotor System* (Büttner-Ennever, ed.). (The riMLF and the
    interstitial nucleus of Cajal as vertical gaze centers —
    premotor saccade generators, not CN nuclei.)
*   **Superior colliculus and tectobulbar drive of CN nuclei:**
    Sparks, D.L. (2002). "The brainstem control of saccadic eye
    movements." *Nature Reviews Neuroscience* 3:952–964. (The
    superior colliculus projecting to the CN III/IV nuclei via
    the tectobulbar tract — the visual grasp reflex and saccade
    generation.)
*   **Pretectal nuclei (contrast — diencephalon):** Klooster, J.,
    Vrensen, G.F.J.M. (1997). "The pretectal complex of the
    rabbit: a cytoarchitectonic and hodological study."
    *Neuroscience* 76:1233–1254. (The pretectal nuclei as the
    diencephalon relay of the pupillary light reflex, projecting
    to Edinger-Westphal.)
*   **Lateral geniculate body (contrast — diencephalon/thalamus):**
    Casagrande, V.A., Xu, X. (2004). "The lateral geniculate
    nucleus." In *The Visual Neurosciences* (Chalupa & Werner,
    eds.). (The lateral geniculate body as the thalamic visual
    relay — NOT a CN nucleus.)
*   **Pontine CN nuclei (contrast — hindbrain/metencephalon):**
    Paxinos, G., Franklin, K.B.J. (2019). *Paxinos and Franklin's
    the Mouse Brain in Stereotaxic Coordinates*, 5th ed. (The
    pontine CN nuclei — CN V main sensory/motor, VI, VII, VIIp,
    VIII vestibular/cochlear — contrast with the midbrain CN
    nuclei.)
*   **Medullary CN nuclei (contrast — hindbrain/myelencephalon):**
    Blessing, W.W. (1997). *The Lower Brainstem and Bodily
    Homeostasis*. (The medullary CN nuclei — IX, X, XI, XII, IXp,
    Xp, solitary nucleus, spinal trigeminal nucleus — contrast with
    the midbrain CN nuclei.)
*   **Cholinergic phenotype (chemicals_hormones-layer fact —
    contrast):** Woolf, N.J. (1991). "Cholinergic systems in
    mammalian brain and spinal cord." *Progress in Neurobiology*
    37:475–524. (The cholinergic phenotype — ChAT, ACh synthesis,
    nicotinic and muscarinic receptors — as a chemicals-layer fact
    documented in the Edinger-Westphal leaf, never imported into
    the midbrain structural layer.)
*   **SLEA (contrast — the CN nuclei are not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    any midbrain CN nucleus.)
*   NeuroNames — Oculomotor nucleus; Trochlear nucleus;
    Mesencephalic trigeminal nucleus; Edinger-Westphal nucleus;
    FMA — corresponding entries.
"""