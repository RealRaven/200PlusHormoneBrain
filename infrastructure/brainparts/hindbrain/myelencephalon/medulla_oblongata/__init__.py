"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata
=====================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata   <-- THIS MODULE

**Primary synonym:** Medulla oblongata; bulb; bulbus; myelencephalon
(adult); caudal brainstem.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**brainstem subdivision** — the **adult medullary structure** of the
**myelencephalon**. It comprises **multiple grey-matter nuclei**
(cranial nerve nuclei IX–XII, olivary complex, respiratory centers,
cardiovascular centers, dorsal column nuclei, reticular nuclei) and
**white-matter tracts** (pyramids, medial lemniscus, spinothalamic
tract, inferior cerebellar peduncle).
**Part of:** The **myelencephalon** — the caudal subdivision of the
**hindbrain**.
**Structural parent:** ``.../myelencephalon/`` → **direct child** of
the myelencephalon container (and its **only** child).
**Structural children:** **Twelve —** each a bilateral container
whose **left/** and **right/** subdirectories hold the paired
structure:
1. ``arcuate_nucleus`` — hypothalamic-projecting chemosensory
   nucleus.
2. ``caudal_ventrolateral_medulla`` — **CVLM** — sympathoinhibitory
   relay.
3. ``cranial_nerve_nuclei`` — CN IX–XII nuclei (dorsal motor nucleus
   of vagus, hypoglossal nucleus, inferior salivatory nucleus,
   nucleus ambiguus).
4. ``medullary_pyramid`` — corticospinal / corticobulbar tract.
5. ``olivary_body`` — inferior olivary nucleus (olivocerebellar
   climbing fibers).
6. ``parafacial_zone`` — expiratory / retrotrapezoid-adjacent
   region.
7. ``paramedian_reticular_nucleus`` — medullary reticular formation.
8. ``perihypoglossal_nuclei`` — intercalated + prepositus nuclei
   (oculomotor / gaze-holding).
9. ``respiratory_center`` — the respiratory-related medullary nuclei
   container (area postrema, chemoreceptor trigger zone, cuneate
   nucleus, dorsal respiratory group, gigantocellular reticular
   nucleus, gracile nucleus).
10. ``rostral_ventrolateral_medulla`` — **RVLM** — sympathetic
    premotor / vasomotor center.
11. ``solitary_nucleus`` — **NTS** — visceral afferent relay.
12. ``ventral_respiratory_group`` — **VRG** — Bötzinger complex,
    pre-Bötzinger complex, nucleus para-ambiguus, nucleus
    retroambiguus, nucleus retrofacialis, retrotrapezoid nucleus.

**Boundary status (NOT the myelencephalon — that is the parent
container):** **Boundary case — the medulla oblongata is NOT the
myelencephalon; the myelencephalon is the developmental vesicle
that becomes it.** The **myelencephalon** (``.../myelencephalon/``)
is the **embryological container**; the **medulla oblongata**
(here) is the **adult structure** — the nuclei and tracts.
Consumers must **not** conflate the **adult structure** with its
**developmental container**.

**Boundary status (NOT the brainstem — that spans three
containers):** **Boundary case — the medulla oblongata is NOT the
brainstem; the brainstem spans midbrain, pons, and medulla.** The
**brainstem** is a **cross-container functional system** —
midbrain (``.../midbrain/``) + pons
(``.../metencephalon/pons/``) + medulla oblongata (here). The
**medulla oblongata** is the **caudal third** of that system.
Consumers must **not** conflate the **medulla** with the **whole
brainstem** — the brainstem is a **composite** assembled from
**three tree containers**.

**Boundary status (NOT the pons — that is the metencephalon):**
**Boundary case — the medulla oblongata is NOT the pons; the pons
is the rostral brainstem subdivision.** The **pons**
(``.../metencephalon/pons/``) is rostral to the **pontomedullary
junction**. The **medulla oblongata** (here) is caudal to that
junction. They are **different brainstem subdivisions** wired
under **different tree containers** (metencephalon vs.
myelencephalon). Consumers must **not** conflate the two.

**Boundary status (NOT the midbrain — that is the mesencephalon):**
**Boundary case — the medulla oblongata is NOT the midbrain; the
midbrain is the rostral-most brainstem subdivision.** The
**midbrain** (``.../midbrain/``) contains the **tectum**,
**tegmentum** (substantia nigra, red nucleus, VTA, PAG,
oculomotor/trochlear nuclei), and the **cerebral peduncle**. The
**medulla oblongata** (here) is **caudal** to both the midbrain
and the pons. Consumers must **not** conflate the two.

**Boundary status (NOT the spinal cord — that begins at the
foramen magnum):** **Boundary case — the medulla oblongata is NOT
the spinal cord; the spinal cord begins at the foramen magnum.**
The **spinal cord** (``.../spinal_cord/``) is a **separate
container** with **grey-matter horns** and **white-matter
columns**. The **medulla oblongata** (here) transitions into the
**cervical spinal cord** at the **spinomedullary junction**. The
**pyramidal decussation** — where the **corticospinal tract
crosses the midline** — is the **anatomical landmark** of that
transition; it lies at the **caudal medulla**, not in the spinal
cord. Consumers must **not** descend from the medulla oblongata
into the spinal cord; the spinal cord is a **sibling container**.

**Boundary status (NOT the fourth ventricle — that is under the
metencephalon):** **Boundary case — the medulla oblongata is NOT
the fourth ventricle.** The **fourth ventricle**
(``.../metencephalon/fourth_ventricle/``) is a **CSF cavity**
wired under the **metencephalon**. Its **caudal portion** lies
between the **medulla** and the **cerebellum**, and the **medulla
forms part of its floor** (the **rhomboid fossa**, via the **vagal
trigone**, **hypoglossal trigone**, and **area postrema** at the
**calamus scriptorius**). But the tree places the **whole
ventricle** under the **metencephalon** — it is **NOT** a
structural child of the medulla oblongata. Consumers must **not**
expect to find the fourth ventricle under the medulla; resolve it
via ``metencephalon``.

**Boundary status (NOT the reticular formation — that spans three
containers):** **Boundary case — the medulla oblongata is NOT the
reticular formation; the reticular formation spans midbrain, pons,
and medulla.** The **medullary reticular components** are wired
under **this container** (``paramedian_reticular_nucleus`` and
``respiratory_center/gigantocellular_reticular_nucleus``); the
**pontine** and **midbrain** reticular components are wired under
their respective containers. The **medulla** is the **caudal
third** of the reticular formation. Consumers must **not** conflate
the **medulla** with the **whole reticular formation**.

**Boundary status (NOT the cerebellum — that is under the
metencephalon):** **Boundary case — the medulla oblongata is NOT
the cerebellum.** The **cerebellum**
(``.../metencephalon/cerebellum/``) is a **separate structure**
wired under the **metencephalon**. The **medulla** and the
**cerebellum** are connected by the **inferior cerebellar
peduncle** (restiform body + juxtarestiform body), which carries
**olivocerebellar** and **spinocerebellar** fibers. That peduncle
is **part of the medullary anatomy**, but the **cerebellum** is
**not**. Consumers must **not** conflate the two.

**Boundary status (NOT a single functional system — multiple
nuclei and tracts):** **Boundary case — the medulla oblongata is a
HETEROGENEOUS structure with MULTIPLE nuclei and tracts and
MULTIPLE functions.** It contains:
*   **Autonomic** nuclei — NTS, dorsal motor nucleus of vagus, RVLM,
    CVLM.
*   **Respiratory** nuclei — VRG (Bötzinger, pre-Bötzinger,
    retrotrapezoid), DRG, nucleus para-ambiguus, nucleus
    retroambiguus.
*   **Cranial nerve** nuclei — IX, X, XI, XII (the motor and
    parasympathetic columns of the medulla).
*   **Somatosensory** nuclei — gracile, cuneate (dorsal column
    relays).
*   **Motor** tracts — pyramids (corticospinal, corticobulbar).
*   **Sensory** tracts — medial lemniscus, spinothalamic tract.
*   **Cerebellar** connections — inferior cerebellar peduncle,
    inferior olivary nucleus, arcuate nucleus.
*   **Oculomotor** — perihypoglossal nuclei.
**Each is functionally distinct.** Consumers must **not** treat
the medulla oblongata as a single uniform structure — it is a
**brainstem subdivision** with **many functionally distinct
parts**.

**Boundary status (BILATERAL — left/right inside each child):**
**Boundary case — the medulla oblongata is BILATERAL at the
child level, not at this level.** The medulla oblongata module
itself is an **unpaired midline container** — its **12 structural
children** each have ``left/`` and ``right/`` subdirectories. The
**bilateralization happens INSIDE the children**, not at the
medulla level. Consumers must **not** look for
``medulla_oblongata/left/`` or ``medulla_oblongata/right/`` —
those do not exist. Resolve bilateral structures via
``<child>/left/`` and ``<child>/right/``.

Overview
--------
The medulla oblongata is the **adult medullary structure** of the
**myelencephalon** — the **caudal subdivision of the brainstem**.
It is a **container** for **12 bilateral nuclei/tract containers**
that together subserve **autonomic homeostasis**,
**respiratory rhythm**, **cranial nerve IX–XII function**,
**somatosensory relay** (dorsal columns), **motor conduction**
(pyramids), and **cerebellar climbing-fiber input** (inferior
olive).

**The medulla oblongata is the STRUCTURE, the myelencephalon is the
CONTAINER.** The **myelencephalon** is the developmental vesicle;
the **medulla oblongata** is the adult anatomy. The **medulla** is
the **only child** of the myelencephalon — all medullary nuclei
and tracts resolve **inside** this container.

**The medulla oblongata is BILATERAL at the child level.** Each of
the **12 structural children** is a **bilateral container** with
``left/`` and ``right/`` subdirectories. The **medulla oblongata**
itself is **unpaired** — it is a **midline structure** whose
**components are paired**.

**The medulla oblongata is NOT the brainstem.** The **brainstem**
is the **cross-container system** (midbrain + pons + medulla).
The **medulla** is the **caudal third** of that system, wired
under ``myelencephalon``.

**The medulla oblongata is NOT the spinal cord.** The transition is
at the **foramen magnum** / **spinomedullary junction**, marked
rostrally by the **pyramidal decussation**. The **spinal cord** is
a **sibling container** under ``brainparts``.

**The medulla oblongata is a container with 12 structural
children, NOT a leaf.** Unlike the
``frontotemporal_cortical_system`` (a leaf with prose subregions),
the medulla oblongata **has 12 structural children** — consumers
**should** descend into them for nucleus-level and tract-level
resolution.

Structural Child Composition
-----------------------------
The medulla oblongata has **12 structural children**, each a
**bilateral container** with ``left/`` and ``right/``:

*   **Autonomic / homeostatic**
    *   ``solitary_nucleus`` — **NTS** — the **visceral afferent
        relay** (taste, baroreceptor, chemoreceptor, gastrointestinal
        afferents); projects to the **parabrachial nucleus** and
        the **autonomic premotor** centers.
    *   ``rostral_ventrolateral_medulla`` — **RVLM** — the
        **sympathetic premotor / vasomotor center**; the **tonic
        excitatory drive** to the **intermediolateral cell column**
        of the spinal cord.
    *   ``caudal_ventrolateral_medulla`` — **CVLM** — the
        **sympathoinhibitory relay**; receives **NTS** input and
        **inhibits the RVLM**.
    *   ``arcuate_nucleus`` — hypothalamic-projecting
        **chemosensory** nucleus at the **ventral medullary
        surface**.

*   **Respiratory**
    *   ``respiratory_center`` — container for **area postrema**
        (chemoreceptor trigger zone), **chemoreceptor trigger
        zone**, **cuneate nucleus**, **dorsal respiratory group**
        (**DRG** — nucleus tractus solitarius region), **gigantocellular
        reticular nucleus**, and **gracile nucleus**. Note: the
        tree groups the **dorsal column nuclei** (cuneate, gracile)
        under the respiratory container — anatomically unusual but
        this is the **wiring**, not a claim about function.
    *   ``ventral_respiratory_group`` — **VRG** — the **respiratory
        rhythm generator**; contains the **Bötzinger complex**
        (expiratory), **pre-Bötzinger complex** (inspiratory
        rhythm), **nucleus para-ambiguus** (expiratory premotor),
        **nucleus retroambiguus** (expiratory / abdominal),
        **nucleus retrofacialis**, and the **retrotrapezoid
        nucleus** (central chemoreceptor).
    *   ``parafacial_zone`` — the **expiratory / retrotrapezoid-adjacent**
        region.

*   **Cranial nerve nuclei (IX–XII)**
    *   ``cranial_nerve_nuclei`` — container for **dorsal motor
        nucleus of vagus** (X — parasympathetic), **hypoglossal
        nucleus** (XII — tongue motor), **inferior salivatory
        nucleus** (IX — parasympathetic), and **nucleus ambiguus**
        (IX/X/XI — branchial motor).

*   **Motor / sensory tracts**
    *   ``medullary_pyramid`` — the **corticospinal** and
        **corticobulbar** tract; the site of the **pyramidal
        decussation** at the **spinomedullary junction**.

*   **Cerebellar**
    *   ``olivary_body`` — contains the **inferior olivary
        nucleus** — the sole source of **climbing fibers** to the
        cerebellum; a major **olivocerebellar** relay.
    *   ``perihypoglossal_nuclei`` — **intercalated nucleus** and
        **prepositus nucleus** — oculomotor / gaze-holding
        structures.

*   **Reticular**
    *   ``paramedian_reticular_nucleus`` — medullary reticular
        formation (the **paramedian** component).

**Consumers should descend into each of the 12 children** for
nucleus-level and tract-level resolution.

The Medulla Oblongata / Myelencephalon Boundary
-----------------------------------------------
This is the **structure / container** boundary:

*   **Medulla oblongata** (this module) — the **adult structure**.

*   **Myelencephalon** (``.../myelencephalon/``) — the
    **developmental container** (the embryological vesicle).

**The medulla oblongata is the ONLY child of the myelencephalon.**
Consumers must **not** conflate the **structure** with its
**developmental container**.

The Medulla Oblongata / Pons and Midbrain Boundary
--------------------------------------------------
This is the **brainstem-subdivision** boundary:

*   **Medulla oblongata** (this module) — the **caudal** brainstem
    subdivision (wired under ``myelencephalon``).

*   **Pons** (``.../metencephalon/pons/``) — the **middle**
    brainstem subdivision.

*   **Midbrain** (``.../midbrain/``) — the **rostral** brainstem
    subdivision.

**The three are DIFFERENT CONTAINERS.** Consumers must **not**
expect a single ``brainstem/`` module — the brainstem is a
**cross-container system** assembled from these three.

The Medulla Oblongata / Spinal Cord Boundary
--------------------------------------------
This is the **spinomedullary** boundary:

*   **Medulla oblongata** (this module) — the **medullary**
    subdivision of the brainstem.

*   **Spinal cord** (``.../spinal_cord/``) — a **separate
    container**.

**The boundary is the foramen magnum / spinomedullary junction**,
marked rostrally by the **pyramidal decussation**. The spinal cord
is **not** a child of the medulla oblongata — it is a **sibling
container** under ``brainparts``.

The Medulla Oblongata / Fourth Ventricle Boundary
-------------------------------------------------
This is the **CSF cavity** boundary:

*   **Medulla oblongata** (this module) — the **medullary
    parenchyma** (nuclei + tracts).

*   **Fourth ventricle**
    (``.../metencephalon/fourth_ventricle/``) — the **CSF cavity**,
    wired under the **metencephalon**.

**The medulla forms part of the fourth ventricle floor** (the
**rhomboid fossa** — the **vagal trigone**, **hypoglossal
trigone**, and **area postrema** at the **calamus scriptorius**),
but the **fourth ventricle** is **NOT** a structural child of the
medulla. Consumers must **not** expect the fourth ventricle under
``medulla_oblongata`` — resolve it via ``metencephalon``.

The Medulla Oblongata / Reticular Formation Boundary
----------------------------------------------------
This is the **distributed system** boundary:

*   **Medulla oblongata** (this module) — the **caudal third** of
    the reticular formation, wired as
    ``paramedian_reticular_nucleus`` and
    ``respiratory_center/gigantocellular_reticular_nucleus``.

*   **Reticular formation** — a **cross-container system**
    spanning **midbrain tegmentum** + **pontine tegmentum** +
    **medullary reticular nuclei**.

**The medullary reticular components are HERE; the pontine and
midbrain components are elsewhere.** Consumers must **not**
conflate the medulla oblongata with the **whole reticular
formation**.

The Medulla Oblongata / Cerebellum Boundary
-------------------------------------------
This is the **cerebellar-connection** boundary:

*   **Medulla oblongata** (this module) — the **medullary**
    subdivision (including the **inferior cerebellar peduncle** as
    the **cerebellar connection**).

*   **Cerebellum** (``.../metencephalon/cerebellum/``) — a
    **separate structure** wired under the **metencephalon**.

**The cerebellum is NOT a child of the medulla.** The **inferior
cerebellar peduncle** connects them, but the cerebellum itself is
wired under the metencephalon.

Function in the Human Brain
---------------------------
The medulla oblongata's functions are the **caudal brainstem
functions** — **autonomic homeostasis**, **respiratory rhythm**,
**cranial nerve IX–XII**, **somatosensory relay**, **motor
conduction**, and **cerebellar input**:

*   **Autonomic homeostasis (NTS, RVLM, CVLM, dorsal motor nucleus
    of vagus):** The **solitary nucleus** receives **visceral
    afferents** (baroreceptor, chemoreceptor, gastrointestinal,
    taste); the **RVLM** provides **tonic sympathetic drive** to
    the **intermediolateral cell column**; the **CVLM** provides
    **sympathoinhibitory** feedback; the **dorsal motor nucleus of
    vagus** provides **parasympathetic** outflow to the **viscera**.
    Together these are the **medullary autonomic control centers**.

*   **Respiratory rhythm (VRG, DRG, retrotrapezoid nucleus,
    pre-Bötzinger complex):** The **ventral respiratory group**
    (especially the **pre-Bötzinger complex**) is the **primary
    respiratory rhythm generator**; the **dorsal respiratory group**
    relays **pulmonary stretch** and **chemoreceptor** input; the
    **retrotrapezoid nucleus** is the **central CO₂/H⁺
    chemoreceptor**. The **Bötzinger complex** and **nucleus
    para-ambiguus** are **expiratory premotor** centers.

*   **Cranial nerve IX–XII (cranial_nerve_nuclei):** The **nucleus
    ambiguus** (branchial motor to pharynx/larynx), the **dorsal
    motor nucleus of vagus** (parasympathetic to thoracic/abdominal
    viscera), the **hypoglossal nucleus** (tongue motor), and the
    **inferior salivatory nucleus** (parasympathetic to parotid) are
    the **medullary cranial nerve nuclei**.

*   **Somatosensory relay (gracile, cuneate nuclei):** The
    **gracile** and **cuneate** nuclei are the **first central
    relays** of the **dorsal column–medial lemniscus pathway**
    (fine touch, vibration, proprioception from the body). Their
    axons **decussate** as the **internal arcuate fibers** and
    ascend as the **medial lemniscus**.

*   **Motor conduction (medullary_pyramid):** The **pyramids**
    carry the **corticospinal** and **corticobulbar** tracts; the
    **pyramidal decussation** at the **spinomedullary junction**
    crosses ~85–90% of corticospinal fibers to form the **lateral
    corticospinal tract**.

*   **Cerebellar climbing-fiber input (olivary_body):** The
    **inferior olivary nucleus** is the **sole source** of
    **climbing fibers** to the cerebellar cortex — a critical
    **error signal** for cerebellar learning.

*   **Oculomotor / gaze-holding (perihypoglossal_nuclei):** The
    **prepositus nucleus** and **intercalated nucleus** are
    **gaze-holding** and **oculomotor** structures in the
    perihypoglossal region.

*   **NOT a single neural processor.** The medulla oblongata is a
    **container** for **many functionally distinct nuclei and
    tracts**. The **processing** happens **inside each child**.

**The unifying theme:** the medulla oblongata is the **caudal
brainstem control center** — **autonomic**, **respiratory**,
**cranial nerve IX–XII**, **somatosensory relay**, **motor
conduction**, and **cerebellar input** — wired as **12 bilateral
child containers**.

Associated Disorders
--------------------
The medulla oblongata is the **substrate** for a set of
**well-defined clinical syndromes**:

*   **Wallenberg syndrome (Lateral Medullary Syndrome / PICA
    syndrome):** Infarction of the **lateral medulla** (PICA or
    vertebral artery territory) — **ipsilateral facial
    thermoalgesic loss** (spinal trigeminal nucleus/tract),
    **contralateral body thermoalgesic loss** (spinothalamic
    tract), **ipsilateral Horner's syndrome** (descending
    sympathetic fibers), **dysphagia / dysarthria / hoarseness**
    (nucleus ambiguus), **vertigo / nystagmus** (vestibular
    nuclei), and **ipsilateral cerebellar signs** (inferior
    cerebellar peduncle). Wired structures: **solitary_nucleus**,
    **cranial_nerve_nuclei** (nucleus ambiguus), **spinothalamic
    tract** (white matter passing through), **inferior cerebellar
    peduncle** (passing through).

*   **Medial medullary syndrome (Dejerine syndrome / anterior
    spinal artery syndrome):** Infarction of the **medial medulla**
    — **contralateral hemiparesis** (pyramid), **contralateral
    loss of proprioception/vibration** (medial lemniscus), and
    **ipsilateral tongue weakness** (hypoglossal nucleus/nerve).
    Wired structures: **medullary_pyramid**,
    **cranial_nerve_nuclei** (hypoglossal nucleus), medial
    lemniscus (passing through).

*   **Central hypoventilation syndrome (Ondine's curse / CCHS):**
    Dysfunction of the **respiratory rhythm generators** and
    **central chemoreceptors** — **pre-Bötzinger complex**,
    **retrotrapezoid nucleus**, **Bötzinger complex**. Wired
    structures: **ventral_respiratory_group**,
    **respiratory_center** (DRG).

*   **Neurogenic hypertension:** Overactivity of the **RVLM** and
    impaired **CVLM** / **NTS** feedback — **sympathetic
    overactivity**. Wired structures:
    **rostral_ventrolateral_medulla**,
    **caudal_ventrolateral_medulla**, **solitary_nucleus**.

*   **Bulbar palsy:** Dysfunction of the **cranial nerve nuclei
    IX–XII** — **dysphagia**, **dysarthria**, **tongue
    weakness**, **palatal weakness**. Wired structures:
    **cranial_nerve_nuclei**.

*   **Area postrema syndrome (chemoreceptor trigger zone):**
    **Nausea** and **vomiting** from **chemotherapy**, **toxins**,
    or **demyelinating lesions** (e.g., **neuromyelitis optica**).
    Wired structure: **respiratory_center/area_postrema** and
    **respiratory_center/chemoreceptor_trigger_zone**.

*   **Palatal myoclonus (palatal tremor):** Disruption of the
    **Guillain–Mollaret triangle** — **dentate nucleus** →
    **inferior olivary nucleus** → **cerebellar cortex**.
    Wired structures: **olivary_body** (inferior olivary
    nucleus).

*   **Lateral medullary / olivary hypertrophy:** **Hypertrophic
    olivary degeneration** — a **transsynaptic** degeneration of
    the **inferior olivary nucleus** after a lesion in the
    **dentato-rubro-olivary** pathway. Wired structure:
    **olivary_body**.

*   **Dorsal column / medial lemniscus deficits:** **Loss of
    proprioception, vibration, and fine touch** from the body —
    from lesions in the **gracile** and **cuneate** nuclei or the
    **medial lemniscus**. Wired structures:
    **respiratory_center/gracile_nucleus**,
    **respiratory_center/cuneate_nucleus** (note the wiring:
    these are grouped under ``respiratory_center`` in the tree).

**What is NOT here:** The medulla oblongata is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala), **fear
conditioning** (amygdala), **Parkinson's disease** (substantia
nigra — midbrain), **Huntington's disease** (striatum — basal
ganglia), or **Alzheimer's disease** (hippocampus, nucleus
basalis). Its clinical relevance is the **medullary syndromes
listed above**.

Lateralization Notes
--------------------
The medulla oblongata is an **unpaired midline container** — its
**12 structural children** each have ``left/`` and ``right/``
subdirectories. There is **NO**
``medulla_oblongata/left/`` or ``medulla_oblongata/right/`` at this
level. Consumers must resolve **bilateral structures** via
``<child>/left/`` and ``<child>/right/``.

*   **Bilateral at the child level:** Each of the 12 children
    (``arcuate_nucleus``, ``caudal_ventrolateral_medulla``,
    ``cranial_nerve_nuclei``, ``medullary_pyramid``,
    ``olivary_body``, ``parafacial_zone``,
    ``paramedian_reticular_nucleus``, ``perihypoglossal_nuclei``,
    ``respiratory_center``, ``rostral_ventrolateral_medulla``,
    ``solitary_nucleus``, ``ventral_respiratory_group``) has
    ``left/`` and ``right/`` subdirectories. **The
    bilateralization is at the child level, not at the medulla
    level.**

*   **Contralateral motor control:** The **pyramidal decussation**
    at the **spinomedullary junction** crosses ~85–90% of
    corticospinal fibers, so each **medullary pyramid** controls
    the **contralateral** body. The **hypoglossal nucleus**
    (except genioglossus) is innervated **contralaterally** by the
    **corticobulbar** tract. This is a **functional**
    contralaterality — the **medulla itself** is structurally
    **symmetric**.

*   **Ipsilateral sensory for the face:** The **spinal trigeminal
    nucleus/tract** carries **ipsilateral** facial
    thermoalgesic sensation — relevant to **Wallenberg
    syndrome**, where facial sensory loss is **ipsilateral** while
    body sensory loss is **contralateral**.

*   **NO extended-amygdala / fear-output / SLEA warnings:** The
    medulla oblongata is **not** part of the amygdala,
    extended-amygdala, or SLEA continuum. It carries **no SLEA
    warning** and **no fear-output warning**. The **autonomic
    nuclei** (NTS, RVLM, CVLM, DMV) are **visceral** homeostatic
    structures, not fear-output structures.

*   **NO amygdala-lateralization warning:** The **right-amygdala
    fear association** belongs to the **amygdala module**, not the
    medulla oblongata.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The medulla oblongata is a
    **midline container** — it does **not** import from ``left/``
    or ``right/``. Bilateral wiring happens **inside** each
    child's own ``left/`` and ``right/`` subdirectories.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../metencephalon/``, ``.../midbrain/``, ``.../spinal_cord/``,
    or any other container. The medulla's relationships to the
    pons, midbrain, spinal cord, fourth ventricle, cerebellum,
    and reticular formation are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container with 12 structural children.** The 12 children are
    documented above and wired as **structural children**. Unlike
    a **leaf** module, consumers **should** descend into them for
    nucleus-level and tract-level resolution.
*   **Bilateral at the child level.** Each of the 12 children has
    ``left/`` and ``right/`` subdirectories. The medulla itself
    has **no** ``left/`` or ``right/``.
*   **NOT the myelencephalon.** The myelencephalon is the
    **developmental container**; the medulla is the **adult
    structure**.
*   **NOT the brainstem.** The brainstem is a **cross-container
    system** (midbrain + pons + medulla). Consumers must **not**
    expect a single ``brainstem/`` module.
*   **NOT the pons or the midbrain.** The pons is under
    ``metencephalon``; the midbrain is under ``.../midbrain/``.
    Consumers must **not** conflate them with the medulla.
*   **NOT the spinal cord.** The spinal cord is a **separate
    container**; the transition is the **foramen magnum** /
    **spinomedullary junction** (marked by the **pyramidal
    decussation**).
*   **NOT the fourth ventricle.** The fourth ventricle is wired
    under the **metencephalon**; the medulla forms **part of its
    floor** (rhomboid fossa) but **does not contain it**.
*   **NOT the reticular formation.** The reticular formation is a
    **cross-container system**; the medullary components are here,
    the pontine and midbrain components are elsewhere.
*   **NOT the cerebellum.** The cerebellum is under the
    **metencephalon**; the **inferior cerebellar peduncle** is the
    connection, not the cerebellum itself.
*   **No ``AREA_PATHS`` hop.** The medulla oblongata is a **local
    container**, not a cross-listed leaf.
*   **No nested cross-listing.** The medulla oblongata has no
    nested dual-framing module. It is a **single container** with
    **12 structural children**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon import medulla_oblongata

Or by fully-qualified path string::

    path = "hindbrain.myelencephalon.medulla_oblongata"

**Do not** assume the medulla oblongata has ``left/`` and
``right/`` subdirectories. **Bilateralization is at the child
level** — each of the 12 children has ``left/`` and ``right/``.
Resolve bilateral structures via ``<child>/left/`` and
``<child>/right/``.

**Do not** assume the medulla oblongata is the **myelencephalon**.
The myelencephalon is the **developmental container**; the medulla
is the **adult structure**.

**Do not** assume the medulla oblongata is the **brainstem**. The
brainstem is a **cross-container system** (midbrain + pons +
medulla).

**Do not** assume the medulla oblongata is the **pons**, the
**midbrain**, or the **spinal cord**. Each is a **different
container** (pons under ``metencephalon``; midbrain under
``.../midbrain/``; spinal cord under ``.../spinal_cord/``).

**Do not** assume the medulla oblongata contains the **fourth
ventricle**. The fourth ventricle is wired under the
**metencephalon** — the medulla forms **part of its floor**.

**Do not** assume the medulla oblongata contains the
**cerebellum**. The cerebellum is wired under the
**metencephalon**; the **inferior cerebellar peduncle** is the
connection.

Iterating the medulla oblongata's structural children (recommended
consumer pattern)::

    MEDULLA_OBLONGATA_CHILDREN = (
        "arcuate_nucleus",
        "caudal_ventrolateral_medulla",
        "cranial_nerve_nuclei",
        "medullary_pyramid",
        "olivary_body",
        "parafacial_zone",
        "paramedian_reticular_nucleus",
        "perihypoglossal_nuclei",
        "respiratory_center",
        "rostral_ventrolateral_medulla",
        "solitary_nucleus",
        "ventral_respiratory_group",
    )
    # Each child has left/ and right/ subdirectories.

Reaching the autonomic nuclei (recommended consumer pattern)::

    # The autonomic control centers are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.solitary_nucleus
    #   hindbrain.myelencephalon.medulla_oblongata.rostral_ventrolateral_medulla
    #   hindbrain.myelencephalon.medulla_oblongata.caudal_ventrolateral_medulla
    #
    # Each has left/ and right/ subdirectories.

Reaching the respiratory nuclei (recommended consumer pattern)::

    # The respiratory centers are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.ventral_respiratory_group
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center
    #   hindbrain.myelencephalon.medulla_oblongata.parafacial_zone
    #
    # Each has left/ and right/ subdirectories.

Reaching the cranial nerve nuclei IX–XII (recommended consumer
pattern)::

    # The medullary cranial nerve nuclei are under:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.cranial_nerve_nuclei.{left,right}
    #
    # The four nuclei are:
    #   dorsal_motor_nucleus_vagus    (X — parasympathetic)
    #   hypoglossal_nucleus           (XII — tongue motor)
    #   inferior_salivatory_nucleus   (IX — parasympathetic)
    #   nucleus_ambiguus              (IX/X/XI — branchial motor)

Reaching the olivary complex (recommended consumer pattern)::

    # The inferior olivary nucleus is under:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.olivary_body.{left,right}.inferior_olivary_nucleus
    #
    # The inferior olive is the SOLE source of climbing fibers to
    # the cerebellar cortex.

Reaching the pyramidal decussation (recommended consumer
pattern)::

    # The medullary pyramid is:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.medullary_pyramid.{left,right}
    #
    # The pyramidal decussation lies at the SPINOMEDULLARY
    # JUNCTION (the caudal boundary of the medulla). It is not a
    # separate container — it is the anatomical landmark at the
    # medulla/spinal_cord transition.

Reaching the brainstem components (recommended consumer pattern —
NOTE the cross-container system)::

    # The brainstem is a CROSS-CONTAINER SYSTEM assembled from:
    #
    #   hindbrain.midbrain
    #   hindbrain.metencephalon.pons
    #   hindbrain.myelencephalon.medulla_oblongata
    #
    # There is NO single brainstem container.

Reaching the spinal cord (recommended consumer pattern — NOTE the
separate container)::

    # The spinal cord is a SEPARATE CONTAINER, not a child of the
    # medulla oblongata:
    #
    #   spinal_cord
    #
    # The boundary is the foramen magnum / spinomedullary junction.

Reaching the fourth ventricle and cerebellum (recommended consumer
pattern — NOTE they are under the metencephalon)::

    # The fourth ventricle and cerebellum are wired under the
    # METENCEPHALON:
    #
    #   hindbrain.metencephalon.fourth_ventricle
    #   hindbrain.metencephalon.cerebellum
    #
    # The medulla forms part of the fourth ventricle floor
    # (rhomboid fossa) and connects to the cerebellum via the
    # inferior cerebellar peduncle, but neither is a child of the
    # medulla.

Bilateral iteration (recommended consumer pattern)::

    for child in MEDULLA_OBLONGATA_CHILDREN:
        for side in ("left", "right"):
            path = (
                f"hindbrain.myelencephalon.medulla_oblongata."
                f"{child}.{side}"
            )
            # resolve path through the memory/recall layer

References
----------
*   **Canonical medullary anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Medulla oblongata overview; cranial nerve nuclei IX–XII;
    olivary complex; pyramids; medial lemniscus.)
*   **Brainstem cytoarchitecture:** Paxinos, G., Huang, X.-F.
    (2013). *The Behaving Human Brain: A Cytoarchitectural Atlas.*
    (Medullary nuclei and tracts; rostrocaudal organization.)
*   **Autonomic control:** Blessing, W.W. (1997). *The Lower Brain
    Stem and Bodily Homeostasis.* (NTS, RVLM, CVLM, DMV; autonomic
    premotor organization.)
*   **Respiratory rhythm:** Feldman, J.L., Del Negro, C.A. (2006).
    "Looking for inspiration: new perspectives on respiratory
    rhythm." *Nature Reviews Neuroscience* 7:232–242.
    (Pre-Bötzinger complex; VRG; respiratory rhythm generation.)
*   **Retrotrapezoid nucleus / central chemoreception:** Guyenet,
    P.G., Stornetta, R.L., Bayliss, D.A. (2008). "Central
    respiratory chemoreception: the retrotrapezoid nucleus."
    *Trends in Neurosciences* 31:565–573.
*   **Inferior olive:** De Zeeuw, C.I., et al. (1998).
    "Microcircuitry and function of the inferior olive." *Trends
    in Neurosciences* 21:391–400. (Inferior olivary nucleus;
    climbing fibers; olivocerebellar pathway.)
*   **Dorsal column nuclei:** Tracey, D.J. (2004). "Ascending and
    descending pathways." In: Paxinos, G. (ed.), *The Rat Nervous
    System*, 3rd ed. (Gracile and cuneate nuclei; medial lemniscus;
    internal arcuate fibers.)
*   **Pyramidal decussation:** Nathan, P.W., Smith, M.C., Deacon,
    P. (1990). "The corticospinal tracts in man: course and
    location of fibres within the spinal cord." *Brain*
    113:303–324. (Pyramidal decussation; lateral corticospinal
    tract.)
*   **Lateral medullary syndrome:** Sacco, R.L., et al. (1993).
    "Lateral medullary infarction: clinical and MRI correlation."
    *Stroke* 24:1981–1987. (Wallenberg syndrome; PICA territory.)
*   **Medial medullary syndrome:** Bassetti, C., et al. (1996).
    "Medial medullary stroke: clinical and MRI findings."
    *Neurology* 46:106–110. (Dejerine syndrome; anterior spinal
    artery territory.)
*   **Central hypoventilation:** Weese-Mayer, D.E., et al. (2010).
    "An official ATS clinical policy statement: congenital
    central hypoventilation syndrome." *American Journal of
    Respiratory and Critical Care Medicine* 181:626–644.
*   **Neurogenic hypertension:** Guyenet, P.G. (2006). "The
    sympathetic control of blood pressure." *Nature Reviews
    Neuroscience* 7:335–346. (RVLM; sympathetic premotor neurons.)
*   **Area postrema / chemoreceptor trigger zone:** Miller, A.D.,
    Leslie, R.A. (1994). "The area postrema and vomiting."
    *Frontiers in Neuroendocrinology* 15:301–320.
*   **Hypertrophic olivary degeneration:** Goto, N., Kaneko, M.
    (1981). "Olivary enlargement: chronological and
    morphometric studies." *Acta Neuropathologica* 54:275–282.
    (Guillain–Mollaret triangle; palatal tremor.)
*   **Cerebellar peduncles:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (Inferior
    cerebellar peduncle; restiform body; juxtarestiform body.)
*   **Perihypoglossal nuclei:** Leigh, R.J., Zee, D.S. (2015).
    *The Neurology of Eye Movements*, 5th ed. (Nucleus prepositus
    hypoglossi; gaze-holding; neural integrator.)
*   NeuroNames — Medulla oblongata; FMA — Medulla oblongata.
"""