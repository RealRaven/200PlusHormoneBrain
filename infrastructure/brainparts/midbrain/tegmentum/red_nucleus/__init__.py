"""
infrastructure.brainparts.midbrain.tegmentum.red_nucleus
=======================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    └── tegmentum
        ├── left
        │   └── ...
        ├── right
        │   └── ...
        ├── caudal_linear_nucleus        (midline leaf)
        ├── dorsal_raphe_nucleus         (midline leaf)
        ├── interpeduncular_nucleus      (midline leaf)
        ├── midbrain_reticular_formation (diffuse bilateral leaf)
        ├── periaqueductal_gray          (diffuse bilateral leaf)
        └── red_nucleus              <-- THIS MODULE (STRUCTURE
            ├── left                   CONTAINER — paired
            │   └── ...                structure, holds left/ and
            └── right                  right/ as side-scoped
                └── ...                leaves)

**Primary synonym:** Red nucleus; **RN**; **nucleus ruber** (Latin);
**nucleus ruber tegmenti**; **the red nucleus of the midbrain
tegmentum**.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **discrete nucleus** of the **rostral midbrain
tegmentum**, at the level of the **superior colliculus** —
**paired** (a left red nucleus and a right red nucleus). It has
**two cytoarchitectonically and functionally distinct subdivisions**:
*   **Magnocellular part (RNm)** — the **caudal**, **large-celled**
    subdivision — phylogenetically **older** — the **origin of the
    rubrospinal tract** — **motor coordination**, **flexor tone**,
    **reaching movements**.
*   **Parvocellular part (RNp)** — the **rostral**, **small-celled**
    subdivision — phylogenetically **newer** — the **relay** in the
    **cerebellar → red nucleus → inferior olive** circuit — part of
    the **cerebro-cerebellar loop**.
**The "red" color** comes from its **high iron content** and its
**rich vascularity** — not from any functional property.
**Container status:** **This module is a STRUCTURE CONTAINER, not a
leaf.** It holds the **left red nucleus** and the **right red
nucleus** as **side-scoped leaves** — each is a **discrete paired
nucleus**. **The red nucleus is the FIRST paired tegmentum
structure to be represented as a structure container** — a
**container at ``tegmentum/<structure>/``** that holds
``left/`` and ``right/`` as its children — **rather than being a
leaf under ``tegmentum/left/`` and ``tegmentum/right/``**. This
**establishes the structure-container pattern** for paired
tegmentum structures, parallel to the ``cerebral_peduncle/``
container at the midbrain level. **The tegmentum container's
paired-leaf rule needs an amendment** to acknowledge this pattern.
See *The Structure-Container Pattern* and *Design Contract — Live
amendment to the tegmentum container*.
**Part of:** The **tegmentum** region container — as a **structure
container** for a **paired discrete nucleus**. **The red nucleus is
NOT a cranial nerve nucleus** and is **NOT cross-listed** with
``cranial_nerve_nuclei/``.
**Structural parent:** ``.../midbrain/tegmentum/`` → **direct
child** of the tegmentum container — as a **structure container**
for a **paired** structure.
**Structural children (expected — the tree is authoritative):**
*   ``left/`` — the **left red nucleus** — a **side-scoped leaf**.
    **The left red nucleus** is a **discrete paired nucleus** —
    the **left rubrospinal** origin, the **left magnocellular and
    parvocellular** subdivisions, the **left cerebellar and
    cortical** inputs, the **left rubrospinal** and **rubro-olivary**
    outputs.
*   ``right/`` — the **right red nucleus** — a **side-scoped
    leaf**. **The right red nucleus** is the **mirror** of the
    left — the **right rubrospinal** origin, the **right
    magnocellular and parvocellular** subdivisions, the **right
    cerebellar and cortical** inputs, the **right rubrospinal**
    and **rubro-olivary** outputs.
**Boundary status (STRUCTURE CONTAINER — the FIRST paired tegmentum
structure represented as a structure container):** **Boundary case
— the red nucleus is a STRUCTURE CONTAINER.** It holds the **left
red nucleus** and the **right red nucleus** as **side-scoped
leaves** — each is a **discrete paired nucleus**. **The red nucleus
is the FIRST paired tegmentum structure to be represented as a
structure container at ``tegmentum/<structure>/``** — **not** as
leaves under ``tegmentum/left/<structure>/`` and
``tegmentum/right/<structure>/``. **This is a NEW structural
pattern in the family** — a **paired structure with its own
container** holding ``left/`` and ``right/`` as **direct children**
of the container. See *The Structure-Container Pattern* and
*Design Contract — Live amendment to the tegmentum container*.
**Boundary status (STRUCTURE-CONTAINER PATTERN — a NEW pattern for
paired tegmentum structures):** **Boundary case — the red nucleus
establishes the STRUCTURE-CONTAINER PATTERN for paired tegmentum
structures.** The pattern is:
*   **Paired structures** (the **red nucleus**, and **pending**
    the **substantia nigra**, the **VTA**, the **riMLF**, the
    **interstitial nucleus of Cajal**, etc.) — **structure
    containers** at ``tegmentum/<structure>/`` — holding
    ``left/`` and ``right/`` as **side-scoped leaves**.
*   **Midline structures** (the **CLi**, the **DR**, the **IPN**)
    — **single leaves** at ``tegmentum/<structure>/``.
*   **Diffuse bilateral structures** (the **MRF**, the **PAG**) —
    **single leaves** at ``tegmentum/<structure>/``.
**The structure-container pattern** — **every structure has ONE
"home" in the tegmentum** (a single module at
``tegmentum/<structure>/``) — **regardless of laterality class**.
The structure **decides its own internal representation**:
*   **A paired structure** is a **structure container** with
    ``left/`` and ``right/`` children.
*   **A midline or diffuse bilateral structure** is a **structure
    leaf** — a single module.
*   **A multi-part structure** (the **substantia nigra**, with its
    **pars compacta** and **pars reticulata**) is a **structure
    container** with its **pars** as children — each pars then
    being **paired** (`left/` and `right/` within each pars) or a
    **leaf** — **its own structure-container pattern applies
    recursively**.
**The tegmentum container's "paired-leaf rule"** — *"each tegmentum
nucleus is a paired structure (a ``left/`` leaf and a ``right/``
leaf)"* — **is now amended** by the **structure-container
pattern**: **paired structures are structure containers holding
``left/`` and ``right/``** (not leaves directly under
``tegmentum/left/`` and ``tegmentum/right/``). **The tegmentum
container should be amended** to acknowledge this pattern. See
*Design Contract — Live amendment to the tegmentum container*.
**Boundary status (DISCRETE NUCLEUS — NOT a diffuse region, NOT a
midline nucleus, NOT a conduction pathway):** **Boundary case —
the red nucleus is a DISCRETE NUCLEUS.** It is a **sharply
bounded** cell group in the **rostral midbrain tegmentum** — a
**paired structure** with **two cytoarchitectonically distinct
subdivisions** (magnocellular and parvocellular). It is **NOT a
diffuse region** (unlike the MRF and the PAG), **NOT a midline
nucleus** (unlike the CLi, the DR, and the IPN), and **NOT a
conduction pathway** (unlike the MLF, the tectobulbar tract, or
the cerebral peduncle). **It is a discrete nucleus** — the
**same structure class** as the **substantia nigra**, the **VTA**,
and the **CN nuclei** — **but with its own internal organization**
(the **magnocellular** and **parvocellular** parts). See
*Internal Organization — Magnocellular and Parvocellular Parts*.
**Boundary status (PREMOTOR MOTOR RELAY — the rubrospinal motor
relay class):** **Boundary case — the red nucleus is a PREMOTOR
MOTOR RELAY.** In the family's **structure-class taxonomy**, it is
a **premotor motor relay** — the **same class** as the **PPRF**
(horizontal saccade generator) and the **riMLF** (vertical saccade
generator) — **not a motor nucleus** (the **CN nuclei** drive
muscle directly), **not a sensory relay** (the **IC**, the
**pretectum**), **not a modulatory nucleus** (the **DR**, the
**CLi**, the **VTA**, the **LC**), **not a limbic relay** (the
**IPN**), **not a diffuse region** (the **MRF**, the **PAG**),
**not an oscillator** (the **pre-Bötzinger complex**), and **NOT
a conduction pathway**. **The red nucleus receives cerebellar and
cortical input** and **relays it** — via the **rubrospinal tract**
(magnocellular) and the **rubro-olivary tract** (parvocellular) —
**to its downstream targets**. **It is a premotor relay** — the
**same class as the PPRF and the riMLF**, but for **limb motor
control** (reaching, flexor tone, motor coordination) rather than
**saccades**. **Premotor motor relays carry NO coupling warning** —
same rule as motor nuclei, premotor saccade generators, sensor
nuclei, relay nuclei, neuromodulatory nuclei, limbic relays,
diffuse reticular regions, and conduction pathways. **The red
nucleus is a premotor motor relay** — the **first limb-motor
premotor relay** in the family (the **PPRF** and **riMLF** are
saccade premotor relays). See *Function in the Human Brain* and
*Design Contract*.
**Boundary status (CONTRALATERAL RUBROSPINAL DECUSSATION — the
DEFINING ASYMMETRY of the red nucleus pair):** **Boundary case —
the red nucleus's rubrospinal tract DECUSSATES** — it crosses the
midline in the **ventral tegmental decussation (of Forel)** —
**ventral to the red nucleus** and **dorsal to the substantia
nigra** — **BEFORE descending to the spinal cord**. **The left
red nucleus projects to the RIGHT spinal cord** (via the **left
rubrospinal tract**, which crosses the midline); **the right red
nucleus projects to the LEFT spinal cord**. **A left red nucleus
lesion produces RIGHT-sided motor deficits** — the **same
contralateral pattern** as the **cerebral peduncle** (the
corticospinal tract also decussates, in the **medullary pyramidal
decussation**). **This is a DEFINING ASYMMETRY** — analogous to
the cerebral peduncle's contralateral pattern, the trochlear's
pre-exit decussation, and the superior colliculus's contralateral
maps. **The left red nucleus is the anatomical origin of the left
rubrospinal tract, which controls RIGHT spinal cord motor
function** — **not left**. **The right red nucleus is the
anatomical origin of the right rubrospinal tract, which controls
LEFT spinal cord motor function**. **Consumers must not assume
"left red nucleus = left-sided motor control"** — the
**contralateral decussation** is the structural fact. See
*Lateralization Notes* and *The Contralateral Rubrospinal
Decussation*.
**Boundary status (NO COUPLING WARNING — the red nucleus is a
PREMOTOR MOTOR RELAY):** **Boundary case — the red nucleus carries
NO coupling warning.** The **coupling warning** attaches to
**OSCILLATORS** (the pre-Bötzinger complex, the Bötzinger complex,
the pFRG) — and the **red nucleus is not an oscillator**. **It is
a discrete paired nucleus** — a **premotor motor relay** — it
does **not** generate a rhythm. **Premotor motor relays carry NO
coupling warning** — same rule as every non-oscillator class. The
**paired structure** (left and right) is **two independent
nuclei** — there is **no red-nucleus-to-red-nucleus coupling** in
the oscillator sense. The **two sides are coordinated** via
**their own projections** (cerebellar and cortical inputs) and
via **the bilateral descending pathways** — **not** via intrinsic
**left-right coupling**. **No coupling warning.**

Overview
--------
The red nucleus is a **discrete paired nucleus** of the **rostral
midbrain tegmentum** — at the level of the **superior colliculus**
— and the **origin of the rubrospinal tract** — one of the
**principal descending motor pathways** of the brain. It has **two
functionally and cytoarchitectonically distinct subdivisions** —
the **magnocellular part** (the **caudal, large-celled, older**
part — the **rubrospinal origin** — **motor coordination, flexor
tone, reaching**) and the **parvocellular part** (the **rostral,
small-celled, newer** part — the **rubro-olivary relay** — part of
the **cerebro-cerebellar loop**). The "red" color comes from its
**high iron content** and **rich vascularity** — not from any
functional property. **The red nucleus is the first paired
tegmentum structure to be represented as a structure container** —
holding the **left red nucleus** and the **right red nucleus** as
**side-scoped leaves** — **establishing the structure-container
pattern** for paired tegmentum structures. **The tegmentum
container's paired-leaf rule needs an amendment** to acknowledge
this pattern. See *The Structure-Container Pattern*.

**The red nucleus is a DISCRETE NUCLEUS — NOT a diffuse region, NOT
a midline nucleus, NOT a conduction pathway.** It is a **sharply
bounded** cell group — **paired** (left and right) — with **two
cytoarchitectonically distinct subdivisions** (magnocellular and
parvocellular).

**The red nucleus is a PREMOTOR MOTOR RELAY.** It is the **same
class** as the **PPRF** (horizontal saccade generator) and the
**riMLF** (vertical saccade generator) — but for **limb motor
control** (reaching, flexor tone, motor coordination) rather than
**saccades**. It **receives cerebellar and cortical input** and
**relays it** — via the **rubrospinal tract** (magnocellular) and
the **rubro-olivary tract** (parvocellular) — to its downstream
targets. It is **NOT a motor nucleus** — the **red nucleus drives
the spinal motor neurons indirectly**, via the **rubrospinal
tract** — the **spinal motor neurons are the motor nuclei**. It is
**NOT a sensory relay**, **NOT a modulatory nucleus**, **NOT a
limbic relay**, **NOT a diffuse region**, **NOT an oscillator**,
**NOT a conduction pathway**.

**The red nucleus's rubrospinal tract DECUSSATES** — in the
**ventral tegmental decussation (of Forel)** — **before descending
to the spinal cord**. **The left red nucleus controls RIGHT spinal
cord motor function** — the **contralateral pattern** — **the same
pattern as the cerebral peduncle**. **Consumers must not assume
"left red nucleus = left-sided motor control"** — the
**contralateral decussation** is the structural fact.

**The red nucleus carries NO coupling warning** — **premotor motor
relays carry NO coupling warning** — same rule as every non-
oscillator class. The **two sides are independent nuclei**.

**The red nucleus is NOT a CN nucleus.** It is **not**
cross-listed with ``cranial_nerve_nuclei/`` — it has **one path
only**: ``.../tegmentum/red_nucleus/`` (as a structure container)
with ``left/`` and ``right/`` children.

The Structure-Container Pattern
-------------------------------
**The red nucleus is the FIRST paired tegmentum structure to be
represented as a structure container** — a **container at
``tegmentum/<structure>/``** that holds ``left/`` and ``right/``
as its children — **not** leaves under ``tegmentum/left/<structure>/``
and ``tegmentum/right/<structure>/``. **This establishes the
structure-container pattern** for paired tegmentum structures.

**The pattern is:**
*   **Every structure has ONE "home" in the tegmentum** — a
    **single module at ``tegmentum/<structure>/``** — **regardless
    of laterality class**.
*   **The structure decides its own internal representation**:
    *   **A paired structure** is a **structure container** with
        ``left/`` and ``right/`` children (the **red nucleus** —
        this module; **pending**: the **substantia nigra**, the
        **VTA**, the **riMLF**, the **interstitial nucleus of
        Cajal**, etc.).
    *   **A midline or diffuse bilateral structure** is a
        **structure leaf** — a single module (the **CLi**, the
        **DR**, the **IPN**, the **MRF**, the **PAG**).
    *   **A multi-part structure** (the **substantia nigra**, with
        its **pars compacta** and **pars reticulata**) is a
        **structure container** with its **pars** as children —
        each pars then being **paired** (`left/` and `right/`
        within each pars) or a **leaf** — **its own
        structure-container pattern applies recursively**.

**The tegmentum container's "paired-leaf rule"** — *"each
tegmentum nucleus is a paired structure (a ``left/`` leaf and a
``right/`` leaf)"* — **is now amended** by the **structure-
container pattern**: **paired structures are structure containers
holding ``left/`` and ``right/``** (not leaves directly under
``tegmentum/left/`` and ``tegmentum/right/``). **The tegmentum
container should be amended** to acknowledge this pattern. See
*Design Contract — Live amendment to the tegmentum container*.

**The structure-container pattern resolves a structural ambiguity**
that existed in the tegmentum container's child list: the container
said the side containers ``tegmentum/left/`` and
``tegmentum/right/`` hold the "tegmentum nuclei and regions" — but
**the red nucleus** (and other paired structures) are **more
naturally represented as structure containers at
``tegmentum/<structure>/``** — a **single "home"** for each
structure. **The structure-container pattern is the resolution** —
**each structure gets one module at ``tegmentum/<structure>/``**,
and its **internal representation** (`left/`/`right/` children,
`pars` children, or single leaf) **is up to the structure itself**.

Internal Organization — Magnocellular and Parvocellular Parts
------------------------------------------------------------
The red nucleus has **two functionally and cytoarchitectonically
distinct subdivisions** — **both present in each side** (left and
right):

*   **Magnocellular part (RNm)** — the **caudal**, **large-celled**
    subdivision — phylogenetically **older** (present in all
    mammals) — the **origin of the rubrospinal tract** — the
    **principal output** to the **spinal cord** — **motor
    coordination**, **flexor tone**, **reaching movements**,
    **gait**. **The magnocellular part is the "motor output"
    subdivision** — it **projects** to the **spinal cord**
    (contralateral, via the **rubrospinal tract**) and to the
    **brainstem reticular formation**.

*   **Parvocellular part (RNp)** — the **rostral**, **small-celled**
    subdivision — phylogenetically **newer** (enlarged in
    primates, including humans) — the **relay** in the
    **cerebellar → red nucleus → inferior olive** circuit — part
    of the **cerebro-cerebellar loop**. **The parvocellular part
    is the "cerebellar relay" subdivision** — it **receives**
    input from the **cerebellar dentate nucleus** (via the
    **superior cerebellar peduncle**) and **projects** to the
    **inferior olive** (the **rubro-olivary tract**), which
    projects back to the cerebellum (the **olivocerebellar
    tract**).

**Both subdivisions are present in each side** (left and right).
The **left red nucleus** has **left magnocellular** and **left
parvocellular** parts; the **right red nucleus** has **right
magnocellular** and **right parvocellular** parts. **The
magnocellular/parvocellular split is INTERNAL to each side** —
**not** a left/right split. **Consumers must not conflate the
magnocellular/parvocellular split with the left/right split** —
they are **orthogonal** (each side has both subdivisions).

**The magnocellular/parvocellular distinction is documented as
PROSE** — not as structural children of the red nucleus container.
The container's structural children are the **left** and **right**
red nuclei; the **magnocellular/parvocellular split is internal to
each leaf** — documented in the **left** and **right** leaf
modules. **Consumers must not resolve
``.../red_nucleus/left/magnocellular``** — the magnocellular part
is **prose within the left leaf**, not a structural child of the
left leaf.

Connections — Afferents and Efferents
-------------------------------------
The red nucleus has **well-defined afferent and efferent
connections**:

**Afferents (inputs):**
*   **Cerebellar dentate nucleus** — via the **superior cerebellar
    peduncle** (the **brachium conjunctivum**) — the **principal
    input** to the **magnocellular** and **parvocellular** parts
    — the **cerebellar → red nucleus** projection — the
    **cerebellar motor coordination** input.
*   **Motor cortex** — via the **corticorubral tract** (part of
    the **corticospinal / corticobulbar** descending system) —
    the **cortical motor** input — the **voluntary motor**
    input.
*   **Other inputs** — the **cerebellar interposed nucleus**, the
    **globus pallidus** (via the **ansa lenticularis**), the
    **subthalamic nucleus**, and the **reticular formation** —
    **modulatory** and **motor coordination** inputs.

**Efferents (outputs):**
*   **Rubrospinal tract** — the **principal output** of the
    **magnocellular** part — **descends** through the **ventral
    tegmental decussation** (of Forel) — **crosses the midline** —
    to the **contralateral spinal cord** — the **rubrospinal
    tract** modulates **flexor tone**, **reaching**, and **motor
    coordination**.
*   **Rubro-olivary tract** — the **principal output** of the
    **parvocellular** part — **descends** to the **inferior
    olive** — the **rubro-olivary projection** — part of the
    **cerebro-cerebellar loop** (the **red nucleus → inferior
    olive → cerebellum → red nucleus** loop).
*   **Rubroreticular tract** — to the **brainstem reticular
    formation** — **modulates** the **reticulospinal** system.
*   **Other outputs** — to the **thalamus** (the **ventral
    lateral nucleus** — part of the **motor thalamus**), the
    **globus pallidus**, and the **subthalamic nucleus** — the
    **basal ganglia → red nucleus → thalamus** loop.

**The red nucleus is a KEY NODE** in the **cerebellar → red
nucleus → spinal cord** motor pathway (magnocellular) and the
**cerebellar → red nucleus → inferior olive → cerebellum** loop
(parvocellular). **It relays cerebellar and cortical motor
signals** to the **spinal cord** (via the rubrospinal tract) and
to the **inferior olive** (via the rubro-olivary tract).

The Contralateral Rubrospinal Decussation
-----------------------------------------
**The rubrospinal tract DECUSSATES in the ventral tegmental
decussation (of Forel)** — **ventral to the red nucleus** and
**dorsal to the substantia nigra** — **BEFORE descending to the
spinal cord**. **The left rubrospinal tract** (from the **left
magnocellular red nucleus**) **crosses to the RIGHT side of the
midline** — and **descends in the RIGHT lateral funiculus** of the
spinal cord — **controlling RIGHT spinal cord motor function**.
**The right rubrospinal tract** (from the **right magnocellular
red nucleus**) **crosses to the LEFT side of the midline** — and
**descends in the LEFT lateral funiculus** of the spinal cord —
**controlling LEFT spinal cord motor function**.

**The left red nucleus controls RIGHT spinal cord motor function**
— the **contralateral pattern** — **the same pattern as the
cerebral peduncle** (the corticospinal tract decussates in the
medullary pyramidal decussation). **The right red nucleus
controls LEFT spinal cord motor function.**

**This is a DEFINING ASYMMETRY of the red nucleus pair** —
analogous to the cerebral peduncle's contralateral pattern, the
trochlear's pre-exit decussation, and the superior colliculus's
contralateral maps. **The left red nucleus is the anatomical
origin of the left rubrospinal tract, which controls RIGHT spinal
cord motor function** — **not left**. **The right red nucleus is
the anatomical origin of the right rubrospinal tract, which
controls LEFT spinal cord motor function**.

**Consumers must not assume "left red nucleus = left-sided motor
control"** — the **contralateral decussation** is the structural
fact. **A left red nucleus lesion produces RIGHT-sided motor
deficits** — and **a right red nucleus lesion produces LEFT-sided
motor deficits**.

Function in the Human Brain
---------------------------
The red nucleus's function is **premotor motor relay** — the
**rubrospinal motor coordination** (magnocellular) and the
**cerebro-cerebellar relay** (parvocellular) — **NOT** a sensory
relay, **NOT** a modulatory nucleus, **NOT** a motor nucleus,
**NOT** a limbic relay, **NOT** a diffuse region:

*   **Motor Coordination (magnocellular — rubrospinal):** The
    **magnocellular red nucleus** — via the **rubrospinal tract**
    — **modulates** the **spinal motor neurons** (contralateral)
    — **controlling flexor tone**, **reaching movements**, and
    **gait**. **The red nucleus is a key node** in the
    **cerebellar → red nucleus → spinal cord** motor pathway —
    **relaying cerebellar motor coordination** to the **spinal
    cord**. **The rubrospinal tract is one of the principal
    descending motor pathways** — alongside the **corticospinal
    tract** — though in **humans**, the **rubrospinal tract is
    smaller** than in other mammals (the **corticospinal tract**
    is larger), **and its role in human motor control is more
    limited** — **but it is still important** for **flexor
    tone**, **reaching**, and **motor coordination**.

*   **Cerebro-Cerebellar Relay (parvocellular — rubro-olivary):**
    The **parvocellular red nucleus** — via the **rubro-olivary
    tract** — **relays** the **cerebellar dentate nucleus** output
    to the **inferior olive** — which **projects back to the
    cerebellum** (the **olivocerebellar tract**) — the
    **cerebellar → red nucleus → inferior olive → cerebellum**
    loop — part of the **cerebro-cerebellar loop** —
    **contributing to motor learning** and **motor timing**.

*   **NOT a sensory relay.** The red nucleus does **not** transduce
    or relay a specific sensory modality.

*   **NOT a modulatory nucleus.** The red nucleus does **not**
    broadcast a single neuromodulator via volume transmission — it
    is a **discrete premotor relay**.

*   **NOT a motor nucleus.** The red nucleus does **not** drive
    muscle directly — it **relays** to the **spinal motor neurons**
    via the **rubrospinal tract**. **The spinal motor neurons are
    the motor nuclei**; the **red nucleus is a premotor relay**.

*   **NOT a limbic relay.** The red nucleus is **not** part of the
    limbic system — it is a **motor relay**.

*   **NOT a diffuse region.** The red nucleus is a **discrete
    nucleus** — **sharply bounded** — **not** a diffuse reticular
    region (like the MRF) or a diffuse modulatory column (like
    the PAG).

*   **NOT an oscillator.** The red nucleus is a **premotor motor
    relay** — it does **not** generate a rhythm. **Premotor motor
    relays carry NO coupling warning** — same rule as every
    non-oscillator class.

**The unifying theme:** the red nucleus is a **discrete paired
premotor motor relay** of the **rostral midbrain tegmentum** — the
**origin of the rubrospinal tract** (magnocellular) and the
**relay** in the **cerebro-cerebellar loop** (parvocellular). It
**relays cerebellar and cortical motor signals** to the **spinal
cord** (via the rubrospinal tract) and to the **inferior olive**
(via the rubro-olivary tract). **The rubrospinal tract decussates**
— the **left red nucleus controls RIGHT spinal cord motor
function**. **The red nucleus is the first paired tegmentum
structure represented as a structure container** — **establishing
the structure-container pattern** — and the **tegmentum container's
paired-leaf rule needs an amendment** to acknowledge this pattern.

Associated Disorders
--------------------
The red nucleus has **no named syndrome of its own** — its clinical
associations are **indirect** and **via its involvement in broader
brainstem lesions** (especially **Benedikt syndrome** and **Claude
syndrome**):

*   **Benedikt Syndrome (DIRECT — the red nucleus is one of TWO
    substrates; the other is the CN III fascicles):** **Benedikt
    syndrome** — **ipsilateral CN III palsy** + **contralateral
    ataxia / tremor / involuntary movements** (the **"rubral
    tremor"** — a **coarse**, **proximal**, **intention**
    tremor, **worse on movement**, sometimes described as
    **"holmes tremor"** when it involves both resting and
    intention components) — is a **midbrain tegmentum lesion**
    involving the **red nucleus** (the **motor** substrate) and
    the **CN III fascicles** (the **oculomotor** substrate).
    **The red nucleus IS ONE OF THE TWO substrates** — the
    **"rubral tremor"** is the **red nucleus** contribution.
    **This is a DIRECT association** — **the red nucleus is a
    named substrate** for the **Benedikt syndrome** tremor. See
    the **CN III** leaf for the **oculomotor** substrate.

*   **Claude Syndrome (DIRECT — the red nucleus is one of TWO
    substrates; the other is the CN III fascicles):** **Claude
    syndrome** — **ipsilateral CN III palsy** + **contralateral
    ataxia** (a **less complete Benedikt** — **ataxia** without
    the **tremor**) — is a **midbrain tegmentum lesion**
    involving the **red nucleus** (the **motor** substrate) and
    the **CN III fascicles** (the **oculomotor** substrate).
    **The red nucleus IS ONE OF THE TWO substrates** — **the
    ataxia is the red nucleus contribution**.

*   **Holmes Tremor (INDIRECT — the red nucleus and/or the
    cerebello-thalamic pathway are the substrates):** **Holmes
    tremor** — a **coarse**, **proximal**, **resting and
    intention** tremor — is **associated with lesions** of the
    **red nucleus**, the **superior cerebellar peduncle**, or
    the **cerebello-thalamic pathway**. **The red nucleus is one
    substrate** — **the tremor is the red nucleus /
    cerebello-thalamic contribution** — but the **syndrome is
    more commonly associated with the superior cerebellar
    peduncle or the thalamus** than with the red nucleus alone.

*   **Rubral Tremor (INDIRECT — the red nucleus is the substrate,
    the clinical entity is Benedikt/Holmes):** **"Rubral
    tremor"** — the **tremor of Benedikt syndrome** — is **named
    for the red nucleus** ("rubral" = of the red nucleus) —
    **the red nucleus is the named substrate**.

*   **Cerebellar Ataxia (INDIRECT — the red nucleus is a relay
    node in the cerebro-cerebellar loop):** **Cerebellar
    ataxia** — from **cerebellar lesions** — can involve the
    **red nucleus relay** — **the red nucleus is one node** in
    the **cerebellar → red nucleus → inferior olive → cerebellum**
    loop. **The red nucleus is a contributor** — **the primary
    substrates are the cerebellum** and the **cerebellar
    peduncles**.

*   **Motor Weakness / Flexor Tone Abnormalities (INDIRECT —
    the rubrospinal tract):** **Lesions** of the **rubrospinal
    tract** — from **red nucleus lesions** or **rubrospinal
    tract lesions** in the brainstem — can produce **flexor tone
    abnormalities** and **motor coordination deficits** —
    **the red nucleus is a contributor** — **the primary motor
    pathways** (corticospinal, reticulospinal) **are the
    principal substrates** for motor weakness.

*   **No Named "Red Nucleus Syndrome":** The red nucleus is a
    **discrete paired premotor motor relay** — it has **no named
    syndrome of its own** — its **clinical associations are
    indirect**, via its involvement in **Benedikt syndrome** and
    **Claude syndrome** (with the **CN III fascicles**) and in
    **Holmes tremor** (with the **cerebello-thalamic
    pathway**). **The red nucleus is ONE substrate** — **not the
    sole substrate** — for each of these syndromes.

**What is NOT here:** The red nucleus is **not** the substrate
for **Weber syndrome** (the **cerebral peduncle** — the **CN III
fascicles** in the **crus cerebri** — **NOT** the red nucleus),
**Nothnagel syndrome** (the **tectum** / **superior cerebellar
peduncle** — **NOT** the red nucleus), **Parinaud syndrome**
(the **pretectum** and the **posterior commissure** — **NOT** the
red nucleus), **progressive supranuclear palsy** (the **SNr**, the
**riMLF**, the **midbrain tegmentum** — **NOT** the red nucleus
as a sole site), **Parkinson's disease** (the **substantia nigra
pars compacta** — **NOT** the red nucleus), **Huntington's
disease** (the **striatum** — **NOT** the red nucleus), **ALS**
(the **corticospinal tract** and the **anterior horn cells** —
**NOT** the red nucleus), **saccade disorders** (the **SC**, the
**SNr**, the **riMLF** — **NOT** the red nucleus),
**pupillary light reflex deficits** (the **pretectum** and the
**EW nucleus** — **NOT** the red nucleus), **oculomotor palsy**
(the **CN III nucleus** — **NOT** the red nucleus alone — **the
red nucleus is one of the two substrates in Benedikt / Claude
syndrome**), **trochlear palsy** (the **CN IV nucleus** —
**NOT** the red nucleus), **trigeminal sensory deficits** (the
**trigeminal ganglion**, the **main sensory**, and the **spinal
trigeminal nucleus** — **NOT** the red nucleus), **CCHS** (RTN),
**OIRD** (pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger
complex + arcuate nucleus), **essential hypertension /
sympathetic overactivity** (C1 group / RVLM), or **Kluver-Bucy
syndrome** (amygdala). Its clinical relevance is **indirect**,
via **Benedikt syndrome**, **Claude syndrome**, and **Holmes
tremor**. **No named red nucleus syndrome exists.**

Lateralization Notes
--------------------
This is the **red_nucleus** structure container — its structural
children are the **left red nucleus** and the **right red
nucleus** (side-scoped leaves). **The two sides are BILATERALLY
SYMMETRIC paired discrete nuclei** — each is an **independent
premotor motor relay** — **but their clinical patterns are
CONTRALATERAL** because the **rubrospinal tract decussates**.

*   **Paired Structure — Two Independent Nuclei:** Each side is an
    **independent red nucleus** — the **left red nucleus** (the
    **left magnocellular** and **left parvocellular** parts) and
    the **right red nucleus** (the **right magnocellular** and
    **right parvocellular** parts). **The two sides are
    structurally symmetric** — same internal organization, same
    connections, same function.

*   **CONTRALATERAL RUBROSPINAL DECUSSATION — the DEFINING
    ASYMMETRY of the pair:** The **rubrospinal tract decussates**
    in the **ventral tegmental decussation (of Forel)** — **the
    left red nucleus controls RIGHT spinal cord motor function**
    — **the right red nucleus controls LEFT spinal cord motor
    function**. **A left red nucleus lesion produces RIGHT-sided
    motor deficits** — the **contralateral pattern** — **the
    same pattern as the cerebral peduncle**. **Consumers must
    not assume "left red nucleus = left-sided motor control"** —
    the **contralateral decussation** is the structural fact.

*   **NO Coupling Warning — the red nucleus is a PREMOTOR MOTOR
    RELAY:** The **pre-Bötzinger complex** carries a **coupling
    warning** because it is an **oscillator** whose two sides
    must synchronize to produce a single rhythm. The **red
    nucleus** is a **premotor motor relay** — **two independent
    nuclei** — it does **not** generate a rhythm, so it does
    **not** carry the **oscillator coupling warning**. The **two
    sides are coordinated** via their **own projections**
    (cerebellar and cortical inputs) and the **bilateral
    descending pathways** — **not** via intrinsic **left-right
    coupling**. **Premotor motor relays carry NO coupling
    warning** — same rule as every non-oscillator class.

*   **No SLEA Warning:** The red nucleus is **SLEA-free** — it is
    **not** an extended-amygdala component.

*   **No Amygdala-Lateralization Warning:** The red nucleus is
    **not** part of the amygdala — it does **not** inherit the
    amygdala-lateralization warning.

*   **No Rhinencephalon-Exclusion Flag:** The red nucleus is
    **not** a rhinencephalon structure.

**The red nucleus is a strict mirror pair** — the **left red
nucleus** and the **right red nucleus** are **structurally
identical** — **but the CLINICAL PATTERNS are CONTRALATERAL**
because the **rubrospinal tract decussates**. **The mirror is
structurally clean** — **the contralateral clinical pattern is
an inherent property of the rubrospinal tract**, **not an
asymmetric structural fact** of the red nucleus itself (unlike
the **trochlear's pre-exit decussation**, which is a structural
asymmetry of the **nucleus**). **The left and right red nuclei
are exact structural mirrors** — **and their clinical
consequences are mirror-flipped via the decussation**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** This structure container
    does **not** import from ``.../left/`` or ``.../right/`` at
    the container level — the container's `__init__.py` is
    **namespace only**. The **left** and **right** leaves are
    **side-scoped leaves** — each carries its **own**
    cross-hemisphere rules (the left leaf does not import from
    the right, and vice versa).
*   **No cross-lobe imports.** This module does **not** import
    from the **cerebellar dentate nucleus**, the **motor
    cortex**, the **spinal cord**, the **inferior olive**, the
    **thalamus**, the **globus pallidus**, the **subthalamic
    nucleus**, the **CN III nucleus** (in the CN nuclei
    container), the **cerebral peduncle**, or any other
    container. The red nucleus's relationships to the cerebellar
    dentate nucleus, the motor cortex, the spinal cord, the
    inferior olive, the thalamus, the globus pallidus, the
    subthalamic nucleus, the CN III nucleus, and the cerebral
    peduncle are documented as **prose and boundary data**, not
    as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The **red
    nucleus's "red" color** (high iron content, rich
    vascularity) is a **``chemicals_hormones``-layer fact** —
    documented as **prose**, **never imported**.
*   **STRUCTURE CONTAINER — the FIRST paired tegmentum structure
    represented as a structure container.** The red nucleus is a
    **structure container** at ``tegmentum/red_nucleus/`` —
    holding the **left red nucleus** and the **right red
    nucleus** as **side-scoped leaves**. **This is a NEW
    structural pattern** — establishing the **structure-container
    pattern** for paired tegmentum structures.
*   **THE STRUCTURE-CONTAINER PATTERN.** Every structure has
    **ONE "home" in the tegmentum** — a **single module at
    ``tegmentum/<structure>/``** — **regardless of laterality
    class**. **Paired structures** are **structure containers**
    (``left/`` and ``right/`` children); **midline and diffuse
    bilateral structures** are **structure leaves** (single
    modules); **multi-part structures** (the **substantia
    nigra**) are **structure containers** with **pars**
    children — **recursively**.
*   **LIVE AMENDMENT TO THE TEGMENTUM CONTAINER.** The tegmentum
    container's **paired-leaf rule** — *"each tegmentum nucleus
    is a paired structure (a ``left/`` leaf and a ``right/``
    leaf)"* — should be **AMENDED** to acknowledge the
    **structure-container pattern**: **paired structures are
    structure containers holding ``left/`` and ``right/``** —
    **not leaves directly under ``tegmentum/left/`` and
    ``tegmentum/right/``**. **The red nucleus is the first
    structure-container pattern example.** The amendment should
    also acknowledge the **midline leaf** and **diffuse
    bilateral leaf** patterns (the **CLi**, **DR**, **IPN**,
    **MRF**, **PAG**) — and the **multi-part structure
    container** pattern (the **substantia nigra**, pending).
*   **DISCRETE NUCLEUS — NOT a diffuse region, NOT a midline
    nucleus, NOT a conduction pathway.** The red nucleus is a
    **sharply bounded** cell group — **paired** — with **two
    cytoarchitectonically distinct subdivisions** (magnocellular
    and parvocellular).
*   **PREMOTOR MOTOR RELAY — the rubrospinal motor relay class.**
    The red nucleus is a **premotor motor relay** — the **same
    class** as the **PPRF** (horizontal saccade generator) and
    the **riMLF** (vertical saccade generator) — **but for limb
    motor control** (reaching, flexor tone, motor coordination)
    rather than **saccades**. **The red nucleus is the first
    limb-motor premotor relay in the family.**
*   **CONTRALATERAL RUBROSPINAL DECUSSATION.** The **rubrospinal
    tract decussates** in the **ventral tegmental decussation
    (of Forel)** — **the left red nucleus controls RIGHT spinal
    cord motor function** — **the right red nucleus controls
    LEFT spinal cord motor function**. **A left red nucleus
    lesion produces RIGHT-sided motor deficits** — the
    **contralateral pattern**. **Consumers must not assume "left
    red nucleus = left-sided motor control".**
*   **NO COUPLING WARNING — premotor motor relays carry NO
    coupling warning.** The red nucleus is **two independent
    nuclei** — **no red-nucleus-to-red-nucleus coupling** in
    the oscillator sense.
*   **MAGNOCELLULAR / PARVOCELLULAR SPLIT — INTERNAL to each
    side, NOT a left/right split.** Both subdivisions are
    present in each side (left and right). **The magnocellular
    and parvocellular parts are documented as PROSE within the
    left and right leaves** — **not as structural children of
    the red nucleus container**.
*   **NOT A CN NUCLEUS.** The red nucleus is **not** a cranial
    nerve nucleus and is **NOT** cross-listed with
    ``cranial_nerve_nuclei/``. It has **one path only** (as a
    structure container).
*   **NOT a motor nucleus — a PREMOTOR MOTOR RELAY.** The
    **spinal motor neurons** are the motor nuclei; the **red
    nucleus** is a premotor relay.
*   **NOT a sensory relay, NOT a modulatory nucleus, NOT a
    limbic relay, NOT a diffuse region, NOT an oscillator, NOT
    a conduction pathway.**
*   **CHEMICALS-LAYER DISCIPLINE.** The **"red" color** (high
    iron content, rich vascularity) is a
    ``chemicals_hormones``-layer fact — documented as **prose**,
    **never imported**.
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The red nucleus
    is a **local structure container** under the tegmentum — no
    cross-listing.
*   **No nested cross-listing** at the container level. The red
    nucleus container's **structural children are the left and
    right leaves** — **not** cross-listed with any other
    container.
*   **The on-disk tree is authoritative.** If the tree has
    ``.../tegmentum/red_nucleus/left/`` and
    ``.../tegmentum/red_nucleus/right/``, the
    **structure-container** representation is authoritative.
    If the tree has ``.../tegmentum/left/red_nucleus/`` and
    ``.../tegmentum/right/red_nucleus/`` (the **alternative**
    paired representation), **the tree is authoritative** — but
    **the structure-container pattern is the cleaner
    representation** (one "home" per structure), and **the
    amendment to the tegmentum container should recommend it**.

Usage
-----
Resolve the structure container by path::

    from infrastructure.brainparts.midbrain.tegmentum import red_nucleus

Resolve a side-scoped leaf by path::

    from infrastructure.brainparts.midbrain.tegmentum.red_nucleus.left import (
        RED_NUCLEUS_LEFT_CHILDREN,
    )
    from infrastructure.brainparts.midbrain.tegmentum.red_nucleus.right import (
        RED_NUCLEUS_RIGHT_CHILDREN,
    )

Or by fully-qualified path string (leaves, not the container)::

    left_path = "midbrain.tegmentum.red_nucleus.left"
    right_path = "midbrain.tegmentum.red_nucleus.right"

**Do not** assume the red nucleus is a **leaf** — it is a
**structure container** — it holds the **left red nucleus** and
the **right red nucleus** as **side-scoped leaves**.

**Do not** assume the red nucleus is a **midline nucleus** or a
**diffuse bilateral region** — it is a **paired discrete
nucleus** — the **same structure class** as the **substantia
nigra** and the **VTA** — **but with its own structure-container
pattern**.

**Do not** assume the red nucleus is a **cranial nerve nucleus** —
it is **not** and is **NOT** cross-listed with
``cranial_nerve_nuclei/``.

**Do not** assume the red nucleus is a **motor nucleus** — it is
a **premotor motor relay** — the **spinal motor neurons** are
the motor nuclei; the **red nucleus** relays via the
**rubrospinal tract**.

**Do not** assume the red nucleus is a **sensory relay**, a
**modulatory nucleus**, a **limbic relay**, a **diffuse
region**, an **oscillator**, or a **conduction pathway** — it is
a **discrete paired premotor motor relay**.

**Do not** assume the red nucleus's **rubrospinal tract is
ipsilateral** — it **decussates** in the **ventral tegmental
decussation (of Forel)** — **the left red nucleus controls RIGHT
spinal cord motor function** — the **contralateral pattern**.
**A left red nucleus lesion produces RIGHT-sided motor
deficits**.

**Do not** conflate the **magnocellular / parvocellular split**
with the **left / right split** — the **magnocellular and
parvocellular parts are both present in each side** — **the
split is internal to each side** — **not a left/right split**.
**The magnocellular and parvocellular parts are documented as
PROSE in the left and right leaves** — **not as structural
children of the red nucleus container**.

**Do not** import the **red nucleus's "red" color** (high iron
content, rich vascularity) into the midbrain structural layer —
it is a **``chemicals_hormones``-layer fact**.

**Do not** import a **coupling warning** into the red nucleus —
**premotor motor relays carry NO coupling warning** — same rule
as every non-oscillator class. **The two sides are independent
nuclei.**

Iterating the red nucleus structure container's children
(recommended consumer pattern)::

    import pkgutil
    import infrastructure.brainparts.midbrain.tegmentum.red_nucleus as rn_pkg

    RED_NUCLEUS_CHILDREN = tuple(
        m.name for m in pkgutil.iter_modules(rn_pkg.__path__)
        if not m.name.startswith("_")
    )
    # Expected: ("left", "right")
    #
    # Each side is a discrete paired nucleus — the left red nucleus
    # and the right red nucleus — with internal subdivisions
    # (magnocellular and parvocellular) documented as PROSE within
    # each leaf.

Reaching the left red nucleus (recommended consumer pattern — the
LEFT leaf)::

    # The left red nucleus — the LEFT discrete paired nucleus —
    # the left rubrospinal origin (which decussates to the RIGHT
    # spinal cord — contralateral clinical pattern):
    #
    #   brainparts.midbrain.tegmentum.red_nucleus.left
    #
    # The left red nucleus controls RIGHT spinal cord motor
    # function (contralateral decussation).

Reaching the right red nucleus (recommended consumer pattern —
the RIGHT leaf)::

    # The right red nucleus — the RIGHT discrete paired nucleus —
    # the right rubrospinal origin (which decussates to the LEFT
    # spinal cord — contralateral clinical pattern):
    #
    #   brainparts.midbrain.tegmentum.red_nucleus.right
    #
    # The right red nucleus controls LEFT spinal cord motor
    # function (contralateral decussation).

Reaching the substantia nigra (recommended consumer pattern — the
NEXT structure container, pending)::

    # The substantia nigra is the NEXT paired structure container
    # (pending) — a multi-part structure with pars_compacta and
    # pars_reticulata — each pars paired (left/right):
    #
    #   brainparts.midbrain.tegmentum.substantia_nigra
    #
    # The substantia nigra will follow the structure-container
    # pattern: a container at tegmentum/substantia_nigra/ with
    # pars_compacta/ and pars_reticulata/ as children — each pars
    # being a paired structure (left/ and right/) — its own
    # structure-container pattern applies recursively.

Reaching the MRF (recommended consumer pattern — the diffuse
bilateral leaf)::

    # The midbrain reticular formation is a diffuse bilateral
    # leaf — a single module:
    #
    #   brainparts.midbrain.tegmentum.midbrain_reticular_formation
    #
    # The MRF is a DIFFUSE BILATERAL REGION — a single leaf. The
    # red nucleus is a DISCRETE PAIRED NUCLEUS — a structure
    # container. DIFFERENT laterality classes: diffuse bilateral
    # (MRF) vs. paired (red nucleus).

Reaching the PAG (recommended consumer pattern — the diffuse
bilateral leaf)::

    # The periaqueductal gray is a diffuse bilateral leaf — a
    # single module:
    #
    #   brainparts.midbrain.tegmentum.periaqueductal_gray
    #
    # The PAG is a DIFFUSE BILATERAL REGION — a single leaf. The
    # red nucleus is a DISCRETE PAIRED NUCLEUS — a structure
    # container. DIFFERENT laterality classes: diffuse bilateral
    # (PAG) vs. paired (red nucleus).

Reaching the CLi, the DR, and the IPN (recommended consumer
pattern — the midline leaves)::

    # The caudal linear nucleus (CLi), the dorsal raphe nucleus
    # (DR), and the interpeduncular nucleus (IPN) are midline
    # leaves — single modules:
    #
    #   brainparts.midbrain.tegmentum.caudal_linear_nucleus
    #   brainparts.midbrain.tegmentum.dorsal_raphe_nucleus
    #   brainparts.midbrain.tegmentum.interpeduncular_nucleus
    #
    # The CLi, the DR, and the IPN are MIDLINE NUCLEI — single
    # leaves. The red nucleus is a PAIRED NUCLEUS — a structure
    # container. DIFFERENT laterality classes: midline vs. paired.

Reaching the CN III nucleus (recommended consumer pattern — the
OTHER substrate of Benedikt / Claude syndrome)::

    # The oculomotor nucleus (CN III) is the OTHER substrate of
    # Benedikt / Claude syndrome — the CN III fascicles traverse
    # the midbrain tegmentum near the red nucleus, and a lesion
    # involving both produces the syndrome:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   (OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #    — cross-listed)
    #
    # Benedikt syndrome = red nucleus (rubral tremor) + CN III
    # fascicles (ipsilateral CN III palsy). Claude syndrome =
    # red nucleus (ataxia) + CN III fascicles (ipsilateral
    # CN III palsy) — a less complete Benedikt. The red nucleus
    # is ONE OF THE TWO substrates — the CN III fascicles are
    # the other.

Reaching the cerebral peduncle (recommended consumer pattern —
the contrast case, with the CONTRASTING decussation)::

    # The cerebral peduncle is the CONTRAST case — the
    # corticospinal tract decussates in the MEDULLARY PYRAMIDAL
    # DECUSSATION — the SAME contralateral clinical pattern as
    # the red nucleus's rubrospinal tract (which decussates in
    # the VENTRAL TEGMENTAL DECUSSATION):
    #
    #   brainparts.midbrain.cerebral_peduncle
    #
    # Both the red nucleus and the cerebral peduncle have
    # CONTRALATERAL clinical patterns — but for DIFFERENT
    # reasons: the cerebral peduncle's corticospinal fibers
    # decussate in the medulla (pyramidal decussation); the
    # red nucleus's rubrospinal fibers decussate in the midbrain
    # (ventral tegmental decussation).

Reaching the inferior olive (recommended consumer pattern — the
DOWNSTREAM target of the parvocellular part)::

    # The inferior olive is the DOWNSTREAM target of the
    # parvocellular red nucleus — the rubro-olivary tract
    # connects the red nucleus to the inferior olive:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.inferior_olive
    #
    # The parvocellular red nucleus projects to the inferior
    # olive, which projects back to the cerebellum (the
    # olivocerebellar tract) — the cerebro-cerebellar loop.

Reaching the cerebellar dentate nucleus (recommended consumer
pattern — the UPSTREAM input)::

    # The cerebellar dentate nucleus is the UPSTREAM input to the
    # red nucleus — the dentatorubral tract (via the superior
    # cerebellar peduncle) connects the dentate nucleus to the
    # red nucleus:
    #
    #   brainparts.hindbrain.metencephalon.cerebellum.deep_cerebellar_nuclei.dentate_nucleus
    #
    # The dentate nucleus projects to the red nucleus (via the
    # superior cerebellar peduncle) — the cerebellar motor
    # coordination input.

Reaching the spinal cord (recommended consumer pattern — the
DOWNSTREAM target of the magnocellular part, CONTRALATERAL)::

    # The spinal cord is the DOWNSTREAM target of the
    # magnocellular red nucleus — the rubrospinal tract
    # connects the red nucleus to the spinal cord
    # (CONTRALATERAL — the left red nucleus projects to the RIGHT
    # spinal cord):
    #
    #   brainparts.spinal_cord
    #
    # The rubrospinal tract decussates in the ventral tegmental
    # decussation (of Forel) — the left red nucleus controls
    # RIGHT spinal cord motor function (contralateral).

Internal-organization detail (not wired — consult references)::

    # The red nucleus has TWO functional subdivisions — BOTH
    # PRESENT IN EACH SIDE (left and right):
    #
    #   magnocellular part (RNm)    -> CAUDAL, LARGE-CELLED,
    #                                  OLDER (present in all
    #                                  mammals) — the rubrospinal
    #                                  origin — motor coordination,
    #                                  flexor tone, reaching,
    #                                  gait — projects to the
    #                                  spinal cord (contralateral,
    #                                  via the rubrospinal tract)
    #   parvocellular part (RNp)    -> ROSTRAL, SMALL-CELLED,
    #                                  NEWER (enlarged in primates,
    #                                  including humans) — the
    #                                  relay in the cerebellar ->
    #                                  red nucleus -> inferior olive
    #                                  circuit — receives from the
    #                                  cerebellar dentate nucleus
    #                                  (via the superior cerebellar
    #                                  peduncle); projects to the
    #                                  inferior olive (via the
    #                                  rubro-olivary tract) — part
    #                                  of the cerebro-cerebellar loop
    #
    # Both subdivisions are INTERNAL to each side — NOT a left/
    # right split. The magnocellular and parvocellular parts are
    # PROSE within each left and right leaf — not structural
    # children of the red nucleus container.
    #
    # Do not attempt to resolve these subdivisions as sub-paths of
    # the red nucleus container — they are PROSE within the left
    # and right leaves.

The rubrospinal decussation — detail (not wired — consult
references)::

    # The CONTRALATERAL RUBROSPINAL DECUSSATION — the defining
    # asymmetry of the red nucleus pair:
    #
    #   LEFT red nucleus (left magnocellular part)
    #     -> LEFT rubrospinal tract
    #     -> crosses the midline in the VENTRAL TEGMENTAL
    #        DECUSSATION (of Forel)
    #     -> RIGHT lateral funiculus of the spinal cord
    #     -> RIGHT spinal motor function
    #
    #   RIGHT red nucleus (right magnocellular part)
    #     -> RIGHT rubrospinal tract
    #     -> crosses the midline in the VENTRAL TEGMENTAL
    #        DECUSSATION (of Forel)
    #     -> LEFT lateral funiculus of the spinal cord
    #     -> LEFT spinal motor function
    #
    # THE LEFT RED NUCLEUS CONTROLS RIGHT SPINAL CORD MOTOR
    # FUNCTION. THE RIGHT RED NUCLEUS CONTROLS LEFT SPINAL CORD
    # MOTOR FUNCTION. A LEFT red nucleus lesion produces RIGHT-
    # sided motor deficits — the CONTRAALTERAL pattern. This is
    # analogous to the cerebral peduncle's contralateral pattern
    # (the corticospinal tract decussates in the medullary
    # pyramidal decussation).
    #
    # Do not assume "left red nucleus = left-sided motor control".
    # The contralateral decussation is the structural fact.

Clinical-pattern detail (not wired — consult references)::

    # The red nucleus has NO NAMED SYNDROME OF ITS OWN — its
    # clinical associations are INDIRECT, via its involvement in
    # BROADER brainstem lesions:
    #
    #   BENEDIKT SYNDROME        -> the red nucleus IS ONE OF THE
    #     (ipsilateral CN III       TWO substrates — the "rubral
    #      palsy + contralateral    tremor" (coarse, proximal,
    #      ataxia / tremor)         resting + intention, worse on
    #                               movement) — the OTHER substrate
    #                               is the CN III fascicles.
    #   CLAUDE SYNDROME          -> the red nucleus IS ONE OF THE
    #     (ipsilateral CN III       TWO substrates — the ataxia
    #      palsy + contralateral    (a less complete Benedikt,
    #      ataxia)                  without the tremor) — the OTHER
    #                               substrate is the CN III
    #                               fascicles.
    #   HOLMES TREMOR            -> one substrate — the red nucleus
    #     (coarse, proximal,        and/or the superior cerebellar
    #      resting + intention     peduncle and/or the
    #      tremor)                  cerebello-thalamic pathway.
    #   CEREBELLAR ATAXIA        -> one relay node — the red
    #     (from cerebellar          nucleus is a node in the
    #      lesions)                 cerebellar -> red nucleus ->
    #                               inferior olive -> cerebellum
    #                               loop.
    #   MOTOR WEAKNESS /         -> one contributor — the
    #     FLEXOR TONE               rubrospinal tract is one of
    #     ABNORMALITIES             several descending motor
    #                               pathways (corticospinal,
    #                               reticulospinal are also
    #                               involved).
    #
    # The red nucleus is ONE substrate (Benedikt, Claude, Holmes
    # tremor) or ONE contributor (cerebellar ataxia, motor
    # weakness) — not the sole substrate. No named red nucleus
    # syndrome exists.
    #
    # Do not conflate these patterns — they localize to the red
    # nucleus plus its co-substrates (CN III fascicles for
    # Benedikt / Claude; superior cerebellar peduncle and
    # cerebello-thalamic pathway for Holmes tremor; cerebellum
    # for cerebellar ataxia; the multiple descending motor
    # pathways for motor weakness).

The structure-container pattern — detail (not wired — structural
note)::

    # The red nucleus is the FIRST PAIRED TEGMENTUM STRUCTURE
    # represented as a STRUCTURE CONTAINER — a new structural
    # pattern in the family:
    #
    #   tegmentum/red_nucleus/          (STRUCTURE CONTAINER)
    #     ├── left/                     (side-scoped leaf)
    #     └── right/                    (side-scoped leaf)
    #
    # The pattern is:
    #   - EVERY structure has ONE "home" in the tegmentum — a
    #     single module at tegmentum/<structure>/ — regardless of
    #     laterality class.
    #   - The structure decides its own internal representation:
    #     * PAIRED structures (the red nucleus, and PENDING: the
    #       substantia nigra, the VTA, the riMLF, the
    #       interstitial nucleus of Cajal) — STRUCTURE CONTAINERS
    #       with left/ and right/ children.
    #     * MIDLINE or DIFFUSE BILATERAL structures (the CLi, the
    #       DR, the IPN, the MRF, the PAG) — STRUCTURE LEAVES —
    #       single modules.
    #     * MULTI-PART structures (the substantia nigra, with its
    #       pars compacta and pars reticulata) — STRUCTURE
    #       CONTAINERS with pars children — each pars then being
    #       paired (left/ and right/ within each pars) or a leaf
    #       — recursively.
    #
    # The tegmentum container's "paired-leaf rule" — "each
    # tegmentum nucleus is a paired structure (a left/ leaf and a
    # right/ leaf)" — is amended by the structure-container
    # pattern: paired structures are structure containers holding
    # left/ and right/ (not leaves directly under tegmentum/left/
    # and tegmentum/right/).
    #
    # The tegmentum container should be amended to acknowledge
    # this pattern.

References
----------
*   **Canonical red nucleus anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (The red nucleus — its magnocellular and parvocellular
    subdivisions, its afferents (cerebellar dentate, motor
    cortex) and efferents (rubrospinal, rubro-olivary,
    rubroreticular, rubro-thalamic), its location in the rostral
    midbrain tegmentum.)
*   **Red nucleus — comprehensive review:** Massion, J. (1967).
    "The mammalian red nucleus." *Physiological Reviews*
    47:383–436. (The red nucleus — the classic comprehensive
    review of its anatomy, connections, and function —
    magnocellular and parvocellular parts, rubrospinal and
    rubro-olivary projections.)
*   **Red nucleus — magnocellular and parvocellular:** Strominger,
    N.L., Strominger, A.I. (1971). "Ascending brain stem
    projections of the red nucleus in the rhesus monkey."
    *Journal of Comparative Neurology* 143:217–242. (The
    magnocellular and parvocellular parts — their different
    connections and functions.)
*   **Rubrospinal tract:** Pompeiano, O., Brodal, A. (1957). "The
    origin of vestibulospinal fibres in the cat. An experimental-
    anatomical study, with comments on the descending medial
    longitudinal fasciculus." *Archives Italiennes de Biologie*
    95:166–195. (The rubrospinal tract — its origin in the
    magnocellular red nucleus, its decussation in the ventral
    tegmental decussation, its termination in the spinal cord.)
*   **Rubrospinal tract — human:** Nathan, P.W., Smith, M.C.
    (1955). "Long descending tracts in man. I. Review of the
    present knowledge." *Brain* 78:248–303. (The rubrospinal
    tract in humans — its relative size compared to other
    mammals, its role in human motor control.)
*   **Rubro-olivary tract:** Saint-Cyr, J.A., Courville, J. (1981).
    "Sources of descending afferents to the inferior olive from
    the upper brain stem in the cat as revealed by the retrograde
    transport of horseradish peroxidase." *Journal of Comparative
    Neurology* 198:567–581. (The rubro-olivary tract — the
    parvocellular red nucleus projection to the inferior olive —
    part of the cerebro-cerebellar loop.)
*   **Cerebro-cerebellar loop:** Allen, G.I., Tsukahara, N. (1974).
    "Cerebrocerebellar communication systems." *Physiological
    Reviews* 54:957–1006. (The cerebro-cerebellar loop — the
    cerebellar dentate nucleus → red nucleus → inferior olive →
    cerebellum circuit — the parvocellular red nucleus relay.)
*   **Benedikt syndrome (DIRECT — the red nucleus is one of two
    substrates):** Benedikt, M. (1889). "Krankenvorstellung."
    *Wiener Medicinische Presse* 30:1–4. (Benedikt syndrome —
    ipsilateral CN III palsy + contralateral ataxia / tremor —
    the red nucleus and the CN III fascicles as the two
    substrates.)
*   **Claude syndrome (DIRECT — the red nucleus is one of two
    substrates):** Claude, H., Loyez, M. (1912). "Ramollissement
    du noyau rouge." *Revue Neurologique* 23:49–51. (Claude
    syndrome — ipsilateral CN III palsy + contralateral ataxia
    — a less complete Benedikt — the red nucleus and the CN III
    fascicles as the two substrates.)
*   **Holmes tremor:** Holmes, G. (1904). "On certain tremors in
    organic cerebral lesions." *Brain* 27:327–375. (Holmes
    tremor — the coarse, proximal, resting and intention tremor
    associated with lesions of the red nucleus, the superior
    cerebellar peduncle, or the cerebello-thalamic pathway.)
*   **Red nucleus — iron content and "red" color:** Morris, C.M.,
    Candy, J.M., Oakley, A.E., Bloxham, C.A., Edwardson, J.A.
    (1992). "Histochemical distribution of non-haem iron in the
    human brain." *Acta Neuropathologica* 84:225–230. (The high
    iron content of the red nucleus — the "red" color comes from
    the iron and the rich vascularity.)
*   **Cerebellar dentate nucleus (contrast — the principal
    upstream input):** Brodal, A. (2010). *The Central Nervous
    System: Structure and Function*, 4th ed. (The cerebellar
    dentate nucleus — the principal input to the red nucleus,
    via the superior cerebellar peduncle.)
*   **CN III nucleus (contrast — the co-substrate of Benedikt /
    Claude syndrome):** Büttner-Ennever, J.A. (2006).
    *Neuroanatomy of the Oculomotor System*. (The CN III
    nucleus and the CN III fascicles — the oculomotor substrate
    of Benedikt and Claude syndrome, alongside the red nucleus.)
*   **Cerebral peduncle (contrast — the same contralateral
    clinical pattern):** Weber, H.D. (1856). "A contribution to
    the pathology of the crura cerebri." *Medico-Chirurgical
    Transactions* 39:121–140. (The cerebral peduncle — the
    corticospinal tract, with its contralateral clinical
    pattern due to the medullary pyramidal decussation — the
    SAME contralateral pattern as the red nucleus's rubrospinal
    tract, but with a DIFFERENT decussation site.)
*   **SLEA (contrast — the red nucleus is not SLEA):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; **NOT** the red nucleus.)
*   NeuroNames — Red nucleus; FMA — Red nucleus. **The red
    nucleus is a paired nucleus — each side is a distinct
    anatomical structure. The structure-container pattern —
    ``tegmentum/red_nucleus/left/`` and
    ``tegmentum/red_nucleus/right/`` — is the clean
    representation.**
"""