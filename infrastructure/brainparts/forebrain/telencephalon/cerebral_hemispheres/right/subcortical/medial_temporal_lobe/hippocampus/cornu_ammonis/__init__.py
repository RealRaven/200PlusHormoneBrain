"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
======================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── medial_temporal_lobe
                    └── hippocampus
                        └── cornu_ammonis   <-- THIS MODULE (CONTAINER)

**Primary synonym:** Cornu ammonis (right); Ammon's horn; hippocampus
proper (in the narrow sense, together with the dentate gyrus); CA
fields; CA1–CA4.
**Cytoarchitectonic designation:** **Not a Brodmann area.** The
**archicortex** subfield system of the hippocampus — a **nested
container module** whose **structural children** are **``ca1``**,
**``ca2``**, **``ca3``**, and **``ca4``**. Together the CA fields
form the **principal-output** subfield system of the hippocampal
formation.
**Part of:** The **hippocampus** container — the **CA field system**
of the hippocampal formation. The **cornu ammonis** is the
**principal-output** subfield system of the hippocampus (CA1 →
subiculum).
**Structural parent:** ``.../hippocampus/`` → **direct child** of
the hippocampus container.
**Structural children:** **YES — this is a CONTAINER module, not a
leaf.** Its **four structural children** are:

*   ``.../cornu_ammonis/ca1/`` — a **leaf**. The **principal output**
    of the cornu ammonis (CA1 → subiculum) and a **principal site**
    of **place cells**.
*   ``.../cornu_ammonis/ca2/`` — a **leaf**. A **small,
    relatively resistant** subfield, enriched in **oxytocin
    receptors** and **social-memory** functions.
*   ``.../cornu_ammonis/ca3/`` — a **leaf**. The **recurrent-
    collateral** subfield and a **principal site** of **pattern
    completion** and **place cells**.
*   ``.../cornu_ammonis/ca4/`` — a **leaf**. The **polymorphic
    layer (hilus) of the dentate gyrus** in most anatomical usage
    — nested here under the cornu ammonis by the tree, documented
    as **prose** (see *CA4 / Dentate Hilus Note*).

Consumers **may** import these children; the cornu ammonis is the
**structural parent** of the CA fields, not a leaf.
**Boundary status (CONTAINER — NOT a leaf, NOT a single subfield):**
**Boundary case — the cornu_ammonis is a CONTAINER module with FOUR
structural children, not a leaf and not a single subfield.** The
**CA1**, **CA2**, **CA3**, and **CA4** subfields are **separate
structural children** — consumers must **not** assume the cornu
ammonis is a single subfield (e.g., "the cornu ammonis = CA1"), and
must **not** assume the CA fields are prose under a leaf. They are
**wired children** with their own modules.
**Boundary status (NOT the dentate gyrus — the dentate gyrus is the
INPUT subfield):** **Boundary case — the cornu_ammonis is NOT the
dentate gyrus; the dentate gyrus is the INPUT subfield.** The
**dentate_gyrus** (``.../hippocampus/dentate_gyrus/``) is the
**principal input** of the hippocampus (entorhinal cortex →
perforant path → dentate gyrus → mossy fibers → CA3) and the
**principal site** of **pattern separation** and **adult
neurogenesis**. The **cornu ammonis** (here) is the
**principal-output** subfield system (CA1 → subiculum) and the
**principal site** of **place cells** and **pattern completion**.
**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES** — the **dentate gyrus** is the **input**; the **cornu
ammonis** is the **output** side. Consumers must **not** conflate
the two.
**Boundary status (NOT the subiculum — the subiculum is the OUTPUT
TARGET of CA1):** **Boundary case — the cornu_ammonis is NOT the
subiculum; the subiculum is the OUTPUT TARGET of CA1.** The
**subiculum** (``.../hippocampus/subiculum/``) is the **principal
output** of the hippocampus to the parahippocampal region, the
mammillary bodies (via the fornix), and the prefrontal cortex —
**CA1 projects to the subiculum**. The **cornu ammonis** (here) is
the **CA field system** that **feeds** the subiculum. **They are
SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES** — the **cornu ammonis** is the **CA fields**; the
**subiculum** is the **output structure** they project to.
Consumers must **not** conflate the two.
**Boundary status (NOT the parasubiculum or presubiculum — those
are the subicular-complex head-direction subfields):** **Boundary
case — the cornu_ammonis is NOT the parasubiculum or the
presubiculum.** The **parasubiculum**
(``.../hippocampus/parasubiculum/``) and the **presubiculum**
(``.../hippocampus/presubiculum/``) are **siblings** of the cornu
ammonis under the hippocampus — the **head-direction** and
**spatial** subfields of the **subicular complex**. The **cornu
ammonis** (here) is the **CA field system**. **They are SIBLINGS
under the hippocampus, and they are DIFFERENT STRUCTURES.**
Consumers must **not** conflate the two.
**Boundary status (NOT the hippocampus container — the cornu
ammonis is a CHILD of the hippocampus):** **Boundary case — the
cornu_ammonis is a CHILD of the hippocampus container, not the
container itself.** The **hippocampus** container contains the
**cornu ammonis**, the **dentate gyrus**, the **parasubiculum**,
the **presubiculum**, and the **subiculum** — the **cornu ammonis**
is **one** of those five children. Consumers must **not** conflate
the cornu ammonis with the hippocampus container.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the cornu_ammonis
is NOT the parahippocampal region.** The **parahippocampal
region** (the **entorhinal cortex**, the **perirhinal cortex**,
and the **parahippocampal gyrus**) is **cortical** — it is wired
under ``.../right/cortex/temporal/gyri/`` and is **outside** the
hippocampus container. The **cornu ammonis** (here) is the
**archicortex**. **They are DIFFERENT STRUCTURES**: the
**parahippocampal region** is the **cortical interface** that
**feeds** the hippocampus; the **cornu ammonis** is the **CA
field system** that **receives** the parahippocampal input (via the
dentate gyrus). Consumers must **not** conflate the two.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the cornu_ammonis is
NOT the fornix or the white matter; the fornix and the white_matter
are WHITE-MATTER structures.** The **fornix**
(``.../right/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../right/white_matter/``) is the **white-matter
infrastructure**. The **cornu ammonis** (here) is the
**grey-matter archicortex**. **They are DIFFERENT STRUCTURES** —
the **cornu ammonis** is the **grey-matter CA fields**; the
**fornix** and the **white_matter** are the **white-matter
tracts**. Consumers must **not** conflate the two.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the cornu_ammonis is NOT the rhinencephalon.** The
**rhinencephalon** (``.../right/cortex/rhinencephalon/``) — the
olfactory bulb, olfactory tract, piriform cortex, periamygdaloid
cortex, anterior olfactory nucleus, and uncus — is the **cortical
olfactory lobe**. The **cornu ammonis** (here) is the **archicortex
of episodic memory and spatial navigation** — it is **not** an
olfactory structure. Consumers must **not** conflate the two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the
cornu_ammonis is NOT the amygdala; the amygdala is the
FEAR/EMOTION/SALIENCE container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), and
the **lateral nucleus** (sensory input). The **cornu ammonis**
(here) is a **CA field system** of the **memory** container. **They
are DIFFERENT STRUCTURES** — the **amygdala** is the **emotion**
container; the **cornu ammonis** is a **child of the memory**
container. Consumers must **not** conflate the two.
**Boundary status (SLEA-FREE — the cornu ammonis is NOT an
extended-amygdala component):** **Boundary case — the
cornu_ammonis is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala)
and to the **BNST**, **ventral pallidum**, and **nucleus accumbens**
(wired elsewhere). The **cornu ammonis** is an
**episodic/declarative-memory and spatial-navigation** structure —
it is **NOT** an extended-amygdala component, and it carries **NO
SLEA warning**. Consumers must **not** import the SLEA warning into
the cornu_ammonis — it is **SLEA-free**.
**Boundary status (NOT the memory software layer — the cornu
ammonis is the BRAIN STRUCTURE, not the ``memory/`` package):**
**Boundary case — the cornu_ammonis is the BRAIN STRUCTURE, NOT the
``memory/`` software package.** The **``memory/`` package**
(``memory/stores/`` — episodic, semantic, procedural, working;
``memory/backends/`` — chroma, in_memory) is the **software memory
layer** of the simulation. The **cornu ammonis** (here) is the
**brain structure** that **subserves** episodic memory. **They are
DIFFERENT LAYERS** — the **``memory/`` package** is the **software
store**; the **cornu ammonis** is the **brain region** whose
function the store models. Consumers must **not** conflate the
two.
**Boundary status (CA4 is the DENTATE HILUS — within the cornu
ammonis container):** **Boundary case — CA4 is the polymorphic
layer (hilus) of the dentate gyrus in most anatomical usage, nested
here under the cornu ammonis by the tree.** The **``ca4``** child
is wired under **``.../cornu_ammonis/``** in the tree, and
consumers should **resolve it there** — but anatomically,
**CA4** is the **hilus (polymorphic layer) of the dentate gyrus**
(the layer that contains **mossy cells** and receives **mossy
fibers** from the dentate granule cells). The tree's placement of
``ca4`` under ``cornu_ammonis`` is honored structurally; the
**dentate-hilus** relationship is documented as **prose**. See
*CA4 / Dentate Hilus Note*.

Overview
--------
The cornu ammonis is the **CA field system** of the hippocampus —
the **archicortex** whose **structural children** are **CA1**,
**CA2**, **CA3**, and **CA4**, and which is the **principal-output**
subfield system of the hippocampal formation. It is a **nested
container** module under the hippocampus, the **sibling of the
dentate gyrus and the subicular complex**, and the **grey-matter
substrate** of **place cells**, **pattern completion**, **temporal
ordering**, and **episodic-memory output**.

**The cornu_ammonis is a CONTAINER, not a leaf.** Its **four
structural children** — ``ca1``, ``ca2``, ``ca3``, ``ca4`` — are
**wired modules**, not prose. Consumers may import them.

**The cornu_ammonis is NOT the dentate gyrus.** The **dentate
gyrus** is the **input** subfield (entorhinal cortex → perforant
path → dentate gyrus → mossy fibers → CA3). The **cornu ammonis**
is the **output** side. **They are SIBLINGS under the hippocampus,
and they are DIFFERENT STRUCTURES.**

**The cornu_ammonis is NOT the subiculum.** **CA1 projects to the
subiculum** — the **subiculum** is the **output target**. **They
are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.**

**The cornu_ammonis is NOT the hippocampus container.** The
**hippocampus** container contains the **cornu ammonis**, the
**dentate gyrus**, the **parasubiculum**, the **presubiculum**, and
the **subiculum** — the **cornu ammonis** is **one** of those five
children.

**The cornu_ammonis is NOT the parahippocampal region.** The
**entorhinal cortex**, **perirhinal cortex**, and **parahippocampal
gyrus** are **cortical** — they are wired under
``cortex/temporal/gyri/``. The **cornu ammonis** is the
**archicortex**.

**The cornu_ammonis is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**. The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The cornu_ammonis is the BRAIN STRUCTURE, not the ``memory/``
software package.** The **``memory/`` package** is the **software
memory layer**. The **cornu ammonis** is the **brain region** whose
function the episodic store models. **They are DIFFERENT LAYERS.**

**The cornu_ammonis is a paired structure.** Each hemisphere has
its own cornu ammonis, with **ipsilateral** and **bilateral**
connections to the dentate gyrus, the subiculum, the
parahippocampal region, and the contralateral cornu ammonis. The
two sides are **bilaterally symmetric** and **partially
lateralized** — the **left** cornu ammonis is more involved in
**verbal** episodic memory, and the **right** cornu ammonis is more
involved in **spatial/nonverbal** episodic memory. This is
**well-documented** (not contested), and documented in the
**medial temporal lobe module** (not at the cornu-ammonis level).
See *Lateralization Notes*.

Structural Children (wired — NOT prose)
---------------------------------------
This is a **container** module — its children are **wired
modules**, not prose:

*   ``.../cornu_ammonis/ca1/`` — **CA1** (Sommer sector). A
    **leaf**. The **principal output** of the cornu ammonis (CA1 →
    subiculum) and a **principal site** of **place cells**. CA1
    also projects directly to the **entorhinal cortex** and the
    **prefrontal cortex**. CA1 is the **most vulnerable** subfield
    to **ischemia**, **hypoxia**, **Alzheimer's pathology**, and
    **hippocampal sclerosis**.

*   ``.../cornu_ammonis/ca2/`` — **CA2**. A **leaf**. A **small,
    relatively resistant** subfield, enriched in **oxytocin
    receptors** and **social-memory** functions. CA2 projects to
    **CA1** and to the **entorhinal cortex**.

*   ``.../cornu_ammonis/ca3/`` — **CA3**. A **leaf**. The
    **recurrent-collateral** subfield — CA3 pyramidal cells
    project back onto each other, forming the **autoassociative
    network** that implements **pattern completion**. CA3
    receives the **mossy fibers** from the **dentate gyrus** and is
    a **principal site** of **place cells**. CA3 is **vulnerable**
    to **seizures** and to **excitotoxic damage**.

*   ``.../cornu_ammonis/ca4/`` — **CA4** (polymorphic layer / hilus
    of the dentate gyrus). A **leaf**. The **hilus** layer,
    containing **mossy cells**, that receives the **mossy fibers**
    from the **dentate granule cells**. See *CA4 / Dentate Hilus
    Note* — the tree nests ``ca4`` under ``cornu_ammonis``; most
    anatomical usage treats CA4 as the **dentate hilus**.

**These children are wired, not prose.** The tree wires them as
**structural children** of the cornu ammonis — they are **not**
prose under a leaf. Consumers that need **CA-field-level**
resolution should import them directly.

CA4 / Dentate Hilus Note
------------------------
**CA4** is the **polymorphic layer (hilus) of the dentate gyrus**
in most anatomical usage — the layer that contains **mossy cells**
and receives the **mossy fibers** from the **dentate granule
cells**. The **tree nests ``ca4`` under ``cornu_ammonis``**, and
consumers should **resolve it there** — the tree's placement is
honored structurally. The **dentate-hilus** relationship is
documented here as **prose**:

*   **CA4 is the hilus** — it is the **polymorphic layer** of the
    dentate gyrus, **not** a classical CA field in the same sense
    as CA1–CA3.
*   **CA4 contains mossy cells** — the **excitatory hilar
    neurons** that project to the **dentate granule cells** and to
    **CA3**.
*   **CA4 is the target of the mossy fibers** — the **dentate
    granule cells** project to the **CA3** and **CA4** (hilus)
    via the **mossy fibers**.
*   **Consumers that need the dentate-hilus framing** should
    consult the references — the tree places CA4 under the **cornu
    ammonis**, and consumers must **not** attempt to resolve it
    under ``.../dentate_gyrus/``.

The Cornu Ammonis / Dentate Gyrus Boundary
------------------------------------------
This is the **output vs. input** sibling boundary:

*   **Cornu_ammonis** (this module) — the **CA field system**
    (principal-output subfield system; CA1 → subiculum).

*   **Dentate_gyrus** (``.../hippocampus/dentate_gyrus/``) — the
    **input** subfield (entorhinal cortex → perforant path →
    dentate gyrus → mossy fibers → CA3).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES** — the **dentate gyrus** is the **input**; the **cornu
ammonis** is the **output** side. Consumers must **not** conflate
the two.

The Cornu Ammonis / Subiculum Boundary
--------------------------------------
This is the **CA fields vs. output-target** sibling boundary:

*   **Cornu_ammonis** (this module) — the **CA field system**.

*   **Subiculum** (``.../hippocampus/subiculum/``) — the
    **principal output** of the hippocampus; **CA1 projects to the
    subiculum**.

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES** — the **cornu ammonis** is the **CA fields**; the
**subiculum** is the **output structure** they project to.
Consumers must **not** conflate the two.

The Cornu Ammonis / Parasubiculum and Presubiculum Boundary
-----------------------------------------------------------
This is the **CA fields vs. subicular-complex** sibling boundary:

*   **Cornu_ammonis** (this module) — the **CA field system**.

*   **Parasubiculum** (``.../hippocampus/parasubiculum/``) and
    **presubiculum** (``.../hippocampus/presubiculum/``) — the
    **head-direction** and **spatial** subfields of the
    **subicular complex**.

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the two.

The Cornu Ammonis / Hippocampus Boundary
----------------------------------------
This is the **child vs. container** boundary:

*   **Cornu_ammonis** (this module) — a **child** of the
    hippocampus container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**The cornu ammonis is ONE of the five children of the
hippocampus.** Consumers must **not** conflate the cornu ammonis
with the hippocampus container.

The Cornu Ammonis / Parahippocampal Region Boundary
---------------------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **Cornu_ammonis** (this module) — the **CA field system**
    (archicortex).

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../right/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus** (via the dentate gyrus). The **cornu ammonis** is
the **archicortex** that **receives** the parahippocampal input
(via the dentate gyrus). Consumers must **not** conflate the
**cornu ammonis** with the **parahippocampal region** — the
parahippocampal region is **cortex/**; the cornu ammonis is
**subcortical/medial_temporal_lobe/**.

The Cornu Ammonis / Fornix and White Matter Boundary
----------------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **Cornu_ammonis** (this module) — the **grey-matter
    archicortex**.

*   **Fornix** (``.../right/white_matter/fornix/``) and
    **white_matter** (``.../right/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — the **cornu ammonis** is the
**grey-matter CA fields**; the **fornix** and the **white_matter**
are the **white-matter tracts**. Consumers must **not** conflate
the two.

The Cornu Ammonis / Rhinencephalon Boundary
-------------------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **Cornu_ammonis** (this module) — the **archicortex of episodic
    memory and spatial navigation**.

*   **Rhinencephalon** (``.../right/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — the **cornu ammonis** is the
**memory archicortex**; the **rhinencephalon** is the **olfactory
lobe**. Consumers must **not** conflate the two.

The Cornu Ammonis / Amygdala Boundary
-------------------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **Cornu_ammonis** (this module) — a **CA field system** of the
    **memory** container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; the **cornu ammonis** is a **child of the
memory** container. Consumers must **not** conflate the two.

The Cornu Ammonis / Memory Software Layer Boundary
--------------------------------------------------
This is the **brain structure vs. software store** boundary:

*   **Cornu_ammonis** (this module) — the **brain structure**
    (CA fields) that subserves episodic memory.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — the **cornu ammonis** is the
**brain region**; the **``memory/`` package** is the **software
store**. Consumers must **not** conflate the two.

The Cornu Ammonis / SLEA Boundary
---------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Cornu_ammonis** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The cornu ammonis is NOT part of the SLEA continuum.** It is an
**episodic/declarative-memory and spatial-navigation** structure,
and it carries **no SLEA warning**. Consumers must **not** import
the SLEA warning into the cornu ammonis.

Function in the Human Brain
---------------------------
The cornu ammonis's functions are **episodic-memory output**,
**place-cell spatial coding**, **pattern completion**, and
**temporal ordering** — **NOT fear-output**:

*   **Principal Output (CA1 → Subiculum):** The **CA1** subfield is
    the **principal output** of the cornu ammonis — it projects to
    the **subiculum**, to the **entorhinal cortex**, and to the
    **prefrontal cortex**. This is the **output gate** of the
    hippocampal formation.

*   **Place-Cell Spatial Coding (CA1 and CA3):** The **CA1** and
    **CA3** subfields are **principal sites** of **place cells** —
    the **spatial** neurons that fire when the animal is in a
    **specific location** in the environment. This is the
    **substrate** of the **cognitive map**.

*   **Pattern Completion (CA3):** The **CA3** subfield is the
    **principal site** of **pattern completion** — the
    **reconstruction** of a **full memory** from a **partial cue**,
    implemented by the **recurrent collateral** network. This is
    the **substrate** of the **recall** of a full episode from a
    partial reminder.

*   **Temporal Ordering (CA1):** The **CA1** subfield is involved in
    **temporal ordering** — the **encoding** of the **order** of
    events in a **sequence**. This is the **substrate** of the
    **temporal structure** of episodic memory.

*   **Social Memory (CA2 — contested):** The **CA2** subfield is
    **enriched in oxytocin receptors** and is implicated in
    **social memory** — the **recognition** of **conspecifics**.
    This is **contested** and is documented in the references.

*   **NOT a neural processor in the classical sense.** The
    **cornu ammonis** is a **memory and navigation** structure — it
    **encodes**, **completes**, and **outputs** the **episodic and
    spatial** representations, but it does **not** produce the
    **fear-output** or the **autonomic and behavioral** fear
    responses. The **fear-output** is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** the cornu ammonis is the **CA field
system** of the **hippocampus** — the **principal-output** subfield
system that anchors **place cells, pattern completion, temporal
ordering, and episodic-memory output**. It is **SLEA-free**,
**memory/navigation**, and **NOT the fear-output structure** — the
**fear-output** is the **central nucleus**, the **fear-learning**
structures are the **basolateral nuclei**, and the **cornu
ammonis** is the **CA field system** of the **memory** container.

Associated Disorders
--------------------
The cornu ammonis has **no named "cornu ammonis syndrome"** in the
narrow sense, but its clinical associations are **well-documented**:

*   **Alzheimer's Disease (Early CA1 Pathology):** The **CA1**
    subfield is the **earliest** affected **CA field** in
    **Alzheimer's disease** — **CA1** shows the **first
    neurofibrillary tangles**, and **CA1 atrophy** is a **core
    biomarker** of the disease. The **cornu ammonis** is the
    **memory substrate** of the disease; its involvement is
    **direct**.

*   **Temporal Lobe Epilepsy (Hippocampal Sclerosis / Ammon's Horn
    Sclerosis):** The **CA1** and **CA3** subfields are the
    **principal sites** of **hippocampal sclerosis** (Ammon's horn
    sclerosis) in **temporal lobe epilepsy** — **CA1** and **CA3**
    are the **most vulnerable** CA fields to **excitotoxic
    damage**. The **cornu ammonis** is the **epileptogenic
    substrate** of temporal lobe epilepsy.

*   **Anterograde Amnesia (Medial Temporal Lobe Amnesia — via the
    Hippocampus):** Bilateral **hippocampal** damage (e.g., patient
    **H.M.**) — including **CA1** — produces **anterograde
    amnesia** — the **inability** to form **new episodic
    memories**, with **preserved** short-term memory and
    **preserved** procedural memory. The **cornu ammonis** is the
    **memory substrate** of this amnesia.

*   **Schizophrenia (CA2 / Hippocampal Dysfunction — Contested):**
    The **CA2** subfield and the **cornu ammonis** more broadly
    show **atypical** findings in **schizophrenia** — **CA2**
    pathology and **hippocampal hyperactivity** are reported. This
    is **contested** and is documented in the references.

*   **No Named "Cornu Ammonis Syndrome":** The cornu ammonis is a
    **CA field system**, not a **single functional system** — it
    has **no named clinical syndrome**. Its clinical relevance is
    **direct** for **memory and navigation** (Alzheimer's,
    hippocampal sclerosis, amnesia), and **contested** for
    **schizophrenia**.

**What is NOT here:** The cornu ammonis is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** for **memory and navigation** (Alzheimer's,
hippocampal sclerosis, amnesia).

Lateralization Notes
--------------------
This is the **right** cornu_ammonis module. The cornu ammonis is
**bilaterally symmetric** and **partially lateralized** — and it
carries **NO warning**:

*   **Bilateral CA Field Function:** Each hemisphere has its own
    cornu ammonis, with **ipsilateral** and **bilateral**
    connections to the dentate gyrus, the subiculum, the
    parahippocampal region, and the contralateral cornu ammonis.
    The two sides are **functionally symmetric** for **basic
    memory and navigation**.

*   **Partial Lateralization (Well-Documented — Verbal vs.
    Spatial):** The **left** cornu ammonis is **more involved in
    verbal** episodic memory (word lists, stories, verbal
    recognition); the **right** cornu ammonis is **more involved in
    spatial/nonverbal** episodic memory (spatial layouts, faces,
    nonverbal recognition). This is **well-documented**, **not
    contested**, and is documented in the **medial temporal lobe
    module** (not at the cornu-ammonis level).

*   **NO Extended-Amygdala Warning (SLEA-free module):** The
    cornu_ammonis is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the cornu_ammonis.

*   **NO Amygdala-Lateralization Warning of their own (the cornu
    ammonis is the MEMORY subfield, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output)
    and the **basolateral nuclei** (fear-learning). The cornu
    ammonis is a **memory subfield** — consumers must **not**
    conflate it with the **whole amygdala** or with the **central
    nucleus**. The **cornu_ammonis** is the **memory** subfield,
    not the **fear circuit**.

**A consumer that assumes "left cornu_ammonis = right
cornu_ammonis" will be structurally correct** — the two sides are
**symmetric** and **partially lateralized** (the lateralization is
documented in the medial temporal lobe module). The cornu_ammonis
is a **strict-mirror pair with NO warning** — **no SLEA warning**,
**no amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../hippocampus/dentate_gyrus/``,
    ``.../hippocampus/subiculum/``,
    ``.../hippocampus/parasubiculum/``,
    ``.../hippocampus/presubiculum/``,
    ``.../medial_temporal_lobe/amygdala/``,
    ``.../right/cortex/temporal/gyri/entorhinal_cortex/``,
    ``.../right/cortex/temporal/gyri/perirhinal_cortex/``,
    ``.../right/cortex/temporal/gyri/parahippocampal_gyrus/``,
    ``.../right/white_matter/fornix/``,
    ``.../right/cortex/rhinencephalon/``, ``memory/``, or any other
    container. The cornu_ammonis's relationships to the dentate
    gyrus, the subiculum, the parasubiculum, the presubiculum, the
    amygdala, the parahippocampal region, the fornix, the
    rhinencephalon, and the ``memory/`` package are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **CONTAINER module — children EXIST.** The **four structural
    children** — ``ca1``, ``ca2``, ``ca3``, ``ca4`` — are **wired
    modules**, not prose. Consumers **may** import them. The cornu
    ammonis is **not** a leaf.
*   **NOT a leaf — do not claim leaf status.** The cornu ammonis
    has **four structural children**; consumers must **not** assume
    it is a leaf and must **not** assume the CA fields are prose.
*   **NOT a single subfield.** The cornu ammonis is **not** "CA1"
    or "CA3" — it is the **container** of all four CA fields.
*   **NOT the dentate gyrus — the dentate gyrus is the INPUT
    subfield.** Consumers must **not** conflate the cornu ammonis
    with the dentate gyrus.
*   **NOT the subiculum — the subiculum is the OUTPUT TARGET of
    CA1.** Consumers must **not** conflate the cornu ammonis with
    the subiculum.
*   **NOT the parasubiculum or presubiculum — those are the
    subicular-complex head-direction subfields.**
*   **NOT the hippocampus container — the cornu ammonis is a CHILD
    of the hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; the cornu ammonis is the
    **archicortex**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** The cornu ammonis is the **grey-matter CA
    fields**.
*   **NOT the rhinencephalon.** The cornu ammonis is **not** an
    olfactory structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    cornu_ammonis is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; the **cornu ammonis** is
    the **brain structure**. Consumers must **not** conflate the
    two.
*   **CA4 is the DENTATE HILUS — within the cornu ammonis
    container.** The **``ca4``** child is wired under
    ``.../cornu_ammonis/``; the **dentate-hilus** relationship is
    documented as **prose**. Consumers must **not** attempt to
    resolve CA4 under ``.../dentate_gyrus/``.
*   **No ``AREA_PATHS`` hop.** The cornu_ammonis is a local
    container under the hippocampus, not a cross-listed structure.
*   **No nested cross-listing.** The cornu_ammonis has no nested
    dual-framing module. It is a single container.
*   **Structural parity with left cornu_ammonis — strict mirror
    with NO warning.** Left and right cornu ammonis modules are
    **structurally identical** — same **container** status, same
    **four structural children**, same **CA-field** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.hippocampus import cornu_ammonis

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "medial_temporal_lobe.hippocampus.cornu_ammonis"
    )

**Do not** assume the cornu_ammonis is a **leaf**. It has **four
structural children** — ``ca1``, ``ca2``, ``ca3``, ``ca4``.

**Do not** assume the cornu_ammonis is the **dentate gyrus**. The
**dentate gyrus** is the **input** subfield; the **cornu ammonis**
is the **output** side. They are **siblings**.

**Do not** assume the cornu_ammonis is the **subiculum**. **CA1
projects to the subiculum** — the subiculum is the **output
target**. They are **siblings**.

**Do not** assume the cornu_ammonis is the **parasubiculum** or the
**presubiculum**. Those are the **subicular-complex
head-direction** subfields. They are **siblings**.

**Do not** assume the cornu_ammonis is the **hippocampus
container**. The **hippocampus** container contains the **cornu
ammonis** and the other four subfields — the **cornu ammonis** is
**one** of those five children.

**Do not** assume the cornu_ammonis is the **parahippocampal
region**. The **entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; the **cornu
ammonis** is the **archicortex**.

**Do not** assume the cornu_ammonis is the **fornix** or the
**white_matter**. Those are **white-matter tracts**; the **cornu
ammonis** is the **grey-matter CA fields**.

**Do not** assume the cornu_ammonis is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; the **cornu
ammonis** is the **memory archicortex**.

**Do not** assume the cornu_ammonis is the **``memory/`` software
package**. The **``memory/`` package** is the **software store**;
the **cornu ammonis** is the **brain structure**.

**Do not** resolve **CA4** under ``.../dentate_gyrus/``. **CA4** is
wired under ``.../cornu_ammonis/`` in the tree; the **dentate
hilus** relationship is **prose**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the cornu_ammonis. **The
cornu_ammonis is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

Iterating the cornu_ammonis's structural children (recommended
consumer pattern — NOTE these are WIRED, not prose)::

    CORNU_AMMONIS_CHILDREN = (
        "ca1",   # leaf
        "ca2",   # leaf
        "ca3",   # leaf
        "ca4",   # leaf (dentate hilus — see CA4 / Dentate Hilus Note)
    )

Reaching the dentate gyrus (recommended consumer pattern — the
input sibling)::

    # The dentate gyrus is the INPUT subfield — the SIBLING of the
    # cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
    #
    # The dentate gyrus is the INPUT; the cornu ammonis is the
    # OUTPUT side.

Reaching the subiculum (recommended consumer pattern — the output
target of CA1)::

    # The subiculum is the OUTPUT TARGET of CA1 — the SIBLING of
    # the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # CA1 projects to the subiculum; the subiculum is the output
    # structure the CA fields feed.

Reaching the parasubiculum and presubiculum (recommended consumer
pattern — the subicular-complex siblings)::

    # The parasubiculum and presubiculum are the HEAD-DIRECTION
    # and SPATIAL subfields of the subicular complex — the
    # SIBLINGS of the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.parasubiculum
    #   subcortical.medial_temporal_lobe.hippocampus.presubiculum
    #
    # The cornu ammonis is the CA field system; the parasubiculum
    # and presubiculum are the subicular-complex head-direction
    # subfields.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the cornu
    # ammonis and the other four subfields:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # The cornu ammonis is ONE of the five children of the
    # hippocampus.

Reaching the parahippocampal region (recommended consumer pattern —
the cortical interface)::

    # The parahippocampal region (entorhinal cortex, perirhinal
    # cortex, parahippocampal gyrus) is the CORTICAL INTERFACE that
    # feeds the hippocampus:
    #
    #   cortex.temporal.gyri.entorhinal_cortex
    #   cortex.temporal.gyri.perirhinal_cortex
    #   cortex.temporal.gyri.parahippocampal_gyrus
    #
    # The cornu ammonis is the ARCHICORTEX; the parahippocampal
    # region is the CORTICAL INPUT.

Reaching the fornix and the white matter (recommended consumer
pattern — the white-matter structures)::

    # The fornix and the white matter are the WHITE-MATTER
    # structures — NOT the cornu ammonis:
    #
    #   white_matter.fornix
    #   white_matter
    #
    # The cornu ammonis is the GREY-MATTER CA fields; the fornix and
    # the white matter are the FIBERS.

Reaching the memory software layer (recommended consumer pattern —
the software store)::

    # The ``memory/`` package is the SOFTWARE MEMORY LAYER of the
    # simulation:
    #
    #   memory.stores.long_term.explicit.episodic
    #   memory.stores.long_term.explicit.semantic
    #   memory.stores.long_term.implicit.procedural
    #   memory.stores.short_term
    #   memory.backends.chroma
    #   memory.backends.in_memory
    #
    # The cornu ammonis is the BRAIN STRUCTURE; the ``memory/``
    # package is the SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE the cornu ammonis is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT cornu ammonis children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # The cornu ammonis is the CA field system of the MEMORY
    # container; the central nucleus and the basolateral nuclei are
    # the FEAR structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
the cornu ammonis is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the cornu
    # ammonis:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The cornu_ammonis is SLEA-FREE.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ca_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.cornu_ammonis"
        )
        # resolve ca_path through the memory/recall layer

References
----------
*   **Original CA1–CA4 nomenclature:** Lorente de Nó, R. (1934).
    "Studies on the structure of the cerebral cortex. II.
    Continuation of the study of the ammonic system." *Journal für
    Psychologie und Neurologie* 46:113–177. (The original CA1–CA4
    parcellation of the cornu ammonis.)
*   **Canonical hippocampal anatomy:** Amaral, D.G., Witter, M.P.
    (1989). "The three-dimensional organization of the hippocampal
    formation: a review of anatomical data." *Neuroscience*
    31:571–591. (Definitive hippocampal formation anatomy; cornu
    ammonis, dentate gyrus, subicular complex.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; CA1–CA4 subfields.)
*   **Place cells:** O'Keefe, J., Dostrovsky, J. (1971). "The
    hippocampus as a spatial map: preliminary evidence from unit
    activity in the freely-moving rat." *Brain Research* 34:171–175.
    (Place cells in the CA1 and CA3 fields.)
*   **CA subfield functions (review):** Kesner, R.P. (2007). "Behavioral
    functions of the CA subregions of the hippocampus." In:
    *Neurobiology of Learning and Memory* (special issue on the
    hippocampus). (CA1 — temporal ordering; CA3 — pattern
    completion; CA2 — social memory.)
*   **CA2 and social memory:** Bartsch, T., et al. (2011). "Focal
    lesions of the CA2 region of the human hippocampus." *Brain*
    134:3415–3425. (CA2 and social memory — contested.)
*   **CA3 recurrent collaterals and pattern completion:** Sloviter,
    R.S. (1994). "The functional organization of the hippocampal
    dentate gyrus and its relevance to the pathogenesis of temporal
    lobe epilepsy." *Annals of Neurology* 35:640–654. (CA3
    recurrent collaterals; pattern completion.)
*   **CA4 / dentate hilus:** Amaral, D.G. (1978). "A Golgi study of
    cell types in the hilar region of the hippocampus in the rat."
    *Journal of Comparative Neurology* 182:851–914. (CA4 as the
    polymorphic layer / hilus of the dentate gyrus.)
*   **CA1 vulnerability in Alzheimer's disease:** Braak, H., Braak,
    E. (1991). "Neuropathological stageing of Alzheimer-related
    changes." *Acta Neuropathologica* 82:239–259. (CA1 as the
    earliest affected CA field.)
*   **Hippocampal sclerosis in temporal lobe epilepsy:** Mathern,
    G.W., Babb, T.L., Vickrey, B.G., Melendez, M., Pretorius, J.K.
    (1995). "The clinical-pathogenic mechanisms of hippocampal
    neuron loss and surgical outcomes in temporal lobe epilepsy."
    *Brain* 118:105–118. (CA1 and CA3 vulnerability in Ammon's horn
    sclerosis.)
*   **H.M. and medial temporal lobe amnesia:** Scoville, W.B.,
    Milner, B. (1957). "Loss of recent memory after bilateral
    hippocampal lesions." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 20:11–21. (Bilateral hippocampal damage and
    anterograde amnesia.)
*   **Declarative memory and the hippocampus:** Squire, L.R.
    (1992). "Memory and the hippocampus: a synthesis from findings
    with rats, monkeys, and humans." *Psychological Review*
    99:195–231. (Hippocampus and declarative memory.)
*   **Hippocampus and declarative memory (review):** Eichenbaum, H.
    (2004). "Hippocampus: cognitive processes and neural
    representations that underlie declarative memory." *Neuron*
    44:109–120. (Hippocampus and declarative memory.)
*   **Spatial memory and the hippocampus:** Burgess, N., Maguire,
    E.A., O'Keefe, J. (2002). "The human hippocampus and spatial
    and episodic memory." *Neuron* 35:625–641. (Hippocampus and
    spatial / episodic memory.)
*   **Pattern separation and pattern completion:** Yassa, M.A.,
    Stark, C.E.L. (2011). "Pattern separation in the hippocampus."
    *Trends in Neurosciences* 34:515–525. (Dentate gyrus pattern
    separation; CA3 pattern completion.)
*   **Adult neurogenesis in the dentate gyrus (contrast — the
    dentate gyrus, not the cornu ammonis):** Eriksson, P.S., et al.
    (1998). "Neurogenesis in the adult human hippocampus." *Nature
    Medicine* 4:1313–1317. (Adult neurogenesis in the dentate
    gyrus.)
*   **Hippocampal volume in depression:** Videbech, P., Ravnkilde,
    B. (2004). "Hippocampal volume and depression: a meta-analysis
    of MRI studies." *American Journal of Psychiatry*
    161:1957–1966. (Hippocampal volume reduction in depression —
    debated.)
*   **Hippocampal volume in PTSD:** Geuze, E., Vermetten, E.,
    Bremner, J.D. (2005). "MR-based in vivo hippocampal
    volumetrics: 2. Findings in neuropsychiatric disorders."
    *Molecular Psychiatry* 10:160–184. (Hippocampal volume
    reduction in PTSD — debated.)
*   **Amygdala (contrast — the cornu ammonis is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the hippocampus memory circuit.)
*   **SLEA (contrast — the cornu ammonis is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    cornu ammonis.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Cornu ammonis in overview.)
*   NeuroNames — Cornu ammonis (right); FMA — Cornu ammonis (right
    member).
"""