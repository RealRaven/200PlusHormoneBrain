"""
infrastructure.brainparts.hindbrain.metencephalon.cerebellum.hemispheres
========================================================================

Anatomical Hierarchy
--------------------
::

    cerebellum
    ├── deep_white_matter
    ├── hemispheres                            <-- THIS MODULE
    │   ├── left
    │   │   ├── anterior_lobe
    │   │   ├── flocculonodular_lobe
    │   │   └── posterior_lobe
    │   └── right
    │       ├── anterior_lobe
    │       ├── flocculonodular_lobe
    │       └── posterior_lobe
    ├── nuclei
    └── vermis

**Primary synonym:** Cerebellar hemispheres; hemispherium cerebelli;
the lateral cerebellar hemispheres; the cerebrocerebellar
hemispheres; the cerebellar lateral zones; the "lateral
cerebellum."
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
single grey-matter or white-matter structure.** A **paired
suprasegmental region** — the **left** and **right** cerebellar
hemispheres, each comprising the **cerebellar cortex** (the
three-layered grey-matter cortex over the hemisphere) and the
**underlying white matter** (the folial white-matter branches of
the arbor vitae), organized into **three lobes** (anterior,
posterior, flocculonodular).
**Part of:** The **cerebellum** container — the **lateral
cerebellar divisions**. The **cerebellum** is the
**metencephalic suprasegmental structure**; the
**metencephalon** is the **rostral** of the **two
rhombencephalic sub-vesicles**; the **hindbrain** is the
**caudal** of the **three primary brain vesicles**.
**Structural parent:** ``.../cerebellum/`` → **direct child** of
the cerebellum container.
**Structural children:** **Two** — ``left/`` and ``right/``. Each
is a **sub-container** with **three lobe sub-containers**
(``anterior_lobe/``, ``flocculonodular_lobe/``, and
``posterior_lobe/``). The **cerebellar cortex** (the
three-layered grey-matter cortex), the **folial white matter**
(the white-matter branches of the arbor vitae within each
hemisphere), the **cerebellar fissures** (primary fissure,
posterolateral fissure, horizontal fissure), the **lobules**
(simplex, ansiform, paramedian, semilunar, biventer, tonsil,
etc.), the **cerebellar zones** (vermal, paravermal,
hemispheral, lateral), and the **cerebellar microzones** are
documented as **prose** or as **children of the lobe
sub-containers**.
**Boundary status (LATERAL CEREBELLAR DIVISION — NOT the
vermis):** **Boundary case — the cerebellar hemispheres are the
LATERAL cerebellar division, NOT the vermis.** The **vermis**
(``.../cerebellum/vermis/``) is the **midline** cerebellar
division — the **spinocerebellum midline** (posture, gait, axial
motor control). The **cerebellar hemispheres** (here) are the
**lateral** cerebellar division — the **cerebrocerebellum
lateral** (limb motor coordination, motor learning, cognition).
**They are DIFFERENT cerebellar divisions** — the **vermis** is
**midline**; the **hemispheres** are **lateral**. They are
**continuous** at the **paravermal zone** (the
**intermediate** cerebellar zone), but they are **distinct
divisions**. Consumers must **not** conflate the cerebellar
hemispheres with the vermis.
**Boundary status (PAIRED — NOT a single structure):** **Boundary
case — the cerebellar hemispheres are a PAIRED structure (left
and right), NOT a single hemisphere.** The **left cerebellar
hemisphere** and the **right cerebellar hemisphere** are
**separate sub-containers** — they are **separated** by the
**vermis** (the midline) and are **continuous** with it at the
**paravermal zone**, but they are **distinct** left and right
**lateral** divisions. **The hemispheres are the PAIR; each
hemisphere is a MEMBER of the pair.** Consumers must **not**
conflate the cerebellar hemispheres (the pair) with a **single
cerebellar hemisphere** — the **hemispheres** are the
**bilateral pair**; each **hemisphere** is a **member**.
**Boundary status (CEREBELLAR — NOT the cerebral hemispheres):**
**Boundary case — the cerebellar hemispheres are CEREBELLAR, NOT
the cerebral hemispheres.** The **cerebral hemispheres**
(``.../forebrain/telencephalon/cerebral_hemispheres/``) are the
**forebrain** structures — the **cortex**, the **white matter**
(centrum semiovale, corona radiata, internal capsule, corpus
callosum), the **basal ganglia**, the **hippocampus**, the
**amygdala**, the **lateral ventricles**. The **cerebellar
hemispheres** (here) are the **hindbrain** structures — the
**lateral** cerebellar divisions. **They are DIFFERENT structures
in DIFFERENT brain vesicles** — the **cerebral hemispheres** are
**forebrain**; the **cerebellar hemispheres** are **hindbrain**.
The word **"hemisphere"** is **shared** (both are
"hemispheres"), but the **structures are different** — consumers
must **not** conflate the cerebellar hemispheres with the
cerebral hemispheres.
**Boundary status (CORTEX + WHITE MATTER — NOT the deep white
matter or the deep nuclei):** **Boundary case — the cerebellar
hemispheres are CORTEX + WHITE MATTER (the lateral hemispheral
tissue), NOT the deep white matter or the deep nuclei.** The
**cerebellar deep white matter**
(``.../cerebellum/deep_white_matter/``) is the **white-matter
core** — the **arbor vitae** and the **intracerebellar tracts**
— that **spans** the hemispheres and the vermis. The
**cerebellar deep nuclei** (``.../cerebellum/nuclei/``) are the
**grey-matter output nuclei** — the **dentate nucleus**, the
**fastigial nucleus**, and the **interposed nucleus**. The
**cerebellar hemispheres** (here) are the **lateral cerebellar
tissue divisions** — the **cortex** (grey matter) **plus** the
**folial white matter** (the white-matter branches within each
hemisphere). **The hemispheres are the LATERAL TISSUE
DIVISIONS; the deep white matter is the WHITE-MATTER CORE; the
deep nuclei are the GREY-MATTER OUTPUT NUCLEI.** Consumers must
**not** conflate the cerebellar hemispheres with the deep white
matter or the deep nuclei.
**Boundary status (LATERAL DIVISION — NOT the metencephalon,
hindbrain, or cerebellum container):** **Boundary case — the
cerebellar hemispheres are a LATERAL DIVISION of the cerebellum,
NOT the metencephalon, the hindbrain, or the cerebellum
container.** The **cerebellum** (``.../cerebellum/``) is the
**suprasegmental structure** (the container); the
**metencephalon** (``.../metencephalon/``) is the **rostral**
hindbrain sub-container (pons + cerebellum + fourth ventricle);
the **hindbrain** (``.../hindbrain/``) is the **whole**
rhombencephalon derivative. The **cerebellar hemispheres**
(here) are a **child sub-container of the cerebellum**. **The
hemispheres are a PART of the cerebellum; the cerebellum is the
WHOLE; the metencephalon and hindbrain are the CONTAINERS ABOVE
it.** Consumers must **not** conflate the cerebellar
hemispheres with the metencephalon, the hindbrain, or the
cerebellum container.
**Boundary status (LATERAL CEREBELLUM — NOT the brainstem):**
**Boundary case — the cerebellar hemispheres are LATERAL
CEREBELLUM, NOT the brainstem.** The **brainstem** is the
**segmental neuraxis** (midbrain + pons + medulla oblongata) —
the **cranial nerve nuclei** and the **long ascending/descending
tracts**. The **cerebellar hemispheres** (here) are
**suprasegmental** — they are **part of the cerebellum**, which
is **attached to the brainstem** via the **cerebellar
peduncles** (children of the pons), but which is **NOT part of
the brainstem** proper. Consumers must **not** conflate the
cerebellar hemispheres with the brainstem — the **hemispheres**
are **suprasegmental**; the **brainstem** is **segmental**.
**Boundary status (LATERAL CEREBELLUM — NOT the fourth
ventricle):** **Boundary case — the cerebellar hemispheres are
LATERAL CEREBELLUM, NOT the fourth ventricle.** The **fourth
ventricle** (``.../metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **cerebellar hemispheres** (here) are the
**lateral cerebellar tissue divisions** — **dorsal** to the
fourth ventricle. Consumers must **not** conflate the cerebellar
hemispheres with the fourth ventricle.
**Boundary status (NOT the cerebellar peduncles — those are
WHITE-MATTER TRACTS, children of the PONS):** **Boundary
case — the cerebellar hemispheres are NOT the cerebellar
peduncles.** The **cerebellar peduncles** — the **superior
cerebellar peduncle**, the **middle cerebellar peduncle**, and
the **inferior cerebellar peduncle** — are the **white-matter
tracts** that **connect** the cerebellum to the brainstem
(midbrain, pons, medulla). In the tree, the **cerebellar
peduncles** are **children of the pons**
(``.../metencephalon/pons/cerebellar_peduncles/``), **not**
children of the cerebellum. The **cerebellar hemispheres**
(here) are the **lateral cerebellar tissue divisions** — the
**cortex** and the **folial white matter**. **The peduncles are
the CONDUCTION INFRASTRUCTURE; the hemispheres are the TISSUE.**
Consumers must **not** conflate the cerebellar hemispheres with
the cerebellar peduncles.
**Boundary status (HETEROGENEOUS — MULTIPLE lobes with DIFFERENT
functions):** **Boundary case — the cerebellar hemispheres are a
HETEROGENEOUS lateral division with MULTIPLE lobes and MULTIPLE
functions, not a single uniform system.** Each hemisphere
includes:
*   **Anterior lobe** — the **spinocerebellum** (limb
    proprioception, motor execution).
*   **Posterior lobe** — the **cerebrocerebellum** (motor
    planning, motor learning, cognition — including the
    **cerebellar cognitive-affective syndrome**).
*   **Flocculonodular lobe** — the **vestibulocerebellum**
    (vestibular control, eye movements, balance).
**Each lobe is functionally distinct** — the tree wires the
**anterior_lobe**, **flocculonodular_lobe**, and
**posterior_lobe** as **sub-containers of each hemisphere**.
Consumers must **not** treat the cerebellar hemispheres as a
single uniform region — they are a **paired heterogeneous
lateral division** with **three functionally distinct lobes**.
**Boundary status (SLEA-FREE — the cerebellar hemispheres are
NOT an extended-amygdala component):** **Boundary case — the
cerebellar hemispheres are SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component**
in the amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The **cerebellar
hemispheres** are a **lateral cerebellar division** — they are
**NOT** an extended-amygdala component, and they carry **NO
SLEA warning**. Consumers must **not** import the SLEA warning
into the cerebellar hemispheres — they are **SLEA-free**.
**Boundary status (NOT a neural processor in the classical
sense — the hemispheres are a REGION, not a single
processor):** **Boundary case — the cerebellar hemispheres are a
REGION, not a single neural processor.** They **contain** neural
processors (the cerebellar cortex microzones of each lobe, the
Purkinje-cell output, the deep nuclei projections) — but they
are **not themselves a processor**. The **processing** happens
in the **sub-structures** (the cerebellar cortex of each lobe,
the deep nuclei). Consumers must **not** treat the cerebellar
hemispheres as a **single neural processor** — they are a
**paired lateral division** with **heterogeneous lobes**, each
with its own function.

Overview
--------
The cerebellar hemispheres are the **lateral cerebellar
divisions** — the **left** and **right** cerebellar
hemispheres, each comprising the **cerebellar cortex** (the
three-layered grey-matter cortex over the hemisphere) and the
**underlying white matter** (the folial white-matter branches of
the arbor vitae), organized into **three lobes** (anterior,
posterior, flocculonodular). They are a **container module**
with **two structural sub-containers** (``left/`` and
``right/``), each with **three lobe sub-containers**.

**The cerebellar hemispheres are the LATERAL cerebellar division,
distinct from the vermis (the midline division).** The **vermis**
(``.../cerebellum/vermis/``) is **midline**; the **cerebellar
hemispheres** (here) are **lateral**. They are **continuous** at
the **paravermal zone** (the **intermediate** cerebellar zone),
but they are **distinct divisions**.

**The cerebellar hemispheres are a PAIRED structure (left and
right).** The **left cerebellar hemisphere** and the **right
cerebellar hemisphere** are **separate sub-containers** —
**separated** by the **vermis** and **continuous** with it at
the **paravermal zone**. **The hemispheres are the PAIR; each
hemisphere is a MEMBER of the pair.**

**The cerebellar hemispheres are NOT the cerebral hemispheres.**
The **cerebral hemispheres** (``.../forebrain/telencephalon/
cerebral_hemispheres/``) are the **forebrain** structures (the
"brain"); the **cerebellar hemispheres** (here) are the
**hindbrain** structures (part of the **"little brain"**). The
word **"hemisphere"** is **shared**, but the **structures are
different** — the **cerebral hemispheres** are **forebrain**;
the **cerebellar hemispheres** are **hindbrain**.

**The cerebellar hemispheres are a HETEROGENEOUS lateral
division, not a single structure.** Each hemisphere includes the
**anterior lobe** (spinocerebellum — limb proprioception, motor
execution), the **posterior lobe** (cerebrocerebellum — motor
planning, motor learning, cognition — including the **cerebellar
cognitive-affective syndrome**), and the **flocculonodular
lobe** (vestibulocerebellum — vestibular control, eye movements,
balance). Each lobe is functionally distinct.

**The cerebellar hemispheres are a REGION, not a single neural
processor.** The **processing** happens in the **sub-structures**
(the cerebellar cortex of each lobe, the deep nuclei). The
**hemispheres** are the **paired lateral division** that
**contains** those sub-structures.

Hemispheral Composition (sub-containers and prose)
--------------------------------------------------
The cerebellar hemispheres are a **paired lateral division** with
**two sub-containers** — documented as **structural children**
(``left/`` and ``right/``) — each with **three lobe
sub-containers**, and **many prose-defined sub-structures**
documented within those lobe sub-containers:

*   **Left hemisphere** (``.../cerebellum/hemispheres/left/``) —
    the **left** lateral cerebellar division:
    *   **Anterior lobe**
        (``.../hemispheres/left/anterior_lobe/``) — the
        **spinocerebellum** (limb proprioception, motor
        execution).
    *   **Posterior lobe**
        (``.../hemispheres/left/posterior_lobe/``) — the
        **cerebrocerebellum** (motor planning, motor learning,
        cognition — including the **cerebellar
        cognitive-affective syndrome**; the **left cerebellar
        hemisphere** is connected to the **right parietal
        lobe** — **visuospatial** function).
    *   **Flocculonodular lobe**
        (``.../hemispheres/left/flocculonodular_lobe/``) — the
        **vestibulocerebellum** (vestibular control, eye
        movements, balance).

*   **Right hemisphere**
    (``.../cerebellum/hemispheres/right/``) — the **right**
    lateral cerebellar division:
    *   **Anterior lobe**
        (``.../hemispheres/right/anterior_lobe/``) — the
        **spinocerebellum** (limb proprioception, motor
        execution).
    *   **Posterior lobe**
        (``.../hemispheres/right/posterior_lobe/``) — the
        **cerebrocerebellum** (motor planning, motor learning,
        cognition — including the **cerebellar
        cognitive-affective syndrome**; the **right cerebellar
        hemisphere** is connected to the **left frontal
        lobe** — **language**).
    *   **Flocculonodular lobe**
        (``.../hemispheres/right/flocculonodular_lobe/``) —
        the **vestibulocerebellum** (vestibular control, eye
        movements, balance).

**These sub-structures are children of the lobe sub-containers
(or prose), not direct structural children of the cerebellar
hemispheres.** The tree wires the **cerebellar hemispheres** as
a **container** with **two sub-containers** (``left/`` and
``right/``) — the **cerebellar cortex**, the **folial white
matter**, the **fissures** (primary fissure, posterolateral
fissure, horizontal fissure), the **lobules** (simplex,
ansiform, paramedian, semilunar, biventer, tonsil, etc.), the
**cerebellar zones** (vermal, paravermal, hemispheral,
lateral), and the **cerebellar microzones** are documented as
**prose** or as **children of the lobe sub-containers**.
Consumers that need **lobule-level** resolution should consult
the **lobe sub-container modules** and the references, not the
hemispheres container.

The Cerebellar Hemispheres / Vermis Boundary
--------------------------------------------
This is the **lateral-vs-midline** boundary:

*   **Cerebellar hemispheres** (this module) — the **lateral**
    cerebellar division.

*   **Vermis** (``.../cerebellum/vermis/``) — the **midline**
    cerebellar division.

**They are DIFFERENT cerebellar divisions** — the **vermis** is
**midline**; the **hemispheres** are **lateral**. They are
**continuous** at the **paravermal zone** (the **intermediate**
cerebellar zone), but they are **distinct divisions**. Consumers
must **not** conflate the cerebellar hemispheres with the
vermis.

The Cerebellar Hemispheres / Left and Right Hemisphere Boundary
---------------------------------------------------------------
This is the **pair-vs-member** boundary:

*   **Cerebellar hemispheres** (this module) — the **paired
    lateral division** (left + right).

*   **Left hemisphere**
    (``.../cerebellum/hemispheres/left/``) and **right
    hemisphere** (``.../cerebellum/hemispheres/right/``) — the
    **individual members** of the pair.

**The hemispheres are the PAIR; each hemisphere is a MEMBER of the
pair.** Consumers must **not** conflate the cerebellar
hemispheres (the pair) with a **single cerebellar hemisphere**.

The Cerebellar Hemispheres / Cerebral Hemispheres Boundary
---------------------------------------------------------
This is the **hindbrain-vs-forebrain** boundary:

*   **Cerebellar hemispheres** (this module) — the **hindbrain**
    structures (part of the **"little brain"**).

*   **Cerebral hemispheres** (``.../forebrain/telencephalon/
    cerebral_hemispheres/``) — the **forebrain** structures
    (the **"brain"** — cortex, white matter, basal ganglia,
    hippocampus, amygdala, lateral ventricles).

**They are DIFFERENT structures in DIFFERENT brain vesicles** —
the **cerebral hemispheres** are **forebrain**; the
**cerebellar hemispheres** are **hindbrain**. The word
**"hemisphere"** is **shared**, but the **structures are
different**. Consumers must **not** conflate the cerebellar
hemispheres with the cerebral hemispheres.

The Cerebellar Hemispheres / Deep White Matter Boundary
-------------------------------------------------------
This is the **lateral-division-vs-white-matter-core** boundary:

*   **Cerebellar hemispheres** (this module) — the **lateral
    cerebellar tissue divisions** (cortex + folial white
    matter).

*   **Cerebellar deep white matter**
    (``.../cerebellum/deep_white_matter/``) — the
    **white-matter core** (arbor vitae and intracerebellar
    tracts).

**The hemispheres are the LATERAL TISSUE DIVISIONS; the deep
white matter is the WHITE-MATTER CORE.** Consumers must **not**
conflate the cerebellar hemispheres with the deep white matter.

The Cerebellar Hemispheres / Deep Nuclei Boundary
-------------------------------------------------
This is the **lateral-division-vs-grey-matter-output-nuclei**
boundary:

*   **Cerebellar hemispheres** (this module) — the **lateral
    cerebellar tissue divisions**.

*   **Cerebellar deep nuclei** (``.../cerebellum/nuclei/``) —
    the **grey-matter output nuclei** (dentate, fastigial,
    interposed).

**The hemispheres are the LATERAL TISSUE DIVISIONS; the deep
nuclei are the GREY-MATTER OUTPUT NUCLEI.** Consumers must
**not** conflate the cerebellar hemispheres with the deep
nuclei.

The Cerebellar Hemispheres / Cerebellum Boundary
------------------------------------------------
This is the **child-vs-container** boundary:

*   **Cerebellar hemispheres** (this module) — the **lateral
    cerebellar division** (a **child of the cerebellum**).

*   **Cerebellum** (``.../cerebellum/``) — the **container**.

**The cerebellar hemispheres are a PART of the cerebellum; the
cerebellum is the WHOLE.** Consumers must **not** conflate the
cerebellar hemispheres with the cerebellum container.

The Cerebellar Hemispheres / Metencephalon and Hindbrain Boundary
-----------------------------------------------------------------
This is the **descendant-vs-container** boundary:

*   **Cerebellar hemispheres** (this module) — a **child of the
    cerebellum** (a **grandchild of the metencephalon**, a
    **great-grandchild of the hindbrain**).

*   **Metencephalon** (``.../metencephalon/``) and **hindbrain**
    (``.../hindbrain/``) — the **containers**.

**The cerebellar hemispheres are a PART of the cerebellum (via the
metencephalon and hindbrain).** Consumers must **not** conflate
the cerebellar hemispheres with the metencephalon or the
hindbrain.

The Cerebellar Hemispheres / Brainstem Boundary
-----------------------------------------------
This is the **suprasegmental-vs-segmental** boundary:

*   **Cerebellar hemispheres** (this module) — the
    **suprasegmental** lateral cerebellar division.

*   **Brainstem** (midbrain + pons + medulla oblongata) — the
    **segmental neuraxis**.

**The cerebellar hemispheres are SUPRASEGMENTAL, not brainstem.**
They are **part of the cerebellum**, which is **attached to the
brainstem** via the **cerebellar peduncles**, but which is
**NOT part of the brainstem** proper. Consumers must **not**
conflate the cerebellar hemispheres with the brainstem.

The Cerebellar Hemispheres / Fourth Ventricle Boundary
------------------------------------------------------
This is the **lateral-cerebellum-vs-CSF-cavity** boundary:

*   **Cerebellar hemispheres** (this module) — the **lateral
    cerebellar tissue divisions**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The fourth ventricle is a CSF CAVITY; the cerebellar
hemispheres are TISSUE DIVISIONS.** Consumers must **not**
conflate the cerebellar hemispheres with the fourth ventricle.

The Cerebellar Hemispheres / Cerebellar Peduncles Boundary
----------------------------------------------------------
This is the **tissue-vs-white-matter-tract** boundary:

*   **Cerebellar hemispheres** (this module) — the **lateral
    cerebellar tissue divisions**.

*   **Cerebellar peduncles** — the **white-matter tracts**
    connecting the cerebellum to the brainstem (children of
    the **pons** in the tree).

**The peduncles are the CONDUCTION INFRASTRUCTURE; the
hemispheres are the TISSUE.** Consumers must **not** conflate
the cerebellar hemispheres with the cerebellar peduncles.

The Cerebellar Hemispheres / SLEA Boundary
------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cerebellar hemispheres** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**,
    **ventral pallidum**, and **nucleus accumbens** (wired
    elsewhere).

**The cerebellar hemispheres are NOT part of the SLEA
continuum.** They are a **lateral cerebellar division**, and
they carry **no SLEA warning**. Consumers must **not** import
the SLEA warning into the cerebellar hemispheres.

Function in the Human Brain
---------------------------
The cerebellar hemispheres' functions are **heterogeneous** —
documented at the **lobe** level, not at the division level:

*   **Motor Coordination and Balance (Anterior, Posterior, and
    Flocculonodular Lobes):** The **anterior lobe**
    (spinocerebellum) — limb proprioception and motor
    execution; the **posterior lobe** (cerebrocerebellum) —
    limb motor planning and execution, motor learning; the
    **flocculonodular lobe** (vestibulocerebellum) —
    vestibular control, balance, and eye movements.

*   **Motor Learning (Posterior Lobe):** The **posterior lobe**
    of each hemisphere is the **neural substrate** of
    **motor learning** — the **cerebellar cortex** (Purkinje
    cells) and the **deep nuclei** (dentate, interposed) are
    **plastic** during **motor adaptation**, **classical
    conditioning** (e.g., **eyeblink conditioning**), and
    **skill learning**.

*   **Cerebellar Cognitive-Affective Syndrome (CCAS —
    Posterior Lobe):** The **posterior lobe** of each
    hemisphere — especially the **lateral** portion — is
    involved in **executive function**, **visuospatial
    processing**, **language**, and **affective regulation**.
    Lesions cause **cerebellar cognitive-affective syndrome**
    (CCAS) — **executive dysfunction**, **visuospatial
    deficits**, **language deficits**, and **affective
    dysregulation**.

*   **Vestibular Control and Eye Movements (Flocculonodular
    Lobe):** The **flocculonodular lobe** of each hemisphere
    is involved in **vestibular control**, **balance**, and
    **eye movements** (the **vestibulo-ocular reflex**,
    **saccadic accuracy**, **smooth pursuit**).

*   **Partial Lateralization (Contested — Language and
    Visuospatial):** The **right cerebellar hemisphere** (and
    its hemisphere) is connected to the **left frontal lobe**
    — **language**; the **left cerebellar hemisphere** (and
    its hemisphere) is connected to the **right parietal
    lobe** — **visuospatial** function. This is **partial**,
    **contested**, and documented in the **cerebellum module**
    (not at the hemispheres level).

*   **NOT a single neural processor.** The cerebellar
    hemispheres are a **paired lateral division** — the
    **processing** happens in the **sub-structures** (the
    cerebellar cortex of each lobe, the deep nuclei). Consumers
    must **not** treat the cerebellar hemispheres as a
    **single processor** — they are a **paired lateral
    division** with **heterogeneous lobes**.

**The unifying theme:** the cerebellar hemispheres are the
**lateral cerebellar divisions** — the **left** and **right**
cerebellar hemispheres, each comprising the **cerebellar
cortex** and the **folial white matter**, organized into
**three lobes** (anterior, posterior, flocculonodular) —
**coordinating limb motor execution, motor learning, balance,
eye movements, and non-motor (cognitive-affective) functions**.
They are a **paired heterogeneous lateral division**, **NOT a
single neural processor**, and **NOT the vermis, the cerebral
hemispheres, the deep white matter, the deep nuclei, the
cerebellum container, the metencephalon, the hindbrain, the
brainstem, or the fourth ventricle**.

Associated Disorders
--------------------
The cerebellar hemispheres have **named clinical syndromes** —
their clinical associations are **cerebellar** (via the
**lobes**, the **cerebellar cortex**, and the **deep nuclei**
of each hemisphere):

*   **Cerebellar Ataxia (Hemispheral — via the Hemispheres):**
    **Limb ataxia**, **dysmetria**, **dysdiadochokinesia**,
    **intention tremor**, and **dysarthria** — the
    **hemispheral cerebellar motor syndrome**. The **posterior
    lobe** of each hemisphere is the **primary substrate** for
    the **limb ataxia**; the **anterior lobe** for the
    **gait ataxia** component. Causes include **cerebellar
    stroke** (PICA, AICA, SCA infarcts), **cerebellar
    hemorrhage**, **cerebellar tumors**, **multiple sclerosis**
    (cerebellar plaques), **alcohol-related cerebellar
    degeneration** (anterior lobe / vermis), and
    **paraneoplastic cerebellar degeneration**.

*   **Spinocerebellar Ataxias (SCAs — via the Hemispheres):**
    A group of **genetically inherited cerebellar ataxias** —
    **autosomal dominant** (SCA1–SCA48+), **autosomal
    recessive** (Friedreich ataxia), and **X-linked** — with
    **progressive cerebellar ataxia** as the core phenotype,
    often with **brainstem**, **basal ganglia**, **retinal**,
    and **cognitive** involvement. The **cerebellar
    hemispheres** are a **primary substrate**.

*   **Cerebellar Cognitive-Affective Syndrome (CCAS — via the
    Posterior Lobe):** **Executive dysfunction**,
    **visuospatial deficits**, **language deficits**
    (agrammatism, dysprosodia), **affective dysregulation** —
    caused by **cerebellar hemispheral lesions** (especially
    the **posterior lobe**). The **cerebellar hemispheres**
    are the **substrate** — the **cerebellar-cortical loops**
    (cerebellum → thalamus → prefrontal cortex) are the
    **mechanism**.

*   **Cerebellar Tumors (Hemispheral — via the Hemispheres):**
    **Pilocytic astrocytoma** (the most common **benign
    pediatric brain tumor**, arising in the **cerebellar
    hemispheres**), **hemangioblastoma** (adult, cerebellar
    hemispheres), **metastatic tumors** (cerebellar
    hemispheres — the **most common adult cerebellar tumor**
    is **metastasis**), and **medulloblastoma** (typically
    arising in the **vermis**, but can involve the
    hemispheres). The **cerebellar hemispheres** are a
    **primary substrate**.

*   **Cerebellar Stroke (Hemispheral — via the Hemispheres):**
    **PICA infarct** (lateral medullary syndrome — involves
    the **inferior cerebellar peduncle** and the **cerebellar
    hemisphere**), **AICA infarct** (lateral pontine
    syndrome — involves the **middle cerebellar peduncle** and
    the **cerebellar hemisphere**), and **SCA infarct**
    (superior cerebellar syndrome — involves the **superior
    cerebellar peduncle** and the **cerebellar hemisphere**).
    The **cerebellar hemispheres** are the **substrate**.

*   **Cerebellar Hemorrhage (Hemispheral — via the
    Hemispheres):** **Hypertensive cerebellar hemorrhage** —
    typically in the **cerebellar hemispheres** — can cause
    **rapid neurological deterioration** (due to
    **fourth-ventricle compression** and **brainstem
    compression**) and requires **emergency neurosurgical
    evacuation**. The **cerebellar hemispheres** are the
    **substrate**.

*   **Paraneoplastic Cerebellar Degeneration (Hemispheral —
    via the Hemispheres):** **Anti-Yo**, **anti-Hu**,
    **anti-Tr**, **anti-Ri**, and **anti-metabotropic
    glutamate receptor 1 (mGluR1)** antibodies —
    **paraneoplastic cerebellar degeneration** associated
    with **ovarian cancer**, **breast cancer**, **Hodgkin
    lymphoma**, and other malignancies. The **cerebellar
    Purkinje cells** (in the **hemispheres**) are the
    **primary target**.

*   **Multiple Sclerosis (Hemispheral — via the Hemispheres):**
    **Demyelinating plaques** in the **cerebellar
    hemispheres** — the **cerebellar peduncles**, the
    **cerebellar white matter**, and the **cerebellar
    cortex** — causing **cerebellar ataxia**, **dysarthria**,
    **nystagmus**, and **intention tremor**. The **cerebellar
    hemispheres** are a **substrate**.

*   **No Named "Cerebellar Hemisphere Syndrome" (singular):**
    The cerebellar hemispheres have **multiple named clinical
    syndromes** (cerebellar ataxia, CCAS, SCAs, pilocytic
    astrocytoma, etc.) — but **no single "cerebellar
    hemisphere syndrome."** Their clinical relevance is
    **cerebellar** — via the **lobes**, the **cerebellar
    cortex**, and the **deep nuclei** of each hemisphere.

**What is NOT here:** The cerebellar hemispheres are **not** the
substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (central nucleus + basolateral nuclei),
**Urbach-Wiethe disease** (amygdala), or **Parkinson's disease**
(substantia nigra, in the midbrain). Their clinical relevance
is **cerebellar** — **cerebellar ataxia**, **CCAS**, **SCAs**,
**cerebellar tumors**, and **cerebellar stroke**.

Lateralization Notes
--------------------
This is the **cerebellar hemispheres** container module. The
cerebellar hemispheres are **bilaterally symmetric** and
**partially lateralized** — and they carry **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right**
    cerebellar hemispheres are **structurally symmetric** —
    same three lobes, same cerebellar cortex, same folial
    white matter, same deep nuclei projections (via the
    peduncles).

*   **Partial Lateralization (Contested — Language and
    Visuospatial):** The **right cerebellar hemisphere** is
    connected to the **left frontal lobe** — **language**
    (the **right cerebellar hemisphere** is more involved in
    **verbal/language** tasks). The **left cerebellar
    hemisphere** is connected to the **right parietal lobe**
    — **visuospatial** function (the **left cerebellar
    hemisphere** is more involved in **visuospatial**
    tasks). This is **partial**, **contested**, and
    documented in the **cerebellum module** (not at the
    hemispheres level).

*   **NO Extended-Amygdala Warning (SLEA-free):** The
    cerebellar hemispheres are **NOT** an extended-amygdala
    component. They carry **no SLEA warning**. Consumers must
    **not** import the SLEA warning into the cerebellar
    hemispheres.

*   **NO Amygdala-Lateralization Warning:** The cerebellar
    hemispheres are **NOT** the fear-output or the
    fear-learning structure. They are a **lateral cerebellar
    division** — consumers must **not** conflate them with
    the **amygdala** or the **fear circuit**.

**A consumer that assumes "left cerebellar hemisphere = right
cerebellar hemisphere" will be structurally correct** — the two
sides are **symmetric** and **partially lateralized** (the
lateralization is documented in the cerebellum module). The
cerebellar hemispheres carry **NO warning** — **no SLEA
warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**. The partial cerebellar
lateralization (language = right cerebellar; visuospatial = left
cerebellar) is **contested** and documented as **prose**, not as
a **warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **container** does
    **not** import from ``.../hemispheres/left/`` or
    ``.../hemispheres/right/`` — it is a **namespace
    container**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../cerebellum/`` (parent),
    ``.../cerebellum/deep_white_matter/`` (sibling),
    ``.../cerebellum/nuclei/`` (sibling),
    ``.../cerebellum/vermis/`` (sibling),
    ``.../metencephalon/`` (grandparent),
    ``.../metencephalon/pons/cerebellar_peduncles/`` (the
    peduncles are **children of the pons**, not of the
    cerebellum), ``.../metencephalon/fourth_ventricle/``,
    ``.../hindbrain/``, ``.../midbrain/``,
    ``.../forebrain/telencephalon/cerebral_hemispheres/`` (the
    cerebral hemispheres), or any other container. The
    cerebellar hemispheres' relationships to the vermis,
    cerebral hemispheres, deep white matter, deep nuclei,
    cerebellum, metencephalon, hindbrain, brainstem, fourth
    ventricle, and cerebellar peduncles are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — two structural children.** The
    ``left/`` and ``right/`` are **sub-containers**, each with
    **three lobe sub-containers** (``anterior_lobe/``,
    ``flocculonodular_lobe/``, and ``posterior_lobe/``). The
    **cerebellar cortex**, the **folial white matter**, the
    **fissures**, the **lobules**, the **cerebellar zones**,
    and the **cerebellar microzones** are **prose** or
    **children of the lobe sub-containers**. Consumers must not
    assume any exist as direct children of the cerebellar
    hemispheres; resolve lobule-level detail through the lobe
    sub-containers and the references.
*   **LATERAL CEREBELLAR DIVISION — NOT the vermis.** The
    **vermis** is the **midline** cerebellar division; the
    **hemispheres** are the **lateral** cerebellar division.
*   **PAIRED STRUCTURE — NOT a single hemisphere.** The
    **hemispheres** are the **pair**; each **hemisphere** is a
    **member**.
*   **CEREBELLAR — NOT the cerebral hemispheres.** The
    **cerebral hemispheres** are **forebrain**; the
    **cerebellar hemispheres** are **hindbrain**.
*   **LATERAL TISSUE DIVISIONS — NOT the deep white matter or
    the deep nuclei.** The **deep white matter** is the
    **white-matter core**; the **deep nuclei** are the
    **grey-matter output nuclei**.
*   **NOT the cerebellum container — a CHILD.** The
    **cerebellum** is the **container**; the **cerebellar
    hemispheres** are a **child**.
*   **NOT the metencephalon or hindbrain — a DESCENDANT.**
*   **NOT the brainstem — SUPRASEGMENTAL.** The
    **hemispheres** are **part of the cerebellum**, which is
    **suprasegmental**.
*   **NOT the fourth ventricle — a CSF cavity.**
*   **NOT the cerebellar peduncles — those are WHITE-MATTER
    TRACTS, children of the PONS.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    cerebellar hemispheres are **not** an extended-amygdala
    component, and they carry **no SLEA warning**.
*   **NOT a single neural processor — the hemispheres are a
    REGION.** The **processing** happens in the **sub-structures**
    (the cerebellar cortex of each lobe, the deep nuclei).
*   **No ``AREA_PATHS`` hop.** The cerebellar hemispheres are a
    local sub-container under the cerebellum, not a
    cross-listed container.
*   **No nested cross-listing.** The cerebellar hemispheres
    have no nested dual-framing module. They are a single
    container with two sub-containers.
*   **No lateralization warning.** The cerebellar hemispheres
    carry **no warning** — **no SLEA warning**, **no
    amygdala-lateralization warning**, and **no
    rhinencephalon-exclusion flag**. The partial cerebellar
    lateralization (language = right cerebellar; visuospatial
    = left cerebellar) is **contested** and documented as
    **prose**, not as a **warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.cerebellum.hemispheres import left, right

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.cerebellum.hemispheres"
    )
    left_path = (
        "hindbrain.metencephalon.cerebellum.hemispheres.left"
    )
    right_path = (
        "hindbrain.metencephalon.cerebellum.hemispheres.right"
    )

**Do not** assume the cerebellar hemispheres are the **vermis**.
The **vermis** is the **midline** division; the **hemispheres**
are the **lateral** division.

**Do not** assume the cerebellar hemispheres are a **single
hemisphere**. The **hemispheres** are the **pair**; each
**hemisphere** is a **member** of the pair.

**Do not** assume the cerebellar hemispheres are the **cerebral
hemispheres**. The **cerebral hemispheres** are **forebrain**;
the **cerebellar hemispheres** are **hindbrain**.

**Do not** assume the cerebellar hemispheres are the **deep
white matter** or the **deep nuclei**. The **deep white
matter** is the **white-matter core**; the **deep nuclei** are
the **grey-matter output nuclei**.

**Do not** assume the cerebellar hemispheres are the
**cerebellum**, **metencephalon**, **hindbrain**, or
**brainstem**. The **cerebellar hemispheres** are a **child of
the cerebellum** (a **grandchild of the metencephalon**, a
**great-grandchild of the hindbrain**).

**Do not** assume the cerebellar hemispheres are the **fourth
ventricle**. The **fourth ventricle** is a **CSF cavity**.

**Do not** assume the cerebellar hemispheres are the
**cerebellar peduncles**. The **peduncles** are the
**white-matter tracts** (children of the **pons**).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the cerebellar
hemispheres. **The cerebellar hemispheres are SLEA-FREE** —
they are **not** an extended-amygdala component, and they are
**NOT the fear-output structure**.

Iterating the cerebellar hemispheres' children (recommended
consumer pattern)::

    CEREBELLAR_HEMISPHERES_CHILDREN = ("left", "right")
    # The left and right cerebellar hemispheres are
    # sub-containers, each with three lobe sub-containers
    # (anterior_lobe, flocculonodular_lobe, posterior_lobe).

Reaching the vermis (recommended consumer pattern — the midline
division)::

    # The vermis is the MIDLINE cerebellar division:
    #
    #   hindbrain.metencephalon.cerebellum.vermis
    #
    # The cerebellar hemispheres are LATERAL; the vermis is
    # MIDLINE. They are continuous at the paravermal zone.

Reaching the cerebellum (recommended consumer pattern — the
parent)::

    # The cerebellum is the CONTAINER:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cerebellar hemispheres are a CHILD of the cerebellum.

Reaching the cerebral hemispheres (recommended consumer pattern —
NOTE the hindbrain-vs-forebrain boundary)::

    # The cerebral hemispheres are the FOREBRAIN structures:
    #
    #   forebrain.telencephalon.cerebral_hemispheres
    #
    # The cerebellar hemispheres are HINDBRAIN structures.

Reaching the deep white matter (recommended consumer pattern —
NOTE the lateral-division-vs-white-matter-core boundary)::

    # The deep white matter is the WHITE-MATTER CORE (arbor
    # vitae):
    #
    #   hindbrain.metencephalon.cerebellum.deep_white_matter
    #
    # The hemispheres are the LATERAL TISSUE DIVISIONS; the
    # deep white matter is the WHITE-MATTER CORE.

Reaching the deep nuclei (recommended consumer pattern — NOTE
the lateral-division-vs-grey-matter-output-nuclei boundary)::

    # The deep nuclei are the GREY-MATTER OUTPUT NUCLEI:
    #
    #   hindbrain.metencephalon.cerebellum.nuclei
    #
    # The hemispheres are the LATERAL TISSUE DIVISIONS; the
    # deep nuclei are the GREY-MATTER OUTPUT NUCLEI.

Reaching the metencephalon (recommended consumer pattern — the
grandparent)::

    # The metencephalon is the CONTAINER (pons + cerebellum +
    # fourth ventricle):
    #
    #   hindbrain.metencephalon
    #
    # The cerebellar hemispheres are a GRANDCHILD of the
    # metencephalon.

Reaching the hindbrain (recommended consumer pattern — the
great-grandparent)::

    # The hindbrain is the WHOLE rhombencephalon derivative:
    #
    #   hindbrain
    #
    # The cerebellar hemispheres are a GREAT-GRANDCHILD of the
    # hindbrain.

Reaching the brainstem (recommended consumer pattern — the
suprasegmental-vs-segmental boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons +
    # medulla):
    #
    #   midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The cerebellar hemispheres are SUPRASEGMENTAL — part of
    # the cerebellum, NOT part of the brainstem.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the lateral-cerebellum-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The fourth ventricle is a CSF CAVITY; the cerebellar
    # hemispheres are TISSUE DIVISIONS.

Reaching the cerebellar peduncles (recommended consumer pattern —
NOTE the tissue-vs-white-matter-tract boundary)::

    # The cerebellar peduncles are the WHITE-MATTER TRACTS —
    # children of the PONS:
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles
    #
    # The peduncles are the CONDUCTION INFRASTRUCTURE; the
    # hemispheres are the TISSUE.

Lobe-level detail (not wired at the hemispheres level — consult
the lobe sub-containers and references)::

    # The cerebellar hemispheres' lobe-level detail is prose
    # within the lobe sub-containers:
    #   anterior_lobe -> spinocerebellum (limb proprioception)
    #   posterior_lobe -> cerebrocerebellum (motor planning,
    #                     motor learning, cognition)
    #   flocculonodular_lobe -> vestibulocerebellum (vestibular
    #                            control, eye movements)
    #
    # Do not attempt to resolve the lobes as sub-paths of the
    # hemispheres.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        hemisphere_path = (
            f"hindbrain.metencephalon.cerebellum.hemispheres.{side}"
        )
        # resolve hemisphere_path through the memory/recall layer

References
----------
*   **Canonical cerebellar hemisphere anatomy:** Standring, S.
    (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Cerebellum — hemispheres,
    vermis, lobes, fissures, lobules.)
*   **Cerebellar overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Cerebellum — hemispheres, vermis, lobes, cerebellar
    peduncles.)
*   **Cerebellar function and dysfunction:** Manto, M., et al.
    (2012). "Consensus paper: roles of the cerebellum in motor
    control — the diversity of cerebellar involvement in
    movement." *The Cerebellum* 11:457–487. (Cerebellum —
    motor coordination, balance, motor learning.)
*   **Cerebellar cognitive-affective syndrome:** Schmahmann,
    J.D., Sherman, J.C. (1998). "The cerebellar cognitive
    affective syndrome." *Brain* 121:561–579. (Cerebellar
    cognitive-affective syndrome — executive dysfunction,
    visuospatial deficits, affective dysregulation; posterior
    lobe of the hemispheres.)
*   **Spinocerebellar ataxias:** Paulson, H.L. (2009). "The
    spinocerebellar ataxias." In *Neurogenetics* (Vance, J.M.,
    ed.). (SCAs — autosomal dominant cerebellar ataxias.)
*   **Pilocytic astrocytoma:** Collins, V.P., et al. (2015).
    "Pilocytic astrocytoma." In *WHO Classification of Tumours
    of the Central Nervous System* (Louis, D.N., et al.,
    eds.). (Pilocytic astrocytoma — pediatric cerebellar
    hemisphere tumor.)
*   **Hemangioblastoma:** Lonser, R.R., et al. (2003). "von
    Hippel-Lindau disease." *The Lancet* 361:2059–2067.
    (Hemangioblastoma — adult cerebellar hemisphere tumor;
    von Hippel-Lindau disease.)
*   **Cerebellar metastasis:** Posner, J.B., Chernik, N.L.
    (1978). "Intracranial metastases from systemic cancer."
    *Advances in Neurology* 19:579–592. (Cerebellar
    metastasis — the most common adult cerebellar tumor.)
*   **Cerebellar stroke (PICA, AICA, SCA):** Wallenberg, A.
    (1895). "Akute Bulbäraffection (Embolie der Arteria
    cerebelli posterior inferior sinistra)." *Archiv für
    Psychiatrie und Nervenkrankheiten* 27:504–540. (PICA
    infarct — lateral medullary syndrome; cerebellar
    hemisphere involvement.)
*   **Cerebellar hemorrhage:** Fisher, C.M., et al. (1965).
    "Acute hypertensive cerebellar hemorrhage: diagnosis and
    surgical treatment." *Journal of Nervous and Mental
    Disease* 140:38–57. (Hypertensive cerebellar hemorrhage —
    cerebellar hemispheres.)
*   **Paraneoplastic cerebellar degeneration:** Dalmau, J.,
    Rosenfeld, M.R. (2008). "Paraneoplastic syndromes of the
    CNS." *The Lancet Neurology* 7:327–340. (Paraneoplastic
    cerebellar degeneration — anti-Yo, anti-Hu, anti-Tr,
    anti-mGluR1; Purkinje cell target in the hemispheres.)
*   **Cerebellar lateralization (contested):** Mariën, P., et
    al. (2014). "Consensus paper: language and the cerebellum
    — an ongoing puzzle in neurobehavioural
    neuroscience." *The Cerebellum* 13:386–410. (Right
    cerebellar hemisphere — language; left cerebellar
    hemisphere — visuospatial; partial, contested.)
*   **SLEA (contrast — the cerebellar hemispheres are NOT
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral
    pallidum, nucleus accumbens; NOT the cerebellar
    hemispheres.)
*   NeuroNames — Cerebellar hemisphere; FMA — Cerebellar
    hemisphere.
"""