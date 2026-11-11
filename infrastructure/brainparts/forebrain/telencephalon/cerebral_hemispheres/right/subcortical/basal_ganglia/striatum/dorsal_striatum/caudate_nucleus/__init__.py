"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.striatum.dorsal_striatum.caudate_nucleus
============================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_ganglia
                    └── striatum
                        └── dorsal_striatum
                            └── caudate_nucleus   <-- THIS MODULE

**Primary synonym:** Caudate nucleus; nucleus caudatus; caudate;
"the tailed nucleus" (from its long, curved tail).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**GABAergic nucleus** — the **cognitive/associative** component of
the **dorsal striatum** (with the **putamen** as the motor/
sensorimotor component).
**Part of:** The **dorsal striatum** container — specifically, the
**cognitive/associative** half (with the **putamen** as the **motor/
sensorimotor** half). Part of the **basal ganglia input** circuit.
**Structural parent:** ``.../dorsal_striatum/`` → **direct child** of
the dorsal striatum container.
**Structural children:** **None.** This is a **leaf** module. The
**head**, **body**, and **tail** of the caudate, and the
**striosome/matrix** compartments, are documented as **prose**, not
as structural children.
**Boundary status (the COGNITIVE/ASSOCIATIVE striatum — NOT the
putamen):** **Boundary case — the caudate is the COGNITIVE/
ASSOCIATIVE component of the dorsal striatum; the PUTAMEN is the
MOTOR/SENSORIMOTOR component.** The two are **cytoarchitecturally
continuous** around the **anterior** and **inferior** margins of the
**internal capsule**, but they are **functionally distinct**:
*   **Caudate** (this module) — **cognitive/associative**: working
    memory, cognitive control, goal-directed behavior, language
    (left — contested). Receives **prefrontal** and **parietal**
    cortical input. **Huntington's disease** (the caudate is the
    **most affected** striatal structure), **Tourette syndrome**,
    **OCD** (with the ventral striatum).
*   **Putamen** (``.../putamen/``) — **motor/sensorimotor**: action
    selection, movement initiation, habit learning. Receives
    **sensorimotor cortical** input. **Parkinson's disease** (the
    putamen is the **most affected** striatal structure),
    **dystonia**.
Consumers must **not** conflate the two — the caudate and putamen
are **functionally distinct** dorsal striatum components, **even
though** they are **cytoarchitecturally continuous** in the intact
brain. The **caudate's** clinical signature is **Huntington's
disease**; the **putamen's** clinical signature is **Parkinson's
disease**.
**Boundary status (NO extended-amygdala relationship — SLEA-free
leaf):** **Boundary case — the caudate nucleus has NO
extended-amygdala relationship, NO SLEA overlap, and NO
amygdala-lateralization warning.** The **extended amygdala (SLEA)**
overlap belongs to the **ventral striatum** (via the **nucleus
accumbens**) and the **ventral pallidum** — **not** to the caudate.
The caudate is a **dorsal striatum** structure — the **motor/
cognitive** subsystem — and the **SLEA** is a **limbic** continuum.
Consumers must **not** import amygdala-lateralization claims into the
caudate — **there is no anatomical relationship** to support them.
**The warning gradient that runs through the ventral striatum and
nucleus accumbens does NOT apply to this module** — the caudate is a
**strict mirror with no warning**.
**Boundary status (head/body/tail — three anatomical subdivisions,
prose not structural children):** **Boundary case — the caudate has
THREE classical subdivisions (head, body, tail) that are
ANATOMICALLY CONTINUOUS and FUNCTIONALLY DISTINCT.** The **caudate
head** is the **anterior** enlargement (adjacent to the frontal
horn of the lateral ventricle); the **caudate body** is the
**middle** segment (along the body of the lateral ventricle); the
**caudate tail** is the **posterior** segment (curving into the
temporal lobe, ending near the **amygdala**). The three subdivisions
are **cytoarchitecturally continuous** — they are **not** separate
nuclei — but they have **different cortical connections** and
**different functions**:
*   **Caudate head** — **prefrontal** and **associative** cortical
    input; **cognitive control, working memory, goal-directed
    behavior**. The **head** is the **most affected** part of the
    caudate in **Huntington's disease** (and the **most studied**).
*   **Caudate body** — **associative** and **sensorimotor** cortical
    input; **transitional** between cognitive and motor functions.
*   **Caudate tail** — **visual** and **auditory** cortical input
    (via the **temporal** and **occipital** lobes); **visual/
    auditory** associative functions. The **tail** ends near the
    **amygdala** — a **topographic** relationship, **not** a
    functional SLEA relationship.
The tree wires the caudate as a **single leaf** — the **head/body/
tail** subdivisions are **prose**, not structural children. Consumers
that need subdivision-level resolution should consult the references,
not the tree. **The head is the most clinically important
subdivision** — it is the **most affected** region in **Huntington's
disease** and the **most studied** caudate region in **cognitive
neuroscience**.
**Boundary status (striosome/matrix — two chemical compartments,
prose not structural children):** **Boundary case — the caudate has
TWO CHEMICAL COMPARTMENTS (striosomes and matrix) that are
INTERMINGLED and FUNCTIONALLY DISTINCT.** The **striosomes**
(**patches**) are **acetylcholinesterase-poor**, **substance
P/dynorphin-rich**, and project to the **substantia nigra pars
compacta** (the **dopaminergic** feedback loop). The **matrix** is
**acetylcholinesterase-rich**, **calbindin-rich**, and projects to
the **globus pallidus** and **substantia nigra pars reticulata** (the
**GABAergic** output loop). The two compartments are **intermingled**
in a **mosaic pattern** — they are **not** separate nuclei, but they
have **different inputs**, **different outputs**, and **different
functions**. The tree does **not** wire them as sub-modules — they are
**prose**. Consumers that need compartment-level resolution should
consult the references, not the tree.
**Boundary status (not the putamen — sibling):** **Boundary case —
the putamen is a SIBLING under the dorsal striatum, not a parent or
child.** The **putamen** is the **motor/sensorimotor** half; the
**caudate** is the **cognitive/associative** half. They are
**cytoarchitecturally continuous** (around the internal capsule) but
**functionally distinct**. Consumers that need the **motor** component
resolve ``.../putamen/``; consumers that need the **cognitive**
component resolve **this module**.
**Boundary status (not the ventral striatum — cousin):** **Boundary
case — the ventral striatum (nucleus accumbens + olfactory tubercle)
is a COUSIN of the caudate, not a parent or child.** The **ventral
striatum** is the **limbic/reward/olfactory** subsystem; the
**caudate** (with the putamen) is the **motor/cognitive/associative**
subsystem. They are **structurally separate** (dorsal vs. ventral)
and **functionally distinct**. Consumers that need the **limbic/
reward** subsystem resolve ``.../striatum/ventral_striatum/``;
consumers that need the **cognitive** subsystem resolve **this
module**. **The SLEA warning belongs to the ventral striatum and
ventral pallidum — NOT to the caudate.**
**Boundary status (not the substantia nigra — midbrain dopaminergic
INPUT):** **Boundary case — the substantia nigra is the
DOPAMINERGIC INPUT to the caudate, but it is a MIDBRAIN structure,
not a caudate child.** The **substantia nigra pars compacta**
provides **dopaminergic input** to the **caudate** (with the
putamen) — the **nigrostriatal pathway**. Its **degeneration** in
**Parkinson's disease** affects the **putamen** more than the
caudate, but the **nigrostriatal pathway** is the **dopaminergic
input to both**. The **substantia nigra** is under
``.../midbrain/tegmentum/substantia_nigra/`` — **not** under the
caudate. Consumers must **not** resolve the substantia nigra through
the caudate, and must **not** treat the caudate's dopaminergic input
as intrinsic to the caudate. **The caudate is the TARGET; the
substantia nigra is the SOURCE.**
**Boundary status (not the globus pallidus — the GPe/GPi are a
DOCUMENTED GAP):** **Boundary case — the caudate projects to the
GPe/GPi, but those are a DOCUMENTED GAP in the `globus_pallidus`
container.** The **caudate** (with the putamen) projects to the
**GPe** and **GPi** — the **direct pathway** (striatum → GPi →
thalamus) and the **indirect pathway** (striatum → GPe → STN → GPi →
thalamus). But the **GPe and GPi are NOT wired** — they are a
**documented structural gap** in the **parent** `globus_pallidus`
container. Consumers that need the **caudate's output** must resolve
the GPe/GPi functions as **prose** in the **parent** `globus_pallidus`
module, **not** here.
**Boundary status (not the internal capsule — white matter
separator):** **Boundary case — the internal capsule SEPARATES the
caudate from the putamen, but it is WHITE MATTER, not a caudate
child.** The **anterior limb** of the internal capsule separates the
**caudate head** from the **putamen**; the **posterior limb**
separates the **caudate body** from the **putamen**. The **internal
capsule** is under ``.../right/white_matter/`` — **not** a caudate
child. Consumers must **not** resolve the internal capsule through
the caudate.
**Boundary status (not a single functional system — head/body/tail
functional split):** **Boundary case — the caudate is a structural
grouping of three functionally distinct subdivisions (head, body,
tail), not a single functional system.** The **head** is **cognitive/
associative**; the **body** is **transitional**; the **tail** is
**visual/auditory associative**. The **head** is the **most
clinically important** subdivision (Huntington's disease). Consumers
must **not** treat "caudate" as a single functional system — it is a
**structural grouping** of **three functionally distinct**
subdivisions, and its **clinical associations** are dominated by the
**head**.

Overview
--------
The caudate nucleus is the **cognitive/associative** component of the
**dorsal striatum** — the **GABAergic nucleus** that receives
**prefrontal** and **parietal** cortical input and is involved in
**working memory, cognitive control, goal-directed behavior, and
habit learning**. It is the **structure that degenerates in
Huntington's disease** (especially the **caudate head**), the
**structure that is dysfunctional in Tourette syndrome and OCD**, and
the **contested left-side seat of procedural language processing**.

**The caudate is the "cognitive striatum."** Its **dorsal** position
(vs. the ventral striatum) and its **prefrontal/parietal** cortical
inputs make it the **associative/cognitive** component of the dorsal
striatum — the **complement** to the **putamen's** motor/sensorimotor
role. The **caudate** and **putamen** are **cytoarchitecturally
continuous** around the internal capsule, but **functionally
distinct** — the tree wires them as **two separate leaves** to
reflect this distinction.

**The caudate has THREE anatomical subdivisions — head, body, tail —
that are anatomically continuous but functionally distinct.** The
**head** is the **anterior** enlargement (adjacent to the frontal
horn of the lateral ventricle); the **body** is the **middle**
segment (along the body of the lateral ventricle); the **tail** is
the **posterior** segment (curving into the temporal lobe, ending
near the **amygdala**). **The head is the most clinically important**
— it is the **most affected** region in **Huntington's disease** and
the **most studied** caudate region in **cognitive neuroscience**.
The three subdivisions are **prose**, not structural children.

**The caudate has TWO chemical compartments — striosomes and matrix —
that are intermingled but functionally distinct.** The **striosomes**
(**patches**) project to the **substantia nigra pars compacta** (the
**dopaminergic** feedback loop); the **matrix** projects to the
**globus pallidus** and **substantia nigra pars reticulata** (the
**GABAergic** output loop). The two compartments are **intermingled**
in a **mosaic pattern** — they are **prose**, not structural children.

**The caudate has NO extended-amygdala relationship.** The **SLEA
overlap** belongs to the **ventral striatum** (via the **nucleus
accumbens**) and the **ventral pallidum** — **not** to the caudate.
**The warning gradient that runs through the ventral striatum and
nucleus accumbens does NOT apply to this module** — the caudate is a
**strict mirror with no warning**. This is a **deliberate structural
fact** — the **caudate** is a **dorsal striatum** structure, and the
**SLEA continuum** touches **only the ventral side** of the striatum.

**The caudate is a paired structure.** Each hemisphere has its own
caudate, with **ipsilateral** cortical, thalamic, and dopaminergic
input. The two sides are **bilaterally symmetric** and **largely
non-lateralized** — the **cognitive/associative** functions are
**bilateral**. Some **subtle lateralization** has been reported
(**left caudate** for language, **right caudate** for spatial
navigation), but it is **weak**, **contested**, and **not a strong
basis for classification**. See *Lateralization Notes*.

Subdivisions (prose, not structural children)
---------------------------------------------
The caudate is classically divided into **three anatomical
subdivisions**:

*   **Caudate head** — the **anterior** enlargement, adjacent to the
    **frontal horn** of the lateral ventricle. Receives **prefrontal**
    and **associative** cortical input. Involved in **cognitive
    control, working memory, and goal-directed behavior**. The **most
    affected** subdivision in **Huntington's disease** (the **caudate
    head atrophy** is a **diagnostic MRI finding**). The **most
    studied** caudate region in **cognitive neuroscience**.

*   **Caudate body** — the **middle** segment, along the **body** of
    the lateral ventricle. Receives **associative** and
    **sensorimotor** cortical input. **Transitional** between
    cognitive and motor functions.

*   **Caudate tail** — the **posterior** segment, curving into the
    **temporal lobe** and ending near the **amygdala**. Receives
    **visual** and **auditory** cortical input (via the **temporal**
    and **occipital** lobes). Involved in **visual/auditory
    associative functions**. The **topographic** relationship to the
    **amygdala** is **proximity**, **not** a functional SLEA
    relationship.

**These subdivisions are prose, not structural children.** The tree
wires the caudate as a **single leaf** — the **head/body/tail**
distinction is **prose**, reflecting the **anatomical continuity**
of the caudate. Consumers that need subdivision-level resolution
should consult the references, not the tree. **The head is the most
clinically important** — it is the **most affected** region in
**Huntington's disease** and the **most studied** caudate region in
**cognitive neuroscience**.

The Caudate / Putamen Boundary
------------------------------
This is the **most consequential boundary** in the module:

*   **Caudate** (this module) — the **cognitive/associative** half of
    the dorsal striatum. **Huntington's disease**, **Tourette
    syndrome**, **OCD**.

*   **Putamen** (``.../putamen/``) — the **motor/sensorimotor** half
    of the dorsal striatum. **Parkinson's disease**, **dystonia**.

**They are cytoarchitecturally continuous but functionally distinct.**
The **caudate** and **putamen** are **separated** by the **internal
capsule** (the **anterior limb** separates the caudate head from the
putamen; the **posterior limb** separates the caudate body from the
putamen), but they are **continuous** around the **anterior** and
**inferior** margins of the capsule. The tree wires them as **two
separate leaves** — a **deliberate boundary choice** reflecting their
**functional distinction** and their **clinical distinction**.

**The clinical distinction is diagnostic:**
- **Caudate** → **Huntington's disease** (chorea, cognitive decline,
  psychiatric symptoms).
- **Putamen** → **Parkinson's disease** (bradykinesia, rigidity,
  tremor).

The Caudate / Ventral Striatum Boundary
---------------------------------------
This is the **dorsal/ventral** boundary of the striatum:

*   **Caudate** (this module) — the **dorsal striatum** (cognitive/
    associative). Part of the **motor/cognitive** subsystem.

*   **Ventral striatum** (``.../striatum/ventral_striatum/``) — the
    **limbic/reward/olfactory** subsystem (nucleus accumbens +
    olfactory tubercle). **SLEA-bearing** half.

**They are cousins (dorsal vs. ventral striatum).** The **caudate**
is the **cognitive** half of the **dorsal** striatum; the **ventral
striatum** is the **limbic/reward** half. Consumers that need the
**cognitive** subsystem resolve **this module**; consumers that need
the **limbic/reward** subsystem resolve
``.../striatum/ventral_striatum/``. **The SLEA warning belongs to the
ventral striatum and ventral pallidum — NOT to the caudate.**

The Caudate / Substantia Nigra Boundary
---------------------------------------
This is the **dopaminergic input** boundary:

*   **Substantia nigra** —
    ``.../midbrain/tegmentum/substantia_nigra/`` — the **dopaminergic**
    (pars compacta) and **GABAergic** (pars reticulata) **midbrain**
    nucleus. Its **pars compacta** provides **dopaminergic input to
    the caudate** (and putamen) — the **nigrostriatal pathway**. Its
    **pars reticulata** receives **striatal output** from the
    **striosomes** of the caudate (the **striatonigral** projection).

*   **Caudate** (this module) — the **dopaminergic TARGET** (via the
    nigrostriatal pathway). **Telencephalic**.

**The substantia nigra is NOT a caudate child.** It is a **midbrain**
structure — functionally related (dopaminergic input to the caudate)
but structurally separate. Consumers must **not** resolve the
substantia nigra through the caudate, and must **not** treat the
caudate's dopaminergic input as intrinsic to the caudate. **The
caudate is the TARGET; the substantia nigra is the SOURCE.**

The Caudate / Globus Pallidus Boundary
--------------------------------------
This is the **output-target** boundary — **the GPe/GPi are a
documented gap**:

*   **Caudate** (this module) — the **input** structure (cognitive/
    associative half of the dorsal striatum). **Wired**.

*   **Globus pallidus** (``.../basal_ganglia/globus_pallidus/``) — the
    **output** structure. Its **dorsal segments** (GPe, GPi) are the
    **caudate's output targets**, but they are **NOT wired** — a
    **documented gap** in the parent `globus_pallidus` container.
    Only the **ventral pallidum** is wired.

**The caudate → GPe/GPi circuit is the cognitive/motor circuit.** The
**direct pathway** (caudate → GPi → thalamus) and the **indirect
pathway** (caudate → GPe → STN → GPi → thalamus) both go through the
**GPe/GPi** — which are **not wired**.

**Consumers that need the caudate's output** must resolve the GPe/GPi
functions as **prose** in the **parent** `globus_pallidus` module —
**not** here, and **not** as structural children. The **caudate's
output targets are a documented gap** in the sibling container.

The Caudate / Internal Capsule Boundary
---------------------------------------
This is the **white-matter separation** boundary:

*   **Internal capsule** — ``.../right/white_matter/`` — the
    **white-matter tract** that **separates** the **caudate** from
    the **putamen**:
    *   **Anterior limb** — separates the **caudate head** from the
        **putamen**.
    *   **Posterior limb** — separates the **caudate body** from the
        **putamen**.

*   **Caudate** (this module) — the **grey-matter structure** that the
    internal capsule **passes beside**.

**The internal capsule is NOT a caudate child.** It is **white
matter** under ``.../right/white_matter/`` — **not** a caudate
component.

Function in the Human Brain
---------------------------
The caudate nucleus has **three functionally distinct subdivisions**
(head, body, tail) and **two chemical compartments** (striosomes,
matrix). The **unifying functions** are **cognitive/associative**:

*   **Working Memory and Cognitive Control (Caudate Head —
    Primary Function):** The **caudate head** receives **prefrontal**
    and **parietal** cortical input and is involved in **working
    memory, cognitive control, and goal-directed behavior**. Its
    **dysfunction** produces **cognitive and psychiatric symptoms**
    — the **cognitive/psychiatric** component of **Huntington's
    disease**, and the **cognitive** component of **OCD**.

*   **Goal-Directed Behavior (Caudate Function):** The **caudate**
    (with the **ventral striatum**) is involved in **goal-directed
    behavior** — the **flexible, outcome-based** selection of
    actions. Its **dysfunction** contributes to the **cognitive
    rigidity** of **Huntington's disease** and the **tics** of
    **Tourette syndrome**.

*   **Habit Learning (Caudate + Putamen Function):** The **caudate**
    (with the **putamen**) is involved in **habit learning** — the
    **gradual shift** from **goal-directed** to **habitual** behavior.
    Its **dopaminergic input** from the **substantia nigra** is
    essential for this **reinforcement learning**.

*   **Language (Left Caudate — Contested):** The **left caudate**
    has been reported to participate in **language** (via the
    **cortico-striatal loop**), contributing to **procedural language
    processing** — but this is **weak**, **contested**, and **not a
    strong basis for classification**. **On the right side**, the
    **right caudate** is **not** the language-lateralized structure —
    its **spatial-memory** association is the **weaker** of the two
    lateralization claims.

*   **Visual/Auditory Associative Functions (Caudate Tail —
    Secondary Function):** The **caudate tail** receives **visual**
    and **auditory** cortical input (via the **temporal** and
    **occipital** lobes) and is involved in **visual/auditory
    associative functions** — the **less studied** caudate
    subdivision.

*   **Tourette Syndrome and OCD (Caudate Dysfunction):** The
    **caudate** (especially the **head**) is **dysfunctional** in
    **Tourette syndrome** (producing **tics**) and **OCD**
    (contributing to **obsessions and compulsions**, with the ventral
    striatum).

**The unifying theme:** the caudate is the **cognitive/associative
striatum** — the **input side** of the **cognitive basal ganglia
circuit**. Its **head** is the **most clinically important**
subdivision (**Huntington's disease**); its **body** is
**transitional**; its **tail** is **less studied** (**visual/
auditory associative**). **The caudate has NO SLEA warning** — it is
a **dorsal striatum** structure, and the **extended amygdala
continuum** touches **only the ventral side** of the striatum.

Associated Disorders
--------------------
Caudate nucleus disorders are **cognitive, psychiatric, and
movement-related** — dominated by the **caudate head**:

*   **Huntington's Disease (Signature Disorder):** The **caudate
    head** is the **most affected** striatal structure in
    **Huntington's disease** — **caudate atrophy** (especially the
    **head**) is a **diagnostic MRI finding**, and **caudate
    degeneration** produces **chorea, cognitive decline, and
    psychiatric symptoms**. **This is the caudate's signature
    clinical association** — more than any other structure, the
    caudate is **defined clinically by its role in Huntington's
    disease**.

*   **Tourette Syndrome:** **Caudate dysfunction** (especially the
    **head**) produces **tics** (motor and vocal). The **caudate** is
    part of the **cortico-striato-thalamo-cortical** circuit that is
    **dysfunctional** in Tourette syndrome. **DBS of the caudate
    region** (or the **thalamus** or **GPi**) has been investigated
    for **refractory tics**.

*   **Obsessive-Compulsive Disorder (OCD):** **Caudate dysfunction**
    (with the **ventral striatum** and **orbitofrontal cortex**)
    contributes to **obsessions and compulsions**. The **caudate** is
    part of the **OCD circuit** — its **dysfunction** impairs the
    **gating** of **intrusive thoughts and repetitive behaviors**.

*   **Cognitive Impairment (Caudate Dysfunction):** **Caudate
    dysfunction** contributes to **working memory** and **executive
    function** deficits in **neurodegenerative disease** (e.g.,
    **Huntington's**, **Parkinson's dementia**, **frontotemporal
    dementia**) and in **psychiatric disorders** (e.g.,
    **schizophrenia**).

*   **Procedural Language Deficits (Left Caudate — Contested):**
    **Left caudate dysfunction** has been reported to impair
    **procedural language processing** (e.g., **grammar**,
    **morphology**) — but this is **weak**, **contested**, and
    **not a strong clinical association**.

*   **Apathy (Caudate Dysfunction):** **Caudate dysfunction** can
    contribute to **apathy** — the **loss of motivation** — in
    **neurodegenerative disease** (with the **ventral striatum** and
    **anterior cingulate**).

**What is NOT here:** The caudate is **not** the substrate for
**Alzheimer's disease** (nucleus basalis), **basal forebrain amnesia**
(septum/DBB), **Kluver-Bucy syndrome** (amygdala), **temporal lobe
epilepsy** (hippocampus), **addiction** (nucleus accumbens — ventral
striatum), or **depression** (nucleus accumbens — ventral striatum).
Its clinical footprint is **cognitive** (**Huntington's disease**,
**Tourette syndrome**, **OCD**, **cognitive impairment**) — a
**distinct category** from the **putamen's** **motor** footprint and
the **ventral striatum's** **limbic/reward** footprint.

Lateralization Notes
--------------------
This is the **right** caudate nucleus module. The caudate is
**bilaterally symmetric** and **largely non-lateralized** — **and it
carries NO extended-amygdala warning**:

*   **Bilateral Cognitive Functions:** Each caudate projects
    **ipsilaterally** to the GPe/GPi. The two sides are
    **functionally symmetric** for cognitive/associative functions.
    **Huntington's disease** is **bilateral** — the **caudate
    degeneration** is **bilateral** (though often **asymmetric** in
    severity).

*   **Weak Lateralization (Contested — Caudate):** The **caudate**
    has been reported to show **subtle** lateralization — **left
    caudate** for **language** (via the cortico-striatal loop),
    **right caudate** for **spatial navigation**. This is **weak**
    and **contested**, documented as **prose**, not as a strong
    classification basis. **On the right side**, the **right
    caudate's spatial-memory association** is the **weaker** of the
    two lateralization claims — it is **not** a strong basis for
    module-level classification. **The weak lateralization is NOT a
    rationale for a prose asymmetry** — the caudate module is a
    **strict mirror** at the structural level.

*   **NO Extended-Amygdala Warning (strict mirror with no warning):**
    The caudate has **NO extended-amygdala relationship**, **NO SLEA
    overlap**, and **NO amygdala-lateralization warning**. The
    **SLEA overlap** belongs to the **ventral striatum** (via the
    **nucleus accumbens**) and the **ventral pallidum** — **not** to
    the caudate. Consumers must **not** import amygdala-lateralization
    claims into the caudate — **there is no anatomical relationship**
    to support them. **The warning gradient that runs through the
    ventral striatum and nucleus accumbens does NOT apply to this
    module** — the caudate is a **strict mirror with no warning**,
    matching the **dorsal striatum container** and the **basal
    ganglia container** at their respective levels. **The right-side
    module carries the same no-warning status** — no dedicated Usage
    block, no contrast reference, no deferral note. **The caudate has
    no amygdala-adjacent structure** at any level of its subtree —
    the head, body, and tail are **not** SLEA-bearing, and **no
    warning applies**.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module** — **not** to the caudate, **not** to the head/
    body/tail, and **not** to the striosomes/matrix. **The caudate
    has no anatomical relationship to the amygdala** — the **SLEA
    overlap** is a **ventral striatum** fact, and it **does not
    transfer** to the caudate. **This is true on the right side as
    well** — the right caudate is **not** SLEA-bearing, and the right
    amygdala's fear-processing association **does not** apply to it.
    The **caudate tail's proximity to the amygdala** is
    **topographic**, **not** a functional SLEA relationship — a
    subtle distinction that consumers must not overinterpret.

**A consumer that assumes "right caudate = left caudate" will be
structurally and functionally correct** — the two sides are
**largely symmetric**, no **strong** lateralized syndrome has been
demonstrated, and the **weak** lateralization reported for the
caudate is **contested**, not a strong classification basis. The
caudate module is a **strict-mirror pair with no warning** —
matching the **dorsal striatum container** and the **basal ganglia
container** at their respective levels. **The right-side module
carries the same no-warning status** — no dedicated Usage block, no
contrast reference, no deferral note.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../diencephalon/``, or any other container.
    The caudate's relationships to the substantia nigra, globus
    pallidus, putamen, and internal capsule are documented as
    **prose and boundary data**, not as structural parents or
    children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **head/body/tail**
    subdivisions and the **striosome/matrix** compartments are
    documented as **prose**, not as sub-modules. Consumers must not
    assume any exist as children; resolve subdivision-level detail
    through the references.
*   **Cognitive/associative component — NOT the putamen.** The
    **caudate** is the **cognitive/associative** half of the dorsal
    striatum; the **putamen** is the **motor/sensorimotor** half.
    Consumers must not conflate the two — they are **functionally
    distinct**.
*   **NO extended-amygdala warning — strict mirror with no warning.**
    The caudate has **NO SLEA overlap**, **NO amygdala relationship**,
    and **NO amygdala-lateralization warning**. The **SLEA warning**
    belongs to the **ventral striatum** (nucleus accumbens) and the
    **ventral pallidum** — **not** here. **The right-side module
    carries the same no-warning status** — no dedicated Usage block,
    no contrast reference, no deferral note.
*   **The GPe/GPi are a documented gap — the caudate's output targets
    are NOT wired.** The **caudate** projects to the **GPe** and
    **GPi**, but those are a **documented gap** in the **parent**
    `globus_pallidus` container. Consumers that need the caudate's
    output must resolve the GPe/GPi functions as **prose** in the
    parent `globus_pallidus` module.
*   **Not the substantia nigra — midbrain input.** The substantia
    nigra provides dopaminergic input to the caudate (nigrostriatal
    pathway). It is a **midbrain** structure, not a caudate child.
*   **Not the internal capsule — white matter.** The internal capsule
    **separates** the caudate from the putamen, but it is **white
    matter** under ``.../right/white_matter/`` — **not** a caudate
    child.
*   **Not a single functional system — head/body/tail split.** The
    **head** (cognitive/associative), **body** (transitional), and
    **tail** (visual/auditory associative) are **functionally
    distinct**. The **head** is the **most clinically important**
    subdivision (Huntington's disease). Consumers must not treat
    "caudate" as a single functional system.
*   **The caudate tail is NEAR the amygdala — but NOT SLEA-related.**
    The **caudate tail** ends near the **amygdala** — a **topographic**
    relationship, **not** a functional SLEA relationship. Consumers
    must not overinterpret the proximity as an extended-amygdala
    connection.
*   **No ``AREA_PATHS`` hop.** The caudate is a local leaf under the
    dorsal striatum, not a cross-listed leaf.
*   **No nested cross-listing.** The caudate has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with left caudate — strict mirror with NO
    warning.** Right and left caudate modules are **structurally
    identical** — same leaf status, same head/body/tail prose, same
    striosome/matrix prose, same GPe/GPi documented-gap note, same
    substantia nigra input note, same **no extended-amygdala
    warning**. **The right-side module carries the same no-warning
    status** — no dedicated Usage block, no contrast reference, no
    deferral note.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.striatum.dorsal_striatum import caudate_nucleus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_ganglia.striatum.dorsal_striatum.caudate_nucleus"
    )

**Do not** assume the caudate is the **putamen**. The **caudate** is
the **cognitive/associative** half; the **putamen** is the **motor/
sensorimotor** half. They are **functionally distinct** — the
caudate is **Huntington's** (chorea, cognitive decline), the putamen
is **Parkinson's** (bradykinesia, rigidity, tremor).

**Do not** assume the caudate is a **single functional system**. Its
**head** (cognitive/associative), **body** (transitional), and
**tail** (visual/auditory associative) are **functionally
distinct**. The **head** is the **most clinically important**
subdivision.

**Do not** assume the caudate has **structural children**. It is a
**leaf**. The **head/body/tail** subdivisions and the **striosome/
matrix** compartments are **prose only** — they are not wired as
modules.

**Do not** assume the caudate **contains** the GPe/GPi. Those are the
**output targets** of the caudate, but they are a **documented gap**
in the **parent** `globus_pallidus` container. They are **not**
caudate children.

**Do not** assume the caudate **contains** the substantia nigra. It is
a **midbrain** structure that provides **dopaminergic input** to the
caudate — functionally related but structurally separate.

**Do not** import **amygdala-lateralization claims** into the caudate.
**The caudate has NO extended-amygdala relationship** — the SLEA
overlap belongs to the **ventral striatum** and **ventral pallidum**.
**The right-side module carries the same no-warning status** — the
right caudate is **not** SLEA-bearing, and the right amygdala's
fear-processing association **does not** apply to it. **The caudate
tail's proximity to the amygdala is TOPOGRAPHIC, not a functional
SLEA relationship** — do not overinterpret it.

Iterating the caudate's (empty) children (recommended consumer
pattern)::

    CAUDATE_CHILDREN = ()
    # The caudate is a leaf. The head/body/tail subdivisions and the
    # striosome/matrix compartments are prose, not modules.

Reaching the caudate's output targets (recommended consumer pattern
— NOTE the GAP)::

    # The caudate projects to the GPe and GPi (the output targets).
    # But the GPe and GPi are a DOCUMENTED GAP in the parent
    # `globus_pallidus` container — they are NOT wired.
    #
    # Resolve:
    #
    #   subcortical.basal_ganglia.globus_pallidus
    #     -> parent module's "Dorsal Segment Gap" section
    #
    # Do NOT attempt to resolve a "gpe" or "gpi" path.

Reaching the substantia nigra (recommended consumer pattern — NOTE
the midbrain boundary)::

    # The substantia nigra provides dopaminergic input to the caudate
    # (nigrostriatal pathway). It is a MIDBRAIN structure, not a
    # caudate child:
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # The substantia nigra is the SOURCE; the caudate is the TARGET.

Reaching the putamen (recommended consumer pattern — the sibling)::

    # The putamen is a SIBLING of the caudate — the motor/sensorimotor
    # half of the dorsal striatum:
    #
    #   subcortical.basal_ganglia.striatum.dorsal_striatum.putamen
    #
    # The caudate and putamen are cytoarchitecturally continuous but
    # functionally distinct.

Reaching the internal capsule (recommended consumer pattern — NOTE
the white-matter boundary)::

    # The internal capsule separates the caudate from the putamen,
    # but it is WHITE MATTER, not a caudate child:
    #
    #   white_matter.internal_capsule
    #
    # Do NOT resolve the internal capsule through the caudate.

Subdivision-level detail (not wired — consult references)::

    # The caudate's subdivisions and compartments are prose, not
    # modules:
    #   head   -> prefrontal/associative; Huntington's disease
    #   body   -> transitional
    #   tail   -> visual/auditory associative; near the amygdala
    #   striosomes -> substantia nigra pars compacta (dopaminergic)
    #   matrix     -> globus pallidus + substantia nigra pars reticulata
    #
    # Do not attempt to resolve these as sub-paths of the caudate.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        caud_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.striatum.dorsal_striatum.caudate_nucleus"
        )
        # resolve caud_path through the memory/recall layer

References
----------
*   **Canonical caudate anatomy:** Alexander, G.E., DeLong, M.R.,
    Strick, P.L. (1986). "Parallel organization of functionally
    segregated circuits linking basal ganglia and cortex." *Annual
    Review of Neuroscience* 9:357–381. (Parallel cortico-striatal
    loops; caudate → cognitive, putamen → motor.)
*   **Caudate functional anatomy:** Graybiel, A.M. (2008). "Habits,
    rituals, and the evaluative brain." *Annual Review of
    Neuroscience* 31:359–387. (Caudate in cognitive control, habit
    learning, and goal-directed behavior.)
*   **Striosome/matrix compartments:** Graybiel, A.M., Ragsdale,
    C.W. (1978). "Histochemically distinct compartments in the
    striatum of human, monkey, and cat demonstrated by
    acetylthiocholinesterase staining." *PNAS* 75:5723–5726.
    (Striosome/matrix compartments; mosaic pattern.)
*   **Caudate head/body/tail:** Parent, A., Carpenter, M.B. (1996).
    *Carpenter's Human Neuroanatomy*, 9th ed. (Caudate subdivisions;
    anatomical continuity and functional distinction.)
*   **Huntington's disease:** Vonsattel, J.P., DiFiglia, M. (1998).
    "Huntington disease." *Journal of Neuropathology and Experimental
    Neurology* 57:369–384. (Caudate degeneration in HD; the caudate
    is the most affected striatal structure; caudate head atrophy as
    a diagnostic MRI finding.)
*   **Tourette syndrome:** Leckman, J.F., et al. (2010). "Tourette
    syndrome: the self under siege." *Journal of Child Neurology*
    25:1155–1162. (Caudate dysfunction in Tourette syndrome; tics.)
*   **OCD:** Saxena, S., Rauch, S.L. (2000). "Functional neuroimaging
    and the neuroanatomy of obsessive-compulsive disorder."
    *Psychiatric Clinics of North America* 23:563–586. (Caudate
    dysfunction in OCD; cortico-striato-thalamo-cortical circuit.)
*   **Cognitive impairment (caudate):** Levy, R., Dubois, B. (2006).
    "Apathy and the functional anatomy of the prefrontal cortex-basal
    ganglia circuits." *Cerebral Cortex* 16:916–928. (Caudate
    dysfunction and apathy; cognitive impairment.)
*   **Substantia nigra (contrast — midbrain input):** Braak, H., et
    al. (2003). "Staging of brain pathology related to sporadic
    Parkinson's disease." *Neurobiology of Aging* 24:197–211.
    (Substantia nigra as the source of dopaminergic input to the
    caudate and putamen; the substantia nigra is a midbrain
    structure, not a caudate child.)
*   **Globus pallidus GPe/GPi gap (contrast — documented gap):**
    DeLong, M.R., Wichmann, T. (2007). "Circuits and circuit disorders
    of the basal ganglia." *Archives of Neurology* 64:20–24. (GPe/GPi
    as the caudate's output targets; the GPe/GPi are a documented gap
    in the parent `globus_pallidus` container.)
*   **Internal capsule (contrast — white matter):** Nieuwenhuys, R.,
    Voogd, J., van Huijzen, C. (2008). *The Human Central Nervous
    System*, 4th ed. (Internal capsule separating the caudate from
    the putamen; the internal capsule is white matter, not a caudate
    child.)
*   **Caudate lateralization (caudate — weak, contested):** Ullman,
    M.T. (2004). "Contributions of memory circuits to language: the
    declarative/procedural model." *Cognition* 92:231–270. (Left
    caudate in language; procedural memory.)
*   **Right caudate spatial memory (contrast):** Postle, B.R.,
    D'Esposito, M. (1999). "Dissociation of human caudate nucleus
    activity during spatial and verbal working memory." *Cognitive
    Brain Research* 7:571–580. (Right caudate and spatial working
    memory; weak, contested lateralization — **contrast reference**,
    not a strong basis for module-level classification.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical
    pathway to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association does
    **not** apply to the caudate — the caudate has **no
    extended-amygdala relationship**, and the SLEA warning is a
    **ventral striatum / ventral pallidum** fact. The right caudate
    is **not** SLEA-bearing.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Caudate nucleus in overview.)
*   NeuroNames — Caudate nucleus (right); FMA — Caudate nucleus
    (right member).
"""