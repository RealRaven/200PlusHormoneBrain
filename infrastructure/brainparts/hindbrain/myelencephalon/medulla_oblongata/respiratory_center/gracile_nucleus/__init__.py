"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus
=======================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── gracile_nucleus   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Gracile nucleus; nucleus gracilis; nucleus of
Goll; Goll's nucleus; dorsal column nucleus (lower body).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**dorsal column nucleus** — the **first central relay** of the
**dorsal column–medial lemniscus pathway** for the **lower body**
(legs, lower trunk). It is a **somatosensory relay** — **NOT** a
respiratory nucleus, **NOT** a chemosensory structure, **NOT** a
circumventricular organ, and **NOT** a reticular nucleus. **In
this tree**, it is wired as a **child** of ``respiratory_center``
— this is a **tree-wiring artifact** (see *Boundary status — NOT
a respiratory nucleus*).
**Part of:** The **respiratory_center** container
(``.../respiratory_center/``) — which is part of the **medulla
oblongata** — the **caudal brainstem** subdivision of the
**myelencephalon**. **The "respiratory_center" label is a
tree-wiring artifact — the gracile nucleus is NOT a respiratory
nucleus.**
**Structural parent:** ``.../respiratory_center/`` → **direct
child** of the respiratory_center container.
**Structural children:** **Two —** ``left`` and ``right`` — each
a **leaf** representing the **left** or **right** gracile
nucleus. **Anatomically**, the left and right gracile nuclei are
**truly separate bilateral structures** (unlike the area
postrema, which is a midline organ wired as left/right by
convention) — the **left gracile nucleus** relays **left
lower-body** somatosensation and the **right gracile nucleus**
relays **right lower-body** somatosensation.
**Boundary status (NOT a respiratory nucleus — a SOMATOSENSORY
relay — the tree-wiring artifact caveat):** **Boundary case —
the gracile nucleus is NOT a respiratory nucleus.** Although
wired under ``respiratory_center``, the **gracile nucleus** is a
**dorsal column somatosensory relay** — it relays **fine touch,
vibration, and conscious proprioception** from the **lower
body** to the **contralateral thalamus** (VPL) via the **medial
lemniscus**. It is **NOT** a respiratory rhythm generator,
**NOT** a respiratory pattern generator, **NOT** a
respiratory-chemoreceptor, and **NOT** a respiratory-related
structure of any kind. **The "respiratory_center" label is a
TREE-WIRING ARTIFACT** — the tree groups the gracile nucleus
with the area postrema, chemoreceptor trigger zone, cuneate
nucleus, dorsal respiratory group, and gigantocellular reticular
nucleus as a **pragmatic cluster** for brainstem organization.
Consumers must **not** infer **respiratory function** from
**container membership** — the gracile nucleus is
**somatosensory**.
**Boundary status (NOT the cuneate nucleus — a DIFFERENT dorsal
column nucleus for a DIFFERENT body region):** **Boundary case
— the gracile nucleus is NOT the cuneate nucleus.** The
**cuneate nucleus** (``.../respiratory_center/cuneate_nucleus/``)
is the **other** dorsal column nucleus — it relays **fine
touch, vibration, and proprioception** from the **upper body**
(arms, upper trunk, neck). The **gracile nucleus** (here)
relays **fine touch, vibration, and proprioception** from the
**lower body** (legs, lower trunk). **They are DIFFERENT
NUCLEI** — both are **dorsal column nuclei** — children of
``respiratory_center`` — but they serve **different body
regions**. The **gracile nucleus** is **medial** to the cuneate
nucleus; the **cuneate nucleus** is **lateral** to the gracile
nucleus. Consumers must **not** conflate the two.
**Boundary status (NOT the accessory cuneate nucleus — a
DIFFERENT nucleus with a DIFFERENT function):** **Boundary case
— the gracile nucleus is NOT the accessory cuneate nucleus.**
The **accessory cuneate nucleus** (lateral cuneate nucleus,
nucleus cuneatus accessorius) is a **different medullary
nucleus** — it is the **origin** of the **posterior
spinocerebellar tract** (unconscious proprioception to the
cerebellum), **NOT** the **dorsal column–medial lemniscus
pathway**. The **accessory cuneate nucleus** is **dorsolateral**
to the main cuneate nucleus — it has **no counterpart** for the
gracile nucleus (there is **no "accessory gracile nucleus"**).
Consumers must **not** conflate the gracile nucleus with the
accessory cuneate nucleus — resolve the accessory cuneate
nucleus via the references.
**Boundary status (NOT the medial lemniscus — a DIFFERENT
structure — the white-matter tract that carries gracile
output):** **Boundary case — the gracile nucleus is NOT the
medial lemniscus.** The **medial lemniscus** is a
**white-matter tract** — it is the **ascending pathway** that
**carries the axons** of the **gracile** and **cuneate**
nuclei (after their **decussation** as the **internal arcuate
fibers**) to the **contralateral thalamus** (VPL). The
**gracile nucleus** (here) is a **grey-matter nucleus** — it
**projects** to the medial lemniscus, but it is **NOT** the
medial lemniscus. Consumers must **not** conflate the
**nucleus** with the **white-matter tract**.
**Boundary status (NOT the internal arcuate fibers — a
DIFFERENT structure — the decussating axons from the gracile
nucleus):** **Boundary case — the gracile nucleus is NOT the
internal arcuate fibers.** The **internal arcuate fibers** are
the **decussating axons** of the **gracile** and **cuneate**
nuclei — they **cross the midline** in the **medulla** and
**ascend** as the **medial lemniscus**. The **gracile nucleus**
(here) is the **grey-matter nucleus** of origin — the
**internal arcuate fibers** are the **white-matter axons** that
**leave** it. Consumers must **not** conflate the **nucleus**
with its **decussating axons**.
**Boundary status (NOT the trigeminal nuclei — a DIFFERENT
somatosensory system):** **Boundary case — the gracile nucleus
is NOT the trigeminal nuclei.** The **trigeminal nuclei**
(principal sensory nucleus, spinal trigeminal nucleus,
mesencephalic trigeminal nucleus) relay **facial** sensation
via **CN V**. The **gracile nucleus** (here) relays
**lower-body somatosensation** via the **dorsal column–medial
lemniscus pathway**. **They are DIFFERENT SOMATOSENSORY
SYSTEMS** — **cranial vs. spinal** — with **different
receptors**, **different pathways**, and **different targets**.
Consumers must **not** conflate the two.
**Boundary status (NOT the spinothalamic tract — a DIFFERENT
somatosensory pathway):** **Boundary case — the gracile
nucleus is NOT the spinothalamic tract.** The **spinothalamic
tract** relays **pain and temperature** sensation — **NOT**
**fine touch, vibration, and proprioception**. The **gracile
nucleus** (here) is a **dorsal column relay** for **fine touch,
vibration, and proprioception**. **They are DIFFERENT
SOMATOSENSORY PATHWAYS** — **dorsal column–medial lemniscus**
vs. **spinothalamic** — with **different receptors**,
**different pathways**, and **different targets**. Consumers
must **not** conflate the two.
**Boundary status (NOT the thalamus — the gracile nucleus
PROJECTS TO the thalamus):** **Boundary case — the gracile
nucleus is NOT the thalamus.** The **ventral posterolateral
(VPL) nucleus** of the **thalamus** is the **third-order
relay** in the dorsal column–medial lemniscus pathway — it
**receives** the medial lemniscus. The **gracile nucleus**
(here) is the **second-order relay** in the medulla. Consumers
must **not** conflate the two.
**Boundary status (NOT the primary somatosensory cortex — the
VPL PROJECTS TO the cortex):** **Boundary case — the gracile
nucleus is NOT the primary somatosensory cortex.** The
**primary somatosensory cortex (S1)** in the **postcentral
gyrus** is the **fourth-order target** of the dorsal
column–medial lemniscus pathway. The **gracile nucleus**
(here) is the **second-order medullary relay**. Consumers must
**not** conflate the two.
**Boundary status (NOT the other respiratory_center children —
area postrema, CTZ, cuneate nucleus, DRG, Gi — DIFFERENT
structures):** **Boundary case — the gracile nucleus is NOT
the area postrema, the chemoreceptor trigger zone, the cuneate
nucleus, the dorsal respiratory group, or the gigantocellular
reticular nucleus.** Each is a **different structure** — see
the respective modules. Consumers must **not** conflate the
gracile nucleus with any of these.
**Boundary status (NOT the whole respiratory_center — a CHILD
of it):** **Boundary case — the gracile nucleus is NOT the
whole respiratory_center.** The **respiratory_center**
(``.../respiratory_center/``) is the **parent container** — it
contains the **gracile nucleus** (here) **plus** the
``area_postrema``, ``chemoreceptor_trigger_zone``,
``cuneate_nucleus``, ``dorsal_respiratory_group``, and
``gigantocellular_reticular_nucleus``. The **gracile nucleus**
is **one child** of that container. Consumers must **not**
conflate the **child** with the **whole container**.
**Boundary status (NOT the whole medulla oblongata — a
somatosensory relay within it):** **Boundary case — the
gracile nucleus is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the gracile nucleus (via
the respiratory_center) **plus** the cranial nerve nuclei, the
autonomic nuclei, the olivary body, the medullary pyramid, the
arcuate nucleus, the parafacial zone, the paramedian reticular
nucleus, the perihypoglossal nuclei, the respiratory_center,
and other structures. The **gracile nucleus** is **one
somatosensory relay** within the medulla. Consumers must **not**
conflate the **gracile nucleus** with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
ANATOMICALLY SEPARATE structures):** **Boundary case — the
gracile nucleus is a BILATERAL container whose left and right
children are ANATOMICALLY SEPARATE.** Unlike the **area
postrema** (a **midline** organ wired as left/right by
convention), the **gracile nucleus** is a **truly paired**
medullary structure — the **left gracile nucleus** relays
**left lower-body** sensation (via the **left gracile
fasciculus**) and the **right gracile nucleus** relays
**right lower-body** sensation (via the **right gracile
fasciculus**). **The left / right split here is ANATOMICAL,
not a wiring convention.** Consumers must **not** infer
**midline wiring convention** from the gracile nucleus (that
convention applies to the area postrema / CTZ, NOT the gracile
nucleus).

Overview
--------
The **gracile nucleus (nucleus gracilis)** — also known as the
**nucleus of Goll** — is a **dorsal column nucleus** in the
**medulla oblongata**. It is the **first central relay** of the
**dorsal column–medial lemniscus pathway** for the **lower body**
(legs, lower trunk). It **receives** primary afferent axons from
the **ipsilateral gracile fasciculus** (carrying fine touch,
vibration, and conscious proprioception from the lower body),
**relays** them to **second-order neurons**, whose axons
**decussate** as the **internal arcuate fibers** and **ascend**
as the **medial lemniscus** to the **contralateral thalamus**
(VPL).

**The gracile nucleus is a SOMATOSENSORY relay, NOT a respiratory
nucleus.** Although it is wired under ``respiratory_center``,
its **primary function** is **fine touch, vibration, and
conscious proprioception** from the **lower body** — **NOT**
**breathing**. The **"respiratory_center"** label is a
**tree-wiring artifact** — the tree groups the gracile nucleus
with the area postrema, chemoreceptor trigger zone, cuneate
nucleus, dorsal respiratory group, and gigantocellular reticular
nucleus as a **pragmatic cluster** for brainstem organization.
Consumers must **not** infer **respiratory function** from
**container membership**.

**The gracile nucleus is TRULY BILATERAL — the left / right split
is ANATOMICAL.** Unlike the **area postrema** (a **midline**
organ wired as left/right by convention), the **left** and
**right** gracile nuclei are **anatomically separate
structures**. The **left gracile nucleus** relays **left
lower-body** sensation (via the **left gracile fasciculus**);
the **right gracile nucleus** relays **right lower-body**
sensation (via the **right gracile fasciculus**). The **left /
right split** here reflects **anatomy** — **NOT** a
**tree-wiring convention**.

**The gracile nucleus is the MEDIAL dorsal column nucleus — the
cuneate nucleus is LATERAL.** The **gracile nucleus** is
**medial** (near the midline, at the **gracile tubercle** of the
medulla); the **cuneate nucleus** is **lateral** (at the
**cuneate tubercle**). The **gracile fasciculus** (lower body)
is **medial** in the spinal cord; the **cuneate fasciculus**
(upper body) is **lateral**. This **medial-lateral organization**
is preserved in the **medulla** — the **gracile nucleus** is the
**medial** member of the dorsal column nuclei pair.

**The gracile nucleus is functionally coupled to the cuneate
nucleus, the medial lemniscus, the VPL thalamus, and the
primary somatosensory cortex (S1).** It is **part of** the
**dorsal column–medial lemniscus pathway** — a **three-neuron
ascending pathway** that relays **fine touch, vibration, and
conscious proprioception** from the body to the cortex.

Bilateral Structure (Anatomical Pairing)
---------------------------------------
The gracile nucleus is a **bilateral container** in this tree
with **two structural children**:

*   ``left`` — the **left** gracile nucleus (a **leaf** module).
*   ``right`` — the **right** gracile nucleus (a **leaf**
    module).

**The two children are ANATOMICALLY SEPARATE structures** —
**NOT** a wiring convention for a midline organ (unlike the
area postrema / CTZ). The **left gracile nucleus** relays
**left lower-body** sensation; the **right gracile nucleus**
relays **right lower-body** sensation.

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **gracile nuclei** as **single structures**.
Consumers that need **side-specific** resolution descend into
``left`` or ``right``; consumers that need the **whole
bilateral pair** use ``gracile_nucleus`` (the container) as a
whole.

**The container itself is unpaired.** There is **no**
``gracile_nucleus/left/.../`` structural hierarchy beyond the
single leaf level — the ``left`` and ``right`` modules are the
**terminal modules** for this structure.

The Gracile Nucleus / Cuneate Nucleus Boundary
----------------------------------------------
This is the **most consequential** dorsal-column nucleus
boundary:

*   **Gracile nucleus** (this module) — the **lower-body** dorsal
    column relay (medial).

*   **Cuneate nucleus**
    (``.../respiratory_center/cuneate_nucleus/``) — the
    **upper-body** dorsal column relay (lateral).

**They are DIFFERENT NUCLEI** — both are **dorsal column nuclei**
— children of ``respiratory_center`` — but they serve **different
body regions**. The **gracile nucleus** is **medial**; the
**cuneate nucleus** is **lateral**. Consumers must **not**
conflate the two.

The Gracile Nucleus / Accessory Cuneate Nucleus Boundary
--------------------------------------------------------
This is the **dorsal column / spinocerebellar** boundary:

*   **Gracile nucleus** (this module) — the **lower-body** dorsal
    column relay (conscious proprioception, fine touch,
    vibration, via the **medial lemniscus** to the **VPL
    thalamus**).

*   **Accessory cuneate nucleus** — the **upper-body**
    **spinocerebellar** relay (unconscious proprioception, via
    the **posterior spinocerebellar tract** to the
    **cerebellum**).

**They are DIFFERENT NUCLEI** with **DIFFERENT functions** — and
the **accessory cuneate nucleus** has **no gracile
counterpart** (there is **no "accessory gracile nucleus"**). The
accessory cuneate nucleus is **NOT wired** in this tree. Consumers
must **not** conflate the gracile nucleus with the accessory
cuneate nucleus.

The Gracile Nucleus / Medial Lemniscus and Internal Arcuate Fibers Boundary
---------------------------------------------------------------------------
This is the **nucleus / white-matter tract** boundary:

*   **Gracile nucleus** (this module) — the **grey-matter relay**.

*   **Medial lemniscus** — the **white-matter tract** that carries
    the **second-order axons** to the **VPL thalamus**.

*   **Internal arcuate fibers** — the **decussating axons** of
    the gracile (and cuneate) nuclei.

**The gracile nucleus PROJECTS TO the medial lemniscus via the
internal arcuate fibers** — but the **nucleus** is **NOT** the
**tract**, and **NOT** the **decussating axons**. Consumers must
**not** conflate the **nucleus** with the **white-matter
structures** it projects through.

The Gracile Nucleus / Trigeminal Nuclei and Spinothalamic Tract Boundary
------------------------------------------------------------------------
This is the **dorsal column / other somatosensory** boundary:

*   **Gracile nucleus** (this module) — the **lower-body** dorsal
    column relay (fine touch, vibration, conscious
    proprioception).

*   **Trigeminal nuclei** — the **facial** somatosensory system.

*   **Spinothalamic tract** — the **pain and temperature** system.

**They are DIFFERENT SOMATOSENSORY SYSTEMS** — the **gracile
nucleus** is a **dorsal column relay**; the **trigeminal nuclei**
carry **facial** sensation; the **spinothalamic tract** carries
**pain and temperature**. Consumers must **not** conflate the
three.

The Gracile Nucleus / VPL Thalamus and Primary Somatosensory Cortex Boundary
----------------------------------------------------------------------------
This is the **medullary relay / higher-order relays** boundary:

*   **Gracile nucleus** (this module) — the **second-order
    medullary relay**.

*   **VPL thalamus** — the **third-order thalamic relay**.

*   **Primary somatosensory cortex (S1)** — the **fourth-order
    cortical target**.

**They are DIFFERENT STRUCTURES** at **different levels** of the
**dorsal column–medial lemniscus pathway**. Consumers must **not**
conflate them.

The Gracile Nucleus / Other Respiratory Center Children Boundary
----------------------------------------------------------------
This is the **somatosensory / respiratory-and-circumventricular**
boundary:

*   **Gracile nucleus** (this module) — the **somatosensory
    relay**.

*   **Area postrema** and **chemoreceptor trigger zone**
    (``.../area_postrema/`` and
    ``.../chemoreceptor_trigger_zone/``) — the
    **circumventricular / chemosensory** structures.

*   **Cuneate nucleus** (``.../cuneate_nucleus/``) — the
    **upper-body** dorsal column relay.

*   **Dorsal respiratory group**
    (``.../dorsal_respiratory_group/``) — the **respiratory**
    pattern generator.

*   **Gigantocellular reticular nucleus**
    (``.../gigantocellular_reticular_nucleus/``) — the **large
    medullary reticular** nucleus.

**They are DIFFERENT STRUCTURES** — all six are **children** of
``respiratory_center``, but they are **functionally distinct**.
Consumers must **not** conflate the **gracile nucleus** with any
of these.

The Gracile Nucleus / Whole Respiratory Center and Whole Medulla Oblongata Boundary
-----------------------------------------------------------------------------------
This is the **child / container** boundary:

*   **Gracile nucleus** (this module) — one **child** of
    ``respiratory_center``.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children**.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The gracile nucleus is a CHILD of respiratory_center, NOT the
container itself, and NOT the whole medulla.** Consumers must
**not** conflate the **child** with either **parent container**.

Function in the Human Brain
---------------------------
The gracile nucleus's function is **somatosensory relay** for the
**lower body** — **NOT respiratory rhythm** and **NOT motor
control**:

*   **Fine touch, vibration, and conscious proprioception relay
    (lower body):** The **gracile nucleus** receives **primary
    afferent axons** from the **ipsilateral gracile fasciculus**
    (carrying **fine touch, vibration, and conscious
    proprioception** from the **lower body** — legs, lower
    trunk) and **relays** them to **second-order neurons** whose
    axons **decussate** as the **internal arcuate fibers** and
    **ascend** as the **medial lemniscus** to the
    **contralateral VPL thalamus**.

*   **Somatotopic organization:** The **gracile nucleus** is
    **somatotopically organized** — the **lower limb** is
    represented **dorsomedially**; the **sacral** segments are
    represented **most medially** (or similar — the exact map
    varies by species). This **somatotopy** is preserved in the
    **medial lemniscus** and the **VPL thalamus**.

*   **Lower-body sensory discrimination:** The **gracile nucleus**
    is **part of** the **neural substrate** for **fine sensory
    discrimination** of the **lower body** — the **ability** to
    **detect** and **localize** **subtle** **tactile**,
    **vibratory**, and **proprioceptive** stimuli on the
    **legs, feet, and lower trunk**. This is **clinically
    critical** — the **lower limbs** carry the **highest density**
    of **proprioceptive** function required for **standing**,
    **walking**, and **balance**.

*   **NOT respiratory rhythm:** The **gracile nucleus** does
    **not** generate the **respiratory rhythm** — that is the
    **pre-Bötzinger complex** (VRG) and the **respiratory**
    centers. The **gracile nucleus** is a **somatosensory**
    relay — **NOT** a respiratory nucleus.

*   **NOT motor control:** The **gracile nucleus** does **not**
    send motor axons to muscles.

**The unifying theme:** the gracile nucleus is the
**lower-body** **dorsal column** somatosensory relay in the
**medulla** — it **relays** **fine touch, vibration, and
conscious proprioception** from the **lower body** to the
**contralateral VPL thalamus** via the **medial lemniscus** —
**NOT** a respiratory nucleus, **NOT** the cuneate nucleus,
**NOT** the accessory cuneate nucleus, **NOT** the trigeminal
nuclei, and **NOT** the spinothalamic tract.

Associated Disorders
--------------------
The gracile nucleus is the **substrate** for **well-defined
clinical syndromes** — its clinical relevance is **direct**,
via **dorsal column somatosensory** dysfunction:

*   **Dorsal column sensory loss — lower body (via gracile
    nucleus dysfunction):** **Lesions** of the **gracile
    nucleus** (from **stroke**, **demyelination**, **tumor**,
    **vitamin B12 deficiency** — subacute combined degeneration,
    or **tabes dorsalis**) cause **loss of fine touch, vibration,
    and proprioception** from the **lower body** — **legs,
    feet, lower trunk** — on the **ipsilateral** side (because
    the **decussation** of the dorsal column–medial lemniscus
    pathway occurs **above** the gracile nucleus, in the
    **medulla**, via the **internal arcuate fibers**). **A
    lesion at or below the gracile nucleus** produces
    **ipsilateral** lower-body sensory loss; a **lesion above
    the decussation** (e.g., in the **medial lemniscus**)
    produces **contralateral** lower-body sensory loss.

*   **Subacute combined degeneration (via dorsal column —
    including gracile nucleus — dysfunction):** **Vitamin B12
    deficiency** causes **demyelination** of the **dorsal
    columns** (including the **gracile fasciculus**) and the
    **lateral corticospinal tracts** — producing **loss of
    vibration and proprioception** (lower and upper body) plus
    **spastic weakness**. The **gracile nucleus** is the
    **lower-body central relay** affected in this condition.

*   **Tabes dorsalis (via dorsal column — including gracile
    nucleus — dysfunction):** **Neurosyphilis** causes
    **demyelination** of the **dorsal columns** (including
    the **gracile fasciculus**) and the **dorsal roots** —
    producing **impaired proprioception**, **sensory ataxia**,
    and **Romberg sign**. The **gracile nucleus** is the
    **lower-body central relay** affected in this condition.

*   **Brainstem stroke (via gracile nucleus involvement):**
    **Lateral medullary syndrome (Wallenberg)** can **involve**
    the **gracile nucleus** (or the **gracile fasciculus**
    rostrally) — contributing to **ipsilateral lower-body
    sensory loss**.

*   **Gracile fasciculus lesions — lower body sensory loss
    (contrast — peripheral / spinal cord):** **Lesions** of
    the **gracile fasciculus** in the **spinal cord** (from
    **trauma**, **tumor**, **MS**, **B12 deficiency**, or
    **tabes dorsalis**) cause **similar** lower-body sensory
    loss — but the **gracile fasciculus** is a **white-matter
    tract** in the **spinal cord**, **NOT** the **gracile
    nucleus** in the **medulla**. Consumers must **not**
    conflate the two.

*   **No Named "Gracile Nucleus Syndrome":** The gracile nucleus
    is a **somatosensory relay** — its clinical syndromes are
    **named for the broader lesion** (dorsal column syndrome,
    subacute combined degeneration, tabes dorsalis, brainstem
    stroke) or the **pattern of sensory loss** — **NOT** for the
    nucleus itself.

**What is NOT here:** The gracile nucleus is **not** the substrate
for **respiratory rhythm** (VRG, pre-Bötzinger complex),
**central hypoventilation** (VRG), **emesis** (area postrema /
chemoreceptor trigger zone), **sympathetic premotor** function
(RVLM), **visceral afferent relay** (NTS), **tongue weakness**
(hypoglossal nucleus), or **pain and temperature loss**
(spinothalamic tract). Its clinical relevance is the
**lower-body dorsal column somatosensory** functions listed above.

Lateralization Notes
--------------------
The gracile nucleus is a **bilateral container** in this tree with
``left`` and ``right`` structural children. There is **no**
``gracile_nucleus/left/.../`` structural hierarchy beyond the
single leaf level.

*   **Bilateral structural children (ANATOMICAL pairing):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left** or **right** gracile nucleus as a **single
    structure**. The **left** and **right** gracile nuclei are
    **anatomically separate structures** (unlike the **area
    postrema**, which is a **midline** organ wired as left/right
    by convention). The **left** gracile nucleus relays **left
    lower-body** sensation (via the **left gracile fasciculus**);
    the **right** gracile nucleus relays **right lower-body**
    sensation (via the **right gracile fasciculus**).

*   **Ipsilateral vs. contralateral — CRITICAL DISTINCTION:** The
    gracile nucleus itself relays **ipsilateral** lower-body
    sensation (the **gracile fasciculus** is **ipsilateral** to
    the receptors). **After the gracile nucleus**, the pathway
    **decussates** (via the **internal arcuate fibers**) —
    becoming the **contralateral** medial lemniscus. **A lesion
    AT the gracile nucleus** produces **ipsilateral** lower-body
    sensory loss; a **lesion ABOVE the decussation** produces
    **contralateral** lower-body sensory loss. This is a
    **classic localization principle** — analogous to the
    hypoglossal nucleus / corticobulbar distinction.

*   **NO lateralization warning:** The gracile nucleus has **no
    known functional lateralization** in humans — the **left**
    and **right** gracile nuclei are **functionally symmetric**
    (each relays **its own side's** lower-body sensation). This
    is **symmetric lateralization** — each side handles **one
    body side** — **NOT** a lateralization **warning** in the
    frontotemporal_cortical_system sense (which concerns
    asymmetric function). Consumers must **not** import a
    **lateralization warning** into the gracile nucleus — the
    **left** and **right** nuclei are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The gracile nucleus
    is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the gracile nucleus.

*   **NO Fear-Output Warning:** The gracile nucleus is **not** a
    fear-output structure — it is a **dorsal column somatosensory**
    relay. Consumers must **not** conflate it with the **central
    nucleus** or with the **amygdala**.

**A consumer that assumes "left gracile nucleus = right gracile
nucleus" will be structurally correct** — the two sides are
**symmetric** and **functionally equivalent** at the **nucleus
level** (each relays **its own side's** lower-body sensation).
The gracile nucleus is a **strict-mirror pair with NO warning** —
**no SLEA warning**, **no fear-output warning**, and **no
lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The gracile nucleus is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../cuneate_nucleus/``,
    ``.../area_postrema/``,
    ``.../chemoreceptor_trigger_zone/``,
    ``.../dorsal_respiratory_group/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``, or any other container. The
    gracile nucleus's relationships to the cuneate nucleus,
    accessory cuneate nucleus, medial lemniscus, internal arcuate
    fibers, trigeminal nuclei, spinothalamic tract, VPL thalamus,
    S1 cortex, area postrema, chemoreceptor trigger zone, dorsal
    respiratory group, and gigantocellular reticular nucleus are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Bilateral container with two leaf children (ANATOMICAL
    pairing).** The structural children are ``left`` and
    ``right``, each a **leaf**. **Anatomically**, the left and
    right gracile nuclei are **truly separate bilateral
    structures** — the **left / right split** is **ANATOMICAL**,
    **NOT** a **tree-wiring convention**.
*   **SOMATOSENSORY RELAY, NOT a respiratory nucleus.** Although
    wired under ``respiratory_center``, the gracile nucleus is a
    **dorsal column somatosensory** relay — **NOT** a respiratory
    rhythm generator, **NOT** a respiratory pattern generator,
    **NOT** a respiratory-chemoreceptor, and **NOT** a
    respiratory-related structure of any kind.
*   **TREE-WIRING ARTIFACT caveat — the "respiratory_center" label
    is NOT a claim about function.** The gracile nucleus is
    **somatosensory**; the **respiratory_center** label reflects
    a **pragmatic tree cluster**, **NOT** a functional
    classification.
*   **NOT the cuneate nucleus.** The **cuneate nucleus** is the
    **upper-body** counterpart — a **different structure**.
*   **NOT the accessory cuneate nucleus.** The **accessory cuneate
    nucleus** is the **spinocerebellar** relay — **NOT wired** in
    this tree, and it has **no gracile counterpart**.
*   **NOT the medial lemniscus or the internal arcuate fibers.**
    Those are **white-matter structures** — the **nucleus**
    **projects to** them, but is **NOT** them.
*   **NOT the trigeminal nuclei or the spinothalamic tract.**
    Those are **different somatosensory systems** — **facial**
    and **pain/temperature**, respectively.
*   **NOT the VPL thalamus or the S1 cortex.** Those are
    **higher-order relays** in the **dorsal column–medial
    lemniscus pathway**.
*   **NOT the whole respiratory_center or whole medulla
    oblongata.** The gracile nucleus is a **child** of
    ``respiratory_center``, not the container itself.
*   **No ``AREA_PATHS`` hop.** The gracile nucleus is a **local
    container** — it is not cross-listed under another brainparts
    path.
*   **No nested cross-listing.** The gracile nucleus has no
    nested dual-framing module. It is a **bilateral container**
    with **two leaf children** (anatomical pairing).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **dorsal column
    somatosensory** framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center import gracile_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.gracile_nucleus"
    )

**Do not** infer **respiratory function** from membership in the
respiratory_center. The gracile nucleus is a **dorsal column
somatosensory** relay — **NOT** a respiratory nucleus. The
**"respiratory_center"** label is a **tree-wiring artifact**.

**Do not** assume the gracile nucleus is the **cuneate nucleus**.
The cuneate nucleus is the **upper-body** counterpart — a
**different structure**.

**Do not** assume the gracile nucleus is the **accessory cuneate
nucleus**. The accessory cuneate nucleus is the
**spinocerebellar** relay — **NOT wired** in this tree, and it
has **no gracile counterpart**.

**Do not** assume the gracile nucleus is the **medial lemniscus**
or the **internal arcuate fibers**. Those are **white-matter
structures** — the **nucleus** projects to them, but is **NOT**
them.

**Do not** assume the gracile nucleus is the **trigeminal
nuclei** or the **spinothalamic tract**. Those are **different
somatosensory systems**.

**Do not** assume the gracile nucleus is the **VPL thalamus** or
the **S1 cortex**. Those are **higher-order relays** in the
**dorsal column–medial lemniscus pathway**.

**Do not** assume the gracile nucleus is the **whole
respiratory_center** or the **whole medulla oblongata**. It is
a **child** of ``respiratory_center``.

**Do not** infer **midline wiring convention** from the gracile
nucleus structure. The **left / right split** is **ANATOMICAL**
— the **left** and **right** gracile nuclei are **truly separate
bilateral structures** (unlike the area postrema / CTZ, which
are midline organs wired as left/right by convention).

Iterating the gracile nucleus's structural children (recommended
consumer pattern)::

    GRACILE_NUCLEUS_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # gracile nucleus. Anatomically, the left and right gracile
    # nuclei are TRULY SEPARATE bilateral structures — the
    # left/right split is ANATOMICAL, NOT a wiring convention.

Reaching the left and right gracile nuclei (recommended consumer
pattern)::

    # The left and right gracile nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus.right
    #
    # Each is a leaf module representing the gracile nucleus of
    # that side. Anatomically, they are TRULY SEPARATE bilateral
    # structures.

Reaching the cuneate nucleus (recommended consumer pattern —
NOTE the DIFFERENT child of respiratory_center)::

    # The cuneate nucleus is a SEPARATE child of respiratory_center
    # in this tree — the UPPER-BODY counterpart of the gracile
    # nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus
    #
    # Both are DORSAL COLUMN NUCLEI — children of
    # respiratory_center — but they serve DIFFERENT BODY REGIONS:
    # the gracile nucleus relays LOWER-BODY sensation; the cuneate
    # nucleus relays UPPER-BODY sensation.

Reaching the medial lemniscus and internal arcuate fibers
(recommended consumer pattern — NOTE the DIFFERENT structures)::

    # The medial lemniscus is a WHITE-MATTER TRACT; the internal
    # arcuate fibers are the DECUSSATING AXONS of the gracile
    # (and cuneate) nuclei:
    #
    #   (medial lemniscus — white-matter tract in the medulla,
    #    pons, and midbrain)
    #   (internal arcuate fibers — decussating axons from the
    #    gracile and cuneate nuclei)
    #
    # The gracile nucleus PROJECTS TO the medial lemniscus via
    # the internal arcuate fibers, but is NOT the tract and NOT
    # the decussating axons.

Reaching the trigeminal nuclei and the spinothalamic tract
(recommended consumer pattern — NOTE the DIFFERENT somatosensory
systems)::

    # The trigeminal nuclei and the spinothalamic tract are
    # DIFFERENT SOMATOSENSORY SYSTEMS:
    #
    #   (trigeminal nuclei — facial sensation via CN V)
    #   (spinothalamic tract — pain and temperature)
    #
    # The gracile nucleus is a DORSAL COLUMN relay for fine
    # touch, vibration, and conscious proprioception from the
    # LOWER BODY — NOT facial sensation, NOT pain/temperature.

Reaching the VPL thalamus and S1 cortex (recommended consumer
pattern — NOTE the DIFFERENT levels of the pathway)::

    # The VPL thalamus and S1 cortex are HIGHER-ORDER RELAYS in
    # the dorsal column–medial lemniscus pathway:
    #
    #   (VPL thalamus — third-order relay in the thalamus)
    #   (S1 cortex — fourth-order target in the postcentral gyrus)
    #
    # The gracile nucleus is the SECOND-ORDER MEDULLARY relay —
    # NOT the thalamus, NOT the cortex.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"respiratory_center.gracile_nucleus.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: the left and right gracile nuclei are TRULY
        # SEPARATE bilateral structures (ANATOMICAL, not a
        # wiring convention).

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Gracile nucleus; dorsal column–medial lemniscus pathway;
    somatotopic organization; internal arcuate fibers.)
*   **Dorsal column–medial lemniscus pathway — overview:**
    Tracey, D.J. (2004). "Ascending and descending pathways."
    In: Paxinos, G. (ed.), *The Rat Nervous System*, 3rd ed.
    (Dorsal column nuclei; gracile nucleus; cuneate nucleus;
    medial lemniscus; internal arcuate fibers.)
*   **Gracile nucleus — somatotopy:** Millar, J., Basbaum, A.I.
    (1975). "Topography of the projection of the body surface
    of the rat to the cuneate nucleus." *Experimental
    Neurology* 49:841–858. (Somatotopic organization of the
    dorsal column nuclei — including the gracile nucleus.)
*   **Dorsal column nuclei — anatomy:** Rustioni, A., Weinberg,
    R.J. (1989). "Somatosensory system: the dorsal column
    nuclei." In: *The Human Nervous System* (Paxinos, G., ed.).
    (Dorsal column nuclei; gracile and cuneate nuclei;
    somatosensory pathways.)
*   **Gracile nucleus — anatomy and connections:** Berkley, K.J.,
    et al. (1986). "Somatosensory projections to the cuneate
    nucleus." *Journal of Comparative Neurology* 253:222–236.
    (Dorsal column nuclei; primary afferent input; projections
    to the medial lemniscus — including the gracile nucleus.)
*   **Subacute combined degeneration — dorsal column:**
    Hemmer, B., et al. (1998). "Subacute combined degeneration:
    clinical, electrophysiological, and magnetic resonance
    imaging findings." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 65:822–827. (Vitamin B12 deficiency; dorsal
    column dysfunction; gracile and cuneate nuclei.)
*   **Tabes dorsalis — dorsal column:** Timmermans, M., Carr,
    J. (2004). "Neurosyphilis." *Current Opinion in Infectious
    Diseases* 17:49–54. (Tabes dorsalis; dorsal column
    dysfunction; gracile and cuneate nuclei; neurosyphilis.)
*   **Lateral medullary syndrome (Wallenberg):** Sacco, R.L., et
    al. (1993). "Lateral medullary infarction: clinical and MRI
    correlation." *Stroke* 24:1981–1987. (Wallenberg syndrome;
    gracile nucleus involvement; lower-body sensory loss.)
*   **Accessory cuneate nucleus (contrast — spinocerebellar):**
    Grant, G. (1962). "Spinal course and somatotopically
    localized termination of the spinocerebellar tracts."
    *Acta Physiologica Scandinavica* 56(Suppl. 204):1–45.
    (Accessory cuneate nucleus; posterior spinocerebellar tract;
    unconscious proprioception — DIFFERENT from the gracile
    nucleus and with NO gracile counterpart.)
*   **Trigeminal nuclei (contrast — facial sensation):** Usunoff,
    K.G., et al. (1997). "The trigeminal system." *Advances in
    Anatomy, Embryology, and Cell Biology* 137:1–112.
    (Trigeminal nuclei — facial sensation via CN V — DIFFERENT
    from the dorsal column pathway.)
*   **Spinothalamic tract (contrast — pain/temperature):**
    Willis, W.D., Westlund, K.N. (1997). "Neuroanatomy of the
    pain system." In: *Textbook of Pain* (Wall, P.D., Melzack,
    R., eds.). (Spinothalamic tract — pain and temperature —
    DIFFERENT from the dorsal column pathway.)
*   **VPL thalamus and S1 cortex (higher-order relays):** Kaas,
    J.H. (2004). "Somatosensory system." In: *The Human Nervous
    System* (Paxinos, G., Mai, J.K., eds.). (VPL thalamus;
    primary somatosensory cortex — higher-order relays in the
    dorsal column–medial lemniscus pathway.)
*   NeuroNames — Nucleus gracilis; FMA — Gracile nucleus.
"""