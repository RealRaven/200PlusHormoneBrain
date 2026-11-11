"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.extended_amygdala.stria_terminalis
=========================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── extended_amygdala
                    └── stria_terminalis   <-- THIS MODULE
                        └── bed_nucleus_of_stria_terminalis

**Primary synonym:** Stria terminalis; terminal stria; stria
terminalis (Latin: "terminal stria"); "the terminal stria."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**white-matter tract** — the **fiber pathway** of the extended
amygdala — wired as a **container** under the extended amygdala
container.
**Part of:** The **extended amygdala** container — specifically, the
**fiber pathway** of the extended amygdala. Its **one child** is the
**bed nucleus of the stria terminalis (BNST)** — the **grey-matter
nucleus** at its terminus.
**Structural parent:** ``.../right/subcortical/extended_amygdala/`` →
**direct child** of the extended amygdala container.
**Structural children (one, closed set):**
``bed_nucleus_of_stria_terminalis`` (the **BNST** — the grey-matter
nucleus at the terminus of the stria terminalis).
**Boundary status (WHITE-MATTER TRACT AS CONTAINER — unique in the
tree):** **Boundary case — the stria terminalis is a WHITE-MATTER
TRACT that is wired as a CONTAINER, with the BNST as its child.**
This is the **only white-matter tract in the entire tree wired as a
container** — every other white-matter tract (fornix, internal
capsule, corpus callosum, corona radiata, etc.) is a **leaf** under
``.../right/white_matter/``. The stria terminalis is **wired here**,
under the **extended amygdala** container, because it is the **fiber
pathway of the extended amygdala** — a **deliberate boundary choice**
that treats the tract as **functionally part of** the extended
amygdala, not as a generic white-matter bundle. Consumers must **not**
resolve the stria terminalis through ``white_matter/`` — it is
**here**, as a **container**.
**Boundary status (TERMINUS NUCLEUS pattern — a fiber tract as
parent of a grey-matter nucleus):** **Boundary case — the stria
terminalis is the ONLY place in the tree where a WHITE-MATTER TRACT
is the PARENT of a GREY-MATTER NUCLEUS.** The **BNST** (the child)
is named after the stria terminalis — **"bed nucleus of the stria
terminalis"** literally means "the nucleus at the **bed (terminus)
of the stria terminalis**." The **fiber tract** and its **terminus
nucleus** are **structurally coupled**: the tract is the **fiber
pathway**, and the nucleus is the **grey-matter structure at its
terminus**. This is a **unique parent-child relationship** in the
tree — a **fiber tract as parent**, a **nucleus as child**. Consumers
must **not** expect this pattern elsewhere — every other
**fiber tract** in the tree is a **leaf** under ``white_matter/``,
and every other **nucleus** is a **direct child of a container**.
The **stria terminalis/BNST** pair is the **only** instance of the
**terminus nucleus** pattern.
**Boundary status (CROSS-CONTAINER FIBER PATHWAY — carries fibers
from the amygdala to the extended amygdala and septal region):**
**Boundary case — the stria terminalis is a CROSS-CONTAINER FIBER
PATHWAY.** It carries axons from the **amygdala** (under
``medial_temporal_lobe/amygdala/``) — especially the **central
nucleus** and **medial nucleus** — to the **BNST** (here, under the
extended amygdala) and to the **septal region** (under
``basal_forebrain/septal_nuclei/``). **The tract crosses THREE
containers**:
*   **Source:** the **amygdala** — under ``medial_temporal_lobe/``
*   **Terminus:** the **BNST** — **here**, under
    ``extended_amygdala/``
*   **Terminus:** the **septal region** — under
    ``basal_forebrain/septal_nuclei/``
**Consumers reconstructing the full stria terminalis circuit** must
**union** across the **amygdala**, the **extended amygdala**, and the
**basal forebrain** — the tree does **not** provide the union as a
single path. **This is the only cross-container fiber pathway in the
tree** — every other white-matter tract is confined to its own
container.
**Boundary status (SPLIT CONTINUUM FIBER PATHWAY — the classical
extended amygdala's fiber bundle):** **Boundary case — the stria
terminalis is the FIBER PATHWAY of the CLASSICAL extended amygdala
(BNST + central amygdaloid nucleus), which the tree SPLITS across two
containers.** The **classical extended amygdala** is the **BNST**
(here, under the extended amygdala) + the **central amygdaloid
nucleus** (under ``medial_temporal_lobe/amygdala/central_nucleus/``).
The **stria terminalis** is the **fiber pathway** connecting the two
— it carries axons **from the central nucleus to the BNST** (and to
the **septal region**). **Consumers reconstructing the classical
extended amygdala** must **union** the **BNST** (here) and the
**central nucleus** (under the amygdala), and the **stria terminalis**
is the **anatomical substrate** of that connection. **The split
continuum's fiber pathway is wired under the extended amygdala (the
SLEA anchor)** — a **deliberate boundary choice** reflecting the
tract's role in the **extended amygdala continuum**.
**Boundary status (not under white_matter/ — a deliberate
asymmetry with the fornix):** **Boundary case — the stria terminalis
is NOT under `white_matter/`, unlike the FORNIX (which IS under
`white_matter/`).** The **fornix** (``.../right/white_matter/fornix/``)
is a **limbic white-matter tract** — like the stria terminalis —
but it is **wired under `white_matter/`**, while the **stria
terminalis** is **wired under the extended amygdala container**.
**This is a deliberate asymmetry**: the **fornix** is a **generic
limbic tract** (hippocampus → mammillary body / septal region), and
it is wired under ``white_matter/``; the **stria terminalis** is the
**fiber pathway of the extended amygdala**, and it is wired under the
**extended amygdala container**. Consumers must **not** assume the
two limbic tracts follow the same wiring convention — the **fornix
is under white_matter/**, and the **stria terminalis is under the
extended amygdala**. **This asymmetry is a deliberate boundary choice
reflecting the stria terminalis's role as the extended amygdala's
fiber pathway.**
**Boundary status (not the central amygdaloid nucleus — SOURCE, not
terminus):** **Boundary case — the central amygdaloid nucleus is the
SOURCE of the stria terminalis fibers, NOT the terminus.**
The **central nucleus** (under ``medial_temporal_lobe/amygdala/central_nucleus/``)
projects **through the stria terminalis** to the **BNST** (here) and
the **septal region**. It is the **source** of the fibers — **not**
the **terminus** and **not** the **tract itself**. Consumers must
**not** conflate the **central nucleus** (a grey-matter structure)
with the **stria terminalis** (a white-matter tract). The **central
nucleus** is under the **amygdala**; the **stria terminalis** is
**here**.
**Boundary status (not the amygdala — SOURCE, not pathway):**
**Boundary case — the amygdala is the SOURCE of the stria terminalis
fibers, NOT the tract itself.** The **amygdala** (under
``medial_temporal_lobe/amygdala/``) — especially the **central
nucleus** and **medial nucleus** — projects **through the stria
terminalis**. The **amygdala** is the **source structure**; the
**stria terminalis** is the **fiber pathway**. Consumers must **not**
resolve the amygdala through the stria terminalis, or the stria
terminalis through the amygdala.
**Boundary status (not the septal region — TERMINUS, not pathway):**
**Boundary case — the septal region is a TERMINUS of the stria
terminalis fibers, NOT the tract itself.** The **septal nuclei**
(under ``basal_forebrain/septal_nuclei/``) receive stria terminalis
fibers (from the amygdala) — they are a **terminus** of the tract.
The **septal region** is a **grey-matter structure**; the **stria
terminalis** is the **fiber pathway**. Consumers must **not** resolve
the septal region through the stria terminalis, or the stria
terminalis through the septal region.
**Boundary status (not the fornix — a DIFFERENT white-matter tract):**
**Boundary case — the fornix is a DIFFERENT white-matter tract.**
The **fornix** (under ``.../right/white_matter/fornix/``) is the
**hippocampal fiber pathway** (hippocampus → mammillary body / septal
region). The **stria terminalis** is the **amygdaloid fiber pathway**
(amygdala → BNST / septal region). They are **two different white-
matter tracts** — both limbic, both terminate in the septal region,
but they originate from **different grey-matter structures** (the
**hippocampus** vs. the **amygdala**) and are **wired under different
containers** (the **fornix under white_matter/**; the **stria
terminalis under the extended amygdala**). Consumers must **not**
conflate the two.
**Boundary status (white-matter tract — NOT a neural processor):**
**Boundary case — the stria terminalis is a WHITE-MATTER TRACT,
not a neural processor.** It is a **fiber bundle** — an **axonal
pathway** connecting grey-matter structures. It does **not** process
neural information — it **conducts** it. Consumers must **not**
treat the stria terminalis as a grey-matter structure or a neural
processor — it is a **conduction pathway**.

Overview
--------
The stria terminalis is the **fiber pathway of the extended
amygdala** — a **C-shaped white-matter tract** that carries axons
from the **amygdala** (especially the **central nucleus** and **medial
nucleus**) to the **BNST** (the **terminus nucleus** at its bed) and
the **septal region**. It is the **only white-matter tract in the
entire tree wired as a container** — a **deliberate boundary choice**
reflecting its role as the **extended amygdala's fiber pathway**.
Its **one child** is the **BNST** — the **grey-matter nucleus at its
terminus** — a **unique parent-child relationship** in the tree:
a **fiber tract as parent**, a **nucleus as child**.

**The stria terminalis is a CROSS-CONTAINER fiber pathway.** It
carries fibers from the **amygdala** (under
``medial_temporal_lobe/amygdala/``) to the **BNST** (here, under
``extended_amygdala/``) and the **septal region** (under
``basal_forebrain/septal_nuclei/``). **This is the only
cross-container fiber pathway in the tree** — every other white-
matter tract is confined to its own container. **Consumers
reconstructing the full stria terminalis circuit** must **union**
across the **amygdala**, the **extended amygdala**, and the **basal
forebrain** — the tree does **not** provide the union as a single
path.

**The stria terminalis is the fiber pathway of the CLASSICAL
extended amygdala** — which the tree **splits** across two
containers (BNST here, central nucleus under the amygdala). The
**stria terminalis** is the **anatomical substrate** of the
**BNST ↔ central nucleus** connection — the **physical link** between
the two halves of the **classical extended amygdala**. **Consumers
reconstructing the classical extended amygdala** must **union** the
**BNST** (here) and the **central nucleus** (under the amygdala), and
the **stria terminalis** is the **tract that connects them**.

**The stria terminalis is NOT under `white_matter/`, unlike the
fornix.** This is a **deliberate asymmetry** — the **fornix** is a
**generic limbic tract** (hippocampus → mammillary body / septal
region), wired under ``white_matter/``; the **stria terminalis** is
the **extended amygdala's fiber pathway**, wired under the **extended
amygdala container**. **Consumers must not assume the two limbic
tracts follow the same wiring convention.**

**The stria terminalis is a paired structure.** Each hemisphere has
its own stria terminalis, carrying **ipsilateral** fibers from its
own amygdala to its own BNST and septal region. The two sides are
**bilaterally symmetric** and **functionally non-lateralized** — the
**amygdala-BNST** connection is **bilateral**. See *Lateralization
Notes*.

Anatomy (origin, course, termination)
-------------------------------------
The stria terminalis is a **C-shaped white-matter tract** with a
well-characterized **origin**, **course**, and **termination**:

*   **Origin** — the **amygdala** (under
    ``medial_temporal_lobe/amygdala/``), especially the **central
    nucleus** (the **fear-output** structure) and the **medial
    nucleus** (the **olfactory-amygdala** structure). The **stria
    terminalis** carries **efferent** axons from these nuclei.

*   **Course** — the tract **arches** from the **amygdala** in the
    **temporal lobe** (under the **lenticular nucleus**), **curves**
    around the **thalamus** in the **groove between the thalamus and
    the caudate nucleus**, and **runs** along the **medial wall of
    the lateral ventricle** — a **C-shaped** course that follows the
    **caudate** and **thalamus**.

*   **Termination** — the **BNST** (here, under the extended amygdala)
    — the **bed nucleus of the stria terminalis** — and the **septal
    region** (under ``basal_forebrain/septal_nuclei/``). The **BNST**
    is the **main terminus** — the **grey-matter nucleus at the bed
    (terminus) of the stria terminalis** — and the **septal region**
    is the **secondary terminus**.

**The stria terminalis is a CROSS-CONTAINER fiber pathway** — it
**crosses three containers**:
*   **Source:** the **amygdala** — under ``medial_temporal_lobe/``
*   **Terminus:** the **BNST** — **here**, under
    ``extended_amygdala/``
*   **Terminus:** the **septal region** — under
    ``basal_forebrain/septal_nuclei/``

**The "bed nucleus" name** — the **BNST** is named after the **stria
terminalis** — **"bed nucleus of the stria terminalis"** literally
means "the nucleus at the **bed (terminus) of the stria terminalis**."
The **tract** and its **terminus nucleus** are **structurally
coupled** — the tract is the **fiber pathway**, and the nucleus is
the **grey-matter structure at its terminus**. **This is the only
"terminus nucleus" pattern in the tree** — a **fiber tract as parent**,
a **nucleus as child**.

Fiber Composition (prose, not structural children)
--------------------------------------------------
The stria terminalis carries fibers from **multiple amygdaloid
nuclei** to **multiple targets**, all documented as **prose**:

*   **From the central nucleus** — to the **BNST** (here) and the
    **lateral hypothalamus** and **brainstem** — the **fear-output**
    pathway of the **central nucleus**.

*   **From the medial nucleus** — to the **BNST** (here) and the
    **septal region** — the **olfactory-amygdala** pathway (the
    **medial nucleus** is part of the **accessory olfactory
    system**).

*   **From the basolateral nuclei** (to a lesser extent) — to the
    **BNST** and **prefrontal cortex** — a **modulatory** pathway
    from the **fear-learning** nuclei.

*   **From the cortical nuclei** (to a lesser extent) — to the
    **BNST** and **olfactory structures** — an **olfactory-amygdala**
    pathway.

**These fiber populations are prose, not structural children.** The
tree wires the **stria terminalis** as a **single container** with
**one child** (the BNST) — the **fiber populations** are **prose**,
not **structural children**. Consumers that need **fiber-level**
resolution should consult the references, not the tree.

The Stria Terminalis / BNST Boundary
------------------------------------
This is the **parent-child** boundary of the module — the **terminus
nucleus** pattern:

*   **Stria terminalis** (this module) — the **white-matter tract**
    (the **fiber pathway**). **Container.**

*   **BNST** (``.../stria_terminalis/bed_nucleus_of_stria_terminalis/``)
    — the **grey-matter nucleus** at the **terminus of the stria
    terminalis** (the **bed nucleus**). **Child.**

**The BNST is named after the stria terminalis** — **"bed nucleus of
the stria terminalis"** means "the nucleus at the **bed (terminus)
of the stria terminalis**." The **tract** and its **terminus nucleus**
are **structurally coupled** — the tract is the **fiber pathway**,
and the nucleus is the **grey-matter structure at its terminus**.
**This is the only "terminus nucleus" pattern in the tree.**

**The BNST is the main grey-matter structure of the extended
amygdala container** — the **stress/anxiety hub** — and it is the
**terminus nucleus** of the stria terminalis. **The stria
terminalis module** documents the **tract**; the **BNST module**
documents the **nucleus**. Consumers must **not** resolve the BNST
through the stria terminalis, or the stria terminalis through the
BNST — they are **separate structures** (a tract and a nucleus) that
are **structurally coupled** by the **terminus nucleus** pattern.

The Stria Terminalis / Amygdala Boundary
----------------------------------------
This is the **source** boundary:

*   **Stria terminalis** (this module) — the **fiber pathway** (from
    the amygdala to the BNST and septal region).

*   **Amygdala** (``.../medial_temporal_lobe/amygdala/``) — the
    **source structure** — especially the **central nucleus** and
    the **medial nucleus**. **Under the medial temporal lobe.**

**The amygdala is the SOURCE of the stria terminalis fibers** — it is
**NOT** the tract itself, and it is **NOT** under the extended
amygdala container. The **stria terminalis** **carries axons from**
the amygdala; the **amygdala** is the **grey-matter structure** that
**originates** them. Consumers must **not** resolve the amygdala
through the stria terminalis, or the stria terminalis through the
amygdala — they are **separate structures** in **different
containers** (the **amygdala** under the medial temporal lobe; the
**stria terminalis** under the extended amygdala).

The Stria Terminalis / Septal Region Boundary
---------------------------------------------
This is the **secondary terminus** boundary:

*   **Stria terminalis** (this module) — the **fiber pathway** (from
    the amygdala to the BNST and septal region).

*   **Septal region** (``.../basal_forebrain/septal_nuclei/``) — a
    **secondary terminus** of the stria terminalis fibers (from the
    medial nucleus and other amygdaloid nuclei). **Under the basal
    forebrain.**

**The septal region is a TERMINUS of the stria terminalis fibers** —
it is **NOT** the tract itself, and it is **NOT** under the extended
amygdala container. The **stria terminalis** **carries axons to** the
septal region; the **septal nuclei** are the **grey-matter structures**
that **receive** them. Consumers must **not** resolve the septal
region through the stria terminalis, or the stria terminalis through
the septal region — they are **separate structures** in **different
containers** (the **septal region** under the basal forebrain; the
**stria terminalis** under the extended amygdala).

The Stria Terminalis / White Matter Boundary
--------------------------------------------
This is the **white-matter** boundary:

*   **Stria terminalis** (this module) — a **white-matter tract**
    wired **here**, under the **extended amygdala container**.

*   **Other white-matter tracts** — the **fornix**, **internal
    capsule**, **corpus callosum**, **corona radiata**, **external
    capsule**, **extreme capsule**, **cingulum**, **medial forebrain
    bundle**, **mammillothalamic tract**, **fasciculus rectus**,
    **centrum semiovale** — all under ``.../right/white_matter/``.

**The stria terminalis is the ONLY white-matter tract in the tree
wired as a container, NOT as a leaf under `white_matter/`.** The
**fornix** — the **most comparable limbic tract** — is under
``white_matter/fornix/``. **This is a deliberate asymmetry**: the
**fornix** is a **generic limbic tract** (hippocampus → mammillary
body / septal region), wired under ``white_matter/``; the **stria
terminalis** is the **extended amygdala's fiber pathway**, wired
under the **extended amygdala container**.

**Consumers must not assume the two limbic tracts follow the same
wiring convention** — the **fornix is under white_matter/**, and the
**stria terminalis is under the extended amygdala**. **This asymmetry
is a deliberate boundary choice** reflecting the stria terminalis's
role as the **extended amygdala's fiber pathway**.

Function in the Human Brain
---------------------------
The stria terminalis's function is **conduction**, not **processing**
— it is a **fiber pathway** connecting the **amygdala** to the
**BNST** and the **septal region**:

*   **Fear-Output Conduction (from the Central Nucleus):** The
    **stria terminalis** carries **fear-output** fibers from the
    **central amygdaloid nucleus** to the **BNST** (here) and the
    **lateral hypothalamus** and **brainstem** — the **classical
    fear-output pathway**. The **central nucleus** → **stria
    terminalis** → **BNST** is the **anatomical substrate** of
    **fear-to-anxiety** signaling — the **phasic fear** signal
    (central nucleus) **modulating** the **sustained anxiety** hub
    (BNST).

*   **Olfactory-Amygdala Conduction (from the Medial Nucleus):** The
    **stria terminalis** carries **olfactory-amygdala** fibers from
    the **medial nucleus** (part of the **accessory olfactory
    system**) to the **BNST** and the **septal region** — the
    **olfactory-amygdala** pathway that connects **pheromonal
    signals** to the **limbic forebrain**.

*   **Modulatory Conduction (from the Basolateral and Cortical
    Nuclei):** The **stria terminalis** carries **modulatory** fibers
    from the **basolateral nuclei** (the **fear-learning** nuclei)
    and the **cortical nuclei** (the **olfactory-amygdala** nuclei)
    to the **BNST** and the **prefrontal cortex** — a **modulatory**
    pathway that **shapes** the **stress/anxiety** response.

*   **NOT a neural processor.** The **stria terminalis** is a
    **white-matter tract** — it **conducts** neural signals but does
    **not** process them. It is the **conduction pathway** of the
    extended amygdala, **not** a processing structure.

*   **NOT a grey-matter structure.** The **stria terminalis** is a
    **fiber bundle**, not a **nucleus**. Its **child** (the BNST)
    is the **grey-matter structure** at its terminus — the
    **stria terminalis itself** is **axons**, not **neurons**.

**The unifying theme:** the stria terminalis is the **conduction
pathway** of the extended amygdala — a **C-shaped white-matter tract**
that carries fibers from the **amygdala** (fear-output, olfactory-
amygdala, and modulatory nuclei) to the **BNST** (the **stress/
anxiety hub**) and the **septal region**. **It is the ONLY
white-matter tract in the tree wired as a container** — a
**deliberate boundary choice** reflecting its role as the **extended
amygdala's fiber pathway**.

Associated Disorders
--------------------
The stria terminalis has **no named clinical syndrome** — its
clinical associations are **indirect**, via the structures it
connects:

*   **PTSD and Anxiety Disorders (via the Amygdala-BNST Pathway):**
    The **stria terminalis** is the **anatomical substrate** of the
    **amygdala-BNST** connection — the **fear-to-anxiety** pathway
    that is **dysregulated** in **PTSD** and **anxiety disorders**.
    **The tract itself** is **not** the primary substrate — the
    **amygdala** (central nucleus) and the **BNST** are — but the
    **stria terminalis** is the **conduction pathway** that
    **connects them**.

*   **Stress-Induced Relapse (via the Amygdala-BNST Pathway):** The
    **stria terminalis** carries **stress-related** fibers from the
    **amygdala** to the **BNST** — the **pathway** that contributes
    to **stress-induced drug-seeking** and **relapse**. **The tract
    itself** is **not** the primary substrate — the **BNST** is —
    but the **stria terminalis** is the **conduction pathway**.

*   **Olfactory-Amygdala Disorders (via the Medial Nucleus
    Pathway):** The **stria terminalis** carries **olfactory-amygdala**
    fibers from the **medial nucleus** (accessory olfactory system)
    to the **BNST** and the **septal region** — the **pathway** that
    is **involved** in **pheromonal** and **social** behaviors. The
    **tract itself** is **not** the primary substrate.

*   **No Named "Stria Terminalis Syndrome":** The stria terminalis
    is a **fiber pathway**, not a **grey-matter structure** — it
    has **no named clinical syndrome**. Its clinical relevance is
    **indirect**, via the **amygdala** and **BNST** structures it
    connects.

**What is NOT here:** The stria terminalis is **not** the substrate
for **Kluver-Bucy syndrome** (amygdala), **fear conditioning**
(central nucleus), **PTSD** (BNST), **addiction** (nucleus accumbens),
or **Alzheimer's disease** (nucleus basalis). Its clinical
associations are **indirect**, via the **amygdala-BNST pathway** it
subserves. **No named stria terminalis syndrome exists.**

Lateralization Notes
--------------------
This is the **right** stria terminalis module. The stria terminalis
is **bilaterally symmetric** and **functionally non-lateralized** —
and it carries **NO warning**:

*   **Bilateral Amygdala-BNST Connection:** Each stria terminalis
    carries **ipsilateral** fibers from its own amygdala to its own
    BNST and septal region. The two sides are **functionally
    symmetric** for the **amygdala-BNST** connection.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the stria terminalis has **no documented strong
    left-lateralized or right-lateralized function**.

*   **NO Extended-Amygdala Warning (strict mirror with no warning):**
    The stria terminalis is a **white-matter tract** — it has **no
    SLEA relationship** of its own (the **SLEA warning** belongs to
    the **grey-matter structures** — the BNST, central nucleus,
    ventral pallidum, and nucleus accumbens — **not** to the **fiber
    pathway** that connects them). Consumers must **not** import
    amygdala-lateralization claims into the stria terminalis — it is
    a **conduction pathway**, **not** a grey-matter structure.
    **The right-side module carries the same no-warning status** —
    no dedicated Usage block, no contrast reference, no deferral
    note.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** (central nucleus) and (weakly via SLEA) to
    the **extended amygdala module** — **not** to the stria
    terminalis. **The stria terminalis** is a **fiber pathway** —
    it has **no** amygdala-lateralization claim of its own. **This
    is true on the right side as well** — the right stria terminalis
    is a white-matter tract with **no SLEA relationship** of its own.

**A consumer that assumes "right stria terminalis = left stria
terminalis" will be structurally and functionally correct** — the
two sides are **symmetric**, no lateralized syndrome has been
demonstrated, and the stria terminalis is a **strict-mirror pair with
no warning** — a **white-matter tract** that is a **conduction
pathway**, not a grey-matter structure.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../medial_temporal_lobe/``, ``.../basal_forebrain/``,
    ``.../white_matter/``, or any other container. The stria
    terminalis's relationships to the amygdala, BNST, septal region,
    and other white-matter tracts are documented as **prose and
    boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — one child, closed set.** The stria terminalis
    has **exactly one child**: ``bed_nucleus_of_stria_terminalis``
    (the BNST — its **terminus nucleus**). Consumers may iterate it,
    but should not assume any other children exist.
*   **WHITE-MATTER TRACT AS CONTAINER — unique in the tree.** The
    stria terminalis is the **only white-matter tract in the entire
    tree wired as a container** — every other white-matter tract is
    a **leaf** under ``white_matter/``. **Consumers must not resolve
    the stria terminalis through ``white_matter/``** — it is **here**.
*   **TERMINUS NUCLEUS pattern — a fiber tract as parent of a
    grey-matter nucleus.** The **BNST** is named after the stria
    terminalis — **"bed nucleus of the stria terminalis"** means "the
    nucleus at the **bed (terminus)** of the stria terminalis." This
    is the **only "terminus nucleus" pattern in the tree**.
*   **CROSS-CONTAINER FIBER PATHWAY.** The stria terminalis carries
    fibers from the **amygdala** (under the medial temporal lobe) to
    the **BNST** (here) and the **septal region** (under the basal
    forebrain). **This is the only cross-container fiber pathway in
    the tree.** Consumers reconstructing the **full stria terminalis
    circuit** must **union** across **three containers**.
*   **SPLIT CONTINUUM FIBER PATHWAY.** The stria terminalis is the
    **fiber pathway** of the **classical extended amygdala** (BNST +
    central nucleus), which the tree **splits** across **two
    containers**. The **stria terminalis** is the **anatomical
    substrate** of the **BNST ↔ central nucleus** connection.
*   **NOT under `white_matter/` — a deliberate asymmetry with the
    fornix.** The **fornix** is under ``white_matter/``; the **stria
    terminalis** is **here**, under the extended amygdala. **This
    asymmetry is deliberate** — the fornix is a **generic limbic
    tract**; the stria terminalis is the **extended amygdala's fiber
    pathway**.
*   **NOT the central amygdaloid nucleus — SOURCE, not terminus.**
    The **central nucleus** is the **source** of stria terminalis
    fibers; the **BNST** is the **terminus**. The **central nucleus**
    is under the **amygdala**; the **stria terminalis** is **here**.
*   **NOT the amygdala — SOURCE, not pathway.** The **amygdala** is
    the **source structure**; the **stria terminalis** is the
    **fiber pathway**.
*   **NOT the septal region — TERMINUS, not pathway.** The **septal
    region** is a **secondary terminus** of stria terminalis fibers;
    the **stria terminalis** is the **fiber pathway**.
*   **NOT the fornix — a DIFFERENT white-matter tract.** The **fornix**
    is the **hippocampal fiber pathway** (hippocampus → mammillary
    body / septal region); the **stria terminalis** is the
    **amygdaloid fiber pathway** (amygdala → BNST / septal region).
    They are **two different tracts** — both limbic, both terminate
    in the septal region, but **different origins** and **different
    containers**.
*   **WHITE-MATTER TRACT — NOT a neural processor.** The stria
    terminalis is a **fiber bundle** — it **conducts** neural signals
    but does **not** process them.
*   **No ``AREA_PATHS`` hop.** The stria terminalis is a local
    container under the extended amygdala, not a cross-listed leaf.
*   **No nested cross-listing.** The stria terminalis has no nested
    dual-framing module. It is a single container.
*   **Structural parity with left stria terminalis — strict mirror
    with NO warning.** Right and left stria terminalis modules are
    **structurally identical** — same one child (BNST), same
    **terminus nucleus** pattern, same **cross-container fiber
    pathway**, same **split continuum fiber pathway**, same
    **white-matter-as-container** caveat, same **no warning**. **The
    right-side module carries the same no-warning status** — no
    dedicated Usage block, no contrast reference, no deferral note.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.extended_amygdala import stria_terminalis

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "extended_amygdala.stria_terminalis"
    )

**Do not** assume the stria terminalis is under ``white_matter/``.
It is a **white-matter tract** wired **here**, under the **extended
amygdala** — the **only white-matter tract in the tree wired as a
container**. **Resolving it through ``white_matter/`` will fail** —
it is **here**.

**Do not** assume the stria terminalis is the **BNST**. The **stria
terminalis** is a **white-matter tract** (the **fiber pathway**); the
**BNST** is its **child** — the **grey-matter nucleus at its
terminus**. They are **separate structures** (a tract and a nucleus)
that are **structurally coupled** by the **terminus nucleus** pattern.

**Do not** assume the stria terminalis **contains** the **amygdala**.
The **amygdala** is the **source** of the stria terminalis fibers —
it is under ``.../medial_temporal_lobe/amygdala/``, **not** a child
of the stria terminalis.

**Do not** assume the stria terminalis **contains** the **septal
region**. The **septal region** is a **secondary terminus** of stria
terminalis fibers — it is under
``.../basal_forebrain/septal_nuclei/``, **not** a child of the stria
terminalis.

**Do not** conflate the stria terminalis with the **fornix**. The
**fornix** is the **hippocampal fiber pathway** (under
``white_matter/``); the **stria terminalis** is the **amygdaloid
fiber pathway** (under the **extended amygdala**). They are **two
different tracts** — both limbic, both terminate in the septal
region, but **different origins** and **different containers**.

Iterating the stria terminalis's one child (recommended consumer
pattern)::

    STRIA_TERMINALIS_CHILDREN = (
        "bed_nucleus_of_stria_terminalis",   # BNST — the terminus nucleus
    )
    # Closed set. The stria terminalis has exactly one child — the
    # BNST, its terminus nucleus.

Reconstructing the full stria terminalis circuit (recommended
consumer pattern — CROSS-CONTAINER)::

    # The stria terminalis carries fibers from the amygdala to the
    # BNST and the septal region — THREE containers:
    STRIA_TERMINALIS_CIRCUIT = {
        "subcortical.medial_temporal_lobe.amygdala.central_nucleus": (
            # SOURCE — central amygdaloid nucleus
        ),
        "subcortical.medial_temporal_lobe.amygdala.medial_nucleus": (
            # SOURCE — medial amygdaloid nucleus
        ),
        "subcortical.extended_amygdala.stria_terminalis."
        "bed_nucleus_of_stria_terminalis": (
            # TERMINUS — BNST (THIS MODULE's child)
        ),
        "subcortical.basal_forebrain.septal_nuclei": (
            # SECONDARY TERMINUS — septal region
        ),
    }
    # The tree does NOT provide this union as a single path.

Reconstructing the CLASSICAL extended amygdala (recommended consumer
pattern — the stria terminalis is the FIBER PATHWAY)::

    # The classical extended amygdala is BNST + central amygdaloid
    # nucleus. The stria terminalis is the FIBER PATHWAY that
    # connects them:
    CLASSICAL_EXTENDED_AMYGDALA = {
        "subcortical.extended_amygdala.stria_terminalis."
        "bed_nucleus_of_stria_terminalis": (
            # BNST — TERMINUS
        ),
        "subcortical.medial_temporal_lobe.amygdala.central_nucleus": (
            # Central amygdaloid nucleus — SOURCE
        ),
        # The stria terminalis is the FIBER PATHWAY between them.
    }

Reaching the BNST (recommended consumer pattern — the child)::

    # The BNST is the CHILD of the stria terminalis — the
    # grey-matter nucleus at its terminus:
    #
    #   subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
    #
    # The stria terminalis is the TRACT; the BNST is the NUCLEUS.
    # They are structurally coupled by the "terminus nucleus" pattern.

Reaching the amygdala sources (recommended consumer pattern — NOTE
the cross-container boundary)::

    # The amygdala is the SOURCE of stria terminalis fibers — it is
    # under the MEDIAL TEMPORAL LOBE, not under the extended
    # amygdala:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #   subcortical.medial_temporal_lobe.amygdala.medial_nucleus
    #
    # Do NOT resolve the amygdala through the stria terminalis.

Reaching the septal region (recommended consumer pattern — NOTE
the cross-container boundary)::

    # The septal region is a SECONDARY TERMINUS of stria terminalis
    # fibers — it is under the BASAL FOREBRAIN, not under the
    # extended amygdala:
    #
    #   subcortical.basal_forebrain.septal_nuclei
    #
    # Do NOT resolve the septal region through the stria terminalis.

Reaching the fornix (recommended consumer pattern — NOTE the
different tract and different container)::

    # The FORNIX is a DIFFERENT white-matter tract — the hippocampal
    # fiber pathway, under white_matter/:
    #
    #   white_matter.fornix
    #
    # The fornix is under `white_matter/`; the stria terminalis is
    # under `extended_amygdala/`. They are two different limbic
    # tracts with different origins (hippocampus vs. amygdala) and
    # different wiring conventions. Do NOT conflate them.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        st_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"extended_amygdala.stria_terminalis"
        )
        # resolve st_path through the memory/recall layer

References
----------
*   **Canonical stria terminalis anatomy:** Price, J.L., Russchen,
    F.T., Amaral, D.G. (1987). "The limbic region. II: The
    amygdaloid complex." In *Handbook of Chemical Neuroanatomy*
    (Björklund, A., Hökfelt, T., Swanson, L.W., eds.).
    (Definitive stria terminalis anatomy — origin, course,
    termination, and fiber composition.)
*   **Stria terminalis review:** de Olmos, J.S., Heimer, L. (1999).
    "The concepts of the ventral striatopallidal system and extended
    amygdala." *Annals of the New York Academy of Sciences*
    877:1–32. (Stria terminalis as the fiber pathway of the extended
    amygdala.)
*   **Extended amygdala anatomy:** Alheid, G.F., Heimer, L. (1988).
    "New perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (The **SLEA** classification — the stria terminalis as
    the fiber pathway of the extended amygdala continuum.)
*   **BNST anatomy:** Ju, G., Swanson, L.W. (1989). "Studies on the
    cellular architecture of the bed nuclei of the stria terminalis
    in the rat." *Journal of Comparative Neurology*
    280:587–602. (Definitive BNST anatomy — the terminus nucleus of
    the stria terminalis.)
*   **Amygdala-BNST pathway:** Davis, M., Walker, D.L., Miles, L.,
    Grillon, C. (2010). "Phasic vs sustained fear in rats and
    humans: role of the extended amygdala in fear vs anxiety."
    *Neuropsychopharmacology* 35:105–135. (The **amygdala-BNST**
    pathway — the stria terminalis as the fear-to-anxiety fiber
    pathway.)
*   **Stria terminalis and PTSD:** Avery, S.N., Clauss, J.A.,
    Blackford, J.U. (2016). "The human BNST: functional role in
    anxiety and addiction." *Neuropsychopharmacology* 41:126–141.
    (The stria terminalis-BNST pathway in PTSD and anxiety.)
*   **Fornix (contrast — different white-matter tract):**
    Nieuwenhuys, R., Voogd, J., van Huijzen, C. (2008). *The Human
    Central Nervous System*, 4th ed. (The fornix as the hippocampal
    fiber pathway — under ``white_matter/``, distinct from the
    stria terminalis.)
*   **White matter (contrast — wiring convention):** Schmahmann,
    J.D., Pandya, D.N. (2006). *Fiber Pathways of the Brain*.
    (White-matter tracts — the stria terminalis as a limbic tract
    wired under the extended amygdala, unlike the fornix under
    ``white_matter/``.)
*   **Central amygdaloid nucleus (contrast — source):** LeDoux,
    J.E. (2000). "Emotion circuits in the brain." *Annual Review
    of Neuroscience* 23:155–184. (Central amygdaloid nucleus as the
    fear-output structure — the **source** of stria terminalis
    fibers.)
*   **Medial amygdaloid nucleus (contrast — source):** Swanson,
    L.W., Petrovich, G.D. (1998). "What is the amygdala?" *Trends
    in Neurosciences* 21:323–331. (Medial amygdaloid nucleus as the
    olfactory-amygdala structure — the **source** of stria
    terminalis fibers.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association belongs to the **amygdala module** — **not** to the
    right stria terminalis, which is a **white-matter tract** with
    no SLEA relationship of its own.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Stria terminalis in overview.)
*   NeuroNames — Stria terminalis (right); FMA — Stria terminalis
    (right member).
"""