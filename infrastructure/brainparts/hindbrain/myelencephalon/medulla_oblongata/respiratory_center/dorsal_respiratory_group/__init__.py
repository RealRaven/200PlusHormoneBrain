"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group
===============================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── dorsal_respiratory_group   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Dorsal respiratory group; DRG; dorsal
respiratory group of the NTS; dorsal respiratory group of the
nucleus tractus solitarius; NTS respiratory region; ventrolateral
NTS respiratory column.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** — a **functionally defined
group** of **respiratory-related neurons** in the **ventrolateral
region of the nucleus tractus solitarius (NTS)** in the **dorsal
medulla oblongata**. It is **involved in inspiratory pattern
generation** and **relays pulmonary stretch receptor input**
(via **vagal afferents**) to the **respiratory rhythm
generator**. It is a **respiratory structure** — **NOT** a
somatosensory relay, **NOT** a circumventricular organ, and
**NOT** a reticular nucleus. **Unlike the cuneate nucleus** (a
somatosensory tree-wiring artifact under ``respiratory_center``),
**the DRG IS actually respiratory** — the **"respiratory_center"**
label is **functionally accurate** for this child.
**Part of:** The **respiratory_center** container
(``.../respiratory_center/``) — which is part of the **medulla
oblongata** — the **caudal brainstem** subdivision of the
**myelencephalon**. **Unlike the cuneate nucleus**, the DRG is a
**respiratory structure** — the **"respiratory_center"** label
is **NOT a tree-wiring artifact** for this child. **Unlike the
area postrema / CTZ**, the DRG is **NOT a midline organ** — it
is a **truly bilateral structure**.
**Structural parent:** ``.../respiratory_center/`` → **direct
child** of the respiratory_center container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** dorsal
respiratory group. **Anatomically**, the left and right DRG are
**truly separate bilateral structures** (unlike the area
postrema, which is a midline organ wired as left/right by
convention) — the **left DRG** is in the **left NTS region**;
the **right DRG** is in the **right NTS region**.
**Boundary status (NOT the ventral respiratory group — a
DIFFERENT respiratory generator in a DIFFERENT container):**
**Boundary case — the dorsal respiratory group is NOT the
ventral respiratory group (VRG).** The **VRG**
(``.../ventral_respiratory_group/``) is the **ventral
respiratory** rhythm and pattern generator group — containing
the **Bötzinger complex**, **pre-Bötzinger complex**, **nucleus
para-ambiguus**, **nucleus retroambiguus**, **nucleus
retrofacialis**, and **retrotrapezoid nucleus** — in the
**ventrolateral medulla**. **They are DIFFERENT RESPIRATORY
STRUCTURES** in **DIFFERENT CONTAINERS** — the **DRG** is
**dorsal** (in the **NTS region**); the **VRG** is
**ventrolateral**. They are **functionally coupled** — the DRG
**relays** input to the VRG's **pre-Bötzinger complex** (the
**primary respiratory rhythm generator**) — but they are
**anatomically distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the solitary nucleus (NTS) — the NTS is
the parent region in the literature, wired as a SEPARATE
container in this tree):** **Boundary case — the dorsal
respiratory group is NOT the solitary nucleus (NTS).** The
**solitary nucleus** (``.../solitary_nucleus/``) is the
**visceral afferent relay** — it is a **separate container**
under ``medulla_oblongata``. **In the literature**, the **DRG**
is **often considered part of** the **NTS** — it is in the
**ventrolateral NTS region**. **In this tree**, the **DRG** is
**wired as a separate child** of ``respiratory_center``, **NOT**
under the **NTS container**. Consumers must **not** expect to
find the DRG under ``solitary_nucleus`` — resolve it via
``respiratory_center.dorsal_respiratory_group``. **The tree
separates** the **NTS** and the **DRG** into **two modules** as
a **deliberate wiring choice** — the **DRG** is a **functional
respiratory group within the NTS region**; the **NTS** is the
**broader visceral afferent relay** of which the **DRG** is a
**functional subregion**.
**Boundary status (NOT the area postrema or the chemoreceptor
trigger zone — DIFFERENT children of respiratory_center):**
**Boundary case — the dorsal respiratory group is NOT the area
postrema or the chemoreceptor trigger zone.** The **area
postrema** and **chemoreceptor trigger zone**
(``.../area_postrema/`` and
``.../chemoreceptor_trigger_zone/``) are **circumventricular
chemoreceptive** structures for the **vomiting reflex** — **NOT**
respiratory pattern generators. **They are DIFFERENT
STRUCTURES** — children of ``respiratory_center`` — but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the cuneate or gracile nuclei — DIFFERENT
children of respiratory_center):** **Boundary case — the dorsal
respiratory group is NOT the cuneate or gracile nucleus.** The
**cuneate** and **gracile nuclei**
(``.../respiratory_center/cuneate_nucleus/`` and
``.../respiratory_center/gracile_nucleus/``) are the **dorsal
column somatosensory relays** (fine touch, vibration,
proprioception). **They are DIFFERENT STRUCTURES** — children
of ``respiratory_center`` — but they are **functionally
distinct**. The **DRG IS respiratory**; the **cuneate and
gracile nuclei are somatosensory**. Consumers must **not**
conflate them.
**Boundary status (NOT the gigantocellular reticular nucleus —
a DIFFERENT child of respiratory_center):** **Boundary case —
the dorsal respiratory group is NOT the gigantocellular reticular
nucleus (Gi).** The **gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/``)
is a **large medullary reticular** nucleus — it is involved in
**respiration**, **autonomic function**, and **descending pain
modulation**. **They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct** —
the **DRG** is a **dorsal respiratory pattern generator** in the
**NTS region**; the **Gi** is a **ventrolateral reticular
nucleus** with **broader** respiratory, autonomic, and pain
functions. Consumers must **not** conflate the two.
**Boundary status (NOT the parafacial zone — a sleep-promoting
region in a DIFFERENT container):** **Boundary case — the
dorsal respiratory group is NOT the parafacial zone.** The
**parafacial zone** (``.../parafacial_zone/``) is a
**GABAergic / glycinergic sleep-promoting** region — **NOT** a
respiratory pattern generator and **NOT** wired under
``respiratory_center``. Consumers must **not** conflate the two.
**Boundary status (NOT the retrotrapezoid nucleus, Bötzinger
complex, pre-Bötzinger complex, or other VRG subnuclei —
DIFFERENT structures in a DIFFERENT container):** **Boundary
case — the dorsal respiratory group is NOT the retrotrapezoid
nucleus, the Bötzinger complex, the pre-Bötzinger complex, or
any other VRG subnucleus.** Those are **ventral respiratory**
structures — wired under the **separate** ``ventral_respiratory_group``
container. **They are DIFFERENT STRUCTURES** from the dorsal
respiratory group — different **dorsoventral position**,
different **functions** (VRG = rhythm / pattern; DRG =
pulmonary stretch relay / inspiratory pattern). Consumers must
**not** conflate the DRG with any VRG subnucleus.
**Boundary status (NOT the NTS or the vagal afferent system —
the DRG RECEIVES vagal input but is NOT the vagus itself):**
**Boundary case — the dorsal respiratory group is NOT the
solitary nucleus (NTS) or the vagal afferent system.** The
**DRG** **receives** **pulmonary stretch receptor** input via
**vagal afferents** — those **afferents** **synapse** in the
**NTS region** (which is anatomically the **DRG's home region**)
— but the **DRG neurons** are **second-order respiratory
neurons**, **NOT** primary afferent neurons. Consumers must
**not** conflate the DRG with the vagal afferent system itself.
**Boundary status (NOT the whole respiratory_center — a CHILD of
it):** **Boundary case — the dorsal respiratory group is NOT
the whole respiratory_center.** The **respiratory_center**
(``.../respiratory_center/``) is the **parent container** — it
contains the **DRG** (here) **plus** the ``area_postrema``,
``chemoreceptor_trigger_zone``, ``cuneate_nucleus``,
``gigantocellular_reticular_nucleus``, and ``gracile_nucleus``.
The **DRG** is **one child** of that container. Consumers must
**not** conflate the **child** with the **whole container**.
**Boundary status (NOT the whole medulla oblongata — a
respiratory group within the NTS region):** **Boundary case —
the dorsal respiratory group is NOT the whole medulla
oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the DRG (via the respiratory_center) **plus** the
cranial nerve nuclei, the autonomic nuclei, the olivary body,
the medullary pyramid, the arcuate nucleus, the parafacial zone,
the paramedian reticular nucleus, the perihypoglossal nuclei,
the respiratory_center, the ventral respiratory group, and
other structures. The **DRG** is **one respiratory group**
within the medulla. Consumers must **not** conflate the **DRG**
with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
ANATOMICALLY SEPARATE structures):** **Boundary case — the
dorsal respiratory group is a BILATERAL container whose left and
right children are ANATOMICALLY SEPARATE.** Unlike the **area
postrema** (a **midline** organ wired as left/right by
convention), the **DRG** is a **truly paired** medullary
structure — the **left DRG** is in the **left NTS region** (in
the **left dorsal medulla**); the **right DRG** is in the
**right NTS region** (in the **right dorsal medulla**). **The
left / right split here is ANATOMICAL, not a wiring
convention.** Consumers must **not** infer **midline wiring
convention** from the DRG (that convention applies to the area
postrema / CTZ, NOT the DRG).

Overview
--------
The **dorsal respiratory group (DRG)** is a **respiratory-related
group of neurons** in the **ventrolateral region of the nucleus
tractus solitarius (NTS)** in the **dorsal medulla oblongata**.
It is **involved in inspiratory pattern generation** and
**relays pulmonary stretch receptor input** (via **vagal
afferents**) to the **respiratory rhythm generator** (the
**pre-Bötzinger complex** in the **ventral respiratory group**).
It is the **dorsal** counterpart to the **ventral respiratory
group (VRG)** — the DRG is **dorsal** (in the **NTS region**);
the VRG is **ventral** (in the **ventrolateral medulla**).

**The DRG IS a respiratory structure — unlike the cuneate
nucleus.** The **"respiratory_center"** label is **functionally
accurate** for the DRG — the DRG is **truly** a respiratory
pattern generator, **NOT** a tree-wiring artifact like the
cuneate nucleus (which is **somatosensory**).

**The DRG is OFTEN CONSIDERED PART OF THE NTS in the
literature.** It is in the **ventrolateral NTS region**. **In
this tree**, the **DRG is wired as a separate child** of
``respiratory_center``, **NOT** under the **NTS container**
(``.../solitary_nucleus/``). **The tree separates the NTS and
the DRG into two modules** as a **deliberate wiring choice** —
the **DRG** is a **functional respiratory group within the NTS
region**; the **NTS** is the **broader visceral afferent relay**
of which the **DRG** is a **functional subregion**.

**The DRG is TRULY BILATERAL — the left / right split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **left** and **right**
DRG are **anatomically separate structures** — the **left DRG**
is in the **left NTS region**; the **right DRG** is in the
**right NTS region**. The **left / right split** here reflects
**anatomy** — **NOT** a **tree-wiring convention**.

**The DRG is functionally coupled to the VRG (pre-Bötzinger
complex), the NTS, the vagal afferent system, the parafacial
zone, and the higher respiratory centers.** It is **part of**
the **ponto-medullary respiratory network** — a **distributed
system** for **breathing**.

Bilateral Structure (Anatomical Pairing)
---------------------------------------
The dorsal respiratory group is a **bilateral container** in this
tree with **two structural children**:

*   ``left`` — the **left** DRG (a **leaf** module).
*   ``right`` — the **right** DRG (a **leaf** module).

**The two children are ANATOMICALLY SEPARATE structures** —
**NOT** a wiring convention for a midline organ (unlike the
area postrema / CTZ). The **left DRG** is in the **left NTS
region**; the **right DRG** is in the **right NTS region**.

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **DRG** as **single structures**. Consumers
that need **side-specific** resolution descend into ``left`` or
``right``; consumers that need the **whole bilateral pair** use
``dorsal_respiratory_group`` (the container) as a whole.

**The container itself is unpaired.** There is **no**
``dorsal_respiratory_group/left/.../`` structural hierarchy
beyond the single leaf level — the ``left`` and ``right``
modules are the **terminal modules** for this structure.

The Dorsal Respiratory Group / Ventral Respiratory Group Boundary
-----------------------------------------------------------------
This is the **most consequential** respiratory-generator
boundary:

*   **Dorsal respiratory group** (this module) — the **dorsal
    respiratory** pattern generator in the **NTS region**.

*   **Ventral respiratory group** (VRG)
    (``.../ventral_respiratory_group/``) — the **ventral
    respiratory** rhythm and pattern generator group (Bötzinger
    complex, pre-Bötzinger complex, nucleus para-ambiguus,
    nucleus retroambiguus, nucleus retrofacialis, retrotrapezoid
    nucleus).

**They are DIFFERENT RESPIRATORY STRUCTURES** in **DIFFERENT
CONTAINERS** — the **DRG** is **dorsal** (in the **NTS
region**); the **VRG** is **ventrolateral**. They are
**functionally coupled** — the DRG **relays** input to the
VRG's **pre-Bötzinger complex** — but they are **anatomically
distinct**. Consumers must **not** conflate the two.

The Dorsal Respiratory Group / Solitary Nucleus Boundary
---------------------------------------------------------
This is the **functional respiratory group / broader visceral
relay** boundary:

*   **Dorsal respiratory group** (this module) — the **respiratory
    group** within the **NTS region**.

*   **Solitary nucleus (NTS)** (``.../solitary_nucleus/``) — the
    **broader visceral afferent relay** — **wired separately**
    under ``medulla_oblongata``.

**The DRG is often considered part of the NTS in the
literature** — but **in this tree**, the two are **wired as
separate modules**. The **DRG** is a **functional respiratory
group within the NTS region**; the **NTS** is the **broader
visceral afferent relay**. Consumers must **not** expect to find
the DRG under ``solitary_nucleus`` — resolve it via
``respiratory_center.dorsal_respiratory_group``.

The Dorsal Respiratory Group / Area Postrema and Chemoreceptor Trigger Zone Boundary
------------------------------------------------------------------------------------
This is the **respiratory / circumventricular** boundary:

*   **Dorsal respiratory group** (this module) — the **respiratory
    pattern generator**.

*   **Area postrema** and **chemoreceptor trigger zone**
    (``.../area_postrema/`` and
    ``.../chemoreceptor_trigger_zone/``) — the
    **circumventricular chemoreceptive** structures for the
    **vomiting reflex**.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Dorsal Respiratory Group / Cuneate and Gracile Nuclei Boundary
------------------------------------------------------------------
This is the **respiratory / somatosensory** boundary:

*   **Dorsal respiratory group** (this module) — the **respiratory
    pattern generator**.

*   **Cuneate nucleus** and **gracile nucleus**
    (``.../cuneate_nucleus/`` and ``.../gracile_nucleus/``) — the
    **dorsal column somatosensory** relays.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
The **DRG IS respiratory**; the **cuneate and gracile nuclei are
somatosensory**. Consumers must **not** conflate them.

The Dorsal Respiratory Group / Gigantocellular Reticular Nucleus Boundary
-------------------------------------------------------------------------
This is the **dorsal respiratory / ventrolateral reticular**
boundary:

*   **Dorsal respiratory group** (this module) — the **dorsal
    respiratory** pattern generator in the **NTS region**.

*   **Gigantocellular reticular nucleus**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/``)
    — the **large ventrolateral reticular** nucleus with
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct** —
the **DRG** is a **dorsal respiratory pattern generator**; the
**Gi** is a **ventrolateral reticular nucleus** with **broader**
functions. Consumers must **not** conflate the two.

The Dorsal Respiratory Group / Parafacial Zone Boundary
-------------------------------------------------------
This is the **respiratory / sleep-promoting** boundary:

*   **Dorsal respiratory group** (this module) — the **respiratory
    pattern generator**.

*   **Parafacial zone** (``.../parafacial_zone/``) — the
    **GABAergic / glycinergic sleep-promoting** region.

**They are DIFFERENT STRUCTURES** in **DIFFERENT containers** —
the **DRG** is a **respiratory pattern generator**; the
**parafacial zone** is a **sleep-promoting region**. Consumers
must **not** conflate the two.

The Dorsal Respiratory Group / Ventral Respiratory Group Subnuclei Boundary
---------------------------------------------------------------------------
This is the **DRG / specific VRG subnucleus** boundary:

*   **Dorsal respiratory group** (this module) — the **dorsal
    respiratory** pattern generator.

*   **Retrotrapezoid nucleus**, **Bötzinger complex**,
    **pre-Bötzinger complex**, **nucleus para-ambiguus**,
    **nucleus retroambiguus**, **nucleus retrofacialis** —
    **specific VRG subnuclei** in the ``ventral_respiratory_group``
    container.

**They are DIFFERENT STRUCTURES** — the **DRG** is **dorsal**;
the **VRG subnuclei** are **ventrolateral**. Consumers must
**not** conflate the DRG with any VRG subnucleus.

The Dorsal Respiratory Group / Whole Respiratory Center and Whole Medulla Oblongata Boundary
--------------------------------------------------------------------------------------------
This is the **child / container** boundary:

*   **Dorsal respiratory group** (this module) — one **child** of
    ``respiratory_center``.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children**.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The DRG is a CHILD of respiratory_center, NOT the container
itself, and NOT the whole medulla.** Consumers must **not**
conflate the **child** with either **parent container**.

Function in the Human Brain
---------------------------
The dorsal respiratory group's function is **inspiratory pattern
generation** and **pulmonary stretch receptor relay** — **NOT
respiratory rhythm generation** (that is the VRG's pre-Bötzinger
complex) and **NOT motor control**:

*   **Inspiratory pattern generation:** The **DRG** is
    **involved in shaping the inspiratory pattern** — it
    **contributes** to the **inspiratory "on-switch"**,
    **"off-switch"**, and **ramp** — **relaying** input from
    **pulmonary stretch receptors** and **higher** respiratory
    centers to the **pre-Bötzinger complex** (VRG) — but the
    **primary rhythm generator** is the **pre-Bötzinger
    complex**, **NOT** the DRG.

*   **Pulmonary stretch receptor relay (Hering-Breuer reflex):**
    The **DRG** **receives** **pulmonary stretch receptor**
    **afferent** input via **vagal afferents** — it **relays**
    this input to the **respiratory rhythm generator** — this is
    the **neural substrate** of the **Hering-Breuer inflation
    reflex** (which **inhibits inspiration** when the **lungs**
    are **inflated**). The **Hering-Breuer reflex** is
    **prominent in infants** but **relatively weak in adults** —
    the DRG **contributes** to it in both.

*   **Vagal afferent respiratory input:** The **DRG** also
    **receives** **other vagal respiratory afferents** —
    including **chemoreceptor** input (from the **carotid
    body** via **CN IX** — though much of this is relayed via
    the **NTS** more broadly) and **irritant receptor** input.
    It **relays** these to the **VRG** and **higher** centers.

*   **Integration with higher respiratory centers:** The **DRG**
    **receives** **descending** input from the **cortex**, the
    **hypothalamus**, the **pons** (pneumotaxic center), and the
    **medullary** respiratory network — it **integrates** these
    with **vagal afferent** input and **relays** the result to
    the **pre-Bötzinger complex** and other **VRG** targets.

*   **NOT respiratory rhythm generation:** The **respiratory
    rhythm** is generated by the **pre-Bötzinger complex**
    (VRG) — **NOT** the DRG. The **DRG** **contributes** to
    **inspiratory pattern** but **does not generate** the
    **rhythm**.

*   **NOT motor control:** The **DRG** does **not** send motor
    axons to muscles — the **phrenic motor nucleus** (in the
    cervical spinal cord) and the **intercostal motor nuclei**
    (in the thoracic spinal cord) are the **motor neurons** for
    breathing. The DRG **modulates** them via its projections
    to the **VRG** and other **respiratory** centers.

**The unifying theme:** the dorsal respiratory group is a
**respiratory pattern generator** in the **NTS region** — it
**relays pulmonary stretch receptor input** and **shapes
inspiratory pattern** via projections to the **pre-Bötzinger
complex** (VRG) — **NOT** the respiratory rhythm generator,
**NOT** the NTS itself (in this tree), **NOT** the VRG, and
**NOT** the area postrema / CTZ.

Associated Disorders
--------------------
The dorsal respiratory group is the **substrate** for
**well-defined clinical syndromes** — its clinical relevance is
**direct** and **indirect**, via **respiratory pattern** and
**pulmonary stretch reflex** dysfunction:

*   **Central hypoventilation (via DRG dysfunction — indirect and
    partial):** **Damage** to the **DRG** can **contribute** to
    **central hypoventilation** — **impaired** inspiratory
    pattern generation, **abnormal** Hering-Breuer reflex —
    but the **primary** respiratory rhythm generators are the
    **pre-Bötzinger complex** (VRG) and other **brainstem**
    structures. **Isolated DRG lesions** rarely cause
    **full-blown central hypoventilation** — the **VRG** and
    **higher centers** can partially compensate.

*   **Impaired Hering-Breuer reflex (via DRG dysfunction):**
    **Reduced** or **absent** **Hering-Breuer inflation reflex**
    — from **DRG** dysfunction — **contributing** to **altered**
    **breathing pattern** (e.g., **increased** tidal volume,
    **reduced** respiratory rate). This is a **subtle** finding
    — not a named syndrome — and is usually **part of a broader
    brainstem lesion**.

*   **Sleep-disordered breathing (via DRG involvement —
    hypothesized):** **DRG** dysfunction may **contribute** to
    **sleep-disordered breathing** (central sleep apnea,
    hypopneas) — but the **primary** central control of
    breathing during sleep is the **pre-Bötzinger complex**
    (VRG) and **higher** centers. The **DRG** is a
    **contributing substrate**, not the **primary** substrate.

*   **Brainstem stroke (via DRG involvement):** **Medullary
    stroke** (lateral medullary syndrome, medial medullary
    syndrome, or **dorsal medullary** lesions) can **involve**
    the **DRG** — contributing to **respiratory pattern**
    abnormalities and **sleep-disordered breathing**.

*   **Rett syndrome and other central respiratory disorders (via
    broader brainstem dysfunction):** **Rett syndrome** and
    other **central respiratory disorders** involve **broader**
    brainstem dysfunction — including the **DRG** and the
    **NTS** — contributing to **breathing
    dysrhythmias** (**hyperventilation**, **apnea**,
    **breath-holding**). The **DRG** is a **contributing
    substrate** in these disorders.

*   **No Named "Dorsal Respiratory Group Syndrome":** The DRG is
    a **functional respiratory group** — its clinical syndromes
    are **named for the broader brainstem lesion** (brainstem
    stroke, central hypoventilation syndrome) or the
    **functional abnormality** (impaired Hering-Breuer reflex,
    sleep-disordered breathing) — **NOT** for the DRG itself.

**What is NOT here:** The DRG is **not** the substrate for
**respiratory rhythm generation** (pre-Bötzinger complex, VRG),
**emesis** (area postrema / CTZ), **somatosensory loss**
(cuneate / gracile nuclei), **autonomic dysfunction** (RVLM,
CVLM, NTS), **tongue weakness** (hypoglossal nucleus), or
**parasympathetic dysfunction** (dorsal motor nucleus of the
vagus). Its clinical relevance is the **inspiratory pattern**
and **pulmonary stretch reflex** functions listed above.

Lateralization Notes
--------------------
The dorsal respiratory group is a **bilateral container** in this
tree with ``left`` and ``right`` structural children. There is
**no** ``dorsal_respiratory_group/left/.../`` structural
hierarchy beyond the single leaf level.

*   **Bilateral structural children (ANATOMICAL pairing):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left** or **right** DRG as a **single structure**.
    The **left** and **right** DRG are **anatomically separate
    structures** (unlike the **area postrema**, which is a
    **midline** organ wired as left/right by convention). The
    **left** DRG is in the **left NTS region**; the **right**
    DRG is in the **right NTS region**.

*   **Bilateral symmetry:** The **left** and **right** DRG are
    **structurally symmetric mirror pairs** — same
    cytoarchitecture, same vagal afferent input, same
    projections to the **VRG** and **higher** centers.

*   **Partly crossed projections:** Some **DRG** projections are
    **ipsilateral** (to the **ipsilateral VRG** and other
    **ipsilateral** brainstem structures) and some are
    **crossed** (via **commissural** pathways). The **DRG**
    functions **bilaterally** in **respiratory pattern
    generation** — a **unilateral** lesion can cause
    **partial** respiratory pattern changes but is usually
    **partially compensated** by the **contralateral** DRG.

*   **NO lateralization warning:** The DRG has **no known
    functional lateralization** in humans — the **left** and
    **right** DRG are **functionally symmetric**. Consumers must
    **not** import a **lateralization warning** into the DRG —
    the **left** and **right** sides are **functionally
    symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The DRG is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into the DRG.

*   **NO Fear-Output Warning:** The DRG is **not** a fear-output
    structure — it is a **dorsal respiratory pattern generator**.
    Consumers must **not** conflate it with the **central
    nucleus** or with the **amygdala**.

**A consumer that assumes "left DRG = right DRG" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **group level**. The DRG is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The DRG is a **bilateral
    container** — it does **not** import from ``left/`` or
    ``right/`` at the container level. The ``left`` and
    ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../ventral_respiratory_group/``,
    ``.../solitary_nucleus/``,
    ``.../area_postrema/``,
    ``.../chemoreceptor_trigger_zone/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../parafacial_zone/``, ``.../cranial_nerve_nuclei/``,
    or any other container. The DRG's relationships to the VRG,
    NTS, area postrema, CTZ, cuneate nucleus, gracile nucleus,
    gigantocellular reticular nucleus, parafacial zone, and
    cranial nerve nuclei are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children (ANATOMICAL
    pairing).** The structural children are ``left`` and
    ``right``, each a **leaf**. **Anatomically**, the left and
    right DRG are **truly separate bilateral structures** — the
    **left / right split** is **ANATOMICAL**, **NOT** a
    **tree-wiring convention**.
*   **RESPIRATORY, NOT a tree-wiring artifact.** Unlike the
    cuneate nucleus, the DRG **IS** actually a respiratory
    structure — the **"respiratory_center"** label is
    **functionally accurate** for this child.
*   **NTS-overlap caveat.** The DRG is **often considered part
    of the NTS** in the literature — but in **this tree**, the
    DRG is **wired as a separate child** of
    ``respiratory_center``, **NOT** under the NTS container.
    Consumers must **not** expect to find the DRG under
    ``solitary_nucleus``.
*   **NOT the VRG.** The **ventral respiratory group** is a
    **separate container** under ``medulla_oblongata`` — the
    **dorsal vs. ventral** distinction is the **most
    consequential** DRG boundary.
*   **NOT the area postrema or CTZ.** Those are
    **circumventricular chemoreceptive** structures — **NOT**
    respiratory pattern generators.
*   **NOT the cuneate or gracile nucleus.** Those are
    **somatosensory relays** — **NOT** respiratory structures.
*   **NOT the gigantocellular reticular nucleus.** That is a
    **ventrolateral reticular** nucleus with **broader**
    respiratory, autonomic, and pain functions — **NOT** the
    dorsal respiratory pattern generator.
*   **NOT the parafacial zone.** That is a **sleep-promoting**
    region — **NOT** a respiratory pattern generator.
*   **NOT the retrotrapezoid nucleus, Bötzinger complex,
    pre-Bötzinger complex, or any other VRG subnucleus.**
    Those are **ventrolateral VRG** structures — **NOT** the
    dorsal respiratory group.
*   **NOT the whole respiratory_center or whole medulla
    oblongata.** The DRG is a **child** of ``respiratory_center``,
    not the container itself.
*   **No ``AREA_PATHS`` hop.** The DRG is a **local container** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The DRG has no nested
    dual-framing module. It is a **bilateral container** with
    **two leaf children** (anatomical pairing).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **dorsal respiratory
    pattern generator** framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center import dorsal_respiratory_group

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.dorsal_respiratory_group"
    )

**Do not** assume the DRG is the **ventral respiratory group
(VRG)**. The VRG is a **separate container** under
``medulla_oblongata`` — the **dorsal vs. ventral** distinction is
the **most consequential** DRG boundary.

**Do not** expect to find the DRG under ``solitary_nucleus``.
The **NTS** is a **separate container** — the DRG is a
**functional respiratory group within the NTS region** but is
**wired separately** under ``respiratory_center`` in this tree.

**Do not** assume the DRG is the **area postrema** or the
**chemoreceptor trigger zone**. Those are **circumventricular
chemoreceptive** structures — **NOT** respiratory pattern
generators.

**Do not** assume the DRG is the **cuneate** or **gracile**
nucleus. Those are **somatosensory relays** — **NOT**
respiratory structures.

**Do not** assume the DRG is the **gigantocellular reticular
nucleus**, the **parafacial zone**, the **retrotrapezoid
nucleus**, the **Bötzinger complex**, the **pre-Bötzinger
complex**, or any other VRG subnucleus. Each is a **different
structure**.

**Do not** assume the DRG is the **whole respiratory_center** or
the **whole medulla oblongata**. It is a **child** of
``respiratory_center``.

**Do not** infer **midline wiring convention** from the DRG
structure. The **left / right split** is **ANATOMICAL** — the
**left** and **right** DRG are **truly separate bilateral
structures** (unlike the area postrema / CTZ, which are midline
organs wired as left/right by convention).

Iterating the DRG's structural children (recommended consumer
pattern)::

    DORSAL_RESPIRATORY_GROUP_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # dorsal respiratory group. Anatomically, the left and right
    # DRG are TRULY SEPARATE bilateral structures — the
    # left/right split is ANATOMICAL, NOT a wiring convention.

Reaching the left and right DRG leaves (recommended consumer
pattern)::

    # The left and right DRG leaves are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.right
    #
    # Each is a leaf module representing the DRG of that side.
    # Anatomically, they are TRULY SEPARATE bilateral structures.

Reaching the ventral respiratory group (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The ventral respiratory group is a SEPARATE container under
    # medulla_oblongata — NOT wired under respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #
    # The DRG (dorsal respiratory group) and the VRG (ventral
    # respiratory group) are DIFFERENT RESPIRATORY STRUCTURES in
    # DIFFERENT CONTAINERS — the DRG is dorsal (in the NTS
    # region); the VRG is ventrolateral (Bötzinger complex,
    # pre-Bötzinger complex, nucleus para-ambiguus, nucleus
    # retroambiguus, nucleus retrofacialis, retrotrapezoid
    # nucleus). The DRG RELAYS input to the VRG — but they are
    # anatomically distinct.

Reaching the solitary nucleus (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The solitary nucleus (NTS) is a SEPARATE container under
    # medulla_oblongata — the DRG is often considered part of the
    # NTS in the literature, but is wired as a separate child of
    # respiratory_center in this tree:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # The DRG is a functional respiratory group WITHIN the NTS
    # region — the tree separates the two into two modules as a
    # deliberate wiring choice.

Reaching the area postrema and CTZ (recommended consumer
pattern — NOTE the DIFFERENT children of respiratory_center)::

    # The area postrema and the chemoreceptor trigger zone are
    # CIRCUMVENTRICULAR structures — children of
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone
    #
    # They are NOT respiratory pattern generators — they are
    # chemoreceptive / emetic structures.

Reaching the cuneate and gracile nuclei (recommended consumer
pattern — NOTE the DIFFERENT children of respiratory_center)::

    # The cuneate and gracile nuclei are SOMATOSENSORY relays —
    # children of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus
    #
    # They are NOT respiratory structures — they are dorsal column
    # somatosensory relays (wired under respiratory_center as a
    # tree-wiring artifact).

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"respiratory_center.dorsal_respiratory_group.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: the left and right DRG are TRULY SEPARATE
        # bilateral structures (ANATOMICAL, not a wiring
        # convention).

References
----------
*   **Canonical brainstem respiratory anatomy:** Feldman, J.L.,
    Del Negro, C.A. (2006). "Looking for inspiration: new
    perspectives on respiratory rhythm." *Nature Reviews
    Neuroscience* 7:232–242. (Dorsal respiratory group; ventral
    respiratory group; pre-Bötzinger complex; respiratory rhythm
    and pattern generation.)
*   **Dorsal respiratory group — overview:** Bianchi, A.L., et
    al. (1995). "Central control of breathing in mammals:
    neuronal circuitry, membrane properties, and
    neurotransmitters." *Physiological Reviews* 75:1–45.
    (Dorsal respiratory group; NTS region; inspiratory pattern
    generation; vagal afferent input.)
*   **Dorsal respiratory group — pulmonary stretch receptor
    relay:** Kubin, L., Davies, R.O. (1988). "Central
    coordination of respiratory and sympathetic activities."
    *Annual Review of Physiology* 50:63–74. (Dorsal respiratory
    group; pulmonary stretch receptors; Hering-Breuer reflex.)
*   **Dorsal respiratory group — NTS region:** Loewy, A.D.,
    Spyer, K.M. (1990). *Central Regulation of Autonomic
    Functions.* (NTS; dorsal respiratory group; respiratory and
    autonomic integration.)
*   **Dorsal respiratory group — Hering-Breuer reflex:**
    Widdicombe, J.G. (2001). "Airway receptors." *Respiration
    Physiology* 125:3–11. (Hering-Breuer reflex; pulmonary
    stretch receptors; dorsal respiratory group; vagal
    afferents.)
*   **Central hypoventilation:** Weese-Mayer, D.E., et al.
    (2010). "An official ATS clinical policy statement:
    congenital central hypoventilation syndrome." *American
    Journal of Respiratory and Critical Care Medicine*
    181:626–644. (Congenital central hypoventilation syndrome;
    brainstem respiratory network dysfunction — DRG contributes
    but the primary rhythm generator is the pre-Bötzinger
    complex.)
*   **Sleep-disordered breathing:** Dempsey, J.A., et al. (2010).
    "Pathophysiology of sleep apnea." *Physiological Reviews*
    90:47–112. (Sleep-disordered breathing; brainstem
    respiratory network; DRG involvement.)
*   **Rett syndrome — respiratory dysrhythmia:** Katz, D.M., et
    al. (2009). "Breathing disorders in Rett syndrome."
    *Respiratory Physiology & Neurobiology* 168:139–145. (Rett
    syndrome; brainstem respiratory dysfunction; DRG
    involvement.)
*   **Ventral respiratory group (contrast — separate
    container):** Feldman, J.L., Del Negro, C.A. (2006).
    "Looking for inspiration: new perspectives on respiratory
    rhythm." *Nature Reviews Neuroscience* 7:232–242. (Ventral
    respiratory group; pre-Bötzinger complex — DIFFERENT from
    the DRG.)
*   **Solitary nucleus (contrast — separate container):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS — broader
    visceral afferent relay, of which the DRG is a functional
    subregion.)
*   **Pre-Bötzinger complex (contrast — VRG rhythm
    generator):** Smith, J.C., et al. (1991). "Pre-Bötzinger
    complex: a brainstem region that may generate respiratory
    rhythm in mammals." *Science* 254:726–729. (Pre-Bötzinger
    complex; primary respiratory rhythm generator — DIFFERENT
    from the DRG pattern generator.)
*   NeuroNames — Dorsal respiratory group; FMA — Dorsal
    respiratory group.
"""