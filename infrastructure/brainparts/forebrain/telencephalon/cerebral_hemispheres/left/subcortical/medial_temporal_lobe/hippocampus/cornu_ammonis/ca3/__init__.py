"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca3
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
                            └── ca3   <-- THIS MODULE

**Primary synonym:** CA3 (left); CA3 field; CA3 subfield; CA3 region;
third CA field; regio inferior.
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**leaf subfield** of the **cornu ammonis** — the
**recurrent-collateral**, **autoassociative**, **pattern-completion**
CA field that **receives** the **mossy fibers** from the dentate
gyrus and **projects** the **Schaffer collaterals** to CA1.
**Part of:** The **cornu_ammonis** container — the **CA field
system** of the hippocampus. The **CA3** is the
**pattern-completion** subfield of the cornu ammonis.
**Structural parent:** ``.../cornu_ammonis/`` → **direct child** of
the cornu ammonis container.
**Structural children:** **None.** This is a **leaf** module. The
**stratum lucidum**, **stratum oriens**, **stratum pyramidale**,
**stratum radiatum**, and **stratum lacunosum-moleculare** of CA3
are documented as **prose**, not as structural children.
**Boundary status (PATTERN-COMPLETION subfield — NOT the
principal-output subfield, NOT the social-memory subfield, and NOT
the dentate hilus):** **Boundary case — the ca3 is the
PATTERN-COMPLETION subfield of the cornu ammonis, NOT the
principal-output subfield, NOT the social-memory subfield, and NOT
the dentate hilus.** The **CA1** sibling (``.../ca1/``) is the
**principal-output** subfield (CA1 → subiculum; entorhinal cortex;
prefrontal cortex). The **CA2** sibling (``.../ca2/``) is the
**social-memory** subfield (oxytocin-receptor enriched). The
**CA4** sibling (``.../ca4/``) is the **dentate hilus** — the
**mossy-cell** layer of the dentate gyrus. **CA3 is the
recurrent-collateral, autoassociative, pattern-completion
subfield** — it is **neither** the output gate, **nor** the
social-memory subfield, **nor** the dentate hilus. Consumers must
**not** conflate CA3 with CA1, CA2, or CA4.
**Boundary status (RECURRENT-COLLATERAL AUTASSOCIATIVE NETWORK —
the defining intrinsic circuit):** **Boundary case — the ca3 is the
RECURRENT-COLLATERAL, AUTOASSOCIATIVE subfield.** The **CA3
pyramidal cells** project **back onto each other** via the
**recurrent collaterals (associational fibers)** — the
**autoassociative network** that implements **pattern
completion**. This **recurrent connectivity** is the **defining
intrinsic circuit** of CA3 — neither CA1 nor CA2 has it at
comparable density, and CA4 is a **different** structure (dentate
hilus, mossy cells). Consumers must **not** treat CA3 as "CA1 with
different inputs" or "CA2 with different inputs" — CA3's
**autoassociative recurrent network** is its **distinctive
identity**.
**Boundary status (VULNERABLE to seizures and excitotoxicity — NOT
the relatively resistant CA2 profile):** **Boundary case — the ca3
is VULNERABLE to seizures and to excitotoxic damage, NOT the
relatively resistant CA2 profile.** The **CA2** sibling is
**relatively resistant** to excitotoxic damage and is **spared**
in **hippocampal sclerosis** (Ammon's horn sclerosis). The
**CA1** sibling is the **most vulnerable** CA field to
**ischemia**, **hypoxia**, and **Alzheimer's pathology**. The
**CA3** (here) is **vulnerable** to **seizures** and to
**excitotoxic damage** — CA3 is a **principal site** of
**seizure-induced** and **excitotoxic** damage, and it is a
**principal site** of **hippocampal sclerosis** in **temporal lobe
epilepsy** (alongside CA1). Consumers must **not** assume CA3
shares the **relative resistance** of CA2 — it does **not** — and
must **not** assume CA3 shares CA1's **ischemia** profile — its
**vulnerability** is primarily **seizure/excitotoxic**.
**Boundary status (NOT the dentate gyrus — the dentate gyrus is the
INPUT subfield):** **Boundary case — the ca3 is NOT the dentate
gyrus; the dentate gyrus is the INPUT subfield.** The
**dentate_gyrus** (``.../hippocampus/dentate_gyrus/``) is the
**principal input** of the hippocampus (entorhinal cortex →
perforant path → dentate gyrus → mossy fibers → CA3) and the
**principal site** of **pattern separation** and **adult
neurogenesis**. The **CA3** (here) is the **pattern-completion**
subfield — **downstream** of the dentate gyrus (the **mossy
fibers** project from the dentate granule cells to CA3). Consumers
must **not** conflate CA3 with the dentate gyrus — the **dentate
gyrus** is the **input**; **CA3** is the **pattern-completion**
subfield.
**Boundary status (NOT the subiculum — the subiculum is the OUTPUT
TARGET of CA1):** **Boundary case — the ca3 is NOT the subiculum;
the subiculum is the OUTPUT TARGET of CA1.** The **subiculum**
(``.../hippocampus/subiculum/``) is the **principal output** of the
hippocampus to the parahippocampal region, the mammillary bodies
(via the fornix), and the prefrontal cortex — **CA1 projects to
the subiculum**. The **CA3** (here) is a **CA field** that
**projects** to **CA1** (via the **Schaffer collaterals**) and to
**CA2** — it is **not** the subiculum. Consumers must **not**
conflate CA3 with the subiculum — the **CA3** is a **CA field**;
the **subiculum** is a **sibling subfield** of the hippocampus.
**Boundary status (NOT the cornu ammonis container — CA3 is a CHILD
of the cornu ammonis):** **Boundary case — the ca3 is a CHILD of
the cornu_ammonis container, not the container itself.** The
**cornu ammonis** container contains **CA1**, **CA2**, **CA3**, and
**CA4** — the **CA3** is **one** of those four children. Consumers
must **not** conflate CA3 with the cornu ammonis container.
**Boundary status (NOT the hippocampus container — CA3 is a
grandchild of the hippocampus):** **Boundary case — the ca3 is a
GRANDCHILD of the hippocampus container.** The **hippocampus**
container contains the **cornu ammonis**, the **dentate gyrus**,
the **parasubiculum**, the **presubiculum**, and the **subiculum**
— and the **cornu ammonis** in turn contains **CA1–CA4**. The
**CA3** is a **child of the cornu ammonis**, and thus a
**grandchild** of the hippocampus. Consumers must **not** conflate
CA3 with the hippocampus container.
**Boundary status (NOT the parahippocampal region — the entorhinal,
perirhinal, and parahippocampal cortices are wired under
``cortex/temporal/gyri/``):** **Boundary case — the ca3 is NOT the
parahippocampal region.** The **parahippocampal region** (the
**entorhinal cortex**, the **perirhinal cortex**, and the
**parahippocampal gyrus**) is **cortical** — it is wired under
``.../left/cortex/temporal/gyri/`` and is **outside** the
hippocampus container. The **CA3** (here) is the **archicortex**.
Consumers must **not** conflate CA3 with the parahippocampal
region — the parahippocampal region is **cortex/**; CA3 is
**subcortical/medial_temporal_lobe/**.
**Boundary status (NOT the fornix or the white matter — those are
WHITE-MATTER structures):** **Boundary case — the ca3 is NOT the
fornix or the white matter; the fornix and the white_matter are
WHITE-MATTER structures.** The **fornix**
(``.../left/white_matter/fornix/``) is the **major output tract**
of the hippocampus — the **white-matter fibers** that carry the
hippocampal output (via the subiculum) to the mammillary bodies
and the anterior thalamic nuclei. The **white_matter** container
(``.../left/white_matter/``) is the **white-matter
infrastructure**. The **CA3** (here) is the **grey-matter
archicortex**. Consumers must **not** conflate the two — the
**CA3** is the **grey-matter subfield**; the **fornix** and the
**white_matter** are the **white-matter tracts**. Note also that
the **Schaffer collaterals** and the **mossy fibers** are
**intra-hippocampal** axonal projections — they are **not** the
**fornix** and **not** the **white_matter**.
**Boundary status (NOT the rhinencephalon — the olfactory
structures are wired under ``cortex/rhinencephalon/``):** **Boundary
case — the ca3 is NOT the rhinencephalon.** The **rhinencephalon**
(``.../left/cortex/rhinencephalon/``) — the olfactory bulb,
olfactory tract, piriform cortex, periamygdaloid cortex, anterior
olfactory nucleus, and uncus — is the **cortical olfactory lobe**.
The **CA3** (here) is the **archicortex of episodic memory and
spatial navigation** — it is **not** an olfactory structure.
Consumers must **not** conflate the two.
**Boundary status (NOT the amygdala — the amygdala is the
FEAR/EMOTION/SALIENCE container):** **Boundary case — the ca3 is
NOT the amygdala; the amygdala is the FEAR/EMOTION/SALIENCE
container.** The **amygdala**
(``.../medial_temporal_lobe/amygdala/``) is the
**fear/emotion/salience** container — its children include the
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), the **basomedial nuclei** (fear-modulatory), the
**lateral nucleus** (sensory input), and the **medial nucleus**
(olfactory/pheromone). The **CA3** (here) is a **CA field** of the
**memory** container. Consumers must **not** conflate CA3 with the
amygdala — they are **different structures** in **different
containers**.
**Boundary status (SLEA-FREE — CA3 is NOT an extended-amygdala
component):** **Boundary case — the ca3 is SLEA-FREE.** The
**SLEA overlap** belongs to the **central nucleus** (the **only
SLEA component** in the amygdala) and to the **BNST**, **ventral
pallidum**, and **nucleus accumbens** (wired elsewhere). The
**CA3** is an **episodic/declarative-memory and
spatial-navigation** structure — it is **NOT** an
extended-amygdala component, and it carries **NO SLEA warning**.
Consumers must **not** import the SLEA warning into CA3 — it is
**SLEA-free**.
**Boundary status (NOT the memory software layer — CA3 is the BRAIN
STRUCTURE, not the ``memory/`` package):** **Boundary case — the
ca3 is the BRAIN STRUCTURE, NOT the ``memory/`` software package.**
The **``memory/`` package** (``memory/stores/`` — episodic,
semantic, procedural, working; ``memory/backends/`` — chroma,
in_memory) is the **software memory layer** of the simulation. The
**CA3** (here) is the **brain structure** that **subserves**
episodic memory. Consumers must **not** conflate the two — the
**brain structure** is wired here; the **software store** is wired
under ``memory/``.
**Boundary status (NOT the fear-output or the fear-learning
structures — those are amygdala children):** **Boundary case — the
ca3 is NOT the fear-output or the fear-learning structures.** The
**central nucleus** (fear-output), the **basolateral nuclei**
(fear-learning), and the **basomedial nuclei** (fear-modulatory)
are **amygdala** children. The **CA3** is the
**pattern-completion** subfield of the **memory** container — it is
**not** a fear-output or fear-learning structure. Consumers must
**not** conflate CA3 with the **amygdala fear circuit**.
**Boundary status (NOT a single uniform layer — MULTIPLE strata,
including the CA3-SPECIFIC stratum lucidum):** **Boundary case —
the ca3 is a HETEROGENEOUS subfield with MULTIPLE strata (stratum
lucidum, stratum oriens, stratum pyramidale, stratum radiatum,
stratum lacunosum-moleculare), not a single uniform layer.** The
**strata** are functionally distinct — the **stratum lucidum** is
the **CA3-specific** layer containing the **mossy-fiber** synapses
from the dentate gyrus; the **stratum pyramidale** contains the
**CA3 pyramidal cells**; the **stratum radiatum** contains the
**recurrent collaterals** and the **Schaffer-collateral** origins;
the **stratum oriens** contains the **basal dendrites**; the
**stratum lacunosum-moleculare** receives **entorhinal** input.
The tree wires the **CA3** as a **single leaf** under the cornu
ammonis — the **strata** are **prose**, not structural children.
Consumers that need **stratum-level** resolution should consult the
references, not the tree.

Overview
--------
CA3 is the **pattern-completion** subfield of the cornu ammonis —
the **recurrent-collateral**, **autoassociative** CA field that
**receives** the **mossy fibers** from the dentate gyrus and
**projects** the **Schaffer collaterals** to CA1. It is a **leaf**
module under the cornu ammonis container, the **sibling of CA1,
CA2, and CA4**, and the **grey-matter substrate** of
**pattern completion**, **autoassociative memory**, and **place
cells**.

**CA3 is the PATTERN-COMPLETION subfield of the cornu ammonis.**
**CA1** (sibling) is the **principal-output** subfield. **CA2**
(sibling) is the **social-memory** subfield. **CA4** (sibling) is
the **dentate hilus**. **CA3 is the recurrent-collateral,
autoassociative, pattern-completion subfield.**

**CA3 is the RECURRENT-COLLATERAL, AUTOASSOCIATIVE subfield.** The
**CA3 pyramidal cells** project **back onto each other** via the
**recurrent collaterals** — the **autoassociative network** that
implements **pattern completion**. This **recurrent connectivity**
is the **defining intrinsic circuit** of CA3.

**CA3 is VULNERABLE to seizures and to excitotoxic damage, NOT the
relatively resistant CA2 profile.** CA3 is a **principal site** of
**seizure-induced** and **excitotoxic** damage, and a **principal
site** of **hippocampal sclerosis** in **temporal lobe epilepsy**
(alongside CA1). **CA2** is **relatively resistant**; **CA1** is
the **most vulnerable** to **ischemia** and **hypoxia**.

**CA3 is NOT the dentate gyrus.** The **dentate gyrus** is the
**input** subfield (the **mossy fibers** project from the dentate
granule cells to CA3). **CA3** is the **pattern-completion**
subfield — **downstream** of the dentate gyrus. **They are
DIFFERENT STRUCTURES.**

**CA3 is NOT the subiculum.** **CA1 projects to the subiculum** —
the **subiculum** is the **output target**. **CA3** is a **CA
field** that **projects** to CA1 (via the **Schaffer
collaterals**) and to CA2. They are **DIFFERENT STRUCTURES.**

**CA3 is NOT the cornu ammonis container or the hippocampus
container.** The **cornu ammonis** container contains **CA1–CA4**;
the **hippocampus** container contains the **cornu ammonis**, the
**dentate gyrus**, and the **subicular complex**.

**CA3 is NOT the parahippocampal region.** The **entorhinal
cortex**, **perirhinal cortex**, and **parahippocampal gyrus** are
**cortical** — they are wired under ``cortex/temporal/gyri/``.
**CA3** is the **archicortex**.

**CA3 is SLEA-FREE.** It is **not** an extended-amygdala component,
and it carries **no SLEA warning**. The **SLEA overlap** belongs to
the **central nucleus** (the **only SLEA component** in the
amygdala) and to the **BNST**, **ventral pallidum**, and **nucleus
accumbens** (wired elsewhere).

**CA3 is the BRAIN STRUCTURE, not the ``memory/`` software
package.** The **``memory/`` package** is the **software memory
layer**. **CA3** is the **brain region** whose function the
episodic store models. **They are DIFFERENT LAYERS.**

**CA3 is a paired structure.** Each hemisphere has its own CA3,
with **ipsilateral** and **bilateral** connections to the dentate
gyrus, CA1, CA2, the entorhinal cortex, and the contralateral CA3.
The two sides are **bilaterally symmetric** and **partially
lateralized** — the **left** CA3 is more involved in **verbal**
episodic memory, and the **right** CA3 is more involved in
**spatial/nonverbal** episodic memory. This is **well-documented**
(not contested), and documented in the **medial temporal lobe
module** (not at the CA3 level). See *Lateralization Notes*.

Stratum Composition (prose, not structural children)
----------------------------------------------------
CA3 is a **heterogeneous subfield** — documented as **prose**, not
as structural children. Unlike CA1 and CA2, CA3 has a **distinctive
stratum lucidum**:

*   **Stratum lucidum** — the **CA3-specific** layer containing the
    **mossy-fiber** synapses from the **dentate granule cells** —
    the **proximal apical dendrites** of the CA3 pyramidal cells.
    The **stratum lucidum** is **not present** in CA1 or CA2 — it
    is a **defining** feature of CA3.

*   **Stratum oriens** — the **deep** layer, containing the
    **basal dendrites** of the CA3 pyramidal cells.

*   **Stratum pyramidale** — the **principal-cell** layer,
    containing the **CA3 pyramidal cells** — the **output neurons**
    of CA3.

*   **Stratum radiatum** — the **apical-dendrite** layer,
    containing the **recurrent collaterals** (the **associational
    fibers**) and the **origins** of the **Schaffer collaterals**.

*   **Stratum lacunosum-moleculare** — the **superficial** layer,
    receiving the **perforant-path** input from the **entorhinal
    cortex** (the **direct** temporoammonic input to CA3).

**These strata are prose, not structural children.** The tree wires
**CA3** as a **single leaf** under the cornu ammonis — the
**strata** are **prose**, not structural children. Consumers that
need **stratum-level** resolution should consult the references,
not the tree.

The CA3 / CA1, CA2, CA4 Boundary
--------------------------------
This is the **sibling CA-field** boundary:

*   **CA3** (this module) — the **pattern-completion** subfield
    (recurrent collaterals; **mossy-fiber** input; **Schaffer**
    output to CA1; vulnerable to seizures and excitotoxicity).

*   **CA1** (``.../cornu_ammonis/ca1/``) — the **principal-output**
    subfield (CA1 → subiculum; entorhinal cortex; prefrontal
    cortex); the **most vulnerable** CA field to **ischemia** and
    **hypoxia**.

*   **CA2** (``.../cornu_ammonis/ca2/``) — the **social-memory**
    subfield (oxytocin-receptor enriched); **relatively resistant**
    to excitotoxic damage.

*   **CA4** (``.../cornu_ammonis/ca4/``) — the **dentate hilus**
    (mossy cells; mossy-fiber target).

**They are SIBLINGS under the cornu ammonis, and they are DIFFERENT
CA FIELDS.** Consumers must **not** conflate CA3 with CA1, CA2, or
CA4 — the **vulnerability profiles differ** (CA3 seizure/
excitotoxic; CA2 resistant; CA1 ischemia), the **functions differ**
(CA3 pattern completion; CA1 output; CA2 social memory), and the
**connectivity differs** (CA3 is the **only** CA field receiving
**mossy fibers** in the **stratum lucidum** and the **only** CA
field with the **dense recurrent-collateral** network).

The CA3 / Dentate Gyrus Boundary
--------------------------------
This is the **pattern-completion vs. pattern-separation** boundary:

*   **CA3** (this module) — the **pattern-completion** subfield
    (recurrent collaterals; autoassociative network; **receives**
    the mossy fibers from the dentate gyrus).

*   **Dentate gyrus** (``.../hippocampus/dentate_gyrus/``) — the
    **pattern-separation** subfield (the **input** subfield;
    **adult neurogenesis**; **mossy-fiber** source).

**The dentate gyrus is the INPUT, and CA3 is the downstream
pattern-completion subfield.** The **mossy fibers** project from
the **dentate granule cells** to the **CA3 stratum lucidum** —
they are **different structures**, and they perform **different
computations** (**pattern separation** in the dentate gyrus;
**pattern completion** in CA3). Consumers must **not** conflate
CA3 with the dentate gyrus.

The CA3 / Subiculum Boundary
----------------------------
This is the **CA field vs. output target** boundary:

*   **CA3** (this module) — a **CA field** (pattern-completion
    subfield).

*   **Subiculum** (``.../hippocampus/subiculum/``) — the **output
    target** of CA1 (the subiculum projects to the parahippocampal
    region, the mammillary bodies, and the prefrontal cortex).

**They are DIFFERENT STRUCTURES** — **CA3** is a **CA field** that
**projects** to CA1 (via the Schaffer collaterals); the
**subiculum** is a **sibling subfield** of the hippocampus.
Consumers must **not** conflate the two.

The CA3 / Cornu Ammonis Boundary
--------------------------------
This is the **child vs. container** boundary:

*   **CA3** (this module) — a **child** of the cornu ammonis
    container.

*   **Cornu ammonis** (``.../cornu_ammonis/``) — the **container**
    that contains **CA1**, **CA2**, **CA3**, and **CA4**.

**CA3 is ONE of the four children of the cornu ammonis.** Consumers
must **not** conflate CA3 with the cornu ammonis container.

The CA3 / Hippocampus Boundary
------------------------------
This is the **grandchild vs. container** boundary:

*   **CA3** (this module) — a **grandchild** of the hippocampus
    container.

*   **Hippocampus** (``.../hippocampus/``) — the **container** that
    contains the **cornu ammonis**, the **dentate gyrus**, the
    **parasubiculum**, the **presubiculum**, and the **subiculum**.

**CA3 is a grandchild of the hippocampus** (child of the cornu
ammonis). Consumers must **not** conflate CA3 with the hippocampus
container.

The CA3 / Parahippocampal Region Boundary
-----------------------------------------
This is the **archicortex vs. cortical interface** boundary:

*   **CA3** (this module) — the **archicortex** subfield.

*   **Parahippocampal region** — the **entorhinal cortex**, the
    **perirhinal cortex**, and the **parahippocampal gyrus** —
    wired under ``.../left/cortex/temporal/gyri/``.

**The parahippocampal region is the CORTICAL INTERFACE that feeds
the hippocampus.** **CA3** is the **archicortex** that **receives**
the parahippocampal input (directly, via the **temporoammonic**
pathway to the stratum lacunosum-moleculare; and indirectly, via
the dentate gyrus and the mossy fibers). Consumers must **not**
conflate CA3 with the parahippocampal region.

The CA3 / Fornix and White Matter Boundary
------------------------------------------
This is the **grey matter vs. white matter** boundary:

*   **CA3** (this module) — the **grey-matter** archicortex
    subfield.

*   **Fornix** (``.../left/white_matter/fornix/``) and
    **white_matter** (``.../left/white_matter/``) — the
    **white-matter tracts**.

**They are DIFFERENT STRUCTURES** — **CA3** is the **grey-matter
subfield**; the **fornix** and the **white_matter** are the
**white-matter tracts**. Note also that the **Schaffer
collaterals** and the **mossy fibers** are **intra-hippocampal**
axonal projections — they are **not** the **fornix** and **not**
the **white_matter**. Consumers must **not** conflate the two.

The CA3 / Rhinencephalon Boundary
---------------------------------
This is the **archicortex vs. olfactory lobe** boundary:

*   **CA3** (this module) — the **archicortex** subfield.

*   **Rhinencephalon** (``.../left/cortex/rhinencephalon/``) — the
    **cortical olfactory lobe** (olfactory bulb, olfactory tract,
    piriform cortex, periamygdaloid cortex, anterior olfactory
    nucleus, uncus).

**They are DIFFERENT STRUCTURES** — **CA3** is the **memory
archicortex**; the **rhinencephalon** is the **olfactory lobe**.
Consumers must **not** conflate the two.

The CA3 / Amygdala Boundary
---------------------------
This is the **memory subfield vs. emotion container** boundary:

*   **CA3** (this module) — a **CA field** of the **memory**
    container.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** container.

**They are DIFFERENT STRUCTURES** — the **amygdala** is the
**emotion** container; **CA3** is a **child of the memory**
container. Consumers must **not** conflate the two.

The CA3 / Memory Software Layer Boundary
----------------------------------------
This is the **brain structure vs. software store** boundary:

*   **CA3** (this module) — the **brain structure** (CA field) that
    subserves episodic memory.

*   **``memory/`` package** (``memory/stores/``,
    ``memory/backends/``, ``memory/system.py``,
    ``memory/forgetting.py``, ``memory/vector.py``,
    ``memory/analytics.py``) — the **software memory layer** of the
    simulation.

**They are DIFFERENT LAYERS** — **CA3** is the **brain region**;
the **``memory/`` package** is the **software store**. Consumers
must **not** conflate the two.

The CA3 / SLEA Boundary
-----------------------
This is the **SLEA** boundary — **NOT applicable**:

*   **CA3** (this module) — **SLEA-FREE**. No extended-amygdala
    relationship, no SLEA warning.

*   **SLEA continuum** — the **central nucleus** (the **only SLEA
    component** in the amygdala) + the **BNST**, **ventral
    pallidum**, and **nucleus accumbens** (wired elsewhere).

**CA3 is NOT part of the SLEA continuum.** It is an
**episodic/declarative-memory and spatial-navigation** structure,
and it carries **no SLEA warning**. Consumers must **not** import
the SLEA warning into CA3.

Function in the Human Brain
---------------------------
CA3's functions are **pattern completion**, **autoassociative
memory**, and **place-cell spatial coding** — **NOT
episodic-memory output and NOT fear-output**:

*   **Pattern Completion (Autoassociative Recurrent Network):**
    **CA3** is the **principal site** of **pattern completion** —
    the **reconstruction** of a **full memory** from a **partial
    cue**, implemented by the **recurrent-collateral**
    autoassociative network. This is the **substrate** of the
    **recall** of a full episode from a partial reminder — the
    **pattern-completion** computation.

*   **Autoassociative Memory (Recurrent Collaterals):** The
    **recurrent collaterals** of CA3 implement an **autoassociative
    memory** — the **network** can **retrieve** a **stored
    pattern** from a **noisy** or **partial** input. This is the
    **network-level** substrate of **pattern completion**.

*   **Mossy-Fiber Input (Dentate Gyrus → CA3):** **CA3** receives
    the **mossy fibers** from the **dentate granule cells** in the
    **stratum lucidum** — the **sparse, powerful** input that
    **drives** the pattern-completion computation. This is the
    **input** side of the CA3 computation.

*   **Schaffer-Collateral Output (CA3 → CA1):** **CA3** projects
    the **Schaffer collaterals** to **CA1** — the **output** side
    of the CA3 computation. This is the **principal** pathway
    from CA3 to CA1.

*   **Place-Cell Spatial Coding (CA3):** **CA3** is a **principal
    site** of **place cells** — the **spatial** neurons that fire
    when the animal is in a **specific location** in the
    environment. This is the **substrate** of the **cognitive
    map**.

*   **Theta Rhythm (CA3 Oscillations):** **CA3** is a **principal
    generator** of the **hippocampal theta rhythm** — the
    **network oscillation** that coordinates the **encoding** and
    **retrieval** of episodic memory. This is the **temporal**
    substrate of the CA3 computation.

*   **NOT a neural processor in the classical sense.** **CA3** is a
    **memory and navigation** subfield — it **completes** and
    **outputs** the **episodic and spatial** representations, but
    it does **not** produce the **fear-output** or the **autonomic
    and behavioral** fear responses. The **fear-output** is the
    **central nucleus**; the **fear-learning** structures are the
    **basolateral nuclei**.

**The unifying theme:** CA3 is the **pattern-completion subfield**
of the **cornu ammonis** — the **recurrent-collateral,
autoassociative** CA field that anchors **pattern completion,
autoassociative memory, and place cells**. It is **SLEA-free**,
**memory/navigation**, and **NOT the fear-output structure** — the
**fear-output** is the **central nucleus**, the **fear-learning**
structures are the **basolateral nuclei**, and **CA3** is the
**pattern-completion subfield** of the **memory** container.

Associated Disorders
--------------------
CA3 has **no named "CA3 syndrome"** in the narrow sense, but its
clinical associations are **well-documented**:

*   **Temporal Lobe Epilepsy (Hippocampal Sclerosis / Ammon's Horn
    Sclerosis):** **CA3** is one of the **principal sites** of
    **hippocampal sclerosis** (Ammon's horn sclerosis) in
    **temporal lobe epilepsy** — **CA3** is **vulnerable** to
    **seizure-induced** and **excitotoxic** damage, and it is
    **destroyed** alongside **CA1** in the **classic** Ammon's
    horn sclerosis. **CA3** is the **epileptogenic substrate** of
    temporal lobe epilepsy.

*   **Seizure-Induced and Excitotoxic Damage (CA3 Vulnerability):**
    **CA3** is **vulnerable** to **seizure-induced** and
    **excitotoxic** damage — the **recurrent-collateral** network
    **amplifies** the **excitotoxic** cascade. **CA3** is the
    **substrate** of the **seizure-induced** memory loss.

*   **Pattern-Completion Deficits (Partial-Cue Recall Failure):**
    **CA3** dysfunction produces **pattern-completion deficits** —
    the **inability** to **recall** a full episode from a
    **partial cue**, even when the **full episode** was
    **encoded**. **CA3** is the **memory substrate** of this
    deficit.

*   **Schizophrenia (CA3 Dysfunction — Contested):** **CA3** shows
    **atypical** findings in **schizophrenia** — **reduced CA3
    pyramidal-cell** markers and **atypical CA3** oscillatory
    activity are reported. This is **contested** — the findings
    are **not** uniformly replicated.

*   **Alzheimer's Disease (CA3 Less Early than CA1):** **CA3**
    shows **pathology** in **Alzheimer's disease**, but it is
    **less early** than **CA1** and the **entorhinal cortex** —
    **CA1** is the **earliest** affected **CA field**, and **CA3**
    is affected **later** in the disease course.

*   **No Named "CA3 Syndrome":** **CA3** is a **CA field**, not a
    **single functional system** — it has **no named clinical
    syndrome**. Its clinical relevance is **direct** for
    **temporal lobe epilepsy**, **seizure-induced memory loss**,
    and **pattern-completion deficits**, and **contested** for
    **schizophrenia**.

**What is NOT here:** **CA3** is **not** the substrate for
**Kluver-Bucy syndrome** (amygdala — basolateral nuclei + central
nucleus), **Urbach-Wiethe disease** (amygdala — basolateral
nuclei), **fear conditioning** (central nucleus + basolateral
nuclei), or **fear extinction** (ventromedial prefrontal cortex +
basomedial nuclei). Its clinical relevance is **direct** for
**temporal lobe epilepsy**, **seizure-induced memory loss**, and
**pattern-completion deficits**.

Lateralization Notes
--------------------
This is the **left** CA3 module. **CA3** is **bilaterally
symmetric** and **partially lateralized** — and it carries **NO
warning**:

*   **Bilateral CA3 Function:** Each hemisphere has its own CA3,
    with **ipsilateral** and **bilateral** connections to the
    dentate gyrus, CA1, CA2, the entorhinal cortex, and the
    contralateral CA3. The two sides are **functionally symmetric**
    for **basic memory and navigation**.

*   **Partial Lateralization (Well-Documented — Verbal vs.
    Spatial):** The **left** CA3 is **more involved in verbal**
    episodic memory (word lists, stories, verbal recognition); the
    **right** CA3 is **more involved in spatial/nonverbal**
    episodic memory (spatial layouts, faces, nonverbal
    recognition). This is **well-documented**, **not contested**,
    and is documented in the **medial temporal lobe module** (not
    at the CA3 level).

*   **NO Extended-Amygdala Warning (SLEA-free leaf):** **CA3** is
    **SLEA-free** — it is **not** an extended-amygdala component.
    Consumers must **not** import the SLEA warning into CA3.

*   **NO Amygdala-Lateralization Warning of their own (CA3 is the
    PATTERN-COMPLETION subfield, not the fear-output):** The
    **right-amygdala fear association** belongs to the **amygdala
    module** — specifically the **central nucleus** (fear-output)
    and the **basolateral nuclei** (fear-learning). **CA3** is a
    **pattern-completion subfield** — consumers must **not**
    conflate it with the **whole amygdala** or with the **central
    nucleus**. **CA3** is the **pattern-completion** subfield, not
    the **fear circuit**.

**A consumer that assumes "left CA3 = right CA3" will be
structurally correct** — the two sides are **symmetric** and
**partially lateralized** (the lateralization is documented in the
medial temporal lobe module). **CA3** is a **strict-mirror pair
with NO warning** — **no SLEA warning**, **no
amygdala-lateralization warning of their own**, and **no
rhinencephalon-exclusion flag**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../cornu_ammonis/ca1/``, ``.../cornu_ammonis/ca2/``,
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
    container. **CA3**'s relationships to CA1, CA2, CA4, the
    dentate gyrus, the subiculum, the parasubiculum, the
    presubiculum, the amygdala, the parahippocampal region, the
    fornix, the rhinencephalon, and the ``memory/`` package are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **LEAF module — no structural children.** The **stratum
    lucidum**, **stratum oriens**, **stratum pyramidale**,
    **stratum radiatum**, and **stratum lacunosum-moleculare** of
    CA3 are documented as **prose**, not as sub-modules. Consumers
    must not assume any exist as children; resolve stratum-level
    detail through the references.
*   **PATTERN-COMPLETION subfield — NOT the principal-output
    subfield, NOT the social-memory subfield, and NOT the dentate
    hilus.** **CA3** is the **pattern-completion** subfield
    (recurrent collaterals; mossy-fiber input; Schaffer-collateral
    output). **CA1** (sibling) is the **principal-output**
    subfield. **CA2** (sibling) is the **social-memory** subfield.
    **CA4** (sibling) is the **dentate hilus**. Consumers must
    **not** conflate CA3 with any of its sibling CA fields.
*   **RECURRENT-COLLATERAL AUTASSOCIATIVE NETWORK — the defining
    intrinsic circuit.** The **recurrent collaterals** are the
    **defining intrinsic circuit** of CA3 — consumers must **not**
    treat CA3 as "CA1 with different inputs" or "CA2 with
    different inputs."
*   **VULNERABLE to seizures and excitotoxicity — NOT the
    relatively resistant CA2 profile.** **CA2** is **relatively
    resistant** and **spared** in **hippocampal sclerosis**;
    **CA3** is **vulnerable** to **seizure-induced** and
    **excitotoxic** damage. Consumers must **not** assume CA3
    shares the **relative resistance** of CA2.
*   **NOT the dentate gyrus — the dentate gyrus is the INPUT
    subfield.** The **mossy fibers** project from the **dentate
    granule cells** to **CA3** — they are **different
    structures**, and they perform **different computations**
    (pattern separation in the dentate gyrus; pattern completion
    in CA3). Consumers must **not** conflate CA3 with the dentate
    gyrus.
*   **NOT the subiculum — the subiculum is the OUTPUT TARGET of
    CA1.** Consumers must **not** conflate CA3 with the subiculum.
*   **NOT the cornu ammonis container — CA3 is a CHILD of the
    cornu ammonis.**
*   **NOT the hippocampus container — CA3 is a GRANDCHILD of the
    hippocampus.**
*   **NOT the parahippocampal region.** The **entorhinal cortex**,
    **perirhinal cortex**, and **parahippocampal gyrus** are
    **cortex/** structures; **CA3** is the **archicortex**.
*   **NOT the fornix or the white matter — those are WHITE-MATTER
    structures.** **CA3** is the **grey-matter CA field**; the
    **Schaffer collaterals** and the **mossy fibers** are
    **intra-hippocampal** projections — not the fornix and not the
    white_matter.
*   **NOT the rhinencephalon.** **CA3** is **not** an olfactory
    structure.
*   **NOT the amygdala — the amygdala is the FEAR/EMOTION/SALIENCE
    container.**
*   **SLEA-FREE — no extended-amygdala relationship.** **CA3** is
    **not** an extended-amygdala component, and it carries **no
    SLEA warning**.
*   **NOT the fear-output or the fear-learning structures.** The
    **central nucleus** (fear-output) and the **basolateral nuclei**
    (fear-learning) are **amygdala** children; **CA3** is the
    **pattern-completion** subfield of the **memory** container.
*   **NOT the ``memory/`` software layer.** The **``memory/``
    package** is the **software store**; **CA3** is the **brain
    structure**. Consumers must **not** conflate the two.
*   **NOT a single uniform layer — MULTIPLE strata, including the
    CA3-SPECIFIC stratum lucidum.** The **stratum lucidum** is
    **not present** in CA1 or CA2 — it is a **defining** feature of
    CA3.
*   **No ``AREA_PATHS`` hop.** **CA3** is a local leaf under the
    cornu ammonis, not a cross-listed leaf.
*   **No nested cross-listing.** **CA3** has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with right CA3 — strict mirror with NO
    warning.** Left and right CA3 modules are **structurally
    identical** — same **leaf** status, same
    **pattern-completion** framing, same **SLEA-free** status, same
    **no warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis import ca3

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "medial_temporal_lobe.hippocampus.cornu_ammonis.ca3"
    )

**Do not** assume CA3 is the **principal-output** subfield. That is
**CA1** — CA3 is the **pattern-completion** subfield.

**Do not** assume CA3 is the **social-memory** subfield. That is
**CA2** — CA3 is the **pattern-completion** subfield.

**Do not** assume CA3 is the **dentate hilus**. That is **CA4** —
CA3 is the **pattern-completion** subfield.

**Do not** assume CA3 is "CA1 with different inputs" or "CA2 with
different inputs." CA3's **recurrent-collateral autoassociative
network** is its **distinctive identity** — it is **not** a
variant of CA1 or CA2.

**Do not** assume CA3 shares the **relative resistance** of CA2.
CA3 is **vulnerable** to **seizures** and **excitotoxicity** —
CA2 is **relatively resistant**.

**Do not** assume CA3 is the **dentate gyrus**. The **dentate
gyrus** is the **input** (pattern separation); **CA3** is the
**pattern-completion** subfield.

**Do not** assume CA3 is the **subiculum**. The **subiculum** is the
**output target** of CA1; **CA3** is a **CA field**.

**Do not** assume CA3 is the **cornu ammonis container** or the
**hippocampus container**. **CA3** is a **child of the cornu
ammonis** and a **grandchild of the hippocampus**.

**Do not** assume CA3 is the **parahippocampal region**. The
**entorhinal cortex**, **perirhinal cortex**, and
**parahippocampal gyrus** are **cortex/** structures; **CA3** is
the **archicortex**.

**Do not** assume CA3 is the **fornix** or the **white_matter**.
Those are **white-matter tracts**; **CA3** is the **grey-matter CA
field**; the **Schaffer collaterals** and the **mossy fibers** are
**intra-hippocampal** projections.

**Do not** assume CA3 is the **rhinencephalon**. The
**rhinencephalon** is the **cortical olfactory lobe**; **CA3** is
the **memory archicortex**.

**Do not** assume CA3 is the **``memory/`` software package**. The
**``memory/`` package** is the **software store**; **CA3** is the
**brain structure**.

**Do not** import the **SLEA warning** or the
**amygdala-lateralization warning** into CA3. **CA3 is SLEA-FREE**
— it is **not** an extended-amygdala component, and it is **NOT
the fear-output structure**.

Iterating CA3's (empty) children (recommended consumer pattern)::

    CA3_CHILDREN = ()
    # CA3 is a leaf. The stratum lucidum, stratum oriens, stratum
    # pyramidale, stratum radiatum, and stratum lacunosum-moleculare
    # are prose, not modules.

Reaching the CA1, CA2, CA4 siblings (recommended consumer pattern —
the sibling CA fields)::

    # CA1, CA2, and CA4 are the SIBLING CA fields under the cornu
    # ammonis:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca1
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca2
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca4
    #
    # CA3 is the PATTERN-COMPLETION subfield; CA1 is the PRINCIPAL
    # OUTPUT; CA2 is the SOCIAL-MEMORY subfield; CA4 is the DENTATE
    # HILUS.

Reaching the dentate gyrus (recommended consumer pattern — the
input / pattern-separation subfield)::

    # The dentate gyrus is the INPUT (pattern-separation) subfield —
    # the sibling of the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.dentate_gyrus
    #
    # The dentate gyrus is the INPUT (pattern separation); CA3 is
    # the downstream PATTERN-COMPLETION subfield. The mossy fibers
    # project from the dentate granule cells to the CA3 stratum
    # lucidum.

Reaching the subiculum (recommended consumer pattern — the output
target of CA1)::

    # The subiculum is the OUTPUT TARGET of CA1 — the sibling of
    # the cornu ammonis under the hippocampus:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.subiculum
    #
    # CA1 projects to the subiculum; CA3 is a CA field that projects
    # to CA1 (via the Schaffer collaterals) and to CA2.

Reaching the cornu ammonis (recommended consumer pattern — the
container)::

    # The cornu ammonis is the CONTAINER that contains CA1, CA2,
    # CA3, and CA4:
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis
    #
    # CA3 is ONE of the four children of the cornu ammonis.

Reaching the hippocampus (recommended consumer pattern — the
container)::

    # The hippocampus is the CONTAINER that contains the cornu
    # ammonis, the dentate gyrus, and the subicular complex:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # CA3 is a GRANDCHILD of the hippocampus (child of the cornu
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
    # CA3 is the ARCHICORTEX; the parahippocampal region is the
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
    # CA3 is the BRAIN STRUCTURE; the ``memory/`` package is the
    # SOFTWARE STORE.

Reaching the amygdala fear-output (recommended consumer pattern —
NOTE CA3 is NOT the fear-output)::

    # The central nucleus is the FEAR-OUTPUT structure; the
    # basolateral nuclei are the FEAR-LEARNING structures. They are
    # AMYGDALA children, NOT CA3 children:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.basolateral_nuclei
    #
    # CA3 is the pattern-completion CA field of the MEMORY
    # container; the central nucleus and the basolateral nuclei are
    # the FEAR structures.

Reaching the SLEA components (recommended consumer pattern — NOTE
CA3 is NOT included)::

    # The SLEA continuum includes the central nucleus (in the
    # amygdala) and the BNST, ventral pallidum, and nucleus
    # accumbens (wired elsewhere). It does NOT include CA3:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # CA3 is SLEA-FREE.

Stratum-level detail (not wired — consult references)::

    # CA3's strata are prose, not modules:
    #   stratum lucidum              -> mossy fibers (from dentate
    #                                    gyrus); CA3-specific
    #   stratum oriens               -> basal dendrites
    #   stratum pyramidale           -> CA3 pyramidal cells
    #   stratum radiatum             -> recurrent collaterals;
    #                                    Schaffer-collateral origins
    #   stratum lacunosum-moleculare -> perforant path (from
    #                                    entorhinal cortex)
    #
    # Do not attempt to resolve these as sub-paths of CA3.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ca3_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe.hippocampus.cornu_ammonis.ca3"
        )
        # resolve ca3_path through the memory/recall layer

References
----------
*   **Original CA1–CA4 nomenclature:** Lorente de Nó, R. (1934).
    "Studies on the structure of the cerebral cortex. II.
    Continuation of the study of the ammonic system." *Journal für
    Psychologie und Neurologie* 46:113–177. (The original CA1–CA4
    parcellation of the cornu ammonis; CA3 as a distinct field.)
*   **Canonical CA3 anatomy:** Amaral, D.G., Witter, M.P. (1989).
    "The three-dimensional organization of the hippocampal
    formation: a review of anatomical data." *Neuroscience*
    31:571–591. (Definitive CA3 anatomy; strata, including the
    stratum lucidum; mossy fibers; Schaffer collaterals.)
*   **CA3 anatomy (mossy fibers and Schaffer collaterals):**
    Amaral, D.G., Dent, J.A. (1981). "Development of the mossy
    fibers of the dentate gyrus: I. A light and electron
    microscopic study of the mossy fibers and their expansions."
    *Journal of Comparative Neurology* 195:51–86. (Mossy-fiber
    anatomy.)
*   **CA3 autoassociative network and pattern completion:** Marr,
    D. (1971). "Simple memory: a theory for archicortex."
    *Philosophical Transactions of the Royal Society of London B*
    262:23–81. (The theoretical autoassociative CA3 network.)
*   **CA3 pattern completion (experimental):** Nakazawa, K., et
    al. (2002). "Requirement for hippocampal CA3 NMDA receptors in
    associative memory recall." *Science* 297:211–218. (CA3 NMDA
    receptors and pattern completion.)
*   **CA3 place cells:** O'Keefe, J., Dostrovsky, J. (1971). "The
    hippocampus as a spatial map: preliminary evidence from unit
    activity in the freely-moving rat." *Brain Research* 34:171–175.
    (Place cells in the CA3 field.)
*   **Hippocampal formation in the human:** Duvernoy, H.M. (2005).
    *The Human Hippocampus: Functional Anatomy, Vascularization and
    Serial Sections with MRI*, 3rd ed. Springer, Berlin. (Human
    hippocampal anatomy; CA3 subfield; stratum lucidum.)
*   **CA3 and temporal lobe epilepsy:** Mathern, G.W., Babb, T.L.,
    Vickrey, B.G., Melendez, M., Pretorius, J.K. (1995). "The
    clinical-pathogenic mechanisms of hippocampal neuron loss and
    surgical outcomes in temporal lobe epilepsy." *Brain*
    118:105–118. (CA3 vulnerability in Ammon's horn sclerosis.)
*   **CA3 excitotoxicity:** Sloviter, R.S. (1994). "The functional
    organization of the hippocampal dentate gyrus and its relevance
    to the pathogenesis of temporal lobe epilepsy." *Annals of
    Neurology* 35:640–654. (CA3 recurrent collaterals;
    excitotoxicity; seizure-induced damage.)
*   **CA3 and schizophrenia (contested):** Benes, F.M., Kwok, E.W.,
    Vincent, S.L., Todtenkopf, M.S. (1998). "A reduction of
    nonpyramidal cells in sector CA2 of schizophrenics and manic
    depressives." *Biological Psychiatry* 44:88–97. (CA3/CA2
    pathology in schizophrenia — contested.)
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
*   **Amygdala (contrast — CA3 is NOT the amygdala):** LeDoux, J.E.
    (2000). "Emotion circuits in the brain." *Annual Review of
    Neuroscience* 23:155–184. (Amygdala fear circuit — distinct
    from the hippocampus memory circuit.)
*   **SLEA (contrast — CA3 is not included):** Alheid, G.F., Heimer,
    L. (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders."
    *Neuroscience* 27:1–39. (SLEA continuum — BNST, central nucleus,
    ventral pallidum, nucleus accumbens; NOT CA3.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (CA3 in overview.)
*   NeuroNames — CA3 field (left); FMA — CA3 field (left member).
"""