"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
==========================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── solitary_nucleus
                └── left   <-- THIS MODULE

**Primary synonym:** Left solitary nucleus; left nucleus tractus
solitarius; left NTS; left nucleus of the solitary tract; left
nucleus solitarius; left solitary tract nucleus; left visceral
afferent nucleus of the medulla.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** in the **left dorsal medulla
oblongata** — the **left primary visceral afferent relay** of the
**brainstem**, receiving **left taste** (via **left CN VII, IX,
X**), **left baroreceptor** afferents (via **left CN IX, X**),
**left chemoreceptor** afferents (via **left CN IX, X**),
**left gastrointestinal** afferents (via **left CN X**), and
**left respiratory** afferents (via **left CN X**). It is **NOT**
a motor nucleus, **NOT** a sympathetic premotor center, **NOT** a
respiratory rhythm generator, **NOT** a circumventricular organ,
and **NOT** a reticular nucleus.
**Part of:** The **solitary_nucleus** bilateral container
(``.../medulla_oblongata/solitary_nucleus/``) — which is part of
the **medulla oblongata** — the **caudal brainstem** subdivision
of the **myelencephalon**. It is a **child** of the solitary
nucleus container — **NOT** a child of ``respiratory_center`` and
**NOT** a child of any other container. It is a **sibling** of
the **left DRG**, the **left RVLM**, the **left CVLM**, the
**left VRG**, and other left medullary containers.
**Structural parent:** ``.../solitary_nucleus/`` → **direct
child** of the solitary_nucleus container. The **left** leaf is
one of the **two** structural children of the container (the
other is ``right``).
**Structural children:** **None.** This is a **leaf** module. The
left NTS is represented as a **single structure** — it has **no
structural children** of its own.
**Boundary status (NOT the right solitary nucleus — the
contralateral leaf):** **Boundary case — the left NTS is NOT the
right NTS.** The **right NTS**
(``.../solitary_nucleus/right/``) is the **contralateral leaf** —
the NTS of the **right** medulla, relaying **right visceral
afferents**. **They are DIFFERENT LEAVES** — the ``left`` and
``right`` modules are the two sides of the **bilateral
container**. **Unlike the area postrema / CTZ** — which are
**midline** organs wired as left/right by convention — **the
left and right NTS are TRULY SEPARATE BILATERAL STRUCTURES**
(anatomical, not a wiring convention). Consumers must **not**
conflate the two.
**Boundary status (NOT the left dorsal respiratory group (DRG) —
a DIFFERENT child of respiratory_center even though OFTEN
CONSIDERED PART OF THE LEFT NTS in the literature):** **Boundary
case — the left NTS is NOT the left DRG IN THIS TREE, even
though the left DRG is often considered part of the left NTS in
the literature.** In the **literature**, the **left DRG** is a
**functional respiratory subregion** within the **ventrolateral
left NTS** — the left NTS **contains** the left DRG. **In this
tree**, however, they are **wired as separate modules**:
``.../solitary_nucleus/left/`` (this module) is a **child** of
the NTS container (a direct child of ``medulla_oblongata``);
``.../respiratory_center/dorsal_respiratory_group/left/`` (the
left DRG) is a **child** of ``respiratory_center``. **The tree
separates the left NTS and the left DRG into two modules** as a
**deliberate wiring choice** — the **left DRG** is a
**functional respiratory group within the left NTS region**; the
**left NTS** is the **broader visceral afferent relay** of which
the **left DRG** is a **functional subregion**. Consumers must
**not** expect to find the left DRG under
``solitary_nucleus.left`` — resolve it via
``respiratory_center.dorsal_respiratory_group.left``. Consumers
must **not** expect to find the left NTS under
``respiratory_center`` — resolve it via
``.../solitary_nucleus/left/``. **The two are separate modules**,
even though the **left DRG is anatomically within the left NTS
region** — the tree **separates** the **left NTS (visceral
afferent relay)** from the **left DRG (dorsal respiratory
pattern generator)**.
**Boundary status (NOT the left RVLM — the RVLM is the
SYMPATHETIC PREMOTOR efferent limb):** **Boundary case — the
left NTS is NOT the left rostral ventrolateral medulla (RVLM).**
The **left RVLM**
(``.../rostral_ventrolateral_medulla/left/``) is the **left
sympathetic premotor** center — the **efferent limb** of the
**left medullary baroreflex arc**. The **left NTS** (here) is the
**left visceral afferent relay** — the **afferent limb** of the
**left medullary baroreflex arc**. **They are DIFFERENT
STRUCTURES** — the **left NTS** is the **afferent** relay; the
**left RVLM** is the **efferent** sympathetic premotor center.
They are **functionally coupled** in the **left baroreflex arc**
(left NTS → left CVLM → left RVLM → left IML column) but are
**anatomically distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the left CVLM — the CVLM is the
SYMPATHOINHIBITORY relay):** **Boundary case — the left NTS is
NOT the left caudal ventrolateral medulla (CVLM).** The **left
CVLM** (``.../caudal_ventrolateral_medulla/left/``) is the
**left sympathoinhibitory** relay — it **inhibits the left
RVLM** (via **GABAergic** input from the **left NTS**). The
**left NTS** (here) is the **left visceral afferent relay** — it
**projects** to the left CVLM. **They are DIFFERENT
STRUCTURES** — the **left NTS** is the **afferent** relay; the
**left CVLM** is the **sympathoinhibitory** relay. Consumers
must **not** conflate the two.
**Boundary status (NOT the left area postrema or left CTZ — the
AP/CTZ PROJECT TO the left NTS, but are NOT the left NTS):**
**Boundary case — the left NTS is NOT the left area postrema or
the left chemoreceptor trigger zone.** The **left area
postrema** and **left chemoreceptor trigger zone**
(``.../respiratory_center/area_postrema/left/`` and
``.../respiratory_center/chemoreceptor_trigger_zone/left/``) are
**left circumventricular chemoreceptive** structures that
**project to** the **left NTS**. The **left NTS** (here) is the
**left visceral afferent relay** — it is the **downstream
target** of the **AP/CTZ emetic** and **autonomic** signals.
**They are DIFFERENT STRUCTURES** — the **left AP/CTZ** is the
**sensor**; the **left NTS** is the **relay**. Consumers must
**not** conflate the two.
**Boundary status (NOT the left dorsal motor nucleus of the vagus
— a DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the left NTS is NOT the left dorsal motor nucleus of the
vagus (DMV).** The **left DMV**
(``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``)
is the **left parasympathetic** motor nucleus — the **left
visceral motor** source of **left CN X**. The **left NTS**
(here) is the **left visceral afferent relay** — the **left
visceral sensory** source of **left CN VII, IX, X**. **They are
DIFFERENT STRUCTURES** — the **left DMV** is **visceral motor**
(parasympathetic); the **left NTS** is **visceral sensory**
(afferent relay). They are **anatomically adjacent** in the
**left dorsal medulla** — **both** are wired under different
containers. Consumers must **not** conflate the two.
**Boundary status (NOT the left hypoglossal nucleus — a
DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the left NTS is NOT the left hypoglossal nucleus.** The
**left hypoglossal nucleus**
(``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) is the
**left somatic motor** nucleus for the **tongue** — **NOT** a
visceral afferent relay. Consumers must **not** conflate the
two.
**Boundary status (NOT the left spinal trigeminal nucleus — a
DIFFERENT somatosensory relay):** **Boundary case — the left NTS
is NOT the left spinal trigeminal nucleus.** The **left spinal
trigeminal nucleus** is the **left facial pain/temperature**
sensory relay (CN V) — **NOT** a visceral afferent relay.
Consumers must **not** conflate the two.
**Boundary status (NOT the left RVLM / left CVLM / left NTS
baroreflex arc as a whole — a COMPONENT of it):** **Boundary
case — the left NTS is NOT the whole left medullary baroreflex
arc.** The **left NTS** is the **afferent limb** of the **left
medullary baroreflex arc** (left NTS → left CVLM → left RVLM →
left IML column). The **left CVLM** and **left RVLM** are the
**intermediate** and **efferent** limbs. **They are DIFFERENT
STRUCTURES** — the **left NTS** is the **afferent** relay; the
**left CVLM** and **left RVLM** are **downstream** autonomic
premotor structures. Consumers must **not** conflate the **left
NTS** with the **whole left baroreflex arc**.
**Boundary status (NOT the left VRG or left DRG — DIFFERENT
respiratory structures):** **Boundary case — the left NTS is NOT
the left ventral respiratory group (VRG) or the left dorsal
respiratory group (DRG).** The **left VRG**
(``.../ventral_respiratory_group/left/``) is the **left ventral
respiratory** rhythm and pattern generator group. The **left
DRG** (``.../respiratory_center/dorsal_respiratory_group/left/``)
is the **left dorsal respiratory** pattern generator — often
considered part of the left NTS in the literature but wired
separately in this tree. **They are DIFFERENT STRUCTURES** from
the left NTS — the **left NTS** is the **visceral afferent
relay**; the **left VRG and left DRG** are **respiratory**
structures. Consumers must **not** conflate the two.
**Boundary status (NOT the left Gi or the left paramedian
reticular nucleus — reticular nuclei in DIFFERENT containers):**
**Boundary case — the left NTS is NOT the left gigantocellular
reticular nucleus (Gi) or the left paramedian reticular
nucleus.** Those are **left reticular** nuclei with **broader**
functions — **NOT** the left visceral afferent relay. Consumers
must **not** conflate the left NTS with either.
**Boundary status (NOT the left arcuate nucleus or left
parafacial zone — ventral-surface-and-sleep-promoting
structures):** **Boundary case — the left NTS is NOT the left
arcuate nucleus or the left parafacial zone.** Those are **left
ventral-surface chemosensory** and **left sleep-promoting**
structures, respectively — **NOT** the left visceral afferent
relay. Consumers must **not** conflate the left NTS with either.
**Boundary status (NOT the whole solitary_nucleus container — an
ASPECT of it):** **Boundary case — the left NTS is NOT the whole
solitary_nucleus container.** The **whole solitary_nucleus**
(``.../solitary_nucleus/``) is the **bilateral container** that
**contains** the left NTS (here) **plus** the right NTS.
Consumers must **not** conflate the **leaf** with the
**container**.
**Boundary status (NOT the whole medulla oblongata — a visceral
afferent relay within it):** **Boundary case — the left NTS is
NOT the whole medulla oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the left NTS (via the solitary_nucleus container)
**plus** the RVLM, CVLM, VRG, respiratory centers, cranial nerve
nuclei, olivary body, medullary pyramid, arcuate nucleus,
parafacial zone, paramedian reticular nucleus, perihypoglossal
nuclei, and other structures. The **left NTS** is **one left
visceral afferent relay** within the medulla. Consumers must
**not** conflate the **left NTS** with the **whole medulla**.

Overview
--------
The **left solitary nucleus (left NTS)** — also known as the
**left nucleus tractus solitarius** — is the **left primary
visceral afferent relay** of the **brainstem**, in the **left
dorsal medulla oblongata**. It **receives** the **left visceral
afferent** fibers of **left CN VII** (taste from the **left
anterior tongue**), **left CN IX** (taste from the **left
posterior tongue**, baroreceptor and chemoreceptor afferents
from the **left carotid body/sinus**), and **left CN X** (taste
from the **left epiglottis**, baroreceptor and chemoreceptor
afferents from the **left aortic arch/body**, left
gastrointestinal afferents, left pulmonary afferents, and left
cardiac afferents). It **projects** to a wide range of **left
autonomic**, **left respiratory**, **left endocrine**, and
**left behavioral** targets — including the **left RVLM**,
**left CVLM**, **left DMV**, **left VRG**, **left parabrachial
nucleus**, **left hypothalamus**, and **left amygdala**.

**This is a LEAF module.** The **left NTS** is represented as a
**single structure** — it has **no structural children**.
Consumers that need **side-specific** resolution of the left side
use this module; consumers that need **right-side** resolution
use ``.../solitary_nucleus/right/``; consumers that need the
**whole solitary_nucleus container** use
``.../solitary_nucleus/``.

**The left NTS is the VISCERAL AFFERENT relay, NOT a motor
nucleus, NOT a sympathetic premotor center, NOT a respiratory
rhythm generator, and NOT a circumventricular organ.** It is a
**genuine left visceral sensory** relay — its classification as
the **left primary visceral afferent relay** is **functionally
accurate**.

**The left NTS is the AFFERENT LIMB of the left medullary
baroreflex arc — NOT the efferent limb.** The **left NTS**
receives **left baroreceptor** afferents via **left CN IX** and
**left CN X**. The **left CVLM**
(``.../caudal_ventrolateral_medulla/left/``) is the **left
sympathoinhibitory** relay; the **left RVLM**
(``.../rostral_ventrolateral_medulla/left/``) is the **left
sympathetic premotor** center. Together they form the **left
medullary baroreflex arc** (left NTS → left CVLM → left RVLM →
left IML column).

**The left NTS is OFTEN CONSIDERED TO INCLUDE THE LEFT DRG in the
literature.** The **left dorsal respiratory group (left DRG)**
is a **functional respiratory subregion** within the
**ventrolateral left NTS**. **In this tree**, the **left DRG is
wired separately** under ``respiratory_center`` — **NOT** under
the left NTS leaf. **The tree separates** the **left NTS
(visceral afferent relay)** from the **left DRG (dorsal
respiratory pattern generator)** as a **deliberate wiring
choice** — consumers must **not** expect to find the left DRG
under ``solitary_nucleus.left``.

**The left NTS is TRULY BILATERAL — the left / right split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **left** and **right**
NTS are **anatomically separate structures**. The **left / right
split** here reflects **anatomy** — **NOT** a **tree-wiring
convention**.

**The left NTS is functionally coupled to the left RVLM, left
CVLM, left DMV, left VRG, left DRG, left area postrema / CTZ,
left parabrachial nucleus, left hypothalamus, left amygdala,
and other higher centers.** It is **part of** the **left
medullary autonomic and respiratory network** — a **distributed
system** for **left visceral sensation**, **left autonomic
regulation**, **left respiratory modulation**, and **left
homeostatic control**.

The Left NTS / Right NTS Boundary
---------------------------------
This is the **ipsilateral / contralateral** boundary:

*   **Left NTS** (this module) — the NTS of the **left** medulla,
    relaying **left visceral afferents**.

*   **Right NTS** (``.../solitary_nucleus/right/``) — the NTS of
    the **right** medulla, relaying **right visceral afferents**.

**They are TRULY SEPARATE BILATERAL STRUCTURES** — the **left**
and **right** NTS are **anatomically distinct** (not a wiring
convention for a midline organ). They are **structurally
symmetric mirror pairs** — same cytoarchitecture, same
projections (with some crossed components), same **no warning**.
Consumers must **not** conflate the left with the right — resolve
the right side via ``solitary_nucleus.right``.

The Left NTS / Left Dorsal Respiratory Group (DRG) Boundary
-----------------------------------------------------------
This is the **most consequential** tree-wiring boundary:

*   **Left NTS** (this module) — the **left broader visceral
    afferent relay**.

*   **Left DRG**
    (``.../respiratory_center/dorsal_respiratory_group/left/``) —
    the **left dorsal respiratory** pattern generator — **often
    considered part of the left NTS in the literature**, but
    **wired separately** under ``respiratory_center`` in this
    tree.

**In this tree, they are SEPARATE MODULES.** The **left NTS** is
the **left broader visceral afferent relay**; the **left DRG** is
a **functional respiratory subregion** within the **ventrolateral
left NTS region** — **wired under a different container**. The
**tree separates** the two as a **deliberate wiring choice**.
Consumers must **not** expect to find the left DRG under
``solitary_nucleus.left`` — resolve it via
``respiratory_center.dorsal_respiratory_group.left``.

The Left NTS / Left RVLM Boundary
---------------------------------
This is the **afferent / efferent** boundary:

*   **Left NTS** (this module) — the **left visceral afferent
    relay**.

*   **Left RVLM** (``.../rostral_ventrolateral_medulla/left/``) —
    the **left sympathetic premotor** center.

**The left NTS is UPSTREAM of the left RVLM in the baroreflex
arc** — the left NTS receives **left baroreceptor** afferents and
**projects** to the left RVLM **directly** (glutamatergic and
GABAergic projections) and **via the left CVLM**. Consumers must
**not** conflate the two — the **left NTS** is the **afferent**
relay; the **left RVLM** is the **sympathetic premotor** center.

The Left NTS / Left CVLM Boundary
---------------------------------
This is the **afferent / sympathoinhibitory** boundary:

*   **Left NTS** (this module) — the **left visceral afferent
    relay**.

*   **Left CVLM** (``.../caudal_ventrolateral_medulla/left/``) —
    the **left sympathoinhibitory** relay.

**The left NTS is UPSTREAM of the left CVLM in the baroreflex
arc** — the left NTS receives **left baroreceptor** afferents and
**projects** to the left CVLM. Consumers must **not** conflate the
two — the **left NTS** is the **afferent** relay; the **left
CVLM** is the **sympathoinhibitory** relay.

The Left NTS / Left Area Postrema and Left CTZ Boundary
-------------------------------------------------------
This is the **visceral afferent / circumventricular** boundary:

*   **Left NTS** (this module) — the **left visceral afferent
    relay**.

*   **Left area postrema** and **left chemoreceptor trigger
    zone** (``.../respiratory_center/area_postrema/left/`` and
    ``.../respiratory_center/chemoreceptor_trigger_zone/left/``)
    — the **left circumventricular chemoreceptive** structures
    for the **vomiting reflex**.

**The left AP/CTZ PROJECT TO the left NTS** — the left NTS is the
**downstream target** of the left AP/CTZ emetic and autonomic
signals. **They are DIFFERENT STRUCTURES** — the **left AP/CTZ**
is the **sensor**; the **left NTS** is the **relay**. Consumers
must **not** conflate the two.

The Left NTS / Left Dorsal Motor Nucleus of the Vagus Boundary
--------------------------------------------------------------
This is the **sensory / motor** boundary:

*   **Left NTS** (this module) — the **left visceral sensory**
    afferent relay.

*   **Left dorsal motor nucleus of the vagus (DMV)**
    (``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``)
    — the **left visceral motor** (parasympathetic) nucleus.

**They are DIFFERENT STRUCTURES** — the **left DMV** is **visceral
motor** (parasympathetic); the **left NTS** is **visceral
sensory** (afferent relay). They are **anatomically adjacent** in
the **left dorsal medulla** but are **functionally distinct**.
Consumers must **not** conflate the two.

The Left NTS / Left Hypoglossal Nucleus and Left Spinal Trigeminal Nucleus Boundary
------------------------------------------------------------------------------------
This is the **visceral afferent / somatic** boundary:

*   **Left NTS** (this module) — the **left visceral sensory**
    afferent relay.

*   **Left hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``) —
    the **left somatic motor** nucleus.

*   **Left spinal trigeminal nucleus** — the **left facial
    pain/temperature** sensory relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the **left NTS** with either.

The Left NTS / Left VRG Boundary
--------------------------------
This is the **visceral afferent / ventral respiratory** boundary:

*   **Left NTS** (this module) — the **left visceral afferent
    relay**.

*   **Left VRG** (``.../ventral_respiratory_group/left/``) — the
    **left ventral respiratory** rhythm and pattern generator
    group.

**They are DIFFERENT STRUCTURES** — the **left NTS** is the **left
visceral afferent relay**; the **left VRG** is a **left
respiratory rhythm generator**. They are **functionally coupled**
(the left NTS **projects** to the left VRG to **modulate** left
respiratory pattern) but are **anatomically distinct**. Consumers
must **not** conflate the two.

The Left NTS / Other Left Medullary Structures Boundary
------------------------------------------------------
This is the **visceral afferent / other-medullary-structures**
boundary:

*   **Left NTS** (this module) — the **left visceral afferent
    relay**.

*   **Left Gi, left paramedian reticular nucleus, left arcuate
    nucleus, left parafacial zone, left olivary body, left
    medullary pyramid, left perihypoglossal nuclei, left cranial
    nerve nuclei** — **other left medullary structures**.

**Each is a DIFFERENT STRUCTURE.** Consumers must **not** conflate
the **left NTS** with any of these.

The Left NTS / Whole Solitary Nucleus Container and Whole Medulla Oblongata Boundary
-----------------------------------------------------------------------------------
This is the **leaf / container** boundary:

*   **Left NTS** (this module) — one **leaf** of the
    ``solitary_nucleus`` container.

*   **Solitary nucleus** (``.../solitary_nucleus/``) — the
    **bilateral container** of the left + right NTS.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the NTS container and other medullary
    structures.

**The left NTS is a LEAF in a CHAIN of containers.** Consumers must
**not** conflate the **leaf** with any of the **parent
containers**.

**The left NTS is NOT a child of respiratory_center.** The
**respiratory_center** is a **sibling container** of the NTS —
**NOT** a parent. Consumers must **not** expect to find the left
NTS under ``respiratory_center``.

Function in the Human Brain
---------------------------
The left NTS's function is **left visceral afferent relay** —
**NOT motor control**, **NOT sympathetic premotor**, and **NOT
respiratory rhythm generation**:

*   **Left taste relay:** The **left NTS** receives **left taste**
    afferents from the **left anterior tongue** (via **left CN
    VII**), **left posterior tongue** (via **left CN IX**), and
    **left epiglottis** (via **left CN X**) — and it **relays**
    them to the **left parabrachial nucleus** and the **left
    thalamus** (VPM) for **conscious taste perception**, and to
    the **left hypothalamus** and **left amygdala** for
    **affective** and **homeostatic** responses to taste.

*   **Left baroreceptor relay:** The **left NTS** receives **left
    baroreceptor** afferents from the **left carotid sinus** (via
    **left CN IX**) and the **left aortic arch** (via **left CN
    X**) — and it **initiates the left baroreflex** by
    **projecting** to the **left CVLM** (which **inhibits the
    left RVLM**) and to the **left DMV** (for **left
    parasympathetic** cardiac **slowing**). This is the **left
    afferent limb** of the **left medullary baroreflex arc**.

*   **Left chemoreceptor relay:** The **left NTS** receives **left
    chemoreceptor** afferents from the **left carotid body** (via
    **left CN IX**) and the **left aortic body** (via **left CN
    X**) — and it **initiates the left chemoreflex** by
    **projecting** to the **left VRG** (for **left respiratory**
    **stimulation**) and to the **left RVLM** (for **left
    sympathetic** **activation**).

*   **Left gastrointestinal relay:** The **left NTS** receives
    **left gastrointestinal** afferents (via **left CN X**) and
    **projects** to the **left DMV** (for **left
    gastrointestinal** **parasympathetic** control), the **left
    parabrachial nucleus** (for **left visceral** **sensation**),
    and the **left hypothalamus** (for **food intake** and
    **metabolic** regulation).

*   **Left respiratory relay:** The **left NTS** receives **left
    pulmonary** afferents (via **left CN X**) — **pulmonary
    stretch receptor** signals and **irritant receptor** signals
    — and it **projects** to the **left VRG** and **left DRG**
    (for **left respiratory** **pattern modulation**).

*   **Left cardiac relay:** The **left NTS** receives **left
    cardiac** afferents (via **left CN X**) — and it **projects**
    to the **left DMV** (for **left parasympathetic** **cardiac**
    control) and the **left RVLM** (for **left sympathetic**
    **cardiac** control).

*   **NOT motor control:** The **left NTS** does **not** send
    motor axons to muscles.

*   **NOT sympathetic premotor:** The **sympathetic premotor**
    function is the **left RVLM** — **NOT** the left NTS.

*   **NOT respiratory rhythm generation:** The **respiratory
    rhythm** is generated by the **pre-Bötzinger complex** (left
    VRG) — **NOT** the left NTS.

**The unifying theme:** the left NTS is the **left primary
visceral afferent relay** of the **brainstem** — it **receives**
left taste, baroreceptor, chemoreceptor, gastrointestinal,
pulmonary, and cardiac afferents via **left CN VII, IX, X** — and
it **projects** to the **left RVLM**, **left CVLM**, **left
DMV**, **left VRG**, **left parabrachial nucleus**, **left
hypothalamus**, and **left amygdala** to **initiate** the **left
baroreflex**, **left chemoreflex**, **left gastrointestinal**,
and **left respiratory** **reflexes** — **NOT** a motor nucleus,
**NOT** a sympathetic premotor center, and **NOT** a respiratory
rhythm generator.

Associated Disorders
--------------------
The left NTS is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct**, via **left
visceral afferent** dysfunction (though the **whole-body** clinical
phenotypes — baroreflex failure, dysautonomia, etc. — are
typically **bilateral** because the NTSs work together):

*   **Baroreflex failure (via bilateral NTS dysfunction — left
    NTS contributes):** **Damage** to the **left NTS** — from
    **stroke**, **demyelination**, **tumor**, or **surgical**
    **injury** — **disrupts** the **left afferent limb** of the
    **baroreflex** — causing **baroreflex failure**: **labile
    blood pressure**, **orthostatic hypotension**,
    **hypertensive crises**, and **loss of heart-rate
    variability**. The **left NTS** is a **contributing
    substrate** — the **right NTS** and **higher centers**
    can partially compensate.

*   **Dysautonomia / autonomic failure (via left NTS dysfunction):
    ** **Damage** to the **left NTS** can **contribute** to
    **dysautonomia** — **orthostatic hypotension**,
    **gastrointestinal** **dysmotility**, **cardiac**
    **arrhythmias**, and **thermoregulatory** dysfunction.

*   **Neurogenic hypertension (via left NTS dysfunction —
    hypothesized in some models):** **Impaired** left NTS
    **baroreceptor** input can **contribute** to **neurogenic
    hypertension** by **reducing** the **baroreflex buffering**
    of **sympathetic outflow**.

*   **Brainstem stroke (via left NTS involvement):** **Left
    Wallenberg syndrome (left lateral medullary syndrome)**
    **frequently** **involves** the **left NTS** — contributing
    to **autonomic instability**, **intractable hiccups**,
    **nausea**, and **cardiovascular** dysfunction.

*   **Taste disorders (via left NTS dysfunction):** **Damage** to
    the **left rostral NTS** can cause **left-sided** **taste
    loss** (ageusia, hypogeusia) or **dysgeusia**. The **left
    NTS** is the **left first central** **taste relay**.

*   **Gastrointestinal dysmotility (via left NTS dysfunction):**
    **Damage** to the **left NTS** can **contribute** to
    **gastroparesis**, **constipation**, or **dysphagia** via
    **impaired** **left visceral afferent** and
    **parasympathetic** **reflexes**.

*   **No Named "Left NTS Syndrome":** The left NTS is a **left
    visceral afferent relay** — its clinical syndromes are
    **named for the broader clinical entity** (baroreflex
    failure, dysautonomia, Wallenberg syndrome) or the **broader
    lesion** — **NOT** for the left NTS itself. There is **no
    named "left NTS syndrome"**.

**What is NOT here:** The left NTS is **not** the substrate for
**sympathetic premotor** function (left RVLM),
**sympathoinhibition** (left CVLM), **respiratory rhythm
generation** (left VRG), **dorsal respiratory pattern generation**
(left DRG), **emesis** (left area postrema / left CTZ), **tongue
weakness** (left hypoglossal nucleus), or **parasympathetic
dysfunction** (left dorsal motor nucleus of the vagus). Its
clinical relevance is the **left visceral afferent** functions
listed above.

Lateralization Notes
--------------------
This is the **left** NTS module. The solitary nucleus is a
**bilateral container** whose two sides are **ANATOMICALLY
SEPARATE** — **not** a wiring convention for a midline organ
(unlike the area postrema / CTZ) — and it carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right** NTS are
    **structurally symmetric** — they are **mirror pairs** with
    the **same** cytoarchitecture, **same** projections (with
    some crossed components), and **same** functions. The
    **left** NTS is in the **left dorsal medulla**; the **right**
    NTS is in the **right dorsal medulla**.

*   **Predominantly Ipsilateral, Partly Crossed Projections:** The
    **left NTS** projects **predominantly ipsilaterally** (to the
    **left RVLM**, **left CVLM**, **left DMV**, **left VRG**,
    **left parabrachial**) — with some **crossed** projections
    via **commissural** pathways. This **functional
    ipsilaterality** is **part of the autonomic and respiratory
    network's bilateral coordination** — the **left and right
    NTS** together coordinate **visceral reflexes** bilaterally.

*   **NO Lateralization Warning:** The NTS has **no known
    functional lateralization** in humans — the **left** and
    **right** NTS are **functionally symmetric** at the
    **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the left NTS — the **left**
    and **right** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The left NTS is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the left NTS.

*   **NO Fear-Output Warning:** The left NTS is **not** a
    fear-output structure — it is a **left visceral afferent
    relay**. Consumers must **not** conflate it with the
    **central nucleus** or with the **amygdala**.

**A consumer that assumes "left NTS = right NTS" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The NTS is
a **strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The left NTS is a **leaf** —
    it does **not** import from ``.../right/`` or any other
    right-side module. The **left / right split** is
    **ANATOMICAL** — not a **wiring convention**. The **left**
    and **right** NTS are **truly separate bilateral
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
    other container. The left NTS's relationships to the left
    DRG, left RVLM, left CVLM, left area postrema, left CTZ,
    left dorsal motor nucleus of the vagus, left hypoglossal
    nucleus, left spinal trigeminal nucleus, left VRG, left Gi,
    left paramedian reticular nucleus, left arcuate nucleus, and
    left parafacial zone are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The left NTS is a
    **single structure** — it has **no structural children**.
    Consumers must **not** expect further sub-paths under
    ``.../left/``.
*   **ANATOMICAL BILATERALITY, NOT a wiring convention.** The
    ``left`` and ``right`` NTS are **anatomically separate
    structures** — unlike the **area postrema** / **CTZ** (which
    are midline organs wired as left/right by convention).
*   **VISCERAL AFFERENT RELAY — the left primary visceral
    sensory relay of the brainstem.** The left NTS is a
    **genuine left visceral afferent relay** — **NOT** a motor
    nucleus, **NOT** a sympathetic premotor center, **NOT** a
    respiratory rhythm generator, and **NOT** a circumventricular
    organ.
*   **NOT the left DRG.** The **left DRG** is a **functional
    respiratory subregion** within the **left NTS region** —
    **often considered part of the left NTS in the literature**,
    but **wired separately** under ``respiratory_center`` in
    this tree. Consumers must **not** expect to find the left DRG
    under ``solitary_nucleus.left``.
*   **NOT the left RVLM or left CVLM.** Those are the **efferent
    limb** (left RVLM) and **sympathoinhibitory** relay (left
    CVLM) of the **left medullary baroreflex arc** — **NOT** the
    **afferent** relay (left NTS).
*   **NOT the left area postrema or left CTZ.** Those are **left
    circumventricular chemoreceptive** structures that **project
    to** the left NTS.
*   **NOT the left dorsal motor nucleus of the vagus.** The **left
    DMV** is **visceral motor** (parasympathetic); the **left
    NTS** is **visceral sensory** (afferent relay).
*   **NOT the left hypoglossal nucleus or left spinal trigeminal
    nucleus.** Those are **somatic motor** and **facial
    somatosensory** structures, respectively.
*   **NOT the left VRG.** The left VRG is a **respiratory rhythm
    generator** — the left NTS **projects to** the left VRG, but
    is **NOT** the left VRG.
*   **NOT the left Gi, left paramedian reticular nucleus, left
    arcuate nucleus, or left parafacial zone.** Each is a
    **different structure**.
*   **NOT the whole solitary_nucleus or whole medulla oblongata.**
    The left NTS is a **leaf** in a **chain** of containers.
*   **No ``AREA_PATHS`` hop.** The left NTS is a **local leaf** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The left NTS has no nested
    dual-framing module. It is a **single leaf**.
*   **Structural parity with the right NTS — strict mirror with
    NO warning.** The left and right modules are **structurally
    identical** — same leaf status, same **visceral afferent**
    framing, same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus import left

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "solitary_nucleus.left"
    )

**Do not** expect to find the **left DRG** under
``solitary_nucleus.left``. The **left DRG** is **often considered
part of the left NTS in the literature**, but it is **wired
separately** under ``respiratory_center`` in this tree. Resolve
the left DRG via
``respiratory_center.dorsal_respiratory_group.left``.

**Do not** assume the left NTS is the **left RVLM** or **left
CVLM**. Those are the **efferent limb** and **sympathoinhibitory**
relay of the **left medullary baroreflex arc** — **NOT** the
**afferent** relay (left NTS).

**Do not** assume the left NTS is the **left area postrema** or
**left CTZ**. Those are **left circumventricular chemoreceptive**
structures that **project to** the left NTS.

**Do not** assume the left NTS is the **left dorsal motor nucleus
of the vagus**. The **left DMV** is **visceral motor**
(parasympathetic); the **left NTS** is **visceral sensory**
(afferent relay).

**Do not** assume the left NTS is the **left hypoglossal nucleus**
or the **left spinal trigeminal nucleus**. Those are **somatic
motor** and **facial somatosensory** structures, respectively.

**Do not** assume the left NTS is the **left VRG**. The left VRG
is a **respiratory rhythm generator** — the left NTS **projects
to** the left VRG, but is **NOT** the left VRG.

**Do not** assume the left NTS is the **left Gi**, the **left
paramedian reticular nucleus**, the **left arcuate nucleus**, or
the **left parafacial zone**. Each is a **different structure**.

**Do not** assume the left NTS is the **right NTS**. The right
NTS is the **separate leaf** at ``.../solitary_nucleus/right/``.

**Do not** assume the left NTS has **structural children**. It
is a **leaf** — it represents the left NTS as a **single
structure**.

**Do not** infer **midline wiring convention** from the left NTS
structure. The **left / right split** is **ANATOMICAL** — the
**left** and **right** NTS are **truly separate bilateral
structures**.

Iterating the left NTS's (empty) children (recommended consumer
pattern)::

    LEFT_SOLITARY_NUCLEUS_CHILDREN = ()
    # The left NTS is a leaf. It has no structural children.

Reaching the right NTS (recommended consumer pattern — the
contralateral leaf, a TRULY SEPARATE structure)::

    # The right NTS is the CONTRALATERAL leaf:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
    #
    # The left and right NTS are TRULY SEPARATE BILATERAL
    # STRUCTURES (anatomical, not a wiring convention).

Reaching the left DRG (recommended consumer pattern — NOTE the
DIFFERENT container, OFTEN CONSIDERED PART OF THE LEFT NTS in
the literature)::

    # The left dorsal respiratory group is a CHILD of
    # respiratory_center — wired SEPARATELY from the left NTS in
    # this tree, even though the left DRG is often considered
    # part of the left NTS in the literature:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group.left
    #
    # The tree separates the left NTS (visceral afferent relay)
    # from the left DRG (dorsal respiratory pattern generator) as
    # a deliberate wiring choice.

Reaching the left RVLM and left CVLM (recommended consumer
pattern — NOTE the DIFFERENT containers)::

    # The left RVLM and left CVLM are the EFFERENT limb and
    # SYMPATHOINHIBITORY relay of the left medullary baroreflex
    # arc — SEPARATE containers:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla.left
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla.left
    #
    # The left NTS is the AFFERENT limb of the baroreflex arc —
    # it PROJECTS to the left CVLM (which inhibits the left RVLM)
    # and to the left RVLM directly. They are DIFFERENT
    # structures.

Reaching the left area postrema and left CTZ (recommended
consumer pattern — NOTE the DIFFERENT children of
respiratory_center)::

    # The left area postrema and left chemoreceptor trigger zone
    # are CIRCUMVENTRICULAR structures that PROJECT TO the left
    # NTS — leaves of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone.left
    #
    # They are DIFFERENT structures from the left NTS — the left
    # AP/CTZ is the sensor; the left NTS is the relay.

Reaching the left dorsal motor nucleus of the vagus (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The left dorsal motor nucleus of the vagus is a VISCERAL
    # MOTOR (parasympathetic) nucleus — a separate container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.dorsal_motor_nucleus_vagus
    #
    # The left NTS is the VISCERAL SENSORY (afferent relay) —
    # they are functionally paired but anatomically distinct.

Reaching the left VRG (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The left ventral respiratory group is a RESPIRATORY
    # structure — a separate container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group.left
    #
    # The left NTS PROJECTS to the left VRG (to modulate
    # respiratory pattern) — but the left NTS is NOT the left VRG.

Reaching the respiratory_center (recommended consumer pattern —
NOTE the SIBLING container)::

    # The respiratory center is a SIBLING container of the left
    # NTS under medulla_oblongata — NOT a parent of the left NTS:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center
    #
    # Consumers must NOT expect to find the left NTS under
    # respiratory_center — resolve it via
    # solitary_nucleus.left.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"solitary_nucleus.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: the left and right NTS are TRULY SEPARATE
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