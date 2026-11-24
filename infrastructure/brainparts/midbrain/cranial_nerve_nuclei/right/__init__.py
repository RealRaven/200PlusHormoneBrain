"""
infrastructure.brainparts.midbrain.cranial_nerve_nuclei.right
=============================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── cranial_nerve_nuclei
        ├── left
        │   ├── oculomotor_nucleus
        │   ├── trochlear_nucleus
        │   ├── mesencephalic_trigeminal_nucleus
        │   └── edinger_westphal_nucleus
        └── right                  <-- THIS MODULE (side container)
            ├── oculomotor_nucleus
            ├── trochlear_nucleus
            ├── mesencephalic_trigeminal_nucleus
            └── edinger_westphal_nucleus

**Primary synonym:** Right midbrain cranial nerve nuclei; right
mesencephalic CN nuclei; the right CN III / CN IV / CN Vm nuclear
group.
**Container status:** **This module is a SIDE-SCOPED CONTAINER, not
a leaf.** It groups the **four right-side midbrain CN nuclei** as a
**side-scoped namespace**. It carries **no substantive leaf-level
content** — the substantive content (function, disorders,
lateralization, boundary stacks, references) lives in the four
**right** leaf modules under it. Consumers resolving this module and
expecting a leaf should go **one level deeper** to the specific
nucleus leaf.
**Developmental designation:** **Mesencephalic (right side)** — the
CN nuclei grouped here are the **right-side** cranial-nerve nuclei
whose cell bodies lie within the **midbrain (mesencephalon)**.
**Structural parent:** ``.../cranial_nerve_nuclei/`` → **direct
child** of the functional grouping container.
**Structural children (expected — the tree is authoritative; each is
a CROSS-LISTED leaf whose topographic home is
``.../tegmentum/right/``):**
*   ``oculomotor_nucleus/`` — **right CN III** — **somatic motor**.
    Topographic home:
    ``.../tegmentum/right/oculomotor_nucleus/``.
*   ``trochlear_nucleus/`` — **right CN IV** — **somatic motor**;
    the **only CN that exits dorsally**; the **only CN whose fibers
    decussate before exiting** (right trochlear nucleus → **left**
    superior oblique).
    Topographic home:
    ``.../tegmentum/right/trochlear_nucleus/``.
*   ``mesencephalic_trigeminal_nucleus/`` — **right CN Vm** —
    **sensory** (proprioceptive); the **only primary sensory nucleus
    in the CNS** whose cell bodies lie within the CNS.
    Topographic home:
    ``.../tegmentum/right/mesencephalic_trigeminal_nucleus/``.
*   ``edinger_westphal_nucleus/`` — **right CN IIIp** —
    **preganglionic parasympathetic**; ciliary ganglion →
    sphincter pupillae and ciliary muscle.
    Topographic home:
    ``.../tegmentum/right/edinger_westphal_nucleus/``.

**Boundary status (SIDE CONTAINER — NOT a leaf, NOT the functional
grouping container):** **Boundary case — the ``right/`` module is a
SIDE-SCOPED CONTAINER, not a leaf and not the functional grouping
container.** The **functional grouping container** is
``.../cranial_nerve_nuclei/`` — it holds **both** the ``left/`` and
``right/`` side containers. This module (**here**) is the **right
side** of that pair — it holds exactly the **four right-side CN
nuclei**. The **substantive content** (function, disorders,
lateralization, boundary stacks, references) lives in each
``.../right/<nucleus>/`` leaf. Consumers resolving ``.../right`` and
expecting a leaf should go one level deeper. See *Design Contract*.
**Boundary status (NOT the ``left/`` side container — the SIDE
boundary):** **Boundary case — the ``right/`` module is NOT the
``left/`` module.** The **left side container**
(``.../cranial_nerve_nuclei/left/``) holds the four **left-side**
CN nuclei. **The two side containers are STRICTLY MIRRORED** — same
four CN nuclei, same leaf-level contract, **mirror-flipped
laterality facts** (see *Lateralization Notes*). Consumers must
**not** conflate the two, and must **not** resolve a left CN
nucleus through the right path.
**Boundary status (NOT the tegmentum side container — the tegmentum
is the TOPOGRAPHIC sibling):** **Boundary case — the ``right/``
module is NOT the ``.../tegmentum/right/`` module.** The **right
tegmentum** (``.../midbrain/tegmentum/right/``) is the **topographic
side container** — it holds the four **right CN nuclei** **plus** the
**right substantia nigra**, the **right ventral tegmental area**, the
**right red nucleus**, the **right periaqueductal gray**
(midline-adjacent), the **right riMLF**, the **right interstitial
nucleus of Cajal**, and the **right midbrain reticular formation**.
This module (**here**) is a **functional side container** that holds
**only** the four **right CN nuclei**. **The two side containers
OVERLAP** on the four CN nuclei — the **tegmentum side container is
the SUPERSET**; this side container is a **functional subset**.
Consumers must **not** conflate the two, and must **not** assume the
two enumerate **disjoint** leaf sets. See *Cross-Listing Statement*.
**Boundary status (CROSS-LISTING — the four right CN nuclei are ALSO
``.../tegmentum/right/<nucleus>/`` leaves):** **Boundary case — each
leaf under this side container is CROSS-LISTED with
``.../tegmentum/right/``.** The same leaf is reachable by **two**
paths:
*   **Functional path** —
    ``.../cranial_nerve_nuclei/right/<nucleus>/``
*   **Topographic path** —
    ``.../tegmentum/right/<nucleus>/``
**Both resolve to the SAME leaf.** Consumers enumerating **both**
paths will see **duplicates** for the four CN nuclei — this is the
**intended cross-listing**, not a bug. Consumers should resolve by
**one** path per lookup. See *Cross-Listing Statement*.
**Boundary status (SIDE-CONSISTENT, NOT bilateral — this is the RIGHT
side only):** **Boundary case — this module is SIDE-CONSISTENT: it
holds ONLY right-side CN nuclei.** The **midbrain CN nuclei** are
**paired** structures — the left and right are **separate leaves**.
The right-side leaves under this container carry the **right-side**
laterality facts (right CN III palsy, right superior oblique
weakness, right pupillary abnormalities, **right** internuclear
ophthalmoplegia — see the individual leaf modules). Consumers must
**not** assume a "bilateral CN nucleus" — there is **no** midline CN
nucleus in the midbrain.
**Boundary status (MOTOR NUCLEI CARRY NO COUPLING WARNING):**
**Boundary case — the four right CN nuclei are **motor nuclei
(CN III, CN IV)**, a **sensory nucleus (CN Vm)**, and a
**preganglionic parasympathetic nucleus (Edinger-Westphal)** — and
**none carries a coupling warning**.** In the family's taxonomy,
**coupling warnings attach to oscillators only** — not to premotor
pools, not to sensor nuclei, not to conduction pathways, and **not
to motor nuclei**. The **right CN nuclei** are **independent** of
the **left CN nuclei** at the **nucleus** level; their
**coordination** is via **descending pathways** (the **MLF**, the
**posterior commissure**) — **not** via intrinsic nucleus-to-nucleus
coupling. **Motor nuclei carry NO coupling warning** — same rule as
premotor pools and sensor nuclei.
**Boundary status (CHEMICALS-LAYER DISCIPLINE — the cholinergic
phenotype of Edinger-Westphal is a chemicals-layer fact):**
**Boundary case — the **right Edinger-Westphal nucleus** is
**cholinergic**, and the **cholinergic phenotype** is a
``chemicals_hormones``-layer fact.** The **right Edinger-Westphal**
leaf documents the **anatomy** and **references** the chemicals
layer as prose. Consumers must **not** import the **cholinergic
phenotype** into the midbrain structural layer.

Overview
--------
The ``right/`` module is the **side-scoped container** for the
**right-side midbrain CN nuclei** — the **right oculomotor nucleus**
(CN III), the **right trochlear nucleus** (CN IV), the **right
mesencephalic trigeminal nucleus** (CN Vm), and the **right
Edinger-Westphal nucleus** (CN IIIp). It is a **thin namespace** —
the **substantive content** lives in each **right leaf** module under
it.

**This module is a SIDE CONTAINER, not a leaf.** The **functional
grouping container** is ``.../cranial_nerve_nuclei/``; this module is
the **right side** of that pair. Consumers resolving this module and
expecting a leaf should go one level deeper to the specific nucleus
leaf.

**The four right CN nuclei are ALSO ``.../tegmentum/right/<nucleus>/``
leaves.** The two paths are **equivalent** — the **tegmentum side
container is the superset**, and this side container is a
**functional subset**.

**The four right CN nuclei carry NO coupling warning.** They are
**motor nuclei**, a **sensory nucleus**, and a **preganglionic
parasympathetic nucleus** — **not oscillators**. Their coordination
with the **left side** is via **descending pathways** (MLF,
posterior commissure), **not** intrinsic nucleus-to-nucleus coupling.

**The ``right/`` module is a strict mirror of ``left/``.** The two
are **structurally identical** — same four CN nuclei, same leaf-level
contract, **mirror-flipped laterality facts**. See *Lateralization
Notes*.

Cross-Listing Statement (side-scoped)
-------------------------------------
Each right CN nucleus under this side container is **CROSS-LISTED**
with ``.../tegmentum/right/`` — the same leaf is reachable by **two**
side-scoped paths:

*   **Functional side-scoped path** —
    ``midbrain.cranial_nerve_nuclei.right.<nucleus>``
*   **Topographic side-scoped path** —
    ``midbrain.tegmentum.right.<nucleus>``

**Both resolve to the SAME leaf.** The **topographic side container**
(``.../tegmentum/right/``) holds the four right CN nuclei **plus** the
**right substantia nigra**, the **right ventral tegmental area**, the
**right red nucleus**, the **right periaqueductal gray**
(midline-adjacent), the **right riMLF**, the **right interstitial
nucleus of Cajal**, and the **right midbrain reticular formation**.
**Neither side enumeration is exhaustive in the other's sense** —
the **tegmentum side container is the superset**; this side container
is a **functional subset** of four CN nuclei.

**A consumer that resolves the right CN nuclei by EITHER path will
be structurally correct** — but a consumer that assumes
``tegmentum/right/`` and ``cranial_nerve_nuclei/right/`` contain
**disjoint** leaf sets will be **wrong** — the four right CN nuclei
are **shared**, and the **tegmentum side container is the superset**.

Aggregation Rules (the side container's contract on its children)
-----------------------------------------------------------------
The ``right/`` side container **imposes the following rules** on
every leaf under it. These are **inherited** from the
``cranial_nerve_nuclei/`` functional grouping container and the
``midbrain`` container, and are **side-scoped** for the right side:

*   **SIDE CONTAINER, NOT A LEAF.** This module is a **side-scoped
    namespace**. It carries **no substantive leaf-level content**;
    the substantive content lives in each right leaf module.
*   **FUNCTIONAL, NOT TOPOGRAPHIC, GROUPING (SIDE-SCOPED).** The
    container groups the **four right CN nuclei** by
    **cranial-nerve identity**, not by **topographic location**. A
    structure that is in the **right tegmentum but is NOT a CN
    nucleus** (right substantia nigra, right VTA, right red nucleus,
    right PAG, right riMLF, right interstitial nucleus of Cajal,
    right midbrain reticular formation) does **NOT** belong here.
*   **CROSS-LISTING DISCIPLINE (SIDE-SCOPED).** Every leaf here is
    **ALSO** a ``.../tegmentum/right/`` leaf. The leaf's **content**
    is identical under both paths. Consumers should **resolve by one
    path** — not by both — for a single lookup. Enumerating **both**
    paths will yield **duplicates** for the four right CN nuclei.
*   **CN-NUCLEI-ONLY — NOT NERVES, NOT PATHWAYS, NOT GAZE CENTERS.**
    The container holds CN **nuclei** — not the **nerves** (peripheral
    structures), not the **right MLF** (a conduction pathway), not the
    **right pretectal nuclei** (diencephalon), not the **right
    superior colliculus** (tectum), not the **right lateral geniculate
    body** (diencephalon/thalamus), and not the **right riMLF** or the
    **right interstitial nucleus of Cajal** (gaze centers).
*   **SIDE-CONSISTENT, NOT BILATERAL.** This container holds **ONLY
    right-side** CN nuclei. There is **no** midline CN nucleus in the
    midbrain.
*   **NO COUPLING WARNING.** The four right CN nuclei are motor
    nuclei, a sensory nucleus, and a preganglionic parasympathetic
    nucleus. **None carries a coupling warning** — same rule as
    premotor pools and sensor nuclei. Coordination with the left
    side is via descending pathways (MLF, posterior commissure), not
    intrinsic nucleus-to-nucleus coupling.
*   **CHEMICALS-LAYER DISCIPLINE.** The **cholinergic phenotype** of
    the right Edinger-Westphal nucleus is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the leaf, **never imported**.
*   **MIRROR PARITY WITH ``left/``.** The ``right/`` side container
    is a **strict mirror** of ``left/`` — same four CN nuclei, same
    leaf-level contract, **mirror-flipped laterality facts**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only — **no** import
    from ``.../left/``.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../tegmentum/``, ``.../tectum/``, ``.../cerebral_peduncle/``,
    the **pretectal nuclei**, the **MLF**, the **riMLF**, the
    **interstitial nucleus of Cajal**, or any other container. The
    right CN nuclei's relationships to the right tegmentum, the right
    MLF, the right pretectal nuclei, the right superior colliculus,
    the right lateral geniculate body, the right riMLF, the right
    interstitial nucleus of Cajal, the pontine CN nuclei, the
    medullary CN nuclei, the ciliary ganglion, and the CN nerves are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **cholinergic
    phenotype** of the right Edinger-Westphal nucleus is a
    ``chemicals_hormones``-layer fact — documented as **prose** in
    the leaf, **never imported**.
*   **SIDE CONTAINER — not a leaf.** The substantive content lives in
    each right leaf module. Consumers resolving ``.../right`` and
    expecting a leaf should go one level deeper.
*   **CROSS-LISTING via ``AREA_PATHS``.** The four right CN nuclei are
    cross-listed between ``.../tegmentum/right/`` and
    ``.../cranial_nerve_nuclei/right/``. The **tegmentum side
    container is the superset**; this side container is a
    **functional subset** of four right CN nuclei.
*   **CONSISTENT with the ``cranial_nerve_nuclei/`` and ``midbrain``
    container child lists.** Both upper containers place the CN
    nuclei under ``tegmentum/`` (their topographic home) **and**
    cross-list them under ``cranial_nerve_nuclei/`` (their functional
    grouping). This side container is the **right-side** slice of
    that cross-listing.
*   **CN NUCLEI — NOT CN NERVES, NOT PATHWAYS, NOT GAZE CENTERS.**
*   **SIDE-CONSISTENT — no midline CN nucleus.**
*   **NO COUPLING WARNING.** Motor nuclei, sensory nuclei, and
    preganglionic parasympathetic nuclei carry no coupling warning.
*   **CHEMICALS-LAYER DISCIPLINE.**
*   **MIRROR PARITY with ``left/`` — strict mirror, no warning.**
*   **The on-disk tree is authoritative.** The expected children
    listed above are the **standard right midbrain CN nuclei**; the
    actual children are **whatever exists on disk**.
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum/right`` ↔
    ``cranial_nerve_nuclei/right``) — not into the forebrain,
    hindbrain, or periphery.
*   **No nested cross-listing.** The four right CN nuclei are
    single-level cross-listed leaves. They are not themselves
    containers.

Usage
-----
Resolve the side container by path::

    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei import right

Resolve a right leaf by **either** side-scoped path (they are
equivalent)::

    # Functional side-scoped path (clinician framing):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei.right import oculomotor_nucleus

    # Topographic side-scoped path (anatomist framing):
    from infrastructure.brainparts.midbrain.tegmentum.right import oculomotor_nucleus

Or by fully-qualified path string (leaves, not the side container)::

    oculomotor_functional_right_path = (
        "midbrain.cranial_nerve_nuclei.right.oculomotor_nucleus"
    )
    oculomotor_topographic_right_path = (
        "midbrain.tegmentum.right.oculomotor_nucleus"
    )
    # Both resolve to the same right leaf.

**Do not** assume the ``right/`` module is a **leaf**. It is a
**side-scoped container** — the substantive content (function,
disorders, lateralization, boundary stacks, references) lives in
each ``.../right/<nucleus>/`` leaf. Go one level deeper.

**Do not** assume the ``right/`` module is the **``cranial_nerve_nuclei/``
functional grouping container**. It is the **right side** of that
pair. The functional grouping container holds **both** ``left/`` and
``right/``.

**Do not** assume the ``right/`` module and ``.../tegmentum/right/``
contain **disjoint** leaf sets. The four right CN nuclei are
**shared**, and the **tegmentum side container is the superset** —
it also holds the right substantia nigra, right VTA, right red
nucleus, right PAG, right riMLF, right interstitial nucleus of Cajal,
and right midbrain reticular formation.

**Do not** assume the ``right/`` module contains **all** right CN
nuclei. It contains **only the right midbrain CN nuclei** — the
**right pontine** CN nuclei (right CN V main, VI, VII, VIII) and the
**right medullary** CN nuclei (right CN IX, X, XI, XII) are
**elsewhere**.

**Do not** conflate the right CN **nuclei** with the right CN
**nerves**. The **nerves** are peripheral; the **nuclei** are here.

**Do not** conflate the right CN **nuclei** with the **right MLF**.
The **right MLF** is a **conduction pathway** — a **longitudinal
fiber tract** — not a CN nucleus. **A right MLF lesion produces a
RIGHT internuclear ophthalmoplegia (INO), NOT a right CN III or right
CN IV nuclear palsy.** These are **different syndromes**.

**Do not** conflate the right CN **nuclei** with the **right
pretectal nuclei** (diencephalon — the afferent relay of the
pupillary light reflex), the **right superior colliculus** (tectum —
drives the CN nuclei for saccades but is not a CN nucleus), the
**right lateral geniculate body** (diencephalon/thalamus — visual
relay), the **right riMLF** and the **right interstitial nucleus of
Cajal** (gaze centers — premotor saccade generators, not CN nuclei).

**Do not** import the **cholinergic phenotype** of the right
Edinger-Westphal nucleus into the midbrain structural layer. The
**cholinergic phenotype** is a **``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the right CN nuclei.
**Motor nuclei, sensory nuclei, and preganglionic parasympathetic
nuclei carry NO coupling warning** — same rule as premotor pools and
sensor nuclei.

Iterating the ``right/`` side container's children (recommended
consumer pattern — NOTE cross-listing)::

    import pkgutil
    import infrastructure.brainparts.midbrain.cranial_nerve_nuclei.right as cnn_right_pkg

    CNN_RIGHT_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(cnn_right_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("oculomotor_nucleus", "trochlear_nucleus",
    #            "mesencephalic_trigeminal_nucleus",
    #            "edinger_westphal_nucleus")
    #
    # Each of these is ALSO a .../tegmentum/right/ child. Enumerating
    # .../tegmentum/right/ will yield these four PLUS right
    # substantia_nigra, right ventral_tegmental_area, right
    # red_nucleus, right periaqueductal_gray (midline-adjacent),
    # right riMLF, right interstitial_nucleus_of_cajal, and right
    # midbrain_reticular_formation.
    #
    # Do NOT assume the two enumerations are disjoint — they are
    # NOT. The tegmentum side container is the SUPERSET.

Reaching the ``left/`` side container (recommended consumer
pattern — the SIDE sibling)::

    # The left/ side container holds the four left midbrain CN
    # nuclei:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left
    #
    # The two side containers are STRICTLY MIRRORED — same four
    # CN nuclei, same leaf-level contract, mirror-flipped laterality
    # facts.

Reaching the topographic side container (recommended consumer
pattern — the tegmentum is the SUPERSET)::

    # The right tegmentum is the TOPOGRAPHIC side container — it
    # holds the four right CN nuclei PLUS right substantia nigra,
    # right VTA, right red nucleus, right PAG, right riMLF, right
    # interstitial nucleus of Cajal, and right midbrain reticular
    # formation:
    #
    #   brainparts.midbrain.tegmentum.right
    #
    # The cranial_nerve_nuclei/right/ is a FUNCTIONAL subset — the
    # four right CN nuclei cross-listed from the right tegmentum.

Reaching the ``cranial_nerve_nuclei/`` functional grouping
container (recommended consumer pattern — the PAIR parent)::

    # The cranial_nerve_nuclei/ container holds BOTH the left/ and
    # right/ side containers:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei
    #
    # The right/ is the RIGHT SIDE of that pair.

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
*   **See the individual right leaf modules**
    (``oculomotor_nucleus/``, ``trochlear_nucleus/``,
    ``mesencephalic_trigeminal_nucleus/``, ``edinger_westphal_nucleus/``)
    for the substantive, laterality-specific references.
*   **Canonical midbrain anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (The midbrain
    CN nuclei — topographic and functional organization, side by
    side.)
*   **SLEA (contrast — the right CN nuclei are not SLEA):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    any midbrain CN nucleus.)
*   NeuroNames — Oculomotor nucleus (right); Trochlear nucleus
    (right); Mesencephalic trigeminal nucleus (right);
    Edinger-Westphal nucleus (right); FMA — corresponding entries.
"""