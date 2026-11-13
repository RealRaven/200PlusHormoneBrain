"""
infrastructure.brainparts.hindbrain.metencephalon.cerebellum
============================================================

Anatomical Hierarchy
--------------------
::

    metencephalon
    ├── cerebellum                             <-- THIS MODULE
    │   ├── deep_white_matter
    │   ├── hemispheres
    │   │   ├── left
    │   │   └── right
    │   ├── nuclei
    │   │   ├── dentate_nucleus
    │   │   ├── fastigial_nucleus
    │   │   └── interposed_nucleus
    │   └── vermis
    ├── fourth_ventricle
    └── pons

**Primary synonym:** Cerebellum; the "little brain"; the
cerebellar structure; the metencephalic suprasegmental
structure.
**Cytoarchitectonic designation:** **Not a Brodmann area. Not a
single grey-matter or white-matter structure.** A
**suprasegmental neural region** — the **cerebellar cortex**
(three-layered, Purkinje-cell-based), the **cerebellar deep
nuclei** (grey matter), and the **cerebellar white matter**
(the **arbor vitae**) — organized into **hemispheres**,
**vermis**, and **three lobes** (anterior, posterior,
flocculonodular), and connected to the brainstem via the
**cerebellar peduncles**.
**Part of:** The **metencephalon** container — the **rostral**
hindbrain sub-container (pons + cerebellum + fourth ventricle).
The **metencephalon** is the **rostral** of the **two
rhombencephalic sub-vesicles**; the **hindbrain** is the
**caudal** of the **three primary brain vesicles**.
**Structural parent:** ``.../metencephalon/`` → **direct child**
of the metencephalon container.
**Structural children:** **Four** — ``deep_white_matter/``,
``hemispheres/``, ``nuclei/``, and ``vermis/``. The
**cerebellar cortex** (the three-layered cortex), the
**cerebellar peduncles** (superior, middle, inferior — white
matter tracts connecting the cerebellum to the brainstem), the
**fissures** (primary fissure, posterolateral fissure),
**lobules** (simplex, ansiform, paramedian, etc.), and the
**cerebellar glomeruli / granular layer / molecular layer /
Purkinje cell layer** are documented as **prose** or as
**children of the sub-containers** (e.g., the cerebellar
peduncles are **children of the pons**, not of the cerebellum
directly — the pons owns the peduncle attachment).
**Boundary status (NOT the metencephalon — the cerebellum is a
CHILD):** **Boundary case — the cerebellum is NOT the
metencephalon.** The **metencephalon**
(``.../metencephalon/``) is the **container** — the **rostral**
hindbrain sub-container, comprising the **cerebellum**, the
**pons**, and the **fourth ventricle**. The **cerebellum**
(here) is a **child sub-container** of the metencephalon. **The
cerebellum is a PART of the metencephalon; the metencephalon is
the WHOLE.** Consumers must **not** conflate the cerebellum with
the metencephalon container.
**Boundary status (NOT the pons — the pons is the SIBLING):**
**Boundary case — the cerebellum is NOT the pons.** The **pons**
(``.../metencephalon/pons/``) is the **metencephalic brainstem
sub-container** — the **basis pontis**, the **tegmentum**, the
**cerebellar peduncles**, and the **cranial nerve nuclei
(V–VIII)**. The **cerebellum** (here) is the **metencephalic
suprasegmental sub-container** — the **hemispheres**, the
**vermis**, the **deep nuclei**, and the **deep white matter**.
**They are DIFFERENT metencephalic sub-structures** — the
**pons** is the **brainstem**; the **cerebellum** is the
**suprasegmental** structure **dorsal** to the pons. They are
connected via the **cerebellar peduncles**, but they are
**distinct sub-structures**. Consumers must **not** conflate
the cerebellum with the pons.
**Boundary status (NOT the fourth ventricle — the fourth
ventricle is the SIBLING):** **Boundary case — the cerebellum
is NOT the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the
**metencephalic CSF cavity** between the pons/medulla and the
cerebellum. The **cerebellum** (here) is the
**metencephalic suprasegmental structure**. **The fourth
ventricle is the CAVITY; the cerebellum is the TISSUE DORSAL
to it.** The cerebellum **forms the roof** of the fourth
ventricle (the **tectum** of the fourth ventricle) via the
**superior medullary velum** and the **inferior medullary
velum** (the **lateral apertures** are near the cerebellar
peduncles). Consumers must **not** conflate the cerebellum with
the fourth ventricle.
**Boundary status (NOT the brainstem — the cerebellum is
SUPRASEGMENTAL, not brainstem):** **Boundary case — the
cerebellum is NOT the brainstem.** The **brainstem** is the
**midbrain + pons + medulla oblongata** — the **segmental**
neuraxis that **contains the cranial nerve nuclei** and the
**long ascending/descending tracts**. The **cerebellum**
(here) is a **suprasegmental** structure — it is **attached to
the brainstem** via the **cerebellar peduncles**, but it is
**NOT part of the brainstem** proper. **The cerebellum is a
separate suprasegmental structure; the brainstem is the
segmental neuraxis.** Consumers must **not** conflate the
cerebellum with the brainstem — the **cerebellum** is
**suprasegmental**; the **brainstem** is **segmental**.
**Boundary status (NOT the cerebrum — the cerebellum is the
"LITTLE brain," not the "brain"):** **Boundary case — the
cerebellum is NOT the cerebrum.** The **cerebrum** (the
**cerebral hemispheres** — ``.../forebrain/telencephalon/
cerebral_hemispheres/``) is the **forebrain** structure — the
**cortex**, the **white matter**, the **basal ganglia**, the
**hippocampus**, the **amygdala**. The **cerebellum** (here)
is the **hindbrain** structure — the **"little brain"** — the
**metencephalic suprasegmental structure**. **They are
DIFFERENT structures in DIFFERENT brain vesicles** — the
**cerebrum** is **forebrain**; the **cerebellum** is
**hindbrain**. The Latin **cerebellum** ("little brain") is
**not** the **cerebrum** ("brain"). Consumers must **not**
conflate the cerebellum with the cerebrum — the **cerebellum**
is the **"little brain"**; the **cerebrum** is the **"brain."**
**Boundary status (NOT the hindbrain container — the cerebellum
is a GRANDCHILD):** **Boundary case — the cerebellum is NOT
the hindbrain.** The **hindbrain** (``.../hindbrain/``) is the
**whole** rhombencephalon derivative (metencephalon +
myelencephalon). The **cerebellum** (here) is a **child of the
metencephalon** — a **grandchild of the hindbrain**. **The
cerebellum is a PART of the hindbrain (via the metencephalon);
the hindbrain is the WHOLE.** Consumers must **not** conflate
the cerebellum with the hindbrain container.
**Boundary status (NOT the myelencephalon — the myelencephalon
is the CAUDAL SIBLING of the metencephalon):** **Boundary
case — the cerebellum is NOT the myelencephalon.** The
**myelencephalon** (``.../hindbrain/myelencephalon/``) is the
**caudal** hindbrain sub-container — the **medulla oblongata**.
The **cerebellum** (here) is a **child of the metencephalon**
— a **part of the rostral** hindbrain sub-container. **They
are DIFFERENT hindbrain sub-compartments** — the **cerebellum**
is **rostral** (via the metencephalon); the **myelencephalon**
is **caudal**. Consumers must **not** conflate the cerebellum
with the myelencephalon.
**Boundary status (NOT the midbrain — the midbrain is ROSTRAL
to the metencephalon):** **Boundary case — the cerebellum is
NOT the midbrain.** The **midbrain** (``.../midbrain/``) is
the **mesencephalon** derivative — the **tectum**, the
**tegmentum**, the **cerebral peduncle**, the **mesencephalic
aqueduct**. The **cerebellum** (here) is the **metencephalic
suprasegmental structure**. **They are DIFFERENT developmental
compartments** — the **midbrain** is **rostral**; the
**cerebellum** is **caudal** (in the metencephalon). They are
connected via the **superior cerebellar peduncle**, but they
are **distinct structures**. Consumers must **not** conflate
the cerebellum with the midbrain.
**Boundary status (NOT the cerebellar peduncles — the peduncles
are WHITE-MATTER TRACTS, children of the PONS):** **Boundary
case — the cerebellum is NOT the cerebellar peduncles.** The
**cerebellar peduncles** — the **superior cerebellar
peduncle**, the **middle cerebellar peduncle**, and the
**inferior cerebellar peduncle** — are the **white-matter
tracts** that **connect** the cerebellum to the brainstem
(midbrain, pons, medulla). In the tree, the **cerebellar
peduncles** are **children of the pons**
(``.../metencephalon/pons/cerebellar_peduncles/``), **not**
children of the cerebellum — the **pons owns the peduncle
attachment**. The **cerebellum** (here) is the **grey-matter
and white-matter tissue** (cortex, deep nuclei, arbor vitae)
that the peduncles **connect**. **The peduncles are the
CONDUCTION INFRASTRUCTURE; the cerebellum is the TISSUE.** They
are **different structures** — consumers must **not** conflate
the cerebellum with the cerebellar peduncles.
**Boundary status (NOT the cerebellar cortex — the cortex is
the GREY-MATTER LAYER within the cerebellum):** **Boundary
case — the cerebellum is NOT the cerebellar cortex.** The
**cerebellar cortex** — the **three-layered** cortex
(**molecular layer**, **Purkinje cell layer**, **granular
layer**) — is the **grey-matter layer** that **covers** the
cerebellar hemispheres and vermis. The **cerebellum** (here)
is the **whole structure** — the cortex **plus** the deep
nuclei, **plus** the deep white matter (arbor vitae), **plus**
the sub-containers (hemispheres, vermis, nuclei, deep white
matter). **The cortex is a LAYER within the cerebellum; the
cerebellum is the WHOLE.** The **cerebellar cortex** is
documented as **prose** (not a structural child of the
cerebellum). Consumers must **not** conflate the cerebellum
with the cerebellar cortex.
**Boundary status (NOT the deep nuclei — the deep nuclei are
CHILDREN):** **Boundary case — the cerebellum is NOT the
cerebellar deep nuclei.** The **cerebellar deep nuclei** —
the **dentate nucleus**, the **fastigial nucleus**, and the
**interposed nucleus** (comprising the **emboliform
nucleus** and the **globose nucleus**) — are the **grey-matter
output nuclei** of the cerebellum. In the tree, the **deep
nuclei** are **children of the cerebellum**
(``.../cerebellum/nuclei/``). **The deep nuclei are a
SUB-STRUCTURE of the cerebellum; the cerebellum is the
CONTAINER.** Consumers must **not** conflate the cerebellum
with the deep nuclei.
**Boundary status (NOT the vermis — the vermis is a CHILD):**
**Boundary case — the cerebellum is NOT the vermis.** The
**vermis** (``.../cerebellum/vermis/``) is the **midline**
cerebellar region (posture, gait, axial motor control) — the
**spinocerebellum** midline. In the tree, the **vermis** is a
**child of the cerebellum**. **The vermis is a SUB-STRUCTURE
of the cerebellum; the cerebellum is the CONTAINER.** Consumers
must **not** conflate the cerebellum with the vermis.
**Boundary status (NOT the hemispheres — the hemispheres are a
CHILD):** **Boundary case — the cerebellum is NOT the
cerebellar hemispheres.** The **cerebellar hemispheres**
(``.../cerebellum/hemispheres/``) are the **lateral**
cerebellar regions (limb motor coordination, motor learning,
cognition) — the **cerebrocerebellum** lateral. In the tree,
the **hemispheres** are a **child of the cerebellum**. **The
hemispheres are a SUB-STRUCTURE of the cerebellum; the
cerebellum is the CONTAINER.** Consumers must **not** conflate
the cerebellum with the cerebellar hemispheres.
**Boundary status (NOT the deep white matter — the arbor vitae
is a CHILD):** **Boundary case — the cerebellum is NOT the
cerebellar deep white matter.** The **cerebellar deep white
matter** (the **arbor vitae**) is the **white-matter core** of
the cerebellum. In the tree, the **deep white matter** is a
**child of the cerebellum**
(``.../cerebellum/deep_white_matter/``). **The arbor vitae is
a SUB-STRUCTURE of the cerebellum; the cerebellum is the
CONTAINER.** Consumers must **not** conflate the cerebellum
with the deep white matter.
**Boundary status (NOT a single functional system — MULTIPLE
sub-regions with DIFFERENT functions):** **Boundary case — the
cerebellum is a HETEROGENEOUS suprasegmental structure with
MULTIPLE functional zones, not a single uniform system.** The
cerebellum includes:
*   **Vermis** — the **spinocerebellum** midline (posture,
    gait, axial motor control).
*   **Hemispheres** — the **cerebrocerebellum** lateral (limb
    motor coordination, motor learning, cognition).
*   **Flocculonodular lobe** — the **vestibulocerebellum**
    (vestibular control, eye movements).
*   **Deep nuclei** — the **output nuclei** (dentate,
    fastigial, interposed — motor output, cognitive-affective
    modulation).
*   **Deep white matter** — the **arbor vitae** (conduction
    infrastructure).
*   **Cerebellar cortex** — the **three-layered cortex**
    (molecular, Purkinje, granular — the **processing layer**).
**Each sub-region is functionally distinct** — the tree wires
the **deep_white_matter**, **hemispheres**, **nuclei**, and
**vermis** as **sub-containers**, and the functional
sub-regions (lobules, zones, microzones) are documented as
**prose or children of those sub-containers**. Consumers must
**not** treat the cerebellum as a single uniform region — it
is a **distributed suprasegmental structure** with
**heterogeneous sub-structures**.
**Boundary status (SLEA-FREE — the cerebellum is NOT an
extended-amygdala component):** **Boundary case — the
cerebellum is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere). The **cerebellum** is
a **suprasegmental neural structure** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA
warning**. Consumers must **not** import the SLEA warning into
the cerebellum — it is **SLEA-free**.
**Boundary status (NOT a single neural processor in the
classical sense — the cerebellum is a REGION, not a single
processor):** **Boundary case — the cerebellum is a REGION,
not a single neural processor.** It **contains** neural
processors (the cerebellar cortex microzones, the deep
nuclei, the Purkinje-cell output) — but it is **not itself a
processor**. The **processing** happens in the
**sub-structures** (cerebellar cortex, deep nuclei). The
**cerebellum** is the **suprasegmental structure** that
**contains** those sub-structures. Consumers must **not** treat
the cerebellum as a **single neural processor** — it is a
**suprasegmental structure** with **heterogeneous
sub-structures**, each with its own function.

Overview
--------
The cerebellum is the **suprasegmental neural structure** of the
**metencephalon** — the **"little brain"** — comprising the
**cerebellar cortex** (three-layered: molecular, Purkinje,
granular), the **cerebellar deep nuclei** (dentate, fastigial,
interposed), the **cerebellar deep white matter** (arbor
vitae), the **cerebellar hemispheres**, and the **vermis**,
organized into **three lobes** (anterior, posterior,
flocculonodular). It is a **container module** with four
**structural sub-containers** (``deep_white_matter/``,
``hemispheres/``, ``nuclei/``, and ``vermis/``).

**The cerebellum is the SUPRASEGMENTAL structure of the
metencephalon, distinct from the pons (brainstem) and the fourth
ventricle (CSF cavity).** The **pons** (``.../metencephalon/
pons/``) is the **brainstem**; the **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is the **CSF
cavity**; the **cerebellum** (here) is the **suprasegmental
neural structure** **dorsal** to the pons and **roofing** the
fourth ventricle.

**The cerebellum is NOT the brainstem.** The **brainstem** is
the **midbrain + pons + medulla oblongata** — the **segmental**
neuraxis. The **cerebellum** (here) is **suprasegmental** — it
is **attached to the brainstem** via the **cerebellar
peduncles**, but it is **NOT part of the brainstem** proper.

**The cerebellum is NOT the cerebrum.** The **cerebrum** (the
**cerebral hemispheres** — ``.../forebrain/telencephalon/
cerebral_hemispheres/``) is the **forebrain** structure. The
**cerebellum** (here) is the **hindbrain** structure — the
**"little brain."** The Latin **cerebellum** ("little brain")
is **not** the **cerebrum** ("brain").

**The cerebellum is a HETEROGENEOUS suprasegmental structure,
not a single structure.** It includes the **vermis**
(spinocerebellum midline — posture, gait, axial motor control),
the **hemispheres** (cerebrocerebellum lateral — limb motor
coordination, motor learning, cognition), the
**flocculonodular lobe** (vestibulocerebellum — vestibular
control, eye movements), the **deep nuclei** (output nuclei),
the **deep white matter** (arbor vitae — conduction
infrastructure), and the **cerebellar cortex** (three-layered
processing layer). Each sub-region is functionally distinct.

**The cerebellum is a REGION, not a single neural processor.**
The **processing** happens in the **sub-structures** (cerebellar
cortex, deep nuclei). The **cerebellum** is the
**suprasegmental structure** that **contains** those
sub-structures.

Cerebellar Composition (sub-containers and prose)
-------------------------------------------------
The cerebellum is a **suprasegmental structure** with **four
sub-containers** — documented as **structural children**
(``deep_white_matter/``, ``hemispheres/``, ``nuclei/``, and
``vermis/``) — and **many prose-defined sub-structures**
documented within those sub-containers:

*   **Deep White Matter**
    (``.../cerebellum/deep_white_matter/``) — the **arbor
    vitae** (the **white-matter core** of the cerebellum; the
    **conduction infrastructure** connecting the cerebellar
    cortex to the deep nuclei and the cerebellar peduncles).

*   **Hemispheres** (``.../cerebellum/hemispheres/``) — the
    **lateral** cerebellar hemispheres (**left** and **right**
    sub-containers), each with **three lobes**:
    *   **Anterior lobe** — the **spinocerebellum** (limb
        proprioception, motor execution).
    *   **Posterior lobe** — the **cerebrocerebellum** (motor
        planning, motor learning, cognition — including the
        **cerebellar cognitive-affective syndrome**).
    *   **Flocculonodular lobe** — the **vestibulocerebellum**
        (vestibular control, eye movements, balance).

*   **Nuclei** (``.../cerebellum/nuclei/``) — the **cerebellar
    deep nuclei** (the **grey-matter output nuclei**):
    *   **Dentate nucleus** — the **cerebrocerebellum**
        output (motor planning, cognition).
    *   **Fastigial nucleus** — the **spinocerebellum /
        vestibulocerebellum** output (axial motor, balance,
        eye movements).
    *   **Interposed nucleus** — the **spinocerebellum**
        output (limb motor control), comprising the
        **emboliform nucleus** and the **globose nucleus**.

*   **Vermis** (``.../cerebellum/vermis/``) — the **midline**
    cerebellar region, with **three lobes**:
    *   **Anterior lobe** — the **spinocerebellum midline**
        (axial proprioception, posture).
    *   **Posterior lobe** — the **spinocerebellum midline**
        (gait, axial motor control).
    *   **Flocculonodular lobe** — the **vestibulocerebellum
        midline** (vestibular control, balance).

**These sub-structures are children of the sub-containers (or
prose), not direct structural children of the cerebellum.** The
tree wires the **cerebellum** as a **container** with **four
sub-containers** (``deep_white_matter/``, ``hemispheres/``,
``nuclei/``, and ``vermis/``) — the **cerebellar cortex**, the
**cerebellar peduncles**, the **fissures**, and the
**lobules** are documented as **prose** or as **children of
the sub-containers** (e.g., the cerebellar peduncles are
**children of the pons**, not of the cerebellum). Consumers
that need **sub-region-level** resolution should consult the
**sub-container modules** and the references, not the
cerebellum container.

The Cerebellum / Metencephalon Boundary
---------------------------------------
This is the **child-vs-container** boundary:

*   **Cerebellum** (this module) — the **metencephalic
    suprasegmental sub-container**.

*   **Metencephalon** (``.../metencephalon/``) — the
    **container** (pons + cerebellum + fourth ventricle).

**The cerebellum is a PART of the metencephalon; the
metencephalon is the WHOLE.** Consumers must **not** conflate
the cerebellum with the metencephalon container.

The Cerebellum / Pons Boundary
------------------------------
This is the **suprasegmental-vs-brainstem** boundary:

*   **Cerebellum** (this module) — the **suprasegmental
    structure** (hemispheres, vermis, deep nuclei, deep white
    matter).

*   **Pons** (``.../metencephalon/pons/``) — the **brainstem
    structure** (basis pontis, tegmentum, cerebellar peduncles,
    cranial nerve nuclei V–VIII).

**They are DIFFERENT metencephalic sub-structures** — the
**pons** is the **brainstem**; the **cerebellum** is the
**suprasegmental** structure **dorsal** to the pons. They are
connected via the **cerebellar peduncles** (children of the
pons), but they are **distinct sub-structures**. Consumers must
**not** conflate the cerebellum with the pons.

The Cerebellum / Fourth Ventricle Boundary
------------------------------------------
This is the **tissue-vs-CSF-cavity** boundary:

*   **Cerebellum** (this module) — the **suprasegmental
    structure**.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the
    **metencephalic CSF cavity**.

**The fourth ventricle is the CAVITY; the cerebellum is the
TISSUE DORSAL to it.** The cerebellum **forms the roof** of the
fourth ventricle (the **tectum** of the fourth ventricle) via
the **superior medullary velum** and the **inferior medullary
velum**. Consumers must **not** conflate the cerebellum with
the fourth ventricle.

The Cerebellum / Brainstem Boundary
-----------------------------------
This is the **suprasegmental-vs-segmental** boundary:

*   **Cerebellum** (this module) — the **suprasegmental**
    structure.

*   **Brainstem** (midbrain + pons + medulla oblongata) — the
    **segmental** neuraxis that contains the cranial nerve
    nuclei and the long ascending/descending tracts.

**The cerebellum is SUPRASEGMENTAL, not brainstem.** It is
**attached to the brainstem** via the **cerebellar peduncles**,
but it is **NOT part of the brainstem** proper. The cerebellum
is **suprasegmental**; the brainstem is **segmental**.
Consumers must **not** conflate the cerebellum with the
brainstem.

The Cerebellum / Cerebrum Boundary
----------------------------------
This is the **hindbrain-vs-forebrain** boundary:

*   **Cerebellum** (this module) — the **hindbrain** structure
    (the **"little brain"**).

*   **Cerebrum** (``.../forebrain/telencephalon/
    cerebral_hemispheres/``) — the **forebrain** structure (the
    **"brain"** — cortex, white matter, basal ganglia,
    hippocampus, amygdala).

**They are DIFFERENT structures in DIFFERENT brain vesicles** —
the **cerebrum** is **forebrain**; the **cerebellum** is
**hindbrain**. The Latin **cerebellum** ("little brain") is
**not** the **cerebrum** ("brain"). Consumers must **not**
conflate the cerebellum with the cerebrum.

The Cerebellum / Hindbrain Boundary
-----------------------------------
This is the **grandchild-vs-container** boundary:

*   **Cerebellum** (this module) — a **child of the
    metencephalon** (a **grandchild of the hindbrain**).

*   **Hindbrain** (``.../hindbrain/``) — the **whole**
    rhombencephalon derivative (metencephalon +
    myelencephalon).

**The cerebellum is a PART of the hindbrain (via the
metencephalon); the hindbrain is the WHOLE.** Consumers must
**not** conflate the cerebellum with the hindbrain container.

The Cerebellum / Myelencephalon Boundary
----------------------------------------
This is the **rostral-vs-caudal** boundary:

*   **Cerebellum** (this module) — a **child of the
    metencephalon** (the **rostral** hindbrain sub-container).

*   **Myelencephalon** (``.../hindbrain/myelencephalon/``) — the
    **caudal** hindbrain sub-container (medulla oblongata).

**They are DIFFERENT hindbrain sub-compartments** — the
**cerebellum** is **rostral** (via the metencephalon); the
**myelencephalon** is **caudal**. Consumers must **not**
conflate the cerebellum with the myelencephalon.

The Cerebellum / Midbrain Boundary
----------------------------------
This is the **caudal-vs-rostral** boundary:

*   **Cerebellum** (this module) — the **metencephalic
    suprasegmental structure**.

*   **Midbrain** (``.../midbrain/``) — the **mesencephalon**
    derivative (tectum + tegmentum + cerebral peduncle +
    mesencephalic aqueduct).

**They are DIFFERENT developmental compartments** — the
**midbrain** is **rostral**; the **cerebellum** is **caudal**
(in the metencephalon). They are connected via the **superior
cerebellar peduncle**, but they are **distinct structures**.
Consumers must **not** conflate the cerebellum with the
midbrain.

The Cerebellum / Cerebellar Peduncles Boundary
----------------------------------------------
This is the **tissue-vs-white-matter-tract** boundary:

*   **Cerebellum** (this module) — the **grey-matter and
    white-matter tissue** (cortex, deep nuclei, arbor vitae).

*   **Cerebellar peduncles** (superior, middle, inferior —
    ``.../metencephalon/pons/cerebellar_peduncles/``) — the
    **white-matter tracts** that **connect** the cerebellum
    to the brainstem.

**The peduncles are the CONDUCTION INFRASTRUCTURE; the
cerebellum is the TISSUE.** In the tree, the peduncles are
**children of the pons**, not of the cerebellum — the **pons
owns the peduncle attachment**. Consumers must **not** conflate
the cerebellum with the cerebellar peduncles.

The Cerebellum / Cerebellar Cortex Boundary
-------------------------------------------
This is the **whole-vs-layer** boundary:

*   **Cerebellum** (this module) — the **whole structure**
    (cortex + deep nuclei + arbor vitae + sub-containers).

*   **Cerebellar cortex** — the **three-layered grey-matter
    layer** (molecular, Purkinje, granular) that **covers** the
    hemispheres and vermis (prose).

**The cortex is a LAYER within the cerebellum; the cerebellum is
the WHOLE.** The **cerebellar cortex** is documented as
**prose** (not a structural child of the cerebellum).
Consumers must **not** conflate the cerebellum with the
cerebellar cortex.

The Cerebellum / Deep Nuclei Boundary
-------------------------------------
This is the **container-vs-child** boundary:

*   **Cerebellum** (this module) — the **container**.

*   **Cerebellar deep nuclei**
    (``.../cerebellum/nuclei/``) — the **grey-matter output
    nuclei** (dentate, fastigial, interposed).

**The deep nuclei are a SUB-STRUCTURE of the cerebellum; the
cerebellum is the CONTAINER.** Consumers must **not** conflate
the cerebellum with the deep nuclei.

The Cerebellum / Vermis Boundary
--------------------------------
This is the **container-vs-child** boundary:

*   **Cerebellum** (this module) — the **container**.

*   **Vermis** (``.../cerebellum/vermis/``) — the **midline**
    cerebellar region (spinocerebellum midline).

**The vermis is a SUB-STRUCTURE of the cerebellum; the
cerebellum is the CONTAINER.** Consumers must **not** conflate
the cerebellum with the vermis.

The Cerebellum / Hemispheres Boundary
-------------------------------------
This is the **container-vs-child** boundary:

*   **Cerebellum** (this module) — the **container**.

*   **Cerebellar hemispheres**
    (``.../cerebellum/hemispheres/``) — the **lateral**
    cerebellar regions (cerebrocerebellum lateral).

**The hemispheres are a SUB-STRUCTURE of the cerebellum; the
cerebellum is the CONTAINER.** Consumers must **not** conflate
the cerebellum with the cerebellar hemispheres.

The Cerebellum / Deep White Matter Boundary
-------------------------------------------
This is the **container-vs-child** boundary:

*   **Cerebellum** (this module) — the **container**.

*   **Cerebellar deep white matter**
    (``.../cerebellum/deep_white_matter/``) — the **arbor
    vitae** (the white-matter core).

**The arbor vitae is a SUB-STRUCTURE of the cerebellum; the
cerebellum is the CONTAINER.** Consumers must **not** conflate
the cerebellum with the deep white matter.

The Cerebellum / SLEA Boundary
------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cerebellum** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only
    SLEA component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The cerebellum is NOT part of the SLEA continuum.** It is a
**suprasegmental neural structure**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into
the cerebellum.

Function in the Human Brain
---------------------------
The cerebellum's functions are **heterogeneous** — documented
at the **sub-structure** level, not at the structure level:

*   **Motor Coordination and Balance (Hemispheres, Vermis, Deep
    Nuclei):** The **cerebellum** coordinates **voluntary
    movement** — the **spinocerebellum** (vermis + anterior
    lobe) coordinates **posture and gait**; the
    **cerebrocerebellum** (posterior lobe of the hemispheres)
    coordinates **limb motor planning and execution**; the
    **vestibulocerebellum** (flocculonodular lobe) coordinates
    **balance and eye movements**. The **deep nuclei**
    (dentate, fastigial, interposed) are the **output
    nuclei** that **transmit** the cerebellar output to the
    brainstem and thalamus.

*   **Motor Learning (Cerebellar Cortex, Deep Nuclei):** The
    **cerebellum** is the **neural substrate** of **motor
    learning** — the **cerebellar cortex** (Purkinje cells)
    and the **deep nuclei** (dentate, interposed) are
    **plastic** during **motor adaptation**, **classical
    conditioning** (e.g., **eyeblink conditioning**), and
    **skill learning**.

*   **Cerebellar Cognitive-Affective Syndrome (CCAS):** The
    **cerebellum** — especially the **posterior lobe** of the
    **hemispheres** and the **vermis** — is involved in
    **executive function**, **visuospatial processing**,
    **language**, and **affective regulation**. Lesions cause
    **cerebellar cognitive-affective syndrome** (CCAS) —
    **executive dysfunction**, **visuospatial deficits**,
    **language deficits**, and **affective dysregulation**.

*   **Vestibular Control and Eye Movements
    (Flocculonodular Lobe, Fastigial Nucleus):** The
    **flocculonodular lobe** (vestibulocerebellum) and the
    **fastigial nucleus** are involved in **vestibular
    control**, **balance**, and **eye movements** (the
    **vestibulo-ocular reflex**, **saccadic accuracy**,
    **smooth pursuit**).

*   **Cerebellar Contribution to Non-Motor Functions
    (Hemispheres, Vermis):** The **cerebellum** contributes to
    **language** (right cerebellar hemisphere), **visuospatial
    function** (left cerebellar hemisphere), **working
    memory**, **attention**, **social cognition**, and
    **affective processing** — via the **cerebellar-cortical
    loops** (cerebellum → thalamus → cortex).

*   **NOT the brainstem.** The **brainstem** (midbrain, pons,
    medulla) is the **segmental** neuraxis — it **contains the
    cranial nerve nuclei** and the **long ascending/descending
    tracts**. The **cerebellum** is **suprasegmental** — it
    **modulates** the brainstem and the cortex, but it is
    **NOT part of the brainstem** proper.

*   **NOT the cerebrum.** The **cerebrum** (cerebral
    hemispheres) is the **forebrain** structure — it
    **contains the cortex**, the **basal ganglia**, the
    **hippocampus**, and the **amygdala**. The **cerebellum**
    is the **hindbrain** structure — the **"little brain."**
    The two are **distinct structures in distinct brain
    vesicles**.

*   **NOT a single neural processor.** The cerebellum is a
    **suprasegmental structure** — the **processing** happens
    in the **sub-structures** (cerebellar cortex, deep nuclei).
    Consumers must **not** treat the cerebellum as a **single
    processor** — it is a **structure** with **heterogeneous
    sub-structures**.

**The unifying theme:** the cerebellum is the **suprasegmental
structure of the metencephalon** — the **"little brain"** —
that **coordinates motor execution, motor learning, balance,
eye movements, and non-motor (cognitive-affective) functions**.
It **contains** the **cerebellar cortex** (three-layered
processing layer), the **cerebellar deep nuclei** (output
nuclei), the **cerebellar deep white matter** (arbor vitae —
conduction infrastructure), the **cerebellar hemispheres**
(lateral regions), and the **vermis** (midline region). It is a
**heterogeneous suprasegmental structure**, **NOT a single
neural processor**, and **NOT the brainstem, cerebrum,
metencephalon, pons, or fourth ventricle**.

Associated Disorders
--------------------
The cerebellum has **named clinical syndromes** — its clinical
associations are **cerebellar** (via the **cerebellar cortex**,
the **cerebellar deep nuclei**, and the **cerebellar
peduncles**):

*   **Cerebellar Ataxia (via the Cerebellum):** **Gait
    ataxia**, **limb ataxia**, **dysarthria** (scanning
    speech), **nystagmus**, and **dysmetria** — the
    **cerebellar motor syndrome**. Causes include **cerebellar
    stroke** (PICA, AICA, SCA infarcts), **cerebellar
    hemorrhage**, **cerebellar tumors**, **multiple sclerosis**
    (cerebellar plaques), **alcohol-related cerebellar
    degeneration** (anterior vermis), and **paraneoplastic
    cerebellar degeneration**.

*   **Spinocerebellar Ataxias (SCAs):** A group of
    **genetically inherited** **cerebellar ataxias** —
    **autosomal dominant** (SCA1–SCA48+), **autosomal
    recessive** (Friedreich ataxia), and **X-linked** — with
    **progressive cerebellar ataxia** as the core phenotype,
    often with **brainstem**, **basal ganglia**, **retinal**,
    and **cognitive** involvement. The **cerebellum** is the
    **primary substrate**.

*   **Cerebellar Cognitive-Affective Syndrome (CCAS):**
    **Executive dysfunction**, **visuospatial deficits**,
    **language deficits** (agrammatism, dysprosodia),
    **affective dysregulation** — caused by **cerebellar
    lesions** (especially **posterior lobe** of the
    **hemispheres** and the **vermis**). The **cerebellum** is
    the **substrate** — the **cerebellar-cortical loops**
    (cerebellum → thalamus → prefrontal cortex) are the
    **mechanism**.

*   **Cerebellar Tumors:** **Medulloblastoma** (the most common
    **malignant pediatric brain tumor**, arising in the
    **cerebellar vermis** — the **midline** cerebellum),
    **pilocytic astrocytoma** (the most common **benign
    pediatric brain tumor**, arising in the **cerebellar
    hemispheres**), **ependymoma** (arising from the
    **ependyma** of the **fourth ventricle** — at the
    **cerebellar–fourth-ventricle interface**), and
    **hemangioblastoma** (adult, cerebellar hemispheres). The
    **cerebellum** is the **primary substrate**.

*   **Cerebellar Stroke:** **PICA infarct** (lateral medullary
    syndrome / Wallenberg — involves the **inferior cerebellar
    peduncle** and the **cerebellar hemisphere**),
    **AICA infarct** (lateral pontine syndrome — involves the
    **middle cerebellar peduncle** and the **cerebellar
    hemisphere**), and **SCA infarct** (superior cerebellar
    syndrome — involves the **superior cerebellar peduncle**
    and the **cerebellar hemisphere**). The **cerebellum** is
    the **substrate**.

*   **Cerebellar Hemorrhage:** **Hypertensive cerebellar
    hemorrhage** — typically in the **cerebellar
    hemispheres** or the **vermis** — can cause **rapid
    neurological deterioration** (due to **fourth-ventricle
    compression** and **brainstem compression**) and requires
    **emergency neurosurgical evacuation**.

*   **Alcohol-Related Cerebellar Degeneration:** **Chronic
    alcohol use** causes **anterior vermis** degeneration —
    **gait ataxia** (truncal ataxia) with **relatively
    preserved limb coordination**. The **cerebellar vermis** is
    the **substrate**.

*   **Paraneoplastic Cerebellar Degeneration:** **Anti-Yo**,
    **anti-Hu**, **anti-Tr**, **anti-Ri**, and
    **anti-metabotropic glutamate receptor 1 (mGluR1)**
    antibodies — **paraneoplastic cerebellar degeneration**
    associated with **ovarian cancer**, **breast cancer**,
    **Hodgkin lymphoma**, and other malignancies. The
    **cerebellar Purkinje cells** are the **primary target**.

*   **Multiple Sclerosis (Cerebellar Plaques):** **Demyelinating
    plaques** in the **cerebellar peduncles**, the
    **cerebellar white matter**, and the **cerebellar
    cortex** — causing **cerebellar ataxia**, **dysarthria**,
    **nystagmus**, and **intention tremor**. The **cerebellum**
    is a **substrate**.

*   **Cerebellar Mutism Syndrome (Posterior Fossa Syndrome):**
    **Transient mutism**, **emotional lability**, and
    **cerebellar ataxia** after **posterior fossa surgery**
    (especially **medulloblastoma** resection in children) —
    the **cerebellar vermis** and the **cerebellar peduncles**
    are the **substrate**.

*   **No Named "Cerebellum Syndrome" (singular):** The
    cerebellum has **multiple named clinical syndromes**
    (cerebellar ataxia, CCAS, SCAs, medulloblastoma, etc.) —
    but **no single "cerebellum syndrome."** Its clinical
    relevance is **cerebellar** — via the **cerebellar
    cortex**, the **cerebellar deep nuclei**, and the
    **cerebellar peduncles**.

**What is NOT here:** The cerebellum is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala), **fear conditioning**
(central nucleus + basolateral nuclei), **Urbach-Wiethe
disease** (amygdala), or **Parkinson's disease** (substantia
nigra, in the midbrain). Its clinical relevance is
**cerebellar** — **cerebellar ataxia**, **CCAS**, **SCAs**,
**cerebellar tumors**, and **cerebellar stroke**.

Lateralization Notes
--------------------
This is the **cerebellum** container module. The cerebellum is a
**midline-spanning suprasegmental structure** with **bilateral
sub-structures** — and it carries **NO warning**:

*   **Bilateral Sub-Structures:** The **cerebellar
    hemispheres** have **left and right** sub-containers; the
    **vermis** is **midline**; the **deep nuclei** (dentate,
    fastigial, interposed) are **bilateral pairs**. The
    cerebellum is **not a paired structure** in the way the
    **lateral ventricles** or the **amygdala** are — it is a
    **midline structure** with **bilateral sub-structures**.

*   **Partial Lateralization (Contested):** Some **cerebellar
    functions** are **partially lateralized** — **language**
    is more **right cerebellar** (the **right cerebellar
    hemisphere** is connected to the **left frontal lobe** via
    the **cerebellar-cortical loops**); **visuospatial**
    function is more **left cerebellar** (the **left
    cerebellar hemisphere** is connected to the **right
    parietal lobe**). This is **partial**, **contested**, and
    documented in the **cerebellum module** (not at the
    metencephalon level).

*   **NO Extended-Amygdala Warning (SLEA-free):** The cerebellum
    is **NOT** an extended-amygdala component. It carries **no
    SLEA warning**. Consumers must **not** import the SLEA
    warning into the cerebellum.

*   **NO Amygdala-Lateralization Warning:** The cerebellum is
    **NOT** the fear-output or the fear-learning structure. It
    is a **suprasegmental structure** — consumers must **not**
    conflate it with the **amygdala** or the **fear circuit**.

**A consumer that assumes "cerebellum = left + right" will be
structurally correct for the bilateral sub-structures** — the
cerebellum is a **midline structure** with **bilateral
sub-structures**. The cerebellum carries **NO warning** — **no
SLEA warning**, **no amygdala-lateralization warning**, and
**no rhinencephalon-exclusion flag**. The partial
cerebellar lateralization (language = right cerebellar;
visuospatial = left cerebellar) is **contested** and documented
as **prose**, not as a **warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-region imports.** The **container** does **not**
    import from ``.../metencephalon/`` (parent),
    ``.../metencephalon/pons/`` (sibling),
    ``.../metencephalon/fourth_ventricle/`` (sibling),
    ``.../hindbrain/``, ``.../midbrain/``, ``.../forebrain/``,
    ``.../spinal_cord/``, ``.../cerebellum/deep_white_matter/``,
    ``.../cerebellum/hemispheres/``, ``.../cerebellum/nuclei/``,
    or ``.../cerebellum/vermis/`` — it is a **namespace
    container**.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../forebrain/telencephalon/``,
    ``.../forebrain/diencephalon/``, ``.../midbrain/``,
    ``.../spinal_cord/``, or any other container. The
    cerebellum's relationships to the metencephalon, pons,
    fourth ventricle, brainstem, cerebrum, hindbrain,
    myelencephalon, midbrain, cerebellar peduncles, cerebellar
    cortex, deep nuclei, vermis, hemispheres, and deep white
    matter are documented as **prose and boundary data**, not
    as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container module — four structural children.** The
    ``deep_white_matter/``, ``hemispheres/``, ``nuclei/``, and
    ``vermis/`` are **sub-containers**. The **cerebellar
    cortex**, the **cerebellar peduncles**, the **fissures**,
    and the **lobules** are **prose** or **children of the
    sub-containers**. Consumers must not assume any exist as
    direct children of the cerebellum; resolve sub-region-level
    detail through the sub-containers and the references.
*   **SUPRASEGMENTAL STRUCTURE — NOT the brainstem.** The
    cerebellum is **suprasegmental** — it is **attached to the
    brainstem** via the **cerebellar peduncles**, but it is
    **NOT part of the brainstem** proper.
*   **NOT the cerebrum — the cerebellum is the "LITTLE brain."**
    The **cerebrum** (cerebral hemispheres) is the **forebrain**
    structure; the **cerebellum** is the **hindbrain**
    structure. They are **different structures in different
    brain vesicles**.
*   **NOT the metencephalon — the cerebellum is a CHILD.** The
    **metencephalon** is the **container** (pons + cerebellum
    + fourth ventricle).
*   **NOT the pons or fourth ventricle — those are SIBLINGS.**
    The **pons** is the **brainstem**; the **fourth
    ventricle** is the **CSF cavity**; the **cerebellum** is
    the **suprasegmental structure**.
*   **NOT the hindbrain — the cerebellum is a GRANDCHILD.** The
    **hindbrain** is the **whole** rhombencephalon derivative.
*   **NOT the myelencephalon — the myelencephalon is the CAUDAL
    SIBLING of the metencephalon.**
*   **NOT the midbrain — the midbrain is ROSTRAL.** The
    **midbrain** is the **mesencephalon** derivative; the
    **cerebellum** is the **metencephalic** structure.
*   **NOT the cerebellar peduncles — the peduncles are
    WHITE-MATTER TRACTS, children of the PONS.** The
    **peduncles** are the **conduction infrastructure**; the
    **cerebellum** is the **tissue**.
*   **NOT the cerebellar cortex — the cortex is a GREY-MATTER
    LAYER within the cerebellum.**
*   **NOT the deep nuclei, vermis, hemispheres, or deep white
    matter alone — those are SUB-STRUCTURES.** The **cerebellum**
    is the **container**; the **sub-structures** are its
    **contents**.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    cerebellum is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT a single neural processor — the cerebellum is a
    REGION.** The **processing** happens in the **sub-structures**
    (cerebellar cortex, deep nuclei). Consumers must **not**
    treat the cerebellum as a **single processor**.
*   **No ``AREA_PATHS`` hop.** The cerebellum is a local
    sub-container under ``metencephalon/``, not a cross-listed
    container.
*   **No nested cross-listing.** The cerebellum has no nested
    dual-framing module. It is a single sub-container with four
    sub-containers.
*   **No lateralization warning.** The cerebellum carries **no
    warning** — **no SLEA warning**, **no
    amygdala-lateralization warning**, and **no
    rhinencephalon-exclusion flag**. The partial cerebellar
    lateralization (language = right cerebellar; visuospatial
    = left cerebellar) is **contested** and documented as
    **prose**, not as a **warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.metencephalon.cerebellum import (
        deep_white_matter, hemispheres, nuclei, vermis,
    )

Or by fully-qualified path string::

    path = (
        "hindbrain.metencephalon.cerebellum"
    )
    hemispheres_path = (
        "hindbrain.metencephalon.cerebellum.hemispheres"
    )
    vermis_path = (
        "hindbrain.metencephalon.cerebellum.vermis"
    )
    nuclei_path = (
        "hindbrain.metencephalon.cerebellum.nuclei"
    )
    deep_white_matter_path = (
        "hindbrain.metencephalon.cerebellum.deep_white_matter"
    )

**Do not** assume the cerebellum is the **metencephalon**. The
**metencephalon** is the **container** (pons + cerebellum +
fourth ventricle); the **cerebellum** is a **child**.

**Do not** assume the cerebellum is the **pons** or the
**fourth ventricle**. The **pons** is the **brainstem**; the
**fourth ventricle** is the **CSF cavity**; the **cerebellum**
is the **suprasegmental structure**.

**Do not** assume the cerebellum is the **brainstem**. The
cerebellum is **suprasegmental** — it is **attached to the
brainstem** via the **cerebellar peduncles**, but it is **NOT
part of the brainstem** proper.

**Do not** assume the cerebellum is the **cerebrum**. The
**cerebrum** (cerebral hemispheres) is the **forebrain**
structure; the **cerebellum** is the **hindbrain** structure —
the **"little brain."**

**Do not** assume the cerebellum is the **hindbrain** or the
**myelencephalon**. The **hindbrain** is the **whole**
rhombencephalon derivative; the **myelencephalon** is the
**caudal** hindbrain sub-container.

**Do not** assume the cerebellum is the **midbrain**. The
**midbrain** is the **mesencephalon** derivative; the
**cerebellum** is the **metencephalic** structure.

**Do not** assume the cerebellum is the **cerebellar
peduncles**. The **peduncles** are the **white-matter tracts**
(children of the pons); the **cerebellum** is the **tissue**.

**Do not** assume the cerebellum is the **cerebellar cortex**,
the **deep nuclei**, the **vermis**, the **hemispheres**, or
the **deep white matter alone**. The **cerebellum** is the
**container**; the **sub-structures** are its **contents**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the cerebellum. **The
cerebellum is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the cerebellum's children (recommended consumer
pattern)::

    CEREBELLUM_CHILDREN = (
        "deep_white_matter", "hemispheres", "nuclei", "vermis",
    )
    # The deep_white_matter, hemispheres, nuclei, and vermis are
    # sub-containers. The cerebellar cortex, cerebellar peduncles,
    # fissures, and lobules are prose or children of the
    # sub-containers.

Reaching the metencephalon (recommended consumer pattern — the
parent)::

    # The metencephalon is the CONTAINER (pons + cerebellum +
    # fourth ventricle):
    #
    #   hindbrain.metencephalon
    #
    # The cerebellum is a CHILD sub-container of the
    # metencephalon.

Reaching the pons (recommended consumer pattern — the
suprasegmental-vs-brainstem boundary)::

    # The pons is the BRAINSTEM structure:
    #
    #   hindbrain.metencephalon.pons
    #
    # The cerebellum is the SUPRASEGMENTAL structure DORSAL to
    # the pons. They are connected via the cerebellar peduncles
    # (children of the pons).

Reaching the fourth ventricle (recommended consumer pattern — the
tissue-vs-CSF-cavity boundary)::

    # The fourth ventricle is the METENCEPHALIC CSF cavity:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The cerebellum FORMS THE ROOF of the fourth ventricle
    # (via the superior and inferior medullary vela).

Reaching the brainstem (recommended consumer pattern — the
suprasegmental-vs-segmental boundary)::

    # The brainstem is the SEGMENTAL neuraxis (midbrain + pons +
    # medulla):
    #
    #   midbrain          (mesencephalon)
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The cerebellum is SUPRASEGMENTAL — attached to the
    # brainstem via the cerebellar peduncles, but NOT part of
    # the brainstem proper.

Reaching the cerebrum (recommended consumer pattern — the
hindbrain-vs-forebrain boundary)::

    # The cerebrum is the FOREBRAIN structure (cerebral
    # hemispheres):
    #
    #   forebrain.telencephalon.cerebral_hemispheres
    #
    # The cerebellum is the HINDBRAIN structure — the "little
    # brain."

Reaching the hindbrain (recommended consumer pattern — the
grandparent)::

    # The hindbrain is the WHOLE rhombencephalon derivative
    # (metencephalon + myelencephalon):
    #
    #   hindbrain
    #
    # The cerebellum is a GRANDCHILD of the hindbrain (via the
    # metencephalon).

Reaching the myelencephalon (recommended consumer pattern — the
rostral-vs-caudal boundary)::

    # The myelencephalon is the CAUDAL hindbrain sub-container:
    #
    #   hindbrain.myelencephalon
    #
    # The cerebellum is ROSTRAL (via the metencephalon); the
    # myelencephalon is CAUDAL.

Reaching the midbrain (recommended consumer pattern — the
caudal-vs-rostral boundary)::

    # The midbrain is the MESENCEPHALON derivative ROSTRAL to the
    # metencephalon:
    #
    #   midbrain
    #
    # The cerebellum is CAUDAL to the midbrain (in the
    # metencephalon). They are connected via the superior
    # cerebellar peduncle.

Reaching the cerebellar peduncles (recommended consumer pattern —
the tissue-vs-white-matter-tract boundary)::

    # The cerebellar peduncles are the WHITE-MATTER TRACTS
    # connecting the cerebellum to the brainstem — children of
    # the PONS:
    #
    #   hindbrain.metencephalon.pons.cerebellar_peduncles
    #
    # The peduncles are the CONDUCTION INFRASTRUCTURE; the
    # cerebellum is the TISSUE.

Reaching the deep nuclei (recommended consumer pattern — the
child)::

    # The deep nuclei are the GREY-MATTER OUTPUT NUCLEI of the
    # cerebellum:
    #
    #   hindbrain.metencephalon.cerebellum.nuclei
    #
    # The deep nuclei are a SUB-STRUCTURE of the cerebellum.

Reaching the vermis (recommended consumer pattern — the
child)::

    # The vermis is the MIDLINE cerebellar region:
    #
    #   hindbrain.metencephalon.cerebellum.vermis
    #
    # The vermis is a SUB-STRUCTURE of the cerebellum.

Reaching the hemispheres (recommended consumer pattern — the
child)::

    # The hemispheres are the LATERAL cerebellar regions:
    #
    #   hindbrain.metencephalon.cerebellum.hemispheres
    #
    # The hemispheres are a SUB-STRUCTURE of the cerebellum.

Reaching the deep white matter (recommended consumer pattern —
the child)::

    # The deep white matter is the ARBOR VITAE — the
    # white-matter core of the cerebellum:
    #
    #   hindbrain.metencephalon.cerebellum.deep_white_matter
    #
    # The arbor vitae is a SUB-STRUCTURE of the cerebellum.

Cerebellar cortex detail (not wired — consult references)::

    # The cerebellar cortex is the THREE-LAYERED grey-matter
    # layer covering the hemispheres and vermis (prose, not a
    # structural child):
    #   molecular layer -> Purkinje cell layer -> granular layer
    #   (with climbing fibers, mossy fibers, parallel fibers,
    #    and the Purkinje-cell output to the deep nuclei)
    #
    # Do not attempt to resolve the cerebellar cortex as a
    # sub-path of the cerebellum.

Bilateral iteration (recommended consumer pattern — for bilateral
sub-structures)::

    for side in ("left", "right"):
        # e.g., cerebellar hemispheres, deep nuclei
        side_path = (
            f"hindbrain.metencephalon.cerebellum.hemispheres.{side}"
        )
        # resolve side_path through the memory/recall layer

References
----------
*   **Canonical cerebellar anatomy:** Standring, S. (ed.) (2020).
    *Gray's Anatomy: The Anatomical Basis of Clinical Practice*,
    42nd ed. (Cerebellum — hemispheres, vermis, lobes, deep
    nuclei, arbor vitae, cerebellar cortex.)
*   **Cerebellar overview:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed.
    (Cerebellum — hemispheres, vermis, deep nuclei, cerebellar
    peduncles, cerebellar cortex.)
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
*   **Cerebellar cortex microcircuitry:** Eccles, J.C., Ito, M.,
    Szentágothai, J. (1967). *The Cerebellum as a Neuronal
    Machine*. (Cerebellar cortex — molecular, Purkinje, and
    granular layers; climbing fibers, mossy fibers, parallel
    fibers.)
*   **Cerebellar deep nuclei:** Allen, G.I., Tsukahara, N.
    (1974). "Cerebrocerebellar communication systems."
    *Physiological Reviews* 54:957–1006. (Dentate, fastigial,
    interposed — the cerebellar deep nuclei and their
    cerebrocerebellar output.)
*   **Spinocerebellar ataxias:** Paulson, H.L. (2009). "The
    spinocerebellar ataxias." In *Neurogenetics* (Vance, J.M.,
    ed.). (SCAs — autosomal dominant cerebellar ataxias.)
*   **Friedreich ataxia:** Campuzano, V., et al. (1996).
    "Friedreich's ataxia: autosomal recessive disease caused by
    an intronic GAA triplet repeat expansion." *Science*
    271:1423–1427. (Friedreich ataxia — autosomal recessive
    cerebellar ataxia.)
*   **Medulloblastoma:** Louis, D.N., et al. (2016). "The 2016
    World Health Organization Classification of Tumors of the
    Central Nervous System: a summary." *Acta Neuropathologica*
    131:803–820. (Medulloblastoma — pediatric cerebellar
    tumor; cerebellar vermis.)
*   **Pilocytic astrocytoma:** Collins, V.P., et al. (2015).
    "Pilocytic astrocytoma." In *WHO Classification of Tumours
    of the Central Nervous System* (Louis, D.N., et al., eds.).
    (Pilocytic astrocytoma — pediatric cerebellar hemisphere
    tumor.)
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
    cerebellar hemispheres and vermis.)
*   **Alcohol-related cerebellar degeneration:** Victor, M.,
    Adams, R.D., Mancall, E.L. (1959). "A restricted form of
    cerebellar cortical degeneration occurring in alcoholic
    patients." *A.M.A. Archives of Neurology* 1:579–688.
    (Anterior vermis degeneration — alcohol-related cerebellar
    ataxia.)
*   **Paraneoplastic cerebellar degeneration:** Dalmau, J.,
    Rosenfeld, M.R. (2008). "Paraneoplastic syndromes of the
    CNS." *The Lancet Neurology* 7:327–340. (Paraneoplastic
    cerebellar degeneration — anti-Yo, anti-Hu, anti-Tr,
    anti-mGluR1; Purkinje cell target.)
*   **Cerebellar mutism syndrome:** Rekate, H.L., et al. (1985).
    "Muteness of cerebellar origin." *American Journal of
    Diseases of Children* 139:697–698. (Cerebellar mutism
    syndrome — posterior fossa surgery; cerebellar vermis and
    peduncles.)
*   **Cerebellar lateralization (contested):** Mariën, P., et
    al. (2014). "Consensus paper: language and the cerebellum
    — an ongoing puzzle in neurobehavioural
    neuroscience." *The Cerebellum* 13:386–410. (Right
    cerebellar hemisphere — language; left cerebellar
    hemisphere — visuospatial; partial, contested.)
*   **SLEA (contrast — the cerebellum is NOT included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum,
    nucleus accumbens; NOT the cerebellum.)
*   NeuroNames — Cerebellum; FMA — Cerebellum.
"""