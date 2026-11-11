"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.striatum.dorsal_striatum.putamen
======================================================================================================================================

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
                            └── putamen   <-- THIS MODULE

**Primary synonym:** Putamen; putamen nucleus; "the shell" (Latin
*putamen*); dorsal striatum (with the caudate); neostriatum
(classical — with the caudate).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**GABAergic medium spiny neuron nucleus** — the **motor/
sensorimotor** component of the **dorsal striatum** (with the
**caudate** as the **cognitive/associative** component).
**Part of:** The **dorsal striatum** container — specifically, the
**motor/sensorimotor** half (with the **caudate** as the
**cognitive/associative** half). The **dorsal striatum** is the
**motor/cognitive** half of the **striatum** (with the **ventral
striatum** as the **limbic/reward/olfactory** half).
**Structural parent:** ``.../right/subcortical/basal_ganglia/striatum/dorsal_striatum/``
→ **direct child** of the dorsal striatum container.
**Structural children:** **None.** This is a **leaf** module. The
**anterior/posterior** and **dorsal/ventral** subdivisions and the
**striosome/matrix** compartments are documented as **prose**, not as
structural children.
**Boundary status (the MOTOR/SENSORIMOTOR half of the dorsal striatum
— NOT the caudate):** **Boundary case — the putamen is the MOTOR/
SENSORIMOTOR component; the CAUDATE is the COGNITIVE/ASSOCIATIVE
component.** The **putamen** and the **caudate** are the two
**classical subdivisions** of the **dorsal striatum** — both **fully
wired leaves** under ``.../dorsal_striatum/``. They are
**cytoarchitecturally continuous** around the **anterior** and
**inferior** margins of the internal capsule (the **caudate-putamen
junction**), but they are **functionally distinct**:
*   **Putamen** (this module) — **motor/sensorimotor**: action
    selection, movement initiation, motor learning, habit learning.
    Receives **sensorimotor cortical** input. **Parkinson's
    disease** (the putamen is the **most affected** striatal
    structure), **dystonia**.
*   **Caudate** (``.../caudate_nucleus/``) — **cognitive/
    associative**: working memory, cognitive control, goal-directed
    behavior, language (left — contested). Receives **prefrontal**
    and **parietal** cortical input. **Huntington's disease** (the
    caudate is the **most affected** striatal structure),
    **Tourette syndrome**, **OCD** (with the ventral striatum).
Consumers must **not** treat the putamen and caudate as
**interchangeable** — they are **functionally distinct** (motor vs.
cognitive), **clinically distinct** (Parkinson's vs. Huntington's),
and **anatomically distinct** (though **cytoarchitecturally
continuous**).
**Boundary status (NO extended-amygdala relationship — the putamen is
SLEA-free):** **Boundary case — the putamen has NO extended-amygdala
relationship, NO SLEA overlap, and NO amygdala-lateralization
warning.** The **SLEA overlap** belongs to the **ventral striatum**
(via the **nucleus accumbens**) and the **ventral pallidum** — **not**
to the putamen. The putamen is a **dorsal striatum** structure — the
**motor/sensorimotor** subsystem — and the **SLEA** is a **limbic**
continuum. Consumers must **not** import amygdala-lateralization
claims into the putamen — **there is no anatomical relationship** to
support them. **The warning gradient that runs through the ventral
striatum and nucleus accumbens does NOT apply to this module** — the
putamen is a **strict mirror with no warning**, matching the
**dorsal striatum container** and the **caudate nucleus**.
**Boundary status (subdivisions — LESS STUDIED than the caudate's
head/body/tail, documented as PROSE, not as structural children):**
**Boundary case — the putamen has LESS WELL-DEFINED subdivisions than
the caudate, and NONE of them are as clinically important as the
caudate head.** The putamen is a **lens-shaped** nucleus — **more
homogeneous** than the **C-shaped** caudate — and its classical
subdivisions are **topographic** rather than **functional**:
*   **Anterior/posterior** — the **anterior** putamen is more
    **associative** (prefrontal input); the **posterior** putamen is
    more **sensorimotor** (motor and somatosensory input). This
    **anterior-posterior gradient** is the **most useful functional
    subdivision** — but it is **graded**, not sharp.
*   **Dorsal/ventral** — the **dorsal** putamen is more
    **sensorimotor**; the **ventral** putamen is more
    **limbic-adjacent** (transitional to the ventral striatum). This
    is a **graded** distinction, not a sharp boundary.
*   **Striosome/matrix** — the same **chemical compartments** as the
    caudate: **striosomes** (patches, limbic-related) and **matrix**
    (sensorimotor-related). The **matrix** is **dominant** in the
    putamen (more than in the caudate), reflecting the putamen's
    **sensorimotor** role.
**These subdivisions are prose, not structural children.** The tree
wires the putamen as a **single leaf** — the subdivisions are
**topographic** (anterior-posterior, dorsal-ventral) or **chemical**
(striosome/matrix), not **separate nuclei**. Consumers that need
subdivision-level resolution should consult the references, not the
tree. **The putamen is more homogeneous than the caudate** — there is
**no putamen equivalent of the caudate head** (the **most clinically
important** caudate subdivision for **Huntington's disease**). The
putamen's clinical signature is **Parkinson's disease** (a
**whole-putamen** dopaminergic denervation, not a **focal** lesion).
**Boundary status (not the caudate — sibling):** **Boundary case —
the caudate is a SIBLING under the dorsal striatum, not a child or
parent of the putamen.** The **caudate** is the **cognitive/
associative** half; the **putamen** is the **motor/sensorimotor**
half. They are **cytoarchitecturally continuous** (around the
internal capsule) but **functionally distinct**. Consumers that need
the **cognitive** component resolve ``.../caudate_nucleus/``;
consumers that need the **motor** component resolve **this module**.
**Boundary status (not the ventral striatum — cousin):** **Boundary
case — the ventral striatum (nucleus accumbens + olfactory tubercle)
is a COUSIN of the putamen, not a parent or child.** The **ventral
striatum** is the **limbic/reward/olfactory** subsystem; the
**putamen** (with the caudate) is the **motor/cognitive** subsystem.
They are **structurally separate** (dorsal vs. ventral) and
**functionally distinct**. Consumers that need the **limbic/reward**
subsystem resolve ``.../striatum/ventral_striatum/``; consumers that
need the **motor** subsystem resolve **this module**. **The SLEA
warning belongs to the ventral striatum and ventral pallidum — NOT to
the putamen.**
**Boundary status (not the globus pallidus — the GPe/GPi are a
DOCUMENTED GAP):** **Boundary case — the putamen projects to the
GPe/GPi, but those are a DOCUMENTED GAP in the `globus_pallidus`
container.** The **putamen** (with the caudate) projects to the
**GPe** and **GPi** — the **direct pathway** (striatum → GPi →
thalamus) and the **indirect pathway** (striatum → GPe → STN → GPi →
thalamus). But the **GPe and GPi are NOT wired** — they are a
**documented structural gap** in the **parent** `globus_pallidus`
container. **This gap is especially consequential here**, because the
**putamen's entire output** goes to the **unwired GPe/GPi** — the
**putamen is wired**, but its **output targets are not**. The
**putamen → GPe/GPi** circuit is the **motor circuit** that is
disrupted in **Parkinson's disease** and **dystonia** — the
**unwired GPe/GPi** are the **anatomical substrate** of the **motor
symptoms**. Consumers that need the putamen's output must resolve the
GPe/GPi functions as **prose** in the **parent** `globus_pallidus`
module, **not** here.
**Boundary status (not the substantia nigra — midbrain dopaminergic
INPUT):** **Boundary case — the substantia nigra is the
DOPAMINERGIC INPUT to the putamen, but it is a MIDBRAIN structure,
not a putamen child.** The **substantia nigra (pars compacta)**
provides **dopaminergic input** to the **putamen** (with the
caudate) — the **nigrostriatal pathway**. Its **degeneration** in
**Parkinson's disease** affects the **putamen MORE than the
caudate** — the **putamen** loses **more** dopaminergic input and is
the **most affected** striatal structure in PD. The **substantia
nigra** is under ``.../midbrain/tegmentum/substantia_nigra/`` —
**not** under the putamen. Consumers must **not** resolve the
substantia nigra through the putamen, and must **not** treat the
putamen's dopaminergic input as intrinsic to the putamen. **The
putamen is the TARGET; the substantia nigra is the SOURCE.**
**Boundary status (not the internal capsule — white matter
separator):** **Boundary case — the internal capsule SEPARATES the
putamen from the caudate and from the globus pallidus, but it is
WHITE MATTER, not a putamen child.** The **anterior limb** of the
internal capsule separates the **putamen** from the **caudate head**;
the **posterior limb** separates the **putamen** from the **caudate
body**; the **external capsule** and **lateral medullary lamina**
separate the **putamen** from the **globus pallidus** (GPe). The
**internal capsule** is under ``.../right/white_matter/`` — **not** a
putamen child. Consumers must **not** resolve the internal capsule
through the putamen.
**Boundary status (not a single functional system — the putamen is
MORE HOMOGENEOUS than the caudate):** **Boundary case — the putamen
is a MORE HOMOGENEOUS structure than the caudate, with a DOMINANT
MOTOR/SENSORIMOTOR function.** Unlike the caudate (which has a
**functionally distinct head/body/tail**), the putamen has **graded**
subdivisions (**anterior-posterior**, **dorsal-ventral**) but a
**single dominant function** — **motor/sensorimotor**. Its **clinical
signature** is **Parkinson's disease**, which affects the **whole
putamen** (via dopaminergic denervation), not a **focal** region.
Consumers can treat the putamen as **functionally more uniform** than
the caudate — but must still recognize the **anterior-posterior** and
**dorsal-ventral** gradients.

Overview
--------
The putamen is the **motor/sensorimotor** component of the **dorsal
striatum** — the **lens-shaped** grey-matter nucleus that lies
**lateral** to the **globus pallidus**, **medial** to the **external
capsule**, and **inferior** to the **caudate** (from which it is
separated by the **internal capsule**). It is the **most affected
striatal structure in Parkinson's disease** (its **dopaminergic
denervation** from the **substantia nigra** is the **neuropathological
substrate** of **bradykinesia, rigidity, and tremor**), a **key node**
in the **cortico-striato-pallido-thalamo-cortical motor circuit**, and
the **anatomical substrate** of **dystonia** pathophysiology.

**The putamen is the motor/sensorimotor half of the dorsal striatum.**
The **caudate** is the **cognitive/associative** half. The two are
**cytoarchitecturally continuous** around the **anterior** and
**inferior** margins of the internal capsule (the **caudate-putamen
junction**), but they are **functionally distinct** — the **putamen**
is **motor/sensorimotor** (action selection, movement initiation,
motor learning, habit learning), and the **caudate** is **cognitive/
associative** (working memory, cognitive control, goal-directed
behavior). The tree wires them as **two separate leaves** — a
**deliberate boundary choice** reflecting their **functional and
clinical distinction**.

**The putamen is MORE HOMOGENEOUS than the caudate.** Unlike the
**C-shaped** caudate (with its **functionally distinct head/body/tail**
and its **clinically important head atrophy** in Huntington's
disease), the putamen is **lens-shaped** and **more uniform** — its
**anterior-posterior** and **dorsal-ventral** subdivisions are
**graded** rather than sharp, and its **clinical signature** is
**Parkinson's disease**, which affects the **whole putamen** (via
dopaminergic denervation), not a **focal** region.

**The putamen is SLEA-free.** The **extended amygdala (SLEA)** overlap
belongs to the **ventral striatum** (via the **nucleus accumbens**)
and the **ventral pallidum** — **not** to the putamen. **The warning
gradient that runs through the ventral striatum and nucleus accumbens
does NOT apply to this module** — the putamen is a **strict mirror
with no warning**, matching the **dorsal striatum container** and the
**caudate nucleus**.

**The putamen's OUTPUT goes to the GPe/GPi — which are a documented
gap in the sibling `globus_pallidus` container.** The **putamen →
GPe/GPi** circuit is the **motor circuit** that is disrupted in
**Parkinson's disease** and **dystonia** — the **unwired GPe/GPi**
are the **anatomical substrate** of the **motor symptoms**.

**The putamen is a paired structure.** Each hemisphere has its own
putamen, with **ipsilateral** cortical, thalamic, and dopaminergic
input. The two sides are **bilaterally symmetric** and **largely
non-lateralized** — the **motor/sensorimotor** functions are
**bilateral**. **Parkinson's disease** is **bilateral** (though often
**asymmetric** in presentation). No **strong lateralized syndrome**
has been documented for the putamen. See *Lateralization Notes*.

Subdivisions (prose, not structural children)
---------------------------------------------
The putamen has **less well-defined subdivisions** than the caudate,
and **none** of them is as clinically important as the **caudate
head**:

*   **Anterior-posterior gradient** — the **anterior** putamen is
    more **associative** (prefrontal and premotor input); the
    **posterior** putamen is more **sensorimotor** (primary motor and
    somatosensory input). This is the **most useful functional
    subdivision** — but it is **graded**, not sharp.

*   **Dorsal-ventral gradient** — the **dorsal** putamen is more
    **sensorimotor**; the **ventral** putamen is more
    **limbic-adjacent** (transitional to the ventral striatum). This
    is a **graded** distinction, not a sharp boundary.

*   **Striosome/matrix compartments** — the same **chemical
    compartments** as the caudate: **striosomes** (**patches**,
    limbic-related) and **matrix** (sensorimotor-related). The
    **matrix** is **dominant** in the putamen (more than in the
    caudate), reflecting the putamen's **sensorimotor** role.

**These subdivisions are prose, not structural children.** The tree
wires the putamen as a **single leaf** — the subdivisions are
**topographic** (anterior-posterior, dorsal-ventral) or **chemical**
(striosome/matrix), not **separate nuclei**. Consumers that need
subdivision-level resolution should consult the references, not the
tree. **The putamen is more homogeneous than the caudate** — there is
**no putamen equivalent of the caudate head** (the **most clinically
important** caudate subdivision for **Huntington's disease**). The
putamen's clinical signature is **Parkinson's disease** (a
**whole-putamen** dopaminergic denervation, not a **focal** lesion).

The Putamen / Caudate Boundary
------------------------------
This is the **most consequential boundary** in the module:

*   **Putamen** (this module) — the **motor/sensorimotor** half of the
    dorsal striatum. **Parkinson's disease**, **dystonia**.

*   **Caudate** (``.../caudate_nucleus/``) — the **cognitive/
    associative** half of the dorsal striatum. **Huntington's
    disease**, **Tourette syndrome**, **OCD**.

**They are cytoarchitecturally continuous but functionally distinct.**
The **putamen** and **caudate** are **separated** by the **internal
capsule** (the **anterior limb** separates the putamen from the
caudate head; the **posterior limb** separates the putamen from the
caudate body), but they are **continuous** around the **anterior**
and **inferior** margins of the capsule. The tree wires them as **two
separate leaves** — a **deliberate boundary choice** reflecting their
**functional distinction** and their **clinical distinction**.

**The clinical distinction is diagnostic:**
- **Putamen** → **Parkinson's disease** (bradykinesia, rigidity,
  tremor).
- **Caudate** → **Huntington's disease** (chorea, cognitive decline,
  psychiatric symptoms).

The Putamen / Ventral Striatum Boundary
---------------------------------------
This is the **dorsal/ventral** boundary of the striatum:

*   **Putamen** (this module) — the **dorsal striatum** (motor/
    sensorimotor). Part of the **motor/cognitive** subsystem.

*   **Ventral striatum** (``.../striatum/ventral_striatum/``) — the
    **limbic/reward/olfactory** subsystem (nucleus accumbens +
    olfactory tubercle). **SLEA-bearing** half.

**They are cousins (dorsal vs. ventral striatum).** The **putamen** is
the **motor** half of the **dorsal** striatum; the **ventral
striatum** is the **limbic/reward** half. Consumers that need the
**motor** subsystem resolve **this module**; consumers that need the
**limbic/reward** subsystem resolve
``.../striatum/ventral_striatum/``. **The SLEA warning belongs to the
ventral striatum and ventral pallidum — NOT to the putamen.**

The Putamen / Substantia Nigra Boundary
---------------------------------------
This is the **dopaminergic input** boundary:

*   **Substantia nigra** —
    ``.../midbrain/tegmentum/substantia_nigra/`` — the **dopaminergic**
    (pars compacta) and **GABAergic** (pars reticulata) **midbrain**
    nucleus. Its **pars compacta** provides **dopaminergic input to
    the putamen** (and caudate) — the **nigrostriatal pathway**. Its
    **pars reticulata** receives **striatal output** from the
    **striosomes** of the putamen (the **striatonigral** projection).

*   **Putamen** (this module) — the **dopaminergic TARGET** (via the
    nigrostriatal pathway). **Telencephalic**.

**The substantia nigra is NOT a putamen child.** It is a **midbrain**
structure — functionally related (dopaminergic input to the putamen)
but structurally separate. **The putamen is the TARGET; the substantia
nigra is the SOURCE.** The **putamen is the most affected** striatal
structure in **Parkinson's disease** — it loses **more** dopaminergic
input than the **caudate**, and its **dopaminergic denervation** is
the **neuropathological substrate** of **bradykinesia, rigidity, and
tremor**.

The Putamen / Globus Pallidus Boundary
--------------------------------------
This is the **output-target** boundary — **the GPe/GPi are a
documented gap**:

*   **Putamen** (this module) — the **input** structure (motor/
    sensorimotor half of the dorsal striatum). **Wired**.

*   **Globus pallidus** (``.../basal_ganglia/globus_pallidus/``) — the
    **output** structure. Its **dorsal segments** (GPe, GPi) are the
    **putamen's output targets**, but they are **NOT wired** — a
    **documented gap** in the parent `globus_pallidus` container.
    Only the **ventral pallidum** is wired.

**The putamen → GPe/GPi circuit is the motor circuit.** The **direct
pathway** (putamen → GPi → thalamus) and the **indirect pathway**
(putamen → GPe → STN → GPi → thalamus) both go through the **GPe/GPi**
— which are **not wired**. The **unwired GPe/GPi** are the
**anatomical substrate** of the **motor symptoms** of **Parkinson's
disease** and **dystonia**.

**Consumers that need the putamen's output** must resolve the GPe/GPi
functions as **prose** in the **parent** `globus_pallidus` module —
**not** here, and **not** as structural children.

The Putamen / Internal Capsule Boundary
---------------------------------------
This is the **white-matter separation** boundary:

*   **Internal capsule** — ``.../right/white_matter/`` — the
    **white-matter tract** that **separates** the **putamen** from
    the **caudate** and from the **globus pallidus**:
    *   **Anterior limb** — separates the **putamen** from the
        **caudate head**.
    *   **Posterior limb** — separates the **putamen** from the
        **caudate body**.
    *   **External capsule** and **lateral medullary lamina** —
        separate the **putamen** from the **globus pallidus (GPe)**.

*   **Putamen** (this module) — the **grey-matter structure** that the
    internal capsule **passes beside**.

**The internal capsule is NOT a putamen child.** It is **white matter**
under ``.../right/white_matter/`` — **not** a putamen component.

Function in the Human Brain
---------------------------
The putamen has a **dominant motor/sensorimotor function** with
**graded subdivisions**:

*   **Action Selection and Movement Initiation (Primary Function):**
    The **putamen** receives **sensorimotor cortical** input and is
    involved in **action selection, movement initiation, and motor
    learning**. Its **dopaminergic denervation** in **Parkinson's
    disease** produces **bradykinesia, rigidity, and tremor** — the
    **signature motor symptoms** of PD.

*   **Habit Learning (Putamen + Caudate):** The **putamen** (with the
    **caudate**) is involved in **habit learning** — the **gradual
    shift** from **goal-directed** to **habitual** behavior. Its
    **dopaminergic input** from the **substantia nigra** is essential
    for this **reinforcement learning**. The **putamen** is the **more
    motor** component of habit learning; the **caudate** is the **more
    cognitive** component.

*   **Dystonia (Putamen Dysfunction):** The **putamen** is
    **dysfunctional** in **dystonia** — producing **sustained muscle
    contractions and abnormal postures**. **Dystonia** is often
    **dopa-responsive** (in children) — the **putamen's** dopaminergic
    signaling is the **therapeutic target**.

*   **Sensorimotor Integration (Anterior-Posterior Gradient):** The
    **posterior putamen** receives **primary motor** and
    **somatosensory** input and is the **sensorimotor core**; the
    **anterior putamen** receives **premotor** and **associative**
    input and is the **transitional** zone to the **caudate**.

*   **NOT a cognitive processor in the classical sense.** The
    **putamen** is **motor/sensorimotor** — it **gates** motor
    processes (action selection, movement initiation) rather than
    **computing** them. The **caudate** is the **cognitive/
    associative** half of the dorsal striatum.

**The unifying theme:** the putamen is the **motor/sensorimotor half**
of the dorsal striatum — the **action selection, movement initiation,
and habit learning** component that is **most affected** in
**Parkinson's disease** (dopaminergic denervation), **dysfunctional**
in **dystonia**, and **more homogeneous** than the caudate. It is
**SLEA-free**, **strict-mirror**, and **fully wired** — but its
**output targets** (the **GPe/GPi**) are a **documented gap** in the
sibling `globus_pallidus` container.

Associated Disorders
--------------------
Putamen disorders are **motor and movement-related**:

*   **Parkinson's Disease (Signature Disorder):** **Putamen
    dopaminergic denervation** (substantia nigra → putamen) is the
    **neuropathological substrate** of **Parkinson's disease** motor
    symptoms — **bradykinesia, rigidity, and tremor**. The **putamen**
    is the **most affected** striatal structure in PD (more than the
    caudate). **Dopaminergic loss** in the **putamen** is **earlier**
    and **more severe** than in the **caudate** — the **putamen's**
    dopaminergic denervation is the **signature clinical association**
    of PD. **This is the putamen's signature clinical association** —
    more than any other structure, the putamen is **defined clinically
    by its role in Parkinson's disease**.

*   **Dystonia (Putamen Dysfunction):** The **putamen** is
    **dysfunctional** in **dystonia** — producing **sustained muscle
    contractions and abnormal postures**. **Dystonia** is often
    **dopa-responsive** (in children) — the **putamen's** dopaminergic
    signaling is the **therapeutic target**. **Putamen lesions**
    (from stroke, tumor, or metabolic disease) can produce
    **dystonia**.

*   **Habit Learning Deficits (Putamen Dysfunction):** **Putamen
    dysfunction** impairs **habit formation** (with the **caudate**),
    contributing to **procedural learning** deficits — especially in
    **Parkinson's disease** and **Huntington's disease**.

*   **Hemiballismus (Contrast — NOT Putamen):** **Hemiballismus** —
    violent, involuntary **proximal limb movements** — is caused by a
    **lesion of the subthalamic nucleus (STN)**, **not** the putamen.
    But the **putamen** is the **upstream** structure (putamen → GPe →
    STN → GPi → thalamus), so **putamen dysfunction** can
    **contribute** to **hemiballismus** indirectly. The STN is
    **diencephalic** (not a putamen child), and this is a **contrast**
    disorder.

*   **Vascular Lesions (Putamen):** **Putamen infarcts** (from
    **lenticulostriate artery** disease) can produce **contralateral
    hemiparesis**, **hemianesthesia**, and **dystonia** — the
    **putamen** is in the **lenticulostriate territory**, and its
    **vascular lesions** are **clinically important**.

**What is NOT here:** The putamen is **not** the substrate for
**Huntington's disease** (that is the **caudate** — the **most
affected** striatal structure in HD), **Tourette syndrome** (that is
the **caudate**), **OCD** (that is the **caudate** and **ventral
striatum**), **addiction** (that is the **nucleus accumbens** —
ventral striatum), **depression** (that is the **nucleus accumbens**),
or **Kluver-Bucy syndrome** (that is the **amygdala**). Its clinical
footprint is **motor** (**Parkinson's disease**, **dystonia**,
**habit learning deficits**) — a **distinct category** from the
**caudate's cognitive** footprint and the **ventral striatum's
limbic/reward** footprint.

Lateralization Notes
--------------------
This is the **right** putamen module. The putamen is **bilaterally
symmetric** and **non-lateralized** — **and it carries NO
extended-amygdala warning**:

*   **Bilateral Motor Functions:** Each putamen projects
    **ipsilaterally** to the GPe/GPi. The two sides are **functionally
    symmetric** for motor functions. **Parkinson's disease** is
    **bilateral** (though often **asymmetric** in presentation) —
    **bradykinesia and rigidity** are typically **bilateral**, and
    **dopaminergic loss** is **bilateral** (though often asymmetric in
    severity).

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the putamen has **no documented strong
    left-lateralized or right-lateralized function**. **Parkinson's
    disease** is **bilateral**; **dystonia** is **bilateral** (though
    often **focal** or **segmental** in distribution, not lateralized
    to one hemisphere). **No weak lateralization** comparable to the
    caudate's **contested language/spatial** lateralization has been
    reported for the putamen. **The right putamen is not the "spatial-
    memory" side of a lateralization** — the putamen has **no
    lateralization at all**, unlike its caudate sibling.

*   **NO Extended-Amygdala Warning (strict mirror with no warning):**
    The putamen has **NO extended-amygdala relationship**, **NO SLEA
    overlap**, and **NO amygdala-lateralization warning**. The
    **SLEA overlap** belongs to the **ventral striatum** (via the
    **nucleus accumbens**) and the **ventral pallidum** — **not** to
    the putamen. Consumers must **not** import amygdala-lateralization
    claims into the putamen — **there is no anatomical relationship**
    to support them. **The warning gradient that runs through the
    ventral striatum and nucleus accumbens does NOT apply to this
    module** — the putamen is a **strict mirror with no warning**,
    matching the **dorsal striatum container** and the **caudate
    nucleus**. **The right-side module carries the same no-warning
    status** — no dedicated Usage block, no contrast reference, no
    deferral note. **The putamen has no amygdala-adjacent structure**
    at any level of its subtree — the anterior/posterior and dorsal/
    ventral gradients are **not** SLEA-bearing, and **no warning
    applies**.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module** — **not** to the putamen. **The putamen has no
    anatomical relationship to the amygdala** — the **SLEA overlap**
    is a **ventral striatum** fact, and it **does not transfer** to
    the putamen. **This is true on the right side as well** — the
    right putamen is **not** SLEA-bearing, and the right amygdala's
    fear-processing association **does not** apply to it.

**A consumer that assumes "right putamen = left putamen" will be
structurally and functionally correct** — the two sides are
**symmetric**, no **strong** lateralized syndrome has been
demonstrated, and **no weak lateralization** comparable to the
caudate's contested language/spatial lateralization has been reported.
The putamen is a **strict-mirror pair with no warning** — matching
the **dorsal striatum container** and the **caudate nucleus**. **This
is the cleanest strict-mirror pair in the entire striatum subtree**
— the putamen has **no lateralization whatsoever** (unlike the
caudate's weak, contested language/spatial lateralization), and no
SLEA warning (unlike the ventral side). The right-side module is a
**pure word-for-word mirror** of the left, with only the path,
hemisphere labels, and FMA member reference changed.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../diencephalon/``, or any other container.
    The putamen's relationships to the substantia nigra, globus
    pallidus, caudate, and internal capsule are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Leaf module — no structural children.** The **anterior/posterior**
    and **dorsal/ventral** subdivisions and the **striosome/matrix**
    compartments are documented as **prose**, not as sub-modules.
    Consumers must not assume any exist as children; resolve
    subdivision-level detail through the references.
*   **Motor/sensorimotor component — NOT the caudate.** The
    **putamen** is the **motor/sensorimotor** half of the dorsal
    striatum; the **caudate** is the **cognitive/associative** half.
    Consumers must not conflate the two — they are **functionally
    distinct**.
*   **MORE HOMOGENEOUS than the caudate.** The putamen has **graded**
    subdivisions (**anterior-posterior**, **dorsal-ventral**) but a
    **single dominant function** — **motor/sensorimotor**. There is
    **no putamen equivalent of the caudate head** (the **most
    clinically important** caudate subdivision). The putamen's
    clinical signature is **Parkinson's disease** (a **whole-putamen**
    dopaminergic denervation, not a **focal** lesion).
*   **NO extended-amygdala warning — strict mirror with no warning.**
    The putamen has **NO SLEA overlap**, **NO amygdala relationship**,
    and **NO amygdala-lateralization warning**. The **SLEA warning**
    belongs to the **ventral striatum** (nucleus accumbens) and the
    **ventral pallidum** — **not** here. **The right-side module
    carries the same no-warning status** — no dedicated Usage block,
    no contrast reference, no deferral note.
*   **The GPe/GPi are a documented gap — the putamen's output targets
    are NOT wired.** The **putamen** projects to the **GPe** and
    **GPi**, but those are a **documented gap** in the **parent**
    `globus_pallidus` container. Consumers that need the putamen's
    output must resolve the GPe/GPi functions as **prose** in the
    parent `globus_pallidus` module.
*   **Not the substantia nigra — midbrain input.** The substantia
    nigra provides dopaminergic input to the putamen (nigrostriatal
    pathway). It is a **midbrain** structure, not a putamen child. The
    **putamen is the most affected** striatal structure in
    **Parkinson's disease**.
*   **Not the internal capsule — white matter.** The internal capsule
    **separates** the putamen from the caudate and globus pallidus,
    but it is **white matter** under ``.../right/white_matter/`` —
    **not** a putamen child.
*   **Parkinson's disease as the signature disorder.** **Putamen
    dopaminergic denervation** (substantia nigra → putamen) is the
    **neuropathological substrate** of **bradykinesia, rigidity, and
    tremor**. The **putamen** is the **most affected** striatal
    structure in PD.
*   **No lateralization whatsoever.** The putamen has **no
    lateralization** — unlike its **caudate sibling**, which has a
    **weak, contested** language/spatial lateralization. The
    **right putamen** is **not** the "spatial-memory" side of a
    lateralization — the putamen has **no lateralization at all**.
*   **No ``AREA_PATHS`` hop.** The putamen is a local leaf under the
    dorsal striatum, not a cross-listed leaf.
*   **No nested cross-listing.** The putamen has no nested
    dual-framing module. It is a single leaf.
*   **Structural parity with left putamen — strict mirror with NO
    warning.** Right and left putamen modules are **structurally
    identical** — same leaf status, same subdivisions as prose, same
    Parkinson's signature disorder, same GPe/GPi documented-gap note,
    same substantia nigra input note, same **no extended-amygdala
    warning**. **The right-side module carries the same no-warning
    status** — no dedicated Usage block, no contrast reference, no
    deferral note. **This is the cleanest strict-mirror pair in the
    entire striatum subtree** — the putamen has **no lateralization
    whatsoever**, and the right module is a **pure word-for-word
    mirror** of the left.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.striatum.dorsal_striatum import putamen

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_ganglia.striatum.dorsal_striatum.putamen"
    )

**Do not** assume the putamen is the **caudate**. The **putamen** is
the **motor/sensorimotor** half; the **caudate** is the **cognitive/
associative** half. They are **functionally distinct** —
**Parkinson's** (putamen) vs. **Huntington's** (caudate).

**Do not** assume the putamen has **structural children**. It is a
**leaf**. The **anterior/posterior**, **dorsal/ventral**, and
**striosome/matrix** subdivisions are **prose only** — they are not
wired as modules.

**Do not** assume the putamen **contains** the GPe/GPi. Those are the
**output targets** of the putamen, but they are a **documented gap**
in the **parent** `globus_pallidus` container. They are **not**
putamen children.

**Do not** assume the putamen **contains** the substantia nigra. It is
a **midbrain** structure that provides **dopaminergic input** to the
putamen — functionally related but structurally separate.

**Do not** import **amygdala-lateralization claims** into the putamen.
**The putamen has NO extended-amygdala relationship** — the SLEA
overlap belongs to the **ventral striatum** and **ventral pallidum**.
**The right-side module carries the same no-warning status** — the
right putamen is **not** SLEA-bearing, and the right amygdala's
fear-processing association **does not** apply to it.

**Do not** assume the putamen has a **lateralization** comparable to
the caudate. The **putamen has NO lateralization** — unlike its
**caudate sibling**, which has a **weak, contested** language/spatial
lateralization. The **right putamen** is **not** the "spatial-memory"
side of a lateralization — the putamen has **no lateralization at
all**.

Iterating the putamen's (empty) children (recommended consumer
pattern)::

    PUTAMEN_CHILDREN = ()
    # The putamen is a leaf. The anterior/posterior, dorsal/ventral,
    # and striosome/matrix subdivisions are prose, not modules.

Reaching the putamen's output targets (recommended consumer pattern —
NOTE the GAP)::

    # The putamen projects to the GPe and GPi (the output targets).
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

    # The substantia nigra provides dopaminergic input to the putamen
    # (nigrostriatal pathway). It is a MIDBRAIN structure, not a
    # putamen child:
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # The substantia nigra is the SOURCE; the putamen is the TARGET.
    # The putamen is the "most affected" striatal structure in
    # Parkinson's disease.

Reaching the caudate (recommended consumer pattern — the sibling)::

    # The caudate is a SIBLING of the putamen — the cognitive/
    # associative half of the dorsal striatum:
    #
    #   subcortical.basal_ganglia.striatum.dorsal_striatum.caudate_nucleus
    #
    # The putamen and caudate are cytoarchitecturally continuous but
    # functionally distinct.

Reaching the internal capsule (recommended consumer pattern — NOTE
the white-matter boundary)::

    # The internal capsule separates the putamen from the caudate and
    # globus pallidus, but it is WHITE MATTER, not a putamen child:
    #
    #   white_matter.internal_capsule
    #
    # Do NOT resolve the internal capsule through the putamen.

Subdivision-level detail (not wired — consult references)::

    # The putamen's subdivisions and compartments are prose, not
    # modules:
    #   anterior-posterior -> associative vs. sensorimotor gradient
    #   dorsal-ventral     -> sensorimotor vs. limbic-adjacent gradient
    #   striosomes         -> substantia nigra pars compacta
    #   matrix             -> globus pallidus + substantia nigra pars
    #                         reticulata (dominant in putamen)
    #
    # Do not attempt to resolve these as sub-paths of the putamen.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        put_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.striatum.dorsal_striatum.putamen"
        )
        # resolve put_path through the memory/recall layer

References
----------
*   **Canonical putamen anatomy:** Alexander, G.E., DeLong, M.R.,
    Strick, P.L. (1986). "Parallel organization of functionally
    segregated circuits linking basal ganglia and cortex." *Annual
    Review of Neuroscience* 9:357–381. (Parallel cortico-striatal
    loops; putamen → motor, caudate → cognitive.)
*   **Putamen functional anatomy:** Graybiel, A.M. (2008). "Habits,
    rituals, and the evaluative brain." *Annual Review of
    Neuroscience* 31:359–387. (Putamen in motor control, action
    selection, and habit learning.)
*   **Striosome/matrix compartments:** Graybiel, A.M., Ragsdale,
    C.W. (1978). "Histochemically distinct compartments in the
    striatum of human, monkey, and cat demonstrated by
    acetylthiocholinesterase staining." *PNAS* 75:5723–5726.
    (Striosome/matrix compartments; matrix dominance in the putamen.)
*   **Putamen subdivisions:** Parent, A., Carpenter, M.B. (1996).
    *Carpenter's Human Neuroanatomy*, 9th ed. (Putamen subdivisions;
    anterior-posterior and dorsal-ventral gradients; homogeneity
    compared with the caudate.)
*   **Parkinson's disease:** Dauer, W., Przedborski, S. (2003).
    "Parkinson's disease: mechanisms and models." *Neuron*
    39:889–909. (Substantia nigra → putamen dopaminergic loss; the
    putamen is the most affected striatal structure.)
*   **Putamen dopaminergic loss is earlier and more severe than
    caudate:** Kish, S.J., Shannak, K., Hornykiewicz, O. (1988).
    "Uneven pattern of dopamine loss in the striatum of patients with
    idiopathic Parkinson's disease." *New England Journal of
    Medicine* 318:876–880. (Putamen dopaminergic loss is earlier and
    more severe than caudate loss in PD.)
*   **Dystonia (putamen):** Bhatia, K.P., Marsden, C.D. (1994). "The
    behavioural and motor consequences of focal lesions of the basal
    ganglia in man." *Brain* 117:859–876. (Putamen lesions and
    dystonia.)
*   **Substantia nigra (contrast — midbrain input):** Braak, H., et
    al. (2003). "Staging of brain pathology related to sporadic
    Parkinson's disease." *Neurobiology of Aging* 24:197–211.
    (Substantia nigra as the source of dopaminergic input to the
    putamen; the substantia nigra is a midbrain structure, not a
    putamen child.)
*   **Globus pallidus GPe/GPi gap (contrast — documented gap):**
    DeLong, M.R., Wichmann, T. (2007). "Circuits and circuit disorders
    of the basal ganglia." *Archives of Neurology* 64:20–24. (GPe/GPi
    as the putamen's output targets; the GPe/GPi are a documented gap
    in the parent `globus_pallidus` container.)
*   **Internal capsule (contrast — white matter):** Nieuwenhuys, R.,
    Voogd, J., van Huijzen, C. (2008). *The Human Central Nervous
    System*, 4th ed. (Internal capsule separating the putamen from the
    caudate and globus pallidus; the internal capsule is white matter,
    not a putamen child.)
*   **Hemiballismus (contrast — STN, not putamen):** Whittier, J.R.,
    Mettler, F.A. (1949). "Studies on the subthalamus of the rhesus
    monkey." *Journal of Comparative Neurology* 90:281–317.
    (Hemiballismus is caused by STN lesions, not putamen lesions —
    contrast reference.)
*   **Putamen vascular lesions:** Kase, C.S., Mohr, J.P. (1986).
    "Hypertensive intracerebral hemorrhage." In *Stroke:
    Pathophysiology, Diagnosis, and Management* (Barnett, H.J.M., et
    al., eds.). (Putamen in the lenticulostriate territory; putamen
    infarcts and hemorrhages.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical
    pathway to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association does
    **not** apply to the putamen — the putamen has **no
    extended-amygdala relationship**.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Putamen in overview.)
*   NeuroNames — Putamen (right); FMA — Putamen (right member).
"""