"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis
========================================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── extended_amygdala
                    └── stria_terminalis
                        └── bed_nucleus_of_stria_terminalis   <-- THIS MODULE

**Primary synonym:** Bed nucleus of the stria terminalis (BNST); bed
nucleus of the terminal stria; nucleus of the stria terminalis;
"the bed nucleus."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**heterogeneous grey-matter nucleus** — the **stress/anxiety hub**
of the limbic forebrain, and the **terminus nucleus** of the stria
terminalis.
**Part of:** The **extended amygdala** container — specifically, the
**main grey-matter structure** of the extended amygdala. Its
**parent** is the **stria terminalis** (the **white-matter tract**).
**Structural parent:** ``.../right/subcortical/extended_amygdala/stria_terminalis/``
→ **only child** of the stria terminalis container.
**Structural children:** **None.** This is a **leaf** module. The
**BNST subdivisions** (medial, lateral, ventral, oval, juxtacapsular,
etc.) and the **SLEA compartments** are documented as **prose**, not
as structural children.
**Boundary status (TERMINUS NUCLEUS — the GREY-MATTER structure at the
TERMINUS of the stria terminalis):** **Boundary case — the BNST is
the GREY-MATTER NUCLEUS at the TERMINUS of the stria terminalis.**
Its name is **literally descriptive**: "**bed nucleus of the stria
terminalis**" means "the **nucleus at the bed (terminus) of the stria
terminalis**." The **stria terminalis** (the **white-matter tract**)
is the **parent**; the **BNST** (the **grey-matter nucleus**) is the
**child** — a **unique parent-child relationship** in the tree: a
**fiber tract as parent**, a **nucleus as child**. **The BNST is
NOT the stria terminalis** — the tract is the **fiber pathway**, and
the BNST is the **grey-matter structure at its terminus**. Consumers
must **not** resolve the BNST through the stria terminalis, or the
stria terminalis through the BNST — they are **separate structures**
(a tract and a nucleus) that are **structurally coupled** by the
**terminus nucleus** pattern.
**Boundary status (the main GREY-MATTER structure of the extended
amygdala — NOT the whole extended amygdala):** **Boundary case —
the BNST is the MAIN GREY-MATTER STRUCTURE of the extended amygdala
container, but it is NOT the whole extended amygdala.** The **BNST**
is the **largest** and **most studied** grey-matter structure of
the extended amygdala container — it is the **stress/anxiety hub**.
But the **extended amygdala** is a **continuum** that includes:
*   The **BNST** (here) — the **stress/anxiety hub**
*   The **central amygdaloid nucleus** —
    ``medial_temporal_lobe/amygdala/central_nucleus/`` — the
    **fear-output** structure
*   The **ventral pallidum** —
    ``basal_ganglia/globus_pallidus/ventral_pallidum/`` — an **SLEA
    extension**
*   The **nucleus accumbens** —
    ``basal_ganglia/striatum/ventral_striatum/nucleus_accumbens/`` —
    an **SLEA extension**
Consumers must **not** conflate the **BNST** (here) with the **whole
extended amygdala** — the **BNST** is **one component** of the
continuum, the **stress/anxiety hub**. The **full continuum** is
**four structures across three containers** — see the **SLEA union
pattern** below.
**Boundary status (CLASSICAL EXTENDED AMYGDALA SPLIT — the BNST is
ONE HALF of the classical extended amygdala):** **Boundary case —
the BNST is ONE HALF of the CLASSICAL extended amygdala; the CENTRAL
AMYGDLOID NUCLEUS is the OTHER HALF, and it is under the AMYGDALA,
not here.** The **classical extended amygdala** is the **BNST**
(here) + the **central amygdaloid nucleus**
(``medial_temporal_lobe/amygdala/central_nucleus/``). The tree
**splits** them across **two containers**. **Consumers reconstructing
the classical extended amygdala** must **union** the two — the tree
does **not** provide the union as a single path. **The BNST is NOT
the central nucleus** — the **BNST** is the **stress/anxiety hub**;
the **central nucleus** is the **fear-output** structure. They are
**functionally coupled** (via the stria terminalis) but
**functionally distinct** — **do not conflate them**.
**Boundary status (FULL SLEA WARNING — the leaf that completes the
SLEA anchor's warning):** **Boundary case — the BNST is the SLEA
ANCHOR STRUCTURE, and THIS is the module that carries the FULL
leaf-level SLEA warning.** The **extended amygdala container** carried
the warning *lightly* (the anchor relationship); the **stria
terminalis** carried *no warning* (it is a **white-matter tract**);
**this leaf** carries the warning **fully** — because the **BNST
itself** is the **grey-matter structure that anchors** the SLEA
continuum, and it is the **structure that actually belongs to** the
extended amygdala continuum. Consumers must **not** import
**right-amygdala lateralization** claims into the BNST — the BNST
is **NOT the amygdala**, **NOT adjacent** to the amygdala, and
**NOT lateralized**. The **full SLEA warning** applies here: the
extended amygdala continuum is **broadly bilateral** and **not
lateralized**, and the **right amygdala's fear association** belongs
to the **amygdala module** and the **extended amygdala module**,
**NOT** to the BNST. See *Lateralization Notes*. **This is the
input-side complement of the ventral pallidum leaf** — together they
are the **two halves of the SLEA pair's grey-matter structures**.
**The right-side module carries the full SLEA warning explicitly** —
matching the right nucleus basalis, right substantia innominata,
right ventral pallidum, and right nucleus accumbens pattern —
because the right BNST is the **SLEA anchor grey-matter leaf** that
carries the right-amygdala association temptation via the SLEA
classification.
**Boundary status (NOT a single functional system — the BNST has
MULTIPLE subdivisions and functions):** **Boundary case — the BNST is
a HETEROGENEOUS nucleus with MULTIPLE subdivisions and MULTIPLE
functions, not a single functional system.** The **BNST** contains
**several subdivisions** — the **medial**, **lateral**, **ventral**,
**oval**, **juxtacapsular**, and **rhomboid** nuclei — each with
**different connections** and **different functions**:
*   **Medial BNST** — **autonomic and neuroendocrine** regulation
    (HPA axis, sympathetic activation) — the **stress-response**
    subdivision.
*   **Lateral BNST** — **reward and reinforcement** (dopaminergic
    input from the VTA) — the **reward-related** subdivision.
*   **Ventral BNST** — **sustained anxiety** (the **"anxiety
    subdivision"**) — the **primary substrate** of **diffuse,
    long-lasting anxiety**.
*   **Oval BNST** — **stress-induced relapse** (the **"relapse
    subdivision"**) — the **substrate** of **stress-induced
    drug-seeking**.
**These subdivisions are prose, not structural children.** The tree
wires the BNST as a **single leaf** — the subdivisions are **prose**,
reflecting the **anatomical continuity** of the BNST. Consumers that
need subdivision-level resolution should consult the references, not
the tree. **The ventral BNST is the more clinically important
subdivision** — it is the **primary substrate** of **sustained
anxiety** and **stress-induced relapse**.
**Boundary status (function — the STRESS/ANXIETY hub, NOT the
fear-output structure):** **Boundary case — the BNST is the
STRESS/ANXIETY HUB, NOT the fear-output structure.** The **BNST** is
the **primary substrate** of **sustained anxiety** — the **diffuse,
long-lasting** anxiety that follows **unpredictable threat** — and
of **autonomic regulation** (HPA axis, sympathetic activation). The
**central amygdaloid nucleus** (under the amygdala) is the
**fear-output** structure — the **phasic fear** hub. The two are
**functionally coupled** (via the stria terminalis) but
**functionally distinct** — **do not conflate them**. Consumers must
**not** treat the BNST as a **fear-output** structure or as a
**substrate for fear conditioning** — the **fear conditioning**
substrate is the **central nucleus** and the **basolateral nuclei**
(under the **amygdala**).

Overview
--------
The BNST is the **grey-matter nucleus** at the **terminus of the
stria terminalis** — the **stress/anxiety hub** of the limbic
forebrain, and the **main structure** of the extended amygdala
container. It is the **terminus nucleus** of the stria terminalis
(a **unique parent-child relationship** in the tree: a **fiber tract
as parent**, a **nucleus as child**), and it is the **SLEA anchor**
structure — the **grey-matter counterpart** of the extended amygdala's
SLEA anchor role.

**The BNST is the "stress/anxiety hub."** Its **primary function** is
**sustained anxiety** — the **diffuse, long-lasting** anxiety that
follows **unpredictable threat** — and **autonomic regulation** (HPA
axis, sympathetic activation). It is **functionally distinct** from
the **central amygdaloid nucleus** (under the amygdala) — the
**fear-output** structure that mediates **phasic fear** and **fear
conditioning**. **The BNST is the anxiety hub; the central nucleus is
the fear hub** — do not conflate them.

**The BNST is ONE HALF of the classical extended amygdala.** The
**classical extended amygdala** is the **BNST** (here) + the
**central amygdaloid nucleus** (under the **amygdala**). The tree
**splits** them — the BNST is here, and the central nucleus is under
the **medial temporal lobe**. **Consumers reconstructing the
classical extended amygdala** must **union** the two — the tree does
**not** provide the union as a single path.

**The BNST is the SLEA ANCHOR STRUCTURE.** The **SLEA continuum** is
**four structures across three containers**:
*   **BNST** (here) — the **anchor**
*   **Central amygdaloid nucleus** — under the **amygdala**
*   **Ventral pallidum** — under the **basal ganglia**
*   **Nucleus accumbens** — under the **basal ganglia**
**The BNST is the anchor** — the **classification's origin**, not a
peripheral member. **Consumers reconstructing the FULL SLEA** must
**union** all four — the tree does **not** provide the union as a
single path.

**The BNST is a paired structure.** Each hemisphere has its own BNST,
with **ipsilateral** connections to its own amygdala, hypothalamus,
and brainstem. The two sides are **bilaterally symmetric** and
**functionally non-lateralized** — the **stress/anxiety** and
**autonomic regulation** functions are **bilateral**. See
*Lateralization Notes*.

Subdivisions (prose, not structural children)
---------------------------------------------
The BNST is **heterogeneous** — it contains **several subdivisions**,
all documented as **prose**:

*   **Medial BNST** — **autonomic and neuroendocrine** regulation
    (HPA axis, sympathetic activation) — the **stress-response**
    subdivision. Receives input from the **medial amygdaloid
    nucleus** and the **hypothalamus**; projects to the
    **paraventricular nucleus** (HPA axis) and the **brainstem**
    (autonomic nuclei).

*   **Lateral BNST** — **reward and reinforcement** (dopaminergic
    input from the **VTA**) — the **reward-related** subdivision.
    Part of the **SLEA reward continuum** (with the **ventral
    pallidum** and the **nucleus accumbens**).

*   **Ventral BNST** — **sustained anxiety** (the **"anxiety
    subdivision"**) — the **primary substrate** of **diffuse,
    long-lasting anxiety**. Receives input from the **amygdala**
    (central nucleus) and the **infralimbic cortex**; projects to
    the **lateral hypothalamus** and the **brainstem**.

*   **Oval BNST** — **stress-induced relapse** (the **"relapse
    subdivision"**) — the **substrate** of **stress-induced
    drug-seeking**. Part of the **SLEA stress-reward** interaction
    (with the **nucleus accumbens** and the **ventral pallidum**).

*   **Juxtacapsular BNST** — **autonomic** and **neuroendocrine**
    regulation (with the medial BNST).

*   **Rhomboid BNST** — **autonomic** regulation (with the medial
    BNST).

**These subdivisions are prose, not structural children.** The tree
wires the BNST as a **single leaf** — the subdivisions are **prose**,
reflecting the **anatomical continuity** of the BNST. Consumers that
need subdivision-level resolution should consult the references, not
the tree. **The ventral BNST is the more clinically important
subdivision** — it is the **primary substrate** of **sustained
anxiety** and **stress-induced relapse**.

Function in the Human Brain
---------------------------
The BNST's functions are **sustained anxiety, autonomic regulation,
and stress-reward interactions** — **NOT** the **fear-output**
functions of the **central amygdaloid nucleus**:

*   **Sustained Anxiety (Primary Function):** The **BNST** is the
    **primary substrate** of **sustained anxiety** — the **diffuse,
    long-lasting** anxiety that follows **unpredictable threat**. It
    is **distinct** from the **phasic fear** mediated by the
    **central amygdaloid nucleus** (under the amygdala). The **BNST**
    is the **anxiety hub**; the **central nucleus** is the **fear
    hub**.

*   **Autonomic Regulation (BNST Function):** The **BNST** projects
    to the **hypothalamus** (paraventricular nucleus) and the
    **brainstem** (parabrachial nucleus, solitary nucleus) — driving
    **HPA axis activation**, **sympathetic activation**, and
    **autonomic regulation**. It is the **limbic-forebrain
    interface** for **stress**.

*   **Stress-Induced Relapse (BNST Function):** The **BNST** (especially
    the **oval subdivision**) is a **key node** in **stress-induced
    drug-seeking** and **relapse** — the **SLEA stress-reward**
    interaction (with the **nucleus accumbens** and the **ventral
    pallidum**) is the **anatomical substrate** of **stress-induced
    relapse**.

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
    the BNST as a cortical processor.

**The unifying theme:** the BNST is the **stress/anxiety hub** of the
limbic forebrain — the **sustained anxiety**, **autonomic
regulation**, and **stress-induced relapse** hub. It is **one half**
of the **classical extended amygdala** (with the central nucleus
under the amygdala), and it is the **SLEA anchor** structure. **The
BNST is NOT the fear-output structure** — the central nucleus is.
**Do not conflate them.**

Associated Disorders
--------------------
BNST disorders are **stress, anxiety, and autonomic**:

*   **PTSD and Anxiety Disorders (Signature Disorders):** The **BNST**
    is **dysfunctional** in **PTSD**, **generalized anxiety
    disorder**, and **panic disorder** — its **sustained-anxiety**
    role makes it a **therapeutic target**. **BNST deep brain
    stimulation** has been investigated (preclinically and in early
    clinical trials) for **treatment-resistant anxiety**. **This is
    the BNST's signature clinical association** — more than any other
    structure, the BNST is **defined clinically by its role in
    stress/anxiety disorders**.

*   **Stress-Induced Relapse (BNST Dysfunction):** The **BNST**
    (especially the **oval subdivision**) is a **key node** in
    **stress-induced drug-seeking** and **relapse** — it is the
    **SLEA stress-reward** interface. **This is a continuum-level
    disorder**, not a BNST-specific syndrome — but the BNST is the
    **stress-relapse** node.

*   **Autonomic Dysregulation (BNST Dysfunction):** The **BNST**
    projects to the **hypothalamus** and **brainstem** — its
    **dysfunction** can contribute to **autonomic dysregulation**
    (e.g., **hyperarousal** in **PTSD**, **autonomic instability**
    in **anxiety disorders**).

*   **No Named "BNST Syndrome":** The BNST is **one component** of the
    extended amygdala continuum — **no named "BNST syndrome" exists**.
    Its clinical footprint is **continuum-level** (stress/anxiety,
    stress-induced relapse, autonomic regulation) — **not
    structure-specific**.

**What is NOT here:** The BNST is **not** the substrate for
**Kluver-Bucy syndrome** (that is the **amygdala** — central and
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
This is the **right** BNST module. The BNST is **bilaterally
symmetric** and **functionally non-lateralized** — and it carries the
**FULL SLEA warning** at the leaf level:

*   **Bilateral Stress/Anxiety Functions:** Each BNST projects
    **ipsilaterally** to its hypothalamus and brainstem. The two sides
    are **functionally symmetric** for stress/anxiety and autonomic
    regulation. **PTSD** and **anxiety disorders** are
    **bilateral** in the BNST.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the BNST has **no documented strong
    left-lateralized or right-lateralized function**.

*   **FULL SLEA WARNING (the leaf that completes the SLEA anchor's
    warning):** The BNST **itself** is the **SLEA anchor structure**
    — **this is the grey-matter structure that carries the full
    SLEA warning** at the leaf level, completing the warning gradient
    from the **extended amygdala container** (light) → the **stria
    terminalis** (none — it is a white-matter tract) → **this leaf**
    (full). The warning is:
    - The BNST is **not the amygdala**.
    - It is **not adjacent** to the amygdala.
    - It is **not lateralized**.
    - The **SLEA continuum** is **broadly bilateral**.
    - The **right amygdala's fear-processing association** belongs to
      the **amygdala module** (central nucleus) and the **extended
      amygdala module** — **not** to the BNST.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** (central nucleus) and (via the classical
    extended amygdala) to the **extended amygdala module** — **not**
    to the **BNST**. **The BNST is the stress/anxiety hub** — **not
    the fear hub**. **This is the most important right-side warning
    in the extended amygdala subtree**: the **right BNST** is the
    **SLEA anchor grey-matter leaf**, and a consumer reading the
    right-side module is **exactly** the consumer most likely to
    attribute the right amygdala's fear-processing association to the
    right BNST. **Do not.** The right BNST is **not** the right
    central amygdaloid nucleus, and the right amygdala's
    fear-processing association **does not** transfer here. The
    warning is **full at this leaf level** — matching the **right
    nucleus basalis**, **right substantia innominata**, **right
    ventral pallidum**, and **right nucleus accumbens** patterns.
    **The right-side module carries the full SLEA warning
    explicitly** — a **light** Usage warning and a contrast
    reference.

**A consumer that assumes "right BNST = left BNST" will be
structurally and functionally correct** — the two sides are
**symmetric**, no **strong** lateralized syndrome has been
demonstrated, and the **FULL SLEA warning** is stated here at the
leaf level. This is a **strict-mirror pair with a full
(light-moderate) warning** — matching the **nucleus basalis**,
**substantia innominata**, **ventral pallidum**, and **nucleus
accumbens** pattern (light warning: Lateralization note + light Usage
warning, **not** the emphatic "Do not import" Usage block of the
periamygdaloid/uncus/subcortical group). The warning is **full** in
the sense of being **the complete SLEA statement at the leaf level**,
but it is **light-moderate** in strength — the BNST is **not
adjacent** to the amygdala, and the SLEA link is **classificatory**,
not **projectional** or **adjacent**. **The right-side module
carries the full SLEA warning explicitly** — matching the right
nucleus basalis, right substantia innominata, right ventral pallidum,
and right nucleus accumbens — because the right BNST is the
**SLEA anchor grey-matter leaf** that carries the right-amygdala
association temptation via the SLEA classification.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../medial_temporal_lobe/``, ``.../basal_ganglia/``, or any
    other container. The BNST's relationships to the amygdala,
    central nucleus, ventral pallidum, and nucleus accumbens are
    documented as **prose and boundary data**, not as structural
    parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **BNST
    subdivisions** (medial, lateral, ventral, oval, juxtacapsular,
    rhomboid) and the **SLEA compartments** are documented as
    **prose**, not as sub-modules. Consumers must not assume any
    exist as children; resolve subdivision-level detail through the
    references.
*   **TERMINUS NUCLEUS — the grey-matter structure at the terminus of
    the stria terminalis.** The BNST is the **child of the stria
    terminalis** — a **unique parent-child relationship** in the
    tree (a **fiber tract as parent**, a **nucleus as child**).
    Consumers must **not** resolve the BNST through the stria
    terminalis, or the stria terminalis through the BNST.
*   **FULL SLEA WARNING — the SLEA anchor's grey-matter leaf.**
    The **extended amygdala container** carried the warning *lightly*
    (the anchor relationship); the **stria terminalis** carried *no
    warning* (it is a **white-matter tract**); **this leaf** carries
    the warning **fully** — because the **BNST itself** is the
    **grey-matter structure that anchors** the SLEA continuum. The
    BNST is **not the amygdala**, **not adjacent** to it, and **not
    lateralized**. The **right-amygdala fear association** belongs to
    the **amygdala module** (central nucleus) and the **extended
    amygdala module**, **not** here. **The right-side module carries
    the full SLEA warning explicitly** — a light Usage warning and a
    contrast reference — matching the right nucleus basalis, right
    substantia innominata, right ventral pallidum, and right nucleus
    accumbens pattern.
*   **CLASSICAL EXTENDED AMYGDALA SPLIT — the BNST is ONE HALF.**
    The **central amygdaloid nucleus** is the **other half**, under
    the **amygdala**. Consumers reconstructing the **classical
    extended amygdala** must **union** the two — the tree does **not**
    provide the union as a single path.
*   **NOT a single functional system — the BNST has MULTIPLE
    subdivisions.** The **medial**, **lateral**, **ventral**,
    **oval**, **juxtacapsular**, and **rhomboid** subdivisions are
    **prose**, not structural children. The **ventral BNST** is the
    more clinically important subdivision (sustained anxiety).
*   **Function — the STRESS/ANXIETY hub, NOT the fear-output
    structure.** The **BNST** is the **sustained anxiety** and
    **autonomic regulation** hub; the **central amygdaloid nucleus**
    (under the **amygdala**) is the **fear-output** structure. **Do
    not conflate them.** **The right-side module keeps the warning
    full** — the right BNST is the **SLEA anchor grey-matter leaf**,
    and the right-amygdala fear association belongs to the **amygdala
    module** (central nucleus) and the **extended amygdala module**,
    **not** here.
*   **No ``AREA_PATHS`` hop.** The BNST is a local leaf under the
    stria terminalis, not a cross-listed leaf.
*   **No nested cross-listing.** The BNST has no nested dual-framing
    module. It is a single leaf.
*   **Structural parity with left BNST — strict mirror with a full
    (light-moderate) warning.** Right and left BNST modules are
    **structurally identical** — same leaf status, same subdivisions
    as prose, same SLEA warning (full at the leaf level), same
    **stress/anxiety** signature disorders, same
    **classical-extended-amygdala split** note, same **non-lateralized**
    caveat. **The right-side module carries the full SLEA warning
    explicitly** — a light Usage warning and a contrast reference —
    matching the right nucleus basalis, right substantia innominata,
    right ventral pallidum, and right nucleus accumbens pattern.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.extended_amygdala.stria_terminalis import bed_nucleus_of_stria_terminalis

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "extended_amygdala.stria_terminalis.bed_nucleus_of_stria_terminalis"
    )

**Do not** assume the BNST is the **stria terminalis**. The **stria
terminalis** is the **white-matter tract** (the **parent**); the
**BNST** is the **grey-matter nucleus** at its **terminus** (the
**child**). They are **separate structures** (a tract and a nucleus)
that are **structurally coupled** by the **terminus nucleus** pattern.

**Do not** assume the BNST is the **central amygdaloid nucleus**. The
**central nucleus** is under the **amygdala**
(``medial_temporal_lobe/amygdala/central_nucleus/``) — **not** here.
The tree **splits** the classical extended amygdala across **two
containers** — the **BNST** is here, and the **central nucleus** is
under the **amygdala**.

**Do not** assume the BNST is the **amygdala**. The BNST is a
**grey-matter nucleus** in the extended amygdala container; the
amygdala is a **separate container** under the medial temporal lobe.

**Do not** assume the BNST is the **whole extended amygdala**. The
BNST is the **main grey-matter structure** of the extended amygdala
container, but the **extended amygdala** is a **continuum** that
includes the **central amygdaloid nucleus** (under the amygdala), the
**ventral pallidum**, and the **nucleus accumbens** (both under the
basal ganglia).

**Do not** import **right-amygdala lateralization claims** into the
right BNST. **The BNST is the SLEA anchor structure**, but it is
**not the amygdala**, **not adjacent** to it, and **not lateralized**.
**This is the FULL SLEA warning** — the grey-matter leaf that
completes the SLEA anchor's warning (extended amygdala container:
light → stria terminalis: none → **BNST: full**). **This is the most
important right-side warning in the extended amygdala subtree** — the
right BNST is the **SLEA anchor grey-matter leaf**, and a consumer
reading the right-side module is **exactly** the consumer most likely
to attribute the right amygdala's fear-processing association to the
right BNST. **Do not.** The right BNST is **not** the right central
amygdaloid nucleus, and the right amygdala's fear-processing
association **does not** transfer here.

**Do not** assume the BNST is a **single functional system**. Its
**medial**, **lateral**, **ventral**, **oval**, **juxtacapsular**, and
**rhomboid** subdivisions are **functionally distinct** — the
**ventral BNST** is the **sustained anxiety** subdivision.

**Do not** conflate the BNST's **stress/anxiety** function with the
central nucleus's **fear-output** function. The **BNST** is the
**sustained anxiety hub**; the **central nucleus** is the **phasic
fear hub**. They are **functionally distinct**.

Iterating the BNST's (empty) children (recommended consumer
pattern)::

    BNST_CHILDREN = ()
    # The BNST is a leaf. Medial, lateral, ventral, oval,
    # juxtacapsular, and rhomboid subdivisions are prose, not modules.

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

Reaching the stria terminalis (recommended consumer pattern — the
parent)::

    # The stria terminalis is the PARENT of the BNST — the white-
    # matter tract whose terminus the BNST is:
    #
    #   subcortical.extended_amygdala.stria_terminalis
    #
    # The stria terminalis is the TRACT; the BNST is the NUCLEUS at
    # its terminus.

Reaching the central amygdaloid nucleus (recommended consumer pattern
— the SPLIT)::

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

Function distinction (stress vs. fear — the key split)::

    # The BNST (here) is the STRESS/ANXIETY hub.
    # The central amygdaloid nucleus (under the amygdala) is the
    # FEAR-OUTPUT structure.
    #
    # Do NOT conflate them — they are FUNCTIONALLY DISTINCT despite
    # being part of the same continuum.

Subdivision-level detail (not wired — consult references)::

    # The BNST's subdivisions are prose, not modules:
    #   medial        -> autonomic/neuroendocrine (HPA axis)
    #   lateral       -> reward/reinforcement (VTA input)
    #   ventral       -> sustained anxiety (the "anxiety subdivision")
    #   oval          -> stress-induced relapse (the "relapse
    #                    subdivision")
    #   juxtacapsular -> autonomic/neuroendocrine
    #   rhomboid      -> autonomic
    #
    # Do not attempt to resolve these as sub-paths of the BNST.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        bnst_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"extended_amygdala.stria_terminalis."
            f"bed_nucleus_of_stria_terminalis"
        )
        # resolve bnst_path through the memory/recall layer

References
----------
*   **Canonical BNST anatomy:** Ju, G., Swanson, L.W. (1989). "Studies
    on the cellular architecture of the bed nuclei of the stria
    terminalis in the rat." *Journal of Comparative Neurology*
    280:587–602. (Definitive BNST anatomy; medial, lateral, ventral,
    oval, juxtacapsular, and rhomboid subdivisions.)
*   **BNST stress/anxiety:** Davis, M., Walker, D.L., Miles, L.,
    Grillon, C. (2010). "Phasic vs sustained fear in rats and
    humans: role of the extended amygdala in fear vs anxiety."
    *Neuropsychopharmacology* 35:105–135. (The **BNST** as the
    **sustained anxiety** hub; the **central nucleus** as the
    **phasic fear** hub — the key functional distinction.)
*   **Extended amygdala anatomy:** Alheid, G.F., Heimer, L. (1988).
    "New perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (The **SLEA** classification — the extended amygdala
    continuum including the BNST, central nucleus, ventral pallidum,
    and nucleus accumbens.)
*   **Extended amygdala review:** de Olmos, J.S., Heimer, L. (1999).
    "The concepts of the ventral striatopallidal system and extended
    amygdala." *Annals of the New York Academy of Sciences*
    877:1–32. (Extended amygdala anatomy and continuum.)
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
    *Psychopharmacology* 168:3–20. (BNST — especially the oval
    subdivision — in stress-induced drug-seeking relapse.)
*   **BNST subdivisions:** Dong, H.W., Petrovich, G.D., Swanson, L.W.
    (2001). "Topography of projections from amygdala to bed nuclei
    of the stria terminalis." *Brain Research Reviews* 38:192–246.
    (Definitive BNST subdivisions and their connections.)
*   **Central amygdaloid nucleus (contrast — fear-output):** LeDoux,
    J.E. (2000). "Emotion circuits in the brain." *Annual Review of
    Neuroscience* 23:155–184. (Central amygdaloid nucleus as the
    fear-output structure — under the **amygdala**, not the BNST.)
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
    association belongs to the **amygdala module** (central nucleus)
    — **not** to the **right BNST** or the extended amygdala
    container.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (BNST in overview.)
*   NeuroNames — Bed nucleus of the stria terminalis (right); FMA —
    Bed nucleus of the stria terminalis (right member).
"""