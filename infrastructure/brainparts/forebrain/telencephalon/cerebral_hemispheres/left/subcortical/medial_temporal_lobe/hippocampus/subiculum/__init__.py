"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.subiculum
====================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── medial_temporal_lobe
                    └── hippocampus
                        └── subiculum   <-- THIS MODULE

**Primary synonym:** Subiculum (left); Sub; subicular cortex;
**principal output of the hippocampus**; **part of the subicular
complex**.
**Cytoarchitectonic designation:** **Not a Brodmann area** (in the
classical numbering; sometimes assigned as area 28 in older schemes
— see references). A **leaf subfield** of the **hippocampus** — a
**cortical region of the subicular complex**, the **principal
output** of the hippocampus to the parahippocampal region, the
mammillary bodies, and the prefrontal cortex, and the **principal
target of CA1**.
**Part of:** The **hippocampus** container — the **principal
output** subfield of the subicular complex. The **subiculum** is
the **principal output** of the hippocampus.
**Structural parent:** ``.../hippocampus/`` → **direct child** of
the hippocampus container.
**Structural children:** **None.** This is a **leaf** module. The
**layers (molecular, pyramidal-cell, polymorphic)**, the **proximal
/ distal subdivisions**, and the **output projections** of the
subiculum are documented as **prose**, not as structural children.
**Boundary status (PRINCIPAL OUTPUT of the hippocampus — NOT a
head-direction / spatial subfield):** **Boundary case — the
subiculum is the PRINCIPAL OUTPUT of the hippocampus, NOT a
head-direction / spatial subfield.** The **subiculum** (here) is
the **principal output** of the hippocampus — **CA1 projects to
the subiculum**, and the **subiculum** projects to the
**parahippocampal region** (the entorhinal cortex, the perirhinal
cortex, the parahippocampal gyrus), the **mammillary bodies**
(via the **postcommissural fornix**), and the **prefrontal
cortex**. The **presubiculum** sibling (``.../presubiculum/``) and
the **parasubiculum** sibling (``.../parasubiculum/``) are
**head-direction / spatial-processing** subfields of the subicular
complex — they are **NOT** the principal output. Consumers must
**not** conflate the subiculum with the presubiculum or the
parasubiculum.
**Boundary status (SUBICULAR COMPLEX — the subicular complex is
PROSE, not a structural container):** **Boundary case — the
subiculum is part of the SUBICULAR COMPLEX, and the subicular
complex is documented as PROSE, not as a structural container.**
The **subicular complex** is the **functional grouping** of the
**subiculum**, the **presubiculum**, and the **parasubiculum**
(some schemes also include the **postsubiculum** / dorsal
presubiculum). The tree **does not** wire a "subicular complex"
container — the three subfields are **separate leaves** at the
same level under the hippocampus. Consumers must **not** assume
there is a `subicular_complex/` container, and must **not** assume
the subiculum, presubiculum, and parasubiculum share a structural
parent **other than the hippocampus itself**.
**Boundary status (NOT the presubiculum — the presubiculum is a
SIBLING subicular-complex head-direction subfield):** **Boundary
case — the subiculum is NOT the presubiculum; the presubiculum is
a SIBLING subicular-complex head-direction subfield.** The
**presubiculum** (``.../presubiculum/``) is a **sibling** of the
subiculum under the hippocampus — a **head-direction /
spatial-processing** subfield that projects principally to the
**medial entorhinal cortex (MEC) layer III**. The **subiculum**
(here) is the **principal output** of the hippocampus — it is
**not** a head-direction / spatial-processing subfield.
**They are SIBLINGS under the hippocampus, and they are DIFFERENT
subfields of the subicular complex.** Consumers must **not**
conflate the subiculum with the presubiculum.
**Boundary status (NOT the parasubiculum — the parasubiculum is a
SIBLING subicular-complex head-direction subfield):** **Boundary
case — the subiculum is NOT the parasubiculum; the parasubiculum
is a SIBLING subicular-complex head-direction subfield.** The
**parasubiculum** (``.../parasubiculum/``) is a **sibling** of the
subiculum under the hippocampus — a **head-direction /
spatial-processing** subfield that projects principally to the
**medial entorhinal cortex (MEC) layer II** (the grid-cell layer).
The **subiculum** (here) is the **principal output** of the
hippocampus. **They are SIBLINGS under the hippocampus, and they
are DIFFERENT subfields of the subicular complex.** Consumers must
**not** conflate the subiculum with the parasubiculum.
**Boundary status (NOT CA1 — CA1 PROJECTS TO the subiculum; the
subiculum IS NOT CA1):** **Boundary case — the subiculum is NOT
CA1; CA1 PROJECTS TO the subiculum.** The **CA1**
(``.../cornu_ammonis/ca1/``) is the **principal-output** subfield
of the **cornu ammonis** — **CA1 projects to the subiculum**.
The **subiculum** (here) is the **principal-output** structure
**downstream** of CA1 — it is the **output target** of CA1 and
the **output relay** of the hippocampus. **They are DIFFERENT
STRUCTURES** — the **CA1** is a **CA field**; the **subiculum**
is a **sibling subfield of the hippocampus** (part of the
**subicular complex**, **not** part of the **cornu ammonis**).
Consumers must **not** conflate the subiculum with CA1.
**Boundary status (NOT the dentate gyrus — the dentate gyrus is the
pattern-separation subfield):** **Boundary case — the subiculum is
NOT the dentate gyrus.** The **dentate gyrus**
(``.../hippocampus/dentate_gyrus/``) is the **pattern-separation**
subfield (granule cells; adult neurogenesis; mossy-fiber source).
The **subiculum** (here) is the **principal output** of the
hippocampus. Consumers must **not** conflate the subiculum with
the dentate gyrus.
**Boundary status (NOT CA2, CA3, or CA4 — those are the CA fields
of the cornu ammonis):** **Boundary case — the subiculum is NOT
CA2, CA3, or CA4.** Those are the **CA fields** of the **cornu
ammonis** container — CA2 (social memory), CA3 (pattern
completion), CA4 (dentate hilus). The **subiculum** (here) is a
**subfield of the subicular complex**, **not** a CA field.
Consumers must **not** conflate the subiculum with the CA fields.
**Boundary status (NOT the cornu ammonis — the cornu ammonis is the
CA-field container):** **Boundary case — the subiculum is NOT the
cornu ammonis.** The **cornu ammonis** (``.../cornu_ammonis/``) is
the **CA-field container** (CA1–CA4). The **subiculum** (here) is
a **sibling** of the cornu ammonis under the hippocampus — a
**subfield of the subicular complex**. **They are SIBLINGS under
the hippocampus, and they are DIFFERENT STRUCTURES.**
**Boundary status (NOT the entorhinal cortex — the entorhinal
cortex is CORTICAL, wired under ``cortex/temporal/gyri/``):
**Boundary case — the subiculum is NOT the entorhinal cortex; the
entorhinal cortex is CORTICAL and is wired under
``.../left/cortex/temporal/gyri/entorhinal_cortex/``.** The
**entorhinal cortex** is the **cortical interface** that **feeds**
the hippocampus (the **perforant-path** source), and it is **the
target** of the subiculum's principal projection. The
**subiculum** (here) is an **archicortex / subicular-complex
subfield** that **projects TO** the entorhinal cortex. **They are
DIFFERENT STRUCTURES** — the **subiculum** is the **source** of
the projection; the **entorhinal cortex** is the **target**.
Consumers must **not** conflate the subiculum with the entorhinal
cortex.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the subiculum is
NOT the parahippocampal region.** The **parahippocampal region**
(the **entorhinal cortex**, the **perirhinal cortex**, and the
**parahippocampal gyrus**) is **cortical** — it is wired under
``.../left/cortex/temporal/gyri/`` and is **outside** the
hippocampus container. The **subiculum** (here) is an **archicortex
/ subicular-complex** subfield. Consumers must **not** conflate the
subiculum with the parahippocampal region — the parahippocampal
region is **cortex/**; the subiculum is
**subcortical/medial_temporal_lobe/**.
**Boundary status (NOT the hippocampus container — the subiculum is
a CHILD of the hippocampus):** **Boundary case — the subiculum is
a CHILD of the hippocampus container, not the container itself.**
The **hippocampus** container contains the **cornu ammonis**, the
**dentate gyrus**, the **parasubiculum**, the **presubiculum**,
and the **subiculum** — the **subiculum** is **one** of those
five children. Consumers must **not** conflate the subiculum with
the hippocampus container.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the subiculum is NOT
the fornix or the white matter; the fornix and the white_matter
are WHITE-MATTER structures.** The **fornix**
(``.../left/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../left/white_matter/``) is the **white-matter
infrastructure**. The **subiculum** (here) is the **grey-matter
archicortex**. Consumers must **not** conflate the two — the
**subiculum** is the **grey-matter output structure**; the
**fornix** and the **white_matter** are the **white-matter
tracts** that carry its output.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the subiculum is NOT the rhinencephalon.** The
**rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
olfactory bulb, olfactory tract, piriform cortex, periamygdaloid
cortex, anterior olfactory nucleus, and uncus — is the **cortical
olfactory lobe**. The **subiculum** (here) is the **principal
output** of the hippocampus — it is **not** an olfactory structure.
Consumers must **not** conflate the two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the
subiculum is NOT the amygdala; the amygdala is the
FEAR/EMOTION/SALIENCE container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), the
**lateral nucleus** (sensory input), and the **medial nucleus**
(olfactory/pheromone). The **subiculum** (here) is a **subfield**
of the **memory/navigation** container. Consumers must **not**
conflate the subiculum with the amygdala.
**Boundary status (SLEA-FREE — the subiculum is NOT an
extended-amygdala component):** **Boundary case — the subiculum is
SLEA-FREE.** The **SLEA overlap** belongs to the **central
nucleus** (the **only SLEA component** in the amygdala) and to the
**BNST**, **ventral pallidum**, and **nucleus accumbens** (wired
elsewhere). The **subiculum** is an **episodic/declarative-memory
and spatial-navigation** structure — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into the subiculum —
it is **SLEA-free**.
**Boundary status (NOT the memory software layer — the subiculum
is the BRAIN STRUCTURE, not the ``memory/`` package):** **Boundary
case — the subiculum is the BRAIN STRUCTURE, NOT the ``memory/``
software package.** The **``memory/`` package** (``memory/stores/``
— episodic, semantic, procedural, working; ``memory/backends/`` —
chroma, in_memory) is the **software memory layer** of the
simulation. The **subiculum** (here) is the **brain structure**
that **subserves** the **principal-output** contribution to
episodic memory. Consumers must **not** conflate the two — the
**brain structure** is wired here; the **software store** is wired
under ``memory/``.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
subiculum is NOT the fear-output or the fear-learning structures.**
The **central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), and the **basomedial nuclei** (fear-modulatory)
are **amygdala** children. The **subiculum** is the **principal
output** of the **memory/navigation** container — it is **not** a
fear-output or fear-learning structure. Consumers must **not**
conflate the subiculum with the **amygdala fear circuit**.
**Boundary status (NOT a single uniform layer — MULTIPLE layers
and proximal / distal subdivisions):** **Boundary case — the
subiculum is a HETEROGENEOUS cortical region with MULTIPLE layers
(molecular, pyramidal-cell, polymorphic) and MULTIPLE
subdivisions (proximal, distal), not a single uniform layer.**
The **layers** and **subdivisions** are functionally distinct —
the **molecular layer** is the **superficial** layer; the
**pyramidal-cell layer** contains the **principal neurons**; the
**polymorphic layer** is the **deep** layer. The **proximal
subiculum** (closer to CA1) projects preferentially to the
**prefrontal cortex** and the **mammillary bodies** (via the
**postcommissural fornix**); the **distal subiculum** (closer to
the presubiculum) projects preferentially to the **parahippocampal
region** (entorhinal cortex, perirhinal cortex, parahippocampal
gyrus). The tree wires the **subiculum** as a **single leaf**
under the hippocampus — the **layers** and **subdivisions** are
**prose**, not structural children. Consumers that need
**layer-level** or **subdivision-level** resolution should
consult the references, not the tree.

Overview
--------
The subiculum is the **principal output** of the hippocampus — a
**cortical region** of the **subicular complex** that **receives**
the **CA1** projection and **projects** to the **parahippocampal
region** (the entorhinal cortex, the perirhinal cortex, the
parahippocampal gyrus), the **mammillary bodies** (via the
**postcommissural fornix**), and the **prefrontal cortex**. It is
a **leaf** module under the hippocampus container, the **sibling
of the cornu ammonis, the dentate gyrus, the parasubiculum, and
the presubiculum**, and the **grey-matter substrate** of the
**principal output** of the hippocampal formation.

**The subiculum is the PRINCIPAL OUTPUT of the hippocampus.** **CA1
projects to the subiculum**, and the **subiculum** projects to
the **parahippocampal region**, the **mammillary bodies** (via the
**postcommissural fornix**), and the **prefrontal cortex**. The
**subiculum** is the **output relay** of the hippocampal
formation.

**The subiculum is NOT a head-direction / spatial subfield.** The
**presubiculum** (sibling) and the **parasubiculum** (sibling) are
**head-direction / spatial-processing** subfields of the
subicular complex. The **subiculum** is the **principal output**.
**They are SIBLINGS under the hippocampus, and they are DIFFERENT
subfields of the subicular complex.**

**The subiculum is NOT CA1.** **CA1 projects to the subiculum** —
the **subiculum** is the **output target** of CA1 and the
**output relay** of the hippocampus. **They are DIFFERENT
STRUCTURES** — **CA1** is a **CA field**; the **subiculum** is a
**sibling subfield** of the hippocampus (part of the **subicular
complex**, **not** the **cornu ammonis**).

**The subicular complex is PROSE, not a structural container.**
The **subicular complex** is the **functional grouping** of the
**subiculum**, the **presubiculum**, and the **parasubiculum**.
The tree **does not** wire a `subicular_complex/` container — the
three subfields are **separate leaves** under the hippocampus.
Consumers must **not** assume a `subicular_complex/` container
exists.

**The subiculum is NOT the entorhinal cortex.** The **entorhinal
cortex** is **cortical** — wired under ``cortex/temporal/gyri/`` —
and it is the **target** of the subiculum's principal projection.
The **subiculum** is the **source** of the projection; the
**entorhinal cortex** is the **target**.

**The subiculum is NOT the cornu ammonis.** The **cornu ammonis**
is the **CA-field container** (CA1–CA4); the **subiculum** is a
**sibling** of the cornu ammonis under the hippocampus.

**The subiculum is NOT the dentate gyrus.** The **dentate gyrus**
is the **pattern-separation** subfield; the **subiculum** is the
**principal output**.

**The subiculum is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**. The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The subiculum is the BRAIN STRUCTURE, not the ``memory/``
software package.** The **``memory/`` package** is the **software
memory layer**. The **subiculum** is the **brain region** whose
function the episodic store models. **They are DIFFERENT LAYERS.**

**The subiculum is a paired structure.** Each hemisphere has its
own subiculum, with **ipsilateral** and **bilateral** connections
to CA1, the presubiculum, the entorhinal cortex, the mammillary
bodies, the prefrontal cortex, and the contralateral subiculum.
The two sides are **bilaterally symmetric** and **partially
lateralized** — the **left** subiculum is more involved in
**verbal** episodic memory, and the **right** subiculum is more
involved in **spatial/nonverbal** episodic memory. This is
**well-documented** (not contested), and documented in the
**medial temporal lobe module** (not at the subiculum level). See
*Lateralization Notes*.

Layer and Subdivision Composition (prose, not structural children)
------------------------------------------------------------------
The subiculum is a **heterogeneous cortical region** — documented
as **prose**, not as structural children:

*   **Molecular layer** — the **superficial** layer.

*   **Pyramidal-cell layer** — the **principal-cell** layer,
    containing the **subicular pyramidal cells** — the **output
    neurons** of the subiculum.

*   **Polymorphic layer** — the **deep** layer.

*   **Proximal subiculum** — the **CA1-adjacent** subdivision —
    projects preferentially to the **prefrontal cortex** and the
    **mammillary bodies** (via the **postcommissural fornix**).

*   **Distal subiculum** — the **presubiculum-adjacent**
    subdivision — projects preferentially to the
    **parahippocampal region** (entorhinal cortex, perirhinal
    cortex, parahippocampal gyrus).

**These layers and subdivisions are prose, not structural
children.** The tree wires the **subiculum** as a **single leaf**
under the hippocampus — the **layers** and **subdivisions** are
**prose**, not structural children. Consumers that need
**layer-level** or **subdivision-level** resolution should consult
the references, not the tree.

The Subiculum / CA1 Boundary
----------------------------
This is the **output target vs. output source** boundary — the most
consequential one:

*   **Subiculum** (this module) — the **principal output** of the
    hippocampus — the **output target** of CA1.

*   **CA1** (``.../cornu_ammonis/ca1/``) — the **principal-output**
    subfield of the cornu ammonis — the **output source** that
    projects to the subiculum.

**CA1 projects to the subiculum** — the **subiculum** is the
**output target** of CA1 and the **output relay** of the
hippocampus. **They are DIFFERENT STRUCTURES** — **CA1** is a
**CA field** of the cornu ammonis; the **subiculum** is a
**sibling subfield** of the hippocampus (part of the subicular
complex). Consumers must **not** conflate the subiculum with CA1.

The Subiculum / Presubiculum Boundary
-------------------------------------
This is the **principal output vs. head-direction subfield**
boundary:

*   **Subiculum** (this module) — the **principal output** of the
    hippocampus.

*   **Presubiculum** (``.../presubiculum/``) — the **sibling
    subicular-complex head-direction** subfield that projects
    principally to **MEC layer III**.

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
subfields of the subicular complex.** Consumers must **not**
conflate the subiculum with the presubiculum.

The Subiculum / Parasubiculum Boundary
--------------------------------------
This is the **principal output vs. head-direction subfield**
boundary:

*   **Subiculum** (this module) — the **principal output** of the
    hippocampus.

*   **Parasubiculum** (``.../parasubiculum/``) — the **sibling
    subicular-complex head-direction** subfield that projects
    principally to **MEC layer II** (the grid-cell layer).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
subfields of the subicular complex.** Consumers must **not**
conflate the subiculum with the parasubiculum.

The Subiculum / Dentate Gyrus Boundary
--------------------------------------
This is the **principal output vs. pattern-separation subfield**
boundary:

*   **Subiculum** (this module) — the **principal output** of the
    hippocampus.

*   **Dentate gyrus** (``.../hippocampus/dentate_gyrus/``) — the
    **pattern-separation** subfield (granule cells; adult
    neurogenesis; mossy-fiber source).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the subiculum with
the dentate gyrus.

The Subiculum / Cornu Ammonis Boundary
--------------------------------------
This is the **subicular-complex subfield vs. CA-field container**
boundary:

*   **Subiculum** (this module) — a **subicular-complex**
    subfield.

*   **Cornu ammonis** (``.../cornu_ammonis/``) — the **CA-field
    container** (CA1–CA4).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the subiculum with
the cornu ammonis container.

The Subiculum / CA2, CA3, CA4 Boundary
-------------------------------------
This is the **subicular-complex subfield vs. CA field** boundary:

*   **Subiculum** (this module) — a **subicular-complex**
    subfield.

*   **CA2, CA3, CA4** (``.../cornu_ammonis/ca2/``,
    ``.../ca3/``, ``.../ca4/``) — the **CA fields** of the cornu
    ammonis.

**They are DIFFERENT STRUCTURES** — the **subiculum** is a
**subicular-complex** subfield; the **CA fields** are the
**cornu-ammonis** subfields. Consumers must **not** conflate the
subiculum with any CA field.

The Subiculum / Entorhinal Cortex Boundary
------------------------------------------
This is the **source vs. target** boundary:

*   **Subiculum** (this module) — the **subicular-complex** subfield
    that **projects** to the entorhinal cortex.

*   **Entorhinal cortex** (``.../left/cortex/temporal/gyri/
    entorhinal_cortex/``) — the **cortical interface** that
    **receives** the subiculum projection and **feeds** the
    hippocampus via the **perforant path**.

**They are DIFFERENT STRUCTURES** — the **subiculum** is the
**source** of the projection; the **entorhinal cortex** is the
**target**. Consumers must **not** conflate the two.

The Subiculum / Parahippocampal Region Boundary
-----------------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **Subiculum** (this module) — the **archicortex** (the
    subicular-complex subfield).

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../left/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus** (via the **perforant path**). The **subiculum**
**projects** to the parahippocampal region. Consumers must **not**
conflate the **subiculum** with the **parahippocampal region** —
the parahippocampal region is **cortex/**; the subiculum is
**subcortical/medial_temporal_lobe/**.

The Subiculum / Hippocampus Boundary
------------------------------------
This is the **child vs. container** boundary:

*   **Subiculum** (this module) — a **child** of the hippocampus
    container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**The subiculum is ONE of the five children of the hippocampus.**
Consumers must **not** conflate the subiculum with the hippocampus
container.

The Subiculum / Fornix and White Matter Boundary
------------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **Subiculum** (this module) — the **grey-matter** archicortex
    — the **source** of the **postcommissural fornix** fibers.

*   **Fornix** (``.../left/white_matter/fornix/``) and
    **white_matter** (``.../left/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — the **subiculum** is the
**grey-matter structure**; the **fornix** and the **white_matter**
are the **white-matter tracts** that carry the subiculum's output
to the mammillary bodies and the anterior thalamic nuclei.
Consumers must **not** conflate the two.

The Subiculum / Rhinencephalon Boundary
---------------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **Subiculum** (this module) — the **principal output** of the
    hippocampus.

*   **Rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — the **subiculum** is the
**principal output** of the memory/navigation archicortex; the
**rhinencephalon** is the **olfactory lobe**. Consumers must
**not** conflate the two.

The Subiculum / Amygdala Boundary
---------------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **Subiculum** (this module) — a **subfield** of the
    **memory/navigation** container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; the **subiculum** is a **child of the
hippocampus** container. Consumers must **not** conflate the two.

The Subiculum / Memory Software Layer Boundary
----------------------------------------------
This is the **brain structure vs. software store** boundary:

*   **Subiculum** (this module) — the **brain structure** that
    subserves the principal-output contribution to episodic memory.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — the **subiculum** is the **brain
region**; the **``memory/`` package** is the **software store**.
Consumers must **not** conflate the two.

The Subiculum / SLEA Boundary
-----------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Subiculum** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The subiculum is NOT part of the SLEA continuum.** It is a
**memory/navigation** structure, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
subiculum.

Function in the Human Brain
---------------------------
The subiculum's functions are **principal output**, **mammillary-
body output**, and **prefrontal and parahippocampal output** —
**NOT head-direction / spatial processing and NOT fear-output**:

*   **Principal Output (CA1 → Subiculum):** The **subiculum** is
    the **principal output** of the hippocampal formation — it
    **receives** the **CA1** projection and **relays** it to the
    **parahippocampal region**, the **mammillary bodies**, and the
    **prefrontal cortex**. This is the **output-relay** substrate
    of the hippocampal formation.

*   **Mammillary-Body Output (Postcommissural Fornix):** The
    **proximal subiculum** projects to the **mammillary bodies**
    via the **postcommissural fornix** — the **Papez-circuit**
    limb of the hippocampal output. This is the **mammillary-body**
    substrate of the subiculum.

*   **Prefrontal Output:** The **proximal subiculum** projects to
    the **prefrontal cortex** — the **prefrontal** access to the
    hippocampal episodic and spatial representations. This is the
    **prefrontal** substrate of the subiculum.

*   **Parahippocampal Output:** The **distal subiculum** projects
    to the **parahippocampal region** (the entorhinal cortex, the
    perirhinal cortex, and the parahippocampal gyrus) — the
    **cortical return** of the hippocampal output to the
    parahippocampal region. This is the **parahippocampal**
    substrate of the subiculum.

*   **NOT a neural processor in the classical sense.** The
    **subiculum** is the **principal output** of the hippocampus —
    it **relays** the **episodic and spatial** representations,
    but it does **not** produce the **fear-output** or the
    **autonomic and behavioral** fear responses. The **fear-output**
    is the **central nucleus**; the **fear-learning** structures
    are the **basolateral nuclei**.

**The unifying theme:** the subiculum is the **principal output**
of the **hippocampus** — the **subicular-complex** subfield that
anchors **mammillary-body output**, **prefrontal output**, and
**parahippocampal output**. It is **SLEA-free**,
**memory/navigation**, and **NOT the fear-output structure** — the
**fear-output** is the **central nucleus**, the **fear-learning**
structures are the **basolateral nuclei**, and the **subiculum** is
the **principal output** of the **memory/navigation** container.

Associated Disorders
--------------------
The subiculum has **no named "subiculum syndrome"** in the narrow
sense, but its clinical associations are **well-documented**:

*   **Alzheimer's Disease (Early Subicular Pathology):** The
    **subiculum** shows **neurofibrillary tangles** and **cell
    loss** in **Alzheimer's disease** — it is part of the **early**
    affected **medial temporal lobe** circuit (the **entorhinal
    cortex** is the **earliest** affected structure; the
    **subiculum** is **adjacent** and **downstream**).
    **Subiculum involvement** is **well-documented** and is part
    of the **early** Alzheimer's pathology of the medial temporal
    lobe.

*   **Temporal Lobe Epilepsy (Subicular-Complex Involvement):**
    The **subiculum** is part of the **subicular complex** involved
    in **temporal lobe epilepsy** — the **subicular complex**
    shows **cell loss** and **network reorganization** in
    **Ammon's horn sclerosis**. **Subiculum involvement** is
    **well-documented** as part of the **sclerotic** circuit.

*   **Anterograde Amnesia (Medial Temporal Lobe Amnesia — via the
    Hippocampus):** Bilateral **hippocampal** damage (e.g., patient
    **H.M.**) — including **subicular** damage — produces
    **anterograde amnesia** — the **inability** to form **new
    episodic memories**, with **preserved** short-term memory and
    **preserved** procedural memory. The **subiculum** is the
    **principal-output** substrate of this amnesia.

*   **Spatial-Memory Deficits (Spatial-Navigation Impairment —
    Indirect):** The **subiculum's** principal-output contribution
    is **impaired** in conditions that affect the **subicular
    complex** — **spatial-memory deficits** and
    **spatial-navigation impairment** are **reported** in **early
    Alzheimer's disease** and in **aging**. The **subiculum** is
    the **output substrate** of these deficits.

*   **No Named "Subiculum Syndrome":** The **subiculum** is a
    **subfield of the subicular complex**, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **well-documented** for
    **Alzheimer's disease** and **temporal lobe epilepsy**, and
    **indirect** for **spatial-memory deficits**.

**What is NOT here:** The **subiculum** is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala — basolateral nuclei +
central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**well-documented** for **Alzheimer's disease** and **temporal lobe
epilepsy**, and **indirect** for **spatial-memory deficits**.

Lateralization Notes
--------------------
This is the **left** subiculum module. The **subiculum** is
**bilaterally symmetric** and **partially lateralized** — and it
carries **NO warning**:

*   **Bilateral Subiculum Function:** Each hemisphere has its own
    subiculum, with **ipsilateral** and **bilateral** connections
    to CA1, the presubiculum, the entorhinal cortex, the
    mammillary bodies, the prefrontal cortex, and the contralateral
    subiculum. The two sides are **functionally symmetric** for
    **basic memory and navigation**.

*   **Partial Lateralization (Well-Documented — Verbal vs.
    Spatial):** The **left** subiculum is **more involved in
    verbal** episodic memory (word lists, stories, verbal
    recognition); the **right** subiculum is **more involved in
    spatial/nonverbal** episodic memory (spatial layouts, faces,
    nonverbal recognition). This is **well-documented**, **not
    contested**, and is documented in the **medial temporal lobe
    module** (not at the subiculum level).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    **subiculum** is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the subiculum.

*   **NO Amygdala-Lateralization Warning of their own (the
    subiculum is the PRINCIPAL OUTPUT, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output)
    and the **basolateral nuclei** (fear-learning). The
    **subiculum** is the **principal output** of the
    memory/navigation container — consumers must **not** conflate
    it with the **whole amygdala** or with the **central
    nucleus**.

**A consumer that assumes "left subiculum = right subiculum" will
be structurally correct** — the two sides are **symmetric** and
**partially lateralized** (the lateralization is documented in the
medial temporal lobe module). The **subiculum** is a
**strict-mirror pair with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cornu_ammonis/ca1/``, ``.../cornu_ammonis/ca2/``,
    ``.../cornu_ammonis/ca3/``, ``.../cornu_ammonis/ca4/``,
    ``.../hippocampus/dentate_gyrus/``,
    ``.../hippocampus/presubiculum/``,
    ``.../hippocampus/parasubiculum/``,
    ``.../medial_temporal_lobe/amygdala/``,
    ``.../left/cortex/temporal/gyri/entorhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/perirhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/parahippocampal_gyrus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/cortex/rhinencephalon/``, ``memory/``, or any other
    container. The **subiculum**'s relationships to CA1, CA2, CA3,
    CA4, the dentate gyrus, the presubiculum, the parasubiculum,
    the amygdala, the entorhinal cortex, the parahippocampal
    region, the fornix, the rhinencephalon, and the ``memory/``
    package are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **layers
    (molecular, pyramidal-cell, polymorphic)** and the **proximal /
    distal subdivisions** of the subiculum are documented as
    **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve layer-level or subdivision-level
    detail through the references.
*   **PRINCIPAL OUTPUT of the hippocampus — NOT a head-direction /
    spatial subfield.** The **subiculum** is the **principal
    output** of the hippocampus. The **presubiculum** (sibling)
    and the **parasubiculum** (sibling) are **head-direction /
    spatial-processing** subfields of the subicular complex.
    Consumers must **not** conflate the subiculum with the
    presubiculum or the parasubiculum.
*   **SUBICULAR COMPLEX — PROSE, not a structural container.** The
    **subicular complex** is the **functional grouping** of the
    **subiculum**, the **presubiculum**, and the **parasubiculum**.
    Consumers must **not** assume a `subicular_complex/` container
    exists.
*   **NOT the presubiculum — the presubiculum is the SIBLING
    subicular-complex head-direction subfield.** Consumers must
    **not** conflate the subiculum with the presubiculum.
*   **NOT the parasubiculum — the parasubiculum is the SIBLING
    subicular-complex head-direction subfield.** Consumers must
    **not** conflate the subiculum with the parasubiculum.
*   **NOT CA1 — CA1 PROJECTS TO the subiculum; the subiculum IS NOT
    CA1.** The **CA1** is a **CA field** of the cornu ammonis; the
    **subiculum** is a **sibling subfield** of the hippocampus
    (part of the subicular complex). Consumers must **not** conflate
    the subiculum with CA1.
*   **NOT CA2, CA3, or CA4 — those are the CA fields of the cornu
    ammonis.**
*   **NOT the cornu ammonis — the cornu ammonis is the CA-field
    container.** Consumers must **not** conflate the subiculum
    with the cornu ammonis.
*   **NOT the dentate gyrus — the dentate gyrus is the
    pattern-separation subfield.**
*   **NOT the entorhinal cortex — the entorhinal cortex is
    CORTICAL, wired under ``cortex/temporal/gyri/``.** The
    **subiculum** → entorhinal cortex projection is the **source**
    of the projection; the **entorhinal cortex** is the
    **target**.
*   **NOT the hippocampus container — the subiculum is a CHILD of
    the hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; the **subiculum** is the
    **archicortex**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** The **subiculum** is the **grey-matter
    archicortex** — the **source** of the **postcommissural
    fornix** fibers.
*   **NOT the rhinencephalon.** The **subiculum** is **not** an
    olfactory structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    **subiculum** is **not** an extended-amygdala component, and it
    carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; the **subiculum** is
    the **principal output** of the **memory/navigation**
    container.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; the **subiculum** is the
    **brain structure**. Consumers must **not** conflate the two.
*   **NOT a single uniform layer — MULTIPLE layers and proximal /
    distal subdivisions.** The **layers** and **subdivisions** are
    **prose**, not structural children.
*   **No ``AREA_PATHS`` hop.** The **subiculum** is a local leaf
    under the hippocampus, not a cross-listed leaf.
*   **No nested cross-listing.** The **subiculum** has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with right subiculum — strict mirror with
    NO warning.** Left and right subiculum modules are
    **structurally identical** — same **leaf** status, same
    **principal-output** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus import subiculum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "medial_temporal_lobe.hippocampus.subiculum"
    )

**Do not** assume the subiculum is **CA1**. **CA1 projects to the
subiculum** — the **subiculum** is the **output target** of CA1
and the **output relay** of the hippocampus. They are **different
structures** — **CA1** is a **CA field** of the cornu ammonis;
the **subiculum** is a **sibling subfield** of the hippocampus.

**Do not** assume the subiculum is the **presubiculum** or the
**parasubiculum**. Those are the **sibling** subicular-complex
**head-direction** subfields — the **presubiculum → MEC layer
III**; the **parasubiculum → MEC layer II**. The **subiculum** is
the **principal output**.

**Do not** assume the subiculum is the **dentate gyrus**. The
**dentate gyrus** is the **pattern-separation** subfield; the
**subiculum** is the **principal output**.

**Do not** assume the subiculum is **CA2**, **CA3**, or **CA4**.
Those are the **CA fields** of the cornu ammonis; the **subiculum**
is a **subicular-complex** subfield.

**Do not** assume the subiculum is the **cornu ammonis**. The
**cornu ammonis** is the **CA-field container**; the **subiculum**
is a **sibling** of the cornu ammonis under the hippocampus.

**Do not** assume the subiculum is the **entorhinal cortex**. The
**entorhinal cortex** is **cortical** — wired under
``cortex/temporal/gyri/`` — and is the **target** of the
subiculum's principal projection. The **subiculum** is the
**source** of the projection.

**Do not** assume the subiculum is the **hippocampus container**.
The **hippocampus** container contains the **subiculum** and the
other four subfields — the **subiculum** is **one** of those five
children.

**Do not** assume the subiculum is the **parahippocampal region**.
The **entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; the
**subiculum** is the **archicortex**.

**Do not** assume the subiculum is the **fornix** or the
**white_matter**. Those are **white-matter tracts**; the
**subiculum** is the **grey-matter archicortex** — the **source**
of the **postcommissural fornix** fibers.

**Do not** assume the subiculum is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; the
**subiculum** is the **principal output** of the memory/navigation
archicortex.

**Do not** assume the subiculum is the **``memory/`` software
package**. The **``memory/`` package** is the **software store**;
the **subiculum** is the **brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the subiculum. **The
subiculum is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

**Do not** assume a `subicular_complex/` container exists. The
**subicular complex** is **prose** — the **subiculum**,
**presubiculum**, and **parasubiculum** are **separate leaves**
under the hippocampus.

Iterating the subiculum's (empty) children (recommended consumer
pattern)::

    SUBICULUM_CHILDREN = ()
    # The subiculum is a leaf. The layers (molecular, pyramidal-cell,
    # polymorphic) and the proximal / distal subdivisions are prose,
    # not modules.

Reaching CA1 (recommended consumer pattern — the output source)::

    # CA1 is the PRINCIPAL-OUTPUT subfield of the cornu ammonis —
    # the SOURCE that projects to the subiculum:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca1
    #
    # CA1 projects to the subiculum; the subiculum is the OUTPUT
    # TARGET of CA1 and the OUTPUT RELAY of the hippocampus.

Reaching the presubiculum sibling (recommended consumer pattern —
the subicular-complex head-direction sibling)::

    # The presubiculum is the SIBLING subicular-complex
    # head-direction subfield — under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.presubiculum
    #
    # The subiculum is the PRINCIPAL OUTPUT; the presubiculum is a
    # head-direction / spatial-processing subfield that projects
    # principally to MEC layer III.

Reaching the parasubiculum sibling (recommended consumer pattern —
the subicular-complex head-direction sibling)::

    # The parasubiculum is the SIBLING subicular-complex
    # head-direction subfield — under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.parasubiculum
    #
    # The subiculum is the PRINCIPAL OUTPUT; the parasubiculum is a
    # head-direction / spatial-processing subfield that projects
    # principally to MEC layer II (the grid-cell layer).

Reaching the dentate gyrus sibling (recommended consumer pattern —
the pattern-separation subfield)::

    # The dentate gyrus is the PATTERN-SEPARATION subfield — the
    # sibling of the subiculum under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
    #
    # The dentate gyrus is the pattern-separation subfield; the
    # subiculum is the principal output.

Reaching the cornu ammonis (recommended consumer pattern — the
sibling container)::

    # The cornu ammonis is the CA-FIELD CONTAINER — the SIBLING of
    # the subiculum under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
    #
    # The subiculum is a subicular-complex subfield; the cornu
    # ammonis is the CA-field container.

Reaching the entorhinal cortex (recommended consumer pattern — the
target of the subiculum projection)::

    # The entorhinal cortex is the CORTICAL TARGET of the
    # subiculum projection:
    #
    #   cortex.temporal.gyri.entorhinal_cortex
    #
    # The subiculum is the SOURCE of the projection; the entorhinal
    # cortex is the TARGET.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the subiculum
    # and the other four subfields:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # The subiculum is ONE of the five children of the hippocampus.

Reaching the parahippocampal region (recommended consumer pattern —
the cortical interface)::

    # The parahippocampal region (entorhinal cortex, perirhinal
    # cortex, parahippocampal gyrus) is the CORTICAL INTERFACE that
    # feeds the hippocampus and receives the subiculum output:
    #
    #   cortex.temporal.gyri.entorhinal_cortex
    #   cortex.temporal.gyri.perirhinal_cortex
    #   cortex.temporal.gyri.parahippocampal_gyrus
    #
    # The subiculum is the ARCHICORTEX; the parahippocampal region
    # is the CORTICAL INTERFACE.

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
    # The subiculum is the BRAIN STRUCTURE; the ``memory/`` package
    # is the SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE the subiculum is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT subiculum children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # The subiculum is the principal output of the
    # MEMORY/NAVIGATION container; the central nucleus and the
    # basolateral nuclei are the FEAR structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
the subiculum is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # subiculum:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The subiculum is SLEA-FREE.

Layer- and subdivision-level detail (not wired — consult
references)::

    # The subiculum's layers and subdivisions are prose, not
    # modules:
    #   molecular layer         -> superficial layer
    #   pyramidal-cell layer    -> subicular pyramidal cells (output
    #                              neurons)
    #   polymorphic layer       -> deep layer
    #   proximal subiculum      -> projects preferentially to the
    #                              prefrontal cortex and the
    #                              mammillary bodies (via the
    #                              postcommissural fornix)
    #   distal subiculum        -> projects preferentially to the
    #                              parahippocampal region (entorhinal
    #                              cortex, perirhinal cortex,
    #                              parahippocampal gyrus)
    #
    # Do not attempt to resolve these as sub-paths of the
    # subiculum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        sub_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.subiculum"
        )
        # resolve sub_path through the memory/recall layer

References
----------
*   **Canonical subicular complex anatomy:** Amaral, D.G., Witter,
    M.P. (1989). "The three-dimensional organization of the
    hippocampal formation: a review of anatomical data."
    *Neuroscience* 31:571–591. (Definitive subicular complex
    anatomy; subiculum, presubiculum, parasubiculum.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; subiculum.)
*   **Subiculum output anatomy:** Witter, M.P. (2006).
    "Connections of the subiculum of the rat: topography in
    relation to columnar and laminar organization." *Behavioural
    Brain Research* 174:251–264. (Definitive subiculum output
    anatomy; proximal vs. distal subdivisions; parahippocampal,
    prefrontal, and mammillary-body targets.)
*   **CA1 → subiculum projection:** Amaral, D.G., Dolorfo, C.,
    Alvarez-Royo, P. (1991). "Organization of CA1 projections to
    the subiculum: a PHA-L analysis in the rat." *Hippocampus*
    1:415–435. (CA1 → subiculum projection — the subiculum as the
    output target of CA1.)
*   **Subiculum → mammillary bodies (postcommissural fornix):**
    Swanson, L.W., Cowan, W.M. (1977). "An autoradiographic study
    of the organization of the efferent connections of the
    hippocampal formation in the rat." *Journal of Comparative
    Neurology* 172:49–84. (Subiculum → mammillary-body projection
    — the postcommissural fornix.)
*   **Subiculum → prefrontal cortex:** Jay, T.M., Witter, M.P.
    (1991). "Distribution of hippocampal CA1 and subicular
    efferents in the prefrontal cortex of the rat studied by means
    of anterograde transport of Phaseolus vulgaris-leucoagglutinin."
    *Journal of Comparative Neurology* 313:574–586. (Subiculum →
    prefrontal cortex projection.)
*   **Subiculum → parahippocampal region:** Witter, M.P. (1993).
    "Organization of the entorhinal-hippocampal system: a review
    of current anatomical data." *Hippocampus* 3:33–44.
    (Subiculum → entorhinal / parahippocampal projection.)
*   **Alzheimer's disease and the subicular complex:** Braak, H.,
    Braak, E. (1991). "Neuropathological stageing of
    Alzheimer-related changes." *Acta Neuropathologica*
    82:239–259. (Early entorhinal / subicular pathology —
    subiculum involvement.)
*   **Temporal lobe epilepsy and the subicular complex:** Mathern,
    G.W., Babb, T.L., Vickrey, B.G., Melendez, M., Pretorius, J.K.
    (1995). "The clinical-pathogenic mechanisms of hippocampal
    neuron loss and surgical outcomes in temporal lobe epilepsy."
    *Brain* 118:105–118. (Subicular-complex involvement in
    Ammon's horn sclerosis.)
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
*   **Amygdala (contrast — the subiculum is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the hippocampus memory circuit.)
*   **SLEA (contrast — the subiculum is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    subiculum.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Subiculum in overview.)
*   NeuroNames — Subiculum (left); FMA — Subiculum (left member).
"""