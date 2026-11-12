"""
infrastructure.brainparts.forebrain.telencephalon.commissures.corpus_callosum
============================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    ├── cerebral_hemispheres
    ├── commissures
    │   ├── anterior_commissure
    │   └── corpus_callosum   <-- THIS MODULE
    └── lateral_ventricles

**Primary synonym:** Corpus callosum; CC; **the great commissure**;
**the neocortical commissure**; **the largest commissure in the
human brain**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **great midline commissural bundle**
that **crosses the midline** beneath the **longitudinal fissure**
and **above the lateral ventricles**, **connecting** the
**neocortical areas** of the two cerebral hemispheres
(prefrontal, premotor, primary motor, primary somatosensory,
parietal association, temporal, and occipital cortices). It is a
**specific named white-matter tract** — a **commissural
white-matter leaf**, **not** a region of passage, **not** a
projection-fiber fan, **not** a capsular white-matter sheet,
**not** an association bundle, **not** a compact projection-fiber
bundle, **not** a hippocampal output tract, **not** a diencephalic
projection, **not** a brainstem-forebrain bundle.
**Part of:** The **commissures** container of the telencephalon —
the **neocortical commissure**. The **corpus callosum** is the
**largest** and **most clinically consequential** commissure in
the human brain, and it is the **principal commissure** of the
**neocortex**.
**Structural parent:** ``.../commissures/`` → **direct child** of
the commissures container.
**Structural children:** **None.** This is a **leaf** module. The
**rostrum**, **genu**, **body (truncus)**, **isthmus**, and
**splenium** of the corpus callosum are documented as **prose**,
not as structural children. The **callosal radiations** (the
**white-matter fibers** that **pass through the cerebral
hemisphere's white matter** to reach the cortex) are documented as
**prose** as well.
**Boundary status (WHITE MATTER — NOT a grey-matter structure):**
**Boundary case — the corpus_callosum is WHITE MATTER, NOT a
grey-matter structure.** The **corpus callosum** (here) is the
**great midline commissural bundle** — **myelinated axons**
(commissural projection fibers). The **grey-matter structures**
that the corpus callosum **connects** — the **neocortical areas**
of the two hemispheres (prefrontal, premotor, primary motor,
primary somatosensory, parietal association, temporal, and
occipital cortices) — are **grey matter** and are wired under
``.../cerebral_hemispheres/left/cortex/`` and
``.../cerebral_hemispheres/right/cortex/``. **They are DIFFERENT
STRUCTURES** — the **corpus callosum** is the **commissural
white-matter bundle**; the **neocortical areas** are the
**grey-matter structures** it **connects**. Consumers must **not**
conflate the corpus callosum with any grey-matter structure.
**Boundary status (NEOCORTICAL COMMISSURE — the LARGEST and MOST
CLINICALLY CONSEQUENTIAL commissure in the human brain):**
**Boundary case — the corpus_callosum is the NEOCORTICAL
COMMISSURE, and it is the LARGEST and MOST CLINICALLY CONSEQUENTIAL
commissure in the human brain.** Unlike its only sibling (the
**anterior commissure**, which is the **anterior-temporal /
olfactory** commissure), the corpus callosum is the **neocortical**
commissure — it **connects** the **neocortical areas** of the two
hemispheres (prefrontal, premotor, primary motor, primary
somatosensory, parietal association, temporal, and occipital
cortices), and it is the **anatomical substrate** of
**interhemispheric transfer** at the **neocortical** level. It is
the **largest** commissure in the human brain (approximately
**200 million** axons in the human), and it is the **most
clinically consequential** — the **target** of **callosotomy**, the
**site** of **agenesis of the corpus callosum**, **Marchiafava-
Bignami disease**, **MS Dawson's fingers**, and **Alexander
disease**. Consumers must **not** treat the corpus callosum as
"just another commissure" — it is the **neocortical** commissure,
the **principal** interhemispheric pathway at the **neocortical**
level.
**Boundary status (COMMISSURAL WHITE MATTER — NOT the ipsilateral
white matter of either hemisphere):** **Boundary case — the
corpus_callosum is COMMISSURAL WHITE MATTER, NOT the ipsilateral
white matter of either hemisphere.** The **corpus callosum**
(here) is a **midline-crossing** white-matter bundle — its fibers
**cross the midline** to connect the **neocortical areas** of the
two hemispheres. The **ipsilateral white matter** — the **centrum
semiovale**, the **cingulum**, the **corona radiata**, the
**external capsule**, the **extreme capsule**, the **fasciculus
rectus**, the **fornix**, the **internal capsule**, the
**mammillothalamic tract**, and the **medial forebrain bundle** —
is the **white-matter compartment of each cerebral hemisphere**,
wired under ``.../left/white_matter/`` and
``.../right/white_matter/``. **They are DIFFERENT COMPARTMENTS** —
the **corpus callosum** is the **commissural (midline-crossing)**
white matter; the **white_matter** is the **ipsilateral** white
matter. **A note on the callosal radiations:** the corpus callosum
has **callosal radiations** that **pass through** the hemisphere's
white matter (specifically through the **centrum semiovale**) to
reach the **neocortical** cortex — the **centrum semiovale**
docstring documents this as **prose** ("callosal radiations"), but
the **corpus callosum itself** is a **separate structure** wired
under the **commissures** container, **not** under the hemisphere's
white_matter container. Consumers must **not** conflate the corpus
callosum with any ipsilateral white-matter leaf, and must **not**
assume the corpus callosum is "part of" the centrum semiovale just
because the callosal radiations pass through it.
**Boundary status (NOT the anterior commissure — the anterior
commissure is a SIBLING commissural leaf):** **Boundary case —
the corpus_callosum is NOT the anterior commissure; the anterior
commissure is a SIBLING commissural leaf.** The **anterior
commissure** (``.../commissures/anterior_commissure/``) is the
**anterior-temporal / olfactory** commissure — the **second-
largest** telencephalic commissure, connecting the **anterior
temporal lobes** and the **olfactory structures** of the two
hemispheres. The **corpus callosum** (here) is the **neocortical**
commissure — the **largest** commissure in the human brain,
connecting the **neocortical areas** of the two hemispheres.
**They are SIBLINGS under the commissures container, and they are
DIFFERENT STRUCTURES** — the **corpus callosum** is the
**neocortical** commissure; the **anterior commissure** is the
**anterior-temporal / olfactory** commissure. **The two
commissures connect DIFFERENT cortical populations** — the corpus
callosum connects the **neocortex**; the anterior commissure
connects the **anterior temporal lobes** and the **olfactory
structures**. Consumers must **not** conflate the corpus callosum
with the anterior commissure.
**Boundary status (NOT the commissures container — the corpus
callosum is a CHILD of the commissures):** **Boundary case — the
corpus_callosum is a CHILD of the commissures container, not the
container itself.** The **commissures** container contains the
**corpus callosum** and the **anterior commissure** — the
**corpus callosum** is **one** of those two children. Consumers
must **not** conflate the corpus callosum with the commissures
container.
**Boundary status (NOT the cerebral_hemispheres container — the
cerebral_hemispheres is the GREY-MATTER + IPSILATERAL-WHITE-
MATTER sibling):** **Boundary case — the corpus_callosum is NOT
the cerebral_hemispheres container; the cerebral_hemispheres is
the GREY-MATTER + IPSILATERAL-WHITE-MATTER sibling.** The
**cerebral_hemispheres** container
(``.../telencephalon/cerebral_hemispheres/``) holds the **left
hemisphere** and the **right hemisphere** — each of which
contains the **cortex**, the **rhinencephalon**, the
**subcortical** structures, the **white_matter**, and the
**lateral_ventricles**. The **corpus callosum** (here) is the
**neocortical commissure** — a **separate commissural structure**
that **connects** the two hemispheres. **They are DIFFERENT
COMPARTMENTS** — the **cerebral_hemispheres** is the **grey-matter
+ ipsilateral-white-matter** compartment; the **corpus callosum**
is the **commissural white matter**. Consumers must **not**
conflate the corpus callosum with the cerebral_hemispheres
container.
**Boundary status (NOT the lateral_ventricles container — the
lateral_ventricles is the CSF-space sibling):** **Boundary case —
the corpus_callosum is NOT the lateral_ventricles container; the
lateral_ventricles is the CSF-space sibling.** The
**lateral_ventricles** container
(``.../telencephalon/lateral_ventricles/``) holds the **left
lateral ventricle** and the **right lateral ventricle** — the
**CSF-filled spaces** inside the cerebral hemispheres. The
**corpus callosum** (here) is the **neocortical commissure** —
its **body** forms the **roof** of the **lateral ventricles**, and
the **septum pellucidum** is the **thin midline membrane**
between the **body of the corpus callosum** (above) and the
**fornix** (below). **They are DIFFERENT COMPARTMENTS** — the
**lateral_ventricles** is the **CSF-space** compartment; the
**corpus callosum** is the **commissural white matter**.
Consumers must **not** conflate the corpus callosum with the
lateral_ventricles container.
**Boundary status (NOT the telencephalon container — the corpus
callosum is a GRANDCHILD of the telencephalon):** **Boundary case
— the corpus_callosum is a GRANDCHILD of the telencephalon
container.** The **telencephalon** container contains the
**cerebral_hemispheres**, the **commissures**, and the
**lateral_ventricles** — and the **commissures** in turn contains
the **corpus callosum** and the **anterior commissure**. The
**corpus callosum** is a **child of the commissures**, and thus a
**grandchild** of the telencephalon. Consumers must **not**
conflate the corpus callosum with the telencephalon container.
**Boundary status (NOT the septum pellucidum — the septum
pellucidum is a SEPARATE midline structure, NOT the corpus
callosum):** **Boundary case — the corpus_callosum is NOT the
septum pellucidum; the septum pellucidum is a SEPARATE midline
structure, NOT the corpus callosum.** The **septum pellucidum**
is a **thin midline membrane** (a **pia-arachnoid derivative**)
that **separates** the **anterior horns** and **bodies** of the
two **lateral ventricles** — it **lies between** the **body of
the corpus callosum** (above) and the **fornix** (below). The
**corpus callosum** (here) is the **neocortical commissure** —
the **commissural white-matter bundle**. **They are DIFFERENT
STRUCTURES** — the **septum pellucidum** is a **thin midline
membrane** (and the tree does **not** currently wire it — it is
documented here as **prose**); the **corpus callosum** is the
**commissural white-matter bundle**. Consumers must **not**
conflate the corpus callosum with the septum pellucidum.
**Boundary status (NOT the fornix — the fornix is an IPSILATERAL
white-matter leaf, and it is the HIPPOCAMPAL OUTPUT tract):**
**Boundary case — the corpus_callosum is NOT the fornix; the
fornix is an IPSILATERAL white-matter leaf, and it is the
HIPPOCAMPAL OUTPUT tract.** The **fornix**
(``.../left/white_matter/fornix/`` and
``.../right/white_matter/fornix/``) is the **hippocampal output
tract** — an **ipsilateral** white-matter leaf under each
hemisphere's `white_matter/` container, carrying the **subicular
output** to the **mammillary bodies**, the **septal nuclei**, and
the **hypothalamus**. The **corpus callosum** (here) is the
**commissural (midline-crossing)** white-matter leaf under the
**commissures** container. **They are DIFFERENT STRUCTURES** —
the **fornix** is an **ipsilateral** white-matter leaf; the
**corpus callosum** is a **midline-crossing commissural**
white-matter leaf. **The two are in DIFFERENT containers** — the
**fornix** is under `white_matter/`; the **corpus callosum** is
under `commissures/`. **The body of the fornix** is
**immediately below** the **body of the corpus callosum**, with
the **septum pellucidum** between them — but the two are **not**
the same structure. Consumers must **not** conflate the corpus
callosum with the fornix.
**Boundary status (NOT the neocortical areas — those are the
GREY-MATTER structures the corpus callosum connects):** **Boundary
case — the corpus_callosum is NOT the neocortical areas; those are
the GREY-MATTER structures the corpus callosum connects.** The
**neocortical areas** of the two hemispheres
(``.../cerebral_hemispheres/left/cortex/`` and
``.../cerebral_hemispheres/right/cortex/``) — the **prefrontal**,
**premotor**, **primary motor**, **primary somatosensory**,
**parietal association**, **temporal**, and **occipital** cortices
— are the **grey-matter structures** the corpus callosum
**connects**. The **corpus callosum** (here) is the
**commissural white-matter bundle** that **connects** them.
**They are DIFFERENT STRUCTURES** — the **neocortical areas** are
**grey matter**; the **corpus callosum** is **white matter**.
Consumers must **not** conflate the corpus callosum with any
neocortical area.
**Boundary status (NOT a single uniform commissure — MULTIPLE
topographic segments):** **Boundary case — the corpus_callosum is
a HETEROGENEOUS commissure with MULTIPLE topographic segments
(rostrum, genu, body, isthmus, splenium), not a single uniform
bundle.** The **topographic segments** are **functionally
distinct** — the **rostrum** and **genu** connect the **prefrontal**
and **premotor** areas; the **body** connects the **primary
motor** and **primary somatosensory** areas and the **parietal
association** areas; the **isthmus** connects the **superior
temporal** and **posterior parietal** areas; the **splenium**
connects the **occipital** and **posterior temporal** areas. The
tree wires the **corpus callosum** as a **single leaf** under the
commissures container — the **rostrum**, **genu**, **body**,
**isthmus**, and **splenium** are **prose**, not structural
children. Consumers that need **segment-level** resolution should
consult the references, not the tree.
**Boundary status (SLEA-FREE — the corpus callosum is NOT an
extended-amygdala component):** **Boundary case — the
corpus_callosum is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala)
and to the **BNST**, **ventral pallidum**, and **nucleus accumbens**
(wired elsewhere). The **corpus callosum** is a **commissural
white-matter bundle** — it is **NOT** an extended-amygdala
component, and it carries **NO SLEA warning**. Consumers must
**not** import the SLEA warning into the corpus callosum — it is
**SLEA-free**.
**Boundary status (MIDLINE STRUCTURE — NOT a left/right paired
structure):** **Boundary case — the corpus_callosum is a MIDLINE
STRUCTURE, NOT a left/right paired structure.** Unlike every
white-matter leaf in the cerebral hemispheres, the **corpus
callosum** is a **single midline structure** — there is **no**
`left/corpus_callosum/` and **no** `right/corpus_callosum/`. The
**corpus callosum** is a **single midline bundle** whose fibers
**cross the midline** to connect the **neocortical areas** of the
two hemispheres. Consumers must **not** look for
`left/corpus_callosum/` or `right/corpus_callosum/` — those paths
**do not exist**.
**Boundary status (COMMISSURAL WHITE-MATTER MODULE — a commissural
white-matter module in the series):** **Boundary case — the
corpus_callosum is a COMMISSURAL WHITE-MATTER module in the
series.** Every white-matter module in the `white_matter/`
container (the **centrum semiovale**, the **cingulum**, the
**corona radiata**, the **external capsule**, the **extreme
capsule**, the **fasciculus rectus**, the **fornix**, the
**internal capsule**, the **mammillothalamic tract**, and the
**medial forebrain bundle**) is an **ipsilateral** white-matter
structure — a **region of passage**, an **association bundle**, a
**projection-fiber fan**, a **capsular sheet**, a **compact
projection-fiber bundle**, a **hippocampal output tract**, a
**diencephalic projection**, or a **brainstem-forebrain bundle**.
The **corpus callosum** (here) is a **commissural
(midline-crossing)** white-matter structure — a **different
category** of white matter. Consumers must **not** treat the
corpus callosum as "another ipsilateral white-matter leaf" — it
is a **commissural** white-matter leaf, **crossing the midline**
to connect the two hemispheres.

Overview
--------
The corpus callosum is the **neocortical commissure** of the
telencephalon — the **great midline commissural bundle** that
**crosses the midline** beneath the **longitudinal fissure** and
**above the lateral ventricles**, **connecting** the **neocortical
areas** of the two cerebral hemispheres (prefrontal, premotor,
primary motor, primary somatosensory, parietal association,
temporal, and occipital cortices). It is the **largest** and
**most clinically consequential** commissure in the human brain
(approximately **200 million** axons), and it is the **principal
commissure** of the **neocortex**. It is a **leaf** module under
the commissures container, the **sibling of the anterior
commissure**, and the **commissural white-matter substrate** of
**neocortical interhemispheric transfer**.

**The corpus callosum is WHITE MATTER, NOT a grey-matter
structure.** It is the **great midline commissural bundle** —
**myelinated axons** (commissural projection fibers). The
**grey-matter structures** it **connects** — the **neocortical
areas** of the two hemispheres — are **grey matter** and are
wired under the **cerebral_hemispheres** container.

**The corpus callosum is the NEOCORTICAL COMMISSURE — the LARGEST
and MOST CLINICALLY CONSEQUENTIAL commissure in the human brain.**
It is the **anatomical substrate** of **interhemispheric
transfer** at the **neocortical** level, and it is the **target**
of **callosotomy**, the **site** of **agenesis of the corpus
callosum**, **Marchiafava-Bignami disease**, **MS Dawson's
fingers**, and **Alexander disease**.

**The corpus callosum is COMMISSURAL WHITE MATTER, NOT the
ipsilateral white matter of either hemisphere.** It **crosses the
midline** to connect the **neocortical areas** of the two
hemispheres. **A note on the callosal radiations:** the corpus
callosum's fibers pass through the **centrum semiovale** (as
**prose**) to reach the **neocortical** cortex — but the **corpus
callosum itself** is a **separate structure** wired under the
**commissures** container.

**The corpus callosum is NOT the anterior commissure.** The
**anterior commissure** (sibling) is the **anterior-temporal /
olfactory** commissure — the **second-largest** telencephalic
commissure. **The two commissures connect DIFFERENT cortical
populations** — the corpus callosum connects the **neocortex**;
the anterior commissure connects the **anterior temporal lobes**
and the **olfactory structures**.

**The corpus callosum is NOT the fornix.** The **fornix** is an
**ipsilateral white-matter leaf** under each hemisphere's
`white_matter/` container. **The two are in DIFFERENT
containers** — the **fornix** is under `white_matter/`; the
**corpus callosum** is under `commissures/`. The **body of the
fornix** is **immediately below** the **body of the corpus
callosum**, with the **septum pellucidum** between them — but the
two are **not** the same structure.

**The corpus callosum is NOT the neocortical areas.** Those are the
**grey-matter structures** the corpus callosum **connects**.

**The corpus callosum is NOT the septum pellucidum.** The **septum
pellucidum** is a **thin midline membrane** that **lies between**
the **body of the corpus callosum** (above) and the **fornix**
(below) — it is **documented here as prose** (the tree does not
currently wire it), and it is **not** the corpus callosum.

**The corpus callosum is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**.
The **SLEA overlap** belongs to the **central nucleus** (the
**only SLEA component** in the amygdala) and to the **BNST**,
**ventral pallidum**, and **nucleus accumbens** (wired
elsewhere).

**The corpus callosum is a MIDLINE STRUCTURE, NOT a left/right
paired structure.** There is **no** `left/corpus_callosum/` and
**no** `right/corpus_callosum/`. The **corpus callosum** is a
**single midline bundle** whose fibers **cross the midline** to
connect the **neocortical areas** of the two hemispheres. There is
**no functional lateralization** of the corpus callosum per se —
but the **connections it carries** are **bidirectional between the
hemispheres**, and the **degree of lateralization** belongs to the
**cortical grey-matter structures** whose fibers it connects (see
*Lateralization Notes*).

Topographic Segments (prose, not structural children)
-----------------------------------------------------
The corpus callosum is a **specific named commissural tract** —
documented as **prose**, not as structural children. It is
conventionally divided into the following topographic segments
(from **anterior** to **posterior**):

*   **Rostrum** — the **anterior-most** part of the corpus
    callosum, the **thin** portion that **curves inferiorly**
    (posteriorly) from the **genu** toward the **lamina
    terminalis** and the **anterior commissure**. It connects
    the **inferior frontal** and **orbitofrontal** areas of the
    two hemispheres.

*   **Genu** — the **anterior bend** of the corpus callosum (its
    "knee"). It is the **thickest** part of the corpus callosum
    anteriorly, and it **curves** from the **rostrum** into the
    **body**. It connects the **prefrontal** and **premotor**
    areas of the two hemispheres.

*   **Body (truncus)** — the **middle** part of the corpus
    callosum, between the **genu** (anterior) and the
    **splenium** (posterior). It forms the **roof** of the
    **lateral ventricles' body**. It connects the **primary
    motor**, **primary somatosensory**, and **parietal
    association** areas of the two hemispheres.

*   **Isthmus** — the **narrow transition** between the **body**
    and the **splenium**, sometimes distinguished as a **separate
    segment**. It connects the **superior temporal** and
    **posterior parietal** areas of the two hemispheres.

*   **Splenium** — the **posterior-most** part of the corpus
    callosum, the **thickest** part of the corpus callosum
    posteriorly. It connects the **occipital** and **posterior
    temporal** areas of the two hemispheres.

**These topographic segments are prose, not structural
children.** The tree wires the **corpus callosum** as a **single
leaf** under ``commissures/`` — the **rostrum**, **genu**,
**body**, **isthmus**, and **splenium** are **prose**, not
structural children. Consumers that need **segment-level**
resolution should consult the references, not the tree.

Fiber Composition (prose, not structural children)
--------------------------------------------------
The corpus callosum is a **neocortical commissure** — documented
as **prose**, not as structural children:

*   **Homotopic commissural fibers** — the **principal**
    commissural fibers, connecting **homologous** (mirror-image)
    areas of the two hemispheres — the **prefrontal-prefrontal**,
    **motor-motor**, **somatosensory-somatosensory**,
    **parietal-parietal**, **temporal-temporal**, and
    **occipital-occipital** connections. These are the **defining
    fiber group** of the corpus callosum.

*   **Heterotopic commissural fibers** — the **minority**
    commissural fibers, connecting **non-homologous** areas of the
    two hemispheres — the **prefrontal-motor**,
    **parietal-occipital**, and other **cross-modal** connections.

*   **Callosal radiations (prose)** — the **white-matter fibers**
    that **carry** the corpus callosum's commissural axons
    **through** the **centrum semiovale** (of each hemisphere) to
    reach the **neocortical cortex**. The **callosal radiations**
    are **prose** — the **corpus callosum itself** is the
    **midline** bundle; the **callosal radiations** are the
    **hemispheric** extensions that pass through the **centrum
    semiovale** (documented as **prose** in the **centrum
    semiovale** docstring).

**These fiber groups are prose, not structural children.** The
tree wires the **corpus callosum** as a **single leaf** under
``commissures/`` — the **homotopic** fibers, the **heterotopic**
fibers, and the **callosal radiations** are **prose**, not
structural children. Consumers that need **fiber-level**
resolution should consult the references, not the tree.

The Corpus Callosum / Anterior Commissure Boundary
--------------------------------------------------
This is the **most consequential sibling boundary** — the
**neocortical commissure vs. anterior-temporal / olfactory
commissure** boundary:

*   **Corpus_callosum** (this module) — the **neocortical
    commissure** — the **largest** commissure in the human brain,
    connecting the **neocortical** areas of the two hemispheres
    (prefrontal, premotor, motor, somatosensory, parietal,
    temporal, occipital).

*   **Anterior_commissure**
    (``.../commissures/anterior_commissure/``) — the
    **anterior-temporal / olfactory** commissure — the
    **second-largest** telencephalic commissure, connecting the
    **anterior temporal lobes** and the **olfactory structures**
    of the two hemispheres.

**They are SIBLINGS under the commissures container, and they are
DIFFERENT STRUCTURES** — the **corpus callosum** is the
**neocortical** commissure; the **anterior commissure** is the
**anterior-temporal / olfactory** commissure. **The two
commissures connect DIFFERENT cortical populations** — the corpus
callosum connects the **neocortex**; the anterior commissure
connects the **anterior temporal lobes** and the **olfactory
structures**. Consumers must **not** conflate the corpus callosum
with the anterior commissure.

The Corpus Callosum / Commissures Container Boundary
----------------------------------------------------
This is the **child vs. container** boundary:

*   **Corpus_callosum** (this module) — a **child** of the
    commissures container.

*   **Commissures** (``.../commissures/``) — the **container**
    that contains the **corpus callosum** and the **anterior
    commissure**.

**The corpus callosum is ONE of the two children of the commissures
container.** Consumers must **not** conflate the corpus callosum
with the commissures container.

The Corpus Callosum / Cerebral Hemispheres Boundary
---------------------------------------------------
This is the **commissural white matter vs. grey-matter +
ipsilateral-white-matter** sibling boundary:

*   **Corpus_callosum** (this module) — the **neocortical
    commissure** — a **commissural white-matter structure**.

*   **Cerebral_hemispheres**
    (``.../telencephalon/cerebral_hemispheres/``) — the **left
    hemisphere** and the **right hemisphere** — each containing
    the **cortex**, the **rhinencephalon**, the **subcortical**
    structures, the **white_matter**, and the
    **lateral_ventricles**.

**They are DIFFERENT COMPARTMENTS** — the **cerebral_hemispheres**
is the **grey-matter + ipsilateral-white-matter** compartment;
the **corpus callosum** is the **commissural white matter**.
Consumers must **not** conflate the corpus callosum with the
cerebral_hemispheres container.

The Corpus Callosum / Lateral Ventricles Boundary
-------------------------------------------------
This is the **commissural white matter vs. CSF-space** sibling
boundary — with a **shared midline proximity**:

*   **Corpus_callosum** (this module) — the **commissural white
    matter** — the **body** of the corpus callosum forms the
    **roof** of the **lateral ventricles' body**.

*   **Lateral_ventricles**
    (``.../telencephalon/lateral_ventricles/``) — the **CSF-filled
    spaces** inside the cerebral hemispheres.

**They are DIFFERENT COMPARTMENTS** — the **lateral_ventricles**
is the **CSF-space** compartment; the **corpus callosum** is the
**commissural white matter**. **The body of the corpus callosum
forms the roof of the lateral ventricles' body**, but it is
**not** the lateral ventricles. Consumers must **not** conflate
the corpus callosum with the lateral_ventricles container.

The Corpus Callosum / Ipsilateral White Matter Boundary
-------------------------------------------------------
This is the **commissural white matter vs. ipsilateral white
matter** boundary — with the **callosal-radiations clarification**:

*   **Corpus_callosum** (this module) — the **commissural white
    matter** — the neocortical commissural fibers that **cross
    the midline**.

*   **White_matter** (``.../left/white_matter/`` and
    ``.../right/white_matter/``) — the **ipsilateral white
    matter** of each cerebral hemisphere — the **centrum
    semiovale**, the **cingulum**, the **corona radiata**, the
    **external capsule**, the **extreme capsule**, the
    **fasciculus rectus**, the **fornix**, the **internal
    capsule**, the **mammillothalamic tract**, and the **medial
    forebrain bundle**.

**They are DIFFERENT COMPARTMENTS** — the **corpus callosum** is
the **commissural white matter**; the **white_matter** is the
**ipsilateral white matter**. **A note on the callosal
radiations:** the **callosal radiations** — the **white-matter
fibers** that carry the corpus callosum's commissural axons
**through** the **centrum semiovale** (of each hemisphere) to
reach the **neocortical cortex** — are **prose** in the
**centrum semiovale** docstring. The **corpus callosum itself**
is the **midline** bundle; the **callosal radiations** are the
**hemispheric** extensions that pass through the **centrum
semiovale** — but the **corpus callosum is not part of the
centrum semiovale**, and the **centrum semiovale is not the
corpus callosum**. Consumers must **not** conflate the corpus
callosum with any ipsilateral white-matter leaf, and must **not**
assume the corpus callosum is "part of" the centrum semiovale
just because the callosal radiations pass through it.

The Corpus Callosum / Fornix Boundary
-------------------------------------
This is the **commissural white matter vs. hippocampal output
tract** boundary — with a **shared midline proximity** (the body
of the fornix is **immediately below** the body of the corpus
callosum, with the **septum pellucidum** between them):

*   **Corpus_callosum** (this module) — the **commissural white
    matter** — the body of the corpus callosum is the **roof** of
    the **lateral ventricles' body**, above the **septum
    pellucidum**.

*   **Fornix** (``.../left/white_matter/fornix/`` and
    ``.../right/white_matter/fornix/``) — the **hippocampal output
    tract** — an **ipsilateral** white-matter leaf under each
    hemisphere's `white_matter/` container — the body of the
    fornix is the **floor** of the **lateral ventricles' body**,
    below the **septum pellucidum**.

**They are DIFFERENT STRUCTURES** — the **fornix** is an
**ipsilateral** white-matter leaf; the **corpus callosum** is a
**midline-crossing commissural** white-matter leaf. **The two are
in DIFFERENT containers** — the **fornix** is under
`white_matter/`; the **corpus callosum** is under `commissures/`.
**The septum pellucidum lies between them** — but the two are
**not** the same structure. Consumers must **not** conflate the
corpus callosum with the fornix.

The Corpus Callosum / Neocortical Areas Boundary
------------------------------------------------
This is the **white matter vs. grey matter** boundary — the
neocortical areas are the **grey-matter cortical targets** of the
corpus callosum:

*   **Corpus_callosum** (this module) — the **commissural
    white-matter bundle** — **connects** the **neocortical areas**
    of the two hemispheres.

*   **Neocortical areas**
    (``.../cerebral_hemispheres/left/cortex/`` and
    ``.../cerebral_hemispheres/right/cortex/``) — the **grey-matter
    cortex** of the **frontal**, **parietal**, **temporal**, and
    **occipital** lobes — the **principal cortical targets** of
    the corpus callosum.

**They are DIFFERENT STRUCTURES** — the **neocortical areas** are
**grey matter**; the **corpus callosum** is **white matter**.
Consumers must **not** conflate the corpus callosum with any
neocortical area.

The Corpus Callosum / Septum Pellucidum Boundary
------------------------------------------------
This is the **white matter vs. midline membrane** boundary — the
septum pellucidum is a **separate midline structure**, documented
here as **prose**:

*   **Corpus_callosum** (this module) — the **commissural
    white-matter bundle** — the body of the corpus callosum is
    **above** the septum pellucidum.

*   **Septum pellucidum** — a **thin midline membrane** (a
    **pia-arachnoid derivative**) that **separates** the
    **anterior horns** and **bodies** of the two **lateral
    ventricles** — it **lies between** the **body of the corpus
    callosum** (above) and the **fornix** (below).

**They are DIFFERENT STRUCTURES** — the **septum pellucidum** is a
**thin midline membrane** (documented here as **prose** — the tree
does **not** currently wire it); the **corpus callosum** is the
**commissural white-matter bundle**. Consumers must **not**
conflate the corpus callosum with the septum pellucidum.

The Corpus Callosum / SLEA Boundary
-----------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Corpus_callosum** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The corpus callosum is NOT part of the SLEA continuum.** It is
a **commissural white-matter bundle**, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
corpus callosum.

The Corpus Callosum / Telencephalon Boundary
--------------------------------------------
This is the **grandchild vs. container** boundary:

*   **Corpus_callosum** (this module) — a **grandchild** of the
    telencephalon container.

*   **Telencephalon** (``.../telencephalon/``) — the
    **container** that contains the **cerebral_hemispheres**, the
    **commissures**, and the **lateral_ventricles**.

**The corpus callosum is a grandchild of the telencephalon** (child
of the commissures container). Consumers must **not** conflate the
corpus callosum with the telencephalon container.

Function in the Human Brain
---------------------------
The corpus callosum's function is **neocortical interhemispheric
transfer** — **NOT a grey-matter function**:

*   **Neocortical Interhemispheric Transfer:** The **corpus
    callosum** carries the **neocortical commissural fibers** that
    **connect the two cerebral hemispheres** across the midline —
    the **neocortical interhemispheric transfer** substrate of the
    corpus callosum. This is the **anatomical substrate** of
    **cross-hemispheric integration** at the **neocortical**
    level — sensory, motor, cognitive, linguistic.

*   **Sensory Integration (Interhemispheric):** The **corpus
    callosum** integrates **sensory information** between the two
    hemispheres — visual, auditory, somatosensory — allowing the
    two hemispheres to form a **unified sensory percept**.

*   **Motor Coordination (Interhemispheric):** The **corpus
    callosum** coordinates **motor behavior** between the two
    hemispheres — bimanual coordination, intermanual transfer of
    motor skill.

*   **Cognitive and Linguistic Integration (Interhemispheric):**
    The **corpus callosum** integrates **cognitive and
    linguistic** information between the two hemispheres —
    allowing the **language-dominant** (usually left) hemisphere
    to share information with the **spatial-attention** (usually
    right) hemisphere. It is the **anatomical substrate** of
    **hemispheric specialization** and **integration**.

*   **NOT a neural processor in the classical sense.** The
    **corpus callosum** is a **commissural white-matter bundle**
    — it **conducts** the **neocortical commissural fibers**, but
    it does **not** **process** information (that happens in the
    **grey-matter structures** — the **neocortical areas** of the
    two hemispheres). The **fear-output** is the **central
    nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**.

**The unifying theme:** the corpus callosum is the **neocortical
commissure** of the **telencephalon** — the **largest** and
**most clinically consequential** commissure in the human brain,
and the **principal commissure** of the **neocortex**. It is
**SLEA-free**, **commissural white matter**, and **NOT a
grey-matter structure** — the **grey-matter structures** are the
**neocortical areas** of the two hemispheres whose fibers pass
through it.

Associated Disorders
--------------------
The corpus callosum is the **most clinically consequential**
commissure in this container — its clinical associations are
**extensive and well-documented**:

*   **Agenesis of the Corpus Callosum (ACC):** **Agenesis of the
    corpus callosum** — the **congenital absence** (complete or
    partial) of the corpus callosum — is the **most common**
    cerebral commissure malformation, and one of the **most
    common** congenital brain malformations overall. It is often
    **asymptomatic** or associated with **subtle cognitive and
    social** deficits, **epilepsy**, and **developmental delay**.
    The **corpus callosum** is the **white-matter substrate** of
    the **interhemispheric transfer** deficit in ACC.

*   **Split-Brain Syndrome (Callosotomy):** **Callosotomy** — the
    **surgical transection** of the **corpus callosum** (used
    historically for **intractable epilepsy**) — produces the
    **split-brain syndrome** — a **disconnection syndrome**
    characterized by **impaired interhemispheric transfer** of
    **sensory, motor, and cognitive** information. The
    **corpus callosum** is the **white-matter substrate** of the
    **split-brain** disconnection — the **classic** example of a
    **disconnection syndrome**.

*   **Marchiafava-Bignami Disease:** **Marchiafava-Bignami
    disease** — a **rare** disorder characterized by
    **demyelination and necrosis** of the **corpus callosum**
    (classically associated with **chronic alcoholism**) —
    produces **interhemispheric disconnection**, **cognitive
    impairment**, and **seizures**. The **corpus callosum** is
    the **white-matter substrate** of the disease.

*   **Multiple Sclerosis (Corpus Callosum Plaques — Dawson's
    Fingers):** The **corpus callosum** is a **principal site**
    of **MS plaques** — the **demyelinating lesions** that are the
    **radiological hallmark** of **multiple sclerosis**. The
    **corpus callosum** (especially the **callosal-septal
    interface**) is a **well-characterized** MS lesion site — the
    **Dawson's fingers** on sagittal MRI (the **perivenular**
    demyelinating lesions radiating from the **callosal-septal
    interface**). The **corpus callosum** is the **white-matter
    substrate** of the **MS lesion** pattern in the corpus
    callosum.

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

*   **Autism Spectrum Disorder (Atypical Callosal Connectivity —
    Contested):** The **corpus callosum** shows **atypical
    connectivity** in **autism spectrum disorder** — **reduced
    callosal volume** and **atypical callosal DTI** are reported.
    This is **contested** and is documented in the references.

*   **Glioblastoma and White-Matter Tumor Infiltration:** The
    **corpus callosum** is a **common site** of **glioblastoma**
    and other **white-matter tumors** — the **infiltrative**
    tumor cells **spread** along the commissural fibers of the
    corpus callosum (the **butterfly glioma** — a
    **glioblastoma** that **crosses the corpus callosum** to
    involve both hemispheres — is the **classic** example). The
    **corpus callosum** is the **white-matter substrate** of the
    **butterfly glioma**.

*   **No Named "Corpus Callosum Syndrome":** The **corpus
    callosum** is a **commissural white-matter bundle**, not a
    **single functional system** — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** as an
    **interhemispheric transfer** target (ACC, split-brain,
    Marchiafava-Bignami, MS, Alexander disease, butterfly
    glioma), and **contested** for **schizophrenia** and
    **autism**.

**What is NOT here:** The **corpus callosum** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** as an **interhemispheric transfer** target, and
**contested** for **schizophrenia** and **autism**.

Lateralization Notes
--------------------
This is the **single midline** corpus_callosum module. The
**corpus callosum** is a **midline structure** — and it carries
**NO warning**:

*   **Midline Structure — NOT a Paired Structure:** The **corpus
    callosum** is a **single midline bundle** — it is **NOT**
    duplicated into `left/corpus_callosum/` and
    `right/corpus_callosum/`. The **corpus callosum** is a
    **single midline bundle** whose fibers **cross the midline**
    to connect the **neocortical areas** of the two hemispheres.
    There is **no left/right split** of the corpus callosum
    itself.

*   **Bidirectional Interhemispheric Connections:** The **corpus
    callosum** carries **bidirectional** fibers between the two
    hemispheres — **homotopic** (mirror-image) and **heterotopic**
    (non-mirror-image) commissural fibers.

*   **NO Functional Lateralization of the Corpus Callosum per se:**
    The **functional lateralization** belongs to the **cortical
    grey-matter structures** whose fibers pass through the corpus
    callosum (e.g., the **left-hemisphere language areas**,
    the **right-hemisphere spatial-attention areas**) — **not** to
    the corpus callosum itself. Consumers must **not** assume the
    corpus callosum carries a **functional lateralization** of its
    own.

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    corpus_callosum is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the corpus callosum.

*   **NO Amygdala-Lateralization Warning of their own (the corpus
    callosum is a COMMISSURAL WHITE-MATTER BUNDLE, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **corpus callosum** is a
    **commissural white-matter bundle** — consumers must **not**
    conflate it with the **whole amygdala** or with the **central
    nucleus**.

**A consumer that assumes the corpus callosum is a paired
left/right structure will be structurally INCORRECT** — the
**corpus callosum** is a **single midline bundle**, not a paired
structure. The **corpus callosum** is a **strict midline leaf**
with **NO left/right split**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** The **corpus callosum** is a
    **midline structure** — it is **not** a left or right
    structure, so the "no cross-hemisphere imports" rule is
    **satisfied by construction**: the leaf does not belong to
    either hemisphere.
*   **No cross-lobe imports.** This module does **not** import from
    the **anterior commissure**
    (``.../commissures/anterior_commissure/``),
    ``.../telencephalon/cerebral_hemispheres/``,
    ``.../telencephalon/lateral_ventricles/``,
    ``.../left/white_matter/``, ``.../right/white_matter/``,
    ``.../left/cortex/``, ``.../right/cortex/``,
    ``.../left/subcortical/medial_temporal_lobe/hippocampus/
    subiculum/``, or
    ``.../right/subcortical/medial_temporal_lobe/hippocampus/
    subiculum/``. The **corpus callosum**'s relationships to the
    anterior commissure, the commissures container, the cerebral
    hemispheres, the lateral ventricles, the ipsilateral white
    matter (especially the **centrum semiovale**), the fornix, the
    neocortical areas, the septum pellucidum, and the telencephalon
    are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **rostrum**,
    **genu**, **body**, **isthmus**, and **splenium** of the corpus
    callosum are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    segment-level detail through the references.
*   **WHITE MATTER — NOT a grey-matter structure.** The **corpus
    callosum** is **white matter**; the **neocortical areas** are
    **grey matter**. Consumers must **not** conflate the corpus
    callosum with any grey-matter structure.
*   **COMMISSURAL WHITE MATTER — NOT the ipsilateral white
    matter.** The **corpus callosum** is the **commissural
    (midline-crossing)** white matter; the **white_matter** under
    each hemisphere is the **ipsilateral** white matter.
    Consumers must **not** conflate the two, and must **not**
    assume the corpus callosum is "part of" the **centrum
    semiovale** just because the **callosal radiations** pass
    through it.
*   **NEOCORTICAL COMMISSURE — the LARGEST and MOST CLINICALLY
    CONSEQUENTIAL commissure in the human brain.** Consumers must
    **not** treat the corpus callosum as "just another commissure"
    — it is the **neocortical** commissure, the **principal**
    interhemispheric pathway at the **neocortical** level.
*   **NOT the anterior commissure — the anterior commissure is a
    SIBLING commissural leaf.** The **two commissures connect
    DIFFERENT cortical populations** — the corpus callosum
    connects the **neocortex**; the anterior commissure connects
    the **anterior temporal lobes** and the **olfactory
    structures**.
*   **NOT the commissures container — the corpus callosum is a
    CHILD of the commissures.**
*   **NOT the cerebral_hemispheres container — the
    cerebral_hemispheres is the GREY-MATTER + IPSILATERAL-WHITE-
    MATTER sibling.**
*   **NOT the lateral_ventricles container — the
    lateral_ventricles is the CSF-space sibling.** The **body**
    of the corpus callosum forms the **roof** of the lateral
    ventricles' body.
*   **NOT the telencephalon container — the corpus callosum is a
    GRANDCHILD of the telencephalon.**
*   **NOT the fornix — the fornix is an IPSILATERAL white-matter
    leaf under each hemisphere's `white_matter/` container.** The
    two are in **DIFFERENT containers**. The **septum pellucidum**
    is **between** the body of the corpus callosum (above) and
    the body of the fornix (below).
*   **NOT the neocortical areas — those are GREY-MATTER structures
    the corpus callosum connects.**
*   **NOT the septum pellucidum — the septum pellucidum is a thin
    midline membrane, documented here as prose.** The tree does
    **not** currently wire it.
*   **SLEA-FREE — no extended-amygdala relationship.** The corpus
    callosum is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning) are **amygdala** children; the
    **corpus callosum** is a **commissural white-matter bundle**.
*   **MIDLINE STRUCTURE — NOT a left/right paired structure.**
    There is **no** `left/corpus_callosum/` and **no**
    `right/corpus_callosum/`. Consumers must **not** look for
    those paths — they **do not exist**.
*   **NOT a single uniform commissure — MULTIPLE topographic
    segments.** The **rostrum**, **genu**, **body**, **isthmus**,
    and **splenium** are **prose**, not structural children.
*   **No ``AREA_PATHS`` hop.** The **corpus callosum** is a local
    leaf under ``commissures/``, not a cross-listed leaf.
*   **No nested cross-listing.** The **corpus callosum** has no
    nested dual-framing module. It is a single leaf.
*   **NO left/right mirror — MIDLINE leaf with NO warning.** The
    **corpus callosum** is a **single midline leaf** — there is
    **no** `left/corpus_callosum/` and **no**
    `right/corpus_callosum/`. The **leaf itself** is **strictly
    hemisphere-neutral**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.commissures import corpus_callosum

Or by fully-qualified path string::

    path = (
        "telencephalon.commissures.corpus_callosum"
    )

**Do not** assume the corpus callosum is the **anterior
commissure**. The **anterior commissure** is the **sibling**
commissural leaf — the **anterior-temporal / olfactory**
commissure. The **corpus callosum** is the **neocortical**
commissure. **The two commissures connect different cortical
populations.**

**Do not** assume the corpus callosum is the **commissures
container**. The **commissures** is the **container** — the
**corpus callosum** is **one** of its two children.

**Do not** assume the corpus callosum is the **cerebral
hemispheres container** or the **lateral ventricles container**.
Those are the **sibling** compartments under the telencephalon.

**Do not** assume the corpus callosum is the **fornix**. The
**fornix** is an **ipsilateral white-matter leaf** under each
hemisphere's `white_matter/` container — the two are in
**different containers**. The **septum pellucidum** is **between**
the body of the corpus callosum (above) and the body of the
fornix (below).

**Do not** assume the corpus callosum is the **neocortical areas**.
Those are the **grey-matter structures** the corpus callosum
**connects**.

**Do not** assume the corpus callosum is the **septum pellucidum**.
The **septum pellucidum** is a **thin midline membrane** — the
**body of the corpus callosum** is **above** it, and the **body of
the fornix** is **below** it.

**Do not** assume the corpus callosum is a **left/right paired
structure**. The **corpus callosum** is a **single midline
bundle** — there is **no** `left/corpus_callosum/` and **no**
`right/corpus_callosum/`.

**Do not** assume the corpus callosum is the **telencephalon
container**. The **telencephalon** container contains the
**cerebral_hemispheres**, the **commissures**, and the
**lateral_ventricles** — and the **commissures** in turn
contains the **corpus callosum** and the **anterior commissure**.

**Do not** assume the corpus callosum is the **ipsilateral white
matter** of the cerebral hemispheres. The **ipsilateral white
matter** is wired under ``.../left/white_matter/`` and
``.../right/white_matter/``; the **corpus callosum** is the
**commissural (midline-crossing)** white matter. **Do not** assume
the corpus callosum is "part of" the **centrum semiovale** just
because the **callosal radiations** pass through it — the **callosal
radiations** are prose in the **centrum semiovale** docstring, but
the **corpus callosum itself** is a **separate structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the corpus callosum.
**The corpus callosum is SLEA-FREE** — it is **not** an
extended-amygdala component, and it is **NOT the fear-output
structure**.

Iterating the corpus callosum's (empty) children (recommended
consumer pattern)::

    CORPUS_CALLOSUM_CHILDREN = ()
    # The corpus callosum is a leaf. The rostrum, genu, body,
    # isthmus, and splenium are prose, not modules.

Reaching the anterior commissure sibling (recommended consumer
pattern — the anterior-temporal / olfactory commissure)::

    # The anterior commissure is the ANTERIOR-TEMPORAL / OLFACTORY
    # COMMISSURE — the SIBLING of the corpus callosum under the
    # commissures container:
    #
    #   telencephalon.commissures.anterior_commissure
    #
    # The anterior commissure is the anterior-temporal / olfactory
    # commissure; the corpus callosum is the neocortical commissure.
    # The two commissures connect DIFFERENT cortical populations.

Reaching the commissures container (recommended consumer pattern —
the container)::

    # The commissures is the CONTAINER that contains the corpus
    # callosum and the anterior commissure:
    #
    #   telencephalon.commissures
    #
    # The corpus callosum is ONE of the two children of the
    # commissures container.

Reaching the cerebral hemispheres (recommended consumer pattern —
the grey-matter + ipsilateral-white-matter sibling)::

    # The cerebral_hemispheres is the GREY-MATTER +
    # IPSILATERAL-WHITE-MATTER sibling under the telencephalon:
    #
    #   telencephalon.cerebral_hemispheres
    #
    # The cerebral_hemispheres is the grey-matter + ipsilateral-
    # white-matter compartment; the corpus callosum is the
    # commissural white matter.

Reaching the lateral ventricles (recommended consumer pattern — the
CSF-space sibling)::

    # The lateral_ventricles is the CSF-SPACE sibling under the
    # telencephalon:
    #
    #   telencephalon.lateral_ventricles
    #
    # The lateral_ventricles is the CSF-space compartment; the
    # corpus callosum is the commissural white matter. The body of
    # the corpus callosum forms the roof of the lateral ventricles'
    # body.

Reaching the fornix (recommended consumer pattern — the ipsilateral
hippocampal output tract)::

    # The fornix is the HIPPOCAMPAL OUTPUT TRACT — an IPSILATERAL
    # white-matter leaf under each hemisphere's white_matter
    # container:
    #
    #   cerebral_hemispheres.left.white_matter.fornix
    #   cerebral_hemispheres.right.white_matter.fornix
    #
    # The fornix is an ipsilateral white-matter leaf; the corpus
    # callosum is a midline-crossing commissural leaf. The two are
    # in DIFFERENT containers. The septum pellucidum is between the
    # body of the corpus callosum (above) and the body of the
    # fornix (below).

Reaching the neocortical areas (recommended consumer pattern — the
principal cortical targets)::

    # The neocortical areas are the GREY-MATTER CORTICAL TARGETS of
    # the corpus callosum:
    #
    #   cerebral_hemispheres.left.cortex
    #   cerebral_hemispheres.right.cortex
    #
    # The neocortical areas are grey matter; the corpus callosum is
    # white matter — the neocortical commissural projection that
    # connects them.

Reaching the centrum semiovale (recommended consumer pattern — the
ipsilateral white-matter leaf through which the callosal radiations
pass)::

    # The centrum semiovale is the WHITE-MATTER MASS ABOVE THE
    # LATERAL VENTRICLES — an IPSILATERAL white-matter leaf under
    # each hemisphere's white_matter container:
    #
    #   cerebral_hemispheres.left.white_matter.centrum_semiovale
    #   cerebral_hemispheres.right.white_matter.centrum_semiovale
    #
    # The callosal radiations — the white-matter fibers that carry
    # the corpus callosum's commissural axons through the centrum
    # semiovale to reach the neocortical cortex — are PROSE in the
    # centrum semiovale docstring. The corpus callosum itself is a
    # SEPARATE structure under the commissures container; it is NOT
    # "part of" the centrum semiovale.

Reaching the telencephalon (recommended consumer pattern — the
container)::

    # The telencephalon is the CONTAINER that contains the
    # cerebral_hemispheres, the commissures, and the
    # lateral_ventricles:
    #
    #   telencephalon
    #
    # The corpus callosum is a GRANDCHILD of the telencephalon
    # (child of the commissures).

Reaching the SLEA components (recommended consumer pattern — NOTE
the corpus callosum is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the corpus
    # callosum:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The corpus callosum is SLEA-FREE.

Topographic segment-level detail (not wired — consult references)::

    # The corpus callosum's topographic segments are prose, not
    # modules:
    #   rostrum       -> anterior-most; thin; curves inferiorly from
    #                    the genu toward the lamina terminalis; connects
    #                    the inferior frontal and orbitofrontal areas
    #   genu          -> anterior bend ("knee"); thickest anteriorly;
    #                    curves from the rostrum into the body; connects
    #                    the prefrontal and premotor areas
    #   body (truncus)-> middle part; roof of the lateral ventricles'
    #                    body; connects the primary motor, primary
    #                    somatosensory, and parietal association areas
    #   isthmus       -> narrow transition between the body and the
    #                    splenium; connects the superior temporal and
    #                    posterior parietal areas
    #   splenium      -> posterior-most; thickest posteriorly; connects
    #                    the occipital and posterior temporal areas
    #
    # Do not attempt to resolve these as sub-paths of the corpus
    # callosum.

Midline (no bilateral iteration — recommended consumer pattern)::

    # The corpus callosum is a SINGLE MIDLINE STRUCTURE — there is
    # NO left/right split. Do NOT iterate over ("left", "right") for
    # the corpus callosum itself.
    #
    # The corpus callosum CROSSES the midline; its fibers are
    # bidirectional between the two hemispheres.

References
----------
*   **Canonical corpus callosum anatomy:** Pandya, D.N., Seltzer,
    B. (1986). "The topography of commissural fibers." In:
    Lepore, F., Ptito, M., Jasper, H.H. (eds.), *Two Hemispheres
    — One Brain: Functions of the Corpus Callosum*. Alan R. Liss,
    New York, pp. 47–73. (Definitive corpus callosum topography —
    the neocortical commissural fibers; the topographic segments
    rostrum, genu, body, splenium.)
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
*   **Commissural anatomy (review):** Raybaud, C. (2010). "The
    corpus callosum: an MR imaging analysis of the anatomical
    variability and congenital anomalies." *American Journal of
    Neuroradiology* 31:1147–1155. (Commissural anatomy — corpus
    callosum and anterior commissure.)
*   **Commissural development:** Raybaud, C., Girard, N. (2008).
    "The developmental disorders of the corpus callosum."
    *Child's Nervous System* 24:1159–1170. (Commissural
    development — corpus callosum and anterior commissure.)
*   **White-matter atlas (human):** Wakana, S., Jiang, H., Nagae,
    L.M., van Zijl, P.C.M., Mori, S. (2004). "White matter atlas
    of the human brain: a diffusion tensor imaging study."
    *Radiology* 230:77–87. (Definitive white-matter tract
    anatomy; the corpus callosum in DTI.)
*   **DTI tractography atlas:** Catani, M., Thiebaut de Schotten,
    M. (2008). "A diffusion tensor imaging tractography atlas for
    virtual in vivo dissections." *Cortex* 44:1105–1132. (The
    corpus callosum in DTI tractography.)
*   **Commissures in the human connectome:** Catani, M., Thiebaut
    de Schotten, M. (2012). *Atlas of Human Brain Connections*.
    Oxford University Press, Oxford. (The corpus callosum in the
    human connectome.)
*   **Fiber pathways (review):** Schmahmann, J.D., Pandya, D.N.
    (2006). *Fiber Pathways of the Brain*. Oxford University
    Press, New York. (Definitive white-matter anatomy; the corpus
    callosum as the neocortical commissure.)
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
*   **Multiple sclerosis and the corpus callosum (Dawson's
    fingers):** Polman, C.H., et al. (2011). "Diagnostic criteria
    for multiple sclerosis: 2010 revisions to the McDonald
    criteria." *Annals of Neurology* 69:292–302. (MS plaques in
    the corpus callosum — the Dawson's fingers on sagittal MRI.)
*   **Alexander disease and the corpus callosum:** van der Knaap,
    M.S., Naidu, S., Breiter, S.N., Blaser, S., Stroink, H.,
    Powers, J.M. (2001). "Alexander disease: diagnosis with MR
    imaging." *American Journal of Neuroradiology* 22:541–552.
    (Alexander disease — corpus callosum predilection.)
*   **Butterfly glioma:** Dziurzynski, K., Blas-Boria, D., Suki,
    D., Cahill, D.P., Prabhu, S.S., Puduvalli, V.K., Levine, N.B.
    (2015). "Butterfly gliomas: a systematic review." *Journal of
    Neuro-Oncology* 124:333–339. (Butterfly glioma — glioblastoma
    crossing the corpus callosum.)
*   **Schizophrenia and the corpus callosum (contested):**
    Walterfang, M., et al. (2009). "Corpus callosum size and
    shape in schizophrenia: a meta-analysis." *Schizophrenia
    Research* 110:1–9. (Corpus callosum abnormalities in
    schizophrenia — contested.)
*   **Autism and the corpus callosum (contested):** Frazier, T.W.,
    Hardan, A.Y. (2009). "A meta-analysis of the corpus callosum
    in autism." *Biological Psychiatry* 66:935–941. (Corpus
    callosum abnormalities in autism — contested.)
*   **H.M. and medial temporal lobe amnesia (contrast — the
    corpus callosum is not the amnesia substrate):** Scoville,
    W.B., Milner, B. (1957). "Loss of recent memory after
    bilateral hippocampal lesions." *Journal of Neurology,
    Neurosurgery, and Psychiatry* 20:11–21. (Bilateral
    hippocampal damage and anterograde amnesia — distinct from
    the corpus callosum.)
*   **Amygdala (contrast — the corpus callosum is NOT the
    amygdala):** LeDoux, J.E. (2000). "Emotion circuits in the
    brain." *Annual Review of Neuroscience* 23:155–184.
    (Amygdala fear circuit — distinct from the corpus callosum.)
*   **SLEA (contrast — the corpus callosum is not included):**
    Alheid, G.F., Heimer, L. (1988). "New perspectives in basal
    forebrain organization of special relevance for
    neuropsychiatric disorders." *Neuroscience* 27:1–39. (SLEA
    continuum — BNST, central nucleus, ventral pallidum, nucleus
    accumbens; NOT the corpus callosum.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Corpus callosum in overview.)
*   NeuroNames — Corpus callosum; FMA — Corpus callosum.
"""