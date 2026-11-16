"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.right
=======================================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── chemoreceptor_trigger_zone
                    └── right   <-- THIS MODULE

**Primary synonym:** Right chemoreceptor trigger zone; right CTZ;
right aspect of the chemoreceptor trigger zone; right aspect of
the area postrema's functional role.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**circumventricular organ's functional role** — in **this tree**,
the **right leaf** representing the **right-side aspect** of the
**midline chemoreceptor trigger zone**. The **CTZ** is the
**functional role** of the **area postrema** (chemoreception /
emetic trigger); **anatomically**, the **CTZ is the area
postrema** — a **single, unpaired, midline** circumventricular
organ at the **caudal floor of the fourth ventricle**. The
``right`` module is a **tree-wiring convention** — **NOT** an
anatomical claim that there is a **separate right CTZ**.
**Part of:** The **chemoreceptor_trigger_zone** bilateral
container
(``.../respiratory_center/chemoreceptor_trigger_zone/``) — which
is part of the **respiratory_center** — which is part of the
**medulla oblongata** — the **caudal brainstem** subdivision of
the **myelencephalon**.
**Structural parent:** ``.../chemoreceptor_trigger_zone/`` →
**direct child** of the chemoreceptor_trigger_zone container.
The **right** leaf is one of the **two** structural children of
the container (the other is ``left``).
**Structural children:** **None.** This is a **leaf** module. The
right CTZ is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the left chemoreceptor trigger zone —
the contralateral leaf, both representing the SAME midline
structure):** **Boundary case — the right chemoreceptor trigger
zone is NOT the left chemoreceptor trigger zone.** The **left
chemoreceptor trigger zone**
(``.../chemoreceptor_trigger_zone/left/``) is the
**contralateral leaf** — the **left-side aspect** of the
**same midline CTZ**. **They are DIFFERENT LEAVES** — the
``right`` and ``left`` modules are the two sides of the
**bilateral container**. **In the brain, there is ONE CTZ** —
the **right** and **left** leaves are **tree-wiring aspects**
of the **same midline structure**, **NOT** two separate
functional roles. Consumers must **not** infer **anatomical
bilaterality** from the tree structure.
**Boundary status (NOT the whole chemoreceptor trigger zone — an
ASPECT of it):** **Boundary case — the right chemoreceptor
trigger zone is NOT the whole chemoreceptor trigger zone.** The
**whole chemoreceptor trigger zone**
(``.../chemoreceptor_trigger_zone/``) is the **bilateral
container** that **contains** the right CTZ (here) **plus** the
left CTZ. The **right** module is **one aspect** — the
**right-side aspect** — of the **midline CTZ**. Consumers must
**not** conflate the **leaf** with the **container**.
**Boundary status (NOT the right area postrema leaf — the SAME
structure under a DIFFERENT name, wired as a SEPARATE child in
this tree):** **Boundary case — the right chemoreceptor trigger
zone is NOT the right area postrema in this tree.** In the
**literature**, the **chemoreceptor trigger zone** and the
**area postrema** are **often used interchangeably** — they are
**largely considered the same structure** — the **CTZ** is the
**functional role** of the **area postrema** for
**blood-borne / CSF-borne emetic detection**. **In this tree**,
they are **wired as two separate child containers** of
``respiratory_center``:
``respiratory_center.chemoreceptor_trigger_zone`` (this module's
parent) and ``respiratory_center.area_postrema``. The
**corresponding right leaf** of the area postrema is at
``.../respiratory_center/area_postrema/right/``. **They refer to
the SAME PHYSICAL STRUCTURE** (right aspect of the midline area
postrema) under **two different names**. Consumers must **not**
conflate the two leaves **within the tree** — resolve the
**right area postrema** via
``respiratory_center.area_postrema.right`` and the **right CTZ**
via ``respiratory_center.chemoreceptor_trigger_zone.right``.
**Consumers must also not conclude** that **wiring separation**
implies **anatomical separation** — the **underlying structure**
is **one**.
**Boundary status (NOT the right solitary nucleus — a DIFFERENT
structure in a DIFFERENT container):** **Boundary case — the
right chemoreceptor trigger zone is NOT the right solitary
nucleus (NTS).** The **right solitary nucleus**
(``.../solitary_nucleus/right/``) is the **right visceral
afferent relay** — it is a **separate structure** in a
**separate container**. The **right CTZ** (here) is a
**right-aspect** of the **circumventricular organ's functional
role** that **projects to** the NTS. **They are DIFFERENT
STRUCTURES** — the **CTZ** is the **sensor's functional role**;
the **NTS** is the **relay**. Consumers must **not** conflate
the two.
**Boundary status (NOT the right dorsal motor nucleus of the
vagus — a DIFFERENT structure with a DIFFERENT function):**
**Boundary case — the right chemoreceptor trigger zone is NOT
the right dorsal motor nucleus of the vagus.** The **right
dorsal motor nucleus of the vagus**
(``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
is the **right parasympathetic** nucleus. The **right CTZ**
(here) is a **right-aspect** of the **circumventricular
organ's functional role** — **NOT** a parasympathetic nucleus.
They are **anatomically adjacent** at the **caudal fourth
ventricle floor**, but they are **functionally distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right hypoglossal nucleus — a
DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the right chemoreceptor trigger zone is NOT the right
hypoglossal nucleus.** The **right hypoglossal nucleus**
(``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is the
**right somatic motor** nucleus for the **tongue**. The **right
CTZ** (here) is a **right-aspect** of the **circumventricular
organ's functional role** — **NOT** a motor nucleus. Consumers
must **not** conflate the two.
**Boundary status (NOT the right dorsal respiratory group — a
DIFFERENT child of respiratory_center):** **Boundary case — the
right chemoreceptor trigger zone is NOT the right dorsal
respiratory group (DRG).** The **right dorsal respiratory group**
(``.../respiratory_center/dorsal_respiratory_group/right/``) is
the **right dorsal respiratory** pattern generator — **NOT** a
circumventricular functional role. Both are **leaves** under
different children of ``respiratory_center``, but they are
**functionally distinct** — the **DRG** is **respiratory**; the
**CTZ** is **circumventricular / chemosensory**. Consumers must
**not** conflate the two.
**Boundary status (NOT the right cuneate or right gracile
nucleus — DIFFERENT children of respiratory_center):**
**Boundary case — the right chemoreceptor trigger zone is NOT
the right cuneate or right gracile nucleus.** The **right
cuneate nucleus**
(``.../respiratory_center/cuneate_nucleus/right/``) and **right
gracile nucleus**
(``.../respiratory_center/gracile_nucleus/right/``) are the
**right dorsal column somatosensory relays**. The **right CTZ**
(here) is a **right-aspect** of the **circumventricular organ's
functional role** — **NOT** a somatosensory relay. Consumers
must **not** conflate them.
**Boundary status (NOT the right gigantocellular reticular
nucleus — a DIFFERENT child of respiratory_center):** **Boundary
case — the right chemoreceptor trigger zone is NOT the right
gigantocellular reticular nucleus (Gi).** The **right
gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/right/``)
is a **right medullary reticular** nucleus. The **right CTZ**
(here) is a **right-aspect** of the **circumventricular organ's
functional role** — **NOT** a reticular nucleus. Consumers must
**not** conflate the two.
**Boundary status (NOT the fourth ventricle — the fourth
ventricle is a CSF cavity, the CTZ is a CSF-sensing functional
role at its floor):** **Boundary case — the right chemoreceptor
trigger zone is NOT the fourth ventricle.** The **fourth
ventricle** (``.../metencephalon/fourth_ventricle/``) is a **CSF
cavity** — **NOT** a grey-matter structure. The **right CTZ**
(here) is a **right-aspect** of the **functional role** of the
**organ** that **lines the caudal fourth ventricle floor**.
Consumers must **not** conflate the **functional role** with
the **cavity**.
**Boundary status (NOT the whole respiratory_center or whole
medulla oblongata — a leaf in a chain of containers):**
**Boundary case — the right chemoreceptor trigger zone is NOT
the whole respiratory_center or the whole medulla oblongata.**
It is a **leaf** at the **bottom** of a **chain** of containers:
``medulla_oblongata`` → ``respiratory_center`` →
``chemoreceptor_trigger_zone`` → ``right``. Consumers must **not**
conflate the **leaf** with **any of the parent containers**.

Overview
--------
The **right chemoreceptor trigger zone** is, **in this tree**, the
**right-side aspect** of the **midline chemoreceptor trigger
zone** — the **functional role** of the **midline area
postrema** for **blood-borne / CSF-borne emetic detection** and
**chemoreception**. **Anatomically**, there is **only one CTZ**
— a **single, unpaired, midline** functional role of the
**single, unpaired, midline** area postrema. The ``right`` /
``left`` split is a **tree-wiring convention** (consistent with
the rest of the medulla oblongata children) — **NOT** an
anatomical claim that the CTZ is **bilaterally paired**.

**This is a LEAF module.** The **right CTZ** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution use this
module; consumers that need **the whole functional role** use
``.../chemoreceptor_trigger_zone/`` (the container); consumers
that need the **anatomical structure** use
``.../area_postrema/`` (the twin container).

**The right CTZ is a CIRCUMVENTRICULAR ORGAN's functional role,
NOT a respiratory nucleus.** Although wired under
``respiratory_center``, its **primary function** is
**chemoreception / emesis / autonomic regulation** — **NOT**
**breathing**. The **"respiratory_center"** label is a
**tree-wiring artifact** — the tree groups the CTZ (and the area
postrema, and the dorsal column nuclei) as a **pragmatic
cluster**. Consumers must **not** infer **respiratory function**
from **container membership**.

**The right CTZ is the SAME PHYSICAL STRUCTURE as the right area
postrema — under a DIFFERENT NAME.** The **CTZ** is the
**functional role**; the **area postrema** is the **anatomical
structure**. **The tree separates the two names into two modules
as a deliberate wiring choice** — consumers must **not conflate
the two modules within the tree**, **and must not conclude** that
**wiring separation** implies **anatomical separation** — the
**underlying structure** is **one**.

**The right CTZ is the RIGHTWARD ASPECT of a MIDLINE functional
role.** It is **functionally and anatomically identical** to the
**left CTZ** (they are two aspects of the same functional role,
not two separate functional roles). Consumers must **not** assume
**laterality** or **functional asymmetry** between the two.

The Right Chemoreceptor Trigger Zone / Left Chemoreceptor Trigger Zone Boundary
------------------------------------------------------------------------------
This is the **aspect / aspect** boundary (within the same
midline functional role):

*   **Right CTZ** (this module) — the **right-side aspect** of
    the **midline CTZ**.

*   **Left CTZ** (``.../chemoreceptor_trigger_zone/left/``) —
    the **left-side aspect** of the **midline CTZ**.

**They are DIFFERENT LEAVES** — the ``right`` and ``left``
modules are the two sides of the **bilateral container**. **In
the brain, there is ONE CTZ** — the **right** and **left**
leaves are **tree-wiring aspects** of the **same midline
functional role**, **NOT** two separate functional roles.
Consumers must **not** infer **anatomical bilaterality** from
the tree structure.

The Right Chemoreceptor Trigger Zone / Whole Chemoreceptor Trigger Zone Boundary
-------------------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Right CTZ** (this module) — the **right-side aspect**.

*   **Whole CTZ** (``.../chemoreceptor_trigger_zone/``) — the
    **bilateral container** of the **midline functional role**.

**The right CTZ is an ASPECT of the whole CTZ.** Consumers must
**not** conflate the **leaf** with the **container**.

The Right Chemoreceptor Trigger Zone / Right Area Postrema Boundary
-------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Right CTZ** (this module) — the **right-side aspect** of
    the **functional role** (chemoreception / emetic trigger).

*   **Right area postrema**
    (``.../respiratory_center/area_postrema/right/``) — the
    **right-side aspect** of the **anatomical structure**.

**They refer to the SAME PHYSICAL STRUCTURE in the literature**
— the **right CTZ** is the **right functional role**; the
**right area postrema** is the **right anatomical structure**.
**The tree separates the two names into two modules as a
deliberate wiring choice.** Consumers must **not** conflate the
two leaves **within the tree** — resolve the **right area
postrema** via ``respiratory_center.area_postrema.right`` and
the **right CTZ** via
``respiratory_center.chemoreceptor_trigger_zone.right``.
**Consumers must also not conclude** that **wiring separation**
implies **anatomical separation** — the **underlying structure**
is **one**.

The Right Chemoreceptor Trigger Zone / Right Solitary Nucleus Boundary
---------------------------------------------------------------------
This is the **sensor / relay** boundary:

*   **Right CTZ** (this module) — the **right-side aspect** of
    the **circumventricular chemosensory** functional role.

*   **Right solitary nucleus (NTS)**
    (``.../solitary_nucleus/right/``) — the **right visceral
    afferent relay**.

**The right CTZ PROJECTS TO the right NTS** — the NTS is the
**downstream target** of the CTZ's **emetic and autonomic**
signals. **They are DIFFERENT STRUCTURES** — the **CTZ** is the
**sensor's functional role**; the **NTS** is the **relay**.
Consumers must **not** conflate the two.

The Right Chemoreceptor Trigger Zone / Right Dorsal Motor Nucleus of the Vagus and Right Hypoglossal Nucleus Boundary
---------------------------------------------------------------------------------------------------------------------
This is the **circumventricular / motor** boundary:

*   **Right CTZ** (this module) — the **right-side aspect** of
    the **circumventricular organ's functional role**.

*   **Right dorsal motor nucleus of the vagus**
    (``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
    — the **right parasympathetic** nucleus.

*   **Right hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **right somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the two.

The Right Chemoreceptor Trigger Zone / Other Right Respiratory Center Children Boundary
--------------------------------------------------------------------------------------
This is the **circumventricular / respiratory-and-somatosensory**
boundary:

*   **Right CTZ** (this module) — the **right-side aspect** of
    the **circumventricular organ's functional role**.

*   **Right dorsal respiratory group**
    (``.../respiratory_center/dorsal_respiratory_group/right/``)
    — the **right dorsal respiratory** pattern generator.

*   **Right gigantocellular reticular nucleus**
    (``.../respiratory_center/gigantocellular_reticular_nucleus/right/``)
    — the **right medullary reticular** nucleus.

*   **Right cuneate nucleus**
    (``.../respiratory_center/cuneate_nucleus/right/``) — the
    **right dorsal column somatosensory** relay (upper body).

*   **Right gracile nucleus**
    (``.../respiratory_center/gracile_nucleus/right/``) — the
    **right dorsal column somatosensory** relay (lower body).

**They are DIFFERENT STRUCTURES** — all are **leaves** of
``respiratory_center``'s children, but they are **functionally
distinct**. Consumers must **not** conflate the **right CTZ**
with any of these.

The Right Chemoreceptor Trigger Zone / Fourth Ventricle Boundary
----------------------------------------------------------------
This is the **functional role / cavity** boundary:

*   **Right CTZ** (this module) — the **right-side aspect** of
    the **circumventricular organ's functional role** at the
    **caudal fourth ventricle floor**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the **CSF
    cavity**.

**The right CTZ is at the FLOOR of the fourth ventricle** — but
it is **NOT** the fourth ventricle itself. Consumers must **not**
conflate the **functional role** with the **cavity**.

Function in the Human Brain
---------------------------
The right chemoreceptor trigger zone's functions are
**chemoreception**, **emesis**, **autonomic regulation**,
**fluid balance**, and **immune-neural signaling** — **NOT
respiratory rhythm** and **NOT motor control** — **and it is
functionally identical to the left CTZ** (they are two aspects
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

**The unifying theme:** the right CTZ is the **right-side aspect**
of the **circumventricular chemosensory** functional role — a
**chemosensory**, **emetic**, **autonomic**, **fluid-balance**,
and **immune-neural** functional role — **NOT** a respiratory
nucleus, **NOT** the NTS, **NOT** the dorsal motor nucleus of
the vagus, **NOT** the fourth ventricle, and **NOT** the area
postrema (in this tree).

Associated Disorders
--------------------
The right chemoreceptor trigger zone's clinical relevance is
**identical** to the **left CTZ** and to the **area
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

*   **No Named "Right Chemoreceptor Trigger Zone Syndrome":** The
    right CTZ is **not a functionally separate structure** from
    the left CTZ — it is the **right aspect** of the **same
    midline functional role**. There is **no named "right CTZ
    syndrome"** — the clinical syndromes are **named for the
    area postrema** (e.g., **area postrema syndrome** in NMOSD)
    or **for the function** (CINV, drug-induced emesis), **not**
    for the CTZ itself and **not** lateralized.

**What is NOT here:** The right CTZ is **not** the substrate for
**central hypoventilation** (VRG, pre-Bötzinger complex),
**sympathetic premotor** function (RVLM), **visceral afferent
relay** (NTS), **tongue weakness** (hypoglossal nucleus), or
**parasympathetic dysfunction** (dorsal motor nucleus of the
vagus). Its clinical relevance is the **emesis**, **autonomic**,
and **immune-neural** functions listed above — **not
lateralized** because the CTZ is a **midline functional role**.

Lateralization Notes
--------------------
This is the **right** CTZ module — the **right-side aspect** of
the **midline chemoreceptor trigger zone**. The CTZ is a
**bilateral container** in this tree whose two sides represent
the **same midline functional role** — and it carries **NO
warning**:

*   **Tree-wiring convention, NOT anatomical bilaterality:** The
    **right** and **left** leaves are **aspects** of the **same
    midline** CTZ — **NOT** two separate functional roles. The
    **right / left split** is a **tree-wiring convention** —
    consistent with the rest of the medulla oblongata children.
    The **human CTZ** (the area postrema's functional role) is a
    **single, unpaired, midline** functional role.

*   **NO lateralization:** The CTZ has **no known functional
    lateralization** — it is a **midline** functional role with
    **no left / right functional difference**. Consumers must
    **not** import a **lateralization warning** into the right
    CTZ — the **right** and **left** sides are **functionally
    identical** and **anatomically the same** functional role.

*   **NO Extended-Amygdala / SLEA Warning:** The right CTZ is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into the right
    CTZ.

*   **NO Fear-Output Warning:** The right CTZ is **not** a
    fear-output structure — it is a **circumventricular
    chemosensory** functional role aspect. Consumers must **not**
    conflate it with the **central nucleus** or with the
    **amygdala**.

**A consumer that assumes "right CTZ = left CTZ" will be
structurally correct** — the two sides are **equivalent** (they
represent the **same midline** functional role). The CTZ is a
**strict-mirror container with NO warning** — **no SLEA
warning**, **no fear-output warning**, and **no lateralization
warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right CTZ is a **leaf** —
    it does **not** import from ``.../left/`` or any other
    left-side module. The **right / left split** is a
    **tree-wiring convention** — not an anatomical bilaterality.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../area_postrema/``,
    ``.../dorsal_respiratory_group/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../metencephalon/fourth_ventricle/``, or any other
    container. The right CTZ's relationships to the right area
    postrema, right dorsal respiratory group, right
    gigantocellular reticular nucleus, right cuneate nucleus,
    right gracile nucleus, right solitary nucleus, right dorsal
    motor nucleus of the vagus, right hypoglossal nucleus, and
    the fourth ventricle are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right CTZ is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../right/``.
*   **WIRING CONVENTION, NOT anatomical bilaterality.** The
    ``right`` module is an **aspect** of the **midline** CTZ —
    **NOT** a separate functional role. The **human CTZ** is a
    **single, unpaired, midline** functional role.
*   **NOT the left CTZ.** The left CTZ is a **separate leaf**
    under ``.../chemoreceptor_trigger_zone/left/``. Consumers
    must **not** conflate the right with the left — they
    represent the **same midline** functional role.
*   **FUNCTIONAL ROLE, NOT an anatomical structure.** The CTZ is
    the **functional role** of the **area postrema** — the
    **two names** refer to the **same physical structure** from
    **two different perspectives**. The **tree separates the two
    names into two modules** as a **deliberate wiring choice** —
    consumers must **not** conflate the **modules within the
    tree**, **and must not conclude** that **wiring separation**
    implies **anatomical separation**.
*   **NOT the right area postrema (in this tree — the same
    structure under a different name, wired as a separate
    child).** The **right area postrema** is a **separate leaf**
    under ``.../respiratory_center/area_postrema/right/`` —
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
    medulla oblongata.** The right CTZ is a **leaf** in a
    **chain** of containers.
*   **No ``AREA_PATHS`` hop.** The right CTZ is a **local leaf** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The right CTZ has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the left CTZ — strict mirror with
    NO warning.** The right and left modules are **structurally
    identical** — same leaf status, same **circumventricular
    functional role aspect** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.chemoreceptor_trigger_zone.right"
    )

**Do not** assume the right CTZ is a **separate functional role**
from the left CTZ. **Anatomically**, there is **ONE CTZ** — the
``right`` / ``left`` split is a **tree-wiring convention**,
**NOT** an anatomical bilaterality.

**Do not** assume the right CTZ is the **right area postrema** in
this tree. They are **separate leaves** under **different
children** of ``respiratory_center`` — even though they refer to
the **same physical structure**. **Consumers must not conclude**
that **wiring separation** implies **anatomical separation**.

**Do not** assume the right CTZ is the **right solitary nucleus
(NTS)**. The NTS is a **separate container** — the CTZ
**projects to** the NTS, but is **NOT** the NTS itself.

**Do not** assume the right CTZ is the **right dorsal motor
nucleus of the vagus**, the **right hypoglossal nucleus**, the
**right dorsal respiratory group**, the **right gigantocellular
reticular nucleus**, the **right cuneate nucleus**, or the
**right gracile nucleus**. Each is a **different structure**.

**Do not** assume the right CTZ is the **fourth ventricle**. The
fourth ventricle is a **CSF cavity**; the CTZ is the
**functional role** of the **organ** at its **caudal floor**.

**Do not** assume the right CTZ is the **whole CTZ**, the
**whole respiratory_center**, or the **whole medulla oblongata**.
It is a **leaf** in a **chain** of containers.

**Do not** assume the right CTZ has **structural children**. It
is a **leaf** — it represents the **right-side aspect** of the
**midline CTZ** as a **single structure**.

Iterating the right CTZ's (empty) children (recommended consumer
pattern)::

    RIGHT_CHEMORECEPTOR_TRIGGER_ZONE_CHILDREN = ()
    # The right CTZ is a leaf. It has no structural children.
    # Anatomically, the CTZ is a SINGLE midline structure — the
    # right/left split is a tree-wiring convention.

Reaching the left CTZ (recommended consumer pattern — the
contralateral leaf, representing the SAME midline structure)::

    # The left CTZ is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.left
    #
    # The right and left CTZ leaves are ASPECTS of the SAME
    # midline structure — NOT two separate functional roles.

Reaching the whole CTZ container (recommended consumer pattern —
for consumers that need the whole functional role)::

    # The whole CTZ is the PARENT container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone
    #
    # Consumers that need the WHOLE CTZ should use the parent
    # container, not the right or left leaf.

Reaching the right area postrema (recommended consumer pattern —
NOTE the DIFFERENT leaf, the SAME physical structure under a
DIFFERENT name, wired as a SEPARATE child in this tree)::

    # The right area postrema is a SEPARATE leaf under a DIFFERENT
    # child of respiratory_center in this tree — even though the
    # literature often treats the AP and the CTZ as synonymous:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.right
    #
    # The AP is the ANATOMICAL STRUCTURE; the CTZ is the
    # FUNCTIONAL ROLE — the tree separates them into TWO MODULES
    # as a deliberate wiring choice. Consumers must NOT conflate
    # the two leaves within the tree, AND must NOT conclude that
    # wiring separation implies anatomical separation — the
    # underlying structure is ONE.

Reaching the right solitary nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The right solitary nucleus (NTS) is a SEPARATE container
    # under medulla_oblongata — the CTZ PROJECTS to the NTS, but
    # is NOT the NTS itself:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
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