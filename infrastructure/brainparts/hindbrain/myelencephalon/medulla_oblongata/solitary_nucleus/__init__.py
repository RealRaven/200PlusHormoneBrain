"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
=====================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── solitary_nucleus   <-- THIS MODULE
                ├── left
                └── right

**Primary synonym:** Solitary nucleus; nucleus tractus solitarius;
NTS; nucleus of the solitary tract; nucleus solitarius; solitary
tract nucleus; visceral afferent nucleus of the medulla.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**medullary grey-matter nucleus** in the **dorsal medulla
oblongata** — the **primary visceral afferent relay** of the
**brainstem**, receiving **taste** (via **CN VII, IX, X**),
**baroreceptor** afferents (via **CN IX, X**),
**chemoreceptor** afferents (via **CN IX, X**),
**gastrointestinal** afferents (via **CN X**), and **respiratory**
afferents (via **CN X**). It is **NOT** a motor nucleus, **NOT**
a sympathetic premotor center, **NOT** a respiratory rhythm
generator, **NOT** a circumventricular organ, and **NOT** a
reticular nucleus.
**Part of:** The **medulla oblongata** — the **caudal brainstem**
subdivision of the **myelencephalon**. It is a **direct child**
of ``medulla_oblongata`` — **NOT** a child of
``respiratory_center`` and **NOT** a child of any other
container. It is a **sibling** of ``respiratory_center``,
``rostral_ventrolateral_medulla``,
``caudal_ventrolateral_medulla``, ``ventral_respiratory_group``,
and other medullary containers.
**Structural parent:** ``.../medulla_oblongata/`` → **direct
child** of the medulla oblongata container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** solitary
nucleus. **Anatomically**, the left and right NTS are **truly
separate bilateral structures** (unlike the area postrema, which
is a midline organ wired as left/right by convention) — the
**left NTS** relays **left visceral afferents**; the **right
NTS** relays **right visceral afferents**.
**Boundary status (NOT the dorsal respiratory group (DRG) — a
DIFFERENT child of respiratory_center even though OFTEN
CONSIDERED PART OF THE NTS in the literature):** **Boundary case
— the solitary nucleus (NTS) is NOT the dorsal respiratory group
(DRG) IN THIS TREE, even though the DRG is often considered part
of the NTS in the literature.** In the **literature**, the
**DRG** is a **functional respiratory subregion** within the
**ventrolateral NTS** — the NTS **contains** the DRG. **In this
tree**, however, they are **wired as separate containers**:
``.../solitary_nucleus/`` (this module) is a **direct child** of
``medulla_oblongata``; ``.../respiratory_center/dorsal_respiratory_group/``
(the DRG) is a **child** of ``respiratory_center``. **The tree
separates the NTS and the DRG into two modules** as a **deliberate
wiring choice** — the **DRG** is a **functional respiratory
group within the NTS region**; the **NTS** is the **broader
visceral afferent relay** of which the **DRG** is a **functional
subregion**. Consumers must **not** expect to find the DRG under
``solitary_nucleus`` — resolve it via
``respiratory_center.dorsal_respiratory_group``. Consumers must
**not** expect to find the NTS under
``respiratory_center`` — resolve it via
``.../solitary_nucleus/``. **The two are separate modules**, even
though the **DRG is anatomically within the NTS region** — the
tree **separates** the **NTS (visceral afferent relay)** from
the **DRG (dorsal respiratory pattern generator)**.
**Boundary status (NOT the RVLM — the RVLM is the SYMPATHETIC
PREMOTOR efferent limb):** **Boundary case — the NTS is NOT the
rostral ventrolateral medulla (RVLM).** The **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor** center — the **efferent limb** of the **medullary
baroreflex arc**. The **NTS** (here) is the **visceral afferent
relay** — the **afferent limb** of the **medullary baroreflex
arc**. **They are DIFFERENT STRUCTURES** — the **NTS** is the
**afferent** relay; the **RVLM** is the **efferent**
sympathetic premotor center. They are **functionally coupled** in
the **baroreflex arc** (NTS → CVLM → RVLM → IML column) but are
**anatomically distinct**. Consumers must **not** conflate the
two.
**Boundary status (NOT the CVLM — the CVLM is the
SYMPATHOINHIBITORY relay):** **Boundary case — the NTS is NOT
the caudal ventrolateral medulla (CVLM).** The **CVLM**
(``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay — it **inhibits the RVLM** (via
**GABAergic** input from the **NTS**). The **NTS** (here) is the
**visceral afferent relay** — it **projects** to the CVLM. **They
are DIFFERENT STRUCTURES** — the **NTS** is the **afferent**
relay; the **CVLM** is the **sympathoinhibitory** relay.
Consumers must **not** conflate the two.
**Boundary status (NOT the area postrema or CTZ — the AP/CTZ
PROJECT TO the NTS, but are NOT the NTS):** **Boundary case —
the NTS is NOT the area postrema or the chemoreceptor trigger
zone.** The **area postrema** and **chemoreceptor trigger zone**
(``.../respiratory_center/area_postrema/`` and
``.../respiratory_center/chemoreceptor_trigger_zone/``) are
**circumventricular chemoreceptive** structures that **project
to** the **NTS**. The **NTS** (here) is the **visceral afferent
relay** — it is the **downstream target** of the **AP/CTZ
emetic** and **autonomic** signals. **They are DIFFERENT
STRUCTURES** — the **AP/CTZ** is the **sensor**; the **NTS** is
the **relay**. Consumers must **not** conflate the two.
**Boundary status (NOT the dorsal motor nucleus of the vagus —
a DIFFERENT structure with a DIFFERENT function):** **Boundary
case — the NTS is NOT the dorsal motor nucleus of the vagus
(DMV).** The **DMV**
(``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``
and
``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
is the **parasympathetic** motor nucleus — the **visceral
motor** source of **CN X**. The **NTS** (here) is the **visceral
afferent relay** — the **visceral sensory** source of **CN
VII, IX, X**. **They are DIFFERENT STRUCTURES** — the **DMV** is
**visceral motor** (parasympathetic); the **NTS** is **visceral
sensory** (afferent relay). They are **anatomically adjacent**
in the **dorsal medulla** — **both** are wired under different
containers. Consumers must **not** conflate the two.
**Boundary status (NOT the hypoglossal nucleus — a DIFFERENT
structure with a DIFFERENT function):** **Boundary case — the
NTS is NOT the hypoglossal nucleus.** The **hypoglossal
nucleus** (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/``
and
``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) is the
**somatic motor** nucleus for the **tongue** — **NOT** a
visceral afferent relay. Consumers must **not** conflate the two.
**Boundary status (NOT the spinal trigeminal nucleus — a DIFFERENT
somatosensory relay):** **Boundary case — the NTS is NOT the
spinal trigeminal nucleus.** The **spinal trigeminal nucleus** is
the **facial pain/temperature** sensory relay (CN V) — **NOT** a
visceral afferent relay. Consumers must **not** conflate the two.
**Boundary status (NOT the RVLM / CVLM / NTS baroreflex arc as a
whole — a COMPONENT of it):** **Boundary case — the NTS is NOT
the whole medullary baroreflex arc.** The **NTS** is the
**afferent limb** of the **medullary baroreflex arc** (NTS →
CVLM → RVLM → IML column). The **CVLM** and **RVLM** are the
**intermediate** and **efferent** limbs. **They are DIFFERENT
STRUCTURES** — the **NTS** is the **afferent** relay; the **CVLM**
and **RVLM** are **downstream** autonomic premotor structures.
Consumers must **not** conflate the **NTS** with the **whole
baroreflex arc**.
**Boundary status (NOT the VRG or DRG — DIFFERENT respiratory
structures):** **Boundary case — the NTS is NOT the ventral
respiratory group (VRG) or the dorsal respiratory group (DRG).**
The **VRG** (``.../ventral_respiratory_group/``) is the
**ventral respiratory** rhythm and pattern generator group. The
**DRG** (``.../respiratory_center/dorsal_respiratory_group/``) is
the **dorsal respiratory** pattern generator — often considered
part of the NTS in the literature but wired separately in this
tree. **They are DIFFERENT STRUCTURES** from the NTS — the **NTS**
is the **visceral afferent relay**; the **VRG and DRG** are
**respiratory** structures. Consumers must **not** conflate the
two.
**Boundary status (NOT the Gi or the paramedian reticular nucleus
— reticular nuclei in DIFFERENT containers):** **Boundary case —
the NTS is NOT the gigantocellular reticular nucleus (Gi) or the
paramedian reticular nucleus.** Those are **reticular** nuclei
with **broader** functions — **NOT** the visceral afferent relay.
Consumers must **not** conflate the NTS with either.
**Boundary status (NOT the arcuate nucleus or parafacial zone —
ventral-surface-and-sleep-promoting structures):** **Boundary
case — the NTS is NOT the arcuate nucleus or the parafacial
zone.** Those are **ventral-surface chemosensory** and
**sleep-promoting** structures, respectively — **NOT** the
visceral afferent relay. Consumers must **not** conflate the NTS
with either.
**Boundary status (NOT the whole medulla oblongata — a visceral
afferent relay within it):** **Boundary case — the NTS is NOT
the whole medulla oblongata.** The **medulla oblongata**
(``.../medulla_oblongata/``) is the **parent container** — it
contains the NTS (here) **plus** the RVLM, CVLM, VRG, respiratory
centers, cranial nerve nuclei, olivary body, medullary pyramid,
arcuate nucleus, parafacial zone, paramedian reticular nucleus,
perihypoglossal nuclei, and other structures. The **NTS** is
**one visceral afferent relay** within the medulla. Consumers
must **not** conflate the **NTS** with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
ANATOMICALLY SEPARATE structures):** **Boundary case — the NTS
is a BILATERAL container whose left and right children are
ANATOMICALLY SEPARATE.** Unlike the **area postrema** (a
**midline** organ wired as left/right by convention), the **NTS**
is a **truly paired** medullary structure — the **left NTS** is
in the **left dorsal medulla**; the **right NTS** is in the
**right dorsal medulla**. **The left / right split here is
ANATOMICAL, not a wiring convention.** Consumers must **not**
infer **midline wiring convention** from the NTS (that
convention applies to the area postrema / CTZ, NOT the NTS).

Overview
--------
The **solitary nucleus (NTS)** — also known as the **nucleus
tractus solitarius** — is the **primary visceral afferent relay**
of the **brainstem**, in the **dorsal medulla oblongata**. It
**receives** the **visceral afferent** fibers of **CN VII**
(taste from the anterior tongue), **CN IX** (taste from the
posterior tongue, baroreceptor and chemoreceptor afferents from
the carotid body/sinus), and **CN X** (taste from the epiglottis,
baroreceptor and chemoreceptor afferents from the aortic
arch/body, gastrointestinal afferents, pulmonary afferents, and
cardiac afferents). It **projects** to a wide range of
**autonomic**, **respiratory**, **endocrine**, and **behavioral**
targets — including the **RVLM**, **CVLM**, **DMV**, **VRG**,
**parabrachial nucleus**, **hypothalamus**, and **amygdala**.

**The NTS is the VISCERAL AFFERENT relay, NOT a motor nucleus,
NOT a sympathetic premotor center, NOT a respiratory rhythm
generator, and NOT a circumventricular organ.** It is a
**genuine visceral sensory** relay — its classification as the
**primary visceral afferent relay** is **functionally accurate**.

**The NTS is the AFFERENT LIMB of the medullary baroreflex arc —
NOT the efferent limb.** The **NTS** receives
**baroreceptor** afferents via **CN IX** and **CN X**. The
**CVLM** (``.../caudal_ventrolateral_medulla/``) is the
**sympathoinhibitory** relay; the **RVLM**
(``.../rostral_ventrolateral_medulla/``) is the **sympathetic
premotor** center. Together they form the **medullary
baroreflex arc** (NTS → CVLM → RVLM → IML column).

**The NTS is OFTEN CONSIDERED TO INCLUDE THE DRG in the
literature.** The **dorsal respiratory group (DRG)** is a
**functional respiratory subregion** within the **ventrolateral
NTS**. **In this tree**, the **DRG is wired separately** under
``respiratory_center`` — **NOT** under the NTS container. **The
tree separates** the **NTS (visceral afferent relay)** from the
**DRG (dorsal respiratory pattern generator)** as a
**deliberate wiring choice** — consumers must **not** expect to
find the DRG under ``solitary_nucleus``.

**The NTS is TRULY BILATERAL — the left / right split is
ANATOMICAL.** Unlike the **area postrema** (a **midline** organ
wired as left/right by convention), the **left** and **right**
NTS are **anatomically separate structures**. The **left / right
split** here reflects **anatomy** — **NOT** a **tree-wiring
convention**.

**The NTS is functionally coupled to the RVLM, CVLM, DMV, VRG,
DRG, area postrema / CTZ, parabrachial nucleus, hypothalamus,
amygdala, and other higher centers.** It is **part of** the
**medullary autonomic and respiratory network** — a
**distributed system** for **visceral sensation**,
**autonomic regulation**, **respiratory modulation**, and
**homeostatic control**.

Bilateral Structure (Anatomical Pairing)
---------------------------------------
The solitary nucleus is a **bilateral container** in this tree
with **two structural children**:

*   ``left`` — the **left** NTS (a **leaf** module).
*   ``right`` — the **right** NTS (a **leaf** module).

**The two children are ANATOMICALLY SEPARATE structures** —
**NOT** a wiring convention for a midline organ (unlike the
area postrema / CTZ). The **left NTS** is in the **left dorsal
medulla**; the **right NTS** is in the **right dorsal medulla**.

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **NTS** as **single structures**. Consumers
that need **side-specific** resolution descend into ``left`` or
``right``; consumers that need the **whole bilateral pair** use
``solitary_nucleus`` (the container) as a whole.

**The container itself is unpaired.** There is **no**
``solitary_nucleus/left/.../`` structural hierarchy beyond the
single leaf level — the ``left`` and ``right`` modules are the
**terminal modules** for this structure.

The NTS / Dorsal Respiratory Group (DRG) Boundary
-------------------------------------------------
This is the **most consequential** tree-wiring boundary:

*   **Solitary nucleus (NTS)** (this module) — the **broader
    visceral afferent relay**.

*   **Dorsal respiratory group (DRG)**
    (``.../respiratory_center/dorsal_respiratory_group/``) — the
    **dorsal respiratory** pattern generator — **often considered
    part of the NTS in the literature**, but **wired separately**
    under ``respiratory_center`` in this tree.

**In this tree, they are SEPARATE MODULES.** The **NTS** is the
**broader visceral afferent relay**; the **DRG** is a
**functional respiratory subregion** within the **ventrolateral
NTS region** — **wired under a different container**. The **tree
separates** the two as a **deliberate wiring choice**. Consumers
must **not** expect to find the DRG under ``solitary_nucleus``
— resolve it via
``respiratory_center.dorsal_respiratory_group``.

The NTS / RVLM Boundary
-----------------------
This is the **afferent / efferent** boundary:

*   **NTS** (this module) — the **visceral afferent relay**.

*   **RVLM** (``.../rostral_ventrolateral_medulla/``) — the
    **sympathetic premotor** center.

**The NTS is UPSTREAM of the RVLM in the baroreflex arc** — the
NTS receives **baroreceptor** afferents and **projects** to the
RVLM **directly** (glutamatergic and GABAergic projections) and
**via the CVLM**. Consumers must **not** conflate the two — the
**NTS** is the **afferent** relay; the **RVLM** is the
**sympathetic premotor** center.

The NTS / CVLM Boundary
-----------------------
This is the **afferent / sympathoinhibitory** boundary:

*   **NTS** (this module) — the **visceral afferent relay**.

*   **CVLM** (``.../caudal_ventrolateral_medulla/``) — the
    **sympathoinhibitory** relay.

**The NTS is UPSTREAM of the CVLM in the baroreflex arc** — the
NTS receives **baroreceptor** afferents and **projects** to the
CVLM. Consumers must **not** conflate the two — the **NTS** is
the **afferent** relay; the **CVLM** is the
**sympathoinhibitory** relay.

The NTS / Area Postrema and CTZ Boundary
----------------------------------------
This is the **visceral afferent / circumventricular** boundary:

*   **NTS** (this module) — the **visceral afferent relay**.

*   **Area postrema** and **chemoreceptor trigger zone**
    (``.../respiratory_center/area_postrema/`` and
    ``.../respiratory_center/chemoreceptor_trigger_zone/``) — the
    **circumventricular chemoreceptive** structures for the
    **vomiting reflex**.

**The AP/CTZ PROJECT TO the NTS** — the NTS is the **downstream
target** of the AP/CTZ emetic and autonomic signals. **They are
DIFFERENT STRUCTURES** — the **AP/CTZ** is the **sensor**; the
**NTS** is the **relay**. Consumers must **not** conflate the
two.

The NTS / Dorsal Motor Nucleus of the Vagus Boundary
----------------------------------------------------
This is the **sensory / motor** boundary:

*   **NTS** (this module) — the **visceral sensory** afferent
    relay.

*   **Dorsal motor nucleus of the vagus (DMV)**
    (``.../cranial_nerve_nuclei/left/dorsal_motor_nucleus_vagus/``
    and
    ``.../cranial_nerve_nuclei/right/dorsal_motor_nucleus_vagus/``)
    — the **visceral motor** (parasympathetic) nucleus.

**They are DIFFERENT STRUCTURES** — the **DMV** is **visceral
motor** (parasympathetic); the **NTS** is **visceral sensory**
(afferent relay). They are **anatomically adjacent** in the
**dorsal medulla** but are **functionally distinct**. Consumers
must **not** conflate the two.

The NTS / Hypoglossal Nucleus and Spinal Trigeminal Nucleus Boundary
--------------------------------------------------------------------
This is the **visceral afferent / somatic** boundary:

*   **NTS** (this module) — the **visceral sensory** afferent
    relay.

*   **Hypoglossal nucleus**
    (``.../cranial_nerve_nuclei/left/hypoglossal_nucleus/`` and
    ``.../cranial_nerve_nuclei/right/hypoglossal_nucleus/``) — the
    **somatic motor** nucleus.

*   **Spinal trigeminal nucleus** — the **facial pain/temperature**
    sensory relay.

**They are DIFFERENT STRUCTURES.** Consumers must **not** conflate
the **NTS** with either.

The NTS / VRG Boundary
----------------------
This is the **visceral afferent / ventral respiratory** boundary:

*   **NTS** (this module) — the **visceral afferent relay**.

*   **VRG** (``.../ventral_respiratory_group/``) — the **ventral
    respiratory** rhythm and pattern generator group.

**They are DIFFERENT STRUCTURES** — the **NTS** is the **visceral
afferent relay**; the **VRG** is a **respiratory rhythm
generator**. They are **functionally coupled** (the NTS
**projects** to the VRG to **modulate** respiratory pattern) but
are **anatomically distinct**. Consumers must **not** conflate
the two.

The NTS / Other Medullary Structures Boundary
---------------------------------------------
This is the **visceral afferent / other-medullary-structures**
boundary:

*   **NTS** (this module) — the **visceral afferent relay**.

*   **Gi, paramedian reticular nucleus, arcuate nucleus,
    parafacial zone, olivary body, medullary pyramid,
    perihypoglossal nuclei, cranial nerve nuclei** — **other
    medullary structures**.

**Each is a DIFFERENT STRUCTURE.** Consumers must **not** conflate
the **NTS** with any of these.

The NTS / Whole Medulla Oblongata Boundary
------------------------------------------
This is the **child / container** boundary:

*   **NTS** (this module) — one **child** of
    ``medulla_oblongata``.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the NTS and other medullary
    structures.

**The NTS is a CHILD of medulla_oblongata, NOT the whole medulla.**
Consumers must **not** conflate the **child** with the **parent
container**.

Function in the Human Brain
---------------------------
The NTS's function is **visceral afferent relay** — **NOT motor
control**, **NOT sympathetic premotor**, and **NOT respiratory
rhythm generation**:

*   **Taste relay:** The **NTS** receives **taste** afferents
    from the **anterior tongue** (via **CN VII** — chorda
    tympani), **posterior tongue** (via **CN IX**), and
    **epiglottis** (via **CN X**) — and it **relays** them to the
    **parabrachial nucleus** and the **thalamus** (VPM) for
    **conscious taste perception**, and to the **hypothalamus**
    and **amygdala** for **affective** and **homeostatic**
    responses to taste.

*   **Baroreceptor relay:** The **NTS** receives
    **baroreceptor** afferents from the **carotid sinus** (via
    **CN IX**) and the **aortic arch** (via **CN X**) — and it
    **initiates the baroreflex** by **projecting** to the
    **CVLM** (which **inhibits the RVLM**) and to the **DMV**
    (for **parasympathetic** cardiac **slowing**). This is the
    **afferent limb** of the **medullary baroreflex arc**.

*   **Chemoreceptor relay:** The **NTS** receives
    **chemoreceptor** afferents from the **carotid body** (via
    **CN IX**) and the **aortic body** (via **CN X**) — and it
    **initiates the chemoreflex** by **projecting** to the
    **VRG** (for **respiratory** **stimulation**) and to the
    **RVLM** (for **sympathetic** **activation**).

*   **Gastrointestinal relay:** The **NTS** receives
    **gastrointestinal** afferents (via **CN X**) —
    **mechanoreceptor**, **chemoreceptor**, and **osmoreceptor**
    signals from the **stomach**, **intestine**, and **liver** —
    and it **projects** to the **DMV** (for
    **gastrointestinal** **parasympathetic** control), the
    **parabrachial nucleus** (for **visceral** **sensation**),
    and the **hypothalamus** (for **food intake** and
    **metabolic** regulation).

*   **Respiratory relay:** The **NTS** receives **pulmonary**
    afferents (via **CN X**) — **pulmonary stretch receptor**
    signals and **irritant receptor** signals — and it
    **projects** to the **VRG** and **DRG** (for **respiratory**
    **pattern modulation**).

*   **Cardiac relay:** The **NTS** receives **cardiac**
    afferents (via **CN X**) — **mechanoreceptor** and
    **chemoreceptor** signals from the **heart** — and it
    **projects** to the **DMV** (for **parasympathetic**
    **cardiac** control) and the **RVLM** (for **sympathetic**
    **cardiac** control).

*   **NOT motor control:** The **NTS** does **not** send motor
    axons to muscles.

*   **NOT sympathetic premotor:** The **sympathetic premotor**
    function is the **RVLM** — **NOT** the NTS.

*   **NOT respiratory rhythm generation:** The **respiratory
    rhythm** is generated by the **pre-Bötzinger complex** (VRG)
    — **NOT** the NTS.

**The unifying theme:** the NTS is the **primary visceral
afferent relay** of the **brainstem** — it **receives** taste,
baroreceptor, chemoreceptor, gastrointestinal, pulmonary, and
cardiac afferents via **CN VII, IX, X** — and it **projects** to
the **RVLM**, **CVLM**, **DMV**, **VRG**, **parabrachial
nucleus**, **hypothalamus**, and **amygdala** to **initiate** the
**baroreflex**, **chemoreflex**, **gastrointestinal**, and
**respiratory** **reflexes** — **NOT** a motor nucleus, **NOT** a
sympathetic premotor center, and **NOT** a respiratory rhythm
generator.

Associated Disorders
--------------------
The NTS is the **substrate** for **well-defined clinical
syndromes** — its clinical relevance is **direct**, via **visceral
afferent** dysfunction:

*   **Baroreflex failure (via NTS dysfunction):** **Damage** to
    the **NTS** — from **stroke**, **demyelination**, **tumor**,
    or **surgical** **injury** — **disrupts** the **afferent
    limb** of the **baroreflex** — causing **baroreflex
    failure**: **labile blood pressure**, **orthostatic
    hypotension**, **hypertensive crises**, and **loss of
    heart-rate variability**. The **NTS** is the **afferent
    limb** — its dysfunction **disrupts** the **entire**
    baroreflex arc.

*   **Dysautonomia / autonomic failure (via NTS dysfunction):**
    **Damage** to the **NTS** can **contribute** to
    **dysautonomia** — **orthostatic hypotension**,
    **gastrointestinal** **dysmotility**, **cardiac**
    **arrhythmias**, and **thermoregulatory** dysfunction. The
    **NTS** is a **key node** in the **central autonomic
    network**.

*   **Neurogenic hypertension (via NTS dysfunction — hypothesized
    in some models):** **Impaired** NTS **baroreceptor** input —
    from **NTS** dysfunction or from **baroreceptor**
    **deafferentation** — can **contribute** to **neurogenic
    hypertension** by **reducing** the **baroreflex buffering**
    of **sympathetic outflow**. The **NTS** is a **contributing
    substrate** — but the **primary** sympathetic premotor
    driver is the **RVLM**.

*   **Brainstem stroke (via NTS involvement):** **Wallenberg
    syndrome (lateral medullary syndrome)** **frequently**
    **involves** the **NTS** — contributing to **autonomic
    instability**, **intractable hiccups**, **nausea**, and
    **cardiovascular** dysfunction.

*   **Taste disorders (via NTS dysfunction):** **Damage** to the
    **rostral NTS** — the **taste relay** — can cause **taste
    loss** (ageusia, hypogeusia) or **dysgeusia**. The **NTS**
    is the **first central** **taste relay**.

*   **Gastrointestinal dysmotility (via NTS dysfunction):**
    **Damage** to the **NTS** can **contribute** to
    **gastroparesis**, **constipation**, or **dysphagia** via
    **impaired** **visceral afferent** and **parasympathetic**
    **reflexes**.

*   **No Named "NTS Syndrome":** The NTS is a **visceral afferent
    relay** — its clinical syndromes are **named for the broader
    clinical entity** (baroreflex failure, dysautonomia, Wallenberg
    syndrome) or the **broader lesion** — **NOT** for the NTS
    itself.

**What is NOT here:** The NTS is **not** the substrate for
**sympathetic premotor** function (RVLM), **sympathoinhibition**
(CVLM), **respiratory rhythm generation** (VRG), **dorsal
respiratory pattern generation** (DRG), **emesis** (area postrema
/ CTZ), **tongue weakness** (hypoglossal nucleus), or
**parasympathetic dysfunction** (dorsal motor nucleus of the
vagus). Its clinical relevance is the **visceral afferent**
functions listed above.

Lateralization Notes
--------------------
The solitary nucleus is a **bilateral container** in this tree with
``left`` and ``right`` structural children. There is **no**
``solitary_nucleus/left/.../`` structural hierarchy beyond the
single leaf level.

*   **Bilateral structural children (ANATOMICAL pairing):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left** or **right** NTS as a **single structure**. The
    **left** and **right** NTS are **anatomically separate
    structures** (unlike the **area postrema**, which is a
    **midline** organ wired as left/right by convention). The
    **left** NTS is in the **left dorsal medulla**; the **right**
    NTS is in the **right dorsal medulla**.

*   **Bilateral symmetry:** The **left** and **right** NTS are
    **structurally symmetric mirror pairs** — same
    cytoarchitecture, same projections (with some crossed
    components), same functions.

*   **Ipsilateral vs. contralateral projections:** Most **NTS**
    projections are **ipsilateral** — the **left NTS** projects
    to the **left RVLM**, **left CVLM**, **left DMV**, **left
    VRG**, and **left parabrachial** — but some are **crossed**
    (via **commissural** pathways) — contributing to
    **bilateral** **integration** of **visceral** signals.
    **The bilateral coordination of the NTS** ensures that
    **visceral reflexes** are **integrated** across the
    **left and right** sides of the brainstem.

*   **NO lateralization warning:** The NTS has **no known
    functional lateralization** in humans — the **left** and
    **right** NTS are **functionally symmetric** at the
    **nucleus level**. Consumers must **not** import a
    **lateralization warning** into the NTS — the **left** and
    **right** sides are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The NTS is
    **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the NTS.

*   **NO Fear-Output Warning:** The NTS is **not** a fear-output
    structure — it is a **visceral afferent relay**. Consumers
    must **not** conflate it with the **central nucleus** or with
    the **amygdala**.

**A consumer that assumes "left NTS = right NTS" will be
structurally correct** — the two sides are **symmetric** and
**functionally equivalent** at the **nucleus level**. The NTS is
a **strict-mirror pair with NO warning** — **no SLEA warning**,
**no fear-output warning**, and **no lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The NTS is a **bilateral
    container** — it does **not** import from ``left/`` or
    ``right/`` at the container level. The ``left`` and ``right``
    leaves are **independent** modules.
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
    other container. The NTS's relationships to the DRG, RVLM,
    CVLM, area postrema, CTZ, dorsal motor nucleus of the vagus,
    hypoglossal nucleus, spinal trigeminal nucleus, VRG, Gi,
    paramedian reticular nucleus, arcuate nucleus, and
    parafacial zone are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children (ANATOMICAL
    pairing).** The structural children are ``left`` and
    ``right``, each a **leaf**. **Anatomically**, the left and
    right NTS are **truly separate bilateral structures** — the
    **left / right split** is **ANATOMICAL**, **NOT** a
    **tree-wiring convention**.
*   **VISCERAL AFFERENT RELAY — the primary visceral sensory
    relay of the brainstem.** The NTS is a **genuine visceral
    afferent relay** — **NOT** a motor nucleus, **NOT** a
    sympathetic premotor center, **NOT** a respiratory rhythm
    generator, and **NOT** a circumventricular organ.
*   **NOT the DRG.** The **DRG** is a **functional respiratory
    subregion** within the **NTS region** — **often considered
    part of the NTS in the literature**, but **wired separately**
    under ``respiratory_center`` in this tree. Consumers must
    **not** expect to find the DRG under ``solitary_nucleus``.
*   **NOT the RVLM or CVLM.** Those are the **efferent limb**
    (RVLM) and **sympathoinhibitory** relay (CVLM) of the
    **medullary baroreflex arc** — **NOT** the **afferent**
    relay (NTS).
*   **NOT the area postrema or CTZ.** Those are **circumventricular
    chemoreceptive** structures that **project to** the NTS.
*   **NOT the dorsal motor nucleus of the vagus.** The **DMV** is
    **visceral motor** (parasympathetic); the **NTS** is
    **visceral sensory** (afferent relay).
*   **NOT the hypoglossal nucleus or spinal trigeminal nucleus.**
    Those are **somatic motor** and **facial somatosensory**
    structures, respectively.
*   **NOT the VRG.** The VRG is a **respiratory rhythm
    generator** — the NTS **projects to** the VRG, but is **NOT**
    the VRG.
*   **NOT the Gi, paramedian reticular nucleus, arcuate nucleus,
    or parafacial zone.** Each is a **different structure**.
*   **NOT the whole medulla oblongata.** The NTS is a **child**
    of ``medulla_oblongata``, not the container itself.
*   **No ``AREA_PATHS`` hop.** The NTS is a **local container** —
    it is not cross-listed under another brainparts path.
*   **No nested cross-listing.** The NTS has no nested
    dual-framing module. It is a **bilateral container** with
    **two leaf children** (anatomical pairing).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **visceral afferent**
    framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata import solitary_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus"
    )

**Do not** expect to find the **DRG** under ``solitary_nucleus``.
The **DRG** is **often considered part of the NTS in the
literature**, but it is **wired separately** under
``respiratory_center`` in this tree. Resolve the DRG via
``respiratory_center.dorsal_respiratory_group``.

**Do not** assume the NTS is the **RVLM** or **CVLM**. Those are
the **efferent limb** and **sympathoinhibitory** relay of the
**medullary baroreflex arc** — **NOT** the **afferent** relay
(NTS).

**Do not** assume the NTS is the **area postrema** or **CTZ**.
Those are **circumventricular chemoreceptive** structures that
**project to** the NTS.

**Do not** assume the NTS is the **dorsal motor nucleus of the
vagus**. The **DMV** is **visceral motor** (parasympathetic);
the **NTS** is **visceral sensory** (afferent relay).

**Do not** assume the NTS is the **hypoglossal nucleus** or the
**spinal trigeminal nucleus**. Those are **somatic motor** and
**facial somatosensory** structures, respectively.

**Do not** assume the NTS is the **VRG**. The VRG is a
**respiratory rhythm generator** — the NTS **projects to** the
VRG, but is **NOT** the VRG.

**Do not** assume the NTS is the **Gi**, the **paramedian
reticular nucleus**, the **arcuate nucleus**, or the
**parafacial zone**. Each is a **different structure**.

**Do not** assume the NTS is the **whole medulla oblongata**.
It is a **child** of ``medulla_oblongata``.

**Do not** infer **midline wiring convention** from the NTS
structure. The **left / right split** is **ANATOMICAL** — the
**left** and **right** NTS are **truly separate bilateral
structures** (unlike the area postrema / CTZ, which are midline
organs wired as left/right by convention).

Iterating the NTS's structural children (recommended consumer
pattern)::

    SOLITARY_NUCLEUS_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # NTS. Anatomically, the left and right NTS are TRULY
    # SEPARATE bilateral structures — the left/right split is
    # ANATOMICAL, NOT a wiring convention.

Reaching the left and right NTS leaves (recommended consumer
pattern)::

    # The left and right NTS leaves are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.left
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus.right
    #
    # Each is a leaf module representing the NTS of that side.
    # Anatomically, they are TRULY SEPARATE bilateral structures.

Reaching the DRG (recommended consumer pattern — NOTE the
DIFFERENT container, OFTEN CONSIDERED PART OF THE NTS in the
literature)::

    # The dorsal respiratory group is a CHILD of respiratory_center
    # — wired SEPARATELY from the NTS in this tree, even though
    # the DRG is often considered part of the NTS in the
    # literature:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.dorsal_respiratory_group
    #
    # The tree separates the NTS (visceral afferent relay) from
    # the DRG (dorsal respiratory pattern generator) as a
    # deliberate wiring choice.

Reaching the RVLM and CVLM (recommended consumer pattern — NOTE
the DIFFERENT containers)::

    # The RVLM and CVLM are the EFFERENT limb and
    # SYMPATHOINHIBITORY relay of the medullary baroreflex arc —
    # SEPARATE containers:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #
    # The NTS is the AFFERENT limb of the baroreflex arc — it
    # PROJECTS to the CVLM (which inhibits the RVLM) and to the
    # RVLM directly. They are DIFFERENT structures.

Reaching the area postrema and CTZ (recommended consumer
pattern — NOTE the DIFFERENT container)::

    # The area postrema and chemoreceptor trigger zone are
    # CIRCUMVENTRICULAR structures that PROJECT TO the NTS —
    # children of respiratory_center:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.area_postrema
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.chemoreceptor_trigger_zone
    #
    # They are DIFFERENT structures from the NTS — the AP/CTZ is
    # the sensor; the NTS is the relay.

Reaching the dorsal motor nucleus of the vagus (recommended
consumer pattern — NOTE the DIFFERENT container)::

    # The dorsal motor nucleus of the vagus is a VISCERAL MOTOR
    # (parasympathetic) nucleus — a separate container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.left.dorsal_motor_nucleus_vagus
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.right.dorsal_motor_nucleus_vagus
    #
    # The NTS is the VISCERAL SENSORY (afferent relay) — they are
    # functionally paired but anatomically distinct.

Reaching the VRG (recommended consumer pattern — NOTE the
DIFFERENT container)::

    # The ventral respiratory group is a RESPIRATORY structure —
    # a separate container:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #
    # The NTS PROJECTS to the VRG (to modulate respiratory pattern)
    # — but the NTS is NOT the VRG.

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
    tractus solitarius; visceral afferent relay; taste, baroreceptor,
    chemoreceptor, and gastrointestinal afferents.)
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