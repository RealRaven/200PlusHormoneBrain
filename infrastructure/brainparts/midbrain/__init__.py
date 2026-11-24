"""
infrastructure.brainparts.midbrain
==================================

Anatomical Hierarchy
--------------------
::

    brainparts
    ├── forebrain
    │   ├── diencephalon
    │   └── telencephalon
    ├── midbrain                    <-- THIS MODULE (container)
    │   ├── tectum
    │   ├── tegmentum
    │   ├── cerebral_aqueduct
    │   └── cerebral_peduncles
    └── hindbrain
        ├── metencephalon
        └── myelencephalon

**Primary synonym:** Midbrain; mesencephalon.
**Developmental designation:** **Mesencephalon** — one of the three
primary vesicles of the embryonic neural tube (prosencephalon,
mesencephalon, rhombencephalon). **Unlike the forebrain and the
hindbrain, the mesencephalon does NOT subdivide into secondary
vesicles** — the midbrain is **one developmental unit**, and it is
**the shortest of the three brain vesicles** in the adult.
**Container status:** **This module is a CONTAINER, not a leaf.**
It holds the midbrain subpackages and imposes aggregation rules on
them. It has **no anatomical function of its own** — every functional
claim belongs to a **child** (the **tectum**, the **tegmentum**, the
**cerebral aqueduct**, the **cerebral peduncles**). Consumers must
**not** resolve a midbrain function by resolving this module — they
must resolve the **child** that carries it.
**Structural parent:** ``infrastructure/brainparts/`` →
**direct child** of the `brainparts` container, **sibling** of
`forebrain/` and `hindbrain/`.
**Structural children (expected — the tree is authoritative):**
*   ``tectum/`` — the **dorsal midbrain** ("roof"); contains the
    **superior colliculus** (visual/oculomotor) and the **inferior
    colliculus** (auditory), each **paired** (left, right).
*   ``tegmentum/`` — the **ventral midbrain** ("covering"); contains
    the **substantia nigra**, the **ventral tegmental area**, the
    **red nucleus**, the **periaqueductal gray**, the **oculomotor
    nucleus** (CN III), the **trochlear nucleus** (CN IV), the
    **Edinger-Westphal nucleus**, the **mesencephalic trigeminal
    nucleus** (CN V mesencephalic), and the **midbrain reticular
    formation**.
*   ``cerebral_aqueduct/`` — the **mesencephalic aqueduct** (aqueduct
    of Sylvius); the **CSF conduit** from the **third ventricle** to
    the **fourth ventricle**; **midline**, not paired.
*   ``cerebral_peduncles/`` — the **crus cerebri** and the
    **corticospinal / corticobulbar** fiber bundles; **paired**
    (left, right).
**Boundary status (NOT the forebrain — the forebrain is
PROSENCEPHALON):** **Boundary case — the midbrain is NOT the
forebrain.** The **forebrain** (``../forebrain/``) is the
**prosencephalon** — it contains the **diencephalon** (thalamus,
hypothalamus, epithalamus, subthalamus, pituitary, third ventricle)
and the **telencephalon** (cerebral hemispheres, cortex, basal
ganglia, amygdala, hippocampus, rhinencephalon, lateral ventricles).
The **midbrain** (here) is the **mesencephalon** — a **separate
developmental vesicle**. **They are DIFFERENT STRUCTURES** —
the **forebrain** is the **prosencephalon**; the **midbrain** is the
**mesencephalon**. Consumers must **not** conflate the midbrain with
the diencephalon (the **thalamus** and **hypothalamus** are
forebrain structures, **caudal to the midbrain's rostral border**),
and must **not** conflate the midbrain with the telencephalon.
**Boundary status (NOT the hindbrain — the hindbrain is
RHOMBENCEPHALON):** **Boundary case — the midbrain is NOT the
hindbrain.** The **hindbrain** (``../hindbrain/``) is the
**rhombencephalon** — it contains the **metencephalon** (pons,
cerebellum) and the **myelencephalon** (medulla oblongata). The
**midbrain** (here) is the **mesencephalon**. **They are DIFFERENT
STRUCTURES** — the **pons** and the **medulla oblongata** are
**rhombencephalic**; the **midbrain** is **mesencephalic**.
Consumers must **not** conflate the midbrain with the pons, the
cerebellum, or the medulla oblongata, and must **not** resolve the
midbrain as a child of the hindbrain.
**Boundary status (NOT the brainstem — the midbrain is only ONE of
three brainstem segments, and "brainstem" is a FEDERATED concept, not
a container):** **Boundary case — the midbrain is NOT the brainstem.**
The **brainstem** is a **federated anatomical concept** spanning
**three developmentally distinct segments**: the **midbrain**
(mesencephalon, **here**), the **pons** (metencephalon, under
`../hindbrain/`), and the **medulla oblongata** (myelencephalon,
under `../hindbrain/`). **The tree does NOT have a
``brainparts/brainstem/`` container** — brainstem is **not a
structural parent**; it is a **prose-and-boundary concept**.
Consumers must **not** assume a ``brainstem/`` directory exists, and
must **not** resolve the midbrain through a "brainstem" path — the
midbrain is a **direct child of `brainparts/`**.
**Boundary status (NOT the diencephalon — the diencephalon is
FOREBRAIN, despite its proximity):** **Boundary case — the midbrain
is NOT the diencephalon, and the diencephalon is NOT the midbrain,
even though they are anatomically adjacent.** The **diencephalon**
(``../forebrain/diencephalon/``) is the **caudal forebrain** — its
**thalamus** and **hypothalamus** sit **rostral to the midbrain**,
and the **cerebral aqueduct** of the midbrain continues rostrally as
the **third ventricle** of the diencephalon. **They are DIFFERENT
STRUCTURES across a lobe boundary** — the **diencephalon** is
**prosencephalic**; the **midbrain** is **mesencephalic**. The
**proximity is a topographic hazard, not a structural relationship.**
Consumers must **not** resolve the **thalamus** or **hypothalamus**
as midbrain children, and must **not** resolve the **tectum** or
**tegmentum** as diencephalon children.
**Boundary status (NOT the pons — the pons is METENCEPHALON):**
**Boundary case — the midbrain is NOT the pons.** The **pons**
(``../hindbrain/metencephalon/pons/``) is the **middle cerebellar
peduncle-bearing** rhombencephalic segment. The **midbrain** is
**rostral to the pons** — the **midbrain-pons junction** is the
**pontomesencephalic junction**. They are **DIFFERENT
STRUCTURES across a lobe boundary**. Consumers must **not** conflate
the midbrain with the pons, and must **not** resolve **substantia
nigra** or **red nucleus** as pontine structures.
**Boundary status (CONTAINER — the midbrain is a PACKAGE, not a
functional leaf):** **Boundary case — the midbrain is a CONTAINER.**
It has **no anatomical function of its own**; its children carry
the functions. Consumers must **not** attribute a midbrain-level
function to this module — resolve the **child** that carries the
function (**tectum** for visual/auditory orienting, **tegmentum**
for motor and dopaminergic/arousal functions, **cerebral aqueduct**
for CSF flow, **cerebral peduncles** for corticospinal/corticobulbar
descent).
**Boundary status (CONTAINER — the midbrain imposes
CHEMICALS-LAYER DISCIPLINE on its children):** **Boundary case —
the midbrain's dopaminergic children (**substantia nigra**,
**ventral tegmental area**) carry a **chemicals-layer hazard**
parallel to the C1 hazard in the medulla.** The **dopaminergic
phenotype** (tyrosine hydroxylase, dopamine synthesis, D1/D2
receptors) is a ``chemicals_hormones``-layer fact — **not** a
midbrain structural fact. Consumers of **substantia nigra** or
**ventral tegmental area** must **not** import the chemicals-layer
phenotype into the structural module; the structural module
documents the **anatomy**, and **references** the chemicals layer
as prose. *(This is the same rule the RTN and nucleus retrofacialis
modules apply to the C1 adrenergic group — see Design Contract.)*
**Boundary status (CONTAINER — the midbrain imposes
CRANIAL-NERVE DISCIPLINE on its children):** **Boundary case — the
midbrain houses **two cranial nerve nuclei (CN III oculomotor, CN
IV trochlear) and one mesencephalic trigeminal (CN V) nucleus**, but
**the cranial nerves themselves are NOT midbrain structures.** The
**nerves** (the peripheral bundles) are wired elsewhere (peripheral
nervous system), and the **nuclei** are wired under
``tegmentum/``. The **oculomotor nucleus** and **trochlear nucleus**
are **midbrain**; the **nerves** are **not**. Consumers must **not**
conflate the midbrain **nuclei** with the cranial **nerves**.

Overview
--------
The midbrain is the **mesencephalon** — the **shortest of the three
brain vesicles** in the adult, and the **middle segment of the
federated brainstem** (midbrain + pons + medulla). It is a
**container** under `brainparts/`, holding the **tectum** (dorsal,
colliculi), the **tegmentum** (ventral, sensorimotor nuclei), the
**cerebral aqueduct** (midline CSF conduit), and the **cerebral
peduncles** (paired descending fiber bundles).

**The midbrain is the mesencephalon, NOT the forebrain and NOT the
hindbrain.** It is **one of the three primary brain vesicles**, and
it **does NOT subdivide** into secondary vesicles. The **forebrain**
(prosencephalon) and the **hindbrain** (rhombencephalon) are its
**siblings**; the **pons** and **medulla oblongata** are
**rhombencephalic**, **not** mesencephalic.

**The midbrain is the CONTAINER, NOT a functional leaf.** Every
functional claim (visual orienting, auditory orienting, dopaminergic
modulation, motor relay, CSF flow) belongs to a **child**. Consumers
must resolve the **child**.

**The midbrain is a PAIRED-STRUCTURE container.** Most of its
functional children (**superior colliculus**, **inferior
colliculus**, **substantia nigra**, **ventral tegmental area**,
**red nucleus**, **oculomotor nucleus**, **trochlear nucleus**,
**Edinger-Westphal nucleus**, **mesencephalic trigeminal nucleus**,
**cerebral peduncles**) are **paired** (left/right). The
**cerebral aqueduct** and the **periaqueductal gray** are **midline
structures**, **not paired**. This mirrors the **diencephalon**
container (paired habenular nuclei, midline third ventricle) and
the **hindbrain** container (paired VRG subnuclei, midline structures
like the median eminence).

Expected Structural Children (prose — the tree is authoritative)
----------------------------------------------------------------
The midbrain container is expected to hold:

*   ``tectum/`` — the **dorsal midbrain**, containing the
    **superior colliculus** (visual/oculomotor; **paired**) and the
    **inferior colliculus** (auditory; **paired**).

*   ``tegmentum/`` — the **ventral midbrain**, containing the
    **substantia nigra** (dopaminergic; **paired**), the **ventral
    tegmental area** (dopaminergic; **paired**), the **red nucleus**
    (rubrospinal; **paired**), the **periaqueductal gray** (pain
    modulation / defensive behavior; **midline, surrounding the
    aqueduct**), the **oculomotor nucleus** (CN III; **paired**),
    the **trochlear nucleus** (CN IV; **paired**), the
    **Edinger-Westphal nucleus** (preganglionic parasympathetic;
    **paired**), the **mesencephalic trigeminal nucleus** (CN V
    mesencephalic; **the only primary sensory nucleus in the CNS**;
    **paired**), and the **midbrain reticular formation**
    (**paired**).

*   ``cerebral_aqueduct/`` — the **mesencephalic aqueduct** (aqueduct
    of Sylvius); the **CSF conduit** from the third ventricle to the
    fourth; **midline**.

*   ``cerebral_peduncles/`` — the **crus cerebri** and the
    **corticospinal / corticobulbar** fiber bundles; **paired**.

**These are the expected children — the on-disk tree is the
authoritative source.** The container imposes the aggregation rules
below; the children impose the leaf-level contract (boundary stacks,
function, disorders, lateralization, references) documented in the
existing leaf modules (e.g., ``ventral_respiratory_group/*``).

Aggregation Rules (the container's contract on its children)
------------------------------------------------------------
The midbrain container **imposes the following rules** on every leaf
under it. These are **inherited**, not restated in each leaf:

*   **Leaf-only functional claims.** A **function** claim is made in
    a **leaf** (e.g., ``tectum/superior_colliculus``), **never** in
    the container. The container itself is **not** a functional
    structure.
*   **Chemicals-layer discipline.** Dopaminergic (SN, VTA),
    cholinergic, and other **transmitter phenotypes** are
    **chemicals_hormones-layer facts** — documented as **prose** in
    the leaf, **never imported**. Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Cranial-nerve discipline.** **Cranial nerve nuclei** (CN III,
    CN IV, CN V mesencephalic) are midbrain **nuclei** (leaves under
    ``tegmentum/``); the **nerves** themselves are **not** midbrain
    structures and are **wired elsewhere**.
*   **Paired-vs-midline discipline.** Paired nuclei are wired as
    ``left/`` and ``right/`` leaf children; **midline structures**
    (aqueduct, periaqueductal gray) are wired as **single leaves**.
    This mirrors the **diencephalon** container.
*   **Lateralization-warning discipline.** The **structure-class
    taxonomy** established in the VRG modules applies here too:
    **oscillators** carry coupling warnings; **premotor pools**,
    **sensor/driver nuclei**, and **sensory nuclei** do **not**.
    A midbrain leaf that is a **sensory nucleus** (e.g., inferior
    colliculus as an auditory relay) or a **motor nucleus** (CN III,
    CN IV) is classified by its **function class** — the container
    does **not** pre-assign a warning.

Design Contract
---------------
*   **No side effects on import.** Pure namespace. The container
    ``__init__.py`` may be empty; re-exports are **optional** and
    **not** required.
*   **No cross-lobe imports.** The midbrain container does **not**
    import from ``../forebrain/`` or ``../hindbrain/``. The
    midbrain's relationship to the forebrain (diencephalon), the
    hindbrain (pons, medulla), and the "brainstem" concept is
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **dopaminergic
    phenotype** of the substantia nigra and the ventral tegmental
    area is a ``chemicals_hormones``-layer fact — documented as
    **prose**, never imported.
*   **Container, not leaf.** The midbrain is a **package**, not a
    functional structure. It has **no anatomical function of its
    own**; every functional claim belongs to a **child**.
*   **The on-disk tree is authoritative.** The expected children
    listed above are **the standard mesencephalon subdivisions**;
    the actual children are **whatever exists on disk**. The
    container **must not** invent children that are not present, and
    **must not** silently drop children that are present.
*   **The three-vesicle rule.** The midbrain is **mesencephalon** —
    a **primary vesicle that does not subdivide**. It is **not** a
    wrapper around a "mesencephalon" subpackage, and it is **not** a
    "brainstem" wrapper. It is **the mesencephalon**.
*   **Sibling parity with forebrain and hindbrain.** The midbrain
    is a **peer** of `../forebrain/` and `../hindbrain/` — **not**
    a child of either, and **not** a "brainstem" child of
    `brainparts/`.
*   **"Brainstem" is federated, not structural.** The tree has
    **no** ``brainparts/brainstem/`` container. The brainstem is a
    **prose-and-boundary concept** spanning midbrain + pons +
    medulla; consumers must **not** resolve a "brainstem" path.
*   **The thalamus and hypothalamus are NOT midbrain.** They are
    **diencephalon** children (`../forebrain/diencephalon/`). The
    **cerebral aqueduct** (midbrain) continues rostrally as the
    **third ventricle** (diencephalon) — **a topographic continuity,
    not a structural containment**.
*   **The pons and medulla are NOT midbrain.** They are **hindbrain**
    children (`../hindbrain/`). The **midbrain-pons junction** is
    **pontomesencephalic** — **a boundary, not a containment**.
*   **No ``AREA_PATHS`` hop.** The midbrain is a **local container**
    under `brainparts/`, not a cross-listed package.
*   **No nested cross-listing.** The midbrain has **no** dual-framing
    module. It is a single container.

Usage
-----
Resolve the container by path::

    from infrastructure.brainparts import midbrain

Resolve a midbrain child by path (the function belongs to the
child)::

    from infrastructure.brainparts.midbrain.tegmentum import substantia_nigra
    from infrastructure.brainparts.midbrain.tectum import superior_colliculus

Or by fully-qualified path string (children, not the container)::

    substantia_nigra_path = (
        "midbrain.tegmentum.substantia_nigra.left"
    )
    superior_colliculus_path = (
        "midbrain.tectum.superior_colliculus.left"
    )

**Do not** assume the midbrain is the **forebrain** or the
**hindbrain**. It is the **mesencephalon** — a **separate
developmental vesicle**.

**Do not** assume the midbrain is the **diencephalon**. The
**thalamus** and **hypothalamus** are **forebrain** structures; the
**midbrain-diencephalon junction** is **a boundary, not a
containment**. The **cerebral aqueduct** (midbrain) continues
rostrally as the **third ventricle** (diencephalon) — **a continuity
of CSF space, not a structural parent-child relationship**.

**Do not** assume the midbrain is the **pons** or the **medulla
oblongata**. Those are **hindbrain** structures. The **midbrain-pons
junction** is **pontomesencephalic**.

**Do not** assume a ``brainparts/brainstem/`` container exists.
**"Brainstem" is a federated concept**, not a structural parent.

**Do not** attribute a midbrain-level function to this container.
**Resolve the child** that carries the function — the **tectum**
(visual/auditory orienting), the **tegmentum** (motor, dopaminergic,
arousal), the **cerebral aqueduct** (CSF flow), the **cerebral
peduncles** (descending motor).

**Do not** import the **dopaminergic phenotype** of the substantia
nigra or the ventral tegmental area into the midbrain structural
layer. The **dopaminergic phenotype** is a ``chemicals_hormones``-
layer fact.

**Do not** conflate the midbrain **cranial-nerve nuclei** (CN III,
CN IV, CN V mesencephalic) with the **cranial nerves** themselves.
The **nuclei** are midbrain leaves; the **nerves** are **peripheral**
structures wired elsewhere.

Iterating the midbrain's children (recommended consumer pattern)::

    import pkgutil
    import infrastructure.brainparts.midbrain as midbrain_pkg

    MIDBRAIN_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(midbrain_pkg.__path__)
        if not m.name.startswith("_")
    )
    # The container does not pre-declare its children as
    # constants; the on-disk tree is authoritative. Use
    # pkgutil.iter_modules (or the memory/recall layer's
    # equivalent) to enumerate.

Reaching the forebrain (recommended consumer pattern — the ROSTRAL
sibling)::

    # The forebrain is the PROSENCEPHALON — the diencephalon
    # (thalamus, hypothalamus, epithalamus, subthalamus,
    # pituitary, third ventricle) and the telencephalon
    # (cerebral hemispheres, cortex, basal ganglia, amygdala,
    # hippocampus, rhinencephalon, lateral ventricles):
    #
    #   brainparts.forebrain
    #
    # The midbrain is the MESENCEPHALON — a separate vesicle.
    # The cerebral aqueduct (midbrain) continues rostrally as the
    # third ventricle (diencephalon) — a continuity of CSF space,
    # not a containment.

Reaching the hindbrain (recommended consumer pattern — the CAUDAL
sibling)::

    # The hindbrain is the RHOMBENCEPHALON — the metencephalon
    # (pons, cerebellum) and the myelencephalon (medulla
    # oblongata):
    #
    #   brainparts.hindbrain
    #
    # The midbrain is the MESENCEPHALON — a separate vesicle.
    # The midbrain-pons junction is pontomesencephalic.

Reaching the brainstem (recommended consumer pattern — NOTE the
federated concept)::

    # The brainstem is a FEDERATED CONCEPT spanning three
    # developmentally distinct segments:
    #   midbrain          -> brainparts.midbrain (mesencephalon)
    #   pons              -> brainparts.hindbrain.metencephalon.pons
    #   medulla oblongata -> brainparts.hindbrain.myelencephalon.
    #                        medulla_oblongata
    #
    # There is NO brainparts.brainstem container. Resolve each
    # segment through its own lobe.

Diencephalon continuity (recommended consumer pattern — NOTE the
topographic hazard)::

    # The cerebral aqueduct (midbrain) continues rostrally as the
    # third ventricle (diencephalon):
    #
    #   brainparts.midbrain.cerebral_aqueduct
    #   brainparts.forebrain.diencephalon.third_ventricle
    #
    # This is a CONTINUITY OF CSF SPACE, not a structural
    # parent-child relationship. The thalamus and hypothalamus are
    # diencephalon (forebrain), NOT midbrain.

References
----------
*   **Canonical midbrain anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (The definitive
    overview of the midbrain — tectum, tegmentum, aqueduct, cerebral
    peduncles; the mesencephalon as one of the three primary
    vesicles.)
*   **Developmental three-vesicle scheme:** Gilbert, S.F. (2014).
    *Developmental Biology*, 10th ed. (Prosencephalon, mesencephalon,
    rhombencephalon; the mesencephalon as a primary vesicle that
    does not subdivide into secondary vesicles.)
*   **Midbrain overview:** Haines, D.E. (2012). *Neuroanatomy: An
    Atlas of Structures, Sections, and Systems*, 8th ed. (Midbrain
    subdivisions; the tectum / tegmentum / cerebral peduncles
    organization; the cerebral aqueduct.)
*   **Superior colliculus (tectum — contrast child):** Sparks, D.L.
    (2002). "The brainstem control of saccadic eye movements."
    *Nature Reviews Neuroscience* 3:952–964. (Superior colliculus
    in visual orienting and saccade generation — contrast with the
    container.)
*   **Inferior colliculus (tectum — contrast child):** Ehret, G.,
    Romand, R. (eds.) (1997). *The Central Auditory System*. Oxford
    University Press. (Inferior colliculus in auditory processing —
    contrast with the container.)
*   **Substantia nigra (tegmentum — contrast child):** Parent, A.,
    Hazrati, L.N. (1995). "Functional anatomy of the basal ganglia.
    I. The cortico-basal ganglia-thalamo-cortical loop." *Brain
    Research Reviews* 20:91–127. (Substantia nigra as a tegmentum
    leaf — contrast with the container.)
*   **Ventral tegmental area (tegmentum — contrast child):**
    Fields, H.L., Hjelmstad, G.O., Margolis, E.B., Nicola, S.M.
    (2007). "Ventral tegmental area neurons in learned appetitive
    behavior and positive reinforcement." *Annual Review of
    Neuroscience* 30:289–316. (VTA as a tegmentum leaf — contrast
    with the container.)
*   **Red nucleus (tegmentum — contrast child):** ten Donkelaar,
    H.J. (1988). "Evolution of the red nucleus and rubrospinal
    tract." *Behavioural Brain Research* 28:9–20. (Red nucleus as a
    tegmentum leaf — contrast with the container.)
*   **Periaqueductal gray (tegmentum — contrast child):** Behbehani,
    M.M. (1995). "Functional characteristics of the midbrain
    periaqueductal gray." *Progress in Neurobiology* 46:575–605.
    (PAG as a midline tegmentum leaf — contrast with the container.)
*   **Oculomotor and trochlear nuclei (tegmentum — contrast
    children):** Büttner-Ennever, J.A. (2006). *Neuroanatomy of the
    Oculomotor System*. (CN III and CN IV nuclei as tegmentum
    leaves — contrast with the container and with the peripheral
    nerves.)
*   **Mesencephalic trigeminal nucleus (tegmentum — contrast
    child):** Lazarov, N.E. (2007). "The mesencephalic trigeminal
    nucleus in the mouse." *Annals of Anatomy* 189:349–360. (The
    only primary sensory nucleus in the CNS — a tegmentum leaf.)
*   **Cerebral peduncles (contrast child):** ten Donkelaar, H.J.,
    Lammens, M., Hori, A. (2003). *Clinical Neuroembryology:
    Development and Developmental Disorders of the Human Central
    Nervous System*. (Corticospinal and corticobulbar bundles in
    the cerebral peduncles — contrast with the container.)
*   **Diencephalon (contrast — the ROSTRAL sibling):** Jones, E.G.
    (1985). *The Thalamus*. (Diencephalon as a forebrain vesicle —
    contrast with the midbrain, despite the CSF-space continuity.)
*   **Hindbrain (contrast — the CAUDAL sibling):** Nieuwenhuys, R.,
    Voogd, J., van Huijzen, C. (2008). *The Human Central Nervous
    System: A Synopsis and Atlas*, 4th ed. (Metencephalon and
    myelencephalon — contrast with the mesencephalon.)
*   **Brainstem as a federated concept:** Blessing, W.W. (1997).
    *The Lower Brainstem and Bodily Homeostasis*. (The brainstem as
    a functional concept spanning midbrain, pons, and medulla —
    contrast with the structural tree.)
*   **Dopaminergic phenotype (chemicals_hormones-layer fact —
    contrast):** Björklund, A., Dunnett, S.B. (2007). "Dopamine
    neuron systems in the brain: an update." *Trends in
    Neurosciences* 30:194–202. (The dopaminergic phenotype as a
    chemicals-layer fact — documented as prose in the SN/VTA
    leaves, never imported.)
*   **SLEA (contrast — the midbrain is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    any midbrain structure.)
*   NeuroNames — Midbrain; FMA — Midbrain (mesencephalon).
"""