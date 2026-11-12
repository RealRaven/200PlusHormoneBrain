"""
infrastructure.brainparts.forebrain.telencephalon.commissures.anterior_commissure
=================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    ├── cerebral_hemispheres
    ├── commissures
    │   ├── anterior_commissure   <-- THIS MODULE
    │   └── corpus_callosum
    └── lateral_ventricles

**Primary synonym:** Anterior commissure (of the telencephalon);
AC; commissura anterior; **the anterior-temporal / olfactory
commissure**; **the second-largest telencephalic commissure**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **midline commissural bundle** that
**crosses the midline** in the **anterior wall of the third
ventricle** (just **anterior** to the **columns of the fornix**)
and **connects** the **anterior temporal lobes** of the two
hemispheres (the **anterior temporal commissure** component) and
the **olfactory structures** (the **olfactory commissure**
component). It is a **specific named white-matter tract** — a
**commissural white-matter leaf**, **not** a region of passage,
**not** a projection-fiber fan, **not** a capsular white-matter
sheet, **not** an association bundle, **not** a compact
projection-fiber bundle, **not** a hippocampal output tract,
**not** a diencephalic projection, **not** a brainstem-forebrain
bundle.
**Part of:** The **commissures** container of the telencephalon —
the **anterior-temporal / olfactory commissure**. The **anterior
commissure** is the **second-largest** telencephalic commissure
(after the **corpus callosum**), and it is the **principal
commissure** of the **anterior temporal lobes** and the
**olfactory structures**.
**Structural parent:** ``.../commissures/`` → **direct child** of
the commissures container.
**Structural children:** **None.** This is a **leaf** module. The
**anterior temporal commissure** component and the **olfactory
commissure** component of the anterior commissure are documented
as **prose**, not as structural children.
**Boundary status (WHITE MATTER — NOT a grey-matter structure):**
**Boundary case — the anterior_commissure is WHITE MATTER, NOT a
grey-matter structure.** The **anterior commissure** (here) is
the **commissural white-matter bundle** — **myelinated axons**
(commissural projection fibers). The **grey-matter structures**
that the anterior commissure **connects** — the **anterior
temporal lobes** and the **olfactory structures** of the two
hemispheres — are **grey matter** and are wired under
``.../cerebral_hemispheres/left/cortex/temporal/``,
``.../cerebral_hemispheres/right/cortex/temporal/``,
``.../cerebral_hemispheres/left/cortex/rhinencephalon/``, and
``.../cerebral_hemispheres/right/cortex/rhinencephalon/``. **They
are DIFFERENT STRUCTURES** — the **anterior commissure** is the
**commissural white-matter bundle**; the **anterior temporal
lobes** and the **olfactory structures** are the **grey-matter
structures** it **connects**. Consumers must **not** conflate the
anterior commissure with any grey-matter structure.
**Boundary status (COMMISSURAL WHITE MATTER — NOT the ipsilateral
white matter of either hemisphere):** **Boundary case — the
anterior_commissure is COMMISSURAL WHITE MATTER, NOT the
ipsilateral white matter of either hemisphere.** The **anterior
commissure** (here) is a **midline-crossing** white-matter
bundle — its fibers **cross the midline** to connect the two
**anterior temporal lobes** and the two **olfactory structures**.
The **ipsilateral white matter** — the **centrum semiovale**, the
**cingulum**, the **corona radiata**, the **external capsule**,
the **extreme capsule**, the **fasciculus rectus**, the
**fornix**, the **internal capsule**, the **mammillothalamic
tract**, and the **medial forebrain bundle** — is the
**white-matter compartment of each cerebral hemisphere**, wired
under ``.../left/white_matter/`` and ``.../right/white_matter/``.
**They are DIFFERENT COMPARTMENTS** — the **anterior commissure**
is the **commissural (midline-crossing)** white matter; the
**white_matter** is the **ipsilateral** white matter. Consumers
must **not** conflate the anterior commissure with any ipsilateral
white-matter leaf.
**Boundary status (ANTERIOR-TEMPORAL / OLFACTORY COMMISSURE — NOT
the corpus callosum):** **Boundary case — the
anterior_commissure is the ANTERIOR-TEMPORAL / OLFACTORY
COMMISSURE, NOT the corpus callosum.** The **corpus callosum**
(``.../commissures/corpus_callosum/``) is the **neocortical
commissure** — the **largest** commissure in the human brain,
connecting the **neocortical** areas of the two hemispheres. The
**anterior commissure** (here) is the **anterior-temporal /
olfactory commissure** — the **second-largest** telencephalic
commissure, connecting the **anterior temporal lobes** and the
**olfactory structures** of the two hemispheres. **They are
SIBLINGS under the commissures container, and they are DIFFERENT
STRUCTURES** — the **corpus callosum** is the **neocortical**
commissure; the **anterior commissure** is the
**anterior-temporal / olfactory** commissure. **The two
commissures connect DIFFERENT cortical populations** — the corpus
callosum connects the **neocortex** (prefrontal, premotor,
motor, somatosensory, parietal, temporal, occipital); the
anterior commissure connects the **anterior temporal lobes** and
the **olfactory structures**. Consumers must **not** conflate the
anterior commissure with the corpus callosum.
**Boundary status (NOT the corpus callosum — the corpus callosum is
a SIBLING commissural leaf):** **Boundary case — the
anterior_commissure is NOT the corpus callosum; the corpus
callosum is a SIBLING commissural leaf.** The **corpus callosum**
(``.../commissures/corpus_callosum/``) is the **neocortical
commissure**; the **anterior commissure** (here) is the
**anterior-temporal / olfactory commissure**. **They are
SIBLINGS under the commissures container, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the anterior
commissure with the corpus callosum.
**Boundary status (NOT the commissures container — the anterior
commissure is a CHILD of the commissures):** **Boundary case —
the anterior_commissure is a CHILD of the commissures container,
not the container itself.** The **commissures** container
contains the **anterior commissure** and the **corpus callosum**
— the **anterior commissure** is **one** of those two children.
Consumers must **not** conflate the anterior commissure with the
commissures container.
**Boundary status (NOT the cerebral_hemispheres container — the
cerebral_hemispheres is the GREY-MATTER + IPSILATERAL-WHITE-
MATTER sibling):** **Boundary case — the anterior_commissure is
NOT the cerebral_hemispheres container; the
cerebral_hemispheres is the GREY-MATTER + IPSILATERAL-WHITE-
MATTER sibling.** The **cerebral_hemispheres** container
(``.../telencephalon/cerebral_hemispheres/``) holds the **left
hemisphere** and the **right hemisphere** — each of which
contains the **cortex**, the **rhinencephalon**, the
**subcortical** structures, the **white_matter**, and the
**lateral_ventricles**. The **anterior commissure** (here) is the
**anterior-temporal / olfactory commissure** — a **separate
commissural structure** that **connects** the two hemispheres.
**They are DIFFERENT COMPARTMENTS** — the
**cerebral_hemispheres** is the **grey-matter + ipsilateral-
white-matter** compartment; the **anterior commissure** is the
**commissural white matter**. Consumers must **not** conflate the
anterior commissure with the cerebral_hemispheres container.
**Boundary status (NOT the lateral_ventricles container — the
lateral_ventricles is the CSF-space sibling):** **Boundary case
— the anterior_commissure is NOT the lateral_ventricles
container; the lateral_ventricles is the CSF-space sibling.**
The **lateral_ventricles** container
(``.../telencephalon/lateral_ventricles/``) holds the **left
lateral ventricle** and the **right lateral ventricle** — the
**CSF-filled spaces** inside the cerebral hemispheres. The
**anterior commissure** (here) is the **anterior-temporal /
olfactory commissure**. **They are DIFFERENT COMPARTMENTS** — the
**lateral_ventricles** is the **CSF-space** compartment; the
**anterior commissure** is the **commissural white matter**.
Consumers must **not** conflate the anterior commissure with the
lateral_ventricles container.
**Boundary status (NOT the telencephalon container — the anterior
commissure is a GRANDCHILD of the telencephalon):** **Boundary
case — the anterior_commissure is a GRANDCHILD of the
telencephalon container.** The **telencephalon** container
contains the **cerebral_hemispheres**, the **commissures**, and
the **lateral_ventricles** — and the **commissures** in turn
contains the **anterior commissure** and the **corpus callosum**.
The **anterior commissure** is a **child of the commissures**, and
thus a **grandchild** of the telencephalon. Consumers must **not**
conflate the anterior commissure with the telencephalon container.
**Boundary status (NOT the fornix — the fornix is an IPSILATERAL
white-matter leaf, and it is the HIPPOCAMPAL OUTPUT tract):**
**Boundary case — the anterior_commissure is NOT the fornix; the
fornix is an IPSILATERAL white-matter leaf, and it is the
HIPPOCAMPAL OUTPUT tract.** The **fornix**
(``.../left/white_matter/fornix/`` and
``.../right/white_matter/fornix/``) is the **hippocampal output
tract** — an **ipsilateral** white-matter leaf under each
hemisphere's `white_matter/` container, carrying the **subicular
output** to the **mammillary bodies**, the **septal nuclei**, and
the **hypothalamus**. The **anterior commissure** (here) is the
**commissural (midline-crossing)** white-matter leaf under the
**commissures** container. **They are DIFFERENT STRUCTURES** —
the **fornix** is an **ipsilateral** white-matter leaf; the
**anterior commissure** is a **midline-crossing commissural**
white-matter leaf. **The two are in DIFFERENT containers** — the
**fornix** is under `white_matter/`; the **anterior commissure**
is under `commissures/`. Consumers must **not** conflate the
anterior commissure with the fornix.
**Boundary status (NOT the anterior temporal lobes — those are the
GREY-MATTER structures the anterior commissure connects):**
**Boundary case — the anterior_commissure is NOT the anterior
temporal lobes; those are the GREY-MATTER structures the anterior
commissure connects.** The **anterior temporal lobes**
(``.../cerebral_hemispheres/left/cortex/temporal/`` and
``.../cerebral_hemispheres/right/cortex/temporal/``) are the
**grey-matter cortex** of the **anterior temporal lobe** — one
of the **principal cortical targets** of the anterior commissure.
The **anterior commissure** (here) is the **commissural
white-matter bundle** that **connects** them. **They are
DIFFERENT STRUCTURES** — the **anterior temporal lobes** are
**grey matter**; the **anterior commissure** is **white matter**.
Consumers must **not** conflate the anterior commissure with the
anterior temporal lobes.
**Boundary status (NOT the olfactory structures — those are the
GREY-MATTER structures the anterior commissure connects):**
**Boundary case — the anterior_commissure is NOT the olfactory
structures; those are the GREY-MATTER structures the anterior
commissure connects.** The **olfactory structures** — the
**olfactory bulb**, the **olfactory tract**, the **piriform
cortex**, the **periamygdaloid cortex**, the **anterior
olfactory nucleus**, and the **uncus**
(``.../cerebral_hemispheres/left/cortex/rhinencephalon/`` and
``.../cerebral_hemispheres/right/cortex/rhinencephalon/``) — are
the **grey-matter olfactory structures** — the **other principal
targets** of the anterior commissure. The **anterior commissure**
(here) is the **commissural white-matter bundle** that
**connects** them. **They are DIFFERENT STRUCTURES** — the
**olfactory structures** are **grey matter**; the **anterior
commissure** is **white matter**. Consumers must **not** conflate
the anterior commissure with the olfactory structures.
**Boundary status (NOT the amygdala — the amygdala is a
GREY-MATTER container, and it is CONNECTED to but NOT identical
with the anterior commissure):** **Boundary case — the
anterior_commissure is NOT the amygdala; the amygdala is a
GREY-MATTER container, and it is CONNECTED to but NOT identical
with the anterior commissure.** The **amygdala**
(``.../left/subcortical/medial_temporal_lobe/amygdala/`` and
``.../right/subcortical/medial_temporal_lobe/amygdala/``) is the
**grey-matter container** of the **fear / emotion / salience**
system — the **anterior commissure** carries **some fibers** to
and from the **amygdala** (especially the **anterior cortical
nucleus** and the **medial nucleus**), but the **anterior
commissure** is **not** the amygdala. **They are DIFFERENT
STRUCTURES** — the **amygdala** is **grey matter**; the
**anterior commissure** is **white matter**. Consumers must
**not** conflate the anterior commissure with the amygdala.
**Boundary status (SLEA-FREE — the anterior commissure is NOT an
extended-amygdala component):** **Boundary case — the
anterior_commissure is SLEA-FREE.** The **SLEA overlap** belongs
to the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere). The **anterior commissure** is a
**commissural white-matter bundle** — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
**A note on the amygdala:** the anterior commissure **connects
to** the amygdala (among other structures), but it is **not
itself** an extended-amygdala component. Consumers must **not**
import the SLEA warning into the anterior commissure — it is
**SLEA-free**.
**Boundary status (MIDLINE STRUCTURE — NOT a left/right paired
structure):** **Boundary case — the anterior_commissure is a
MIDLINE STRUCTURE, NOT a left/right paired structure.** Unlike
every white-matter leaf in the cerebral hemispheres, the
**anterior commissure** is a **single midline structure** — there
is **no** `left/anterior_commissure/` and **no**
`right/anterior_commissure/`. The **anterior commissure** is a
**single midline bundle** whose fibers **cross the midline** to
connect the two **anterior temporal lobes** and the two
**olfactory structures**. Consumers must **not** look for
`left/anterior_commissure/` or `right/anterior_commissure/` —
those paths **do not exist**.
**Boundary status (WHITE-MATTER MODULE — a commissural white-matter
module in the series):** **Boundary case — the anterior_commissure
is a COMMISSURAL WHITE-MATTER module in the series.** Every
white-matter module in the `white_matter/` container (the
**centrum semiovale**, the **cingulum**, the **corona radiata**,
the **external capsule**, the **extreme capsule**, the
**fasciculus rectus**, the **fornix**, the **internal capsule**,
the **mammillothalamic tract**, and the **medial forebrain
bundle**) is an **ipsilateral** white-matter structure — a
**region of passage**, an **association bundle**, a
**projection-fiber fan**, a **capsular sheet**, a **compact
projection-fiber bundle**, a **hippocampal output tract**, a
**diencephalic projection**, or a **brainstem-forebrain bundle**.
The **anterior commissure** (here) is a **commissural
(midline-crossing)** white-matter structure — a **different
category** of white matter. Consumers must **not** treat the
anterior commissure as "another ipsilateral white-matter leaf" —
it is a **commissural** white-matter leaf, **crossing the
midline** to connect the two hemispheres.

Overview
--------
The anterior commissure is the **anterior-temporal / olfactory
commissure** of the telencephalon — a **specific named
commissural white-matter tract** that **crosses the midline** in
the **anterior wall of the third ventricle** (just **anterior**
to the **columns of the fornix**) and **connects** the
**anterior temporal lobes** of the two hemispheres (the
**anterior temporal commissure** component) and the **olfactory
structures** (the **olfactory commissure** component). It is a
**leaf** module under the commissures container, the **sibling of
the corpus callosum**, and the **commissural white-matter
substrate** of the **anterior-temporal / olfactory interhemispheric
transfer**.

**The anterior commissure is WHITE MATTER, NOT a grey-matter
structure.** It is the **commissural white-matter bundle** —
**myelinated axons** (commissural projection fibers). The
**grey-matter structures** it **connects** — the **anterior
temporal lobes** and the **olfactory structures** of the two
hemispheres — are **grey matter** and are wired under the
**cerebral_hemispheres** container.

**The anterior commissure is COMMISSURAL WHITE MATTER, NOT the
ipsilateral white matter of either hemisphere.** It **crosses the
midline** to connect the two **anterior temporal lobes** and the
two **olfactory structures**. The **ipsilateral white matter** is
wired under ``.../left/white_matter/`` and
``.../right/white_matter/``. **They are DIFFERENT COMPARTMENTS.**

**The anterior commissure is the ANTERIOR-TEMPORAL / OLFACTORY
COMMISSURE, NOT the corpus callosum.** The **corpus callosum**
(sibling) is the **neocortical commissure** — the **largest**
commissure in the human brain, connecting the **neocortical**
areas of the two hemispheres. The **anterior commissure** is the
**second-largest** telencephalic commissure, connecting the
**anterior temporal lobes** and the **olfactory structures**.
**They are SIBLINGS under the commissures container** — **the two
commissures connect DIFFERENT cortical populations**.

**The anterior commissure is NOT the fornix.** The **fornix** is
an **ipsilateral white-matter leaf** under each hemisphere's
`white_matter/` container. **The two are in DIFFERENT
containers** — the **fornix** is under `white_matter/`; the
**anterior commissure** is under `commissures/`.

**The anterior commissure is NOT the anterior temporal lobes, the
olfactory structures, or the amygdala.** Those are the
**grey-matter structures** the anterior commissure **connects**.

**The anterior commissure is SLEA-FREE.** It is **not** an
extended-amygdala component, even though it **connects to** the
**amygdala** (among other structures). The **SLEA overlap**
belongs to the **central nucleus** (the **only SLEA component** in
the amygdala) and to the **BNST**, **ventral pallidum**, and
**nucleus accumbens** (wired elsewhere).

**The anterior commissure is a MIDLINE STRUCTURE, NOT a left/right
paired structure.** There is **no** `left/anterior_commissure/`
and **no** `right/anterior_commissure/`. The **anterior
commissure** is a **single midline bundle** whose fibers **cross
the midline** to connect the two **anterior temporal lobes** and
the two **olfactory structures**. There is **no functional
lateralization** of the anterior commissure per se — but the
**connections it carries** are **bidirectional between the
hemispheres**, and the **degree of lateralization** belongs to
the **cortical grey-matter structures** whose fibers it connects
(see *Lateralization Notes*).

Course and Fiber Composition (prose, not structural children)
--------------------------------------------------------------
The anterior commissure is an **anterior-temporal / olfactory
commissure** — documented as **prose**, not as structural
children:

*   **Anterior temporal commissure component** — the **larger**
    component of the anterior commissure — carries the
    **commissural fibers** that **connect** the **anterior
    temporal lobes** of the two hemispheres. These fibers
    **cross the midline** and **terminate** in the **anterior
    temporal cortex** (the **temporal pole** and the **anterior
    middle and inferior temporal gyri**). This is the
    **anterior-temporal** substrate of the anterior commissure.

*   **Olfactory commissure component** — the **smaller**
    component of the anterior commissure — carries the
    **commissural fibers** that **connect** the **olfactory
    structures** of the two hemispheres (the **olfactory bulb**,
    the **olfactory tract**, the **piriform cortex**, the
    **periamygdaloid cortex**, the **anterior olfactory
    nucleus**, and the **uncus**). These fibers **cross the
    midline** and **terminate** in the **olfactory cortex** of
    the contralateral hemisphere. This is the **olfactory**
    substrate of the anterior commissure.

**These course and fiber details are prose, not structural
children.** The tree wires the **anterior commissure** as a
**single leaf** under ``commissures/`` — the **anterior temporal
commissure** component and the **olfactory commissure** component
are **prose**, not structural children. Consumers that need
**fiber-level** resolution should consult the references, not the
tree.

The Anterior Commissure / Corpus Callosum Boundary
--------------------------------------------------
This is the **most consequential sibling boundary** — the
**anterior-temporal / olfactory commissure vs. neocortical
commissure** boundary:

*   **Anterior_commissure** (this module) — the **anterior-
    temporal / olfactory commissure** — the **second-largest**
    telencephalic commissure, connecting the **anterior temporal
    lobes** and the **olfactory structures** of the two
    hemispheres.

*   **Corpus_callosum**
    (``.../commissures/corpus_callosum/``) — the **neocortical
    commissure** — the **largest** commissure in the human brain,
    connecting the **neocortical** areas of the two hemispheres
    (prefrontal, premotor, motor, somatosensory, parietal,
    temporal, occipital).

**They are SIBLINGS under the commissures container, and they are
DIFFERENT STRUCTURES** — the **corpus callosum** is the
**neocortical** commissure; the **anterior commissure** is the
**anterior-temporal / olfactory** commissure. **The two
commissures connect DIFFERENT cortical populations** — the corpus
callosum connects the **neocortex**; the anterior commissure
connects the **anterior temporal lobes** and the **olfactory
structures**. Consumers must **not** conflate the anterior
commissure with the corpus callosum.

The Anterior Commissure / Commissures Container Boundary
--------------------------------------------------------
This is the **child vs. container** boundary:

*   **Anterior_commissure** (this module) — a **child** of the
    commissures container.

*   **Commissures** (``.../commissures/``) — the **container**
    that contains the **anterior commissure** and the **corpus
    callosum**.

**The anterior commissure is ONE of the two children of the
commissures container.** Consumers must **not** conflate the
anterior commissure with the commissures container.

The Anterior Commissure / Cerebral Hemispheres Boundary
-------------------------------------------------------
This is the **commissural white matter vs. grey-matter +
ipsilateral-white-matter** sibling boundary:

*   **Anterior_commissure** (this module) — the **anterior-
    temporal / olfactory commissure** — a **commissural
    white-matter structure**.

*   **Cerebral_hemispheres**
    (``.../telencephalon/cerebral_hemispheres/``) — the **left
    hemisphere** and the **right hemisphere** — each containing
    the **cortex**, the **rhinencephalon**, the **subcortical**
    structures, the **white_matter**, and the
    **lateral_ventricles**.

**They are DIFFERENT COMPARTMENTS** — the **cerebral_hemispheres**
is the **grey-matter + ipsilateral-white-matter** compartment;
the **anterior commissure** is the **commissural white matter**.
Consumers must **not** conflate the anterior commissure with the
cerebral_hemispheres container.

The Anterior Commissure / Lateral Ventricles Boundary
-----------------------------------------------------
This is the **commissural white matter vs. CSF-space** sibling
boundary:

*   **Anterior_commissure** (this module) — the **commissural
    white matter** — crosses the midline in the **anterior wall
    of the third ventricle**.

*   **Lateral_ventricles**
    (``.../telencephalon/lateral_ventricles/``) — the **CSF-filled
    spaces** inside the cerebral hemispheres.

**They are DIFFERENT COMPARTMENTS** — the **lateral_ventricles**
is the **CSF-space** compartment; the **anterior commissure** is
the **commissural white matter**. Consumers must **not** conflate
the anterior commissure with the lateral_ventricles container.

The Anterior Commissure / Ipsilateral White Matter Boundary
-----------------------------------------------------------
This is the **commissural white matter vs. ipsilateral white
matter** boundary:

*   **Anterior_commissure** (this module) — the **commissural
    white matter** — the anterior-temporal / olfactory commissural
    fibers that **cross the midline**.

*   **White_matter** (``.../left/white_matter/`` and
    ``.../right/white_matter/``) — the **ipsilateral white
    matter** of each cerebral hemisphere — the **centrum
    semiovale**, the **cingulum**, the **corona radiata**, the
    **external capsule**, the **extreme capsule**, the
    **fasciculus rectus**, the **fornix**, the **internal
    capsule**, the **mammillothalamic tract**, and the **medial
    forebrain bundle**.

**They are DIFFERENT COMPARTMENTS** — the **anterior commissure**
is the **commissural white matter**; the **white_matter** is the
**ipsilateral white matter**. Consumers must **not** conflate the
anterior commissure with any ipsilateral white-matter leaf.

The Anterior Commissure / Fornix Boundary
-----------------------------------------
This is the **commissural white matter vs. hippocampal output
tract** boundary — with a **shared regional proximity** (the
anterior commissure is **just anterior** to the **columns of the
fornix**):

*   **Anterior_commissure** (this module) — the **commissural
    white matter** — crosses the midline just **anterior** to the
    **columns of the fornix**.

*   **Fornix** (``.../left/white_matter/fornix/`` and
    ``.../right/white_matter/fornix/``) — the **hippocampal output
    tract** — an **ipsilateral** white-matter leaf under each
    hemisphere's `white_matter/` container.

**They are DIFFERENT STRUCTURES** — the **fornix** is an
**ipsilateral** white-matter leaf; the **anterior commissure** is
a **midline-crossing commissural** white-matter leaf. **The two
are in DIFFERENT containers** — the **fornix** is under
`white_matter/`; the **anterior commissure** is under
`commissures/`. **The anterior commissure passes just anterior to
the columns of the fornix** — but the two are **not** the same
structure. Consumers must **not** conflate the anterior commissure
with the fornix.

The Anterior Commissure / Anterior Temporal Lobes Boundary
----------------------------------------------------------
This is the **white matter vs. grey matter** boundary — the
anterior temporal lobes are the **principal grey-matter cortical
targets** of the anterior commissure:

*   **Anterior_commissure** (this module) — the **commissural
    white-matter bundle** — **connects** the **anterior temporal
    lobes** of the two hemispheres.

*   **Anterior_temporal_lobes**
    (``.../cerebral_hemispheres/left/cortex/temporal/`` and
    ``.../cerebral_hemispheres/right/cortex/temporal/``) — the
    **grey-matter cortex** of the **anterior temporal lobe** —
    the **principal cortical targets** of the anterior
    commissure.

**They are DIFFERENT STRUCTURES** — the **anterior temporal
lobes** are **grey matter**; the **anterior commissure** is
**white matter**. Consumers must **not** conflate the anterior
commissure with the anterior temporal lobes.

The Anterior Commissure / Olfactory Structures Boundary
-------------------------------------------------------
This is the **white matter vs. grey matter** boundary — the
olfactory structures are the **other principal grey-matter
targets** of the anterior commissure:

*   **Anterior_commissure** (this module) — the **commissural
    white-matter bundle** — **connects** the **olfactory
    structures** of the two hemispheres.

*   **Olfactory_structures**
    (``.../cerebral_hemispheres/left/cortex/rhinencephalon/``
    and
    ``.../cerebral_hemispheres/right/cortex/rhinencephalon/``) —
    the **grey-matter olfactory structures** — the **olfactory
    bulb**, the **olfactory tract**, the **piriform cortex**, the
    **periamygdaloid cortex**, the **anterior olfactory
    nucleus**, and the **uncus**.

**They are DIFFERENT STRUCTURES** — the **olfactory structures**
are **grey matter**; the **anterior commissure** is **white
matter**. Consumers must **not** conflate the anterior commissure
with the olfactory structures.

The Anterior Commissure / Amygdala Boundary
-------------------------------------------
This is the **white matter vs. grey matter** boundary — the
amygdala is a **grey-matter container** to which the anterior
commissure **connects**, but is **not identical**:

*   **Anterior_commissure** (this module) — the **commissural
    white-matter bundle**.

*   **Amygdala**
    (``.../left/subcortical/medial_temporal_lobe/amygdala/`` and
    ``.../right/subcortical/medial_temporal_lobe/amygdala/``) —
    the **grey-matter container** of the **fear / emotion /
    salience** system — the anterior commissure carries **some
    fibers** to and from the **amygdala** (especially the
    **anterior cortical nucleus** and the **medial nucleus**).

**They are DIFFERENT STRUCTURES** — the **amygdala** is **grey
matter**; the **anterior commissure** is **white matter**.
Consumers must **not** conflate the anterior commissure with the
amygdala.

The Anterior Commissure / SLEA Boundary
---------------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Anterior_commissure** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The anterior commissure is NOT part of the SLEA continuum.** It
is a **commissural white-matter bundle** — it **connects to** the
amygdala (among other structures), but is **not itself** an
extended-amygdala component. **A note on the amygdala:** consumers
must **not** assume the anterior commissure is a SLEA component
**because it connects to the amygdala** — the anterior commissure
**connects to** the amygdala, but is **not itself** an
extended-amygdala component. Consumers must **not** import the
SLEA warning into the anterior commissure — it is **SLEA-free**.

The Anterior Commissure / Telencephalon Boundary
------------------------------------------------
This is the **grandchild vs. container** boundary:

*   **Anterior_commissure** (this module) — a **grandchild** of
    the telencephalon container.

*   **Telencephalon** (``.../telencephalon/``) — the
    **container** that contains the **cerebral_hemispheres**, the
    **commissures**, and the **lateral_ventricles**.

**The anterior commissure is a grandchild of the telencephalon**
(child of the commissures container). Consumers must **not**
conflate the anterior commissure with the telencephalon container.

Function in the Human Brain
---------------------------
The anterior commissure's function is **anterior-temporal /
olfactory interhemispheric transfer** — **NOT a grey-matter
function**:

*   **Anterior-Temporal Commissural Transfer:** The **anterior
    temporal commissure** component of the anterior commissure
    **connects** the **anterior temporal lobes** of the two
    hemispheres — the **anterior-temporal** substrate of the
    anterior commissure. This contributes to
    **interhemispheric transfer** of **anterior temporal** (and
    **amygdala-related**) information, including **emotional
    face processing** and **semantic memory**.

*   **Olfactory Commissural Transfer:** The **olfactory commissure**
    component of the anterior commissure **connects** the
    **olfactory structures** of the two hemispheres — the
    **olfactory** substrate of the anterior commissure. This
    contributes to **interhemispheric transfer** of **olfactory**
    information (the **only** telencephalic commissure to do so
    directly).

*   **Bitemporal Hemianopia Spared (Contrast):** Because the
    **anterior commissure** carries the **inferior**
    **decussating fibers** of the **optic chiasm** in some
    descriptions, sparing of the anterior commissure can be
    relevant to some **bitemporal hemianopia** patterns — this
    is **contested** and is **indirect**.

*   **NOT a neural processor in the classical sense.** The
    **anterior commissure** is a **commissural white-matter
    bundle** — it **conducts** the **anterior-temporal** and
    **olfactory** commissural fibers, but it does **not**
    **process** information (that happens in the **grey-matter
    structures** — the **anterior temporal cortex** and the
    **olfactory cortex**). The **fear-output** is the **central
    nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**.

**The unifying theme:** the anterior commissure is the
**anterior-temporal / olfactory commissure** of the
**telencephalon** — the **second-largest commissure** in the
human brain, and the **principal commissure** of the **anterior
temporal lobes** and the **olfactory structures**. It is
**SLEA-free** (even though it connects to the amygdala),
**commissural white matter**, and **NOT a grey-matter
structure** — the **grey-matter structures** are the **anterior
temporal lobes** and the **olfactory structures** whose fibers
pass through it.

Associated Disorders
--------------------
The anterior commissure has **no named "anterior commissure
syndrome"** in the narrow sense, but its clinical associations
are **well-documented** — primarily as an **interhemispheric
transfer** target:

*   **Agenesis of the Anterior Commissure:** The **anterior
    commissure** is **congenitally absent** in some cases of
    **commissural agenesis** — often **co-occurring** with
    **agenesis of the corpus callosum**, but sometimes **isolated**.
    The **anterior commissure** is the **white-matter substrate**
    of the **anterior-temporal / olfactory interhemispheric
    transfer** deficit in **isolated anterior commissure
    agenesis**.

*   **Split-Brain Syndrome (Anterior Commissure Component):**
    **Callosotomy** (surgical transection of the corpus callosum)
    typically **spares** the anterior commissure — the **anterior
    commissure** is the **residual commissural pathway** that
    can **partially compensate** for the **interhemispheric
    transfer** deficit after callosotomy. This is a
    **well-documented** component of **split-brain** studies
    (the anterior commissure mediates **some** residual
    interhemispheric transfer).

*   **Epilepsy Surgery (Anterior Commissurotomy):** **Anterior
    commissurotomy** — surgical transection of the anterior
    commissure — has been performed (rarely, and often in
    combination with callosotomy) for **intractable epilepsy** —
    the **anterior commissure** is the **white-matter substrate**
    of the **anterior-temporal / olfactory interhemispheric
    transfer** deficit after anterior commissurotomy.

*   **Schizophrenia (Anterior Commissure Abnormalities —
    Contested):** The **anterior commissure** shows **structural
    and DTI abnormalities** in **schizophrenia** — **reduced
    cross-sectional area** and **reduced fractional anisotropy**
    are reported. This is **contested** — the findings are
    **not** uniformly replicated.

*   **Temporal Lobe Epilepsy (Anterior Commissure Involvement):**
    The **anterior commissure** is **involved** in the
    **temporal lobe epilepsy** circuit — the **anterior
    temporal commissure** component **connects** the two anterior
    temporal lobes, and its involvement contributes to
    **seizure propagation** between the two temporal lobes. The
    **anterior commissure** is the **white-matter substrate** of
    the **anterior-temporal** component of the temporal lobe
    epilepsy circuit.

*   **Multiple Sclerosis (Anterior Commissure Plaques):** The
    **anterior commissure** is a **rare site** of **MS plaques**
    — the **demyelinating lesions** that are the **radiological
    hallmark** of **multiple sclerosis**. Its involvement is
    **rare**.

*   **No Named "Anterior Commissure Syndrome":** The **anterior
    commissure** is a **commissural white-matter bundle**, not a
    **single functional system** — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** for
    **commissural agenesis**, **split-brain** (as the residual
    pathway after callosotomy), **epilepsy surgery**, and
    **temporal lobe epilepsy** circuit involvement, and
    **contested** for **schizophrenia**.

**What is NOT here:** The **anterior commissure** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** for **commissural agenesis**, **split-brain** (as the
residual pathway), **epilepsy surgery**, and **temporal lobe
epilepsy** circuit involvement, and **contested** for
**schizophrenia**.

Lateralization Notes
--------------------
This is the **single midline** anterior_commissure module. The
**anterior commissure** is a **midline structure** — and it
carries **NO warning**:

*   **Midline Structure — NOT a Paired Structure:** The
    **anterior commissure** is a **single midline bundle** — it is
    **NOT** duplicated into `left/anterior_commissure/` and
    `right/anterior_commissure/`. The **anterior commissure** is
    a **single midline bundle** whose fibers **cross the
    midline** to connect the two **anterior temporal lobes** and
    the two **olfactory structures**. There is **no left/right
    split** of the anterior commissure itself.

*   **Bidirectional Interhemispheric Connections:** The **anterior
    commissure** carries **bidirectional** fibers between the two
    **anterior temporal lobes** and between the two **olfactory
    structures**. The **anterior commissure** is a
    **bidirectional** midline structure.

*   **NO Functional Lateralization of the Anterior Commissure per
    se:** The **functional lateralization** belongs to the
    **cortical grey-matter structures** whose fibers pass through
    the anterior commissure (e.g., the **left** and **right**
    **anterior temporal lobes**, the **left** and **right**
    **olfactory structures**) — **not** to the anterior
    commissure itself. Consumers must **not** assume the anterior
    commissure carries a **functional lateralization** of its
    own.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    anterior_commissure is **SLEA-free** — it is **not** an
    extended-amygdala component, even though it **connects to**
    the amygdala. Consumers must **not** import the SLEA warning
    into the anterior commissure.

*   **NO Amygdala-Lateralization Warning of their own (the
    anterior commissure is a COMMISSURAL WHITE-MATTER BUNDLE, not
    the fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **anterior commissure** is a
    **commissural white-matter bundle** — consumers must **not**
    conflate it with the **whole amygdala** or with the **central
    nucleus**.

**A consumer that assumes the anterior commissure is a paired
left/right structure will be structurally INCORRECT** — the
**anterior commissure** is a **single midline bundle**, not a
paired structure. The **anterior commissure** is a **strict
midline leaf** with **NO left/right split**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **anterior commissure** is
    a **midline structure** — it is **not** a left or right
    structure, so the "no cross-hemisphere imports" rule is
    **satisfied by construction**: the leaf does not belong to
    either hemisphere.
*   **No cross-lobe imports.** This module does **not** import from
    the **corpus callosum**
    (``.../commissures/corpus_callosum/``),
    ``.../telencephalon/cerebral_hemispheres/``,
    ``.../telencephalon/lateral_ventricles/``,
    ``.../left/white_matter/``, ``.../right/white_matter/``,
    ``.../left/cortex/temporal/``, ``.../right/cortex/temporal/``,
    ``.../left/cortex/rhinencephalon/``,
    ``.../right/cortex/rhinencephalon/``,
    ``.../left/subcortical/medial_temporal_lobe/amygdala/``, or
    ``.../right/subcortical/medial_temporal_lobe/amygdala/``. The
    **anterior commissure**'s relationships to the corpus callosum,
    the commissures container, the cerebral hemispheres, the
    lateral ventricles, the ipsilateral white matter, the fornix,
    the anterior temporal lobes, the olfactory structures, the
    amygdala, and the telencephalon are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **anterior
    temporal commissure** component and the **olfactory commissure**
    component are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    fiber-level detail through the references.
*   **WHITE MATTER — NOT a grey-matter structure.** The **anterior
    commissure** is **white matter**; the **anterior temporal
    lobes**, the **olfactory structures**, and the **amygdala**
    are **grey matter**. Consumers must **not** conflate the
    anterior commissure with any grey-matter structure.
*   **COMMISSURAL WHITE MATTER — NOT the ipsilateral white
    matter.** The **anterior commissure** is the **commissural
    (midline-crossing)** white matter; the **white_matter** under
    each hemisphere is the **ipsilateral** white matter.
    Consumers must **not** conflate the two.
*   **ANTERIOR-TEMPORAL / OLFACTORY COMMISSURE — NOT the corpus
    callosum.** The **corpus callosum** (sibling) is the
    **neocortical commissure**; the **anterior commissure** is the
    **anterior-temporal / olfactory commissure**. Consumers must
    **not** conflate the two.
*   **NOT the corpus callosum — the corpus callosum is a SIBLING
    commissural leaf.**
*   **NOT the commissures container — the anterior commissure is a
    CHILD of the commissures.**
*   **NOT the cerebral_hemispheres container — the
    cerebral_hemispheres is the GREY-MATTER + IPSILATERAL-WHITE-
    MATTER sibling.**
*   **NOT the lateral_ventricles container — the
    lateral_ventricles is the CSF-space sibling.**
*   **NOT the telencephalon container — the anterior commissure is a
    GRANDCHILD of the telencephalon.**
*   **NOT the fornix — the fornix is an IPSILATERAL white-matter
    leaf under each hemisphere's `white_matter/` container.** The
    two are in **DIFFERENT containers**.
*   **NOT the anterior temporal lobes, the olfactory structures, or
    the amygdala — those are GREY-MATTER structures the anterior
    commissure connects.**
*   **SLEA-FREE — no extended-amygdala relationship.** The anterior
    commissure is **not** an extended-amygdala component, even
    though it connects to the amygdala.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning) are **amygdala** children; the
    **anterior commissure** is a **commissural white-matter
    bundle**.
*   **MIDLINE STRUCTURE — NOT a left/right paired structure.**
    There is **no** `left/anterior_commissure/` and **no**
    `right/anterior_commissure/`. Consumers must **not** look for
    those paths — they **do not exist**.
*   **No ``AREA_PATHS`` hop.** The **anterior commissure** is a
    local leaf under ``commissures/``, not a cross-listed leaf.
*   **No nested cross-listing.** The **anterior commissure** has no
    nested dual-framing module. It is a single leaf.
*   **NO left/right mirror — MIDLINE leaf with NO warning.** The
    **anterior commissure** is a **single midline leaf** — there
    is **no** `left/anterior_commissure/` and **no**
    `right/anterior_commissure/`. The **leaf itself** is
    **strictly hemisphere-neutral**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.commissures import anterior_commissure

Or by fully-qualified path string::

    path = (
        "telencephalon.commissures.anterior_commissure"
    )

**Do not** assume the anterior commissure is the **corpus callosum**.
The **corpus callosum** is the **sibling** commissural leaf — the
**neocortical commissure**. The **anterior commissure** is the
**anterior-temporal / olfactory commissure**.

**Do not** assume the anterior commissure is the **commissures
container**. The **commissures** is the **container** — the
**anterior commissure** is **one** of its two children.

**Do not** assume the anterior commissure is the **cerebral
hemispheres container** or the **lateral ventricles container**.
Those are the **sibling** compartments under the telencephalon.

**Do not** assume the anterior commissure is the **fornix**. The
**fornix** is an **ipsilateral white-matter leaf** under each
hemisphere's `white_matter/` container — the two are in
**different containers**.

**Do not** assume the anterior commissure is the **anterior
temporal lobes**, the **olfactory structures**, or the
**amygdala**. Those are the **grey-matter structures** the
anterior commissure **connects**.

**Do not** assume the anterior commissure is a **left/right
paired structure**. The **anterior commissure** is a **single
midline bundle** — there is **no** `left/anterior_commissure/`
and **no** `right/anterior_commissure/`.

**Do not** assume the anterior commissure is the **telencephalon
container**. The **telencephalon** container contains the
**cerebral_hemispheres**, the **commissures**, and the
**lateral_ventricles** — and the **commissures** in turn
contains the **anterior commissure** and the **corpus callosum**.

**Do not** assume the anterior commissure is the **ipsilateral
white matter** of the cerebral hemispheres. The **ipsilateral
white matter** is wired under ``.../left/white_matter/`` and
``.../right/white_matter/``; the **anterior commissure** is the
**commissural (midline-crossing)** white matter.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the anterior commissure.
**The anterior commissure is SLEA-FREE** — it is **not** an
extended-amygdala component, even though it connects to the
amygdala, and it is **NOT the fear-output structure**.

Iterating the anterior commissure's (empty) children (recommended
consumer pattern)::

    ANTERIOR_COMMISSURE_CHILDREN = ()
    # The anterior commissure is a leaf. The anterior temporal
    # commissure component and the olfactory commissure component
    # are prose, not modules.

Reaching the corpus callosum sibling (recommended consumer pattern —
the neocortical commissure)::

    # The corpus callosum is the NEOCORTICAL COMMISSURE — the
    # SIBLING of the anterior commissure under the commissures
    # container:
    #
    #   telencephalon.commissures.corpus_callosum
    #
    # The corpus callosum is the largest commissure in the human
    # brain (neocortical); the anterior commissure is the
    # anterior-temporal / olfactory commissure. The two commissures
    # connect DIFFERENT cortical populations.

Reaching the commissures container (recommended consumer pattern —
the container)::

    # The commissures is the CONTAINER that contains the anterior
    # commissure and the corpus callosum:
    #
    #   telencephalon.commissures
    #
    # The anterior commissure is ONE of the two children of the
    # commissures container.

Reaching the cerebral hemispheres (recommended consumer pattern —
the grey-matter + ipsilateral-white-matter sibling)::

    # The cerebral_hemispheres is the GREY-MATTER +
    # IPSILATERAL-WHITE-MATTER sibling under the telencephalon:
    #
    #   telencephalon.cerebral_hemispheres
    #
    # The cerebral_hemispheres is the grey-matter + ipsilateral-
    # white-matter compartment; the anterior commissure is the
    # commissural white matter.

Reaching the lateral ventricles (recommended consumer pattern — the
CSF-space sibling)::

    # The lateral_ventricles is the CSF-SPACE sibling under the
    # telencephalon:
    #
    #   telencephalon.lateral_ventricles
    #
    # The lateral_ventricles is the CSF-space compartment; the
    # anterior commissure is the commissural white matter.

Reaching the fornix (recommended consumer pattern — the ipsilateral
hippocampal output tract)::

    # The fornix is the HIPPOCAMPAL OUTPUT TRACT — an IPSILATERAL
    # white-matter leaf under each hemisphere's white_matter
    # container:
    #
    #   cerebral_hemispheres.left.white_matter.fornix
    #   cerebral_hemispheres.right.white_matter.fornix
    #
    # The fornix is an ipsilateral white-matter leaf; the anterior
    # commissure is a midline-crossing commissural leaf. The two
    # are in DIFFERENT containers.

Reaching the anterior temporal lobes (recommended consumer pattern
— the principal cortical targets)::

    # The anterior temporal lobes are the GREY-MATTER CORTICAL
    # TARGETS of the anterior commissure:
    #
    #   cerebral_hemispheres.left.cortex.temporal
    #   cerebral_hemispheres.right.cortex.temporal
    #
    # The anterior temporal lobes are grey matter; the anterior
    # commissure is white matter — the anterior-temporal
    # commissural projection that connects them.

Reaching the olfactory structures (recommended consumer pattern —
the other principal cortical targets)::

    # The olfactory structures are the GREY-MATTER OLFACTORY
    # TARGETS of the anterior commissure:
    #
    #   cerebral_hemispheres.left.cortex.rhinencephalon
    #   cerebral_hemispheres.right.cortex.rhinencephalon
    #
    # The olfactory structures are grey matter; the anterior
    # commissure is white matter — the olfactory commissural
    # projection that connects them.

Reaching the amygdala (recommended consumer pattern — a
grey-matter container the anterior commissure connects to)::

    # The amygdala is a GREY-MATTER CONTAINER the anterior
    # commissure connects to (among other structures):
    #
    #   cerebral_hemispheres.left.subcortical.medial_temporal_lobe.amygdala
    #   cerebral_hemispheres.right.subcortical.medial_temporal_lobe.amygdala
    #
    # The amygdala is grey matter; the anterior commissure is white
    # matter — the anterior commissure carries some fibers to and
    # from the amygdala (especially the anterior cortical nucleus
    # and the medial nucleus).
    #
    # NOTE: the anterior commissure connects to the amygdala, but
    # is NOT itself an extended-amygdala component.

Reaching the telencephalon (recommended consumer pattern — the
container)::

    # The telencephalon is the CONTAINER that contains the
    # cerebral_hemispheres, the commissures, and the
    # lateral_ventricles:
    #
    #   telencephalon
    #
    # The anterior commissure is a GRANDCHILD of the telencephalon
    # (child of the commissures).

Reaching the SLEA components (recommended consumer pattern — NOTE
the anterior commissure is NOT included, even though it connects
to the amygdala)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # anterior commissure:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The anterior commissure is SLEA-FREE — it connects to the
    # amygdala (among other structures), but is NOT itself a SLEA
    # component.

Fiber-level detail (not wired — consult references)::

    # The anterior commissure's fiber components are prose, not
    # modules:
    #   anterior temporal commissure component -> larger component;
    #                                             connects the
    #                                             anterior temporal
    #                                             lobes of the two
    #                                             hemispheres
    #   olfactory commissure component        -> smaller component;
    #                                             connects the
    #                                             olfactory
    #                                             structures of the
    #                                             two hemispheres
    #
    # Do not attempt to resolve these as sub-paths of the anterior
    # commissure.

Midline (no bilateral iteration — recommended consumer pattern)::

    # The anterior commissure is a SINGLE MIDLINE STRUCTURE — there
    # is NO left/right split. Do NOT iterate over ("left", "right")
    # for the anterior commissure itself.
    #
    # The anterior commissure CROSSES the midline; its fibers are
    # bidirectional between the two anterior temporal lobes and
    # between the two olfactory structures.

References
----------
*   **Canonical anterior commissure anatomy:** FitzGerald, M.J.T.,
    Folan-Curran, J., O'Brien, E. (2001). "The anterior commissure
    in the human brain." *Journal of Anatomy* 199:669–676. (The
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
*   **Commissural development:** Raybaud, C., Girard, N. (2008).
    "The developmental disorders of the corpus callosum."
    *Child's Nervous System* 24:1159–1170. (Commissural
    development — anterior commissure and corpus callosum.)
*   **Split-brain studies (anterior commissure component):**
    Sperry, R.W. (1968). "Hemisphere deconnection and unity in
    conscious awareness." *American Psychologist* 23:723–733.
    (The original split-brain studies — anterior commissure as
    the residual commissural pathway after callosotomy.)
*   **Split-brain (review — anterior commissure component):**
    Gazzaniga, M.S. (2005). "Forty-five years of split-brain
    research and still going strong." *Nature Reviews
    Neuroscience* 6:653–659. (Review of the split-brain studies
    — the anterior commissure as the residual interhemispheric
    pathway.)
*   **Anterior commissure and anterior temporal transfer:**
    Catani, M., Thiebaut de Schotten, M. (2012). *Atlas of Human
    Brain Connections*. Oxford University Press, Oxford. (The
    anterior commissure in the human connectome — the
    anterior-temporal and olfactory components.)
*   **White-matter atlas (human):** Wakana, S., Jiang, H., Nagae,
    L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter atlas
    of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the anterior commissure in DTI.)
*   **DTI tractography atlas:** Catani, M., Thiebaut de Schotten,
    M. (2008). "A diffusion tensor imaging tractography atlas for
    virtual in vivo dissections." *Cortex* 44:1105–1132. (The
    anterior commissure in DTI tractography.)
*   **Fiber pathways (review):** Schmahmann, J.D., Pandya, D.N.
    (2006). *Fiber Pathways of the Brain*. Oxford University
    Press, New York. (Definitive white-matter anatomy; the
    anterior commissure as an anterior-temporal / olfactory
    commissure.)
*   **Commissural agenesis (review):** Paul, L.K., et al. (2007).
    "Agenesis of the corpus callosum: genetic, developmental and
    functional aspects of connectivity." *Nature Reviews
    Neuroscience* 8:287–299. (Commissural agenesis — corpus
    callosum and anterior commissure.)
*   **Anterior commissurotomy and epilepsy:** Engel, J., Jr.
    (1996). "Surgery for seizures." *New England Journal of
    Medicine* 334:647–652. (Epilepsy surgery — anterior
    commissurotomy as a (rare) surgical option for intractable
    epilepsy.)
*   **Temporal lobe epilepsy and the anterior commissure:** Spencer,
    S.S. (2002). "Neural networks in human epilepsy: evidence of
    and implications for treatment." *Epilepsia* 43:219–227.
    (Temporal lobe epilepsy — the anterior commissure as a
    propagation pathway between the two temporal lobes.)
*   **Schizophrenia and the anterior commissure (contested):**
    Highley, J.R., et al. (1999). "Sex-dependent changes in
    anterior commissure size in schizophrenia." *Biological
    Psychiatry* 46:546–549. (Anterior commissure abnormalities in
    schizophrenia — contested.)
*   **Multiple sclerosis and the anterior commissure:** Polman,
    C.H., et al. (2011). "Diagnostic criteria for multiple
    sclerosis: 2010 revisions to the McDonald criteria." *Annals
    of Neurology* 69:292–302. (MS plaques in the anterior
    commissure — rare.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    anterior commissure is not the amnesia substrate):** Scoville,
    W.B., Milner, B. (1957). "Loss of recent memory after
    bilateral hippocampal lesions." *Journal of Neurology,
    Neurosurgery, and Psychiatry* 20:11–21. (Bilateral
    hippocampal damage and anterograde amnesia — distinct from
    the anterior commissure.)
*   **Amygdala (contrast — the anterior commissure is NOT the
    amygdala):** LeDoux, J.E. (2000). "Emotion circuits in the
    brain." *Annual Review of Neuroscience* 23:155–184.
    (Amygdala fear circuit — distinct from the anterior
    commissure.)
*   **SLEA (contrast — the anterior commissure is not included,
    even though it connects to the amygdala):** Alheid, G.F.,
    Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    anterior commissure.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Anterior commissure in overview.)
*   NeuroNames — Anterior commissure; FMA — Anterior commissure.
"""