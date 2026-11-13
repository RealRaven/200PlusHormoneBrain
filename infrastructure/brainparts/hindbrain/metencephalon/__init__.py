"""
infrastructure.brainparts.hindbrain.metencephalon
=================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    ├── metencephalon                          <-- THIS MODULE
    │   ├── cerebellum
    │   ├── fourth_ventricle
    │   └── pons
    └── myelencephalon

**Primary synonym:** Metencephalon; the rostral rhombencephalic
vesicle derivative; the "after-brain" (epencephalon in older
literature); the pons–cerebellum–fourth-ventricle compartment.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
single grey-matter or white-matter structure.** A
**developmental sub-region** — the **rostral** of the **two
rhombencephalic sub-vesicles**, whose **cavity is the fourth
ventricle** and whose **parenchyma is the pons and the
cerebellum**.
**Part of:** The **hindbrain** container — the **rostral**
hindbrain sub-container. The **hindbrain** is the **caudal** of
the **three primary brain vesicles** (prosencephalon → forebrain;
mesencephalon → midbrain; rhombencephalon → hindbrain).
**Structural parent:** ``.../hindbrain/`` → **direct child** of
the hindbrain container.
**Structural children:** **Three** — ``cerebellum/``,
``fourth_ventricle/``, and ``pons/``. Each is a **sub-container**.
The **pontine nuclei**, **cerebellar peduncles**, **cranial
nerve nuclei (V–VIII)**, **parabrachial complex**, **locus
coeruleus**, **pedunculopontine nucleus**, **laterodorsal
tegmental nucleus**, **superior olivary complex**, **pontine
reticular formation**, **cerebellar cortex**, **cerebellar deep
nuclei**, **cerebellar white matter**, and **median aperture
(foramen of Magendie)** are documented as **children of those
sub-containers**, not directly as children of the metencephalon.
**Boundary status (NOT the hindbrain container — the metencephalon
is a SUB-CONTAINER):** **Boundary case — the metencephalon is NOT
the hindbrain.** The **hindbrain** (``.../hindbrain/``) is the
**container** — the **whole rhombencephalon derivative**,
including the metencephalon **and** the myelencephalon. The
**metencephalon** (here) is the **rostral** sub-container. **The
metencephalon is a PART of the hindbrain; the hindbrain is the
WHOLE.** Consumers must **not** conflate the metencephalon with
the hindbrain container.
**Boundary status (NOT the myelencephalon — the myelencephalon is
the CAUDAL SIBLING):** **Boundary case — the metencephalon is NOT
the myelencephalon.** The **myelencephalon**
(``.../hindbrain/myelencephalon/``) is the **caudal** hindbrain
sub-container — the **medulla oblongata**. The **metencephalon**
(here) is the **rostral** hindbrain sub-container — the **pons,
cerebellum, and fourth ventricle**. **They are DIFFERENT
developmental sub-compartments** — the **metencephalon** is
**rostral**; the **myelencephalon** is **caudal**. They are
**continuous at the pontomedullary junction** (the
**bulbopontine sulcus**), but they are **distinct
sub-compartments**. Consumers must **not** conflate the
metencephalon with the myelencephalon.
**Boundary status (NOT the cerebellum alone — the cerebellum is a
CHILD):** **Boundary case — the metencephalon is NOT the
cerebellum.** The **cerebellum**
(``.../hindbrain/metencephalon/cerebellum/``) is the
**metencephalic** motor-coordination structure — the
**hemispheres**, the **vermis**, the **deep nuclei** (dentate,
fastigial, interposed), and the **cerebellar cortex**. The
**metencephalon** (here) **contains** the cerebellum **and** the
pons, **and** the fourth ventricle. Consumers must **not**
conflate the metencephalon with the cerebellum — the
**cerebellum** is a **child sub-container**; the
**metencephalon** is the **container**.
**Boundary status (NOT the pons alone — the pons is a CHILD):**
**Boundary case — the metencephalon is NOT the pons.** The
**pons** (``.../hindbrain/metencephalon/pons/``) is the
**metencephalic** brainstem structure — the **basis pontis**
(pontine nuclei, corticospinal and corticobulbar tracts,
transverse pontine fibers), the **tegmentum**, the **cerebellar
peduncles**, and the **cranial nerve nuclei (V, VI, VII,
VIII)**. The **metencephalon** (here) **contains** the pons
**and** the cerebellum, **and** the fourth ventricle. Consumers
must **not** conflate the metencephalon with the pons — the
**pons** is a **child sub-container**; the **metencephalon** is
the **container**.
**Boundary status (NOT the fourth ventricle alone — the fourth
ventricle is a CHILD):** **Boundary case — the metencephalon is
NOT the fourth ventricle.** The **fourth ventricle**
(``.../hindbrain/metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **metencephalon** (here) is the
**developmental sub-region** whose **cavity** is the fourth
ventricle. **The fourth ventricle is the CAVITY of the
metencephalon; the metencephalon is the TISSUE REGION around
it.** Consumers must **not** conflate the metencephalon with the
fourth ventricle.
**Boundary status (NOT the midbrain — the midbrain is ROSTRAL):**
**Boundary case — the metencephalon is NOT the midbrain.** The
**midbrain** (``.../midbrain/``) is the **mesencephalon**
derivative — the **tectum** (superior and inferior colliculi),
the **tegmentum** (substantia nigra, red nucleus,
periaqueductal gray, ventral tegmental area), the **cerebral
peduncle**, and the **mesencephalic aqueduct**. The
**metencephalon** (here) is the **rostral** rhombencephalic
sub-vesicle. **They are DIFFERENT developmental compartments** —
the **midbrain** is **rostral** to the metencephalon; the
**metencephalon** is **caudal** to the midbrain. They are
continuous at the **mesencephalic–metencephalic junction** (the
**caudal midbrain / rostral pons junction**), but they are
**distinct sub-compartments**. Consumers must **not** conflate
the metencephalon with the midbrain.
**Boundary status (NOT the diencephalon — the diencephalon is
FURTHER ROSTRAL):** **Boundary case — the metencephalon is NOT
the diencephalon.** The **diencephalon**
(``.../forebrain/diencephalon/``) is the **prosencephalic**
sub-vesicle — the **thalamus**, **hypothalamus**,
**epithalamus**, **subthalamus**, and **third ventricle**. The
**metencephalon** (here) is the **rostral** rhombencephalic
sub-vesicle. **They are DIFFERENT developmental compartments** —
the **diencephalon** is **rostral**; the **metencephalon** is
**caudal** (separated by the **midbrain**). Consumers must
**not** conflate the metencephalon with the diencephalon.
**Boundary status (NOT the forebrain — the forebrain is
ROSTRAL):** **Boundary case — the metencephalon is NOT the
forebrain.** The **forebrain** (``.../forebrain/``) is the
**prosencephalon** derivative — the **telencephalon** and the
**diencephalon**. The **metencephalon** (here) is the **rostral**
rhombencephalic sub-vesicle. **They are DIFFERENT developmental
compartments** — the **forebrain** is **rostral**; the
**metencephalon** is **caudal** (separated by the **midbrain**).
Consumers must **not** conflate the metencephalon with the
forebrain.
**Boundary status (NOT the spinal cord — the spinal cord is
CAUDAL, beyond the medulla):** **Boundary case — the
metencephalon is NOT the spinal cord.** The **spinal cord**
(``.../spinal_cord/``) is the **caudal** continuation of the
neuraxis — the **gray matter** and **white matter** caudal to
the **medulla oblongata**. The **metencephalon** (here) is the
**rostral** hindbrain sub-container — **rostral** to the
**medulla oblongata** (which is in the myelencephalon), which is
**rostral** to the spinal cord. **The metencephalon is separated
from the spinal cord by the whole myelencephalon.** Consumers
must **not** conflate the metencephalon with the spinal cord.
**Boundary status (NOT the rhombencephalon — the rhombencephalon
is the EMBRYONIC vesicle; the metencephalon is its ROSTRAL
derivative):** **Boundary case — the metencephalon is the
ROSTRAL ADULT derivative of the rhombencephalon, not the
embryonic vesicle itself.** The **rhombencephalon** is the
**embryonic** brain vesicle (the **caudal** of the three primary
vesicles). The **metencephalon** (here) is the **rostral** adult
derivative (the **pons + cerebellum + fourth ventricle**); the
**myelencephalon** is the **caudal** adult derivative (the
**medulla oblongata**). The **rhombencephalon** is documented as
**prose** (the developmental origin); the **metencephalon** is
the **adult sub-region**. Consumers must **not** conflate the
metencephalon with the rhombencephalon.
**Boundary status (NOT a single functional system — MULTIPLE
sub-structures with DIFFERENT functions):** **Boundary case —
the metencephalon is a HETEROGENEOUS developmental sub-region
with MULTIPLE sub-structures and MULTIPLE functions, not a single
uniform system.** The metencephalon includes:
*   **Cerebellum** — motor coordination, balance, motor learning,
    cerebellar cognitive-affective syndrome.
*   **Pons** — pontine nuclei, corticospinal/corticobulbar
    relay, cranial nerve nuclei V–VIII, pontine respiratory
    group, locus coeruleus, parabrachial complex,
    pedunculopontine nucleus, laterodorsal tegmental nucleus,
    superior olivary complex, pontine reticular formation.
*   **Fourth ventricle** — the metencephalic CSF cavity.
**Each sub-structure is functionally distinct** — the tree wires
the **cerebellum**, **fourth_ventricle**, and **pons** as
**sub-containers**, and the functional sub-regions are
documented as **children of those sub-containers** or as
**prose**. Consumers must **not** treat the metencephalon as a
single uniform region — it is a **distributed developmental
sub-region** with **heterogeneous sub-structures**.
**Boundary status (SLEA-FREE — the metencephalon is NOT an
extended-amygdala component):** **Boundary case — the
metencephalon is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The **metencephalon**
is a **developmental sub-region** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the
metencephalon — it is **SLEA-free**.
**Boundary status (NOT a neural processor in the classical sense
— the metencephalon is a REGION, not a single processor):**
**Boundary case — the metencephalon is a REGION, not a single
neural processor.** It **contains** neural processors (the
cerebellum, the pontine nuclei, the pontine respiratory group,
the reticular formation, the cranial nerve nuclei V–VIII) — but
it is **not itself a processor**. The **processing** happens in
the **sub-structures** (cerebellum, pons). Consumers must **not**
treat the metencephalon as a **single neural processor** — it is
a **developmental sub-region** with **heterogeneous
sub-structures**, each with its own function.

Overview
--------
The metencephalon is the **rostral** of the **two rhombencephalic
sub-vesicles** — the **adult sub-region** comprising the
**cerebellum**, the **pons**, and the **fourth ventricle**. It is
a **container module** with three **structural sub-containers**
(``cerebellum/``, ``fourth_ventricle/``, and ``pons/``).

**The metencephalon is the ROSTRAL hindbrain sub-container,
distinct from the myelencephalon (the caudal hindbrain
sub-container).** They are **continuous at the pontomedullary
junction** (the **bulbopontine sulcus**), but they are **distinct
sub-compartments** — the **metencephalon** is **rostral**; the
**myelencephalon** is **caudal**.

**The metencephalon is ROSTRAL to the myelencephalon and CAUDAL to
the midbrain.** The **midbrain** (``.../midbrain/``) is
**rostral**; the **myelencephalon**
(``.../hindbrain/myelencephalon/``) is **caudal**. They are
**different developmental compartments** — the **midbrain** is
the **mesencephalon** derivative; the **metencephalon** is the
**rostral rhombencephalon** derivative.

**The metencephalon is a HETEROGENEOUS developmental sub-region,
not a single structure.** It includes the **cerebellum** (motor
coordination, balance, motor learning), the **pons** (pontine
nuclei, corticospinal/corticobulbar relay, cranial nerve nuclei
V–VIII, pontine respiratory group, locus coeruleus, parabrachial
complex), and the **fourth ventricle** (CSF cavity). Each
sub-structure is functionally distinct.

**The metencephalon is a REGION, not a single neural processor.**
The **processing** happens in the **sub-structures** (cerebellum,
pons). The **metencephalon** is the **developmental sub-region**
that **contains** those sub-structures.

Metencephalon Composition (prose, not structural children)
----------------------------------------------------------
The metencephalon is a **developmental sub-region** with **three
sub-containers** — documented as **structural children**
(``cerebellum/``, ``fourth_ventricle/``, and ``pons/``) — and
**many prose-defined sub-structures** documented within those
sub-containers:

*   **Cerebellum** (``.../hindbrain/metencephalon/cerebellum/``)
    — the **motor-coordination sub-container**:
    *   **Hemispheres** — the **left** and **right** cerebellar
        hemispheres (motor coordination, motor learning).
    *   **Vermis** — the **midline** cerebellar vermis (posture,
        gait, axial motor control).
    *   **Nuclei** — the **dentate nucleus**, **fastigial
        nucleus**, and **interposed nucleus** (the **cerebellar
        deep nuclei** — motor output).
    *   **Deep white matter** — the **cerebellar white matter**
        (the **arbor vitae**).

*   **Fourth ventricle**
    (``.../hindbrain/metencephalon/fourth_ventricle/``) — the
    **CSF-cavity sub-container**:
    *   **Median aperture (foramen of Magendie)** — the
        **midline** CSF outflow aperture into the
        **subarachnoid space**.
    *   (The **lateral apertures — foramina of Luschka** — are
        documented as prose, and are the **lateral** CSF
        outflow apertures into the **subarachnoid space**.)

*   **Pons** (``.../hindbrain/metencephalon/pons/``) — the
    **brainstem sub-container**:
    *   **Basis pontis** — the **ventral pons** (pontine nuclei,
        corticospinal/corticobulbar tracts, transverse pontine
        fibers).
    *   **Tegmentum** — the **dorsal pons** (reticular formation,
        cranial nerve nuclei V–VIII, locus coeruleus,
        parabrachial complex, pedunculopontine nucleus,
        laterodorsal tegmental nucleus).
    *   **Cerebellar peduncles** — the **superior**, **middle**,
        and **inferior** cerebellar peduncles (white-matter
        tracts connecting the cerebellum to the brainstem).
    *   **Cranial nerve nuclei** — the **trigeminal (V)**,
        **abducens (VI)**, **facial (VII)**, and
        **vestibulocochlear (VIII)** nuclei.
    *   **Parabrachial area** — the **lateral** and **medial
        parabrachial nuclei** and the **subparabrachial
        nucleus** (autonomic and respiratory relay).
    *   **Superior olivary complex** — the **lateral superior
        olive**, **medial nucleus of trapezoid body**, and
        **medial superior olive** (auditory processing).
    *   **Pontine reticular formation** — the **caudal pontine
        reticular nucleus**, **paramedian pontine reticular
        formation**, **parvocellular reticular nucleus**, and
        **tegmental pontine reticular nucleus** (arousal,
        sleep-wake, autonomic reflexes).

**These sub-structures are prose (or children of the
sub-containers), not direct structural children of the
metencephalon.** The tree wires the **metencephalon** as a
**container** with **three sub-containers** (``cerebellum/``,
``fourth_ventricle/``, and ``pons/``) — the finer sub-regions
(pontine nuclei, cranial nerve nuclei, cerebellar deep nuclei,
etc.) are documented as **children of those sub-containers** or
as **prose**. Consumers that need **sub-region-level** resolution
should consult the **sub-container modules** and the references,
not the metencephalon container.

The Metencephalon / Hindbrain Boundary
--------------------------------------
This is the **sub-container-vs-container** boundary:

*   **Metencephalon** (this module) — the **rostral** hindbrain
    sub-container.

*   **Hindbrain** (``.../hindbrain/``) — the **whole**
    rhombencephalon derivative (metencephalon +
    myelencephalon).

**The metencephalon is a PART of the hindbrain; the hindbrain is
the WHOLE.** Consumers must **not** conflate the metencephalon
with the hindbrain container.

The Metencephalon / Myelencephalon Boundary
-------------------------------------------
This is the **rostral-vs-caudal** boundary:

*   **Metencephalon** (this module) — the **rostral** hindbrain
    sub-container (pons + cerebellum + fourth ventricle).

*   **Myelencephalon** (``.../hindbrain/myelencephalon/``) — the
    **caudal** hindbrain sub-container (medulla oblongata).

**They are DIFFERENT developmental sub-compartments** — the
**metencephalon** is **rostral**; the **myelencephalon** is
**caudal**. They are **continuous at the pontomedullary
junction** (the **bulbopontine sulcus**), but they are **distinct
sub-compartments**. Consumers must **not** conflate the
metencephalon with the myelencephalon.

The Metencephalon / Cerebellum Boundary
---------------------------------------
This is the **container-vs-child** boundary:

*   **Metencephalon** (this module) — the **container**.

*   **Cerebellum**
    (``.../hindbrain/metencephalon/cerebellum/``) — the
    **motor-coordination child sub-container**.

**The cerebellum is a child sub-container of the metencephalon.**
Consumers must **not** conflate the metencephalon with the
cerebellum — the **cerebellum** is a **child**; the
**metencephalon** is the **container**.

The Metencephalon / Pons Boundary
---------------------------------
This is the **container-vs-child** boundary:

*   **Metencephalon** (this module) — the **container**.

*   **Pons** (``.../hindbrain/metencephalon/pons/``) — the
    **brainstem child sub-container**.

**The pons is a child sub-container of the metencephalon.**
Consumers must **not** conflate the metencephalon with the pons —
the **pons** is a **child**; the **metencephalon** is the
**container**.

The Metencephalon / Fourth Ventricle Boundary
---------------------------------------------
This is the **region-vs-CSF-cavity** boundary:

*   **Metencephalon** (this module) — the **developmental
    sub-region**.

*   **Fourth ventricle**
    (``.../hindbrain/metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The fourth ventricle is the CAVITY of the metencephalon; the
metencephalon is the TISSUE REGION around it.** Consumers must
**not** conflate the metencephalon with the fourth ventricle.

The Metencephalon / Midbrain Boundary
-------------------------------------
This is the **caudal-vs-rostral** boundary:

*   **Metencephalon** (this module) — the **rostral**
    rhombencephalic sub-vesicle.

*   **Midbrain** (``.../midbrain/``) — the **mesencephalon**
    derivative (tectum + tegmentum + cerebral peduncle).

**They are DIFFERENT developmental compartments** — the
**midbrain** is **rostral**; the **metencephalon** is **caudal**.
They are continuous at the **mesencephalic–metencephalic
junction** (the **caudal midbrain / rostral pons junction**), but
they are **distinct sub-compartments**. Consumers must **not**
conflate the metencephalon with the midbrain.

The Metencephalon / Diencephalon Boundary
-----------------------------------------
This is the **caudal-vs-further-rostral** boundary:

*   **Metencephalon** (this module) — the **rostral**
    rhombencephalic sub-vesicle.

*   **Diencephalon** (``.../forebrain/diencephalon/``) — the
    **prosencephalic** sub-vesicle (thalamus, hypothalamus,
    epithalamus, subthalamus, third ventricle).

**They are DIFFERENT developmental compartments** — the
**diencephalon** is **rostral**; the **metencephalon** is
**caudal** (separated by the **midbrain**). Consumers must
**not** conflate the metencephalon with the diencephalon.

The Metencephalon / Forebrain Boundary
--------------------------------------
This is the **caudal-vs-rostral** boundary:

*   **Metencephalon** (this module) — the **rostral**
    rhombencephalic sub-vesicle.

*   **Forebrain** (``.../forebrain/``) — the **prosencephalon**
    derivative (telencephalon + diencephalon).

**They are DIFFERENT developmental compartments** — the
**forebrain** is **rostral**; the **metencephalon** is **caudal**
(separated by the **midbrain**). Consumers must **not** conflate
the metencephalon with the forebrain.

The Metencephalon / Spinal Cord Boundary
----------------------------------------
This is the **brain-vs-spinal-cord** boundary:

*   **Metencephalon** (this module) — the **rostral** hindbrain
    sub-container.

*   **Spinal cord** (``.../spinal_cord/``) — the **caudal**
    continuation of the neuraxis, beginning at the
    **cervicomedullary junction**.

**The metencephalon is separated from the spinal cord by the whole
myelencephalon.** Consumers must **not** conflate the
metencephalon with the spinal cord.

The Metencephalon / Rhombencephalon Boundary
--------------------------------------------
This is the **adult-sub-region-vs-embryonic-vesicle** boundary:

*   **Metencephalon** (this module) — the **rostral ADULT
    derivative** of the rhombencephalon.

*   **Rhombencephalon** — the **embryonic** brain vesicle (prose).

**The metencephalon is the ROSTRAL ADULT derivative; the
rhombencephalon is the EMBRYONIC vesicle.** The terms are often
used interchangeably, but the **tree wires the adult structure**.
Consumers must **not** conflate the metencephalon with the
rhombencephalon — the **rhombencephalon** is the **developmental
origin**; the **metencephalon** is the **adult sub-region**.

The Metencephalon / SLEA Boundary
---------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Metencephalon** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The metencephalon is NOT part of the SLEA continuum.** It is a
**developmental sub-region**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the
metencephalon.

Function in the Human Brain
---------------------------
The metencephalon's functions are **heterogeneous** — documented
at the **sub-structure** level, not at the sub-region level:

*   **Motor Coordination and Balance (Cerebellum):** The
    **cerebellum** — the **metencephalic** sub-structure —
    coordinates **voluntary movement**, **balance**, **posture**,
    and **motor learning**. It is the **neural substrate** of
    **cerebellar motor coordination** and **cerebellar
    cognitive-affective syndrome**.

*   **Corticospinal / Corticobulbar Relay (Pons):** The **basis
    pontis** — the **ventral pons** — contains the **pontine
    nuclei** and the **transverse pontine fibers** that **relay**
    the **corticospinal** and **corticobulbar** tracts from the
    cortex to the cerebellum and the medulla. The **pons** is a
    **major relay station** in the motor pathway.

*   **Cranial Nerve Nuclei (Pons):** The **pons** contains the
    **cranial nerve nuclei V (trigeminal), VI (abducens), VII
    (facial), and VIII (vestibulocochlear)**. These nuclei are
    the **brainstem control centers** for **facial sensation**,
    **eye movement**, **facial expression**, **hearing**,
    **balance**, and **taste**.

*   **Respiratory Control (Pons):** The **pontine respiratory
    group** (the **pneumotaxic center** and the **apneustic
    center**) is the **pontine respiratory center** — it
    **modulates** the **respiratory rhythm** generated in the
    **medulla** (the **pre-Bötzinger complex**).

*   **Arousal and Sleep-Wake (Pons):** The **locus coeruleus**
    (noradrenergic), the **pedunculopontine nucleus** and
    **laterodorsal tegmental nucleus** (cholinergic), and the
    **parabrachial complex** (glutamatergic) are **brainstem
    arousal and sleep-wake centers** — they **modulate**
    **wakefulness**, **REM sleep**, and **arousal**.

*   **Auditory Processing (Pons):** The **superior olivary
    complex** — the **lateral superior olive**, the **medial
    nucleus of trapezoid body**, and the **medial superior
    olive** — is the **brainstem auditory processing center** —
    it **processes** **sound localization** and **auditory
    timing** (interaural time and intensity differences).

*   **Reticular Formation (Pons):** The **pontine reticular
    formation** — the **caudal pontine reticular nucleus**,
    **paramedian pontine reticular formation**,
    **parvocellular reticular nucleus**, and **tegmental
    pontine reticular nucleus** — is part of the **brainstem
    arousal system**, the **descending pain modulation system**,
    and the **autonomic reflex integration system** (including
    the **pontine micturition center**).

*   **CSF Production and Circulation (Fourth Ventricle):** The
    **choroid plexus of the fourth ventricle** (in the
    metencephalon) **produces CSF**; the fourth ventricle is a
    **CSF compartment** in the **CSF flow path** (third ventricle
    → mesencephalic aqueduct → fourth ventricle → **median
    aperture (Magendie)** and **lateral apertures (Luschka)** →
    subarachnoid space).

*   **NOT a single neural processor.** The metencephalon is a
    **developmental sub-region** — the **processing** happens in
    the **sub-structures** (cerebellum, pons). Consumers must
    **not** treat the metencephalon as a **single processor** —
    it is a **sub-region** with **heterogeneous sub-structures**.

**The unifying theme:** the metencephalon is the **rostral
hindbrain sub-region** — the **rostral rhombencephalon
derivative** — that **contains** the **cerebellum** (motor
coordination), the **pons** (corticospinal/corticobulbar relay,
cranial nerve nuclei V–VIII, pontine respiratory group, arousal
centers, superior olivary complex), and the **fourth ventricle**
(CSF cavity). It is a **heterogeneous developmental sub-region**,
**NOT a single neural processor**, and **NOT the hindbrain
container, myelencephalon, midbrain, or spinal cord**.

Associated Disorders
--------------------
The metencephalon has **no single named clinical syndrome** — its
clinical associations are **heterogeneous**, via the
**sub-structures** it contains:

*   **Cerebellar Disorders (via the Cerebellum):** **Cerebellar
    ataxia** (gait ataxia, limb ataxia, dysarthria, nystagmus),
    **cerebellar cognitive-affective syndrome** (executive
    dysfunction, visuospatial deficits, affective
    dysregulation), **spinocerebellar ataxias** (SCAs),
    **cerebellar tumors** (medulloblastoma, pilocytic
    astrocytoma), and **cerebellar stroke** (PICA, AICA, SCA
    infarcts). The **cerebellum** is the **substrate**.

*   **Pontine Disorders (via the Pons):** **Pontine stroke**
    (locked-in syndrome from ventral pontine infarction,
    paramedian pontine syndromes), **central pontine myelinolysis**
    (osmotic demyelination syndrome), **pontine glioma** (diffuse
    intrinsic pontine glioma — DIPG), and **pontine hemorrhage**.
    The **pons** is the **substrate**.

*   **Brainstem Glioma (via the Metencephalon):** **Diffuse
    midline glioma** (formerly DIPG) — a **pediatric brainstem
    tumor** arising in the **pons**. The **metencephalon** is the
    **region**; the **pons** is the **primary substrate**.

*   **Brainstem Stroke (via the Metencephalon):** **Pontine
    infarcts** — **ischemic** or **hemorrhagic** — causing
    **cranial nerve deficits**, **long tract signs**,
    **autonomic dysfunction**, and **disorders of
    consciousness**. The **metencephalon** is the **region**; the
    **pons** is the **substrate**.

*   **Central Pontine Myelinolysis (via the Pons):** **Osmotic
    demyelination syndrome** — **demyelination** of the **basis
    pontis**, typically after **rapid correction of
    hyponatremia** — causing **quadriparesis**,
    **pseudobulbar palsy**, and **locked-in syndrome**. The
    **pons** is the **substrate**.

*   **Locked-In Syndrome (via the Pons):** **Ventral pontine
    infarction** — **quadriplegia** with **preserved
    consciousness** and **vertical eye movements** (the
    **basis pontis** is the **substrate**).

*   **Locus Coeruleus Dysfunction (via the Pons):** **Arousal**,
    **attention**, and **stress-response** dysfunction — the
    **locus coeruleus** (the **major noradrenergic nucleus**) is
    implicated in **PTSD**, **depression**, **anxiety**, and
    **Alzheimer's disease** (early locus coeruleus tau
    pathology). The **pons** is the **substrate**.

*   **Superior Olivary Complex Dysfunction (via the Pons):**
    **Auditory processing deficits** — **sound localization**
    deficits, **auditory neuropathy spectrum disorder**, and
    **age-related hearing loss** (central component). The
    **pons** is the **substrate**.

*   **No Named "Metencephalon Syndrome":** The metencephalon is a
    **developmental sub-region**, not a **single structure** — it
    has **no named clinical syndrome**. Its clinical relevance is
    **heterogeneous**, via the **sub-structures** it contains.

**What is NOT here:** The metencephalon is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala), **fear conditioning**
(central nucleus + basolateral nuclei), **Urbach-Wiethe disease**
(amygdala), or **Parkinson's disease** (substantia nigra, in the
midbrain). Its clinical relevance is **heterogeneous**, via the
**cerebellum**, **pons**, and **fourth ventricle**. **No named
metencephalon syndrome exists.**

Lateralization Notes
--------------------
This is the **metencephalon** container module. The metencephalon
is a **midline-spanning developmental sub-region** with
**bilateral sub-structures** — and it carries **NO warning**:

*   **Bilateral Sub-Structures:** The **cerebellum** has **left
    and right hemispheres**; the **pons** has **bilateral
    cranial nerve nuclei** and **bilateral
    ascending/descending tracts**. The metencephalon is **not a
    paired structure** in the way the **lateral ventricles** or
    the **amygdala** are — it is a **midline sub-region** with
    **bilateral sub-structures**.

*   **Partial Lateralization (Contested):** Some **cerebellar
    functions** are **partially lateralized** (e.g., **language**
    is more **right cerebellar**; **visuospatial** function is
    more **left cerebellar**) — this is **partial**,
    **contested**, and documented in the **cerebellum module**
    (not at the metencephalon level).

*   **NO Extended-Amygdala Warning (SLEA-free):** The
    metencephalon is **NOT** an extended-amygdala component. It
    carries **no SLEA warning**. Consumers must **not** import
    the SLEA warning into the metencephalon.

*   **NO Amygdala-Lateralization Warning:** The metencephalon is
    **NOT** the fear-output or the fear-learning structure. It is
    a **developmental sub-region** — consumers must **not**
    conflate it with the **amygdala** or the **fear circuit**.

**A consumer that assumes "metencephalon = left + right" will be
structurally correct for the bilateral sub-structures** — the
metencephalon is a **midline sub-region** with **bilateral
sub-structures**. The metencephalon carries **NO warning** — **no
SLEA warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-region imports.** The **container** does **not**
    import from ``.../hindbrain/`` (parent),
    ``.../hindbrain/myelencephalon/`` (sibling),
    ``.../midbrain/`` (rostral neighbor),
    ``.../forebrain/``, ``.../spinal_cord/``,
    ``.../metencephalon/cerebellum/``, ``.../metencephalon/pons/``,
    or ``.../metencephalon/fourth_ventricle/`` — it is a
    **namespace container**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../forebrain/telencephalon/``,
    ``.../forebrain/diencephalon/``, ``.../midbrain/``,
    ``.../spinal_cord/``, or any other container. The
    metencephalon's relationships to the hindbrain,
    myelencephalon, midbrain, diencephalon, forebrain, spinal
    cord, rhombencephalon, cerebellum, pons, and fourth ventricle
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — three structural children.** The
    ``cerebellum/``, ``fourth_ventricle/``, and ``pons/`` are
    **sub-containers**. The **pontine nuclei**, **cerebellar
    peduncles**, **cranial nerve nuclei V–VIII**, **parabrachial
    complex**, **locus coeruleus**, **pedunculopontine
    nucleus**, **laterodorsal tegmental nucleus**, **superior
    olivary complex**, **pontine reticular formation**,
    **cerebellar cortex**, **cerebellar deep nuclei**,
    **cerebellar white matter**, and **median aperture (foramen
    of Magendie)** are **children of those sub-containers** or
    **prose**. Consumers must not assume any exist as direct
    children of the metencephalon; resolve sub-region-level
    detail through the sub-containers and the references.
*   **REGION — NOT a single structure.** The metencephalon is the
    **rostral rhombencephalon derivative** — a **heterogeneous
    developmental sub-region** containing the **cerebellum**,
    **pons**, and **fourth ventricle**. Consumers must **not**
    conflate the metencephalon with any single sub-structure.
*   **NOT the hindbrain container — the metencephalon is a
    SUB-CONTAINER.** The **hindbrain** is the **whole**
    rhombencephalon derivative; the **metencephalon** is the
    **rostral** sub-container.
*   **NOT the myelencephalon — the myelencephalon is the CAUDAL
    SIBLING.** The **metencephalon** is **rostral**; the
    **myelencephalon** is **caudal**. They are continuous at the
    **pontomedullary junction**.
*   **NOT the midbrain — the midbrain is ROSTRAL.** The
    **midbrain** is the **mesencephalon** derivative; the
    **metencephalon** is the **rostral rhombencephalon**
    derivative.
*   **NOT the diencephalon or forebrain — those are FURTHER
    ROSTRAL.** The **diencephalon** is **prosencephalic**; the
    **forebrain** is **prosencephalic**; the **metencephalon**
    is **rhombencephalic**.
*   **NOT the spinal cord — the spinal cord is CAUDAL, beyond the
    medulla.** The **metencephalon** is separated from the
    spinal cord by the whole **myelencephalon**.
*   **NOT the fourth ventricle — the fourth ventricle is INSIDE
    the metencephalon.** The **metencephalon** is the **tissue
    region**; the **fourth ventricle** is the **CSF cavity**
    within it.
*   **NOT the cerebellum or pons alone — those are
    SUB-STRUCTURES.** The **metencephalon** is the **region**;
    the **sub-structures** are its **contents**.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    metencephalon is **not** an extended-amygdala component, and
    it carries **no SLEA warning**.
*   **NOT a single neural processor — the metencephalon is a
    REGION.** The **processing** happens in the **sub-structures**
    (cerebellum, pons). Consumers must **not** treat the
    metencephalon as a **single processor**.
*   **No ``AREA_PATHS`` hop.** The metencephalon is a local
    sub-container under ``hindbrain/``, not a cross-listed
    container.
*   **No nested cross-listing.** The metencephalon has no nested
    dual-framing module. It is a single sub-container with three
    sub-containers.
*   **No lateralization warning.** The metencephalon carries
    **no warning** — **no SLEA warning**, **no
    amygdala-lateralization warning**, and **no
    rhinencephalon-exclusion flag**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon import (
        cerebellum, fourth_ventricle, pons,
    )

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon"
    )
    cerebellum_path = (
        "hindbrain.metencephalon.cerebellum"
    )
    pons_path = (
        "hindbrain.metencephalon.pons"
    )
    fourth_ventricle_path = (
        "hindbrain.metencephalon.fourth_ventricle"
    )

**Do not** assume the metencephalon is the **hindbrain**. The
**hindbrain** is the **whole** rhombencephalon derivative; the
**metencephalon** is the **rostral** sub-container.

**Do not** assume the metencephalon is the **myelencephalon**.
The **myelencephalon** is the **caudal** sub-container
(medulla oblongata).

**Do not** assume the metencephalon is the **midbrain**,
**diencephalon**, or **forebrain**. The **midbrain** is
**rostral**; the **diencephalon** and **forebrain** are
**further rostral**.

**Do not** assume the metencephalon is the **spinal cord**. The
**metencephalon** is separated from the spinal cord by the whole
**myelencephalon**.

**Do not** assume the metencephalon is the **fourth ventricle**,
**cerebellum**, or **pons alone**. The **metencephalon** is the
**region**; the **sub-structures** are its **contents**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the metencephalon. **The
metencephalon is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the metencephalon's children (recommended consumer
pattern)::

    METENCEPHALON_CHILDREN = (
        "cerebellum", "fourth_ventricle", "pons",
    )
    # The cerebellum, fourth ventricle, and pons are
    # sub-containers. The finer sub-regions are children of those
    # sub-containers.

Reaching the hindbrain (recommended consumer pattern — the
parent)::

    # The hindbrain is the WHOLE rhombencephalon derivative:
    #
    #   hindbrain
    #
    # The metencephalon is the ROSTRAL sub-container.

Reaching the myelencephalon (recommended consumer pattern — the
caudal sibling)::

    # The myelencephalon is the CAUDAL hindbrain sub-container:
    #
    #   hindbrain.myelencephalon
    #
    # The metencephalon is ROSTRAL; the myelencephalon is CAUDAL.
    # They are continuous at the pontomedullary junction.

Reaching the midbrain (recommended consumer pattern — the rostral
neighbor)::

    # The midbrain is the MESENCEPHALON derivative ROSTRAL to the
    # metencephalon:
    #
    #   midbrain
    #
    # The metencephalon is CAUDAL to the midbrain.

Reaching the diencephalon (recommended consumer pattern — NOTE
the further-rostral boundary)::

    # The diencephalon is the PROSENCEPHALIC sub-vesicle FURTHER
    # ROSTRAL:
    #
    #   forebrain.diencephalon
    #
    # The diencephalon is separated from the metencephalon by the
    # midbrain.

Reaching the forebrain (recommended consumer pattern — NOTE the
rostral boundary)::

    # The forebrain is the PROSENCEPHALON derivative:
    #
    #   forebrain
    #
    # The forebrain is ROSTRAL to the metencephalon (separated by
    # the midbrain).

Reaching the spinal cord (recommended consumer pattern — NOTE
the caudal boundary)::

    # The spinal cord is CAUDAL to the whole hindbrain (beyond the
    # medulla oblongata):
    #
    #   spinal_cord
    #
    # The metencephalon is separated from the spinal cord by the
    # whole myelencephalon.

Reaching the cerebellum (recommended consumer pattern — the
child)::

    # The cerebellum is the METENCEPHALIC motor-coordination
    # sub-container:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cerebellum is a CHILD sub-container of the
    # metencephalon.

Reaching the pons (recommended consumer pattern — the child)::

    # The pons is the METENCEPHALIC brainstem sub-container:
    #
    #   hindbrain.metencephalon.pons
    #
    # The pons is a CHILD sub-container of the metencephalon.

Reaching the fourth ventricle (recommended consumer pattern —
the child)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The fourth ventricle is the CAVITY of the metencephalon.

Sub-region detail (not wired at the metencephalon level — consult
the sub-containers and references)::

    # The metencephalon's finer sub-regions are prose within the
    # sub-containers:
    #   cerebellum -> hemispheres, vermis, deep nuclei,
    #                 deep white matter
    #   fourth_ventricle -> median aperture (Magendie),
    #                       lateral apertures (Luschka) (prose)
    #   pons -> basis pontis, tegmentum, cerebellar peduncles,
    #           cranial nerve nuclei V-VIII, parabrachial area,
    #           superior olivary complex, pontine reticular
    #           formation
    #
    # Do not attempt to resolve these as sub-paths of the
    # metencephalon.

Bilateral iteration (recommended consumer pattern — for bilateral
sub-structures)::

    for side in ("left", "right"):
        # e.g., cerebellar hemispheres, cranial nerve nuclei
        side_path = (
            f"hindbrain.metencephalon.cerebellum.hemispheres.{side}"
        )
        # resolve side_path through the memory/recall layer

References
----------
*   **Canonical metencephalon anatomy:** Standring, S. (ed.)
    (2020). *Gray's Anatomy: The Anatomical Basis of Clinical
    Practice*, 42nd ed. (Metencephalon — pons, cerebellum,
    fourth ventricle.)
*   **Brainstem overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Metencephalon — pons, cerebellum; cranial nerve nuclei
    V–VIII; reticular formation.)
*   **Developmental origin (rhombencephalon → metencephalon):**
    Puelles, L., Rubenstein, J.L.R. (2015). "A new scenario of
    hypothalamic organization: implications of a new model of
    the prosomeric brain." *Journal of Comparative Neurology*
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
*   **Pontine respiratory group:** Lumsden, T. (1923).
    "Observations on the respiratory centres in the cat."
    *Journal of Physiology* 57:153–160. (Pontine respiratory
    group — pneumotaxic and apneustic centers.)
*   **Locus coeruleus and arousal:** Berridge, C.W., Waterhouse,
    B.D. (2003). "The locus coeruleus-noradrenergic system:
    modulation of behavioral state and state-dependent cognitive
    processes." *Brain Research Reviews* 42:33–84. (Locus
    coeruleus — arousal, attention, stress-response.)
*   **Superior olivary complex and sound localization:**
    Grothe, B., Pecka, M., McAlpine, D. (2010). "Mechanisms of
    sound localization in mammals." *Physiological Reviews*
    90:983–1012. (Superior olivary complex — sound localization;
    interaural time and intensity differences.)
*   **Brainstem glioma (DIPG / diffuse midline glioma):**
    Louis, D.N., et al. (2016). "The 2016 World Health
    Organization Classification of Tumors of the Central Nervous
    System: a summary." *Acta Neuropathologica* 131:803–820.
    (Diffuse midline glioma — pediatric brainstem tumor
    arising in the pons.)
*   **Central pontine myelinolysis:** Adams, R.D., Victor, M.,
    Mancall, E.L. (1959). "Central pontine myelinolysis: a
    hitherto undescribed disease occurring in alcoholic and
    malnourished patients." *A.M.A. Archives of Neurology and
    Psychiatry* 81:154–172. (Osmotic demyelination syndrome —
    demyelination of the basis pontis.)
*   **Locked-in syndrome (ventral pontine infarction):**
    Plum, F., Posner, J.B. (1980). *The Diagnosis of Stupor and
    Coma*, 3rd ed. (Locked-in syndrome — ventral pontine
    infarction; the basis pontis.)
*   **SLEA (contrast — the metencephalon is NOT included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the metencephalon.)
*   NeuroNames — Metencephalon; FMA — Metencephalon.
"""