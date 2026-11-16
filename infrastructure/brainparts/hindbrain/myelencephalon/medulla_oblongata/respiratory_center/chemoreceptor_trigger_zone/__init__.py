"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone
=================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── chemoreceptor_trigger_zone   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Chemoreceptor trigger zone; CTZ; the CTZ; the
emetic chemoreceptor trigger zone; the area postrema's functional
role.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**circumventricular organ's functional role** — in **this tree**,
the **chemoreceptor trigger zone** is wired as a **separate child
container** of ``respiratory_center`` from the **area postrema**
container, **even though the two names refer to the same physical
structure** in the **literature**. The **CTZ** is the **functional
role** (chemoreception / emetic trigger); the **area postrema**
is the **anatomical structure**. **Anatomically**, the **CTZ is
the area postrema** — the two names refer to **the same midline
circumventricular organ** from **two different perspectives**
(anatomical vs. functional). The **tree separates them into two
modules** as a **deliberate wiring choice** — **NOT** an
anatomical claim that they are **two different structures**.
**Part of:** The **respiratory_center** container
(``.../respiratory_center/``) — which is part of the **medulla
oblongata** — the **caudal brainstem** subdivision of the
**myelencephalon**.
**Structural parent:** ``.../respiratory_center/`` → **direct
child** of the respiratory_center container.
**Structural children:** **Two —** ``left`` and ``right`` — each a
**leaf** representing the **left** or **right** aspect of the
chemoreceptor trigger zone. The bilateral CTZ is the **structural
children** of this **bilateral container**; the container itself
is **unpaired**. **Anatomically**, the human chemoreceptor
trigger zone (the area postrema's functional role) is a
**single, unpaired, midline** structure — the **left / right
split** is a **tree-wiring convention**, **NOT** an anatomical
claim that there are two separate CTZs.
**Boundary status (NOT the area postrema — the SAME structure
under a DIFFERENT name in the literature, wired as a SEPARATE
child in this tree):** **Boundary case — the chemoreceptor
trigger zone is NOT the area postrema in this tree.** In the
**literature**, the **chemoreceptor trigger zone** and the
**area postrema** are **often used interchangeably** — they are
**largely considered the same structure** — the **CTZ** is the
**functional role** of the **area postrema** for
**blood-borne / CSF-borne emetic detection**. **In this tree**,
however, they are **wired as two separate child containers** of
``respiratory_center``:
``respiratory_center.chemoreceptor_trigger_zone`` (this module)
and ``respiratory_center.area_postrema``. **Consumers must not
conflate the two modules within the tree** — resolve the
**area postrema** via
``respiratory_center.area_postrema``. **Consumers must also not
conclude** that **wiring separation** implies **anatomical
separation** — the **underlying structure** is **one**. The
**tree separates** the **two names** into **two modules** as a
**deliberate wiring choice** — the **CTZ** is the **functional
role**; the **area postrema** is the **anatomical structure**;
both refer to the **same midline circumventricular organ**.
**Boundary status (NOT the left chemoreceptor trigger zone leaf —
a DIFFERENT child of the chemoreceptor_trigger_zone container):**
**Boundary case — the chemoreceptor trigger zone container is
NOT the left chemoreceptor trigger zone leaf.** The **left
chemoreceptor trigger zone**
(``.../chemoreceptor_trigger_zone/left/``) is the **left-side
aspect** of the CTZ — it is a **leaf child** of this container.
The **chemoreceptor_trigger_zone** module (here) is the
**bilateral container** that **contains** the left CTZ **plus**
the right CTZ. Consumers must **not** conflate the **container**
with the **leaf**.
**Boundary status (NOT the right chemoreceptor trigger zone —
the contralateral leaf):** **Boundary case — the
chemoreceptor_trigger_zone container is NOT the right
chemoreceptor trigger zone leaf.** The **right chemoreceptor
trigger zone**
(``.../chemoreceptor_trigger_zone/right/``) is the **right-side
aspect** of the CTZ — the **contralateral leaf**. Consumers must
**not** conflate the **container** with the **leaf**.
**Boundary status (NOT the solitary nucleus (NTS) — the NTS is
the primary projection target of the CTZ):** **Boundary case —
the chemoreceptor trigger zone is NOT the solitary nucleus
(NTS).** The **solitary nucleus** (``.../solitary_nucleus/``) is
the **visceral afferent relay** — it is a **separate container**
under ``medulla_oblongata``. The **chemoreceptor trigger zone**
(here) is a **circumventricular organ's functional role** that
**projects to** the NTS — the NTS is the **downstream target**
of the CTZ's **emetic and autonomic** signals. **They are
DIFFERENT STRUCTURES** — the **CTZ / AP** is the **sensor**; the
**NTS** is the **relay**. Consumers must **not** conflate the
two.
**Boundary status (NOT the dorsal motor nucleus of the vagus —
a DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the chemoreceptor trigger zone is NOT the dorsal motor
nucleus of the vagus.** The **dorsal motor nucleus of the vagus**
(``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``
and
``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
is the **parasympathetic** nucleus for the **thoracic and
abdominal viscera**. The **chemoreceptor trigger zone** (here)
is a **circumventricular organ's functional role** — **NOT** a
parasympathetic nucleus. They are **anatomically adjacent** at
the **caudal fourth ventricle floor**, but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the hypoglossal nucleus — a DIFFERENT
structure with a DIFFERENT function):** **Boundary case — the
chemoreceptor trigger zone is NOT the hypoglossal nucleus.** The
**hypoglossal nucleus**
(``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/`` and
``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is the
**somatic motor** nucleus for the **tongue**. The
**chemoreceptor trigger zone** (here) is a **circumventricular
organ's functional role** — **NOT** a motor nucleus. They are
**anatomically adjacent** at the **caudal fourth ventricle
floor**, but they are **functionally distinct**. Consumers must
**not** conflate the two.
**Boundary status (NOT the dorsal respiratory group — a
DIFFERENT child of respiratory_center):** **Boundary case — the
chemoreceptor trigger zone is NOT the dorsal respiratory group
(DRG).** The **dorsal respiratory group**
(``.../respiratory_center/dorsal_respiratory_group/``) is the
**dorsal respiratory** pattern generator — **NOT** a
circumventricular structure. Both are **children** of
``respiratory_center``, but they are **functionally distinct** —
the **DRG** is **respiratory**; the **CTZ** is
**circumventricular / chemosensory**. Consumers must **not**
conflate the two.
**Boundary status (NOT the dorsal column nuclei — cuneate and
gracile — DIFFERENT children of respiratory_center):**
**Boundary case — the chemoreceptor trigger zone is NOT the
cuneate or gracile nucleus.** The **cuneate** and **gracile
nuclei** (``.../respiratory_center/cuneate_nucleus/`` and
``.../respiratory_center/gracile_nucleus/``) are the **dorsal
column somatosensory relays**. The **chemoreceptor trigger
zone** (here) is a **circumventricular organ's functional
role**. All three are **children** of ``respiratory_center``,
but they are **functionally distinct**. Consumers must **not**
conflate them.
**Boundary status (NOT the gigantocellular reticular nucleus —
a DIFFERENT child of respiratory_center):** **Boundary case —
the chemoreceptor trigger zone is NOT the gigantocellular
reticular nucleus (Gi).** The **gigantocellular reticular
nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/``)
is a **large medullary reticular** nucleus. The **chemoreceptor
trigger zone** (here) is a **circumventricular organ's
functional role**. Both are **children** of
``respiratory_center``, but they are **functionally distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the fourth ventricle — the fourth
ventricle is a CSF cavity, the CTZ is a CSF-sensing functional
role at its floor):** **Boundary case — the chemoreceptor
trigger zone is NOT the fourth ventricle.** The **fourth
ventricle** (``.../metencephalon/fourth_ventricle/``) is a **CSF
cavity** — **NOT** a grey-matter structure. The
**chemoreceptor trigger zone** (here) is a **functional role**
of the **organ** that **lines the caudal fourth ventricle
floor**. Consumers must **not** conflate the **functional role**
with the **cavity**.
**Boundary status (NOT the whole respiratory_center — a CHILD of
it):** **Boundary case — the chemoreceptor trigger zone is NOT
the whole respiratory_center.** The **respiratory_center**
(``.../respiratory_center/``) is the **parent container** — it
contains the **chemoreceptor trigger zone** (here) **plus** the
``area_postrema``, ``cuneate_nucleus``,
``dorsal_respiratory_group``,
``gigantocellular_reticular_nucleus``, and ``gracile_nucleus``.
The **chemoreceptor trigger zone** is **one child** of that
container. Consumers must **not** conflate the **child** with
the **whole container**.
**Boundary status (NOT the whole medulla oblongata — a small
circumventricular structure's functional role within it):**
**Boundary case — the chemoreceptor trigger zone is NOT the
whole medulla oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the chemoreceptor trigger zone (via the
respiratory_center) **plus** the cranial nerve nuclei, the
autonomic nuclei, the olivary body, the medullary pyramid, the
arcuate nucleus, the parafacial zone, the paramedian reticular
nucleus, the perihypoglossal nuclei, the respiratory_center, and
other structures. The **chemoreceptor trigger zone** is **one
small circumventricular structure's functional role** within the
medulla. Consumers must **not** conflate the **CTZ** with the
**whole medulla**.
**Boundary status (BILATERAL container — left and right are
structural children, but the CTZ is ANATOMICALLY MIDLINE):**
**Boundary case — the chemoreceptor trigger zone is a BILATERAL
container in this tree, but it is ANATOMICALLY MIDLINE in the
human brain.** The **chemoreceptor_trigger_zone** module (here)
is an **unpaired container**; its **structural children** are
``left`` and ``right`` — each a **leaf** representing the **left**
or **right** aspect of the CTZ. **Anatomically**, the human CTZ
(the area postrema's functional role) is a **single, unpaired,
midline** structure — the ``left`` and ``right`` children in this
tree are a **wiring convention** (consistent with the rest of the
medulla oblongata children), **NOT** an anatomical claim that
there are **two separate CTZs**. Consumers must **not** infer
that the human CTZ is **bilateral / paired** from the tree
structure.

Overview
--------
The **chemoreceptor trigger zone (CTZ)** is, **in this tree**, a
**separate child container** of ``respiratory_center`` — wired
**alongside** the ``area_postrema`` container, even though
**anatomically** the **CTZ is the area postrema**. The **two
names** refer to the **same midline circumventricular organ**
from **two different perspectives**:
*   **Area postrema** — the **anatomical structure**.
*   **Chemoreceptor trigger zone** — the **functional role**
    (chemoreception / emetic trigger).

**The tree separates the two names into two modules as a
deliberate wiring choice** — **NOT** an anatomical claim that
they are **two different structures**. Consumers must **not
conflate the two modules within the tree** — resolve the
**area postrema** via ``respiratory_center.area_postrema`` and
the **chemoreceptor trigger zone** via
``respiratory_center.chemoreceptor_trigger_zone``. **Consumers
must also not conclude** that **wiring separation** implies
**anatomical separation** — the **underlying structure** is
**one**.

**The CTZ is a CIRCUMVENTRICULAR ORGAN's functional role, NOT a
respiratory nucleus.** Although wired under ``respiratory_center``,
its **primary function** is **chemoreception / emesis /
autonomic regulation** — **NOT** **breathing**. The
**"respiratory_center"** label is a **tree-wiring artifact** —
the tree groups the CTZ (and the area postrema, and the
dorsal column nuclei) as a **pragmatic cluster**. Consumers must
**not** infer **respiratory function** from **container
membership**.

**The CTZ is ANATOMICALLY MIDLINE — the tree's ``left`` /
``right`` split is a WIRING CONVENTION.** The human CTZ (the
area postrema's functional role) is a **single, unpaired,
midline** circumventricular organ at the **caudal floor** of the
fourth ventricle. The tree represents it as a **bilateral
container** with ``left`` and ``right`` leaf children —
**consistent with the wiring pattern** of the other medulla
oblongata children — but **NOT** an anatomical claim that the
CTZ is **paired**.

**The CTZ is functionally coupled to the solitary nucleus (NTS),
the parabrachial nucleus, the dorsal motor nucleus of the vagus,
and the hypothalamic autonomic centers.** It **projects** to the
**NTS** (the primary target), the **parabrachial nucleus** (for
**visceral / autonomic** integration), and the **hypothalamus**
(for **fluid balance**, **cardiovascular regulation**, and
**neuroendocrine** responses). It is **functionally coupled** to
these structures but **NOT** identical to any of them.

Bilateral Structure (Wiring Convention)
---------------------------------------
The chemoreceptor trigger zone is a **bilateral container** in
this tree with **two structural children**:

*   ``left`` — the **left** aspect of the CTZ (a **leaf** module).
*   ``right`` — the **right** aspect of the CTZ (a **leaf**
    module).

**The two children are a WIRING CONVENTION, NOT an anatomical
claim.** The human CTZ (the area postrema's functional role) is a
**single, unpaired, midline** circumplex organ — the ``left`` and
``right`` leaves do **not** represent **two separate CTZs**. They
are **wired** as **left / right leaves** to **maintain
consistency** with the rest of the medulla oblongata children.

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **aspects** of the **midline CTZ** as **single
structures**, **NOT** two separate functional roles. Consumers
that need **side-specific** resolution should descend into
``left`` or ``right``; consumers that need **the whole functional
role** should use ``chemoreceptor_trigger_zone`` (the container)
as a whole.

**The container itself is unpaired.** There is **no**
``chemoreceptor_trigger_zone/left/.../`` structural hierarchy
beyond the single leaf level — the ``left`` and ``right`` modules
are the **terminal modules** for this structure.

The Chemoreceptor Trigger Zone / Area Postrema Boundary
-------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Chemoreceptor trigger zone (CTZ)** (this module) — the
    **functional role** of the circumventricular organ
    (chemoreception / emetic trigger).

*   **Area postrema (AP)**
    (``.../respiratory_center/area_postrema/``) — the
    **anatomical structure**.

**They refer to the SAME PHYSICAL STRUCTURE in the literature**
— the **CTZ** is the **functional role**; the **AP** is the
**anatomical structure**. **The tree separates the two names into
two modules as a deliberate wiring choice.** Consumers must
**not** conflate the two modules **within the tree** — resolve
the **AP** via ``respiratory_center.area_postrema`` and the
**CTZ** via ``respiratory_center.chemoreceptor_trigger_zone``.
**Consumers must also not conclude** that **wiring separation**
implies **anatomical separation** — the **underlying structure**
is **one**.

The Chemoreceptor Trigger Zone / Solitary Nucleus Boundary
----------------------------------------------------------
This is the **sensor / relay** boundary:

*   **Chemoreceptor trigger zone** (this module) — the
    **circumventricular chemosensory** functional role.

*   **Solitary nucleus (NTS)** (``.../solitary_nucleus/``) — the
    **visceral afferent relay**.

**The CTZ PROJECTS TO the NTS** — the NTS is the **downstream
target** of the CTZ's **emetic and autonomic** signals. **They
are DIFFERENT STRUCTURES** — the **CTZ / AP** is the **sensor**;
the **NTS** is the **relay**. Consumers must **not** conflate the
two.

The Chemoreceptor Trigger Zone / Dorsal Motor Nucleus of the Vagus and Hypoglossal Nucleus Boundary
---------------------------------------------------------------------------------------------------
This is the **circumventricular / motor** boundary:

*   **Chemoreceptor trigger zone** (this module) — the
    **circumventricular organ's functional role**.

*   **Dorsal motor nucleus of the vagus**
    (``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``
    and
    ``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
    — the **parasympathetic** nucleus.

*   **Hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/`` and
    ``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES** — the **CTZ** is a
**circumventricular functional role**; the **dorsal motor nucleus
of the vagus** and the **hypoglossal nucleus** are **motor
nuclei**. Consumers must **not** conflate the two.

The Chemoreceptor Trigger Zone / Other Respiratory Center Children Boundary
---------------------------------------------------------------------------
This is the **circumventricular / respiratory-and-somatosensory**
boundary:

*   **Chemoreceptor trigger zone** (this module) — the
    **circumventricular organ's functional role**.

*   **Dorsal respiratory group**
    (``.../dorsal_respiratory_group/``) — the **dorsal
    respiratory** pattern generator.

*   **Gigantocellular reticular nucleus**
    (``.../gigantocellular_reticular_nucleus/``) — the **large
    medullary reticular** nucleus.

*   **Cuneate nucleus** (``.../cuneate_nucleus/``) — the **dorsal
    column somatosensory** relay (upper body).

*   **Gracile nucleus** (``.../gracile_nucleus/``) — the **dorsal
    column somatosensory** relay (lower body).

**They are DIFFERENT STRUCTURES** — all six are **children** of
``respiratory_center``, but they are **functionally distinct**.
Consumers must **not** conflate the **CTZ** with any of these.

The Chemoreceptor Trigger Zone / Fourth Ventricle Boundary
----------------------------------------------------------
This is the **functional role / cavity** boundary:

*   **Chemoreceptor trigger zone** (this module) — the
    **circumventricular organ's functional role** that **lines
    the floor** of the **caudal fourth ventricle**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the **CSF
    cavity**.

**The CTZ is at the FLOOR of the fourth ventricle** — but it is
**NOT** the fourth ventricle itself. Consumers must **not**
conflate the **functional role** with the **cavity**.

The Chemoreceptor Trigger Zone / Whole Respiratory Center and Whole Medulla Oblongata Boundary
----------------------------------------------------------------------------------------------
This is the **child / container** boundary:

*   **Chemoreceptor trigger zone** (this module) — one **child**
    of ``respiratory_center``.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children**.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The CTZ is a CHILD of respiratory_center, NOT the container
itself, and NOT the whole medulla.** Consumers must **not**
conflate the **child** with either **parent container**.

Function in the Human Brain
---------------------------
The chemoreceptor trigger zone's functions are **chemoreception**,
**emesis**, **autonomic regulation**, **fluid balance**, and
**immune-neural signaling** — **NOT respiratory rhythm** and
**NOT motor control** — and are **identical to the area
postrema's functional profile** (because the CTZ **is** the area
postrema's functional role):

*   **Chemoreception (blood-borne and CSF-borne signals):** The
    **CTZ** — the **functional role** of the **area postrema** —
    **senses blood-borne and CSF-borne substances** (toxins,
    emetics, hormones, cytokines) via the **fenestrated
    capillaries** and **CSF-facing surface** of the **area
    postrema**. It is the **primary chemosensory functional
    role** of the **caudal brainstem**.

*   **Vomiting reflex (emesis):** The **CTZ** is the **primary
    chemoreceptor trigger** for the **vomiting reflex** — it
    **detects** **emetic substances** (e.g., **apomorphine**,
    **chemotherapy agents**, **toxins**) and **triggers**
    **nausea and vomiting** via **projections** to the **NTS**
    and other **emetic centers**.

*   **Autonomic regulation (cardiovascular and
    gastrointestinal):** The **CTZ** **participates** in
    **cardiovascular regulation** and **gastrointestinal
    regulation** via **projections** to the **NTS** and
    **hypothalamus**.

*   **Fluid and electrolyte balance:** The **CTZ** **senses**
    **plasma osmolality** and **angiotensin II** —
    **contributing** to **thirst**, **salt appetite**, and
    **vasopressin** release.

*   **Immune-neural signaling:** The **CTZ** **senses**
    **cytokines** and **bacterial endotoxin** (LPS) — it is a
    **site of immune-to-brain signaling** contributing to
    **sickness behavior**, **fever**, and **anorexia**.

*   **Conditioned taste aversion:** The **CTZ** is **required**
    for **conditioned taste aversion**.

*   **NOT respiratory rhythm:** The **CTZ** does **not** generate
    the **respiratory rhythm** — that is the **pre-Bötzinger
    complex** (VRG) and the **respiratory** centers.

*   **NOT motor control:** The **CTZ** does **not** send motor
    axons to muscles.

**The unifying theme:** the chemoreceptor trigger zone is the
**functional role** of the **area postrema** — a **circumventricular
chemosensory** functional role at the **caudal fourth ventricle
floor** — a **chemosensory**, **emetic**, **autonomic**,
**fluid-balance**, and **immune-neural** functional role —
**NOT** a respiratory nucleus, **NOT** the NTS, **NOT** the
dorsal motor nucleus of the vagus, and **NOT** the fourth
ventricle.

Associated Disorders
--------------------
The chemoreceptor trigger zone's clinical relevance is
**identical** to the **area postrema's** — the **CTZ** is the
**functional role** of the **area postrema**, so the **clinical
syndromes** are **not lateralized** and are **resolved by the
area postrema**:

*   **Chemotherapy-induced nausea and vomiting (CINV — via CTZ /
    AP):** **Chemotherapy agents** **stimulate** the **CTZ**
    (the **area postrema's** functional role) — triggering
    **nausea** and **vomiting** via **NTS** and **parabrachial**
    projections. **5-HT3 receptor antagonists** (e.g.,
    **ondansetron**) and **NK1 receptor antagonists** (e.g.,
    **aprepitant**) **target** the **CTZ / NTS** pathway to
    **prevent** **CINV**.

*   **Area postrema syndrome (APS — in neuromyelitis optica
    spectrum disorder, NMOSD):** **NMOSD** — an **autoimmune**
    disorder targeting **aquaporin-4 (AQP4)** — **frequently**
    involves the **area postrema** (a **high-AQP4** site),
    causing **intractable nausea**, **vomiting**, and **hiccups**
    — the **CTZ's functional role** is the **direct substrate**
    of these **emetic** symptoms.

*   **Cyclic vomiting syndrome (CVS — hypothesized CTZ / AP
    involvement):** **CVS** is a **disorder** of **recurrent
    episodes** of **severe nausea and vomiting** —
    **hypothesized** to involve **CTZ / AP** and
    **mitochondrial** dysfunction.

*   **Bulimia nervosa and eating disorders (hypothesized CTZ /
    AP involvement):** **Impaired** **CTZ / AP-mediated**
    **satiety** and **emetic** signaling have been
    **hypothesized** to **contribute** to **bulimia nervosa**
    and **binge-eating disorder**.

*   **Drug-induced emesis (via CTZ / AP):** **Many** drugs
    (**opioids**, **digoxin**, **apomorphine**, **nicotine**)
    **stimulate** the **CTZ** — triggering **nausea** and
    **vomiting**.

*   **Sickness behavior and fever (via CTZ / AP immune-neural
    signaling):** The **CTZ** **senses** **cytokines** and
    **LPS** — **contributing** to **fever**, **anorexia**,
    **lethargy**, and **sickness behavior** during **infection**
    and **inflammation**.

*   **No Named "Chemoreceptor Trigger Zone Syndrome":** The CTZ
    is the **functional role** of the **area postrema** — its
    **clinical syndromes** are **named for the area postrema**
    (e.g., **area postrema syndrome** in NMOSD) or **for the
    function** (CINV, drug-induced emesis), **not** for the CTZ
    itself.

**What is NOT here:** The chemoreceptor trigger zone is **not**
the substrate for **central hypoventilation** (VRG,
pre-Bötzinger complex), **sympathetic premotor** function
(RVLM), **visceral afferent relay** (NTS), **tongue weakness**
(hypoglossal nucleus), or **parasympathetic dysfunction**
(dorsal motor nucleus of the vagus). Its clinical relevance is
the **emesis**, **autonomic**, and **immune-neural** functions
listed above.

Lateralization Notes
--------------------
The chemoreceptor trigger zone is a **bilateral container** in
this tree with ``left`` and ``right`` structural children. There
is **no** ``chemoreceptor_trigger_zone/left/.../`` structural
hierarchy beyond the single leaf level.

*   **Bilateral structural children (wiring convention):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left-side** or **right-side** **aspects** of the
    **midline CTZ** as a **single structure**. The **anatomical
    CTZ** (the area postrema's functional role) is a **single,
    unpaired, midline** structure — the **left / right split**
    is a **tree-wiring convention**.

*   **NO lateralization:** The CTZ has **no known functional
    lateralization** — it is a **midline** functional role with
    **no left / right functional difference**. Consumers must
    **not** import a **lateralization warning** into the CTZ —
    the **left** and **right** sides are **functionally
    identical** and **anatomically the same** functional role.

*   **NO Extended-Amygdala / SLEA Warning:** The CTZ is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the CTZ.

*   **NO Fear-Output Warning:** The CTZ is **not** a fear-output
    structure — it is a **circumventricular chemosensory**
    functional role. Consumers must **not** conflate it with the
    **central nucleus** or with the **amygdala**.

**A consumer that assumes "left CTZ = right CTZ" will be
structurally correct** — the two sides are **equivalent** (they
represent the **same midline** structure). The CTZ is a
**strict-mirror container with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The CTZ is a **bilateral
    container** — it does **not** import from ``left/`` or
    ``right/`` at the container level. The ``left`` and
    ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../area_postrema/``,
    ``.../dorsal_respiratory_group/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../metencephalon/fourth_ventricle/``, or any other
    container. The CTZ's relationships to the area postrema,
    dorsal respiratory group, gigantocellular reticular nucleus,
    cuneate nucleus, gracile nucleus, solitary nucleus, dorsal
    motor nucleus of the vagus, hypoglossal nucleus, and fourth
    ventricle are documented as **prose and boundary data**, not
    as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children (wiring
    convention).** The structural children are ``left`` and
    ``right``, each a **leaf**. **Anatomically**, the human CTZ
    (the area postrema's functional role) is a **single midline
    structure** — the **left / right split** is a **tree-wiring
    convention**, **NOT** an anatomical claim of two separate
    CTZs.
*   **FUNCTIONAL ROLE, NOT an anatomical structure.** The CTZ is
    the **functional role** of the **area postrema** — the
    **two names** refer to the **same physical structure** from
    **two different perspectives**. The **tree separates the two
    names into two modules** as a **deliberate wiring choice** —
    consumers must **not** conflate the **modules within the
    tree**, **and must not conclude** that **wiring separation**
    implies **anatomical separation**.
*   **CIRCUMVENTRICULAR ORGAN's functional role, NOT a
    respiratory nucleus.** Although wired under
    ``respiratory_center``, the CTZ is a **chemoreceptive /
    emetic / autonomic / immune-neural** functional role —
    **NOT** a respiratory rhythm generator.
*   **NOT the area postrema (in this tree — the same structure
    under a different name, wired as a separate child).** The
    **area postrema** is a **separate child** of
    ``respiratory_center`` — consumers must **not** conflate the
    two modules **within the tree**, even though they refer to
    the **same physical structure** in the literature.
*   **NOT the solitary nucleus (NTS).** The **NTS** is a
    **separate container** — the **CTZ / AP projects to** the
    **NTS**, but is **NOT** the NTS itself.
*   **NOT the dorsal motor nucleus of the vagus, hypoglossal
    nucleus, dorsal respiratory group, gigantocellular reticular
    nucleus, cuneate nucleus, or gracile nucleus.** Each is a
    **different structure** — see the respective modules.
*   **NOT the fourth ventricle.** The fourth ventricle is a
    **CSF cavity**; the CTZ is the **functional role** of the
    **organ** that **lines its caudal floor**.
*   **NOT the whole respiratory_center or whole medulla
    oblongata.** The CTZ is a **child** of
    ``respiratory_center``, not the container itself.
*   **No ``AREA_PATHS`` hop.** The CTZ is a **local container** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The CTZ has no nested
    dual-framing module. It is a **bilateral container** with
    **two leaf children** (wiring convention).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **circumventricular
    functional role** framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center import chemoreceptor_trigger_zone

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.chemoreceptor_trigger_zone"
    )

**Do not** assume the chemoreceptor trigger zone is the **area
postrema** in this tree. They are **separate children** of
``respiratory_center`` — resolve the **area postrema** via
``respiratory_center.area_postrema`` and the **CTZ** via
``respiratory_center.chemoreceptor_trigger_zone``. **Consumers
must not conclude** that **wiring separation** implies
**anatomical separation** — the **underlying structure** is
**one**.

**Do not** assume the CTZ is the **solitary nucleus (NTS)**. The
NTS is a **separate container** — the CTZ **projects to** the
NTS, but is **NOT** the NTS itself.

**Do not** assume the CTZ is the **dorsal motor nucleus of the
vagus**, the **hypoglossal nucleus**, the **dorsal respiratory
group**, the **gigantocellular reticular nucleus**, the
**cuneate nucleus**, or the **gracile nucleus**. Each is a
**different structure**.

**Do not** assume the CTZ is the **fourth ventricle**. The
fourth ventricle is a **CSF cavity**; the CTZ is the
**functional role** of the **organ** at its **caudal floor**.

**Do not** assume the CTZ is the **whole respiratory_center** or
the **whole medulla oblongata**. It is a **child** of
``respiratory_center``.

**Do not** assume the human CTZ is **bilateral / paired** from
the tree structure. **Anatomically**, it is a **single,
unpaired, midline** functional role — the ``left`` / ``right``
split is a **tree-wiring convention**.

Iterating the CTZ's structural children (recommended consumer
pattern)::

    CHEMORECEPTOR_TRIGGER_ZONE_CHILDREN = ("left", "right")
    # Each child is a leaf module representing an aspect of the
    # MIDLINE CTZ. Anatomically, the CTZ (the functional role of
    # the area postrema) is a SINGLE midline structure — the
    # left/right split is a tree-wiring convention, NOT an
    # anatomical claim of two separate CTZs.

Reaching the left and right CTZ leaves (recommended consumer
pattern)::

    # The left and right CTZ leaves are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.right
    #
    # Each is a leaf module representing an ASPECT of the MIDLINE
    # CTZ. Anatomically, there is ONE CTZ (the functional role of
    # the area postrema) — the left/right split is a tree-wiring
    # convention.

Reaching the area postrema (recommended consumer pattern — NOTE
the SAME STRUCTURE under a DIFFERENT NAME, wired as a separate
child in this tree)::

    # The area postrema is a SEPARATE child of respiratory_center
    # in this tree — even though the literature often treats it
    # as synonymous with the CTZ:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema
    #
    # The AP is the ANATOMICAL STRUCTURE; the CTZ is the
    # FUNCTIONAL ROLE — the tree separates them into TWO MODULES
    # as a deliberate wiring choice. Consumers must NOT conflate
    # the two modules within the tree, AND must NOT conclude that
    # wiring separation implies anatomical separation — the
    # underlying structure is ONE.

Reaching the solitary nucleus (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The solitary nucleus (NTS) is a SEPARATE container under
    # medulla_oblongata — the CTZ PROJECTS to the NTS, but is
    # NOT the NTS itself:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # The CTZ / AP is the CHEMOSENSORY functional role; the NTS
    # is the VISCERAL AFFERENT relay.

Reaching the dorsal motor nucleus of the vagus and hypoglossal
nucleus (recommended consumer pattern — NOTE the DIFFERENT
containers)::

    # The dorsal motor nucleus of the vagus and the hypoglossal
    # nucleus are cranial nerve MOTOR nuclei — SEPARATE
    # containers:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.dorsal_motor_nucleus_vagus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.hypoglossal_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.dorsal_motor_nucleus_vagus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.hypoglossal_nucleus
    #
    # They are NOT part of the CTZ — they are functionally
    # distinct motor nuclei.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The fourth ventricle is a CSF cavity in the METENCEPHALON:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The CTZ / AP LINES the caudal floor of the fourth ventricle
    # — but it is NOT the ventricle itself.

Bilateral iteration (recommended consumer pattern — with the
caveat that the CTZ is anatomically midline)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"respiratory_center.chemoreceptor_trigger_zone.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: left and right represent aspects of the SAME
        # midline structure, NOT two separate CTZs.

References
----------
*   **Chemoreceptor trigger zone — canonical:** Borison, H.L.,
    Brizzee, K.R. (1951). "Morphology of emetic chemoreceptor
    trigger zone in cat medulla oblongata." *Proceedings of the
    Society for Experimental Biology and Medicine* 77:38–42.
    (Chemoreceptor trigger zone; the functional role of the area
    postrema; emetic reflex; often used interchangeably with the
    area postrema in the literature.)
*   **Chemoreceptor trigger zone — emesis:** Borison, H.L., Wang,
    S.C. (1953). "Physiology and pharmacology of vomiting."
    *Pharmacological Reviews* 5:193–230. (Chemoreceptor trigger
    zone; emetic reflex; apomorphine; the CTZ as the functional
    role of the area postrema.)
*   **Area postrema — canonical anatomy:** Miller, A.D., Leslie,
    R.A. (1994). "The area postrema and vomiting." *Frontiers in
    Neuroendocrinology* 15:301–320. (Area postrema;
    circumventricular organ; chemoreceptor trigger zone; vomiting
    reflex — the CTZ and AP are the same structure.)
*   **CINV (chemotherapy-induced nausea and vomiting):** Hesketh,
    P.J. (2008). "Chemotherapy-induced nausea and vomiting."
    *New England Journal of Medicine* 358:2482–2494.
    (Chemoreceptor trigger zone; 5-HT3 and NK1 receptor
    antagonists; CINV.)
*   **NMOSD — area postrema syndrome:** Pittock, S.J., et al.
    (2006). "Neuromyelitis optica brain lesions localized at
    sites of high aquaporin 4 expression." *Archives of
    Neurology* 63:964–968. (Area postrema — the anatomical
    structure whose functional role is the CTZ; AQP4-rich site;
    area postrema syndrome in NMOSD.)
*   **Immune-neural signaling — AP / CTZ:** Ericsson, A., et al.
    (1994). "A functional anatomical analysis of central pathways
    subserving interleukin-1-induced fever." *Journal of
    Comparative Neurology* 344:338–349. (Area postrema /
    chemoreceptor trigger zone; immune-to-brain signaling;
    cytokines; fever.)
*   **Cardiovascular regulation — AP / CTZ:** Ferguson, A.V.
    (1991). "The area postrema: a cardiovascular control centre
    during pregnancy?" *Canadian Journal of Physiology and
    Pharmacology* 69:555–558. (Area postrema / chemoreceptor
    trigger zone; angiotensin II; cardiovascular regulation.)
*   **Fluid balance — AP / CTZ:** McKinley, M.J., et al. (2003).
    "The sensory circumventricular organs of the mammalian brain:
    osmoreceptor, sodium receptor, or both?" *Progress in
    Biophysics and Molecular Biology* 82:125–137. (Area postrema
    / chemoreceptor trigger zone; osmoregulation; fluid balance.)
*   **Conditioned taste aversion — AP / CTZ:** Bernstein, I.L.,
    et al. (1984). "Area postrema mediates the formation of a
    conditioned taste aversion to a toxin." *Behavioral
    Neuroscience* 98:735–738. (Area postrema / chemoreceptor
    trigger zone; conditioned taste aversion.)
*   **Solitary nucleus (contrast — separate container):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS — primary
    projection target of the CTZ / AP, but a separate structure.)
*   **Fourth ventricle (contrast — CSF cavity):** Brodal, A.
    (2010). *The Central Nervous System: Structure and Function*,
    4th ed. (Fourth ventricle; CSF cavity; the caudal floor is
    lined by the area postrema whose functional role is the
    CTZ.)
*   **Dorsal motor nucleus of the vagus (contrast —
    parasympathetic):** Hopkins, D.A., Armour, J.A. (1984).
    "Localization of sympathetic postganglionic and
    parasympathetic preganglionic neurons which innervate
    different regions of the heart." *Journal of Comparative
    Neurology* 240:65–77. (Dorsal motor nucleus of the vagus —
    parasympathetic, different from the CTZ.)
*   **Hypoglossal nucleus (contrast — motor):** Lowe, A.A.
    (1980). "The neural regulation of tongue movement."
    *Progress in Neurobiology* 14:273–349. (Hypoglossal nucleus;
    tongue motor — different from the CTZ.)
*   NeuroNames — Area postrema (chemoreceptor trigger zone is a
    functional designation, not a distinct anatomical structure);
    FMA — Area postrema (the CTZ is the functional role of the
    area postrema, not a separate anatomical entity).
"""