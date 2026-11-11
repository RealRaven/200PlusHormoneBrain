"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca1
===========================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── medial_temporal_lobe
                    └── hippocampus
                        └── cornu_ammonis
                            └── ca1   <-- THIS MODULE

**Primary synonym:** CA1 (left); CA1 field; CA1 subfield; Sommer
sector; regio superior of the cornu ammonis; first CA field.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**leaf subfield** of the **cornu ammonis** — the **principal-output
subfield** of the hippocampal formation (CA1 → subiculum) and the
**most vulnerable** CA field to **ischemia, hypoxia, Alzheimer's
pathology, and hippocampal sclerosis**.
**Part of:** The **cornu_ammonis** container — the **CA field
system** of the hippocampus. The **CA1** is the **principal-output
subfield** of the cornu ammonis.
**Structural parent:** ``.../cornu_ammonis/`` → **direct child** of
the cornu ammonis container.
**Structural children:** **None.** This is a **leaf** module. The
**stratum oriens**, **stratum pyramidale**, **stratum radiatum**,
and **stratum lacunosum-moleculare** of CA1 are documented as
**prose**, not as structural children.
**Boundary status (PRINCIPAL OUTPUT — the output gate of the
hippocampal formation):** **Boundary case — the ca1 is the
PRINCIPAL-OUTPUT subfield of the cornu ammonis, NOT the
pattern-completion subfield and NOT the input subfield.** The
**CA1** (here) is the **principal output** of the cornu ammonis —
it **projects** to the **subiculum**, the **entorhinal cortex**,
and the **prefrontal cortex**. The **CA3** sibling (``.../ca3/``)
is the **recurrent-collateral** subfield — the **pattern-completion**
subfield that **feeds** CA1. The **CA2** sibling (``.../ca2/``) is
the **social-memory** subfield. The **CA4** sibling (``.../ca4/``)
is the **dentate hilus** — the **mossy-cell** layer of the dentate
gyrus. **CA1 is the OUTPUT gate; CA2, CA3, and CA4 are the
upstream subfields.** Consumers must **not** conflate CA1 with
its sibling CA fields.
**Boundary status (NOT the dentate gyrus — the dentate gyrus is
the INPUT subfield):** **Boundary case — the ca1 is NOT the
dentate gyrus; the dentate gyrus is the INPUT subfield.** The
**dentate_gyrus** (``.../hippocampus/dentate_gyrus/``) is the
**principal input** of the hippocampus (entorhinal cortex →
perforant path → dentate gyrus → mossy fibers → CA3). The
**CA1** (here) is the **principal-output** subfield — **downstream**
of the dentate gyrus (dentate gyrus → CA3 → CA1). Consumers must
**not** conflate CA1 with the dentate gyrus — they are **different
subfields of the same hippocampus**.
**Boundary status (NOT the subiculum — the subiculum is the OUTPUT
TARGET of CA1):** **Boundary case — the ca1 is NOT the subiculum;
the subiculum is the OUTPUT TARGET of CA1.** The **subiculum**
(``.../hippocampus/subiculum/``) is the **principal output** of the
hippocampus to the parahippocampal region, the mammillary bodies
(via the fornix), and the prefrontal cortex — **CA1 projects to
the subiculum**. **CA1 is the output gate; the subiculum is the
output structure CA1 feeds.** Consumers must **not** conflate the
two — the **CA1** is a **CA field**; the **subiculum** is a
**sibling subfield** of the hippocampus.
**Boundary status (NOT the cornu ammonis container — CA1 is a CHILD
of the cornu ammonis):** **Boundary case — the ca1 is a CHILD of
the cornu_ammonis container, not the container itself.** The
**cornu ammonis** container contains **CA1**, **CA2**, **CA3**, and
**CA4** — the **CA1** is **one** of those four children. Consumers
must **not** conflate CA1 with the cornu ammonis container.
**Boundary status (NOT the hippocampus container — CA1 is a
grandchild of the hippocampus):** **Boundary case — the ca1 is a
GRANDCHILD of the hippocampus container.** The **hippocampus**
container contains the **cornu ammonis**, the **dentate gyrus**,
the **parasubiculum**, the **presubiculum**, and the **subiculum**
— and the **cornu ammonis** in turn contains **CA1–CA4**. The
**CA1** is a **child of the cornu ammonis**, and thus a
**grandchild** of the hippocampus. Consumers must **not** conflate
CA1 with the hippocampus container.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the ca1 is NOT the
parahippocampal region.** The **parahippocampal region** (the
**entorhinal cortex**, the **perirhinal cortex**, and the
**parahippocampal gyrus**) is **cortical** — it is wired under
``.../left/cortex/temporal/gyri/`` and is **outside** the
hippocampus container. The **CA1** (here) is the **archicortex**.
Consumers must **not** conflate CA1 with the parahippocampal
region — the parahippocampal region is **cortex/**; CA1 is
**subcortical/medial_temporal_lobe/**.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the ca1 is NOT the
fornix or the white matter; the fornix and the white_matter are
WHITE-MATTER structures.** The **fornix**
(``.../left/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../left/white_matter/``) is the **white-matter
infrastructure**. The **CA1** (here) is the **grey-matter
archicortex**. Consumers must **not** conflate the two — the
**CA1** is the **grey-matter subfield**; the **fornix** and the
**white_matter** are the **white-matter tracts**.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the ca1 is NOT the rhinencephalon.** The **rhinencephalon**
(``.../left/cortex/rhinencephalon/``) — the olfactory bulb,
olfactory tract, piriform cortex, periamygdaloid cortex, anterior
olfactory nucleus, and uncus — is the **cortical olfactory lobe**.
The **CA1** (here) is the **archicortex of episodic memory and
spatial navigation** — it is **not** an olfactory structure.
Consumers must **not** conflate the two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the ca1 is
NOT the amygdala; the amygdala is the FEAR/EMOTION/SALIENCE
container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), and
the **lateral nucleus** (sensory input). The **CA1** (here) is a
**CA field** of the **memory** container. Consumers must **not**
conflate CA1 with the amygdala — they are **different structures**
in **different containers**.
**Boundary status (SLEA-FREE — CA1 is NOT an extended-amygdala
component):** **Boundary case — the ca1 is SLEA-FREE.** The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere). The
**CA1** is an **episodic/declarative-memory and spatial-navigation**
structure — it is **NOT** an extended-amygdala component, and it
carries **NO SLEA warning**. Consumers must **not** import the
SLEA warning into CA1 — it is **SLEA-free**.
**Boundary status (NOT the memory software layer — CA1 is the BRAIN
STRUCTURE, not the ``memory/`` package):** **Boundary case — the
ca1 is the BRAIN STRUCTURE, NOT the ``memory/`` software package.**
The **``memory/`` package** (``memory/stores/`` — episodic,
semantic, procedural, working; ``memory/backends/`` — chroma,
in_memory) is the **software memory layer** of the simulation. The
**CA1** (here) is the **brain structure** that **subserves**
episodic memory. Consumers must **not** conflate the two — the
**brain structure** is wired here; the **software store** is wired
under ``memory/``.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
ca1 is NOT the fear-output or the fear-learning structures.** The
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), and the **basomedial nuclei** (fear-modulatory)
are **amygdala** children. The **CA1** is the **principal-output**
subfield of the **memory** container — it is **not** a fear-output
or fear-learning structure. Consumers must **not** conflate CA1
with the **amygdala fear circuit**.
**Boundary status (NOT a single uniform layer — MULTIPLE strata):**
**Boundary case — the ca1 is a HETEROGENEOUS subfield with
MULTIPLE strata (stratum oriens, stratum pyramidale, stratum
radiatum, stratum lacunosum-moleculare), not a single uniform
layer.** The **strata** are functionally distinct — the **stratum
pyramidale** contains the **CA1 pyramidal cells**; the **stratum
radiatum** and **stratum oriens** contain the **dendrites** and
**interneurons**; the **stratum lacunosum-moleculare** receives
the **perforant-path** input from the entorhinal cortex. The tree
wires the **CA1** as a **single leaf** under the cornu ammonis —
the **strata** are **prose**, not structural children. Consumers
that need **stratum-level** resolution should consult the
references, not the tree.

Overview
--------
CA1 is the **principal-output** subfield of the cornu ammonis — the
**archicortex** subfield that **projects** to the **subiculum**,
the **entorhinal cortex**, and the **prefrontal cortex**, and the
**most vulnerable** CA field to **ischemia, hypoxia, Alzheimer's
pathology, and hippocampal sclerosis**. It is a **leaf** module
under the cornu ammonis container, the **sibling of CA2, CA3, and
CA4**, and the **grey-matter substrate** of **place cells**,
**temporal ordering**, and **episodic-memory output**.

**CA1 is the PRINCIPAL-OUTPUT subfield of the cornu ammonis.**
**CA3** (sibling) is the **pattern-completion** subfield — it
**feeds** CA1. **CA2** (sibling) is the **social-memory** subfield.
**CA4** (sibling) is the **dentate hilus** — the **mossy-cell**
layer of the dentate gyrus. **CA1 is the OUTPUT gate; CA2, CA3, and
CA4 are the upstream subfields.**

**CA1 is NOT the subiculum.** **CA1 projects to the subiculum** —
the **subiculum** is the **output target**. **They are SIBLINGS
under the hippocampus, and they are DIFFERENT STRUCTURES.**

**CA1 is NOT the dentate gyrus.** The **dentate gyrus** is the
**input** subfield. **CA1** is the **output gate**. **They are
DIFFERENT STRUCTURES.**

**CA1 is NOT the cornu ammonis container or the hippocampus
container.** The **cornu ammonis** container contains **CA1–CA4**;
the **hippocampus** container contains the **cornu ammonis**, the
**dentate gyrus**, and the **subicular complex**.

**CA1 is NOT the parahippocampal region.** The **entorhinal
cortex**, **perirhinal cortex**, and **parahippocampal gyrus** are
**cortical** — they are wired under ``cortex/temporal/gyri/``.
**CA1** is the **archicortex**.

**CA1 is SLEA-FREE.** It is **not** an extended-amygdala component,
and it carries **no SLEA warning**. The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere).

**CA1 is the BRAIN STRUCTURE, not the ``memory/`` software
package.** The **``memory/`` package** is the **software memory
layer**. **CA1** is the **brain region** whose function the
episodic store models. **They are DIFFERENT LAYERS.**

**CA1 is a paired structure.** Each hemisphere has its own CA1,
with **ipsilateral** and **bilateral** connections to CA3, CA2, the
subiculum, the entorhinal cortex, and the contralateral CA1. The
two sides are **bilaterally symmetric** and **partially
lateralized** — the **left** CA1 is more involved in **verbal**
episodic memory, and the **right** CA1 is more involved in
**spatial/nonverbal** episodic memory. This is **well-documented**
(not contested), and documented in the **medial temporal lobe
module** (not at the CA1 level). See *Lateralization Notes*.

Stratum Composition (prose, not structural children)
----------------------------------------------------
CA1 is a **heterogeneous subfield** — documented as **prose**, not
as structural children:

*   **Stratum oriens** — the **deep** layer, containing the
    **basal dendrites** of the CA1 pyramidal cells and the
    **oriens-lacunosum-moleculare (O-LM)** interneurons.

*   **Stratum pyramidale** — the **principal-cell** layer,
    containing the **CA1 pyramidal cells** — the **output neurons**
    of CA1.

*   **Stratum radiatum** — the **apical-dendrite** layer,
    containing the **Schaffer collateral** synapses from CA3.

*   **Stratum lacunosum-moleculare** — the **superficial** layer,
    receiving the **perforant-path** input from the **entorhinal
    cortex** (via the **temporoammonic** pathway).

**These strata are prose, not structural children.** The tree wires
**CA1** as a **single leaf** under the cornu ammonis — the
**strata** are **prose**, not structural children. Consumers that
need **stratum-level** resolution should consult the references,
not the tree.

The CA1 / CA2, CA3, CA4 Boundary
--------------------------------
This is the **sibling CA-field** boundary:

*   **CA1** (this module) — the **principal-output** subfield (CA1 →
    subiculum; entorhinal cortex; prefrontal cortex).

*   **CA2** (``.../cornu_ammonis/ca2/``) — the **social-memory**
    subfield (oxytocin-receptor enriched).

*   **CA3** (``.../cornu_ammonis/ca3/``) — the
    **pattern-completion** subfield (recurrent collaterals;
    **feeds** CA1).

*   **CA4** (``.../cornu_ammonis/ca4/``) — the **dentate hilus**
    (mossy cells; mossy-fiber target).

**They are SIBLINGS under the cornu ammonis, and they are DIFFERENT
CA FIELDS.** Consumers must **not** conflate CA1 with CA2, CA3, or
CA4.

The CA1 / Dentate Gyrus Boundary
--------------------------------
This is the **output vs. input** boundary:

*   **CA1** (this module) — the **principal-output** subfield.

*   **Dentate gyrus** (``.../hippocampus/dentate_gyrus/``) — the
    **input** subfield (entorhinal cortex → perforant path →
    dentate gyrus → mossy fibers → CA3).

**They are DIFFERENT STRUCTURES** — the **dentate gyrus** is the
**input**; **CA1** is the **output gate**. Consumers must **not**
conflate the two.

The CA1 / Subiculum Boundary
----------------------------
This is the **output gate vs. output target** boundary:

*   **CA1** (this module) — the **output gate** of the cornu
    ammonis.

*   **Subiculum** (``.../hippocampus/subiculum/``) — the **output
    target** of CA1 (the subiculum projects to the parahippocampal
    region, the mammillary bodies, and the prefrontal cortex).

**CA1 projects to the subiculum** — they are **DIFFERENT
STRUCTURES**. Consumers must **not** conflate the two — **CA1** is
a **CA field**; the **subiculum** is a **sibling subfield** of the
hippocampus.

The CA1 / Cornu Ammonis Boundary
--------------------------------
This is the **child vs. container** boundary:

*   **CA1** (this module) — a **child** of the cornu ammonis
    container.

*   **Cornu ammonis** (``.../cornu_ammonis/``) — the **container**
    that contains **CA1**, **CA2**, **CA3**, and **CA4**.

**CA1 is ONE of the four children of the cornu ammonis.** Consumers
must **not** conflate CA1 with the cornu ammonis container.

The CA1 / Hippocampus Boundary
------------------------------
This is the **grandchild vs. container** boundary:

*   **CA1** (this module) — a **grandchild** of the hippocampus
    container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**CA1 is a grandchild of the hippocampus** (child of the cornu
ammonis). Consumers must **not** conflate CA1 with the hippocampus
container.

The CA1 / Parahippocampal Region Boundary
-----------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **CA1** (this module) — the **archicortex** subfield.

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../left/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus.** **CA1** is the **archicortex** that **receives**
the parahippocampal input (directly, via the
**temporoammonic** pathway; and indirectly, via the dentate gyrus
and CA3). Consumers must **not** conflate CA1 with the
parahippocampal region.

The CA1 / Fornix and White Matter Boundary
------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **CA1** (this module) — the **grey-matter** archicortex
    subfield.

*   **Fornix** (``.../left/white_matter/fornix/``) and
    **white_matter** (``.../left/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — **CA1** is the **grey-matter
subfield**; the **fornix** and the **white_matter** are the
**white-matter tracts**. Consumers must **not** conflate the two.

The CA1 / Rhinencephalon Boundary
---------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **CA1** (this module) — the **archicortex of episodic memory
    and spatial navigation**.

*   **Rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — **CA1** is the **memory
archicortex**; the **rhinencephalon** is the **olfactory lobe**.
Consumers must **not** conflate the two.

The CA1 / Amygdala Boundary
---------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **CA1** (this module) — a **CA field** of the **memory**
    container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; **CA1** is a **child of the memory**
container. Consumers must **not** conflate the two.

The CA1 / Memory Software Layer Boundary
----------------------------------------
This is the **brain structure vs. software store** boundary:

*   **CA1** (this module) — the **brain structure** (CA field) that
    subserves episodic memory.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — **CA1** is the **brain region**;
the **``memory/`` package** is the **software store**. Consumers
must **not** conflate the two.

The CA1 / SLEA Boundary
-----------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **CA1** (this module) — **SLEA-FREE**. No extended-amygdala
    relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**CA1 is NOT part of the SLEA continuum.** It is an
**episodic/declarative-memory and spatial-navigation** structure,
and it carries **no SLEA warning**. Consumers must **not** import
the SLEA warning into CA1.

Function in the Human Brain
---------------------------
CA1's functions are **episodic-memory output**, **place-cell
spatial coding**, **temporal ordering**, and **direct
parahippocampal output** — **NOT fear-output**:

*   **Principal Output (CA1 → Subiculum):** **CA1** is the
    **principal output** of the cornu ammonis — it projects to the
    **subiculum**, the **entorhinal cortex**, and the
    **prefrontal cortex**. This is the **output gate** of the
    hippocampal formation.

*   **Place-Cell Spatial Coding (CA1):** **CA1** is a **principal
    site** of **place cells** — the **spatial** neurons that fire
    when the animal is in a **specific location** in the
    environment. This is the **substrate** of the **cognitive
    map**.

*   **Temporal Ordering (CA1):** **CA1** is involved in **temporal
    ordering** — the **encoding** of the **order** of events in a
    **sequence**. This is the **substrate** of the **temporal
    structure** of episodic memory.

*   **Direct Parahippocampal Output (CA1 → Entorhinal Cortex):**
    **CA1** projects **directly** to the **entorhinal cortex** (the
    **temporoammonic** pathway), providing a **direct cortical
    return** of the hippocampal output.

*   **Prefrontal Output (CA1 → Prefrontal Cortex):** **CA1**
    projects to the **prefrontal cortex** — providing the
    **prefrontal** access to the hippocampal **episodic and
    spatial** representations.

*   **NOT a neural processor in the classical sense.** **CA1** is a
    **memory and navigation** subfield — it **outputs** the
    **episodic and spatial** representations, but it does **not**
    produce the **fear-output** or the **autonomic and behavioral**
    fear responses. The **fear-output** is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** CA1 is the **principal-output subfield** of
the **cornu ammonis** — the **output gate** that anchors **place
cells, temporal ordering, and episodic-memory output**. It is
**SLEA-free**, **memory/navigation**, and **NOT the fear-output
structure** — the **fear-output** is the **central nucleus**, the
**fear-learning** structures are the **basolateral nuclei**, and
**CA1** is the **output gate** of the **memory** container.

Associated Disorders
--------------------
CA1 has **no named "CA1 syndrome"** in the narrow sense, but its
clinical associations are **well-documented**:

*   **Alzheimer's Disease (Early CA1 Pathology):** **CA1** is the
    **earliest** affected **CA field** in **Alzheimer's disease** —
    **CA1** shows the **first neurofibrillary tangles**, and **CA1
    atrophy** is a **core biomarker** of the disease. **CA1** is
    the **memory substrate** of the disease; its involvement is
    **direct**.

*   **Temporal Lobe Epilepsy (Hippocampal Sclerosis / Ammon's Horn
    Sclerosis):** **CA1** is one of the **principal sites** of
    **hippocampal sclerosis** (Ammon's horn sclerosis) in
    **temporal lobe epilepsy** — **CA1** is the **most vulnerable**
    CA field to **excitotoxic damage**. **CA1** is the
    **epileptogenic substrate** of temporal lobe epilepsy.

*   **Anterograde Amnesia (Medial Temporal Lobe Amnesia — via the
    Hippocampus):** Bilateral **hippocampal** damage (e.g., patient
    **H.M.**) — including **CA1** — produces **anterograde
    amnesia** — the **inability** to form **new episodic
    memories**, with **preserved** short-term memory and
    **preserved** procedural memory. **CA1** is the **memory
    substrate** of this amnesia.

*   **Ischemia and Hypoxia (Selective CA1 Vulnerability):** **CA1**
    is the **most vulnerable** CA field to **global ischemia** and
    **hypoxia** (e.g., cardiac arrest, near-drowning) — **CA1**
    pyramidal cells are **selectively vulnerable** to **excitotoxic
    damage**. **CA1** is the **memory substrate** of the resulting
    **hypoxic-ischemic amnesia**.

*   **No Named "CA1 Syndrome":** **CA1** is a **CA field**, not a
    **single functional system** — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** for **memory
    and navigation** (Alzheimer's, hippocampal sclerosis, amnesia,
    ischemia).

**What is NOT here:** **CA1** is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **fear conditioning** (central nucleus + basolateral
nuclei), or **fear extinction** (ventromedial prefrontal cortex +
basomedial nuclei). Its clinical relevance is **direct** for
**memory and navigation** (Alzheimer's, hippocampal sclerosis,
amnesia, ischemia).

Lateralization Notes
--------------------
This is the **left** CA1 module. **CA1** is **bilaterally
symmetric** and **partially lateralized** — and it carries **NO
warning**:

*   **Bilateral CA1 Function:** Each hemisphere has its own CA1,
    with **ipsilateral** and **bilateral** connections to CA3, CA2,
    the subiculum, the entorhinal cortex, and the contralateral
    CA1. The two sides are **functionally symmetric** for **basic
    memory and navigation**.

*   **Partial Lateralization (Well-Documented — Verbal vs.
    Spatial):** The **left** CA1 is **more involved in verbal**
    episodic memory (word lists, stories, verbal recognition); the
    **right** CA1 is **more involved in spatial/nonverbal**
    episodic memory (spatial layouts, faces, nonverbal
    recognition). This is **well-documented**, **not contested**,
    and is documented in the **medial temporal lobe module** (not
    at the CA1 level).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** **CA1** is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into CA1.

*   **NO Amygdala-Lateralization Warning of their own (CA1 is the
    MEMORY subfield, not the fear-output):** The **right-amygdala
    fear association** belongs to the **amygdala module** —
    specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). **CA1** is a **memory
    subfield** — consumers must **not** conflate it with the
    **whole amygdala** or with the **central nucleus**. **CA1** is
    the **memory** subfield, not the **fear circuit**.

**A consumer that assumes "left CA1 = right CA1" will be
structurally correct** — the two sides are **symmetric** and
**partially lateralized** (the lateralization is documented in the
medial temporal lobe module). **CA1** is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cornu_ammonis/ca2/``, ``.../cornu_ammonis/ca3/``,
    ``.../cornu_ammonis/ca4/``,
    ``.../hippocampus/dentate_gyrus/``,
    ``.../hippocampus/subiculum/``,
    ``.../hippocampus/parasubiculum/``,
    ``.../hippocampus/presubiculum/``,
    ``.../medial_temporal_lobe/amygdala/``,
    ``.../left/cortex/temporal/gyri/entorhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/perirhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/parahippocampal_gyrus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/cortex/rhinencephalon/``, ``memory/``, or any other
    container. **CA1**'s relationships to CA2, CA3, CA4, the
    dentate gyrus, the subiculum, the parasubiculum, the
    presubiculum, the amygdala, the parahippocampal region, the
    fornix, the rhinencephalon, and the ``memory/`` package are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **stratum oriens**,
    **stratum pyramidale**, **stratum radiatum**, and **stratum
    lacunosum-moleculare** of CA1 are documented as **prose**, not
    as sub-modules. Consumers must not assume any exist as
    children; resolve stratum-level detail through the references.
*   **PRINCIPAL OUTPUT — the output gate of the cornu ammonis.**
    **CA1** is the **principal-output** subfield (CA1 → subiculum;
    entorhinal cortex; prefrontal cortex). **CA3** (sibling) is the
    **pattern-completion** subfield. **CA2** (sibling) is the
    **social-memory** subfield. **CA4** (sibling) is the **dentate
    hilus**. Consumers must **not** conflate CA1 with any of its
    sibling CA fields.
*   **NOT the dentate gyrus — the dentate gyrus is the INPUT
    subfield.** Consumers must **not** conflate CA1 with the
    dentate gyrus.
*   **NOT the subiculum — the subiculum is the OUTPUT TARGET of
    CA1.** Consumers must **not** conflate CA1 with the subiculum.
*   **NOT the cornu ammonis container — CA1 is a CHILD of the
    cornu ammonis.**
*   **NOT the hippocampus container — CA1 is a GRANDCHILD of the
    hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; **CA1** is the **archicortex**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** **CA1** is the **grey-matter CA field**.
*   **NOT the rhinencephalon.** **CA1** is **not** an olfactory
    structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** **CA1** is
    **not** an extended-amygdala component, and it carries **no
    SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; **CA1** is the
    **principal-output** subfield of the **memory** container.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; **CA1** is the **brain
    structure**. Consumers must **not** conflate the two.
*   **NOT a single uniform layer — MULTIPLE strata.** The
    **stratum oriens**, **stratum pyramidale**, **stratum
    radiatum**, and **stratum lacunosum-moleculare** are **prose**,
    not structural children.
*   **No ``AREA_PATHS`` hop.** **CA1** is a local leaf under the
    cornu ammonis, not a cross-listed leaf.
*   **No nested cross-listing.** **CA1** has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with right CA1 — strict mirror with NO
    warning.** Left and right CA1 modules are **structurally
    identical** — same **leaf** status, same **CA-field** framing,
    same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis import ca1

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "medial_temporal_lobe.hippocampus.cornu_ammonis.ca1"
    )

**Do not** assume CA1 is the **subiculum**. The **subiculum** is the
**output target**; **CA1** is the **output gate**. They are
**siblings**.

**Do not** assume CA1 is the **dentate gyrus**. The **dentate
gyrus** is the **input** subfield; **CA1** is the **output gate**.

**Do not** assume CA1 is **CA2**, **CA3**, or **CA4**. Those are
the **sibling CA fields** — CA2 (social memory), CA3 (pattern
completion), CA4 (dentate hilus). **CA1** is the **principal
output**.

**Do not** assume CA1 is the **cornu ammonis container** or the
**hippocampus container**. **CA1** is a **child of the cornu
ammonis** and a **grandchild of the hippocampus**.

**Do not** assume CA1 is the **parahippocampal region**. The
**entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; **CA1** is
the **archicortex**.

**Do not** assume CA1 is the **fornix** or the **white_matter**.
Those are **white-matter tracts**; **CA1** is the **grey-matter CA
field**.

**Do not** assume CA1 is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; **CA1** is
the **memory archicortex**.

**Do not** assume CA1 is the **``memory/`` software package**. The
**``memory/`` package** is the **software store**; **CA1** is the
**brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into CA1. **CA1 is SLEA-FREE**
— it is **not** an extended-amygdala component, and it is **NOT
the fear-output structure**.

Iterating CA1's (empty) children (recommended consumer pattern)::

    CA1_CHILDREN = ()
    # CA1 is a leaf. The stratum oriens, stratum pyramidale,
    # stratum radiatum, and stratum lacunosum-moleculare are prose,
    # not modules.

Reaching the CA2, CA3, CA4 siblings (recommended consumer pattern —
the sibling CA fields)::

    # CA2, CA3, and CA4 are the SIBLING CA fields under the cornu
    # ammonis:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca2
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca3
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca4
    #
    # CA1 is the PRINCIPAL OUTPUT; CA3 is the PATTERN-COMPLETION
    # subfield; CA2 is the SOCIAL-MEMORY subfield; CA4 is the
    # DENTATE HILUS.

Reaching the dentate gyrus (recommended consumer pattern — the
input subfield)::

    # The dentate gyrus is the INPUT subfield — the sibling of the
    # cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
    #
    # The dentate gyrus is the INPUT; CA1 is the OUTPUT gate.

Reaching the subiculum (recommended consumer pattern — the output
target of CA1)::

    # The subiculum is the OUTPUT TARGET of CA1 — the sibling of
    # the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # CA1 projects to the subiculum; the subiculum is the output
    # structure CA1 feeds.

Reaching the cornu ammonis (recommended consumer pattern — the
container)::

    # The cornu ammonis is the CONTAINER that contains CA1, CA2,
    # CA3, and CA4:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
    #
    # CA1 is ONE of the four children of the cornu ammonis.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the cornu
    # ammonis, the dentate gyrus, and the subicular complex:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # CA1 is a GRANDCHILD of the hippocampus (child of the cornu
    # ammonis).

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
    # CA1 is the ARCHICORTEX; the parahippocampal region is the
    # CORTICAL INPUT.

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
    # CA1 is the BRAIN STRUCTURE; the ``memory/`` package is the
    # SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE CA1 is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT CA1 children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # CA1 is the principal-output CA field of the MEMORY container;
    # the central nucleus and the basolateral nuclei are the FEAR
    # structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
CA1 is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include CA1:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # CA1 is SLEA-FREE.

Stratum-level detail (not wired — consult references)::

    # CA1's strata are prose, not modules:
    #   stratum oriens                -> basal dendrites; O-LM
    #                                    interneurons
    #   stratum pyramidale            -> CA1 pyramidal cells
    #                                    (output neurons)
    #   stratum radiatum              -> Schaffer collaterals
    #                                    (from CA3)
    #   stratum lacunosum-moleculare  -> perforant path (from
    #                                    entorhinal cortex, via the
    #                                    temporoammonic pathway)
    #
    # Do not attempt to resolve these as sub-paths of CA1.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ca1_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.cornu_ammonis.ca1"
        )
        # resolve ca1_path through the memory/recall layer

References
----------
*   **Original CA1 nomenclature:** Lorente de Nó, R. (1934).
    "Studies on the structure of the cerebral cortex. II.
    Continuation of the study of the ammonic system." *Journal für
    Psychologie und Neurologie* 46:113–177. (The original CA1–CA4
    parcellation of the cornu ammonis.)
*   **Canonical CA1 anatomy:** Amaral, D.G., Witter, M.P. (1989).
    "The three-dimensional organization of the hippocampal
    formation: a review of anatomical data." *Neuroscience*
    31:571–591. (Definitive CA1 anatomy; strata; intrinsic
    circuitry.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; CA1 subfield.)
*   **Place cells:** O'Keefe, J., Dostrovsky, J. (1971). "The
    hippocampus as a spatial map: preliminary evidence from unit
    activity in the freely-moving rat." *Brain Research* 34:171–175.
    (Place cells in the CA1 field.)
*   **CA1 and temporal ordering:** Kesner, R.P., Gilbert, P.E.,
    Barua, L.A. (2002). "The role of the hippocampus in memory for
    the temporal order of a sequence of odors." *Behavioral
    Neuroscience* 116:286–290. (CA1 and temporal ordering.)
*   **CA1 output to the subiculum:** Amaral, D.G., Dolorfo, C.,
    Alvarez-Royo, P. (1991). "Organization of CA1 projections to the
    subiculum: a PHA-L analysis in the rat." *Hippocampus* 1:415–435.
    (CA1 → subiculum projection.)
*   **CA1 output to the entorhinal cortex (temporoammonic
    pathway):** Witter, M.P. (1993). "Organization of the entorhinal-
    hippocampal system: a review of current anatomical data."
    *Hippocampus* 3:33–44. (CA1 → entorhinal cortex direct
    projection.)
*   **CA1 and Alzheimer's disease:** Braak, H., Braak, E. (1991).
    "Neuropathological stageing of Alzheimer-related changes."
    *Acta Neuropathologica* 82:239–259. (CA1 as the earliest
    affected CA field.)
*   **CA1 and hippocampal sclerosis:** Mathern, G.W., Babb, T.L.,
    Vickrey, B.G., Melendez, M., Pretorius, J.K. (1995). "The
    clinical-pathogenic mechanisms of hippocampal neuron loss and
    surgical outcomes in temporal lobe epilepsy." *Brain*
    118:105–118. (CA1 vulnerability in Ammon's horn sclerosis.)
*   **Selective CA1 vulnerability to ischemia:** Kirino, T. (1982).
    "Delayed neuronal death in the gerbil hippocampus following
    ischemia." *Brain Research* 239:57–69. (Selective CA1
    vulnerability to ischemia and hypoxia.)
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
    *Trends in Neurosciences* 34:515–525. (CA3 pattern completion;
    dentate gyrus pattern separation.)
*   **Amygdala (contrast — CA1 is NOT the amygdala):** LeDoux, J.E.
    (2000). "Emotion circuits in the brain." *Annual Review of
    Neuroscience* 23:155–184. (Amygdala fear circuit — distinct
    from the hippocampus memory circuit.)
*   **SLEA (contrast — CA1 is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT CA1.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (CA1 in overview.)
*   NeuroNames — CA1 field (left); FMA — CA1 field (left member).
"""