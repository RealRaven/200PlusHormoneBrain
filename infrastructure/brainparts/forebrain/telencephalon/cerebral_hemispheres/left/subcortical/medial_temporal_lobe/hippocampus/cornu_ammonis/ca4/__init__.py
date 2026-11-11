"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca4
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
                            └── ca4   <-- THIS MODULE

**Primary synonym:** CA4 (left); CA4 field; CA4 subfield; CA4 region;
fourth CA field; **polymorphic layer of the dentate gyrus**;
**dentate hilus**; **hilus**; **endal blade of the dentate gyrus**.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**leaf subfield** of the **cornu ammonis** — the **polymorphic
layer (hilus) of the dentate gyrus** in standard anatomical usage,
containing the **mossy cells** and receiving the **mossy fibers**
from the dentate granule cells. Wired under the **cornu_ammonis**
container by the tree; documented anatomically as the **dentate
hilus** in *CA4 / Dentate Hilus Note*.
**Part of:** The **cornu_ammonis** container — the **CA field
system** of the hippocampus. The **CA4** is the **dentate hilus**
— the **mossy-cell** layer of the dentate gyrus — wired under the
cornu ammonis by the tree.
**Structural parent:** ``.../cornu_ammonis/`` → **direct child** of
the cornu ammonis container.
**Structural children:** **None.** This is a **leaf** module. The
**mossy cells**, **hilar interneurons**, and **mossy fibers** of
CA4 are documented as **prose**, not as structural children.
**Boundary status (DENTATE HILUS — the polymorphic layer of the
dentate gyrus, NOT the CA1/CA2/CA3 pyramidal fields):** **Boundary
case — the ca4 is the DENTATE HILUS — the polymorphic layer of the
dentate gyrus — NOT the CA1, CA2, or CA3 pyramidal fields.** The
**CA1** sibling (``.../ca1/``) is the **principal-output**
subfield. The **CA2** sibling (``.../ca2/``) is the
**social-memory** subfield. The **CA3** sibling (``.../ca3/``) is
the **pattern-completion** subfield. The **CA4** (here) is the
**dentate hilus** — the **mossy-cell** layer of the dentate gyrus.
**CA4 is the ONLY CA field that is a DENTATE-GYRUS layer** — it is
**not** a pyramidal-cell field in the same sense as CA1–CA3, and
its principal neurons are **mossy cells** (excitatory hilar
neurons), not **pyramidal cells**. Consumers must **not** conflate
CA4 with CA1, CA2, or CA3.
**Boundary status (TREE-WIRED UNDER CORNU AMMONIS — NOT under
dentate_gyrus):** **Boundary case — the ca4 is TREE-WIRED UNDER
``cornu_ammonis``, NOT under ``dentate_gyrus``.** Although **CA4**
is the **dentate hilus** anatomically, the **tree** places
``ca4`` under **``.../cornu_ammonis/``**. Consumers must
**resolve CA4 under ``.../cornu_ammonis/ca4/``** — **not** under
``.../hippocampus/dentate_gyrus/``. The **dentate-hilus**
relationship is documented as **prose** in *CA4 / Dentate Hilus
Note*. Consumers must **not** attempt to resolve CA4 under the
dentate gyrus container.
**Boundary status (NOT the dentate gyrus proper — the dentate
gyrus proper is the GRANULE-CELL layer, wired under
``dentate_gyrus/``):** **Boundary case — the ca4 is NOT the
dentate gyrus proper; the dentate gyrus proper is the
GRANULE-CELL layer, wired under ``.../hippocampus/dentate_gyrus/``.**
The **dentate_gyrus** (``.../hippocampus/dentate_gyrus/``) is the
**granule-cell layer** — the **principal input** of the hippocampus
(entorhinal cortex → perforant path → dentate gyrus → mossy fibers
→ CA3 / CA4) and the **principal site** of **pattern separation**
and **adult neurogenesis**. The **CA4** (here) is the **dentate
hilus** — the **polymorphic layer** that **receives** the
**mossy fibers** from the **dentate granule cells**. **They are
DIFFERENT LAYERS** — the **dentate gyrus proper** is the
**granule-cell layer**; **CA4** is the **hilus** (the
**polymorphic cell layer** *between* the granule-cell layer and
CA3). Consumers must **not** conflate CA4 with the dentate gyrus
proper — they are **different layers** of the **same** dentate
complex.
**Boundary status (NOT CA3 — CA3 is the pyramidal-cell layer that
receives the mossy fibers, CA4 is the hilus):** **Boundary case —
the ca4 is NOT CA3; CA3 is the pyramidal-cell layer that receives
the mossy fibers, CA4 is the hilus.** The **CA3** sibling is the
**pattern-completion** subfield — the **pyramidal-cell layer**
that receives the **mossy fibers** in the **stratum lucidum** and
projects the **Schaffer collaterals** to CA1. The **CA4** (here) is
the **hilus** — the **polymorphic cell layer** that contains the
**mossy cells** and is the **target** of the **mossy fibers**
*before* they reach CA3, and a **relay** back to the **dentate
granule cells**. **CA4 is upstream/parallel to CA3 in the
mossy-fiber stream** — the **dentate granule cells** project to
**both CA3 and CA4** via the **mossy fibers**. Consumers must
**not** conflate CA4 with CA3.
**Boundary status (MOSSY CELLS — NOT pyramidal cells; the
distinctive principal neurons of CA4):** **Boundary case — the
ca4's principal neurons are MOSSY CELLS, NOT pyramidal cells.**
The **CA1**, **CA2**, and **CA3** subfields have **pyramidal
cells** as their principal neurons. The **CA4** (here) has **mossy
cells** as its principal neurons — **large, excitatory hilar
neurons** that **project** to the **dentate granule cells** (back)
and to **CA3**. **CA4 is the ONLY CA field with mossy cells as
its principal neurons.** Consumers must **not** treat CA4 as "CA3
with different inputs" or "another pyramidal-cell field" — its
**mossy cells** are its **distinctive identity**.
**Boundary status (VULNERABLE to mossy-cell loss in epilepsy — NOT
the CA1 ischemia profile or the CA2 resistant profile):**
**Boundary case — the ca4 is VULNERABLE to mossy-cell loss in
epilepsy, NOT the CA1 ischemia profile or the CA2 resistant
profile.** The **CA1** sibling is the **most vulnerable** CA field
to **ischemia** and **hypoxia** — its **principal neurons**
(pyramidal cells) are lost in **CA1 sclerosis**. The **CA2**
sibling is **relatively resistant** and **spared** in
**hippocampal sclerosis**. The **CA3** sibling is **vulnerable** to
**seizure-induced** and **excitotoxic** damage. The **CA4** (here)
is **vulnerable** to **mossy-cell loss** in **temporal lobe
epilepsy** — the **mossy cells** are **lost** in **Ammon's horn
sclerosis**, and **mossy-cell loss** is a **hallmark** of
**epileptogenic** hippocampus. Consumers must **not** assume CA4
shares CA1's **ischemia** profile or CA2's **relative
resistance** — its **vulnerability** is **mossy-cell loss in
epilepsy**.
**Boundary status (NOT the subiculum — the subiculum is the OUTPUT
TARGET of CA1):** **Boundary case — the ca4 is NOT the subiculum;
the subiculum is the OUTPUT TARGET of CA1.** The **subiculum**
(``.../hippocampus/subiculum/``) is the **principal output** of the
hippocampus to the parahippocampal region, the mammillary bodies
(via the fornix), and the prefrontal cortex — **CA1 projects to
the subiculum**. The **CA4** (here) is the **dentate hilus** —
**upstream/parallel to CA3** in the mossy-fiber stream. Consumers
must **not** conflate CA4 with the subiculum.
**Boundary status (NOT the cornu ammonis container — CA4 is a CHILD
of the cornu ammonis):** **Boundary case — the ca4 is a CHILD of
the cornu_ammonis container, not the container itself.** The
**cornu ammonis** container contains **CA1**, **CA2**, **CA3**, and
**CA4** — the **CA4** is **one** of those four children. Consumers
must **not** conflate CA4 with the cornu ammonis container.
**Boundary status (NOT the hippocampus container — CA4 is a
grandchild of the hippocampus):** **Boundary case — the ca4 is a
GRANDCHILD of the hippocampus container.** The **hippocampus**
container contains the **cornu ammonis**, the **dentate gyrus**,
the **parasubiculum**, the **presubiculum**, and the **subiculum**
— and the **cornu ammonis** in turn contains **CA1–CA4**. The
**CA4** is a **child of the cornu ammonis**, and thus a
**grandchild** of the hippocampus. Consumers must **not** conflate
CA4 with the hippocampus container.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the ca4 is NOT the
parahippocampal region.** The **parahippocampal region** (the
**entorhinal cortex**, the **perirhinal cortex**, and the
**parahippocampal gyrus**) is **cortical** — it is wired under
``.../left/cortex/temporal/gyri/`` and is **outside** the
hippocampus container. The **CA4** (here) is the **dentate
hilus** — an **archicortex/dentate** structure. Consumers must
**not** conflate CA4 with the parahippocampal region.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the ca4 is NOT the
fornix or the white matter; the fornix and the white_matter are
WHITE-MATTER structures.** The **fornix**
(``.../left/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../left/white_matter/``) is the **white-matter
infrastructure**. The **CA4** (here) is the **grey-matter dentate
hilus**. Consumers must **not** conflate the two. Note also that
the **mossy fibers** are **intra-hippocampal** axonal projections —
they are **not** the **fornix** and **not** the **white_matter**.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the ca4 is NOT the rhinencephalon.** The **rhinencephalon**
(``.../left/cortex/rhinencephalon/``) — the olfactory bulb,
olfactory tract, piriform cortex, periamygdaloid cortex, anterior
olfactory nucleus, and uncus — is the **cortical olfactory lobe**.
The **CA4** (here) is the **dentate hilus** — part of the
**archicortex** of episodic memory and spatial navigation. It is
**not** an olfactory structure. Consumers must **not** conflate the
two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the ca4 is
NOT the amygdala; the amygdala is the FEAR/EMOTION/SALIENCE
container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), the
**lateral nucleus** (sensory input), and the **medial nucleus**
(olfactory/pheromone). The **CA4** (here) is the **dentate hilus**
of the **memory** container. Consumers must **not** conflate CA4
with the amygdala.
**Boundary status (SLEA-FREE — CA4 is NOT an extended-amygdala
component):** **Boundary case — the ca4 is SLEA-FREE.** The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere). The
**CA4** is an **episodic/declarative-memory and
spatial-navigation** structure — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into CA4 — it is
**SLEA-free**.
**Boundary status (NOT the memory software layer — CA4 is the BRAIN
STRUCTURE, not the ``memory/`` package):** **Boundary case — the
ca4 is the BRAIN STRUCTURE, NOT the ``memory/`` software package.**
The **``memory/`` package** (``memory/stores/`` — episodic,
semantic, procedural, working; ``memory/backends/`` — chroma,
in_memory) is the **software memory layer** of the simulation. The
**CA4** (here) is the **brain structure** that **subserves** the
dentate-hilus contribution to episodic memory. Consumers must
**not** conflate the two — the **brain structure** is wired here;
the **software store** is wired under ``memory/``.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
ca4 is NOT the fear-output or the fear-learning structures.** The
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), and the **basomedial nuclei** (fear-modulatory)
are **amygdala** children. The **CA4** is the **dentate hilus** of
the **memory** container — it is **not** a fear-output or
fear-learning structure. Consumers must **not** conflate CA4 with
the **amygdala fear circuit**.
**Boundary status (NOT a single uniform layer — MULTIPLE cell
types):** **Boundary case — the ca4 is a HETEROGENEOUS layer with
MULTIPLE cell types (mossy cells, hilar interneurons, mossy-fiber
synapses), not a single uniform layer.** The **mossy cells** are
the **principal neurons** — the **excitatory hilar neurons** that
project to the **dentate granule cells** (back) and to **CA3**.
The **hilar interneurons** — the **GABAergic inhibitory neurons**
— are the **local-circuit** neurons of the hilus. The **mossy
fibers** are the **dentate granule-cell axons** that **synapse**
in the hilus **before** projecting to CA3. The tree wires the
**CA4** as a **single leaf** under the cornu ammonis — the **cell
types** are **prose**, not structural children. Consumers that
need **cell-type-level** resolution should consult the
references, not the tree.

Overview
--------
CA4 is the **polymorphic layer (hilus) of the dentate gyrus** — the
**mossy-cell** layer that **receives** the **mossy fibers** from
the dentate granule cells and **projects** back to the dentate
granule cells and to CA3. It is a **leaf** module under the cornu
ammonis container by the tree, the **sibling of CA1, CA2, and
CA3**, and the **grey-matter substrate** of the **dentate-hilus
contribution** to the **mossy-fiber circuit** — the **dentate
hilus** that gates mossy-fiber throughput and supports
**mossy-cell** feedback.

**CA4 is the DENTATE HILUS — the polymorphic layer of the dentate
gyrus, NOT the CA1, CA2, or CA3 pyramidal fields.** **CA1**
(sibling) is the **principal-output** subfield. **CA2** (sibling)
is the **social-memory** subfield. **CA3** (sibling) is the
**pattern-completion** subfield. **CA4 is the dentate hilus** — the
**mossy-cell** layer of the dentate gyrus.

**CA4 is TREE-WIRED UNDER ``cornu_ammonis``, NOT under
``dentate_gyrus``.** Although **CA4** is the **dentate hilus**
anatomically, the **tree** places ``ca4`` under
**``.../cornu_ammonis/``**. Consumers must **resolve CA4 under
``.../cornu_ammonis/ca4/``** — **not** under
``.../hippocampus/dentate_gyrus/``. The **dentate-hilus**
relationship is documented as **prose** in *CA4 / Dentate Hilus
Note*.

**CA4 is NOT the dentate gyrus proper.** The **dentate gyrus
proper** is the **granule-cell layer**, wired under
``.../hippocampus/dentate_gyrus/``. **CA4** is the **hilus** — the
**polymorphic cell layer** *between* the granule-cell layer and
CA3. **They are DIFFERENT LAYERS of the same dentate complex.**

**CA4 is NOT CA3.** **CA3** is the **pyramidal-cell layer** that
receives the **mossy fibers** in the **stratum lucidum** and
projects the **Schaffer collaterals** to CA1. **CA4** is the
**hilus** — the **polymorphic cell layer** that receives the
**mossy fibers** *before* they reach CA3. **The dentate granule
cells project to BOTH CA3 and CA4 via the mossy fibers** — CA4 is
**upstream/parallel to CA3** in the mossy-fiber stream.

**CA4's principal neurons are MOSSY CELLS, NOT pyramidal cells.**
**CA1**, **CA2**, and **CA3** have **pyramidal cells** as their
principal neurons. **CA4** has **mossy cells** as its principal
neurons — **large, excitatory hilar neurons** that **project** to
the **dentate granule cells** (back) and to **CA3**. **CA4 is the
ONLY CA field with mossy cells as its principal neurons.**

**CA4 is VULNERABLE to mossy-cell loss in epilepsy, NOT the CA1
ischemia profile or the CA2 resistant profile.** **CA4** is
**vulnerable** to **mossy-cell loss** in **temporal lobe
epilepsy** — the **mossy cells** are **lost** in **Ammon's horn
sclerosis**, and **mossy-cell loss** is a **hallmark** of
**epileptogenic** hippocampus.

**CA4 is NOT the subiculum.** **CA1 projects to the subiculum** —
the **subiculum** is the **output target**. **CA4** is the
**dentate hilus** — **upstream/parallel to CA3** in the
mossy-fiber stream.

**CA4 is NOT the cornu ammonis container or the hippocampus
container.** The **cornu ammonis** container contains **CA1–CA4**;
the **hippocampus** container contains the **cornu ammonis**, the
**dentate gyrus**, and the **subicular complex**.

**CA4 is NOT the parahippocampal region.** The **entorhinal
cortex**, **perirhinal cortex**, and **parahippocampal gyrus** are
**cortical** — they are wired under ``cortex/temporal/gyri/``.
**CA4** is the **dentate hilus** — an **archicortex/dentate**
structure.

**CA4 is SLEA-FREE.** It is **not** an extended-amygdala component,
and it carries **no SLEA warning**. The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere).

**CA4 is the BRAIN STRUCTURE, not the ``memory/`` software
package.** The **``memory/`` package** is the **software memory
layer**. **CA4** is the **brain region** whose function the
episodic store models. **They are DIFFERENT LAYERS.**

**CA4 is a paired structure.** Each hemisphere has its own CA4,
with **ipsilateral** and **bilateral** connections to the dentate
gyrus, CA3, the entorhinal cortex, and the contralateral CA4. The
two sides are **bilaterally symmetric** and **partially
lateralized** — the **left** CA4 is more involved in **verbal**
episodic memory, and the **right** CA4 is more involved in
**spatial/nonverbal** episodic memory. This is **well-documented**
(not contested), and documented in the **medial temporal lobe
module** (not at the CA4 level). See *Lateralization Notes*.

CA4 / Dentate Hilus Note
------------------------
**CA4** is the **polymorphic layer (hilus) of the dentate gyrus**
in standard anatomical usage — the layer that contains the **mossy
cells** and receives the **mossy fibers** from the **dentate
granule cells**. The **tree nests ``ca4`` under
``cornu_ammonis``**, and consumers should **resolve it there** —
the tree's placement is honored structurally. The **dentate-hilus**
relationship is documented here as **prose**:

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

Cell-Type Composition (prose, not structural children)
------------------------------------------------------
CA4 is a **heterogeneous layer** — documented as **prose**, not as
structural children:

*   **Mossy cells** — the **principal neurons** of CA4 — **large,
    excitatory hilar neurons** that project to the **dentate
    granule cells** (back) and to **CA3**.

*   **Hilar interneurons** — the **GABAergic inhibitory neurons**
    of the hilus — the **local-circuit** neurons that shape
    mossy-fiber throughput.

*   **Mossy-fiber synapses** — the **dentate granule-cell axons**
    that **synapse** in the hilus **before** projecting to CA3.

**These cell types are prose, not structural children.** The tree
wires **CA4** as a **single leaf** under the cornu ammonis — the
**cell types** are **prose**, not structural children. Consumers
that need **cell-type-level** resolution should consult the
references, not the tree.

The CA4 / CA1, CA2, CA3 Boundary
--------------------------------
This is the **sibling CA-field** boundary:

*   **CA4** (this module) — the **dentate hilus** (mossy cells;
    mossy-fiber target; vulnerable to mossy-cell loss in epilepsy).

*   **CA1** (``.../cornu_ammonis/ca1/``) — the **principal-output**
    subfield (CA1 → subiculum; entorhinal cortex; prefrontal
    cortex); the **most vulnerable** CA field to **ischemia** and
    **hypoxia**.

*   **CA2** (``.../cornu_ammonis/ca2/``) — the **social-memory**
    subfield (oxytocin-receptor enriched); **relatively resistant**
    to excitotoxic damage.

*   **CA3** (``.../cornu_ammonis/ca3/``) — the
    **pattern-completion** subfield (recurrent collaterals;
    **mossy-fiber** input; **Schaffer** output to CA1; vulnerable
    to seizures and excitotoxicity).

**They are SIBLINGS under the cornu ammonis, and they are DIFFERENT
CA FIELDS.** Consumers must **not** conflate CA4 with CA1, CA2, or
CA3 — the **cell types differ** (CA4 has **mossy cells**; CA1–CA3
have **pyramidal cells**), the **vulnerability profiles differ**
(CA4 mossy-cell loss in epilepsy; CA1 ischemia; CA2 resistant;
CA3 seizure/excitotoxic), and the **connectivity differs** (CA4 is
the **hilus**, upstream/parallel to CA3 in the mossy-fiber stream).

The CA4 / Dentate Gyrus Boundary
--------------------------------
This is the **dentate-hilus vs. dentate-granule-cell-layer**
boundary:

*   **CA4** (this module) — the **dentate hilus** (the
    **polymorphic cell layer** *between* the granule-cell layer
    and CA3).

*   **Dentate gyrus** (``.../hippocampus/dentate_gyrus/``) — the
    **granule-cell layer** (the **principal input** of the
    hippocampus; **pattern separation**; **adult neurogenesis**;
    **mossy-fiber** source).

**They are DIFFERENT LAYERS of the same dentate complex** — the
**dentate gyrus proper** is the **granule-cell layer**; **CA4** is
the **hilus** (the **polymorphic cell layer** between the
granule-cell layer and CA3). The **mossy fibers** project from the
**dentate granule cells** to **both CA3 and CA4**. Consumers must
**not** conflate CA4 with the dentate gyrus proper.

The CA4 / Subiculum Boundary
----------------------------
This is the **dentate hilus vs. output target** boundary:

*   **CA4** (this module) — the **dentate hilus**.

*   **Subiculum** (``.../hippocampus/subiculum/``) — the **output
    target** of CA1 (the subiculum projects to the parahippocampal
    region, the mammillary bodies, and the prefrontal cortex).

**They are DIFFERENT STRUCTURES** — **CA4** is the **dentate
hilus**; the **subiculum** is a **sibling subfield** of the
hippocampus. Consumers must **not** conflate the two.

The CA4 / Cornu Ammonis Boundary
--------------------------------
This is the **child vs. container** boundary:

*   **CA4** (this module) — a **child** of the cornu ammonis
    container.

*   **Cornu ammonis** (``.../cornu_ammonis/``) — the **container**
    that contains **CA1**, **CA2**, **CA3**, and **CA4**.

**CA4 is ONE of the four children of the cornu ammonis.** Consumers
must **not** conflate CA4 with the cornu ammonis container.

The CA4 / Hippocampus Boundary
------------------------------
This is the **grandchild vs. container** boundary:

*   **CA4** (this module) — a **grandchild** of the hippocampus
    container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**CA4 is a grandchild of the hippocampus** (child of the cornu
ammonis). Consumers must **not** conflate CA4 with the hippocampus
container.

The CA4 / Parahippocampal Region Boundary
-----------------------------------------
This is the **dentate hilus vs. cortical interface** boundary:

*   **CA4** (this module) — the **dentate hilus** (an
    **archicortex/dentate** structure).

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../left/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus.** **CA4** is the **dentate hilus** — a **local
hilar layer** inside the hippocampus. Consumers must **not**
conflate CA4 with the parahippocampal region.

The CA4 / Fornix and White Matter Boundary
------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **CA4** (this module) — the **grey-matter** dentate hilus.

*   **Fornix** (``.../left/white_matter/fornix/``) and
    **white_matter** (``.../left/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — **CA4** is the **grey-matter
dentate hilus**; the **fornix** and the **white_matter** are the
**white-matter tracts**. Note also that the **mossy fibers** are
**intra-hippocampal** axonal projections — they are **not** the
**fornix** and **not** the **white_matter**. Consumers must **not**
conflate the two.

The CA4 / Rhinencephalon Boundary
---------------------------------
This is the **dentate hilus vs. olfactory lobe** boundary:

*   **CA4** (this module) — the **dentate hilus**.

*   **Rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — **CA4** is the **dentate
hilus** (memory/navigation); the **rhinencephalon** is the
**olfactory lobe**. Consumers must **not** conflate the two.

The CA4 / Amygdala Boundary
---------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **CA4** (this module) — a **CA field** of the **memory**
    container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; **CA4** is a **child of the memory**
container. Consumers must **not** conflate the two.

The CA4 / Memory Software Layer Boundary
----------------------------------------
This is the **brain structure vs. software store** boundary:

*   **CA4** (this module) — the **brain structure** (dentate
    hilus) that subserves episodic memory.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — **CA4** is the **brain region**;
the **``memory/`` package** is the **software store**. Consumers
must **not** conflate the two.

The CA4 / SLEA Boundary
-----------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **CA4** (this module) — **SLEA-FREE**. No extended-amygdala
    relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**CA4 is NOT part of the SLEA continuum.** It is an
**episodic/declarative-memory and spatial-navigation** structure,
and it carries **no SLEA warning**. Consumers must **not** import
the SLEA warning into CA4.

Function in the Human Brain
---------------------------
CA4's functions are **dentate-hilus throughput**, **mossy-cell
feedback**, and **mossy-fiber gating** — **NOT episodic-memory
output and NOT fear-output**:

*   **Dentate-Hilus Throughput (Mossy-Fiber Gating):** **CA4** is
    the **hilus** — the **polymorphic cell layer** that the
    **mossy fibers** pass through **before** reaching CA3. The
    **hilar interneurons** (GABAergic) **gate** the mossy-fiber
    throughput — this is the **gating** substrate of the dentate
    hilus.

*   **Mossy-Cell Feedback (Hilus → Dentate Granule Cells):** The
    **mossy cells** of CA4 project **back** to the **dentate
    granule cells** — the **excitatory feedback** loop that
    **shapes** the **dentate-gyrus output**. This is the
    **feedback** substrate of the dentate hilus.

*   **Mossy-Fiber Target (Dentate Granule Cells → CA4):** **CA4**
    is the **target** of the **mossy fibers** from the **dentate
    granule cells** — the **hilar relay** of the mossy-fiber
    stream. This is the **input** side of the CA4 computation.

*   **Mossy-Cell Projection to CA3:** The **mossy cells** of CA4
    project to **CA3** — the **hilar-to-CA3** projection that
    **relays** the dentate-hilus signal to the pattern-completion
    subfield. This is the **output** side of the CA4 computation.

*   **NOT a neural processor in the classical sense.** **CA4** is
    a **dentate-hilus** structure — it **gates** and **relays**
    the **mossy-fiber** signal, but it does **not** produce the
    **fear-output** or the **autonomic and behavioral** fear
    responses. The **fear-output** is the **central nucleus**; the
    **fear-learning** structures are the **basolateral nuclei**.

**The unifying theme:** CA4 is the **dentate hilus** of the
**cornu ammonis** container — the **polymorphic cell layer** that
anchors **dentate-hilus throughput, mossy-cell feedback, and
mossy-fiber gating**. It is **SLEA-free**,
**memory/navigation**, and **NOT the fear-output structure** — the
**fear-output** is the **central nucleus**, the **fear-learning**
structures are the **basolateral nuclei**, and **CA4** is the
**dentate hilus** of the **memory** container.

Associated Disorders
--------------------
CA4 has **no named "CA4 syndrome"** in the narrow sense, but its
clinical associations are **well-documented**:

*   **Temporal Lobe Epilepsy (Mossy-Cell Loss):** **CA4** shows
    **mossy-cell loss** in **temporal lobe epilepsy** —
    **mossy-cell loss** is a **hallmark** of **Ammon's horn
    sclerosis**, and it is **well-documented** in **epileptogenic**
    hippocampus. **CA4** is the **epileptogenic substrate** of
    temporal lobe epilepsy via the **mossy-cell** circuit.

*   **Hippocampal Sclerosis (Ammon's Horn Sclerosis — Mossy-Cell
    Loss Component):** **CA4** contributes the **mossy-cell loss**
    component of **hippocampal sclerosis** — alongside the **CA1
    pyramidal-cell loss** and the **CA3 pyramidal-cell loss**, the
    **CA4 mossy-cell loss** is part of the **classic** Ammon's
    horn sclerosis. **CA2** is **relatively spared**.

*   **Traumatic Brain Injury (Mossy-Cell Vulnerability):** **CA4**
    mossy cells are **vulnerable** to **traumatic brain injury**
    (TBI) — **mossy-cell loss** and **hilar network dysfunction**
    are **reported** after **TBI**, contributing to
    **post-traumatic epilepsy**.

*   **Pattern-Completion Deficits (Mossy-Cell Loss — Indirect):**
    **CA4 mossy-cell loss** contributes to
    **pattern-completion deficits** — the **hilar feedback** and
    **hilar-to-CA3** projection are **disrupted**, contributing to
    the **pattern-completion** failure that follows **mossy-cell
    loss**.

*   **No Named "CA4 Syndrome":** **CA4** is the **dentate hilus**
    — a **layer** of the dentate complex, not a **single
    functional system** — it has **no named clinical syndrome**.
    Its clinical relevance is **direct** for **temporal lobe
    epilepsy** and **hippocampal sclerosis**, and **reported** for
    **traumatic brain injury** and **pattern-completion
    deficits**.

**What is NOT here:** **CA4** is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **fear conditioning** (central nucleus + basolateral
nuclei), or **fear extinction** (ventromedial prefrontal cortex +
basomedial nuclei). Its clinical relevance is **direct** for
**temporal lobe epilepsy** and **hippocampal sclerosis**, and
**reported** for **traumatic brain injury**.

Lateralization Notes
--------------------
This is the **left** CA4 module. **CA4** is **bilaterally
symmetric** and **partially lateralized** — and it carries **NO
warning**:

*   **Bilateral CA4 Function:** Each hemisphere has its own CA4,
    with **ipsilateral** and **bilateral** connections to the
    dentate gyrus, CA3, the entorhinal cortex, and the
    contralateral CA4. The two sides are **functionally symmetric**
    for **basic memory and navigation**.

*   **Partial Lateralization (Well-Documented — Verbal vs.
    Spatial):** The **left** CA4 is **more involved in verbal**
    episodic memory (word lists, stories, verbal recognition); the
    **right** CA4 is **more involved in spatial/nonverbal**
    episodic memory (spatial layouts, faces, nonverbal
    recognition). This is **well-documented**, **not contested**,
    and is documented in the **medial temporal lobe module** (not
    at the CA4 level).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** **CA4** is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into CA4.

*   **NO Amygdala-Lateralization Warning of their own (CA4 is the
    DENTATE HILUS, not the fear-output):** The **right-amygdala
    fear association** belongs to the **amygdala module** —
    specifically the **central nucleus** (fear-output) and the
    **basolateral nuclei** (fear-learning). **CA4** is the
    **dentate hilus** — consumers must **not** conflate it with the
    **whole amygdala** or with the **central nucleus**. **CA4** is
    the **dentate hilus**, not the **fear circuit**.

**A consumer that assumes "left CA4 = right CA4" will be
structurally correct** — the two sides are **symmetric** and
**partially lateralized** (the lateralization is documented in the
medial temporal lobe module). **CA4** is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cornu_ammonis/ca1/``, ``.../cornu_ammonis/ca2/``,
    ``.../cornu_ammonis/ca3/``,
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
    container. **CA4**'s relationships to CA1, CA2, CA3, the
    dentate gyrus, the subiculum, the parasubiculum, the
    presubiculum, the amygdala, the parahippocampal region, the
    fornix, the rhinencephalon, and the ``memory/`` package are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **mossy cells**,
    **hilar interneurons**, and **mossy-fiber synapses** of CA4
    are documented as **prose**, not as sub-modules. Consumers must
    not assume any exist as children; resolve cell-type-level
    detail through the references.
*   **DENTATE HILUS — the polymorphic layer of the dentate gyrus,
    NOT the CA1/CA2/CA3 pyramidal fields.** **CA4** is the
    **dentate hilus**; **CA1** (sibling) is the **principal
    output**; **CA2** (sibling) is the **social-memory** subfield;
    **CA3** (sibling) is the **pattern-completion** subfield.
    Consumers must **not** conflate CA4 with any of its sibling CA
    fields.
*   **TREE-WIRED UNDER ``cornu_ammonis`` — NOT under
    ``dentate_gyrus``.** Consumers must **resolve CA4 under
    ``.../cornu_ammonis/ca4/``** — **not** under
    ``.../hippocampus/dentate_gyrus/``.
*   **NOT the dentate gyrus proper — the dentate gyrus proper is
    the GRANULE-CELL layer, wired under ``dentate_gyrus/``.**
    Consumers must **not** conflate CA4 with the dentate gyrus
    proper.
*   **NOT CA3 — CA3 is the pyramidal-cell layer that receives the
    mossy fibers, CA4 is the hilus.**
*   **MOSSY CELLS — NOT pyramidal cells; the distinctive principal
    neurons of CA4.** Consumers must **not** treat CA4 as "CA3
    with different inputs" or "another pyramidal-cell field."
*   **VULNERABLE to mossy-cell loss in epilepsy — NOT the CA1
    ischemia profile or the CA2 resistant profile.**
*   **NOT the subiculum — the subiculum is the OUTPUT TARGET of
    CA1.** Consumers must **not** conflate CA4 with the subiculum.
*   **NOT the cornu ammonis container — CA4 is a CHILD of the
    cornu ammonis.**
*   **NOT the hippocampus container — CA4 is a GRANDCHILD of the
    hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; **CA4** is the **dentate hilus**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** **CA4** is the **grey-matter dentate hilus**;
    the **mossy fibers** are **intra-hippocampal** projections —
    not the fornix and not the white_matter.
*   **NOT the rhinencephalon.** **CA4** is **not** an olfactory
    structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** **CA4** is
    **not** an extended-amygdala component, and it carries **no
    SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; **CA4** is the
    **dentate hilus** of the **memory** container.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; **CA4** is the **brain
    structure**. Consumers must **not** conflate the two.
*   **NOT a single uniform layer — MULTIPLE cell types.** The
    **mossy cells**, **hilar interneurons**, and **mossy-fiber
    synapses** are **prose**, not structural children.
*   **No ``AREA_PATHS`` hop.** **CA4** is a local leaf under the
    cornu ammonis, not a cross-listed leaf.
*   **No nested cross-listing.** **CA4** has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with right CA4 — strict mirror with NO
    warning.** Left and right CA4 modules are **structurally
    identical** — same **leaf** status, same **dentate-hilus**
    framing, same **SLEA-free** status, same **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis import ca4

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "medial_temporal_lobe.hippocampus.cornu_ammonis.ca4"
    )

**Do not** assume CA4 is a **pyramidal-cell field**. CA4's
principal neurons are **mossy cells** — the **only** CA field with
mossy cells as its principal neurons.

**Do not** assume CA4 is **CA1**, **CA2**, or **CA3**. Those are
the **pyramidal-cell CA fields** — CA1 (principal output), CA2
(social memory), CA3 (pattern completion). **CA4** is the
**dentate hilus**.

**Do not** assume CA4 is the **dentate gyrus proper**. The
**dentate gyrus proper** is the **granule-cell layer**; **CA4** is
the **hilus** — the **polymorphic cell layer** *between* the
granule-cell layer and CA3. They are **different layers** of the
same dentate complex.

**Do not** resolve CA4 under ``.../hippocampus/dentate_gyrus/``.
CA4 is **wired under ``.../cornu_ammonis/ca4/``** in the tree —
the **dentate-hilus** relationship is **prose**.

**Do not** assume CA4 is the **subiculum**. The **subiculum** is
the **output target** of CA1; **CA4** is the **dentate hilus**.

**Do not** assume CA4 is the **cornu ammonis container** or the
**hippocampus container**. **CA4** is a **child of the cornu
ammonis** and a **grandchild of the hippocampus**.

**Do not** assume CA4 is the **parahippocampal region**. The
**entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; **CA4** is
the **dentate hilus**.

**Do not** assume CA4 is the **fornix** or the **white_matter**.
Those are **white-matter tracts**; **CA4** is the **grey-matter
dentate hilus**; the **mossy fibers** are **intra-hippocampal**
projections.

**Do not** assume CA4 is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; **CA4** is
the **dentate hilus**.

**Do not** assume CA4 is the **``memory/`` software package**. The
**``memory/`` package** is the **software store**; **CA4** is the
**brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into CA4. **CA4 is SLEA-FREE**
— it is **not** an extended-amygdala component, and it is **NOT
the fear-output structure**.

Iterating CA4's (empty) children (recommended consumer pattern)::

    CA4_CHILDREN = ()
    # CA4 is a leaf. The mossy cells, hilar interneurons, and
    # mossy-fiber synapses are prose, not modules.

Reaching the CA1, CA2, CA3 siblings (recommended consumer pattern —
the sibling CA fields)::

    # CA1, CA2, and CA3 are the SIBLING CA fields under the cornu
    # ammonis:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca1
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca2
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca3
    #
    # CA4 is the DENTATE HILUS; CA1 is the PRINCIPAL OUTPUT; CA2 is
    # the SOCIAL-MEMORY subfield; CA3 is the PATTERN-COMPLETION
    # subfield.

Reaching the dentate gyrus (recommended consumer pattern — the
dentate-granule-cell layer)::

    # The dentate gyrus is the GRANULE-CELL layer — the sibling of
    # the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
    #
    # The dentate gyrus is the GRANULE-CELL layer (the INPUT;
    # pattern separation; adult neurogenesis; mossy-fiber source);
    # CA4 is the DENTATE HILUS (the polymorphic layer *between*
    # the granule-cell layer and CA3).

Reaching the subiculum (recommended consumer pattern — the output
target of CA1)::

    # The subiculum is the OUTPUT TARGET of CA1 — the sibling of
    # the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # CA1 projects to the subiculum; CA4 is the dentate hilus.

Reaching the cornu ammonis (recommended consumer pattern — the
container)::

    # The cornu ammonis is the CONTAINER that contains CA1, CA2,
    # CA3, and CA4:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
    #
    # CA4 is ONE of the four children of the cornu ammonis.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the cornu
    # ammonis, the dentate gyrus, and the subicular complex:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # CA4 is a GRANDCHILD of the hippocampus (child of the cornu
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
    # CA4 is the DENTATE HILUS; the parahippocampal region is the
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
    # CA4 is the BRAIN STRUCTURE; the ``memory/`` package is the
    # SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE CA4 is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT CA4 children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # CA4 is the dentate hilus of the MEMORY container; the central
    # nucleus and the basolateral nuclei are the FEAR structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
CA4 is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include CA4:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # CA4 is SLEA-FREE.

Cell-type-level detail (not wired — consult references)::

    # CA4's cell types are prose, not modules:
    #   mossy cells           -> principal neurons of the hilus;
    #                            project to dentate granule cells
    #                            (feedback) and to CA3
    #   hilar interneurons    -> GABAergic inhibitory local-circuit
    #                            neurons; gate mossy-fiber
    #                            throughput
    #   mossy-fiber synapses  -> dentate granule-cell axons;
    #                            synapse in the hilus *before*
    #                            projecting to CA3
    #
    # Do not attempt to resolve these as sub-paths of CA4.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ca4_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.cornu_ammonis.ca4"
        )
        # resolve ca4_path through the memory/recall layer

References
----------
*   **Original CA1–CA4 nomenclature:** Lorente de Nó, R. (1934).
    "Studies on the structure of the cerebral cortex. II.
    Continuation of the study of the ammonic system." *Journal für
    Psychologie und Neurologie* 46:113–177. (The original CA1–CA4
    parcellation; CA4 as the hilus.)
*   **Canonical CA4 / dentate hilus anatomy:** Amaral, D.G. (1978).
    "A Golgi study of cell types in the hilar region of the
    hippocampus in the rat." *Journal of Comparative Neurology*
    182:851–914. (The definitive anatomical treatment of CA4 as the
    polymorphic layer / hilus of the dentate gyrus; mossy cells;
    hilar interneurons.)
*   **Hippocampal formation anatomy (including the hilus):**
    Amaral, D.G., Witter, M.P. (1989). "The three-dimensional
    organization of the hippocampal formation: a review of
    anatomical data." *Neuroscience* 31:571–591. (Hippocampal
    formation anatomy; CA4 / hilus; mossy fibers.)
*   **Mossy-cell anatomy and connectivity:** Scharfman, H.E.
    (1991). "Dentate hilar cells with dendrites in the molecular
    layer have synaptic connections with granule cells in the rat
    hippocampus." *Journal of Neuroscience* 11:2081–2090.
    (Mossy-cell connectivity.)
*   **Mossy-cell function (feedback):** Scharfman, H.E. (2016).
    "The enigmatic mossy cell of the dentate gyrus." *Nature
    Reviews Neuroscience* 17:562–575. (Mossy-cell function —
    feedback and gating.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; CA4 / hilus.)
*   **CA4 mossy-cell loss in epilepsy:** Sloviter, R.S. (1987).
    "Decreased hippocampal inhibition and a selective loss of
    interneurons in experimental epilepsy." *Science* 235:73–76.
    (Mossy-cell and hilar interneuron loss in epilepsy.)
*   **CA4 mossy-cell loss in Ammon's horn sclerosis:** Mathern,
    G.W., Babb, T.L., Vickrey, B.G., Melendez, M., Pretorius, J.K.
    (1995). "The clinical-pathogenic mechanisms of hippocampal
    neuron loss and surgical outcomes in temporal lobe epilepsy."
    *Brain* 118:105–118. (CA4 mossy-cell loss in Ammon's horn
    sclerosis.)
*   **Mossy-cell vulnerability in traumatic brain injury:**
    Lowenstein, D.H., Thomas, M.J., Smith, D.H., McIntosh, T.K.
    (1992). "Selective vulnerability of dentate hilar neurons
    following traumatic brain injury: a potential mechanistic link
    between head trauma and disorders of the hippocampus." *Journal
    of Neuroscience* 12:4846–4853. (Mossy-cell vulnerability to
    TBI.)
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
    separation; CA3 pattern completion; hilar / mossy-cell
    contribution to the circuit.)
*   **Amygdala (contrast — CA4 is NOT the amygdala):** LeDoux, J.E.
    (2000). "Emotion circuits in the brain." *Annual Review of
    Neuroscience* 23:155–184. (Amygdala fear circuit — distinct
    from the hippocampus memory circuit.)
*   **SLEA (contrast — CA4 is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT CA4.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (CA4 / hilus in overview.)
*   NeuroNames — CA4 field (left); FMA — CA4 field (left member).
"""