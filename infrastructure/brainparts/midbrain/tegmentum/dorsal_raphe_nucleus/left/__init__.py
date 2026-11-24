"""
infrastructure.brainparts.midbrain.tegmentum.dorsal_raphe_nucleus.left
=====================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        ├── caudal_linear_nucleus
        │   ├── (midline leaf)
        │   ├── left               (anomalous)
        │   └── right              (anomalous)
        └── dorsal_raphe_nucleus
            ├── (MIDLINE LEAF — the DR leaf, written ASSUMING
            │   the tree represents the DR cleanly with NO left/
            │   or right/ nodes)
            ├── left               <-- THIS MODULE (TREE-STRUCTURAL
            │                           side container — FALSIFIES
            │                           the DR leaf's clean-case
            │                           assumption)
            └── right

**Primary synonym:** Left dorsal raphe nucleus — **only in the sense
of a tree-structural side container.** The dorsal raphe nucleus is a
**midline serotonergic nucleus** — it has **no left/right pair**
anatomically. See *Structural Tension — the Falsified Clean-Case
Assumption*.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). The dorsal raphe nucleus is a **midline serotonergic
nucleus** in the **ventral midbrain tegmentum**, at the level of the
**superior colliculus**. **The `left/` module is not a distinct
anatomical structure** — it is a **tree-structural side container**
for a **midline leaf**. See *Structural Tension*.
**Container status:** **This module is a TREE-STRUCTURAL
SIDE CONTAINER, not an anatomical leaf.** It exists because the
on-disk tree represents the dorsal raphe nucleus as a container
with `left/` and `right/` children — a **tree-consistency**
artifact for a nucleus that is **anatomically midline**. **This
module is structurally identical to the caudal linear nucleus's
``left/`` module** — the same pattern, the same anomaly, the same
delegation — **but the DR's `left/` also has a second structural
job**: it must **acknowledge and flag** that the DR leaf **was
written assuming the tree represents the DR cleanly** — with **no
`left/` or `right/` nodes** — and that **this assumption is now
FALSE** given the on-disk tree. See *Structural Tension*, *The
Falsified Clean-Case Assumption*, and *Design Contract*.
**Part of:** The **dorsal_raphe_nucleus** container (the
tree-structural container for the midline DR) — as the **left**
side **tree-structural** child.
**Structural parent:** ``.../dorsal_raphe_nucleus/`` → **direct
child** of the tree-structural DR container.
**Structural children:** **None.** This is a **thin side
container** — it does not hold leaf children. Its substantive
content is **delegated** to the midline leaf.
**Structural tension (LIVE ANOMALY — the DR is anatomically MIDLINE
and has NO left/right pair):** **The DR is a MIDLINE nucleus.** It
is a **raphe nucleus** — a midline serotonergic nucleus of the
rostral raphe complex. It **modulates both sides** via its
**distributed projections**, **not** via intrinsic left-right
coupling. **The midline position is the structural expression of
its modulatory function.** **The `left/` module is a
TREE-STRUCTURAL side container** — it exists **only because** the
on-disk tree represents the DR as a container with `left/` and
`right/` children. **It is NOT an anatomical left/right pair.**
Consumers must **not** assume the DR has a left/right pair
anatomically — it **does not**. See *The Falsified Clean-Case
Assumption* for **why this anomaly is more serious than the CLi's**.
**Structural tension — THE FALSIFIED CLEAN-CASE ASSUMPTION (why this
anomaly is MORE SERIOUS than the CLi's):** **The DR leaf was written
on a specific assumption about the on-disk tree — and that
assumption is now FALSE.**
*   **What the DR leaf assumed:** The DR leaf **explicitly stated**
    that *"the tree represents it [the DR] **cleanly** — one
    midline leaf under ``tegmentum/``, **no `left/` or `right/`
    nodes**"* — and **used the DR's clean representation as the
    PROOF CASE** that the tree **can** represent midline nuclei
    cleanly, **and as the MODEL** that the CLi's anomalous
    representation should follow (Resolution B — remove the CLi's
    `left/` and `right/` nodes).
*   **What the on-disk tree actually has:** The on-disk tree has
    ``.../dorsal_raphe_nucleus/left/`` (this module) and
    ``.../dorsal_raphe_nucleus/right/`` — **tree-structural side
    containers** that **contradict** the DR leaf's clean-case
    assumption. **The DR leaf said those paths "do not exist" —
    they exist.** **The DR leaf said the tree represents the DR
    cleanly — it does not.**
*   **What this means for the DR leaf's proof-case role:** The DR
    **can no longer serve as the proof case** that the tree can
    represent midline nuclei cleanly — because the DR itself is
    **now represented as paired**, exactly like the CLi.
    **The CLi was the anomalous case; the DR was the proof case;
    now BOTH are anomalous.** The tree **cannot** be pointed to as
    evidence that midline nuclei are represented cleanly — **none
    are**.
*   **What needs to happen:** There are two resolutions, and one of
    them is **urgent**:
    *   **Resolution B (recommended — restore the clean case):**
        **Remove** the ``dorsal_raphe_nucleus/left/`` and
        ``dorsal_raphe_nucleus/right/`` nodes from the tree. The
        DR becomes a **single midline leaf**, as the DR leaf
        **assumed it was**. **This restores the DR leaf's clean-
        case framing** — the DR is again the proof case, and the
        CLi amendment (Resolution B for the CLi) **retains its
        model**. **This module and the ``right/`` module would be
        deleted**, and the DR leaf's claim would be **true again**.
    *   **Resolution A (this module's implementation — amend the
        DR leaf):** Keep the ``left/`` and ``right/`` nodes, and
        **amend the DR leaf** to **acknowledge** that the tree
        represents the DR as paired (contradicting its earlier
        clean-case framing). **The DR leaf's "proof case" and
        "model" framing must be amended** — the DR is no longer
        the proof case; **both the DR and the CLi are anomalous**;
        the **proposed amendment to the CLi is still valid on its
        own merits** (the CLi is midline, and the tree **should**
        represent it cleanly), **but the DR no longer provides
        independent evidence that the tree already does this**.
*   **The amendment is URGENT.** The DR leaf's clean-case framing
    is **explicit** — it is in the `Boundary status (MIDLINE LEAF
    — CLEANLY REPRESENTED)` section, the `The Cleanest Midline
    Leaf in the Tree` section, the `Overview`, the `Lateralization
    Notes`, the `Design Contract`, and the `Usage` `Do not` block.
    **All of those sections claim the tree represents the DR
    cleanly.** **The on-disk tree does not.** **The DR leaf must be
    amended** — either by Resolution B (removing the nodes,
    restoring the clean case) **or** by Resolution A (updating
    the DR leaf's prose to acknowledge the paired representation).
    **Until it is amended, the DR leaf contains a claim that
    contradicts the on-disk tree.**
*   **The CLi amendment is NOT invalidated — but it LOSES its proof
    case.** The CLi amendment (Resolution B for the CLi) remains
    **valid on its own merits** — the CLi is a midline nucleus, and
    the tree **should** represent it as a single midline leaf,
    consistent with its anatomy. **But the CLi amendment can no
    longer be justified by appeal to the DR's clean
    representation** — the DR is no longer clean. **The CLi's
    amendment must stand on its own** (which it does — the
    argument that "the CLi is midline, therefore the tree should
    represent it as midline" does not require a proof case from
    another nucleus).
*   **The DR leaf and the CLi leaf now share the same anomaly.**
    Both are midline nuclei represented as paired. **Both should
    be resolved by Resolution B** (remove the `left/`/`right/`
    nodes) **or** by Resolution A (thin delegating side containers
    with anomaly flags — this module's implementation for the DR,
    the CLi's implementation for the CLi). **The tree has TWO
    anomalies now, not one — and they should be resolved
    consistently.**

Delegation to the Midline Leaf
------------------------------
The substantive anatomical content of the dorsal raphe nucleus —
**including its midline position, its modulatory class, its
serotonergic subpopulation, its place in the rostral raphe complex,
its place in the ascending serotonergic system, its subnuclear
organization, its clinical associations (major depressive disorder,
anxiety disorders, OCD, REM sleep, SSRI-induced sexual dysfunction),
and its full boundary stack** — is **entirely** in the **midline
leaf** at ``.../dorsal_raphe_nucleus/``. **This `left/` module adds
nothing to it.**

The midline leaf covers:
*   **The midline position** — the structural expression of the
    modulatory function; the raphe nucleus anatomy; the distributed
    projections that reach both sides.
*   **The neuromodulatory class** — the same class as the locus
    coeruleus, the median raphe, the caudal linear nucleus, and the
    VTA.
*   **The serotonergic subpopulation** — the overwhelming majority
    of DR neurons; the small non-serotonergic minority.
*   **The subnuclear organization** — the dorsal, ventral,
    ventrolateral, interfascicular, and caudal subnuclei — **all
    midline subdivisions of a single midline nucleus**.
*   **The rostral raphe complex context** — the DR as the largest,
    primary serotonergic nucleus; the CLi, the RLi, and the MnR as
    smaller contributors.
*   **The clinical associations** — the DR is the primary
    serotonergic substrate for major depressive disorder, anxiety
    disorders, OCD, REM sleep, and SSRI-induced sexual dysfunction.
*   **The full boundary stack** — the DR vs. the CLi, the MnR, the
    RLi, the VTA, the SN, the PAG, the locus coeruleus, and the
    medullary raphe nuclei.
*   **The full reference list** — the human raphe anatomy, the
    serotonergic system, the DR's subnuclear organization and
    forebrain projections, the REM sleep findings, the SSRI / mood
    / anxiety clinical literature, the contrast references.

**Consumers should resolve the DR's anatomical content by the
MIDLINE LEAF**, not by this `left/` module.

**Important — the midline leaf itself needs amendment.** The DR
leaf's **substantive anatomical content** is correct — the DR **is**
a midline serotonergic nucleus with the properties the leaf
describes. **What needs amendment is the DR leaf's framing of the
tree's representation** — its claims that "the tree represents the
DR cleanly", "the tree represents the DR correctly", "there are no
`left/` or `right/` nodes", "the DR path is the model the CLi
should follow". **Those claims are contradicted by the on-disk
tree** (this `left/` module and the `right/` mirror). The DR
leaf's **anatomical** content is **unchanged** by the amendment —
only the **tree-representation** claims need to be updated, **or**
the nodes need to be removed (Resolution B). **This `left/` module
is a statement of what needs to be amended** — it does not carry
anatomical content.

Function in the Human Brain
---------------------------
**See the midline leaf** at ``.../dorsal_raphe_nucleus/`` for the
substantive function of the dorsal raphe nucleus. **This `left/`
module has no function of its own** — the DR is a **midline**
nucleus, and the "left" of a midline nucleus is a **tree-structural
abstraction**, not an anatomical side. The DR's modulatory function
— the serotonergic modulation of its forebrain targets via
distributed projections — is documented **once**, in the midline
leaf.

Associated Disorders
--------------------
**See the midline leaf** at ``.../dorsal_raphe_nucleus/`` for the
substantive clinical associations of the dorsal raphe nucleus —
major depressive disorder, anxiety disorders, obsessive-compulsive
disorder, panic disorder, REM sleep disorders, and SSRI-induced
sexual dysfunction — all **direct** associations of the DR as the
**primary serotonergic substrate**. **This `left/` module has no
clinical associations of its own** — the DR is a **midline**
nucleus, and the "left" of a midline nucleus is a **tree-structural
abstraction**.

Lateralization Notes
--------------------
**There is no lateralization for a midline nucleus.** The dorsal
raphe nucleus is **midline** — it has **no left/right pair**
anatomically, and its "left" is a **tree-structural abstraction**,
not an anatomical side. **The DR modulates both sides** via its
**distributed projections** — it has no **left-vs-right functional
distinction** of its own.

*   **NO pairing — the DR is one midline nucleus.** The `left/`
    module is a **tree-structural** side container for a nucleus
    that is anatomically midline. **It does not imply the DR has a
    left/right pair anatomically.**
*   **NO lateralization — the DR's function is distributed
    bilaterally.** The DR's **serotonergic** projections reach
    **both sides** via their **distributed targets** — **the DR is
    a midline modulator**, not a lateralized structure.
*   **NO coupling warning — the DR is a modulatory nucleus.** The
    **midline position** is **not a coupling hazard** — there are
    **no "two sides" to couple** (the DR is one midline nucleus).
    **Neuromodulatory nuclei carry NO coupling warning** — same
    rule as every non-oscillator class.
*   **NO SLEA warning, NO amygdala-lateralization warning, NO
    rhinencephalon-exclusion flag** — the DR is not an
    extended-amygdala component, not part of the amygdala, and not
    a rhinencephalon structure.

**Consumers must NOT assume "left DR = right DR"** — there is no
**left DR** and **no right DR** anatomically. The DR is **one
midline nucleus**, and its "left" and "right" (in the tree) are
**tree-structural** abstractions, not anatomical sides. **The
midline leaf's `Lateralization Notes` section is the substantive
one** — this section only states the tree-structural fact.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** This `left/` module is a
    **tree-structural** side container — it does **not** import
    from `.../right/` (the DR is **midline** — there is no
    anatomical right side to import from).
*   **No cross-lobe imports.** This module does **not** import from
    the **PAG**, the **VTA**, the **substantia nigra**, the
    **caudal linear nucleus**, the **median raphe**, the **rostral
    linear nucleus**, the **medullary raphe nuclei**, the **locus
    coeruleus**, the **cerebral aqueduct**, or any other container.
    **The DR's relationships to these structures are documented in
    the MIDLINE LEAF** — not re-stated here.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **serotonergic phenotype** is a
    ``chemicals_hormones``-layer fact — documented in the
    **midline leaf**, **not** here.
*   **TREE-STRUCTURAL SIDE CONTAINER — NOT an anatomical pair.**
    This module is a **thin** side container for a **midline**
    nucleus. It **delegates** to the midline leaf at
    ``.../dorsal_raphe_nucleus/``. It **does not** carry
    substantive anatomical content, **does not** duplicate the
    midline leaf's boundary stacks, function, disorders,
    lateralization, or references, and **does not** imply the DR
    has a left/right pair anatomically.
*   **DELEGATION — the midline leaf is authoritative for the DR's
    anatomy.** Consumers seeking substantive DR content should
    resolve the **midline leaf** at ``.../dorsal_raphe_nucleus/``.
    **This `left/` module re-states nothing and adds no anatomical
    claims.**
*   **LIVE ANOMALY — the tree represents a MIDLINE nucleus as
    PAIRED.** This is the **same anomaly** as the CLi's `left/` and
    `right/` modules — **a midline nucleus represented as
    paired**.
*   **FALSIFIED CLEAN-CASE ASSUMPTION — the DR leaf's framing is
    now FALSE.** **The DR leaf was written assuming the tree
    represents the DR cleanly — with NO `left/` or `right/`
    nodes.** **That assumption is contradicted by this `left/`
    module and the `right/` mirror.** **The DR leaf's `Boundary
    status (MIDLINE LEAF — CLEANLY REPRESENTED)` section, its
    `The Cleanest Midline Leaf in the Tree` section, its
    `Overview`, its `Lateralization Notes`, its `Design Contract`,
    and its `Usage` `Do not` block all claim the tree represents
    the DR cleanly.** **The on-disk tree does not.** **The DR leaf
    must be amended** — either by **Resolution B** (removing the
    `left/` and `right/` nodes, restoring the clean case the DR
    leaf assumed) **or** by **Resolution A** (updating the DR
    leaf's prose to acknowledge the paired representation — this
    module's implementation).
*   **URGENT AMENDMENT — the DR leaf's proof-case role is
    compromised.** The DR leaf **used the DR as the proof case**
    that the tree can represent midline nuclei cleanly, **and as
    the model** that the CLi's representation should follow.
    **With `left/` and `right/` nodes under the DR, the DR is no
    longer a clean case, and no longer a model.** **The CLi
    amendment is NOT invalidated** — it remains **valid on its own
    merits** (the CLi is midline and should be represented
    cleanly) — **but the DR can no longer be cited as independent
    evidence.** **Both the DR and the CLi are now anomalous.**
    **The tree has TWO anomalies, not one.**
*   **RESOLUTION OPTIONS (recommend Resolution B — restore the
    clean case):**
    *   **Resolution B (recommended):** **Remove** the
        ``dorsal_raphe_nucleus/left/`` and
        ``dorsal_raphe_nucleus/right/`` nodes. The DR becomes a
        **single midline leaf**, as the DR leaf **assumed it was**.
        **This restores the DR leaf's clean-case framing** — the
        DR is again the proof case, the CLi amendment retains its
        model, and **this module and the ``right/`` module are
        deleted**. **Resolution B for the DR** is the same
        resolution the CLi leaf, the CLi `left/`, and the CLi
        `right/` modules recommend **for the CLi** — **both
        anomalies should be resolved the same way: remove the
        `left/`/`right/` nodes from both midline nuclei.**
    *   **Resolution A (this module's implementation):** Keep the
        ``left/`` and ``right/`` nodes, and **amend the DR leaf**
        to **acknowledge** that the tree represents the DR as
        paired (contradicting its earlier clean-case framing).
        **The DR leaf's "proof case" and "model" framing must be
        amended** — the DR is no longer the proof case; **both the
        DR and the CLi are anomalous**.
*   **THE TEGMENTUM CONTAINER AMENDMENT IS STILL NEEDED.** The
    tegmentum container's paired-leaf rule — *"each tegmentum
    nucleus is a paired structure (a ``left/`` leaf and a
    ``right/`` leaf)"* — **should be amended** to permit **midline
    nuclei** as **direct children** of ``tegmentum/`` — **not
    required** to be under ``left/`` or ``right/``. **The CLi
    leaf, the CLi `left/`, the CLi `right/`, the DR leaf, and now
    this `left/` module all flag this.** **The amendment is
    needed**, but **with the DR leaf's clean-case framing
    compromised**, the amendment's justification **now rests on
    the anatomy alone** — midline nuclei **should** be direct
    children **because they are midline**, **not because the tree
    already does this** (the tree does NOT already do this — both
    the CLi and the DR are represented as paired).
*   **THE MIDBRAIN CONTAINER AMENDMENT IS STILL NEEDED.** The
    midbrain container's PAG prose and the tegmentum container's
    paired-leaf rule are **still contradictory**, and the DR's
    paired representation **adds to the evidence** that the tree's
    midline representation is **inconsistent** (two midline nuclei
    — the CLi and the DR — both represented as paired, but both
    anatomically midline).
*   **NO coupling warning.** The DR is a **modulatory nucleus** —
    **neuromodulatory nuclei carry NO coupling warning**. This
    `left/` module **inherits** that — no coupling warning is
    imported here.
*   **NOT a CN nucleus.** The DR is **not** a cranial nerve
    nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. This `left/` module **inherits**
    that — no cross-listing is imported here.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** No cross-listing.
*   **No nested cross-listing.** This `left/` module is a **thin
    side container** — it has **no leaf children**, and its
    substantive content is **delegated** to the midline leaf.
*   **MIRROR PARITY with ``.../right/`` — strict mirror, NO
    warning.** The `left/` and `right/` modules are
    **structurally identical** — both are **thin tree-structural
    side containers** for a **midline** nucleus, both delegate to
    the midline leaf, both carry the same anomaly flag, both flag
    the same falsified clean-case assumption, both recommend the
    same resolutions. **The mirror is trivially clean** — the two
    side containers are symmetric **because the DR is midline and
    has no anatomical sides at all**.
*   **The on-disk tree is authoritative.** If the tree has
    ``dorsal_raphe_nucleus/left/`` and
    ``dorsal_raphe_nucleus/right/``, the **tree-structural**
    representation is authoritative **as a tree fact** — but the
    **anatomical fact** is that the DR is **midline**. **The
    midline leaf is authoritative for the DR's anatomy; the
    `left/` and `right/` nodes are tree-structural artifacts.**
    **The on-disk tree currently contradicts the DR leaf's
    clean-case framing — and the DR leaf should be amended.**

Usage
-----
Resolve the `left/` tree-structural side container by path::

    from infrastructure.brainparts.midbrain.tegmentum.dorsal_raphe_nucleus import left

**Resolve substantive DR content by the MIDLINE LEAF** — not by
this `left/` module::

    from infrastructure.brainparts.midbrain.tegmentum import dorsal_raphe_nucleus

Or by fully-qualified path string (midline leaf — the anatomical
home)::

    midline_path = "midbrain.tegmentum.dorsal_raphe_nucleus"
    # The MIDLINE LEAF — the anatomical home of the DR.
    # Substantive content: midline position, modulatory class,
    # serotonergic subpopulation, subnuclear organization, rostral
    # raphe complex context, clinical associations (depression,
    # anxiety, OCD, REM sleep, SSRI-induced sexual dysfunction),
    # full boundary stack, full references.
    #
    # AMENDMENT NOTE: the midline leaf's framing of the tree's
    # representation ("the tree represents the DR cleanly — no
    # left/ or right/ nodes") is CONTRADICTED by the on-disk tree
    # (this left/ module and the right/ mirror). The midline leaf
    # should be amended — either by removing the left/ and right/
    # nodes (Resolution B) or by updating the leaf's tree-
    # representation prose (Resolution A).

**Do not** assume the DR has a **left/right pair** anatomically.
It is a **midline raphe nucleus** — it has **no left/right pair**.
**This `left/` module is a tree-structural side container** — a
**tree-consistency** artifact for a nucleus that is anatomically
midline.

**Do not** assume the DR leaf's claim — *"the tree represents the
DR cleanly — no `left/` or `right/` nodes"* — is **true**. **It is
FALSE.** **This `left/` module and the `right/` mirror contradict
it.** **The DR leaf should be amended** — either by **removing**
the `left/` and `right/` nodes (Resolution B), or by **updating**
the DR leaf's prose (Resolution A). **Until it is amended, the DR
leaf contains a claim that contradicts the on-disk tree.**

**Do not** assume the DR leaf's claim — *"the DR is the proof case
that the tree can represent midline nuclei cleanly, and the model
the CLi should follow"* — is **still valid**. **It is NOT.** **The
DR is now represented as paired, exactly like the CLi.** **Both
are anomalous.** The **CLi amendment remains valid on its own
merits** — the CLi is midline and should be represented cleanly —
**but the DR can no longer be cited as independent evidence.**

**Do not** resolve the DR's anatomical content by this `left/`
module — **resolve the midline leaf** at
``.../dorsal_raphe_nucleus/``.

**Do not** import a **coupling warning** into this `left/` module —
the DR is a **modulatory nucleus**, and **neuromodulatory nuclei
carry NO coupling warning**.

**Do not** import the **serotonergic phenotype** into this `left/`
module — it is a ``chemicals_hormones``-layer fact, documented in
the **midline leaf**, **not** here.

**Do not** assume this `left/` module is a **CN nucleus** — the DR
is **not** a cranial nerve nucleus and is **NOT** cross-listed
with ``cranial_nerve_nuclei/``.

**Do not** assume "left DR = right DR" — there is **no left DR**
and **no right DR** anatomically. The DR is **one midline nucleus**.

**The structural tension should be resolved — URGENTLY.** The DR
leaf's **explicit clean-case framing** is **contradicted by the
on-disk tree**. **Resolution B (remove the `left/` and `right/`
nodes) is recommended** — it restores the clean case the DR leaf
assumed, it preserves the DR's role as the proof case for the CLi
amendment, and it resolves **both** anomalies (the CLi's and the
DR's) consistently. **Resolution A (amend the DR leaf's prose)**
is also valid — but the tree still represents the DR as paired,
and the DR leaf still needs updating. See *Design Contract* —
*URGENT AMENDMENT*.

Iterating the `left/` tree-structural side container's children
(recommended consumer pattern)::

    DORSAL_RAPHE_NUCLEUS_LEFT_CHILDREN = ()
    # The left/ module is a THIN tree-structural side container. It
    # has NO leaf children. Its substantive content is DELEGATED to
    # the midline leaf at .../dorsal_raphe_nucleus/.

Resolving substantive DR content (recommended consumer pattern)::

    # The MIDLINE LEAF is the anatomical home of the DR:
    #
    #   brainparts.midbrain.tegmentum.dorsal_raphe_nucleus
    #
    # It carries: the midline position, the modulatory class, the
    # serotonergic subpopulation, the subnuclear organization
    # (dorsal, ventral, ventrolateral, interfascicular, caudal),
    # the rostral raphe complex context, the ascending
    # serotonergic system context, the clinical associations, the
    # full boundary stack, and the full reference list.
    #
    # Do NOT resolve substantive DR content from this left/ module
    # — the left/ module is a tree-structural side container, not
    # an anatomical leaf.
    #
    # AMENDMENT NOTE: the midline leaf's tree-representation
    # framing ("the tree represents the DR cleanly") is CONTRADICTED
    # by this left/ module and the right/ mirror. The midline leaf
    # should be amended — see the DR leaf's own Design Contract
    # 'URGENT AMENDMENT' rule once it has been updated, or the
    # amendments recommended here.

The structural tension — options (not wired — structural decision)::

    # The tree represents the dorsal raphe nucleus as a container
    # with left/ and right/ children — a TREE-STRUCTURAL artifact
    # for a nucleus that is anatomically MIDLINE. There are two
    # resolutions, and they are the SAME two resolutions as for the
    # CLi — BOTH anomalies should be resolved consistently:
    #
    #   RESOLUTION B (recommended — restore the clean case):
    #     Remove the dorsal_raphe_nucleus/left/ and
    #     dorsal_raphe_nucleus/right/ nodes from the tree. The DR
    #     becomes a single midline leaf, as the DR leaf ASSUMED it
    #     was. This RESTORES the DR leaf's clean-case framing,
    #     preserves the DR's role as the proof case for the CLi
    #     amendment, and resolves BOTH anomalies (the CLi's and
    #     the DR's) consistently. THIS left/ module and the right/
    #     mirror WOULD BE DELETED.
    #
    #   RESOLUTION A (this module's implementation):
    #     Keep the left/ and right/ nodes, and AMEND the DR leaf
    #     to acknowledge that the tree represents the DR as paired
    #     (contradicting its earlier clean-case framing). The DR
    #     leaf's "proof case" and "model" framing must be amended —
    #     the DR is no longer the proof case; both the DR and the
    #     CLi are anomalous. THE CLi AMENDMENT REMAINS VALID ON ITS
    #     OWN MERITS — the CLi is midline and should be represented
    #     cleanly — but the DR can no longer be cited as independent
    #     evidence.
    #
    # Either resolution is valid. The tree should NOT continue to
    # represent the DR as paired WITHOUT either (a) removing the
    # left/ and right/ nodes (Resolution B), or (b) amending the DR
    # leaf's prose to acknowledge the paired representation
    # (Resolution A). The DR leaf currently contains a claim that
    # contradicts the on-disk tree — this is a LIVE
    # INCONSISTENCY that should be resolved URGENTLY.

References
----------
*   **See the midline leaf** at ``.../dorsal_raphe_nucleus/`` for
    the full reference list — the human raphe anatomy (Hornung,
    2003), the DR's subnuclear organization (Michelsen et al.,
    2007), the serotonergic system (Jacobs & Azmitia, 1992), the
    rostral raphe complex ascending projections (Azmitia & Segal,
    1978), the DR's forebrain serotonergic projections (Moore et
    al., 1978), the DR and REM sleep (McGinty & Harper, 1976), the
    serotonergic hypothesis of depression and SSRIs (Albert et
    al., 2012), the role of 5-HT in stress, anxiety, and
    depression (Graeff et al., 1996), the SSRI-induced sexual
    dysfunction (Clayton et al., 2002), the descending pain
    modulation (Fields & Basbaum, 1978), the anatomy of the
    serotonergic system (Törk, 1990), the serotonin receptors
    (Pazos & Palacios, 1985), the human DR serotonergic cells
    (Baker et al., 1991), the median raphe (contrast; Vertes &
    Crane, 1997), the locus coeruleus (contrast; Foote et al.,
    1983), the VTA (contrast; Fields et al., 2007), and the SLEA
    contrast (Alheid & Heimer, 1988).
*   **This `left/` module has no substantive references of its
    own** — it is a **tree-structural side container** for a
    **midline** nucleus. The **midline leaf** carries the
    substantive references.
*   NeuroNames — Dorsal raphe nucleus; FMA — Dorsal raphe nucleus.
    **There is no "left dorsal raphe nucleus" or "right dorsal
    raphe nucleus"** in the standard anatomical atlases — the DR
    is a **single midline nucleus**.
"""