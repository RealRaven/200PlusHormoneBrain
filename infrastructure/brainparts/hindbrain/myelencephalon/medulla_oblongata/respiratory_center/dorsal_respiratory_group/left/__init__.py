"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.left
=====================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── dorsal_respiratory_group
                    └── left   <-- THIS MODULE

**Primary synonym:** Left dorsal respiratory group; left DRG; left
dorsal respiratory group of the NTS; left NTS respiratory region;
left ventrolateral NTS respiratory column.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** — the **left-side** group of
**respiratory-related neurons** in the **ventrolateral region of
the left nucleus tractus solitarius (NTS)** in the **left dorsal
medulla oblongata**. It is **involved in inspiratory pattern
generation** and **relays pulmonary stretch receptor input**
(via **left vagal afferents**) to the **respiratory rhythm
generator**. It is a **respiratory structure** — **NOT** a
somatosensory relay, **NOT** a circumventricular organ, and
**NOT** a reticular nucleus. **Unlike the left cuneate nucleus**
(a somatosensory tree-wiring artifact under ``respiratory_center``),
**the left DRG IS actually respiratory** — the
**"respiratory_center"** label is **functionally accurate** for
this child.
**Part of:** The **dorsal_respiratory_group** bilateral container
(``.../respiratory_center/dorsal_respiratory_group/``) — which is
part of the **respiratory_center** — which is part of the
**medulla oblongata** — the **caudal brainstem** subdivision of
the **myelencephalon**.
**Structural parent:** ``.../dorsal_respiratory_group/`` →
**direct child** of the dorsal_respiratory_group container. The
**left** leaf is one of the **two** structural children of the
container (the other is ``right``).
**Structural children:** **None.** This is a **leaf** module. The
left DRG is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the right dorsal respiratory group — the
contralateral leaf):** **Boundary case — the left dorsal
respiratory group is NOT the right dorsal respiratory group.**
The **right dorsal respiratory group**
(``.../dorsal_respiratory_group/right/``) is the **contralateral
leaf** — the DRG of the **right** medulla, in the **right NTS
region**. **They are DIFFERENT LEAVES** — the ``left`` and
``right`` modules are the two sides of the **bilateral
container**. **Unlike the area postrema / CTZ** — which are
**midline** organs wired as left/right by convention — **the
left and right DRG are TRULY SEPARATE BILATERAL STRUCTURES**
(anatomical, not a wiring convention). The **left DRG** is in
the **left NTS region**; the **right DRG** is in the **right
NTS region**. Consumers must **not** conflate the two.
**Boundary status (NOT a tree-wiring artifact — the left DRG IS
actually respiratory):** **Boundary case — the left dorsal
respiratory group IS a respiratory structure, NOT a tree-wiring
artifact.** Unlike the **left cuneate nucleus** (a somatosensory
relay wired under ``respiratory_center`` as a tree-wiring
artifact) and unlike the **left area postrema** / **left
chemoreceptor trigger zone** (circumventricular chemoreceptive
structures), the **left DRG** (here) **IS** actually a
**respiratory pattern generator** — it **participates in
inspiratory pattern generation** and **relays pulmonary stretch
receptor input** to the **respiratory rhythm generator**. The
**"respiratory_center"** label is **functionally accurate** for
this child.
**Boundary status (NOT the left ventral respiratory group — a
DIFFERENT respiratory generator in a DIFFERENT container):**
**Boundary case — the left dorsal respiratory group is NOT the
left ventral respiratory group (VRG).** The **left VRG**
(``.../ventral_respiratory_group/left/``) is the **left ventral
respiratory** rhythm and pattern generator group — containing
the **left Bötzinger complex**, **left pre-Bötzinger complex**,
**left nucleus para-ambiguus**, **left nucleus retroambiguus**,
**left nucleus retrofacialis**, and **left retrotrapezoid
nucleus** — in the **left ventrolateral medulla**. **They are
DIFFERENT RESPIRATORY STRUCTURES** in **DIFFERENT CONTAINERS** —
the **left DRG** is **dorsal** (in the **left NTS region**); the
**left VRG** is **ventrolateral**. They are **functionally
coupled** — the left DRG **relays** input to the **left
pre-Bötzinger complex** (the **primary respiratory rhythm
generator**) — but they are **anatomically distinct**. Consumers
must **not** conflate the two.
**Boundary status (NOT the left solitary nucleus (NTS) — the
left NTS is the parent region in the literature, wired as a
SEPARATE container in this tree):** **Boundary case — the left
dorsal respiratory group is NOT the left solitary nucleus
(NTS).** The **left solitary nucleus**
(``.../solitary_nucleus/left/``) is the **left visceral afferent
relay** — it is a **separate container** under
``medulla_oblongata``. **In the literature**, the **left DRG** is
**often considered part of** the **left NTS** — it is in the
**ventrolateral left NTS region**. **In this tree**, the **left
DRG** is **wired as a separate leaf** under
``respiratory_center.dorsal_respiratory_group``, **NOT** under
the **left NTS container**. Consumers must **not** expect to
find the left DRG under ``solitary_nucleus.left`` — resolve it
via ``respiratory_center.dorsal_respiratory_group.left``. **The
tree separates** the **left NTS** and the **left DRG** into
**two modules** as a **deliberate wiring choice** — the **left
DRG** is a **functional respiratory group within the left NTS
region**; the **left NTS** is the **broader visceral afferent
relay** of which the **left DRG** is a **functional subregion**.
**Boundary status (NOT the left area postrema or left
chemoreceptor trigger zone — DIFFERENT children of
respiratory_center):** **Boundary case — the left dorsal
respiratory group is NOT the left area postrema or left
chemoreceptor trigger zone.** The **left area postrema** and
**left chemoreceptor trigger zone**
(``.../area_postrema/left/`` and
``.../chemoreceptor_trigger_zone/left/``) are **circumventricular
chemoreceptive** structures for the **vomiting reflex** — **NOT**
respiratory pattern generators. **They are DIFFERENT
STRUCTURES** — children of ``respiratory_center`` — but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the left cuneate or left gracile nucleus
— DIFFERENT children of respiratory_center):** **Boundary case
— the left dorsal respiratory group is NOT the left cuneate or
left gracile nucleus.** The **left cuneate** and **left gracile
nuclei**
(``.../respiratory_center/cuneate_nucleus/left/`` and
``.../respiratory_center/gracile_nucleus/left/``) are the **left
dorsal column somatosensory relays** (fine touch, vibration,
proprioception). **They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
The **left DRG IS respiratory**; the **left cuneate and left
gracile nuclei are somatosensory**. Consumers must **not**
conflate them.
**Boundary status (NOT the left gigantocellular reticular
nucleus — a DIFFERENT child of respiratory_center):** **Boundary
case — the left dorsal respiratory group is NOT the left
gigantocellular reticular nucleus (Gi).** The **left
gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/left/``)
is a **left ventrolateral reticular** nucleus — it is involved in
**respiration**, **autonomic function**, and **descending pain
modulation**. **They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct** —
the **left DRG** is a **dorsal respiratory pattern generator** in
the **left NTS region**; the **left Gi** is a **ventrolateral
reticular nucleus** with **broader** respiratory, autonomic, and
pain functions. Consumers must **not** conflate the two.
**Boundary status (NOT the left parafacial zone — a
sleep-promoting region in a DIFFERENT container):** **Boundary
case — the left dorsal respiratory group is NOT the left
parafacial zone.** The **left parafacial zone**
(``.../parafacial_zone/left/``) is a **GABAergic / glycinergic
sleep-promoting** region — **NOT** a respiratory pattern
generator and **NOT** wired under ``respiratory_center``.
Consumers must **not** conflate the two.
**Boundary status (NOT the left retrotrapezoid nucleus, left
Bötzinger complex, left pre-Bötzinger complex, or other left VRG
subnuclei — DIFFERENT structures in a DIFFERENT container):**
**Boundary case — the left dorsal respiratory group is NOT the
left retrotrapezoid nucleus, the left Bötzinger complex, the
left pre-Bötzinger complex, or any other left VRG subnucleus.**
Those are **left ventral respiratory** structures — wired under
the **separate** ``ventral_respiratory_group`` container. **They
are DIFFERENT STRUCTURES** from the left dorsal respiratory
group — different **dorsoventral position**, different
**functions** (left VRG = rhythm / pattern; left DRG =
pulmonary stretch relay / inspiratory pattern). Consumers must
**not** conflate the left DRG with any left VRG subnucleus.
**Boundary status (NOT the left NTS or the left vagal afferent
system — the left DRG RECEIVES left vagal input but is NOT the
vagus itself):** **Boundary case — the left dorsal respiratory
group is NOT the left solitary nucleus (NTS) or the left vagal
afferent system.** The **left DRG** **receives** **left
pulmonary stretch receptor** input via **left vagal afferents** —
those **afferents** **synapse** in the **left NTS region**
(which is anatomically the **left DRG's home region**) — but the
**left DRG neurons** are **left second-order respiratory
neurons**, **NOT** left primary afferent neurons. Consumers must
**not** conflate the left DRG with the left vagal afferent
system itself.
**Boundary status (NOT the whole dorsal_respiratory_group
container — an ASPECT of it):** **Boundary case — the left
dorsal respiratory group is NOT the whole
dorsal_respiratory_group container.** The **whole
dorsal_respiratory_group**
(``.../dorsal_respiratory_group/``) is the **bilateral
container** that **contains** the left DRG (here) **plus** the
right DRG. Consumers must **not** conflate the **leaf** with the
**container**.
**Boundary status (NOT the whole respiratory_center or whole
medulla oblongata — a leaf in a chain of containers):**
**Boundary case — the left dorsal respiratory group is NOT the
whole respiratory_center or the whole medulla oblongata.** It
is a **leaf** at the **bottom** of a **chain** of containers:
``medulla_oblongata`` → ``respiratory_center`` →
``dorsal_respiratory_group`` → ``left``. Consumers must **not**
conflate the **leaf** with **any of the parent containers**.

Overview
--------
The **left dorsal respiratory group (DRG)** is the **left-side**
group of **respiratory-related neurons** in the **ventrolateral
region of the left nucleus tractus solitarius (NTS)** in the
**left dorsal medulla oblongata**. It is **involved in
inspiratory pattern generation** and **relays left pulmonary
stretch receptor input** (via **left vagal afferents**) to the
**respiratory rhythm generator** (the **left pre-Bötzinger
complex** in the **left ventral respiratory group**).

**This is a LEAF module.** The **left DRG** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution of the left
side use this module; consumers that need **right-side**
resolution use ``.../dorsal_respiratory_group/right/``;
consumers that need the **whole dorsal_respiratory_group
container** use ``.../dorsal_respiratory_group/``.

**The left DRG IS actually respiratory — NOT a tree-wiring
artifact.** Unlike the **left cuneate nucleus** (a somatosensory
relay wired under ``respiratory_center`` as a tree-wiring
artifact) and unlike the **left area postrema** / **left
chemoreceptor trigger zone** (circumventricular chemoreceptive
structures), the **left DRG** **IS** actually a **respiratory
pattern generator**. The **"respiratory_center"** label is
**functionally accurate** for this child.

**The left DRG is OFTEN CONSIDERED PART OF THE left NTS in the
literature.** It is in the **ventrolateral left NTS region**.
**In this tree**, the **left DRG is wired as a separate leaf**
under ``respiratory_center.dorsal_respiratory_group``, **NOT**
under the **left NTS container** (``.../solitary_nucleus/left/``).
**The tree separates the left NTS and the left DRG into two
modules** as a **deliberate wiring choice** — the **left DRG**
is a **functional respiratory group within the left NTS
region**; the **left NTS** is the **broader visceral afferent
relay** of which the **left DRG** is a **functional subregion**.

**The left DRG is TRULY BILATERAL — the left / right split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **left** and **right**
DRG are **anatomically separate structures** — the **left DRG**
is in the **left NTS region**; the **right DRG** is in the
**right NTS region**. The **left / right split** here reflects
**anatomy** — **NOT** a **tree-wiring convention**.

**The left DRG relays IPSILATERAL input to the IPSILATERAL VRG.**
The **left DRG** receives **left pulmonary stretch receptor**
input via **left vagal afferents** — and it **projects**
primarily to the **left pre-Bötzinger complex** (in the **left
VRG**) — contributing to the **left-side inspiratory pattern**.
There is also some **crossed** projection — the **left DRG**
can influence the **right VRG** via **commissural** pathways —
but the **predominant** projection is **ipsilateral**.

The Left Dorsal Respiratory Group / Right Dorsal Respiratory Group Boundary
--------------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left DRG** (this module) — the DRG of the **left** medulla,
    in the **left NTS region**.

*   **Right DRG** (``.../dorsal_respiratory_group/right/``) — the
    DRG of the **right** medulla, in the **right NTS region**.

**They are TRULY SEPARATE BILATERAL STRUCTURES** — the **left**
and **right** DRG are **anatomically distinct** (not a wiring
convention for a midline organ). They are **structurally
symmetric mirror pairs** — same cytoarchitecture, same
ipsilateral vagal input, same **no warning**. Consumers must
**not** conflate the left with the right — resolve the right
side via ``dorsal_respiratory_group.right``.

The Left Dorsal Respiratory Group / Left Ventral Respiratory Group Boundary
--------------------------------------------------------------------------
This is the **most consequential** respiratory-generator
boundary:

*   **Left DRG** (this module) — the **left dorsal respiratory**
    pattern generator in the **left NTS region**.

*   **Left VRG** (``.../ventral_respiratory_group/left/``) — the
    **left ventral respiratory** rhythm and pattern generator
    group (left Bötzinger complex, left pre-Bötzinger complex,
    left nucleus para-ambiguus, left nucleus retroambiguus,
    left nucleus retrofacialis, left retrotrapezoid nucleus).

**They are DIFFERENT RESPIRATORY STRUCTURES** in **DIFFERENT
CONTAINERS** — the **left DRG** is **dorsal** (in the **left
NTS region**); the **left VRG** is **ventrolateral**. They are
**functionally coupled** — the left DRG **relays** input to the
**left pre-Bötzinger complex** — but they are **anatomically
distinct**. Consumers must **not** conflate the two.

The Left Dorsal Respiratory Group / Left Solitary Nucleus Boundary
------------------------------------------------------------------
This is the **functional respiratory group / broader visceral
relay** boundary:

*   **Left DRG** (this module) — the **left respiratory group**
    within the **left NTS region**.

*   **Left solitary nucleus (NTS)**
    (``.../solitary_nucleus/left/``) — the **left broader
    visceral afferent relay** — **wired separately** under
    ``medulla_oblongata``.

**The left DRG is often considered part of the left NTS in the
literature** — but **in this tree**, the two are **wired as
separate modules**. The **left DRG** is a **functional
respiratory group within the left NTS region**; the **left NTS**
is the **broader visceral afferent relay**. Consumers must **not**
expect to find the left DRG under ``solitary_nucleus.left`` —
resolve it via
``respiratory_center.dorsal_respiratory_group.left``.

The Left Dorsal Respiratory Group / Left Area Postrema and Left Chemoreceptor Trigger Zone Boundary
---------------------------------------------------------------------------------------------------
This is the **respiratory / circumventricular** boundary:

*   **Left DRG** (this module) — the **left respiratory pattern
    generator**.

*   **Left area postrema** and **left chemoreceptor trigger
    zone** (``.../area_postrema/left/`` and
    ``.../chemoreceptor_trigger_zone/left/``) — the
    **left circumventricular chemoreceptive** structures for the
    **vomiting reflex**.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Left Dorsal Respiratory Group / Left Cuneate and Left Gracile Nuclei Boundary
---------------------------------------------------------------------------------
This is the **respiratory / somatosensory** boundary:

*   **Left DRG** (this module) — the **left respiratory pattern
    generator**.

*   **Left cuneate nucleus** and **left gracile nucleus**
    (``.../cuneate_nucleus/left/`` and
    ``.../gracile_nucleus/left/``) — the **left dorsal column
    somatosensory** relays.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
The **left DRG IS respiratory**; the **left cuneate and left
gracile nuclei are somatosensory**. Consumers must **not**
conflate them.

The Left Dorsal Respiratory Group / Left Gigantocellular Reticular Nucleus Boundary
-----------------------------------------------------------------------------------
This is the **dorsal respiratory / ventrolateral reticular**
boundary:

*   **Left DRG** (this module) — the **left dorsal respiratory**
    pattern generator in the **left NTS region**.

*   **Left gigantocellular reticular nucleus**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/left/``)
    — the **left large ventrolateral reticular** nucleus with
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Left Dorsal Respiratory Group / Left Parafacial Zone Boundary
-----------------------------------------------------------------
This is the **respiratory / sleep-promoting** boundary:

*   **Left DRG** (this module) — the **left respiratory pattern
    generator**.

*   **Left parafacial zone** (``.../parafacial_zone/left/``) — the
    **left GABAergic / glycinergic sleep-promoting** region.

**They are DIFFERENT STRUCTURES** in **DIFFERENT containers**.
Consumers must **not** conflate the two.

The Left Dorsal Respiratory Group / Left VRG Subnuclei Boundary
---------------------------------------------------------------
This is the **left DRG / specific left VRG subnucleus** boundary:

*   **Left DRG** (this module) — the **left dorsal respiratory**
    pattern generator.

*   **Left retrotrapezoid nucleus**, **left Bötzinger complex**,
    **left pre-Bötzinger complex**, **left nucleus
    para-ambiguus**, **left nucleus retroambiguus**, **left
    nucleus retrofacialis** — **specific left VRG subnuclei** in
    the ``ventral_respiratory_group`` container.

**They are DIFFERENT STRUCTURES** — the **left DRG** is
**dorsal**; the **left VRG subnuclei** are **ventrolateral**.
Consumers must **not** conflate the left DRG with any left VRG
subnucleus.

The Left Dorsal Respiratory Group / Whole Dorsal Respiratory Group, Whole Respiratory Center, and Whole Medulla Oblongata Boundary
----------------------------------------------------------------------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Left DRG** (this module) — one **leaf** of the
    ``dorsal_respiratory_group`` container.

*   **Dorsal respiratory group** (``.../dorsal_respiratory_group/``)
    — the **bilateral container** of the left + right DRG.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children** (of which
    ``dorsal_respiratory_group`` is one).

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The left DRG is a LEAF in a CHAIN of containers.** Consumers
must **not** conflate the **leaf** with any of the **parent
containers**.

Function in the Human Brain
---------------------------
The left DRG's function is **inspiratory pattern generation** and
**left pulmonary stretch receptor relay** — **NOT respiratory
rhythm generation** (that is the left VRG's pre-Bötzinger
complex) and **NOT motor control**:

*   **Left inspiratory pattern generation:** The **left DRG** is
    **involved in shaping the left inspiratory pattern** — it
    **contributes** to the **left inspiratory "on-switch"**,
    **"off-switch"**, and **ramp** — **relaying** input from
    **left pulmonary stretch receptors** and **higher**
    respiratory centers to the **left pre-Bötzinger complex**
    (left VRG) — but the **primary rhythm generator** is the
    **left pre-Bötzinger complex**, **NOT** the left DRG.

*   **Left pulmonary stretch receptor relay (Hering-Breuer
    reflex):** The **left DRG** **receives** **left pulmonary
    stretch receptor** **afferent** input via **left vagal
    afferents** — it **relays** this input to the **left
    respiratory rhythm generator** — this is the **left-side
    neural substrate** of the **Hering-Breuer inflation
    reflex** (which **inhibits inspiration** when the **left
    lung** is **inflated**).

*   **Left vagal afferent respiratory input:** The **left DRG**
    also **receives** **other left vagal respiratory
    afferents** — including **chemoreceptor** input (from the
    **left carotid body** via **left CN IX** — though much of
    this is relayed via the **left NTS** more broadly) and
    **irritant receptor** input. It **relays** these to the
    **left VRG** and **higher** centers.

*   **Integration with higher respiratory centers:** The **left
    DRG** **receives** **descending** input from the **left and
    right cortex**, the **hypothalamus**, the **pons**
    (pneumotaxic center), and the **medullary** respiratory
    network — it **integrates** these with **left vagal
    afferent** input and **relays** the result to the **left
    pre-Bötzinger complex** and other **left VRG** targets.

*   **NOT respiratory rhythm generation:** The **respiratory
    rhythm** is generated by the **left pre-Bötzinger complex**
    (left VRG) — **NOT** the left DRG. The **left DRG**
    **contributes** to **left inspiratory pattern** but **does
    not generate** the **rhythm**.

*   **NOT motor control:** The **left DRG** does **not** send
    motor axons to muscles — the **left phrenic motor nucleus**
    (in the **left cervical spinal cord**) and the **left
    intercostal motor nuclei** (in the **left thoracic spinal
    cord**) are the **motor neurons** for breathing. The left
    DRG **modulates** them via its projections to the **left
    VRG** and other **respiratory** centers.

**The unifying theme:** the left DRG is a **left respiratory
pattern generator** in the **left NTS region** — it **relays
left pulmonary stretch receptor input** and **shapes left
inspiratory pattern** via projections to the **left
pre-Bötzinger complex** (left VRG) — **NOT** the left
respiratory rhythm generator, **NOT** the left NTS itself (in
this tree), **NOT** the left VRG, and **NOT** the left area
postrema / left CTZ.

Associated Disorders
--------------------
The left DRG is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct** and
**indirect**, via **left respiratory pattern** and **left
pulmonary stretch reflex** dysfunction:

*   **Central hypoventilation (via left DRG dysfunction —
    indirect and partial):** **Damage** to the **left DRG** can
    **contribute** to **central hypoventilation** — but the
    **primary** respiratory rhythm generators are the **left
    pre-Bötzinger complex** (left VRG) and other **brainstem**
    structures. **Isolated left DRG lesions** rarely cause
    **full-blown central hypoventilation** — the **right DRG**,
    the **VRG**, and **higher centers** can partially
    compensate.

*   **Impaired Hering-Breuer reflex (via left DRG
    dysfunction):** **Reduced** or **absent** **left-side
    Hering-Breuer inflation reflex** — from **left DRG**
    dysfunction — **contributing** to **altered** **breathing
    pattern**. This is a **subtle** finding — not a named
    syndrome — and is usually **part of a broader brainstem
    lesion**.

*   **Sleep-disordered breathing (via left DRG involvement —
    hypothesized):** **Left DRG** dysfunction may
    **contribute** to **sleep-disordered breathing** (central
    sleep apnea, hypopneas) — but the **primary** central
    control of breathing during sleep is the **pre-Bötzinger
    complex** (VRG) and **higher** centers.

*   **Brainstem stroke (via left DRG involvement):** **Left
    medullary stroke** (lateral medullary syndrome, medial
    medullary syndrome, or **left dorsal medullary** lesions)
    can **involve** the **left DRG** — contributing to
    **left-side respiratory pattern** abnormalities and
    **sleep-disordered breathing**.

*   **Rett syndrome and other central respiratory disorders
    (via broader brainstem dysfunction):** **Rett syndrome**
    and other **central respiratory disorders** involve
    **broader** brainstem dysfunction — including the **left
    DRG** and the **left NTS** — contributing to **breathing
    dysrhythmias**.

*   **No Named "Left Dorsal Respiratory Group Syndrome":** The
    left DRG is a **functional respiratory group** — its
    clinical syndromes are **named for the broader brainstem
    lesion** (brainstem stroke, central hypoventilation
    syndrome) or the **functional abnormality** (impaired
    Hering-Breuer reflex, sleep-disordered breathing) — **NOT**
    for the left DRG itself. There is **no named "left DRG
    syndrome"**.

**What is NOT here:** The left DRG is **not** the substrate for
**respiratory rhythm generation** (left pre-Bötzinger complex,
left VRG), **emesis** (left area postrema / left CTZ),
**somatosensory loss** (left cuneate / left gracile nuclei),
**autonomic dysfunction** (left RVLM, left CVLM, left NTS),
**tongue weakness** (left hypoglossal nucleus), or
**parasympathetic dysfunction** (left dorsal motor nucleus of
the vagus). Its clinical relevance is the **left inspiratory
pattern** and **left pulmonary stretch reflex** functions listed
above.

Lateralization Notes
--------------------
This is the **left** DRG module. The dorsal respiratory group is
a **bilateral container** whose two sides are **ANATOMICALLY
SEPARATE** — **not** a wiring convention for a midline organ
(unlike the area postrema / CTZ) — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right** DRG are
    **structurally symmetric** — they are **mirror pairs** with
    the **same** cytoarchitecture, **same** ipsilateral vagal
    input, and **same** functions. The **left** DRG is in the
    **left NTS region**; the **right** DRG is in the **right
    NTS region**.

*   **Predominantly Ipsilateral, Partly Crossed Projections:**
    The **left DRG** projects **predominantly ipsilaterally**
    (to the **left pre-Bötzinger complex** and the **left
    VRG**) — with some **crossed** projection to the **right
    VRG** via **commissural** pathways. This **functional
    ipsilaterality** is **part of the respiratory network's
    bilateral coordination** — the **left and right DRG**
    together coordinate **breathing** bilaterally.

*   **NO Lateralization Warning:** The DRG has **no known
    functional lateralization** in humans — the **left** and
    **right** DRG are **functionally symmetric** at the **group
    level**. Consumers must **not** import a **lateralization
    warning** into the left DRG — the **left** and **right**
    sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left DRG is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the left DRG.

*   **NO Fear-Output Warning:** The left DRG is **not** a
    fear-output structure — it is a **left dorsal respiratory
    pattern generator**. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left DRG = right DRG" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **group level**. The DRG is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left DRG is a **leaf** —
    it does **not** import from ``.../right/`` or any other
    right-side module. The **left / right split** is
    **ANATOMICAL** — not a **wiring convention**. The **left**
    and **right** DRG are **truly separate bilateral
    structures**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../ventral_respiratory_group/``,
    ``.../solitary_nucleus/``,
    ``.../area_postrema/``,
    ``.../chemoreceptor_trigger_zone/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../parafacial_zone/``, ``.../cranial_nerve_nuclei/``,
    or any other container. The left DRG's relationships to the
    left VRG, left NTS, left area postrema, left CTZ, left
    cuneate nucleus, left gracile nucleus, left gigantocellular
    reticular nucleus, left parafacial zone, and left cranial
    nerve nuclei are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left DRG is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../left/``.
*   **ANATOMICAL BILATERALITY, NOT a wiring convention.** The
    ``left`` and ``right`` DRG are **anatomically separate
    structures** — unlike the **area postrema** / **CTZ** (which
    are midline organs wired as left/right by convention).
*   **RESPIRATORY, NOT a tree-wiring artifact.** Unlike the left
    cuneate nucleus, the left DRG **IS** actually a respiratory
    structure — the **"respiratory_center"** label is
    **functionally accurate** for this child.
*   **NTS-overlap caveat.** The left DRG is **often considered
    part of the left NTS** in the literature — but in **this
    tree**, the left DRG is **wired as a separate leaf** under
    ``respiratory_center.dorsal_respiratory_group``, **NOT**
    under the left NTS container. Consumers must **not** expect
    to find the left DRG under ``solitary_nucleus.left``.
*   **NOT the right DRG.** The **right DRG** is a **separate
    leaf** under ``.../dorsal_respiratory_group/right/``.
    Consumers must **not** conflate the left with the right.
*   **NOT the left VRG.** The **left VRG** is a **separate
    container** — the **dorsal vs. ventral** distinction is the
    **most consequential** left DRG boundary.
*   **NOT the left area postrema or left CTZ.** Those are
    **circumventricular chemoreceptive** structures — **NOT**
    respiratory pattern generators.
*   **NOT the left cuneate or left gracile nucleus.** Those are
    **somatosensory relays** — **NOT** respiratory structures.
*   **NOT the left gigantocellular reticular nucleus.** That is a
    **left ventrolateral reticular** nucleus with **broader**
    respiratory, autonomic, and pain functions — **NOT** the
    dorsal respiratory pattern generator.
*   **NOT the left parafacial zone.** That is a
    **sleep-promoting** region — **NOT** a respiratory pattern
    generator.
*   **NOT the left retrotrapezoid nucleus, left Bötzinger
    complex, left pre-Bötzinger complex, or any other left VRG
    subnucleus.** Those are **left ventrolateral VRG**
    structures — **NOT** the left dorsal respiratory group.
*   **NOT the whole dorsal_respiratory_group, whole
    respiratory_center, or whole medulla oblongata.** The left
    DRG is a **leaf** in a **chain** of containers.
*   **No ``AREA_PATHS`` hop.** The left DRG is a **local leaf** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The left DRG has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the right DRG — strict mirror with
    NO warning.** The left and right modules are **structurally
    identical** — same leaf status, same **dorsal respiratory
    pattern generator** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.dorsal_respiratory_group.left"
    )

**Do not** assume the left DRG is the **right DRG**. The right
DRG is the **separate leaf** at
``.../dorsal_respiratory_group/right/``. They are **truly
separate bilateral structures** — the left DRG is in the **left
NTS region**; the right DRG is in the **right NTS region**.

**Do not** assume the left DRG is the **left ventral respiratory
group (VRG)**. The left VRG is a **separate container** under
``medulla_oblongata`` — the **dorsal vs. ventral** distinction
is the **most consequential** left DRG boundary.

**Do not** expect to find the left DRG under
``solitary_nucleus.left``. The **left NTS** is a **separate
container** — the left DRG is a **functional respiratory group
within the left NTS region** but is **wired separately** under
``respiratory_center`` in this tree.

**Do not** assume the left DRG is the **left area postrema** or
the **left chemoreceptor trigger zone**. Those are
**circumventricular chemoreceptive** structures — **NOT**
respiratory pattern generators.

**Do not** assume the left DRG is the **left cuneate** or
**left gracile** nucleus. Those are **somatosensory relays** —
**NOT** respiratory structures.

**Do not** assume the left DRG is the **left gigantocellular
reticular nucleus**, the **left parafacial zone**, the **left
retrotrapezoid nucleus**, the **left Bötzinger complex**, the
**left pre-Bötzinger complex**, or any other left VRG
subnucleus. Each is a **different structure**.

**Do not** assume the left DRG has **structural children**. It
is a **leaf** — it represents the left DRG as a **single
structure**.

**Do not** infer **midline wiring convention** from the left DRG
structure. The **left / right split** is **ANATOMICAL** — the
**left** and **right** DRG are **truly separate bilateral
structures** (unlike the area postrema / CTZ, which are midline
organs wired as left/right by convention).

Iterating the left DRG's (empty) children (recommended consumer
pattern)::

    LEFT_DORSAL_RESPIRATORY_GROUP_CHILDREN = ()
    # The left DRG is a leaf. It has no structural children.

Reaching the right DRG (recommended consumer pattern — the
contralateral leaf, a TRULY SEPARATE structure)::

    # The right DRG is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.right
    #
    # The left and right DRG are TRULY SEPARATE BILATERAL
    # STRUCTURES (anatomical, not a wiring convention).

Reaching the left ventral respiratory group (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The left ventral respiratory group is a SEPARATE container
    # under medulla_oblongata — NOT wired under
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left
    #
    # The left DRG (dorsal respiratory group) and the left VRG
    # (ventral respiratory group) are DIFFERENT RESPIRATORY
    # STRUCTURES in DIFFERENT CONTAINERS — the left DRG is dorsal
    # (in the left NTS region); the left VRG is ventrolateral
    # (left Bötzinger complex, left pre-Bötzinger complex, left
    # nucleus para-ambiguus, left nucleus retroambiguus, left
    # nucleus retrofacialis, left retrotrapezoid nucleus). The
    # left DRG RELAYS input to the left VRG — but they are
    # anatomically distinct.

Reaching the left solitary nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The left solitary nucleus (NTS) is a SEPARATE container
    # under medulla_oblongata — the left DRG is often considered
    # part of the left NTS in the literature, but is wired as a
    # separate leaf of respiratory_center in this tree:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
    #
    # The left DRG is a functional respiratory group WITHIN the
    # left NTS region — the tree separates the two into two
    # modules as a deliberate wiring choice.

Reaching the left area postrema and left CTZ (recommended
consumer pattern — NOTE the DIFFERENT leaves of
respiratory_center)::

    # The left area postrema and the left chemoreceptor trigger
    # zone are CIRCUMVENTRICULAR structures — leaves of
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.left
    #
    # They are NOT respiratory pattern generators — they are
    # chemoreceptive / emetic structures.

Reaching the left cuneate and left gracile nuclei
(recommended consumer pattern — NOTE the DIFFERENT leaves of
respiratory_center)::

    # The left cuneate and left gracile nuclei are SOMATOSENSORY
    # relays — leaves of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus.left
    #
    # They are NOT respiratory structures — they are dorsal
    # column somatosensory relays (wired under respiratory_center
    # as a tree-wiring artifact).

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