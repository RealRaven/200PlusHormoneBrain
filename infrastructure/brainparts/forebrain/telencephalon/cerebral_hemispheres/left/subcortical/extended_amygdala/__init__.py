"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.extended_amygdala
=========================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── extended_amygdala   <-- THIS MODULE
                    └── stria_terminalis
                        └── bed_nucleus_of_stria_terminalis

**Primary synonym:** Extended amygdala; extended amygdaloid complex;
extended amygdala continuum (in the SLEA framing).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**structural grouping** — the **classical extended amygdala**
(BNST + central amygdaloid nucleus) — with **one wired child**
(``stria_terminalis``) and **one grandchild**
(``bed_nucleus_of_stria_terminalis``).
**Part of:** The **subcortical** container — a **sibling** of
``basal_forebrain``, ``basal_ganglia``, ``claustrum``, and
``medial_temporal_lobe``.
**Structural parent:** ``.../left/subcortical/`` → **direct child** of
the subcortical container.
**Structural children (one, closed set):**
``stria_terminalis`` (→ ``bed_nucleus_of_stria_terminalis``).
**Boundary status (CLASSICAL EXTENDED AMYGDALA ANCHOR — split across
the tree):** **Boundary case — the extended amygdala is the ANCHOR of
the classical extended amygdala (BNST + central amygdaloid nucleus),
but the tree SPLITS the classical extended amygdala across TWO
containers:**
*   **BNST** → **here**, under
    ``extended_amygdala/stria_terminalis/bed_nucleus_of_stria_terminalis/``
*   **Central amygdaloid nucleus** →
    ``medial_temporal_lobe/amygdala/central_nucleus/`` — **NOT here**
The **classical extended amygdala** is the **BNST + central
amygdaloid nucleus** — a **limbic-forebrain continuum**. The tree
**splits** it: the **BNST** is under the **extended amygdala
container**, and the **central nucleus** is under the **amygdala**
container. **Consumers reconstructing the classical extended
amygdala** must **union** the two — the tree does **not** provide
this union as a single path. **This is the first container in the
tree whose primary structural fact is a SPLIT** — not a gap, not a
deferral, but a **deliberate two-container split** of a single
classical continuum.
**Boundary status (SLEA ANCHOR — the origin of the SLEA continuum):**
**Boundary case — the extended amygdala is the ANCHOR of the
sublenticular extended amygdala (SLEA) continuum.** The **SLEA
classification** (Alheid & Heimer, 1988) **extends** the classical
extended amygdala to include the **ventral pallidum** and the
**nucleus accumbens** — both **wired under the basal ganglia**, not
under the extended amygdala. The **SLEA continuum** is therefore
**four structures across THREE containers**:
*   **BNST** → **here**, under the **extended amygdala** container
    (the **anchor**)
*   **Central amygdaloid nucleus** →
    ``medial_temporal_lobe/amygdala/central_nucleus/``
*   **Ventral pallidum** →
    ``basal_ganglia/globus_pallidus/ventral_pallidum/``
*   **Nucleus accumbens** →
    ``basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/``
**Consumers reconstructing the FULL SLEA** must **union** all four —
the tree does **not** provide the union as a single path. **The
extended amygdala container is the SLEA ANCHOR** — the
classification's **origin**, not a peripheral member. **This is the
first module in the tree whose warning is an ANCHOR relationship** —
the anchor **unions** with the other SLEA components to reconstruct
the full continuum, rather than being "classified as SLEA but wired
elsewhere" (which is the pattern for the ventral pallidum and nucleus
accumbens).
**Boundary status (NOT a leaf — a two-level container):** **Boundary
case — the extended amygdala is a CONTAINER, not a leaf — it has a
two-level chain: `extended_amygdala/` → `stria_terminalis/` →
`bed_nucleus_of_stria_terminalis/`.** Consumers iterating the
extended amygdala must **recurse to two levels** to reach the
**BNST** leaf. The **stria terminalis** is a **white-matter tract**
wired as a **container** (with the BNST as its child) — a
**deliberate boundary choice** reflecting its role as the extended
amygdala's **fiber pathway** (see *The Stria Terminalis* below).
**Boundary status (the stria terminalis is a WHITE-MATTER TRACT
wired here, NOT under white_matter/):** **Boundary case — the stria
terminalis is a WHITE-MATTER TRACT, but it is wired under the
extended amygdala container, NOT under `white_matter/`.** The **stria
terminalis** is the **fiber bundle** carrying axons from the
**amygdala** (especially the **central nucleus** and **medial
nucleus**) to the **BNST** and the **septal region**. By strict
**tissue-type** convention, it would be under ``white_matter/`` —
but the tree places it **here**, under the extended amygdala,
because it is **the fiber pathway of the extended amygdala**. This
is a **deliberate boundary choice** — the stria terminalis is
**functionally part of** the extended amygdala, even though it is
**cytologically white matter**. Consumers must **not** resolve the
stria terminalis through ``white_matter/`` — it is **here**.
**Boundary status (the BNST is the main GREY-MATTER structure, NOT
the whole extended amygdala):** **Boundary case — the BNST is the
main GREY-MATTER structure of the extended amygdala container, but it
is NOT the whole extended amygdala.** The **BNST** is the **bed
nucleus of the stria terminalis** — the **grey-matter nucleus** at
the **terminus of the stria terminalis**. It is the **main wired
structure** of the extended amygdala container, and it is the
**classical** extended amygdala component **that is wired here**.
The **central amygdaloid nucleus** — the **other classical** extended
amygdala component — is **NOT here** (it is under the **amygdala**).
Consumers must **not** conflate the **BNST** (here) with the **whole
extended amygdala** — the **classical extended amygdala** is
**BNST + central nucleus**, and the **SLEA continuum** adds the
**ventral pallidum** and **nucleus accumbens**.
**Boundary status (NOT the amygdala — the amygdala is a sibling of
the subcortical container):** **Boundary case — the amygdala is a
SEPARATE container, a SIBLING of the subcortical container, not a
parent or child of the extended amygdala.** The **amygdala**
(``medial_temporal_lobe/amygdala/``) is the **medial temporal lobe
nuclear complex** — it contains the **central nucleus** (the
**other** classical extended amygdala component), the **basolateral
nuclei**, the **cortical nuclei**, and the **main olfactory system**
and **accessory olfactory system**. The **extended amygdala** is a
**separate container** under the subcortical container. The two are
**functionally coupled** (via the **stria terminalis** and the
**extended amygdala continuum**), but **structurally separate**.
Consumers must **not** resolve the extended amygdala through the
amygdala, or the amygdala through the extended amygdala.
**Boundary status (NOT the basal ganglia — the SLEA extensions are
siblings):** **Boundary case — the basal ganglia is a SIBLING of the
extended amygdala, not a parent or child.** The **SLEA extensions**
(the **ventral pallidum** and the **nucleus accumbens**) are
**wired under the basal ganglia**, not under the extended amygdala.
The **extended amygdala** and the **basal ganglia** are **siblings**
under the subcortical container. Consumers reconstructing the **full
SLEA** must **union** across the **extended amygdala** and the
**basal ganglia** — the tree does **not** provide the union as a
single path.
**Boundary status (function — the extended amygdala is the
STRESS/ANXIETY continuum, NOT the fear circuit):** **Boundary case —
the extended amygdala is the LIMBIC-FOREBRAIN CONTINUUM for stress,
anxiety, and autonomic regulation — NOT the fear-output circuit.**
The **BNST** (here) is the **stress/anxiety hub** — it is the
**primary substrate** of **sustained anxiety**, **stress responses**,
and **autonomic regulation**. The **central amygdaloid nucleus**
(under the amygdala) is the **fear-output** structure — the
**amygdala's "fear center."** The two are **functionally coupled**
(via the stria terminalis) but **functionally distinct** — the **BNST
is stress/anxiety**, the **central nucleus is fear**. Consumers must
**not** conflate the two — the **BNST** is **not** the **fear-output**
structure, and the **right-amygdala fear association** belongs to
the **amygdala module** (central nucleus), **not** to the **BNST**.

Overview
--------
The extended amygdala is the **anchor of the SLEA continuum** — the
**classical extended amygdala** (BNST + central amygdaloid nucleus)
**plus** the **SLEA extensions** (ventral pallidum + nucleus
accumbens). The **tree splits** this continuum across **three
containers**:
*   **BNST** — **here**, under the **extended amygdala** container
    (the **anchor**)
*   **Central amygdaloid nucleus** —
    ``medial_temporal_lobe/amygdala/central_nucleus/``
*   **Ventral pallidum** —
    ``basal_ganglia/globus_pallidus/ventral_pallidum/``
*   **Nucleus accumbens** —
    ``basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/``

**The extended amygdala container is the SLEA anchor** — the
**origin** of the classification, not a peripheral member. Its
**warning** is an **anchor** warning: **union with us**, not
**lateralize from us**. The **full SLEA** requires **union** across
all four structures.

**The extended amygdala container has ONE wired child (the stria
terminalis) and ONE grandchild (the BNST).** The **stria terminalis**
is a **white-matter tract** — the **fiber pathway** of the extended
amygdala — wired **here** (under the extended amygdala) rather than
under ``white_matter/``, because it is **functionally part of** the
extended amygdala. The **BNST** is the **grey-matter nucleus** —
the **stress/anxiety hub** — and is the **main structure** of the
container.

**The classical extended amygdala is BNST + central amygdaloid
nucleus.** The tree **splits** them: the **BNST** is here, and the
**central nucleus** is under the **amygdala**. **Consumers
reconstructing the classical extended amygdala** must **union** the
two — the tree does **not** provide this union as a single path.
**This is the first container in the tree whose primary structural
fact is a SPLIT** — not a gap, not a deferral, but a **deliberate
two-container split** of a single classical continuum.

**The extended amygdala is the stress/anxiety continuum, NOT the
fear-output circuit.** The **BNST** (here) is the **stress/anxiety
hub** — the **primary substrate** of **sustained anxiety**, **stress
responses**, and **autonomic regulation**. The **central amygdaloid
nucleus** (under the amygdala) is the **fear-output** structure. The
two are **functionally coupled** (via the stria terminalis) but
**functionally distinct** — **do not conflate them**.

**The extended amygdala is a paired structure.** Each hemisphere has
its own extended amygdala, with **ipsilateral** connections to its
own amygdala and basal ganglia. The two sides are **bilaterally
symmetric** and **functionally non-lateralized** — the **SLEA
continuum** is **broadly bilateral**. See *Lateralization Notes*.

Container Contents (one child, one grandchild, closed set)
----------------------------------------------------------
The extended amygdala container has **exactly one child** and **one
grandchild**:

*   **``stria_terminalis``** — the **stria terminalis** — a
    **white-matter tract** that is the **fiber pathway** of the
    extended amygdala. It is a **container** with **one child**:
    ``bed_nucleus_of_stria_terminalis``. **Depth: two levels** from
    the extended amygdala container.

*   **``bed_nucleus_of_stria_terminalis``** (the **BNST**) — the
    **grey-matter nucleus** at the terminus of the stria terminalis.
    It is the **main structure** of the extended amygdala container
    — the **stress/anxiety hub** — and the **classical** extended
    amygdala component **that is wired here**. **Depth: leaf (no
    children).**

**Not children (deliberately excluded):**
*   **Central amygdaloid nucleus** —
    ``medial_temporal_lobe/amygdala/central_nucleus/`` — the **other
    classical** extended amygdala component, **split** from the BNST
    by the tree.
*   **Ventral pallidum** —
    ``basal_ganglia/globus_pallidus/ventral_pallidum/`` — an **SLEA
    extension**, wired under the **basal ganglia**.
*   **Nucleus accumbens** —
    ``basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/`` —
    an **SLEA extension**, wired under the **basal ganglia**.
*   **Amygdala** — ``medial_temporal_lobe/amygdala/`` — a
    **sibling** of the subcortical container, not a child of the
    extended amygdala.

The Extended Amygdala / Amygdala Boundary
-----------------------------------------
This is the **most consequential split** in the extended amygdala
container:

*   **Extended amygdala** (this module) — the **BNST** (via the
    stria terminalis). **Stress/anxiety hub.**
*   **Amygdala** (``medial_temporal_lobe/amygdala/``) — the
    **central amygdaloid nucleus** (the **fear-output** structure),
    the **basolateral nuclei**, the **cortical nuclei**, and the
    **olfactory systems**.

**The classical extended amygdala is BNST + central nucleus.** The
tree **splits** them: the **BNST** is **here**, and the **central
nucleus** is under the **amygdala**. **Consumers reconstructing the
classical extended amygdala** must **union** the two — the tree does
**not** provide this union as a single path.

**The BNST is NOT the central nucleus.** The **BNST** is the
**stress/anxiety hub**; the **central nucleus** is the **fear-output**
structure. They are **functionally coupled** (via the stria
terminalis) but **functionally distinct** — **do not conflate them**.

The Extended Amygdala / Basal Ganglia Boundary
----------------------------------------------
This is the **SLEA extension** boundary:

*   **Extended amygdala** (this module) — the **BNST** (the **SLEA
    anchor**). **Stress/anxiety hub.**
*   **Basal ganglia** (``.../basal_ganglia/``) — the **ventral
    pallidum** (under the globus pallidus) and the **nucleus
    accumbens** (under the ventral striatum). **SLEA extensions.**

**The SLEA continuum is four structures across three containers.**
The **extended amygdala is the anchor**; the **ventral pallidum** and
**nucleus accumbens** are the **extensions**. **Consumers
reconstructing the full SLEA** must **union** all four — the tree
does **not** provide the union as a single path.

The Extended Amygdala / Medial Temporal Lobe Boundary
-----------------------------------------------------
This is the **classical partner** boundary:

*   **Extended amygdala** (this module) — the **BNST**.
*   **Medial temporal lobe** (``.../medial_temporal_lobe/``) — the
    **amygdala** (which contains the **central nucleus**), the
    **hippocampus**, and the **parahippocampal region**.

**The classical extended amygdala is BNST (here) + central nucleus
(under the medial temporal lobe).** **Consumers reconstructing the
classical extended amygdala** must **union** the two — the tree
does **not** provide the union as a single path.

The Stria Terminalis
---------------------
The **stria terminalis** is a **white-matter tract** — the **fiber
pathway** of the extended amygdala. It is **wired as a container**
under the extended amygdala, with the **BNST as its child** — a
**deliberate boundary choice** reflecting its role as the **extended
amygdala's fiber pathway**.

**The stria terminalis is NOT a pure white-matter tract** in the
strict sense — it is the **fiber bundle** carrying axons from the
**amygdala** (especially the **central nucleus** and **medial
nucleus**) to the **BNST** and the **septal region**. By strict
**tissue-type** convention, it would be under ``white_matter/`` —
but the tree places it **here**, under the extended amygdala, because
it is **functionally part of** the extended amygdala.

**Consumers must not resolve the stria terminalis through
``white_matter/``** — it is **here**, as a **container** of the
extended amygdala.

The BNST
--------
The **bed nucleus of the stria terminalis (BNST)** is the
**grey-matter nucleus** at the **terminus of the stria terminalis**
— the **main structure** of the extended amygdala container, and
the **stress/anxiety hub** of the limbic forebrain.

**The BNST is NOT the central amygdaloid nucleus.** The **BNST** is
the **stress/anxiety hub** — sustained anxiety, stress responses,
autonomic regulation. The **central nucleus** (under the **amygdala**)
is the **fear-output** structure. They are **functionally coupled**
(via the stria terminalis) but **functionally distinct** — **do not
conflate them**.

Function in the Human Brain
---------------------------
The extended amygdala's functions are **stress, anxiety, and
autonomic regulation** (via the BNST) — **NOT** the **fear-output**
functions of the **central amygdaloid nucleus** (under the amygdala):

*   **Sustained Anxiety (BNST Function):** The **BNST** is the
    **primary substrate** of **sustained anxiety** — the **diffuse,
    long-lasting** anxiety that follows **unpredictable threat**. It
    is **distinct** from the **phasic fear** mediated by the
    **central amygdaloid nucleus** (under the amygdala). The **BNST**
    is the **anxiety hub**; the **central nucleus** is the **fear
    hub**.

*   **Stress Response and Autonomic Regulation (BNST Function):**
    The **BNST** is a **key node** in the **stress-response
    circuit** — it projects to the **hypothalamus** (paraventricular
    nucleus) and the **brainstem** (parabrachial nucleus, solitary
    nucleus), driving **HPA axis activation**, **sympathetic
    activation**, and **autonomic regulation**. It is the
    **limbic-forebrain interface** for **stress**.

*   **Reward and Aversion (SLEA Function — with the Ventral Pallidum
    and Nucleus Accumbens):** The **SLEA continuum** (including the
    **ventral pallidum** and **nucleus accumbens** — **wired under
    the basal ganglia**) is involved in **reward and aversion** —
    the **BNST** and **central nucleus** (under the amygdala) are
    the **stress/anxiety** components; the **ventral pallidum** and
    **nucleus accumbens** are the **reward** components. The **SLEA
    is the integration hub** for **reward-aversion** and
    **stress-reward** interactions.

*   **NOT the fear-output circuit.** The **fear-output** structure
    is the **central amygdaloid nucleus** (under the **amygdala**)
    — **not** the BNST. The **BNST** is the **stress/anxiety hub**;
    the **central nucleus** is the **fear hub**. **Consumers must not
    conflate the two.**

*   **NOT a neural processor in the classical sense.** The **BNST**
    is a **GABAergic output nucleus** — it **gates** stress/anxiety
    behavior rather than **computing** it. Consumers must not treat
    the extended amygdala as a cortical processor.

**The unifying theme:** the extended amygdala is the **stress/anxiety
continuum** of the limbic forebrain — the **BNST** (here) is the
**stress/anxiety hub**, and the **central nucleus** (under the
amygdala) is the **fear-output** structure. The **SLEA extensions**
(ventral pallidum, nucleus accumbens) add the **reward** component.
**Consumers must not conflate the BNST with the central nucleus** —
they are **two distinct hubs** of the same continuum.

Associated Disorders
--------------------
Extended amygdala disorders are **stress, anxiety, and autonomic**:

*   **PTSD and Anxiety Disorders (BNST Dysfunction):** The **BNST**
    is **dysfunctional** in **PTSD**, **generalized anxiety
    disorder**, and **panic disorder** — its **sustained-anxiety**
    role makes it a **therapeutic target**. **BNST deep brain
    stimulation** has been investigated (preclinically and in early
    clinical trials) for **treatment-resistant anxiety**.

*   **Addiction and Stress-Reward Interactions (SLEA
    Dysfunction):** The **SLEA continuum** (including the BNST,
    central nucleus, ventral pallidum, and nucleus accumbens) is
    involved in **stress-induced relapse** and **addiction** — the
    **BNST** is a **key node** in **stress-induced drug-seeking**.
    **This is a continuum-level disorder**, not a BNST-specific
    syndrome.

*   **Autonomic Dysregulation (BNST Dysfunction):** The **BNST**
    projects to the **hypothalamus** and **brainstem** — its
    **dysfunction** can contribute to **autonomic dysregulation**
    (e.g., **hyperarousal** in **PTSD**, **autonomic instability**
    in **anxiety disorders**).

*   **No Named "Extended Amygdala Syndrome":** The extended amygdala
    is a **continuum**, not a **single clinical entity** — **no named
    syndrome** exists. Its clinical footprint is **continuum-level**
    (stress/anxiety, addiction, autonomic regulation) — **not
    structure-specific**.

**What is NOT here:** The extended amygdala is **not** the substrate
for **Kluver-Bucy syndrome** (that is the **amygdala** — central and
basolateral nuclei), **fear conditioning** (that is the **central
amygdaloid nucleus** — under the **amygdala**), **Urbach-Wiethe
disease** (that is the **amygdala**), or **Parkinson's disease**
(putamen), **Huntington's disease** (caudate), **addiction** alone
(the nucleus accumbens is the primary reward substrate — the BNST is
the **stress-induced relapse** node), or **Alzheimer's disease**
(nucleus basalis). Its clinical footprint is **stress/anxiety**
(PTSD, GAD, panic) and **stress-reward interactions** (addiction
relapse) — a **distinct category** from the **fear-output** footprint
of the central amygdaloid nucleus.

Lateralization Notes
--------------------
This is the **left** extended amygdala container. The extended
amygdala is **bilaterally symmetric** and **functionally
non-lateralized** — and it carries a **LIGHT warning** (the anchor
relationship):

*   **Bilateral Stress/Anxiety Functions:** Each BNST projects
    **ipsilaterally** to its hypothalamus and brainstem. The two sides
    are **functionally symmetric** for stress/anxiety and autonomic
    regulation. **PTSD** and **anxiety disorders** are
    **bilateral** in the extended amygdala.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the extended amygdala has **no documented strong
    left-lateralized or right-lateralized function**.

*   **LIGHT WARNING (ANCHOR — the right-amygdala fear association
    belongs to the amygdala module):** The **extended amygdala
    container** carries a **light warning**: the **BNST** (here) is
    **NOT the central amygdaloid nucleus** (under the amygdala). The
    **right-amygdala fear association** belongs to the **amygdala
    module** (central nucleus) and the **extended amygdala module**
    (via the classical extended amygdala), but **NOT** to the
    **BNST leaf**. **This is the anchor-level warning** — the
    extended amygdala **anchors** the SLEA continuum, and its
    **fear-output** component (the central nucleus) is **split off**
    under the **amygdala**. Consumers must **not** import the
    right-amygdala fear association into the **BNST** — the BNST is
    the **stress/anxiety hub**, **not** the **fear-output**
    structure.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** (central nucleus) and the **extended amygdala
    module** (via the **classical extended amygdala**), **not** to
    the **BNST**. The **BNST** is the **stress/anxiety hub** —
    **not the fear hub**. Consumers must **not** conflate the two.

**A consumer that assumes "left extended amygdala = right extended
amygdala" will be structurally and functionally correct** — the two
sides are **symmetric**, no **strong** lateralized syndrome has been
demonstrated. The extended amygdala container is a **strict-mirror
pair with a LIGHT warning** — the **anchor-level warning** that the
**right-amygdala fear association** belongs to the **amygdala module**
(central nucleus), **not** to the **BNST**.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../medial_temporal_lobe/``, ``.../basal_ganglia/``, or any
    other container. The extended amygdala's relationships to the
    amygdala, basal ganglia, and medial temporal lobe are documented
    as **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — one child, one grandchild, closed set.** The
    extended amygdala has **exactly one child**
    (``stria_terminalis``) and **one grandchild**
    (``bed_nucleus_of_stria_terminalis``). Consumers may iterate
    them, but should not assume any others exist.
*   **CLASSICAL EXTENDED AMYGDALA SPLIT.** The **BNST** is **here**;
    the **central amygdaloid nucleus** is under the **amygdala**
    (medial temporal lobe). **Consumers reconstructing the classical
    extended amygdala** must **union** the two — the tree does **not**
    provide the union as a single path.
*   **SLEA ANCHOR — the extended amygdala is the anchor of the SLEA
    continuum.** The **SLEA extensions** (ventral pallidum, nucleus
    accumbens) are wired under the **basal ganglia**. **Consumers
    reconstructing the FULL SLEA** must **union** the extended
    amygdala with the **amygdala** (central nucleus) and the **basal
    ganglia** (ventral pallidum, nucleus accumbens).
*   **THE STRIA TERMINALIS IS A WHITE-MATTER TRACT WIRED HERE.**
    By strict tissue-type convention, it would be under
    ``white_matter/`` — but the tree places it **here**, under the
    extended amygdala, because it is **functionally part of** the
    extended amygdala.
*   **THE BNST IS THE MAIN GREY-MATTER STRUCTURE.** The **BNST** is
    the **stress/anxiety hub**, **NOT** the **fear-output**
    structure (the central nucleus is the fear output — under the
    **amygdala**).
*   **NOT the amygdala — sibling of the subcortical container.** The
    amygdala is under ``medial_temporal_lobe/amygdala/`` — a
    **sibling** of the subcortical container, not a child of the
    extended amygdala.
*   **NOT the basal ganglia — the SLEA extensions are siblings.**
    The ventral pallidum and nucleus accumbens are **siblings** under
    the basal ganglia, not children of the extended amygdala.
*   **Function — stress/anxiety, NOT fear-output.** The BNST is the
    **stress/anxiety hub**; the central nucleus (under the amygdala)
    is the **fear-output** structure. **Do not conflate them.**
*   **No ``AREA_PATHS`` hop.** The extended amygdala is a local
    container under the subcortical container, not a cross-listed
    leaf.
*   **No nested cross-listing.** The extended amygdala has no nested
    dual-framing module. It is a single container.
*   **Structural parity with right extended amygdala — strict mirror
    with a LIGHT (anchor) warning.** Left and right extended amygdala
    modules are **structurally identical** — same one child, same one
    grandchild, same **classical extended amygdala split**, same
    **SLEA anchor**, same **light warning**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical import extended_amygdala

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "extended_amygdala"
    )

**Do not** assume the extended amygdala **contains** the **central
amygdaloid nucleus**. The central nucleus is under the **amygdala**
(``medial_temporal_lobe/amygdala/central_nucleus/``) — **not** here.
The tree **splits** the classical extended amygdala across **two
containers**.

**Do not** assume the extended amygdala **contains** the **ventral
pallidum** or the **nucleus accumbens**. Those are **SLEA
extensions**, wired under the **basal ganglia** — **not** here.

**Do not** resolve the **stria terminalis** through
``white_matter/``. It is a **white-matter tract** wired **here**,
under the extended amygdala, as a **container** of the extended
amygdala.

**Do not** conflate the **BNST** with the **central amygdaloid
nucleus**. The **BNST** (here) is the **stress/anxiety hub**; the
**central nucleus** (under the amygdala) is the **fear-output**
structure. They are **functionally coupled** but **functionally
distinct**.

**Do not** import the **right-amygdala fear association** into the
**BNST**. That association belongs to the **amygdala module**
(central nucleus) — **not** to the **BNST**. The **BNST** is the
**stress/anxiety hub**, **not** the **fear hub**.

Iterating the extended amygdala container's child and grandchild
(recommended consumer pattern)::

    EXTENDED_AMYGDALA_CHILDREN = (
        "stria_terminalis",   # child — container
    )
    EXTENDED_AMYGDALA_GRANDCHILDREN = {
        "stria_terminalis": (
            "bed_nucleus_of_stria_terminalis",   # grandchild — leaf
        ),
    }
    # Closed set. The extended amygdala has one child (stria
    # terminalis) and one grandchild (BNST).

Reconstructing the CLASSICAL extended amygdala (recommended consumer
pattern — the tree SPLITS it)::

    # The classical extended amygdala is BNST + central amygdaloid
    # nucleus. The tree SPLITS it across two containers:
    CLASSICAL_EXTENDED_AMYGDALA = {
        "subcortical.extended_amygdala.stria_terminalis."
        "bed_nucleus_of_stria_terminalis": (
            # BNST — THIS MODULE
        ),
        "subcortical.medial_temporal_lobe.amygdala.central_nucleus": (
            # Central amygdaloid nucleus — under the AMYGDALA
        ),
    }
    # The tree does NOT provide this union as a single path.

Reconstructing the FULL SLEA (recommended consumer pattern — the tree
SPLITS it across three containers)::

    # The SLEA continuum is four structures across three containers:
    FULL_SLEA = {
        "subcortical.extended_amygdala.stria_terminalis."
        "bed_nucleus_of_stria_terminalis": (
            # BNST — THIS MODULE (the ANCHOR)
        ),
        "subcortical.medial_temporal_lobe.amygdala.central_nucleus": (
            # Central amygdaloid nucleus — under the AMYGDALA
        ),
        "subcortical.basal_ganglia.globus_pallidus.ventral_pallidum": (
            # Ventral pallidum — under the BASAL GANGLIA
        ),
        "subcortical.basal_ganglia.striatum.ventral_striatum."
        "nucleus_accumbens": (
            # Nucleus accumbens — under the BASAL GANGLIA
        ),
    }
    # The tree does NOT provide this union as a single path.

Reaching the classical extended amygdala's central nucleus
(recommended consumer pattern — the SPLIT)::

    # The central amygdaloid nucleus is under the AMYGDALA, not
    # here:
    #
    #   subcortical.medial_temporal_lobe.amygdala.central_nucleus
    #
    # It is the FEAR-OUTPUT structure (not the stress/anxiety hub).

Reaching the SLEA extensions (recommended consumer pattern — the
SLEA union)::

    # The SLEA extensions are wired under the BASAL GANGLIA:
    #
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #
    # They are the REWARD components of the SLEA continuum.

Reaching the stria terminalis (recommended consumer pattern — NOTE
the white-matter wired here)::

    # The stria terminalis is a WHITE-MATTER TRACT wired HERE, under
    # the extended amygdala — not under white_matter/:
    #
    #   subcortical.extended_amygdala.stria_terminalis
    #
    # It is the FIBER PATHWAY of the extended amygdala.

Function distinction (stress vs. fear — the key split)::

    # The BNST (here) is the STRESS/ANXIETY hub.
    # The central amygdaloid nucleus (under the amygdala) is the
    # FEAR-OUTPUT structure.
    #
    # Do NOT conflate them — they are FUNCTIONALLY DISTINCT despite
    # being part of the same continuum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ea_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"extended_amygdala"
        )
        # resolve ea_path through the memory/recall layer

References
----------
*   **Canonical extended amygdala anatomy:** Alheid, G.F., Heimer, L.
    (1988). "New perspectives in basal forebrain organization of
    special relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (The **SLEA** classification — the extended amygdala
    continuum including the BNST, central nucleus, ventral pallidum,
    and nucleus accumbens.)
*   **Extended amygdala review:** de Olmos, J.S., Heimer, L. (1999).
    "The concepts of the ventral striatopallidal system and extended
    amygdala." *Annals of the New York Academy of Sciences*
    877:1–32. (Extended amygdala anatomy and continuum.)
*   **BNST stress/anxiety:** Davis, M., Walker, D.L., Miles, L.,
    Grillon, C. (2010). "Phasic vs sustained fear in rats and
    humans: role of the extended amygdala in fear vs anxiety."
    *Neuropsychopharmacology* 35:105–135. (The **BNST** as the
    **sustained anxiety** hub; the **central nucleus** as the
    **phasic fear** hub — the key functional distinction.)
*   **BNST anatomy:** Ju, G., Swanson, L.W. (1989). "Studies on the
    cellular architecture of the bed nuclei of the stria terminalis
    in the rat." *Journal of Comparative Neurology*
    280:587–602. (Definitive BNST anatomy.)
*   **Stria terminalis:** Price, J.L., Russchen, F.T., Amaral, D.G.
    (1987). "The limbic region. II: The amygdaloid complex." In
    *Handbook of Chemical Neuroanatomy* (Björklund, A., Hökfelt, T.,
    Swanson, L.W., eds.). (Stria terminalis as the fiber pathway of
    the extended amygdala.)
*   **PTSD and BNST:** Avery, S.N., Clauss, J.A., Blackford, J.U.
    (2016). "The human BNST: functional role in anxiety and
    addiction." *Neuropsychopharmacology* 41:126–141. (BNST in PTSD,
    anxiety, and addiction.)
*   **BNST DBS for anxiety (preclinical/early clinical):** Langevin,
    J.P., et al. (2015). "Deep brain stimulation of the basolateral
    amygdala for treatment-refractory posttraumatic stress
    disorder." *Biological Psychiatry* 81:886–897. (DBS of the
    extended amygdala region for treatment-resistant PTSD — early
    clinical evidence.)
*   **Stress-induced relapse:** Shaham, Y., Shalev, U., Lu, L., de
    Wit, H., Stewart, J. (2003). "The reinstatement model of drug
    relapse: history, methodology and major findings."
    *Psychopharmacology* 168:3–20. (BNST in stress-induced
    drug-seeking relapse.)
*   **Classical extended amygdala (central nucleus — contrast):**
    LeDoux, J.E. (2000). "Emotion circuits in the brain." *Annual
    Review of Neuroscience* 23:155–184. (Central amygdaloid nucleus
    as the fear-output structure — under the **amygdala**, not the
    extended amygdala container.)
*   **SLEA extensions (contrast — ventral pallidum and nucleus
    accumbens):** Heimer, L., de Olmos, J., Alheid, G.F., Záborszky,
    L. (1999). "The human basal forebrain: an overview." In *The
    Human Nervous System* (Paxinos, G., ed.), 2nd ed. (Ventral
    pallidum and nucleus accumbens as SLEA components — under the
    basal ganglia.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association belongs to the **amygdala module** (central
    nucleus) — **not** to the **BNST** or the extended amygdala
    container.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Extended amygdala in overview.)
*   NeuroNames — Extended amygdala (left); FMA — Extended amygdala
    (left member).
"""