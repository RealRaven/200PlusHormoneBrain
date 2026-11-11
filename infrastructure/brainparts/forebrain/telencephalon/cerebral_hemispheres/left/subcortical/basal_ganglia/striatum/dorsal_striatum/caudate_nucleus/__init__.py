"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_ganglia.striatum.dorsal_striatum.caudate_nucleus
=============================================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── left
            └── subcortical
                └── basal_ganglia
                    └── striatum
                        └── dorsal_striatum
                            └── caudate_nucleus   <-- THIS MODULE

**Primary synonym:** Caudate nucleus; caudate; nucleus caudatus;
"the caudate."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**GABAergic medium spiny neuron nucleus** — the **cognitive/
associative** component of the **dorsal striatum** (with the
**putamen** as the **motor/sensorimotor** component).
**Part of:** The **dorsal striatum** container — specifically, the
**cognitive/associative** half (with the **putamen** as the
**motor/sensorimotor** half). The **dorsal striatum** is the
**motor/cognitive** half of the **striatum** (with the **ventral
striatum** as the **limbic/reward/olfactory** half).
**Structural parent:** ``.../dorsal_striatum/`` → **direct child** of
the dorsal striatum container.
**Structural children:** **None.** This is a **leaf** module. The
**C-shape subdivisions** (head, body, tail) and the **striosome/
matrix** compartments are documented as **prose**, not as structural
children.
**Boundary status (the cognitive/associative half of the dorsal
striatum — NOT the putamen):** **Boundary case — the caudate is the
COGNITIVE/ASSOCIATIVE component; the PUTAMEN is the MOTOR/
SENSORIMOTOR component.** The **caudate** and the **putamen** are the
two **classical subdivisions** of the **dorsal striatum** — both
**fully wired leaves** under ``.../dorsal_striatum/``. They are
**cytoarchitecturally continuous** around the **anterior** and
**inferior** margins of the internal capsule (the **caudate-putamen
junction**), but they are **functionally distinct**:
*   **Caudate** — **cognitive/associative**: working memory, cognitive
    control, goal-directed behavior, language (left, contested). Its
    **degeneration** in **Huntington's disease** produces **chorea,
    cognitive decline, and psychiatric symptoms**. Its **dysfunction**
    in **Tourette syndrome** produces **tics**; in **OCD**,
    **obsessions and compulsions**.
*   **Putamen** — **motor/sensorimotor**: action selection, movement
    initiation, habit learning. Its **dopaminergic denervation** in
    **Parkinson's disease** produces **bradykinesia, rigidity, and
    tremor**. Its **dysfunction** in **dystonia** produces **sustained
    muscle contractions**.
Consumers must **not** treat the caudate and putamen as
**interchangeable** — they are **functionally distinct** (cognitive
vs. motor), **clinically distinct** (Huntington's vs. Parkinson's),
and **anatomically distinct** (though **cytoarchitecturally
continuous**).
**Boundary status (C-shape — head, body, tail as PROSE, not
structural children):** **Boundary case — the caudate is a C-SHAPED
structure with THREE classical subdivisions (head, body, tail), all
documented as PROSE, not as structural children.** The **C-shape**
follows the **lateral ventricle**:
*   **Head (caput)** — the **anterior**, bulbous part, bulging into
    the **anterior horn of the lateral ventricle**. It is the
    **largest** subdivision and the **most affected** in
    **Huntington's disease** (the **caudate head atrophy** is the
    **classic imaging finding** in HD).
*   **Body (corpus)** — the **middle** part, running along the
    **thalamus** and forming the **floor of the central part of the
    lateral ventricle**.
*   **Tail (cauda)** — the **posterior**, thin part, arching around
    the **thalamus** and ending at the **amygdala** in the **temporal
    lobe**.
**These subdivisions are prose, not structural children.** The tree
does **not** wire them as sub-modules. Consumers that need
subdivision-level resolution should consult the references, not the
tree. The **head** is the **most clinically important** subdivision
(the **HD imaging hallmark**), and the **tail** is the **only
subdivision that reaches the temporal lobe** (ending at the amygdala
— a **topographic** relationship, not a structural one).
**Boundary status (NO extended-amygdala relationship — the caudate is
SLEA-free):** **Boundary case — the caudate has NO extended-amygdala
relationship, NO SLEA overlap, and NO amygdala-lateralization
warning.** The **SLEA overlap** belongs to the **ventral striatum**
(via the **nucleus accumbens**) and the **ventral pallidum** — **not**
to the caudate. The **caudate tail** ends at the **amygdala** in the
**temporal lobe** — a **topographic** relationship (the tail's
terminal point) — but it is **NOT** an **extended-amygdala** structure.
Consumers must **not** import amygdala-lateralization claims into the
caudate — **there is no anatomical relationship** to support them.
**The warning gradient that runs through the ventral striatum and
nucleus accumbens does NOT apply to this module** — the caudate is a
**strict mirror with no warning**, matching the **dorsal striatum
container**.
**Boundary status (not the putamen — sibling):** **Boundary case —
the putamen is a SIBLING under the dorsal striatum, not a child or
parent of the caudate.** The **putamen** is the **motor/sensorimotor**
half; the **caudate** is the **cognitive/associative** half. They are
**functionally distinct** and **clinically distinct**.
**Boundary status (not the ventral striatum — different striatal
subsystem):** **Boundary case — the ventral striatum (nucleus
accumbens + olfactory tubercle) is a DIFFERENT striatal subsystem,
not a parent or child of the caudate.** The **caudate** is the
**dorsal striatum's cognitive/associative** component; the **ventral
striatum** is the **limbic/reward/olfactory** subsystem. Consumers
that need the **limbic/reward** subsystem resolve
``.../ventral_striatum/``; consumers that need the **cognitive/
associative** subsystem resolve **this module**.
**Boundary status (not the globus pallidus — the GPe/GPi are the
caudate's OUTPUT TARGETS but a DOCUMENTED GAP in the sibling
container):** **Boundary case — the globus pallidus is a SIBLING of
the striatum (under the basal ganglia), and its DORSAL segments (GPe,
GPi) are the CAUDATE'S OUTPUT TARGETS but are a DOCUMENTED GAP in
the `globus_pallidus` container.** The **caudate** projects to the
**GPe** and **GPi** (via the **direct** and **indirect pathways**),
but the **GPe and GPi are NOT wired** — they are a **documented
structural gap** in the **parent** `globus_pallidus` container (which
wires only the **ventral pallidum**). **The caudate's output targets
are NOT wired** — a **major structural gap** for the cognitive/
associative circuit. Consumers that need the caudate's output must
resolve the GPe/GPi functions as **prose** in the **parent**
`globus_pallidus` module, **not** here and **not** as structural
children.
**Boundary status (not the substantia nigra — midbrain dopaminergic
INPUT):** **Boundary case — the substantia nigra provides
DOPAMINERGIC INPUT to the caudate (via the nigrostriatal pathway),
but it is a MIDBRAIN structure, not a caudate child.** The
**substantia nigra (pars compacta)** → **caudate** is the
**nigrostriatal dopaminergic pathway**. **Degeneration of this
pathway** is the **basis of Parkinson's disease motor symptoms** —
but the **caudate** is **less affected** than the **putamen** in PD
(the **putamen** loses **more** dopaminergic input than the
**caudate**). The **substantia nigra** is under
``.../midbrain/tegmentum/substantia_nigra/`` — **not** under the
caudate. Consumers must **not** resolve the substantia nigra through
the caudate.
**Boundary status (not the internal capsule — white matter
separator):** **Boundary case — the internal capsule SEPARATES the
caudate from the putamen, but it is WHITE MATTER, not a caudate
child.** The **anterior limb** of the internal capsule separates the
**caudate head** from the **putamen**; the **posterior limb**
separates the **caudate body** from the **putamen**. The **internal
capsule** is under ``.../left/white_matter/`` — **not** a caudate
child. Consumers must **not** resolve the internal capsule through
the caudate.

Overview
--------
The caudate nucleus is the **cognitive/associative** component of the
**dorsal striatum** — the **C-shaped** grey-matter structure that
follows the **lateral ventricle** and forms the **floor of its
anterior horn and central part**. It is the **most affected striatal
structure in Huntington's disease** (its **head atrophy** is the
**classic imaging hallmark** of HD), a **key node** in the
**cortico-striato-thalamo-cortical cognitive/associative circuit**,
and the **anatomical substrate** of **Tourette syndrome** tics and
**OCD** compulsions (with the ventral striatum).

**The caudate is the cognitive/associative half of the dorsal
striatum.** The **putamen** is the **motor/sensorimotor** half. The
two are **cytoarchitecturally continuous** around the **anterior**
and **inferior** margins of the internal capsule (the **caudate-
putamen junction**), but they are **functionally distinct** — the
**caudate** is **cognitive/associative** (working memory, cognitive
control, goal-directed behavior), and the **putamen** is **motor/
sensorimotor** (action selection, movement initiation, habit
learning). The tree wires them as **two separate leaves** — a
**deliberate boundary choice** reflecting their **functional and
clinical distinction**.

**The caudate is C-shaped with THREE classical subdivisions (head,
body, tail).** The **head** is the **anterior, bulbous** part — the
**largest** subdivision and the **most affected** in **Huntington's
disease**. The **body** runs along the **thalamus**. The **tail**
arches around the **thalamus** and ends at the **amygdala** in the
**temporal lobe** — a **topographic** relationship (the tail's
terminal point), **not** an **extended-amygdala** relationship. The
**C-shape** follows the **lateral ventricle**, and its **three
subdivisions** are documented as **prose**, not as structural
children.

**The caudate is SLEA-free.** The **extended amygdala (SLEA)**
overlap belongs to the **ventral striatum** (via the **nucleus
accumbens**) and the **ventral pallidum** — **not** to the caudate.
The **caudate tail** ends at the **amygdala**, but this is a
**topographic** relationship (the **terminal point** of the tail),
**not** an **SLEA** relationship. **The warning gradient that runs
through the ventral striatum and nucleus accumbens does NOT apply to
the caudate** — the caudate is a **strict mirror with no warning**,
matching the **dorsal striatum container**.

**The caudate's OUTPUT goes to the GPe/GPi — which are a documented
gap in the sibling `globus_pallidus` container.** This is the **most
consequential boundary fact** in the module: the **caudate is
wired**, but its **output targets** (the **GPe** and **GPi**) are
**not**. The **caudate → GPe/GPi** circuit is the **cognitive/
associative circuit** that is disrupted in **Huntington's disease**
and **Tourette syndrome** — the **unwired GPe/GPi** are the
**anatomical substrate** of the **cognitive and motor symptoms** of
those diseases.

**The caudate is a paired structure.** Each hemisphere has its own
caudate, with **ipsilateral** cortical, thalamic, and dopaminergic
input. The two sides are **bilaterally symmetric** and **largely
non-lateralized** — the cognitive/associative functions are
**bilateral**. Some **subtle lateralization** has been reported
(left caudate for language, right caudate for spatial), but it is
**weak** and **contested**. See *Lateralization Notes*.

Subdivisions (prose, not structural children)
---------------------------------------------
The caudate is a **C-shaped** structure with **three classical
subdivisions**, all documented as **prose**:

*   **Head (caput)** — the **anterior**, **bulbous** part,
    **bulging into the anterior horn of the lateral ventricle**.
    It is the **largest** subdivision, the **most affected** in
    **Huntington's disease** (the **caudate head atrophy** is the
    **classic imaging finding** in HD), and the **primary target**
    of **prefrontal** and **parietal** cortical input (via the
    **cortico-striatal loop**). It is the **cognitive/associative**
    core of the caudate.

*   **Body (corpus)** — the **middle** part, running along the
    **thalamus** and forming the **floor of the central part of the
    lateral ventricle**. It receives **prefrontal** and **parietal**
    input and is **functionally continuous** with the head.

*   **Tail (cauda)** — the **posterior**, **thin** part, arching
    around the **thalamus** and ending at the **amygdala** in the
    **temporal lobe**. It is the **only subdivision that reaches
    the temporal lobe** — a **topographic** relationship (the tail's
    terminal point), **not** an **extended-amygdala** relationship.
    The tail receives **temporal** and **limbic** input and is
    **functionally distinct** from the head/body (more **limbic-
    adjacent**).

**These subdivisions are prose, not structural children.** The tree
does **not** wire them as sub-modules. Consumers that need
subdivision-level resolution should consult the references, not the
tree. The **head** is the **most clinically important** subdivision
(the **HD imaging hallmark**); the **tail** is the **only one that
reaches the temporal lobe** (ending at the amygdala).

**The striosome/matrix compartments** are also **prose** — the
**caudate** (with the **putamen**) contains **two chemically and
connectionally distinct compartments**: the **striosomes** (patches,
**limbic-related**) and the **matrix** (**sensorimotor-related**).
These compartments are **cytoarchitecturally defined** but **not
wired** as structural children. Consumers that need **compartment-
level** resolution should consult the references.

Function in the Human Brain
---------------------------
The caudate's functions are **cognitive/associative** — working
memory, cognitive control, goal-directed behavior, and language
(left, contested):

*   **Working Memory and Cognitive Control (Primary Function):**
    The **caudate** receives **prefrontal** and **parietal** cortical
    input and is involved in **working memory, cognitive control, and
    goal-directed behavior**. Its **dysfunction** produces
    **cognitive and psychiatric symptoms** — the **cognitive/
    psychiatric** component of **Huntington's disease**.

*   **Goal-Directed Behavior (Cognitive Function):** The **caudate**
    (with the **ventral striatum**) is involved in **goal-directed
    behavior** — the **flexible, outcome-based** selection of
    actions. Its **dysfunction** contributes to the **cognitive
    rigidity** of **Huntington's disease** and the **tics** of
    **Tourette syndrome**.

*   **Habit Learning (with Putamen):** The **caudate** (with the
    **putamen**) is involved in **habit learning** — the **gradual
    shift** from **goal-directed** to **habitual** behavior. Its
    **dopaminergic input** from the **substantia nigra** is essential
    for this **reinforcement learning**. The **caudate** is more
    **cognitive/associative** in habit learning; the **putamen** is
    more **motor/sensorimotor**.

*   **Language (Left Caudate — Contested):** The **left caudate**
    has been reported to participate in **language** (via the
    **cortico-striatal loop**), contributing to **procedural
    language processing** — but this is **weak**, **contested**, and
    **not a strong basis for classification** (see *Lateralization
    Notes*).

*   **Tourette Syndrome (Caudate Dysfunction):** The **caudate** is
    **dysfunctional** in **Tourette syndrome** — producing **tics**
    (motor and vocal). The **caudate** is part of the
    **cortico-striato-thalamo-cortical** circuit that **gates** the
    **tics**, and its **dysfunction** contributes to the **loss of
    inhibitory control** over tics.

*   **OCD (Caudate Dysfunction, with Ventral Striatum):** The
    **caudate** (with the **ventral striatum**) is **dysfunctional**
    in **OCD** — contributing to **obsessions and compulsions**. The
    **cortico-striato-thalamo-cortical** loop is the **target** of
    **OCD pathophysiology** and **DBS**.

*   **NOT a motor processor in the classical sense.** The **caudate**
    is **cognitive/associative** — it **gates** cognitive processes
    (working memory, goal-directed behavior) rather than **computing**
    them. The **putamen** is the **motor/sensorimotor** half of the
    dorsal striatum.

**The unifying theme:** the caudate is the **cognitive/associative
half** of the dorsal striatum — the **working memory, cognitive
control, and goal-directed behavior** component that is **most
affected** in **Huntington's disease**, **dysfunctional** in
**Tourette syndrome** and **OCD**, and **weakly lateralized** for
**language** (left) and **spatial memory** (right). It is **SLEA-
free**, **strict-mirror**, and **fully wired** — but its **output
targets** (the **GPe/GPi**) are a **documented gap** in the sibling
`globus_pallidus` container.

Associated Disorders
--------------------
Caudate disorders are **cognitive, psychiatric, and hyperkinetic**:

*   **Huntington's Disease (Signature Disorder):** **Caudate
    degeneration** (especially the **caudate head**) is the
    **neuropathological hallmark** of **Huntington's disease** —
    producing **chorea** (hyperkinetic movements), **cognitive
    decline** (working memory, executive function), and **psychiatric
    symptoms** (depression, irritability, psychosis). The **caudate
    head atrophy** is the **classic imaging finding** in HD — it is
    visible on **MRI** as **enlarged lateral ventricles** with a
    **"boxcar" appearance**. **This is the caudate's signature
    clinical association** — more than any other structure, the
    caudate is **defined clinically by its role in Huntington's
    disease**.

*   **Tourette Syndrome (Caudate Dysfunction):** The **caudate** is
    **dysfunctional** in **Tourette syndrome** — producing **tics**
    (motor and vocal). The **cortico-striato-thalamo-cortical**
    circuit is the **target** of Tourette pathophysiology, and the
    **caudate** (especially the **head**) is the **anatomical
    substrate** of the **tics**. **Caudate volume reduction** has
    been reported in Tourette syndrome.

*   **OCD (Caudate Dysfunction, with Ventral Striatum):** The
    **caudate** (with the **ventral striatum**) is **dysfunctional**
    in **OCD** — contributing to **obsessions and compulsions**.
    **Caudate hyperactivity** has been reported in OCD, and the
    **cortico-striato-thalamo-cortical** loop is the **target** of
    **OCD DBS**.

*   **Cognitive Impairment (Caudate Dysfunction):** **Caudate
    dysfunction** contributes to **working memory** and **executive
    function** deficits in **neurodegenerative disease** (Huntington's,
    Parkinson's, Alzheimer's) and in **focal lesions** (stroke,
    tumor). The **caudate** is part of the **cognitive/associative**
    cortico-striatal loop.

*   **Attention-Deficit/Hyperactivity Disorder (Caudate Dysfunction —
    Contested):** Some studies report **caudate dysfunction** in
    **ADHD** — contributing to **attention and impulse control**
    deficits. The evidence is **mixed**, and the **caudate's role**
    in ADHD is **not established** as a primary substrate.

*   **Language Deficits (Left Caudate — Contested):** The **left
    caudate** has been reported to be involved in **procedural
    language processing** — its **dysfunction** may contribute to
    **language deficits** in **Huntington's disease** and in
    **left caudate lesions**. The evidence is **weak** and
    **contested**.

**What is NOT here:** The caudate is **not** the substrate for
**Parkinson's disease** (that is the **putamen** — the **most
affected** striatal structure in PD), **dystonia** (that is the
**putamen**), **addiction** (that is the **nucleus accumbens** —
ventral striatum), **depression** (that is the **nucleus accumbens**),
or **Kluver-Bucy syndrome** (that is the **amygdala**). Its clinical
footprint is **cognitive/psychiatric** (Huntington's, Tourette's,
OCD, cognitive impairment) — a **distinct category** from the
**putamen's motor** footprint.

Lateralization Notes
--------------------
This is the **left** caudate nucleus module. The caudate is
**bilaterally symmetric** and **largely non-lateralized** — **and it
carries NO extended-amygdala warning**:

*   **Bilateral Cognitive Functions:** Each caudate projects
    **ipsilaterally** to the GPe/GPi. The two sides are
    **functionally symmetric** for cognitive functions. **Huntington's
    disease** is **bilateral** — the **caudate degeneration** is
    **bilateral** (though often **asymmetric** in severity).

*   **Weak Lateralization (Contested — Language vs. Spatial):** The
    **caudate** has been reported to show **subtle** lateralization
    — **left caudate** for **language** (via the cortico-striatal
    loop, contributing to **procedural language processing**) and
    **right caudate** for **spatial navigation** (contributing to
    **spatial working memory**). Both are **weak** and **contested**,
    documented as **prose**, **not** as a strong classification
    basis. **The weak lateralization is NOT a rationale for a prose
    asymmetry** — the caudate is a **strict mirror** at the
    structural level.

*   **NO Extended-Amygdala Warning (strict mirror with no warning):**
    The caudate has **NO extended-amygdala relationship**, **NO SLEA
    overlap**, and **NO amygdala-lateralization warning**. The
    **caudate tail** ends at the **amygdala** — a **topographic**
    relationship (the tail's terminal point), **not** an **SLEA**
    relationship. Consumers must **not** import amygdala-lateralization
    claims into the caudate — **there is no anatomical relationship**
    to support them. **The warning gradient that runs through the
    ventral striatum and nucleus accumbens does NOT apply to this
    module** — the caudate is a **strict mirror with no warning**,
    matching the **dorsal striatum container**.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module** — **not** to the caudate. **The caudate has no
    SLEA relationship** — the **caudate tail's terminal point at the
    amygdala** is a **topographic** fact, **not** an **extended-
    amygdala** relationship. Consumers must **not** import the
    right-amygdala fear association into the caudate — the caudate
    is **SLEA-free**.

**A consumer that assumes "left caudate = right caudate" will be
structurally and functionally correct** — the two sides are
**largely symmetric**, no **strong** lateralized syndrome has been
demonstrated, and the **weak** lateralization reported for language
and spatial memory is **contested**, not a strong classification
basis. The caudate is a **strict-mirror pair with no warning** —
matching the **dorsal striatum container**. **This is the first
striatum-side leaf with NO warning** — the warning gradient runs
**only through the ventral side** of the striatum.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Left side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../diencephalon/``, or any other container.
    The caudate's relationships to the substantia nigra, subthalamic
    nucleus, globus pallidus, and amygdala are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **C-shape
    subdivisions** (head, body, tail) and the **striosome/matrix
    compartments** are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    subdivision-level detail through the references.
*   **Cognitive/associative half of the dorsal striatum — NOT the
    putamen.** The **caudate** is the **cognitive/associative**
    component; the **putamen** is the **motor/sensorimotor**
    component. Consumers must not conflate the two — they are
    **functionally distinct** and **clinically distinct**
    (Huntington's vs. Parkinson's).
*   **C-shape subdivisions as prose, not children.** The **head**,
    **body**, and **tail** are **topographic subdivisions** of a
    single **C-shaped** structure, not separate nuclei. The **head**
    is the **most affected** in Huntington's disease; the **tail**
    ends at the **amygdala** (a **topographic** relationship, not an
    **SLEA** relationship).
*   **NO extended-amygdala warning — strict mirror with no warning.**
    The caudate has **NO SLEA overlap**, **NO amygdala relationship**
    (the **tail's terminal point** is **topographic**, not **SLEA**),
    and **NO amygdala-lateralization warning**. **This is the first
    striatum-side leaf with NO warning** — the warning gradient runs
    **only through the ventral side** of the striatum.
*   **The GPe/GPi are a documented gap — the caudate's output targets
    are NOT wired.** The **caudate** projects to the **GPe** and
    **GPi**, but those are a **documented gap** in the **parent**
    `globus_pallidus` container. Consumers that need the caudate's
    output must resolve the GPe/GPi functions as **prose** in the
    parent `globus_pallidus` module.
*   **Not the substantia nigra — midbrain input.** The substantia
    nigra provides dopaminergic input to the caudate (nigrostriatal
    pathway). It is a **midbrain** structure, not a caudate child.
    The **caudate** is **less affected** than the **putamen** in
    **Parkinson's disease**.
*   **Not the putamen — sibling.** The putamen is the **motor/
    sensorimotor** half; the caudate is the **cognitive/associative**
    half. They are **siblings** under the dorsal striatum.
*   **Not the internal capsule — white matter.** The internal capsule
    **separates** the caudate from the putamen, but it is **white
    matter** under ``.../left/white_matter/`` — **not** a caudate
    child.
*   **Huntington's disease as the signature disorder.** **Caudate
    degeneration** (especially the **head**) is the **neuropathological
    hallmark** of HD. The **caudate head atrophy** is the **classic
    imaging finding** — it is **visible on MRI** as **enlarged lateral
    ventricles** with a **"boxcar" appearance**.
*   **No ``AREA_PATHS`` hop.** The caudate is a local leaf under the
    dorsal striatum, not a cross-listed leaf.
*   **No nested cross-listing.** The caudate has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with right caudate — strict mirror with NO
    warning.** Left and right caudate modules are **structurally
    identical** — same leaf status, same C-shape subdivisions (head,
    body, tail) as prose, same Huntington's signature disorder, same
    GPe/GPi documented-gap note, same substantia nigra input note,
    same **no extended-amygdala warning**. **The caudate is the first
    striatum-side leaf with NO warning** — the warning gradient runs
    **only through the ventral side**.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.left.subcortical.basal_ganglia.striatum.dorsal_striatum import caudate_nucleus

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.left.subcortical."
        "basal_ganglia.striatum.dorsal_striatum.caudate_nucleus"
    )

**Do not** assume the caudate is the **putamen**. The **caudate** is
the **cognitive/associative** half; the **putamen** is the **motor/
sensorimotor** half. They are **functionally distinct** (Huntington's
vs. Parkinson's).

**Do not** assume the caudate is the **ventral striatum**. The
**caudate** is the **dorsal striatum's cognitive/associative**
component; the **ventral striatum** is the **limbic/reward/olfactory**
subsystem. They are **different striatal subsystems**.

**Do not** assume the caudate has **structural children**. It is a
**leaf**. The **C-shape subdivisions** (head, body, tail) and the
**striosome/matrix compartments** are **prose only** — they are not
wired as modules.

**Do not** assume the caudate **contains** the GPe/GPi. Those are the
**output targets** of the caudate, but they are a **documented gap**
in the **parent** `globus_pallidus` container. They are **not**
caudate children.

**Do not** assume the caudate **contains** the substantia nigra or
subthalamic nucleus. Those are **midbrain** and **diencephalic**
structures — functionally related but structurally separate.

**Do not** assume the caudate **contains** the amygdala. The **caudate
tail** ends at the **amygdala** — a **topographic** relationship
(the tail's terminal point), **not** a **structural** relationship.
The caudate is **SLEA-free**.

**Do not** import **amygdala-lateralization claims** into the caudate.
**The caudate has NO extended-amygdala relationship** — the SLEA
overlap belongs to the **ventral striatum** and **ventral pallidum**.
**This is the first striatum-side leaf with NO warning** — the
warning gradient runs **only through the ventral side** of the
striatum.

Iterating the caudate's (empty) children (recommended consumer
pattern)::

    CAUDATE_CHILDREN = ()
    # The caudate is a leaf. Head, body, tail, and striosome/matrix
    # are prose, not modules.

Reaching the caudate's C-shape subdivisions (recommended consumer
pattern — NOTE: prose, not modules)::

    # The caudate has THREE classical subdivisions, all PROSE:
    #
    #   head (caput)  -> anterior, bulbous; most affected in HD
    #   body (corpus) -> middle; along the thalamus
    #   tail (cauda)  -> posterior; ends at the amygdala (topographic)
    #
    # Do NOT attempt to resolve "caudate_head", "caudate_body", or
    # "caudate_tail" paths — they do not exist in the tree.

Reaching the caudate's output targets (recommended consumer pattern —
NOTE the GAP)::

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
    # The caudate is LESS affected than the putamen in Parkinson's
    # disease — the putamen is the "most affected" striatal structure
    # in PD.

Reaching the amygdala (recommended consumer pattern — NOTE the
topographic-only relationship)::

    # The caudate tail ends at the amygdala — a TOPOGRAPHIC
    # relationship (the tail's terminal point), NOT a structural or
    # SLEA relationship:
    #
    #   subcortical.medial_temporal_lobe.amygdala
    #
    # The caudate is SLEA-FREE. Do NOT import amygdala-lateralization
    # claims into the caudate.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        cd_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.striatum.dorsal_striatum.caudate_nucleus"
        )
        # resolve cd_path through the memory/recall layer

References
----------
*   **Canonical caudate anatomy:** Graybiel, A.M. (2008). "Habits,
    rituals, and the evaluative brain." *Annual Review of
    Neuroscience* 31:359–387. (Definitive functional overview;
    caudate/putamen distinction; striosome/matrix compartments.)
*   **Caudate/putamen functional distinction:** Alexander, G.E.,
    DeLong, M.R., Strick, P.L. (1986). "Parallel organization of
    functionally segregated circuits linking basal ganglia and
    cortex." *Annual Review of Neuroscience* 9:357–381. (Parallel
    cortico-striatal loops; caudate → cognitive/associative,
    putamen → motor/sensorimotor.)
*   **Huntington's disease (caudate):** Vonsattel, J.P., DiFiglia, M.
    (1998). "Huntington disease." *Journal of Neuropathology and
    Experimental Neurology* 57:369–384. (Definitive caudate
    degeneration in HD; head atrophy is the imaging hallmark.)
*   **Caudate head atrophy on MRI:** Aylward, E.H., et al. (1994).
    "Longitudinal change in basal ganglia volume in patients with
    Huntington's disease." *Neurology* 44:1971–1975. (Caudate head
    atrophy; "boxcar" appearance of lateral ventricles.)
*   **Tourette syndrome (caudate):** Leckman, J.F., et al. (2010).
    "Tourette syndrome: the self under siege." *Journal of Child
    Neurology* 25:1155–1162. (Caudate dysfunction in Tourette
    syndrome; caudate volume reduction.)
*   **OCD (caudate):** Saxena, S., Rauch, S.L. (2000). "Functional
    neuroimaging and the neuroanatomy of obsessive-compulsive
    disorder." *Psychiatric Clinics of North America* 23:563–586.
    (Caudate hyperactivity in OCD; cortico-striato-thalamo-cortical
    loop.)
*   **Substantia nigra (contrast — midbrain input):** Braak, H., et
    al. (2003). "Staging of brain pathology related to sporadic
    Parkinson's disease." *Neurobiology of Aging* 24:197–211.
    (Substantia nigra as the source of dopaminergic input to the
    caudate; the caudate is less affected than the putamen in PD.)
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
*   **Amygdala (contrast — topographic relationship only):** Amaral,
    D.G., Insausti, R. (1990). "The hippocampal formation." In *The
    Human Nervous System* (Paxinos, G., ed.). (The caudate tail ends
    at the amygdala — a topographic relationship, not a structural
    or SLEA relationship.)
*   **Left caudate language (weak, contested):** Ullman, M.T. (2004).
    "Contributions of memory circuits to language: the
    declarative/procedural model." *Cognition* 92:231–270. (Left
    caudate in language; procedural memory.)
*   **Right caudate spatial memory (contrast):** Postle, B.R.,
    D'Esposito, M. (1999). "Dissociation of human caudate nucleus
    activity during spatial and verbal working memory." *Cognitive
    Brain Research* 7:571–580. (Right caudate and spatial working
    memory; weak, contested lateralization.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical
    pathway to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association does
    **not** apply to the caudate — the caudate is **SLEA-free**, and
    the **caudate tail's terminal point at the amygdala** is a
    **topographic** fact, not an **SLEA** relationship.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Caudate nucleus in overview.)
*   NeuroNames — Caudate nucleus (left); FMA — Caudate nucleus (left
    member).
"""