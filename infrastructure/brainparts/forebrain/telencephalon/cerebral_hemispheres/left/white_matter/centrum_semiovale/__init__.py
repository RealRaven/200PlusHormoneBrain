"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter.centrum_semiovale
==========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── white_matter
                └── centrum_semiovale   <-- THIS MODULE

**Primary synonym:** Centrum semiovale (left); centrum ovale;
semioval center; **centrum semiovale of Vieussens**; **the
white-matter mass of the cerebral hemisphere above the level of the
lateral ventricles**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter region** — the **mass of white matter** in the
cerebral hemisphere **above the level of the lateral ventricles**,
composed of **projection fibers** (the corona radiata), **association
fibers** (the superior longitudinal fasciculus, the arcuate
fasciculus, the inferior longitudinal fasciculus, and others), and
**callosal fibers** (the callosal radiations of the corpus
callosum). It is a **region of passage**, **not** a single named
tract, **not** a nucleus, **not** a cortical area.
**Part of:** The **white_matter** container of the left
cerebral hemisphere — the **superficial white-matter mass** that
**carries** the projection, association, and callosal fibers
between the cortex, the deep grey matter, and the contralateral
hemisphere. The **centrum semiovale** is the **white-matter mass
above the lateral ventricles**.
**Structural parent:** ``.../left/white_matter/`` → **direct
child** of the white_matter container.
**Structural children:** **None.** This is a **leaf** module. The
**projection fibers (corona radiata)**, **association fibers
(superior longitudinal fasciculus, arcuate fasciculus, inferior
longitudinal fasciculus, uncinate fasciculus)**, and **callosal
fibers (callosal radiations)** that pass through the centrum
semiovale are documented as **prose**, not as structural children.
**Boundary status (WHITE MATTER — NOT a grey-matter structure):**
**Boundary case — the centrum_semiovale is WHITE MATTER, NOT a
grey-matter structure.** The **centrum semiovale** (here) is the
**mass of white matter** above the lateral ventricles —
**myelinated axons** (projection, association, and callosal
fibers). The **grey-matter structures** that the centrum semiovale
**carries fibers for** — the **cortex**, the **basal ganglia**,
and the **thalamus** — are **grey matter** and are wired under
their own containers (``.../left/cortex/``,
``.../left/subcortical/basal_ganglia/``, and
``.../left/subcortical/diencephalon/thalamus/``). **They are
DIFFERENT STRUCTURES** — the **centrum semiovale** is the
**white-matter mass**; the **cortex**, **basal ganglia**, and
**thalamus** are the **grey-matter structures** whose axons pass
through it. Consumers must **not** conflate the centrum semiovale
with any grey-matter structure.
**Boundary status (REGION OF PASSAGE — NOT a single named tract):**
**Boundary case — the centrum_semiovale is a REGION OF PASSAGE, NOT
a single named tract.** The **centrum semiovale** is the
**white-matter mass** that **contains** the **corona radiata**
(projection fibers), the **superior longitudinal fasciculus**, the
**arcuate fasciculus**, the **inferior longitudinal fasciculus**,
the **uncinate fasciculus**, and the **callosal radiations** of
the **corpus callosum** — but it is **not** any **one** of those
tracts. It is the **region** through which they pass. Consumers
must **not** treat the centrum semiovale as "the corona radiata" or
"the superior longitudinal fasciculus" — it is the **region** that
**contains** them as **prose**.
**Boundary status (NOT the corona radiata — the corona radiata is a
SIBLING white-matter leaf):** **Boundary case — the
centrum_semiovale is NOT the corona radiata; the corona radiata is
a SIBLING white-matter leaf.** The **corona radiata**
(``.../left/white_matter/corona_radiata/``) is the
**projection-fiber fan** that **radiates** from the internal
capsule up to the cortex, at and above the level of the lateral
ventricles. The **centrum semiovale** (here) is the
**white-matter mass** **above** the lateral ventricles that
**contains** the corona radiata fibers as they pass through. **The
two are sometimes used interchangeably in the radiology
literature** — the tree wires them as **separate leaves**.
Consumers must **not** conflate the centrum semiovale with the
corona radiata — the **corona radiata** is the **projection-fiber
fan**; the **centrum semiovale** is the **white-matter mass above
the lateral ventricles** that contains it.
**Boundary status (NOT the internal capsule — the internal capsule
is a SIBLING white-matter leaf):** **Boundary case — the
centrum_semiovale is NOT the internal capsule; the internal capsule
is a SIBLING white-matter leaf.** The **internal capsule**
(``.../left/white_matter/internal_capsule/``) is the **compact
projection-fiber bundle** that passes **between** the basal
ganglia, the thalamus, and the caudate nucleus — **deep** to the
centrum semiovale and **below** the level of the lateral
ventricles' body. The **centrum semiovale** (here) is the
**superficial** white-matter mass **above** the lateral ventricles
— **superficial** to the internal capsule. **They are DIFFERENT
STRUCTURES** — the **internal capsule** is the **deep, compact
projection-fiber bundle**; the **centrum semiovale** is the
**superficial white-matter mass** above the ventricles. Consumers
must **not** conflate the centrum semiovale with the internal
capsule.
**Boundary status (NOT the corpus callosum — the corpus callosum is
wired under ``commissures/``):** **Boundary case — the
centrum_semiovale is NOT the corpus callosum; the corpus callosum
is wired under ``.../left/commissures/corpus_callosum/``.** The
**corpus callosum** (``.../left/commissures/corpus_callosum/``) is
the **commissural structure** — the **midline white-matter
commissure** that connects the two hemispheres. The **centrum
semiovale** (here) **contains** the **callosal radiations** (the
**callosal fibers** that pass through it to reach the cortex), but
it is **not** the corpus callosum. **They are DIFFERENT
STRUCTURES** — the **corpus callosum** is the **commissural
structure** (wired under ``commissures/``); the **centrum
semiovale** is the **white-matter mass** above the ventricles that
**contains** the callosal radiations as they pass. Consumers must
**not** conflate the centrum semiovale with the corpus callosum.
**Boundary status (NOT the cingulum — the cingulum is a SIBLING
white-matter leaf):** **Boundary case — the centrum_semiovale is
NOT the cingulum; the cingulum is a SIBLING white-matter leaf.**
The **cingulum** (``.../left/white_matter/cingulum/``) is the
**specific association bundle** that runs in the **cingulate
gyrus** — **inferior** to the main mass of the centrum semiovale.
The **centrum semiovale** (here) is the **white-matter mass**
**above** the lateral ventricles — it **does not contain** the
cingulum. **They are DIFFERENT STRUCTURES** — the **cingulum** is
a **named association bundle**; the **centrum semiovale** is the
**white-matter mass** that **contains** other association fibers
(the superior longitudinal fasciculus, etc.) but **not** the
cingulum specifically. Consumers must **not** conflate the centrum
semiovale with the cingulum.
**Boundary status (NOT the external capsule, extreme capsule,
fasciculus rectus, fornix, mammillothalamic tract, or medial
forebrain bundle — those are SIBLING white-matter leaves):**
**Boundary case — the centrum_semiovale is NOT the external
capsule, extreme capsule, fasciculus rectus, fornix,
mammillothalamic tract, or medial forebrain bundle; those are
SIBLING white-matter leaves.** Each of those is a **specific
named white-matter structure** — the **external capsule** and
**extreme capsule** (capsule fibers lateral to the putamen and
claustrum), the **fasciculus rectus** (a small bundle), the
**fornix** (the major output tract of the hippocampus), the
**mammillothalamic tract** (the mammillary-body → anterior-thalamic
projection), and the **medial forebrain bundle** (a
brainstem-forebrain bundle). **None of them is part of the centrum
semiovale** — each is a **separate leaf** under ``white_matter/``.
Consumers must **not** conflate the centrum semiovale with any of
those siblings.
**Boundary status (NOT the cortex — the cortex is the GREY-MATTER
structure above):** **Boundary case — the centrum_semiovale is NOT
the cortex; the cortex is the GREY-MATTER structure above.** The
**cortex** (``.../left/cortex/``) is the **grey-matter sheet** that
**caps** the cerebral hemisphere — **superficial** to the centrum
semiovale. The **centrum semiovale** (here) is the
**white-matter mass** **immediately deep** to the cortex. **They
are DIFFERENT STRUCTURES** — the **cortex** is **grey matter**
(the neuronal cell bodies); the **centrum semiovale** is **white
matter** (the myelinated axons that project to and from the
cortex). Consumers must **not** conflate the centrum semiovale
with the cortex.
**Boundary status (NOT the basal ganglia — the basal ganglia are
the GREY-MATTER structures below):** **Boundary case — the
centrum_semiovale is NOT the basal ganglia; the basal ganglia are
the GREY-MATTER structures below.** The **basal ganglia**
(``.../left/subcortical/basal_ganglia/``) — the **caudate
nucleus**, the **putamen**, the **globus pallidus**, and the
**ventral striatum** — are **grey-matter** structures **deep** to
the centrum semiovale and **inferior** to it. The **centrum
semiovale** (here) is the **white-matter mass** **above** the
level of the basal ganglia. **They are DIFFERENT STRUCTURES** —
the **basal ganglia** are **grey matter**; the **centrum
semiovale** is **white matter**. Consumers must **not** conflate
the centrum semiovale with the basal ganglia.
**Boundary status (NOT the thalamus — the thalamus is a GREY-MATTER
structure below):** **Boundary case — the centrum_semiovale is NOT
the thalamus; the thalamus is a GREY-MATTER structure below.** The
**thalamus**
(``.../left/subcortical/diencephalon/thalamus/``) is a
**grey-matter** structure **deep** to the centrum semiovale and
**inferior** to it. The **centrum semiovale** (here) is the
**white-matter mass** **above** the level of the thalamus. **They
are DIFFERENT STRUCTURES** — the **thalamus** is **grey matter**;
the **centrum semiovale** is **white matter**. Consumers must
**not** conflate the centrum semiovale with the thalamus.
**Boundary status (NOT the lateral ventricles — the lateral
ventricles are the CSF spaces below):** **Boundary case — the
centrum_semiovale is NOT the lateral ventricles; the lateral
ventricles are the CSF spaces below.** The **lateral ventricles**
(``.../left/lateral_ventricles/``) are the **CSF-filled spaces**
**inferior** to the centrum semiovale — the **centrum semiovale**
is the **white-matter mass** **above** the lateral ventricles.
**They are DIFFERENT STRUCTURES** — the **lateral ventricles** are
**CSF spaces**; the **centrum semiovale** is **white matter**.
Consumers must **not** conflate the centrum semiovale with the
lateral ventricles.
**Boundary status (SLEA-FREE — the centrum semiovale is NOT an
extended-amygdala component):** **Boundary case — the
centrum_semiovale is SLEA-FREE.** The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **centrum semiovale** is a
**white-matter region** — it is **NOT** an extended-amygdala
component, and it carries **NO SLEA warning**. Consumers must
**not** import the SLEA warning into the centrum semiovale — it is
**SLEA-free**.
**Boundary status (NOT a grey-matter module — this is the FIRST
white-matter module in the series):** **Boundary case — the
centrum_semiovale is the FIRST WHITE-MATTER module in the
series.** Every previous module in the medial_temporal_lobe subtree
(amygdala, hippocampus, and their children) is a **grey-matter**
structure — a **nucleus**, a **cortical region**, or a **CA
field**. The **centrum semiovale** (here) is **white matter** —
the **first module in the series that is white matter, not grey
matter**. Consumers must **not** treat the centrum semiovale as
"another grey-matter structure" — it is **white matter**, and the
boundaries that anchored the grey-matter modules ("NOT the white
matter") are **reversed** here ("IS the white matter, NOT the
grey-matter structure").

Overview
--------
The centrum semiovale is the **white-matter mass of the cerebral
hemisphere above the level of the lateral ventricles** — a
**white-matter region** that **contains** the **projection
fibers** (the corona radiata), the **association fibers** (the
superior longitudinal fasciculus, the arcuate fasciculus, the
inferior longitudinal fasciculus, and others), and the **callosal
fibers** (the callosal radiations of the corpus callosum). It is
a **leaf** module under the white_matter container, the
**sibling of the cingulum, the corona radiata, the external
capsule, the extreme capsule, the fasciculus rectus, the fornix,
the internal capsule, the mammillothalamic tract, and the medial
forebrain bundle**, and the **white-matter substrate** of the
**long-range connectivity** of the cerebral hemisphere.

**The centrum semiovale is WHITE MATTER, NOT a grey-matter
structure.** It is the **mass of white matter** above the lateral
ventricles — **myelinated axons** (projection, association, and
callosal fibers). The **grey-matter structures** it **carries
fibers for** — the **cortex**, the **basal ganglia**, and the
**thalamus** — are **grey matter** and are wired under their own
containers.

**The centrum semiovale is a REGION OF PASSAGE, NOT a single named
tract.** It **contains** the **corona radiata**, the **superior
longitudinal fasciculus**, the **arcuate fasciculus**, the
**inferior longitudinal fasciculus**, the **uncinate fasciculus**,
and the **callosal radiations** of the **corpus callosum** — but
it is **not** any **one** of those tracts. It is the **region**
through which they pass.

**The centrum semiovale is NOT the corona radiata.** The **corona
radiata** (sibling) is the **projection-fiber fan** that radiates
from the internal capsule up to the cortex — at and above the
level of the lateral ventricles. The **centrum semiovale** is the
**white-matter mass above the lateral ventricles** that contains
the corona radiata fibers as they pass through. **They are
sometimes used interchangeably in the radiology literature; the
tree wires them as separate leaves.**

**The centrum semiovale is NOT the internal capsule.** The
**internal capsule** (sibling) is the **compact projection-fiber
bundle** that passes between the basal ganglia, the thalamus, and
the caudate nucleus — **deep** to the centrum semiovale and
**below** the level of the lateral ventricles' body. The
**centrum semiovale** is **superficial** to the internal capsule.

**The centrum semiovale is NOT the corpus callosum.** The
**corpus callosum** is wired under
``.../left/commissures/corpus_callosum/`` — the **commissural
structure** that connects the two hemispheres. The **centrum
semiovale** **contains** the **callosal radiations** (the callosal
fibers that pass through it to reach the cortex), but it is
**not** the corpus callosum.

**The centrum semiovale is NOT the cingulum.** The **cingulum**
(sibling) is the **specific association bundle** that runs in the
**cingulate gyrus** — **inferior** to the main mass of the
centrum semiovale. The **centrum semiovale** does **not contain**
the cingulum.

**The centrum semiovale is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.

**The centrum semiovale is a paired structure.** Each hemisphere
has its own centrum semiovale, with **ipsilateral** and
**bilateral** connections to the cortex, the basal ganglia, the
thalamus, and the contralateral hemisphere (via the corpus
callosum). The two sides are **bilaterally symmetric** — the
centrum semiovale is a **white-matter region**, and its **gross
anatomy** is **symmetric**; there is **no functional
lateralization** of the centrum semiovale per se. The
**functional lateralization** belongs to the **cortical and
subcortical grey-matter structures** whose fibers pass through it
(see *Lateralization Notes*).

Fiber Composition (prose, not structural children)
--------------------------------------------------
The centrum semiovale is a **region of passage** — documented as
**prose**, not as structural children:

*   **Projection fibers (corona radiata)** — the **corticospinal,
    corticobulbar, and corticopontine** descending fibers, and the
    **thalamocortical** ascending fibers, that **radiate** from
    the internal capsule up to the cortex. The corona radiata is
    **wired as a separate leaf** under ``white_matter/`` — the
    centrum semiovale **contains** the corona radiata fibers as
    they pass through it, but the **corona radiata** is a
    **sibling** leaf.

*   **Association fibers (superior longitudinal fasciculus,
    arcuate fasciculus, inferior longitudinal fasciculus,
    uncinate fasciculus)** — the **intrahemispheric** association
    bundles that connect **cortical areas** within the same
    hemisphere. The **superior longitudinal fasciculus** and the
    **arcuate fasciculus** run **through** the centrum semiovale;
    the **inferior longitudinal fasciculus** and the **uncinate
    fasciculus** run **more inferiorly** and **partly** through
    the centrum semiovale.

*   **Callosal fibers (callosal radiations)** — the **commissural
    fibers** that cross the **corpus callosum** and **radiate**
    through the centrum semiovale to reach the **cortex**. The
    **corpus callosum** itself is wired under
    ``.../left/commissures/corpus_callosum/`` — the centrum
    semiovale **contains** the callosal radiations, but the
    **corpus callosum** is a **separate commissural structure**.

**These fiber groups are prose, not structural children.** The
tree wires the **centrum semiovale** as a **single leaf** under
``white_matter/`` — the **corona radiata** is a **sibling leaf**,
the **association fibers** are **prose**, and the **corpus
callosum** is wired under ``commissures/``. Consumers that need
**tract-level** resolution should consult the references, not the
tree.

The Centrum Semiovale / Corona Radiata Boundary
-----------------------------------------------
This is the **most consequential sibling boundary** — the
**white-matter-mass vs. projection-fiber-fan** boundary:

*   **Centrum_semiovale** (this module) — the **white-matter mass
    above the lateral ventricles** that **contains** the corona
    radiata (and the association and callosal fibers) as they
    pass through.

*   **Corona_radiata** (``.../left/white_matter/corona_radiata/``)
    — the **projection-fiber fan** that **radiates** from the
    internal capsule up to the cortex, at and above the level of
    the lateral ventricles.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **centrum semiovale** is the
**region** (the white-matter mass); the **corona radiata** is the
**projection-fiber fan** that passes through it (and through the
level of the ventricles). **The two are sometimes used
interchangeably in the radiology literature** — the tree wires
them as **separate leaves**. Consumers must **not** conflate the
centrum semiovale with the corona radiata.

The Centrum Semiovale / Internal Capsule Boundary
-------------------------------------------------
This is the **superficial white-matter mass vs. deep compact
bundle** boundary:

*   **Centrum_semiovale** (this module) — the **superficial**
    white-matter mass **above** the lateral ventricles.

*   **Internal_capsule**
    (``.../left/white_matter/internal_capsule/``) — the
    **compact** projection-fiber bundle that passes **between**
    the basal ganglia, the thalamus, and the caudate nucleus —
    **deep** to the centrum semiovale.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **internal capsule** is the **deep,
compact projection-fiber bundle**; the **centrum semiovale** is
the **superficial white-matter mass** above the ventricles.
Consumers must **not** conflate the centrum semiovale with the
internal capsule.

The Centrum Semiovale / Corpus Callosum Boundary
------------------------------------------------
This is the **white-matter mass vs. commissural structure**
boundary:

*   **Centrum_semiovale** (this module) — the **white-matter
    mass** above the lateral ventricles that **contains** the
    **callosal radiations**.

*   **Corpus_callosum**
    (``.../left/commissures/corpus_callosum/``) — the
    **commissural structure** that connects the two hemispheres
    — wired under ``commissures/``, **not** under
    ``white_matter/``.

**They are DIFFERENT STRUCTURES** — the **corpus callosum** is the
**commissural structure** (wired under ``commissures/``); the
**centrum semiovale** is the **white-matter mass** above the
ventricles that **contains** the callosal radiations as they pass.
Consumers must **not** conflate the centrum semiovale with the
corpus callosum.

The Centrum Semiovale / Cingulum Boundary
-----------------------------------------
This is the **white-matter mass vs. named association bundle**
boundary:

*   **Centrum_semiovale** (this module) — the **white-matter
    mass** above the lateral ventricles.

*   **Cingulum** (``.../left/white_matter/cingulum/``) — the
    **specific association bundle** that runs in the
    **cingulate gyrus**, **inferior** to the main mass of the
    centrum semiovale.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — the **cingulum** is a **named
association bundle**; the **centrum semiovale** is the
**white-matter mass** that **contains other association fibers**
(the superior longitudinal fasciculus, etc.) but **not** the
cingulum specifically. Consumers must **not** conflate the centrum
semiovale with the cingulum.

The Centrum Semiovale / Other White-Matter Leaves Boundary
---------------------------------------------------------
This is the **white-matter-mass vs. other named white-matter
structures** boundary:

*   **Centrum_semiovale** (this module) — the **white-matter mass**
    above the lateral ventricles.

*   **External capsule**, **extreme capsule**, **fasciculus
    rectus**, **fornix**, **mammillothalamic tract**, **medial
    forebrain bundle** — the **other named white-matter leaves**
    under ``white_matter/``.

**They are SIBLINGS under the white_matter container, and they are
DIFFERENT STRUCTURES** — each of those is a **specific named
white-matter structure**; the **centrum semiovale** is the
**white-matter mass** above the ventricles. **None of those is part
of the centrum semiovale.** Consumers must **not** conflate the
centrum semiovale with any of those siblings.

The Centrum Semiovale / Cortex Boundary
---------------------------------------
This is the **white matter vs. grey matter** boundary:

*   **Centrum_semiovale** (this module) — the **white-matter mass**
    **immediately deep** to the cortex.

*   **Cortex** (``.../left/cortex/``) — the **grey-matter sheet**
    that **caps** the cerebral hemisphere.

**They are DIFFERENT STRUCTURES** — the **cortex** is **grey
matter** (the neuronal cell bodies); the **centrum semiovale** is
**white matter** (the myelinated axons that project to and from
the cortex). Consumers must **not** conflate the centrum semiovale
with the cortex.

The Centrum Semiovale / Basal Ganglia Boundary
----------------------------------------------
This is the **white matter vs. grey matter** boundary:

*   **Centrum_semiovale** (this module) — the **white-matter mass**
    **above** the level of the basal ganglia.

*   **Basal ganglia** (``.../left/subcortical/basal_ganglia/``) —
    the **grey-matter structures** **deep** and **inferior** to
    the centrum semiovale.

**They are DIFFERENT STRUCTURES** — the **basal ganglia** are
**grey matter**; the **centrum semiovale** is **white matter**.
Consumers must **not** conflate the centrum semiovale with the
basal ganglia.

The Centrum Semiovale / Thalamus Boundary
-----------------------------------------
This is the **white matter vs. grey matter** boundary:

*   **Centrum_semiovale** (this module) — the **white-matter mass**
    **above** the level of the thalamus.

*   **Thalamus** (``.../left/subcortical/diencephalon/thalamus/``)
    — the **grey-matter structure** **deep** and **inferior** to
    the centrum semiovale.

**They are DIFFERENT STRUCTURES** — the **thalamus** is **grey
matter**; the **centrum semiovale** is **white matter**. Consumers
must **not** conflate the centrum semiovale with the thalamus.

The Centrum Semiovale / Lateral Ventricles Boundary
---------------------------------------------------
This is the **white matter vs. CSF space** boundary:

*   **Centrum_semiovale** (this module) — the **white-matter mass**
    **above** the lateral ventricles.

*   **Lateral ventricles** (``.../left/lateral_ventricles/``) — the
    **CSF-filled spaces** **inferior** to the centrum semiovale.

**They are DIFFERENT STRUCTURES** — the **lateral ventricles** are
**CSF spaces**; the **centrum semiovale** is **white matter**.
Consumers must **not** conflate the centrum semiovale with the
lateral ventricles.

The Centrum Semiovale / White Matter Container Boundary
-------------------------------------------------------
This is the **child vs. container** boundary:

*   **Centrum_semiovale** (this module) — a **child** of the
    white_matter container.

*   **White_matter** (``.../left/white_matter/``) — the
    **container** that contains the **centrum semiovale**, the
    **cingulum**, the **corona radiata**, the **external
    capsule**, the **extreme capsule**, the **fasciculus rectus**,
    the **fornix**, the **internal capsule**, the
    **mammillothalamic tract**, and the **medial forebrain
    bundle**.

**The centrum semiovale is ONE of the ten children of the
white_matter container.** Consumers must **not** conflate the
centrum semiovale with the white_matter container.

The Centrum Semiovale / Cerebral Hemisphere Boundary
---------------------------------------------------
This is the **grandchild vs. container** boundary:

*   **Centrum_semiovale** (this module) — a **grandchild** of the
    ``.../left/`` (cerebral hemisphere) container.

*   **``.../left/``** — the **cerebral hemisphere container** that
    contains the **cortex**, the **rhinencephalon**, the
    **subcortical** structures, the **white_matter**, the
    **commissures**, and the **lateral_ventricles**.

**The centrum semiovale is a grandchild of the cerebral hemisphere**
(child of the white_matter container). Consumers must **not**
conflate the centrum semiovale with the cerebral hemisphere
container.

The Centrum Semiovale / SLEA Boundary
------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Centrum_semiovale** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The centrum semiovale is NOT part of the SLEA continuum.** It is
a **white-matter region**, and it carries **no SLEA warning**.
Consumers must **not** import the SLEA warning into the centrum
semiovale.

Function in the Human Brain
---------------------------
The centrum semiovale's functions are **long-range white-matter
connectivity** — **projection**, **association**, and
**commissural** conduction — **NOT a grey-matter function**:

*   **Projection-Fiber Conduction (Corona Radiata):** The
    **centrum semiovale** carries the **projection fibers** (the
    **corona radiata**) — the **corticospinal**,
    **corticobulbar**, and **corticopontine** descending fibers,
    and the **thalamocortical** ascending fibers — between the
    **internal capsule** and the **cortex**. This is the
    **projection** substrate of the centrum semiovale.

*   **Association-Fiber Conduction (Superior Longitudinal
    Fasciculus, Arcuate Fasciculus, Inferior Longitudinal
    Fasciculus, Uncinate Fasciculus):** The **centrum semiovale**
    carries the **association fibers** — the **intrahemispheric**
    bundles that connect **cortical areas** within the same
    hemisphere. This is the **association** substrate of the
    centrum semiovale.

*   **Callosal-Fiber Conduction (Callosal Radiations):** The
    **centrum semiovale** carries the **callosal fibers** — the
    **commissural** fibers that cross the **corpus callosum** and
    **radiate** through the centrum semiovale to reach the
    **cortex**. This is the **commissural** substrate of the
    centrum semiovale.

*   **NOT a neural processor in the classical sense.** The
    **centrum semiovale** is a **white-matter region** — it
    **conducts** the **projection**, **association**, and
    **commissural** fibers, but it does **not** **process**
    information (that happens in the **grey-matter structures** —
    the cortex, the basal ganglia, and the thalamus whose axons
    pass through it). The **fear-output** is the **central
    nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**.

**The unifying theme:** the centrum semiovale is the
**white-matter mass** of the **cerebral hemisphere** — the
**region of passage** that anchors the **projection**,
**association**, and **commissural** connectivity of the
hemisphere. It is **SLEA-free**, **white-matter**, and **NOT a
grey-matter structure** — the **grey-matter structures** are the
**cortex**, the **basal ganglia**, and the **thalamus** whose
axons pass through it.

Associated Disorders
--------------------
The centrum semiovale has **no named "centrum semiovale
syndrome"** in the narrow sense, but its clinical associations are
**well-documented** — primarily as a **white-matter imaging
target**:

*   **White-Matter Hyperintensities (Leukoaraiosis / Small-Vessel
    Disease):** The **centrum semiovale** is a **principal site**
    of **white-matter hyperintensities** — the **T2/FLAIR
    hyperintensities** that are the **radiological hallmark** of
    **small-vessel disease**, **aging**, and **vascular
    dementia**. The **Fazekas scale** grades these
    **centrum-semiovale** (and **periventricular**)
    hyperintensities. The **centrum semiovale** is the
    **white-matter substrate** of **leukoaraiosis**.

*   **Multiple Sclerosis (White-Matter Plaques):** The **centrum
    semiovale** is a **principal site** of **MS plaques** — the
    **demyelinating lesions** that are the **radiological
    hallmark** of **multiple sclerosis**. The **centrum
    semiovale** is the **white-matter substrate** of **MS
    lesions**.

*   **Cerebral Amyloid Angiopathy (Centrum Semiovale Perivascular
    Spaces):** The **centrum semiovale** is a **principal site**
    of **enlarged perivascular spaces** — the **cribriform
    appearance** on MRI that is a **radiological marker** of
    **cerebral amyloid angiopathy** (CAA) and of **small-vessel
    disease**. The **centrum semiovale** is the **white-matter
    substrate** of **centrum-semiovale perivascular spaces**.

*   **Glioblastoma and White-Matter Tumors:** The **centrum
    semiovale** is a **common site** of **glioblastoma** and
    other **white-matter tumors** — the **infiltrative** tumor
    cells **spread** along the white-matter tracts of the centrum
    semiovale. The **centrum semiovale** is the **white-matter
    substrate** of **tumor infiltration**.

*   **No Named "Centrum Semiovale Syndrome":** The **centrum
    semiovale** is a **white-matter region**, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **direct** as a **white-matter
    imaging target** (leukoaraiosis, MS plaques, perivascular
    spaces, tumor infiltration).

**What is NOT here:** The **centrum semiovale** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as a **white-matter imaging target**.

Lateralization Notes
--------------------
This is the **left** centrum_semiovale module. The **centrum
semiovale** is **bilaterally symmetric** — and it carries **NO
warning**:

*   **Bilateral White-Matter Anatomy:** Each hemisphere has its own
    centrum semiovale. The two sides are **grossly symmetric** —
    the centrum semiovale is a **white-matter region**, and its
    **gross anatomy** is **symmetric**. There is **no functional
    lateralization** of the centrum semiovale per se.

*   **NO Functional Lateralization of the White-Matter Region:**
    The **functional lateralization** belongs to the **cortical
    and subcortical grey-matter structures** whose fibers pass
    through the centrum semiovale (e.g., the **left-hemisphere
    language areas**, the **right-hemisphere spatial-attention
    areas**) — **not** to the centrum semiovale itself. Consumers
    must **not** assume the centrum semiovale carries a
    **functional lateralization** of its own.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    centrum_semiovale is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the centrum semiovale.

*   **NO Amygdala-Lateralization Warning of their own (the centrum
    semiovale is a WHITE-MATTER REGION, not the fear-output):**
    The **right-amygdala fear association** belongs to the
    **amygdala module** — specifically the **central nucleus**
    (fear-output) and the **basolateral nuclei** (fear-learning).
    The **centrum semiovale** is a **white-matter region** —
    consumers must **not** conflate it with the **whole amygdala**
    or with the **central nucleus**.

**A consumer that assumes "left centrum semiovale = right centrum
semiovale" will be structurally correct** — the two sides are
**symmetric** (the centrum semiovale is a **white-matter region**,
and its **gross anatomy** is **symmetric**). The **centrum
semiovale** is a **strict-mirror pair with NO warning** — **no
SLEA warning**, **no amygdala-lateralization warning of their
own**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../left/white_matter/cingulum/``,
    ``.../left/white_matter/corona_radiata/``,
    ``.../left/white_matter/external_capsule/``,
    ``.../left/white_matter/extreme_capsule/``,
    ``.../left/white_matter/fasciculus_rectus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/white_matter/internal_capsule/``,
    ``.../left/white_matter/mammillothalamic_tract/``,
    ``.../left/white_matter/medial_forebrain_bundle/``,
    ``.../left/cortex/``, ``.../left/commissures/``,
    ``.../left/subcortical/basal_ganglia/``,
    ``.../left/subcortical/diencephalon/thalamus/``,
    ``.../left/lateral_ventricles/``, or any other container. The
    **centrum semiovale**'s relationships to the other white-matter
    leaves, the cortex, the corpus callosum, the basal ganglia, the
    thalamus, and the lateral ventricles are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **projection
    fibers (corona radiata)**, the **association fibers (superior
    longitudinal fasciculus, arcuate fasciculus, inferior
    longitudinal fasciculus, uncinate fasciculus)**, and the
    **callosal fibers (callosal radiations)** are documented as
    **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve tract-level detail through the
    references.
*   **WHITE MATTER — NOT a grey-matter structure.** The **centrum
    semiovale** is **white matter**; the **cortex**, the **basal
    ganglia**, and the **thalamus** are **grey matter**. Consumers
    must **not** conflate the centrum semiovale with any
    grey-matter structure.
*   **REGION OF PASSAGE — NOT a single named tract.** The **centrum
    semiovale** is the **white-matter mass** that **contains** the
    corona radiata, the association fibers, and the callosal
    radiations — but it is **not** any **one** of those tracts.
*   **NOT the corona radiata — the corona radiata is a SIBLING
    white-matter leaf.** The two are **sometimes used
    interchangeably in the radiology literature**; the tree wires
    them as **separate leaves**.
*   **NOT the internal capsule — the internal capsule is a SIBLING
    white-matter leaf.** The internal capsule is the **deep,
    compact projection-fiber bundle**; the centrum semiovale is
    the **superficial white-matter mass** above the ventricles.
*   **NOT the corpus callosum — the corpus callosum is wired under
    ``commissures/``.** The centrum semiovale **contains** the
    callosal radiations, but it is **not** the corpus callosum.
*   **NOT the cingulum — the cingulum is a SIBLING white-matter
    leaf.** The centrum semiovale does **not contain** the
    cingulum.
*   **NOT the external capsule, extreme capsule, fasciculus rectus,
    fornix, mammillothalamic tract, or medial forebrain bundle —
    those are SIBLING white-matter leaves.** None of them is part
    of the centrum semiovale.
*   **NOT the cortex, basal ganglia, or thalamus — those are
    GREY-MATTER structures.** The centrum semiovale is the
    **white-matter mass** that **carries their fibers**.
*   **NOT the lateral ventricles — the lateral ventricles are CSF
    spaces.** The centrum semiovale is the **white-matter mass**
    above the ventricles.
*   **NOT the white_matter container — the centrum semiovale is a
    CHILD of the white_matter container.**
*   **NOT the cerebral hemisphere container — the centrum
    semiovale is a GRANDCHILD of the ``.../left/`` container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    centrum_semiovale is **not** an extended-amygdala component,
    and it carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; the **centrum
    semiovale** is a **white-matter region**.
*   **NOT a single uniform structure — a REGION OF PASSAGE.** The
    **corona radiata**, the **association fibers**, and the
    **callosal radiations** are **prose**, not structural children.
*   **No ``AREA_PATHS`` hop.** The **centrum semiovale** is a local
    leaf under ``white_matter/``, not a cross-listed leaf.
*   **No nested cross-listing.** The **centrum semiovale** has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with right centrum semiovale — strict
    mirror with NO warning.** Left and right centrum semiovale
    modules are **structurally identical** — same **leaf** status,
    same **white-matter-region** framing, same **SLEA-free**
    status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.white_matter import centrum_semiovale

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.white_matter."
        "centrum_semiovale"
    )

**Do not** assume the centrum semiovale is the **corona radiata**.
The **corona radiata** is a **sibling** white-matter leaf — the
**projection-fiber fan**. The **centrum semiovale** is the
**white-matter mass** above the ventricles that **contains** the
corona radiata fibers as they pass through.

**Do not** assume the centrum semiovale is the **internal capsule**.
The **internal capsule** is a **sibling** white-matter leaf — the
**deep, compact projection-fiber bundle**. The **centrum
semiovale** is the **superficial white-matter mass** above the
ventricles.

**Do not** assume the centrum semiovale is the **corpus callosum**.
The **corpus callosum** is wired under ``commissures/`` — the
**commissural structure**. The **centrum semiovale** **contains**
the **callosal radiations** (the callosal fibers that pass through
it to reach the cortex), but it is **not** the corpus callosum.

**Do not** assume the centrum semiovale is the **cingulum**. The
**cingulum** is a **sibling** white-matter leaf — the
**specific association bundle** in the **cingulate gyrus**. The
**centrum semiovale** does **not contain** the cingulum.

**Do not** assume the centrum semiovale is **any** of the other
white-matter siblings — the **external capsule**, the **extreme
capsule**, the **fasciculus rectus**, the **fornix**, the
**mammillothalamic tract**, or the **medial forebrain bundle**.
Those are **separate leaves** under ``white_matter/``.

**Do not** assume the centrum semiovale is the **cortex**, the
**basal ganglia**, or the **thalamus**. Those are **grey-matter
structures** — the centrum semiovale is the **white-matter mass**
that **carries their fibers**.

**Do not** assume the centrum semiovale is the **lateral
ventricles**. The **lateral ventricles** are **CSF spaces** — the
centrum semiovale is the **white-matter mass** above the
ventricles.

**Do not** assume the centrum semiovale is the **white_matter
container**. The **white_matter** container contains the
**centrum semiovale** and the other nine white-matter leaves — the
**centrum semiovale** is **one** of those ten children.

**Do not** assume the centrum semiovale is the **cerebral
hemisphere container**. The **centrum semiovale** is a
**grandchild** of the ``.../left/`` container (child of the
white_matter container).

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the centrum semiovale.
**The centrum semiovale is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the centrum semiovale's (empty) children (recommended
consumer pattern)::

    CENTRUM_SEMIOVALE_CHILDREN = ()
    # The centrum semiovale is a leaf. The projection fibers (corona
    # radiata), the association fibers (superior longitudinal
    # fasciculus, arcuate fasciculus, inferior longitudinal
    # fasciculus, uncinate fasciculus), and the callosal fibers
    # (callosal radiations) are prose, not modules.

Reaching the corona radiata sibling (recommended consumer pattern —
the projection-fiber fan)::

    # The corona radiata is the PROJECTION-FIBER FAN — the SIBLING
    # of the centrum semiovale under the white_matter container:
    #
    #   white_matter.corona_radiata
    #
    # The corona radiata is the projection-fiber fan; the centrum
    # semiovale is the white-matter mass above the lateral
    # ventricles that contains it (and the association and callosal
    # fibers) as they pass through.

Reaching the internal capsule sibling (recommended consumer pattern
— the deep compact projection-fiber bundle)::

    # The internal capsule is the DEEP, COMPACT PROJECTION-FIBER
    # BUNDLE — the SIBLING of the centrum semiovale under the
    # white_matter container:
    #
    #   white_matter.internal_capsule
    #
    # The internal capsule is the deep, compact projection-fiber
    # bundle; the centrum semiovale is the superficial white-matter
    # mass above the lateral ventricles.

Reaching the cingulum sibling (recommended consumer pattern — the
cingulate-gyrus association bundle)::

    # The cingulum is the CINGULATE-GYRUS ASSOCIATION BUNDLE — the
    # SIBLING of the centrum semiovale under the white_matter
    # container:
    #
    #   white_matter.cingulum
    #
    # The cingulum is a specific named association bundle; the
    # centrum semiovale is the white-matter mass above the lateral
    # ventricles that does not contain the cingulum specifically.

Reaching the other white-matter siblings (recommended consumer
pattern — the other white-matter leaves)::

    # The external capsule, extreme capsule, fasciculus rectus,
    # fornix, mammillothalamic tract, and medial forebrain bundle
    # are the other SIBLING white-matter leaves under the
    # white_matter container:
    #
    #   white_matter.external_capsule
    #   white_matter.extreme_capsule
    #   white_matter.fasciculus_rectus
    #   white_matter.fornix
    #   white_matter.mammillothalamic_tract
    #   white_matter.medial_forebrain_bundle
    #
    # Each is a specific named white-matter structure; the centrum
    # semiovale is the white-matter mass above the lateral
    # ventricles. None of them is part of the centrum semiovale.

Reaching the corpus callosum (recommended consumer pattern — the
commissural structure, NOT under white_matter/)::

    # The corpus callosum is the COMMISSURAL STRUCTURE — wired
    # under ``commissures/``, NOT under ``white_matter/``:
    #
    #   left.commissures.corpus_callosum
    #
    # The centrum semiovale contains the CALLOSAL RADIATIONS (the
    # callosal fibers that pass through it to reach the cortex),
    # but the corpus callosum itself is a separate commissural
    # structure.

Reaching the cortex (recommended consumer pattern — the grey-matter
sheet above)::

    # The cortex is the GREY-MATTER SHEET that caps the hemisphere —
    # the structure the centrum semiovale carries fibers to and
    # from:
    #
    #   left.cortex
    #
    # The cortex is grey matter; the centrum semiovale is white
    # matter — the myelinated axons that project to and from the
    # cortex.

Reaching the basal ganglia (recommended consumer pattern — the
grey-matter structures below)::

    # The basal ganglia (caudate, putamen, globus pallidus, ventral
    # striatum) are the GREY-MATTER structures deep and inferior to
    # the centrum semiovale:
    #
    #   left.subcortical.basal_ganglia
    #
    # The basal ganglia are grey matter; the centrum semiovale is
    # white matter — the myelinated axons that pass above the level
    # of the basal ganglia.

Reaching the thalamus (recommended consumer pattern — the
grey-matter structure below)::

    # The thalamus is the GREY-MATTER structure deep and inferior
    # to the centrum semiovale:
    #
    #   left.subcortical.diencephalon.thalamus
    #
    # The thalamus is grey matter; the centrum semiovale is white
    # matter — the myelinated axons that pass above the level of
    # the thalamus.

Reaching the white_matter container (recommended consumer pattern —
the container)::

    # The white_matter container contains the centrum semiovale and
    # the other nine white-matter leaves:
    #
    #   left.white_matter
    #
    # The centrum semiovale is ONE of the ten children of the
    # white_matter container.

Reaching the SLEA components (recommended consumer pattern — NOTE
the centrum semiovale is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the centrum
    # semiovale:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The centrum_semiovale is SLEA-FREE.

Fiber-level detail (not wired — consult references)::

    # The centrum semiovale's fiber groups are prose, not modules:
    #   projection fibers (corona radiata)  -> corticospinal,
    #                                          corticobulbar,
    #                                          corticopontine,
    #                                          thalamocortical
    #   association fibers                  -> superior longitudinal
    #                                          fasciculus, arcuate
    #                                          fasciculus, inferior
    #                                          longitudinal fasciculus,
    #                                          uncinate fasciculus
    #   callosal fibers (callosal
    #     radiations)                       -> corpus callosum
    #                                          radiations to the
    #                                          cortex
    #
    # Do not attempt to resolve these as sub-paths of the centrum
    # semiovale.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cs_path = (
            f"telencephalon.cerebral_hemispheres.{side}.white_matter."
            f"centrum_semiovale"
        )
        # resolve cs_path through the memory/recall layer

References
----------
*   **Canonical white-matter anatomy:** Wakana, S., Jiang, H.,
    Nagae, L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter
    atlas of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the centrum semiovale as a region of passage.)
*   **Centrum semiovale anatomy (review):** Schmahmann, J.D.,
    Pandya, D.N. (2006). *Fiber Pathways of the Brain*. Oxford
    University Press, New York. (Definitive white-matter anatomy;
    the centrum semiovale and the corona radiata; association and
    callosal fibers.)
*   **Centrum semiovale / corona radiata distinction (radiology):**
    Mori, S., Wakana, S., van Zijl, P.C.M. (2005). *MRI Atlas of
    Human White Matter*. Elsevier, Amsterdam. (The centrum
    semiovale vs. the corona radiata in the radiology
    literature — sometimes used interchangeably, sometimes
    distinguished.)
*   **White-matter hyperintensities (leukoaraiosis):** Fazekas, F.,
    Chawluk, J.B., Alavi, A., Hurtig, H.I., Zimmerman, R.A.
    (1987). "MR signal abnormalities at 1.5 T in Alzheimer's
    dementia and normal aging." *American Journal of
    Roentgenology* 149:351–356. (The Fazekas scale for
    centrum-semiovale and periventricular hyperintensities —
    the radiological hallmark of small-vessel disease.)
*   **Leukoaraiosis (review):** Pantoni, L., Garcia, J.H. (1997).
    "Pathogenesis of leukoaraiosis: a review." *Stroke*
    28:652–659. (Leukoaraiosis in the centrum semiovale and
    periventricular white matter — small-vessel disease.)
*   **Multiple sclerosis and white-matter plaques:** Polman, C.H.,
    et al. (2011). "Diagnostic criteria for multiple sclerosis:
    2010 revisions to the McDonald criteria." *Annals of
    Neurology* 69:292–302. (MS plaques in the centrum semiovale —
    the radiological hallmark of MS.)
*   **Centrum semiovale perivascular spaces and cerebral amyloid
    angiopathy:** Charidimou, A., et al. (2017). "White matter
    perivascular spaces in cerebral amyloid angiopathy and
    hypertensive arteriopathy." *Neurology* 88:1157–1164.
    (Centrum-semiovale perivascular spaces — the cribriform
    appearance as a marker of CAA.)
*   **Glioblastoma and white-matter tumor infiltration:** Louis,
    D.N., et al. (2016). "The 2016 World Health Organization
    classification of tumors of the central nervous system: a
    summary." *Acta Neuropathologica* 131:803–820. (Glioblastoma
    and white-matter tumor infiltration — the centrum semiovale
    as a common site of infiltration.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    centrum semiovale is not the amnesia substrate):** Scoville,
    W.B., Milner, B. (1957). "Loss of recent memory after
    bilateral hippocampal lesions." *Journal of Neurology,
    Neurosurgery, and Psychiatry* 20:11–21. (Bilateral
    hippocampal damage and anterograde amnesia — distinct from
    the centrum semiovale.)
*   **Amygdala (contrast — the centrum semiovale is NOT the
    amygdala):** LeDoux, J.E. (2000). "Emotion circuits in the
    brain." *Annual Review of Neuroscience* 23:155–184.
    (Amygdala fear circuit — distinct from the centrum
    semiovale.)
*   **SLEA (contrast — the centrum semiovale is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the centrum semiovale.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Centrum semiovale in overview.)
*   NeuroNames — Centrum semiovale (left); FMA — Centrum
    semiovale (left member).
"""