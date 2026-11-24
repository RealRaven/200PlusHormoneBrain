"""
infrastructure.brainparts.midbrain.tegmentum.caudal_linear_nucleus.left
======================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        └── caudal_linear_nucleus
            ├── (anatomical content — the MIDLINE LEAF)
            ├── left                   <-- THIS MODULE (TREE-STRUCTURAL
            │                               side container — NOT an
            │                               anatomical pair)
            └── right

**Primary synonym:** Left caudal linear nucleus — **only in the sense
of a tree-structural side container.** The caudal linear nucleus is
a **midline raphe nucleus** — it has **no left/right pair**
anatomically. See *Structural Tension*.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). The caudal linear nucleus is a **midline**
**serotonergic and dopaminergic** nucleus in the **ventral midbrain
tegmentum**, at the level of the **inferior colliculus**. **The
`left/` module is not a distinct anatomical structure** — it is a
**tree-structural side container** for a **midline leaf**. See
*Structural Tension*.
**Container status:** **This module is a TREE-STRUCTURAL
SIDE CONTAINER, not an anatomical leaf.** It exists because the
on-disk tree represents the caudal linear nucleus as a container
with `left/` and `right/` children — a **tree-consistency**
artifact for a nucleus that is **anatomically midline**. The
**substantive anatomical content** of the caudal linear nucleus
lives in the **midline leaf** at ``.../caudal_linear_nucleus/``.
This `left/` module **delegates** to that midline leaf — it
**re-states nothing**, **adds no anatomical claims**, and **does
not imply the CLi has a left/right pair**. See *Structural
Tension*, *Delegation to the Midline Leaf*, and *Design Contract*.
**Part of:** The **caudal_linear_nucleus** container (the
tree-structural container for the midline CLi) — as the **left**
side **tree-structural** child.
**Structural parent:** ``.../caudal_linear_nucleus/`` → **direct
child** of the tree-structural CLi container.
**Structural children:** **None.** This is a **thin side
container** — it does not hold leaf children. Its substantive
content is **delegated** to the midline leaf.
**Structural tension (LIVE ANOMALY — the CLi is anatomically MIDLINE
and has NO left/right pair):** **This is the primary structural
fact of the module, and it is a LIVE ANOMALY in the tree.**
*   **The CLi is a MIDLINE nucleus.** It is a **raphe nucleus** — a
    midline serotonergic and dopaminergic nucleus of the rostral
    raphe complex. It **modulates both sides** via its **distributed
    projections**, **not** via intrinsic left-right coupling. **The
    midline position is the structural expression of its modulatory
    function.** See ``.../caudal_linear_nucleus/`` for the full
    anatomical leaf — the midline position, the modulatory class,
    the subpopulations, the ascending serotonergic system, and the
    clinical associations.
*   **The `left/` module is a TREE-STRUCTURAL side container.** It
    exists **only because** the on-disk tree represents the CLi as
    a container with `left/` and `right/` children. **It is a
    tree-consistency artifact** — a generic tree structure applied
    uniformly to the tegmentum's nuclei, **including the one
    nucleus that is anatomically midline**. **It is NOT an
    anatomical left/right pair.**
*   **The midline leaf is the anatomical home.** The substantive
    anatomical content — the CLi as a **midline modulatory
    nucleus** — lives in the midline leaf at
    ``.../caudal_linear_nucleus/``. **This `left/` module
    delegates to it** — it does not duplicate, re-state, or
    re-frame the anatomical content. Consumers seeking
    substantive CLi content should resolve the **midline leaf**.
*   **Consumers must NOT assume the CLi has a left/right pair
    anatomically** — it does **not**. The CLi is **one midline
    nucleus**. The `left/` module is a **tree-structural**
    construct — a **side container** for a nucleus that has **no
    side**.
*   **Resolution A** (this module's implementation): the `left/` and
    `right/` modules are **thin, delegating** side containers that
    point at the midline leaf and explicitly state that the paired
    tree structure is a **tree-consistency artifact**, not an
    anatomical claim. **The midline leaf's content is authoritative
    for the CLi's anatomy.**
*   **Resolution B** (cleanest): the tree should **remove** the
    `left/` and `right/` nodes under `caudal_linear_nucleus/`. The
    CLi would then be a **single midline leaf** — consistent with
    its anatomy, and consistent with the CLi leaf's own
    `Bilateral iteration — NOT APPLICABLE` block, which **explicitly
    says** that writing `for side in ("left", "right"): path =
    f"midbrain.tegmentum.{side}.caudal_linear_nucleus"` is
    **WRONG**.
*   **The amendment is a follow-up.** The tegmentum container's
    **paired-leaf rule** and the midbrain container's **PAG prose**
    both need **amendment** to permit **midline leaves** — the CLi
    leaf already flagged this. This `left/` module **reinforces**
    the flag: **the tree has at least one midline nucleus
    represented as paired** — the CLi — and the tree should be
    **amended** to represent it as **midline** (Resolution B), or
    the midline leaf should be **amended** to acknowledge the tree
    represents it as **paired** (Resolution A, this module's
    implementation). See *Design Contract* — *Live amendment*.

Delegation to the Midline Leaf
------------------------------
The substantive anatomical content of the caudal linear nucleus —
**including its midline position, its modulatory class, its
serotonergic and dopaminergic subpopulations, its place in the
rostral raphe complex, its place in the ascending serotonergic
system, and its clinical associations** — is **entirely** in the
**midline leaf** at ``.../caudal_linear_nucleus/``. **This `left/`
module adds nothing to it.**

The midline leaf covers:
*   **The midline position** — the structural expression of the
    modulatory function; the raphe nucleus anatomy; the distributed
    projections that reach both sides.
*   **The neuromodulatory class** — the same class as the locus
    coeruleus, the dorsal raphe, the median raphe, and the VTA.
*   **The serotonergic and dopaminergic subpopulations** — the
    majority serotonergic subpopulation and the A10 dopaminergic
    subset.
*   **The rostral raphe complex context** — the CLi as a smaller
    ascending raphe nucleus, alongside the dorsal raphe, the
    median raphe, and the rostral linear nucleus.
*   **The clinical associations** — indirect, shared with the
    larger serotonergic and dopaminergic nuclei (the DR, the MnR,
    the VTA).
*   **The full boundary stack** — the CLi vs. the DR, the MnR, the
    RLi, the VTA, the SN, the PAG, the medullary raphe nuclei, and
    the cerebral aqueduct.
*   **The full reference list** — the human raphe anatomy, the
    serotonergic system, the caudal linear nucleus's serotonergic
    and dopaminergic subpopulations, and the contrast references.

**Consumers should resolve the CLi's anatomical content by the
MIDLINE LEAF**, not by this `left/` module.

Function in the Human Brain
---------------------------
**See the midline leaf** at ``.../caudal_linear_nucleus/`` for the
substantive function of the caudal linear nucleus. **This `left/`
module has no function of its own** — the CLi is a **midline**
nucleus, and the "left" of a midline nucleus is a **tree-structural
abstraction**, not an anatomical side. The CLi's modulatory function
— the serotonergic and dopaminergic modulation of its targets via
distributed projections — is documented **once**, in the midline
leaf.

Associated Disorders
--------------------
**See the midline leaf** at ``.../caudal_linear_nucleus/`` for the
substantive clinical associations of the caudal linear nucleus —
mood disorders, addiction, sleep and circadian regulation, and
descending pain modulation — all **indirect** and **shared** with
the larger serotonergic and dopaminergic nuclei (the DR, the MnR,
the VTA). **This `left/` module has no clinical associations of
its own** — the CLi is a **midline** nucleus, and the "left" of a
midline nucleus is a **tree-structural abstraction**.

Lateralization Notes
--------------------
**There is no lateralization for a midline nucleus.** The caudal
linear nucleus is **midline** — it has **no left/right pair**
anatomically, and its "left" is a **tree-structural abstraction**,
not an anatomical side. **The CLi modulates both sides** via its
**distributed projections** — it has no **left-vs-right
functional distinction** of its own.

*   **NO pairing — the CLi is one midline nucleus.** The `left/`
    module is a **tree-structural** side container for a nucleus
    that is anatomically midline. **It does not imply the CLi has a
    left/right pair anatomically.**
*   **NO lateralization — the CLi's function is distributed
    bilaterally.** The CLi's **serotonergic** and **dopaminergic**
    projections reach **both sides** via their **distributed
    targets** — **the CLi is a midline modulator**, not a
    lateralized structure.
*   **NO coupling warning — the CLi is a modulatory nucleus.** The
    **midline position** is **not a coupling hazard** — there are
    **no "two sides" to couple** (the CLi is one midline nucleus).
    **Neuromodulatory nuclei carry NO coupling warning** — same
    rule as every non-oscillator class.
*   **NO SLEA warning, NO amygdala-lateralization warning, NO
    rhinencephalon-exclusion flag** — the CLi is not an
    extended-amygdala component, not part of the amygdala, and not
    a rhinencephalon structure.

**Consumers must NOT assume "left CLi = right CLi"** — there is no
**left CLi** and **no right CLi** anatomically. The CLi is **one
midline nucleus**, and its "left" and "right" (in the tree) are
**tree-structural** abstractions, not anatomical sides.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** This `left/` module is a
    **tree-structural** side container — it does **not** import
    from `.../right/` (the CLi is **midline** — there is no
    anatomical right side to import from).
*   **No cross-lobe imports.** This module does **not** import from
    the **PAG**, the **VTA**, the **substantia nigra**, the
    **dorsal raphe**, the **median raphe**, the **rostral linear
    nucleus**, the **medullary raphe nuclei**, the **cerebral
    aqueduct**, or any other container. **The CLi's relationships
    to these structures are documented in the MIDLINE LEAF** — not
    re-stated here.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **serotonergic** and **dopaminergic** phenotypes are
    ``chemicals_hormones``-layer facts — documented in the
    **midline leaf**, **not** here.
*   **TREE-STRUCTURAL SIDE CONTAINER — NOT an anatomical pair.**
    This module is a **thin** side container for a **midline**
    nucleus. It **delegates** to the midline leaf at
    ``.../caudal_linear_nucleus/``. It **does not** carry
    substantive anatomical content, **does not** duplicate the
    midline leaf's boundary stacks, function, disorders,
    lateralization, or references, and **does not** imply the CLi
    has a left/right pair anatomically.
*   **DELEGATION — the midline leaf is authoritative for the CLi's
    anatomy.** Consumers seeking substantive CLi content should
    resolve the **midline leaf** at ``.../caudal_linear_nucleus/``.
    **This `left/` module re-states nothing and adds no anatomical
    claims.**
*   **LIVE ANOMALY — the tree represents a MIDLINE nucleus as
    PAIRED.** This is a **live structural anomaly** in the tree —
    the CLi is anatomically midline, but the tree has
    `caudal_linear_nucleus/left/` and `caudal_linear_nucleus/right/`
    nodes. The **midline leaf** already flagged this in its
    `Bilateral iteration — NOT APPLICABLE` block. **This `left/`
    module reinforces the flag.** The anomaly should be **resolved**
    — either by **removing** the `left/` and `right/` nodes
    (Resolution B), or by **amending** the midline leaf to
    acknowledge the tree's paired representation (Resolution A,
    this module's implementation).
*   **LIVE AMENDMENT — the tegmentum container's paired-leaf rule
    should be amended to permit midline leaves.** The tegmentum
    container's aggregation rule — *"each tegmentum nucleus is a
    paired structure (a ``left/`` leaf and a ``right/`` leaf)"* —
    should be **amended** to state that **midline nuclei are
    permitted** as **direct children** of ``tegmentum/`` — **not
    required** to be under ``left/`` or ``right/``. The **CLi
    leaf** flagged this; **this `left/` module reinforces the
    flag**.
*   **LIVE AMENDMENT — the midbrain container's PAG prose and the
    tegmentum container's paired-leaf rule should be reconciled.**
    The midbrain container said "the cerebral aqueduct and the
    periaqueductal gray are midline structures, not paired"; the
    tegmentum container said "the PAG is midline-adjacent but is
    treated as paired in the tree". **These statements contradict
    each other.** The **CLi is a clean new data point** — the
    tegmentum container **has at least one midline nucleus
    represented in the tree** — and the tree should be **amended**
    to reflect the midline facts consistently.
*   **NO coupling warning.** The CLi is a **modulatory nucleus** —
    **neuromodulatory nuclei carry NO coupling warning**. This
    `left/` module **inherits** that — no coupling warning is
    imported here.
*   **NOT a CN nucleus.** The CLi is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. This `left/` module **inherits**
    that — no cross-listing is imported here.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** No cross-listing.
*   **No nested cross-listing.** This `left/` module is a **thin
    side container** — it has **no leaf children**, and its
    substantive content is **delegated** to the midline leaf.
*   **The on-disk tree is authoritative.** If the tree has
    `caudal_linear_nucleus/left/` and `caudal_linear_nucleus/right/`,
    the **tree-structural** representation is authoritative **as a
    tree fact** — but the **anatomical fact** is that the CLi is
    **midline**. **The midline leaf is authoritative for the CLi's
    anatomy; the `left/` and `right/` nodes are tree-structural
    artifacts.**

Usage
-----
Resolve the `left/` tree-structural side container by path::

    from infrastructure.brainparts.midbrain.tegmentum.caudal_linear_nucleus import left

**Resolve substantive CLi content by the MIDLINE LEAF** — not by
this `left/` module::

    from infrastructure.brainparts.midbrain.tegmentum import caudal_linear_nucleus

Or by fully-qualified path string (midline leaf — the anatomical
home)::

    midline_path = "midbrain.tegmentum.caudal_linear_nucleus"
    # The MIDLINE LEAF — the anatomical home of the CLi.
    # Substantive content: midline position, modulatory class,
    # serotonergic and dopaminergic subpopulations, rostral raphe
    # complex context, clinical associations, full boundary stack,
    # full references.

**Do not** assume the CLi has a **left/right pair** anatomically.
It is a **midline raphe nucleus** — it has **no left/right pair**.
**This `left/` module is a tree-structural side container** — a
**tree-consistency** artifact for a nucleus that is anatomically
midline. See the midline leaf's
`Bilateral iteration — NOT APPLICABLE` block — which **explicitly
says** that writing `for side in ("left", "right"): path =
f"midbrain.tegmentum.{side}.caudal_linear_nucleus"` is **WRONG**.

**Do not** resolve the CLi's anatomical content by this `left/`
module — **resolve the midline leaf** at
``.../caudal_linear_nucleus/``. The `left/` module **delegates**
to the midline leaf.

**Do not** assume the `left/` module's `__init__.py` carries
substantive content — it **does not**. The substantive content is
in the **midline leaf**. This `left/` module is a **thin side
container**.

**Do not** import a **coupling warning** into this `left/` module —
the CLi is a **modulatory nucleus**, and **neuromodulatory nuclei
carry NO coupling warning**.

**Do not** import the **serotonergic** or **dopaminergic**
phenotypes into this `left/` module — they are
``chemicals_hormones``-layer facts, documented in the **midline
leaf**, **not** here.

**Do not** assume this `left/` module is a **CN nucleus** — the
CLi is **not** a cranial nerve nucleus and is **NOT** cross-listed
with ``cranial_nerve_nuclei/``.

**The structural tension should be resolved** — either by
**removing** the `left/` and `right/` nodes (Resolution B), or by
**amending** the midline leaf to acknowledge the tree's paired
representation (Resolution A, this module's implementation). The
**tegmentum container's paired-leaf rule** and the **midbrain
container's PAG prose** should also be **amended** to accommodate
midline leaves. See *Design Contract* — *Live amendment*.

Iterating the `left/` tree-structural side container's children
(recommended consumer pattern)::

    CAUDAL_LINEAR_NUCLEUS_LEFT_CHILDREN = ()
    # The left/ module is a THIN tree-structural side container. It
    # has NO leaf children. Its substantive content is DELEGATED to
    # the midline leaf at .../caudal_linear_nucleus/.

Resolving substantive CLi content (recommended consumer pattern)::

    # The MIDLINE LEAF is the anatomical home of the CLi:
    #
    #   brainparts.midbrain.tegmentum.caudal_linear_nucleus
    #
    # It carries: the midline position, the modulatory class, the
    # serotonergic and dopaminergic subpopulations, the rostral
    # raphe complex context, the ascending serotonergic system
    # context, the clinical associations, the full boundary stack,
    # and the full reference list.
    #
    # Do NOT resolve substantive CLi content from this left/ module
    # — the left/ module is a tree-structural side container, not
    # an anatomical leaf.

The structural tension — options (not wired — structural decision)::

    # The tree represents the caudal linear nucleus as a container
    # with left/ and right/ children — a TREE-STRUCTURAL artifact
    # for a nucleus that is anatomically MIDLINE. There are two
    # resolutions:
    #
    #   RESOLUTION A (this module's implementation):
    #     The left/ and right/ modules are THIN, DELEGATING side
    #     containers that point at the midline leaf and explicitly
    #     state that the paired tree structure is a TREE-CONSISTENCY
    #     artifact, not an anatomical claim. The midline leaf's
    #     content is authoritative for the CLi's anatomy.
    #
    #   RESOLUTION B (cleanest):
    #     Remove the left/ and right/ nodes from the tree. The CLi
    #     is a single midline leaf — consistent with its anatomy,
    #     and consistent with the CLi leaf's own
    #     'Bilateral iteration — NOT APPLICABLE' block, which
    #     explicitly says that writing
    #     `for side in ("left", "right"): path =
    #      f"midbrain.tegmentum.{side}.caudal_linear_nucleus"`
    #     is WRONG.
    #
    # Either resolution is valid. The tree should NOT continue to
    # represent the CLi as paired WITHOUT the explicit delegation
    # and anomaly flag in the left/ and right/ modules — otherwise
    # the tree would be making an anatomical claim (that the CLi
    # has a left/right pair) that contradicts the midline anatomy.

References
----------
*   **See the midline leaf** at ``.../caudal_linear_nucleus/`` for
    the full reference list — the human raphe anatomy (Hornung,
    2003), the serotonergic system (Jacobs & Azmitia, 1992), the
    rostral raphe complex ascending projections (Azmitia & Segal,
    1978), the caudal linear nucleus's serotonergic cells
    (Halliday & Törk, 1989; Baker et al., 1991), the A10
    dopaminergic cell group (Dahlstroem & Fuxe, 1964), the
    monoamine cell groups (Hökfelt et al., 1984), the raphe nuclei
    anatomy (Törk, 1990), the serotonin receptors (Pazos &
    Palacios, 1985), the raphe magnus descending pain modulation
    (contrast; Fields & Basbaum, 1978), the dorsal raphe (contrast;
    Michelsen et al., 2007), the median raphe (contrast; Vertes &
    Crane, 1997), and the SLEA contrast (Alheid & Heimer, 1988).
*   **This `left/` module has no substantive references of its
    own** — it is a **tree-structural side container** for a
    **midline** nucleus. The **midline leaf** carries the
    substantive references.
*   NeuroNames — Caudal linear nucleus; FMA — Caudal linear
    nucleus. **There is no "left caudal linear nucleus" or "right
    caudal linear nucleus"** in the standard anatomical atlases
    — the CLi is a **single midline nucleus**.
"""