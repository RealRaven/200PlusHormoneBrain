"""
infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left.mesencephalic_trigeminal_nucleus
=============================================================================================

Anatomical Hierarchy
--------------------
::

    midbrain
    ├── cranial_nerve_nuclei
    │   ├── left
    │   │   ├── oculomotor_nucleus
    │   │   ├── trochlear_nucleus
    │   │   ├── mesencephalic_trigeminal_nucleus   <-- THIS MODULE
    │   │   │                                       (leaf — FUNCTIONAL
    │   │   │                                       parent)
    │   │   └── edinger_westphal_nucleus
    │   └── right
    │       └── ...
    └── tegmentum
        ├── left
        │   ├── oculomotor_nucleus
        │   ├── trochlear_nucleus
        │   ├── mesencephalic_trigeminal_nucleus   (SAME LEAF —
        │   │                                       TOPOGRAPHIC
        │   │                                       parent)
        │   ├── edinger_westphal_nucleus
        │   ├── substantia_nigra
        │   └── ...
        └── right
            └── ...

**Primary synonym:** Left mesencephalic trigeminal nucleus; left
mesencephalic nucleus of the trigeminal nerve; left mesV; left
mesencephalic nucleus of V; left nucleus of the mesencephalic tract
of the trigeminal nerve; **the left primary proprioceptive nucleus
of the trigeminal system**.
**Cytoarchitectonic designation:** **Not a Brodmann area**
(brainstem). A **primary sensory nucleus** located in the **lateral
midbrain tegmentum**, at the **level of the superior colliculus**,
**lateral to the periaqueductal gray** and **medial to the lateral
lemniscus**. It is composed of **large, pseudounipolar neurons** —
**morphologically identical to dorsal root ganglion cells** — but
**uniquely located inside the CNS**. **The only primary sensory
nucleus in the CNS** whose **pseudounipolar cell bodies lie within
the CNS** — see *The Only Primary Sensory Nucleus in the CNS* below.
**Part of:** The **cranial_nerve_nuclei** functional grouping
container → **left** side container (functional parent), **and** the
**tegmentum** topographic container → **left** side container
(topographic parent). **Dual-parent leaf — see *Structural parent*
below and *Cross-Listing Statement*.**
**Structural parent (FUNCTIONAL):** ``.../cranial_nerve_nuclei/left/``
→ **direct child** of the **left side container** of the
cranial_nerve_nuclei functional grouping container.
**Structural parent (TOPOGRAPHIC):** ``.../tegmentum/left/`` →
**direct child** of the **left side container** of the tegmentum
topographic container.
**Structural children:** **None.** This is a **leaf** module. The
**primary afferent fibers** (from jaw muscle spindles, periodontal
mechanoreceptors, and possibly extraocular muscle proprioceptors)
are **prose** — they are the **peripheral branches of these very
neurons** (pseudounipolar cells have one process that bifurcates into
a peripheral and a central branch), **not** structural children.
**Boundary status (DUAL-PARENT LEAF — CROSS-LISTED between
``cranial_nerve_nuclei/left/`` and ``tegmentum/left/``):** **Boundary
case — the left mesencephalic trigeminal nucleus is a DUAL-PARENT
LEAF.** It is reachable by **two** structural paths:
*   **Functional path** —
    ``.../cranial_nerve_nuclei/left/mesencephalic_trigeminal_nucleus/``
*   **Topographic path** —
    ``.../tegmentum/left/mesencephalic_trigeminal_nucleus/``
**Both resolve to the SAME leaf** — this module. Consumers resolving
the leaf by **either** path get **the same module**. Consumers must
**not** assume the two paths lead to different structures — they lead
to **one leaf**, dual-parented. See *Cross-Listing Statement*.
**Boundary status (THE ONLY PRIMARY SENSORY NUCLEUS IN THE CNS — the
defining fact of this leaf):** **Boundary case — the left
mesencephalic trigeminal nucleus is the ONLY PRIMARY SENSORY NUCLEUS
IN THE CNS.** Every other primary sensory nucleus in the body has its
**primary afferent cell bodies in a PERIPHERAL ganglion**:
*   **Dorsal root ganglia** — for the **spinal cord** primary
    sensory neurons.
*   **Trigeminal ganglion (semilunar / Gasserian ganglion)** — for
    the **main sensory trigeminal nucleus** (touch, pressure) and
    the **spinal trigeminal nucleus** (pain, temperature).
*   **Geniculate, inferior (petrosal), nodose, and jugular ganglia**
    — for the cranial nerves VII, IX, and X.
*   **Vestibular and spiral ganglia** — for the cranial nerve VIII.
The **mesencephalic trigeminal nucleus** is the **sole exception** —
its **pseudounipolar cell bodies lie INSIDE the CNS**, in the
**midbrain tegmentum**. Its **primary afferent fibers** are the
**peripheral branches of these very neurons** — they **bifurcate**
from the cell body, one branch going **peripherally** (to the jaw
muscle spindles and periodontal mechanoreceptors, via the
**mandibular division of the trigeminal nerve, V3**), and the other
branch going **centrally** (via the **mesencephalic tract of V** to
the **trigeminal motor nucleus** in the pons, for the **jaw-jerk
reflex**). **This is the only place in the body where a primary
sensory neuron's cell body is in the CNS.** Consumers must **not**
conflate the mesencephalic V with the **main sensory trigeminal
nucleus** or the **spinal trigeminal nucleus** — both of those have
their **primary afferent cell bodies in the trigeminal ganglion** and
are **NOT** "primary sensory neurons in the CNS" in this strict
sense.
**Boundary status (PROPRIOCEPTIVE — NOT touch/pressure, NOT
pain/temperature):** **Boundary case — the left mesencephalic
trigeminal nucleus is the PROPRIOCEPTIVE trigeminal nucleus — NOT the
touch/pressure nucleus, and NOT the pain/temperature nucleus.** The
trigeminal system has **three** primary sensory nuclei, distinguished
by **sensory modality**:
*   **Mesencephalic trigeminal nucleus (mesV)** — **THIS LEAF** —
    **proprioception** from **jaw muscle spindles** (masseter,
    temporalis, medial pterygoid, lateral pterygoid), **periodontal
    mechanoreceptors**, and possibly **extraocular muscle
    proprioceptors** (contested) and **dental pulp** (contested).
*   **Main (principal / pontine) sensory trigeminal nucleus** — **NOT
    this leaf** — **touch and pressure** from the face, oral cavity,
    and teeth. **Pons** structure
    (``.../hindbrain/metencephalon/pons/trigeminal_main_sensory_nucleus/``).
*   **Spinal trigeminal nucleus** — **NOT this leaf** — **pain and
    temperature** from the face, oral cavity, and teeth. **Pons +
    medulla** structure
    (``.../hindbrain/myencephalon/medulla_oblongata/spinal_trigeminal_nucleus/``).
**They are THREE DIFFERENT NUCLEI** in **THREE DIFFERENT LOCATIONS**
(midbrain, pons, medulla/pons) processing **THREE DIFFERENT
MODALITIES**. Consumers must **not** conflate mesV with the main
sensory or spinal trigeminal nuclei, and must **not** attribute
**facial touch** or **facial pain** function to this leaf.
**Boundary status (NOT the trigeminal motor nucleus — the motor
nucleus is the MASTICATORY MOTOR pool):** **Boundary case — the left
mesencephalic trigeminal nucleus is NOT the left trigeminal motor
nucleus.** The **left trigeminal motor nucleus (CN V motor)**
(``.../hindbrain/metencephalon/pons/trigeminal_motor_nucleus/``) is
the **branchiomotor** nucleus for the **muscles of mastication** —
**masseter**, **temporalis**, **medial pterygoid**, **lateral
pterygoid**, **mylohyoid**, **anterior belly of the digastric**, and
**tensor tympani** and **tensor veli palatini**. It is a **pons**
structure. The **left mesV** (here) is a **midbrain** structure —
the **proprioceptive sensory nucleus**. **They are DIFFERENT
NUCLEI** in **DIFFERENT LOCATIONS** (pons vs. midbrain) — the
**motor** nucleus is **branchiomotor**; the **mesV** is **primary
sensory**. **They are CONNECTED** — the mesV's central processes
project to the trigeminal motor nucleus for the **jaw-jerk reflex** —
but **connectivity is not identity**. Consumers must **not** conflate
the two, and must **not** resolve the trigeminal motor nucleus
through the mesV path.
**Boundary status (NOT the trigeminal ganglion — the ganglion is
PERIPHERAL):** **Boundary case — the left mesencephalic trigeminal
nucleus is NOT the left trigeminal (semilunar / Gasserian)
ganglion.** The **trigeminal ganglion** is a **PERIPHERAL sensory
ganglion** — it contains the **pseudounipolar cell bodies** for the
**primary afferent fibers of the main sensory trigeminal nucleus**
(touch, pressure) and the **spinal trigeminal nucleus** (pain,
temperature). It is **NOT a midbrain structure** — it is **wired
elsewhere** (in the peripheral nervous system, in Meckel's cave). The
**left mesV** (here) is the **exception** — its **cell bodies are in
the CNS**, in the **midbrain tegmentum**. **They are DIFFERENT
STRUCTURES across the CNS-PNS boundary** — the **ganglion** is
**peripheral**; the **mesV** is **central**. **The mesV has NO
ganglion** — its cell bodies are **in the nucleus itself**. Consumers
must **not** conflate the two, and must **not** assume mesV primary
afferents have their cell bodies in the trigeminal ganglion — they
**do not**.
**Boundary status (NOT the mesencephalic tract of V — the tract is
the FIBER PATHWAY):** **Boundary case — the left mesencephalic
trigeminal nucleus is NOT the left mesencephalic tract of V.** The
**mesencephalic tract of V** (also called the **mesencephalic root
of the trigeminal nerve**, or **tractus mesencephalicus nervi
trigemini**) is the **longitudinal fiber bundle** formed by the
**central branches** of the mesV neurons — the axons that travel
**down** from the midbrain mesV to the **trigeminal motor nucleus**
in the pons. **The tract is a CONDUCTION PATHWAY** — **white
matter**; the **nucleus** is **grey matter**. **They are DIFFERENT
STRUCTURES** — the **nucleus** contains the **cell bodies**; the
**tract** contains the **axons**. Consumers must **not** conflate the
nucleus with the tract, and must **not** resolve the tract through
the nucleus path (or vice versa).
**Boundary status (NOT the trigeminal nerve — the nerve is
PERIPHERAL):** **Boundary case — the left mesencephalic trigeminal
nucleus is NOT the left trigeminal nerve.** The **left trigeminal
nerve (CN V)** is the **peripheral axon bundle** — it is **wired
elsewhere** (peripheral nervous system). Its **mandibular division
(V3)** carries the **peripheral branches of the mesV neurons** to the
**jaw muscle spindles and periodontal mechanoreceptors** — but the
**nerve** is **not the nucleus**. **They are DIFFERENT STRUCTURES
across the CNS-PNS boundary.** Consumers must **not** conflate the
mesV with the trigeminal nerve, and must **not** resolve the nerve
through the mesV path.
**Boundary status (NOT the jaw-jerk reflex — the reflex is the
CIRCUIT):** **Boundary case — the left mesencephalic trigeminal
nucleus is NOT the jaw-jerk reflex.** The **jaw-jerk reflex** (also
called the **masseter reflex** or **jaw jerk**) is a
**monosynaptic stretch reflex** — one of the **shortest reflex arcs
in the body** — whose circuit is:
*   **Afferent limb:** **Jaw muscle spindle primary afferents** (in
    the **masseter** and **temporalis**) → **mesV neurons** (their
    peripheral branches, cell bodies in the mesV).
*   **Central branch:** MesV neurons → **mesencephalic tract of V**
    → **trigeminal motor nucleus** (pons).
*   **Efferent limb:** **Trigeminal motor nucleus** →
    **masseter** and **temporalis** (contraction of the jaw-closing
    muscles).
**The mesV is ONE COMPONENT of this circuit** — the **afferent
limb's cell bodies**. The **circuit itself** is a **physiological
entity**, not a structure. Consumers must **not** conflate the mesV
with the jaw-jerk reflex, and must **not** resolve the reflex through
the mesV path — the reflex is **prose**, not a structural child.
**Boundary status (NOT the periaqueductal gray or the lateral
lemniscus — those are NEIGHBORS):** **Boundary case — the left
mesencephalic trigeminal nucleus is NOT the left periaqueductal gray
(PAG), and NOT the left lateral lemniscus.** The **PAG**
(``.../tegmentum/left/periaqueductal_gray/``) is the
**pain-modulation and defensive-behavior** structure — **medial** to
mesV. The **lateral lemniscus**
(``.../hindbrain/metencephalon/pons/lateral_lemniscus/``) is the
**auditory** ascending tract — **lateral** to mesV. **They are
DIFFERENT STRUCTURES** — the **PAG** is a **modulatory grey-matter
region**; the **lateral lemniscus** is a **conduction pathway**; the
**mesV** is a **primary sensory nucleus**. Consumers must **not**
conflate the mesV with either, and must **not** resolve the PAG or
the lateral lemniscus through the mesV path.
**Boundary status (NOT the locus coeruleus or the dorsal raphe —
those are NEIGHBORS, not mesV):** **Boundary case — the left
mesencephalic trigeminal nucleus is NOT the locus coeruleus and NOT
the dorsal raphe nucleus.** The **locus coeruleus**
(``.../hindbrain/metencephalon/pons/locus_coeruleus/``) is the
**noradrenergic** arousal/attention nucleus — **pons**. The **dorsal
raphe nucleus**
(``.../midbrain/tegmentum/dorsal_raphe_nucleus/``) is the
**serotonergic** arousal/mood nucleus — **midbrain**, but
**medial** to mesV. **They are DIFFERENT STRUCTURES** — the **locus
coeruleus** and **dorsal raphe** are **neuromodulatory nuclei** (with
chemicals-layer phenotypes); the **mesV** is a **primary sensory
nucleus**. Consumers must **not** conflate the mesV with either.
*(The **noradrenergic** and **serotonergic** phenotypes are
``chemicals_hormones``-layer facts — not structural facts of mesV.)*
**Boundary status (SENSORY NUCLEUS — NOT a motor nucleus, NOT an
oscillator, NOT a premotor pool, NOT a conduction pathway):**
**Boundary case — the left mesencephalic trigeminal nucleus is a
SENSORY NUCLEUS.** In the family's **structure-class taxonomy**, it
is the **first sensory nucleus** in the midbrain CN group — **not** a
motor nucleus (CN III, CN IV), **not** a preganglionic
parasympathetic nucleus (Edinger-Westphal), **not** an oscillator,
**not** a premotor pool, **not** a conduction pathway, and **not** a
grey-matter processing nucleus (substantia nigra, red nucleus). **The
family's rule applies: sensory nuclei carry NO coupling warning** —
same rule as motor nuclei, premotor pools, and conduction pathways.
Its coordination with the **right mesV** is **not** intrinsic
nucleus-to-nucleus coupling — the mesV **projects bilaterally** to
the **trigeminal motor nuclei** (for the jaw-jerk reflex and jaw
movements), and this **bilateral projection** is what produces the
**bilateral jaw-jerk response** in the clinic. **Sensory nuclei carry
NO coupling warning** — same rule as all non-oscillator classes. It
is a **strict mirror with NO warning**. See *Lateralization Notes*
and *Design Contract*.

Overview
--------
The left mesencephalic trigeminal nucleus (left mesV) is the **left
primary proprioceptive nucleus of the trigeminal system** — the
**only primary sensory nucleus in the CNS** whose **pseudounipolar
cell bodies lie within the CNS**. It is located in the **left
lateral midbrain tegmentum**, at the **level of the superior
colliculus**, **medial to the lateral lemniscus** and **lateral to
the periaqueductal gray**. It is the **afferent limb's cell bodies**
of the **jaw-jerk reflex** (masseter reflex), and it is a
**dual-parent leaf** — reachable by **both** the functional path
(``.../cranial_nerve_nuclei/left/mesencephalic_trigeminal_nucleus/``)
and the topographic path
(``.../tegmentum/left/mesencephalic_trigeminal_nucleus/``).

**The left mesV is the ONLY PRIMARY SENSORY NUCLEUS IN THE CNS.**
Every other primary sensory nucleus has its **primary afferent cell
bodies in a peripheral ganglion** (dorsal root ganglion, trigeminal
ganglion, geniculate/petrosal/nodose/jugular ganglia, vestibular/
spiral ganglia). **The mesV is the sole exception** — its
**pseudounipolar cell bodies lie inside the CNS**, and its
**peripheral and central branches bifurcate from the cell body**.
This is **the defining fact** of the leaf.

**The left mesV is the PROPRIOCEPTIVE trigeminal nucleus — NOT the
touch/pressure nucleus, NOT the pain/temperature nucleus.** The
**touch/pressure** nucleus is the **main (principal / pontine)
sensory trigeminal nucleus** (pons); the **pain/temperature**
nucleus is the **spinal trigeminal nucleus** (pons + medulla). The
three are **different nuclei** in **different locations** processing
**different modalities**.

**The left mesV is a SENSORY NUCLEUS in the family's taxonomy.** It
carries **NO coupling warning** — same rule as motor nuclei,
premotor pools, and conduction pathways. Its **bilateral projection**
to the trigeminal motor nuclei (via the mesencephalic tract of V) is
what produces the **bilateral jaw-jerk response** — **not** intrinsic
mesV-to-mesV coupling.

**The left mesV is a dual-parent leaf.** Both structural parents are
named together — the **functional parent**
(``.../cranial_nerve_nuclei/left/``) and the **topographic parent**
(``.../tegmentum/left/``). Consumers resolving the leaf by **either**
path get **this module**.

The Only Primary Sensory Nucleus in the CNS (the defining distinction)
---------------------------------------------------------------------
**The mesV is the only primary sensory nucleus in the CNS.** This is
worth stating precisely, because it is **the single most distinctive
fact** about the leaf and the fact most easily lost in the middle of
a "cranial nerve nuclei" discussion:

*   **Dorsal root ganglion (DRG)** neurons — **peripheral** —
    primary afferents of the **spinal cord**.
*   **Trigeminal ganglion (semilunar / Gasserian)** — **peripheral** —
    primary afferents of the **main sensory trigeminal nucleus**
    (touch, pressure) and the **spinal trigeminal nucleus** (pain,
    temperature).
*   **Geniculate, inferior (petrosal), nodose, jugular** — **peripheral**
    — primary afferents of **CN VII, IX, X**.
*   **Vestibular and spiral ganglia** — **peripheral** — primary
    afferents of **CN VIII**.
*   **MesV** — **CENTRAL** — the **only exception**. The
    **pseudounipolar cell bodies** are **inside the CNS**, in the
    **midbrain tegmentum**. The **peripheral branch** goes to the
    **jaw muscle spindles** and **periodontal mechanoreceptors** via
    **V3**; the **central branch** goes to the **trigeminal motor
    nucleus** (pons) via the **mesencephalic tract of V**.

**This is a common exam point and a common consumer misconception.**
A consumer who says "the mesV is a trigeminal primary sensory
nucleus, so its cell bodies must be in the trigeminal ganglion" is
**wrong** — **mesV has no ganglion**; its cell bodies are **in the
nucleus itself**. A consumer who says "the main sensory and spinal
trigeminal nuclei are also primary sensory nuclei in the CNS" is
**also wrong** — their primary afferent cell bodies are in the
**trigeminal ganglion** (peripheral). **The mesV is the sole
exception.**

The Three Primary Sensory Trigeminal Nuclei (the sibling
disambiguation)
-------------------------------------------------------------------
The trigeminal system has **three primary sensory nuclei**,
distinguished by **modality** and **location**:

*   **Mesencephalic trigeminal nucleus (mesV)** — **THIS LEAF** —
    **proprioception** — **midbrain tegmentum** — **cell bodies in
    the nucleus itself** (the **only CNS primary sensory nucleus**).

*   **Main (principal / pontine) sensory trigeminal nucleus** — **NOT
    this leaf** — **touch and pressure** — **pons**
    (``.../hindbrain/metencephalon/pons/trigeminal_main_sensory_nucleus/``)
    — **cell bodies in the trigeminal ganglion** (peripheral).

*   **Spinal trigeminal nucleus** — **NOT this leaf** — **pain and
    temperature** — **pons + medulla**
    (``.../hindbrain/myencephalon/medulla_oblongata/spinal_trigeminal_nucleus/``)
    — **cell bodies in the trigeminal ganglion** (peripheral).

**A consumer must not conflate the three.** Each has a **distinct
modality**, a **distinct location**, and — critically — a **distinct
ganglion status**: mesV **is inside the CNS**; the main sensory and
spinal trigeminal nuclei **are not** (their primary afferents have
their cell bodies in the **peripheral trigeminal ganglion**).

The Jaw-Jerk Reflex (the circuit the mesV participates in)
----------------------------------------------------------
The **jaw-jerk reflex** (also called the **masseter reflex** or
**jaw jerk**) is a **monosynaptic stretch reflex** — one of the
**shortest reflex arcs in the body** — whose circuit is:

*   **Afferent limb:** **jaw muscle spindle primary afferents** (in
    the **masseter** and **temporalis**) → **mesV neurons** (their
    peripheral branches; cell bodies in the mesV).
*   **Central branch:** **mesV neurons** → **mesencephalic tract of
    V** → **trigeminal motor nucleus** (pons).
*   **Efferent limb:** **trigeminal motor nucleus** → **masseter** and
    **temporalis** (jaw-closing muscle contraction).
*   **Reflex response:** a **tap on the chin** (stretching the
    masseter) produces a **jaw-closing jerk** — the **jaw jerk**.

**The mesV is ONE COMPONENT of this circuit** — the **afferent limb's
cell bodies**. The **circuit itself** is a **physiological entity**,
not a structure. Consumers must **not** conflate the mesV with the
jaw-jerk reflex, and must **not** resolve the reflex through the mesV
path — the reflex is **prose**, not a structural child. The
**mesencephalic tract of V** is the **conduction pathway** carrying
the central branches; the **trigeminal motor nucleus** is the
**motor output** — **both are outside this leaf**.

The Left Mesencephalic Trigeminal Nucleus / Trigeminal Motor Nucleus Boundary
----------------------------------------------------------------------------
This is the **primary sensory / branchiomotor** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) — the
    **primary sensory (proprioceptive)** nucleus — **midbrain**.

*   **Left trigeminal motor nucleus (CN V motor)**
    (``.../hindbrain/metencephalon/pons/trigeminal_motor_nucleus/``)
    — the **branchiomotor** nucleus for the **muscles of mastication**
    — **pons**.

**They are DIFFERENT NUCLEI** in **DIFFERENT LOCATIONS** (midbrain vs.
pons) — the **motor** nucleus is **branchiomotor**; the **mesV** is
**primary sensory**. **They are CONNECTED** — the mesV's central
processes project to the motor nucleus for the **jaw-jerk reflex** —
but **connectivity is not identity**. Consumers must **not** conflate
the two, and must **not** resolve the trigeminal motor nucleus
through the mesV path.

The Left Mesencephalic Trigeminal Nucleus / Trigeminal Ganglion Boundary
----------------------------------------------------------------------
This is the **central / peripheral** boundary — the **defining**
boundary of the leaf:

*   **Left mesencephalic trigeminal nucleus** (this module) — the
    **only primary sensory nucleus in the CNS** — **cell bodies in
    the CNS** (midbrain).

*   **Left trigeminal (semilunar / Gasserian) ganglion** — the
    **peripheral sensory ganglion** — **cell bodies in the PNS** —
    for the **main sensory trigeminal nucleus** (touch, pressure) and
    the **spinal trigeminal nucleus** (pain, temperature).

**The mesV has NO ganglion** — its cell bodies are **in the nucleus
itself**. **They are DIFFERENT STRUCTURES across the CNS-PNS
boundary** — the **ganglion** is **peripheral**; the **mesV** is
**central**. Consumers must **not** conflate the two, and must **not**
assume mesV primary afferents have their cell bodies in the
trigeminal ganglion — they **do not**.

The Left Mesencephalic Trigeminal Nucleus / Main Sensory Trigeminal Nucleus Boundary
-----------------------------------------------------------------------------------
This is the **proprioceptive / touch-pressure** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) —
    **proprioceptive** — **midbrain**.

*   **Left main (principal / pontine) sensory trigeminal nucleus**
    (``.../hindbrain/metencephalon/pons/trigeminal_main_sensory_nucleus/``)
    — **touch and pressure** — **pons**.

**They are DIFFERENT NUCLEI** in **DIFFERENT LOCATIONS** processing
**DIFFERENT MODALITIES**. Consumers must **not** conflate the two,
and must **not** attribute **facial touch** or **pressure** function
to the mesV.

The Left Mesencephalic Trigeminal Nucleus / Spinal Trigeminal Nucleus Boundary
-----------------------------------------------------------------------------
This is the **proprioceptive / pain-temperature** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) —
    **proprioceptive** — **midbrain**.

*   **Left spinal trigeminal nucleus**
    (``.../hindbrain/myencephalon/medulla_oblongata/spinal_trigeminal_nucleus/``)
    — **pain and temperature** — **pons + medulla**.

**They are DIFFERENT NUCLEI** in **DIFFERENT LOCATIONS** processing
**DIFFERENT MODALITIES**. Consumers must **not** conflate the two,
and must **not** attribute **facial pain** or **temperature**
function to the mesV.

The Left Mesencephalic Trigeminal Nucleus / Mesencephalic Tract of V Boundary
----------------------------------------------------------------------------
This is the **nucleus / conduction pathway** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) — the
    **nucleus** — **grey matter** — the **cell bodies**.

*   **Left mesencephalic tract of V** — the **longitudinal fiber
    bundle** — **white matter** — the **axons** (central branches of
    the mesV neurons).

**They are DIFFERENT STRUCTURES** — the **nucleus** contains the
**cell bodies**; the **tract** contains the **axons**. The tract is a
**conduction pathway** (analogous to the `cerebral_peduncle`'s
conduction-pathway framing). Consumers must **not** conflate the
nucleus with the tract.

The Left Mesencephalic Trigeminal Nucleus / Trigeminal Nerve Boundary
---------------------------------------------------------------------
This is the **nucleus / peripheral nerve** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) — the
    **nucleus** — **CNS grey matter**.

*   **Left trigeminal nerve (CN V)** — the **peripheral axon bundle**
    — **PNS**.

**The mesV's peripheral branches travel IN the V3 division of the
trigeminal nerve** — but the **nerve** is **not the nucleus**.
**They are DIFFERENT STRUCTURES across the CNS-PNS boundary.**
Consumers must **not** conflate the two.

The Left Mesencephalic Trigeminal Nucleus / PAG and Lateral Lemniscus Boundary
-----------------------------------------------------------------------------
This is the **neighbor** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) — the
    **primary sensory (proprioceptive)** nucleus — **lateral
    midbrain tegmentum**.

*   **Left periaqueductal gray (PAG)**
    (``.../tegmentum/left/periaqueductal_gray/``) — the
    **pain-modulation and defensive-behavior** grey-matter region —
    **medial** to mesV.

*   **Left lateral lemniscus**
    (``.../hindbrain/metencephalon/pons/lateral_lemniscus/``) — the
    **auditory** ascending tract — **lateral** to mesV.

**They are DIFFERENT STRUCTURES in DIFFERENT functional systems.**
Consumers must **not** conflate the mesV with the PAG (pain
modulation) or with the lateral lemniscus (auditory conduction).

The Left Mesencephalic Trigeminal Nucleus / Locus Coeruleus and Dorsal Raphe Boundary
-----------------------------------------------------------------------------------
This is the **primary sensory / neuromodulatory** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) — the
    **primary sensory (proprioceptive)** nucleus.

*   **Locus coeruleus** (pons) and **dorsal raphe nucleus**
    (midbrain tegmentum) — **neuromodulatory nuclei** —
    **noradrenergic** and **serotonergic**, respectively.

**They are DIFFERENT STRUCTURES in DIFFERENT functional systems.**
The **noradrenergic** and **serotonergic** phenotypes are
``chemicals_hormones``-layer facts — **not** structural facts of
mesV. Consumers must **not** conflate the mesV with the locus
coeruleus or the dorsal raphe.

The Left Mesencephalic Trigeminal Nucleus / Right Mesencephalic Trigeminal Nucleus Boundary
-----------------------------------------------------------------------------------------
This is the **side** boundary:

*   **Left mesencephalic trigeminal nucleus** (this module) — the
    **left mesV**.

*   **Right mesencephalic trigeminal nucleus**
    (``.../cranial_nerve_nuclei/right/mesencephalic_trigeminal_nucleus/``
    **and** ``.../tegmentum/right/mesencephalic_trigeminal_nucleus/``)
    — the **right mesV**.

**They are STRICTLY SYMMETRIC SENSORY NUCLEI** — each is an
**independent primary sensory nucleus** for its side's jaw muscle
spindles and periodontal mechanoreceptors. **The BILATERAL jaw-jerk
response** in the clinic is produced by the **bilateral projection**
of each mesV to **both** trigeminal motor nuclei (via the
mesencephalic tract of V) — **not** by direct mesV-to-mesV coupling.
Consumers must **not** conflate the left mesV with the right mesV,
and must **not** assume the two are **directly coupled** — they are
**independent nuclei** whose **outputs** converge bilaterally on the
**trigeminal motor nuclei**.

Function in the Human Brain
---------------------------
The left mesencephalic trigeminal nucleus's function is
**proprioceptive sensing from the left jaw-closing muscles and the
left periodontal mechanoreceptors** — **NOT** touch or pressure from
the face, **NOT** pain or temperature from the face, **NOT** motor
control of the muscles of mastication:

*   **Jaw Proprioception (masseter and temporalis):** The left mesV
    receives **proprioceptive** input from the **muscle spindles** of
    the **left masseter** and **left temporalis**. These are the
    **primary afferents of the jaw-jerk reflex** — the **afferent
    limb's cell bodies**. When the jaw is **tapped downward** (or
    during **chewing**), the **masseter spindle afferents** fire,
    the mesV neurons fire, and the **mesencephalic tract of V**
    carries the signal **down** to the **left and right trigeminal
    motor nuclei**, producing **jaw-closing muscle contraction**.

*   **Periodontal Mechanoreception (dental pressure):** The left mesV
    receives **mechanoreceptive** input from the **periodontal
    mechanoreceptors** around the **left teeth** — the **sensors of
    bite force and dental pressure**. This input contributes to
    **jaw-closing force regulation** during biting and chewing.

*   **Possible Extraocular Muscle Proprioception (CONTESTED):** Some
    literature proposes that the mesV receives **proprioceptive**
    input from the **extraocular muscles** — but this is **contested**
    and remains an area of active investigation. It is documented as
    **prose** here, **not** as a structural child, and **not** as a
    settled functional claim.

*   **Possible Dental Pulp Innervation (CONTESTED):** Some literature
    proposes **dental pulp** innervation via mesV — **contested**,
    documented as **prose**.

*   **NOT facial touch or pressure.** Those are the **main sensory
    trigeminal nucleus** (pons).

*   **NOT facial pain or temperature.** Those are the **spinal
    trigeminal nucleus** (pons + medulla).

*   **NOT motor control of mastication.** That is the **trigeminal
    motor nucleus** (pons) — the **branchiomotor** pool for the
    muscles of mastication.

*   **NOT an oscillator.** The mesV is a **sensory nucleus** — it
    **fires in response to peripheral input** (muscle stretch,
    periodontal pressure). It does **not** generate a rhythm. Its
    **bilateral projection** to the trigeminal motor nuclei (via
    the mesencephalic tract of V) is **downstream** — **not**
    intrinsic mesV-to-mesV coupling.

**The unifying theme:** the left mesV is the **left primary
proprioceptive nucleus of the trigeminal system** — the **only
primary sensory nucleus in the CNS**. It is **proprioceptive**
(**NOT touch/pressure**, **NOT pain/temperature**), it is the
**afferent limb's cell bodies** of the **jaw-jerk reflex** (**NOT
the reflex itself**), and it is a **sensory nucleus** in the family's
taxonomy — **NO coupling warning** (same rule as motor nuclei,
premotor pools, and conduction pathways).

Associated Disorders
--------------------
The left mesencephalic trigeminal nucleus has **no named syndrome of
its own** — the trigeminal disorders that are famous clinically
(**trigeminal neuralgia**, **anesthesia dolorosa**) are **not**
mesV lesions. Its clinical associations are **rare and indirect**:

*   **Absent or Diminished Jaw Jerk (INDIRECT — via a mesV lesion,
    rare):** A **lesion of the mesV** — from **small infarction**,
    **demyelination** (e.g., **multiple sclerosis**), or **tumor** —
    would produce an **absent or diminished jaw jerk** on the
    **left** side (or bilaterally if the lesion involves the
    bilateral projections to the trigeminal motor nuclei, or if the
    trigeminal motor nucleus is also involved). **This is rare in
    isolation** — the jaw jerk is more commonly affected by
    **bilateral cortical or corticobulbar lesions** (producing
    **hyperreflexia** of the jaw jerk — **UMN** pattern) or by
    **trigeminal motor nucleus / nerve** lesions (producing
    **hyporeflexia** — **LMN** pattern). **An isolated mesV lesion
    producing isolated jaw-jerk hyporeflexia is RARE.**

*   **Trigeninal Neuralgia (NOT a MesV Lesion — the trigeminal
    NERVE / root entry zone):** **Trigeninal neuralgia** — paroxysmal,
    lancinating **facial pain** in the distribution of **V2** or
    **V3** — is caused by **vascular compression of the trigeminal
    nerve root entry zone** (often by the **superior cerebellar
    artery**) at the **pons**, or by **demyelination** of the
    **trigeminal nerve root** (e.g., in **multiple sclerosis**).
    **The mesV is NOT the lesion site** — the mesV is a
    **proprioceptive** nucleus, **not** a **pain** nucleus.
    **Trigeninal neuralgia is NOT a mesV disorder** — the pain
    **primary afferents** have their cell bodies in the **trigeminal
    ganglion** (peripheral), not in mesV.

*   **Anesthesia Dolorosa (NOT a MesV Lesion — post-trigeminal
    deafferentation):** **Anesthesia dolorosa** — **anesthesia** in
    the face **accompanied by constant burning pain** — is a
    **deafferentation syndrome** following **trigeminal nerve
    damage** (from surgery, trauma, or tumor), typically involving
    the **trigeminal ganglion or nerve** — **NOT the mesV**.

*   **Trigeninal Neuropathy (NOT a MesV Lesion — the trigeminal
    NERVE):** **Trigeninal neuropathy** — sensory loss in the
    trigeminal distribution (often **V2** and **V3**) — is a
    **trigeminal nerve / ganglion** lesion (e.g., **tumor**,
    **inflammation**, **connective tissue disease**) — **NOT a mesV
    lesion**.

*   **Jaw-Jerk Hyperreflexia (NOT a MesV Lesion — CORTICAL / UMN):**
    **Bilateral jaw-jerk hyperreflexia** is a **corticobulbar (UMN)**
    sign — it reflects **loss of cortical inhibition** of the
    trigeminal motor nucleus, typically from **bilateral cortical or
    corticobulbar lesions** — **NOT a mesV lesion**.

*   **Isolated MesV Lesion (RARE — NO NAMED SYNDROME):** A **focal
    lesion** of the **left mesV** — from **small infarction**,
    **demyelination**, or **tumor** — would produce **left
    jaw-jerk hyporeflexia** and possibly **impaired jaw
    proprioception**, **without** facial touch/pain loss (those are
    the main sensory and spinal trigeminal nuclei). This is **rare
    in practice** — most trigeminal clinical syndromes are **nerve**
    or **ganglion** lesions, not **mesV nucleus** lesions. **No
    named mesV syndrome exists.**

*   **MS Plaques (INDIRECT — mesV can be involved):** **Multiple
    sclerosis** plaques can occur **anywhere in the CNS**, including
    the **mesV** — producing **jaw-jerk abnormalities** as part of a
    **broader MS presentation**. This is **indirect** — the mesV is
    **not** a named MS site.

*   **No Named "Mesencephalic Trigeminal Nucleus Syndrome":** The
    left mesV is a **primary sensory nucleus** — it has **no named
    syndrome of its own**. Its clinical relevance is **rare and
    indirect**, via **jaw-jerk abnormalities** and **jaw
    proprioceptive deficits** in focal lesions (rare) or as part of
    **broader MS / demyelinating disease**.

**What is NOT here:** The left mesV is **not** the substrate for
**trigeminal neuralgia** (trigeminal nerve / root entry zone —
**NOT** mesV), **anesthesia dolorosa** (trigeminal nerve / ganglion
deafferentation — **NOT** mesV), **trigeminal neuropathy**
(trigeminal nerve / ganglion — **NOT** mesV), **jaw-jerk
hyperreflexia** (cortical / UMN — **NOT** mesV), **facial
touch/pressure loss** (main sensory trigeminal nucleus — **pons**),
**facial pain/temperature loss** (spinal trigeminal nucleus — **pons
+ medulla**), **masticatory weakness** (trigeminal motor nucleus —
**pons**), **Benedikt syndrome** (tegmentum — red nucleus + CN III),
**Claude syndrome** (tegmentum — red nucleus + CN III), **Weber
syndrome** (crus cerebri — CN III fascicles),
**Parinaud syndrome** (dorsal midbrain — tectum / pretectum),
**Nothnagel syndrome** (tectum / colliculi), **Millard-Gubler
syndrome** (pons), **Wallenberg syndrome** (lateral medulla),
**locked-in syndrome** (basis pontis), **CCHS** (RTN), **OIRD**
(pre-Bötzinger complex — NK1R neurons), **Rett syndrome**
(pre-Bötzinger complex), **SIDS** (proposed — pre-Bötzinger complex
+ arcuate nucleus), **essential hypertension / sympathetic
overactivity** (C1 group / RVLM), **Parkinson's disease**
(substantia nigra — tegmentum), **Huntington's disease** (striatum
— telencephalon), or **Kluver-Bucy syndrome** (amygdala). Its
clinical relevance is **rare and indirect**, via **jaw-jerk
abnormalities** and **jaw proprioceptive deficits** in focal lesions
(rare) or **demyelinating disease**. **No named mesV syndrome
exists.**

Lateralization Notes
--------------------
This is the **left** mesencephalic trigeminal nucleus leaf. The left
and right mesV are **bilaterally symmetric** and carry **NO coupling
warning of their own** — and they **inherit no warning from any
oscillator**:

*   **Bilateral Independent Sensory Nuclei:** Each hemisphere has
    its own mesV — each is an **independent primary sensory nucleus**
    receiving **proprioceptive** input from **its own side's** jaw
    muscle spindles and periodontal mechanoreceptors.

*   **NO Coupling Warning (the coupling warning attaches to
    OSCILLATORS, not to SENSORY NUCLEI):** The **pre-Bötzinger
    complex** carries a **coupling warning** because it is an
    **oscillator** whose two sides must synchronize to produce a
    single rhythm. The **left mesV** is a **sensory nucleus** — it
    **fires in response to peripheral input**, and it does **not**
    generate a rhythm, so it does **not** carry the **oscillator
    coupling warning**. Its **left** and **right** sides are
    **independent nuclei** — there is **no** mesV-to-mesV coupling.
    **The BILATERAL jaw-jerk response** in the clinic is produced by
    the **bilateral projection** of each mesV to **both** trigeminal
    motor nuclei (via the **mesencephalic tract of V**) — **not** by
    direct **mesV-to-mesV** coupling. **Sensory nuclei carry NO
    coupling warning** — same rule as motor nuclei, premotor pools,
    and conduction pathways.

*   **Clinical Laterality — few named syndromes:**
    *   A **left mesV lesion** → **left jaw-jerk hyporeflexia** and
        possibly **left jaw proprioceptive impairment** — **without**
        facial touch/pain loss (those are main sensory and spinal
        trigeminal nuclei). **Rare in isolation**, no named
        syndrome.
    *   A **left trigeminal nerve / ganglion lesion** → **left
        facial sensory loss** (touch/pressure/pain/temperature) —
        **NOT a mesV lesion**.
    *   A **left trigeminal motor nucleus lesion** → **left
        masticatory weakness** — **NOT a mesV lesion**.
    *   **Bilateral corticobulbar (UMN) lesions** → **bilateral
        jaw-jerk hyperreflexia** — **NOT a mesV lesion**.
    *   **A consumer that assumes "left mesV = right mesV" will be
        structurally correct** (the two are symmetric), but a
        consumer that assumes a **left mesV lesion** produces the
        same clinical picture as a **left trigeminal nerve lesion**
        is **wrong** — the mesV is **proprioceptive**, not
        **touch/pain**, and the **two patterns** are **distinct**.

**The left mesencephalic trigeminal nucleus is a strict mirror pair
with the right mesV — no coupling warning, no SLEA warning, no
amygdala-lateralization warning, and no rhinencephalon-exclusion
flag** — **but with two crucial caveats**: (1) the **bilateral
jaw-jerk response** is produced by **bilateral projection** to the
**trigeminal motor nuclei**, not by mesV-to-mesV coupling; (2) the
**clinical patterns** of left mesV lesions, left trigeminal nerve
lesions, left trigeminal motor nucleus lesions, and bilateral UMN
lesions are **distinct** — the mesV is **proprioceptive**, and its
lesions produce **jaw-jerk and proprioceptive** findings, **not**
facial sensory or motor deficits.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only — **no** import
    from ``.../right/mesencephalic_trigeminal_nucleus/``.
*   **No cross-lobe imports.** This module does **not** import from
    the **trigeminal ganglion**, the **trigeminal nerve**, the
    **trigeminal motor nucleus**, the **main sensory trigeminal
    nucleus**, the **spinal trigeminal nucleus**, the
    **mesencephalic tract of V**, the **lateral lemniscus**, the
    **PAG**, the **locus coeruleus**, the **dorsal raphe nucleus**,
    or any other container. The left mesV's relationships to the
    trigeminal ganglion, the trigeminal nerve, the trigeminal motor
    nucleus, the main sensory trigeminal nucleus, the spinal
    trigeminal nucleus, the mesencephalic tract of V, the lateral
    lemniscus, the PAG, the locus coeruleus, the dorsal raphe
    nucleus, and the right mesV are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``. The
    **noradrenergic** and **serotonergic** phenotypes of the locus
    coeruleus and the dorsal raphe nucleus are
    ``chemicals_hormones``-layer facts — **not** structural facts of
    mesV, documented as **prose**, **never imported**.
*   **DUAL-PARENT LEAF — CROSS-LISTED between
    ``cranial_nerve_nuclei/left/`` and ``tegmentum/left/``.** Both
    paths resolve to **this module**.
*   **CROSS-LISTING via ``AREA_PATHS``.** The leaf is cross-listed
    between the functional container (``cranial_nerve_nuclei/``) and
    the topographic container (``tegmentum/``). Consumers resolving
    by **either** path get **this module**.
*   **CONSISTENT with the ``cranial_nerve_nuclei/``,
    ``cranial_nerve_nuclei/left/``, and ``midbrain`` container child
    lists.** The CN nuclei are placed under ``tegmentum/``
    (topographic home) **and** cross-listed under
    ``cranial_nerve_nuclei/`` (functional grouping). This leaf is
    the **left-side mesV** slice of that cross-listing.
*   **THE ONLY PRIMARY SENSORY NUCLEUS IN THE CNS.** Every other
    primary sensory nucleus has its primary afferent cell bodies in
    a **peripheral ganglion**. The **mesV is the sole exception**.
    Consumers must **not** conflate mesV with the main sensory
    trigeminal nucleus or the spinal trigeminal nucleus — **those
    have primary afferent cell bodies in the trigeminal ganglion**.
*   **PROPRIOCEPTIVE — NOT touch/pressure, NOT pain/temperature.**
    The **touch/pressure** nucleus is the **main sensory trigeminal
    nucleus** (pons); the **pain/temperature** nucleus is the
    **spinal trigeminal nucleus** (pons + medulla). The **mesV is
    proprioceptive**.
*   **SENSORY NUCLEUS — NOT a motor nucleus, NOT an oscillator, NOT
    a premotor pool, NOT a conduction pathway.** It is the first
    **sensory nucleus** in the midbrain CN group.
*   **NO coupling warning — sensory nuclei carry NO coupling
    warning.** Same rule as motor nuclei, premotor pools, and
    conduction pathways. The **bilateral jaw-jerk response** is
    produced by **bilateral projection** to the **trigeminal motor
    nuclei** — **not** by mesV-to-mesV coupling.
*   **NOT the trigeminal motor nucleus.** The motor nucleus is the
    **branchiomotor** pool for mastication — **pons**. The mesV is
    **primary sensory** — **midbrain**.
*   **NOT the trigeminal ganglion.** The ganglion is **peripheral**.
    The mesV is the **only** primary sensory nucleus whose cell
    bodies are **in the CNS**.
*   **NOT the mesencephalic tract of V.** The tract is the
    **conduction pathway** (axons of the mesV neurons); the nucleus
    contains the **cell bodies**.
*   **NOT the trigeminal nerve.** The nerve is the **peripheral**
    axon bundle; the mesV is the **nucleus**.
*   **NOT the jaw-jerk reflex.** The reflex is the **circuit**; the
    mesV is **one component** — the afferent limb's cell bodies.
*   **NOT the PAG, the lateral lemniscus, the locus coeruleus, or the
    dorsal raphe.** Those are **neighbors** in **different
    functional systems**.
*   **SIDE-CONSISTENT — this leaf is the LEFT mesV.**
*   **MIRROR PARITY with ``.../right/mesencephalic_trigeminal_nucleus/``
    — strict mirror with NO warning.**
*   **SLEA-FREE — no extended-amygdala relationship.**
*   **No ``AREA_PATHS`` hop into other lobes.** The cross-listing is
    **within the midbrain** (``tegmentum/left`` ↔
    ``cranial_nerve_nuclei/left``) — not into the forebrain,
    hindbrain, or periphery. The **trigeminal motor nucleus**,
    **trigeminal ganglion**, **trigeminal nerve**, **main sensory
    trigeminal nucleus**, **spinal trigeminal nucleus**, and
    **mesencephalic tract of V** are **separate structures**
    referenced as **prose**, not as cross-listed parents.
*   **No nested cross-listing.** This is a **single dual-parent
    leaf**. It is **not** a container.
*   **The on-disk tree is authoritative.**

Usage
-----
Resolve the leaf by **either** path (they are equivalent — **this is
a dual-parent anchor**)::

    # Functional path (clinician framing):
    from infrastructure.brainparts.midbrain.cranial_nerve_nuclei.left import mesencephalic_trigeminal_nucleus

    # Topographic path (anatomist framing):
    from infrastructure.brainparts.midbrain.tegmentum.left import mesencephalic_trigeminal_nucleus

Or by fully-qualified path string::

    functional_path = (
        "midbrain.cranial_nerve_nuclei.left.mesencephalic_trigeminal_nucleus"
    )
    topographic_path = (
        "midbrain.tegmentum.left.mesencephalic_trigeminal_nucleus"
    )
    # Both resolve to THIS module.

**Do not** assume the two paths lead to **different structures** —
they lead to **one leaf**, **dual-parented**.

**Do not** assume the left mesV is the **main sensory trigeminal
nucleus** or the **spinal trigeminal nucleus**. Those are **pons** or
**pons + medulla** structures, processing **touch/pressure** (main
sensory) and **pain/temperature** (spinal). The **mesV is
proprioceptive**, in the **midbrain**.

**Do not** assume the left mesV's primary afferents have their cell
bodies in the **trigeminal ganglion**. The **mesV is the sole
exception** — its **cell bodies are in the nucleus itself** (in the
CNS). The **main sensory** and **spinal trigeminal** nuclei **do**
have their primary afferent cell bodies in the **trigeminal
ganglion** — but the **mesV does not**.

**Do not** assume the left mesV is the **trigeminal motor nucleus**.
The **motor nucleus** is the **branchiomotor** pool for mastication
— **pons**. The mesV is **primary sensory** — **midbrain**. They are
**connected** (mesV projects to the motor nucleus for the jaw-jerk)
but **different structures**.

**Do not** assume the left mesV is the **mesencephalic tract of V**.
The **tract** is the **conduction pathway** (axons); the **nucleus**
contains the **cell bodies**.

**Do not** assume the left mesV is the **trigeminal nerve**. The
**nerve** is the **peripheral** axon bundle; the mesV is the
**nucleus**. The mesV's **peripheral branches** travel in **V3** —
but the **nerve** is not the **nucleus**.

**Do not** assume the left mesV is the **jaw-jerk reflex**. The
**reflex** is the **circuit**; the mesV is **one component** — the
afferent limb's cell bodies.

**Do not** conflate the left mesV with the **left PAG**, the **left
lateral lemniscus**, the **locus coeruleus**, or the **dorsal raphe
nucleus** — those are **neighbors** in **different functional
systems**.

**Do not** attribute **facial touch/pressure**, **facial
pain/temperature**, or **masticatory weakness** to the left mesV.
Those are **main sensory trigeminal nucleus**, **spinal trigeminal
nucleus**, and **trigeminal motor nucleus** functions,
respectively — **NOT** mesV functions.

**Do not** import the **noradrenergic** or **serotonergic**
phenotypes of the locus coeruleus or the dorsal raphe nucleus into
the midbrain structural layer. Those are
**``chemicals_hormones``-layer facts**.

**Do not** import a **coupling warning** into the left mesV.
**Sensory nuclei carry NO coupling warning** — same rule as motor
nuclei, premotor pools, and conduction pathways. **The bilateral
jaw-jerk response is produced by bilateral projection to the
trigeminal motor nuclei, not by mesV-to-mesV coupling.**

Iterating the left mesV's (empty) children (recommended consumer
pattern)::

    MESENCEPHALIC_TRIGEMINAL_NUCLEUS_LEFT_CHILDREN = ()
    # The left mesencephalic trigeminal nucleus is a leaf. The
    # primary afferent fibers (from jaw muscle spindles, periodontal
    # mechanoreceptors, and possibly extraocular muscle proprioceptors)
    # are prose — they are the peripheral branches of the mesV
    # neurons (pseudounipolar cells have one process that bifurcates
    # into a peripheral and a central branch), not structural
    # children.

Reaching the **functional parent** (``cranial_nerve_nuclei/left/``)::

    # The functional parent is the left side container of the
    # cranial_nerve_nuclei functional grouping:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left
    #
    # The left mesV is a child of BOTH the functional parent and the
    # topographic parent (see below).

Reaching the **topographic parent** (``tegmentum/left/``)::

    # The topographic parent is the left side container of the
    # tegmentum topographic container — the SUPERSET:
    #
    #   brainparts.midbrain.tegmentum.left
    #
    # The left mesV is a child of BOTH the topographic parent and the
    # functional parent (see above).

Reaching the left trigeminal motor nucleus (recommended consumer
pattern — the CN V MOTOR nucleus)::

    # The left trigeminal motor nucleus is the CN V BRANCHIOMOTOR
    # nucleus — muscles of mastication:
    #
    #   brainparts.hindbrain.metencephalon.pons.trigeminal_motor_nucleus
    #
    # The left trigeminal motor nucleus is BRANCHIOMOTOR; the left
    # mesV is PRIMARY SENSORY. They are DIFFERENT NUCLEI in
    # DIFFERENT LOCATIONS (pons vs. midbrain). The mesV PROJECTS TO
    # the motor nucleus for the jaw-jerk reflex.

Reaching the left main sensory trigeminal nucleus (recommended
consumer pattern — the CN V TOUCH/PRESSURE nucleus)::

    # The left main (principal / pontine) sensory trigeminal nucleus
    # is the CN V TOUCH/PRESSURE nucleus — pons:
    #
    #   brainparts.hindbrain.metencephalon.pons.trigeminal_main_sensory_nucleus
    #
    # The left main sensory trigeminal nucleus processes TOUCH and
    # PRESSURE. The left mesV processes PROPRIOCEPTION. They are
    # DIFFERENT NUCLEI processing DIFFERENT MODALITIES. The main
    # sensory nucleus's primary afferent cell bodies are in the
    # trigeminal ganglion; the mesV's are in the mesV itself.

Reaching the left spinal trigeminal nucleus (recommended consumer
pattern — the CN V PAIN/TEMPERATURE nucleus)::

    # The left spinal trigeminal nucleus is the CN V PAIN/TEMPERATURE
    # nucleus — pons + medulla:
    #
    #   brainparts.hindbrain.myencephalon.medulla_oblongata.spinal_trigeminal_nucleus
    #
    # The left spinal trigeminal nucleus processes PAIN and
    # TEMPERATURE. The left mesV processes PROPRIOCEPTION. They are
    # DIFFERENT NUCLEI processing DIFFERENT MODALITIES.

Reaching the trigeminal ganglion (recommended consumer pattern — the
PERIPHERAL ganglion, NOT the mesV)::

    # The trigeminal (semilunar / Gasserian) ganglion is the
    # PERIPHERAL sensory ganglion — the primary afferent cell bodies
    # for the MAIN SENSORY TRIGEMINAL NUCLEUS and the SPINAL
    # TRIGEMINAL NUCLEUS:
    #
    #   peripheral.trigeminal_ganglion
    #
    # The mesV has NO ganglion — its cell bodies are in the NUCLEUS
    # itself. This is the ONLY primary sensory nucleus in the CNS.

Reaching the mesencephalic tract of V (recommended consumer pattern —
the CONDUCTION PATHWAY, NOT a nucleus)::

    # The mesencephalic tract of V (mesencephalic root of the
    # trigeminal nerve) is the LONGITUDINAL FIBER BUNDLE formed by
    # the CENTRAL BRANCHES of the mesV neurons — the axons that
    # travel DOWN from the midbrain mesV to the trigeminal motor
    # nucleus in the pons:
    #
    #   brainparts.midbrain.tegmentum.left.mesencephalic_tract_of_v
    #
    # The mesencephalic tract of V is a CONDUCTION PATHWAY; the mesV
    # is a NUCLEUS (cell bodies). They are DIFFERENT STRUCTURES.

Reaching the trigeminal nerve (recommended consumer pattern — the
PERIPHERAL bundle, NOT the mesV)::

    # The trigeminal nerve (CN V) is the PERIPHERAL axon bundle — the
    # mandibular division (V3) carries the PERIPHERAL BRANCHES of the
    # mesV neurons to the jaw muscle spindles and periodontal
    # mechanoreceptors:
    #
    #   peripheral.cranial_nerves.trigeminal
    #
    # The mesV's peripheral branches travel IN V3, but the nerve is
    # NOT the nucleus.

Reaching the right mesV (recommended consumer pattern — the SIDE
mirror)::

    # The right mesencephalic trigeminal nucleus is the RIGHT mesV:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.right.mesencephalic_trigeminal_nucleus
    #   OR: brainparts.midbrain.tegmentum.right.mesencephalic_trigeminal_nucleus
    #
    # The two mesV are STRICTLY SYMMETRIC and INDEPENDENT. The
    # BILATERAL jaw-jerk response is produced by BILATERAL
    # PROJECTION of each mesV to BOTH trigeminal motor nuclei —
    # NOT by mesV-to-mesV coupling.

Reaching the left oculomotor nucleus (recommended consumer pattern —
the CN III SOMATIC nucleus, sibling)::

    # The left oculomotor nucleus is the CN III SOMATIC MOTOR
    # nucleus — extraocular muscles and levator palpebrae:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.oculomotor_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.oculomotor_nucleus
    #
    # The left oculomotor nucleus is SOMATIC MOTOR; the left mesV is
    # PRIMARY SENSORY (proprioceptive). They are DIFFERENT NUCLEI in
    # DIFFERENT functional systems.

Reaching the left trochlear nucleus (recommended consumer pattern —
the CN IV SOMATIC nucleus, sibling)::

    # The left trochlear nucleus is the CN IV SOMATIC MOTOR nucleus
    # — superior oblique:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.trochlear_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.trochlear_nucleus
    #
    # The left trochlear nucleus is SOMATIC MOTOR; the left mesV is
    # PRIMARY SENSORY (proprioceptive). They are DIFFERENT NUCLEI in
    # DIFFERENT functional systems.

Reaching the left Edinger-Westphal nucleus (recommended consumer
pattern — the CN IIIp PARASYMPATHETIC nucleus, sibling)::

    # The left Edinger-Westphal nucleus is the CN III PREGANGLIONIC
    # PARASYMPATHETIC nucleus — pupil and lens:
    #
    #   brainparts.midbrain.cranial_nerve_nuclei.left.edinger_westphal_nucleus
    #   OR: brainparts.midbrain.tegmentum.left.edinger_westphal_nucleus
    #
    # The left Edinger-Westphal nucleus is PREGANGLIONIC
    # PARASYMPATHETIC; the left mesV is PRIMARY SENSORY
    # (proprioceptive). They are DIFFERENT NUCLEI in DIFFERENT
    # functional systems.

Bilateral iteration (recommended consumer pattern — NOTE the
no-coupling-warning rule and the bilateral jaw-jerk mechanism)::

    for side in ("left", "right"):
        for nucleus in (
            "oculomotor_nucleus",
            "trochlear_nucleus",
            "mesencephalic_trigeminal_nucleus",
            "edinger_westphal_nucleus",
        ):
            # Either path resolves to the same leaf — use ONE:
            path = (
                f"midbrain.cranial_nerve_nuclei.{side}.{nucleus}"
            )
            # OR:
            # path = f"midbrain.tegmentum.{side}.{nucleus}"
            #
            # resolve path through the memory/recall layer
            #
            # NOTE: the CN nuclei are MOTOR NUCLEI (CN III, CN IV),
            # a SENSORY NUCLEUS (CN Vm), and a PREGANGLIONIC
            # PARASYMPATHETIC NUCLEUS (Edinger-Westphal). NONE
            # carries a coupling warning. The BILATERAL jaw-jerk
            # response is produced by BILATERAL PROJECTION of each
            # mesV to BOTH trigeminal motor nuclei — not by
            # mesV-to-mesV coupling.

Jaw-jerk-reflex detail (not wired — consult references)::

    # The jaw-jerk reflex (masseter reflex) — the mesV is the
    # AFFERENT limb's cell bodies:
    #
    #   tap on chin -> masseter spindle stretches ->
    #   mesV peripheral branch (V3) -> mesV cell body (midbrain) ->
    #   mesencephalic tract of V (central branch) ->
    #   trigeminal motor nucleus (pons) ->
    #   masseter and temporalis contraction -> jaw closes (jerk)
    #
    # The mesV projects BILATERALLY to BOTH trigeminal motor nuclei
    # — this is why the jaw-jerk response is usually BILATERAL in
    # the clinic. The two mesV are NOT directly coupled.
    #
    # Do not attempt to resolve the trigeminal motor nucleus, the
    # mesencephalic tract of V, or the masseter as sub-paths of the
    # mesV — they are DIFFERENT structures, and the mesV is ONLY
    # the afferent limb's cell bodies.

Trigeninal-primary-sensory-nuclei detail (not wired — consult
references)::

    # The trigeminal system has THREE primary sensory nuclei, by
    # modality:
    #
    #   mesencephalic trigeminal nucleus  -> PROPRIOCEPTION  ->
    #                                         MIDBRAIN  -> cell
    #                                         bodies in the NUCLEUS
    #                                         (only CNS primary
    #                                         sensory nucleus)
    #   main (principal / pontine) sensory-> TOUCH/PRESSURE -> PONS
    #     trigeminal nucleus                  -> cell bodies in the
    #                                         TRIGEMINAL GANGLION
    #   spinal trigeminal nucleus         -> PAIN/TEMPERATURE ->
    #                                         PONS + MEDULLA ->
    #                                         cell bodies in the
    #                                         TRIGEMINAL GANGLION
    #
    # The MESV is the ONLY one whose cell bodies are in the CNS.
    #
    # Do not conflate these three — they process DIFFERENT
    # MODALITIES and are in DIFFERENT LOCATIONS with DIFFERENT
    # ganglion status.

Clinical-pattern detail (not wired — consult references)::

    # The left mesV is the LEFT PRIMARY PROPRIOCEPTIVE nucleus of the
    # trigeminal system. The CLINICAL PATTERNS of the related lesions
    # are DISTINCT:
    #
    #   left mesV lesion                -> left jaw-jerk
    #                                       HYPOreflexia (rare);
    #                                       possible left jaw
    #                                       proprioceptive
    #                                       impairment; NO facial
    #                                       touch/pain loss
    #   left trigeminal nerve lesion    -> left facial sensory loss
    #     (V1/V2/V3)                        (touch/pressure/pain/
    #                                       temperature) + left
    #                                       masticatory weakness if
    #                                       motor V involved; NOT
    #                                       a mesV lesion
    #   left trigeminal motor nucleus   -> left masticatory
    #     lesion                            weakness; NOT a mesV
    #                                       lesion
    #   bilateral corticobulbar (UMN)   -> BILATERAL jaw-jerk
    #     lesion                            HYPERreflexia; NOT a
    #                                       mesV lesion
    #   trigeminal neuralgia            -> paroxysmal facial PAIN
    #     (trigeminal nerve root             (V2/V3); NOT a mesV
    #      entry zone)                        lesion
    #
    # Do not conflate these patterns — they localize to DIFFERENT
    # STRUCTURES.

References
----------
*   **Canonical mesV anatomy:** Brodal, A. (2010). *The Central
    Nervous System: Structure and Function*, 4th ed. (The
    mesencephalic trigeminal nucleus — the only primary sensory
    nucleus in the CNS; its pseudounipolar cell bodies, its
    peripheral branches via V3, its central branches via the
    mesencephalic tract of V.)
*   **Trigeminal system organization:** Usunoff, K.G., Marani, E.,
    Schoen, J.H.R. (2006). *The Trigeminal System in Man*. (The
    three primary sensory trigeminal nuclei — mesencephalic, main
    sensory, spinal — distinguished by modality and location; the
    mesV's unique CNS cell body placement.)
*   **MesV and the jaw-jerk reflex:** Lund, J.P., Olsson, K.A.
    (1983). "The importance of reflexes and their descending
    control during jaw movement." *Trends in Neurosciences*
    6:458–463. (The jaw-jerk reflex — the mesV as the afferent
    limb's cell bodies, its bilateral projection to the trigeminal
    motor nuclei.)
*   **MesV and jaw muscle proprioception:** Rokx, J.T.M., van
    Willigen, J.D., Jansen, H.W.B. (1985). "Muscle fibre types and
    muscle spindles of the rat masseter muscle." *Archives of Oral
    Biology* 30:781–785. (The masseter muscle spindles — the source
    of mesV proprioceptive input.)
*   **MesV and periodontal mechanoreception:** Trulsson, M.,
    Johansson, R.S. (2002). "Orofacial mechanoreceptors in humans:
    encoding of forces during biting." *Experimental Brain Research*
    147:1–14. (The periodontal mechanoreceptors — their input via
    mesV, and their contribution to jaw-closing force regulation.)
*   **MesV and possible extraocular proprioception (contested):**
    Büttner-Ennever, J.A. (2006). *Neuroanatomy of the Oculomotor
    System*. (The hypothesis that mesV receives extraocular muscle
    proprioceptive input — CONTESTED and remains under active
    investigation.)
*   **MesV and dental pulp (contested):** Byers, M.R., Närhi, M.V.O.
    (1999). "Dental injury models: experimental tools for
    understanding nociceptive and neuropeptide mechanisms."
    *Critical Reviews in Oral Biology & Medicine* 10:4–39. (The
    possibility that mesV receives dental pulp afferent input —
    CONTESTED, and documented as prose.)
*   **Trigeminal neuralgia (contrast — NOT mesV):** Jannetta, P.J.
    (1967). "Arterial compression of the trigeminal nerve at the
    pons in patients with trigeminal neuralgia." *Journal of
    Neurosurgery* 26:159–162. (Trigeminal neuralgia as a vascular
    compression of the trigeminal nerve root entry zone — NOT a
    mesV lesion.)
*   **Anesthesia dolorosa (contrast — NOT mesV):** Sweet, W.H.
    (1984). "Deafferentation pain." In *Advances in Pain Research
    and Therapy* (Bonica, ed.). (Anesthesia dolorosa as a
    deafferentation syndrome following trigeminal nerve / ganglion
    damage — NOT a mesV lesion.)
*   **Main sensory trigeminal nucleus (contrast — pons):** Capra,
    N.F., Dessem, D. (1992). "Central connections of trigeminal
    primary afferent neurons: topographical and functional
    considerations." *Critical Reviews in Oral Biology & Medicine*
    4:1–52. (The main sensory trigeminal nucleus as the touch/
    pressure nucleus — PONS; its primary afferent cell bodies in
    the trigeminal ganglion.)
*   **Spinal trigeminal nucleus (contrast — pons + medulla):**
    Dubner, R., Sessle, B.J., Storey, A.T. (1978). *The Neural
    Basis of Oral and Facial Function*. (The spinal trigeminal
    nucleus as the pain/temperature nucleus — PONS + MEDULLA; its
    primary afferent cell bodies in the trigeminal ganglion.)
*   **Trigeminal ganglion (contrast — peripheral):** Young, R.F.
    (2001). "Unmyelinated primary afferents in the trigeminal
    system." In *Neurobiology of Spinal Cord Injury* (Patterson &
    Young, eds.). (The trigeminal ganglion as the peripheral
    sensory ganglion for the main sensory and spinal trigeminal
    nuclei — contrast with the mesV, which has NO ganglion.)
*   **Mesencephalic tract of V (contrast — conduction pathway):**
    Olszewski, J. (1950). "On the anatomical and functional
    organization of the spinal trigeminal nucleus." *Journal of
    Comparative Neurology* 92:401–413. (The mesencephalic tract of
    V as the longitudinal fiber bundle formed by the central
    branches of mesV neurons — a CONDUCTION PATHWAY, contrast with
    the nucleus.)
*   **Trigeninal motor nucleus (contrast — pons):** Mizuno, N.,
    Konishi, A., Sato, M. (1975). "Localization of masticatory
    motoneurons in the cat and rat by means of retrograde axonal
    transport of horseradish peroxidase." *Journal of Comparative
    Neurology* 164:105–115. (The trigeminal motor nucleus as the
    branchiomotor pool for mastication — PONS; the efferent limb
    of the jaw-jerk reflex.)
*   **PAG (contrast — neighbor):** Behbehani, M.M. (1995).
    "Functional characteristics of the midbrain periaqueductal
    gray." *Progress in Neurobiology* 46:575–605. (The PAG as the
    pain-modulation and defensive-behavior structure — MEDIAL to
    mesV; a different functional system.)
*   **Lateral lemniscus (contrast — neighbor):** Oliver, D.L.,
    Huerta, M.F. (1992). "Inferior and superior colliculi." In
    *The Mammalian Auditory Pathway* (Webster et al., eds.). (The
    lateral lemniscus as the auditory ascending tract — LATERAL to
    mesV; a different functional system.)
*   **Locus coeruleus and dorsal raphe (contrast — neuromodulatory
    nuclei):** Foote, S.L., Bloom, F.E., Aston-Jones, G. (1983).
    "Nucleus locus ceruleus: new evidence of anatomical and
    physiological specificity." *Physiological Reviews*
    63:844–914. (The locus coeruleus — noradrenergic arousal —
    NOT mesV; its noradrenergic phenotype is a
    chemicals_hormones-layer fact.)
*   **SLEA (contrast — the left mesV is not SLEA):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; **NOT**
    the mesV.)
*   NeuroNames — Mesencephalic trigeminal nucleus (left); FMA —
    Mesencephalic nucleus of the trigeminal nerve (left member).
"""