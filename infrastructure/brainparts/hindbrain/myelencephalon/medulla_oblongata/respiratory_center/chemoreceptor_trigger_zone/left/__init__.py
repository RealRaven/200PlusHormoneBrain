"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.left
======================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── chemoreceptor_trigger_zone
                    └── left   <-- THIS MODULE

**Primary synonym:** Left chemoreceptor trigger zone; left CTZ;
left aspect of the chemoreceptor trigger zone; left aspect of the
area postrema's functional role.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**circumventricular organ's functional role** — in **this tree**,
the **left leaf** representing the **left-side aspect** of the
**midline chemoreceptor trigger zone**. The **CTZ** is the
**functional role** of the **area postrema** (chemoreception /
emetic trigger); **anatomically**, the **CTZ is the area
postrema** — a **single, unpaired, midline** circumventricular
organ at the **caudal floor of the fourth ventricle**. The
``left`` module is a **tree-wiring convention** — **NOT** an
anatomical claim that there is a **separate left CTZ**.
**Part of:** The **chemoreceptor_trigger_zone** bilateral
container
(``.../respiratory_center/chemoreceptor_trigger_zone/``) — which
is part of the **respiratory_center** — which is part of the
**medulla oblongata** — the **caudal brainstem** subdivision of
the **myelencephalon**.
**Structural parent:** ``.../chemoreceptor_trigger_zone/`` →
**direct child** of the chemoreceptor_trigger_zone container.
The **left** leaf is one of the **two** structural children of
the container (the other is ``right``).
**Structural children:** **None.** This is a **leaf** module. The
left CTZ is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the right chemoreceptor trigger zone —
the contralateral leaf, both representing the SAME midline
structure):** **Boundary case — the left chemoreceptor trigger
zone is NOT the right chemoreceptor trigger zone.** The **right
chemoreceptor trigger zone**
(``.../chemoreceptor_trigger_zone/right/``) is the
**contralateral leaf** — the **right-side aspect** of the
**same midline CTZ**. **They are DIFFERENT LEAVES** — the
``left`` and ``right`` modules are the two sides of the
**bilateral container**. **In the brain, there is ONE CTZ** —
the **left** and **right** leaves are **tree-wiring aspects**
of the **same midline structure**, **NOT** two separate
functional roles. Consumers must **not** infer **anatomical
bilaterality** from the tree structure.
**Boundary status (NOT the whole chemoreceptor trigger zone — an
ASPECT of it):** **Boundary case — the left chemoreceptor
trigger zone is NOT the whole chemoreceptor trigger zone.** The
**whole chemoreceptor trigger zone**
(``.../chemoreceptor_trigger_zone/``) is the **bilateral
container** that **contains** the left CTZ (here) **plus** the
right CTZ. The **left** module is **one aspect** — the
**left-side aspect** — of the **midline CTZ**. Consumers must
**not** conflate the **leaf** with the **container**.
**Boundary status (NOT the left area postrema leaf — the SAME
structure under a DIFFERENT name, wired as a SEPARATE child in
this tree):** **Boundary case — the left chemoreceptor trigger
zone is NOT the left area postrema in this tree.** In the
**literature**, the **chemoreceptor trigger zone** and the
**area postrema** are **often used interchangeably** — they are
**largely considered the same structure** — the **CTZ** is the
**functional role** of the **area postrema** for
**blood-borne / CSF-borne emetic detection**. **In this tree**,
they are **wired as two separate child containers** of
``respiratory_center``:
``respiratory_center.chemoreceptor_trigger_zone`` (this module's
parent) and ``respiratory_center.area_postrema``. The
**corresponding left leaf** of the area postrema is at
``.../respiratory_center/area_postrema/left/``. **They refer to
the SAME PHYSICAL STRUCTURE** (left aspect of the midline area
postrema) under **two different names**. Consumers must **not**
conflate the two leaves **within the tree** — resolve the
**left area postrema** via
``respiratory_center.area_postrema.left`` and the **left CTZ**
via ``respiratory_center.chemoreceptor_trigger_zone.left``.
**Consumers must also not conclude** that **wiring separation**
implies **anatomical separation** — the **underlying structure**
is **one**.
**Boundary status (NOT the left solitary nucleus — a DIFFERENT
structure in a DIFFERENT container):** **Boundary case — the
left chemoreceptor trigger zone is NOT the left solitary nucleus
(NTS).** The **left solitary nucleus**
(``.../solitary_nucleus/left/``) is the **left visceral
afferent relay** — it is a **separate structure** in a
**separate container**. The **left CTZ** (here) is a
**left-aspect** of the **circumventricular organ's functional
role** that **projects to** the NTS. **They are DIFFERENT
STRUCTURES** — the **CTZ** is the **sensor's functional role**;
the **NTS** is the **relay**. Consumers must **not** conflate
the two.
**Boundary status (NOT the left dorsal motor nucleus of the
vagus — a DIFFERENT structure with a DIFFERENT function):**
**Boundary case — the left chemoreceptor trigger zone is NOT the
left dorsal motor nucleus of the vagus.** The **left dorsal
motor nucleus of the vagus**
(``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``)
is the **left parasympathetic** nucleus. The **left CTZ**
(here) is a **left-aspect** of the **circumventricular
organ's functional role** — **NOT** a parasympathetic nucleus.
They are **anatomically adjacent** at the **caudal fourth
ventricle floor**, but they are **functionally distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the left hypoglossal nucleus — a
DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the left chemoreceptor trigger zone is NOT the left
hypoglossal nucleus.** The **left hypoglossal nucleus**
(``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) is the
**left somatic motor** nucleus for the **tongue**. The **left
CTZ** (here) is a **left-aspect** of the **circumventricular
organ's functional role** — **NOT** a motor nucleus. Consumers
must **not** conflate the two.
**Boundary status (NOT the left dorsal respiratory group — a
DIFFERENT child of respiratory_center):** **Boundary case — the
left chemoreceptor trigger zone is NOT the left dorsal
respiratory group (DRG).** The **left dorsal respiratory group**
(``.../respiratory_center/dorsal_respiratory_group/left/``) is
the **left dorsal respiratory** pattern generator — **NOT** a
circumventricular functional role. Both are **leaves** under
different children of ``respiratory_center``, but they are
**functionally distinct** — the **DRG** is **respiratory**; the
**CTZ** is **circumventricular / chemosensory**. Consumers must
**not** conflate the two.
**Boundary status (NOT the left cuneate or left gracile nucleus
— DIFFERENT children of respiratory_center):** **Boundary case
— the left chemoreceptor trigger zone is NOT the left cuneate or
left gracile nucleus.** The **left cuneate nucleus**
(``.../respiratory_center/cuneate_nucleus/left/``) and **left
gracile nucleus**
(``.../respiratory_center/gracile_nucleus/left/``) are the
**left dorsal column somatosensory relays**. The **left CTZ**
(here) is a **left-aspect** of the **circumventricular organ's
functional role** — **NOT** a somatosensory relay. Consumers
must **not** conflate them.
**Boundary status (NOT the left gigantocellular reticular
nucleus — a DIFFERENT child of respiratory_center):** **Boundary
case — the left chemoreceptor trigger zone is NOT the left
gigantocellular reticular nucleus (Gi).** The **left
gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/left/``)
is a **left medullary reticular** nucleus. The **left CTZ**
(here) is a **left-aspect** of the **circumventricular organ's
functional role** — **NOT** a reticular nucleus. Consumers must
**not** conflate the two.
**Boundary status (NOT the fourth ventricle — the fourth
ventricle is a CSF cavity, the CTZ is a CSF-sensing functional
role at its floor):** **Boundary case — the left chemoreceptor
trigger zone is NOT the fourth ventricle.** The **fourth
ventricle** (``.../metencephalon/fourth_ventricle/``) is a **CSF
cavity** — **NOT** a grey-matter structure. The **left CTZ**
(here) is a **left-aspect** of the **functional role** of the
**organ** that **lines the caudal fourth ventricle floor**.
Consumers must **not** conflate the **functional role** with
the **cavity**.
**Boundary status (NOT the whole respiratory_center or whole
medulla oblongata — a leaf in a chain of containers):**
**Boundary case — the left chemoreceptor trigger zone is NOT
the whole respiratory_center or the whole medulla oblongata.**
It is a **leaf** at the **bottom** of a **chain** of containers:
``medulla_oblongata`` → ``respiratory_center`` →
``chemoreceptor_trigger_zone`` → ``left``. Consumers must **not**
conflate the **leaf** with **any of the parent containers**.

Overview
--------
The **left chemoreceptor trigger zone** is, **in this tree**, the
**left-side aspect** of the **midline chemoreceptor trigger
zone** — the **functional role** of the **midline area
postrema** for **blood-borne / CSF-borne emetic detection** and
**chemoreception**. **Anatomically**, there is **only one CTZ**
— a **single, unpaired, midline** functional role of the
**single, unpaired, midline** area postrema. The ``left`` /
``right`` split is a **tree-wiring convention** (consistent with
the rest of the medulla oblongata children) — **NOT** an
anatomical claim that the CTZ is **bilaterally paired**.

**This is a LEAF module.** The **left CTZ** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution use this
module; consumers that need **the whole functional role** use
``.../chemoreceptor_trigger_zone/`` (the container); consumers
that need the **anatomical structure** use
``.../area_postrema/`` (the twin container).

**The left CTZ is a CIRCUMVENTRICULAR ORGAN's functional role,
NOT a respiratory nucleus.** Although wired under
``respiratory_center``, its **primary function** is
**chemoreception / emesis / autonomic regulation** — **NOT**
**breathing**. The **"respiratory_center"** label is a
**tree-wiring artifact** — the tree groups the CTZ (and the area
postrema, and the dorsal column nuclei) as a **pragmatic
cluster**. Consumers must **not** infer **respiratory function**
from **container membership**.

**The left CTZ is the SAME PHYSICAL STRUCTURE as the left area
postrema — under a DIFFERENT NAME.** The **CTZ** is the
**functional role**; the **area postrema** is the **anatomical
structure**. **The tree separates the two names into two modules
as a deliberate wiring choice** — consumers must **not conflate
the two modules within the tree**, **and must not conclude** that
**wiring separation** implies **anatomical separation** — the
**underlying structure** is **one**.

**The left CTZ is the LEFTWARD ASPECT of a MIDLINE functional
role.** It is **functionally and anatomically identical** to the
**right CTZ** (they are two aspects of the same functional role,
not two separate functional roles). Consumers must **not** assume
**laterality** or **functional asymmetry** between the two.

The Left Chemoreceptor Trigger Zone / Right Chemoreceptor Trigger Zone Boundary
------------------------------------------------------------------------------
This is the **aspect / aspect** boundary (within the same
midline functional role):

*   **Left CTZ** (this module) — the **left-side aspect** of the
    **midline CTZ**.

*   **Right CTZ** (``.../chemoreceptor_trigger_zone/right/``) —
    the **right-side aspect** of the **midline CTZ**.

**They are DIFFERENT LEAVES** — the ``left`` and ``right``
modules are the two sides of the **bilateral container**. **In
the brain, there is ONE CTZ** — the **left** and **right**
leaves are **tree-wiring aspects** of the **same midline
functional role**, **NOT** two separate functional roles.
Consumers must **not** infer **anatomical bilaterality** from
the tree structure.

The Left Chemoreceptor Trigger Zone / Whole Chemoreceptor Trigger Zone Boundary
------------------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Left CTZ** (this module) — the **left-side aspect**.

*   **Whole CTZ** (``.../chemoreceptor_trigger_zone/``) — the
    **bilateral container** of the **midline functional role**.

**The left CTZ is an ASPECT of the whole CTZ.** Consumers must
**not** conflate the **leaf** with the **container**.

The Left Chemoreceptor Trigger Zone / Left Area Postrema Boundary
-----------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Left CTZ** (this module) — the **left-side aspect** of the
    **functional role** (chemoreception / emetic trigger).

*   **Left area postrema**
    (``.../respiratory_center/area_postrema/left/``) — the
    **left-side aspect** of the **anatomical structure**.

**They refer to the SAME PHYSICAL STRUCTURE in the literature**
— the **left CTZ** is the **left functional role**; the **left
area postrema** is the **left anatomical structure**. **The tree
separates the two names into two modules as a deliberate wiring
choice.** Consumers must **not** conflate the two leaves **within
the tree** — resolve the **left area postrema** via
``respiratory_center.area_postrema.left`` and the **left CTZ**
via ``respiratory_center.chemoreceptor_trigger_zone.left``.
**Consumers must also not conclude** that **wiring separation**
implies **anatomical separation** — the **underlying structure**
is **one**.

The Left Chemoreceptor Trigger Zone / Left Solitary Nucleus Boundary
--------------------------------------------------------------------
This is the **sensor / relay** boundary:

*   **Left CTZ** (this module) — the **left-side aspect** of the
    **circumventricular chemosensory** functional role.

*   **Left solitary nucleus (NTS)**
    (``.../solitary_nucleus/left/``) — the **left visceral
    afferent relay**.

**The left CTZ PROJECTS TO the left NTS** — the NTS is the
**downstream target** of the CTZ's **emetic and autonomic**
signals. **They are DIFFERENT STRUCTURES** — the **CTZ** is the
**sensor's functional role**; the **NTS** is the **relay**.
Consumers must **not** conflate the two.

The Left Chemoreceptor Trigger Zone / Left Dorsal Motor Nucleus of the Vagus and Left Hypoglossal Nucleus Boundary
-----------------------------------------------------------------------------------------------------------------
This is the **circumventricular / motor** boundary:

*   **Left CTZ** (this module) — the **left-side aspect** of
    the **circumventricular organ's functional role**.

*   **Left dorsal motor nucleus of the vagus**
    (``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``)
    — the **left parasympathetic** nucleus.

*   **Left hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) —
    the **left somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the two.

The Left Chemoreceptor Trigger Zone / Other Left Respiratory Center Children Boundary
------------------------------------------------------------------------------------
This is the **circumventricular / respiratory-and-somatosensory**
boundary:

*   **Left CTZ** (this module) — the **left-side aspect** of the
    **circumventricular organ's functional role**.

*   **Left dorsal respiratory group**
    (``.../respiratory_center/dorsal_respiratory_group/left/``)
    — the **left dorsal respiratory** pattern generator.

*   **Left gigantocellular reticular nucleus**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/left/``)
    — the **left medullary reticular** nucleus.

*   **Left cuneate nucleus**
    (``.../respiratory_center/cuneate_nucleus/left/``) — the
    **left dorsal column somatosensory** relay (upper body).

*   **Left gracile nucleus**
    (``.../respiratory_center/gracile_nucleus/left/``) — the
    **left dorsal column somatosensory** relay (lower body).

**They are DIFFERENT STRUCTURES** — all are **leaves** of
``respiratory_center``'s children, but they are **functionally
distinct**. Consumers must **not** conflate the **left CTZ**
with any of these.

The Left Chemoreceptor Trigger Zone / Fourth Ventricle Boundary
--------------------------------------------------------------
This is the **functional role / cavity** boundary:

*   **Left CTZ** (this module) — the **left-side aspect** of the
    **circumventricular organ's functional role** at the
    **caudal fourth ventricle floor**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the **CSF
    cavity**.

**The left CTZ is at the FLOOR of the fourth ventricle** — but
it is **NOT** the fourth ventricle itself. Consumers must **not**
conflate the **functional role** with the **cavity**.

Function in the Human Brain
---------------------------
The left chemoreceptor trigger zone's functions are
**chemoreception**, **emesis**, **autonomic regulation**,
**fluid balance**, and **immune-neural signaling** — **NOT
respiratory rhythm** and **NOT motor control** — **and it is
functionally identical to the right CTZ** (they are two aspects
of the same midline functional role):

*   **Chemoreception (blood-borne and CSF-borne signals):** The
    **CTZ** — the **functional role** of the **area postrema** —
    **senses blood-borne and CSF-borne substances** (toxins,
    emetics, hormones, cytokines) via the **fenestrated
    capillaries** and **CSF-facing surface** of the **area
    postrema**.

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

**The unifying theme:** the left CTZ is the **left-side aspect**
of the **circumventricular chemosensory** functional role — a
**chemosensory**, **emetic**, **autonomic**, **fluid-balance**,
and **immune-neural** functional role — **NOT** a respiratory
nucleus, **NOT** the NTS, **NOT** the dorsal motor nucleus of
the vagus, **NOT** the fourth ventricle, and **NOT** the area
postrema (in this tree).

Associated Disorders
--------------------
The left chemoreceptor trigger zone's clinical relevance is
**identical** to the **right CTZ** and to the **area
postrema's** — the **CTZ** is the **functional role** of the
**area postrema**, so the **clinical syndromes** are **not
lateralized**:

*   **Chemotherapy-induced nausea and vomiting (CINV — via CTZ /
    AP):** **Chemotherapy agents** **stimulate** the **CTZ**
    — triggering **nausea** and **vomiting** via **NTS** and
    **parabrachial** projections. **5-HT3 receptor antagonists**
    (e.g., **ondansetron**) and **NK1 receptor antagonists**
    (e.g., **aprepitant**) **target** the **CTZ / NTS** pathway
    to **prevent** **CINV**.

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

*   **No Named "Left Chemoreceptor Trigger Zone Syndrome":** The
    left CTZ is **not a functionally separate structure** from
    the right CTZ — it is the **left aspect** of the **same
    midline functional role**. There is **no named "left CTZ
    syndrome"** — the clinical syndromes are **named for the
    area postrema** (e.g., **area postrema syndrome** in NMOSD)
    or **for the function** (CINV, drug-induced emesis), **not**
    for the CTZ itself and **not** lateralized.

**What is NOT here:** The left CTZ is **not** the substrate for
**central hypoventilation** (VRG, pre-Bötzinger complex),
**sympathetic premotor** function (RVLM), **visceral afferent
relay** (NTS), **tongue weakness** (hypoglossal nucleus), or
**parasympathetic dysfunction** (dorsal motor nucleus of the
vagus). Its clinical relevance is the **emesis**, **autonomic**,
and **immune-neural** functions listed above — **not
lateralized** because the CTZ is a **midline functional role**.

Lateralization Notes
--------------------
This is the **left** CTZ module — the **left-side aspect** of the
**midline chemoreceptor trigger zone**. The CTZ is a **bilateral
container** in this tree whose two sides represent the **same
midline functional role** — and it carries **NO warning**:

*   **Tree-wiring convention, NOT anatomical bilaterality:** The
    **left** and **right** leaves are **aspects** of the **same
    midline** CTZ — **NOT** two separate functional roles. The
    **left / right split** is a **tree-wiring convention** —
    consistent with the rest of the medulla oblongata children.
    The **human CTZ** (the area postrema's functional role) is a
    **single, unpaired, midline** functional role.

*   **NO lateralization:** The CTZ has **no known functional
    lateralization** — it is a **midline** functional role with
    **no left / right functional difference**. Consumers must
    **not** import a **lateralization warning** into the left
    CTZ — the **left** and **right** sides are **functionally
    identical** and **anatomically the same** functional role.

*   **NO Extended-Amygdala / SLEA Warning:** The left CTZ is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into the left
    CTZ.

*   **NO Fear-Output Warning:** The left CTZ is **not** a
    fear-output structure — it is a **circumventricular
    chemosensory** functional role aspect. Consumers must **not**
    conflate it with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "left CTZ = right CTZ" will be
structurally correct** — the two sides are **equivalent** (they
represent the **same midline** functional role). The CTZ is a
**strict-mirror container with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left CTZ is a **leaf** —
    it does **not** import from ``.../right/`` or any other
    right-side module. The **left / right split** is a
    **tree-wiring convention** — not an anatomical bilaterality.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../area_postrema/``,
    ``.../dorsal_respiratory_group/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../metencephalon/fourth_ventricle/``, or any other
    container. The left CTZ's relationships to the left area
    postrema, left dorsal respiratory group, left gigantocellular
    reticular nucleus, left cuneate nucleus, left gracile
    nucleus, left solitary nucleus, left dorsal motor nucleus of
    the vagus, left hypoglossal nucleus, and the fourth ventricle
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left CTZ is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../left/``.
*   **WIRING CONVENTION, NOT anatomical bilaterality.** The
    ``left`` module is an **aspect** of the **midline** CTZ —
    **NOT** a separate functional role. The **human CTZ** is a
    **single, unpaired, midline** functional role.
*   **NOT the right CTZ.** The right CTZ is a **separate leaf**
    under ``.../chemoreceptor_trigger_zone/right/``. Consumers
    must **not** conflate the left with the right — they
    represent the **same midline** functional role.
*   **FUNCTIONAL ROLE, NOT an anatomical structure.** The CTZ is
    the **functional role** of the **area postrema** — the
    **two names** refer to the **same physical structure** from
    **two different perspectives**. The **tree separates the two
    names into two modules** as a **deliberate wiring choice** —
    consumers must **not** conflate the **modules within the
    tree**, **and must not conclude** that **wiring separation**
    implies **anatomical separation**.
*   **NOT the left area postrema (in this tree — the same
    structure under a different name, wired as a separate
    child).** The **left area postrema** is a **separate leaf**
    under ``.../respiratory_center/area_postrema/left/`` —
    consumers must **not** conflate the two leaves **within the
    tree**, even though they refer to the **same physical
    structure**.
*   **CIRCUMVENTRICULAR ORGAN's functional role, NOT a
    respiratory nucleus.** Although wired under
    ``respiratory_center``, the CTZ is a **chemoreceptive /
    emetic / autonomic / immune-neural** functional role —
    **NOT** a respiratory rhythm generator.
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
*   **NOT the whole CTZ, whole respiratory_center, or whole
    medulla oblongata.** The left CTZ is a **leaf** in a
    **chain** of containers.
*   **No ``AREA_PATHS`` hop.** The left CTZ is a **local leaf** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The left CTZ has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the right CTZ — strict mirror with
    NO warning.** The left and right modules are **structurally
    identical** — same leaf status, same **circumventricular
    functional role aspect** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.chemoreceptor_trigger_zone.left"
    )

**Do not** assume the left CTZ is a **separate functional role**
from the right CTZ. **Anatomically**, there is **ONE CTZ** — the
``left`` / ``right`` split is a **tree-wiring convention**,
**NOT** an anatomical bilaterality.

**Do not** assume the left CTZ is the **left area postrema** in
this tree. They are **separate leaves** under **different
children** of ``respiratory_center`` — even though they refer to
the **same physical structure**. **Consumers must not conclude**
that **wiring separation** implies **anatomical separation**.

**Do not** assume the left CTZ is the **left solitary nucleus
(NTS)**. The NTS is a **separate container** — the CTZ
**projects to** the NTS, but is **NOT** the NTS itself.

**Do not** assume the left CTZ is the **left dorsal motor
nucleus of the vagus**, the **left hypoglossal nucleus**, the
**left dorsal respiratory group**, the **left gigantocellular
reticular nucleus**, the **left cuneate nucleus**, or the
**left gracile nucleus**. Each is a **different structure**.

**Do not** assume the left CTZ is the **fourth ventricle**. The
fourth ventricle is a **CSF cavity**; the CTZ is the
**functional role** of the **organ** at its **caudal floor**.

**Do not** assume the left CTZ is the **whole CTZ**, the
**whole respiratory_center**, or the **whole medulla oblongata**.
It is a **leaf** in a **chain** of containers.

**Do not** assume the left CTZ has **structural children**. It
is a **leaf** — it represents the **left-side aspect** of the
**midline CTZ** as a **single structure**.

Iterating the left CTZ's (empty) children (recommended consumer
pattern)::

    LEFT_CHEMORECEPTOR_TRIGGER_ZONE_CHILDREN = ()
    # The left CTZ is a leaf. It has no structural children.
    # Anatomically, the CTZ is a SINGLE midline structure — the
    # left/right split is a tree-wiring convention.

Reaching the right CTZ (recommended consumer pattern — the
contralateral leaf, representing the SAME midline structure)::

    # The right CTZ is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.right
    #
    # The left and right CTZ leaves are ASPECTS of the SAME
    # midline structure — NOT two separate functional roles.

Reaching the whole CTZ container (recommended consumer pattern —
for consumers that need the whole functional role)::

    # The whole CTZ is the PARENT container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone
    #
    # Consumers that need the WHOLE CTZ should use the parent
    # container, not the left or right leaf.

Reaching the left area postrema (recommended consumer pattern —
NOTE the DIFFERENT leaf, the SAME physical structure under a
DIFFERENT name, wired as a SEPARATE child in this tree)::

    # The left area postrema is a SEPARATE leaf under a DIFFERENT
    # child of respiratory_center in this tree — even though the
    # literature often treats the AP and the CTZ as synonymous:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.left
    #
    # The AP is the ANATOMICAL STRUCTURE; the CTZ is the
    # FUNCTIONAL ROLE — the tree separates them into TWO MODULES
    # as a deliberate wiring choice. Consumers must NOT conflate
    # the two leaves within the tree, AND must NOT conclude that
    # wiring separation implies anatomical separation — the
    # underlying structure is ONE.

Reaching the left solitary nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The left solitary nucleus (NTS) is a SEPARATE container
    # under medulla_oblongata — the CTZ PROJECTS to the NTS, but
    # is NOT the NTS itself:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
    #
    # The CTZ / AP is the CHEMOSENSORY functional role; the NTS
    # is the VISCERAL AFFERENT relay.

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