"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.right
===========================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── area_postrema
                    └── right   <-- THIS MODULE

**Primary synonym:** Right area postrema; right AP; right postrema;
right area postrema of the fourth ventricle; right aspect of the
area postrema.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**circumventricular organ** — in **this tree**, the **right leaf**
representing the **right-side aspect** of the **midline area
postrema**. **Anatomically**, the human area postrema is a
**single, unpaired, midline** circumventricular organ at the
**caudal floor of the fourth ventricle**, **lacking a
blood-brain barrier**, that **senses blood-borne and CSF-borne
substances** and **triggers the vomiting reflex**. The ``right``
module is a **tree-wiring convention** — **NOT** an anatomical
claim that there is a **separate right area postrema**.
**Part of:** The **area_postrema** bilateral container
(``.../respiratory_center/area_postrema/``) — which is part of
the **respiratory_center** — which is part of the **medulla
oblongata** — the **caudal brainstem** subdivision of the
**myelencephalon**.
**Structural parent:** ``.../area_postrema/`` → **direct child**
of the area_postrema container. The **right** leaf is one of the
**two** structural children of the container (the other is
``left``).
**Structural children:** **None.** This is a **leaf** module. The
right area postrema is represented as a **single structure** — it
has **no structural children** of its own.
**Boundary status (NOT the left area postrema — the
contralateral leaf, both representing the SAME midline
structure):** **Boundary case — the right area postrema is NOT
the left area postrema.** The **left area postrema**
(``.../area_postrema/left/``) is the **contralateral leaf** —
the **left-side aspect** of the **same midline area postrema**.
**They are DIFFERENT LEAVES** — the ``left`` and ``right``
modules are the two sides of the **bilateral container**. **In
the brain, there is ONE area postrema** — the **right** and
**left** leaves are **tree-wiring aspects** of the **same
midline structure**, **NOT** two separate organs. Consumers must
**not** infer **anatomical bilaterality** from the tree
structure.
**Boundary status (NOT the whole area postrema — an ASPECT of
it):** **Boundary case — the right area postrema is NOT the whole
area postrema.** The **whole area postrema**
(``.../area_postrema/``) is the **bilateral container** that
**contains** the right area postrema (here) **plus** the left
area postrema. The **right** module is **one aspect** — the
**right-side aspect** — of the **midline area postrema**.
Consumers must **not** conflate the **leaf** with the
**container**.
**Boundary status (NOT the chemoreceptor trigger zone — a
DIFFERENT child in THIS TREE, even though often synonymous in
the literature):** **Boundary case — the right area postrema is
NOT the chemoreceptor trigger zone (CTZ) in this tree.** In the
**literature**, the **area postrema** and the **chemoreceptor
trigger zone** are **often used interchangeably** — they are
**largely considered** the **same structure**. **In this tree**,
however, they are **wired as two separate child containers** of
``respiratory_center``:
``respiratory_center.area_postrema`` (this module's parent) and
``respiratory_center.chemoreceptor_trigger_zone``. Consumers must
**not** conflate the two modules **within the tree** — resolve
the **CTZ** via
``respiratory_center.chemoreceptor_trigger_zone``.
**Boundary status (NOT the right chemoreceptor trigger zone leaf —
a DIFFERENT child of respiratory_center):** **Boundary case —
the right area postrema is NOT the right chemoreceptor trigger
zone.** The **right chemoreceptor trigger zone**
(``.../respiratory_center/chemoreceptor_trigger_zone/right/``) is
a **separate leaf** — the **right-side aspect** of the **CTZ**.
**They are DIFFERENT LEAVES** under **different children** of
``respiratory_center`` — even though the **literature** often
treats **AP and CTZ as synonymous**. Consumers must **not**
conflate the two leaves **within the tree**.
**Boundary status (NOT the right solitary nucleus — a DIFFERENT
structure in a DIFFERENT container):** **Boundary case — the
right area postrema is NOT the right solitary nucleus (NTS).**
The **right solitary nucleus**
(``.../solitary_nucleus/right/``) is the **right visceral
afferent relay** — it is a **separate structure** in a
**separate container**. The **right area postrema** (here) is a
**right-aspect** of the **circumventricular organ** that
**projects to** the NTS. **They are DIFFERENT STRUCTURES** — the
**AP** is the **sensor**; the **NTS** is the **relay**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right dorsal motor nucleus of the
vagus — a DIFFERENT structure with a DIFFERENT function):**
**Boundary case — the right area postrema is NOT the right
dorsal motor nucleus of the vagus.** The **right dorsal motor
nucleus of the vagus**
(``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
is the **right parasympathetic** nucleus. The **right area
postrema** (here) is a **right-aspect** of the
**circumventricular organ** — **NOT** a parasympathetic nucleus.
They are **anatomically adjacent** at the **caudal fourth
ventricle floor**, but they are **functionally distinct**.
Consumers must **not** conflate the two.
**Boundary status (NOT the right hypoglossal nucleus — a
DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the right area postrema is NOT the right hypoglossal
nucleus.** The **right hypoglossal nucleus**
(``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is the
**right somatic motor** nucleus for the **tongue**. The **right
area postrema** (here) is a **right-aspect** of the
**circumventricular organ** — **NOT** a motor nucleus. Consumers
must **not** conflate the two.
**Boundary status (NOT the right dorsal respiratory group — a
DIFFERENT child of respiratory_center):** **Boundary case — the
right area postrema is NOT the right dorsal respiratory group
(DRG).** The **right dorsal respiratory group**
(``.../respiratory_center/dorsal_respiratory_group/right/``) is
the **right dorsal respiratory** pattern generator — **NOT** a
circumventricular organ. Both are **leaves** under different
children of ``respiratory_center``, but they are **functionally
distinct** — the **DRG** is **respiratory**; the **AP** is
**circumventricular / chemosensory**. Consumers must **not**
conflate the two.
**Boundary status (NOT the right cuneate or right gracile
nucleus — DIFFERENT children of respiratory_center):**
**Boundary case — the right area postrema is NOT the right
cuneate or right gracile nucleus.** The **right cuneate nucleus**
(``.../respiratory_center/cuneate_nucleus/right/``) and **right
gracile nucleus**
(``.../respiratory_center/gracile_nucleus/right/``) are the
**right dorsal column somatosensory relays**. The **right area
postrema** (here) is a **right-aspect** of the
**circumventricular organ** — **NOT** a somatosensory relay.
Consumers must **not** conflate them.
**Boundary status (NOT the right gigantocellular reticular
nucleus — a DIFFERENT child of respiratory_center):**
**Boundary case — the right area postrema is NOT the right
gigantocellular reticular nucleus (Gi).** The **right
gigantocellular reticular nucleus**
(``.../respiratory_center/gigantocellular_reticular_nucleus/right/``)
is a **right medullary reticular** nucleus. The **right area
postrema** (here) is a **right-aspect** of the
**circumventricular organ** — **NOT** a reticular nucleus.
Consumers must **not** conflate the two.
**Boundary status (NOT the fourth ventricle — the fourth
ventricle is a CSF cavity, the area postrema is a CSF-sensing
organ at its floor):** **Boundary case — the right area
postrema is NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is a **CSF cavity** —
**NOT** a grey-matter structure. The **right area postrema**
(here) is a **right-aspect** of the **organ** that **lines the
caudal floor** of the fourth ventricle. Consumers must **not**
conflate the **organ** with the **cavity**.
**Boundary status (NOT the whole respiratory_center or whole
medulla oblongata — a leaf in a chain of containers):**
**Boundary case — the right area postrema is NOT the whole
respiratory_center or the whole medulla oblongata.** It is a
**leaf** at the **bottom** of a **chain** of containers:
``medulla_oblongata`` → ``respiratory_center`` → ``area_postrema``
→ ``right``. Consumers must **not** conflate the **leaf** with
**any of the parent containers**.

Overview
--------
The **right area postrema** is, **in this tree**, the **right-side
aspect** of the **midline area postrema** — a **circumventricular
organ** at the **caudal floor of the fourth ventricle** near the
**obex**. **Anatomically**, there is **only one area postrema** —
a **single, unpaired, midline** structure. The ``right`` /
``left`` split is a **tree-wiring convention** (consistent with
the rest of the medulla oblongata children) — **NOT** an
anatomical claim that the area postrema is **bilaterally
paired**.

**This is a LEAF module.** The **right area postrema** is
represented as a **single structure** — it has **no structural
children**. Consumers that need **side-specific** resolution use
this module; consumers that need **the whole organ** use
``.../area_postrema/`` (the container); consumers that need the
**whole respiratory_center** use ``.../respiratory_center/``.

**The right area postrema is a CIRCUMVENTRICULAR ORGAN aspect,
NOT a respiratory nucleus.** Although wired under
``respiratory_center``, its **primary function** is
**chemoreception / emesis / autonomic regulation** — **NOT**
**breathing**. The **"respiratory_center"** label is a
**tree-wiring artifact** — the tree groups the area postrema
with respiratory and dorsal column nuclei as a **pragmatic
cluster**. Consumers must **not** infer **respiratory function**
from **container membership**.

**The right area postrema is NOT the chemoreceptor trigger zone
in this tree.** In this tree, the **chemoreceptor trigger zone
(CTZ)** is a **separate child** of ``respiratory_center`` — even
though the **literature** often treats **AP and CTZ as
synonymous**. The **AP** (this container) is the **anatomical
structure**; the **CTZ** is the **functional role** — and this
tree **separates** them into **two modules**.

**The right area postrema is the RIGHTWARD ASPECT of a MIDLINE
organ.** It is **functionally and anatomically identical** to
the **left area postrema** (they are two aspects of the same
structure, not two separate organs). Consumers must **not**
assume **laterality** or **functional asymmetry** between the
two.

The Right Area Postrema / Left Area Postrema Boundary
-----------------------------------------------------
This is the **aspect / aspect** boundary (within the same
midline organ):

*   **Right area postrema** (this module) — the **right-side
    aspect** of the **midline area postrema**.

*   **Left area postrema** (``.../area_postrema/left/``) — the
    **left-side aspect** of the **midline area postrema**.

**They are DIFFERENT LEAVES** — the ``right`` and ``left``
modules are the two sides of the **bilateral container**. **In
the brain, there is ONE area postrema** — the **right** and
**left** leaves are **tree-wiring aspects** of the **same
midline structure**, **NOT** two separate organs. Consumers must
**not** infer **anatomical bilaterality** from the tree
structure.

The Right Area Postrema / Whole Area Postrema Boundary
------------------------------------------------------
This is the **leaf / container** boundary:

*   **Right area postrema** (this module) — the **right-side
    aspect**.

*   **Whole area postrema** (``.../area_postrema/``) — the
    **bilateral container** of the **midline organ**.

**The right area postrema is an ASPECT of the whole area
postrema.** Consumers must **not** conflate the **leaf** with
the **container**.

The Right Area Postrema / Right Chemoreceptor Trigger Zone Boundary
-------------------------------------------------------------------
This is the **most consequential** name-collision boundary:

*   **Right area postrema** (this module) — the **right-side
    aspect** of the **circumventricular organ**.

*   **Right chemoreceptor trigger zone**
    (``.../respiratory_center/chemoreceptor_trigger_zone/right/``)
    — the **right-side aspect** of the **CTZ** — **often used
    interchangeably** with the **area postrema** in the
    **literature**.

**They are WIRED AS TWO SEPARATE LEAVES** under **different
children** of ``respiratory_center`` **in this tree**, even
though the **literature** often treats them as **synonymous**.
Consumers must **not** conflate the two leaves **within the
tree** — resolve the **CTZ** via
``respiratory_center.chemoreceptor_trigger_zone.right``.

The Right Area Postrema / Right Solitary Nucleus Boundary
---------------------------------------------------------
This is the **sensor / relay** boundary:

*   **Right area postrema** (this module) — the **right-side
    aspect** of the **circumventricular chemosensory organ**.

*   **Right solitary nucleus (NTS)**
    (``.../solitary_nucleus/right/``) — the **right visceral
    afferent relay**.

**The right area postrema PROJECTS TO the right NTS** — the NTS
is the **downstream target** of the AP's **emetic and autonomic**
signals. **They are DIFFERENT STRUCTURES** — the **AP** is the
**sensor**; the **NTS** is the **relay**. Consumers must **not**
conflate the two.

The Right Area Postrema / Right Dorsal Motor Nucleus of the Vagus and Right Hypoglossal Nucleus Boundary
---------------------------------------------------------------------------------------------------------
This is the **circumventricular / motor** boundary:

*   **Right area postrema** (this module) — the **right-side
    aspect** of the **circumventricular organ**.

*   **Right dorsal motor nucleus of the vagus**
    (``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
    — the **right parasympathetic** nucleus.

*   **Right hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **right somatic motor** nucleus for the **tongue**.

**They are DIFFERENT STRUCTURES.** Consumers must **not**
conflate the two.

The Right Area Postrema / Other Right Respiratory Center Children Boundary
--------------------------------------------------------------------------
This is the **circumventricular / respiratory-and-somatosensory**
boundary:

*   **Right area postrema** (this module) — the **right-side
    aspect** of the **circumventricular organ**.

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
distinct**. Consumers must **not** conflate the **right area
postrema** with any of these.

The Right Area Postrema / Fourth Ventricle Boundary
---------------------------------------------------
This is the **organ / cavity** boundary:

*   **Right area postrema** (this module) — the **right-side
    aspect** of the **circumventricular organ** at the **caudal
    fourth ventricle floor**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the **CSF
    cavity**.

**The right area postrema is at the FLOOR of the fourth
ventricle** — but it is **NOT** the fourth ventricle itself.
Consumers must **not** conflate the **organ** with the
**cavity**.

Function in the Human Brain
---------------------------
The right area postrema's functions are **chemoreception**,
**emesis**, **autonomic regulation**, **fluid balance**, and
**immune-neural signaling** — **NOT respiratory rhythm** and
**NOT motor control** — **and it is functionally identical to
the left area postrema** (they are two aspects of the same
midline organ):

*   **Chemoreception (blood-borne and CSF-borne signals):** The
    **area postrema** **lacks a blood-brain barrier** — its
    **fenestrated capillaries** allow **blood-borne substances**
    (toxins, emetics, hormones, cytokines) to **reach** its
    **neurons**. It is the **primary chemosensory organ** of
    the **caudal brainstem**.

*   **Vomiting reflex (emesis):** The **area postrema** is the
    **primary chemoreceptor trigger zone** for the **vomiting
    reflex** — it **detects** **emetic substances** (e.g.,
    **apomorphine**, **chemotherapy agents**, **toxins**) and
    **triggers** **nausea and vomiting** via **projections** to
    the **NTS** and other **emetic centers**.

*   **Autonomic regulation (cardiovascular and
    gastrointestinal):** The **area postrema** **participates**
    in **cardiovascular regulation** and **gastrointestinal
    regulation** via **projections** to the **NTS** and
    **hypothalamus**.

*   **Fluid and electrolyte balance:** The **area postrema**
    **senses** **plasma osmolality** and **angiotensin II** —
    **contributing** to **thirst**, **salt appetite**, and
    **vasopressin** release.

*   **Immune-neural signaling:** The **area postrema**
    **senses** **cytokines** and **bacterial endotoxin** (LPS)
    — it is a **site of immune-to-brain signaling** contributing
    to **sickness behavior**, **fever**, and **anorexia**.

*   **Conditioned taste aversion:** The **area postrema** is
    **required** for **conditioned taste aversion**.

*   **NOT respiratory rhythm:** The **area postrema** does
    **not** generate the **respiratory rhythm** — that is the
    **pre-Bötzinger complex** (VRG) and the **respiratory**
    centers.

*   **NOT motor control:** The **area postrema** does **not**
    send motor axons to muscles.

**The unifying theme:** the right area postrema is the
**right-side aspect** of the **circumventricular organ** at the
**caudal fourth ventricle floor** — a **chemosensory**,
**emetic**, **autonomic**, **fluid-balance**, and
**immune-neural** structure — **NOT** a respiratory nucleus,
**NOT** the NTS, **NOT** the chemoreceptor trigger zone (in this
tree), and **NOT** the fourth ventricle.

Associated Disorders
--------------------
The right area postrema is the **substrate** for the **same
clinical syndromes** as the left area postrema — the two sides
are **aspects of the same midline organ**, so the clinical
syndromes are **not lateralized**:

*   **Chemotherapy-induced nausea and vomiting (CINV — via area
    postrema):** **Chemotherapy agents** (e.g., **cisplatin**,
    **doxorubicin**) and their **metabolites** **stimulate** the
    **area postrema** — triggering **nausea** and **vomiting**
    via **NTS** and **parabrachial** projections.

*   **Area postrema syndrome (APS — in neuromyelitis optica
    spectrum disorder, NMOSD):** **Neuromyelitis optica
    (NMO)** — an **autoimmune** disorder targeting
    **aquaporin-4 (AQP4)** — **frequently** involves the **area
    postrema**, causing **intractable nausea**, **vomiting**, and
    **hiccups** (**area postrema syndrome**).

*   **Cyclic vomiting syndrome (CVS — hypothesized AP
    involvement):** **CVS** is a **disorder** of **recurrent
    episodes** of **severe nausea and vomiting** —
    **hypothesized** to involve **AP** and **mitochondrial**
    dysfunction.

*   **Bulimia nervosa and eating disorders (hypothesized AP
    involvement):** **Impaired** **AP-mediated** **satiety** and
    **emetic** signaling have been **hypothesized** to
    **contribute** to **bulimia nervosa** and **binge-eating
    disorder**.

*   **Drug-induced emesis (via AP):** **Many** drugs
    (**opioids**, **digoxin**, **apomorphine**, **nicotine**)
    **stimulate** the **area postrema** — triggering **nausea**
    and **vomiting**.

*   **Sickness behavior and fever (via AP immune-neural
    signaling):** The **AP** **senses** **cytokines** and
    **LPS** — **contributing** to **fever**, **anorexia**,
    **lethargy**, and **sickness behavior** during **infection**
    and **inflammation**.

*   **No Named "Right Area Postrema Syndrome":** The right area
    postrema is **not a functionally separate structure** from
    the left area postrema — it is the **right aspect** of the
    **same midline organ**. There is **no named "right area
    postrema syndrome"** — the clinical syndromes are **named
    for the whole area postrema** (e.g., **area postrema
    syndrome** in NMOSD) or **for the function** (CINV,
    drug-induced emesis).

**What is NOT here:** The right area postrema is **not** the
substrate for **central hypoventilation** (VRG, pre-Bötzinger
complex), **sympathetic premotor** function (RVLM), **visceral
afferent relay** (NTS), **tongue weakness** (hypoglossal
nucleus), or **parasympathetic dysfunction** (dorsal motor
nucleus of the vagus). Its clinical relevance is the **emesis**,
**autonomic**, and **immune-neural** functions listed above —
**not lateralized** because the area postrema is a **midline
organ**.

Lateralization Notes
--------------------
This is the **right** area postrema module — the **right-side
aspect** of the **midline area postrema**. The area postrema is
a **bilateral container** in this tree whose two sides represent
the **same midline structure** — and it carries **NO warning**:

*   **Tree-wiring convention, NOT anatomical bilaterality:**
    The **right** and **left** leaves are **aspects** of the
    **same midline** area postrema — **NOT** two separate
    organs. The **right / left split** is a **tree-wiring
    convention** — consistent with the rest of the medulla
    oblongata children (which **are** bilateral in the brain).
    The **human area postrema** is a **single, unpaired,
    midline** structure.

*   **NO lateralization:** The area postrema has **no known
    functional lateralization** — it is a **midline** structure
    with **no left / right functional difference**. Consumers
    must **not** import a **lateralization warning** into the
    right area postrema — the **right** and **left** sides are
    **functionally identical** and **anatomically the same**
    structure.

*   **NO Extended-Amygdala / SLEA Warning:** The right area
    postrema is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the right area postrema.

*   **NO Fear-Output Warning:** The right area postrema is
    **not** a fear-output structure — it is a **circumventricular
    chemosensory** organ aspect. Consumers must **not** conflate
    it with the **central nucleus** or with the **amygdala**.

**A consumer that assumes "right area postrema = left area
postrema" will be structurally correct** — the two sides are
**equivalent** (they represent the **same midline** structure).
The area postrema is a **strict-mirror container with NO
warning** — **no SLEA warning**, **no fear-output warning**,
and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right area postrema is a
    **leaf** — it does **not** import from ``.../left/`` or any
    other left-side module. The **right / left split** is a
    **tree-wiring convention** — not an anatomical bilaterality.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../chemoreceptor_trigger_zone/``,
    ``.../dorsal_respiratory_group/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../cuneate_nucleus/``, ``.../gracile_nucleus/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../metencephalon/fourth_ventricle/``, or any other
    container. The right area postrema's relationships to the
    right chemoreceptor trigger zone, right dorsal respiratory
    group, right gigantocellular reticular nucleus, right cuneate
    nucleus, right gracile nucleus, right solitary nucleus, right
    dorsal motor nucleus of the vagus, right hypoglossal nucleus,
    and the fourth ventricle are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right area
    postrema is a **single structure** — it has **no structural
    children**. Consumers must **not** expect further sub-paths
    under ``.../right/``.
*   **WIRING CONVENTION, NOT anatomical bilaterality.** The
    ``right`` module is an **aspect** of the **midline** area
    postrema — **NOT** a separate organ. The **human area
    postrema** is a **single, unpaired, midline** structure.
*   **NOT the left area postrema.** The left area postrema is a
    **separate leaf** under ``.../area_postrema/left/``.
    Consumers must **not** conflate the right with the left —
    they represent the **same midline** structure.
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
*   **NOT the whole area postrema or whole respiratory_center or
    whole medulla oblongata.** The right area postrema is a
    **leaf** in a **chain** of containers.
*   **No ``AREA_PATHS`` hop.** The right area postrema is a
    **local leaf** — it is not cross-listed under another
    brainparts path.
*   **No nested cross-listing.** The right area postrema has no
    nested dual-framing module. It is a **single leaf**.
*   **Structural parity with the left area postrema — strict
    mirror with NO warning.** The right and left modules are
    **structurally identical** — same leaf status, same
    **circumventricular chemosensory aspect** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.area_postrema.right"
    )

**Do not** assume the right area postrema is a **separate organ**
from the left area postrema. **Anatomically**, there is **ONE
midline area postrema** — the ``right`` / ``left`` split is a
**tree-wiring convention**, **NOT** an anatomical bilaterality.

**Do not** assume the right area postrema is the **right
chemoreceptor trigger zone** in this tree. They are **separate
leaves** under **different children** of ``respiratory_center``
— resolve the **CTZ** via
``respiratory_center.chemoreceptor_trigger_zone.right``.

**Do not** assume the right area postrema is the **right solitary
nucleus (NTS)**. The NTS is a **separate container** — the AP
**projects to** the NTS, but is **NOT** the NTS itself.

**Do not** assume the right area postrema is the **right dorsal
motor nucleus of the vagus**, the **right hypoglossal nucleus**,
the **right dorsal respiratory group**, the **right
gigantocellular reticular nucleus**, the **right cuneate
nucleus**, or the **right gracile nucleus**. Each is a
**different structure**.

**Do not** assume the right area postrema is the **fourth
ventricle**. The fourth ventricle is a **CSF cavity**; the area
postrema is the **circumventricular organ** at its **caudal
floor**.

**Do not** assume the right area postrema is the **whole area
postrema**, the **whole respiratory_center**, or the **whole
medulla oblongata**. It is a **leaf** in a **chain** of
containers.

**Do not** assume the right area postrema has **structural
children**. It is a **leaf** — it represents the **right-side
aspect** of the **midline area postrema** as a **single
structure**.

Iterating the right area postrema's (empty) children
(recommended consumer pattern)::

    RIGHT_AREA_POSTREMA_CHILDREN = ()
    # The right area postrema is a leaf. It has no structural
    # children. Anatomically, the area postrema is a SINGLE
    # midline structure — the right/left split is a tree-wiring
    # convention.

Reaching the left area postrema (recommended consumer
pattern — the contralateral leaf, representing the SAME midline
structure)::

    # The left area postrema is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.left
    #
    # The right and left area postrema leaves are ASPECTS of the
    # SAME midline structure — NOT two separate organs.

Reaching the whole area postrema container (recommended
consumer pattern — for consumers that need the whole organ)::

    # The whole area postrema is the PARENT container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema
    #
    # Consumers that need the WHOLE area postrema should use the
    # parent container, not the right or left leaf.

Reaching the right chemoreceptor trigger zone (recommended
consumer pattern — NOTE the DIFFERENT leaf, often synonymous in
the literature but SEPARATE in this tree)::

    # The right chemoreceptor trigger zone is a SEPARATE leaf
    # under a DIFFERENT child of respiratory_center in this
    # tree — even though the literature often treats the AP and
    # the CTZ as synonymous:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.right
    #
    # Consumers must NOT conflate the two leaves within the tree.

Reaching the right solitary nucleus (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The right solitary nucleus (NTS) is a SEPARATE container
    # under medulla_oblongata — the area postrema PROJECTS to
    # the NTS, but is NOT the NTS itself:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
    #
    # The area postrema is the CHEMOSENSORY organ; the NTS is
    # the VISCERAL AFFERENT relay.

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
        # NOTE: left and right represent aspects of the SAME
        # midline structure, NOT two separate organs.

References
----------
*   **Area postrema — canonical anatomy:** Miller, A.D., Leslie,
    R.A. (1994). "The area postrema and vomiting." *Frontiers in
    Neuroendocrinology* 15:301–320. (Area postrema;
    circumventricular organ; chemoreceptor trigger zone; vomiting
    reflex.)
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
*   **Area postrema — NMOSD — area postrema syndrome:**
    Wingerchuk, D.M., et al. (2015). "International consensus
    diagnostic criteria for neuromyelitis optica spectrum
    disorders." *Neurology* 85:177–189. (Area postrema
    syndrome; NMOSD diagnostic criteria.)
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
*   NeuroNames — Area postrema; FMA — Area postrema.
"""