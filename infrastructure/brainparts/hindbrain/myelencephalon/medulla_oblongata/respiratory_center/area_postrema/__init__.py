"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema
=====================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── area_postrema   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Area postrema; AP; postrema; area postrema of
the fourth ventricle; AP organ; circumventricular organ of the
area postrema.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**circumventricular organ** — a **specialized grey-matter region**
at the **caudal floor of the fourth ventricle** near the
**obex**, **lacking a blood-brain barrier**, that **senses
blood-borne and CSF-borne substances** (toxins, emetics,
hormones, cytokines) and **triggers the vomiting reflex** via
projections to the **NTS** and other **autonomic / emetic**
centers. It is **NOT** the **chemoreceptor trigger zone (CTZ)** —
in **this tree**, the CTZ is a **separate child** of
``respiratory_center``, even though the **literature** often
treats **AP and CTZ as synonymous**. It is **NOT** the
**solitary nucleus (NTS)** — the NTS is the **visceral afferent
relay** to which the AP **projects**, **NOT** the AP itself. It
is **NOT** the **dorsal motor nucleus of the vagus**, **NOT**
the **hypoglossal nucleus**, **NOT** the **dorsal respiratory
group**, and **NOT** the **whole respiratory_center**.
**Part of:** The **respiratory_center** container
(``.../respiratory_center/``) — which is part of the
**medulla oblongata** — the **caudal brainstem** subdivision of
the **myelencephalon**.
**Structural parent:** ``.../respiratory_center/`` → **direct
child** of the respiratory_center container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** area postrema.
The bilateral area postrema is the **structural children** of
this **bilateral container**; the container itself is
**unpaired**. **In the human brain, the area postrema is a
midline structure** (a single, unpaired circumventricular
organ), but the **tree wires it as a bilateral container** with
``left`` and ``right`` leaf children — this is a **wiring
convention** consistent with the rest of the medulla oblongata
children, **NOT** an anatomical claim that there are two separate
area postremae.
**Boundary status (NOT the chemoreceptor trigger zone — a
DIFFERENT child in THIS TREE, even though often synonymous in
the literature):** **Boundary case — the area postrema is NOT
the chemoreceptor trigger zone (CTZ) in this tree.** In the
**literature**, the **area postrema** and the **chemoreceptor
trigger zone** are **often used interchangeably** — they are
**largely considered** the **same structure** (the AP **is** the
CTZ for most physiological and pharmacological purposes). **In
this tree**, however, they are **wired as two separate child
containers** of ``respiratory_center``:
``respiratory_center.area_postrema`` (this module) and
``respiratory_center.chemoreceptor_trigger_zone``. Consumers must
**not** conflate the two modules **within the tree** — resolve
the **CTZ** via
``respiratory_center.chemoreceptor_trigger_zone``. This is a
**deliberate tree-wiring choice** — the **"area postrema"** name
denotes the **anatomical structure**; the **"chemoreceptor
trigger zone"** name denotes the **functional role** — and the
tree **separates** them into **two children** even though the
**literature** may treat them as **one**.
**Boundary status (NOT the solitary nucleus (NTS) — the NTS is
the primary projection target of the area postrema):**
**Boundary case — the area postrema is NOT the solitary nucleus
(NTS).** The **solitary nucleus**
(``.../solitary_nucleus/``) is the **visceral afferent relay** —
it is a **separate container** under ``medulla_oblongata``. The
**area postrema** (here) is a **circumventricular organ** that
**projects to** the NTS — the NTS is the **downstream target**
of the AP's **emetic and autonomic** signals. **They are
DIFFERENT STRUCTURES** — the **AP** is the **sensor**
(circumventricular); the **NTS** is the **relay** (visceral
afferent). Consumers must **not** conflate the two.
**Boundary status (NOT the dorsal motor nucleus of the vagus —
a DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the area postrema is NOT the dorsal motor nucleus of the
vagus.** The **dorsal motor nucleus of the vagus**
(``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``
and
``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
is the **parasympathetic** nucleus for the **thoracic and
abdominal viscera**. The **area postrema** (here) is a
**circumventricular organ** — **NOT** a parasympathetic nucleus.
They are **anatomically adjacent** at the **caudal fourth
ventricle floor**, but they are **functionally distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the hypoglossal nucleus — a DIFFERENT
structure with a DIFFERENT function):** **Boundary case — the
area postrema is NOT the hypoglossal nucleus.** The
**hypoglossal nucleus**
(``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/`` and
``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is the
**somatic motor** nucleus for the **tongue**. The **area
postrema** (here) is a **circumventricular organ** — **NOT** a
motor nucleus. They are **anatomically adjacent** at the
**caudal fourth ventricle floor** (the hypoglossal trigone is
**rostral** to the area postrema), but they are **functionally
distinct**. Consumers must **not** conflate the two.
**Boundary status (NOT the dorsal respiratory group — a
DIFFERENT child of respiratory_center):** **Boundary case — the
area postrema is NOT the dorsal respiratory group (DRG).** The
**dorsal respiratory group**
(``.../respiratory_center/dorsal_respiratory_group/``) is the
**dorsal respiratory** pattern generator — **NOT** a
circumventricular organ. Both are **children** of
``respiratory_center``, but they are **functionally distinct** —
the **DRG** is **respiratory**; the **AP** is **circumventricular
/ chemosensory**. Consumers must **not** conflate the two.
**Boundary status (NOT the dorsal column nuclei — cuneate and
gracile — DIFFERENT children of respiratory_center):**
**Boundary case — the area postrema is NOT the cuneate or
gracile nucleus.** The **cuneate** and **gracile nuclei**
(``.../respiratory_center/cuneate_nucleus/`` and
``.../respiratory_center/gracile_nucleus/``) are the **dorsal
column somatosensory relays**. The **area postrema** (here) is a
**circumventricular organ**. All three are **children** of
``respiratory_center``, but they are **functionally distinct**.
Consumers must **not** conflate them.
**Boundary status (NOT the gigantocellular reticular nucleus —
a DIFFERENT child of respiratory_center):** **Boundary case —
the area postrema is NOT the gigantocellular reticular nucleus
(Gi).** The **gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/``)
is a **large medullary reticular** nucleus. The **area
postrema** (here) is a **circumventricular organ**. Both are
**children** of ``respiratory_center``, but they are
**functionally distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the fourth ventricle — the fourth
ventricle is a CSF cavity, the area postrema is a CSF-sensing
organ at its floor):** **Boundary case — the area postrema is
NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is a **CSF cavity** —
**NOT** a grey-matter structure. The **area postrema** (here)
**lines the floor** of the **caudal fourth ventricle** and
**senses the CSF** — but it is **NOT** the ventricle itself.
Consumers must **not** conflate the **organ** with the
**cavity**.
**Boundary status (NOT the whole respiratory_center — a CHILD of
it):** **Boundary case — the area postrema is NOT the whole
respiratory_center.** The **respiratory_center**
(``.../respiratory_center/``) is the **parent container** — it
contains the **area postrema** (here) **plus** the
``chemoreceptor_trigger_zone``, ``cuneate_nucleus``,
``dorsal_respiratory_group``, ``gigantocellular_reticular_nucleus``,
and ``gracile_nucleus``. The **area postrema** is **one child**
of that container. Consumers must **not** conflate the **child**
with the **whole container**.
**Boundary status (NOT the whole medulla oblongata — a small
circumventricular organ within it):** **Boundary case — the
area postrema is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the area postrema (via the
respiratory_center) **plus** the cranial nerve nuclei, the
autonomic nuclei, the olivary body, the medullary pyramid, the
arcuate nucleus, the parafacial zone, the paramedian reticular
nucleus, the perihypoglossal nuclei, the respiratory_center, and
other structures. The **area postrema** is **one small
circumventricular organ** within the medulla. Consumers must
**not** conflate the **area postrema** with the **whole
medulla**.
**Boundary status (BILATERAL container — left and right are
structural children, but the area postrema is ANATOMICALLY
MIDLINE):** **Boundary case — the area postrema is a BILATERAL
container in this tree, but it is ANATOMICALLY MIDLINE in the
human brain.** The **area_postrema** module (here) is an
**unpaired container**; its **structural children** are ``left``
and ``right`` — each a **leaf** representing the **left** or
**right** side of the area postrema. **Anatomically**, the human
area postrema is a **single, unpaired, midline** structure — the
``left`` and ``right`` children in this tree are a **wiring
convention** (consistent with the rest of the medulla oblongata
children), **NOT** an anatomical claim that there are **two
separate area postremae**. Consumers must **not** infer that the
human area postrema is **bilateral / paired** from the tree
structure.

Overview
--------
The **area postrema (AP)** is a **circumventricular organ** at
the **caudal floor of the fourth ventricle**, near the **obex**.
It is a **specialized grey-matter region** that **lacks a
blood-brain barrier** — its **fenestrated capillaries** allow
**blood-borne substances** to **reach** its **neurons**
directly, and it **senses** **CSF-borne substances** via its
**CSF-facing surface**. It is the **primary chemosensory organ**
for the **vomiting reflex** — it **detects** **toxins**,
**emetics** (e.g., **apomorphine**), **hormones** (e.g.,
**angiotensin II**, **amylin**, **GLP-1**), and **cytokines**,
and it **triggers** **nausea and vomiting** via **projections**
to the **NTS** and other **autonomic** and **emetic** centers.

**The area postrema is a CIRCUMVENTRICULAR ORGAN, NOT a
respiratory nucleus.** Although it is wired under
``respiratory_center``, its **primary function** is
**chemoreception / emesis / autonomic regulation** — **NOT**
**breathing**. The **"respiratory_center"** label is a
**tree-wiring artifact** — the tree groups the area postrema with
respiratory and dorsal column nuclei as a **pragmatic cluster**.
Consumers must **not** infer **respiratory function** from
**container membership**.

**The area postrema is the CHEMOSENSORY organ, NOT the
chemoreceptor trigger zone.** In **this tree**, the
**chemoreceptor trigger zone (CTZ)** is a **separate child** of
``respiratory_center`` — even though the **literature** often
treats **AP and CTZ as synonymous**. The **AP** is the
**anatomical structure**; the **CTZ** is the **functional role**
— and this tree **separates** them into **two modules**.

**The area postrema is ANATOMICALLY MIDLINE — the tree's
``left`` / ``right`` split is a WIRING CONVENTION.** The human
area postrema is a **single, unpaired** circumventricular organ
at the **caudal floor** of the fourth ventricle. The tree
represents it as a **bilateral container** with ``left`` and
``right`` leaf children — **consistent with the wiring pattern**
of the other medulla oblongata children — but **NOT** an
anatomical claim that the area postrema is **paired**.

**The area postrema is functionally coupled to the solitary
nucleus (NTS), the parabrachial nucleus, the dorsal motor
nucleus of the vagus, and the hypothalamic autonomic centers.**
It **projects** to the **NTS** (the primary target), the
**parabrachial nucleus** (for **visceral / autonomic**
integration), and the **hypothalamus** (for **fluid balance**,
**cardiovascular regulation**, and **neuroendocrine** responses).
It is **functionally coupled** to these structures but **NOT**
identical to any of them.

Bilateral Structure (Wiring Convention)
---------------------------------------
The area postrema is a **bilateral container** in this tree with
**two structural children**:

*   ``left`` — the **left** area postrema (a **leaf** module).
*   ``right`` — the **right** area postrema (a **leaf** module).

**The two children are a WIRING CONVENTION, NOT an anatomical
claim.** The human area postrema is a **single, unpaired, midline**
circumventricular organ — the ``left`` and ``right`` leaves do
**not** represent **two separate area postremae**. They are
**wired** as **left / right leaves** to **maintain consistency**
with the rest of the medulla oblongata children (which **are**
bilateral in the brain).

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **aspects** of the **midline area postrema**
as **single structures**, **NOT** two separate organs. Consumers
that need **side-specific** resolution should descend into
``left`` or ``right``; consumers that need **the whole organ**
should use ``area_postrema`` (the container) as a whole.

**The container itself is unpaired.** There is **no**
``area_postrema/left/.../`` structural hierarchy beyond the
single leaf level — the ``left`` and ``right`` modules are the
**terminal modules** for this structure.

The Area Postrema / Chemoreceptor Trigger Zone Boundary
-------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Area postrema (AP)** (this module) — the **anatomical
    circumventricular organ**.

*   **Chemoreceptor trigger zone (CTZ)**
    (``.../respiratory_center/chemoreceptor_trigger_zone/``) —
    the **functional role** — **often used interchangeably** with
    the **area postrema** in the **literature**.

**They are WIRED AS TWO SEPARATE CHILDREN** of
``respiratory_center`` **in this tree**, even though the
**literature** often treats them as **synonymous**. Consumers
must **not** conflate the two modules **within the tree** —
resolve the **CTZ** via
``respiratory_center.chemoreceptor_trigger_zone`` and the **AP**
via ``respiratory_center.area_postrema``.

The Area Postrema / Solitary Nucleus Boundary
---------------------------------------------
This is the **sensor / relay** boundary:

*   **Area postrema** (this module) — the **circumventricular
    chemosensory organ**.

*   **Solitary nucleus (NTS)** (``.../solitary_nucleus/``) — the
    **visceral afferent relay**.

**The area postrema PROJECTS TO the NTS** — the NTS is the
**downstream target** of the AP's **emetic and autonomic**
signals. **They are DIFFERENT STRUCTURES** — the **AP** is the
**sensor**; the **NTS** is the **relay**. Consumers must **not**
conflate the two.

The Area Postrema / Dorsal Motor Nucleus of the Vagus and Hypoglossal Nucleus Boundary
--------------------------------------------------------------------------------------
This is the **circumventricular / motor** boundary:

*   **Area postrema** (this module) — the **circumventricular
    organ**.

*   **Dorsal motor nucleus of the vagus**
    (``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``
    and
    ``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
    — the **parasympathetic** nucleus.

*   **Hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/`` and
    ``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES** — the **AP** is a
**circumventricular organ**; the **dorsal motor nucleus of the
vagus** and the **hypoglossal nucleus** are **motor nuclei**.
Consumers must **not** conflate the two.

The Area Postrema / Other Respiratory Center Children Boundary
--------------------------------------------------------------
This is the **circumventricular / respiratory-and-somatosensory**
boundary:

*   **Area postrema** (this module) — the **circumventricular
    organ**.

*   **Dorsal respiratory group** (``.../dorsal_respiratory_group/``)
    — the **dorsal respiratory** pattern generator.

*   **Gigantocellular reticular nucleus**
    (``.../gigantocellular_reticular_nucleus/``) — the **large
    medullary reticular** nucleus.

*   **Cuneate nucleus** (``.../cuneate_nucleus/``) — the **dorsal
    column somatosensory** relay (upper body).

*   **Gracile nucleus** (``.../gracile_nucleus/``) — the **dorsal
    column somatosensory** relay (lower body).

**They are DIFFERENT STRUCTURES** — all six are **children** of
``respiratory_center``, but they are **functionally distinct**.
Consumers must **not** conflate the **AP** with any of these.

The Area Postrema / Fourth Ventricle Boundary
---------------------------------------------
This is the **organ / cavity** boundary:

*   **Area postrema** (this module) — the **circumventricular
    organ** that **lines the floor** of the **caudal fourth
    ventricle**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the **CSF
    cavity**.

**The AP is at the FLOOR of the fourth ventricle** — but it is
**NOT** the fourth ventricle itself. Consumers must **not**
conflate the **organ** with the **cavity**.

The Area Postrema / Whole Respiratory Center and Whole Medulla Oblongata Boundary
--------------------------------------------------------------------------------
This is the **child / container** boundary:

*   **Area postrema** (this module) — one **child** of
    ``respiratory_center``.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children**.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The area postrema is a CHILD of respiratory_center, NOT the
container itself, and NOT the whole medulla.** Consumers must
**not** conflate the **child** with either **parent container**.

Function in the Human Brain
---------------------------
The area postrema's functions are **chemoreception**,
**emesis**, **autonomic regulation**, **fluid balance**, and
**immune-neural signaling** — **NOT respiratory rhythm** and
**NOT motor control**:

*   **Chemoreception (blood-borne and CSF-borne signals):** The
    **area postrema** **lacks a blood-brain barrier** — its
    **fenestrated capillaries** allow **blood-borne substances**
    (toxins, emetics, hormones, cytokines) to **reach** its
    **neurons**. It also **senses CSF-borne substances** via its
    **CSF-facing surface**. It is the **primary chemosensory
    organ** of the **caudal brainstem**.

*   **Vomiting reflex (emesis):** The **area postrema** is the
    **primary chemoreceptor trigger zone** for the **vomiting
    reflex** — it **detects** **emetic substances** (e.g.,
    **apomorphine**, **chemotherapy agents**, **toxins**) and
    **triggers** **nausea and vomiting** via **projections** to
    the **NTS** and other **emetic centers**.

*   **Autonomic regulation (cardiovascular and gastrointestinal):**
    The **area postrema** **participates** in **cardiovascular
    regulation** (sensing **angiotensin II**, **osmolality**)
    and **gastrointestinal regulation** (sensing **gut
    hormones** like **GLP-1** and **amylin**), **projecting** to
    the **NTS** and **hypothalamus**.

*   **Fluid and electrolyte balance:** The **area postrema**
    **senses** **plasma osmolality** and **angiotensin II** —
    **contributing** to **thirst**, **salt appetite**, and
    **vasopressin** release (via **hypothalamic** projections).

*   **Immune-neural signaling:** The **area postrema** **senses**
    **cytokines** and **bacterial endotoxin** (LPS) — it is a
    **site of immune-to-brain signaling** contributing to
    **sickness behavior**, **fever**, and **anorexia**.

*   **Conditioned taste aversion:** The **area postrema** is
    **required** for **conditioned taste aversion** — the
    **learned avoidance** of a **taste** that has been
    **paired** with **nausea** or **vomiting**.

*   **NOT respiratory rhythm:** The **area postrema** does
    **not** generate the **respiratory rhythm** — that is the
    **pre-Bötzinger complex** (VRG) and the **respiratory**
    centers. The **AP** is a **circumventricular** organ — **NOT**
    a respiratory nucleus.

*   **NOT motor control:** The **area postrema** does **not**
    send motor axons to muscles.

**The unifying theme:** the area postrema is a **circumventricular
organ** at the **caudal fourth ventricle floor** — a
**chemosensory**, **emetic**, **autonomic**, **fluid-balance**,
and **immune-neural** structure — **NOT** a respiratory nucleus,
**NOT** the NTS, **NOT** the chemoreceptor trigger zone (in this
tree), and **NOT** the fourth ventricle.

Associated Disorders
--------------------
The area postrema is the **substrate** for **well-defined
clinical syndromes** — its clinical relevance is **direct**,
via **emesis**, **autonomic**, and **immune-neural** dysfunction:

*   **Chemotherapy-induced nausea and vomiting (CINV — via area
    postrema):** **Chemotherapy agents** (e.g., **cisplatin**,
    **doxorubicin**) and their **metabolites** **stimulate** the
    **area postrema** — triggering **nausea** and **vomiting**
    via **NTS** and **parabrachial** projections. **5-HT3
    receptor antagonists** (e.g., **ondansetron**) and **NK1
    receptor antagonists** (e.g., **aprepitant**) **target** the
    **AP / NTS** pathway to **prevent** **CINV**.

*   **Area postrema syndrome (APS — in neuromyelitis optica
    spectrum disorder, NMOSD):** **Neuromyelitis optica
    (NMO)** — an **autoimmune** disorder targeting
    **aquaporin-4 (AQP4)** — **frequently** involves the **area
    postrema** (a **high-AQP4** site), causing **intractable
    nausea**, **vomiting**, and **hiccups** (**area postrema
    syndrome**). **APS** is often an **initial** manifestation of
    **NMOSD**.

*   **Cyclic vomiting syndrome (CVS — hypothesized AP
    involvement):** **CVS** is a **disorder** of **recurrent
    episodes** of **severe nausea and vomiting** — **hypothesized**
    to involve **AP** and **mitochondrial** dysfunction. The
    **AP** is a **contributing substrate**, though the **primary**
    mechanism is **not fully characterized**.

*   **Bulimia nervosa and eating disorders (hypothesized AP
    involvement):** **Impaired** **AP-mediated** **satiety** and
    **emetic** signaling have been **hypothesized** to
    **contribute** to **bulimia nervosa** and **binge-eating
    disorder** — though the **primary** pathology is
    **multifactorial**.

*   **Drug-induced emesis (via AP):** **Many** drugs
    (**opioids**, **digoxin**, **apomorphine**, **nicotine**)
    **stimulate** the **area postrema** — triggering **nausea**
    and **vomiting**. The **AP** is the **primary** central
    **emetic** sensor.

*   **Sickness behavior and fever (via AP immune-neural
    signaling):** The **AP** **senses** **cytokines** and
    **LPS** — **contributing** to **fever**, **anorexia**,
    **lethargy**, and **sickness behavior** during **infection**
    and **inflammation**.

*   **No Named "Area Postrema Syndrome" beyond APS:** The
    **area postrema** has **one** named clinical syndrome —
    **area postrema syndrome (APS)** — which is **specific** to
    **NMOSD** and **not** a general term for **AP dysfunction**.
    Its **other** clinical relevance is **emesis**,
    **autonomic**, and **immune-neural** — as described above.

**What is NOT here:** The area postrema is **not** the substrate
for **central hypoventilation** (VRG, pre-Bötzinger complex),
**sympathetic premotor** function (RVLM), **visceral afferent
relay** (NTS), **tongue weakness** (hypoglossal nucleus), or
**parasympathetic dysfunction** (dorsal motor nucleus of the
vagus). Its clinical relevance is the **emesis**, **autonomic**,
and **immune-neural** functions listed above.

Lateralization Notes
--------------------
The area postrema is a **bilateral container** in this tree with
``left`` and ``right`` structural children. There is **no**
``area_postrema/left/.../`` structural hierarchy beyond the
single leaf level.

*   **Bilateral structural children (wiring convention):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left-side** or **right-side** **aspects** of the
    **midline area postrema** as a **single structure**. The
    **anatomical area postrema** is a **single, unpaired,
    midline** circumventricular organ — the **left / right split**
    is a **tree-wiring convention**.

*   **NO lateralization:** The area postrema has **no known
    functional lateralization** — it is a **midline** structure
    with **no left / right functional difference**. Consumers
    must **not** import a **lateralization warning** into the
    area postrema — the **left** and **right** sides are
    **functionally identical** and **anatomically the same**
    structure.

*   **NO Extended-Amygdala / SLEA Warning:** The area postrema
    is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the area postrema.

*   **NO Fear-Output Warning:** The area postrema is **not** a
    fear-output structure — it is a **circumventricular
    chemosensory** organ. Consumers must **not** conflate it
    with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "left area postrema = right area
postrema" will be structurally correct** — the two sides are
**equivalent** (they represent the **same midline** structure).
The area postrema is a **strict-mirror container with NO
warning** — **no SLEA warning**, **no fear-output warning**,
and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The area postrema is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../chemoreceptor_trigger_zone/``,
    ``.../dorsal_respiratory_group/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../metencephalon/fourth_ventricle/``, or any other
    container. The area postrema's relationships to the
    chemoreceptor trigger zone, dorsal respiratory group,
    gigantocellular reticular nucleus, cuneate nucleus, gracile
    nucleus, solitary nucleus, dorsal motor nucleus of the
    vagus, hypoglossal nucleus, and fourth ventricle are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children (wiring
    convention).** The structural children are ``left`` and
    ``right``, each a **leaf**. **Anatomically**, the human area
    postrema is a **single midline structure** — the **left /
    right split** is a **tree-wiring convention**, **NOT** an
    anatomical claim of two separate organs.
*   **CIRCUMVENTRICULAR ORGAN, NOT a respiratory nucleus.**
    Although wired under ``respiratory_center``, the area
    postrema is a **chemoreceptive / emetic / autonomic /
    immune-neural** structure — **NOT** a respiratory rhythm
    generator.
*   **NOT the chemoreceptor trigger zone (in this tree).** The
    **CTZ** is a **separate child** of ``respiratory_center`` —
    consumers must **not** conflate the two modules **within the
    tree**, even though the **literature** often treats them as
    **synonymous**.
*   **NOT the solitary nucleus (NTS).** The **NTS** is a
    **separate container** — the **AP projects to** the **NTS**,
    but is **NOT** the NTS itself.
*   **NOT the dorsal motor nucleus of the vagus, hypoglossal
    nucleus, dorsal respiratory group, gigantocellular reticular
    nucleus, cuneate nucleus, or gracile nucleus.** Each is a
    **different structure** — see the respective modules.
*   **NOT the fourth ventricle.** The fourth ventricle is a
    **CSF cavity**; the area postrema is the **circumventricular
    organ** that **lines its caudal floor**.
*   **NOT the whole respiratory_center or whole medulla
    oblongata.** The area postrema is a **child** of
    ``respiratory_center``, not the container itself.
*   **No ``AREA_PATHS`` hop.** The area postrema is a **local
    container** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The area postrema has no
    nested dual-framing module. It is a **bilateral container**
    with **two leaf children** (wiring convention).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **circumventricular
    chemosensory** framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center import area_postrema

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.area_postrema"
    )

**Do not** assume the area postrema is the **chemoreceptor
trigger zone** in this tree. They are **separate children** of
``respiratory_center`` — resolve the **CTZ** via
``respiratory_center.chemoreceptor_trigger_zone``.

**Do not** assume the area postrema is the **solitary nucleus
(NTS)**. The NTS is a **separate container** — the AP
**projects to** the NTS, but is **NOT** the NTS itself.

**Do not** assume the area postrema is the **dorsal motor
nucleus of the vagus**, the **hypoglossal nucleus**, the
**dorsal respiratory group**, the **gigantocellular reticular
nucleus**, the **cuneate nucleus**, or the **gracile nucleus**.
Each is a **different structure**.

**Do not** assume the area postrema is the **fourth ventricle**.
The fourth ventricle is a **CSF cavity**; the area postrema is
the **circumventricular organ** at its **caudal floor**.

**Do not** assume the area postrema is the **whole
respiratory_center** or the **whole medulla oblongata**. It is
a **child** of ``respiratory_center``.

**Do not** assume the human area postrema is **bilateral /
paired** from the tree structure. **Anatomically**, it is a
**single, unpaired, midline** structure — the ``left`` / ``right``
split is a **tree-wiring convention**.

Iterating the area postrema's structural children (recommended
consumer pattern)::

    AREA_POSTREMA_CHILDREN = ("left", "right")
    # Each child is a leaf module representing an aspect of the
    # MIDLINE area postrema. Anatomically, the area postrema is
    # a SINGLE midline structure — the left/right split is a
    # tree-wiring convention, NOT an anatomical claim of two
    # separate organs.

Reaching the left and right area postrema leaves (recommended
consumer pattern)::

    # The left and right area postrema leaves are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.right
    #
    # Each is a leaf module representing an ASPECT of the MIDLINE
    # area postrema. Anatomically, there is ONE area postrema —
    # the left/right split is a tree-wiring convention.

Reaching the chemoreceptor trigger zone (recommended consumer
pattern — NOTE the DIFFERENT child, often synonymous in the
literature but SEPARATE in this tree)::

    # The chemoreceptor trigger zone is a SEPARATE child of
    # respiratory_center in this tree — even though the
    # literature often treats it as synonymous with the area
    # postrema:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone
    #
    # Consumers must NOT conflate the two modules within the
    # tree — resolve the CTZ via its own path.

Reaching the solitary nucleus (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The solitary nucleus (NTS) is a SEPARATE container under
    # medulla_oblongata — the area postrema PROJECTS to the
    # NTS, but is NOT the NTS itself:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #
    # The area postrema is the CHEMOSENSORY organ; the NTS is
    # the VISCERAL AFFERENT relay.

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
    # They are NOT part of the area postrema — they are
    # functionally distinct motor nuclei.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the DIFFERENT container)::

    # The fourth ventricle is a CSF cavity in the METENCEPHALON:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The area postrema LINES the caudal floor of the fourth
    # ventricle — but it is NOT the ventricle itself.

Bilateral iteration (recommended consumer pattern — with the
caveat that the area postrema is anatomically midline)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"respiratory_center.area_postrema.{side}"
        )
        # resolve path through the memory/recall layer

References
----------
*   **Area postrema — canonical anatomy:** Miller, A.D., Leslie,
    R.A. (1994). "The area postrema and vomiting." *Frontiers in
    Neuroendocrinology* 15:301–320. (Area postrema; circumventricular
    organ; chemoreceptor trigger zone; vomiting reflex.)
*   **Area postrema — circumventricular organ:** Broadwell,
    R.D., Brightman, M.W. (1976). "Entry of peroxidase into
    neurons of the central and peripheral nervous systems from
    extracerebral and cerebral blood." *Journal of Comparative
    Neurology* 166:257–283. (Area postrema; fenestrated
    capillaries; lack of blood-brain barrier.)
*   **Area postrema — emesis:** Borison, H.L., Wang, S.C. (1953).
    "Physiology and pharmacology of vomiting." *Pharmacological
    Reviews* 5:193–230. (Area postrema; chemoreceptor trigger
    zone; emetic reflex; apomorphine.)
*   **Area postrema — CINV (chemotherapy-induced nausea and
    vomiting):** Hesketh, P.J. (2008). "Chemotherapy-induced
    nausea and vomiting." *New England Journal of Medicine*
    358:2482–2494. (Area postrema; 5-HT3 and NK1 receptor
    antagonists; CINV.)
*   **Area postrema — NMOSD / area postrema syndrome:** Pittock,
    S.J., et al. (2006). "Neuromyelitis optica brain lesions
    localized at sites of high aquaporin 4 expression."
    *Archives of Neurology* 63:964–968. (Area postrema;
    AQP4-rich site; area postrema syndrome in NMOSD.)
*   **Area postrema — NMOSD — area postrema syndrome:** Wingerchuk,
    D.M., et al. (2015). "International consensus diagnostic
    criteria for neuromyelitis optica spectrum disorders."
    *Neurology* 85:177–189. (Area postrema syndrome;
    NMOSD diagnostic criteria.)
*   **Area postrema — immune-neural signaling:** Ericsson, A.,
    et al. (1994). "A functional anatomical analysis of central
    pathways subserving interleukin-1-induced fever." *Journal
    of Comparative Neurology* 344:338–349. (Area postrema;
    immune-to-brain signaling; cytokines; fever.)
*   **Area postrema — cardiovascular regulation:** Ferguson,
    A.V. (1991). "The area postrema: a cardiovascular control
    centre during pregnancy?" *Canadian Journal of Physiology
    and Pharmacology* 69:555–558. (Area postrema; angiotensin
    II; cardiovascular regulation.)
*   **Area postrema — fluid balance:** McKinley, M.J., et al.
    (2003). "The sensory circumventricular organs of the
    mammalian brain: osmoreceptor, sodium receptor, or both?"
    *Progress in Biophysics and Molecular Biology* 82:125–137.
    (Area postrema; osmoregulation; fluid balance.)
*   **Area postrema — conditioned taste aversion:** Bernstein,
    I.L., et al. (1984). "Area postrema mediates the formation
    of a conditioned taste aversion to a toxin." *Behavioral
    Neuroscience* 98:735–738. (Area postrema; conditioned taste
    aversion.)
*   **Chemoreceptor trigger zone (contrast — often synonymous
    with AP in the literature):** Borison, H.L., Brizzee, K.R.
    (1951). "Morphology of emetic chemoreceptor trigger zone in
    cat medulla oblongata." *Proceedings of the Society for
    Experimental Biology and Medicine* 77:38–42. (Chemoreceptor
    trigger zone — the functional role of the area postrema —
    often used interchangeably with AP in the literature.)
*   **Solitary nucleus (contrast — separate container):**
    Andresen, M.C., Kunze, D.L. (1994). "Nucleus tractus
    solitarius — gateway to neural circulatory control."
    *Annual Review of Physiology* 56:93–116. (NTS — primary
    projection target of the area postrema, but a separate
    structure.)
*   **Fourth ventricle (contrast — CSF cavity):** Brodal, A.
    (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Fourth ventricle; CSF cavity; the
    caudal floor is lined by the area postrema.)
*   **Hypoglossal nucleus (contrast — motor):** Lowe, A.A.
    (1980). "The neural regulation of tongue movement."
    *Progress in Neurobiology* 14:273–349. (Hypoglossal nucleus;
    tongue motor — different from the area postrema.)
*   **Dorsal motor nucleus of the vagus (contrast —
    parasympathetic):** Hopkins, D.A., Armour, J.A. (1984).
    "Localization of sympathetic postganglionic and
    parasympathetic preganglionic neurons which innervate
    different regions of the heart." *Journal of Comparative
    Neurology* 240:65–77. (Dorsal motor nucleus of the vagus —
    parasympathetic, different from the area postrema.)
*   NeuroNames — Area postrema; FMA — Area postrema.
"""