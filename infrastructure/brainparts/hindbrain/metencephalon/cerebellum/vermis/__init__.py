"""
infrastructure.brainparts.hindbrain.metencephalon.cerebellum.vermis
===================================================================

Anatomical Hierarchy
--------------------
::

    cerebellum
    ├── deep_white_matter
    ├── hemispheres
    ├── nuclei
    └── vermis                                <-- THIS MODULE
        ├── anterior_lobe
        ├── flocculonodular_lobe
        └── posterior_lobe

**Primary synonym:** Cerebellar vermis; vermis cerebelli; the vermis;
the midline cerebellar vermis; the median cerebellar division;
the vermal zone; the spinocerebellum midline; the
vestibulocerebellum midline; the "worm" (from Latin *vermis* —
worm); the medial cerebellar division.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
single grey-matter or white-matter structure.** A **single
midline cerebellar division** — the **midline region** of the
cerebellum, comprising the **vermal cerebellar cortex** (the
three-layered grey-matter cortex over lobules I–X), the
**vermal folial white matter** (the white-matter branches of
the arbor vitae within the vermis), and the **vermal lobes**
(anterior, posterior, flocculonodular) — organized along the
**midline** of the cerebellum, continuous with the **hemispheres**
at the **paravermal zone** (the **intermediate** cerebellar
zone).
**Part of:** The **cerebellum** container — the **midline
cerebellar division**. The **cerebellum** is the
**metencephalic suprasegmental structure**; the
**metencephalon** is the **rostral** of the **two
rhombencephalic sub-vesicles**; the **hindbrain** is the
**caudal** of the **three primary brain vesicles**.
**Structural parent:** ``.../cerebellum/`` → **direct child**
of the cerebellum container.
**Structural children:** **Three** — ``anterior_lobe/``,
``flocculonodular_lobe/``, and ``posterior_lobe/``. Each is a
**lobe sub-container**. The **vermal lobules** (I–X — the
vermal anterior lobe lobules I–V, the vermal posterior lobe
lobules VI–IX, and the vermal flocculonodular lobe lobule X),
the **vermal cerebellar cortex**, the **vermal folial white
matter**, the **primary fissure** (fissura prima), the
**posterolateral fissure** (fissura posterolateralis), the
**preculminate**, **intraculminate**, **prepyramidal**,
**secondary**, and **horizontal** fissures, the **vermal
zones** (vermal, paravermal, intermediate), and the **vermal
microzones** are documented as **prose** or as **children of
the lobe sub-containers**.
**Boundary status (MIDLINE DIVISION — NOT the cerebellar
hemispheres):** **Boundary case — the cerebellar vermis is the
MIDLINE division, NOT the cerebellar hemispheres.** The
**cerebellar hemispheres** (``.../cerebellum/hemispheres/``)
are the **lateral** cerebellar division — the **left** and
**right** cerebellar hemispheres, comprising the **lateral**
cerebellar cortex and folial white matter. The **cerebellar
vermis** (here) is the **midline** cerebellar division — the
**median** cerebellar cortex and folial white matter.
**They are DIFFERENT cerebellar divisions** — the
**hemispheres** are **lateral**; the **vermis** is **midline**.
They are **continuous** at the **paravermal zone** (the
**intermediate** cerebellar zone), but they are **distinct
divisions**. Consumers must **not** conflate the cerebellar
vermis with the cerebellar hemispheres.
**Boundary status (MIDLINE DIVISION — NOT the deep nuclei):**
**Boundary case — the cerebellar vermis is the MIDLINE cortical
division, NOT the cerebellar deep nuclei.** The **cerebellar
deep nuclei** (``.../cerebellum/nuclei/``) — the **dentate
nucleus**, the **interposed nucleus** (the **emboliform
nucleus** + the **globose nucleus**), and the **fastigial
nucleus** — are the **grey-matter output nuclei** of the
cerebellum. The **cerebellar vermis** (here) is the **midline
cortical division** — the **vermal cortex** and **folial white
matter** that **project to** the deep nuclei. **The vermis is
the MIDLINE CORTICAL DIVISION; the deep nuclei are the
GREY-MATTER OUTPUT NUCLEI.** They are **DIFFERENT
STRUCTURES** — the **vermis** is **cortical**; the **deep
nuclei** are **deep grey matter**. The **vermal anterior lobe**
projects to the **fastigial nucleus**; the **vermal nodulus**
projects to the **fastigial nucleus** — those are
**connections**, not identities. Consumers must **not**
conflate the cerebellar vermis with the cerebellar deep nuclei.
**Boundary status (CORTICAL DIVISION — NOT the cerebellar
cortex alone):** **Boundary case — the cerebellar vermis is the
MIDLINE CORTICAL DIVISION, NOT the cerebellar cortex alone.**
The **cerebellar cortex** — the **three-layered grey-matter
cortex** (**molecular layer**, **Purkinje cell layer**,
**granular layer**) — is the **grey-matter cortex** that
**covers** the cerebellar folia (including the vermal folia).
The **cerebellar vermis** (here) is the **midline cortical
division** — the **vermal cortex** **plus** the **vermal folial
white matter** (the white-matter branches within the vermal
folia) **plus** the **vermal lobes** (anterior, posterior,
flocculonodular). **The cortex is a LAYER within the vermis;
the vermis is the WHOLE midline division.** The **cerebellar
cortex** is documented as **prose** (not a structural child of
the vermis). Consumers must **not** conflate the cerebellar
vermis with the cerebellar cortex.
**Boundary status (CORTICAL DIVISION — NOT the deep white
matter):** **Boundary case — the cerebellar vermis is the
MIDLINE CORTICAL DIVISION, NOT the deep white matter.** The
**cerebellar deep white matter**
(``.../cerebellum/deep_white_matter/``) is the **white-matter
core** — the **arbor vitae** and the **intracerebellar
tracts** — that **spans** the hemispheres and the vermis. The
**cerebellar vermis** (here) is the **midline cortical
division** — the **vermal cortex** **plus** the **vermal folial
white matter** (a **component** of the arbor vitae, within the
vermal folia). **The vermis is the MIDLINE CORTICAL DIVISION;
the deep white matter is the WHITE-MATTER CORE that spans all
the divisions.** Consumers must **not** conflate the cerebellar
vermis with the deep white matter.
**Boundary status (VERMAL — NOT the fastigial nucleus):**
**Boundary case — the cerebellar vermis is the VERMAL cortical
division, NOT the fastigial nucleus.** The **fastigial
nucleus** (``.../cerebellum/nuclei/fastigial_nucleus/``) is the
**medial output nucleus** of the cerebellum — the **grey-matter
output nucleus** that **receives** the **Purkinje-cell output**
of the **vermis** (the vermal anterior lobe and the vermal
nodulus) and **projects** (via the **juxtarestiform body** —
the **uncinate fasciculus of Russell** and the **fastigial
efferents**) **bilaterally** to the **vestibular nuclei** and
the **reticular formation**, and to the **contralateral
thalamus VL**. The **cerebellar vermis** (here) is the
**midline cortical division** — the **vermal cortex** and
**folial white matter** that **project to** the fastigial
nucleus. **The vermis is the MIDLINE CORTICAL DIVISION; the
fastigial nucleus is the MEDIAL OUTPUT NUCLEUS.** They are
**DIFFERENT STRUCTURES** — the **vermis** is **cortical**; the
**fastigial nucleus** is **deep grey matter**. The **vermal
anterior lobe** and the **vermal nodulus** project to the
**fastigial nucleus** — that is a **connection**, not an
identity. Consumers must **not** conflate the cerebellar vermis
with the fastigial nucleus.
**Boundary status (VERMAL — NOT the vestibular nuclei):**
**Boundary case — the cerebellar vermis is the VERMAL cortical
division, NOT the vestibular nuclei.** The **vestibular nuclei**
(medial, superior, lateral, inferior — in the **pons** and
**medulla**) are the **brainstem vestibular nuclei** — the
**primary output target** of the **flocculonodular lobe** (the
flocculus projects **directly** to the vestibular nuclei, **not**
to the deep nuclei). The **cerebellar vermis** (here) is the
**midline cortical division** — the **vermal cortex** and
**folial white matter**. **They are DIFFERENT STRUCTURES** —
the **vermis** is **cerebellar grey and white matter**; the
**vestibular nuclei** are **brainstem grey matter**. Consumers
must **not** conflate the cerebellar vermis with the vestibular
nuclei.
**Boundary status (VERMAL — NOT the brainstem):** **Boundary
case — the cerebellar vermis is the VERMAL cortical division,
NOT the brainstem.** The **brainstem** is the **segmental
neuraxis** (midbrain + pons + medulla oblongata). The
**cerebellar vermis** (here) is **suprasegmental** — it is
**part of the cerebellum**, which is **attached to the
brainstem** via the **cerebellar peduncles** (children of the
pons), but which is **NOT part of the brainstem** proper.
Consumers must **not** conflate the cerebellar vermis with the
brainstem — the **vermis** is **suprasegmental**; the
**brainstem** is **segmental**.
**Boundary status (VERMAL — NOT the fourth ventricle):**
**Boundary case — the cerebellar vermis is the VERMAL cortical
division, NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **cerebellar vermis** (here) is the **midline
cortical division** — the **vermal cortex** and **folial white
matter** — **dorsal** to the fourth ventricle. The **vermis**
**forms part of the roof** of the fourth ventricle (via the
**superior medullary velum** and the **inferior medullary
velum**) — but the **vermis** is **NOT** the fourth ventricle.
Consumers must **not** conflate the cerebellar vermis with the
fourth ventricle.
**Boundary status (VERMAL — NOT the cerebellar peduncles):**
**Boundary case — the cerebellar vermis is the VERMAL cortical
division, NOT the cerebellar peduncles.** The **cerebellar
peduncles** — the **superior cerebellar peduncle**, the
**middle cerebellar peduncle**, and the **inferior cerebellar
peduncle** — are the **white-matter tracts** that **connect**
the cerebellum to the brainstem. In the tree, the **cerebellar
peduncles** are **children of the pons**
(``.../metencephalon/pons/cerebellar_peduncles/``), **not**
children of the cerebellum. The **cerebellar vermis** (here) is
the **midline cortical division**. **The peduncles are the
CONDUCTION INFRASTRUCTURE; the vermis is the MIDLINE CORTICAL
DIVISION.** Consumers must **not** conflate the cerebellar
vermis with the cerebellar peduncles.
**Boundary status (VERMAL — NOT the cerebral hemispheres):**
**Boundary case — the cerebellar vermis is CEREBELLAR, NOT the
cerebral hemispheres.** The **cerebral hemispheres**
(``.../forebrain/telencephalon/cerebral_hemispheres/``) are the
**forebrain** structures — the **cortex**, the **white
matter**, the **basal ganglia**, the **hippocampus**, the
**amygdala**, the **lateral ventricles**. The **cerebellar
vermis** (here) is the **hindbrain** structure — the **midline
cerebellar division**. **They are DIFFERENT structures in
DIFFERENT brain vesicles** — the **cerebral hemispheres** are
**forebrain**; the **cerebellar vermis** is **hindbrain**.
Consumers must **not** conflate the cerebellar vermis with the
cerebral hemispheres.
**Boundary status (VERMAL — NOT the metencephalon, hindbrain,
or brainstem):** **Boundary case — the cerebellar vermis is a
CHILD of the cerebellum (a grandchild of the metencephalon, a
great-grandchild of the hindbrain), NOT the metencephalon,
hindbrain, or brainstem.** The **metencephalon**
(``.../metencephalon/``) is the **container** (pons +
cerebellum + fourth ventricle); the **hindbrain**
(``.../hindbrain/``) is the **whole** rhombencephalon
derivative; the **brainstem** is the **segmental neuraxis**
(midbrain + pons + medulla). The **cerebellar vermis** (here)
is a **child of the cerebellum** — **four levels deep** from
the brainparts root. Consumers must **not** conflate the
cerebellar vermis with the metencephalon, the hindbrain, or the
brainstem.
**Boundary status (VERMAL — NOT the cerebellum container):**
**Boundary case — the cerebellar vermis is a CHILD of the
cerebellum, NOT the cerebellum container.** The **cerebellum**
(``.../cerebellum/``) is the **container** — the
**suprasegmental structure**; the **cerebellar vermis** (here)
is a **child sub-container** of the cerebellum. Consumers must
**not** conflate the cerebellar vermis with the cerebellum
container.
**Boundary status (HETEROGENEOUS — MULTIPLE lobes with
DIFFERENT functions):** **Boundary case — the cerebellar vermis
is a HETEROGENEOUS midline division with MULTIPLE lobes and
MULTIPLE functions, not a single uniform system.** The
cerebellar vermis includes:
*   **Vermal anterior lobe** (lobules I–V) — the
    **spinocerebellum midline** — **posture, gait, truncal
    motor control** (projecting to the **fastigial nucleus**).
*   **Vermal posterior lobe** (lobules VI–IX) — the
    **spinocerebellum midline** / **cerebrocerebellum midline
    transition** — **gait, axial motor**, and the **limbic
    cerebellum** component (the **vermal posterior lobe** is
    involved in **affective regulation** — a **contributing
    substrate** of the **cerebellar cognitive-affective
    syndrome — CCAS**, via the **fastigial → thalamus VL →
    prefrontal cortex** pathway).
*   **Vermal flocculonodular lobe** (lobule X — the
    **nodulus** — the **midline** component — **shared** with
    the **flocculonodular lobes** of the **left** and
    **right** cerebellar hemispheres) — the
    **vestibulocerebellum midline** — **vestibular control,
    balance, eye movements** (projecting to the **fastigial
    nucleus** and the **vestibular nuclei**).
**Each lobe is functionally distinct** — the tree wires the
**anterior_lobe**, **flocculonodular_lobe**, and
**posterior_lobe** as **sub-containers of the vermis**.
Consumers must **not** treat the cerebellar vermis as a single
uniform region — it is a **midline heterogeneous division**
with **three functionally distinct lobes**.
**Boundary status (NODULUS SHARED — the VERMAL NODULUS is
SHARED with the FLOCCULONODULAR LOBES of the HEMISPHERES):**
**Boundary case — the vermal nodulus is the SHARED midline
component of the flocculonodular lobe — SHARED between the
vermis and the flocculonodular lobes of the left and right
cerebellar hemispheres.** The **vermal flocculonodular lobe**
(lobule X) — specifically the **nodulus** — is the **midline**
component. The **left flocculonodular lobe** (the left
flocculus + the nodulus) and the **right flocculonodular
lobe** (the right flocculus + the nodulus) both **share** the
**same nodulus** — the **nodulus** belongs to the **vermis**
(the **midline division**). **The nodulus is NOT a paired
structure — it is the SHARED midline component.** Consumers
must **not** treat the vermal nodulus as a purely **vermal**
structure — the **nodulus** is the **midline (vermal)
component** that is **shared** with the left and right
flocculonodular lobes. See the **flocculonodular lobe
modules** (``.../hemispheres/left/flocculonodular_lobe/`` and
``.../hemispheres/right/flocculonodular_lobe/``) for the
mirror-contract treatment of this shared component.
**Boundary status (VERMAL — NOT a single neural processor):**
**Boundary case — the cerebellar vermis is a REGION, not a
single neural processor.** It **contains** neural processors
(the **vermal cortical microzones** of the anterior,
posterior, and flocculonodular lobes, the **Purkinje-cell
output** to the **fastigial nucleus** and the **vestibular
nuclei**) — but it is **not itself a processor**. The
**processing** happens in the **vermal cortex** and in the
**deep nuclei** (the fastigial nucleus and the vestibular
nuclei). Consumers must **not** treat the cerebellar vermis as
a **single neural processor** — it is a **midline division**
with **heterogeneous lobes**, each with its own function.
**Boundary status (SLEA-FREE — the cerebellar vermis is NOT an
extended-amygdala component):** **Boundary case — the
cerebellar vermis is SLEA-FREE.** The **SLEA overlap** belongs
to the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The **cerebellar
vermis** is a **midline cerebellar division** — it is **NOT**
an extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into
the cerebellar vermis — it is **SLEA-free**.

Overview
--------
The cerebellar vermis is the **midline cerebellar division** — the
**median region** of the cerebellum, comprising the **vermal
cerebellar cortex** (the three-layered grey-matter cortex over
lobules I–X), the **vermal folial white matter** (the
white-matter branches of the arbor vitae within the vermis), and
the **vermal lobes** (anterior, posterior, flocculonodular) —
organized along the **midline** of the cerebellum, continuous
with the **hemispheres** at the **paravermal zone** (the
**intermediate** cerebellar zone). It is a **container module**
with **three structural sub-containers** (``anterior_lobe/``,
``flocculonodular_lobe/``, and ``posterior_lobe/``).

**The cerebellar vermis is the MIDLINE division, distinct from
the cerebellar hemispheres (the lateral division).** The
**cerebellar hemispheres** (``.../cerebellum/hemispheres/``) are
**lateral**; the **cerebellar vermis** (here) is **midline**.
They are **continuous** at the **paravermal zone** (the
**intermediate** cerebellar zone), but they are **distinct
divisions**.

**The cerebellar vermis is the SPINOCEREBELLUM MIDLINE (anterior
lobe), the CEREBROCEREBELLUM MIDLINE TRANSITION (posterior
lobe), and the VESTIBULOCEREBELLUM MIDLINE (flocculonodular
lobe — the nodulus).** The **vermal anterior lobe** (lobules
I–V) is the **spinocerebellum midline** — **posture, gait,
truncal motor control** (projecting to the **fastigial
nucleus**). The **vermal posterior lobe** (lobules VI–IX) is
the **spinocerebellum midline** / **cerebrocerebellum midline
transition** — **gait, axial motor**, and the **limbic
cerebellum** component (involved in **affective regulation**).
The **vermal flocculonodular lobe** (lobule X — the
**nodulus**) is the **vestibulocerebellum midline** —
**vestibular control, balance, eye movements** (projecting to
the **fastigial nucleus** and the **vestibular nuclei**).

**The vermal nodulus is the SHARED midline component of the
flocculonodular lobe.** The **vermal flocculonodular lobe**
(lobule X) — specifically the **nodulus** — is the **midline**
component, and it is **shared** between the **vermis** and the
**flocculonodular lobes** of the **left** and **right**
cerebellar hemispheres (the **left flocculus + nodulus** and
the **right flocculus + nodulus**). The **nodulus** is **NOT a
paired structure** — it is the **shared midline component**.
See the **flocculonodular lobe modules** (``.../hemispheres/
left/flocculonodular_lobe/`` and ``.../hemispheres/right/
flocculonodular_lobe/``) for the mirror-contract treatment.

**The cerebellar vermis is a HETEROGENEOUS midline division, not a
single structure.** It includes the **vermal anterior lobe**
(spinocerebellum midline — posture, gait), the **vermal
posterior lobe** (spinocerebellum / cerebrocerebellum transition
— gait, axial motor, limbic cerebellum), and the **vermal
flocculonodular lobe** (vestibulocerebellum midline —
vestibular control, balance, eye movements). Each lobe is
functionally distinct.

**The cerebellar vermis is a REGION, not a single neural
processor.** The **processing** happens in the **vermal
cortex** and in the **deep nuclei** (the fastigial nucleus and
the vestibular nuclei). The **vermis** is the **midline
division** that **contains** those structures.

Vermal Composition (sub-containers and prose)
---------------------------------------------
The cerebellar vermis is a **midline cerebellar division** with
**three lobe sub-containers** — documented as **structural
children** (``anterior_lobe/``, ``flocculonodular_lobe/``, and
``posterior_lobe/``) — and **many prose-defined sub-structures**
documented within those lobe sub-containers:

*   **Vermal Anterior Lobe**
    (``.../vermis/anterior_lobe/``) — the **spinocerebellum
    midline** (lobules I–V):
    *   **Vermal lobules I–V** — the **five lobules** of the
        vermal anterior lobe (Larsell nomenclature — the
        **lingula I**, **lobulus centralis II–III**,
        **culmen IV–V**) — documented as **prose** or
        **children of the anterior_lobe**.
    *   **Vermal anterior lobe homunculus** — the **somatotopic
        map** of the vermal anterior lobe — the
        **trunk/axial** representation — documented as
        **prose**.

*   **Vermal Posterior Lobe**
    (``.../vermis/posterior_lobe/``) — the **spinocerebellum
    midline** / **cerebrocerebellum midline transition**
    (lobules VI–IX):
    *   **Vermal lobules VI–IX** — the **four lobules** of the
        vermal posterior lobe (Larsell nomenclature —
        **declive VI**, **folium VII**, **tuber VIII**,
        **pyramis VIII**, **uvula IX**) — documented as
        **prose** or **children of the posterior_lobe**.
    *   **Limbic cerebellum** — the **vermal posterior lobe**
        (especially the **pyramis** and **uvula**) is the
        **limbic cerebellum** — involved in **affective
        regulation** — a **contributing substrate** of the
        **cerebellar cognitive-affective syndrome (CCAS)**
        via the **fastigial → thalamus VL → prefrontal
        cortex** pathway — documented as **prose**.

*   **Vermal Flocculonodular Lobe**
    (``.../vermis/flocculonodular_lobe/``) — the
    **vestibulocerebellum midline** (lobule X — the
    **nodulus**):
    *   **Nodulus** (lobule X) — the **midline** component of
        the flocculonodular lobe — **shared** with the
        **flocculonodular lobes** of the **left** and
        **right** cerebellar hemispheres (the **left
        flocculus + nodulus** and the **right flocculus +
        nodulus**) — documented as **prose**.

**These sub-structures are children of the lobe sub-containers
(or prose), not direct structural children of the cerebellar
vermis.** The tree wires the **cerebellar vermis** as a
**container** with **three lobe sub-containers**
(``anterior_lobe/``, ``flocculonodular_lobe/``, and
``posterior_lobe/``) — the **vermal lobules** (I–X), the
**vermal cortex**, the **vermal folial white matter**, the
**fissures**, the **vermal zones**, and the **vermal
microzones** are documented as **prose** or as **children of
the lobe sub-containers**. Consumers that need **lobule-level**
resolution should consult the **lobe sub-container modules**
and the references, not the cerebellar vermis container.

The Cerebellar Vermis / Cerebellar Hemispheres Boundary
-------------------------------------------------------
This is the **midline-vs-lateral** boundary:

*   **Cerebellar vermis** (this module) — the **midline**
    cerebellar division.

*   **Cerebellar hemispheres**
    (``.../cerebellum/hemispheres/``) — the **lateral**
    cerebellar division (left + right).

**They are DIFFERENT cerebellar divisions** — the
**hemispheres** are **lateral**; the **vermis** is **midline**.
They are **continuous** at the **paravermal zone** (the
**intermediate** cerebellar zone), but they are **distinct
divisions**. Consumers must **not** conflate the cerebellar
vermis with the cerebellar hemispheres.

The Cerebellar Vermis / Cerebellar Deep Nuclei Boundary
-------------------------------------------------------
This is the **cortical-division-vs-grey-matter-output-nuclei**
boundary:

*   **Cerebellar vermis** (this module) — the **midline
    cortical division**.

*   **Cerebellar deep nuclei** (``.../cerebellum/nuclei/``) —
    the **grey-matter output nuclei** (dentate, fastigial,
    interposed).

**The vermis is the MIDLINE CORTICAL DIVISION; the deep nuclei are
the GREY-MATTER OUTPUT NUCLEI.** The **vermal anterior lobe** and
the **vermal nodulus** project to the **fastigial nucleus** —
those are **connections**, not identities. Consumers must **not**
conflate the cerebellar vermis with the cerebellar deep nuclei.

The Cerebellar Vermis / Cerebellar Cortex Boundary
--------------------------------------------------
This is the **whole-vs-layer** boundary:

*   **Cerebellar vermis** (this module) — the **midline
    cortical division** (cortex + folial white matter + lobes).

*   **Cerebellar cortex** — the **three-layered grey-matter
    layer** (molecular, Purkinje, granular — prose).

**The cortex is a LAYER within the vermis; the vermis is the WHOLE
midline division.** Consumers must **not** conflate the
cerebellar vermis with the cerebellar cortex.

The Cerebellar Vermis / Deep White Matter Boundary
--------------------------------------------------
This is the **cortical-division-vs-white-matter-core** boundary:

*   **Cerebellar vermis** (this module) — the **midline
    cortical division** (with the **vermal folial white
    matter** as a component).

*   **Cerebellar deep white matter**
    (``.../cerebellum/deep_white_matter/``) — the
    **white-matter core** (arbor vitae and intracerebellar
    tracts).

**The vermis is the MIDLINE CORTICAL DIVISION; the deep white
matter is the WHITE-MATTER CORE that spans all the divisions.**
Consumers must **not** conflate the cerebellar vermis with the
deep white matter.

The Cerebellar Vermis / Fastigial Nucleus Boundary
--------------------------------------------------
This is the **cortical-division-vs-medial-output-nucleus**
boundary:

*   **Cerebellar vermis** (this module) — the **midline
    cortical division**.

*   **Fastigial nucleus**
    (``.../cerebellum/nuclei/fastigial_nucleus/``) — the
    **medial output nucleus** of the cerebellum.

**The vermis is the MIDLINE CORTICAL DIVISION; the fastigial
nucleus is the MEDIAL OUTPUT NUCLEUS.** The **vermal anterior
lobe** and the **vermal nodulus** project to the **fastigial
nucleus** — that is a **connection**, not an identity.
Consumers must **not** conflate the cerebellar vermis with the
fastigial nucleus.

The Cerebellar Vermis / Vestibular Nuclei Boundary
--------------------------------------------------
This is the **cerebellar-division-vs-brainstem-vestibular-nuclei**
boundary:

*   **Cerebellar vermis** (this module) — the **midline
    cortical division**.

*   **Vestibular nuclei** (medial, superior, lateral,
    inferior — in the pons and medulla) — the **brainstem
    vestibular nuclei** — the **primary output target** of
    the **flocculonodular lobe**.

**The vermis is the MIDLINE CORTICAL DIVISION; the vestibular
nuclei are the BRAINSTEM GREY-MATTER NUCLEI.** The **vermal
nodulus** projects to the **vestibular nuclei** — that is a
**connection**, not an identity. Consumers must **not** conflate
the cerebellar vermis with the vestibular nuclei.

The Cerebellar Vermis / Brainstem Boundary
------------------------------------------
This is the **suprasegmental-vs-segmental** boundary:

*   **Cerebellar vermis** (this module) — the
    **suprasegmental** midline cerebellar division.

*   **Brainstem** (midbrain + pons + medulla oblongata) — the
    **segmental neuraxis**.

**The vermis is SUPRASEGMENTAL, not brainstem.** It is **part of
the cerebellum**, which is **attached to the brainstem** via the
**cerebellar peduncles**, but which is **NOT part of the
brainstem** proper. Consumers must **not** conflate the
cerebellar vermis with the brainstem.

The Cerebellar Vermis / Fourth Ventricle Boundary
-------------------------------------------------
This is the **cortical-division-vs-CSF-cavity** boundary:

*   **Cerebellar vermis** (this module) — the **midline
    cortical division**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The fourth ventricle is a CSF CAVITY; the vermis is the MIDLINE
CORTICAL DIVISION.** The **vermis forms part of the roof** of the
fourth ventricle (via the **superior medullary velum** and the
**inferior medullary velum**) but is **NOT** the fourth
ventricle. Consumers must **not** conflate the cerebellar vermis
with the fourth ventricle.

The Cerebellar Vermis / Cerebellar Peduncles Boundary
-----------------------------------------------------
This is the **cortical-division-vs-white-matter-tract** boundary:

*   **Cerebellar vermis** (this module) — the **midline
    cortical division**.

*   **Cerebellar peduncles** (superior, middle, inferior —
    ``.../metencephalon/pons/cerebellar_peduncles/``) — the
    **white-matter tracts** connecting the cerebellum to the
    brainstem (children of the **pons**).

**The peduncles are the CONDUCTION INFRASTRUCTURE; the vermis is
the MIDLINE CORTICAL DIVISION.** Consumers must **not** conflate
the cerebellar vermis with the cerebellar peduncles.

The Cerebellar Vermis / Cerebral Hemispheres Boundary
-----------------------------------------------------
This is the **hindbrain-vs-forebrain** boundary:

*   **Cerebellar vermis** (this module) — the **hindbrain**
    structure.

*   **Cerebral hemispheres**
    (``.../forebrain/telencephalon/cerebral_hemispheres/``) —
    the **forebrain** structures (cortex, white matter, basal
    ganglia, hippocampus, amygdala, lateral ventricles).

**They are DIFFERENT structures in DIFFERENT brain vesicles** —
the **cerebral hemispheres** are **forebrain**; the
**cerebellar vermis** is **hindbrain**. Consumers must **not**
conflate the cerebellar vermis with the cerebral hemispheres.

The Cerebellar Vermis / Cerebellum Boundary
-------------------------------------------
This is the **child-vs-container** boundary:

*   **Cerebellar vermis** (this module) — a **child
    sub-container of the cerebellum**.

*   **Cerebellum** (``.../cerebellum/``) — the **container**.

**The cerebellar vermis is a CHILD of the cerebellum.** Consumers
must **not** conflate the cerebellar vermis with the cerebellum
container.

The Cerebellar Vermis / Metencephalon, Hindbrain, and Brainstem Boundary
-----------------------------------------------------------------------
This is the **deep-descendant-vs-container** boundary:

*   **Cerebellar vermis** (this module) — a **child of the
    cerebellum** (a **grandchild of the metencephalon**, a
    **great-grandchild of the hindbrain**).

*   **Metencephalon** (``.../metencephalon/``), **hindbrain**
    (``.../hindbrain/``), and **brainstem** (midbrain + pons
    + medulla oblongata) — the **containers and the segmental
    neuraxis**.

**The cerebellar vermis is a CHILD of the cerebellum** — **four
levels deep** from the brainparts root. Consumers must **not**
conflate the cerebellar vermis with the metencephalon, the
hindbrain, or the brainstem.

The Cerebellar Vermis / SLEA Boundary
-------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cerebellar vermis** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**,
    **ventral pallidum**, and **nucleus accumbens** (wired
    elsewhere).

**The cerebellar vermis is NOT part of the SLEA continuum.** It is
a **midline cerebellar division**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into
the cerebellar vermis.

Function in the Human Brain
---------------------------
The cerebellar vermis's functions are **heterogeneous** —
documented at the **lobe** level, not at the division level:

*   **Axial Motor Control and Gait (Vermal Anterior Lobe):** The
    **vermal anterior lobe** (lobules I–V) — the
    **spinocerebellum midline** — is the **neural substrate**
    of **axial motor control** and **gait** — the **truncal
    motor control** and the **gait** (the **trunk** and the
    **proximal limbs**). The **vermal anterior lobe** projects
    to the **fastigial nucleus** (the **medial output
    nucleus**), which **projects bilaterally** to the
    **vestibular nuclei** and the **reticular formation** —
    the **reticulospinal** and **vestibulospinal** tracts —
    to **modulate** the **axial motor** and **postural** tone.
    The **vermal anterior lobe** is the **substrate** of
    **gait ataxia** (the **classic vermal syndrome**).

*   **Axial Motor and Limbic Cerebellum (Vermal Posterior
    Lobe):** The **vermal posterior lobe** (lobules VI–IX) —
    the **spinocerebellum midline** / **cerebrocerebellum
    midline transition** — is the **neural substrate** of
    **axial motor** (the **gait** and the **trunk**) and the
    **limbic cerebellum** (the **pyramis** and **uvula** —
    the **vermal posterior lobe** is involved in **affective
    regulation** — a **contributing substrate** of the
    **cerebellar cognitive-affective syndrome — CCAS** via
    the **fastigial → thalamus VL → prefrontal cortex**
    pathway). The **vermal posterior lobe** is a **substrate**
    of **gait ataxia** and the **affective dysregulation**
    component of **CCAS**.

*   **Vestibular Control, Balance, and Eye Movements (Vermal
    Flocculonodular Lobe — the Nodulus):** The **vermal
    flocculonodular lobe** (lobule X — the **nodulus**) — the
    **vestibulocerebellum midline** — is the **neural
    substrate** of **vestibular control**, **balance**, and
    **eye movements** (the **vestibulo-ocular reflex
    velocity storage**, the **optokinetic response**, the
    **tilt-translation discrimination**, the **spatial
    orientation**). The **nodulus** projects to the
    **vestibular nuclei** (the **medial** and **inferior
    vestibular nuclei**) and the **fastigial nucleus** —
    the **nodulus** is the **midline** component of the
    **vestibulocerebellum**.

*   **NOT the hemispheral functions.** The **cerebellar
    hemispheres** (the **lateral division**) are the
    substrate of **limb motor execution** (the anterior lobe —
    spinocerebellum lateral), **motor planning, motor
    learning, and cognition** (the posterior lobe —
    cerebrocerebellum lateral — including the **CCAS**), and
    **VOR adaptation, smooth pursuit, and gaze-holding** (the
    flocculonodular lobe — the flocculus). The **vermis** is
    the **midline** division — the **axial motor** and
    **limbic cerebellum** substrate, **NOT** the **lateral
    limb** or **cognition** substrate.

*   **NOT the deep nuclei.** The **cerebellar deep nuclei** —
    the **dentate nucleus**, the **interposed nucleus**, the
    **fastigial nucleus** — are the **grey-matter output
    nuclei**. The **vermis** is the **midline cortical
    division** that **projects to** the **fastigial nucleus**
    (and, for the nodulus, to the **vestibular nuclei**) —
    those are **connections**, not identities.

*   **NOT a single neural processor.** The cerebellar vermis is
    a **midline heterogeneous division** — the **processing**
    happens in the **vermal cortex** and in the **deep nuclei**
    (the fastigial nucleus and the vestibular nuclei).
    Consumers must **not** treat the cerebellar vermis as a
    **single processor** — it is a **division** with
    **heterogeneous lobes**, each with its own function.

**The unifying theme:** the cerebellar vermis is the **midline
cerebellar division** — the **vermal anterior lobe**
(spinocerebellum midline — axial motor, posture, gait), the
**vermal posterior lobe** (spinocerebellum / cerebrocerebellum
transition — axial motor, limbic cerebellum — the **CCAS**
affective component), and the **vermal flocculonodular lobe**
(vestibulocerebellum midline — the **nodulus** — vestibular
control, balance, eye movements) — that **projects** to the
**fastigial nucleus** (the **medial output nucleus**) and the
**vestibular nuclei**. It is a **heterogeneous midline
division**, **NOT a single neural processor**, and **NOT the
cerebellar hemispheres, the cerebellar deep nuclei, the
fastigial nucleus, the vestibular nuclei, the brainstem, the
fourth ventricle, or the cerebral hemispheres**.

Associated Disorders
--------------------
The cerebellar vermis has **named clinical syndromes** — its
clinical associations are **cerebellar** (via the **vermal
lobes** and the **fastigial nucleus**):

*   **Vermal Syndrome (Vermal Ataxia):** **Vermal lesions** —
    from **cerebellar stroke** (PICA, AICA, SCA territories),
    **cerebellar hemorrhage**, **cerebellar tumors**
    (medulloblastoma — typically arising in the **vermis**;
    ependymoma — arising from the **fourth ventricle** floor
    adjacent to the **vermis**), **alcohol-related cerebellar
    degeneration** (the **anterior vermis** is
    **preferentially affected**), **paraneoplastic cerebellar
    degeneration**, and **multiple sclerosis** — cause
    **truncal ataxia**, **gait ataxia**, and **postural
    instability** (the **classic vermal syndrome** — the
    **axial** ataxia with **relatively preserved limb
    coordination**). The **vermis** is the **substrate**.

*   **Alcohol-Related Cerebellar Degeneration (Vermal Anterior
    Lobe + Anterior Vermis):** **Chronic alcohol use** causes
    **anterior vermis** degeneration — **gait ataxia**
    (truncal ataxia) with **relatively preserved limb
    coordination**. The **vermal anterior lobe** (and the
    **anterior vermis**) is the **substrate** — the
    **Purkinje cells** in the **vermal anterior lobe** are
    the **primary target**.

*   **Medulloblastoma (Vermal):** **Medulloblastoma** — the
    most common **malignant pediatric brain tumor** — typically
    **arises** in the **cerebellar vermis** (the **midline**
    cerebellum). The **vermis** is the **substrate**.

*   **Ependymoma (Fourth Ventricle Floor, Adjacent to the
    Vermis):** **Ependymoma** — a **pediatric posterior fossa
    tumor** — arises from the **ependyma** of the **fourth
    ventricle floor** (adjacent to the **vermis**). The
    **vermis** is **adjacent** to the **substrate**.

*   **Cerebellar Cognitive-Affective Syndrome (CCAS — Vermal
    Posterior Lobe Contribution):** The **vermal posterior
    lobe** — the **limbic cerebellum** (the **pyramis** and
    **uvula**) — is a **contributing substrate** of the
    **affective** and **executive** components of **CCAS**
    (via the **vermis → fastigial nucleus → thalamus VL →
    prefrontal cortex** pathway). The **principal** CCAS
    substrate is the **dentate nucleus** (the **neodentate**).

*   **Vermal Stroke (PICA, AICA, SCA territories):** **Cerebellar
    stroke** — **PICA**, **AICA**, and **SCA** infarcts — can
    involve the **vermis** (the **superior vermis** via the
    **SCA**; the **inferior vermis** via the **PICA**) — the
    **vermis** is a **substrate** for the **cerebellar
    stroke** syndrome.

*   **Paraneoplastic Cerebellar Degeneration (Vermal):** Some
    **paraneoplastic cerebellar degeneration** forms
    **preferentially affect** the **vermis** (the **Purkinje
    cells** in the **vermis** are the **primary target**) —
    the **vermis** is a **potential substrate**.

*   **Chiari Malformation (Vermal Compression):** **Chiari
    malformation** — the **tonsillar herniation** through
    the **foramen magnum** — can **compress** the **vermis**
    (as well as the **cerebellar tonsil** and the
    **brainstem**), contributing to the **cerebellar** and
    **bulbar** symptoms of **Chiari**.

*   **No Named "Vermal Syndrome" (singular):** The cerebellar
    vermis has **multiple named clinical syndromes** (vermal
    syndrome, alcohol-related cerebellar degeneration,
    medulloblastoma, ependymoma, CCAS contribution, vermal
    stroke, paraneoplastic cerebellar degeneration, Chiari
    malformation) — but **no single "vermal syndrome."** Its
    clinical relevance is **cerebellar** — via the **vermal
    lobes** and the **fastigial nucleus**.

**What is NOT here:** The cerebellar vermis is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (central nucleus + basolateral nuclei),
**Urbach-Wiethe disease** (amygdala), or **Parkinson's disease**
(substantia nigra, in the midbrain). Its clinical relevance is
**cerebellar** — **vermal syndrome**, **alcohol-related
cerebellar degeneration**, **medulloblastoma**, **ependymoma**,
**CCAS contribution**, **vermal stroke**, **paraneoplastic
cerebellar degeneration**, and **Chiari malformation**.

Lateralization Notes
--------------------
This is the **cerebellar vermis** container module. The
cerebellar vermis is a **midline cerebellar division** — the
**median** region of the cerebellum, **not a paired structure**
in the way the **lateral ventricles** or the **amygdala** are —
it is a **midline division** with **shared** projections (the
**vermal anterior lobe** and the **vermal nodulus** project to
the **fastigial nucleus** — a **paired** nucleus, but the vermal
projection is **midline** and **bilateral**).

*   **Midline Division (Not a Pair):** The **cerebellar
    vermis** is the **midline** cerebellar division — the
    **median** region **between** the **left** and **right**
    cerebellar hemispheres. The **vermis** is **not a paired
    structure** — it is a **midline** division, **continuous**
    with the **hemispheres** at the **paravermal zone** (the
    **intermediate** cerebellar zone).

*   **The Vermal Nodulus is SHARED (Not a Pair):** The **vermal
    flocculonodular lobe** (lobule X — the **nodulus**) is the
    **midline** component, and it is **shared** between the
    **vermis** and the **flocculonodular lobes** of the **left**
    and **right** cerebellar hemispheres (the **left flocculus
    + nodulus** and the **right flocculus + nodulus**). The
    **nodulus** is **NOT a paired structure** — it is the
    **shared midline component**. See the **flocculonodular
    lobe modules** (``.../hemispheres/left/flocculonodular_
    lobe/`` and ``.../hemispheres/right/flocculonodular_
    lobe/``) for the mirror-contract treatment of this shared
    component.

*   **NO Extended-Amygdala Warning (SLEA-free):** The
    cerebellar vermis is **NOT** an extended-amygdala
    component. It carries **no SLEA warning**. Consumers must
    **not** import the SLEA warning into the cerebellar vermis.

*   **NO Amygdala-Lateralization Warning:** The cerebellar
    vermis is **NOT** the fear-output or the fear-learning
    structure. It is a **midline cerebellar division** —
    consumers must **not** conflate it with the **amygdala**
    or the **fear circuit**.

**A consumer that assumes "left vermis = right vermis" should be
reminded that the vermis is a MIDLINE division, not a paired
structure** — there is **one vermis**, spanning the **midline**
of the cerebellum, **continuous** with the left and right
hemispheres at the **paravermal zone**. The **vermal nodulus**
is the **shared midline component** of the flocculonodular lobe
(shared with the left and right flocculonodular lobes). The
cerebellar vermis carries **NO warning** — **no SLEA warning**,
**no amygdala-lateralization warning**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **container** does
    **not** import from ``.../cerebellum/hemispheres/left/``
    or ``.../cerebellum/hemispheres/right/`` — it is a
    **namespace container**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../cerebellum/`` (parent),
    ``.../cerebellum/deep_white_matter/`` (sibling),
    ``.../cerebellum/hemispheres/`` (sibling),
    ``.../cerebellum/nuclei/`` (sibling),
    ``.../metencephalon/`` (grandparent),
    ``.../metencephalon/pons/cerebellar_peduncles/`` (the
    peduncles are **children of the pons**, not of the
    cerebellum), ``.../metencephalon/fourth_ventricle/``,
    ``.../hindbrain/``, ``.../midbrain/``,
    ``.../forebrain/telencephalon/cerebral_hemispheres/``
    (the cerebral hemispheres), or any other container. The
    cerebellar vermis's relationships to the cerebellar
    hemispheres, the cerebellar deep nuclei, the fastigial
    nucleus, the vestibular nuclei, the cerebellar peduncles,
    the fourth ventricle, the brainstem, the cerebellum, the
    metencephalon, the hindbrain, and the cerebral hemispheres
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — three structural children.** The
    ``anterior_lobe/``, ``flocculonodular_lobe/``, and
    ``posterior_lobe/`` are **lobe sub-containers**. The
    **vermal lobules** (I–X), the **vermal cortex**, the
    **vermal folial white matter**, the **fissures**, the
    **vermal zones**, and the **vermal microzones** are
    **prose** or **children of the lobe sub-containers**.
    Consumers must not assume any exist as direct children of
    the cerebellar vermis; resolve lobule-level detail through
    the lobe sub-containers and the references.
*   **MIDLINE DIVISION — NOT the cerebellar hemispheres.** The
    **cerebellar hemispheres** are the **lateral** division;
    the **cerebellar vermis** (here) is the **midline**
    division.
*   **CORTICAL DIVISION — NOT the deep nuclei.** The
    **cerebellar deep nuclei** are the **grey-matter output
    nuclei**; the **vermis** is the **midline cortical
    division**.
*   **SPINOCEREBELLUM MIDLINE (anterior lobe), CEREBROCEREBELLUM
    MIDLINE TRANSITION (posterior lobe), VESTIBULOCEREBELLUM
    MIDLINE (flocculonodular lobe — the nodulus).**
*   **THE VERMAL NODULUS IS SHARED** — the **nodulus** is the
    **shared midline component** of the **flocculonodular
    lobe**, **shared** with the **left** and **right**
    flocculonodular lobes.
*   **VERMAL ANTERIOR LOBE PROJECTS TO THE FASTIGIAL NUCLEUS.**
    The **vermal anterior lobe** and the **vermal nodulus**
    project to the **fastigial nucleus** (the **medial output
    nucleus**) — those are **connections**, not identities.
*   **NOT the fastigial nucleus — a CONNECTION.** The **vermis**
    is the **midline cortical division**; the **fastigial
    nucleus** is the **medial output nucleus** that the
    **vermis** projects to.
*   **NOT the vestibular nuclei — a CONNECTION.** The **vermal
    nodulus** projects to the **vestibular nuclei** — that is
    a **connection**, not an identity.
*   **NOT the brainstem — SUPRASEGMENTAL.** The **vermis** is
    **part of the cerebellum**, which is **suprasegmental**.
*   **NOT the fourth ventricle — a CSF cavity.** The **vermis**
    **forms part of the roof** of the fourth ventricle (via
    the **superior medullary velum** and the **inferior
    medullary velum**), but is **NOT** the fourth ventricle.
*   **NOT the cerebellar peduncles — those are WHITE-MATTER
    TRACTS, children of the PONS.**
*   **NOT the cerebral hemispheres — a FOREBRAIN structure.**
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **NOT a single neural processor — a REGION.** The
    **processing** happens in the **vermal cortex** and in the
    **deep nuclei** (the fastigial nucleus and the vestibular
    nuclei).
*   **HETEROGENEOUS MIDLINE DIVISION — three functionally
    distinct lobes.** The **vermal anterior lobe**
    (spinocerebellum midline — axial motor, posture, gait);
    the **vermal posterior lobe** (spinocerebellum /
    cerebrocerebellum transition — axial motor, limbic
    cerebellum — CCAS affective component); the **vermal
    flocculonodular lobe** (vestibulocerebellum midline — the
    **nodulus** — vestibular control, balance, eye
    movements).
*   **No ``AREA_PATHS`` hop.** The cerebellar vermis is a
    **local container** under the cerebellum, not a
    **cross-listed container**.
*   **No nested cross-listing.** The cerebellar vermis has **no
    nested dual-framing module**. It is a **single container**
    with three sub-containers.
*   **No lateralization warning.** The cerebellar vermis is a
    **midline division** — it carries **no warning** — **no
    SLEA warning**, **no amygdala-lateralization warning**, and
    **no rhinencephalon-exclusion flag**. The **shared
    nodulus** (shared with the left and right flocculonodular
    lobes) is documented as **structural fact**, not as a
    **lateralization warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.cerebellum.vermis import (
        anterior_lobe, flocculonodular_lobe, posterior_lobe,
    )

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.cerebellum.vermis"
    )
    anterior_lobe_path = (
        "hindbrain.metencephalon.cerebellum.vermis.anterior_lobe"
    )
    posterior_lobe_path = (
        "hindbrain.metencephalon.cerebellum.vermis.posterior_lobe"
    )
    flocculonodular_lobe_path = (
        "hindbrain.metencephalon.cerebellum.vermis.flocculonodular_lobe"
    )

**Do not** assume the cerebellar vermis is the **cerebellar
hemispheres**. The **cerebellar hemispheres** are the **lateral**
division; the **cerebellar vermis** is the **midline**
division.

**Do not** assume the cerebellar vermis is the **cerebellar deep
nuclei** or the **fastigial nucleus**. The **cerebellar deep
nuclei** are the **grey-matter output nuclei**; the **fastigial
nucleus** is the **medial output nucleus** that the **vermal
anterior lobe** and the **vermal nodulus** project to — that is
a **connection**, not an identity.

**Do not** assume the cerebellar vermis is the **vestibular
nuclei**. The **vestibular nuclei** are the **primary output
target** of the **flocculonodular lobe** — the **vermal
nodulus** projects to them, but that is a **connection**, not
an identity.

**Do not** assume the cerebellar vermis is the **brainstem**,
the **fourth ventricle**, or the **cerebellar peduncles**. The
**vermis** is **suprasegmental** (part of the cerebellum); it
**forms part of the roof** of the fourth ventricle but is **NOT**
the fourth ventricle; the **cerebellar peduncles** are the
**white-matter tracts** (children of the **pons**).

**Do not** assume the cerebellar vermis is the **cerebellum**
container, the **metencephalon**, the **hindbrain**, or the
**cerebral hemispheres**. The **cerebellar vermis** is a **child
of the cerebellum** (a **grandchild of the metencephalon**, a
**great-grandchild of the hindbrain**).

**Do not** treat the **vermal nodulus** as a purely **vermal**
structure — the **nodulus** is the **shared midline component**
of the **flocculonodular lobe**, **shared** with the **left**
and **right** flocculonodular lobes. See the **flocculonodular
lobe modules** for the mirror-contract treatment of this
shared component.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the cerebellar vermis.
**The cerebellar vermis is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the cerebellar vermis's children (recommended
consumer pattern)::

    CEREBELLAR_VERMIS_CHILDREN = (
        "anterior_lobe", "flocculonodular_lobe", "posterior_lobe",
    )
    # The anterior_lobe, flocculonodular_lobe, and posterior_lobe
    # are lobe sub-containers.

Reaching the cerebellum (recommended consumer pattern — the
parent)::

    # The cerebellum is the CONTAINER:
    #
    #   hindbrain.metencephalon.cerebellum
    #
    # The cerebellar vermis is a CHILD sub-container of the
    # cerebellum.

Reaching the cerebellar hemispheres (recommended consumer
pattern — NOTE the midline-vs-lateral boundary)::

    # The cerebellar hemispheres are the LATERAL division:
    #
    #   hindbrain.metencephalon.cerebellum.hemispheres
    #
    # The cerebellar vermis is the MIDLINE division. They are
    # continuous at the paravermal zone.

Reaching the cerebellar deep nuclei (recommended consumer
pattern — NOTE the cortical-division-vs-grey-matter-output-
nuclei boundary)::

    # The cerebellar deep nuclei are the GREY-MATTER OUTPUT
    # NUCLEI (dentate, fastigial, interposed):
    #
    #   hindbrain.metencephalon.cerebellum.nuclei
    #
    # The vermis is the MIDLINE CORTICAL DIVISION; the deep
    # nuclei are the GREY-MATTER OUTPUT NUCLEI.

Reaching the fastigial nucleus (recommended consumer pattern —
NOTE the cortical-division-vs-medial-output-nucleus boundary)::

    # The fastigial nucleus is the MEDIAL OUTPUT NUCLEUS —
    # the output nucleus of the vermis and nodulus:
    #
    #   hindbrain.metencephalon.cerebellum.nuclei.fastigial_nucleus
    #
    # The vermal anterior lobe and the vermal nodulus PROJECT to
    # the fastigial nucleus — that is a CONNECTION, not an
    # identity.

Reaching the vestibular nuclei (recommended consumer pattern —
NOTE the cerebellar-division-vs-brainstem-vestibular-nuclei
boundary)::

    # The vestibular nuclei are the BRAINSTEM VESTIBULAR NUCLEI
    # — the PRIMARY OUTPUT TARGET of the FLOCCULONODULAR LOBE:
    #
    #   hindbrain.metencephalon.pons.<vestibular_nuclei>
    #   hindbrain.myelencephalon.medulla_oblongata.<vestibular_nuclei>
    #
    # The vermal nodulus PROJECTS to the vestibular nuclei —
    # that is a CONNECTION, not an identity.

Reaching the cerebellar cortex (recommended consumer pattern —
NOTE the whole-vs-layer boundary)::

    # The cerebellar cortex is the THREE-LAYERED GREY-MATTER
    # CORTEX (molecular, Purkinje, granular — prose):
    #
    #   (prose) hindbrain.metencephalon.cerebellum.<cortex>
    #
    # The cortex is a LAYER within the vermis; the vermis is the
    # WHOLE midline division.

Reaching the cerebellar deep white matter (recommended
consumer pattern — NOTE the cortical-division-vs-white-matter-
core boundary)::

    # The cerebellar deep white matter is the WHITE-MATTER CORE
    # (arbor vitae) that spans all the divisions:
    #
    #   hindbrain.metencephalon.cerebellum.deep_white_matter
    #
    # The vermis is the MIDLINE CORTICAL DIVISION; the deep
    # white matter is the WHITE-MATTER CORE that spans all the
    # divisions.

Reaching the brainstem (recommended consumer pattern — the
suprasegmental-vs-segmental boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons +
    # medulla):
    #
    #   midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The cerebellar vermis is SUPRASEGMENTAL — part of the
    # cerebellum, NOT part of the brainstem.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE the cortical-division-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The vermis FORMS PART OF THE ROOF of the fourth ventricle
    # (via the superior and inferior medullary vela) but is NOT
    # the fourth ventricle.

Reaching the cerebellar peduncles (recommended consumer
pattern — NOTE the cortical-division-vs-white-matter-tract
boundary)::

    # The cerebellar peduncles are the WHITE-MATTER TRACTS —
    # children of the PONS:
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles
    #
    # The peduncles are the CONDUCTION INFRASTRUCTURE; the
    # vermis is the MIDLINE CORTICAL DIVISION.

Reaching the cerebral hemispheres (recommended consumer
pattern — NOTE the hindbrain-vs-forebrain boundary)::

    # The cerebral hemispheres are the FOREBRAIN structures:
    #
    #   forebrain.telencephalon.cerebral_hemispheres
    #
    # The cerebellar vermis is a HINDBRAIN structure.

Lobule-level detail (not wired at the vermis level — consult
the lobe sub-containers and references)::

    # The cerebellar vermis's lobule-level detail is prose within
    # the lobe sub-containers:
    #   anterior_lobe -> vermal lobules I-V (lingula I,
    #                     lobulus centralis II-III, culmen IV-V)
    #                     — spinocerebellum midline (axial motor,
    #                     posture, gait)
    #   posterior_lobe -> vermal lobules VI-IX (declive VI,
    #                      folium VII, tuber VIII, pyramis VIII,
    #                      uvula IX) — spinocerebellum /
    #                      cerebrocerebellum transition — axial
    #                      motor, limbic cerebellum (CCAS
    #                      affective component)
    #   flocculonodular_lobe -> vermal lobule X (the NODULUS)
    #                            — vestibulocerebellum midline —
    #                            vestibular control, balance, eye
    #                            movements (SHARED with the left
    #                            and right flocculonodular lobes)
    #
    # Do not attempt to resolve these as sub-paths of the
    # cerebellar vermis.

Bilateral iteration (recommended consumer pattern — for the
hemisphere-associated lobules, not the vermis itself)::

    # The cerebellar vermis is a MIDLINE division (not a paired
    # structure) — the "left" and "right" hemisphere iteration
    # patterns are for the cerebellar hemispheres, NOT for the
    # vermis. The vermal nodulus (lobule X) is the SHARED
    # midline component of the flocculonodular lobe; the left
    # and right flocculonodular lobes share the nodulus:
    for side in ("left", "right"):
        # e.g., the left and right flocculonodular lobes share
        # the vermal nodulus
        flocculonodular_lobe_path = (
            f"hindbrain.metencephalon.cerebellum.hemispheres."
            f"{side}.flocculonodular_lobe"
        )
        # resolve flocculonodular_lobe_path through the
        # memory/recall layer

References
----------
*   **Canonical cerebellar vermis anatomy:** Standring, S.
    (ed.) (2020). *Gray's Anatomy: The Anatomical Basis of
    Clinical Practice*, 42nd ed. (Cerebellum — vermis, vermal
    lobules I–X, primary fissure, posterolateral fissure.)
*   **Cerebellar lobule nomenclature (Larsell):** Larsell, O.
    (1970). *The Comparative Anatomy and Histology of the
    Cerebellum from Monotremes through Apes*. (Vermal
    lobules I–X — lingula I, lobulus centralis II–III,
    culmen IV–V, declive VI, folium VII, tuber VIII,
    pyramis VIII, uvula IX, nodulus X.)
*   **Cerebellum overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Cerebellum — vermis, hemispheres, spinocerebellum,
    cerebrocerebellum, vestibulocerebellum.)
*   **Vermal anterior lobe and gait:** Manto, M., et al.
    (2012). "Consensus paper: roles of the cerebellum in
    motor control — the diversity of cerebellar involvement
    in movement." *The Cerebellum* 11:457–487. (Vermis —
    axial motor, posture, gait; vermal anterior lobe.)
*   **Vermal posterior lobe and limbic cerebellum:**
    Schmahmann, J.D., Sherman, J.C. (1998). "The cerebellar
    cognitive affective syndrome." *Brain* 121:561–579.
    (CCAS — the limbic cerebellum — the vermal posterior
    lobe — affective dysregulation component.)
*   **Vermal nodulus and vestibulocerebellum:** Waespe, W.,
    Cohen, B., Raphan, T. (1985). "Dynamic modification of
    the vestibulo-ocular reflex by the nodulus and uvula."
    *Science* 228:199–202. (Nodulus — velocity storage;
    vestibulocerebellum midline.)
*   **Nodulus and optokinetic response:** Precht, W., et al.
    (1976). "Functional organization of the vestibular
    input to the flocculus." *Experimental Brain Research*
    26:291–312. (Nodulus — optokinetic response.)
*   **Nodulus and tilt-translation discrimination:** Angelaki,
    D.E., Hess, B.J.M. (1995). "Inertial representation of
    angular motion in the vestibular system of rhesus
    monkeys." *Journal of Neurophysiology* 73:235–249.
    (Nodulus — tilt-translation discrimination.)
*   **Fastigial nucleus (vermal output target):** Batton,
    R.R., et al. (1977). "The fastigial nucleus: its
    connections and function." *Neurosurgery* 1:253–261.
    (Fastigial nucleus — the medial output nucleus that the
    vermal anterior lobe and the vermal nodulus project to.)
*   **Alcohol-related cerebellar degeneration (anterior
    vermis):** Victor, M., Adams, R.D., Mancall, E.L.
    (1959). "A restricted form of cerebellar cortical
    degeneration occurring in alcoholic patients." *A.M.A.
    Archives of Neurology* 1:579–688. (Anterior vermis
    degeneration — alcohol-related cerebellar ataxia.)
*   **Medulloblastoma (vermis):** Louis, D.N., et al.
    (2016). "The 2016 World Health Organization
    Classification of Tumors of the Central Nervous
    System: a summary." *Acta Neuropathologica*
    131:803–820. (Medulloblastoma — pediatric cerebellar
    tumor; typically arises in the vermis.)
*   **Ependymoma (fourth ventricle floor):** Louis, D.N., et
    al. (2016). "The 2016 World Health Organization
    Classification of Tumors of the Central Nervous
    System: a summary." *Acta Neuropathologica*
    131:803–820. (Ependymoma — pediatric posterior fossa
    tumor; arises from the fourth ventricle floor adjacent
    to the vermis.)
*   **Chiari malformation (vermal compression):** Chiari, H.
    (1891). "Über Veränderungen des Kleinhirns infolge
    von Hydrocephalie des Grosshirns." *Deutsche
    Medizinische Wochenschrift* 17:1172–1175. (Chiari
    malformation — tonsillar herniation through the foramen
    magnum; vermal compression.)
*   **Spinocerebellar ataxias (SCAs):** Paulson, H.L. (2009).
    "The spinocerebellar ataxias." In *Neurogenetics*
    (Vance, J.M., ed.). (SCAs — autosomal dominant
    cerebellar ataxias; vermal involvement in some forms.)
*   **Cerebellar stroke (PICA, AICA, SCA):** Savoiardo, M.,
    et al. (1987). "Cerebellar infarcts: clinical and CT
    findings." *Journal of Neurology* 234:256–262.
    (Cerebellar stroke — PICA, AICA, SCA territories; vermal
    involvement.)
*   **SLEA (contrast — the cerebellar vermis is NOT
    included):** Alheid, G.F., Heimer, L. (1988). "New
    perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central
    nucleus, ventral pallidum, nucleus accumbens; NOT the
    cerebellar vermis.)
*   NeuroNames — Vermis; FMA — Vermis.
"""