"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gigantocellular_reticular_nucleus
=========================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── gigantocellular_reticular_nucleus   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Gigantocellular reticular nucleus; Gi; nucleus
gigantocellularis; nucleus reticularis gigantocellularis;
gigantocellular tegmental field (FTG); nucleus gigantocellularis
medullae oblongatae.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter reticular nucleus** in the **medial
reticular formation** of the **medulla oblongata** — a **large**,
**multifunctional** reticular nucleus involved in **respiratory
pattern modulation**, **autonomic regulation**, and **descending
pain modulation**. It is **NOT** the **paramedian reticular
nucleus** (a **different**, **smaller**, **more medial** reticular
nucleus wired under ``.../paramedian_reticular_nucleus/``), **NOT**
the **DRG** (a **dorsal respiratory group** in the **NTS
region**), **NOT** the **VRG** (a **ventrolateral** respiratory
rhythm and pattern generator group in a **separate container**),
and **NOT** the **parvocellular reticular nucleus** (a **smaller**
reticular nucleus, not wired in this tree).
**Part of:** The **respiratory_center** container
(``.../respiratory_center/``) — which is part of the **medulla
oblongata** — the **caudal brainstem** subdivision of the
**myelencephalon**. **The "respiratory_center" label is
PARTIALLY accurate** for this child — the Gi **is involved in
respiratory function** (among **other** functions), unlike the
**cuneate nucleus** (which is **somatosensory**, a **tree-wiring
artifact**) and unlike the **area postrema** / **CTZ** (which are
**circumventricular chemoreceptive**, not primarily
respiratory).
**Structural parent:** ``.../respiratory_center/`` → **direct
child** of the respiratory_center container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** gigantocellular
reticular nucleus. **Anatomically**, the left and right Gi are
**truly separate bilateral structures** (unlike the area
postrema, which is a midline organ wired as left/right by
convention) — the **left Gi** is in the **left medial reticular
formation**; the **right Gi** is in the **right medial reticular
formation**.
**Boundary status (NOT the paramedian reticular nucleus — a
DIFFERENT reticular nucleus in a DIFFERENT container):**
**Boundary case — the gigantocellular reticular nucleus is NOT
the paramedian reticular nucleus.** The **paramedian reticular
nucleus** (``.../paramedian_reticular_nucleus/``) is a
**smaller**, **more medial** medullary reticular nucleus — it is
a **cerebellar projection** nucleus with **nociceptive** and
**autonomic** roles, and it is **wired as its own container**
under ``medulla_oblongata``. **They are DIFFERENT RETICULAR
NUCLEI** — the **Gi** is **larger**, **more lateral**, and
**wired under** ``respiratory_center`` (with **respiratory**,
**autonomic**, and **pain-modulatory** roles); the
**paramedian reticular nucleus** is **smaller**, **more
medial**, and **wired separately** under
``medulla_oblongata``. Consumers must **not** conflate the two.
**Boundary status (NOT the dorsal respiratory group — a DIFFERENT
child of respiratory_center):** **Boundary case — the
gigantocellular reticular nucleus is NOT the dorsal respiratory
group (DRG).** The **DRG**
(``.../respiratory_center/dorsal_respiratory_group/``) is the
**dorsal respiratory** pattern generator in the **NTS region** —
it **relays pulmonary stretch receptor input** to the
**respiratory rhythm generator**. The **Gi** (here) is a
**ventrolateral** reticular nucleus with **broader**
respiratory, autonomic, and pain-modulatory functions — **NOT**
the dorsal respiratory pattern generator. **They are DIFFERENT
STRUCTURES** — children of ``respiratory_center`` — but they are
**functionally distinct** and **anatomically distinct** (the DRG
is **dorsal** in the **NTS region**; the Gi is
**ventrolateral**). Consumers must **not** conflate the two.
**Boundary status (NOT the ventral respiratory group — a
DIFFERENT respiratory generator in a DIFFERENT container):**
**Boundary case — the gigantocellular reticular nucleus is NOT
the ventral respiratory group (VRG).** The **VRG**
(``.../ventral_respiratory_group/``) is the **ventral
respiratory** rhythm and pattern generator group — containing
the **Bötzinger complex**, **pre-Bötzinger complex**, **nucleus
para-ambiguus**, **nucleus retroambiguus**, **nucleus
retrofacialis**, and **retrotrapezoid nucleus** — in the
**ventrolateral medulla**. The **Gi** (here) is a **medial
reticular** nucleus with **broader** functions. **They are
DIFFERENT STRUCTURES** in **DIFFERENT CONTAINERS** — the **Gi**
is a **reticular** nucleus (not a **VRG** subnucleus); the
**VRG** is a **respiratory rhythm** and **pattern** generator
group. They are **functionally coupled** (the Gi **modulates**
respiratory function **including** via **VRG projections** and
**respiratory pattern modulation**), but they are **anatomically
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the solitary nucleus (NTS) — a SEPARATE
container):** **Boundary case — the gigantocellular reticular
nucleus is NOT the solitary nucleus (NTS).** The **NTS**
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
it is a **separate container** under ``medulla_oblongata``. The
**Gi** (here) is a **reticular** nucleus in the **medial
reticular formation** — **NOT** the NTS. Consumers must **not**
conflate the two.
**Boundary status (NOT the area postrema or the chemoreceptor
trigger zone — DIFFERENT children of respiratory_center):**
**Boundary case — the gigantocellular reticular nucleus is NOT
the area postrema or the chemoreceptor trigger zone.** The
**area postrema** and **chemoreceptor trigger zone**
(``.../area_postrema/`` and
``.../chemoreceptor_trigger_zone/``) are **circumventricular
chemoreceptive** structures for the **vomiting reflex** — **NOT**
reticular nuclei. **They are DIFFERENT STRUCTURES** — children
of ``respiratory_center`` — but they are **functionally
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the cuneate or gracile nuclei — DIFFERENT
children of respiratory_center):** **Boundary case — the
gigantocellular reticular nucleus is NOT the cuneate or gracile
nucleus.** The **cuneate** and **gracile nuclei**
(``.../respiratory_center/cuneate_nucleus/`` and
``.../respiratory_center/gracile_nucleus/``) are the **dorsal
column somatosensory relays** (fine touch, vibration,
proprioception). **They are DIFFERENT STRUCTURES** — children
of ``respiratory_center`` — but they are **functionally
distinct**. The **Gi IS (partially) respiratory**; the
**cuneate and gracile nuclei are somatosensory**. Consumers must
**not** conflate them.
**Boundary status (NOT the parafacial zone — a sleep-promoting
region in a DIFFERENT container):** **Boundary case — the
gigantocellular reticular nucleus is NOT the parafacial zone.**
The **parafacial zone** (``.../parafacial_zone/``) is a
**GABAergic / glycinergic sleep-promoting** region — **NOT** a
reticular nucleus and **NOT** wired under
``respiratory_center``. Consumers must **not** conflate the two.
**Boundary status (NOT the RVLM or CVLM — autonomic structures in
DIFFERENT containers):** **Boundary case — the gigantocellular
reticular nucleus is NOT the RVLM or CVLM.** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor** center; the **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay. **They are DIFFERENT STRUCTURES**
in **DIFFERENT CONTAINERS** — the **Gi** is a **medial
reticular** nucleus with **broader** functions (including
**autonomic modulation**, **but NOT** being the **sympathetic
premotor** center or the **sympathoinhibitory** relay). Consumers
must **not** conflate the Gi with the RVLM or CVLM.
**Boundary status (NOT the parvocellular reticular nucleus — a
DIFFERENT reticular nucleus NOT wired in this tree):** **Boundary
case — the gigantocellular reticular nucleus is NOT the
parvocellular reticular nucleus.** The **parvocellular reticular
nucleus** (nucleus reticularis parvocellularis) is a
**different**, **smaller** reticular nucleus — it is **NOT
wired** in this tree. **In the literature**, it is **adjacent
to** the Gi and the paramedian reticular nucleus — but it is a
**different structure**. Consumers must **not** conflate the Gi
with the parvocellular reticular nucleus — resolve the
parvocellular reticular nucleus via the references.
**Boundary status (NOT the lateral reticular nucleus — a
DIFFERENT reticular nucleus NOT wired in this tree):** **Boundary
case — the gigantocellular reticular nucleus is NOT the lateral
reticular nucleus.** The **lateral reticular nucleus** (nucleus
reticularis lateralis) is a **cerebellar projection** nucleus —
it is **NOT wired** in this tree. **In the literature**, it is
**ventrolateral** to the Gi — but it is a **different
structure**. Consumers must **not** conflate the Gi with the
lateral reticular nucleus — resolve the lateral reticular nucleus
via the references.
**Boundary status (NOT the whole reticular formation — a specific
nucleus within it):** **Boundary case — the gigantocellular
reticular nucleus is NOT the whole medullary reticular
formation.** The **medullary reticular formation** is a
**distributed system** — it includes the **Gi** (here), the
**paramedian reticular nucleus**
(``.../paramedian_reticular_nucleus/``), the **parvocellular
reticular nucleus** (not wired here), the **lateral reticular
nucleus** (not wired here), and **other** reticular nuclei. The
**Gi** is **one specific nucleus** within the medullary reticular
formation — it is **NOT** the whole formation. Consumers must
**not** conflate the **Gi** with the **whole medullary reticular
formation**.
**Boundary status (NOT the whole respiratory_center — a CHILD of
it):** **Boundary case — the gigantocellular reticular nucleus
is NOT the whole respiratory_center.** The **respiratory_center**
(``.../respiratory_center/``) is the **parent container** — it
contains the **Gi** (here) **plus** the ``area_postrema``,
``chemoreceptor_trigger_zone``, ``cuneate_nucleus``,
``dorsal_respiratory_group``, and ``gracile_nucleus``. The **Gi**
is **one child** of that container. Consumers must **not**
conflate the **child** with the **whole container**.
**Boundary status (NOT the whole medulla oblongata — a reticular
nucleus within it):** **Boundary case — the gigantocellular
reticular nucleus is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the Gi (via the
respiratory_center) **plus** the cranial nerve nuclei, the
autonomic nuclei, the olivary body, the medullary pyramid, the
arcuate nucleus, the parafacial zone, the paramedian reticular
nucleus, the perihypoglossal nuclei, the respiratory_center, the
ventral respiratory group, and other structures. The **Gi** is
**one reticular nucleus** within the medulla. Consumers must
**not** conflate the **Gi** with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
ANATOMICALLY SEPARATE structures):** **Boundary case — the
gigantocellular reticular nucleus is a BILATERAL container whose
left and right children are ANATOMICALLY SEPARATE.** Unlike the
**area postrema** (a **midline** organ wired as left/right by
convention), the **Gi** is a **truly paired** medullary
structure — the **left Gi** is in the **left medial reticular
formation**; the **right Gi** is in the **right medial reticular
formation**. **The left / right split here is ANATOMICAL, not a
wiring convention.** Consumers must **not** infer **midline
wiring convention** from the Gi (that convention applies to the
area postrema / CTZ, NOT the Gi).

Overview
--------
The **gigantocellular reticular nucleus (Gi)** — also known as the
**nucleus gigantocellularis** — is a **large**, **multifunctional**
medullary reticular nucleus in the **medial reticular formation**
of the **medulla oblongata**. It is **involved in** at least
**three** functional systems:
*   **Respiratory modulation** — the Gi **modulates respiratory
    pattern** (including **inspiratory** and **expiratory**
    timing) via its projections to the **respiratory rhythm**
    and **pattern** generators (VRG, DRG) and to the **spinal
    cord** respiratory motor neurons. **This is why it is wired
    under** ``respiratory_center``.
*   **Autonomic regulation** — the Gi **participates** in
    **cardiovascular**, **gastrointestinal**, and **other**
    autonomic regulation via its projections to the **RVLM**,
    **CVLM**, **NTS**, and **spinal cord** autonomic
    preganglionic neurons.
*   **Descending pain modulation** — the Gi is a **key node** in
    the **descending pain-modulating** system — it **receives**
    input from the **periaqueductal gray (PAG)** and **projects**
    to the **spinal cord dorsal horn** (via the **dorsolateral
    funiculus**), **modulating** **nociceptive** transmission.
    The Gi **contributes** to **stress-induced analgesia** and
    **descending inhibition** of pain.

**The Gi is a MULTIFUNCTIONAL reticular nucleus, NOT a single-function
respiratory nucleus.** The **"respiratory_center"** label is
**partially accurate** — the Gi **IS involved in respiratory
function**, but it is **also** involved in **autonomic** and
**pain-modulatory** function. **Unlike the cuneate nucleus** (a
somatosensory tree-wiring artifact under ``respiratory_center``),
the Gi **does** have a **genuine respiratory role**; but
**unlike the DRG** (a **pure respiratory** pattern generator),
the Gi has **broader** functions. Consumers must **not** assume
that **every** Gi function is **respiratory** — the Gi's
**autonomic** and **pain-modulatory** roles are **equally
important**.

**The Gi is OFTEN PAIRED WITH THE PARAMEDIAN RETICULAR NUCLEUS
in the literature** as **part** of the **medullary reticular
formation** — but **the two are DIFFERENT NUCLEI**, and **this
tree wires them separately**: the **Gi** under
``respiratory_center``; the **paramedian reticular nucleus**
under ``medulla_oblongata`` as its **own container**. The tree
**separates** the two as a **deliberate wiring choice** — the
**Gi** is **wired with the respiratory cluster**; the
**paramedian reticular nucleus** is **wired standalone** (with
its **own** cerebellum-projection and nociception functions).

**The Gi is TRULY BILATERAL — the left / right split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **left** and **right**
Gi are **anatomically separate structures** — the **left Gi** is
in the **left medial reticular formation**; the **right Gi** is
in the **right medial reticular formation**. The **left / right
split** here reflects **anatomy** — **NOT** a **tree-wiring
convention**.

**The Gi is functionally coupled to the VRG, the DRG, the NTS,
the RVLM, the CVLM, the PAG, the thalamus, the hypothalamus, and
the spinal cord dorsal horn.** It is **part of** the
**reticular formation's** **distributed integrative network** —
a **multi-target** system for **respiration**, **autonomic
function**, **pain modulation**, and **arousal**.

Bilateral Structure (Anatomical Pairing)
---------------------------------------
The gigantocellular reticular nucleus is a **bilateral container**
in this tree with **two structural children**:

*   ``left`` — the **left** Gi (a **leaf** module).
*   ``right`` — the **right** Gi (a **leaf** module).

**The two children are ANATOMICALLY SEPARATE structures** —
**NOT** a wiring convention for a midline organ (unlike the
area postrema / CTZ). The **left Gi** is in the **left medial
reticular formation**; the **right Gi** is in the **right
medial reticular formation**.

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **Gi** as **single structures**. Consumers
that need **side-specific** resolution descend into ``left`` or
``right``; consumers that need the **whole bilateral pair** use
``gigantocellular_reticular_nucleus`` (the container) as a whole.

**The container itself is unpaired.** There is **no**
``gigantocellular_reticular_nucleus/left/.../`` structural
hierarchy beyond the single leaf level — the ``left`` and
``right`` modules are the **terminal modules** for this
structure.

The Gigantocellular Reticular Nucleus / Paramedian Reticular Nucleus Boundary
-----------------------------------------------------------------------------
This is the **most consequential** reticular-nucleus boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **larger**, **more lateral** medullary reticular nucleus —
    **wired under** ``respiratory_center``.

*   **Paramedian reticular nucleus**
    (``.../paramedian_reticular_nucleus/``) — the **smaller**,
    **more medial** medullary reticular nucleus — **wired
    standalone** under ``medulla_oblongata``.

**They are DIFFERENT RETICULAR NUCLEI** — the **Gi** is **larger**,
**more lateral**, and **wired under** ``respiratory_center``; the
**paramedian reticular nucleus** is **smaller**, **more medial**,
and **wired standalone**. The **tree separates** the two as a
**deliberate wiring choice**. Consumers must **not** conflate the
two.

The Gigantocellular Reticular Nucleus / Dorsal Respiratory Group Boundary
-------------------------------------------------------------------------
This is the **ventrolateral reticular / dorsal respiratory** (both
under `respiratory_center`) boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **ventrolateral reticular** nucleus with **respiratory**,
    **autonomic**, and **pain-modulatory** functions.

*   **Dorsal respiratory group** (DRG)
    (``.../respiratory_center/dorsal_respiratory_group/``) — the
    **dorsal respiratory** pattern generator in the **NTS
    region**.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**
and **anatomically distinct** (the DRG is **dorsal** in the
**NTS region**; the Gi is **ventrolateral**). Consumers must
**not** conflate the two.

The Gigantocellular Reticular Nucleus / Ventral Respiratory Group Boundary
--------------------------------------------------------------------------
This is the **reticular / respiratory-rhythm** boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **ventrolateral reticular** nucleus.

*   **Ventral respiratory group** (VRG)
    (``.../ventral_respiratory_group/``) — the **ventral
    respiratory** rhythm and pattern generator group
    (Bötzinger complex, pre-Bötzinger complex, nucleus
    para-ambiguus, nucleus retroambiguus, nucleus retrofacialis,
    retrotrapezoid nucleus).

**They are DIFFERENT STRUCTURES** in **DIFFERENT CONTAINERS** —
the **Gi** is a **reticular** nucleus (not a **VRG** subnucleus);
the **VRG** is a **respiratory rhythm** and **pattern** generator
group. Consumers must **not** conflate the two.

The Gigantocellular Reticular Nucleus / Solitary Nucleus Boundary
-----------------------------------------------------------------
This is the **reticular / visceral-afferent** boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **ventrolateral reticular** nucleus.

*   **Solitary nucleus (NTS)** (``.../solitary_nucleus/``) — the
    **visceral afferent relay**.

**They are DIFFERENT STRUCTURES** in **DIFFERENT CONTAINERS.**
Consumers must **not** conflate the two.

The Gigantocellular Reticular Nucleus / Area Postrema and Chemoreceptor Trigger Zone Boundary
--------------------------------------------------------------------------------------------
This is the **reticular / circumventricular** boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **ventrolateral reticular** nucleus.

*   **Area postrema** and **chemoreceptor trigger zone**
    (``.../area_postrema/`` and
    ``.../chemoreceptor_trigger_zone/``) — the **circumventricular
    chemoreceptive** structures for the **vomiting reflex**.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Gigantocellular Reticular Nucleus / Cuneate and Gracile Nuclei Boundary
---------------------------------------------------------------------------
This is the **reticular / somatosensory** boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **ventrolateral reticular** nucleus.

*   **Cuneate nucleus** and **gracile nucleus**
    (``.../respiratory_center/cuneate_nucleus/`` and
    ``.../respiratory_center/gracile_nucleus/``) — the **dorsal
    column somatosensory** relays.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
Consumers must **not** conflate them.

The Gigantocellular Reticular Nucleus / Parafacial Zone, RVLM, and CVLM Boundary
--------------------------------------------------------------------------------
This is the **reticular / sleep-promoting-and-autonomic** boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **ventrolateral reticular** nucleus.

*   **Parafacial zone** (``.../parafacial_zone/``) — the
    **GABAergic / glycinergic sleep-promoting** region.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) — the
    **sympathetic premotor** center.

*   **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **sympathoinhibitory** relay.

**They are DIFFERENT STRUCTURES** in **DIFFERENT CONTAINERS.**
Consumers must **not** conflate the Gi with any of these.

The Gigantocellular Reticular Nucleus / Parvocellular and Lateral Reticular Nuclei Boundary
------------------------------------------------------------------------------------------
This is the **Gi / other-reticular-nuclei** boundary:

*   **Gigantocellular reticular nucleus** (this module) — the
    **large**, **medial** reticular nucleus.

*   **Parvocellular reticular nucleus** — a **smaller**,
    **adjacent** reticular nucleus — **NOT wired** in this tree.

*   **Lateral reticular nucleus** — a **cerebellar projection**
    nucleus — **NOT wired** in this tree.

**They are DIFFERENT RETICULAR NUCLEI** — the **Gi** is **larger**,
**medial**, and **wired here**; the **parvocellular** and
**lateral** reticular nuclei are **smaller** / **more lateral**
and **NOT wired here**. Consumers must **not** conflate the Gi
with either.

The Gigantocellular Reticular Nucleus / Whole Respiratory Center and Whole Medulla Oblongata Boundary
----------------------------------------------------------------------------------------------------
This is the **child / container** boundary:

*   **Gigantocellular reticular nucleus** (this module) — one
    **child** of ``respiratory_center``.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children**.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The Gi is a CHILD of respiratory_center, NOT the container
itself, and NOT the whole medulla.** Consumers must **not**
conflate the **child** with either **parent container**.

Function in the Human Brain
---------------------------
The gigantocellular reticular nucleus's functions are
**multifunctional** — **respiratory modulation**, **autonomic
regulation**, and **descending pain modulation** — **NOT motor
conduction** and **NOT primary respiratory rhythm generation**:

*   **Respiratory modulation:** The **Gi** **modulates
    respiratory pattern** — it **contributes** to
    **inspiratory** and **expiratory** timing and to **respiratory
    pattern** (rate, depth, and **integration** with the
    **VRG** and **DRG**). It **receives** input from the
    **VRG**, **DRG**, **NTS**, **pons**, **hypothalamus**, and
    **cortex** — and it **projects** to the **respiratory
    pattern** generators and the **spinal cord** respiratory
    motor neurons.

*   **Autonomic regulation:** The **Gi** **participates** in
    **cardiovascular**, **gastrointestinal**, and **other**
    autonomic regulation — it **receives** input from the
    **NTS**, **RVLM**, **CVLM**, and **hypothalamus** — and it
    **projects** to the **RVLM**, **CVLM**, **NTS**, and the
    **spinal cord** autonomic preganglionic neurons.

*   **Descending pain modulation:** The **Gi** is a **key node**
    in the **descending pain-modulating** system — it
    **receives** input from the **periaqueductal gray (PAG)**
    and **projects** to the **spinal cord dorsal horn** (via the
    **dorsolateral funiculus**), **modulating** **nociceptive**
    transmission. The Gi **contributes** to **stress-induced
    analgesia** and **descending inhibition** of pain.

*   **Arousal and reticular activating system:** The **Gi**
    **contributes** to the **ascending reticular activating
    system (ARAS)** — it **projects** to the **thalamus** and
    **cortex** and **contributes** to **arousal** and
    **wakefulness**.

*   **NOT motor conduction:** The **Gi** does **not** send motor
    axons to muscles.

*   **NOT primary respiratory rhythm generation:** The
    **respiratory rhythm** is generated by the **pre-Bötzinger
    complex** (VRG) — **NOT** the Gi. The Gi **modulates** the
    respiratory pattern but **does not generate** the **rhythm**.

**The unifying theme:** the gigantocellular reticular nucleus is
a **multifunctional ventrolateral reticular nucleus** —
**respiratory modulation**, **autonomic regulation**,
**descending pain modulation**, and **ARAS arousal** — **NOT**
a pure respiratory structure (unlike the DRG) and **NOT** a
somatosensory tree-wiring artifact (unlike the cuneate nucleus).

Associated Disorders
--------------------
The gigantocellular reticular nucleus is the **substrate** for
**well-defined clinical syndromes** — its clinical relevance is
**direct** and **indirect**, via **respiratory**, **autonomic**,
and **pain-modulatory** dysfunction:

*   **Central hypoventilation (via Gi dysfunction — indirect and
    partial):** **Damage** to the **Gi** can **contribute** to
    **central hypoventilation** — **impaired** respiratory
    pattern **modulation** — but the **primary** rhythm
    generators are the **pre-Bötzinger complex** (VRG) and
    other **brainstem** structures. **Isolated Gi lesions**
    rarely cause **full-blown central hypoventilation** — the
    **VRG**, **DRG**, and **higher centers** can partially
    compensate.

*   **Chronic pain (via Gi dysfunction — hypothesized):**
    **Impaired** descending **pain modulation** from the **Gi**
    could contribute to **chronic pain** syndromes
    (fibromyalgia, neuropathic pain). The **Gi** is **part of**
    the **descending pain-modulating** system — but **not** the
    **sole** or **primary** substrate.

*   **Autonomic dysfunction (via Gi involvement —
    hypothesized):** **Damage** to the **Gi** could contribute
    to **autonomic** dysregulation — but the **RVLM**, **CVLM**,
    and **NTS** are the **primary** autonomic substrates.

*   **Sleep-disordered breathing (via Gi involvement —
    hypothesized):** **Gi** dysfunction may **contribute** to
    **sleep-disordered breathing** (central sleep apnea,
    hypopneas) — but the **primary** central control of
    breathing during sleep is the **pre-Bötzinger complex**
    (VRG) and **higher** centers.

*   **Brainstem stroke (via Gi involvement):** **Medullary
    stroke** can **involve** the **Gi** — contributing to
    **respiratory pattern** abnormalities, **autonomic**
    instability, and **pain**-related dysfunction.

*   **No Named "Gigantocellular Reticular Nucleus Syndrome":** The
    Gi is a **multifunctional reticular nucleus** — its clinical
    syndromes are **named for the broader lesion** (brainstem
    stroke) or the **functional abnormality** (central
    hypoventilation, chronic pain, autonomic dysfunction) —
    **NOT** for the Gi itself.

**What is NOT here:** The Gi is **not** the substrate for
**primary respiratory rhythm generation** (pre-Bötzinger complex,
VRG), **emesis** (area postrema / CTZ), **somatosensory loss**
(cuneate / gracile nuclei), **sympathetic premotor** function
(RVLM), **sympathoinhibitory** function (CVLM), **visceral
afferent relay** (NTS), **tongue weakness** (hypoglossal
nucleus), or **parasympathetic dysfunction** (dorsal motor
nucleus of the vagus). Its clinical relevance is the
**respiratory modulation**, **autonomic regulation**, and
**descending pain modulation** functions listed above.

Lateralization Notes
--------------------
The gigantocellular reticular nucleus is a **bilateral container**
in this tree with ``left`` and ``right`` structural children.
There is **no** ``gigantocellular_reticular_nucleus/left/.../``
structural hierarchy beyond the single leaf level.

*   **Bilateral structural children (ANATOMICAL pairing):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left** or **right** Gi as a **single structure**. The
    **left** and **right** Gi are **anatomically separate
    structures** (unlike the **area postrema**, which is a
    **midline** organ wired as left/right by convention). The
    **left** Gi is in the **left medial reticular formation**;
    the **right** Gi is in the **right medial reticular
    formation**.

*   **Bilateral symmetry:** The **left** and **right** Gi are
    **structurally symmetric mirror pairs** — same
    cytoarchitecture, same projections, same functions.

*   **Bilateral projections:** Most **Gi** projections are
    **bilateral** — the left Gi and right Gi both project to
    the **bilateral** respiratory, autonomic, and pain-modulatory
    targets. This is a **bilaterally distributed** functional
    system — a **unilateral** lesion is usually **partially
    compensated** by the **contralateral** Gi.

*   **NO lateralization warning:** The Gi has **no known
    functional lateralization** in humans — the **left** and
    **right** Gi are **functionally symmetric**. Consumers must
    **not** import a **lateralization warning** into the Gi —
    the **left** and **right** sides are **functionally
    symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The Gi is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the Gi.

*   **NO Fear-Output Warning:** The Gi is **not** a fear-output
    structure — it is a **ventrolateral multifunctional
    reticular** nucleus. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left Gi = right Gi" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The Gi is
a **strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The Gi is a **bilateral
    container** — it does **not** import from ``left/`` or
    ``right/`` at the container level. The ``left`` and
    ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../paramedian_reticular_nucleus/``,
    ``.../ventral_respiratory_group/``,
    ``.../solitary_nucleus/``,
    ``.../area_postrema/``,
    ``.../chemoreceptor_trigger_zone/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../dorsal_respiratory_group/``,
    ``.../parafacial_zone/``,
    ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``, or any other
    container. The Gi's relationships to the paramedian reticular
    nucleus, VRG, NTS, area postrema, CTZ, cuneate nucleus,
    gracile nucleus, dorsal respiratory group, parafacial zone,
    RVLM, and CVLM are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children (ANATOMICAL
    pairing).** The structural children are ``left`` and
    ``right``, each a **leaf**. **Anatomically**, the left and
    right Gi are **truly separate bilateral structures** — the
    **left / right split** is **ANATOMICAL**, **NOT** a
    **tree-wiring convention**.
*   **MULTIFUNCTIONAL reticular nucleus — respiratory,
    autonomic, and pain-modulatory.** Unlike the cuneate nucleus
    (somatosensory) and unlike the DRG (pure respiratory), the
    **Gi** is **multifunctional** — the **"respiratory_center"**
    label is **partially accurate** for this child.
*   **DISTINCT from the paramedian reticular nucleus.** The
    **paramedian reticular nucleus** is a **different**,
    **smaller**, **more medial** reticular nucleus — **wired
    separately** under ``medulla_oblongata``. The tree
    **separates** the two as a **deliberate wiring choice**.
*   **NOT the DRG.** The **DRG** is the **dorsal respiratory**
    pattern generator in the **NTS region** — a **different**
    child of ``respiratory_center``.
*   **NOT the VRG.** The **VRG** is a **separate container** —
    the **Gi** is a **reticular** nucleus, not a **VRG**
    subnucleus.
*   **NOT the NTS, area postrema, CTZ, cuneate nucleus, or
    gracile nucleus.** Each is a **different structure**.
*   **NOT the parafacial zone, RVLM, or CVLM.** Each is a
    **different structure** in a **different container**.
*   **NOT the parvocellular or lateral reticular nuclei.** Those
    are **different reticular nuclei** — **NOT wired** in this
    tree.
*   **NOT the whole respiratory_center or whole medulla
    oblongata.** The Gi is a **child** of ``respiratory_center``,
    not the container itself.
*   **No ``AREA_PATHS`` hop.** The Gi is a **local container** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The Gi has no nested
    dual-framing module. It is a **bilateral container** with
    **two leaf children** (anatomical pairing).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **multifunctional
    reticular** framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center import gigantocellular_reticular_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.gigantocellular_reticular_nucleus"
    )

**Do not** assume the Gi is a **pure respiratory** structure.
The Gi is **multifunctional** — **respiratory modulation**,
**autonomic regulation**, and **descending pain modulation**.
The **"respiratory_center"** label is **partially accurate**.

**Do not** assume the Gi is the **paramedian reticular
nucleus**. The paramedian reticular nucleus is a **different**,
**smaller**, **more medial** reticular nucleus — **wired
separately** under ``medulla_oblongata``.

**Do not** assume the Gi is the **dorsal respiratory group**.
The DRG is the **dorsal respiratory** pattern generator in the
**NTS region** — a **different** child of ``respiratory_center``.

**Do not** assume the Gi is the **ventral respiratory group
(VRG)**. The VRG is a **separate container** under
``medulla_oblongata``.

**Do not** assume the Gi is the **solitary nucleus (NTS)**,
**area postrema**, **chemoreceptor trigger zone**,
**cuneate nucleus**, or **gracile nucleus**. Each is a
**different structure**.

**Do not** assume the Gi is the **parafacial zone**, the
**RVLM**, or the **CVLM**. Each is a **different structure** in
a **different container**.

**Do not** assume the Gi is the **parvocellular** or **lateral**
reticular nucleus. Those are **different reticular nuclei** —
**NOT wired** in this tree.

**Do not** assume the Gi is the **whole respiratory_center** or
the **whole medulla oblongata**. It is a **child** of
``respiratory_center``.

**Do not** infer **midline wiring convention** from the Gi
structure. The **left / right split** is **ANATOMICAL** — the
**left** and **right** Gi are **truly separate bilateral
structures**.

Iterating the Gi's structural children (recommended consumer
pattern)::

    GIGANTOCELLULAR_RETICULAR_NUCLEUS_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # gigantocellular reticular nucleus. Anatomically, the left
    # and right Gi are TRULY SEPARATE bilateral structures — the
    # left/right split is ANATOMICAL, NOT a wiring convention.

Reaching the left and right Gi leaves (recommended consumer
pattern)::

    # The left and right Gi leaves are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gigantocellular_reticular_nucleus.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gigantocellular_reticular_nucleus.right
    #
    # Each is a leaf module representing the Gi of that side.
    # Anatomically, they are TRULY SEPARATE bilateral structures.

Reaching the paramedian reticular nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The paramedian reticular nucleus is a SEPARATE container
    # under medulla_oblongata — NOT wired under
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.paramedian_reticular_nucleus
    #
    # The Gi and the paramedian reticular nucleus are DIFFERENT
    # RETICULAR NUCLEI — the Gi is larger, more lateral, and
    # wired under respiratory_center; the paramedian reticular
    # nucleus is smaller, more medial, and wired standalone.

Reaching the ventral respiratory group (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The ventral respiratory group is a SEPARATE container under
    # medulla_oblongata — NOT wired under respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #
    # The Gi (a reticular nucleus) and the VRG (a respiratory
    # rhythm/pattern generator group) are DIFFERENT STRUCTURES in
    # DIFFERENT CONTAINERS.

Reaching the DRG (recommended consumer pattern — NOTE the
DIFFERENT child of respiratory_center)::

    # The dorsal respiratory group is a DIFFERENT child of
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group
    #
    # The Gi and the DRG are DIFFERENT STRUCTURES — both children
    # of respiratory_center — but the DRG is a DORSAL respiratory
    # pattern generator in the NTS region; the Gi is a
    # VENTROLATERAL multifunctional reticular nucleus.

Reaching the area postrema and CTZ (recommended consumer
pattern — NOTE the DIFFERENT children of respiratory_center)::

    # The area postrema and the chemoreceptor trigger zone are
    # CIRCUMVENTRICULAR structures — children of
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone
    #
    # They are NOT reticular nuclei — they are chemoreceptive /
    # emetic structures.

Reaching the cuneate and gracile nuclei (recommended consumer
pattern — NOTE the DIFFERENT children of respiratory_center)::

    # The cuneate and gracile nuclei are SOMATOSENSORY relays —
    # children of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus
    #
    # They are NOT reticular nuclei — they are dorsal column
    # somatosensory relays (wired under respiratory_center as a
    # tree-wiring artifact).

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"respiratory_center.gigantocellular_reticular_nucleus.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: the left and right Gi are TRULY SEPARATE
        # bilateral structures (ANATOMICAL, not a wiring
        # convention).

References
----------
*   **Canonical brainstem reticular anatomy:** Brodal, A. (2010).
    *The Central Nervous System: Structure and Function*, 4th ed.
    (Medullary reticular formation; gigantocellular reticular
    nucleus; paramedian reticular nucleus; parvocellular
    reticular nucleus; lateral reticular nucleus.)
*   **Gigantocellular reticular nucleus — overview:** Newman,
    D.B. (1985). "Distinguishing rat medullary reticular
    formation regions by afferent and efferent connections."
    *Brain Research* 326:129–138. (Gigantocellular reticular
    nucleus; afferent and efferent connections; functional
    distinction from other medullary reticular nuclei.)
*   **Gigantocellular reticular nucleus — respiratory function:**
    Bianchi, A.L., et al. (1995). "Central control of breathing
    in mammals: neuronal circuitry, membrane properties, and
    neurotransmitters." *Physiological Reviews* 75:1–45.
    (Gigantocellular reticular nucleus; respiratory pattern
    modulation; integration with VRG and DRG.)
*   **Gigantocellular reticular nucleus — autonomic function:**
    Loewy, A.D., Spyer, K.M. (1990). *Central Regulation of
    Autonomic Functions.* (Gigantocellular reticular nucleus;
    autonomic integration; projections to RVLM, CVLM, and NTS.)
*   **Gigantocellular reticular nucleus — descending pain
    modulation:** Basbaum, A.I., Fields, H.L. (1984).
    "Endogenous pain control systems: brainstem spinal pathways
    and endorphin circuitry." *Annual Review of Neuroscience*
    7:309–338. (Descending pain modulation; medullary reticular
    nuclei including the gigantocellular reticular nucleus.)
*   **Gigantocellular reticular nucleus — pain modulation:**
    Fields, H.L., Basbaum, A.I. (1994). "Central nervous system
    mechanisms of pain modulation." In: *Textbook of Pain*, 3rd
    ed. (Gigantocellular reticular nucleus; PAG → Gi → spinal
    cord dorsal horn pathway; stress-induced analgesia.)
*   **Gigantocellular reticular nucleus — ARAS:** Moruzzi, G.,
    Magoun, H.W. (1949). "Brain stem reticular formation and
    activation of the EEG." *Electroencephalography and Clinical
    Neurophysiology* 1:455–473. (Ascending reticular activating
    system; reticular nuclei including the gigantocellular
    reticular nucleus.)
*   **Paramedian reticular nucleus (contrast — separate
    container):** Newman, D.B., Ginsberg, C.Y. (1992). "Brainstem
    reticular nuclei of the cat: I. Sources of the
    reticulocerebellar projection." *Neuroscience* 47:149–168.
    (Paramedian reticular nucleus — distinct from the
    gigantocellular reticular nucleus.)
*   **Ventral respiratory group (contrast — separate
    container):** Feldman, J.L., Del Negro, C.A. (2006). "Looking
    for inspiration: new perspectives on respiratory rhythm."
    *Nature Reviews Neuroscience* 7:232–242. (Ventral respiratory
    group; pre-Bötzinger complex — separate from the Gi.)
*   **Dorsal respiratory group (contrast — different child of
    respiratory_center):** Kubin, L., Davies, R.O. (1988).
    "Central coordination of respiratory and sympathetic
    activities." *Annual Review of Physiology* 50:63–74. (Dorsal
    respiratory group — different from the Gi.)
*   **Solitary nucleus (contrast — separate container):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS — separate from
    the Gi.)
*   **RVLM and CVLM (contrast — separate containers):** Guyenet,
    P.G. (2006). "The sympathetic control of blood pressure."
    *Nature Reviews Neuroscience* 7:335–346. (RVLM; CVLM —
    separate from the Gi.)
*   NeuroNames — Nucleus gigantocellularis; FMA — Gigantocellular
    reticular nucleus.
"""