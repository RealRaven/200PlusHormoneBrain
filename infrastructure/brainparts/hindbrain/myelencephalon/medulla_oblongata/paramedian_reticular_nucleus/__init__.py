"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.paramedian_reticular_nucleus
==================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── paramedian_reticular_nucleus   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Paramedian reticular nucleus; PRN; paramedian
reticular nucleus of the medulla; nucleus reticularis
paramedianus; nucleus reticularis medullae oblongatae
paramedianus; medial reticular nucleus (caudal).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** in the **paramedian reticular
formation** of the **medulla oblongata** — a **cerebellar
projection** nucleus that also **modulates nociception** and
**participates** in **autonomic** and **respiratory**
integration. It is **NOT** the **paramedian pontine reticular
formation (PPRF)** — which is a **pontine** **horizontal
gaze** center, **NOT** a medullary cerebellar relay. It is
**also NOT** the **gigantocellular reticular nucleus** — which
is a **different** reticular nucleus, wired under
``.../respiratory_center/gigantocellular_reticular_nucleus/``.
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** paramedian
reticular nucleus. The bilateral paramedian reticular nuclei are
the **structural children** of this **bilateral container**;
the container itself is **unpaired**.
**Boundary status (NOT the paramedian pontine reticular formation
(PPRF) — a DIFFERENT structure with a SIMILAR name):** **Boundary
case — the paramedian reticular nucleus (PRN) is NOT the
paramedian pontine reticular formation (PPRF).** The **PPRF** is
a **pontine** **horizontal gaze** center — it is wired under
``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``
and it **drives horizontal saccades** via the **abducens
nucleus** and the **contralateral medial longitudinal
fasciculus (MLF)**. The **paramedian reticular nucleus** (here)
is a **medullary** **cerebellar projection** nucleus — it
**projects** to the **cerebellar cortex** and **modulates
nociception**. **They share the name "paramedian reticular" but
are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS with DIFFERENT
FUNCTIONS** — the **PPRF** is **pontine horizontal gaze**; the
**PRN** is **medullary cerebellar / nociceptive / autonomic**.
Consumers must **not** conflate the two.
**Boundary status (NOT the gigantocellular reticular nucleus — a
DIFFERENT reticular nucleus):** **Boundary case — the
paramedian reticular nucleus is NOT the gigantocellular reticular
nucleus.** The **gigantocellular reticular nucleus (Gi)** is a
**larger** medullary reticular nucleus — it is wired under
``.../respiratory_center/gigantocellular_reticular_nucleus/``
and is **involved** in **respiratory** and **autonomic**
functions (including **respiratory** pattern generation and
**pain modulation**). The **paramedian reticular nucleus**
(here) is a **smaller**, **more medial** nucleus — it is a
**cerebellar projection** nucleus with **nociceptive** and
**autonomic** roles. **They are DIFFERENT RETICULAR NUCLEI** —
the **Gi** is **larger**, **more lateral**, and part of the
**respiratory_center** container; the **PRN** is **smaller**,
**more medial**, and wired as its **own container**. Consumers
must **not** conflate the two.
**Boundary status (NOT the whole medullary reticular formation —
a specific nucleus within it):** **Boundary case — the
paramedian reticular nucleus is NOT the whole medullary reticular
formation.** The **medullary reticular formation** is a
**distributed system** — it includes the **paramedian reticular
nucleus** (here), the **gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/``),
the **parvocellular reticular nucleus** (pontomedullary),
the **lateral reticular nucleus** (not wired under
``medulla_oblongata`` in this tree), and **other** reticular
nuclei. The **paramedian reticular nucleus** is **one specific
nucleus** within the medullary reticular formation — it is
**NOT** the whole formation. Consumers must **not** conflate the
**PRN** with the **whole medullary reticular formation**.
**Boundary status (NOT the RVLM or CVLM — autonomic premotor
regions):** **Boundary case — the paramedian reticular nucleus
is NOT the RVLM or CVLM.** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor / vasomotor** center; the **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay. The **paramedian reticular
nucleus** (here) is a **paramedian cerebellar / nociceptive /
autonomic** nucleus — it **modulates** autonomic function but is
**NOT** the sympathetic premotor or sympathoinhibitory center.
Consumers must **not** conflate the two.
**Boundary status (NOT the respiratory_center structures — a
different functional system):** **Boundary case — the
paramedian reticular nucleus is NOT the respiratory_center
structures.** The **respiratory_center**
(``.../respiratory_center/``) contains the **dorsal respiratory
group**, **area postrema**, **chemoreceptor trigger zone**,
**gracile nucleus**, **cuneate nucleus**, and
**gigantocellular reticular nucleus** — **respiratory** and
**chemosensory** structures. The **paramedian reticular
nucleus** (here) is a **cerebellar / nociceptive / autonomic**
nucleus — **NOT** a respiratory rhythm generator and **NOT** a
chemoreceptor. Consumers must **not** conflate the two.
**Boundary status (NOT the ventral respiratory group — a
respiratory rhythm generator):** **Boundary case — the
paramedian reticular nucleus is NOT the ventral respiratory
group (VRG).** The **VRG**
(``.../ventral_respiratory_group/``) contains the **Bötzinger
complex**, **pre-Bötzinger complex**, **nucleus para-ambiguus**,
**nucleus retroambiguus**, **nucleus retrofacialis**, and
**retrotrapezoid nucleus** — the **respiratory rhythm** and
**pattern** generators. The **paramedian reticular nucleus**
(here) is a **cerebellar / nociceptive / autonomic** nucleus —
**NOT** a respiratory rhythm generator. Consumers must **not**
conflate the two.
**Boundary status (NOT the solitary nucleus — a visceral
afferent relay):** **Boundary case — the paramedian reticular
nucleus is NOT the solitary nucleus.** The **solitary nucleus
(NTS)** (``.../solitary_nucleus/``) is the **visceral afferent
relay** — it receives **taste**, **baroreceptor**,
**chemoreceptor**, and **gastrointestinal** afferents. The
**paramedian reticular nucleus** (here) is a **cerebellar /
nociceptive / autonomic** nucleus — **NOT** a visceral afferent
relay. Consumers must **not** conflate the two.
**Boundary status (NOT the hypoglossal nucleus or other cranial
nerve nuclei — motor nuclei):** **Boundary case — the
paramedian reticular nucleus is NOT the cranial nerve nuclei.**
The **cranial nerve nuclei** (``.../cranial_nerve_nuclei/``) are
the **medullary motor** nuclei (hypoglossal, dorsal motor vagus,
inferior salivatory, nucleus ambiguus). The **paramedian
reticular nucleus** (here) is a **cerebellar / nociceptive /
autonomic** nucleus — **NOT** a cranial nerve motor nucleus.
Consumers must **not** conflate the two.
**Boundary status (NOT the medullary pyramid — a white-matter
tract):** **Boundary case — the paramedian reticular nucleus is
NOT the medullary pyramid.** The **medullary pyramid**
(``.../medullary_pyramid/``) is the **ventral white-matter**
corticospinal / corticobulbar tract. The **paramedian reticular
nucleus** (here) is a **grey-matter** nucleus. Consumers must
**not** conflate the two.
**Boundary status (NOT the olivary body — a cerebellar
climbing-fiber relay):** **Boundary case — the paramedian
reticular nucleus is NOT the olivary body.** The **olivary
body** (``.../olivary_body/``) is the **cerebellar
climbing-fiber relay** (inferior olivary nucleus). The
**paramedian reticular nucleus** (here) is a **cerebellar mossy-
fiber relay** — **NOT** a climbing-fiber relay. Consumers must
**not** conflate the two.
**Boundary status (NOT the arcuate nucleus — a ventral-surface
chemosensory nucleus):** **Boundary case — the paramedian
reticular nucleus is NOT the arcuate nucleus.** The **arcuate
nucleus** (``.../arcuate_nucleus/``) is a **ventral-surface
chemosensory and hypothalamic-projecting** nucleus. The
**paramedian reticular nucleus** (here) is a **paramedian
cerebellar / nociceptive / autonomic** nucleus. Consumers must
**not** conflate the two.
**Boundary status (NOT the parafacial zone — a sleep-promoting
region):** **Boundary case — the paramedian reticular nucleus is
NOT the parafacial zone.** The **parafacial zone**
(``.../parafacial_zone/``) is a **GABAergic / glycinergic
sleep-promoting** region. The **paramedian reticular nucleus**
(here) is a **cerebellar / nociceptive / autonomic** nucleus.
Consumers must **not** conflate the two.
**Boundary status (NOT the perihypoglossal nuclei — a different
medullary structure):** **Boundary case — the paramedian
reticular nucleus is NOT the perihypoglossal nuclei.** The
**perihypoglossal nuclei** (``.../perihypoglossal_nuclei/``) —
the **intercalated nucleus** and **prepositus nucleus** — are
**oculomotor / gaze-holding** structures. The **paramedian
reticular nucleus** (here) is a **cerebellar / nociceptive /
autonomic** nucleus. Consumers must **not** conflate the two.
**Boundary status (NOT the whole medulla oblongata — a small
grey-matter nucleus within it):** **Boundary case — the
paramedian reticular nucleus is NOT the whole medulla
oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the cranial nerve nuclei, the autonomic nuclei, the
respiratory centers, the olivary body, the medullary pyramid,
the arcuate nucleus, the parafacial zone, the paramedian
reticular nucleus (here), and other structures. The
**paramedian reticular nucleus** is **one small grey-matter
nucleus** within the medulla. Consumers must **not** conflate
the **PRN** with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
structural children):** **Boundary case — the paramedian
reticular nucleus is a BILATERAL container with ``left`` and
``right`` structural children.** The
**paramedian_reticular_nucleus** module (here) is an
**unpaired container**; its **structural children** are
``left`` and ``right`` — each a **leaf** representing the
**left** or **right** paramedian reticular nucleus. Consumers
must **not** look for a single unpaired paramedian reticular
nucleus — the **left** and **right** nuclei are **separate
modules** under this container. Resolve them via
``paramedian_reticular_nucleus.left`` and
``paramedian_reticular_nucleus.right``.

Overview
--------
The **paramedian reticular nucleus (PRN)** is a **small grey-matter
nucleus** in the **paramedian reticular formation** of the
**medulla oblongata** — it lies **near the midline**, **dorsal**
to the **medullary pyramid**, **medial** to the **hypoglossal
nucleus**, and **ventral** to the **medial longitudinal
fasciculus (MLF)**. It is a **cerebellar projection** nucleus
that **also** **modulates nociception** and **participates** in
**autonomic** and **respiratory** integration.

**The paramedian reticular nucleus is the MEDULLARY paramedian
reticular nucleus, NOT the paramedian pontine reticular
formation (PPRF).** The **PPRF** is a **pontine horizontal gaze**
center — **NOT** a medullary cerebellar relay. **They share the
name "paramedian reticular" but are DIFFERENT STRUCTURES in
DIFFERENT CONTAINERS with DIFFERENT FUNCTIONS.**

**The paramedian reticular nucleus is a BILATERAL container.**
Its structural children are ``left`` and ``right`` — each a leaf
representing the left or right PRN. The **container itself** is
**unpaired**.

**The paramedian reticular nucleus is a CEREBELLAR PROJECTION
NUCLEUS, NOT a respiratory rhythm generator, NOT an autonomic
premotor center, and NOT a cranial nerve motor nucleus.** It
**projects** to the **cerebellar cortex** via **mossy fibers**
(via the **inferior cerebellar peduncle**), and it **receives**
input from the **spinal cord** (**spinoreticular** fibers) and
from **higher** centers. It is **part of** the **ascending
reticular activating system (ARAS)** and the **descending
pain-modulating** system.

**The paramedian reticular nucleus is part of the medullary
reticular formation, but it is NOT the whole reticular
formation.** It is **one specific nucleus** — **distinct** from
the **gigantocellular reticular nucleus** (wired under
``.../respiratory_center/gigantocellular_reticular_nucleus/``),
the **parvocellular reticular nucleus** (pontomedullary), the
**lateral reticular nucleus** (not wired here), and other
reticular nuclei.

Bilateral Structure
-------------------
The paramedian reticular nucleus is a **bilateral container**
with **two structural children**:

*   ``left`` — the **left** paramedian reticular nucleus (a leaf
    module).
*   ``right`` — the **right** paramedian reticular nucleus (a
    leaf module).

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left** and
**right** paramedian reticular nuclei as **single structures**,
not as further sub-containers. Consumers that need
**side-specific** resolution should descend into ``left`` or
``right``; consumers that need **bilateral** resolution should
iterate over both.

**The container itself is unpaired.** There is **no**
``paramedian_reticular_nucleus/left/.../`` structural hierarchy
beyond the single leaf level — the ``left`` and ``right``
modules are the **terminal modules** for this structure.

The Paramedian Reticular Nucleus / Paramedian Pontine Reticular Formation Boundary
----------------------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Paramedian reticular nucleus (PRN)** (this module) — the
    **medullary** cerebellar / nociceptive / autonomic nucleus.

*   **Paramedian pontine reticular formation (PPRF)** — the
    **pontine** horizontal gaze center
    (``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``).

**They share the name "paramedian reticular" but are DIFFERENT
STRUCTURES in DIFFERENT CONTAINERS with DIFFERENT FUNCTIONS** —
the **PPRF** is **pontine horizontal gaze**; the **PRN** is
**medullary cerebellar / nociceptive / autonomic**. Consumers
must **not** conflate the two.

The Paramedian Reticular Nucleus / Gigantocellular Reticular Nucleus Boundary
-----------------------------------------------------------------------------
This is the **paramedian / gigantocellular** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **paramedian** cerebellar / nociceptive / autonomic nucleus.

*   **Gigantocellular reticular nucleus**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/``)
    — the **larger**, **more lateral** medullary reticular
    nucleus — involved in **respiratory** and **autonomic**
    functions.

**They are DIFFERENT RETICULAR NUCLEI** — the **Gi** is **larger**,
**more lateral**, and part of the **respiratory_center**
container; the **PRN** is **smaller**, **more medial**, and
wired as its **own container**. Consumers must **not** conflate
the two.

The Paramedian Reticular Nucleus / RVLM and CVLM Boundary
---------------------------------------------------------
This is the **reticular / autonomic-premotor** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **paramedian** cerebellar / nociceptive / autonomic nucleus.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) and
    **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **ventrolateral** sympathetic premotor / sympathoinhibitory
    nuclei.

**They are DIFFERENT STRUCTURES** — the **PRN** is **paramedian**
and **cerebellar / nociceptive / autonomic**; the **RVLM** and
**CVLM** are **ventrolateral** and **autonomic premotor /
sympathoinhibitory**. Consumers must **not** conflate the two.

The Paramedian Reticular Nucleus / Respiratory Center and Ventral Respiratory Group Boundary
--------------------------------------------------------------------------------------------
This is the **reticular / respiratory** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **paramedian** cerebellar / nociceptive / autonomic nucleus.

*   **Respiratory center** (``.../respiratory_center/``) and
    **ventral respiratory group**
    (``.../ventral_respiratory_group/``) — the **respiratory**
    rhythm and pattern generators.

**They are DIFFERENT STRUCTURES** — the **PRN** is **NOT** a
respiratory rhythm generator. Consumers must **not** conflate the
two.

The Paramedian Reticular Nucleus / Solitary Nucleus Boundary
------------------------------------------------------------
This is the **reticular / visceral-sensory** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **paramedian** cerebellar / nociceptive / autonomic nucleus.

*   **Solitary nucleus** (``.../solitary_nucleus/``) — the
    **visceral afferent sensory** relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Paramedian Reticular Nucleus / Cranial Nerve Nuclei Boundary
----------------------------------------------------------------
This is the **reticular / motor** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **paramedian** cerebellar / nociceptive / autonomic nucleus.

*   **Cranial nerve nuclei** (``.../cranial_nerve_nuclei/``) — the
    **medullary motor** nuclei.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the two.

The Paramedian Reticular Nucleus / Medullary Pyramid Boundary
-------------------------------------------------------------
This is the **grey-matter / white-matter** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **paramedian grey-matter** nucleus.

*   **Medullary pyramid** (``.../medullary_pyramid/``) — the
    **ventral white-matter** corticospinal / corticobulbar
    tract.

**They are DIFFERENT STRUCTURES.** The **PRN** is **dorsal** to
the **medullary pyramid** — but they are **different structures**
(grey matter vs. white matter).

The Paramedian Reticular Nucleus / Olivary Body Boundary
--------------------------------------------------------
This is the **cerebellar mossy-fiber / climbing-fiber** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **cerebellar mossy-fiber** relay.

*   **Olivary body** (``.../olivary_body/``) — the **cerebellar
    climbing-fiber** relay.

**They are DIFFERENT STRUCTURES** — the **PRN** projects to the
cerebellum via **mossy fibers**; the **olivary body** projects
via **climbing fibers**. Consumers must **not** conflate the two.

The Paramedian Reticular Nucleus / Arcuate Nucleus, Parafacial Zone, and Perihypoglossal Nuclei Boundary
--------------------------------------------------------------------------------------------------------
This is the **reticular / other-medullary-structures** boundary:

*   **Paramedian reticular nucleus** (this module) — the
    **paramedian** cerebellar / nociceptive / autonomic nucleus.

*   **Arcuate nucleus** (``.../arcuate_nucleus/``) — the
    **ventral-surface chemosensory** nucleus.

*   **Parafacial zone** (``.../parafacial_zone/``) — the
    **sleep-promoting** region.

*   **Perihypoglossal nuclei** (``.../perihypoglossal_nuclei/``) —
    the **oculomotor / gaze-holding** structures.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the **PRN** with any of these.

Function in the Human Brain
---------------------------
The paramedian reticular nucleus's function is **cerebellar
projection**, **nociception modulation**, and **autonomic /
respiratory integration** — **NOT motor conduction**, **NOT
cranial nerve motor control**, and **NOT respiratory rhythm**:

*   **Cerebellar projection (mossy fibers):** The **paramedian
    reticular nucleus** is a **cerebellar projection** nucleus —
    it sends **mossy fibers** to the **cerebellar cortex** (via
    the **inferior cerebellar peduncle**), contributing to
    **cerebellar** **sensorimotor** and **autonomic** processing.
    The **PRN** is one of the **precerebellar nuclei** — along
    with the **lateral reticular nucleus**, **arcuate nucleus**,
    **inferior olive**, **pontine nuclei**, and **vestibular
    nuclei**.

*   **Nociception modulation (descending pain control):** The
    **paramedian reticular nucleus** is **part of** the
    **descending pain-modulating** system — it **receives**
    input from the **periaqueductal gray (PAG)** and **projects**
    to the **spinal cord dorsal horn** (via the **dorsolateral
    funiculus**), **modulating** **nociceptive** transmission.
    The **PRN** contributes to **stress-induced analgesia** and
    **descending inhibition** of pain.

*   **Autonomic and respiratory integration:** The **paramedian
    reticular nucleus** **participates** in **autonomic** and
    **respiratory** integration — it **receives** input from the
    **solitary nucleus (NTS)**, the **ventrolateral medulla**,
    and the **hypothalamus**, and it **projects** to the
    **respiratory** and **autonomic** centers. The **PRN** is
    **part of** the **reticular** **integrative** network —
    **NOT** a primary rhythm generator.

*   **Ascending reticular activating system (ARAS):** The
    **paramedian reticular nucleus** is **part of** the
    **ascending reticular activating system (ARAS)** — it
    **projects** to the **thalamus** and **cortex** and
    **contributes** to **arousal** and **wakefulness**. The
    **PRN** is one of the **reticular** **arousal** nuclei,
    **distinct** from the **sleep-promoting** parafacial zone.

*   **NOT motor conduction:** The **motor conduction** is the
    **corticospinal tract** (via the **medullary pyramid**) —
    **NOT** the PRN.

*   **NOT cranial nerve motor control:** The **cranial nerve
    motor control** is the **cranial nerve nuclei** — **NOT**
    the PRN.

*   **NOT respiratory rhythm:** The **respiratory rhythm** is
    generated by the **pre-Bötzinger complex** (VRG) — **NOT**
    the PRN.

**The unifying theme:** the paramedian reticular nucleus is a
**small medullary reticular nucleus** — **cerebellar projection
(mossy fibers)**, **nociception modulation**, **autonomic /
respiratory integration**, and **ARAS arousal** — **NOT** the
**paramedian pontine reticular formation (PPRF)**, **NOT** the
**gigantocellular reticular nucleus**, and **NOT** the **whole
medullary reticular formation**.

Associated Disorders
--------------------
The paramedian reticular nucleus has **no named clinical syndrome**
of its own — its clinical associations are **indirect**, via
**cerebellar**, **nociceptive**, **autonomic**, and **arousal**
functions:

*   **Cerebellar ataxia (via PRN involvement — hypothesized):**
    **Damage** to the **PRN** or its **cerebellar projections**
    could contribute to **cerebellar ataxia** or
    **sensorimotor** deficits. The **PRN** is a **precerebellar**
    nucleus — but it is **rarely** the **primary** site of
    cerebellar ataxia (the **inferior olive**, **pontine
    nuclei**, and **cerebellar cortex** are the **primary**
    substrates).

*   **Chronic pain (via PRN dysfunction — hypothesized):**
    **Impaired** descending **pain modulation** from the **PRN**
    could contribute to **chronic pain** syndromes
    (fibromyalgia, neuropathic pain). The **PRN** is **part of**
    the **descending pain-modulating** system — but **not** the
    **sole** or **primary** substrate.

*   **Autonomic dysfunction (via PRN involvement —
    hypothesized):** **Damage** to the **PRN** could contribute
    to **autonomic** dysregulation — but the **RVLM**, **CVLM**,
    and **NTS** are the **primary** autonomic substrates.

*   **Arousal / sleep-wake disorders (via PRN involvement —
    hypothesized):** **Damage** to the **PRN** could contribute
    to **arousal** or **sleep-wake** dysfunction — but the
    **ARAS**, **parafacial zone**, and other **sleep-wake**
    structures are the **primary** substrates.

*   **No Named "Paramedian Reticular Nucleus Syndrome":** The
    paramedian reticular nucleus is a **small, functionally
    subtle** nucleus — it has **no named clinical syndrome** of
    its own. Its clinical relevance is **indirect**, via the
    **cerebellar**, **nociceptive**, **autonomic**, and
    **arousal** functions listed above.

**What is NOT here:** The paramedian reticular nucleus is **not**
the substrate for **cranial nerve motor deficits** (cranial nerve
nuclei), **respiratory rhythm** (pre-Bötzinger complex, VRG),
**sympathetic premotor** function (RVLM), or **horizontal gaze
palsy** (PPRF — **NOT** in this container). Its clinical
relevance is the **cerebellar / nociceptive / autonomic /
arousal** functions listed above.

Lateralization Notes
--------------------
The paramedian reticular nucleus is a **bilateral container** with
``left`` and ``right`` structural children. There is **no**
``paramedian_reticular_nucleus/left/.../`` structural hierarchy
beyond the single leaf level.

*   **Bilateral structural children:** ``left`` and ``right``
    are **leaf modules** — each represents the **left** or
    **right** paramedian reticular nucleus as a **single
    structure**. Consumers resolve the **left** paramedian
    reticular nucleus via ``paramedian_reticular_nucleus.left``
    and the **right** via
    ``paramedian_reticular_nucleus.right``.

*   **Bilateral symmetry:** The **left** and **right**
    paramedian reticular nuclei are **structurally symmetric** —
    they are **mirror pairs** with the **same**
    cytoarchitecture, **same** projections (bilateral to the
    cerebellum and spinal cord), and **same** functions.

*   **Bilateral projections:** Each **paramedian reticular
    nucleus** projects **bilaterally** to the **cerebellar
    cortex** (via mossy fibers) and **bilaterally** to the
    **spinal cord dorsal horn** (via the descending
    pain-modulating system). This is **functionally** a
    **bilateral** circuit — the **PRN** does **not** project
    **purely** ipsilaterally or **purely** contralaterally.

*   **NO lateralization warning:** The paramedian reticular
    nucleus has **no known functional lateralization** in humans.
    Consumers must **not** import a **lateralization warning**
    into the paramedian reticular nucleus — the **left** and
    **right** nuclei are **functionally symmetric**.

*   **NO extended-amygdala / fear-output / SLEA warnings:** The
    paramedian reticular nucleus is **not** part of the amygdala,
    extended-amygdala, or SLEA continuum. It carries **no SLEA
    warning** and **no fear-output warning**.

**A consumer that assumes "left paramedian reticular nucleus =
right paramedian reticular nucleus" will be structurally
correct** — the two sides are **symmetric** and **functionally
equivalent** at the **nucleus level**. The paramedian reticular
nucleus is a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The paramedian reticular
    nucleus is a **bilateral container** — it does **not** import
    from ``left/`` or ``right/`` at the container level. The
    ``left`` and ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../metencephalon/pons/tegmentum/paramedian_pontine_reticular_formation/``,
    ``.../respiratory_center/gigantocellular_reticular_nucleus/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../respiratory_center/``,
    ``.../ventral_respiratory_group/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``, ``.../medullary_pyramid/``,
    ``.../olivary_body/``, ``.../arcuate_nucleus/``,
    ``.../parafacial_zone/``, ``.../perihypoglossal_nuclei/``,
    or any other container. The paramedian reticular nucleus's
    relationships to the PPRF, gigantocellular reticular nucleus,
    RVLM, CVLM, respiratory centers, solitary nucleus, cranial
    nerve nuclei, medullary pyramid, olivary body, arcuate
    nucleus, parafacial zone, and perihypoglossal nuclei are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children.** The structural
    children are ``left`` and ``right``, each a **leaf**. The
    container itself is **unpaired**.
*   **NOT the paramedian pontine reticular formation (PPRF).**
    The PPRF is a **pontine horizontal gaze** center — **NOT** a
    medullary cerebellar relay. Consumers must **not** conflate
    the two.
*   **NOT the gigantocellular reticular nucleus.** The Gi is a
    **different reticular nucleus** (larger, more lateral, wired
    under ``.../respiratory_center/gigantocellular_reticular_nucleus/``).
*   **NOT the whole medullary reticular formation.** The PRN is
    **one specific nucleus** within the reticular formation.
*   **NOT the RVLM or CVLM.** Those are **autonomic premotor /
    sympathoinhibitory** structures.
*   **NOT the respiratory_center or ventral respiratory group.**
    Those are **respiratory** structures.
*   **NOT the solitary nucleus, cranial nerve nuclei, medullary
    pyramid, olivary body, arcuate nucleus, parafacial zone, or
    perihypoglossal nuclei.** Each is a **different structure**.
*   **No ``AREA_PATHS`` hop.** The paramedian reticular nucleus is
    a **local container** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The paramedian reticular nucleus
    has no nested dual-framing module. It is a **bilateral
    container** with **two leaf children**.
*   **Structural parity with the right side — strict mirror.** The
    ``left`` and ``right`` leaves are **structurally identical**
    — same leaf status, same **cerebellar / nociceptive /
    autonomic** framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import paramedian_reticular_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "paramedian_reticular_nucleus"
    )

**Do not** assume the paramedian reticular nucleus is the
**paramedian pontine reticular formation (PPRF)**. The **PPRF**
is a **pontine horizontal gaze** center — **NOT** a medullary
cerebellar relay.

**Do not** assume the paramedian reticular nucleus is the
**gigantocellular reticular nucleus**. The **Gi** is a
**different reticular nucleus** (larger, more lateral, wired
under ``.../respiratory_center/gigantocellular_reticular_nucleus/``).

**Do not** assume the paramedian reticular nucleus is the
**whole medullary reticular formation**. It is **one specific
nucleus** within the reticular formation.

**Do not** assume the paramedian reticular nucleus is the
**RVLM**, the **CVLM**, the **respiratory_center**, the
**ventral respiratory group**, the **solitary nucleus**, the
**cranial nerve nuclei**, the **medullary pyramid**, the
**olivary body**, the **arcuate nucleus**, the **parafacial
zone**, or the **perihypoglossal nuclei**. Each is a
**different structure**.

**Do not** look for a single unpaired paramedian reticular
nucleus. The **left** and **right** paramedian reticular nuclei
are **separate leaf modules** under this container.

Iterating the paramedian reticular nucleus's structural children
(recommended consumer pattern)::

    PARAMEDIAN_RETICULAR_NUCLEUS_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # paramedian reticular nucleus.

Reaching the left and right paramedian reticular nuclei
(recommended consumer pattern)::

    # The left and right paramedian reticular nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.paramedian_reticular_nucleus.left
    #   hindbrain.myelencephalon.medulla_oblongata.paramedian_reticular_nucleus.right
    #
    # Each is a leaf module representing the paramedian reticular
    # nucleus of that side.

Reaching the paramedian pontine reticular formation (PPRF)
(recommended consumer pattern — NOTE the DIFFERENT container)::

    # The paramedian pontine reticular formation (PPRF) is a
    # PONTINE horizontal gaze center, NOT a medullary cerebellar
    # relay:
    #
    #   hindbrain.metencephalon.pons.tegmentum.paramedian_pontine_reticular_formation
    #
    # The PPRF and the PRN share the name "paramedian reticular"
    # — but they are DIFFERENT STRUCTURES in DIFFERENT CONTAINERS
    # with DIFFERENT FUNCTIONS.

Reaching the gigantocellular reticular nucleus (recommended
consumer pattern — NOTE the DIFFERENT structure)::

    # The gigantocellular reticular nucleus is a DIFFERENT
    # reticular nucleus, wired under the respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gigantocellular_reticular_nucleus
    #
    # The Gi and the PRN are DIFFERENT RETICULAR NUCLEI — the Gi
    # is larger, more lateral, and part of the respiratory_center
    # container; the PRN is smaller, more medial, and wired as its
    # own container.

Reaching the RVLM, CVLM, and respiratory_center structures
(recommended consumer pattern — NOTE the DIFFERENT structures)::

    # The RVLM, CVLM, respiratory_center, and ventral respiratory
    # group are DIFFERENT from the paramedian reticular nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #
    # The RVLM and CVLM are ventrolateral autonomic structures;
    # the respiratory_center and VRG are respiratory structures.
    # The paramedian reticular nucleus is a PARAMEDIAN cerebellar
    # / nociceptive / autonomic nucleus — DIFFERENT from all of
    # these.

Reaching the other medullary structures (recommended consumer
pattern — NOTE the DIFFERENT structures)::

    # The solitary nucleus, cranial nerve nuclei, medullary
    # pyramid, olivary body, arcuate nucleus, parafacial zone,
    # and perihypoglossal nuclei are DIFFERENT from the
    # paramedian reticular nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone
    #   hindbrain.myelencephalon.medulla_oblongata.perihypoglossal_nuclei
    #
    # Each is a DIFFERENT STRUCTURE with a DIFFERENT function.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"paramedian_reticular_nucleus.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Medullary reticular formation; paramedian reticular nucleus;
    precerebellar nuclei; mossy fibers.)
*   **Paramedian reticular nucleus — cerebellar projections:**
    Brodal, P., Bjaalie, J.G. (1992). "Organization of the
    pontine nuclei and the projection to the cerebellum."
    *Progress in Brain Research* 88:423–438. (Precerebellar
    nuclei — including the paramedian reticular nucleus;
    mossy-fiber projections.)
*   **Paramedian reticular nucleus — anatomy and connections:**
    Newman, D.B., Ginsberg, C.Y. (1992). "Brainstem reticular
    nuclei of the cat: I. Sources of the reticulocerebellar
    projection." *Neuroscience* 47:149–168. (Paramedian
    reticular nucleus; reticulocerebellar mossy-fiber
    projections.)
*   **Paramedian reticular nucleus — nociception:** Fields, H.L.,
    Basbaum, A.I. (1994). "Central nervous system mechanisms of
    pain modulation." In: *Textbook of Pain*, 3rd ed.
    (Descending pain-modulating system; reticular nuclei —
    including the paramedian reticular nucleus.)
*   **Descending pain modulation:** Basbaum, A.I., Fields, H.L.
    (1984). "Endogenous pain control systems: brainstem spinal
    pathways and endorphin circuitry." *Annual Review of
    Neuroscience* 7:309–338. (Descending pain-modulating
    system; reticular nuclei; periaqueductal gray → medullary
    reticular formation → spinal cord dorsal horn.)
*   **Paramedian pontine reticular formation (contrast — pontine
    horizontal gaze):** Leigh, R.J., Zee, D.S. (2015). *The
    Neurology of Eye Movements*, 5th ed. (PPRF; pontine
    horizontal gaze center — DIFFERENT from the medullary
    paramedian reticular nucleus.)
*   **Gigantocellular reticular nucleus (contrast — different
    reticular nucleus):** Newman, D.B. (1985). "Distinguishing
    rat medullary reticular formation regions by afferent and
    efferent connections." *Brain Research* 326:129–138.
    (Gigantocellular reticular nucleus — DIFFERENT from the
    paramedian reticular nucleus.)
*   **ARAS — ascending reticular activating system:** Moruzzi,
    G., Magoun, H.W. (1949). "Brain stem reticular formation
    and activation of the EEG." *Electroencephalography and
    Clinical Neurophysiology* 1:455–473. (Ascending reticular
    activating system; reticular nuclei — including the
    paramedian reticular nucleus.)
*   **Precerebellar nuclei — overview:** Brodal, P. (1981).
    "The cerebellar projection from the reticular formation."
    *Neuroscience* 6:763–773. (Precerebellar nuclei;
    reticulocerebellar projections — including the paramedian
    reticular nucleus.)
*   NeuroNames — Paramedian reticular nucleus; FMA — Paramedian
    reticular nucleus.
"""