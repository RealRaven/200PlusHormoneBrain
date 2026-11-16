"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center
=======================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center   <-- THIS MODULE
                ├── area_postrema
                │   ├── left
                │   └── right
                ├── chemoreceptor_trigger_zone
                │   ├── left
                │   └── right
                ├── cuneate_nucleus
                │   ├── left
                │   └── right
                ├── dorsal_respiratory_group
                │   ├── left
                │   └── right
                ├── gigantocellular_reticular_nucleus
                │   ├── left
                │   └── right
                └── gracile_nucleus
                    ├── left
                    └── right

**Primary synonym:** Respiratory center; medullary respiratory
center; respiratory control center; bulbar respiratory center;
ventral medullary respiratory chemosensory group (misleading —
the container also includes dorsal column nuclei).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter container** — the **tree's** grouping of
**respiratory**, **chemosensory / circumventricular**, and
**dorsal column somatosensory** nuclei in the **medulla
oblongata**. It is **NOT** a single anatomical nucleus, **NOT**
a single functional system, **NOT** the whole respiratory
network (the **ventral respiratory group** and the **RVLM / CVLM**
are **outside** this container), and **NOT** the **NTS /
solitary nucleus** (which is wired separately).
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Six —** each a **bilateral container**
with ``left/`` and ``right/`` leaf children:
1. ``area_postrema`` — **circumventricular organ** at the
   **caudal fourth ventricle floor** — **chemoreceptor trigger
   zone** for the **vomiting reflex**.
2. ``chemoreceptor_trigger_zone`` — **circumventricular organ**
   / **chemoreceptor** region — **often treated as synonymous
   with the area postrema** in the literature, but **wired as a
   separate child** in this tree.
3. ``cuneate_nucleus`` — **dorsal column nucleus** — **fine
   touch, vibration, and proprioception relay** from the **upper
   body** (somatosensory — **NOT** respiratory, but wired here
   per the tree).
4. ``dorsal_respiratory_group`` — **DRG** — the **dorsal
   respiratory** group of the **NTS region**, involved in
   **inspiratory pattern generation** (often considered **part
   of** the **NTS**).
5. ``gigantocellular_reticular_nucleus`` — **Gi** — the **large
   medullary reticular nucleus**, involved in **respiration**,
   **autonomic function**, and **descending pain modulation**
   (distinct from the **paramedian reticular nucleus**).
6. ``gracile_nucleus`` — **dorsal column nucleus** — **fine
   touch, vibration, and proprioception relay** from the **lower
   body** (somatosensory — **NOT** respiratory, but wired here
   per the tree).
**Boundary status (NOT a single functional system — a
HETEROGENEOUS container with THREE DIFFERENT functional systems
wired together):** **Boundary case — the respiratory_center is
NOT a single functional system.** It is a **tree container** that
groups **three different functional systems**:
*   **Respiratory** — the ``dorsal_respiratory_group`` and the
    ``gigantocellular_reticular_nucleus`` (the latter is
    **respiratory**, **autonomic**, and **pain-modulatory**).
*   **Chemosensory / circumventricular** — the ``area_postrema``
    and the ``chemoreceptor_trigger_zone`` (vomiting reflex,
    CSF-borne substance sensing).
*   **Dorsal column somatosensory** — the ``cuneate_nucleus`` and
    the ``gracile_nucleus`` (fine touch, vibration,
    proprioception).
**The container name "respiratory_center" is a TREE-WIRING
LABEL, NOT a claim that ALL SIX CHILDREN ARE RESPIRATORY.** The
**cuneate** and **gracile nuclei** are **somatosensory relays**
— they are **NOT respiratory** structures. **Consumers must not
infer function from container membership.** This is a
**deliberate design choice** — the tree groups these nuclei
under ``respiratory_center`` as a **pragmatic cluster** for
**brainstem organization**, but the **functional** distinctions
must be resolved by **descending into the individual leaf
modules**.
**Boundary status (NOT the whole respiratory network — the
ventral respiratory group and RVLM / CVLM are OUTSIDE this
container):** **Boundary case — the respiratory_center is NOT
the whole respiratory network.** The **ventral respiratory
group** (``.../ventral_respiratory_group/``) — which contains the
**Bötzinger complex**, **pre-Bötzinger complex**, **nucleus
para-ambiguus**, **nucleus retroambiguus**, **nucleus
retrofacialis**, and **retrotrapezoid nucleus** — is a
**separate container** under ``medulla_oblongata``. The **RVLM**
(``.../rostral_ventrolateral_medulla/``) and **CVLM**
(``.../caudal_ventrolateral_medulla/``) are **autonomic premotor
/ sympathoinhibitory** structures — **also outside** this
container. The **respiratory_center** (here) is only **part of**
the **broader respiratory** network. Consumers must **not**
conflate the **respiratory_center** with the **whole respiratory
network**.
**Boundary status (NOT the solitary nucleus / NTS — a SEPARATE
container):** **Boundary case — the respiratory_center is NOT
the solitary nucleus (NTS).** The **solitary nucleus**
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
**wired separately** under ``medulla_oblongata``. The
**dorsal_respiratory_group** child of **this container** is
**often considered part of** the **NTS region** — but in **this
tree**, the **NTS itself** is **NOT** a structural child of the
**respiratory_center**; only the **DRG** is. Consumers must
**not** expect to find the **solitary nucleus** under
``respiratory_center`` — resolve it via
``.../solitary_nucleus/``.
**Boundary status (NOT the ventral respiratory group — a
SEPARATE container):** **Boundary case — the respiratory_center
is NOT the ventral respiratory group (VRG).** The **VRG**
(``.../ventral_respiratory_group/``) is the **ventral
respiratory** rhythm and pattern generator group — **wired
separately** under ``medulla_oblongata``. The **respiratory_center**
(here) contains the **DRG** and the **Gi** — the **dorsal** and
**reticular** respiratory contributors — **NOT** the VRG.
Consumers must **not** conflate the two.
**Boundary status (NOT the RVLM or CVLM — autonomic structures):
** **Boundary case — the respiratory_center is NOT the RVLM or
CVLM.** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor** center; the **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay. Both are **autonomic** structures
— **NOT** respiratory_center children. Consumers must **not**
conflate the two.
**Boundary status (NOT the parafacial zone — a sleep-promoting
region):** **Boundary case — the respiratory_center is NOT the
parafacial zone.** The **parafacial zone**
(``.../parafacial_zone/``) is a **GABAergic / glycinergic
sleep-promoting** region — **NOT** a respiratory structure and
**NOT** wired under ``respiratory_center``. Consumers must
**not** conflate the two.
**Boundary status (NOT the paramedian reticular nucleus — a
SEPARATE reticular nucleus):** **Boundary case — the
respiratory_center is NOT the paramedian reticular nucleus.** The
**paramedian reticular nucleus**
(``.../paramedian_reticular_nucleus/``) is a **separate
reticular nucleus** — **NOT** wired under ``respiratory_center``.
The **gigantocellular reticular nucleus** (a child of
``respiratory_center``) is **larger**, **more lateral**, and
**different** from the **paramedian reticular nucleus**.
Consumers must **not** conflate the two.
**Boundary status (NOT the olivary body, medullary pyramid,
arcuate nucleus, cranial nerve nuclei, or other medullary
structures — DIFFERENT structures):** **Boundary case — the
respiratory_center is NOT these other medullary structures.**
Each is a **different structure** — see the respective modules.
Consumers must **not** conflate the **respiratory_center** with
any of these.
**Boundary status (NOT the whole medulla oblongata — a container
of six specific children):** **Boundary case — the
respiratory_center is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the cranial nerve nuclei, the
autonomic nuclei, the respiratory centers, the olivary body, the
medullary pyramid, the arcuate nucleus, the parafacial zone, the
paramedian reticular nucleus, the perihypoglossal nuclei, the
respiratory_center (here), and other structures. The
**respiratory_center** is **one container** — the **tree's
pragmatic cluster** of **six specific children**. Consumers must
**not** conflate the **respiratory_center** with the **whole
medulla**.
**Boundary status (BILATERAL container with TWO-LEVEL container
structure):** **Boundary case — the respiratory_center is a
BILATERAL container with a TWO-LEVEL container structure.** The
**respiratory_center** module (here) is an **unpaired
container**; its **structural children** are **six containers**
— each with its own ``left/`` and ``right/`` leaf children.
Consumers must **not** expect the nuclei to be wired **directly**
under ``respiratory_center`` — they are **under** the six
**intermediate** child containers, **each of which** has
``left/`` and ``right/`` leaf children. Resolve them via
``respiratory_center.<child>.{left,right}``.

Overview
--------
The **respiratory_center** container is the **tree's pragmatic
cluster** of **six medullary grey-matter nuclei / regions** that
are **associated** with **respiration**, **chemoreception /
circumventricular sensing**, and **dorsal column
somatosensory** relay. It is a **two-level container** — its
**six children** are **bilateral containers**, each with
``left/`` and ``right/`` leaf children.

**The respiratory_center is a HETEROGENEOUS container — its six
children belong to THREE DIFFERENT functional systems.** The
name "respiratory_center" is a **tree-wiring label**, **NOT** a
claim that **all six children** are respiratory. The **cuneate**
and **gracile nuclei** are **dorsal column somatosensory
relays** — **NOT** respiratory. The **area postrema** and
**chemoreceptor trigger zone** are **circumventricular /
chemoreceptive** — involved in **vomiting**, **NOT** primarily
in **breathing**. Only the **dorsal_respiratory_group** and
**gigantocellular reticular nucleus** are **directly**
**respiratory**-associated.

**The respiratory_center is NOT the whole respiratory network.**
The **ventral respiratory group** (VRG) — containing the
**Bötzinger**, **pre-Bötzinger**, **nucleus para-ambiguus**,
**nucleus retroambiguus**, **nucleus retrofacialis**, and
**retrotrapezoid nucleus** — is a **separate container** under
``medulla_oblongata``. The **RVLM** and **CVLM** — the
**autonomic premotor / sympathoinhibitory** nuclei — are also
**separate containers**. The **NTS / solitary nucleus** is
**separate**. The **respiratory_center** is **only part** of
the **broader** respiratory / autonomic / chemosensory network.

**The respiratory_center is a BILATERAL container with a
TWO-LEVEL container structure.** Its children are **six
bilateral containers** — each with **left** and **right** leaf
children. The **container itself** is **unpaired**.

**The respiratory_center is a NAME-COLLISION HAZARD.** The term
"respiratory center" is used **broadly** in the literature —
sometimes referring to the **DRG + VRG** collectively, sometimes
to the **pre-Bötzinger complex** specifically, sometimes to the
**whole ponto-medullary respiratory network**. **In this tree**,
the **respiratory_center** container is a **specific,
pragmatically-wired cluster** of **six children** — it is
**NOT** the **broader** "respiratory center" of the literature.
Consumers must **not** assume that the **respiratory_center**
container maps to any single **literature** notion of
"respiratory center".

Two-Level Container Structure
-----------------------------
The respiratory_center container has **six structural children**,
each a **bilateral container** with ``left/`` and ``right/`` leaf
children:

*   ``area_postrema`` (container) → ``left`` / ``right`` (leaves) —
    **circumventricular organ** — **vomiting reflex** trigger.
*   ``chemoreceptor_trigger_zone`` (container) → ``left`` /
    ``right`` (leaves) — **circumventricular organ /
    chemoreceptor** region — **often synonymous** with the **area
    postrema** in the literature, but **wired separately** in
    this tree.
*   ``cuneate_nucleus`` (container) → ``left`` / ``right``
    (leaves) — **dorsal column nucleus** — **fine touch,
    vibration, proprioception** from the **upper body**.
*   ``dorsal_respiratory_group`` (container) → ``left`` /
    ``right`` (leaves) — **DRG** — **dorsal respiratory**
    group of the **NTS region**.
*   ``gigantocellular_reticular_nucleus`` (container) → ``left``
    / ``right`` (leaves) — **Gi** — large medullary **reticular**
    nucleus — **respiratory**, **autonomic**, **pain-modulatory**.
*   ``gracile_nucleus`` (container) → ``left`` / ``right``
    (leaves) — **dorsal column nucleus** — **fine touch,
    vibration, proprioception** from the **lower body**.

**Two-level container structure:**
``respiratory_center`` → **six child containers** → ``left`` /
``right`` → **leaf nuclei**. Consumers that need
**nucleus-level** resolution descend into
``respiratory_center.<child>.{left,right}``; consumers that need
**child-level** resolution descend into
``respiratory_center.<child>``; consumers that need the
**whole container** use ``respiratory_center``.

**The cuneate and gracile nuclei are SOMATOSENSORY, NOT
respiratory.** The tree wires them under ``respiratory_center``
as a **pragmatic cluster** — **NOT** as a claim about function.
Consumers must **not** infer respiratory function from
membership in this container.

**The area postrema and chemoreceptor trigger zone are
CHEMOSENSORY / CIRCUMVENTRICULAR, NOT primarily respiratory.**
They are involved in the **vomiting reflex** and **CSF-borne
substance sensing** — **NOT** primarily in **breathing**. The
tree wires them under ``respiratory_center`` as a **pragmatic
cluster**.

The Respiratory Center / Ventral Respiratory Group Boundary
-----------------------------------------------------------
This is the **dorsal / ventral respiratory** boundary:

*   **Respiratory center** (this module) — the **tree's
    container** of **dorsal respiratory**, **circumventricular**,
    and **dorsal column** structures.

*   **Ventral respiratory group (VRG)**
    (``.../ventral_respiratory_group/``) — the **ventral
    respiratory** rhythm and pattern generator group
    (Bötzinger complex, pre-Bötzinger complex, nucleus
    para-ambiguus, nucleus retroambiguus, nucleus retrofacialis,
    retrotrapezoid nucleus).

**They are DIFFERENT CONTAINERS.** The **VRG** is a
**separate** container under ``medulla_oblongata`` — **NOT**
wired under ``respiratory_center``. Consumers must **not**
conflate the two.

The Respiratory Center / Solitary Nucleus Boundary
--------------------------------------------------
This is the **respiratory_center / NTS** boundary:

*   **Respiratory center** (this module) — contains the
    **dorsal_respiratory_group** child.

*   **Solitary nucleus (NTS)** (``.../solitary_nucleus/``) —
    the **visceral afferent relay**.

**They are DIFFERENT CONTAINERS.** The **NTS itself** is **NOT**
wired under ``respiratory_center`` — only the **DRG** is.
Consumers must **not** expect to find the NTS under
``respiratory_center``.

The Respiratory Center / RVLM and CVLM Boundary
-----------------------------------------------
This is the **respiratory_center / autonomic** boundary:

*   **Respiratory center** (this module) — the tree's
    cluster of **dorsal respiratory**, **circumventricular**, and
    **dorsal column** structures.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) and
    **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **sympathetic premotor** and **sympathoinhibitory** nuclei.

**They are DIFFERENT CONTAINERS.** Consumers must **not**
conflate the two.

The Respiratory Center / Area Postrema and Chemoreceptor Trigger Zone Boundary
------------------------------------------------------------------------------
This is the **within-container** naming boundary:

*   **Area postrema** (``respiratory_center.area_postrema``) —
    the **circumventricular organ** at the **caudal fourth
    ventricle floor**.

*   **Chemoreceptor trigger zone**
    (``respiratory_center.chemoreceptor_trigger_zone``) — the
    **chemoreceptor** region — **often treated as synonymous**
    with the **area postrema** in the **literature**.

**In this tree, they are TWO SEPARATE CHILDREN** — the tree
**wires** them as **different modules**, even though the
**literature** often treats them as **the same structure**.
Consumers must **not** conflate them **within the tree** —
resolve them via their **respective** paths.

The Respiratory Center / Cuneate and Gracile Nuclei Boundary
------------------------------------------------------------
This is the **somatosensory / respiratory** boundary (within the
container):

*   **Cuneate nucleus** and **gracile nucleus**
    (``respiratory_center.cuneate_nucleus`` and
    ``respiratory_center.gracile_nucleus``) — **dorsal column
    somatosensory** relays (fine touch, vibration,
    proprioception).

*   **Other respiratory_center children** — the **dorsal
    respiratory** and **circumventricular** structures.

**The cuneate and gracile nuclei are SOMATOSENSORY, NOT
respiratory.** They are wired under ``respiratory_center`` as a
**pragmatic cluster** — **NOT** as a claim about function.
Consumers must **not** infer respiratory function from
membership.

The Respiratory Center / Paramedian Reticular Nucleus Boundary
--------------------------------------------------------------
This is the **gigantocellular / paramedian** boundary:

*   **Gigantocellular reticular nucleus**
    (``respiratory_center.gigantocellular_reticular_nucleus``) —
    the **large**, **more lateral** medullary reticular nucleus
    — **wired here**.

*   **Paramedian reticular nucleus**
    (``.../paramedian_reticular_nucleus/``) — the **smaller**,
    **more medial** medullary reticular nucleus — **wired
    separately** under ``medulla_oblongata``.

**They are DIFFERENT RETICULAR NUCLEI.** Consumers must **not**
conflate the two.

The Respiratory Center / Other Medullary Structures Boundary
------------------------------------------------------------
This is the **respiratory_center / other medullary
structures** boundary:

*   **Respiratory center** (this module) — the tree's
    cluster of **six children**.

*   **Olivary body, medullary pyramid, arcuate nucleus, cranial
    nerve nuclei, parafacial zone, perihypoglossal nuclei** —
    **other medullary structures**.

**Each is a DIFFERENT STRUCTURE.** Consumers must **not** conflate
the **respiratory_center** with any of these.

Function in the Human Brain
---------------------------
The respiratory_center container's function is **heterogeneous**
— its **six children** subserve **three different functional
systems** — **NOT** a single uniform respiratory function:

*   **Respiratory (dorsal_respiratory_group, gigantocellular
    reticular nucleus):** The **dorsal_respiratory_group**
    participates in **inspiratory pattern generation**; the
    **gigantocellular reticular nucleus** participates in
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

*   **Chemosensory / circumventricular (area_postrema,
    chemoreceptor_trigger_zone):** The **area postrema** and
    **chemoreceptor trigger zone** are involved in the
    **vomiting reflex** and **CSF-borne substance sensing** —
    **NOT** primarily in **breathing**.

*   **Dorsal column somatosensory (cuneate_nucleus,
    gracile_nucleus):** The **cuneate** and **gracile nuclei**
    are **somatosensory relays** — they relay **fine touch,
    vibration, and proprioception** from the **body** (upper and
    lower, respectively) to the **contralateral thalamus** via
    the **medial lemniscus**. They are **NOT respiratory**.

**The unifying theme:** the respiratory_center is a **pragmatic
tree container** — it groups **six medullary nuclei** that are
**associated** with **respiration**, **chemoreception**, and
**somatosensory relay** — but it is **NOT a single functional
system**. Consumers must **descend into the individual leaf
modules** for **functional** resolution.

Associated Disorders
--------------------
The respiratory_center container's clinical relevance is
**heterogeneous** — its **six children** are associated with
**different clinical syndromes**:

*   **Central hypoventilation (via the dorsal respiratory group
    and gigantocellular reticular nucleus):** **Dysfunction** of
    the **dorsal respiratory group** and **gigantocellular
    reticular nucleus** can contribute to **central
    hypoventilation** — but the **primary** respiratory rhythm
    generators are the **pre-Bötzinger complex** (VRG) — **NOT**
    in this container.

*   **Vomiting and nausea (via area postrema and chemoreceptor
    trigger zone):** The **area postrema** and **chemoreceptor
    trigger zone** are the **direct substrate** of the
    **vomiting reflex** — involved in **chemotherapy-induced
    nausea and vomiting**, **area postrema syndrome** (e.g.,
    **neuromyelitis optica**), and **cyclic vomiting
    syndrome**.

*   **Dorsal column sensory loss (via cuneate and gracile
    nuclei):** The **cuneate** and **gracile nuclei** are the
    **first central relays** of the **dorsal column–medial
    lemniscus pathway** — their **dysfunction** (from
    **stroke**, **demyelination**, **tumor**, or **vitamin
    B12 deficiency** — subacute combined degeneration) causes
    **loss of fine touch, vibration, and proprioception** from
    the **body**.

*   **Pain modulation (via gigantocellular reticular
    nucleus):** The **gigantocellular reticular nucleus**
    participates in **descending pain modulation** — its
    **dysfunction** may contribute to **chronic pain**
    syndromes.

*   **No Named "Respiratory Center Syndrome":** The
    respiratory_center is a **heterogeneous tree container** —
    it has **no named clinical syndrome** of its own. Its
    clinical relevance is resolved **per child** — see the
    individual leaf modules.

Lateralization Notes
--------------------
The respiratory_center is a **bilateral container** with **six
bilateral child containers** — each with ``left`` and ``right``
leaf children.

*   **Bilateral structural children:** The **six child
    containers** (area_postrema, chemoreceptor_trigger_zone,
    cuneate_nucleus, dorsal_respiratory_group,
    gigantocellular_reticular_nucleus, gracile_nucleus) are each
    **bilateral containers** with ``left`` and ``right`` leaf
    children. Consumers resolve the nuclei via
    ``respiratory_center.<child>.{left,right}``.

*   **Bilateral symmetry:** Each **left** nucleus is
    **structurally symmetric** with its **right** counterpart
    — same cytoarchitecture, same projections (with some
    crossed / contralateral components), same functions.

*   **NO Lateralization Warning:** The respiratory_center
    **children** have **no known functional lateralization** at
    the **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the respiratory_center — the
    **left** and **right** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The
    respiratory_center is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the respiratory_center.

*   **NO Fear-Output Warning:** The respiratory_center is
    **not** a fear-output structure — its **children** are
    **respiratory**, **circumventricular**, and
    **somatosensory** structures. Consumers must **not** conflate
    it with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left respiratory_center = right
respiratory_center" will be structurally correct** — the two
sides are **symmetric** and **functionally equivalent** at the
**container level**. The respiratory_center is a
**strict-mirror container with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The respiratory_center is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The
    ``left`` and ``right`` leaves of each child are **independent**
    modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../ventral_respiratory_group/``,
    ``.../solitary_nucleus/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../parafacial_zone/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../olivary_body/``, ``.../medullary_pyramid/``,
    ``.../arcuate_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../perihypoglossal_nuclei/``, or any other container. The
    respiratory_center's relationships to the VRG, NTS, RVLM,
    CVLM, parafacial zone, paramedian reticular nucleus, olivary
    body, medullary pyramid, arcuate nucleus, cranial nerve
    nuclei, and perihypoglossal nuclei are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with six bilateral container children.** The
    structural children are the six **bilateral containers** —
    each with ``left`` / ``right`` leaf children. Consumers
    **should** descend into them for **nucleus-level**
    resolution.
*   **HETEROGENEOUS container — three functional systems.** The
    **cuneate** and **gracile nuclei** are **somatosensory**;
    the **area postrema** and **chemoreceptor trigger zone** are
    **circumventricular**; only the **DRG** and **Gi** are
    **directly respiratory**. Consumers must **not** infer
    **respiratory function** from container membership.
*   **NOT a single functional system.** The
    "respiratory_center" is a **tree-wiring label**, **NOT** a
    claim that **all six children** are respiratory.
*   **NOT the VRG.** The **ventral respiratory group** is a
    **separate container**.
*   **NOT the NTS.** The **solitary nucleus** is a **separate
    container** — only the **DRG** is a child of
    ``respiratory_center``.
*   **NOT the RVLM / CVLM.** Those are **autonomic** structures
    — **separate containers**.
*   **NOT the parafacial zone, paramedian reticular nucleus,
    olivary body, medullary pyramid, arcuate nucleus, cranial
    nerve nuclei, or perihypoglossal nuclei.** Each is a
    **different structure**.
*   **Area postrema and chemoreceptor trigger zone — often
    synonymous in the literature, but WIRED SEPARATELY in this
    tree.** Consumers must **not** conflate the two modules
    **within the tree**, even though they may represent the
    **same structure** in the **literature**.
*   **Gigantocellular vs. paramedian reticular nuclei — DIFFERENT
    reticular nuclei.** The **Gi** is a child of
    ``respiratory_center``; the **paramedian reticular nucleus**
    is a **separate container**.
*   **No ``AREA_PATHS`` hop.** The respiratory_center is a
    **local container** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The respiratory_center has no
    nested dual-framing module. It is a **container** with **six
    bilateral container children**, each with **two leaf
    children**.
*   **Structural parity with the right side — strict mirror.**
    Each ``left`` leaf is **structurally identical** to its
    ``right`` counterpart — same leaf status, same framing, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import respiratory_center

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.respiratory_center"
    )

**Do not** infer **respiratory function** from membership in the
respiratory_center. The **cuneate** and **gracile nuclei** are
**somatosensory relays**, and the **area postrema** and
**chemoreceptor trigger zone** are **circumventricular /
chemoreceptive** — **NOT** primarily respiratory. Only the
**DRG** and **Gi** are **directly** respiratory.

**Do not** expect the nuclei to be wired directly under
``respiratory_center``. The **six children** are **intermediate
bilateral containers** — the nuclei are **leaf children** of
those containers. Resolve them via
``respiratory_center.<child>.{left,right}``.

**Do not** assume the respiratory_center is the **ventral
respiratory group (VRG)**. The **VRG** is a **separate
container** under ``medulla_oblongata``.

**Do not** assume the respiratory_center is the **solitary
nucleus (NTS)**. The **NTS** is a **separate container** — only
the **dorsal_respiratory_group** is a child of
``respiratory_center``.

**Do not** assume the respiratory_center is the **RVLM** or
**CVLM**. Those are **autonomic** structures — **separate
containers**.

**Do not** assume the respiratory_center is the **parafacial
zone**, the **paramedian reticular nucleus**, the **olivary
body**, the **medullary pyramid**, the **arcuate nucleus**, the
**cranial nerve nuclei**, or the **perihypoglossal nuclei**.
Each is a **different structure**.

**Do not** conflate the **area_postrema** and
**chemoreceptor_trigger_zone** children — they are **wired
separately** in this tree, even though they may represent the
**same structure** in the literature.

Iterating the respiratory_center's structural children
(recommended consumer pattern)::

    RESPIRATORY_CENTER_CHILDREN = (
        "area_postrema",
        "chemoreceptor_trigger_zone",
        "cuneate_nucleus",
        "dorsal_respiratory_group",
        "gigantocellular_reticular_nucleus",
        "gracile_nucleus",
    )
    # Each child is a BILATERAL CONTAINER with left/ and right/
    # leaf children.

Iterating the leaf modules per child (recommended consumer
pattern)::

    for child in RESPIRATORY_CENTER_CHILDREN:
        for side in ("left", "right"):
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"respiratory_center.{child}.{side}"
            )
            # resolve path through the memory/recall layer

Reaching the ventral respiratory group (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The ventral respiratory group is a SEPARATE container under
    # medulla_oblongata — NOT wired under respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #
    # The respiratory_center and the VRG are DIFFERENT
    # containers — the VRG contains the respiratory rhythm and
    # pattern generators (Bötzinger, pre-Bötzinger, nucleus
    # para-ambiguus, nucleus retroambiguus, nucleus retrofacialis,
    # retrotrapezoid nucleus).

Reaching the solitary nucleus (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The solitary nucleus (NTS) is a SEPARATE container under
    # medulla_oblongata — only the dorsal_respiratory_group is a
    # child of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # The NTS is the visceral afferent relay — it is NOT wired
    # under respiratory_center.

Reaching the RVLM and CVLM (recommended consumer pattern — NOTE
the DIFFERENT containers)::

    # The RVLM and CVLM are autonomic structures — SEPARATE
    # containers under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #
    # They are NOT wired under respiratory_center.

Reaching the paramedian reticular nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The paramedian reticular nucleus is a DIFFERENT reticular
    # nucleus, wired separately under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.paramedian_reticular_nucleus
    #
    # The gigantocellular reticular nucleus (a child of
    # respiratory_center) and the paramedian reticular nucleus
    # are DIFFERENT RETICULAR NUCLEI.

Bilateral iteration (recommended consumer pattern — for
consumers that need both sides and all six children)::

    for child in RESPIRATORY_CENTER_CHILDREN:
        for side in ("left", "right"):
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"respiratory_center.{child}.{side}"
            )
            # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Medullary respiratory centers; dorsal respiratory group;
    gigantocellular reticular nucleus; area postrema; dorsal
    column nuclei.)
*   **Dorsal respiratory group:** Feldman, J.L., Del Negro, C.A.
    (2006). "Looking for inspiration: new perspectives on
    respiratory rhythm." *Nature Reviews Neuroscience* 7:232–242.
    (Dorsal respiratory group; inspiratory pattern generation;
    NTS region.)
*   **Gigantocellular reticular nucleus:** Newman, D.B. (1985).
    "Distinguishing rat medullary reticular formation regions by
    afferent and efferent connections." *Brain Research*
    326:129–138. (Gigantocellular reticular nucleus; respiratory,
    autonomic, and pain-modulatory functions.)
*   **Area postrema — chemoreceptor trigger zone:** Miller, A.D.,
    Leslie, R.A. (1994). "The area postrema and vomiting."
    *Frontiers in Neuroendocrinology* 15:301–320. (Area
    postrema; chemoreceptor trigger zone; vomiting reflex.)
*   **Area postrema — neuromyelitis optica:** Pittock, S.J., et
    al. (2010). "Neuromyelitis optica brain lesions localized at
    sites of high aquaporin 4 expression." *Archives of
    Neurology* 63:964–968. (Area postrema syndrome in NMO.)
*   **Cuneate nucleus — dorsal column:** Tracey, D.J. (2004).
    "Ascending and descending pathways." In: Paxinos, G. (ed.),
    *The Rat Nervous System*, 3rd ed. (Cuneate nucleus; dorsal
    column–medial lemniscus pathway.)
*   **Gracile nucleus — dorsal column:** Tracey, D.J. (2004).
    "Ascending and descending pathways." In: Paxinos, G. (ed.),
    *The Rat Nervous System*, 3rd ed. (Gracile nucleus; dorsal
    column–medial lemniscus pathway.)
*   **Subacute combined degeneration — dorsal column:** Hemmer,
    B., et al. (1998). "Subacute combined degeneration: clinical,
    electrophysiological, and magnetic resonance imaging
    findings." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 65:822–827. (Vitamin B12 deficiency; dorsal
    column dysfunction; cuneate and gracile nuclei.)
*   **Descending pain modulation — gigantocellular reticular
    nucleus:** Basbaum, A.I., Fields, H.L. (1984). "Endogenous
    pain control systems: brainstem spinal pathways and endorphin
    circuitry." *Annual Review of Neuroscience* 7:309–338.
    (Descending pain modulation; medullary reticular nuclei
    including the gigantocellular reticular nucleus.)
*   **Ventral respiratory group (contrast — separate container):**
    Feldman, J.L., Del Negro, C.A. (2006). "Looking for
    inspiration: new perspectives on respiratory rhythm."
    *Nature Reviews Neuroscience* 7:232–242. (Ventral respiratory
    group; pre-Bötzinger complex — separate from the respiratory
    center container.)
*   **Solitary nucleus (contrast — separate container):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS — separate from
    the respiratory center container.)
*   **RVLM and CVLM (contrast — separate containers):** Guyenet,
    P.G. (2006). "The sympathetic control of blood pressure."
    *Nature Reviews Neuroscience* 7:335–346. (RVLM; CVLM —
    separate from the respiratory center container.)
*   **Paramedian reticular nucleus (contrast — separate
    container):** Newman, D.B., Ginsberg, C.Y. (1992). "Brainstem
    reticular nuclei of the cat: I. Sources of the
    reticulocerebellar projection." *Neuroscience* 47:149–168.
    (Paramedian reticular nucleus — distinct from the
    gigantocellular reticular nucleus.)
*   NeuroNames — Respiratory center; FMA — Respiratory center.
"""