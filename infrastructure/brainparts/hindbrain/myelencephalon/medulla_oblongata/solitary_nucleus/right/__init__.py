"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
===========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── solitary_nucleus
                └── right   <-- THIS MODULE

**Primary synonym:** Right solitary nucleus; right nucleus tractus
solitarius; right NTS; right nucleus of the solitary tract; right
nucleus solitarius; right solitary tract nucleus; right visceral
afferent nucleus of the medulla.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** in the **right dorsal medulla
oblongata** — the **right primary visceral afferent relay** of the
**brainstem**, receiving **right taste** (via **right CN VII, IX,
X**), **right baroreceptor** afferents (via **right CN IX, X**),
**right chemoreceptor** afferents (via **right CN IX, X**),
**right gastrointestinal** afferents (via **right CN X**), and
**right respiratory** afferents (via **right CN X**). It is
**NOT** a motor nucleus, **NOT** a sympathetic premotor center,
**NOT** a respiratory rhythm generator, **NOT** a circumventricular
organ, and **NOT** a reticular nucleus.
**Part of:** The **solitary_nucleus** bilateral container
(``.../medulla_oblongata/solitary_nucleus/``) — which is part of
the **medulla oblongata** — the **caudal brainstem** subdivision
of the **myelencephalon**. It is a **child** of the solitary
nucleus container — **NOT** a child of ``respiratory_center`` and
**NOT** a child of any other container. It is a **sibling** of
the **right DRG**, the **right RVLM**, the **right CVLM**, the
**right VRG**, and other right medullary containers.
**Structural parent:** ``.../solitary_nucleus/`` → **direct
child** of the solitary_nucleus container. The **right** leaf is
one of the **two** structural children of the container (the
other is ``left``).
**Structural children:** **None.** This is a **leaf** module. The
right NTS is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the left solitary nucleus — the
contralateral leaf):** **Boundary case — the right NTS is NOT
the left NTS.** The **left NTS**
(``.../solitary_nucleus/left/``) is the **contralateral leaf** —
the NTS of the **left** medulla, relaying **left visceral
afferents**. **They are DIFFERENT LEAVES** — the ``right`` and
``left`` modules are the two sides of the **bilateral
container**. **Unlike the area postrema / CTZ** — which are
**midline** organs wired as left/right by convention — **the
right and left NTS are TRULY SEPARATE BILATERAL STRUCTURES**
(anatomical, not a wiring convention). Consumers must **not**
conflate the two.
**Boundary status (NOT the right dorsal respiratory group (DRG) —
a DIFFERENT child of respiratory_center even though OFTEN
CONSIDERED PART OF THE RIGHT NTS in the literature):** **Boundary
case — the right NTS is NOT the right DRG IN THIS TREE, even
though the right DRG is often considered part of the right NTS in
the literature.** In the **literature**, the **right DRG** is a
**functional respiratory subregion** within the **ventrolateral
right NTS** — the right NTS **contains** the right DRG. **In this
tree**, however, they are **wired as separate modules**:
``.../solitary_nucleus/right/`` (this module) is a **child** of
the NTS container (a direct child of ``medulla_oblongata``);
``.../respiratory_center/dorsal_respiratory_group/right/`` (the
right DRG) is a **child** of ``respiratory_center``. **The tree
separates the right NTS and the right DRG into two modules** as a
**deliberate wiring choice** — the **right DRG** is a
**functional respiratory group within the right NTS region**; the
**right NTS** is the **broader visceral afferent relay** of which
the **right DRG** is a **functional subregion**. Consumers must
**not** expect to find the right DRG under
``solitary_nucleus.right`` — resolve it via
``respiratory_center.dorsal_respiratory_group.right``. Consumers
must **not** expect to find the right NTS under
``respiratory_center`` — resolve it via
``.../solitary_nucleus/right/``. **The two are separate modules**,
even though the **right DRG is anatomically within the right NTS
region** — the tree **separates** the **right NTS (visceral
afferent relay)** from the **right DRG (dorsal respiratory
pattern generator)**.
**Boundary status (NOT the right RVLM — the RVLM is the
SYMPATHETIC PREMOTOR efferent limb):** **Boundary case — the
right NTS is NOT the right rostral ventrolateral medulla (RVLM).**
The **right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) is the **right
sympathetic premotor** center — the **efferent limb** of the
**right medullary baroreflex arc**. The **right NTS** (here) is
the **right visceral afferent relay** — the **afferent limb** of
the **right medullary baroreflex arc**. **They are DIFFERENT
STRUCTURES** — the **right NTS** is the **afferent** relay; the
**right RVLM** is the **efferent** sympathetic premotor center.
They are **functionally coupled** in the **right baroreflex arc**
(right NTS → right CVLM → right RVLM → right IML column) but are
**anatomically distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the right CVLM — the CVLM is the
SYMPATHOINHIBITORY relay):** **Boundary case — the right NTS is
NOT the right caudal ventrolateral medulla (CVLM).** The **right
CVLM** (``.../caudal_ventrolateral_medulla/right/``) is the
**right sympathoinhibitory** relay — it **inhibits the right
RVLM** (via **GABAergic** input from the **right NTS**). The
**right NTS** (here) is the **right visceral afferent relay** —
it **projects** to the right CVLM. **They are DIFFERENT
STRUCTURES** — the **right NTS** is the **afferent** relay; the
**right CVLM** is the **sympathoinhibitory** relay. Consumers
must **not** conflate the two.
**Boundary status (NOT the right area postrema or right CTZ — the
AP/CTZ PROJECT TO the right NTS, but are NOT the right NTS):**
**Boundary case — the right NTS is NOT the right area postrema or
the right chemoreceptor trigger zone.** The **right area
postrema** and **right chemoreceptor trigger zone**
(``.../respiratory_center/area_postrema/right/`` and
``.../respiratory_center/chemoreceptor_trigger_zone/right/``) are
**right circumventricular chemoreceptive** structures that
**project to** the **right NTS**. The **right NTS** (here) is the
**right visceral afferent relay** — it is the **downstream
target** of the **AP/CTZ emetic** and **autonomic** signals.
**They are DIFFERENT STRUCTURES** — the **right AP/CTZ** is the
**sensor**; the **right NTS** is the **relay**. Consumers must
**not** conflate the two.
**Boundary status (NOT the right dorsal motor nucleus of the
vagus — a DIFFERENT structure with a DIFFERENT function):**
**Boundary case — the right NTS is NOT the right dorsal motor
nucleus of the vagus (DMV).** The **right DMV**
(``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
is the **right parasympathetic** motor nucleus — the **right
visceral motor** source of **right CN X**. The **right NTS**
(here) is the **right visceral afferent relay** — the **right
visceral sensory** source of **right CN VII, IX, X**. **They are
DIFFERENT STRUCTURES** — the **right DMV** is **visceral motor**
(parasympathetic); the **right NTS** is **visceral sensory**
(afferent relay). They are **anatomically adjacent** in the
**right dorsal medulla** — **both** are wired under different
containers. Consumers must **not** conflate the two.
**Boundary status (NOT the right hypoglossal nucleus — a
DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the right NTS is NOT the right hypoglossal nucleus.** The
**right hypoglossal nucleus**
(``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is the
**right somatic motor** nucleus for the **tongue** — **NOT** a
visceral afferent relay. Consumers must **not** conflate the two.
**Boundary status (NOT the right spinal trigeminal nucleus — a
DIFFERENT somatosensory relay):** **Boundary case — the right
NTS is NOT the right spinal trigeminal nucleus.** The **right
spinal trigeminal nucleus** is the **right facial
pain/temperature** sensory relay (CN V) — **NOT** a visceral
afferent relay. Consumers must **not** conflate the two.
**Boundary status (NOT the right RVLM / right CVLM / right NTS
baroreflex arc as a whole — a COMPONENT of it):** **Boundary
case — the right NTS is NOT the whole right medullary baroreflex
arc.** The **right NTS** is the **afferent limb** of the **right
medullary baroreflex arc** (right NTS → right CVLM → right RVLM
→ right IML column). The **right CVLM** and **right RVLM** are
the **intermediate** and **efferent** limbs. **They are
DIFFERENT STRUCTURES** — the **right NTS** is the **afferent**
relay; the **right CVLM** and **right RVLM** are **downstream**
autonomic premotor structures. Consumers must **not** conflate
the **right NTS** with the **whole right baroreflex arc**.
**Boundary status (NOT the right VRG or right DRG — DIFFERENT
respiratory structures):** **Boundary case — the right NTS is
NOT the right ventral respiratory group (VRG) or the right dorsal
respiratory group (DRG).** The **right VRG**
(``.../ventral_respiratory_group/right/``) is the **right
ventral respiratory** rhythm and pattern generator group. The
**right DRG**
(``.../respiratory_center/dorsal_respiratory_group/right/``) is
the **right dorsal respiratory** pattern generator — often
considered part of the right NTS in the literature but wired
separately in this tree. **They are DIFFERENT STRUCTURES** from
the right NTS — the **right NTS** is the **visceral afferent
relay**; the **right VRG and right DRG** are **respiratory**
structures. Consumers must **not** conflate the two.
**Boundary status (NOT the right Gi or the right paramedian
reticular nucleus — reticular nuclei in DIFFERENT containers):**
**Boundary case — the right NTS is NOT the right gigantocellular
reticular nucleus (Gi) or the right paramedian reticular
nucleus.** Those are **right reticular** nuclei with **broader**
functions — **NOT** the right visceral afferent relay. Consumers
must **not** conflate the right NTS with either.
**Boundary status (NOT the right arcuate nucleus or right
parafacial zone — ventral-surface-and-sleep-promoting
structures):** **Boundary case — the right NTS is NOT the right
arcuate nucleus or the right parafacial zone.** Those are **right
ventral-surface chemosensory** and **right sleep-promoting**
structures, respectively — **NOT** the right visceral afferent
relay. Consumers must **not** conflate the right NTS with either.
**Boundary status (NOT the whole solitary_nucleus container — an
ASPECT of it):** **Boundary case — the right NTS is NOT the whole
solitary_nucleus container.** The **whole solitary_nucleus**
(``.../solitary_nucleus/``) is the **bilateral container** that
**contains** the right NTS (here) **plus** the left NTS.
Consumers must **not** conflate the **leaf** with the
**container**.
**Boundary status (NOT the whole medulla oblongata — a visceral
afferent relay within it):** **Boundary case — the right NTS is
NOT the whole medulla oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the right NTS (via the solitary_nucleus container)
**plus** the RVLM, CVLM, VRG, respiratory centers, cranial nerve
nuclei, olivary body, medullary pyramid, arcuate nucleus,
parafacial zone, paramedian reticular nucleus, perihypoglossal
nuclei, and other structures. The **right NTS** is **one right
visceral afferent relay** within the medulla. Consumers must
**not** conflate the **right NTS** with the **whole medulla**.

Overview
--------
The **right solitary nucleus (right NTS)** — also known as the
**right nucleus tractus solitarius** — is the **right primary
visceral afferent relay** of the **brainstem**, in the **right
dorsal medulla oblongata**. It **receives** the **right visceral
afferent** fibers of **right CN VII** (taste from the **right
anterior tongue**), **right CN IX** (taste from the **right
posterior tongue**, baroreceptor and chemoreceptor afferents
from the **right carotid body/sinus**), and **right CN X** (taste
from the **right epiglottis**, baroreceptor and chemoreceptor
afferents from the **right aortic arch/body**, right
gastrointestinal afferents, right pulmonary afferents, and right
cardiac afferents). It **projects** to a wide range of **right
autonomic**, **right respiratory**, **right endocrine**, and
**right behavioral** targets — including the **right RVLM**,
**right CVLM**, **right DMV**, **right VRG**, **right
parabrachial nucleus**, **right hypothalamus**, and **right
amygdala**.

**This is a LEAF module.** The **right NTS** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution of the right side
use this module; consumers that need **left-side** resolution use
``.../solitary_nucleus/left/``; consumers that need the **whole
solitary_nucleus container** use ``.../solitary_nucleus/``.

**The right NTS is the VISCERAL AFFERENT relay, NOT a motor
nucleus, NOT a sympathetic premotor center, NOT a respiratory
rhythm generator, and NOT a circumventricular organ.** It is a
**genuine right visceral sensory** relay — its classification as
the **right primary visceral afferent relay** is **functionally
accurate**.

**The right NTS is the AFFERENT LIMB of the right medullary
baroreflex arc — NOT the efferent limb.** The **right NTS**
receives **right baroreceptor** afferents via **right CN IX** and
**right CN X**. The **right CVLM**
(``.../caudal_ventrolateral_medulla/right/``) is the **right
sympathoinhibitory** relay; the **right RVLM**
(``.../rostral_ventrolateral_medulla/right/``) is the **right
sympathetic premotor** center. Together they form the **right
medullary baroreflex arc** (right NTS → right CVLM → right RVLM
→ right IML column).

**The right NTS is OFTEN CONSIDERED TO INCLUDE THE RIGHT DRG in
the literature.** The **right dorsal respiratory group (right
DRG)** is a **functional respiratory subregion** within the
**ventrolateral right NTS**. **In this tree**, the **right DRG is
wired separately** under ``respiratory_center`` — **NOT** under
the right NTS leaf. **The tree separates** the **right NTS
(visceral afferent relay)** from the **right DRG (dorsal
respiratory pattern generator)** as a **deliberate wiring
choice** — consumers must **not** expect to find the right DRG
under ``solitary_nucleus.right``.

**The right NTS is TRULY BILATERAL — the right / left split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **right** and **left**
NTS are **anatomically separate structures**. The **right / left
split** here reflects **anatomy** — **NOT** a **tree-wiring
convention**.

**The right NTS is functionally coupled to the right RVLM, right
CVLM, right DMV, right VRG, right DRG, right area postrema /
CTZ, right parabrachial nucleus, right hypothalamus, right
amygdala, and other higher centers.** It is **part of** the
**right medullary autonomic and respiratory network** — a
**distributed system** for **right visceral sensation**, **right
autonomic regulation**, **right respiratory modulation**, and
**right homeostatic control**.

The Right NTS / Left NTS Boundary
---------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Right NTS** (this module) — the NTS of the **right**
    medulla, relaying **right visceral afferents**.

*   **Left NTS** (``.../solitary_nucleus/left/``) — the NTS of the
    **left** medulla, relaying **left visceral afferents**.

**They are TRULY SEPARATE BILATERAL STRUCTURES** — the **right**
and **left** NTS are **anatomically distinct** (not a wiring
convention for a midline organ). They are **structurally
symmetric mirror pairs** — same cytoarchitecture, same
projections (with some crossed components), same **no warning**.
Consumers must **not** conflate the right with the left — resolve
the left side via ``solitary_nucleus.left``.

The Right NTS / Right Dorsal Respiratory Group (DRG) Boundary
------------------------------------------------------------
This is the **most consequential** tree-wiring boundary:

*   **Right NTS** (this module) — the **right broader visceral
    afferent relay**.

*   **Right DRG**
    (``.../respiratory_center/dorsal_respiratory_group/right/``)
    — the **right dorsal respiratory** pattern generator — **often
    considered part of the right NTS in the literature**, but
    **wired separately** under ``respiratory_center`` in this
    tree.

**In this tree, they are SEPARATE MODULES.** The **right NTS** is
the **right broader visceral afferent relay**; the **right DRG**
is a **functional respiratory subregion** within the
**ventrolateral right NTS region** — **wired under a different
container**. The **tree separates** the two as a **deliberate
wiring choice**. Consumers must **not** expect to find the right
DRG under ``solitary_nucleus.right`` — resolve it via
``respiratory_center.dorsal_respiratory_group.right``.

The Right NTS / Right RVLM Boundary
-----------------------------------
This is the **afferent / efferent** boundary:

*   **Right NTS** (this module) — the **right visceral afferent
    relay**.

*   **Right RVLM** (``.../rostral_ventrolateral_medulla/right/``) —
    the **right sympathetic premotor** center.

**The right NTS is UPSTREAM of the right RVLM in the baroreflex
arc** — the right NTS receives **right baroreceptor** afferents
and **projects** to the right RVLM **directly** (glutamatergic
and GABAergic projections) and **via the right CVLM**. Consumers
must **not** conflate the two — the **right NTS** is the
**afferent** relay; the **right RVLM** is the **sympathetic
premotor** center.

The Right NTS / Right CVLM Boundary
-----------------------------------
This is the **afferent / sympathoinhibitory** boundary:

*   **Right NTS** (this module) — the **right visceral afferent
    relay**.

*   **Right CVLM** (``.../caudal_ventrolateral_medulla/right/``) —
    the **right sympathoinhibitory** relay.

**The right NTS is UPSTREAM of the right CVLM in the baroreflex
arc** — the right NTS receives **right baroreceptor** afferents
and **projects** to the right CVLM. Consumers must **not** conflate
the two — the **right NTS** is the **afferent** relay; the
**right CVLM** is the **sympathoinhibitory** relay.

The Right NTS / Right Area Postrema and Right CTZ Boundary
---------------------------------------------------------
This is the **visceral afferent / circumventricular** boundary:

*   **Right NTS** (this module) — the **right visceral afferent
    relay**.

*   **Right area postrema** and **right chemoreceptor trigger
    zone** (``.../respiratory_center/area_postrema/right/`` and
    ``.../respiratory_center/chemoreceptor_trigger_zone/right/``)
    — the **right circumventricular chemoreceptive** structures
    for the **vomiting reflex**.

**The right AP/CTZ PROJECT TO the right NTS** — the right NTS is
the **downstream target** of the right AP/CTZ emetic and
autonomic signals. **They are DIFFERENT STRUCTURES** — the
**right AP/CTZ** is the **sensor**; the **right NTS** is the
**relay**. Consumers must **not** conflate the two.

The Right NTS / Right Dorsal Motor Nucleus of the Vagus Boundary
----------------------------------------------------------------
This is the **sensory / motor** boundary:

*   **Right NTS** (this module) — the **right visceral sensory**
    afferent relay.

*   **Right dorsal motor nucleus of the vagus (DMV)**
    (``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
    — the **right visceral motor** (parasympathetic) nucleus.

**They are DIFFERENT STRUCTURES** — the **right DMV** is
**visceral motor** (parasympathetic); the **right NTS** is
**visceral sensory** (afferent relay). They are **anatomically
adjacent** in the **right dorsal medulla** but are **functionally
distinct**. Consumers must **not** conflate the two.

The Right NTS / Right Hypoglossal Nucleus and Right Spinal Trigeminal Nucleus Boundary
--------------------------------------------------------------------------------------
This is the **visceral afferent / somatic** boundary:

*   **Right NTS** (this module) — the **right visceral sensory**
    afferent relay.

*   **Right hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) —
    the **right somatic motor** nucleus.

*   **Right spinal trigeminal nucleus** — the **right facial
    pain/temperature** sensory relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the **right NTS** with either.

The Right NTS / Right VRG Boundary
----------------------------------
This is the **visceral afferent / ventral respiratory** boundary:

*   **Right NTS** (this module) — the **right visceral afferent
    relay**.

*   **Right VRG** (``.../ventral_respiratory_group/right/``) — the
    **right ventral respiratory** rhythm and pattern generator
    group.

**They are DIFFERENT STRUCTURES** — the **right NTS** is the
**right visceral afferent relay**; the **right VRG** is a
**right respiratory rhythm generator**. They are **functionally
coupled** (the right NTS **projects** to the right VRG to
**modulate** right respiratory pattern) but are **anatomically
distinct**. Consumers must **not** conflate the two.

The Right NTS / Other Right Medullary Structures Boundary
--------------------------------------------------------
This is the **visceral afferent / other-medullary-structures**
boundary:

*   **Right NTS** (this module) — the **right visceral afferent
    relay**.

*   **Right Gi, right paramedian reticular nucleus, right arcuate
    nucleus, right parafacial zone, right olivary body, right
    medullary pyramid, right perihypoglossal nuclei, right cranial
    nerve nuclei** — **other right medullary structures**.

**Each is a DIFFERENT STRUCTURE.** Consumers must **not** conflate
the **right NTS** with any of these.

The Right NTS / Whole Solitary Nucleus Container and Whole Medulla Oblongata Boundary
------------------------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Right NTS** (this module) — one **leaf** of the
    ``solitary_nucleus`` container.

*   **Solitary nucleus** (``.../solitary_nucleus/``) — the
    **bilateral container** of the right + left NTS.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the NTS container and other medullary
    structures.

**The right NTS is a LEAF in a CHAIN of containers.** Consumers
must **not** conflate the **leaf** with any of the **parent
containers**.

**The right NTS is NOT a child of respiratory_center.** The
**respiratory_center** is a **sibling container** of the NTS —
**NOT** a parent. Consumers must **not** expect to find the right
NTS under ``respiratory_center``.

Function in the Human Brain
---------------------------
The right NTS's function is **right visceral afferent relay** —
**NOT motor control**, **NOT sympathetic premotor**, and **NOT
respiratory rhythm generation**:

*   **Right taste relay:** The **right NTS** receives **right
    taste** afferents from the **right anterior tongue** (via
    **right CN VII**), **right posterior tongue** (via **right CN
    IX**), and **right epiglottis** (via **right CN X**) — and it
    **relays** them to the **right parabrachial nucleus** and
    the **right thalamus** (VPM) for **conscious taste
    perception**, and to the **right hypothalamus** and **right
    amygdala** for **affective** and **homeostatic** responses to
    taste.

*   **Right baroreceptor relay:** The **right NTS** receives
    **right baroreceptor** afferents from the **right carotid
    sinus** (via **right CN IX**) and the **right aortic arch**
    (via **right CN X**) — and it **initiates the right
    baroreflex** by **projecting** to the **right CVLM** (which
    **inhibits the right RVLM**) and to the **right DMV** (for
    **right parasympathetic** cardiac **slowing**). This is the
    **right afferent limb** of the **right medullary baroreflex
    arc**.

*   **Right chemoreceptor relay:** The **right NTS** receives
    **right chemoreceptor** afferents from the **right carotid
    body** (via **right CN IX**) and the **right aortic body**
    (via **right CN X**) — and it **initiates the right
    chemoreflex** by **projecting** to the **right VRG** (for
    **right respiratory** **stimulation**) and to the **right
    RVLM** (for **right sympathetic** **activation**).

*   **Right gastrointestinal relay:** The **right NTS** receives
    **right gastrointestinal** afferents (via **right CN X**) and
    **projects** to the **right DMV** (for **right
    gastrointestinal** **parasympathetic** control), the **right
    parabrachial nucleus** (for **right visceral** **sensation**),
    and the **right hypothalamus** (for **food intake** and
    **metabolic** regulation).

*   **Right respiratory relay:** The **right NTS** receives
    **right pulmonary** afferents (via **right CN X**) —
    **pulmonary stretch receptor** signals and **irritant
    receptor** signals — and it **projects** to the **right VRG**
    and **right DRG** (for **right respiratory** **pattern
    modulation**).

*   **Right cardiac relay:** The **right NTS** receives **right
    cardiac** afferents (via **right CN X**) — and it **projects**
    to the **right DMV** (for **right parasympathetic**
    **cardiac** control) and the **right RVLM** (for **right
    sympathetic** **cardiac** control).

*   **NOT motor control:** The **right NTS** does **not** send
    motor axons to muscles.

*   **NOT sympathetic premotor:** The **sympathetic premotor**
    function is the **right RVLM** — **NOT** the right NTS.

*   **NOT respiratory rhythm generation:** The **respiratory
    rhythm** is generated by the **pre-Bötzinger complex** (right
    VRG) — **NOT** the right NTS.

**The unifying theme:** the right NTS is the **right primary
visceral afferent relay** of the **brainstem** — it **receives**
right taste, baroreceptor, chemoreceptor, gastrointestinal,
pulmonary, and cardiac afferents via **right CN VII, IX, X** —
and it **projects** to the **right RVLM**, **right CVLM**,
**right DMV**, **right VRG**, **right parabrachial nucleus**,
**right hypothalamus**, and **right amygdala** to **initiate** the
**right baroreflex**, **right chemoreflex**, **right
gastrointestinal**, and **right respiratory** **reflexes** —
**NOT** a motor nucleus, **NOT** a sympathetic premotor center,
and **NOT** a respiratory rhythm generator.

Associated Disorders
--------------------
The right NTS is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct**, via **right
visceral afferent** dysfunction (though the **whole-body**
clinical phenotypes — baroreflex failure, dysautonomia, etc. —
are typically **bilateral** because the NTSs work together):

*   **Baroreflex failure (via bilateral NTS dysfunction — right
    NTS contributes):** **Damage** to the **right NTS** — from
    **stroke**, **demyelination**, **tumor**, or **surgical**
    **injury** — **disrupts** the **right afferent limb** of the
    **baroreflex** — causing **baroreflex failure**: **labile
    blood pressure**, **orthostatic hypotension**,
    **hypertensive crises**, and **loss of heart-rate
    variability**. The **right NTS** is a **contributing
    substrate** — the **left NTS** and **higher centers** can
    partially compensate.

*   **Dysautonomia / autonomic failure (via right NTS
    dysfunction):** **Damage** to the **right NTS** can
    **contribute** to **dysautonomia** — **orthostatic
    hypotension**, **gastrointestinal** **dysmotility**,
    **cardiac** **arrhythmias**, and **thermoregulatory**
    dysfunction.

*   **Neurogenic hypertension (via right NTS dysfunction —
    hypothesized in some models):** **Impaired** right NTS
    **baroreceptor** input can **contribute** to **neurogenic
    hypertension** by **reducing** the **baroreflex buffering**
    of **sympathetic outflow**.

*   **Brainstem stroke (via right NTS involvement):** **Right
    Wallenberg syndrome (right lateral medullary syndrome)**
    **frequently** **involves** the **right NTS** — contributing
    to **autonomic instability**, **intractable hiccups**,
    **nausea**, and **cardiovascular** dysfunction.

*   **Taste disorders (via right NTS dysfunction):** **Damage**
    to the **right rostral NTS** can cause **right-sided**
    **taste loss** (ageusia, hypogeusia) or **dysgeusia**. The
    **right NTS** is the **right first central** **taste
    relay**.

*   **Gastrointestinal dysmotility (via right NTS dysfunction):**
    **Damage** to the **right NTS** can **contribute** to
    **gastroparesis**, **constipation**, or **dysphagia** via
    **impaired** **right visceral afferent** and
    **parasympathetic** **reflexes**.

*   **No Named "Right NTS Syndrome":** The right NTS is a **right
    visceral afferent relay** — its clinical syndromes are
    **named for the broader clinical entity** (baroreflex
    failure, dysautonomia, Wallenberg syndrome) or the **broader
    lesion** — **NOT** for the right NTS itself. There is **no
    named "right NTS syndrome"**.

**What is NOT here:** The right NTS is **not** the substrate for
**sympathetic premotor** function (right RVLM),
**sympathoinhibition** (right CVLM), **respiratory rhythm
generation** (right VRG), **dorsal respiratory pattern
generation** (right DRG), **emesis** (right area postrema / right
CTZ), **tongue weakness** (right hypoglossal nucleus), or
**parasympathetic dysfunction** (right dorsal motor nucleus of the
vagus). Its clinical relevance is the **right visceral afferent**
functions listed above.

Lateralization Notes
--------------------
This is the **right** NTS module. The solitary nucleus is a
**bilateral container** whose two sides are **ANATOMICALLY
SEPARATE** — **not** a wiring convention for a midline organ
(unlike the area postrema / CTZ) — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **right** and **left** NTS are
    **structurally symmetric** — they are **mirror pairs** with
    the **same** cytoarchitecture, **same** projections (with
    some crossed components), and **same** functions. The
    **right** NTS is in the **right dorsal medulla**; the **left**
    NTS is in the **left dorsal medulla**.

*   **Predominantly Ipsilateral, Partly Crossed Projections:** The
    **right NTS** projects **predominantly ipsilaterally** (to
    the **right RVLM**, **right CVLM**, **right DMV**, **right
    VRG**, **right parabrachial**) — with some **crossed**
    projections via **commissural** pathways. This **functional
    ipsilaterality** is **part of the autonomic and respiratory
    network's bilateral coordination** — the **right and left
    NTS** together coordinate **visceral reflexes** bilaterally.

*   **NO Lateralization Warning:** The NTS has **no known
    functional lateralization** in humans — the **right** and
    **left** NTS are **functionally symmetric** at the
    **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the right NTS — the **right**
    and **left** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The right NTS is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the right NTS.

*   **NO Fear-Output Warning:** The right NTS is **not** a
    fear-output structure — it is a **right visceral afferent
    relay**. Consumers must **not** conflate it with the
    **central nucleus** or with the **amygdala**.

**A consumer that assumes "right NTS = left NTS" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The NTS is
a **strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The right NTS is a **leaf** —
    it does **not** import from ``.../left/`` or any other
    left-side module. The **right / left split** is
    **ANATOMICAL** — not a **wiring convention**. The **right**
    and **left** NTS are **truly separate bilateral
    structures**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../rostral_ventrolateral_medulla/``,
    ``.../caudal_ventrolateral_medulla/``,
    ``.../ventral_respiratory_group/``,
    ``.../respiratory_center/``,
    ``.../cranial_nerve_nuclei/``,
    ``.../paramedian_reticular_nucleus/``,
    ``.../arcuate_nucleus/``, ``.../parafacial_zone/``,
    ``.../perihypoglossal_nuclei/``,
    ``.../medullary_pyramid/``, ``.../olivary_body/``, or any
    other container. The right NTS's relationships to the right
    DRG, right RVLM, right CVLM, right area postrema, right CTZ,
    right dorsal motor nucleus of the vagus, right hypoglossal
    nucleus, right spinal trigeminal nucleus, right VRG, right
    Gi, right paramedian reticular nucleus, right arcuate
    nucleus, and right parafacial zone are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The right NTS is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../right/``.
*   **ANATOMICAL BILATERALITY, NOT a wiring convention.** The
    ``right`` and ``left`` NTS are **anatomically separate
    structures** — unlike the **area postrema** / **CTZ** (which
    are midline organs wired as left/right by convention).
*   **VISCERAL AFFERENT RELAY — the right primary visceral
    sensory relay of the brainstem.** The right NTS is a
    **genuine right visceral afferent relay** — **NOT** a motor
    nucleus, **NOT** a sympathetic premotor center, **NOT** a
    respiratory rhythm generator, and **NOT** a
    circumventricular organ.
*   **NOT the right DRG.** The **right DRG** is a **functional
    respiratory subregion** within the **right NTS region** —
    **often considered part of the right NTS in the
    literature**, but **wired separately** under
    ``respiratory_center`` in this tree. Consumers must **not**
    expect to find the right DRG under ``solitary_nucleus.right``.
*   **NOT the right RVLM or right CVLM.** Those are the **efferent
    limb** (right RVLM) and **sympathoinhibitory** relay (right
    CVLM) of the **right medullary baroreflex arc** — **NOT** the
    **afferent** relay (right NTS).
*   **NOT the right area postrema or right CTZ.** Those are
    **right circumventricular chemoreceptive** structures that
    **project to** the right NTS.
*   **NOT the right dorsal motor nucleus of the vagus.** The
    **right DMV** is **visceral motor** (parasympathetic); the
    **right NTS** is **visceral sensory** (afferent relay).
*   **NOT the right hypoglossal nucleus or right spinal trigeminal
    nucleus.** Those are **somatic motor** and **facial
    somatosensory** structures, respectively.
*   **NOT the right VRG.** The right VRG is a **respiratory
    rhythm generator** — the right NTS **projects to** the right
    VRG, but is **NOT** the right VRG.
*   **NOT the right Gi, right paramedian reticular nucleus, right
    arcuate nucleus, or right parafacial zone.** Each is a
    **different structure**.
*   **NOT the whole solitary_nucleus or whole medulla oblongata.**
    The right NTS is a **leaf** in a **chain** of containers.
*   **No ``AREA_PATHS`` hop.** The right NTS is a **local leaf** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The right NTS has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the left NTS — strict mirror with
    NO warning.** The right and left modules are **structurally
    identical** — same leaf status, same **visceral afferent**
    framing, same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus import right

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "solitary_nucleus.right"
    )

**Do not** expect to find the **right DRG** under
``solitary_nucleus.right``. The **right DRG** is **often
considered part of the right NTS in the literature**, but it is
**wired separately** under ``respiratory_center`` in this tree.
Resolve the right DRG via
``respiratory_center.dorsal_respiratory_group.right``.

**Do not** assume the right NTS is the **right RVLM** or **right
CVLM**. Those are the **efferent limb** and **sympathoinhibitory**
relay of the **right medullary baroreflex arc** — **NOT** the
**afferent** relay (right NTS).

**Do not** assume the right NTS is the **right area postrema** or
**right CTZ**. Those are **right circumventricular chemoreceptive**
structures that **project to** the right NTS.

**Do not** assume the right NTS is the **right dorsal motor
nucleus of the vagus**. The **right DMV** is **visceral motor**
(parasympathetic); the **right NTS** is **visceral sensory**
(afferent relay).

**Do not** assume the right NTS is the **right hypoglossal
nucleus** or the **right spinal trigeminal nucleus**. Those are
**somatic motor** and **facial somatosensory** structures,
respectively.

**Do not** assume the right NTS is the **right VRG**. The right
VRG is a **respiratory rhythm generator** — the right NTS
**projects to** the right VRG, but is **NOT** the right VRG.

**Do not** assume the right NTS is the **right Gi**, the **right
paramedian reticular nucleus**, the **right arcuate nucleus**, or
the **right parafacial zone**. Each is a **different structure**.

**Do not** assume the right NTS is the **left NTS**. The left NTS
is the **separate leaf** at ``.../solitary_nucleus/left/``.

**Do not** assume the right NTS has **structural children**. It
is a **leaf** — it represents the right NTS as a **single
structure**.

**Do not** infer **midline wiring convention** from the right NTS
structure. The **right / left split** is **ANATOMICAL** — the
**right** and **left** NTS are **truly separate bilateral
structures**.

Iterating the right NTS's (empty) children (recommended consumer
pattern)::

    RIGHT_SOLITARY_NUCLEUS_CHILDREN = ()
    # The right NTS is a leaf. It has no structural children.

Reaching the left NTS (recommended consumer pattern — the
contralateral leaf, a TRULY SEPARATE structure)::

    # The left NTS is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
    #
    # The right and left NTS are TRULY SEPARATE BILATERAL
    # STRUCTURES (anatomical, not a wiring convention).

Reaching the right DRG (recommended consumer pattern — NOTE the
DIFFERENT container, OFTEN CONSIDERED PART OF THE RIGHT NTS in
the literature)::

    # The right dorsal respiratory group is a CHILD of
    # respiratory_center — wired SEPARATELY from the right NTS in
    # this tree, even though the right DRG is often considered
    # part of the right NTS in the literature:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.right
    #
    # The tree separates the right NTS (visceral afferent relay)
    # from the right DRG (dorsal respiratory pattern generator) as
    # a deliberate wiring choice.

Reaching the right RVLM and right CVLM (recommended consumer
pattern — NOTE the DIFFERENT containers)::

    # The right RVLM and right CVLM are the EFFERENT limb and
    # SYMPATHOINHIBITORY relay of the right medullary baroreflex
    # arc — SEPARATE containers:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.right
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.right
    #
    # The right NTS is the AFFERENT limb of the baroreflex arc —
    # it PROJECTS to the right CVLM (which inhibits the right
    # RVLM) and to the right RVLM directly. They are DIFFERENT
    # structures.

Reaching the right area postrema and right CTZ (recommended
consumer pattern — NOTE the DIFFERENT children of
respiratory_center)::

    # The right area postrema and right chemoreceptor trigger zone
    # are CIRCUMVENTRICULAR structures that PROJECT TO the right
    # NTS — leaves of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.right
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.right
    #
    # They are DIFFERENT structures from the right NTS — the right
    # AP/CTZ is the sensor; the right NTS is the relay.

Reaching the right dorsal motor nucleus of the vagus
(recommended consumer pattern — NOTE the DIFFERENT container)::

    # The right dorsal motor nucleus of the vagus is a VISCERAL
    # MOTOR (parasympathetic) nucleus — a separate container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.dorsal_motor_nucleus_vagus
    #
    # The right NTS is the VISCERAL SENSORY (afferent relay) —
    # they are functionally paired but anatomically distinct.

Reaching the right VRG (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The right ventral respiratory group is a RESPIRATORY
    # structure — a separate container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.right
    #
    # The right NTS PROJECTS to the right VRG (to modulate
    # respiratory pattern) — but the right NTS is NOT the right
    # VRG.

Reaching the respiratory_center (recommended consumer pattern —
NOTE the SIBLING container)::

    # The respiratory center is a SIBLING container of the right
    # NTS under medulla_oblongata — NOT a parent of the right NTS:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center
    #
    # Consumers must NOT expect to find the right NTS under
    # respiratory_center — resolve it via
    # solitary_nucleus.right.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"solitary_nucleus.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: the right and left NTS are TRULY SEPARATE
        # bilateral structures (ANATOMICAL, not a wiring
        # convention).

References
----------
*   **Canonical NTS anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Nucleus
    tractus solitarius; visceral afferent relay; taste,
    baroreceptor, chemoreceptor, and gastrointestinal afferents.)
*   **NTS — baroreflex afferent limb:** Andresen, M.C., Kunze,
    D.L. (1994). "Nucleus tractus solitarius — gateway to neural
    circulatory control." *Annual Review of Physiology*
    56:93–116. (NTS as the afferent limb of the baroreflex;
    baroreceptor and chemoreceptor afferent integration.)
*   **NTS — baroreflex arc:** Dampney, R.A.L. (1994).
    "Functional organization of central pathways regulating the
    cardiovascular system." *Physiological Reviews* 74:323–364.
    (NTS → CVLM → RVLM baroreflex arc; visceral afferent
    organization.)
*   **NTS — taste relay:** Norgren, R. (1995). "Gustatory
    system." In: Paxinos, G. (ed.), *The Rat Nervous System*,
    2nd ed. (NTS; rostral gustatory region; taste relay.)
*   **NTS — gastrointestinal afferents:** Travagli, R.A.,
    Anselmi, L. (2016). "Vagal neurocircuitry and its effects
    on gastrointestinal motility." *Current Opinion in
    Pharmacology* 31:1–7. (NTS; gastrointestinal vagal
    afferents; vagovagal reflex.)
*   **NTS — respiratory integration:** Kubin, L., Davies, R.O.
    (1988). "Central coordination of respiratory and sympathetic
    activities." *Annual Review of Physiology* 50:63–74. (NTS;
    respiratory and sympathetic integration.)
*   **NTS — dysautonomia:** Benarroch, E.E. (1993). "The central
    autonomic network: functional organization, dysfunction,
    and perspective." *Mayo Clinic Proceedings* 68:988–1001.
    (NTS as a key node in the central autonomic network;
    dysautonomia.)
*   **NTS — Wallenberg syndrome:** Sacco, R.L., et al. (1993).
    "Lateral medullary infarction: clinical and MRI correlation."
    *Stroke* 24:1981–1987. (Wallenberg syndrome; NTS involvement;
    autonomic instability; intractable hiccups.)
*   **NTS — baroreflex failure:** Robertson, D., et al. (1993).
    "Baroreflex failure: a new syndrome of hypertension and
    hypotension." *Hypertension* 21:496–501. (Baroreflex
    failure; NTS involvement.)
*   **Dorsal respiratory group (contrast — often considered part
    of the NTS in the literature):** Bianchi, A.L., et al.
    (1995). "Central control of breathing in mammals: neuronal
    circuitry, membrane properties, and neurotransmitters."
    *Physiological Reviews* 75:1–45. (DRG — a functional
    respiratory subregion within the ventrolateral NTS; wired
    separately in this tree.)
*   **RVLM (contrast — efferent limb):** Guyenet, P.G. (2006).
    "The sympathetic control of blood pressure." *Nature Reviews
    Neuroscience* 7:335–346. (RVLM — sympathetic premotor
    center; efferent limb of the baroreflex.)
*   **CVLM (contrast — sympathoinhibitory):** Schreihofer, A.M.,
    Guyenet, P.G. (2000). "Role of the ventrolateral medulla in
    sympathoinhibition." *American Journal of Physiology*
    279:R1701–R1711. (CVLM — sympathoinhibitory relay.)
*   **Area postrema (contrast — circumventricular):** Miller,
    A.D., Leslie, R.A. (1994). "The area postrema and vomiting."
    *Frontiers in Neuroendocrinology* 15:301–320. (Area postrema
    — circumventricular structure that PROJECTS TO the NTS.)
*   **Dorsal motor nucleus of the vagus (contrast — visceral
    motor):** Hopkins, D.A., Armour, J.A. (1984). "Localization
    of sympathetic postganglionic and parasympathetic
    preganglionic neurons which innervate different regions of
    the heart." *Journal of Comparative Neurology* 240:65–77.
    (Dorsal motor nucleus of the vagus — visceral motor
    (parasympathetic), DIFFERENT from the NTS.)
*   NeuroNames — Nucleus tractus solitarius; FMA — Nucleus of the
    solitary tract.
"""