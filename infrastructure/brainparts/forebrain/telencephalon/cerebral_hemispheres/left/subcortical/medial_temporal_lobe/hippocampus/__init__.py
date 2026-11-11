"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus
========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── medial_temporal_lobe
                    └── hippocampus   <-- THIS MODULE (CONTAINER)

**Primary synonym:** Hippocampus (left); hippocampal formation (in
the broad sense that includes the subicular complex); hippocampus
proper (in the narrow sense, = cornu ammonis + dentate gyrus).
**Cytoarchitectonic designation:** **Not a Brodmann area.** The
**archicortex** of the medial temporal lobe — a **container
module** whose **structural children** are the **cornu ammonis**
(with CA1–CA4), the **dentate gyrus**, the **parasubiculum**, the
**presubiculum**, and the **subiculum**. Together these form the
**hippocampal formation**.
**Part of:** The **medial_temporal_lobe** container — the
**episodic/declarative-memory and spatial-navigation** structure of
the medial temporal lobe, the **sibling of the amygdala**.
**Structural parent:** ``.../medial_temporal_lobe/`` → **direct
child** of the medial temporal lobe container.
**Structural children:** **YES — this is a CONTAINER module, not a
leaf.** Its **five structural children** are:

*   ``.../hippocampus/cornu_ammonis/`` — a **container** whose own
    children are ``ca1``, ``ca2``, ``ca3``, and ``ca4``.
*   ``.../hippocampus/dentate_gyrus/`` — a **leaf**.
*   ``.../hippocampus/parasubiculum/`` — a **leaf**.
*   ``.../hippocampus/presubiculum/`` — a **leaf**.
*   ``.../hippocampus/subiculum/`` — a **leaf**.

Consumers **may** import these children; the hippocampus container
is the **structural parent** of the hippocampal formation, not a
leaf.
**Boundary status (CONTAINER — NOT a leaf, NOT a single subfield):**
**Boundary case — the hippocampus is a CONTAINER module with FIVE
structural children, not a leaf and not a single subfield.** The
**cornu ammonis**, **dentate gyrus**, **parasubiculum**,
**presubiculum**, and **subiculum** are **separate structural
children** — consumers must **not** assume the hippocampus is a
single subfield (e.g., "the hippocampus = CA1"), and must **not**
assume the subfields are prose under a leaf. They are **wired
children** with their own modules.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the
hippocampus is NOT the amygdala; the amygdala is the
FEAR/EMOTION/SALIENCE container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), the
**lateral nucleus** (sensory input), the **medial nucleus**
(olfactory/pheromone), and the **frontotemporal_cortical_system**
(cortical modulatory). The **hippocampus** (here) is the
**episodic/declarative-memory and spatial-navigation** container.
**They are SIBLINGS under the medial temporal lobe, and they are
DIFFERENT STRUCTURES** — the **amygdala** is the **emotion**
container; the **hippocampus** is the **memory** container.
Consumers must **not** conflate the two.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the hippocampus is
NOT the parahippocampal region.** The **parahippocampal region**
(the **entorhinal cortex**, the **perirhinal cortex**, and the
**parahippocampal gyrus**) is **cortical** — it is wired under
``.../left/cortex/temporal/gyri/`` (entorhinal cortex, perirhinal
cortex, parahippocampal gyrus) and is **outside** the hippocampus
container. The **hippocampus** (here) is the **archicortex** —
the **cornu ammonis**, **dentate gyrus**, **parasubiculum**,
**presubiculum**, and **subiculum**. **They are DIFFERENT
STRUCTURES**: the **parahippocampal region** is the **cortical
interface** (periallocortex and neocortex) that **feeds** the
hippocampus; the **hippocampus** is the **archicortex** that
**receives** the parahippocampal input. Consumers must **not**
conflate the **hippocampus** with the **parahippocampal region** —
the parahippocampal region is **cortex/**; the hippocampus is
**subcortical/medial_temporal_lobe/**.
**Boundary status (NOT the fornix — the fornix is a WHITE-MATTER
tract):** **Boundary case — the hippocampus is NOT the fornix; the
fornix is a WHITE-MATTER tract.** The **fornix**
(``.../left/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output to the mammillary bodies, the anterior thalamic
nuclei, and the septal nuclei. The **hippocampus** (here) is the
**grey-matter archicortex**. **They are DIFFERENT STRUCTURES**: the
**hippocampus** is the **grey-matter structure**; the **fornix** is
the **white-matter tract** it projects through. Consumers must
**not** conflate the two.
**Boundary status (NOT the white matter — the hippocampus is
GREY MATTER):** **Boundary case — the hippocampus is GREY MATTER,
NOT white matter.** The **white_matter** container
(``.../left/white_matter/``) — centrum semiovale, cingulum, corona
radiata, external capsule, extreme capsule, fasciculus rectus,
fornix, internal capsule, mammillothalamic tract, medial forebrain
bundle — is the **white-matter infrastructure**. The
**hippocampus** (here) is the **grey-matter archicortex**.
Consumers must **not** conflate the two.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the hippocampus is NOT the rhinencephalon.** The
**rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
olfactory bulb, olfactory tract, piriform cortex, periamygdaloid
cortex, anterior olfactory nucleus, and uncus — is the **cortical
olfactory lobe**. The **hippocampus** (here) is the **archicortex
of episodic memory and spatial navigation** — it is **not** an
olfactory structure. Consumers must **not** conflate the two.
**Boundary status (NOT the medial temporal lobe container — the
hippocampus is a CHILD of the medial temporal lobe):** **Boundary
case — the hippocampus is a CHILD of the medial_temporal_lobe
container, not the container itself.** The **medial_temporal_lobe**
container contains the **hippocampus** and the **amygdala**. The
**hippocampus** is **one** of those two children. Consumers must
**not** conflate the hippocampus with the medial temporal lobe
container.
**Boundary status (SLEA-FREE — the hippocampus is NOT an
extended-amygdala component):** **Boundary case — the hippocampus
is SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **hippocampus** is an
**episodic/declarative-memory and spatial-navigation** structure —
it is **NOT** an extended-amygdala component, and it carries **NO
SLEA warning**. Consumers must **not** import the SLEA warning into
the hippocampus — it is **SLEA-free**.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
hippocampus is NOT the fear-output or the fear-learning structures.**
The **central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), and the **basomedial nuclei** (fear-modulatory)
are **amygdala** children. The **hippocampus** is the
**episodic/declarative-memory and spatial-navigation** container —
it is **not** a fear-output or fear-learning structure. Consumers
must **not** conflate the hippocampus with the **amygdala fear
circuit**.
**Boundary status (NOT the memory software layer — the hippocampus
is the BRAIN STRUCTURE, not the ``memory/`` package):** **Boundary
case — the hippocampus is the BRAIN STRUCTURE, NOT the ``memory/``
software package.** The **``memory/`` package** (``memory/stores/``
— episodic, semantic, procedural, working; ``memory/backends/`` —
chroma, in_memory) is the **software memory layer** of the
simulation. The **hippocampus** (here) is the **brain structure**
that **subserves** episodic memory. **They are DIFFERENT LAYERS**:
the **``memory/`` package** is the **software store**; the
**hippocampus** is the **brain region** whose function the store
models. Consumers must **not** conflate the two — the **brain
structure** is wired here; the **software store** is wired under
``memory/``.

Overview
--------
The hippocampus is the **episodic/declarative-memory and
spatial-navigation** container of the medial temporal lobe — the
**archicortex** whose **structural children** are the **cornu
ammonis** (CA1–CA4), the **dentate gyrus**, the **parasubiculum**,
the **presubiculum**, and the **subiculum**. It is a **container**
module under the medial temporal lobe, the **sibling of the
amygdala**, and the **grey-matter substrate** of **episodic memory,
declarative memory, spatial navigation, and memory consolidation**.

**The hippocampus is a CONTAINER, not a leaf.** Its **five
structural children** — ``cornu_ammonis``, ``dentate_gyrus``,
``parasubiculum``, ``presubiculum``, ``subiculum`` — are **wired
modules**, not prose. Consumers may import them.

**The hippocampus is NOT the amygdala.** The **amygdala** is the
**fear/emotion/salience** container; the **hippocampus** is the
**episodic/declarative-memory and spatial-navigation** container.
**They are SIBLINGS under the medial temporal lobe, and they are
DIFFERENT STRUCTURES.**

**The hippocampus is NOT the parahippocampal region.** The
**entorhinal cortex**, **perirhinal cortex**, and **parahippocampal
gyrus** are **cortical** — they are wired under
``cortex/temporal/gyri/`` and are **outside** the hippocampus
container. The **hippocampus** is the **archicortex** — the
**cornu ammonis**, **dentate gyrus**, **parasubiculum**,
**presubiculum**, and **subiculum**. The **parahippocampal region**
is the **cortical interface** that **feeds** the hippocampus.

**The hippocampus is NOT the fornix.** The **fornix** is the
**white-matter output tract** of the hippocampus — the
**white-matter fibers** that carry the hippocampal output to the
mammillary bodies and the anterior thalamic nuclei. The
**hippocampus** is the **grey-matter archicortex**.

**The hippocampus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**. The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The hippocampus is the BRAIN STRUCTURE, not the ``memory/``
software package.** The **``memory/`` package** is the **software
memory layer** (episodic, semantic, procedural, working stores;
chroma and in_memory backends). The **hippocampus** is the **brain
region** whose function the episodic store models. **They are
DIFFERENT LAYERS** — the brain structure is wired here; the
software store is wired under ``memory/``.

**The hippocampus is a paired structure.** Each hemisphere has its
own hippocampus, with **ipsilateral** and **bilateral**
connections to the parahippocampal region, the septal nuclei, and
the contralateral hippocampus (via the hippocampal commissure). The
two sides are **bilaterally symmetric** and **partially
lateralized** — the **left** hippocampus is more involved in
**verbal** episodic memory, and the **right** hippocampus is more
involved in **spatial/nonverbal** episodic memory. This is
**well-documented** (not contested), and documented in the
**medial temporal lobe module** (not at the hippocampus level). See
*Lateralization Notes*.

Structural Children (wired — NOT prose)
---------------------------------------
This is a **container** module — its children are **wired
modules**, not prose:

*   ``.../hippocampus/cornu_ammonis/`` — the **Ammon's horn**
    (CA1–CA4). A **container** whose own children are ``ca1``,
    ``ca2``, ``ca3``, and ``ca4``. The cornu ammonis is the
    **principal output** of the hippocampus (CA1 → subiculum) and
    the **principal site** of **place cells** (CA1, CA3) and
    **pattern completion** (CA3).

*   ``.../hippocampus/dentate_gyrus/`` — the **dentate gyrus**. A
    **leaf**. The **principal input** of the hippocampus (from the
    entorhinal cortex) and the **principal site** of **pattern
    separation** and **adult neurogenesis**.

*   ``.../hippocampus/parasubiculum/`` — the **parasubiculum**. A
    **leaf**. Part of the **subicular complex** — involved in
    **head-direction** and **spatial** processing.

*   ``.../hippocampus/presubiculum/`` — the **presubiculum**. A
    **leaf**. Part of the **subicular complex** — involved in
    **head-direction** and **spatial** processing.

*   ``.../hippocampus/subiculum/`` — the **subiculum**. A **leaf**.
    The **principal output** of the hippocampus to the
    parahippocampal region, the mammillary bodies (via the fornix),
    and the prefrontal cortex.

**These children are wired, not prose.** The tree wires them as
**structural children** of the hippocampus — they are **not** prose
under a leaf. Consumers that need **subfield-level** resolution
should import them directly.

The Hippocampus / Amygdala Boundary
-----------------------------------
This is the **memory vs. emotion** sibling boundary:

*   **Hippocampus** (this module) — the **episodic/declarative-
    memory and spatial-navigation** container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are SIBLINGS under the medial temporal lobe, and they are
DIFFERENT STRUCTURES** — the **hippocampus** is the **memory**
container; the **amygdala** is the **emotion** container. Consumers
must **not** conflate the two.

The Hippocampus / Parahippocampal Region Boundary
-------------------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **Hippocampus** (this module) — the **archicortex** (cornu
    ammonis, dentate gyrus, parasubiculum, presubiculum, subiculum).

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../left/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus.** The **entorhinal cortex** is the **principal
input** to the hippocampus (via the perforant path to the dentate
gyrus). The **hippocampus** is the **archicortex** that **receives**
that input. Consumers must **not** conflate the **hippocampus** with
the **parahippocampal region** — the parahippocampal region is
**cortex/**; the hippocampus is
**subcortical/medial_temporal_lobe/**.

The Hippocampus / Fornix Boundary
---------------------------------
This is the **grey matter vs. white matter** boundary:

*   **Hippocampus** (this module) — the **grey-matter archicortex**.

*   **Fornix** (``.../left/white_matter/fornix/``) — the
    **white-matter output tract** of the hippocampus.

**They are DIFFERENT STRUCTURES** — the **hippocampus** is the
**grey-matter structure**; the **fornix** is the **white-matter
tract** it projects through. Consumers must **not** conflate the
two.

The Hippocampus / White Matter Boundary
---------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **Hippocampus** (this module) — the **grey-matter archicortex**.

*   **White_matter** (``.../left/white_matter/``) — the
    **white-matter infrastructure** (centrum semiovale, cingulum,
    corona radiata, external capsule, extreme capsule, fasciculus
    rectus, fornix, internal capsule, mammillothalamic tract,
    medial forebrain bundle).

**They are DIFFERENT STRUCTURES** — the **hippocampus** is the
**grey-matter archicortex**; the **white_matter** is the
**white-matter infrastructure**. Consumers must **not** conflate
the two.

The Hippocampus / Rhinencephalon Boundary
-----------------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **Hippocampus** (this module) — the **archicortex of episodic
    memory and spatial navigation**.

*   **Rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — the **hippocampus** is the
**memory archicortex**; the **rhinencephalon** is the **olfactory
lobe**. Consumers must **not** conflate the two.

The Hippocampus / Medial Temporal Lobe Boundary
-----------------------------------------------
This is the **child vs. container** boundary:

*   **Hippocampus** (this module) — a **child** of the
    medial_temporal_lobe container.

*   **Medial_temporal_lobe** (``.../medial_temporal_lobe/``) — the
    **container** that contains the **hippocampus** and the
    **amygdala**.

**The hippocampus is ONE of the two children of the medial temporal
lobe.** Consumers must **not** conflate the hippocampus with the
medial temporal lobe container.

The Hippocampus / Memory Software Layer Boundary
------------------------------------------------
This is the **brain structure vs. software store** boundary:

*   **Hippocampus** (this module) — the **brain structure** that
    subserves episodic memory.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation (episodic, semantic, procedural, working stores;
    chroma and in_memory backends).

**They are DIFFERENT LAYERS** — the **hippocampus** is the **brain
region**; the **``memory/`` package** is the **software store**.
Consumers must **not** conflate the two — the brain structure is
wired here; the software store is wired under ``memory/``.

The Hippocampus / SLEA Boundary
-------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Hippocampus** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The hippocampus is NOT part of the SLEA continuum.** It is an
**episodic/declarative-memory and spatial-navigation** structure,
and it carries **no SLEA warning**. Consumers must **not** import
the SLEA warning into the hippocampus.

Function in the Human Brain
---------------------------
The hippocampus's functions are **episodic memory**,
**declarative memory**, **spatial navigation**, and **memory
consolidation** — **NOT fear-output**:

*   **Episodic Memory (Encoding and Retrieval):** The
    **hippocampus** is the **principal brain structure** for
    **episodic memory** — the **encoding**, **consolidation**, and
    **retrieval** of **autobiographical events** (what happened,
    where, and when). This is the **substrate** of the
    **``memory/stores/long_term/explicit/episodic/``** store in the
    simulation.

*   **Declarative Memory (Semantic and Episodic):** The
    **hippocampus** is the **principal brain structure** for
    **declarative memory** — the **conscious recall** of **facts
    and events**. This is the **substrate** of the
    **``memory/stores/long_term/explicit/``** stores in the
    simulation (episodic and semantic).

*   **Spatial Navigation (Cognitive Map):** The **hippocampus** is
    the **principal brain structure** for **spatial navigation** —
    the **cognitive map** of the environment, implemented by
    **place cells** (CA1, CA3), **head-direction cells**
    (presubiculum, parasubiculum), and **grid cells** (entorhinal
    cortex — a **parahippocampal-region** structure, outside this
    module). This is the **substrate** of the **allocentric** and
    **egocentric** spatial representations.

*   **Pattern Separation (Dentate Gyrus):** The **dentate gyrus**
    is the **principal site** of **pattern separation** — the
    **orthogonalization** of **similar experiences** into
    **distinct memory traces**. This is the **substrate** of the
    **discrimination** of similar episodes.

*   **Pattern Completion (CA3):** The **CA3** subfield is the
    **principal site** of **pattern completion** — the
    **reconstruction** of a **full memory** from a **partial cue**.
    This is the **substrate** of the **recall** of a full episode
    from a partial reminder.

*   **Memory Consolidation (Systems Consolidation):** The
    **hippocampus** is the **principal brain structure** for
    **systems consolidation** — the **transfer** of **episodic
    memories** from the **hippocampus** to the **neocortex** over
    time. This is the **substrate** of the **shift** from
    **hippocampus-dependent** to **hippocampus-independent**
    memory.

*   **NOT a neural processor in the classical sense.** The
    **hippocampus** is a **memory and navigation** structure — it
    **encodes**, **consolidates**, and **retrieves** the
    **episodic and spatial** representations, but it does **not**
    produce the **fear-output** or the **autonomic and behavioral**
    fear responses. The **fear-output** is the **central nucleus**;
    the **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** the hippocampus is the
**episodic/declarative-memory and spatial-navigation** container of
the **medial temporal lobe** — the **archicortex** that anchors
**memory and navigation**. It is **SLEA-free**,
**memory/navigation**, and **NOT the fear-output structure** — the
**fear-output** is the **central nucleus**, the **fear-learning**
structures are the **basolateral nuclei**, and the **hippocampus**
is the **memory** structure.

Associated Disorders
--------------------
The hippocampus has **no named "hippocampus syndrome"** in the
narrow sense, but its clinical associations are **well-documented**:

*   **Alzheimer's Disease (Early Hippocampal and Entorhinal
    Pathology):** The **hippocampus** and the **entorhinal cortex**
    are the **earliest** affected structures in **Alzheimer's
    disease** — **CA1** and the **entorhinal cortex** show the
    **first neurofibrillary tangles**, and **hippocampal atrophy**
    is a **core biomarker** of the disease. The **hippocampus** is
    the **memory substrate** of the disease; its involvement is
    **direct**.

*   **Temporal Lobe Epilepsy (Hippocampal Sclerosis / Ammon's Horn
    Sclerosis):** The **hippocampus** — especially **CA1** and
    **CA3** — is the **principal site** of **hippocampal sclerosis**
    (Ammon's horn sclerosis) in **temporal lobe epilepsy**.
    **CA1** and **CA3** are the **most vulnerable** subfields to
    **excitotoxic damage**. The **hippocampus** is the
    **epileptogenic substrate** of temporal lobe epilepsy.

*   **Anterograde Amnesia (Medial Temporal Lobe Amnesia — via the
    Hippocampus):** Bilateral **hippocampal** damage (e.g., patient
    **H.M.**) produces **anterograde amnesia** — the **inability**
    to form **new episodic memories**, with **preserved** short-term
    memory and **preserved** procedural memory. The **hippocampus**
    is the **memory substrate** of this amnesia.

*   **PTSD (Hippocampal Volume Reduction — Debated):** The
    **hippocampus** shows **reduced volume** in **PTSD** — the
    **memory and context** functions of the hippocampus are
    **impaired**, contributing to **fear generalization** and
    **contextual** memory deficits. The involvement is
    **debated** (cause vs. consequence), and is **indirect** via the
    **amygdala** structures it interacts with.

*   **Depression (Hippocampal Volume Reduction — Debated):** The
    **hippocampus** shows **reduced volume** in **major depressive
    disorder** — the **memory and context** functions of the
    hippocampus are **impaired**. The involvement is **debated**
    (cause vs. consequence), and is **indirect**.

*   **Schizophrenia (Hippocampal Dysfunction):** The **hippocampus**
    is **dysfunctional** in **schizophrenia** — **hippocampal
    hyperactivity** and **reduced hippocampal volume** are
    **well-documented**. The involvement is **indirect**, via the
    **dopaminergic** and **glutamatergic** circuits it interacts
    with.

**What is NOT here:** The hippocampus is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **fear conditioning** (central nucleus + basolateral
nuclei), or **fear extinction** (ventromedial prefrontal cortex +
basomedial nuclei). Its clinical relevance is **direct** for
**memory and navigation** (Alzheimer's, hippocampal sclerosis,
amnesia), and **indirect** for **PTSD, depression, and
schizophrenia**.

Lateralization Notes
--------------------
This is the **left** hippocampus module. The hippocampus is
**bilaterally symmetric** and **partially lateralized** — and it
carries **NO warning**:

*   **Bilateral Hippocampal Function:** Each hemisphere has its own
    hippocampus, with **ipsilateral** and **bilateral** connections
    to the parahippocampal region, the septal nuclei, and the
    contralateral hippocampus (via the hippocampal commissure). The
    two sides are **functionally symmetric** for **basic memory and
    navigation**.

*   **Partial Lateralization (Well-Documented — Verbal vs.
    Spatial):** The **left** hippocampus is **more involved in
    verbal** episodic memory (word lists, stories, verbal
    recognition); the **right** hippocampus is **more involved in
    spatial/nonverbal** episodic memory (spatial layouts, faces,
    nonverbal recognition). This is **well-documented**, **not
    contested**, and is documented in the **medial temporal lobe
    module** (not at the hippocampus level).

*   **NO Extended-Amygdala Warning (SLEA-free module):** The
    hippocampus is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the hippocampus.

*   **NO Amygdala-Lateralization Warning of their own (the
    hippocampus is the MEMORY structure, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output)
    and the **basolateral nuclei** (fear-learning). The hippocampus
    is the **memory** structure — consumers must **not** conflate it
    with the **whole amygdala** or with the **central nucleus**. The
    **hippocampus** is the **memory and navigation** structure, not
    the **fear circuit**.

**A consumer that assumes "left hippocampus = right hippocampus"
will be structurally correct** — the two sides are **symmetric** and
**partially lateralized** (the lateralization is documented in the
medial temporal lobe module). The hippocampus is a **strict-mirror
pair with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../medial_temporal_lobe/amygdala/``,
    ``.../left/cortex/temporal/gyri/entorhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/perirhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/parahippocampal_gyrus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/cortex/rhinencephalon/``, ``memory/``, or any other
    container. The hippocampus's relationships to the amygdala, the
    parahippocampal region, the fornix, the white matter, the
    rhinencephalon, and the ``memory/`` package are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **CONTAINER module — children EXIST.** The **five structural
    children** — ``cornu_ammonis`` (with ``ca1``–``ca4``),
    ``dentate_gyrus``, ``parasubiculum``, ``presubiculum``,
    ``subiculum`` — are **wired modules**, not prose. Consumers
    **may** import them. The hippocampus is **not** a leaf.
*   **NOT a leaf — do not claim leaf status.** The hippocampus has
    **five structural children**; consumers must **not** assume it
    is a leaf and must **not** assume the subfields are prose.
*   **NOT a single subfield.** The hippocampus is **not** "CA1" or
    "the dentate gyrus" — it is the **container** of all five
    children.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.** The hippocampus is the
    **EPISODIC/DECLARATIVE-MEMORY and SPATIAL-NAVIGATION**
    container. Consumers must **not** conflate the two.
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures wired under ``cortex/temporal/gyri/``;
    the hippocampus is the **archicortex** under
    ``subcortical/medial_temporal_lobe/``. Consumers must **not**
    conflate the two.
*   **NOT the fornix — the fornix is a WHITE-MATTER tract.** The
    hippocampus is the **grey-matter archicortex**.
*   **NOT the white matter — the hippocampus is GREY MATTER.**
*   **NOT the rhinencephalon.** The hippocampus is **not** an
    olfactory structure.
*   **NOT the medial temporal lobe container — the hippocampus is a
    CHILD of the medial temporal lobe.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    hippocampus is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; the **hippocampus**
    is the **memory and navigation** structure.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; the **hippocampus** is the
    **brain structure**. Consumers must **not** conflate the two.
*   **No ``AREA_PATHS`` hop.** The hippocampus is a local container
    under the medial temporal lobe, not a cross-listed structure.
*   **No nested cross-listing.** The hippocampus has no nested
    dual-framing module. It is a single container.
*   **Structural parity with right hippocampus — strict mirror
    with NO warning.** Left and right hippocampus modules are
    **structurally identical** — same **container** status, same
    **five structural children**, same **memory/navigation**
    framing, same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe import hippocampus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "medial_temporal_lobe.hippocampus"
    )

**Do not** assume the hippocampus is a **leaf**. It has **five
structural children** — ``cornu_ammonis`` (with ``ca1``–``ca4``),
``dentate_gyrus``, ``parasubiculum``, ``presubiculum``,
``subiculum``.

**Do not** assume the hippocampus is the **amygdala**. The
**amygdala** is the **fear/emotion/salience** container; the
**hippocampus** is the **episodic/declarative-memory and
spatial-navigation** container. They are **siblings**.

**Do not** assume the hippocampus is the **parahippocampal
region**. The **entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; the
**hippocampus** is the **archicortex**.

**Do not** assume the hippocampus is the **fornix**. The **fornix**
is a **white-matter tract**; the **hippocampus** is the
**grey-matter archicortex**.

**Do not** assume the hippocampus is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; the
**hippocampus** is the **memory archicortex**.

**Do not** assume the hippocampus is the **``memory/`` software
package**. The **``memory/`` package** is the **software store**;
the **hippocampus** is the **brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the hippocampus. **The
hippocampus is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

Iterating the hippocampus's structural children (recommended
consumer pattern — NOTE these are WIRED, not prose)::

    HIPPOCAMPUS_CHILDREN = (
        "cornu_ammonis",        # container (ca1, ca2, ca3, ca4)
        "dentate_gyrus",        # leaf
        "parasubiculum",        # leaf
        "presubiculum",         # leaf
        "subiculum",            # leaf
    )

Reaching the amygdala (recommended consumer pattern — the
fear/emotion/salience sibling)::

    # The amygdala is the FEAR/EMOTION/SALIENCE container — the
    # SIBLING of the hippocampus under the medial temporal lobe:
    #
    #   subcortical.medial_temporal_lobe.amygdala
    #
    # The hippocampus is the MEMORY container; the amygdala is the
    # EMOTION container.

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
    # The hippocampus is the ARCHICORTEX; the parahippocampal region
    # is the CORTICAL INPUT.

Reaching the fornix (recommended consumer pattern — the
white-matter output tract)::

    # The fornix is the WHITE-MATTER output tract of the
    # hippocampus:
    #
    #   white_matter.fornix
    #
    # The hippocampus is the GREY-MATTER ARCHICORTEX; the fornix is
    # the FIBERS it projects through.

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
    # The hippocampus is the BRAIN STRUCTURE; the ``memory/``
    # package is the SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE the hippocampus is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT hippocampus children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # The hippocampus is the MEMORY structure; the central nucleus
    # and the basolateral nuclei are the FEAR structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
the hippocampus is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # hippocampus:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The hippocampus is SLEA-FREE.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        hpc_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus"
        )
        # resolve hpc_path through the memory/recall layer

References
----------
*   **Canonical hippocampal anatomy:** Amaral, D.G., Witter, M.P.
    (1989). "The three-dimensional organization of the hippocampal
    formation: a review of anatomical data." *Neuroscience*
    31:571–591. (Definitive hippocampal formation anatomy; cornu
    ammonis, dentate gyrus, subicular complex.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; subfields.)
*   **H.M. and medial temporal lobe amnesia:** Scoville, W.B.,
    Milner, B. (1957). "Loss of recent memory after bilateral
    hippocampal lesions." *Journal of Neurology, Neurosurgery, and
    Psychiatry* 20:11–21. (Bilateral hippocampal damage and
    anterograde amnesia.)
*   **Declarative memory and the hippocampus:** Squire, L.R.
    (1992). "Memory and the hippocampus: a synthesis from findings
    with rats, monkeys, and humans." *Psychological Review*
    99:195–231. (Hippocampus and declarative memory.)
*   **Cognitive map:** O'Keefe, J., Nadel, L. (1978). *The
    Hippocampus as a Cognitive Map*. Clarendon Press, Oxford.
    (Hippocampus as the cognitive map.)
*   **Place cells:** O'Keefe, J., Dostrovsky, J. (1971). "The
    hippocampus as a spatial map: preliminary evidence from unit
    activity in the freely-moving rat." *Brain Research* 34:171–175.
    (Place cells in the hippocampus.)
*   **Grid cells (entorhinal — parahippocampal region, contrast):**
    Hafting, T., Fyhn, M., Molden, S., Moser, M.-B., Moser, E.I.
    (2005). "Microstructure of a spatial map in the entorhinal
    cortex." *Nature* 436:801–806. (Grid cells in the entorhinal
    cortex — a parahippocampal-region structure, outside this
    module.)
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
*   **Adult neurogenesis in the dentate gyrus:** Eriksson, P.S.,
    et al. (1998). "Neurogenesis in the adult human hippocampus."
    *Nature Medicine* 4:1313–1317. (Adult neurogenesis in the
    dentate gyrus.)
*   **Alzheimer's disease and hippocampal pathology:** Braak, H.,
    Braak, E. (1991). "Neuropathological stageing of Alzheimer-
    related changes." *Acta Neuropathologica* 82:239–259.
    (Neurofibrillary tangles in CA1 and entorhinal cortex as the
    earliest pathology.)
*   **Hippocampal atrophy in Alzheimer's disease:** Small, S.A.,
    et al. (2011). "A pathophysiological framework of hippocampal
    dysfunction in ageing and disease." *Nature Reviews
    Neuroscience* 12:585–601. (Hippocampal atrophy as a core
    biomarker.)
*   **Hippocampal sclerosis in temporal lobe epilepsy:** Mathern,
    G.W., Babb, T.L., Vickrey, B.G., Melendez, M., Pretorius, J.K.
    (1995). "The clinical-pathogenic mechanisms of hippocampal
    neuron loss and surgical outcomes in temporal lobe epilepsy."
    *Brain* 118:105–118. (Ammon's horn sclerosis; CA1 and CA3
    vulnerability.)
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
*   **Amygdala (contrast — the hippocampus is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the hippocampus memory circuit.)
*   **SLEA (contrast — the hippocampus is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    hippocampus.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Hippocampus in overview.)
*   NeuroNames — Hippocampus (left); FMA — Hippocampus (left
    member).
"""