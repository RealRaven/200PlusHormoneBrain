"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.medial_temporal_lobe
===========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── medial_temporal_lobe   <-- THIS MODULE
                    ├── amygdala
                    │   ├── accessory_olfactory_system
                    │   ├── amygdala_cortex_pathways
                    │   ├── autonomic_nervous_system
                    │   ├── basolateral_nuclei
                    │   ├── basomedial_nuclei
                    │   ├── central_nucleus
                    │   ├── frontotemporal_cortical_system
                    │   ├── lateral_nucleus
                    │   ├── main_olfactory_system
                    │   └── medial_nucleus
                    └── hippocampus
                        ├── cornu_ammonis
                        │   ├── ca1
                        │   ├── ca2
                        │   ├── ca3
                        │   └── ca4
                        ├── dentate_gyrus
                        ├── parasubiculum
                        ├── presubiculum
                        └── subiculum

**Primary synonym:** Medial temporal lobe (MTL); medial temporal
region; "the medial temporal lobe."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container node** — the parent of two medial temporal lobe children
(``amygdala``, ``hippocampus``) and **fifteen** grandchildren and
great-grandchildren.
**Part of:** The **subcortical** container — a **sibling** of
``basal_forebrain``, ``basal_ganglia``, ``claustrum``, and
``extended_amygdala``.
**Structural parent:** ``.../right/subcortical/`` → **direct child** of
the subcortical container.
**Structural children (two, closed set):**
``amygdala`` (→ 10 children including ``central_nucleus``,
``basolateral_nuclei``, etc.) and ``hippocampus`` (→
``cornu_ammonis`` → ``ca1``/``ca2``/``ca3``/``ca4``; ``dentate_gyrus``,
``parasubiculum``, ``presubiculum``, ``subiculum``).
**Boundary status (DEEPEST container — FIVE levels deep, the
deepest in the entire tree):** **Boundary case — the medial
temporal lobe is a FIVE-LEVEL container, the deepest in the entire
tree.** The **deepest branch** is
``medial_temporal_lobe/hippocampus/cornu_ammonis/ca1/`` — **five
levels** from the subcortical container. **No other container in the
tree reaches this depth.** Consumers iterating the medial temporal
lobe must be prepared to **recurse to five levels** — the
**hippocampus's CA1-CA4 subfields** are the **deepest leaves** in
the entire subcortical tree.
**Boundary status (CONTAINS BOTH REMAINING RHINENCEPHALON-EXCLUDED
STRUCTURES — amygdala and hippocampus):** **Boundary case — the
medial temporal lobe contains BOTH of the remaining rhinencephalon-
excluded structures: the AMYGDALA and the HIPPOCAMPUS.** These are
**two of the five** rhinencephalon-excluded structures:
*   **Amygdala** — ``medial_temporal_lobe/amygdala/`` (here)
*   **Hippocampus** — ``medial_temporal_lobe/hippocampus/`` (here)
*   **Septal nuclei** —
    ``basal_forebrain/septal_nuclei/`` (documented)
*   **Anterior perforated substance** —
    ``basal_forebrain/anterior_perforated_substance/`` (documented)
*   **Olfactory tubercle** —
    ``basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/``
    (documented)
**The medial temporal lobe is the LAST container to hold
rhinencephalon-excluded structures** — after the medial temporal
lobe's **amygdala** and **hippocampus** leaves are written, **all
five** rhinencephalon-excluded structures will be **fully
documented at the leaf level**. **Consumers reconstructing the
classical full rhinencephalon** must **union** the rhinencephalon
with **all five** excluded structures — **two of which are here**.
**Boundary status (CONTAINS THE ONLY REMAINING SLEA COMPONENT —
central amygdaloid nucleus):** **Boundary case — the medial temporal
lobe contains the ONLY remaining SLEA component: the CENTRAL
AMYGDLOID NUCLEUS** (under the **amygdala**). The **SLEA continuum**
is **four structures across three containers**:
*   **BNST** — ``extended_amygdala/stria_terminalis/bed_nucleus_of_stria_terminalis/``
    (documented)
*   **Central amygdaloid nucleus** —
    ``medial_temporal_lobe/amygdala/central_nucleus/`` (**here** —
    the **only remaining SLEA component**)
*   **Ventral pallidum** —
    ``basal_ganglia/globus_pallidus/ventral_pallidum/`` (documented)
*   **Nucleus accumbens** —
    ``basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/``
    (documented)
**The medial temporal lobe is the LAST container to hold a SLEA
component** — after the **central amygdaloid nucleus** leaf is
written, the **full SLEA story** will be **fully documented on both
sides at every level**. **Consumers reconstructing the FULL SLEA**
must **union** all four — the tree does **not** provide the union as
a single path.
**Boundary status (EMPHATIC amygdala-lateralization warning —
matching the subcortical container):** **Boundary case — the medial
temporal lobe carries an EMPHATIC amygdala-lateralization warning,
matching the `subcortical` container itself.** The **amygdala** is a
**DIRECT CHILD** of the medial temporal lobe — and the **amygdala**
is the **fear-output** structure (central nucleus) and the
**fear-learning** structure (basolateral nuclei). **The warning is
EMPHATIC at this container level** — **NOT deferred** (as at the
`striatum` and `basal_ganglia` containers) and **NOT light** (as at
the `extended_amygdala`, `globus_pallidus`, and `ventral_striatum`
containers). The **warning is**:
- The **right amygdala's fear association** belongs to the
  **amygdala module** (central nucleus) — **not** to the **medial
  temporal lobe container**.
- The **amygdala** is a **direct child** of the medial temporal
  lobe — a consumer reading this container is **exactly** the
  consumer most likely to attribute the right-amygdala fear
  association to the whole medial temporal lobe.
- **Do not** conflate the **medial temporal lobe** with the
  **amygdala** — the medial temporal lobe contains the **amygdala**
  AND the **hippocampus** (memory) AND their subnuclei.
**Consumers must not import amygdala-lateralization claims into the
medial temporal lobe container** — the **container is not the
amygdala**, and the **right-amygdala fear association** belongs to
the **amygdala module** (central nucleus). See *Lateralization
Notes*. **This is the FIRST container in the tree with an EMPHATIC
warning, matching the `subcortical` container** — because the
**amygdala** (the fear-output structure) is a **direct child**.
**The right-side module carries the emphatic warning explicitly** —
a dedicated "Do not import" Usage block, an emphatic Lateralization
note, and a contrast reference — because the **right medial temporal
lobe** contains the **right amygdala** (the fear-output structure)
as a **direct child**.
**Boundary status (NOT the parahippocampal gyrus — under the
temporal cortex, not the medial temporal lobe):** **Boundary case —
the parahippocampal gyrus is NOT under the medial temporal lobe — it
is under the temporal cortex.** The **parahippocampal gyrus** is
under ``cortex/temporal/gyri/parahippocampal_gyrus/`` — it is a
**neocortical** structure (six-layered), and it is **not** wired
under the medial temporal lobe. The **medial temporal lobe** contains
the **amygdala** and **hippocampus** — **allocortical and nuclear
structures** — not the **parahippocampal gyrus** (neocortical).
Consumers must **not** resolve the parahippocampal gyrus through the
medial temporal lobe — it is under the **temporal cortex**.
**Boundary status (NOT the entorhinal or perirhinal cortex — under
the temporal cortex):** **Boundary case — the entorhinal and
perirhinal cortex are NOT under the medial temporal lobe — they are
under the temporal cortex.** The **entorhinal cortex** is under
``cortex/temporal/gyri/entorhinal_cortex/``; the **perirhinal
cortex** is under ``cortex/temporal/gyri/perirhinal_cortex/`` — both
**neocortical** (or transitional) structures under the **temporal
cortex**, not the medial temporal lobe. The **medial temporal lobe**
contains the **amygdala** and **hippocampus** — the **allocortical
and nuclear structures**. Consumers must **not** conflate the
medial temporal lobe with the **parahippocampal region** (which
includes the parahippocampal gyrus, entorhinal cortex, and
perirhinal cortex — all under the temporal cortex).
**Boundary status (NOT the amygdala — the amygdala is a CHILD, not
the container):** **Boundary case — the amygdala is a CHILD of the
medial temporal lobe, not the container itself.** The **medial
temporal lobe** is the **container**; the **amygdala** is a **child**
(``medial_temporal_lobe/amygdala/``). The **amygdala** contains the
**fear-output** structure (central nucleus), the **fear-learning**
structure (basolateral nuclei), the **olfactory-amygdala** structures
(medial nucleus, cortical nuclei), and the **SLEA component** (central
nucleus). Consumers must **not** conflate the **medial temporal
lobe** (the container) with the **amygdala** (a child) — the
container contains **two** children (amygdala and hippocampus).
**Boundary status (NOT the hippocampus — the hippocampus is a
CHILD, not the container):** **Boundary case — the hippocampus is a
CHILD of the medial temporal lobe, not the container itself.** The
**medial temporal lobe** is the **container**; the **hippocampus**
is a **child** (``medial_temporal_lobe/hippocampus/``). The
**hippocampus** contains the **memory** structures (CA1-CA4, dentate
gyrus, subiculum, presubiculum, parasubiculum). Consumers must
**not** conflate the **medial temporal lobe** (the container) with
the **hippocampus** (a child) — the container contains **two**
children (amygdala and hippocampus).
**Boundary status (NOT a single functional system — FEAR vs.
MEMORY split):** **Boundary case — the medial temporal lobe is a
structural grouping of TWO FUNCTIONALLY DISTINCT subsystems, not a
single functional system.** The **two children** have **different
functions**:
*   **``amygdala``** — **fear, emotion, and salience**: fear
    conditioning (central nucleus + basolateral nuclei), emotional
    memory modulation (basolateral nuclei → hippocampus), olfactory-
    amygdala processing (medial nucleus, cortical nuclei), and the
    **SLEA fear-anxiety continuum** (central nucleus + BNST).
*   **``hippocampus``** — **memory and spatial navigation**:
    episodic memory (CA1, subiculum), spatial navigation (place cells
    in CA1/CA3), pattern separation (dentate gyrus), and **memory
    consolidation** (hippocampus → cortex).
**The medial temporal lobe is the "fear + memory" container** — the
**amygdala** is the **fear** half, and the **hippocampus** is the
**memory** half. Consumers must **not** treat the medial temporal
lobe as a single functional system — it is a **structural grouping**
of **two functionally distinct** subsystems (fear vs. memory).

Overview
--------
The medial temporal lobe is the **final major subtree** of the
subcortical container — the **deepest** (five levels), the **most
clinically documented** (memory, fear, emotion, epilepsy), and the
**only container that holds both of the remaining rhinencephalon-
excluded structures** (amygdala, hippocampus) **and** the **only
remaining SLEA component** (the central amygdaloid nucleus, under the
amygdala). It contains **two children**:

*   **``amygdala``** — the **fear/emotion/salience** subsystem.
    Contains **10 children** (accessory olfactory system,
    amygdala-cortex pathways, autonomic nervous system, basolateral
    nuclei, basomedial nuclei, central nucleus, frontotemporal
    cortical system, lateral nucleus, main olfactory system, medial
    nucleus). The **central nucleus** is the **fear-output**
    structure and the **only remaining SLEA component**.

*   **``hippocampus``** — the **memory/spatial navigation**
    subsystem. Contains **6 children** (cornu ammonis → CA1-CA4,
    dentate gyrus, parasubiculum, presubiculum, subiculum). The
    **CA1-CA4 subfields** are the **deepest leaves** in the entire
    subcortical tree (five levels).

**The medial temporal lobe is the "fear + memory" container.** The
**amygdala** is the **fear** half — the **fear-output** structure
(central nucleus), the **fear-learning** structure (basolateral
nuclei), and the **SLEA component** (central nucleus). The
**hippocampus** is the **memory** half — the **episodic memory**
structure (CA1, subiculum), the **spatial navigation** structure
(place cells in CA1/CA3), the **pattern separation** structure
(dentate gyrus), and the **memory consolidation** structure
(hippocampus → cortex). **The two are functionally distinct** —
consumers must **not** treat the medial temporal lobe as a single
functional system.

**The medial temporal lobe is the LAST container to hold a
rhinencephalon-excluded structure.** Both the **amygdala** and the
**hippocampus** are rhinencephalon-excluded structures. After the
**amygdala** and **hippocampus** leaves are written, **all five**
rhinencephalon-excluded structures will be **fully documented at the
leaf level**.

**The medial temporal lobe is the LAST container to hold a SLEA
component.** The **central amygdaloid nucleus** (under the amygdala)
is the **only remaining SLEA component**. After the **central
nucleus** leaf is written, the **full SLEA story** will be **fully
documented on both sides at every level**.

**The medial temporal lobe carries an EMPHATIC amygdala-
lateralization warning** — matching the **subcortical container**
itself. The **amygdala** is a **direct child** of the medial temporal
lobe, and the **amygdala** is the **fear-output** structure.
**Consumers must not import amygdala-lateralization claims into the
medial temporal lobe container** — the **container is not the
amygdala**, and the **right-amygdala fear association** belongs to
the **amygdala module** (central nucleus). **This is the FIRST
container in the tree with an EMPHATIC warning, matching the
`subcortical` container** — and **the right-side module carries it
with extra emphasis**, because the **right medial temporal lobe**
contains the **right amygdala** as a **direct child**.

**The medial temporal lobe is a paired structure.** Each hemisphere
has its own medial temporal lobe, with **ipsilateral** cortical,
thalamic, and brainstem connections. The two sides are **bilaterally
symmetric** and **largely non-lateralized** — though the **amygdala**
and **hippocampus** have **partial lateralization** (documented in
their own modules, not at the container level). See *Lateralization
Notes*.

Container Contents (two children, closed set)
----------------------------------------------
The medial temporal lobe container has **exactly two children**:

*   **``amygdala``** — the **fear/emotion/salience** subsystem. **10
    children** (accessory olfactory system, amygdala-cortex
    pathways, autonomic nervous system, basolateral nuclei,
    basomedial nuclei, central nucleus, frontotemporal cortical
    system, lateral nucleus, main olfactory system, medial nucleus).
    **Depth: up to three levels** (the amygdala's children are
    leaves). The **central nucleus** is the **fear-output**
    structure and the **only remaining SLEA component**.

*   **``hippocampus``** — the **memory/spatial navigation**
    subsystem. **6 children** (cornu ammonis → CA1/CA2/CA3/CA4,
    dentate gyrus, parasubiculum, presubiculum, subiculum). **Depth:
    up to five levels** (the hippocampus's CA1-CA4 are the deepest
    leaves in the tree). The **CA1-CA4 subfields** are the **deepest
    leaves** in the entire subcortical tree.

**Not children (deliberately excluded):**
*   **Parahippocampal gyrus** —
    ``cortex/temporal/gyri/parahippocampal_gyrus/`` — **neocortical**,
    under the **temporal cortex**, not the medial temporal lobe.
*   **Entorhinal cortex** —
    ``cortex/temporal/gyri/entorhinal_cortex/`` — **allocortical/
    transitional**, under the **temporal cortex**, not the medial
    temporal lobe.
*   **Perirhinal cortex** —
    ``cortex/temporal/gyri/perirhinal_cortex/`` — **neocortical/
    transitional**, under the **temporal cortex**, not the medial
    temporal lobe.
*   **Extended amygdala** — ``extended_amygdala/`` — a **sibling** of
    the medial temporal lobe, not a child of it.
*   **Basal ganglia** — ``basal_ganglia/`` — a **sibling** of the
    medial temporal lobe, not a child of it.
*   **Basal forebrain** — ``basal_forebrain/`` — a **sibling** of
    the medial temporal lobe, not a child of it.

The Medial Temporal Lobe / Amygdala Boundary
--------------------------------------------
This is the **fear** boundary:

*   **Medial temporal lobe** (this module) — the **container**. It
    contains the **amygdala** and the **hippocampus**.

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **fear/emotion/salience** child. Contains the **central
    nucleus** (fear-output, SLEA component), the **basolateral
    nuclei** (fear-learning), the **medial nucleus** (olfactory-
    amygdala), the **cortical nuclei** (olfactory-amygdala), and
    the **main olfactory system** and **accessory olfactory
    system**.

**The amygdala is a CHILD of the medial temporal lobe** — it is **not
the container itself**. The **medial temporal lobe** contains **two**
children (amygdala and hippocampus); the **amygdala** is the **fear**
half. Consumers must **not** conflate the two.

**The central amygdaloid nucleus** (under the amygdala) is the **only
remaining SLEA component** — the **fear-output** structure and the
**SLEA fear-anxiety continuum** node. After the **central nucleus**
leaf is written, the **full SLEA story** will be **fully documented**.

The Medial Temporal Lobe / Hippocampus Boundary
-----------------------------------------------
This is the **memory** boundary:

*   **Medial temporal lobe** (this module) — the **container**. It
    contains the **amygdala** and the **hippocampus**.

*   **Hippocampus** (``.../medial_temporal_lobe/hippocampus/``) — the
    **memory/spatial navigation** child. Contains the **cornu
    ammonis** (CA1-CA4), the **dentate gyrus**, the **subiculum**,
    the **presubiculum**, and the **parasubiculum**.

**The hippocampus is a CHILD of the medial temporal lobe** — it is
**not the container itself**. The **medial temporal lobe** contains
**two** children (amygdala and hippocampus); the **hippocampus** is
the **memory** half. Consumers must **not** conflate the two.

The Medial Temporal Lobe / Parahippocampal Region Boundary
----------------------------------------------------------
This is the **neocortical vs. allocortical/nuclear** boundary:

*   **Medial temporal lobe** (this module) — the **allocortical and
    nuclear** structures: the **amygdala** (nuclear) and the
    **hippocampus** (archicortical/allocortical).

*   **Parahippocampal region** — the **neocortical/transitional**
    structures under the **temporal cortex**:
    *   **Parahippocampal gyrus** —
        ``cortex/temporal/gyri/parahippocampal_gyrus/``
    *   **Entorhinal cortex** —
        ``cortex/temporal/gyri/entorhinal_cortex/``
    *   **Perirhinal cortex** —
        ``cortex/temporal/gyri/perirhinal_cortex/``

**The parahippocampal region is NOT under the medial temporal lobe** —
it is under the **temporal cortex**. The **medial temporal lobe**
contains the **allocortical and nuclear** structures (amygdala,
hippocampus); the **parahippocampal region** contains the
**neocortical/transitional** structures (parahippocampal gyrus,
entorhinal, perirhinal). **This is a deliberate boundary choice** —
the tree places the **neocortical** medial temporal structures under
the **temporal cortex**, and the **allocortical/nuclear** structures
under the **medial temporal lobe**.

**Consumers must not conflate the "medial temporal lobe"** (the
allocortical/nuclear container) with the **"parahippocampal
region"** (the neocortical/transitional region under the temporal
cortex). The two are **anatomically adjacent** but **structurally
separate** in the tree.

The Medial Temporal Lobe / Rhinencephalon Boundary
--------------------------------------------------
This is the **rhinencephalon-exclusion** boundary — **both remaining
excluded structures are here**:

*   **Medial temporal lobe** (this module) — contains **two** of the
    five **rhinencephalon-excluded structures**:
    *   **Amygdala** — ``medial_temporal_lobe/amygdala/``
    *   **Hippocampus** — ``medial_temporal_lobe/hippocampus/``

*   **Rhinencephalon** (``.../right/rhinencephalon/``) — the **narrow
    olfactory definition** (bulb, tract, AON, piriform,
    periamygdaloid, uncus). The **amygdala** and **hippocampus** are
    **excluded** from this definition.

**The full rhinencephalon-exclusion set (all five now documented):**

| Excluded structure | Tree location | Leaf status |
|---|---|---|
| **Amygdala** | **`medial_temporal_lobe/amygdala/`** | **Container-level (this module); leaf pending** |
| **Hippocampus** | **`medial_temporal_lobe/hippocampus/`** | **Container-level (this module); leaf pending** |
| Septal nuclei | `basal_forebrain/septal_nuclei/` | ✓ (both sides) |
| Anterior perforated substance | `basal_forebrain/anterior_perforated_substance/` | ✓ (both sides) |
| Olfactory tubercle | `basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/` | ✓ (both sides) |

**Three of the five** rhinencephalon-excluded structures are **fully
documented at the leaf level on both sides**; **two** (amygdala,
hippocampus) are **container-level documented here** and **pending at
the leaf level**. After the **amygdala** and **hippocampus** leaves
are written, **all five** will be **fully documented**.

**Consumers reconstructing the classical full rhinencephalon** must
**union** the rhinencephalon with **all five** excluded structures —
**two of which are here**.

The Medial Temporal Lobe / SLEA Boundary
----------------------------------------
This is the **SLEA** boundary — **the only remaining SLEA component is
here**:

*   **Medial temporal lobe** (this module) — contains the **central
    amygdaloid nucleus** (under the **amygdala**) — the **only
    remaining SLEA component**.

*   **SLEA continuum** — four structures across three containers:
    *   **BNST** — ``extended_amygdala/stria_terminalis/bed_nucleus_of_stria_terminalis/``
        (documented)
    *   **Central amygdaloid nucleus** —
        ``medial_temporal_lobe/amygdala/central_nucleus/`` (**here**)
    *   **Ventral pallidum** —
        ``basal_ganglia/globus_pallidus/ventral_pallidum/``
        (documented)
    *   **Nucleus accumbens** —
        ``basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/``
        (documented)

**The medial temporal lobe is the LAST container to hold a SLEA
component.** After the **central nucleus** leaf is written, the
**full SLEA story** will be **fully documented on both sides at
every level**.

**The central amygdaloid nucleus** is the **fear-output** structure
and the **SLEA fear-anxiety continuum** node. The **right-amygdala
fear association** belongs to the **amygdala module** (central
nucleus) — **not** to the medial temporal lobe container, **not** to
the amygdala container (as a whole), and **not** to the hippocampus.

Function in the Human Brain
---------------------------
The medial temporal lobe has **two functionally distinct
subsystems** — **fear/emotion** (amygdala) and **memory/spatial
navigation** (hippocampus):

**Amygdala (fear/emotion/salience):**

*   **Fear Conditioning (Central Nucleus + Basolateral Nuclei):** The
    **central nucleus** is the **fear-output** structure — it
    produces the **autonomic and behavioral** fear responses
    (freezing, tachycardia, startle). The **basolateral nuclei** are
    the **fear-learning** structures — they **associate** the
    conditioned stimulus with the unconditioned stimulus. Together,
    they mediate **classical fear conditioning**.

*   **Emotional Memory Modulation (Basolateral Nuclei → Hippocampus):**
    The **basolateral nuclei** project to the **hippocampus** and
    **modulate** memory consolidation — **emotional arousal**
    enhances memory (the **"emotional memory"** effect).

*   **Olfactory-Amygdala Processing (Medial Nucleus + Cortical
    Nuclei):** The **medial nucleus** and **cortical nuclei** are
    the **olfactory-amygdala** structures — they receive input from
    the **accessory olfactory system** (pheromones) and the **main
    olfactory system** (odors), and they mediate **pheromonal** and
    **social** behaviors.

*   **SLEA Fear-Anxiety Continuum (Central Nucleus + BNST):** The
    **central nucleus** is part of the **SLEA fear-anxiety
    continuum** — it is the **phasic fear** hub, and the **BNST**
    (under the extended amygdala) is the **sustained anxiety** hub.
    The **stria terminalis** connects them.

**Hippocampus (memory/spatial navigation):**

*   **Episodic Memory (CA1 + Subiculum):** The **hippocampus** is
    the **episodic memory** structure — it **binds** the
    **what/where/when** of an experience into a **unified memory
    trace**, and it **consolidates** it to the **cortex** (via the
    **subiculum** and the **entorhinal cortex**).

*   **Spatial Navigation (CA1 + CA3):** The **CA1** and **CA3**
    subfields contain **place cells** — neurons that fire when the
    animal is in a **specific location** — and **grid cells** (in
    the **entorhinal cortex**) — neurons that fire in a
    **hexagonal grid** pattern. Together, they form the **cognitive
    map**.

*   **Pattern Separation (Dentate Gyrus):** The **dentate gyrus** is
    the **pattern separation** structure — it **distinguishes**
    similar experiences from each other, preventing **memory
    interference**.

*   **Memory Consolidation (Hippocampus → Cortex):** The
    **hippocampus** **consolidates** memories to the **cortex** —
    during **sleep** (especially **slow-wave sleep**), the
    hippocampus **replays** the memory traces, and the cortex
    **stores** them as **long-term memories**.

**The unifying theme:** the medial temporal lobe is the **fear +
memory** container — the **amygdala** is the **fear/emotion** half,
and the **hippocampus** is the **memory/spatial navigation** half.
**The two are functionally distinct** — consumers must **not** treat
the medial temporal lobe as a single functional system.

Associated Disorders
--------------------
The medial temporal lobe container has **no single syndrome** — its
children's disorders are documented in their own modules:

*   **Amygdala (fear/emotion/salience):**
    - **Kluver-Bucy syndrome** — **bilateral amygdala lesions**,
      producing **fearlessness, hypersexuality, hyperorality, and
      visual agnosia**.
    - **Urbach-Wiethe disease** — **bilateral amygdala
      calcification**, producing **fearlessness** and **impaired
      fear recognition**.
    - **PTSD and anxiety disorders** — **amygdala hyperactivity**
      (central nucleus) and **BNST dysfunction** (sustained anxiety).
    - **Autism spectrum disorder** — **amygdala dysfunction**,
      contributing to **social-emotional** deficits.
    - **Temporal lobe epilepsy** — **amygdala kindling** and
      **emotional auras**.

*   **Hippocampus (memory/spatial navigation):**
    - **Alzheimer's disease** — **hippocampal atrophy** is the
      **earliest** and **most consistent** structural finding;
      **episodic memory loss** is the **earliest** clinical symptom.
    - **Temporal lobe epilepsy** — **hippocampal sclerosis** (CA1
      and CA3 neuron loss) is the **most common** cause of
      **drug-resistant** temporal lobe epilepsy.
    - **Anterograde amnesia** — **bilateral hippocampal lesions**
      (e.g., **patient H.M.**) produce **inability to form new
      episodic memories**.
    - **Spatial memory deficits** — **hippocampal dysfunction**
      impairs **spatial navigation** (e.g., in **taxi drivers**,
      **London** — hippocampal volume correlates with navigation
      experience).
    - **Depression** — **hippocampal volume reduction** is a
      **consistent** finding in **major depressive disorder**.

*   **Container-level:** **no single syndrome** — the medial temporal
  lobe is a **structural grouping**, and its disorders are the
  **aggregate** of its children's disorders.

**What is NOT here:** The medial temporal lobe is **not** the substrate
for **semantic dementia** (anterior temporal neocortex — under the
**temporal cortex**), **Wernicke's aphasia** (BA22 — under the
**temporal cortex**), **prosopagnosia** (fusiform gyrus — under the
**temporal cortex**), or **Alzheimer's disease as a whole** (nucleus
basalis — basal forebrain; cortical pathology — cortex). Its clinical
footprint is **fear/emotion** (Kluver-Bucy, Urbach-Wiethe, PTSD) and
**memory** (Alzheimer's, hippocampal sclerosis, amnesia) — a
**distinct category**.

Lateralization Notes
--------------------
This is the **right** medial temporal lobe container. The medial
temporal lobe is **bilaterally symmetric** and **largely
non-lateralized at the container level** — but it carries an
**EMPHATIC amygdala-lateralization warning** (matching the
**subcortical** container):

*   **Bilateral Fear and Memory Functions:** Each hemisphere has its
    own amygdala (fear) and hippocampus (memory). The two sides are
    **functionally symmetric** for basic fear and memory functions.

*   **Partial Lateralization (Amygdala — Contested):** The **right
    amygdala** is sometimes reported to be **more involved in fear
    processing** than the left. This is **partial**, **contested**,
    and documented in the **amygdala module** (not at the container
    level). **The right-amygdala fear association belongs to the
    amygdala module (central nucleus)** — **not** to the medial
    temporal lobe container. **This is especially important for this
    right-side module** — the **right medial temporal lobe** contains
    the **right amygdala** as a **direct child**, and a consumer
    reading the right-side module is **exactly** the consumer most
    likely to attribute the right-amygdala fear association to the
    whole medial temporal lobe. **Do not.** The right medial temporal
    lobe is **not** the right amygdala.

*   **Partial Lateralization (Hippocampus — Contested):** The **left
    hippocampus** is sometimes reported to be **more involved in
    verbal memory**; the **right hippocampus** in **spatial memory**.
    This is **partial**, **contested**, and documented in the
    **hippocampus module** (not at the container level).

*   **EMPHATIC AMYGDALA-LATERALIZATION WARNING (matching the
    subcortical container):** The **medial temporal lobe container**
    carries an **EMPHATIC** warning: the **amygdala** is a **direct
    child**, and the **right-amygdala fear association** belongs to
    the **amygdala module** (central nucleus) — **not** to the
    **medial temporal lobe container**. **This is the first container
    in the tree with an EMPHATIC warning, matching the `subcortical`
    container** — because the **amygdala** (the fear-output
    structure) is a **direct child**. Consumers must **not** import
    the right-amygdala fear association into the **medial temporal
    lobe container** — the **container is not the amygdala**, and
    the **right-amygdala fear association** belongs to the
    **amygdala module** (central nucleus). **The right-side module
    carries the emphatic warning explicitly** — a dedicated "Do not
    import" Usage block, an emphatic Lateralization note, and a
    contrast reference.

*   **Right-amygdala fear association (contrast — not this
    container):** The **right amygdala's fear association** belongs
    to the **amygdala module** (central nucleus) and (weakly via
    SLEA) to the **extended amygdala module** — **not** to the
    medial temporal lobe container, **not** to the hippocampus, and
    **not** to the medial temporal lobe as a whole. **This is the
    most important right-side warning in the entire subcortical
    tree** — the **right medial temporal lobe** is the **direct
    parent** of the **right amygdala**, and a consumer reading the
    right-side module is **exactly** the consumer most likely to
    attribute the right-amygdala fear association to the medial
    temporal lobe as a whole. **Do not.** The right medial temporal
    lobe is **not** the right amygdala, and the **right-amygdala
    fear association** belongs to the **amygdala module** (central
    nucleus) — **not** here.

**A consumer that assumes "right medial temporal lobe = left medial
temporal lobe" will be structurally correct** — the two sides are
**symmetric** at the container level. But the **amygdala** and
**hippocampus** have **partial lateralization** (documented in their
own modules, not at the container level). The medial temporal lobe
container is a **strict-mirror pair with an EMPHATIC warning** —
matching the **subcortical container**. **The right-side module
carries the emphatic warning explicitly** — a dedicated "Do not
import" Usage block, an emphatic Lateralization note, and a contrast
reference.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``cortex/``, ``.../extended_amygdala/``, ``.../basal_ganglia/``,
    or any other container. The medial temporal lobe's relationships
    to the parahippocampal region, extended amygdala, and basal
    ganglia are documented as **prose and boundary data**, not as
    structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — two children, closed set.** The medial
    temporal lobe has exactly two children: ``amygdala`` and
    ``hippocampus``. Consumers may iterate them, but should not
    assume any others exist.
*   **DEEPEST container — FIVE levels deep.** The medial temporal
    lobe is the **deepest container in the entire tree** — the
    hippocampus's CA1-CA4 subfields are **five levels** from the
    subcortical container. Consumers must be prepared to **recurse to
    five levels**.
*   **CONTAINS BOTH REMAINING RHINENCEPHALON-EXCLUDED STRUCTURES.**
    The **amygdala** and **hippocampus** are **two of the five**
    rhinencephalon-excluded structures. After their leaves are
    written, **all five** will be **fully documented at the leaf
    level**.
*   **CONTAINS THE ONLY REMAINING SLEA COMPONENT.** The **central
    amygdaloid nucleus** (under the amygdala) is the **only
    remaining SLEA component**. After its leaf is written, the
    **full SLEA story** will be **fully documented on both sides at
    every level**.
*   **EMPHATIC AMYGDALA-LATERALIZATION WARNING — matching the
    subcortical container.** The **amygdala** is a **direct child**
    of the medial temporal lobe, and the **amygdala** is the
    **fear-output** structure. **Consumers must not import
    amygdala-lateralization claims into the medial temporal lobe
    container** — the **right-amygdala fear association** belongs
    to the **amygdala module** (central nucleus). **The right-side
    module carries the emphatic warning explicitly** — a dedicated
    "Do not import" Usage block, an emphatic Lateralization note,
    and a contrast reference — because the **right medial temporal
    lobe** contains the **right amygdala** as a **direct child**.
*   **NOT the parahippocampal gyrus — under the temporal cortex.**
    The **parahippocampal gyrus**, **entorhinal cortex**, and
    **perirhinal cortex** are under the **temporal cortex** —
    **not** the medial temporal lobe. The medial temporal lobe
    contains the **allocortical and nuclear** structures; the
    parahippocampal region contains the **neocortical/transitional**
    structures.
*   **NOT a single functional system — FEAR vs. MEMORY split.** The
    **amygdala** (fear/emotion) and **hippocampus** (memory/spatial
    navigation) are **functionally distinct**. Consumers must not
    treat the medial temporal lobe as a single functional system.
*   **No ``AREA_PATHS`` hop.** The medial temporal lobe is a local
    container under the subcortical container, not a cross-listed
    leaf.
*   **No nested cross-listing.** The medial temporal lobe has no
    nested dual-framing module. It is a single container.
*   **Structural parity with left medial temporal lobe — strict
    mirror with an EMPHATIC warning.** Right and left medial temporal
    lobe modules are **structurally identical** — same two children,
    same five-level recursion, same **both-remaining-excluded-
    structures** flag, same **only-remaining-SLEA-component** flag,
    same **emphatic warning**. **The right-side module carries the
    emphatic warning explicitly** — a dedicated "Do not import"
    Usage block, an emphatic Lateralization note, and a contrast
    reference.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical import medial_temporal_lobe

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "medial_temporal_lobe"
    )

**Do not** assume the medial temporal lobe is a **flat container**.
It is the **deepest container in the entire tree** — **five levels**
deep (the hippocampus's CA1-CA4 subfields are the deepest leaves).
Consumers must be prepared to **recurse to five levels**.

**Do not** assume the medial temporal lobe **contains** the
**parahippocampal gyrus**, **entorhinal cortex**, or **perirhinal
cortex**. Those are **neocortical/transitional** structures under
the **temporal cortex** — **not** under the medial temporal lobe.
The medial temporal lobe contains the **allocortical and nuclear**
structures (amygdala, hippocampus).

**Do not** assume the medial temporal lobe is the **amygdala**. The
**amygdala** is a **child** of the medial temporal lobe — not the
container itself. The medial temporal lobe contains **two** children
(amygdala and hippocampus).

**Do not** assume the medial temporal lobe is the **hippocampus**.
The **hippocampus** is a **child** of the medial temporal lobe — not
the container itself.

**Do not** assume the medial temporal lobe is a **single functional
system**. Its **amygdala** (fear/emotion) and **hippocampus**
(memory/spatial navigation) are **functionally distinct**.

**Do not** import **right-amygdala lateralization claims** into the
right medial temporal lobe container. **This is the FIRST container
in the tree with an EMPHATIC warning, matching the `subcortical`
container** — the **right amygdala** (the fear-output structure) is
a **direct child** of the right medial temporal lobe, and the
**right-amygdala fear association** belongs to the **amygdala
module** (central nucleus). **This is the most important right-side
warning in the entire subcortical tree** — the right medial temporal
lobe is the **direct parent** of the right amygdala, and a consumer
reading the right-side module is **exactly** the consumer most likely
to attribute the right-amygdala fear association to the medial
temporal lobe as a whole. **Do not.** The right medial temporal lobe
is **not** the right amygdala, and the **right-amygdala fear
association** belongs to the **amygdala module** (central nucleus) —
**not** here.

Iterating the medial temporal lobe's two children (recommended
consumer pattern)::

    MEDIAL_TEMPORAL_LOBE_CHILDREN = (
        "amygdala",
        "hippocampus",
    )
    # Closed set. The medial temporal lobe has exactly two children.

Recursive iteration over the medial temporal lobe tree (recommended
consumer pattern — FIVE LEVELS)::

    # The medial temporal lobe is up to five levels deep. Recurse.
    #
    #   subcortical.medial_temporal_lobe.hippocampus.cornu_ammonis.ca1
    #
    # is a valid leaf; so is
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #
    # Do not stop at the first level. The deepest leaves are the
    # hippocampal CA1-CA4 subfields (five levels).

Reconstructing the classical full rhinencephalon (recommended
consumer pattern — BOTH remaining excluded structures are here)::

    # The rhinencephalon's narrow definition excludes five
    # structures. TWO of the five are HERE:
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",       # THIS MODULE
            "medial_temporal_lobe.hippocampus",    # THIS MODULE
            "basal_forebrain.septal_nuclei",
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",
        ),
    }
    # After the amygdala and hippocampus leaves are written, ALL FIVE
    # rhinencephalon-excluded structures will be fully documented.

Reconstructing the FULL SLEA (recommended consumer pattern — the
ONLY REMAINING SLEA component is here)::

    # The SLEA continuum is four structures across three containers.
    # THREE are documented; the central amygdaloid nucleus is HERE:
    FULL_SLEA = {
        "subcortical.extended_amygdala.stria_terminalis."
        "bed_nucleus_of_stria_terminalis": (
            # BNST — documented
        ),
        "subcortical.medial_temporal_lobe.amygdala.central_nucleus": (
            # Central amygdaloid nucleus — THIS MODULE
        ),
        "subcortical.basal_ganglia.globus_pallidus.ventral_pallidum": (
            # Ventral pallidum — documented
        ),
        "subcortical.basal_ganglia.striatum.ventral_striatum."
        "nucleus_accumbens": (
            # Nucleus accumbens — documented
        ),
    }
    # After the central nucleus leaf is written, the FULL SLEA story
    # will be fully documented on both sides at every level.

Reaching the amygdala (recommended consumer pattern — the FEAR
child)::

    # The amygdala is a CHILD of the medial temporal lobe — the
    # fear/emotion/salience subsystem:
    #
    #   subcortical.medial_temporal_lobe.amygdala
    #
    # It contains the central nucleus (fear-output, SLEA component),
    # the basolateral nuclei (fear-learning), and the olfactory-
    # amygdala structures.

Reaching the hippocampus (recommended consumer pattern — the MEMORY
child)::

    # The hippocampus is a CHILD of the medial temporal lobe — the
    # memory/spatial navigation subsystem:
    #
    #   subcortical.medial_temporal_lobe.hippocampus
    #
    # It contains the cornu ammonis (CA1-CA4), the dentate gyrus,
    # the subiculum, the presubiculum, and the parasubiculum.

Reaching the parahippocampal region (recommended consumer pattern —
NOTE the temporal cortex boundary)::

    # The parahippocampal gyrus, entorhinal cortex, and perirhinal
    # cortex are under the TEMPORAL CORTEX — not the medial temporal
    # lobe:
    #
    #   cortex.temporal.gyri.parahippocampal_gyrus
    #   cortex.temporal.gyri.entorhinal_cortex
    #   cortex.temporal.gyri.perirhinal_cortex
    #
    # Do NOT resolve them through the medial temporal lobe.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        mtl_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"medial_temporal_lobe"
        )
        # resolve mtl_path through the memory/recall layer

References
----------
*   **Canonical medial temporal lobe anatomy:** Amaral, D.G.,
    Insausti, R. (1990). "The hippocampal formation." In *The Human
    Nervous System* (Paxinos, G., ed.). (Definitive hippocampal
    anatomy; CA1-CA4, dentate gyrus, subiculum; relationship to the
    parahippocampal region.)
*   **Amygdala anatomy:** Amaral, D.G., Price, J.L., Pitkänen, A.,
    Carmichael, S.T. (1992). "Anatomical organization of the primate
    amygdaloid complex." In *The Amygdala* (Aggleton, J.P., ed.).
    (Definitive amygdala anatomy; basolateral, central, medial, and
    cortical nuclei.)
*   **Fear conditioning:** LeDoux, J.E. (2000). "Emotion circuits in
    the brain." *Annual Review of Neuroscience* 23:155–184.
    (Central nucleus and basolateral nuclei in fear conditioning.)
*   **Kluver-Bucy syndrome:** Kluver, H., Bucy, P.C. (1939).
    "Preliminary analysis of functions of the temporal lobes in
    monkeys." *Archives of Neurology and Psychiatry* 42:979–1000.
    (Bilateral amygdala lesions and the Kluver-Bucy syndrome.)
*   **Hippocampal memory:** Scoville, W.B., Milner, B. (1957). "Loss
    of recent memory after bilateral hippocampal lesions." *Journal
    of Neurology, Neurosurgery, and Psychiatry* 20:11–21. (Patient
    H.M.; bilateral hippocampal lesions and anterograde amnesia.)
*   **Spatial navigation:** O'Keefe, J., Dostrovsky, J. (1971). "The
    hippocampus as a spatial map: preliminary evidence from unit
    activity in the freely-moving rat." *Brain Research* 34:171–175.
    (Place cells in the hippocampus; cognitive map.)
*   **Grid cells:** Hafting, T., Fyhn, M., Molden, S., Moser, M.-B.,
    Moser, E.I. (2005). "Microstructure of a spatial map in the
    entorhinal cortex." *Nature* 436:801–806. (Grid cells in the
    entorhinal cortex.)
*   **Pattern separation:** Yassa, M.A., Stark, C.E.L. (2011).
    "Pattern separation in the hippocampus." *Trends in
    Neurosciences* 34:515–525. (Dentate gyrus in pattern
    separation.)
*   **Alzheimer's disease:** Braak, H., Braak, E. (1991).
    "Neuropathological stageing of Alzheimer-related changes." *Acta
    Neuropathologica* 82:239–259. (Hippocampal involvement in early
    Alzheimer's disease.)
*   **Hippocampal sclerosis:** Mathern, G.W., et al. (1995).
    "Hippocampal sclerosis in temporal lobe epilepsy." *Annals of
    Neurology* 37:190–196. (Hippocampal sclerosis in temporal lobe
    epilepsy.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this container):** Morris, J.S., Öhman, A., Dolan, R.J. (1998).
    "A subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association belongs to the **amygdala module** — **not** to the
    right medial temporal lobe container.)
*   **Parahippocampal region (contrast — under the temporal
    cortex):** Insausti, R., Amaral, D.G. (2012). "Hippocampal
    formation." In *The Human Nervous System* (Mai, J.K., Paxinos,
    G., eds.), 3rd ed. (Parahippocampal gyrus, entorhinal cortex,
    and perirhinal cortex as neocortical/transitional structures
    under the temporal cortex — not under the medial temporal lobe.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Medial temporal lobe in overview.)
*   NeuroNames — Medial temporal lobe (right); FMA — Medial temporal
    lobe (right member).
"""