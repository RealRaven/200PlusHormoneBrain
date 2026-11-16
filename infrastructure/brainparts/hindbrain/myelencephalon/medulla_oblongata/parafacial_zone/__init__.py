"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.parafacial_zone
=====================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── parafacial_zone   <-- THIS MODULE

**Primary synonym:** Parafacial zone; PZ; parafacial zone of the
medulla; parafacial sleep-promoting zone; Anaclet parafacial zone;
GABAergic parafacial zone; "the parafacial zone proper" (to
distinguish it from the parafacial respiratory group).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** at the **ponto-medullary
junction** — a **GABAergic / glycinergic** neuronal population
**ventral and lateral** to the **facial nucleus (VII)** and
**adjacent** to the **rostral ventrolateral medulla**. It is a
**sleep-promoting center**, **NOT** a respiratory rhythm
generator, **NOT** an autonomic premotor center, and **NOT** the
**parafacial respiratory group (pFRG)** — though the two are
**anatomically adjacent** and are **frequently conflated** in the
older literature.
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **None.** This is a **leaf** module. The
parafacial zone is represented as a **single structure** — it
has **no structural children**. It is a **bilateral** structure
in the brain, but in this tree it is wired as a **single leaf**
(rather than as a bilateral container with ``left`` and ``right``
children). Consumers that need **side-specific** resolution
should consult the references; the tree does **not** split it.
**Boundary status (NOT the parafacial respiratory group — a
DIFFERENT structure with a SIMILAR name):** **Boundary case —
the parafacial zone (PZ) is NOT the parafacial respiratory group
(pFRG).** The **parafacial respiratory group (pFRG)** is a
**respiratory** structure in the **rostral ventrolateral
medulla** — it contains **pre-inspiratory** and
**expiratory-modulating** neurons that are **active during high
metabolic demand** (exercise, hypercapnia), and it is **often
grouped** with the **retrotrapezoid nucleus (RTN)** as the
**RTN/pFRG** **central chemoreceptor** complex. The **parafacial
zone (PZ)** (here) is a **GABAergic / glycinergic
sleep-promoting** region — it is **active during NREM sleep**
and **promotes slow-wave sleep**. **They share the name
"parafacial" but are DIFFERENT STRUCTURES with DIFFERENT
FUNCTIONS** — the **pFRG** is **respiratory**; the **PZ** is
**sleep-promoting**. Consumers must **not** conflate the two.
**Boundary status (NOT the retrotrapezoid nucleus — a DIFFERENT
structure with a DIFFERENT function):** **Boundary case — the
parafacial zone is NOT the retrotrapezoid nucleus.** The
**retrotrapezoid nucleus (RTN)**
(``.../ventral_respiratory_group/retrotrapezoid_nucleus/``) is a
**respiratory chemoreceptor** at the **ventral medullary
surface** — it senses **CO₂/H⁺** and **drives breathing**. The
**parafacial zone** (here) is a **sleep-promoting** region —
it is **NOT** a respiratory chemoreceptor. They are
**anatomically adjacent** in the **rostral ventrolateral
medulla**, but they are **functionally distinct**. Consumers
must **not** conflate the two.
**Boundary status (NOT the RVLM — a DIFFERENT structure with a
DIFFERENT function):** **Boundary case — the parafacial zone is
NOT the rostral ventrolateral medulla (RVLM).** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor / vasomotor** center — it provides **tonic
excitatory drive** to the **intermediolateral cell column**. The
**parafacial zone** (here) is a **sleep-promoting** region — it
is **NOT** an autonomic premotor center. They are **anatomically
adjacent** in the **rostral ventrolateral medulla**, but they
are **functionally distinct**. Consumers must **not** conflate
the two.
**Boundary status (NOT the CVLM — a DIFFERENT structure with a
DIFFERENT function):** **Boundary case — the parafacial zone is
NOT the caudal ventrolateral medulla (CVLM).** The **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay. The **parafacial zone** (here) is
a **sleep-promoting** region. Consumers must **not** conflate
the two — they are at **different rostrocaudal levels** and have
**different functions**.
**Boundary status (NOT the facial nucleus — a DIFFERENT structure
in the PONS):** **Boundary case — the parafacial zone is NOT the
facial nucleus.** The **facial nucleus (VII)**
(``.../metencephalon/pons/cranial_nerve_nuclei/facial_nerve_nucleus/``)
is a **branchial motor** nucleus in the **pons** — it supplies
the **muscles of facial expression**. The **parafacial zone**
(here) is **ventral and lateral** to the facial nucleus — it is
**named after** its **position beside** the facial nucleus
("parafacial" = "beside the facial nucleus"). But it is a
**DIFFERENT STRUCTURE** with a **DIFFERENT function** — the
facial nucleus is **motor**; the parafacial zone is
**sleep-promoting**. Consumers must **not** conflate the two.
**Boundary status (NOT the ventral respiratory group — a
DIFFERENT respiratory structure):** **Boundary case — the
parafacial zone is NOT the ventral respiratory group (VRG).**
The **VRG** (``.../ventral_respiratory_group/``) contains the
**Bötzinger complex**, **pre-Bötzinger complex**, **nucleus
para-ambiguus**, **nucleus retroambiguus**, **nucleus
retrofacialis**, and **retrotrapezoid nucleus** — the
**respiratory rhythm** and **pattern** generators. The
**parafacial zone** (here) is a **sleep-promoting** region —
**NOT** a respiratory rhythm generator. Consumers must **not**
conflate the two.
**Boundary status (NOT the dorsal respiratory group or other
respiratory_center nuclei — a DIFFERENT structure):** **Boundary
case — the parafacial zone is NOT the respiratory_center
structures.** The **respiratory_center**
(``.../respiratory_center/``) contains the **dorsal respiratory
group**, **area postrema**, **chemoreceptor trigger zone**,
**gracile nucleus**, **cuneate nucleus**, and **gigantocellular
reticular nucleus** — the **dorsal respiratory** and
**chemosensory** structures. The **parafacial zone** (here) is a
**sleep-promoting** region — **NOT** a respiratory or
chemosensory structure. Consumers must **not** conflate the
two.
**Boundary status (NOT the solitary nucleus — a DIFFERENT
structure):** **Boundary case — the parafacial zone is NOT the
solitary nucleus.** The **solitary nucleus (NTS)**
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
it receives **taste**, **baroreceptor**, **chemoreceptor**, and
**gastrointestinal** afferents. The **parafacial zone** (here)
is a **sleep-promoting** region — **NOT** a visceral afferent
relay. Consumers must **not** conflate the two.
**Boundary status (NOT the medullary pyramid — a DIFFERENT
structure):** **Boundary case — the parafacial zone is NOT the
medullary pyramid.** The **medullary pyramid**
(``.../medullary_pyramid/``) is the **ventral white-matter**
corticospinal / corticobulbar tract. The **parafacial zone**
(here) is a **grey-matter** sleep-promoting region. Consumers
must **not** conflate the two.
**Boundary status (NOT the olivary body — a DIFFERENT
structure):** **Boundary case — the parafacial zone is NOT the
olivary body.** The **olivary body** (``.../olivary_body/``) is
the **cerebellar climbing-fiber relay**. The **parafacial
zone** (here) is a **sleep-promoting** region. Consumers must
**not** conflate the two.
**Boundary status (NOT the arcuate nucleus — a DIFFERENT
structure):** **Boundary case — the parafacial zone is NOT the
arcuate nucleus.** The **arcuate nucleus**
(``.../arcuate_nucleus/``) is a **ventral-surface chemosensory
and hypothalamic-projecting** nucleus. The **parafacial zone**
(here) is a **sleep-promoting** region. Consumers must **not**
conflate the two.
**Boundary status (NOT the cranial nerve nuclei — DIFFERENT
structures):** **Boundary case — the parafacial zone is NOT the
cranial nerve nuclei.** The **cranial nerve nuclei**
(``.../cranial_nerve_nuclei/``) are the **medullary motor**
nuclei (hypoglossal, dorsal motor vagus, inferior salivatory,
nucleus ambiguus). The **parafacial zone** (here) is a
**sleep-promoting** region — **NOT** a cranial nerve motor
nucleus. Consumers must **not** conflate the two.
**Boundary status (NOT the whole medulla oblongata — a small
grey-matter region within it):** **Boundary case — the
parafacial zone is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the cranial nerve nuclei, the
autonomic nuclei, the respiratory centers, the olivary body, the
medullary pyramid, the arcuate nucleus, the parafacial zone
(here), and other structures. The **parafacial zone** is **one
small grey-matter region** within the medulla. Consumers must
**not** conflate the **parafacial zone** with the **whole
medulla**.
**Boundary status (BILATERAL in the brain — but a SINGLE LEAF in
this tree):** **Boundary case — the parafacial zone is a
BILATERAL structure in the brain, but it is wired as a SINGLE
LEAF in this tree.** The parafacial zone exists **bilaterally**
in the medulla — a **left** and **right** parafacial zone —
but the tree does **not** split it into ``left`` and ``right``
modules. Consumers that need **side-specific** resolution should
**consult the references**; the tree represents the parafacial
zone as a **single structure**. This is a **deliberate design
choice** — the parafacial zone's function (sleep promotion) is
**not obviously lateralized** in humans, and the tree does not
carry a lateralization warning for it.

Overview
--------
The **parafacial zone (PZ)** is a **GABAergic / glycinergic**
grey-matter region at the **ponto-medullary junction** —
**ventral and lateral** to the **facial nucleus (VII)** and
**adjacent** to the **rostral ventrolateral medulla (RVLM)**. It
is a **sleep-promoting center** — it is **active during NREM
sleep**, and it **promotes slow-wave sleep (SWS)** by
**inhibiting** the **wake-promoting** systems of the **basal
forebrain**, **lateral hypothalamus**, and **brainstem**.

**The parafacial zone is the SLEEP-PROMOTING parafacial zone,
NOT the parafacial respiratory group.** The **parafacial
respiratory group (pFRG)** is a **respiratory** structure —
part of the **RTN/pFRG** **central chemoreceptor** complex —
**NOT** a sleep-promoting center. **They share the name
"parafacial" but are DIFFERENT STRUCTURES with DIFFERENT
FUNCTIONS** — the **pFRG** is **respiratory**; the **PZ** is
**sleep-promoting**. In older literature, the two are
**frequently conflated**; modern work (Anaclet et al., 2012)
has **dissociated** them.

**The parafacial zone is a LEAF module in this tree.** It is
**bilateral** in the brain, but the tree represents it as a
**single structure** — **no** ``left`` / ``right`` split. This
is a **deliberate design choice** — see *Lateralization Notes*.

**The parafacial zone is a GREY-MATTER sleep-promoting region,
NOT a respiratory rhythm generator, NOT an autonomic premotor
center, and NOT a cranial nerve motor nucleus.** It
**contains** a **GABAergic / glycinergic** neuronal population
that **projects** to the **basal forebrain**, the **lateral
hypothalamus** (including **MCH neurons**), and other
**wake-promoting** centers, and it **promotes NREM sleep**.

**The parafacial zone is a NAME-COLLISION HAZARD.** The name
"parafacial" appears in **two different structures** — the
**parafacial zone (PZ)** and the **parafacial respiratory group
(pFRG)** — and the two are **often conflated** in the
literature. Consumers must **not** import the **respiratory**
function of the **pFRG** into the **parafacial zone** — the
parafacial zone is a **sleep-promoting** center.

The Parafacial Zone / Parafacial Respiratory Group Boundary
-----------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Parafacial zone (PZ)** (this module) — the **sleep-promoting**
    GABAergic region.

*   **Parafacial respiratory group (pFRG)** — the **respiratory**
    structure in the **rostral ventrolateral medulla** (often
    grouped with the **RTN** as the **RTN/pFRG** complex).

**They share the name "parafacial" but are DIFFERENT STRUCTURES
with DIFFERENT FUNCTIONS.** The **pFRG** is **respiratory**
(active expiration, pre-inspiratory neurons); the **PZ** is
**sleep-promoting**. Consumers must **not** conflate the two.
Note that the **pFRG** is **not** wired as a **separate module**
in this tree — it is **anatomically adjacent** to the
**retrotrapezoid nucleus** under
``.../ventral_respiratory_group/retrotrapezoid_nucleus/``, and
it is **documented there** as part of the **RTN/pFRG** complex.

The Parafacial Zone / Retrotrapezoid Nucleus Boundary
-----------------------------------------------------
This is the **sleep / respiratory-chemoreceptor** boundary:

*   **Parafacial zone** (this module) — the **sleep-promoting**
    region.

*   **Retrotrapezoid nucleus (RTN)**
    (``.../ventral_respiratory_group/retrotrapezoid_nucleus/``)
    — the **respiratory chemoreceptor**.

**They are anatomically adjacent** in the **rostral
ventrolateral medulla**, but they are **functionally distinct**
— the **RTN** senses **CO₂/H⁺** and **drives breathing**; the
**PZ** **promotes sleep**. Consumers must **not** conflate the
two.

The Parafacial Zone / RVLM Boundary
-----------------------------------
This is the **sleep / autonomic-premotor** boundary:

*   **Parafacial zone** (this module) — the **sleep-promoting**
    region.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) — the
    **sympathetic premotor / vasomotor** center.

**They are anatomically adjacent** in the **rostral
ventrolateral medulla**, but they are **functionally distinct**
— the **RVLM** **drives sympathetic outflow**; the **PZ**
**promotes sleep**. Consumers must **not** conflate the two.

The Parafacial Zone / Facial Nucleus Boundary
---------------------------------------------
This is the **medulla / pons** and **sleep / motor** boundary:

*   **Parafacial zone** (this module) — the **sleep-promoting**
    region.

*   **Facial nucleus (VII)**
    (``.../metencephalon/pons/cranial_nerve_nuclei/facial_nerve_nucleus/``)
    — the **branchial motor** nucleus for the **muscles of
    facial expression**.

**They are anatomically adjacent** — the parafacial zone is
**named after** its position **beside** the facial nucleus
("parafacial" = "beside the facial nucleus"). But they are
**DIFFERENT STRUCTURES** — the **facial nucleus** is **motor**;
the **parafacial zone** is **sleep-promoting**. Consumers must
**not** conflate the two.

The Parafacial Zone / Ventral Respiratory Group Boundary
--------------------------------------------------------
This is the **sleep / respiratory-rhythm** boundary:

*   **Parafacial zone** (this module) — the **sleep-promoting**
    region.

*   **Ventral respiratory group (VRG)**
    (``.../ventral_respiratory_group/``) — the **respiratory
    rhythm and pattern** generators (Bötzinger complex,
    pre-Bötzinger complex, nucleus para-ambiguus, nucleus
    retroambiguus, nucleus retrofacialis, retrotrapezoid
    nucleus).

**They are functionally distinct** — the **VRG** **generates
respiratory rhythm**; the **PZ** **promotes sleep**. Consumers
must **not** conflate the two.

The Parafacial Zone / Respiratory Center Boundary
-------------------------------------------------
This is the **sleep / dorsal-respiratory** boundary:

*   **Parafacial zone** (this module) — the **sleep-promoting**
    region.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **dorsal respiratory** and **chemosensory** structures
    (dorsal respiratory group, area postrema, chemoreceptor
    trigger zone, gracile nucleus, cuneate nucleus,
    gigantocellular reticular nucleus).

**They are functionally distinct** — the **respiratory_center**
contains **respiratory** and **chemosensory** structures; the
**PZ** is **sleep-promoting**. Consumers must **not** conflate
the two.

The Parafacial Zone / Solitary Nucleus Boundary
-----------------------------------------------
This is the **sleep / visceral-sensory** boundary:

*   **Parafacial zone** (this module) — the **sleep-promoting**
    region.

*   **Solitary nucleus** (``.../solitary_nucleus/``) — the
    **visceral afferent sensory** relay.

**They are functionally distinct.** Consumers must **not**
conflate the two.

The Parafacial Zone / Medullary Pyramid, Olivary Body, Arcuate Nucleus, and Cranial Nerve Nuclei Boundary
---------------------------------------------------------------------------------------------------------
This is the **sleep / white-matter, cerebellar-relay,
chemosensory, and motor** boundary:

*   **Parafacial zone** (this module) — the **sleep-promoting**
    region.

*   **Medullary pyramid** (``.../medullary_pyramid/``) — the
    **white-matter** corticospinal / corticobulbar tract.

*   **Olivary body** (``.../olivary_body/``) — the **cerebellar
    climbing-fiber relay**.

*   **Arcuate nucleus** (``.../arcuate_nucleus/``) — the
    **ventral-surface chemosensory** nucleus.

*   **Cranial nerve nuclei** (``.../cranial_nerve_nuclei/``) —
    the **medullary motor** nuclei.

**They are functionally distinct** from the **parafacial zone**.
Consumers must **not** conflate the parafacial zone with any of
these structures.

Function in the Human Brain
---------------------------
The parafacial zone's function is **sleep promotion** — **NOT
respiratory rhythm**, **NOT autonomic regulation**, and **NOT
motor control**:

*   **NREM sleep promotion:** The **parafacial zone** is
    **active during NREM sleep** (especially **slow-wave
    sleep**) and **promotes** NREM sleep onset and maintenance.
    **Pharmacogenetic activation** of the **GABAergic PZ
    neurons** in rodents **rapidly induces** NREM sleep and
    **cortical slow-wave activity** (Anaclet et al., 2012).

*   **Inhibition of wake-promoting systems:** The **parafacial
    zone** **projects** to the **basal forebrain**, the
    **lateral hypothalamus** (including **MCH neurons**), and
    other **wake-promoting** centers, and it **inhibits**
    them — thereby **promoting sleep**.

*   **Slow-wave sleep (SWS) generation:** The **parafacial
    zone** contributes to the **cortical slow-wave activity**
    that characterizes **NREM sleep** — its **GABAergic
    output** **modulates** the **cortical** and
    **thalamocortical** circuits that generate **slow waves**.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** (VRG) — **NOT**
    the parafacial zone.

*   **NOT autonomic regulation:** The **autonomic regulation**
    is the **RVLM**, **CVLM**, and **NTS** — **NOT** the
    parafacial zone.

*   **NOT motor control:** The **motor control** is the
    **corticospinal tract** (via the **medullary pyramid**) and
    the **cranial nerve motor nuclei** — **NOT** the parafacial
    zone.

**The unifying theme:** the parafacial zone is a **GABAergic /
glycinergic sleep-promoting region** at the **ponto-medullary
junction** — it **promotes NREM sleep** and **slow-wave
sleep** by **inhibiting wake-promoting systems**. It is **NOT**
the parafacial respiratory group, **NOT** the retrotrapezoid
nucleus, **NOT** the RVLM, **NOT** the CVLM, **NOT** the
facial nucleus, **NOT** the ventral respiratory group, and
**NOT** the respiratory_center.

Associated Disorders
--------------------
The parafacial zone has **no named clinical syndrome** of its
own — its clinical associations are **indirect**, via **sleep
regulation**:

*   **Insomnia (via parafacial zone dysfunction — hypothesized):**
    **Reduced** parafacial zone **GABAergic** output — or
    **impaired** parafacial zone **inhibition** of
    **wake-promoting** systems — could contribute to
    **insomnia** (difficulty initiating or maintaining sleep).
    The **parafacial zone** is a **sleep-promoting** center;
    its dysfunction is **hypothesized** to contribute to
    **insomnia**, though this is **not** a well-established
    clinical entity.

*   **Sleep-wake disorders (via parafacial zone dysfunction —
    hypothesized):** **Abnormal** parafacial zone **activity**
    — or **altered** parafacial zone **connectivity** with the
    **basal forebrain** and **lateral hypothalamus** — could
    contribute to **sleep-wake dysregulation** in conditions
    such as **narcolepsy**, **idiopathic hypersomnia**, or
    **circadian rhythm sleep disorders**. This is
    **speculative** and **not** a well-established clinical
    entity.

*   **Sudden infant death syndrome (SIDS — via adjacent
    structures):** **SIDS** has been associated with
    **abnormalities** in the **medullary** **serotonergic**
    system — **including** regions **adjacent** to the
    **parafacial zone** (e.g., the **arcuate nucleus**,
    **retrotrapezoid nucleus**, **solitary nucleus**). The
    **parafacial zone** itself is **not** a primary SIDS
    substrate, but it is **anatomically adjacent** to the
    **ventral medullary** regions implicated in **SIDS**.

*   **No Named "Parafacial Zone Syndrome":** The parafacial
    zone is a **functionally defined region** (not a sharply
    demarcated nucleus) — it has **no named clinical
    syndrome** of its own. Its clinical relevance is
    **indirect**, via **sleep regulation**.

**What is NOT here:** The parafacial zone is **not** the
substrate for **respiratory rhythm** (pre-Bötzinger complex,
VRG), **central hypoventilation** (RTN, VRG), **autonomic
dysfunction** (RVLM, CVLM, NTS), or **cranial nerve motor
deficits** (cranial nerve nuclei). Its clinical relevance is
the **sleep-regulation** functions listed above.

Lateralization Notes
--------------------
The parafacial zone is **bilateral in the brain** — a **left**
and **right** parafacial zone exist — but it is wired as a
**single leaf** in this tree. This is a **deliberate design
choice**:

*   **Bilateral in the brain:** The parafacial zone exists
    **bilaterally** in the medulla, with **left** and **right**
    components that are **structurally symmetric** and
    **functionally equivalent**.

*   **Single leaf in this tree:** The tree represents the
    parafacial zone as a **single structure** — **no**
    ``left`` / ``right`` split. This reflects:
    1.  The **sleep-promoting function** is **not obviously
        lateralized** in humans.
    2.  The parafacial zone is a **diffuse, functionally
        defined region** (not a sharply demarcated nucleus) —
        splitting it into left/right may **overstate** the
        precision of the tree.
    3.  The **name-collision hazard** with the **pFRG** is
        **more consequential** than any side-specific
        resolution — the tree prioritizes **clearly**
        distinguishing the PZ from the pFRG over
        **side-specific** resolution.

*   **NO Lateralization Warning:** The parafacial zone has **no
    known functional lateralization** in humans. Consumers must
    **not** import a **lateralization warning** into the
    parafacial zone — the **left** and **right** sides are
    **functionally equivalent**.

*   **NO Extended-Amygdala / SLEA Warning:** The parafacial zone
    is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the parafacial zone.

*   **NO Fear-Output Warning:** The parafacial zone is **not** a
    fear-output structure — it is a **sleep-promoting**
    region. Consumers must **not** conflate it with the
    **central nucleus** or with the **amygdala**.

**A consumer that needs side-specific parafacial zone
resolution should consult the references** — the tree
represents the parafacial zone as a **single structure** with
**no** left/right split and **no** lateralization warning.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The parafacial zone is a
    **leaf** — it does **not** import from any left-side or
    right-side module. The parafacial zone is **bilateral** in
    the brain but is **not** split into ``left`` / ``right`` in
    the tree; bilateral relationships are documented as **prose
    and boundary data**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../ventral_respiratory_group/``,
    ``.../respiratory_center/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../solitary_nucleus/``, ``.../medullary_pyramid/``,
    ``.../olivary_body/``, ``.../arcuate_nucleus/``,
    ``.../cranial_nerve_nuclei/``, ``.../metencephalon/``, or
    any other container. The parafacial zone's relationships to
    the parafacial respiratory group (pFRG), retrotrapezoid
    nucleus, RVLM, CVLM, facial nucleus, VRG, respiratory_center,
    solitary nucleus, medullary pyramid, olivary body, arcuate
    nucleus, and cranial nerve nuclei are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The parafacial
    zone is a **single structure** — it has **no structural
    children**. Consumers must **not** expect further sub-paths
    under ``.../parafacial_zone/``.
*   **NOT the parafacial respiratory group (pFRG).** The pFRG is
    a **respiratory** structure — often grouped with the **RTN**
    as the **RTN/pFRG** complex. The **parafacial zone** is a
    **sleep-promoting** region. Consumers must **not** conflate
    the two.
*   **NOT the retrotrapezoid nucleus.** The RTN is a
    **respiratory chemoreceptor** — **NOT** a sleep-promoting
    center.
*   **NOT the RVLM or CVLM.** Those are **autonomic** structures.
*   **NOT the facial nucleus.** The facial nucleus is a
    **branchial motor** nucleus in the **pons** — **NOT** a
    sleep-promoting medullary region.
*   **NOT the ventral respiratory group or respiratory_center.**
    Those are **respiratory** structures.
*   **NOT the solitary nucleus.** The solitary nucleus is the
    **visceral afferent sensory** relay.
*   **NOT the medullary pyramid, olivary body, arcuate nucleus,
    or cranial nerve nuclei.** Those are **white-matter motor
    tract**, **cerebellar relay**, **chemosensory nucleus**, and
    **motor nuclei** respectively.
*   **NOT bilateral in the tree.** The parafacial zone is
    **bilateral** in the brain but is represented as a **single
    leaf** in the tree — **no** ``left`` / ``right`` split.
    Consumers that need **side-specific** resolution should
    **consult the references**.
*   **No ``AREA_PATHS`` hop.** The parafacial zone is a **local
    leaf** — it is not cross-listed under another brainparts
    path.
*   **No nested cross-listing.** The parafacial zone has no
    nested dual-framing module. It is a **single leaf**.
*   **No lateralization warning.** The parafacial zone is
    **bilaterally symmetric** and **functionally equivalent**
    across sides — it carries **no** lateralization warning.
    This is a **deliberate design choice** — see
    *Lateralization Notes*.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import parafacial_zone

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.parafacial_zone"
    )

**Do not** assume the parafacial zone is the **parafacial
respiratory group (pFRG)**. The **pFRG** is a **respiratory**
structure — often grouped with the **RTN** as the **RTN/pFRG**
complex. The **parafacial zone** is a **sleep-promoting**
region.

**Do not** assume the parafacial zone is the **retrotrapezoid
nucleus**. The **RTN** is a **respiratory chemoreceptor** —
**NOT** a sleep-promoting center.

**Do not** assume the parafacial zone is the **RVLM** or
**CVLM**. Those are **autonomic** structures.

**Do not** assume the parafacial zone is the **facial nucleus**.
The facial nucleus is a **branchial motor** nucleus in the
**pons** — **NOT** a sleep-promoting medullary region.

**Do not** assume the parafacial zone is the **ventral
respiratory group** or **respiratory_center**. Those are
**respiratory** structures.

**Do not** assume the parafacial zone is the **solitary nucleus**,
the **medullary pyramid**, the **olivary body**, the **arcuate
nucleus**, or the **cranial nerve nuclei**. Each is a
**different structure**.

**Do not** look for ``left`` / ``right`` subdirectories under
the parafacial zone. The parafacial zone is **bilateral in the
brain** but is represented as a **single leaf** in the tree —
**no** left/right split. Consumers that need **side-specific**
resolution should **consult the references**.

Iterating the parafacial zone's (empty) children (recommended
consumer pattern)::

    PARAFACIAL_ZONE_CHILDREN = ()
    # The parafacial zone is a leaf. It has no structural
    # children. The parafacial zone is bilateral in the brain
    # but is not split into left/right in the tree.

Reaching the retrotrapezoid nucleus (recommended consumer
pattern — NOTE the DIFFERENT structure)::

    # The retrotrapezoid nucleus is a respiratory chemoreceptor,
    # NOT the sleep-promoting parafacial zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus
    #
    # The RTN and the parafacial zone are anatomically adjacent
    # in the rostral ventrolateral medulla — but they are
    # functionally distinct. The RTN is respiratory; the
    # parafacial zone is sleep-promoting.

Reaching the RVLM (recommended consumer pattern — NOTE the
DIFFERENT structure)::

    # The RVLM is a sympathetic premotor / vasomotor center, NOT
    # the sleep-promoting parafacial zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #
    # The RVLM and the parafacial zone are anatomically adjacent
    # in the rostral ventrolateral medulla — but they are
    # functionally distinct. The RVLM is autonomic; the
    # parafacial zone is sleep-promoting.

Reaching the facial nucleus (recommended consumer pattern — NOTE
the DIFFERENT container)::

    # The facial nucleus is a branchial motor nucleus in the
    # PONS, NOT the sleep-promoting parafacial zone:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei.facial_nerve_nucleus
    #
    # The parafacial zone is named after its position BESIDE the
    # facial nucleus ("parafacial" = "beside the facial nucleus")
    # — but it is a DIFFERENT structure with a DIFFERENT
    # function.

Reaching the ventral respiratory group and respiratory_center
(recommended consumer pattern — NOTE the DIFFERENT structures)::

    # The ventral respiratory group and the respiratory_center
    # are RESPIRATORY structures, NOT the sleep-promoting
    # parafacial zone:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center
    #
    # The parafacial zone is a SLEEP-PROMOTING region — it is
    # NOT a respiratory structure.

Reaching the parafacial respiratory group (pFRG) — NOTE the
NAME COLLISION::

    # The parafacial respiratory group (pFRG) is a RESPIRATORY
    # structure — often grouped with the retrotrapezoid nucleus
    # as the RTN/pFRG complex. It is NOT wired as a separate
    # module in this tree — it is documented as part of the
    # RTN/pFRG complex under:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.retrotrapezoid_nucleus
    #
    # Consumers must NOT conflate the parafacial zone (sleep-
    # promoting) with the parafacial respiratory group
    # (respiratory).

References
----------
*   **Parafacial zone — sleep-promoting center:** Anaclet, C.,
    et al. (2012). "The GABAergic parafacial zone is a medullary
    slow wave sleep-promoting center." *Nature Neuroscience*
    15:747–753. (Parafacial zone; GABAergic / glycinergic
    neurons; NREM sleep promotion; cortical slow-wave activity;
    projections to basal forebrain and lateral hypothalamus.)
*   **Parafacial zone — sleep-wake control:** Anaclet, C., et
    al. (2014). "Identification and characterization of a
    sleep-active region in the medullary parafacial zone."
    *Journal of Neurophysiology* 111:1897–1907. (Parafacial
    zone; sleep-active neurons; wake-promoting systems.)
*   **Parafacial zone — cortico-hypothalamic projections:**
    Anaclet, C., Fuller, P.M. (2017). "Brainstem regulation of
    slow-wave sleep." *Current Opinion in Neurobiology*
    44:131–138. (Parafacial zone; slow-wave sleep; projections
    to basal forebrain and lateral hypothalamus.)
*   **Parafacial respiratory group (contrast — respiratory):**
    Janczewski, W.A., Feldman, J.L. (2006). "Distinct rhythm
    generators for inspiration and expiration in the
    neonatal rat." *Journal of Physiology* 570:407–420.
    (Parafacial respiratory group; pre-inspiratory neurons;
    active expiration; RTN/pFRG complex.)
*   **RTN/pFRG complex (contrast — respiratory chemoreceptor):**
    Guyenet, P.G., et al. (2010). "The retrotrapezoid nucleus,
    central chemoreception and arterial pressure regulation."
    *Journal of Physiology* 588:47–58. (RTN/pFRG complex;
    central chemoreception; active expiration — DIFFERENT from
    the parafacial zone.)
*   **Retrotrapezoid nucleus (contrast — respiratory
    chemoreceptor):** Guyenet, P.G., Stornetta, R.L., Bayliss,
    D.A. (2008). "Central respiratory chemoreception: the
    retrotrapezoid nucleus." *Trends in Neurosciences*
    31:565–573. (RTN; CO₂/H⁺ chemoreception — DIFFERENT from
    the parafacial zone.)
*   **RVLM (contrast — sympathetic premotor):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure."
    *Nature Reviews Neuroscience* 7:335–346. (RVLM; sympathetic
    premotor neurons — DIFFERENT from the parafacial zone.)
*   **Facial nucleus (contrast — branchial motor):** Brodal, A.
    (2010). *The Central Nervous System: Structure and Function*,
    4th ed. (Facial nucleus; branchial motor column — DIFFERENT
    from the parafacial zone.)
*   **Ventral respiratory group (contrast — respiratory
    rhythm):** Feldman, J.L., Del Negro, C.A. (2006). "Looking
    for inspiration: new perspectives on respiratory rhythm."
    *Nature Reviews Neuroscience* 7:232–242. (Ventral
    respiratory group; pre-Bötzinger complex — DIFFERENT from
    the parafacial zone.)
*   **Solitary nucleus (contrast — visceral afferent):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS as the
    visceral afferent relay — DIFFERENT from the parafacial
    zone.)
*   **Insomnia (hypothesized parafacial zone involvement):**
    Anaclet, C., et al. (2012). "The GABAergic parafacial zone
    is a medullary slow wave sleep-promoting center." *Nature
    Neuroscience* 15:747–753. (Parafacial zone; sleep
    promotion; hypothesized insomnia relevance.)
*   **SIDS (adjacent medullary structures):** Kinney, H.C., et
    al. (2003). "Sudden infant death syndrome and the medullary
    serotonergic system." *JAMA* 290:1599–1609. (Medullary
    serotonergic abnormalities in SIDS — including regions
    adjacent to the parafacial zone.)
*   **Sleep-wake circuits:** Saper, C.B., Fuller, P.M. (2017).
    "Wake-sleep circuitry: an overview." *Current Opinion in
    Neurobiology* 44:186–195. (Sleep-wake circuits; wake-
    promoting systems; parafacial zone as sleep-promoting
    center.)
*   NeuroNames — Parafacial zone; FMA — Parafacial zone.
"""