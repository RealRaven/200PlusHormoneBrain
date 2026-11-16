"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
==================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── rostral_ventrolateral_medulla   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Rostral ventrolateral medulla; RVLM; rostral
ventrolateral medullary region; rostral ventrolateral medullary
pressor area; vasomotor center; sympathoexcitatory center;
"the sympathetic premotor center."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter region** in the **rostral ventrolateral
medulla oblongata** — a **sympathetic premotor / vasomotor**
region that provides **tonic excitatory drive** to the
**intermediolateral (IML) cell column** of the **thoracic and
upper lumbar spinal cord**. It is **NOT** a respiratory nucleus
(that is the **VRG** and **DRG**), **NOT** a sympathoinhibitory
relay (that is the **CVLM**), **NOT** a ventral-surface
chemosensory nucleus (that is the **arcuate nucleus**), **NOT**
a sleep-promoting region (that is the **parafacial zone**), and
**NOT** a reticular nucleus (those are the **Gi** and
**paramedian reticular nucleus**).
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**. It is a **direct child**
of ``medulla_oblongata`` — **NOT** a child of
``respiratory_center`` and **NOT** a child of any other
container. It is a **sibling** of ``respiratory_center``,
``caudal_ventrolateral_medulla``, ``solitary_nucleus``,
``ventral_respiratory_group``, and other medullary containers.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** RVLM.
**Anatomically**, the left and right RVLM are **truly separate
bilateral structures** (unlike the area postrema, which is a
midline organ wired as left/right by convention) — the **left
RVLM** provides **sympathetic premotor drive** primarily to the
**left IML column** (with some crossed components); the **right
RVLM** provides **sympathetic premotor drive** primarily to the
**right IML column** (with some crossed components).
**Boundary status (NOT the CVLM — the CVLM is the CAUDAL
ventrolateral medulla):** **Boundary case — the RVLM is NOT the
CVLM.** The **CVLM** (``.../caudal_ventrolateral_medulla/``) is
the **caudal** ventrolateral medulla — the **sympathoinhibitory
relay** that **inhibits the RVLM** (via **GABAergic** input from
the **NTS**). The **RVLM** (here) is the **rostral**
ventrolateral medulla — the **sympathetic premotor** center
that **drives** sympathetic outflow. **They are DIFFERENT
STRUCTURES at DIFFERENT rostrocaudal levels** — the **RVLM** is
**rostral**; the **CVLM** is **caudal**. They are **functionally
coupled** in the **medullary baroreflex arc** (NTS → CVLM →
RVLM → IML column) but are **anatomically distinct**. Consumers
must **not** conflate the two — the **RVLM** **drives**
sympathetic outflow; the **CVLM** **inhibits** it. This is the
**most consequential** RVLM boundary.
**Boundary status (NOT the NTS — the NTS is the VISCERAL
AFFERENT relay):** **Boundary case — the RVLM is NOT the
solitary nucleus (NTS).** The **NTS**
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
it receives **baroreceptor**, **chemoreceptor**, and
**gastrointestinal** afferents. The **RVLM** (here) is the
**sympathetic premotor** center — it **receives** NTS input
**via** the **CVLM** and **directly** (gluatamatergic and
GABAergic projections) — and it **projects** to the **IML
column**. **They are DIFFERENT STRUCTURES** — the **NTS** is the
**afferent** relay; the **RVLM** is the **sympathetic premotor**
center. Consumers must **not** conflate the two.
**Boundary status (NOT the arcuate nucleus — a DIFFERENT
ventral-surface chemosensory nucleus):** **Boundary case — the
RVLM is NOT the arcuate nucleus.** The **arcuate nucleus**
(``.../arcuate_nucleus/``) is a **ventral-surface grey-matter**
chemosensory and hypothalamic-projecting nucleus at the
**ventral medullary surface**, adjacent to the **anterior
median fissure**. The **RVLM** (here) is a **more lateral**
ventrolateral medullary region — it is **NOT** the arcuate
nucleus. **They are DIFFERENT STRUCTURES** — the **arcuate
nucleus** is **ventral-surface chemosensory**; the **RVLM** is
**ventrolateral sympathetic premotor**. Consumers must **not**
conflate the two.
**Boundary status (NOT the parafacial zone — a sleep-promoting
region):** **Boundary case — the RVLM is NOT the parafacial
zone.** The **parafacial zone** (``.../parafacial_zone/``) is a
**GABAergic / glycinergic sleep-promoting** region — **NOT** a
sympathetic premotor center. They are **anatomically adjacent**
in the **rostral ventrolateral medulla**, but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the VRG — a DIFFERENT respiratory
generator group):** **Boundary case — the RVLM is NOT the
ventral respiratory group (VRG).** The **VRG**
(``.../ventral_respiratory_group/``) is the **ventral
respiratory** rhythm and pattern generator group — containing
the **Bötzinger complex**, **pre-Bötzinger complex**, **nucleus
para-ambiguus**, **nucleus retroambiguus**, **nucleus
retrofacialis**, and **retrotrapezoid nucleus** — in the
**ventrolateral medulla**. The **RVLM** (here) is the
**sympathetic premotor** center. **They are DIFFERENT
STRUCTURES** — the **VRG** is **respiratory**; the **RVLM** is
**autonomic (sympathetic premotor)**. Both are **ventrolateral**
and **rostral** — but they are **distinct functional systems**.
Consumers must **not** conflate the two.
**Boundary status (NOT the DRG — a DIFFERENT respiratory
generator in a DIFFERENT container):** **Boundary case — the
RVLM is NOT the dorsal respiratory group (DRG).** The **DRG**
(``.../respiratory_center/dorsal_respiratory_group/``) is the
**dorsal respiratory** pattern generator in the **NTS region**.
The **RVLM** (here) is the **ventrolateral sympathetic
premotor** center. **They are DIFFERENT STRUCTURES** —
**dorsal** vs. **ventrolateral** — **respiratory** vs.
**autonomic**. Consumers must **not** conflate the two.
**Boundary status (NOT the Gi or paramedian reticular nucleus —
reticular nuclei in DIFFERENT containers):** **Boundary case —
the RVLM is NOT the gigantocellular reticular nucleus (Gi) or
the paramedian reticular nucleus.** The **Gi**
(``.../respiratory_center/gigantocellular_reticular_nucleus/``)
is a **large ventrolateral reticular** nucleus with
**respiratory**, **autonomic**, and **pain-modulatory**
functions. The **paramedian reticular nucleus**
(``.../paramedian_reticular_nucleus/``) is a **smaller**,
**more medial** reticular nucleus with **cerebellar** and
**nociceptive** functions. The **RVLM** (here) is the
**sympathetic premotor** center. **They are DIFFERENT
STRUCTURES** — the **Gi** and **paramedian reticular nucleus**
are **reticular** nuclei (with **broader** functions); the
**RVLM** is a **sympathetic premotor** region. Consumers must
**not** conflate the two.
**Boundary status (NOT the area postrema or CTZ — circumventricular
structures):** **Boundary case — the RVLM is NOT the area
postrema or the chemoreceptor trigger zone.** Those are
**circumventricular chemoreceptive** structures for the
**vomiting reflex** — **NOT** sympathetic premotor centers.
Consumers must **not** conflate the two.
**Boundary status (NOT the cuneate or gracile nuclei —
somatosensory relays):** **Boundary case — the RVLM is NOT the
cuneate or gracile nucleus.** Those are **dorsal column
somatosensory relays** — **NOT** sympathetic premotor centers.
Consumers must **not** conflate the two.
**Boundary status (NOT the whole respiratory_center — a SIBLING
container):** **Boundary case — the RVLM is NOT the
respiratory_center.** The **respiratory_center**
(``.../respiratory_center/``) is a **sibling container** of the
RVLM — it contains the **DRG**, **Gi**, **cuneate**, **gracile**,
**area postrema**, and **CTZ**. The **RVLM** is **not a child**
of the ``respiratory_center`` — it is a **sibling container**
under ``medulla_oblongata``. Consumers must **not** expect to
find the RVLM under ``respiratory_center`` — resolve it via
``.../rostral_ventrolateral_medulla/``.
**Boundary status (NOT the whole medulla oblongata — a
sympathetic premotor region within it):** **Boundary case — the
RVLM is NOT the whole medulla oblongata.** The **medulla
oblongata** (``.../medulla_oblongata/``) is the **parent
container** — it contains the RVLM (here) **plus** the CVLM, the
NTS, the cranial nerve nuclei, the olivary body, the medullary
pyramid, the arcuate nucleus, the parafacial zone, the
paramedian reticular nucleus, the perihypoglossal nuclei, the
respiratory_center, the ventral respiratory group, and other
structures. The **RVLM** is **one sympathetic premotor region**
within the medulla. Consumers must **not** conflate the **RVLM**
with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
ANATOMICALLY SEPARATE structures):** **Boundary case — the RVLM
is a BILATERAL container whose left and right children are
ANATOMICALLY SEPARATE.** Unlike the **area postrema** (a
**midline** organ wired as left/right by convention), the
**RVLM** is a **truly paired** medullary structure — the **left
RVLM** is in the **left rostral ventrolateral medulla**; the
**right RVLM** is in the **right rostral ventrolateral
medulla**. **The left / right split here is ANATOMICAL, not a
wiring convention.** Consumers must **not** infer **midline
wiring convention** from the RVLM (that convention applies to
the area postrema / CTZ, NOT the RVLM).

Overview
--------
The **rostral ventrolateral medulla (RVLM)** is a **sympathetic
premotor / vasomotor** region in the **rostral ventrolateral
medulla oblongata**. It is the **primary source** of **tonic
excitatory drive** to the **intermediolateral (IML) cell
column** of the **thoracic and upper lumbar spinal cord** — the
**sympathetic preganglionic neurons** that control **blood
pressure**, **heart rate**, **regional blood flow**, and other
**sympathetic** functions.

**The RVLM is the SYMPATHETIC PREMOTOR center, NOT the
sympathoinhibitory center and NOT a respiratory generator.** The
**sympathoinhibitory** center is the **CVLM**
(``.../caudal_ventrolateral_medulla/``) — the **caudal**
ventrolateral medulla — which **inhibits** the RVLM. The
**respiratory** centers are the **VRG**
(``.../ventral_respiratory_group/``) and the **DRG**
(``.../respiratory_center/dorsal_respiratory_group/``). The
**RVLM** is the **sympathetic premotor** center — it **drives**
sympathetic outflow.

**The RVLM is the ROSTRAL ventrolateral medulla, NOT the caudal
ventrolateral medulla.** The **CVLM** is the **caudal**
sympathoinhibitory relay; the **RVLM** is the **rostral**
sympathetic premotor center. **They are DIFFERENT STRUCTURES at
DIFFERENT rostrocaudal levels** — the **RVLM** **drives**
sympathetic outflow; the **CVLM** **inhibits** it. They form the
**medullary baroreflex arc** (NTS → CVLM → RVLM → IML column).

**The RVLM is a BILATERAL container.** Its structural children
are ``left`` and ``right`` — each a leaf representing the left
or right RVLM. **Anatomically**, the left and right RVLM are
**truly separate bilateral structures** (not a midline wiring
convention). The **container itself** is **unpaired**.

**The RVLM is genuinely a SYMPATHETIC PREMOTOR center — NOT a
tree-wiring artifact.** Unlike the **cuneate nucleus** (a
somatosensory tree-wiring artifact under ``respiratory_center``)
and unlike the **area postrema** / **CTZ** (circumventricular
chemoreceptive structures), the **RVLM** **IS** actually a
**sympathetic premotor** center. Its classification as a
**sympathetic premotor** region is **functionally accurate**.

**The RVLM is functionally coupled to the NTS, the CVLM, the
IML column, the RVMM, the hypothalamus, the amygdala, the PAG,
and the rostral ventrolateral medullary autonomic network.** It
is **part of** the **medullary autonomic network** — a
**distributed system** for **cardiovascular regulation**,
**baroreflex control**, and **sympathetic outflow modulation**.

Bilateral Structure (Anatomical Pairing)
---------------------------------------
The rostral ventrolateral medulla is a **bilateral container** in
this tree with **two structural children**:

*   ``left`` — the **left** RVLM (a **leaf** module).
*   ``right`` — the **right** RVLM (a **leaf** module).

**The two children are ANATOMICALLY SEPARATE structures** —
**NOT** a wiring convention for a midline organ (unlike the
area postrema / CTZ). The **left RVLM** is in the **left
rostral ventrolateral medulla**; the **right RVLM** is in the
**right rostral ventrolateral medulla**.

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **RVLM** as **single structures**. Consumers
that need **side-specific** resolution descend into ``left`` or
``right``; consumers that need the **whole bilateral pair** use
``rostral_ventrolateral_medulla`` (the container) as a whole.

**The container itself is unpaired.** There is **no**
``rostral_ventrolateral_medulla/left/.../`` structural hierarchy
beyond the single leaf level — the ``left`` and ``right``
modules are the **terminal modules** for this structure.

The RVLM / CVLM Boundary
------------------------
This is the **most consequential** rostrocaudal boundary:

*   **RVLM** (this module) — the **rostral** ventrolateral medulla
    — the **sympathetic premotor / vasomotor** center.

*   **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **caudal** ventrolateral medulla — the **sympathoinhibitory
    relay**.

**They are DIFFERENT STRUCTURES at DIFFERENT rostrocaudal
levels** — the **RVLM** **drives** sympathetic outflow; the
**CVLM** **inhibits** it. They form the **medullary baroreflex
arc** (NTS → CVLM → RVLM → IML column). Consumers must **not**
conflate the two.

The RVLM / NTS Boundary
-----------------------
This is the **efferent / afferent** boundary:

*   **RVLM** (this module) — the **sympathetic premotor** center.

*   **NTS** (``.../solitary_nucleus/``) — the **visceral afferent
    relay**.

**The NTS is UPSTREAM of the RVLM in the baroreflex arc** — the
NTS receives **baroreceptor** afferents and **projects** to the
RVLM **directly** (glutamatergic and GABAergic projections) and
**via the CVLM**. Consumers must **not** conflate the two — the
**NTS** is the **afferent** relay; the **RVLM** is the
**sympathetic premotor** center.

The RVLM / Arcuate Nucleus and Parafacial Zone Boundary
-------------------------------------------------------
This is the **ventrolateral / ventral-surface-and-sleep-promoting**
boundary:

*   **RVLM** (this module) — the **ventrolateral sympathetic
    premotor** center.

*   **Arcuate nucleus** (``.../arcuate_nucleus/``) — the
    **ventral-surface chemosensory** nucleus.

*   **Parafacial zone** (``.../parafacial_zone/``) — the
    **sleep-promoting** region.

**They are DIFFERENT STRUCTURES** in the **rostral ventrolateral
medulla region**. Consumers must **not** conflate the **RVLM**
with the **arcuate nucleus** or with the **parafacial zone**.

The RVLM / VRG and DRG Boundary
-------------------------------
This is the **sympathetic premotor / respiratory** boundary:

*   **RVLM** (this module) — the **sympathetic premotor** center.

*   **VRG** (``.../ventral_respiratory_group/``) — the **ventral
    respiratory** rhythm and pattern generator group.

*   **DRG** (``.../respiratory_center/dorsal_respiratory_group/``)
    — the **dorsal respiratory** pattern generator.

**They are DIFFERENT STRUCTURES** — the **RVLM** is
**autonomic (sympathetic premotor)**; the **VRG** and **DRG** are
**respiratory**. Consumers must **not** conflate the RVLM with
either.

The RVLM / Gi and Paramedian Reticular Nucleus Boundary
-------------------------------------------------------
This is the **sympathetic premotor / reticular** boundary:

*   **RVLM** (this module) — the **sympathetic premotor** center.

*   **Gi** (``.../respiratory_center/gigantocellular_reticular_nucleus/``)
    — the **large ventrolateral reticular** nucleus with
    **respiratory**, **autonomic**, and **pain-modulatory**
    functions.

*   **Paramedian reticular nucleus**
    (``.../paramedian_reticular_nucleus/``) — the **smaller**,
    **more medial** reticular nucleus.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the **RVLM** with either reticular nucleus.

The RVLM / Other Medullary Structures Boundary
----------------------------------------------
This is the **sympathetic premotor / other-medullary-structures**
boundary:

*   **RVLM** (this module) — the **sympathetic premotor** center.

*   **Area postrema, CTZ, cuneate nucleus, gracile nucleus,
    cranial nerve nuclei, olivary body, medullary pyramid,
    perihypoglossal nuclei** — **other medullary structures**.

**Each is a DIFFERENT STRUCTURE.** Consumers must **not** conflate
the **RVLM** with any of these.

Function in the Human Brain
---------------------------
The RVLM's function is **sympathetic premotor drive** and
**cardiovascular regulation** — **NOT respiratory rhythm** and
**NOT sympathoinhibition**:

*   **Sympathetic premotor drive:** The **RVLM** provides **tonic
    excitatory drive** to the **IML column** — the **sympathetic
    preganglionic neurons** of the **thoracic and upper lumbar
    spinal cord**. This **tonic drive** maintains **resting
    sympathetic vasomotor tone** — **vascular smooth muscle
    constriction**, **heart rate**, and **blood pressure**.

*   **Baroreflex control:** The **RVLM** is the **efferent** limb
    of the **medullary baroreflex arc** (NTS → CVLM → RVLM → IML
    column). **Increased blood pressure** → **increased NTS
    activity** → **increased CVLM activity** → **decreased RVLM
    activity** → **decreased sympathetic outflow** →
    **decreased blood pressure**. **Decreased blood pressure** →
    **reverse** — **decreased NTS activity** → **decreased CVLM
    activity** → **increased RVLM activity** → **increased
    sympathetic outflow** → **increased blood pressure**. This is
    the **neural substrate** of the **baroreflex**.

*   **Chemoreflex control:** The **RVLM** **receives** input from
    the **NTS** (which relays **peripheral chemoreceptor**
    afferents) and **contributes** to the **sympathetic
    response** to **hypoxia** and **hypercapnia** — **increased
    sympathetic outflow** to **maintain blood pressure** during
    **chemoreflex activation**.

*   **Cardiovascular response to stress:** The **RVLM**
    **receives** descending input from the **hypothalamus**, the
    **amygdala**, the **PAG**, and other **higher** centers —
    and it **integrates** these with **NTS** input to **produce**
    the **sympathetic response** to **stress**, **exercise**,
    **hemorrhage**, and **other** challenges.

*   **Integration with other autonomic centers:** The **RVLM**
    **interacts** with the **RVMM (rostral ventromedial
    medulla)** and the **caudal pressor area (CPA)** — other
    **autonomic** regions in the **medulla** — to **coordinate**
    **sympathetic outflow** across **multiple targets**.

*   **NOT respiratory rhythm generation:** The **respiratory
    rhythm** is generated by the **pre-Bötzinger complex** (VRG) —
    **NOT** the RVLM.

*   **NOT sympathoinhibition:** The **sympathoinhibition** is the
    **CVLM** — **NOT** the RVLM.

**The unifying theme:** the RVLM is the **sympathetic premotor /
vasomotor** center in the **rostral ventrolateral medulla** — it
**provides tonic excitatory drive** to the **IML column** and
**integrates** afferent and descending input to **regulate blood
pressure**, **heart rate**, and **sympathetic outflow** —
**NOT** a respiratory generator, **NOT** a sympathoinhibitory
relay, and **NOT** a tree-wiring artifact.

Associated Disorders
--------------------
The RVLM is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct**, via
**sympathetic** dysfunction:

*   **Neurogenic hypertension (via RVLM overactivity):** **RVLM**
    **overactivity** — **increased** tonic **sympathetic drive**
    to the **IML column** — causes **increased sympathetic
    vasomotor tone** and **neurogenic hypertension**. This is
    the **direct substrate** of **sympathetic overactivity** in
    conditions such as **essential hypertension** (in some
    models) and **stress-induced hypertension**. The **RVLM** is
    a **major therapeutic target** for **centrally acting
    antihypertensives** (e.g., **clonidine**, **moxonidine** —
    α2-adrenergic and imidazoline receptor agonists that
    **reduce RVLM activity**).

*   **Baroreflex failure (via RVLM / NTS / CVLM circuit
    dysfunction):** **Disruption** of the **medullary baroreflex
    arc** — including the **RVLM** — causes **baroreflex
    failure** — **labile blood pressure**, **orthostatic
    hypotension**, and **hypertensive crises**.

*   **Brainstem stroke (via RVLM involvement):** **Lateral
    medullary syndrome (Wallenberg)** can **involve** the
    **RVLM** — contributing to **autonomic instability**,
    **neurogenic hypertension** (in some cases), and
    **cardiovascular** dysfunction.

*   **Central sleep apnea (via RVLM / autonomic brainstem
    dysfunction):** **Impaired** sympathetic **and** respiratory
    **integration** in the **medulla** can **contribute** to
    **central sleep apnea** — the **RVLM** is **part of** the
    **brainstem** network **integrating** respiration and
    autonomic function.

*   **Hypertensive crisis / sympathetic storm (via RVLM
    overactivity):** **Severe** RVLM **overactivity** —
    **increased sympathetic outflow** — can **precipitate**
    **hypertensive crisis** in conditions such as
    **pheochromocytoma**, **subarachnoid hemorrhage**, or
    **autonomic dysreflexia**. The **RVLM** is a **direct
    substrate** of the **sympathetic storm**.

*   **No Named "RVLM Syndrome":** The RVLM is a **sympathetic
    premotor** region — its clinical syndromes are **named for
    the broader clinical entity** (neurogenic hypertension,
    baroreflex failure, hypertensive crisis) or the **broader
    lesion** (brainstem stroke) — **NOT** for the RVLM itself.

**What is NOT here:** The RVLM is **not** the substrate for
**sympathoinhibition** (CVLM), **respiratory rhythm** (VRG,
DRG), **emesis** (area postrema / CTZ), **somatosensory loss**
(cuneate / gracile nuclei), **tongue weakness** (hypoglossal
nucleus), or **sleep promotion** (parafacial zone). Its clinical
relevance is the **sympathetic premotor** functions listed
above.

Lateralization Notes
--------------------
The rostral ventrolateral medulla is a **bilateral container** in
this tree with ``left`` and ``right`` structural children. There
is **no** ``rostral_ventrolateral_medulla/left/.../`` structural
hierarchy beyond the single leaf level.

*   **Bilateral structural children (ANATOMICAL pairing):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left** or **right** RVLM as a **single structure**. The
    **left** and **right** RVLM are **anatomically separate
    structures** (unlike the **area postrema**, which is a
    **midline** organ wired as left/right by convention). The
    **left** RVLM is in the **left rostral ventrolateral
    medulla**; the **right** RVLM is in the **right rostral
    ventrolateral medulla**.

*   **Bilateral symmetry:** The **left** and **right** RVLM are
    **structurally symmetric mirror pairs** — same
    cytoarchitecture, same projections (with some crossed
    components), same functions.

*   **Ipsilateral vs. contralateral projections:** The **left
    RVLM** projects **primarily** to the **left IML column** (with
    some crossed projections); the **right RVLM** projects
    **primarily** to the **right IML column** (with some crossed
    projections). The **bilateral coordination** of the **two
    RVLM** ensures **sympathetic outflow** is **distributed
    symmetrically** across the **left and right** **sympathetic
    preganglionic neurons** — but each side is **functionally
    active** in its own right.

*   **NO lateralization warning:** The RVLM has **no known
    functional lateralization** in humans — the **left** and
    **right** RVLM are **functionally symmetric** at the
    **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the RVLM — the **left** and
    **right** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The RVLM is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into the RVLM.

*   **NO Fear-Output Warning:** The RVLM is **not** a fear-output
    structure — it is a **sympathetic premotor** center.
    Consumers must **not** conflate it with the **central
    nucleus** or with the **amygdala**.

**A consumer that assumes "left RVLM = right RVLM" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The RVLM
is a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The RVLM is a **bilateral
    container** — it does **not** import from ``left/`` or
    ``right/`` at the container level. The ``left`` and ``right``
    leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../caudal_ventrolateral_medulla/``,
    ``.../solitary_nucleus/``, ``.../arcuate_nucleus/``,
    ``.../parafacial_zone/``,
    ``.../ventral_respiratory_group/``,
    ``.../respiratory_center/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../perihypoglossal_nuclei/``, ``.../cranial_nerve_nuclei/``,
    or any other container. The RVLM's relationships to the CVLM,
    NTS, arcuate nucleus, parafacial zone, VRG, DRG, Gi,
    paramedian reticular nucleus, area postrema, CTZ, cuneate
    nucleus, gracile nucleus, and other medullary structures are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children (ANATOMICAL
    pairing).** The structural children are ``left`` and
    ``right``, each a **leaf**. **Anatomically**, the left and
    right RVLM are **truly separate bilateral structures** — the
    **left / right split** is **ANATOMICAL**, **NOT** a
    **tree-wiring convention**.
*   **SYMPATHETIC PREMOTOR, NOT a respiratory generator, NOT a
    tree-wiring artifact.** The RVLM is a **genuine sympathetic
    premotor / vasomotor** center — **NOT** a respiratory
    nucleus, **NOT** a somatosensory relay, and **NOT** a
    circumventricular organ.
*   **NOT a child of respiratory_center.** The RVLM is a
    **sibling container** of ``respiratory_center`` — **NOT** a
    child of it. Consumers must **not** expect to find the RVLM
    under ``respiratory_center``.
*   **NOT the CVLM.** The **CVLM** is the **caudal**
    ventrolateral medulla — the **sympathoinhibitory** relay. The
    **RVLM** is the **rostral** ventrolateral medulla — the
    **sympathetic premotor** center. This is the **most
    consequential** RVLM boundary.
*   **NOT the NTS.** The **NTS** is the **visceral afferent**
    relay — **NOT** the sympathetic premotor center.
*   **NOT the arcuate nucleus or parafacial zone.** Those are
    **ventral-surface chemosensory** and **sleep-promoting**
    structures, respectively.
*   **NOT the VRG or DRG.** Those are **respiratory** structures
    — **NOT** sympathetic premotor centers.
*   **NOT the Gi or paramedian reticular nucleus.** Those are
    **reticular** nuclei with **broader** functions.
*   **No ``AREA_PATHS`` hop.** The RVLM is a **local container** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The RVLM has no nested
    dual-framing module. It is a **bilateral container** with
    **two leaf children** (anatomical pairing).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **sympathetic premotor**
    framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import rostral_ventrolateral_medulla

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "rostral_ventrolateral_medulla"
    )

**Do not** assume the RVLM is the **CVLM**. The **CVLM** is the
**caudal** ventrolateral medulla — the **sympathoinhibitory**
relay. The **RVLM** is the **rostral** ventrolateral medulla —
the **sympathetic premotor** center.

**Do not** assume the RVLM is the **NTS**. The **NTS** is the
**visceral afferent relay** — **NOT** the sympathetic premotor
center.

**Do not** assume the RVLM is the **arcuate nucleus** or the
**parafacial zone**. Those are **ventral-surface chemosensory**
and **sleep-promoting** structures, respectively.

**Do not** assume the RVLM is the **VRG** or **DRG**. Those are
**respiratory** structures — **NOT** sympathetic premotor
centers.

**Do not** assume the RVLM is the **Gi** or **paramedian
reticular nucleus**. Those are **reticular** nuclei with
**broader** functions.

**Do not** expect to find the RVLM under ``respiratory_center``.
The RVLM is a **sibling container** of ``respiratory_center`` —
**NOT** a child of it.

**Do not** infer **midline wiring convention** from the RVLM
structure. The **left / right split** is **ANATOMICAL** — the
**left** and **right** RVLM are **truly separate bilateral
structures** (unlike the area postrema / CTZ, which are midline
organs wired as left/right by convention).

Iterating the RVLM's structural children (recommended consumer
pattern)::

    ROSTRAL_VENTROLATERAL_MEDULLA_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # RVLM. Anatomically, the left and right RVLM are TRULY
    # SEPARATE bilateral structures — the left/right split is
    # ANATOMICAL, NOT a wiring convention.

Reaching the left and right RVLM leaves (recommended consumer
pattern)::

    # The left and right RVLM leaves are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #
    # Each is a leaf module representing the RVLM of that side.
    # Anatomically, they are TRULY SEPARATE bilateral structures.

Reaching the CVLM (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The caudal ventrolateral medulla is a SEPARATE container
    # under medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #
    # The RVLM and the CVLM are DIFFERENT STRUCTURES at DIFFERENT
    # rostrocaudal levels — the RVLM drives sympathetic outflow;
    # the CVLM inhibits it. They form the medullary baroreflex arc
    # (NTS -> CVLM -> RVLM -> IML column).

Reaching the NTS (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The solitary nucleus is a SEPARATE container under
    # medulla_oblongata:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # The NTS is the VISCERAL AFFERENT relay — it PROJECTS TO the
    # RVLM (directly and via the CVLM), but is NOT the RVLM.

Reaching the VRG and DRG (recommended consumer pattern — NOTE
the DIFFERENT containers)::

    # The ventral respiratory group and the dorsal respiratory
    # group are RESPIRATORY structures — SEPARATE containers:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group
    #
    # They are NOT sympathetic premotor centers — they are
    # respiratory rhythm and pattern generators.

Reaching the arcuate nucleus and parafacial zone (recommended
consumer pattern — NOTE the DIFFERENT containers)::

    # The arcuate nucleus and the parafacial zone are VENTRAL-
    # SURFACE CHEMOSENSORY and SLEEP-PROMOTING structures —
    # SEPARATE containers:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.arcuate_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone
    #
    # They are NOT sympathetic premotor centers.

Reaching the Gi and paramedian reticular nucleus (recommended
consumer pattern — NOTE the DIFFERENT containers)::

    # The gigantocellular reticular nucleus and the paramedian
    # reticular nucleus are RETICULAR nuclei — in DIFFERENT
    # containers:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gigantocellular_reticular_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.paramedian_reticular_nucleus
    #
    # They are NOT sympathetic premotor centers — they are
    # reticular nuclei with broader functions.

Reaching the respiratory_center (recommended consumer pattern —
NOTE the SIBLING container)::

    # The respiratory center is a SIBLING container of the RVLM
    # under medulla_oblongata — NOT a parent of the RVLM:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center
    #
    # Consumers must NOT expect to find the RVLM under
    # respiratory_center — resolve it via
    # rostral_ventrolateral_medulla.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"rostral_ventrolateral_medulla.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: the left and right RVLM are TRULY SEPARATE
        # bilateral structures (ANATOMICAL, not a wiring
        # convention).

References
----------
*   **Canonical RVLM anatomy and function:** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure." *Nature
    Reviews Neuroscience* 7:335–346. (RVLM; sympathetic premotor
    neurons; baroreflex; tonic sympathetic drive; neurogenic
    hypertension.)
*   **RVLM — baroreflex arc:** Dampney, R.A.L. (1994).
    "Functional organization of central pathways regulating the
    cardiovascular system." *Physiological Reviews* 74:323–364.
    (RVLM; NTS; CVLM; baroreflex arc; sympathetic premotor
    organization.)
*   **RVLM — C1 neurons:** Ross, C.A., et al. (1984). "Adrenaline
    neurons in the rostral ventrolateral medulla: a major
    substrate for tonic and reflex sympathetic vasomotor
    tone." *Journal of the Autonomic Nervous System* 11:1–15.
    (RVLM; C1 catecholaminergic neurons; sympathetic vasomotor
    tone.)
*   **RVLM — C1 neurons and vasomotor control:** Schreihofer,
    A.M., Guyenet, P.G. (2000). "Role of the ventrolateral
    medulla in sympathoinhibition." *American Journal of
    Physiology* 279:R1701–R1711. (RVLM; CVLM;
    sympathoinhibition; baroreflex.)
*   **RVLM — clonidine and moxonidine:** Ernsberger, P., et al.
    (1990). "Role of imidazole receptors in the vasodepressor
    response to clonidine and related agents." *Journal of
    Clinical Investigation* 85:1074–1083. (RVLM; imidazoline
    receptors; clonidine; moxonidine; centrally acting
    antihypertensives.)
*   **RVLM — hypertension:** Guyenet, P.G. (2006). "The
    sympathetic control of blood pressure." *Nature Reviews
    Neuroscience* 7:335–346. (RVLM overactivity; neurogenic
    hypertension; sympathetic overactivity.)
*   **RVLM — baroreflex failure:** Robertson, D., et al. (1993).
    "Baroreflex failure: a new syndrome of hypertension and
    hypotension." *Hypertension* 21:496–501. (Baroreflex
    failure; autonomic instability.)
*   **RVLM — brainstem stroke:** Sacco, R.L., et al. (1993).
    "Lateral medullary infarction: clinical and MRI correlation."
    *Stroke* 24:1981–1987. (Wallenberg syndrome; RVLM
    involvement; autonomic instability.)
*   **RVLM — central sleep apnea:** Dempsey, J.A., et al. (2010).
    "Pathophysiology of sleep apnea." *Physiological Reviews*
    90:47–112. (Central sleep apnea; brainstem autonomic and
    respiratory integration; RVLM.)
*   **RVLM — autonomic dysreflexia:** Krassioukov, A., et al.
    (2003). "A systematic review of the management of autonomic
    dysreflexia after spinal cord injury." *Archives of Physical
    Medicine and Rehabilitation* 90:682–695. (Autonomic
    dysreflexia; sympathetic storm; RVLM overactivity.)
*   **CVLM (contrast — sympathoinhibitory):** Schreihofer, A.M.,
    Guyenet, P.G. (2000). "Role of the ventrolateral medulla in
    sympathoinhibition." *American Journal of Physiology*
    279:R1701–R1711. (CVLM — sympathoinhibitory relay, DIFFERENT
    from the RVLM.)
*   **NTS (contrast — visceral afferent):** Andresen, M.C.,
    Kunze, D.L. (1994). "Nucleus tractus solitarius — gateway
    to neural circulatory control." *Annual Review of
    Physiology* 56:93–116. (NTS — visceral afferent relay,
    DIFFERENT from the RVLM.)
*   **VRG and DRG (contrast — respiratory generators):** Feldman,
    J.L., Del Negro, C.A. (2006). "Looking for inspiration: new
    perspectives on respiratory rhythm." *Nature Reviews
    Neuroscience* 7:232–242. (VRG and DRG — respiratory
    generators, DIFFERENT from the RVLM.)
*   NeuroNames — Rostral ventrolateral medulla; FMA — Rostral
    ventrolateral medulla.
"""