"""
infrastructure.brainparts.forebrain.telencephalon.commissures
=============================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    ├── cerebral_hemispheres
    ├── commissures   <-- THIS MODULE (CONTAINER)
    │   ├── anterior_commissure
    │   └── corpus_callosum
    └── lateral_ventricles

**Primary synonym:** Commissures (of the telencephalon); forebrain
commissures; telencephalic commissures; **the commissural white-matter
container of the telencephalon**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container module** — the **commissural white-matter compartment**
of the **telencephalon**, containing **two structural children**:

*   ``corpus_callosum`` — the **neocortical commissure** — the
    **largest commissure** in the human brain.
*   ``anterior_commissure`` — the **anterior commissure** —
    connecting the **anterior temporal lobes** and the
    **olfactory structures**.

**Part of:** The **telencephalon** container — the **commissural
white-matter compartment** of the telencephalon. The **commissures**
container is the **parent of the two commissural white-matter
leaves** — **both of which are commissural white matter**, **both
of which cross the midline**.
**Structural parent:** ``.../telencephalon/`` → **direct child**
of the telencephalon container.
**Structural children:** **YES — this is a CONTAINER module, not a
leaf.** Its **two structural children** are:

*   ``.../commissures/corpus_callosum/`` — a **leaf**.
*   ``.../commissures/anterior_commissure/`` — a **leaf**.

Consumers **may** import these children; the commissures container
is the **structural parent** of the commissural white-matter
leaves, not a leaf.
**Boundary status (CONTAINER — NOT a leaf and NOT a single
commissure):** **Boundary case — the commissures is a CONTAINER
module with TWO structural children, not a leaf and not a single
commissure.** The **corpus callosum** and the **anterior
commissure** are **separate structural leaves** — consumers must
**not** assume the commissures is a single commissure (e.g., "the
commissures = the corpus callosum"), and must **not** assume the
commissural leaves are prose under a container. They are **wired
children** with their own modules.
**Boundary status (MIDLINE CONTAINER — NOT a left/right paired
container):** **Boundary case — the commissures is a MIDLINE
container, NOT a left/right paired container.** Unlike every other
container in the cerebral hemisphere (`cortex/`, `subcortical/`,
`white_matter/`, `lateral_ventricles/`), the **commissures
container is a MIDLINE structure** — it is **NOT** duplicated into
`left/commissures/` and `right/commissures/`. The **corpus
callosum** and the **anterior commissure** are **midline
commissures** that **cross the midline** to connect the two
hemispheres (in the corpus callosum) or the two anterior temporal
lobes (in the anterior commissure). **There is only ONE
`commissures/` container** — the one documented here. Consumers
must **not** look for `left/commissures/` or `right/commissures/`
— those paths **do not exist**.
**Boundary status (COMMISSURAL WHITE MATTER — NOT the ipsilateral
white matter of the cerebral hemispheres):** **Boundary case —
the commissures is COMMISSURAL WHITE MATTER, NOT the ipsilateral
white matter of the cerebral hemispheres.** The **commissures**
(here) is the **compartment of midline-crossing (commissural)
white-matter fibers** — the **corpus callosum** and the
**anterior commissure**, both of which **cross the midline** to
connect the two hemispheres (or the two anterior temporal
lobes). The **ipsilateral white matter** — the **centrum
semiovale**, the **cingulum**, the **corona radiata**, the
**external capsule**, the **extreme capsule**, the **fasciculus
rectus**, the **fornix**, the **internal capsule**, the
**mammillothalamic tract**, and the **medial forebrain bundle**
— is the **white-matter compartment of each cerebral hemisphere**,
wired under ``.../left/white_matter/`` and
``.../right/white_matter/``. **They are DIFFERENT
COMPARTMENTS** — the **commissures** is the **midline-crossing
(commissural)** white matter; the **white_matter** is the
**ipsilateral** white matter of each cerebral hemisphere.
Consumers must **not** conflate the commissures container with
the cerebral hemisphere white-matter container.
**Boundary status (NOT the cerebral_hemispheres container — the
cerebral_hemispheres is the GREY-MATTER + IPSILATERAL WHITE-MATTER
sibling):** **Boundary case — the commissures is NOT the
cerebral_hemispheres container; the cerebral_hemispheres is the
grey-matter + ipsilateral-white-matter sibling.** The
**cerebral_hemispheres** container
(``.../telencephalon/cerebral_hemispheres/``) holds the **left
hemisphere** and the **right hemisphere** — each of which
contains the **cortex**, the **rhinencephalon**, the
**subcortical** structures, the **white_matter**, and the
**lateral_ventricles**. The **commissures** (here) is the
**commissural white matter** — a **separate compartment** that
**connects** the two hemispheres. **They are SIBLINGS under the
telencephalon, and they are DIFFERENT COMPARTMENTS** — the
**cerebral_hemispheres** is the **grey-matter + ipsilateral-white-
matter** compartment; the **commissures** is the **commissural
white matter**. Consumers must **not** conflate the commissures
container with the cerebral_hemispheres container.
**Boundary status (NOT the lateral_ventricles container — the
lateral_ventricles is the CSF-space sibling):** **Boundary case
— the commissures is NOT the lateral_ventricles container; the
lateral_ventricles is the CSF-space sibling.** The
**lateral_ventricles** container
(``.../telencephalon/lateral_ventricles/``) holds the **left
lateral ventricle** and the **right lateral ventricle** — the
**CSF-filled spaces** inside the cerebral hemispheres. The
**commissures** (here) is the **commissural white matter**.
**They are SIBLINGS under the telencephalon, and they are
DIFFERENT COMPARTMENTS** — the **lateral_ventricles** is the
**CSF-space** compartment; the **commissures** is the
**commissural white matter**. Consumers must **not** conflate the
commissures container with the lateral_ventricles container.
**Boundary status (NOT the corpus_callosum or anterior_commissure
— those are the CHILDREN):** **Boundary case — the commissures is
NOT the corpus_callosum or the anterior_commissure; those are the
CHILDREN.** The **corpus callosum**
(``.../commissures/corpus_callosum/``) and the **anterior
commissure** (``.../commissures/anterior_commissure/``) are the
**two structural children** of the commissures container.
Consumers must **not** conflate the commissures container with
either of its children.
**Boundary status (NOT the telencephalon container — the
commissures is a CHILD of the telencephalon):** **Boundary case —
the commissures is a CHILD of the telencephalon container, not the
container itself.** The **telencephalon** container contains the
**cerebral_hemispheres**, the **commissures**, and the
**lateral_ventricles** — the **commissures** is **one** of those
three children. Consumers must **not** conflate the commissures
container with the telencephalon container.
**Boundary status (NOT a grey-matter structure — the commissures
is WHITE MATTER):** **Boundary case — the commissures is WHITE
MATTER, NOT a grey-matter structure.** The **commissures** (here)
is the **commissural white-matter compartment** — **myelinated
axons** (commissural projection fibers). The **grey-matter
structures** of the telencephalon — the **cortex**, the
**rhinencephalon**, the **subcortical** structures — are **grey
matter** and are wired under the **cerebral_hemispheres**
container. **They are DIFFERENT COMPARTMENTS** — the
**commissures** is the **commissural white matter**; the
**cortex**, **rhinencephalon**, and **subcortical** structures are
the **grey-matter compartments**. Consumers must **not** conflate
the commissures container with any grey-matter container.
**Boundary status (NOT a single uniform commissure — TWO structural
children with DIFFERENT functions):** **Boundary case — the
commissures is a HETEROGENEOUS compartment with TWO structural
children and TWO different functions, not a single uniform
commissure.** The **two children** are **functionally distinct** —
the **corpus callosum** is the **neocortical commissure** (the
**largest** commissure in the human brain, connecting the
**neocortical** areas of the two hemispheres); the **anterior
commissure** is the **anterior-temporal / olfactory commissure**
(connecting the **anterior temporal lobes** and the **olfactory
structures**). **Each child is functionally distinct** — the tree
wires them as **separate structural children** of the commissures
container, **not** as a single uniform commissure. Consumers must
**not** treat the commissures container as a single uniform
structure — it is a **compartment** of **two distinct commissural
white-matter structures**.
**Boundary status (SLEA-FREE — the commissures is NOT an
extended-amygdala component):** **Boundary case — the commissures
is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **commissures** is a **commissural white-matter
compartment** — it is **NOT** an extended-amygdala component, and
it carries **NO SLEA warning**. Consumers must **not** import the
SLEA warning into the commissures — it is **SLEA-free**.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case —
the commissures is NOT the fear-output or the fear-learning
structures.** The **central nucleus** (fear-output) and the
**basolateral nuclei** (fear-learning) are **amygdala** children.
The **commissures** is a **commissural white-matter compartment**
— it is **not** a fear-output or fear-learning structure.
Consumers must **not** conflate the commissures with the
**amygdala fear circuit**.

Overview
--------
The commissures container is the **commissural white-matter
compartment** of the **telencephalon** — the **parent of the two
commissural white-matter leaves** (the **corpus callosum** and
the **anterior commissure**). It is a **container** module under
the telencephalon container, the **sibling of the
cerebral_hemispheres and the lateral_ventricles**, and the
**commissural white-matter substrate** of the **interhemispheric
transfer** (via the corpus callosum) and the
**anterior-temporal / olfactory transfer** (via the anterior
commissure).

**The commissures is a CONTAINER, not a leaf.** Its **two
structural children** are **wired modules**, not prose. Consumers
may import them.

**The commissures is a MIDLINE container, NOT a left/right paired
container.** The **commissures** is a **single midline
structure** — there is **no** `left/commissures/` and **no**
`right/commissures/`. The **corpus callosum** and the **anterior
commissure** **cross the midline** to connect the two hemispheres
(in the corpus callosum) or the two anterior temporal lobes (in
the anterior commissure).

**The commissures is COMMISSURAL WHITE MATTER, NOT the ipsilateral
white matter of the cerebral hemispheres.** The **commissures** is
the **compartment of midline-crossing (commissural) white-matter
fibers**. The **ipsilateral white matter** — the **centrum
semiovale**, the **cingulum**, the **corona radiata**, the
**external capsule**, the **extreme capsule**, the **fasciculus
rectus**, the **fornix**, the **internal capsule**, the
**mammillothalamic tract**, and the **medial forebrain bundle**
— is wired under ``.../left/white_matter/`` and
``.../right/white_matter/``. **They are DIFFERENT COMPARTMENTS.**

**The commissures is NOT the cerebral_hemispheres container.** The
**cerebral_hemispheres** is the **grey-matter + ipsilateral-white-
matter** sibling; the **commissures** is the **commissural white
matter**. **They are SIBLINGS under the telencephalon.**

**The commissures is NOT the lateral_ventricles container.** The
**lateral_ventricles** is the **CSF-space** sibling; the
**commissures** is the **commissural white matter**. **They are
SIBLINGS under the telencephalon.**

**The commissures is NOT the corpus callosum or the anterior
commissure.** Those are the **two children** of the commissures
container.

**The commissures is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the
**only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired
elsewhere).

**The commissures is a SINGLE MIDLINE structure, NOT a paired
structure.** Unlike every other container in the cerebral
hemispheres, the **commissures** is a **single midline container**
— it is **NOT** duplicated into a left version and a right
version. The **commissural white-matter leaves** cross the
midline to connect the two hemispheres. There is **no functional
lateralization** of the commissures per se — but the **connections
they carry** are **bidirectional between the hemispheres**, and
the **degree of lateralization** belongs to the **cortical
grey-matter structures** whose fibers they connect (see
*Lateralization Notes*).

Structural Children (wired — NOT prose)
---------------------------------------
This is a **container** module — its children are **wired
modules**, not prose:

*   ``.../commissures/corpus_callosum/`` — the **neocortical
    commissure**. A **leaf**. The **largest commissure** in the
    human brain, connecting the **neocortical** areas of the two
    hemispheres (prefrontal, premotor, motor, somatosensory,
    parietal, temporal, occipital).

*   ``.../commissures/anterior_commissure/`` — the **anterior
    commissure**. A **leaf**. Connecting the **anterior temporal
    lobes** (the **anterior temporal commissure** component) and
    the **olfactory structures** (the **olfactory commissure**
    component).

**These children are wired, not prose.** The tree wires them as
**structural children** of the commissures container — they are
**not** prose under a container. Consumers that need
**commissure-level** resolution should import them directly.

The Commissures / Cerebral Hemispheres Boundary
-----------------------------------------------
This is the **commissural white matter vs. grey-matter +
ipsilateral-white-matter** sibling boundary:

*   **Commissures** (this module) — the **commissural white
    matter** — the **corpus callosum** and the **anterior
    commissure**.

*   **Cerebral_hemispheres**
    (``.../telencephalon/cerebral_hemispheres/``) — the **left
    hemisphere** and the **right hemisphere** — each containing
    the **cortex**, the **rhinencephalon**, the **subcortical**
    structures, the **white_matter**, and the
    **lateral_ventricles**.

**They are SIBLINGS under the telencephalon, and they are DIFFERENT
COMPARTMENTS** — the **cerebral_hemispheres** is the **grey-matter
+ ipsilateral-white-matter** compartment; the **commissures** is
the **commissural white matter**. Consumers must **not** conflate
the commissures container with the cerebral_hemispheres
container.

The Commissures / Lateral Ventricles Boundary
---------------------------------------------
This is the **commissural white matter vs. CSF-space** sibling
boundary:

*   **Commissures** (this module) — the **commissural white
    matter**.

*   **Lateral_ventricles**
    (``.../telencephalon/lateral_ventricles/``) — the **CSF-filled
    spaces** inside the cerebral hemispheres.

**They are SIBLINGS under the telencephalon, and they are DIFFERENT
COMPARTMENTS** — the **lateral_ventricles** is the **CSF-space**
compartment; the **commissures** is the **commissural white
matter**. Consumers must **not** conflate the commissures container
with the lateral_ventricles container.

The Commissures / Ipsilateral White Matter Boundary
---------------------------------------------------
This is the **commissural white matter vs. ipsilateral white
matter** boundary:

*   **Commissures** (this module) — the **commissural white
    matter** — the **corpus callosum** and the **anterior
    commissure** (midline-crossing fibers).

*   **White_matter** (``.../left/white_matter/`` and
    ``.../right/white_matter/``) — the **ipsilateral white
    matter** of each cerebral hemisphere — the **centrum
    semiovale**, the **cingulum**, the **corona radiata**, the
    **external capsule**, the **extreme capsule**, the
    **fasciculus rectus**, the **fornix**, the **internal
    capsule**, the **mammillothalamic tract**, and the **medial
    forebrain bundle**.

**They are DIFFERENT COMPARTMENTS** — the **commissures** is the
**commissural white matter**; the **white_matter** is the
**ipsilateral white matter**. **A note on the callosal
radiations:** the **corpus callosum** has **callosal radiations**
that **pass through** the hemisphere's white matter — the
**centrum semiovale** docstring documents this as **prose**
("callosal radiations"), but the **corpus callosum itself** is a
**separate structure** wired under the commissures container.
Consumers must **not** conflate the commissures container with the
cerebral hemisphere white-matter container.

The Commissures / Telencephalon Boundary
----------------------------------------
This is the **child vs. container** boundary:

*   **Commissures** (this module) — a **child** of the
    telencephalon container.

*   **Telencephalon** (``.../telencephalon/``) — the **container**
    that contains the **cerebral_hemispheres**, the
    **commissures**, and the **lateral_ventricles**.

**The commissures is ONE of the three children of the
telencephalon.** Consumers must **not** conflate the commissures
container with the telencephalon container.

The Commissures / Corpus Callosum Boundary
------------------------------------------
This is the **container vs. child** boundary:

*   **Commissures** (this module) — the **container**.

*   **Corpus_callosum**
    (``.../commissures/corpus_callosum/``) — the **neocortical
    commissure** — a **child** of the commissures container.

**The corpus callosum is ONE of the two children of the
commissures container.** Consumers must **not** conflate the
commissures container with the corpus callosum.

The Commissures / Anterior Commissure Boundary
----------------------------------------------
This is the **container vs. child** boundary:

*   **Commissures** (this module) — the **container**.

*   **Anterior_commissure**
    (``.../commissures/anterior_commissure/``) — the **anterior
    commissure** — a **child** of the commissures container.

**The anterior commissure is ONE of the two children of the
commissures container.** Consumers must **not** conflate the
commissures container with the anterior commissure.

The Commissures / SLEA Boundary
-------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Commissures** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The commissures is NOT part of the SLEA continuum.** It is a
**commissural white-matter compartment**, and it carries **no
SLEA warning**. Consumers must **not** import the SLEA warning
into the commissures.

Function in the Human Brain
---------------------------
The commissures container's functions are **interhemispheric
transfer** and **anterior-temporal / olfactory transfer** — **NOT
a grey-matter function**:

*   **Interhemispheric Transfer (Corpus Callosum):** The **corpus
    callosum** — the **larger** of the two commissures — carries
    the **neocortical commissural fibers** that **connect the two
    cerebral hemispheres** across the midline. This is the
    **interhemispheric transfer** substrate of the commissures
    container — the **anatomical substrate** of **cross-
    hemispheric integration** (sensory, motor, cognitive,
    linguistic).

*   **Anterior-Temporal / Olfactory Transfer (Anterior
    Commissure):** The **anterior commissure** — the **smaller**
    of the two commissures — carries the **anterior-temporal
    commissural fibers** (connecting the two **anterior temporal
    lobes**) and the **olfactory commissural fibers** (connecting
    the two **olfactory structures**). This is the
    **anterior-temporal / olfactory** substrate of the
    commissures container.

*   **NOT a neural processor in the classical sense.** The
    **commissures** is a **commissural white-matter compartment**
    — it **conducts** the **commissural fibers**, but it does
    **not** **process** information (that happens in the
    **grey-matter structures** — the **cortex** of the two
    hemispheres). The **fear-output** is the **central nucleus**;
    the **fear-learning** structures are the **basolateral
    nuclei**.

**The unifying theme:** the commissures is the **commissural
white-matter compartment** of the **telencephalon** — the
**parent of the two commissural white-matter leaves** that anchor
**interhemispheric transfer** and **anterior-temporal /
olfactory transfer**. It is **SLEA-free**, **commissural white
matter**, and **NOT a grey-matter container** — the
**grey-matter structures** are the **cortex** of the two
hemispheres whose fibers pass through it.

Associated Disorders
--------------------
The commissures container has **no named "commissures syndrome"** in
the narrow sense, but its clinical associations are
**well-documented** — primarily as an **interhemispheric transfer**
target:

*   **Agenesis of the Corpus Callosum (ACC):** The **corpus
    callosum** is the **most common** cerebral commissure to be
    **congenitally absent** — **agenesis of the corpus callosum**
    is a **well-characterized** congenital malformation, often
    **asymptomatic** or associated with **subtle cognitive and
    social** deficits, **epilepsy**, and **developmental
    delay**. The **corpus callosum** is the **white-matter
    substrate** of the **interhemispheric transfer** deficit in
    ACC.

*   **Split-Brain Syndrome (Callosotomy):** **Callosotomy** — the
    **surgical transection** of the **corpus callosum** (used
    historically for **intractable epilepsy**) — produces the
    **split-brain syndrome** — a **disconnection syndrome**
    characterized by **impaired interhemispheric transfer** of
    **sensory, motor, and cognitive** information. The
    **corpus callosum** is the **white-matter substrate** of the
    **split-brain** disconnection.

*   **Marchiafava-Bignami Disease:** **Marchiafava-Bignami
    disease** — a **rare** disorder characterized by
    **demyelination and necrosis** of the **corpus callosum**
    (classically associated with **chronic alcoholism**) —
    produces **interhemispheric disconnection**, **cognitive
    impairment**, and **seizures**. The **corpus callosum** is
    the **white-matter substrate** of the disease.

*   **Multiple Sclerosis (Corpus Callosum Plaques):** The **corpus
    callosum** is a **principal site** of **MS plaques** — the
    **demyelinating lesions** that are the **radiological
    hallmark** of **multiple sclerosis**. The **corpus callosum**
    (especially the **callosal-septal interface**) is a
    **well-characterized** MS lesion site (the **Dawson's
    fingers** on sagittal MRI).

*   **Alexander Disease (Leukodystrophy):** **Alexander disease**
    — a **leukodystrophy** caused by **GFAP** mutations — has a
    **predilection** for the **corpus callosum** (and the
    **frontal white matter**). The **corpus callosum** is the
    **white-matter substrate** of the **leukodystrophy** in
    Alexander disease.

*   **Schizophrenia (Callosal Abnormalities — Contested):** The
    **corpus callosum** shows **structural and DTI
    abnormalities** in **schizophrenia** — **reduced callosal
    thickness** and **reduced fractional anisotropy** are
    reported. This is **contested** — the findings are **not**
    uniformly replicated.

*   **No Named "Commissures Syndrome":** The **commissures** is a
    **commissural white-matter compartment**, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **direct** as an **interhemispheric
    transfer** target (ACC, split-brain, Marchiafava-Bignami, MS,
    Alexander disease), and **contested** for
    **schizophrenia**.

**What is NOT here:** The **commissures** is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as an **interhemispheric transfer** target, and
**contested** for **schizophrenia**.

Lateralization Notes
--------------------
This is the **single midline** commissures module. The
**commissures** is a **midline structure** — and it carries
**NO warning**:

*   **Midline Structure — NOT a Paired Structure:** The
    **commissures** is a **single midline container** — it is
    **NOT** duplicated into `left/commissures/` and
    `right/commissures/`. The **corpus callosum** and the
    **anterior commissure** are **midline commissures** that
    **cross the midline** to connect the two hemispheres (in the
    corpus callosum) or the two anterior temporal lobes (in the
    anterior commissure). There is **no left/right split** of the
    commissures themselves.

*   **Bidirectional Interhemispheric Connections:** The **corpus
    callosum** carries **bidirectional** fibers between the two
    hemispheres; the **anterior commissure** carries
    **bidirectional** fibers between the two anterior temporal
    lobes. The **commissures** is a **bidirectional** midline
    structure.

*   **NO Functional Lateralization of the Commissures per se:**
    The **functional lateralization** belongs to the **cortical
    grey-matter structures** whose fibers pass through the
    commissures (e.g., the **left-hemisphere language areas**,
    the **right-hemisphere spatial-attention areas**) — **not** to
    the commissures itself. Consumers must **not** assume the
    commissures carries a **functional lateralization** of its
    own.

*   **NO Extended-Amygdala Warning (SLEA-free container):** The
    commissures is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import
    the SLEA warning into the commissures.

*   **NO Amygdala-Lateralization Warning of their own (the
    commissures is a COMMISSURAL WHITE-MATTER COMPARTMENT, not
    the fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **commissures** is a
    **commissural white-matter compartment** — consumers must
    **not** conflate it with the **whole amygdala** or with the
    **central nucleus**.

**A consumer that assumes the commissures is a paired left/right
structure will be structurally INCORRECT** — the **commissures**
is a **single midline container**, not a paired structure. The
**corpus callosum** and the **anterior commissure** **cross the
midline** to connect the two hemispheres. The **commissures** is
a **strict midline container** with **NO left/right split**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **commissures** is a
    **midline container** — it is **not** a left or right
    structure, so the "no cross-hemisphere imports" rule is
    **satisfied by construction**: the container does not belong
    to either hemisphere.
*   **No cross-lobe imports.** This module does **not** import from
    the two commissural leaves (the children are imported by
    consumers, not by the container), and it does **not** import
    from ``.../telencephalon/cerebral_hemispheres/``,
    ``.../telencephalon/lateral_ventricles/``,
    ``.../left/white_matter/``, ``.../right/white_matter/``, or
    any other container. The **commissures**'s relationships to
    the cerebral hemispheres, the lateral ventricles, the
    ipsilateral white matter, the corpus callosum, the anterior
    commissure, and the telencephalon are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **CONTAINER module — children EXIST.** The **two structural
    children** — ``corpus_callosum`` and ``anterior_commissure``
    — are **wired modules**, not prose. Consumers **may** import
    them. The **commissures** is **not** a leaf.
*   **NOT a leaf — do not claim leaf status.** The **commissures**
    has **two structural children**; consumers must **not** assume
    it is a leaf and must **not** assume the two commissural
    structures are prose.
*   **MIDLINE CONTAINER — NOT a left/right paired container.**
    There is **only ONE** `commissures/` container (this one).
    Consumers must **not** look for `left/commissures/` or
    `right/commissures/` — those paths **do not exist**.
*   **COMMISSURAL WHITE MATTER — NOT the ipsilateral white
    matter.** The **commissures** is the **midline-crossing
    (commissural)** white matter; the **white_matter** under each
    hemisphere is the **ipsilateral** white matter. Consumers must
    **not** conflate the two.
*   **NOT the cerebral_hemispheres container — the
    cerebral_hemispheres is the GREY-MATTER + IPSILATERAL-WHITE-
    MATTER sibling.** Consumers must **not** conflate the
    commissures with the cerebral hemispheres.
*   **NOT the lateral_ventricles container — the
    lateral_ventricles is the CSF-space sibling.**
*   **NOT the corpus_callosum or the anterior_commissure — those
    are the CHILDREN.**
*   **NOT the telencephalon container — the commissures is a CHILD
    of the telencephalon.**
*   **NOT a grey-matter structure — the commissures is WHITE
    MATTER.**
*   **NOT a single uniform commissure — TWO structural children
    with DIFFERENT functions.** The **corpus callosum** is the
    **neocortical commissure**; the **anterior commissure** is
    the **anterior-temporal / olfactory commissure**.
*   **SLEA-FREE — no extended-amygdala relationship.** The
    commissures is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning) are **amygdala** children; the
    **commissures** is a **commissural white-matter
    compartment**.
*   **No ``AREA_PATHS`` hop.** The **commissures** is a local
    container under the telencephalon, not a cross-listed
    structure.
*   **No nested cross-listing.** The **commissures** has no
    nested dual-framing module. It is a single container.
*   **NO left/right mirror — MIDLINE container with NO
    warning.** The **commissures** is a **single midline
    container** — there is **no** `left/commissures/` and **no**
    `right/commissures/`. The **container itself** is
    **strictly hemisphere-neutral**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon import commissures

Or by fully-qualified path string::

    path = (
        "telencephalon.commissures"
    )

**Do not** assume the commissures is a **leaf**. It has **two
structural children** — ``corpus_callosum`` and
``anterior_commissure``.

**Do not** assume the commissures is a **left/right paired
container**. The commissures is a **single midline container** —
there is **no** `left/commissures/` and **no**
`right/commissures/`.

**Do not** assume the commissures is the **cerebral_hemispheres
container**. The **cerebral_hemispheres** is the **grey-matter +
ipsilateral-white-matter** sibling; the **commissures** is the
**commissural white matter**.

**Do not** assume the commissures is the **lateral_ventricles
container**. The **lateral_ventricles** is the **CSF-space**
sibling.

**Do not** assume the commissures is the **corpus callosum** or
the **anterior commissure**. Those are the **two children** of
the commissures container.

**Do not** assume the commissures is the **telencephalon
container**. The **telencephalon** container contains the
**cerebral_hemispheres**, the **commissures**, and the
**lateral_ventricles** — the **commissures** is **one** of those
three children.

**Do not** assume the commissures is the **ipsilateral white
matter** of the cerebral hemispheres. The **ipsilateral white
matter** is wired under ``.../left/white_matter/`` and
``.../right/white_matter/``; the **commissures** is the
**commissural (midline-crossing)** white matter.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the commissures. **The
commissures is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

Iterating the commissures's structural children (recommended
consumer pattern — NOTE these are WIRED, not prose)::

    COMMISSURES_CHILDREN = (
        "corpus_callosum",       # leaf
        "anterior_commissure",   # leaf
    )

Reaching the cerebral hemispheres (recommended consumer pattern —
the grey-matter + ipsilateral-white-matter sibling)::

    # The cerebral_hemispheres is the GREY-MATTER +
    # IPSILATERAL-WHITE-MATTER sibling under the telencephalon:
    #
    #   telencephalon.cerebral_hemispheres
    #
    # The cerebral_hemispheres is the grey-matter + ipsilateral-
    # white-matter compartment; the commissures is the commissural
    # white matter.

Reaching the lateral ventricles (recommended consumer pattern — the
CSF-space sibling)::

    # The lateral_ventricles is the CSF-SPACE sibling under the
    # telencephalon:
    #
    #   telencephalon.lateral_ventricles
    #
    # The lateral_ventricles is the CSF-space compartment; the
    # commissures is the commissural white matter.

Reaching the ipsilateral white matter (recommended consumer pattern —
the white matter of each cerebral hemisphere)::

    # The ipsilateral white matter is under each cerebral
    # hemisphere:
    #
    #   cerebral_hemispheres.left.white_matter
    #   cerebral_hemispheres.right.white_matter
    #
    # The ipsilateral white matter is the white-matter compartment
    # of each hemisphere; the commissures is the commissural
    # white matter that crosses the midline.

Reaching the corpus callosum (recommended consumer pattern — the
neocortical commissure child)::

    # The corpus callosum is the NEOCORTICAL COMMISSURE — a CHILD of
    # the commissures container:
    #
    #   telencephalon.commissures.corpus_callosum
    #
    # The corpus callosum is the largest commissure in the human
    # brain, connecting the neocortical areas of the two
    # hemispheres.

Reaching the anterior commissure (recommended consumer pattern — the
anterior-temporal / olfactory commissure child)::

    # The anterior commissure is the ANTERIOR-TEMPORAL / OLFACTORY
    # COMMISSURE — a CHILD of the commissures container:
    #
    #   telencephalon.commissures.anterior_commissure
    #
    # The anterior commissure connects the anterior temporal lobes
    # (anterior temporal commissure component) and the olfactory
    # structures (olfactory commissure component).

Reaching the telencephalon (recommended consumer pattern — the
container)::

    # The telencephalon is the CONTAINER that contains the
    # cerebral_hemispheres, the commissures, and the
    # lateral_ventricles:
    #
    #   telencephalon
    #
    # The commissures is ONE of the three children of the
    # telencephalon container.

Reaching the SLEA components (recommended consumer pattern — NOTE
the commissures is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # commissures:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The commissures is SLEA-FREE.

Bilateral iteration (recommended consumer pattern — NOTE the
commissures is a MIDLINE container, NOT a paired structure)::

    # The commissures is a SINGLE MIDLINE container — there is NO
    # left/right split. Do NOT iterate over ("left", "right") for
    # the commissures itself.
    #
    # The corpus callosum and the anterior commissure CROSS the
    # midline; their fibers are bidirectional between the two
    # hemispheres (or the two anterior temporal lobes).

References
----------
*   **Canonical corpus callosum anatomy:** Pandya, D.N., Seltzer,
    B. (1986). "The topography of commissural fibers." In:
    Lepore, F., Ptito, M., Jasper, H.H. (eds.), *Two Hemispheres
    — One Brain: Functions of the Corpus Callosum*. Alan R. Liss,
    New York, pp. 47–73. (Definitive corpus callosum topography
    — the neocortical commissural fibers.)
*   **Corpus callosum (review):** Paul, L.K., et al. (2007).
    "Agenesis of the corpus callosum: genetic, developmental and
    functional aspects of connectivity." *Nature Reviews
    Neuroscience* 8:287–299. (Review of the corpus callosum —
    anatomy, agenesis, and functional aspects.)
*   **Split-brain studies:** Sperry, R.W. (1968). "Hemisphere
    deconnection and unity in conscious awareness." *American
    Psychologist* 23:723–733. (The original split-brain studies —
    the callosotomy disconnection syndrome.)
*   **Split-brain (review):** Gazzaniga, M.S. (2005). "Forty-five
    years of split-brain research and still going strong."
    *Nature Reviews Neuroscience* 6:653–659. (Review of the
    split-brain studies — interhemispheric transfer.)
*   **Anterior commissure anatomy:** FitzGerald, M.J.T., Folan-
    Curran, J., O'Brien, E. (2001). "The anterior commissure in
    the human brain." *Journal of Anatomy* 199:669–676. (The
    anterior commissure — anterior temporal and olfactory
    components.)
*   **Anterior commissure (review):** Di Virgilio, G., Clarke, S.,
    Pizzolato, G., Schaffner, T. (1999). "Cortical connections of
    the anterior commissure in the human brain." *NeuroReport*
    10:2299–2303. (The anterior commissure — cortical
    connections.)
*   **Commissural anatomy (review):** Raybaud, C. (2010). "The
    corpus callosum: an MR imaging analysis of the anatomical
    variability and congenital anomalies." *American Journal of
    Neuroradiology* 31:1147–1155. (Commissural anatomy — corpus
    callosum and anterior commissure.)
*   **White-matter atlas (human):** Wakana, S., Jiang, H., Nagae,
    L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter atlas
    of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the commissures in DTI.)
*   **DTI tractography atlas:** Catani, M., Thiebaut de Schotten,
    M. (2008). "A diffusion tensor imaging tractography atlas for
    virtual in vivo dissections." *Cortex* 44:1105–1132. (The
    commissures in DTI tractography.)
*   **Commissures in the human connectome:** Catani, M., Thiebaut
    de Schotten, M. (2012). *Atlas of Human Brain Connections*.
    Oxford University Press, Oxford. (The commissures in the
    human connectome.)
*   **Fiber pathways (review):** Schmahmann, J.D., Pandya, D.N.
    (2006). *Fiber Pathways of the Brain*. Oxford University
    Press, New York. (Definitive white-matter anatomy; the
    commissures as the midline-crossing white matter.)
*   **Marchiafava-Bignami disease:** Hillbom, M., Saloheimo, P.,
    Fujioka, S., Patel, Z., Patel, N., Kannan, R., Choudhary, S.,
    Senthil, K., Qu, C., Kato, H. (2014). "Diagnosis and
    management of Marchiafava-Bignami disease: a review of
    literature." *Journal of the Neurological Sciences*
    345:1–11. (Marchiafava-Bignami disease — corpus callosum
    demyelination and necrosis.)
*   **Agenesis of the corpus callosum (review):** Paul, L.K.
    (2011). "Developmental malformation of the corpus callosum: a
    review of typical and atypical development." *Neuropsychology
    Review* 21:1–22. (Agenesis of the corpus callosum — the
    congenital absence of the neocortical commissure.)
*   **Multiple sclerosis and the corpus callosum:** Polman, C.H.,
    et al. (2011). "Diagnostic criteria for multiple sclerosis:
    2010 revisions to the McDonald criteria." *Annals of
    Neurology* 69:292–302. (MS plaques in the corpus callosum —
    the Dawson's fingers on sagittal MRI.)
*   **Alexander disease and the corpus callosum:** van der Knaap,
    M.S., Naidu, S., Breiter, S.N., Blaser, S., Stroink, H.,
    Powers, J.M. (2001). "Alexander disease: diagnosis with MR
    imaging." *American Journal of Neuroradiology* 22:541–552.
    (Alexander disease — corpus callosum predilection.)
*   **Schizophrenia and the corpus callosum (contested):** Walterfang,
    M., et al. (2009). "Corpus callosum size and shape in
    schizophrenia: a meta-analysis." *Schizophrenia Research*
    110:1–9. (Corpus callosum abnormalities in schizophrenia —
    contested.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    commissures is not the amnesia substrate):** Scoville, W.B.,
    Milner, B. (1957). "Loss of recent memory after bilateral
    hippocampal lesions." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 20:11–21. (Bilateral hippocampal damage and
    anterograde amnesia — distinct from the commissures.)
*   **Amygdala (contrast — the commissures is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the commissures.)
*   **SLEA (contrast — the commissures is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    commissures.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Commissures in overview.)
*   NeuroNames — Commissures (telencephalon); FMA — Commissures
    (telencephalon).
"""