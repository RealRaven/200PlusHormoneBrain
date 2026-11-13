"""
infrastructure.brainparts.hindbrain
===================================

Anatomical Hierarchy
--------------------
::

    brainparts
    ├── forebrain
    ├── midbrain
    └── hindbrain                              <-- THIS MODULE
        ├── metencephalon
        └── myelencephalon

**Primary synonym:** Hindbrain; rhombencephalon; the
rhombencephalic brain vesicle derivative; the caudal brain
vesicle.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
single grey-matter or white-matter structure.** A
**developmental region** — the **rhombencephalon** derivative,
comprising the **metencephalon** (pons + cerebellum) and the
**myelencephalon** (medulla oblongata).
**Part of:** The **brainparts** package — the **caudal** of the
**three primary brain vesicles** (prosencephalon → forebrain;
mesencephalon → midbrain; rhombencephalon → hindbrain).
**Structural parent:** ``.../brainparts/`` → **direct child** of
the brainparts container.
**Structural children:** **Two** — ``metencephalon/`` and
``myelencephalon/``. Each is a **sub-container**. The
**cerebellum**, **pons**, **fourth ventricle**, **medulla
oblongata**, **cranial nerve nuclei (V–XII)**, **reticular
formation**, **respiratory centers**, **cardiovascular centers**,
and the **choroid plexus of the fourth ventricle** are documented
as **prose or as children of the sub-containers**, not directly as
children of the hindbrain.
**Boundary status (NOT the forebrain — the forebrain is
ROSTRAL):** **Boundary case — the hindbrain is NOT the
forebrain.** The **forebrain** (``.../forebrain/``) is the
**rostral** brain vesicle derivative — the **telencephalon**
(cerebral hemispheres, basal ganglia, hippocampus, amygdala,
lateral ventricles) and the **diencephalon** (thalamus,
hypothalamus, epithalamus, subthalamus, third ventricle). The
**hindbrain** (here) is the **caudal** brain vesicle derivative.
**They are DIFFERENT developmental compartments** — the
**forebrain** is **rostral**; the **hindbrain** is **caudal**.
Consumers must **not** conflate the hindbrain with the forebrain.
**Boundary status (NOT the midbrain — the midbrain is BETWEEN
them):** **Boundary case — the hindbrain is NOT the midbrain.**
The **midbrain** (``.../midbrain/``) is the **mesencephalon**
derivative — the **tectum** (superior and inferior colliculi),
the **tegmentum** (substantia nigra, red nucleus, periaqueductal
gray, ventral tegmental area), the **cerebral peduncle**, the
**mesencephalic aqueduct**, and the **oculomotor (III) and
trochlear (IV) cranial nerve nuclei**. The **hindbrain** (here)
is the **caudal** brain vesicle derivative — the
**metencephalon** and **myelencephalon**. **They are DIFFERENT
developmental compartments** — the **midbrain** is **between**
the forebrain and the hindbrain; the **hindbrain** is **caudal**
to the midbrain. Consumers must **not** conflate the hindbrain
with the midbrain.
**Boundary status (NOT the spinal cord — the spinal cord is
CAUDAL to the medulla):** **Boundary case — the hindbrain is NOT
the spinal cord.** The **spinal cord** (``.../spinal_cord/``) is
the **caudal** continuation of the neuraxis — the **gray matter**
(dorsal, lateral, ventral horns) and **white matter**
(corticospinal tract, dorsal columns, spinothalamic tract). The
**hindbrain** (here) is **rostral** to the spinal cord — the
**medulla oblongata** is continuous with the spinal cord at the
**foramen magnum / cervicomedullary junction**. **The hindbrain
ends where the spinal cord begins** — the **medulla oblongata**
is the **caudal-most hindbrain structure**, and the **spinal
cord** is **caudal** to it. Consumers must **not** conflate the
hindbrain with the spinal cord.
**Boundary status (NOT the metencephalon alone — the hindbrain
CONTAINS the metencephalon):** **Boundary case — the hindbrain is
NOT the metencephalon.** The **metencephalon**
(``.../hindbrain/metencephalon/``) is the **rostral** hindbrain
sub-container — the **pons**, the **cerebellum**, and the
**fourth ventricle**. The **hindbrain** (here) **contains** the
metencephalon **and** the myelencephalon. Consumers must **not**
conflate the hindbrain with the metencephalon — the
**metencephalon** is a **sub-container**; the **hindbrain** is
the **container**.
**Boundary status (NOT the myelencephalon alone — the hindbrain
CONTAINS the myelencephalon):** **Boundary case — the hindbrain
is NOT the myelencephalon.** The **myelencephalon**
(``.../hindbrain/myelencephalon/``) is the **caudal** hindbrain
sub-container — the **medulla oblongata**. The **hindbrain**
(here) **contains** the myelencephalon **and** the
metencephalon. Consumers must **not** conflate the hindbrain with
the myelencephalon — the **myelencephalon** is a
**sub-container**; the **hindbrain** is the **container**.
**Boundary status (NOT the fourth ventricle — the fourth ventricle
is INSIDE the hindbrain, not the hindbrain itself):** **Boundary
case — the hindbrain is NOT the fourth ventricle.** The **fourth
ventricle**
(``.../hindbrain/metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **hindbrain** (here) is the **neural tissue
region** that **surrounds and contains** the fourth ventricle.
**The fourth ventricle is a CSF cavity INSIDE the hindbrain; the
hindbrain is the neural tissue region around it.** Consumers must
**not** conflate the hindbrain with the fourth ventricle.
**Boundary status (NOT the cerebellum alone — the cerebellum is a
CHILD of the metencephalon):** **Boundary case — the hindbrain
is NOT the cerebellum.** The **cerebellum**
(``.../hindbrain/metencephalon/cerebellum/``) is the
**metencephalic** motor-coordination structure — the
**hemispheres**, the **vermis**, the **deep nuclei** (dentate,
fastigial, interposed), and the **cerebellar cortex**. The
**hindbrain** (here) **contains** the cerebellum **and** the
pons, **and** the medulla oblongata. Consumers must **not**
conflate the hindbrain with the cerebellum — the **cerebellum**
is a **sub-structure**; the **hindbrain** is the **region**.
**Boundary status (NOT the pons alone — the pons is a CHILD of
the metencephalon):** **Boundary case — the hindbrain is NOT the
pons.** The **pons** (``.../hindbrain/metencephalon/pons/``) is
the **metencephalic** brainstem structure — the **basis pontis**
(pontine nuclei, corticospinal and corticobulbar tracts,
transverse pontine fibers), the **tegmentum**, the **cerebellar
peduncles**, and the **cranial nerve nuclei (V, VI, VII,
VIII)**. The **hindbrain** (here) **contains** the pons **and**
the cerebellum, **and** the medulla oblongata. Consumers must
**not** conflate the hindbrain with the pons — the **pons** is a
**sub-structure**; the **hindbrain** is the **region**.
**Boundary status (NOT the medulla oblongata alone — the medulla
is a CHILD of the myelencephalon):** **Boundary case — the
hindbrain is NOT the medulla oblongata.** The **medulla
oblongata** (``.../hindbrain/myelencephalon/medulla_oblongata/``)
is the **myelencephalic** brainstem structure — the **pyramids**,
the **olives**, the **cranial nerve nuclei (IX, X, XI, XII)**,
the **respiratory centers** (dorsal and ventral respiratory
groups), and the **cardiovascular centers** (nucleus tractus
solitarius, rostral ventrolateral medulla). The **hindbrain**
(here) **contains** the medulla **and** the metencephalon.
Consumers must **not** conflate the hindbrain with the medulla
oblongata — the **medulla** is a **sub-structure**; the
**hindbrain** is the **region**.
**Boundary status (NOT a single functional system — MULTIPLE
sub-regions with DIFFERENT functions):** **Boundary case — the
hindbrain is a HETEROGENEOUS developmental region with MULTIPLE
sub-regions and MULTIPLE functions, not a single uniform
system.** The hindbrain includes:
*   **Metencephalon** — the **pons** (pontine nuclei,
    corticospinal/corticobulbar relay, cranial nerve nuclei V–VIII,
    pontine respiratory group, locus coeruleus, parabrachial
    complex, pedunculopontine nucleus, laterodorsal tegmental
    nucleus), the **cerebellum** (motor coordination, balance,
    motor learning, cerebellar cognitive-affective syndrome), and
    the **fourth ventricle** (CSF cavity).
*   **Myelencephalon** — the **medulla oblongata** (autonomic
    control — respiratory, cardiovascular, vasomotor; cranial
    nerve nuclei IX–XII; ascending/descending tracts; inferior
    olivary complex; area postrema; nucleus tractus solitarius;
    rostral ventrolateral medulla).
**Each sub-region is functionally distinct** — the tree wires the
**metencephalon** and **myelencephalon** as **sub-containers**,
and the functional sub-regions are documented as **prose or as
children of those sub-containers**. Consumers must **not** treat
the hindbrain as a single uniform region — it is a **distributed
developmental region** with **heterogeneous sub-structures**.
**Boundary status (NOT the rhombencephalon — the rhombencephalon
is the EMBRYONIC vesicle; the hindbrain is its ADULT
derivative):** **Boundary case — the hindbrain is the ADULT
derivative of the rhombencephalon, not the embryonic vesicle
itself.** The **rhombencephalon** is the **embryonic** brain
vesicle (the **caudal** of the three primary vesicles); the
**hindbrain** (here) is its **adult derivative** — the
**metencephalon** and **myelencephalon**. The terms are often used
interchangeably, but the **tree wires the adult structure**. The
**rhombencephalon** is documented as **prose** (the developmental
origin); the **hindbrain** is the **adult region**.
**Boundary status (SLEA-FREE — the hindbrain is NOT an
extended-amygdala component):** **Boundary case — the hindbrain
is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to
the **BNST**, **ventral pallidum**, and **nucleus accumbens**
(wired elsewhere). The **hindbrain** is a **developmental
region** — it is **NOT** an extended-amygdala component, and it
carries **NO SLEA warning**. Consumers must **not** import the
SLEA warning into the hindbrain — it is **SLEA-free**.
**Boundary status (NOT a neural processor in the classical
sense — the hindbrain is a REGION, not a single processor):**
**Boundary case — the hindbrain is a REGION, not a single
neural processor.** It **contains** neural processors (the
cerebellum, the pontine nuclei, the medullary respiratory and
cardiovascular centers, the reticular formation) — but it is
**not itself a processor**. The **processing** happens in the
**sub-structures** (cerebellum, pons, medulla). Consumers must
**not** treat the hindbrain as a **single neural processor** —
it is a **developmental region** with **heterogeneous
sub-structures**, each with its own function.

Overview
--------
The hindbrain is the **caudal** of the **three primary brain
vesicles** — the **adult derivative of the rhombencephalon** —
comprising the **metencephalon** (pons + cerebellum + fourth
ventricle) and the **myelencephalon** (medulla oblongata). It is a
**container module** with two **structural sub-containers**
(``metencephalon/`` and ``myelencephalon/``).

**The hindbrain is the CAUDAL brain region, distinct from the
forebrain and midbrain.** The **forebrain** (``.../forebrain/``)
is **rostral**; the **midbrain** (``.../midbrain/``) is
**between**; the **hindbrain** (here) is **caudal**. They are
**different developmental compartments** — the **forebrain** is
the **prosencephalon** derivative; the **midbrain** is the
**mesencephalon** derivative; the **hindbrain** is the
**rhombencephalon** derivative.

**The hindbrain is CONTINUOUS with the spinal cord caudally.**
The **medulla oblongata** (the caudal-most hindbrain structure)
is continuous with the **spinal cord** at the **foramen magnum /
cervicomedullary junction**. The **hindbrain ends where the spinal
cord begins** — the **medulla** is the **caudal-most hindbrain
structure**, and the **spinal cord** is **caudal** to it.

**The hindbrain is a HETEROGENEOUS developmental region, not a
single structure.** It includes the **cerebellum** (motor
coordination, balance, motor learning), the **pons** (pontine
nuclei, cranial nerve nuclei V–VIII, pontine respiratory group,
locus coeruleus, parabrachial complex), the **fourth ventricle**
(CSF cavity), and the **medulla oblongata** (autonomic control,
cranial nerve nuclei IX–XII, ascending/descending tracts,
inferior olivary complex, area postrema, nucleus tractus
solitarius). Each sub-region is functionally distinct.

**The hindbrain is a REGION, not a single neural processor.** The
**processing** happens in the **sub-structures** (cerebellum,
pons, medulla). The **hindbrain** is the **developmental region**
that **contains** those sub-structures.

Hindbrain Composition (prose, not structural children)
------------------------------------------------------
The hindbrain is a **developmental region** with **two
sub-containers** — documented as **structural children**
(``metencephalon/`` and ``myelencephalon/``) — and **many
prose-defined sub-structures** documented as **prose** within
those sub-containers:

*   **Metencephalon** (``.../hindbrain/metencephalon/``) — the
    **rostral** hindbrain sub-container:
    *   **Cerebellum** — motor coordination, balance, motor
        learning, cerebellar cognitive-affective syndrome.
    *   **Pons** — pontine nuclei, corticospinal/corticobulbar
        relay, cranial nerve nuclei V–VIII, pontine respiratory
        group, locus coeruleus, parabrachial complex,
        pedunculopontine nucleus, laterodorsal tegmental nucleus.
    *   **Fourth ventricle** — the metencephalic CSF cavity.

*   **Myelencephalon** (``.../hindbrain/myelencephalon/``) — the
    **caudal** hindbrain sub-container:
    *   **Medulla oblongata** — autonomic control (respiratory,
        cardiovascular, vasomotor), cranial nerve nuclei IX–XII,
        ascending/descending tracts, inferior olivary complex,
        area postrema, nucleus tractus solitarius, rostral
        ventrolateral medulla.

**These sub-regions are prose (or children of the sub-containers),
not direct structural children of the hindbrain.** The tree wires
the **hindbrain** as a **container** with **two sub-containers**
(``metencephalon/`` and ``myelencephalon/``) — the
**cerebellum**, **pons**, **fourth ventricle**, and **medulla
oblongata** are documented as **children of those
sub-containers**, and the finer sub-regions (cranial nerve
nuclei, respiratory centers, etc.) are documented as **prose**.
Consumers that need **sub-region-level** resolution should
consult the **sub-container modules** and the references, not the
hindbrain container.

The Hindbrain / Forebrain Boundary
----------------------------------
This is the **caudal-vs-rostral** boundary:

*   **Hindbrain** (this module) — the **rhombencephalon**
    derivative (metencephalon + myelencephalon).

*   **Forebrain** (``.../forebrain/``) — the **prosencephalon**
    derivative (telencephalon + diencephalon).

**They are DIFFERENT developmental compartments** — the
**forebrain** is **rostral**; the **hindbrain** is **caudal**.
Consumers must **not** conflate the hindbrain with the forebrain.

The Hindbrain / Midbrain Boundary
---------------------------------
This is the **caudal-vs-between** boundary:

*   **Hindbrain** (this module) — the **rhombencephalon**
    derivative (metencephalon + myelencephalon).

*   **Midbrain** (``.../midbrain/``) — the **mesencephalon**
    derivative (tectum + tegmentum + cerebral peduncle).

**They are DIFFERENT developmental compartments** — the
**midbrain** is **between** the forebrain and the hindbrain;
the **hindbrain** is **caudal** to the midbrain. Consumers must
**not** conflate the hindbrain with the midbrain.

The Hindbrain / Spinal Cord Boundary
------------------------------------
This is the **brain-vs-spinal-cord** boundary:

*   **Hindbrain** (this module) — the **rhombencephalon**
    derivative, ending at the **medulla oblongata**.

*   **Spinal cord** (``.../spinal_cord/``) — the **caudal**
    continuation of the neuraxis, beginning at the
    **cervicomedullary junction**.

**The hindbrain ends where the spinal cord begins** — the
**medulla oblongata** is the **caudal-most hindbrain structure**,
and the **spinal cord** is **caudal** to it. Consumers must
**not** conflate the hindbrain with the spinal cord.

The Hindbrain / Metencephalon Boundary
--------------------------------------
This is the **container-vs-sub-container** boundary:

*   **Hindbrain** (this module) — the **container**.

*   **Metencephalon** (``.../hindbrain/metencephalon/``) — the
    **rostral** sub-container (pons + cerebellum + fourth
    ventricle).

**The metencephalon is a sub-container of the hindbrain.** Consumers
must **not** conflate the hindbrain with the metencephalon — the
**metencephalon** is a **sub-container**; the **hindbrain** is
the **container**.

The Hindbrain / Myelencephalon Boundary
---------------------------------------
This is the **container-vs-sub-container** boundary:

*   **Hindbrain** (this module) — the **container**.

*   **Myelencephalon** (``.../hindbrain/myelencephalon/``) — the
    **caudal** sub-container (medulla oblongata).

**The myelencephalon is a sub-container of the hindbrain.**
Consumers must **not** conflate the hindbrain with the
myelencephalon — the **myelencephalon** is a **sub-container**;
the **hindbrain** is the **container**.

The Hindbrain / Fourth Ventricle Boundary
-----------------------------------------
This is the **region-vs-CSF-cavity** boundary:

*   **Hindbrain** (this module) — the **neural tissue region**.

*   **Fourth ventricle**
    (``.../hindbrain/metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity** between the pons/medulla and
    the cerebellum.

**The fourth ventricle is a CSF cavity INSIDE the hindbrain; the
hindbrain is the neural tissue region around it.** Consumers must
**not** conflate the hindbrain with the fourth ventricle.

The Hindbrain / Cerebellum Boundary
-----------------------------------
This is the **region-vs-sub-structure** boundary:

*   **Hindbrain** (this module) — the **region**.

*   **Cerebellum**
    (``.../hindbrain/metencephalon/cerebellum/``) — the
    **metencephalic** motor-coordination structure.

**The cerebellum is a sub-structure of the metencephalon (and thus
of the hindbrain).** Consumers must **not** conflate the hindbrain
with the cerebellum — the **cerebellum** is a **sub-structure**;
the **hindbrain** is the **region**.

The Hindbrain / Pons Boundary
-----------------------------
This is the **region-vs-sub-structure** boundary:

*   **Hindbrain** (this module) — the **region**.

*   **Pons** (``.../hindbrain/metencephalon/pons/``) — the
    **metencephalic** brainstem structure.

**The pons is a sub-structure of the metencephalon (and thus of
the hindbrain).** Consumers must **not** conflate the hindbrain
with the pons — the **pons** is a **sub-structure**; the
**hindbrain** is the **region**.

The Hindbrain / Medulla Oblongata Boundary
------------------------------------------
This is the **region-vs-sub-structure** boundary:

*   **Hindbrain** (this module) — the **region**.

*   **Medulla oblongata**
    (``.../hindbrain/myelencephalon/medulla_oblongata/``) — the
    **myelencephalic** brainstem structure.

**The medulla oblongata is a sub-structure of the myelencephalon
(and thus of the hindbrain).** Consumers must **not** conflate
the hindbrain with the medulla oblongata — the **medulla** is a
**sub-structure**; the **hindbrain** is the **region**.

The Hindbrain / Rhombencephalon Boundary
----------------------------------------
This is the **adult-vs-embryonic** boundary:

*   **Hindbrain** (this module) — the **adult derivative** of the
    rhombencephalon.

*   **Rhombencephalon** — the **embryonic** brain vesicle (prose).

**The hindbrain is the ADULT derivative; the rhombencephalon is
the EMBRYONIC vesicle.** The terms are often used
interchangeably, but the **tree wires the adult structure**.
Consumers must **not** conflate the hindbrain with the
rhombencephalon — the **rhombencephalon** is the **developmental
origin**; the **hindbrain** is the **adult region**.

The Hindbrain / SLEA Boundary
-----------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Hindbrain** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The hindbrain is NOT part of the SLEA continuum.** It is a
**developmental region**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the hindbrain.

Function in the Human Brain
---------------------------
The hindbrain's functions are **heterogeneous** — documented at
the **sub-structure** level, not at the region level:

*   **Motor Coordination and Balance (Cerebellum):** The
    **cerebellum** — the **metencephalic** structure — coordinates
    **voluntary movement**, **balance**, **posture**, and **motor
    learning**. It is the **neural substrate** of **cerebellar
    motor coordination** and **cerebellar cognitive-affective
    syndrome**.

*   **Corticospinal / Corticobulbar Relay (Pons):** The **basis
    pontis** — the **ventral pons** — contains the **pontine
    nuclei** and the **transverse pontine fibers** that **relay**
    the **corticospinal** and **corticobulbar** tracts from the
    cortex to the cerebellum and the medulla. The **pons** is a
    **major relay station** in the motor pathway.

*   **Cranial Nerve Nuclei (Pons and Medulla):** The **pons**
    contains the **cranial nerve nuclei V (trigeminal), VI
    (abducens), VII (facial), and VIII (vestibulocochlear)**; the
    **medulla oblongata** contains the **cranial nerve nuclei IX
    (glossopharyngeal), X (vagus), XI (accessory), and XII
    (hypoglossal)**. These nuclei are the **brainstem control
    centers** for **facial sensation**, **eye movement**,
    **facial expression**, **hearing**, **balance**, **taste**,
    **swallowing**, **vocalization**, **head and shoulder
    movement**, and **tongue movement**.

*   **Respiratory Control (Pons and Medulla):** The **pontine
    respiratory group** (in the pons) and the **dorsal and
    ventral respiratory groups** (in the medulla) are the
    **brainstem respiratory centers** — they **generate and
    modulate** the **respiratory rhythm**. The **pre-Bötzinger
    complex** (in the medulla) is the **primary respiratory
    rhythm generator**.

*   **Cardiovascular Control (Medulla):** The **nucleus tractus
    solitarius** (NTS) and the **rostral ventrolateral medulla**
    (RVLM) are the **brainstem cardiovascular centers** — they
    **regulate** **blood pressure**, **heart rate**, and
    **vasomotor tone** via the **baroreceptor reflex** and the
    **chemoreceptor reflex**.

*   **Autonomic Control (Medulla):** The **dorsal motor nucleus
    of the vagus** and the **nucleus ambiguus** are the
    **parasympathetic** brainstem nuclei — they **regulate**
    **gastrointestinal motility**, **secretions**, and **cardiac
    function** via the **vagus nerve**.

*   **Arousal and Sleep-Wake (Pons):** The **locus coeruleus**
    (noradrenergic), the **pedunculopontine nucleus** and
    **laterodorsal tegmental nucleus** (cholinergic), and the
    **parabrachial complex** (glutamatergic) are **brainstem
    arousal and sleep-wake centers** — they **modulate**
    **wakefulness**, **REM sleep**, and **arousal**.

*   **Reticular Formation (Pons and Medulla):** The **reticular
    formation** spans the **pons** and the **medulla** — it is
    the **brainstem arousal system**, the **descending pain
    modulation system**, and the **autonomic reflex integration
    system**.

*   **CSF Production and Circulation (Fourth Ventricle):** The
    **choroid plexus of the fourth ventricle** (in the
    metencephalon) **produces CSF**; the fourth ventricle is a
    **CSF compartment** in the **CSF flow path** (third ventricle
    → mesencephalic aqueduct → fourth ventricle → foramina of
    Luschka and Magendie → subarachnoid space).

*   **NOT a single neural processor.** The hindbrain is a
    **developmental region** — the **processing** happens in the
    **sub-structures** (cerebellum, pons, medulla). Consumers must
    **not** treat the hindbrain as a **single processor** — it is
    a **region** with **heterogeneous sub-structures**.

**The unifying theme:** the hindbrain is the **caudal brain
region** — the **rhombencephalon derivative** — that **contains**
the **cerebellum** (motor coordination), the **pons**
(corticospinal/corticobulbar relay, cranial nerve nuclei V–VIII,
respiratory group, arousal centers), the **fourth ventricle**
(CSF cavity), and the **medulla oblongata** (autonomic control,
cranial nerve nuclei IX–XII, respiratory and cardiovascular
centers). It is a **heterogeneous developmental region**, **NOT a
single neural processor**, and **NOT the forebrain, midbrain, or
spinal cord**.

Associated Disorders
--------------------
The hindbrain has **no single named clinical syndrome** — its
clinical associations are **heterogeneous**, via the
**sub-structures** it contains:

*   **Cerebellar Disorders (via the Cerebellum):** **Cerebellar
    ataxia** (gait ataxia, limb ataxia, dysarthria,
    nystagmus), **cerebellar cognitive-affective syndrome**
    (executive dysfunction, visuospatial deficits, affective
    dysregulation), **spinocerebellar ataxias** (SCAs),
    **cerebellar tumors** (medulloblastoma, pilocytic
    astrocytoma), and **cerebellar stroke** (PICA, AICA, SCA
    infarcts). The **cerebellum** is the **substrate** — the
    hindbrain is the **region**.

*   **Pontine Disorders (via the Pons):** **Pontine stroke**
    (locked-in syndrome from ventral pontine infarction,
    paramedian pontine syndromes), **central pontine myelinolysis**
    (osmotic demyelination syndrome), **pontine glioma** (diffuse
    intrinsic pontine glioma — DIPG), and **pontine hemorrhage**.
    The **pons** is the **substrate**.

*   **Medullary Disorders (via the Medulla Oblongata):**
    **Wallenberg syndrome** (lateral medullary syndrome — PICA
    infarct), **medial medullary syndrome** (Dejerine syndrome —
    anterior spinal artery infarct), **medullary hemorrhage**,
    **medullary glioma**, and **bulbar palsy** (cranial nerve
    IX–XII dysfunction). The **medulla oblongata** is the
    **substrate**.

*   **Brainstem Glioma (via the Hindbrain):** **Diffuse midline
    glioma** (formerly DIPG) — a **pediatric brainstem tumor**
    arising in the **pons** (and sometimes the medulla or
    midbrain). The **hindbrain** is the **region**; the **pons**
    is the **primary substrate**.

*   **Brainstem Stroke (via the Hindbrain):** **Brainstem
    infarcts** (pontine, medullary, midbrain) — **ischemic** or
    **hemorrhagic** — causing **cranial nerve deficits**,
    **long tract signs**, **autonomic dysfunction**, and
    **disorders of consciousness**. The **hindbrain** is the
    **region**; the **pons** and **medulla** are the **substrates**.

*   **Central Sleep Apnea (via the Medulla):** **Dysfunction of
    the medullary respiratory centers** (pre-Bötzinger complex,
    dorsal and ventral respiratory groups) — **central sleep
    apnea**, **Ondine's curse** (congenital central
    hypoventilation syndrome), and **sleep-disordered
    breathing** in **brainstem lesions**. The **medulla** is the
    **substrate**.

*   **Neurogenic Hypertension (via the Medulla):** **Dysfunction
    of the rostral ventrolateral medulla (RVLM)** and the
    **nucleus tractus solitarius (NTS)** — **neurogenic
    hypertension**, **baroreflex failure**, and **autonomic
    dysreflexia**. The **medulla** is the **substrate**.

*   **Area Postrema Syndrome (via the Medulla):** **Vomiting**
    and **nausea** — the **area postrema** (the **chemoreceptor
    trigger zone**) is the **substrate**; **neuromyelitis
    optica spectrum disorder (NMOSD)** can present with
    **intractable hiccups and vomiting** via area postrema
    involvement.

*   **Locus Coeruleus Dysfunction (via the Pons):** **Arousal**,
    **attention**, and **stress-response** dysfunction —
    the **locus coeruleus** (the **major noradrenergic
    nucleus**) is implicated in **PTSD**, **depression**,
    **anxiety**, and **Alzheimer's disease** (early locus
    coeruleus tau pathology). The **pons** is the **substrate**.

*   **No Named "Hindbrain Syndrome":** The hindbrain is a
    **developmental region**, not a **single structure** — it has
    **no named clinical syndrome**. Its clinical relevance is
    **heterogeneous**, via the **sub-structures** it contains.

**What is NOT here:** The hindbrain is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala), **fear conditioning**
(central nucleus + basolateral nuclei), **Urbach-Wiethe disease**
(amygdala), or **Parkinson's disease** (substantia nigra, in the
midbrain). Its clinical relevance is **heterogeneous**, via the
**cerebellum**, **pons**, and **medulla oblongata**. **No named
hindbrain syndrome exists.**

Lateralization Notes
--------------------
This is the **hindbrain** container module. The hindbrain is a
**midline-spanning developmental region** with **bilateral
sub-structures** — and it carries **NO warning**:

*   **Bilateral Sub-Structures:** The **cerebellum** has **left
    and right hemispheres**; the **pons** and **medulla** have
    **bilateral cranial nerve nuclei** and **bilateral
    ascending/descending tracts**. The hindbrain is **not a
    paired structure** in the way the **lateral ventricles** or
    the **amygdala** are — it is a **midline region** with
    **bilateral sub-structures**.

*   **Partial Lateralization (Contested):** Some **cerebellar
    functions** are **partially lateralized** (e.g., **language**
    is more **right cerebellar**; **visuospatial** function is
    more **left cerebellar**) — this is **partial**,
    **contested**, and documented in the **cerebellum module**
    (not at the hindbrain level).

*   **NO Extended-Amygdala Warning (SLEA-free):** The hindbrain
    is **NOT** an extended-amygdala component. It carries **no
    SLEA warning**. Consumers must **not** import the SLEA
    warning into the hindbrain.

*   **NO Amygdala-Lateralization Warning:** The hindbrain is
    **NOT** the fear-output or the fear-learning structure. It is
    a **developmental region** — consumers must **not** conflate
    it with the **amygdala** or the **fear circuit**.

**A consumer that assumes "hindbrain = left + right" will be
structurally correct for the bilateral sub-structures** — the
hindbrain is a **midline region** with **bilateral
sub-structures**. The hindbrain carries **NO warning** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-region imports.** The **container** does **not**
    import from ``.../forebrain/``, ``.../midbrain/``,
    ``.../spinal_cord/``, ``.../metencephalon/``, or
    ``.../myelencephalon/`` — it is a **namespace container**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../forebrain/telencephalon/``,
    ``.../forebrain/diencephalon/``, ``.../midbrain/``,
    ``.../spinal_cord/``, or any other container. The hindbrain's
    relationships to the forebrain, midbrain, spinal cord,
    metencephalon, myelencephalon, fourth ventricle, cerebellum,
    pons, medulla oblongata, and rhombencephalon are documented
    as **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — two structural children.** The
    ``metencephalon/`` and ``myelencephalon/`` are
    **sub-containers**. The **cerebellum**, **pons**, **fourth
    ventricle**, and **medulla oblongata** are **children of
    those sub-containers**; the finer sub-regions (cranial nerve
    nuclei, respiratory centers, etc.) are **prose** within
    those sub-containers. Consumers must not assume any exist as
    direct children of the hindbrain; resolve sub-region-level
    detail through the sub-containers and the references.
*   **REGION — NOT a single structure.** The hindbrain is the
    **rhombencephalon derivative** — a **heterogeneous
    developmental region** containing the **cerebellum**,
    **pons**, **fourth ventricle**, and **medulla oblongata**.
    Consumers must **not** conflate the hindbrain with any single
    sub-structure.
*   **NOT the forebrain — the forebrain is ROSTRAL.** The
    **forebrain** is the **prosencephalon** derivative; the
    **hindbrain** is the **rhombencephalon** derivative.
*   **NOT the midbrain — the midbrain is BETWEEN them.** The
    **midbrain** is the **mesencephalon** derivative; the
    **hindbrain** is the **rhombencephalon** derivative.
*   **NOT the spinal cord — the spinal cord is CAUDAL.** The
    **medulla oblongata** is the **caudal-most hindbrain
    structure**; the **spinal cord** begins at the
    **cervicomedullary junction**.
*   **NOT the fourth ventricle — the fourth ventricle is INSIDE
    the hindbrain.** The **hindbrain** is the **region**; the
    **fourth ventricle** is the **CSF cavity** within it.
*   **NOT the cerebellum, pons, or medulla oblongata alone —
    those are SUB-STRUCTURES.** The **hindbrain** is the
    **region**; the **sub-structures** are its **contents**.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    hindbrain is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT a single neural processor — the hindbrain is a REGION.**
    The **processing** happens in the **sub-structures**
    (cerebellum, pons, medulla). Consumers must **not** treat the
    hindbrain as a **single processor**.
*   **No ``AREA_PATHS`` hop.** The hindbrain is a local container
    under ``brainparts/``, not a cross-listed container.
*   **No nested cross-listing.** The hindbrain has no nested
    dual-framing module. It is a single container with two
    sub-containers.
*   **No lateralization warning.** The hindbrain carries **no
    warning** — **no SLEA warning**, **no amygdala-lateralization
    warning**, and **no rhinencephalon-exclusion flag**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain import (
        metencephalon, myelencephalon,
    )

Or by fully-qualified path string::

    path = (
        "hindbrain"
    )
    metencephalon_path = (
        "hindbrain.metencephalon"
    )
    myelencephalon_path = (
        "hindbrain.myelencephalon"
    )

**Do not** assume the hindbrain is the **forebrain**. The
**forebrain** is **rostral**; the **hindbrain** is **caudal**.

**Do not** assume the hindbrain is the **midbrain**. The
**midbrain** is **between** the forebrain and the hindbrain.

**Do not** assume the hindbrain is the **spinal cord**. The
**medulla oblongata** is the **caudal-most hindbrain structure**;
the **spinal cord** is **caudal** to it.

**Do not** assume the hindbrain is the **fourth ventricle**,
**cerebellum**, **pons**, or **medulla oblongata alone**. The
**hindbrain** is the **region**; the **sub-structures** are its
**contents**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the hindbrain. **The
hindbrain is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

Iterating the hindbrain's children (recommended consumer
pattern)::

    HINDBRAIN_CHILDREN = ("metencephalon", "myelencephalon")
    # The metencephalon and myelencephalon are sub-containers.
    # The cerebellum, pons, fourth ventricle, and medulla
    # oblongata are children of those sub-containers.

Reaching the forebrain (recommended consumer pattern — NOTE the
caudal-vs-rostral boundary)::

    # The forebrain is the ROSTRAL brain vesicle derivative:
    #
    #   forebrain
    #
    # The hindbrain is the CAUDAL brain vesicle derivative.

Reaching the midbrain (recommended consumer pattern — NOTE the
caudal-vs-between boundary)::

    # The midbrain is the MESENCEPHALON derivative BETWEEN the
    # forebrain and the hindbrain:
    #
    #   midbrain
    #
    # The hindbrain is CAUDAL to the midbrain.

Reaching the spinal cord (recommended consumer pattern — NOTE the
brain-vs-spinal-cord boundary)::

    # The spinal cord is CAUDAL to the medulla oblongata:
    #
    #   spinal_cord
    #
    # The medulla oblongata is the CAUDAL-MOST hindbrain
    # structure; the spinal cord begins at the cervicomedullary
    # junction.

Reaching the metencephalon (recommended consumer pattern — the
rostral sub-container)::

    # The metencephalon is the ROSTRAL hindbrain sub-container:
    #
    #   hindbrain.metencephalon
    #
    # It contains the cerebellum, the pons, and the fourth
    # ventricle.

Reaching the myelencephalon (recommended consumer pattern — the
caudal sub-container)::

    # The myelencephalon is the CAUDAL hindbrain sub-container:
    #
    #   hindbrain.myelencephalon
    #
    # It contains the medulla oblongata.

Reaching the fourth ventricle (recommended consumer pattern — NOTE
the region-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The fourth ventricle is INSIDE the hindbrain; the hindbrain
    # is the neural tissue region around it.

Reaching the cerebellum (recommended consumer pattern — NOTE the
region-vs-sub-structure boundary)::

    # The cerebellum is the METENCEPHALIC motor-coordination
    # structure:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cerebellum is a SUB-STRUCTURE of the metencephalon.

Reaching the pons (recommended consumer pattern — NOTE the
region-vs-sub-structure boundary)::

    # The pons is the METENCEPHALIC brainstem structure:
    #
    #   hindbrain.metencephalon.pons
    #
    # The pons is a SUB-STRUCTURE of the metencephalon.

Reaching the medulla oblongata (recommended consumer pattern —
NOTE the region-vs-sub-structure boundary)::

    # The medulla oblongata is the MYELENCEPHALIC brainstem
    # structure:
    #
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The medulla oblongata is a SUB-STRUCTURE of the
    # myelencephalon.

Sub-region detail (not wired at the hindbrain level — consult the
sub-containers and references)::

    # The hindbrain's finer sub-regions are prose within the
    # sub-containers:
    #   metencephalon -> cerebellum, pons, fourth ventricle
    #   myelencephalon -> medulla oblongata
    #     (cranial nerve nuclei IX-XII, respiratory centers,
    #      cardiovascular centers, inferior olivary complex,
    #      area postrema, nucleus tractus solitarius)
    #
    # Do not attempt to resolve these as sub-paths of the
    # hindbrain.

Bilateral iteration (recommended consumer pattern — for bilateral
sub-structures)::

    for side in ("left", "right"):
        # e.g., cerebellar hemispheres, cranial nerve nuclei
        side_path = (
            f"hindbrain.metencephalon.cerebellum.{side}"
        )
        # resolve side_path through the memory/recall layer

References
----------
*   **Canonical hindbrain anatomy:** Standring, S. (ed.) (2020).
    *Gray's Anatomy: The Anatomical Basis of Clinical Practice*,
    42nd ed. (Hindbrain — rhombencephalon, metencephalon,
    myelencephalon, pons, cerebellum, medulla oblongata.)
*   **Brainstem overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Hindbrain — pons, cerebellum, medulla; cranial nerve
    nuclei; reticular formation.)
*   **Developmental origin (rhombencephalon):** Puelles, L.,
    Rubenstein, J.L.R. (2015). "A new scenario of hypothalamic
    organization: implications of a new model of the
    prosomeric brain." *Journal of Comparative Neurology*
    523:1077–1108. (Rhombencephalon — the embryonic hindbrain
    vesicle; adult derivatives metencephalon and
    myelencephalon.)
*   **Cerebellar function and dysfunction:** Manto, M., et al.
    (2012). "Consensus paper: roles of the cerebellum in motor
    control — the diversity of cerebellar involvement in
    movement." *The Cerebellum* 11:457–487. (Cerebellum — motor
    coordination, balance, motor learning.)
*   **Cerebellar cognitive-affective syndrome:** Schmahmann,
    J.D., Sherman, J.C. (1998). "The cerebellar cognitive
    affective syndrome." *Brain* 121:561–579. (Cerebellar
    cognitive-affective syndrome — executive dysfunction,
    visuospatial deficits, affective dysregulation.)
*   **Pontine nuclei and corticospinal relay:** Mihailoff, G.A.,
    et al. (1985). "The basilar pontine gray of the opossum:
    a correlated light and electron microscopic analysis."
    *Journal of Comparative Neurology* 233:417–437. (Pontine
    nuclei and transverse pontine fibers — corticospinal and
    corticobulbar relay.)
*   **Medullary autonomic control (RVLM, NTS):** Guyenet, P.G.
    (2006). "The sympathetic control of blood pressure."
    *Nature Reviews Neuroscience* 7:335–346. (Rostral
    ventrolateral medulla and nucleus tractus solitarius —
    cardiovascular control.)
*   **Respiratory rhythm generation (pre-Bötzinger complex):**
    Smith, J.C., et al. (1991). "Pre-Bötzinger complex: a
    brainstem region that may generate respiratory rhythm in
    mammals." *Science* 254:726–729. (Pre-Bötzinger complex —
    the primary respiratory rhythm generator.)
*   **Locus coeruleus and arousal:** Berridge, C.W., Waterhouse,
    B.D. (2003). "The locus coeruleus-noradrenergic system:
    modulation of behavioral state and state-dependent cognitive
    processes." *Brain Research Reviews* 42:33–84. (Locus
    coeruleus — arousal, attention, stress-response.)
*   **Brainstem glioma (DIPG / diffuse midline glioma):**
    Louis, D.N., et al. (2016). "The 2016 World Health
    Organization Classification of Tumors of the Central Nervous
    System: a summary." *Acta Neuropathologica* 131:803–820.
    (Diffuse midline glioma — pediatric brainstem tumor
    arising in the pons.)
*   **Wallenberg syndrome (lateral medullary syndrome):**
    Wallenberg, A. (1895). "Akute Bulbäraffection
    (Embolie der Arteria cerebelli posterior inferior
    sinistra)." *Archiv für Psychiatrie und
    Nervenkrankheiten* 27:504–540. (Lateral medullary
    syndrome — PICA infarct.)
*   **Locked-in syndrome (ventral pontine infarction):**
    Plum, F., Posner, J.B. (1980). *The Diagnosis of Stupor and
    Coma*, 3rd ed. (Locked-in syndrome — ventral pontine
    infarction; the basis pontis.)
*   **Congenital central hypoventilation syndrome (Ondine's
    curse):** Weese-Mayer, D.E., et al. (2010). "An official
    ATS clinical policy statement: congenital central
    hypoventilation syndrome." *American Journal of Respiratory
    and Critical Care Medicine* 181:1262–1269. (Ondine's curse
    — medullary respiratory center dysfunction.)
*   **Area postrema syndrome (NMOSD):** Pittock, S.J., Lucchinetti,
    C.F. (2016). "Neuromyelitis optica and the evolving spectrum
    of autoimmune aquaporin-4 channelopathies." *Multiple
    Sclerosis Journal* 22:1534–1543. (Area postrema syndrome —
    intractable hiccups and vomiting in NMOSD.)
*   **SLEA (contrast — the hindbrain is NOT included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the hindbrain.)
*   NeuroNames — Hindbrain; FMA — Hindbrain (rhombencephalon).
"""