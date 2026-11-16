"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.right
===========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── arcuate_nucleus
                └── right   <-- THIS MODULE

**Primary synonym:** Right arcuate nucleus of the medulla oblongata;
right medullary arcuate nucleus; right nucleus arcuatus medullae
oblongatae; right ventral medullary surface (VMS) arcuate region.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** — a group of **small,
heterogeneous neurons and glia** at the **right ventral medullary
surface** (VMS), adjacent to the **anterior median fissure** and
the **right medullary pyramid**. It is **NOT** the **right
hypothalamic arcuate nucleus** (infundibular nucleus) — a
**different structure** in a **different container**.
**Part of:** The **arcuate_nucleus** bilateral container — which
is part of the **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../arcuate_nucleus/`` → **direct child**
of the arcuate_nucleus container. The **right** arcuate nucleus is
one of the **two** structural children of the container (the other
is ``left``).
**Structural children:** **None.** This is a **leaf** module. The
right arcuate nucleus is represented as a **single structure** — it
has **no structural children** of its own.
**Boundary status (NOT the left arcuate nucleus — the
contralateral leaf):** **Boundary case — the right arcuate nucleus
is NOT the left arcuate nucleus.** The **left arcuate nucleus**
(``.../arcuate_nucleus/left/``) is the **contralateral leaf** —
the arcuate nucleus of the **left** medulla. **They are
DIFFERENT LEAVES** — the ``left`` and ``right`` modules are the two
sides of the **bilateral container**. Consumers must **not**
conflate the **right** arcuate nucleus with the **left** arcuate
nucleus — resolve the left side via ``arcuate_nucleus.left``.
**Boundary status (NOT the hypothalamic arcuate nucleus — a
DIFFERENT STRUCTURE with the SAME NAME):** **Boundary case — the
right medullary arcuate nucleus is NOT the right hypothalamic
arcuate nucleus.** The **hypothalamic arcuate nucleus**
(infundibular nucleus) is a **mediobasal hypothalamic** structure
— part of the **hypothalamus**
(``.../diencephalon/hypothalamus/``) — and is the **central
regulator** of **energy homeostasis**, **GnRH secretion**, and
**prolactin** regulation. The **right medullary arcuate nucleus**
(here) is a **caudal brainstem** structure at the **right ventral
medullary surface** — it does **NOT** regulate **energy
homeostasis** or **reproduction**. **They share a NAME but are
DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** Consumers must
**not** conflate the **right medullary arcuate nucleus** with the
**right hypothalamic arcuate nucleus** — resolve the hypothalamic
one via ``.../hypothalamus/``.
**Boundary status (NOT the ventrolateral medulla as a whole — a
specific nucleus within the region):** **Boundary case — the right
arcuate nucleus is NOT the right ventrolateral medulla (VLM).** The
**right ventrolateral medulla** is a **region** containing the
**right RVLM** (``.../rostral_ventrolateral_medulla/right/``), the
**right CVLM** (``.../caudal_ventrolateral_medulla/right/``), and
the **right arcuate nucleus** (here). The **right arcuate nucleus**
is a **specific nucleus** at the **right ventral surface** — it is
**NOT** the whole **right VLM**, and it is **NOT** the **right
RVLM** or **right CVLM**. Consumers must **not** conflate the
**right arcuate nucleus** with the **whole right ventrolateral
medulla**.
**Boundary status (NOT the right RVLM — the RVLM is the sympathetic
premotor / vasomotor center):** **Boundary case — the right arcuate
nucleus is NOT the right RVLM.** The **right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) is the **right
sympathetic premotor / vasomotor center** — it provides the
**tonic excitatory drive** to the **right intermediolateral cell
column**. The **right arcuate nucleus** (here) is a
**ventral-surface chemosensory and hypothalamic-projecting**
nucleus — it is **NOT** the **right RVLM**. Consumers must **not**
conflate the two.
**Boundary status (NOT the right CVLM — the CVLM is the
sympathoinhibitory relay):** **Boundary case — the right arcuate
nucleus is NOT the right CVLM.** The **right CVLM**
(``.../caudal_ventrolateral_medulla/right/``) is the **right
sympathoinhibitory relay** — it receives **NTS** input and
**inhibits the RVLM**. The **right arcuate nucleus** (here) is a
**ventral-surface chemosensory and hypothalamic-projecting**
nucleus — it is **NOT** the **right CVLM**. Consumers must **not**
conflate the two.
**Boundary status (NOT the right retrotrapezoid nucleus — adjacent
but distinct):** **Boundary case — the right arcuate nucleus is
NOT the right retrotrapezoid nucleus.** The **right retrotrapezoid
nucleus** (RTN) is a **more rostral** ventral-surface **respiratory
chemoreceptor** — it is wired under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/right/``.
The **right arcuate nucleus** (here) is a **more caudal**
ventral-surface chemosensory / hypothalamic-projecting nucleus.
**Both are ventral-surface chemosensory regions, but they are
DIFFERENT STRUCTURES.** Consumers must **not** conflate the two —
the **right RTN** is a **respiratory chemoreceptor**; the **right
arcuate nucleus** is a **hypothalamic-projecting chemosensory
nucleus**.
**Boundary status (NOT the right olivary body — adjacent but
distinct):** **Boundary case — the right arcuate nucleus is NOT
the right olivary body.** The **right olivary body**
(``.../olivary_body/right/``) contains the **right inferior
olivary nucleus** — the **sole source of climbing fibers** to the
cerebellum. The **right arcuate nucleus** (here) is a
**ventral-surface chemosensory / hypothalamic-projecting**
nucleus. **They are DIFFERENT STRUCTURES** — the right olivary
body is a **cerebellar relay**; the right arcuate nucleus is a
**ventral-surface nucleus**. Consumers must **not** conflate the
two.
**Boundary status (NOT the right medullary pyramid — adjacent but
distinct):** **Boundary case — the right arcuate nucleus is NOT
the right medullary pyramid.** The **right medullary pyramid**
(``.../medullary_pyramid/right/``) is the **right corticospinal /
corticobulbar tract** — a **white-matter** structure at the **right
ventral medulla**. The **right arcuate nucleus** (here) is a
**grey-matter** nucleus at the **right ventral medullary surface**,
**adjacent to** the right pyramid. **They are DIFFERENT
STRUCTURES** — the pyramid is **white matter** (descending motor
fibers); the right arcuate nucleus is **grey matter** (neurons and
glia). Consumers must **not** conflate the two.

Overview
--------
The **right arcuate nucleus** is the **right-side
ventral-surface chemosensory and hypothalamic-projecting** nucleus
of the **medulla oblongata**. It lies at the **right ventral
medullary surface** (VMS), adjacent to the **anterior median
fissure** and the **right medullary pyramid**, and projects
**rostrally to the hypothalamus**.

**This is a LEAF module.** The **right arcuate nucleus** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **nucleus-level** resolution of
the right side use this module; consumers that need **left-side**
resolution use ``.../arcuate_nucleus/left/``; consumers that need
**bilateral** resolution iterate over both.

**The right arcuate nucleus is the MEDULLARY arcuate nucleus, NOT
the hypothalamic one.** The **right hypothalamic arcuate nucleus**
(infundibular nucleus) is a **different structure** in a
**different container** (``.../hypothalamus/right/``). It
regulates **energy homeostasis**, **GnRH**, and **prolactin**.
The **right medullary arcuate nucleus** (here) is a **caudal
brainstem** nucleus involved in **central chemoreception** and
**hypothalamic projection**. **They share a NAME but are
DIFFERENT STRUCTURES.**

**The right arcuate nucleus is at the RIGHT VENTRAL MEDULLARY
SURFACE.** It is **not** a deep medullary nucleus — it lies at
the **surface**, which is relevant for its **chemosensory** and
**neurosecretory** roles (it can sense **CSF** and **blood**
composition at the right ventral surface).

**The right arcuate nucleus is functionally adjacent to the right
RVLM and right CVLM, but is NOT the right RVLM or right CVLM.** It
is a **separate structure** with its own **hypothalamic-projecting**
and **chemosensory** roles.

The Right Arcuate Nucleus / Left Arcuate Nucleus Boundary
---------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right arcuate nucleus** (this module) — the arcuate nucleus
    of the **right** medulla.

*   **Left arcuate nucleus** (``.../arcuate_nucleus/left/``) —
    the arcuate nucleus of the **left** medulla.

**The two are the SIDES of the bilateral arcuate nucleus
container.** They are **structurally symmetric mirror pairs** —
same cytoarchitecture, same projections, same functions.
Consumers must **not** conflate the right with the left — resolve
the left side via ``arcuate_nucleus.left``.

The Right Arcuate Nucleus / Hypothalamic Arcuate Nucleus Boundary
-----------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Right medullary arcuate nucleus** (this module) — a **caudal
    brainstem** nucleus at the **right ventral medullary surface**.

*   **Right hypothalamic arcuate nucleus** (infundibular nucleus)
    (``.../diencephalon/hypothalamus/right/``) — a **mediobasal
    hypothalamic** nucleus regulating **energy homeostasis**,
    **GnRH**, and **prolactin**.

**They share a NAME but are DIFFERENT STRUCTURES in DIFFERENT
CONTAINERS.** Consumers must **not** conflate the two — resolve
the **right hypothalamic** one via ``.../hypothalamus/right/``, and
the **right medullary** one via this module.

The Right Arcuate Nucleus / Right Ventrolateral Medulla Boundary
---------------------------------------------------------------
This is the **region / specific-nucleus** boundary:

*   **Right arcuate nucleus** (this module) — a **specific
    nucleus** at the right ventral medullary surface.

*   **Right ventrolateral medulla (VLM)** — a **region**
    containing the **right RVLM**, **right CVLM**, and the **right
    arcuate nucleus**.

**The right arcuate nucleus is a NUCLEUS within the right VLM
region, but it is NOT the whole right VLM.** Consumers must
**not** conflate the **right arcuate nucleus** with the **right
RVLM** or **right CVLM**.

The Right Arcuate Nucleus / Right RVLM Boundary
-----------------------------------------------
This is the **sympathetic-premotor** boundary:

*   **Right arcuate nucleus** (this module) — a **right
    ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``) —
    the **right sympathetic premotor / vasomotor center**.

**The right arcuate nucleus is NOT the right RVLM.** Consumers must
**not** conflate the two — the **right RVLM** provides **tonic
sympathetic drive**; the **right arcuate nucleus** is a
**chemosensory and hypothalamic-projecting** nucleus.

The Right Arcuate Nucleus / Right CVLM Boundary
-----------------------------------------------
This is the **sympathoinhibitory** boundary:

*   **Right arcuate nucleus** (this module) — a **right
    ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.

*   **Right CVLM** (``.../caudal_ventrolateral_medulla/right/``) —
    the **right sympathoinhibitory relay**.

**The right arcuate nucleus is NOT the right CVLM.** Consumers must
**not** conflate the two.

The Right Arcuate Nucleus / Right Retrotrapezoid Nucleus Boundary
-----------------------------------------------------------------
This is the **chemosensory-adjacency** boundary:

*   **Right arcuate nucleus** (this module) — a **caudal
    right ventral-surface chemosensory / hypothalamic-projecting**
    nucleus.

*   **Right retrotrapezoid nucleus** (RTN)
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/right/``)
    — a **more rostral** right ventral-surface **respiratory
    chemoreceptor**.

**Both are right ventral-surface chemosensory regions, but they
are DIFFERENT STRUCTURES.** Consumers must **not** conflate them.

The Right Arcuate Nucleus / Right Olivary Body Boundary
-------------------------------------------------------
This is the **cerebellar-relay** boundary:

*   **Right arcuate nucleus** (this module) — a **right
    ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.

*   **Right olivary body** (``.../olivary_body/right/``) — contains
    the **right inferior olivary nucleus** (source of **climbing
    fibers** to the right cerebellar hemisphere).

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
them.

The Right Arcuate Nucleus / Right Medullary Pyramid Boundary
------------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Right arcuate nucleus** (this module) — **grey-matter**
    nucleus at the right ventral medullary surface.

*   **Right medullary pyramid** (``.../medullary_pyramid/right/``) —
    **white-matter** right corticospinal / corticobulbar tract.

**They are ADJACENT but DIFFERENT** — the right arcuate nucleus
sits **at the right surface** near the right pyramid, but is **grey
matter**, not **white matter**. Consumers must **not** conflate
the two.

Function in the Human Brain
---------------------------
The right arcuate nucleus's functions are **right
ventral-surface chemosensory** and **hypothalamic-projecting** —
**NOT sympathetic premotor** and **NOT respiratory rhythm**:

*   **Central chemoreception (right ventral medullary surface):**
    The **right arcuate nucleus** — together with the **right
    ventral medullary surface** glia and the adjacent **right
    RTN** — contributes to **central CO₂/H⁺ chemoreception**.
    The **right ventral medullary surface** is a **chemosensory**
    region; the **right arcuate nucleus** is part of that region.

*   **Hypothalamic projection (right ventral medullary surface →
    hypothalamus):** The **right arcuate nucleus** projects
    **rostrally to the hypothalamus** (right preoptic area, right
    anterior hypothalamus, right lateral hypothalamus) via **right
    ventral medullary surface pathways**. These projections
    contribute to **neuroendocrine** and **autonomic**
    regulation — possibly including **fever**, **satiety**, and
    **stress responses**.

*   **Neurosecretion / CSF-contacting (right ventral medullary
    surface):** The **right arcuate nucleus** is a region of
    **CSF-contacting neurons** and **neurosecretory** cells at
    the right ventral surface — releasing substances into the
    **CSF** or **perivascular space**. This is **less
    characterized** in humans than the **hypothalamic**
    neurosecretory nuclei.

*   **NOT the hypothalamic arcuate nucleus functions:** The
    **energy homeostasis**, **GnRH**, and **prolactin**
    regulation are **hypothalamic arcuate nucleus** functions —
    **NOT** right medullary arcuate nucleus functions.

*   **NOT right sympathetic premotor:** The **right sympathetic
    premotor** function is the **right RVLM** — **NOT** the right
    arcuate nucleus.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the right arcuate nucleus.

**The unifying theme:** the right arcuate nucleus is a **right
ventral-surface chemosensory and hypothalamic-projecting** nucleus
of the **caudal medulla** — it is **NOT** the right hypothalamic
arcuate nucleus, **NOT** the right RVLM, **NOT** the right CVLM,
**NOT** the right RTN, and **NOT** the right olivary body. It is a
**specific right ventral-surface nucleus** with **chemosensory**
and **hypothalamic-projecting** roles.

Associated Disorders
--------------------
The right arcuate nucleus has **no named clinical syndrome** of its
own — its clinical associations are **indirect**:

*   **Central hypoventilation (via right ventral medullary surface
    chemoreception):** Dysfunction of the **right ventral medullary
    surface** chemosensory region — including the **right arcuate
    nucleus** and the **right RTN** — contributes to **central
    hypoventilation** (e.g., **CCHS**). The **right arcuate
    nucleus** is a **chemosensory** contributor, but the
    **primary rhythm generator** is the **pre-Bötzinger complex**
    (VRG).

*   **Sudden infant death syndrome (SIDS — via right ventral
    medullary surface abnormalities):** Abnormalities of the
    **right arcuate nucleus** and the **right ventral medullary
    surface** have been reported in **SIDS** — **reduced**
    **neurotransmitter** (e.g., **serotonin**) **binding** and
    **abnormal** **cytoarchitecture** in the right arcuate region.
    These findings are **contested** and **not specific** to the
    right arcuate nucleus.

*   **Neurogenic hypertension (via right ventrolateral medulla
    dysfunction):** The **right ventrolateral medulla** —
    including the **right RVLM** and adjacent **right arcuate**
    region — is involved in **neurogenic hypertension**. The
    **right arcuate nucleus** contributes to the **chemosensory**
    and **hypothalamic** aspects, but the **sympathetic premotor**
    role is the **right RVLM**.

*   **No Named "Right Arcuate Nucleus Syndrome":** The right
    arcuate nucleus is a **specific** but **functionally subtle**
    nucleus — it has **no named clinical syndrome**. Its clinical
    relevance is **indirect**, via **right ventral medullary
    surface** **chemosensory** and **hypothalamic-projecting**
    functions.

**What is NOT here:** The right arcuate nucleus is **not** the
substrate for **hypothalamic obesity** (right hypothalamic arcuate
nucleus), **Kallmann syndrome** (right hypothalamic arcuate nucleus
/ GnRH neurons), or **hyperprolactinemia** (right hypothalamic
arcuate nucleus / tuberoinfundibular dopamine neurons). Its
clinical relevance is the **right medullary** **chemosensory** and
**hypothalamic-projecting** functions listed above.

Lateralization Notes
--------------------
This is the **right** arcuate nucleus module. The arcuate nucleus
is a **bilateral container** whose two sides are **structurally
symmetric mirror pairs** — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **right** and **left** arcuate
    nuclei are **structurally symmetric** — they are **mirror
    pairs** with the **same** cytoarchitecture, **same**
    projections, and **same** functions. The **right** arcuate
    nucleus projects to the **right** hypothalamus and adjacent
    structures; the **left** arcuate nucleus projects to the
    **left** hypothalamus and adjacent structures.

*   **NO Lateralization Warning:** The arcuate nucleus has **no
    known functional lateralization** in humans. Consumers must
    **not** import a **lateralization warning** into the right
    arcuate nucleus — the **right** and **left** sides are
    **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right arcuate
    nucleus is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the right arcuate nucleus.

*   **NO Fear-Output Warning:** The right arcuate nucleus is **not**
    a fear-output structure — it is a **ventral-surface
    chemosensory and hypothalamic-projecting** nucleus. Consumers
    must **not** conflate it with the **central nucleus** or with
    the **amygdala**.

**A consumer that assumes "right arcuate nucleus = left arcuate
nucleus" will be structurally correct** — the two sides are
**symmetric** and **functionally equivalent**. The arcuate
nucleus is a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no
lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right arcuate nucleus is a
    **leaf** — it does **not** import from ``.../left/`` or any
    other left-side module. Bilateral relationships are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../ventral_respiratory_group/``, ``.../olivary_body/``,
    ``.../medullary_pyramid/``, or any other container. The right
    arcuate nucleus's relationships to the right RVLM, right CVLM,
    right RTN, right olivary body, right medullary pyramid, and
    right hypothalamic arcuate nucleus are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right arcuate
    nucleus is a **single structure** — it has **no structural
    children**. Consumers must **not** expect further sub-paths
    under ``.../right/``.
*   **NOT the left arcuate nucleus.** The left arcuate nucleus
    is a **separate leaf** under ``.../arcuate_nucleus/left/``.
    Consumers must **not** conflate the right with the left.
*   **NOT the hypothalamic arcuate nucleus.** The right
    hypothalamic arcuate nucleus (infundibular nucleus) is a
    **different structure** in a **different container**
    (``.../hypothalamus/right/``). Consumers must **not** conflate
    the two.
*   **NOT the right RVLM or right CVLM.** The right RVLM is the
    right sympathetic premotor center; the right CVLM is the right
    sympathoinhibitory relay. The right arcuate nucleus is a
    **ventral-surface chemosensory and hypothalamic-projecting**
    nucleus.
*   **NOT the right retrotrapezoid nucleus.** The right RTN is a
    **more rostral** respiratory chemoreceptor. The right arcuate
    nucleus is **caudal** to the right RTN.
*   **NOT the right olivary body.** The right olivary body is a
    cerebellar relay (right inferior olivary nucleus).
*   **NOT the right medullary pyramid.** The right pyramid is
    white-matter right corticospinal / corticobulbar tract; the
    right arcuate nucleus is grey matter.
*   **No ``AREA_PATHS`` hop.** The right arcuate nucleus is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The right arcuate nucleus has no
    nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the left arcuate nucleus — strict
    mirror with NO warning.** The right and left arcuate nucleus
    modules are **structurally identical** — same leaf status,
    same **chemosensory / hypothalamic-projecting** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.right"
    )

**Do not** assume the right arcuate nucleus is the **left arcuate
nucleus**. The left arcuate nucleus is the **separate leaf** at
``.../arcuate_nucleus/left/``.

**Do not** assume the right arcuate nucleus is the **right
hypothalamic arcuate nucleus**. The **right hypothalamic arcuate
nucleus** (infundibular nucleus) is a **different structure** in a
**different container** (``.../hypothalamus/right/``).

**Do not** assume the right arcuate nucleus is the **right RVLM**,
the **right CVLM**, the **right retrotrapezoid nucleus**, the
**right olivary body**, or the **right medullary pyramid**. Each is
a **different structure**.

**Do not** assume the right arcuate nucleus has **structural
children**. It is a **leaf** — it represents the right arcuate
nucleus as a **single structure**.

Iterating the right arcuate nucleus's (empty) children (recommended
consumer pattern)::

    RIGHT_ARCUATE_NUCLEUS_CHILDREN = ()
    # The right arcuate nucleus is a leaf. It has no structural
    # children.

Reaching the left arcuate nucleus (recommended consumer pattern
— the contralateral leaf)::

    # The left arcuate nucleus is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.left
    #
    # The right and left arcuate nuclei are structurally
    # symmetric mirror pairs.

Reaching the right hypothalamic arcuate nucleus (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The right hypothalamic arcuate nucleus (infundibular
    # nucleus) is NOT the right medullary arcuate nucleus:
    #
    #   diencephalon.hypothalamus.right.arcuate_nucleus
    #
    # It regulates energy homeostasis, GnRH, and prolactin —
    # functions DIFFERENT from the right medullary arcuate nucleus.

Reaching the right ventrolateral medulla components (recommended
consumer pattern — NOTE the region vs. specific-nucleus
distinction)::

    # The right RVLM and right CVLM are SEPARATE structures from
    # the right arcuate nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.right
    #
    # The right arcuate nucleus is a VENTRAL-SURFACE nucleus — it
    # is PART of the right ventrolateral medulla REGION, but it is
    # NOT the right RVLM or right CVLM.

Reaching the right retrotrapezoid nucleus (recommended consumer
pattern — NOTE the different structure)::

    # The right retrotrapezoid nucleus is:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus.right
    #
    # It is a MORE ROSTRAL respiratory chemoreceptor — DIFFERENT
    # from the caudal right arcuate nucleus.

Reaching the right olivary body and right medullary pyramid
(recommended consumer pattern — NOTE the different structures)::

    # The right olivary body and right medullary pyramid are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.right
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.right
    #
    # The right olivary body contains the right inferior olivary
    # nucleus (cerebellar climbing fibers); the right medullary
    # pyramid is the right corticospinal / corticobulbar tract.
    # Both are DIFFERENT from the right arcuate nucleus.

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