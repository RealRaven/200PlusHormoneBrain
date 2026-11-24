"""
infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left
============================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── cranial_nerve_nuclei
        ├── left                   <-- THIS MODULE (side container)
        │   ├── oculomotor_nucleus
        │   ├── trochlear_nucleus
        │   ├── mesencephalic_trigeminal_nucleus
        │   └── edinger_westphal_nucleus
        └── right
            ├── oculomotor_nucleus
            ├── trochlear_nucleus
            ├── mesencephalic_trigeminal_nucleus
            └── edinger_westphal_nucleus

**Primary synonym:** Left midbrain cranial nerve nuclei; left
mesencephalic CN nuclei; the left CN III / CN IV / CN Vm nuclear
group.
**Container status:** **This module is a SIDE-SCOPED CONTAINER, not
a leaf.** It groups the **four left-side midbrain CN nuclei** as a
**side-scoped namespace**. It carries **no substantive leaf-level
content** — the substantive content (function, disorders,
lateralization, boundary stacks, references) lives in the four
**left** leaf modules under it. Consumers resolving this module and
expecting a leaf should go **one level deeper** to the specific
nucleus leaf.
**Developmental designation:** **Mesencephalic (left side)** — the
CN nuclei grouped here are the **left-side** cranial-nerve nuclei
whose cell bodies lie within the **midbrain (mesencephalon)**.
**Structural parent:** ``.../cranial_nerve_nuclei/`` → **direct
child** of the functional grouping container.
**Structural children (expected — the tree is authoritative; each is
a CROSS-LISTED leaf whose topographic home is
``.../tegmentum/left/``):**
*   ``oculomotor_nucleus/`` — **left CN III** — **somatic motor**.
    Topographic home:
    ``.../tegmentum/left/oculomotor_nucleus/``.
*   ``trochlear_nucleus/`` — **left CN IV** — **somatic motor**;
    the **only CN that exits dorsally**; the **only CN whose fibers
    decussate before exiting** (left trochlear nucleus → **right**
    superior oblique).
    Topographic home:
    ``.../tegmentum/left/trochlear_nucleus/``.
*   ``mesencephalic_trigeminal_nucleus/`` — **left CN Vm** —
    **sensory** (proprioceptive); the **only primary sensory nucleus
    in the CNS** whose cell bodies lie within the CNS.
    Topographic home:
    ``.../tegmentum/left/mesencephalic_trigeminal_nucleus/``.
*   ``edinger_westphal_nucleus/`` — **left CN IIIp** —
    **preganglionic parasympathetic**; ciliary ganglion →
    sphincter pupillae and ciliary muscle.
    Topographic home:
    ``.../tegmentum/left/edinger_westphal_nucleus/``.

**Boundary status (SIDE CONTAINER — NOT a leaf, NOT the functional
grouping container):** **Boundary case — the ``left/`` module is a
SIDE-SCOPED CONTAINER, not a leaf and not the functional grouping
container.** The **functional grouping container** is
``.../cranial_nerve_nuclei/`` — it holds **both** the ``left/`` and
``right/`` side containers. This module (**here**) is the **left
side** of that pair — it holds exactly the **four left-side CN
nuclei**. The **substantive content** (function, disorders,
lateralization, boundary stacks, references) lives in each
``.../left/<nucleus>/`` leaf. Consumers resolving ``.../left`` and
expecting a leaf should go one level deeper. See *Design Contract*.
**Boundary status (NOT the ``right/`` side container — the SIDE
boundary):** **Boundary case — the ``left/`` module is NOT the
``right/`` module.** The **right side container**
(``.../cranial_nerve_nuclei/right/``) holds the four **right-side**
CN nuclei. **The two side containers are STRICTLY MIRRORED** — same
four CN nuclei, same leaf-level contract, **mirror-flipped
laterality facts** (see *Lateralization Notes*). Consumers must
**not** conflate the two, and must **not** resolve a right CN
nucleus through the left path.
**Boundary status (NOT the tegmentum side container — the tegmentum
is the TOPOGRAPHIC sibling):** **Boundary case — the ``left/``
module is NOT the ``.../tegmentum/left/`` module.** The **left
tegmentum** (``.../midbrain/tegmentum/left/``) is the **topographic
side container** — it holds the four **left CN nuclei** **plus** the
**left substantia nigra**, the **left ventral tegmental area**, the
**left red nucleus**, the **left periaqueductal gray**
(midline-adjacent), the **left riMLF**, the **left interstitial
nucleus of Cajal**, and the **left midbrain reticular formation**.
This module (**here**) is a **functional side container** that holds
**only** the four **left CN nuclei**. **The two side containers
OVERLAP** on the four CN nuclei — the **tegmentum side container is
the SUPERSET**; this side container is a **functional subset**.
Consumers must **not** conflate the two, and must **not** assume the
two enumerate **disjoint** leaf sets. See *Cross-Listing Statement*.
**Boundary status (CROSS-LISTING — the four left CN nuclei are ALSO
``.../tegmentum/left/<nucleus>/`` leaves):** **Boundary case — each
leaf under this side container is CROSS-LISTED with
``.../tegmentum/left/``.** The same leaf is reachable by **two**
paths:
*   **Functional path** —
    ``.../cranial_nerve_nuclei/left/<nucleus>/``
*   **Topographic path** —
    ``.../tegmentum/left/<nucleus>/``
**Both resolve to the SAME leaf.** Consumers enumerating **both**
paths will see **duplicates** for the four CN nuclei — this is the
**intended cross-listing**, not a bug. Consumers should resolve by
**one** path per lookup. See *Cross-Listing Statement*.
**Boundary status (SIDE-CONSISTENT, NOT bilateral — this is the LEFT
side only):** **Boundary case — this module is SIDE-CONSISTENT: it
holds ONLY left-side CN nuclei.** The **midbrain CN nuclei** are
**paired** structures — the left and right are **separate leaves**.
The left-side leaves under this container carry the **left-side**
laterality facts (left CN III palsy, left superior oblique weakness,
left pupillary abnormalities, **left** internuclear ophthalmoplegia
— see the individual leaf modules). Consumers must **not** assume a
"bilateral CN nucleus" — there is **no** midline CN nucleus in the
midbrain.
**Boundary status (MOTOR NUCLEI CARRY NO COUPLING WARNING):**
**Boundary case — the four left CN nuclei are **motor nuclei
(CN III, CN IV)**, a **sensory nucleus (CN Vm)**, and a
**preganglionic parasympathetic nucleus (Edinger-Westphal)** — and
**none carries a coupling warning**.** In the family's taxonomy,
**coupling warnings attach to oscillators only** — not to premotor
pools, not to sensor nuclei, not to conduction pathways, and **not
to motor nuclei**. The **left CN nuclei** are **independent** of the
**right CN nuclei** at the **nucleus** level; their **coordination**
is via **descending pathways** (the **MLF**, the **posterior
commissure**) — **not** via intrinsic nucleus-to-nucleus coupling.
**Motor nuclei carry NO coupling warning** — same rule as premotor
pools and sensor nuclei.
**Boundary status (CHEMICALS-LAYER DISCIPLINE — the cholinergic
phenotype of Edinger-Westphal is a chemicals-layer fact):**
**Boundary case — the **left Edinger-Westphal nucleus** is
**cholinergic**, and the **cholinergic phenotype** is a
``chemicals_hormones``-layer fact.** The **left Edinger-Westphal**
leaf documents the **anatomy** and **references** the chemicals
layer as prose. Consumers must **not** import the **cholinergic
phenotype** into the midbrain structural layer.

Overview
--------
The ``left/`` module is the **side-scoped container** for the
**left-side midbrain CN nuclei** — the **left oculomotor nucleus**
(CN III), the **left trochlear nucleus** (CN IV), the **left
mesencephalic trigeminal nucleus** (CN Vm), and the **left
Edinger-Westphal nucleus** (CN IIIp). It is a **thin namespace** —
the **substantive content** lives in each **left leaf** module under
it.

**This module is a SIDE CONTAINER, not a leaf.** The **functional
grouping container** is ``.../cranial_nerve_nuclei/``; this module is
the **left side** of that pair. Consumers resolving this module and
expecting a leaf should go one level deeper to the specific nucleus
leaf.

**The four left CN nuclei are ALSO ``.../tegmentum/left/<nucleus>/``
leaves.** The two paths are **equivalent** — the **tegmentum side
container is the superset**, and this side container is a
**functional subset**.

**The four left CN nuclei carry NO coupling warning.** They are
**motor nuclei**, a **sensory nucleus**, and a **preganglionic
parasympathetic nucleus** — **not oscillators**. Their coordination
with the **right side** is via **descending pathways** (MLF,
posterior commissure), **not** intrinsic nucleus-to-nucleus coupling.

**The ``left/`` module is a strict mirror of ``right/``.** The two
are **structurally identical** — same four CN nuclei, same leaf-level
contract, **mirror-flipped laterality facts**. See *Lateralization
Notes*.

Cross-Listing Statement (side-scoped)
-------------------------------------
Each left CN nucleus under this side container is **CROSS-LISTED**
with ``.../tegmentum/left/`` — the same leaf is reachable by **two**
side-scoped paths:

*   **Functional side-scoped path** —
    ``midbrain.cranial_nerve_nuclei.left.<nucleus>``
*   **Topographic side-scoped path** —
    ``midbrain.tegmentum.left.<nucleus>``

**Both resolve to the SAME leaf.** The **topographic side container**
(``.../tegmentum/left/``) holds the four left CN nuclei **plus** the
**left substantia nigra**, the **left ventral tegmental area**, the
**left red nucleus**, the **left periaqueductal gray**
(midline-adjacent), the **left riMLF**, the **left interstitial
nucleus of Cajal**, and the **left midbrain reticular formation**.
**Neither side enumeration is exhaustive in the other's sense** —
the **tegmentum side container is the superset**; this side container
is a **functional subset** of four CN nuclei.

**A consumer that resolves the left CN nuclei by EITHER path will be
structurally correct** — but a consumer that assumes
``tegmentum/left/`` and ``cranial_nerve_nuclei/left/`` contain
**disjoint** leaf sets will be **wrong** — the four left CN nuclei
are **shared**, and the **tegmentum side container is the superset**.

Aggregation Rules (the side container's contract on its children)
-----------------------------------------------------------------
The ``left/`` side container **imposes the following rules** on every
leaf under it. These are **inherited** from the
``cranial_nerve_nuclei/`` functional grouping container and the
``midbrain`` container, and are **side-scoped** for the left side:

*   **SIDE CONTAINER, NOT A LEAF.** This module is a **side-scoped
    namespace**. It carries **no substantive leaf-level content**;
    the substantive content lives in each left leaf module.
*   **FUNCTIONAL, NOT TOPOGRAPHIC, GROUPING (SIDE-SCOPED).** The
    container groups the **four left CN nuclei** by
    **cranial-nerve identity**, not by **topographic location**. A
    structure that is in the **left tegmentum but is NOT a CN
    nucleus** (left substantia nigra, left VTA, left red nucleus,
    left PAG, left riMLF, left interstitial nucleus of Cajal, left
    midbrain reticular formation) does **NOT** belong here.
*   **CROSS-LISTING DISCIPLINE (SIDE-SCOPED).** Every leaf here is
    **ALSO** a ``.../tegmentum/left/`` leaf. The leaf's **content**
    is identical under both paths. Consumers should **resolve by one
    path** — not by both — for a single lookup. Enumerating **both**
    paths will yield **duplicates** for the four left CN nuclei.
*   **CN-NUCLEI-ONLY — NOT NERVES, NOT PATHWAYS, NOT GAZE CENTERS.**
    The container holds CN **nuclei** — not the **nerves** (peripheral
    structures), not the **left MLF** (a conduction pathway), not the
    **left pretectal nuclei** (diencephalon), not the **left superior
    colliculus** (tectum), not the **left lateral geniculate body**
    (diencephalon/thalamus), and not the **left riMLF** or the
    **left interstitial nucleus of Cajal** (gaze centers).
*   **SIDE-CONSISTENT, NOT BILATERAL.** This container holds **ONLY
    left-side** CN nuclei. There is **no** midline CN nucleus in the
    midbrain.
*   **NO COUPLING WARNING.** The four left CN nuclei are motor
    nuclei, a sensory nucleus, and a preganglionic parasympathetic
    nucleus. **None carries a coupling warning** — same rule as
    premotor pools and sensor nuclei. Coordination with the right
    side is via descending pathways (MLF, posterior commissure), not
    intrinsic nucleus-to-nucleus coupling.
*   **CHEMICALS-LAYER DISCIPLINE.** The **cholinergic phenotype** of
    the left Edinger-Westphal nucleus is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the leaf, **never imported**.
*   **MIRROR PARITY WITH ``right/``.** The ``left/`` side container
    is a **strict mirror** of ``right/`` — same four CN nuclei, same
    leaf-level contract, **mirror-flipped laterality facts**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only — **no** import
    from ``.../right/``.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/``, ``.../tectum/``, ``.../cerebral_peduncle/``,
    the **pretectal nuclei**, the **MLF**, the **riMLF**, the
    **interstitial nucleus of Cajal**, or any other container. The
    left CN nuclei's relationships to the left tegmentum, the left
    MLF, the left pretectal nuclei, the left superior colliculus, the
    left lateral geniculate body, the left riMLF, the left
    interstitial nucleus of Cajal, the pontine CN nuclei, the
    medullary CN nuclei, the ciliary ganglion, and the CN nerves are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **cholinergic
    phenotype** of the left Edinger-Westphal nucleus is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the leaf, **never imported**.
*   **SIDE CONTAINER — not a leaf.** The substantive content lives in
    each left leaf module. Consumers resolving ``.../left`` and
    expecting a leaf should go one level deeper.
*   **CROSS-LISTING via ``AREA_PATHS``.** The four left CN nuclei are
    cross-listed between ``.../tegmentum/left/`` and
    ``.../cranial_nerve_nuclei/left/``. The **tegmentum side
    container is the superset**; this side container is a
    **functional subset** of four left CN nuclei.
*   **CONSISTENT with the ``cranial_nerve_nuclei/`` and ``midbrain``
    container child lists.** Both upper containers place the CN
    nuclei under ``tegmentum/`` (their topographic home) **and**
    cross-list them under ``cranial_nerve_nuclei/`` (their functional
    grouping). This side container is the **left-side** slice of that
    cross-listing.
*   **CN NUCLEI — NOT CN NERVES, NOT PATHWAYS, NOT GAZE CENTERS.**
*   **SIDE-CONSISTENT — no midline CN nucleus.**
*   **NO COUPLING WARNING.** Motor nuclei, sensory nuclei, and
    preganglionic parasympathetic nuclei carry no coupling warning.
*   **CHEMICALS-LAYER DISCIPLINE.**
*   **MIRROR PARITY with ``right/`` — strict mirror, no warning.**
*   **The on-disk tree is authoritative.** The expected children
    listed above are the **standard left midbrain CN nuclei**; the
    actual children are **whatever exists on disk**.
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum/left`` ↔
    ``cranial_nerve_nuclei/left``) — not into the forebrain, hindbrain,
    or periphery.
*   **No nested cross-listing.** The four left CN nuclei are
    single-level cross-listed leaves. They are not themselves
    containers.

Usage
-----
Resolve the side container by path::

    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei import left

Resolve a left leaf by **either** side-scoped path (they are
equivalent)::

    # Functional side-scoped path (clinician framing):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left import oculomotor_nucleus

    # Topographic side-scoped path (anatomist framing):
    from infrastructure.brainparts.midbrain.tegmentum.left import oculomotor_nucleus

Or by fully-qualified path string (leaves, not the side container)::

    oculomotor_functional_left_path = (
        "midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus"
    )
    oculomotor_topographic_left_path = (
        "midbrain.tegmentum.left.oculomotor_nucleus"
    )
    # Both resolve to the same left leaf.

**Do not** assume the ``left/`` module is a **leaf**. It is a
**side-scoped container** — the substantive content (function,
disorders, lateralization, boundary stacks, references) lives in
each ``.../left/<nucleus>/`` leaf. Go one level deeper.

**Do not** assume the ``left/`` module is the **``cranial_nerve_nuclei/``
functional grouping container**. It is the **left side** of that
pair. The functional grouping container holds **both** ``left/`` and
``right/``.

**Do not** assume the ``left/`` module and ``.../tegmentum/left/``
contain **disjoint** leaf sets. The four left CN nuclei are
**shared**, and the **tegmentum side container is the superset** —
it also holds the left substantia nigra, left VTA, left red nucleus,
left PAG, left riMLF, left interstitial nucleus of Cajal, and left
midbrain reticular formation.

**Do not** assume the ``left/`` module contains **all** left CN
nuclei. It contains **only the left midbrain CN nuclei** — the
**left pontine** CN nuclei (left CN V main, VI, VII, VIII) and the
**left medullary** CN nuclei (left CN IX, X, XI, XII) are
**elsewhere**.

**Do not** conflate the left CN **nuclei** with the left CN
**nerves**. The **nerves** are peripheral; the **nuclei** are here.

**Do not** conflate the left CN **nuclei** with the **left MLF**. The
**left MLF** is a **conduction pathway** — a **longitudinal fiber
tract** — not a CN nucleus. **A left MLF lesion produces a LEFT
internuclear ophthalmoplegia (INO), NOT a left CN III or left CN IV
nuclear palsy.** These are **different syndromes**.

**Do not** conflate the left CN **nuclei** with the **left
pretectal nuclei** (diencephalon — the afferent relay of the
pupillary light reflex), the **left superior colliculus** (tectum —
drives the CN nuclei for saccades but is not a CN nucleus), the
**left lateral geniculate body** (diencephalon/thalamus — visual
relay), the **left riMLF** and the **left interstitial nucleus of
Cajal** (gaze centers — premotor saccade generators, not CN nuclei).

**Do not** import the **cholinergic phenotype** of the left
Edinger-Westphal nucleus into the midbrain structural layer. The
**cholinergic phenotype** is a **``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the left CN nuclei.
**Motor nuclei, sensory nuclei, and preganglionic parasympathetic
nuclei carry NO coupling warning** — same rule as premotor pools and
sensor nuclei.

Iterating the ``left/`` side container's children (recommended
consumer pattern — NOTE cross-listing)::

    import pkgutil
    import infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left as cnn_left_pkg

    CNN_LEFT_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(cnn_left_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("oculomotor_nucleus", "trochlear_nucleus",
    #            "mesencephalic_trigeminal_nucleus",
    #            "edinger_westphal_nucleus")
    #
    # Each of these is ALSO a .../tegmentum/left/ child. Enumerating
    # .../tegmentum/left/ will yield these four PLUS left
    # substantia_nigra, left ventral_tegmental_area, left
    # red_nucleus, left periaqueductal_gray (midline-adjacent),
    # left riMLF, left interstitial_nucleus_of_cajal, and left
    # midbrain_reticular_formation.
    #
    # Do NOT assume the two enumerations are disjoint — they are
    # NOT. The tegmentum side container is the SUPERSET.

Reaching the ``right/`` side container (recommended consumer
pattern — the SIDE sibling)::

    # The right/ side container holds the four right midbrain CN
    # nuclei:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right
    #
    # The two side containers are STRICTLY MIRRORED — same four
    # CN nuclei, same leaf-level contract, mirror-flipped laterality
    # facts.

Reaching the topographic side container (recommended consumer
pattern — the tegmentum is the SUPERSET)::

    # The left tegmentum is the TOPOGRAPHIC side container — it
    # holds the four left CN nuclei PLUS left substantia nigra,
    # left VTA, left red nucleus, left PAG, left riMLF, left
    # interstitial nucleus of Cajal, and left midbrain reticular
    # formation:
    #
    #   brainparts.midbrain.tegmentum.left
    #
    # The cranial_nerve_nuclei/left/ is a FUNCTIONAL subset — the
    # four left CN nuclei cross-listed from the left tegmentum.

Reaching the ``cranial_nerve_nuclei/`` functional grouping
container (recommended consumer pattern — the PAIR parent)::

    # The cranial_nerve_nuclei/ container holds BOTH the left/ and
    # right/ side containers:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei
    #
    # The left/ is the LEFT SIDE of that pair.

Reaching the midbrain container (recommended consumer pattern —
the LOBE parent)::

    # The midbrain container holds the CN nuclei under BOTH paths
    # (topographic tegmentum/ AND functional cranial_nerve_nuclei/):
    #
    #   brainparts.midbrain
    #
    # The CN nuclei are TOPOGRAPHICALLY in the tegmentum, and
    # FUNCTIONALLY grouped under cranial_nerve_nuclei.

Bilateral iteration (recommended consumer pattern — NOTE
cross-listing and the no-coupling-warning rule)::

    for side in ("left", "right"):
        for nucleus in (
            "oculomotor_nucleus",
            "trochlear_nucleus",
            "mesencephalic_trigeminal_nucleus",
            "edinger_westphal_nucleus",
        ):
            # Either path resolves to the same leaf — use ONE:
            path = (
                f"midbrain.cranial_nerve_nuclei.{side}.{nucleus}"
            )
            # OR:
            # path = f"midbrain.tegmentum.{side}.{nucleus}"
            #
            # resolve path through the memory/recall layer
            #
            # NOTE: the CN nuclei are MOTOR NUCLEI (CN III, CN IV),
            # a SENSORY NUCLEUS (CN Vm), and a PREGANGLIONIC
            # PARASYMPATHETIC NUCLEUS (Edinger-Westphal). NONE
            # carries a coupling warning. Coordination with the
            # contralateral side is via descending pathways (MLF,
            # posterior commissure), not intrinsic
            # nucleus-to-nucleus coupling.

References
----------
*   **See the ``cranial_nerve_nuclei/`` container's References
    section** for the canonical CN-nuclei anatomy, function, and
    clinical literature (Büttner-Ennever, Gamlin, Wilhelm, Frohman
    et al., Sparks, Lazarov, Brodal).
*   **See the individual left leaf modules**
    (``oculomotor_nucleus/``, ``trochlear_nucleus/``,
    ``mesencephalic_trigeminal_nucleus/``, ``edinger_westphal_nucleus/``)
    for the substantive, laterality-specific references.
*   **Canonical midbrain anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (The midbrain
    CN nuclei — topographic and functional organization, side by
    side.)
*   **SLEA (contrast — the left CN nuclei are not SLEA):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    any midbrain CN nucleus.)
*   NeuroNames — Oculomotor nucleus (left); Trochlear nucleus (left);
    Mesencephalic trigeminal nucleus (left); Edinger-Westphal nucleus
    (left); FMA — corresponding entries.
"""