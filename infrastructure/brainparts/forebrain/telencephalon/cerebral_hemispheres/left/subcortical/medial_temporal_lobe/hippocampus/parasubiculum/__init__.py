"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.parasubiculum
========================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── medial_temporal_lobe
                    └── hippocampus
                        └── parasubiculum   <-- THIS MODULE

**Primary synonym:** Parasubiculum (left); PaS; para-subiculum;
parasubicular area; **part of the subicular complex**.
**Cytoarchitectonic designation:** **Not a Brodmann area** (in the
classical numbering; sometimes assigned as a subdivision of area
28 or 27 in older schemes — see references). A **leaf subfield**
of the **hippocampus** — a **cortical region of the subicular
complex**, **enriched in head-direction cells**, and a **major
input to the medial entorhinal cortex (MEC) layer II** (the
grid-cell layer).
**Part of:** The **hippocampus** container — a **subfield of the
subicular complex**. The **parasubiculum** is a **head-direction
and spatial-processing** subfield that relays **head-direction and
spatial** signals to the **medial entorhinal cortex**.
**Structural parent:** ``.../hippocampus/`` → **direct child** of
the hippocampus container.
**Structural children:** **None.** This is a **leaf** module. The
**layers (II–VI)** and the **head-direction cells** of the
parasubiculum are documented as **prose**, not as structural
children.
**Boundary status (HEAD-DIRECTION / SPATIAL-PROCESSING subfield —
NOT the principal-output subfield and NOT the pattern-separation
or pattern-completion subfields):** **Boundary case — the
parasubiculum is a HEAD-DIRECTION and SPATIAL-PROCESSING subfield
of the subicular complex, NOT the principal-output subfield and
NOT the pattern-separation or pattern-completion subfields.** The
**subiculum** sibling (``.../subiculum/``) is the **principal
output** of the hippocampus to the parahippocampal region, the
mammillary bodies, and the prefrontal cortex — **CA1 projects to
the subiculum**. The **dentate gyrus** sibling
(``.../dentate_gyrus/``) is the **pattern-separation** subfield.
The **CA3** subfield (``.../cornu_ammonis/ca3/``) is the
**pattern-completion** subfield. The **parasubiculum** (here) is a
**head-direction / spatial-processing** subfield of the
**subicular complex** — it is **neither** the principal output,
**nor** the pattern-separation subfield, **nor** the
pattern-completion subfield. Consumers must **not** conflate the
parasubiculum with the subiculum, the dentate gyrus, or the CA
fields.
**Boundary status (SUBICULAR COMPLEX — the subicular complex is
PROSE, not a structural container):** **Boundary case — the
parasubiculum is part of the SUBICULAR COMPLEX, and the subicular
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
**Boundary status (NOT the presubiculum — the presubiculum is the
SIBLING subicular-complex head-direction subfield, with a
DIFFERENT MEC target layer):** **Boundary case — the
parasubiculum is NOT the presubiculum; the presubiculum is the
SIBLING subicular-complex head-direction subfield, with a
DIFFERENT MEC target layer.** The **presubiculum**
(``.../presubiculum/``) is a **sibling** of the parasubiculum
under the hippocampus — **also** a **head-direction** subfield of
the subicular complex. **The distinction between the two is the
principal layer of their entorhinal-cortex projection:**
*   **Parasubiculum** (here) projects principally to the **medial
    entorhinal cortex (MEC) layer II** — the **grid-cell layer**
    (the layer containing **stellate cells** that are the
    **grid cells** of the entorhinal cortex).
*   **Presubiculum** (sibling) projects principally to the
    **medial entorhinal cortex (MEC) layer III** — the
    **pyramidal-cell layer** that projects to **CA1** and the
    **subiculum**.

  **They are SIBLINGS under the hippocampus, and they are
  DIFFERENT subfields of the subicular complex.** Consumers must
  **not** conflate the parasubiculum with the presubiculum — the
  **parasubiculum → MEC layer II**; the **presubiculum → MEC
  layer III**.
**Boundary status (NOT the subiculum — the subiculum is the
principal OUTPUT of the hippocampus):** **Boundary case — the
parasubiculum is NOT the subiculum; the subiculum is the principal
OUTPUT of the hippocampus.** The **subiculum**
(``.../hippocampus/subiculum/``) is the **principal output** of
the hippocampus to the parahippocampal region, the mammillary
bodies (via the fornix), and the prefrontal cortex — **CA1
projects to the subiculum**. The **parasubiculum** (here) is a
**head-direction / spatial-processing** subfield of the
**subicular complex** — it is **not** the principal output.
Consumers must **not** conflate the parasubiculum with the
subiculum.
**Boundary status (NOT the dentate gyrus — the dentate gyrus is the
pattern-separation subfield):** **Boundary case — the
parasubiculum is NOT the dentate gyrus.** The **dentate gyrus**
(``.../hippocampus/dentate_gyrus/``) is the **pattern-separation**
subfield (granule cells; adult neurogenesis; mossy-fiber source).
The **parasubiculum** (here) is a **head-direction /
spatial-processing** subfield of the subicular complex. Consumers
must **not** conflate the parasubiculum with the dentate gyrus.
**Boundary status (NOT CA1, CA2, CA3, or CA4 — those are the CA
fields of the cornu ammonis):** **Boundary case — the
parasubiculum is NOT CA1, CA2, CA3, or CA4.** Those are the **CA
fields** of the **cornu ammonis** container — CA1 (principal
output), CA2 (social memory), CA3 (pattern completion), CA4
(dentate hilus). The **parasubiculum** (here) is a **subfield of
the subicular complex**, **not** a CA field. Consumers must **not**
conflate the parasubiculum with the CA fields.
**Boundary status (NOT the cornu ammonis — the cornu ammonis is the
CA-field container):** **Boundary case — the parasubiculum is NOT
the cornu ammonis.** The **cornu ammonis** (``.../cornu_ammonis/``)
is the **CA-field container** (CA1–CA4). The **parasubiculum**
(here) is a **sibling** of the cornu ammonis under the
hippocampus — a **subfield of the subicular complex**. **They are
SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.**
**Boundary status (NOT the entorhinal cortex — the entorhinal
cortex is CORTICAL, wired under ``cortex/temporal/gyri/``):
**Boundary case — the parasubiculum is NOT the entorhinal cortex;
the entorhinal cortex is CORTICAL and is wired under
``.../left/cortex/temporal/gyri/entorhinal_cortex/``.** The
**entorhinal cortex** is the **cortical interface** that **feeds**
the hippocampus (the **perforant-path** source), and it is **the
target** of the parasubiculum's principal projection. The
**parasubiculum** (here) is an **archicortex / subicular-complex
subfield** that **projects TO** the entorhinal cortex. **They are
DIFFERENT STRUCTURES** — the **parasubiculum** is the **source**
of the projection; the **entorhinal cortex** is the **target**
(the **MEC layer II** grid-cell layer). Consumers must **not**
conflate the parasubiculum with the entorhinal cortex.
**Boundary status (NOT the hippocampus container — the
parasubiculum is a CHILD of the hippocampus):** **Boundary case —
the parasubiculum is a CHILD of the hippocampus container, not the
container itself.** The **hippocampus** container contains the
**cornu ammonis**, the **dentate gyrus**, the **parasubiculum**,
the **presubiculum**, and the **subiculum** — the
**parasubiculum** is **one** of those five children. Consumers
must **not** conflate the parasubiculum with the hippocampus
container.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the
parasubiculum is NOT the parahippocampal region.** The
**parahippocampal region** (the **entorhinal cortex**, the
**perirhinal cortex**, and the **parahippocampal gyrus**) is
**cortical** — it is wired under ``.../left/cortex/temporal/
gyri/`` and is **outside** the hippocampus container. The
**parasubiculum** (here) is an **archicortex /
subicular-complex** subfield. Consumers must **not** conflate the
parasubiculum with the parahippocampal region — the
parahippocampal region is **cortex/**; the parasubiculum is
**subcortical/medial_temporal_lobe/**.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the parasubiculum is
NOT the fornix or the white matter; the fornix and the white_matter
are WHITE-MATTER structures.** The **fornix**
(``.../left/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../left/white_matter/``) is the **white-matter
infrastructure**. The **parasubiculum** (here) is the
**grey-matter archicortex**. Consumers must **not** conflate the
two.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the parasubiculum is NOT the rhinencephalon.** The
**rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
olfactory bulb, olfactory tract, piriform cortex, periamygdaloid
cortex, anterior olfactory nucleus, and uncus — is the **cortical
olfactory lobe**. The **parasubiculum** (here) is a
**head-direction / spatial-processing** subfield of the subicular
complex — it is **not** an olfactory structure. Consumers must
**not** conflate the two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the
parasubiculum is NOT the amygdala; the amygdala is the
FEAR/EMOTION/SALIENCE container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), the
**lateral nucleus** (sensory input), and the **medial nucleus**
(olfactory/pheromone). The **parasubiculum** (here) is a
**subfield** of the **memory/navigation** container. Consumers
must **not** conflate the parasubiculum with the amygdala.
**Boundary status (SLEA-FREE — the parasubiculum is NOT an
extended-amygdala component):** **Boundary case — the
parasubiculum is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala)
and to the **BNST**, **ventral pallidum**, and **nucleus accumbens**
(wired elsewhere). The **parasubiculum** is an
**episodic/declarative-memory and spatial-navigation** structure —
it is **NOT** an extended-amygdala component, and it carries **NO
SLEA warning**. Consumers must **not** import the SLEA warning
into the parasubiculum — it is **SLEA-free**.
**Boundary status (NOT the memory software layer — the
parasubiculum is the BRAIN STRUCTURE, not the ``memory/``
package):** **Boundary case — the parasubiculum is the BRAIN
STRUCTURE, NOT the ``memory/`` software package.** The
**``memory/`` package** (``memory/stores/`` — episodic, semantic,
procedural, working; ``memory/backends/`` — chroma, in_memory) is
the **software memory layer** of the simulation. The
**parasubiculum** (here) is the **brain structure** that
**subserves** the **head-direction / spatial** contribution to
episodic memory. Consumers must **not** conflate the two — the
**brain structure** is wired here; the **software store** is wired
under ``memory/``.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
parasubiculum is NOT the fear-output or the fear-learning
structures.** The **central nucleus** (fear-output), the
**basolateral nuclei** (fear-learning), and the **basomedial
nuclei** (fear-modulatory) are **amygdala** children. The
**parasubiculum** is a **head-direction / spatial-processing**
subfield of the **memory/navigation** container — it is **not** a
fear-output or fear-learning structure. Consumers must **not**
conflate the parasubiculum with the **amygdala fear circuit**.
**Boundary status (NOT a single uniform layer — MULTIPLE layers,
II–VI):** **Boundary case — the parasubiculum is a HETEROGENEOUS
cortical region with MULTIPLE layers (II–VI), not a single uniform
layer.** The **layers** are functionally distinct — **layer II**
contains the **principal neurons** that project to the **medial
entorhinal cortex layer II**; **layer III** contains the
**pyramidal cells** that project to other targets (including the
entorhinal cortex and the subiculum); **layers V–VI** contain the
**deep** neurons that project **subcortically**. The tree wires
the **parasubiculum** as a **single leaf** under the hippocampus
— the **layers** are **prose**, not structural children.
Consumers that need **layer-level** resolution should consult the
references, not the tree.

Overview
--------
The parasubiculum is a **head-direction and spatial-processing**
subfield of the **subicular complex** — a **cortical region** of
the hippocampus that contains **head-direction cells**, receives
**head-direction and spatial** input, and **projects principally
to the medial entorhinal cortex (MEC) layer II** (the grid-cell
layer). It is a **leaf** module under the hippocampus container,
the **sibling of the cornu ammonis, the dentate gyrus, the
presubiculum, and the subiculum**, and the **grey-matter
substrate** of **head-direction and spatial-navigation** signals
routed to the entorhinal-hippocampal loop.

**The parasubiculum is a HEAD-DIRECTION and SPATIAL-PROCESSING
subfield of the subicular complex.** The **subiculum** (sibling)
is the **principal output** of the hippocampus. The **dentate
gyrus** (sibling) is the **pattern-separation** subfield. **CA3**
is the **pattern-completion** subfield. **CA1** is the **principal
output** of the cornu ammonis. **CA2** is the **social-memory**
subfield. **CA4** is the **dentate hilus**. The **parasubiculum**
is a **head-direction / spatial-processing** subfield.

**The subicular complex is PROSE, not a structural container.**
The **subicular complex** is the **functional grouping** of the
**subiculum**, the **presubiculum**, and the **parasubiculum**
(some schemes also include the **postsubiculum**). The tree **does
not** wire a `subicular_complex/` container — the three subfields
are **separate leaves** under the hippocampus. Consumers must
**not** assume a `subicular_complex/` container exists.

**The parasubiculum is NOT the presubiculum.** Both are
**head-direction** subfields of the subicular complex, but their
**entorhinal-cortex targets differ**: the **parasubiculum**
projects principally to **MEC layer II** (the **grid-cell
layer**); the **presubiculum** projects principally to **MEC layer
III** (the **pyramidal-cell layer** that projects to CA1 and the
subiculum). **They are SIBLINGS under the hippocampus.**

**The parasubiculum is NOT the subiculum.** The **subiculum** is
the **principal output** of the hippocampus; the **parasubiculum**
is a **head-direction / spatial-processing** subfield.

**The parasubiculum is NOT the entorhinal cortex.** The
**entorhinal cortex** is **cortical** — wired under
``cortex/temporal/gyri/`` — and it is the **target** of the
parasubiculum's principal projection. The **parasubiculum** is the
**source** of the projection; the **entorhinal cortex** is the
**target**.

**The parasubiculum is NOT the cornu ammonis.** The **cornu
ammonis** is the **CA-field container** (CA1–CA4); the
**parasubiculum** is a **sibling** of the cornu ammonis under the
hippocampus.

**The parasubiculum is NOT the dentate gyrus.** The **dentate
gyrus** is the **pattern-separation** subfield; the
**parasubiculum** is a **head-direction / spatial-processing**
subfield of the subicular complex.

**The parasubiculum is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**. The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The parasubiculum is the BRAIN STRUCTURE, not the ``memory/``
software package.** The **``memory/`` package** is the **software
memory layer**. The **parasubiculum** is the **brain region** whose
function the episodic store models. **They are DIFFERENT LAYERS.**

**The parasubiculum is a paired structure.** Each hemisphere has
its own parasubiculum, with **ipsilateral** and **bilateral**
connections to the presubiculum, the subiculum, the medial
entorhinal cortex, and the contralateral parasubiculum. The two
sides are **bilaterally symmetric** and **partially lateralized**
— the **left** parasubiculum is more involved in **verbal** spatial
processing, and the **right** parasubiculum is more involved in
**spatial/nonverbal** navigation. This is **partial**, **less
well-documented than the hippocampus lateralization**, and
documented in the **medial temporal lobe module** (not at the
parasubiculum level). See *Lateralization Notes*.

Layer Composition (prose, not structural children)
--------------------------------------------------
The parasubiculum is a **heterogeneous cortical region** —
documented as **prose**, not as structural children:

*   **Layer II** — the **principal-neuron** layer containing the
    cells that project to the **medial entorhinal cortex (MEC)
    layer II** — the **grid-cell layer** (stellate cells in MEC
    layer II are the grid cells).

*   **Layer III** — the **pyramidal-cell** layer containing cells
    that project to other targets (including the entorhinal
    cortex and the subiculum).

*   **Layers V–VI** — the **deep** layers containing cells that
    project **subcortically** (to the thalamus and other targets).

**These layers are prose, not structural children.** The tree wires
the **parasubiculum** as a **single leaf** under the hippocampus —
the **layers** are **prose**, not structural children. Consumers
that need **layer-level** resolution should consult the references,
not the tree.

The Parasubiculum / Presubiculum Boundary
-----------------------------------------
This is the **sibling subicular-complex head-direction** boundary —
the most consequential one:

*   **Parasubiculum** (this module) — the **subicular-complex
    head-direction** subfield that projects principally to **MEC
    layer II** (the **grid-cell layer**).

*   **Presubiculum** (``.../presubiculum/``) — the **sibling
    subicular-complex head-direction** subfield that projects
    principally to **MEC layer III** (the **pyramidal-cell
    layer** that projects to CA1 and the subiculum).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
subfields of the subicular complex.** Consumers must **not**
conflate the two — the **parasubiculum → MEC layer II**; the
**presubiculum → MEC layer III**.

The Parasubiculum / Subiculum Boundary
--------------------------------------
This is the **head-direction subfield vs. principal output**
boundary:

*   **Parasubiculum** (this module) — a **head-direction /
    spatial-processing** subfield of the subicular complex.

*   **Subiculum** (``.../hippocampus/subiculum/``) — the
    **principal output** of the hippocampus (CA1 → subiculum →
    parahippocampal region, mammillary bodies, prefrontal cortex).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES** — the **parasubiculum** is a **head-direction /
spatial-processing** subfield; the **subiculum** is the
**principal output**. Consumers must **not** conflate the two.

The Parasubiculum / Dentate Gyrus Boundary
------------------------------------------
This is the **head-direction subfield vs. pattern-separation
subfield** boundary:

*   **Parasubiculum** (this module) — a **head-direction /
    spatial-processing** subfield of the subicular complex.

*   **Dentate gyrus** (``.../hippocampus/dentate_gyrus/``) — the
    **pattern-separation** subfield (granule cells; adult
    neurogenesis; mossy-fiber source).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the two.

The Parasubiculum / Cornu Ammonis Boundary
------------------------------------------
This is the **subicular-complex subfield vs. CA-field container**
boundary:

*   **Parasubiculum** (this module) — a **subicular-complex
    subfield**.

*   **Cornu ammonis** (``.../cornu_ammonis/``) — the **CA-field
    container** (CA1–CA4).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the parasubiculum
with the cornu ammonis container.

The Parasubiculum / CA1, CA2, CA3, CA4 Boundary
-----------------------------------------------
This is the **subicular-complex subfield vs. CA field** boundary:

*   **Parasubiculum** (this module) — a **subicular-complex
    subfield**.

*   **CA1, CA2, CA3, CA4** (``.../cornu_ammonis/ca1/``,
    ``.../ca2/``, ``.../ca3/``, ``.../ca4/``) — the **CA fields**
    of the cornu ammonis.

**They are DIFFERENT STRUCTURES** — the **parasubiculum** is a
**subicular-complex** subfield; the **CA fields** are the
**cornu-ammonis** subfields. Consumers must **not** conflate the
parasubiculum with any CA field.

The Parasubiculum / Entorhinal Cortex Boundary
----------------------------------------------
This is the **source vs. target** boundary:

*   **Parasubiculum** (this module) — the **subicular-complex**
    subfield that **projects** to the medial entorhinal cortex.

*   **Entorhinal cortex** (``.../left/cortex/temporal/gyri/
    entorhinal_cortex/``) — the **cortical interface** that
    **receives** the parasubiculum projection (in **MEC layer
    II** — the grid-cell layer) and **feeds** the hippocampus via
    the **perforant path**.

**They are DIFFERENT STRUCTURES** — the **parasubiculum** is the
**source** of the projection; the **entorhinal cortex** is the
**target**. Consumers must **not** conflate the two.

The Parasubiculum / Hippocampus Boundary
----------------------------------------
This is the **child vs. container** boundary:

*   **Parasubiculum** (this module) — a **child** of the
    hippocampus container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**The parasubiculum is ONE of the five children of the
hippocampus.** Consumers must **not** conflate the parasubiculum
with the hippocampus container.

The Parasubiculum / Parahippocampal Region Boundary
---------------------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **Parasubiculum** (this module) — the **archicortex** (the
    subicular-complex subfield).

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../left/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus** (via the **perforant path**). The
**parasubiculum** **projects** to the entorhinal cortex, which is
part of the parahippocampal region. Consumers must **not** conflate
the **parasubiculum** with the **parahippocampal region** — the
parahippocampal region is **cortex/**; the parasubiculum is
**subcortical/medial_temporal_lobe/**.

The Parasubiculum / Fornix and White Matter Boundary
----------------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **Parasubiculum** (this module) — the **grey-matter**
    archicortex.

*   **Fornix** (``.../left/white_matter/fornix/``) and
    **white_matter** (``.../left/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — the **parasubiculum** is the
**grey-matter structure**; the **fornix** and the **white_matter**
are the **white-matter tracts**. Consumers must **not** conflate
the two.

The Parasubiculum / Rhinencephalon Boundary
-------------------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **Parasubiculum** (this module) — a **head-direction /
    spatial-processing** subfield of the subicular complex.

*   **Rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — the **parasubiculum** is a
**memory/navigation** archicortex; the **rhinencephalon** is the
**olfactory lobe**. Consumers must **not** conflate the two.

The Parasubiculum / Amygdala Boundary
-------------------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **Parasubiculum** (this module) — a **subfield** of the
    **memory/navigation** container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; the **parasubiculum** is a **child of the
hippocampus** container. Consumers must **not** conflate the two.

The Parasubiculum / Memory Software Layer Boundary
--------------------------------------------------
This is the **brain structure vs. software store** boundary:

*   **Parasubiculum** (this module) — the **brain structure** that
    subserves head-direction and spatial navigation.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — the **parasubiculum** is the
**brain region**; the **``memory/`` package** is the **software
store**. Consumers must **not** conflate the two.

The Parasubiculum / SLEA Boundary
---------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Parasubiculum** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The parasubiculum is NOT part of the SLEA continuum.** It is a
**memory/navigation** structure, and it carries **no SLEA
warning**. Consumers must **not** import the SLEA warning into the
parasubiculum.

Function in the Human Brain
---------------------------
The parasubiculum's functions are **head-direction**, **spatial
processing**, and **grid-cell-layer input to the medial entorhinal
cortex** — **NOT episodic-memory output and NOT fear-output**:

*   **Head-Direction (HD) Cells:** The **parasubiculum** contains
    **head-direction cells** — neurons that fire when the animal's
    head points in a **specific direction**, independent of
    location and of the animal's ongoing behavior. This is the
    **head-direction** substrate of spatial navigation.

*   **Spatial Processing:** The **parasubiculum** is involved in
    **spatial processing** — it **integrates** the head-direction
    signal with **location** and **context** information and
    **relays** it to the medial entorhinal cortex. This is the
    **spatial-processing** substrate of the subicular complex.

*   **Grid-Cell-Layer Input to MEC Layer II:** The
    **parasubiculum** projects principally to the **medial
    entorhinal cortex (MEC) layer II** — the **grid-cell layer**.
    The **grid cells** in MEC layer II are the **spatial** neurons
    that fire in a **hexagonal** pattern across the environment —
    the **grid-cell** spatial representation. The **parasubiculum
    → MEC layer II** projection is the **input** side of the
    grid-cell computation (the **grid-cell-layer** substrate).

*   **Theta-Rhythm Modulation:** The **parasubiculum** is
    **involved** in the **theta-rhythm** — the **network
    oscillation** that coordinates **spatial encoding** and
    **navigation**. This is the **temporal** substrate of the
    parasubiculum's spatial contribution.

*   **NOT a neural processor in the classical sense.** The
    **parasubiculum** is a **head-direction / spatial-processing**
    subfield — it **integrates** and **relays** the
    **head-direction and spatial** signals, but it does **not**
    produce the **fear-output** or the **autonomic and behavioral**
    fear responses. The **fear-output** is the **central
    nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**.

**The unifying theme:** the parasubiculum is a **head-direction and
spatial-processing** subfield of the **subicular complex** — the
**subicular-complex** subfield that anchors **head-direction**,
**spatial processing**, and the **grid-cell-layer input to the
medial entorhinal cortex**. It is **SLEA-free**,
**memory/navigation**, and **NOT the fear-output structure** — the
**fear-output** is the **central nucleus**, the **fear-learning**
structures are the **basolateral nuclei**, and the
**parasubiculum** is a **head-direction / spatial-processing**
subfield of the **memory/navigation** container.

Associated Disorders
--------------------
The parasubiculum has **no named "parasubiculum syndrome"** in the
narrow sense, but its clinical associations are **reported**:

*   **Alzheimer's Disease (Early Entorhinal-Subicular Pathology):**
    The **parasubiculum** shows **neurofibrillary tangles** and
    **cell loss** in **Alzheimer's disease** — it is part of the
    **early** affected **medial temporal lobe** circuit (the
    **entorhinal cortex** is the **earliest** affected structure;
    the **parasubiculum** is **adjacent** and **downstream**).
    **Parasubiculum involvement** is **reported** and is part of
    the **early** Alzheimer's pathology of the medial temporal
    lobe.

*   **Temporal Lobe Epilepsy (Subicular-Complex Involvement):**
    The **parasubiculum** is part of the **subicular complex**
    involved in **temporal lobe epilepsy** — the **subicular
    complex** shows **cell loss** and **network reorganization**
    in **Ammon's horn sclerosis**. **Parasubiculum involvement** is
    **reported** as part of the **sclerotic** circuit.

*   **Spatial-Memory Deficits (Head-Direction / Spatial-Navigation
    Impairment — Indirect):** The **parasubiculum's**
    head-direction and grid-cell-layer contributions are
    **impaired** in conditions that affect the **subicular
    complex** — **spatial-memory deficits** and
    **spatial-navigation impairment** are **reported** in
    **early Alzheimer's disease** and in **aging**. The
    **parasubiculum** is the **spatial substrate** of these
    deficits; its involvement is **indirect**, via the
    **entorhinal-hippocampal** spatial circuit.

*   **No Named "Parasubiculum Syndrome":** The **parasubiculum** is
    a **subfield of the subicular complex**, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **reported** for **Alzheimer's
    disease** and **temporal lobe epilepsy**, and **indirect** for
    **spatial-memory deficits**.

**What is NOT here:** The **parasubiculum** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**reported** for **Alzheimer's disease** and **temporal lobe
epilepsy**, and **indirect** for **spatial-memory deficits**.

Lateralization Notes
--------------------
This is the **left** parasubiculum module. The **parasubiculum**
is **bilaterally symmetric** and **partially lateralized** — and
it carries **NO warning**:

*   **Bilateral Parasubiculum Function:** Each hemisphere has its
    own parasubiculum, with **ipsilateral** and **bilateral**
    connections to the presubiculum, the subiculum, the medial
    entorhinal cortex, and the contralateral parasubiculum. The
    two sides are **functionally symmetric** for **basic
    head-direction and spatial processing**.

*   **Partial Lateralization (Contested — Semantic vs.
    Spatial):** The **left** parasubiculum is sometimes reported
    to be **more involved in verbal** spatial processing; the
    **right** parasubiculum is sometimes reported to be **more
    involved in spatial/nonverbal** navigation. This is
    **partial**, **contested**, and **less well-documented than
    the hippocampus lateralization**, and is documented in the
    **medial temporal lobe module** (not at the parasubiculum
    level).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    **parasubiculum** is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the parasubiculum.

*   **NO Amygdala-Lateralization Warning of their own (the
    parasubiculum is a HEAD-DIRECTION / SPATIAL subfield, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **parasubiculum** is a
    **head-direction / spatial** subfield — consumers must **not**
    conflate it with the **whole amygdala** or with the **central
    nucleus**.

**A consumer that assumes "left parasubiculum = right
parasubiculum" will be structurally correct** — the two sides are
**symmetric** and **partially lateralized** (the lateralization is
documented in the medial temporal lobe module). The
**parasubiculum** is a **strict-mirror pair with NO warning** —
**no SLEA warning**, **no amygdala-lateralization warning of their
own**, and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cornu_ammonis/ca1/``, ``.../cornu_ammonis/ca2/``,
    ``.../cornu_ammonis/ca3/``, ``.../cornu_ammonis/ca4/``,
    ``.../hippocampus/dentate_gyrus/``,
    ``.../hippocampus/subiculum/``,
    ``.../hippocampus/presubiculum/``,
    ``.../medial_temporal_lobe/amygdala/``,
    ``.../left/cortex/temporal/gyri/entorhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/perirhinal_cortex/``,
    ``.../left/cortex/temporal/gyri/parahippocampal_gyrus/``,
    ``.../left/white_matter/fornix/``,
    ``.../left/cortex/rhinencephalon/``, ``memory/``, or any other
    container. The **parasubiculum**'s relationships to CA1, CA2,
    CA3, CA4, the dentate gyrus, the subiculum, the presubiculum,
    the amygdala, the entorhinal cortex, the parahippocampal
    region, the fornix, the rhinencephalon, and the ``memory/``
    package are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **layers (II–VI)**
    and the **head-direction cells** of the parasubiculum are
    documented as **prose**, not as sub-modules. Consumers must not
    assume any exist as children; resolve layer-level detail
    through the references.
*   **HEAD-DIRECTION / SPATIAL-PROCESSING subfield — NOT the
    principal-output subfield and NOT the pattern-separation or
    pattern-completion subfields.** The **parasubiculum** is a
    **head-direction / spatial-processing** subfield of the
    **subicular complex**. **Subiculum** (sibling) is the
    **principal output**. **Dentate gyrus** (sibling) is the
    **pattern-separation** subfield. **CA3** is the
    **pattern-completion** subfield. Consumers must **not** conflate
    the parasubiculum with any of these.
*   **SUBICULAR COMPLEX — PROSE, not a structural container.** The
    **subicular complex** is the **functional grouping** of the
    **subiculum**, the **presubiculum**, and the **parasubiculum**.
    Consumers must **not** assume a `subicular_complex/` container
    exists.
*   **NOT the presubiculum — the presubiculum is the SIBLING
    subicular-complex head-direction subfield, with a DIFFERENT
    MEC target layer.** The **parasubiculum → MEC layer II** (the
    **grid-cell layer**); the **presubiculum → MEC layer III**.
*   **NOT the subiculum — the subiculum is the principal OUTPUT of
    the hippocampus.** Consumers must **not** conflate the
    parasubiculum with the subiculum.
*   **NOT the dentate gyrus — the dentate gyrus is the
    pattern-separation subfield.**
*   **NOT CA1, CA2, CA3, or CA4 — those are the CA fields of the
    cornu ammonis.**
*   **NOT the cornu ammonis — the cornu ammonis is the CA-field
    container.** Consumers must **not** conflate the parasubiculum
    with the cornu ammonis.
*   **NOT the entorhinal cortex — the entorhinal cortex is
    CORTICAL, wired under ``cortex/temporal/gyri/``.** The
    **parasubiculum → MEC layer II** projection is the **source**
    of the projection; the **entorhinal cortex** is the
    **target**.
*   **NOT the hippocampus container — the parasubiculum is a CHILD
    of the hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; the **parasubiculum** is the
    **archicortex**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** The **parasubiculum** is the **grey-matter
    archicortex**.
*   **NOT the rhinencephalon.** The **parasubiculum** is **not** an
    olfactory structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    **parasubiculum** is **not** an extended-amygdala component,
    and it carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; the
    **parasubiculum** is a **head-direction / spatial-processing**
    subfield of the **memory/navigation** container.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; the **parasubiculum** is
    the **brain structure**. Consumers must **not** conflate the
    two.
*   **NOT a single uniform layer — MULTIPLE layers (II–VI).** The
    **layers** are **prose**, not structural children.
*   **No ``AREA_PATHS`` hop.** The **parasubiculum** is a local
    leaf under the hippocampus, not a cross-listed leaf.
*   **No nested cross-listing.** The **parasubiculum** has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with right parasubiculum — strict mirror
    with NO warning.** Left and right parasubiculum modules are
    **structurally identical** — same **leaf** status, same
    **head-direction / spatial-processing** framing, same
    **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus import parasubiculum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "medial_temporal_lobe.hippocampus.parasubiculum"
    )

**Do not** assume the parasubiculum is the **presubiculum**. The
**presubiculum** is the **sibling** subicular-complex head-direction
subfield with a **different MEC target layer** — the
**parasubiculum → MEC layer II** (the grid-cell layer); the
**presubiculum → MEC layer III**.

**Do not** assume the parasubiculum is the **subiculum**. The
**subiculum** is the **principal output** of the hippocampus; the
**parasubiculum** is a **head-direction / spatial-processing**
subfield.

**Do not** assume the parasubiculum is the **dentate gyrus**. The
**dentate gyrus** is the **pattern-separation** subfield; the
**parasubiculum** is a **head-direction / spatial-processing**
subfield.

**Do not** assume the parasubiculum is **CA1**, **CA2**, **CA3**,
or **CA4**. Those are the **CA fields** of the cornu ammonis; the
**parasubiculum** is a **subicular-complex** subfield.

**Do not** assume the parasubiculum is the **cornu ammonis**. The
**cornu ammonis** is the **CA-field container**; the
**parasubiculum** is a **sibling** of the cornu ammonis under the
hippocampus.

**Do not** assume the parasubiculum is the **entorhinal cortex**.
The **entorhinal cortex** is **cortical** — wired under
``cortex/temporal/gyri/`` — and is the **target** of the
parasubiculum's principal projection (MEC layer II). The
**parasubiculum** is the **source** of the projection.

**Do not** assume the parasubiculum is the **hippocampus
container**. The **hippocampus** container contains the
**parasubiculum** and the other four subfields — the
**parasubiculum** is **one** of those five children.

**Do not** assume the parasubiculum is the **parahippocampal
region**. The **entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; the
**parasubiculum** is the **archicortex**.

**Do not** assume the parasubiculum is the **fornix** or the
**white_matter**. Those are **white-matter tracts**; the
**parasubiculum** is the **grey-matter archicortex**.

**Do not** assume the parasubiculum is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; the
**parasubiculum** is a **memory/navigation** subfield.

**Do not** assume the parasubiculum is the **``memory/`` software
package**. The **``memory/`` package** is the **software store**;
the **parasubiculum** is the **brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the parasubiculum. **The
parasubiculum is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

**Do not** assume a `subicular_complex/` container exists. The
**subicular complex** is **prose** — the **subiculum**,
**presubiculum**, and **parasubiculum** are **separate leaves**
under the hippocampus.

Iterating the parasubiculum's (empty) children (recommended
consumer pattern)::

    PARASUBICULUM_CHILDREN = ()
    # The parasubiculum is a leaf. The layers (II–VI) and the
    # head-direction cells are prose, not modules.

Reaching the presubiculum sibling (recommended consumer pattern —
the subicular-complex head-direction sibling)::

    # The presubiculum is the SIBLING subicular-complex
    # head-direction subfield — under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.presubiculum
    #
    # The parasubiculum projects principally to MEC layer II (the
    # grid-cell layer); the presubiculum projects principally to
    # MEC layer III.

Reaching the subiculum sibling (recommended consumer pattern — the
principal output)::

    # The subiculum is the PRINCIPAL OUTPUT of the hippocampus —
    # the sibling of the parasubiculum under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # The subiculum is the principal output; the parasubiculum is
    # a head-direction / spatial-processing subfield.

Reaching the dentate gyrus sibling (recommended consumer pattern —
the pattern-separation subfield)::

    # The dentate gyrus is the PATTERN-SEPARATION subfield — the
    # sibling of the parasubiculum under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
    #
    # The dentate gyrus is the pattern-separation subfield; the
    # parasubiculum is a head-direction / spatial-processing
    # subfield of the subicular complex.

Reaching the cornu ammonis (recommended consumer pattern — the
sibling container)::

    # The cornu ammonis is the CA-FIELD CONTAINER — the SIBLING of
    # the parasubiculum under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
    #
    # The parasubiculum is a subicular-complex subfield; the cornu
    # ammonis is the CA-field container.

Reaching the entorhinal cortex (recommended consumer pattern — the
target of the parasubiculum projection)::

    # The entorhinal cortex is the CORTICAL TARGET of the
    # parasubiculum projection (MEC layer II — the grid-cell
    # layer):
    #
    #   cortex.temporal.gyri.entorhinal_cortex
    #
    # The parasubiculum is the SOURCE of the projection; the
    # entorhinal cortex is the TARGET.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the
    # parasubiculum and the other four subfields:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # The parasubiculum is ONE of the five children of the
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
    # The parasubiculum is the ARCHICORTEX; the parahippocampal
    # region is the CORTICAL INTERFACE.

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
    # The parasubiculum is the BRAIN STRUCTURE; the ``memory/``
    # package is the SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE the parasubiculum is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT parasubiculum children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # The parasubiculum is a head-direction / spatial-processing
    # subfield of the MEMORY/NAVIGATION container; the central
    # nucleus and the basolateral nuclei are the FEAR structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
the parasubiculum is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the
    # parasubiculum:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The parasubiculum is SLEA-FREE.

Layer-level detail (not wired — consult references)::

    # The parasubiculum's layers are prose, not modules:
    #   layer II     -> principal neurons that project to MEC
    #                   layer II (the grid-cell layer)
    #   layer III    -> pyramidal cells that project to the
    #                   entorhinal cortex and the subiculum
    #   layers V–VI  -> deep neurons that project subcortically
    #
    # Do not attempt to resolve these as sub-paths of the
    # parasubiculum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        pas_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.parasubiculum"
        )
        # resolve pas_path through the memory/recall layer

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
    hippocampal anatomy; parasubiculum.)
*   **Parasubiculum → MEC layer II projection:** Witter, M.P.,
    Doan, T.P., Jacobsen, B., Nilssen, E.S., Ohara, S. (2017).
    "Architecture of the entorhinal cortex a review of entorhinal
    anatomy in the rat." *Frontiers in Systems Neuroscience*
    11:46. (Parasubiculum → MEC layer II projection; contrast with
    presubiculum → MEC layer III.)
*   **Head-direction cells in the parasubiculum:** Taube, J.S.
    (1995). "Head direction cells recorded in the anterior
    thalamic nuclei of freely moving rats." *Journal of
    Neuroscience* 15:70–86. (Head-direction cells; parasubiculum
    and presubiculum as head-direction regions.)
*   **Head-direction system (review):** Taube, J.S. (2007). "The
    head direction signal: origins and sensory-motor
    integration." *Annual Review of Neuroscience* 30:181–207.
    (Head-direction system; parasubiculum as a head-direction
    node.)
*   **Grid cells in the medial entorhinal cortex:** Hafting, T.,
    Fyhn, M., Molden, S., Moser, M.-B., Moser, E.I. (2005).
    "Microstructure of a spatial map in the entorhinal cortex."
    *Nature* 436:801–806. (Grid cells in MEC layer II; the
    grid-cell layer that the parasubiculum projects to.)
*   **Parasubiculum and spatial navigation:** Boccara, C.N.,
    Sargolini, F., Thoresen, V.H., Solstad, T., Witter, M.P.,
    Moser, E.I., Moser, M.-B. (2010). "Grid cells in pre- and
    parasubiculum." *Nature Neuroscience* 13:987–994. (Grid cells
    in the parasubiculum — spatial-processing role.)
*   **Parasubiculum and theta rhythm:** Chrobak, J.J., Buzsáki, G.
    (1998). "Operational dynamics in the hippocampal-entorhinal
    axis: gamma and fast theta oscillations in the
    parasubiculum." *Neuroscience* 84:977–982. (Theta-rhythm
    involvement of the parasubiculum.)
*   **Alzheimer's disease and the subicular complex:** Braak, H.,
    Braak, E. (1991). "Neuropathological stageing of
    Alzheimer-related changes." *Acta Neuropathologica*
    82:239–259. (Early entorhinal / subicular pathology —
    parasubiculum involvement.)
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
*   **Amygdala (contrast — the parasubiculum is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the hippocampus memory circuit.)
*   **SLEA (contrast — the parasubiculum is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    parasubiculum.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Parasubiculum in overview.)
*   NeuroNames — Parasubiculum (left); FMA — Parasubiculum (left
    member).
"""