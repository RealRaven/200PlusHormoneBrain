"""
infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia.striatum
==============================================================================================================

Anatomical Hierarchy
--------------------
::

    telencephalon
    └── cerebral_hemispheres
        └── right
            └── subcortical
                └── basal_ganglia
                    └── striatum   <-- THIS MODULE
                        ├── dorsal_striatum
                        │   ├── caudate_nucleus
                        │   └── putamen
                        └── ventral_striatum
                            ├── nucleus_accumbens
                            └── olfactory_tubercle

**Primary synonym:** Striatum; corpus striatum (classical — partial);
neostriatum (dorsal striatum — classical); "the striatum."
**Cytoarchitectonic designation:** **Not a Brodmann area.** A
**container node** — the parent of two striatal children
(``dorsal_striatum``, ``ventral_striatum``) and **four**
grandchildren (``caudate_nucleus``, ``putamen``,
``nucleus_accumbens``, ``olfactory_tubercle``).
**Part of:** The **basal ganglia** container — specifically, the
**input side** of the basal ganglia (with the **globus pallidus** as
the output side).
**Structural parent:** ``.../right/subcortical/basal_ganglia/`` →
**direct child** of the basal ganglia container.
**Structural children (two, closed set):**
``dorsal_striatum`` (→ ``caudate_nucleus``, ``putamen``) and
``ventral_striatum`` (→ ``nucleus_accumbens``, ``olfactory_tubercle``).
**Boundary status (deep four-level container — the DEEPEST fully-wired
branch in the subcortical tree):** **Boundary case — a FOUR-level
container with BOTH branches fully wired, unlike its sibling
`globus_pallidus` (which has a documented dorsal gap).** The
striatum's deepest branch is
``striatum/dorsal_striatum/caudate_nucleus/`` (three levels from the
basal ganglia container, four from the subcortical container). Unlike
the globus pallidus, **both** the dorsal and ventral branches are
**fully wired** — there is **no documented structural gap** at this
container. Consumers must be prepared to **recurse to four levels**
(``subcortical/basal_ganglia/striatum/dorsal_striatum/caudate_nucleus/``
and
``subcortical/basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/``).
**Boundary status (not a single functional system — dorsal/ventral
split):** **Boundary case — the striatum is a structural grouping of
functionally distinct DORSAL and VENTRAL subsystems, not a single
functional system.** The two children have **different functions**:
*   **``dorsal_striatum``** (caudate + putamen) — **motor,
    cognitive, and associative**. Part of the
    **cortico-striato-pallido-thalamo-cortical** motor/cognitive
    loop. **Parkinson's disease** (dorsal striatal dopaminergic
    loss), **Huntington's disease** (dorsal striatum degeneration),
    **dystonia** (dorsal striatum dysfunction).
*   **``ventral_striatum``** (nucleus accumbens + olfactory tubercle)
    — **limbic, reward, motivation, and olfactory**. Part of the
    **ventral striatopallidal** limbic/reward loop. **Addiction**
    (nucleus accumbens), **depression** (nucleus accumbens),
    **olfactory dysfunction** (olfactory tubercle).
Consumers must **not** treat "striatum" as a single functional
system — it is a **structural grouping** of **dorsal and ventral**
subsystems with **different roles**.
**Boundary status (not the globus pallidus — sibling):** **Boundary
case — the globus pallidus is a SIBLING under the basal ganglia, not
a parent or child.** The **striatum** is the **input** structure;
the **globus pallidus** is the **output** structure. They are
**structurally separate** and **functionally complementary**. The
tree wires them as **siblings** under ``.../basal_ganglia/``.
Consumers that need the **input** structure resolve **this module**;
consumers that need the **output** structure resolve
``.../globus_pallidus/``. They are **not** parent and child — they
are **two halves** of the basal ganglia circuit.
**Boundary status (the olfactory tubercle is HERE — the FIFTH and
FINAL rhinencephalon-excluded structure):** **Boundary case — the
olfactory tubercle is a CHILD of `ventral_striatum/`, not of the
rhinencephalon or the basal forebrain.** The **olfactory tubercle**
— a **primary olfactory cortical target** on the **anterior
perforated substance** — is classically rhinencephalic. The tree
**excludes** it from the rhinencephalon and places it **here**, under
the **ventral striatum** (because of its **striatal-like
cytoarchitecture**). This is the **fifth and final** rhinencephalon-
excluded structure. **All five** rhinencephalon-excluded structures
are now documented at their tree locations:
*   **Amygdala** → ``medial_temporal_lobe/amygdala/``
*   **Hippocampus** → ``medial_temporal_lobe/hippocampus/``
*   **Septal nuclei** → ``basal_forebrain/septal_nuclei/``
*   **Anterior perforated substance** →
    ``basal_forebrain/anterior_perforated_substance/``
*   **Olfactory tubercle** → **here**, under
    ``striatum/ventral_striatum/``
Consumers reconstructing the **classical full rhinencephalon** must
**union** the rhinencephalon with **all five** excluded structures —
**four** of which are documented in the **basal forebrain** or
**medial temporal lobe**, and **one** of which is **here**, in the
**basal ganglia** (specifically, under the **ventral striatum**).
**Boundary status (the nucleus accumbens is HERE — the reward
nucleus, with the INPUT-SIDE SLEA overlap):** **Boundary case — the
nucleus accumbens is a CHILD of `ventral_striatum/`, and it carries
the INPUT-SIDE SLEA overlap (matching the OUTPUT-SIDE overlap of the
ventral pallidum).** The **nucleus accumbens** — the **primary
reward nucleus of the ventral striatum** — is classically grouped
with the basal forebrain in some literature. The tree places it
**here**, under the **ventral striatum**. It is **part of the
sublenticular extended amygdala (SLEA)** in some classifications —
the **input-side SLEA overlap**, matching the **output-side overlap**
of the **ventral pallidum**. See *The Striatum / Extended Amygdala
Boundary* and *Lateralization Notes*.
**Boundary status (extended amygdala overlap — DEFERRED warning at
this level):** **Boundary case — the nucleus accumbens has the
INPUT-SIDE SLEA overlap, but it is a GRANDCHILD of the striatum
container (not a direct child), so the warning is DEFERRED at this
level.** The **basal ganglia container** *deferred* the warning
because the nucleus accumbens is a **grandchild**. The **striatum
container** is **one level deeper** than the basal ganglia container,
but the nucleus accumbens is still a **grandchild** (striatum →
ventral_striatum → nucleus_accumbens). **The warning remains
DEFERRED at this level** — no container-level warning, only a
**deferral note** in the Lateralization section. The **light warning**
belongs to the **ventral_striatum container** (the nucleus accumbens
is a **direct child** there), and the **full warning** belongs to the
**nucleus_accumbens leaf** (the structure **itself** has the SLEA
relationship). See *Lateralization Notes*.
**Boundary status (not the substantia nigra — midbrain input):**
**Boundary case — the substantia nigra is FUNCTIONALLY related to the
DORSAL striatum (dopaminergic input) but STRUCTURALLY separate
(midbrain).** The **substantia nigra** (pars compacta) provides
**dopaminergic input** to the **dorsal striatum** — the
**nigrostriatal pathway**. But the substantia nigra is a **midbrain**
structure, not a striatum child. Consumers must not resolve the
substantia nigra through the striatum, and must not treat the
striatum's dopaminergic input as intrinsic to the striatum. **The
striatum is the TARGET of the dopaminergic input; the substantia
nigra is the SOURCE.**
**Boundary status (not the VTA — midbrain input):** **Boundary
case — the VTA is FUNCTIONALLY related to the VENTRAL striatum
(dopaminergic input) but STRUCTURALLY separate (midbrain).** The
**ventral tegmental area (VTA)** provides **dopaminergic input** to
the **ventral striatum** (nucleus accumbens, olfactory tubercle) —
the **mesolimbic pathway**. But the VTA is a **midbrain** structure,
not a striatum child. Consumers must not resolve the VTA through the
striatum, and must not treat the ventral striatum's dopaminergic
input as intrinsic to the striatum. **The ventral striatum is the
TARGET of the mesolimbic input; the VTA is the SOURCE.**
**Boundary status (not the extended amygdala — SLEA classificatory
overlap, wired separately):** **Boundary case — the nucleus accumbens
is part of the SLEA in some classifications, but the tree wires it
under the ventral striatum, not the extended amygdala.** The
**extended amygdala** container (``.../extended_amygdala/``) includes
the **BNST** and the **central amygdaloid nucleus**; the **SLEA**
classification **adds** the **ventral pallidum** and parts of the
**nucleus accumbens**. The tree **splits** them — the nucleus
accumbens is here, under the **ventral striatum**. This is a
**deliberate boundary choice**. Consumers that need the **extended
amygdala** as a unit (per the SLEA classification) must **union**
``.../extended_amygdala/`` with
``.../striatum/ventral_striatum/nucleus_accumbens/`` and
``.../globus_pallidus/ventral_pallidum/`` — the tree does **not**
provide this union as a single path.

Overview
--------
The striatum is the **input side** of the basal ganglia — the
**GABAergic** structure that receives **cortical**, **thalamic**, and
**dopaminergic** input and projects to the **globus pallidus** (the
output side). Together with the **globus pallidus**, it forms the
**input-output circuit** of the basal ganglia:

*   **``striatum``** — the **input** structure (this module).
*   **``globus_pallidus``** — the **output** structure (sibling).

**The striatum has TWO functional subsystems** — the **dorsal** and
**ventral** striatum — and **both are fully wired**. This is its
**defining structural fact**:
*   **Dorsal striatum** (caudate + putamen) — **motor, cognitive, and
    associative**. Receives **cortical** and **thalamic** input and
    **dopaminergic** input from the **substantia nigra** (pars
    compacta). Projects to the **GPe** and **GPi** and to the
    **substantia nigra** (pars reticulata). **Fully wired** as
    ``dorsal_striatum/`` with children ``caudate_nucleus/`` and
    ``putamen/``.
*   **Ventral striatum** (nucleus accumbens + olfactory tubercle) —
    **limbic, reward, motivation, and olfactory**. Receives
    **limbic cortical** and **dopaminergic** input from the **VTA**
    (mesolimbic pathway). Projects to the **ventral pallidum**.
    **Fully wired** as ``ventral_striatum/`` with children
    ``nucleus_accumbens/`` and ``olfactory_tubercle/``.

**Both striatal subsystems are fully wired — there is NO documented
structural gap at this container.** This distinguishes the striatum
from its sibling **globus pallidus** (which has a **documented gap**
for the dorsal GPe/GPi segments). The striatum is the **only
basal ganglia child with all branches fully wired**.

**The striatum contains the FIFTH and FINAL rhinencephalon-excluded
structure — the olfactory tubercle.** The **olfactory tubercle** is
under ``ventral_striatum/``, alongside the **nucleus accumbens**.
This closes the **five-structure rhinencephalon-exclusion loop** —
all five excluded structures are now documented at their tree
locations.

**The striatum is the INPUT side of the basal ganglia's SLEA pair.**
The **nucleus accumbens** (a ventral striatum child) carries the
**input-side SLEA overlap**, matching the **output-side overlap** of
the **ventral pallidum**. The **basal ganglia's SLEA pair** is
therefore:
*   **Input side:** nucleus accumbens (under the ventral striatum).
*   **Output side:** ventral pallidum (under the globus pallidus).
Both are **wired under the basal ganglia**, both are **split from the
extended amygdala** by the tree, and both carry the **SLEA warning**
at their respective levels — **deferred** at the container level,
**light** at the intermediate container level, and **full** at the
leaf level.

**The striatum is a paired structure.** Each hemisphere has its own
striatum, with **ipsilateral** cortical, thalamic, and dopaminergic
input. The two sides are **bilaterally symmetric** and **largely
non-lateralized** — the dorsal striatum's motor/cognitive functions
and the ventral striatum's reward/olfactory functions are
**bilateral**. Some **subtle lateralization** has been reported
(left caudate for language, right caudate for spatial), but it is
**weak** and **not a strong classification basis**. See
*Lateralization Notes*.

Container Contents (two children, four grandchildren, closed set)
------------------------------------------------------------------
The striatum container has **exactly two children** and **four
grandchildren**:

*   **``dorsal_striatum``** — the **dorsal** (motor/cognitive/
    associative) striatum. **Children:** ``caudate_nucleus``,
    ``putamen``. **Depth: three levels** from the striatum
    container (four levels from the subcortical container). The
    dorsal striatum is the **canonical "neostriatum"** — the
    structure that degenerates in **Huntington's disease** and
    receives **dopaminergic input** from the **substantia nigra**
    in **Parkinson's disease**.

*   **``ventral_striatum``** — the **ventral** (limbic/reward/
    olfactory) striatum. **Children:** ``nucleus_accumbens``,
    ``olfactory_tubercle``. **Depth: three levels** from the
    striatum container (four levels from the subcortical container).
    The ventral striatum is the **limbic/reward** subsystem — the
    target of the **mesolimbic pathway** (VTA → nucleus accumbens)
    and the location of the **olfactory tubercle** (the fifth
    rhinencephalon-excluded structure).

**Not children (deliberately excluded):**
*   **Globus pallidus** — ``.../basal_ganglia/globus_pallidus/`` —
    **sibling** (output structure).
*   **Substantia nigra** — ``.../midbrain/tegmentum/substantia_nigra/``
    — **midbrain** (dopaminergic input to the **dorsal** striatum;
    functionally related, structurally separate).
*   **VTA** — ``.../midbrain/tegmentum/ventral_tegmental_area/`` —
    **midbrain** (dopaminergic input to the **ventral** striatum;
    functionally related, structurally separate).
*   **Extended amygdala** — ``.../extended_amygdala/`` — **sibling**
    of the basal forebrain, not a child of the striatum. The nucleus
    accumbens is a **classificatory overlap** with the extended
    amygdala (SLEA), but the tree **splits** them.
*   **Amygdala** — ``.../medial_temporal_lobe/amygdala/`` —
    **sibling** of the subcortical container, not a child of the
    striatum. The amygdala has **strong functional connections** to
    the ventral striatum, but it is **structurally separate**.

The Striatum / Globus Pallidus Boundary
---------------------------------------
This is the **input-output** boundary of the basal ganglia:

*   **Striatum** (this module) — the **input** structure (dorsal:
    caudate, putamen; ventral: nucleus accumbens, olfactory
    tubercle). **Sibling**.

*   **Globus pallidus** (``.../globus_pallidus/``) — the **output**
    structure (dorsal: GPe, GPi — a **documented gap**; ventral:
    ventral pallidum — **wired**). **Sibling**.

**They are siblings under the basal ganglia container.** The
**cortico-striato-pallido-thalamo-cortical loop** connects them: the
**striatum** is the **first** relay (cortical input), and the
**globus pallidus** is the **second** relay (thalamic output).
Consumers that need the **input** structure resolve **this module**;
consumers that need the **output** structure resolve
``.../globus_pallidus/``.

**A note on the asymmetry between the two siblings:** the **striatum**
has **both branches fully wired**, while the **globus pallidus** has a
**documented dorsal gap** (the GPe/GPi are **not wired**). This
asymmetry is a **deliberate structural choice** in the tree — the
striatum subtree is **complete**, while the globus pallidus subtree is
**partial** (only the ventral pallidum is wired).

The Striatum / Extended Amygdala Boundary
-----------------------------------------
This is the **SLEA** boundary — the **deferred warning**:

*   **Extended amygdala** (``.../extended_amygdala/``) — the **BNST**
    and the **central amygdaloid nucleus**. **Classically** the
    extended amygdala; **SLEA** adds the **ventral pallidum** and
    parts of the **nucleus accumbens**.

*   **Striatum** (this module) — the **nucleus accumbens** (a
    **ventral striatum** child) is part of the **SLEA**
    classification. The **olfactory tubercle** (also a **ventral
    striatum** child) is **NOT** part of the SLEA — it is the
    **fifth rhinencephalon-excluded structure**, but **not** an
    extended-amygdala component.

**The tree splits them.** The **nucleus accumbens** is under
``.../striatum/ventral_striatum/nucleus_accumbens/``, and the
**ventral pallidum** is under
``.../globus_pallidus/ventral_pallidum/`` — **not** under the extended
amygdala. This is a **deliberate boundary choice**. Consumers that
need the **extended amygdala** as a unit (per the SLEA classification)
must **union** ``.../extended_amygdala/`` with the **nucleus
accumbens** and **ventral pallidum** — the tree does **not** provide
this union as a single path.

**The striatum container carries a DEFERRED warning**: the **nucleus
accumbens is a GRANDCHILD** (striatum → ventral_striatum →
nucleus_accumbens), not a **direct child**, so the warning is **not
container-wide** at this level. The **light warning** belongs to the
**ventral_striatum container** (the nucleus accumbens is a **direct
child** there), and the **full warning** belongs to the
**nucleus_accumbens leaf** (the structure **itself** has the SLEA
relationship). **The warning gradient** from the striatum side
mirrors the gradient from the globus pallidus side:
*   **Basal ganglia container** — *deferred* (both SLEA structures are
    grandchildren).
*   **Striatum container** — *deferred* (the nucleus accumbens is a
    grandchild).
*   **Ventral striatum container** — *light* (the nucleus accumbens is
    a direct child).
*   **Nucleus accumbens leaf** — *full*.

The Striatum / Midbrain Boundary
--------------------------------
This is the **dopaminergic input** boundary:

*   **Substantia nigra** —
    ``.../midbrain/tegmentum/substantia_nigra/`` — the **dopaminergic**
    (pars compacta) and **GABAergic** (pars reticulata) **midbrain**
    nucleus. Its **pars compacta** provides **dopaminergic input to
    the DORSAL striatum** — the **nigrostriatal pathway**. Its
    **pars reticulata** receives **striatal output** from the
    **dorsal striatum** (the **striatonigral** projection). **The
    nigrostriatal pathway is the major dopaminergic input to the
    dorsal striatum** — its degeneration in **Parkinson's disease**
    is the **signature clinical association** of the dorsal
    striatum.

*   **Ventral tegmental area (VTA)** —
    ``.../midbrain/tegmentum/ventral_tegmental_area/`` — the
    **dopaminergic** midbrain nucleus that projects to the **VENTRAL
    striatum** (nucleus accumbens) — the **mesolimbic pathway**. The
    **mesolimbic pathway** is the **major dopaminergic input to the
    ventral striatum** — its dysregulation in **addiction** is the
    **signature clinical association** of the ventral striatum.

**The substantia nigra and VTA are NOT striatum children.** They are
**midbrain** structures — functionally related (dopaminergic input to
the striatum) but structurally separate. Consumers must not resolve
them through the striatum, and must not treat the striatum's
dopaminergic input as intrinsic to the striatum. **The striatum is
the TARGET; the substantia nigra and VTA are the SOURCES.**

The Striatum / Rhinencephalon Boundary
--------------------------------------
This is the **fifth and final** rhinencephalon-excluded structure
boundary:

*   **Rhinencephalon** (``.../right/rhinencephalon/``) — the **narrow
    olfactory definition** (bulb, tract, AON, piriform, periamygdaloid,
    uncus). The **olfactory tubercle** is **excluded** from this
    definition.

*   **Striatum** (this module) — the **olfactory tubercle** is under
    ``.../striatum/ventral_striatum/olfactory_tubercle/``. It is a
    **primary olfactory cortical target** with **striatal-like
    cytoarchitecture** — a **deliberate boundary choice** reflecting
    its **striatal identity** over its **olfactory identity**.

**The full rhinencephalon-exclusion set (all five now documented):**

| Excluded structure | Tree location | Documentation status |
|---|---|---|
| Amygdala | `medial_temporal_lobe/amygdala/` | (not yet written at leaf level) |
| Hippocampus | `medial_temporal_lobe/hippocampus/` | (not yet written at leaf level) |
| Septal nuclei | `basal_forebrain/septal_nuclei/` | ✓ (left + right) |
| Anterior perforated substance | `basal_forebrain/anterior_perforated_substance/` | ✓ (left + right) |
| **Olfactory tubercle** | **`basal_ganglia/striatum/ventral_striatum/olfactory_tubercle/`** | **This module (container-level redirect)** |

**Consumers reconstructing the classical full rhinencephalon** must
union the rhinencephalon with **all five** excluded structures —
**four** of which are documented in the **basal forebrain** or
**medial temporal lobe**, and **one** of which is **here**, in the
**basal ganglia** (specifically, under the **ventral striatum**).

Function in the Human Brain
---------------------------
The striatum has **two functionally distinct subsystems**, both
**fully wired**:

**Dorsal striatum (caudate + putamen — wired as `dorsal_striatum/`):**

*   **Motor Control and Action Selection (Putamen Function):** The
    **putamen** is the **sensorimotor** striatum — it receives
    **sensorimotor cortical** input and projects to the **GPi** and
    **GPe**. It is involved in **action selection, movement
    initiation, and motor learning** — its **dopaminergic
    denervation** in **Parkinson's disease** produces
    **bradykinesia, rigidity, and tremor**.

*   **Cognitive and Associative Functions (Caudate Function):** The
    **caudate** is the **associative/cognitive** striatum — it
    receives **prefrontal** and **parietal** input and is involved
    in **working memory, cognitive control, and goal-directed
    behavior**. Its **degeneration** in **Huntington's disease**
    produces **cognitive and psychiatric symptoms** alongside
    **chorea**.

*   **Habit Learning (Dorsal Striatum Function):** The **dorsal
    striatum** is the substrate for **habit learning** — the
    **gradual shift** from **goal-directed** to **habitual**
    behavior. Its **dopaminergic input** from the **substantia
    nigra** is essential for this **reinforcement learning**.

**Ventral striatum (nucleus accumbens + olfactory tubercle — wired as
`ventral_striatum/`):**

*   **Reward and Motivation (Nucleus Accumbens Function):** The
    **nucleus accumbens** is the **primary reward nucleus** of the
    ventral striatum — it receives **dopaminergic input** from the
    **VTA** (mesolimbic pathway) and **limbic cortical** input. It is
    involved in **reward prediction, motivation, and reinforcement
    learning** — its **dysfunction** is the **signature** of
    **addiction**.

*   **Olfactory Function (Olfactory Tubercle Function):** The
    **olfactory tubercle** is a **primary olfactory cortical
    target** — it receives **lateral olfactory stria** input and
    **projects to the ventral pallidum** (as part of the ventral
    striatum). It is involved in **olfactory-reward association** —
    the **integration of smell with reward**.

*   **Limbic-Motor Interface (Ventral Striatum Function):** The
    **ventral striatum** is the **limbic-motor interface** — it
    receives **limbic** input and projects to the **ventral
    pallidum**, which then **gates** reward-related behavior. This
    is the **anatomical substrate** for **motivated behavior** — the
    **translation of motivation into action**.

**The unifying theme:** the striatum is the **input side** of the
basal ganglia — the **dorsal** subsystem is **motor/cognitive** (via
the substantia nigra → dorsal striatum → globus pallidus loop), and
the **ventral** subsystem is **limbic/reward** (via the VTA → ventral
striatum → ventral pallidum loop). **Both subsystems are fully wired**
in the tree — the striatum is the **only basal ganglia child with all
branches fully wired**.

Associated Disorders
--------------------
The striatum container has **no single syndrome** — its children's
disorders are documented in their own modules:

*   **Dorsal striatum (caudate + putamen):**
    - **Parkinson's disease** — **dorsal striatal dopaminergic loss**
      (substantia nigra → putamen), producing **bradykinesia,
      rigidity, and tremor**.
    - **Huntington's disease** — **dorsal striatum degeneration**
      (especially the caudate), producing **chorea, cognitive
      decline, and psychiatric symptoms**.
    - **Dystonia** — **dorsal striatum dysfunction** (often
      dopa-responsive in children), producing **sustained muscle
      contractions and abnormal postures**.
    - **Tourette syndrome** — **caudate dysfunction**, producing
      **tics**.

*   **Ventral striatum (nucleus accumbens + olfactory tubercle):**
    - **Addiction** — **nucleus accumbens dysfunction** (mesolimbic
      pathway dysregulation), producing **craving, compulsive
      drug-seeking, and relapse**.
    - **Depression** — **nucleus accumbens dysfunction**, producing
      **anhedonia and motivation deficits**.
    - **OCD** — **ventral striatum dysfunction** (cortico-striato-
      thalamo-cortical loop), producing **obsessions and
      compulsions**.
    - **Olfactory dysfunction** — **olfactory tubercle involvement**
      in **anosmia, hyposmia, or olfactory agnosia**.

*   **Container-level:** **no single syndrome** — the striatum is a
  **structural grouping**, and its disorders are the **aggregate** of
  its children's disorders.

**What is NOT here:** The striatum is **not** the substrate for
**Alzheimer's disease** (nucleus basalis — basal forebrain),
**basal forebrain amnesia** (septum/DBB), **Kluver-Bucy syndrome**
(amygdala — medial temporal lobe), or **temporal lobe epilepsy**
(hippocampus). Its clinical footprint is **motor/cognitive** (dorsal
— Parkinson's, Huntington's, dystonia) and **limbic/reward/
olfactory** (ventral — addiction, depression, OCD, olfactory
dysfunction) — a **distinct category** from the basal forebrain's
**cholinergic-cognitive** footprint.

Lateralization Notes
--------------------
This is the **right** striatum container. The striatum is **bilaterally
symmetric** and **largely non-lateralized** — but the **deferred
warning** from the basal ganglia container applies at this level:

*   **Bilateral Motor/Cognitive Functions (Dorsal):** Each dorsal
    striatum projects **ipsilaterally** to the globus pallidus and
    substantia nigra. The two sides are **functionally symmetric**
    for motor and cognitive functions. **Parkinson's** and
    **Huntington's** are **bilateral** (though often **asymmetric**
    in presentation).

*   **Bilateral Limbic/Reward/Olfactory Functions (Ventral):** Each
    ventral striatum projects **ipsilaterally** to the ventral
    pallidum. The two sides are **functionally symmetric** for
    reward, motivation, and olfaction. **Addiction** and
    **depression** are **bilateral** in the ventral striatum.

*   **No Established Lateralized Syndrome:** Unlike BA22 (left
    Wernicke's), BA37 (left VWFA / right FFA), or BA38 (left semantic
    / right social), the striatum has **no documented strong
    left-lateralized or right-lateralized function**. **Parkinson's**
    and **Huntington's** are **bilateral** (though often asymmetric);
    **addiction** and **depression** are **bilateral** in the ventral
    striatum.

*   **Weak Lateralization (Contested — Dorsal Striatum):** The
    **dorsal striatum** (caudate) has been reported to show **subtle**
    lateralization — **left caudate** for **language** (via the
    cortico-striatal loop), **right caudate** for **spatial
    navigation**. This is **weak** and **contested**, documented in
    the **striatum** module (this module) as prose, not as a strong
    classification basis. **On the right side**, the **right
    caudate's spatial-memory association** is the weaker of the two
    lateralization claims — it is **not** a strong basis for
    container-level classification. **The weak lateralization is NOT
    a rationale for a prose asymmetry** — the striatum container is a
    **strict mirror** at the structural level.

*   **Extended Amygdala Overlap (DEFERRED WARNING — at container
    level):** The **nucleus accumbens** (a ventral striatum child) is
    part of the **SLEA** in some classifications. The **nucleus
    accumbens is a GRANDCHILD** of the striatum container (striatum →
    ventral_striatum → nucleus_accumbens), so the **warning is
    DEFERRED at this level** — no container-level warning, only a
    **deferral note**. The **light warning** belongs to the
    **ventral_striatum container** (the nucleus accumbens is a
    **direct child** there), and the **full warning** belongs to the
    **nucleus_accumbens leaf** (the structure **itself** has the
    SLEA relationship). **The olfactory tubercle** (the other ventral
    striatum child) is **NOT** part of the SLEA — it is the **fifth
    rhinencephalon-excluded structure**, but **not** an
    extended-amygdala component.

*   **Right-amygdala fear association (contrast — not this module):**
    The **right amygdala's fear association** belongs to the
    **amygdala module** and (weakly via SLEA) to the **extended
    amygdala module** — **not** to the striatum container, **not** to
    the dorsal striatum (which has **no amygdala relationship**), and
    **not** to the ventral striatum (which contains the nucleus
    accumbens, but the nucleus accumbens's SLEA relationship is
    handled at the **ventral striatum container** and **nucleus
    accumbens leaf** levels). **This is especially important for
    this right-side module** — the right nucleus accumbens is
    **downstream of** the container, and the right amygdala's
    fear-processing association belongs to the **amygdala module**
    and the **extended amygdala module**, **not** to the container
    that contains the right nucleus accumbens. The container itself
    carries **no warning**.

**A consumer that assumes "right striatum = left striatum" will be
structurally and functionally correct** — the two sides are
**largely symmetric**, no **strong** lateralized syndrome has been
demonstrated, and the **weak** lateralization reported for the dorsal
striatum is **contested**, not a strong classification basis. The
striatum container is a **strict-mirror pair with a deferred warning**
— matching the **basal ganglia container**, because the nucleus
accumbens is a **grandchild** here (the warning is **deferred** to
the **ventral_striatum container** and **nucleus_accumbens leaf**).
**The right-side module keeps the warning deferred** — no dedicated
Usage block, no emphatic contrast reference, only a **deferral note**
in the Lateralization section — matching the deferred-warning pattern
established by the basal ganglia container pair.

Design Contract
---------------
*   **No side effects on import.** Pure namespace.
*   **No cross-hemisphere imports.** Right side only.
*   **No cross-lobe imports.** This module does **not** import from
    ``.../midbrain/``, ``.../extended_amygdala/``, or any other
    container. The striatum's relationships to the substantia nigra,
    VTA, and extended amygdala are documented as **prose and boundary
    data**, not as structural parents or children.
*   **No hormone imports.** Dependency DAG unchanged:
    ``chemicals_hormones → memory → brainparts``.
*   **Container node — two children, four grandchildren, closed set.**
    The striatum container has exactly two children
    (``dorsal_striatum``, ``ventral_striatum``) and four
    grandchildren (``caudate_nucleus``, ``putamen``,
    ``nucleus_accumbens``, ``olfactory_tubercle``). Consumers may
    iterate them, but should not assume any others exist.
*   **Deep four-level container — prepared to recurse.** The
    striatum's deepest branch is
    ``striatum/dorsal_striatum/caudate_nucleus/`` (three levels from
    the striatum container, four from the subcortical container).
    Consumers must be prepared to **recurse to four levels**.
*   **BOTH branches fully wired — no documented gap.** Unlike its
    sibling ``globus_pallidus`` (which has a **dorsal GPe/GPi gap**),
    the striatum has **both branches fully wired** — the **only
    basal ganglia child with all branches complete**.
*   **Dorsal/ventral functional split.** The **dorsal striatum**
    (caudate + putamen) is **motor/cognitive/associative**; the
    **ventral striatum** (nucleus accumbens + olfactory tubercle) is
    **limbic/reward/olfactory**. Consumers must not treat "striatum"
    as a single functional system.
*   **The olfactory tubercle is HERE — the FIFTH and FINAL
    rhinencephalon-excluded structure.** This is the **last of the
    five** — **all five** are now documented at their tree locations.
    Consumers reconstructing the **classical full rhinencephalon**
    must **union** the rhinencephalon with the **striatum container**
    (specifically, the olfactory tubercle).
*   **The nucleus accumbens is HERE — the INPUT-SIDE SLEA overlap.**
    The nucleus accumbens carries the **input-side SLEA overlap**,
    matching the **output-side overlap** of the **ventral pallidum**.
    The **basal ganglia's SLEA pair** is now **both sides
    identified**.
*   **Extended amygdala overlap — DEFERRED warning at this level.**
    The **nucleus accumbens is a GRANDCHILD** of the striatum
    container (striatum → ventral_striatum → nucleus_accumbens), so
    the warning is **DEFERRED at this level** — no container-level
    warning, only a **deferral note**. The **light warning** belongs
    to the **ventral_striatum container**; the **full warning**
    belongs to the **nucleus_accumbens leaf**. **The olfactory
    tubercle is NOT part of the SLEA** — it is the fifth
    rhinencephalon-excluded structure, but not an extended-amygdala
    component. **The right-side module keeps the warning deferred** —
    matching the basal ganglia container pair — because the nucleus
    accumbens is **downstream of** the container, and the right
    amygdala's fear association belongs to the **amygdala module** and
    the **extended amygdala module**, **not** here.
*   **Not the substantia nigra or VTA — midbrain inputs.** The
    substantia nigra provides dopaminergic input to the **dorsal**
    striatum (nigrostriatal pathway); the VTA provides dopaminergic
    input to the **ventral** striatum (mesolimbic pathway). Both are
    **midbrain** structures, not striatum children.
*   **Not the globus pallidus — sibling.** The globus pallidus is the
    **output** structure; the striatum is the **input** structure.
    They are **siblings** under the basal ganglia.
*   **No ``AREA_PATHS`` hop.** The striatum is a local container under
    the basal ganglia, not a cross-listed leaf.
*   **No nested cross-listing.** The striatum has no nested
    dual-framing module. It is a single container.
*   **Structural parity with left striatum — strict mirror with a
    deferred warning.** Right and left striatum modules are
    **structurally identical** — same two children, same four
    grandchildren, same four-level recursion, same
    olfactory-tubercle redirect (the fifth rhinencephalon-excluded
    structure), same deferred-warning treatment. **The deferred
    warning tracks the anatomy** — the nucleus accumbens is a
    grandchild, so the warning is deferred at this level, matching
    the basal ganglia container. **The right-side module keeps the
    warning deferred** — no dedicated Usage block, no emphatic
    contrast reference, only a **deferral note** in the Lateralization
    section.

Usage
-----
Resolve by path::

    from infrastructure.brainparts.forebrain.telencephalon.cerebral_hemispheres.right.subcortical.basal_ganglia import striatum

Or by fully-qualified path string::

    path = (
        "telencephalon.cerebral_hemispheres.right.subcortical."
        "basal_ganglia.striatum"
    )

**Do not** assume the striatum is under ``basal_forebrain/``. It is
under ``basal_ganglia/`` — the **sibling** of the basal forebrain.
A consumer that iterates the basal forebrain and expects to find the
striatum there will **miss it**.

**Do not** assume the striatum is a **flat container**. It is a
**deep, four-level tree**. Consumers must be prepared to **recurse**.

**Do not** assume the striatum has a **documented structural gap**.
Unlike its sibling ``globus_pallidus`` (which has a **dorsal
GPe/GPi gap**), the striatum has **both branches fully wired**.

**Do not** assume the striatum **contains** the substantia nigra, VTA,
or extended amygdala. Those are **midbrain or extended amygdala**
structures, not striatum children.

**Do not** assume the striatum is a **single functional system**.
Its **dorsal** (motor/cognitive) and **ventral** (limbic/reward/
olfactory) subsystems are functionally distinct.

**Do not** import **right-amygdala lateralization claims** into the
striatum container. The **nucleus accumbens** (a ventral striatum
child) has **classificatory overlap** with the extended amygdala
(SLEA), but the warning is **DEFERRED at this container level** — the
**light warning** belongs to the **ventral_striatum container**, and
the **full warning** belongs to the **nucleus_accumbens leaf**. The
**olfactory tubercle** (the other ventral striatum child) is **not**
part of the SLEA. **This is especially important for this right-side
module** — the right nucleus accumbens is **downstream of** the
container, and the right amygdala's fear-processing association
belongs to the **amygdala module** and the **extended amygdala
module**, **not** to the container that contains the right nucleus
accumbens.

Iterating the striatum container's two children (recommended
consumer pattern)::

    STRIATUM_CHILDREN = (
        "dorsal_striatum",
        "ventral_striatum",
    )
    # Closed set. Do not assume additional children.

Iterating the striatum container's four grandchildren (recommended
consumer pattern)::

    STRIATUM_GRANDCHILDREN = {
        "dorsal_striatum": ("caudate_nucleus", "putamen"),
        "ventral_striatum": ("nucleus_accumbens", "olfactory_tubercle"),
    }
    # Closed set. Do not assume additional grandchildren.

Recursive iteration over the striatum tree (recommended consumer
pattern)::

    # The striatum is up to four levels deep. Recurse over it.
    #
    #   subcortical.basal_ganglia.striatum.dorsal_striatum.caudate_nucleus
    #
    # is a valid leaf; so is
    #
    #   subcortical.basal_ganglia.striatum.ventral_striatum.olfactory_tubercle
    #
    # Do not stop at the first level.

Reconstructing the classical full rhinencephalon (recommended
consumer pattern — the olfactory tubercle is the fifth and final
excluded structure)::

    # The rhinencephalon's narrow definition excludes five
    # structures that classical anatomy includes. The full union:
    CLASSICAL_FULL_RHINENCEPHALON = {
        "rhinencephalon": (),
        "subcortical": (
            "medial_temporal_lobe.amygdala",
            "medial_temporal_lobe.hippocampus",
            "basal_forebrain.septal_nuclei",
            "basal_forebrain.anterior_perforated_substance",
            "basal_ganglia.striatum.ventral_striatum.olfactory_tubercle",  # THIS MODULE
        ),
    }
    # ALL FIVE rhinencephalon-excluded structures are now documented
    # at their tree locations. The olfactory tubercle is the ONLY one
    # wired under the basal ganglia (specifically, the ventral
    # striatum).

Reaching the extended amygdala's SLEA components (recommended
consumer pattern — the SLEA union)::

    # The extended amygdala's SLEA classification includes the
    # nucleus accumbens (ventral striatum, this module) and the
    # ventral pallidum (globus pallidus). The tree splits them.
    # Consumers that need the SLEA grouping must union:
    #
    #   subcortical.extended_amygdala
    #   subcortical.basal_ganglia.striatum.ventral_striatum.nucleus_accumbens
    #   subcortical.basal_ganglia.globus_pallidus.ventral_pallidum
    #
    # The tree does not provide this union as a single path.

Reaching the substantia nigra (recommended consumer pattern — NOTE
the midbrain boundary)::

    # The substantia nigra is FUNCTIONALLY related to the DORSAL
    # striatum (dopaminergic input) but STRUCTURALLY separate
    # (midbrain):
    #
    #   midbrain.tegmentum.substantia_nigra
    #
    # The substantia nigra is the SOURCE of the dopaminergic input;
    # the dorsal striatum is the TARGET.

Reaching the VTA (recommended consumer pattern — NOTE the midbrain
boundary)::

    # The VTA is FUNCTIONALLY related to the VENTRAL striatum
    # (dopaminergic input, mesolimbic pathway) but STRUCTURALLY
    # separate (midbrain):
    #
    #   midbrain.tegmentum.ventral_tegmental_area
    #
    # The VTA is the SOURCE of the dopaminergic input; the ventral
    # striatum is the TARGET.

Bilateral iteration (recommended consumer pattern)::

    for side in ("left", "right"):
        stri_path = (
            f"telencephalon.cerebral_hemispheres.{side}.subcortical."
            f"basal_ganglia.striatum"
        )
        # resolve stri_path through the memory/recall layer

References
----------
*   **Canonical striatal anatomy:** Graybiel, A.M. (2008). "Habits,
    rituals, and the evaluative brain." *Annual Review of
    Neuroscience* 31:359–387. (Definitive functional overview;
    cortico-striato-pallido-thalamo-cortical loop; dorsal/ventral
    striatum.)
*   **Dorsal vs ventral striatum:** Voorn, P., Vanderschuren, L.J.,
    Groenewegen, H.J., Robbins, T.W., Pennartz, C.M. (2004). "Putting
    a spin on the dorsal-ventral divide of the striatum." *Trends in
    Neurosciences* 27:468–474. (Dorsal/ventral functional
    distinction.)
*   **Olfactory tubercle:** Heimer, L., Wilson, R.D. (1975). "The
    subcortical projections of the allocortex: similarities in the
    neural associations of the hippocampus, the piriform cortex, and
    the neocortex." In *Golgi Centennial Symposium* (Santini, M.,
    ed.). (Olfactory tubercle as a ventral striatum structure.)
*   **Nucleus accumbens:** Mogenson, G.J., Jones, D.L., Yim, C.Y.
    (1980). "From motivation to action: functional interface between
    the limbic system and the motor system." *Progress in
    Neurobiology* 14:69–97. (Nucleus accumbens as limbic-motor
    interface; ventral striatum.)
*   **Extended amygdala / SLEA:** Alheid, G.F., Heimer, L. (1988).
    "New perspectives in basal forebrain organization of special
    relevance for neuropsychiatric disorders." *Neuroscience*
    27:1–39. (SLEA; nucleus accumbens and ventral pallidum in the
    extended amygdala continuum.)
*   **Substantia nigra / nigrostriatal pathway (contrast):** Braak,
    H., et al. (2003). "Staging of brain pathology related to
    sporadic Parkinson's disease." *Neurobiology of Aging*
    24:197–211. (Substantia nigra as the source of dopaminergic input
    to the dorsal striatum; the substantia nigra is a midbrain
    structure, not a striatum child.)
*   **VTA / mesolimbic pathway (contrast):** Nestler, E.J. (2005).
    "Is there a common molecular pathway for addiction?" *Nature
    Neuroscience* 8:1445–1449. (VTA as the source of dopaminergic
    input to the ventral striatum; the VTA is a midbrain structure,
    not a striatum child.)
*   **Addiction:** Koob, G.F., Volkow, N.D. (2010). "Neurocircuitry
    of addiction." *Neuropsychopharmacology* 35:217–238. (Nucleus
    accumbens and ventral striatum in addiction.)
*   **Huntington's disease:** Vonsattel, J.P., DiFiglia, M. (1998).
    "Huntington disease." *Journal of Neuropathology and Experimental
    Neurology* 57:369–384. (Dorsal striatum degeneration.)
*   **Parkinson's disease:** Dauer, W., Przedborski, S. (2003).
    "Parkinson's disease: mechanisms and models." *Neuron*
    39:889–909. (Substantia nigra → dorsal striatum dopaminergic
    loss.)
*   **Dorsal striatum lateralization:** Ullman, M.T. (2004).
    "Contributions of memory circuits to language: the
    declarative/procedural model." *Cognition* 92:231–270. (Left
    caudate in language; procedural memory.)
*   **Right caudate spatial memory (contrast):** Postle, B.R.,
    D'Esposito, M. (1999). "Dissociation of human caudate nucleus
    activity during spatial and verbal working memory." *Cognitive
    Brain Research* 7:571–580. (Right caudate and spatial working
    memory; weak, contested lateralization.)
*   **Right amygdala lateralization (contrast — amygdala proper, not
    this module):** Morris, J.S., Öhman, A., Dolan, R.J. (1998). "A
    subcortical pathway to the right amygdala mediating 'unseen'
    fear." *PNAS* 96:1680–1685. (Right amygdala and fear; the
    association does **not** apply to the striatum container — the
    right nucleus accumbens's SLEA relationship is deferred to the
    right ventral striatum container and the right nucleus accumbens
    leaf.)
*   Brodal, A. (2010). *The Central Nervous System: Structure and
    Function*, 4th ed. (Striatum in overview.)
*   NeuroNames — Striatum (right); FMA — Striatum (right member).
"""