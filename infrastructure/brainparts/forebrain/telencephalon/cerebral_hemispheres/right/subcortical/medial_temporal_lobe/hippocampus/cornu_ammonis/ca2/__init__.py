"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca2
============================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── medial_temporal_lobe
                    └── hippocampus
                        └── cornu_ammonis
                            └── ca2   <-- THIS MODULE

**Primary synonym:** CA2 (right); CA2 field; CA2 subfield; CA2 region;
second CA field; regio inferior transitional zone.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**leaf subfield** of the **cornu ammonis** — the **small,
transitional, relatively excitotoxin-resistant** CA field between
CA1 and CA3, **enriched in oxytocin and vasopressin receptors** and
implicated (contestedly) in **social memory**.
**Part of:** The **cornu_ammonis** container — the **CA field
system** of the hippocampus. The **CA2** is the **social-memory**
subfield of the cornu ammonis.
**Structural parent:** ``.../cornu_ammonis/`` → **direct child** of
the cornu ammonis container.
**Structural children:** **None.** This is a **leaf** module. The
**stratum oriens**, **stratum pyramidale**, **stratum radiatum**,
and **stratum lacunosum-moleculare** of CA2 are documented as
**prose**, not as structural children.
**Boundary status (SOCIAL-MEMORY subfield — NOT the
principal-output subfield and NOT the pattern-completion
subfield):** **Boundary case — the ca2 is the SOCIAL-MEMORY
subfield of the cornu ammonis, NOT the principal-output subfield
and NOT the pattern-completion subfield.** The **CA1** sibling
(``.../ca1/``) is the **principal-output** subfield (CA1 →
subiculum; entorhinal cortex; prefrontal cortex). The **CA3**
sibling (``.../ca3/``) is the **recurrent-collateral**,
**pattern-completion** subfield. The **CA4** sibling
(``.../ca4/``) is the **dentate hilus** — the **mossy-cell** layer
of the dentate gyrus. **CA2 is the small, transitional,
social-memory subfield** — it is **neither** the output gate
**nor** the pattern-completion subfield. Consumers must **not**
conflate CA2 with CA1, CA3, or CA4.
**Boundary status (TRANSITIONAL — between CA1 and CA3, NOT a
homologue of either):** **Boundary case — the ca2 is a
TRANSITIONAL subfield between CA1 and CA3, NOT a homologue of
either.** **CA2** sits **between** CA1 and CA3 — it is a
**transitional zone** with a **distinct molecular and
electrophysiological profile** (it is **not** simply "the border
between CA1 and CA3"). CA2 has its **own** cytoarchitectonic
identity — **large, dark-staining pyramidal cells**, **distinct
afferent and efferent connectivity**, and **oxytocin and
vasopressin receptor enrichment** that neither CA1 nor CA3 has.
Consumers must **not** treat CA2 as a boundary artifact or as
"part of CA1" or "part of CA3" — it is a **distinct CA field**.
**Boundary status (RELATIVELY RESISTANT — NOT the vulnerable CA1 or
CA3 profile):** **Boundary case — the ca2 is RELATIVELY RESISTANT
to excitotoxic damage, NOT the vulnerable CA1 or CA3 profile.** The
**CA1** sibling is the **most vulnerable** CA field to
**ischemia**, **hypoxia**, **Alzheimer's pathology**, and
**hippocampal sclerosis**. The **CA3** sibling is **vulnerable** to
**seizures** and to **excitotoxic damage**. The **CA2** (here) is
**relatively resistant** to **excitotoxic damage** and is
**spared** in **hippocampal sclerosis** (Ammon's horn sclerosis) —
CA2 is one of the **first** places to look for **preserved**
pyramidal cells in a **sclerotic** hippocampus. Consumers must
**not** assume CA2 shares the **vulnerability profile** of CA1 or
CA3 — it does **not**.
**Boundary status (NOT the dentate gyrus — the dentate gyrus is the
INPUT subfield):** **Boundary case — the ca2 is NOT the dentate
gyrus; the dentate gyrus is the INPUT subfield.** The
**dentate_gyrus** (``.../hippocampus/dentate_gyrus/``) is the
**principal input** of the hippocampus (entorhinal cortex →
perforant path → dentate gyrus → mossy fibers → CA3). The **CA2**
(here) is a **CA field** — **downstream** of the dentate gyrus (via
CA3 and the entorhinal cortex). Consumers must **not** conflate CA2
with the dentate gyrus — they are **different subfields of the same
hippocampus**.
**Boundary status (NOT the subiculum — the subiculum is the OUTPUT
TARGET of CA1):** **Boundary case — the ca2 is NOT the subiculum;
the subiculum is the OUTPUT TARGET of CA1.** The **subiculum**
(``.../hippocampus/subiculum/``) is the **principal output** of the
hippocampus to the parahippocampal region, the mammillary bodies
(via the fornix), and the prefrontal cortex — **CA1 projects to
the subiculum**. The **CA2** (here) is a **CA field** that
**projects** to CA1 and to the **entorhinal cortex** — it is **not**
the subiculum. Consumers must **not** conflate CA2 with the
subiculum — the **CA2** is a **CA field**; the **subiculum** is a
**sibling subfield** of the hippocampus.
**Boundary status (NOT the cornu ammonis container — CA2 is a CHILD
of the cornu ammonis):** **Boundary case — the ca2 is a CHILD of
the cornu_ammonis container, not the container itself.** The
**cornu ammonis** container contains **CA1**, **CA2**, **CA3**, and
**CA4** — the **CA2** is **one** of those four children. Consumers
must **not** conflate CA2 with the cornu ammonis container.
**Boundary status (NOT the hippocampus container — CA2 is a
grandchild of the hippocampus):** **Boundary case — the ca2 is a
GRANDCHILD of the hippocampus container.** The **hippocampus**
container contains the **cornu ammonis**, the **dentate gyrus**,
the **parasubiculum**, the **presubiculum**, and the **subiculum**
— and the **cornu ammonis** in turn contains **CA1–CA4**. The
**CA2** is a **child of the cornu ammonis**, and thus a
**grandchild** of the hippocampus. Consumers must **not** conflate
CA2 with the hippocampus container.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the ca2 is NOT the
parahippocampal region.** The **parahippocampal region** (the
**entorhinal cortex**, the **perirhinal cortex**, and the
**parahippocampal gyrus**) is **cortical** — it is wired under
``.../right/cortex/temporal/gyri/`` and is **outside** the
hippocampus container. The **CA2** (here) is the **archicortex**.
Consumers must **not** conflate CA2 with the parahippocampal
region — the parahippocampal region is **cortex/**; CA2 is
**subcortical/medial_temporal_lobe/**.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the ca2 is NOT the
fornix or the white matter; the fornix and the white_matter are
WHITE-MATTER structures.** The **fornix**
(``.../right/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../right/white_matter/``) is the **white-matter
infrastructure**. The **CA2** (here) is the **grey-matter
archicortex**. Consumers must **not** conflate the two — the
**CA2** is the **grey-matter subfield**; the **fornix** and the
**white_matter** are the **white-matter tracts**.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the ca2 is NOT the rhinencephalon.** The **rhinencephalon**
(``.../right/cortex/rhinencephalon/``) — the olfactory bulb,
olfactory tract, piriform cortex, periamygdaloid cortex, anterior
olfactory nucleus, and uncus — is the **cortical olfactory lobe**.
The **CA2** (here) is the **archicortex of episodic memory and
spatial navigation** — it is **not** an olfactory structure.
Consumers must **not** conflate the two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the ca2 is
NOT the amygdala; the amygdala is the FEAR/EMOTION/SALIENCE
container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), the
**lateral nucleus** (sensory input), and the **medial nucleus**
(olfactory/pheromone). The **CA2** (here) is a **CA field** of the
**memory** container. Consumers must **not** conflate CA2 with the
amygdala — they are **different structures** in **different
containers**.
**Boundary status (SLEA-FREE — CA2 is NOT an extended-amygdala
component):** **Boundary case — the ca2 is SLEA-FREE.** The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere). The
**CA2** is an **episodic/declarative-memory and
spatial-navigation** structure — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into CA2 — it is
**SLEA-free**.
**Boundary status (NOT the memory software layer — CA2 is the BRAIN
STRUCTURE, not the ``memory/`` package):** **Boundary case — the
ca2 is the BRAIN STRUCTURE, NOT the ``memory/`` software package.**
The **``memory/`` package** (``memory/stores/`` — episodic,
semantic, procedural, working; ``memory/backends/`` — chroma,
in_memory) is the **software memory layer** of the simulation. The
**CA2** (here) is the **brain structure** that **subserves**
episodic and social memory. Consumers must **not** conflate the
two — the **brain structure** is wired here; the **software
store** is wired under ``memory/``.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
ca2 is NOT the fear-output or the fear-learning structures.** The
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), and the **basomedial nuclei** (fear-modulatory)
are **amygdala** children. The **CA2** is the **social-memory**
subfield of the **memory** container — it is **not** a fear-output
or fear-learning structure. Consumers must **not** conflate CA2
with the **amygdala fear circuit**.
**Boundary status (NOT a single uniform layer — MULTIPLE strata):**
**Boundary case — the ca2 is a HETEROGENEOUS subfield with
MULTIPLE strata (stratum oriens, stratum pyramidale, stratum
radiatum, stratum lacunosum-moleculare), not a single uniform
layer.** The **strata** are functionally distinct — the **stratum
pyramidale** contains the **CA2 pyramidal cells** (large,
dark-staining); the **stratum radiatum** and **stratum oriens**
contain the **dendrites** and **interneurons**; the **stratum
lacunosum-moleculare** receives **entorhinal** input. The tree
wires the **CA2** as a **single leaf** under the cornu ammonis —
the **strata** are **prose**, not structural children. Consumers
that need **stratum-level** resolution should consult the
references, not the tree.

Overview
--------
CA2 is the **social-memory** subfield of the cornu ammonis — the
**small, transitional, relatively excitotoxin-resistant** CA field
between CA1 and CA3, **enriched in oxytocin and vasopressin
receptors**, and implicated (contestedly) in **social memory**. It
is a **leaf** module under the cornu ammonis container, the
**sibling of CA1, CA3, and CA4**, and the **grey-matter substrate**
of **social recognition**, **social memory**, and
**social-relevance gating** of episodic content.

**CA2 is the SOCIAL-MEMORY subfield of the cornu ammonis.** **CA1**
(sibling) is the **principal-output** subfield. **CA3** (sibling)
is the **pattern-completion** subfield. **CA4** (sibling) is the
**dentate hilus**. **CA2 is the small, transitional,
social-memory subfield** — it is **neither** the output gate
**nor** the pattern-completion subfield.

**CA2 is a TRANSITIONAL subfield between CA1 and CA3, NOT a
homologue of either.** CA2 has its **own** cytoarchitectonic
identity — **large, dark-staining pyramidal cells**, **distinct
afferent and efferent connectivity**, and **oxytocin and
vasopressin receptor enrichment** that neither CA1 nor CA3 has.
Consumers must **not** treat CA2 as a boundary artifact or as
"part of CA1" or "part of CA3."

**CA2 is RELATIVELY RESISTANT to excitotoxic damage, NOT the
vulnerable CA1 or CA3 profile.** CA2 is **spared** in
**hippocampal sclerosis** (Ammon's horn sclerosis) — it is one of
the **first** places to look for **preserved** pyramidal cells in a
**sclerotic** hippocampus. **CA1** and **CA3** are the
**vulnerable** subfields; **CA2** is the **relatively resistant**
subfield.

**CA2 is NOT the subiculum.** **CA1 projects to the subiculum** —
the **subiculum** is the **output target**. **CA2** is a **CA
field** that **projects** to CA1 and to the entorhinal cortex. They
are **DIFFERENT STRUCTURES.**

**CA2 is NOT the dentate gyrus.** The **dentate gyrus** is the
**input** subfield. **CA2** is a **CA field**. **They are
DIFFERENT STRUCTURES.**

**CA2 is NOT the cornu ammonis container or the hippocampus
container.** The **cornu ammonis** container contains **CA1–CA4**;
the **hippocampus** container contains the **cornu ammonis**, the
**dentate gyrus**, and the **subicular complex**.

**CA2 is NOT the parahippocampal region.** The **entorhinal
cortex**, **perirhinal cortex**, and **parahippocampal gyrus** are
**cortical** — they are wired under ``cortex/temporal/gyri/``.
**CA2** is the **archicortex**.

**CA2 is SLEA-FREE.** It is **not** an extended-amygdala component,
and it carries **no SLEA warning**. The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere).

**CA2 is the BRAIN STRUCTURE, not the ``memory/`` software
package.** The **``memory/`` package** is the **software memory
layer**. **CA2** is the **brain region** whose function the
episodic and social stores model. **They are DIFFERENT LAYERS.**

**CA2 is a paired structure.** Each hemisphere has its own CA2,
with **ipsilateral** and **bilateral** connections to CA1, CA3, the
entorhinal cortex, and the contralateral CA2. The two sides are
**bilaterally symmetric** and **partially lateralized** — the
**left** CA2 is more involved in **verbal** social memory, and the
**right** CA2 is more involved in **spatial/nonverbal** social
memory. This is **partial**, **contested**, and documented in the
**medial temporal lobe module** (not at the CA2 level). See
*Lateralization Notes*.

Stratum Composition (prose, not structural children)
----------------------------------------------------
CA2 is a **heterogeneous subfield** — documented as **prose**, not
as structural children:

*   **Stratum oriens** — the **deep** layer, containing the
    **basal dendrites** of the CA2 pyramidal cells.

*   **Stratum pyramidale** — the **principal-cell** layer,
    containing the **CA2 pyramidal cells** — the **large,
    dark-staining** output neurons that distinguish CA2 from CA1
    and CA3.

*   **Stratum radiatum** — the **apical-dendrite** layer,
    containing **CA2-associated** synapses (including **CA3**
    input).

*   **Stratum lacunosum-moleculare** — the **superficial** layer,
    receiving the **entorhinal** input.

**These strata are prose, not structural children.** The tree wires
**CA2** as a **single leaf** under the cornu ammonis — the
**strata** are **prose**, not structural children. Consumers that
need **stratum-level** resolution should consult the references,
not the tree.

The CA2 / CA1, CA3, CA4 Boundary
--------------------------------
This is the **sibling CA-field** boundary:

*   **CA2** (this module) — the **social-memory** subfield
    (oxytocin-receptor enriched; relatively excitotoxin-resistant).

*   **CA1** (``.../cornu_ammonis/ca1/``) — the **principal-output**
    subfield (CA1 → subiculum; entorhinal cortex; prefrontal
    cortex); the **most vulnerable** CA field.

*   **CA3** (``.../cornu_ammonis/ca3/``) — the
    **pattern-completion** subfield (recurrent collaterals;
    vulnerable to seizures and excitotoxicity).

*   **CA4** (``.../cornu_ammonis/ca4/``) — the **dentate hilus**
    (mossy cells; mossy-fiber target).

**They are SIBLINGS under the cornu ammonis, and they are DIFFERENT
CA FIELDS.** Consumers must **not** conflate CA2 with CA1, CA3, or
CA4 — the **vulnerability profiles differ** (CA1 and CA3 vulnerable;
CA2 resistant), the **functions differ** (CA1 output; CA3 pattern
completion; CA2 social memory), and the **connectivity differs**.

The CA2 / Dentate Gyrus Boundary
--------------------------------
This is the **CA field vs. input subfield** boundary:

*   **CA2** (this module) — a **CA field** (social-memory subfield).

*   **Dentate gyrus** (``.../hippocampus/dentate_gyrus/``) — the
    **input** subfield (entorhinal cortex → perforant path →
    dentate gyrus → mossy fibers → CA3).

**They are DIFFERENT STRUCTURES** — the **dentate gyrus** is the
**input**; **CA2** is a **CA field** (downstream of the dentate
gyrus, via CA3 and the entorhinal cortex). Consumers must **not**
conflate the two.

The CA2 / Subiculum Boundary
----------------------------
This is the **CA field vs. output target** boundary:

*   **CA2** (this module) — a **CA field** (social-memory subfield).

*   **Subiculum** (``.../hippocampus/subiculum/``) — the **output
    target** of CA1 (the subiculum projects to the parahippocampal
    region, the mammillary bodies, and the prefrontal cortex).

**They are DIFFERENT STRUCTURES** — **CA2** is a **CA field**; the
**subiculum** is a **sibling subfield** of the hippocampus.
Consumers must **not** conflate the two.

The CA2 / Cornu Ammonis Boundary
--------------------------------
This is the **child vs. container** boundary:

*   **CA2** (this module) — a **child** of the cornu ammonis
    container.

*   **Cornu ammonis** (``.../cornu_ammonis/``) — the **container**
    that contains **CA1**, **CA2**, **CA3**, and **CA4**.

**CA2 is ONE of the four children of the cornu ammonis.** Consumers
must **not** conflate CA2 with the cornu ammonis container.

The CA2 / Hippocampus Boundary
------------------------------
This is the **grandchild vs. container** boundary:

*   **CA2** (this module) — a **grandchild** of the hippocampus
    container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**CA2 is a grandchild of the hippocampus** (child of the cornu
ammonis). Consumers must **not** conflate CA2 with the hippocampus
container.

The CA2 / Parahippocampal Region Boundary
-----------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **CA2** (this module) — the **archicortex** subfield.

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../right/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus.** **CA2** is the **archicortex** that **receives**
the parahippocampal input (via the entorhinal cortex and CA3).
Consumers must **not** conflate CA2 with the parahippocampal
region.

The CA2 / Fornix and White Matter Boundary
------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **CA2** (this module) — the **grey-matter** archicortex
    subfield.

*   **Fornix** (``.../right/white_matter/fornix/``) and
    **white_matter** (``.../right/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — **CA2** is the **grey-matter
subfield**; the **fornix** and the **white_matter** are the
**white-matter tracts**. Consumers must **not** conflate the two.

The CA2 / Rhinencephalon Boundary
---------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **CA2** (this module) — the **archicortex** subfield.

*   **Rhinencephalon** (``.../right/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — **CA2** is the **memory
archicortex**; the **rhinencephalon** is the **olfactory lobe**.
Consumers must **not** conflate the two.

The CA2 / Amygdala Boundary
---------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **CA2** (this module) — a **CA field** of the **memory**
    container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; **CA2** is a **child of the memory**
container. Consumers must **not** conflate the two.

The CA2 / Memory Software Layer Boundary
----------------------------------------
This is the **brain structure vs. software store** boundary:

*   **CA2** (this module) — the **brain structure** (CA field) that
    subserves episodic and social memory.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — **CA2** is the **brain region**;
the **``memory/`` package** is the **software store**. Consumers
must **not** conflate the two.

The CA2 / SLEA Boundary
-----------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **CA2** (this module) — **SLEA-FREE**. No extended-amygdala
    relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**CA2 is NOT part of the SLEA continuum.** It is an
**episodic/declarative-memory and spatial-navigation** structure,
and it carries **no SLEA warning**. Consumers must **not** import
the SLEA warning into CA2.

Function in the Human Brain
---------------------------
CA2's functions are **social memory**, **social recognition**, and
**social-relevance gating of episodic content** — **NOT
episodic-memory output and NOT fear-output**:

*   **Social Memory (Oxytocin-Receptor Enriched):** **CA2** is
    **enriched in oxytocin and vasopressin receptors** and is
    implicated in **social memory** — the **recognition** and
    **retention** of **conspecific** information. This is the
    **substrate** of **social recognition** and **social memory**.
    The role is **contested** — see *Associated Disorders*.

*   **Social Recognition (Conspecific Recognition):** **CA2** is
    implicated in **social recognition** — the **recognition** of
    **familiar conspecifics**. This is the **substrate** of
    **social-recognition memory**.

*   **Social-Relevance Gating of Episodic Content:** **CA2** is
    implicated in **gating** which **episodic content** is
    **tagged** as **socially relevant** — the **social-salience**
    filter on episodic encoding. This is **contested** and is
    documented in the references.

*   **Output to CA1 and the Entorhinal Cortex:** **CA2** projects to
    **CA1** and to the **entorhinal cortex** — it is a **relay**
    in the **CA3 → CA2 → CA1** stream and a **direct** contributor
    to the **entorhinal** output. This is the **circuit** position
    of CA2.

*   **Relatively Excitotoxin-Resistant (Sparing in Hippocampal
    Sclerosis):** **CA2** is **relatively resistant** to
    **excitotoxic damage** — it is **spared** in **hippocampal
    sclerosis** (Ammon's horn sclerosis), where **CA1** and **CA3**
    are **destroyed**. This is the **clinical** signature of CA2.

*   **NOT a neural processor in the classical sense.** **CA2** is a
    **memory and social-cognition** subfield — it **encodes** and
    **gates** the **social and episodic** representations, but it
    does **not** produce the **fear-output** or the **autonomic and
    behavioral** fear responses. The **fear-output** is the
    **central nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**.

**The unifying theme:** CA2 is the **social-memory subfield** of the
**cornu ammonis** — the **small, transitional, relatively
excitotoxin-resistant** CA field that anchors **social memory,
social recognition, and social-relevance gating**. It is
**SLEA-free**, **memory/social-cognition**, and **NOT the
fear-output structure** — the **fear-output** is the **central
nucleus**, the **fear-learning** structures are the **basolateral
nuclei**, and **CA2** is the **social-memory subfield** of the
**memory** container.

Associated Disorders
--------------------
CA2 has **no named "CA2 syndrome"** in the narrow sense, but its
clinical associations are **reported** — several of them
**contested**:

*   **Schizophrenia (CA2 Pathology — Contested):** **CA2** shows
    **atypical** findings in **schizophrenia** — **reduced CA2
    volume**, **reduced CA2 pyramidal-cell density**, and
    **atypical CA2 connectivity** are reported. This is
    **contested** — the findings are **not** uniformly replicated.
    **CA2** is the **memory substrate** of the reported findings;
    its involvement is **contested**.

*   **Social-Memory Deficits (Focal CA2 Lesions — Contested):**
    **Focal CA2 lesions** in humans have been associated with
    **social-memory deficits** — **impaired recognition** of
    **familiar conspecifics** and **impaired social
    recognition**. This is **contested** and is documented in the
    references (Bartsch et al., 2011).

*   **Temporal Lobe Epilepsy (CA2 Sparing):** **CA2** is
    **relatively spared** in **hippocampal sclerosis** (Ammon's
    horn sclerosis) — **CA2** is one of the **first** places to
    look for **preserved** pyramidal cells in a **sclerotic**
    hippocampus. This is the **clinical** signature of CA2's
    **relative excitotoxin resistance**.

*   **Autism Spectrum Disorder (Social-Memory Circuit — Indirect):**
    **CA2** is part of the **social-memory circuit** — the
    **oxytocin-receptor-enriched** circuit implicated in **social
    recognition**. Its involvement in **autism spectrum disorder**
    is **indirect**, via the **social-memory circuit** it anchors.

*   **No Named "CA2 Syndrome":** **CA2** is a **CA field**, not a
    **single functional system** — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** for **social
    memory and hippocampal sclerosis sparing**, and **contested**
    for **schizophrenia and focal-lesion social-memory deficits**.

**What is NOT here:** **CA2** is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **fear conditioning** (central nucleus + basolateral
nuclei), or **fear extinction** (ventromedial prefrontal cortex +
basomedial nuclei). Its clinical relevance is **direct** for
**social memory and hippocampal sclerosis sparing**, and
**contested** for **schizophrenia and focal-lesion social-memory
deficits**.

Lateralization Notes
--------------------
This is the **right** CA2 module. **CA2** is **bilaterally
symmetric** and **partially lateralized** — and it carries **NO
warning**:

*   **Bilateral CA2 Function:** Each hemisphere has its own CA2,
    with **ipsilateral** and **bilateral** connections to CA1, CA3,
    the entorhinal cortex, and the contralateral CA2. The two sides
    are **functionally symmetric** for **basic social memory**.

*   **Partial Lateralization (Contested — Semantic vs.
    Automatic):** The **left** CA2 is sometimes reported to be
    **more involved in verbal** social memory (verbal recognition
    of conspecifics); the **right** CA2 is sometimes reported to be
    **more involved in spatial/nonverbal** social memory (spatial
    social recognition). This is **partial**, **contested**, and
    documented in the **medial temporal lobe module** (not at the
    CA2 level).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** **CA2** is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into CA2.

*   **NO Amygdala-Lateralization Warning of their own (CA2 is the
    SOCIAL-MEMORY subfield, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output)
    and the **basolateral nuclei** (fear-learning). **CA2** is a
    **social-memory subfield** — consumers must **not** conflate
    it with the **whole amygdala** or with the **central nucleus**.
    **CA2** is the **social-memory** subfield, not the **fear
    circuit**.

**A consumer that assumes "left CA2 = right CA2" will be
structurally correct** — the two sides are **symmetric** and
**partially lateralized** (the lateralization is documented in the
medial temporal lobe module). **CA2** is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cornu_ammonis/ca1/``, ``.../cornu_ammonis/ca3/``,
    ``.../cornu_ammonis/ca4/``,
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
    container. **CA2**'s relationships to CA1, CA3, CA4, the
    dentate gyrus, the subiculum, the parasubiculum, the
    presubiculum, the amygdala, the parahippocampal region, the
    fornix, the rhinencephalon, and the ``memory/`` package are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **stratum oriens**,
    **stratum pyramidale**, **stratum radiatum**, and **stratum
    lacunosum-moleculare** of CA2 are documented as **prose**, not
    as sub-modules. Consumers must not assume any exist as
    children; resolve stratum-level detail through the references.
*   **SOCIAL-MEMORY subfield — NOT the principal-output subfield
    and NOT the pattern-completion subfield.** **CA2** is the
    **social-memory** subfield (oxytocin-receptor enriched).
    **CA1** (sibling) is the **principal-output** subfield. **CA3**
    (sibling) is the **pattern-completion** subfield. **CA4**
    (sibling) is the **dentate hilus**. Consumers must **not**
    conflate CA2 with any of its sibling CA fields.
*   **TRANSITIONAL — between CA1 and CA3, NOT a homologue of
    either.** CA2 is a **distinct CA field** with its **own**
    cytoarchitectonic identity — consumers must **not** treat it as
    a boundary artifact or as "part of CA1" or "part of CA3."
*   **RELATIVELY RESISTANT — NOT the vulnerable CA1 or CA3
    profile.** CA2 is **spared** in **hippocampal sclerosis**;
    CA1 and CA3 are the **vulnerable** subfields. Consumers must
    **not** assume CA2 shares the **vulnerability profile** of CA1
    or CA3.
*   **NOT the dentate gyrus — the dentate gyrus is the INPUT
    subfield.** Consumers must **not** conflate CA2 with the
    dentate gyrus.
*   **NOT the subiculum — the subiculum is the OUTPUT TARGET of
    CA1.** Consumers must **not** conflate CA2 with the subiculum.
*   **NOT the cornu ammonis container — CA2 is a CHILD of the
    cornu ammonis.**
*   **NOT the hippocampus container — CA2 is a GRANDCHILD of the
    hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; **CA2** is the **archicortex**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** **CA2** is the **grey-matter CA field**.
*   **NOT the rhinencephalon.** **CA2** is **not** an olfactory
    structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** **CA2** is
    **not** an extended-amygdala component, and it carries **no
    SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; **CA2** is the
    **social-memory** subfield of the **memory** container.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; **CA2** is the **brain
    structure**. Consumers must **not** conflate the two.
*   **NOT a single uniform layer — MULTIPLE strata.** The
    **stratum oriens**, **stratum pyramidale**, **stratum
    radiatum**, and **stratum lacunosum-moleculare** are **prose**,
    not structural children.
*   **No ``AREA_PATHS`` hop.** **CA2** is a local leaf under the
    cornu ammonis, not a cross-listed leaf.
*   **No nested cross-listing.** **CA2** has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with left CA2 — strict mirror with NO
    warning.** Left and right CA2 modules are **structurally
    identical** — same **leaf** status, same **social-memory**
    framing, same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis import ca2

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "medial_temporal_lobe.hippocampus.cornu_ammonis.ca2"
    )

**Do not** assume CA2 is the **principal-output** subfield. That is
**CA1** — CA2 is the **social-memory** subfield.

**Do not** assume CA2 is the **pattern-completion** subfield. That
is **CA3** — CA2 is the **social-memory** subfield.

**Do not** assume CA2 is the **dentate hilus**. That is **CA4** —
CA2 is the **social-memory** subfield.

**Do not** assume CA2 is a **homologue of CA1 or CA3**. CA2 is a
**transitional** but **distinct** CA field with its **own**
cytoarchitectonic identity.

**Do not** assume CA2 is the **vulnerable** CA field. CA2 is
**relatively resistant** — it is **spared** in **hippocampal
sclerosis**.

**Do not** assume CA2 is the **dentate gyrus**. The **dentate
gyrus** is the **input** subfield; **CA2** is a **CA field**.

**Do not** assume CA2 is the **subiculum**. The **subiculum** is the
**output target** of CA1; **CA2** is a **CA field**.

**Do not** assume CA2 is the **cornu ammonis container** or the
**hippocampus container**. **CA2** is a **child of the cornu
ammonis** and a **grandchild of the hippocampus**.

**Do not** assume CA2 is the **parahippocampal region**. The
**entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; **CA2** is
the **archicortex**.

**Do not** assume CA2 is the **fornix** or the **white_matter**.
Those are **white-matter tracts**; **CA2** is the **grey-matter CA
field**.

**Do not** assume CA2 is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; **CA2** is
the **memory archicortex**.

**Do not** assume CA2 is the **``memory/`` software package**. The
**``memory/`` package** is the **software store**; **CA2** is the
**brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into CA2. **CA2 is SLEA-FREE**
— it is **not** an extended-amygdala component, and it is **NOT
the fear-output structure**.

Iterating CA2's (empty) children (recommended consumer pattern)::

    CA2_CHILDREN = ()
    # CA2 is a leaf. The stratum oriens, stratum pyramidale,
    # stratum radiatum, and stratum lacunosum-moleculare are prose,
    # not modules.

Reaching the CA1, CA3, CA4 siblings (recommended consumer pattern —
the sibling CA fields)::

    # CA1, CA3, and CA4 are the SIBLING CA fields under the cornu
    # ammonis:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca1
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca3
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca4
    #
    # CA2 is the SOCIAL-MEMORY subfield; CA1 is the PRINCIPAL
    # OUTPUT; CA3 is the PATTERN-COMPLETION subfield; CA4 is the
    # DENTATE HILUS.

Reaching the dentate gyrus (recommended consumer pattern — the
input subfield)::

    # The dentate gyrus is the INPUT subfield — the sibling of the
    # cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
    #
    # The dentate gyrus is the INPUT; CA2 is a CA field downstream
    # of the dentate gyrus (via CA3 and the entorhinal cortex).

Reaching the subiculum (recommended consumer pattern — the output
target of CA1)::

    # The subiculum is the OUTPUT TARGET of CA1 — the sibling of
    # the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # CA1 projects to the subiculum; CA2 is a CA field that
    # projects to CA1 and the entorhinal cortex.

Reaching the cornu ammonis (recommended consumer pattern — the
container)::

    # The cornu ammonis is the CONTAINER that contains CA1, CA2,
    # CA3, and CA4:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
    #
    # CA2 is ONE of the four children of the cornu ammonis.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the cornu
    # ammonis, the dentate gyrus, and the subicular complex:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # CA2 is a GRANDCHILD of the hippocampus (child of the cornu
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
    # CA2 is the ARCHICORTEX; the parahippocampal region is the
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
    # CA2 is the BRAIN STRUCTURE; the ``memory/`` package is the
    # SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE CA2 is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT CA2 children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # CA2 is the social-memory CA field of the MEMORY container;
    # the central nucleus and the basolateral nuclei are the FEAR
    # structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
CA2 is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include CA2:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # CA2 is SLEA-FREE.

Stratum-level detail (not wired — consult references)::

    # CA2's strata are prose, not modules:
    #   stratum oriens                -> basal dendrites
    #   stratum pyramidale            -> CA2 pyramidal cells
    #                                    (large, dark-staining;
    #                                    oxytocin-receptor enriched)
    #   stratum radiatum              -> apical dendrites; CA3
    #                                    input
    #   stratum lacunosum-moleculare  -> entorhinal input
    #
    # Do not attempt to resolve these as sub-paths of CA2.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ca2_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.cornu_ammonis.ca2"
        )
        # resolve ca2_path through the memory/recall layer

References
----------
*   **Original CA1–CA4 nomenclature:** Lorente de Nó, R. (1934).
    "Studies on the structure of the cerebral cortex. II.
    Continuation of the study of the ammonic system." *Journal für
    Psychologie und Neurologie* 46:113–177. (The original CA1–CA4
    parcellation of the cornu ammonis; CA2 as a distinct field.)
*   **Canonical CA2 anatomy:** Amaral, D.G., Witter, M.P. (1989).
    "The three-dimensional organization of the hippocampal
    formation: a review of anatomical data." *Neuroscience*
    31:571–591. (Definitive CA2 anatomy; strata; intrinsic
    circuitry.)
*   **CA2 cytoarchitectonic identity:** Woodhams, P.L., Celio, M.R.,
    Ulfig, N., Witter, M.P. (1993). "Morphological and functional
    correlates of the CA2 subfield of the hippocampus."
    *Hippocampus* 3:213–226. (CA2 as a distinct cytoarchitectonic
    field.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; CA2 subfield.)
*   **CA2 and social memory:** Bartsch, T., et al. (2011). "Focal
    lesions of the CA2 region of the human hippocampus." *Brain*
    134:3415–3425. (CA2 and social memory — contested.)
*   **Oxytocin receptors in CA2:** Young, L.J., Wang, Z. (2004).
    "The neurobiology of pair bonding." *Nature Neuroscience*
    7:1048–1054. (Oxytocin and vasopressin receptors in CA2;
    social memory circuit.)
*   **CA2 in schizophrenia:** Benes, F.M., Kwok, E.W., Vincent,
    S.L., Todtenkopf, M.S. (1998). "A reduction of nonpyramidal
    cells in sector CA2 of schizophrenics and manic depressives."
    *Biological Psychiatry* 44:88–97. (CA2 pathology in
    schizophrenia — contested.)
*   **CA2 relative resistance in hippocampal sclerosis:** Mathern,
    G.W., Babb, T.L., Vickrey, B.G., Melendez, M., Pretorius, J.K.
    (1995). "The clinical-pathogenic mechanisms of hippocampal
    neuron loss and surgical outcomes in temporal lobe epilepsy."
    *Brain* 118:105–118. (CA2 sparing in Ammon's horn sclerosis.)
*   **CA2 output to CA1 and the entorhinal cortex:** Witter, M.P.
    (1993). "Organization of the entorhinal-hippocampal system: a
    review of current anatomical data." *Hippocampus* 3:33–44.
    (CA2 → CA1 and entorhinal cortex projections.)
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
*   **Amygdala (contrast — CA2 is NOT the amygdala):** LeDoux, J.E.
    (2000). "Emotion circuits in the brain." *Annual Review of
    Neuroscience* 23:155–184. (Amygdala fear circuit — distinct
    from the hippocampus memory circuit.)
*   **SLEA (contrast — CA2 is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT CA2.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (CA2 in overview.)
*   NeuroNames — CA2 field (right); FMA — CA2 field (right member).
"""