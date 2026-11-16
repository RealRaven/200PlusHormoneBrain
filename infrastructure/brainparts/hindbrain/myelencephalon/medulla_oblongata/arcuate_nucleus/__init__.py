"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus
=====================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── arcuate_nucleus   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Arcuate nucleus of the medulla oblongata;
medullary arcuate nucleus; nucleus arcuatus medullae oblongatae;
ventral medullary surface (VMS) arcuate region.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** — a group of **small,
heterogeneous neurons and glia** at the **ventral medullary
surface** (VMS), adjacent to the **anterior median fissure** and
the **medullary pyramid**. It is **NOT** the **hypothalamic
arcuate nucleus** (infundibular nucleus) — a **different
structure** in a **different container**.
**Part of:** The **medulla oblongata** — the **caudal
brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each a
**leaf** representing the **left** or **right** arcuate nucleus.
The bilateral arcuate nuclei are the **structural children** of
this **bilateral container**; the container itself is **unpaired**.
**Boundary status (NOT the hypothalamic arcuate nucleus — a
DIFFERENT STRUCTURE with the SAME NAME):** **Boundary case — the
medullary arcuate nucleus is NOT the hypothalamic arcuate
nucleus.** The **hypothalamic arcuate nucleus** (infundibular
nucleus) is a **mediobasal hypothalamic** structure — part of the
**hypothalamus** (``.../diencephalon/hypothalamus/``) — and is the
**central regulator** of **energy homeostasis**, **GnRH
secretion**, and **prolactin** regulation. The **medullary
arcuate nucleus** (here) is a **caudal brainstem** structure at
the **ventral medullary surface** — it does **NOT** regulate
**energy homeostasis** or **reproduction**. **They share a NAME
but are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS.** Consumers
must **not** conflate the **medullary arcuate nucleus** with the
**hypothalamic arcuate nucleus** — resolve the hypothalamic one via
``.../hypothalamus/``.
**Boundary status (NOT the ventrolateral medulla as a whole — a
specific nucleus within the region):** **Boundary case — the
arcuate nucleus is NOT the ventrolateral medulla (VLM).** The
**ventrolateral medulla** is a **region** containing the **RVLM**
(``.../rostral_ventrolateral_medulla/``), the **CVLM**
(``.../caudal_ventrolateral_medulla/``), and the **arcuate
nucleus** (here). The **arcuate nucleus** is a **specific
nucleus** at the **ventral surface** — it is **NOT** the whole
**VLM**, and it is **NOT** the **RVLM** or **CVLM**. Consumers
must **not** conflate the **arcuate nucleus** with the **whole
ventrolateral medulla**.
**Boundary status (NOT the RVLM — the RVLM is the sympathetic
premotor / vasomotor center):** **Boundary case — the arcuate
nucleus is NOT the RVLM.** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor / vasomotor center** — it provides the **tonic
excitatory drive** to the **intermediolateral cell column**. The
**arcuate nucleus** (here) is a **ventral-surface chemosensory
and hypothalamic-projecting** nucleus — it is **NOT** the
**RVLM**. Consumers must **not** conflate the two.
**Boundary status (NOT the CVLM — the CVLM is the
sympathoinhibitory relay):** **Boundary case — the arcuate
nucleus is NOT the CVLM.** The **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory relay** — it receives **NTS** input and
**inhibits the RVLM**. The **arcuate nucleus** (here) is a
**ventral-surface chemosensory and hypothalamic-projecting**
nucleus — it is **NOT** the **CVLM**. Consumers must **not**
conflate the two.
**Boundary status (NOT the retrotrapezoid nucleus — adjacent but
distinct):** **Boundary case — the arcuate nucleus is NOT the
retrotrapezoid nucleus.** The **retrotrapezoid nucleus** (RTN)
is a **more rostral** ventral-surface **respiratory
chemoreceptor** — it is wired under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/``. The
**arcuate nucleus** (here) is a **more caudal** ventral-surface
chemosensory / hypothalamic-projecting nucleus. **Both are
ventral-surface chemosensory regions, but they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the two — the
**RTN** is a **respiratory chemoreceptor**; the **arcuate
nucleus** is a **hypothalamic-projecting chemosensory nucleus**.
**Boundary status (NOT the olivary body — adjacent but distinct):**
**Boundary case — the arcuate nucleus is NOT the olivary body.**
The **olivary body** (``.../olivary_body/``) contains the
**inferior olivary nucleus** — the **sole source of climbing
fibers** to the cerebellum. The **arcuate nucleus** (here) is a
**ventral-surface chemosensory / hypothalamic-projecting**
nucleus. **They are DIFFERENT STRUCTURES** — the olivary body is
a **cerebellar relay**; the arcuate nucleus is a
**ventral-surface nucleus**. Consumers must **not** conflate the
two.
**Boundary status (NOT the medullary pyramid — adjacent but
distinct):** **Boundary case — the arcuate nucleus is NOT the
medullary pyramid.** The **medullary pyramid**
(``.../medullary_pyramid/``) is the **corticospinal /
corticobulbar tract** — a **white-matter** structure at the
**ventral medulla**. The **arcuate nucleus** (here) is a
**grey-matter** nucleus at the **ventral medullary surface**,
**adjacent to** the pyramid. **They are DIFFERENT STRUCTURES** —
the pyramid is **white matter** (descending motor fibers); the
arcuate nucleus is **grey matter** (neurons and glia). Consumers
must **not** conflate the two.
**Boundary status (BILATERAL container — left and right are
structural children):** **Boundary case — the arcuate nucleus is
a BILATERAL container with ``left`` and ``right`` structural
children.** The **arcuate_nucleus** module (here) is an
**unpaired container**; its **structural children** are
``left`` and ``right`` — each a **leaf** representing the
**left** or **right** arcuate nucleus. Consumers must **not**
look for a single unpaired arcuate nucleus — the **left** and
**right** arcuate nuclei are **separate modules** under this
container. Resolve them via ``arcuate_nucleus.left`` and
``arcuate_nucleus.right``.

Overview
--------
The arcuate nucleus is the **ventral-surface chemosensory and
hypothalamic-projecting** nucleus of the **medulla oblongata**. It
lies at the **ventral medullary surface** (VMS), adjacent to the
**anterior median fissure** and the **medullary pyramid**, and
projects **rostrally to the hypothalamus**.

**The arcuate nucleus is the MEDULLARY arcuate nucleus, NOT the
hypothalamic one.** The **hypothalamic arcuate nucleus**
(infundibular nucleus) is a **different structure** in a
**different container** (``.../hypothalamus/``). It regulates
**energy homeostasis**, **GnRH**, and **prolactin**. The
**medullary arcuate nucleus** (here) is a **caudal brainstem**
nucleus involved in **central chemoreception** and
**hypothalamic projection**. **They share a NAME but are
DIFFERENT STRUCTURES.**

**The arcuate nucleus is a BILATERAL container.** Its structural
children are ``left`` and ``right`` — each a leaf representing
the left or right arcuate nucleus. The **container itself** is
**unpaired**.

**The arcuate nucleus is at the VENTRAL MEDULLARY SURFACE.** It is
**not** a deep medullary nucleus — it lies at the **surface**,
which is relevant for its **chemosensory** and
**neurosecretory** roles (it can sense **CSF** and **blood**
composition at the ventral surface).

**The arcuate nucleus is functionally adjacent to the RVLM and
CVLM, but is NOT the RVLM or CVLM.** It is a **separate
structure** with its own **hypothalamic-projecting** and
**chemosensory** roles.

Bilateral Structure
-------------------
The arcuate nucleus is a **bilateral container** with **two
structural children**:

*   ``left`` — the **left** arcuate nucleus (a leaf module).
*   ``right`` — the **right** arcuate nucleus (a leaf module).

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left** and
**right** arcuate nuclei as **single structures**, not as further
sub-containers. Consumers that need **side-specific** resolution
should descend into ``left`` or ``right``; consumers that need
**bilateral** resolution should iterate over both.

**The container itself is unpaired.** There is **no**
``arcuate_nucleus/left/.../`` structural hierarchy beyond the
single leaf level — the ``left`` and ``right`` modules are the
**terminal modules** for this structure.

The Arcuate Nucleus / Hypothalamic Arcuate Nucleus Boundary
-----------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Medullary arcuate nucleus** (this module) — a **caudal
    brainstem** nucleus at the **ventral medullary surface**.

*   **Hypothalamic arcuate nucleus** (infundibular nucleus)
    (``.../diencephalon/hypothalamus/``) — a **mediobasal
    hypothalamic** nucleus regulating **energy homeostasis**,
    **GnRH**, and **prolactin**.

**They share a NAME but are DIFFERENT STRUCTURES in DIFFERENT
CONTAINERS.** Consumers must **not** conflate the two — resolve
the **hypothalamic** one via ``.../hypothalamus/``, and the
**medullary** one via this module.

The Arcuate Nucleus / Ventrolateral Medulla Boundary
----------------------------------------------------
This is the **region / specific-nucleus** boundary:

*   **Arcuate nucleus** (this module) — a **specific nucleus** at
    the ventral medullary surface.

*   **Ventrolateral medulla (VLM)** — a **region** containing the
    **RVLM**, **CVLM**, and the **arcuate nucleus**.

**The arcuate nucleus is a NUCLEUS within the VLM region, but it
is NOT the whole VLM.** Consumers must **not** conflate the
**arcuate nucleus** with the **RVLM** or **CVLM**.

The Arcuate Nucleus / RVLM Boundary
-----------------------------------
This is the **sympathetic-premotor** boundary:

*   **Arcuate nucleus** (this module) — a **ventral-surface
    chemosensory and hypothalamic-projecting** nucleus.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) — the
    **sympathetic premotor / vasomotor center**.

**The arcuate nucleus is NOT the RVLM.** Consumers must **not**
conflate the two — the **RVLM** provides **tonic sympathetic
drive**; the **arcuate nucleus** is a **chemosensory and
hypothalamic-projecting** nucleus.

The Arcuate Nucleus / CVLM Boundary
-----------------------------------
This is the **sympathoinhibitory** boundary:

*   **Arcuate nucleus** (this module) — a **ventral-surface
    chemosensory and hypothalamic-projecting** nucleus.

*   **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **sympathoinhibitory relay**.

**The arcuate nucleus is NOT the CVLM.** Consumers must **not**
conflate the two.

The Arcuate Nucleus / Retrotrapezoid Nucleus Boundary
-----------------------------------------------------
This is the **chemosensory-adjacency** boundary:

*   **Arcuate nucleus** (this module) — a **caudal ventral-surface
    chemosensory / hypothalamic-projecting** nucleus.

*   **Retrotrapezoid nucleus** (RTN)
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/``) —
    a **more rostral** ventral-surface **respiratory
    chemoreceptor**.

**Both are ventral-surface chemosensory regions, but they are
DIFFERENT STRUCTURES.** Consumers must **not** conflate them.

The Arcuate Nucleus / Olivary Body Boundary
-------------------------------------------
This is the **cerebellar-relay** boundary:

*   **Arcuate nucleus** (this module) — a **ventral-surface
    chemosensory and hypothalamic-projecting** nucleus.

*   **Olivary body** (``.../olivary_body/``) — contains the
    **inferior olivary nucleus** (source of **climbing fibers**).

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
them.

The Arcuate Nucleus / Medullary Pyramid Boundary
------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Arcuate nucleus** (this module) — **grey-matter** nucleus at
    the ventral medullary surface.

*   **Medullary pyramid** (``.../medullary_pyramid/``) —
    **white-matter** corticospinal / corticobulbar tract.

**They are ADJACENT but DIFFERENT** — the arcuate nucleus sits
**at the surface** near the pyramid, but is **grey matter**, not
**white matter**. Consumers must **not** conflate the two.

Function in the Human Brain
---------------------------
The arcuate nucleus's functions are **ventral-surface
chemosensory** and **hypothalamic-projecting** — **NOT
sympathetic premotor** and **NOT respiratory rhythm**:

*   **Central chemoreception (ventral medullary surface):** The
    **arcuate nucleus** — together with the **ventral medullary
    surface** glia and the adjacent **RTN** — contributes to
    **central CO₂/H⁺ chemoreception**. The **ventral medullary
    surface** is a **chemosensory** region; the **arcuate
    nucleus** is part of that region.

*   **Hypothalamic projection (ventral medullary surface →
    hypothalamus):** The **arcuate nucleus** projects **rostrally
    to the hypothalamus** (preoptic area, anterior hypothalamus,
    lateral hypothalamus) via **ventral medullary surface
    pathways**. These projections contribute to
    **neuroendocrine** and **autonomic** regulation — possibly
    including **fever**, **satiety**, and **stress responses**.

*   **Neurosecretion / CSF-contacting (ventral medullary
    surface):** The **arcuate nucleus** is a region of
    **CSF-contacting neurons** and **neurosecretory** cells at
    the ventral surface — releasing substances into the **CSF**
    or **perivascular space**. This is **less characterized** in
    humans than the **hypothalamic** neurosecretory nuclei.

*   **NOT the hypothalamic arcuate nucleus functions:** The
    **energy homeostasis**, **GnRH**, and **prolactin**
    regulation are **hypothalamic arcuate nucleus** functions —
    **NOT** medullary arcuate nucleus functions.

*   **NOT sympathetic premotor:** The **sympathetic premotor**
    function is the **RVLM** — **NOT** the arcuate nucleus.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the arcuate nucleus.

**The unifying theme:** the arcuate nucleus is a **ventral-surface
chemosensory and hypothalamic-projecting** nucleus of the
**caudal medulla** — it is **NOT** the hypothalamic arcuate
nucleus, **NOT** the RVLM, **NOT** the CVLM, **NOT** the RTN, and
**NOT** the olivary body. It is a **specific ventral-surface
nucleus** with **chemosensory** and **hypothalamic-projecting**
roles.

Associated Disorders
--------------------
The arcuate nucleus has **no named clinical syndrome** of its own
— its clinical associations are **indirect**:

*   **Central hypoventilation (via ventral medullary surface
    chemoreception):** Dysfunction of the **ventral medullary
    surface** chemosensory region — including the **arcuate
    nucleus** and the **RTN** — contributes to **central
    hypoventilation** (e.g., **CCHS**). The **arcuate nucleus**
    is a **chemosensory** contributor, but the **primary rhythm
    generator** is the **pre-Bötzinger complex** (VRG).

*   **Sudden infant death syndrome (SIDS — via ventral medullary
    surface abnormalities):** Abnormalities of the **arcuate
    nucleus** and the **ventral medullary surface** have been
    reported in **SIDS** — **reduced** **neurotransmitter**
    (e.g., **serotonin**) **binding** and **abnormal**
    **cytoarchitecture** in the arcuate region. These findings
    are **contested** and **not specific** to the arcuate
    nucleus.

*   **Neurogenic hypertension (via ventrolateral medulla
    dysfunction):** The **ventrolateral medulla** — including the
    **RVLM** and adjacent **arcuate** region — is involved in
    **neurogenic hypertension**. The **arcuate nucleus**
    contributes to the **chemosensory** and **hypothalamic**
    aspects, but the **sympathetic premotor** role is the
    **RVLM**.

*   **No Named "Arcuate Nucleus Syndrome":** The arcuate nucleus
    is a **specific** but **functionally subtle** nucleus — it has
    **no named clinical syndrome**. Its clinical relevance is
    **indirect**, via **ventral medullary surface**
    **chemosensory** and **hypothalamic-projecting** functions.

**What is NOT here:** The arcuate nucleus is **not** the substrate
for **hypothalamic obesity** (hypothalamic arcuate nucleus),
**Kallmann syndrome** (hypothalamic arcuate nucleus / GnRH
neurons), or **hyperprolactinemia** (hypothalamic arcuate
nucleus / tuberoinfundibular dopamine neurons). Its clinical
relevance is the **medullary** **chemosensory** and
**hypothalamic-projecting** functions listed above.

Lateralization Notes
--------------------
The arcuate nucleus is a **bilateral container** with ``left``
and ``right`` structural children. There is **no**
``arcuate_nucleus/left/.../`` structural hierarchy beyond the
single leaf level.

*   **Bilateral structural children:** ``left`` and ``right`` are
    **leaf modules** — each represents the **left** or **right**
    arcuate nucleus as a **single structure**. Consumers resolve
    the **left** arcuate nucleus via ``arcuate_nucleus.left``
    and the **right** via ``arcuate_nucleus.right``.

*   **Bilateral symmetry:** The **left** and **right** arcuate
    nuclei are **structurally symmetric** — they are **mirror
    pairs** with the **same** cytoarchitecture, **same**
    projections, and **same** functions.

*   **NO lateralization warning:** The arcuate nucleus has **no
    known functional lateralization** in humans. Consumers must
    **not** import a **lateralization warning** into the arcuate
    nucleus — the **left** and **right** sides are
    **functionally symmetric**.

*   **NO extended-amygdala / fear-output / SLEA warnings:** The
    arcuate nucleus is **not** part of the amygdala,
    extended-amygdala, or SLEA continuum. It carries **no SLEA
    warning** and **no fear-output warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The arcuate nucleus is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../ventral_respiratory_group/``, ``.../olivary_body/``,
    ``.../medullary_pyramid/``, or any other container. The
    arcuate nucleus's relationships to the RVLM, CVLM, RTN,
    olivary body, medullary pyramid, and hypothalamic arcuate
    nucleus are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children.** The structural
    children are ``left`` and ``right``, each a **leaf**. The
    container itself is **unpaired**.
*   **NOT the hypothalamic arcuate nucleus.** The hypothalamic
    arcuate nucleus (infundibular nucleus) is a **different
    structure** in a **different container**
    (``.../hypothalamus/``). Consumers must **not** conflate the
    two.
*   **NOT the RVLM or CVLM.** The RVLM is the sympathetic
    premotor center; the CVLM is the sympathoinhibitory relay.
    The arcuate nucleus is a **ventral-surface chemosensory and
    hypothalamic-projecting** nucleus.
*   **NOT the retrotrapezoid nucleus.** The RTN is a **more
    rostral** respiratory chemoreceptor. The arcuate nucleus is
    **caudal** to the RTN.
*   **NOT the olivary body.** The olivary body is a cerebellar
    relay (inferior olivary nucleus).
*   **NOT the medullary pyramid.** The pyramid is white-matter
    corticospinal / corticobulbar tract; the arcuate nucleus is
    grey matter.
*   **No cross-listed leaf hop.** The arcuate nucleus is a
    **local container** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The arcuate nucleus has no
    nested dual-framing module. It is a **bilateral container**
    with **two leaf children**.
*   **Structural parity with the right side — strict mirror.** The
    ``left`` and ``right`` leaves are **structurally identical**
    — same leaf status, same chemosensory / hypothalamic-projecting
    framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import arcuate_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus"
    )

**Do not** assume the arcuate nucleus is the **hypothalamic
arcuate nucleus**. The **hypothalamic arcuate nucleus**
(infundibular nucleus) is a **different structure** in a
**different container** (``.../hypothalamus/``). The **medullary
arcuate nucleus** (here) is a **caudal brainstem** nucleus.

**Do not** assume the arcuate nucleus is the **RVLM**, the
**CVLM**, the **retrotrapezoid nucleus**, the **olivary body**,
or the **medullary pyramid**. Each is a **different structure**.

**Do not** look for a single unpaired arcuate nucleus. The
**left** and **right** arcuate nuclei are **separate leaf
modules** under this container.

Iterating the arcuate nucleus's structural children (recommended
consumer pattern)::

    ARCUATE_NUCLEUS_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # arcuate nucleus.

Reaching the left and right arcuate nuclei (recommended consumer
pattern)::

    # The left and right arcuate nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.left
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus.right
    #
    # Each is a leaf module representing the arcuate nucleus of
    # that side.

Reaching the hypothalamic arcuate nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The hypothalamic arcuate nucleus (infundibular nucleus) is
    # NOT the medullary arcuate nucleus:
    #
    #   diencephalon.hypothalamus.arcuate_nucleus
    #
    # It regulates energy homeostasis, GnRH, and prolactin —
    # functions DIFFERENT from the medullary arcuate nucleus.

Reaching the ventrolateral medulla components (recommended
consumer pattern — NOTE the region vs. specific-nucleus
distinction)::

    # The RVLM and CVLM are SEPARATE structures from the arcuate
    # nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #
    # The arcuate nucleus is a VENTRAL-SURFACE nucleus — it is
    # PART of the ventrolateral medulla REGION, but it is NOT the
    # RVLM or CVLM.

Reaching the retrotrapezoid nucleus (recommended consumer pattern
— NOTE the different structure)::

    # The retrotrapezoid nucleus is:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus
    #
    # It is a MORE ROSTRAL respiratory chemoreceptor — DIFFERENT
    # from the caudal arcuate nucleus.

Reaching the olivary body and medullary pyramid (recommended
consumer pattern — NOTE the different structures)::

    # The olivary body and medullary pyramid are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid
    #
    # The olivary body contains the inferior olivary nucleus
    # (cerebellar climbing fibers); the medullary pyramid is the
    # corticospinal / corticobulbar tract. Both are DIFFERENT from
    # the arcuate nucleus.

Bilateral iteration (recommended consumer pattern)::

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