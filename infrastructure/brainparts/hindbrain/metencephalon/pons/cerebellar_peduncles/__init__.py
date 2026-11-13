"""
infrastructure.brainparts.hindbrain.metencephalon.pons.cerebellar_peduncles
===========================================================================

Anatomical Hierarchy
--------------------
::

    pons
    ├── caudal_pontine_reticular_nucleus
    ├── cerebellar_peduncles                   <-- THIS MODULE
    │   ├── inferior_cerebellar_peduncle
    │   ├── middle_cerebellar_peduncle
    │   └── superior_cerebellar_peduncle
    ├── cranial_nerve_nuclei
    ├── parabrachial_area
    ├── paramedian_pontine_reticular_formation
    ├── parvocellular_reticular_nucleus
    ├── pontine_nuclei
    ├── superior_olivary_complex
    └── tegmentum

**Primary synonym:** Cerebellar peduncles; pedunculi cerebellares;
the cerebellar stalks; the cerebellar peduncles (as a group); the
three cerebellar peduncles; the peduncles of the cerebellum;
the superior / middle / inferior cerebellar peduncles (as a
set); the cerebellar white-matter peduncles.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
grey-matter structure.** A **group of three paired white-matter
tracts** — the **superior cerebellar peduncle (brachium
conjunctivum)**, the **middle cerebellar peduncle (brachium
pontis)**, and the **inferior cerebellar peduncle (restiform
body + juxtarestiform body)** — that **connect** the cerebellum
to the **brainstem** (midbrain, pons, medulla oblongata) and
**carry** the **afferent** and **efferent** fibers of the
cerebellum.
**Part of:** The **pons** container — the **white-matter
peduncles** that **attach** the cerebellum to the brainstem
(the tree wires the cerebellar peduncles as **children of the
pons**, **not** of the cerebellum — see *Boundary status*).
The **pons** is a **child sub-container of the metencephalon**;
the **metencephalon** is the **rostral** of the **two
rhombencephalic sub-vesicles**; the **hindbrain** is the
**caudal** of the **three primary brain vesicles**.
**Structural parent:** ``.../pons/`` → **direct child** of the
pons container.
**Structural children:** **Three** — ``inferior_cerebellar_
peduncle/``, ``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/``. Each is a **sub-container**
(the **peduncle itself**), comprising the **white-matter
fibers** of that peduncle. The **superior cerebellar peduncle
(decussation of Wernekink)**, the **middle cerebellar peduncle
(pontocerebellar fibers)**, the **inferior cerebellar peduncle
(restiform body + juxtarestiform body)**, the **specific
fiber tracts** within each peduncle (the **dorsal
spinocerebellar tract**, the **ventral spinocerebellar
tract**, the **cuneocerebellar tract**, the **trigemino-
cerebellar tract**, the **corticopontocerebellar fibers**,
the **olivocerebellar fibers**, the **vestibulocerebellar
fibers**, the **reticulocerebellar fibers**, the **superior
cerebellar peduncle efferents** from the **dentate**,
**interposed**, and **fastigial nuclei**, the **juxtarestiform
body**), and the **decussation of Wernekink** (the **superior
cerebellar peduncle decussation** — the **ventral tegmental
decussation** of the **superior cerebellar peduncle** in the
**caudal midbrain**) are documented as **prose**, not as
structural children of the cerebellar peduncles container.
**Boundary status (PEDUNCLES — NOT the cerebellum):** **Boundary
case — the cerebellar peduncles are the WHITE-MATTER TRACTS
that CONNECT the cerebellum to the brainstem, NOT the
cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is the **dorsal
suprasegmental structure** — the **lateral hemispheres** and
the **midline vermis**, with the **cortical divisions** and
the **deep nuclei**. The **cerebellar peduncles** (here) are
the **white-matter tracts** that **connect** the cerebellum
to the brainstem — the **conduction infrastructure** that
**carries** the cerebellar afferents and efferents. **The
cerebellum is the SUPRASEGMENTAL STRUCTURE; the cerebellar
peduncles are the CONDUCTION INFRASTRUCTURE.** Consumers must
**not** conflate the cerebellar peduncles with the cerebellum
— the **peduncles** are the **tracts**; the **cerebellum**
is the **structure** they **connect**.
**Boundary status (PEDUNCLES AS A GROUP — NOT a single
peduncle):** **Boundary case — the cerebellar peduncles as a
group are the SET of three peduncles, NOT a single
peduncle.** The **cerebellar peduncles** container (here) is
the **group of three peduncles** — the **superior cerebellar
peduncle** (``.../cerebellar_peduncles/superior_cerebellar_
peduncle/``), the **middle cerebellar peduncle**
(``.../cerebellar_peduncles/middle_cerebellar_peduncle/``),
and the **inferior cerebellar peduncle**
(``.../cerebellar_peduncles/inferior_cerebellar_peduncle/``).
**The container is the GROUP; each peduncle is a MEMBER of the
group.** Consumers must **not** conflate the cerebellar
peduncles as a group with any single peduncle — the
**superior**, **middle**, and **inferior** cerebellar
peduncles are **distinct peduncles** with **distinct
fiber content** and **distinct functions**.
**Boundary status (PEDUNCLES — NOT the brainstem):** **Boundary
case — the cerebellar peduncles are the WHITE-MATTER TRACTS
that ATTACH the cerebellum to the brainstem, NOT the
brainstem.** The **brainstem** is the **segmental neuraxis**
(midbrain + pons + medulla oblongata) — the **neural tissue**
that the cerebellar peduncles **attach** the cerebellum to.
The **cerebellar peduncles** (here) are the **white-matter
tracts** that **connect** the cerebellum to the brainstem —
the **conduction infrastructure**. **The brainstem is the
SEGMENTAL NEURAXIS; the cerebellar peduncles are the
CONDUCTION INFRASTRUCTURE that connects the cerebellum to
it.** Consumers must **not** conflate the cerebellar
peduncles with the brainstem — the **peduncles** are the
**tracts**; the **brainstem** is the **neural tissue**.
**Boundary status (PEDUNCLES — NOT the fourth ventricle):**
**Boundary case — the cerebellar peduncles are the WHITE-MATTER
TRACTS, NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **cerebellar peduncles** (here) are the
**white-matter tracts** that **attach** the cerebellum to
the brainstem — the **tracts** that **form the lateral
walls** of the fourth ventricle (the **superior cerebellar
peduncle** forms the **lateral wall** of the **rostral fourth
ventricle**; the **inferior cerebellar peduncle** forms the
**lateral wall** of the **caudal fourth ventricle**). **The
peduncles are the TRACTS; the fourth ventricle is the CSF
CAVITY that the peduncles are ADJACENT to.** Consumers must
**not** conflate the cerebellar peduncles with the fourth
ventricle.
**Boundary status (PEDUNCLES — NOT the deep nuclei):** **Boundary
case — the cerebellar peduncles are the WHITE-MATTER TRACTS,
NOT the deep nuclei.** The **cerebellar deep nuclei**
(``.../cerebellum/nuclei/``) — the **dentate nucleus**, the
**interposed nucleus** (the **emboliform nucleus** + the
**globose nucleus**), and the **fastigial nucleus** — are
the **grey-matter output nuclei** of the cerebellum. The
**cerebellar peduncles** (here) are the **white-matter
tracts** that **carry** the **efferents** of the cerebellar
deep nuclei (the **superior cerebellar peduncle** carries the
**dentate** and **interposed** efferents; the **inferior
cerebellar peduncle** — the **juxtarestiform body** — carries
the **fastigial** efferents). **The deep nuclei are the
GREY-MATTER OUTPUT NUCLEI; the cerebellar peduncles are the
WHITE-MATTER TRACTS that carry their efferents.** Consumers
must **not** conflate the cerebellar peduncles with the
cerebellar deep nuclei.
**Boundary status (PEDUNCLES — NOT the cerebellar white
matter):** **Boundary case — the cerebellar peduncles are the
WHITE-MATTER TRACTS that CONNECT the cerebellum to the
brainstem, NOT the cerebellar deep white matter (the arbor
vitae).** The **cerebellar deep white matter**
(``.../cerebellum/deep_white_matter/``) is the **white-matter
core** of the cerebellum — the **arbor vitae** and the
**intracerebellar tracts**. The **cerebellar peduncles**
(here) are the **white-matter tracts** that **attach** the
cerebellum to the brainstem — the **extracerebellar white
matter** that **connects** the cerebellar white matter (the
arbor vitae) to the brainstem. **The deep white matter is
INTRACEREBELLAR; the cerebellar peduncles are EXTRACEREBELLAR
(they connect the cerebellum to the brainstem).** Consumers
must **not** conflate the cerebellar peduncles with the
cerebellar deep white matter — the **deep white matter** is
the **arbor vitae**; the **peduncles** are the **extracerebellar
white-matter tracts**.
**Boundary status (PEDUNCLES — NOT the cerebral peduncle):**
**Boundary case — the cerebellar peduncles are the CEREBELLAR
WHITE-MATTER TRACTS, NOT the cerebral peduncle.** The
**cerebral peduncle** (``.../midbrain/cerebral_peduncle/``)
is the **midbrain** structure — the **ventral midbrain**
(crus cerebri + substantia nigra + tegmentum) that **contains**
the **corticospinal**, **corticobulbar**, and
**corticopontine** tracts. The **cerebellar peduncles**
(here) are the **cerebellar** white-matter tracts that
**connect** the cerebellum to the brainstem. **They are
DIFFERENT PEDUNCLES** — the **cerebral peduncle** is the
**midbrain ventral structure**; the **cerebellar peduncles**
are the **cerebellar white-matter tracts** (superior,
middle, inferior). The name **"peduncle"** is **shared**
(both are "peduncles"), but the **structures are different**
— consumers must **not** conflate the cerebellar peduncles
with the cerebral peduncle.
**Boundary status (THREE PEDUNCLES — NOT a single uniform
structure):** **Boundary case — the cerebellar peduncles are
a GROUP of THREE peduncles (superior, middle, inferior),
each with DISTINCT fiber content and DISTINCT functions,
not a single uniform structure.** The **superior cerebellar
peduncle** (``.../cerebellar_peduncles/superior_cerebellar_
peduncle/``) is the **efferent** peduncle (the **dentate**,
**interposed**, and (via the **juxtarestiform body**) the
**fastigial** efferents — the **superior cerebellar
peduncle** — the **decussation of Wernekink**). The
**middle cerebellar peduncle**
(``.../cerebellar_peduncles/middle_cerebellar_peduncle/``) is
the **afferent** peduncle (the **corticopontocerebellar**
fibers — the **pontocerebellar** fibers — the **largest**
peduncle). The **inferior cerebellar peduncle**
(``.../cerebellar_peduncles/inferior_cerebellar_peduncle/``)
is the **mixed** peduncle — the **restiform body** (the
**dorsal spinocerebellar tract**, the **cuneocerebellar
tract**, the **olivocerebellar fibers**, the
**reticulocerebellar fibers**) + the **juxtarestiform body**
(the **fastigial efferents**, the **vestibulocerebellar
fibers**, the **cerebellovestibular fibers**). **Each
peduncle has a distinct fiber content and a distinct
function** — the tree wires the **inferior_cerebellar_
peduncle/``**, ``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/`` as **sub-containers** of
the cerebellar peduncles. Consumers must **not** treat the
cerebellar peduncles as a single uniform structure — they
are a **group of three functionally distinct peduncles**.
**Boundary status (PAIRED — MULTIPLE left/right peduncles):**
**Boundary case — the cerebellar peduncles are PAIRED (left
and right), with THREE PEDUNCLES PER SIDE (the left superior,
the right superior, the left middle, the right middle, the
left inferior, and the right inferior cerebellar peduncles).**
The cerebellar peduncles container (here) is the **group of
three peduncles** — each peduncle is **bilaterally paired**
(the **left** and **right** superior cerebellar peduncles;
the **left** and **right** middle cerebellar peduncles; the
**left** and **right** inferior cerebellar peduncles). The
tree wires the **inferior_cerebellar_peduncle/``**,
``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/`` as **sub-containers** of
the cerebellar peduncles — **each sub-container is the
peduncle as a bilateral pair** (the left and right peduncle
of that name). The **bilateral pairing** is documented as
**prose** within each peduncle sub-container. Consumers must
**not** treat the cerebellar peduncles as a **single
unpaired structure** — they are **paired** (left and right)
for each of the **three peduncles**.
**Boundary status (PONS — NOT the cerebellum or the
brainstem):** **Boundary case — the cerebellar peduncles are
CHILDREN of the PONS, NOT of the cerebellum or the
brainstem.** The tree wires the **cerebellar peduncles** as
**children of the pons** (``.../pons/cerebellar_peduncles/``),
**not** of the cerebellum
(``.../metencephalon/cerebellum/``) or the brainstem (which
is not a single container in this tree). **The pons "owns"
the peduncle attachment** — the peduncles are the
**white-matter tracts** that **attach** the cerebellum to
the brainstem, and the tree places them under the **pons**
(the rostral brainstem segment that the peduncles are most
closely associated with — the **middle cerebellar peduncle**
is the **pontine** peduncle). Consumers must **not** treat
the cerebellar peduncles as children of the cerebellum — the
**tree wires them as children of the pons**.
**Boundary status (SLEA-FREE — the cerebellar peduncles are
NOT an extended-amygdala component):** **Boundary case — the
cerebellar peduncles are SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA
component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **cerebellar peduncles** are **white-matter
tracts** — they are **NOT** an extended-amygdala component,
and they carry **NO SLEA warning**. Consumers must **not**
import the SLEA warning into the cerebellar peduncles — they
are **SLEA-free**.
**Boundary status (CONDUCTION INFRASTRUCTURE — NOT a neural
processor):** **Boundary case — the cerebellar peduncles are
CONDUCTION INFRASTRUCTURE, NOT a neural processor.** They do
**not** compute, **modulate**, or **process** neural signals
in the classical sense — they **conduct** them. The
**processing** happens in the **cerebellum** (cerebellar
cortex, deep nuclei) and in the **brainstem** (pons,
medulla oblongata, midbrain). The **cerebellar peduncles**
are the **white-matter tracts** that **carry** the signals
between the cerebellum and the brainstem. Consumers must
**not** treat the cerebellar peduncles as a **grey-matter
processing structure** — they are **white matter**.

Overview
--------
The cerebellar peduncles are the **group of three paired
white-matter tracts** that **connect** the cerebellum to the
**brainstem** — the **superior cerebellar peduncle (brachium
conjunctivum)**, the **middle cerebellar peduncle (brachium
pontis)**, and the **inferior cerebellar peduncle (restiform
body + juxtarestiform body)**. They are a **container module**
with **three structural sub-containers**
(``inferior_cerebellar_peduncle/``,
``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/``), **each representing the
peduncle as a bilateral pair** (left and right).

**The cerebellar peduncles are the CONDUCTION INFRASTRUCTURE
between the cerebellum and the brainstem, NOT the cerebellum
and NOT the brainstem.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is the **dorsal
suprasegmental structure**; the **brainstem** is the
**segmental neuraxis** (midbrain + pons + medulla oblongata);
the **cerebellar peduncles** (here) are the **white-matter
tracts** that **connect** them. **The peduncles are the
tracts; the cerebellum and the brainstem are the structures
they connect.**

**The cerebellar peduncles are a GROUP of THREE peduncles, each
with DISTINCT fiber content and DISTINCT functions.** The
**superior cerebellar peduncle** is the **efferent** peduncle
(mostly); the **middle cerebellar peduncle** is the
**afferent** peduncle (the **largest** peduncle — the
**corticopontocerebellar** fibers); the **inferior cerebellar
peduncle** is the **mixed** peduncle (the **restiform body**
= **spinocerebellar**, **cuneocerebellar**,
**olivocerebellar**, **reticulocerebellar**; the
**juxtarestiform body** = **fastigial efferents**,
**vestibulocerebellar**, **cerebellovestibular**).

**The cerebellar peduncles are PAIRED — each peduncle has a
LEFT and a RIGHT member.** The **left superior cerebellar
peduncle** and the **right superior cerebellar peduncle**;
the **left middle cerebellar peduncle** and the **right
middle cerebellar peduncle**; the **left inferior cerebellar
peduncle** and the **right inferior cerebellar peduncle**.
The tree wires the **three peduncles** as **three
sub-containers**, each representing the **peduncle as a
bilateral pair**.

**The cerebellar peduncles are CHILDREN of the PONS in the
tree.** The tree wires the cerebellar peduncles as
**children of the pons** (``.../pons/cerebellar_peduncles/``)
— **not** of the cerebellum or the brainstem. The **pons
"owns" the peduncle attachment** — the **middle cerebellar
peduncle** is the **pontine peduncle** (the **brachium
pontis**), and the tree wires all three peduncles under the
**pons**.

Cerebellar Peduncles Composition (sub-containers and prose)
----------------------------------------------------------
The cerebellar peduncles are a **group of three paired
white-matter tracts** with **three sub-containers** —
documented as **structural children**
(``inferior_cerebellar_peduncle/``,
``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/``) — and **many prose-defined
sub-structures** documented within those sub-containers:

*   **Superior cerebellar peduncle (brachium conjunctivum)**
    (``.../cerebellar_peduncles/superior_cerebellar_peduncle/``)
    — the **efferent** peduncle (mostly) — the **superior
    cerebellar peduncle** (the **brachium conjunctivum**).
    Documented as a **structural child**. Its **fiber
    content** (the **dentate** and **interposed** efferents;
    the **fastigial** efferents via the **juxtarestiform
    body**; the **decussation of Wernekink** — the **ventral
    tegmental decussation** of the superior cerebellar
    peduncle in the **caudal midbrain**) is documented as
    **prose** within the **superior_cerebellar_peduncle/`**
    sub-container.

*   **Middle cerebellar peduncle (brachium pontis)**
    (``.../cerebellar_peduncles/middle_cerebellar_peduncle/``)
    — the **afferent** peduncle (the **largest** peduncle) —
    the **middle cerebellar peduncle** (the **brachium
    pontis**). Documented as a **structural child**. Its
    **fiber content** (the **corticopontocerebellar**
    fibers — the **pontocerebellar** fibers — from the
    **contralateral pontine nuclei** to the **contralateral
    cerebellar cortex**) is documented as **prose** within
    the **middle_cerebellar_peduncle/`** sub-container.

*   **Inferior cerebellar peduncle (restiform body +
    juxtarestiform body)**
    (``.../cerebellar_peduncles/inferior_cerebellar_peduncle/``)
    — the **mixed** peduncle — the **inferior cerebellar
    peduncle** (the **restiform body** = the **dorsal
    spinocerebellar tract**, the **cuneocerebellar tract**,
    the **olivocerebellar fibers**, the **reticulocerebellar
    fibers**; the **juxtarestiform body** = the **fastigial
    efferents**, the **vestibulocerebellar fibers**, the
    **cerebellovestibular fibers**). Documented as a
    **structural child**. Its **fiber content** (the
    **restiform body** + the **juxtarestiform body**) is
    documented as **prose** within the
    **inferior_cerebellar_peduncle/`** sub-container.

**These fiber contents are prose, not structural children of
the cerebellar peduncles container.** The tree wires the
**cerebellar peduncles** as a **container** with **three
sub-containers** (the **three peduncles**) — the **fiber
tracts** (the **dorsal spinocerebellar tract**, the
**ventral spinocerebellar tract**, the **cuneocerebellar
tract**, the **trigeminocerebellar tract**, the
**corticopontocerebellar fibers**, the **olivocerebellar
fibers**, the **vestibulocerebellar fibers**, the
**reticulocerebellar fibers**, the **dentate efferents**,
the **interposed efferents**, the **fastigial efferents**,
the **cerebellovestibular fibers**, the **juxtarestiform
body**, and the **decussation of Wernekink**) are
documented as **prose** within the **sub-containers**.
Consumers that need **tract-level** resolution should consult
the **sub-container modules** and the references, not the
cerebellar peduncles container.

The Cerebellar Peduncles / Cerebellum Boundary
----------------------------------------------
This is the **conduction-infrastructure-vs-suprasegmental-
structure** boundary:

*   **Cerebellar peduncles** (this module) — the
    **white-matter tracts** that **connect** the cerebellum
    to the brainstem.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the
    **dorsal suprasegmental structure**.

**The cerebellum is the SUPRASEGMENTAL STRUCTURE; the cerebellar
peduncles are the CONDUCTION INFRASTRUCTURE.** Consumers must
**not** conflate the cerebellar peduncles with the cerebellum.

The Cerebellar Peduncles / Brainstem Boundary
---------------------------------------------
This is the **conduction-infrastructure-vs-segmental-neuraxis**
boundary:

*   **Cerebellar peduncles** (this module) — the
    **white-matter tracts** that **connect** the cerebellum
    to the brainstem.

*   **Brainstem** (midbrain + pons + medulla oblongata) — the
    **segmental neuraxis**.

**The brainstem is the SEGMENTAL NEURAXIS; the cerebellar
peduncles are the CONDUCTION INFRASTRUCTURE that connects the
cerebellum to it.** Consumers must **not** conflate the
cerebellar peduncles with the brainstem.

The Cerebellar Peduncles / Fourth Ventricle Boundary
----------------------------------------------------
This is the **white-matter-tract-vs-CSF-cavity** boundary:

*   **Cerebellar peduncles** (this module) — the **white-matter
    tracts**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The peduncles are the TRACTS; the fourth ventricle is the CSF
CAVITY that the peduncles are ADJACENT to (the superior and
inferior cerebellar peduncles form the lateral walls of the
fourth ventricle).** Consumers must **not** conflate the
cerebellar peduncles with the fourth ventricle.

The Cerebellar Peduncles / Deep Nuclei Boundary
-----------------------------------------------
This is the **white-matter-tract-vs-grey-matter-output-nuclei**
boundary:

*   **Cerebellar peduncles** (this module) — the **white-matter
    tracts**.

*   **Cerebellar deep nuclei** (``.../cerebellum/nuclei/``) —
    the **grey-matter output nuclei** (dentate, interposed,
    fastigial).

**The deep nuclei are the GREY-MATTER OUTPUT NUCLEI; the
cerebellar peduncles are the WHITE-MATTER TRACTS that carry
their efferents.** Consumers must **not** conflate the
cerebellar peduncles with the cerebellar deep nuclei.

The Cerebellar Peduncles / Cerebellar Deep White Matter Boundary
----------------------------------------------------------------
This is the **extracerebellar-vs-intracerebellar white
matter** boundary:

*   **Cerebellar peduncles** (this module) — the
    **extracerebellar white-matter tracts** that **connect**
    the cerebellum to the brainstem.

*   **Cerebellar deep white matter**
    (``.../cerebellum/deep_white_matter/``) — the
    **intracerebellar white-matter core** (arbor vitae).

**The deep white matter is INTRACEREBELLAR; the cerebellar
peduncles are EXTRACEREBELLAR.** Consumers must **not**
conflate the cerebellar peduncles with the cerebellar deep
white matter.

The Cerebellar Peduncles / Cerebral Peduncle Boundary
-----------------------------------------------------
This is the **cerebellar-white-matter-vs-midbrain-ventral-
structure** boundary:

*   **Cerebellar peduncles** (this module) — the **cerebellar**
    white-matter tracts (superior, middle, inferior).

*   **Cerebral peduncle**
    (``.../midbrain/cerebral_peduncle/``) — the **midbrain
    ventral structure** (crus cerebri + substantia nigra +
    tegmentum).

**They are DIFFERENT PEDUNCLES** — the **cerebral peduncle** is
the **midbrain ventral structure**; the **cerebellar
peduncles** are the **cerebellar white-matter tracts**. The
name **"peduncle"** is **shared**, but the **structures are
different**. Consumers must **not** conflate the cerebellar
peduncles with the cerebral peduncle.

The Cerebellar Peduncles / Pons Boundary
----------------------------------------
This is the **child-vs-container** boundary:

*   **Cerebellar peduncles** (this module) — **children of the
    pons** in the tree.

*   **Pons** (``.../pons/``) — the **container** (the whole
    metencephalic brainstem segment).

**The cerebellar peduncles are CHILDREN of the pons in the
tree** — the **pons "owns" the peduncle attachment**.
Consumers must **not** treat the cerebellar peduncles as
children of the cerebellum or the brainstem — the **tree
wires them as children of the pons**.

The Cerebellar Peduncles / SLEA Boundary
----------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cerebellar peduncles** (this module) — **SLEA-FREE**.
    No extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**,
    **ventral pallidum**, and **nucleus accumbens** (wired
    elsewhere).

**The cerebellar peduncles are NOT part of the SLEA
continuum.** They are **white-matter tracts**, and they carry
**no SLEA warning**. Consumers must **not** import the SLEA
warning into the cerebellar peduncles.

Function in the Human Brain
---------------------------
The cerebellar peduncles' functions are **conduction** — the
**carriage** of **afferent** and **efferent** signals
between the cerebellum and the brainstem — **NOT neural
processing**:

*   **Superior Cerebellar Peduncle (Efferent — Mostly):** The
    **superior cerebellar peduncle** carries the **efferent**
    fibers from the **dentate nucleus** and the **interposed
    nucleus** (the **cerebellothalamocortical** and
    **cerebellorubral** projections) — and, via the
    **juxtarestiform body** (part of the **inferior
    cerebellar peduncle**), the **fastigial nucleus
    efferents** (the **cerebellovestibular** and
    **cerebelloreticular** projections). The **superior
    cerebellar peduncle** **decussates** in the **caudal
    midbrain** (the **decussation of Wernekink** — the
    **ventral tegmental decussation**) — the **cerebellar
    efferents cross** to the **contralateral** side. The
    **double crossing** (the **corticopontocerebellar** and
    the **cerebellothalamocortical**) makes cerebellar
    control **ipsilateral**.

*   **Middle Cerebellar Peduncle (Afferent — the Largest
    Peduncle):** The **middle cerebellar peduncle** (the
    **brachium pontis**) carries the **afferent** fibers
    from the **contralateral pontine nuclei** to the
    **contralateral cerebellar cortex** — the
    **corticopontocerebellar** fibers (the **cortico-ponto-
    cerebellar** pathway — the **largest** cerebro-cerebellar
    pathway). The **middle cerebellar peduncle** is the
    **largest** of the three cerebellar peduncles.

*   **Inferior Cerebellar Peduncle (Mixed — Restiform Body +
    Juxtarestiform Body):** The **inferior cerebellar
    peduncle** carries a **mixed** set of fibers:
    *   **Restiform body** (the **larger, dorsolateral
        portion**) — the **dorsal spinocerebellar tract**
        (from **Clarke's column**), the **cuneocerebellar
        tract** (from the **accessory cuneate nucleus**),
        the **olivocerebellar fibers** (the **climbing
        fibers** from the **inferior olivary nucleus**), and
        the **reticulocerebellar fibers**.
    *   **Juxtarestiform body** (the **smaller, ventromedial
        portion**) — the **fastigial efferents** (the
        **cerebellovestibular** and **cerebelloreticular**
        projections — the **uncinate fasciculus of
        Russell**), the **vestibulocerebellar fibers**, and
        the **cerebellovestibular fibers**.

*   **NOT a neural processor.** The cerebellar peduncles do
    **not** compute, **modulate**, or **process** neural
    signals in the classical sense — they **conduct** them.
    The **processing** happens in the **cerebellum**
    (cerebellar cortex, deep nuclei) and in the
    **brainstem** (pons, medulla oblongata, midbrain). The
    **cerebellar peduncles** are the **white-matter tracts**
    that **carry** the signals.

**The unifying theme:** the cerebellar peduncles are the
**group of three paired white-matter tracts** — the
**superior cerebellar peduncle** (efferent, mostly — the
**dentate** and **interposed** efferents, the **fastigial**
efferents via the **juxtarestiform body**, the
**decussation of Wernekink**), the **middle cerebellar
peduncle** (afferent, the **largest** — the
**corticopontocerebellar** fibers), and the **inferior
cerebellar peduncle** (mixed — the **restiform body** and
the **juxtarestiform body**) — that **connect** the
**cerebellum** to the **brainstem**. They are **white-matter
tracts** (**conduction infrastructure**), **NOT neural
tissue** that processes, and **NOT the cerebellum or the
brainstem**.

Associated Disorders
--------------------
The cerebellar peduncles have **named clinical syndromes** —
their clinical associations are **cerebellar** (via the
**white-matter tracts** and the **structures they connect**):

*   **Superior Cerebellar Artery (SCA) Infarct (Superior
    Cerebellar Peduncle):** The **superior cerebellar artery
    (SCA)** **supplies** the **superior cerebellum** and the
    **superior cerebellar peduncle** — an **SCA infarct**
    can involve the **superior cerebellar peduncle** (and
    the **superior cerebellar peduncle's decussation of
    Wernekink** in the **caudal midbrain**), causing
    **ipsilateral cerebellar ataxia** (the **superior
    cerebellar syndrome**). The **superior cerebellar
    peduncle** is a **substrate**.

*   **Anterior Inferior Cerebellar Artery (AICA) Infarct
    (Middle Cerebellar Peduncle):** The **anterior inferior
    cerebellar artery (AICA)** **supplies** the **middle
    cerebellar peduncle** — an **AICA infarct** can involve
    the **middle cerebellar peduncle** (and the **lateral
    pontine** structures), causing **ipsilateral cerebellar
    ataxia**, **facial weakness**, and **hearing loss**
    (the **lateral pontine syndrome**). The **middle
    cerebellar peduncle** is a **substrate**.

*   **Posterior Inferior Cerebellar Artery (PICA) Infarct
    (Inferior Cerebellar Peduncle):** The **posterior
    inferior cerebellar artery (PICA)** **supplies** the
    **inferior cerebellar peduncle** — a **PICA infarct**
    can involve the **inferior cerebellar peduncle** (and
    the **lateral medullary** structures), causing
    **ipsilateral cerebellar ataxia**, **Horner's
    syndrome**, **loss of pain and temperature on the
    ipsilateral face and contralateral body**, and
    **dysphagia** (the **lateral medullary syndrome** —
    Wallenberg syndrome). The **inferior cerebellar
    peduncle** is a **substrate**.

*   **Multiple Sclerosis (Cerebellar Peduncles):**
    **Demyelinating plaques** in the **cerebellar
    peduncles** (superior, middle, inferior) cause
    **cerebellar ataxia**, **dysarthria**, **nystagmus**,
    and **intention tremor**. The **cerebellar peduncles**
    are **substrates**.

*   **Cerebellar Peduncle Tumors (Superior, Middle,
    Inferior):** **Tumors** — **pilocytic astrocytoma**,
    **ependymoma**, **medulloblastoma**, and **metastasis**
    — can **arise** in or **involve** the **cerebellar
    peduncles**. The **cerebellar peduncles** are
    **substrates**.

*   **Cerebellar Peduncle Lesions (Trauma, Stroke, MS,
    Tumors):** **Lesions** of the cerebellar peduncles —
    **trauma**, **stroke**, **multiple sclerosis**, and
    **tumors** — cause **cerebellar ataxia**, **dysarthria**,
    **nystagmus**, and **intention tremor** (the
    **cerebellar syndrome**). The **cerebellar peduncles**
    are **substrates**.

*   **No Named "Cerebellar Peduncle Syndrome" (singular):**
    The cerebellar peduncles have **multiple named clinical
    syndromes** (SCA infarct, AICA infarct, PICA infarct,
    multiple sclerosis, cerebellar peduncle tumors,
    cerebellar peduncle lesions) — but **no single
    "cerebellar peduncle syndrome."** Their clinical
    relevance is **cerebellar** — via the **white-matter
    tracts** and the **structures they connect**.

**What is NOT here:** The cerebellar peduncles are **not** the
substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (central nucleus + basolateral nuclei),
**Urbach-Wiethe disease** (amygdala), or **Parkinson's
disease** (substantia nigra, in the midbrain). Their clinical
relevance is **cerebellar** — **SCA infarct**, **AICA
infarct**, **PICA infarct**, **multiple sclerosis**,
**cerebellar peduncle tumors**, and **cerebellar peduncle
lesions**.

Lateralization Notes
--------------------
This is the **cerebellar peduncles** container module. The
cerebellar peduncles are **bilaterally paired** — each
peduncle has a **left** and a **right** member — and they
carry **NO warning**:

*   **Bilateral Pairing (Each Peduncle):** The **superior
    cerebellar peduncle** is **bilaterally paired** (the
    **left superior cerebellar peduncle** and the **right
    superior cerebellar peduncle**); the **middle cerebellar
    peduncle** is **bilaterally paired** (the **left middle
    cerebellar peduncle** and the **right middle cerebellar
    peduncle**); the **inferior cerebellar peduncle** is
    **bilaterally paired** (the **left inferior cerebellar
    peduncle** and the **right inferior cerebellar
    peduncle**). The tree wires the **three peduncles** as
    **three sub-containers** — **each sub-container is the
    peduncle as a bilateral pair**. The **bilateral pairing**
    is documented as **prose** within each peduncle
    sub-container.

*   **Bilateral Connectivity (Middle Cerebellar Peduncle):**
    The **middle cerebellar peduncle** is the **cerebellar
    cortex's principal input** — the **corticopontocerebellar**
    fibers — which are **contralateral**: the **left middle
    cerebellar peduncle** carries the **corticopontocerebellar**
    fibers from the **right pontine nuclei** to the **left
    cerebellar cortex**; the **right middle cerebellar
    peduncle** carries the **corticopontocerebellar** fibers
    from the **left pontine nuclei** to the **right
    cerebellar cortex**.

*   **Decussation (Superior Cerebellar Peduncle):** The
    **superior cerebellar peduncle** **decussates** in the
    **caudal midbrain** (the **decussation of Wernekink** —
    the **ventral tegmental decussation**) — the **left
    superior cerebellar peduncle** **crosses** to the
    **right** red nucleus and thalamus; the **right
    superior cerebellar peduncle** **crosses** to the
    **left** red nucleus and thalamus. The **double
    crossing** (the **corticopontocerebellar** and the
    **cerebellothalamocortical**) makes cerebellar control
    **ipsilateral**.

*   **NO Extended-Amygdala Warning (SLEA-free):** The
    cerebellar peduncles are **NOT** an extended-amygdala
    component. They carry **no SLEA warning**. Consumers
    must **not** import the SLEA warning into the cerebellar
    peduncles.

*   **NO Amygdala-Lateralization Warning:** The cerebellar
    peduncles are **NOT** the fear-output or the
    fear-learning structure. They are **white-matter
    tracts** — consumers must **not** conflate them with
    the **amygdala** or the **fear circuit**.

**A consumer that assumes "left cerebellar peduncle = right
cerebellar peduncle" will be structurally correct** — the two
sides are **symmetric** (the **bilateral pairing**, the
**bilateral connectivity** of the middle cerebellar peduncle,
and the **decussation** of the superior cerebellar peduncle
are documented as **prose**). The cerebellar peduncles carry
**NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **container** does
    **not** import from any ``left/`` or ``right/`` sub-container
    — the tree wires the cerebellar peduncles as **three
    sub-containers** (the three peduncles), each representing
    the peduncle as a bilateral pair — the container itself
    does **not** import from any left/right sub-containers.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../pons/`` (parent),
    ``.../pons/caudal_pontine_reticular_nucleus/`` (sibling),
    ``.../pons/cranial_nerve_nuclei/`` (sibling),
    ``.../pons/parabrachial_area/`` (sibling),
    ``.../pons/paramedian_pontine_reticular_formation/``
    (sibling),
    ``.../pons/parvocellular_reticular_nucleus/`` (sibling),
    ``.../pons/pontine_nuclei/`` (sibling),
    ``.../pons/superior_olivary_complex/`` (sibling),
    ``.../pons/tegmentum/`` (sibling),
    ``.../metencephalon/cerebellum/`` (the cerebellum),
    ``.../metencephalon/fourth_ventricle/`` (the fourth
    ventricle), ``.../cerebellum/deep_white_matter/`` (the
    cerebellar deep white matter),
    ``.../cerebellum/nuclei/`` (the cerebellar deep
    nuclei), ``.../midbrain/cerebral_peduncle/`` (the
    cerebral peduncle), ``.../midbrain/``, ``.../hindbrain/``,
    ``.../forebrain/``, or any other container. The
    cerebellar peduncles' relationships to the cerebellum,
    the brainstem, the fourth ventricle, the deep nuclei, the
    deep white matter, the cerebral peduncle, the pons, the
    metencephalon, the hindbrain, and the various fiber tracts
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — three structural children.** The
    ``inferior_cerebellar_peduncle/``,
    ``middle_cerebellar_peduncle/``, and
    ``superior_cerebellar_peduncle/`` are **sub-containers**
    (the three peduncles). The **fiber tracts** within each
    peduncle (the **dorsal spinocerebellar tract**, the
    **ventral spinocerebellar tract**, the
    **cuneocerebellar tract**, the
    **trigeminocerebellar tract**, the
    **corticopontocerebellar fibers**, the
    **olivocerebellar fibers**, the
    **vestibulocerebellar fibers**, the
    **reticulocerebellar fibers**, the **dentate efferents**,
    the **interposed efferents**, the **fastigial efferents**,
    the **cerebellovestibular fibers**, the
    **juxtarestiform body**, the **restiform body**, and the
    **decussation of Wernekink**) are **prose** within the
    sub-containers. Consumers must not assume any exist as
    direct children of the cerebellar peduncles container;
    resolve tract-level detail through the sub-containers
    and the references.
*   **WHITE-MATTER TRACTS — NOT the cerebellum or the
    brainstem.** The **cerebellum** is the **suprasegmental
    structure**; the **brainstem** is the **segmental
    neuraxis**; the **cerebellar peduncles** are the
    **conduction infrastructure** that **connects** them.
*   **THREE PEDUNCLES — NOT a single uniform structure.** The
    **superior cerebellar peduncle** (efferent, mostly), the
    **middle cerebellar peduncle** (afferent, the
    **largest**), and the **inferior cerebellar peduncle**
    (mixed — the **restiform body** + the
    **juxtarestiform body**) are **functionally distinct
    peduncles**.
*   **PAIRED — MULTIPLE left/right peduncles.** Each peduncle
    is **bilaterally paired**; the tree wires the **three
    peduncles** as **three sub-containers**, each
    representing the peduncle as a **bilateral pair**.
*   **CHILDREN OF THE PONS — NOT of the cerebellum or the
    brainstem.** The tree wires the cerebellar peduncles as
    **children of the pons** — the **pons "owns" the
    peduncle attachment**.
*   **NOT the fourth ventricle — a CSF cavity.** The superior
    and inferior cerebellar peduncles form the **lateral
    walls** of the fourth ventricle, but they are **NOT**
    the fourth ventricle.
*   **NOT the deep nuclei.** The **deep nuclei** are the
    **grey-matter output nuclei**; the **peduncles** are the
    **white-matter tracts** that carry their efferents.
*   **NOT the cerebellar deep white matter.** The **deep
    white matter** is the **intracerebellar white-matter
    core** (arbor vitae); the **cerebellar peduncles** are
    the **extracerebellar white-matter tracts**.
*   **NOT the cerebral peduncle.** The **cerebral peduncle**
    is the **midbrain ventral structure**; the **cerebellar
    peduncles** are the **cerebellar white-matter tracts**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **NOT a neural processor — CONDUCTION INFRASTRUCTURE.**
    The **processing** happens in the **cerebellum** and the
    **brainstem**; the **cerebellar peduncles** are the
    **white-matter tracts** that **carry** the signals.
*   **No ``AREA_PATHS`` hop.** The cerebellar peduncles are a
    **local container** under the pons, not a
    **cross-listed container**.
*   **No nested cross-listing.** The cerebellar peduncles have
    **no nested dual-framing module**. They are a **single
    container** with three sub-containers.
*   **No lateralization warning.** The cerebellar peduncles
    carry **no warning** — **no SLEA warning**, **no
    amygdala-lateralization warning**, and **no
    rhinencephalon-exclusion flag**. The **bilateral pairing**,
    the **bilateral connectivity** of the middle cerebellar
    peduncle, and the **decussation** of the superior
    cerebellar peduncle are documented as **prose**, not as a
    **warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cerebellar_peduncles import (
        inferior_cerebellar_peduncle,
        middle_cerebellar_peduncle,
        superior_cerebellar_peduncle,
    )

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles"
    )
    inferior_path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles."
        "inferior_cerebellar_peduncle"
    )
    middle_path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles."
        "middle_cerebellar_peduncle"
    )
    superior_path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles."
        "superior_cerebellar_peduncle"
    )

**Do not** assume the cerebellar peduncles are the **cerebellum**.
The **cerebellum** is the **suprasegmental structure**; the
**cerebellar peduncles** are the **white-matter tracts** that
**connect** the cerebellum to the brainstem.

**Do not** assume the cerebellar peduncles are the **brainstem**.
The **brainstem** is the **segmental neuraxis**; the
**cerebellar peduncles** are the **conduction infrastructure**
that **connects** the cerebellum to it.

**Do not** assume the cerebellar peduncles are a **single
uniform structure**. The **superior cerebellar peduncle**
(efferent, mostly), the **middle cerebellar peduncle**
(afferent, the **largest**), and the **inferior cerebellar
peduncle** (mixed) are **functionally distinct peduncles**.

**Do not** assume the cerebellar peduncles are **unpaired**.
Each peduncle is **bilaterally paired**; the tree wires the
**three peduncles** as **three sub-containers**, each
representing the peduncle as a **bilateral pair**.

**Do not** assume the cerebellar peduncles are the **fourth
ventricle**. The **superior and inferior cerebellar
peduncles** form the **lateral walls** of the fourth
ventricle, but they are **NOT** the fourth ventricle.

**Do not** assume the cerebellar peduncles are the **deep
nuclei**. The **deep nuclei** are the **grey-matter output
nuclei**; the **peduncles** are the **white-matter tracts**
that carry their efferents.

**Do not** assume the cerebellar peduncles are the
**cerebellar deep white matter**. The **deep white matter** is
the **intracerebellar white-matter core** (arbor vitae); the
**cerebellar peduncles** are the **extracerebellar
white-matter tracts**.

**Do not** assume the cerebellar peduncles are the **cerebral
peduncle**. The **cerebral peduncle** is the **midbrain
ventral structure**; the **cerebellar peduncles** are the
**cerebellar white-matter tracts**.

**Do not** assume the cerebellar peduncles are the
**pons**, **metencephalon**, **hindbrain**, **brainstem**,
**cerebellum**, or **fourth ventricle**. The **cerebellar
peduncles** are **children of the pons** (the **tree wires
them as children of the pons**) — the **white-matter tracts**
that **connect** the cerebellum to the brainstem.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the cerebellar
peduncles. **The cerebellar peduncles are SLEA-FREE** — they
are **not** an extended-amygdala component, and they are
**NOT the fear-output structure**.

Iterating the cerebellar peduncles' children (recommended
consumer pattern)::

    CEREBELLAR_PEDUNCLES_CHILDREN = (
        "inferior_cerebellar_peduncle",
        "middle_cerebellar_peduncle",
        "superior_cerebellar_peduncle",
    )
    # The three peduncles (superior, middle, inferior) are the
    # three structural children of the cerebellar peduncles
    # container. Each sub-container is the peduncle as a
    # bilateral pair (left and right).

Reaching the pons (recommended consumer pattern — the parent)::

    # The pons is the CONTAINER (the whole metencephalic
    # brainstem segment):
    #
    #   hindbrain.metencephalon.pons
    #
    # The cerebellar peduncles are CHILDREN of the pons in the
    # tree.

Reaching the cerebellum (recommended consumer pattern — NOTE
the conduction-infrastructure-vs-suprasegmental-structure
boundary)::

    # The cerebellum is the DORSAL SUPRASEGMENTAL structure:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cerebellum is the SUPRASEGMENTAL STRUCTURE; the
    # cerebellar peduncles are the CONDUCTION INFRASTRUCTURE
    # that connect it to the brainstem.

Reaching the brainstem (recommended consumer pattern — NOTE
the conduction-infrastructure-vs-segmental-neuraxis boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons
    # + medulla):
    #
    #   midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The brainstem is the SEGMENTAL NEURAXIS; the cerebellar
    # peduncles are the CONDUCTION INFRASTRUCTURE that connects
    # the cerebellum to it.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the white-matter-tract-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The superior and inferior cerebellar peduncles form the
    # LATERAL WALLS of the fourth ventricle, but they are NOT
    # the fourth ventricle.

Reaching the deep nuclei (recommended consumer pattern — NOTE
the white-matter-tract-vs-grey-matter-output-nuclei boundary)::

    # The deep nuclei are the GREY-MATTER OUTPUT NUCLEI
    # (dentate, interposed, fastigial):
    #
    #   hindbrain.metencephalon.cerebellum.nuclei
    #
    # The deep nuclei are the GREY-MATTER OUTPUT NUCLEI; the
    # cerebellar peduncles are the WHITE-MATTER TRACTS that
    # carry their efferents.

Reaching the cerebellar deep white matter (recommended
consumer pattern — NOTE the extracerebellar-vs-
intracerebellar white matter boundary)::

    # The cerebellar deep white matter is the INTRACEREBELLAR
    # white-matter core (arbor vitae):
    #
    #   hindbrain.metencephalon.cerebellum.deep_white_matter
    #
    # The deep white matter is INTRACEREBELLAR; the cerebellar
    # peduncles are EXTRACEREBELLAR.

Reaching the cerebral peduncle (recommended consumer pattern —
NOTE the cerebellar-white-matter-vs-midbrain-ventral-structure
boundary)::

    # The cerebral peduncle is the MIDBRAIN ventral structure
    # (crus cerebri + substantia nigra + tegmentum):
    #
    #   midbrain.cerebral_peduncle
    #
    # The cerebral peduncle is the MIDBRAIN ventral structure;
    # the cerebellar peduncles are the CEREBELLAR white-matter
    # tracts. The name "peduncle" is shared, but the structures
    # are different.

Reaching the superior cerebellar peduncle (recommended
consumer pattern — NOTE the efferent-peduncle boundary)::

    # The superior cerebellar peduncle (brachium conjunctivum)
    # is the EFFERENT peduncle (mostly):
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles.
    #   superior_cerebellar_peduncle
    #
    # The superior cerebellar peduncle carries the dentate and
    # interposed efferents (and, via the juxtarestiform body,
    # the fastigial efferents) and decussates in the caudal
    # midbrain (the decussation of Wernekink).

Reaching the middle cerebellar peduncle (recommended
consumer pattern — NOTE the afferent-peduncle boundary)::

    # The middle cerebellar peduncle (brachium pontis) is the
    # AFFERENT peduncle (the LARGEST peduncle):
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles.
    #   middle_cerebellar_peduncle
    #
    # The middle cerebellar peduncle carries the
    # corticopontocerebellar fibers (the pontocerebellar
    # fibers) from the contralateral pontine nuclei to the
    # contralateral cerebellar cortex.

Reaching the inferior cerebellar peduncle (recommended
consumer pattern — NOTE the mixed-peduncle boundary)::

    # The inferior cerebellar peduncle is the MIXED peduncle
    # (the restiform body + the juxtarestiform body):
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles.
    #   inferior_cerebellar_peduncle
    #
    # The inferior cerebellar peduncle carries the restiform
    # body (the dorsal spinocerebellar tract, the
    # cuneocerebellar tract, the olivocerebellar fibers, the
    # reticulocerebellar fibers) and the juxtarestiform body
    # (the fastigial efferents, the vestibulocerebellar
    # fibers, the cerebellovestibular fibers).

Fiber-tract detail (not wired at the cerebellar peduncles level
— consult the sub-containers and references)::

    # The cerebellar peduncles' fiber-tract detail is prose
    # within the sub-containers:
    #   superior_cerebellar_peduncle -> dentate efferents,
    #                                   interposed efferents,
    #                                   fastigial efferents
    #                                   (via the juxtarestiform
    #                                   body), the decussation of
    #                                   Wernekink
    #   middle_cerebellar_peduncle -> corticopontocerebellar
    #                                 fibers (the
    #                                 pontocerebellar fibers)
    #   inferior_cerebellar_peduncle -> restiform body (the
    #                                   dorsal spinocerebellar
    #                                   tract, the
    #                                   cuneocerebellar tract,
    #                                   the olivocerebellar
    #                                   fibers, the
    #                                   reticulocerebellar
    #                                   fibers) + the
    #                                   juxtarestiform body (the
    #                                   fastigial efferents, the
    #                                   vestibulocerebellar
    #                                   fibers, the
    #                                   cerebellovestibular
    #                                   fibers)
    #
    # Do not attempt to resolve these as sub-paths of the
    # cerebellar peduncles.

Bilateral iteration (recommended consumer pattern — each
peduncle is bilaterally paired)::

    # Each peduncle is bilaterally paired (left and right).
    # The tree wires the three peduncles as three sub-
    # containers, each representing the peduncle as a
    # bilateral pair. Do not attempt to resolve left/right
    # sub-paths of the cerebellar peduncles — the bilateral
    # pairing is documented as prose within each peduncle
    # sub-container.

References
----------
*   **Canonical cerebellar peduncle anatomy:** Standring, S.
    (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Cerebellum — superior,
    middle, and inferior cerebellar peduncles; the
    decussation of Wernekink; the restiform body; the
    juxtarestiform body.)
*   **Cerebellum overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Cerebellum — superior cerebellar peduncle, middle
    cerebellar peduncle, inferior cerebellar peduncle,
    cerebellar afferents and efferents.)
*   **Superior cerebellar peduncle (decussation of
    Wernekink):** Voogd, J., Glickstein, M. (1998). "The
    anatomy of the cerebellum." *Trends in Neurosciences*
    21:370–375. (Superior cerebellar peduncle — the
    efferent peduncle; the decussation of Wernekink; the
    double crossing that makes cerebellar control
    ipsilateral.)
*   **Middle cerebellar peduncle (corticopontocerebellar
    fibers):** Mihailoff, G.A., et al. (1985). "The basilar
    pontine gray of the opossum: a correlated light and
    electron microscopic analysis." *Journal of Comparative
    Neurology* 233:417–437. (Middle cerebellar peduncle —
    the corticopontocerebellar fibers — the pontocerebellar
    projection from the contralateral pontine nuclei to the
    contralateral cerebellar cortex.)
*   **Inferior cerebellar peduncle (restiform body):**
    Oscarsson, O. (1965). "Functional organization of the
    spino-cerebellar paths." In *Physiology of Spinal
    Neurons* (Eccles, J.C., Schadé, J.P., eds.). (Restiform
    body — the dorsal spinocerebellar tract, the
    cuneocerebellar tract, the olivocerebellar fibers, the
    reticulocerebellar fibers.)
*   **Juxtarestiform body (fastigial efferents):** Russell,
    J.S.R. (1897). "The origin and destination of certain
    tracts of the nervous system." *Brain* 20:350–369.
    (Juxtarestiform body — the fastigial efferents, the
    vestibulocerebellar fibers, the cerebellovestibular
    fibers.)
*   **Superior cerebellar artery (SCA) territory:**
    Savoiardo, M., et al. (1987). "Cerebellar infarcts:
    clinical and CT findings." *Journal of Neurology*
    234:256–262. (SCA — supplies the superior cerebellum
    and the superior cerebellar peduncle.)
*   **Anterior inferior cerebellar artery (AICA)
    territory:** Savoiardo, M., et al. (1987). "Cerebellar
    infarcts: clinical and CT findings." *Journal of
    Neurology* 234:256–262. (AICA — supplies the middle
    cerebellar peduncle and the lateral pons.)
*   **Posterior inferior cerebellar artery (PICA)
    territory:** Wallenberg, A. (1895). "Akute
    Bulbäraffection (Embolie der Arteria cerebelli
    posterior inferior sinistra)." *Archiv für Psychiatrie
    und Nervenkrankheiten* 27:504–540. (PICA — supplies
    the inferior cerebellar peduncle and the lateral
    medulla; lateral medullary syndrome.)
*   **Multiple sclerosis (cerebellar peduncles):** Compston,
    A., Coles, A. (2008). "Multiple sclerosis." *The
    Lancet* 372:1502–1517. (Multiple sclerosis —
    cerebellar peduncle demyelinating plaques.)
*   **SLEA (contrast — the cerebellar peduncles are NOT
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens;
    NOT the cerebellar peduncles.)
*   NeuroNames — Cerebellar peduncles; FMA — Cerebellar
    peduncles.
""""""
infrastructure.brainparts.hindbrain.metencephalon.pons.cerebellar_peduncles
===========================================================================

Anatomical Hierarchy
--------------------
::

    pons
    ├── caudal_pontine_reticular_nucleus
    ├── cerebellar_peduncles                   <-- THIS MODULE
    │   ├── inferior_cerebellar_peduncle
    │   ├── middle_cerebellar_peduncle
    │   └── superior_cerebellar_peduncle
    ├── cranial_nerve_nuclei
    ├── parabrachial_area
    ├── paramedian_pontine_reticular_formation
    ├── parvocellular_reticular_nucleus
    ├── pontine_nuclei
    ├── superior_olivary_complex
    └── tegmentum

**Primary synonym:** Cerebellar peduncles; pedunculi cerebellares;
the cerebellar stalks; the cerebellar peduncles (as a group); the
three cerebellar peduncles; the peduncles of the cerebellum;
the superior / middle / inferior cerebellar peduncles (as a
set); the cerebellar white-matter peduncles.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
grey-matter structure.** A **group of three paired white-matter
tracts** — the **superior cerebellar peduncle (brachium
conjunctivum)**, the **middle cerebellar peduncle (brachium
pontis)**, and the **inferior cerebellar peduncle (restiform
body + juxtarestiform body)** — that **connect** the cerebellum
to the **brainstem** (midbrain, pons, medulla oblongata) and
**carry** the **afferent** and **efferent** fibers of the
cerebellum.
**Part of:** The **pons** container — the **white-matter
peduncles** that **attach** the cerebellum to the brainstem
(the tree wires the cerebellar peduncles as **children of the
pons**, **not** of the cerebellum — see *Boundary status*).
The **pons** is a **child sub-container of the metencephalon**;
the **metencephalon** is the **rostral** of the **two
rhombencephalic sub-vesicles**; the **hindbrain** is the
**caudal** of the **three primary brain vesicles**.
**Structural parent:** ``.../pons/`` → **direct child** of the
pons container.
**Structural children:** **Three** — ``inferior_cerebellar_
peduncle/``, ``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/``. Each is a **sub-container**
(the **peduncle itself**), comprising the **white-matter
fibers** of that peduncle. The **superior cerebellar peduncle
(decussation of Wernekink)**, the **middle cerebellar peduncle
(pontocerebellar fibers)**, the **inferior cerebellar peduncle
(restiform body + juxtarestiform body)**, the **specific
fiber tracts** within each peduncle (the **dorsal
spinocerebellar tract**, the **ventral spinocerebellar
tract**, the **cuneocerebellar tract**, the **trigemino-
cerebellar tract**, the **corticopontocerebellar fibers**,
the **olivocerebellar fibers**, the **vestibulocerebellar
fibers**, the **reticulocerebellar fibers**, the **superior
cerebellar peduncle efferents** from the **dentate**,
**interposed**, and **fastigial nuclei**, the **juxtarestiform
body**), and the **decussation of Wernekink** (the **superior
cerebellar peduncle decussation** — the **ventral tegmental
decussation** of the **superior cerebellar peduncle** in the
**caudal midbrain**) are documented as **prose**, not as
structural children of the cerebellar peduncles container.
**Boundary status (PEDUNCLES — NOT the cerebellum):** **Boundary
case — the cerebellar peduncles are the WHITE-MATTER TRACTS
that CONNECT the cerebellum to the brainstem, NOT the
cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is the **dorsal
suprasegmental structure** — the **lateral hemispheres** and
the **midline vermis**, with the **cortical divisions** and
the **deep nuclei**. The **cerebellar peduncles** (here) are
the **white-matter tracts** that **connect** the cerebellum
to the brainstem — the **conduction infrastructure** that
**carries** the cerebellar afferents and efferents. **The
cerebellum is the SUPRASEGMENTAL STRUCTURE; the cerebellar
peduncles are the CONDUCTION INFRASTRUCTURE.** Consumers must
**not** conflate the cerebellar peduncles with the cerebellum
— the **peduncles** are the **tracts**; the **cerebellum**
is the **structure** they **connect**.
**Boundary status (PEDUNCLES AS A GROUP — NOT a single
peduncle):** **Boundary case — the cerebellar peduncles as a
group are the SET of three peduncles, NOT a single
peduncle.** The **cerebellar peduncles** container (here) is
the **group of three peduncles** — the **superior cerebellar
peduncle** (``.../cerebellar_peduncles/superior_cerebellar_
peduncle/``), the **middle cerebellar peduncle**
(``.../cerebellar_peduncles/middle_cerebellar_peduncle/``),
and the **inferior cerebellar peduncle**
(``.../cerebellar_peduncles/inferior_cerebellar_peduncle/``).
**The container is the GROUP; each peduncle is a MEMBER of the
group.** Consumers must **not** conflate the cerebellar
peduncles as a group with any single peduncle — the
**superior**, **middle**, and **inferior** cerebellar
peduncles are **distinct peduncles** with **distinct
fiber content** and **distinct functions**.
**Boundary status (PEDUNCLES — NOT the brainstem):** **Boundary
case — the cerebellar peduncles are the WHITE-MATTER TRACTS
that ATTACH the cerebellum to the brainstem, NOT the
brainstem.** The **brainstem** is the **segmental neuraxis**
(midbrain + pons + medulla oblongata) — the **neural tissue**
that the cerebellar peduncles **attach** the cerebellum to.
The **cerebellar peduncles** (here) are the **white-matter
tracts** that **connect** the cerebellum to the brainstem —
the **conduction infrastructure**. **The brainstem is the
SEGMENTAL NEURAXIS; the cerebellar peduncles are the
CONDUCTION INFRASTRUCTURE that connects the cerebellum to
it.** Consumers must **not** conflate the cerebellar
peduncles with the brainstem — the **peduncles** are the
**tracts**; the **brainstem** is the **neural tissue**.
**Boundary status (PEDUNCLES — NOT the fourth ventricle):**
**Boundary case — the cerebellar peduncles are the WHITE-MATTER
TRACTS, NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **cerebellar peduncles** (here) are the
**white-matter tracts** that **attach** the cerebellum to
the brainstem — the **tracts** that **form the lateral
walls** of the fourth ventricle (the **superior cerebellar
peduncle** forms the **lateral wall** of the **rostral fourth
ventricle**; the **inferior cerebellar peduncle** forms the
**lateral wall** of the **caudal fourth ventricle**). **The
peduncles are the TRACTS; the fourth ventricle is the CSF
CAVITY that the peduncles are ADJACENT to.** Consumers must
**not** conflate the cerebellar peduncles with the fourth
ventricle.
**Boundary status (PEDUNCLES — NOT the deep nuclei):** **Boundary
case — the cerebellar peduncles are the WHITE-MATTER TRACTS,
NOT the deep nuclei.** The **cerebellar deep nuclei**
(``.../cerebellum/nuclei/``) — the **dentate nucleus**, the
**interposed nucleus** (the **emboliform nucleus** + the
**globose nucleus**), and the **fastigial nucleus** — are
the **grey-matter output nuclei** of the cerebellum. The
**cerebellar peduncles** (here) are the **white-matter
tracts** that **carry** the **efferents** of the cerebellar
deep nuclei (the **superior cerebellar peduncle** carries the
**dentate** and **interposed** efferents; the **inferior
cerebellar peduncle** — the **juxtarestiform body** — carries
the **fastigial** efferents). **The deep nuclei are the
GREY-MATTER OUTPUT NUCLEI; the cerebellar peduncles are the
WHITE-MATTER TRACTS that carry their efferents.** Consumers
must **not** conflate the cerebellar peduncles with the
cerebellar deep nuclei.
**Boundary status (PEDUNCLES — NOT the cerebellar white
matter):** **Boundary case — the cerebellar peduncles are the
WHITE-MATTER TRACTS that CONNECT the cerebellum to the
brainstem, NOT the cerebellar deep white matter (the arbor
vitae).** The **cerebellar deep white matter**
(``.../cerebellum/deep_white_matter/``) is the **white-matter
core** of the cerebellum — the **arbor vitae** and the
**intracerebellar tracts**. The **cerebellar peduncles**
(here) are the **white-matter tracts** that **attach** the
cerebellum to the brainstem — the **extracerebellar white
matter** that **connects** the cerebellar white matter (the
arbor vitae) to the brainstem. **The deep white matter is
INTRACEREBELLAR; the cerebellar peduncles are EXTRACEREBELLAR
(they connect the cerebellum to the brainstem).** Consumers
must **not** conflate the cerebellar peduncles with the
cerebellar deep white matter — the **deep white matter** is
the **arbor vitae**; the **peduncles** are the **extracerebellar
white-matter tracts**.
**Boundary status (PEDUNCLES — NOT the cerebral peduncle):**
**Boundary case — the cerebellar peduncles are the CEREBELLAR
WHITE-MATTER TRACTS, NOT the cerebral peduncle.** The
**cerebral peduncle** (``.../midbrain/cerebral_peduncle/``)
is the **midbrain** structure — the **ventral midbrain**
(crus cerebri + substantia nigra + tegmentum) that **contains**
the **corticospinal**, **corticobulbar**, and
**corticopontine** tracts. The **cerebellar peduncles**
(here) are the **cerebellar** white-matter tracts that
**connect** the cerebellum to the brainstem. **They are
DIFFERENT PEDUNCLES** — the **cerebral peduncle** is the
**midbrain ventral structure**; the **cerebellar peduncles**
are the **cerebellar white-matter tracts** (superior,
middle, inferior). The name **"peduncle"** is **shared**
(both are "peduncles"), but the **structures are different**
— consumers must **not** conflate the cerebellar peduncles
with the cerebral peduncle.
**Boundary status (THREE PEDUNCLES — NOT a single uniform
structure):** **Boundary case — the cerebellar peduncles are
a GROUP of THREE peduncles (superior, middle, inferior),
each with DISTINCT fiber content and DISTINCT functions,
not a single uniform structure.** The **superior cerebellar
peduncle** (``.../cerebellar_peduncles/superior_cerebellar_
peduncle/``) is the **efferent** peduncle (the **dentate**,
**interposed**, and (via the **juxtarestiform body**) the
**fastigial** efferents — the **superior cerebellar
peduncle** — the **decussation of Wernekink**). The
**middle cerebellar peduncle**
(``.../cerebellar_peduncles/middle_cerebellar_peduncle/``) is
the **afferent** peduncle (the **corticopontocerebellar**
fibers — the **pontocerebellar** fibers — the **largest**
peduncle). The **inferior cerebellar peduncle**
(``.../cerebellar_peduncles/inferior_cerebellar_peduncle/``)
is the **mixed** peduncle — the **restiform body** (the
**dorsal spinocerebellar tract**, the **cuneocerebellar
tract**, the **olivocerebellar fibers**, the
**reticulocerebellar fibers**) + the **juxtarestiform body**
(the **fastigial efferents**, the **vestibulocerebellar
fibers**, the **cerebellovestibular fibers**). **Each
peduncle has a distinct fiber content and a distinct
function** — the tree wires the **inferior_cerebellar_
peduncle/``**, ``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/`` as **sub-containers** of
the cerebellar peduncles. Consumers must **not** treat the
cerebellar peduncles as a single uniform structure — they
are a **group of three functionally distinct peduncles**.
**Boundary status (PAIRED — MULTIPLE left/right peduncles):**
**Boundary case — the cerebellar peduncles are PAIRED (left
and right), with THREE PEDUNCLES PER SIDE (the left superior,
the right superior, the left middle, the right middle, the
left inferior, and the right inferior cerebellar peduncles).**
The cerebellar peduncles container (here) is the **group of
three peduncles** — each peduncle is **bilaterally paired**
(the **left** and **right** superior cerebellar peduncles;
the **left** and **right** middle cerebellar peduncles; the
**left** and **right** inferior cerebellar peduncles). The
tree wires the **inferior_cerebellar_peduncle/``**,
``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/`` as **sub-containers** of
the cerebellar peduncles — **each sub-container is the
peduncle as a bilateral pair** (the left and right peduncle
of that name). The **bilateral pairing** is documented as
**prose** within each peduncle sub-container. Consumers must
**not** treat the cerebellar peduncles as a **single
unpaired structure** — they are **paired** (left and right)
for each of the **three peduncles**.
**Boundary status (PONS — NOT the cerebellum or the
brainstem):** **Boundary case — the cerebellar peduncles are
CHILDREN of the PONS, NOT of the cerebellum or the
brainstem.** The tree wires the **cerebellar peduncles** as
**children of the pons** (``.../pons/cerebellar_peduncles/``),
**not** of the cerebellum
(``.../metencephalon/cerebellum/``) or the brainstem (which
is not a single container in this tree). **The pons "owns"
the peduncle attachment** — the peduncles are the
**white-matter tracts** that **attach** the cerebellum to
the brainstem, and the tree places them under the **pons**
(the rostral brainstem segment that the peduncles are most
closely associated with — the **middle cerebellar peduncle**
is the **pontine** peduncle). Consumers must **not** treat
the cerebellar peduncles as children of the cerebellum — the
**tree wires them as children of the pons**.
**Boundary status (SLEA-FREE — the cerebellar peduncles are
NOT an extended-amygdala component):** **Boundary case — the
cerebellar peduncles are SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA
component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **cerebellar peduncles** are **white-matter
tracts** — they are **NOT** an extended-amygdala component,
and they carry **NO SLEA warning**. Consumers must **not**
import the SLEA warning into the cerebellar peduncles — they
are **SLEA-free**.
**Boundary status (CONDUCTION INFRASTRUCTURE — NOT a neural
processor):** **Boundary case — the cerebellar peduncles are
CONDUCTION INFRASTRUCTURE, NOT a neural processor.** They do
**not** compute, **modulate**, or **process** neural signals
in the classical sense — they **conduct** them. The
**processing** happens in the **cerebellum** (cerebellar
cortex, deep nuclei) and in the **brainstem** (pons,
medulla oblongata, midbrain). The **cerebellar peduncles**
are the **white-matter tracts** that **carry** the signals
between the cerebellum and the brainstem. Consumers must
**not** treat the cerebellar peduncles as a **grey-matter
processing structure** — they are **white matter**.

Overview
--------
The cerebellar peduncles are the **group of three paired
white-matter tracts** that **connect** the cerebellum to the
**brainstem** — the **superior cerebellar peduncle (brachium
conjunctivum)**, the **middle cerebellar peduncle (brachium
pontis)**, and the **inferior cerebellar peduncle (restiform
body + juxtarestiform body)**. They are a **container module**
with **three structural sub-containers**
(``inferior_cerebellar_peduncle/``,
``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/``), **each representing the
peduncle as a bilateral pair** (left and right).

**The cerebellar peduncles are the CONDUCTION INFRASTRUCTURE
between the cerebellum and the brainstem, NOT the cerebellum
and NOT the brainstem.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is the **dorsal
suprasegmental structure**; the **brainstem** is the
**segmental neuraxis** (midbrain + pons + medulla oblongata);
the **cerebellar peduncles** (here) are the **white-matter
tracts** that **connect** them. **The peduncles are the
tracts; the cerebellum and the brainstem are the structures
they connect.**

**The cerebellar peduncles are a GROUP of THREE peduncles, each
with DISTINCT fiber content and DISTINCT functions.** The
**superior cerebellar peduncle** is the **efferent** peduncle
(mostly); the **middle cerebellar peduncle** is the
**afferent** peduncle (the **largest** peduncle — the
**corticopontocerebellar** fibers); the **inferior cerebellar
peduncle** is the **mixed** peduncle (the **restiform body**
= **spinocerebellar**, **cuneocerebellar**,
**olivocerebellar**, **reticulocerebellar**; the
**juxtarestiform body** = **fastigial efferents**,
**vestibulocerebellar**, **cerebellovestibular**).

**The cerebellar peduncles are PAIRED — each peduncle has a
LEFT and a RIGHT member.** The **left superior cerebellar
peduncle** and the **right superior cerebellar peduncle**;
the **left middle cerebellar peduncle** and the **right
middle cerebellar peduncle**; the **left inferior cerebellar
peduncle** and the **right inferior cerebellar peduncle**.
The tree wires the **three peduncles** as **three
sub-containers**, each representing the **peduncle as a
bilateral pair**.

**The cerebellar peduncles are CHILDREN of the PONS in the
tree.** The tree wires the cerebellar peduncles as
**children of the pons** (``.../pons/cerebellar_peduncles/``)
— **not** of the cerebellum or the brainstem. The **pons
"owns" the peduncle attachment** — the **middle cerebellar
peduncle** is the **pontine peduncle** (the **brachium
pontis**), and the tree wires all three peduncles under the
**pons**.

Cerebellar Peduncles Composition (sub-containers and prose)
----------------------------------------------------------
The cerebellar peduncles are a **group of three paired
white-matter tracts** with **three sub-containers** —
documented as **structural children**
(``inferior_cerebellar_peduncle/``,
``middle_cerebellar_peduncle/``, and
``superior_cerebellar_peduncle/``) — and **many prose-defined
sub-structures** documented within those sub-containers:

*   **Superior cerebellar peduncle (brachium conjunctivum)**
    (``.../cerebellar_peduncles/superior_cerebellar_peduncle/``)
    — the **efferent** peduncle (mostly) — the **superior
    cerebellar peduncle** (the **brachium conjunctivum**).
    Documented as a **structural child**. Its **fiber
    content** (the **dentate** and **interposed** efferents;
    the **fastigial** efferents via the **juxtarestiform
    body**; the **decussation of Wernekink** — the **ventral
    tegmental decussation** of the superior cerebellar
    peduncle in the **caudal midbrain**) is documented as
    **prose** within the **superior_cerebellar_peduncle/`**
    sub-container.

*   **Middle cerebellar peduncle (brachium pontis)**
    (``.../cerebellar_peduncles/middle_cerebellar_peduncle/``)
    — the **afferent** peduncle (the **largest** peduncle) —
    the **middle cerebellar peduncle** (the **brachium
    pontis**). Documented as a **structural child**. Its
    **fiber content** (the **corticopontocerebellar**
    fibers — the **pontocerebellar** fibers — from the
    **contralateral pontine nuclei** to the **contralateral
    cerebellar cortex**) is documented as **prose** within
    the **middle_cerebellar_peduncle/`** sub-container.

*   **Inferior cerebellar peduncle (restiform body +
    juxtarestiform body)**
    (``.../cerebellar_peduncles/inferior_cerebellar_peduncle/``)
    — the **mixed** peduncle — the **inferior cerebellar
    peduncle** (the **restiform body** = the **dorsal
    spinocerebellar tract**, the **cuneocerebellar tract**,
    the **olivocerebellar fibers**, the **reticulocerebellar
    fibers**; the **juxtarestiform body** = the **fastigial
    efferents**, the **vestibulocerebellar fibers**, the
    **cerebellovestibular fibers**). Documented as a
    **structural child**. Its **fiber content** (the
    **restiform body** + the **juxtarestiform body**) is
    documented as **prose** within the
    **inferior_cerebellar_peduncle/`** sub-container.

**These fiber contents are prose, not structural children of
the cerebellar peduncles container.** The tree wires the
**cerebellar peduncles** as a **container** with **three
sub-containers** (the **three peduncles**) — the **fiber
tracts** (the **dorsal spinocerebellar tract**, the
**ventral spinocerebellar tract**, the **cuneocerebellar
tract**, the **trigeminocerebellar tract**, the
**corticopontocerebellar fibers**, the **olivocerebellar
fibers**, the **vestibulocerebellar fibers**, the
**reticulocerebellar fibers**, the **dentate efferents**,
the **interposed efferents**, the **fastigial efferents**,
the **cerebellovestibular fibers**, the **juxtarestiform
body**, and the **decussation of Wernekink**) are
documented as **prose** within the **sub-containers**.
Consumers that need **tract-level** resolution should consult
the **sub-container modules** and the references, not the
cerebellar peduncles container.

The Cerebellar Peduncles / Cerebellum Boundary
----------------------------------------------
This is the **conduction-infrastructure-vs-suprasegmental-
structure** boundary:

*   **Cerebellar peduncles** (this module) — the
    **white-matter tracts** that **connect** the cerebellum
    to the brainstem.

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — the
    **dorsal suprasegmental structure**.

**The cerebellum is the SUPRASEGMENTAL STRUCTURE; the cerebellar
peduncles are the CONDUCTION INFRASTRUCTURE.** Consumers must
**not** conflate the cerebellar peduncles with the cerebellum.

The Cerebellar Peduncles / Brainstem Boundary
---------------------------------------------
This is the **conduction-infrastructure-vs-segmental-neuraxis**
boundary:

*   **Cerebellar peduncles** (this module) — the
    **white-matter tracts** that **connect** the cerebellum
    to the brainstem.

*   **Brainstem** (midbrain + pons + medulla oblongata) — the
    **segmental neuraxis**.

**The brainstem is the SEGMENTAL NEURAXIS; the cerebellar
peduncles are the CONDUCTION INFRASTRUCTURE that connects the
cerebellum to it.** Consumers must **not** conflate the
cerebellar peduncles with the brainstem.

The Cerebellar Peduncles / Fourth Ventricle Boundary
----------------------------------------------------
This is the **white-matter-tract-vs-CSF-cavity** boundary:

*   **Cerebellar peduncles** (this module) — the **white-matter
    tracts**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The peduncles are the TRACTS; the fourth ventricle is the CSF
CAVITY that the peduncles are ADJACENT to (the superior and
inferior cerebellar peduncles form the lateral walls of the
fourth ventricle).** Consumers must **not** conflate the
cerebellar peduncles with the fourth ventricle.

The Cerebellar Peduncles / Deep Nuclei Boundary
-----------------------------------------------
This is the **white-matter-tract-vs-grey-matter-output-nuclei**
boundary:

*   **Cerebellar peduncles** (this module) — the **white-matter
    tracts**.

*   **Cerebellar deep nuclei** (``.../cerebellum/nuclei/``) —
    the **grey-matter output nuclei** (dentate, interposed,
    fastigial).

**The deep nuclei are the GREY-MATTER OUTPUT NUCLEI; the
cerebellar peduncles are the WHITE-MATTER TRACTS that carry
their efferents.** Consumers must **not** conflate the
cerebellar peduncles with the cerebellar deep nuclei.

The Cerebellar Peduncles / Cerebellar Deep White Matter Boundary
----------------------------------------------------------------
This is the **extracerebellar-vs-intracerebellar white
matter** boundary:

*   **Cerebellar peduncles** (this module) — the
    **extracerebellar white-matter tracts** that **connect**
    the cerebellum to the brainstem.

*   **Cerebellar deep white matter**
    (``.../cerebellum/deep_white_matter/``) — the
    **intracerebellar white-matter core** (arbor vitae).

**The deep white matter is INTRACEREBELLAR; the cerebellar
peduncles are EXTRACEREBELLAR.** Consumers must **not**
conflate the cerebellar peduncles with the cerebellar deep
white matter.

The Cerebellar Peduncles / Cerebral Peduncle Boundary
-----------------------------------------------------
This is the **cerebellar-white-matter-vs-midbrain-ventral-
structure** boundary:

*   **Cerebellar peduncles** (this module) — the **cerebellar**
    white-matter tracts (superior, middle, inferior).

*   **Cerebral peduncle**
    (``.../midbrain/cerebral_peduncle/``) — the **midbrain
    ventral structure** (crus cerebri + substantia nigra +
    tegmentum).

**They are DIFFERENT PEDUNCLES** — the **cerebral peduncle** is
the **midbrain ventral structure**; the **cerebellar
peduncles** are the **cerebellar white-matter tracts**. The
name **"peduncle"** is **shared**, but the **structures are
different**. Consumers must **not** conflate the cerebellar
peduncles with the cerebral peduncle.

The Cerebellar Peduncles / Pons Boundary
----------------------------------------
This is the **child-vs-container** boundary:

*   **Cerebellar peduncles** (this module) — **children of the
    pons** in the tree.

*   **Pons** (``.../pons/``) — the **container** (the whole
    metencephalic brainstem segment).

**The cerebellar peduncles are CHILDREN of the pons in the
tree** — the **pons "owns" the peduncle attachment**.
Consumers must **not** treat the cerebellar peduncles as
children of the cerebellum or the brainstem — the **tree
wires them as children of the pons**.

The Cerebellar Peduncles / SLEA Boundary
----------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cerebellar peduncles** (this module) — **SLEA-FREE**.
    No extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**,
    **ventral pallidum**, and **nucleus accumbens** (wired
    elsewhere).

**The cerebellar peduncles are NOT part of the SLEA
continuum.** They are **white-matter tracts**, and they carry
**no SLEA warning**. Consumers must **not** import the SLEA
warning into the cerebellar peduncles.

Function in the Human Brain
---------------------------
The cerebellar peduncles' functions are **conduction** — the
**carriage** of **afferent** and **efferent** signals
between the cerebellum and the brainstem — **NOT neural
processing**:

*   **Superior Cerebellar Peduncle (Efferent — Mostly):** The
    **superior cerebellar peduncle** carries the **efferent**
    fibers from the **dentate nucleus** and the **interposed
    nucleus** (the **cerebellothalamocortical** and
    **cerebellorubral** projections) — and, via the
    **juxtarestiform body** (part of the **inferior
    cerebellar peduncle**), the **fastigial nucleus
    efferents** (the **cerebellovestibular** and
    **cerebelloreticular** projections). The **superior
    cerebellar peduncle** **decussates** in the **caudal
    midbrain** (the **decussation of Wernekink** — the
    **ventral tegmental decussation**) — the **cerebellar
    efferents cross** to the **contralateral** side. The
    **double crossing** (the **corticopontocerebellar** and
    the **cerebellothalamocortical**) makes cerebellar
    control **ipsilateral**.

*   **Middle Cerebellar Peduncle (Afferent — the Largest
    Peduncle):** The **middle cerebellar peduncle** (the
    **brachium pontis**) carries the **afferent** fibers
    from the **contralateral pontine nuclei** to the
    **contralateral cerebellar cortex** — the
    **corticopontocerebellar** fibers (the **cortico-ponto-
    cerebellar** pathway — the **largest** cerebro-cerebellar
    pathway). The **middle cerebellar peduncle** is the
    **largest** of the three cerebellar peduncles.

*   **Inferior Cerebellar Peduncle (Mixed — Restiform Body +
    Juxtarestiform Body):** The **inferior cerebellar
    peduncle** carries a **mixed** set of fibers:
    *   **Restiform body** (the **larger, dorsolateral
        portion**) — the **dorsal spinocerebellar tract**
        (from **Clarke's column**), the **cuneocerebellar
        tract** (from the **accessory cuneate nucleus**),
        the **olivocerebellar fibers** (the **climbing
        fibers** from the **inferior olivary nucleus**), and
        the **reticulocerebellar fibers**.
    *   **Juxtarestiform body** (the **smaller, ventromedial
        portion**) — the **fastigial efferents** (the
        **cerebellovestibular** and **cerebelloreticular**
        projections — the **uncinate fasciculus of
        Russell**), the **vestibulocerebellar fibers**, and
        the **cerebellovestibular fibers**.

*   **NOT a neural processor.** The cerebellar peduncles do
    **not** compute, **modulate**, or **process** neural
    signals in the classical sense — they **conduct** them.
    The **processing** happens in the **cerebellum**
    (cerebellar cortex, deep nuclei) and in the
    **brainstem** (pons, medulla oblongata, midbrain). The
    **cerebellar peduncles** are the **white-matter tracts**
    that **carry** the signals.

**The unifying theme:** the cerebellar peduncles are the
**group of three paired white-matter tracts** — the
**superior cerebellar peduncle** (efferent, mostly — the
**dentate** and **interposed** efferents, the **fastigial**
efferents via the **juxtarestiform body**, the
**decussation of Wernekink**), the **middle cerebellar
peduncle** (afferent, the **largest** — the
**corticopontocerebellar** fibers), and the **inferior
cerebellar peduncle** (mixed — the **restiform body** and
the **juxtarestiform body**) — that **connect** the
**cerebellum** to the **brainstem**. They are **white-matter
tracts** (**conduction infrastructure**), **NOT neural
tissue** that processes, and **NOT the cerebellum or the
brainstem**.

Associated Disorders
--------------------
The cerebellar peduncles have **named clinical syndromes** —
their clinical associations are **cerebellar** (via the
**white-matter tracts** and the **structures they connect**):

*   **Superior Cerebellar Artery (SCA) Infarct (Superior
    Cerebellar Peduncle):** The **superior cerebellar artery
    (SCA)** **supplies** the **superior cerebellum** and the
    **superior cerebellar peduncle** — an **SCA infarct**
    can involve the **superior cerebellar peduncle** (and
    the **superior cerebellar peduncle's decussation of
    Wernekink** in the **caudal midbrain**), causing
    **ipsilateral cerebellar ataxia** (the **superior
    cerebellar syndrome**). The **superior cerebellar
    peduncle** is a **substrate**.

*   **Anterior Inferior Cerebellar Artery (AICA) Infarct
    (Middle Cerebellar Peduncle):** The **anterior inferior
    cerebellar artery (AICA)** **supplies** the **middle
    cerebellar peduncle** — an **AICA infarct** can involve
    the **middle cerebellar peduncle** (and the **lateral
    pontine** structures), causing **ipsilateral cerebellar
    ataxia**, **facial weakness**, and **hearing loss**
    (the **lateral pontine syndrome**). The **middle
    cerebellar peduncle** is a **substrate**.

*   **Posterior Inferior Cerebellar Artery (PICA) Infarct
    (Inferior Cerebellar Peduncle):** The **posterior
    inferior cerebellar artery (PICA)** **supplies** the
    **inferior cerebellar peduncle** — a **PICA infarct**
    can involve the **inferior cerebellar peduncle** (and
    the **lateral medullary** structures), causing
    **ipsilateral cerebellar ataxia**, **Horner's
    syndrome**, **loss of pain and temperature on the
    ipsilateral face and contralateral body**, and
    **dysphagia** (the **lateral medullary syndrome** —
    Wallenberg syndrome). The **inferior cerebellar
    peduncle** is a **substrate**.

*   **Multiple Sclerosis (Cerebellar Peduncles):**
    **Demyelinating plaques** in the **cerebellar
    peduncles** (superior, middle, inferior) cause
    **cerebellar ataxia**, **dysarthria**, **nystagmus**,
    and **intention tremor**. The **cerebellar peduncles**
    are **substrates**.

*   **Cerebellar Peduncle Tumors (Superior, Middle,
    Inferior):** **Tumors** — **pilocytic astrocytoma**,
    **ependymoma**, **medulloblastoma**, and **metastasis**
    — can **arise** in or **involve** the **cerebellar
    peduncles**. The **cerebellar peduncles** are
    **substrates**.

*   **Cerebellar Peduncle Lesions (Trauma, Stroke, MS,
    Tumors):** **Lesions** of the cerebellar peduncles —
    **trauma**, **stroke**, **multiple sclerosis**, and
    **tumors** — cause **cerebellar ataxia**, **dysarthria**,
    **nystagmus**, and **intention tremor** (the
    **cerebellar syndrome**). The **cerebellar peduncles**
    are **substrates**.

*   **No Named "Cerebellar Peduncle Syndrome" (singular):**
    The cerebellar peduncles have **multiple named clinical
    syndromes** (SCA infarct, AICA infarct, PICA infarct,
    multiple sclerosis, cerebellar peduncle tumors,
    cerebellar peduncle lesions) — but **no single
    "cerebellar peduncle syndrome."** Their clinical
    relevance is **cerebellar** — via the **white-matter
    tracts** and the **structures they connect**.

**What is NOT here:** The cerebellar peduncles are **not** the
substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (central nucleus + basolateral nuclei),
**Urbach-Wiethe disease** (amygdala), or **Parkinson's
disease** (substantia nigra, in the midbrain). Their clinical
relevance is **cerebellar** — **SCA infarct**, **AICA
infarct**, **PICA infarct**, **multiple sclerosis**,
**cerebellar peduncle tumors**, and **cerebellar peduncle
lesions**.

Lateralization Notes
--------------------
This is the **cerebellar peduncles** container module. The
cerebellar peduncles are **bilaterally paired** — each
peduncle has a **left** and a **right** member — and they
carry **NO warning**:

*   **Bilateral Pairing (Each Peduncle):** The **superior
    cerebellar peduncle** is **bilaterally paired** (the
    **left superior cerebellar peduncle** and the **right
    superior cerebellar peduncle**); the **middle cerebellar
    peduncle** is **bilaterally paired** (the **left middle
    cerebellar peduncle** and the **right middle cerebellar
    peduncle**); the **inferior cerebellar peduncle** is
    **bilaterally paired** (the **left inferior cerebellar
    peduncle** and the **right inferior cerebellar
    peduncle**). The tree wires the **three peduncles** as
    **three sub-containers** — **each sub-container is the
    peduncle as a bilateral pair**. The **bilateral pairing**
    is documented as **prose** within each peduncle
    sub-container.

*   **Bilateral Connectivity (Middle Cerebellar Peduncle):**
    The **middle cerebellar peduncle** is the **cerebellar
    cortex's principal input** — the **corticopontocerebellar**
    fibers — which are **contralateral**: the **left middle
    cerebellar peduncle** carries the **corticopontocerebellar**
    fibers from the **right pontine nuclei** to the **left
    cerebellar cortex**; the **right middle cerebellar
    peduncle** carries the **corticopontocerebellar** fibers
    from the **left pontine nuclei** to the **right
    cerebellar cortex**.

*   **Decussation (Superior Cerebellar Peduncle):** The
    **superior cerebellar peduncle** **decussates** in the
    **caudal midbrain** (the **decussation of Wernekink** —
    the **ventral tegmental decussation**) — the **left
    superior cerebellar peduncle** **crosses** to the
    **right** red nucleus and thalamus; the **right
    superior cerebellar peduncle** **crosses** to the
    **left** red nucleus and thalamus. The **double
    crossing** (the **corticopontocerebellar** and the
    **cerebellothalamocortical**) makes cerebellar control
    **ipsilateral**.

*   **NO Extended-Amygdala Warning (SLEA-free):** The
    cerebellar peduncles are **NOT** an extended-amygdala
    component. They carry **no SLEA warning**. Consumers
    must **not** import the SLEA warning into the cerebellar
    peduncles.

*   **NO Amygdala-Lateralization Warning:** The cerebellar
    peduncles are **NOT** the fear-output or the
    fear-learning structure. They are **white-matter
    tracts** — consumers must **not** conflate them with
    the **amygdala** or the **fear circuit**.

**A consumer that assumes "left cerebellar peduncle = right
cerebellar peduncle" will be structurally correct** — the two
sides are **symmetric** (the **bilateral pairing**, the
**bilateral connectivity** of the middle cerebellar peduncle,
and the **decussation** of the superior cerebellar peduncle
are documented as **prose**). The cerebellar peduncles carry
**NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **container** does
    **not** import from any ``left/`` or ``right/`` sub-container
    — the tree wires the cerebellar peduncles as **three
    sub-containers** (the three peduncles), each representing
    the peduncle as a bilateral pair — the container itself
    does **not** import from any left/right sub-containers.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../pons/`` (parent),
    ``.../pons/caudal_pontine_reticular_nucleus/`` (sibling),
    ``.../pons/cranial_nerve_nuclei/`` (sibling),
    ``.../pons/parabrachial_area/`` (sibling),
    ``.../pons/paramedian_pontine_reticular_formation/``
    (sibling),
    ``.../pons/parvocellular_reticular_nucleus/`` (sibling),
    ``.../pons/pontine_nuclei/`` (sibling),
    ``.../pons/superior_olivary_complex/`` (sibling),
    ``.../pons/tegmentum/`` (sibling),
    ``.../metencephalon/cerebellum/`` (the cerebellum),
    ``.../metencephalon/fourth_ventricle/`` (the fourth
    ventricle), ``.../cerebellum/deep_white_matter/`` (the
    cerebellar deep white matter),
    ``.../cerebellum/nuclei/`` (the cerebellar deep
    nuclei), ``.../midbrain/cerebral_peduncle/`` (the
    cerebral peduncle), ``.../midbrain/``, ``.../hindbrain/``,
    ``.../forebrain/``, or any other container. The
    cerebellar peduncles' relationships to the cerebellum,
    the brainstem, the fourth ventricle, the deep nuclei, the
    deep white matter, the cerebral peduncle, the pons, the
    metencephalon, the hindbrain, and the various fiber tracts
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — three structural children.** The
    ``inferior_cerebellar_peduncle/``,
    ``middle_cerebellar_peduncle/``, and
    ``superior_cerebellar_peduncle/`` are **sub-containers**
    (the three peduncles). The **fiber tracts** within each
    peduncle (the **dorsal spinocerebellar tract**, the
    **ventral spinocerebellar tract**, the
    **cuneocerebellar tract**, the
    **trigeminocerebellar tract**, the
    **corticopontocerebellar fibers**, the
    **olivocerebellar fibers**, the
    **vestibulocerebellar fibers**, the
    **reticulocerebellar fibers**, the **dentate efferents**,
    the **interposed efferents**, the **fastigial efferents**,
    the **cerebellovestibular fibers**, the
    **juxtarestiform body**, the **restiform body**, and the
    **decussation of Wernekink**) are **prose** within the
    sub-containers. Consumers must not assume any exist as
    direct children of the cerebellar peduncles container;
    resolve tract-level detail through the sub-containers
    and the references.
*   **WHITE-MATTER TRACTS — NOT the cerebellum or the
    brainstem.** The **cerebellum** is the **suprasegmental
    structure**; the **brainstem** is the **segmental
    neuraxis**; the **cerebellar peduncles** are the
    **conduction infrastructure** that **connects** them.
*   **THREE PEDUNCLES — NOT a single uniform structure.** The
    **superior cerebellar peduncle** (efferent, mostly), the
    **middle cerebellar peduncle** (afferent, the
    **largest**), and the **inferior cerebellar peduncle**
    (mixed — the **restiform body** + the
    **juxtarestiform body**) are **functionally distinct
    peduncles**.
*   **PAIRED — MULTIPLE left/right peduncles.** Each peduncle
    is **bilaterally paired**; the tree wires the **three
    peduncles** as **three sub-containers**, each
    representing the peduncle as a **bilateral pair**.
*   **CHILDREN OF THE PONS — NOT of the cerebellum or the
    brainstem.** The tree wires the cerebellar peduncles as
    **children of the pons** — the **pons "owns" the
    peduncle attachment**.
*   **NOT the fourth ventricle — a CSF cavity.** The superior
    and inferior cerebellar peduncles form the **lateral
    walls** of the fourth ventricle, but they are **NOT**
    the fourth ventricle.
*   **NOT the deep nuclei.** The **deep nuclei** are the
    **grey-matter output nuclei**; the **peduncles** are the
    **white-matter tracts** that carry their efferents.
*   **NOT the cerebellar deep white matter.** The **deep
    white matter** is the **intracerebellar white-matter
    core** (arbor vitae); the **cerebellar peduncles** are
    the **extracerebellar white-matter tracts**.
*   **NOT the cerebral peduncle.** The **cerebral peduncle**
    is the **midbrain ventral structure**; the **cerebellar
    peduncles** are the **cerebellar white-matter tracts**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **NOT a neural processor — CONDUCTION INFRASTRUCTURE.**
    The **processing** happens in the **cerebellum** and the
    **brainstem**; the **cerebellar peduncles** are the
    **white-matter tracts** that **carry** the signals.
*   **No ``AREA_PATHS`` hop.** The cerebellar peduncles are a
    **local container** under the pons, not a
    **cross-listed container**.
*   **No nested cross-listing.** The cerebellar peduncles have
    **no nested dual-framing module**. They are a **single
    container** with three sub-containers.
*   **No lateralization warning.** The cerebellar peduncles
    carry **no warning** — **no SLEA warning**, **no
    amygdala-lateralization warning**, and **no
    rhinencephalon-exclusion flag**. The **bilateral pairing**,
    the **bilateral connectivity** of the middle cerebellar
    peduncle, and the **decussation** of the superior
    cerebellar peduncle are documented as **prose**, not as a
    **warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.pons.cerebellar_peduncles import (
        inferior_cerebellar_peduncle,
        middle_cerebellar_peduncle,
        superior_cerebellar_peduncle,
    )

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles"
    )
    inferior_path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles."
        "inferior_cerebellar_peduncle"
    )
    middle_path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles."
        "middle_cerebellar_peduncle"
    )
    superior_path = (
        "hindbrain.metencephalon.pons.cerebellar_peduncles."
        "superior_cerebellar_peduncle"
    )

**Do not** assume the cerebellar peduncles are the **cerebellum**.
The **cerebellum** is the **suprasegmental structure**; the
**cerebellar peduncles** are the **white-matter tracts** that
**connect** the cerebellum to the brainstem.

**Do not** assume the cerebellar peduncles are the **brainstem**.
The **brainstem** is the **segmental neuraxis**; the
**cerebellar peduncles** are the **conduction infrastructure**
that **connects** the cerebellum to it.

**Do not** assume the cerebellar peduncles are a **single
uniform structure**. The **superior cerebellar peduncle**
(efferent, mostly), the **middle cerebellar peduncle**
(afferent, the **largest**), and the **inferior cerebellar
peduncle** (mixed) are **functionally distinct peduncles**.

**Do not** assume the cerebellar peduncles are **unpaired**.
Each peduncle is **bilaterally paired**; the tree wires the
**three peduncles** as **three sub-containers**, each
representing the peduncle as a **bilateral pair**.

**Do not** assume the cerebellar peduncles are the **fourth
ventricle**. The **superior and inferior cerebellar
peduncles** form the **lateral walls** of the fourth
ventricle, but they are **NOT** the fourth ventricle.

**Do not** assume the cerebellar peduncles are the **deep
nuclei**. The **deep nuclei** are the **grey-matter output
nuclei**; the **peduncles** are the **white-matter tracts**
that carry their efferents.

**Do not** assume the cerebellar peduncles are the
**cerebellar deep white matter**. The **deep white matter** is
the **intracerebellar white-matter core** (arbor vitae); the
**cerebellar peduncles** are the **extracerebellar
white-matter tracts**.

**Do not** assume the cerebellar peduncles are the **cerebral
peduncle**. The **cerebral peduncle** is the **midbrain
ventral structure**; the **cerebellar peduncles** are the
**cerebellar white-matter tracts**.

**Do not** assume the cerebellar peduncles are the
**pons**, **metencephalon**, **hindbrain**, **brainstem**,
**cerebellum**, or **fourth ventricle**. The **cerebellar
peduncles** are **children of the pons** (the **tree wires
them as children of the pons**) — the **white-matter tracts**
that **connect** the cerebellum to the brainstem.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the cerebellar
peduncles. **The cerebellar peduncles are SLEA-FREE** — they
are **not** an extended-amygdala component, and they are
**NOT the fear-output structure**.

Iterating the cerebellar peduncles' children (recommended
consumer pattern)::

    CEREBELLAR_PEDUNCLES_CHILDREN = (
        "inferior_cerebellar_peduncle",
        "middle_cerebellar_peduncle",
        "superior_cerebellar_peduncle",
    )
    # The three peduncles (superior, middle, inferior) are the
    # three structural children of the cerebellar peduncles
    # container. Each sub-container is the peduncle as a
    # bilateral pair (left and right).

Reaching the pons (recommended consumer pattern — the parent)::

    # The pons is the CONTAINER (the whole metencephalic
    # brainstem segment):
    #
    #   hindbrain.metencephalon.pons
    #
    # The cerebellar peduncles are CHILDREN of the pons in the
    # tree.

Reaching the cerebellum (recommended consumer pattern — NOTE
the conduction-infrastructure-vs-suprasegmental-structure
boundary)::

    # The cerebellum is the DORSAL SUPRASEGMENTAL structure:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cerebellum is the SUPRASEGMENTAL STRUCTURE; the
    # cerebellar peduncles are the CONDUCTION INFRASTRUCTURE
    # that connect it to the brainstem.

Reaching the brainstem (recommended consumer pattern — NOTE
the conduction-infrastructure-vs-segmental-neuraxis boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons
    # + medulla):
    #
    #   midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The brainstem is the SEGMENTAL NEURAXIS; the cerebellar
    # peduncles are the CONDUCTION INFRASTRUCTURE that connects
    # the cerebellum to it.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the white-matter-tract-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The superior and inferior cerebellar peduncles form the
    # LATERAL WALLS of the fourth ventricle, but they are NOT
    # the fourth ventricle.

Reaching the deep nuclei (recommended consumer pattern — NOTE
the white-matter-tract-vs-grey-matter-output-nuclei boundary)::

    # The deep nuclei are the GREY-MATTER OUTPUT NUCLEI
    # (dentate, interposed, fastigial):
    #
    #   hindbrain.metencephalon.cerebellum.nuclei
    #
    # The deep nuclei are the GREY-MATTER OUTPUT NUCLEI; the
    # cerebellar peduncles are the WHITE-MATTER TRACTS that
    # carry their efferents.

Reaching the cerebellar deep white matter (recommended
consumer pattern — NOTE the extracerebellar-vs-
intracerebellar white matter boundary)::

    # The cerebellar deep white matter is the INTRACEREBELLAR
    # white-matter core (arbor vitae):
    #
    #   hindbrain.metencephalon.cerebellum.deep_white_matter
    #
    # The deep white matter is INTRACEREBELLAR; the cerebellar
    # peduncles are EXTRACEREBELLAR.

Reaching the cerebral peduncle (recommended consumer pattern —
NOTE the cerebellar-white-matter-vs-midbrain-ventral-structure
boundary)::

    # The cerebral peduncle is the MIDBRAIN ventral structure
    # (crus cerebri + substantia nigra + tegmentum):
    #
    #   midbrain.cerebral_peduncle
    #
    # The cerebral peduncle is the MIDBRAIN ventral structure;
    # the cerebellar peduncles are the CEREBELLAR white-matter
    # tracts. The name "peduncle" is shared, but the structures
    # are different.

Reaching the superior cerebellar peduncle (recommended
consumer pattern — NOTE the efferent-peduncle boundary)::

    # The superior cerebellar peduncle (brachium conjunctivum)
    # is the EFFERENT peduncle (mostly):
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles.
    #   superior_cerebellar_peduncle
    #
    # The superior cerebellar peduncle carries the dentate and
    # interposed efferents (and, via the juxtarestiform body,
    # the fastigial efferents) and decussates in the caudal
    # midbrain (the decussation of Wernekink).

Reaching the middle cerebellar peduncle (recommended
consumer pattern — NOTE the afferent-peduncle boundary)::

    # The middle cerebellar peduncle (brachium pontis) is the
    # AFFERENT peduncle (the LARGEST peduncle):
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles.
    #   middle_cerebellar_peduncle
    #
    # The middle cerebellar peduncle carries the
    # corticopontocerebellar fibers (the pontocerebellar
    # fibers) from the contralateral pontine nuclei to the
    # contralateral cerebellar cortex.

Reaching the inferior cerebellar peduncle (recommended
consumer pattern — NOTE the mixed-peduncle boundary)::

    # The inferior cerebellar peduncle is the MIXED peduncle
    # (the restiform body + the juxtarestiform body):
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles.
    #   inferior_cerebellar_peduncle
    #
    # The inferior cerebellar peduncle carries the restiform
    # body (the dorsal spinocerebellar tract, the
    # cuneocerebellar tract, the olivocerebellar fibers, the
    # reticulocerebellar fibers) and the juxtarestiform body
    # (the fastigial efferents, the vestibulocerebellar
    # fibers, the cerebellovestibular fibers).

Fiber-tract detail (not wired at the cerebellar peduncles level
— consult the sub-containers and references)::

    # The cerebellar peduncles' fiber-tract detail is prose
    # within the sub-containers:
    #   superior_cerebellar_peduncle -> dentate efferents,
    #                                   interposed efferents,
    #                                   fastigial efferents
    #                                   (via the juxtarestiform
    #                                   body), the decussation of
    #                                   Wernekink
    #   middle_cerebellar_peduncle -> corticopontocerebellar
    #                                 fibers (the
    #                                 pontocerebellar fibers)
    #   inferior_cerebellar_peduncle -> restiform body (the
    #                                   dorsal spinocerebellar
    #                                   tract, the
    #                                   cuneocerebellar tract,
    #                                   the olivocerebellar
    #                                   fibers, the
    #                                   reticulocerebellar
    #                                   fibers) + the
    #                                   juxtarestiform body (the
    #                                   fastigial efferents, the
    #                                   vestibulocerebellar
    #                                   fibers, the
    #                                   cerebellovestibular
    #                                   fibers)
    #
    # Do not attempt to resolve these as sub-paths of the
    # cerebellar peduncles.

Bilateral iteration (recommended consumer pattern — each
peduncle is bilaterally paired)::

    # Each peduncle is bilaterally paired (left and right).
    # The tree wires the three peduncles as three sub-
    # containers, each representing the peduncle as a
    # bilateral pair. Do not attempt to resolve left/right
    # sub-paths of the cerebellar peduncles — the bilateral
    # pairing is documented as prose within each peduncle
    # sub-container.

References
----------
*   **Canonical cerebellar peduncle anatomy:** Standring, S.
    (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Cerebellum — superior,
    middle, and inferior cerebellar peduncles; the
    decussation of Wernekink; the restiform body; the
    juxtarestiform body.)
*   **Cerebellum overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Cerebellum — superior cerebellar peduncle, middle
    cerebellar peduncle, inferior cerebellar peduncle,
    cerebellar afferents and efferents.)
*   **Superior cerebellar peduncle (decussation of
    Wernekink):** Voogd, J., Glickstein, M. (1998). "The
    anatomy of the cerebellum." *Trends in Neurosciences*
    21:370–375. (Superior cerebellar peduncle — the
    efferent peduncle; the decussation of Wernekink; the
    double crossing that makes cerebellar control
    ipsilateral.)
*   **Middle cerebellar peduncle (corticopontocerebellar
    fibers):** Mihailoff, G.A., et al. (1985). "The basilar
    pontine gray of the opossum: a correlated light and
    electron microscopic analysis." *Journal of Comparative
    Neurology* 233:417–437. (Middle cerebellar peduncle —
    the corticopontocerebellar fibers — the pontocerebellar
    projection from the contralateral pontine nuclei to the
    contralateral cerebellar cortex.)
*   **Inferior cerebellar peduncle (restiform body):**
    Oscarsson, O. (1965). "Functional organization of the
    spino-cerebellar paths." In *Physiology of Spinal
    Neurons* (Eccles, J.C., Schadé, J.P., eds.). (Restiform
    body — the dorsal spinocerebellar tract, the
    cuneocerebellar tract, the olivocerebellar fibers, the
    reticulocerebellar fibers.)
*   **Juxtarestiform body (fastigial efferents):** Russell,
    J.S.R. (1897). "The origin and destination of certain
    tracts of the nervous system." *Brain* 20:350–369.
    (Juxtarestiform body — the fastigial efferents, the
    vestibulocerebellar fibers, the cerebellovestibular
    fibers.)
*   **Superior cerebellar artery (SCA) territory:**
    Savoiardo, M., et al. (1987). "Cerebellar infarcts:
    clinical and CT findings." *Journal of Neurology*
    234:256–262. (SCA — supplies the superior cerebellum
    and the superior cerebellar peduncle.)
*   **Anterior inferior cerebellar artery (AICA)
    territory:** Savoiardo, M., et al. (1987). "Cerebellar
    infarcts: clinical and CT findings." *Journal of
    Neurology* 234:256–262. (AICA — supplies the middle
    cerebellar peduncle and the lateral pons.)
*   **Posterior inferior cerebellar artery (PICA)
    territory:** Wallenberg, A. (1895). "Akute
    Bulbäraffection (Embolie der Arteria cerebelli
    posterior inferior sinistra)." *Archiv für Psychiatrie
    und Nervenkrankheiten* 27:504–540. (PICA — supplies
    the inferior cerebellar peduncle and the lateral
    medulla; lateral medullary syndrome.)
*   **Multiple sclerosis (cerebellar peduncles):** Compston,
    A., Coles, A. (2008). "Multiple sclerosis." *The
    Lancet* 372:1502–1517. (Multiple sclerosis —
    cerebellar peduncle demyelinating plaques.)
*   **SLEA (contrast — the cerebellar peduncles are NOT
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens;
    NOT the cerebellar peduncles.)
*   NeuroNames — Cerebellar peduncles; FMA — Cerebellar
    peduncles.
"""