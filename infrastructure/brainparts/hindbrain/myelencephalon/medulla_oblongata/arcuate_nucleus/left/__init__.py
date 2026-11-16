"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.left
==========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── arcuate_nucleus
                └── left   <-- THIS MODULE

**Primary synonym:** Left arcuate nucleus of the medulla oblongata;
left medullary arcuate nucleus; left nucleus arcuatus medullae
oblongatae; left ventral medullary surface (VMS) arcuate region.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** — a group of **small,
heterogeneous neurons and glia** at the **left ventral medullary
surface** (VMS), adjacent to the **anterior median fissure** and
the **left medullary pyramid**. It is **NOT** the **left
hypothalamic arcuate nucleus** (infundibular nucleus) — a
**different structure** in a **different container**.
**Part of:** The **arcuate_nucleus** bilateral container — which
is part of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../arcuate_nucleus/`` → **direct child**
of the arcuate_nucleus container. The **left** arcuate nucleus is
one of the **two** structural children of the container (the other
is ``right``).
**Structural children:** **None.** This is a **leaf** module. The
left arcuate nucleus is represented as a **single structure** — it
has **no structural children** of its own.
**Boundary status (NOT the right arcuate nucleus — the
contralateral leaf):** **Boundary case — the left arcuate nucleus
is NOT the right arcuate nucleus.** The **right arcuate nucleus**
(``.../arcuate_nucleus/right/``) is the **contralateral leaf** —
the arcuate nucleus of the **right** medulla. **They are
DIFFERENT LEAVES** — the ``left`` and ``right`` modules are the two
sides of the **bilateral container**. Consumers must **not**
conflate the **left** arcuate nucleus with the **right** arcuate
nucleus — resolve the right side via ``arcuate_nucleus.right``.
**Boundary status (NOT the hypothalamic arcuate nucleus — a
DIFFERENT STRUCTURE with the SAME NAME):** **Boundary case — the
left medullary arcuate nucleus is NOT the left hypothalamic
arcuate nucleus.** The **hypothalamic arcuate nucleus**
(infundibular nucleus) is a **mediobasal hypothalamic** structure
— part of the **hypothalamus**
(``.../diencephalon/hypothalamus/``) — and is the **central
regulator** of **energy homeostasis**, **GnRH secretion**, and
**prolactin** regulation. The **left medullary arcuate nucleus**
(here) is a **caudal brainstem** structure at the **left ventral
medullary surface** — it does **NOT** regulate **energy
homeostasis** or **reproduction**. **They share a NAME but are
DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** Consumers must
**not** conflate the **left medullary arcuate nucleus** with the
**left hypothalamic arcuate nucleus** — resolve the hypothalamic
one via ``.../hypothalamus/``.
**Boundary status (NOT the ventrolateral medulla as a whole — a
specific nucleus within the region):** **Boundary case — the left
arcuate nucleus is NOT the left ventrolateral medulla (VLM).** The
**left ventrolateral medulla** is a **region** containing the
**left RVLM** (``.../rostral_ventrolateral_medulla/left/``), the
**left CVLM** (``.../caudal_ventrolateral_medulla/left/``), and the
**left arcuate nucleus** (here). The **left arcuate nucleus** is a
**specific nucleus** at the **left ventral surface** — it is
**NOT** the whole **left VLM**, and it is **NOT** the **left
RVLM** or **left CVLM**. Consumers must **not** conflate the
**left arcuate nucleus** with the **whole left ventrolateral
medulla**.
**Boundary status (NOT the left RVLM — the RVLM is the sympathetic
premotor / vasomotor center):** **Boundary case — the left arcuate
nucleus is NOT the left RVLM.** The **left RVLM**
(``.../rostral_ventrolateral_medulla/left/``) is the **left
sympathetic premotor / vasomotor center** — it provides the
**tonic excitatory drive** to the **left intermediolateral cell
column**. The **left arcuate nucleus** (here) is a
**ventral-surface chemosensory and hypothalamic-projecting**
nucleus — it is **NOT** the **left RVLM**. Consumers must **not**
conflate the two.
**Boundary status (NOT the left CVLM — the CVLM is the
sympathoinhibitory relay):** **Boundary case — the left arcuate
nucleus is NOT the left CVLM.** The **left CVLM**
(``.../caudal_ventrolateral_medulla/left/``) is the **left
sympathoinhibitory relay** — it receives **NTS** input and
**inhibits the RVLM**. The **left arcuate nucleus** (here) is a
**ventral-surface chemosensory and hypothalamic-projecting**
nucleus — it is **NOT** the **left CVLM**. Consumers must **not**
conflate the two.
**Boundary status (NOT the left retrotrapezoid nucleus — adjacent
but distinct):** **Boundary case — the left arcuate nucleus is
NOT the left retrotrapezoid nucleus.** The **left retrotrapezoid
nucleus** (RTN) is a **more rostral** ventral-surface **respiratory
chemoreceptor** — it is wired under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/left/``.
The **left arcuate nucleus** (here) is a **more caudal**
ventral-surface chemosensory / hypothalamic-projecting nucleus.
**Both are ventral-surface chemosensory regions, but they are
DIFFERENT STRUCTURES.** Consumers must **not** conflate the two —
the **left RTN** is a **respiratory chemoreceptor**; the **left
arcuate nucleus** is a **hypothalamic-projecting chemosensory
nucleus**.
**Boundary status (NOT the left olivary body — adjacent but
distinct):** **Boundary case — the left arcuate nucleus is NOT the
left olivary body.** The **left olivary body**
(``.../olivary_body/left/``) contains the **left inferior olivary
nucleus** — the **sole source of climbing fibers** to the
cerebellum. The **left arcuate nucleus** (here) is a
**ventral-surface chemosensory / hypothalamic-projecting**
nucleus. **They are DIFFERENT STRUCTURES** — the left olivary
body is a **cerebellar relay**; the left arcuate nucleus is a
**ventral-surface nucleus**. Consumers must **not** conflate the
two.
**Boundary status (NOT the left medullary pyramid — adjacent but
distinct):** **Boundary case — the left arcuate nucleus is NOT
the left medullary pyramid.** The **left medullary pyramid**
(``.../medullary_pyramid/left/``) is the **left corticospinal /
corticobulbar tract** — a **white-matter** structure at the **left
ventral medulla**. The **left arcuate nucleus** (here) is a
**grey-matter** nucleus at the **left ventral medullary surface**,
**adjacent to** the left pyramid. **They are DIFFERENT
STRUCTURES** — the pyramid is **white matter** (descending motor
fibers); the left arcuate nucleus is **grey matter** (neurons and
glia). Consumers must **not** conflate the two.

Overview
--------
The **left arcuate nucleus** is the **left-side
ventral-surface chemosensory and hypothalamic-projecting** nucleus
of the **medulla oblongata**. It lies at the **left ventral
medullary surface** (VMS), adjacent to the **anterior median
fissure** and the **left medullary pyramid**, and projects
**rostrally to the hypothalamus**.

**This is a LEAF module.** The **left arcuate nucleus** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **nucleus-level** resolution of
the left side use this module; consumers that need **right-side**
resolution use ``.../arcuate_nucleus/right/``; consumers that
need **bilateral** resolution iterate over both.

**The left arcuate nucleus is the MEDULLARY arcuate nucleus, NOT
the hypothalamic one.** The **left hypothalamic arcuate nucleus**
(infundibular nucleus) is a **different structure** in a
**different container** (``.../hypothalamus/left/``). It
regulates **energy homeostasis**, **GnRH**, and **prolactin**.
The **left medullary arcuate nucleus** (here) is a **caudal
brainstem** nucleus involved in **central chemoreception** and
**hypothalamic projection**. **They share a NAME but are
DIFFERENT STRUCTURES.**

**The left arcuate nucleus is at the LEFT VENTRAL MEDULLARY
SURFACE.** It is **not** a deep medullary nucleus — it lies at
the **surface**, which is relevant for its **chemosensory** and
**neurosecretory** roles (it can sense **CSF** and **blood**
composition at the left ventral surface).

**The left arcuate nucleus is functionally adjacent to the left
RVLM and left CVLM, but is NOT the left RVLM or left CVLM.** It
is a **separate structure** with its own **hypothalamic-projecting**
and **chemosensory** roles.

The Left Arcuate Nucleus / Right Arcuate Nucleus Boundary
---------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left arcuate nucleus** (this module) — the arcuate nucleus
    of the **left** medulla.

*   **Right arcuate nucleus** (``.../arcuate_nucleus/right/``) —
    the arcuate nucleus of the **right** medulla.

**The two are the SIDES of the bilateral arcuate nucleus
container.** They are **structurally symmetric mirror pairs** —
same cytoarchitecture, same projections, same functions.
Consumers must **not** conflate the left with the right — resolve
the right side via ``arcuate_nucleus.right``.

The Left Arcuate Nucleus / Hypothalamic Arcuate Nucleus Boundary
----------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Left medullary arcuate nucleus** (this module) — a **caudal
    brainstem** nucleus at the **left ventral medullary surface**.

*   **Left hypothalamic arcuate nucleus** (infundibular nucleus)
    (``.../diencephalon/hypothalamus/left/``) — a **mediobasal
    hypothalamic** nucleus regulating **energy homeostasis**,
    **GnRH**, and **prolactin**.

**They share a NAME but are DIFFERENT STRUCTURES in DIFFERENT
CONTAINERS.** Consumers must **not** conflate the two — resolve
the **left hypothalamic** one via ``.../hypothalamus/left/``, and
the **left medullary** one via this module.

The Left Arcuate Nucleus / Left Ventrolateral Medulla Boundary
--------------------------------------------------------------
This is the **region / specific-nucleus** boundary:

*   **Left arcuate nucleus** (this module) — a **specific
    nucleus** at the left ventral medullary surface.

*   **Left ventrolateral medulla (VLM)** — a **region**
    containing the **left RVLM**, **left CVLM**, and the **left
    arcuate nucleus**.

**The left arcuate nucleus is a NUCLEUS within the left VLM
region, but it is NOT the whole left VLM.** Consumers must
**not** conflate the **left arcuate nucleus** with the **left
RVLM** or **left CVLM**.

The Left Arcuate Nucleus / Left RVLM Boundary
---------------------------------------------
This is the **sympathetic-premotor** boundary:

*   **Left arcuate nucleus** (this module) — a **left
    ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``) —
    the **left sympathetic premotor / vasomotor center**.

**The left arcuate nucleus is NOT the left RVLM.** Consumers must
**not** conflate the two — the **left RVLM** provides **tonic
sympathetic drive**; the **left arcuate nucleus** is a
**chemosensory and hypothalamic-projecting** nucleus.

The Left Arcuate Nucleus / Left CVLM Boundary
---------------------------------------------
This is the **sympathoinhibitory** boundary:

*   **Left arcuate nucleus** (this module) — a **left
    ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.

*   **Left CVLM** (``.../caudal_ventrolateral_medulla/left/``) —
    the **left sympathoinhibitory relay**.

**The left arcuate nucleus is NOT the left CVLM.** Consumers must
**not** conflate the two.

The Left Arcuate Nucleus / Left Retrotrapezoid Nucleus Boundary
---------------------------------------------------------------
This is the **chemosensory-adjacency** boundary:

*   **Left arcuate nucleus** (this module) — a **caudal
    left ventral-surface chemosensory / hypothalamic-projecting**
    nucleus.

*   **Left retrotrapezoid nucleus** (RTN)
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/left/``)
    — a **more rostral** left ventral-surface **respiratory
    chemoreceptor**.

**Both are left ventral-surface chemosensory regions, but they
are DIFFERENT STRUCTURES.** Consumers must **not** conflate them.

The Left Arcuate Nucleus / Left Olivary Body Boundary
-----------------------------------------------------
This is the **cerebellar-relay** boundary:

*   **Left arcuate nucleus** (this module) — a **left
    ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.

*   **Left olivary body** (``.../olivary_body/left/``) — contains
    the **left inferior olivary nucleus** (source of **climbing
    fibers** to the left cerebellar hemisphere).

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
them.

The Left Arcuate Nucleus / Left Medullary Pyramid Boundary
----------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Left arcuate nucleus** (this module) — **grey-matter**
    nucleus at the left ventral medullary surface.

*   **Left medullary pyramid** (``.../medullary_pyramid/left/``) —
    **white-matter** left corticospinal / corticobulbar tract.

**They are ADJACENT but DIFFERENT** — the left arcuate nucleus
sits **at the left surface** near the left pyramid, but is **grey
matter**, not **white matter**. Consumers must **not** conflate
the two.

Function in the Human Brain
---------------------------
The left arcuate nucleus's functions are **left
ventral-surface chemosensory** and **hypothalamic-projecting** —
**NOT sympathetic premotor** and **NOT respiratory rhythm**:

*   **Central chemoreception (left ventral medullary surface):**
    The **left arcuate nucleus** — together with the **left
    ventral medullary surface** glia and the adjacent **left
    RTN** — contributes to **central CO₂/H⁺ chemoreception**.
    The **left ventral medullary surface** is a **chemosensory**
    region; the **left arcuate nucleus** is part of that region.

*   **Hypothalamic projection (left ventral medullary surface →
    hypothalamus):** The **left arcuate nucleus** projects
    **rostrally to the hypothalamus** (left preoptic area, left
    anterior hypothalamus, left lateral hypothalamus) via **left
    ventral medullary surface pathways**. These projections
    contribute to **neuroendocrine** and **autonomic**
    regulation — possibly including **fever**, **satiety**, and
    **stress responses**.

*   **Neurosecretion / CSF-contacting (left ventral medullary
    surface):** The **left arcuate nucleus** is a region of
    **CSF-contacting neurons** and **neurosecretory** cells at
    the left ventral surface — releasing substances into the
    **CSF** or **perivascular space**. This is **less
    characterized** in humans than the **hypothalamic**
    neurosecretory nuclei.

*   **NOT the hypothalamic arcuate nucleus functions:** The
    **energy homeostasis**, **GnRH**, and **prolactin**
    regulation are **hypothalamic arcuate nucleus** functions —
    **NOT** left medullary arcuate nucleus functions.

*   **NOT left sympathetic premotor:** The **left sympathetic
    premotor** function is the **left RVLM** — **NOT** the left
    arcuate nucleus.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the left arcuate nucleus.

**The unifying theme:** the left arcuate nucleus is a **left
ventral-surface chemosensory and hypothalamic-projecting** nucleus
of the **caudal medulla** — it is **NOT** the left hypothalamic
arcuate nucleus, **NOT** the left RVLM, **NOT** the left CVLM,
**NOT** the left RTN, and **NOT** the left olivary body. It is a
**specific left ventral-surface nucleus** with **chemosensory**
and **hypothalamic-projecting** roles.

Associated Disorders
--------------------
The left arcuate nucleus has **no named clinical syndrome** of its
own — its clinical associations are **indirect**:

*   **Central hypoventilation (via left ventral medullary surface
    chemoreception):** Dysfunction of the **left ventral medullary
    surface** chemosensory region — including the **left arcuate
    nucleus** and the **left RTN** — contributes to **central
    hypoventilation** (e.g., **CCHS**). The **left arcuate
    nucleus** is a **chemosensory** contributor, but the
    **primary rhythm generator** is the **pre-Bötzinger complex**
    (VRG).

*   **Sudden infant death syndrome (SIDS — via left ventral
    medullary surface abnormalities):** Abnormalities of the
    **left arcuate nucleus** and the **left ventral medullary
    surface** have been reported in **SIDS** — **reduced**
    **neurotransmitter** (e.g., **serotonin**) **binding** and
    **abnormal** **cytoarchitecture** in the left arcuate region.
    These findings are **contested** and **not specific** to the
    left arcuate nucleus.

*   **Neurogenic hypertension (via left ventrolateral medulla
    dysfunction):** The **left ventrolateral medulla** —
    including the **left RVLM** and adjacent **left arcuate**
    region — is involved in **neurogenic hypertension**. The
    **left arcuate nucleus** contributes to the **chemosensory**
    and **hypothalamic** aspects, but the **sympathetic premotor**
    role is the **left RVLM**.

*   **No Named "Left Arcuate Nucleus Syndrome":** The left arcuate
    nucleus is a **specific** but **functionally subtle** nucleus
    — it has **no named clinical syndrome**. Its clinical
    relevance is **indirect**, via **left ventral medullary
    surface** **chemosensory** and **hypothalamic-projecting**
    functions.

**What is NOT here:** The left arcuate nucleus is **not** the
substrate for **hypothalamic obesity** (left hypothalamic arcuate
nucleus), **Kallmann syndrome** (left hypothalamic arcuate nucleus
/ GnRH neurons), or **hyperprolactinemia** (left hypothalamic
arcuate nucleus / tuberoinfundibular dopamine neurons). Its
clinical relevance is the **left medullary** **chemosensory** and
**hypothalamic-projecting** functions listed above.

Lateralization Notes
--------------------
This is the **left** arcuate nucleus module. The arcuate nucleus
is a **bilateral container** whose two sides are **structurally
symmetric mirror pairs** — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right** arcuate
    nuclei are **structurally symmetric** — they are **mirror
    pairs** with the **same** cytoarchitecture, **same**
    projections, and **same** functions. The **left** arcuate
    nucleus projects to the **left** hypothalamus and adjacent
    structures; the **right** arcuate nucleus projects to the
    **right** hypothalamus and adjacent structures.

*   **NO Lateralization Warning:** The arcuate nucleus has **no
    known functional lateralization** in humans. Consumers must
    **not** import a **lateralization warning** into the left
    arcuate nucleus — the **left** and **right** sides are
    **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left arcuate
    nucleus is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the left arcuate nucleus.

*   **NO Fear-Output Warning:** The left arcuate nucleus is **not**
    a fear-output structure — it is a **ventral-surface
    chemosensory and hypothalamic-projecting** nucleus. Consumers
    must **not** conflate it with the **central nucleus** or with
    the **amygdala**.

**A consumer that assumes "left arcuate nucleus = right arcuate
nucleus" will be structurally correct** — the two sides are
**symmetric** and **functionally equivalent**. The arcuate
nucleus is a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no
lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left arcuate nucleus is a
    **leaf** — it does **not** import from ``.../right/`` or any
    other right-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../ventral_respiratory_group/``, ``.../olivary_body/``,
    ``.../medullary_pyramid/``, or any other container. The left
    arcuate nucleus's relationships to the left RVLM, left CVLM,
    left RTN, left olivary body, left medullary pyramid, and left
    hypothalamic arcuate nucleus are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left arcuate
    nucleus is a **single structure** — it has **no structural
    children**. Consumers must **not** expect further sub-paths
    under ``.../left/``.
*   **NOT the right arcuate nucleus.** The right arcuate nucleus
    is a **separate leaf** under ``.../arcuate_nucleus/right/``.
    Consumers must **not** conflate the left with the right.
*   **NOT the hypothalamic arcuate nucleus.** The left
    hypothalamic arcuate nucleus (infundibular nucleus) is a
    **different structure** in a **different container**
    (``.../hypothalamus/left/``). Consumers must **not** conflate
    the two.
*   **NOT the left RVLM or left CVLM.** The left RVLM is the
    left sympathetic premotor center; the left CVLM is the left
    sympathoinhibitory relay. The left arcuate nucleus is a
    **ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.
*   **NOT the left retrotrapezoid nucleus.** The left RTN is a
    **more rostral** respiratory chemoreceptor. The left arcuate
    nucleus is **caudal** to the left RTN.
*   **NOT the left olivary body.** The left olivary body is a
    cerebellar relay (left inferior olivary nucleus).
*   **NOT the left medullary pyramid.** The left pyramid is
    white-matter left corticospinal / corticobulbar tract; the
    left arcuate nucleus is grey matter.
*   **No ``AREA_PATHS`` hop.** The left arcuate nucleus is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The left arcuate nucleus has no
    nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the right arcuate nucleus — strict
    mirror with NO warning.** The left and right arcuate nucleus
    modules are **structurally identical** — same leaf status,
    same **chemosensory / hypothalamic-projecting** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.left"
    )

**Do not** assume the left arcuate nucleus is the **right arcuate
nucleus**. The right arcuate nucleus is the **separate leaf** at
``.../arcuate_nucleus/right/``.

**Do not** assume the left arcuate nucleus is the **left
hypothalamic arcuate nucleus**. The **left hypothalamic arcuate
nucleus** (infundibular nucleus) is a **different structure** in a
**different container** (``.../hypothalamus/left/``).

**Do not** assume the left arcuate nucleus is the **left RVLM**,
the **left CVLM**, the **left retrotrapezoid nucleus**, the
**left olivary body**, or the **left medullary pyramid**. Each is
a **different structure**.

**Do not** assume the left arcuate nucleus has **structural
children**. It is a **leaf** — it represents the left arcuate
nucleus as a **single structure**.

Iterating the left arcuate nucleus's (empty) children (recommended
consumer pattern)::

    LEFT_ARCUATE_NUCLEUS_CHILDREN = ()
    # The left arcuate nucleus is a leaf. It has no structural
    # children.

Reaching the right arcuate nucleus (recommended consumer pattern
— the contralateral leaf)::

    # The right arcuate nucleus is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.right
    #
    # The left and right arcuate nuclei are structurally
    # symmetric mirror pairs.

Reaching the left hypothalamic arcuate nucleus (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The left hypothalamic arcuate nucleus (infundibular
    # nucleus) is NOT the left medullary arcuate nucleus:
    #
    #   diencephalon.hypothalamus.left.arcuate_nucleus
    #
    # It regulates energy homeostasis, GnRH, and prolactin —
    # functions DIFFERENT from the left medullary arcuate nucleus.

Reaching the left ventrolateral medulla components (recommended
consumer pattern — NOTE the region vs. specific-nucleus
distinction)::

    # The left RVLM and left CVLM are SEPARATE structures from
    # the left arcuate nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.left
    #
    # The left arcuate nucleus is a VENTRAL-SURFACE nucleus — it
    # is PART of the left ventrolateral medulla REGION, but it is
    # NOT the left RVLM or left CVLM.

Reaching the left retrotrapezoid nucleus (recommended consumer
pattern — NOTE the different structure)::

    # The left retrotrapezoid nucleus is:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.left
    #
    # It is a MORE ROSTRAL respiratory chemoreceptor — DIFFERENT
    # from the caudal left arcuate nucleus.

Reaching the left olivary body and left medullary pyramid
(recommended consumer pattern — NOTE the different structures)::

    # The left olivary body and left medullary pyramid are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.left
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.left
    #
    # The left olivary body contains the left inferior olivary
    # nucleus (cerebellar climbing fibers); the left medullary
    # pyramid is the left corticospinal / corticobulbar tract.
    # Both are DIFFERENT from the left arcuate nucleus.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"arcuate_nucleus.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical medullary anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Medulla oblongata overview; ventral medullary surface
    structures.)
*   **Ventral medullary surface chemosensitivity:** Millhorn,
    D.E., Eldridge, F.L. (eds.) (1990). *Neurobiology of Central
    Chemosensitivity.* (Ventral medullary surface; arcuate
    nucleus; central chemoreception.)
*   **Medullary arcuate nucleus projections:** Blessing, W.W.
    (1997). *The Lower Brain Stem and Bodily Homeostasis.*
    (Medullary arcuate nucleus; hypothalamic projections;
    ventral medullary surface pathways.)
*   **Central chemoreception overview:** Guyenet, P.G.,
    Stornetta, R.L., Bayliss, D.A. (2008). "Central respiratory
    chemoreception: the retrotrapezoid nucleus." *Trends in
    Neurosciences* 31:565–573. (RTN and adjacent ventral-surface
    regions; chemosensory organization.)
*   **RVLM / sympathetic premotor (contrast):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure." *Nature
    Reviews Neuroscience* 7:335–346. (RVLM; sympathetic premotor
    neurons — DIFFERENT from the arcuate nucleus.)
*   **CVLM / sympathoinhibition (contrast):** Schreihofer, A.M.,
    Guyenet, P.G. (2000). "Role of the ventrolateral medulla in
    sympathoinhibition." *American Journal of Physiology*
    279:R1701–R1711. (CVLM; sympathoinhibitory relay — DIFFERENT
    from the arcuate nucleus.)
*   **Hypothalamic arcuate nucleus (contrast — NOT this
    structure):** Cone, R.D., et al. (2001). "The arcuate
    nucleus as a conduit for diverse signals relevant to energy
    homeostasis." *International Journal of Obesity* 25:S63–S67.
    (Hypothalamic arcuate nucleus — DIFFERENT from the medullary
    arcuate nucleus.)
*   **SIDS and ventral medullary surface:** Kinney, H.C., et al.
    (2003). "Sudden infant death syndrome and the medullary
    serotonergic system." *JAMA* 290:1599–1609. (Arcuate nucleus
    and ventral medullary surface abnormalities in SIDS —
    contested and not specific.)
*   **CSF-contacting neurons:** Vigh, B., et al. (2004). "The
    system of cerebrospinal fluid-contacting neurons." *Archives
    of Histology and Cytology* 46:427–468. (Ventral medullary
    surface neurons; arcuate nucleus as CSF-contacting region.)
*   **Medullary cytoarchitecture:** Paxinos, G., Huang, X.-F.
    (2013). *The Behaving Human Brain: A Cytoarchitectural
    Atlas.* (Medullary nuclei; ventral-surface structures.)
*   NeuroNames — Arcuate nucleus of the medulla oblongata; FMA —
    Arcuate nucleus of medulla oblongata.
"""