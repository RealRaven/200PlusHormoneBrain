"""
infrastructure.brainparts.hindbrain.myelencephalon
===================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon   <-- THIS MODULE
        └── medulla_oblongata

**Primary synonym:** Myelencephalon (afterbrain); caudal
rhombencephalon; medulla vesicle (embryological).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**developmental / embryological subdivision** of the hindbrain — the
**caudal of the two secondary hindbrain vesicles** (the other is the
**metencephalon**). In the adult it is the **container** for the
**medulla oblongata**.
**Part of:** The **hindbrain** (rhombencephalon) — together with the
**metencephalon** (pons + cerebellum + fourth ventricle).
**Structural parent:** ``.../hindbrain/`` → **direct child** of the
hindbrain container.
**Structural children:** **One —** ``medulla_oblongata``. The
myelencephalon is a **single-child container**: the embryological
vesicle becomes the adult medulla oblongata, and the tree wires that
relationship as one structural child.
**Boundary status (NOT the hindbrain — a subdivision of it):**
**Boundary case — the myelencephalon is NOT the hindbrain; it is
one of the two hindbrain subdivisions.** The **hindbrain**
(``.../hindbrain/``) contains **both** the **myelencephalon** (here)
and the **metencephalon**. Consumers must **not** conflate the
**myelencephalon** with the **whole hindbrain** — the hindbrain is
the **parent container**, and the myelencephalon is its **caudal
subdivision**.
**Boundary status (NOT the metencephalon — that is the rostral
sibling):** **Boundary case — the myelencephalon is NOT the
metencephalon; the metencephalon is the rostral hindbrain
subdivision.** The **metencephalon** (``.../metencephalon/``)
contains the **pons**, the **cerebellum**, and the **fourth
ventricle**. The **myelencephalon** (here) contains the **medulla
oblongata**. **They are DIFFERENT SUBDIVISIONS** — the
**metencephalon** is rostral (pontine/cerebellar); the
**myelencephalon** is caudal (medullary). Consumers must **not**
conflate the two.
**Boundary status (NOT the medulla oblongata — that is the
structural child):** **Boundary case — the myelencephalon is NOT the
medulla oblongata; the medulla oblongata is its child.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the **adult
structure** — the **grey-matter nuclei** (cranial nerve nuclei
IX–XII, olivary complex, respiratory centers, cardiovascular
centers, reticular nuclei, dorsal column nuclei, etc.) and the
**white-matter tracts** (pyramids, medial lemniscus, spinothalamic
tract, etc.). The **myelencephalon** (here) is the **developmental
container** — the **vesicle** that **becomes** the medulla
oblongata. Consumers must **not** conflate the **container** with
its **single structural child** — the **myelencephalon** is the
**vesicle**; the **medulla oblongata** is the **adult structure**.
**Boundary status (NOT the brainstem — the brainstem spans multiple
containers):** **Boundary case — the myelencephalon is NOT the
brainstem; the brainstem is a cross-container system.** The
**brainstem** comprises the **midbrain** (mesencephalon), the
**pons** (metencephalon), and the **medulla oblongata**
(myelencephalon) — it **spans three different containers** in the
tree. The **myelencephalon** (here) is **one subdivision** of that
system — the **caudal medullary** subdivision. Consumers must
**not** conflate the **myelencephalon** with the **whole brainstem**
— the brainstem is a **functional/anatomical system** assembled
from **multiple tree containers**.
**Boundary status (NOT the spinal cord — transition at the foramen
magnum):** **Boundary case — the myelencephalon is NOT the spinal
cord; the spinal cord is a separate container.** The **spinal
cord** (``.../spinal_cord/``) begins **caudal to the foramen
magnum**, where the **medulla oblongata** transitions into the
**cervical spinal cord**. The **myelencephalon** (here) is the
**medullary** subdivision — its **caudal boundary** is the
**foramen magnum** / **spinomedullary junction**. Consumers must
**not** conflate the **myelencephalon** with the **spinal cord** —
they are **adjacent but distinct** containers.
**Boundary status (NOT the fourth ventricle — that is wired under
the metencephalon):** **Boundary case — the myelencephalon is NOT
the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is a **CSF cavity**
wired under the **metencephalon** — its **caudal portion** lies
between the **medulla** and the **cerebellum**, but the tree places
the **whole ventricle** under the **metencephalon**. The
**myelencephalon** (here) is the **medullary parenchyma container**
— it **does not** contain the fourth ventricle as a structural
child. Consumers must **not** expect to find the fourth ventricle
under the myelencephalon; resolve it via the metencephalon.
**Boundary status (NOT the reticular formation — a cross-container
system):** **Boundary case — the myelencephalon is NOT the reticular
formation; the reticular formation spans midbrain, pons, and
medulla.** The **reticular formation** is a **distributed
system** with components in the **midbrain tegmentum**, the
**pontine tegmentum**, and the **medullary reticular nuclei**
(e.g., **gigantocellular reticular nucleus**, **paramedian
reticular nucleus**, **ventral respiratory group**). The tree
wires the **medullary reticular components** under
``.../medulla_oblongata/respiratory_center/`` and
``.../medulla_oblongata/paramedian_reticular_nucleus/`` — the
**myelencephalon** (here) is the **container** for those medullary
components, **not** the reticular formation as a whole. Consumers
must **not** conflate the **myelencephalon** with the **reticular
formation**.
**Boundary status (NOT a single functional system — multiple
nuclei and tracts):** **Boundary case — the myelencephalon is a
CONTAINER, not a single functional system.** Its child
(``medulla_oblongata``) contains **multiple functionally distinct
nuclei and tracts** — **cranial nerve nuclei** (IX–XII),
**respiratory centers**, **cardiovascular centers**, the **olivary
complex**, the **dorsal column nuclei** (gracile, cuneate), the
**pyramids**, the **medial lemniscus**, the **spinothalamic
tract**, etc. Consumers must **not** treat the myelencephalon as
a single uniform structure — it is a **container** for a
**heterogeneous medullary subdivision**.

Overview
--------
The myelencephalon is the **caudal subdivision of the hindbrain**
and the **developmental container** for the **medulla oblongata**.
It is the **single-child container** of the hindbrain tree — the
**embryological vesicle** that **becomes** the adult medulla. Its
sole structural child is ``medulla_oblongata``.

**The myelencephalon is the CONTAINER, the medulla oblongata is the
STRUCTURE.** The **medulla oblongata** is the **adult anatomical
structure** — the nuclei, tracts, and centers that occupy the
caudal brainstem. The **myelencephalon** (here) is the
**developmental subdivision** that **contains** it. Consumers that
need **nucleus-level** resolution (e.g., **hypoglossal nucleus**,
**inferior olivary nucleus**, **dorsal respiratory group**) must
descend into ``medulla_oblongata`` — the myelencephalon itself has
**no children other than** the medulla.

**The myelencephalon is the CAUDAL hindbrain subdivision.** The
**rostral** hindbrain subdivision is the **metencephalon**
(pons + cerebellum + fourth ventricle). The **caudal** subdivision
is the **myelencephalon** (medulla oblongata). The boundary between
them is the **pontomedullary junction**. Consumers must **not**
conflate the two subdivisions.

**The myelencephalon is NOT the brainstem.** The brainstem is a
**cross-container system** (midbrain + pons + medulla) — it spans
**three tree containers**. The myelencephalon is **one** of those
subdivisions (the caudal medullary one).

**The myelencephalon is NOT the spinal cord.** The transition is at
the **foramen magnum** / **spinomedullary junction**. The spinal
cord is a **separate container** (``.../spinal_cord/``) wired under
``.../`` (the brainparts root), not under the myelencephalon.

**The myelencephalon is a container, NOT a leaf.** Unlike the
``frontotemporal_cortical_system`` (a leaf with prose subregions),
the myelencephalon **has a structural child** — ``medulla_oblongata``
— and consumers **should** descend into it to reach the medullary
nuclei and tracts.

Structural Child Composition
-----------------------------
The myelencephalon has **exactly one structural child**:

*   **Medulla oblongata** (``.../myelencephalon/medulla_oblongata/``)
    — the **adult medullary structure**. Contains (as *its* structural
    children, documented in the medulla's own module):
    *   **Arcuate nucleus**
    *   **Caudal ventrolateral medulla**
    *   **Cranial nerve nuclei** (dorsal motor nucleus of vagus,
        hypoglossal nucleus, inferior salivatory nucleus, nucleus
        ambiguus — each bilaterally wired)
    *   **Medullary pyramid**
    *   **Olivary body** (with inferior olivary nucleus)
    *   **Parafacial zone**
    *   **Paramedian reticular nucleus**
    *   **Perihypoglossal nuclei** (intercalated nucleus, prepositus
        nucleus)
    *   **Respiratory center** (area postrema, chemoreceptor trigger
        zone, cuneate nucleus, dorsal respiratory group,
        gigantocellular reticular nucleus, gracile nucleus)
    *   **Rostral ventrolateral medulla**
    *   **Solitary nucleus**
    *   **Ventral respiratory group** (Bötzinger complex, nucleus
        para-ambiguus, nucleus retroambiguus, nucleus retrofacialis,
        pre-Bötzinger complex, retrotrapezoid nucleus)

**Consumers should descend into** ``medulla_oblongata`` **for all
nucleus-level and tract-level resolution.** The myelencephalon
itself is a **thin container** — do not expect medullary nuclei to
be wired directly under it.

The Myelencephalon / Metencephalon Boundary
-------------------------------------------
This is the **rostral–caudal hindbrain** boundary:

*   **Myelencephalon** (this module) — the **caudal** hindbrain
    subdivision (medulla oblongata).

*   **Metencephalon** (``.../metencephalon/``) — the **rostral**
    hindbrain subdivision (pons + cerebellum + fourth ventricle).

**The boundary is the pontomedullary junction.** The
**myelencephalon** is **caudal** (medullary); the
**metencephalon** is **rostral** (pontine/cerebellar). Consumers
must **not** conflate the two — they are **sibling subdivisions**
of the hindbrain.

The Myelencephalon / Hindbrain Boundary
---------------------------------------
This is the **subdivision / parent** boundary:

*   **Myelencephalon** (this module) — a **subdivision** of the
    hindbrain.

*   **Hindbrain** (``.../hindbrain/``) — the **parent container**
    (rhombencephalon), containing both the **metencephalon** and
    the **myelencephalon**.

**The myelencephalon is a CHILD of the hindbrain, not the hindbrain
itself.** Consumers must **not** conflate the **subdivision** with
its **parent container**.

The Myelencephalon / Medulla Oblongata Boundary
-----------------------------------------------
This is the **container / child** boundary — the **most
consequential** boundary for consumers:

*   **Myelencephalon** (this module) — the **developmental
    container** (the embryological vesicle).

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **adult structure** (nuclei + tracts + centers).

**Descend into the medulla for structure-level resolution.** The
myelencephalon has **no medullary nuclei wired directly under it**
— every nucleus and tract is under ``medulla_oblongata``.
Consumers must **not** expect **hypoglossal nucleus**, **inferior
olivary nucleus**, **dorsal respiratory group**, or **pyramids**
to resolve under the myelencephalon directly — resolve them under
``medulla_oblongata``.

The Myelencephalon / Brainstem Boundary
---------------------------------------
This is the **cross-container system** boundary:

*   **Myelencephalon** (this module) — the **caudal medullary**
    subdivision of the brainstem.

*   **Brainstem** — a **cross-container system** assembled from
    the **midbrain** (``.../midbrain/``), the **pons**
    (``.../metencephalon/pons/``), and the **medulla oblongata**
    (``.../myelencephalon/medulla_oblongata/``).

**The brainstem is not a single tree container.** Consumers must
**not** expect a ``brainstem/`` module — the brainstem is a
**functional system** assembled from **three tree containers**.
The myelencephalon is **one** of those subdivisions.

The Myelencephalon / Spinal Cord Boundary
-----------------------------------------
This is the **spinomedullary** boundary:

*   **Myelencephalon** (this module) — the **medullary** subdivision
    of the brainstem.

*   **Spinal cord** (``.../spinal_cord/``) — a **separate
    container** (grey matter horns, white matter columns, ascending
    and descending tracts).

**The boundary is the foramen magnum / spinomedullary junction.**
The spinal cord is **not** a child of the myelencephalon — it is a
**sibling container** under ``brainparts``. Consumers must **not**
descend from the myelencephalon into the spinal cord; resolve the
spinal cord via its own container.

The Myelencephalon / Fourth Ventricle Boundary
----------------------------------------------
This is the **CSF cavity** boundary:

*   **Myelencephalon** (this module) — the **medullary parenchyma**
    container.

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the **CSF cavity**,
    wired under the **metencephalon**.

**The fourth ventricle is NOT a child of the myelencephalon.**
Although its **caudal portion** lies between the medulla and the
cerebellum, the tree places the **whole ventricle** under the
**metencephalon**. Consumers must **not** expect to find the fourth
ventricle under the myelencephalon — resolve it via
``metencephalon``.

The Myelencephalon / Reticular Formation Boundary
-------------------------------------------------
This is the **distributed system** boundary:

*   **Myelencephalon** (this module) — the **container** for the
    **medullary reticular components** (via
    ``medulla_oblongata/paramedian_reticular_nucleus/`` and
    ``medulla_oblongata/respiratory_center/gigantocellular_reticular_nucleus/``).

*   **Reticular formation** — a **cross-container system** spanning
    the **midbrain tegmentum**, the **pontine tegmentum**, and the
    **medullary reticular nuclei**.

**The reticular formation is not a single tree container.** The
medullary reticular components are wired under the **medulla
oblongata**; the pontine and midbrain components are wired under
their respective containers. Consumers must **not** conflate the
**myelencephalon** with the **whole reticular formation**.

Function in the Human Brain
---------------------------
The myelencephalon's **function** is to **contain and organize**
the **medulla oblongata** — the **caudal brainstem** subdivision
that subserves:

*   **Autonomic homeostasis (medulla oblongata):** The **nucleus
    tractus solitarius**, the **dorsal motor nucleus of the vagus**,
    and the **rostral/caudal ventrolateral medulla** are the
    **autonomic control centers** for **cardiovascular**,
    **respiratory**, and **gastrointestinal** homeostasis.

*   **Respiratory rhythm (medulla oblongata):** The **ventral
    respiratory group** (Bötzinger complex, pre-Bötzinger complex,
    retrotrapezoid nucleus, nucleus para-ambiguus) and the **dorsal
    respiratory group** are the **respiratory rhythm generators**.

*   **Cranial nerve nuclei IX–XII (medulla oblongata):** The
    **glossopharyngeal** (IX), **vagus** (X), **accessory** (XI),
    and **hypoglossal** (XII) nerve nuclei are wired under
    ``medulla_oblongata/cranial_nerve_nuclei/``.

*   **Motor and sensory tracts (medulla oblongata):** The
    **pyramids** (corticospinal tract), the **medial lemniscus**
    (dorsal column pathway), and the **spinothalamic tract** pass
    through the medulla.

*   **NOT a neural processor in the classical sense.** The
    **myelencephalon** is a **developmental container** — it
    **does not itself process** information. The **processing**
    happens in the **medulla oblongata nuclei** (cranial nerve
    nuclei, respiratory centers, autonomic centers). Consumers
    must resolve **functional** detail at the **medulla** level,
    not at the myelencephalon level.

**The unifying theme:** the myelencephalon is the **caudal
hindbrain container** — the **embryological vesicle** that
**becomes** the **medulla oblongata**, which is the **autonomic,
respiratory, and cranial-nerve** control center of the caudal
brainstem.

Associated Disorders
--------------------
The myelencephalon has **no named clinical syndrome** of its own —
its clinical associations are those of the **medulla oblongata**
it contains:

*   **Wallenberg syndrome (Lateral Medullary Syndrome — via the
    medulla oblongata):** Infarction of the **lateral medulla**
    (PICA territory) — **vestibular**, **autonomic**, and
    **cranial nerve** deficits. The **myelencephalon** is the
    **container**; the lesion is in **medulla oblongata**
    structures (solitary nucleus, spinothalamic tract, inferior
    cerebellar peduncle, nucleus ambiguus).

*   **Medial medullary syndrome (Dejerine syndrome — via the
    medulla oblongata):** Infarction of the **medial medulla**
    (anterior spinal artery territory) — **pyramidal**,
    **medial lemniscus**, and **hypoglossal** deficits. The lesion
    is in **medulla oblongata** structures.

*   **Central hypoventilation / Ondine's curse (via the medulla
    oblongata):** Dysfunction of the **respiratory centers** in
    the **ventral respiratory group** (Bötzinger complex,
    retrotrapezoid nucleus). The lesion is in **medulla
    oblongata** structures.

*   **Bulbar palsy (via the medulla oblongata):** Dysfunction of
    the **cranial nerve nuclei IX–XII** — **dysphagia**,
    **dysarthria**, **tongue weakness**. The lesion is in **medulla
    oblongata** structures.

*   **Neurogenic hypertension (via the medulla oblongata):**
    Dysfunction of the **rostral ventrolateral medulla** and the
    **nucleus tractus solitarius** — **sympathetic overactivity**.
    The lesion is in **medulla oblongata** structures.

*   **No Named "Myelencephalon Syndrome":** The myelencephalon is a
    **developmental container**, not a **single structure** — it has
    **no named clinical syndrome**. Its clinical relevance is
    **the clinical relevance of the medulla oblongata** it
    contains.

**What is NOT here:** The myelencephalon is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala), **fear conditioning**
(amygdala — central + basolateral nuclei), **Parkinson's disease**
(substantia nigra — midbrain), **Huntington's disease** (striatum
— basal ganglia), or **Alzheimer's disease** (hippocampus, nucleus
basalis). Its clinical relevance is **the medullary clinical
relevance** it contains.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The myelencephalon is a
    **container**; it does **not** import from ``left/`` or
    ``right/`` containers — bilateral wiring happens **inside**
    ``medulla_oblongata``'s own children.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../metencephalon/``, ``.../midbrain/``, ``.../spinal_cord/``,
    or any other container. The myelencephalon's relationships to
    the metencephalon, the hindbrain, the brainstem, the spinal
    cord, the fourth ventricle, and the reticular formation are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Single-child container.** The **only** structural child is
    ``medulla_oblongata``. Consumers must **not** expect medullary
    nuclei to be wired directly under the myelencephalon — descend
    into ``medulla_oblongata``.
*   **NOT the hindbrain.** The myelencephalon is a **subdivision**,
    not the parent container. The parent is ``.../hindbrain/``.
*   **NOT the metencephalon.** The metencephalon (pons +
    cerebellum + fourth ventricle) is the **rostral** sibling
    subdivision. Consumers must **not** conflate the two.
*   **NOT the medulla oblongata.** The medulla oblongata is the
    **structural child** — the adult structure. The myelencephalon
    is the **developmental container**.
*   **NOT the brainstem.** The brainstem is a **cross-container
    system** (midbrain + pons + medulla). Consumers must **not**
    expect a single ``brainstem/`` module.
*   **NOT the spinal cord.** The spinal cord is a **separate
    container** (``.../spinal_cord/``). The transition is the
    **foramen magnum** / **spinomedullary junction**.
*   **NOT the fourth ventricle.** The fourth ventricle is wired
    under the **metencephalon**. Consumers must **not** expect it
    under the myelencephalon.
*   **NOT the reticular formation.** The reticular formation is a
    **cross-container system** (midbrain + pons + medulla).
*   **No ``AREA_PATHS`` hop.** The myelencephalon is a **local
    container**, not a cross-listed leaf.
*   **No nested cross-listing.** The myelencephalon has no nested
    dual-framing module. It is a **single container** with a
    **single structural child**.
*   **Structural parity with the right side — N/A.** The
    myelencephalon is an **unpaired midline container** (like the
    hindbrain and the metencephalon). Bilateralization happens
    **inside** ``medulla_oblongata``'s children (``left/`` and
    ``right/`` subdirectories), **not** at the myelencephalon level.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain import myelencephalon

Or by fully-qualified path string::

    path = "hindbrain.myelencephalon"

**Do not** assume the myelencephalon contains medullary nuclei
directly. **The myelencephalon has exactly one structural child:**
``medulla_oblongata``. Descend into ``medulla_oblongata`` for
nucleus-level and tract-level resolution.

**Do not** assume the myelencephalon is the **hindbrain**. The
hindbrain (``.../hindbrain/``) is the **parent container**; the
myelencephalon is a **caudal subdivision** of it.

**Do not** assume the myelencephalon is the **metencephalon**. The
metencephalon is the **rostral** sibling subdivision
(pons + cerebellum + fourth ventricle).

**Do not** assume the myelencephalon is the **brainstem**. The
brainstem is a **cross-container system** (midbrain + pons +
medulla). The myelencephalon is **one** of its subdivisions.

**Do not** assume the myelencephalon is the **spinal cord**. The
spinal cord is a **separate container**
(``.../spinal_cord/``), beginning at the **foramen magnum**.

**Do not** assume the myelencephalon contains the **fourth
ventricle**. The fourth ventricle is wired under the
**metencephalon**.

Iterating the myelencephalon's structural children (recommended
consumer pattern)::

    MYELENCEPHALON_CHILDREN = ("medulla_oblongata",)
    # The myelencephalon is a single-child container. Every
    # medullary nucleus and tract resolves under medulla_oblongata.

Reaching the medulla oblongata (recommended consumer pattern —
the child)::

    # The medulla oblongata is the ADULT STRUCTURE — the nuclei,
    # tracts, and centers that occupy the caudal brainstem:
    #
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # The myelencephalon is the DEVELOPMENTAL CONTAINER; the
    # medulla oblongata is the structure it becomes.

Reaching the metencephalon (recommended consumer pattern — the
rostral sibling)::

    # The metencephalon is the ROSTRAL hindbrain subdivision —
    # the pons, the cerebellum, and the fourth ventricle:
    #
    #   hindbrain.metencephalon
    #
    # The boundary between the myelencephalon and the metencephalon
    # is the pontomedullary junction.

Reaching the hindbrain (recommended consumer pattern — the
parent)::

    # The hindbrain (rhombencephalon) is the PARENT container:
    #
    #   hindbrain
    #
    # The myelencephalon is a caudal SUBDIVISION of the hindbrain.

Reaching the brainstem components (recommended consumer pattern —
NOTE the cross-container system)::

    # The brainstem is a CROSS-CONTAINER SYSTEM assembled from:
    #
    #   hindbrain.midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # There is NO single brainstem container. Consumers must
    # assemble the brainstem from these three containers.

Reaching the spinal cord (recommended consumer pattern — NOTE the
separate container)::

    # The spinal cord is a SEPARATE CONTAINER, not a child of the
    # myelencephalon:
    #
    #   spinal_cord
    #
    # The boundary is the foramen magnum / spinomedullary junction.

Reaching the fourth ventricle (recommended consumer pattern —
NOTE it is under the metencephalon)::

    # The fourth ventricle is wired under the METENCEPHALON:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #
    # The myelencephalon does NOT contain the fourth ventricle as
    # a structural child.

References
----------
*   **Canonical developmental anatomy:** Larsen, W.J. (2001).
    *Human Embryology*, 3rd ed. (Myelencephalon and medulla
    oblongata development; rhombencephalic vesicle derivatives.)
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Myelencephalon / medulla oblongata in overview; cranial nerve
    nuclei IX–XII; respiratory and cardiovascular centers.)
*   **Cranial nerve nuclei:** Blessing, W.W. (1997). *The Lower
    Brain Stem and Bodily Homeostasis.* (Medullary autonomic
    nuclei; nucleus tractus solitarius; rostral ventrolateral
    medulla.)
*   **Respiratory rhythm:** Feldman, J.L., Del Negro, C.A. (2006).
    "Looking for inspiration: new perspectives on respiratory
    rhythm." *Nature Reviews Neuroscience* 7:232–242.
    (Bötzinger complex and pre-Bötzinger complex; ventral
    respiratory group.)
*   **Olivary complex:** De Zeeuw, C.I., et al. (1998). "Microcircuitry
    and function of the inferior olive." *Trends in Neurosciences*
    21:391–400. (Inferior olivary nucleus; olivocerebellar
    pathway.)
*   **Dorsal column nuclei:** Tracey, D.J. (2004). "Ascending and
    descending pathways." In: Paxinos, G. (ed.), *The Rat Nervous
    System*, 3rd ed. (Gracile and cuneate nuclei; medial lemniscus.)
*   **Lateral medullary syndrome:** Sacco, R.L., et al. (1993).
    "Lateral medullary infarction: clinical and MRI correlation."
    *Stroke* 24:1981–1987. (Wallenberg syndrome; medullary
    lesion localization.)
*   **Medial medullary syndrome:** Bassetti, C., et al. (1996).
    "Medial medullary stroke: clinical and MRI findings."
    *Neurology* 46:106–110. (Dejerine syndrome; medullary lesion
    localization.)
*   **Central hypoventilation:** Weese-Mayer, D.E., et al. (2010).
    "An official ATS clinical policy statement: congenital central
    hypoventilation syndrome." *American Journal of Respiratory
    and Critical Care Medicine* 181:626–644. (Respiratory center
    dysfunction; medullary localization.)
*   **Neurogenic hypertension:** Guyenet, P.G. (2006). "The
    sympathetic control of blood pressure." *Nature Reviews
    Neuroscience* 7:335–346. (Rostral ventrolateral medulla;
    sympathetic premotor neurons.)
*   **Reticular formation (contrast — cross-container system):**
    Büttner-Ennever, J.A., Horn, A.K.E. (2014). *Olszewski and
    Baxter's Cytoarchitecture of the Human Brainstem*, 3rd ed.
    (Reticular nuclei spanning midbrain, pons, and medulla.)
*   **Brainstem (contrast — cross-container system):** Paxinos, G.,
    Huang, X.-F. (2013). *The Behaving Human Brain: A
    Cytoarchitectural Atlas.* (Brainstem as a functional system
    spanning midbrain, pons, and medulla.)
*   **Fourth ventricle (contrast — wired under the metencephalon):**
    Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Fourth ventricle; caudal portion between
    medulla and cerebellum.)
*   NeuroNames — Myelencephalon; FMA — Myelencephalon.
"""