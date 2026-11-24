"""
infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.right
====================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tectum
        ├── left
        │   └── ...
        ├── right
        │   ├── superior_colliculus               (modern path)
        │   └── inferior_colliculus
        └── corpora_quadrigemina
            ├── left
            │   └── ...
            └── right                   <-- THIS MODULE (side container)
                ├── superior_colliculus  (CROSS-LISTED — SAME leaf as
                │                         .../tectum/right/superior_colliculus)
                └── inferior_colliculus  (CROSS-LISTED — SAME leaf as
                                          .../tectum/right/inferior_colliculus)

**Primary synonym:** Right corpora quadrigemina; **the right two
bodies**; **right quadrigeminal plate**; **right corpora quadrigemina
anterior** (right superior colliculus); **right corpora quadrigemina
posterior** (right inferior colliculus).
**Container status:** **This module is a SIDE-SCOPED CONTAINER, not
a leaf.** It holds the **two right colliculi** (superior + inferior)
under the **older-term** path. Its children are **CROSS-LISTED** —
they are the **SAME leaves** as
``.../tectum/right/superior_colliculus/`` and
``.../tectum/right/inferior_colliculus/``. It carries **no unique
leaf-level content** — the substantive content (structure classes,
rostrocaudal anchors, boundary stacks, function, disorders,
lateralization, references) lives in the **modern-path leaves**
under ``.../tectum/right/``. Consumers resolving this module and
expecting a leaf should go **one level deeper** to the specific
colliculus leaf.
**Developmental designation:** **Mesencephalic (right side)** — the
right colliculi are **unambiguously mesencephalic** — no contested
placement, no junction ambiguity.
**Structural parent:** ``.../tectum/corpora_quadrigemina/`` →
**direct child** of the corpora quadrigemina synonym container.
**Structural children (expected — the tree is authoritative; each is
a CROSS-LISTED leaf whose structural home is
``.../tectum/right/``):**
*   ``superior_colliculus/`` — **right superior colliculus** —
    **sensorimotor integration / saccade command generator** —
    **rostral** — at the **oculomotor / EW / mesV level**.
    Structural home: ``.../tectum/right/superior_colliculus/``.
*   ``inferior_colliculus/`` — **right inferior colliculus** —
    **auditory relay** — **caudal** — at the **trochlear level**.
    Structural home: ``.../tectum/right/inferior_colliculus/``.

**Boundary status (SIDE-SCOPED SYNONYM CONTAINER — NOT a leaf, NOT
the corpora quadrigemina container):** **Boundary case — the
``right/`` module is a SIDE-SCOPED CONTAINER, not a leaf and not the
corpora quadrigemina container.** The **corpora quadrigemina
container** is ``.../tectum/corpora_quadrigemina/`` — it holds
**both** the ``left/`` and ``right/`` side containers. This module
(**here**) is the **right side** of that pair — it holds exactly the
**two right colliculi** (superior + inferior). The **substantive
content** (structure classes, rostrocaudal anchors, boundary
stacks, function, disorders, lateralization, references) lives in
the **modern-path leaves** under ``.../tectum/right/``. Consumers
resolving ``.../corpora_quadrigemina/right`` and expecting a leaf
should go one level deeper. See *Design Contract*.
**Boundary status (CROSS-LISTING — the two right colliculi are the
SAME leaves as ``.../tectum/right/``):** **Boundary case — each leaf
under this side container is CROSS-LISTED with
``.../tectum/right/``.** The **right superior colliculus** and the
**right inferior colliculus** are reachable by **two** paths:
*   **Modern path (structural home)** —
    ``.../tectum/right/superior_colliculus/`` and
    ``.../tectum/right/inferior_colliculus/``
*   **Older-term path (synonym alias)** —
    ``.../tectum/corpora_quadrigemina/right/superior_colliculus/`` and
    ``.../tectum/corpora_quadrigemina/right/inferior_colliculus/``
**Both paths resolve to the SAME TWO LEAVES.** **The modern path is
the structural home** — the **corpora_quadrigemina** path is the
**older-term alias**. Consumers should resolve by **one** path per
lookup — enumerating **both** paths yields **duplicates** for the
two right colliculi. See *Cross-Listing Statement*.
**Boundary status (NOT the ``left/`` side container — the SIDE
boundary):** **Boundary case — the ``right/`` module is NOT the
``left/`` module.** The **left side container**
(``.../tectum/corpora_quadrigemina/left/``) holds the **two left
colliculi** (left SC + left IC). **The two side containers are
STRICTLY MIRRORED** — each holds the two colliculi on its side, and
each is **cross-listed** with the corresponding **modern-path side
container** (``.../tectum/left/`` and ``.../tectum/right/``
respectively). **Both colliculi are PAIRED, NO-coupling-warning
structures** — the SC (sensorimotor integration) and the IC
(auditory relay) do **not** carry a coupling warning, on either
side. Consumers must **not** conflate the ``right/`` module with the
``left/`` module, and must **not** resolve a left colliculus
through the right path.
**Boundary status (NOT the ``.../tectum/right/`` modern-path side
container — the MODERN PATH is the STRUCTURAL HOME):** **Boundary
case — the ``right/`` module is NOT the ``.../tectum/right/``
modern-path side container.** The **modern-path side container**
(``.../tectum/right/``) is the **structural home** of the two right
colliculi — it is where the **substantive content** lives (or, once
the individual colliculus leaves are written, where the leaf modules
live). This side container (**here**) is the **older-term alias**
path — **the same two leaves**, reachable under a **different
name**. Consumers must **not** conflate the two — the **modern path
is authoritative** for leaf content; the **older-term path is the
synonym alias**.
**Boundary status (INHERITANCE — structure classes, rostrocaudal
anchors, function, lateralization, and clinical associations are
INHERITED from ``tectum/right/`` and the two colliculi leaves):**
**Boundary case — this side container INHERITS the substantive
content of ``tectum/right/`` and the two colliculi leaves.** It does
**not** re-state:
*   **The two structure classes** — **right SC = sensorimotor
    integration / saccade command generator**; **right IC = auditory
    relay**; **both carry NO coupling warning**. These are stated
    in ``.../tectum/`` and in the individual colliculi leaves.
*   **The rostrocaudal anchors** — **right SC at the oculomotor /
    EW / mesV level**; **right IC at the trochlear level**. These
    are stated in ``.../tectum/`` and in the individual colliculi
    leaves.
*   **The saccade hierarchy** — **SC (command) → PPRF / riMLF
    (premotor) → CN III/IV/VI nuclei (motor) → extraocular muscles
    (effector)**. This is stated in ``.../tectum/``.
*   **The auditory relay chain** — **IC (midbrain relay) → MGN
    (thalamic relay) → A1 (auditory cortex)**. This is stated in
    ``.../tectum/``.
*   **The boundary stacks** — SC vs. PPRF / riMLF / CN nuclei /
    LGN / pretectum; IC vs. MGN / lateral lemniscus / SC. These are
    stated in ``.../tectum/`` and in the individual colliculi
    leaves.
*   **The lateralization facts** — SC and IC are **paired
    structures with NO coupling warning**. This is stated in
    ``.../tectum/``.
*   **The clinical associations** — **Parinaud syndrome** (dorsal
    midbrain / quadrigeminal plate lesions), **audiogenic seizures**
    (IC), **saccade deficits** (SC). These are stated in
    ``.../tectum/`` and in the individual colliculi leaves.
Consumers must **not** expect this side container to **re-state**
this content — it is **inherited** from ``tectum/right/`` and the
two colliculi leaves. This side container's **own** contribution is
the **side-scoped synonym framing** and the **cross-listing** —
nothing more. See *Design Contract*.
**Boundary status (NO UNIQUE LEAVES — the two right colliculi are
the SAME two leaves as ``.../tectum/right/``):** **Boundary case —
the two right colliculi under this side container are the SAME TWO
LEAVES as ``.../tectum/right/superior_colliculus/`` and
``.../tectum/right/inferior_colliculus/``.** They are the **same**
**right superior colliculus** (sensorimotor integration) and the
**same** **right inferior colliculus** (auditory relay). This side
container does **not** add new structures. Consumers must **not**
assume the corpora quadrigemina right side contains **different**
colliculi from ``.../tectum/right/`` — it contains the **same two**.
See *The Two Right Bodies* below.
**Boundary status (NOT a new region — the SAME two right colliculi
as ``.../tectum/right/`` under a DIFFERENT NAME):** **Boundary
case — the ``right/`` corpora quadrigemina is NOT a new region.** It
is the **same two right colliculi** as ``.../tectum/right/`` — the
**older name** for the same structures. The distinction in modern
usage is **nominal**: "right superior colliculus" / "right inferior
colliculus" is preferred for the **individual structures**;
"right corpora quadrigemina" (or **"right corpora quadrigemina
anterior"** and **"right corpora quadrigemina posterior"**) is the
**older collective term** for the **two right bodies**. **The two
names describe the same two right colliculi** — consumers must
**not** assume the corpora quadrigemina right side is a **separate
structure** from ``.../tectum/right/``. See *Older-Term Framing*
below.
**Boundary status (NO COUPLING WARNING — the two right colliculi
carry NO coupling warning):** **Boundary case — the two right
colliculi under this side container carry NO coupling warning.**
The **right SC** is a **sensorimotor integration** structure —
**not an oscillator**; the **right IC** is an **auditory relay** —
**not an oscillator**. **Neither carries a coupling warning** —
same rule as motor nuclei, premotor pools, sensor nuclei, relay
nuclei, and conduction pathways. The **pretectum's** bilateral
projection to the EW nuclei (for the consensual pupillary light
reflex) has **no analogue** in the colliculi — the **two right
colliculi** are **independent paired structures** — the right SC
drives **left-or-right** saccade commands via the **tectobulbar
tract** (to the PPRF, riMLF, and CN nuclei **bilaterally**), and
the right IC projects **bilaterally** to the **left and right MGN**
via the **brachium of the inferior colliculus** and to the
**superior colliculus** (for auditory orienting) — **but this
bilateral output is not an intrinsic bilateral coupling** of the
two right colliculi with the two left colliculi. **The two right
colliculi are independent paired structures with NO coupling
warning.** See *Lateralization Notes*.

Overview
--------
The ``right/`` module is the **side-scoped container** for the **two
right bodies of the corpora quadrigemina** — the **right superior
colliculus** and the **right inferior colliculus**. It is a **thin
namespace** — the **substantive content** lives in the **modern-path
leaves** under ``.../tectum/right/``, and is **inherited** from
``tectum/`` and the two colliculi leaves.

**This module is a SIDE CONTAINER, not a leaf.** The **corpora
quadrigemina container** is ``.../tectum/corpora_quadrigemina/``;
this module is the **right side** of that pair. Consumers resolving
this module and expecting a leaf should go one level deeper to the
specific colliculus leaf.

**The two right colliculi are ALSO
``.../tectum/right/<colliculus>/`` leaves.** The two paths are
**equivalent** — the **modern path** is the **structural home**;
the **older-term path** (this side container) is the **synonym
alias**.

**The two right colliculi carry NO coupling warning.** The right SC
is a **sensorimotor integration** structure; the right IC is an
**auditory relay** — neither is an **oscillator**.

**The ``right/`` module is a strict mirror of ``left/``.** The two
are **structurally identical** — same two colliculi on the
respective sides, same **cross-listing** with the corresponding
modern-path side container, same **no coupling warning**. The
mirror is **clean** — the two colliculi are **bilaterally symmetric
paired structures** with **no asymmetric subnuclear or decussation
facts** (unlike the oculomotor's contralateral superior rectus
subnucleus, or the trochlear's pre-exit decussation). The left and
right side containers are **exact mirrors**.

Cross-Listing Statement (side-scoped)
-------------------------------------
Each right colliculus under this side container is **CROSS-LISTED**
with ``.../tectum/right/`` — the same leaf is reachable by **two**
side-scoped paths:

*   **Modern side-scoped path (structural home)** —
    ``midbrain.tectum.right.<colliculus>``
*   **Older-term side-scoped path (synonym alias)** —
    ``midbrain.tectum.corpora_quadrigemina.right.<colliculus>``

**Both resolve to the SAME leaf.** The **modern side-scoped path**
(``.../tectum/right/``) is the **structural home** — the
**older-term side-scoped path** (this side container) is the
**synonym alias**.

**A consumer that resolves the two right colliculi by EITHER path
will be structurally correct** — but a consumer that assumes
``tectum/right/`` and ``tectum/corpora_quadrigemina/right/`` contain
**disjoint** leaf sets will be **wrong** — the **same two right
colliculi** are **shared**, and the **modern path is the
authoritative home**.

The Two Right Bodies
--------------------
The term **"right corpora quadrigemina"** refers to the **two right
bodies** of the four-body tectal plate:

*   **Right superior colliculus** — **right SC** — **sensorimotor
    integration / saccade command generator** — **rostral** — at
    the **oculomotor / EW / mesV level**.
*   **Right inferior colliculus** — **right IC** — **auditory relay**
    — **caudal** — at the **trochlear level**.

**The right superior colliculus** is the **"right corpus
quadrigeminum anterius"** (in older Latin usage). **The right
inferior colliculus** is the **"right corpus quadrigeminum
posterius"** (in older Latin usage). **The "right corpora
quadrigemina"** as a collective term refers to the **two right
bodies together**.

**These two bodies are the SAME two leaves as
``.../tectum/right/``** — nothing is added, nothing is removed,
nothing is changed.

Older-Term Framing
------------------
**"Right corpora quadrigemina"** is the **older collective name**
for the **two right bodies of the tectal plate** — the right
superior colliculus and the right inferior colliculus. Modern
anatomy prefers **"right superior colliculus"** and **"right
inferior colliculus"** for the **individual structures**, and
**"right tectal plate"** or **"right tectum"** for the **right
collective**. The older collective term **remains in use** in the
same clinical, neuroradiological, and historical contexts as the
whole-term **"corpora quadrigemina"** — see the parent container for
the full list.

**The tree preserves the older term** as a **side-scoped synonym
path** under ``.../tectum/corpora_quadrigemina/right/`` — so
consumers who **think in the older terminology** have a
**structural home** for the right two bodies. **The two right
colliculi are the same two leaves** under both names — **nothing
new is added** — the older term is **preserved as an alias**.

Expected Structural Children (prose — the tree is authoritative)
----------------------------------------------------------------
This side container is expected to hold **two leaves** — **the same
two leaves** as ``.../tectum/right/``:

*   **``superior_colliculus/``** — the **right superior colliculus**
    — **cross-listed** from
    ``.../tectum/right/superior_colliculus/`` — the **substantive
    leaf** lives there; this side container's child is the **same
    leaf**, reachable under the older-term path.
*   **``inferior_colliculus/``** — the **right inferior colliculus**
    — **cross-listed** from
    ``.../tectum/right/inferior_colliculus/`` — the **substantive
    leaf** lives there; this side container's child is the **same
    leaf**, reachable under the older-term path.

**These are the SAME TWO LEAVES as ``.../tectum/right/``.** The
right side container does **not** add new structures. The
**substantive content** of each colliculus leaf is the **same**
under both paths — the leaves are **identical**, the paths are
**cross-listed**.

**These are the expected children — the on-disk tree is the
authoritative source.** The **leaves** impose the leaf-level
contract (boundary stacks, function, disorders, lateralization,
references) documented in the **two right colliculi leaf modules**
under ``.../tectum/right/``.

Aggregation Rules (the side container's contract on its children)
-----------------------------------------------------------------
The ``right/`` side container **imposes the following rules** on
every leaf under it. These are **inherited** from the corpora
quadrigemina container and the tectum container, and are
**side-scoped** for the right side:

*   **SIDE CONTAINER, NOT A LEAF.** This module is a **side-scoped
    namespace**. It carries **no substantive leaf-level content**;
    the substantive content lives in the **modern-path leaves**
    under ``.../tectum/right/``.
*   **SYNONYM-CONTAINER DISCIPLINE (SIDE-SCOPED).** The ``right/``
    corpora quadrigemina is the **older-term name** for the **two
    right colliculi**. Its children are the **same two leaves** as
    ``.../tectum/right/`` — **no unique leaves**, **no new
    structures**.
*   **CROSS-LISTING DISCIPLINE (SIDE-SCOPED).** The two right
    colliculi are **cross-listed** between ``.../tectum/right/`` and
    ``.../tectum/corpora_quadrigemina/right/``. **Both paths resolve
    to the SAME TWO LEAVES.** Consumers should resolve by **one**
    path per lookup — enumerating **both** paths yields
    **duplicates**.
*   **INHERITANCE FROM ``tectum/right/``.** The **structure classes**
    (right SC = sensorimotor integration; right IC = auditory relay;
    both no coupling warning), the **rostrocaudal anchors** (right
    SC at CN III level; right IC at CN IV level), the **saccade
    hierarchy**, the **auditory relay chain**, the **boundary
    stacks**, the **lateralization facts**, and the **clinical
    associations** are **inherited from ``tectum/right/`` and the
    two colliculi leaves**. This side container does **not**
    re-state them.
*   **NO NEW FUNCTIONAL CLAIMS.** The ``right/`` corpora
    quadrigemina container makes **no new functional claims** —
    every function belongs to a **child** (right SC: saccade command
    generation; right IC: auditory relay), and every function is
    **inherited** from the corresponding **colliculus leaf**.
*   **NO COUPLING WARNING.** The two right colliculi carry **NO
    coupling warning** — same rule as every non-oscillator class.
    Consumers must **not** import a **coupling warning** into the
    right side container.
*   **MIRROR PARITY WITH ``left/``.** The ``right/`` side container
    is a **strict mirror** of ``left/`` — same two colliculi on
    the respective sides, same **cross-listing** with the
    corresponding modern-path side container, same **no coupling
    warning**. The mirror is **clean** — the two colliculi are
    **bilaterally symmetric paired structures** with **no
    asymmetric subnuclear or decussation facts**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only — **no** import
    from ``.../left/``.
*   **No cross-lobe imports.** This module does **not** import from
    the **pretectum**, the **tegmentum**, the **CN nuclei**,
    the **PPRF**, the **riMLF**, the **lateral lemniscus**, the
    **brachia of the colliculi**, the **thalamic relays** (LGN,
    MGN), or any other container. The right colliculi's
    relationships to the **pretectum**, the **tegmentum**, the
    **CN nuclei**, the **PPRF**, the **riMLF**, the **lateral
    lemniscus**, the **brachia of the colliculi**, and the
    **thalamic relays** are documented as **prose and boundary
    data** in ``tectum/`` and the two colliculi leaves — **not
    re-stated here**.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **transmitter
    phenotypes** of the collicular neurons are
    ``chemicals_hormones``-layer facts — documented as **prose** in
    the two colliculi leaves, **never imported**.
*   **SIDE CONTAINER — not a leaf.** The substantive content lives
    in the **modern-path leaves** under ``.../tectum/right/``.
    Consumers resolving ``.../corpora_quadrigemina/right`` and
    expecting a leaf should go one level deeper.
*   **SYNONYM-CONTAINER DISCIPLINE.** The ``right/`` corpora
    quadrigemina is the **older-term name** for the **two right
    colliculi**. Its children are the **same two leaves** as
    ``.../tectum/right/``.
*   **CROSS-LISTING via ``AREA_PATHS``.** The two right colliculi are
    cross-listed between ``.../tectum/right/`` and
    ``.../tectum/corpora_quadrigemina/right/``. **Both paths resolve
    to the SAME TWO LEAVES.** Consumers resolve by **one** path per
    lookup.
*   **INHERITANCE from ``tectum/right/``.** The substantive content
    is inherited. This side container's **own** contribution is the
    **side-scoped synonym framing** and the **cross-listing**.
*   **NO UNIQUE LEAVES.** The two leaves under the right corpora
    quadrigemina are the **same two leaves** as under
    ``.../tectum/right/``.
*   **NO NEW FUNCTIONAL CLAIMS.** Every function belongs to a
    **child** (right SC or right IC), and every function is
    **inherited** from the corresponding **colliculus leaf**.
*   **NO COUPLING WARNING.** The two right colliculi carry **NO
    coupling warning** — same rule as every non-oscillator class.
*   **MIRROR PARITY with ``left/`` — strict mirror, NO warning.**
    The mirror is **clean** — the two colliculi are **bilaterally
    symmetric paired structures** with **no asymmetric subnuclear
    or decussation facts**.
*   **The on-disk tree is authoritative.** If the tree has **both**
    ``tectum/right/`` **and**
    ``tectum/corpora_quadrigemina/right/``, then the two right
    colliculi are reachable by **either** path. If the tree has
    **only** ``tectum/corpora_quadrigemina/right/``, then that is
    the **sole** path — but the two leaves are still the **same two
    colliculi**.
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the tectum** (``tectum/right`` ↔
    ``tectum/corpora_quadrigemina/right``) — not into the forebrain
    or hindbrain.
*   **No nested cross-listing.** The right corpora quadrigemina is a
    **single side-scoped synonym container**. It is **not** a
    container of containers — its children are the **same two
    colliculi** as ``tectum/right/``.

Usage
-----
Resolve the side container by path::

    from infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina import right

Resolve a right leaf by **either** side-scoped path (they are
equivalent)::

    # Modern side-scoped path (structural home):
    from infrastructure.brainparts.midbrain.tectum.right import superior_colliculus

    # Older-term side-scoped path (synonym alias — resolves to the SAME leaf):
    from infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.right import superior_colliculus

Or by fully-qualified path string (leaves, not the side container)::

    modern_right_sc_path = (
        "midbrain.tectum.right.superior_colliculus"
    )
    older_term_right_sc_path = (
        "midbrain.tectum.corpora_quadrigemina.right.superior_colliculus"
    )
    # Both resolve to the SAME leaf.

**Do not** assume the ``right/`` module is a **leaf**. It is a
**side-scoped container** — the substantive content (structure
classes, rostrocaudal anchors, boundary stacks, function, disorders,
lateralization, references) lives in the **modern-path leaves**
under ``.../tectum/right/``. Go one level deeper.

**Do not** assume the ``right/`` module is the
**``corpora_quadrigemina/`` container**. It is the **right side** of
that pair. The corpora quadrigemina container holds **both**
``left/`` and ``right/``.

**Do not** assume the ``right/`` module and ``.../tectum/right/``
contain **disjoint** leaf sets. The **two right colliculi** are
**shared**, and the **modern path is the authoritative home**.

**Do not** assume the ``right/`` module is a **new region**. It is
the **older collective name** for the **two right bodies of the
tectal plate** — the **same two leaves** as
``.../tectum/right/superior_colliculus/`` and
``.../tectum/right/inferior_colliculus/``.

**Do not** resolve the two right colliculi by **both** paths in a
single lookup. Use **one** path — the modern path
(``tectum/right/superior_colliculus``) or the older-term path
(``tectum/corpora_quadrigemina/right/superior_colliculus``).
Enumerating **both** paths yields **duplicates**.

**Do not** conflate the ``right/`` module with the ``left/``
module. The two side containers hold the **two colliculi on their
respective sides** — the **right two bodies** (right SC + right IC)
here, and the **left two bodies** (left SC + left IC) there.
**They are strictly mirrored** — and the mirror is **clean** (no
asymmetric subnuclear or decussation facts).

**Do not** import a **coupling warning** into the right corpora
quadrigemina. The **two right colliculi carry NO coupling warning**
— same rule as every non-oscillator class. The **right SC** is a
**sensorimotor integration** structure; the **right IC** is an
**auditory relay** — neither is an **oscillator**.

Iterating the ``right/`` side container's children (recommended
consumer pattern — NOTE cross-listing)::

    import pkgutil
    import infrastructure.brainparts.midbrain.tectum.corpora_quadrigemina.right as cq_right_pkg

    CQ_RIGHT_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(cq_right_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("superior_colliculus", "inferior_colliculus")
    #
    # These are the SAME TWO LEAVES as .../tectum/right/. Enumerating
    # BOTH paths yields DUPLICATES. Use ONE path per lookup.

Reaching the modern-path side container (recommended consumer
pattern — the STRUCTURAL HOME)::

    # The modern-path side container is the STRUCTURAL HOME of the
    # two right colliculi — the substantive content lives there:
    #
    #   brainparts.midbrain.tectum.right
    #
    # The right/ corpora quadrigemina is the OLDER-TERM ALIAS —
    # the same two leaves, reachable under a different name.

Reaching the ``left/`` side container (recommended consumer pattern
— the SIDE mirror)::

    # The left/ side container holds the two left colliculi:
    #
    #   brainparts.midbrain.tectum.corpora_quadrigemina.left
    #
    # The two side containers are STRICTLY MIRRORED — each holds the
    # two colliculi on its side, same cross-listing structure, same
    # no coupling warning. The mirror is CLEAN — the two colliculi
    # are bilaterally symmetric paired structures with no asymmetric
    # subnuclear or decussation facts.

Reaching the ``corpora_quadrigemina/`` container (recommended
consumer pattern — the PAIR parent)::

    # The corpora_quadrigemina/ container holds BOTH the left/ and
    # right/ side containers:
    #
    #   brainparts.midbrain.tectum.corpora_quadrigemina
    #
    # The right/ is the RIGHT SIDE of that pair.

Reaching the ``tectum/`` container (recommended consumer pattern —
the REGION parent)::

    # The tectum/ container holds the modern-path side containers
    # (left/, right/) AND the corpora_quadrigemina/ synonym container:
    #
    #   brainparts.midbrain.tectum
    #
    # The two right colliculi are reachable by BOTH the modern-path
    # (tectum/right/) and the older-term path
    # (tectum/corpora_quadrigemina/right/).

Bilateral iteration (recommended consumer pattern — NOTE the
cross-listing and the no-coupling-warning rule)::

    for side in ("left", "right"):
        for colliculus in (
            "superior_colliculus",
            "inferior_colliculus",
        ):
            # Either path resolves to the same leaf — use ONE:
            modern_path = (
                f"midbrain.tectum.{side}.{colliculus}"
            )
            older_term_path = (
                f"midbrain.tectum.corpora_quadrigemina."
                f"{side}.{colliculus}"
            )
            # Both resolve to the SAME leaf.
            #
            # NOTE: the four colliculi carry NO coupling warning —
            # same rule as every non-oscillator class. The
            # corpora_quadrigemina/right/ is the OLDER NAME for the
            # same two right colliculi as .../tectum/right/.

References
----------
*   **See the ``tectum/`` container's References section** for the
    canonical tectum anatomy, the SC / IC functional literature, the
    saccade hierarchy, the auditory relay chain, and the clinical
    associations (Sparks, Stein & Stanford, Ehret & Romand,
    Kahle & Frotscher, Parinaud, Newton & Potts).
*   **See the individual right colliculus leaf modules**
    (``.../tectum/right/superior_colliculus/`` and
    ``.../tectum/right/inferior_colliculus/``) for the substantive,
    laterality-specific references.
*   **Canonical tectum anatomy (including the corpora quadrigemina
    terminology):** Brodal, A. (2010). *The Central Nervous System:
    Structure and Function*, 4th ed. (The tectum as the dorsal
    midbrain; the corpora quadrigemina as the four colliculi —
    superior + inferior, left + right; the side-scoped older-term
    framing "right corpora quadrigemina" / "left corpora
    quadrigemina".)
*   **Corpora quadrigemina — historical framing:** Kahle, W.,
    Frotscher, M. (2003). *Color Atlas of Human Anatomy, Vol. 3:
    Nervous System and Sensory Organs*, 5th ed. (The corpora
    quadrigemina as the older term for the four colliculi — the
    left and right side-scoped framing, and the "corpora
    quadrigemina anterior" / "posterior" Latin usage.)
*   **Quadrigeminal plate — clinical usage:** Parinaud, H. (1883).
    "Paralysie des mouvements associés des yeux." *Annales
    d'Oculistique* 90:1–21. (The "quadrigeminal plate syndrome" —
    Parinaud syndrome — the term "quadrigeminal plate" remains in
    clinical use for the tectum; the left/right side-scoped
    framing is preserved in the older clinical literature.)
*   **SLEA (contrast — the right corpora quadrigemina is not
    SLEA):** Alheid, G.F., Heimer, L. (1988). "New perspectives in
    basal forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the right corpora quadrigemina.)
*   NeuroNames — Corpora quadrigemina (right); Superior colliculus
    (right); Inferior colliculus (right); FMA — Corpora
    quadrigemina (right); Superior colliculus (right); Inferior
    colliculus (right).
"""