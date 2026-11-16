"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.right
======================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── dorsal_respiratory_group
                    └── right   <-- THIS MODULE

**Primary synonym:** Right dorsal respiratory group; right DRG;
right dorsal respiratory group of the NTS; right NTS respiratory
region; right ventrolateral NTS respiratory column.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** — the **right-side** group of
**respiratory-related neurons** in the **ventrolateral region of
the right nucleus tractus solitarius (NTS)** in the **right dorsal
medulla oblongata**. It is **involved in inspiratory pattern
generation** and **relays pulmonary stretch receptor input**
(via **right vagal afferents**) to the **respiratory rhythm
generator**. It is a **respiratory structure** — **NOT** a
somatosensory relay, **NOT** a circumventricular organ, and
**NOT** a reticular nucleus. **Unlike the right cuneate nucleus**
(a somatosensory tree-wiring artifact under ``respiratory_center``),
**the right DRG IS actually respiratory** — the
**"respiratory_center"** label is **functionally accurate** for
this child.
**Part of:** The **dorsal_respiratory_group** bilateral container
(``.../respiratory_center/dorsal_respiratory_group/``) — which is
part of the **respiratory_center** — which is part of the
**medulla oblongata** — the **caudal brainstem** subdivision of
the **myelencephalon**.
**Structural parent:** ``.../dorsal_respiratory_group/`` →
**direct child** of the dorsal_respiratory_group container. The
**right** leaf is one of the **two** structural children of the
container (the other is ``left``).
**Structural children:** **None.** This is a **leaf** module. The
right DRG is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the left dorsal respiratory group — the
contralateral leaf):** **Boundary case — the right dorsal
respiratory group is NOT the left dorsal respiratory group.**
The **left dorsal respiratory group**
(``.../dorsal_respiratory_group/left/``) is the **contralateral
leaf** — the DRG of the **left** medulla, in the **left NTS
region**. **They are DIFFERENT LEAVES** — the ``right`` and
``left`` modules are the two sides of the **bilateral
container**. **Unlike the area postrema / CTZ** — which are
**midline** organs wired as left/right by convention — **the
right and left DRG are TRULY SEPARATE BILATERAL STRUCTURES**
(anatomical, not a wiring convention). The **right DRG** is in
the **right NTS region**; the **left DRG** is in the **left
NTS region**. Consumers must **not** conflate the two.
**Boundary status (NOT a tree-wiring artifact — the right DRG IS
actually respiratory):** **Boundary case — the right dorsal
respiratory group IS a respiratory structure, NOT a tree-wiring
artifact.** Unlike the **right cuneate nucleus** (a somatosensory
relay wired under ``respiratory_center`` as a tree-wiring
artifact) and unlike the **right area postrema** / **right
chemoreceptor trigger zone** (circumventricular chemoreceptive
structures), the **right DRG** (here) **IS** actually a
**respiratory pattern generator** — it **participates in
inspiratory pattern generation** and **relays pulmonary stretch
receptor input** to the **respiratory rhythm generator**. The
**"respiratory_center"** label is **functionally accurate** for
this child.
**Boundary status (NOT the right ventral respiratory group — a
DIFFERENT respiratory generator in a DIFFERENT container):**
**Boundary case — the right dorsal respiratory group is NOT the
right ventral respiratory group (VRG).** The **right VRG**
(``.../ventral_respiratory_group/right/``) is the **right ventral
respiratory** rhythm and pattern generator group — containing
the **right Bötzinger complex**, **right pre-Bötzinger complex**,
**right nucleus para-ambiguus**, **right nucleus retroambiguus**,
**right nucleus retrofacialis**, and **right retrotrapezoid
nucleus** — in the **right ventrolateral medulla**. **They are
DIFFERENT RESPIRATORY STRUCTURES** in **DIFFERENT CONTAINERS** —
the **right DRG** is **dorsal** (in the **right NTS region**); the
**right VRG** is **ventrolateral**. They are **functionally
coupled** — the right DRG **relays** input to the **right
pre-Bötzinger complex** (the **primary respiratory rhythm
generator**) — but they are **anatomically distinct**. Consumers
must **not** conflate the two.
**Boundary status (NOT the right solitary nucleus (NTS) — the
right NTS is the parent region in the literature, wired as a
SEPARATE container in this tree):** **Boundary case — the right
dorsal respiratory group is NOT the right solitary nucleus
(NTS).** The **right solitary nucleus**
(``.../solitary_nucleus/right/``) is the **right visceral afferent
relay** — it is a **separate container** under
``medulla_oblongata``. **In the literature**, the **right DRG** is
**often considered part of** the **right NTS** — it is in the
**ventrolateral right NTS region**. **In this tree**, the **right
DRG** is **wired as a separate leaf** under
``respiratory_center.dorsal_respiratory_group``, **NOT** under
the **right NTS container**. Consumers must **not** expect to
find the right DRG under ``solitary_nucleus.right`` — resolve it
via ``respiratory_center.dorsal_respiratory_group.right``. **The
tree separates** the **right NTS** and the **right DRG** into
**two modules** as a **deliberate wiring choice** — the **right
DRG** is a **functional respiratory group within the right NTS
region**; the **right NTS** is the **broader visceral afferent
relay** of which the **right DRG** is a **functional subregion**.
**Boundary status (NOT the right area postrema or right
chemoreceptor trigger zone — DIFFERENT children of
respiratory_center):** **Boundary case — the right dorsal
respiratory group is NOT the right area postrema or right
chemoreceptor trigger zone.** The **right area postrema** and
**right chemoreceptor trigger zone**
(``.../area_postrema/right/`` and
``.../chemoreceptor_trigger_zone/right/``) are **circumventricular
chemoreceptive** structures for the **vomiting reflex** — **NOT**
respiratory pattern generators. **They are DIFFERENT
STRUCTURES** — children of ``respiratory_center`` — but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the right cuneate or right gracile nucleus
— DIFFERENT children of respiratory_center):** **Boundary case
— the right dorsal respiratory group is NOT the right cuneate or
right gracile nucleus.** The **right cuneate** and **right
gracile nuclei**
(``.../respiratory_center/cuneate_nucleus/right/`` and
``.../respiratory_center/gracile_nucleus/right/``) are the
**right dorsal column somatosensory relays** (fine touch,
vibration, proprioception). **They are DIFFERENT STRUCTURES** —
children of ``respiratory_center`` — but they are **functionally
distinct**. The **right DRG IS respiratory**; the **right cuneate
and right gracile nuclei are somatosensory**. Consumers must
**not** conflate them.
**Boundary status (NOT the right gigantocellular reticular
nucleus — a DIFFERENT child of respiratory_center):** **Boundary
case — the right dorsal respiratory group is NOT the right
gigantocellular reticular nucleus (Gi).** The **right
gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/right/``)
is a **right ventrolateral reticular** nucleus — it is involved
in **respiration**, **autonomic function**, and **descending
pain modulation**. **They are DIFFERENT STRUCTURES** — children
of ``respiratory_center`` — but they are **functionally
distinct** — the **right DRG** is a **dorsal respiratory pattern
generator** in the **right NTS region**; the **right Gi** is a
**ventrolateral reticular nucleus** with **broader** respiratory,
autonomic, and pain functions. Consumers must **not** conflate
the two.
**Boundary status (NOT the right parafacial zone — a
sleep-promoting region in a DIFFERENT container):** **Boundary
case — the right dorsal respiratory group is NOT the right
parafacial zone.** The **right parafacial zone**
(``.../parafacial_zone/right/``) is a **GABAergic / glycinergic
sleep-promoting** region — **NOT** a respiratory pattern
generator and **NOT** wired under ``respiratory_center``.
Consumers must **not** conflate the two.
**Boundary status (NOT the right retrotrapezoid nucleus, right
Bötzinger complex, right pre-Bötzinger complex, or other right
VRG subnuclei — DIFFERENT structures in a DIFFERENT container):**
**Boundary case — the right dorsal respiratory group is NOT the
right retrotrapezoid nucleus, the right Bötzinger complex, the
right pre-Bötzinger complex, or any other right VRG subnucleus.**
Those are **right ventral respiratory** structures — wired under
the **separate** ``ventral_respiratory_group`` container. **They
are DIFFERENT STRUCTURES** from the right dorsal respiratory
group — different **dorsoventral position**, different
**functions** (right VRG = rhythm / pattern; right DRG =
pulmonary stretch relay / inspiratory pattern). Consumers must
**not** conflate the right DRG with any right VRG subnucleus.
**Boundary status (NOT the right NTS or the right vagal afferent
system — the right DRG RECEIVES right vagal input but is NOT the
vagus itself):** **Boundary case — the right dorsal respiratory
group is NOT the right solitary nucleus (NTS) or the right
vagal afferent system.** The **right DRG** **receives** **right
pulmonary stretch receptor** input via **right vagal afferents**
— those **afferents** **synapse** in the **right NTS region**
(which is anatomically the **right DRG's home region**) — but
the **right DRG neurons** are **right second-order respiratory
neurons**, **NOT** right primary afferent neurons. Consumers
must **not** conflate the right DRG with the right vagal
afferent system itself.
**Boundary status (NOT the whole dorsal_respiratory_group
container — an ASPECT of it):** **Boundary case — the right
dorsal respiratory group is NOT the whole
dorsal_respiratory_group container.** The **whole
dorsal_respiratory_group**
(``.../dorsal_respiratory_group/``) is the **bilateral
container** that **contains** the right DRG (here) **plus** the
left DRG. Consumers must **not** conflate the **leaf** with the
**container**.
**Boundary status (NOT the whole respiratory_center or whole
medulla oblongata — a leaf in a chain of containers):**
**Boundary case — the right dorsal respiratory group is NOT the
whole respiratory_center or the whole medulla oblongata.** It
is a **leaf** at the **bottom** of a **chain** of containers:
``medulla_oblongata`` → ``respiratory_center`` →
``dorsal_respiratory_group`` → ``right``. Consumers must **not**
conflate the **leaf** with **any of the parent containers**.

Overview
--------
The **right dorsal respiratory group (DRG)** is the **right-side**
group of **respiratory-related neurons** in the **ventrolateral
region of the right nucleus tractus solitarius (NTS)** in the
**right dorsal medulla oblongata**. It is **involved in
inspiratory pattern generation** and **relays right pulmonary
stretch receptor input** (via **right vagal afferents**) to the
**respiratory rhythm generator** (the **right pre-Bötzinger
complex** in the **right ventral respiratory group**).

**This is a LEAF module.** The **right DRG** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution of the right
side use this module; consumers that need **left-side**
resolution use ``.../dorsal_respiratory_group/left/``;
consumers that need the **whole dorsal_respiratory_group
container** use ``.../dorsal_respiratory_group/``.

**The right DRG IS actually respiratory — NOT a tree-wiring
artifact.** Unlike the **right cuneate nucleus** (a somatosensory
relay wired under ``respiratory_center`` as a tree-wiring
artifact) and unlike the **right area postrema** / **right
chemoreceptor trigger zone** (circumventricular chemoreceptive
structures), the **right DRG** **IS** actually a **respiratory
pattern generator**. The **"respiratory_center"** label is
**functionally accurate** for this child.

**The right DRG is OFTEN CONSIDERED PART OF THE right NTS in the
literature.** It is in the **ventrolateral right NTS region**.
**In this tree**, the **right DRG is wired as a separate leaf**
under ``respiratory_center.dorsal_respiratory_group``, **NOT**
under the **right NTS container** (``.../solitary_nucleus/right/``).
**The tree separates the right NTS and the right DRG into two
modules** as a **deliberate wiring choice** — the **right DRG**
is a **functional respiratory group within the right NTS
region**; the **right NTS** is the **broader visceral afferent
relay** of which the **right DRG** is a **functional subregion**.

**The right DRG is TRULY BILATERAL — the right / left split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **right** and **left**
DRG are **anatomically separate structures** — the **right DRG**
is in the **right NTS region**; the **left DRG** is in the
**left NTS region**. The **right / left split** here reflects
**anatomy** — **NOT** a **tree-wiring convention**.

**The right DRG relays IPSILATERAL input to the IPSILATERAL VRG.**
The **right DRG** receives **right pulmonary stretch receptor**
input via **right vagal afferents** — and it **projects**
primarily to the **right pre-Bötzinger complex** (in the **right
VRG**) — contributing to the **right-side inspiratory pattern**.
There is also some **crossed** projection — the **right DRG**
can influence the **left VRG** via **commissural** pathways —
but the **predominant** projection is **ipsilateral**.

The Right Dorsal Respiratory Group / Left Dorsal Respiratory Group Boundary
--------------------------------------------------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right DRG** (this module) — the DRG of the **right** medulla,
    in the **right NTS region**.

*   **Left DRG** (``.../dorsal_respiratory_group/left/``) — the
    DRG of the **left** medulla, in the **left NTS region**.

**They are TRULY SEPARATE BILATERAL STRUCTURES** — the **right**
and **left** DRG are **anatomically distinct** (not a wiring
convention for a midline organ). They are **structurally
symmetric mirror pairs** — same cytoarchitecture, same
ipsilateral vagal input, same **no warning**. Consumers must
**not** conflate the right with the left — resolve the left side
via ``dorsal_respiratory_group.left``.

The Right Dorsal Respiratory Group / Right Ventral Respiratory Group Boundary
---------------------------------------------------------------------------
This is the **most consequential** respiratory-generator
boundary:

*   **Right DRG** (this module) — the **right dorsal respiratory**
    pattern generator in the **right NTS region**.

*   **Right VRG** (``.../ventral_respiratory_group/right/``) — the
    **right ventral respiratory** rhythm and pattern generator
    group (right Bötzinger complex, right pre-Bötzinger complex,
    right nucleus para-ambiguus, right nucleus retroambiguus,
    right nucleus retrofacialis, right retrotrapezoid nucleus).

**They are DIFFERENT RESPIRATORY STRUCTURES** in **DIFFERENT
CONTAINERS** — the **right DRG** is **dorsal** (in the **right
NTS region**); the **right VRG** is **ventrolateral**. They are
**functionally coupled** — the right DRG **relays** input to the
**right pre-Bötzinger complex** — but they are **anatomically
distinct**. Consumers must **not** conflate the two.

The Right Dorsal Respiratory Group / Right Solitary Nucleus Boundary
-------------------------------------------------------------------
This is the **functional respiratory group / broader visceral
relay** boundary:

*   **Right DRG** (this module) — the **right respiratory group**
    within the **right NTS region**.

*   **Right solitary nucleus (NTS)**
    (``.../solitary_nucleus/right/``) — the **right broader
    visceral afferent relay** — **wired separately** under
    ``medulla_oblongata``.

**The right DRG is often considered part of the right NTS in the
literature** — but **in this tree**, the two are **wired as
separate modules**. The **right DRG** is a **functional
respiratory group within the right NTS region**; the **right
NTS** is the **broader visceral afferent relay**. Consumers must
**not** expect to find the right DRG under
``solitary_nucleus.right`` — resolve it via
``respiratory_center.dorsal_respiratory_group.right``.

The Right Dorsal Respiratory Group / Right Area Postrema and Right Chemoreceptor Trigger Zone Boundary
-----------------------------------------------------------------------------------------------------
This is the **respiratory / circumventricular** boundary:

*   **Right DRG** (this module) — the **right respiratory pattern
    generator**.

*   **Right area postrema** and **right chemoreceptor trigger
    zone** (``.../area_postrema/right/`` and
    ``.../chemoreceptor_trigger_zone/right/``) — the
    **right circumventricular chemoreceptive** structures for the
    **vomiting reflex**.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Right Dorsal Respiratory Group / Right Cuneate and Right Gracile Nuclei Boundary
-----------------------------------------------------------------------------------
This is the **respiratory / somatosensory** boundary:

*   **Right DRG** (this module) — the **right respiratory pattern
    generator**.

*   **Right cuneate nucleus** and **right gracile nucleus**
    (``.../cuneate_nucleus/right/`` and
    ``.../gracile_nucleus/right/``) — the **right dorsal column
    somatosensory** relays.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
The **right DRG IS respiratory**; the **right cuneate and right
gracile nuclei are somatosensory**. Consumers must **not**
conflate them.

The Right Dorsal Respiratory Group / Right Gigantocellular Reticular Nucleus Boundary
------------------------------------------------------------------------------------
This is the **dorsal respiratory / ventrolateral reticular**
boundary:

*   **Right DRG** (this module) — the **right dorsal respiratory**
    pattern generator in the **right NTS region**.

*   **Right gigantocellular reticular nucleus**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/right/``)
    — the **right large ventrolateral reticular** nucleus with
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

**They are DIFFERENT STRUCTURES** — children of
``respiratory_center`` — but they are **functionally distinct**.
Consumers must **not** conflate the two.

The Right Dorsal Respiratory Group / Right Parafacial Zone Boundary
------------------------------------------------------------------
This is the **respiratory / sleep-promoting** boundary:

*   **Right DRG** (this module) — the **right respiratory pattern
    generator**.

*   **Right parafacial zone** (``.../parafacial_zone/right/``) —
    the **right GABAergic / glycinergic sleep-promoting**
    region.

**They are DIFFERENT STRUCTURES** in **DIFFERENT containers**.
Consumers must **not** conflate the two.

The Right Dorsal Respiratory Group / Right VRG Subnuclei Boundary
----------------------------------------------------------------
This is the **right DRG / specific right VRG subnucleus** boundary:

*   **Right DRG** (this module) — the **right dorsal respiratory**
    pattern generator.

*   **Right retrotrapezoid nucleus**, **right Bötzinger complex**,
    **right pre-Bötzinger complex**, **right nucleus
    para-ambiguus**, **right nucleus retroambiguus**, **right
    nucleus retrofacialis** — **specific right VRG subnuclei** in
    the ``ventral_respiratory_group`` container.

**They are DIFFERENT STRUCTURES** — the **right DRG** is
**dorsal**; the **right VRG subnuclei** are **ventrolateral**.
Consumers must **not** conflate the right DRG with any right VRG
subnucleus.

The Right Dorsal Respiratory Group / Whole Dorsal Respiratory Group, Whole Respiratory Center, and Whole Medulla Oblongata Boundary
----------------------------------------------------------------------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Right DRG** (this module) — one **leaf** of the
    ``dorsal_respiratory_group`` container.

*   **Dorsal respiratory group** (``.../dorsal_respiratory_group/``)
    — the **bilateral container** of the right + left DRG.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children** (of which
    ``dorsal_respiratory_group`` is one).

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The right DRG is a LEAF in a CHAIN of containers.** Consumers
must **not** conflate the **leaf** with any of the **parent
containers**.

Function in the Human Brain
---------------------------
The right DRG's function is **inspiratory pattern generation** and
**right pulmonary stretch receptor relay** — **NOT respiratory
rhythm generation** (that is the right VRG's pre-Bötzinger
complex) and **NOT motor control**:

*   **Right inspiratory pattern generation:** The **right DRG** is
    **involved in shaping the right inspiratory pattern** — it
    **contributes** to the **right inspiratory "on-switch"**,
    **"off-switch"**, and **ramp** — **relaying** input from
    **right pulmonary stretch receptors** and **higher**
    respiratory centers to the **right pre-Bötzinger complex**
    (right VRG) — but the **primary rhythm generator** is the
    **right pre-Bötzinger complex**, **NOT** the right DRG.

*   **Right pulmonary stretch receptor relay (Hering-Breuer
    reflex):** The **right DRG** **receives** **right pulmonary
    stretch receptor** **afferent** input via **right vagal
    afferents** — it **relays** this input to the **right
    respiratory rhythm generator** — this is the **right-side
    neural substrate** of the **Hering-Breuer inflation
    reflex** (which **inhibits inspiration** when the **right
    lung** is **inflated**).

*   **Right vagal afferent respiratory input:** The **right DRG**
    also **receives** **other right vagal respiratory
    afferents** — including **chemoreceptor** input (from the
    **right carotid body** via **right CN IX** — though much of
    this is relayed via the **right NTS** more broadly) and
    **irritant receptor** input. It **relays** these to the
    **right VRG** and **higher** centers.

*   **Integration with higher respiratory centers:** The **right
    DRG** **receives** **descending** input from the **right
    and left cortex**, the **hypothalamus**, the **pons**
    (pneumotaxic center), and the **medullary** respiratory
    network — it **integrates** these with **right vagal
    afferent** input and **relays** the result to the **right
    pre-Bötzinger complex** and other **right VRG** targets.

*   **NOT respiratory rhythm generation:** The **respiratory
    rhythm** is generated by the **right pre-Bötzinger complex**
    (right VRG) — **NOT** the right DRG. The **right DRG**
    **contributes** to **right inspiratory pattern** but **does
    not generate** the **rhythm**.

*   **NOT motor control:** The **right DRG** does **not** send
    motor axons to muscles — the **right phrenic motor nucleus**
    (in the **right cervical spinal cord**) and the **right
    intercostal motor nuclei** (in the **right thoracic spinal
    cord**) are the **motor neurons** for breathing. The right
    DRG **modulates** them via its projections to the **right
    VRG** and other **respiratory** centers.

**The unifying theme:** the right DRG is a **right respiratory
pattern generator** in the **right NTS region** — it **relays
right pulmonary stretch receptor input** and **shapes right
inspiratory pattern** via projections to the **right
pre-Bötzinger complex** (right VRG) — **NOT** the right
respiratory rhythm generator, **NOT** the right NTS itself (in
this tree), **NOT** the right VRG, and **NOT** the right area
postrema / right CTZ.

Associated Disorders
--------------------
The right DRG is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct** and
**indirect**, via **right respiratory pattern** and **right
pulmonary stretch reflex** dysfunction:

*   **Central hypoventilation (via right DRG dysfunction —
    indirect and partial):** **Damage** to the **right DRG** can
    **contribute** to **central hypoventilation** — but the
    **primary** respiratory rhythm generators are the **right
    pre-Bötzinger complex** (right VRG) and other **brainstem**
    structures. **Isolated right DRG lesions** rarely cause
    **full-blown central hypoventilation** — the **left DRG**,
    the **VRG**, and **higher centers** can partially
    compensate.

*   **Impaired Hering-Breuer reflex (via right DRG
    dysfunction):** **Reduced** or **absent** **right-side
    Hering-Breuer inflation reflex** — from **right DRG**
    dysfunction — **contributing** to **altered** **breathing
    pattern**. This is a **subtle** finding — not a named
    syndrome — and is usually **part of a broader brainstem
    lesion**.

*   **Sleep-disordered breathing (via right DRG involvement —
    hypothesized):** **Right DRG** dysfunction may
    **contribute** to **sleep-disordered breathing** (central
    sleep apnea, hypopneas) — but the **primary** central
    control of breathing during sleep is the **pre-Bötzinger
    complex** (VRG) and **higher** centers.

*   **Brainstem stroke (via right DRG involvement):** **Right
    medullary stroke** (lateral medullary syndrome, medial
    medullary syndrome, or **right dorsal medullary** lesions)
    can **involve** the **right DRG** — contributing to
    **right-side respiratory pattern** abnormalities and
    **sleep-disordered breathing**.

*   **Rett syndrome and other central respiratory disorders
    (via broader brainstem dysfunction):** **Rett syndrome**
    and other **central respiratory disorders** involve
    **broader** brainstem dysfunction — including the **right
    DRG** and the **right NTS** — contributing to **breathing
    dysrhythmias**.

*   **No Named "Right Dorsal Respiratory Group Syndrome":** The
    right DRG is a **functional respiratory group** — its
    clinical syndromes are **named for the broader brainstem
    lesion** (brainstem stroke, central hypoventilation
    syndrome) or the **functional abnormality** (impaired
    Hering-Breuer reflex, sleep-disordered breathing) — **NOT**
    for the right DRG itself. There is **no named "right DRG
    syndrome"**.

**What is NOT here:** The right DRG is **not** the substrate for
**respiratory rhythm generation** (right pre-Bötzinger complex,
right VRG), **emesis** (right area postrema / right CTZ),
**somatosensory loss** (right cuneate / right gracile nuclei),
**autonomic dysfunction** (right RVLM, right CVLM, right NTS),
**tongue weakness** (right hypoglossal nucleus), or
**parasympathetic dysfunction** (right dorsal motor nucleus of
the vagus). Its clinical relevance is the **right inspiratory
pattern** and **right pulmonary stretch reflex** functions listed
above.

Lateralization Notes
--------------------
This is the **right** DRG module. The dorsal respiratory group is
a **bilateral container** whose two sides are **ANATOMICALLY
SEPARATE** — **not** a wiring convention for a midline organ
(unlike the area postrema / CTZ) — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **right** and **left** DRG are
    **structurally symmetric** — they are **mirror pairs** with
    the **same** cytoarchitecture, **same** ipsilateral vagal
    input, and **same** functions. The **right** DRG is in the
    **right NTS region**; the **left** DRG is in the **left
    NTS region**.

*   **Predominantly Ipsilateral, Partly Crossed Projections:**
    The **right DRG** projects **predominantly ipsilaterally**
    (to the **right pre-Bötzinger complex** and the **right
    VRG**) — with some **crossed** projection to the **left
    VRG** via **commissural** pathways. This **functional
    ipsilaterality** is **part of the respiratory network's
    bilateral coordination** — the **right and left DRG**
    together coordinate **breathing** bilaterally.

*   **NO Lateralization Warning:** The DRG has **no known
    functional lateralization** in humans — the **right** and
    **left** DRG are **functionally symmetric** at the **group
    level**. Consumers must **not** import a **lateralization
    warning** into the right DRG — the **right** and **left**
    sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right DRG is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the right DRG.

*   **NO Fear-Output Warning:** The right DRG is **not** a
    fear-output structure — it is a **right dorsal respiratory
    pattern generator**. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "right DRG = left DRG" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **group level**. The DRG is a
**strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right DRG is a **leaf** —
    it does **not** import from ``.../left/`` or any other
    left-side module. The **right / left split** is
    **ANATOMICAL** — not a **wiring convention**. The **right**
    and **left** DRG are **truly separate bilateral
    structures**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../ventral_respiratory_group/``,
    ``.../solitary_nucleus/``,
    ``.../area_postrema/``,
    ``.../chemoreceptor_trigger_zone/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../parafacial_zone/``, ``.../cranial_nerve_nuclei/``,
    or any other container. The right DRG's relationships to the
    right VRG, right NTS, right area postrema, right CTZ, right
    cuneate nucleus, right gracile nucleus, right gigantocellular
    reticular nucleus, right parafacial zone, and right cranial
    nerve nuclei are documented as **prose and boundary data**,
    not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right DRG is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../right/``.
*   **ANATOMICAL BILATERALITY, NOT a wiring convention.** The
    ``right`` and ``left`` DRG are **anatomically separate
    structures** — unlike the **area postrema** / **CTZ** (which
    are midline organs wired as left/right by convention).
*   **RESPIRATORY, NOT a tree-wiring artifact.** Unlike the right
    cuneate nucleus, the right DRG **IS** actually a respiratory
    structure — the **"respiratory_center"** label is
    **functionally accurate** for this child.
*   **NTS-overlap caveat.** The right DRG is **often considered
    part of the right NTS** in the literature — but in **this
    tree**, the right DRG is **wired as a separate leaf** under
    ``respiratory_center.dorsal_respiratory_group``, **NOT**
    under the right NTS container. Consumers must **not** expect
    to find the right DRG under ``solitary_nucleus.right``.
*   **NOT the left DRG.** The **left DRG** is a **separate leaf**
    under ``.../dorsal_respiratory_group/left/``. Consumers must
    **not** conflate the right with the left.
*   **NOT the right VRG.** The **right VRG** is a **separate
    container** — the **dorsal vs. ventral** distinction is the
    **most consequential** right DRG boundary.
*   **NOT the right area postrema or right CTZ.** Those are
    **circumventricular chemoreceptive** structures — **NOT**
    respiratory pattern generators.
*   **NOT the right cuneate or right gracile nucleus.** Those are
    **somatosensory relays** — **NOT** respiratory structures.
*   **NOT the right gigantocellular reticular nucleus.** That is a
    **right ventrolateral reticular** nucleus with **broader**
    respiratory, autonomic, and pain functions — **NOT** the
    dorsal respiratory pattern generator.
*   **NOT the right parafacial zone.** That is a
    **sleep-promoting** region — **NOT** a respiratory pattern
    generator.
*   **NOT the right retrotrapezoid nucleus, right Bötzinger
    complex, right pre-Bötzinger complex, or any other right VRG
    subnucleus.** Those are **right ventrolateral VRG**
    structures — **NOT** the right dorsal respiratory group.
*   **NOT the whole dorsal_respiratory_group, whole
    respiratory_center, or whole medulla oblongata.** The right
    DRG is a **leaf** in a **chain** of containers.
*   **No ``AREA_PATHS`` hop.** The right DRG is a **local leaf** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The right DRG has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the left DRG — strict mirror with
    NO warning.** The right and left modules are **structurally
    identical** — same leaf status, same **dorsal respiratory
    pattern generator** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.dorsal_respiratory_group.right"
    )

**Do not** assume the right DRG is the **left DRG**. The left
DRG is the **separate leaf** at
``.../dorsal_respiratory_group/left/``. They are **truly
separate bilateral structures** — the right DRG is in the **right
NTS region**; the left DRG is in the **left NTS region**.

**Do not** assume the right DRG is the **right ventral respiratory
group (VRG)**. The right VRG is a **separate container** under
``medulla_oblongata`` — the **dorsal vs. ventral** distinction
is the **most consequential** right DRG boundary.

**Do not** expect to find the right DRG under
``solitary_nucleus.right``. The **right NTS** is a **separate
container** — the right DRG is a **functional respiratory group
within the right NTS region** but is **wired separately** under
``respiratory_center`` in this tree.

**Do not** assume the right DRG is the **right area postrema** or
the **right chemoreceptor trigger zone**. Those are
**circumventricular chemoreceptive** structures — **NOT**
respiratory pattern generators.

**Do not** assume the right DRG is the **right cuneate** or
**right gracile** nucleus. Those are **somatosensory relays** —
**NOT** respiratory structures.

**Do not** assume the right DRG is the **right gigantocellular
reticular nucleus**, the **right parafacial zone**, the **right
retrotrapezoid nucleus**, the **right Bötzinger complex**, the
**right pre-Bötzinger complex**, or any other right VRG
subnucleus. Each is a **different structure**.

**Do not** assume the right DRG has **structural children**. It
is a **leaf** — it represents the right DRG as a **single
structure**.

**Do not** infer **midline wiring convention** from the right DRG
structure. The **right / left split** is **ANATOMICAL** — the
**right** and **left** DRG are **truly separate bilateral
structures** (unlike the area postrema / CTZ, which are midline
organs wired as left/right by convention).

Iterating the right DRG's (empty) children (recommended consumer
pattern)::

    RIGHT_DORSAL_RESPIRATORY_GROUP_CHILDREN = ()
    # The right DRG is a leaf. It has no structural children.

Reaching the left DRG (recommended consumer pattern — the
contralateral leaf, a TRULY SEPARATE structure)::

    # The left DRG is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.left
    #
    # The right and left DRG are TRULY SEPARATE BILATERAL
    # STRUCTURES (anatomical, not a wiring convention).

Reaching the right ventral respiratory group (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The right ventral respiratory group is a SEPARATE container
    # under medulla_oblongata — NOT wired under
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right
    #
    # The right DRG (dorsal respiratory group) and the right VRG
    # (ventral respiratory group) are DIFFERENT RESPIRATORY
    # STRUCTURES in DIFFERENT CONTAINERS — the right DRG is dorsal
    # (in the right NTS region); the right VRG is ventrolateral
    # (right Bötzinger complex, right pre-Bötzinger complex, right
    # nucleus para-ambiguus, right nucleus retroambiguus, right
    # nucleus retrofacialis, right retrotrapezoid nucleus). The
    # right DRG RELAYS input to the right VRG — but they are
    # anatomically distinct.

Reaching the right solitary nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The right solitary nucleus (NTS) is a SEPARATE container
    # under medulla_oblongata — the right DRG is often considered
    # part of the right NTS in the literature, but is wired as a
    # separate leaf of respiratory_center in this tree:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
    #
    # The right DRG is a functional respiratory group WITHIN the
    # right NTS region — the tree separates the two into two
    # modules as a deliberate wiring choice.

Reaching the right area postrema and right CTZ (recommended
consumer pattern — NOTE the DIFFERENT leaves of
respiratory_center)::

    # The right area postrema and the right chemoreceptor trigger
    # zone are CIRCUMVENTRICULAR structures — leaves of
    # respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.right
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.right
    #
    # They are NOT respiratory pattern generators — they are
    # chemoreceptive / emetic structures.

Reaching the right cuneate and right gracile nuclei
(recommended consumer pattern — NOTE the DIFFERENT leaves of
respiratory_center)::

    # The right cuneate and right gracile nuclei are SOMATOSENSORY
    # relays — leaves of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus.right
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus.right
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
        # NOTE: the right and left DRG are TRULY SEPARATE
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