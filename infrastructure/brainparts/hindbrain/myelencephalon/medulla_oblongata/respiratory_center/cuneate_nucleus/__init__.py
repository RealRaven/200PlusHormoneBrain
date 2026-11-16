"""
infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus
=======================================================================================================

Anatomical Hierarchy
--------------------
::

    hindbrain
    └── myelencephalon
        └── medulla_oblongata
            └── respiratory_center
                └── cuneate_nucleus   <-- THIS MODULE
                    ├── left
                    └── right

**Primary synonym:** Cuneate nucleus; nucleus cuneatus; nucleus of
Burdach; Burdach's nucleus; lateral cuneate nucleus (avoid — that
is the accessory cuneate nucleus, a **different** structure);
dorsal column nucleus (upper body).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**dorsal column nucleus** — the **first central relay** of the
**dorsal column–medial lemniscus pathway** for the **upper body**
(arms, upper trunk, neck). It is a **somatosensory relay** —
**NOT** a respiratory nucleus, **NOT** a chemosensory structure,
**NOT** a circumventricular organ, and **NOT** a reticular
nucleus. **In this tree**, it is wired as a **child** of
``respiratory_center`` — this is a **tree-wiring artifact** (see
*Boundary status — NOT a respiratory nucleus*).
**Part of:** The **respiratory_center** container
(``.../respiratory_center/``) — which is part of the **medulla
oblongata** — the **caudal brainstem** subdivision of the
**myelencephalon**. **The "respiratory_center" label is a
tree-wiring artifact — the cuneate nucleus is NOT a respiratory
nucleus.**
**Structural parent:** ``.../respiratory_center/`` → **direct
child** of the respiratory_center container.
**Structural children:** **Two —** ``left`` and ``right`` — each a
**leaf** representing the **left** or **right** cuneate nucleus.
**Anatomically**, the left and right cuneate nuclei are **truly
separate bilateral structures** (unlike the area postrema, which
is a midline organ wired as left/right by convention) — the
left cuneate nucleus relays **left upper-body** somatosensation
and the right cuneate nucleus relays **right upper-body**
somatosensation.
**Boundary status (NOT a respiratory nucleus — a SOMATOSENSORY
relay — the tree-wiring artifact caveat):** **Boundary case —
the cuneate nucleus is NOT a respiratory nucleus.** Although
wired under ``respiratory_center``, the **cuneate nucleus** is a
**dorsal column somatosensory relay** — it relays **fine touch,
vibration, and conscious proprioception** from the **upper
body** to the **contralateral thalamus** (VPL) via the **medial
lemniscus**. It is **NOT** a respiratory rhythm generator,
**NOT** a respiratory pattern generator, **NOT** a
respiratory-chemoreceptor, and **NOT** a respiratory-related
structure of any kind. **The "respiratory_center" label is a
TREE-WIRING ARTIFACT** — the tree groups the cuneate nucleus
with the area postrema, chemoreceptor trigger zone, dorsal
respiratory group, gigantocellular reticular nucleus, and
gracile nucleus as a **pragmatic cluster** for brainstem
organization. Consumers must **not** infer **respiratory
function** from **container membership** — the cuneate nucleus
is **somatosensory**.
**Boundary status (NOT the gracile nucleus — a DIFFERENT dorsal
column nucleus for a DIFFERENT body region):** **Boundary case
— the cuneate nucleus is NOT the gracile nucleus.** The
**gracile nucleus**
(``.../respiratory_center/gracile_nucleus/``) is the **other**
dorsal column nucleus — it relays **fine touch, vibration, and
proprioception** from the **lower body** (legs, lower trunk).
The **cuneate nucleus** (here) relays **fine touch, vibration,
and proprioception** from the **upper body** (arms, upper
trunk, neck). **They are DIFFERENT NUCLEI** — both are **dorsal
column nuclei** — children of ``respiratory_center`` — but they
serve **different body regions**. The **cuneate nucleus** is
**lateral** to the gracile nucleus; the **gracile nucleus** is
**medial** to the cuneate nucleus. Consumers must **not**
conflate the two.
**Boundary status (NOT the accessory cuneate nucleus — a
DIFFERENT nucleus with a SIMILAR name):** **Boundary case — the
cuneate nucleus is NOT the accessory cuneate nucleus.** The
**accessory cuneate nucleus** (lateral cuneate nucleus,
nucleus cuneatus accessorius) is a **different medullary
nucleus** — it is the **origin** of the **posterior
spinocerebellar tract** (unconscious proprioception to the
cerebellum), **NOT** the **dorsal column–medial lemniscus
pathway**. The **accessory cuneate nucleus** is **dorsolateral**
to the main cuneate nucleus. **In this tree**, the accessory
cuneate nucleus is **NOT wired** — only the main cuneate
nucleus is. Consumers must **not** conflate the two — resolve
the accessory cuneate nucleus via the references.
**Boundary status (NOT the medial lemniscus — a DIFFERENT
structure — the white-matter tract that carries cuneate
output):** **Boundary case — the cuneate nucleus is NOT the
medial lemniscus.** The **medial lemniscus** is a
**white-matter tract** — it is the **ascending pathway** that
**carries the axons** of the **cuneate** and **gracile**
nuclei (after their **decussation** as the **internal arcuate
fibers**) to the **contralateral thalamus** (VPL). The
**cuneate nucleus** (here) is a **grey-matter nucleus** — it
**projects** to the medial lemniscus, but it is **NOT** the
medial lemniscus. Consumers must **not** conflate the
**nucleus** with the **white-matter tract**.
**Boundary status (NOT the internal arcuate fibers — a
DIFFERENT structure — the decussating axons from the cuneate
nucleus):** **Boundary case — the cuneate nucleus is NOT the
internal arcuate fibers.** The **internal arcuate fibers** are
the **decussating axons** of the **cuneate** and **gracile**
nuclei — they **cross the midline** in the **medulla** and
**ascend** as the **medial lemniscus**. The **cuneate nucleus**
(here) is the **grey-matter nucleus** of origin — the
**internal arcuate fibers** are the **white-matter axons** that
**leave** it. Consumers must **not** conflate the **nucleus**
with its **decussating axons**.
**Boundary status (NOT the gracile nucleus, NTS, dorsal motor
nucleus of the vagus, hypoglossal nucleus, or other medullary
structures — DIFFERENT structures):** **Boundary case — the
cuneate nucleus is NOT these other medullary structures.** Each
is a **different structure** — see the respective modules.
Consumers must **not** conflate the **cuneate nucleus** with
any of these.
**Boundary status (NOT the trigeminal nuclei — a DIFFERENT
somatosensory system):** **Boundary case — the cuneate nucleus
is NOT the trigeminal nuclei.** The **trigeminal nuclei**
(principal sensory nucleus, spinal trigeminal nucleus,
mesencephalic trigeminal nucleus) relay **facial** sensation
via **CN V**. The **cuneate nucleus** (here) relays **upper-body
somatosensation** via the **dorsal column–medial lemniscus
pathway**. **They are DIFFERENT SOMATOSENSORY SYSTEMS** —
**cranial vs. spinal** — with **different receptors**,
**different pathways**, and **different targets**. Consumers
must **not** conflate the two.
**Boundary status (NOT the spinothalamic tract — a DIFFERENT
somatosensory pathway):** **Boundary case — the cuneate
nucleus is NOT the spinothalamic tract.** The **spinothalamic
tract** relays **pain and temperature** sensation — **NOT**
**fine touch, vibration, and proprioception**. The **cuneate
nucleus** (here) is a **dorsal column relay** for **fine touch,
vibration, and proprioception**. **They are DIFFERENT
SOMATOSENSORY PATHWAYS** — **dorsal column–medial lemniscus**
vs. **spinothalamic** — with **different receptors**,
**different pathways**, and **different targets**. Consumers
must **not** conflate the two.
**Boundary status (NOT the thalamus — the cuneate nucleus
PROJECTS TO the thalamus):** **Boundary case — the cuneate
nucleus is NOT the thalamus.** The **ventral posterolateral
(VPL) nucleus** of the **thalamus** is the **third-order
relay** in the dorsal column–medial lemniscus pathway — it
**receives** the medial lemniscus. The **cuneate nucleus**
(here) is the **second-order relay** in the medulla. Consumers
must **not** conflate the two.
**Boundary status (NOT the primary somatosensory cortex — the
VPL PROJECTS TO the cortex):** **Boundary case — the cuneate
nucleus is NOT the primary somatosensory cortex.** The
**primary somatosensory cortex (S1)** in the **postcentral
gyrus** is the **fourth-order target** of the dorsal
column–medial lemniscus pathway. The **cuneate nucleus**
(here) is the **second-order medullary relay**. Consumers must
**not** conflate the two.
**Boundary status (NOT the whole respiratory_center — a CHILD
of it):** **Boundary case — the cuneate nucleus is NOT the
whole respiratory_center.** The **respiratory_center**
(``.../respiratory_center/``) is the **parent container** — it
contains the **cuneate nucleus** (here) **plus** the
``area_postrema``, ``chemoreceptor_trigger_zone``,
``dorsal_respiratory_group``,
``gigantocellular_reticular_nucleus``, and ``gracile_nucleus``.
The **cuneate nucleus** is **one child** of that container.
Consumers must **not** conflate the **child** with the **whole
container**.
**Boundary status (NOT the whole medulla oblongata — a
somatosensory relay within it):** **Boundary case — the
cuneate nucleus is NOT the whole medulla oblongata.** The
**medulla oblongata** (``.../medulla_oblongata/``) is the
**parent container** — it contains the cuneate nucleus (via
the respiratory_center) **plus** the cranial nerve nuclei, the
autonomic nuclei, the olivary body, the medullary pyramid, the
arcuate nucleus, the parafacial zone, the paramedian reticular
nucleus, the perihypoglossal nuclei, the respiratory_center,
and other structures. The **cuneate nucleus** is **one
somatosensory relay** within the medulla. Consumers must **not**
conflate the **cuneate nucleus** with the **whole medulla**.
**Boundary status (BILATERAL container — left and right are
ANATOMICALLY SEPARATE structures):** **Boundary case — the
cuneate nucleus is a BILATERAL container whose left and right
children are ANATOMICALLY SEPARATE.** Unlike the **area
postrema** (a **midline** organ wired as left/right by
convention), the **cuneate nucleus** is a **truly paired**
medullary structure — the **left cuneate nucleus** relays
**left upper-body** sensation (via the **left cuneate
fasciculus**) and the **right cuneate nucleus** relays **right
upper-body** sensation (via the **right cuneate fasciculus**).
**The left / right split here is ANATOMICAL, not a wiring
convention.** Consumers must **not** infer **midline wiring
convention** from the cuneate nucleus (that convention applies
to the area postrema / CTZ, NOT the cuneate nucleus).

Overview
--------
The **cuneate nucleus (nucleus cuneatus)** — also known as the
**nucleus of Burdach** — is a **dorsal column nucleus** in the
**medulla oblongata**. It is the **first central relay** of the
**dorsal column–medial lemniscus pathway** for the **upper
body** (arms, upper trunk, neck). It **receives** primary
afferent axons from the **ipsilateral cuneate fasciculus**
(carrying fine touch, vibration, and conscious proprioception
from the upper body), **relays** them to **second-order
neurons**, whose axons **decussate** as the **internal arcuate
fibers** and **ascend** as the **medial lemniscus** to the
**contralateral thalamus** (VPL).

**The cuneate nucleus is a SOMATOSENSORY relay, NOT a
respiratory nucleus.** Although it is wired under
``respiratory_center``, its **primary function** is **fine
touch, vibration, and conscious proprioception** from the
**upper body** — **NOT** **breathing**. The **"respiratory_center"**
label is a **tree-wiring artifact** — the tree groups the
cuneate nucleus with the area postrema, chemoreceptor trigger
zone, dorsal respiratory group, gigantocellular reticular
nucleus, and gracile nucleus as a **pragmatic cluster** for
brainstem organization. Consumers must **not** infer
**respiratory function** from **container membership**.

**The cuneate nucleus is TRULY BILATERAL — the left / right
split is ANATOMICAL.** Unlike the **area postrema** (a
**midline** organ wired as left/right by convention), the
**left** and **right** cuneate nuclei are **anatomically
separate structures**. The **left cuneate nucleus** relays
**left upper-body** sensation (via the **left cuneate
fasciculus**); the **right cuneate nucleus** relays **right
upper-body** sensation (via the **right cuneate fasciculus**).
The **left / right split** here reflects **anatomy** — **NOT**
a **tree-wiring convention**.

**The cuneate nucleus is a DORSAL COLUMN NUCLEUS — NOT the
gracile nucleus, NOT the accessory cuneate nucleus, NOT the
trigeminal nuclei, NOT the spinothalamic tract.** It is
**specifically** the **upper-body dorsal column relay** — the
**gracile nucleus** is the **lower-body** counterpart; the
**accessory cuneate nucleus** is the **spinocerebellar** relay
(unconscious proprioception); the **trigeminal nuclei** are the
**facial** somatosensory system; and the **spinothalamic
tract** carries **pain and temperature**, **NOT** dorsal column
sensation.

**The cuneate nucleus is functionally coupled to the gracile
nucleus, the medial lemniscus, the VPL thalamus, and the
primary somatosensory cortex (S1).** It is **part of** the
**dorsal column–medial lemniscus pathway** — a **three-neuron
ascending pathway** that relays **fine touch, vibration, and
conscious proprioception** from the body to the cortex.

Bilateral Structure (Anatomical Pairing)
---------------------------------------
The cuneate nucleus is a **bilateral container** in this tree
with **two structural children**:

*   ``left`` — the **left** cuneate nucleus (a **leaf** module).
*   ``right`` — the **right** cuneate nucleus (a **leaf**
    module).

**The two children are ANATOMICALLY SEPARATE structures** —
**NOT** a wiring convention for a midline organ (unlike the
area postrema / CTZ). The **left cuneate nucleus** relays
**left upper-body** sensation; the **right cuneate nucleus**
relays **right upper-body** sensation.

**Each side is a leaf.** The ``left`` and ``right`` modules each
contain only ``__init__.py`` — they represent the **left-side**
and **right-side** **cuneate nuclei** as **single structures**.
Consumers that need **side-specific** resolution descend into
``left`` or ``right``; consumers that need the **whole
bilateral pair** use ``cuneate_nucleus`` (the container) as a
whole.

**The container itself is unpaired.** There is **no**
``cuneate_nucleus/left/.../`` structural hierarchy beyond the
single leaf level — the ``left`` and ``right`` modules are the
**terminal modules** for this structure.

The Cuneate Nucleus / Gracile Nucleus Boundary
----------------------------------------------
This is the **most consequential** dorsal-column nucleus
boundary:

*   **Cuneate nucleus** (this module) — the **upper-body** dorsal
    column relay.

*   **Gracile nucleus**
    (``.../respiratory_center/gracile_nucleus/``) — the
    **lower-body** dorsal column relay.

**They are DIFFERENT NUCLEI** — both are **dorsal column nuclei**
— children of ``respiratory_center`` — but they serve **different
body regions**. The **cuneate nucleus** is **lateral** to the
gracile nucleus; the **gracile nucleus** is **medial** to the
cuneate nucleus. Consumers must **not** conflate the two.

The Cuneate Nucleus / Accessory Cuneate Nucleus Boundary
--------------------------------------------------------
This is the **dorsal column / spinocerebellar** boundary:

*   **Cuneate nucleus** (this module) — the **upper-body** dorsal
    column relay (conscious proprioception, fine touch,
    vibration, via the **medial lemniscus** to the **VPL
    thalamus**).

*   **Accessory cuneate nucleus** — the **spinocerebellar** relay
    (unconscious proprioception, via the **posterior
    spinocerebellar tract** to the **cerebellum**).

**They are DIFFERENT NUCLEI** with **DIFFERENT functions** — the
**accessory cuneate nucleus** is **dorsolateral** to the main
cuneate nucleus and is **NOT wired** in this tree. Consumers
must **not** conflate the two.

The Cuneate Nucleus / Medial Lemniscus and Internal Arcuate Fibers Boundary
---------------------------------------------------------------------------
This is the **nucleus / white-matter tract** boundary:

*   **Cuneate nucleus** (this module) — the **grey-matter relay**.

*   **Medial lemniscus** — the **white-matter tract** that carries
    the **second-order axons** to the **VPL thalamus**.

*   **Internal arcuate fibers** — the **decussating axons** of
    the cuneate (and gracile) nuclei.

**The cuneate nucleus PROJECTS TO the medial lemniscus via the
internal arcuate fibers** — but the **nucleus** is **NOT** the
**tract**, and **NOT** the **decussating axons**. Consumers must
**not** conflate the **nucleus** with the **white-matter
structures** it projects through.

The Cuneate Nucleus / Trigeminal Nuclei and Spinothalamic Tract Boundary
------------------------------------------------------------------------
This is the **dorsal column / other somatosensory** boundary:

*   **Cuneate nucleus** (this module) — the **upper-body** dorsal
    column relay (fine touch, vibration, conscious
    proprioception).

*   **Trigeminal nuclei** — the **facial** somatosensory system.

*   **Spinothalamic tract** — the **pain and temperature** system.

**They are DIFFERENT SOMATOSENSORY SYSTEMS** — the **cuneate
nucleus** is a **dorsal column relay**; the **trigeminal nuclei**
carry **facial** sensation; the **spinothalamic tract** carries
**pain and temperature**. Consumers must **not** conflate the
three.

The Cuneate Nucleus / VPL Thalamus and Primary Somatosensory Cortex Boundary
----------------------------------------------------------------------------
This is the **medullary relay / higher-order relays** boundary:

*   **Cuneate nucleus** (this module) — the **second-order
    medullary relay**.

*   **VPL thalamus** — the **third-order thalamic relay**.

*   **Primary somatosensory cortex (S1)** — the **fourth-order
    cortical target**.

**They are DIFFERENT STRUCTURES** at **different levels** of the
**dorsal column–medial lemniscus pathway**. Consumers must **not**
conflate them.

The Cuneate Nucleus / Other Respiratory Center Children Boundary
----------------------------------------------------------------
This is the **somatosensory / respiratory-and-circumventricular**
boundary:

*   **Cuneate nucleus** (this module) — the **somatosensory
    relay**.

*   **Area postrema** and **chemoreceptor trigger zone**
    (``.../area_postrema/`` and
    ``.../chemoreceptor_trigger_zone/``) — the
    **circumventricular / chemosensory** structures.

*   **Dorsal respiratory group**
    (``.../dorsal_respiratory_group/``) — the **respiratory**
    pattern generator.

*   **Gigantocellular reticular nucleus**
    (``.../gigantocellular_reticular_nucleus/``) — the **large
    medullary reticular** nucleus.

*   **Gracile nucleus** (``.../gracile_nucleus/``) — the
    **lower-body** dorsal column relay.

**They are DIFFERENT STRUCTURES** — all six are **children** of
``respiratory_center``, but they are **functionally distinct**.
Consumers must **not** conflate the **cuneate nucleus** with any
of these.

The Cuneate Nucleus / Whole Respiratory Center and Whole Medulla Oblongata Boundary
-----------------------------------------------------------------------------------
This is the **child / container** boundary:

*   **Cuneate nucleus** (this module) — one **child** of
    ``respiratory_center``.

*   **Respiratory center** (``.../respiratory_center/``) — the
    **parent container** of **six children**.

*   **Medulla oblongata** (``.../medulla_oblongata/``) — the
    **parent container** of the **respiratory_center** and other
    medullary structures.

**The cuneate nucleus is a CHILD of respiratory_center, NOT the
container itself, and NOT the whole medulla.** Consumers must
**not** conflate the **child** with either **parent container**.

Function in the Human Brain
---------------------------
The cuneate nucleus's function is **somatosensory relay** for
the **upper body** — **NOT respiratory rhythm** and **NOT motor
control**:

*   **Fine touch, vibration, and conscious proprioception relay
    (upper body):** The **cuneate nucleus** receives **primary
    afferent axons** from the **ipsilateral cuneate fasciculus**
    (carrying **fine touch, vibration, and conscious
    proprioception** from the **upper body** — arms, upper
    trunk, neck) and **relays** them to **second-order neurons**
    whose axons **decussate** as the **internal arcuate fibers**
    and **ascend** as the **medial lemniscus** to the
    **contralateral VPL thalamus**.

*   **Somatotopic organization:** The **cuneate nucleus** is
    **somatotopically organized** — the **upper limb** is
    represented **dorsomedially**; the **neck** is represented
    **ventrolaterally** (or similar — the exact map varies by
    species). This **somatotopy** is preserved in the **medial
    lemniscus** and the **VPL thalamus**.

*   **Upper-body sensory discrimination:** The **cuneate nucleus**
    is **part of** the **neural substrate** for **fine sensory
    discrimination** of the **upper body** — the **ability** to
    **detect** and **localize** **subtle** **tactile**,
    **vibratory**, and **proprioceptive** stimuli on the
    **arms, hands, upper trunk, and neck**.

*   **NOT respiratory rhythm:** The **cuneate nucleus** does
    **not** generate the **respiratory rhythm** — that is the
    **pre-Bötzinger complex** (VRG) and the **respiratory**
    centers. The **cuneate nucleus** is a **somatosensory**
    relay — **NOT** a respiratory nucleus.

*   **NOT motor control:** The **cuneate nucleus** does **not**
    send motor axons to muscles.

**The unifying theme:** the cuneate nucleus is the
**upper-body** **dorsal column** somatosensory relay in the
**medulla** — it **relays** **fine touch, vibration, and
conscious proprioception** from the **upper body** to the
**contralateral VPL thalamus** via the **medial lemniscus** —
**NOT** a respiratory nucleus, **NOT** the gracile nucleus,
**NOT** the accessory cuneate nucleus, **NOT** the trigeminal
nuclei, and **NOT** the spinothalamic tract.

Associated Disorders
--------------------
The cuneate nucleus is the **substrate** for **well-defined
clinical syndromes** — its clinical relevance is **direct**,
via **dorsal column somatosensory** dysfunction:

*   **Dorsal column sensory loss — upper body (via cuneate
    nucleus dysfunction):** **Lesions** of the **cuneate
    nucleus** (from **stroke**, **demyelination**,
    **tumor**, **vitamin B12 deficiency** — subacute combined
    degeneration, or **tabes dorsalis**) cause **loss of fine
    touch, vibration, and proprioception** from the **upper
    body** — **arms, hands, upper trunk, neck** — on the
    **ipsilateral** side (because the **decussation** of the
    dorsal column–medial lemniscus pathway occurs **above** the
    cuneate nucleus, in the **medulla**, via the **internal
    arcuate fibers**). **A lesion at or below the cuneate
    nucleus** produces **ipsilateral** upper-body sensory loss;
    a **lesion above the decussation** (e.g., in the **medial
    lemniscus**) produces **contralateral** upper-body sensory
    loss.

*   **Subacute combined degeneration (via dorsal column —
    including cuneate nucleus — dysfunction):** **Vitamin B12
    deficiency** causes **demyelination** of the **dorsal
    columns** (including the **cuneate fasciculus**) and the
    **lateral corticospinal tracts** — producing **loss of
    vibration and proprioception** (upper and lower body) plus
    **spastic weakness**. The **cuneate nucleus** is the
    **upper-body central relay** affected in this condition.

*   **Tabes dorsalis (via dorsal column — including cuneate
    nucleus — dysfunction):** **Neurosyphilis** causes
    **demyelination** of the **dorsal columns** (including
    the **cuneate fasciculus**) and the **dorsal roots** —
    producing **impaired proprioception**, **sensory ataxia**,
    and **Romberg sign**. The **cuneate nucleus** is the
    **upper-body central relay** affected in this condition.

*   **Brainstem stroke (via cuneate nucleus involvement):**
    **Lateral medullary syndrome (Wallenberg)** can **involve**
    the **cuneate nucleus** (or the **cuneate fasciculus**
    rostrally) — contributing to **ipsilateral upper-body
    sensory loss**.

*   **Cuneate fasciculus lesions — upper body sensory loss
    (contrast — peripheral / spinal cord):** **Lesions** of
    the **cuneate fasciculus** in the **spinal cord** (from
    **trauma**, **tumor**, **MS**, **B12 deficiency**, or
    **tabes dorsalis**) cause **similar** upper-body sensory
    loss — but the **cuneate fasciculus** is a **white-matter
    tract** in the **spinal cord**, **NOT** the **cuneate
    nucleus** in the **medulla**. Consumers must **not**
    conflate the two.

*   **No Named "Cuneate Nucleus Syndrome":** The cuneate nucleus
    is a **somatosensory relay** — its clinical syndromes are
    **named for the broader lesion** (dorsal column syndrome,
    subacute combined degeneration, tabes dorsalis, brainstem
    stroke) or the **pattern of sensory loss** — **NOT** for the
    nucleus itself.

**What is NOT here:** The cuneate nucleus is **not** the substrate
for **respiratory rhythm** (VRG, pre-Bötzinger complex),
**central hypoventilation** (VRG), **emesis** (area postrema /
chemoreceptor trigger zone), **sympathetic premotor** function
(RVLM), **visceral afferent relay** (NTS), **tongue weakness**
(hypoglossal nucleus), or **pain and temperature loss**
(spinothalamic tract). Its clinical relevance is the **upper-body
dorsal column somatosensory** functions listed above.

Lateralization Notes
--------------------
The cuneate nucleus is a **bilateral container** in this tree with
``left`` and ``right`` structural children. There is **no**
``cuneate_nucleus/left/.../`` structural hierarchy beyond the
single leaf level.

*   **Bilateral structural children (ANATOMICAL pairing):**
    ``left`` and ``right`` are **leaf modules** — each represents
    the **left** or **right** cuneate nucleus as a **single
    structure**. The **left** and **right** cuneate nuclei are
    **anatomically separate structures** (unlike the **area
    postrema**, which is a **midline** organ wired as left/right
    by convention). The **left** cuneate nucleus relays **left
    upper-body** sensation (via the **left cuneate fasciculus**);
    the **right** cuneate nucleus relays **right upper-body**
    sensation (via the **right cuneate fasciculus**).

*   **Ipsilateral vs. contralateral — CRITICAL DISTINCTION:** The
    cuneate nucleus itself relays **ipsilateral** upper-body
    sensation (the **cuneate fasciculus** is **ipsilateral** to
    the receptors). **After the cuneate nucleus**, the pathway
    **decussates** (via the **internal arcuate fibers**) —
    becoming the **contralateral** medial lemniscus. **A lesion
    AT the cuneate nucleus** produces **ipsilateral** upper-body
    sensory loss; a **lesion ABOVE the decussation** produces
    **contralateral** upper-body sensory loss. This is a
    **classic localization principle** — analogous to the
    hypoglossal nucleus / corticobulbar distinction.

*   **NO lateralization warning:** The cuneate nucleus has **no
    known functional lateralization** in humans — the **left**
    and **right** cuneate nuclei are **functionally symmetric**
    (each relays **its own side's** upper-body sensation). This
    is **symmetric lateralization** — each side handles **one
    body side** — **NOT** a lateralization **warning** in the
    frontotemporal_cortical_system sense (which concerns
    asymmetric function). Consumers must **not** import a
    **lateralization warning** into the cuneate nucleus — the
    **left** and **right** nuclei are **functionally symmetric**.

*   **NO Extended-Amygdala / SLEA Warning:** The cuneate nucleus
    is **SLEA-free** — it is **not** an extended-amygdala
    component. Consumers must **not** import the SLEA warning
    into the cuneate nucleus.

*   **NO Fear-Output Warning:** The cuneate nucleus is **not** a
    fear-output structure — it is a **dorsal column somatosensory**
    relay. Consumers must **not** conflate it with the **central
    nucleus** or with the **amygdala**.

**A consumer that assumes "left cuneate nucleus = right cuneate
nucleus" will be structurally correct** — the two sides are
**symmetric** and **functionally equivalent** at the **nucleus
level** (each relays **its own side's** upper-body sensation).
The cuneate nucleus is a **strict-mirror pair with NO warning** —
**no SLEA warning**, **no fear-output warning**, and **no
lateralization warning**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The cuneate nucleus is a
    **bilateral container** — it does **not** import from
    ``left/`` or ``right/`` at the container level. The ``left``
    and ``right`` leaves are **independent** modules.
*   **No cross-lobe imports.** This module does **not** import
    from ``.../gracile_nucleus/``,
    ``.../area_postrema/``,
    ``.../chemoreceptor_trigger_zone/``,
    ``.../dorsal_respiratory_group/``,
    ``.../gigantocellular_reticular_nucleus/``,
    ``.../solitary_nucleus/``,
    ``.../cranial_nerve_nuclei/``, or any other container. The
    cuneate nucleus's relationships to the gracile nucleus,
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
    right cuneate nuclei are **truly separate bilateral
    structures** — the **left / right split** is **ANATOMICAL**,
    **NOT** a **tree-wiring convention**.
*   **SOMATOSENSORY RELAY, NOT a respiratory nucleus.** Although
    wired under ``respiratory_center``, the cuneate nucleus is a
    **dorsal column somatosensory** relay — **NOT** a respiratory
    rhythm generator, **NOT** a respiratory pattern generator,
    **NOT** a respiratory-chemoreceptor, and **NOT** a
    respiratory-related structure of any kind.
*   **TREE-WIRING ARTIFACT caveat — the "respiratory_center" label
    is NOT a claim about function.** The cuneate nucleus is
    **somatosensory**; the **respiratory_center** label reflects
    a **pragmatic tree cluster**, **NOT** a functional
    classification.
*   **NOT the gracile nucleus.** The **gracile nucleus** is the
    **lower-body** counterpart — a **different structure**.
*   **NOT the accessory cuneate nucleus.** The **accessory cuneate
    nucleus** is the **spinocerebellar** relay — **NOT wired** in
    this tree.
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
    oblongata.** The cuneate nucleus is a **child** of
    ``respiratory_center``, not the container itself.
*   **No ``AREA_PATHS`` hop.** The cuneate nucleus is a **local
    container** — it is not cross-listed under another brainparts
    path.
*   **No nested cross-listing.** The cuneate nucleus has no
    nested dual-framing module. It is a **bilateral container**
    with **two leaf children** (anatomical pairing).
*   **Structural parity with the right side — strict mirror.**
    The ``left`` and ``right`` leaves are **structurally
    identical** — same leaf status, same **dorsal column
    somatosensory** framing, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.hindbrain.myelencephalon.medulla_oblongata.respiratory_center import cuneate_nucleus

Or by fully-qualified path string::

    path = (
        "hindbrain.myelencephalon.medulla_oblongata."
        "respiratory_center.cuneate_nucleus"
    )

**Do not** infer **respiratory function** from membership in the
respiratory_center. The cuneate nucleus is a **dorsal column
somatosensory** relay — **NOT** a respiratory nucleus. The
**"respiratory_center"** label is a **tree-wiring artifact**.

**Do not** assume the cuneate nucleus is the **gracile nucleus**.
The gracile nucleus is the **lower-body** counterpart — a
**different structure**.

**Do not** assume the cuneate nucleus is the **accessory cuneate
nucleus**. The accessory cuneate nucleus is the
**spinocerebellar** relay — **NOT wired** in this tree.

**Do not** assume the cuneate nucleus is the **medial lemniscus**
or the **internal arcuate fibers**. Those are **white-matter
structures** — the **nucleus** projects to them, but is **NOT**
them.

**Do not** assume the cuneate nucleus is the **trigeminal
nuclei** or the **spinothalamic tract**. Those are **different
somatosensory systems**.

**Do not** assume the cuneate nucleus is the **VPL thalamus** or
the **S1 cortex**. Those are **higher-order relays** in the
**dorsal column–medial lemniscus pathway**.

**Do not** assume the cuneate nucleus is the **whole
respiratory_center** or the **whole medulla oblongata**. It is
a **child** of ``respiratory_center``.

**Do not** infer **midline wiring convention** from the cuneate
nucleus structure. The **left / right split** is **ANATOMICAL**
— the **left** and **right** cuneate nuclei are **truly separate
bilateral structures** (unlike the area postrema / CTZ, which
are midline organs wired as left/right by convention).

Iterating the cuneate nucleus's structural children (recommended
consumer pattern)::

    CUNEATE_NUCLEUS_CHILDREN = ("left", "right")
    # Each child is a leaf module representing the left or right
    # cuneate nucleus. Anatomically, the left and right cuneate
    # nuclei are TRULY SEPARATE bilateral structures — the
    # left/right split is ANATOMICAL, NOT a wiring convention.

Reaching the left and right cuneate nuclei (recommended consumer
pattern)::

    # The left and right cuneate nuclei are:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus.left
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.cuneate_nucleus.right
    #
    # Each is a leaf module representing the cuneate nucleus of
    # that side. Anatomically, they are TRULY SEPARATE bilateral
    # structures.

Reaching the gracile nucleus (recommended consumer pattern —
NOTE the DIFFERENT child of respiratory_center)::

    # The gracile nucleus is a SEPARATE child of respiratory_center
    # in this tree — the LOWER-BODY counterpart of the cuneate
    # nucleus:
    #
    #   hindbrain.myelencephalon.medulla_oblongata.respiratory_center.gracile_nucleus
    #
    # Both are DORSAL COLUMN NUCLEI — children of
    # respiratory_center — but they serve DIFFERENT BODY REGIONS:
    # the cuneate nucleus relays UPPER-BODY sensation; the
    # gracile nucleus relays LOWER-BODY sensation.

Reaching the medial lemniscus and internal arcuate fibers
(recommended consumer pattern — NOTE the DIFFERENT structures)::

    # The medial lemniscus is a WHITE-MATTER TRACT; the internal
    # arcuate fibers are the DECUSSATING AXONS of the cuneate
    # (and gracile) nuclei:
    #
    #   (medial lemniscus — white-matter tract in the medulla,
    #    pons, and midbrain)
    #   (internal arcuate fibers — decussating axons from the
    #    cuneate and gracile nuclei)
    #
    # The cuneate nucleus PROJECTS TO the medial lemniscus via
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
    # The cuneate nucleus is a DORSAL COLUMN relay for
    # fine touch, vibration, and conscious proprioception from
    # the UPPER BODY — NOT facial sensation, NOT pain/temperature.

Reaching the VPL thalamus and S1 cortex (recommended consumer
pattern — NOTE the DIFFERENT levels of the pathway)::

    # The VPL thalamus and S1 cortex are HIGHER-ORDER RELAYS in
    # the dorsal column–medial lemniscus pathway:
    #
    #   (VPL thalamus — third-order relay in the thalamus)
    #   (S1 cortex — fourth-order target in the postcentral gyrus)
    #
    # The cuneate nucleus is the SECOND-ORDER MEDULLARY relay —
    # NOT the thalamus, NOT the cortex.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        path = (
            f"hindbrain.myelencephalon.medulla_oblongata."
            f"respiratory_center.cuneate_nucleus.{side}"
        )
        # resolve path through the memory/recall layer
        # NOTE: the left and right cuneate nuclei are TRULY
        # SEPARATE bilateral structures (ANATOMICAL, not a
        # wiring convention).

References
----------
*   **Canonical brainstem anatomy:** Brodal, A. (2010). *The
    Central Nervous System: Structure and Function*, 4th ed.
    (Cuneate nucleus; dorsal column–medial lemniscus pathway;
    somatotopic organization; internal arcuate fibers.)
*   **Dorsal column–medial lemniscus pathway — overview:**
    Tracey, D.J. (2004). "Ascending and descending pathways."
    In: Paxinos, G. (ed.), *The Rat Nervous System*, 3rd ed.
    (Dorsal column nuclei; cuneate nucleus; gracile nucleus;
    medial lemniscus; internal arcuate fibers.)
*   **Cuneate nucleus — somatotopy:** Millar, J., Basbaum, A.I.
    (1975). "Topography of the projection of the body surface
    of the rat to the cuneate nucleus." *Experimental
    Neurology* 49:841–858. (Somatotopic organization of the
    cuneate nucleus.)
*   **Cuneate nucleus — anatomy and connections:** Berkley, K.J.,
    et al. (1986). "Somatosensory projections to the cuneate
    nucleus." *Journal of Comparative Neurology* 253:222–236.
    (Cuneate nucleus; primary afferent input; projections to
    the medial lemniscus.)
*   **Dorsal column nuclei — anatomy:** Rustioni, A., Weinberg,
    R.J. (1989). "Somatosensory system: the dorsal column
    nuclei." In: *The Human Nervous System* (Paxinos, G., ed.).
    (Dorsal column nuclei; cuneate and gracile nuclei;
    somatosensory pathways.)
*   **Accessory cuneate nucleus (contrast — spinocerebellar):**
    Grant, G. (1962). "Spinal course and somatotopically
    localized termination of the spinocerebellar tracts."
    *Acta Physiologica Scandinavica* 56(Suppl. 204):1–45.
    (Accessory cuneate nucleus; posterior spinocerebellar tract;
    unconscious proprioception — DIFFERENT from the main cuneate
    nucleus.)
*   **Subacute combined degeneration — dorsal column:**
    Hemmer, B., et al. (1998). "Subacute combined degeneration:
    clinical, electrophysiological, and magnetic resonance
    imaging findings." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 65:822–827. (Vitamin B12 deficiency; dorsal
    column dysfunction; cuneate and gracile nuclei.)
*   **Tabes dorsalis — dorsal column:** Timmermans, M., Carr,
    J. (2004). "Neurosyphilis." *Current Opinion in Infectious
    Diseases* 17:49–54. (Tabes dorsalis; dorsal column
    dysfunction; cuneate and gracile nuclei; neurosyphilis.)
*   **Lateral medullary syndrome (Wallenberg):** Sacco, R.L., et
    al. (1993). "Lateral medullary infarction: clinical and MRI
    correlation." *Stroke* 24:1981–1987. (Wallenberg syndrome;
    cuneate nucleus involvement; upper-body sensory loss.)
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
*   NeuroNames — Nucleus cuneatus; FMA — Cuneate nucleus.
"""