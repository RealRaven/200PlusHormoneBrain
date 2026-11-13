"""
infrastructure.brainparts.hindbrain.metencephalon.cerebellum.hemispheres.left
=============================================================================

Anatomical Hierarchy
--------------------
::

    hemispheres
    ├── left                                  <-- THIS MODULE
    │   ├── anterior_lobe
    │   ├── flocculonodular_lobe
    │   └── posterior_lobe
    └── right
        ├── anterior_lobe
        ├── flocculonodular_lobe
        └── posterior_lobe

**Primary synonym:** Left cerebellar hemisphere; hemispherium
cerebelli sinistrum; the left lateral cerebellar hemisphere; the
left cerebrocerebellar hemisphere; the left lateral zone of the
cerebellum.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
single grey-matter or white-matter structure.** A **single
suprasegmental region** — the **left** cerebellar hemisphere,
comprising the **cerebellar cortex** (the three-layered
grey-matter cortex over the left hemisphere) and the **underlying
white matter** (the folial white-matter branches of the arbor
vitae within the left hemisphere), organized into **three lobes**
(anterior, posterior, flocculonodular).
**Part of:** The **hemispheres** container — the **left member**
of the **paired lateral cerebellar division**. The
**hemispheres** are a **child sub-container of the cerebellum**;
the **cerebellum** is the **metencephalic suprasegmental
structure**; the **metencephalon** is the **rostral** of the
**two rhombencephalic sub-vesicles**; the **hindbrain** is the
**caudal** of the **three primary brain vesicles**.
**Structural parent:** ``.../hemispheres/`` → **direct child**
of the hemispheres container.
**Structural children:** **Three** — ``anterior_lobe/``,
``flocculonodular_lobe/``, and ``posterior_lobe/``. Each is a
**lobe sub-container**. The **cerebellar cortex** (the
three-layered grey-matter cortex over the left hemisphere), the
**folial white matter** (the white-matter branches of the arbor
vitae within the left hemisphere), the **cerebellar fissures**
(primary fissure, posterolateral fissure, horizontal fissure),
the **lobules** (simplex, ansiform, paramedian, semilunar,
biventer, tonsil, etc.), the **cerebellar zones** (vermal,
paravermal, hemispheral, lateral), and the **cerebellar
microzones** are documented as **prose** or as **children of
the lobe sub-containers**.
**Boundary status (LEFT — NOT the right cerebellar hemisphere):**
**Boundary case — the left cerebellar hemisphere is the LEFT
member of the paired cerebellar hemispheres, NOT the right
cerebellar hemisphere.** The **right cerebellar hemisphere**
(``.../hemispheres/right/``) is the **right member** of the
pair. The **left cerebellar hemisphere** (here) is the **left
member**. **They are DIFFERENT LATERAL DIVISIONS on DIFFERENT
SIDES** — **separated** by the **vermis** (the midline) and
**continuous** with it at the **paravermal zone**, but they are
**distinct left and right lateral divisions**. The two are
**bilaterally symmetric** — they are **mirror siblings** with
**partial lateralization** (**contested** — see
*Lateralization Notes*). Consumers must **not** conflate the
left cerebellar hemisphere with the right cerebellar hemisphere
— the **left** is the **left member**; the **right** is the
**right member**.
**Boundary status (LATERAL CEREBELLAR DIVISION — NOT the
vermis):** **Boundary case — the left cerebellar hemisphere is
the LATERAL cerebellar division (left side), NOT the vermis.**
The **vermis** (``.../cerebellum/vermis/``) is the **midline**
cerebellar division — the **spinocerebellum midline** (posture,
gait, axial motor control). The **left cerebellar hemisphere**
(here) is the **lateral** cerebellar division — the
**cerebrocerebellum lateral** (limb motor coordination, motor
learning, cognition). **They are DIFFERENT cerebellar
divisions** — the **vermis** is **midline**; the **left
cerebellar hemisphere** is **lateral**. They are **continuous**
at the **left paravermal zone** (the **intermediate** cerebellar
zone), but they are **distinct divisions**. Consumers must
**not** conflate the left cerebellar hemisphere with the vermis.
**Boundary status (CEREBELLAR — NOT the left cerebral
hemisphere):** **Boundary case — the left cerebellar hemisphere
is CEREBELLAR, NOT the left cerebral hemisphere.** The **left
cerebral hemisphere**
(``.../forebrain/telencephalon/cerebral_hemispheres/left/``) is
the **forebrain** structure — the **cortex**, the **white
matter** (centrum semiovale, corona radiata, internal capsule,
corpus callosum), the **basal ganglia**, the **hippocampus**,
the **amygdala**, the **left lateral ventricle**. The **left
cerebellar hemisphere** (here) is the **hindbrain** structure —
the **left** cerebellar lateral division. **They are DIFFERENT
structures in DIFFERENT brain vesicles** — the **left cerebral
hemisphere** is **forebrain**; the **left cerebellar
hemisphere** is **hindbrain**. The word **"hemisphere"** is
**shared** (both are "hemispheres"), but the **structures are
different** — consumers must **not** conflate the left
cerebellar hemisphere with the left cerebral hemisphere.
**Boundary status (CORTEX + WHITE MATTER — NOT the deep white
matter or the deep nuclei):** **Boundary case — the left
cerebellar hemisphere is CORTEX + WHITE MATTER (the left
hemispheral tissue), NOT the deep white matter or the deep
nuclei.** The **cerebellar deep white matter**
(``.../cerebellum/deep_white_matter/``) is the **white-matter
core** — the **arbor vitae** and the **intracerebellar tracts**
— that **spans** both hemispheres and the vermis. The
**cerebellar deep nuclei** (``.../cerebellum/nuclei/``) are the
**grey-matter output nuclei** — the **dentate nucleus**, the
**fastigial nucleus**, and the **interposed nucleus** — with
**bilateral pairs** of each. The **left cerebellar hemisphere**
(here) is the **left cerebellar tissue division** — the
**cortex** (grey matter) **plus** the **folial white matter**
(the white-matter branches within the left hemisphere). **The
left hemisphere is the LEFT LATERAL TISSUE DIVISION; the deep
white matter is the WHITE-MATTER CORE; the deep nuclei are the
GREY-MATTER OUTPUT NUCLEI (bilateral pairs).** Consumers must
**not** conflate the left cerebellar hemisphere with the deep
white matter or the deep nuclei.
**Boundary status (MEMBER OF A PAIR — NOT the hemispheres
container):** **Boundary case — the left cerebellar hemisphere
is a MEMBER of the paired cerebellar hemispheres, NOT the
hemispheres container.** The **hemispheres** container
(``.../cerebellum/hemispheres/``) contains the **left** and
**right** cerebellar hemispheres. The **left cerebellar
hemisphere** (here) is the **left member** of that pair.
**Consumers must not conflate the left cerebellar hemisphere
with the hemispheres container** — the **hemispheres** are the
**pair**; the **left hemisphere** is a **member**.
**Boundary status (NOT the cerebellum container — a
GRANDCHILD):** **Boundary case — the left cerebellar hemisphere
is a GRANDCHILD of the cerebellum (via the hemispheres
container), NOT the cerebellum container.** The **cerebellum**
(``.../cerebellum/``) is the **container** — the
**suprasegmental structure**; the **hemispheres**
(``.../cerebellum/hemispheres/``) is a **child sub-container**;
the **left cerebellar hemisphere** (here) is a **grandchild of
the cerebellum**. Consumers must **not** conflate the left
cerebellar hemisphere with the cerebellum container.
**Boundary status (NOT the metencephalon, hindbrain, or
brainstem — a DEEP DESCENDANT):** **Boundary case — the left
cerebellar hemisphere is a GRANDCHILD of the cerebellum (a
great-grandchild of the metencephalon, a
great-great-grandchild of the hindbrain), NOT the metencephalon,
hindbrain, or brainstem.** The **metencephalon**
(``.../metencephalon/``) is the **container** (pons + cerebellum
+ fourth ventricle); the **hindbrain** (``.../hindbrain/``) is
the **whole** rhombencephalon derivative; the **brainstem** is
the **segmental neuraxis** (midbrain + pons + medulla). The
**left cerebellar hemisphere** (here) is a **grandchild of the
cerebellum** — **five levels deep** from the brainparts root.
Consumers must **not** conflate the left cerebellar hemisphere
with the metencephalon, the hindbrain, or the brainstem.
**Boundary status (SUPRASEGMENTAL — NOT the brainstem):**
**Boundary case — the left cerebellar hemisphere is
SUPRASEGMENTAL, NOT the brainstem.** The **brainstem** is the
**segmental neuraxis** (midbrain + pons + medulla oblongata).
The **left cerebellar hemisphere** (here) is **suprasegmental**
— it is **part of the cerebellum**, which is **attached to the
brainstem** via the **cerebellar peduncles** (children of the
pons), but which is **NOT part of the brainstem** proper.
Consumers must **not** conflate the left cerebellar hemisphere
with the brainstem — the **left hemisphere** is
**suprasegmental**; the **brainstem** is **segmental**.
**Boundary status (NOT the fourth ventricle — a CSF cavity):**
**Boundary case — the left cerebellar hemisphere is LATERAL
CEREBELLUM, NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **left cerebellar hemisphere** (here) is the
**left cerebellar tissue division** — **dorsal** to the fourth
ventricle. Consumers must **not** conflate the left cerebellar
hemisphere with the fourth ventricle.
**Boundary status (NOT the cerebellar peduncles — those are
WHITE-MATTER TRACTS, children of the PONS):** **Boundary case
— the left cerebellar hemisphere is NOT the cerebellar
peduncles.** The **cerebellar peduncles** — the **superior
cerebellar peduncle**, the **middle cerebellar peduncle**, and
the **inferior cerebellar peduncle** — are the **white-matter
tracts** that **connect** the cerebellum to the brainstem
(midbrain, pons, medulla). In the tree, the **cerebellar
peduncles** are **children of the pons**
(``.../metencephalon/pons/cerebellar_peduncles/``), **not**
children of the cerebellum. The **left cerebellar hemisphere**
(here) is the **left cerebellar tissue division** — the
**cortex** and the **folial white matter**. **The peduncles are
the CONDUCTION INFRASTRUCTURE; the left hemisphere is TISSUE.**
Consumers must **not** conflate the left cerebellar hemisphere
with the cerebellar peduncles.
**Boundary status (HETEROGENEOUS — MULTIPLE lobes with DIFFERENT
functions):** **Boundary case — the left cerebellar hemisphere
is a HETEROGENEOUS lateral division with MULTIPLE lobes and
MULTIPLE functions, not a single uniform system.** The left
hemisphere includes:
*   **Anterior lobe** (``.../hemispheres/left/anterior_lobe/``)
    — the **spinocerebellum** (limb proprioception, motor
    execution).
*   **Posterior lobe** (``.../hemispheres/left/posterior_lobe/``)
    — the **cerebrocerebellum** (motor planning, motor
    learning, cognition — including the **cerebellar
    cognitive-affective syndrome**; the **left cerebellar
    hemisphere** is connected to the **right parietal lobe** —
    **visuospatial** function — **contested** lateralization).
*   **Flocculonodular lobe**
    (``.../hemispheres/left/flocculonodular_lobe/``) — the
    **vestibulocerebellum** (vestibular control, eye
    movements, balance).
**Each lobe is functionally distinct** — the tree wires the
**anterior_lobe**, **flocculonodular_lobe**, and
**posterior_lobe** as **sub-containers of the left hemisphere**.
Consumers must **not** treat the left cerebellar hemisphere as a
single uniform region — it is a **heterogeneous lateral
division** with **three functionally distinct lobes**.
**Boundary status (SLEA-FREE — the left cerebellar hemisphere is
NOT an extended-amygdala component):** **Boundary case — the
left cerebellar hemisphere is SLEA-FREE.** The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component**
in the amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The **left cerebellar
hemisphere** is a **lateral cerebellar division** — it is
**NOT** an extended-amygdala component, and it carries **NO
SLEA warning**. Consumers must **not** import the SLEA warning
into the left cerebellar hemisphere — it is **SLEA-free**.
**Boundary status (NOT a neural processor in the classical
sense — the left hemisphere is a REGION, not a single
processor):** **Boundary case — the left cerebellar hemisphere
is a REGION, not a single neural processor.** It **contains**
neural processors (the cerebellar cortex microzones of each
lobe, the Purkinje-cell output, the deep nuclei projections) —
but it is **not itself a processor**. The **processing**
happens in the **sub-structures** (the cerebellar cortex of
each lobe, the deep nuclei). Consumers must **not** treat the
left cerebellar hemisphere as a **single neural processor** — it
is a **lateral division** with **heterogeneous lobes**, each
with its own function.

Overview
--------
The left cerebellar hemisphere is the **left** of the two paired
cerebellar hemispheres — the **left lateral cerebellar division**
comprising the **cerebellar cortex** (the three-layered
grey-matter cortex over the left hemisphere) and the **underlying
white matter** (the folial white-matter branches of the arbor
vitae within the left hemisphere), organized into **three lobes**
(anterior, posterior, flocculonodular). It is a **sub-container**
under the **hemispheres** container, and it is the **left
member** of the **paired lateral cerebellar division**.

**The left cerebellar hemisphere is the LEFT member of the pair,
distinct from the right cerebellar hemisphere (the right
member).** The **right cerebellar hemisphere**
(``.../hemispheres/right/``) is the **right member** of the
pair. The two are **separated** by the **vermis** and
**continuous** with it at the **paravermal zone**, but they are
**distinct left and right lateral divisions**. They are
**bilaterally symmetric** — **mirror siblings** with **partial
lateralization** (**contested**).

**The left cerebellar hemisphere is the LATERAL cerebellar
division (left side), distinct from the vermis (the midline
division).** The **vermis** (``.../cerebellum/vermis/``) is
**midline**; the **left cerebellar hemisphere** (here) is
**lateral**. They are **continuous** at the **left paravermal
zone**, but they are **distinct divisions**.

**The left cerebellar hemisphere is NOT the left cerebral
hemisphere.** The **left cerebral hemisphere**
(``.../forebrain/telencephalon/cerebral_hemispheres/left/``) is
the **forebrain** structure; the **left cerebellar hemisphere**
(here) is the **hindbrain** structure — part of the **"little
brain."** The word **"hemisphere"** is **shared**, but the
**structures are different**.

**The left cerebellar hemisphere is a HETEROGENEOUS lateral
division, not a single structure.** It includes the **anterior
lobe** (spinocerebellum — limb proprioception, motor execution),
the **posterior lobe** (cerebrocerebellum — motor planning,
motor learning, cognition — including the **cerebellar
cognitive-affective syndrome**; the **left cerebellar
hemisphere** is connected to the **right parietal lobe** —
**visuospatial** function — **contested** lateralization), and
the **flocculonodular lobe** (vestibulocerebellum — vestibular
control, eye movements, balance). Each lobe is functionally
distinct.

**The left cerebellar hemisphere is a REGION, not a single
neural processor.** The **processing** happens in the
**sub-structures** (the cerebellar cortex of each lobe, the
deep nuclei). The **left hemisphere** is the **lateral
division** that **contains** those sub-structures.

Hemispheral Composition (sub-containers and prose)
--------------------------------------------------
The left cerebellar hemisphere is a **lateral division** with
**three lobe sub-containers** — documented as **structural
children** (``anterior_lobe/``, ``flocculonodular_lobe/``, and
``posterior_lobe/``) — and **many prose-defined sub-structures**
documented within those lobe sub-containers:

*   **Anterior Lobe**
    (``.../hemispheres/left/anterior_lobe/``) — the
    **spinocerebellum** (limb proprioception, motor execution).
    *   **Lobules** — the **lobule simplex** (HVI), the
        **anterior lobe** lobules (HII–HV), documented as
        **prose** or **children of the anterior_lobe**.

*   **Posterior Lobe**
    (``.../hemispheres/left/posterior_lobe/``) — the
    **cerebrocerebellum** (motor planning, motor learning,
    cognition — including the **cerebellar cognitive-affective
    syndrome**; the **left cerebellar hemisphere** is
    connected to the **right parietal lobe** — **visuospatial**
    function — **contested** lateralization).
    *   **Lobules** — the **ansiform lobule** (crus I, crus
        II), the **paramedian lobule** (HVIIB), the
        **semilunar lobules**, the **biventer lobule** (HVIII),
        the **tonsil** (HIX), documented as **prose** or
        **children of the posterior_lobe**.

*   **Flocculonodular Lobe**
    (``.../hemispheres/left/flocculonodular_lobe/``) — the
    **vestibulocerebellum** (vestibular control, eye
    movements, balance).
    *   **Components** — the **flocculus** (the **left
        flocculus**), the **nodulus** (the midline portion —
        **shared** with the vermis), documented as **prose** or
        **children of the flocculonodular_lobe**.

**These sub-structures are children of the lobe sub-containers
(or prose), not direct structural children of the left
cerebellar hemisphere.** The tree wires the **left cerebellar
hemisphere** as a **sub-container** with **three lobe
sub-containers** (``anterior_lobe/``,
``flocculonodular_lobe/``, and ``posterior_lobe/``) — the
**cerebellar cortex**, the **folial white matter**, the
**fissures** (primary fissure, posterolateral fissure,
horizontal fissure), the **lobules**, the **cerebellar zones**,
and the **cerebellar microzones** are documented as **prose**
or as **children of the lobe sub-containers**. Consumers that
need **lobule-level** resolution should consult the **lobe
sub-container modules** and the references, not the left
cerebellar hemisphere container.

The Left Cerebellar Hemisphere / Right Cerebellar Hemisphere Boundary
---------------------------------------------------------------------
This is the **left-vs-right** boundary:

*   **Left cerebellar hemisphere** (this module) — the **left
    member** of the paired cerebellar hemispheres.

*   **Right cerebellar hemisphere**
    (``.../hemispheres/right/``) — the **right member** of the
    paired cerebellar hemispheres.

**They are DIFFERENT LATERAL DIVISIONS on DIFFERENT SIDES** —
**separated** by the **vermis** and **continuous** with it at
the **paravermal zone**, but they are **distinct left and right
lateral divisions**. They are **bilaterally symmetric** —
**mirror siblings** with **partial lateralization**
(**contested**). Consumers must **not** conflate the left
cerebellar hemisphere with the right cerebellar hemisphere.

The Left Cerebellar Hemisphere / Vermis Boundary
------------------------------------------------
This is the **lateral-vs-midline** boundary:

*   **Left cerebellar hemisphere** (this module) — the **left
    lateral** cerebellar division.

*   **Vermis** (``.../cerebellum/vermis/``) — the **midline**
    cerebellar division.

**They are DIFFERENT cerebellar divisions** — the **vermis** is
**midline**; the **left cerebellar hemisphere** is **lateral**.
They are **continuous** at the **left paravermal zone** (the
**intermediate** cerebellar zone), but they are **distinct
divisions**. Consumers must **not** conflate the left
cerebellar hemisphere with the vermis.

The Left Cerebellar Hemisphere / Left Cerebral Hemisphere Boundary
------------------------------------------------------------------
This is the **hindbrain-vs-forebrain** boundary:

*   **Left cerebellar hemisphere** (this module) — the
    **hindbrain** structure (part of the **"little brain"**).

*   **Left cerebral hemisphere**
    (``.../forebrain/telencephalon/cerebral_hemispheres/left/``)
    — the **forebrain** structure (the **"brain"** — cortex,
    white matter, basal ganglia, hippocampus, amygdala, left
    lateral ventricle).

**They are DIFFERENT structures in DIFFERENT brain vesicles** —
the **left cerebral hemisphere** is **forebrain**; the **left
cerebellar hemisphere** is **hindbrain**. The word
**"hemisphere"** is **shared**, but the **structures are
different**. Consumers must **not** conflate the left cerebellar
hemisphere with the left cerebral hemisphere.

The Left Cerebellar Hemisphere / Deep White Matter Boundary
-----------------------------------------------------------
This is the **lateral-division-vs-white-matter-core**
boundary:

*   **Left cerebellar hemisphere** (this module) — the **left
    cerebellar tissue division** (cortex + folial white
    matter).

*   **Cerebellar deep white matter**
    (``.../cerebellum/deep_white_matter/``) — the
    **white-matter core** (arbor vitae and intracerebellar
    tracts).

**The left hemisphere is the LEFT LATERAL TISSUE DIVISION; the
deep white matter is the WHITE-MATTER CORE.** Consumers must
**not** conflate the left cerebellar hemisphere with the deep
white matter.

The Left Cerebellar Hemisphere / Deep Nuclei Boundary
-----------------------------------------------------
This is the **lateral-division-vs-grey-matter-output-nuclei**
boundary:

*   **Left cerebellar hemisphere** (this module) — the **left
    cerebellar tissue division**.

*   **Cerebellar deep nuclei** (``.../cerebellum/nuclei/``) —
    the **grey-matter output nuclei** (dentate, fastigial,
    interposed — with **bilateral pairs** of each).

**The left hemisphere is the LEFT LATERAL TISSUE DIVISION; the
deep nuclei are the GREY-MATTER OUTPUT NUCLEI.** Consumers must
**not** conflate the left cerebellar hemisphere with the deep
nuclei.

The Left Cerebellar Hemisphere / Hemispheres Container Boundary
---------------------------------------------------------------
This is the **member-vs-pair** boundary:

*   **Left cerebellar hemisphere** (this module) — the **left
    member** of the paired cerebellar hemispheres.

*   **Hemispheres** (``.../cerebellum/hemispheres/``) — the
    **paired lateral division** (left + right).

**The left hemisphere is a MEMBER of the pair; the hemispheres
are the PAIR.** Consumers must **not** conflate the left
cerebellar hemisphere with the hemispheres container.

The Left Cerebellar Hemisphere / Cerebellum Boundary
----------------------------------------------------
This is the **grandchild-vs-container** boundary:

*   **Left cerebellar hemisphere** (this module) — a
    **grandchild of the cerebellum** (via the hemispheres
    container).

*   **Cerebellum** (``.../cerebellum/``) — the **container**.

**The left cerebellar hemisphere is a GRANDCHILD of the
cerebellum.** Consumers must **not** conflate the left
cerebellar hemisphere with the cerebellum container.

The Left Cerebellar Hemisphere / Metencephalon and Hindbrain Boundary
---------------------------------------------------------------------
This is the **deep-descendant-vs-container** boundary:

*   **Left cerebellar hemisphere** (this module) — a
    **grandchild of the cerebellum** (a **great-grandchild of
    the metencephalon**, a **great-great-grandchild of the
    hindbrain**).

*   **Metencephalon** (``.../metencephalon/``) and **hindbrain**
    (``.../hindbrain/``) — the **containers**.

**The left cerebellar hemisphere is a GRANDCHILD of the
cerebellum** — **five levels deep** from the brainparts root.
Consumers must **not** conflate the left cerebellar hemisphere
with the metencephalon or the hindbrain.

The Left Cerebellar Hemisphere / Brainstem Boundary
---------------------------------------------------
This is the **suprasegmental-vs-segmental** boundary:

*   **Left cerebellar hemisphere** (this module) — the
    **suprasegmental** left lateral cerebellar division.

*   **Brainstem** (midbrain + pons + medulla oblongata) — the
    **segmental neuraxis**.

**The left cerebellar hemisphere is SUPRASEGMENTAL, not
brainstem.** It is **part of the cerebellum**, which is
**attached to the brainstem** via the **cerebellar peduncles**,
but which is **NOT part of the brainstem** proper. Consumers
must **not** conflate the left cerebellar hemisphere with the
brainstem.

The Left Cerebellar Hemisphere / Fourth Ventricle Boundary
----------------------------------------------------------
This is the **lateral-cerebellum-vs-CSF-cavity** boundary:

*   **Left cerebellar hemisphere** (this module) — the **left
    cerebellar tissue division**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The fourth ventricle is a CSF CAVITY; the left cerebellar
hemisphere is TISSUE.** Consumers must **not** conflate the left
cerebellar hemisphere with the fourth ventricle.

The Left Cerebellar Hemisphere / Cerebellar Peduncles Boundary
--------------------------------------------------------------
This is the **tissue-vs-white-matter-tract** boundary:

*   **Left cerebellar hemisphere** (this module) — the **left
    cerebellar tissue division**.

*   **Cerebellar peduncles** — the **white-matter tracts**
    connecting the cerebellum to the brainstem (children of
    the **pons** in the tree).

**The peduncles are the CONDUCTION INFRASTRUCTURE; the left
hemisphere is TISSUE.** Consumers must **not** conflate the left
cerebellar hemisphere with the cerebellar peduncles.

The Left Cerebellar Hemisphere / SLEA Boundary
----------------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Left cerebellar hemisphere** (this module) —
    **SLEA-FREE**. No extended-amygdala relationship, no SLEA
    warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**,
    **ventral pallidum**, and **nucleus accumbens** (wired
    elsewhere).

**The left cerebellar hemisphere is NOT part of the SLEA
continuum.** It is a **lateral cerebellar division**, and it
carries **no SLEA warning**. Consumers must **not** import the
SLEA warning into the left cerebellar hemisphere.

Function in the Human Brain
---------------------------
The left cerebellar hemisphere's functions are **heterogeneous**
— documented at the **lobe** level, not at the division level:

*   **Motor Coordination and Balance (Anterior, Posterior, and
    Flocculonodular Lobes):** The **anterior lobe**
    (spinocerebellum) — limb proprioception and motor
    execution; the **posterior lobe** (cerebrocerebellum) —
    limb motor planning and execution, motor learning; the
    **flocculonodular lobe** (vestibulocerebellum) —
    vestibular control, balance, and eye movements.

*   **Motor Learning (Posterior Lobe):** The **posterior lobe**
    of the left hemisphere is the **neural substrate** of
    **motor learning** — the **cerebellar cortex** (Purkinje
    cells) and the **deep nuclei** (dentate, interposed) are
    **plastic** during **motor adaptation**, **classical
    conditioning** (e.g., **eyeblink conditioning**), and
    **skill learning**.

*   **Cerebellar Cognitive-Affective Syndrome (CCAS —
    Posterior Lobe):** The **posterior lobe** of the left
    hemisphere — especially the **lateral** portion — is
    involved in **executive function**, **visuospatial
    processing**, **language**, and **affective regulation**.
    Lesions cause **cerebellar cognitive-affective syndrome**
    (CCAS) — **executive dysfunction**, **visuospatial
    deficits**, **language deficits**, and **affective
    dysregulation**.

*   **Vestibular Control and Eye Movements (Flocculonodular
    Lobe):** The **flocculonodular lobe** of the left
    hemisphere is involved in **vestibular control**,
    **balance**, and **eye movements** (the
    **vestibulo-ocular reflex**, **saccadic accuracy**,
    **smooth pursuit**).

*   **Partial Lateralization (Contested — Visuospatial):** The
    **left cerebellar hemisphere** (and its hemispheral
    cortex) is connected to the **right parietal lobe** —
    **visuospatial** function (the **left cerebellar
    hemisphere** is more involved in **visuospatial** tasks).
    This is **partial**, **contested**, and documented in the
    **cerebellum module** (not at the left-hemisphere level).

*   **NOT a single neural processor.** The left cerebellar
    hemisphere is a **lateral division** — the **processing**
    happens in the **sub-structures** (the cerebellar cortex of
    each lobe, the deep nuclei). Consumers must **not** treat
    the left cerebellar hemisphere as a **single processor** —
    it is a **lateral division** with **heterogeneous lobes**.

**The unifying theme:** the left cerebellar hemisphere is the
**left lateral cerebellar division** — comprising the
**cerebellar cortex** and the **folial white matter**,
organized into **three lobes** (anterior, posterior,
flocculonodular) — **coordinating left limb motor execution,
motor learning, balance, eye movements, and non-motor
(cognitive-affective) functions**. It is a **heterogeneous
lateral division**, **NOT a single neural processor**, and
**NOT the right hemisphere, the vermis, the left cerebral
hemisphere, the deep white matter, the deep nuclei, the
hemispheres container, the cerebellum, the metencephalon, the
hindbrain, the brainstem, or the fourth ventricle**.

Associated Disorders
--------------------
The left cerebellar hemisphere has **named clinical syndromes**
— its clinical associations are **cerebellar** (via the
**lobes**, the **cerebellar cortex**, and the **deep nuclei**
of the left hemisphere):

*   **Left Hemispheral Cerebellar Ataxia (via the Left
    Hemisphere):** **Left limb ataxia**, **dysmetria**,
    **dysdiadochokinesia**, **intention tremor**, and
    **dysarthria** — the **left hemispheral cerebellar motor
    syndrome**. The **posterior lobe** of the left hemisphere
    is the **primary substrate** for the **left limb ataxia**;
    the **anterior lobe** for the **left gait ataxia**
    component. Causes include **cerebellar stroke** (left
    PICA, left AICA, left SCA infarcts), **cerebellar
    hemorrhage**, **cerebellar tumors**, **multiple sclerosis**
    (left cerebellar plaques), and **paraneoplastic
    cerebellar degeneration**.

*   **Spinocerebellar Ataxias (SCAs — via the Left
    Hemisphere):** A group of **genetically inherited
    cerebellar ataxias** — **autosomal dominant**
    (SCA1–SCA48+), **autosomal recessive** (Friedreich
    ataxia), and **X-linked** — with **progressive cerebellar
    ataxia** as the core phenotype, often with **brainstem**,
    **basal ganglia**, **retinal**, and **cognitive**
    involvement. The **left cerebellar hemisphere** is a
    **primary substrate**.

*   **Cerebellar Cognitive-Affective Syndrome (CCAS — via the
    Left Posterior Lobe):** **Executive dysfunction**,
    **visuospatial deficits**, **language deficits**
    (agrammatism, dysprosodia), **affective dysregulation** —
    caused by **left cerebellar hemispheral lesions**
    (especially the **left posterior lobe**). The **left
    cerebellar hemisphere** is the **substrate** — the
    **left cerebellar-cortical loops** (left cerebellum →
    right thalamus → right parietal / left prefrontal cortex)
    are the **mechanism**. The **left cerebellar hemisphere**
    is the **visuospatial substrate** (connected to the
    **right parietal lobe** — **contested** lateralization).

*   **Cerebellar Tumors (Left Hemispheral — via the Left
    Hemisphere):** **Pilocytic astrocytoma** (the most common
    **benign pediatric brain tumor**, arising in the **left
    cerebellar hemisphere**), **hemangioblastoma** (adult,
    left cerebellar hemisphere), **metastatic tumors** (left
    cerebellar hemisphere — the **most common adult
    cerebellar tumor** is **metastasis**), and
    **medulloblastoma** (typically arising in the **vermis**,
    but can involve the left hemisphere). The **left
    cerebellar hemisphere** is a **primary substrate**.

*   **Cerebellar Stroke (Left Hemispheral — via the Left
    Hemisphere):** **Left PICA infarct** (lateral medullary
    syndrome — involves the **left inferior cerebellar
    peduncle** and the **left cerebellar hemisphere**),
    **left AICA infarct** (lateral pontine syndrome —
    involves the **left middle cerebellar peduncle** and the
    **left cerebellar hemisphere**), and **left SCA infarct**
    (superior cerebellar syndrome — involves the **left
    superior cerebellar peduncle** and the **left cerebellar
    hemisphere**). The **left cerebellar hemisphere** is the
    **substrate**.

*   **Cerebellar Hemorrhage (Left Hemispheral — via the Left
    Hemisphere):** **Hypertensive cerebellar hemorrhage** —
    typically in the **left cerebellar hemisphere** — can
    cause **rapid neurological deterioration** (due to
    **fourth-ventricle compression** and **brainstem
    compression**) and requires **emergency neurosurgical
    evacuation**. The **left cerebellar hemisphere** is the
    **substrate**.

*   **Paraneoplastic Cerebellar Degeneration (Left Hemispheral
    — via the Left Hemisphere):** **Anti-Yo**, **anti-Hu**,
    **anti-Tr**, **anti-Ri**, and **anti-metabotropic
    glutamate receptor 1 (mGluR1)** antibodies —
    **paraneoplastic cerebellar degeneration** associated
    with **ovarian cancer**, **breast cancer**, **Hodgkin
    lymphoma**, and other malignancies. The **left cerebellar
    Purkinje cells** (in the **left hemisphere**) are the
    **primary target**.

*   **Multiple Sclerosis (Left Hemispheral — via the Left
    Hemisphere):** **Demyelinating plaques** in the **left
    cerebellar hemisphere** — the **left cerebellar
    peduncles**, the **left cerebellar white matter**, and
    the **left cerebellar cortex** — causing **left
    cerebellar ataxia**, **dysarthria**, **nystagmus**, and
    **intention tremor**. The **left cerebellar hemisphere**
    is a **substrate**.

*   **No Named "Left Cerebellar Hemisphere Syndrome"
    (singular):** The left cerebellar hemisphere has
    **multiple named clinical syndromes** (left hemispheral
    cerebellar ataxia, CCAS, SCAs, pilocytic astrocytoma,
    etc.) — but **no single "left cerebellar hemisphere
    syndrome."** Its clinical relevance is **cerebellar** —
    via the **lobes**, the **cerebellar cortex**, and the
    **deep nuclei** of the left hemisphere.

**What is NOT here:** The left cerebellar hemisphere is **not**
the substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (central nucleus + basolateral nuclei),
**Urbach-Wiethe disease** (amygdala), or **Parkinson's disease**
(substantia nigra, in the midbrain). Its clinical relevance is
**cerebellar** — **left hemispheral cerebellar ataxia**,
**CCAS**, **SCAs**, **cerebellar tumors**, and **cerebellar
stroke**.

Lateralization Notes
--------------------
This is the **left** cerebellar hemisphere module. The left and
right cerebellar hemispheres are **bilaterally symmetric** and
**partially lateralized** — and the left carries **NO warning**:

*   **Bilateral Symmetry:** The **left** and **right**
    cerebellar hemispheres are **structurally symmetric** —
    same three lobes, same cerebellar cortex, same folial
    white matter, same deep nuclei projections (via the
    peduncles).

*   **Partial Lateralization (Contested — Visuospatial):** The
    **left cerebellar hemisphere** is connected to the
    **right parietal lobe** — **visuospatial** function (the
    **left cerebellar hemisphere** is more involved in
    **visuospatial** tasks). The **right cerebellar
    hemisphere** is connected to the **left frontal lobe** —
    **language** (the **right cerebellar hemisphere** is more
    involved in **verbal/language** tasks). This is
    **partial**, **contested**, and documented in the
    **cerebellum module** (not at the left-hemisphere level).

*   **NO Extended-Amygdala Warning (SLEA-free):** The left
    cerebellar hemisphere is **NOT** an extended-amygdala
    component. It carries **no SLEA warning**. Consumers must
    **not** import the SLEA warning into the left cerebellar
    hemisphere.

*   **NO Amygdala-Lateralization Warning:** The left cerebellar
    hemisphere is **NOT** the fear-output or the
    fear-learning structure. It is a **lateral cerebellar
    division** — consumers must **not** conflate it with the
    **amygdala** or the **fear circuit**.

**A consumer that assumes "left cerebellar hemisphere = right
cerebellar hemisphere" will be structurally correct** — the two
sides are **symmetric** and **partially lateralized** (the
lateralization is documented in the cerebellum module). The left
cerebellar hemisphere carries **NO warning** — **no SLEA
warning**, **no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**. The partial cerebellar
lateralization (visuospatial = left cerebellar; language = right
cerebellar) is **contested** and documented as **prose**, not as
a **warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only — does
    **not** import from ``.../hemispheres/right/``.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../hemispheres/`` (parent),
    ``.../cerebellum/`` (grandparent),
    ``.../cerebellum/deep_white_matter/`` (sibling of the
    parent), ``.../cerebellum/nuclei/`` (sibling of the
    parent), ``.../cerebellum/vermis/`` (sibling of the
    parent), ``.../metencephalon/`` (great-grandparent),
    ``.../metencephalon/pons/cerebellar_peduncles/`` (the
    peduncles are **children of the pons**, not of the
    cerebellum), ``.../metencephalon/fourth_ventricle/``,
    ``.../hindbrain/``, ``.../midbrain/``,
    ``.../forebrain/telencephalon/cerebral_hemispheres/left/``
    (the left cerebral hemisphere), or any other container.
    The left cerebellar hemisphere's relationships to the
    right cerebellar hemisphere, the vermis, the left cerebral
    hemisphere, the deep white matter, the deep nuclei, the
    hemispheres container, the cerebellum, the metencephalon,
    the hindbrain, the brainstem, the fourth ventricle, and
    the cerebellar peduncles are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Sub-container module — three structural children.** The
    ``anterior_lobe/``, ``flocculonodular_lobe/``, and
    ``posterior_lobe/`` are **lobe sub-containers**. The
    **cerebellar cortex**, the **folial white matter**, the
    **fissures**, the **lobules**, the **cerebellar zones**,
    and the **cerebellar microzones** are **prose** or
    **children of the lobe sub-containers**. Consumers must not
    assume any exist as direct children of the left cerebellar
    hemisphere; resolve lobule-level detail through the lobe
    sub-containers and the references.
*   **LATERAL CEREBELLAR DIVISION (LEFT) — NOT the right
    hemisphere.** The **right cerebellar hemisphere** is the
    **right member** of the pair; the **left cerebellar
    hemisphere** is the **left member**.
*   **LATERAL CEREBELLAR DIVISION — NOT the vermis.** The
    **vermis** is the **midline** cerebellar division; the
    **left cerebellar hemisphere** is **lateral**.
*   **CEREBELLAR — NOT the left cerebral hemisphere.** The
    **left cerebral hemisphere** is **forebrain**; the **left
    cerebellar hemisphere** is **hindbrain**.
*   **LATERAL TISSUE DIVISION — NOT the deep white matter or
    the deep nuclei.** The **deep white matter** is the
    **white-matter core**; the **deep nuclei** are the
    **grey-matter output nuclei** (bilateral pairs).
*   **MEMBER OF A PAIR — NOT the hemispheres container.** The
    **hemispheres** are the **pair**; the **left hemisphere**
    is a **member**.
*   **NOT the cerebellum — a GRANDCHILD.** The **cerebellum**
    is the **container**; the **left cerebellar hemisphere** is
    a **grandchild** of the cerebellum (via the hemispheres
    container).
*   **NOT the metencephalon or hindbrain — a DEEP DESCENDANT.**
    The **left cerebellar hemisphere** is a **great-grandchild**
    of the metencephalon (a **great-great-grandchild** of the
    hindbrain).
*   **NOT the brainstem — SUPRASEGMENTAL.** The **left
    cerebellar hemisphere** is **suprasegmental** — part of
    the cerebellum, which is **attached to the brainstem** via
    the **cerebellar peduncles**, but which is **NOT part of
    the brainstem** proper.
*   **NOT the fourth ventricle — a CSF cavity.**
*   **NOT the cerebellar peduncles — those are WHITE-MATTER
    TRACTS, children of the PONS.**
*   **SLEA-FREE — no extended-amygdala relationship.** The left
    cerebellar hemisphere is **not** an extended-amygdala
    component, and it carries **no SLEA warning**.
*   **NOT a single neural processor — the left hemisphere is a
    REGION.** The **processing** happens in the **sub-structures**
    (the cerebellar cortex of each lobe, the deep nuclei).
*   **No ``AREA_PATHS`` hop.** The left cerebellar hemisphere
    is a **local sub-container** under the hemispheres
    container, not a **cross-listed container**.
*   **No nested cross-listing.** The left cerebellar
    hemisphere has **no nested dual-framing module**. It is a
    **single sub-container** with three lobe sub-containers.
*   **Structural parity with right cerebellar hemisphere —
    strict mirror with NO warning.** The left and right
    cerebellar hemisphere modules are **structurally
    identical** — same sub-container status, same three lobe
    sub-containers, same **SLEA-free** status, same **no
    warning**. The partial cerebellar lateralization
    (visuospatial = left; language = right) is **contested**
    and documented as **prose**, not as a **warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.cerebellum.hemispheres import left

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.cerebellum.hemispheres.left"
    )
    anterior_lobe_path = (
        "hindbrain.metencephalon.cerebellum.hemispheres.left."
        "anterior_lobe"
    )
    posterior_lobe_path = (
        "hindbrain.metencephalon.cerebellum.hemispheres.left."
        "posterior_lobe"
    )
    flocculonodular_lobe_path = (
        "hindbrain.metencephalon.cerebellum.hemispheres.left."
        "flocculonodular_lobe"
    )

**Do not** assume the left cerebellar hemisphere is the **right
cerebellar hemisphere**. The **right** is the **right member**
of the pair; the **left** is the **left member**.

**Do not** assume the left cerebellar hemisphere is the
**vermis**. The **vermis** is the **midline** division; the
**left hemisphere** is **lateral**.

**Do not** assume the left cerebellar hemisphere is the **left
cerebral hemisphere**. The **left cerebral hemisphere** is
**forebrain**; the **left cerebellar hemisphere** is
**hindbrain**.

**Do not** assume the left cerebellar hemisphere is the **deep
white matter** or the **deep nuclei**. The **deep white
matter** is the **white-matter core**; the **deep nuclei** are
the **grey-matter output nuclei**.

**Do not** assume the left cerebellar hemisphere is the
**hemispheres** container. The **hemispheres** are the
**pair**; the **left hemisphere** is a **member**.

**Do not** assume the left cerebellar hemisphere is the
**cerebellum**, **metencephalon**, **hindbrain**, or
**brainstem**. The **left cerebellar hemisphere** is a
**grandchild of the cerebellum** (a **great-grandchild of the
metencephalon**, a **great-great-grandchild of the
hindbrain**).

**Do not** assume the left cerebellar hemisphere is the
**fourth ventricle**. The **fourth ventricle** is a **CSF
cavity**.

**Do not** assume the left cerebellar hemisphere is the
**cerebellar peduncles**. The **peduncles** are the
**white-matter tracts** (children of the **pons**).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the left cerebellar
hemisphere. **The left cerebellar hemisphere is SLEA-FREE** —
it is **not** an extended-amygdala component, and it is **NOT
the fear-output structure**.

Iterating the left cerebellar hemisphere's children
(recommended consumer pattern)::

    LEFT_CEREBELLAR_HEMISPHERE_CHILDREN = (
        "anterior_lobe", "flocculonodular_lobe", "posterior_lobe",
    )
    # The anterior_lobe, flocculonodular_lobe, and posterior_lobe
    # are lobe sub-containers.

Reaching the right cerebellar hemisphere (recommended consumer
pattern — the mirror sibling)::

    # The right cerebellar hemisphere is the RIGHT member of the
    # pair:
    #
    #   hindbrain.metencephalon.cerebellum.hemispheres.right
    #
    # The left and right hemispheres are bilaterally symmetric —
    # mirror siblings with partial lateralization (contested).

Reaching the vermis (recommended consumer pattern — the midline
division)::

    # The vermis is the MIDLINE cerebellar division:
    #
    #   hindbrain.metencephalon.cerebellum.vermis
    #
    # The left cerebellar hemisphere is LATERAL; the vermis is
    # MIDLINE. They are continuous at the left paravermal zone.

Reaching the hemispheres container (recommended consumer pattern
— the parent)::

    # The hemispheres are the PAIRED lateral division:
    #
    #   hindbrain.metencephalon.cerebellum.hemispheres
    #
    # The left cerebellar hemisphere is a MEMBER of the pair.

Reaching the cerebellum (recommended consumer pattern — the
grandparent)::

    # The cerebellum is the CONTAINER:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The left cerebellar hemisphere is a GRANDCHILD of the
    # cerebellum (via the hemispheres container).

Reaching the left cerebral hemisphere (recommended consumer
pattern — NOTE the hindbrain-vs-forebrain boundary)::

    # The left cerebral hemisphere is the FOREBRAIN structure:
    #
    #   forebrain.telencephalon.cerebral_hemispheres.left
    #
    # The left cerebellar hemisphere is a HINDBRAIN structure.

Reaching the deep white matter (recommended consumer pattern —
NOTE the lateral-division-vs-white-matter-core boundary)::

    # The deep white matter is the WHITE-MATTER CORE (arbor
    # vitae):
    #
    #   hindbrain.metencephalon.cerebellum.deep_white_matter
    #
    # The left hemisphere is the LEFT LATERAL TISSUE DIVISION;
    # the deep white matter is the WHITE-MATTER CORE.

Reaching the deep nuclei (recommended consumer pattern — NOTE
the lateral-division-vs-grey-matter-output-nuclei boundary)::

    # The deep nuclei are the GREY-MATTER OUTPUT NUCLEI (with
    # bilateral pairs):
    #
    #   hindbrain.metencephalon.cerebellum.nuclei
    #
    # The left hemisphere is the LEFT LATERAL TISSUE DIVISION;
    # the deep nuclei are the GREY-MATTER OUTPUT NUCLEI.

Reaching the metencephalon (recommended consumer pattern — the
great-grandparent)::

    # The metencephalon is the CONTAINER (pons + cerebellum +
    # fourth ventricle):
    #
    #   hindbrain.metencephalon
    #
    # The left cerebellar hemisphere is a GREAT-GRANDCHILD of
    # the metencephalon.

Reaching the hindbrain (recommended consumer pattern — the
great-great-grandparent)::

    # The hindbrain is the WHOLE rhombencephalon derivative:
    #
    #   hindbrain
    #
    # The left cerebellar hemisphere is a GREAT-GREAT-GRANDCHILD
    # of the hindbrain.

Reaching the brainstem (recommended consumer pattern — the
suprasegmental-vs-segmental boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons +
    # medulla):
    #
    #   midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The left cerebellar hemisphere is SUPRASEGMENTAL — part
    # of the cerebellum, NOT part of the brainstem.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the lateral-cerebellum-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The fourth ventricle is a CSF CAVITY; the left cerebellar
    # hemisphere is TISSUE.

Reaching the cerebellar peduncles (recommended consumer pattern
— NOTE the tissue-vs-white-matter-tract boundary)::

    # The cerebellar peduncles are the WHITE-MATTER TRACTS —
    # children of the PONS:
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles
    #
    # The peduncles are the CONDUCTION INFRASTRUCTURE; the left
    # hemisphere is TISSUE.

Lobe-level detail (not wired at the left-hemisphere level —
consult the lobe sub-containers and references)::

    # The left cerebellar hemisphere's lobe-level detail is
    # prose within the lobe sub-containers:
    #   anterior_lobe -> spinocerebellum (limb proprioception)
    #   posterior_lobe -> cerebrocerebellum (motor planning,
    #                     motor learning, cognition, visuospatial
    #                     — left hemisphere -> right parietal)
    #   flocculonodular_lobe -> vestibulocerebellum (vestibular
    #                            control, eye movements)
    #
    # Do not attempt to resolve the lobes as sub-paths of the
    # left cerebellar hemisphere.

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
    infarct — lateral medullary syndrome; left cerebellar
    hemisphere involvement in left-sided infarcts.)
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
*   **SLEA (contrast — the left cerebellar hemisphere is NOT
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA continuum — BNST, central nucleus, ventral
    pallidum, nucleus accumbens; NOT the left cerebellar
    hemisphere.)
*   NeuroNames — Cerebellar hemisphere (left); FMA — Cerebellar
    hemisphere (left member).
"""