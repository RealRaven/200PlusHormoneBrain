"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
=======================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── medial_temporal_lobe
                    └── hippocampus
                        └── dentate_gyrus   <-- THIS MODULE

**Primary synonym:** Dentate gyrus (right); DG; dentate area; fascia
dentata; gyrus dentatus; **granule-cell layer of the dentate
gyrus** (the layer-name, in the narrow sense).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**leaf subfield** of the **hippocampus** — the **granule-cell
layer + molecular layer + subgranular zone** of the dentate
complex, and the **principal input** of the hippocampus
(entorhinal cortex → perforant path → dentate gyrus → mossy fibers
→ CA3 / CA4). The **polymorphic layer (hilus)** of the dentate
complex is **NOT** wired here — it is wired as **``ca4``** under
``.../cornu_ammonis/`` by the tree. See *Dentate Hilus / CA4
Note*.
**Part of:** The **hippocampus** container — the **input**
subfield of the hippocampal formation. The **dentate gyrus** is the
**principal input** of the hippocampus and the **principal site**
of **pattern separation** and **adult neurogenesis**.
**Structural parent:** ``.../hippocampus/`` → **direct child** of
the hippocampus container.
**Structural children:** **None.** This is a **leaf** module. The
**molecular layer**, **granule-cell layer**, and **subgranular
zone** of the dentate gyrus are documented as **prose**, not as
structural children.
**Boundary status (PATTERN-SEPARATION subfield — NOT the
pattern-completion subfield and NOT the dentate hilus):**
**Boundary case — the dentate_gyrus is the PATTERN-SEPARATION
subfield of the hippocampus, NOT the pattern-completion subfield
and NOT the dentate hilus.** The **CA3** sibling
(``.../cornu_ammonis/ca3/``) is the **pattern-completion**
subfield (recurrent collaterals; autoassociative network). The
**CA4** sibling (``.../cornu_ammonis/ca4/``) is the **dentate
hilus** — the **polymorphic layer** of the dentate complex. The
**dentate gyrus** (here) is the **pattern-separation** subfield —
the **granule-cell layer** that **decorrelates** similar inputs
into **distinct** representations. **The dentate gyrus and CA3
perform DIFFERENT computations** — **pattern separation** in the
dentate gyrus; **pattern completion** in CA3 — and **the dentate
gyrus and CA4 are DIFFERENT LAYERS** of the same dentate complex.
Consumers must **not** conflate the dentate gyrus with CA3 or with
CA4.
**Boundary status (GRANULE-CELL LAYER — NOT the polymorphic
layer / hilus):** **Boundary case — the dentate_gyrus is the
GRANULE-CELL LAYER (plus the molecular layer and subgranular
zone), NOT the polymorphic layer / hilus.** The **granule cells**
are the **principal neurons** of the dentate gyrus — the **densely
packed**, **glutamatergic** neurons whose **axons** form the
**mossy fibers**. The **polymorphic layer (hilus)** — the layer
**between** the granule-cell layer and CA3 — is the **dentate
hilus**, wired in the tree as **``ca4``** under
``.../cornu_ammonis/``. **They are DIFFERENT LAYERS** of the
**same dentate complex**. Consumers must **not** conflate the
dentate gyrus proper (granule-cell layer) with the dentate hilus
(CA4).
**Boundary status (TREE-WIRED UNDER ``hippocampus/``, NOT under
``cornu_ammonis/``):** **Boundary case — the dentate_gyrus is
TREE-WIRED UNDER ``hippocampus/`` as a SIBLING of
``cornu_ammonis``, NOT a child of ``cornu_ammonis``.** The
**cornu ammonis** container contains **CA1**, **CA2**, **CA3**,
and **CA4** — **not** the dentate gyrus. The **dentate gyrus** is
a **direct child of the hippocampus** — a **sibling** of the
**cornu ammonis**, the **subiculum**, the **presubiculum**, and
the **parasubiculum**. Consumers must **not** resolve the dentate
gyrus under ``.../cornu_ammonis/``.
**Boundary status (NOT CA4 — the dentate hilus is wired under
``cornu_ammonis/ca4/``):** **Boundary case — the dentate_gyrus is
NOT CA4; the dentate hilus is wired under
``.../cornu_ammonis/ca4/``.** The **CA4** (``.../cornu_ammonis/
ca4/``) is the **dentate hilus** — the **polymorphic layer**
containing the **mossy cells**. The **dentate gyrus** (here) is
the **granule-cell layer + molecular layer + subgranular zone**.
The **mossy fibers** project from the **dentate granule cells**
to **both CA3 and CA4** — but the **dentate gyrus** and the
**dentate hilus** are **different layers** of the same dentate
complex. Consumers must **not** conflate the two.
**Boundary status (NOT the cornu ammonis — the cornu ammonis is
the CA-field container):** **Boundary case — the dentate_gyrus is
NOT the cornu ammonis; the cornu ammonis is the CA-field
container.** The **cornu ammonis** (``.../cornu_ammonis/``) is
the **CA-field container** — CA1, CA2, CA3, CA4. The **dentate
gyrus** (here) is a **sibling** of the cornu ammonis under the
hippocampus — the **input** subfield. **They are SIBLINGS under
the hippocampus, and they are DIFFERENT STRUCTURES.**
**Boundary status (NOT CA1, CA2, or CA3 — those are the
pyramidal-cell CA fields):** **Boundary case — the dentate_gyrus
is NOT CA1, CA2, or CA3; those are the pyramidal-cell CA
fields.** The **CA1** (principal output), **CA2** (social
memory), and **CA3** (pattern completion) subfields are
**pyramidal-cell fields** in the cornu ammonis. The **dentate
gyrus** (here) is the **granule-cell layer** — its **principal
neurons** are **granule cells**, not **pyramidal cells**.
Consumers must **not** conflate the dentate gyrus with the CA
fields.
**Boundary status (NOT the subiculum — the subiculum is the OUTPUT
TARGET of CA1):** **Boundary case — the dentate_gyrus is NOT the
subiculum; the subiculum is the OUTPUT TARGET of CA1.** The
**subiculum** (``.../hippocampus/subiculum/``) is the **principal
output** of the hippocampus to the parahippocampal region, the
mammillary bodies (via the fornix), and the prefrontal cortex —
**CA1 projects to the subiculum**. The **dentate gyrus** (here) is
the **INPUT** subfield. Consumers must **not** conflate the
dentate gyrus with the subiculum.
**Boundary status (NOT the presubiculum or parasubiculum — those
are the subicular-complex head-direction subfields):** **Boundary
case — the dentate_gyrus is NOT the presubiculum or the
parasubiculum.** The **presubiculum** (``.../hippocampus/
presubiculum/``) and the **parasubiculum**
(``.../hippocampus/parasubiculum/``) are **siblings** of the
dentate gyrus under the hippocampus — the **head-direction** and
**spatial** subfields of the **subicular complex**. The
**dentate gyrus** (here) is the **granule-cell layer**. **They are
SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.**
**Boundary status (NOT the hippocampus container — the dentate
gyrus is a CHILD of the hippocampus):** **Boundary case — the
dentate_gyrus is a CHILD of the hippocampus container, not the
container itself.** The **hippocampus** container contains the
**cornu ammonis**, the **dentate gyrus**, the **parasubiculum**,
the **presubiculum**, and the **subiculum** — the **dentate
gyrus** is **one** of those five children. Consumers must **not**
conflate the dentate gyrus with the hippocampus container.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the dentate_gyrus
is NOT the parahippocampal region.** The **parahippocampal
region** (the **entorhinal cortex**, the **perirhinal cortex**,
and the **parahippocampal gyrus**) is **cortical** — it is wired
under ``.../right/cortex/temporal/gyri/`` and is **outside** the
hippocampus container. The **dentate gyrus** (here) is the
**archicortex**. **They are DIFFERENT STRUCTURES**: the
**parahippocampal region** is the **cortical interface** that
**feeds** the hippocampus (via the **perforant path**); the
**dentate gyrus** is the **archicortex** that **receives** the
perforant-path input. Consumers must **not** conflate the two.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the dentate_gyrus is
NOT the fornix or the white matter; the fornix and the white_matter
are WHITE-MATTER structures.** The **fornix**
(``.../right/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../right/white_matter/``) is the **white-matter
infrastructure**. The **dentate gyrus** (here) is the
**grey-matter archicortex**. Consumers must **not** conflate the
two. Note also that the **mossy fibers** are
**intra-hippocampal** axonal projections — they are **not** the
**fornix** and **not** the **white_matter**.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the dentate_gyrus is NOT the rhinencephalon.** The
**rhinencephalon** (``.../right/cortex/rhinencephalon/``) — the
olfactory bulb, olfactory tract, piriform cortex, periamygdaloid
cortex, anterior olfactory nucleus, and uncus — is the **cortical
olfactory lobe**. The **dentate gyrus** (here) is the
**archicortex of episodic memory and spatial navigation** — it is
**not** an olfactory structure. Consumers must **not** conflate
the two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the
dentate_gyrus is NOT the amygdala; the amygdala is the
FEAR/EMOTION/SALIENCE container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), the
**lateral nucleus** (sensory input), and the **medial nucleus**
(olfactory/pheromone). The **dentate gyrus** (here) is a
**subfield** of the **memory** container. Consumers must **not**
conflate the dentate gyrus with the amygdala.
**Boundary status (SLEA-FREE — the dentate gyrus is NOT an
extended-amygdala component):** **Boundary case — the
dentate_gyrus is SLEA-FREE.** The **SLEA overlap** belongs to the
**central nucleus** (the **only SLEA component** in the amygdala)
and to the **BNST**, **ventral pallidum**, and **nucleus accumbens**
(wired elsewhere). The **dentate gyrus** is an
**episodic/declarative-memory and spatial-navigation** structure —
it is **NOT** an extended-amygdala component, and it carries **NO
SLEA warning**. Consumers must **not** import the SLEA warning
into the dentate gyrus — it is **SLEA-free**.
**Boundary status (NOT the memory software layer — the dentate
gyrus is the BRAIN STRUCTURE, not the ``memory/`` package):**
**Boundary case — the dentate_gyrus is the BRAIN STRUCTURE, NOT
the ``memory/`` software package.** The **``memory/`` package**
(``memory/stores/`` — episodic, semantic, procedural, working;
``memory/backends/`` — chroma, in_memory) is the **software memory
layer** of the simulation. The **dentate gyrus** (here) is the
**brain structure** that **subserves** the **pattern-separation**
and **adult-neurogenesis** contribution to episodic memory.
Consumers must **not** conflate the two — the **brain structure**
is wired here; the **software store** is wired under ``memory/``.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
dentate_gyrus is NOT the fear-output or the fear-learning
structures.** The **central nucleus** (fear-output), the
**basolateral nuclei** (fear-learning), and the **basomedial
nuclei** (fear-modulatory) are **amygdala** children. The
**dentate gyrus** is the **pattern-separation** subfield of the
**memory** container — it is **not** a fear-output or
fear-learning structure. Consumers must **not** conflate the
dentate gyrus with the **amygdala fear circuit**.
**Boundary status (NOT a single uniform layer — MULTIPLE layers and
the adult-neurogenic subgranular zone):** **Boundary case — the
dentate_gyrus is a HETEROGENEOUS structure with MULTIPLE layers
(molecular layer, granule-cell layer, subgranular zone), not a
single uniform layer.** The **layers** are functionally distinct
— the **molecular layer** receives the **perforant-path** input
from the **entorhinal cortex**; the **granule-cell layer**
contains the **granule cells** (the **principal neurons** of the
dentate gyrus); the **subgranular zone** (SGZ) is the **adult
neurogenic niche** — one of the **two canonical** adult
neurogenic niches of the mammalian brain. The tree wires the
**dentate gyrus** as a **single leaf** under the hippocampus —
the **layers** and the **subgranular zone** are **prose**, not
structural children. Consumers that need **layer-level** or
**neurogenesis-level** resolution should consult the references,
not the tree.

Overview
--------
The dentate gyrus is the **pattern-separation** subfield of the
hippocampus — the **granule-cell layer + molecular layer +
subgranular zone** that **receives** the **perforant-path** input
from the entorhinal cortex and **projects** the **mossy fibers** to
CA3 and CA4. It is a **leaf** module under the hippocampus
container, the **sibling of the cornu ammonis, the subiculum, the
presubiculum, and the parasubiculum**, and the **grey-matter
substrate** of **pattern separation**, **adult neurogenesis**, and
the **mossy-fiber input** to the CA fields.

**The dentate gyrus is the PATTERN-SEPARATION subfield of the
hippocampus.** **CA3** (sibling) is the **pattern-completion**
subfield. **CA1** is the **principal output**. **CA2** is the
**social-memory** subfield. **CA4** is the **dentate hilus**. The
**dentate gyrus** is the **granule-cell layer** that
**decorrelates** similar inputs into **distinct** representations
— the **pattern-separation** computation.

**The dentate gyrus is the GRANULE-CELL LAYER (plus the molecular
layer and subgranular zone), NOT the polymorphic layer / hilus.**
The **granule cells** are the **principal neurons** of the dentate
gyrus — the **densely packed**, **glutamatergic** neurons whose
**axons** form the **mossy fibers**. The **polymorphic layer
(hilus)** is the **dentate hilus** — wired in the tree as
**``ca4``** under ``.../cornu_ammonis/``. **They are DIFFERENT
LAYERS** of the **same dentate complex**.

**The dentate gyrus is TREE-WIRED UNDER ``hippocampus/``, NOT under
``cornu_ammonis/``.** The **dentate gyrus** is a **direct child of
the hippocampus** — a **sibling** of the **cornu ammonis**, the
**subiculum**, the **presubiculum**, and the **parasubiculum**.
Consumers must **not** resolve the dentate gyrus under
``.../cornu_ammonis/``.

**The dentate gyrus is NOT CA4.** **CA4** is the **dentate hilus**
— wired under ``.../cornu_ammonis/ca4/`` — the **polymorphic
layer** containing the **mossy cells**. The **dentate gyrus** is
the **granule-cell layer**. The **mossy fibers** project from the
**dentate granule cells** to **both CA3 and CA4** — but the
**dentate gyrus** and the **dentate hilus** are **different
layers** of the same dentate complex.

**The dentate gyrus is NOT the cornu ammonis.** The **cornu
ammonis** is the **CA-field container** (CA1–CA4); the **dentate
gyrus** is a **sibling** of the cornu ammonis under the
hippocampus — the **input** subfield.

**The dentate gyrus is NOT the subiculum.** The **subiculum** is
the **output target** of CA1. The **dentate gyrus** is the
**input**.

**The dentate gyrus is NOT the presubiculum or the parasubiculum.**
Those are the **head-direction** and **spatial** subfields of the
**subicular complex** — **siblings** of the dentate gyrus under
the hippocampus.

**The dentate gyrus is NOT the parahippocampal region.** The
**entorhinal cortex**, **perirhinal cortex**, and **parahippocampal
gyrus** are **cortical** — they are wired under
``cortex/temporal/gyri/``. The **dentate gyrus** is the
**archicortex**.

**The dentate gyrus is SLEA-FREE.** It is **not** an
extended-amygdala component, and it carries **no SLEA warning**. The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere).

**The dentate gyrus is the BRAIN STRUCTURE, not the ``memory/``
software package.** The **``memory/`` package** is the **software
memory layer**. The **dentate gyrus** is the **brain region** whose
function the episodic store models. **They are DIFFERENT LAYERS.**

**The dentate gyrus is a paired structure.** Each hemisphere has
its own dentate gyrus, with **ipsilateral** and **bilateral**
connections to the entorhinal cortex, CA3, CA4, and the
contralateral dentate gyrus. The two sides are **bilaterally
symmetric** and **partially lateralized** — the **left** dentate
gyrus is more involved in **verbal** episodic memory, and the
**right** dentate gyrus is more involved in **spatial/nonverbal**
episodic memory. This is **well-documented** (not contested), and
documented in the **medial temporal lobe module** (not at the
dentate-gyrus level). See *Lateralization Notes*.

Dentate Hilus / CA4 Note
------------------------
**The polymorphic layer (hilus) of the dentate gyrus is wired in
the tree as ``ca4`` under ``.../cornu_ammonis/`` — NOT as a child
of ``dentate_gyrus/``.** Consumers should **resolve the dentate
hilus at ``.../cornu_ammonis/ca4/``** — **not** at
``.../dentate_gyrus/``. The **dentate gyrus** proper (this module)
is the **granule-cell layer + molecular layer + subgranular
zone**; the **hilus** is the **CA4 sibling** under the cornu
ammonis. The **mossy fibers** project from the **dentate granule
cells** to **both CA3 and CA4** — the **same** granule-cell
population feeds **both** downstream targets. Consumers must
**not** attempt to resolve the dentate hilus under
``.../dentate_gyrus/``, and must **not** assume the dentate gyrus
is a container that includes the hilus.

Layer Composition (prose, not structural children)
--------------------------------------------------
The dentate gyrus is a **heterogeneous structure** — documented as
**prose**, not as structural children:

*   **Molecular layer** — the **superficial** layer, receiving the
    **perforant-path** input from the **entorhinal cortex** (the
    **principal input** of the hippocampus).

*   **Granule-cell layer** — the **principal-cell** layer,
    containing the **dentate granule cells** — the **densely
    packed**, **glutamatergic** neurons whose **axons** form the
    **mossy fibers**.

*   **Subgranular zone (SGZ)** — the **adult-neurogenic niche**
    — one of the **two canonical** adult neurogenic niches of the
    mammalian brain (the other is the **subventricular zone /
    olfactory bulb**). The SGZ is **NOT** a separate structural
    child — it is the **prose** neurogenic zone **between** the
    granule-cell layer and the hilus.

**These layers are prose, not structural children.** The tree
wires the **dentate gyrus** as a **single leaf** under the
hippocampus — the **layers** and the **subgranular zone** are
**prose**, not structural children. Consumers that need
**layer-level** or **neurogenesis-level** resolution should
consult the references, not the tree.

The Dentate Gyrus / CA3 Boundary
--------------------------------
This is the **pattern-separation vs. pattern-completion** sibling
boundary:

*   **Dentate gyrus** (this module) — the **pattern-separation**
    subfield (granule cells; **mossy-fiber** source; **adult
    neurogenesis**; **perforant-path** input).

*   **CA3** (``.../cornu_ammonis/ca3/``) — the
    **pattern-completion** subfield (recurrent collaterals;
    autoassociative network; **mossy-fiber** input; **Schaffer**
    output to CA1).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES** — the **dentate gyrus** is the **input** and the
**pattern-separation** computation; **CA3** is the
**pattern-completion** computation. The **mossy fibers** project
from the **dentate granule cells** to **CA3** (and to **CA4**).
Consumers must **not** conflate the dentate gyrus with CA3.

The Dentate Gyrus / CA4 Boundary
--------------------------------
This is the **granule-cell layer vs. polymorphic layer (hilus)**
boundary:

*   **Dentate gyrus** (this module) — the **granule-cell layer +
    molecular layer + subgranular zone**.

*   **CA4** (``.../cornu_ammonis/ca4/``) — the **dentate hilus**
    — the **polymorphic layer** containing the **mossy cells**.

**They are DIFFERENT LAYERS of the same dentate complex** — the
**dentate gyrus proper** is the **granule-cell layer**; **CA4** is
the **hilus** (the **polymorphic cell layer** between the
granule-cell layer and CA3). The **mossy fibers** project from the
**dentate granule cells** to **both CA3 and CA4**. Consumers must
**not** conflate the dentate gyrus with CA4.

The Dentate Gyrus / Cornu Ammonis Boundary
------------------------------------------
This is the **sibling-container** boundary:

*   **Dentate gyrus** (this module) — the **input** subfield —
    a **sibling** of the cornu ammonis under the hippocampus.

*   **Cornu ammonis** (``.../cornu_ammonis/``) — the **CA-field
    container** — CA1, CA2, CA3, CA4.

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the dentate gyrus
with the cornu ammonis container.

The Dentate Gyrus / Subiculum Boundary
--------------------------------------
This is the **input vs. output** sibling boundary:

*   **Dentate gyrus** (this module) — the **input** subfield.

*   **Subiculum** (``.../hippocampus/subiculum/``) — the **output
    target** of CA1 (the subiculum projects to the parahippocampal
    region, the mammillary bodies, and the prefrontal cortex).

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES** — the **dentate gyrus** is the **input**; the
**subiculum** is the **output structure**. Consumers must **not**
conflate the two.

The Dentate Gyrus / Presubiculum and Parasubiculum Boundary
-----------------------------------------------------------
This is the **dentate vs. subicular-complex** sibling boundary:

*   **Dentate gyrus** (this module) — the **granule-cell layer**.

*   **Presubiculum** (``.../hippocampus/presubiculum/``) and
    **parasubiculum** (``.../hippocampus/parasubiculum/``) — the
    **head-direction** and **spatial** subfields of the
    **subicular complex**.

**They are SIBLINGS under the hippocampus, and they are DIFFERENT
STRUCTURES.** Consumers must **not** conflate the dentate gyrus
with the presubiculum or the parasubiculum.

The Dentate Gyrus / Hippocampus Boundary
----------------------------------------
This is the **child vs. container** boundary:

*   **Dentate gyrus** (this module) — a **child** of the
    hippocampus container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**The dentate gyrus is ONE of the five children of the
hippocampus.** Consumers must **not** conflate the dentate gyrus
with the hippocampus container.

The Dentate Gyrus / Parahippocampal Region Boundary
---------------------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **Dentate gyrus** (this module) — the **archicortex** (the
    granule-cell layer).

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../right/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus** (via the **perforant path**). The **dentate
gyrus** is the **archicortex** that **receives** the
perforant-path input. Consumers must **not** conflate the **dentate
gyrus** with the **parahippocampal region** — the parahippocampal
region is **cortex/**; the dentate gyrus is
**subcortical/medial_temporal_lobe/**.

The Dentate Gyrus / Fornix and White Matter Boundary
----------------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **Dentate gyrus** (this module) — the **grey-matter**
    archicortex.

*   **Fornix** (``.../right/white_matter/fornix/``) and
    **white_matter** (``.../right/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — the **dentate gyrus** is the
**grey-matter structure**; the **fornix** and the **white_matter**
are the **white-matter tracts**. Note also that the **mossy
fibers** are **intra-hippocampal** axonal projections — they are
**not** the **fornix** and **not** the **white_matter**. Consumers
must **not** conflate the two.

The Dentate Gyrus / Rhinencephalon Boundary
-------------------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **Dentate gyrus** (this module) — the **archicortex of
    episodic memory and spatial navigation**.

*   **Rhinencephalon** (``.../right/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — the **dentate gyrus** is the
**memory archicortex**; the **rhinencephalon** is the **olfactory
lobe**. Consumers must **not** conflate the two.

The Dentate Gyrus / Amygdala Boundary
-------------------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **Dentate gyrus** (this module) — a **subfield** of the
    **memory** container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; the **dentate gyrus** is a **child of the
memory** container. Consumers must **not** conflate the two.

The Dentate Gyrus / Memory Software Layer Boundary
--------------------------------------------------
This is the **brain structure vs. software store** boundary:

*   **Dentate gyrus** (this module) — the **brain structure** that
    subserves pattern separation and adult neurogenesis.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — the **dentate gyrus** is the
**brain region**; the **``memory/`` package** is the **software
store**. Consumers must **not** conflate the two.

The Dentate Gyrus / SLEA Boundary
---------------------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **Dentate gyrus** (this module) — **SLEA-FREE**. No
    extended-amygdala relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**The dentate gyrus is NOT part of the SLEA continuum.** It is an
**episodic/declarative-memory and spatial-navigation** structure,
and it carries **no SLEA warning**. Consumers must **not** import
the SLEA warning into the dentate gyrus.

Function in the Human Brain
---------------------------
The dentate gyrus's functions are **pattern separation**, **adult
neurogenesis**, and **mossy-fiber input to the CA fields** — **NOT
episodic-memory output and NOT fear-output**:

*   **Pattern Separation (Sparse Coding):** The **dentate gyrus**
    is the **principal site** of **pattern separation** — the
    **decorrelation** of **similar inputs** into **distinct**
    representations, implemented by the **sparse, high-dimensional**
    granule-cell code. This is the **substrate** of the
    **discrimination** of similar episodes. **CA3** performs the
    **complementary** computation — **pattern completion** —
    retrieving a **stored** pattern from a **partial cue**.

*   **Adult Neurogenesis (Subgranular Zone):** The **subgranular
    zone** (SGZ) of the dentate gyrus is one of the **two
    canonical** adult neurogenic niches of the mammalian brain (the
    other is the **subventricular zone / olfactory bulb**). **New
    granule cells** are **born** in the SGZ throughout adulthood
    and **integrate** into the dentate circuit — the **adult
    neurogenesis** substrate of the dentate gyrus.

*   **Mossy-Fiber Input to CA3 and CA4:** The **dentate granule
    cells** project the **mossy fibers** to **CA3** (stratum
    lucidum) and to **CA4** (the dentate hilus) — the **input**
    side of the CA3 pattern-completion computation and the
    **hilar** mossy-cell feedback circuit. This is the **output**
    side of the dentate-gyrus computation.

*   **Perforant-Path Receipt (Entorhinal Cortex → Dentate Gyrus):**
    The **dentate gyrus** receives the **perforant-path** input
    from the **entorhinal cortex** — the **principal input** of
    the hippocampus. This is the **input** side of the
    dentate-gyrus computation.

*   **NOT a neural processor in the classical sense.** The
    **dentate gyrus** is an **input and pattern-separation**
    structure — it **gates** and **decorrelates** the
    **perforant-path** input, but it does **not** produce the
    **fear-output** or the **autonomic and behavioral** fear
    responses. The **fear-output** is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** the dentate gyrus is the
**pattern-separation subfield** of the **hippocampus** — the
**granule-cell layer** that anchors **pattern separation, adult
neurogenesis, and the mossy-fiber input to the CA fields**. It is
**SLEA-free**, **memory/navigation**, and **NOT the fear-output
structure** — the **fear-output** is the **central nucleus**, the
**fear-learning** structures are the **basolateral nuclei**, and
the **dentate gyrus** is the **pattern-separation subfield** of the
**memory** container.

Associated Disorders
--------------------
The dentate gyrus has **no named "dentate gyrus syndrome"** in the
narrow sense, but its clinical associations are **well-documented**:

*   **Temporal Lobe Epilepsy (Granule-Cell Dispersion and
    Mossy-Fiber Sprouting):** The **dentate gyrus** shows
    **granule-cell dispersion** — the **broadening** and
    **disorganization** of the **granule-cell layer** — and
    **mossy-fiber sprouting** — the **aberrant** mossy-fiber
    projections **back** into the **molecular layer** — in
    **temporal lobe epilepsy**. The **dentate gyrus** is the
    **epileptogenic substrate** of the **dentate** contribution to
    temporal lobe epilepsy.

*   **Hippocampal Sclerosis (Ammon's Horn Sclerosis — Dentate
    Component):** The **dentate gyrus** shows **granule-cell
    dispersion** and **mossy-fiber sprouting** in **Ammon's horn
    sclerosis** — alongside the **CA1** and **CA3** pyramidal-cell
    loss and the **CA4** mossy-cell loss. The **dentate gyrus** is
    part of the **sclerotic** hippocampal circuit.

*   **Alzheimer's Disease (Early Entorhinal-Dentate Involvement):**
    The **dentate gyrus** is involved in **Alzheimer's disease**
    — the **entorhinal cortex** (the **perforant-path** source)
    is the **earliest** affected structure, and the **dentate
    gyrus** is **downstream**. **Dentate neurogenesis** is
    **reduced** in Alzheimer's disease.

*   **Major Depressive Disorder (Reduced Adult Neurogenesis —
    Contested):** The **dentate gyrus** shows **reduced adult
    neurogenesis** in **major depressive disorder** — the
    **neurogenesis hypothesis** of depression proposes that
    **reduced SGZ neurogenesis** contributes to **depressive
    symptoms** and that **antidepressants** **increase**
    neurogenesis. This is **contested** and is documented in the
    references.

*   **Aging (Decline of Adult Neurogenesis):** The **dentate
    gyrus** shows a **decline** in **adult neurogenesis** with
    **aging** — the **SGZ** produces **fewer** new granule cells
    in **older** individuals. This is **well-documented** and is
    part of the **normal aging** trajectory of the hippocampus.

*   **No Named "Dentate Gyrus Syndrome":** The **dentate gyrus**
    is a **subfield** of the hippocampus, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **direct** for **temporal lobe
    epilepsy** and **hippocampal sclerosis**, **reported** for
    **Alzheimer's disease** and **aging**, and **contested** for
    **major depressive disorder**.

**What is NOT here:** The **dentate gyrus** is **not** the
substrate for **Kluver-Bucy syndrome** (amygdala — basolateral
nuclei + central nucleus), **Urbach-Wiethe disease** (amygdala —
basolateral nuclei), **fear conditioning** (central nucleus +
basolateral nuclei), or **fear extinction** (ventromedial
prefrontal cortex + basomedial nuclei). Its clinical relevance is
**direct** for **temporal lobe epilepsy** and **hippocampal
sclerosis**, **reported** for **Alzheimer's disease** and
**aging**, and **contested** for **major depressive disorder**.

Lateralization Notes
--------------------
This is the **right** dentate_gyrus module. The **dentate gyrus**
is **bilaterally symmetric** and **partially lateralized** — and
it carries **NO warning**:

*   **Bilateral Dentate Function:** Each hemisphere has its own
    dentate gyrus, with **ipsilateral** and **bilateral**
    connections to the entorhinal cortex, CA3, CA4, and the
    contralateral dentate gyrus. The two sides are **functionally
    symmetric** for **basic memory and navigation**.

*   **Partial Lateralization (Well-Documented — Verbal vs.
    Spatial):** The **left** dentate gyrus is **more involved in
    verbal** episodic memory (word lists, stories, verbal
    recognition); the **right** dentate gyrus is **more involved in
    spatial/nonverbal** episodic memory (spatial layouts, faces,
    nonverbal recognition). This is **well-documented**, **not
    contested**, and is documented in the **medial temporal lobe
    module** (not at the dentate-gyrus level).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** The
    **dentate gyrus** is **SLEA-free** — it is **not** an
    extended-amygdala component. Consumers must **not** import the
    SLEA warning into the dentate gyrus.

*   **NO Amygdala-Lateralization Warning of their own (the dentate
    gyrus is the PATTERN-SEPARATION subfield, not the
    fear-output):** The **right-amygdala fear association**
    belongs to the **amygdala module** — specifically the
    **central nucleus** (fear-output) and the **basolateral
    nuclei** (fear-learning). The **dentate gyrus** is a
    **pattern-separation subfield** — consumers must **not**
    conflate it with the **whole amygdala** or with the **central
    nucleus**. The **dentate gyrus** is the
    **pattern-separation** subfield, not the **fear circuit**.

**A consumer that assumes "left dentate gyrus = right dentate
gyrus" will be structurally correct** — the two sides are
**symmetric** and **partially lateralized** (the lateralization is
documented in the medial temporal lobe module). The **dentate
gyrus** is a **strict-mirror pair with NO warning** — **no SLEA
warning**, **no amygdala-lateralization warning of their own**,
and **no rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cornu_ammonis/ca1/``, ``.../cornu_ammonis/ca2/``,
    ``.../cornu_ammonis/ca3/``, ``.../cornu_ammonis/ca4/``,
    ``.../hippocampus/subiculum/``,
    ``.../hippocampus/parasubiculum/``,
    ``.../hippocampus/presubiculum/``,
    ``.../medial_temporal_lobe/amygdala/``,
    ``.../right/cortex/temporal/gyri/entorhinal_cortex/``,
    ``.../right/cortex/temporal/gyri/perirhinal_cortex/``,
    ``.../right/cortex/temporal/gyri/parahippocampal_gyrus/``,
    ``.../right/white_matter/fornix/``,
    ``.../right/cortex/rhinencephalon/``, ``memory/``, or any other
    container. The **dentate gyrus**'s relationships to CA1, CA2,
    CA3, CA4, the subiculum, the parasubiculum, the presubiculum,
    the amygdala, the parahippocampal region, the fornix, the
    rhinencephalon, and the ``memory/`` package are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **molecular
    layer**, **granule-cell layer**, and **subgranular zone** of
    the dentate gyrus are documented as **prose**, not as
    sub-modules. Consumers must not assume any exist as children;
    resolve layer-level or neurogenesis-level detail through the
    references.
*   **PATTERN-SEPARATION subfield — NOT the pattern-completion
    subfield and NOT the dentate hilus.** The **dentate gyrus** is
    the **pattern-separation** subfield (granule cells; mossy-fiber
    source; adult neurogenesis). **CA3** (sibling) is the
    **pattern-completion** subfield. **CA4** (sibling) is the
    **dentate hilus**. Consumers must **not** conflate the dentate
    gyrus with CA3 or CA4.
*   **GRANULE-CELL LAYER — NOT the polymorphic layer / hilus.**
    The **dentate gyrus** proper is the **granule-cell layer +
    molecular layer + subgranular zone**; the **hilus** is the
    **dentate hilus**, wired as **``ca4``** under
    ``.../cornu_ammonis/``. Consumers must **not** conflate the
    dentate gyrus proper with the dentate hilus (CA4).
*   **TREE-WIRED UNDER ``hippocampus/``, NOT under
    ``cornu_ammonis/``.** The **dentate gyrus** is a **sibling**
    of the cornu ammonis under the hippocampus — **not** a child
    of the cornu ammonis.
*   **NOT CA4 — the dentate hilus is wired under
    ``cornu_ammonis/ca4/``.** Consumers must **not** resolve the
    dentate hilus under ``.../dentate_gyrus/``, and must **not**
    assume the dentate gyrus is a container that includes the
    hilus.
*   **NOT the cornu ammonis — the cornu ammonis is the CA-field
    container.** Consumers must **not** conflate the dentate gyrus
    with the cornu ammonis container.
*   **NOT CA1, CA2, or CA3 — those are the pyramidal-cell CA
    fields.** Consumers must **not** conflate the dentate gyrus
    with the CA fields.
*   **NOT the subiculum — the subiculum is the OUTPUT TARGET of
    CA1.** Consumers must **not** conflate the dentate gyrus with
    the subiculum.
*   **NOT the presubiculum or the parasubiculum — those are the
    subicular-complex head-direction subfields.**
*   **NOT the hippocampus container — the dentate gyrus is a CHILD
    of the hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; the **dentate gyrus** is the
    **archicortex**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** The **dentate gyrus** is the **grey-matter
    archicortex**; the **mossy fibers** are **intra-hippocampal**
    projections — not the fornix and not the white_matter.
*   **NOT the rhinencephalon.** The **dentate gyrus** is **not** an
    olfactory structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** The
    **dentate gyrus** is **not** an extended-amygdala component,
    and it carries **no SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; the **dentate
    gyrus** is the **pattern-separation** subfield of the
    **memory** container.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; the **dentate gyrus** is
    the **brain structure**. Consumers must **not** conflate the
    two.
*   **NOT a single uniform layer — MULTIPLE layers and the
    adult-neurogenic subgranular zone.** The **molecular layer**,
    **granule-cell layer**, and **subgranular zone** are **prose**,
    not structural children.
*   **No ``AREA_PATHS`` hop.** The **dentate gyrus** is a local
    leaf under the hippocampus, not a cross-listed leaf.
*   **No nested cross-listing.** The **dentate gyrus** has no
    nested dual-framing module. It is a single leaf.
*   **Structural parity with left dentate gyrus — strict mirror
    with NO warning.** Left and right dentate gyrus modules are
    **structurally identical** — same **leaf** status, same
    **pattern-separation** framing, same **SLEA-free** status,
    same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe.hippocampus import dentate_gyrus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "medial_temporal_lobe.hippocampus.dentate_gyrus"
    )

**Do not** assume the dentate gyrus is **CA4**. The **dentate
hilus** (CA4) is wired under ``.../cornu_ammonis/ca4/`` — **not**
under ``.../dentate_gyrus/``.

**Do not** assume the dentate gyrus is the **polymorphic layer /
hilus**. The **dentate gyrus** proper is the **granule-cell layer
+ molecular layer + subgranular zone**; the **hilus** is the
**dentate hilus** (CA4), wired under ``.../cornu_ammonis/``.

**Do not** assume the dentate gyrus is **CA3**. The **dentate
gyrus** is the **pattern-separation** subfield; **CA3** is the
**pattern-completion** subfield. They are **siblings**, and the
**mossy fibers** project from the dentate granule cells to CA3
(and to CA4).

**Do not** assume the dentate gyrus is **CA1**, **CA2**, or
**CA3**. Those are the **pyramidal-cell CA fields** — the dentate
gyrus is the **granule-cell layer**.

**Do not** assume the dentate gyrus is the **cornu ammonis
container**. The **cornu ammonis** is the **CA-field container**
(CA1–CA4); the **dentate gyrus** is a **sibling** of the cornu
ammonis under the hippocampus.

**Do not** assume the dentate gyrus is the **subiculum**. The
**subiculum** is the **output target** of CA1; the **dentate
gyrus** is the **input** subfield.

**Do not** assume the dentate gyrus is the **presubiculum** or the
**parasubiculum**. Those are the **subicular-complex
head-direction** subfields. They are **siblings**.

**Do not** assume the dentate gyrus is the **hippocampus
container**. The **hippocampus** container contains the **dentate
gyrus** and the other four subfields — the **dentate gyrus** is
**one** of those five children.

**Do not** assume the dentate gyrus is the **parahippocampal
region**. The **entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; the **dentate
gyrus** is the **archicortex**.

**Do not** assume the dentate gyrus is the **fornix** or the
**white_matter**. Those are **white-matter tracts**; the **dentate
gyrus** is the **grey-matter archicortex**; the **mossy fibers**
are **intra-hippocampal** projections.

**Do not** assume the dentate gyrus is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; the
**dentate gyrus** is the **memory archicortex**.

**Do not** assume the dentate gyrus is the **``memory/`` software
package**. The **``memory/`` package** is the **software store**;
the **dentate gyrus** is the **brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into the dentate gyrus. **The
dentate gyrus is SLEA-FREE** — it is **not** an extended-amygdala
component, and it is **NOT the fear-output structure**.

Iterating the dentate gyrus's (empty) children (recommended
consumer pattern)::

    DENTATE_GYRUS_CHILDREN = ()
    # The dentate gyrus is a leaf. The molecular layer, granule-cell
    # layer, and subgranular zone are prose, not modules.

Reaching the CA3 sibling (recommended consumer pattern — the
pattern-completion subfield)::

    # CA3 is the PATTERN-COMPLETION subfield — the SIBLING of the
    # dentate gyrus under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca3
    #
    # The dentate gyrus is the PATTERN-SEPARATION subfield (the
    # input); CA3 is the PATTERN-COMPLETION subfield (downstream).
    # The mossy fibers project from the dentate granule cells to
    # the CA3 stratum lucidum.

Reaching the CA4 sibling (recommended consumer pattern — the
dentate hilus)::

    # CA4 is the DENTATE HILUS — the SIBLING of the dentate gyrus
    # under the hippocampus (wired under cornu_ammonis):
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca4
    #
    # The dentate gyrus proper is the GRANULE-CELL layer; CA4 is the
    # HILUS (the polymorphic layer between the granule-cell layer
    # and CA3). The mossy fibers project from the dentate granule
    # cells to both CA3 and CA4.

Reaching the cornu ammonis (recommended consumer pattern — the
sibling container)::

    # The cornu ammonis is the CA-FIELD CONTAINER — the SIBLING of
    # the dentate gyrus under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
    #
    # The dentate gyrus is a SIBLING of the cornu ammonis — NOT a
    # child of it.

Reaching the subiculum (recommended consumer pattern — the output
target of CA1)::

    # The subiculum is the OUTPUT TARGET of CA1 — the sibling of
    # the dentate gyrus under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # The dentate gyrus is the INPUT; the subiculum is the OUTPUT
    # structure.

Reaching the presubiculum and parasubiculum (recommended consumer
pattern — the subicular-complex siblings)::

    # The presubiculum and parasubiculum are the HEAD-DIRECTION and
    # SPATIAL subfields of the subicular complex — the SIBLINGS of
    # the dentate gyrus under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.presubiculum
    #   subcortical.medial_temporal_lobe.hippocampus.parasubiculum
    #
    # The dentate gyrus is the granule-cell layer; the presubiculum
    # and parasubiculum are the subicular-complex head-direction
    # subfields.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the dentate
    # gyrus and the other four subfields:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # The dentate gyrus is ONE of the five children of the
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
    # The dentate gyrus is the ARCHICORTEX; the parahippocampal
    # region is the CORTICAL INPUT (the perforant-path source).

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
    # The dentate gyrus is the BRAIN STRUCTURE; the ``memory/``
    # package is the SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE the dentate gyrus is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT dentate gyrus children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # The dentate gyrus is the pattern-separation subfield of the
    # MEMORY container; the central nucleus and the basolateral
    # nuclei are the FEAR structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
the dentate gyrus is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include the dentate
    # gyrus:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # The dentate gyrus is SLEA-FREE.

Layer-level detail (not wired — consult references)::

    # The dentate gyrus's layers are prose, not modules:
    #   molecular layer       -> perforant path (from entorhinal
    #                            cortex); the principal input
    #   granule-cell layer    -> dentate granule cells; the
    #                            principal neurons (mossy-fiber
    #                            source)
    #   subgranular zone      -> adult-neurogenic niche (one of the
    #                            two canonical adult neurogenic
    #                            niches; the other is the SVZ /
    #                            olfactory bulb)
    #
    # Do not attempt to resolve these as sub-paths of the dentate
    # gyrus.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        dg_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.dentate_gyrus"
        )
        # resolve dg_path through the memory/recall layer

References
----------
*   **Canonical dentate gyrus anatomy:** Amaral, D.G., Witter, M.P.
    (1989). "The three-dimensional organization of the hippocampal
    formation: a review of anatomical data." *Neuroscience*
    31:571–591. (Definitive dentate gyrus anatomy; granule-cell
    layer; molecular layer; subgranular zone; mossy fibers.)
*   **Dentate gyrus anatomy (including the hilus, contrast — the
    dentate hilus is wired as CA4):** Amaral, D.G. (1978). "A Golgi
    study of cell types in the hilar region of the hippocampus in
    the rat." *Journal of Comparative Neurology* 182:851–914.
    (The dentate hilus — CA4 — and its mossy cells; the hilus is
    distinct from the granule-cell layer.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; dentate gyrus.)
*   **Pattern separation:** Yassa, M.A., Stark, C.E.L. (2011).
    "Pattern separation in the hippocampus." *Trends in
    Neurosciences* 34:515–525. (Dentate gyrus pattern separation;
    contrast with CA3 pattern completion.)
*   **Pattern separation (experimental):** Bakker, A., Kirwan,
    C.B., Miller, M., Stark, C.E.L. (2008). "Pattern separation in
    the human hippocampal CA3 and dentate gyrus." *Science*
    319:1640–1642. (Dentate gyrus / CA3 pattern separation in
    humans.)
*   **Adult neurogenesis in the dentate gyrus:** Eriksson, P.S.,
    et al. (1998). "Neurogenesis in the adult human hippocampus."
    *Nature Medicine* 4:1313–1317. (Adult neurogenesis in the
    subgranular zone of the dentate gyrus.)
*   **Adult neurogenesis (review):** Ming, G.-L., Song, H. (2011).
    "Adult neurogenesis in the mammalian brain: significant
    answers and significant questions." *Neuron* 70:687–702.
    (Subgranular zone as one of the two canonical adult neurogenic
    niches.)
*   **Granule-cell dispersion and mossy-fiber sprouting in
    epilepsy:** Houser, C.R. (1990). "Granule cell dispersion in
    the dentate gyrus of humans with temporal lobe epilepsy."
    *Brain Research* 535:195–204. (Granule-cell dispersion in
    temporal lobe epilepsy.)
*   **Mossy-fiber sprouting in epilepsy:** Tauck, D.L., Nadler,
    J.V. (1985). "Evidence of functional mossy fiber sprouting in
    hippocampal formation of kainic acid-treated rats." *Journal
    of Neuroscience* 5:1016–1022. (Mossy-fiber sprouting in the
    epileptogenic dentate gyrus.)
*   **Hippocampal sclerosis (dentate component):** Mathern, G.W.,
    Babb, T.L., Vickrey, B.G., Melendez, M., Pretorius, J.K.
    (1995). "The clinical-pathogenic mechanisms of hippocampal
    neuron loss and surgical outcomes in temporal lobe epilepsy."
    *Brain* 118:105–118. (Dentate granule-cell dispersion and
    mossy-fiber sprouting in Ammon's horn sclerosis.)
*   **Alzheimer's disease and the entorhinal-dentate axis:** Braak,
    H., Braak, E. (1991). "Neuropathological stageing of
    Alzheimer-related changes." *Acta Neuropathologica*
    82:239–259. (Entorhinal cortex as the earliest affected
    structure; dentate gyrus downstream.)
*   **Depression and adult neurogenesis (contested):** Santarelli,
    L., et al. (2003). "Requirement of hippocampal neurogenesis
    for the behavioral effects of antidepressants." *Science*
    301:805–809. (Reduced adult neurogenesis in depression —
    contested.)
*   **Aging and adult neurogenesis:** Kuhn, H.G., Dickinson-Anson,
    H., Gage, F.H. (1996). "Neurogenesis in the dentate gyrus of
    the adult rat: age-related decrease of neuronal progenitor
    proliferation." *Journal of Neuroscience* 16:2027–2033.
    (Age-related decline of adult neurogenesis in the dentate
    gyrus.)
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
*   **Amygdala (contrast — the dentate gyrus is NOT the amygdala):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Amygdala fear circuit —
    distinct from the hippocampus memory circuit.)
*   **SLEA (contrast — the dentate gyrus is not included):** Alheid,
    G.F., Heimer, L. (1988). "New perspectives in basal forebrain
    organization of special relevance for neuropsychiatric
    disorders." *Neuroscience* 27:1–39. (SLEA continuum — BNST,
    central nucleus, ventral pallidum, nucleus accumbens; NOT the
    dentate gyrus.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Dentate gyrus in overview.)
*   NeuroNames — Dentate gyrus (right); FMA — Dentate gyrus (right
    member).
"""