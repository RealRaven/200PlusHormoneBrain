"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
==================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── caudal_ventrolateral_medulla   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Caudal ventrolateral medulla; CVLM; caudal
ventrolateral medullary region; caudal ventrolateral medullary
depressor area; caudal pressor area (contested).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** — a group of **functionally
defined neurons** in the **caudal ventrolateral medulla**,
**ventral and lateral** to the **nucleus ambiguus** and the
**lateral reticular nucleus**, **caudal** to the **RVLM** and
**rostral** to the **spinomedullary junction**. It is a
**sympathoinhibitory relay** — the **CVLM** of the **medullary
autonomic circuit**.
**Part of:** The **medulla oblongata** — the **caudal
brainstem** subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each a
**leaf** representing the **left** or **right** CVLM. The
bilateral CVLM regions are the **structural children** of this
**bilateral container**; the container itself is **unpaired**.
**Boundary status (NOT the RVLM — the RVLM is the ROSTRAL
ventrolateral medulla):** **Boundary case — the CVLM is NOT the
RVLM.** The **RVLM** (``.../rostral_ventrolateral_medulla/``) is
the **rostral** ventrolateral medulla — the **sympathetic
premotor / vasomotor center** that provides **tonic excitatory
drive** to the **intermediolateral cell column**. The **CVLM**
(here) is the **caudal** ventrolateral medulla — the
**sympathoinhibitory relay** that **inhibits the RVLM**. **They
are DIFFERENT STRUCTURES at DIFFERENT rostrocaudal levels** — the
**RVLM** is **rostral**; the **CVLM** is **caudal**. Consumers
must **not** conflate the two — the **RVLM** **drives**
sympathetic outflow; the **CVLM** **inhibits** it.
**Boundary status (NOT the arcuate nucleus — a ventral-surface
nucleus):** **Boundary case — the CVLM is NOT the arcuate
nucleus.** The **arcuate nucleus** (``.../arcuate_nucleus/``) is a
**ventral-surface chemosensory and hypothalamic-projecting**
nucleus at the **ventral medullary surface**, adjacent to the
**anterior median fissure**. The **CVLM** (here) is a **more
lateral** ventrolateral medullary region — it is **NOT** the
arcuate nucleus. **They are DIFFERENT STRUCTURES** — the
**arcuate nucleus** is a **ventral-surface** nucleus; the **CVLM**
is a **ventrolateral** region. Consumers must **not** conflate
the two.
**Boundary status (NOT the solitary nucleus — the NTS is the
visceral afferent relay):** **Boundary case — the CVLM is NOT the
solitary nucleus.** The **solitary nucleus** (NTS)
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
it receives **baroreceptor**, **chemoreceptor**, and
**gastrointestinal** afferents. The **CVLM** (here) is the
**sympathoinhibitory relay** — it **receives NTS input** and
**inhibits the RVLM**. **They are DIFFERENT STRUCTURES** — the
**NTS** is the **afferent** relay; the **CVLM** is the
**sympathoinhibitory** relay. Consumers must **not** conflate the
two.
**Boundary status (NOT the retrotrapezoid nucleus — that is a
respiratory chemoreceptor):** **Boundary case — the CVLM is NOT
the retrotrapezoid nucleus.** The **retrotrapezoid nucleus**
(RTN) is a **more rostral** ventral-surface **respiratory
chemoreceptor** — it is wired under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/``. The
**CVLM** (here) is a **caudal ventrolateral** **sympathoinhibitory
relay**. **They are DIFFERENT STRUCTURES** — the **RTN** is a
**respiratory chemoreceptor**; the **CVLM** is a
**sympathoinhibitory** relay. Consumers must **not** conflate the
two.
**Boundary status (NOT the ventrolateral medulla as a whole — a
specific rostrocaudal subdivision):** **Boundary case — the CVLM
is NOT the whole ventrolateral medulla (VLM).** The
**ventrolateral medulla** is a **region** containing the
**RVLM**, the **CVLM**, and the **arcuate nucleus**. The **CVLM**
(here) is the **caudal** subdivision — it is **NOT** the whole
**VLM**, and it is **NOT** the **RVLM** or the **arcuate
nucleus**. Consumers must **not** conflate the **CVLM** with the
**whole ventrolateral medulla**.
**Boundary status (NOT the medullary pyramid — adjacent but
distinct):** **Boundary case — the CVLM is NOT the medullary
pyramid.** The **medullary pyramid** (``.../medullary_pyramid/``)
is the **corticospinal / corticobulbar tract** — a
**white-matter** structure at the **ventral medulla**. The
**CVLM** (here) is a **grey-matter** region in the **caudal
ventrolateral medulla**. **They are DIFFERENT STRUCTURES** — the
pyramid is **white matter** (descending motor fibers); the
**CVLM** is **grey matter** (neurons). Consumers must **not**
conflate the two.
**Boundary status (NOT the olivary body — adjacent but distinct):**
**Boundary case — the CVLM is NOT the olivary body.** The
**olivary body** (``.../olivary_body/``) contains the **inferior
olivary nucleus** — the **sole source of climbing fibers** to the
cerebellum. The **CVLM** (here) is a **ventrolateral medullary
sympathoinhibitory** region. **They are DIFFERENT STRUCTURES** —
the olivary body is a **cerebellar relay**; the **CVLM** is a
**sympathoinhibitory** relay. Consumers must **not** conflate the
two.
**Boundary status (NOT the nucleus ambiguus — adjacent but
distinct):** **Boundary case — the CVLM is NOT the nucleus
ambiguus.** The **nucleus ambiguus**
(``.../cranial_nerve_nuclei/nucleus_ambiguus/``) is a **branchial
motor** nucleus (CN IX/X/XI) **dorsal** to the CVLM. The **CVLM**
(here) is a **ventrolateral sympathoinhibitory** region. **They
are DIFFERENT STRUCTURES** — the nucleus ambiguus is a **motor
nucleus**; the **CVLM** is a **sympathoinhibitory** region.
Consumers must **not** conflate the two.
**Boundary status (NOT the spinal cord — that begins at the
foramen magnum):** **Boundary case — the CVLM is NOT the spinal
cord.** The **spinal cord** (``.../spinal_cord/``) is a
**separate container** beginning at the **foramen magnum**. The
**CVLM** (here) is a **medullary** region — its **caudal
boundary** is the **spinomedullary junction** (the **pyramidal
decussation**). Consumers must **not** conflate the **CVLM**
with the **spinal cord**.
**Boundary status (BILATERAL container — left and right are
structural children):** **Boundary case — the CVLM is a BILATERAL
container with ``left`` and ``right`` structural children.** The
**caudal_ventrolateral_medulla** module (here) is an **unpaired
container**; its **structural children** are ``left`` and
``right`` — each a **leaf** representing the **left** or
**right** CVLM. Consumers must **not** look for a single
unpaired CVLM — the **left** and **right** CVLM regions are
**separate modules** under this container. Resolve them via
``caudal_ventrolateral_medulla.left`` and
``caudal_ventrolateral_medulla.right``.

Overview
--------
The CVLM is the **caudal ventrolateral medulla** — the
**sympathoinhibitory relay** of the **medullary autonomic
circuit**. It lies **ventrolateral** in the **caudal medulla**,
**caudal** to the **RVLM** and **rostral** to the
**spinomedullary junction**, and it **inhibits the RVLM** in
response to **baroreceptor** and **visceral** input relayed by
the **NTS**.

**The CVLM is the CAUDAL ventrolateral medulla, NOT the rostral
one.** The **RVLM** is **rostral**; the **CVLM** is **caudal**.
**They are DIFFERENT STRUCTURES at DIFFERENT rostrocaudal
levels** — the **RVLM** **drives** sympathetic outflow; the
**CVLM** **inhibits** it.

**The CVLM is a BILATERAL container.** Its structural children
are ``left`` and ``right`` — each a leaf representing the left or
right CVLM. The **container itself** is **unpaired**.

**The CVLM is a SYMPATHOINHIBITORY RELAY, NOT a sympathoexcitatory
center.** It **inhibits** the **RVLM** — it **does not** drive
sympathetic outflow. This is the **opposite** of the **RVLM**,
which provides **tonic excitatory drive** to the
**intermediolateral cell column**.

**The CVLM is functionally coupled to the NTS and RVLM in the
medullary baroreflex circuit.** The **NTS** receives
**baroreceptor** afferents; the **CVLM** receives **NTS** input
and **inhibits the RVLM**; the **RVLM** drives **sympathetic
outflow**. This is the **medullary baroreflex arc** — a
**three-structure circuit** (NTS → CVLM → RVLM).

**The CVLM is NOT the arcuate nucleus, the RTN, the nucleus
ambiguus, the medullary pyramid, or the olivary body.** Each is a
**different structure** in the **caudal ventrolateral medulla
region**.

Bilateral Structure
-------------------
The CVLM is a **bilateral container** with **two structural
children**:

*   ``left`` — the **left** CVLM (a leaf module).
*   ``right`` — the **right** CVLM (a leaf module).

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left** and
**right** CVLM as **single structures**, not as further
sub-containers. Consumers that need **side-specific** resolution
should descend into ``left`` or ``right``; consumers that need
**bilateral** resolution should iterate over both.

**The container itself is unpaired.** There is **no**
``caudal_ventrolateral_medulla/left/.../`` structural hierarchy
beyond the single leaf level — the ``left`` and ``right`` modules
are the **terminal modules** for this structure.

The CVLM / RVLM Boundary
------------------------
This is the **most consequential** rostrocaudal boundary:

*   **CVLM** (this module) — the **caudal** ventrolateral medulla
    — the **sympathoinhibitory relay**.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) — the
    **rostral** ventrolateral medulla — the **sympathetic
    premotor / vasomotor center**.

**The two are ROSTROCAUDAL SIBLINGS of the ventrolateral medulla.**
The **RVLM** **drives** sympathetic outflow; the **CVLM**
**inhibits** it. Consumers must **not** conflate the two — the
**RVLM** is **rostral**; the **CVLM** is **caudal**.

The CVLM / NTS Boundary
-----------------------
This is the **autonomic-circuit** boundary:

*   **CVLM** (this module) — the **sympathoinhibitory relay**.

*   **NTS** (``.../solitary_nucleus/``) — the **visceral afferent
    relay**.

**The NTS is UPSTREAM of the CVLM in the medullary baroreflex
arc.** The **NTS** receives **baroreceptor** afferents and
**projects** to the **CVLM**; the **CVLM** **inhibits the
RVLM**. Consumers must **not** conflate the **NTS** with the
**CVLM** — the **NTS** is the **afferent** relay; the **CVLM**
is the **sympathoinhibitory** relay.

The CVLM / Arcuate Nucleus Boundary
-----------------------------------
This is the **ventral-surface** boundary:

*   **CVLM** (this module) — the **caudal ventrolateral medulla**
    (more **lateral**).

*   **Arcuate nucleus** (``.../arcuate_nucleus/``) — a
    **ventral-surface chemosensory and hypothalamic-projecting**
    nucleus (more **medial**, at the **ventral surface**).

**They are DIFFERENT STRUCTURES in the ventrolateral medullary
region.** Consumers must **not** conflate the **CVLM** with the
**arcuate nucleus**.

The CVLM / Retrotrapezoid Nucleus Boundary
------------------------------------------
This is the **respiratory-chemoreceptor** boundary:

*   **CVLM** (this module) — the **caudal ventrolateral
    sympathoinhibitory** relay.

*   **RTN** (``.../ventral_respiratory_group/retrotrapezoid_nucleus/``)
    — a **more rostral** ventral-surface **respiratory
    chemoreceptor**.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
them.

The CVLM / Medullary Pyramid and Olivary Body Boundary
------------------------------------------------------
This is the **grey-matter / white-matter and cerebellar-relay**
boundary:

*   **CVLM** (this module) — **grey-matter** region in the
    **caudal ventrolateral medulla**.

*   **Medullary pyramid** (``.../medullary_pyramid/``) —
    **white-matter** corticospinal / corticobulbar tract.

*   **Olivary body** (``.../olivary_body/``) — contains the
    **inferior olivary nucleus** (cerebellar climbing fibers).

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the **CVLM** with the **medullary pyramid** or the **olivary
body**.

The CVLM / Nucleus Ambiguus Boundary
------------------------------------
This is the **motor-nucleus** boundary:

*   **CVLM** (this module) — a **ventrolateral sympathoinhibitory**
    region.

*   **Nucleus ambiguus**
    (``.../cranial_nerve_nuclei/nucleus_ambiguus/``) — a
    **branchial motor** nucleus (CN IX/X/XI) **dorsal** to the
    CVLM.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
them.

Function in the Human Brain
---------------------------
The CVLM's function is **sympathoinhibition** in the **medullary
baroreflex circuit** — **NOT sympathetic premotor** and **NOT
respiratory rhythm**:

*   **Sympathoinhibition (medullary baroreflex):** The **CVLM**
    receives **glutamatergic** input from the **NTS** and
    **projects GABAergic inhibitory** fibers to the **RVLM** —
    **inhibiting** the **sympathetic premotor** neurons. This is
    the **medullary baroreflex arc** (NTS → CVLM → RVLM) that
    **buffers** blood pressure **fluctuations**.

*   **Baroreflex buffering:** The **CVLM** is the **key
    sympathoinhibitory** node in the **baroreflex** — it
    **reduces sympathetic outflow** when **blood pressure rises**,
    and it **withdraws** inhibition when **blood pressure falls**.
    This is a **critical** homeostatic mechanism.

*   **Visceral reflex integration:** The **CVLM** integrates
    **visceral** input from the **NTS** (baroreceptor,
    chemoreceptor, gastrointestinal) and **modulates** the
    **RVLM** sympathetic drive accordingly.

*   **NOT sympathetic premotor:** The **sympathetic premotor**
    function is the **RVLM** — **NOT** the CVLM.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** / **VRG** —
    **NOT** the CVLM.

*   **NOT chemosensory:** The **central chemoreception** function
    is the **ventral medullary surface** (arcuate nucleus, RTN) —
    **NOT** the CVLM.

**The unifying theme:** the CVLM is the **caudal ventrolateral
medulla** — the **sympathoinhibitory relay** that **buffers**
sympathetic outflow via the **medullary baroreflex arc** (NTS →
CVLM → RVLM). It is **NOT** the RVLM, **NOT** the NTS, **NOT**
the arcuate nucleus, **NOT** the RTN, and **NOT** the nucleus
ambiguus.

Associated Disorders
--------------------
The CVLM has **no named clinical syndrome** of its own — its
clinical associations are **indirect**:

*   **Neurogenic hypertension (via CVLM dysfunction):** Impaired
    **CVLM** sympathoinhibition — or impaired **NTS → CVLM**
    signaling — contributes to **sympathetic overactivity** and
    **neurogenic hypertension**. The **CVLM** is the
    **sympathoinhibitory** node; its dysfunction **reduces**
    baroreflex **buffering**.

*   **Baroreflex failure (via CVLM / NTS / RVLM circuit
    dysfunction):** Disruption of the **medullary baroreflex
    arc** — including the **CVLM** — causes **baroreflex
    failure** — **labile blood pressure**, **orthostatic
    hypotension**, and **hypertensive crises**.

*   **Brainstem stroke (via ventrolateral medullary
    infarction):** Infarction of the **caudal ventrolateral
    medulla** — adjacent to the **CVLM** — can cause
    **autonomic** and **cardiovascular** instability. The
    **CVLM** contributes to the **autonomic** component of
    **Wallenberg syndrome** (lateral medullary syndrome), though
    the **primary** lesion is in the **lateral medulla**
    structures (NTS, spinothalamic tract, nucleus ambiguus,
    inferior cerebellar peduncle).

*   **No Named "CVLM Syndrome":** The CVLM is a **functionally
    defined region** (not a sharply demarcated nucleus) — it has
    **no named clinical syndrome**. Its clinical relevance is
    **indirect**, via the **medullary baroreflex** circuit.

**What is NOT here:** The CVLM is **not** the substrate for
**central hypoventilation** (ventral medullary surface /
pre-Bötzinger complex), **Wallenberg syndrome** (lateral medulla
— NTS, nucleus ambiguus, spinothalamic tract), or
**neurogenic hypertension of the RVLM type** (RVLM). Its
clinical relevance is the **sympathoinhibitory** and
**baroreflex** functions listed above.

Lateralization Notes
--------------------
The CVLM is a **bilateral container** with ``left`` and ``right``
structural children. There is **no**
``caudal_ventrolateral_medulla/left/.../`` structural hierarchy
beyond the single leaf level.

*   **Bilateral structural children:** ``left`` and ``right`` are
    **leaf modules** — each represents the **left** or **right**
    CVLM as a **single structure**. Consumers resolve the
    **left** CVLM via ``caudal_ventrolateral_medulla.left`` and
    the **right** via ``caudal_ventrolateral_medulla.right``.

*   **Bilateral symmetry:** The **left** and **right** CVLM
    regions are **structurally symmetric** — they are **mirror
    pairs** with the **same** cytoarchitecture, **same**
    projections (ipsilateral to the RVLM), and **same**
    functions.

*   **Ipsilateral projection:** Each **CVLM** projects
    **ipsilaterally** to its **ipsilateral RVLM** —
    **left CVLM → left RVLM** and **right CVLM → right RVLM**.
    This is **functionally** an **ipsilateral** circuit; the
    bilateral **sympathoinhibition** is the **sum** of the two
    sides.

*   **NO lateralization warning:** The CVLM has **no known
    functional lateralization** in humans. Consumers must **not**
    import a **lateralization warning** into the CVLM — the
    **left** and **right** sides are **functionally symmetric**.

*   **NO extended-amygdala / fear-output / SLEA warnings:** The
    CVLM is **not** part of the amygdala, extended-amygdala, or
    SLEA continuum. It carries **no SLEA warning** and **no
    fear-output warning**. The **sympathoinhibitory** function is
    **autonomic**, not **fear-output**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The CVLM is a **bilateral
    container** — it does **not** import from ``left/`` or
    ``right/`` at the container level. The ``left`` and ``right``
    leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../rostral_ventrolateral_medulla/``,
    ``.../arcuate_nucleus/``, ``.../solitary_nucleus/``,
    ``.../ventral_respiratory_group/``, ``.../medullary_pyramid/``,
    ``.../olivary_body/``, ``.../cranial_nerve_nuclei/``, or any
    other container. The CVLM's relationships to the RVLM, NTS,
    arcuate nucleus, RTN, medullary pyramid, olivary body, and
    nucleus ambiguus are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children.** The structural
    children are ``left`` and ``right``, each a **leaf**. The
    container itself is **unpaired**.
*   **NOT the RVLM.** The RVLM is the **rostral** ventrolateral
    medulla — the **sympathetic premotor** center. The **CVLM**
    is the **caudal** ventrolateral medulla — the
    **sympathoinhibitory** relay. Consumers must **not** conflate
    the two.
*   **NOT the NTS.** The NTS is the **visceral afferent** relay;
    the **CVLM** is the **sympathoinhibitory** relay.
*   **NOT the arcuate nucleus.** The arcuate nucleus is a
    **ventral-surface chemosensory** nucleus; the **CVLM** is a
    **ventrolateral sympathoinhibitory** region.
*   **NOT the retrotrapezoid nucleus.** The RTN is a **respiratory
    chemoreceptor**; the **CVLM** is a **sympathoinhibitory**
    relay.
*   **NOT the medullary pyramid or the olivary body.** The
    pyramid is white-matter corticospinal / corticobulbar tract;
    the olivary body is a cerebellar relay. The **CVLM** is
    grey-matter ventrolateral medulla.
*   **NOT the nucleus ambiguus.** The nucleus ambiguus is a
    branchial motor nucleus; the **CVLM** is a sympathoinhibitory
    region.
*   **No ``AREA_PATHS`` hop.** The CVLM is a **local container** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The CVLM has no nested
    dual-framing module. It is a **bilateral container** with
    **two leaf children**.
*   **Structural parity with the right side — strict mirror.** The
    ``left`` and ``right`` leaves are **structurally identical**
    — same leaf status, same **sympathoinhibitory** framing, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import caudal_ventrolateral_medulla

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "caudal_ventrolateral_medulla"
    )

**Do not** assume the CVLM is the **RVLM**. The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **rostral**
ventrolateral medulla — the **sympathetic premotor** center. The
**CVLM** is the **caudal** ventrolateral medulla — the
**sympathoinhibitory** relay. They are **DIFFERENT STRUCTURES at
DIFFERENT rostrocaudal levels**.

**Do not** assume the CVLM is the **NTS**, the **arcuate
nucleus**, the **retrotrapezoid nucleus**, the **medullary
pyramid**, the **olivary body**, or the **nucleus ambiguus**.
Each is a **different structure**.

**Do not** look for a single unpaired CVLM. The **left** and
**right** CVLMs are **separate leaf modules** under this
container.

Iterating the CVLM's structural children (recommended consumer
pattern)::

    CAUDAL_VENTROLATERAL_MEDULLA_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # CVLM.

Reaching the left and right CVLMs (recommended consumer
pattern)::

    # The left and right CVLMs are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.left
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.right
    #
    # Each is a leaf module representing the CVLM of that side.

Reaching the RVLM (recommended consumer pattern — the ROSTRAL
sibling)::

    # The RVLM is the ROSTRAL ventrolateral medulla — the
    # sympathetic premotor / vasomotor center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #
    # The CVLM INHIBITS the RVLM via GABAergic projection. They
    # are DIFFERENT STRUCTURES at DIFFERENT rostrocaudal levels.

Reaching the NTS (recommended consumer pattern — the UPSTREAM
afferent)::

    # The NTS is the visceral afferent relay UPSTREAM of the
    # CVLM in the medullary baroreflex arc:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # Circuit: NTS -> CVLM -> RVLM -> intermediolateral cell
    # column. The CVLM is the SYMPATHOINHIBITORY node.

Reaching the arcuate nucleus (recommended consumer pattern —
NOTE the ventral-surface distinction)::

    # The arcuate nucleus is a VENTRAL-SURFACE chemosensory and
    # hypothalamic-projecting nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus
    #
    # The CVLM is more LATERAL in the caudal ventrolateral
    # medulla. They are DIFFERENT STRUCTURES.

Reaching the retrotrapezoid nucleus (recommended consumer
pattern — NOTE the respiratory-chemoreceptor distinction)::

    # The retrotrapezoid nucleus is a respiratory chemoreceptor:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus
    #
    # The CVLM is a sympathoinhibitory relay. They are DIFFERENT
    # STRUCTURES.

Reaching the nucleus ambiguus (recommended consumer pattern —
NOTE the motor-nucleus distinction)::

    # The nucleus ambiguus is a branchial motor nucleus (CN
    # IX/X/XI):
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.nucleus_ambiguus
    #
    # The CVLM is a sympathoinhibitory region. They are DIFFERENT
    # STRUCTURES.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"caudal_ventrolateral_medulla.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical medullary autonomic anatomy:** Blessing, W.W.
    (1997). *The Lower Brain Stem and Bodily Homeostasis.*
    (CVLM; RVLM; NTS; medullary baroreflex circuit; autonomic
    premotor organization.)
*   **CVLM and sympathoinhibition:** Schreihofer, A.M., Guyenet,
    P.G. (2000). "Role of the ventrolateral medulla in
    sympathoinhibition." *American Journal of Physiology*
    279:R1701–R1711. (CVLM as the sympathoinhibitory relay;
    GABAergic projection to RVLM.)
*   **RVLM and sympathetic premotor (contrast):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure." *Nature
    Reviews Neuroscience* 7:335–346. (RVLM; sympathetic premotor
    neurons — DIFFERENT from the CVLM.)
*   **NTS and visceral afferents (contrast — UPSTREAM of CVLM):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS as the
    visceral afferent relay — UPSTREAM of CVLM.)
*   **Medullary baroreflex circuit:** Dampney, R.A.L. (1994).
    "Functional organization of central pathways regulating the
    cardiovascular system." *Physiological Reviews* 74:323–364.
    (NTS → CVLM → RVLM baroreflex arc.)
*   **CVLM and baroreflex buffering:** Jeske, I., et al. (1995).
    "Contribution of the caudal ventrolateral medulla to the
    baroreflex." *American Journal of Physiology*
    269:R1003–R1010. (CVLM as the sympathoinhibitory node in the
    baroreflex.)
*   **Neurogenic hypertension (via CVLM dysfunction):** Guyenet,
    P.G. (2006). "The sympathetic control of blood pressure."
    *Nature Reviews Neuroscience* 7:335–346. (CVLM dysfunction
    and sympathetic overactivity.)
*   **Baroreflex failure:** Robertson, D., et al. (1993).
    "Baroreflex failure: a new syndrome of hypertension and
    hypotension." *Hypertension* 21:496–501. (Baroreflex failure
    — autonomic instability.)
*   **Brainstem stroke (contrast — Wallenberg syndrome):** Sacco,
    R.L., et al. (1993). "Lateral medullary infarction: clinical
    and MRI correlation." *Stroke* 24:1981–1987. (Wallenberg
    syndrome; lateral medullary lesion — CVLM-adjacent.)
*   **Medullary cytoarchitecture:** Paxinos, G., Huang, X.-F.
    (2013). *The Behaving Human Brain: A Cytoarchitectural
    Atlas.* (Medullary nuclei; ventrolateral medullary regions.)
*   **CVLM functional anatomy:** Dampney, R.A.L., et al. (2002).
    "Medullary and supramedullary mechanisms regulating
    sympathetic vasomotor tone." *Clinical and Experimental
    Pharmacology and Physiology* 30:6–12. (CVLM; RVLM; NTS;
    autonomic circuit.)
*   NeuroNames — Caudal ventrolateral medulla; FMA — Caudal
    ventrolateral medulla.
"""