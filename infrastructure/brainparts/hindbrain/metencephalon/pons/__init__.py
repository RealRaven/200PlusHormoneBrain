"""
infrastructure.brainparts.hindbrain.metencephalon.pons
======================================================

Anatomical Hierarchy
--------------------
::

    metencephalon
    ├── cerebellum
    ├── fourth_ventricle
    └── pons                                <-- THIS MODULE
        ├── caudal_pontine_reticular_nucleus
        ├── cerebellar_peduncles
        │   ├── inferior_cerebellar_peduncle
        │   ├── middle_cerebellar_peduncle
        │   └── superior_cerebellar_peduncle
        ├── cranial_nerve_nuclei
        │   ├── left
        │   │   ├── abducens_nucleus
        │   │   ├── chief_sensory_trigeminal_nucleus
        │   │   ├── facial_nerve_nucleus
        │   │   ├── motor_trigeminal_nucleus
        │   │   ├── superior_salivatory_nucleus
        │   │   └── vestibulocochlear_nuclei
        │   │       ├── cochlear_nuclei
        │   │       └── vestibular_nuclei
        │   └── right
        │       ├── abducens_nucleus
        │       ├── chief_sensory_trigeminal_nucleus
        │       ├── facial_nerve_nucleus
        │       ├── motor_trigeminal_nucleus
        │       ├── superior_salivatory_nucleus
        │       └── vestibulocochlear_nuclei
        │           ├── cochlear_nuclei
        │           └── vestibular_nuclei
        ├── parabrachial_area
        │   ├── lateral_parabrachial_nucleus
        │   ├── medial_parabrachial_nucleus
        │   └── subparabrachial_nucleus
        │       ├── kolliker_fuse_nucleus
        │       └── pontine_respiratory_group
        ├── paramedian_pontine_reticular_formation
        ├── parvocellular_reticular_nucleus
        ├── pontine_nuclei
        │   ├── left
        │   └── right
        ├── superior_olivary_complex
        │   ├── lateral_superior_olive
        │   │   ├── left
        │   │   └── right
        │   ├── medial_nucleus_of_trapezoid_body
        │   └── medial_superior_olive
        │       ├── left
        │       └── right
        └── tegmentum
            ├── laterodorsal_tegmental_nucleus
            ├── locus_coeruleus
            ├── nucleus_incertus
            ├── pedunculopontine_nucleus
            ├── pontine_micturition_center
            └── tegmental_pontine_reticular_nucleus

**Primary synonym:** Pons; pons Varolii ("bridge of Varolius" —
the historical name from Costanzo Varolio, 1573); the pontine
brainstem; the metencephalic brainstem; the pontine segment of
the brainstem; the basis pontis + pontine tegmentum.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**segmental brainstem region** — the **rostral hindbrain**
structure between the **midbrain** (rostral) and the **medulla
oblongata** (caudal), comprising the **basis pontis** (ventral
— pontine nuclei, corticospinal and corticobulbar tracts,
transverse pontine fibers), the **pontine tegmentum** (dorsal
— cranial nerve nuclei V–VIII, pontine reticular formation,
locus coeruleus, parabrachial complex, pedunculopontine
nucleus, laterodorsal tegmental nucleus, superior olivary
complex, nucleus incertus, pontine micturition center, and the
**tegmental pontine reticular nucleus**), and the **cerebellar
peduncles** (superior, middle, and inferior — the white-matter
tracts that connect the cerebellum to the brainstem).
**Part of:** The **metencephalon** container — the **rostral**
of the **two rhombencephalic sub-vesicles** (with the
cerebellum and the fourth ventricle). The **metencephalon** is
the **rostral** of the **two rhombencephalic sub-vesicles**;
the **hindbrain** is the **caudal** of the **three primary
brain vesicles**.
**Structural parent:** ``.../metencephalon/`` → **direct child**
of the metencephalon container.
**Structural children:** **Eleven** — ``caudal_pontine_
reticular_nucleus/``, ``cerebellar_peduncles/`` (with three
sub-containers: ``inferior_cerebellar_peduncle/``,
``middle_cerebellar_peduncle/``, ``superior_cerebellar_
peduncle/``), ``cranial_nerve_nuclei/`` (with left/right
sub-containers, each with six leaf nuclei, and the
``vestibulocochlear_nuclei/`` sub-container with left/right
sub-containers, each with ``cochlear_nuclei/`` and
``vestibular_nuclei/`` sub-containers), ``parabrachial_area/``
(with three sub-containers), ``paramedian_pontine_reticular_
formation/``, ``parvocellular_reticular_nucleus/``,
``pontine_nuclei/`` (with left/right sub-containers),
``superior_olivary_complex/`` (with ``lateral_superior_
olive/``, ``medial_nucleus_of_trapezoid_body/``, and
``medial_superior_olive/`` sub-containers, each with
left/right sub-containers for the olives), and ``tegmentum/``
(with six sub-containers: ``laterodorsal_tegmental_nucleus/``,
``locus_coeruleus/``, ``nucleus_incertus/``,
``pedunculopontine_nucleus/``,
``pontine_micturition_center/``, and
``tegmental_pontine_reticular_nucleus/``). The **basis pontis**
(ventral pons), the **transverse pontine fibers**, the
**corticospinal** and **corticobulbar** tracts within the
pons, the **pontine tegmentum** (as a general region), the
**medial longitudinal fasciculus** (MLF) within the pons,
the **medial lemniscus** within the pons, the **spinal
trigeminal tract** within the pons, and the **mesencephalic
trigeminal tract** within the pons are documented as **prose**,
not as structural children.
**Boundary status (PONS — NOT the metencephalon):** **Boundary
case — the pons is a CHILD of the metencephalon, NOT the
metencephalon.** The **metencephalon** (``.../metencephalon/``)
is the **container** — the **rostral** rhombencephalic
sub-vesicle, comprising the **pons**, the **cerebellum**, and
the **fourth ventricle**. The **pons** (here) is a **child
sub-container** of the metencephalon. **The pons is a PART of
the metencephalon; the metencephalon is the WHOLE.** Consumers
must **not** conflate the pons with the metencephalon
container.
**Boundary status (PONS — NOT the cerebellum):** **Boundary
case — the pons is the VENTRAL BRAINSTEM structure, NOT the
cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is the **dorsal
suprasegmental structure** — the **lateral hemispheres** and
the **midline vermis**, with the **cortical divisions** and
the **deep nuclei**. The **pons** (here) is the **ventral
brainstem** structure — the **basis pontis** and the
**tegmental pons**. **The pons is the VENTRAL BRAINSTEM; the
cerebellum is the DORSAL SUPRASEGMENTAL structure.** They are
**connected** via the **cerebellar peduncles** (children of
the pons — the **superior**, **middle**, and **inferior
cerebellar peduncles**), but they are **distinct structures**.
Consumers must **not** conflate the pons with the cerebellum.
**Boundary status (PONS — NOT the fourth ventricle):** **Boundary
case — the pons is the VENTRAL WALL of the fourth ventricle,
NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla
(ventrally) and the cerebellum (dorsally). The **pons** (here)
is the **ventral brainstem** structure that **forms the
ventral wall** of the fourth ventricle. **The pons is the
VENTRAL BRAINSTEM; the fourth ventricle is the CSF CAVITY.**
Consumers must **not** conflate the pons with the fourth
ventricle.
**Boundary status (PONS — NOT the medulla oblongata):**
**Boundary case — the pons is the ROSTRAL brainstem segment,
NOT the medulla oblongata (the CAUDAL brainstem segment).** The
**medulla oblongata**
(``.../hindbrain/myelencephalon/medulla_oblongata/``) is the
**caudal hindbrain** structure — the **myelencephalic** part
of the brainstem (from the pontomedullary junction caudally to
the foramen magnum / cervicomedullary junction). The **pons**
(here) is the **rostral hindbrain** structure — the
**metencephalic** part of the brainstem (from the
mesencephalic–metencephalic junction rostrally to the
**pontomedullary junction** — the **bulbopontine sulcus**
caudally). **They are DIFFERENT brainstem segments** —
**separated** by the **pontomedullary junction** (the
**bulbopontine sulcus**) — the **pons** is **rostral**; the
**medulla oblongata** is **caudal**. They are **continuous**
at the **pontomedullary junction**, but they are **distinct
segments**. Consumers must **not** conflate the pons with the
medulla oblongata.
**Boundary status (PONS — NOT the midbrain):** **Boundary
case — the pons is the METENCEPHALIC brainstem segment, NOT
the midbrain (the MESENCEPHALIC brainstem segment).** The
**midbrain** (``.../midbrain/``) is the **mesencephalic**
derivative — the **tectum** (superior and inferior
colliculi), the **tegmentum** (substantia nigra, red nucleus,
periaqueductal gray, ventral tegmental area), the **cerebral
peduncle**, and the **mesencephalic aqueduct**. The **pons**
(here) is the **metencephalic** brainstem segment. **They are
DIFFERENT brainstem segments** — **separated** by the
**mesencephalic–metencephalic junction** (the **caudal midbrain
/ rostral pons junction**) — the **midbrain** is **rostral**;
the **pons** is **caudal**. They are **continuous** at the
**mesencephalic–metencephalic junction**, but they are
**distinct segments**. Consumers must **not** conflate the pons
with the midbrain.
**Boundary status (PONS — NOT the brainstem as a whole):**
**Boundary case — the pons is the PONTINE SEGMENT of the
brainstem, NOT the whole brainstem.** The **brainstem** is the
**segmental neuraxis** — the **midbrain** (mesencephalon) +
the **pons** (metencephalon) + the **medulla oblongata**
(myelencephalon). The **pons** (here) is the **middle segment**
— the **pons** between the midbrain (rostral) and the medulla
oblongata (caudal). **The pons is a SEGMENT of the brainstem;
the brainstem is the WHOLE neuraxis.** Consumers must **not**
conflate the pons with the brainstem as a whole — the
**pons** is one of the three **segments** of the brainstem.
**Boundary status (PONS — NOT the basis pontis alone):**
**Boundary case — the pons is the WHOLE pontine region
(basis pontis + tegmentum + cerebellar peduncles), NOT the
basis pontis alone.** The **basis pontis** (ventral pons) is
the **ventral portion** of the pons — the **pontine nuclei**,
the **corticospinal** and **corticobulbar** tracts, and the
**transverse pontine fibers**. The **pons** (here) is the
**whole pontine region** — the **basis pontis** **plus** the
**pontine tegmentum** (dorsal pons) **plus** the **cerebellar
peduncles**. **The basis pontis is a PART of the pons; the
pons is the WHOLE region.** The **basis pontis** is documented
as **prose** in this module. Consumers must **not** conflate
the pons with the basis pontis alone.
**Boundary status (PONS — NOT the tegmentum alone):**
**Boundary case — the pons is the WHOLE pontine region (basis
pontis + tegmentum + cerebellar peduncles), NOT the tegmentum
alone.** The **pontine tegmentum** (``.../pons/tegmentum/``)
is the **dorsal portion** of the pons — the **cranial nerve
nuclei V–VIII**, the **pontine reticular formation**, the
**locus coeruleus**, the **parabrachial complex**, the
**pedunculopontine nucleus**, the **laterodorsal tegmental
nucleus**, the **superior olivary complex**, the **nucleus
incertus**, and the **pontine micturition center**. The
**pons** (here) is the **whole pontine region** — the
**basis pontis** **plus** the **pontine tegmentum** **plus**
the **cerebellar peduncles**. **The tegmentum is a PART of
the pons; the pons is the WHOLE region.** Consumers must
**not** conflate the pons with the tegmentum alone.
**Boundary status (PONS — NOT the pontine nuclei alone):**
**Boundary case — the pons is the WHOLE pontine region, NOT
the pontine nuclei alone.** The **pontine nuclei**
(``.../pons/pontine_nuclei/``) are the **grey-matter nuclei**
of the **basis pontis** — the **relay nuclei** for the
**corticopontocerebellar** pathway (the **cortico-ponto-
cerebellar** fibers that relay through the pontine nuclei to
the cerebellum). The **pons** (here) is the **whole pontine
region**. **The pontine nuclei are a PART of the pons; the
pons is the WHOLE region.** Consumers must **not** conflate
the pons with the pontine nuclei alone.
**Boundary status (PONS — NOT the cranial nerve nuclei alone):**
**Boundary case — the pons is the WHOLE pontine region, NOT
the cranial nerve nuclei (V–VIII) alone.** The **cranial
nerve nuclei** (``.../pons/cranial_nerve_nuclei/``) — the
**trigeminal (V)** (chief sensory + motor), **abducens (VI)**,
**facial (VII)**, **vestibulocochlear (VIII)** nuclei, and
the **superior salivatory nucleus** — are the **grey-matter
cranial nerve nuclei** of the pontine tegmentum. The **pons**
(here) is the **whole pontine region**. **The cranial nerve
nuclei are a PART of the pons; the pons is the WHOLE region.**
Consumers must **not** conflate the pons with the cranial
nerve nuclei alone.
**Boundary status (PONS — NOT the cerebellar peduncles alone):**
**Boundary case — the pons is the WHOLE pontine region, NOT
the cerebellar peduncles alone.** The **cerebellar peduncles**
(``.../pons/cerebellar_peduncles/``) — the **superior**,
**middle**, and **inferior cerebellar peduncles** — are the
**white-matter tracts** that **connect** the cerebellum to
the brainstem. They are **children of the pons** (the tree
wires the peduncles under the pons, not under the
cerebellum). The **pons** (here) is the **whole pontine
region** — the **basis pontis** **plus** the **pontine
tegmentum** **plus** the **cerebellar peduncles**. **The
cerebellar peduncles are a PART of the pons; the pons is the
WHOLE region.** Consumers must **not** conflate the pons with
the cerebellar peduncles alone.
**Boundary status (PONS — NOT the reticular formation alone):**
**Boundary case — the pons is the WHOLE pontine region, NOT
the pontine reticular formation alone.** The **pontine
reticular formation** — the **caudal pontine reticular
nucleus**, the **paramedian pontine reticular formation**,
the **parvocellular reticular nucleus**, and the **tegmental
pontine reticular nucleus** — is the **reticular formation**
of the pons (a component of the **pontine tegmentum**). The
**pons** (here) is the **whole pontine region**. **The
pontine reticular formation is a PART of the pons; the pons
is the WHOLE region.** Consumers must **not** conflate the
pons with the pontine reticular formation alone.
**Boundary status (PONS — NOT the parabrachial area or the
superior olivary complex alone):** **Boundary case — the pons
is the WHOLE pontine region, NOT the parabrachial area or the
superior olivary complex alone.** The **parabrachial area**
(``.../pons/parabrachial_area/``) — the **lateral
parabrachial nucleus**, **medial parabrachial nucleus**, and
**subparabrachial nucleus** (with the **Kölliker-Fuse
nucleus** and the **pontine respiratory group**) — is a
**pontine tegmentum component**. The **superior olivary
complex** (``.../pons/superior_olivary_complex/``) — the
**lateral superior olive**, **medial nucleus of trapezoid
body**, and **medial superior olive** — is a **pontine
tegmentum component** (auditory processing). The **pons**
(here) is the **whole pontine region**. **The parabrachial
area and the superior olivary complex are PARTS of the pons;
the pons is the WHOLE region.** Consumers must **not**
conflate the pons with either alone.
**Boundary status (PONS — NOT the locus coeruleus or the
tegmentum nuclei alone):** **Boundary case — the pons is the
WHOLE pontine region, NOT the locus coeruleus or the
tegmentum nuclei alone.** The **locus coeruleus**
(``.../pons/tegmentum/locus_coeruleus/``), the
**laterodorsal tegmental nucleus**
(``.../pons/tegmentum/laterodorsal_tegmental_nucleus/``),
the **pedunculopontine nucleus**
(``.../pons/tegmentum/pedunculopontine_nucleus/``), the
**nucleus incertus**
(``.../pons/tegmentum/nucleus_incertus/``), the **pontine
micturition center**
(``.../pons/tegmentum/pontine_micturition_center/``), and
the **tegmental pontine reticular nucleus**
(``.../pons/tegmentum/tegmental_pontine_reticular_nucleus/``)
are **pontine tegmentum nuclei**. The **pons** (here) is the
**whole pontine region**. **These tegmentum nuclei are
PARTS of the pons; the pons is the WHOLE region.** Consumers
must **not** conflate the pons with any one of these nuclei
alone.
**Boundary status (METENCEPHALIC — NOT the myelencephalic or
mesencephalic brainstem):** **Boundary case — the pons is the
METENCEPHALIC brainstem segment, NOT the myelencephalic
(medulla oblongata) or mesencephalic (midbrain) brainstem
segments.** The **pons** is the **metencephalic** derivative;
the **medulla oblongata** is the **myelencephalic**
derivative; the **midbrain** is the **mesencephalic**
derivative. **They are DIFFERENT brainstem segments in
DIFFERENT developmental compartments** — the **pons** is
**metencephalic**; the **medulla oblongata** is
**myelencephalic**; the **midbrain** is **mesencephalic**.
Consumers must **not** conflate the pons with the medulla
oblongata or the midbrain.
**Boundary status (PONS — NOT the diencephalon or the
telencephalon):** **Boundary case — the pons is a HINDBRAIN
(metencephalic) structure, NOT the diencephalon or the
telencephalon.** The **diencephalon**
(``.../forebrain/diencephalon/``) — the **thalamus**,
**hypothalamus**, **epithalamus**, **subthalamus**, and
**third ventricle** — is the **prosencephalic** sub-vesicle.
The **telencephalon**
(``.../forebrain/telencephalon/``) — the **cerebral
hemispheres**, **basal ganglia**, **hippocampus**,
**amygdala**, and **lateral ventricles** — is the
**prosencephalic** derivative. The **pons** (here) is the
**hindbrain (metencephalic)** structure. **They are DIFFERENT
structures in DIFFERENT brain vesicles** — the **pons** is
**hindbrain**; the **diencephalon** and **telencephalon**
are **forebrain**. Consumers must **not** conflate the pons
with the diencephalon or the telencephalon.
**Boundary status (PONS — NOT the spinal cord):** **Boundary
case — the pons is a BRAINSTEM structure, NOT the spinal
cord.** The **spinal cord** (``.../spinal_cord/``) is the
**caudal** continuation of the neuraxis — the **gray matter**
(dorsal, lateral, ventral horns) and **white matter**
(corticospinal tract, dorsal columns, spinothalamic tract).
The **pons** (here) is the **metencephalic brainstem**
structure — **rostral** to the medulla oblongata, which is
**rostral** to the spinal cord. **The pons is separated from
the spinal cord by the whole medulla oblongata.** Consumers
must **not** conflate the pons with the spinal cord.
**Boundary status (HETEROGENEOUS — MULTIPLE sub-regions with
DIFFERENT functions):** **Boundary case — the pons is a
HETEROGENEOUS brainstem segment with MULTIPLE sub-regions and
MULTIPLE functions, not a single uniform structure.** The pons
includes the **basis pontis** (pontine nuclei, corticospinal
and corticobulbar tracts, transverse pontine fibers), the
**pontine tegmentum** (cranial nerve nuclei V–VIII, pontine
reticular formation, locus coeruleus, parabrachial complex,
pedunculopontine nucleus, laterodorsal tegmental nucleus,
superior olivary complex, nucleus incertus, pontine
micturition center), and the **cerebellar peduncles**
(superior, middle, inferior). **Each sub-region is
functionally distinct** — the tree wires the **caudal
pontine reticular nucleus**, **cerebellar peduncles**,
**cranial nerve nuclei**, **parabrachial area**,
**paramedian pontine reticular formation**,
**parvocellular reticular nucleus**, **pontine nuclei**,
**superior olivary complex**, and **tegmentum** as
**sub-containers**, and the functional sub-regions are
documented as **children of those sub-containers** or as
**prose**. Consumers must **not** treat the pons as a single
uniform region — it is a **distributed brainstem segment**
with **heterogeneous sub-structures**.
**Boundary status (SLEA-FREE — the pons is NOT an
extended-amygdala component):** **Boundary case — the pons is
SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and
to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **pons** is a **brainstem
segment** — it is **NOT** an extended-amygdala component, and
it carries **NO SLEA warning**. Consumers must **not** import
the SLEA warning into the pons — it is **SLEA-free**.
**Boundary status (NOT a single neural processor — the pons is
a SEGMENT, not a single processor):** **Boundary case — the
pons is a SEGMENT, not a single neural processor.** It
**contains** neural processors (the **pontine nuclei**, the
**cranial nerve nuclei V–VIII**, the **pontine reticular
formation**, the **locus coeruleus**, the **parabrachial
complex**, the **superior olivary complex**, the
**pedunculopontine nucleus**, the **laterodorsal tegmental
nucleus**, the **nucleus incertus**, the **pontine
micturition center**, and the **tegmental pontine reticular
nucleus**) — but it is **not itself a processor**. The
**processing** happens in the **sub-structures** of the
pons. Consumers must **not** treat the pons as a **single
neural processor** — it is a **brainstem segment** with
**heterogeneous sub-structures**, each with its own function.

Overview
--------
The pons is the **rostral brainstem segment** of the
**metencephalon** — the **ventral brainstem structure** between
the **midbrain** (rostral) and the **medulla oblongata**
(caudal), comprising the **basis pontis** (ventral pons —
pontine nuclei, corticospinal and corticobulbar tracts,
transverse pontine fibers), the **pontine tegmentum** (dorsal
pons — cranial nerve nuclei V–VIII, pontine reticular
formation, locus coeruleus, parabrachial complex,
pedunculopontine nucleus, laterodorsal tegmental nucleus,
superior olivary complex, nucleus incertus, pontine micturition
center, tegmental pontine reticular nucleus), and the
**cerebellar peduncles** (superior, middle, and inferior —
the white-matter tracts connecting the cerebellum to the
brainstem). It is a **container module** with **eleven
structural sub-containers**.

**The pons is the VENTRAL BRAINSTEM structure, distinct from the
cerebellum (dorsal suprasegmental) and the fourth ventricle
(CSF cavity).** The **cerebellum** is the **dorsal
suprasegmental** structure; the **fourth ventricle** is the
**CSF cavity** between the pons/medulla and the cerebellum;
the **pons** (here) is the **ventral brainstem** structure
that forms the **ventral wall** of the fourth ventricle.

**The pons is ROSTRAL to the medulla oblongata and CAUDAL to the
midbrain.** The **midbrain** (``.../midbrain/``) is
**rostral**; the **medulla oblongata**
(``.../hindbrain/myelencephalon/medulla_oblongata/``) is
**caudal**. They are **different brainstem segments** —
**separated** by the **mesencephalic–metencephalic junction**
(rostral) and the **pontomedullary junction** (caudal), but
**continuous** with the pons at those junctions.

**The pons is a HETEROGENEOUS brainstem segment, not a single
structure.** It includes the **basis pontis** (ventral —
pontine nuclei, corticospinal and corticobulbar tracts,
transverse pontine fibers — the **cortico-ponto-cerebellar
relay**), the **pontine tegmentum** (dorsal — cranial nerve
nuclei V–VIII, pontine reticular formation, locus coeruleus,
parabrachial complex, pedunculopontine nucleus,
laterodorsal tegmental nucleus, superior olivary complex,
nucleus incertus, pontine micturition center, tegmental
pontine reticular nucleus), and the **cerebellar peduncles**
(superior, middle, and inferior — the **cerebellar
connections**). Each sub-region is functionally distinct.

**The pons is a SEGMENT, not a single neural processor.** The
**processing** happens in the **sub-structures** of the pons.
The **pons** is the **brainstem segment** that **contains**
those sub-structures.

Pons Composition (sub-containers and prose)
-------------------------------------------
The pons is a **brainstem segment** with **eleven sub-containers**
— documented as **structural children** — and **many
prose-defined sub-structures** documented within those
sub-containers:

*   **Caudal pontine reticular nucleus**
    (``.../pons/caudal_pontine_reticular_nucleus/``) — the
    **caudal pontine reticular nucleus** — a component of the
    **pontine reticular formation** (the **reticular
    formation** of the **caudal pons**). Documented as a
    **structural child**.

*   **Cerebellar peduncles**
    (``.../pons/cerebellar_peduncles/``) — the **superior**,
    **middle**, and **inferior cerebellar peduncles** — the
    **white-matter tracts** connecting the cerebellum to the
    brainstem. Documented as a **structural child** with
    three sub-containers
    (``inferior_cerebellar_peduncle/``,
    ``middle_cerebellar_peduncle/``,
    ``superior_cerebellar_peduncle/``).

*   **Cranial nerve nuclei**
    (``.../pons/cranial_nerve_nuclei/``) — the **cranial
    nerve nuclei V–VIII** of the **pons** — the **trigeminal
    (V)** (chief sensory + motor), **abducens (VI)**,
    **facial (VII)**, **vestibulocochlear (VIII)** nuclei,
    and the **superior salivatory nucleus** — with **left**
    and **right** sub-containers (each with six leaf
    nuclei), and the **vestibulocochlear_nuclei/`** sub-
    container with **left** and **right** sub-containers,
    each with ``cochlear_nuclei/`` and ``vestibular_nuclei/``
    sub-containers. Documented as a **structural child**.

*   **Parabrachial area**
    (``.../pons/parabrachial_area/``) — the **lateral
    parabrachial nucleus**, **medial parabrachial nucleus**,
    and **subparabrachial nucleus** (with the **Kölliker-Fuse
    nucleus** and the **pontine respiratory group**) — the
    **parabrachial complex** (autonomic and respiratory
    relay). Documented as a **structural child**.

*   **Paramedian pontine reticular formation**
    (``.../pons/paramedian_pontine_reticular_formation/``) —
    the **paramedian pontine reticular formation** (PPRF) — a
    component of the **pontine reticular formation** (the
    **horizontal gaze center** — the **PPRF**). Documented as
    a **structural child**.

*   **Parvocellular reticular nucleus**
    (``.../pons/parvocellular_reticular_nucleus/``) — the
    **parvocellular reticular nucleus** — a component of the
    **pontine reticular formation**. Documented as a
    **structural child**.

*   **Pontine nuclei**
    (``.../pons/pontine_nuclei/``) — the **pontine nuclei**
    — the **grey-matter relay nuclei** of the **basis
    pontis** (the **cortico-ponto-cerebellar** relay) — with
    **left** and **right** sub-containers. Documented as a
    **structural child**.

*   **Superior olivary complex**
    (``.../pons/superior_olivary_complex/``) — the
    **lateral superior olive**, **medial nucleus of
    trapezoid body**, and **medial superior olive** — the
    **superior olivary complex** (auditory processing — the
    **sound localization** circuit) — with **left** and
    **right** sub-containers for the **lateral** and
    **medial superior olives**. Documented as a **structural
    child**.

*   **Tegmentum** (``.../pons/tegmentum/``) — the **pontine
    tegmentum** (the **dorsal pons**) — with six sub-containers:
    ``laterodorsal_tegmental_nucleus/``,
    ``locus_coeruleus/``, ``nucleus_incertus/``,
    ``pedunculopontine_nucleus/``,
    ``pontine_micturition_center/``, and
    ``tegmental_pontine_reticular_nucleus/``. Documented as a
    **structural child**.

**These sub-structures are children of the sub-containers (or
prose), not direct structural children of the pons.** The tree
wires the **pons** as a **container** with **eleven
sub-containers** — the **basis pontis** (ventral pons), the
**transverse pontine fibers**, the **corticospinal** and
**corticobulbar** tracts within the pons, the **pontine
tegmentum** (as a general region), the **medial longitudinal
fasciculus** (MLF) within the pons, the **medial lemniscus**
within the pons, the **spinal trigeminal tract** within the
pons, and the **mesencephalic trigeminal tract** within the
pons are documented as **prose**, not structural children.
Consumers that need **nucleus-level** or **tract-level**
resolution should consult the **sub-container modules** and
the references, not the pons container.

The Pons / Metencephalon Boundary
---------------------------------
This is the **child-vs-container** boundary:

*   **Pons** (this module) — a **child sub-container of the
    metencephalon**.

*   **Metencephalon** (``.../metencephalon/``) — the
    **container** (pons + cerebellum + fourth ventricle).

**The pons is a PART of the metencephalon; the metencephalon is
the WHOLE.** Consumers must **not** conflate the pons with the
metencephalon container.

The Pons / Cerebellum Boundary
------------------------------
This is the **ventral-brainstem-vs-dorsal-suprasegmental**
boundary:

*   **Pons** (this module) — the **ventral brainstem**
    structure.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the
    **dorsal suprasegmental** structure.

**The pons is the VENTRAL BRAINSTEM; the cerebellum is the DORSAL
SUPRASEGMENTAL structure.** They are **connected** via the
**cerebellar peduncles** (children of the pons), but they are
**distinct structures**. Consumers must **not** conflate the
pons with the cerebellum.

The Pons / Fourth Ventricle Boundary
------------------------------------
This is the **ventral-brainstem-vs-CSF-cavity** boundary:

*   **Pons** (this module) — the **ventral brainstem**
    structure.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The pons is the VENTRAL WALL of the fourth ventricle; the
fourth ventricle is the CSF CAVITY between the pons/medulla and
the cerebellum.** Consumers must **not** conflate the pons with
the fourth ventricle.

The Pons / Medulla Oblongata Boundary
-------------------------------------
This is the **rostral-vs-caudal** boundary:

*   **Pons** (this module) — the **rostral** brainstem segment
    (metencephalic).

*   **Medulla oblongata**
    (``.../hindbrain/myelencephalon/medulla_oblongata/``) —
    the **caudal** brainstem segment (myelencephalic).

**They are DIFFERENT brainstem segments** — **separated** by the
**pontomedullary junction** (the **bulbopontine sulcus**) — the
**pons** is **rostral**; the **medulla oblongata** is
**caudal**. They are **continuous** at the **pontomedullary
junction**, but they are **distinct segments**. Consumers must
**not** conflate the pons with the medulla oblongata.

The Pons / Midbrain Boundary
----------------------------
This is the **caudal-vs-rostral** boundary:

*   **Pons** (this module) — the **caudal** brainstem segment
    (metencephalic).

*   **Midbrain** (``.../midbrain/``) — the **rostral**
    brainstem segment (mesencephalic).

**They are DIFFERENT brainstem segments** — **separated** by the
**mesencephalic–metencephalic junction** — the **midbrain** is
**rostral**; the **pons** is **caudal**. They are **continuous**
at the **mesencephalic–metencephalic junction**, but they are
**distinct segments**. Consumers must **not** conflate the pons
with the midbrain.

The Pons / Brainstem Boundary
-----------------------------
This is the **segment-vs-whole-neuraxis** boundary:

*   **Pons** (this module) — the **pontine segment** of the
    brainstem.

*   **Brainstem** (midbrain + pons + medulla oblongata) — the
    **segmental neuraxis**.

**The pons is a SEGMENT of the brainstem; the brainstem is the
WHOLE neuraxis.** Consumers must **not** conflate the pons with
the brainstem as a whole — the **pons** is one of the three
**segments** of the brainstem.

The Pons / Basis Pontis Boundary
--------------------------------
This is the **whole-vs-ventral-portion** boundary:

*   **Pons** (this module) — the **whole pontine region**
    (basis pontis + tegmentum + cerebellar peduncles).

*   **Basis pontis** — the **ventral portion** of the pons
    (pontine nuclei, corticospinal and corticobulbar tracts,
    transverse pontine fibers — prose).

**The basis pontis is a PART of the pons; the pons is the WHOLE
region.** Consumers must **not** conflate the pons with the
basis pontis alone.

The Pons / Pontine Tegmentum Boundary
-------------------------------------
This is the **whole-vs-dorsal-portion** boundary:

*   **Pons** (this module) — the **whole pontine region**
    (basis pontis + tegmentum + cerebellar peduncles).

*   **Pontine tegmentum** (``.../pons/tegmentum/``) — the
    **dorsal portion** of the pons (cranial nerve nuclei
    V–VIII, pontine reticular formation, locus coeruleus,
    parabrachial complex, pedunculopontine nucleus,
    laterodorsal tegmental nucleus, superior olivary complex,
    nucleus incertus, pontine micturition center, tegmental
    pontine reticular nucleus).

**The tegmentum is a PART of the pons; the pons is the WHOLE
region.** Consumers must **not** conflate the pons with the
tegmentum alone.

The Pons / Pontine Nuclei Boundary
----------------------------------
This is the **whole-vs-grey-matter-relay-nuclei** boundary:

*   **Pons** (this module) — the **whole pontine region**.

*   **Pontine nuclei** (``.../pons/pontine_nuclei/``) — the
    **grey-matter relay nuclei** of the basis pontis (the
    cortico-ponto-cerebellar relay).

**The pontine nuclei are a PART of the pons; the pons is the
WHOLE region.** Consumers must **not** conflate the pons with
the pontine nuclei alone.

The Pons / Cranial Nerve Nuclei Boundary
----------------------------------------
This is the **whole-vs-cranial-nerve-nuclei** boundary:

*   **Pons** (this module) — the **whole pontine region**.

*   **Cranial nerve nuclei** (``.../pons/cranial_nerve_
    nuclei/``) — the **cranial nerve nuclei V–VIII** of the
    pontine tegmentum (trigeminal, abducens, facial,
    vestibulocochlear, superior salivatory).

**The cranial nerve nuclei are a PART of the pons; the pons is
the WHOLE region.** Consumers must **not** conflate the pons
with the cranial nerve nuclei alone.

The Pons / Cerebellar Peduncles Boundary
----------------------------------------
This is the **whole-vs-white-matter-tracts** boundary:

*   **Pons** (this module) — the **whole pontine region**.

*   **Cerebellar peduncles**
    (``.../pons/cerebellar_peduncles/``) — the **superior**,
    **middle**, and **inferior cerebellar peduncles** — the
    **white-matter tracts** connecting the cerebellum to the
    brainstem.

**The cerebellar peduncles are a PART of the pons; the pons is
the WHOLE region.** Consumers must **not** conflate the pons
with the cerebellar peduncles alone.

The Pons / Pontine Reticular Formation Boundary
-----------------------------------------------
This is the **whole-vs-reticular-formation** boundary:

*   **Pons** (this module) — the **whole pontine region**.

*   **Pontine reticular formation** — the **caudal pontine
    reticular nucleus**, the **paramedian pontine reticular
    formation**, the **parvocellular reticular nucleus**, and
    the **tegmental pontine reticular nucleus** (prose or
    children of the sub-containers).

**The pontine reticular formation is a PART of the pons; the pons
is the WHOLE region.** Consumers must **not** conflate the pons
with the pontine reticular formation alone.

The Pons / Parabrachial Area Boundary
-------------------------------------
This is the **whole-vs-parabrachial-complex** boundary:

*   **Pons** (this module) — the **whole pontine region**.

*   **Parabrachial area** (``.../pons/parabrachial_area/``) —
    the **lateral parabrachial nucleus**, **medial
    parabrachial nucleus**, and **subparabrachial nucleus**
    (with the **Kölliker-Fuse nucleus** and the **pontine
    respiratory group**) — the **parabrachial complex**.

**The parabrachial area is a PART of the pons; the pons is the
WHOLE region.** Consumers must **not** conflate the pons with
the parabrachial area alone.

The Pons / Superior Olivary Complex Boundary
--------------------------------------------
This is the **whole-vs-auditory-processing-complex** boundary:

*   **Pons** (this module) — the **whole pontine region**.

*   **Superior olivary complex**
    (``.../pons/superior_olivary_complex/``) — the **lateral
    superior olive**, **medial nucleus of trapezoid body**,
    and **medial superior olive** — the **superior olivary
    complex** (auditory processing — sound localization).

**The superior olivary complex is a PART of the pons; the pons is
the WHOLE region.** Consumers must **not** conflate the pons
with the superior olivary complex alone.

The Pons / Locus Coeruleus and Tegmentum Nuclei Boundary
--------------------------------------------------------
This is the **whole-vs-tegmentum-nuclei** boundary:

*   **Pons** (this module) — the **whole pontine region**.

*   **Locus coeruleus**
    (``.../pons/tegmentum/locus_coeruleus/``), the
    **laterodorsal tegmental nucleus**, the
    **pedunculopontine nucleus**, the **nucleus incertus**,
    the **pontine micturition center**, and the **tegmental
    pontine reticular nucleus** — the **pontine tegmentum
    nuclei**.

**These tegmentum nuclei are PARTS of the pons; the pons is the
WHOLE region.** Consumers must **not** conflate the pons with
any one of these nuclei alone.

The Pons / Diencephalon and Telencephalon Boundary
--------------------------------------------------
This is the **hindbrain-vs-forebrain** boundary:

*   **Pons** (this module) — the **hindbrain (metencephalic)**
    structure.

*   **Diencephalon** (``.../forebrain/diencephalon/``) and
    **telencephalon** (``.../forebrain/telencephalon/``) —
    the **forebrain (prosencephalic)** structures.

**They are DIFFERENT structures in DIFFERENT brain vesicles** —
the **pons** is **hindbrain**; the **diencephalon** and
**telencephalon** are **forebrain**. Consumers must **not**
conflate the pons with the diencephalon or the telencephalon.

The Pons / Spinal Cord Boundary
-------------------------------
This is the **brainstem-vs-spinal-cord** boundary:

*   **Pons** (this module) — the **metencephalic brainstem**
    structure.

*   **Spinal cord** (``.../spinal_cord/``) — the **caudal**
    continuation of the neuraxis.

**The pons is separated from the spinal cord by the whole medulla
oblongata.** Consumers must **not** conflate the pons with the
spinal cord.

The Pons / SLEA Boundary
------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Pons** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**,
    **ventral pallidum**, and **nucleus accumbens** (wired
    elsewhere).

**The pons is NOT part of the SLEA continuum.** It is a
**brainstem segment**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the pons.

Function in the Human Brain
---------------------------
The pons's functions are **heterogeneous** — documented at the
**sub-structure** level, not at the segment level:

*   **Cortico-Ponto-Cerebellar Relay (Basis Pontis, Pontine
    Nuclei):** The **basis pontis** contains the **pontine
    nuclei** and the **transverse pontine fibers** that
    **relay** the **corticopontine** fibers from the
    **cerebral cortex** to the **contralateral cerebellar
    cortex** (via the **middle cerebellar peduncle**) — the
    **cortico-ponto-cerebellar** pathway, the **largest
    cerebro-cerebellar pathway**. The **pons** is the
    **major relay station** in the **cortico-cerebellar
    communication** system.

*   **Corticospinal and Corticobulbar Conduction (Basis
    Pontis):** The **basis pontis** contains the
    **corticospinal** and **corticobulbar** tracts — the
    **descending motor pathways** from the **cerebral
    cortex** to the **spinal cord** (corticospinal) and the
    **cranial nerve nuclei** (corticobulbar) — that
    **traverse** the pons. The **pons** is a **key
    conduit** in the **descending motor system**.

*   **Cranial Nerve Nuclei Functions (Cranial Nerve Nuclei
    V–VIII):** The **pons** contains the **cranial nerve
    nuclei V (trigeminal), VI (abducens), VII (facial), and
    VIII (vestibulocochlear)** — the **brainstem control
    centers** for **facial sensation** (V), **eye movement**
    (VI), **facial expression**, **taste** (VII), and
    **hearing**, **balance** (VIII). The **superior
    salivatory nucleus** (VII) is the **parasympathetic
    control** for **lacrimal** and **salivary** secretion.

*   **Respiratory Control (Pontine Respiratory Group,
    Parabrachial Area):** The **pontine respiratory group**
    (the **pneumotaxic center** and the **apneustic
    center** — within the **subparabrachial nucleus** /
    **Kölliker-Fuse nucleus**) — is the **pontine
    respiratory center** that **modulates** the
    **respiratory rhythm** generated in the **medulla** (the
    **pre-Bötzinger complex**).

*   **Auditory Processing and Sound Localization (Superior
    Olivary Complex):** The **superior olivary complex** —
    the **lateral superior olive**, the **medial nucleus of
    trapezoid body**, and the **medial superior olive** — is
    the **brainstem auditory processing center** that
    **processes** **sound localization** (interaural time
    and intensity differences) and **auditory timing**.

*   **Arousal and Sleep-Wake (Locus Coeruleus,
    Pedunculopontine Nucleus, Laterodorsal Tegmental
    Nucleus):** The **locus coeruleus** (noradrenergic), the
    **pedunculopontine nucleus** and the **laterodorsal
    tegmental nucleus** (cholinergic) — the **pontine
    arousal and sleep-wake centers** — **modulate**
    **wakefulness**, **REM sleep**, and **arousal**.

*   **Autonomic Relay (Parabrachial Area, Nucleus
    Incertus):** The **parabrachial complex** (lateral,
    medial, subparabrachial nuclei) — the **autonomic and
    respiratory relay** from the **nucleus tractus
    solitarius** to the **forebrain** (hypothalamus,
    amygdala, insula). The **nucleus incertus** — a
    **pontine tegmentum nucleus** involved in **stress**,
    **anxiety**, and **feeding**.

*   **Micturition Control (Pontine Micturition Center):** The
    **pontine micturition center** (Barrington's nucleus) —
    the **pontine tegmentum nucleus** that **controls**
    **micturition** (bladder contraction).

*   **Horizontal Gaze (Paramedian Pontine Reticular
    Formation):** The **paramedian pontine reticular
    formation** (PPRF) — the **pontine reticular
    formation** component that is the **horizontal gaze
    center** — the **supranuclear control** of **horizontal
    saccades** (via the **abducens nucleus**).

*   **Reticular Formation Functions (Pontine Reticular
    Formation):** The **caudal pontine reticular nucleus**,
    the **parvocellular reticular nucleus**, and the
    **tegmental pontine reticular nucleus** — the **pontine
    reticular formation** — contribute to **arousal**,
    **sleep-wake**, **autonomic reflexes**, and the
    **descending pain modulation system**.

*   **NOT a single neural processor.** The pons is a
    **brainstem segment** — the **processing** happens in
    the **sub-structures** of the pons (pontine nuclei,
    cranial nerve nuclei, reticular formation, etc.).
    Consumers must **not** treat the pons as a **single
    processor** — it is a **segment** with **heterogeneous
    sub-structures**, each with its own function.

**The unifying theme:** the pons is the **metencephalic
brainstem segment** — the **ventral brainstem structure**
between the midbrain (rostral) and the medulla oblongata
(caudal) — that **contains** the **basis pontis**
(cortico-ponto-cerebellar relay, corticospinal and
corticobulbar conduction), the **pontine tegmentum**
(cranial nerve nuclei V–VIII, pontine reticular formation,
locus coeruleus, parabrachial complex, pedunculopontine
nucleus, laterodorsal tegmental nucleus, superior olivary
complex, nucleus incertus, pontine micturition center), and
the **cerebellar peduncles** (superior, middle, inferior —
the cerebellar connections). It is a **heterogeneous
brainstem segment**, **NOT a single neural processor**, and
**NOT the metencephalon, cerebellum, fourth ventricle,
medulla oblongata, midbrain, brainstem as a whole, basis
pontis, tegmentum, pontine nuclei, cranial nerve nuclei,
cerebellar peduncles, reticular formation, parabrachial
area, superior olivary complex, locus coeruleus, or any
single sub-structure alone**.

Associated Disorders
--------------------
The pons has **named clinical syndromes** — its clinical
associations are **heterogeneous**, via the **sub-structures**
it contains:

*   **Pontine Stroke (Basis Pontis, Tegmentum):** **Pontine
    infarcts** — **ischemic** (paramedian pontine, lateral
    pontine, and other pontine syndromes) and **hemorrhagic**
    (pontine hemorrhage) — cause **cranial nerve deficits**
    (VI, VII, V), **long tract signs** (hemiparesis,
    hemisensory loss), **autonomic dysfunction**, and
    **disorders of consciousness**. The **pons** is the
    **region**; the **basis pontis** and the **pontine
    tegmentum** are the **substrates**.

*   **Locked-In Syndrome (Ventral Pontine Infarction):**
    **Ventral pontine infarction** — **quadriplegia** with
    **preserved consciousness** and **vertical eye
    movements**. The **basis pontis** (the **corticospinal**
    and **corticobulbar** tracts within it) is the
    **substrate**.

*   **Central Pontine Myelinolysis (Osmotic Demyelination
    Syndrome):** **Demyelination** of the **basis pontis** —
    typically after **rapid correction of hyponatremia** —
    causing **quadriparesis**, **pseudobulbar palsy**, and
    **locked-in syndrome**. The **basis pontis** is the
    **substrate**.

*   **Pontine Glioma (Diffuse Midline Glioma — DIPG):** A
    **pediatric brainstem tumor** arising in the **pons** —
    the **basis pontis** and the **pontine tegmentum** are
    the **substrates**.

*   **Cranial Nerve Nuclei Syndromes (Cranial Nerve Nuclei
    V–VIII):** **Trigeminal neuralgia** (V), **abducens
    palsy** (VI), **facial palsy** (VII — the **facial
    nerve**), **vestibulocochlear syndromes** (VIII —
    **vestibular schwannoma** / **acoustic neuroma**), and
    **superior salivatory nucleus** syndromes (VII —
    **lacrimal** and **salivary** dysfunction). The **pons**
    is the **region**; the **cranial nerve nuclei** are the
    **substrates**.

*   **Locus Coeruleus Dysfunction (Pons):** **Arousal**,
    **attention**, and **stress-response** dysfunction — the
    **locus coeruleus** (the **major noradrenergic nucleus**)
    is implicated in **PTSD**, **depression**, **anxiety**,
    and **Alzheimer's disease** (early locus coeruleus tau
    pathology). The **pons** is the **region**; the **locus
    coeruleus** is the **substrate**.

*   **Central Pontine Myelinolysis (Basis Pontis):** **Osmotic
    demyelination syndrome** — see above. The **basis
    pontis** is the **substrate**.

*   **Respiratory Center Dysfunction (Pontine Respiratory
    Group, Parabrachial Area):** **Dysfunction** of the
    **pontine respiratory group** — **sleep-disordered
    breathing** (some forms), **central sleep apnea**
    (pontine respiratory group dysfunction). The **pons** is
    the **region**; the **pontine respiratory group** (within
    the **parabrachial area**) is the **substrate**.

*   **Superior Olivary Complex Dysfunction (Pons):**
    **Auditory processing deficits** — **sound localization**
    deficits, **auditory neuropathy spectrum disorder** (some
    forms), and **age-related hearing loss** (central
    component). The **pons** is the **region**; the
    **superior olivary complex** is the **substrate**.

*   **Parabrachial Area Dysfunction (Pons):** **Autonomic
    dysfunction** — **respiratory** and **cardiovascular**
    autonomic reflexes, **feeding** and **stress**
    (nucleus incertus), and **taste** (parabrachial relay).
    The **pons** is the **region**; the **parabrachial area**
    is the **substrate**.

*   **Pontine Micturition Center Dysfunction (Pons):**
    **Micturition** dysfunction — **urinary retention** (in
    **pontine lesions**) and **urinary incontinence**. The
    **pons** is the **region**; the **pontine micturition
    center** is the **substrate**.

*   **No Named "Pons Syndrome" (singular):** The pons has
    **multiple named clinical syndromes** (pontine stroke,
    locked-in syndrome, central pontine myelinolysis,
    pontine glioma, cranial nerve nuclei syndromes, locus
    coeruleus dysfunction, respiratory center dysfunction,
    superior olivary complex dysfunction, parabrachial area
    dysfunction, pontine micturition center dysfunction) —
    but **no single "pons syndrome."** Its clinical
    relevance is **heterogeneous**, via the **sub-structures**
    it contains.

**What is NOT here:** The pons is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala), **fear conditioning**
(central nucleus + basolateral nuclei), **Urbach-Wiethe
disease** (amygdala), or **Parkinson's disease** (substantia
nigra, in the midbrain). Its clinical relevance is
**heterogeneous**, via the **basis pontis**, **pontine
tegmentum**, and **cerebellar peduncles**. **No named pons
syndrome exists.**

Lateralization Notes
--------------------
This is the **pons** container module. The pons is a
**midline-spanning brainstem segment** with **bilateral
sub-structures** — and it carries **NO warning**:

*   **Bilateral Sub-Structures:** The **cranial nerve nuclei**
    (V–VIII) have **left and right** sub-containers; the
    **pontine nuclei** have **left and right** sub-containers;
    the **superior olivary complex** (the **lateral superior
    olive** and the **medial superior olive**) has **left
    and right** sub-containers. The **pons** is **not a
    paired structure** in the way the **lateral ventricles**
    or the **amygdala** are — it is a **midline segment** with
    **bilateral sub-structures**.

*   **Contralateral Connectivity (Corticospinal and
    Corticobulbar, Cortico-Ponto-Cerebellar):** The
    **corticospinal** and **corticobulbar** tracts within
    the **basis pontis** are **contralateral** to their
    cortical origins (after the **pyramidal decussation** for
    corticospinal; after the **cranial nerve nuclei** for
    corticobulbar). The **cortico-ponto-cerebellar** pathway
    (via the **pontine nuclei** and the **transverse pontine
    fibers**) **crosses** the midline to the
    **contralateral cerebellar hemisphere**.

*   **Partial Lateralization (Contested — Some Cranial Nerve
    Functions):** Some **cranial nerve functions** are
    **partially lateralized** — e.g., **language-related**
    auditory processing (the **superior olivary complex** and
    the auditory pathways have some lateralization);
    **vestibular** and **cochlear** processing have some
    lateralization. This is **partial**, **contested**, and
    documented in the **sub-container modules**.

*   **NO Extended-Amygdala Warning (SLEA-free):** The pons is
    **NOT** an extended-amygdala component. It carries **no
    SLEA warning**. Consumers must **not** import the SLEA
    warning into the pons.

*   **NO Amygdala-Lateralization Warning:** The pons is
    **NOT** the fear-output or the fear-learning structure.
    It is a **brainstem segment** — consumers must **not**
    conflate it with the **amygdala** or the **fear circuit**.

**A consumer that assumes "left pons = right pons" will be
structurally correct for the bilateral sub-structures** — the
pons is a **midline segment** with **bilateral sub-structures**.
The pons carries **NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-region imports.** The **container** does **not**
    import from ``.../metencephalon/`` (parent),
    ``.../metencephalon/cerebellum/`` (sibling),
    ``.../metencephalon/fourth_ventricle/`` (sibling),
    ``.../hindbrain/myelencephalon/`` (caudal neighbor),
    ``.../midbrain/`` (rostral neighbor),
    ``.../forebrain/``, ``.../spinal_cord/``, or any of its
    own sub-containers — it is a **namespace container**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../forebrain/telencephalon/``,
    ``.../forebrain/diencephalon/``, ``.../midbrain/``,
    ``.../spinal_cord/``, or any other container. The pons's
    relationships to the metencephalon, cerebellum, fourth
    ventricle, medulla oblongata, midbrain, brainstem,
    basis pontis, tegmentum, pontine nuclei, cranial nerve
    nuclei, cerebellar peduncles, reticular formation,
    parabrachial area, superior olivary complex, locus
    coeruleus, and the various tegmentum nuclei are
    documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — eleven structural children.** The
    ``caudal_pontine_reticular_nucleus/``,
    ``cerebellar_peduncles/``, ``cranial_nerve_nuclei/``,
    ``parabrachial_area/``,
    ``paramedian_pontine_reticular_formation/``,
    ``parvocellular_reticular_nucleus/``,
    ``pontine_nuclei/``, ``superior_olivary_complex/``, and
    ``tegmentum/`` are **sub-containers** (with the
    ``cerebellar_peduncles/``, ``cranial_nerve_nuclei/``,
    ``parabrachial_area/``, ``pontine_nuclei/``,
    ``superior_olivary_complex/``, and ``tegmentum/`` having
    their own **sub-containers** and **left/right**
    sub-containers where appropriate). The **basis pontis**,
    the **transverse pontine fibers**, the **corticospinal**
    and **corticobulbar** tracts within the pons, the
    **pontine tegmentum** (as a general region), the **medial
    longitudinal fasciculus** (MLF), the **medial lemniscus**,
    the **spinal trigeminal tract**, and the **mesencephalic
    trigeminal tract** are **prose**. Consumers must not
    assume any exist as direct children of the pons beyond
    the eleven sub-containers; resolve sub-structure-level
    detail through the sub-containers and the references.
*   **BRAINSTEM SEGMENT — NOT the whole brainstem or the
    metencephalon.** The **pons** is a **segment** of the
    brainstem (between the midbrain and the medulla
    oblongata) and a **child** of the metencephalon.
*   **VENTRAL BRAINSTEM — NOT the cerebellum or the fourth
    ventricle.** The **cerebellum** is **dorsal
    suprasegmental**; the **fourth ventricle** is the **CSF
    cavity**; the **pons** is the **ventral brainstem**.
*   **ROSTRAL TO THE MEDULLA OBLONGATA — CAUDAL TO THE
    MIDBRAIN.** They are **different brainstem segments**
    separated by the **pontomedullary junction** and the
    **mesencephalic–metencephalic junction**.
*   **HETEROGENEOUS SEGMENT — MULTIPLE sub-regions.** The
    **basis pontis**, the **pontine tegmentum**, and the
    **cerebellar peduncles** are functionally distinct.
*   **NOT the basis pontis, tegmentum, pontine nuclei,
    cranial nerve nuclei, cerebellar peduncles, reticular
    formation, parabrachial area, superior olivary complex,
    locus coeruleus, or any single tegmentum nucleus alone.**
    Those are **sub-structures** of the pons.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **NOT a single neural processor — the pons is a SEGMENT.**
    The **processing** happens in the **sub-structures**
    (pontine nuclei, cranial nerve nuclei, reticular
    formation, etc.).
*   **No ``AREA_PATHS`` hop.** The pons is a **local
    container** under the metencephalon, not a
    **cross-listed container**.
*   **No nested cross-listing.** The pons has **no nested
    dual-framing module**. It is a **single container** with
    eleven sub-containers.
*   **No lateralization warning.** The pons carries **no
    warning** — **no SLEA warning**, **no
    amygdala-lateralization warning**, and **no
    rhinencephalon-exclusion flag**. The **bilateral
    sub-structures** and the **contralateral connectivity**
    are documented as **prose**, not as a **warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons import (
        caudal_pontine_reticular_nucleus,
        cerebellar_peduncles,
        cranial_nerve_nuclei,
        parabrachial_area,
        paramedian_pontine_reticular_formation,
        parvocellular_reticular_nucleus,
        pontine_nuclei,
        superior_olivary_complex,
        tegmentum,
    )

Or by fully-qualified path string::

    path = "hindbrain.metencephalon.pons"
    tegmentum_path = "hindbrain.metencephalon.pons.tegmentum"
    locus_coeruleus_path = (
        "hindbrain.metencephalon.pons.tegmentum.locus_coeruleus"
    )
    cranial_nerve_nuclei_path = (
        "hindbrain.metencephalon.pons.cranial_nerve_nuclei"
    )

**Do not** assume the pons is the **metencephalon**. The
**metencephalon** is the **container** (pons + cerebellum +
fourth ventricle); the **pons** is a **child**.

**Do not** assume the pons is the **cerebellum** or the
**fourth ventricle**. The **cerebellum** is **dorsal
suprasegmental**; the **fourth ventricle** is the **CSF
cavity**; the **pons** is the **ventral brainstem**.

**Do not** assume the pons is the **medulla oblongata** or the
**midbrain**. The **midbrain** is **rostral**; the **medulla
oblongata** is **caudal**; the **pons** is the **middle**
brainstem segment.

**Do not** assume the pons is the **brainstem as a whole**. The
**pons** is a **segment** of the brainstem.

**Do not** assume the pons is the **basis pontis**, the
**tegmentum**, the **pontine nuclei**, the **cranial nerve
nuclei**, the **cerebellar peduncles**, the **pontine
reticular formation**, the **parabrachial area**, the
**superior olivary complex**, the **locus coeruleus**, or any
single tegmentum nucleus alone. Those are **sub-structures**
of the pons.

**Do not** assume the pons is the **diencephalon**,
**telencephalon**, or **spinal cord**. The **pons** is
**hindbrain (metencephalic)**; the **diencephalon** and
**telencephalon** are **forebrain**; the **spinal cord** is
**caudal to the whole hindbrain**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the pons. **The pons
is SLEA-FREE** — it is **not** an extended-amygdala component,
and it is **NOT the fear-output structure**.

Iterating the pons's children (recommended consumer pattern)::

    PONS_CHILDREN = (
        "caudal_pontine_reticular_nucleus",
        "cerebellar_peduncles",
        "cranial_nerve_nuclei",
        "parabrachial_area",
        "paramedian_pontine_reticular_formation",
        "parvocellular_reticular_nucleus",
        "pontine_nuclei",
        "superior_olivary_complex",
        "tegmentum",
    )
    # The pons has eleven structural children (nine sub-
    # containers + the cerebellar peduncles + the cranial nerve
    # nuclei sub-containers with their own sub-containers).
    # The basis pontis, transverse pontine fibers, corticospinal
    # and corticobulbar tracts, pontine tegmentum (general),
    # MLF, medial lemniscus, spinal trigeminal tract, and
    # mesencephalic trigeminal tract are prose.

Reaching the metencephalon (recommended consumer pattern — the
parent)::

    # The metencephalon is the CONTAINER (pons + cerebellum +
    # fourth ventricle):
    #
    #   hindbrain.metencephalon
    #
    # The pons is a CHILD sub-container of the metencephalon.

Reaching the cerebellum (recommended consumer pattern — NOTE
the ventral-brainstem-vs-dorsal-suprasegmental boundary)::

    # The cerebellum is the DORSAL SUPRASEGMENTAL structure:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The pons is the VENTRAL BRAINSTEM; the cerebellum is the
    # DORSAL SUPRASEGMENTAL structure. They are connected via
    # the cerebellar peduncles (children of the pons).

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the ventral-brainstem-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The pons is the VENTRAL WALL of the fourth ventricle; the
    # fourth ventricle is the CSF cavity between the pons/medulla
    # and the cerebellum.

Reaching the medulla oblongata (recommended consumer pattern —
NOTE the rostral-vs-caudal boundary)::

    # The medulla oblongata is the CAUDAL brainstem segment
    # (myelencephalic):
    #
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The pons is ROSTRAL; the medulla oblongata is CAUDAL. They
    # are continuous at the pontomedullary junction (the
    # bulbopontine sulcus).

Reaching the midbrain (recommended consumer pattern — NOTE the
caudal-vs-rostral boundary)::

    # The midbrain is the ROSTRAL brainstem segment
    # (mesencephalic):
    #
    #   midbrain
    #
    # The pons is CAUDAL to the midbrain; the midbrain is ROSTRAL
    # to the pons. They are continuous at the mesencephalic-
    # metencephalic junction.

Reaching the brainstem (recommended consumer pattern — NOTE the
segment-vs-whole-neuraxis boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons +
    # medulla oblongata):
    #
    #   midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The pons is a SEGMENT of the brainstem.

Reaching the basis pontis (recommended consumer pattern — NOTE
the whole-vs-ventral-portion boundary)::

    # The basis pontis is the VENTRAL PORTION of the pons:
    #
    #   (prose) hindbrain.metencephalon.pons.<basis_pontis>
    #
    # The basis pontis is a PART of the pons; the pons is the
    # WHOLE region.

Reaching the pontine tegmentum (recommended consumer pattern —
NOTE the whole-vs-dorsal-portion boundary)::

    # The pontine tegmentum is the DORSAL PORTION of the pons:
    #
    #   hindbrain.metencephalon.pons.tegmentum
    #
    # The pontine tegmentum is a PART of the pons; the pons is
    # the WHOLE region.

Reaching the pontine nuclei (recommended consumer pattern —
NOTE the whole-vs-grey-matter-relay-nuclei boundary)::

    # The pontine nuclei are the GREY-MATTER RELAY NUCLEI of the
    # basis pontis (the cortico-ponto-cerebellar relay):
    #
    #   hindbrain.metencephalon.pons.pontine_nuclei
    #
    # The pontine nuclei are a PART of the pons; the pons is the
    # WHOLE region.

Reaching the cranial nerve nuclei (recommended consumer
pattern — NOTE the whole-vs-cranial-nerve-nuclei boundary)::

    # The cranial nerve nuclei (V-VIII) are the CRANIAL NERVE
    # NUCLEI of the pontine tegmentum:
    #
    #   hindbrain.metencephalon.pons.cranial_nerve_nuclei
    #
    # The cranial nerve nuclei are a PART of the pons; the pons
    # is the WHOLE region.

Reaching the cerebellar peduncles (recommended consumer
pattern — NOTE the whole-vs-white-matter-tracts boundary)::

    # The cerebellar peduncles (superior, middle, inferior) are
    # the WHITE-MATTER TRACTS connecting the cerebellum to the
    # brainstem:
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles
    #
    # The cerebellar peduncles are a PART of the pons; the pons
    # is the WHOLE region.

Reaching the pontine reticular formation (recommended consumer
pattern — NOTE the whole-vs-reticular-formation boundary)::

    # The pontine reticular formation is the RETICULAR FORMATION
    # of the pons (the caudal pontine reticular nucleus, the
    # paramedian pontine reticular formation, the parvocellular
    # reticular nucleus, and the tegmental pontine reticular
    # nucleus):
    #
    #   hindbrain.metencephalon.pons.caudal_pontine_reticular_nucleus
    #   hindbrain.metencephalon.pons.paramedian_pontine_reticular_formation
    #   hindbrain.metencephalon.pons.parvocellular_reticular_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.tegmental_pontine_reticular_nucleus
    #
    # The pontine reticular formation is a PART of the pons; the
    # pons is the WHOLE region.

Reaching the parabrachial area (recommended consumer pattern —
NOTE the whole-vs-parabrachial-complex boundary)::

    # The parabrachial area is the PARABRACHIAL COMPLEX of the
    # pontine tegmentum (the lateral parabrachial nucleus, the
    # medial parabrachial nucleus, and the subparabrachial
    # nucleus with the Kölliker-Fuse nucleus and the pontine
    # respiratory group):
    #
    #   hindbrain.metencephalon.pons.parabrachial_area
    #
    # The parabrachial area is a PART of the pons; the pons is
    # the WHOLE region.

Reaching the superior olivary complex (recommended consumer
pattern — NOTE the whole-vs-auditory-processing-complex
boundary)::

    # The superior olivary complex is the AUDITORY PROCESSING
    # complex of the pontine tegmentum (the lateral superior
    # olive, the medial nucleus of trapezoid body, and the
    # medial superior olive):
    #
    #   hindbrain.metencephalon.pons.superior_olivary_complex
    #
    # The superior olivary complex is a PART of the pons; the
    # pons is the WHOLE region.

Reaching the locus coeruleus and the tegmentum nuclei
(recommended consumer pattern — NOTE the whole-vs-tegmentum-
nuclei boundary)::

    # The locus coeruleus, the laterodorsal tegmental nucleus,
    # the pedunculopontine nucleus, the nucleus incertus, the
    # pontine micturition center, and the tegmental pontine
    # reticular nucleus are the PONTINE TEGMENTUM NUCLEI:
    #
    #   hindbrain.metencephalon.pons.tegmentum.locus_coeruleus
    #   hindbrain.metencephalon.pons.tegmentum.laterodorsal_tegmental_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.pedunculopontine_nucleus
    #   hindbrain.metencephalon.pons.tegmentum.nucleus_incertus
    #   hindbrain.metencephalon.pons.tegmentum.pontine_micturition_center
    #   hindbrain.metencephalon.pons.tegmentum.tegmental_pontine_reticular_nucleus
    #
    # These tegmentum nuclei are PARTS of the pons; the pons is
    # the WHOLE region.

Reaching the diencephalon and the telencephalon (recommended
consumer pattern — NOTE the hindbrain-vs-forebrain boundary)::

    # The diencephalon and the telencephalon are the FOREBRAIN
    # structures:
    #
    #   forebrain.diencephalon
    #   forebrain.telencephalon
    #
    # The pons is a HINDBRAIN (metencephalic) structure.

Reaching the spinal cord (recommended consumer pattern — NOTE
the brainstem-vs-spinal-cord boundary)::

    # The spinal cord is the CAUDAL continuation of the
    # neuraxis:
    #
    #   spinal_cord
    #
    # The pons is separated from the spinal cord by the whole
    # medulla oblongata.

Sub-region detail (not wired at the pons level — consult the
sub-containers and references)::

    # The pons's sub-region detail is prose within the
    # sub-containers:
    #   basis pontis -> pontine nuclei, corticospinal and
    #                   corticobulbar tracts, transverse
    #                   pontine fibers (the cortico-ponto-
    #                   cerebellar relay)
    #   pontine tegmentum -> cranial nerve nuclei V-VIII, pontine
    #                        reticular formation, locus coeruleus,
    #                        parabrachial complex,
    #                        pedunculopontine nucleus,
    #                        laterodorsal tegmental nucleus,
    #                        superior olivary complex, nucleus
    #                        incertus, pontine micturition center
    #   cerebellar peduncles -> superior, middle, inferior
    #   MLF, medial lemniscus, spinal trigeminal tract,
    #   mesencephalic trigeminal tract -> ascending/descending
    #                                     tracts within the pons
    #
    # Do not attempt to resolve these as sub-paths of the pons.

Bilateral iteration (recommended consumer pattern — for
bilateral sub-structures)::

    for side in ("left", "right"):
        # e.g., cranial nerve nuclei, pontine nuclei,
        # superior olivary complex
        side_path = (
            f"hindbrain.metencephalon.pons.cranial_nerve_nuclei."
            f"{side}"
        )
        # resolve side_path through the memory/recall layer

References
----------
*   **Canonical pons anatomy:** Standring, S. (ed.) (2020).
    *Gray's Anatomy: The Anatomical Basis of Clinical
    Practice*, 42nd ed. (Pons — basis pontis, pontine
    tegmentum, cranial nerve nuclei, pontine nuclei,
    cerebellar peduncles, reticular formation, locus
    coeruleus, parabrachial complex, superior olivary
    complex.)
*   **Brainstem overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Pons — basis pontis, pontine tegmentum, cranial nerve
    nuclei V–VIII, pontine reticular formation, locus
    coeruleus, parabrachial complex, superior olivary
    complex, pedunculopontine nucleus, laterodorsal
    tegmental nucleus, nucleus incertus, pontine micturition
    center.)
*   **Developmental origin (rhombencephalon → metencephalon):**
    Puelles, L., Rubenstein, J.L.R. (2015). "A new scenario
    of hypothalamic organization: implications of a new
    model of the prosomeric brain." *Journal of Comparative
    Neurology* 523:1077–1108. (Rhombencephalon — the
    embryonic hindbrain vesicle; adult derivatives
    metencephalon and myelencephalon.)
*   **Cortico-ponto-cerebellar pathway:** Mihailoff, G.A.,
    et al. (1985). "The basilar pontine gray of the opossum:
    a correlated light and electron microscopic analysis."
    *Journal of Comparative Neurology* 233:417–437.
    (Pontine nuclei and transverse pontine fibers —
    corticopontine and corticobulbar relay.)
*   **Corticospinal and corticobulbar tracts (basis pontis):**
    Nathan, P.W., Smith, M.C. (1955). "Long descending
    tracts in man." *Brain* 78:319–348. (Corticospinal and
    corticobulbar tracts — descending motor pathways
    traversing the basis pontis.)
*   **Pontine respiratory group:** Lumsden, T. (1923).
    "Observations on the respiratory centres in the cat."
    *Journal of Physiology* 57:153–160. (Pontine respiratory
    group — pneumotaxic and apneustic centers.)
*   **Locus coeruleus and arousal:** Berridge, C.W.,
    Waterhouse, B.D. (2003). "The locus coeruleus-
    noradrenergic system: modulation of behavioral state
    and state-dependent cognitive processes." *Brain
    Research Reviews* 42:33–84. (Locus coeruleus —
    arousal, attention, stress-response.)
*   **Superior olivary complex and sound localization:**
    Grothe, B., Pecka, M., McAlpine, D. (2010). "Mechanisms
    of sound localization in mammals." *Physiological
    Reviews* 90:983–1012. (Superior olivary complex —
    sound localization; interaural time and intensity
    differences.)
*   **Pontine micturition center (Barrington's nucleus):**
    Barrington, F.J.F. (1925). "The effect of lesions of the
    hind- and mid-brain on micturition in the cat."
    *Quarterly Journal of Experimental Physiology* 15:81–102.
    (Pontine micturition center — Barrington's nucleus —
    pontine control of micturition.)
*   **Parabrachial complex (autonomic relay):** Saper, C.B.,
    Loewy, A.D. (1980). "Efferent connections of the
    parabrachial nucleus in the rat." *Brain Research*
    197:291–317. (Parabrachial complex — autonomic and
    respiratory relay from the nucleus tractus solitarius
    to the forebrain.)
*   **Pedunculopontine nucleus and laterodorsal tegmental
    nucleus (arousal and sleep-wake):** Saper, C.B., et al.
    (2005). "Hypothalamic regulation of sleep and circadian
    rhythms." *Nature* 437:1257–1263. (Pedunculopontine
    nucleus and laterodorsal tegmental nucleus — cholinergic
    arousal and sleep-wake centers.)
*   **Nucleus incertus (stress, anxiety, feeding):** Ryan,
    P.J., et al. (2017). "Nucleus incertus — an
    emerging role in the control of motivated behavior."
    *Frontiers in Neuroendocrinology* 46:35–47. (Nucleus
    incertus — stress, anxiety, feeding.)
*   **Locked-in syndrome (ventral pontine infarction):**
    Plum, F., Posner, J.B. (1980). *The Diagnosis of Stupor
    and Coma*, 3rd ed. (Locked-in syndrome — ventral
    pontine infarction; the basis pontis.)
*   **Central pontine myelinolysis:** Adams, R.D., Victor,
    M., Mancall, E.L. (1959). "Central pontine
    myelinolysis: a hitherto undescribed disease occurring
    in alcoholic and malnourished patients." *A.M.A.
    Archives of Neurology and Psychiatry* 81:154–172.
    (Osmotic demyelination syndrome — demyelination of the
    basis pontis.)
*   **Brainstem glioma (DIPG / diffuse midline glioma):**
    Louis, D.N., et al. (2016). "The 2016 World Health
    Organization Classification of Tumors of the Central
    Nervous System: a summary." *Acta Neuropathologica*
    131:803–820. (Diffuse midline glioma — pediatric
    brainstem tumor arising in the pons.)
*   **SLEA (contrast — the pons is NOT included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39.
    (SLEA continuum — BNST, central nucleus, ventral
    pallidum, nucleus accumbens; NOT the pons.)
*   NeuroNames — Pons; FMA — Pons.
"""