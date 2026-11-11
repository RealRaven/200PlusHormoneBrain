"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.striatum.dorsal_striatum
==============================================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_ganglia
                    └── striatum
                        └── dorsal_striatum   <-- THIS MODULE
                            ├── caudate_nucleus
                            └── putamen

**Primary synonym:** Dorsal striatum; neostriatum (classical); corpus
striatum (classical — partial, before the globus pallidus was
separated); striatum proper (in older usage).
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container node** — the parent of two dorsal striatum children
(``caudate_nucleus``, ``putamen``).
**Part of:** The **striatum** container — specifically, the
**DORSAL** (motor/cognitive/associative) half. The other half is the
**ventral striatum** (limbic/reward/olfactory).
**Structural parent:** ``.../right/subcortical/basal_ganglia/striatum/``
→ **direct child** of the striatum container.
**Structural children (two, closed set):**
``caudate_nucleus`` and ``putamen``. Both are **fully wired leaves**
(no further children).
**Boundary status (the DORSAL half of the striatum — NOT the ventral
striatum):** **Boundary case — the dorsal striatum is the
MOTOR/COGNITIVE/ASSOCIATIVE subsystem; the VENTRAL striatum is the
LIMBIC/REWARD/OLFACTORY subsystem.** The two halves are **siblings**
under the striatum container, **anatomically separate** (dorsal vs.
ventral), and **functionally distinct** (motor/cognitive vs. limbic/
reward/olfactory). The **dorsal striatum** is the **canonical
"neostriatum"** — the structure that degenerates in **Huntington's
disease**, receives **dopaminergic input** from the **substantia
nigra** in **Parkinson's disease**, and is the target of **dystonia**
and **Tourette syndrome** pathophysiology. The **ventral striatum** is
the **limbic/reward** half — the structure involved in **addiction**,
**depression**, and **OCD** (and the location of the **olfactory
tubercle**). Consumers must **not** conflate the two — they are
**different striatal subsystems** with **different inputs**, **different
outputs**, and **different clinical associations**.
**Boundary status (the caudate/putamen split — both children are
leaves):** **Boundary case — the dorsal striatum's two children
(caudate and putamen) are FUNCTIONALLY DISTINCT but ANATOMICALLY
CONTINUOUS.** The **caudate nucleus** and the **putamen** are the two
**classical subdivisions** of the dorsal striatum. They are
**separated** by the **internal capsule** (the **anterior limb**
separates the caudate head from the putamen; the **posterior limb**
separates the caudate body from the putamen), but they are
**cytoarchitecturally continuous** around the **anterior** and
**inferior** margins of the internal capsule. The tree wires them as
**two separate leaves** — a **deliberate boundary choice** reflecting
their **functional distinction** (caudate: cognitive/associative;
putamen: motor/sensorimotor) and their **clinical distinction**
(Huntington's affects the caudate most; Parkinson's affects the
putamen most). Consumers must **not** treat the caudate and putamen as
**interchangeable** — they are **functionally distinct** dorsal
striatum components, **even though** they are **cytoarchitecturally
continuous** in the intact brain.
**Boundary status (NO extended-amygdala relationship — this is the
motor/cognitive half):** **Boundary case — the dorsal striatum has
NO extended-amygdala relationship, NO SLEA overlap, and NO
amygdala-lateralization warning.** The **extended amygdala (SLEA)**
overlap belongs to the **ventral striatum** (via the **nucleus
accumbens**) and the **ventral pallidum** — **not** to the dorsal
striatum. The dorsal striatum is the **motor/cognitive** subsystem;
the SLEA is a **limbic** continuum. Consumers must **not** import
amygdala-lateralization claims into the dorsal striatum — **there is
no anatomical relationship** to support them. **The warning gradient
that runs through the ventral striatum and nucleus accumbens does
NOT apply to this module** — the dorsal striatum is a **strict
mirror with no warning**.
**Boundary status (not the ventral striatum — sibling):** **Boundary
case — the ventral striatum is a SIBLING under the striatum
container, not a child or parent of the dorsal striatum.** The
**ventral striatum** (nucleus accumbens + olfactory tubercle) is the
**limbic/reward/olfactory** half; the **dorsal striatum** (caudate +
putamen) is the **motor/cognitive** half. They are **structurally
separate** (dorsal vs. ventral) and **functionally distinct**.
Consumers that need the **limbic/reward/olfactory** subsystem resolve
``.../ventral_striatum/``; consumers that need the **motor/cognitive**
subsystem resolve **this module**.
**Boundary status (not the globus pallidus — the dorsal GPe/GPi are a
DOCUMENTED GAP in the sibling container):** **Boundary case — the
globus pallidus is a SIBLING of the striatum (under the basal
ganglia), and its DORSAL segments (GPe, GPi) are the DORSAL
STRIATUM'S OUTPUT TARGETS but are a DOCUMENTED GAP in the
`globus_pallidus` container.** The **dorsal striatum** projects to the
**GPe** and **GPi** — the **indirect pathway** (striatum → GPe → STN
→ GPi → thalamus) and the **direct pathway** (striatum → GPi →
thalamus). But the **GPe and GPi are NOT wired** in the tree — they
are a **documented structural gap** in the **parent** `globus_pallidus`
container (which wires only the **ventral pallidum**). **This gap is
especially consequential here**, because the **dorsal striatum's
entire output** goes to the **unwired GPe/GPi** — the **striatum is
wired**, but its **output targets are not**. Consumers that need the
**dorsal striatum's output** must resolve the GPe/GPi functions as
**prose** in the **parent** `globus_pallidus` module, **not** here and
**not** as structural children. Consumers must also be aware that the
**dorsal striatum → GPe/GPi** circuit is the **motor circuit** that
is disrupted in **Parkinson's disease** and **dystonia** — the
**unwired GPe/GPi** are the **anatomical substrate** of the **motor
symptoms**.
**Boundary status (not the substantia nigra — midbrain dopaminergic
INPUT):** **Boundary case — the substantia nigra is the
DOPAMINERGIC INPUT to the dorsal striatum, but it is a MIDBRAIN
structure, not a dorsal striatum child.** The **substantia nigra
(pars compacta)** provides **dopaminergic input** to the **dorsal
striatum** — the **nigrostriatal pathway**. Its **degeneration** in
**Parkinson's disease** is the **signature clinical association** of
the dorsal striatum. But the **substantia nigra** is under
``.../midbrain/tegmentum/substantia_nigra/`` — **not** under the
dorsal striatum. Consumers must **not** resolve the substantia nigra
through the dorsal striatum, and must **not** treat the dorsal
striatum's dopaminergic input as intrinsic to the dorsal striatum.
**The dorsal striatum is the TARGET; the substantia nigra is the
SOURCE.**
**Boundary status (not the subthalamic nucleus — diencephalic
indirect-pathway relay):** **Boundary case — the subthalamic nucleus
(STN) is part of the INDIRECT PATHWAY that the dorsal striatum feeds
into, but it is a DIENCEPHALIC structure, not a dorsal striatum
child.** The **indirect pathway** is: dorsal striatum → GPe → **STN**
→ GPi → thalamus. The **STN** is under
``.../diencephalon/subthalamus/subthalamic_nucleus/`` — **not** under
the dorsal striatum. Its **overactivity** contributes to
**Parkinson's disease** motor symptoms, and it is a **different
surgical target** from the GPi (**STN DBS** vs. **GPi
pallidotomy/DBS**). Consumers must **not** resolve the STN through
the dorsal striatum.
**Boundary status (not the internal capsule — white matter, not a
dorsal striatum child):** **Boundary case — the internal capsule
SEPARATES the caudate from the putamen, but it is WHITE MATTER, not a
dorsal striatum child.** The **anterior limb** of the internal
capsule separates the **caudate head** from the **putamen**; the
**posterior limb** separates the **caudate body** from the
**putamen**. The **internal capsule** is under
``.../right/white_matter/`` — **not** a dorsal striatum child.
Consumers must **not** resolve the internal capsule through the
dorsal striatum.
**Boundary status (not a single functional system — caudate/putamen
functional split):** **Boundary case — the dorsal striatum is a
structural grouping of two functionally distinct nuclei (caudate and
putamen), not a single functional system.** The **caudate** is
**cognitive/associative**; the **putamen** is **motor/sensorimotor**.
Consumers must **not** treat "dorsal striatum" as a single functional
system — it is a **structural grouping** of **two functionally
distinct** nuclei, and its **clinical associations** differ by
subnucleus (**Huntington's** — caudate; **Parkinson's** — putamen).

Overview
--------
The dorsal striatum is the **motor/cognitive half** of the striatum —
the **canonical "neostriatum"** — and the **input** structure of the
**motor/cognitive basal ganglia circuit**. It contains **two
children** — the **caudate nucleus** (cognitive/associative) and the
**putamen** (motor/sensorimotor) — both **fully wired leaves**. The
dorsal striatum is the **structure that degenerates in Huntington's
disease** (caudate), **receives dopaminergic input from the substantia
nigra** in **Parkinson's disease** (putamen), and is the target of
**dystonia** and **Tourette syndrome** pathophysiology.

**The dorsal striatum is the canonical "neostriatum."** In classical
anatomy, the **neostriatum** is the **caudate + putamen** — the
**phylogenetically newer** part of the striatum (compared with the
**paleostriatum** = globus pallidus). The tree uses the **modern**
term **"dorsal striatum"** for the same structure, which is preferred
because it **parallels** the **"ventral striatum"** (nucleus
accumbens + olfactory tubercle). The **dorsal/ventral** framing is
**functional and anatomical** — the two halves have **different
inputs** (cortical vs. limbic), **different outputs** (GPe/GPi vs.
ventral pallidum), and **different clinical associations**
(motor/cognitive vs. limbic/reward/olfactory).

**The dorsal striatum has TWO functionally distinct children** — the
**caudate nucleus** and the **putamen** — both **fully wired leaves**.
The **caudate** is the **cognitive/associative** striatum; the
**putamen** is the **motor/sensorimotor** striatum. They are
**cytoarchitecturally continuous** around the **anterior** and
**inferior** margins of the internal capsule, but the tree wires them
as **two separate leaves** — a **deliberate boundary choice**
reflecting their **functional distinction** and their **clinical
distinction**.

**The dorsal striatum's OUTPUT goes to the GPe/GPi — which are a
documented gap in the sibling `globus_pallidus` container.** This is
the **most consequential boundary fact** in the module: the **dorsal
striatum is wired**, but its **output targets** (the **GPe** and
**GPi**) are **not**. The **dorsal striatum → GPe/GPi** circuit is
the **motor circuit** disrupted in **Parkinson's disease** and
**dystonia** — the **unwired GPe/GPi** are the **anatomical
substrate** of the **motor symptoms**. Consumers that need the
**dorsal striatum's output** must resolve the GPe/GPi functions as
**prose** in the **parent** `globus_pallidus` module.

**The dorsal striatum has NO extended-amygdala relationship.** The
**SLEA overlap** belongs to the **ventral striatum** (via the **nucleus
accumbens**) and the **ventral pallidum** — **not** to the dorsal
striatum. **The warning gradient that runs through the ventral
striatum and nucleus accumbens does NOT apply to this module** — the
dorsal striatum is a **strict mirror with no warning**. This is a
**deliberate structural fact** — the **dorsal** (motor/cognitive) and
**ventral** (limbic/reward) subsystems are **anatomically separate**,
and the **extended amygdala continuum** touches **only the ventral
side**.

**The dorsal striatum is a paired structure.** Each hemisphere has its
own dorsal striatum, with **ipsilateral** cortical, thalamic, and
dopaminergic input. The two sides are **bilaterally symmetric** and
**largely non-lateralized** — the motor (putamen) and cognitive
(caudate) functions are **bilateral**. Some **subtle lateralization**
has been reported (left caudate for language, right caudate for
spatial), but it is **weak** and **contested**. See *Lateralization
Notes*.

Container Contents (two children, closed set)
----------------------------------------------
The dorsal striatum container has **exactly two children** — both
**fully wired leaves**:

*   **``caudate_nucleus``** — the **cognitive/associative** dorsal
    striatum. **Depth: leaf (no children).** Receives **prefrontal**
    and **parietal** cortical input and is involved in **working
    memory, cognitive control, and goal-directed behavior**. Its
    **degeneration** in **Huntington's disease** produces
    **cognitive and psychiatric symptoms** alongside **chorea**. Its
    **dysfunction** in **Tourette syndrome** produces **tics**.

*   **``putamen``** — the **motor/sensorimotor** dorsal striatum.
    **Depth: leaf (no children).** Receives **sensorimotor cortical**
    input and projects to the **GPe** and **GPi**. It is involved in
    **action selection, movement initiation, and motor learning** —
    its **dopaminergic denervation** in **Parkinson's disease**
    produces **bradykinesia, rigidity, and tremor**. Its
    **dysfunction** in **dystonia** produces **sustained muscle
    contractions and abnormal postures**.

**Not children (deliberately excluded):**
*   **Ventral striatum** — ``.../striatum/ventral_striatum/`` —
    **sibling** (limbic/reward/olfactory half).
*   **Globus pallidus** — ``.../basal_ganglia/globus_pallidus/`` —
    **sibling** of the striatum container (the **output side**;
    its **dorsal GPe/GPi are a documented gap**).
*   **Substantia nigra** — ``.../midbrain/tegmentum/substantia_nigra/``
    — **midbrain** (dopaminergic **input** to the dorsal striatum).
*   **Subthalamic nucleus** — ``.../diencephalon/subthalamus/subthalamic_nucleus/``
    — **diencephalic** (indirect pathway relay, **downstream** of the
    dorsal striatum).
*   **Internal capsule** — ``.../right/white_matter/`` — **white
    matter** (separates the caudate from the putamen).

The Dorsal Striatum / Ventral Striatum Boundary
-----------------------------------------------
This is the **most consequential boundary** in the module:

*   **Dorsal striatum** (this module) — the **motor/cognitive/
    associative** subsystem (caudate + putamen). **Canonical
    "neostriatum."** Projects to the **GPe/GPi** (a **documented gap**).

*   **Ventral striatum** (``.../striatum/ventral_striatum/``) — the
    **limbic/reward/olfactory** subsystem (nucleus accumbens +
    olfactory tubercle). **SLEA-bearing half.** Projects to the
    **ventral pallidum** (wired).

**They are siblings under the striatum container.** The **dorsal**
half is **motor/cognitive**; the **ventral** half is **limbic/reward/
olfactory**. Consumers that need the **motor/cognitive** subsystem
resolve **this module**; consumers that need the **limbic/reward/
olfactory** subsystem resolve ``.../ventral_striatum/``.

**A note on the SLEA asymmetry between the two siblings:** the
**ventral striatum** contains the **nucleus accumbens** (an
**SLEA-bearing** structure) — so the **ventral striatum's** children
carry the **SLEA warning**. The **dorsal striatum** contains the
**caudate** and **putamen** — **neither** of which is **SLEA-bearing**
— so **the dorsal striatum's children carry NO SLEA warning**. This is
a **deliberate structural fact** — the **extended amygdala continuum**
touches **only the ventral side** of the striatum.

The Dorsal Striatum / Globus Pallidus Boundary
----------------------------------------------
This is the **output-target** boundary — **especially consequential
because the output targets are a documented gap**:

*   **Dorsal striatum** (this module) — the **input** structure
    (caudate + putamen). **Wired**.

*   **Globus pallidus** (``.../basal_ganglia/globus_pallidus/``) —
    the **output** structure. Its **dorsal segments** (GPe, GPi) are
    the **dorsal striatum's output targets**, but they are **NOT
    wired** — a **documented gap** in the parent `globus_pallidus`
    container. Only the **ventral pallidum** is wired.

**The dorsal striatum → GPe/GPi circuit is the motor circuit.** The
**direct pathway** (striatum → GPi → thalamus) and the **indirect
pathway** (striatum → GPe → STN → GPi → thalamus) both go through the
**GPe/GPi** — which are **not wired**. The **unwired GPe/GPi** are
the **anatomical substrate** of the **motor symptoms** of
**Parkinson's disease** and **dystonia**.

**Consumers that need the dorsal striatum's output** must resolve the
GPe/GPi functions as **prose** in the **parent** `globus_pallidus`
module — **not** here, and **not** as structural children. The
**dorsal striatum's output targets are a documented gap** in the
sibling container.

The Dorsal Striatum / Substantia Nigra Boundary
-----------------------------------------------
This is the **dopaminergic input** boundary:

*   **Substantia nigra** —
    ``.../midbrain/tegmentum/substantia_nigra/`` — the **dopaminergic**
    (pars compacta) and **GABAergic** (pars reticulata) **midbrain**
    nucleus. Its **pars compacta** provides **dopaminergic input to
    the DORSAL striatum** — the **nigrostriatal pathway**. Its
    **pars reticulata** receives **striatal output** from the
    **dorsal striatum** (the **striatonigral** projection).

*   **Dorsal striatum** (this module) — the **dopaminergic TARGET**
    (via the nigrostriatal pathway). **Telencephalic**.

**The substantia nigra is NOT a dorsal striatum child.** It is a
**midbrain** structure — functionally related (dopaminergic input to
the dorsal striatum) but structurally separate. Consumers must **not**
resolve the substantia nigra through the dorsal striatum, and must
**not** treat the dorsal striatum's dopaminergic input as intrinsic to
the dorsal striatum. **The dorsal striatum is the TARGET; the
substantia nigra is the SOURCE.**

The Dorsal Striatum / Subthalamic Nucleus Boundary
--------------------------------------------------
This is the **indirect-pathway** boundary:

*   **Subthalamic nucleus (STN)** —
    ``.../diencephalon/subthalamus/subthalamic_nucleus/`` — the
    **diencephalic** relay of the **indirect pathway**. The indirect
    pathway is: **dorsal striatum → GPe → STN → GPi → thalamus**. The
    STN is **downstream** of the dorsal striatum (via the GPe).

*   **Dorsal striatum** (this module) — the **indirect pathway
    ORIGIN**. **Telencephalic**.

**The STN is NOT a dorsal striatum child.** It is a **diencephalic**
structure — functionally related (part of the same indirect pathway)
but structurally separate. Consumers must **not** resolve the STN
through the dorsal striatum.

The Dorsal Striatum / Internal Capsule Boundary
-----------------------------------------------
This is the **white-matter separation** boundary:

*   **Internal capsule** — ``.../right/white_matter/`` — the
    **white-matter tract** that **separates** the **caudate** from
    the **putamen**:
    *   **Anterior limb** — separates the **caudate head** from the
        **putamen**.
    *   **Posterior limb** — separates the **caudate body** from the
        **putamen**.

*   **Dorsal striatum** (this module) — the **grey-matter structures**
    (caudate + putamen) that the internal capsule **passes between**.

**The internal capsule is NOT a dorsal striatum child.** It is
**white matter** under ``.../right/white_matter/`` — **not** a dorsal
striatum component. The **caudate and putamen are cytoarchitecturally
continuous** around the **anterior** and **inferior** margins of the
internal capsule — the separation is **partial**, not complete. But
the tree wires them as **two separate leaves**, and the internal
capsule is **documented as the separator** — a **prose** fact, not a
structural child.

Function in the Human Brain
---------------------------
The dorsal striatum has **two functionally distinct children**:

**Caudate nucleus (cognitive/associative):**

*   **Working Memory and Cognitive Control:** The **caudate** receives
    **prefrontal** and **parietal** cortical input and is involved in
    **working memory, cognitive control, and goal-directed behavior**.
    Its **dysfunction** produces **cognitive and psychiatric
    symptoms** — the **cognitive/psychiatric** component of
    **Huntington's disease**.

*   **Goal-Directed Behavior:** The **caudate** (with the **ventral
    striatum**) is involved in **goal-directed behavior** — the
    **flexible, outcome-based** selection of actions. Its
    **dysfunction** contributes to the **cognitive rigidity** of
    **Huntington's disease** and the **tics** of **Tourette
    syndrome**.

*   **Language (Left Caudate — Contested):** The **left caudate** has
    been reported to participate in **language** (via the
    **cortico-striatal loop**), contributing to **procedural language
    processing** — but this is **weak**, **contested**, and **not a
    strong basis for classification** (see *Lateralization Notes*).
    **On the right side**, the **right caudate** is **not** the
    language-lateralized structure — its **spatial-memory**
    association is the weaker of the two lateralization claims.

**Putamen (motor/sensorimotor):**

*   **Action Selection and Movement Initiation:** The **putamen**
    receives **sensorimotor cortical** input and is involved in
    **action selection, movement initiation, and motor learning**. Its
    **dopaminergic denervation** in **Parkinson's disease** produces
    **bradykinesia, rigidity, and tremor** — the **signature motor
    symptoms** of PD.

*   **Habit Learning:** The **putamen** (with the **caudate**) is
    involved in **habit learning** — the **gradual shift** from
    **goal-directed** to **habitual** behavior. Its **dopaminergic
    input** from the **substantia nigra** is essential for this
    **reinforcement learning**.

*   **Dystonia:** The **putamen** is **dysfunctional** in **dystonia**
    — producing **sustained muscle contractions and abnormal
    postures**. **Dystonia** is often **dopa-responsive** (in
    children) — the **putamen's** dopaminergic signaling is the
    **therapeutic target**.

**The unifying theme:** the dorsal striatum is the **input side** of
the **motor/cognitive basal ganglia circuit** — the **caudate** is
**cognitive/associative** (working memory, cognitive control,
goal-directed behavior), and the **putamen** is **motor/sensorimotor**
(action selection, movement initiation, habit learning). **Both
children are fully wired**, but their **output targets** (the
**GPe/GPi**) are a **documented gap** in the sibling `globus_pallidus`
container.

Associated Disorders
--------------------
The dorsal striatum container has **no single syndrome** — its
children's disorders are documented in their own modules:

*   **Caudate nucleus (cognitive/associative):**
    - **Huntington's disease** — **caudate degeneration** (especially
      the **caudate head**), producing **chorea, cognitive decline,
      and psychiatric symptoms**. The **caudate** is the **most
      affected** striatal structure in HD.
    - **Tourette syndrome** — **caudate dysfunction**, producing
      **tics** (motor and vocal).
    - **OCD** — **caudate dysfunction** (with the ventral striatum),
      contributing to **obsessions and compulsions**.
    - **Cognitive impairment** — **caudate dysfunction** contributes
      to **working memory** and **executive function** deficits in
      **neurodegenerative disease**.

*   **Putamen (motor/sensorimotor):**
    - **Parkinson's disease** — **putamen dopaminergic denervation**
      (substantia nigra → putamen), producing **bradykinesia,
      rigidity, and tremor**. The **putamen** is the **most affected**
      striatal structure in PD.
    - **Dystonia** — **putamen dysfunction**, producing **sustained
      muscle contractions and abnormal postures**. Often
      **dopa-responsive** in children.
    - **Habit learning deficits** — **putamen dysfunction** impairs
      **habit formation** (with the **caudate**), contributing to
      **procedural learning** deficits.

*   **Container-level:** **no single syndrome** — the dorsal striatum
  is a **structural grouping**, and its disorders are the **aggregate**
  of its children's disorders.

**What is NOT here:** The dorsal striatum is **not** the substrate for
**Alzheimer's disease** (nucleus basalis), **basal forebrain amnesia**
(septum/DBB), **Kluver-Bucy syndrome** (amygdala), **temporal lobe
epilepsy** (hippocampus), **addiction** (nucleus accumbens — ventral
striatum), or **depression** (nucleus accumbens — ventral striatum).
Its clinical footprint is **motor** (putamen) and **cognitive/
psychiatric** (caudate) — a **distinct category** from the **ventral
striatum's** **limbic/reward** footprint.

Lateralization Notes
--------------------
This is the **right** dorsal striatum container. The dorsal striatum is
**bilaterally symmetric** and **largely non-lateralized** — **and it
carries NO extended-amygdala warning**:

*   **Bilateral Motor Functions (Putamen):** Each putamen projects
    **ipsilaterally** to the GPe/GPi. The two sides are **functionally
    symmetric** for motor functions. **Parkinson's disease** is
    **bilateral** (though often **asymmetric** in presentation) —
    **bradykinesia and rigidity** are typically **bilateral**.

*   **Bilateral Cognitive Functions (Caudate):** Each caudate projects
    **ipsilaterally** to the GPe/GPi. The two sides are **functionally
    symmetric** for cognitive functions. **Huntington's disease** is
    **bilateral** — the **caudate degeneration** is **bilateral**.

*   **Weak Lateralization (Contested — Caudate):** The **caudate** has
    been reported to show **subtle** lateralization — **left caudate**
    for **language** (via the cortico-striatal loop), **right caudate**
    for **spatial navigation**. This is **weak** and **contested**,
    documented as **prose**, not as a strong classification basis.
    **On the right side**, the **right caudate's spatial-memory
    association** is the weaker of the two lateralization claims —
    it is **not** a strong basis for container-level classification.
    **The weak lateralization is NOT a rationale for a prose
    asymmetry** — the dorsal striatum container is a **strict mirror**
    at the structural level.

*   **NO Extended-Amygdala Warning (strict mirror with no warning):**
    The dorsal striatum has **NO extended-amygdala relationship**, **NO
    SLEA overlap**, and **NO amygdala-lateralization warning**. The
    **SLEA overlap** belongs to the **ventral striatum** (via the
    **nucleus accumbens**) and the **ventral pallidum** — **not** to
    the dorsal striatum. Consumers must **not** import
    amygdala-lateralization claims into the dorsal striatum — **there
    is no anatomical relationship** to support them. **The warning
    gradient that runs through the ventral striatum and nucleus
    accumbens does NOT apply to this module** — the dorsal striatum is
    a **strict mirror with no warning**, matching the **basal ganglia
    container** and the **globus pallidus container** at their
    respective levels. **The right-side module carries the same
    no-warning status** — no dedicated Usage block, no contrast
    reference, no deferral note. **The dorsal striatum has no
    amygdala-adjacent structure** at any level of its subtree — the
    caudate and putamen are **not** SLEA-bearing, and **no warning
    applies**.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module** — **not** to the dorsal striatum, **not** to the
    caudate, and **not** to the putamen. **The dorsal striatum has no
    anatomical relationship to the amygdala** — the **SLEA overlap** is
    a **ventral striatum** fact, and it **does not transfer** to the
    dorsal striatum. **This is true on the right side as well** — the
    right caudate and right putamen are **not** SLEA-bearing, and the
    right amygdala's fear-processing association **does not** apply to
    them.

**A consumer that assumes "right dorsal striatum = left dorsal
striatum" will be structurally and functionally correct** — the two
sides are **largely symmetric**, no **strong** lateralized syndrome
has been demonstrated, and the **weak** lateralization reported for
the caudate is **contested**, not a strong classification basis. The
dorsal striatum container is a **strict-mirror pair with no warning**
— matching the **basal ganglia container** and the **globus pallidus
container** at their respective levels. **This is the FIRST
striatum-side container with NO warning** — the warning gradient runs
**only through the ventral side** of the striatum. **The right-side
module carries the same no-warning status** — no dedicated Usage
block, no contrast reference, no deferral note.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../diencephalon/``, or any other container.
    The dorsal striatum's relationships to the substantia nigra,
    subthalamic nucleus, and globus pallidus are documented as **prose
    and boundary data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — two children, closed set.** The dorsal striatum
    container has exactly two children: ``caudate_nucleus`` and
    ``putamen``. Both are **fully wired leaves** — there is **no
    documented gap** at this container.
*   **Dorsal half of the striatum — NOT the ventral striatum.** The
    **dorsal striatum** is the **motor/cognitive/associative** half;
    the **ventral striatum** is the **limbic/reward/olfactory** half.
    Consumers must not conflate the two — they are **different
    striatal subsystems**.
*   **Caudate/putamen split — both children are leaves.** The
    **caudate** (cognitive/associative) and **putamen** (motor/
    sensorimotor) are **functionally distinct** but **cytoarchitecturally
    continuous**. The tree wires them as **two separate leaves** — a
    **deliberate boundary choice** reflecting their functional and
    clinical distinction.
*   **NO extended-amygdala warning — strict mirror with no warning.**
    The dorsal striatum has **NO SLEA overlap**, **NO amygdala
    relationship**, and **NO amygdala-lateralization warning**. The
    **SLEA warning** belongs to the **ventral striatum** (nucleus
    accumbens) and the **ventral pallidum** — **not** here. **This is
    the first striatum-side container with NO warning** — the warning
    gradient runs **only through the ventral side** of the striatum.
    **The right-side module carries the same no-warning status** — no
    dedicated Usage block, no contrast reference, no deferral note.
*   **The GPe/GPi are a documented gap — the dorsal striatum's output
    targets are NOT wired.** The **dorsal striatum** projects to the
    **GPe** and **GPi**, but those are a **documented gap** in the
    **parent** `globus_pallidus` container. Consumers that need the
    dorsal striatum's output must resolve the GPe/GPi functions as
    **prose** in the parent `globus_pallidus` module.
*   **Not the substantia nigra — midbrain input.** The substantia
    nigra provides dopaminergic input to the dorsal striatum
    (nigrostriatal pathway). It is a **midbrain** structure, not a
    dorsal striatum child.
*   **Not the subthalamic nucleus — diencephalic indirect-pathway
    relay.** The STN is **downstream** of the dorsal striatum (via the
    GPe). It is a **diencephalic** structure, not a dorsal striatum
    child.
*   **Not the internal capsule — white matter.** The internal capsule
    **separates** the caudate from the putamen, but it is **white
    matter** under ``.../right/white_matter/`` — **not** a dorsal
    striatum child.
*   **Not a single functional system — caudate/putamen split.** The
    **caudate** (cognitive) and **putamen** (motor) are **functionally
    distinct**. Consumers must not treat "dorsal striatum" as a single
    functional system.
*   **No ``AREA_PATHS`` hop.** The dorsal striatum is a local container
    under the striatum, not a cross-listed leaf.
*   **No nested cross-listing.** The dorsal striatum has no nested
    dual-framing module. It is a single container.
*   **Structural parity with left dorsal striatum — strict mirror
    with NO warning.** Right and left dorsal striatum modules are
    **structurally identical** — same two children, same caudate/
    putamen split, same GPe/GPi documented-gap note, same substantia
    nigra input note, same **no extended-amygdala warning**. **The
    dorsal striatum is the first striatum-side container with NO
    warning** — the warning gradient runs **only through the ventral
    side**. **The right-side module carries the same no-warning
    status** — no dedicated Usage block, no contrast reference, no
    deferral note.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.striatum import dorsal_striatum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_ganglia.striatum.dorsal_striatum"
    )

**Do not** assume the dorsal striatum is the **ventral striatum**. The
**dorsal** half is **motor/cognitive** (caudate + putamen); the
**ventral** half is **limbic/reward/olfactory** (nucleus accumbens +
olfactory tubercle). They are **different striatal subsystems**.

**Do not** assume the dorsal striatum is a **single functional
system**. Its **caudate** (cognitive) and **putamen** (motor) are
**functionally distinct**.

**Do not** assume the dorsal striatum has a **documented structural
gap**. Unlike its sibling `globus_pallidus` (which has a dorsal
GPe/GPi gap), the dorsal striatum has **both children fully wired** —
there is **no gap** at this container.

**Do not** assume the dorsal striatum **contains** the GPe/GPi. Those
are the **output targets** of the dorsal striatum, but they are a
**documented gap** in the **parent** `globus_pallidus` container. They
are **not** dorsal striatum children.

**Do not** assume the dorsal striatum **contains** the substantia
nigra or subthalamic nucleus. Those are **midbrain** and
**diencephalic** structures — functionally related but structurally
separate.

**Do not** import **amygdala-lateralization claims** into the dorsal
striatum. **The dorsal striatum has NO extended-amygdala
relationship** — the SLEA overlap belongs to the **ventral striatum**
and **ventral pallidum**. **This is the FIRST striatum-side container
with NO warning** — the warning gradient runs **only through the
ventral side** of the striatum. **The right-side module carries the
same no-warning status** — the right caudate and right putamen are
**not** SLEA-bearing, and the right amygdala's fear-processing
association **does not** apply to them.

Iterating the dorsal striatum container's two children (recommended
consumer pattern)::

    DORSAL_STRIATUM_CHILDREN = (
        "caudate_nucleus",
        "putamen",
    )
    # Closed set. Both children are fully wired leaves.

Iterating the dorsal striatum's children's functions (recommended
consumer pattern)::

    DORSAL_STRIATUM_FUNCTIONS = {
        "caudate_nucleus": ("cognitive", "associative", "working_memory"),
        "putamen": ("motor", "sensorimotor", "habit_learning"),
    }
    # The caudate/putamen split reflects their functional distinction.

Reaching the dorsal striatum's output targets (recommended consumer
pattern — NOTE the GAP)::

    # The dorsal striatum projects to the GPe and GPi (the output
    # targets). But the GPe and GPi are a DOCUMENTED GAP in the
    # parent `globus_pallidus` container — they are NOT wired.
    #
    # Resolve:
    #
    #   subcortical.basal_ganglia.globus_pallidus
    #     -> parent module's "Dorsal Segment Gap" section
    #
    # Do NOT attempt to resolve a "gpe" or "gpi" path.

Reaching the substantia nigra (recommended consumer pattern — NOTE
the midbrain boundary)::

    # The substantia nigra provides dopaminergic input to the dorsal
    # striatum (nigrostriatal pathway). It is a MIDBRAIN structure,
    # not a dorsal striatum child:
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # The substantia nigra is the SOURCE; the dorsal striatum is the
    # TARGET.

Reaching the subthalamic nucleus (recommended consumer pattern —
NOTE the diencephalon boundary)::

    # The subthalamic nucleus is part of the indirect pathway
    # (downstream of the dorsal striatum, via the GPe). It is a
    # DIENCEPHALIC structure, not a dorsal striatum child:
    #
    #   diencephalon.subthalamus.subthalamic_nucleus
    #
    # Do NOT resolve the STN through the dorsal striatum.

Reaching the internal capsule (recommended consumer pattern — NOTE
the white-matter boundary)::

    # The internal capsule separates the caudate from the putamen,
    # but it is WHITE MATTER, not a dorsal striatum child:
    #
    #   white_matter.internal_capsule
    #
    # Do NOT resolve the internal capsule through the dorsal striatum.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        ds_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.striatum.dorsal_striatum"
        )
        # resolve ds_path through the memory/recall layer

References
----------
*   **Canonical dorsal striatum anatomy:** Graybiel, A.M. (2008).
    "Habits, rituals, and the evaluative brain." *Annual Review of
    Neuroscience* 31:359–387. (Definitive functional overview;
    caudate/putamen distinction; dorsal striatum in habit learning.)
*   **Caudate/putamen functional distinction:** Alexander, G.E.,
    DeLong, M.R., Strick, P.L. (1986). "Parallel organization of
    functionally segregated circuits linking basal ganglia and
    cortex." *Annual Review of Neuroscience* 9:357–381. (Parallel
    cortico-striatal loops; caudate → cognitive, putamen → motor.)
*   **Huntington's disease (caudate):** Vonsattel, J.P., DiFiglia, M.
    (1998). "Huntington disease." *Journal of Neuropathology and
    Experimental Neurology* 57:369–384. (Caudate degeneration in HD;
    the caudate is the most affected striatal structure.)
*   **Parkinson's disease (putamen):** Dauer, W., Przedborski, S.
    (2003). "Parkinson's disease: mechanisms and models." *Neuron*
    39:889–909. (Substantia nigra → putamen dopaminergic loss; the
    putamen is the most affected striatal structure.)
*   **Dystonia (putamen):** Bhatia, K.P., Marsden, C.D. (1994). "The
    behavioural and motor consequences of focal lesions of the basal
    ganglia in man." *Brain* 117:859–876. (Putamen lesions and
    dystonia.)
*   **Tourette syndrome (caudate):** Leckman, J.F., et al. (2010).
    "Tourette syndrome: the self under siege." *Journal of Child
    Neurology* 25:1155–1162. (Caudate dysfunction in Tourette
    syndrome.)
*   **Substantia nigra (contrast — midbrain input):** Braak, H., et
    al. (2003). "Staging of brain pathology related to sporadic
    Parkinson's disease." *Neurobiology of Aging* 24:197–211.
    (Substantia nigra as the source of dopaminergic input to the
    dorsal striatum; the substantia nigra is a midbrain structure,
    not a dorsal striatum child.)
*   **Subthalamic nucleus (contrast — diencephalic relay):** Bergman,
    H., Wichmann, T., DeLong, M.R. (1990). "Reversal of experimental
    parkinsonism by lesions of the subthalamic nucleus." *Science*
    249:1436–1438. (STN in the indirect pathway; the STN is
    diencephalic, not a dorsal striatum child.)
*   **Globus pallidus GPe/GPi gap (contrast — documented gap):**
    DeLong, M.R., Wichmann, T. (2007). "Circuits and circuit disorders
    of the basal ganglia." *Archives of Neurology* 64:20–24. (GPe/GPi
    as the dorsal striatum's output targets; the GPe/GPi are a
    documented gap in the parent `globus_pallidus` container.)
*   **Internal capsule (contrast — white matter):** Nieuwenhuys, R.,
    Voogd, J., van Huijzen, C. (2008). *The Human Central Nervous
    System*, 4th ed. (Internal capsule separating the caudate from
    the putamen; the internal capsule is white matter, not a dorsal
    striatum child.)
*   **Dorsal striatum lateralization (caudate — weak, contested):**
    Ullman, M.T. (2004). "Contributions of memory circuits to
    language: the declarative/procedural model." *Cognition*
    92:231–270. (Left caudate in language; procedural memory.)
*   **Right caudate spatial memory (contrast):** Postle, B.R.,
    D'Esposito, M. (1999). "Dissociation of human caudate nucleus
    activity during spatial and verbal working memory." *Cognitive
    Brain Research* 7:571–580. (Right caudate and spatial working
    memory; weak, contested lateralization — **contrast reference**,
    not a strong basis for container-level classification.)
*   **Right amygdala lateralization (contrast — NOT this module):**
    Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A subcortical
    pathway to the right amygdala mediating 'unseen' fear." *PNAS*
    96:1680–1685. (Right amygdala and fear; the association does
    **not** apply to the dorsal striatum — the dorsal striatum has
    **no extended-amygdala relationship**, and the SLEA warning is a
    **ventral striatum / ventral pallidum** fact. The right caudate
    and right putamen are **not** SLEA-bearing.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Dorsal striatum in overview.)
*   NeuroNames — Dorsal striatum (right); FMA — Dorsal striatum
    (right member).
"""